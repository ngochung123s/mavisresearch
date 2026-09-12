"""Verify every lesson claim occurrence using a provider-neutral bundle offline."""
from __future__ import annotations
import argparse
from pathlib import Path
from evidence_verify import claim_report, write_report

def build_report(path: Path, evidence_bundle: Path, topic: str | None = None, **_: object) -> tuple[dict, int]:
    return claim_report(path, evidence_bundle, brief=False, topic=topic)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("md", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--topic")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--guideline-report", type=Path)
    parser.add_argument("--full-text-report", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    report, code = build_report(args.md, args.evidence_bundle, args.topic)
    write_report(report, args.json_out)
    return code
if __name__ == "__main__": raise SystemExit(main())
