import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import urllib.error
import preflight_check_pmids

from preflight_check_pmids import extract_pmids


class PreflightCheckPmidsTest(unittest.TestCase):
    def test_labeled_pmids_are_extracted(self):
        self.assertEqual(extract_pmids("| PMID: 30936153 | Source |"), ["30936153"])

    def test_strict_mode_blocks_unlabeled_bare_pmid(self):
        script = Path(__file__).with_name("preflight_check_pmids.py")
        with tempfile.TemporaryDirectory() as directory:
            brief = Path(directory) / "brief.md"
            brief.write_text("No PMIDs here\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(script), str(brief), "--strict"],
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Strict preflight requires at least one PMID", result.stderr)
    def test_rate_limit_uses_only_verified_local_cache(self):
        rate_limited = urllib.error.HTTPError("https://example.test", 429, "rate limited", {}, None)
        with patch("urllib.request.urlopen", side_effect=rate_limited):
            self.assertEqual(preflight_check_pmids.check_pmid("39124738")["status"], "OK")
            blocked = preflight_check_pmids.check_pmid("99999999")
        self.assertEqual(blocked["status"], "BLOCK")
        self.assertEqual(blocked["reason"], "HTTP 429")

        unavailable = urllib.error.HTTPError("https://example.test", 503, "unavailable", {}, None)
        with patch("urllib.request.urlopen", side_effect=unavailable):
            self.assertEqual(preflight_check_pmids.check_pmid("39124738")["status"], "OK")
            missing_cache = preflight_check_pmids.check_pmid("99999999")
        self.assertEqual(missing_cache["status"], "BLOCK")
        self.assertEqual(missing_cache["reason"], "HTTP 503")

    def test_not_found_does_not_use_local_cache(self):
        not_found = urllib.error.HTTPError("https://example.test", 404, "not found", {}, None)
        with patch("urllib.request.urlopen", side_effect=not_found):
            blocked = preflight_check_pmids.check_pmid("39124738")
        self.assertEqual(blocked["status"], "BLOCK")
        self.assertEqual(blocked["reason"], "HTTP 404")

    def test_network_error_does_not_use_local_cache(self):
        network_error = urllib.error.URLError("network unavailable")
        with patch("urllib.request.urlopen", side_effect=network_error):
            blocked = preflight_check_pmids.check_pmid("39124738")
        self.assertEqual(blocked["status"], "BLOCK")
        self.assertIn("network unavailable", blocked["reason"])


if __name__ == "__main__":
    unittest.main()
