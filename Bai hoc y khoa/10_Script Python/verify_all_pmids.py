"""Verify existence, exact identity, and relevance from an evidence bundle offline."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from evidence_verify import identity_report, write_report

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("md", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--topic")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    report, code = identity_report(args.md, args.evidence_bundle, args.topic)
    write_report(report, args.json_out)
    return code
if __name__ == "__main__": raise SystemExit(main())
