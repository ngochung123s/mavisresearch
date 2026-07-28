"""Canonical fail-closed release runner for medical lessons.

Usage:
  python build_pipeline.py --brief BRIEF.md --lesson RELEASE.md \
      --cards RELEASE.cards.v2.json --guidelines guideline_evidence.json

The runner executes every gate in the brief contract, stores command output as
an artifact, hashes inputs/artifacts, writes ``gate-results.json``, and invokes
``publish_gate.py``. It never writes the catalog.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Callable

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from publish_gate import extract_contract, validate_contract
from verification_core import sha256_file
from verify_apkg_diacritics import verify_apkg
from verify_diacritics import count_words_classified


def hashed(path: Path) -> dict[str, str]:
    resolved = path.resolve()
    return {"path": str(resolved), "sha256": sha256_file(resolved)}


def run(command: list[str], timeout: int = 300) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, capture_output=True, text=True, timeout=timeout, cwd=SCRIPT_DIR)


def write_command_artifact(path: Path, completed: subprocess.CompletedProcess[str]) -> None:
    path.write_text(
        json.dumps({"returncode": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_cards(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cards = data if isinstance(data, list) else data.get("cards") if isinstance(data, dict) else None
    if not isinstance(cards, list) or not cards:
        raise ValueError("cards JSON must contain a non-empty card list")
    for index, card in enumerate(cards, 1):
        if not isinstance(card, dict):
            raise ValueError(f"card {index} is not an object")
        card_type = card.get("type", "basic")
        if card_type == "basic" and not str(card.get("front", "")).strip():
            raise ValueError(f"basic card {index} has an empty front")
        if card_type == "basic" and not str(card.get("back", "")).strip():
            raise ValueError(f"basic card {index} has an empty back")
        if card_type == "cloze" and not re.search(r"\{\{c\d+::.+?\}\}", str(card.get("text", ""))):
            raise ValueError(f"cloze card {index} has no valid cloze field")
        if card_type not in {"basic", "cloze"}:
            raise ValueError(f"card {index} has unsupported type {card_type!r}")
    return cards


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all required release gates and produce hashed evidence")
    parser.add_argument("--brief", required=True, type=Path)
    parser.add_argument("--lesson", required=True, type=Path)
    parser.add_argument("--cards", required=True, type=Path)
    parser.add_argument("--guidelines", required=True, type=Path, help="Guideline evidence JSON")
    parser.add_argument("--outputs", type=Path, help="Release outputs folder; default: <lesson-dir>/outputs")
    args = parser.parse_args()

    for path in (args.brief, args.lesson, args.cards, args.guidelines):
        if not path.is_file():
            parser.error(f"file not found: {path}")

    contract = extract_contract(args.brief.read_text(encoding="utf-8"))
    profile, required = validate_contract(contract)
    release_id = args.lesson.stem
    outputs = (args.outputs or args.lesson.parent / "outputs").resolve()
    evidence_dir = outputs / "verification" / release_id
    evidence_dir.mkdir(parents=True, exist_ok=True)
    apkg = outputs / f"{release_id}.apkg"
    docx = outputs / f"{release_id}.docx"
    results_path = evidence_dir / "gate-results.json"
    results: list[dict] = []

    def record(gate: str, command: list[str], inputs: list[Path], artifacts: list[Path], exit_code: int) -> None:
        if gate not in required:
            return
        missing = [str(path) for path in artifacts if not path.is_file()]
        status = "PASS" if exit_code == 0 and not missing else "FAIL"
        results.append({
            "gate": gate,
            "status": status,
            "command": command,
            "exit_code": exit_code if not missing else max(exit_code, 2),
            "release_id": release_id,
            "inputs": [hashed(path) for path in inputs],
            "artifacts": [hashed(path) for path in artifacts if path.is_file()],
        })

    def command_gate(gate: str, command: list[str], inputs: list[Path], artifact_name: str, timeout: int = 300) -> int:
        artifact = evidence_dir / artifact_name
        completed = run(command, timeout)
        write_command_artifact(artifact, completed)
        record(gate, command, inputs, [artifact], completed.returncode)
        print(f"[{results[-1]['status']}] {gate}")
        return completed.returncode

    python = sys.executable
    command_gate("brief_pmid_preflight", [python, str(SCRIPT_DIR / "preflight_check_pmids.py"), str(args.brief), "--strict", "--json"], [args.brief], "brief_pmid_preflight.json")
    brief_claim_report = evidence_dir / "brief_claims_report.json"
    command_gate("brief_claims_strict", [python, str(SCRIPT_DIR / "verify_claim_vs_abstract.py"), str(args.brief), "--json-out", str(brief_claim_report)], [args.brief], "brief_claims_command.json")
    if results[-1]["gate"] == "brief_claims_strict" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(brief_claim_report))
    command_gate("source_pmid_strict", [python, str(SCRIPT_DIR / "verify_all_pmids.py"), str(args.lesson), "--strict", "--json"], [args.lesson], "source_pmid_strict.json")
    claims_report = evidence_dir / "source_claims_report.json"
    command_gate("source_claims_strict", [python, str(SCRIPT_DIR / "verify_claims.py"), str(args.lesson), "--strict", "--json-out", str(claims_report)], [args.lesson], "source_claims_command.json")
    if results[-1]["gate"] == "source_claims_strict" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(claims_report))
    retraction_report = evidence_dir / "source_retraction_report.json"
    command_gate("source_retraction", [python, str(SCRIPT_DIR / "retraction_check.py"), "--md", str(args.lesson), "--strict", "--json-out", str(retraction_report)], [args.lesson], "source_retraction_command.json")
    if results[-1]["gate"] == "source_retraction" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(retraction_report))
    guideline_report = evidence_dir / "guideline_report.json"
    command_gate("guideline_evidence", [python, str(SCRIPT_DIR / "verify_guidelines.py"), str(args.guidelines), "--json-out", str(guideline_report)], [args.guidelines], "guideline_command.json")
    if results[-1]["gate"] == "guideline_evidence" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(guideline_report))

    citation_command = [python, str(SCRIPT_DIR / "citation_audit.py"), str(args.lesson), "--json"]
    citation_run = run(citation_command)
    citation_artifact = evidence_dir / "citation_audit.json"
    citation_artifact.write_text(citation_run.stdout or json.dumps({"error": citation_run.stderr}), encoding="utf-8")
    citation_code = citation_run.returncode
    try:
        summary = json.loads(citation_run.stdout)["summary"]
        if summary.get("block", 0) != 0 or summary.get("warn", 0) != 0:
            citation_code = 2
    except (json.JSONDecodeError, KeyError, TypeError):
        citation_code = 2
    record("citation_zero_block", citation_command, [args.lesson], [citation_artifact], citation_code)
    print(f"[{results[-1]['status']}] citation_zero_block")

    structure_gate = "depth_disease" if profile == "disease" else f"profile_{profile}"
    structure_script = "depth_check.py" if profile == "disease" else "profile_check.py"
    structure_args = [str(args.lesson), "--profile", profile] if profile == "disease" else [profile, str(args.lesson)]
    command_gate(structure_gate, [python, str(SCRIPT_DIR / structure_script), *structure_args], [args.lesson], f"{structure_gate}.json")

    cards_artifact = evidence_dir / "cards_schema.json"
    try:
        cards = load_cards(args.cards)
        cards_artifact.write_text(json.dumps({"status": "PASS", "card_count": len(cards)}, indent=2), encoding="utf-8")
        cards_code = 0
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        cards = []
        cards_artifact.write_text(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2), encoding="utf-8")
        cards_code = 2
    record("cards_schema", [python, str(Path(__file__).resolve()), "--internal", "cards_schema"], [args.cards], [cards_artifact], cards_code)
    print(f"[{results[-1]['status']}] cards_schema")

    command_gate("candidate_apkg_build", [python, str(SCRIPT_DIR / "build_apkg.py"), str(args.cards), "--output", str(apkg), "--verify"], [args.cards], "candidate_apkg_build.json")
    if results[-1]["gate"] == "candidate_apkg_build" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(apkg))

    package_artifact = evidence_dir / "package_counts.json"
    try:
        ratio, _, _, notes, package_cards = verify_apkg(apkg)
        expected = len(cards)
        ok = ratio is not None and notes == expected and package_cards >= notes and notes > 0
        package_artifact.write_text(json.dumps({"expected_notes": expected, "actual_notes": notes, "actual_cards": package_cards, "status": "PASS" if ok else "FAIL"}, indent=2), encoding="utf-8")
        package_code = 0 if ok else 2
    except Exception as exc:
        package_artifact.write_text(json.dumps({"status": "FAIL", "error": str(exc)}, indent=2), encoding="utf-8")
        package_code = 2
    record("package_note_count", [python, str(Path(__file__).resolve()), "internal:package_note_count"], [args.cards, apkg] if apkg.is_file() else [args.cards], [package_artifact], package_code)
    print(f"[{results[-1]['status']}] package_note_count")
    if apkg.is_file():
        command_gate("package_diacritics", [python, str(SCRIPT_DIR / "verify_apkg_diacritics.py"), str(apkg)], [apkg], "package_diacritics.json")
    else:
        missing_apkg = evidence_dir / "package_diacritics.json"
        missing_apkg.write_text(json.dumps({"status": "FAIL", "error": "APKG missing"}), encoding="utf-8")
        record("package_diacritics", [python, str(SCRIPT_DIR / "verify_apkg_diacritics.py"), str(apkg)], [args.cards], [missing_apkg], 2)
        print("[FAIL] package_diacritics")

    source_artifact = evidence_dir / "source_diacritics.json"
    vn_diac, vn_no_diac, other = count_words_classified(args.lesson.read_text(encoding="utf-8"))
    vn_total = vn_diac + vn_no_diac
    ratio = vn_diac / vn_total if vn_total else 1.0
    source_code = 0 if ratio >= 0.80 else 2
    source_artifact.write_text(json.dumps({"ratio": ratio, "vn_diacritics": vn_diac, "vn_total": vn_total, "other": other, "status": "PASS" if source_code == 0 else "FAIL"}, ensure_ascii=False, indent=2), encoding="utf-8")
    record("source_diacritics", [python, str(Path(__file__).resolve()), "internal:source_diacritics"], [args.lesson], [source_artifact], source_code)
    print(f"[{results[-1]['status']}] source_diacritics")

    command_gate("docx_build", [python, str(SCRIPT_DIR / "md_to_docx.py"), str(args.lesson), str(docx)], [args.lesson], "docx_build.json")
    if results[-1]["gate"] == "docx_build" and results[-1]["status"] == "PASS":
        results[-1]["artifacts"].append(hashed(docx))

    learner_command = [python, str(SCRIPT_DIR / "make_knowledge_check.py"), str(args.cards), "--output-dir", str(outputs)]
    learner_run = run(learner_command)
    learner_artifact = evidence_dir / "learner_smoke.json"
    score_path = outputs / f"{args.cards.stem.replace('.cards', '').replace('.v2', '')}_knowledge_check_score.json"
    learner_code = learner_run.returncode
    learner_paths = [
        outputs / f"{args.cards.stem.replace('.cards', '').replace('.v2', '')}_knowledge_check.md",
        outputs / f"{args.cards.stem.replace('.cards', '').replace('.v2', '')}_knowledge_check_answer_key.md",
        score_path,
    ]
    try:
        score = json.loads(score_path.read_text(encoding="utf-8"))
        if (
            score.get("total_questions", 0) <= 0
            or len(score.get("section_counts", {})) != 5
            or score.get("status") != "not_graded"
            or any(not path.is_file() or path.stat().st_size == 0 for path in learner_paths)
        ):
            learner_code = 2
    except (OSError, json.JSONDecodeError):
        learner_code = 2
    write_command_artifact(learner_artifact, learner_run)
    learner_outputs = [learner_artifact, *(path for path in learner_paths if path.is_file())]
    record("learner_smoke", learner_command, [args.cards], learner_outputs, learner_code)
    print(f"[{results[-1]['status']}] learner_smoke")

    results_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    publish = run([python, str(SCRIPT_DIR / "publish_gate.py"), str(args.brief), "--results", str(results_path)])
    print(publish.stdout, end="")
    if publish.stderr:
        print(publish.stderr, file=sys.stderr, end="")
    return publish.returncode


if __name__ == "__main__":
    raise SystemExit(main())
