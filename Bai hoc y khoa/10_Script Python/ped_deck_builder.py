# -*- coding: utf-8 -*-
"""ped_deck_builder.py — builder dùng chung cho mọi deck Nhi khoa (PED).

    python ped_deck_builder.py <lesson_dir> [--mode release|hotfix] [--sync-anki] [--lint-only]

Đầu vào trong <lesson_dir>:
  ped_deck.json        spec deck (xem PED_RULES.md §3)
  pedXX_cards_data.py  `cards_data = [...]` — nguồn duy nhất của thẻ
Đầu ra:
  <basename>.cards.v2.json, <basename>.apkg (root folder bài)
  pedXX_anki_lock.json (GUID + note id cố định cho từng card id)
  outputs/verification/<basename>/card-lint.json
Exit: 0 = PASS, 2 = BLOCK (lint/verify/sync thất bại).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import re
import sqlite3
import sys
import tempfile
import zipfile
from pathlib import Path

import genanki

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ped_card_lint as lint  # noqa: E402

SHARED_MODELS = {
    "basic": {"id": 1790604700021, "name": "NhiKhoa_Master_Basic"},
    "cloze": {"id": 1790604702132, "name": "NhiKhoa_Master_Cloze"},
}
BASIC_FIELDS = ["Front", "Back", "Extra", "Category", "Badge", "BadgeClass"]
CLOZE_FIELDS = ["Text", "Extra", "Category", "Badge", "BadgeClass"]
DEFAULT_BADGE = {"barem_goc": ("🏛️ BAREM GỐC Y THÁI BÌNH", "badge-barem"),
                 "ebm": ("🔬 EBM HIỆN ĐẠI & LÂM SÀNG", "badge-ebm")}

CSS = """
.card { font-family: 'Be Vietnam Pro', 'Segoe UI', -apple-system, sans-serif; font-size: 16px; line-height: 1.6;
  color: #e2e8f0; background-color: #0b1120; padding: 20px; max-width: 680px; margin: 0 auto; border-radius: 12px; }
.badge { display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 800;
  letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 12px; }
.badge-barem { background-color: rgba(245,158,11,0.15); color: #fbbf24; border: 1px solid rgba(245,158,11,0.4); }
.badge-ebm { background-color: rgba(6,182,212,0.15); color: #22d3ee; border: 1px solid rgba(6,182,212,0.4); }
.badge-red { background-color: rgba(255,107,107,0.15); color: #ff6b6b; border: 1px solid rgba(255,107,107,0.45); }
.badge-amber { background-color: rgba(255,212,59,0.15); color: #ffd43b; border: 1px solid rgba(255,212,59,0.45); }
.badge-green { background-color: rgba(81,207,102,0.15); color: #51cf66; border: 1px solid rgba(81,207,102,0.45); }
.badge-blue, .badge-cyan { background-color: rgba(116,192,252,0.15); color: #74c0fc; border: 1px solid rgba(116,192,252,0.45); }
.badge-purple { background-color: rgba(177,151,252,0.15); color: #b197fc; border: 1px solid rgba(177,151,252,0.45); }
.badge-algo { background-color: rgba(81,207,102,0.15); color: #51cf66; border: 1px solid rgba(81,207,102,0.45); }
.question { font-size: 16px; font-weight: 600; color: #f8fafc; margin-bottom: 12px; }
.answer-box { background-color: rgba(255,255,255,0.03); border-radius: 8px; padding: 14px 16px;
  border-left: 3px solid #06b6d4; margin-top: 12px; font-size: 14.5px; }
.extra-box { margin-top: 16px; padding: 10px 14px; border-radius: 8px; background-color: rgba(255,255,255,0.02);
  border-left: 3px solid #64748b; font-size: 13.5px; color: #94a3b8; }
.extra-title { font-weight: 700; color: #cbd5e1; margin-bottom: 4px; font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; }
.cloze { font-weight: 700; color: #ffd43b; }
img { max-width: 100%; height: auto; border-radius: 8px; }
"""
BADGE_HTML = '<div class="badge {{BadgeClass}}">{{Badge}}{{#Category}} • {{Category}}{{/Category}}</div>'
EXTRA_HTML = '{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn trích dẫn y chứng & Tài liệu học tập:</div>{{Extra}}</div>{{/Extra}}'


def model_specs(spec: dict) -> dict[str, dict]:
    chosen = {**SHARED_MODELS, **(spec.get("models") or {})}
    basic, cloze = chosen["basic"], chosen["cloze"]
    return {
        "basic": {"id": int(basic["id"]), "name": basic["name"], "fields": BASIC_FIELDS, "is_cloze": False, "css": CSS,
                  "template_name": "Nhi khoa Master Basic",
                  "qfmt": BADGE_HTML + '<div class="question">{{Front}}</div>',
                  "afmt": BADGE_HTML + '<div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>' + EXTRA_HTML},
        "cloze": {"id": int(cloze["id"]), "name": cloze["name"], "fields": CLOZE_FIELDS, "is_cloze": True, "css": CSS,
                  "template_name": "Nhi khoa Master Cloze",
                  "qfmt": BADGE_HTML + '<div class="question">{{cloze:Text}}</div>',
                  "afmt": BADGE_HTML + '<div class="question">{{cloze:Text}}</div>' + EXTRA_HTML},
    }


def genanki_model(m: dict) -> genanki.Model:
    return genanki.Model(m["id"], m["name"], fields=[{"name": f} for f in m["fields"]],
                         templates=[{"name": m["template_name"], "qfmt": m["qfmt"], "afmt": m["afmt"]}],
                         css=m["css"], model_type=genanki.Model.CLOZE if m["is_cloze"] else genanki.Model.FRONT_BACK)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?![a-zA-Z/])", "&lt;", text)


def load_cards(lesson_dir: Path, module_name: str) -> list[dict]:
    path = lesson_dir / f"{module_name}.py"
    loader = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module.cards_data


def render_card(card: dict) -> dict:
    """Chuẩn hóa thẻ → đúng nội dung người học sẽ thấy (đã escape, đủ badge)."""
    out = dict(card)
    out["type"] = lint.card_kind(card)
    for key in ("front", "back", "text", "extra"):
        if key in out:
            out[key] = escape_angle_brackets(out[key])
    badge, badge_class = DEFAULT_BADGE.get(card.get("track", ""), ("", ""))
    if lint.is_algo(card):
        badge, badge_class = lint.ALGO_BADGE, "badge-algo"
    out["badge"] = card.get("badge") or badge
    out["badge_class"] = card.get("badge_class") or badge_class
    out["category"] = card.get("category", "")
    return out


def card_note_fields(c: dict) -> list[str]:
    """Thứ tự field theo notetype chung (CLOZE_FIELDS / BASIC_FIELDS)."""
    if c["type"] == "cloze":
        return [c["text"], c.get("extra", ""), c["category"], c["badge"], c["badge_class"]]
    return [c["front"], c["back"], c.get("extra", ""), c["category"], c["badge"], c["badge_class"]]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(lesson_dir: Path, mode: str, sync_anki: bool, lint_only: bool) -> int:
    spec = json.loads((lesson_dir / "ped_deck.json").read_text(encoding="utf-8"))
    code, basename = spec["code"], spec["basename"]
    module = spec.get("cards_module") or f"ped{code.split('-')[1].lower()}_cards_data"
    media_dir = lesson_dir / spec.get("media_dir", "outputs/figures")
    lock_path = lesson_dir / f"{module.replace('_cards_data', '')}_anki_lock.json"
    apkg_path = lesson_dir / f"{basename}.apkg"
    json_path = lesson_dir / f"{basename}.cards.v2.json"
    verify_dir = lesson_dir / "outputs" / "verification" / basename
    models = model_specs(spec)

    raw_cards = load_cards(lesson_dir, module)
    cards = [render_card(c) for c in raw_cards]
    print(f"=== {code}: {spec['deck_name']} — {len(cards)} thẻ, mode={mode} ===")

    issues = lint.lint_cards(cards, spec) + lint.lint_media(cards, media_dir)
    lint.classify(issues, mode)
    lint.print_report(issues)
    summary = lint.summarize(issues)
    print(f"  lint: BLOCK={summary['block']} DEBT={summary['debt']} WARN={summary['warn']}")

    def write_report(status: str, extra: dict | None = None) -> None:
        verify_dir.mkdir(parents=True, exist_ok=True)
        payload = {"code": code, "deck_name": spec["deck_name"], "mode": mode, "status": status,
                   "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
                   "cards_source": f"{module}.py", "cards_source_sha256": sha256(lesson_dir / f"{module}.py"),
                   "card_count": len(cards), "summary": summary,
                   "issues": [i.to_dict() for i in issues], **(extra or {})}
        (verify_dir / "card-lint.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    if summary["block"]:
        write_report("BLOCK")
        print("[BLOCK] Sửa các lỗi trên trong cards data rồi build lại.")
        return 2
    if lint_only:
        print("[OK] lint-only")
        return 0

    lock = json.loads(lock_path.read_text(encoding="utf-8")) if lock_path.exists() else {}
    g_models = {k: genanki_model(m) for k, m in models.items()}
    media_files: set[str] = set()
    expected_cards = 0
    for c in cards:
        expected_cards += len(set(re.findall(r"\{\{c(\d+)::", c["text"]))) if c["type"] == "cloze" else 1
        for value in card_note_fields(c):
            media_files.update(lint.IMG_RE.findall(value))

    def write_apkg() -> None:
        deck = genanki.Deck(int(spec["deck_id"]), spec["deck_name"])
        for c in cards:
            guid = lock.get(c["id"], {}).get("guid") or genanki.guid_for(code, c["id"])
            lock.setdefault(c["id"], {})["guid"] = guid
            deck.add_note(genanki.Note(model=g_models[c["type"]], fields=card_note_fields(c), guid=guid,
                                       tags=c.get("tags") or [code]))
        package = genanki.Package(deck)
        package.media_files = [str(media_dir / name) for name in sorted(media_files)]
        package.write_to_file(str(apkg_path))

    def verify_apkg() -> list[str]:
        with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(apkg_path) as zf:
            zf.extractall(tmp)
            db = next(Path(tmp) / n for n in ("collection.anki21", "collection.anki2") if (Path(tmp) / n).exists())
            con = sqlite3.connect(db)
            n_notes = con.execute("select count(*) from notes").fetchone()[0]
            n_cards = con.execute("select count(*) from cards").fetchone()[0]
            guids = {g for (g,) in con.execute("select guid from notes")}
            con.close()
            media_map = json.loads((Path(tmp) / "media").read_text(encoding="utf-8") or "{}")
        problems = []
        if n_notes != len(cards):
            problems.append(f"SQLite notes {n_notes} != input {len(cards)}")
        if n_cards != expected_cards:
            problems.append(f"SQLite cards {n_cards} != kỳ vọng {expected_cards}")
        if guids != {lock[c["id"]]["guid"] for c in cards} or len(guids) != len(cards):
            problems.append("GUID không duy nhất hoặc lệch lock file")
        if set(media_map.values()) != media_files:
            problems.append(f"media lệch: {sorted(media_files ^ set(media_map.values()))}")
        return problems

    write_apkg()
    problems = verify_apkg()
    post = lint.lint_diacritics(apkg_path)
    lint.classify(post, mode)
    issues.extend(post)
    summary = lint.summarize(issues)
    for p in problems + [i.message for i in post]:
        print(f"  [BLOCK] verify: {p}")
    if problems or post:
        write_report("BLOCK")
        return 2
    extra = {"apkg": apkg_path.name}

    if sync_anki:
        import ped_anki_sync

        report = ped_anki_sync.sync(code, spec["deck_name"], cards, models, lock,
                                    legacy_decks=spec.get("legacy_anki_decks"))
        print(f"  [ANKI] {report}")
        extra["anki_sync"] = report
        write_apkg()  # GUID thật của Anki → import APKG ở máy khác sẽ cập nhật, không nhân đôi
        if problems := verify_apkg():
            print(f"  [BLOCK] verify sau sync: {problems}")
            write_report("BLOCK", extra)
            return 2
    lock_path.write_text(json.dumps(dict(sorted(lock.items())), ensure_ascii=False, indent=2), encoding="utf-8")
    json_path.write_text(json.dumps({"deck_id": spec["deck_id"], "deck_name": spec["deck_name"],
                                     "card_count": len(raw_cards), "cards": raw_cards},
                                    ensure_ascii=False, indent=2), encoding="utf-8")
    extra.update(apkg_sha256=sha256(apkg_path), sqlite_notes=len(cards), sqlite_cards=expected_cards)
    print(f"  [OK] APKG {apkg_path.name}: {len(cards)} notes / {expected_cards} cards / {len(media_files)} media")
    status = "PASS" if summary["debt"] == 0 else "PASS_WITH_DEBT"
    write_report(status, extra)
    print(f"[{status}] {code}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lesson_dir", type=Path)
    ap.add_argument("--mode", default="release", choices=["release", "hotfix"])
    ap.add_argument("--sync-anki", action="store_true")
    ap.add_argument("--lint-only", action="store_true")
    args = ap.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    return build(args.lesson_dir.resolve(), args.mode, args.sync_anki, args.lint_only)


if __name__ == "__main__":
    sys.exit(main())
