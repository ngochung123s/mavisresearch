#!/usr/bin/env python3
"""Verify locked brief claim occurrences using a provider-neutral bundle offline."""
from __future__ import annotations
import argparse
from pathlib import Path
from evidence_verify import claim_report, write_report

def build_report(brief: Path, evidence_bundle: Path, topic: str | None = None) -> tuple[dict, int]:
    return claim_report(brief, evidence_bundle, brief=True, topic=topic)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--topic")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    report, code = build_report(args.brief, args.evidence_bundle, args.topic)
    write_report(report, args.json_out)
    return code
if __name__ == "__main__": raise SystemExit(main())
