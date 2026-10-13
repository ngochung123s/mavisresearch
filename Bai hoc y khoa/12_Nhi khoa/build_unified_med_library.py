"""
build_unified_med_library.py
Xây dựng kho dữ liệu Y khoa hợp nhất HungMed (Nhi khoa & Sản Phụ khoa):
1. Quét toàn bộ bài học Nhi khoa (PED & PEDYTB).
2. Quét toàn bộ 54 bài Giáo trình Sản Phụ khoa ĐHYD Thái Bình 2021.
3. Xuất file data.js hợp nhất phục vụ app.html và mobile.html của BS. Đỗ Văn Ngọc Hưng.
"""
from __future__ import annotations
from datetime import datetime
import os
import re
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CURRICULUM_PATH = BASE_DIR.parent / "_CURRICULUM_NHI_KHOA.md"
SAN_KHOA_DIR = Path(r"F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021")
DATA_JS_PATH = BASE_DIR / "data.js"
CATALOG_JSON_PATH = BASE_DIR / "CATALOG_PED_VIEWER.json"

def strip_frontmatter(text: str) -> str:
    cleaned = (text or "").lstrip()
    if cleaned.startswith("---"):
        return re.sub(r"^---\s*[\r\n]+[\s\S]*?[\r\n]+---\s*[\r\n]*", "", cleaned)
    return text

def normalize_image_paths(md_text: str, folder_rel: str) -> str:
    if not folder_rel or not md_text:
        return md_text
    clean_folder = folder_rel.replace("\\", "/").rstrip("/")
    def repl_md(m):
        alt = m.group(1)
        src = m.group(2)
        if not src.startswith(("http://", "https://", "data:", "/")) and not src.startswith(clean_folder):
            clean_src = src.lstrip("./")
            return f"![{alt}]({clean_folder}/{clean_src})"
        return m.group(0)

    def repl_img(m):
        pre = m.group(1)
        src = m.group(2)
        post = m.group(3)
        if not src.startswith(("http://", "https://", "data:", "/")) and not src.startswith(clean_folder):
            clean_src = src.lstrip("./")
            return f'<img {pre}src="{clean_folder}/{clean_src}"{post}>'
        return m.group(0)

    res = re.sub(r'!\[(.*?)\]\(((?!https?:\/\/|\/|data:)(?:\.\/)?([^)]+))\)', repl_md, md_text)
    res = re.sub(r'<img\s+([^>]*?)src=["\']((?!https?:\/\/|\/|data:)(?:\.\/)?([^"\']+))["\']([^>]*?)>', repl_img, res, flags=re.IGNORECASE)
    return res

def parse_ped_curriculum() -> list[dict]:
    if not CURRICULUM_PATH.exists():
        print(f"Warning: Curriculum file not found at {CURRICULUM_PATH}")
        return []

    content = CURRICULUM_PATH.read_text(encoding="utf-8")
    block_sections = re.split(r'(?=### Block \d+ — )', content)
    lessons = []

    for section in block_sections:
        if not section.strip().startswith("### Block"):
            continue

        block_m = re.match(r'### (Block \d+ — [^\n\(]+)', section)
        block_name = block_m.group(1).strip() if block_m else "Khác"

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

def scan_ped_files() -> dict[str, dict]:
    discovered: dict[str, dict] = {}

    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in {"outputs", "raw_cache", ".git"}]
        root_path = Path(root)

        for file in files:
            ped_m = re.search(r'(PED-\d+[a-z]?)', file)
            if not ped_m:
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
            if file.endswith(".md"):
                raw_text = strip_frontmatter(fpath.read_text(encoding="utf-8"))
                norm_text = normalize_image_paths(raw_text, discovered[ped_id]["folder_rel"])
                if "PEDYTB" in file.upper():
                    discovered[ped_id]["pedytb_file"] = file
                    discovered[ped_id]["pedytb_content"] = norm_text
                elif ("RELEASE" in file.upper() or (file.startswith("PED-") and "BRIEF" not in file.upper())) and "KNOWLEDGE_CHECK" not in file.upper():
                    discovered[ped_id]["ped_file"] = file
                    discovered[ped_id]["ped_content"] = norm_text
            elif file.endswith(".cards.v2.json"):
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
            elif file.endswith(".html") and not file.startswith("app") and not file.startswith("mobile"):
                discovered[ped_id]["html_file"] = file

    return discovered

def scan_obgyn_files() -> list[dict]:
    obgyn_lessons = []
    if not SAN_KHOA_DIR.exists():
        print(f"Warning: San Khoa directory not found at {SAN_KHOA_DIR}")
        return []

    index_file = SAN_KHOA_DIR / "index.json"
    if not index_file.exists():
        print(f"Warning: San Khoa index.json not found at {index_file}")
        return []

    index_data = json.loads(index_file.read_text(encoding="utf-8"))
    for item in index_data:
        md_path = SAN_KHOA_DIR / item["md_path"]
        json_path = SAN_KHOA_DIR / item["json_path"]

        md_content = ""
        if md_path.exists():
            md_content = md_path.read_text(encoding="utf-8")

        key_numbers = []
        key_drugs = []
        if json_path.exists():
            try:
                j_obj = json.loads(json_path.read_text(encoding="utf-8"))
                key_numbers = j_obj.get("key_numbers", [])
                key_drugs = j_obj.get("key_drugs", [])
            except Exception:
                pass

        obgyn_lessons.append({
            "id": item["id"],
            "specialty": "obgyn",
            "specialty_name": "Sản Phụ Khoa",
            "chapter": item["chapter"],
            "folder": item["folder"],
            "title": item["title"],
            "author": item.get("author", "Bộ môn Phụ Sản ĐHYD Thái Bình"),
            "word_count": item.get("word_count", 0),
            "content": md_content,
            "key_numbers": key_numbers,
            "key_drugs": key_drugs,
            "md_path": item["md_path"]
        })

    return obgyn_lessons

