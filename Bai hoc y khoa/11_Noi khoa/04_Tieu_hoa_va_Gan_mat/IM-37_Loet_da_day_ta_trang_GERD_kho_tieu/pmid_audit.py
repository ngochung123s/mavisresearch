#!/usr/bin/env python3
"""
pmid_audit.py — Gate-based PMID Verification Audit Script
===========================================================
Quét tất cả file .md trong thư mục bài học, trích xuất PMID claims,
gọi NCBI API kiểm tra tồn tại + lấy abstract, so sánh claim vs abstract,
xuất báo cáo audit_report.md.

Usage: python pmid_audit.py <folder_path>
Output: <folder_path>/audit_report.md + <folder_path>/audit_artifacts/*.json
"""

import os, sys, re, json, urllib.request, urllib.parse, time, glob
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ─── NCBI API helpers ───────────────────────────────────────────────
NCBI_HEADERS = {'User-Agent': 'PMID-Audit-Script/1.0 (medical-education)'}

def ncbi_api(url, retries=3, delay=0.5):
    """Call NCBI API with retry logic."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=NCBI_HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay * (attempt + 1))
            else:
                return {"error": str(e)}

def fetch_summary(pmid):
    """Gate 0: Fetch metadata from NCBI E-summary."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    data = ncbi_api(url)
    if "error" in data:
        return {"pmid": pmid, "exists": False, "error": data["error"]}
    res = data.get('result', {}).get(str(pmid), {})
    if not res or not res.get('title'):
        return {"pmid": pmid, "exists": False, "error": "No result from NCBI"}
    return {
        "pmid": pmid,
        "exists": True,
        "title": res.get('title', ''),
        "journal": res.get('source', ''),
        "pubdate": res.get('pubdate', ''),
        "pubtype": [pt for pt in res.get('pubtype', [])],
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    }

