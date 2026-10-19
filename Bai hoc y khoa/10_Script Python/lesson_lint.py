# -*- coding: utf-8 -*-
"""lesson_lint.py — linter bài học Markdown dùng chung cho MỌI chuyên khoa.

    python lesson_lint.py <lesson_dir> [--mode release|hotfix]
    python lesson_lint.py --scan <root> --json report.json     # sổ nợ (luôn hotfix)

Nguồn rule: Bai hoc y khoa/RULES_LESSON_APKG.md §4. Mã lỗi:
  M_*  manifest (lesson.json, mã bài, profile khớp brief)
  S_*  cấu trúc & chiều sâu theo profile (dùng depth_check.py — một engine duy nhất)
  F_*  định dạng an toàn cho marked.js/DOCX: tab đầu dòng, indented code block, LaTeX, ký tự điều khiển
  C_*  chuỗi cơ chế phải ở dạng blockquote `> 🔄 **Chuỗi cơ chế:** … → …`
  I_*  hình ảnh: local `outputs/figures/`, ≤150 KB, ≤1200 px, tên `<MÃ>_figN_<ten>.<ext>`, ≤4 ảnh, có alt
  V_*  nhãn verification: chỉ nhãn hợp lệ; ở chế độ `ncbi_artifacts` mỗi nhãn phải có artifact tương ứng
Mode `release`: mọi lỗi BLOCK (bài mới / viết lại). Mode `hotfix`: mọi lỗi là DEBT (bài cũ — sổ nợ).
Exit: 0 = không BLOCK, 2 = có BLOCK.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import card_lint  # noqa: E402
import depth_check  # noqa: E402
import lesson_manifest  # noqa: E402
import specialties  # noqa: E402
from card_lint import Issue, summarize  # noqa: E402

ALLOWED_LABELS = {"[FETCHED]", "[ABSTRACT VERIFIED]", "[DATA VERIFIED]", "[GUIDELINE VERIFIED]",
                  "[FULL TEXT VERIFIED]", "[FULL TEXT / VISUAL VERIFIED]"}
BANNED_LABELS = {"[FULL VERIFIED]": "dùng [FULL TEXT VERIFIED] hoặc [FULL TEXT / VISUAL VERIFIED]",
                 "[ABSTRACT MATCH]": "dùng [ABSTRACT VERIFIED]", "[DIRECTION ONLY]": "bỏ nhãn",
                 "[TEXTBOOK]": "kiến thức nền không gắn nhãn", "[PMC VERIFIED]": "dùng [FULL TEXT VERIFIED]",
                 "[Thông tin cơ bản - LLM verified]": "kiến thức nền không gắn nhãn"}
LABEL_RE = re.compile(r"\[(?:[A-Z][A-Z /]+VERIFIED|FETCHED|ABSTRACT MATCH|DIRECTION ONLY|TEXTBOOK|Thông tin cơ bản - LLM verified)\]")
PMID_RE = re.compile(r"PMID[:\s*]*\**\s*(\d{6,9})")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CHAIN_BLOCK_RE = re.compile(r"^>\s*🔄\s*\*\*Chuỗi cơ chế[^*]*\*\*:?.*→", re.M)
MAX_IMAGES = 4
LATEX_MD_RE = re.compile(r"\$\$|(?<![\w$])\$[^$\n]{1,80}\$(?!\w)|\\(?:text|frac|rightarrow|leftarrow|times|geq?|leq?|approx|pm|mu|alpha|beta|Delta|to)(?![a-zA-Z])"
                         r"|\\[^\x00-\x7f]|(?<![a-zA-Z])(?:ightarrow|ext\{)")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s")


def _prose_lines(text: str):
    """(số dòng, nội dung) của các dòng NGOÀI code fence."""
    in_fence = False
    for no, line in enumerate(text.splitlines(), 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield no, line


def check_format(text: str) -> list[Issue]:
    issues, prev, prev_nonblank = [], "", ""
    for no, line in _prose_lines(text):
        where = f"dòng {no}"
        if line.startswith("\t"):
            issues.append(Issue("F_TAB_INDENT", where, "dòng bắt đầu bằng Tab → marked.js hiểu thành code block"))
        elif re.match(r"^ {4,}\S", line) and not prev.strip() and not LIST_ITEM_RE.match(prev_nonblank) \
                and not prev_nonblank.startswith((" ", "|")):
            issues.append(Issue("F_INDENTED_CODE", where, "đoạn thụt ≥4 dấu cách sau dòng trống → thành code block"))
        if m := LATEX_MD_RE.search(line):
            issues.append(Issue("F_LATEX", where, f"LaTeX/escape thừa `{m.group(0)[:30]}` — dùng Unicode → ≥ ≤ ×"))
        if m := card_lint.CONTROL_CHAR_RE.search(line):
            issues.append(Issue("F_CONTROL_CHAR", where, f"ký tự điều khiển {m.group(0)!r}"))
        prev = line
        if line.strip():
            prev_nonblank = line
    return issues


def check_chains(text: str, cfg: depth_check.DepthConfig) -> list[Issue]:
    found = len(CHAIN_BLOCK_RE.findall(text))
    if found < cfg.min_mechanism_chains:
        return [Issue("C_CHAIN_FORMAT", "*", f"chỉ {found} chuỗi cơ chế dạng `> 🔄 **Chuỗi cơ chế:** … → …` "
                                              f"(profile {cfg.profile_name} cần ≥ {cfg.min_mechanism_chains})")]
    return []


def check_images(text: str, m: lesson_manifest.Manifest) -> list[Issue]:
    issues, images = [], IMAGE_RE.findall(text)
    stem = m.id.replace("-", "")
    for alt, path in images:
        where = path
        if re.match(r"https?://", path):
            issues.append(Issue("I_REMOTE", where, "ảnh phải tải về, nén và lưu local trong outputs/figures/"))
            continue
        if not path.startswith("outputs/figures/"):
            issues.append(Issue("I_PATH", where, "ảnh phải nằm trong outputs/figures/"))
        if not alt.strip():
            issues.append(Issue("I_ALT", where, "thiếu mô tả ảnh (alt text)"))
        name = Path(path).name
        if not re.fullmatch(rf"{re.escape(stem)}_fig\d+_[a-z0-9_]+\.(?:jpg|jpeg|png|webp)", name):
            issues.append(Issue("I_NAME", where, f"tên ảnh phải dạng {stem}_figN_<ten_khong_dau>.jpg"))
        file = m.lesson_dir / path
        if not file.exists():
            issues.append(Issue("I_MISSING", where, "không thấy file ảnh"))
            continue
        if file.stat().st_size > card_lint.MAX_IMAGE_BYTES:
            issues.append(Issue("I_SIZE", where, f"{file.stat().st_size / 1024:.0f} KB > 150 KB"))
        try:
            from PIL import Image

            with Image.open(file) as im:
                if im.width > card_lint.MAX_IMAGE_WIDTH:
                    issues.append(Issue("I_SIZE", where, f"rộng {im.width}px > 1200px"))
        except Exception as exc:
            issues.append(Issue("I_MISSING", where, f"không mở được ảnh: {exc}"))
    if len(images) > MAX_IMAGES:
        issues.append(Issue("I_COUNT", "*", f"{len(images)} ảnh > {MAX_IMAGES} ảnh high-yield/bài"))
    return issues


def _find_artifact(lesson_dir: Path, name: str) -> Path | None:
    hits = sorted(p for p in lesson_dir.rglob(name) if "_duplicates_review" not in p.parts)
    return hits[0] if hits else None


def check_labels(text: str, m: lesson_manifest.Manifest) -> list[Issue]:
    issues = []
    for no, line in _prose_lines(text):
        for label in LABEL_RE.findall(line):
            if label in BANNED_LABELS:
                issues.append(Issue("V_BANNED_LABEL", f"dòng {no}", f"nhãn cũ {label} bị cấm — {BANNED_LABELS[label]}"))
            elif label not in ALLOWED_LABELS:
                issues.append(Issue("V_UNKNOWN_LABEL", f"dòng {no}", f"nhãn {label} không thuộc bộ nhãn chuẩn"))
    if m.specialty.evidence_mode != "ncbi_artifacts":
        return issues  # evidence_bundle: build_pipeline.py kiểm từng claim (preflight/claims/guideline gates)

    fetch_p = _find_artifact(m.lesson_dir, "ncbi_fetch.json")
    match_p = _find_artifact(m.lesson_dir, "abstract_match.jsonl")
    table_p = _find_artifact(m.lesson_dir, "full_verify_table.md")
    fetched = json.loads(fetch_p.read_text(encoding="utf-8")) if fetch_p else {}
    matched = {}
    if match_p:
        for row in match_p.read_text(encoding="utf-8").splitlines():
            if row.strip():
                rec = json.loads(row)
                if rec.get("match") in (True, "true", "partial"):
                    matched.setdefault(str(rec.get("pmid")), rec)
    table = table_p.read_text(encoding="utf-8") if table_p else ""
    guide_p = _find_artifact(m.lesson_dir, "guideline_evidence.json")
    guidelines = json.loads(guide_p.read_text(encoding="utf-8")) if guide_p else []
    guidelines = guidelines.get("guidelines", []) if isinstance(guidelines, dict) else guidelines
    guide_keys = {str(g.get(k)).casefold() for g in guidelines if isinstance(g, dict)
                  for k in ("document_id", "society", "title") if g.get(k)}
    for no, line in _prose_lines(text):
        labels = [lb for lb in LABEL_RE.findall(line) if lb in ALLOWED_LABELS]
        if not labels:
            continue
        pmids = PMID_RE.findall(line)
        where = f"dòng {no}"
        if not pmids:
            # guideline không có PMID: phải có mục tương ứng trong guideline_evidence.json
            if labels == ["[GUIDELINE VERIFIED]"] and any(k in line.casefold() for k in guide_keys):
                continue
            issues.append(Issue("V_NO_PMID", where, f"{labels[0]} không kèm PMID trên cùng dòng "
                                                    "(guideline không PMID phải có mục trong guideline_evidence.json)"))
            continue
        for pmid in pmids:
            if pmid not in fetched:
                issues.append(Issue("V_NOT_FETCHED", where, f"PMID {pmid} không có trong ncbi_fetch.json (Gate 0)"))
                continue
            for label in labels:
                if label in ("[ABSTRACT VERIFIED]", "[GUIDELINE VERIFIED]") and pmid not in matched:
                    issues.append(Issue("V_NO_ABSTRACT_MATCH", where, f"{label} PMID {pmid} thiếu dòng match trong abstract_match.jsonl (Gate 1)"))
                if label == "[GUIDELINE VERIFIED]":
                    types = " ".join(fetched[pmid].get("publication_types") or fetched[pmid].get("pubtype") or [])
                    if not re.search(r"Guideline|Consensus", types, re.I):
                        issues.append(Issue("V_NOT_GUIDELINE", where, f"PMID {pmid} không có pubtype Guideline/Consensus"))
                if label in ("[DATA VERIFIED]", "[FULL TEXT VERIFIED]", "[FULL TEXT / VISUAL VERIFIED]") and pmid not in table:
                    issues.append(Issue("V_NO_FULL_VERIFY", where, f"{label} PMID {pmid} không có trong full_verify_table.md (Gate 2)"))
    return issues


def brief_profile(m: lesson_manifest.Manifest) -> str | None:
    if not m.brief:
        return None
    text = (m.lesson_dir / m.brief).read_text(encoding="utf-8")
    block = re.search(r"^##\s+0\.\s+Lesson profile & release contract\s*$.*?```json\s*(\{.*?\})\s*```", text, re.S | re.M)
    if not block:
        return None
    try:
        return json.loads(block.group(1)).get("profile")
    except json.JSONDecodeError:
        return None


def lint_lesson(m: lesson_manifest.Manifest) -> list[Issue]:
    issues = [Issue("M_MANIFEST", "lesson.json", e) for e in lesson_manifest.validate(m)]
    if not m.lesson_path or not m.lesson_path.exists():
        issues.append(Issue("M_MANIFEST", "lesson.json", "thiếu file bài học (`lesson`)"))
        return issues
    if not re.fullmatch(rf"{re.escape(m.id)}_[A-Za-z0-9_]+_\d{{4}}-\d{{2}}-\d{{2}}_RELEASE_v\d+\.md", m.lesson_path.name):
        issues.append(Issue("M_FILENAME", m.lesson_path.name, f"tên file bài phải dạng {m.id}_<Ten_khong_dau>_YYYY-MM-DD_RELEASE_vN.md"))
    if (bp := brief_profile(m)) and bp != m.profile:
        hint = "" if bp in lesson_manifest.PROFILES else f" — brief dùng profile ngoài danh sách {lesson_manifest.PROFILES}"
        issues.append(Issue("M_PROFILE", "lesson.json", f"profile {m.profile!r} khác contract trong brief ({bp!r}){hint}"))
    text = m.lesson_path.read_text(encoding="utf-8")
    cfg = depth_check.get_depth_config(m.profile)
    report = depth_check.run_depth_check(m.lesson_path, cfg)
    for r in report.results:
        if not r.passed and not r.informational:
            issues.append(Issue("S_DEPTH", r.name, f"{r.value} (cần {r.threshold}) {r.message}".strip()))
    issues += check_format(text) + check_chains(text, cfg) + check_images(text, m) + check_labels(text, m)
    return issues


def classify(issues: list[Issue], mode: str) -> list[Issue]:
    for issue in issues:
        issue.severity = "BLOCK" if mode == "release" else "DEBT"
    return issues


def run(lesson_dir: Path, mode: str, quiet: bool = False) -> tuple[int, list[Issue]]:
    m = lesson_manifest.load(lesson_dir)
    issues = classify(lint_lesson(m), mode)
    s = summarize(issues)
    m.verify_dir.mkdir(parents=True, exist_ok=True)
    (m.verify_dir / "lesson-lint.json").write_text(json.dumps(
        {"id": m.id, "specialty": m.specialty.key, "profile": m.profile, "lesson": m.lesson, "mode": mode,
         "summary": s, "issues": [i.to_dict() for i in issues]}, ensure_ascii=False, indent=2), encoding="utf-8")
    if not quiet:
        print(f"=== LESSON {m.id} ({m.specialty.name}, profile={m.profile}, mode={mode}) ===")
        card_lint.print_report(issues, limit_per_code=8)
        print(f"  lesson-lint: BLOCK={s['block']} DEBT={s['debt']}")
    return (2 if s["block"] else 0), issues


# ---------------------------------------------------------------- sổ nợ (bài chưa có lesson.json)
def guess_lesson_md(folder: Path, lesson_id: str | None) -> Path | None:
    cands = [p for p in folder.glob("*.md") if not re.search(r"BRIEF|PEDYTB|knowledge_check|citation_audit|README|MCQ|QA-",
                                                              p.name, re.I)]
    release = [p for p in cands if "RELEASE" in p.name.upper()]
    pool = release or [p for p in cands if re.search(r"\d{4}-\d{2}-\d{2}", p.name)]
    return max(pool, key=lambda p: (p.stat().st_mtime, p.name)) if pool else None


def scan(root: Path) -> list[dict]:
    """Quét mọi folder bài dưới root ở mode hotfix → danh sách nợ (không ghi gì vào folder bài)."""
    rows = []
    for spec in specialties.load().values():
        base = root / spec.folder
        if not base.exists():
            continue
        for folder in sorted({p.parent for p in base.rglob("*.md")} | {p.parent for p in base.rglob("lesson.json")}):
            if {"outputs", "_duplicates_review", "sources", "raw_cache"} & set(folder.relative_to(root).parts):
                continue
            lesson_id = spec.lesson_id_from_folder(folder.name)
            if not lesson_id:
                continue
            row = {"specialty": spec.key, "id": lesson_id, "folder": str(folder.relative_to(root)).replace("\\", "/")}
            if (folder / lesson_manifest.MANIFEST_NAME).exists():
                m = lesson_manifest.load(folder)
                issues = classify(lint_lesson(m), "hotfix")
                row.update(manifest=True, profile=m.profile, lesson=m.lesson)
            else:
                md = guess_lesson_md(folder, lesson_id)
                row.update(manifest=False, profile=None, lesson=md.name if md else None)
                issues = [Issue("M_MANIFEST", "lesson.json", "chưa có lesson.json")]
                if md:
                    profile = "disease"
                    fake = lesson_manifest.Manifest(folder, lesson_id, spec, profile, md.name, None, None,
                                                    {"basename": md.stem, "cards_source": "-"})
                    row["profile"] = f"{profile} (giả định)"
                    issues += [i for i in lint_lesson(fake) if i.code != "M_MANIFEST"]
                else:
                    issues.append(Issue("M_MANIFEST", "-", "không tìm thấy file bài .md"))
                classify(issues, "hotfix")
            row["debt"] = len(issues)
            row["by_code"] = dict(sorted(Counter(i.code for i in issues).items()))
            row["depth_fails"] = sorted({i.card_id for i in issues if i.code == "S_DEPTH"})
            rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lesson_dir", type=Path, nargs="?")
    ap.add_argument("--mode", default="release", choices=["release", "hotfix"])
    ap.add_argument("--scan", type=Path, help="quét sổ nợ toàn bộ bài dưới thư mục này")
    ap.add_argument("--json", type=Path)
    args = ap.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if args.scan:
        rows = scan(args.scan.resolve())
        for r in rows:
            print(f"{r['id']:10} {r['specialty']:12} nợ={r['debt']:4}  {', '.join(f'{k}:{v}' for k, v in r['by_code'].items())}")
        if args.json:
            args.json.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0
    if not args.lesson_dir:
        ap.print_help()
        return 1
    try:
        code, _ = run(args.lesson_dir.resolve(), args.mode)
    except lesson_manifest.ManifestError as exc:
        print(f"[BLOCK] {exc}")
        return 2
    return code


if __name__ == "__main__":
    sys.exit(main())
