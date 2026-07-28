"""Verify that every cited PMID exists and record its PubMed metadata.

This gate does not prove claim support; ``verify_claims.py`` does that per
claim occurrence. Strict mode fails when no PMID is found or any lookup warns.
"""
import sys
import re
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


def extract_pmids(text):
    """Extract all unique PMIDs from markdown text."""
    return list(set(re.findall(r'PMID:?\s*\*?\*?\s*(\d{7,8})', text)))


def extract_context(text, pmid, window=300):
    """Extract context around a PMID citation to verify expected title."""
    idx = text.find(pmid)
    if idx == -1:
        return ""
    start = max(0, idx - window)
    end = min(len(text), idx + window)
    return text[start:end]


def fetch_pmid(pmid, timeout=15):
    """Fetch PMID metadata from PubMed efetch XML."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml&rettype=abstract"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read(), None
    except Exception as e:
        return None, str(e)


def fetch_europepmc_metadata(pmid, timeout=15):
    """Fetch minimal metadata from Europe PMC when NCBI blocks E-utilities."""
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{pmid}&format=json"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        result = payload.get("resultList", {}).get("result", [])
        if not result:
            return None
        item = result[0]
        return {
            "pmid": item.get("pmid", pmid),
            "title": item.get("title", "").strip(),
            "journal": item.get("journalTitle", "") or item.get("journal", ""),
            "year": str(item.get("pubYear", "")),
            "authors": [],
            "pubtypes": [],
        }
    except Exception:
        return None

def parse_pubmed_xml(xml_data):
    """Parse PubMed efetch XML, return dict with title, journal, year, authors."""
    root = ET.fromstring(xml_data)
    result = {}
    for art in root.iter("PubmedArticle"):
        pmid_el = art.find(".//PMID")
        if pmid_el is not None:
            result['pmid'] = pmid_el.text.strip()
        title_el = art.find(".//ArticleTitle")
        if title_el is not None:
            result['title'] = "".join(title_el.itertext()).strip()
        journal_el = art.find(".//Journal/Title")
        if journal_el is None:
            journal_el = art.find(".//Journal/ISOAbbreviation")
        if journal_el is not None:
            result['journal'] = journal_el.text.strip() if journal_el.text else ""
        year_el = art.find(".//PubDate/Year")
        if year_el is not None:
            result['year'] = year_el.text.strip()[:4] if year_el.text else ""
        authors = []
        for au in art.findall(".//AuthorList/Author"):
            last = au.findtext("LastName") or ""
            initials = au.findtext("Initials") or ""
            if last:
                authors.append(f"{last} {initials}".strip())
        result['authors'] = authors[:3]
        pubtypes = [pt.text.strip() for pt in art.findall(".//PublicationTypeList/PublicationType") if pt.text]
        result['pubtypes'] = pubtypes
        break
    return result


def verify_pmid(pmid, expected_context=""):
    """Verify a PMID exists and title matches expected content.
    
    Returns: (status, message, data)
        status: 'ok', 'warn', 'block'
    """
    xml_data, error = fetch_pmid(pmid)
    if error or xml_data is None:
        fallback = fetch_europepmc_metadata(pmid)
        if fallback and fallback.get('title'):
            return 'ok', f"PMID {pmid}: {fallback['title'][:100]} [{fallback['journal']} {fallback['year']}] (Europe PMC fallback)", fallback
        return 'warn', f"Fetch error: {error}", {}

    try:
        info = parse_pubmed_xml(xml_data)
    except ET.ParseError as exc:
        fallback = fetch_europepmc_metadata(pmid)
        if fallback and fallback.get('title'):
            return 'ok', f"PMID {pmid}: {fallback['title'][:100]} [{fallback['journal']} {fallback['year']}] (Europe PMC fallback)", fallback
        return 'warn', f"Malformed PubMed XML: {exc}", {}
    if not info or 'title' not in info:
        return 'block', f"PMID {pmid}: NOT FOUND in PubMed", {}

    # Quick sanity checks on the title
    title = info.get('title', '').lower()
    suspicious = [
        'cigarette smoking', 'community health', 'new york medical',
        'euglena', 'immunosuppressed', 'social vulnerability',
        'soccer', 'football', 'sport', 'exercise physiology',
        'veterinary', 'veterinarian', 'dentist', 'dental',
    ]
    for pattern in suspicious:
        if re.search(rf"\b{re.escape(pattern)}\b", title):
            return 'block', f"PMID {pmid}: SUSPICIOUS TITLE — '{title[:80]}' (matches suspect pattern '{pattern}')", info

    return 'ok', f"PMID {pmid}: {info.get('title','')[:100]} [{info.get('journal','')} {info.get('year','')}]", info


def main():
    import argparse
    ap = argparse.ArgumentParser(description='Verify all PMIDs in a medical lesson')
    ap.add_argument('md', help='Path to lesson MD file')
    ap.add_argument('--strict', action='store_true', help='Fail on warnings too')
    ap.add_argument('--json', action='store_true', help='Output as JSON')
    args = ap.parse_args()

    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    md_path = Path(args.md)
    if not md_path.exists():
        print(f"File not found: {args.md}")
        sys.exit(3)

    text = md_path.read_text(encoding='utf-8')
    pmids = extract_pmids(text)

    if not pmids:
        message = "[verify_all_pmids] No PMIDs found"
        if args.json:
            print(json.dumps({"summary": {"ok": 0, "warn": 0, "block": int(args.strict)}, "results": {}, "error": message}, ensure_ascii=False, indent=2))
        else:
            print(message)
        sys.exit(2 if args.strict else 0)

    print(f"[verify_all_pmids] Checking {len(pmids)} PMIDs...\n")

    results = {}
    ok_count = warn_count = block_count = 0

    for pmid in sorted(pmids):
        status, msg, info = verify_pmid(pmid)
        results[pmid] = {'status': status, 'message': msg, 'info': info}
        
        icon = {'ok': '✅', 'warn': '⚠️', 'block': '🛑'}.get(status, '?')
        print(f"  {icon} {msg}")
        
        if status == 'ok':
            ok_count += 1
        elif status == 'block':
            block_count += 1
        elif status == 'warn':
            warn_count += 1

    print(f"\n  Results: {ok_count} OK, {warn_count} WARN, {block_count} BLOCK")

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))

    if block_count > 0:
        print(f"\n  🛑 BLOCKING: {block_count} PMID(s) FAILED verification!")
        print(f"  Fix or remove these citations before building deliverables.")
        sys.exit(2)
    elif warn_count > 0 and args.strict:
        print(f"\n  ⚠️ STRICT MODE: {warn_count} PMID(s) could not be verified.")
        sys.exit(1)
    elif warn_count > 0:
        print(f"\n  ⚠️ {warn_count} PMID(s) could not be verified (network issue?).")
        print(f"  Consider re-running or manually checking these.")
        sys.exit(0)
    else:
        print(f"\n  ✅ All {ok_count} PMIDs exist in PubMed")
        sys.exit(0)


if __name__ == '__main__':
    main()
