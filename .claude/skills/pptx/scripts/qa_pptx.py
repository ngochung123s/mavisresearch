#!/usr/bin/env python3
"""Blocking QA checks for PPTX decks created by the pptx skill.

Canonical mode enforces the skill contract: 10 x 5.625 in canvas,
page badges, no overflow, no placeholders. Use --legacy to inspect older
13.33 x 7.5 python-pptx decks without failing only for canvas/page badges.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from dataclasses import dataclass
from pathlib import Path

try:
    from load_settings import load_settings
except ImportError:  # pragma: no cover
    load_settings = None

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

CANONICAL_W = 10.0
CANONICAL_H = 5.625
LEGACY_W = 13.33
LEGACY_H = 7.5
TOL = 0.02
PLACEHOLDER_RE = re.compile(r"xxxx|lorem|ipsum|placeholder|this\s+.*(page|slide).*layout", re.I)
PMID_RE = re.compile(r"\bPMID\s*:?\s*\d{7,8}\b", re.I)
PAGE_BADGE_RE = re.compile(r"\b\d+\s*/\s*\d+\b")


@dataclass
class Finding:
    level: str
    slide: int | None
    message: str


def inches(emu: int) -> float:
    return emu / 914400


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def iter_shapes(shapes):
    for shape in shapes:
        yield shape
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from iter_shapes(shape.shapes)


def shape_text(shape) -> str:
    chunks: list[str] = []
    if getattr(shape, "has_text_frame", False):
        chunks.append(shape.text_frame.text or "")
    if getattr(shape, "has_table", False):
        for row in shape.table.rows:
            for cell in row.cells:
                chunks.append(cell.text or "")
    return "\n".join(c for c in chunks if c)


def slide_text(slide) -> str:
    chunks = [shape_text(s) for s in iter_shapes(slide.shapes)]
    return "\n".join(c for c in chunks if c)


def notes_text(slide) -> str:
    if not slide.has_notes_slide:
        return ""
    return (slide.notes_slide.notes_text_frame.text or "").strip()


def check_deck(args: argparse.Namespace) -> list[Finding]:
    prs = Presentation(args.pptx_path)
    findings: list[Finding] = []
    slide_w = inches(prs.slide_width)
    slide_h = inches(prs.slide_height)

    if getattr(args, "check_canvas", True) and args.legacy:
        if not (close(slide_w, CANONICAL_W) and close(slide_h, CANONICAL_H)) and not (
            close(slide_w, LEGACY_W, 0.05) and close(slide_h, LEGACY_H, 0.05)
        ):
            findings.append(Finding("fail", None, f"unexpected legacy slide size {slide_w:.3f} x {slide_h:.3f} in"))
    elif getattr(args, "check_canvas", True):
        if not (close(slide_w, CANONICAL_W) and close(slide_h, CANONICAL_H)):
            findings.append(Finding("fail", None, f"slide size {slide_w:.3f} x {slide_h:.3f} in, expected 10.000 x 5.625"))

    footer_counts: dict[str, int] = {}
    total_images = 0

    for idx, slide in enumerate(prs.slides, 1):
        text = slide_text(slide)
        flat_text = " ".join(text.split())
        if getattr(args, "check_placeholder", True) and PLACEHOLDER_RE.search(text):
            findings.append(Finding("fail", idx, "placeholder/demo text remains"))
        if getattr(args, "check_thin_slides", True) and idx > 1 and len(flat_text) < args.min_chars:
            findings.append(Finding("warn" if args.allow_thin else "fail", idx, f"thin slide text ({len(flat_text)} chars)"))

        if getattr(args, "check_page_badge", True) and not args.legacy and idx > 1 and not PAGE_BADGE_RE.search(text):
            findings.append(Finding("fail", idx, "missing page badge like '2 / 12' on non-cover slide"))

        if (args.require_notes or args.medical) and idx > 1:
            note = notes_text(slide)
            if len(note) < args.min_note_chars:
                findings.append(Finding("fail", idx, f"speaker notes missing or too thin ({len(note)} chars)"))
            elif args.medical and ("tại sao" not in note.lower() and "why" not in note.lower()):
                findings.append(Finding("warn", idx, "medical notes do not include a why/rationale cue"))

        for line in text.splitlines():
            if PMID_RE.search(line):
                normalized = " ".join(line.split())
                footer_counts[normalized] = footer_counts.get(normalized, 0) + 1

        for shape in iter_shapes(slide.shapes):
            try:
                x, y, w, h = map(inches, (shape.left, shape.top, shape.width, shape.height))
            except Exception:
                continue
            if getattr(args, "check_overflow", True) and (x < -TOL or y < -TOL or x + w > slide_w + TOL or y + h > slide_h + TOL):
                findings.append(Finding("fail", idx, f"shape out of bounds: {getattr(shape, 'name', 'shape')} @ {x:.2f},{y:.2f} {w:.2f}x{h:.2f}"))

            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                total_images += 1
                if args.require_image_sources:
                    descr = getattr(shape, "_element", None)
                    # python-pptx does not expose alt text consistently; use the visible slide text as the enforceable contract.
                    if not re.search(r"(source|nguồn|license|permission|PMID|DOI)", text, re.I):
                        findings.append(Finding("fail", idx, "image present without visible source/license/provenance cue"))

    slide_count = len(prs.slides)
    repeated = [footer for footer, count in footer_counts.items() if slide_count > 5 and count >= max(5, slide_count // 3)]
    if repeated and not args.allow_repeated_citations:
        findings.append(Finding("warn", None, f"generic repeated PMID footer appears on many slides ({len(repeated)} repeated line(s))"))

    if args.require_image_sources and total_images == 0:
        findings.append(Finding("warn", None, "--require-image-sources set, but deck contains no pictures"))

    if args.render:
        findings.extend(check_render(args.pptx_path, slide_count, args.render_outdir))

    return findings


def check_render(pptx_path: str, slide_count: int, outdir: str | None) -> list[Finding]:
    findings: list[Finding] = []
    target = Path(outdir) if outdir else Path(tempfile.mkdtemp(prefix="pptx_render_"))
    target.mkdir(parents=True, exist_ok=True)

    if sys.platform.startswith("win"):
        ok = export_with_powerpoint(pptx_path, target, getattr(check_render, "try_powerpoint", True))
        if not ok:
            ok = export_with_libreoffice(pptx_path, target, getattr(check_render, "try_libreoffice", True))
    else:
        ok = export_with_libreoffice(pptx_path, target, getattr(check_render, "try_libreoffice", True))

    if not ok:
        findings.append(Finding("fail", None, "render export unavailable or failed; install PowerPoint or LibreOffice for visual QA"))
        return findings

    images = sorted([p for p in target.rglob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg"}])
    if len(images) < slide_count:
        findings.append(Finding("fail", None, f"render produced {len(images)} image(s), expected at least {slide_count}"))
    for image in images:
        if image.stat().st_size == 0:
            findings.append(Finding("fail", None, f"empty rendered image: {image}"))
    if outdir:
        findings.append(Finding("info", None, f"rendered previews: {target}"))
    else:
        shutil.rmtree(target, ignore_errors=True)
    return findings


def export_with_powerpoint(pptx_path: str, outdir: Path, enabled: bool = True) -> bool:
    if not enabled:
        return False
    if not sys.platform.startswith("win"):
        return False
    script = f'''
$ErrorActionPreference = "Stop"
$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open("{Path(pptx_path).resolve()}", $true, $false, $false)
$pres.Export("{outdir.resolve()}", "PNG")
$pres.Close()
$ppt.Quit()
'''
    try:
        result = subprocess.run(["powershell", "-NoProfile", "-Command", script], capture_output=True, text=True, timeout=120)
        return result.returncode == 0
    except Exception:
        return False


def export_with_libreoffice(pptx_path: str, outdir: Path, enabled: bool = True) -> bool:
    if not enabled:
        return False
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return False
    try:
        result = subprocess.run(
            [soffice, "--headless", "--convert-to", "png", "--outdir", str(outdir), pptx_path],
            capture_output=True,
            text=True,
            timeout=120,
        )
        return result.returncode == 0
    except Exception:
        return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run blocking QA checks for PPTX skill outputs.")
    parser.add_argument("pptx_path", nargs="?", help="PPTX file to check")
    parser.add_argument("--legacy", action="store_true", help="Permit legacy 13.33 x 7.5 decks and skip page-badge enforcement")
    parser.add_argument("--medical", action="store_true", help="Require useful notes and prefer why/rationale cues")
    parser.add_argument("--require-notes", action="store_true", help="Require speaker notes on non-cover slides")
    parser.add_argument("--require-image-sources", action="store_true", help="Require visible image source/provenance cues on image slides")
    parser.add_argument("--allow-repeated-citations", action="store_true", help="Do not warn on repeated PMID footer lines")
    parser.add_argument("--allow-thin", action="store_true", help="Warn, not fail, on suspiciously thin non-cover slides")
    parser.add_argument("--min-chars", type=int, default=20, help="Minimum extracted text characters for non-cover slides")
    parser.add_argument("--min-note-chars", type=int, default=40, help="Minimum note characters when notes are required")
    parser.add_argument("--render", action="store_true", help="Attempt screenshot/render export and verify images exist")
    parser.add_argument("--render-outdir", help="Directory for rendered previews; temp dir is used and deleted if omitted")
    parser.add_argument("--config", help="Path to PPTX skill settings.json; defaults to ../settings.json")
    parser.add_argument("--no-config", action="store_true", help="Ignore settings.json and use CLI/defaults only")
    parser.add_argument("--self-test", action="store_true", help="Run a small assertion-based self-test and exit")
    return parser.parse_args()


def run_self_test() -> int:
    from pptx import Presentation
    from pptx.util import Inches

    tmp = Path(tempfile.mkdtemp(prefix="pptx_qa_selftest_"))
    try:
        good = tmp / "good.pptx"
        prs = Presentation()
        prs.slide_width = Inches(10)
        prs.slide_height = Inches(5.625)
        blank = prs.slide_layouts[6]
        prs.slides.add_slide(blank).shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(5), Inches(1)).text_frame.text = "Cover"
        s2 = prs.slides.add_slide(blank)
        s2.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(5), Inches(1)).text_frame.text = "Body text with enough content\n2 / 2"
        s2.notes_slide.notes_text_frame.text = "Làm gì? Test. Tại sao làm vậy? Verify notes."
        prs.save(good)
        args = argparse.Namespace(
            pptx_path=str(good), legacy=False, medical=True, require_notes=True,
            require_image_sources=False, allow_repeated_citations=True, allow_thin=False,
            min_chars=20, min_note_chars=20, render=False, render_outdir=None,
        )
        assert not [f for f in check_deck(args) if f.level == "fail"]

        bad = tmp / "bad.pptx"
        prs = Presentation()
        prs.slide_width = Inches(13.33)
        prs.slide_height = Inches(7.5)
        bad_blank = prs.slide_layouts[6]
        prs.slides.add_slide(bad_blank).shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(5), Inches(1)).text_frame.text = "Cover"
        prs.slides.add_slide(bad_blank).shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(5), Inches(1)).text_frame.text = "xxxx"
        prs.save(bad)
        args.pptx_path = str(bad)
        args.medical = False
        args.require_notes = False
        messages = [f.message for f in check_deck(args) if f.level == "fail"]
        assert any("slide size" in m for m in messages)
        assert any("placeholder" in m for m in messages)
        assert any("page badge" in m for m in messages)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("self-test passed")
    return 0




def apply_config(args: argparse.Namespace) -> argparse.Namespace:
    if args.no_config or load_settings is None:
        return args
    cfg = load_settings(args.config)
    qa = cfg.get("qa", {})
    med = cfg.get("medicalTeaching", {})
    render = cfg.get("render", {})
    citation = cfg.get("citation", {})

    if cfg.get("engine") == "slider3636" or cfg.get("canvas") == "legacy":
        args.legacy = True
    # medicalTeaching.enabled is a generation preference; QA uses --medical when notes should be checked.
    args.require_notes = args.require_notes or bool(qa.get("requireSpeakerNotes", False))
    args.require_image_sources = args.require_image_sources or bool(qa.get("requireImageSources", False))
    args.render = args.render or bool(render.get("enabled", False)) or bool(render.get("requireRenderPass", False))
    args.allow_repeated_citations = args.allow_repeated_citations or bool(
        citation.get("allowRepeatedPmidFooter", False)
    ) or not bool(qa.get("warnRepeatedCitations", True))

    # Setting switches can deliberately disable default gates. CLI flags can only tighten, not re-enable disabled gates.
    args.check_canvas = bool(qa.get("checkCanvas", True))
    args.check_overflow = bool(qa.get("checkOverflow", True))
    args.check_page_badge = bool(qa.get("checkPageBadge", True))
    args.check_placeholder = bool(qa.get("checkPlaceholder", True))
    args.check_thin_slides = bool(qa.get("checkThinSlides", True))
    check_render.try_powerpoint = bool(render.get("tryPowerPoint", True))
    check_render.try_libreoffice = bool(render.get("tryLibreOffice", True))
    return args

def main() -> int:
    args = apply_config(parse_args())
    if args.self_test:
        return run_self_test()
    if not os.path.isfile(args.pptx_path):
        print(f"File not found: {args.pptx_path}", file=sys.stderr)
        return 2

    findings = check_deck(args)
    failures = [f for f in findings if f.level == "fail"]
    warnings = [f for f in findings if f.level == "warn"]

    for finding in findings:
        loc = f"slide {finding.slide}" if finding.slide else "deck"
        print(f"[{finding.level.upper()}] {loc}: {finding.message}")

    if failures:
        print(f"\nQA FAILED: {len(failures)} failure(s), {len(warnings)} warning(s).")
        return 2
    if warnings:
        print(f"\nQA PASSED WITH WARNINGS: {len(warnings)} warning(s).")
        return 1
    print("QA PASSED: no blocking issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
