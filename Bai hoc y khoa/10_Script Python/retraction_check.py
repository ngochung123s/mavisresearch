"""Fail-closed PubMed retraction and expression-of-concern gate.

Usage: ``retraction_check.py --md lesson.md [--strict] [--json-out report.json]``.
Zero PMID or an incomplete lookup fails in strict mode.
"""
import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re
import time
from pathlib import Path
import sys; sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def check_pmids(pmids, timeout=10):
    """Check list of PMIDs for retraction status.
    Returns dict: {pmid: {retracted: bool, reason: str, details: dict}}
    """
    if not pmids:
        return {}
    
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={','.join(pmids)}&retmode=xml&rettype=abstract"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
    except Exception as e:
        return {p: {"retracted": None, "reason": f"Fetch error: {e}", "details": {}} for p in pmids}
    
    root = ET.fromstring(data)
    results = {}
    
    for art in root.iter("PubmedArticle"):
        pmid_elem = art.find(".//PMID")
        if pmid_elem is None:
            continue
        pmid = pmid_elem.text.strip()
        
        # Check PublicationType for retraction indicators
        pub_types = []
        for pt in art.findall(".//PublicationType"):
            if pt.text:
                pub_types.append(pt.text.strip())
        
        retracted = False
        reason = ""
        for pt in pub_types:
            if "Retracted" in pt or "Retraction" in pt:
                retracted = True
                reason = pt
                break
            if "Expression of Concern" in pt:
                retracted = True
                reason = pt
                break
        
        # Also check for CommentsCorrections
        corrections = []
        for cc in art.findall(".//CommentsCorrections"):
            ref_type = cc.attrib.get("RefType", "")
            ref_pmid = (cc.findtext("PMID") or "").strip()
            note = (cc.findtext("Note") or "").strip()
            if "Retraction" in ref_type or "Retraction" in note:
                corrections.append({"type": ref_type, "pmid": ref_pmid, "note": note})
        
        # Title check
        title_node = art.find(".//ArticleTitle")
        title = "".join(title_node.itertext()).strip() if title_node is not None else ""
        if "retraction" in title.lower() or "retracted" in title.lower():
            retracted = True
            reason = reason or "Title contains retraction notice"
        
        details = {
            "title": title[:200],
            "journal": (art.findtext(".//Journal/Title") or ""),
            "year": (art.findtext(".//PubDate/Year") or "")[:4],
            "publication_types": pub_types,
            "corrections": corrections,
        }
        
        results[pmid] = {
            "retracted": retracted,
            "reason": reason,
            "details": details,
        }
    
    return results


def check_md(md_path):
    """Extract PMIDs from MD and check them."""
    text = Path(md_path).read_text(encoding='utf-8')
    pmids = list(set(re.findall(r'PMID:?\s*[*\s]*(\d{7,8})', text)))
    return check_pmids(pmids)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Check PubMed retraction status")
    parser.add_argument("pmids", nargs="*")
    parser.add_argument("--md")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    pmids = [value for value in args.pmids if re.fullmatch(r"\d{7,8}", value)]
    if args.md:
        text = Path(args.md).read_text(encoding="utf-8")
        pmids.extend(re.findall(r"PMID:?\s*[*\s]*(\d{7,8})", text))
    pmids = sorted(set(pmids))
    if not pmids:
        report = {"status": "FAIL" if args.strict else "PASS", "checked": 0, "error": "No PMIDs found", "results": {}}
        if args.json_out:
            args.json_out.parent.mkdir(parents=True, exist_ok=True)
            args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(2 if args.strict else 0)
    print(f"[retraction_check] Checking {len(pmids)} PMIDs...")
    results = check_pmids(pmids)
    
    retracted = []
    unknown = []
    clean = []
    
    for pmid, info in sorted(results.items()):
        if info.get("retracted") is None:
            unknown.append(pmid)
            print(f"  ❓ PMID {pmid}: FETCH ERROR — {info.get('reason', 'Unknown')}")
        elif info["retracted"]:
            retracted.append(pmid)
            print(f"  🛑 PMID {pmid}: RETRACTED — {info['reason']}")
            d = info["details"]
            print(f"      Title: {d['title'][:150]}")
            print(f"      Journal: {d['journal']} ({d['year']})")
        else:
            clean.append(pmid)
    
    complete = len(results) == len(pmids)
    report = {
        "status": "PASS" if not retracted and not unknown and complete else "FAIL",
        "checked": len(results),
        "expected": len(pmids),
        "clean": clean,
        "retracted_or_concern": retracted,
        "unknown": unknown,
        "results": results,
    }
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if retracted:
        sys.exit(1)
    if unknown or not complete:
        sys.exit(2 if args.strict else 0)
    sys.exit(0)


if __name__ == '__main__':
    main()
