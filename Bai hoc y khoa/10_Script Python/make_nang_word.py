"""Tạo file Word cho bài học nang tồn dư buồng trứng trong ART."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:\Users\THANHANH\.mavis\agents\mavis\workspace\bai_nang_ton_du_ART_2026-06-13.docx"

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

title = doc.add_heading('NANG TỒN DƯ BUỒNG TRỨNG VÀ Ý NGHĨA TRONG ART', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph('Bài học IVF ngày 13/06/2026')
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
doc.add_paragraph()

doc.add_heading('1. Định nghĩa và phân loại', 1)
doc.add_heading('1.1 Nang tồn dư sau phẫu thuật (ovarian remnant syndrome)', 2)
doc.add_paragraph(
    'Mô buồng trứng còn sót lại sau phẫu thuật cắt buồng trứng (oophorectomy), '
    'thường do phẫu thuật khó, dính nhiều. Bệnh cảnh hay gặp: phẫu thuật cắt buồng trứng '
    'trong endometriosis giai đoạn nặng, viêm vùng chậu mạn, dính tiểu khung. '
    'Vẫn có thể hoạt động nội tiết, có thể tạo nang, có thể đau. '
    'Chẩn đoán: siêu âm thấy mô buồng trứng cạnh vị trí cắt; FSH/E2 có thể thấp dù đã cắt.'
)

doc.add_heading('1.2 Nang cơ năng buồng trứng (functional ovarian cyst)', 2)
for item in [
    'Nang nang noãn (follicular cyst): nang trứng không vỡ, tiếp tục phát triển',
    'Nang hoàng thể (luteal cyst): sau rụng trứng, hoàng thể hóa lỏng thành nang',
    'Nang hoàng thể xuất huyết (hemorrhagic corpus luteum): chảy máu trong nang hoàng thể',
    'Kích thước: thường < 5 cm, lành tính',
    'Cơ chế: tăng FSH/HCG kích thích, không vỡ nang đúng chu kỳ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('1.3 Nang tồn dư do thuốc (phổ biến nhất trong ART)', 2)
doc.add_paragraph(
    'Theo PMID 16253965 (Qublan 2006): nang buồng trứng có thể hình thành trong quá trình dùng '
    'GnRH agonist ở giai đoạn đầu (hiện tượng flare-up) hoặc do suppression không hoàn toàn '
    'trong agonist long protocol.'
)

doc.add_heading('2. Cơ chế hình thành nang trong ART', 1)

doc.add_heading('2.1 Nang sau GnRH agonist', 2)
doc.add_paragraph(
    'PMID 16253965 (Qublan 2006) báo cáo: tỷ lệ hình thành nang sau khi dùng GnRH agonist '
    'trong IVF khoảng 8-12%. Cơ chế gồm:'
)
for item in [
    'Flare-up ban đầu: 2-3 ngày đầu, FSH/LH tăng vọt kích thích nang nhỏ phát triển',
    'Nang tồn tại qua down-regulation: nang lớn > 10 mm không co lại được',
    'Không đáp ứng suppression: nang có tự chủ steroidogenesis',
]:
    doc.add_paragraph(item, style='List Bullet')
doc.add_paragraph('Nang này có thể:')
for item in [
    'Tự thoái triển trong vài tuần (40-60% trường hợp)',
    'Tồn tại dai dẳng, ảnh hưởng chất lượng noãn',
    'Twist buồng trứng hoặc vỡ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('2.2 Nang trong antagonist protocol', 2)
doc.add_paragraph(
    'Ít gặp hơn vì không có flare-up. Có thể xuất hiện do nang cơ năng không thoái triển '
    'giữa 2 chu kỳ. Tỷ lệ: 3-5% theo một số nghiên cứu.'
)

doc.add_heading('3. Ảnh hưởng của nang tồn dư trong ART', 1)

doc.add_heading('3.1 Ảnh hưởng lên số lượng và chất lượng noãn', 2)
for sub, content in [
    ('Giả thuyết 1: Ức chế nang mới',
     'Nang lớn tiết estrogen tự chủ → feedback âm → ức chế FSH nội sinh → cohort nang mới ít được tuyển chọn → giảm số noãn thu được.'),
    ('Giả thuyết 2: Cạnh tranh FSH',
     'Nang tồn dư tiêu thụ FSH → giảm FSH cho cohort mới. Đặc biệt trong cycle mới bắt đầu.'),
    ('Giả thuyết 3: Ảnh hưởng chất lượng noãn',
     'Một số nghiên cứu cho thấy tăng tỷ lệ noãn bất thường, giảm tỷ lệ thụ tinh. '
     'PMID 19657665 (Firouzabadi 2010) báo cáo giảm số noãn M2 khi có nang lớn > 16mm.'),
]:
    doc.add_heading(sub, 3)
    doc.add_paragraph(content)

doc.add_heading('3.2 Nguy cơ biến chứng', 2)
for item in [
    'Twist buồng trứng: nang lớn > 5-6 cm, đặc biệt nếu hai bên',
    'Vỡ nang: cấp cứu, xuất huyết trong ổ bụng',
    'Xuất huyết trong nang: đau, có thể cần phẫu thuật',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Cách xử lý nang tồn dư trong ART', 1)

t1 = doc.add_table(rows=5, cols=3)
t1.style = 'Light Grid Accent 1'

headers1 = ['Phương pháp', 'Chỉ định', 'Bằng chứng']
rows1 = [
    ('Theo dõi thụ động', 'Nang < 5 cm, không triệu chứng, lành tính', 'Tự thoái trong 1-3 tháng'),
    ('Hút nang qua đường âm đạo', 'Nang > 5-6 cm, tồn tại > 2-3 tháng, có triệu chứng', 'PMID 25502626 (Cochrane 2014): KHÔNG cải thiện live birth rate'),
    ('OCP / GnRH antagonist ngắn hạn', 'Nang cơ năng, cần đồng bộ cohort', 'Đồng bộ cohort nang, giảm FSH nội sinh'),
    ('Phẫu thuật nội soi', 'Nang > 7-8 cm, nghi ác tính, biến chứng', 'Hiếm, chỉ khi thật cần'),
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

doc.add_heading('4.1 Tiêu chuẩn SIÊU ÂM đánh giá nang', 2)
for item in [
    'Nang đơn thuần (simple cyst): mỏng, trong, không vách, không solid → gần như chắc chắn lành tính',
    'Nang phức tạp (complex): có vách, nhú, solid, dịch đục → nghi ngờ cao',
    'Kích thước > 7 cm: nguy cơ ác tính tăng (đặc biệt sau mãn kinh)',
    'IOTA simple rules: tiêu chuẩn chuẩn hóa đánh giá nang buồng trứng',
    'Đặc điểm nghi ngờ ác tính: nhú, vách dày, thành không đều, dịch đặc, Doppler RI < 0.4',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Hướng dẫn hiện hành (ASRM 2023, ESHRE 2023)', 1)

t2 = doc.add_table(rows=4, cols=3)
t2.style = 'Light Grid Accent 1'

headers2 = ['Kích thước nang', 'Xử trí', 'Ghi chú']
rows2 = [
    ('< 3 cm', 'KHÔNG can thiệp, tiến hành kích thích', 'Thường là nang cơ năng'),
    ('3-5 cm', 'Cân nhắc theo dõi hoặc dùng OCP 1-2 tháng', 'Đánh giá đặc điểm siêu âm'),
    ('> 5 cm hoặc nghi ngờ', 'Đánh giá thêm, có thể hút/phẫu thuật', 'Loại trừ ác tính trước'),
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

doc.add_heading('6. Điểm cần nhớ', 1)
for item in [
    'Nang tồn dư buồng trứng phổ biến trong ART, đặc biệt với GnRH agonist (8-12%)',
    'Cơ chế: flare-up đầu + suppression không hoàn toàn + nang cơ năng tồn tại',
    'Hút nang thường quy KHÔNG cải thiện tỷ lệ thai (Cochrane 2014)',
    'Xử lý: theo dõi + OCP, hút nang chỉ khi cần, phẫu thuật khi nghi ác tính',
    'Tiêu chuẩn IOTA simple rules giúp đánh giá chuẩn hóa',
    'Nang buồng trứng và OHSS: cùng cơ chế với PCOS, tăng nguy cơ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Tài liệu tham khảo', 1)
for item in [
    'PMID 16253965 (Qublan 2006): Nang buồng trứng sau GnRH agonist trong IVF',
    'PMID 25502626 (McDonnell 2014, Cochrane): Hút nang trước IVF',
    'PMID 19657665 (Firouzabadi 2010): Hút nang với GnRH protocol',
    'ASRM Practice Committee 2023: Nang buồng trứng và ART',
    'ESHRE Guideline 2023: Quản lý nang trong ART',
]:
    doc.add_paragraph(item, style='List Bullet')

footer = doc.add_paragraph('— Hết bài học ngày 13/06/2026 —')
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.runs[0].italic = True
footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {__import__('os').path.getsize(OUT)} bytes")