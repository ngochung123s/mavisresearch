#!/usr/bin/env python3
"""Verify every locked brief claim occurrence against its declared evidence."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

from verification_core import (
    Claim,
    extract_brief_claims,
    extract_claim_numbers,
    extract_numbers,
    has_numeric_data,
    validate_tag_policy,
)
NCBIBASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def fetch_abstract(pmid: str) -> str:
    url = f"{NCBIBASE}/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract&retmode=text"
    with urllib.request.urlopen(url, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def keyword_ratio(claim: str, evidence: str) -> float:
    words = re.findall(r"[A-Za-z0-9À-ỹ]{4,}", claim.casefold())
    meaningful = set(words)
    if not meaningful:
        return 1.0
    evidence_folded = evidence.casefold()
    return sum(word in evidence_folded for word in meaningful) / len(meaningful)


def verify_occurrence(claim: Claim, abstract: str, min_match: float) -> tuple[str, list[str]]:
    if claim.verification in {"FULL TEXT VERIFIED", "GUIDELINE VERIFIED"}:
        return "PASS", []

    failures = validate_tag_policy(claim, "abstract")
    if not abstract.strip():
        failures.append("empty abstract")
        return "BLOCK", failures
    if not claim.quote or claim.quote in {"—", "-"}:
        ratio = keyword_ratio(claim.claim_text, abstract)
        if ratio < min_match:
            failures.append(f"weak claim/evidence keyword overlap: {ratio:.2f} < {min_match:.2f}")

    if has_numeric_data(claim.claim_text):
        if not claim.quote or claim.quote in {"—", "-"}:
            failures.append("numeric claim has no exact source quote")
        claim_numbers = extract_claim_numbers(claim.claim_text)
        quote_numbers = extract_numbers(claim.quote)
        abstract_numbers = extract_numbers(abstract)
        missing_quote = [number for number in claim_numbers if number not in quote_numbers]
        missing_abstract = [number for number in claim_numbers if number not in abstract_numbers]
        if missing_quote:
            failures.append(f"claim numbers absent from quote: {missing_quote}")
        if missing_abstract:
            failures.append(f"claim numbers absent from abstract: {missing_abstract}")
        if claim.quote and claim.quote.casefold() not in abstract.casefold():
            failures.append("source quote is not an exact abstract substring")

    return ("BLOCK" if failures else "PASS"), failures


def build_report(brief: Path, min_match: float) -> tuple[dict, int]:
    text = brief.read_text(encoding="utf-8")
    claims = extract_brief_claims(text)
    if not claims:
        return {
            "document": str(brief.resolve()),
            "parsed_claim_count": 0,
            "verified_claim_count": 0,
            "status": "FAIL",
            "reason": "No claim rows parsed from the locked claims section",
            "claims": [],
        }, 2

    cache: dict[str, str] = {}
    rows = []
    for claim in claims:
        if claim.source_id not in cache:
            time.sleep(0.15)
            try:
                cache[claim.source_id] = fetch_abstract(claim.source_id)
            except Exception as exc:
                cache[claim.source_id] = ""
                rows.append({**claim.to_dict(), "status": "BLOCK", "failures": [f"fetch error: {exc}"]})
                continue
        status, failures = verify_occurrence(claim, cache[claim.source_id], min_match)
        rows.append({**claim.to_dict(), "status": status, "failures": failures})

    blocked = sum(row["status"] != "PASS" for row in rows)
    report = {
        "document": str(brief.resolve()),
        "parsed_claim_count": len(claims),
        "verified_claim_count": len(claims) - blocked,
        "status": "PASS" if blocked == 0 else "FAIL",
        "claims": rows,
    }
    return report, 0 if blocked == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path, help="Path to locked RESEARCH_BRIEF.md")
    parser.add_argument("--min-match", type=float, default=0.30)
    parser.add_argument("--json-out", type=Path, help="Write the complete evidence report")
    args = parser.parse_args()
    if not args.brief.is_file():
        parser.error(f"file not found: {args.brief}")

    report, exit_code = build_report(args.brief, args.min_match)
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload, encoding="utf-8")
    print(payload)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
