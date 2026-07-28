#!/usr/bin/env python3
"""
extract_claims_from_abstract.py
Tự động trích xuất các câu có chứa số liệu (% / mg / RR / CI / n=) từ Abstract của một PMID.
Giúp bác sĩ copy thẳng vào RESEARCH_BRIEF.md mà không phải gõ tay.
Usage: python extract_claims_from_abstract.py <PMID>
"""

import argparse
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

NCBIBASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_abstract(pmid):
    url = f"{NCBIBASE}/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    req = urllib.request.urlopen(url)
    data = req.read().decode("utf-8")
    root = ET.fromstring(data)
    
    abstract_texts = root.findall('.//AbstractText')
    if not abstract_texts:
        return None
        
    full_abstract = " ".join([t.text for t in abstract_texts if t.text])
    return full_abstract

def extract_claims(abstract):
    # Tách thành các câu (chia theo dấu chấm)
    sentences = re.split(r'(?<=[.!?])\s+', abstract)
    
    # Pattern tìm số liệu
    claim_patterns = [
        r"\bRR\s*[=:]\s*\d+\.?\d*",
        r"\bCI\s*[=:]\s*\d+\.?\d*\s*[-–]\s*\d+\.?\d*",
        r"\ba?OR\s*[=:]\s*\d+\.?\d*",
        r"\ba?RR\s*[=:]\s*\d+\.?\d*",
        r"\bn\s*=\s*\d{2,}",
        r"\d+\.?\d*\s*%",
        r"\bp\s*[<=<]\s*0\.\d+",
        r"\bHR\s*[=:]\s*\d+\.?\d*",
        r"\bSMD\s*[=:]\s*[\-+]?\d+\.?\d*",
        r"\bAUC\s*[=:]\s*\d+\.?\d*",
        r"\d+\s*mg",
        r"\d+\s*mcg",
        r"\d+\s*g\b",
        r"\d+\s*mmol"
    ]
    
    combined_pattern = "|".join(claim_patterns)
    
    extracted = []
    for sentence in sentences:
        if re.search(combined_pattern, sentence, re.IGNORECASE):
            extracted.append(sentence.strip())
            
    return extracted

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pmid", help="PMID to extract claims from")
    args = parser.parse_args()

    print(f"Fetching abstract for PMID: {args.pmid}...")
    try:
        abstract = fetch_abstract(args.pmid)
    except Exception as e:
        print(f"Error fetching PMID: {e}")
        sys.exit(1)
        
    if not abstract:
        print("No abstract found for this PMID.")
        sys.exit(0)
        
    claims = extract_claims(abstract)
    
    print("\n" + "="*60)
    print(f"EXTRACTED CLAIMS FOR PMID {args.pmid}")
    print("="*60)
    
    if not claims:
        print("No specific data claims (%, mg, RR, CI, etc.) found in the abstract.")
        print("\nFull abstract preview:")
        print(abstract[:300] + "...")
    else:
        for i, claim in enumerate(claims, 1):
            print(f"\n[Claim {i}]: {claim}")
            print(f"-> Format for Brief: - PMID: {args.pmid} — {claim} [DATA VERIFIED] (chỉ sau khi quote và số khớp chính xác)")
            
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
