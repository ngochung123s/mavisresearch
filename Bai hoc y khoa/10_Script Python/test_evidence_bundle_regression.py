import hashlib
import json
import shutil
import socket
import subprocess
import sys
import unittest
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import build_pipeline
import evidence_sync
from evidence_bundle import BundleError, content_hash, document_checks, load_bundle, seven_gate_check

ROOT = Path(__file__).resolve().parent / ".evidence_test_tmp"
NOW = datetime.now(timezone.utc)
NOW_TEXT = NOW.isoformat().replace("+00:00", "Z")


def base_record(pmid="12345678", title="Venous blood sampling guideline", abstract="Venous blood sampling guideline reduces preanalytical errors in patients."):
    return {
        "exists": True,
        "identifiers": {"pmid": pmid, "doi": "10.1000/exact"},
        "title": title,
        "abstract": abstract,
        "journal": "Clinical Chemistry and Laboratory Medicine",
        "year": "2024",
        "publication_types": ["Journal Article"],
        "topics": ["venous blood sampling", "preanalytical errors"],
        "providers": ["europe_pmc_metadata", "openalex", "crossref_retraction_watch"],
        "metadata_checked_at": NOW_TEXT,
        "full_text": {"available": False, "license": None, "reuse_suitable": False},
        "integrity": {"status": "clean", "checked_at": NOW_TEXT, "corrections": [], "provider": "crossref_retraction_watch"},
        "conflicts": [],
    }


def make_bundle(name, records, *, stale=False):
    root = ROOT / name
    cache = root / "cache"
    raw_dir = cache / "raw" / "fixture"
    raw_dir.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"fixture": name}, sort_keys=True).encode()
    digest = hashlib.sha256(payload).hexdigest()
    raw = raw_dir / f"{digest}.json"
    raw.write_bytes(payload)
    checked = (NOW - timedelta(hours=80)).isoformat() if stale else NOW_TEXT
    for record in records.values():
        record["raw_sha256"] = [digest]
        record["metadata_checked_at"] = checked
    data = {
        "schema_version": "1.0", "created_at": NOW_TEXT, "providers": ["fixture"],
        "cache_root": str(cache.resolve()), "records": records,
        "raw_objects": [{"provider": "fixture", "retrieved_at": NOW_TEXT, "sha256": digest, "path": f"raw/fixture/{digest}.json", "media_type": "application/json", "license": "metadata-only"}],
        "content_hash": "",
    }
    data["content_hash"] = content_hash(data)
    bundle = root / "bundle.json"
    bundle.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return bundle, raw


