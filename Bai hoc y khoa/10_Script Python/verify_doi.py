"""verify_doi.py — Verify DOI citations via Crossref API.

Usage:
    python verify_doi.py <lesson.md>
    python verify_doi.py <lesson.md> --json
    python verify_doi.py <lesson.md> --strict

Exit codes:
    0 = All DOIs verified OK
    1 = WARN — some DOIs could not be verified (network issue)
    2 = BLOCK — DOI doesn't exist or retracted → MUST FIX before publishing

Đây là script TÙY CHỌN trong pipeline. Chỉ chạy khi bài có citation
không có PMID (DOI-only). Crossref lấp gap:
- Guideline/doc không có PMID → resolve DOI lấy title + journal
- DOI không có PMID → verify paper tồn tại thật, journal gì, tier mấy
- Retraction check bổ sung (title-based, không toàn diện như PubMed)
"""
import sys
import re
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
JOURNAL_Q_FILE = SCRIPT_DIR / "journal_quartile.json"

CROSSREF_DELAY = 0.2
VALID_TYPES = {
    "journal-article", "proceedings-article", "book-chapter", "book",
    "report", "standard", "dataset", "dissertation", "reference-entry",
    "posted-content", "peer-review",
}


def load_journal_table():
    with open(JOURNAL_Q_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def build_journal_map(jt):
    jmap = {}
    for q_key in ["Q1", "Q2", "Q3", "Q4_AVOID"]:
        for jname, info in jt.get(q_key, {}).items():
            if isinstance(info, dict):
                tier = {"Q1": 1, "Q2": 2, "Q3": 3, "Q4_AVOID": 4}[q_key]
                jmap[jname] = {"quartile": q_key, "tier": tier, **info}
    return jmap


def resolve_journal(name, jmap, aliases):
    if not name:
        return None, "No journal name in Crossref response"

    if name in jmap:
        e = jmap[name]
        return e, f"{e['quartile']} — direct match"

    for alias_key, alias_val in aliases.items():
        if name.lower() == alias_key.lower() or name == alias_val:
            target = aliases.get(alias_key, alias_key)
            if target in jmap:
                e = jmap[target]
                return e, f"{e['quartile']} — alias match ({alias_key})"

    # Short-name lookup via ALIASES section (maps short -> full)
    for alias_key, alias_val in aliases.items():
        if alias_val and alias_val.lower() == name.lower() and alias_key in jmap:
            e = jmap[alias_key]
            return e, f"{e['quartile']} — ALIASES reverse match ({alias_key})"

    # Fuzzy: first 10 chars
    for jname in jmap:
        if jname[:10].lower() == name[:10].lower():
            e = jmap[jname]
            return e, f"{e['quartile']} — fuzzy {jname[:10]}..."

    return None, f"Unknown journal: {name}"


def extract_dois(text):
    doi_patterns = [
        r'\b10\.\d{4,}/[^\s\]\)]+',  # standard DOI
        r'https?://doi\.org/(10\.\d{4,}/[^\s\]\)]+)',  # DOI URL
    ]
    dois = set()
    for pat in doi_patterns:
        for m in re.finditer(pat, text):
            raw = m.group(0)
            doi = raw if raw.startswith("10.") else m.group(1)
            doi = doi.rstrip(".],;:'\"")
            dois.add(doi)
    return sorted(dois)


def fetch_crossref(doi, timeout=15):
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "verify-doi/1.0 (bai-hoc-y-khoa; mailto:user@example.com)"
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data, None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, "DOI not found (404)"
        return None, f"HTTP {e.code}: {e.reason}"
    except Exception as e:
        return None, str(e)


def parse_crossref(data):
    msg = data.get("message", {})
    title_list = msg.get("title", [])
    subtitle_list = msg.get("subtitle", [])
    title = title_list[0] if title_list else ""
    if subtitle_list:
        title += " " + subtitle_list[0]
    title = title.strip()

    authors = []
    for au in msg.get("author", []):
        family = au.get("family", "")
        given = au.get("given", "")
        if family:
            authors.append(f"{family} {given}".strip())
    authors = authors[:5]

    journal = ""
    container = msg.get("container-title", [])
    if container:
        journal = container[0]

    year = ""
    published = msg.get("published-print") or msg.get("published-online") or {}
    date_parts = published.get("date-parts", [[None]])
    if date_parts and date_parts[0] and date_parts[0][0]:
        year = str(date_parts[0][0])

    doi = msg.get("DOI", "")
    cr_type = msg.get("type", "")
    publisher = msg.get("publisher", "")
    issn = (msg.get("ISSN") or [None])[0] if isinstance(msg.get("ISSN"), list) else msg.get("ISSN", "")

    # Retraction signals
    is_retraction = False
    if cr_type == "retraction":
        is_retraction = True
    if "retraction" in title.lower() or "retracted" in title.lower():
        is_retraction = True

    return {
        "doi": doi,
        "title": title,
        "authors": authors,
        "journal": journal,
        "year": year,
        "type": cr_type,
        "publisher": publisher,
        "issn": issn,
        "is_retraction": is_retraction,
    }


def verify_doi(doi, jmap, aliases):
    data, err = fetch_crossref(doi)
    if err:
        return {
            "doi": doi, "status": "ERROR", "error": err,
            "tier": None, "severity": "warn",
            "verdict": f"Fetch error: {err}",
        }

    info = parse_crossref(data)
    entry = {
        "doi": doi, "status": "OK",
        "info": info,
        "tier": None, "severity": "pass",
        "verdict": "OK",
    }

    if info["is_retraction"]:
        entry["tier"] = 4
        entry["severity"] = "block"
        entry["verdict"] = "RETRACTED — this is a retraction notice"
        return entry

    journal_entry, reason = resolve_journal(info["journal"], jmap, aliases)
    if journal_entry:
        entry["tier"] = journal_entry["tier"]
        entry["tier_reason"] = reason
        entry["details"] = {
            "journal": info["journal"],
            "quartile": journal_entry["quartile"],
            "if": journal_entry.get("if", "NA"),
        }
        if journal_entry["tier"] == 4:
            entry["severity"] = "block"
            entry["verdict"] = "BLOCK (Q4_AVOID journal)"
        else:
            entry["verdict"] = f"OK (Tier {journal_entry['tier']}, {journal_entry['quartile']})"
    else:
        entry["tier"] = 3
        entry["tier_reason"] = reason
        entry["details"] = {"journal": info["journal"], "quartile": "UNKNOWN", "if": "NA"}
        entry["severity"] = "warn"
        entry["verdict"] = "WARN (Unknown journal — default Tier 3)"

    return entry


def verify_file(file_path):
    text = Path(file_path).read_text(encoding="utf-8", errors="replace")
    dois = extract_dois(text)

    if not dois:
        return {"file": str(file_path), "summary": {"total": 0, "pass": 0, "warn": 0, "block": 0}, "entries": []}

    jt = load_journal_table()
    jmap = build_journal_map(jt)
    aliases = {}
    # Merge ALIASES section (short -> full) with "aliases" section (short -> full)
    if "ALIASES" in jt:
        aliases.update(jt["ALIASES"])
    if "aliases" in jt:
        aliases.update(jt["aliases"])

    entries = []
    for doi in dois:
        e = verify_doi(doi, jmap, aliases)
        entries.append(e)

    summary = {
        "total": len(entries),
        "pass": sum(1 for e in entries if e["severity"] == "pass"),
        "warn": sum(1 for e in entries if e["severity"] == "warn"),
        "block": sum(1 for e in entries if e["severity"] == "block"),
    }

    return {"file": str(file_path), "summary": summary, "entries": entries}


def print_console(result):
    s = result["summary"]
    print()
    print("=" * 80)
    print(f"  CROSSREF DOI VERIFICATION: {result['file']}")
    print("=" * 80)
    print()
    print(f"  Total: {s['total']}  |  Pass: {s['pass']}  |  Warn: {s['warn']}  |  BLOCK: {s['block']}")
    print()

    if not result["entries"]:
        print("  (khong co DOI nao de verify)")
        return

    for i, e in enumerate(result["entries"], 1):
        icon = {"pass": chr(0x2713), "warn": "!", "block": "X"}.get(e["severity"], "?")
        print(f"  [{icon}] #{i}  {e['verdict']}")
        print(f"      DOI: {e['doi']}")
        if "info" in e:
            info = e["info"]
            print(f"      Title: {info.get('title', '')[:120]}")
            author_str = ", ".join(info.get("authors", [])[:3])
            print(f"      Authors: {author_str}")
            print(f"      Journal: {info.get('journal', '?')} ({info.get('year', '?')})")
            print(f"      Type: {info.get('type', '?')}  |  Publisher: {info.get('publisher', '?')}")
        if e.get("tier_reason"):
            print(f"      Tier: {e['tier']} — {e['tier_reason']}")
        print()


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Verify DOI citations via Crossref API")
    ap.add_argument("file", help="Path to MD file")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    ap.add_argument("--strict", action="store_true", help="Fail on warnings too")
    args = ap.parse_args()

    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"File not found: {args.file}")
        sys.exit(3)

    print(f"[verify_doi] Checking DOIs in {args.file}...")

    result = verify_file(str(file_path))

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_console(result)

    s = result["summary"]
    if s["block"] > 0:
        print(f"  [X] {s['block']} DOI(s) BLOCKED — fix or remove before publishing")
        sys.exit(2)
    elif s["warn"] > 0 and args.strict:
        print(f"  [!] STRICT MODE: {s['warn']} DOI(s) have warnings")
        sys.exit(1)
    elif s["total"] > 0:
        print(f"  [OK] All {s['total']} DOI(s) verified")
        sys.exit(0)
    else:
        print(f"  [OK] No DOIs found — nothing to verify")
        sys.exit(0)


if __name__ == "__main__":
    main()
