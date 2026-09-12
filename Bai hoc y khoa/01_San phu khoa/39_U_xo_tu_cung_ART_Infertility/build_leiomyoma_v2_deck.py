# -*- coding: utf-8 -*-
"""Build a Vietnamese personal-note leiomyoma ART deck from the approved DOCX.

Storyline (user-defined order):
1. Định nghĩa
2. Cơ chế bệnh sinh
3. Phân loại
4. Triệu chứng
5. Chẩn đoán
6. Cơ chế ảnh hưởng ART
7. Xử trí theo FIGO
8. Phương pháp điều trị
9. Thứ tự ART, theo dõi và bằng chứng

No page numbers in the rendered deck. No author/footer signature. Every
non-structural slide maps back to DOCX paragraph/table IDs.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from docx import Document

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).parent
DATE = "2026-07-14"
SOURCE_DOCX = ROOT / "U_xo_tu_cung_ART_Infertility_2026-07-12.docx"
OUT = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.deck.json"
PROV_OUT = ROOT / f"U_xo_tu_cung_leiomyoma_v2_personal_{DATE}.provenance.json"

EXPECTED_TABLES = 26
MIN_PARAGRAPHS = 280
FORBIDDEN_SOURCE_NAMES = [
    "Quá trình mổ u xơ", "Giải thích các bước phẫu thuật u xơ",
    "Hạn chế dính buồng tử cung", "PMC13278667_fulltext", ".md", ".txt",
]

slides: list[dict] = []
manifest_slides: list[dict] = []


@dataclass(frozen=True)
class Block:
    id: str
    kind: str
    text: str
    heading: str = ""
    table_index: int | None = None
    row_index: int | None = None


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iter_block_items(doc: Document):
    """Yield paragraphs and tables in document order."""
    from docx.oxml.table import CT_Tbl
    from docx.oxml.text.paragraph import CT_P
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    body = doc.element.body
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)


def table_to_rows(table) -> list[list[str]]:
    rows = []
    for row in table.rows:
        rows.append([" ".join(cell.text.split()) for cell in row.cells])
    return rows


def extract_docx_blocks(path: Path) -> tuple[list[Block], dict[str, list[list[str]]]]:
    if path.resolve() != SOURCE_DOCX.resolve():
        raise SystemExit(f"Refuse non-approved source: {path}")
    doc = Document(path)
    blocks: list[Block] = []
    tables: dict[str, list[list[str]]] = {}
    p_i = 0
    t_i = 0
    current_heading = ""
    for item in iter_block_items(doc):
        if item.__class__.__name__ == "Paragraph":
            text = " ".join((item.text or "").split())
            if not text:
                continue
            p_i += 1
            bid = f"P{p_i:03d}"
            style_name = getattr(item.style, "name", "") or ""
            if style_name.lower().startswith("heading") or text.startswith(
                ("0.", "1.", "2.", "2A.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")
            ):
                current_heading = text
            blocks.append(Block(bid, "paragraph", text, current_heading))
        else:
            t_i += 1
            tid = f"T{t_i}"
            rows = table_to_rows(item)
            tables[tid] = rows
            joined = " | ".join(" / ".join(r) for r in rows)
            blocks.append(Block(tid, "table", joined, current_heading, t_i))
            for r_i, row in enumerate(rows, 1):
                blocks.append(Block(f"{tid}R{r_i:02d}", "table_row", " | ".join(row), current_heading, t_i, r_i))
    if p_i < MIN_PARAGRAPHS:
        raise SystemExit(f"DOCX extraction too thin: {p_i} paragraphs (<{MIN_PARAGRAPHS})")
    if t_i != EXPECTED_TABLES:
        raise SystemExit(f"DOCX table count mismatch: {t_i} (expected {EXPECTED_TABLES})")
    for tid in ["T3", "T5", "T11", "T15", "T20", "T21", "T24"]:
        if tid not in tables:
            raise SystemExit(f"Missing required backbone table: {tid}")
    return blocks, tables


BLOCKS, TABLES = extract_docx_blocks(SOURCE_DOCX)
BLOCK_BY_ID = {b.id: b for b in BLOCKS}
DOCX_HASH = sha256(SOURCE_DOCX)
ALL_DOCX_TEXT = "\n".join(b.text for b in BLOCKS)


def pmids_from_text(text: str) -> list[str]:
    return sorted(set(re.findall(r"\bPMID\s*[: ]?\s*(\d{6,9})\b", text, flags=re.I)))


def dois_from_text(text: str) -> list[str]:
    return sorted(set(re.findall(r"\b10\.\d{4,9}/[^\s;,)]+", text)))


def pmids_for(source_ids: Iterable[str]) -> list[str]:
    text = "\n".join(BLOCK_BY_ID[sid].text for sid in source_ids if sid in BLOCK_BY_ID)
    return pmids_from_text(text)


def snippets_for(source_ids: Iterable[str], limit: int = 220) -> list[dict]:
    out = []
    for sid in source_ids:
        b = BLOCK_BY_ID.get(sid)
        if not b:
            raise SystemExit(f"Unknown source ID: {sid}")
        out.append({"id": sid, "kind": b.kind, "heading": b.heading, "snippet": b.text[:limit]})
    return out


def note(action: str, why: str, risk: str, source_ids: list[str]) -> str:
    src = ", ".join(source_ids)
    return (
        f"Làm gì? {action}\n"
        f"Tại sao? {why}\n"
        f"Nếu bỏ qua/làm sai? {risk or 'Dễ áp dụng máy móc hoặc quyết định không khớp mục tiêu ART.'}\n"
        f"Nguồn DOCX: {src}"
    )


def add(kind: str, *, title: str = "", source_ids: list[str] | None = None,
        action: str = "Trình bày ý chính.",
        why: str = "Giúp học viên ra quyết định lâm sàng.",
        risk: str = "", **kw) -> dict:
    source_ids = source_ids or []
    structural = kind in {"title", "section", "outline", "reference"}
    if not structural and not source_ids:
        raise SystemExit(f"Slide content missing source_ids: {title}")
    for sid in source_ids:
        if sid not in BLOCK_BY_ID:
            raise SystemExit(f"Slide {title!r} references missing source {sid}")
    slide = {"type": kind}
    if title:
        slide["title"] = title
    slide.update(kw)
    if kind not in {"title", "outline", "section", "reference"}:
        slide["note"] = note(action, why, risk, source_ids)
    slides.append(slide)
    manifest_slides.append({
        "slide_index": len(slides),
        "title": title or kw.get("part_title", kw.get("subtitle", kind)),
        "type": kind,
        "source_docx": str(SOURCE_DOCX),
        "source_docx_sha256": DOCX_HASH,
        "source_ids": source_ids,
        "source_summary": why if source_ids else "structural slide",
        "pmids": pmids_for(source_ids),
        "dois": dois_from_text("\n".join(BLOCK_BY_ID[sid].text for sid in source_ids if sid in BLOCK_BY_ID)),
        "snippets": snippets_for(source_ids) if source_ids else [],
        "image_policy": "no embedded factual image; native shapes/tables only",
    })
    return slide


def title_slide():
    add("title", variant="centered_minimal", title="U xơ cơ tử cung và ART/IVF",
        subtitle="Ghi chú cá nhân · Từ định nghĩa đến quyết định ART", date=DATE)


def section(num: int, heading: str, sub: str):
    add("section", variant="number_block", part_number=str(num), part_title=heading, part_subtitle=sub)


def content(title: str, points: list[str], src: list[str], action: str, why: str, risk: str = "", numbered: bool = False):
    add("content", variant="numbered" if numbered else "bullets", title=title, points=points,
        source_ids=src, action=action, why=why, risk=risk)


def two_col(title: str, left_title: str, left: list[str], right_title: str, right: list[str],
            src: list[str], action: str, why: str, risk: str = "", vs: bool = False):
    add("two_column", variant="vs_compare" if vs else "cards", title=title,
        left_title=left_title, left_points=left, right_title=right_title, right_points=right,
        source_ids=src, action=action, why=why, risk=risk)


def three_col(title: str, columns: list[dict], src: list[str], action: str, why: str, risk: str = ""):
    add("three_column", variant="pillars", title=title, columns=columns,
        source_ids=src, action=action, why=why, risk=risk)


def mechanism(title: str, steps: list[tuple[str, str]], src: list[str], action: str, why: str, risk: str = "", outcome: str = ""):
    add("mechanism", variant="horizontal_steps", title=title,
        steps=[{"title": a, "description": b} for a, b in steps],
        outcome=outcome or why,
        source_ids=src, action=action, why=why, risk=risk)


def algorithm(title: str, steps: list[str], src: list[str], action: str, why: str, risk: str = ""):
    add("algorithm", variant="linear_flow", title=title,
        nodes=[{"text": s, "type": "start" if i == 0 else "end" if i == len(steps)-1 else "process"} for i, s in enumerate(steps)],
        source_ids=src, action=action, why=why, risk=risk)


def table_slide(title: str, headers: list[str], rows: list[list[str]], src: list[str],
                action: str, why: str, risk: str = "", footnote: str = ""):
    add("table", variant="standard", title=title, headers=headers, rows=rows,
        source_ids=src, action=action, why=why, risk=risk, footnote=footnote)


def definition_slide(term: str, definition: str, src: list[str], action: str, why: str):
    add("definition", variant="term_box", title="Định nghĩa", term=term, definition=definition,
        source_ids=src, action=action, why=why)


def glossary_slide(title: str, entries: list[dict], src: list[str], action: str, why: str):
    add("definition", variant="glossary_table", title=title, entries=entries,
        source_ids=src, action=action, why=why)


def summary_slide(title: str, points: list[str], src: list[str],
                  action: str = "Tổng hợp thông điệp cần nhớ.",
                  why: str = "Tóm tắt giúp chuyển kiến thức thành hành động."):
    add("summary", variant="takeaways", title=title, points=points,
        source_ids=src, action=action, why=why)


def case_slide(title: str, vignette: str, question: str, pearl: str, src: list[str]):
    add("qa_clinical", variant="pearl_card", title=title, question=question, pearl=pearl,
        why="Dùng ca lâm sàng để kiểm tra quyết định, không học thuộc máy móc.",
        source_ids=src, action="Thảo luận ca đại diện.",
        risk="Không đặt ca vào thuật toán sẽ dễ chọn mổ/IVF theo phản xạ.")


def qa_mcq_slide(title: str, stem: str, options: list[str], answer: str, src: list[str],
                 pearl: str, why: str):
    add("qa_clinical", variant="mcq_5option", title=title,
        question=stem, options=options, answer=answer, show_answer=True,
        source_ids=src, action="Đặt câu hỏi và đáp án để tự kiểm.",
        why=why, risk=pearl)


def kpi_slide(title: str, stats: list[dict], src: list[str], action: str, why: str,
              risk: str = ""):
    """big_number KPI strip."""
    add("big_number", variant="multi_kpi", title=title, stats=stats,
        source_ids=src, action=action, why=why, risk=risk)


def kpi_hero_slide(title: str, stat: dict, src: list[str], action: str, why: str,
                   trend: dict | None = None, risk: str = ""):
    add("big_number", variant="with_trend" if trend else "single_hero",
        title=title, stats=[stat], trend=trend,
        source_ids=src, action=action, why=why, risk=risk)


def refs_slide():
    refs = []
    for b in BLOCKS:
        if b.heading.startswith("9.") or "PMID" in b.text or "DOI" in b.text:
            for part in re.split(r"(?<=\.)\s+", b.text):
                if "PMID" in part or "DOI" in part or "http" in part:
                    clean = part.strip()
                    if clean and clean not in refs:
                        refs.append(clean)
    if not refs:
        refs = ["Tài liệu tham khảo: xem phần 9 của DOCX nguồn."]
    add("references", variant="numbered", title="Tài liệu tham khảo từ DOCX nguồn",
        refs=refs[:12], source_ids=["P281"],
        action="Hiển thị nguồn chính đã có trong DOCX.",
        why="Không thêm reference từ ngoài DOCX.",
        risk="Thêm nguồn ngoài sẽ vi phạm phạm vi user yêu cầu.")


# Backbone compressed rows (kept in sync with the previous builder).
T3_ROWS = [
    ["0–2", "Dưới niêm mạc/làm biến dạng buồng tử cung", "Ưu tiên đánh giá và sửa buồng tử cung trước chuyển phôi"],
    ["3", "Chạm nội mạc, không lồi buồng tử cung", "Vùng xám trong ART"],
    ["4", "Trong cơ không chạm buồng tử cung", "Cá thể hóa theo từng ca"],
    ["5–7", "Dưới thanh mạc", "Thường không mổ chỉ vì chuẩn bị IVF"],
    ["8", "Vị trí đặc biệt (cổ tử cung, dây chằng, ký sinh)", "Cần lập bản đồ riêng"],
]
T5_ROWS = [
    ["Cao", "Type 0–2/biến dạng buồng tử cung", "Sửa buồng tử cung trước"],
    ["Trung gian", "Type 3/intramural chọn lọc", "Cá thể hóa"],
    ["Thấp hơn", "Dưới thanh mạc nhỏ", "Thường theo dõi"],
    ["Thuộc về thao tác", "Cản chọc hút noãn/chuyển phôi", "Xử trí theo đường vào ART"],
]
T11_ROWS = [
    ["Siêu âm qua ngã âm đạo 2D", "Bước đầu tiên", "Không đủ nếu buồng tử cung chưa rõ"],
    ["Siêu âm qua ngã âm đạo 3D", "Phân biệt type 3/4, dựng bản đồ buồng tử cung", "Cần kinh nghiệm người làm"],
    ["Bơm nước buồng tử cung (SIS)", "Làm rõ đường viền buồng tử cung", "Rất hữu ích trước chuyển phôi"],
    ["Nội soi buồng tử cung", "Chẩn đoán và xử trí tổn thương buồng", "Không khảo sát hết phần cơ tử cung"],
    ["Cộng hưởng từ (MRI)", "Đa u/nghi lạc nội mạc/dấu hiệu bất thường", "Không dùng thường quy"],
]
T15_ROWS = [
    ["0–2", "Làm biến dạng buồng tử cung", "Thường sửa buồng tử cung trước chuyển phôi"],
    ["3", "Chạm nội mạc không lồi buồng", "Hội chẩn và cá thể hóa"],
    ["4", "Không chạm buồng tử cung", "Cân bằng kích thước, tuổi, số phôi"],
    ["5–7", "Dưới thanh mạc", "Không mổ chỉ vì IVF nếu nhỏ"],
    ["8", "Vị trí đặc biệt", "MRI/kế hoạch riêng"],
]
T20_ROWS = [
    ["Nội soi buồng tử cung", "Type 0–2", "Sửa buồng tử cung, bảo vệ nội mạc"],
    ["Nội soi ổ bụng/mổ mở/robot", "Type 3–7 chọn lọc", "Sẹo, dính, thời gian chờ"],
    ["Theo dõi", "Không triệu chứng, buồng tử cung ổn", "Tránh trì hoãn ART"],
    ["Chụp lại hình ảnh", "Buồng tử cung chưa chắc chắn", "Trước chuyển phôi/khi phôi quý"],
]
T21_ROWS = [
    ["Tạo/trữ phôi trước", "Tuổi cao/AMH thấp, u chưa cản chọc hút noãn", "Bảo vệ tuổi noãn"],
    ["Xử trí u trước", "Buồng tử cung méo rõ, type 0–2 lớn", "Không chuyển phôi vào buồng tử cung xấu"],
    ["Đánh giá lại buồng tử cung", "Sau mổ hoặc sau can thiệp", "Chứng minh buồng tử cung trước chuyển phôi"],
]
T24_ROWS = [
    ["Sắt, NSAID, axit tranexamic", "Giảm triệu chứng và sửa thiếu máu", "Không sửa được buồng tử cung"],
    ["Nội tiết/GnRH", "Cầu nối trước mổ, giảm chảy máu", "Không chữa được cấu trúc"],
    ["Bóc u", "Có thể sửa buồng tử cung/lấy u", "Dính, sẹo, thời gian chờ"],
    ["Nút mạch, siêu âm hội tụ, đốt", "Giảm thể tích và triệu chứng", "Còn bất định về kết quả ART"],
]


def build_deck():
    # 0. Mở bài
    title_slide()
    add("objectives", variant="icon_check", title="Mục tiêu ghi chú cá nhân",
        objectives=[
            "Nắm u xơ cơ tử cung là gì, bệnh sinh và phân loại FIGO.",
            "Nhận diện triệu chứng và chọn công cụ chẩn đoán theo câu hỏi buồng tử cung.",
            "Giải thích cơ chế u xơ ảnh hưởng ART và vì sao buồng tử cung là lõi quyết định.",
            "Đề xuất thứ tự xử trí: theo dõi / thuốc / bóc u / tạo và trữ phôi / chuyển phôi.",
        ],
        source_ids=["P001", "P018"], action="Định hướng ghi chú cá nhân.",
        why="Ghi chú cá nhân cần rõ mục tiêu để biết chọn slide nào cần đọc kỹ.")
    add("outline", variant="tree", title="Lộ trình 9 phần",
        chapters=[
            {"title": "1. Định nghĩa", "sub": ["thuật ngữ", "dịch tễ"]},
            {"title": "2. Cơ chế bệnh sinh", "sub": ["nội tiết", "ECM", "biến thể"]},
            {"title": "3. Phân loại", "sub": ["FIGO", "type 3 vs 4", "tối thiểu cần mô tả"]},
            {"title": "4. Triệu chứng", "sub": ["AUB", "đau/chèn ép", "biến chứng thai kỳ"]},
            {"title": "5. Chẩn đoán", "sub": ["2D/3D", "SIS", "MRI", "report"]},
            {"title": "6. Cơ chế ảnh hưởng ART", "sub": ["buồng tử cung", "nội mạc", "co bóp"]},
            {"title": "7. Xử trí theo FIGO", "sub": ["type 0–8", "vùng xám"]},
            {"title": "8. Phương pháp điều trị", "sub": ["nội khoa", "phẫu thuật", "UAE/HIFU/RFA"]},
            {"title": "9. Thứ tự ART & theo dõi", "sub": ["tạo phôi", "thai kỳ", "evidence"]},
        ])

    # 1. Định nghĩa
    section(1, "Định nghĩa", "U xơ là gì, vì sao gặp nhiều trong ART")
    definition_slide(
        "U xơ cơ tử cung (leiomyoma)",
        "Khối u lành tính xuất phát từ cơ trơn tử cung, giàu chất nền ngoại bào, "
        "chịu ảnh hưởng nội tiết (estrogen + progesterone) nhưng không chỉ là bệnh 'do hormone'. "
        "Trong thực hành ART, u xơ phổ biến và thường phát hiện tình cờ khi khám hiếm muộn.",
        ["P038", "P043", "P045"],
        "Đặt nền khái niệm.",
        "Hiểu đúng bản chất tránh nhầm u xơ với lạc nội mạc, ung thư cơ trơn hoặc polyp nội mạc.")
    glossary_slide("Cách gọi và thuật ngữ", [
        {"term": "U xơ cơ tử cung", "definition": "Tên tiếng Việt thống nhất; tên tiếng Anh là u cơ trơn tử cung (leiomyoma, fibroid, myoma)."},
        {"term": "Dưới niêm mạc", "definition": "Type 0–2 FIGO; lồi vào buồng tử cung, ảnh hưởng trực tiếp khả năng làm tổ."},
        {"term": "Trong cơ", "definition": "Type 3–4 FIGO; ảnh hưởng tuỳ kích thước, vị trí và khoảng cách tới nội mạc."},
        {"term": "Dưới thanh mạc", "definition": "Type 5–7 FIGO; thường ít ảnh hưởng ART nếu nhỏ và không cản thao tác."},
        {"term": "Buồng tử cung", "definition": "Khoang nơi phôi làm tổ; chỉ một biến dạng nhỏ cũng có thể làm giảm tỉ lệ thành công."},
        {"term": "Lạc nội mạc tử cung", "definition": "Tuyến nội mạc trong cơ tử cung (tên tiếng Anh: adenomyosis); thường đi kèm hoặc nhầm với u xơ trong cơ."},
        {"term": "Polyp nội mạc", "definition": "Tổn thương dạng polyp trong buồng tử cung; cần phân biệt với u dưới niêm mạc."},
    ], ["P038", "P045"], "Việt hoá thuật ngữ chuẩn để dùng xuyên suốt ghi chú.",
        "Từ vựng thống nhất giúp đọc lại không bị nhầm.")
    content("Vì sao u xơ là chủ đề thường trực trong ART",
        ["U xơ gặp ở phần lớn phụ nữ tuổi sinh sản; phát hiện tình cờ qua siêu âm rất phổ biến.",
         "Trong IVF/FET, mối quan tâm không phải 'có hay không có u' mà là u nằm ở đâu, chạm/méo buồng tử cung không, có cản thao tác không.",
         "Bài note này tách u xơ thành ngôn ngữ ra quyết định thay vì một bệnh duy nhất."],
        ["P018", "P023", "P043"],
        "Đặt vấn đề đúng.",
        "Nếu cứ 'có u xơ là mổ' sẽ điều trị thừa rất nhiều.")
    content("Dịch tễ và yếu tố nguy cơ cần biết",
        ["Tuổi: tăng theo tuổi sinh sản, đỉnh quanh tiền mãn kinh.",
         "Chủng tộc/ancestry: phụ nữ da đen có tần suất và tuổi phát hiện sớm hơn.",
         "Tiền sử gia đình, nulliparity, béo phì, tăng huyết áp.",
         "Vitamin D thấp và một số yếu tố môi trường được đề cập.",
         "Thai kỳ thường thấy u xơ tăng kích thước; mãn kinh thường teo nhỏ."],
        ["P029", "P031", "P033", "P035"],
        "Liệt kê yếu tố nguy cơ.",
        "Biết nguy cơ giúp tiên lượng ca và tư vấn phòng ngừa.")
    content("Điểm nhớ cuối phần",
        ["Có u xơ không đồng nghĩa cần can thiệp.",
         "Câu hỏi đúng là: u này ảnh hưởng buồng tử cung, triệu chứng, thao tác ART hay thời gian noãn?",
         "Ghi chú tiếp theo sẽ đi qua cơ chế để hiểu vì sao vị trí quan trọng hơn kích thước."],
        ["P023", "P043"],
        "Tổng hợp quan điểm.",
        "Đây là ý chính nếu phải nhớ một câu của phần 1.")
    kpi_slide("Số liệu dịch tễ để đặt vấn đề",
        [
            {"number": "5–10%", "unit": "ở phụ nữ vô sinh", "label": "tỷ lệ có u xơ trên siêu âm"},
            {"number": "2–3%", "unit": "là nguyên nhân đơn độc", "label": "u xơ là nguyên nhân duy nhất của vô sinh"},
            {"number": ">80%", "unit": "ở người da đen", "label": "tích lũy đến 50 tuổi (Baird 2003)"},
            {"number": "~70%", "unit": "ở người da trắng", "label": "tích lũy đến 50 tuổi (Baird 2003)"},
        ],
        ["P027", "P029", "P031"],
        "Gắn số cho phần định nghĩa.",
        "Gặp u xơ nhiều không có nghĩa là phải mổ mọi u; nhưng đừng xem là hiếm.")

    # 2. Cơ chế bệnh sinh
    section(2, "Cơ chế bệnh sinh và sinh học u xơ", "Vì sao u phát triển, vì sao không cắt là xong")
    three_col("Ba trụ cột của bệnh sinh u xơ", [
        {"title": "Nội tiết", "points": ["Estrogen kích thích tăng trưởng.",
                                        "Progesterone là yếu tố then chốt trong tăng sinh u.",
                                        "Đó là lý do GnRH tạm thời nhỏ lại được."]},
        {"title": "Tế bào và chất nền ngoại bào", "points": ["Tế bào cơ trơn biến đổi và tế bào gốc tiền thân.",
                                              "Chất nền ngoại bào (ECM) tăng nhiều → u cứng, mặt cắt xoáy.",
                                              "TGF-β là chất trung gian xơ hoá chính."]},
        {"title": "Tín hiệu nội bào", "points": ["Wnt/β-catenin thúc đẩy tăng sinh.",
                                                "Tạo mạch và thiếu oxy trong u.",
                                                "MED12, HMGA2 là đột biến hay gặp.",
                                                "FH-deficient/HLRCC là dạng hiếm, đỏ flag."]},
    ], ["P051", "P053", "P055", "P057"],
        "Tách ba trụ cột để dễ nhớ.",
        "Bệnh sinh không phải một đường tín hiệu duy nhất.")
    mechanism("Cơ chế tăng trưởng u xơ theo trục nội tiết",
        [("Nội tiết (E + P)", "Hai hormone chính kích thích thụ thể, tăng phân bào, giảm chết tế bào theo chương trình."),
         ("Tế bào gốc cơ tử cung", "Cung cấp nguồn tế bào u xơ theo thời gian."),
         ("ECM và xơ hoá", "Collagen type I/III tăng, u cứng và biến dạng."),
         ("Wnt/β-catenin + TGF-β", "Duy trì tăng sinh và xơ hoá.")],
        ["P051", "P053", "P055"],
        "Dựng chuỗi cơ chế.",
        "Giải thích vì sao thuốc nội tiết chỉ là 'cầu nối' chứ không chữa cấu trúc.",
        outcome="U phát triển theo thời gian và thường đáp ứng nhất thời với GnRH.")
    definition_slide("Đặc điểm đại thể và mô học thường gặp",
        "Đại thể: khối u cứng, ranh giới rõ, mặt cắt trắng xám xoáy vòng. "
        "Mô học: bó cơ trơn dày đặc, xen kẽ chất nền nhiều collagen. "
        "Thoái hoá hay gặp khi u lớn hoặc thiếu máu nuôi: hyaline, cystic, myxoid, đỏ, vôi hoá, mỡ/lipoleiomyoma.",
        ["P038", "P073", "P075"],
        "Ghép đặc điểm mô học thường gặp.",
        "Giúp nhận diện khi đọc giải phẫu bệnh, đặc biệt các dạng thoái hoá.")
    content("Thoái hoá và biến thể u xơ — khi nào cần chú ý",
        ["Hyaline là phổ biến nhất; vôi hoá thường gặp ở u lâu năm, đặc biệt sau mãn kinh.",
         "Thoái hoá đỏ (còn gọi carneous trong tài liệu cũ) thường xảy ra ở phụ nữ mang thai hoặc dùng GnRH.",
         "STUMP và ung thư cơ trơn tử cung rất hiếm; chẩn đoán dựa vào nhân chia, hoại tử, nhân không điển hình.",
         "Lipoleiomyoma chứa nhiều mỡ, thường lành tính."],
        ["P073", "P075", "P077"],
        "Liệt kê các biến thể.",
        "Đừng nhầm STUMP/ung thư cơ trơn với u thường; chỉ định mổ và cắt nhỏ u không bảo vệ (morcellation) phải cẩn thận.")
    content("Dấu hiệu cảnh báo sinh học và bệnh học",
        ["Tăng kích thước nhanh sau mãn kinh (không phải teo nhỏ).",
         "Chảy máu bất thường hoặc ra dịch sau mãn kinh.",
         "MRI có dấu hiệu hoại tử không điển hình, bờ xâm lấn, khuếch tán hạn chế.",
         "Tiền sử xạ trị, tamoxifen, hoặc hội chứng di truyền (HLRCC).",
         "Tránh cắt nhỏ u không bảo vệ khi nghi ác tính."],
        ["P077", "P079", "P081", "P103"],
        "Liệt kê dấu hiệu cảnh báo.",
        "Dấu hiệu cảnh báo thay đổi hoàn toàn chiến lược: cần MRI chuyên khoa và hội chẩn với ung thư phụ khoa.")
    content("Điểm nhớ cơ chế bệnh sinh",
        ["U xơ không chỉ là bệnh 'nội tiết' thuần tuý.",
         "Cơ chế gồm nội tiết, tế bào gốc, ECM, TGF-β, Wnt/β-catenin, MED12/HMGA2.",
         "Biết cơ chế giúp hiểu vì sao GnRH chỉ tạm nhỏ và vì sao bóc u không chữa 'căn nguyên'.",
         "STUMP/ung thư cơ trơn rất hiếm nhưng phải nghĩ tới khi có dấu hiệu cảnh báo."],
        ["P079", "P190"],
        "Tổng hợp phần cơ chế.",
        "Phần 2 đặt nền để hiểu các phương pháp điều trị ở phần 8.")

    # 3. Phân loại
    section(3, "Phân loại", "Biến 'u xơ' thành ngôn ngữ ra quyết định")
    content("Vì sao phải phân loại?",
        ["Cùng tên 'u xơ' nhưng nhóm khác nhau có nguy cơ ART và chỉ định điều trị rất khác.",
         "Phân loại tốt giúp giao tiếp giữa bác sĩ và bệnh nhân rõ ràng.",
         "Trong ART, vị trí và quan hệ với buồng tử cung quan trọng hơn kích thước đơn độc."],
        ["P045", "P105"],
        "Đặt câu hỏi 'phân loại để làm gì'.",
        "Nếu không phân loại thì mọi quyết định trở thành cảm tính.")
    table_slide("FIGO 0–8: ngôn ngữ chính để ra quyết định",
        ["Nhóm", "Giải phẫu", "Ý nghĩa ART"], T3_ROWS,
        ["T3", "T5", "P038"],
        "Dựng FIGO bằng bảng native (DOCX không có hình).",
        "Học bảng FIGO là học cách dùng ngôn ngữ chung giữa siêu âm viên và bác sĩ điều trị.")
    two_col("FIGO 0–2 — nhóm ảnh hưởng trực tiếp",
        "Mô tả", ["Type 0: hoàn toàn trong buồng tử cung, có cuống.",
                  "Type 1: phần lớn trong buồng tử cung.",
                  "Type 2: phần lớn trong cơ nhưng lồi vào buồng."],
        "Xử trí ART", ["Ảnh hưởng trực tiếp nơi phôi bám.",
                       "Thường chỉ định xử trí trước chuyển phôi.",
                       "Đường nội soi buồng tử cung phù hợp nhất."],
        ["T3", "P038", "P123"],
        "Tách nhóm 0–2.",
        "Đây là nhóm đồng thuận cao nhất để can thiệp trước chuyển phôi.",
        vs=True)
    content("FIGO 3 — chạm nội mạc, không lồi buồng tử cung",
        ["Không thấy lồi buồng tử cung như u dưới niêm mạc.",
         "Nội soi buồng tử cung có thể gần bình thường.",
         "Cần phân biệt rõ với type 4 khi tư vấn ART.",
         "Là vùng xám cần cá thể hoá theo RIF, phôi quý, kích thước và diện tiếp xúc nội mạc."],
        ["T3", "P069", "P131"],
        "Tách type 3.",
        "Chạm nội mạc có ý nghĩa với vi môi trường dù không méo buồng tử cung rõ.")
    content("FIGO 4 — trong cơ, không chạm buồng tử cung",
        ["U nằm trọn trong cơ.",
         "Quyết định theo kích thước, số lượng, triệu chứng, tuổi noãn và số phôi hiện có.",
         "Không tự động mổ chỉ vì IVF.",
         "Khi phân loại mơ hồ giữa 3 và 4, dùng 3D, bơm nước buồng tử cung hoặc MRI theo câu hỏi."],
        ["T3", "P134", "P190"],
        "Cá thể hoá type 4.",
        "Type 4 là nơi điều trị thừa dễ xảy ra nhất.")
    content("FIGO 5–7 và type 8",
        ["5–7: dưới thanh mạc, xa buồng tử cung hơn.",
         "Thường không ảnh hưởng khả năng làm tổ nếu nhỏ và không triệu chứng.",
         "Mổ khi có triệu chứng, khối lớn, xoắn, hoặc cản thao tác.",
         "Type 8: cổ tử cung, dây chằng rộng, vị trí đặc biệt — lập bản đồ MRI riêng."],
        ["T3", "P041", "P101"],
        "Tách 5–7 và 8.",
        "Không áp công thức FIGO thường gặp cho vị trí nguy cơ cao.")
    two_col("Type 3 và type 4 — cạnh tranh hay đồng phạm?",
        "Type 3", ["Chạm nội mạc.", "Không lồi buồng tử cung.", "Nội soi buồng tử cung có thể không thấy rõ.", "Vùng xám trong ART."],
        "Type 4", ["Không chạm buồng tử cung.", "Trong cơ thật sự.", "Theo dõi hoặc cá thể hoá.", "Không tự động mổ nếu nhỏ, buồng tử cung ổn."],
        ["P069", "P131", "P134"],
        "So sánh ranh giới sát nội mạc.",
        "Gộp hai nhóm làm mất thông tin quan trọng cho ART.",
        vs=True)
    content("Hệ hỗ trợ: PALM-COEIN, Wamsteker, Lasmar STEPW",
        ["PALM-COEIN đặt u xơ trong nhóm nguyên nhân rong kinh cường kinh cấu trúc.",
         "Wamsteker phân loại u dưới niêm mạc theo độ sâu xâm nhập cơ.",
         "Lasmar STEPW đánh giá khả năng cắt nội soi buồng tử cung một hay nhiều thì.",
         "Ba hệ này là công cụ; FIGO vẫn là ngôn ngữ chính của ART."],
        ["P049", "P125"],
        "Đặt hệ phân loại hỗ trợ đúng chỗ.",
        "Tránh nhầm lẫn role: FIGO là giao tiếp, các hệ khác phục vụ chọn thủ thuật.")
    content("Mô tả tối thiểu một khối u trước ART",
        ["Số lượng và ba kích thước.",
         "FIGO type và khoảng cách tới nội mạc.",
         "Có/không biến dạng buồng tử cung.",
         "Liên quan cổ tử cung, lỗ vòi trứng, buồng trứng.",
         "Adenomyosis/polyp/dính đi kèm nếu phát hiện."],
        ["P045", "P105"],
        "Chuẩn hoá mô tả u.",
        "Thiếu dữ liệu này thì không thể chọn đúng thứ tự IVF và mổ.")

    # 4. Triệu chứng
    section(4, "Triệu chứng và biểu hiện lâm sàng", "Không chỉ nhìn hình ảnh")
    content("Nhiều u xơ không có triệu chứng",
        ["Phát hiện tình cờ qua siêu âm ở phụ nữ khám hiếm muộn/ART là rất phổ biến.",
         "U nhỏ dưới thanh mạc thường im lặng cho đến khi đủ lớn hoặc có biến chứng.",
         "Vì vậy 'có u xơ' cần nối với triệu chứng và mục tiêu bệnh nhân chứ không đứng riêng."],
        ["P091", "P093"],
        "Đặt vấn đề triệu chứng.",
        "Đừng điều trị một 'phát hiện tình cờ' như thể là bệnh.")
    three_col("Ba nhóm triệu chứng cần tách", [
        {"title": "Chảy máu", "points": ["Rong kinh, cường kinh.", "Thiếu máu, mệt mỏi.", "Liên hệ PALM-COEIN."]},
        {"title": "Khối và chèn ép", "points": ["Đau vùng chậu, đau giao hợp.", "Tiểu nhiều, táo bón.", "Bụng to, sờ thấy khối."]},
        {"title": "Sinh sản và thai kỳ", "points": ["Hiếm muộn, sảy thai.", "Thất bại làm tổ/thất bại chuyển phôi lặp lại.", "Biến chứng thai kỳ (xem slide sau)."]},
    ], ["P091", "P105"],
        "Tách ba nhóm triệu chứng.",
        "Trộn lẫn các nhóm dễ dẫn tới điều trị nhầm mục tiêu.")
    table_slide("Ra huyết tử cung bất thường — nhóm PALM",
        ["Nhóm (FIGO)", "Tên tiếng Việt", "Liên hệ"],
        [["P — Polyp", "Polyp nội mạc", "Cần phân biệt với u dưới niêm mạc"],
         ["A — Adenomyosis", "Lạc nội mạc trong cơ", "Đi kèm hoặc nhầm với u trong cơ"],
         ["L — Leiomyoma", "U xơ cơ tử cung", "Chủ đề chính của ghi chú (viết tắt L là u xơ)"],
         ["M — Malignancy", "Tăng sản/ung thư nội mạc", "Cần loại trừ khi chảy máu bất thường"]],
        ["P091", "P049"],
        "Liệt kê nhóm PALM.",
        "PALM là nhóm nguyên nhân cấu trúc, dễ phát hiện qua hình ảnh.")
    table_slide("Ra huyết tử cung bất thường — nhóm COEIN",
        ["Nhóm (FIGO)", "Tên tiếng Việt", "Liên hệ"],
        [["O — Ovulatory", "Rối loạn phóng noãn", "Liên quan nội tiết, ART kích thích"],
         ["E — Endometrial", "Viêm nội mạc, vết cắt", "Đừng bỏ qua sau thủ thuật"],
         ["I — Iatrogenic", "Do thuốc/dụng cụ", "LNG-IUS, tamoxifen"],
         ["N — Not classified", "Chưa rõ nguyên nhân", "Cần đánh giá thêm"]],
        ["P091", "P049"],
        "Liệt kê nhóm COEIN.",
        "COEIN là nhóm nguyên nhân không cấu trúc; cần khảo sát riêng.")
    content("Triệu chứng sinh sản — không thẳng tới 'do u xơ'",
        ["Hiếm muộn: u xơ là nguyên nhân duy nhất ở khoảng 2–3% các ca; gặp u xơ ở khoảng 5–10% dân số hiếm muộn.",
         "Sảy thai, thất bại làm tổ lặp lại cần đánh giá đồng thời: phôi, nội mạc, lạc nội mạc, polyp, viêm nội mạc, ứ dịch vòi trứng, yếu tố nam.",
         "Đừng quy RIF cho u xơ trước khi khảo sát đầy đủ."],
        ["P033", "P201"],
        "Phân tách triệu chứng sinh sản.",
        "RIF là hội chứng đa nguyên nhân; u xơ chỉ là một phần.")
    content("Biến chứng thai kỳ liên quan u xơ",
        ["Sảy thai, sinh non.",
         "Ngôi bất thường, nhau bám bất thường, nhau tiền đạo.",
         "Tăng tỉ lệ mổ lấy thai.",
         "Băng huyết sau sinh do rối loạn co hồi tử cung quanh vị trí u."],
        ["P211", "P222"],
        "Liệt kê biến chứng thai kỳ.",
        "Biến chứng này không thay đổi thực sự khi đã có thai; tư vấn trước ART là quan trọng.")
    kpi_slide("Triệu chứng thường gặp — Zimmermann 2012 (PMID 22448610)",
        [
            {"number": "59,8%", "unit": "có u xơ", "label": "kinh nhiều"},
            {"number": "37,4%", "unit": "không có u xơ", "label": "kinh nhiều"},
            {"number": "32,6%", "unit": "có u xơ", "label": "đè bàng quang"},
            {"number": "23,5%", "unit": "có u xơ", "label": "đau khi giao hợp"},
            {"number": "53,7%", "unit": "có u xơ", "label": "ảnh hưởng chất lượng cuộc sống 12 tháng qua"},
        ],
        ["P093"],
        "Gắn số cho phần triệu chứng.",
        "Khảo sát quốc tế trên 21.479 phụ nữ ở 8 quốc gia — giúp nhớ u xơ không chỉ là phát hiện trên siêu âm.")
    content("Điểm nhớ triệu chứng",
        ["Triệu chứng là một chỉ định riêng, ảnh hưởng ART là một chỉ định riêng.",
         "Đừng trộn hai mục tiêu khi tư vấn.",
         "Khi điều trị triệu chứng máu/đau, xong vẫn phải đánh giá buồng tử cung trước chuyển phôi."],
        ["P201", "P222"],
        "Chốt quan điểm.",
        "Bệnh nhân đỡ triệu chứng chưa chắc đã đủ điều kiện chuyển phôi.")

    # 5. Chẩn đoán
    section(5, "Chẩn đoán và hình ảnh học", "Câu hỏi buồng tử cung điều khiển xét nghiệm")
    content("Khai thác bệnh sử và khám lâm sàng",
        ["Hỏi về chu kỳ kinh, lượng máu, thiếu máu; đau và chèn ép.",
         "Tiền sử ART: thất bại làm tổ, sảy thai, số lần chuyển phôi.",
         "Khám: kích thước tử cung, khối bất thường, tình trạng cổ tử cung và phần phụ.",
         "Dựa vào câu trả lời để chọn công cụ hình ảnh phù hợp."],
        ["P045", "P105"],
        "Đặt nền bệnh sử.",
        "Khám sàng lọc tốt giúp giảm thử nghiệm thừa.")
    table_slide("So sánh công cụ hình ảnh",
        ["Công cụ", "Mạnh nhất khi", "Giới hạn"], T11_ROWS,
        ["T11", "P099"],
        "Tóm bảng diagnostic methods.",
        "Người học cần biết chọn test theo câu hỏi, không chọn theo thói quen.")
    content("2D TVUS — bước đầu, không bao giờ là cuối nếu chưa trả lời được buồng tử cung",
        ["Ghi nhận kích thước, vị trí, số lượng u và mối liên quan buồng tử cung tương đối.",
         "Không phân biệt tốt type 3 với type 4 ở nhiều ca.",
         "Không đánh giá được mặt phẳng buồng tử cung toàn diện.",
         "Làm lại sau can thiệp nếu cần, đặc biệt khi phôi quý."],
        ["T11", "P101"],
        "Đặt vai trò 2D.",
        "2D là khởi đầu, nhưng buồng tử cung là câu hỏi → phải nâng bậc.")
    content("3D TVUS — mặt phẳng vành thay đổi cuộc chơi",
        ["Dựng được mặt phẳng vành của buồng tử cung.",
         "Phân biệt type 3 với type 4 khi 2D mơ hồ.",
         "Đo khoảng cách u tới nội mạc chính xác hơn.",
         "Hữu ích trước chuyển phôi khi cần chứng minh buồng tử cung lành."],
        ["T11", "P101"],
        "Chỉ định 3D.",
        "3D giải quyết vấn đề mặt phẳng buồng tử cung mà 2D dễ bỏ sót.")
    content("SIS/HyFoSy — bơm nước buồng tử cung",
        ["Làm rõ đường viền buồng tử cung.",
         "Phát hiện u dưới niêm mạc và polyp nhỏ trong buồng.",
         "Rẻ và nhanh hơn một lần chuyển phôi thất bại.",
         "Tránh khi đang viêm âm đạo cấp hoặc có thai."],
        ["T11", "P101"],
        "Chỉ định bơm nước buồng tử cung.",
        "Bơm nước giúp chứng minh buồng tử cung sẵn sàng trước chuyển phôi.")
    content("Nội soi buồng tử cung — vừa chẩn đoán vừa xử trí",
        ["Phù hợp cho type 0–2 và tổn thương dạng polyp nội mạc/dính.",
         "Không khảo sát được phần cơ tử cung.",
         "Can thiệp quá mức dễ làm tổn thương nội mạc và gây dính.",
         "Kết hợp với siêu âm để biết vị trí u trong cơ trước khi cắt."],
        ["T11", "P125"],
        "Đặt vai trò nội soi buồng tử cung.",
        "Nội soi buồng tử cung không thay thế được bản đồ toàn cơ tử cung.")
    content("MRI — chỉ khi bản đồ 2D/3D chưa đủ",
        ["Đa u hoặc u lớn làm siêu âm khó lập bản đồ.",
         "Nghi lạc nội mạc tử cung đi kèm.",
         "Dấu hiệu nghi ung thư cơ trơn tử cung (sarcom) hoặc STUMP.",
         "Lập kế hoạch phẫu thuật cho ca khó.",
         "Không dùng thường quy cho mọi bệnh nhân ART."],
        ["T11", "P101", "P103"],
        "Đặt chỉ định MRI.",
        "MRI có ích ở ca phức tạp nhưng không cần thường quy mọi ca.")
    algorithm("Thuật toán nâng bậc hình ảnh trước ART",
        ["Siêu âm 2D TVUS — ghi nhận FIGO nghi ngờ.",
         "Buồng tử cung chưa rõ/type 3–4? → 3D TVUS hoặc bơm nước buồng tử cung.",
         "Tổn thương trong buồng nghi ngờ? → nội soi buồng tử cung.",
         "Đa u, u lớn, nghi lạc nội mạc hoặc nghi sarcom → MRI."],
        ["P101", "T11"],
        "Dạy lộ trình chẩn đoán.",
        "Đi từng bước giúp tránh vừa thiếu vừa thừa xét nghiệm.")
    content("Chẩn đoán phân biệt không được quên",
        ["Lạc nội mạc tử cung trong cơ đi kèm.",
         "Polyp nội mạc hoặc vách ngăn tử cung.",
         "Tăng sản/ung thư nội mạc khi chảy máu bất thường.",
         "Ung thư cơ trơn tử cung hoặc STUMP khi u lớn nhanh, tăng sinh mạch, hoại tử.",
         "Khối buồng trứng giả u cuống, thai sớm, sản phẩm thai.",
         "Co cơ tử cung khu trú (thường mất khi siêu âm lại)."],
        ["P103", "P087"],
        "Liệt kê chẩn đoán phân biệt.",
        "Mổ đúng u xơ nhưng sai bệnh chính vẫn thất bại.")
    content("Mẫu báo cáo siêu âm tối thiểu trước ART",
        ["Số lượng u và ba chiều kích thước.",
         "FIGO type và vị trí.",
         "Khoảng cách tới nội mạc.",
         "Có hay không biến dạng buồng tử cung.",
         "Liên quan cổ tử cung, lỗ vòi trứng, buồng trứng.",
         "Lạc nội mạc/polyp/dính đi kèm."],
        ["P045", "P105"],
        "Chuẩn hoá báo cáo.",
        "Báo cáo tốt rút ngắn đường đi quyết định.")
    content("Trước chuyển phôi: phải chứng minh buồng tử cung",
        ["Không giả định buồng tử cung ổn chỉ vì 2D bình thường.",
         "Phôi quý cần buồng tử cung được chứng minh cụ thể.",
         "Đánh giá lại sau can thiệp khó hoặc khi siêu âm không chắc chắn.",
         "Không chuyển phôi vào buồng tử cung còn mơ hồ."],
        ["P101", "P105", "P193"],
        "Chốt tiêu chuẩn.",
        "Chuyển phôi là lúc cần chắc chắn về buồng tử cung.")

    # 6. Cơ chế ảnh hưởng ART
    section(6, "Cơ chế ảnh hưởng ART", "Từ hình học buồng tử cung đến kết quả chuyển phôi")
    content("Tư duy chính trước khi vào cơ chế",
        ["Không phải mọi u xơ đều làm giảm kết quả ART.",
         "Quan hệ với buồng tử cung và nội mạc mới quyết định nhiều nhất.",
         "Cơ chế sinh học không tự động thành chỉ định mổ; nó giúp chọn đúng hướng đi."],
        ["P061", "P123"],
        "Đặt lại tư duy.",
        "Tránh bẫy 'có cơ chế → phải mổ'.")
    mechanism("Chuỗi 5 tầng cơ chế ảnh hưởng ART",
        [("Buồng tử cung", "U lồi làm thay đổi hình học nơi phôi bám."),
         ("Nội mạc", "Tín hiệu tiếp nhận phôi bị ảnh hưởng khi u chạm nội mạc."),
         ("Viêm và tưới máu", "Môi trường quanh u xơ thay đổi vi môi trường."),
         ("Co bóp", "Nhu động quanh thời điểm làm tổ có thể rối loạn."),
         ("Thao tác ART", "U cản chọc hút noãn hoặc làm khó chuyển phôi.")],
        ["P061", "P063", "P065", "P067", "P123"],
        "Dựng chuỗi cơ chế.",
        "Cơ chế cho thấy vì sao vị trí quan trọng hơn kích thước.",
        outcome="Giảm làm tổ, tăng sảy thai và tăng biến chứng thai kỳ.")
    two_col("Type 0–2 ảnh hưởng trực tiếp", "Vì sao", ["Méo buồng tử cung.",
        "Mất vùng nội mạc lành để phôi bám.",
        "Có thể rối loạn vi môi trường quanh u."],
        "Hệ quả", ["Giảm tỉ lệ làm tổ.",
        "Tăng sảy thai sớm.",
        "Có thể ảnh hưởng co bóp tử cung."],
        ["P061", "P123"],
        "Tách 0–2.",
        "Đây là nhóm có cơ chế rõ nhất và đồng thuận can thiệp cao nhất.",
        vs=True)
    two_col("Type 3 và 4 — vùng cơ chế khó phân tách",
        "Type 3", ["Chạm nội mạc nhưng không lồi buồng tử cung.",
                  "Vi môi trường nội mạc tại vị trí chạm có thể bị ảnh hưởng.",
                  "Hệ quả khó lường."],
        "Type 4", ["Không chạm nội mạc.",
                  "Ảnh hưởng phụ thuộc kích thước, số lượng, vị trí.",
                  "Bằng chứng yếu hơn cho cả mặt ART."],
        ["P069", "P131", "P134"],
        "So sánh 3 và 4 trên góc cơ chế.",
        "Cơ chế khác nhau dẫn tới quyết định khác nhau trong vùng xám.",
        vs=True)
    content("Type 5–7 và nguy cơ thuần thao tác",
        ["U dưới thanh mạc nhỏ thường không ảnh hưởng khả năng làm tổ.",
         "Lo ngại chính là thao tác: u đẩy lệch buồng trứng, cản chọc hút noãn.",
         "U cổ tử cung hoặc u làm biến dạng trục tử cung có thể làm khó chuyển phôi.",
         "Quyết định theo đường vào, không theo loại u."],
        ["P045", "P123", "P196"],
        "Tách 5–7.",
        "ART có thể bị ảnh hưởng không vì buồng tử cung mà vì đường vào.")
    content("Bẫy lâm sàng: đừng đổ hết cho u xơ",
        ["Trước khi can thiệp, kiểm tra: phôi, nội mạc, lạc nội mạc, polyp nội mạc, viêm nội mạc, ứ dịch vòi trứng, yếu tố nam.",
         "U xơ có thể là một phần nguyên nhân, không phải nguyên nhân chính.",
         "Bệnh nhân chuyển phôi thất bại lặp lại cần được đánh giá đa chiều trước khi đi mổ."],
        ["P201", "P222", "P246"],
        "Chống thiên kiến neo bám.",
        "Tránh mổ oan vì tin nhanh rằng u xơ là 'thủ phạm'.")
    algorithm("Thuật toán tích hợp cơ chế vào quyết định ART",
        ["Phát hiện u xơ trên TVUS — mô tả đầy đủ.",
         "Xác định FIGO + trạng thái buồng tử cung.",
         "Đánh giá tuổi, AMH/AFC, số phôi, triệu chứng.",
         "Chọn: theo dõi / chụp thêm hình ảnh / mổ / tạo và trữ phôi trước / đánh giá lại buồng tử cung.",
         "Chứng minh buồng tử cung trước chuyển phôi."],
        ["P045", "T15", "T21", "P222"],
        "Tích hợp cơ chế vào hành động.",
        "Cơ chế chỉ hữu ích khi kết thúc bằng một quyết định có lợi.")
    kpi_slide("U xơ trong cơ và kết quả sinh sản — meta-analysis 2024 (PMID 38935974)",
        [
            {"number": "OR 0,53", "unit": "u <3 cm", "label": "giảm tỉ lệ có thai lâm sàng"},
            {"number": "OR 0,59", "unit": "u <3 cm", "label": "giảm tỉ lệ thai tiến triển/sanh sống"},
            {"number": "OR 0,43", "unit": "u 3–6 cm", "label": "giảm tỉ lệ có thai lâm sàng"},
            {"number": "OR 0,62", "unit": "nhiều u", "label": "giảm tỉ lệ có thai lâm sàng"},
        ],
        ["P131"],
        "Gắn số cho cơ chế ảnh hưởng ART.",
        "OR < 1 nghĩa là u xơ làm giảm kết quả; nhưng phải cân bằng với cái giá của bóc u.")

    # 7. Xử trí theo FIGO
    section(7, "Xử trí theo FIGO", "Cùng là u xơ, hành động khác nhau")
    table_slide("Quyết định theo FIGO trước ART",
        ["FIGO", "Vấn đề chính", "Hành động"], T15_ROWS,
        ["T15", "P123"],
        "Dùng bảng quyết định FIGO.",
        "Đây là xương sống của phần xử trí theo FIGO.")
    content("Type 0 — trong buồng tử cung có cuống",
        ["Thường xử trí trước chuyển phôi.",
         "Đường nội soi buồng tử cung phù hợp nhất với tổn thương có cuống.",
         "Tránh đốt sâu để bảo vệ nội mạc.",
         "Kiểm tra lại buồng tử cung sau thủ thuật ở ca khó hoặc polyp/dính đi kèm."],
        ["T15", "P125"],
        "Xử trí type 0.",
        "Đây là tổn thương sửa được rõ trước chuyển phôi.")
    content("Type 1 — phần lớn trong buồng tử cung",
        ["Cắt từng lớp qua nội soi buồng tử cung.",
         "Bảo vệ lớp đáy nội mạc.",
         "Tránh đốt rộng hoặc cắt sâu gây sẹo dày.",
         "Staged procedure nếu u lớn hoặc vị trí khó."],
        ["T15", "P125"],
        "Xử trí type 1.",
        "Mục tiêu là vừa lấy u vừa giữ nội mạc cho ART.")
    content("Type 2 — phần sâu trong cơ",
        ["Nguy cơ thủng, dính, quá tải dịch.",
         "Có thể chia hai thì để an toàn.",
         "Lấy sạch bằng mọi giá chưa chắc tốt cho ART.",
         "Bảo vệ lớp đáy nội mạc là ưu tiên."],
        ["T15", "P125", "P190"],
        "Xử trí type 2.",
        "Buồng tử cung sau mổ quan trọng hơn cảm giác lấy sạch.")
    content("Type 3 — vùng xám cần cá thể hoá",
        ["Chạm nội mạc, không lồi buồng tử cung.",
         "Bằng chứng còn chưa đủ để mổ mọi ca.",
         "Xác nhận bằng 3D/SIS/MRI khi phân loại chưa chắc.",
         "Cân nhắc RIF, phôi quý, tuổi, kích thước, diện tiếp xúc nội mạc.",
         "Quyết định cần hội chẩn và trao đổi với bệnh nhân."],
        ["T15", "P131"],
        "Tách type 3.",
        "Không vô hại nhưng cũng không nên mổ theo phản xạ.")
    content("Type 4 — cân bằng nhiều yếu tố",
        ["Kích thước và số lượng u.",
         "Triệu chứng kèm theo.",
         "Tuổi, AMH, số phôi hiện có.",
         "Nguy cơ phẫu thuật: sẹo, dính, thời gian chờ.",
         "Không dùng công thức cứng, không tự động mổ chỉ vì IVF."],
        ["T15", "P134", "P196"],
        "Cá thể hoá type 4.",
        "Type 4 là nơi cần cân bằng nhiều nhất.")
    content("Type 5–7 — thường không mổ chỉ vì IVF",
        ["Xa buồng tử cung, ít ảnh hưởng khả năng làm tổ nếu nhỏ.",
         "Mổ khi có triệu chứng, khối lớn, xoắn, cản thao tác ART.",
         "Theo dõi nếu không triệu chứng và buồng tử cung ổn.",
         "Không mổ chỉ để cải thiện IVF đơn thuần khi u nhỏ."],
        ["T15", "P201"],
        "Tránh mổ thừa 5–7.",
        "Tránh trì hoãn IVF cho một u dưới thanh mạc nhỏ vô hại.")
    content("Type 8 — vị trí đặc biệt",
        ["Cổ tử cung, dây chằng rộng, ký sinh hoặc vị trí đặc biệt.",
         "Có thể gần bàng quang, niệu quản, mạch máu.",
         "MRI có ích khi bản đồ phức tạp.",
         "Cần cá thể hoá và phẫu thuật viên kinh nghiệm."],
        ["T3", "P041", "P101"],
        "Tách 8.",
        "Không áp công thức FIGO thường gặp cho vị trí nguy cơ cao.")
    content("Khi nào mổ trước IVF — chốt rõ",
        ["Buồng tử cung méo rõ.",
         "Type 0–2.",
         "Thiếu máu hoặc triệu chứng nặng.",
         "U cản chọc hút noãn hoặc chuyển phôi.",
         "Dấu hiệu bất thường nghi ác tính."],
        ["P123", "P137", "P201"],
        "Chốt chỉ định mổ trước.",
        "Mổ trước có lợi khi sửa đúng nút nghẽn thật.")
    content("Khi nào không trì hoãn IVF — chốt rõ",
        ["Tuổi cao hoặc dự trữ buồng trứng giảm (DOR).",
         "Type 4 nhỏ hoặc type 5–7 nhỏ.",
         "Không méo buồng tử cung và không cản thao tác.",
         "Bệnh nhân chấp nhận theo dõi u sau chuyển phôi."],
        ["P134", "P196", "P201"],
        "Chốt chỉ định không trì hoãn.",
        "Ở DOR, vài tháng trì hoãn có thể đắt hơn lợi ích mổ chưa chắc.")

    # 8. Phương pháp điều trị
    section(8, "Phương pháp điều trị", "Đích điều trị trước, rồi mới chọn phương pháp")
    content("Đích điều trị trước khi chọn phương pháp",
        ["Giảm máu/đau.",
         "Sửa thiếu máu.",
         "Giảm thể tích khối u.",
         "Phục hồi buồng tử cung.",
         "Tạo điều kiện chọc hút noãn/chuyển phôi.",
         "Bảo vệ thời gian noãn.",
         "Giảm nguy cơ thai kỳ."],
        ["P119", "P137", "P196"],
        "Tách rời đích điều trị.",
        "Tên phương pháp ít quan trọng hơn đích điều trị.")
    table_slide("Ma trận tác động điều trị",
        ["Nhóm", "Thay đổi gì", "Không thay đổi gì"], T24_ROWS,
        ["T24", "P240"],
        "Tóm hiệu ứng điều trị.",
        "Bảng này ngăn nhầm mục tiêu triệu chứng với mục tiêu ART.")
    content("Sắt, NSAID, axit tranexamic",
        ["Sắt (uống/tiêm): sửa thiếu máu, là cầu nối phổ biến nhất.",
         "NSAID: giảm đau và giảm máu mức độ nhất định.",
         "Axit tranexamic: giảm chảy máu nặng ngắn hạn.",
         "Cả ba đều không sửa được cấu trúc buồng tử cung."],
        ["P137", "P141", "T24"],
        "Đặt thuốc triệu chứng đúng vai trò.",
        "Đúng cho chảy máu nhiều chưa chắc đủ cho chuyển phôi.")
    content("Nội tiết — COC/progestin/LNG-IUS và GnRH",
        ["COC/progestin/LNG-IUS kiểm soát triệu chứng chọn lọc; cần cân nhắc kế hoạch ART.",
         "Đồng vận GnRH/đối vận GnRH ± bổ sung nội tiết (add-back) giảm chảy máu và thể tích tạm thời.",
         "Dùng làm cầu nối trước mổ hoặc trước chuyển phôi.",
         "Không chứng minh được khoang tử cung sẵn sàng để chuyển phôi."],
        ["P137", "P141", "T24"],
        "Tách hai nhóm thuốc nội tiết.",
        "Mỗi nhóm có vai trò riêng; không nên dùng như nhau.")
    content("Bóc u qua nội soi buồng tử cung",
        ["Phù hợp type 0–2.",
         "Sửa buồng tử cung và bảo vệ nội mạc.",
         "Nguy cơ: thủng, quá tải dịch, đốt sâu, dính sau mổ.",
         "Chia thì khi u lớn hoặc xâm nhập sâu vào cơ."],
        ["P125", "P190"],
        "Đặt vai trò nội soi buồng tử cung.",
        "Phù hợp nhất cho nhóm can thiệp rõ nhất và ít xâm lấn nhất.")
    two_col("Bóc u qua nội soi ổ bụng, mổ mở, robot",
        "Giải quyết", ["U trong cơ lớn.", "Nhiều u.", "Cản thao tác ART.", "Triệu chứng khối."],
        "Cái giá", ["Sẹo cơ tử cung.", "Dính vùng chậu.", "Thời gian chờ.", "Cần theo dõi thai kỳ sau này."],
        ["P128", "P190", "P193"],
        "Tư vấn cân bằng cho bóc u qua bụng.",
        "Bảo tồn tử cung không miễn phí về mặt ART.",
        vs=True)
    content("Type 2: an toàn hơn là lấy sạch",
        ["Có phần sâu trong cơ.",
         "Không cố 'đào' khi mất an toàn.",
         "Có thể chia thì phẫu thuật.",
         "Bảo vệ lớp đáy nội mạc là ưu tiên.",
         "Ghi rõ trong tường trình mổ nếu có mở vào buồng tử cung."],
        ["P125", "P190"],
        "Dạy nguyên tắc dừng an toàn.",
        "Buồng tử cung lành quan trọng hơn lấy hết bằng mọi giá.")
    content("Nguy cơ dính và lớp đáy nội mạc",
        ["Tổn thương nội mạc làm tăng nguy cơ dính.",
         "Đốt rộng hoặc tổn thương sâu có hại.",
         "Hai diện thương đối diện dễ dính.",
         "Phôi cần buồng tử cung lành."],
        ["P190", "P211", "P246"],
        "Giải thích nguyên tắc.",
        "Không lấy nội dung phẫu thuật phụ; chỉ giữ nguyên tắc có trong DOCX.")
    content("UAE — nút mạch tử cung",
        ["Giảm triệu chứng ở ca chọn lọc.",
         "Không dùng thường quy khi đang tích cực mong thai.",
         "Lo ngại ảnh hưởng nội mạc, buồng trứng và tử cung.",
         "Không thay thế chỉ định mổ cho ART."],
        ["P159", "T24"],
        "Tư vấn UAE theo mục tiêu sinh sản.",
        "Ít xâm lấn không đồng nghĩa phù hợp ART.")
    content("HIFU/MRgFUS và RFA/TRFA",
        ["HIFU/MRgFUS: vai trò chọn lọc; cần đánh giá lại cấu trúc và mục tiêu ART.",
         "RFA/TRFA: dữ liệu giảm thể tích tốt nhưng còn bất định về ART/thai kỳ.",
         "Cả hai cần tư vấn về thời gian chờ trước khi cố thai.",
         "Không dùng thường quy khi đang tích cực mong thai."],
        ["T24", "P196"],
        "Tách HIFU/RFA.",
        "Can thiệp 'không phẫu thuật' chưa chắc an toàn cho ART.")
    table_slide("Mục tiêu → phương pháp → kiểm tra lại",
        ["Mục tiêu", "Có thể đạt", "Cần kiểm tra lại"],
        [["Máu và đau", "Thuốc và cầu nối", "Hb và triệu chứng"],
         ["Thể tích khối u", "GnRH, UAE, HIFU, đốt", "Buồng tử cung và thời điểm"],
         ["Buồng tử cung", "Bóc u chọn lọc", "Bơm nước, 3D, nội soi buồng"],
         ["Tuổi noãn", "Tạo và trữ phôi", "Số phôi và AMH"]],
        ["T24", "P196"],
        "Chốt ma trận.",
        "Mỗi mục tiêu cần một cách kiểm tra khác nhau.")

    # 9. Thứ tự ART, theo dõi và bằng chứng
    section(9, "Thứ tự ART, theo dõi và bằng chứng", "Noãn và tử cung lão hoá khác nhau")
    table_slide("Quyết định tạo và trữ phôi",
        ["Chiến lược", "Ứng viên", "Lý do"], T21_ROWS,
        ["T21", "P196"],
        "Tóm quyết định tạo và trữ phôi.",
        "Đây là cầu nối giữa tuổi noãn và tối ưu tử cung.")
    content("Ưu tiên tạo và trữ phôi trước — ai phù hợp",
        ["Tuổi cao hoặc AMH/AFC thấp.",
         "U chưa cản chọc hút noãn.",
         "Buồng tử cung chưa cần sửa ngay.",
         "Cần bảo vệ cơ hội tạo phôi.",
         "Sẵn sàng chuyển phôi trữ sau khi tối ưu tử cung."],
        ["T21", "P196"],
        "Nhận diện nhóm tạo phôi trước.",
        "Tạo phôi trước là chiến lược thời gian, không phải điều trị u.")
    content("Ưu tiên xử trí u trước — ai phù hợp",
        ["Type 0–2 lớn hoặc méo buồng tử cung rõ.",
         "U cản chọc hút noãn hoặc chuyển phôi.",
         "Thiếu máu hoặc triệu chứng nặng.",
         "Dấu hiệu bất thường nghi ác tính."],
        ["T21", "P123", "P137"],
        "Nhận diện nhóm xử trí u trước.",
        "Không nên tạo phôi rồi chuyển vào buồng tử cung chưa thể dùng.")
    two_col("Chuyển phôi tươi và chuyển phôi trữ",
        "Tươi", ["Ít thời gian chuẩn bị tử cung.",
                "Tránh nếu buồng tử cung chưa rõ.",
                "Không phù hợp khi cần mổ hoặc can thiệp."],
        "Trữ", ["Tách tạo phôi khỏi chuẩn bị tử cung.",
                "Cho thời gian sửa và đánh giá lại.",
                "Phù hợp với phôi quý và ca chọn lọc."],
        ["P196", "P193"],
        "Phân biệt thời điểm chuyển phôi.",
        "Chuyển phôi trữ giúp giải quyết tuần tự hai bài toán.",
        vs=True)
    algorithm("Thuật toán chọn thứ tự ART",
        ["Đánh giá FIGO và buồng tử cung.",
         "Nút nghẽn là noãn hay tử cung?",
         "Tạo và trữ phôi nếu noãn là nút nghẽn.",
         "Sửa buồng tử cung nếu đó là nút nghẽn.",
         "Đánh giá lại buồng tử cung trước chuyển phôi."],
        ["T21", "P196", "P193"],
        "Tích hợp thứ tự xử trí.",
        "Thuật toán giảm mâu thuẫn giữa phẫu thuật và tuổi noãn.")
    content("Thời gian chờ sau bóc u",
        ["Không có một mốc duy nhất cho mọi ca.",
         "Phụ thuộc đường mổ, độ sâu đường rạch, số lớp khâu.",
         "Phụ thuộc có mở vào buồng tử cung hay không.",
         "Cần thời gian lành sẹo cơ tử cung trước thai.",
         "Tư vấn thai kỳ và lựa chọn sinh mổ chọn lọc sau đường bụng vào cơ."],
        ["P193", "P211"],
        "Tư vấn thời điểm sau mổ.",
        "Dùng guideline cứng 1 con số dễ sai; tuỳ ca là đúng.")
    content("Theo dõi khi chưa can thiệp",
        ["Tái khám theo triệu chứng.",
         "Chụp lại hình ảnh khi kế hoạch ART thay đổi.",
         "Theo dõi chảy máu và thiếu máu.",
         "Ghi nhận khi bệnh nhân quyết định chuyển sang can thiệp."],
        ["P211", "P222"],
        "Dạy theo dõi bảo tồn.",
        "Theo dõi có chủ đích khác với bỏ mặc.")
    content("Sau nội soi buồng tử cung",
        ["Theo dõi ra máu và đau.",
         "Nghi dính nếu kinh ít rõ.",
         "Đánh giá lại buồng tử cung ở ca nguy cơ cao.",
         "Đợi buồng tử cung lành trước chuyển phôi."],
        ["P193", "P211"],
        "Dạy theo dõi sau nội soi buồng tử cung.",
        "Buồng tử cung sau thủ thuật là mục tiêu ART.")
    content("Sau bóc u đường bụng hoặc nội soi ổ bụng",
        ["Theo dõi đau và thiếu máu.",
         "Sẹo cơ tử cung và nguy cơ vỡ tử cung thấp nhưng cần tư vấn.",
         "Việc mở vào buồng tử cung và thời gian chờ.",
         "Nguy cơ u tái phát và u còn lại."],
        ["P193", "P211"],
        "Dạy theo dõi đường bụng.",
        "Sẹo và u tái phát ảnh hưởng kế hoạch thai kỳ.")
    content("Tư vấn thai kỳ sau bóc u",
        ["Có thể cần theo dõi thai kỳ nguy cơ cao.",
         "Kế hoạch sinh phụ thuộc độ sâu và việc mở vào buồng tử cung.",
         "Tư vấn nguy cơ u tái phát và u còn lại.",
         "Ghi rõ thông tin mổ cho bác sĩ sản khoa theo dõi."],
        ["P211", "P222"],
        "Dạy tư vấn thai kỳ.",
        "Thông tin phẫu thuật hiện tại phục vụ an toàn thai kỳ sau này.")
    content("Cập nhật bằng chứng 2024–2026",
        ["Mocanu 2026 — Fibroids and infertility (PMID 42104843).",
         "Intramural meta-analysis 2024 (PMID 38935974).",
         "Myomectomy before IVF/ICSI systematic review 2026 (PMID 41408877).",
         "FIGO type 3 IVF meta-analysis 2023 (PMID 37183601).",
         "ASRM/ACOG guideline cues cho quyết định theo FIGO và bối cảnh ART."],
        ["P275", "P281"],
        "Liệt kê evidence.",
        "Bằng chứng thay đổi nhanh; ưu tiên tổng quan hệ thống và guideline.")
    kpi_slide("Số liệu can thiệp — phần cần nhớ trước khi tư vấn",
        [
            {"number": "11,9%", "unit": "UAE", "label": "tỉ lệ sanh sống (live birth) sau nút mạch"},
            {"number": "27,4%", "unit": "UAE", "label": "tỉ lệ sảy thai sau nút mạch"},
            {"number": "49,4%", "unit": "RFA 6 tháng", "label": "giảm thể tích u type 2–5"},
            {"number": "69,8%", "unit": "RFA 12 tháng", "label": "giảm thể tích u type 2–5"},
            {"number": "0,4%", "unit": "bóc u", "label": "nguy cơ vỡ tử cung sau mổ"},
            {"number": "~18 tháng", "unit": "sau mổ", "label": "thời gian trung bình đến có thai"},
        ],
        ["P190", "P193", "P211"],
        "Gắn số cho phần can thiệp.",
        "Dùng số này để bệnh nhân hiểu mặt trái của các can thiệp, không phải để khuyến cáo nếu chưa đối chiếu full text.")
    case_slide("Ca luyện 1 — type 1 trước chuyển phôi",
        "Bệnh nhân 36 tuổi, đã có phôi trữ, siêu âm phát hiện u type 1 lồi vào buồng tử cung, không thiếu máu.",
        "Có nên chuyển phôi ngay không, hay cần xử trí u trước?",
        "Ưu tiên sửa buồng tử cung trước chuyển phôi; sau đó đánh giá lại bằng bơm nước hoặc 3D nếu diện thương rộng.",
        ["T15", "P125"])
    case_slide("Ca luyện 2 — DOR và type 4 nhỏ",
        "Bệnh nhân 39 tuổi, AMH thấp, type 4 nhỏ trong cơ, buồng tử cung không méo, u không cản chọc hút.",
        "Nên mổ trước hay tạo và trữ phôi trước?",
        "Ưu tiên tạo và trữ phôi trước vì tuổi noãn đang là nút nghẽn; buồng tử cung ổn có thể tối ưu sau bằng theo dõi.",
        ["T21", "P196", "P134"])
    case_slide("Ca luyện 3 — RIF và type 3",
        "Bệnh nhân thất bại chuyển phôi lặp lại, type 3 chạm nội mạc nhưng không lồi buồng tử cung.",
        "Bước tiếp theo trước khi quyết định mổ là gì?",
        "Đánh giá lại buồng tử cung bằng 3D hoặc nội soi, loại trừ lạc nội mạc, polyp nội mạc, viêm nội mạc, ứ dịch vòi trứng và yếu tố phôi; rồi mới hội chẩn.",
        ["P131", "P201"])
    qa_mcq_slide("Tự kiểm nhanh cuối note",
        "Bệnh nhân 34 tuổi, chưa có phôi, AMH bình thường, type 2 lồi buồng tử cung ~3 cm, chưa thiếu máu. Bước ưu tiên trước khi vào IVF?",
        ["A. Mổ buồng tử cung ngay qua nội soi buồng tử cung.",
         "B. Tạo và trữ phôi trước, mổ tử cung sau nếu cần.",
         "C. Theo dõi và chuyển phôi tươi khi chu kỳ thuận lợi.",
         "D. Đợi chảy máu nặng rồi xử trí."],
        "B",
        ["T15", "T20", "P125"],
        "Bóc u type 2 một thì có thể sẵn sàng trước chuyển phôi nếu không mở buồng; nhưng để bảo vệ phôi và có lựa chọn, tạo phôi trước vẫn an toàn hơn.",
        "Lấy phôi từ noãn tốt rồi sửa tử cung khi đã có phôi trữ giúp tránh mất cơ hội do biến chứng mổ. Tuy nhiên nếu buồng tử cung méo rõ, mổ trước vẫn đúng.")
    summary_slide("Take-home cá nhân",
        ["Điều trị bệnh nhân, không điều trị hình ảnh.",
         "FIGO + buồng tử cung là ngôn ngữ quyết định ART.",
         "Type 0–2 là nhóm rõ nhất, cần sửa buồng tử cung trước chuyển phôi.",
         "Type 3 là vùng xám riêng, không gộp chung type 4.",
         "Type 5–7 nhỏ và 4 nhỏ ở DOR thường không đáng trì hoãn IVF.",
         "Thuốc giảm triệu chứng không chứng minh buồng tử cung sẵn sàng.",
         "Tạo và trữ phôi là chiến lược thời gian khi noãn là nút nghẽn.",
         "Trước chuyển phôi, phải chứng minh buồng tử cung."],
        ["P222", "P246"])
    refs_slide()


build_deck()

# Forbidden-source guard: generated text must not mention side source files.
deck_text = json.dumps(slides, ensure_ascii=False)
for name in FORBIDDEN_SOURCE_NAMES:
    if name in deck_text and name != ".md":
        raise SystemExit(f"Forbidden source name leaked into deck: {name}")

deck = {
    "meta": {
        "title": "U xơ cơ tử cung và ART/IVF",
        "subtitle": "Ghi chú cá nhân · 9 phần · Dựng từ DOCX nguồn",
        "author": "",
        "specialty": "",
        "date": DATE,
        "source_docx": str(SOURCE_DOCX),
        "source_docx_sha256": DOCX_HASH,
    },
    "slides": slides,
}
manifest = {
    "source_docx": str(SOURCE_DOCX),
    "source_docx_sha256": DOCX_HASH,
    "paragraph_count_minimum": MIN_PARAGRAPHS,
    "table_count": EXPECTED_TABLES,
    "required_backbone_tables": ["T3", "T5", "T11", "T15", "T20", "T21", "T24"],
    "image_policy": "zero embedded factual images; native shapes/tables only",
    "show_page_numbers": False,
    "author_signature": False,
    "slides": manifest_slides,
}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
PROV_OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {OUT} ({len(slides)} slides)")
print(f"Saved {PROV_OUT} ({len(manifest_slides)} provenance entries)")
print(f"Source: {SOURCE_DOCX}")
print(f"DOCX SHA256: {DOCX_HASH}")
