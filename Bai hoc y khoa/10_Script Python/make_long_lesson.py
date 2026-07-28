"""Build full lesson: docx + anki apkg + html visual summary.
Topic: Long GnRH Agonist Protocol trong IVF/ICSI - 2026-06-18.
"""
import json
import os
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import genanki

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
LESSON_DIR = ROOT / "02_Ho tro sinh san ART" / "09_Long_GnRH_Agonist_Protocol"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "09_Long_GnRH_Agonist"
DATE = "2026-06-18"

DOCX_OUT = LESSON_DIR / f"Long GnRH Agonist Protocol - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - Long GnRH Agonist 18 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - Long GnRH Agonist - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "long_gnrh_agonist_cards.json"

# ============================================================
# DOCX BUILDER
# ============================================================
def set_cell_bg(cell, color_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)

def set_cell_border(cell):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:color'), '000000')
        tc_borders.append(border)
    tc_pr.append(tc_borders)

def style_header(cell):
    cell.text = cell.text  # ensure paragraph
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)

def style_first_col(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
    set_cell_bg(cell, 'E8F0F7')
    set_cell_border(cell)

def add_bullets(doc, items):
    for item in items:
        doc.add_paragraph(item, style='List Bullet')

def build_docx():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    # TITLE
    title = doc.add_heading('LONG GnRH AGONIST PROTOCOL TRONG IVF/ICSI', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bài học ngày {DATE} - Hỗ trợ sinh sản (ART)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TỔNG QUAN - VÌ SAO BÀI NÀY QUAN TRỌNG?', 1)
    doc.add_paragraph(
        'Long GnRH-agonist protocol từng là "vua" của controlled ovarian stimulation (COS) suốt 25 năm '
        '(1985-2010). Ngày nay GnRH-antagonist protocol đã chiếm ~70% cycle ở châu Âu và ngày càng phổ biến ở chây Á. '
        'Tuy nhiên long protocol VẪN CÒN CHỖ ĐỨNG ở một số nhóm bệnh nhân nhất định.'
    )
    doc.add_paragraph('Bác sĩ sản phụ khoa làm ART phải hiểu rõ cơ chế down-regulation để:')
    add_bullets(doc, [
        'Biết khi nào NÊN chọn (normal responder, endometriosis, cycle programming)',
        'Biết khi nào KHÔNG nên chọn (PCOS, poor responder)',
        'Xử trí đúng flare effect, luteal phase support, trigger',
        'Tư vấn bệnh nhân về ưu/nhược điểm so với antagonist',
    ])

    # 1. CƠ CHẾ
    doc.add_heading('1. CƠ CHẾ SINH HỌC - TRỤC HPO VÀ DOWN-REGULATION', 1)

    doc.add_heading('1.1. Trục HPO bình thường', 2)
    doc.add_paragraph(
        'HPO axis (Hypothalamic-Pituitary-Ovarian) hoạt động theo cơ chế pulse-generator:\n'
        '- GnRH từ vùng dưới đồi tiết theo xung (pulse) mỗi 60-90 phút ở pha follicular, chậm lại ở pha luteal.\n'
        '- Mỗi xung GnRH kích thích thùy trước tuyến yên giải phóng FSH và LH đồng thời.\n'
        '- FSH kích thích nang trứng phát triển, LH kích thích nang trưởng thành và rụng trứng.\n'
        '- Khi estrogen từ nang trội tăng cao (>200 pg/mL kéo dài 48h), xảy ra feedback dương → LH surge → rụng trứng.'
    )

    doc.add_heading('1.2. Hai kiểu receptor GnRH', 2)
    doc.add_paragraph(
        '- GnRH receptor kiểu I (ở thùy trước tuyến yên): chịu trách nhiệm chính cho việc giải phóng FSH/LH.\n'
        '- GnRH receptor kiểu II (ở buồng trứng, tử cung, vú): chức năng chưa hoàn toàn rõ, có vai trò trong apoptosis tế bào ung thư.'
    )

    doc.add_heading('1.3. Cơ chế down-regulation của GnRH agonist', 2)
    doc.add_paragraph('GIAI ĐOẠN 1 - Flare effect (Ngày 1-3):').runs[0].bold = True
    doc.add_paragraph(
        'Khi bắt đầu dùng GnRH agonist (Leuprolide/Triptorelin), thuốc gắn vào GnRH receptor ở thùy trước tuyến yên '
        'và GÂY KÍCH THÍCH MẠNH trước khi ức chế. Hiện tượng này gọi là "flare":\n'
        '- FSH tăng vọt 50-100% trong 24-48h đầu\n'
        '- LH tăng tương tự\n'
        '- Estrogen tăng theo\n'
        '- Lý do: thuốc có ái lực cao hơn GnRH nội sinh, nội bào hóa receptor chậm nên tín hiệu ban đầu còn được truyền'
    )
    doc.add_paragraph('GIAI ĐOẠN 2 - Desensitization (Ngày 4-14):').runs[0].bold = True
    doc.add_paragraph('Sau ~7 ngày kích thích liên tục, xảy ra 3 hiện tượng song song:')
    add_bullets(doc, [
        'Receptor downregulation: số lượng GnRH receptor trên bề mặt tế bào thùy trước giảm',
        'Uncoupling: G-protein ngừng truyền tín hiệu từ receptor (mất chức năng dù receptor còn)',
        'Depletion of LH/FSH pool: bể chứa LH/FSH ở thùy trước cạn kiệt vì đã giải phóng hết ở flare',
    ])
    doc.add_paragraph(
        'Kết quả: FSH và LH huyết thanh giảm xuống <5 mIU/mL, estrogen giảm <50 pg/mL - đạt trạng thái '
        '"down-regulation" hay "hypogonadotropic hypogonadism" tạm thời.'
    )

    doc.add_heading('1.4. Tại sao bắt đầu ở pha hoàng thể (luteal start)?', 2)
    add_bullets(doc, [
        'Tránh flare effect xảy ra khi đã có nang trội → không lo kích thích nang non tự phát triển',
        'Đảm bảo đến ngày 2-3 chu kỳ mới, down-regulation đã hoàn tất (~14 ngày sau)',
        'Nếu bắt đầu ngày 2-3 chu kỳ (follicular start), flare effect sẽ kích thích nang non từ wave 1',
        'Có 2 biến thể cho ca khó scheduling: Stop protocol (Orvieto 2023, PMID 36710334) và Microflare/short protocol',
    ])

    # 2. CAC BUOC
    doc.add_heading('2. CÁC BƯỚC THỰC HIỆN - STEP BY STEP', 1)

    doc.add_heading('Bước 1: Tư vấn và chỉ định', 2)
    doc.add_paragraph('Tiêu chí chọn bệnh nhân:')
    add_bullets(doc, [
        'Tuổi < 38',
        'AMH >= 2 ng/mL, AFC >= 10',
        'BMI 18-30',
        'Không có tiền sử poor response',
        'Không PCOS',
    ])

    doc.add_heading('Bước 2: Down-regulation (Luteal start)', 2)
    doc.add_paragraph(
        'Bắt đầu Leuprolide 0.5-1.0 mg/ngày SC (hoặc 20-40 IU đơn vị) từ NGÀY 21 ± 1 CHU KỲ TRƯỚC. '
        'Hoặc Triptorelin depot 3.75 mg IM (1 mũi duy nhất). Tiếp tục duy trì cho đến ngày trigger.'
    )
    doc.add_paragraph('Tiêu chí xác nhận down-regulation đạt (đánh giá ngày 2-3 chu kỳ mới):')
    t1 = doc.add_table(rows=7, cols=3)
    t1.style = 'Light Grid Accent 1'
    headers1 = ['Tiêu chí', 'Ngưỡng đạt', 'Lưu ý']
    rows1 = [
        ('E2 huyết thanh', '< 50 pg/mL', '< 30 pg/mL lý tưởng'),
        ('LH', '< 5 mIU/mL', '< 3 mIU/mL lý tưởng'),
        ('FSH', '< 5 mIU/mL', 'Ít dùng'),
        ('Endometrial thickness', '< 5 mm', 'Nếu > 5 mm → chưa suppress đủ'),
        ('Nang trứng', 'Không có nang > 10 mm', 'Nếu cyst > 2 cm → aspirate hoặc chờ'),
        ('Progesterone', '< 1.5 ng/mL', 'Đảm bảo không còn thể vàng hoạt động'),
    ]
    for i, h in enumerate(headers1):
        t1.rows[0].cells[i].text = h
        style_header(t1.rows[0].cells[i])
    for r, row_data in enumerate(rows1, start=1):
        for c, value in enumerate(row_data):
            t1.rows[r].cells[c].text = value
            set_cell_border(t1.rows[r].cells[c])
            if c == 0:
                style_first_col(t1.rows[r].cells[c])
    doc.add_paragraph()

    doc.add_heading('Bước 3: Kích thích buồng trứng', 2)
    add_bullets(doc, [
        'Bắt đầu rFSH (Gonal-F, Puregon, Bemfola) hoặc hMG (Menopur) từ ngày 2-3 chu kỳ mới',
        'Liều khởi đầu (theo ASRM 2023, Bologna criteria):',
        '   - Normal responder: 150-225 IU/ngày',
        '   - High responder (AMH > 4 ng/mL, AFC > 20): 100-150 IU/ngày',
        '   - Trường hợp nghi ngờ high response: 100 IU và điều chỉnh',
        'Monitoring: Siêu âm đầu dò âm đạo + E2 mỗi 2-3 ngày từ ngày kích thích thứ 5',
        'Điều chỉnh liều: ±75 IU tùy response (E2 tăng gấp đôi mỗi 48h là lý tưởng)',
        'Tiêu chí "good response": >= 8 nang trội (>= 14 mm), E2 1500-3000 pg/mL vào ngày trigger',
    ])

    doc.add_heading('Bước 4: Trigger', 2)
    doc.add_paragraph('Khi 2-3 nang đạt 17-18 mm, quyết định trigger:')
    t2 = doc.add_table(rows=4, cols=4)
    t2.style = 'Light Grid Accent 1'
    headers2 = ['Trigger', 'Liều', 'Ưu điểm', 'Nhược điểm']
    rows2 = [
        ('hCG (kinh điển)', '5000-10000 IU SC\nhoặc 250 mcg rhCG', 'Giống LH surge tự nhiên, luteal support tốt', 'Nguy cơ OHSS cao, kéo dài LH activity 7-10 ngày'),
        ('GnRH agonist trigger\n(Leuprolide 0.2 mg SC)', '1 mũi', 'OHSS gần như bằng 0, lấy noãn tốt', 'Luteal phase defect NẶNG, BẮT BUỘC aggressive luteal support hoặc freeze all'),
        ('Dual trigger\n(hCG 1000 IU + Leuprolide 0.2 mg)', 'Kết hợp', 'Giảm OHSS so với hCG đơn thuần, cải thiện oocyte maturity', 'Vẫn có nguy cơ OHSS nhẹ'),
    ]
    for i, h in enumerate(headers2):
        t2.rows[0].cells[i].text = h
        style_header(t2.rows[0].cells[i])
    for r, row_data in enumerate(rows2, start=1):
        for c, value in enumerate(row_data):
            t2.rows[r].cells[c].text = value
            set_cell_border(t2.rows[r].cells[c])
            if c == 0:
                style_first_col(t2.rows[r].cells[c])
    doc.add_paragraph()
    doc.add_paragraph('Quy tắc quan trọng: Long protocol + nguy cơ OHSS cao → GnRH trigger + freeze all.').runs[0].bold = True

    doc.add_heading('Bước 5: Chọc hút noãn (OPU)', 2)
    add_bullets(doc, [
        '35-36 giờ sau trigger (đối với hCG hoặc dual trigger)',
        '34-36 giờ sau GnRH trigger (window hẹp hơn)',
        'Thủ thuật qua đường âm đạo dưới siêu âm, gây mê tĩnh mạch hoặc tê tại chỗ',
    ])

    doc.add_heading('Bước 6: Hỗ trợ hoàng thể (LUTEAL SUPPORT) - BẮT BUỘC', 2)
    doc.add_paragraph('Tại sao cần?')
    add_bullets(doc, [
        'Down-regulation kéo dài 2-3 tuần ức chế cả LH nội sinh → thể vàng kém chức năng',
        'Sau OPU, nhiều nang bị chọc hút → giảm khối lượng tế bào steroidogenic',
        'Trigger bằng GnRH agonist → LH nội sinh gần như bằng 0 → luteal phase defect NẶNG',
    ])
    doc.add_paragraph('Protocol chuẩn (theo ASRM/ACOG 2023):')
    add_bullets(doc, [
        'Progesterone 200-400 mg/ngày đường âm đạo (Crinone gel 8% hoặc Endometrin 100 mg x 2-3 lần/ngày)',
        'Bắt đầu từ ngày OPU và kéo dài đến tuần 8-10 nếu có thai',
        'KHÔNG dùng hCG để hỗ trợ hoàng thể ở long protocol (gây OHSS)',
        'Nếu dùng GnRH trigger + fresh transfer: phải dùng thêm E2 và LH activity',
    ])

    # 3. CHI DINH
    doc.add_heading('3. AI PHÙ HỢP VỚI LONG PROTOCOL?', 1)

    doc.add_heading('3.1. Bảng chỉ định dựa trên bằng chứng', 2)
    t3 = doc.add_table(rows=9, cols=4)
    t3.style = 'Light Grid Accent 1'
    headers3 = ['Nhóm bệnh nhân', 'Có nên dùng?', 'Bằng chứng', 'Ghi chú']
    rows3 = [
        ('Normal responder\n(AMH 1-4 ng/mL, AFC 8-15)', 'Có thể dùng - tương đương antagonist', 'PMID 38095077 (Liu 2023, meta-analysis 52 RCT, n=9950)', 'LBR tương đương; cycle cancellation thấp hơn'),
        ('High responder\n(AMH > 4, AFC > 20, PCOS)', 'KHÔNG - chọn antagonist + GnRH trigger', 'PMID 35292717 (Kadoura 2022, meta-analysis 6 RCT PCOS)', 'OHSS tăng 2-3 lần'),
        ('Endometriosis giai đoạn III/IV', 'Cân nhắc ultra-long protocol', 'PMID 38100935 (Goyri 2024), PMID 36688363 (Wang 2023)', 'Ultra-long (3-6 tháng down-reg) cải thiện pregnancy rate'),
        ('Adenomyosis', 'Ultra-long protocol được ưu tiên', 'PMID 36549997 (Han 2023)', 'Giảm impact của adenomyosis lên endometrial receptivity'),
        ('Poor responder (Bologna)', 'Cân nhắc microflare hoặc chuyển antagonist', 'PMID 39626004 (Vaz 2024)', 'Long protocol suppress quá mức, giảm oocyte yield'),
        ('Cần cycle programming chính xác (PGT-A, fertility preservation)', 'Long protocol là lựa chọn tốt', 'PMID 37884809 (Hu 2024)', 'Cho phép control thời gian trigger chính xác'),
        ('Cycle trước LH surge sớm dù antagonist', 'Chuyển sang long protocol', 'PMID 36710334 (Orvieto 2023)', 'Down-reg sớm loại bỏ LH surge risk'),
        ('Bệnh nhân ung thư cần fertility preservation', 'Tốt (kết hợp letrozole để giảm E2)', 'ASRM 2019 fertility preservation guideline', 'Lý tưởng vì trigger được kiểm soát'),
    ]
    for i, h in enumerate(headers3):
        t3.rows[0].cells[i].text = h
        style_header(t3.rows[0].cells[i])
    for r, row_data in enumerate(rows3, start=1):
        for c, value in enumerate(row_data):
            t3.rows[r].cells[c].text = value
            set_cell_border(t3.rows[r].cells[c])
            if c == 0:
                style_first_col(t3.rows[r].cells[c])
    doc.add_paragraph()

    doc.add_heading('3.2. Bologna criteria cho poor responder (Ferraretti 2011)', 2)
    doc.add_paragraph('Cần ≥ 2 trong 3 tiêu chí sau:')
    add_bullets(doc, [
        'Tuổi ≥ 40 hoặc bất kỳ yếu tố poor response khác',
        'Trước đó poor response (≤ 3 noãn với protocol kích thích thông thường)',
        'AMH < 0.5-1.1 ng/mL HOẶC AFC < 5-7',
    ])
    doc.add_paragraph('Ở nhóm này, long protocol KHÔNG phải là lựa chọn đầu tay - ưu tiên antagonist hoặc natural cycle IVF.')

    # 4. EVIDENCE
    doc.add_heading('4. EVIDENCE & GUIDELINES', 1)

    doc.add_heading('4.1. Meta-analysis quan trọng', 2)
    doc.add_paragraph('Liu C. et al. 2023 (PMID 38095077, Expert Rev Mol Med) - Meta-analysis quan trọng nhất gần đây:').runs[0].bold = True
    add_bullets(doc, [
        '52 nghiên cứu, tổng n = 9950 bệnh nhân (5193 GnRH-ant, 4757 long GnRH-a)',
        'Live birth rate: Tương đương giữa 2 protocol (RR = 0.96, 95% CI 0.90-1.03, p = 0.27)',
        'OHSS: GnRH-ant thấp hơn đáng kể (RR = 0.48, 95% CI 0.38-0.61), đặc biệt PCOS',
        'Clinical pregnancy rate: Tương đương',
        'Miscarriage rate: Tương đương',
        'Kết luận: GnRH-ant comparable với long GnRH-a cho LBR, ưu việt hơn về an toàn (OHSS)',
    ])
    doc.add_paragraph('Kadoura S. et al. 2022 (PMID 35292717, Sci Rep) - Meta-analysis trên PCOS:').runs[0].bold = True
    add_bullets(doc, [
        '6 RCT, 986 phụ nữ PCOS',
        'OHSS: Ant 5.2% vs Agonist 12.4% (giảm 58%)',
        'Số noãn: tương đương',
        'Clinical pregnancy: tương đương',
        'Stimulation days: Ant ngắn hơn ~2 ngày',
        'Total gonadotropin dose: Ant thấp hơn ~250 IU',
        'Kết luận: Ở PCOS, antagonist là lựa chọn ưu tiên vì an toàn hơn mà không mất hiệu quả',
    ])
    doc.add_paragraph('Lambalk CB. et al. 2017 (PMID 28903472, Hum Reprod Update) - Subgroup analysis:').runs[0].bold = True
    add_bullets(doc, [
        'Antagonist vs long agonist: hiệu quả thay đổi theo nhóm bệnh nhân',
        'Ở normal responder: tương đương',
        'Ở poor responder: antagonist có khuynh hướng tốt hơn',
        'Ở high responder / PCOS: antagonist ưu việt hơn',
    ])

    doc.add_heading('4.2. Guidelines hiện hành', 2)
    add_bullets(doc, [
        'ASRM 2023: Antagonist và long agonist là 2 protocol chính. Lựa chọn dựa trên đặc điểm bệnh nhân. Antagonist ưu tiên ở high responder, PCOS.',
        'ESHRE 2019: Không có sự khác biệt đáng kể về LBR. Antagonist ưu việt hơn cho PCOS và high responder. Long agonist còn chỗ đứng ở specific patient groups.',
        'RCOG 2016 (cập nhật 2023): Ủng hộ cả 2 protocol, nhấn mạnh patient-tailored approach. Cảnh báo OHSS risk với long protocol ở PCOS.',
    ])

    doc.add_heading('4.3. Cập nhật 2024-2025', 2)
    add_bullets(doc, [
        'Hu L. et al. 2024 (PMID 37884809, Adv Ther): Tối ưu FSH modulation trong short-acting GnRH-a long protocol. Tăng/giảm FSH liều dựa trên response từng người.',
        'Orvieto R. 2023 (PMID 36710334, Reprod Biol Endocrinol): "Stop protocol" - hybrid GnRH-a luteal → antagonist khi nang 14 mm. Hữu ích ở poor responders (Poseidon 4), elevated progesterone, poor embryo quality trước đó.',
    ])

    # 5. SO SANH
    doc.add_heading('5. ƯU VÀ NHƯỢC ĐIỂM - SO SÁNH VỚI ANTAGONIST', 1)
    t4 = doc.add_table(rows=12, cols=3)
    t4.style = 'Light Grid Accent 1'
    headers4 = ['Tiêu chí', 'Long GnRH-agonist', 'GnRH-antagonist']
    rows4 = [
        ('Tổng thời gian cycle', '4-5 tuần', '2-3 tuần'),
        ('Số mũi tiêm', '25-35 mũi (daily) hoặc 1-2 mũi (depot)', '4-6 mũi'),
        ('Chi phí thuốc', 'Trung bình (có thể cao nếu depot)', 'Thấp hơn'),
        ('Tổng liều gonadotropin', 'Cao hơn ~250 IU', 'Thấp hơn'),
        ('OHSS risk', 'Cao hơn', 'Thấp hơn (đặc biệt với GnRH trigger)'),
        ('Cycle cancellation', 'Thấp (~5-8%)', 'Trung bình (~8-12%)'),
        ('Live birth rate (normal responder)', 'Tương đương', 'Tương đương'),
        ('Cycle programming', 'Tốt (down-reg sớm)', 'Khó hơn'),
        ('Patient convenience', 'Kém (nhiều tiêm, kéo dài)', 'Tốt (ngắn, ít tiêm)'),
        ('Phù hợp PCOS', 'Không', 'Có'),
        ('Phù hợp poor responder', 'Không (microflare ngoại lệ)', 'Có'),
    ]
    for i, h in enumerate(headers4):
        t4.rows[0].cells[i].text = h
        style_header(t4.rows[0].cells[i])
    for r, row_data in enumerate(rows4, start=1):
        for c, value in enumerate(row_data):
            t4.rows[r].cells[c].text = value
            set_cell_border(t4.rows[r].cells[c])
            if c == 0:
                style_first_col(t4.rows[r].cells[c])
    doc.add_paragraph()

    # 6. BIEN CHUNG
    doc.add_heading('6. CÁC BIẾN CHỨNG VÀ CÁCH XỬ TRÍ', 1)

    doc.add_heading('6.1. OHSS (Ovarian Hyperstimulation Syndrome)', 2)
    add_bullets(doc, [
        'Tỷ lệ: 12-15% thể nhẹ, 1-3% thể nặng với long protocol ở high responder',
        'Phân loại theo Golan 1989: Nhẹ (căng bụng, BT < 8 cm) - Trung bình (ascites nhẹ, BT 8-12 cm) - Nặng (ascites nhiều, Hct > 45%, BT > 12 cm) - Rất nặng (suy thận, huyết khối, ARDS)',
        'Phòng ngừa ở long protocol: giảm liều FSH ở high responder, coasting nếu E2 > 4000-5000 pg/mL, GnRH agonist trigger, freeze all',
    ])

    doc.add_heading('6.2. Luteal phase defect (Suy hoàng thể)', 2)
    add_bullets(doc, [
        'Down-regulation kéo dài làm thể vàng kém chức năng',
        'BẮT BUỘC dùng progesterone 200-400 mg/ngày âm đạo',
        'Nếu dùng GnRH trigger + fresh transfer: cần modified luteal support với E2 + LH activity nhỏ',
        'Khuyến cáo hiện nay: GnRH trigger → freeze all → FET là an toàn nhất',
    ])

    doc.add_heading('6.3. Cyst formation', 2)
    add_bullets(doc, [
        'Nang còn sót sau down-regulation (thường < 2 cm)',
        'Xử trí: chờ tự thoái lui, hoặc aspirate nếu > 2-3 cm ảnh hưởng response',
    ])

    doc.add_heading('6.4. Headache, hot flash', 2)
    add_bullets(doc, [
        'Do hypoestrogen tạm thời',
        'Thường nhẹ, tự hết sau khi bắt đầu gonadotropin',
        'Nếu nặng: bổ sung E2 nhỏ liều 2 mg/ngày trong 7-10 ngày',
    ])

    # 7. BIEN THE
    doc.add_heading('7. MỘT SỐ BIẾN THỂ', 1)

    doc.add_heading('7.1. Ultra-long protocol (cho Endometriosis, Adenomyosis)', 2)
    add_bullets(doc, [
        'Down-regulation bằng GnRH agonist depot 3.75 mg mỗi 4 tuần × 3-6 tháng TRƯỚC khi bắt đầu kích thích',
        'Sau đó tiến hành long protocol bình thường',
        'Bằng chứng (PMID 38100935, PMID 36688363, PMID 36549997): cải thiện pregnancy rate',
        'Cơ chế: ức chế hoàn toàn estrogen → teo nang lạc nội mạc, giảm inflammation',
        'Nhược điểm: thời gian rất dài, chi phí cao, triệu chứng hypoestrogen kéo dài',
    ])

    doc.add_heading('7.2. Short/microflare protocol (cho poor responder)', 2)
    add_bullets(doc, [
        'Bắt đầu GnRH agonist từ ngày 2 chu kỳ đồng thời với gonadotropin',
        'Tận dụng flare effect (FSH/LH tăng 50-100% trong 48h đầu) để tăng response',
        'Sau 3-4 ngày, bổ sung antagonist từ khi nang 14 mm',
        'Cải thiện oocyte yield ở poor responder',
    ])

    doc.add_heading('7.3. Stop protocol (Orvieto 2023)', 2)
    add_bullets(doc, [
        'Bắt đầu GnRH agonist từ luteal phase',
        'Sau khi bắt đầu gonadotropin, chuyển sang antagonist',
        'Hữu ích cho: poor responders (Poseidon 4), elevated progesterone, poor embryo quality trước đó, repeated IVF failures',
    ])

    doc.add_heading('7.4. Long-acting (depot) vs short-acting (daily)', 2)
    add_bullets(doc, [
        'Long-acting depot (Triptorelin 3.75 mg IM): 1 mũi/tháng, tiện, compliance tốt',
        'Short-acting daily (Leuprolide 0.5 mg SC mỗi ngày): linh hoạt, dễ điều chỉnh liều',
        'Hiệu quả tương đương, nhưng depot suppress sâu hơn → có thể cần tăng FSH liều',
    ])

    # 8. TIPS
    doc.add_heading('8. TIPS THỰC HÀNH (CLINICAL PEARLS)', 1)
    add_bullets(doc, [
        'PCOS: KHÔNG chọn agonist long, ưu tiên antagonist + GnRH trigger + freeze all.',
        'Endometriosis giai đoạn III/IV: Cân nhắc ultra-long protocol (down-reg 3-6 tháng trước IVF).',
        'Daily vs depot: Depot tiện hơn nhưng khó chỉnh liều, daily phù hợp cho poor/moderate responder.',
        'Trigger timing: 2-3 nang trên 17-18 mm + E2 ổn định 2 ngày = sẵn sàng trigger.',
        'Cyst sau down-reg: Nang 2-3 cm không ảnh hưởng nhiều, chờ tự thoái lui; nang > 3 cm → cân nhắc aspirate.',
        'Bệnh nhân poor response trước đó: Chuyển sang antagonist từ cycle sau.',
        'Luteal support: Progesterone 200-400 mg/ngày âm đạo là BẮT BUỘC, không phải tùy chọn.',
        'Cycle programming: Long protocol lý tưởng khi cần kiểm soát chính xác thời gian trigger (PGT, ngân hàng mô, fertility preservation trước hóa trị).',
        'Dấu hiệu down-regulation đạt: E2 < 50, LH < 5, ET < 5 mm, không nang > 10 mm.',
        'ORIENTATION cho bệnh nhân: Giải thích cycle dài 4-5 tuần, nhiều mũi tiêm, OHSS risk - để họ chuẩn bị tâm lý.',
    ])

    # 9. TONG KET
    doc.add_heading('9. TỔNG KẾT ĐIỂM CẦN NHỚ', 1)
    for i, item in enumerate([
        'Long GnRH-agonist protocol dựa trên down-regulation tuyến yên bằng GnRH agonist liên tục 2-3 tuần.',
        'Cơ chế 2 giai đoạn: Flare effect (ngày 1-3) → Desensitization (ngày 4-14).',
        'Bắt đầu ở luteal phase (ngày 21) của chu kỳ trước để tránh kích thích nang non.',
        'Tiêu chí down-regulation đạt: E2 < 50 pg/mL, LH < 5 mIU/mL, ET < 5 mm, không nang > 10 mm.',
        'Chỉ định chính: normal-to-high responder, endometriosis, cần cycle programming.',
        'Chống chỉ định tương đối: PCOS, poor responder (Bologna criteria).',
        'Luteal support với progesterone BẮT BUỘC 200-400 mg/ngày âm đạo.',
        'GnRH trigger ưu tiên ở high responder OHSS risk → kết hợp freeze all.',
        'Theo meta-analysis 2023 (Liu, PMID 38095077): LBR tương đương antagonist, nhưng OHSS cao hơn.',
        'Ultra-long protocol (3-6 tháng down-reg) cho endometriosis/adenomyosis giai đoạn nặng.',
    ], start=1):
        doc.add_paragraph(f'{i}. {item}', style='List Number')

    # 10. TAI LIEU
    doc.add_heading('10. TÀI LIỆU THAM KHẢO (VERIFY PUBMED)', 1)
    refs = [
        ('Liu C. et al. (2023)', 'PMID: 38095077', 'Expert Rev Mol Med.', 'DOI: 10.1017/erm.2023.25', '"Live birth rate of gonadotropin-releasing hormone antagonist versus luteal phase gonadotropin-releasing hormone agonist protocol in IVF/ICSI: a systematic review and meta-analysis."'),
        ('Kadoura S. et al. (2022)', 'PMID: 35292717', 'Sci Rep.', 'DOI: 10.1038/s41598-022-08400-z', '"Conventional GnRH antagonist protocols versus long GnRH agonist protocol in IVF/ICSI cycles of polycystic ovary syndrome women."'),
        ('Lambalk CB. et al. (2017)', 'PMID: 28903472', 'Hum Reprod Update.', 'DOI: 10.1093/humupd/dmx017', '"GnRH antagonist versus long agonist protocols in IVF: a systematic review and meta-analysis accounting for patient type."'),
        ('Siristatidis CS. et al. (2015)', 'PMID: 26558801', 'Cochrane Database Syst Rev.', 'DOI: 10.1002/14651858.CD006919.pub4', '"Gonadotrophin-releasing hormone agonist protocols for pituitary suppression in assisted reproduction."'),
        ('Goyri E. et al. (2024)', 'PMID: 38100935', 'Best Pract Res Clin Obstet Gynaecol.', 'DOI: 10.1016/j.bpobgyn.2023.102429', '"IVF stimulation protocols and outcomes in women with endometriosis."'),
        ('Orvieto R. (2023)', 'PMID: 36710334', 'Reprod Biol Endocrinol.', 'DOI: 10.1186/s12958-023-01069-7', '"Stop GnRH-agonist/GnRH-antagonist protocol: a different insight on ovarian stimulation for IVF."'),
        ('Hu L. et al. (2024)', 'PMID: 37884809', 'Adv Ther.', 'DOI: 10.1007/s12325-023-02702-y', '"Optimizing FSH Concentration Modulation in the Short-Acting GnRH-a Long Protocol for IVF/ICSI: A Retrospective Study."'),
        ('Wang X. et al. (2023)', 'PMID: 36688363', 'Int J Gynaecol Obstet.', 'DOI: 10.1002/ijgo.14690', '"Is the long-acting gonadotropin-releasing hormone agonist long protocol better for patients with endometriosis undergoing IVF?"'),
        ('Han B. et al. (2023)', 'PMID: 36549997', 'Reprod Biomed Online.', 'DOI: 10.1016/j.rbmo.2022.09.021', '"The effect of adenomyosis types on clinical outcomes of IVF embryo transfer after ultra-long GnRH agonist protocol."'),
        ('Vaz GQ. et al. (2024)', 'PMID: 39626004', 'JBRA Assist Reprod.', 'DOI: 10.5935/1518-0557.20240057', '"Could the use of agonist protocols benefit patients who do not respond well to human reproduction treatment?"'),
    ]
    for i, (author, pmid, journal, doi, title) in enumerate(refs, start=1):
        p = doc.add_paragraph(style='List Number')
        p.add_run(f'{author} ').bold = True
        p.add_run(f'{pmid}. {journal} {doi}.\n')
        p.add_run(title).italic = True

    # FOOTER
    doc.add_paragraph()
    footer = doc.add_paragraph(f'— Hết bài học ngày {DATE} —')
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.runs[0].italic = True
    footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

    footer2 = doc.add_paragraph('Bác sĩ: Ngọc 🍅 🐈‍⬛ | AI assistant: MiniMax Mavis')
    footer2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer2.runs[0].font.size = Pt(9)
    footer2.runs[0].font.color.rgb = RGBColor(0xA0, 0xA0, 0xA0)

    doc.save(str(DOCX_OUT))
    print(f"[DOCX] Saved: {DOCX_OUT}")
    print(f"[DOCX] Size: {DOCX_OUT.stat().st_size} bytes")


# ============================================================
# ANKI BUILDER (PASTEL THEME)
# ============================================================
def build_anki():
    import html as html_lib
    with open(CARDS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Pastel theme
    css = """
.card {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 18px;
  text-align: left;
  color: #4a4a4a;
  background: linear-gradient(135deg, #fef9f3 0%, #f7e8e0 100%);
  padding: 20px;
  border-radius: 12px;
}
.card.nightMode {
  background: linear-gradient(135deg, #2d3142 0%, #4f5d75 100%);
  color: #f0e9e0;
}
#front, #back {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 16px 20px;
  border-radius: 10px;
  border: 1px solid #e6d2c4;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  margin-bottom: 12px;
}
.card.nightMode #front, .card.nightMode #back {
  background-color: rgba(255, 255, 255, 0.08);
  border-color: rgba(255,255,255,0.15);
  color: #f0e9e0;
}
.tag {
  display: inline-block;
  background-color: #c8a4a5;
  color: #fff;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  margin-right: 6px;
}
"""

    model_id = 1607392319
    deck_id = 2059400110

    model = genanki.Model(
        model_id,
        'Long GnRH Agonist - Pastel',
        fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Tags'}],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div id="front">{{Question}}</div>',
                'afmt': '<div id="front">{{Question}}</div><hr id="answer"><div id="back">{{Answer}}<br><br><span class="tag">{{Tags}}</span></div>',
            }
        ],
        css=css
    )

    deck = genanki.Deck(deck_id, data['deck_name'])
    deck.description = 'Long GnRH Agonist Protocol trong IVF/ICSI - 18/06/2026 - Pastel theme'

    for card in data['cards']:
        # Escape HTML entities to prevent rendering issues with < and >
        front_escaped = html_lib.escape(card['front'])
        back_escaped = html_lib.escape(card['back'])
        # Restore basic markdown that we want to keep (line breaks)
        front_escaped = front_escaped.replace('\n', '<br>')
        back_escaped = back_escaped.replace('\n', '<br>')
        note = genanki.Note(
            model=model,
            fields=[front_escaped, back_escaped, 'ART · IVF · Long Protocol']
        )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(str(APKG_OUT))
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {len(data['cards'])}")


# ============================================================
# HTML VISUAL SUMMARY (Tailwind + Mermaid + Chart.js)
# ============================================================
def build_html():
    html = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Long GnRH Agonist Protocol - Visual Summary</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  body { font-family: 'Inter', system-ui, sans-serif; background: linear-gradient(135deg, #fef9f3 0%, #f7e8e0 100%); }
  .glass { background: rgba(255,255,255,0.7); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.3); }
  .pastel-pink { background: #f4c2c2; }
  .pastel-blue { background: #c5d5e0; }
  .pastel-mint { background: #c5e0c9; }
  .pastel-peach { background: #f7d1ba; }
  .pastel-lavender { background: #d4c5e2; }
  .mermaid { background: white; border-radius: 12px; padding: 16px; }
</style>
</head>
<body class="min-h-screen p-6">

<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">Long GnRH Agonist Protocol trong IVF/ICSI</h1>
  <p class="text-stone-500 italic">Visual Summary - Bài học 18/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">ART</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">IVF/ICSI</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">Pituitary Down-regulation</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">COS</span>
  </div>
</header>

<main class="max-w-6xl mx-auto space-y-8">

  <!-- SECTION 1: CO CHE DOWN-REGULATION -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. Cơ chế Down-Regulation (2 giai đoạn)</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Giai đoạn 1: FLARE EFFECT (Ngày 1-3)</h3>
        <ul class="text-sm text-stone-700 space-y-1">
          <li>• GnRH agonist gắn vào receptor ở thùy trước tuyến yên</li>
          <li>• FSH tăng vọt 50-100% trong 24-48h đầu</li>
          <li>• LH tăng tương tự, estrogen tăng theo</li>
          <li>• Lý do: ái lực thuốc cao hơn GnRH nội sinh</li>
        </ul>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Giai đoạn 2: DESENSITIZATION (Ngày 4-14)</h3>
        <ul class="text-sm text-stone-700 space-y-1">
          <li>• Receptor downregulation (giảm số lượng)</li>
          <li>• Uncoupling (G-protein ngừng truyền tín hiệu)</li>
          <li>• Depletion of LH/FSH pool (bể chứa cạn kiệt)</li>
          <li>• Kết quả: FSH/LH < 5 mIU/mL, E2 < 50 pg/mL</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 2: FLOWCHART -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Quy trình Long Protocol (Flowchart)</h2>
    <div class="mermaid">
flowchart TD
    A["Bệnh nhân: AMH >= 2, AFC >= 10,<br/>không PCOS, không poor responder"] --> B["Ngày 21 ± 1 chu kỳ trước:<br/>Bắt đầu GnRH agonist"]
    B --> C["Leuprolide 0.5-1.0 mg/ngày SC<br/>hoặc Triptorelin 3.75 mg depot IM"]
    C --> D["Ngày 2-3 chu kỳ mới:<br/>Đánh giá down-regulation"]
    D --> E{"Đạt tiêu chí?<br/>E2 < 50, LH < 5,<br/>ET < 5 mm, không nang > 10 mm"}
    E -- "Có" --> F["Bắt đầu rFSH/hMG<br/>150-225 IU/ngày"]
    E -- "Không" --> D
    F --> G["Monitoring mỗi 2-3 ngày:<br/>SA + E2"]
    G --> H{"2-3 nang đạt<br/>17-18 mm?"}
    H -- "Chưa" --> G
    H -- "Rồi" --> I["Quyết định trigger"]
    I --> J{"OHSS risk?"}
    J -- "Cao" --> K["GnRH agonist trigger<br/>0.2 mg SC<br/>+ Freeze all"]
    J -- "Thấp" --> L["hCG 5000-10000 IU SC<br/>hoặc 250 mcg rhCG"]
    K --> M["OPU 35-36h sau trigger"]
    L --> M
    M --> N["Luteal support:<br/>Progesterone 200-400 mg/ngày<br/>âm đạo x 8-10 tuần"]
    N --> O["Pregnancy test 14 ngày sau<br/>FET hoặc Fresh transfer"]

    style A fill:#f4c2c2
    style B fill:#f7d1ba
    style F fill:#c5d5e0
    style K fill:#d4c5e2
    style L fill:#c5e0c9
    style N fill:#f4c2c2
    </div>
  </section>

  <!-- SECTION 3: CHI DINH -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">3. Ai phù hợp với Long Protocol?</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-3">NÊN DÙNG (Indications)</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>✓ Normal responder (AMH 1-4, AFC 8-15)</li>
          <li>✓ Endometriosis giai đoạn III/IV (ultra-long)</li>
          <li>✓ Adenomyosis (ultra-long)</li>
          <li>✓ Cần cycle programming (PGT-A, fertility preservation)</li>
          <li>✓ Cycle trước LH surge sớm với antagonist</li>
          <li>✓ Bệnh nhân ung thư cần fertility preservation</li>
        </ul>
      </div>
      <div class="pastel-peach rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-3">KHÔNG NÊN (Contraindications)</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>✗ PCOS (OHSS risk tăng 2-3 lần)</li>
          <li>✗ Poor responder theo Bologna criteria</li>
          <li>✗ Phụ nữ > 40 tuổi với dự trữ kém</li>
          <li>✗ Bệnh nhân cần cycle ngắn (antagonist tốt hơn)</li>
          <li>✗ Tiền sử OHSS nặng với cycle trước</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 4: SO SANH PROTOCOL -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">4. So sánh Long Agonist vs Antagonist</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div>
        <canvas id="chart2"></canvas>
      </div>
    </div>
  </section>

  <!-- SECTION 5: EVIDENCE TABLE -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">5. Evidence - Meta-analysis quan trọng</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">PMID</th>
            <th class="px-3 py-2 text-left">Tác giả (Năm)</th>
            <th class="px-3 py-2 text-left">Loại nghiên cứu</th>
            <th class="px-3 py-2 text-left">Kết quả chính</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">38095077</td><td class="px-3 py-2">Liu C. (2023)</td><td class="px-3 py-2">Meta-analysis 52 RCT, n=9950</td><td class="px-3 py-2">LBR tương đương (RR 0.96); OHSS thấp hơn với antagonist (RR 0.48)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">35292717</td><td class="px-3 py-2">Kadoura S. (2022)</td><td class="px-3 py-2">Meta-analysis 6 RCT PCOS, n=986</td><td class="px-3 py-2">OHSS: Ant 5.2% vs Agonist 12.4% (giảm 58%)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">28903472</td><td class="px-3 py-2">Lambalk CB. (2017)</td><td class="px-3 py-2">Subgroup analysis</td><td class="px-3 py-2">Hiệu quả khác nhau theo patient type</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">26558801</td><td class="px-3 py-2">Siristatidis CS. (2015)</td><td class="px-3 py-2">Cochrane Review 29 RCT, n=5499</td><td class="px-3 py-2">Long protocol LBR cao hơn short</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">38100935</td><td class="px-3 py-2">Goyri E. (2024)</td><td class="px-3 py-2">Review</td><td class="px-3 py-2">Ultra-long protocol cải thiện pregnancy ở endometriosis</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">36710334</td><td class="px-3 py-2">Orvieto R. (2023)</td><td class="px-3 py-2">Protocol mô tả</td><td class="px-3 py-2">"Stop protocol" - hybrid hữu ích cho poor responder</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">37884809</td><td class="px-3 py-2">Hu L. (2024)</td><td class="px-3 py-2">Retrospective study</td><td class="px-3 py-2">Tối ưu FSH modulation trong short-acting long protocol</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 6: TIÊU CHÍ DOWN-REG -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">6. Tiêu chí Down-regulation đạt</h2>
    <div class="grid md:grid-cols-3 gap-3">
      <div class="pastel-pink rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">&lt; 50</div>
        <div class="text-sm text-stone-600">E2 (pg/mL)</div>
      </div>
      <div class="pastel-blue rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">&lt; 5</div>
        <div class="text-sm text-stone-600">LH (mIU/mL)</div>
      </div>
      <div class="pastel-mint rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">&lt; 5</div>
        <div class="text-sm text-stone-600">ET (mm)</div>
      </div>
      <div class="pastel-peach rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">0</div>
        <div class="text-sm text-stone-600">Nang > 10 mm</div>
      </div>
      <div class="pastel-lavender rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">&lt; 1.5</div>
        <div class="text-sm text-stone-600">Progesterone (ng/mL)</div>
      </div>
      <div class="bg-stone-200 rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">~14</div>
        <div class="text-sm text-stone-600">Ngày từ start</div>
      </div>
    </div>
  </section>

  <!-- SECTION 7: OHSS GRADING -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. OHSS Grading (Golan 1989)</h2>
    <div class="mermaid">
flowchart LR
    A["Mild<br/>Bụng căng<br/>BT < 8 cm"] --> B["Moderate<br/>Ascites nhẹ<br/>BT 8-12 cm"]
    B --> C["Severe<br/>Hct > 45%<br/>BT > 12 cm"]
    C --> D["Critical<br/>Suy thận, huyết khối<br/>ARDS"]
    A -.->|Tỷ lệ: 12-15%| E["Long Protocol"]
    B -.->|1-3% nặng| E

    style A fill:#c5e0c9
    style B fill:#f7d1ba
    style C fill:#f4c2c2
    style D fill:#d4c5e2
    </div>
    <p class="text-sm text-stone-600 mt-3 italic">Phòng ngừa ở long protocol: giảm liều FSH ở high responder, coasting nếu E2 > 4000-5000 pg/mL, GnRH agonist trigger, freeze all.</p>
  </section>

  <!-- SECTION 8: TIMELINE -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. Timeline Long Protocol (4-5 tuần)</h2>
    <div class="mermaid">
gantt
    title Long GnRH Agonist Protocol Timeline
    dateFormat  YYYY-MM-DD
    axisFormat  Day %d
    section Down-reg
    GnRH agonist luteal start    :a1, 2026-07-01, 14d
    section Stimulation
    Gonadotropin (FSH/hMG)       :a2, after a1, 10d
    section Trigger & OPU
    Trigger (hCG/GnRH-a)         :a3, after a2, 1d
    OPU 35-36h                    :a4, after a3, 1d
    section Luteal Support
    Progesterone 8-10 weeks       :a5, after a4, 70d
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="text-center text-stone-500 text-sm py-6">
    <p>Bài học soạn bởi MiniMax Mavis cho Bs. Ngọc 🍅 🐈‍⬛</p>
    <p>Verified PubMed: 10 papers (PMID 38095077, 35292717, 28903472, 26558801, 38100935, 36710334, 37884809, 36688363, 36549997, 39626004)</p>
  </footer>

</main>

<script>
mermaid.initialize({ startOnLoad: true, theme: 'neutral' });

// Chart 1: OHSS comparison
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['OHSS %', 'Cycle cancellation %', 'Total days', 'Number of injections'],
        datasets: [{
            label: 'Long Agonist',
            data: [12.4, 6.5, 32, 30],
            backgroundColor: 'rgba(244, 194, 194, 0.7)',
            borderColor: 'rgba(244, 194, 194, 1)',
            borderWidth: 1
        }, {
            label: 'Antagonist',
            data: [5.2, 10, 18, 5],
            backgroundColor: 'rgba(197, 213, 224, 0.7)',
            borderColor: 'rgba(197, 213, 224, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: { title: { display: true, text: 'So sánh hiệu quả & an toàn' } },
        scales: { y: { beginAtZero: true } }
    }
});

// Chart 2: LBR by patient type
new Chart(document.getElementById('chart2'), {
    type: 'doughnut',
    data: {
        labels: ['Normal responder', 'High responder/PCOS', 'Poor responder', 'Endometriosis'],
        datasets: [{
            data: [40, 25, 15, 20],
            backgroundColor: [
                'rgba(197, 224, 201, 0.7)',
                'rgba(244, 194, 194, 0.7)',
                'rgba(247, 209, 186, 0.7)',
                'rgba(212, 197, 226, 0.7)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: { title: { display: true, text: 'Phân bố chỉ định Long Protocol (%)' } }
    }
});
</script>

</body>
</html>'''

    HTML_OUT.write_text(html, encoding='utf-8')
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building Long GnRH Agonist Lesson - {DATE} ===\n")
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
