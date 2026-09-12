# -*- coding: utf-8 -*-
"""build_from_md_pptx.py — render bài cô gửi.md sang PPTX.

Đọc trực tiếp file Markdown, dựng deck JSON trong memory, render qua
slider3636.py, patch speaker notes với template
Làm gì? / Tại sao? / Nếu bỏ qua/làm sai? / Nguồn MD:.
"""

import importlib.util
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pptx import Presentation

ROOT = Path(__file__).parent
ENGINE = ROOT.parents[1] / "10_Script Python" / "slider3636.py"
SOURCE_MD = ROOT.parents[1] / "bài cô gửi.md"
OUT = ROOT / "US_Monitoring_Ovarian_Stimulation_from_MD_2026-07-14.pptx"

NOTE_TEMPLATE = (
    "Làm gì? {action}\n"
    "Tại sao? {why}\n"
    "Nếu bỏ qua/làm sai? {risk}\n"
    "Nguồn MD: {src}"
)


def load_slider():
    spec = importlib.util.spec_from_file_location("slider3636", ENGINE)
    slider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(slider)
    return slider


def parse_md_pages(text):
    """Trả về list[(page_label, section_path, body_text)]."""
    pages = []
    current_page = "(đầu)"
    current_path = []
    body_buf = []

    def flush():
        if body_buf:
            body = "\n".join(body_buf).strip()
            if body:
                pages.append((current_page, " / ".join(current_path), body))
            body_buf.clear()

    for line in text.splitlines():
        m = re.match(r"^##\s+Trang\s+(\d+)\s*$", line.strip())
        if m:
            flush()
            current_page = f"Trang {m.group(1)}"
            continue
        if line.startswith("## "):
            flush()
            current_path = [line[3:].strip()]
            continue
        if line.startswith("### "):
            flush()
            current_path = current_path[:1] + [line[4:].strip()]
            continue
        body_buf.append(line)
    flush()
    return pages


def src_for(page, section):
    return f"{page}, mục {section}" if section else page


def s(kind, **kw):
    d = {"type": kind}
    d.update(kw)
    return d


def title_slide():
    return s(
        "title",
        variant="split_dark",
        title="Siêu âm theo dõi quá trình kích thích buồng trứng",
        subtitle="Bài học ART / IVF — dựng trực tiếp từ Markdown 'bài cô gửi.md'",
        author="",
        specialty="",
        date="2026-07-14",
        note=NOTE_TEMPLATE.format(
            action="Đọc tiêu đề + outline để nắm bố cục 7 phần.",
            why="Giúp người học định hướng trước khi vào chi tiết lâm sàng.",
            risk="Đọc lan man sẽ khó nhớ quyết định theo ngày.",
            src=src_for("Trang 85", "Chương 5 — đại cương"),
        ),
    )


def outline_slide():
    return s(
        "outline",
        variant="numbered",
        title="Bản đồ bài học",
        chapters=[
            "0. Đại cương",
            "1. Dự trữ và đáp ứng buồng trứng",
            "2. Cơ sở sinh lý kích thích",
            "3. Các phác đồ kích thích buồng trứng",
            "4. Thời điểm và liều FSH khởi đầu",
            "5. Theo dõi trong quá trình kích thích",
            "6. Trưởng thành noãn",
            "7. Đông phôi toàn bộ và kết luận",
        ],
        note=NOTE_TEMPLATE.format(
            action="Đọc outline để biết các phần theo thứ tự Chương 5.",
            why="Bài cô gửi chia thành 7 mục lớn theo sách; outline giúp tra cứu nhanh.",
            risk="Bỏ qua outline sẽ khó map từ slide về trang sách.",
            src=src_for("Trang 85–105", "Chương 5"),
        ),
    )


def section_slide(part, title, subtitle):
    return s(
        "section",
        variant="number_block",
        part_number=str(part),
        part_title=title,
        part_subtitle=subtitle,
        note=NOTE_TEMPLATE.format(
            action=f"Nêu tầm quan trọng của phần {part} trước khi vào chi tiết.",
            why="Đánh dấu mốc chuyển phần giúp ghi nhớ theo khối.",
            risk="Không đánh dấu sẽ trộn lẫn kiến thức các phần.",
            src=src_for(f"Trang 85–{100 + part}", f"Phần {part}"),
        ),
    )


def content_slide(title, points, page, section, action, why, risk):
    return s(
        "content",
        title=title,
        points=points,
        note=NOTE_TEMPLATE.format(
            action=action,
            why=why,
            risk=risk,
            src=src_for(page, section),
        ),
    )


def definition_slide(term, definition, page, section):
    return s(
        "definition",
        variant="term_box",
        term=term,
        definition=definition,
        note=NOTE_TEMPLATE.format(
            action=f"Phát biểu chính xác định nghĩa của '{term}'.",
            why="Định nghĩa là nền cho mọi quyết định phác đồ.",
            risk="Định nghĩa sai sẽ dẫn đến chọn sai phác đồ.",
            src=src_for(page, section),
        ),
    )


def two_col(title, lt, lp, rt, rp, page, section, action, why, risk):
    return s(
        "two_column",
        title=title,
        left_title=lt,
        left_points=lp,
        right_title=rt,
        right_points=rp,
        variant="vs_compare",
        note=NOTE_TEMPLATE.format(
            action=action,
            why=why,
            risk=risk,
            src=src_for(page, section),
        ),
    )


