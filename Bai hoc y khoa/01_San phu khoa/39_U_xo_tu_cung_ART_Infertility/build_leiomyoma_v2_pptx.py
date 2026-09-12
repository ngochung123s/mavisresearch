# -*- coding: utf-8 -*-
"""Build the v2 leiomyoma ART PPTX from deck JSON + provenance JSON.

User requirements:
- Use the slider3636 engine.
- Medical Teal palette + Arial + Large preset.
- No page numbers.
- No author / footer signature (no author / specialty metadata).
- Source-only content from the approved DOCX; notes carry Nguồn DOCX provenance.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

ROOT = Path(__file__).parent
DATE = "2026-07-14"
ENGINE = Path("F:/DL/slider3636.py")
DECK = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.deck.json"
PROVENANCE = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.provenance.json"
OUT = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.pptx"
APPROVED_DOCX = ROOT / "U_xo_tu_cung_ART_Infertility_2026-07-12.docx"

ALLOWED_WARNING_FIELDS = {"note"}


def load_slider():
    import types
    slider = types.ModuleType("slider3636")
    code_lines = []
    for line in ENGINE.read_text(encoding="utf-8").splitlines():
        if "Cell 5 · Theme Designer" in line:
            break
        stripped = line.lstrip()
        if stripped.startswith("!") or stripped.startswith("%"):
            continue
        code_lines.append(line)
    exec(compile("\n".join(code_lines), str(ENGINE), "exec"), slider.__dict__)
    return slider


def load_inputs():
    if not DECK.exists():
        raise SystemExit(f"Missing deck JSON: {DECK}")
    if not PROVENANCE.exists():
        raise SystemExit(f"Missing provenance JSON: {PROVENANCE}")
    deck = json.loads(DECK.read_text(encoding="utf-8"))
    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    slides = deck.get("slides", [])
    prov_slides = provenance.get("slides", [])
    if len(prov_slides) != len(slides):
        raise SystemExit(f"Provenance has {len(prov_slides)} entries; deck has {len(slides)}")
    src = Path(provenance.get("source_docx", ""))
    if src.resolve() != APPROVED_DOCX.resolve():
        raise SystemExit(f"Forbidden provenance source: {src}")
    for i, entry in enumerate(prov_slides, 1):
        if entry.get("slide_index") != i:
            raise SystemExit(f"Provenance index mismatch at {i}: {entry.get('slide_index')}")
        if Path(entry.get("source_docx", "")).resolve() != APPROVED_DOCX.resolve():
            raise SystemExit(f"Slide {i} has forbidden source: {entry.get('source_docx')}")
    return deck, provenance


def apply_theme(slider):
    """Set the active palette/font/sizes for the build call."""
    import __main__
    class T: pass
    for k, v in slider.PALETTES["🟢 Medical Teal"].items():
        setattr(T, k, v)
    __main__.T = T()
    __main__.ACTIVE_PALETTE_NAME = "🟢 Medical Teal"
    __main__.ACTIVE_FONT = "Arial"
    __main__.ACTIVE_FONT_SIZES = slider.FONT_SIZE_PRESETS["Large — hội trường lớn"].copy()
    # User requirement: no page numbers, no author signature.
    __main__.SHOW_PAGE_NUM = False


def strip_footer_signature(deck: dict) -> dict:
    """Force-empty author/specialty so the footer_text concatenated from
    `meta.title + meta.author + meta.subtitle` contains only the title."""
    deck = json.loads(json.dumps(deck, ensure_ascii=False))
    meta = deck.get("meta", {})
    meta["author"] = ""
    meta["specialty"] = ""
    deck["meta"] = meta
    return deck


def patch_notes(pptx_path: Path, deck: dict):
    """Re-apply notes directly to ensure the Nguồn DOCX provenance is present
    even when the engine variant didn't write a note."""
    prs = Presentation(str(pptx_path))
    specs = deck["slides"]
    if len(prs.slides) != len(specs):
        raise SystemExit(f"PPTX slide count {len(prs.slides)} != deck {len(specs)}")
    for i, slide in enumerate(prs.slides):
        spec = specs[i]
        note_text = spec.get("note")
        if not note_text:
            if spec.get("type") in {"title", "outline", "section", "reference"}:
                note_text = f"Structural slide. Nguồn DOCX: {APPROVED_DOCX.name}."
            else:
                raise SystemExit(f"Slide {i+1} missing note")
        slide.notes_slide.notes_text_frame.text = note_text
    prs.save(str(pptx_path))


def actual_slide_count(pptx_path: Path) -> int:
    return len(Presentation(str(pptx_path)).slides)


def validate_warnings(warnings):
    bad = []
    for w in warnings:
        m = re.search(r"field không nhận diện: ([^()]+)", w)
        if not m:
            bad.append(w)
            continue
        fields = {x.strip() for x in m.group(1).split(",")}
        if not fields <= ALLOWED_WARNING_FIELDS:
            bad.append(w)
    if bad:
        print("UNACCEPTABLE WARNINGS:")
        for w in bad[:30]:
            print(" -", w)
        if len(bad) > 30:
            print(f" - ... {len(bad)-30} more")
        raise SystemExit(2)


def main():
    deck, provenance = load_inputs()
    slider = load_slider()
    apply_theme(slider)

    # Render with cleared author/specialty to suppress footer signature.
    deck_clean = strip_footer_signature(deck)
    slides = deck_clean["slides"]

    errors, warnings = slider.validate_deck(slides)
    validate_warnings(warnings)
    if errors:
        print("ERRORS:")
        for e in errors:
            print(" -", e)
        raise SystemExit(2)

    path, rendered = slider.build_presentation(deck_clean, str(OUT))
    if rendered != len(slides):
        raise SystemExit(f"Rendered {rendered}/{len(slides)}; refusing partial PPTX")
    if actual_slide_count(path) != len(slides):
        raise SystemExit(f"Actual PPTX slide count {actual_slide_count(path)} != {len(slides)}")

    patch_notes(path, deck_clean)
    if actual_slide_count(path) != len(slides):
        raise SystemExit(f"Patched PPTX slide count changed: {actual_slide_count(path)}")

    print(f"OK: rendered {rendered}/{len(slides)} slides -> {path}")
    print(f"Deck JSON: {DECK}")
    print(f"Provenance: {PROVENANCE}")


if __name__ == "__main__":
    main()
