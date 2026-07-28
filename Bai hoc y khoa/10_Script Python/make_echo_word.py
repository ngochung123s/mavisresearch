"""Siêu âm tim thai - file Word."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:\Users\THANHANH\.mavis\agents\mavis\workspace\sieu_am_tim_thai_2026-06-13.docx"

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
style = doc.styles['Normal']
style.font.name = 'Arial'
style.font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

title = doc.add_heading('HƯỚNG DẪN THỰC HÀNH SIÊU ÂM TIM THAI', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph('Bài học ngày 13/06/2026')
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
doc.add_paragraph()

doc.add_heading('1. Tổng quan dị tật tim bẩm sinh (CHD)', 1)
doc.add_paragraph(
    'Dị tật tim bẩm sinh (CHD) là dị tật bẩm sinh phổ biến nhất: tỷ lệ 8-10/1000 trẻ sơ sinh sống. '
    'Là nguyên nhân tử vong hàng đầu ở trẻ sơ sinh do dị tật bẩm sinh. Khoảng 1/4 trường hợp cần phẫu thuật '
    'trong năm đầu đời. Phát hiện sớm giúp can thiệp kịp thời, cải thiện tiên lượng.'
)

doc.add_heading('2. Cấp độ sàng lọc tim thai', 1)

doc.add_heading('2.1 Sàng lọc cơ bản', 2)
doc.add_paragraph(
    'Thực hiện bởi bác sĩ sản khoa, nữ hộ sinh siêu âm. Thời điểm: siêu âm hình thái tuần 18-22 '
    '(anatomy scan). Mục tiêu: phát hiện sơ bộ, chuyển tuyến kịp thời nếu nghi ngờ. '
    'Tiêu chuẩn: 4 mặt cắt cơ bản theo ISUOG.'
)

doc.add_heading('2.2 Siêu âm tim thai chuyên sâu', 2)
doc.add_paragraph(
    'Thực hiện bởi bác sĩ chuyên khoa tim mạch nhi hoặc sản khoa được đào tạo về tim thai. '
    'Thời điểm: tuần 18-22 hoặc bất kỳ khi có chỉ định. Mục tiêu: chẩn đoán xác định, '
    'đánh giá chi tiết, tư vấn tiên lượng. Nội dung: đầy đủ các mặt cắt, đo đạc, đánh giá chức năng. '
    'Theo PMID 40208627 (De Robertis 2025) - consensus quốc tế về chỉ định.'
)

doc.add_heading('3. 4 mặt cắt cơ bản theo ISUOG', 1)
doc.add_paragraph('Theo ISUOG Practice Guidelines 2006, cập nhật 2013:')

doc.add_heading('3.1 Mặt cắt bốn buồng (four-chamber view)', 2)
for item in [
    'Vị trí: ngang ngực thai nhi, ngang mức tim',
    'Tâm thất trái (LV): hình bầu dục, thành nhẵn, dày 3-4 mm tuần 20',
    'Tâm thất phải (RV): hình tam giác, có moderator band, thành có vân',
    'Nhĩ trái, nhĩ phải: kích thước xấp xỉ bằng nhau',
    'Vách liên thất: nguyên vẹn',
    'Vách liên nhĩ: có lỗ bầu dục (foramen ovale) đập về nhĩ trái',
    'Van nhĩ thất: 2 van (van 2 lá trái, van 3 lá phải), van 3 lá chèn xuống thấp hơn van 2 lá',
    'Phát hiện: VSD lớn, bất thường vách liên thất, bất sản van, Ebstein anomaly, tim một thất',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3.2 Mặt cắt đường ra thất trái (LVOT view)', 2)
for item in [
    'Vị trí: hơi nghiêng đầu dò lên trên và sang phải thai nhi từ mặt cắt 4 buồng',
    'Đường ra thất trái: từ mỏm tim đi lên qua van động mạch chủ',
    'Van động mạch chủ: 3 lá van bình thường, không dày',
    'Vách liên thất liên tục với thành động mạch chủ (membranous continuity)',
    'Phát hiện: hẹp van động mạch chủ, VSD phần màng, bất sản van động mạch chủ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3.3 Mặt cắt đường ra thất phải và 3-vessel view', 2)
for item in [
    'Vị trí: nghiêng đầu dò thêm lên trên',
    'Động mạch phổi: từ thất phải, chia hai nhánh (PPA + PDA)',
    'Động mạch chủ: cắt ngang, nằm giữa',
    'Tĩnh mạch chủ trên: nằm bên phải, kích thước nhỏ nhất',
    'Tỷ lệ kích thước bình thường: ĐMP > ĐMC > TMCT',
    'Nếu chỉ thấy 2 mạch: nghi transposition đại động mạch (TGA)',
    'Phát hiện: TGA, bất thường cung động mạch chủ, hẹp động mạch phổi',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3.4 Mặt cắt cung động mạch chủ và cung ống động mạch (arch view)', 2)
for item in [
    'Cung động mạch chủ: cong hình candy cane, cho ra 3 nhánh',
    'Ống động mạch (ductus arteriosus): nối ĐMP với ĐMC xuống',
    'Hai cung giao nhau ở phía sau khí quản',
    'Phát hiện: coarctation ĐMC, cung động mạch chủ đôi, interruption of aortic arch, vascular ring',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Hướng dẫn ASE 2023', 1)
doc.add_paragraph('Theo Moon-Grady et al. 2023 (PMID 37227365), hướng dẫn cập nhật từ American Society of Echocardiography:')

doc.add_heading('4.1 Cấu trúc cần đánh giá', 2)
for item in [
    'Vị trí: tim trong lồng ngực, đỉnh chĩa xuống dưới-trái',
    'Tỷ lệ tim/ngực: 1/3 - 1/2 (không quá to)',
    'Bề dày cơ thất: thành LV dày ~3-4 mm tuần 20-22',
    'Chức năng: phân suất tống máu, fractional shortening',
    'Doppler màu: dòng chảy qua các van, vách',
    'Hệ thống mạch máu: các mạch máu lớn theo 4 mặt cắt',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4.2 Đo đạc chuẩn theo tuổi thai', 2)
for item in [
    'Đường kính các buồng tim',
    'Bề dày vách',
    'Đường kính van, động mạch chủ, động mạch phổi',
    'Chiều dài tâm thất',
    'So sánh với biểu đồ chuẩn theo tuổi thai (z-score)',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Siêu âm tim thai 3 tháng đầu (11-14 tuần)', 1)
doc.add_paragraph('Theo PMID 34369613 (Karim 2022) và PMID 40019943 (Yang 2025):')

doc.add_heading('5.1 Chỉ định', 2)
for item in [
    'Tiền sử gia đình có CHD (cha/mẹ/anh chị em)',
    'Bất thường nhiễm sắc thể (hội chứng Down, Turner, DiGeorge)',
    'Đái tháo đường thai kỳ',
    'Thai bất thường NT (nuchal translucency) ≥ 3.5 mm',
    'Dùng thuốc gây quái thai (ACEI, retinoid, lithium)',
    'Mẹ mắc bệnh tự miễn (lupus, antiphospholipid)',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5.2 Kỹ thuật', 2)
for item in [
    'Siêu âm qua đường bụng hoặc đường âm đạo với đầu dò tần số cao',
    'Có thể kết hợp với đo NT và DV (ductus venosus)',
    'Sử dụng Doppler xung để đánh giá dòng chảy',
    'Mặt cắt 4 buồng thường thấy được từ tuần 11',
    'Tỷ lệ phát hiện CHD nặng: 50-60%',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5.3 Hạn chế', 2)
for item in [
    'Tim còn nhỏ, khó đánh giá chi tiết',
    'Một số CHD chỉ biểu hiện muộn (sau 14-16 tuần)',
    'Cần siêu âm lại ở tuần 18-22 dù kết quả 3 tháng đầu bình thường',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('6. Chỉ định siêu âm tim thai chuyên sâu', 1)
doc.add_paragraph('Theo PMID 40208627 (De Robertis 2025):')

doc.add_heading('6.1 Chỉ định từ phía mẹ', 2)
for item in [
    'Tiền sử con trước bị CHD',
    'Bệnh tự miễn (SLE, antiphospholipid syndrome)',
    'Đái tháo đường thai kỳ (đặc biệt HbA1c cao)',
    'Dùng thuốc gây quái thai',
    'Bệnh phenylketon niệu không kiểm soát',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('6.2 Chỉ định từ phía thai', 2)
for item in [
    'Bất thường nhiễm sắc thể',
    'NT dày ≥ 3.5 mm hoặc DV bất thường',
    'Bất thường trên siêu âm hình thái',
    'Đa thai (đặc biệt MCMA, MCDA)',
    'Bất thường nhau ối (oligo, poly)',
    'Thai chậm tăng trưởng',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('6.3 Chỉ định từ gia đình', 2)
for item in [
    'Cha hoặc mẹ bị CHD',
    'Anh chị em ruột bị CHD (nguy cơ tái phát 2-3%)',
    'Hội chứng di truyền liên quan CHD (Noonan, DiGeorge, Williams, Turner)',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('7. Dị tật thường gặp', 1)

t1 = doc.add_table(rows=8, cols=4)
t1.style = 'Light Grid Accent 1'

headers1 = ['Dị tật', 'Tỷ lệ', 'Mặt cắt nghi ngờ', 'Hậu quả']
rows1 = [
    ('VSD', '25-30% CHD', '4 buồng hoặc LVOT', 'Tùy kích thước, có thể tự đóng'),
    ('ASD', '10%', '4 buồng', 'Thường muộn, cần theo dõi'),
    ('Fallot (TOF)', '5-7%', '3 vessel view', 'Phẫu thuật trong năm đầu'),
    ('TGA', '3-5%', '3 vessel view (chỉ thấy 2 mạch)', 'Cấp cứu PGE1 sau sinh'),
    ('Coarctation ĐMC', '5%', 'Cung ĐMC nhỏ', 'Cần phẫu thuật'),
    ('HLHS', '2-3%', '4 buồng (1 thất phát triển)', 'Cần nhiều phẫu thuật'),
    ('AVSD (Down)', '5%', '4 buồng (van chung)', 'Phẫu thuật'),
]

for i, h in enumerate(headers1):
    cell = t1.rows[0].cells[i]
    cell.text = h
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)

for r, row_data in enumerate(rows1, start=1):
    for c, value in enumerate(row_data):
        cell = t1.rows[r].cells[c]
        cell.text = value
        set_cell_border(cell)
        if c == 0:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.bold = True

doc.add_paragraph()

doc.add_heading('8. Thực hành siêu âm tim thai ở Việt Nam', 1)
doc.add_paragraph(
    'Hầu hết bệnh viện tuyến tỉnh: chỉ sàng lọc cơ bản (4 mặt cắt). '
    'Bệnh viện tuyến trung ương: có thể làm chuyên sâu (BV Từ Dũ, BV Hùng Vương, '
    'BV Nhi Trung Ương, BV Phụ sản Trung ương). Bệnh viện tỉnh phát hiện bất thường → chuyển tuyến.'
)

doc.add_heading('8.1 Lưu ý thực hành', 2)
for item in [
    'Luôn dùng Doppler màu khi khó thấy mặt cắt 4 buồng',
    'Không bỏ sót mặt cắt 3 vessel view - phát hiện TGA, double outlet right ventricle',
    'Nếu nghi ngờ: không vội kết luận, hẹn siêu âm lại sau 1-2 tuần hoặc chuyển tuyến',
    'Lưu hình ảnh cẩn thận để hội chẩn hoặc theo dõi',
    'Báo cáo đầy đủ: vị trí, kích thước, đo đạc, kết luận, đề xuất theo dõi',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('9. Tần suất theo dõi khi phát hiện bất thường', 1)

t2 = doc.add_table(rows=4, cols=2)
t2.style = 'Light Grid Accent 1'

headers2 = ['Mức độ nghi ngờ', 'Tần suất theo dõi']
rows2 = [
    ('Nghi ngờ nhẹ (focus tăng âm nhỏ, thành cơ tim dày nhẹ)', 'Siêu âm lại sau 4-6 tuần'),
    ('Nghi ngờ rõ (VSD lớn, bất thường cung)', 'Siêu âm lại sau 1-2 tuần'),
    ('Xác định bệnh', 'Theo dõi mỗi 2-4 tuần tùy mức độ'),
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

doc.add_heading('10. Điểm cần nhớ', 1)
for item in [
    'Siêu âm hình thái tuần 18-22: bắt buộc đánh giá 4 mặt cắt tim (4 buồng, LVOT, 3 vessel, arch)',
    'Siêu âm tim thai chuyên sâu: khi có chỉ định',
    'Tỷ lệ CHD: 8-10/1000, cao nhất trong các dị tật bẩm sinh',
    'Mặt cắt 3 vessel view: dễ quên nhưng quan trọng (phát hiện TGA)',
    'Tỷ lệ tim/ngực < 1/3 là bình thường',
    'LV dày ~3-4 mm tuần 20 là bình thường',
    'Nghi ngờ → siêu âm lại 1-2 tuần hoặc chuyển tuyến',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Tài liệu tham khảo', 1)
for item in [
    'PMID 37227365 (Moon-Grady 2023, ASE guideline): Hướng dẫn siêu âm tim thai cập nhật',
    'PMID 40208627 (De Robertis 2025): Consensus về chỉ định',
    'PMID 34369613 (Karim 2022, meta-analysis): Sàng lọc 3 tháng đầu',
    'PMID 40019943 (Yang 2025): Chiến lược sàng lọc 3 tháng đầu',
    'ISUOG Practice Guidelines 2006, cập nhật 2013',
    'Hướng dẫn Bộ Y tế Việt Nam về sàng lọc trước sinh',
]:
    doc.add_paragraph(item, style='List Bullet')

footer = doc.add_paragraph('— Hết bài học ngày 13/06/2026 —')
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.runs[0].italic = True
footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {__import__('os').path.getsize(OUT)} bytes")