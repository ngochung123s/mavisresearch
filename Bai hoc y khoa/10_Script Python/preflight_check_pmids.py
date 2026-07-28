"""preflight_check_pmids.py — Kiểm tra tất cả PMID trong plan/brief TRƯỚC KHI viết MD.

Dùng: python preflight_check_pmids.py <plan_file.md|brief_file.md> [--strict]

Logic:
- Trích xuất mọi PMID từ file (pattern: PMID[: ]*XXXXXXXX)
- Gọi verify_all_pmids để kiểm tra từng PMID có tồn tại không
- Báo cáo: OK (tồn tại) / BLOCK (không tồn tại hoặc sai ngành)
- Exit 0 nếu tất cả OK, exit 2 nếu có BLOCK
"""

import re
import sys
import subprocess
import json
import argparse
from pathlib import Path

PMID_LABELED = re.compile(r'PMID[: ]*\**(\d{7,8})\**')
# Match bare 7-8 digit numbers in markdown table cells (col 2 typically: | 1 | 35120736 | ...)
PMID_TABLE = re.compile(r'\|\s*(?:[A-Za-z0-9_-]+\s*\|\s*.*?\s*\|\s*)?(\d{7,8})\s*\|')


CLAIM_CACHE = Path(__file__).with_name("claim_cache")


def cached_pmid(pmid: str) -> dict | None:
    """Return local verified metadata only when the cache row is internally valid."""
    try:
        metadata = json.loads((CLAIM_CACHE / f"{pmid}.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if metadata.get("pmid") != pmid or metadata.get("status") != "ok":
        return None
    return {
        "pmid": pmid,
        "status": "OK",
        "title": metadata.get("title", "???"),
        "year": metadata.get("year", "????"),
        "source": metadata.get("journal", "local cache"),
        "cached": True,
    }


def extract_pmids(text: str) -> list[str]:
    """Trích xuất tất cả PMID duy nhất từ văn bản (cả format PMID: X và table)."""
    labeled = PMID_LABELED.findall(text)
    table = PMID_TABLE.findall(text)
    all_pmids = labeled + table
    # Deduplicate while preserving order
    seen = set()
    result = []
    for p in all_pmids:
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result


def check_pmid(pmid: str, timeout: int = 15) -> dict:
    """Kiểm tra 1 PMID qua NCBI E-utilities efetch."""
    import urllib.request
    import urllib.error

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            data = json.loads(resp.read())
        result = data.get("result", {})
        uids = result.get("uids", [])
        if pmid in uids:
            article = result.get(pmid, {})
            title = article.get("title", "???")
            year = article.get("pubdate", "????")[:4]
            source = article.get("source", "???")
            return {
                "pmid": pmid,
                "status": "OK",
                "title": title,
                "year": year,
                "source": source,
            }
        else:
            return {
                "pmid": pmid,
                "status": "BLOCK",
                "reason": "PMID not found in PubMed",
            }
    except urllib.error.HTTPError as error:
        if error.code == 429 or 500 <= error.code < 600:
            cached = cached_pmid(pmid)
            if cached:
                return cached
        return {
            "pmid": pmid,
            "status": "BLOCK",
            "reason": f"HTTP {error.code}",
        }
    except (urllib.error.URLError, TimeoutError) as error:
        return {
            "pmid": pmid,
            "status": "BLOCK",
            "reason": str(error)[:100],
        }
    except Exception as error:
        return {
            "pmid": pmid,
            "status": "BLOCK",
            "reason": str(error)[:100],
        }


def main():
    parser = argparse.ArgumentParser(
        description="Pre-flight PMID checker — kiểm tra PMIDs trước khi viết bài"
    )
    parser.add_argument("plan_file", help="File plan hoặc brief chứa PMIDs cần kiểm tra")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Strict mode: BLOCK nếu PMID không tồn tại",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON output",
    )
    args = parser.parse_args()

    plan_path = Path(args.plan_file)
    if not plan_path.exists():
        print(f"❌ File không tồn tại: {plan_path}", file=sys.stderr)
        sys.exit(1)

    text = plan_path.read_text(encoding="utf-8")
    pmids = extract_pmids(text)

    if not pmids:
        message = "Không tìm thấy PMID nào trong file. Strict preflight requires at least one PMID."
        if args.json:
            print(json.dumps({"summary": {"ok": 0, "block": int(args.strict)}, "results": [], "error": message}, ensure_ascii=False, indent=2))
        else:
            print(f"🛑 {message}" if args.strict else f"⚠️  {message}", file=sys.stderr)
        sys.exit(2 if args.strict else 0)

    if not args.json:
        print(f"\n🔍 [preflight] Kiểm tra {len(pmids)} PMIDs trong {plan_path.name}...\n")

    results = []
    ok_count = 0
    block_count = 0

    for pmid in pmids:
        result = check_pmid(pmid)
        results.append(result)
        if result["status"] == "OK":
            ok_count += 1
            if not args.json:
                print(f"  ✅ PMID {pmid}: {result['title'][:80]} ({result['source']}, {result['year']})")
        else:
            block_count += 1
            if not args.json:
                print(f"  🛑 PMID {pmid}: {result.get('reason', 'FAILED')}")

    if not args.json:
        print(f"\n  Kết quả: {ok_count} OK, 0 WARN, {block_count} BLOCK")
        if block_count > 0:
            print(f"\n  🛑 {block_count} PMID KHÔNG TỒN TẠI! Sửa plan trước khi bắt đầu research.")
            print(f"     Đây là các PMID cần sửa. Không tiếp tục cho đến khi tất cả OK.")
        else:
            print(f"\n  ✅ Tất cả {ok_count} PMIDs tồn tại — an toàn để bắt đầu research!")

    if args.json:
        print(json.dumps({"summary": {"ok": ok_count, "block": block_count}, "results": results}, ensure_ascii=False, indent=2))

    if block_count > 0 and args.strict:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
