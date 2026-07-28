"""Wrapper: build lesson -> citation audit.

Usage:
    python make_lesson_cited.py <topic> <date>

Workflow:
1. Run citation_audit.py on existing lesson file (if any)
2. Show summary of citations
3. (Optional) Interactively help fix BLOCK issues

This is meant to be run AFTER make_long_lesson.py or similar.
"""
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
AUDIT_SCRIPT = SCRIPT_DIR / "citation_audit.py"


def run_audit(file_path, json_output=True, out_md=None):
    """Run citation_audit.py and return parsed JSON result."""
    args = [
        sys.executable, str(AUDIT_SCRIPT), str(file_path),
        "--json", "--quiet",
    ]
    if out_md:
        args.extend(["--out", str(out_md)])

    result = subprocess.run(args, capture_output=True, text=True, encoding='utf-8')
    if result.returncode not in (0, 1):
        print(f"ERROR: audit script failed (exit {result.returncode})")
        print(result.stderr)
        return None

    if json_output:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"ERROR: failed to parse audit output: {e}")
            print(result.stdout[:500])
            return None
    return None


def print_summary(result, file_path):
    """Print human-readable summary."""
    s = result['summary']
    print()
    print('=' * 80)
    print(f"  CITATION AUDIT: {file_path}")
    print('=' * 80)
    print()
    print(f"  Total: {s['total']}  |  Pass: {s['pass']}  |  Warn: {s['warn']}  |  BLOCK: {s['block']}")
    print()

    if s['block'] > 0:
        print(f"  [X] CANNOT PUBLISH - {s['block']} BLOCK issue(s):")
        for c in result['citations']:
            if c['severity'] == 'block':
                print(f"      - {c['citation']}: {c['verdict']}")
        print()

    if s['warn'] > 0:
        print(f"  [!] {s['warn']} WARN issue(s) - review truoc khi publish:")
        for c in result['citations']:
            if c['severity'] == 'warn':
                print(f"      - {c['citation']}: {c['verdict']}")
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python make_lesson_cited.py <file.docx|file.md> [out_report.md]")
        print()
        print("Examples:")
        print("  python make_lesson_cited.py 'Bai hoc - 2026-06-18.docx'")
        sys.exit(2)

    file_path = Path(sys.argv[1])
    out_md = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not file_path.exists():
        print(f"ERROR: file not found: {file_path}")
        sys.exit(2)

    if not AUDIT_SCRIPT.exists():
        print(f"ERROR: citation_audit.py not found: {AUDIT_SCRIPT}")
        sys.exit(2)

    print(f"[*] Running citation audit on: {file_path}")
    result = run_audit(file_path, out_md=out_md)
    if result is None:
        sys.exit(1)

    print_summary(result, file_path)

    if out_md:
        print(f"  [+] Markdown report saved: {out_md}")
        print()

    # Exit code: 0 if no block, 1 if block
    sys.exit(0 if result['summary']['block'] == 0 else 1)


if __name__ == '__main__':
    main()
