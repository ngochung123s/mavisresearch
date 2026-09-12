import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from publish_gate import ContractError, PROFILE_GATES, load_results, validate_results
from verification_core import extract_brief_claims, extract_lesson_claims, sha256_file
from verify_guidelines import REGISTRY_PATH, is_official_host, validate_evidence


def brief_claims(rows: str) -> str:
    return f"""## 2. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
{rows}

## 3. End
"""


class VerificationGovernanceTest(unittest.TestCase):
    def test_current_brief_schema_parses_each_claim_occurrence(self):
        text = brief_claims(
            "| C-001 | Outcome giảm 20% | 12345678 | [DATA VERIFIED] | Outcome decreased 20% | adults | A vs B | outcome | 12 weeks |\n"
            "| C-002 | Adverse events tăng 5% | 12345678 | [DATA VERIFIED] | Adverse events increased 5% | adults | A vs B | adverse events | 12 weeks |"
        )
        claims = extract_brief_claims(text)
        self.assertEqual([claim.claim_id for claim in claims], ["C-001", "C-002"])
        self.assertEqual([claim.source_id for claim in claims], ["12345678", "12345678"])



    def test_lesson_parser_keeps_same_pmid_occurrences(self):
        text = (
            "Claim A được hỗ trợ. PMID: 12345678 [ABSTRACT VERIFIED]\n\n"
            "Claim B khác cũng dùng nguồn này. PMID: 12345678 [ABSTRACT VERIFIED]"
        )
        claims = extract_lesson_claims(text)
        self.assertEqual(len(claims), 2)
        self.assertNotEqual(claims[0].claim_id, claims[1].claim_id)

    def test_strict_zero_pmid_exits_two(self):
        script = Path(__file__).with_name("verify_all_pmids.py")
        with tempfile.TemporaryDirectory() as directory:
            lesson = Path(directory) / "lesson.md"
            lesson.write_text("Không có PMID.", encoding="utf-8")
            result = subprocess.run([sys.executable, str(script), str(lesson), "--strict"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("--evidence-bundle", result.stderr)

    def test_handwritten_pass_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.json"
            path.write_text(json.dumps([{"gate": gate, "status": "PASS"} for gate in PROFILE_GATES["disease"]]), encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "must have exactly"):
                load_results(path)

    def test_hashed_manifest_detects_modified_input_and_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "lesson.md"
            artifact = root / "gate.json"
            source.write_text("v1", encoding="utf-8")
            artifact.write_text("ok", encoding="utf-8")
            required = ("one",)
            result = [{
                "gate": "one", "status": "PASS", "command": ["python", "gate.py"],
                "exit_code": 0, "release_id": "release-v1",
                "inputs": [{"path": str(source), "sha256": sha256_file(source)}],
                "artifacts": [{"path": str(artifact), "sha256": sha256_file(artifact)}],
            }]
            validate_results(result, required)
            source.write_text("v2", encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "stale or modified inputs"):
                validate_results(result, required)

    def test_guideline_web_evidence_and_supersession(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("official guideline", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "official guideline",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("PASS", 0))
            row["superseded_by"] = "ESHRE-OS-2026"
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))

    def test_fabricated_quote_with_matching_hash_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Actual official statement text without fabricated quote.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Fabricated recommendation quote",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))
            self.assertTrue(any("quote not found" in f for f in report["guidelines"][0]["failures"]))

    def test_ellipsis_quote_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Low-frequency cutoff is 0.05 Hz and high-frequency cutoff is 150 Hz.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Low-frequency cutoff... high-frequency cutoff",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))
            self.assertTrue(any("ellipsis" in f for f in report["guidelines"][0]["failures"]))

    def test_exact_normalized_quote_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Low-frequency cutoff is 0.05 Hz.\nHigh-frequency cutoff is 150 Hz.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Low-frequency cutoff is 0.05 Hz. High-frequency cutoff is 150 Hz.",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("PASS", 0))

    def test_reference_citation_not_counted_as_claim(self):
        text = """# Lesson Title
Section 1 text. {claim:C-001} PMID: 12345678 [GUIDELINE VERIFIED]

## Tài liệu tham khảo
1. Author et al. Paper title. J Med 2024. [PMID: 12345678] [GUIDELINE VERIFIED]
"""
        claims = extract_lesson_claims(text)
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0].claim_id, "C-001")
        self.assertEqual(claims[0].line, 2)

    def test_unit_number_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Standard speed is 50 mm/s and cutoff is 0.1 Hz.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Standard speed is 50 mm/s and cutoff is 0.1 Hz.",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            # Verify exact quote match in file
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("PASS", 0))

            # Now test numeric mismatch when text numbers don't match claim numbers
            row["recommendation_text"] = "Standard speed is 25 mm/s and cutoff is 0.05 Hz."
            local.write_text("Standard speed is 50 mm/s and cutoff is 0.1 Hz.", encoding="utf-8")
            row["sha256"] = sha256_file(local)
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))
            self.assertTrue(any("numbers absent from local source" in f for f in report["guidelines"][0]["failures"]))
    def test_unverified_locator_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Standard speed is 25 mm/s.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Standard speed is 25 mm/s.",
                "locator": "UNVERIFIED_FULLTEXT_PAYWALLED", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))
            self.assertTrue(any("locator is unverified" in f for f in report["guidelines"][0]["failures"]))

    def test_bsg_canonical_hosts_pass_and_lookalikes_fail(self):
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

        self.assertEqual(
            is_official_host("BSG", "https://gut.bmj.com/content/67/1/6", registry),
            (True, ""),
        )
        self.assertEqual(
            is_official_host(
                "British Society of Gastroenterology",
                "https://www.bsg.org.uk/clinical-resource",
                registry,
            ),
            (True, ""),
        )
        for url in (
            "https://gut.bmj.com.evil.example/content/67/1/6",
            "https://bsg-guidelines.example.org/abnormal-liver-tests",
        ):
            valid, error = is_official_host("BSG", url, registry)
            self.assertFalse(valid)
            self.assertIn("not registered or known official host", error)

    def test_unregistered_society_or_host_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "guideline.txt"
            local.write_text("Standard speed is 25 mm/s.", encoding="utf-8")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "UnregisteredSociety", "title": "Official guideline",
                "document_id": "UNREG-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://unregistered.com/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Standard speed is 25 mm/s.",
                "locator": "Section 1", "pmid": None, "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))
            self.assertTrue(any("is not registered" in f for f in report["guidelines"][0]["failures"]))


if __name__ == "__main__":
    unittest.main()
