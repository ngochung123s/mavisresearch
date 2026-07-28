#!/usr/bin/env python3
"""Scan tất cả bài học .docx + .md trong project và chạy citation_audit trên từng file.

Output:
- audit_all_lessons_<date>.md - báo cáo tổng hợp (table per-file + list journal Unknown)
- audit_all_lessons_<date>.json - dữ liệu raw để analyze tiếp
- unknown_journals_<date>.txt - list journal cần add vào journal_quartile.json

Usage:
    python scan_all_lessons.py [project_root]
    python scan_all_lessons.py "F:\\DL\\mavisresearch\\Bai hoc y khoa"
"""
import json
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
AUDIT_SCRIPT = SCRIPT_DIR / "citation_audit.py"
DEFAULT_ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
DATE = time.strftime("%Y-%m-%d")


def find_lesson_files(root):
    """Find all .docx and .md files in lessons directories (not in script/source dirs)."""
    files = []
    skip_dirs = {'10_Script Python', '09_Source - Markdown', '07_Visual Summary - HTML', '08_Anki Deck - apkg'}

    for item in root.rglob('*'):
        if not item.is_file():
            continue
        if item.suffix.lower() not in ('.docx', '.md'):
            continue
        # Skip if any parent is in skip_dirs
        if any(skip in item.parts for skip in skip_dirs):
            continue
        files.append(item)
    return sorted(files)


