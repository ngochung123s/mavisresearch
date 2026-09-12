"""Fail-closed retraction, concern, correction, reinstatement freshness gate offline."""
from __future__ import annotations
import argparse
from pathlib import Path
from evidence_verify import retraction_report, write_report

def check_md(md_path: Path, evidence_bundle: Path) -> tuple[dict, int]:
    return retraction_report(Path(md_path), Path(evidence_bundle))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--md", required=True, type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    report, code = check_md(args.md, args.evidence_bundle)
    write_report(report, args.json_out)
    return code
if __name__ == "__main__": raise SystemExit(main())
