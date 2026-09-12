"""Validate official guideline evidence independently from PubMed.

Evidence JSON schema:
{
  "guidelines": [{
    "claim_id": "C-001", "society": "ESHRE", "title": "...",
    "document_id": "...", "version": "2025", "publication_date": "2025-...",
    "accessed_at": "2026-07-28", "canonical_url": "https://...",
    "local_copy": "outputs/sources/file.pdf", "sha256": "...",
    "recommendation_text": "...", "locator": "Section 5 / Page 12", "superseded_by": null
  }]
}
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from verification_core import extract_claim_numbers, extract_numbers, has_numeric_data, sha256_file

REQUIRED = {
    "claim_id", "society", "title", "document_id", "version",
    "publication_date", "accessed_at", "canonical_url", "local_copy",
    "sha256", "recommendation_text", "locator", "pmid", "superseded_by",
}

REGISTRY_PATH = Path(__file__).with_name("guideline_registry.json")

OFFICIAL_PUBLISHERS = {
    "doi.org", "www.jacc.org", "jacc.org", "ahajournals.org", "www.ahajournals.org",
    "academic.oup.com", "sciencedirect.com", "www.sciencedirect.com",
    "ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov", "diabetesjournals.org", "abcd.care",
}


def _load_registry() -> dict:
    if REGISTRY_PATH.is_file():
        try:
            return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def is_official_host(society: str, url: str, registry: dict) -> tuple[bool, str]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        return False, "canonical_url must be an official HTTPS URL"
    netloc = parsed.netloc.lower()

    if not registry:
        return False, "guideline registry is unavailable or empty"

    registry_hosts = set()
    found_society = False
    for key, data in registry.items():
        if key == "_meta":
            continue
        # Society match: exact match, or substring match e.g. AHA/ACC/HRS matching AHA/ACC
        soc_parts = [p.strip() for p in society.split("/")]
        key_parts = [p.strip() for p in key.split("/")]
        if key == society or key in society or society in key or any(p in key_parts for p in soc_parts):
            found_society = True
            if isinstance(data, dict):
                if "url_base" in data:
                    registry_hosts.add(urlparse(data["url_base"]).netloc.lower())
                if "guidelines" in data and isinstance(data["guidelines"], dict):
                    for ginfo in data["guidelines"].values():
                        if isinstance(ginfo, dict) and "url" in ginfo:
                            registry_hosts.add(urlparse(ginfo["url"]).netloc.lower())

    if not found_society:
        return False, f"society '{society}' is not registered in guideline_registry.json"

    allowed = registry_hosts | OFFICIAL_PUBLISHERS
    if netloc not in allowed and not any(netloc.endswith("." + h) for h in allowed):
        return False, f"canonical_url host '{netloc}' is not registered or known official host for society '{society}'"

    return True, ""


def extract_source_text(local_copy: Path) -> tuple[str, str]:
    """Extract plain text from local source file (.txt, .md, .pdf). Return (text, error)."""
    suffix = local_copy.suffix.lower()
    if suffix in {".txt", ".md"}:
        try:
            return local_copy.read_text(encoding="utf-8", errors="replace"), ""
        except Exception as exc:
            return "", f"failed to read text file: {exc}"
    elif suffix == ".pdf":
        for mod_name in ("fitz", "pdfplumber", "pdfminer.high_level", "PyPDF2"):
            try:
                if mod_name == "fitz":
                    import fitz
                    doc = fitz.open(local_copy)
                    pages = [page.get_text() for page in doc]
                    doc.close()
                    return "\n".join(pages), ""
                elif mod_name == "pdfplumber":
                    import pdfplumber
                    with pdfplumber.open(local_copy) as pdf:
                        pages = [p.extract_text() or "" for p in pdf.pages]
                        return "\n".join(pages), ""
                elif mod_name == "pdfminer.high_level":
                    from pdfminer.high_level import extract_text
                    return extract_text(local_copy), ""
                elif mod_name == "PyPDF2":
                    import PyPDF2
                    reader = PyPDF2.PdfReader(str(local_copy))
                    pages = [p.extract_text() or "" for p in reader.pages]
                    return "\n".join(pages), ""
            except Exception:
                continue
        return "", "no supported PDF extraction library available (fitz/pdfplumber/pdfminer/PyPDF2)"
    else:
        return "", f"unsupported source format: {suffix} (only .txt, .md, .pdf supported)"

def validate_evidence(path: Path, max_age_days: int = 730) -> tuple[dict, int]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"status": "FAIL", "error": str(exc), "guidelines": []}, 2
    rows = payload.get("guidelines") if isinstance(payload, dict) else None
    if not isinstance(rows, list) or not rows:
        return {"status": "FAIL", "error": "guidelines must be a non-empty list", "guidelines": []}, 2

    today = dt.date.today()
    checked = []
    for index, row in enumerate(rows, 1):
        failures = []
        if not isinstance(row, dict) or set(row) != REQUIRED:
            checked.append({"index": index, "status": "FAIL", "failures": [f"fields must be exactly {sorted(REQUIRED)}"]})
            continue
        for field in REQUIRED - {"superseded_by", "pmid"}:
            if not isinstance(row[field], str) or not row[field].strip():
                failures.append(f"missing {field}")
        pmid_val = row.get("pmid")
        if pmid_val not in (None, "") and not (isinstance(pmid_val, str) and re.fullmatch(r"\d{7,8}", pmid_val.strip())):
            failures.append(f"pmid must be null or a valid 7-8 digit PMID string (got {pmid_val!r})")
        locator_str = row.get("locator", "")
        if locator_str.upper().startswith("UNVERIFIED"):
            failures.append(f"locator is unverified: '{locator_str}' (must be a valid machine-readable locator like section/page/paragraph)")
        if "..." in row.get("recommendation_text", "") or "…" in row.get("recommendation_text", ""):
            failures.append("recommendation_text contains forbidden ellipsis '...' (must be exact continuous quote)")
        registry = _load_registry()
        valid_url, url_err = is_official_host(row.get("society", ""), row.get("canonical_url", ""), registry)
        if not valid_url:
            failures.append(url_err)
        if row.get("superseded_by") not in (None, ""):
            failures.append(f"guideline is superseded by {row['superseded_by']}")
        try:
            accessed = dt.date.fromisoformat(row["accessed_at"])
            if accessed > today or (today - accessed).days > max_age_days:
                failures.append(f"freshness check is stale: {row['accessed_at']}")
        except (ValueError, TypeError):
            failures.append("accessed_at must be YYYY-MM-DD")
        try:
            dt.date.fromisoformat(row["publication_date"])
        except (ValueError, TypeError):
            failures.append("publication_date must be YYYY-MM-DD")
        local_copy = Path(row.get("local_copy", ""))
        if not local_copy.is_file():
            failures.append(f"local_copy not found: {local_copy}")
        elif not re.fullmatch(r"[0-9a-f]{64}", row.get("sha256", "")) or sha256_file(local_copy) != row["sha256"]:
            failures.append("local_copy SHA-256 mismatch")
        else:
            text, extract_err = extract_source_text(local_copy)
            if extract_err:
                failures.append(extract_err)
            else:
                rec_text = row.get("recommendation_text", "")
                norm_rec = " ".join(rec_text.split())
                norm_src = " ".join(text.split())
                if norm_rec not in norm_src:
                    failures.append("recommendation_text quote not found as exact normalized continuous substring in local_copy")
                if has_numeric_data(rec_text):
                    src_numbers = extract_numbers(text)
                    rec_numbers = extract_claim_numbers(rec_text)
                    missing = [num for num in rec_numbers if num not in src_numbers]
                    if missing:
                        failures.append(f"recommendation_text numbers absent from local source: {missing}")

        checked.append({**row, "status": "FAIL" if failures else "PASS", "failures": failures})

    failed = sum(row["status"] != "PASS" for row in checked)
    return {"status": "PASS" if failed == 0 else "FAIL", "checked": len(checked), "failed": failed, "guidelines": checked}, 0 if failed == 0 else 2

def main() -> int:
    parser = argparse.ArgumentParser(description="Verify official guideline evidence")
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--max-age-days", type=int, default=730)
    args = parser.parse_args()
    report, code = validate_evidence(args.evidence, args.max_age_days)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(output, encoding="utf-8")
    print(output)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
