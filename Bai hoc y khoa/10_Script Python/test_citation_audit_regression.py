"""Regression tests for citation_audit: PMID canonical context extraction bug fix."""
import json
import shutil
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import citation_audit
from evidence_bundle import BundleError, load_bundle, seven_gate_check

ROOT = Path(__file__).resolve().parent / ".citation_audit_test_tmp"
NOW = datetime.now(timezone.utc)
NOW_TEXT = NOW.isoformat().replace("+00:00", "Z")


def base_record(pmid="12345678", title="Sample Title", abstract="Sample abstract text."):
    return {
        "exists": True,
        "year": 2023,
        "title": title,
        "abstract": abstract,
        "author": "Doe J",
        "journal": "Test Journal",
        "publication_types": ["journal article"],
        "identifiers": {"pmid": pmid, "doi": "10.1000/test"},
        "topics": ["testing"],
        "providers": ["europe_pmc_metadata", "openalex", "crossref_retraction_watch"],
        "raw_sha256": [],
        "metadata_checked_at": NOW_TEXT,
        "conflicts": [],
        "integrity": {
            "provider": "crossref_retraction_watch",
            "status": "clean",
            "checked_at": NOW_TEXT,
            "corrections": [],
        },
        "full_text": {"available": False, "reuse_suitable": False},
        "official_source": {"authority_verified": False, "document_type": "journal article"},
        "claim_quote": "",
    }


def make_minimal_bundle(name, records):
    """Create a minimal valid evidence bundle on disk."""
    root = ROOT / name
    cache = root / "cache"
    raw_dir = cache / "raw" / "fixture"
    raw_dir.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"fixture": name}, sort_keys=True).encode()
    import hashlib
    digest = hashlib.sha256(payload).hexdigest()
    raw = raw_dir / f"{digest}.json"
    raw.write_bytes(payload)
    for record in records.values():
        record["raw_sha256"] = [digest]
        record["metadata_checked_at"] = NOW_TEXT
        record["integrity"]["checked_at"] = NOW_TEXT
    data = {
        "schema_version": "1.0",
        "created_at": NOW_TEXT,
        "records": records,
        "raw_objects": [
            {
                "provider": "fixture",
                "retrieved_at": NOW_TEXT,
                "sha256": digest,
                "path": str(raw.relative_to(cache)),
                "media_type": "application/json",
                "license": "fixture",
            }
        ],
        "providers": {"fixture": {"name": "fixture", "version": "1.0"}},
    }
    from evidence_bundle import content_hash
    data["cache_root"] = str(cache)
    data["content_hash"] = content_hash(data)
    bundle = root / "bundle.json"
    bundle.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return bundle, raw


class CitationAuditRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        shutil.rmtree(ROOT, ignore_errors=True)
        ROOT.mkdir(parents=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(ROOT, ignore_errors=True)

    def test_pmid_canonical_does_not_crash_with_nameerror(self):
        """A PMID citation passing through audit_citation must not raise NameError
        due to undefined context_start/context_end."""
        record = base_record("12345678")
        bundle, _ = make_minimal_bundle("no_nameerror", {"pmid:12345678": record})

        auditor = citation_audit.CitationAuditor(
            evidence_bundle=str(bundle),
        )

        text = (
            "This is a sample medical text discussing various topics. "
            + "The study by Doe et al. provides evidence for treatment efficacy "
            + "PMID: 12345678 demonstrates that the intervention is effective. "
            + "Further research is needed to confirm these findings in larger populations."
        )
        # Find the actual span of PMID: 12345678 in text
        import re
        m = re.search(r'PMID[:\s]*(\d{6,9})', text, re.IGNORECASE)
        self.assertIsNotNone(m, "Test text must contain a PMID")

        citation = {
            'type': 'pmid',
            'value': m.group(1),
            'span': m.span(),
            'raw': m.group(0),
        }

        # This must NOT raise NameError
        entry = auditor.audit_citation(citation, text)

        self.assertIsNotNone(entry)
        self.assertEqual(entry['citation'], citation['raw'])
        self.assertEqual(entry['type'], 'pmid')
        # Should have gone through the PMID path without NameError
        # Verdict depends on journal/gate resolution — any outcome is fine
        self.assertIsNotNone(entry.get('verdict'), 'entry must have a verdict')
        self.assertIn(entry['severity'], ['pass', 'warn', 'block'],
                      'severity must be one of pass/warn/block')
        self.assertIn('details', entry, 'entry must have details')
        self.assertIn('pmid_info', entry['details'], 'details must contain pmid_info')

    def test_pmid_canonical_passes_correct_claim_context_to_gate(self):
        """The claim context extracted around the citation must be the text
        surrounding the PMID occurrence, deterministically derived from the span."""
        record = base_record("99999999",
                            title="Treatment efficacy in heart failure",
                            abstract="This study examined treatment efficacy in heart failure patients with reduced ejection fraction and found significant improvements.")
        bundle, _ = make_minimal_bundle("claim_context", {"pmid:99999999": record})

        auditor = citation_audit.CitationAuditor(
            evidence_bundle=str(bundle),
        )

        # Place the PMID at a known position with distinctive surrounding text
        prefix = "Before text. " * 10
        suffix = " After text." * 10
        text = prefix + "PMID: 99999999 " + suffix

        import re
        m = re.search(r'PMID[:\s]*(\d{6,9})', text, re.IGNORECASE)
        citation = {
            'type': 'pmid',
            'value': m.group(1),
            'span': m.span(),
            'raw': m.group(0),
        }

        # Patch seven_gate_check to capture the claim argument
        original_sgc = seven_gate_check
        captured_claims = []

        def capturing_sgc(record, *, claim="", **kwargs):
            captured_claims.append(claim)
            return {
                "existence": {"status": "PASS", "reason": "exists"},
                "exact_identity": {"status": "PASS", "reason": "ok"},
                "topic_relevance": {"status": "PASS", "reason": "relevant"},
                "claim_abstract": {"status": "PASS", "reason": "match"},
                "numeric_full_text": {"status": "PASS", "reason": "not numeric"},
                "guideline_authority": {"status": "PASS", "reason": "not guideline"},
                "integrity_freshness": {"status": "PASS", "reason": "ok"},
            }

        with patch("citation_audit.seven_gate_check", side_effect=capturing_sgc):
            entry = auditor.audit_citation(citation, text)

        self.assertEqual(len(captured_claims), 1, "seven_gate_check should be called exactly once for PMID")
        claim = captured_claims[0]

        # The claim must be a substring of the original text
        self.assertIn(claim, text,
                      "claim context must be a substring of the original text")

        # The claim must contain the PMID marker itself
        self.assertIn("PMID: 99999999", claim,
                      "claim must contain the PMID itself")

        # Verify context window is correct: window=300 on each side
        # The window should extend 300 chars before and after the span
        expected_start = max(0, citation['span'][0] - 300)
        expected_end = min(len(text), citation['span'][1] + 300)
        expected_claim = text[expected_start:expected_end]
        self.assertEqual(claim, expected_claim,
                         f"claim should be text[{expected_start}:{expected_end}]")

        # Verify entry was processed without crash
        self.assertEqual(entry['type'], 'pmid')
        self.assertIn('verdict', entry)


if __name__ == "__main__":
    unittest.main()
