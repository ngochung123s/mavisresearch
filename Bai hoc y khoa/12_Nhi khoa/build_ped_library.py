"""
build_ped_library.py
Trình quét tự động và đóng gói dữ liệu cho PedViewer (Nhi khoa Mavis Research):
1. Đọc _CURRICULUM_NHI_KHOA.md để lấy toàn bộ 46 chủ đề thuộc 7 Block.
2. Quét đệ quy toàn bộ thư mục 12_Nhi khoa để phát hiện:
   - File PED chuẩn hóa (*_RELEASE_*.md)
   - File PEDYTB giáo trình mở rộng (*_PEDYTB.md)
   - File thẻ nhớ Anki (*.cards.v2.json)
   - File HTML & APKG liên quan
3. Xuất ra data.js và CATALOG_PED_VIEWER.json dùng cho app.html (PedViewer).
"""
from __future__ import annotations
from datetime import datetime
import os
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
CURRICULUM_PATH = BASE_DIR.parent / "_CURRICULUM_NHI_KHOA.md"
DATA_JS_PATH = BASE_DIR / "data.js"
CATALOG_JSON_PATH = BASE_DIR / "CATALOG_PED_VIEWER.json"

def strip_frontmatter(text: str) -> str:
    cleaned = (text or "").lstrip()
    if cleaned.startswith("---"):
        return re.sub(r"^---\s*[\r\n]+[\s\S]*?[\r\n]+---\s*[\r\n]*", "", cleaned)
    return text

def parse_curriculum() -> list[dict]:
    if not CURRICULUM_PATH.exists():
        print(f"Warning: Curriculum file not found at {CURRICULUM_PATH}")
        return []

    content = CURRICULUM_PATH.read_text(encoding="utf-8")

    # Extract blocks and tables
    # Blocks start with: ### Block X — Title (N bài)
    block_sections = re.split(r'(?=### Block \d+ — )', content)
    lessons = []

    for section in block_sections:
        if not section.strip().startswith("### Block"):
            continue

        block_m = re.match(r'### (Block \d+ — [^\n\(]+)', section)
        block_name = block_m.group(1).strip() if block_m else "Khác"

        # Rows: | **PED-xx** | P0 | Title | Scope | Dependency | Status |
        row_matches = re.findall(
            r'\|\s*\*\*(PED-\d+[a-z]?)\*\*\s*\|\s*(P\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|',
            section,
            re.IGNORECASE
        )
        for r in row_matches:
            lessons.append({
                "id": r[0].strip(),
                "priority": r[1].strip(),
                "title": r[2].strip(),
                "scope": r[3].strip(),
                "dependency": r[4].strip(),
                "curriculum_status": r[5].strip(),
                "block": block_name
            })

    return lessons

def scan_files_in_nhi_khoa() -> dict[str, dict]:
    discovered: dict[str, dict] = {}

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in {"outputs", "raw_cache", ".git"}]
        root_path = Path(root)

        # Check folder or files matching PED-XX
        for file in files:
            ped_m = re.search(r'(PED-\d+[a-z]?)', file)
            if not ped_m:
                # check parent folder
                ped_m = re.search(r'(PED-\d+[a-z]?)', root_path.name)

            if not ped_m:
                continue

            ped_id = ped_m.group(1).upper()
            if ped_id not in discovered:
                discovered[ped_id] = {
                    "ped_file": None,
                    "ped_content": "",
                    "pedytb_file": None,
                    "pedytb_content": "",
                    "cards_file": None,
                    "cards_count": 0,
                    "cards_data": [],
                    "apkg_file": None,
                    "html_file": None,
                    "folder_rel": str(root_path.relative_to(BASE_DIR)).replace("\\", "/")
                }

            fpath = root_path / file

            # Identify file roles
            if file.endswith(".md"):
                if "PEDYTB" in file.upper():
                    discovered[ped_id]["pedytb_file"] = file
                    discovered[ped_id]["pedytb_content"] = strip_frontmatter(fpath.read_text(encoding="utf-8"))
                elif ("RELEASE" in file.upper() or (file.startswith("PED-") and "BRIEF" not in file.upper())) and "KNOWLEDGE_CHECK" not in file.upper():
                    # Main lesson release file
                    discovered[ped_id]["ped_file"] = file
                    discovered[ped_id]["ped_content"] = strip_frontmatter(fpath.read_text(encoding="utf-8"))
            elif file.endswith(".cards.v2.json"):
                # Ưu tiên nạp bộ Master Combo nếu có
                if "MASTER" in file.upper() or not discovered[ped_id]["cards_file"]:
                    discovered[ped_id]["cards_file"] = file
                    try:
                        cdata = json.loads(fpath.read_text(encoding="utf-8"))
                        cards = cdata.get("cards", []) if isinstance(cdata, dict) else cdata
                        discovered[ped_id]["cards_count"] = len(cards)
                        discovered[ped_id]["cards_data"] = cards
                    except Exception as e:
                        print(f"Error parsing cards for {ped_id}: {e}")
            elif file.endswith(".apkg"):
                if "MASTER" in file.upper() or not discovered[ped_id]["apkg_file"]:
                    discovered[ped_id]["apkg_file"] = file
            elif file.endswith(".html") and not file.startswith("app"):
                discovered[ped_id]["html_file"] = file

    return discovered

