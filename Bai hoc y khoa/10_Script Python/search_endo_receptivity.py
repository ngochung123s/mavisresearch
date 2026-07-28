#!/usr/bin/env python3
"""
Search PubMed via MCP wrapper for daily lesson 21/06:
Endometrial receptivity & advanced ultrasound.
"""
import json
import subprocess
import time
from pathlib import Path

QUERIES = [
    ("era_overview", "ERA endometrial receptivity analysis IVF", 2018, "relevance", 10),
    ("era_rct", "endometrial receptivity analysis randomized trial pregnancy", 2018, "relevance", 8),
    ("endo_thickness", "endometrial thickness IVF live birth meta-analysis", 2019, "relevance", 8),
    ("endo_3d_volume", "3D endometrial volume ultrasound IVF pregnancy", 2018, "relevance", 8),
    ("uterine_doppler", "uterine artery Doppler pulsatility index IVF", 2018, "relevance", 8),
    ("woi_window", "window of implantation endometrium transcriptomic ERA", 2018, "relevance", 8),
    ("asrm_ivf", "ASRM guideline IVF endometrial evaluation ultrasound", 2018, "relevance", 5),
    ("eshre_era", "ESHRE ERA endometrial receptivity", 2018, "relevance", 5),
    ("recurrent_implant", "recurrent implantation failure endometrium evaluation", 2020, "relevance", 6),
]

def call_pubmed_search(args):
    """Call mavis mcp call pubmed pubmed_search with given args."""
    args_file = Path("F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/_tmp_args.json")
    args_file.write_text(json.dumps(args), encoding="utf-8")
    cmd_str = f'mavis mcp call pubmed pubmed_search --file "{args_file}"'
    r = subprocess.run(cmd_str, capture_output=True, text=True, timeout=60, shell=True)
    if r.returncode != 0:
        return {"error": r.stderr or r.stdout}
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return {"error": "non-json", "raw": r.stdout[:500]}

def main():
    out = {}
    for label, query, year, sort, limit in QUERIES:
        print(f"[search] {label}: {query}")
        args = {
            "query": query,
            "year_from": year,
            "sort": sort,
            "limit": limit,
        }
        result = call_pubmed_search(args)
        if "error" in result:
            print(f"  ERROR: {result['error'][:200]}")
            out[label] = {"query": query, "year_from": year, "error": result["error"][:300]}
        else:
            results = result.get("results", [])
            pmids = [r.get("pmid") for r in results if r.get("pmid")]
            total = result.get("total_returned", len(pmids))
            print(f"  -> {len(pmids)} hits; total_returned={total}")
            out[label] = {
                "query": query,
                "year_from": year,
                "total_returned": total,
                "results": results[:limit],
                "pmids": pmids[:limit],
            }
        time.sleep(0.4)

    out_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/pubmed_searches")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "endo_receptivity_2026-06-21.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved to: {out_path}")

    # Print concise list
    print("\n=== PMID list per topic ===")
    for label, data in out.items():
        if "error" in data:
            print(f"{label}: ERROR")
            continue
        print(f"{label} (total={data.get('total')}): {', '.join(data['pmids'][:5])}")

if __name__ == "__main__":
    main()