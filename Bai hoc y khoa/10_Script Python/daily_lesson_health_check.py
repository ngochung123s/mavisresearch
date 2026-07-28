"""
daily_lesson_health_check.py — Verify daily lesson có đủ Markdown và Anki deck không.

Chạy SAU daily-lesson-2100 cron (recommend 21:05 hoặc 21:10).
Nếu thiếu file hoặc gates fail → gửi Telegram alert qua curl.

Checklist:
1. Có folder mới trong 01_San phu khoa / 02_Ho tro sinh san ART / 03_Sieu am thai
   trong 30 phút qua không? (skip folder 09_Source/10_Script)
2. Nếu có folder mới → check 2 deliverables:
   - <folder>/<topic> - YYYY-MM-DD.md
   - <folder>/Anki - <topic> N cards - YYYY-MM-DD.apkg
3. Chạy depth_check + citation_audit + verify_diacritics
4. Nếu có BLOCK ở bất kỳ gate → alert Telegram

Usage:
    python daily_lesson_health_check.py --since-min 60   # check trong 60 phút qua
    python daily_lesson_health_check.py --since-min 1440 # check cả ngày

Exit codes:
    0 = OK (no missing files, no BLOCK)
    1 = FAIL (missing files or BLOCK detected)
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
SCRIPT_DIR = ROOT / "10_Script Python"
OUTPUT_DIRS = [
    ROOT / "01_San phu khoa",
    ROOT / "02_Ho tro sinh san ART",
    ROOT / "03_Sieu am thai",
]
MD_DIR = ROOT / "09_Source - Markdown"

# Skip folders này khi scan (source / script dirs)
SKIP_NAMES = {
    "_abstracts.txt", ".bak", "_backup", "_templates",
    "_fulltext_", "_search_args_", "_fetch",
}


def get_recent_files(folder: Path, since: datetime):
    """Trả về tất cả .md/.apkg được tạo/sửa trong folder kể từ `since`."""
    if not folder.exists():
        return []
    result = []
    for f in folder.rglob("*"):
        if not f.is_file():
            continue
        if any(skip in f.name.lower() for skip in SKIP_NAMES):
            continue
        if f.suffix.lower() not in {".md", ".apkg"}:
            continue
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        if mtime >= since:
            result.append((f, mtime))
    return sorted(result, key=lambda x: -x[1].timestamp())


def run_gate(script: str, *args) -> tuple[int, str]:
    """Chạy 1 script con. Trả về (exit_code, stdout)."""
    script_path = SCRIPT_DIR / script
    if not script_path.exists():
        return (2, f"Script not found: {script_path}")
    try:
        result = subprocess.run(
            ["python", str(script_path), *args],
            capture_output=True, text=True, timeout=120,
        )
        return (result.returncode, result.stdout + result.stderr)
    except subprocess.TimeoutExpired:
        return (2, f"Timeout running {script}")
    except Exception as e:
        return (2, f"Error running {script}: {e}")


def check_lesson(folder: Path) -> dict:
    """Check 1 folder lesson: tìm MD/APKG mới, chạy gates."""
    report = {"folder": str(folder), "files": [], "gates": {}, "block_count": 0}

    patterns = {
        "md": list(folder.glob("*.md")),
        "apkg": list(folder.glob("Anki*.apkg")) + list(folder.glob("*cards*.apkg")),
    }
    for kind, files in patterns.items():
        if not files:
            report.setdefault("missing", []).append(kind)
        for f in files[:3]:  # top 3 files per kind
            report["files"].append({"kind": kind, "path": str(f), "size": f.stat().st_size})

    md_candidates = patterns["md"]
    if not md_candidates:
        # Fallback cho bài cũ, có MD ở thư mục nguồn riêng.
        folder_name = folder.name
        for sub in MD_DIR.iterdir():
            if sub.is_dir() and folder_name.lower() in sub.name.lower():
                md_candidates.extend(sub.glob("*.md"))
        md_candidates.extend([f for f in MD_DIR.glob("*.md") if folder_name.lower() in f.name.lower()])

    if md_candidates:
        md_path = md_candidates[0]
        report["md"] = str(md_path)

        # Run gates
        ec, out = run_gate("depth_check.py", str(md_path))
        report["gates"]["depth_check"] = {"exit": ec, "pass": ec == 0, "snippet": out[-300:] if out else ""}

        ec, out = run_gate("verify_diacritics.py", "--file", str(md_path))
        report["gates"]["diacritics"] = {"exit": ec, "pass": ec == 0, "snippet": out[-200:] if out else ""}

        ec, out = run_gate("citation_audit.py", str(md_path))
        # Parse BLOCK count from output
        block_count = 0
        for line in out.splitlines():
            if "BLOCK:" in line:
                try:
                    block_count = int(line.split("BLOCK:")[1].strip().split()[0])
                except (IndexError, ValueError):
                    pass
        report["gates"]["citation_audit"] = {"exit": ec, "pass": ec == 0 and block_count == 0, "block": block_count}
        if block_count > 0:
            report["block_count"] += block_count


    return report


def send_telegram(message: str):
    """Gửi Telegram qua curl. Cần env TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID."""
    import os
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not bot_token or not chat_id:
        print(f"[Telegram] Skipped (no token/chat_id). Message would be:\n{message}")
        return False
    try:
        import urllib.request
        import urllib.parse
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": message, "parse_mode": "HTML"}).encode()
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception as e:
        print(f"[Telegram] Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Daily lesson health check.")
    parser.add_argument("--since-min", type=int, default=60,
                        help="Check files modified trong N phút qua (default: 60)")
    parser.add_argument("--no-telegram", action="store_true", help="Skip Telegram alert")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    args = parser.parse_args()

    since = datetime.now() - timedelta(minutes=args.since_min)
    print(f"[Health] Checking files modified since {since.isoformat()}")
    print(f"[Health] Time window: {args.since_min} minutes")

    # Tìm tất cả folder có file mới. Chỉ check folder lesson (NN_Topic), skip root.
    folders_with_recent = set()
    for out_dir in OUTPUT_DIRS:
        for f, mtime in get_recent_files(out_dir, since):
            parent = f.parent
            # Skip root: chỉ check folder con có dạng "NN_Topic" hoặc có chứa " - "
            if parent == out_dir:
                continue  # file ở root, không phải lesson folder
            folders_with_recent.add(parent)

    if not folders_with_recent:
        print(f"[Health] No recent lesson files in last {args.since_min} min")
        if args.json:
            print(json.dumps({"since": since.isoformat(), "results": [], "summary": {"folders": 0, "missing": 0, "blocks": 0}}, indent=2))
        return 0

    # Check từng folder
    results = []
    total_blocks = 0
    total_missing = 0
    for folder in sorted(folders_with_recent):
        report = check_lesson(folder)
        results.append(report)
        total_blocks += report.get("block_count", 0)
        total_missing += len(report.get("missing", []))

    # Build summary
    summary = {
        "since": since.isoformat(),
        "folders_checked": len(folders_with_recent),
        "folders_missing_files": sum(1 for r in results if r.get("missing")),
        "total_blocks": total_blocks,
        "results": results,
    }

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("=" * 80)
        print(f"DAILY LESSON HEALTH CHECK (since {since.strftime('%Y-%m-%d %H:%M')})")
        print("=" * 80)
        for r in results:
            status = "OK"
            if r.get("missing"):
                status = f"MISSING: {','.join(r['missing'])}"
            elif r.get("block_count", 0) > 0:
                status = f"BLOCK: {r['block_count']}"
            print(f"  [{status}] {r['folder']}")
            for f_info in r.get("files", []):
                print(f"           {f_info['kind']:5s} {f_info['path']} ({f_info['size']} bytes)")
            if r.get("md"):
                print(f"           md: {r['md']}")
            for gate, info in r.get("gates", {}).items():
                marker = "OK" if info["pass"] else "FAIL"
                extra = f" (BLOCK={info.get('block', '?')})" if "block" in info else ""
                print(f"           gate {gate}: {marker}{extra}")
        print("=" * 80)
        print(f"Folders checked: {summary['folders_checked']}")
        print(f"Missing files: {summary['folders_missing_files']}")
        print(f"Total BLOCKs: {summary['total_blocks']}")

    # Telegram alert nếu có vấn đề
    if not args.no_telegram and (total_blocks > 0 or total_missing > 0):
        alert_lines = ["🚨 <b>Daily Lesson Health Alert</b>"]
        alert_lines.append(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        alert_lines.append(f"Window: {args.since_min} min")
        if total_missing > 0:
            alert_lines.append(f"❌ Missing files: {total_missing}")
        if total_blocks > 0:
            alert_lines.append(f"❌ Total BLOCKs: {total_blocks}")
        for r in results:
            if r.get("missing") or r.get("block_count", 0) > 0:
                folder_name = Path(r["folder"]).name
                alert_lines.append(f"\n📁 {folder_name}")
                if r.get("missing"):
                    alert_lines.append(f"  Missing: {','.join(r['missing'])}")
                for gate, info in r.get("gates", {}).items():
                    if not info["pass"]:
                        alert_lines.append(f"  {gate} FAIL")
        send_telegram("\n".join(alert_lines))

    return 1 if (total_blocks > 0 or total_missing > 0) else 0


if __name__ == "__main__":
    sys.exit(main())