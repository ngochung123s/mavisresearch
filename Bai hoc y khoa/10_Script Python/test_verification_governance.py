import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from publish_gate import ContractError, PROFILE_GATES, load_results, validate_results
from verification_core import extract_brief_claims, extract_lesson_claims, sha256_file
from verify_claim_vs_abstract import build_report as build_brief_report, verify_occurrence as verify_brief_occurrence
from verify_guidelines import validate_evidence


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

    def test_zero_claim_is_a_hard_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "brief.md"
            path.write_text("## 2. Claims đã verify\n\nKhông có bảng claim.\n", encoding="utf-8")
            report, code = build_brief_report(path, 0.3)
        self.assertEqual(code, 2)
        self.assertEqual(report["parsed_claim_count"], 0)
        self.assertEqual(report["status"], "FAIL")

    def test_numeric_claim_must_match_quote_and_abstract(self):
        claim = extract_brief_claims(brief_claims(
            "| C-001 | Live birth tăng 20% | 12345678 | [DATA VERIFIED] | Live birth increased 20% | adults | A vs B | live birth | 12 weeks |"
        ))[0]
        status, failures = verify_brief_occurrence(claim, "Live birth increased 20% in adults after 12 weeks.", 0.1)
        self.assertEqual(status, "PASS", failures)
        status, failures = verify_brief_occurrence(claim, "Live birth increased 10% in adults after 12 weeks.", 0.1)
        self.assertEqual(status, "BLOCK")
        self.assertTrue(any("absent from abstract" in failure for failure in failures))

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
        self.assertIn("No PMIDs found", result.stdout)

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
            local = root / "guideline.pdf"
            local.write_bytes(b"official guideline")
            evidence = root / "guideline.json"
            row = {
                "claim_id": "C-G1", "society": "ESHRE", "title": "Official guideline",
                "document_id": "ESHRE-OS-2025", "version": "2025",
                "publication_date": "2025-01-01", "accessed_at": "2026-07-28",
                "canonical_url": "https://www.eshre.eu/guideline", "local_copy": str(local),
                "sha256": sha256_file(local), "recommendation_text": "Recommendation text",
                "superseded_by": None,
            }
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("PASS", 0))
            row["superseded_by"] = "ESHRE-OS-2026"
            evidence.write_text(json.dumps({"guidelines": [row]}), encoding="utf-8")
            report, code = validate_evidence(evidence)
            self.assertEqual((report["status"], code), ("FAIL", 2))

    def test_retraction_strict_zero_pmid_and_expression_of_concern(self):
        script = Path(__file__).with_name("retraction_check.py")
        with tempfile.TemporaryDirectory() as directory:
            lesson = Path(directory) / "lesson.md"
            lesson.write_text("Không có citation.", encoding="utf-8")
            empty = subprocess.run([sys.executable, str(script), "--md", str(lesson), "--strict"], capture_output=True, text=True)
            self.assertEqual(empty.returncode, 2)

        import retraction_check
        xml = b"""<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>12345678</PMID><Article><ArticleTitle>Study</ArticleTitle><Journal><Title>Journal</Title><JournalIssue><PubDate><Year>2024</Year></PubDate></JournalIssue></Journal><PublicationTypeList><PublicationType>Expression of Concern</PublicationType></PublicationTypeList></Article></MedlineCitation></PubmedArticle></PubmedArticleSet>"""
        response = unittest.mock.MagicMock()
        response.__enter__.return_value.read.return_value = xml
        with patch("urllib.request.urlopen", return_value=response):
            result = retraction_check.check_pmids(["12345678"])
        self.assertTrue(result["12345678"]["retracted"])
        self.assertEqual(result["12345678"]["reason"], "Expression of Concern")


if __name__ == "__main__":
    unittest.main()
