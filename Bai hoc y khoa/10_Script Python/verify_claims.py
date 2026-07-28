"""Verify every PMID claim occurrence in a lesson; never deduplicate by PMID."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from verification_core import (
    Claim,
    LEGACY_TAG_RE,
    extract_claim_numbers,
    extract_lesson_claims,
    extract_numbers,
    has_numeric_data,
    validate_tag_policy,
)
CACHE_DIR = Path(__file__).with_name("claim_cache")
CACHE_DIR.mkdir(exist_ok=True)
MIN_EVIDENCE_LENGTH = 100


def fetch_source(pmid: str, timeout: int = 20) -> dict:
    cache = CACHE_DIR / f"{pmid}.json"
    if cache.is_file() and time.time() - cache.stat().st_mtime < 86400:
        try:
            cached = json.loads(cache.read_text(encoding="utf-8"))
            if cached.get("status") == "ok":
                return cached
        except (OSError, json.JSONDecodeError):
            pass

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml&rettype=abstract"
    with urllib.request.urlopen(url, timeout=timeout) as response:
        root = ET.fromstring(response.read())
    article = next(root.iter("PubmedArticle"), None)
    if article is None:
        return {"pmid": pmid, "status": "not_found", "abstract": ""}
    abstract = "\n".join("".join(node.itertext()).strip() for node in article.findall(".//AbstractText"))
    title_node = article.find(".//ArticleTitle")
    result = {
        "pmid": pmid,
        "status": "ok",
        "title": "".join(title_node.itertext()).strip() if title_node is not None else "",
        "abstract": abstract,
        "journal": article.findtext(".//Journal/Title") or "",
        "year": article.findtext(".//PubDate/Year") or "",
    }
    cache.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def keyword_overlap(claim: str, source: str) -> int:
    claim_words = set(re.findall(r"[A-Za-zÀ-ỹ]{4,}", claim.casefold()))
    source_words = set(re.findall(r"[A-Za-zÀ-ỹ]{4,}", source.casefold()))
    return len(claim_words & source_words)


def verify_occurrence(claim: Claim, source: dict) -> tuple[str, list[str]]:
    if claim.verification in {"FULL TEXT VERIFIED", "GUIDELINE VERIFIED"}:
        return "PASS", []
    failures = validate_tag_policy(claim, "abstract")
    abstract = source.get("abstract", "")
    if source.get("status") != "ok" or len(abstract) < MIN_EVIDENCE_LENGTH:
        failures.append("PubMed abstract unavailable or too short")
    if abstract and keyword_overlap(claim.claim_text, abstract) < 2:
        failures.append("claim has fewer than two meaningful words overlapping the abstract")
    if abstract and has_numeric_data(claim.claim_text):
        abstract_numbers = extract_numbers(abstract)
        missing = [number for number in extract_claim_numbers(claim.claim_text) if number not in abstract_numbers]
        if missing:
            failures.append(f"numbers absent from abstract: {missing}")
    return ("BLOCK" if failures else "PASS"), failures


def build_report(path: Path, skip_fetch: bool = False) -> tuple[dict, int]:
    text = path.read_text(encoding="utf-8")
    legacy = sorted(set(match.group(0) for match in LEGACY_TAG_RE.finditer(text)))
    claims = extract_lesson_claims(text)
    if not claims:
        return {
            "document": str(path.resolve()),
            "parsed_claim_count": 0,
            "status": "FAIL",
            "reason": "No PMID claim occurrences parsed",
            "legacy_tags": legacy,
            "checks": [],
        }, 2

    cache: dict[str, dict] = {}
    rows = []
    for claim in claims:
        if claim.source_id not in cache:
            if skip_fetch:
                cache_path = CACHE_DIR / f"{claim.source_id}.json"
                try:
                    cache[claim.source_id] = json.loads(cache_path.read_text(encoding="utf-8"))
                except (OSError, json.JSONDecodeError):
                    cache[claim.source_id] = {"status": "error", "abstract": ""}
            else:
                try:
                    cache[claim.source_id] = fetch_source(claim.source_id)
                except Exception as exc:
                    cache[claim.source_id] = {"status": "error", "abstract": "", "error": str(exc)}
        status, failures = verify_occurrence(claim, cache[claim.source_id])
        rows.append({**claim.to_dict(), "status": status, "failures": failures})

    if legacy:
        rows.append({"claim_id": "TAG-POLICY", "status": "BLOCK", "failures": [f"legacy verification tags are forbidden: {legacy}"]})
    blocked = sum(row["status"] != "PASS" for row in rows)
    report = {
        "document": str(path.resolve()),
        "parsed_claim_count": len(claims),
        "verified_claim_count": len(claims) - blocked,
        "status": "PASS" if blocked == 0 else "FAIL",
        "legacy_tags": legacy,
        "checks": rows,
    }
    return report, 0 if blocked == 0 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify each lesson claim occurrence against PubMed")
    parser.add_argument("md", type=Path)
    parser.add_argument("--strict", action="store_true", help="Retained for CLI compatibility; verification is always strict")
    parser.add_argument("--skip-fetch", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    if not args.md.is_file():
        parser.error(f"file not found: {args.md}")
    report, code = build_report(args.md, args.skip_fetch)
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload, encoding="utf-8")
    print(payload)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
