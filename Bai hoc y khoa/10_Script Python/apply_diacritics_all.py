"""Apply add_diacritics to all bai hoc y khoa .md files."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from add_diacritics import convert_file

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown")


def main():
    """Auto-find all .md lesson files in 09_Source - Markdown (excluding subdirs we don't want)."""
    # Find all .md in 09_Source - Markdown and subdirs
    all_md = list(ROOT.rglob("*.md"))
    # Exclude audit_reports
    all_md = [p for p in all_md if "audit_reports" not in str(p)]
    # Exclude README
    all_md = [p for p in all_md if p.name != "_README.md"]
    # Exclude very short files (likely stubs)
    all_md = [p for p in all_md if p.stat().st_size > 1000]

    converted = 0
    failed = []
    for path in sorted(all_md):
        try:
            convert_file(path)
            rel = path.relative_to(ROOT)
            print(f"  [OK]   {rel}")
            converted += 1
        except Exception as e:
            rel = path.relative_to(ROOT)
            print(f"  [ERR]  {rel} - {e}")
            failed.append(str(rel))
    print(f"\nConverted: {converted}/{len(all_md)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
