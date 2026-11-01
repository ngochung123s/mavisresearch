"""
build_unified_med_library.py — builder DUY NHẤT của dữ liệu web HungMed (dvnhmed.pages.dev).

Sinh trong `12_Nhi khoa/`:
  - data.js                  window.HUNG_MED_DATA {metadata, curriculum, ped, obgyn}
                             + alias window.PED_LIBRARY_DATA (app/mobile/checklist) + window.SAN_KHOA_DATA
  - CATALOG_PED_VIEWER.json  cùng payload (bản đọc được cho người/agent)
  - checklist.html           EMBEDDED_CURRICULUM (dự phòng khi không tải được data.js)
  - app.html, mobile.html, checklist.html: `data.js?v=<version>` để trình duyệt lấy bản mới
  - san_khoa_media/          ảnh giáo trình Sản (chép từ nguồn, xóa ảnh không còn dùng)

Nguồn:
  - Nhi khoa: `_CURRICULUM_NHI_KHOA.md` + folder bài `PED-xx_*` (bỏ outputs/). Folder có lesson.json thì
    lấy đúng file bài / cards / APKG khai trong manifest.
  - Sản khoa: giáo trình ĐHYD Thái Bình 2021 ở `--san-dir` (mặc định F:/DL/Giao_trinh_San_khoa_Y_Thai_Binh_2021),
    do `01_San phu khoa/_Giao_trinh_YTB_2021_tools/extract_san_khoa.py` trích từ file .doc gốc.
    Thiếu nguồn Sản hoặc thiếu ảnh được trỏ tới → DỪNG, không ghi gì (tránh deploy trang mất/hỏng mục Sản khoa).

Chạy tự động sau mỗi lần release bài Nhi (post_release trong 10_Script Python/specialties.json).
Push `main` = Cloudflare Pages deploy.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
PED_DIR = REPO_ROOT / "12_Nhi khoa"
CURRICULUM_PATH = REPO_ROOT / "_CURRICULUM_NHI_KHOA.md"
DEFAULT_SAN_KHOA_DIR = Path(r"F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021")
DEFAULT_HOASINH_DIR = REPO_ROOT / "14_Hoa sinh"
DEFAULT_CLINICAL_SAN_DIR = REPO_ROOT / "01_San phu khoa"
DEFAULT_CLINICAL_ART_DIR = REPO_ROOT / "02_Ho tro sinh san ART"
DEFAULT_CLINICAL_FUS_DIR = REPO_ROOT / "03_Sieu am thai"
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
        if not src.startswith(("http://", "https://", "data:", "/", "san_khoa_media/", "hoasinh_media/")) and not src.startswith(clean_folder):
            return f"![{alt}]({clean_folder}/{src.lstrip('./')})"
        return m.group(0)

    def repl_img(m):
        pre, src, post = m.group(1), m.group(2), m.group(4)
        if not src.startswith(("http://", "https://", "data:", "/", "san_khoa_media/", "hoasinh_media/")) and not src.startswith(clean_folder):
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
    for root, dirs, files in os.walk(PED_DIR):
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
                "folder_rel": Path(os.path.relpath(root_path, BASE_DIR)).as_posix(),
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


SAN_MEDIA_WEB = BASE_DIR / "san_khoa_media"  # ảnh giáo trình Sản phải nằm trong web root mới hiển thị được
IMG_LINK_RE = re.compile(r"\]\(media/([^)]+)\)")


def scan_obgyn_files(san_dir: Path) -> list[dict]:
    index_file = san_dir / "index.json"
    if not index_file.exists():
        raise SystemExit(f"[BLOCK] không thấy nguồn Sản khoa {index_file} — dừng để không ghi đè data.js "
                         f"thành bản mất mục Sản khoa. Dùng --san-dir nếu nguồn ở chỗ khác.")
    lessons, used_media = [], set()
    for item in json.loads(index_file.read_text(encoding="utf-8")):
        md_path, json_path = san_dir / item["md_path"], san_dir / item["json_path"]
        if not md_path.exists():
            raise SystemExit(f"[BLOCK] Sản khoa {item['id']}: thiếu {md_path}")
        meta = {}
        if json_path.exists():
            meta = json.loads(json_path.read_text(encoding="utf-8"))
        content = md_path.read_text(encoding="utf-8")
        for rel in IMG_LINK_RE.findall(content):
            if not (san_dir / "media" / rel).is_file():
                raise SystemExit(f"[BLOCK] Sản khoa {item['id']}: thiếu ảnh media/{rel}")
            used_media.add(rel)
        lessons.append({
            "id": item["id"], "specialty": "obgyn", "specialty_name": "Sản Phụ Khoa",
            "chapter": item["chapter"], "folder": item["folder"], "title": item["title"],
            "author": item.get("author", "Bộ môn Phụ Sản ĐHYD Thái Bình"), "word_count": item.get("word_count", 0),
            "content": IMG_LINK_RE.sub(lambda m: f"]({SAN_MEDIA_WEB.name}/{m.group(1)})", content),
            "key_numbers": meta.get("key_numbers", []), "key_drugs": meta.get("key_drugs", []),
            "md_path": item["md_path"],
        })
    if not lessons:
        raise SystemExit(f"[BLOCK] {index_file} không có bài Sản khoa nào")
    sync_media(san_dir / "media", used_media)
    return lessons


def sync_media(src_root: Path, used: set[str]) -> None:
    """Chép ảnh Sản đang được dùng vào web root; xóa ảnh không còn bài nào trỏ tới."""
    for rel in used:
        src, dst = src_root / rel, SAN_MEDIA_WEB / rel
        if not dst.exists() or dst.stat().st_size != src.stat().st_size:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    if SAN_MEDIA_WEB.exists():
        for f in SAN_MEDIA_WEB.rglob("*"):
            if f.is_file() and f.relative_to(SAN_MEDIA_WEB).as_posix() not in used:
                f.unlink()




def scan_hoasinh_files(hoasinh_dir: Path) -> list[dict]:
    index_file = hoasinh_dir / "index.json"
    if not index_file.exists():
        return []
    hs_media_src = hoasinh_dir / "media"
    hs_media_web = BASE_DIR / "hoasinh_media"
    if hs_media_src.exists():
        hs_media_web.mkdir(parents=True, exist_ok=True)
        for f in hs_media_src.glob("*.*"):
            dst = hs_media_web / f.name
            if not dst.exists() or dst.stat().st_size != f.stat().st_size:
                shutil.copy2(f, dst)
    lessons = []
    items = json.loads(index_file.read_text(encoding="utf-8"))
    for item in items:
        md_path = hoasinh_dir / item.get("md_path", "")
        content = ""
        if md_path.exists():
            content = md_path.read_text(encoding="utf-8")
        json_path = hoasinh_dir / item.get("json_path", "")
        meta = {}
        if json_path.exists():
            try:
                meta = json.loads(json_path.read_text(encoding="utf-8"))
            except Exception:
                pass
        folder_rel = Path(os.path.relpath(hoasinh_dir, BASE_DIR)).as_posix()
        norm_content = normalize_image_paths(content, folder_rel)
        lessons.append({
            "id": item["id"],
            "specialty": "hoasinh",
            "specialty_name": "Hóa Sinh Y Khoa",
            "part": item.get("part", "Phần I: Cấu tạo và Chuyển hóa chất"),
            "chapter": item.get("chapter", ""),
            "title": item.get("title", ""),
            "author": item.get("author", "GS.TS. Tạ Thành Văn (Chủ biên) — ĐHY Hà Nội"),
            "pages": f"{item.get('start_page', '')}-{item.get('end_page', '')}",
            "word_count": item.get("word_count", len(norm_content.split())),
            "content": norm_content,
            "key_numbers": meta.get("key_numbers", item.get("key_numbers", [])),
            "key_points": meta.get("key_points", item.get("key_points", [])),
            "folder_rel": "",
        })
    return lessons

def docx_to_markdown(docx_path: Path) -> str:
    try:
        import docx
    except ImportError:
        return ""
    doc = docx.Document(str(docx_path))
    lines = []
    for element in doc.element.body:
        if element.tag.endswith('p'):
            p = docx.text.paragraph.Paragraph(element, doc)
            text = ""
            for run in p.runs:
                r_text = run.text
                if not r_text:
                    continue
                if run.bold and run.italic:
                    r_text = f"***{r_text}***"
                elif run.bold:
                    r_text = f"**{r_text}**"
                elif run.italic:
                    r_text = f"*{r_text}*"
                text += r_text
            text = text.strip()
            if not text:
                continue
            style_name = p.style.name.lower()
            if "title" in style_name:
                lines.append(f"# {text}\n")
            elif "heading 1" in style_name:
                lines.append(f"## {text}\n")
            elif "heading 2" in style_name:
                lines.append(f"### {text}\n")
            elif "heading 3" in style_name:
                lines.append(f"#### {text}\n")
            elif "bullet" in style_name:
                lines.append(f"- {text}")
            else:
                lines.append(f"{text}\n")
        elif element.tag.endswith('tbl'):
            table = docx.table.Table(element, doc)
            if not table.rows:
                continue
            table_lines = []
            header_cells = [cell.text.replace("\n", " ").strip() for cell in table.rows[0].cells]
            table_lines.append("| " + " | ".join(header_cells) + " |")
            table_lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
            for row in table.rows[1:]:
                row_cells = [cell.text.replace("\n", " ").strip() for cell in row.cells]
                if len(row_cells) < len(header_cells):
                    row_cells += [""] * (len(header_cells) - len(row_cells))
                table_lines.append("| " + " | ".join(row_cells[:len(header_cells)]) + " |")
            lines.append("\n" + "\n".join(table_lines) + "\n")
    return "\n".join(lines)


def extract_clinical_title(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        t = m.group(1).strip()
        t = re.sub(r"^(BÀI HỌC[:\s]*|BÀI GIẢNG[:\s]*|BÀI HỌC Y KHOA[:\s]*|CHUYÊN ĐỀ[:\s]*)", "", t, flags=re.IGNORECASE).strip()
        t = re.sub(r"\s*[-–—]\s*\d{4}[-/]\d{2}[-/]\d{2}.*$", "", t).strip()
        return t
    return fallback


def count_clinical_cards(folder: Path) -> int:
    card_files = [f for f in folder.iterdir() if "card" in f.name.lower() and f.suffix.lower() == ".json"]
    if card_files:
        try:
            d = json.loads(card_files[0].read_text(encoding="utf-8"))
            cards = d.get("cards", []) if isinstance(d, dict) else d
            return len(cards)
        except Exception:
            pass
    apkgs = [f for f in folder.iterdir() if f.suffix.lower() == ".apkg"]
    if apkgs:
        m = re.search(r"(\d+)\s*cards?", apkgs[0].name, re.IGNORECASE)
        if m:
            return int(m.group(1))
    return 0


def pick_best_docx(d: Path) -> Path | None:
    docxs = [f for f in d.iterdir() if f.suffix.lower() == ".docx"]
    if not docxs:
        return None
    if len(docxs) == 1:
        return docxs[0]
    import unicodedata
    def norm(text: str) -> set:
        text = unicodedata.normalize('NFD', text.lower())
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn').replace('đ', 'd')
        return {t for t in re.sub(r'[^a-z0-9]+', ' ', text).split() if len(t) >= 3 and t not in {'2026', 'docx', 'bai', 'hoc'}}
    d_tokens = norm(d.name)
    scored = []
    for doc in docxs:
        score = len(norm(doc.name) & d_tokens)
        scored.append((score, doc.stat().st_size, doc))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return scored[0][2]


def scan_clinical_san(san_dir: Path) -> list[dict]:
    if not san_dir.exists():
        return []
    lessons = []
    chapter_map = {
        "01": "Bệnh lý Phụ khoa & Tử cung",
        "02": "Bệnh lý Phụ khoa & Tử cung",
        "03": "Sản khoa & Chuyển dạ",
        "04": "Bệnh lý Phụ khoa & Tử cung",
        "05": "Sản khoa & Chuyển dạ",
        "06": "Bệnh lý Phụ khoa & Tử cung",
        "07_De_chi_huy": "Sản khoa & Chuyển dạ",
        "07_U_xo": "Bệnh lý Phụ khoa & Tử cung",
        "22": "Nội tiết Sinh sản & Tránh thai",
        "33": "Siêu âm Phụ khoa (TVS)",
        "34": "Siêu âm Phụ khoa (TVS)",
        "35": "Siêu âm Phụ khoa (TVS)",
        "36": "Nội tiết Sinh sản & Tránh thai",
        "37": "Nội tiết Sinh sản & Tránh thai",
        "38": "Bệnh lý Phụ khoa & Tử cung",
        "39": "Bệnh lý Phụ khoa & Tử cung",
    }
    for d in sorted(san_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        m = re.match(r"^(\d+)", d.name)
        num_str = m.group(1) if m else "00"
        if d.name.startswith("07_De_chi_huy"):
            lid = "OB-07"
            ch = chapter_map["07_De_chi_huy"]
        elif d.name.startswith("07_U_xo"):
            lid = "OB-07B"
            ch = chapter_map["07_U_xo"]
        else:
            lid = f"OB-{int(num_str):02d}"
            ch = chapter_map.get(num_str, "Sản Phụ khoa Lâm sàng")
        content = ""
        if d.name == "39_U_xo_tu_cung_ART_Infertility":
            mfile = d / "U_xo_tu_cung_ART_Infertility_2026-07-12.md"
            if mfile.exists():
                content = mfile.read_text(encoding="utf-8", errors="ignore")
        if not content:
            mds = [f for f in d.rglob("*.md") if not any(x in f.name for x in ["knowledge_check", "research", "audit"])]
            if mds:
                content = mds[0].read_text(encoding="utf-8", errors="ignore")
            else:
                best_doc = pick_best_docx(d)
                if best_doc:
                    content = docx_to_markdown(best_doc)
        if not content.strip():
            continue
        fallback = d.name.split("_", 1)[1].replace("_", " ") if "_" in d.name else d.name
        title = extract_clinical_title(content, fallback)
        n_cards = count_clinical_cards(d)
        lessons.append({
            "id": lid,
            "specialty": "san",
            "specialty_name": "Sản Phụ Khoa",
            "chapter": ch,
            "folder": d.name,
            "title": title,
            "author": "Đỗ Văn Ngọc Hưng",
            "word_count": len(content.split()),
            "cards_count": n_cards,
            "has_cards": n_cards > 0,
            "content": content,
            "folder_rel": "",
        })
    return lessons


def scan_clinical_art(art_dir: Path) -> list[dict]:
    if not art_dir.exists():
        return []
    lessons = []
    chapter_map = {
        "01": "Quản lý Thai sau ART",
        "02": "Pha Hoàng thể & Tiếp nhận Nội mạc",
        "03": "Phác đồ Chuyên sâu & Bệnh lý",
        "04": "Kích thích Buồng trứng (COS) & Trigger",
        "05": "Kích thích Buồng trứng (COS) & Trigger",
        "06": "Quản lý Thai sau ART",
        "07": "Hội chứng Quá kích Buồng trứng (OHSS)",
        "08": "Pha Hoàng thể & Tiếp nhận Nội mạc",
        "09": "Phác đồ Chuyên sâu & Bệnh lý",
        "10": "Phác đồ Chuyên sâu & Bệnh lý",
        "11": "Pha Hoàng thể & Tiếp nhận Nội mạc",
        "12": "Pha Hoàng thể & Tiếp nhận Nội mạc",
        "13": "Phác đồ Chuyên sâu & Bệnh lý",
        "14": "Kích thích Buồng trứng (COS) & Trigger",
        "15": "Kích thích Buồng trứng (COS) & Trigger",
        "16": "Phác đồ Chuyên sâu & Bệnh lý",
        "17": "Kích thích Buồng trứng (COS) & Trigger",
        "18": "Kích thích Buồng trứng (COS) & Trigger",
        "19": "Phác đồ Chuyên sâu & Bệnh lý",
        "21": "Hội chứng Quá kích Buồng trứng (OHSS)",
        "22": "Pha Hoàng thể & Tiếp nhận Nội mạc",
        "32": "Phác đồ Chuyên sâu & Bệnh lý",
        "33": "Kích thích Buồng trứng (COS) & Trigger",
        "41": "Kích thích Buồng trứng (COS) & Trigger",
        "42": "Vô sinh Nam & Đánh giá Nội tiết",
        "43": "Vô sinh Nam & Đánh giá Nội tiết",
        "44": "Vô sinh Nam & Đánh giá Nội tiết",
        "46": "Phác đồ Chuyên sâu & Bệnh lý",
    }
    for d in sorted(art_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        m = re.match(r"^(\d+)", d.name)
        num_str = m.group(1) if m else "00"
        lid = f"ART-{int(num_str):02d}"
        ch = chapter_map.get(num_str, "Hỗ trợ Sinh sản ART")
        content = ""
        if d.name == "46_Endometrioma_Adenomyosis_ART_Infertility":
            mfile = d / "46_Endometrioma_Adenomyosis_ART_Infertility.md"
            if mfile.exists():
                content = mfile.read_text(encoding="utf-8", errors="ignore")
        if not content:
            mds = [f for f in d.iterdir() if f.suffix.lower() == ".md" and not any(x in f.name for x in ["knowledge_check", "research", "audit"])]
            if mds:
                content = mds[0].read_text(encoding="utf-8", errors="ignore")
            else:
                best_doc = pick_best_docx(d)
                if best_doc:
                    content = docx_to_markdown(best_doc)
        if not content.strip():
            continue
        fallback = d.name.split("_", 1)[1].replace("_", " ") if "_" in d.name else d.name
        title = extract_clinical_title(content, fallback)
        n_cards = count_clinical_cards(d)
        lessons.append({
            "id": lid,
            "specialty": "art",
            "specialty_name": "Hỗ trợ Sinh sản (ART)",
            "chapter": ch,
            "folder": d.name,
            "title": title,
            "author": "Đỗ Văn Ngọc Hưng",
            "word_count": len(content.split()),
            "cards_count": n_cards,
            "has_cards": n_cards > 0,
            "content": content,
            "folder_rel": "",
        })
    return lessons


def scan_clinical_fus(fus_dir: Path) -> list[dict]:
    if not fus_dir.exists():
        return []
    lessons = []
    chapter_map = {
        "01": "Siêu âm Tim thai (Fetal Echo)",
        "02": "Khảo sát Hình thái & Giải phẫu thai",
        "03": "Bánh nhau, Nước ối & Nhiễm trùng thai",
        "04": "Khảo sát Hình thái & Giải phẫu thai",
        "05": "Siêu âm Tim thai (Fetal Echo)",
        "06": "Siêu âm Tim thai (Fetal Echo)",
        "07": "Hệ Thần kinh thai (Fetal Neurosonography)",
        "08": "Khảo sát Hình thái & Giải phẫu thai",
        "09_Cervical": "Sinh trắc, Doppler & Sàng lọc Quý 1",
        "09_Sinh_trac": "Sinh trắc, Doppler & Sàng lọc Quý 1",
        "10": "Sinh trắc, Doppler & Sàng lọc Quý 1",
        "11": "Sinh trắc, Doppler & Sàng lọc Quý 1",
        "12": "Sinh trắc, Doppler & Sàng lọc Quý 1",
        "35": "Khảo sát Hình thái & Giải phẫu thai",
        "36": "Khảo sát Hình thái & Giải phẫu thai",
        "37": "Khảo sát Hình thái & Giải phẫu thai",
        "38": "Khảo sát Hình thái & Giải phẫu thai",
        "39": "Khảo sát Hình thái & Giải phẫu thai",
        "40": "Bánh nhau, Nước ối & Nhiễm trùng thai",
        "41": "Khảo sát Hình thái & Giải phẫu thai",
        "43": "Bánh nhau, Nước ối & Nhiễm trùng thai",
        "44": "Khảo sát Hình thái & Giải phẫu thai",
    }
    for d in sorted(fus_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        m = re.match(r"^(\d+)", d.name)
        num_str = m.group(1) if m else "00"
        if d.name.startswith("42_Twin_Pregnancy"):
            twin_modules = [
                ("D1_Chorionicity_Amnionicity", "FUS-42A", "Song thai D1 — Xác định Chorionicity & Amnionicity"),
                ("D2_MCMA", "FUS-42B", "Song thai D2 — MCMA: Song thai 1 buồng ối"),
                ("D3_MCDA_TTTS_TAPS_sIUGR", "FUS-42C", "Song thai D3 — MCDA: TTTS, TAPS, sIUGR"),
                ("D4_DCDA_Monitoring", "FUS-42D", "Song thai D4 — DCDA: Theo dõi, Biến chứng & Sinh"),
            ]
            for sub_name, tid, t_fallback in twin_modules:
                sub_dir = d / sub_name
                if not sub_dir.exists():
                    continue
                s_mds = [f for f in sub_dir.iterdir() if f.suffix.lower() == ".md" and not any(x in f.name for x in ["knowledge_check", "research", "audit"])]
                if s_mds:
                    s_content = s_mds[0].read_text(encoding="utf-8", errors="ignore")
                else:
                    best_doc = pick_best_docx(sub_dir)
                    s_content = docx_to_markdown(best_doc) if best_doc else ""
                if not s_content.strip():
                    continue
                t_title = extract_clinical_title(s_content, t_fallback)
                n_cards = count_clinical_cards(sub_dir)
                lessons.append({
                    "id": tid,
                    "specialty": "fus",
                    "specialty_name": "Siêu Âm Thai",
                    "chapter": "Song thai (Twin Pregnancy)",
                    "folder": f"{d.name}/{sub_name}",
                    "title": t_title,
                    "author": "Đỗ Văn Ngọc Hưng",
                    "word_count": len(s_content.split()),
                    "cards_count": n_cards,
                    "has_cards": n_cards > 0,
                    "content": s_content,
                    "folder_rel": "",
                })
            continue
        elif d.name.startswith("09_Cervical"):
            lid = "FUS-09A"
            ch = chapter_map["09_Cervical"]
        elif d.name.startswith("09_Sinh_trac"):
            lid = "FUS-09B"
            ch = chapter_map["09_Sinh_trac"]
        else:
            lid = f"FUS-{int(num_str):02d}"
            ch = chapter_map.get(num_str, "Siêu âm Thai")
        content = ""
        mds = [f for f in d.iterdir() if f.suffix.lower() == ".md" and not any(x in f.name for x in ["knowledge_check", "research", "audit"])]
        if mds:
            content = mds[0].read_text(encoding="utf-8", errors="ignore")
        else:
            best_doc = pick_best_docx(d)
            if best_doc:
                content = docx_to_markdown(best_doc)
        if not content.strip():
            continue
        fallback = d.name.split("_", 1)[1].replace("_", " ") if "_" in d.name else d.name
        title = extract_clinical_title(content, fallback)
        n_cards = count_clinical_cards(d)
        lessons.append({
            "id": lid,
            "specialty": "fus",
            "specialty_name": "Siêu Âm Thai",
            "chapter": ch,
            "folder": d.name,
            "title": title,
            "author": "Đỗ Văn Ngọc Hưng",
            "word_count": len(content.split()),
            "cards_count": n_cards,
            "has_cards": n_cards > 0,
            "content": content,
            "folder_rel": "",
        })
    return lessons


def build_payload(san_dir: Path, hoasinh_dir: Path, clin_san_dir: Path, clin_art_dir: Path, clin_fus_dir: Path, version: str, generated_at: str) -> dict:
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
            continue
        ped_lessons.append({
            **item, "specialty": "ped", "specialty_name": "Nhi Khoa",
            "has_ped": has_ped, "has_pedytb": has_pedytb, "has_cards": disc.get("cards_count", 0) > 0,
            "ped_file": disc.get("ped_file"), "ped_content": disc.get("ped_content", ""),
            "pedytb_file": disc.get("pedytb_file"), "pedytb_content": disc.get("pedytb_content", ""),
            "cards_count": disc.get("cards_count", 0),
            "apkg_file": disc.get("apkg_file"), "html_file": disc.get("html_file"),
            "folder_rel": disc.get("folder_rel", ""),
        })
    obgyn_lessons = scan_obgyn_files(san_dir)
    obgyn_chapters = list(dict.fromkeys(lesson["chapter"] for lesson in obgyn_lessons))
    hoasinh_lessons = scan_hoasinh_files(hoasinh_dir)
    hoasinh_chapters = list(dict.fromkeys(lesson["chapter"] for lesson in hoasinh_lessons))
    
    # New clinical specialties
    san_clinical_lessons = scan_clinical_san(clin_san_dir)
    san_clinical_chapters = list(dict.fromkeys(lesson["chapter"] for lesson in san_clinical_lessons))
    art_lessons = scan_clinical_art(clin_art_dir)
    art_chapters = list(dict.fromkeys(lesson["chapter"] for lesson in art_lessons))
    fus_lessons = scan_clinical_fus(clin_fus_dir)
    fus_chapters = list(dict.fromkeys(lesson["chapter"] for lesson in fus_lessons))
    
    total_all = len(ped_lessons) + len(obgyn_lessons) + len(hoasinh_lessons) + len(san_clinical_lessons) + len(art_lessons) + len(fus_lessons)
    
    return {
        "metadata": {
            "title": "HungMed · Cẩm Nang Lâm Sàng & Giáo Trình Y Khoa",
            "author": "Đỗ Văn Ngọc Hưng",
            "version": version,
            "generated_at": generated_at,
            "total_curriculum": len(curriculum),
            "total_ped": len(ped_lessons),
            "total_ped_standard": sum(lesson["has_ped"] for lesson in ped_lessons),
            "total_pedytb": sum(lesson["has_pedytb"] for lesson in ped_lessons),
            "total_cards": sum(lesson["cards_count"] for lesson in ped_lessons),
            "total_obgyn": len(obgyn_lessons),
            "total_hoasinh": len(hoasinh_lessons),
            "total_san": len(san_clinical_lessons),
            "total_art": len(art_lessons),
            "total_fus": len(fus_lessons),
            "total_all": total_all,
            "blocks": PED_BLOCKS,
            "ped_blocks": PED_BLOCKS,
            "obgyn_chapters": obgyn_chapters,
            "hoasinh_chapters": hoasinh_chapters,
            "san_chapters": san_clinical_chapters,
            "art_chapters": art_chapters,
            "fus_chapters": fus_chapters,
        },
        "curriculum": curriculum_summary,
        "ped": ped_lessons,
        "obgyn": obgyn_lessons,
        "hoasinh": hoasinh_lessons,
        "san": san_clinical_lessons,
        "art": art_lessons,
        "fus": fus_lessons,
    }
def write_outputs(payload: dict) -> None:
    version = payload["metadata"]["version"]
    js = ("/* Auto-generated by build_unified_med_library.py — KHÔNG sửa tay */\n"
          "window.HUNG_MED_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n"
          "window.PED_LIBRARY_DATA = { metadata: window.HUNG_MED_DATA.metadata, "
          "curriculum: window.HUNG_MED_DATA.curriculum, lessons: window.HUNG_MED_DATA.ped };\n"
          "window.SAN_KHOA_DATA = window.HUNG_MED_DATA.obgyn;\n"
          "/* lesson.content của bài Nhi = PED chuẩn, không có thì sách YTB — gán bằng tham chiếu, không lưu 2 lần */\n"
          "window.HUNG_MED_DATA.ped.forEach(function (l) { l.content = l.ped_content || l.pedytb_content; });\n")
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
    ap.add_argument("--hoasinh-dir", type=Path, default=DEFAULT_HOASINH_DIR, help="thư mục Hóa sinh (có index.json)")
    ap.add_argument("--clin-san-dir", type=Path, default=DEFAULT_CLINICAL_SAN_DIR, help="thư mục Sản phụ khoa lâm sàng")
    ap.add_argument("--clin-art-dir", type=Path, default=DEFAULT_CLINICAL_ART_DIR, help="thư mục Hỗ trợ sinh sản ART")
    ap.add_argument("--clin-fus-dir", type=Path, default=DEFAULT_CLINICAL_FUS_DIR, help="thư mục Siêu âm thai")
    args = ap.parse_args(argv)
    now = datetime.now()
    payload = build_payload(args.san_dir, args.hoasinh_dir, args.clin_san_dir, args.clin_art_dir, args.clin_fus_dir, now.strftime("%Y%m%d_%H%M%S"), now.strftime("%Y-%m-%d %H:%M:%S"))
    write_outputs(payload)
    m = payload["metadata"]
    print(f"[OK] data.js v{m['version']} ({DATA_JS_PATH.stat().st_size / 1e6:.2f} MB): "
          f"Tổng {m['total_all']} bài (Nhi {m['total_ped']} · Sản YTB {m['total_obgyn']} · Hóa sinh {m['total_hoasinh']} · "
          f"Sản LS {m['total_san']} · ART {m['total_art']} · Siêu âm thai {m['total_fus']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