def fetch_abstract(pmid):
    """Gate 1: Fetch abstract from NCBI E-fetch."""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml&rettype=abstract"
    req = urllib.request.Request(url, headers=NCBI_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml = resp.read().decode('utf-8')
            # Extract AbstractText
            abs_match = re.findall(r'<AbstractText[^>]*>(.*?)</AbstractText>', xml, re.DOTALL)
            if abs_match:
                abstract = ' '.join(abs_match)
            else:
                # Try older format
                abs_match2 = re.findall(r'<Abstract>(.*?)</Abstract>', xml, re.DOTALL)
                abstract = ' '.join(abs_match2) if abs_match2 else ""
            return abstract.strip()
    except Exception as e:
        return f"[FETCH ERROR: {e}]"

# ─── Claim extraction ───────────────────────────────────────────────
def extract_claims_from_file(filepath):
    """Trích xuất tất cả PMID claims từ file .md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    claims = []
    # Pattern: match PMID: NNNNNNN [OPTIONAL TAG]
    pmid_pattern = re.compile(r'PMID:\s*(\d+)')
    tag_pattern = re.compile(r'\[(FULL VERIFIED|ABSTRACT VERIFIED|GUIDELINE VERIFIED|FETCHED|DATA VERIFIED|FULL TEXT VERIFIED|REVIEW VERIFIED|META-ANALYSIS VERIFIED)\]')

    for idx, line in enumerate(lines):
        pmid_matches = pmid_pattern.findall(line)
        for pmid in pmid_matches:
            tag_match = tag_pattern.search(line)
            tag = tag_match.group(1) if tag_match else "NO_TAG"
            # Clean line text
            clean_line = line.strip()
            if len(clean_line) > 500:
                clean_line = clean_line[:497] + "..."
            claims.append({
                "file": Path(filepath).name,
                "relpath": str(Path(filepath)),
                "line_num": idx + 1,
                "line_text": clean_line,
                "pmid": pmid,
                "current_tag": tag
            })

    return claims

# ─── Claim type detection ───────────────────────────────────────────
def detect_claim_type(claim_text):
    """Phân loại claim: numeric (có con số) vs factual (định tính) vs guideline (khuyến cáo)."""
    has_numbers = bool(re.search(r'\b\d+[\.,]?\d*\s*(%|mg|g|mmHg|lần|tuần|ngày|năm|tháng|tuổi|n\s*[=≈]|RR|OR|CI|HR|p\s*[<>=])', claim_text, re.IGNORECASE))
    has_guideline_marker = bool(re.search(r'(guideline|khuyến cáo|consensus|đồng thuận|hướng dẫn|ACG|AGA|VNAGE|Maastricht|Rome|Kyoto)', claim_text, re.IGNORECASE))
    has_rr = bool(re.search(r'\bRR\b|\bOR\b|\bHR\b|\bCI\b|nguy cơ tương đối', claim_text, re.IGNORECASE))

    if has_rr:
        return "numeric_rr"
    if has_numbers:
        return "numeric"
    if has_guideline_marker:
        return "guideline"
    return "factual"

# ─── Abstract-claim matching ────────────────────────────────────────
def match_claim_to_abstract(claim_text, abstract, claim_type):
    """So sánh claim với abstract để xác định mức khớp."""
    if not abstract or "[FETCH ERROR" in abstract:
        return {"match": "unknown", "reason": "Abstract not available", "snippet": ""}

    # Tokenize keywords from claim
    claim_lower = claim_text.lower()
    abstract_lower = abstract.lower()

    # Extract key phrases from claim (after removing punctuation)
    keywords = re.findall(r'[a-zA-Zà-ỹÀ-Ỹ]{4,}', claim_lower)
    keyword_count = sum(1 for kw in keywords if kw in abstract_lower)
    keyword_ratio = keyword_count / max(len(keywords), 1)

    # For numeric claims: check if the same numbers appear
    if claim_type in ("numeric", "numeric_rr"):
        numbers_in_claim = set(re.findall(r'\d+[\.,]?\d*', claim_text))
        numbers_in_abstract = set(re.findall(r'\d+[\.,]?\d*', abstract))
        number_overlap = len(numbers_in_claim & numbers_in_abstract) / max(len(numbers_in_claim), 1)

        if number_overlap >= 0.5 and keyword_ratio >= 0.4:
            return {"match": True, "reason": f"Number overlap: {number_overlap:.0%}, Keyword overlap: {keyword_ratio:.0%}",
                    "snippet": abstract[:300]}
        elif number_overlap >= 0.3 and keyword_ratio >= 0.3:
            return {"match": "partial", "reason": f"Partial number/keyword match (n:{number_overlap:.0%}, k:{keyword_ratio:.0%})",
                    "snippet": abstract[:300]}
        else:
            return {"match": "weak", "reason": f"Weak match (n:{number_overlap:.0%}, k:{keyword_ratio:.0%}). Cannot confirm numbers.",
                    "snippet": abstract[:300]}

    # For factual/guideline claims
    if keyword_ratio >= 0.5:
        return {"match": True, "reason": f"Keyword overlap: {keyword_ratio:.0%}", "snippet": abstract[:300]}
    elif keyword_ratio >= 0.3:
        return {"match": "partial", "reason": f"Partial keyword match: {keyword_ratio:.0%}", "snippet": abstract[:300]}
    else:
        return {"match": "weak", "reason": f"Weak keyword match: {keyword_ratio:.0%}", "snippet": abstract[:300]}

# ─── Tier assessment ────────────────────────────────────────────────
def assess_tier(claim_type, summary, abstract_match, current_tag):
    """Xác định tier verification thực tế dựa trên evidence."""
    has_pubtype_guideline = any(
        g in str(summary.get('pubtype', [])).lower()
        for g in ['practice guideline', 'consensus statement']
    )

    tier_map = {
        ("numeric", True): ("DATA VERIFIED", True),
        ("numeric", "partial"): ("ABSTRACT VERIFIED", False),
        ("numeric", "weak"): ("FETCHED", False),
        ("numeric_rr", True): ("DATA VERIFIED", True),
        ("numeric_rr", "partial"): ("ABSTRACT VERIFIED", False),
        ("numeric_rr", "weak"): ("FETCHED", False),
        ("guideline", True): ("GUIDELINE VERIFIED" if has_pubtype_guideline else "ABSTRACT VERIFIED", True),
        ("guideline", "partial"): ("ABSTRACT VERIFIED", True),
        ("guideline", "weak"): ("FETCHED", False),
        ("factual", True): ("ABSTRACT VERIFIED", True),
        ("factual", "partial"): ("ABSTRACT VERIFIED", True),
        ("factual", "weak"): ("FETCHED", False),
    }

    match = abstract_match.get("match", "unknown")
    actual_tier, can_keep = tier_map.get((claim_type, match), ("FETCHED", False))
    return actual_tier, can_keep

# ─── Main audit function ────────────────────────────────────────────
def run_audit(folder_path):
    """Chạy audit toàn bộ file .md trong folder."""
    folder = Path(folder_path)
    md_files = list(folder.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {folder_path}")
        return

    print(f"[AUDIT] Found {len(md_files)} .md files in {folder_path}")

    # Step 1: Extract all claims
    all_claims = []
    for f in md_files:
        claims = extract_claims_from_file(str(f))
        all_claims.extend(claims)

    print(f"[AUDIT] Extracted {len(all_claims)} PMID claims")

    # Step 2: Unique PMIDs
    unique_pmids = list(set(c["pmid"] for c in all_claims))
    print(f"[AUDIT] {len(unique_pmids)} unique PMIDs to verify")

    # Step 3: Gate 0 — Fetch summaries
    print("[AUDIT] Gate 0: Fetching NCBI summaries...")
    pmid_summaries = {}
    for i, pmid in enumerate(unique_pmids):
        summary = fetch_summary(pmid)
        pmid_summaries[pmid] = summary
        status = "✅" if summary.get("exists") else "❌"
        print(f"  [{i+1}/{len(unique_pmids)}] PMID {pmid} {status} {summary.get('title', '')[:80]}...")
        time.sleep(0.2)  # Be nice to NCBI

    # Step 4: Gate 1 — Fetch abstracts
    print("\n[AUDIT] Gate 1: Fetching abstracts...")
    pmid_abstracts = {}
    for i, pmid in enumerate(unique_pmids):
        if pmid_summaries[pmid].get("exists"):
            abstract = fetch_abstract(pmid)
            pmid_abstracts[pmid] = abstract
            has_abs = "✅" if abstract and "[FETCH ERROR" not in abstract else "⚠️"
            print(f"  [{i+1}/{len(unique_pmids)}] PMID {pmid} {has_abs} abstract ({len(abstract)} chars)")
            time.sleep(0.3)  # Be nice to NCBI
        else:
            pmid_abstracts[pmid] = "PMID NOT FOUND"

    # Step 5: Gate 2 — Match claims to abstracts
    print("\n[AUDIT] Gate 2: Matching claims to abstracts...")
    results = []
    tier_counts = defaultdict(int)

    for claim in all_claims:
        pmid = claim["pmid"]
        summary = pmid_summaries.get(pmid, {"exists": False, "error": "Not fetched"})
        abstract = pmid_abstracts.get(pmid, "")
        claim_type = detect_claim_type(claim["line_text"])
        match_result = match_claim_to_abstract(claim["line_text"], abstract, claim_type)
        actual_tier, evidence_ok = assess_tier(claim_type, summary, match_result, claim["current_tag"])

        needs_downgrade = False
        tier_order = {"NO_TAG": 0, "FETCHED": 1, "ABSTRACT VERIFIED": 2, "META-ANALYSIS VERIFIED": 2, "REVIEW VERIFIED": 2, "GUIDELINE VERIFIED": 3, "DATA VERIFIED": 3, "FULL VERIFIED": 4, "FULL TEXT VERIFIED": 5}
        current_tier_val = tier_order.get(claim["current_tag"], 0)
        actual_tier_val = tier_order.get(actual_tier, 0)

        if current_tier_val > actual_tier_val:
            needs_downgrade = True
            tier_counts["DOWNGRADE"] += 1
        elif match_result.get("match") == True:
            tier_counts["PASS"] += 1
        elif match_result.get("match") == "partial":
            tier_counts["PARTIAL"] += 1
        else:
            tier_counts["WEAK"] += 1

        if not summary.get("exists"):
            tier_counts["MISSING_PMID"] += 1

        results.append({
            "file": claim["file"],
            "line": claim["line_num"],
            "pmid": pmid,
            "claim_short": claim["line_text"][:150] + ("..." if len(claim["line_text"]) > 150 else ""),
            "claim_type": claim_type,
            "pmid_title": summary.get("title", "NOT FOUND"),
            "pmid_pubtype": summary.get("pubtype", []),
            "current_tag": claim["current_tag"],
            "actual_tier": actual_tier,
            "needs_downgrade": needs_downgrade,
            "abstract_match": match_result.get("match"),
            "match_reason": match_result.get("reason", "")
        })

    # Step 6: Save artifacts
    artifacts_dir = folder / "audit_artifacts"
    artifacts_dir.mkdir(exist_ok=True)

    # Save summaries
    with open(artifacts_dir / "ncbi_fetch.json", "w", encoding="utf-8") as f:
        json.dump(pmid_summaries, f, indent=2, ensure_ascii=False, default=str)

    # Save abstract matches
    with open(artifacts_dir / "abstract_match.jsonl", "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps({
                "pmid": r["pmid"],
                "claim_text": r["claim_short"],
                "abstract_snippet": pmid_abstracts.get(r["pmid"], "")[:500],
                "claim_type": r["claim_type"],
                "match": r["abstract_match"],
                "reason": r["match_reason"]
            }, ensure_ascii=False) + "\n")

    # Step 7: Generate audit report
    report_lines = []
    report_lines.append("# AUDIT REPORT — PMID Verification (Gate-Based Pipeline)")
    report_lines.append(f"**Thư mục:** `{folder_path}`")
    report_lines.append(f"**Thời gian:** {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    report_lines.append(f"**Tổng file:** {len(md_files)} | **Tổng claims:** {len(all_claims)} | **Unique PMIDs:** {len(unique_pmids)}")
    report_lines.append("")
    report_lines.append("## Tổng kết nhanh")
    report_lines.append("")
    report_lines.append("| Kết quả | Số lượng |")
    report_lines.append("|---|---|")
    for k in ["PASS", "PARTIAL", "DOWNGRADE", "WEAK", "MISSING_PMID"]:
        report_lines.append(f"| {k} | {tier_counts.get(k, 0)} |")
    report_lines.append("")

    # Downgrade details
    downgrades = [r for r in results if r["needs_downgrade"]]
    if downgrades:
        report_lines.append("## 🚨 CẦN HẠ NHÃN (DOWNGRADE)")
        report_lines.append("")
        for d in downgrades:
            report_lines.append(f"| {d['file']} | L{d['line']} | PMID {d['pmid']} | `{d['current_tag']}` → `{d['actual_tier']}` | {d['match_reason']} |")

        report_lines.append("")

    # Per-file summary
    report_lines.append("## Chi tiết từng file")
    report_lines.append("")
    files_grouped = defaultdict(list)
    for r in results:
        files_grouped[r["file"]].append(r)

    for fname in sorted(files_grouped.keys()):
        file_results = files_grouped[fname]
        file_downgrades = [r for r in file_results if r["needs_downgrade"]]
        report_lines.append(f"### {fname} ({len(file_results)} claims, {len(file_downgrades)} cần hạ nhãn)")
        report_lines.append("")
        for r in file_results:
            flag = "🔴" if r["needs_downgrade"] else "🟢" if r["abstract_match"] == True else "🟡"
            report_lines.append(f"| {flag} | L{r['line']} | `{r['current_tag']}` | PMID {r['pmid']} | {r['claim_short'][:100]} | → `{r['actual_tier']}` |")
        report_lines.append("")

    report_path = folder / "audit_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(report_lines))

    print(f"\n[AUDIT] Completed! Report: {report_path}")
    print(f"[AUDIT] Artifacts: {artifacts_dir}/")
    print(f"[AUDIT] PASS: {tier_counts.get('PASS', 0)} | PARTIAL: {tier_counts.get('PARTIAL', 0)} | DOWNGRADE: {tier_counts.get('DOWNGRADE', 0)} | MISSING: {tier_counts.get('MISSING_PMID', 0)}")

    return results, pmid_summaries, pmid_abstracts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pmid_audit.py <folder_path>")
        sys.exit(1)
    folder = sys.argv[1]
    run_audit(folder)
