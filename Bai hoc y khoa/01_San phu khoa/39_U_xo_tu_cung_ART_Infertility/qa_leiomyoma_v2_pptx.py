# -*- coding: utf-8 -*-
"""QA gate for the v2 leiomyoma ART personal-note PPTX."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

ROOT = Path(__file__).parent
DATE = "2026-07-14"
PPTX = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.pptx"
DECK = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.deck.json"
PROV = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.provenance.json"
APPROVED_DOCX = ROOT / "U_xo_tu_cung_ART_Infertility_2026-07-12.docx"

REQUIRED_BACKBONE_TABLES = {"T3", "T5", "T11", "T15", "T20", "T21", "T24"}
REQUIRED_SECTION_TITLES = [
    "Định nghĩa", "Cơ chế bệnh sinh và sinh học u xơ",
    "Phân loại", "Triệu chứng và biểu hiện lâm sàng",
    "Chẩn đoán và hình ảnh học", "Cơ chế ảnh hưởng ART",
    "Xử trí theo FIGO", "Phương pháp điều trị",
    "Thứ tự ART, theo dõi và bằng chứng",
]

# Forbidden text outside metadata (no "Làm gì:", English teaching headings,
# forbitten side-source names). Visible English is limited to accepted acronyms.
FORBIDDEN_TEXT = [
    "Quá trình mổ u xơ", "Giải thích các bước phẫu thuật u xơ",
    "Hạn chế dính buồng tử cung", "PMC13278667_fulltext",
    "placeholder", "lorem", "ipsum", "xxxx",
    "Làm gì:", "Tại sao:", "Nếu bỏ qua/làm sai:", "Nguy cơ nếu sai:",
    
    "leiomyosarcoma",
    
    
]
FORBIDDEN_ENGLISH_VISIBLE = [
    "Roadmap", "ART risk", "cavity-distorting", "restore cavity",
    "shared decision", "anchoring bias", "over-treatment",
    "Decision by FIGO", "Management by FIGO", "Embryo banking decision",
    "Fresh vs frozen", "Integrated ART decision algorithm",
    "Take-home messages", "Case drill", "Treatment-effect matrix",
    "Note cá nhân", "Note:",
]
# Allowed acronyms in slides: ART, IVF, FET, FIGO, TVUS, SIS, MRI, RIF,
# AMH, AFC, AUB, Hb, GnRH, UAE, HIFU, RFA, NSAID, TXA, STUMP, DOR,
# PMID, DOI, HyFoSy, COC, LNG-IUS, ICSI.

MAX_VISIBLE_CHARS = 1200
DENSE_CHARS = 950
MIN_VISIBLE_CHARS = 90
MAX_DENSE_SLIDES = 12

NO_PAGE_TYPES = {"title", "section", "outline", "key_message", "transition"}


def iter_shapes(shapes):
    for shape in shapes:
        yield shape
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from iter_shapes(shape.shapes)


def shape_text(shape):
    parts = []
    if getattr(shape, "has_text_frame", False):
        parts.append(shape.text_frame.text or "")
    if getattr(shape, "has_table", False):
        for row in shape.table.rows:
            for cell in row.cells:
                parts.append(cell.text or "")
    return "\n".join(p for p in parts if p)


def slide_text(slide):
    return "\n".join(shape_text(s) for s in iter_shapes(slide.shapes) if shape_text(s))


def notes_text(slide):
    if not slide.has_notes_slide:
        return ""
    return (slide.notes_slide.notes_text_frame.text or "").strip()


def fail(msg: str, failures: list[str]):
    print(f"[FAIL] {msg}")
    failures.append(msg)


def ok(msg: str):
    print(f"[OK] {msg}")


def picture_count(prs: Presentation) -> int:
    total = 0
    for slide in prs.slides:
        for s in iter_shapes(slide.shapes):
            if s.shape_type == MSO_SHAPE_TYPE.PICTURE:
                total += 1
    return total


def has_footer_signature(all_text: str, meta: dict) -> bool:
    """No author/specialty strings should appear in slide text."""
    author = (meta.get("author") or "").strip()
    specialty = (meta.get("specialty") or "").strip()
    bad = []
    if author and author in all_text:
        bad.append(f"author={author!r}")
    if specialty and specialty in all_text:
        bad.append(f"specialty={specialty!r}")
    return bad


def page_number_tokens(text: str) -> list[str]:
    """slider3636 page-number badge uses TWO spaces around `/`
    (e.g. ``37  /  91``). Require whitespace around `/` so medical
    ``type 3/4`` does not false-positive."""
    return re.findall(r"\b\d+\s+\/\s+\d+\b", text)


def main():
    failures: list[str] = []
    if not PPTX.exists():
        raise SystemExit(f"Missing PPTX: {PPTX}")
    if not DECK.exists():
        raise SystemExit(f"Missing deck JSON: {DECK}")
    if not PROV.exists():
        raise SystemExit(f"Missing provenance JSON: {PROV}")

    deck = json.loads(DECK.read_text(encoding="utf-8"))
    prov = json.loads(PROV.read_text(encoding="utf-8"))
    meta = deck.get("meta", {})
    slides = deck.get("slides", [])
    prov_slides = prov.get("slides", [])

    prs = Presentation(str(PPTX))
    slide_texts = [slide_text(slide).strip() for slide in prs.slides]
    all_text = "\n".join(slide_texts)

    print(f"PPTX: {PPTX}")
    print(f"slides: {len(prs.slides)}")
    print(f"deck_slides: {len(slides)}")
    print(f"provenance_entries: {len(prov_slides)}")

    if len(prs.slides) == len(slides) == len(prov_slides):
        ok(f"counts match: {len(prs.slides)}")
    else:
        fail(f"count mismatch pptx={len(prs.slides)} deck={len(slides)} prov={len(prov_slides)}",
             failures)

    src = Path(prov.get("source_docx", ""))
    if src.resolve() == APPROVED_DOCX.resolve():
        ok("approved DOCX source path")
    else:
        fail(f"wrong provenance source {src}", failures)

    wrong_sources = []
    for e in prov_slides:
        if Path(e.get("source_docx", "")).resolve() != APPROVED_DOCX.resolve():
            wrong_sources.append(e.get("slide_index"))
    if not wrong_sources:
        ok("all manifest entries use approved DOCX")
    else:
        fail(f"slides with wrong source: {wrong_sources[:20]}", failures)

    used_ids = {sid for e in prov_slides for sid in e.get("source_ids", [])}
    if REQUIRED_BACKBONE_TABLES <= used_ids:
        ok(f"required backbone tables covered: {sorted(REQUIRED_BACKBONE_TABLES)}")
    else:
        missing = sorted(REQUIRED_BACKBONE_TABLES - used_ids)
        fail(f"missing backbone tables: {missing}", failures)

    forbidden_hits = [x for x in FORBIDDEN_TEXT if x in all_text]
    if not forbidden_hits:
        ok("no forbidden/source-leak text in slides")
    else:
        fail(f"forbidden text hits: {forbidden_hits}", failures)

    english_hits = [x for x in FORBIDDEN_ENGLISH_VISIBLE if x in all_text]
    if not english_hits:
        ok("no visible English leakage")
    else:
        fail(f"visible English leakage: {english_hits}", failures)

    pics = picture_count(prs)
    if pics == 0:
        ok("no embedded factual images")
    else:
        fail(f"embedded picture count should be 0, got {pics}", failures)

    # Footer signature: meta.author / meta.specialty must be empty AND not appear in slide text.
    bad_sig = has_footer_signature(all_text, meta)
    if not bad_sig:
        ok("no author / specialty footer signature")
    else:
        fail(f"footer signature present: {bad_sig}", failures)

    # Section ordering: match against section-divider slides specifically,
    # not arbitrary text matches (which false-positive on chapter names in body text).
    pos = []
    section_divider_pos = []  # (index, title) for every section divider
    for i, slide in enumerate(prs.slides, 1):
        stype = slides[i-1].get("type") if i <= len(slides) else None
        if stype == "section":
            title = slides[i-1].get("part_title", "")
            section_divider_pos.append((i, title))
    for title in REQUIRED_SECTION_TITLES:
        matches = [(i, t) for i, t in section_divider_pos if t == title]
        if not matches:
            # Allow short-title variants (e.g., section uses a shortener)
            shorter = title.split(" ")[0]
            matches = [(i, t) for i, t in section_divider_pos if shorter and shorter in t]
        if not matches:
            fail(f"missing section title: {title}", failures)
            continue
        if len(matches) > 1:
            fail(f"ambiguous section title {title!r}: {matches}", failures)
            continue
        pos.append(matches[0][0])
    if len(pos) == len(REQUIRED_SECTION_TITLES) and pos == sorted(pos):
        ok(f"required sections present in order: {REQUIRED_SECTION_TITLES}")
    else:
        fail(f"sections out of order or missing: positions={pos}, expected order={REQUIRED_SECTION_TITLES}", failures)

    # Page-number badge: the engine places "N  /  M" with spaces around slash.
    # Medical "type 3/4" has no spaces. With SHOW_PAGE_NUM=False, footer is skipped.
    expected_numbered = sum(1 for s in slides if s.get("type") not in NO_PAGE_TYPES)
    page_number_count = sum(len(page_number_tokens(t)) for t in slide_texts)
    if page_number_count == 0:
        ok(f"no page-number badges rendered (numbered expected {expected_numbered})")
    else:
        sample = []
        for i, t in enumerate(slide_texts, 1):
            sample.append((i, page_number_tokens(t)))
        sample = [s for s in sample if s[1]][:20]
        fail(f"page-number badges found: {sample}", failures)

    # Notes/DOCX source presence.
    thin_notes = []
    missing_source_notes = []
    no_note_types = {"title", "outline", "section", "references", "transition"}
    for i, slide in enumerate(prs.slides, 1):
        n = notes_text(slide)
        stype = slides[i-1].get("type") if i <= len(slides) else ""
        if len(n) < 30:
            thin_notes.append(i)
        if stype not in no_note_types and "Nguồn DOCX:" not in n:
            missing_source_notes.append(i)
    if not thin_notes and not missing_source_notes:
        ok("speaker notes present with DOCX source IDs")
    else:
        if thin_notes:
            fail(f"thin notes: {thin_notes[:20]}", failures)
        if missing_source_notes:
            fail(f"notes lacking DOCX IDs: {missing_source_notes[:20]}", failures)

    # Density.
    dense = []
    too_dense = []
    for i, txt in enumerate(slide_texts, 1):
        n = len(txt)
        if n > DENSE_CHARS:
            dense.append((i, n))
        if n > MAX_VISIBLE_CHARS:
            too_dense.append((i, n))
    if not too_dense and len(dense) <= MAX_DENSE_SLIDES:
        ok(f"visible text density acceptable ({len(dense)} slides > {DENSE_CHARS})")
    else:
        if too_dense:
            fail(f"too dense slides >{MAX_VISIBLE_CHARS}: {too_dense[:20]}", failures)
        if len(dense) > MAX_DENSE_SLIDES:
            fail(f"too many dense slides >{DENSE_CHARS}: {dense[:20]}", failures)

    # Sparse slide gate: content slides (not structural) must have ≥ MIN_VISIBLE_CHARS.
    sparse_types = {"title", "section", "outline", "references", "transition", "key_message"}
    thin = []
    for i, txt in enumerate(slide_texts, 1):
        stype = slides[i-1].get("type") if i <= len(slides) else ""
        if stype in sparse_types:
            continue
        core = re.sub(r"\b\d+\s+/\s+\d+\b", "", txt).strip()
        if len(core) < MIN_VISIBLE_CHARS:
            thin.append((i, stype, len(core)))
    if not thin:
        ok(f"no sparse content slides (>= {MIN_VISIBLE_CHARS} chars)")
    else:
        fail(f"sparse slides <{MIN_VISIBLE_CHARS}: {thin[:20]}", failures)

    # Forbidden source name leak (case-sensitive, the script runs against deck_text elsewhere).
    forbidden_source_hits = []
    for name in [
        "Quá trình mổ u xơ", "Giải thích các bước phẫu thuật u xơ",
        "Hạn chế dính buồng tử cung", "PMC13278667_fulltext",
    ]:
        if name in all_text:
            forbidden_source_hits.append(name)
    if not forbidden_source_hits:
        ok("no side-source filename leaks")
    else:
        fail(f"side-source leaks: {forbidden_source_hits}", failures)

    print(f"text_chars: {len(all_text)}")
    print(f"picture_count: {pics}")
    print(f"dense_slides (>={DENSE_CHARS}): {dense[:10]}")
    print(f"page_number_badges: {page_number_count}")

    if failures:
        print("\nRESULT: FAIL")
        raise SystemExit(1)
    print("\nRESULT: PASS")


if __name__ == "__main__":
    main()