def main():
    print("=" * 60)
    print("XÂY DỰNG DỮ LIỆU THƯ VIỆN NHI KHOA (PED & PEDYTB)")
    print("=" * 60)

    curriculum = parse_curriculum()
    discovered = scan_files_in_nhi_khoa()

    print(f"Đã đọc {len(curriculum)} bài trong Curriculum.")
    print(f"Đã tìm thấy tài liệu thực tế cho {len(discovered)} bài học.")

    lessons_out = []
    blocks_set = []

    ped_count = 0
    pedytb_count = 0
    cards_total = 0

    for item in curriculum:
        pid = item["id"]
        disc = discovered.get(pid) or discovered.get(pid.upper()) or discovered.get(pid.lower()) or {}

        has_ped = bool(disc.get("ped_content"))
        has_pedytb = bool(disc.get("pedytb_content"))
        has_cards = disc.get("cards_count", 0) > 0

        # Lọc bỏ những bài chưa có file thực tế (chưa có output) theo yêu cầu người dùng
        if not (has_ped or has_pedytb):
            continue

        if has_ped:
            ped_count += 1
        if has_pedytb:
            pedytb_count += 1
        cards_total += disc.get("cards_count", 0)

        if item["block"] not in blocks_set:
            blocks_set.append(item["block"])

        lessons_out.append({
            "id": pid,
            "priority": item["priority"],
            "title": item["title"],
            "block": item["block"],
            "scope": item["scope"],
            "dependency": item["dependency"],
            "curriculum_status": item["curriculum_status"],
            "has_ped": has_ped,
            "has_pedytb": has_pedytb,
            "has_cards": has_cards,
            "ped_file": disc.get("ped_file"),
            "ped_content": disc.get("ped_content", ""),
            "pedytb_file": disc.get("pedytb_file"),
            "pedytb_content": disc.get("pedytb_content", ""),
            "cards_count": disc.get("cards_count", 0),
            "cards_data": disc.get("cards_data", []),
            "apkg_file": disc.get("apkg_file"),
            "html_file": disc.get("html_file"),
            "folder_rel": disc.get("folder_rel", "")
        })

    curriculum_summary = []
    for item in curriculum:
        pid = item["id"]
        disc = discovered.get(pid) or discovered.get(pid.upper()) or discovered.get(pid.lower()) or {}
        curriculum_summary.append({
            "id": pid,
            "priority": item["priority"],
            "title": item["title"],
            "block": item["block"],
            "scope": item["scope"],
            "dependency": item["dependency"],
            "curriculum_status": item["curriculum_status"],
            "has_ped": bool(disc.get("ped_content")),
            "has_pedytb": bool(disc.get("pedytb_content")),
            "cards_count": disc.get("cards_count", 0),
            "apkg_file": disc.get("apkg_file"),
            "folder_rel": disc.get("folder_rel", "")
        })

    payload = {
        "metadata": {
            "title": "PedViewer — Thư viện Sách & Bài học Nhi khoa",
            "version": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_curriculum": len(curriculum),
            "total_ped": ped_count,
            "total_pedytb": pedytb_count,
            "total_cards": cards_total,
            "blocks": [
                "Block 0 — Nền tảng tư duy, Tiếp cận & Dược lý Nhi khoa",
                "Block 1 — Hồi sức, Cấp cứu & Ngộ độc Nhi khoa",
                "Block 2 — Sơ sinh học",
                "Block 3 — Hô hấp Nhi khoa",
                "Block 4 — Tiêu hóa & Dinh dưỡng Nhi khoa",
                "Block 5 — Bệnh Truyền nhiễm Nhi khoa",
                "Block 6 — Thận, Tim mạch, Huyết học & Nội tiết Nhi"
            ]
        },
        "curriculum": curriculum_summary,
        "lessons": lessons_out
    }
    # Write data.js
    js_content = "/* Auto-generated by build_ped_library.py */\nwindow.PED_LIBRARY_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    DATA_JS_PATH.write_text(js_content, encoding="utf-8")
    print(f"Đã ghi: {DATA_JS_PATH} ({len(js_content)} ký tự)")

    # Write CATALOG_PED_VIEWER.json
    CATALOG_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã ghi: {CATALOG_JSON_PATH}")
    # Update checklist.html embedded curriculum
    checklist_path = BASE_DIR / "checklist.html"
    if checklist_path.is_file():
        ch_text = checklist_path.read_text(encoding="utf-8")
        replacement = "const EMBEDDED_CURRICULUM = " + json.dumps(curriculum_summary, ensure_ascii=False, indent=2) + ";"
        ch_text = re.sub(r'const EMBEDDED_CURRICULUM = \[[\s\S]*?\];', replacement, ch_text)
        checklist_path.write_text(ch_text, encoding="utf-8")
        print(f"Đã đồng bộ tự động dữ liệu cho Checklist: {checklist_path}")

    print("\nThống kê:")
    print(f"- Tổng số bài Curriculum: {len(curriculum)}")
    print(f"- Số bài có PED chuẩn hóa: {ped_count}")
    print(f"- Số bài có sách mở rộng PEDYTB: {pedytb_count}")
    print(f"- Tổng số flashcard Anki: {cards_total}")

if __name__ == "__main__":
    main()
