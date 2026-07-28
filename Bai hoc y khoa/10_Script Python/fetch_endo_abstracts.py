#!/usr/bin/env python3
"""Fetch PubMed abstracts - incremental save."""
import json
import subprocess
import time
import sys
from pathlib import Path

KEY_PMIDS = [
    "33880420", "33880419", "36414088", "37203432", "37964969",
    "30624659", "31786047", "35222264", "37284089", "32330673",
    "36686483", "30929719",
]

OUT_DIR = Path("F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/pubmed_searches")
OUT_FILE = OUT_DIR / "endo_receptivity_abstracts_2026-06-21.json"
PARTIAL_FILE = OUT_DIR / "endo_receptivity_abstracts_PARTIAL.json"


def fetch_one(pmid):
    args_file = OUT_DIR / "_tmp_args.json"
    args_file.write_text(json.dumps({"pmid": pmid}), encoding="utf-8")
    cmd = f'mavis mcp call pubmed pubmed_fetch --file "{args_file}"'
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20, shell=True)
    except subprocess.TimeoutExpired:
        return {"pmid": pmid, "error": "TIMEOUT"}
    if r.returncode != 0:
        return {"pmid": pmid, "error": r.stderr[:300] or r.stdout[:300]}
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"pmid": pmid, "error": "non-json", "raw": r.stdout[:400]}


def main():
    # Load partial if exists
    partial = {}
    if PARTIAL_FILE.exists():
        try:
            partial = json.loads(PARTIAL_FILE.read_text(encoding="utf-8"))
            print(f"Loaded {len(partial)} from partial")
        except Exception:
            partial = {}

    done = set(partial.keys())
    remaining = [p for p in KEY_PMIDS if p not in done]
    print(f"Already done: {sorted(done)}")
    print(f"Remaining: {remaining}")

    for pmid in remaining:
        print(f"[fetch] {pmid}", flush=True)
        d = fetch_one(pmid)
        if "error" in d:
            print(f"  ERROR: {d['error'][:200]}")
        else:
            t = d.get("title", "?")[:80]
            print(f"  -> {t}", flush=True)
        partial[pmid] = d
        # Save after each fetch
        PARTIAL_FILE.write_text(json.dumps(partial, indent=2, ensure_ascii=False), encoding="utf-8")
        time.sleep(0.5)

    # Final save
    OUT_FILE.write_text(json.dumps(partial, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved to: {OUT_FILE} ({len(partial)} papers)")


if __name__ == "__main__":
    main()