# -*- coding: utf-8 -*-
"""release_lesson.py — MỘT lệnh phát hành bài học + APKG cho MỌI chuyên khoa.

    python release_lesson.py <lesson_dir> [--mode release|hotfix] [--sync-anki]
                             [--evidence-bundle bundle.json --guidelines guideline_evidence.json]

Trình tự (RULES_LESSON_APKG.md §2):
  1. lesson.json hợp lệ (mã bài, chuyên khoa, profile, đường dẫn)
  2. lesson_lint  — cấu trúc/chiều sâu/định dạng/ảnh/nhãn verification của bài .md
  3. evidence     — chuyên khoa `evidence_bundle`: build_pipeline.py (offline, 7 gate nguồn + DOCX + learner smoke,
                    APKG candidate do deck_builder build) ; `ncbi_artifacts`: nhãn ↔ artifact đã kiểm ở bước 2
  4. deck_builder — card_lint + APKG + verify (+ đồng bộ Anki tại chỗ nếu --sync-anki)
  5. post_release — script của chuyên khoa trong specialties.json (vd. build_unified_med_library.py)
Mode `release` (bài mới/viết lại): mọi gate BLOCK. Mode `hotfix` (bài cũ): lỗi bài + governance thẻ chỉ ghi nợ,
không chạy build_pipeline, chỉ chặn lỗi kỹ thuật của thẻ.
Kết quả: outputs/verification/<basename>/release.json. Exit 0 = phát hành được, 2 = BLOCK.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import deck_builder  # noqa: E402
import lesson_lint  # noqa: E402
import lesson_manifest  # noqa: E402


def run_script(args: list[str], cwd: Path | None = None) -> int:
    print(f"  $ {' '.join(args)}")
    return subprocess.run([sys.executable, *args], cwd=cwd).returncode


def pipeline(m: lesson_manifest.Manifest, bundle: Path, guidelines: Path) -> int:
    return run_script([str(SCRIPT_DIR / "build_pipeline.py"), "--brief", str(m.lesson_dir / m.brief),
                       "--lesson", str(m.lesson_path), "--cards", str(m.cards_source_path),
                       "--guidelines", str(guidelines), "--evidence-bundle", str(bundle)])


def release(lesson_dir: Path, mode: str, sync_anki: bool, bundle: Path | None, guidelines: Path | None) -> int:
    m = lesson_manifest.load(lesson_dir)
    steps: list[dict] = []

    def step(name: str, code: int) -> bool:
        steps.append({"step": name, "exit_code": code, "status": "PASS" if code == 0 else "BLOCK"})
        print(f"[{'PASS' if code == 0 else 'BLOCK'}] {name}")
        return code == 0

    def finish(status: str) -> int:
        m.verify_dir.mkdir(parents=True, exist_ok=True)
        (m.verify_dir / "release.json").write_text(json.dumps(
            {"id": m.id, "specialty": m.specialty.key, "mode": mode, "status": status, "steps": steps,
             "finished_at": dt.datetime.now().isoformat(timespec="seconds")}, ensure_ascii=False, indent=2),
            encoding="utf-8")
        print(f"=== {m.id}: {status} ===")
        if status != "BLOCK":
            print("  Tiếp theo: cập nhật dòng trạng thái trong", m.specialty.curriculum, "→ git commit + push (RULES §2 bước 5).")
        return 0 if status != "BLOCK" else 2

    print(f"##### RELEASE {m.id} — {m.specialty.name} — evidence={m.specialty.evidence_mode} — mode={mode}")
    errors = lesson_manifest.validate(m)
    for e in errors:
        print(f"  [BLOCK] lesson.json: {e}")
    if not step("manifest", 2 if errors else 0):
        return finish("BLOCK")

    code, lesson_issues = lesson_lint.run(m.lesson_dir, mode)
    if not step("lesson_lint", code):
        return finish("BLOCK")

    use_pipeline = mode == "release" and m.specialty.evidence_mode == "evidence_bundle"
    if use_pipeline:
        if not (bundle and guidelines and m.brief):
            print("  [BLOCK] chuyên khoa evidence_bundle cần --evidence-bundle, --guidelines và `brief` trong lesson.json")
            step("evidence_pipeline", 2)
            return finish("BLOCK")
        if not step("evidence_pipeline", pipeline(m, bundle, guidelines)):
            return finish("BLOCK")
        if sync_anki:
            # đồng bộ Anki (lấy GUID thật) rồi chạy lại pipeline để manifest băm đúng APKG cuối cùng
            if not step("deck_builder+anki", deck_builder.build(m.lesson_dir, mode, True, False)):
                return finish("BLOCK")
            if not step("evidence_pipeline (final)", pipeline(m, bundle, guidelines)):
                return finish("BLOCK")
    elif not step("deck_builder" + ("+anki" if sync_anki else ""), deck_builder.build(m.lesson_dir, mode, sync_anki, False)):
        return finish("BLOCK")

    for script in m.specialty.post_release:
        if not step(f"post_release {script}", run_script([str(lesson_manifest.specialties.LESSONS_ROOT / script)])):
            return finish("BLOCK")

    card_report = json.loads((m.verify_dir / "card-lint.json").read_text(encoding="utf-8"))
    debt = card_report["summary"]["debt"] + sum(1 for i in lesson_issues if i.severity == "DEBT")
    return finish("PUBLISH_READY" if mode == "release" else ("PASS_WITH_DEBT" if debt else "PASS"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lesson_dir", type=Path)
    ap.add_argument("--mode", default="release", choices=["release", "hotfix"])
    ap.add_argument("--sync-anki", action="store_true")
    ap.add_argument("--evidence-bundle", type=Path)
    ap.add_argument("--guidelines", type=Path)
    args = ap.parse_args(argv)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        return release(args.lesson_dir.resolve(), args.mode, args.sync_anki, args.evidence_bundle, args.guidelines)
    except lesson_manifest.ManifestError as exc:
        print(f"[BLOCK] {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
