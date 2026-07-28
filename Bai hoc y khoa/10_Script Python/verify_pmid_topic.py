#!/usr/bin/env python3
"""Advisory MeSH topic screen; never authorizes or blocks claim support.

Exit 0 means the advisory completed, including when a paper is unindexed or
has no mapped topic. Required verification is performed claim-by-claim by
``verify_claim_vs_abstract.py`` and ``verify_claims.py``.
"""

import argparse
import json
import re
import sys
import time
import urllib.request

NCBIBASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

MESH_TOPIC_MAP = {
    "irritable bowel syndrome": [
        "Irritable Bowel Syndrome",
        "Irritable Bowel Syndrome "
        "Irritable Bowel Syndrome"
    ],
    "gastroesophageal reflux": [
        "Gastroesophageal Reflux",
    ],
    "peptic ulcer": [
        "Peptic Ulcer",
    ],
    "hypertension": [
        "Hypertension",
    ],
    "diabetes": [
        "Diabetes Mellitus",
    ],
    "heart failure": [
        "Heart Failure",
    ],
    "pneumonia": [
        "Pneumonia",
    ],
    "liver cirrhosis": [
        "Liver Cirrhosis",
    ],
    "electrocardiography": [
        "Electrocardiography",
        "Heart Conduction System",
        "Arrhythmias, Cardiac",
        "Myocardial Infarction",
        "Hyperkalemia"
    ],
    "inflammatory bowel diseases": [
        "Inflammatory Bowel Diseases",
        "Colitis, Ulcerative",
        "Crohn Disease",
        "Crohn's Disease",
        "Calprotectin"
        "Irritable Bowel Syndrome",
        "Diarrhea",
    ],
    "diuretics": [
        "Diuretics",
        "Sodium Potassium Chloride Symporter Inhibitors",
        "Sodium Chloride Symporter Inhibitors",
        "Mineralocorticoid Receptor Antagonists",
        "Kidney Tubules",
        "Nephrons"
    ],
}

def fetch_idlist_from_brief(brief_path):
    with open(brief_path, encoding="utf-8") as f:
        text = f.read()
    return list(set(re.findall(r"PMID[:\s]+(\d{7,8})", text)))

def fetch_mesh_terms(pmid):
    url = f"{NCBIBASE}/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    req = urllib.request.urlopen(url)
    data = req.read().decode("utf-8")
    mesh_terms = re.findall(r"<DescriptorName[^>]*>([^<]+)</DescriptorName>", data)
    return mesh_terms

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("brief", help="Path to RESEARCH_BRIEF.md")
    parser.add_argument("--topic", required=True, help="Lesson topic in English")
    args = parser.parse_args()

    topic = args.topic.lower()
    expected_mesh = MESH_TOPIC_MAP.get(topic, [])
    if not expected_mesh:
        print(f"[INFO] No MeSH map entry for '{topic}'; topic screening is advisory only.")

    pmids = fetch_idlist_from_brief(args.brief)
    if not pmids:
        print("[WARN] No PMIDs found in brief; strict PMID preflight must decide release eligibility.")
        sys.exit(0)

    reviews = []
    passes = []
    for pmid in pmids:
        time.sleep(0.3)
        try:
            mesh_terms = fetch_mesh_terms(pmid)
        except Exception as e:
            print(f"[REVIEW] PMID {pmid}: cannot fetch MeSH — {e}")
            reviews.append(pmid)
            continue
        overlap = [m for m in mesh_terms if any(em.lower() in m.lower() or m.lower() in em.lower() for em in expected_mesh)]
        if overlap:
            print(f"[PASS] PMID {pmid}: MeSH overlap → {overlap}")
            passes.append(pmid)
        else:
            print(f"[REVIEW] PMID {pmid}: no MeSH overlap with '{topic}' (unindexed/mechanistic papers may still be valid)")
            reviews.append(pmid)

    print(f"\n[SUMMARY] PASS: {len(passes)}/{len(pmids)}, REVIEW: {len(reviews)}")
    print("[EXIT 0] Advisory complete; use claim-level evidence to accept or reject each source.")
    sys.exit(0)

if __name__ == "__main__":
    main()
