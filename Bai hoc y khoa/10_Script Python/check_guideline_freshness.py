"""Check guideline freshness - tự động search PubMed cho mỗi guideline trong
guideline_versions.json, so sánh với current, báo cáo nếu có version mới.

IMPROVED v2:
- Tighter query (broad term + society abbrev + current year) để giảm false positive
- 2-phase: search → filter "guideline" article type + society name match
- Filter "new papers" must be same society (ESHRE/ACOG/ASRM) + contain "guideline"
"""
import json
import sys
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Config
REGISTRY_PATH = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\guideline_versions.json")
LOG_PATH = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\guideline_freshness_log.json")
API_KEY = ""  # PubMed API key optional
TZ_VN = timezone(timedelta(hours=7))

# Society keywords to filter guideline papers
SOCIETY_KEYWORDS = {
    "ESHRE": ["ESHRE", "European Society of Human Reproduction"],
    "ACOG": ["ACOG", "American College of Obstetricians"],
    "ASRM": ["ASRM", "American Society for Reproductive"],
    "ISUOG": ["ISUOG", "International Society of Ultrasound"],
    "NICE": ["NICE", "National Institute for Health"],
    "WHO": ["WHO", "World Health Organization"],
    "FIGO": ["FIGO", "International Federation of Gynecology"],
    "RCOG": ["RCOG", "Royal College of Obstetricians"],
    "SMFM": ["SMFM", "Society for Maternal-Fetal Medicine"],
    "RANZCOG": ["RANZCOG", "Royal Australian and New Zealand"],
}


def detect_society(name, g):
    """Detect society for this guideline."""
    name_lower = name.lower()
    for society, keywords in SOCIETY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in name_lower:
                return society
    return None


def search_pubmed(query, max_results=5, year_from=None, article_type="Guideline"):
    """Search PubMed, filter by article_type=Guideline and society keyword."""
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    # Use article type filter to bias toward guidelines
    if article_type:
        full_query = f"{query} AND {article_type}[pt]"
    else:
        full_query = query
    params = {
        "db": "pubmed",
        "term": full_query,
        "retmode": "json",
        "retmax": str(max_results),
        "sort": "date",
    }
    if year_from:
        params["mindate"] = f"{year_from}/01/01"
        params["datetype"] = "pdat"
    if API_KEY:
        params["api_key"] = API_KEY
    url = base + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        return {"error": str(e), "pmids": []}

    pmids = data.get("esearchresult", {}).get("idlist", [])
    if not pmids:
        return {"pmids": []}

    # Fetch details
    fetch_base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
        "rettype": "abstract",
    }
    if API_KEY:
        fetch_params["api_key"] = API_KEY
    fetch_url = fetch_base + "?" + urllib.parse.urlencode(fetch_params)
    try:
        with urllib.request.urlopen(fetch_url, timeout=30) as resp:
            xml_data = resp.read()
    except Exception as e:
        return {"error": f"fetch failed: {e}", "pmids": pmids}

    results = []
    root = ET.fromstring(xml_data)
    for art in root.findall(".//PubmedArticle"):
        try:
            pmid = art.findtext(".//PMID")
            title = art.findtext(".//ArticleTitle", "")
            year = art.findtext(".//PubDate/Year") or art.findtext(".//PubDate/MedlineDate", "").split(" ")[0]
            journal = art.findtext(".//Journal/Title", "") or art.findtext(".//Journal/ISOAbbreviation", "")
            first_author = art.findtext(".//AuthorList/Author[1]/LastName", "") or art.findtext(".//AuthorList/Author[1]/CollectiveName", "")
            # Article types
            article_types = [t.text for t in art.findall(".//PublicationTypeList/PublicationType") if t.text]
            is_guideline = "Journal Article" in article_types and "Guideline" in str(article_types)
            # Check if title has "guideline" or "recommendation" or "consensus"
            has_guideline_word = any(w in title.lower() for w in ["guideline", "recommendation", "consensus", "practice bulletin", "committee opinion"])
            results.append({
                "pmid": pmid,
                "title": title[:200],
                "year": year,
                "journal": journal,
                "first_author": first_author,
                "is_guideline_pt": is_guideline,
                "has_guideline_word": has_guideline_word,
                "article_types": article_types,
            })
        except Exception:
            continue
    return {"pmids": pmids, "results": results}


