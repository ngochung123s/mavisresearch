#!/usr/bin/env python3
"""
preflight_claim_check.py — Pre-execution claim blocker.
Chạy strict PMID existence + claim/abstract verification; MeSH chỉ là advisory.
Usage: python preflight_claim_check.py <RESEARCH_BRIEF.md> [--topic "..."]
"""

import argparse
import subprocess
import sys
import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", help="Path to RESEARCH_BRIEF.md")
    parser.add_argument("--topic", help="Optional lesson topic for advisory MeSH screening")
    args = parser.parse_args()

    brief = args.brief
    topic = args.topic

    print(f"=== STRICT CLAIM PREFLIGHT for {brief} ===\n")

    print("--- Gate 1: PMID existence ---")
    existence = subprocess.run([
        sys.executable,
        os.path.join(SCRIPTS_DIR, "preflight_check_pmids.py"),
        brief, "--strict"
    ])
    if existence.returncode != 0:
        print("\n[REJECT] PMID existence preflight failed.")
        sys.exit(2)

    if topic:
        print("\n--- Advisory: MeSH topic screen ---")
        subprocess.run([
            sys.executable,
            os.path.join(SCRIPTS_DIR, "verify_pmid_topic.py"),
            brief, "--topic", topic
        ])

    print("\n--- Gate 2: Every claim occurrence vs abstract ---")
    claims = subprocess.run([
        sys.executable,
        os.path.join(SCRIPTS_DIR, "verify_claim_vs_abstract.py"),
        brief
    ])
    if claims.returncode != 0:
        print("\n[REJECT] Claim evidence preflight failed.")
        sys.exit(2)

    print("\n=== PREFLIGHT EXIT 0 === Strict source gates passed. Ready for execute.")
    sys.exit(0)

if __name__ == "__main__":
    main()
