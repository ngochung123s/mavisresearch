import subprocess
import sys
import unittest
from pathlib import Path

from preflight_check_pmids import extract_pmids

class PreflightCheckPmidsTest(unittest.TestCase):
    def test_labeled_pmids_are_extracted(self):
        self.assertEqual(extract_pmids("| PMID: 30936153 | Source |"), ["30936153"])

    def test_evidence_bundle_is_mandatory(self):
        script = Path(__file__).with_name("preflight_check_pmids.py")
        fixture = Path(__file__).with_name("test_preflight_fixture.md")
        fixture.write_text("PMID: 30936153", encoding="utf-8")
        try:
            result = subprocess.run([sys.executable, str(script), str(fixture), "--strict"], capture_output=True, text=True)
        finally:
            fixture.unlink(missing_ok=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("--evidence-bundle", result.stderr)

    def test_no_unlabeled_pmid_is_hard_failure_after_bundle_argument(self):
        script = Path(__file__).with_name("preflight_check_pmids.py")
        fixture = Path(__file__).with_name("test_preflight_fixture.md")
        fixture.write_text("No PMIDs here", encoding="utf-8")
        try:
            result = subprocess.run([sys.executable, str(script), str(fixture), "--strict", "--evidence-bundle", str(fixture)], capture_output=True, text=True)
        finally:
            fixture.unlink(missing_ok=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Strict preflight requires at least one PMID", result.stderr)

if __name__ == "__main__": unittest.main()