def run_audit(file_path):
    """Run citation_audit.py on a file, return parsed JSON or None on error."""
    args = [sys.executable, str(AUDIT_SCRIPT), str(file_path), "--json", "--quiet"]
    try:
        result = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', timeout=120)
        if result.returncode not in (0, 1):
            print(f"  [WARN] audit failed for {file_path.name}: exit {result.returncode}", file=sys.stderr)
            return None
        return json.loads(result.stdout)
    except subprocess.TimeoutExpired:
        print(f"  [WARN] audit timeout for {file_path.name}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"  [WARN] bad JSON for {file_path.name}: {e}", file=sys.stderr)
        return None


def collect_unknown_journals(all_results):
    """Find journals that appeared as 'Unknown journal' in audit results."""
    unknown = Counter()
    unknown_details = defaultdict(list)
    for file_result in all_results:
        if not file_result:
            continue
        for c in file_result.get('citations', []):
            tier_reason = c.get('tier_reason', '')
            if 'Unknown journal' in tier_reason:
                # Extract journal name
                journal = c.get('details', {}).get('journal', 'NA')
                if journal and journal != 'NA':
                    unknown[journal] += 1
                    unknown_details[journal].append({
                        'file': Path(file_result['file']).name,
                        'pmid': c.get('citation', ''),
                        'tier_reason': tier_reason,
                    })
    return unknown, unknown_details


def generate_markdown_report(all_results, unknown_journals, total_files, total_blocked):
    """Generate markdown audit report."""
    md = f"""# Citation Audit Report - All Lessons

**Date:** {DATE}
**Project:** `F:\\DL\\mavisresearch\\Bai hoc y khoa`
**Files scanned:** {total_files}

## Overall Summary

| Metric | Count |
|---|---|
| Total files | {total_files} |
| Files with BLOCK | {total_blocked} |
| Total citations | {sum(r.get('summary', {}).get('total', 0) for r in all_results if r)} |
| Total PASS | {sum(r.get('summary', {}).get('pass', 0) for r in all_results if r)} |
| Total WARN | {sum(r.get('summary', {}).get('warn', 0) for r in all_results if r)} |
| Total BLOCK | {sum(r.get('summary', {}).get('block', 0) for r in all_results if r)} |

## Per-File Summary

| File | Topic | Total | Pass | Warn | Block | Status |
|---|---|---|---|---|---|---|
"""
    for r in all_results:
        if not r:
            continue
        s = r['summary']
        path = Path(r['file'])
        topic = path.parent.name
        status = '❌ BLOCK' if s['block'] > 0 else ('⚠️ WARN' if s['warn'] > 0 else '✅ OK')
        md += f"| `{path.name}` | {topic} | {s['total']} | {s['pass']} | {s['warn']} | {s['block']} | {status} |\n"

    md += "\n## BLOCK Issues (must fix)\n\n"
    has_block = False
    for r in all_results:
        if not r:
            continue
        blocks = [c for c in r.get('citations', []) if c.get('severity') == 'block']
        if not blocks:
            continue
        has_block = True
        md += f"### {Path(r['file']).name}\n\n"
        for c in blocks:
            pmid_info = c.get('details', {}).get('pmid_info', {})
            if pmid_info.get('status') == 'NOT_FOUND':
                md += f"- ❌ **{c['citation']}** — PMID không tồn tại trong PubMed (CẦN TÌM PMID ĐÚNG HOẶC BỎ CITE)\n"
            else:
                md += f"- ❌ **{c['citation']}** — {c['verdict']}\n"
        md += "\n"
    if not has_block:
        md += "_Không có BLOCK issue._\n\n"

    md += "## Unknown Journals (cần add vào journal_quartile.json)\n\n"
    md += f"**Total unique unknown journals:** {len(unknown_journals)}\n\n"
    md += "| # | Journal Name | Times Seen | Sample File |\n|---|---|---|---|\n"
    for i, (journal, count) in enumerate(unknown_journals.most_common(40), 1):
        sample = ""
        if journal and journal != 'NA':
            # Find first appearance
            for r in all_results:
                if not r:
                    continue
                for c in r.get('citations', []):
                    if c.get('details', {}).get('journal') == journal:
                        sample = Path(r['file']).name
                        break
                if sample:
                    break
        md += f"| {i} | `{journal}` | {count} | {sample} |\n"

    md += f"\n---\n*Generated by scan_all_lessons.py at {time.strftime('%Y-%m-%d %H:%M:%S')}*\n"
    return md


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ROOT
    if not root.exists():
        print(f"ERROR: root not found: {root}")
        sys.exit(2)

    out_dir = root / "10_Script Python" / "audit_reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_md = out_dir / f"audit_all_lessons_{DATE}.md"
    out_json = out_dir / f"audit_all_lessons_{DATE}.json"
    out_unknown = out_dir / f"unknown_journals_{DATE}.txt"

    print(f"[*] Scanning {root}...", file=sys.stderr)
    files = find_lesson_files(root)
    print(f"[*] Found {len(files)} lesson files", file=sys.stderr)

    all_results = []
    for i, f in enumerate(files, 1):
        print(f"  [{i}/{len(files)}] {f.name}...", file=sys.stderr)
        result = run_audit(f)
        all_results.append(result)

    # Collect unknown journals
    unknown, unknown_details = collect_unknown_journals(all_results)

    # Save outputs
    with open(out_json, 'w', encoding='utf-8') as f:
        # Convert Path objects in 'file' to str
        serializable = []
        for r in all_results:
            if r:
                r['file'] = str(r['file'])
            serializable.append(r)
        json.dump(serializable, f, indent=2, ensure_ascii=False)

    out_md.write_text(generate_markdown_report(all_results, unknown, len(files), sum(1 for r in all_results if r and r.get('summary', {}).get('block', 0) > 0)), encoding='utf-8')

    with open(out_unknown, 'w', encoding='utf-8') as f:
        f.write(f"# Unknown Journals - {DATE}\n\n")
        f.write(f"Total: {len(unknown)}\n\n")
        for journal, count in unknown.most_common():
            f.write(f"{count}\t{journal}\n")

    print(f"\n[+] JSON saved: {out_json}", file=sys.stderr)
    print(f"[+] Markdown report: {out_md}", file=sys.stderr)
    print(f"[+] Unknown journals: {out_unknown}", file=sys.stderr)
    print(f"\n[*] Summary: {len(files)} files, {sum(r.get('summary', {}).get('total', 0) for r in all_results if r)} citations, {sum(r.get('summary', {}).get('block', 0) for r in all_results if r)} BLOCK, {len(unknown)} unique unknown journals", file=sys.stderr)


if __name__ == '__main__':
    main()
