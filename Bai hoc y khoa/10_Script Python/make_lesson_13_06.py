"""Bài học IVF 13/06/2026: Cơ chế LH surge & Rụng trứng."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:\Users\THANHANH\.mavis\agents\mavis\workspace\bai_hoc_ivf_2026-06-13.docx"

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

title = doc.add_heading('BÀI HỌC IVF NGÀY 13/06/2026', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph('Cơ chế LH surge tự nhiên & rụng trứng — Nền tảng hiểu về trigger trong ART')
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
doc.add_paragraph()

doc.add_heading('PHẦN 1: CƠ CHẾ LH SURGE TỰ NHIÊN', 1)

doc.add_heading('1. Vai trò của HPO axis', 2)
doc.add_paragraph(
    'Trục HPO (Hypothalamic-Pituitary-Ovarian) điều hòa toàn bộ chu kỳ sinh sản nữ. '
    'Trong đó, GnRH (Gonadotropin-Releasing Hormone) từ vùng dưới đồi tiết ra theo xung (pulse), '
    'tần số và biên độ thay đổi theo pha chu kỳ. Ở pha nang noãn muộn, xung GnHR tăng tần số (~1 xung/giờ), '
    'kích thích thùy trước tuyến yên giải phóng FSH và LH. Hai hormone này tác động lên buồng trứng: '
    'FSH kích thích nang trứng trưởng thành, LH kích thích tế bào vỏ tiết androgen, tế bào hạt chuyển thành estrogen. '
    'Khi nồng độ estrogen đạt ngưỡng cao (~200-300 pg/mL) và duy trì ≥48 giờ, '
    'có sự chuyển từ feedback âm sang feedback dương lên vùng dưới đồi và tuyến yên, '
    'gây ra đỉnh LH (LH surge) — yếu tố kích hoạt rụng trứng.'
)

doc.add_heading('2. Tế bào thần kinh Kisspeptin', 2)
doc.add_paragraph(
    'Theo PMID 36479214 (Stevenson 2022) và PMID 36842628 (Piet 2023), kisspeptin là peptide '
    'then chốt điều hòa GnRH. Tế bào thần kinh Kisspeptin nằm ở vùng dưới đồi (nucleus arcuate và anteroventral periventricular nucleus). '
    'Ở nucleus arcuate, tạo xung GnRH đều đặn (pulse generator). Ở vùng periventricular, '
    'chịu ảnh hưởng estrogen → tạo surge GnRH khi estrogen cao kéo dài.'
)
doc.add_paragraph(
    'Cơ chế estrogen → kisspeptin → GnRH surge → LH surge:'
)
for item in [
    'Nang trội tiết estrogen tăng dần',
    'Estrogen cao kích hoạt Kiss1 neurons ở AVPV',
    'Kisspeptin tăng → kích thích GnRH neurons',
    'GnRH surge → LH surge mạnh',
    'LH surge kích hoạt rụng trứng sau 36-40 giờ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Đặc điểm của LH surge', 2)
for item in [
    'Biên độ: tăng 5-10 lần so với nền (từ 5-20 mIU/mL lên 40-100+ mIU/mL)',
    'Thời gian: kéo dài 48-50 giờ (3 pha: tăng → đỉnh ~12-24h → giảm dần)',
    'Mục tiêu: vỡ nang trội (rupture) + chuyển nang thành hoàng thể',
    'Kết quả: phóng noãn vào vòi trứng, bắt đầu luteinization',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Tại sao LH surge tự nhiên 36-40 giờ mới rụng trứng?', 2)
doc.add_paragraph(
    'LH surge không làm nang vỡ ngay. Nó kích hoạt một loạt quá trình kế tiếp:'
)
for item in [
    'Giờ 0-12: LH kích hoạt tế bào hạt + tế bào vỏ, tăng progesterone và prostaglandin',
    'Giờ 12-24: Hoạt hóa enzyme protease (MMP, plasmin), thoái biến collagen ở thành nang',
    'Giờ 24-36: Nang mỏng dần, NO và prostaglandin giãn mạch cục bộ',
    'Giờ 36-40: Vỡ nang, phóng noãn vào vòi trứng',
    'Sau đó: Luteinization, tạo hoàng thể tiết progesterone',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Ứng dụng vào trigger trong ART', 2)
doc.add_paragraph(
    'Hiểu LH surge giúp thiết kế protocol trigger phù hợp:'
)

t1 = doc.add_table(rows=5, cols=3)
t1.style = 'Light Grid Accent 1'

headers1 = ['Loại trigger', 'Cơ chế', 'Ghi chú']
rows1 = [
    ('hCG 5000-10000 IU', 'Bắt chước LH nhờ chung thụ thể LHCGR, thời gian bán hủy dài (~30 giờ)', 'Trigger chuẩn, an toàn, kinh tế'),
    ('GnRH agonist trigger (0.2 mg Triptorelin)', 'Kích thích tuyến yên giải phóng LH + FSH nội sinh (surge tự nhiên)', 'OHSS thấp, nhưng luteal phase yếu, cần hỗ trợ'),
    ('hCG + GnRH agonist dual trigger', 'Cả hai cùng lúc, tận dụng ưu điểm', 'Cải thiện tỷ lệ thụ tinh, chín noãn tốt hơn'),
    ('Kisspeptin (thử nghiệm)', 'Kích hoạt GnRH nội sinh, gây LH surge tự nhiên', 'Đang nghiên cứu lâm sàng'),
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

doc.add_heading('PHẦN 2: CƠ CHẾ RỤNG TRỨNG (OVULATION)', 1)

doc.add_heading('1. Định nghĩa và quá trình', 2)
doc.add_paragraph(
    'Rụng trứng là sự vỡ nang trội (dominant follicle) để phóng noãn (oocyte) ra ngoài buồng trứng, '
    'sau đó được tua (fimbriae) của vòi trứng hứng lấy. Quá trình này xảy ra vào khoảng giữa chu kỳ kinh nguyệt (ngày 14 của cycle 28 ngày).'
)
doc.add_paragraph(
    'Theo PMID 30496379 (Duffy 2019, Endocr Rev), rụng trứng có sự tương đồng đáng kinh ngạc với quá trình viêm (parallels with inflammatory processes). '
    'Các cytokine, prostaglandin, và tế bào miễn dịch đều tham gia tích cực.'
)

doc.add_heading('2. Các bước của quá trình rụng trứng', 2)

t2 = doc.add_table(rows=8, cols=2)
t2.style = 'Light Grid Accent 1'

headers2 = ['Giai đoạn', 'Sự kiện chính']
rows2 = [
    ('Pha nang sớm (ngày 1-7)', 'FSH tuyển chọn cohort nang, nang trội bắt đầu nổi bật'),
    ('Pha nang muộn (ngày 7-12)', 'Nang trội tiết estrogen tăng dần, các nang khác thoái'),
    ('Estrogen đỉnh (ngày 12-13)', 'E2 > 200-300 pg/mL, kéo dài > 48h → chuyển feedback dương'),
    ('LH surge khởi phát (giờ 0)', 'GnRH surge → LH surge tăng 5-10 lần'),
    ('Resumption of meiosis (giờ 0-12)', 'Oocyte hoàn thành meiosis I, bắt đầu meiosis II, đến metaphase II'),
    ('Cumulus expansion (giờ 12-24)', 'Tế bào cumulus tách ra, noãn chuẩn bị phóng'),
    ('Vỡ nang (giờ 36-40)', 'Collagen thành nang thoái biến, prostaglandin gây co bóp, vỡ nang'),
    ('Luteinization (sau 0-24h)', 'Tế bào hạt + vỏ chuyển thành tế bào lutein, bắt đầu tiết progesterone'),
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

doc.add_heading('3. Các yếu tố điều hòa chính', 2)
for item in [
    'LH surge: yếu tố kích hoạt, bắt buộc cho rụng trứng',
    'FSH surge: phối hợp với LH, hỗ trợ chín noãn',
    'Progesterone: tăng nhẹ trước LH surge (từ nang trội), giúp tăng đáp ứng LH',
    'Prostaglandin (PGE2, PGF2α): gây viêm cục bộ + co bóp nang, NO giãn mạch',
    'Enzyme thoái giáng collagen: MMP (matrix metalloproteinase), plasmin',
    'Cytokine: TNF-α, IL-1, IL-6 — tạo môi trường viêm cần thiết',
    'Tế bào miễn dịch: macrophage, neutrophil — "cleanup crew" sau rụng trứng',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Cơ chế phân tử (Molecular mechanism)', 2)
for item in [
    'LH gắn thụ thể LHCGR (G-protein coupled receptor) trên tế bào hạt + tế bào vỏ',
    'Kích hoạt adenylyl cyclase → tăng cAMP → hoạt hóa PKA',
    'PKA kích hoạt ERK1/2 → tăng COX-2 → tăng prostaglandin',
    'PKA kích hoạt STAR (steroidogenic acute regulatory protein) → vận chuyển cholesterol vào ti thể',
    'STAR → CYP11A1 → pregnenolone → progesterone',
    'Tăng MMP-2, MMP-9 → thoái giáng collagen type IV ở thành nang',
    'Prostaglandin → co cơ trơn vỏ nang + giãn mạch → vỡ nang',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Bất thường của quá trình rụng trứng', 2)
for item in [
    'Anovulation: không phóng noãn (PCOS, suy buồng trứng, stress)',
    'Luteinized unruptured follicle (LUF) syndrome: nang chín nhưng không vỡ, có progesterone',
    'Premature LH surge: gặp trong ART, làm hỏng cycle (phải dùng GnRH antagonist)',
    'Empty follicle syndrome: chọc hút không có noãn, hiếm gặp',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 2: SIÊU ÂM THAI - 4 MẶT CẮT TIM', 1)

doc.add_heading('1. Tầm quan trọng của sàng lọc', 2)
doc.add_paragraph(
    'Dị tật tim bẩm sinh (CHD) chiếm 8-10/1000 trẻ sơ sinh sống - là dị tật bẩm sinh phổ biến nhất. '
    'Siêu âm hình thái tuần 18-22 là thời điểm quan trọng để đánh giá 4 mặt cắt tim cơ bản.'
)

doc.add_heading('2. 4 mặt cắt cơ bản theo ISUOG', 2)
for item in [
    'Mặt cắt bốn buồng: kích thước buồng tim, tỷ lệ tim/ngực, vách liên thất, van nhĩ thất',
    'LVOT: đường ra thất trái, van động mạch chủ, liên tục với vách liên thất',
    '3-vessel view: ĐMP, ĐMC, TMCT - phát hiện TGA khi chỉ thấy 2 mạch',
    'Arch view: cung ĐMC hình candy cane, ống động mạch',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Các chỉ định siêu âm tim thai chuyên sâu', 2)
for item in [
    'Tiền sử gia đình có CHD',
    'Bất thường nhiễm sắc thể (Down, Turner, DiGeorge)',
    'NT dày >= 3.5 mm',
    'Đái tháo đường thai kỳ, SLE, dùng thuốc gây quái thai',
    'Bất thường trên siêu âm hình thái',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('ĐIỂM CẦN NHỚ', 1)
for item in [
    'HPO axis: GnRH → FSH/LH → estrogen → LH surge → rụng trứng',
    'Kisspeptin là peptide then chốt kích hoạt GnRH surge (PMID 36479214, 36842628)',
    'LH surge tự nhiên: biên độ tăng 5-10 lần, kéo dài 48-50 giờ',
    'Rụng trứng xảy ra 36-40 giờ sau đỉnh LH',
    'hCG bắt chước LH nhờ chung thụ thể LHCGR - thời gian bán hủy dài hơn',
    'Siêu âm tim thai 4 mặt cắt ở tuần 18-22 bắt buộc cho mọi thai kỳ',
    'PMID 30496379 (Duffy 2019): rụng trứng có sự tương đồng với quá trình viêm',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('TÀI LIỆU THAM KHẢO', 1)
for item in [
    'PMID 36479214 (Stevenson 2022, Front Endocrinol): Kisspeptin-neuron control of LH pulsatility and ovulation',
    'PMID 36842628 (Piet 2023, Peptides): Circadian and kisspeptin regulation of the preovulatory surge',
    'PMID 30496379 (Duffy 2019, Endocr Rev): Ovulation: Parallels With Inflammatory Processes',
    'PMID 35856663 (Fiorentino 2023, Hum Reprod Update): Biomechanical forces in ovary',
    'PMID 37227365 (Moon-Grady 2023, ASE): Fetal echocardiography guidelines',
    'PMID 40208627 (De Robertis 2025): Indications for fetal echocardiography consensus',
]:
    doc.add_paragraph(item, style='List Bullet')

footer = doc.add_paragraph('— Hết bài học ngày 13/06/2026 —')
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.runs[0].italic = True
footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {__import__('os').path.getsize(OUT)} bytes")