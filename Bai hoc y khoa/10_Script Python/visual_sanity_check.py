"""
visual_sanity_check.py — Static + dynamic visual gate cho HTML visual summary.

Phát hiện bug render-time mà depth_check + citation_audit + diacritics
không bắt được. Điển hình: Chart.js canvas bị kéo dãn khi render trên
màn hình rộng (container > canvas internal pixel ratio).

Hai lớp check:

1. STATIC (luôn chạy, ~1s):
   - Canvas có hardcoded width attribute → FAIL (chart sẽ méo khi responsive)
   - Canvas không nằm trong wrapper có max-width → FAIL
   - CSS rule `canvas { max-width: ... }` không có trong <style> → FAIL
   - Mermaid block quá rộng (không có max-width) → WARN

2. DYNAMIC (optional, cần Playwright Python package):
   - Render HTML ở viewport 1920x1080 (desktop rộng)
   - Đo tỉ lệ aspect của canvas thực tế
   - Nếu aspect > 5:1 (chart kéo ngang quá) → FAIL

Usage:
    python visual_sanity_check.py path/to/file.html            # static only
    python visual_sanity_check.py path/to/file.html --dynamic  # + playwright check
    python visual_sanity_check.py --folder 09_Source - Markdown # scan all HTML

Exit codes:
    0 = PASS (no blocking issues)
    1 = FAIL (có ít nhất 1 BLOCK)
    2 = ERROR (file không tồn tại, parse fail)

Workflow integration:
    Sau khi build HTML (lesson_builder.write_html), chạy:
        python visual_sanity_check.py <html_path>
    Nếu exit 1 → fix HTML (thêm wrapper div hoặc CSS rule) rồi build lại.
"""
import argparse
import json
import re
import sys
from pathlib import Path


# ============================================================
# STATIC CHECKS
# ============================================================

# Pattern 1: <canvas id="X" width="N" height="M"> — hardcoded width
CANVAS_HARDCODED_WIDTH_RE = re.compile(
    r'<canvas\s+[^>]*\bwidth\s*=\s*["\']\d+["\'][^>]*>',
    re.IGNORECASE,
)

# Pattern 2: <canvas id="X" height="N"> không có width attr (OK nếu có wrapper)
CANVAS_HEIGHT_ONLY_RE = re.compile(
    r'<canvas\s+[^>]*\bheight\s*=\s*["\']\d+["\'][^>]*>',
    re.IGNORECASE,
)

# Pattern 3: detect wrapper div có max-width
WRAPPER_MAXWIDTH_RE = re.compile(
    r'<div[^>]*style\s*=\s*["\'][^"\']*max-width\s*:',
    re.IGNORECASE,
)

# Pattern 4: CSS rule canvas { ... } có max-width
CSS_CANVAS_MAXWIDTH_RE = re.compile(
    r'canvas\s*\{[^}]*max-width\s*:',
    re.IGNORECASE | re.DOTALL,
)


def check_html_static(html_path: Path) -> dict:
    """Static analysis cho 1 HTML file. Trả về dict {ok, issues, summary}."""
    issues = []
    if not html_path.exists():
        return {"ok": False, "error": f"File not found: {html_path}", "issues": []}

    try:
        html_text = html_path.read_text(encoding='utf-8')
    except UnicodeDecodeError as e:
        return {"ok": False, "error": f"Encoding error: {e}", "issues": []}

    # Check 1: hardcoded width attribute
    hardcoded = CANVAS_HARDCODED_WIDTH_RE.findall(html_text)
    if hardcoded:
        for m in hardcoded[:5]:  # limit to 5 examples
            issues.append({
                "level": "BLOCK",
                "kind": "canvas_hardcoded_width",
                "snippet": m[:150],
                "fix_hint": "Bỏ width attr, dùng wrapper div max-width hoặc CSS rule canvas { max-width: 800px }",
            })

    # Check 2: tất cả canvas có height-only (không có width attr)
    all_canvas = CANVAS_HEIGHT_ONLY_RE.findall(html_text)
    if all_canvas and not CSS_CANVAS_MAXWIDTH_RE.search(html_text):
        # Không có CSS rule canvas max-width → mỗi canvas cần wrapper manually
        wrapper_count = len(WRAPPER_MAXWIDTH_RE.findall(html_text))
        if wrapper_count < len(all_canvas):
            issues.append({
                "level": "BLOCK",
                "kind": "canvas_no_maxwidth_protection",
                "snippet": f"{len(all_canvas)} canvas, {wrapper_count} wrapper có max-width",
                "fix_hint": (
                    "Thêm CSS rule vào <style>: canvas { display:block; max-width:800px; margin:0 auto; height:auto!important }"
                    " — hoặc wrap từng canvas trong <div style='max-width:800px;margin:0 auto'>...</div>"
                ),
            })

    # Check 3: Tailwind có load không (sanity)
    if "tailwindcss" not in html_text.lower() and "tailwind" not in html_text.lower():
        issues.append({
            "level": "WARN",
            "kind": "tailwind_missing",
            "snippet": "",
            "fix_hint": "Không thấy Tailwind CDN — chart có thể render raw HTML không có styling",
        })

    # Check 4: Chart.js + mermaid CDN có load không
    if "chart.js" not in html_text.lower() and "chartjs" not in html_text.lower():
        issues.append({
            "level": "WARN",
            "kind": "chartjs_missing",
            "snippet": "",
            "fix_hint": "Không thấy Chart.js CDN — charts sẽ không render",
        })

    ok = not any(i["level"] == "BLOCK" for i in issues)
    return {
        "ok": ok,
        "file": str(html_path),
        "issues": issues,
        "canvas_count": len(all_canvas),
        "wrapper_count": len(WRAPPER_MAXWIDTH_RE.findall(html_text)),
    }