def table_slide(title, headers, rows, page, section, action, why, risk):
    return s(
        "table",
        variant="comparison_highlight",
        title=title,
        headers=headers,
        rows=rows,
        note=NOTE_TEMPLATE.format(
            action=action,
            why=why,
            risk=risk,
            src=src_for(page, section),
        ),
    )


def checklist_slide(title, items, page, section, action, why, risk):
    return s(
        "criteria",
        variant="score_points",
        title=title,
        items=[{"text": i, "points": "✓"} for i in items],
        note=NOTE_TEMPLATE.format(
            action=action,
            why=why,
            risk=risk,
            src=src_for(page, section),
        ),
    )


def big_number_slide(title, stats, page, section, action, why, risk):
    return s(
        "big_number",
        variant="single_hero",
        title=title,
        stats=stats,
        note=NOTE_TEMPLATE.format(
            action=action,
            why=why,
            risk=risk,
            src=src_for(page, section),
        ),
    )


def summary_slide(title, points, page, section):
    return s(
        "summary",
        variant="takeaways",
        title=title,
        points=points,
        note=NOTE_TEMPLATE.format(
            action="Đọc chậm 5 take-home để củng cố trước khi đóng bài.",
            why="Tăng độ bền kiến thức theo y học nhận thức.",
            risk="Bỏ qua dễ quên chi tiết quan trọng giữa các phần.",
            src=src_for(page, section),
        ),
    )


def refs_slide():
    return s(
        "references",
        variant="numbered",
        title="Tài liệu tham khảo (theo bài cô gửi)",
        refs=[
            "ESHRE 2020 — hướng dẫn lựa chọn phác đồ, liều FSH khởi đầu, trưởng thành noãn (Trang 101–102).",
            "Sunkara et al. — số noãn tối ưu để đạt tỷ lệ có thai cao nhất (~15 noãn) (Trang 87).",
            "Howles — khái niệm cửa sổ LH (Trang 89).",
            "La Marca — định liều FSH khởi đầu theo dự trữ buồng trứng (Trang 95).",
            "Nyboe và cộng sự — định liều theo cân nặng và AMH (follitropin delta) (Trang 95–96).",
            "Liu và cộng sự — kích thích buồng trứng kép ở bệnh nhân >38 tuổi (Trang 93, 99).",
            "Hồ Sỹ Hùng và cộng sự — trưởng thành noãn kép ở bệnh nhân giảm dự trữ (Trang 105).",
            "Khalaf Y và cộng sự — tăng liều không cải thiện kết quả khi đáp ứng kém (Trang 96).",
            "Kuang Yanping — báo cáo đầu tiên về duo-stimulation (Trang 93).",
        ],
        note=NOTE_TEMPLATE.format(
            action="Dùng nguồn này khi cần đối chiếu lại trong bài giảng.",
            why="Bài cô gửi đã dẫn nguồn theo từng trang, dễ truy ngược.",
            risk="Không đối chiếu sẽ khó phân biệt khuyến cáo vs kinh nghiệm cá nhân.",
            src=src_for("Trang 85–105", "Kết luận"),
        ),
    )


