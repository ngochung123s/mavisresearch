import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from publish_gate import (
    DEFAULT_DEPTH_CONTRACTS,
    PROFILE_GATES,
    ContractError,
    extract_contract,
    load_results,
    validate_contract,
    validate_results,
)
from verification_core import sha256_file


def brief_with(contract: object, prefix: str = "") -> str:
    payload = json.dumps(contract, ensure_ascii=False, indent=2)
    return f"{prefix}\n## 0. Lesson profile & release contract\n\n```json\n{payload}\n```\n\n## 1. Papers đã chọn\n"


def valid_contract(profile: str = "disease") -> dict:
    return {
        "profile": profile,
        "mode": "L3_BEGINNER",
        "required_gates": list(PROFILE_GATES[profile]),
        "lesson_depth_contract": dict(DEFAULT_DEPTH_CONTRACTS[profile]),
        "not_applicable": [],
        "approved_exemptions": [],
    }


def evidence_rows(root: Path, profile: str = "disease") -> list[dict]:
    source = root / "release.md"
    source.write_text("release", encoding="utf-8")
    rows = []
    for gate in PROFILE_GATES[profile]:
        artifact = root / f"{gate}.json"
        artifact.write_text(json.dumps({"gate": gate}), encoding="utf-8")
        rows.append({
            "gate": gate, "status": "PASS", "command": ["python", f"{gate}.py"],
            "exit_code": 0, "release_id": "release-v1",
            "inputs": [{"path": str(source), "sha256": sha256_file(source)}],
            "artifacts": [{"path": str(artifact), "sha256": sha256_file(artifact)}],
        })
    return rows


class PublishGateTest(unittest.TestCase):
    def test_extracts_contract_only_from_its_heading(self):
        unrelated = "```json\n{\"not\": \"the contract\"}\n```\n"
        contract = valid_contract()
        self.assertEqual(extract_contract(brief_with(contract, unrelated)), contract)

    def test_duplicate_or_malformed_contract_is_rejected(self):
        contract = valid_contract()
        with self.assertRaisesRegex(ContractError, "duplicate release-contract heading"):
            extract_contract(brief_with(contract) + brief_with(contract))
        with self.assertRaisesRegex(ContractError, "missing heading"):
            extract_contract("## 1. Papers\n```json\n{}\n```")
        with self.assertRaisesRegex(ContractError, "malformed contract JSON"):
            extract_contract("## 0. Lesson profile & release contract\n```json\n{bad}\n```")

    def test_contract_is_exact_and_cannot_waive_required_gate(self):
        contract = valid_contract()
        contract["required_gates"].pop()
        with self.assertRaisesRegex(ContractError, "exactly match"):
            validate_contract(contract)
        contract = valid_contract()
        contract["not_applicable"] = ["depth_disease"]
        with self.assertRaisesRegex(ContractError, "cannot include required"):
            validate_contract(contract)

    def test_mode_and_depth_contract_validation(self):
        contract = valid_contract()
        contract["mode"] = "LONG_FORM_DEEP_DIVE"
        with self.assertRaisesRegex(ContractError, "invalid contract mode"):
            validate_contract(contract)

        # Modified threshold (lowered)
        contract = valid_contract()
        contract["lesson_depth_contract"]["min_total_words"] = 100
        with self.assertRaisesRegex(ContractError, "must exactly match canonical default"):
            validate_contract(contract)

        # Modified threshold (raised)
        contract = valid_contract()
        contract["lesson_depth_contract"]["min_total_words"] = 99999
        with self.assertRaisesRegex(ContractError, "must exactly match canonical default"):
            validate_contract(contract)

        # Extra key
        contract = valid_contract()
        contract["lesson_depth_contract"]["extra_key"] = 123
        with self.assertRaisesRegex(ContractError, "keys mismatch"):
            validate_contract(contract)

        # Missing key
        contract = valid_contract()
        del contract["lesson_depth_contract"]["no_padding"]
        with self.assertRaisesRegex(ContractError, "keys mismatch"):
            validate_contract(contract)

        # Wrong type
        contract = valid_contract()
        contract["lesson_depth_contract"]["no_padding"] = 1
        with self.assertRaisesRegex(ContractError, "must exactly match canonical default"):
            validate_contract(contract)
    def test_results_fail_closed_for_fake_pass_missing_unknown_duplicate_and_warn(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _, required = validate_contract(valid_contract())
            passing = evidence_rows(root)
            validate_results(passing, required)
            fake = root / "fake.json"
            fake.write_text(json.dumps([{"gate": gate, "status": "PASS"} for gate in required]), encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "must have exactly"):
                load_results(fake)
            with self.assertRaisesRegex(ContractError, "missing required"):
                validate_results(passing[:-1], required)
            with self.assertRaisesRegex(ContractError, "unknown or non-required"):
                validate_results(passing + [{**passing[0], "gate": "made_up_gate"}], required)
            with self.assertRaisesRegex(ContractError, "duplicate result"):
                validate_results(passing + [passing[0]], required)
            warned = [dict(row) for row in passing]
            warned[0]["status"] = "WARN"
            with self.assertRaisesRegex(ContractError, "PASS with exit_code 0"):
                validate_results(warned, required)

    def test_cli_requires_real_hashed_evidence(self):
        script = Path(__file__).with_name("publish_gate.py")
        listed = subprocess.run([sys.executable, str(script), "--list-profiles"], capture_output=True, text=True)
        self.assertEqual(listed.returncode, 0, listed.stderr)
        self.assertEqual(json.loads(listed.stdout), {profile: list(gates) for profile, gates in PROFILE_GATES.items()})

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            brief = root / "brief.md"
            results = root / "results.json"
            brief.write_text(brief_with(valid_contract()), encoding="utf-8")
            results.write_text(json.dumps(evidence_rows(root)), encoding="utf-8")
            passed = subprocess.run([sys.executable, str(script), str(brief), "--results", str(results)], capture_output=True, text=True)
            self.assertEqual(passed.returncode, 0, passed.stderr)
            self.assertIn("PUBLISH READY", passed.stdout)

            rows = json.loads(results.read_text(encoding="utf-8"))
            Path(rows[0]["artifacts"][0]["path"]).write_text("tampered", encoding="utf-8")
            blocked = subprocess.run([sys.executable, str(script), str(brief), "--results", str(results)], capture_output=True, text=True)
            self.assertEqual(blocked.returncode, 1)
            self.assertIn("stale or modified artifacts", blocked.stderr)


if __name__ == "__main__":
    unittest.main()
