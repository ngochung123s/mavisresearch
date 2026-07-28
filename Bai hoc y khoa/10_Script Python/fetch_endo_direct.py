#!/usr/bin/env python3
"""
Fetch PubMed abstracts directly via E-utilities efetch.
Bypass the broken MCP pubmed_fetch wrapper.
"""
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

EMAIL = "thanh-anh.researcher@example.com"
API_KEY = ""  # efetch doesn't need it; saves us from wrong-key issues
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

KEY_PMIDS = [
    "33880420", "33880419", "36414088", "37203432", "37964969",
    "30624659", "31786047", "35222264", "37284089", "32330673",
    "36686483", "30929719",
]


def efetch(pmid):
    params = {
        "db": "pubmed",
        "id": pmid,
        "rettype": "abstract",
        "retmode": "text",
        "email": EMAIL,
    }
    if API_KEY:
        params["api_key"] = API_KEY
    url = f"{BASE}/efetch.fcgi?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return f"ERROR: {e}"


def parse_abstract(text):
    """Parse PubMed efetch text format into structured fields."""
    if text.startswith("ERROR:"):
        return {"raw": text, "error": True}

    out = {"raw": text, "error": False}

    # Title (first line starting with capitalized text, ends without period often)
    # Better: split into sections by blank lines
    sections = {}
    current = "header"
    buf = []
    for line in text.splitlines():
        if line.strip() == "":
            if buf:
                sections.setdefault(current, []).append("\n".join(buf).strip())
                buf = []
        else:
            buf.append(line)
    if buf:
        sections.setdefault(current, []).append("\n".join(buf).strip())

    # First non-empty section is title + authors
    all_text = "\n".join(["\n".join(v) for v in sections.values()])

    # Find structured abstract sections
    structured = {}
    for label in ["OBJECTIVE", "DESIGN", "SETTING", "PATIENTS", "PATIENT(S)",
                  "INTERVENTIONS", "INTERVENTION(S)", "MAIN OUTCOME MEASURES",
                  "RESULTS", "CONCLUSION(S)", "CONCLUSION", "METHODS",
                  "INTRODUCTION", "AIM", "BACKGROUND", "SUMMARY"]:
        m = re.search(rf"\n\s*{re.escape(label)}:\s*(.*?)(?=\n\s*(?:OBJECTIVE|DESIGN|SETTING|PATIENTS|PATIENT\(S\)|INTERVENTIONS|INTERVENTION\(S\)|MAIN OUTCOME|RESULTS|CONCLUSION|CONCLUSION\(S\)|METHODS|INTRODUCTION|AIM|BACKGROUND|SUMMARY|$))",
                      all_text, re.DOTALL)
        if m:
            structured[label] = m.group(1).strip()[:2000]

    out["sections"] = structured
    out["full_text"] = text[:8000]  # cap to 8KB
    return out


def main():
    out = {}
    for pmid in KEY_PMIDS:
        print(f"[fetch] {pmid}", flush=True)
        text = efetch(pmid)
        parsed = parse_abstract(text)
        if parsed.get("error"):
            print(f"  ERROR: {parsed['raw'][:100]}")
        else:
            sects = list(parsed.get("sections", {}).keys())
            print(f"  -> sections: {sects}")
        out[pmid] = parsed
        time.sleep(0.4)

    OUT_DIR = Path("F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/pubmed_searches")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "endo_receptivity_abstracts_direct_2026-06-21.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    main()