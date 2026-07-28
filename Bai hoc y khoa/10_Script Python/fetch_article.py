#!/usr/bin/env python3
"""
Fetch PubMed article details via NCBI E-utilities (efetch XML + esummary JSON).
Replaces broken `biomcp get article` — no PubTator3 or Semantic Scholar dependency.

Usage:
  python fetch_article.py --pmid 30103263                           # full metadata JSON
  python fetch_article.py --pmid 30103263 --abstract                # structured abstract
  python fetch_article.py --pmid 30103263 --tldr                    # one-line summary
  python fetch_article.py --pmid 30103263,30103264 --cited-by --tldr # TLDR + citation counts
  python fetch_article.py --pmid 30103263,30103264 --cited-by        # citation counts only
  python fetch_article.py --pmid 30103263,30103264 --output out.json # batch to file
  python fetch_article.py --pmid 30103263 --fulltext                 # PMC fulltext (if OA)
  python fetch_article.py --pmid 30103263 --citations --limit 10 --tldr  # citing articles
  python fetch_article.py --pmid 30103263 --references --limit 10 --tldr # references
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# ── config ──────────────────────────────────────────────────────────
EMAIL = "thanh-anh.researcher@example.com"
API_KEY = ""  # efetch works without key at 3 req/s; add key for 10 req/s
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
REQUEST_DELAY = 0.4  # seconds between requests (safe for no-key: 3/sec)

# ── helpers ──────────────────────────────────────────────────────────

def _ncbi_url(endpoint, params):
    """Build NCBI E-utilities URL with email (and API key if set)."""
    p = dict(params)
    p.setdefault("email", EMAIL)
    p.setdefault("tool", "mavis_fetch_article")
    if API_KEY:
        p["api_key"] = API_KEY
    return f"{BASE}/{endpoint}?" + urllib.parse.urlencode(p)


def _get(url, timeout=30):
    """GET with retry on transient errors."""
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


# ── esummary (fast metadata) ─────────────────────────────────────────

def _esummary(pmids):
    """Fetch article metadata via esummary JSON. Returns {pmid: {...}}."""
    url = _ncbi_url("esummary.fcgi", {
        "db": "pubmed",
        "id": ",".join(str(p) for p in pmids),
        "retmode": "json",
        "retmax": len(pmids),
    })
    data = json.loads(_get(url))
    return data.get("result", {})


# ── efetch XML (structured abstract) ─────────────────────────────────

def _efetch_xml(pmids):
    """Fetch full XML via efetch. Returns root Element."""
    url = _ncbi_url("efetch.fcgi", {
        "db": "pubmed",
        "id": ",".join(str(p) for p in pmids),
        "retmode": "xml",
        "retmax": len(pmids),
    })
    return ET.fromstring(_get(url))


def _parse_abstract_text(article_elem):
    """Extract structured abstract sections from efetch XML article element."""
    sections = {}
    abstract_elem = article_elem.find(".//Abstract")
    if abstract_elem is None:
        return sections

    for child in abstract_elem:
        label = child.get("Label", "").strip().rstrip(":")
        text = "".join(child.itertext()).strip()
        if label:
            sections[label] = text
        else:
            sections.setdefault("TEXT", "")
            sections["TEXT"] += text + "\n"

    if "TEXT" in sections:
        sections["TEXT"] = sections["TEXT"].strip()
    return sections


def _parse_article(article_elem):
    """Parse a PubmedArticle XML element into structured dict."""
    medline = article_elem.find(".//MedlineCitation")
    if medline is None:
        return None

    art = medline.find("Article")
    if art is None:
        return None

    pmid_elem = medline.find("PMID")
    pmid = pmid_elem.text if pmid_elem is not None else "???"

    title_elem = art.find("ArticleTitle")
    title = "".join(title_elem.itertext()) if title_elem is not None else ""

    journal_elem = art.find("Journal")
    journal_title = ""
    journal_iso = ""
    pub_year = ""
    if journal_elem is not None:
        jt = journal_elem.find("Title")
        ji = journal_elem.find("ISOAbbreviation")
        ji2 = journal_elem.find(".//JournalIssue/PubDate/Year")
        journal_title = jt.text if jt is not None else ""
        journal_iso = ji.text if ji is not None else ""
        pub_year = ji2.text if ji2 is not None else ""

    author_list = art.find("AuthorList")
    authors = []
    if author_list is not None:
        for auth in author_list.findall("Author"):
            ln = auth.find("LastName")
            fn = auth.find("ForeName")
            if ln is not None:
                name = ln.text
                if fn is not None:
                    name = f"{ln.text} {fn.text}"
                authors.append(name)

    first_author = authors[0] if authors else ""
    last_author = authors[-1] if len(authors) > 1 else ""

    pub_types = []
    pt_list = art.find("PublicationTypeList")
    if pt_list is not None:
        for pt in pt_list.findall("PublicationType"):
            if pt.text and pt.text.strip():
                pub_types.append(pt.text.strip())

    doi = ""
    for eid in art.findall("ELocationID"):
        if eid.get("EIdType") == "doi":
            doi = (eid.text or "").strip()
            break

    pmcid = ""
    pid_list = article_elem.find(".//PubmedData/ArticleIdList")
    if pid_list is not None:
        for aid in pid_list.findall("ArticleId"):
            if aid.get("IdType") == "pmc":
                pmcid = (aid.text or "").strip()
                break

    abstract_sections = _parse_abstract_text(art)

    abstract_plain = ""
    if abstract_sections:
        parts = []
        for label, text in abstract_sections.items():
            if label == "TEXT":
                parts.append(text)
            else:
                parts.append(f"{label}: {text}")
        abstract_plain = "\n".join(parts)

    return {
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "title": title,
        "journal": journal_title,
        "journal_iso": journal_iso,
        "year": pub_year,
        "first_author": first_author,
        "last_author": last_author,
        "authors": authors,
        "pub_types": pub_types,
        "abstract": abstract_plain,
        "abstract_sections": abstract_sections,
    }


# ── tldr generator ───────────────────────────────────────────────────

def _make_tldr(article, cited_count=None):
    """Condense article into one-line summary. cited_count adds 'Cit: N' suffix."""
    title = article.get("title", "")[:120]
    first = article.get("first_author", "")
    journal = article.get("journal_iso", article.get("journal", ""))
    year = article.get("year", "")
    pub_types = article.get("pub_types", [])
    abs_text = article.get("abstract", "")

    is_meta = any("Meta-Analysis" in pt for pt in pub_types)
    is_review = any("Review" in pt for pt in pub_types) or any("Systematic Review" in pt for pt in pub_types)
    is_rct = any("Randomized Controlled Trial" in pt for pt in pub_types)
    is_guideline = any("Practice Guideline" in pt for pt in pub_types)

    type_tag = ""
    if is_guideline:
        type_tag = " [GUIDELINE]"
    elif is_meta:
        type_tag = " [META-ANALYSIS]"
    elif is_review:
        type_tag = " [REVIEW]"
    elif is_rct:
        type_tag = " [RCT]"

    pmid = article.get("pmid", "")
    cite_suffix = f" [Cit: {cited_count}]" if cited_count is not None else ""

    gist = ""
    if abs_text:
        first_sent = re.split(r'(?<=[.!?])\s+', abs_text[:300])[0]
        gist = first_sent[:200].strip()

    return f"[{pmid}] {first} et al., {journal} {year} | {title[:100]}{type_tag}{cite_suffix} | {gist}"


# ── elink (citations / references) ───────────────────────────────────

def _elink(pmid, linkname, limit=10):
    """Fetch linked PMIDs via elink."""
    url = _ncbi_url("elink.fcgi", {
        "dbfrom": "pubmed",
        "db": "pubmed",
        "id": pmid,
        "linkname": linkname,
        "retmode": "json",
    })
    data = json.loads(_get(url))
    linksets = data.get("linksets", [])
    if not linksets:
        return []
    ids = []
    for ls in linksets:
        for link in ls.get("linksetdbs", []):
            if link.get("linkname") == linkname:
                ids.extend(link.get("links", []))
    return ids[:limit]


# ── cited-by count ───────────────────────────────────────────────────

def _cited_by_count(pmid):
    """Get citation count for a PMID via NCBI elink. Returns int."""
    url = _ncbi_url("elink.fcgi", {
        "dbfrom": "pubmed",
        "db": "pubmed",
        "id": pmid,
        "linkname": "pubmed_pubmed_citedin",
        "retmode": "json",
    })
    data = json.loads(_get(url))
    linksets = data.get("linksets", [])
    if not linksets:
        return 0
    for ls in linksets:
        for link in ls.get("linksetdbs", []):
            if link.get("linkname") == "pubmed_pubmed_citedin":
                return len(link.get("links", []))
    return 0


def _cited_by_batch(pmids):
    """Get citation counts for multiple PMIDs (parallel). Returns {pmid: count}."""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    results = {}
    with ThreadPoolExecutor(max_workers=min(len(pmids), 5)) as ex:
        futures = {ex.submit(_cited_by_count, p): p for p in pmids}
        for future in as_completed(futures):
            pmid = futures[future]
            try:
                results[pmid] = future.result()
            except Exception:
                results[pmid] = 0
    return results


# ── PMC fulltext ─────────────────────────────────────────────────────

def _pmc_fulltext(pmcid):
    """Fetch PMC OA fulltext as plain text."""
    url = _ncbi_url("efetch.fcgi", {
        "db": "pmc",
        "id": pmcid,
        "retmode": "xml",
    })
    xml_bytes = _get(url, timeout=60)
    root = ET.fromstring(xml_bytes)
    texts = []
    for p in root.iter("p"):
        t = "".join(p.itertext()).strip()
        if t:
            texts.append(t)
    return "\n\n".join(texts)


# ── main CLI ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed articles via NCBI E-utilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--pmid", required=True,
                        help="PubMed ID(s), comma-separated (max 50)")
    parser.add_argument("--abstract", action="store_true",
                        help="Include structured abstract sections")
    parser.add_argument("--tldr", action="store_true",
                        help="One-line summary per article")
    parser.add_argument("--table", action="store_true",
                        help="Output as Markdown table (for scanning)")
    parser.add_argument("--cited-by", action="store_true",
                        help="Show citation counts for PMID(s)")
    parser.add_argument("--fulltext", action="store_true",
                        help="Attempt to fetch PMC OA fulltext")
    parser.add_argument("--citations", action="store_true",
                        help="Find articles that cite this PMID")
    parser.add_argument("--references", action="store_true",
                        help="Find articles this PMID cites")
    parser.add_argument("--limit", type=int, default=10,
                        help="Max results for citations/references (default 10)")
    parser.add_argument("--output", "-o",
                        help="Write JSON to file instead of stdout")
    parser.add_argument("--json", action="store_true",
                        help="Force JSON output (default for single PMID)")
    args = parser.parse_args()

    pmids = [p.strip() for p in args.pmid.split(",") if p.strip()]
    if not pmids:
        print("ERROR: no valid PMIDs", file=sys.stderr)
        sys.exit(1)
    if len(pmids) > 50:
        print("ERROR: max 50 PMIDs per call", file=sys.stderr)
        sys.exit(1)

    # ── citations / references mode ──
    if args.citations or args.references:
        pmid = pmids[0]
        linkname = "pubmed_pubmed_citedin" if args.citations else "pubmed_pubmed_refs"
        label = "Citing articles" if args.citations else "References"

        ids = _elink(pmid, linkname, limit=args.limit)
        if not ids:
            print(f"# {label} for PMID {pmid}: 0 found")
            return

        time.sleep(REQUEST_DELAY)
        articles = [_parse_article(a) for a in _efetch_xml(ids).findall(".//PubmedArticle")]
        articles = [a for a in articles if a is not None]

        print(f"# {label} for PMID {pmid}: {len(articles)} found")
        print()
        if args.tldr:
            for a in articles:
                print(_make_tldr(a))
        elif args.table:
            print("| PMID | First Author | Year | Journal | Title |")
            print("|---|---|---|---|---|")
            for a in articles:
                print(f"| {a['pmid']} | {a['first_author']} | {a['year']} | {a['journal_iso'] or a['journal']} | {a['title'][:100]} |")
        else:
            out = {a["pmid"]: {k: v for k, v in a.items() if k != "abstract_sections"} for a in articles}
            if args.output:
                Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"Saved to {args.output}")
            else:
                print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    # ── cited-by mode ──
    if args.cited_by:
        counts = _cited_by_batch(pmids)
        print(f"# Citation counts for {len(pmids)} PMID(s)")
        print()

        need_details = args.tldr or args.table
        if need_details:
            root = _efetch_xml(pmids)
            articles = []
            for pubmed_article in root.findall(".//PubmedArticle"):
                a = _parse_article(pubmed_article)
                if a:
                    articles.append(a)

        if args.tldr:
            for a in (articles if need_details else []):
                cnt = counts.get(a["pmid"], 0)
                print(_make_tldr(a, cited_count=cnt))
        elif args.table:
            print("| PMID | First Author | Year | Journal | Type | Cit. | Title |")
            print("|---|---|---|---|---|---|---|")
            for a in (articles if need_details else []):
                cnt = counts.get(a["pmid"], 0)
                pts = a.get("pub_types", [])
                ptype = pts[0] if pts else ""
                print(f"| {a['pmid']} | {a['first_author']} | {a['year']} | {a['journal_iso'] or a['journal']} | {ptype} | {cnt} | {a['title'][:100]} |")
        else:
            for pmid in pmids:
                cnt = counts.get(pmid, 0)
                print(f"[{pmid}] {cnt} citation(s)")
        return

    # ── article detail mode ──
    root = _efetch_xml(pmids)
    articles = []
    for pubmed_article in root.findall(".//PubmedArticle"):
        a = _parse_article(pubmed_article)
        if a:
            articles.append(a)

    if not articles:
        print("ERROR: no articles found", file=sys.stderr)
        sys.exit(1)

    # ── fulltext mode ──
    if args.fulltext:
        for a in articles:
            pmcid = a.get("pmcid", "")
            if not pmcid:
                print(f"[{a['pmid']}] No PMCID — fulltext not available", file=sys.stderr)
                continue
            try:
                text = _pmc_fulltext(pmcid)
                out_path = f"PMC{pmcid}_fulltext.txt"
                Path(out_path).write_text(text, encoding="utf-8")
                print(f"[{a['pmid']}] Fulltext saved to {out_path} ({len(text)} chars)")
            except Exception as e:
                print(f"[{a['pmid']}] Fulltext fetch failed: {e}", file=sys.stderr)
        return

    # ── output ──
    if args.tldr:
        for a in articles:
            print(_make_tldr(a))
        return

    if args.table:
        print("| PMID | First Author | Year | Journal | Type | Title |")
        print("|---|---|---|---|---|---|")
        for a in articles:
            pts = a.get("pub_types", [])
            ptype = pts[0] if pts else ""
            print(f"| {a['pmid']} | {a['first_author']} | {a['year']} | {a['journal_iso'] or a['journal']} | {ptype} | {a['title'][:100]} |")
        return

    # JSON output
    out = {}
    for a in articles:
        entry = {
            "pmid": a["pmid"],
            "pmcid": a["pmcid"],
            "doi": a["doi"],
            "title": a["title"],
            "journal": a["journal"],
            "journal_iso": a["journal_iso"],
            "year": a["year"],
            "first_author": a["first_author"],
            "last_author": a["last_author"],
            "authors": a["authors"],
            "pub_types": a["pub_types"],
            "abstract": a["abstract"],
        }
        if args.abstract:
            entry["abstract_sections"] = a["abstract_sections"]
        out[a["pmid"]] = entry

    if args.output:
        Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Saved to {args.output}")
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