def main():
    print("=" * 70)
    print("XÂY DỰNG KHO DỮ LIỆU Y KHOA HỢP NHẤT: NHI KHOA + SẢN PHỤ KHOA")
    print("Tác giả: BS. Đỗ Văn Ngọc Hưng")
    print("=" * 70)

    # 1. Nhi khoa
    curriculum = parse_ped_curriculum()
    discovered = scan_ped_files()

    ped_lessons = []
    ped_count = 0
    pedytb_count = 0
    cards_total = 0

    for item in curriculum:
        pid = item["id"]
        disc = discovered.get(pid) or discovered.get(pid.upper()) or discovered.get(pid.lower()) or {}

        has_ped = bool(disc.get("ped_content"))
        has_pedytb = bool(disc.get("pedytb_content"))
        if not (has_ped or has_pedytb):
            continue

        if has_ped:
            ped_count += 1
        if has_pedytb:
            pedytb_count += 1
        cards_total += disc.get("cards_count", 0)

        ped_lessons.append({
            "id": pid,
            "specialty": "ped",
            "specialty_name": "Nhi Khoa",
            "priority": item["priority"],
            "title": item["title"],
            "block": item["block"],
            "scope": item["scope"],
            "dependency": item["dependency"],
            "curriculum_status": item["curriculum_status"],
            "has_ped": has_ped,
            "has_pedytb": has_pedytb,
            "has_cards": disc.get("cards_count", 0) > 0,
            "ped_file": disc.get("ped_file"),
            "ped_content": disc.get("ped_content", ""),
            "pedytb_file": disc.get("pedytb_file"),
            "pedytb_content": disc.get("pedytb_content", ""),
            "content": disc.get("ped_content", "") or disc.get("pedytb_content", ""),
            "cards_count": disc.get("cards_count", 0),
            "cards_data": disc.get("cards_data", []),
            "apkg_file": disc.get("apkg_file"),
            "folder_rel": disc.get("folder_rel", "")
        })

    # 2. Sản khoa
    obgyn_lessons = scan_obgyn_files()
    print(f"-> Nhi khoa: Đã nạp {len(ped_lessons)} bài có nội dung.")
    print(f"-> Sản khoa: Đã nạp {len(obgyn_lessons)} bài từ Giáo trình Thái Bình 2021.")

    chapters = []
    for l in obgyn_lessons:
        if l["chapter"] not in chapters:
            chapters.append(l["chapter"])

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ver_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    hung_med_payload = {
        "metadata": {
            "title": "HungMed · Cẩm Nang Lâm Sàng & Giáo Trình Y Khoa",
            "author": "BS. Đỗ Văn Ngọc Hưng",
            "version": ver_str,
            "generated_at": now_str,
            "total_ped": len(ped_lessons),
            "total_obgyn": len(obgyn_lessons),
            "total_all": len(ped_lessons) + len(obgyn_lessons),
            "ped_blocks": [
                "Block 0 — Nền tảng tư duy, Tiếp cận & Dược lý Nhi khoa",
                "Block 1 — Hồi sức, Cấp cứu & Ngộ độc Nhi khoa",
                "Block 2 — Sơ sinh học",
                "Block 3 — Hô hấp Nhi khoa",
                "Block 4 — Tiêu hóa & Dinh dưỡng Nhi khoa",
                "Block 5 — Bệnh Truyền nhiễm Nhi khoa",
                "Block 6 — Thận, Tim mạch, Huyết học & Nội tiết Nhi"
            ],
            "obgyn_chapters": chapters
        },
        "ped": ped_lessons,
        "obgyn": obgyn_lessons
    }

    # Đóng gói data.js với cả 2 namespace mới và cũ để tương thích ngược 100%
    js_content = "/* Auto-generated by build_unified_med_library.py */\n"
    js_content += "window.HUNG_MED_DATA = " + json.dumps(hung_med_payload, ensure_ascii=False) + ";\n"
    js_content += "window.PED_LIBRARY_DATA = { metadata: window.HUNG_MED_DATA.metadata, lessons: window.HUNG_MED_DATA.ped };\n"
    js_content += "window.SAN_KHOA_DATA = window.HUNG_MED_DATA.obgyn;\n"

    DATA_JS_PATH.write_text(js_content, encoding="utf-8")
    print(f"\n[OK] Đã xuất {DATA_JS_PATH} (Dung lượng: {len(js_content) / (1024*1024):.2f} MB)")

    # Ghi catalog JSON
    CATALOG_JSON_PATH.write_text(json.dumps(hung_med_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] Đã xuất {CATALOG_JSON_PATH}")

    print("\n" + "=" * 70)
    print("HOÀN TẤT ĐÓNG GÓI DỮ LIỆU HỢP NHẤT HUNGMED!")
    print(f"- Tổng số bài Nhi khoa: {len(ped_lessons)} bài")
    print(f"- Tổng số bài Sản khoa: {len(obgyn_lessons)} bài")
    print(f"- TỔNG CỘNG: {len(ped_lessons) + len(obgyn_lessons)} BÀI HỌC TOÀN VĂN")
    print("=" * 70)

if __name__ == "__main__":
    main()
