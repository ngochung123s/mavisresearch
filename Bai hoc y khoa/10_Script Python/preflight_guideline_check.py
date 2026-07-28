"""Pre-flight guideline check - chạy TRƯỚC khi viết medical lesson.

Usage:
    python preflight_guideline_check.py --topic "ovarian stimulation" --guideline "ESHRE 2025"

Verify:
1. Guideline có trong guideline_versions.json không
2. Nếu có: có phải current version không (so với guideline_versions.json)
3. Nếu KHÔNG có trong registry: warn, suggest add
4. Nếu stale (có version mới hơn current): block, suggest use new version

Exit codes:
  0 = OK, proceed
  1 = WARN, proceed with caution
  2 = BLOCK, must use new guideline version
"""
import argparse
import json
import sys
from pathlib import Path

REGISTRY_PATH = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\guideline_versions.json")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True, help="Topic of lesson, e.g. 'ovarian stimulation'")
    parser.add_argument("--guideline", required=True, help="Guideline user plan to use, e.g. 'ESHRE 2025'")
    args = parser.parse_args()

    if not REGISTRY_PATH.exists():
        print(f"[WARN] Registry not found: {REGISTRY_PATH}")
        print(f"[WARN] Run check_guideline_freshness.py first to initialize registry.")
        return 1

    with open(REGISTRY_PATH, encoding="utf-8") as f:
        registry = json.load(f)

    guidelines = registry.get("guidelines", {})

    # Map topic to guideline key (heuristic)
    topic_lower = args.topic.lower()
    guideline_lower = args.guideline.lower()

    # Find best match
    matched_key = None
    for key, g in guidelines.items():
        key_words = key.replace("_", " ").lower()
        if topic_lower in key_words or any(w in key_words for w in topic_lower.split()):
            if "ovarian" in key_words and "stimulation" in key_words:
                matched_key = key
                break
            if "fertility" in key_words and "fertility" in topic_lower:
                matched_key = key
                break
            if matched_key is None:
                matched_key = key  # First match

    if not matched_key:
        print(f"[WARN] No guideline found in registry for topic: {args.topic}")
        print(f"[WARN] Consider adding to guideline_versions.json before writing lesson.")
        return 1

    g = guidelines[matched_key]
    current = g.get("current", {})
    current_label = current.get("version_label", "")
    current_pmid = current.get("pmid", "")
    current_year = ""

    if "year_published" in current:
        import re
        m = re.search(r"(\d{4})", current["year_published"])
        if m:
            current_year = m.group(1)

    # Check if user plan matches current
    guideline_year = ""
    import re
    m = re.search(r"(\d{4})", args.guideline)
    if m:
        guideline_year = m.group(1)

    print(f"[INFO] Topic '{args.topic}' → matched guideline key: {matched_key}")
    print(f"[INFO] Registry current: {current_label} (PMID {current_pmid}, year {current_year})")
    print(f"[INFO] User plans to use: {args.guideline}")

    if guideline_year and current_year:
        # Convert to int for comparison
        try:
            gy = int(guideline_year)
            cy = int(current_year)
            # Accept ±1 year tolerance (e.g. "ESHRE 2025" published in 2026 Hum Reprod)
            if gy < cy - 1:
                print(f"\n[BLOCK] User plans to use OLDER version ({guideline_year}) than current ({current_year}).")
                print(f"[BLOCK] MUST use {current_label} instead.")
                print(f"[BLOCK] Action: Update MD/DOCX/HTML to use PMID {current_pmid} ({current_label}).")
                return 2
            elif gy > cy + 1:
                print(f"\n[WARN] User plans to use NEWER version ({guideline_year}) than registry ({current_year}).")
                print(f"[WARN] Registry may be stale. Run check_guideline_freshness.py to update.")
                return 1
            else:
                print(f"\n[OK] User plans to use CURRENT version ({guideline_year}, registry {current_year}).")
                return 0
        except ValueError:
            pass

    # Fallback: search guideline_lower in current_label
    if guideline_lower.replace(" ", "") in current_label.replace(" ", "").lower():
        print(f"\n[OK] User plans to use current guideline.")
        return 0

    print(f"\n[WARN] Cannot definitively match. Registry has {current_label}. User: {args.guideline}.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