def build_deck():
    slides = [title_slide(), outline_slide()]

    # ═══ 0. ĐẠI CƯƠNG ═══
    slides.append(section_slide(0, "Đại cương", "Vì sao siêu âm theo dõi là trụ cột trong KTBT?"))
    slides.append(content_slide(
        "Kích thích buồng trứng (KTBT) trong IVF/ICSI",
        [
            "KTBT là bước nền tảng — quyết định số và chất lượng noãn thu được.",
            "Theo dõi giúp: đánh giá dự trữ, định liều FSH khởi đầu, điều chỉnh liều, bổ sung antagonist, quyết định thời điểm trưởng thành noãn và phát hiện sớm nguy cơ quá kích buồng trứng (OHSS).",
            "Liều khởi đầu quá thấp → nang thoái hoá; liều quá cao → OHSS và tăng chi phí.",
        ],
        "Trang 85", "I. Đại cương",
        action="Đọc mục đích và 4 lợi ích theo dõi.",
        why="Khung đầu để nhớ toàn bộ mục tiêu của theo dõi KTBT.",
        risk="Quên mục đích sẽ xem nhẹ việc đo lặp lại.",
    ))
    slides.append(content_slide(
        "Hai khái niệm nền: kích thích so với trưởng thành noãn",
        [
            "Kích thích buồng trứng (ovarian stimulation): dùng thuốc để kích thích nang phát triển — áp dụng cho bơm tinh trùng.",
            "Kích thích có kiểm soát (COH): vừa kích thích nang vừa kiểm soát LH tránh hoàng thể sớm — áp dụng cho IVF.",
            "Kích thích phóng noãn (trigger): dùng thuốc để phóng noãn và giúp noãn chuyển từ MI sang MII.",
        ],
        "Trang 87", "II. Cơ sở lý thuyết",
        action="Phân biệt rõ 3 khái niệm trước khi học phác đồ.",
        why="Ba khái niệm thường bị gộp vào 'kích thích'.",
        risk="Gộp khái niệm dẫn đến chọn sai thời điểm trigger.",
    ))

    # ═══ 1. DỰ TRỮ VÀ ĐÁP ỨNG ═══
    slides.append(section_slide(1, "Dự trữ và đáp ứng buồng trứng", "AFC, AMH, tuổi, FSH — và chỉ số FOI/FORT"))
    slides.append(content_slide(
        "Các yếu tố đánh giá dự trữ buồng trứng",
        [
            "Tuổi bệnh nhân: tuổi càng cao, dự trữ càng giảm; ≥35 tuổi tỷ lệ bất thường nhiễm sắc thể tăng.",
            "FSH đầu chu kỳ kinh: FSH >10 IU/L → dự trữ giảm, kích thích khó khăn.",
            "Số nang thứ cấp (AFC) và AMH: hai chỉ số được dùng nhiều nhất hiện nay.",
            "Tiền sử đáp ứng các chu kỳ trước và cân nặng cũng được tham khảo.",
        ],
        "Trang 85–86", "1. Dự trữ buồng trứng",
        action="Liệt kê 4 yếu tố chính trước mỗi ca KTBT.",
        why="Dự trữ quyết định liều FSH khởi đầu và chiến lược phác đồ.",
        risk="Bỏ AFC/AMH sẽ định liều sai, lãng phí gonadotropin.",
    ))
    slides.append(content_slide(
        "AFC — đếm nang thứ cấp 2–9 mm đầu chu kỳ",
        [
            "AFC = số nang đường kính 2–9 mm đếm vào ngày đầu chu kỳ kinh.",
            "Phản ánh đoàn hệ nang được tuyển chọn từ trước, sẽ phát triển trong chu kỳ phụ thuộc FSH.",
            "Đánh giá thêm: độ đồng đều của các nang và tiếp cận của đầu dò với buồng trứng.",
            "Nang không đồng đều → một số noãn trưởng thành, một số thoái hoá/non.",
            "Buồng trứng xa đầu dò → khó chọc hút; nghi ngờ viêm dính, kéo cao, ảnh hưởng tưới máu.",
        ],
        "Trang 86", "1.1. AFC",
        action="Đếm AFC bằng đầu dò âm đạo tần số cao vào ngày 2–4.",
        why="AFC là chỉ số thực hành quan trọng nhất để định liều.",
        risk="Bỏ sót nang nhỏ 2–4 mm sẽ định liều thấp hơn cần thiết.",
    ))
    slides.append(content_slide(
        "AMH và các chỉ số khác",
        [
            "AMH do tế bào hạt của nang nhỏ và nang có hốc bài tiết; ức chế tuyển chọn nang.",
            "AMH không đổi trong chu kỳ kinh → lấy máu được bất kỳ ngày nào; thuận tiện hơn FSH.",
            "Buồng trứng đa nang → AMH cao, nang không trưởng thành; giảm dự trữ → AMH rất thấp.",
            "FSH đầu chu kỳ chủ yếu xem xét khi AFC và AMH thấp; FSH cao trong giảm dự trữ → tiên lượng kém hơn.",
            "Số noãn tối ưu để đạt tỷ lệ có thai cao nhất (Sunkara) là khoảng 15; tăng hơn không tăng tỷ lệ có thai mà tăng OHSS.",
        ],
        "Trang 87", "1.2–1.3",
        action="Đo AMH bất kỳ ngày nào; phối hợp AFC để phân nhóm đáp ứng.",
        why="Hai chỉ số bổ sung cho nhau, dùng đồng thời.",
        risk="Chỉ dựa FSH sẽ bỏ sót nhiều ca giảm dự trữ nhẹ.",
    ))
    slides.append(two_col(
        "Đáp ứng buồng trứng vs dự trữ buồng trứng",
        "Dự trữ buồng trứng",
        [
            "Khả năng tích trữ nang noãn còn lại.",
            "Phản ánh bởi tuổi, AFC, AMH.",
            "Không đổi theo từng chu kỳ.",
        ],
        "Đáp ứng buồng trứng",
        [
            "Khả năng nang phát triển khi kích thích.",
            "Phản ánh qua FOI (noãn/AFC) và FORT (nang trưởng thành/AFC).",
            "Phụ thuộc phác đồ và liều.",
        ],
        "Trang 85", "1. Dự trữ và đáp ứng",
        action="Phân biệt dự trữ (có sẵn) và đáp ứng (thực hiện được).",
        why="Dự trữ tốt chưa chắc đáp ứng tốt.",
        risk="Nhầm dẫn đến chọn phác đồ không phù hợp.",
    ))

    # ═══ 2. CƠ SỞ SINH LÝ ═══
    slides.append(section_slide(2, "Cơ sở sinh lý của kích thích", "Ngưỡng và cửa sổ FSH, LH; giả thuyết hai hormon hai tế bào"))
    slides.append(definition_slide(
        "Ngưỡng FSH",
        "Nồng độ FSH mà trên giá trị này nang noãn sẽ phát triển. Mỗi nang có một ngưỡng riêng.",
        "Trang 88", "2. Cơ sở lý thuyết",
    ))
    slides.append(definition_slide(
        "Cửa sổ FSH",
        "Khoảng thời gian nồng độ FSH nằm trên ngưỡng. Cửa sổ đủ dài để nhiều nang cùng phát triển và tránh thoái hoá.",
        "Trang 88", "2. Cơ sở lý thuyết",
    ))
    slides.append(definition_slide(
        "Ngưỡng LH và cửa sổ LH",
        "Theo Howles, có một khoảng nồng độ LH đảm bảo nang phát triển bình thường; quá cao gây thoái hoá/hoàng thể sớm, quá thấp nang không phát triển.",
        "Trang 89", "2. Cơ sở lý thuyết",
    ))
    slides.append(content_slide(
        "Giả thuyết hai hormon, hai tế bào",
        [
            "LH kích thích tế bào vỏ bài tiết androgen; androgen được FSH 'thơm hoá' thành estrogen trong tế bào hạt.",
            "Thiếu LH → giảm quá trình thơm hoá → giảm estrogen trong dịch nang và huyết thanh.",
            "Phác đồ KTBT phải: nâng FSH trên ngưỡng và kéo dài cửa sổ FSH; đồng thời kiểm soát đỉnh LH để tránh hoàng thể sớm.",
        ],
        "Trang 88", "2. Cơ sở lý thuyết",
        action="Vẽ/đọc lại giả thuyết hai hormon hai tế bào khi học.",
        why="Giải thích vì sao cần cả FSH và LH đầy đủ.",
        risk="KTBT chỉ dùng FSH đơn thuần có thể thiếu estrogen.",
    ))
    slides.append(content_slide(
        "Lý thuyết tuyển chọn nang và KTBT kép",
        [
            "Đầu chu kỳ một đoàn hệ nang được tuyển chọn; 1–2 nang vượt trội, các nang khác thoái hoá (tuyển chọn đơn).",
            "Hiện đã chứng minh có nhiều làn sóng tuyển chọn trong một chu kỳ — thường 2 đợt (đầu pha nang và đầu pha hoàng thể).",
            "Đây là cơ sở cho duo-stimulation và 'random start'.",
            "DuoStim chỉ nên áp dụng cho giảm dự trữ buồng trứng hoặc bảo tồn sinh sản cần chạy đua với thời gian (hoá/xạ trị).",
        ],
        "Trang 89–90", "4. Thời điểm KTBT",
        action="Xác định làn sóng tuyển chọn trước khi quyết định thời điểm bắt đầu.",
        why="Giải thích vì sao có thể bắt đầu KTBT bất kỳ ngày nào (random start).",
        risk="Lạm dụng random start ngoài chỉ định sẽ không cải thiện kết quả.",
    ))

    # ═══ 3. PHÁC ĐỒ KTBT ═══
    slides.append(section_slide(3, "Các phác đồ kích thích buồng trứng", "Agonist (dài/ngắn), Antagonist, PPOS, DuoStim"))
    slides.append(table_slide(
        "Hai nhóm phác đồ chính",
        ["Phác đồ", "Cách kiểm soát LH", "Ưu điểm", "Hạn chế", "Vai trò hiện nay"],
        [
            ["Agonist (dài/ngắn)", "Dùng GnRH agonist ức chế vùng dưới đồi–tuyến yên", "Nang đồng đều, chất lượng noãn tốt (phác đồ dài)", "Dài ngày, nhiều gonadotropin, OHSS cao hơn", "Hiếm dùng"],
            ["Antagonist", "GnRH antagonist từ ngày 5–6 FSH", "Ngắn ngày, an toàn, có thể trigger bằng agonist", "Linh hoạt tuỳ trung tâm", "Phổ biến nhất"],
            ["PPOS", "Progestin (dyhydrogesterone 30 mg/ngày) cùng FSH", "Ức chế đỉnh LH, đơn giản", "Luôn phải đông phôi toàn bộ", "Chỉ định chọn lọc"],
            ["Mild stimulation", "Clomiphene citrate hoặc aromatase inhibitor + FSH ≤150 IU", "Ít thuốc, chi phí thấp", "Ít noãn hơn", "Hiệu quả tương đương antagonist ở giảm dự trữ"],
        ],
        "Trang 90–93", "3. Phác đồ",
        action="Đối chiếu 4 nhóm phác đồ theo bảng này.",
        why="Mỗi phác đồ có chỉ định riêng, không thay thế nhau tuỳ tiện.",
        risk="Chọn sai phác đồ dẫn đến kết quả thấp hoặc OHSS.",
    ))
    slides.append(content_slide(
        "Phác đồ dài (long protocol)",
        [
            "Pha 1: GnRH agonist từ giữa pha hoàng thể chu kỳ trước ~12–14 ngày để ức chế tuyến yên hoàn toàn (LH <5 IU/L, E2 <50 pg/L).",
            "Pha 2: thêm gonadotropin ngoại sinh, tiếp tục agonist giảm ½ liều cho đến ngày trưởng thành noãn.",
            "Ưu điểm: nang đồng đều, chất lượng noãn tốt. Nhược: kéo dài, tốn thuốc, OHSS cao hơn — nhất với buồng trứng đa nang.",
            "Hiện nay gần như rất ít sử dụng.",
        ],
        "Trang 91", "3.1. Phác đồ dài",
        action="Áp dụng khi cần kiểm soát chặt và chất lượng noãn ưu tiên.",
        why="Đây là phác đồ 'chuẩn' cũ, cần hiểu để thấy vì sao antagonist thay thế.",
        risk="Dùng cho bệnh nhân đa nang dễ OHSS nặng.",
    ))
    slides.append(content_slide(
        "Phác đồ ngắn (flare-up)",
        [
            "Lợi dụng tác dụng flare-up của agonist để tăng FSH nội sinh, kết hợp FSH ngoại sinh.",
            "Không kiểm soát tốt LH nội sinh → nang không đồng đều, chất lượng noãn thường không tốt.",
            "Thường áp dụng cho bệnh nhân lớn tuổi giảm dự trữ; hiện nay gần như ít dùng.",
            "Bắt đầu GnRH agonist từ ngày 2 chu kỳ cùng FSH, theo dõi bằng siêu âm và hormon.",
        ],
        "Trang 91", "3.2. Phác đồ ngắn",
        action="Cân nhắc cho bệnh nhân lớn tuổi, dự trữ giảm.",
        why="Một lựa chọn 'cứu vãn' nhưng không phải mặc định.",
        risk="Không kiểm soát LH dẫn đến chất lượng noãn kém.",
    ))
    slides.append(content_slide(
        "Phác đồ đối vận (antagonist)",
        [
            "Hiện áp dụng cho phần lớn bệnh nhân — lấy bệnh nhân làm trung tâm, ngắn ngày, ít OHSS.",
            "Antagonist ức chế đỉnh LH tốt; chất lượng noãn tương đương phác đồ dài.",
            "Có thể trưởng thành noãn bằng agonist trong nguy cơ OHSS.",
            "Hai cách dùng: cố định (ngày 5 hoặc 6) và linh hoạt (khi nang lớn nhất ≥14 mm và không muộn hơn ngày 7).",
            "Gonadotropin dùng từ ngày 2–3 chu kỳ kinh.",
        ],
        "Trang 92", "3.3. Antagonist",
        action="Chọn antagonist cố định ngày 5–6 cho hầu hết ca.",
        why="Đơn giản, an toàn, có thêm lựa chọn trigger agonist.",
        risk="Phác đồ linh hoạt quên siêu âm ngày 6 sẽ bỏ lỡ thời điểm antagonist.",
    ))
    slides.append(two_col(
        "Antagonist cố định vs linh hoạt",
        "Cố định (fixed)",
        [
            "Bắt đầu ngày 5 hoặc 6 FSH.",
            "Không phụ thuộc nang, dễ vận hành.",
            "Ít lỗi dùng muộn antagonist.",
        ],
        "Linh hoạt (flexible)",
        [
            "Bắt đầu khi nang lớn nhất ≥14 mm.",
            "Không muộn hơn ngày 7 FSH.",
            "Có thể giảm ngày dùng antagonist ở một số ca.",
            "Đòi hỏi siêu âm đúng ngày.",
        ],
        "Trang 92", "3.3. Antagonist",
        action="Chọn cố định khi trung tâm đông hoặc bệnh nhân khó tái khám đúng hẹn.",
        why="Cố định giảm lỗi vận hành; linh hoạt tiết kiệm thuốc ở ca thuận lợi.",
        risk="Linh hoạt + siêu âm trễ → LH surge, hỏng chu kỳ.",
    ))
    slides.append(content_slide(
        "Phác đồ nhẹ, PPOS và duo-stimulation",
        [
            "Mild stimulation: clomiphene citrate hoặc aromatase inhibitor + FSH ≤150 IU — hiệu quả không thua antagonist ở giảm dự trữ.",
            "DuoStim (Kuang Yanping): 2 đợt KTBT trong 1 chu kỳ; chỉ định giảm dự trữ nặng hoặc bảo tồn sinh sản cần chạy đua thời gian.",
            "PPOS: dyhydrogesterone 30 mg/ngày từ khi bắt đầu FSH — ức chế LH, LUÔN đông phôi toàn bộ.",
        ],
        "Trang 93", "3.4. Phác đồ khác",
        action="Dùng mild/PPOS/DuoStim trong chỉ định chọn lọc.",
        why="Mỗi phác đồ giải quyết một bài toán cụ thể.",
        risk="Dùng PPOS rồi chuyển phôi tươi sẽ hỏng chu kỳ.",
    ))

    # ═══ 4. THỜI ĐIỂM VÀ LIỀU ═══
    slides.append(section_slide(4, "Thời điểm bắt đầu và liều FSH khởi đầu", "Định liều theo La Marca, Nyboe; ESHRE khuyến cáo ≤300 IU"))
    slides.append(content_slide(
        "Khi nào bắt đầu kích thích buồng trứng?",
        [
            "Phác đồ dài: bắt đầu agonist giữa pha hoàng thể (khoảng ngày 21), chuyển FSH sau khi ức chế hoàn toàn.",
            "Phác đồ ngắn hoặc antagonist: bắt đầu FSH ngày 2–4 chu kỳ, khi đoàn hệ nang thứ cấp đã tuyển mộ.",
            "Random start: bắt đầu bất kỳ thời điểm nào trong chu kỳ — chỉ định bảo tồn sinh sản, LUÔN đông phôi toàn bộ.",
        ],
        "Trang 94", "4. Thời điểm KTBT",
        action="Chọn thời điểm bắt đầu theo phác đồ và mục tiêu.",
        why="Bắt đầu sai ngày làm lệch pha nang và nội mạc.",
        risk="Random start ngoài chỉ định không tăng số noãn tốt.",
    ))
    slides.append(content_slide(
        "Liều FSH khởi đầu và điều chỉnh",
        [
            "Liều khởi đầu dựa vào: cân nặng, AMH, AFC, FSH đầu chu kỳ, tiền sử đáp ứng.",
            "Có thể dùng bảng của La Marca (tuổi, FSH cơ bản, AMH) hoặc theo AMH + cân nặng (Nyboe, follitropin delta).",
            "Liều tối đa không quá 300 đơn vị/ngày — ESHRE khuyến cáo.",
            "Đáp ứng kém đã dùng liều cao → tăng liều không cải thiện kết quả (Khalaf Y).",
        ],
        "Trang 95–96", "5. Liều FSH khởi đầu",
        action="Định liều theo bảng La Marca hoặc Nyboe, không vượt 300 IU/ngày.",
        why="Định liều đúng giúp cân bằng đáp ứng và OHSS.",
        risk="Tăng liều quá 300 IU chỉ tốn thêm thuốc, không tăng noãn.",
    ))

    # ═══ 5. THEO DÕI TRONG KTBT ═══
    slides.append(section_slide(5, "Theo dõi trong quá trình kích thích", "Siêu âm, nội tiết, niêm mạc tử cung"))
    slides.append(content_slide(
        "Đánh giá trước khi bắt đầu KTBT (baseline)",
        [
            "Siêu âm AFC và phát hiện nang tồn dư, nang lạc nội mạc tử cung, bất thường tử cung (polyp, u xơ, vách ngăn).",
            "Nang tồn dư >18 mm: chọc hút hoặc chờ sang chu kỳ tiếp theo.",
            "Nang lạc nội mạc không ảnh hưởng chọc hút noãn thì không nhất thiết chọc trước KTBT.",
            "Tử cung ngả sau, cố định, đau khi ấn: nghi dính, thường do lạc nội mạc — tiên lượng không tốt.",
        ],
        "Trang 96–97", "5.1. Đánh giá trước KTBT",
        action="Làm baseline scan đầy đủ cho mọi bệnh nhân.",
        why="Phát hiện sớm bất thường quyết định chuyển phôi tươi hay đông phôi.",
        risk="Bỏ sót polyp/u xơ dưới niêm mạc sẽ giảm tỷ lệ làm tổ.",
    ))
    slides.append(content_slide(
        "Mục tiêu theo dõi trong quá trình KTBT",
        [
            "Đánh giá hiệu quả ức chế tuyến yên (phác đồ dài).",
            "Theo dõi đáp ứng buồng trứng để thay đổi liều nếu cần.",
            "Xác định thời điểm dùng antagonist (phác đồ linh hoạt).",
            "Xác định thời điểm trưởng thành noãn và phát hiện sớm OHSS.",
        ],
        "Trang 97", "5.2. Theo dõi",
        action="Lập lịch siêu âm ngày 6–7 và sau đó mỗi 1–2 ngày.",
        why="Đây là 'bản đồ' 4 điểm quyết định trong theo dõi.",
        risk="Bỏ ngày 6–7 sẽ lỡ quyết định antagonist.",
    ))
    slides.append(content_slide(
        "Theo dõi sự đáp ứng buồng trứng",
        [
            "Phác đồ dài: sau 10–12 ngày agonist, xét nghiệm LH <5 IU/L, E2 <50 pg/L, không nang tồn dư → bắt đầu FSH.",
            "Antagonist hoặc ngắn: bắt đầu FSH ngày 2–3 khi không có nang tồn dư và bất thường.",
            "Siêu âm tiếp theo ngày 6 hoặc 7: đo nang, niêm mạc, sau đó mỗi 1–2 ngày tuỳ tốc độ nang.",
            "Antagonist cố định không cần siêu âm sớm; linh hoạt bắt buộc siêu âm ngày 6.",
        ],
        "Trang 98", "5.3. Theo dõi đáp ứng",
        action="Tuân thủ mốc ngày 6–7 cho mọi ca antagonist.",
        why="Đây là thời điểm quyết định antagonist và đánh giá đáp ứng.",
        risk="Phác đồ linh hoạt quên siêu âm ngày 6 → LH surge.",
    ))
    slides.append(content_slide(
        "Kỹ thuật đo nang và phân nhóm kích thước",
        [
            "Đo từ bờ trong bên này đến bờ trong bên đối diện. Nang tròn: 1 chiều. Nang không tròn: đo 2 chiều vuông góc, lấy trung bình.",
            "Đầu chu kỳ nang thứ cấp 2–9 mm; khoảng ngày 6–7 nang vượt trội ≥12 mm, tốc độ trung bình 2 mm/ngày.",
            "Vùng kỳ vọng noãn tốt: 14–24 mm. Trên 24 mm: tỷ lệ thu hồi noãn giảm.",
            "PCOS nhiều nang nhỏ: dễ bỏ sót/đếm lặp; 3D probe giúp giảm sai số nhưng giá thành cao.",
        ],
        "Trang 99–100", "5.3. Đo nang",
        action="Đo đúng kỹ thuật, phân nhóm nang theo kích thước.",
        why="Quyết định trigger dựa vào toàn bộ cohort nang.",
        risk="Đo sai dẫn đến trigger sớm/muộn hoặc bỏ sót OHSS.",
    ))
    slides.append(content_slide(
        "Niêm mạc tử cung — đo và phân loại",
        [
            "Đo ở mặt cắt dọc, vị trí dày nhất, vuông góc đường niêm mạc; không tính dịch lòng tử cung.",
            "Ba hình thái: dạng 1 (ba lá, thuận lợi nhất), dạng 2 (tăng âm đồng nhất, kém thuận lợi), dạng 3 (trung gian).",
            "Chỉ cần đo niêm mạc có ý nghĩa vào ngày trigger hoặc 1–2 ngày trước — quyết định chuyển phôi tươi hay đông phôi.",
            "Tử cung ngả sau cố định và đau khi ấn: gợi ý dính, thường do lạc nội mạc tử cung — tiên lượng kém.",
        ],
        "Trang 100–101", "6. Niêm mạc tử cung",
        action="Đo niêm mạc 1 lần vào gần ngày trigger; đủ để tư vấn và quyết định fresh/freeze.",
        why="Tránh đo lặp gây lo lắng không cần thiết cho bệnh nhân.",
        risk="Niêm mạc <7 mm hoặc dạng 2 → cân nhắc đông phôi toàn bộ.",
    ))
    slides.append(content_slide(
        "Xét nghiệm nội tiết trong theo dõi",
        [
            "E2 hữu ích khi nghi OHSS, PCOS, đáp ứng không tương xứng; không cần thiết cho mọi ca.",
            "LH hữu ích khi nghi LH surge (linh hoạt, nang lớn nhanh); không cần ở fixed/long agonist.",
            "Progesterone hữu ích trước trigger để quyết định chuyển phôi tươi; tăng sớm → đông phôi toàn bộ.",
            "Định lượng hormon thường quy KHÔNG cải thiện tỷ lệ có thai so với chỉ siêu âm (quan sát giai đoạn đại dịch).",
        ],
        "Trang 101", "7. Nội tiết",
        action="Đặt câu: 'Kết quả này có làm thay đổi kế hoạch hôm nay?' trước khi chỉ định xét nghiệm.",
        why="Nội tiết là bổ sung, không thay thế siêu âm.",
        risk="Định lượng đầy đủ tốn máu, không cải thiện quyết định.",
    ))
    slides.append(checklist_slide(
        "Checklist trước khi rời phòng siêu âm",
        [
            "Hôm nay là ngày thứ mấy dùng FSH?",
            "Tốc độ tăng trưởng nang phù hợp so với lần trước?",
            "Đã đến lúc bắt đầu antagonist chưa (linh hoạt)?",
            "Có dấu hiệu OHSS không?",
            "Có dấu hiệu LH surge không (P4 tăng, niêm mạc thay đổi sớm)?",
            "Liều FSH có cần thay đổi không?",
            "Ngày hẹn tiếp theo?",
            "Bệnh nhân có hiểu kế hoạch không?",
        ],
        "Trang 101", "7. Nội tiết",
        action="Hoàn thành 8 mục checklist mỗi lần siêu âm.",
        why="Đảm bảo không bỏ sót quyết định quan trọng.",
        risk="Một mục thiếu có thể dẫn đến trì hoãn trigger hoặc OHSS.",
    ))

    # ═══ 6. TRƯỞNG THÀNH NOÃN ═══
    slides.append(section_slide(6, "Tiêu chuẩn và phác đồ trưởng thành noãn", "hCG, GnRH agonist, dual/double trigger"))
    slides.append(content_slide(
        "Tiêu chuẩn trưởng thành noãn",
        [
            "≥3 nang ≥17 mm HOẶC ≥2 nang ≥18 mm, tối thiểu 1/2 tổng số nang ≥14 mm.",
            "Thời gian kích thích trung bình 8–12 ngày; E2 trung bình cho mỗi nang 150–200 pmol.",
            "hCG liều 5.000–10.000 đơn vị hoặc hCG tái tổ hợp 250 mcg (tương đương 6.500 đơn vị).",
            "Sau trigger 34–36 giờ → chọc hút noãn qua đường âm đạo.",
        ],
        "Trang 102", "6.1. Tiêu chuẩn",
        action="Kiểm tra đủ 2 tiêu chuẩn trước khi trigger.",
        why="Trigger đúng thời điểm quyết định số noãn MII.",
        risk="Trigger sớm → nhiều noãn non; muộn → nang >24 mm giảm thu hồi.",
    ))
    slides.append(two_col(
        "Trigger hCG vs GnRH agonist",
        "hCG",
        [
            "Liều 5.000–10.000 IU.",
            "Ái lực với receptor mạnh gấp 200 lần LH, bán hủy dài.",
            "Dùng được cho mọi phác đồ.",
            "Nguy cơ OHSS cao hơn.",
        ],
        "GnRH agonist",
        [
            "Tạo đỉnh LH nội sinh qua tác dụng flare-up.",
            "Giảm OHSS sớm gần như tuyệt đối.",
            "Suy hoàng thể → giảm tiếp nhận niêm mạc → giảm tỷ lệ có thai ở chu kỳ tươi.",
            "Chỉ dùng với phác đồ antagonist; BẮT BUỘC đông phôi toàn bộ.",
        ],
        "Trang 103–104", "6.2–6.3",
        action="Chọn hCG cho nguy cơ thường; chọn GnRH agonist cho nguy cơ OHSS cao.",
        why="Mỗi loại trigger phù hợp một bối cảnh lâm sàng.",
        risk="Dùng agonist trigger trong phác đồ dài sẽ thất bại vì tuyến yên đã bị ức chế.",
    ))
    slides.append(content_slide(
        "Trưởng thành noãn kép (dual/double trigger)",
        [
            "Dùng cả hCG và GnRH agonist nhằm giảm OHSS nhưng giữ tỷ lệ có thai cao.",
            "Về sau mở rộng cho đáp ứng kém và tiền sử trigger kém (Ding và cộng sự).",
            "Hai cách: dual trigger (tiêm đồng thời) và double trigger (agonist trước, hCG sau).",
            "Hồ Sỹ Hùng và cộng sự: trên bệnh nhân giảm dự trữ, dual trigger tăng tỷ lệ noãn MII so với rhCG đơn thuần.",
        ],
        "Trang 104–105", "6.4. Trưởng thành noãn kép",
        action="Cân nhắc dual trigger khi đáp ứng kém hoặc tiền sử trigger cho kết quả kém.",
        why="Hai cơ chế hỗ trợ nhau, cải thiện số noãn MII.",
        risk="Dual trigger không thay thế việc đông phôi toàn bộ trong OHSS.",
    ))
    slides.append(content_slide(
        "Thất bại trưởng thành noãn và EFS rescue",
        [
            "Khoảng 3% bệnh nhân trigger bằng GnRH agonist thất bại — không có noãn khi chọc hút.",
            "Nguyên nhân: tuyến yên bị ức chế quá mạnh (agonist không tạo flare-up), hoặc không rõ nguyên nhân.",
            "Cứu vãn bằng hCG: tiêm hCG, chọc hút theo lịch hCG (34–36 giờ sau rescue).",
            "Phác đồ dài: KHÔNG dùng agonist trigger (tuyến yên đã bị ức chế).",
            "Antagonist: từ mũi antagonist đến trigger phải ≥10 giờ để đảm bảo tuyến yên đã phục hồi.",
        ],
        "Trang 104", "6.3. Lưu ý",
        action="Đo LH 8–12 giờ sau agonist trigger nếu nghi thất bại.",
        why="Phát hiện sớm để rescue bằng hCG, không mất chu kỳ.",
        risk="Bỏ sót LH thấp → chọc hút không có noãn, lãng phí cả chu kỳ.",
    ))

    # ═══ 7. ĐÔNG PHÔI VÀ KẾT LUẬN ═══
    slides.append(section_slide(7, "Đông phôi toàn bộ và kết luận", "Khi nào đông phôi toàn bộ — và tổng kết"))
    slides.append(content_slide(
        "Chỉ định đông phôi toàn bộ",
        [
            "Nguy cơ OHSS, P4 tăng sớm, niêm mạc không thuận lợi, hoặc bất kỳ lý do cần trì hoãn chuyển phôi.",
            "Trigger bằng GnRH agonist: BẮT BUỘC đông phôi toàn bộ (trừ khi có hỗ trợ hoàng thể đặc biệt).",
            "Random start và PPOS: đông phôi toàn bộ vì niêm mạc không đồng bộ với tuổi phôi.",
            "Vitrification: tỷ lệ sống sau rã >95% ở hầu hết trung tâm — chuyển phôi trữ không thua kém tươi.",
        ],
        "Trang 105", "7. Đông phôi toàn bộ",
        action="Chủ động chỉ định đông phôi toàn bộ khi có yếu tố nguy cơ.",
        why="Đông phôi toàn bộ bảo vệ bệnh nhân và không giảm tỷ lệ làm tổ.",
        risk="Cố chuyển phôi tươi khi có chống chỉ định sẽ giảm cơ hội thành công.",
    ))
    slides.append(summary_slide(
        "Tổng kết Chương 5",
        [
            "KTBT là nền tảng IVF/ICSI — theo dõi quyết định chất lượng noãn và phát hiện sớm OHSS.",
            "Siêu âm đường âm đạo (nang, niêm mạc) + xét nghiệm hormon là hai công cụ chính; siêu âm không thể thay thế.",
            "Dự trữ (AFC, AMH, tuổi, FSH) quyết định liều FSH khởi đầu; tối đa không quá 300 IU/ngày.",
            "Antagonist là phác đồ phổ biến nhất; PPOS/random start luôn đông phôi toàn bộ.",
            "Trigger chuẩn: ≥3 nang ≥17 mm hoặc ≥2 nang ≥18 mm; 34–36 giờ sau trigger chọc hút noãn.",
        ],
        "Trang 105", "III. Kết luận",
    ))
    slides.append(refs_slide())

    return {"meta": {}, "slides": slides}


