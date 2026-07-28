"""Validate official guideline evidence independently from PubMed.

Evidence JSON schema:
{
  "guidelines": [{
    "claim_id": "C-001", "society": "ESHRE", "title": "...",
    "document_id": "...", "version": "2025", "publication_date": "2025-...",
    "accessed_at": "2026-07-28", "canonical_url": "https://...",
    "local_copy": "outputs/sources/file.pdf", "sha256": "...",
    "recommendation_text": "...", "superseded_by": null
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

from verification_core import sha256_file

REQUIRED = {
    "claim_id", "society", "title", "document_id", "version",
    "publication_date", "accessed_at", "canonical_url", "local_copy",
    "sha256", "recommendation_text", "superseded_by",
}


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
        for field in REQUIRED - {"superseded_by"}:
            if not isinstance(row[field], str) or not row[field].strip():
                failures.append(f"missing {field}")
        parsed = urlparse(row.get("canonical_url", ""))
        if parsed.scheme != "https" or not parsed.netloc:
            failures.append("canonical_url must be an official HTTPS URL")
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