def is_likely_same_guideline(new_paper, current, name, society):
    """Filter: is this likely the same guideline (updated version) or unrelated?"""
    if not new_paper.get("has_guideline_word"):
        return False
    title_lower = new_paper["title"].lower()
    name_words = name.replace("_", " ").lower().split()

    # Check name keywords appear in title (loose match)
    matches = sum(1 for w in name_words if w in title_lower and len(w) > 3)
    if matches < 2 and society not in title_lower:
        return False
    return True


def check_guideline(name, g):
    """Check 1 guideline: search latest, compare with current."""
    current = g.get("current", {})
    current_pmid = current.get("pmid", "")
    current_year = ""
    if "year_published" in current:
        m = re.search(r"(\d{4})", current["year_published"])
        if m:
            current_year = m.group(1)
    society = detect_society(name, g)

    # Skip if no year (no baseline to compare)
    if not current_year:
        return {
            "name": name,
            "current_pmid": current_pmid,
            "current_year": current_year,
            "society": society,
            "status": "SKIP_NO_YEAR",
            "new_papers_found": [],
        }

    # Search 3 variants
    name_clean = name.replace("_", " ")
    queries = [
        f'"{name_clean}" guideline[pt] AND {int(current_year)+1}:3000[dp]',
        f'{society} "{name_clean}"[ti] AND (guideline OR recommendation)',
    ]
    findings = []
    for q in queries:
        result = search_pubmed(q, max_results=5, year_from=int(current_year) + 1)
        if "results" in result:
            for r in result["results"]:
                if r["pmid"] != current_pmid and is_likely_same_guideline(r, current, name, society):
                    findings.append(r)
        if len(findings) >= 3:
            break

    status = "OK"
    if findings:
        status = "POTENTIAL_UPDATE"

    return {
        "name": name,
        "current_pmid": current_pmid,
        "current_year": current_year,
        "society": society,
        "status": status,
        "new_papers_found": findings[:3],
    }


def main():
    if not REGISTRY_PATH.exists():
        print(f"[ERROR] Registry not found: {REGISTRY_PATH}")
        sys.exit(1)

    with open(REGISTRY_PATH, encoding="utf-8") as f:
        registry = json.load(f)

    guidelines = registry.get("guidelines", {})
    print(f"[INFO] Checking {len(guidelines)} guidelines from registry...")

    results = []
    for name, g in guidelines.items():
        if "current" not in g:
            continue
        print(f"  Checking {name}...")
        result = check_guideline(name, g)
        results.append(result)

    log = {
        "timestamp": datetime.now(TZ_VN).isoformat(),
        "checked": len(results),
        "potential_updates": [r for r in results if r["status"] == "POTENTIAL_UPDATE"],
        "results": results,
    }
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2, ensure_ascii=False)

    updates = log["potential_updates"]
    skipped = [r for r in results if r["status"] == "SKIP_NO_YEAR"]
    ok = [r for r in results if r["status"] == "OK"]
    print(f"\n[SUMMARY] Checked {len(results)} guidelines.")
    print(f"  - OK: {len(ok)}")
    print(f"  - POTENTIAL_UPDATE: {len(updates)}")
    print(f"  - SKIPPED (no year baseline): {len(skipped)}")

    if updates:
        print(f"\n[ACTION NEEDED] {len(updates)} guideline(s) may have updates:")
        for u in updates:
            print(f"\n  {u['name']} (Society: {u['society']}):")
            print(f"    Current: PMID {u['current_pmid']} ({u['current_year']})")
            for p in u["new_papers_found"]:
                print(f"    New: PMID {p['pmid']} - {p['title']}")
                print(f"           {p['first_author']} et al, {p['journal']} ({p['year']})")

    print(f"\n[LOG SAVED] {LOG_PATH}")


if __name__ == "__main__":
    main()