def patch_notes(pptx_path, slides):
    """Đảm bảo mọi slide có notes (kể cả slide engine không nhận note)."""
    prs = Presentation(pptx_path)
    for i, slide in enumerate(prs.slides):
        spec_note = ""
        if i < len(slides):
            spec_note = slides[i].get("note", "")
        if not spec_note:
            spec_note = (
                "Làm gì? Xem nội dung slide để nắm ý chính.\n"
                "Tại sao? Giúp liên hệ với quyết định theo dõi KTBT.\n"
                "Nếu bỏ qua/làm sai? Dễ bỏ lỡ mốc quyết định ngày 6–7.\n"
                "Nguồn MD: bài cô gửi.md (Chương 5)."
            )
        slide.notes_slide.notes_text_frame.text = spec_note
    prs.save(pptx_path)


def main():
    md_text = SOURCE_MD.read_text(encoding="utf-8")
    pages = parse_md_pages(md_text)
    print(f"[info] parsed {len(pages)} page/section blocks from MD")

    slider = load_slider()
    slider.set_theme(
        palette_name="🟢 Medical Teal",
        font_name="Arial",
        size_preset="Large — hội trường lớn",
        show_pagenum=False,
    )

    deck = build_deck()
    deck["meta"] = {"title": "", "author": "", "subtitle": ""}

    slides = deck["slides"]
    errors, warnings = slider.validate_deck(slides)
    if errors:
        print("[ERROR] validate_deck:")
        for e in errors:
            print(" -", e)
        raise SystemExit(2)
    if warnings:
        print("[WARN] validate_deck:")
        for w in warnings[:20]:
            print(" -", w)

    path, count = slider.build_presentation(deck, str(OUT))
    patch_notes(path, slides)
    print(f"[OK] {count} slides -> {path}")


if __name__ == "__main__":
    main()
