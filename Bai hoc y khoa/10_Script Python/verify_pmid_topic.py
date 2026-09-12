#!/usr/bin/env python3
"""Offline advisory topic screen backed by normalized bundle metadata."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from evidence_bundle import BundleError, extract_pmids, load_bundle, overlap_ratio

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", type=Path)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    args = parser.parse_args()
    try: bundle = load_bundle(args.evidence_bundle)
    except BundleError as exc:
        print(json.dumps({"status":"FAIL","error":str(exc)})); return 2
    rows=[]
    for pmid in extract_pmids(args.brief.read_text(encoding="utf-8")):
        record=bundle.record_for_pmid(pmid) or {}
        evidence=" ".join([record.get("title",""),record.get("abstract","")," ".join(record.get("topics",[]))])
        ratio=overlap_ratio(args.topic,evidence)
        rows.append({"pmid":pmid,"status":"INFO" if ratio>=0.12 else "REVIEW","overlap":ratio})
    print(json.dumps({"status":"PASS","results":rows},ensure_ascii=False,indent=2)); return 0
if __name__ == "__main__": raise SystemExit(main())
