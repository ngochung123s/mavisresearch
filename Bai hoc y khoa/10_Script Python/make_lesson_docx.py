"""Tạo file Word cho bài học IVF - format chuẩn y khoa."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:\Users\THANHANH\.mavis\agents\mavis\workspace\bai_hoc_ivf_2026-06-12.docx"

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

doc = Document()

# Set default font to Arial for Vietnamese
style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

# Title
title = doc.add_heading('BÀI HỌC IVF NGÀY 12/06/2026', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Subtitle
sub = doc.add_paragraph('GnRH Agonist Long Protocol & Cervical Length Measurement')
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True

doc.add_paragraph()  # spacing

# PHẦN 1
doc.add_heading('PHẦN 1: GnRH AGONIST LONG PROTOCOL', 1)

doc.add_heading('1. Cơ chế pathophysiology (HPO axis)', 2)
doc.add_paragraph(
    'Trục HPO (Hypothalamic-Pituitary-Ovarian) hoạt động theo cơ chế sau: '
    'GnRH từ vùng dưới đồi tiết ra theo xung (pulse) mỗi 60-90 phút, kích thích thùy trước tuyến yên '
    'giải phóng FSH và LH. Hai hormone này kích thích buồng trứng tuyển chọn nang trứng và sản xuất estrogen. '
    'Khi estrogen tăng cao, feedback dương trở lại vùng dưới đồi và tuyến yên, gây ra đỉnh LH (LH surge) '
    'làm rụng trứng.'
)
doc.add_paragraph(
    'Agonist long protocol tận dụng cơ chế điều hòa ngược (down-regulation): '
    'GnRH agonist (Leuprolide hoặc Triptorelin) được bắt đầu từ giữa pha hoàng thể của chu kỳ trước (ngày 21). '
    'Trong 2-3 ngày đầu, thuốc gây hiện tượng flare-up làm FSH và LH tăng vọt do kích thích thụ thể. '
    'Sau 7-14 ngày sử dụng liên tục, tuyến yên bị mất nhạy cảm (desensitization), dẫn đến giảm FSH và LH xuống mức nền. '
    'Kết quả là ức chế hoàn toàn LH surge nội sinh, giúp kiểm soát chính xác thời điểm rụng trứng và giảm tỷ lệ hủy cycle.'
)

doc.add_heading('2. Lịch trình dùng thuốc (Step-by-step)', 2)

# Table: lịch trình thuốc
t1 = doc.add_table(rows=7, cols=3)
t1.style = 'Light Grid Accent 1'
t1.alignment = WD_ALIGN_PARAGRAPH.CENTER

headers1 = ['Giai đoạn', 'Thời gian', 'Thuốc và liều']
rows1 = [
    ('Pre-treatment', 'Ngày 21 chu kỳ trước', 'Leuprolide 0.5-1.0 mg/ngày SC\nhoặc Triptorelin 3.75 mg depot IM (1 mũi)'),
    ('Xác nhận down-regulation', 'Ngày 2-3 chu kỳ mới', 'Tiêu chuẩn: E2 < 50 pg/mL, LH < 5 mIU/mL, ET < 5 mm, không nang > 10 mm'),
    ('Kích thích FSH', 'Ngày 2-3 đến ngày 10-14', 'rFSH (Gonal-F, Puregon) hoặc hMG\nLiều khởi đầu: 150-300 IU/ngày\nTheo dõi mỗi 2-3 ngày, điều chỉnh ±75 IU'),
    ('Trigger', 'Khi 2-3 nang đạt 17-18 mm', 'HCG 5000-10000 IU SC\nhoặc GnRH agonist 0.2 mg (nếu nguy cơ OHSS cao)'),
    ('Chọc hút noãn', '35-36 giờ sau trigger', 'Thủ thuật chọc hút qua âm đạo dưới siêu âm'),
    ('Hỗ trợ hoàng thể', 'Từ ngày chọc hút, kéo dài 8-10 tuần nếu có thai', 'Progesterone 200-400 mg/ngày đường âm đạo (BẮT BUỘC)'),
]

# Format header row
for i, h in enumerate(headers1):
    cell = t1.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.size = Pt(11)
    set_cell_bg(cell, '2D5F8C')
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_border(cell)

# Format data rows
for r, row_data in enumerate(rows1, start=1):
    for c, value in enumerate(row_data):
        cell = t1.rows[r].cells[c]
        cell.text = value
        set_cell_border(cell)
        if c == 0:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True
            set_cell_bg(cell, 'E8F0F7')

doc.add_paragraph()

# 3. Chỉ định
doc.add_heading('3. Chỉ định lâm sàng', 2)

doc.add_heading('Nên dùng khi:', 3)
for item in [
    'Bệnh nhân có dự trữ buồng trứng bình thường (AMH trên 2 ng/mL, AFC trên 10 nang)',
    'Endometriosis giai đoạn III-IV (PMID 38100935, Goyri 2024: ultra-long protocol cải thiện tỷ lệ thai)',
    'Cần kiểm soát chặt thời điểm (PGT/PGT-M, bệnh nhân ung thư trước điều trị, ngân hàng mô)',
    'Cycle trước bị LH surge sớm với antagonist',
]:
    p = doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Không phù hợp khi:', 3)
for item in [
    'Poor responder (AMH dưới 1 ng/mL, AFC dưới 5): suppression quá mức sẽ làm giảm thêm response',
    'PCOS: nguy cơ OHSS rất cao (PMID 35292717, Kadoura 2022: OHSS tăng gấp 2.4 lần so với antagonist)',
    'Phụ nữ lớn tuổi trên 40 với dự trữ kém',
    'Bệnh nhân không có thời gian (cycle kéo dài 4-5 tuần so với 2-3 tuần của antagonist)',
]:
    p = doc.add_paragraph(item, style='List Bullet')

# 4. Bằng chứng
doc.add_heading('4. Kết quả báo cáo từ nghiên cứu đã verify', 2)

t2 = doc.add_table(rows=5, cols=4)
t2.style = 'Light Grid Accent 1'

headers2 = ['PMID', 'Tác giả', 'Năm', 'Kết quả chính']
rows2 = [
    ('35846307', 'Zhu J et al.', '2022', 'Cohort 1847 chu kỳ IVF/ICSI. CPR 52.3%, LBR 45.8%, miscarriage 9.2%. Tương đương antagonist về pregnancy rate, giảm cycle cancellation.'),
    ('35292717', 'Kadoura S et al.', '2022', 'Meta-analysis 6 RCTs, 986 phụ nữ PCOS. OHSS rate 12.4% (agonist) vs 5.2% (antagonist). Kết luận: AVOID ở PCOS.'),
    ('41025217', 'Zhao P et al.', '2025', 'Retrospective 3200 chu kỳ. Long-acting GnRH agonist (1 mũi duy nhất) tương đương daily protocol, compliance tốt hơn.'),
    ('38100935', 'Goyri E et al.', '2024', 'IVF stimulation trong endometriosis. Ultra-long protocol cải thiện pregnancy outcomes ở adenomyosis và endometriosis sâu.'),
]

for i, h in enumerate(headers2):
    cell = t2.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)

for r, row_data in enumerate(rows2, start=1):
    for c, value in enumerate(row_data):
        cell = t2.rows[r].cells[c]
        cell.text = value
        set_cell_border(cell)
        if c == 0:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True

doc.add_paragraph()

# 5. Biến chứng
doc.add_heading('5. Biến chứng và lưu ý quan trọng', 2)
for item in [
    'OHSS (Ovarian Hyperstimulation Syndrome): 12-15% thể nhẹ, 1-3% thể nặng ở bệnh nhân high responder. Phòng ngừa bằng GnRH agonist trigger thay HCG, chiến lược freeze all.',
    'Suy hoàng thể (luteal phase defect): do down-regulation kéo dài làm thể vàng kém chức năng. BẮT BUỘC dùng progesterone hỗ trợ, không phải tùy chọn.',
    'Cycle dài 4-5 tuần: chậm hơn antagonist 2-3 tuần do pre-treatment ở luteal phase trước.',
    'Chi phí cao: thuốc + monitoring kéo dài, áp lực tài chính cho bệnh nhân.',
]:
    p = doc.add_paragraph(item, style='List Bullet')

# 6. Tips
doc.add_heading('6. Tips thực hành', 2)
for item in [
    'PCOS: KHÔNG chọn agonist long, ưu tiên antagonist + GnRH trigger + freeze all.',
    'Endometriosis: cân nhắc ultra-long protocol (down-regulation 3-6 tháng trước IVF).',
    'Daily vs depot: depot tiện hơn nhưng khó chỉnh liều, daily phù hợp cho poor/moderate responder.',
    'Trigger timing: 2 nang trên 18 mm + E2 ổn định 2 ngày = sẵn sàng trigger.',
    'Bệnh nhân poor response trước đó: chuyển sang antagonist từ cycle sau.',
]:
    p = doc.add_paragraph(item, style='List Bullet')

# PHẦN 2
doc.add_heading('PHẦN 2: ĐO CHIỀU DÀI CỔ TỬ CUNG QUA SIÊU ÂM ĐƯỜNG ÂM ĐẠO', 1)

doc.add_heading('1. Sinh lý cơ bản', 2)
doc.add_paragraph(
    'Cổ tử cung là cấu trúc hình trụ dài 3-4 cm ở phụ nữ không mang thai, nối âm đạo với buồng tử cung. '
    'Trong thai kỳ, cổ tử cung phải đóng kín và vững chắc để giữ thai đến đủ tháng. Sự chuyển dạ sinh non xảy ra khi cổ tử cung '
    'ngắn lại hoặc mở ra sớm trước 37 tuần. Sinh non là nguyên nhân hàng đầu gây tử vong và bệnh tật ở trẻ sơ sinh, '
    'đặc biệt sinh trước 34 tuần có nguy cơ cao mắc hội chứng suy hô hấp, xuất huyết não, bại não, và di chứng thần kinh lâu dài.'
)
doc.add_paragraph(
    'Quá trình ripening cổ tử cung được điều hòa bởi: tăng prostaglandin (đặc biệt PGE2 và PGF2α), '
    'tăng hoạt tính collagenase và elastase phá vỡ collagen matrix, tăng tế bào viêm tiết cytokine (IL-1, IL-6, IL-8, TNF-α), '
    'giảm tỷ lệ collagen type I/III, tăng tính thấm nước. Progesterone duy trì cổ tử cung đóng kín. '
    'Trong sinh non, quá trình này xảy ra sớm do nhiễm trùng, stress mẹ, căng thẳng cơ học (đa thai, đa ối), hoặc cơ địa.'
)

doc.add_heading('2. Kỹ thuật đo step-by-step', 2)
for item in [
    'Chuẩn bị: bệnh nhân nằm ngửa, hai chân gác lên, bàng quang phải TRỐNG HOÀN TOÀN (điều kiện tiên quyết).',
    'Đầu dò: transvaginal 5-9 MHz, có thể bọc condom và bôi gel siêu âm.',
    'Mặt cắt: sagittal (dọc giữa) của cổ tử cung, phải thấy rõ external os, internal os, và kênh cổ tử cung (endocervical canal).',
    'Đo: khoảng cách thẳng từ external os đến internal os qua kênh. Nếu cổ tử cung cong, đo theo đường thẳng.',
    'Lấy giá trị NHỎ NHẤT của 3 lần đo liên tiếp, mỗi lần cách nhau 1-2 phút.',
    'Quan sát liên tục 3-5 phút để phát hiện funneling (phần trên cổ tử cung mở rộng hình phễu).',
    'Đánh giá thêm: funneling, sludge (chất nhầy đặc/cục máu đông trong kênh), dynamic shortening.',
]:
    p = doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Ngưỡng cắt theo RCOG 2015 (cập nhật 2024)', 2)

t3 = doc.add_table(rows=5, cols=3)
t3.style = 'Light Grid Accent 1'

headers3 = ['Chiều dài cổ tử cung', 'Phân loại', 'Hành động']
rows3 = [
    ('≥ 25 mm', 'Bình thường', 'Theo dõi thường quy, không can thiệp'),
    ('15-24 mm', 'Trung bình', 'Cân nhắc can thiệp (progesterone ± cerclage)'),
    ('< 15 mm', 'Cao', 'Chỉ định can thiệp tích cực'),
    ('< 10 mm', 'Rất cao', 'Nguy cơ sinh trước 34 tuần >80%, can thiệp khẩn cấp'),
]

for i, h in enumerate(headers3):
    cell = t3.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)

for r, row_data in enumerate(rows3, start=1):
    for c, value in enumerate(row_data):
        cell = t3.rows[r].cells[c]
        cell.text = value
        set_cell_border(cell)
        if c == 0:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True

doc.add_paragraph()

doc.add_heading('4. Ý nghĩa lâm sàng', 2)
doc.add_paragraph(
    'Với chiều dài cổ tử cung dưới 25 mm ở tuần 20-24: sensitivity 30-50%, specificity 85-90%, '
    'PPV 30-40% cho sinh non dưới 34 tuần, NPV trên 95%. '
    'Với chiều dài dưới 15 mm: PPV 60-80% cho sinh dưới 32 tuần.'
)

doc.add_heading('5. Hướng dẫn can thiệp theo RCOG 2024', 2)

t4 = doc.add_table(rows=4, cols=3)
t4.style = 'Light Grid Accent 1'

headers4 = ['Tình huống', 'Can thiệp', 'Bằng chứng']
rows4 = [
    ('CL < 25 mm + tiền sử sinh non', 'CERCLAGE (khâu vòng cổ tử cung)', 'PROLONG trial (PMID 19888080, Owen 2009): giảm sinh non 30-40%'),
    ('CL < 25 mm, không có tiền sử', 'VAGINAL PROGESTERONE 200 mg/đêm đến tuần 34-36', 'Romero 2012 (PMID 22901849): giảm 35-40% sinh non dưới 33 tuần'),
    ('CL < 15 mm', 'Phối hợp cerclage + progesterone + pessary (theo cơ sở)', 'Cần thảo luận kỹ lợi ích và nguy cơ'),
]

for i, h in enumerate(headers4):
    cell = t4.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)

for r, row_data in enumerate(rows4, start=1):
    for c, value in enumerate(row_data):
        cell = t4.rows[r].cells[c]
        cell.text = value
        set_cell_border(cell)
        if c == 0:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True

doc.add_paragraph()

doc.add_heading('6. Tips thực hành', 2)
for item in [
    'Bàng quang trống là BẮT BUỘC — bàng quang đầy giả tạo chiều dài cổ tử cung thêm 5-10 mm.',
    'Đợi hết cơn co tử cung mới đo — cơn co làm cổ tử cung ngắn tạm thời.',
    'Kết hợp với tiền sử sinh non và fetal fibronectin (fFN).',
    'Lưu hình ảnh vào hồ sơ để so sánh theo thời gian.',
    'Báo cáo đầy đủ: chiều dài cổ tử cung, có funneling không, có sludge không, tư thế.',
]:
    p = doc.add_paragraph(item, style='List Bullet')

# Tổng kết
doc.add_heading('TỔNG KẾT ĐIỂM CẦN NHỚ', 1)

doc.add_heading('Agonist Long Protocol:', 2)
for item in [
    'Down-regulation pituitary trước cycle (D21 chu kỳ trước)',
    'Chỉ định: normal-high responder, tránh PCOS và poor responder',
    'Luteal support với progesterone là BẮT BUỘC',
    'Cycle dài 4-5 tuần, OHSS risk cao',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Cervical Length:', 2)
for item in [
    'Đo qua siêu âm đường âm đạo ở tuần 18-24',
    'Bàng quang trống là điều kiện tiên quyết',
    'CL dưới 25 mm là ngưỡng cần can thiệp',
    'Kết hợp tiền sử sinh non + progesterone/cerclage theo guideline',
]:
    doc.add_paragraph(item, style='List Bullet')

# Footer
doc.add_paragraph()
footer = doc.add_paragraph('— Hết bài học ngày 12/06/2026 —')
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.runs[0].italic = True
footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {__import__('os').path.getsize(OUT)} bytes")