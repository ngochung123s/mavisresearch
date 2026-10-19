"""
build_unified_med_library.py — builder DUY NHẤT của dữ liệu web HungMed (dvnhmed.pages.dev).

Sinh trong `12_Nhi khoa/`:
  - data.js                  window.HUNG_MED_DATA {metadata, curriculum, ped, obgyn}
                             + alias window.PED_LIBRARY_DATA (app/mobile/checklist) + window.SAN_KHOA_DATA
  - CATALOG_PED_VIEWER.json  cùng payload (bản đọc được cho người/agent)
  - checklist.html           EMBEDDED_CURRICULUM (dự phòng khi không tải được data.js)
  - app.html, mobile.html, checklist.html: `data.js?v=<version>` để trình duyệt lấy bản mới

Nguồn:
  - Nhi khoa: `_CURRICULUM_NHI_KHOA.md` + folder bài `PED-xx_*` (bỏ outputs/). Folder có lesson.json thì
    lấy đúng file bài / cards / APKG khai trong manifest.
  - Sản khoa: giáo trình ĐHYD Thái Bình 2021 ở `--san-dir` (mặc định F:/DL/Giao_trinh_San_khoa_Y_Thai_Binh_2021).
    Thiếu nguồn Sản → DỪNG, không ghi gì (tránh deploy trang mất mục Sản khoa).

Chạy tự động sau mỗi lần release bài Nhi (post_release trong 10_Script Python/specialties.json).
Push `main` = Cloudflare Pages deploy.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CURRICULUM_PATH = BASE_DIR.parent / "_CURRICULUM_NHI_KHOA.md"
DEFAULT_SAN_KHOA_DIR = Path(r"F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021")
DATA_JS_PATH = BASE_DIR / "data.js"
CATALOG_JSON_PATH = BASE_DIR / "CATALOG_PED_VIEWER.json"
CHECKLIST_PATH = BASE_DIR / "checklist.html"
VERSIONED_PAGES = ("app.html", "mobile.html", "checklist.html")
DATA_JS_SRC_RE = re.compile(r'<script src="data\.js(?:\?v=[^"]*)?"></script>')
PED_BLOCKS = [
    "Block 0 — Nền tảng tư duy, Tiếp cận & Dược lý Nhi khoa",
    "Block 1 — Hồi sức, Cấp cứu & Ngộ độc Nhi khoa",
    "Block 2 — Sơ sinh học",
    "Block 3 — Hô hấp Nhi khoa",
    "Block 4 — Tiêu hóa & Dinh dưỡng Nhi khoa",
    "Block 5 — Bệnh Truyền nhiễm Nhi khoa",
    "Block 6 — Thận, Tim mạch, Huyết học & Nội tiết Nhi",
]


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
        alt, src = m.group(1), m.group(2)
        if not src.startswith(("http://", "https://", "data:", "/")) and not src.startswith(clean_folder):
            return f"![{alt}]({clean_folder}/{src.lstrip('./')})"
        return m.group(0)

    def repl_img(m):
        pre, src, post = m.group(1), m.group(2), m.group(4)
        if not src.startswith(("http://", "https://", "data:", "/")) and not src.startswith(clean_folder):
            return f'<img {pre}src="{clean_folder}/{src.lstrip("./")}"{post}>'
        return m.group(0)

    res = re.sub(r'!\[(.*?)\]\(((?!https?:\/\/|\/|data:)(?:\.\/)?([^)]+))\)', repl_md, md_text)
    return re.sub(r'<img\s+([^>]*?)src=["\']((?!https?:\/\/|\/|data:)(?:\.\/)?([^"\']+))["\']([^>]*?)>',
                  repl_img, res, flags=re.IGNORECASE)


def parse_ped_curriculum() -> list[dict]:
    if not CURRICULUM_PATH.exists():
        raise SystemExit(f"[BLOCK] không thấy giáo trình Nhi: {CURRICULUM_PATH}")
    lessons = []
    for section in re.split(r'(?=### Block \d+ — )', CURRICULUM_PATH.read_text(encoding="utf-8")):
        if not section.strip().startswith("### Block"):
            continue
        block_m = re.match(r'### (Block \d+ — [^\n\(]+)', section)
        block_name = block_m.group(1).strip() if block_m else "Khác"
        # | **PED-xx** | P0 | Tên | Phạm vi | Phụ thuộc | Trạng thái |
        for r in re.findall(r'\|\s*\*\*(PED-\d+[a-z]?)\*\*\s*\|\s*(P\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|',
                            section, re.IGNORECASE):
            lessons.append({"id": r[0].strip(), "priority": r[1].strip(), "title": r[2].strip(), "scope": r[3].strip(),
                            "dependency": r[4].strip(), "curriculum_status": r[5].strip(), "block": block_name})
    return lessons


def _load_cards(path: Path) -> list:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("cards", []) if isinstance(data, dict) else data


def _apply_manifest(entry: dict, folder: Path) -> None:
    """Folder có lesson.json → dùng đúng file bài/cards/APKG của manifest thay vì đoán theo tên."""
    manifest = json.loads((folder / "lesson.json").read_text(encoding="utf-8"))
    lesson_file = folder / manifest["lesson"] if manifest.get("lesson") else None
    if lesson_file and lesson_file.exists():
        entry["ped_file"] = lesson_file.name
        entry["ped_content"] = normalize_image_paths(strip_frontmatter(lesson_file.read_text(encoding="utf-8")),
                                                     entry["folder_rel"])
    basename = manifest.get("deck", {}).get("basename")
    if basename and (folder / f"{basename}.cards.v2.json").exists():
        entry["cards_file"] = f"{basename}.cards.v2.json"
        entry["cards_count"] = len(_load_cards(folder / entry["cards_file"]))
    if basename and (folder / f"{basename}.apkg").exists():
        entry["apkg_file"] = f"{basename}.apkg"


def scan_ped_files() -> dict[str, dict]:
    discovered: dict[str, dict] = {}
    manifests: dict[str, Path] = {}
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in {"outputs", "raw_cache", ".git", "__pycache__"}]
        root_path = Path(root)
        for file in files:
            ped_m = re.search(r'(PED-\d+[a-z]?)', file) or re.search(r'(PED-\d+[a-z]?)', root_path.name)
            if not ped_m:
                continue
            ped_id = ped_m.group(1).upper()
            entry = discovered.setdefault(ped_id, {
                "ped_file": None, "ped_content": "", "pedytb_file": None, "pedytb_content": "",
                "cards_file": None, "cards_count": 0, "apkg_file": None, "html_file": None,
                "folder_rel": str(root_path.relative_to(BASE_DIR)).replace("\\", "/"),
            })
            fpath = root_path / file
            upper = file.upper()
            if file == "lesson.json":
                manifests[ped_id] = root_path
            elif file.endswith(".md"):
                text = normalize_image_paths(strip_frontmatter(fpath.read_text(encoding="utf-8")), entry["folder_rel"])
                if "PEDYTB" in upper:
                    entry["pedytb_file"], entry["pedytb_content"] = file, text
                elif ("RELEASE" in upper or (file.startswith("PED-") and "BRIEF" not in upper)) and "KNOWLEDGE_CHECK" not in upper:
                    entry["ped_file"], entry["ped_content"] = file, text
            elif file.endswith(".cards.v2.json"):
                if "MASTER" in upper or not entry["cards_file"]:
                    try:
                        entry["cards_count"] = len(_load_cards(fpath))
                        entry["cards_file"] = file
                    except (ValueError, OSError) as e:
                        print(f"[WARN] {ped_id}: không đọc được {file}: {e}")
            elif file.endswith(".apkg"):
                if "MASTER" in upper or not entry["apkg_file"]:
                    entry["apkg_file"] = file
            elif file.endswith(".html") and not file.startswith(("app", "mobile")):
                entry["html_file"] = file
    for ped_id, folder in manifests.items():
        _apply_manifest(discovered[ped_id], folder)
    return discovered


def scan_obgyn_files(san_dir: Path) -> list[dict]:
    index_file = san_dir / "index.json"
    if not index_file.exists():
        raise SystemExit(f"[BLOCK] không thấy nguồn Sản khoa {index_file} — dừng để không ghi đè data.js "
                         f"thành bản mất mục Sản khoa. Dùng --san-dir nếu nguồn ở chỗ khác.")
    lessons = []
    for item in json.loads(index_file.read_text(encoding="utf-8")):
        md_path, json_path = san_dir / item["md_path"], san_dir / item["json_path"]
        if not md_path.exists():
            raise SystemExit(f"[BLOCK] Sản khoa {item['id']}: thiếu {md_path}")
        meta = {}
        if json_path.exists():
            meta = json.loads(json_path.read_text(encoding="utf-8"))
        lessons.append({
            "id": item["id"], "specialty": "obgyn", "specialty_name": "Sản Phụ Khoa",
            "chapter": item["chapter"], "folder": item["folder"], "title": item["title"],
            "author": item.get("author", "Bộ môn Phụ Sản ĐHYD Thái Bình"), "word_count": item.get("word_count", 0),
            "content": md_path.read_text(encoding="utf-8"),
            "key_numbers": meta.get("key_numbers", []), "key_drugs": meta.get("key_drugs", []),
            "md_path": item["md_path"],
        })
    if not lessons:
        raise SystemExit(f"[BLOCK] {index_file} không có bài Sản khoa nào")
    return lessons


def build_payload(san_dir: Path, version: str, generated_at: str) -> dict:
    curriculum = parse_ped_curriculum()
    discovered = scan_ped_files()
    ped_lessons, curriculum_summary = [], []
    for item in curriculum:
        disc = discovered.get(item["id"].upper(), {})
        has_ped, has_pedytb = bool(disc.get("ped_content")), bool(disc.get("pedytb_content"))
        curriculum_summary.append({**item, "has_ped": has_ped, "has_pedytb": has_pedytb,
                                   "cards_count": disc.get("cards_count", 0), "apkg_file": disc.get("apkg_file"),
                                   "folder_rel": disc.get("folder_rel", "")})
        if not (has_ped or has_pedytb):
            continue  # chỉ đưa lên web bài đã có nội dung
        ped_lessons.append({
            **item, "specialty": "ped", "specialty_name": "Nhi Khoa",
            "has_ped": has_ped, "has_pedytb": has_pedytb, "has_cards": disc.get("cards_count", 0) > 0,
            "ped_file": disc.get("ped_file"), "ped_content": disc.get("ped_content", ""),
            "pedytb_file": disc.get("pedytb_file"), "pedytb_content": disc.get("pedytb_content", ""),
            "content": disc.get("ped_content") or disc.get("pedytb_content", ""),
            # chỉ số thẻ — nội dung thẻ nằm trong APKG/cards.v2.json, viewer không đọc (bớt ~3,4 MB cho điện thoại)
            "cards_count": disc.get("cards_count", 0),
            "apkg_file": disc.get("apkg_file"), "html_file": disc.get("html_file"),
            "folder_rel": disc.get("folder_rel", ""),
        })
    obgyn_lessons = scan_obgyn_files(san_dir)
    chapters = list(dict.fromkeys(lesson["chapter"] for lesson in obgyn_lessons))
    return {
        "metadata": {
            "title": "HungMed · Cẩm Nang Lâm Sàng & Giáo Trình Y Khoa",
            "author": "BS. Đỗ Văn Ngọc Hưng",
            "version": version,
            "generated_at": generated_at,
            "total_curriculum": len(curriculum),
            "total_ped": len(ped_lessons),
            "total_ped_standard": sum(lesson["has_ped"] for lesson in ped_lessons),
            "total_pedytb": sum(lesson["has_pedytb"] for lesson in ped_lessons),
            "total_cards": sum(lesson["cards_count"] for lesson in ped_lessons),
            "total_obgyn": len(obgyn_lessons),
            "total_all": len(ped_lessons) + len(obgyn_lessons),
            "blocks": PED_BLOCKS,
            "ped_blocks": PED_BLOCKS,
            "obgyn_chapters": chapters,
        },
        "curriculum": curriculum_summary,
        "ped": ped_lessons,
        "obgyn": obgyn_lessons,
    }


def write_outputs(payload: dict) -> None:
    version = payload["metadata"]["version"]
    js = ("/* Auto-generated by build_unified_med_library.py — KHÔNG sửa tay */\n"
          "window.HUNG_MED_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n"
          "window.PED_LIBRARY_DATA = { metadata: window.HUNG_MED_DATA.metadata, "
          "curriculum: window.HUNG_MED_DATA.curriculum, lessons: window.HUNG_MED_DATA.ped };\n"
          "window.SAN_KHOA_DATA = window.HUNG_MED_DATA.obgyn;\n")
    DATA_JS_PATH.write_text(js, encoding="utf-8")
    CATALOG_JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    checklist = CHECKLIST_PATH.read_text(encoding="utf-8")
    embedded = "const EMBEDDED_CURRICULUM = " + json.dumps(payload["curriculum"], ensure_ascii=False, indent=2) + ";"
    checklist, n = re.subn(r'const EMBEDDED_CURRICULUM = \[[\s\S]*?\n\];', lambda _: embedded, checklist, count=1)
    if n != 1:
        raise SystemExit("[BLOCK] checklist.html: không tìm thấy khối EMBEDDED_CURRICULUM")
    CHECKLIST_PATH.write_text(checklist, encoding="utf-8")

    tag = f'<script src="data.js?v={version}"></script>'
    for page in VERSIONED_PAGES:
        path = BASE_DIR / page
        text, n = DATA_JS_SRC_RE.subn(tag, path.read_text(encoding="utf-8"))
        if n != 1:
            raise SystemExit(f"[BLOCK] {page}: cần đúng 1 thẻ <script src=\"data.js...\">, thấy {n}")
        path.write_text(text, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--san-dir", type=Path, default=DEFAULT_SAN_KHOA_DIR, help="thư mục giáo trình Sản khoa (có index.json)")
    args = ap.parse_args(argv)
    now = datetime.now()
    payload = build_payload(args.san_dir, now.strftime("%Y%m%d_%H%M%S"), now.strftime("%Y-%m-%d %H:%M:%S"))
    write_outputs(payload)
    m = payload["metadata"]
    print(f"[OK] data.js v{m['version']} ({DATA_JS_PATH.stat().st_size / 1e6:.2f} MB): "
          f"Nhi {m['total_ped']} bài ({m['total_ped_standard']} PED chuẩn, {m['total_pedytb']} YTB, {m['total_cards']} thẻ) · "
          f"Sản {m['total_obgyn']} bài · giáo trình Nhi {m['total_curriculum']} mục")
    return 0


if __name__ == "__main__":
    sys.exit(main())
