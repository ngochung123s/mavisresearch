"""Strict provider-neutral PMID preflight; consumes an immutable evidence bundle offline."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from evidence_bundle import BundleError, document_checks, extract_pmids, load_bundle

PMID_LABELED = re.compile(r"PMID[: ]*\**(\d{7,8})\**", re.I)
PMID_TABLE = re.compile(r"\|\s*(?:[A-Za-z0-9_-]+\s*\|\s*.*?\s*\|\s*)?(\d{7,8})\s*\|")

def extract_pmids_from_text(text: str) -> list[str]:
    return list(dict.fromkeys(PMID_LABELED.findall(text) + PMID_TABLE.findall(text)))

# Public legacy name denotes parsing only, not a compatibility network shim.
extract_pmids = extract_pmids_from_text

def check_pmid(pmid: str, evidence_bundle: Path) -> dict:
    try:
        bundle = load_bundle(evidence_bundle)
    except BundleError as exc:
        return {"pmid": pmid, "status": "BLOCK", "reason": str(exc)}
    record = bundle.record_for_pmid(pmid)
    if not record or record.get("exists") is not True:
        return {"pmid": pmid, "status": "BLOCK", "reason": "no exact provider record"}
    if record.get("conflicts"):
        return {"pmid": pmid, "status": "BLOCK", "reason": "; ".join(record["conflicts"])}
    return {"pmid": pmid, "status": "OK", "title": record.get("title", ""), "year": record.get("year", ""), "source": ",".join(record.get("providers", []))}

def main() -> int:
    parser = argparse.ArgumentParser(description="Strict offline evidence-bundle PMID preflight")
    parser.add_argument("plan_file", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--topic")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.plan_file.is_file():
        parser.error(f"file not found: {args.plan_file}")
    text = args.plan_file.read_text(encoding="utf-8")
    pmids = extract_pmids_from_text(text)
    if not pmids:
        report = {"status": "FAIL", "summary": {"ok": 0, "block": 1}, "error": "Strict preflight requires at least one PMID", "results": []}
        print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else report["error"], file=sys.stderr)
        return 2
    try:
        bundle = load_bundle(args.evidence_bundle)
        rows = document_checks(text, bundle, topic=args.topic)
        results = [{"pmid": row["pmid"], "status": "OK" if row["status"] == "PASS" else "BLOCK", "gates": row["gates"]} for row in rows]
    except BundleError as exc:
        results = [{"pmid": pmid, "status": "BLOCK", "reason": str(exc)} for pmid in pmids]
    block = sum(row["status"] != "OK" for row in results)
    report = {"status": "PASS" if not block else "FAIL", "summary": {"ok": len(results)-block, "block": block}, "results": results}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not block else 2

if __name__ == "__main__":
    raise SystemExit(main())
