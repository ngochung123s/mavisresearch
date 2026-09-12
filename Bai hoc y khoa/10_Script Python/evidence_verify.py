"""Shared provider-neutral offline release verifier implementation."""
from __future__ import annotations
import json
from pathlib import Path
from evidence_bundle import BundleError, document_checks, extract_pmids, load_bundle, seven_gate_check
from verification_core import extract_brief_claims, extract_lesson_claims, validate_tag_policy


def identity_report(path: Path, bundle_path: Path, topic: str | None = None) -> tuple[dict, int]:
    try:
        bundle = load_bundle(bundle_path)
    except BundleError as exc:
        return {"status": "FAIL", "error": str(exc), "checks": []}, 2
    text = path.read_text(encoding="utf-8")
    pmids = extract_pmids(text)
    if not pmids:
        return {"status": "FAIL", "error": "No PMIDs found", "checks": []}, 2
    rows = document_checks(text, bundle, topic=topic)
    blocked = sum(row["status"] != "PASS" for row in rows)
    return {"status": "PASS" if not blocked else "FAIL", "checked": len(rows), "checks": rows, "bundle_hash": bundle.data["content_hash"]}, 0 if not blocked else 2


def claim_report(path: Path, bundle_path: Path, *, brief: bool = False, topic: str | None = None) -> tuple[dict, int]:
    try:
        bundle = load_bundle(bundle_path)
    except BundleError as exc:
        return {"status": "FAIL", "error": str(exc), "checks": []}, 2
    text = path.read_text(encoding="utf-8")
    claims = extract_brief_claims(text) if brief else extract_lesson_claims(text)
    if not claims:
        return {"document": str(path.resolve()), "parsed_claim_count": 0, "status": "FAIL", "reason": "No claim rows parsed" if brief else "No PMID claim occurrences parsed", "checks": []}, 2
    rows = []
    for claim in claims:
        record = bundle.record_for_pmid(claim.source_id)
        gates = seven_gate_check(record, claim=claim.claim_text, topic=topic, verification=claim.verification)
        source_kind = "guideline" if claim.verification == "GUIDELINE VERIFIED" else "full_text" if claim.verification == "FULL TEXT VERIFIED" else "abstract"
        failures = validate_tag_policy(claim, source_kind)
        failures.extend(f"{name}: {gate['reason']}" for name, gate in gates.items() if gate["status"] != "PASS")
        rows.append({**claim.to_dict(), "status": "BLOCK" if failures else "PASS", "failures": failures, "gates": gates})
    blocked = sum(row["status"] != "PASS" for row in rows)
    key = "claims" if brief else "checks"
    return {"document": str(path.resolve()), "parsed_claim_count": len(claims), "verified_claim_count": len(claims)-blocked, "status": "PASS" if not blocked else "FAIL", key: rows, "bundle_hash": bundle.data["content_hash"]}, 0 if not blocked else 2


def retraction_report(path: Path, bundle_path: Path) -> tuple[dict, int]:
    try:
        bundle = load_bundle(bundle_path)
    except BundleError as exc:
        return {"status": "FAIL", "error": str(exc), "results": {}}, 2
    pmids = extract_pmids(path.read_text(encoding="utf-8"))
    if not pmids:
        return {"status": "FAIL", "checked": 0, "error": "No PMIDs found", "results": {}}, 2
    results, blocked = {}, False
    for pmid in pmids:
        record = bundle.record_for_pmid(pmid)
        gate = seven_gate_check(record, claim=record.get("title", "") if record else "")["integrity_freshness"]
        results[pmid] = {"status": gate["status"], "reason": gate["reason"], "integrity": (record or {}).get("integrity")}
        blocked |= gate["status"] != "PASS"
    return {"status": "FAIL" if blocked else "PASS", "checked": len(results), "results": results, "bundle_hash": bundle.data["content_hash"]}, 2 if blocked else 0


def write_report(report: dict, output: Path | None) -> None:
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    print(payload)
