# -*- coding: utf-8 -*-
"""Build the leiomyoma ART slider3636 deck from one approved DOCX source only.

Content source policy:
- The only content source is U_xo_tu_cung_ART_Infertility_2026-07-12.docx.
- Other DOCX/MD/TXT/PPTX files in the folder are deliberately ignored.
- Every non-structural slide is mapped to DOCX paragraph/table IDs in a provenance JSON.
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
DATE = "2026-07-13"
SOURCE_DOCX = ROOT / "U_xo_tu_cung_ART_Infertility_2026-07-12.docx"
OUT = ROOT / f"U_xo_tu_cung_leiomyoma_slider3636_long_{DATE}.deck.json"
PROV_OUT = ROOT / f"U_xo_tu_cung_leiomyoma_slider3636_long_{DATE}.provenance.json"
EXPECTED_SLIDES = 104
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
            if style_name.lower().startswith("heading") or text.startswith(("0.", "1.", "2.", "2A.", "3.", "4.", "5.", "6.", "7.", "8.", "9.")):
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
        action: str = "Trình bày ý chính.", why: str = "Giúp học viên ra quyết định lâm sàng.",
        risk: str = "", **kw) -> dict:
    source_ids = source_ids or []
    structural = kind in {"title", "section", "outline"}
    if not structural and not source_ids:
        raise SystemExit(f"Slide content missing source_ids: {title}")
    for sid in source_ids:
        if sid not in BLOCK_BY_ID:
            raise SystemExit(f"Slide {title!r} references missing source {sid}")
    slide = {"type": kind}
    if title:
        slide["title"] = title
    slide.update(kw)
    if kind not in {"title", "outline", "section"}:
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
    add("title", variant="split_dark", title="U xơ cơ tử cung và ART",
        subtitle="Từ mô tả tổn thương đến quyết định IVF/FET", author="Bác sĩ Ngọc Hưng",
        specialty="Sản phụ khoa + Hỗ trợ sinh sản", date=DATE)


def section(num: int, heading: str, sub: str):
    add("section", variant="number_block", part_number=str(num), part_title=heading, part_subtitle=sub)


def content(title: str, points: list[str], src: list[str], action: str, why: str, risk: str = "", numbered: bool = False):
    add("content", variant="numbered" if numbered else "bullets", title=title, points=points,
        source_ids=src, action=action, why=why, risk=risk)


def two_col(title: str, left_title: str, left: list[str], right_title: str, right: list[str], src: list[str], action: str, why: str, risk: str = "", vs: bool = False):
    add("two_column", variant="vs_compare" if vs else "cards", title=title,
        left_title=left_title, left_points=left, right_title=right_title, right_points=right,
        source_ids=src, action=action, why=why, risk=risk)


def three_col(title: str, columns: list[dict], src: list[str], action: str, why: str, risk: str = ""):
    add("three_column", variant="pillars", title=title, columns=columns,
        source_ids=src, action=action, why=why, risk=risk)


def mechanism(title: str, steps: list[tuple[str, str]], src: list[str], action: str, why: str, risk: str = ""):
    add("mechanism", variant="horizontal_steps", title=title,
        steps=[{"title": a, "description": b} for a, b in steps], outcome=why,
        source_ids=src, action=action, why=why, risk=risk)


def algorithm(title: str, steps: list[str], src: list[str], action: str, why: str, risk: str = ""):
    add("algorithm", variant="linear_flow", title=title,
        nodes=[{"text": s, "type": "start" if i == 0 else "end" if i == len(steps)-1 else "process"} for i, s in enumerate(steps)],
        source_ids=src, action=action, why=why, risk=risk)


def table_slide(title: str, headers: list[str], rows: list[list[str]], src: list[str], action: str, why: str, risk: str = ""):
    add("table", variant="standard", title=title, headers=headers, rows=rows,
        source_ids=src, action=action, why=why, risk=risk)


def summary_slide(title: str, points: list[str], src: list[str], action: str = "Tổng hợp thông điệp cần nhớ.", why: str = "Tóm tắt giúp chuyển kiến thức thành hành động."):
    add("summary", variant="takeaways", title=title, points=points, source_ids=src, action=action, why=why)


def case_slide(title: str, vignette: str, question: str, pearl: str, src: list[str]):
    add("qa_clinical", variant="pearl_card", title=title, question=question, pearl=pearl, why="Dùng ca lâm sàng để kiểm tra quyết định, không học thuộc máy móc.",
        source_ids=src, action="Thảo luận ca đại diện.", risk="Không đặt ca vào thuật toán sẽ dễ chọn mổ/IVF theo phản xạ.")


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
    add("references", variant="numbered", title="Tài liệu tham khảo từ DOCX nguồn", refs=refs[:10],
        source_ids=["P281"], action="Hiển thị nguồn chính đã có trong DOCX.", why="Không thêm reference từ ngoài DOCX.", risk="Thêm nguồn ngoài sẽ vi phạm phạm vi user yêu cầu.")


# Backbone table compressed rows from DOCX-derived table indices.
T3_ROWS = [["0–2", "Dưới niêm mạc/làm biến dạng buồng tử cung", "Ưu tiên đánh giá và sửa buồng tử cung trước chuyển phôi"], ["3", "Chạm nội mạc, không lồi buồng tử cung", "Vùng xám trong ART"], ["4", "Trong cơ không chạm buồng tử cung", "Cá thể hóa theo từng ca"], ["5–7", "Dưới thanh mạc", "Thường không mổ chỉ vì chuẩn bị IVF"], ["8", "Vị trí đặc biệt (cổ tử cung, dây chằng, ký sinh)", "Cần lập bản đồ riêng"]]
T5_ROWS = [["Cao", "Type 0–2/biến dạng buồng tử cung", "Sửa buồng tử cung trước"], ["Trung gian", "Type 3/intramural chọn lọc", "Cá thể hóa"], ["Thấp hơn", "Dưới thanh mạc nhỏ", "Thường theo dõi"], ["Thuộc về thao tác", "Cản chọc hút noãn/chuyển phôi", "Xử trí theo đường vào ART"]]
T11_ROWS = [["Siêu âm qua ngã âm đạo 2D", "Bước đầu tiên", "Không đủ nếu buồng tử cung chưa rõ"], ["Siêu âm qua ngã âm đạo 3D", "Phân biệt type 3/4, dựng bản đồ buồng tử cung", "Cần kinh nghiệm người làm"], ["Bơm nước buồng tử cung (SIS)", "Làm rõ đường viền buồng tử cung", "Rất hữu ích trước chuyển phôi"], ["Nội soi buồng tử cung", "Chẩn đoán và xử trí tổn thương buồng", "Không khảo sát hết phần cơ tử cung"], ["Cộng hưởng từ (MRI)", "Đa u/nghi adenomyosis/dấu hiệu bất thường", "Không dùng thường quy"]]
T15_ROWS = [["0–2", "Làm biến dạng buồng tử cung", "Thường sửa buồng tử cung trước chuyển phôi"], ["3", "Chạm nội mạc không lồi buồng", "Hội chẩn và cá thể hóa"], ["4", "Không chạm buồng tử cung", "Cân bằng kích thước, tuổi, số phôi"], ["5–7", "Dưới thanh mạc", "Không mổ chỉ vì IVF nếu nhỏ"], ["8", "Vị trí đặc biệt", "MRI/kế hoạch riêng"]]
T20_ROWS = [["Nội soi buồng tử cung", "Type 0–2", "Sửa buồng tử cung, bảo vệ nội mạc"], ["Nội soi ổ bụng/mổ mở/robot", "Type 3–7 chọn lọc", "Sẹo, dính, thời gian chờ"], ["Theo dõi", "Không triệu chứng, buồng tử cung ổn", "Tránh trì hoãn ART"], ["Chụp lại hình ảnh", "Buồng tử cung chưa chắc chắn", "Trước chuyển phôi/khi phôi quý"]]
T21_ROWS = [["Tạo/trữ phôi trước", "Tuổi cao/AMH thấp, u chưa cản chọc hút noãn", "Bảo vệ tuổi noãn"], ["Xử trí u trước", "Buồng tử cung méo rõ, type 0–2 lớn", "Không chuyển phôi vào buồng tử cung xấu"], ["Đánh giá lại buồng tử cung", "Sau mổ hoặc sau can thiệp", "Chứng minh buồng tử cung trước chuyển phôi"]]
T24_ROWS = [["Sắt, NSAID, tranexamic acid", "Giảm triệu chứng và sửa thiếu máu", "Không sửa được buồng tử cung"], ["Nội tiết/GnRH", "Cầu nối trước mổ, giảm chảy máu", "Không chữa được cấu trúc"], ["Bóc u (myomectomy)", "Có thể sửa buồng tử cung/lấy u", "Dính, sẹo, thời gian chờ"], ["Nút mạch, siêu âm hội tụ, đốt", "Giảm thể tích và triệu chứng", "Còn bất định về kết quả ART"]]


def build_deck():
    title_slide()
    add("objectives", variant="icon_check", title="Mục tiêu học tập",
        objectives=["Mô tả u xơ bằng ngôn ngữ FIGO và dữ liệu ART cần thiết", "Chọn xét nghiệm hình ảnh theo câu hỏi lâm sàng", "Quyết định mổ, theo dõi, tạo phôi trước hoặc chuyển phôi dựa trên buồng tử cung + tuổi noãn + triệu chứng", "Tư vấn trade-off: lợi ích sửa buồng tử cung và cái giá sẹo/dính/trì hoãn"],
        source_ids=["P001", "P018"], action="Định hướng mục tiêu bài học.", why="Người học cần biết bài này dạy quyết định ART, không chỉ mô tả bệnh.")
    add("outline", variant="tree", title="Lộ trình bài giảng", chapters=[
        {"title": "Khung lâm sàng", "sub": ["câu hỏi đúng", "dữ liệu tối thiểu"]},
        {"title": "FIGO và nguy cơ ART", "sub": ["buồng tử cung", "type 3", "tuổi noãn"]},
        {"title": "Chẩn đoán", "sub": ["Siêu âm", "Bơm nước/3D", "MRI"]},
        {"title": "Xử trí", "sub": ["Theo FIGO", "phẫu thuật", "thời điểm"]},
        {"title": "Tích hợp", "sub": ["thuật toán", "ca lâm sàng", "điểm cần nhớ"]},
    ])
    content("Vì sao u xơ quan trọng trong ART", ["U xơ rất thường gặp nhưng không phải mọi u đều cần can thiệp", "Trong ART, điều quan trọng là buồng tử cung, nội mạc, đường thao tác và thời gian của noãn", "Bài này chuyển từ mô tả bệnh sang quyết định: mổ trước, tạo phôi trước, theo dõi hay đánh giá lại"], ["P018", "P023", "P043"], "Đặt vấn đề lâm sàng.", "U xơ phổ biến nên phát hiện tình cờ dễ dẫn tới điều trị thừa.")

    section(1, "Khung tư duy lâm sàng", "Không hỏi ‘có u xơ thì mổ không?’")
    content("Câu hỏi sai: có u xơ thì mổ không?", ["Câu hỏi này bỏ qua vị trí, buồng tử cung và mục tiêu sinh sản", "Một u nhỏ trong buồng tử cung có thể quan trọng hơn u lớn dưới thanh mạc", "Mổ nhầm chỉ định có thể gây dính, sẹo và trì hoãn IVF"], ["P023", "P108", "P201"], "Sửa câu hỏi mở đầu.", "Quyết định đúng bắt đầu từ câu hỏi đúng.")
    content("Câu hỏi đúng trong phòng khám ART", ["U thuộc FIGO type nào?", "Có chạm hoặc biến dạng buồng tử cung không?", "Có gây AUB, thiếu máu, đau, chèn ép không?", "Can thiệp giúp mục tiêu ART hay chỉ làm chậm?"], ["P043", "P045", "P108"], "Dạy bộ câu hỏi ra quyết định.", "Bốn câu này thay thế phản xạ ‘cứ u xơ là mổ’. ")
    three_col("Ba đích cần giữ cùng lúc", [{"title": "Noãn", "points": ["Tuổi", "AMH/AFC", "khả năng tạo phôi"]}, {"title": "Phôi", "points": ["số phôi", "phôi quý", "chuyển tươi hay chuyển trữ"]}, {"title": "Tử cung", "points": ["buồng tử cung", "nội mạc", "sẹo/dính"]}], ["P196", "P193", "P211"], "Tách ba đích ART.", "Một quyết định tốt phải bảo vệ cả thời gian noãn và readiness tử cung.")
    two_col("Ba archetype lâm sàng", "Chỉ định rõ", ["Type 0–2", "méo buồng tử cung", "trước chuyển phôi"], "Vùng xám", ["Type 3", "type 4 lớn hoặc nhiều u", "RIF hoặc phôi quý"], ["P023", "P123", "P131", "P134"], "Nhận diện ba kiểu ca.", "Ca rõ và ca vùng xám cần cách tư vấn khác nhau.")
    two_col("Khi nào không nên trì hoãn ART", "Không nên mổ vội", ["type 5–7 nhỏ", "type 4 nhỏ", "không méo buồng tử cung", "DOR hoặc tuổi cao"], "Cần xử trí trước", ["type 0–2", "thiếu máu nặng", "cản chọc hút hoặc chuyển phôi", "dấu hiệu bất thường"], ["P134", "P196", "P201"], "Dạy điểm cân bằng thời gian.", "Noãn mất theo thời gian; tử cung có thể tối ưu sau trong nhiều ca.", vs=True)
    content("Đừng quy mọi thất bại ART cho u xơ", ["Kiểm tra phôi, nội mạc, adenomyosis, polyp, viêm nội mạc, ứ dịch vòi trứng và yếu tố nam", "U xơ có thể là một phần, không phải luôn là nguyên nhân chính", "Cần đánh giá lại buồng tử cung trước khi can thiệp lớn"], ["P201", "P222", "P246"], "Chống thiên kiến neo bám.", "RIF là hội chứng đa nguyên nhân.")
    content("Bộ dữ liệu tối thiểu trước tư vấn", ["Số lượng u + ba kích thước", "FIGO type và khoảng cách tới nội mạc", "Có/không biến dạng buồng tử cung", "Liên quan lỗ vòi/cổ tử cung/buồng trứng", "Adenomyosis/polyp/dính đi kèm"], ["P045", "P105"], "Chuẩn hóa dữ liệu đầu vào.", "Thiếu dữ liệu này thì không thể chọn đúng thứ tự IVF-mổ.")

    section(2, "Mô tả tổn thương và FIGO", "Vị trí quan trọng hơn kích thước đơn độc")
    content("Mỗi khối u cần được mô tả thế nào", ["Vị trí theo FIGO", "Kích thước 3 chiều", "Khoảng cách đến nội mạc", "Biến dạng buồng tử cung hay không", "Ảnh hưởng đường chọc hút/chuyển phôi"], ["P038", "P045", "P105"], "Dạy mô tả u theo ART.", "Mô tả đủ biến siêu âm thành quyết định.")
    table_slide("FIGO 0–8: bản đồ dựng bằng shape native", ["Nhóm", "Giải phẫu", "Ý nghĩa ART"], T3_ROWS, ["T3", "P038"], "Dựng FIGO bằng bảng native.", "DOCX không có hình, nhưng FIGO có thể dạy rõ bằng bảng/shape.")
    content("FIGO 0–2: làm biến dạng buồng tử cung", ["Type 0: trong buồng tử cung có cuống", "Type 1: phần lớn trong buồng tử cung", "Type 2: phần lớn trong cơ nhưng lồi buồng tử cung", "Đây là nhóm can thiệp rõ nhất trước chuyển phôi"], ["T3", "P038", "P123"], "Nhận diện nhóm dưới niêm mạc.", "Buồng tử cung là nơi phôi bám nên méo buồng tử cung là thông tin quyết định.")
    content("FIGO 3: chạm nội mạc nhưng không lồi buồng tử cung", ["Không thấy rõ như u dưới niêm mạc", "Nội soi buồng tử cung có thể gần bình thường", "Cần tách khỏi type 4 khi tư vấn ART", "Là vùng xám cần cá thể hóa", "Quyết định phụ thuộc kích thước, diện tiếp xúc nội mạc, tiền sử RIF hoặc phôi quý"], ["T3", "P069", "P131"], "Tách type 3 thành nhóm riêng.", "Chạm nội mạc có ý nghĩa với vi môi trường dù không méo buồng tử cung rõ.")
    content("FIGO 4: trong cơ không chạm buồng tử cung", ["Trong cơ hoàn toàn", "Quyết định theo kích thước, số lượng, triệu chứng, tuổi noãn", "Không tự động mổ chỉ vì IVF", "Cần cân bằng lợi ích chưa chắc với thời gian chờ, sẹo, dính", "Khi phân loại mơ hồ, cần 3D, bơm nước buồng tử cung, hoặc MRI theo câu hỏi"], ["T3", "P134", "P190"], "Cá thể hóa type 4.", "Type 4 là nơi điều trị thừa dễ xảy ra.")
    content("FIGO 5–7: dưới thanh mạc", ["Xa buồng tử cung hơn", "Thường ít ảnh hưởng khả năng làm tổ nếu nhỏ", "Mổ nếu có triệu chứng, xoắn, cản thao tác hoặc khối lớn", "Không mổ chỉ vì chuẩn bị IVF"], ["T3", "P123", "P201"], "Tránh mổ thừa dưới thanh mạc.", "Vị trí xa nội mạc thường không phải nút nghẽn ART.")
    content("FIGO 8 và vị trí đặc biệt", ["Cổ tử cung, dây chằng rộng, ký sinh hoặc vị trí đặc biệt", "Có thể gần bàng quang, niệu quản, mạch máu", "MRI có ích khi bản đồ phức tạp", "Cần cá thể hóa và phẫu thuật viên kinh nghiệm"], ["T3", "P041", "P101"], "Nhận diện nhóm đặc biệt.", "Không áp công thức FIGO thường gặp cho vị trí nguy cơ cao.")
    two_col("Type 3 và type 4", "Type 3", ["chạm nội mạc", "không lồi buồng tử cung", "vùng xám trong ART", "nội soi buồng tử cung có thể không thấy tổn thương rõ"], "Type 4", ["không chạm buồng tử cung", "trong cơ thật sự", "theo dõi hoặc cá thể hóa", "không tự động mổ nếu nhỏ và buồng tử cung ổn"], ["P069", "P131", "P134"], "So sánh ranh giới sát nội mạc.", "Gộp hai nhóm làm mất thông tin quan trọng cho ART.", vs=True)
    content("Checklist báo cáo siêu âm trước ART", ["FIGO type + kích thước", "khoảng cách đến nội mạc", "biến dạng buồng tử cung", "liên quan lỗ vòi/cổ tử cung", "khả năng tiếp cận buồng trứng"], ["P045", "P105"], "Chuẩn hóa báo cáo hình ảnh.", "Báo cáo tốt rút ngắn đường đi quyết định.")

    section(3, "Phân tầng nguy cơ ART", "Nguy cơ là bối cảnh, không phải nhãn cố định")
    table_slide("Nhóm nguy cơ trong ART theo DOCX", ["Nhóm", "Dấu hiệu", "Hành động"], T5_ROWS, ["T5", "P043"], "Tóm bảng nguy cơ ART.", "Bảng này chuyển FIGO thành quyết định ART.")
    content("Nhóm nguy cơ cao: buồng tử cung bị ảnh hưởng", ["Type 0–2", "biến dạng buồng tử cung", "polyp hoặc dính phối hợp cần phân biệt", "ưu tiên chứng minh và sửa buồng tử cung trước chuyển phôi"], ["T5", "P123", "P101"], "Nhận diện nhóm nguy cơ cao.", "Phôi cần buồng tử cung đủ điều kiện để làm tổ.")
    content("Nhóm trung gian: type 3 và intramural chọn lọc", ["Type 3 chạm nội mạc", "type 4 lớn hoặc nhiều u", "tiền sử RIF hoặc phôi quý", "cần hội chẩn thay vì áp công thức"], ["T5", "P131", "P134"], "Dạy xử trí vùng xám.", "Bằng chứng không đủ để biến mọi type 3/4 thành chỉ định mổ.")
    content("Nhóm thấp hơn: dưới thanh mạc nhỏ", ["Type 5–7 nhỏ", "không méo buồng tử cung", "không triệu chứng", "không cản thao tác ART"], ["T5", "P123", "P201"], "Tránh điều trị thừa.", "Mổ không cần thiết có thể tạo nguy cơ mới.")
    content("Nguy cơ kỹ thuật trong ART", ["U đẩy lệch buồng trứng", "cản đường chọc hút noãn", "làm khó chuyển phôi", "cần nhận diện trước khi kích thích buồng trứng"], ["P045", "P123", "P196"], "Đưa thao tác ART vào quyết định.", "Không chỉ buồng tử cung, đường vào ART cũng quyết định tạo phôi được hay không.")
    content("Nguy cơ do thời gian bệnh nhân", ["Tuổi", "AMH và AFC", "số phôi hiện có", "thời gian chờ sau can thiệp", "khả năng trì hoãn an toàn"], ["P196", "P193"], "Gắn tuổi noãn vào quyết định.", "Ở DOR, vài tháng trì hoãn có thể đắt hơn lợi ích mổ chưa chắc.")
    content("Bẫy: điều trị theo hình ảnh", ["Siêu âm bất thường không đồng nghĩa cần mổ", "Cần nối hình ảnh với triệu chứng và mục tiêu ART", "Theo dõi có thể là điều trị đúng", "Quyết định phải là quyết định chung với bệnh nhân"], ["P108", "P201", "P222"], "Chống điều trị theo siêu âm.", "Mổ không đúng đích có thể gây hại.")

    section(4, "Cơ chế ảnh hưởng sinh sản", "Chỉ giữ phần thay đổi quyết định")
    mechanism("Năm tầng cơ chế", [("Buồng tử cung", "hình học nơi phôi bám"), ("Nội mạc", "khả năng tiếp nhận phôi"), ("Co bóp", "nhu động tử cung"), ("Tưới máu và viêm", "vi môi trường quanh u"), ("Kỹ thuật", "chọc hút noãn và chuyển phôi")], ["P061", "P063", "P065", "P067"], "Tóm cơ chế theo tầng.", "Cơ chế giúp giải thích tại sao vị trí quan trọng hơn kích thước.")
    content("Hình học buồng tử cung", ["U lồi vào buồng tử cung thay đổi nơi phôi bám", "Có thể làm méo nội mạc dù kích thước không lớn", "Buồng tử cung là mục tiêu trực tiếp trước chuyển phôi", "Khoảng cách từ u tới nội mạc quyết định mức độ ảnh hưởng"], ["P063", "P123"], "Giải thích vai trò buồng tử cung.", "Nếu buồng tử cung xấu, phôi tốt vẫn có thể thất bại.")
    content("Nội mạc tiếp nhận phôi", ["U gần nội mạc có thể ảnh hưởng tín hiệu tiếp nhận", "Type 3 quan trọng vì chạm nội mạc", "Không thấy lồi buồng tử cung không có nghĩa hoàn toàn vô hại", "Đánh giá cần siêu âm kinh nghiệm hoặc 3D"], ["P065", "P069", "P131"], "Liên hệ nội mạc với type 3.", "Đây là lý do type 3 không nên bị gộp chung type 4.")
    content("Co bóp tử cung", ["U có thể thay đổi nhu động quanh thời điểm làm tổ", "Cơ chế này giải thích thất bại không chỉ do chiếm chỗ", "Không dùng cơ chế đơn độc để chỉ định mổ", "Đánh giá nhu động còn hạn chế trên siêu âm thường"], ["P067", "P071"], "Giải thích nhu động tử cung.", "Cơ chế hỗ trợ tư vấn nhưng quyết định vẫn cần bằng chứng và bối cảnh.")
    content("Vi môi trường và thao tác ART", ["Viêm và tưới máu cục bộ quanh u có thể ảnh hưởng nội mạc", "U cũng có thể cản chọc hút noãn hoặc chuyển phôi", "Đây là chỉ định kỹ thuật khác với chỉ định về khả năng làm tổ", "Cơ chế không đồng nghĩa tự động mổ"], ["P045", "P065", "P067", "P123"], "Gộp vi môi trường và đường vào ART.", "Cơ chế chỉ có giá trị khi nối được với hành động có lợi.")
    algorithm("Từ cơ chế đến quyết định", ["Cơ chế nghi ngờ", "Xác định FIGO và buồng tử cung", "Đánh giá triệu chứng và thời điểm ART", "Chọn: theo dõi / sửa buồng tử cung / tạo phôi trước / đánh giá lại"], ["P061", "P123", "P196", "P222"], "Chuyển cơ chế thành thuật toán.", "Cơ chế chỉ hữu ích khi dẫn đến hành động có lợi.")

    section(5, "Chẩn đoán để trả lời câu hỏi ART", "Không làm xét nghiệm cho đủ; làm để quyết định")
    content("Mục tiêu của chẩn đoán", ["Xác định FIGO và buồng tử cung", "Phân biệt tổn thương đi kèm", "Lập kế hoạch mổ hoặc ART", "Tránh chuyển phôi khi buồng tử cung chưa rõ"], ["P090", "P099", "P101"], "Định nghĩa mục tiêu chẩn đoán.", "Câu hỏi chẩn đoán quyết định xét nghiệm cần làm.")
    table_slide("So sánh công cụ hình ảnh", ["Công cụ", "Mạnh nhất khi", "Giới hạn"], T11_ROWS, ["T11", "P099"], "Tóm bảng diagnostic methods.", "Người học cần biết chọn test theo câu hỏi.")
    content("Siêu âm 3D qua ngã âm đạo", ["Mặt phẳng vành giúp nhìn quan hệ u với nội mạc", "Phân biệt type 3 với type 4 khi 2D mơ hồ", "Đo khoảng cách tới nội mạc", "Hữu ích trước chuyển phôi khi cần chứng minh buồng tử cung", "Giới hạn: phụ thuộc người làm và chất lượng máy"], ["T11", "P101"], "Chỉ định 3D đúng câu hỏi.", "3D giải quyết vấn đề mặt phẳng buồng tử cung mà 2D dễ bỏ sót.")
    content("Bơm nước buồng tử cung (SIS)", ["Làm rõ đường viền buồng tử cung", "Phát hiện u dưới niêm mạc và polyp nhỏ", "Rẻ và nhanh hơn một lần chuyển phôi thất bại", "Tránh khi đang viêm âm đạo cấp hoặc đang có thai"], ["T11", "P101"], "Chọn bơm nước khi câu hỏi là buồng tử cung.", "Bơm nước giúp chứng minh điều kiện chuyển phôi.")
    content("Nội soi buồng tử cung", ["Vừa chẩn đoán vừa điều trị tổn thương buồng tử cung", "Phù hợp cho type 0–2", "Không khảo sát phần ngoài cơ tử cung", "Can thiệp quá mức làm tăng nguy cơ dính", "Cần kết hợp siêu âm để biết vị trí u trong cơ"], ["T11", "P125"], "Đặt nội soi buồng tử cung đúng vai trò.", "Không dùng nội soi buồng tử cung để thay thế toàn bộ bản đồ u xơ.")
    content("Cộng hưởng từ (MRI)", ["Dùng khi đa u hoặc u lớn làm siêu âm khó lập bản đồ", "Nghi adenomyosis đi kèm", "Dấu hiệu bất thường nghi sarcoma hoặc STUMP", "Lập kế hoạch phẫu thuật cho ca khó", "Không dùng thường quy cho mọi bệnh nhân ART"], ["T11", "P101", "P103"], "Dùng MRI khi bản đồ 2D/3D không đủ.", "MRI có ích ở ca phức tạp nhưng không cần thường quy mọi ca.")
    algorithm("Thuật toán nâng bậc hình ảnh trước ART", ["Siêu âm 2D qua ngã âm đạo", "Ghi nhận FIGO nghi ngờ", "Buồng tử cung chưa rõ?", "Siêu âm 3D hoặc bơm nước buồng tử cung", "Nội soi buồng tử cung nếu tổn thương trong buồng", "MRI nếu đa u, u lớn, nghi adenomyosis hoặc dấu hiệu bất thường"], ["P101", "T11"], "Dạy lộ trình chẩn đoán.", "Đi từng bước giúp tránh vừa thiếu vừa thừa xét nghiệm.")
    content("Mẫu báo cáo tối thiểu", ["Số lượng và ba chiều kích thước của u", "FIGO type và vị trí", "Khoảng cách tới nội mạc", "Có hay không biến dạng buồng tử cung", "Liên quan cổ tử cung, lỗ vòi trứng, buồng trứng"], ["P105"], "Chuẩn hóa kết quả chẩn đoán hình ảnh.", "Báo cáo đủ giúp chọn đúng thứ tự IVF và mổ.")
    content("Chẩn đoán phân biệt và dấu hiệu bất thường", ["Adenomyosis đi kèm", "Polyp hoặc vách ngăn buồng tử cung", "Nghi sarcoma hoặc STUMP khi u lớn nhanh, tăng sinh mạch", "Khối buồng trứng giả u cuống"], ["P103", "P087"], "Không bỏ sót chẩn đoán khác.", "Mổ đúng u xơ nhưng sai bệnh chính vẫn thất bại.")
    content("Trước chuyển phôi: phải chứng minh buồng tử cung", ["Không giả định buồng tử cung ổn chỉ vì 2D bình thường", "Phôi quý cần buồng tử cung được chứng minh", "Đánh giá lại sau can thiệp khó hoặc kết quả siêu âm không chắc chắn", "Đừng chuyển phôi vào buồng tử cung còn mơ hồ"], ["P101", "P105", "P193"], "Chốt tiêu chuẩn trước chuyển phôi.", "Chuyển phôi là lúc cần chắc chắn về buồng tử cung.")

    section(6, "Đích điều trị trước khi chọn phương pháp", "Biết đang sửa gì trước khi can thiệp")
    content("Chọn mục tiêu điều trị trước", ["Giảm máu và đau", "Sửa thiếu máu", "Giảm thể tích khối u", "Phục hồi buồng tử cung", "Bảo vệ thời gian noãn"], ["P119", "P137", "P196"], "Dạy tư duy đặt mục tiêu trước.", "Tên phương pháp ít quan trọng hơn mục tiêu điều trị.")
    table_slide("Quyết định theo FIGO trước ART", ["FIGO", "Vấn đề chính", "Hành động"], T15_ROWS, ["T15", "P123"], "Dùng bảng quyết định FIGO.", "Đây là xương sống của phần xử trí.")
    content("Type 0–2: phục hồi buồng tử cung", ["Ảnh hưởng trực tiếp buồng tử cung", "Đường nội soi buồng tử cung thường phù hợp", "Kiểm tra lại buồng tử cung nếu ca khó", "Ưu tiên trước chuyển phôi", "Cần theo dõi nguy cơ dính sau thủ thuật"], ["T15", "P125"], "Dạy chỉ định rõ nhất.", "Sửa buồng tử cung là mục tiêu có lý nhất trước chuyển phôi.")
    content("Type 3: vùng xám", ["Chạm nội mạc", "Không lồi buồng tử cung", "Cân nhắc tiền sử ART và phôi quý", "Chưa đủ chắc để mổ mọi ca", "Quyết định cần hội chẩn và trao đổi với bệnh nhân"], ["T15", "P131"], "Tư vấn type 3 cân bằng.", "Vùng xám cần quyết định chung và hội chẩn.")
    content("Type 4: cân bằng nhiều yếu tố", ["Kích thước và số lượng u", "Triệu chứng kèm theo", "Tuổi, AMH, số phôi hiện có", "Nguy cơ phẫu thuật (sẹo, dính, thời gian chờ)", "Không dùng công thức cứng"], ["T15", "P134", "P196"], "Cá thể hóa type 4.", "Type 4 là nơi cần cân bằng nhất.")
    content("Type 5–7: thường không mổ chỉ vì IVF", ["Xa buồng tử cung", "Ít ảnh hưởng khả năng làm tổ nếu nhỏ", "Mổ khi có triệu chứng hoặc cản thao tác", "Theo dõi nếu không triệu chứng và buồng tử cung ổn"], ["T15", "P201"], "Tránh trì hoãn IVF vì u dưới thanh mạc nhỏ.", "Lợi ích mổ thấp không bù được sẹo, dính, thời gian chờ.")
    content("Triệu chứng và thiếu máu là chỉ định riêng", ["Chảy máu nhiều và thiếu máu cần xử trí", "Đau và chèn ép cần cân nhắc", "Chỉ định triệu chứng khác chỉ định vì khả năng làm tổ", "Đừng trộn hai mục tiêu khi tư vấn", "Mức Hb mục tiêu trước khi chuyển phôi"], ["P091", "P115", "P137"], "Tách chỉ định triệu chứng khỏi ART.", "Điều trị đúng triệu chứng chưa chắc tối ưu tỉ lệ sanh sống.")
    content("Đường vào ART: chọc hút noãn và chuyển phôi", ["U cản đường chọc hút noãn", "Cổ tử cung hoặc trục tử cung khó chuyển phôi", "Cần đánh giá trước khi kích thích buồng trứng", "Đây có thể là chỉ định kỹ thuật riêng"], ["P045", "P123", "P196"], "Đưa kỹ thuật ART vào kế hoạch.", "Một ca có buồng tử cung ổn vẫn có thể thất bại do không lấy được noãn hoặc không chuyển được phôi.")
    checklist_items = ["FIGO và tình trạng buồng tử cung đã rõ chưa?", "Triệu chứng và thiếu máu có cần xử trí trước?", "Tuổi, AMH và số phôi hiện có thế nào?", "Đường chọc hút noãn và chuyển phôi có thuận?", "Nguy cơ sẹo, dính và thời gian chờ?", "Bệnh nhân ưu tiên điều gì nhất?"]
    add("criteria", variant="score_points", title="Bảng kiểm quyết định chung", items=[{"text": x, "points": "✓"} for x in checklist_items], interpretation=[{"range": "Đủ dữ liệu", "label": "Có thể chọn thứ tự IVF và mổ"}, {"range": "Thiếu dữ liệu", "label": "Chụp lại hình ảnh hoặc hội chẩn trước"}], source_ids=["P108", "P196", "P222"], action="Dùng bảng kiểm trước quyết định.", why="Quyết định chung cần dữ liệu và mục tiêu rõ.")

    section(7, "Xử trí theo FIGO và bối cảnh ART", "Cùng là u xơ, hành động khác nhau")
    table_slide("Xử trí theo FIGO", ["Đường", "Nhóm", "Điểm phải nhớ"], T20_ROWS, ["T20", "P174"], "Tóm xử trí theo FIGO.", "Bảng này thay các slide phẫu thuật dàn trải.")
    content("Type 0", ["Trong buồng tử cung có cuống", "Bóc u qua nội soi buồng tử cung thường hợp lý", "Mục tiêu sửa nơi phôi bám", "Kiểm tra nền và diện cắt cuống", "Tránh đốt sâu để bảo vệ nội mạc"], ["T20", "P125"], "Xử trí type 0.", "Đây là tổn thương sửa được rõ trước chuyển phôi.")
    content("Type 1", ["Phần lớn trong buồng tử cung", "Cắt từng lớp", "Bảo vệ lớp đáy nội mạc", "Tránh đốt sâu để không hình thành sẹo dày"], ["T20", "P125"], "Xử trí type 1.", "Vừa lấy u vừa giữ nội mạc cho ART.")
    content("Type 2", ["Phần lớn trong cơ", "Nguy cơ thủng, dính, quá tải dịch", "Có thể chia hai thì", "An toàn hơn là lấy sạch bằng mọi giá"], ["T20", "P125", "P190"], "Xử trí type 2 an toàn.", "Buồng tử cung sau mổ quan trọng hơn cảm giác lấy sạch.")
    content("Type 3", ["Không thấy lồi buồng tử cung", "Chạm nội mạc", "Bằng chứng còn vùng xám", "Cần cá thể hóa và hội chẩn"], ["T20", "P131"], "Xử trí type 3.", "Không vô hại nhưng cũng không tự động mổ.")
    content("Type 4", ["Trong cơ thật sự", "Mổ nếu lớn, nhiều, có triệu chứng hoặc cản thao tác", "Cân nhắc tạo và trữ phôi trước", "Theo dõi nếu nhỏ và buồng tử cung ổn"], ["T20", "P134", "P196"], "Xử trí type 4.", "Quyết định phải cân bằng lợi ích và nguy cơ.")
    content("Type 5–7", ["Dưới thanh mạc", "Mổ khi có triệu chứng hoặc cản thao tác ART", "Không mổ chỉ vì IVF đơn thuần nếu nhỏ", "Giữ thời gian cho noãn"], ["T20", "P201"], "Xử trí type 5–7.", "Tránh tạo sẹo và dính vì lợi ích ART thấp.")
    content("Khi nào mổ trước IVF", ["Buồng tử cung méo rõ", "Type 0–2", "Thiếu máu hoặc triệu chứng nặng", "U cản chọc hút noãn hoặc chuyển phôi", "Dấu hiệu bất thường nghi ác tính"], ["P123", "P137", "P201"], "Chốt chỉ định mổ trước.", "Mổ trước có lợi khi sửa đúng nút nghẽn thật.")
    content("Khi nào không trì hoãn IVF", ["Tuổi cao hoặc DOR", "Type 4 nhỏ", "Type 5–7 nhỏ", "Không méo buồng tử cung", "Không cản thao tác ART"], ["P134", "P196", "P201"], "Chốt chỉ định không trì hoãn.", "Tạo phôi có thể là bước bảo vệ cơ hội sinh sản.")
    content("Khi nào tạo và trữ phôi trước", ["AMH hoặc AFC thấp", "Tuổi lớn", "U chưa cản chọc hút noãn", "Tử cung có thể tối ưu sau", "Phôi cần được bảo vệ trước"], ["T21", "P196"], "Dạy chiến lược tạo và trữ phôi trước.", "Noãn lão hóa nhanh hơn nhiều kế hoạch tối ưu tử cung.")

    section(8, "Phẫu thuật và cái giá của bảo tồn tử cung", "Lấy u là phá; bảo vệ tử cung là xây lại")
    content("Bóc u không phải một thủ thuật duy nhất", ["Qua nội soi buồng tử cung", "Qua nội soi ổ bụng", "Mổ mở", "Phẫu thuật robot", "Chọn theo FIGO và mục tiêu điều trị"], ["P125", "P128", "P174"], "Phân loại đường mổ.", "Tên mổ không đủ; cần biết đường vào sửa vấn đề nào.")
    two_col("Bóc u qua nội soi buồng tử cung", "Giải quyết", ["Type 0–2", "Buồng tử cung", "Chảy máu nhiều", "Trước chuyển phôi"], "Nguy cơ", ["Thủng", "Quá tải dịch", "Đốt sâu", "Dính sau mổ"], ["P125", "P190"], "Tư vấn nội soi buồng tử cung cân bằng.", "Sửa buồng tử cung có lợi nhưng cũng có nguy cơ với nội mạc.", vs=True)
    two_col("Bóc u qua nội soi ổ bụng, mổ mở, robot", "Giải quyết", ["U trong cơ lớn", "Nhiều u", "Cản thao tác ART", "Triệu chứng khối"], "Cái giá", ["Sẹo cơ tử cung", "Dính", "Thời gian chờ", "Cần theo dõi thai kỳ sau này"], ["P128", "P190", "P193"], "Tư vấn đường vào qua bụng.", "Bảo tồn tử cung không miễn phí về mặt ART.", vs=True)
    content("Type 2: an toàn hơn là lấy sạch", ["Có phần sâu trong cơ", "Không cố đào khi mất an toàn", "Có thể chia thì phẫu thuật", "Bảo vệ lớp đáy nội mạc"], ["P125", "P190"], "Dạy nguyên tắc dừng an toàn.", "Buồng tử cung lành quan trọng hơn lấy hết bằng mọi giá.")
    content("Ghi nhận khi mở vào buồng tử cung", ["U sâu gần nội mạc có thể mở vào buồng tử cung", "Ảnh hưởng thời điểm chuyển phôi", "Ảnh hưởng tư vấn thai kỳ và sinh", "Cần ghi rõ trong tường trình mổ"], ["P193", "P211"], "Nhấn mạnh ghi nhận đầy đủ.", "Thiếu thông tin này làm mất dữ liệu an toàn cho lần theo.")
    content("Nguy cơ dính và lớp đáy nội mạc", ["Tổn thương nội mạc làm tăng nguy cơ dính", "Đốt rộng hoặc tổn thương sâu có hại", "Hai diện thương đối diện dễ dính", "Phôi cần buồng tử cung lành"], ["P190", "P211", "P246"], "Giải thích dính ở mức cần thiết.", "Không lấy nội dung phẫu thuật phụ; chỉ giữ nguyên tắc có trong DOCX mega.")
    content("Nguyên tắc phòng dính", ["Hạn chế sang chấn", "Bảo vệ nội mạc lành", "Cân nhắc chia thì cho type 2", "Kiểm tra lại buồng tử cung khi nguy cơ cao"], ["P190", "P211", "P246"], "Dạy thứ tự ưu tiên phòng dính.", "Phòng dính là bảo vệ tương lai chuyển phôi.")
    content("Đánh giá lại buồng tử cung sau mổ", ["Bơm nước, siêu âm 3D hoặc nội soi buồng tử cung khi ca khó", "Trước chuyển phôi nếu phôi quý", "Khi kinh ít hoặc nghi dính", "Không giả định buồng tử cung đã tốt"], ["P193", "P211"], "Dạy đánh giá lại sau mổ.", "Điều trị xong u chưa chắc xong buồng tử cung.")
    content("Thời điểm sau nội soi buồng tử cung", ["Phụ thuộc độ sâu u và diện thương nội mạc", "Ca đơn giản có thể rút ngắn thời gian chờ", "Type 2 hoặc nhiều diện thương cần đánh giá lại buồng tử cung", "Ưu tiên buồng tử cung lành hơn số tuần cố định"], ["P193", "P211"], "Tư vấn thời điểm sau nội soi buồng tử cung.", "Đợi đúng mức giúp giảm nguy cơ mất phôi do buồng tử cung chưa lành.")
    content("Thời điểm sau bóc u đường bụng hoặc nội soi ổ bụng", ["Không có một mốc duy nhất cho mọi ca", "Phụ thuộc độ sâu đường rạch, số lớp khâu, có mở vào buồng tử cung hay không", "Cần thời gian lành sẹo cơ tử cung trước thai", "Tư vấn thai kỳ và lựa chọn sinh mổ chọn lọc"], ["P193", "P211"], "Tư vấn thời điểm sau đường bụng.", "Sẹo cơ tử cung ảnh hưởng an toàn thai kỳ.")

    section(9, "Thuốc và can thiệp không phẫu thuật", "Giảm triệu chứng không đồng nghĩa sửa buồng tử cung")
    table_slide("Ma trận tác động điều trị", ["Nhóm", "Thay đổi gì", "Không thay đổi gì"], T24_ROWS, ["T24", "P240"], "Tóm hiệu ứng điều trị.", "Bảng này ngăn nhầm mục tiêu triệu chứng với mục tiêu ART.")
    content("Sắt, NSAID, tranexamic acid", ["Sửa thiếu máu, giảm đau, giảm máu", "Không làm nhỏ u đáng kể", "Không sửa biến dạng buồng tử cung", "Rất hữu ích như cầu nối chờ mổ"], ["P137", "P141", "T24"], "Đặt thuốc triệu chứng đúng vai trò.", "Đúng cho chảy máu nhiều chưa chắc đủ cho chuyển phôi.")
    content("Nội tiết và GnRH", ["Kiểm soát chảy máu", "Giảm kích thước tạm thời", "Là cầu nối trước mổ", "Không phải điều trị cấu trúc"], ["P137", "P141", "T24"], "Dạy thuốc như cầu nối.", "Thuốc không thay thế sửa type 0–2.")
    content("Nút mạch tử cung (UAE)", ["Giảm triệu chứng ở ca chọn lọc", "Không dùng thường quy khi đang tích cực mong thai", "Lo ngại ảnh hưởng nội mạc, buồng trứng và tử cung", "Không thay thế chỉ định mổ cho ART"], ["P159", "T24"], "Tư vấn UAE theo mục tiêu sinh sản.", "Ít xâm lấn không đồng nghĩa phù hợp ART.")
    table_slide("Thay đổi gì và không thay đổi gì", ["Mục tiêu", "Có thể đạt", "Cần kiểm tra lại"], [["Máu và đau", "Thuốc và cầu nối", "Hb và triệu chứng"], ["Thể tích khối u", "GnRH, UAE, HIFU, đốt", "Buồng tử cung và thời điểm"], ["Buồng tử cung", "Bóc u chọn lọc", "Bơm nước, 3D, nội soi buồng"], ["Tuổi noãn", "Tạo và trữ phôi", "Số phôi và AMH"]], ["T24", "P196"], "Chốt ma trận mục tiêu.", "Mỗi mục tiêu cần một cách kiểm tra khác nhau.")

    section(10, "Tạo và trữ phôi và thứ tự", "Noãn và tử cung lão hóa khác nhau")
    table_slide("Quyết định tạo và trữ phôi", ["Chiến lược", "Ứng viên", "Lý do"], T21_ROWS, ["T21", "P196"], "Tóm quyết định tạo và trữ phôi.", "Đây là cầu nối giữa tuổi noãn và tối ưu tử cung.")
    content("Ưu tiên tạo và trữ phôi trước: ai phù hợp", ["Tuổi cao hoặc AMH thấp", "U chưa cản chọc hút noãn", "Buồng tử cung chưa cần sửa ngay", "Cần bảo vệ cơ hội tạo phôi", "Sẵn sàng chuyển phôi trữ sau khi tối ưu tử cung"], ["T21", "P196"], "Nhận diện nhóm tạo và trữ trước.", "Tạo phôi trước là chiến lược thời gian, không phải điều trị u.")
    content("Ưu tiên xử trí u trước: ai phù hợp", ["Type 0–2 lớn hoặc méo buồng tử cung", "U cản chọc hút noãn hoặc chuyển phôi", "Thiếu máu hoặc triệu chứng nặng", "Dấu hiệu bất thường nghi ác tính"], ["T21", "P123", "P137"], "Nhận diện nhóm xử trí u trước.", "Không nên tạo phôi rồi chuyển vào buồng tử cung chưa thể dùng.")
    two_col("Chuyển phôi tươi và chuyển phôi trữ", "Tươi", ["Ít thời gian chuẩn bị tử cung", "Tránh nếu buồng tử cung chưa rõ", "Không phù hợp khi cần mổ hoặc can thiệp"], "Trữ", ["Tách tạo phôi khỏi chuẩn bị tử cung", "Cho thời gian sửa và đánh giá lại", "Phù hợp với phôi quý và ca chọn lọc"], ["P196", "P193"], "Phân biệt thời điểm chuyển phôi.", "Chuyển phôi trữ giúp giải quyết tuần tự hai bài toán.", vs=True)
    algorithm("Thuật toán chọn thời điểm", ["Đánh giá FIGO và buồng tử cung", "Nút nghẽn là noãn hay tử cung?", "Tạo và trữ phôi nếu noãn là nút nghẽn", "Sửa buồng tử cung nếu đó là nút nghẽn", "Đánh giá lại buồng tử cung", "Chuyển phôi khi buồng tử cung sẵn sàng"], ["T21", "P196", "P193"], "Tích hợp thứ tự xử trí.", "Thuật toán giảm mâu thuẫn giữa phẫu thuật và tuổi noãn.")

    section(11, "Theo dõi và tư vấn thai kỳ", "Kết thúc can thiệp chưa phải kết thúc nguy cơ")
    content("Theo dõi khi chưa can thiệp", ["Tái khám theo triệu chứng", "Chụp lại hình ảnh khi kế hoạch ART thay đổi", "Theo dõi chảy máu và thiếu máu", "Không quên bệnh đi kèm", "Ghi nhận khi bệnh nhân quyết định chuyển sang can thiệp"], ["P211", "P222"], "Dạy theo dõi bảo tồn.", "Theo dõi có chủ đích khác với bỏ mặc.")
    content("Sau nội soi buồng tử cung", ["Theo dõi ra máu và đau", "Nghi dính nếu kinh ít rõ", "Đánh giá lại buồng tử cung ở ca nguy cơ", "Đợi buồng tử cung lành trước chuyển phôi"], ["P193", "P211"], "Dạy theo dõi sau nội soi buồng tử cung.", "Buồng tử cung sau thủ thuật là mục tiêu ART.")
    content("Sau bóc u đường bụng hoặc nội soi ổ bụng", ["Theo dõi đau và thiếu máu", "Sẹo cơ tử cung và nguy cơ vỡ tử cung", "Việc mở vào buồng tử cung và thời gian chờ", "Nguy cơ u tái phát và u còn lại"], ["P193", "P211"], "Dạy theo dõi đường bụng.", "Sẹo và u tái phát ảnh hưởng kế hoạch thai kỳ.")
    content("Tư vấn thai kỳ sau bóc u", ["Có thể cần theo dõi thai kỳ nguy cơ cao", "Kế hoạch sinh phụ thuộc độ sâu và việc mở vào buồng tử cung", "Tư vấn nguy cơ u tái phát và u còn lại", "Ghi rõ thông tin mổ cho bác sĩ sản khoa theo dõi"], ["P211", "P222"], "Dạy tư vấn thai kỳ.", "Thông tin phẫu thuật hiện tại phục vụ an toàn thai kỳ sau này.")

    section(12, "Tích hợp và kết thúc", "Từ dữ liệu đến quyết định")
    algorithm("Thuật toán quyết định ART tích hợp", ["Mô tả u xơ: FIGO và tình trạng buồng tử cung", "Đánh giá triệu chứng, thiếu máu, dấu hiệu bất thường", "Đánh giá thời gian noãn và số phôi hiện có", "Chọn: theo dõi / chụp thêm hình ảnh / mổ / tạo và trữ phôi trước", "Đánh giá lại buồng tử cung trước chuyển phôi"], ["P045", "T15", "T21", "P222"], "Tích hợp toàn bài.", "Thuật toán biến bài dài thành hành động tại phòng khám.")
    summary_slide("Điểm cần nhớ", ["Điều trị bệnh nhân, không điều trị hình ảnh", "FIGO cộng buồng tử cung là ngôn ngữ quyết định ART", "Type 0–2 rõ nhất cần sửa buồng tử cung", "Type 3 là vùng xám riêng, không gộp chung type 4", "Type 5–7 nhỏ thường không mổ chỉ vì IVF", "Thuốc giảm triệu chứng không chứng minh buồng tử cung sẵn sàng", "Tạo và trữ phôi bảo vệ tuổi noãn trong ca chọn lọc", "Trước chuyển phôi: phải chứng minh buồng tử cung"], ["P222", "P246"], "Chốt thông điệp.", "Người học cần nhớ thuật toán hơn là từng số liệu.")
    case_slide("Ca luyện quyết định 1: type 1 trước chuyển phôi", "Bệnh nhân 36 tuổi, đã có phôi trữ, siêu âm phát hiện u type 1 lồi vào buồng tử cung, không thiếu máu.", "Có nên chuyển phôi ngay không, hay cần xử trí u trước?", "Ưu tiên sửa buồng tử cung trước chuyển phôi; sau đó đánh giá lại bằng bơm nước hoặc 3D nếu diện thương rộng hoặc nghi type 2.", ["T15", "P125"])
    case_slide("Ca luyện quyết định 2: DOR và type 4 nhỏ", "Bệnh nhân 39 tuổi, AMH thấp, type 4 nhỏ trong cơ, buồng tử cung không méo, u không cản chọc hút.", "Nên mổ trước hay tạo và trữ phôi trước?", "Ưu tiên tạo và trữ phôi trước vì tuổi noãn đang là nút nghẽn; buồng tử cung ổn có thể tối ưu sau bằng theo dõi.", ["T21", "P196", "P134"])
    case_slide("Ca luyện quyết định 3: RIF và type 3", "Bệnh nhân thất bại chuyển phôi lặp lại, type 3 chạm nội mạc nhưng không lồi buồng tử cung.", "Bước tiếp theo trước khi quyết định mổ là gì?", "Đánh giá lại buồng tử cung bằng 3D hoặc nội soi, loại trừ adenomyosis, polyp và yếu tố phôi, rồi mới hội chẩn; không mổ theo phản xạ.", ["P131", "P201"])
    refs_slide()


build_deck()
if len(slides) != EXPECTED_SLIDES:
    raise SystemExit(f"Deck slide count {len(slides)} != expected {EXPECTED_SLIDES}")

# Forbidden-source guard: generated text must not mention side source files.
deck_text = json.dumps(slides, ensure_ascii=False)
for name in FORBIDDEN_SOURCE_NAMES:
    if name in deck_text and name != ".md":
        raise SystemExit(f"Forbidden source name leaked into deck: {name}")

# Do not embed extra unknown fields in the deck specs; provenance is separate.
deck = {
    "meta": {
        "title": "U xơ cơ tử cung và ART",
        "subtitle": "Dựng lại từ DOCX nguồn",
        "author": "Bác sĩ Ngọc Hưng",
        "specialty": "Sản phụ khoa + Hỗ trợ sinh sản",
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
    "expected_slide_count": EXPECTED_SLIDES,
    "image_policy": "zero embedded factual images; native shapes/tables only",
    "required_backbone_tables": ["T3", "T5", "T11", "T15", "T20", "T21", "T24"],
    "slides": manifest_slides,
}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
PROV_OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {OUT} ({len(slides)} slides)")
print(f"Saved {PROV_OUT} ({len(manifest_slides)} provenance entries)")
print(f"Source: {SOURCE_DOCX}")
print(f"DOCX SHA256: {DOCX_HASH}")