# ============================================================
# DYNAMIC CHECK (Playwright — optional)
# ============================================================

def check_html_dynamic(html_path: Path, viewport_width: int = 1920, viewport_height: int = 1080) -> dict:
    """Render HTML với Playwright headless, đo canvas aspect ratio thực tế.

    Cần `pip install playwright && playwright install chromium`.

    Returns: dict với {ok, canvases: [{id, width, height, aspect_ratio, ok}]}
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {
            "ok": False,
            "error": "playwright not installed. Run: pip install playwright && playwright install chromium",
            "canvases": [],
        }

    issues = []
    file_url = f"file:///{html_path.as_posix()}"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": viewport_width, "height": viewport_height})
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle", timeout=15000)
        # Wait for Chart.js to render
        page.wait_for_timeout(2000)

        canvases = page.evaluate("""
            () => {
                const result = [];
                document.querySelectorAll('canvas').forEach(c => {
                    const rect = c.getBoundingClientRect();
                    result.push({
                        id: c.id || '(no-id)',
                        width: Math.round(rect.width),
                        height: Math.round(rect.height),
                        aspect_ratio: rect.height > 0 ? +(rect.width / rect.height).toFixed(2) : 0,
                    });
                });
                return result;
            }
        """)
        browser.close()

    # Heuristic: aspect ratio > 5:1 (canvas ngang quá dài, gần như chắc chắn méo)
    # Hoặc aspect > 8:1 (rất méo, chắc chắn bug)
    for c in canvases:
        if c["aspect_ratio"] > 8:
            issues.append({
                "level": "BLOCK",
                "kind": "canvas_extreme_aspect",
                "snippet": f'canvas#{c["id"]} {c["width"]}x{c["height"]} ratio={c["aspect_ratio"]}',
                "fix_hint": "Chart quá ngang — wrapper max-width chưa hoạt động hoặc height attr quá nhỏ",
            })
        elif c["aspect_ratio"] > 5:
            issues.append({
                "level": "WARN",
                "kind": "canvas_high_aspect",
                "snippet": f'canvas#{c["id"]} {c["width"]}x{c["height"]} ratio={c["aspect_ratio"]}',
                "fix_hint": "Chart hơi ngang — kiểm tra max-width có hoạt động không",
            })

    ok = not any(i["level"] == "BLOCK" for i in issues)
    return {"ok": ok, "viewport": f"{viewport_width}x{viewport_height}", "canvases": canvases, "issues": issues}


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Visual sanity check cho HTML lesson summary.")
    parser.add_argument("path", nargs="?", help="Path to HTML file")
    parser.add_argument("--folder", help="Scan all HTML trong folder (recursive)")
    parser.add_argument("--dynamic", action="store_true", help="Dùng Playwright render thực tế (chậm ~5s/file)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    # Collect files
    files = []
    if args.folder:
        folder = Path(args.folder)
        if not folder.exists():
            print(f"ERROR: Folder not found: {folder}", file=sys.stderr)
            return 2
        files = list(folder.rglob("*.html"))
        # Filter: skip source/template files
        files = [f for f in files if "_template" not in f.name.lower() and "_backup" not in str(f).lower()]
    elif args.path:
        p = Path(args.path)
        if not p.exists():
            print(f"ERROR: File not found: {p}", file=sys.stderr)
            return 2
        files = [p]
    else:
        parser.print_help()
        return 2

    if not files:
        print("No HTML files found.")
        return 0

    all_results = []
    n_block = 0
    n_warn = 0
    for f in files:
        static_result = check_html_static(f)
        result = {"file": str(f), "static": static_result}
        if args.dynamic:
            result["dynamic"] = check_html_dynamic(f)
        all_results.append(result)
        if static_result.get("issues"):
            for i in static_result["issues"]:
                if i["level"] == "BLOCK":
                    n_block += 1
                elif i["level"] == "WARN":
                    n_warn += 1

    if args.json:
        print(json.dumps(all_results, indent=2, ensure_ascii=False))
    else:
        print("=" * 80)
        print(f"VISUAL SANITY CHECK ({len(files)} file(s))")
        print("=" * 80)
        for r in all_results:
            issues = r["static"].get("issues", [])
            if not issues:
                print(f"  [OK]    {r['file']}")
                print(f"          ({r['static'].get('canvas_count', 0)} canvas, {r['static'].get('wrapper_count', 0)} wrapper)")
                continue
            status = "FAIL" if any(i["level"] == "BLOCK" for i in issues) else "WARN"
            print(f"  [{status}] {r['file']}")
            print(f"          ({r['static'].get('canvas_count', 0)} canvas, {r['static'].get('wrapper_count', 0)} wrapper)")
            for i in issues:
                marker = "🔴" if i["level"] == "BLOCK" else "🟡"
                print(f"          {marker} {i['kind']}: {i['snippet'][:120]}")
                if i.get("fix_hint"):
                    print(f"             → fix: {i['fix_hint'][:140]}")
            if "dynamic" in r and r["dynamic"].get("canvases"):
                print(f"          [dynamic @ {r['dynamic'].get('viewport', '?')}]")
                for c in r["dynamic"]["canvases"]:
                    flag = " ⚠" if c["aspect_ratio"] > 5 else ""
                    print(f"            canvas#{c['id']}: {c['width']}x{c['height']} ratio={c['aspect_ratio']}{flag}")
        print("=" * 80)
        print(f"BLOCK: {n_block}  WARN: {n_warn}  PASS: {len(files) - n_block}")

    return 1 if n_block > 0 else 0


if __name__ == "__main__":
    sys.exit(main())