# -*- coding: utf-8 -*-
"""card_lint.py — linter dùng chung cho thẻ Anki của MỌI chuyên khoa.

Ánh xạ gate → mã lỗi: xem `Bai hoc y khoa/RULES_LESSON_APKG.md` §5.

Nhóm lỗi:
  T_*  kỹ thuật (HTML/escape/LaTeX/cấu trúc)  — luôn BLOCK
  P_*  back-purity (nguồn trong mặt sau)      — luôn BLOCK
  D_*  deck (section, tên deck, media, dấu)    — luôn BLOCK
  G_*  governance (Basic-first, anti-spoiler, 🎯/💡, màu, ⚡) — BLOCK ở `release`, DEBT ở `hotfix`
  W_*  cảnh báo — không chặn

CLI:
  python card_lint.py --scan-apkg <dir> [--mode release|hotfix]   # báo cáo nợ cho APKG đã build
  python card_lint.py --apkg <file.apkg> [--mode ...]              # chi tiết 1 APKG
Exit: 0 = không BLOCK, 2 = có BLOCK.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sqlite3
import sys
import tempfile
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

PALETTE = ("#ff6b6b", "#ffd43b", "#51cf66", "#74c0fc")
ALGO_BADGE = "⚡ THUẬT TOÁN QUYẾT ĐỊNH"
ALGO_MIN = 3
MAX_IMAGE_BYTES = 150 * 1024
MAX_IMAGE_WIDTH = 1200
DIACRITICS_MIN = 0.80
sys.path.insert(0, str(Path(__file__).resolve().parent))
import specialties  # noqa: E402
from specialties import VN_DIACRITIC_RE  # noqa: E402,F401  (dùng lại ở test/công cụ khác)

_HTML_TAGS = r"(?:b|br|i|u|em|strong|span|div|hr|img|sup|sub|ul|ol|li|table|thead|tbody|tr|td|th|p|font|small|code)"
ESCAPED_TAG_RE = re.compile(r"&lt;/?" + _HTML_TAGS + r"(?=[\s>/&]|$)", re.I)
DOUBLE_ESCAPE_RE = re.compile(r"&amp;(?:lt|gt|amp|nbsp|quot);|<[a-zA-Z][^<>]*&gt;")
CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0b-\x1f]|\t")  # gồm \r: "\rightarrow" trong string thường → CR + "ightarrow"
LATEX_RE = re.compile(
    r"\$|\\(?:rightarrow|leftarrow|Rightarrow|to|times|cdot|geq?|leq?|neq|approx|pm|mu|alpha|beta|gamma|delta|Delta|"
    r"text|frac|sqrt|mathrm|mathbf|longrightarrow|uparrow|downarrow|circ|%)(?![a-zA-Z])"
    r"|\\[^\x00-\x7f]"
    r"|(?<![a-zA-Z])(?:ightarrow|ext\{|imes\b|eftarrow)"  # tàn dư sau khi \r, \t, \b bị Python nuốt
)
BACK_SOURCE_RE = re.compile(
    r"trang\s*\d+|giáo\s*trình|văn\s*bản\s*gốc|nguồn\s*:|\bpmid\b|\bch\.\s*\d+|\bchương\s+\d+|\bmục\s+(?:[ivx]+|\d+)(?:[.\s,)]|$)",
    re.I,
)
CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)\}\}", re.S)
IMG_RE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*[\"']?([^\"'\s>]+)", re.I)
TAG_RE = re.compile(r"<[^>]+>")
GOVERNANCE_PREFIX = "G_"


@dataclass
class Issue:
    code: str
    card_id: str
    message: str
    severity: str = ""  # BLOCK | DEBT | WARN (gán bởi classify)

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------- helpers
def strip_html(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAG_RE.sub(" ", text or ""))).strip()


def norm_key(text: str) -> str:
    return re.sub(r"[^\w]+", " ", strip_html(text).lower()).strip()


def card_kind(card: dict) -> str:
    kind = (card.get("type") or "").lower()
    if kind not in {"basic", "cloze"}:
        kind = "cloze" if "text" in card and "front" not in card else "basic"
    return kind


def card_fields(card: dict) -> dict[str, str]:
    """Các field nội dung người học nhìn thấy (để kiểm kỹ thuật)."""
    keys = ("text", "extra") if card_kind(card) == "cloze" else ("front", "back", "extra")
    return {k: card.get(k) or "" for k in keys}


def answer_side(card: dict) -> str:
    return card.get("text", "") if card_kind(card) == "cloze" else card.get("back", "")


def has_palette(text: str) -> bool:
    low = (text or "").lower()
    return any(color in low for color in PALETTE)


def is_algo(card: dict) -> bool:
    return ALGO_BADGE in (card.get("badge") or "") or ALGO_BADGE in (card.get("front") or card.get("text") or "")


def tag_balance_errors(text: str) -> list[str]:
    errors = []
    for tag in ("b", "span", "div", "i", "u", "strong", "em", "sup", "sub", "ul", "ol", "li", "table", "tr", "td"):
        opened = len(re.findall(rf"<{tag}(?=[\s>])[^>]*>", text, re.I))
        closed = len(re.findall(rf"</{tag}\s*>", text, re.I))
        if opened != closed:
            errors.append(f"<{tag}> mở {opened} / đóng {closed}")
    return errors


def _words(text: str) -> list[str]:
    return [w for w in re.findall(r"[^\W_]+", text.replace("⟦CLOZE⟧", " ")) if re.search(r"[^\W\d_]", w)]


def partial_cloze_segments(text: str) -> list[str]:
    """Trả về các câu liệt kê (≥3 phần tử) có phần tử bị che lẫn phần tử để trần.

    - Mỗi cloze được thay bằng 1 token trước khi tách, nên một cloze che trọn danh mục
      (kể cả có dấu phẩy bên trong) chỉ tính là 1 phần tử → hợp lệ.
    - Chỉ coi là danh mục khi: có dấu `:` dẫn danh mục (phần tử ≤ 12 từ), hoặc mọi phần tử
      đều ngắn (≤ 8 từ). Phần tử "bị che" = token cloze + tối đa 4 từ trần.
    """
    masked = CLOZE_RE.sub(" ⟦CLOZE⟧ ", text or "")
    plain = strip_html(masked)
    hits = []
    for sentence in re.split(r"(?<=[.!?])\s+(?=[A-ZĐÀ-Ỹ\[])", plain):
        if "⟦CLOZE⟧" not in sentence:
            continue
        has_colon = ":" in sentence
        segment = sentence.rsplit(":", 1)[-1] if has_colon else sentence
        if has_colon and "⟦CLOZE⟧" not in segment:
            continue
        items = [x.strip(" .") for x in re.split(r"[,;•]|\b\d+\)\s|\s+(?:và|hoặc|hay)\s+", segment) if x and x.strip(" .")]
        if len(items) < 3:
            continue
        limit = 12 if has_colon else 8
        if any(len(_words(x)) > limit for x in items):
            continue
        clozed = [x for x in items if "⟦CLOZE⟧" in x and len(_words(x)) <= 4]
        bare = [x for x in items if "⟦CLOZE⟧" not in x and _words(x)]
        if clozed and bare:
            hits.append(sentence[:160])
    return hits


# ---------------------------------------------------------------- core lint
def lint_cards(cards: list[dict], spec: dict | None = None) -> list[Issue]:
    spec = spec or {}
    issues: list[Issue] = []
    add = lambda code, cid, msg: issues.append(Issue(code, str(cid), msg))  # noqa: E731

    ids = Counter(str(c.get("id", "")) for c in cards)
    for cid, n in ids.items():
        if not cid:
            add("T_EMPTY", "?", f"{n} thẻ thiếu id")
        elif n > 1:
            add("T_DUP_ID", cid, f"id lặp {n} lần")

    prompts = Counter(norm_key(c.get("front") or c.get("text") or "") for c in cards)
    for c in cards:
        cid = c.get("id", "?")
        kind = card_kind(c)
        fields = card_fields(c)
        joined = "\n".join(fields.values())

        # --- kỹ thuật
        required = ("text",) if kind == "cloze" else ("front", "back")
        for key in required:
            if not strip_html(fields.get(key, "")):
                add("T_EMPTY", cid, f"field `{key}` rỗng")
        for key, value in fields.items():
            if m := ESCAPED_TAG_RE.search(value):
                add("T_ESCAPED_TAG", cid, f"{key}: tag HTML bị escape thành chữ `{m.group(0)}`")
            if m := DOUBLE_ESCAPE_RE.search(value):
                add("T_DOUBLE_ESCAPE", cid, f"{key}: double-escape `{m.group(0)[:30]}`")
            if m := CONTROL_CHAR_RE.search(value):
                add("T_CONTROL_CHAR", cid, f"{key}: ký tự điều khiển {m.group(0)!r}")
            if m := LATEX_RE.search(value):
                add("T_LATEX", cid, f"{key}: token LaTeX/escape thừa `{m.group(0)}`")
            for err in tag_balance_errors(value):
                add("T_TAG_BALANCE", cid, f"{key}: {err}")
        if kind == "cloze":
            body = fields["text"]
            if not CLOZE_RE.search(body) or body.count("{{") != body.count("}}"):
                add("T_CLOZE_SYNTAX", cid, "cloze thiếu `{{cN::…}}` hoặc ngoặc không cân")
        elif "{{c" in joined:
            add("T_CLOZE_SYNTAX", cid, "thẻ Basic chứa cú pháp cloze")
        key = norm_key(c.get("front") or c.get("text") or "")
        if key and prompts[key] > 1:
            add("T_DUP_FRONT", cid, "mặt trước trùng nguyên văn với thẻ khác")

        # --- back-purity
        if m := BACK_SOURCE_RE.search(strip_html(answer_side(c))):
            add("P_BACK_SOURCE", cid, f"vị trí nguồn trong mặt trả lời: `{m.group(0)}` → chuyển sang Extra")

        # --- governance
        if kind == "basic":
            back = c.get("back", "")
            if "🎯" not in back or "💡" not in back:
                missing = [s for s in ("🎯 Trả lời cốt lõi", "💡 Giải thích của AI") if s[0] not in back]
                add("G_BACK_STRUCTURE", cid, "thiếu " + " + ".join(missing))
            if not has_palette(c.get("front", "")):
                add("G_COLOR_FRONT", cid, "Front không có màu palette")
            if not has_palette(back):
                add("G_COLOR_BACK", cid, "Back không có màu palette")
        else:
            for seg in partial_cloze_segments(fields["text"]):
                add("G_PARTIAL_CLOZE", cid, f"cloze nửa vời trong liệt kê: «{seg}»")
        if not strip_html(c.get("extra", "")):
            add("G_EXTRA_EMPTY", cid, "Extra (nguồn) rỗng")

    # --- deck-level
    basics = [c for c in cards if card_kind(c) == "basic"]
    if cards and not basics:
        add("G_CLOZE_ONLY", "*", f"deck 100% Cloze ({len(cards)} thẻ, 0 Basic)")
    sections = spec.get("required_sections") or []
    have = Counter(c.get("section") for c in cards)
    have_basic = Counter(c.get("section") for c in basics)
    for s in sections:
        if have.get(s, 0) == 0:
            add("D_SECTION_MISSING", s, "section bắt buộc không có thẻ")
        elif have_basic.get(s, 0) == 0:
            add("G_SECTION_NO_BASIC", s, "section không có thẻ Basic nền tảng")
    algo = sum(1 for c in cards if is_algo(c))
    if cards and algo < ALGO_MIN:
        add("G_ALGO_COUNT", "*", f"chỉ {algo} thẻ `{ALGO_BADGE}` (tối thiểu {ALGO_MIN})")
    if cards and not any("tier" in c for c in cards):
        add("W_TIER", "*", "chưa khai báo `tier` (1 = khung, 2 = chi tiết) cho thẻ nào")
    if deck_name := spec.get("deck_name"):
        if spec.get("specialty"):
            error = specialties.get(spec["specialty"]).deck_name_error(deck_name, spec.get("id"))
        else:
            matches = specialties.for_deck_name(deck_name)
            errors = [s.deck_name_error(deck_name) for s in matches]
            error = None if any(e is None for e in errors) else (errors[0] if errors else
                    "gốc deck không thuộc chuyên khoa nào trong specialties.json")
        if error:
            add("D_DECK_NAME", "*", f"tên deck {deck_name!r}: {error}")
    return issues


def lint_media(cards: list[dict], media_dir: Path | None, available: dict[str, int] | None = None) -> list[Issue]:
    """Kiểm ảnh được tham chiếu: tồn tại, ≤150 KB, ≤1200 px (nếu có file để đo)."""
    issues = []
    for c in cards:
        for key, value in card_fields(c).items():
            for name in IMG_RE.findall(value):
                if available is not None:
                    size = available.get(name)
                    if size is None:
                        issues.append(Issue("D_MEDIA", c.get("id", "?"), f"ảnh `{name}` không có trong package"))
                    elif size > MAX_IMAGE_BYTES:
                        issues.append(Issue("D_MEDIA", c.get("id", "?"), f"ảnh `{name}` {size/1024:.0f} KB > 150 KB"))
                    continue
                path = (media_dir / name) if media_dir else None
                if not path or not path.exists():
                    issues.append(Issue("D_MEDIA", c.get("id", "?"), f"ảnh `{name}` không tồn tại trong {media_dir}"))
                    continue
                if path.stat().st_size > MAX_IMAGE_BYTES:
                    issues.append(Issue("D_MEDIA", c.get("id", "?"), f"ảnh `{name}` {path.stat().st_size/1024:.0f} KB > 150 KB"))
                try:
                    from PIL import Image

                    with Image.open(path) as im:
                        if im.width > MAX_IMAGE_WIDTH:
                            issues.append(Issue("D_MEDIA", c.get("id", "?"), f"ảnh `{name}` rộng {im.width}px > 1200px"))
                except Exception as exc:  # ảnh hỏng cũng là lỗi media
                    issues.append(Issue("D_MEDIA", c.get("id", "?"), f"không mở được ảnh `{name}`: {exc}"))
    return issues


def lint_diacritics(apkg_path: Path) -> list[Issue]:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from verify_apkg_diacritics import verify_apkg

    ratio = verify_apkg(apkg_path)[0]
    if ratio < DIACRITICS_MIN:
        return [Issue("D_DIACRITICS", "*", f"tỷ lệ dấu tiếng Việt {ratio:.1%} < 80%")]
    return []


def classify(issues: list[Issue], mode: str) -> list[Issue]:
    if mode not in {"release", "hotfix"}:
        raise ValueError(f"mode không hợp lệ: {mode}")
    for issue in issues:
        if issue.code.startswith("W_"):
            issue.severity = "WARN"
        elif issue.code.startswith(GOVERNANCE_PREFIX):
            issue.severity = "BLOCK" if mode == "release" else "DEBT"
        else:
            issue.severity = "BLOCK"
    return issues


def summarize(issues: list[Issue]) -> dict:
    by_sev = Counter(i.severity for i in issues)
    by_code = Counter(i.code for i in issues)
    return {"block": by_sev.get("BLOCK", 0), "debt": by_sev.get("DEBT", 0), "warn": by_sev.get("WARN", 0),
            "by_code": dict(sorted(by_code.items()))}


def print_report(issues: list[Issue], limit_per_code: int = 5) -> None:
    shown = Counter()
    for issue in sorted(issues, key=lambda i: ({"BLOCK": 0, "DEBT": 1, "WARN": 2}[i.severity], i.code)):
        shown[issue.code] += 1
        if shown[issue.code] <= limit_per_code:
            print(f"  [{issue.severity}] {issue.code} {issue.card_id}: {issue.message}")
    for code, n in shown.items():
        if n > limit_per_code:
            print(f"  … {code}: thêm {n - limit_per_code} lỗi")


# ---------------------------------------------------------------- APKG reader
def read_apkg(apkg_path: Path) -> tuple[list[dict], list[str], dict[str, int]]:
    """Đọc APKG → (cards dạng chuẩn, deck names, media {tên: bytes})."""
    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(apkg_path) as zf:
        names = zf.namelist()
        db_name = "collection.anki21" if "collection.anki21" in names else "collection.anki2"
        zf.extract(db_name, tmp)
        media_map = json.loads(zf.read("media").decode("utf-8") or "{}") if "media" in names else {}
        media = {fname: zf.getinfo(idx).file_size for idx, fname in media_map.items() if idx in names}
        con = sqlite3.connect(Path(tmp) / db_name)
        try:
            models = json.loads(con.execute("select models from col").fetchone()[0])
            decks = json.loads(con.execute("select decks from col").fetchone()[0])
            rows = con.execute("select id, mid, flds from notes order by id").fetchall()
        finally:
            con.close()
    cards = []
    for nid, mid, flds in rows:
        model = models[str(mid)]
        values = dict(zip([f["name"] for f in model["flds"]], flds.split("\x1f")))
        if model.get("type") == 1:
            text_key = "Text" if "Text" in values else list(values)[0]
            card = {"id": str(nid), "type": "cloze", "text": values.get(text_key, ""), "extra": values.get("Extra", "")}
        else:
            keys = list(values)
            card = {"id": str(nid), "type": "basic",
                    "front": values.get("Front", values.get(keys[0], "")),
                    "back": values.get("Back", values.get(keys[1], "") if len(keys) > 1 else ""),
                    "extra": values.get("Extra", "")}
        card["badge"] = values.get("Badge", "")
        cards.append(card)
    deck_names = [d["name"] for d in decks.values() if d["name"] != "Default"]
    return cards, deck_names, media


def lint_apkg(apkg_path: Path, mode: str) -> tuple[list[Issue], dict]:
    cards, deck_names, media = read_apkg(apkg_path)
    spec = {"deck_name": deck_names[0] if len(deck_names) == 1 else (deck_names[-1] if deck_names else "")}
    if specialty := specialties.for_path(apkg_path):
        spec["specialty"] = specialty.key
        spec["id"] = specialty.lesson_id_from_folder(apkg_path.parent.name)
    issues = lint_cards(cards, spec) + lint_media(cards, None, media) + lint_diacritics(apkg_path)
    classify(issues, mode)
    basic = sum(1 for c in cards if c["type"] == "basic")
    return issues, {"deck": spec["deck_name"], "id": spec.get("id") or apkg_path.parent.name,
                    "specialty": spec.get("specialty"), "notes": len(cards), "basic": basic,
                    "cloze": len(cards) - basic}


def release_apkgs(root: Path) -> list[Path]:
    """APKG phát hành của các folder bài dưới `root` (bỏ outputs/ candidate, legacy, bản trùng)."""
    skip = {"_duplicates_review", "80_Legacy_by_format", "99_Inbox", "08_Anki Deck - apkg", "cache"}
    return sorted(p for p in root.rglob("*.apkg") if not skip & set(p.parts) and "verification" not in p.parts)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apkg", type=Path, help="lint chi tiết 1 file APKG")
    ap.add_argument("--scan-apkg", type=Path, help="lint mọi APKG của các folder bài dưới thư mục này")
    ap.add_argument("--mode", default="release", choices=["release", "hotfix"])
    ap.add_argument("--json", type=Path, help="ghi báo cáo JSON")
    args = ap.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    if args.apkg:
        issues, meta = lint_apkg(args.apkg, args.mode)
        print(f"{args.apkg.name}: {meta}")
        print_report(issues)
        print(summarize(issues))
        if args.json:
            args.json.write_text(json.dumps({"meta": meta, "issues": [i.to_dict() for i in issues]},
                                            ensure_ascii=False, indent=2), encoding="utf-8")
        return 2 if summarize(issues)["block"] else 0

    if args.scan_apkg:
        report, any_block = [], False
        print(f"{'Mã':10} {'notes':>5} {'B/C':>9} {'BLOCK':>6} {'DEBT':>6}  top codes")
        for path in release_apkgs(args.scan_apkg):
            issues, meta = lint_apkg(path, args.mode)
            s = summarize(issues)
            any_block |= bool(s["block"])
            top = ", ".join(f"{k}:{v}" for k, v in Counter(i.code for i in issues if i.severity != "WARN").most_common(4))
            print(f"{meta['id'][:10]:10} {meta['notes']:>5} {meta['basic']:>4}/{meta['cloze']:<4} {s['block']:>6} {s['debt']:>6}  {top}")
            report.append({"apkg": str(path), **meta, **s})
        if args.json:
            args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        return 2 if any_block else 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
