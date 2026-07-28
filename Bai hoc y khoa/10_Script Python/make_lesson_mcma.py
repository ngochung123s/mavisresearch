"""Bài học Fetal Ultrasound 13/06/2026: Song thai 1 buồng ối (MCMA)."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:\Users\THANHANH\.mavis\agents\mavis\workspace\bai_hoc_fetal_2026-06-13.docx"

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

title = doc.add_heading('BÀI HỌC FETAL ULTRASOUND NGÀY 13/06/2026', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph('Song thai 1 bánh nhau 1 buồng ối (MCMA) — Quản lý, theo dõi và thời điểm can thiệp')
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
doc.add_paragraph()

doc.add_heading('PHẦN 1: ĐẠI CƯƠNG VÀ PHÂN LOẠI', 1)

doc.add_heading('1. Định nghĩa', 2)
doc.add_paragraph(
    'MCMA (Monochorionic Monoamniotic) là tình trạng song thai CÙNG GIỚI, CÙNG BÁNH NHAU, '
    'CÙNG BUỒNG ỐI. Hai thai chia sẻ chung một buồng ối nên không có màng ngăn cách (no inter-twin membrane). '
    'Đây là dạng song thai hiếm gặp nhưng có nguy cơ cao nhất trong các loại song thai.'
)
doc.add_paragraph('Tỷ lệ: 1/800-1/1000 thai kỳ, chiếm ~5% tổng số song thai một bánh nhau (MC).')

doc.add_heading('2. Phân loại song thai theo mức độ chia sẻ bánh nhau + buồng ối', 2)

t1 = doc.add_table(rows=5, cols=4)
t1.style = 'Light Grid Accent 1'

headers1 = ['Loại', 'Bánh nhau', 'Buồng ối', 'Tần suất']
rows1 = [
    ('DCDA (Dichorionic Diamniotic)', '2 bánh', '2 buồng', '~80% song thai tự nhiên'),
    ('MCDA (Monochorionic Diamniotic)', '1 bánh', '2 buồng', '~20% song thai tự nhiên, ~99% sau ET 2 phôi'),
    ('MCMA (Monochorionic Monoamniotic)', '1 bánh', '1 buồng', '~1% song thai tự nhiên, 1/800-1/1000 thai kỳ'),
    ('Conjoined twins (dính nhau)', '1 bánh', '1 buồng', '1/50.000-1/200.000, dạng đặc biệt của MCMA'),
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

doc.add_heading('3. Cơ chế hình thành', 2)
for item in [
    'Thụ tinh: 2 noãn thụ tinh bởi 2 tinh trùng khác nhau → 2 hợp tử → 2 phôi → DCDA (luôn)',
    'Nếu 1 noãn thụ tinh → 1 hợp tử → 1 phôi phân chia:',
    '+ Phân chia ngày 0-3 (morula): 2 bánh nhau 2 buồng ối → DCDA',
    '+ Phân chia ngày 4-8 (blastocyst): 1 bánh nhau 2 buồng ối → MCDA',
    '+ Phân chia ngày 8-13 (sau khi tạo túi ối): 1 bánh nhau 1 buồng ối → MCMA',
    '+ Phân chia ngày >13: dính nhau (conjoined twins)',
    'MCMA = phôi phân chia muộn, sau khi túi ối đã hình thành → không có màng ngăn',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 2: CHẨN ĐOÁN', 1)

doc.add_heading('1. Chẩn đoán trước sinh', 2)
doc.add_paragraph(
    'Thời điểm: có thể chẩn đoán từ tuần 8-14 nhờ siêu âm khi thấy:'
)
for item in [
    '1 bánh nhau (1 khối mô nhau đồng nhất, không có "lambda sign")',
    '1 buồng ối (không thấy màng ngăn giữa 2 thai)',
    '2 thai di động tự do trong cùng 1 buồng ối',
    'Dây rốn có thể thấy "cord entanglement" ngay từ 3 tháng đầu (PMID 33804073)',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_paragraph(
    'Đặc điểt: trên siêu âm có thể thấy các dấu hiệu âm tính của DCDA: KHÔNG có "lambda sign" '
    '(dấu hiệu chữ lambda ở vùng bánh nhau chỉ trong DCDA).'
)

doc.add_heading('2. Các dấu hiệu siêu âm đặc trưng MCMA', 2)
for item in [
    'No inter-twin membrane: không thấy màng ngăn giữa 2 thai ở mọi mặt cắt',
    'Insertion của dây rốn: thường gần nhau (do cùng bánh nhau), dễ thấy entanglement',
    'Dây rốn entanglement: nhìn thấy dây rốn xoắn vào nhau trong buồng ối',
    'Cùng giới tính: luôn cùng giới (vì từ cùng 1 hợp tử)',
    'Số lượng mạch máu: kiểm tra Doppler để phát hiện 2 thai có tuần hoàn liên tục',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Phân biệt với MCDA', 2)
for item in [
    'Màng ngăn: MCDA có màng ngăn mỏng (2 lớp amnion), MCMA không có màng',
    '"T-sign" trong MCDA: màng ngăn vuông góc với thành tử cung (do 2 lớp amnion ép sát)',
    'Trong MCMA: KHÔNG tìm thấy màng ngăn ở bất kỳ mặt cắt nào',
    'Có thể dùng Doppler để xác nhận: không thấy tín hiệu Doppler của màng ngăn',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 3: CÁC BIẾN CHỨNG', 1)

doc.add_paragraph(
    'Theo PMID 30125418 (D\'Antonio 2019, meta-analysis trên >2900 thai MCMA), '
    'tỷ lệ biến chứng cao: tử vong chu sinh 11-30% (so với 2-5% ở MCDA).'
)

doc.add_heading('1. Dây rốn thắt nút (Cord entanglement)', 2)
doc.add_paragraph(
    'Là biến chứng ĐẶC TRƯNG và NGUY HIỂM NHẤT của MCMA. Do 2 thai cùng chung buồng ối, '
    'dây rốn có thể quấn, thắt nút với nhau ngay từ 3 tháng đầu.'
)
for item in [
    'Tỷ lệ: 50-70% MCMA có dây rốn entanglement (PMID 33804073)',
    'Có thể phát hiện sớm từ 10-12 tuần bằng Doppler màu',
    'Khi một thai di động mạnh hơn → thắt chặt → mất tuần hoàn → thai chết',
    'Nguy cơ tử vong: có thể lên tới 50% nếu không theo dõi sát',
    'Yếu tố nguy cơ: tuổi thai càng lớn → nguy cơ càng cao do thai cử động nhiều',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('2. Twin-Twin Transfusion Syndrome (TTTS)', 2)
doc.add_paragraph(
    'MCMA có thể có TTTS "ngược chiều" hoặc không điển hình do 2 thai chia sẻ cả buồng ối:'
)
for item in [
    'Tỷ lệ: 10-15% MCMA có TTTS (thấp hơn MCDA 15-20% do chung nguồn ối)',
    'Đặc điểm: cả 2 thai đều có thể có đa ối hoặc thiểu ối (không rõ ràng như MCDA)',
    'Chẩn đoán Quintero thường không áp dụng được cho MCMA',
    'Cần dựa vào: chênh lệch cân nặng >20%, bàng quang thai nhỏ/mất bàng quang, Doppler bất thường',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Twin Anemia-Polycythemia Sequence (TAPS)', 2)
for item in [
    'Tỷ lệ: 5-10% MCMA (thấp hơn MCDA 13% sau laser)',
    'Cơ chế: thông mạch máu nhỏ ở bánh nhau → một thai thiếu máu, một thai đa hồng cầu',
    'Chẩn đoán: MCA-PSV > 1.5 MoM (thai đa hồng cầu), < 1.0 MoM (thai thiếu máu)',
    'Xử trí: laser, truyền máu trong tử cung, hoặc chấm dứt thai kỳ tùy mức độ',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Sẩy thai và thai chết lưu', 2)
for item in [
    'Sẩy thai tự nhiên: 10-20% MCMA (cao hơn MCDA)',
    'Thai chết lưu sau 24 tuần: 4-8% (cao gấp 10 lần đơn thai)',
    'Nguy cơ cao nhất ở tuần 20-32, đặc biệt do cord entanglement',
    'Tử vong chu sinh tổng thể: 11-30% (PMID 30125418)',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Sinh non', 2)
for item in [
    'Tuổi thai trung bình sinh: 32-34 tuần (PMID 37541734)',
    'Tỷ lệ sinh non < 32 tuần: 20-30%',
    'Tỷ lệ sinh non < 28 tuần: 5-10%',
    'Liên quan: đa ối, TTTS, nhiễm trùng, cắt đốt laser',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('6. Dị tật bẩm sinh', 2)
for item in [
    'Tỷ lệ dị tật: 15-25% (cao hơn MCDA 6-10%)',
    'Dị tật tim: 5-7% (gấp 5 lần đơn thai)',
    'Dị tật thận, hệ tiêu hóa, hệ thần kinh: tăng',
    'Cơ chế: do phôi phân chia muộn + chia sẻ nguồn máu không đều',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 4: THEO DÕI VÀ QUẢN LÝ', 1)

doc.add_heading('1. Lịch theo dõi siêu âm (theo SOGC 2023 + ISUOG 2023)', 2)

t2 = doc.add_table(rows=8, cols=3)
t2.style = 'Light Grid Accent 1'

headers2 = ['Tuổi thai', 'Tần suất', 'Mục đích']
rows2 = [
    ('10-14 tuần', '1 lần', 'Chẩn đoán MCMA, đánh giá NT, sàng lọc bất thường'),
    ('16-24 tuần', 'Mỗi 2 tuần', 'Theo dõi cord entanglement, phát hiện TTTS/TAPS sớm'),
    ('24-28 tuần', 'Mỗi 1-2 tuần', 'Đánh giá Doppler, MCA-PSV, cân nặng ước lượng'),
    ('28-32 tuần', 'Mỗi 1 tuần', 'Sát sao, chuẩn bị can thiệp'),
    ('32-34 tuần', 'Mỗi 1 tuần', 'Quyết định thời điểm mổ lấy thai'),
    ('Nhập viện', 'Tuần 26-28', 'Theo dõi sát, monitor tim thai liên tục'),
    ('Sinh', 'Tuần 32-34', 'Mổ lấy thai chủ động, không chờ chuyển dạ tự nhiên'),
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

doc.add_heading('2. Nội dung siêu âm mỗi lần khám', 2)
for item in [
    'Xác nhận cùng buồng ối (không có màng ngăn)',
    'Đo kích thước 2 thai: BPD, HC, AC, FL',
    'Cân nặng ước lượng: chênh lệch > 20% → nghi ngờ TAPS/TTTS',
    'Lượng nước ối: AFI hoặc khoang ối sâu nhất (DVP) mỗi thai',
    'Bàng quang thai: kích thước, có hay không',
    'Doppler ĐMP: PSV, chỉ số xung (PI), so sánh 2 thai',
    'Doppler MCA: PSV để chẩn đoán TAPS (PMID 37541734)',
    'Dây rốn: vị trí chèn, entanglement, nút thắt',
    'Tim thai: nhịp, có dấu hiệu suy tim?',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Theo dõi tim thai (CTG) trong nhập viện', 2)
for item in [
    'Monitor tim thai mỗi ngày 1-2 lần từ tuần 26-28',
    'Tìm dấu hiệu suy thai: nhịp chậm, giảm dao động, nhịp muộn',
    'Nếu có dấu hiệu bất thường → cân nhắc mổ cấp cứu',
    'Không cố gắng chờ chuyển dạ tự nhiên vì nguy cơ cord entanglement',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 5: XỬ TRÍ VÀ CAN THIỆP', 1)

doc.add_heading('1. Theo dõi thai kỳ', 2)
for item in [
    'Nhập viện từ tuần 26-28 (PMID 34563720 Delabaere 2022)',
    'Corticosteroid trưởng thành phổi: betamethasone 12mg x 2 liều, 24h trước sinh dự kiến',
    'Magnesium sulfate bảo vệ thần kinh: nếu sinh < 32 tuần',
    'Tocolysis: KHÔNG khuyến cáo thường quy vì không cải thiện kết cục',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('2. Thời điểm sinh', 2)
for item in [
    'PMID 37541734 (SOGC 2023): khuyến cáo mổ lấy thai tuần 32-34',
    'PMID 30125418 (D\'Antonio 2019): tỷ lệ sống cao nhất khi sinh tuần 33-34',
    'Mổ chủ động, KHÔNG chờ chuyển dạ tự nhiên',
    'Lý do: tránh cord entanglement cấp tính khi chuyển dạ → tử vong thai',
    'Cân nhắc cá nhân hóa: nếu có biến chứng (TTTS, TAPS, suy thai) → mổ sớm hơn',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Phương pháp sinh', 2)
for item in [
    'Mổ lấy thai là BẮT BUỘC (PMID 37541734)',
    'Lý do: tránh cord entanglement, tránh sa dây rốn',
    'Sinh thường qua âm đạo CHỐNG CHỈ ĐỊNH',
    'Tư thế mổ: tương tự mổ song thai khác, lưu ý vị trí 2 thai',
    'Có thể dùng kiểm soát tử cung bằng thuốc: oxytocin, methylergometrine',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('4. Vai trò của laser ablation trong MCMA', 2)
doc.add_paragraph(
    'Laser ablation (đốt laser thông mạch máu nhau thai) có vai trò HẠN CHẾ trong MCMA so với MCDA:'
)
for item in [
    'Chỉ định: TTTS hoặc TAPS giai đoạn nặng (Quintero ≥ 3, TAPS ≥ 2)',
    'Khó khăn: do 2 thai cùng buồng ối, màng ngăn không có → khó tiếp cận',
    'Hiệu quả: thấp hơn MCDA, tỷ lệ thai sống ~50-60% (vs 70-80% ở MCDA)',
    'Chống chỉ định tương đối: sa dây rốn, suy thai nặng',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('5. Vai trò của chấm dứt thai kỳ chọn lọc', 2)
for item in [
    'Chỉ định: 1 thai chết lưu, dị tật nặng không thể sống, TAPS nặng',
    'Phương pháp: bipolar cord occlusion hoặc radiofrequency ablation (RFA)',
    'Rủi ro: tổn thương thai còn lại 10-20% (do chia sẻ bánh nhau)',
    'Quyết định: hội chẩn đa chuyên khoa, tư vấn gia đình kỹ lưỡng',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 6: SẢN KHOA THỰC HÀNH', 1)

doc.add_heading('1. Khi phát hiện MCMA ở quý 1', 2)
for item in [
    'Thông báo cho gia đình về nguy cơ cao (tử vong chu sinh 11-30%)',
    'Tư vấn di truyền: cùng giới, cùng bộ gen',
    'Sàng lọc quý 1: NIPT, combined test',
    'Lên kế hoạch theo dõi sát từ tuần 16',
    'Chuyển đến trung tâm chuyên sâu về song thai + can thiệp bào thai',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('2. Vai trò của siêu âm viên trong MCMA', 2)
for item in [
    'Xác nhận chẩn đoán MCMA từ sớm (10-14 tuần)',
    'Theo dõi Doppler MCA-PSV mỗi 2 tuần để phát hiện TAPS',
    'Đo lượng nước ối từng thai, đánh giá chênh lệch',
    'Khảo sát cord entanglement, ghi nhận vị trí nút thắt',
    'Đánh giá tăng trưởng: chênh lệch cân nặng > 20% cảnh báo',
    'Phối hợp với bác sĩ sản khoa + bác sĩ can thiệp bào thai',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('3. Vai trò của bác sĩ sản khoa', 2)
for item in [
    'Quyết định thời điểm nhập viện (thường tuần 26-28)',
    'Quyết định thời điểm mổ lấy thai (32-34 tuần)',
    'Tư vấn corticosteroid trưởng thành phổi',
    'Phối hợp với NICU (đơn vị sơ sinh)',
    'Hội chẩn với bác sĩ can thiệp bào thai khi có biến chứng',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('PHẦN 7: SO SÁNH VỚI MCDA', 1)

t3 = doc.add_table(rows=10, cols=3)
t3.style = 'Light Grid Accent 1'

headers3 = ['Đặc điểm', 'MCDA', 'MCMA']
rows3 = [
    ('Bánh nhau', '1 bánh', '1 bánh'),
    ('Buồng ối', '2 buồng (có màng ngăn)', '1 buồng (không màng)'),
    ('Tỷ lệ', '~20% song thai tự nhiên', '~1% song thai tự nhiên'),
    ('Cord entanglement', 'Hiếm gặp', '50-70%'),
    ('TTTS', '15-20%', '10-15% (khó chẩn đoán hơn)'),
    ('TAPS', '13% (sau laser)', '5-10%'),
    ('Tử vong chu sinh', '2-5%', '11-30%'),
    ('Thời điểm sinh', '36-38 tuần', '32-34 tuần'),
    ('Phương pháp sinh', 'Có thể sinh thường (tùy vị trí)', 'Bắt buộc mổ lấy thai'),
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

doc.add_heading('ĐIỂM CẦN NHỚ', 1)
for item in [
    'MCMA: 1 bánh nhau, 1 buồng ối, không có màng ngăn - dạng song thai nguy cơ cao nhất',
    'Cơ chế: phôi phân chia ngày 8-13 (sau khi tạo túi ối)',
    'Tỷ lệ: 1/800-1/1000 thai kỳ, chiếm 1% song thai tự nhiên',
    'Biến chứng đặc trưng: cord entanglement 50-70%, tử vong chu sinh 11-30%',
    'Siêu âm chẩn đoán: tuần 8-14, thấy 1 bánh nhau, 1 buồng ối, không màng ngăn',
    'Theo dõi: siêu âm mỗi 2 tuần từ tuần 16, Doppler MCA-PSV phát hiện TAPS',
    'Nhập viện tuần 26-28, monitor tim thai mỗi ngày',
    'Mổ lấy thai chủ động tuần 32-34, KHÔNG chờ chuyển dạ tự nhiên',
    'PMID 30125418 (D\'Antonio 2019): meta-analysis trên >2900 thai MCMA',
    'PMID 37541734 (SOGC 2023): guideline quản lý song thai 1 bánh nhau',
]:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('TÀI LIỆU THAM KHẢO', 1)
for item in [
    'PMID 30125418 (D\'Antonio 2019, Ultrasound Obstet Gynecol): Perinatal mortality, timing of delivery and prenatal management of MCMA - meta-analysis',
    'PMID 37541734 (Lee HS 2023, J Obstet Gynaecol Can): SOGC Guideline No. 440 - Management of Monochorionic Twin Pregnancies',
    'PMID 34563720 (Delabaere 2022, J Gynecol Obstet Hum Reprod): Management of monoamniotic twin pregnancies: Where, when, how?',
    'PMID 33804073 (Panaitescu 2021, Diagnostics): Early Ultrasound Identification of Cord Entanglement in MCMA',
    'PMID 37087836 (Oliver 2023, Eur J Obstet Gynecol Reprod Biol): Comparison of international guidelines on twin pregnancy',
    'PMID 34101825 (Svelato 2021, Int J Gynaecol Obstet): Cord entanglement case report',
    'PMID 41810058 (Alagha 2026, Case Rep Obstet Gynecol): Severe cord entanglement case report',
]:
    doc.add_paragraph(item, style='List Bullet')

footer = doc.add_paragraph('— Hết bài học ngày 13/06/2026 —')
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer.runs[0].italic = True
footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)

doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {__import__('os').path.getsize(OUT)} bytes")