def sync_official_bundle(name, official_row, *, provider_conflict=False):
    root = ROOT / name
    cache = root / "cache"
    source = root / "official.pdf"
    source.parent.mkdir(parents=True, exist_ok=True)
    official_payload = f"official fixture: {name}".encode()
    source.write_bytes(official_payload)
    manifest_row = dict(official_row, local_copy=source.name, media_type="application/pdf")
    manifest = root / "official_sources.json"
    manifest.write_text(json.dumps([manifest_row], ensure_ascii=False), encoding="utf-8")
    output = root / "bundle.json"

    def raw(provider, payload):
        return evidence_sync.store_raw(cache, provider, json.dumps(payload, sort_keys=True).encode(), "application/json", NOW_TEXT)

    def epmc_metadata(_root, pmid, _retrieved_at):
        row = {
            "pmid": pmid, "title": official_row["title"], "abstractText": official_row.get("summary", ""),
            "doi": official_row.get("doi"), "pubYear": "2024", "pubTypeList": {"pubType": ["Journal Article"]},
        }
        return row, raw("europe_pmc_metadata", row)

    def openalex(_root, pmid, _retrieved_at):
        doi = "10.1000/conflict" if provider_conflict else official_row.get("doi")
        row = {"id": "https://openalex.org/W1", "ids": {"pmid": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"}, "doi": f"https://doi.org/{doi}" if doi else None, "title": official_row["title"]}
        return row, raw("openalex", row)

    def crossref(_root, doi, _retrieved_at):
        row = {"DOI": doi, "title": [official_row["title"]]}
        return row, raw("crossref_retraction_watch", row)

    with patch.object(evidence_sync, "utcnow", return_value=NOW_TEXT), \
         patch.object(evidence_sync, "epmc_metadata", side_effect=epmc_metadata) as mocked_epmc, \
         patch.object(evidence_sync, "openalex", side_effect=openalex), \
         patch.object(evidence_sync, "crossref", side_effect=crossref), \
         patch.object(evidence_sync, "oa_full_text", return_value=({"available": False, "license": None, "reuse_suitable": False}, [])):
        data = evidence_sync.sync([], output, cache, manifest)
    return output, data, official_payload, mocked_epmc.call_count


class EvidenceBundleRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        shutil.rmtree(ROOT, ignore_errors=True)
        ROOT.mkdir(parents=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(ROOT, ignore_errors=True)

    def test_01_29910186_wrong_topic_blocks(self):
        record = base_record("29910186", "Structural Basis of Phosphatidic Acid Sensing by APH in Apicomplexan Parasites", "APH senses phosphatidic acid in Apicomplexan parasites.")
        record["topics"] = ["Apicomplexa", "phosphatidic acid"]
        bundle, _ = make_bundle("wrong_topic", {"pmid:29910186": record})
        rows = document_checks("EFLM venous blood sampling PMID: 29910186 [ABSTRACT VERIFIED]", load_bundle(bundle), topic="venous blood sampling")
        self.assertEqual(rows[0]["gates"]["topic_relevance"]["status"], "BLOCK")

    def test_02_27235445_non_oa_still_exists(self):
        record = base_record("27235445", "Cardiac study", "Cardiac study reports patient outcomes.")
        record["full_text"] = {"available": False, "license": None, "reuse_suitable": False}
        bundle, _ = make_bundle("non_oa_exists", {"pmid:27235445": record})
        self.assertTrue(load_bundle(bundle).record_for_pmid("27235445")["exists"])

    def test_03_valid_exact_match_passes(self):
        gates = seven_gate_check(base_record(), claim="Venous blood sampling reduces preanalytical errors", expected_doi="10.1000/exact", expected_title="Venous blood sampling guideline")
        self.assertTrue(all(g["status"] == "PASS" for g in gates.values()))

    def test_04_nonexistent_blocks(self):
        gates = seven_gate_check({"exists": False})
        self.assertTrue(all(g["status"] == "BLOCK" for g in gates.values()))

    def test_05_missing_abstract_blocks(self):
        record = base_record(); record["abstract"] = ""
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["claim_abstract"]["status"], "BLOCK")

    def test_06_title_mismatch_blocks(self):
        self.assertEqual(seven_gate_check(base_record(), claim="Venous blood sampling", expected_title="Cancer immunotherapy trial")["exact_identity"]["status"], "BLOCK")

    def test_07_pmid_doi_conflict_blocks(self):
        self.assertEqual(seven_gate_check(base_record(), claim="Venous blood sampling", expected_doi="10.9999/wrong")["exact_identity"]["status"], "BLOCK")

    def test_08_retracted_blocks(self):
        record = base_record(); record["integrity"]["status"] = "retracted"
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["integrity_freshness"]["status"], "BLOCK")

    def test_09_expression_of_concern_blocks(self):
        record = base_record(); record["integrity"]["status"] = "expression_of_concern"
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["integrity_freshness"]["status"], "BLOCK")

    def test_10_correction_affecting_claim_blocks(self):
        record = base_record(); record["integrity"]["corrections"] = [{"requires_adjudication": True, "adjudication": "affected"}]
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["integrity_freshness"]["status"], "BLOCK")

    def test_11_correction_non_affecting_claim_passes_after_adjudication(self):
        record = base_record(); record["integrity"]["corrections"] = [{"requires_adjudication": True, "adjudication": "unaffected"}]
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["integrity_freshness"]["status"], "PASS")

    def test_12_reinstatement_passes(self):
        record = base_record(); record["integrity"].update({"status": "clean", "reinstated": True})
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["integrity_freshness"]["status"], "PASS")

    def test_13_official_guideline_without_pmid_passes(self):
        record = base_record(); record["identifiers"] = {"official_id": "WHO-2025"}; record["publication_types"] = ["guideline"]
        record["official_source"] = {"authority_verified": True, "document_type": "guideline", "current_version": True}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "PASS")

    def test_14_educational_slide_mislabeled_guideline_blocks(self):
        record = base_record(); record["publication_types"] = ["educational resource"]
        record["official_source"] = {"authority_verified": True, "document_type": "educational"}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "BLOCK")

    def test_clinical_practice_guideline_document_type_passes_casefolded(self):
        record = base_record(); record["publication_types"] = ["Clinical Practice Guideline"]
        record["official_source"] = {"authority_verified": True, "document_type": "  CLINICAL   PRACTICE GUIDELINE  ", "current_version": True}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "PASS")

    def test_consensus_statement_document_type_passes(self):
        record = base_record(); record["publication_types"] = ["Consensus Statement"]
        record["official_source"] = {"authority_verified": True, "document_type": "Consensus Statement", "current_version": True}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "PASS")

    def test_arbitrary_official_document_is_not_a_guideline(self):
        record = base_record(); record["publication_types"] = ["Official Policy Brief"]
        record["official_source"] = {"authority_verified": True, "document_type": "Official Policy Brief", "current_version": True}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "BLOCK")

    def test_15_raw_hash_mismatch_blocks_bundle(self):
        bundle, raw = make_bundle("raw_mismatch", {"pmid:12345678": base_record()})
        raw.write_bytes(b"tampered")
        with self.assertRaisesRegex(BundleError, "raw hash mismatch"): load_bundle(bundle)

    def test_16_stale_retraction_or_metadata_blocks_bundle(self):
        bundle, _ = make_bundle("stale", {"pmid:12345678": base_record()}, stale=True)
        with self.assertRaisesRegex(BundleError, "stale metadata"): load_bundle(bundle)

    def test_17_http_429_fails_without_retry(self):
        err = urllib.error.HTTPError("https://example.test", 429, "rate", {}, None)
        with patch("urllib.request.urlopen", side_effect=err) as mocked:
            with self.assertRaisesRegex(evidence_sync.ProviderFailure, "HTTP 429"): evidence_sync.request("https://example.test")
        mocked.assert_called_once()

    def test_18_5xx_malformed_and_outage_fail_closed(self):
        for exc, message in [(urllib.error.HTTPError("https://x", 503, "down", {}, None), "HTTP 503"), (urllib.error.URLError("offline"), "provider outage")]:
            with patch("urllib.request.urlopen", side_effect=exc):
                with self.assertRaisesRegex(evidence_sync.ProviderFailure, message): evidence_sync.request("https://example.test")
        with patch.object(evidence_sync, "request", return_value=(b"not-json", "application/json")):
            with self.assertRaisesRegex(evidence_sync.ProviderFailure, "malformed"): evidence_sync.fetch_json(ROOT, "fixture", "https://example.test", NOW_TEXT)

    def test_19_non_oa_metadata_not_conflated_with_nonexistence(self):
        record = base_record(); record["full_text"] = {"available": False, "license": "all-rights-reserved", "reuse_suitable": False}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["existence"]["status"], "PASS")

    def test_20_unsuitable_fulltext_license_blocks_numeric(self):
        record = base_record(); record["full_text"] = {"available": True, "license": "all-rights-reserved", "reuse_suitable": False}; record["claim_quote"] = "10 mg"
        self.assertEqual(seven_gate_check(record, claim="Dose 10 mg", verification="FULL TEXT VERIFIED")["numeric_full_text"]["status"], "BLOCK")

    def test_21_provider_conflict_blocks_identity(self):
        record = base_record(); record["conflicts"] = ["Europe PMC/OpenAlex DOI conflict"]
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling")["exact_identity"]["status"], "BLOCK")

    def test_22_build_subprocess_egress_is_blocked(self):
        result = build_pipeline.run([sys.executable, "-c", "import socket; socket.create_connection(('example.com',80),1)"])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("offline build blocked network egress", result.stderr)

    def test_translation_non_endorsed_cannot_be_official_guideline(self):
        record = base_record(); record["publication_types"] = ["guideline"]
        record["official_source"] = {"authority_verified": True, "document_type": "guideline", "translation_of": "10.1515/cclm-2018-0602", "endorsement_status": "not_endorsed", "current_version": True}
        self.assertEqual(seven_gate_check(record, claim="Venous blood sampling", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "BLOCK")

    def test_superseded_kdigo_style_guideline_blocks(self):
        record = base_record(); record["publication_types"] = ["guideline"]
        record["official_source"] = {"authority_verified": True, "document_type": "guideline", "superseded_by": "KDIGO newer version", "current_version": False}
        self.assertEqual(seven_gate_check(record, claim="Acute kidney injury", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "BLOCK")

    def test_linked_official_pmid_is_one_enriched_corroborated_record(self):
        official = {
            "id": "WHO-PHLEBOTOMY-2010", "pmid": "23741774", "doi": None,
            "title": "WHO Guidelines on Drawing Blood: Best Practices in Phlebotomy",
            "summary": "This document provides guidance on the steps recommended for safe phlebotomy.",
            "document_type": "guideline", "authority_verified": True, "current_version": True,
        }
        bundle_path, data, official_payload, fetch_count = sync_official_bundle("linked_official", official)
        self.assertEqual(fetch_count, 1)
        self.assertEqual(list(data["records"]), ["pmid:23741774"])
        bundle = load_bundle(bundle_path)
        record = bundle.record_for_pmid("23741774")
        self.assertIs(record, bundle.record_for_official_id("WHO-PHLEBOTOMY-2010"))
        self.assertEqual(record["identifiers"]["official_id"], "WHO-PHLEBOTOMY-2010")
        self.assertEqual(set(record["providers"]), {"europe_pmc_metadata", "openalex", "official_source"})
        self.assertEqual(len(record["raw_sha256"]), 3)
        official_hash = hashlib.sha256(official_payload).hexdigest()
        self.assertIn(official_hash, record["raw_sha256"])
        official_raw = next(row for row in data["raw_objects"] if row["sha256"] == official_hash)
        self.assertEqual((official_raw["provider"], official_raw["media_type"]), ("official_source", "application/pdf"))

    def test_official_guideline_without_pmid_remains_official_record(self):
        official = {
            "id": "WHO-GUIDELINE-2025", "pmid": None, "doi": None,
            "title": "WHO Clinical Guideline", "summary": "Official clinical recommendations.",
            "document_type": "guideline", "authority_verified": True, "current_version": True,
        }
        bundle_path, data, _, fetch_count = sync_official_bundle("official_without_pmid", official)
        self.assertEqual(fetch_count, 0)
        self.assertEqual(list(data["records"]), ["official:WHO-GUIDELINE-2025"])
        self.assertIsNotNone(load_bundle(bundle_path).record_for_official_id("WHO-GUIDELINE-2025"))

    def test_official_sync_preserves_original_document_type_provenance(self):
        official = {
            "id": "WHO-CPG-2025", "pmid": None, "doi": None,
            "title": "WHO Clinical Practice Guideline", "summary": "Official clinical recommendations.",
            "document_type": "Clinical Practice Guideline", "authority_verified": True, "current_version": True,
        }
        bundle_path, _, _, _ = sync_official_bundle("official_cpg_provenance", official)
        record = load_bundle(bundle_path).record_for_official_id("WHO-CPG-2025")
        self.assertEqual(record["official_source"]["document_type"], "Clinical Practice Guideline")
        self.assertEqual(record["publication_types"], ["Clinical Practice Guideline"])
        self.assertEqual(seven_gate_check(record, claim="Official clinical recommendations", verification="GUIDELINE VERIFIED")["guideline_authority"]["status"], "PASS")

    def test_linked_official_provider_conflicts_remain_blocking(self):
        official = {
            "id": "WHO-CONFLICT", "pmid": "23741774", "doi": "10.1000/exact",
            "title": "WHO Guidelines on Drawing Blood: Best Practices in Phlebotomy",
            "summary": "This document provides guidance on the steps recommended for safe phlebotomy.",
            "document_type": "guideline", "authority_verified": True, "current_version": True,
        }
        bundle_path, data, _, _ = sync_official_bundle("linked_conflict", official, provider_conflict=True)
        self.assertEqual(list(data["records"]), ["pmid:23741774"])
        record = load_bundle(bundle_path).record_for_pmid("23741774")
        self.assertIn("Europe PMC/OpenAlex DOI conflict", record["conflicts"])
        self.assertEqual(seven_gate_check(record, claim="safe phlebotomy")["exact_identity"]["status"], "BLOCK")

if __name__ == "__main__": unittest.main()
