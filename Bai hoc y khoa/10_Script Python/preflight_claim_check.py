#!/usr/bin/env python3
"""Strict offline pre-execution evidence preflight."""
from __future__ import annotations
import argparse, subprocess, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def run(script: str, *args: str) -> int:
    return subprocess.run([sys.executable, str(SCRIPT_DIR / script), *args], cwd=SCRIPT_DIR).returncode

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--topic")
    args = parser.parse_args()
    common = [str(args.brief), "--evidence-bundle", str(args.evidence_bundle)]
    if args.topic: common += ["--topic", args.topic]
    if run("preflight_check_pmids.py", *common, "--strict") != 0: return 2
    if args.topic and run("verify_pmid_topic.py", str(args.brief), "--topic", args.topic, "--evidence-bundle", str(args.evidence_bundle)) != 0: return 2
    return 0 if run("verify_claim_vs_abstract.py", *common) == 0 else 2
if __name__ == "__main__": raise SystemExit(main())
