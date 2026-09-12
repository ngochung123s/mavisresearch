# -*- coding: utf-8 -*-
"""build_comprehensive_master_deck.py — Build in-depth 34-slide Master PPTX Deck.
Includes full textbook-level detail, embedded authentic clinical images, and speaker notes.
"""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\46_Endometrioma_Adenomyosis_ART_Infertility")
REAL_IMG_DIR = TARGET_DIR / "figures" / "real_images"
OUT_PPTX = TARGET_DIR / "outputs" / "Endometrioma_Adenomyosis_ART_Comprehensive_Mastery.pptx"

prs = Presentation()
prs.slide_width = Inches(13.333)  # 16:9 Widescreen
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Color Palette
DARK_BG = RGBColor(0x0F, 0x17, 0x2A)       # Slate 900
PRIMARY_BLUE = RGBColor(0x02, 0x84, 0xC7)  # Sky 600
TITLE_COLOR = RGBColor(0x0F, 0x17, 0x2A)   # Slate 900
TEXT_MUTED = RGBColor(0x64, 0x74, 0x8B)    # Slate 500
TEXT_MAIN = RGBColor(0x33, 0x41, 0x55)     # Slate 700

# Theme Card Colors
BLUE_BG = RGBColor(0xEF, 0xF6, 0xFF)
BLUE_BORDER = RGBColor(0x93, 0xC5, 0xFD)
BLUE_TITLE = RGBColor(0x1D, 0x4E, 0xD8)

AMBER_BG = RGBColor(0xFF, 0xFB, 0xEB)
AMBER_BORDER = RGBColor(0xFD, 0xE6, 0x8A)
AMBER_TITLE = RGBColor(0xB4, 0x53, 0x09)

RED_BG = RGBColor(0xFE, 0xF2, 0xF2)
RED_BORDER = RGBColor(0xFC, 0xA5, 0xA5)
RED_TITLE = RGBColor(0xB9, 0x1C, 0x1C)

GREEN_BG = RGBColor(0xF0, 0xFD, 0xF4)
GREEN_BORDER = RGBColor(0x86, 0xEF, 0xAC)
GREEN_TITLE = RGBColor(0x15, 0x80, 0x3D)

PURPLE_BG = RGBColor(0xFA, 0xF5, 0xFF)
PURPLE_BORDER = RGBColor(0xD8, 0xB4, 0xFE)
PURPLE_TITLE = RGBColor(0x6B, 0x21, 0xA8)

def add_header(slide, title_text, category_text="HỖ TRỢ SINH SẢN & PHỤ KHOA LÂM SÀNG"):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = PRIMARY_BLUE
    
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.size = Pt(21)
    p_title.font.bold = True
    p_title.font.color.rgb = TITLE_COLOR

def add_card(slide, left, top, width, height, title, items, bg_color=BLUE_BG, border_color=BLUE_BORDER, title_color=BLUE_TITLE, body_size=11):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.22)
    tf.margin_right = Inches(0.22)
    tf.margin_top = Inches(0.20)
    tf.margin_bottom = Inches(0.20)
    
    p_title = tf.paragraphs[0]
    p_title.text = title
    p_title.font.size = Pt(13.5)
    p_title.font.bold = True
    p_title.font.color.rgb = title_color
    
    for item in items:
        p = tf.add_paragraph()
        p.text = item
        p.font.size = Pt(body_size)
        p.font.color.rgb = TEXT_MAIN
        p.space_before = Pt(4)

def add_speaker_note(slide, note_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = note_text

# ==============================================================================
# SLIDE 1: TITLE SLIDE
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = DARK_BG
bg1.line.fill.background()

tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.0))
tf1 = tb1.text_frame
tf1.word_wrap = True
p1_sub = tf1.paragraphs[0]
p1_sub.text = "GIÁO TRÌNH BÀI GIẢNG Y KHOA CHUYÊN SÂU (EBM MASTER DECK)"
p1_sub.font.size = Pt(13)
p1_sub.font.bold = True
p1_sub.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8)

p1_title = tf1.add_paragraph()
p1_title.text = "U Lạc Nội Mạc Buồng Trứng & Lạc Nội Mạc Tử Cung Trong Cơ\ntrong Vô Sinh và Hỗ Trợ Sinh Sản (ART)"
p1_title.font.size = Pt(28)
p1_title.font.bold = True
p1_title.font.color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
p1_title.space_before = Pt(12)

p1_desc = tf1.add_paragraph()
p1_desc.text = "Từ Cơ Chế Phân Tử, Hình Ảnh Siêu Âm MUSA / Phim MRI Thực Tế Đến Phác Đồ Can Thiệp Lâm Sàng Cá Thể Hóa"
p1_desc.font.size = Pt(15)
p1_desc.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)
p1_desc.space_before = Pt(14)

add_speaker_note(s1, "Mục tiêu: Đem lại góc nhìn toàn diện từ sinh học phân tử đến từng quyết định lâm sàng thực tế trong phòng khám và labo IVF.")

# ==============================================================================
# SLIDE 2: ROADMAP 6 CHƯƠNG
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Lộ Trình Bài Giảng: 6 Chương Học Toàn Diện")
add_card(s2, Inches(0.8), Inches(1.7), Inches(3.6), Inches(2.4),
         "Chương 1: Cơ Chế Bệnh Sinh",
         ["• Giải phẫu Vùng chuyển tiếp (JZ).", "• Cơ chế 'Toxic Follicular Milieu'.", "• Đề kháng Progesterone & Dysperistalsis."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s2, Inches(4.8), Inches(1.7), Inches(3.6), Inches(2.4),
         "Chương 2: Chẩn Đoán Hình Ảnh",
         ["• Tiêu chuẩn siêu âm MUSA.", "• Phân loại #Enzian trên TVS.", "• Đo độ dày JZ trên MRI & 3D TVS."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

add_card(s2, Inches(8.8), Inches(1.7), Inches(3.7), Inches(2.4),
         "Chương 3: Quản Lý Endometrioma",
         ["• Khuyến cáo ESHRE: Không mổ thường quy.", "• Bảo tồn sinh sản trước mổ.", "• Kỹ thuật tiêm xơ cồn EST & Laser."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s2, Inches(0.8), Inches(4.4), Inches(3.6), Inches(2.5),
         "Chương 4: Kích Thích Buồng Trứng",
         ["• Phác đồ GnRH Antagonist & PPOS.", "• Kích thích kép DuoStim cho DOR.", "• An toàn OPU & Xử trí chọc nhầm OMA."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

add_card(s2, Inches(4.8), Inches(4.4), Inches(3.6), Inches(2.5),
         "Chương 5: Chuẩn Bị Niêm Mạc FET",
         ["• Chiến lược Freeze-all phôi ngày 5.", "• Phác đồ Ultra-long GnRHa 2-3 tháng.", "• Đánh giá lại JZ & Tối ưu hoàng thể LPS."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

add_card(s2, Inches(8.8), Inches(4.4), Inches(3.7), Inches(2.5),
         "Chương 6: Quản Lý Sản Khoa",
         ["• Dự phòng Tiền sản giật (Aspirin tuần 12).", "• Tầm soát sinh non & Rau cài răng lược.", "• Cơ chế đờ tử cung & Băng huyết (PPH)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

# ==============================================================================
# SLIDE 3: CHƯƠNG 1 - DỊCH TỄ HỌC & TỶ LỆ ĐỒNG MẮC
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Dịch Tễ Học & Gánh Nặng Bệnh Lý Trong Hỗ Trợ Sinh Sản", "CHƯƠNG 1: ĐẠI CƯƠNG & CƠ CHẾ BỆNH SINH")
add_card(s3, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Tỷ Lệ Mắc & Tác Động Toàn Cầu",
         ["• Lạc nội mạc tử cung (Endometriosis): Xuất hiện ở 10% phụ nữ trong độ tuổi sinh sản và chiếm 30% - 50% phụ nữ vô sinh, hiếm muộn.",
          "• U lạc nội mạc buồng trứng (Endometrioma - OMA): Chiếm 17% - 44% bệnh nhân Lạc nội mạc tử cung. Thường là chỉ điểm của tổn thương vùng chậu nặng.",
          "• Lạc nội mạc tử cung trong cơ (Adenomyosis): Đồng mắc ở 30% - 40% bệnh nhân lạc nội mạc tử cung sâu (DIE) hoặc u buồng trứng.",
          "• 'Bộ đôi thách thức': Khi OMA và Adenomyosis cùng tồn tại, khả năng sinh sản bị tấn công kép: vừa suy giảm chất lượng/số lượng noãn, vừa hỏng cửa sổ làm tổ."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s3, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Sự Chuyển Dịch Quan Điểm Điều Trị (EBM Paradigm Shift)",
         ["• Quan điểm cũ (Ngoại khoa cổ điển): Thấy u nang buồng trứng là mổ bóc nang; chẩn đoán muộn Adenomyosis sau nhiều lần thất bại chuyển phôi.",
          "• Quan điểm Y học chứng cứ hiện đại (EBM 2022 - 2026):",
          "  1. Tuyệt đối tránh phẫu thuật bóc nang OMA không cần thiết nhằm bảo toàn dự trữ buồng trứng (AMH/AFC).",
          "  2. Tầm soát chủ động Adenomyosis bằng siêu âm TVS chuẩn MUSA trước khi lên kế hoạch chuyển phôi.",
          "  3. Ưu tiên bảo tồn sinh sản (Fertility Preservation) trữ đông giao tử/phôi từ sớm."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

# ==============================================================================
# SLIDE 4: CHƯƠNG 1 - PHÂN BIỆT 4 KHÁI NIỆM GIẢI PHẪU NỀN TẢNG
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Phân Biệt 4 Khái Niệm Bệnh Học Nền Tảng", "CHƯƠNG 1: ĐẠI CƯƠNG & CƠ CHẾ BỆNH SINH")
add_card(s4, Inches(0.8), Inches(1.7), Inches(5.6), Inches(2.5),
         "1. Nội Mạc Bình Thường (Eutopic Endometrium)",
         ["• Lớp lót trong lòng tử cung, chịu sự kích thích chu kỳ của Estrogen & Progesterone.",
          "• Gồm lớp chức năng (bong tróc tạo kinh) và lớp đáy (chứa tế bào gốc)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s4, Inches(6.8), Inches(1.7), Inches(5.7), Inches(2.5),
         "2. Lạc Nội Mạc Tử Cung (Endometriosis)",
         ["• Tuyến và mô đệm nội mạc xuất hiện bên ngoài buồng tử cung (phúc mạc, buồng trứng, vòi trứng, trực tràng).",
          "• Chảy máu chu kỳ gây viêm dính vùng chậu mạn tính."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

add_card(s4, Inches(0.8), Inches(4.4), Inches(5.6), Inches(2.5),
         "3. U Lạc Nội Mạc Buồng Trứng (Endometrioma - OMA)",
         ["• Nang hình thành do mô nội mạc lạc trong nhu mô buồng trứng chảy máu tích tụ lâu ngày.",
          "• Máu thoái hóa tạo dịch sô-cô-la sánh đặc, giàu sắt tự do và ROS."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s4, Inches(6.8), Inches(4.4), Inches(5.7), Inches(2.5),
         "4. Lạc Nội Mạc Trong Cơ (Adenomyosis)",
         ["• Tuyến và mô đệm lớp nội mạc đáy xâm lấn sâu vào trong lớp cơ tử cung (Myometrium).",
          "• Kèm theo sự phì đại và xơ hóa sợi cơ xung quanh, phá vỡ vùng chuyển tiếp JZ."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

# ==============================================================================
# SLIDE 5: CHƯƠNG 1 - VÙNG CHUYỂN TIẾP JZ & EMBED REAL MRI
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Vùng Chuyển Tiếp (Junctional Zone - JZ) & Đối Chiếu Phim MRI Thật", "CHƯƠNG 1: CƠ CHẾ BỆNH SINH HỌC")
add_card(s5, Inches(0.8), Inches(1.7), Inches(6.2), Inches(5.2),
         "Giải Phẫu & Ý Nghĩa Sinh Lý Bệnh Của JZ",
         ["• Nguồn gốc phôi thai: JZ (lớp cơ trong) có nguồn gốc từ ống Müller, khác với cơ ngoài nguồn gốc trung mô.",
          "• Sinh lý bình thường: Độ dày JZ < 8 mm. Co bóp nhẹ nhàng từ cổ tử cung lên đáy ở pha nang noãn để hút tinh trùng.",
          "• Bệnh lý Adenomyosis: JZ bị phá vỡ cấu trúc và phì đại dày bất thường (JZ >= 12 mm hoặc JZ_diff >= 5 mm trên MRI/3D TVS).",
          "• Hậu quả: Gây tăng nhu động tử cung bất thường (Dysperistalsis / Hyperperistalsis) tống phôi ra ngoài trước khi kịp làm tổ."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

mri_path = REAL_IMG_DIR / "real_mri_adenomyosis_thick_jz.jpg"
if mri_path.exists():
    s5.shapes.add_picture(str(mri_path), Inches(7.3), Inches(1.7), width=Inches(5.2))
    cap_box = s5.shapes.add_textbox(Inches(7.3), Inches(6.1), Inches(5.2), Inches(0.7))
    cap_tf = cap_box.text_frame
    cap_tf.word_wrap = True
    p_cap = cap_tf.paragraphs[0]
    p_cap.text = "📷 Phim MRI Sagittal T2W thật: Thành sau tử cung dày bất đối xứng, dải đen JZ dày vượt mốc 12 mm (JZmax ≈ 18 mm) chứa nhiều chấm tăng tín hiệu nhỏ."
    p_cap.font.size = Pt(10)
    p_cap.font.italic = True
    p_cap.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 6: CHƯƠNG 1 - OMA TOXIC MILIEU & EMBED REAL US
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Endometrioma: Vi Môi Trường Độc Hại & Hình Ảnh Siêu Âm 'Kính Mờ' Thật", "CHƯƠNG 1: CƠ CHẾ BỆNH SINH HỌC")
add_card(s6, Inches(0.8), Inches(1.7), Inches(6.2), Inches(5.2),
         "Dòng Thác Phản Ứng Fenton & Stress Oxy Hóa",
         ["• Dịch u sô-cô-la chứa nồng độ Sắt tự do (Fe2+) cực cao từ máu thoái hóa.",
          "• Phản ứng Fenton: Fe2+ phản ứng tạo ồ ạt các gốc oxy hóa tự do (ROS) và Cytokine viêm (TNF-alpha, IL-6, IL-8).",
          "• Tác động lên noãn: Gây đứt gãy thoi vô sắc, phân mảnh DNA giao tử, làm giảm chất lượng noãn và phôi.",
          "• Tác động lên vỏ buồng trứng: Viêm mạn tính gây xơ hóa mô vỏ (Cortical Fibrosis), làm tắc mạch máu nuôi dưỡng và kích hoạt cạn kiệt nang noãn nguyên thủy ('Burnout' effect).",
          "• Dẫn đến sụt giảm nhanh nồng độ AMH và số lượng nang thứ cấp AFC."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

us_oma = REAL_IMG_DIR / "real_us_endometrioma_ground_glass.jpg"
if us_oma.exists():
    s6.shapes.add_picture(str(us_oma), Inches(7.3), Inches(1.7), width=Inches(5.2))
    cap_box = s6.shapes.add_textbox(Inches(7.3), Inches(6.1), Inches(5.2), Inches(0.7))
    cap_tf = cap_box.text_frame
    cap_tf.word_wrap = True
    p_cap = cap_tf.paragraphs[0]
    p_cap.text = "📷 Siêu âm TVS thật: Khối u lạc nội mạc buồng trứng (OMA) kích thước lớn với hồi âm kém dạng 'kính mờ' (ground-glass) đồng nhất đặc trưng."
    p_cap.font.size = Pt(10)
    p_cap.font.italic = True
    p_cap.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 7: CHƯƠNG 1 - ADENOMYOSIS: ĐỀ KHÁNG PROGESTERONE & WOI
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Adenomyosis: Hiện Tượng Đề Kháng Progesterone & Hỏng Cửa Sổ Làm Tổ", "CHƯƠNG 1: CƠ CHẾ BỆNH SINH HỌC")
add_card(s7, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Cơ Chế Đề Kháng Progesterone (PR-B)",
         ["• Bình thường: Progesterone gắn thụ thể PR-B để chuyển nội mạc từ tăng sinh sang chế tiết và kích hoạt màng rụng hóa (Decidualization).",
          "• Trong Adenomyosis: Suy giảm nghiêm trọng thụ thể PR-B và tăng tỷ lệ thụ thể ức chế PR-A.",
          "• Hậu quả: Dù nồng độ Progesterone trong máu rất cao, nội mạc tử cung vẫn 'trơ' và không đáp ứng, làm hỏng quá trình màng rụng hóa.",
          "• Suy giảm các phân tử tiếp nhận then chốt của cửa sổ làm tổ (WOI): HOXA10, Leukemia Inhibitory Factor (LIF), và integrin alpha_v_beta_3."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s7, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Tăng Sinh Mạch, Aromatase & Thất Bại Làm Tổ (RIF)",
         ["• Biểu hiện quá mức enzyme Aromatase tại cơ tử cung (chuyển Androgen thành Estrogen tại chỗ).",
          "• Sản xuất thừa Prostaglandin E2 (PGE2) tạo vòng xoắn bệnh lý viêm mạn tính và kích thích u cơ tuyến phát triển.",
          "• Bằng chứng EBM (Cozzolino 2022 - PMID: 34981458):",
          "  - Giảm tỷ lệ thai lâm sàng: RR = 0.69 (95% CI: 0.59 - 0.81).",
          "  - Giảm tỷ lệ trẻ sinh sống: RR = 0.69 (95% CI: 0.51 - 0.94).",
          "  - Tăng nguy cơ sảy thai tự nhiên: RR = 2.17 (95% CI: 1.25 - 3.79)."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

# ==============================================================================
# SLIDE 8: CHƯƠNG 2 - TIÊU CHUẨN MUSA & EMBED REAL TVS
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Tiêu Chuẩn Siêu Âm MUSA: Dấu Hiệu 'Bóng Lưng Hình Quạt' Thật", "CHƯƠNG 2: CHẨN ĐOÁN HÌNH ẢNH NÂNG CAO")
add_card(s8, Inches(0.8), Inches(1.7), Inches(6.2), Inches(5.2),
         "Đồng Thuận Quốc Tế MUSA (2015 / 2026)",
         ["• 4 DẤU HIỆU TRỰC TIẾP (Khẳng định mô bệnh học):",
          "  1. Nang cơ tử cung (Myometrial cysts): Ổ trống âm 1-5 mm rải rác.",
          "  2. Đảo tăng âm (Hyperechoic islands): Nốt tăng âm từ mô đệm lạc chỗ.",
          "  3. Bóng lưng hình quạt (Fan-shaped shadowing / Linear striations): Dải cản âm song song tỏa ra từ cơ xơ hóa.",
          "  4. Vệt tăng âm dưới nội mạc (Subendometrial lines/buds).",
          "• 3 DẤU HIỆU GIÁN TIẾP (Gợi ý):",
          "  1. Thành cơ dày bất đối xứng (> 1.5 - 2 lần).",
          "  2. Tử cung to hình cầu (Globular uterus).",
          "  3. Mạch máu xuyên cơ (Translesional flow trên Doppler)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

us_adeno = REAL_IMG_DIR / "real_us_adenomyosis_linear_striations.jpg"
if us_adeno.exists():
    s8.shapes.add_picture(str(us_adeno), Inches(7.3), Inches(1.7), width=Inches(5.2))
    cap_box = s8.shapes.add_textbox(Inches(7.3), Inches(6.1), Inches(5.2), Inches(0.7))
    cap_tf = cap_box.text_frame
    cap_tf.word_wrap = True
    p_cap = cap_tf.paragraphs[0]
    p_cap.text = "📷 Siêu âm TVS thật: Lớp nội mạc tăng âm ở giữa tỏa ra các dải sọc tăng âm và bóng lưng hình quạt (linear striations) cắm sâu vào lớp cơ."
    p_cap.font.size = Pt(10)
    p_cap.font.italic = True
    p_cap.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 9: CHƯƠNG 2 - THỂ KHU TRÚ VS LAN TỎA & EMBED REAL CASE TVS
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Phân Biệt Thể Khu Trú vs Lan Tỏa & Ca Lâm Sàng Chuẩn Bị FET Thật", "CHƯƠNG 2: CHẨN ĐOÁN HÌNH ẢNH NÂNG CAO")
add_card(s9, Inches(0.8), Inches(1.7), Inches(6.2), Inches(5.2),
         "Phân Nhóm Lâm Sàng Quyết Định Phác Đồ ART",
         ["• Adenomyosis Khu Trú (Adenomyoma):",
          "  - Tổn thương tụ thành khối khu trú, có ranh giới tương đối nhưng không có vỏ bao giả (khác u xơ).",
          "  - Ảnh hưởng vừa phải đến làm tổ nếu nằm xa niêm mạc.",
          "• Adenomyosis Lan Tỏa (Diffuse Adenomyosis):",
          "  - Tổn thương lan rộng toàn bộ thành tử cung, làm biến dạng hoàn toàn tử cung thành hình cầu.",
          "  - Là nguyên nhân hàng đầu gây thất bại làm tổ tái phát (RIF) và sảy thai liên tiếp trong ART.",
          "  - Bắt buộc phải điều trị hạ điều hòa GnRHa kéo dài trước khi chuyển phôi."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

case_tvs = REAL_IMG_DIR / "real_fig_03_tvs_adenomyosis_case2.jpg"
if case_tvs.exists():
    s9.shapes.add_picture(str(case_tvs), Inches(7.3), Inches(1.7), width=Inches(5.2))
    cap_box = s9.shapes.add_textbox(Inches(7.3), Inches(6.1), Inches(5.2), Inches(0.7))
    cap_tf = cap_box.text_frame
    cap_tf.word_wrap = True
    p_cap = cap_tf.paragraphs[0]
    p_cap.text = "📷 Ca bệnh thật (JMCR 2026): TVS Adenomyosis lan tỏa chuẩn bị làm IVF: (A) Tử cung hình cầu, (B) Thành dày bất đối xứng và nang cơ tử cung."
    p_cap.font.size = Pt(10)
    p_cap.font.italic = True
    p_cap.font.color.rgb = TEXT_MUTED

# ==============================================================================
# SLIDE 10: CHƯƠNG 2 - BẢN ĐỒ LẠC NỘI MẠC TỬ CUNG SÂU #ENZIAN
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
add_header(s10, "Hệ Thống Phân Loại #Enzian Trên Siêu Âm & Ý Nghĩa Trước OPU", "CHƯƠNG 2: CHẨN ĐOÁN HÌNH ẢNH NÂNG CAO")
add_card(s10, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Cấu Trúc Bảng Phân Loại #Enzian (Keckstein 2023)",
         ["• #Enzian O: Lạc nội mạc buồng trứng (Ovary: O1 < 3cm, O2 = 3-7cm, O3 > 7cm).",
          "• #Enzian U: Lạc nội mạc cơ tử cung (Uterus / Adenomyosis).",
          "• #Enzian T: Dính vòi trứng - buồng trứng (Tubo-ovarian adhesions).",
          "• #Enzian A, B, C (Lạc nội mạc sâu DIE khoang sau):",
          "  - Khoang A: Âm đạo và vách trực tràng - âm đạo.",
          "  - Khoang B: Dây chằng tử cung - cùng và thành bên chậu.",
          "  - Khoang C: Trực tràng và đại tràng sigma."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

add_card(s10, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Ý Nghĩa Lâm Sàng Khi Chọc Hút Noãn (OPU)",
         ["• Bệnh nhân có #Enzian B hoặc C nặng (Frozen Pelvis - Đáy chậu đóng băng):",
          "  1. Buồng trứng thường bị kéo dính chặt vào mặt sau tử cung hoặc dính sát vào thành trực tràng.",
          "  2. Mất dấu hiệu trượt ('Sliding sign' âm tính) giữa tử cung và trực tràng.",
          "  3. Cảnh báo an toàn: Bác sĩ chọc hút noãn phải xác định cực kỳ rõ ranh giới trực tràng trên siêu âm để tránh đâm kim xuyên vào lòng ruột gây viêm phúc mạc / nhiễm trùng huyết."],
         RED_BG, RED_BORDER, RED_TITLE)

# ==============================================================================
# SLIDE 11: CHƯƠNG 3 - TẠI SAO ESHRE KHUYÊN KHÔNG MỔ OMA THƯỜNG QUY?
# ==============================================================================
s11 = prs.slides.add_slide(blank_layout)
add_header(s11, "Quản Lý Endometrioma: Tại Sao ESHRE Khuyên 'Không Mổ Thường Quy'?", "CHƯƠNG 3: QUẢN LÝ ENDOMETRIOMA TRƯỚC ART")
add_card(s11, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Bản Chất Kỹ Thuật Bóc Nang (Stripping Cystectomy)",
         ["• Vỏ nang OMA không có ranh giới tự nhiên rõ ràng với nhu mô buồng trứng lành.",
          "• Khi bóc tách vỏ nang (stripping), phẫu thuật viên vô tình tước đi một dải mô buồng trứng lành bám chặt theo vỏ u.",
          "• Mô bệnh học: Trong > 90% mảnh vỏ u bóc ra đều chứa các nang noãn nguyên thủy lành lặn.",
          "• Đốt điện cầm máu (Bipolar): Làm cháy và tắc nghẽn toàn bộ vi mạch rốn buồng trứng, khiến mô buồng trứng còn lại bị thiếu máu nuôi và teo xơ."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s11, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bằng Chứng Y Học Chứng Cứ (EBM Evidence)",
         ["• ESHRE Guideline 2022 (PMID: 35350465): Không phẫu thuật bóc OMA thường quy trước IVF chỉ nhằm mục đích tăng tỷ lệ thai.",
          "• Muzii et al. 2014 (PMID: 25085800): Phẫu thuật bóc nang làm giảm có ý nghĩa thống kê số nang AFC so với buồng trứng đối bên.",
          "• Riemma et al. 2026 (PMID: 41447907): Bóc OMA làm giảm AMH trung bình 0.57 ng/mL, giảm 1.24 noãn thu được mà KHÔNG làm tăng tỷ lệ sinh sống (LBR OR 0.89)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

# ==============================================================================
# SLIDE 12: CHƯƠNG 3 - CHỈ ĐỊNH MỔ & BẢO TỒN SINH SẢN
# ==============================================================================
s12 = prs.slides.add_slide(blank_layout)
add_header(s12, "Chỉ Định Mổ Chọn Lọc & Bảo Tồn Sinh Sản Trước Phẫu Thuật", "CHƯƠNG 3: QUẢN LÝ ENDOMETRIOMA TRƯỚC ART")
add_card(s12, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "4 Chỉ Định Phẫu Thuật Rõ Ràng",
         ["1. Cấp cứu ngoại khoa: Xoắn buồng trứng hoặc vỡ nang OMA gây viêm phúc mạc cấp tính.",
          "2. Nghi ngờ u ác tính: U có chồi sùi, tăng sinh mạch máu Doppler (IOTA score 3-4), tăng kích thước nhanh ở phụ nữ > 40 tuổi.",
          "3. Đau vùng chậu dữ dội kháng trị: Đau bụng kinh nặng, đau khi giao hợp sâu không đáp ứng thuốc nội khoa.",
          "4. Trở ngại cơ học cho OPU: U nang quá lớn (> 5-6 cm) che khuất toàn bộ buồng trứng làm không thể tiếp cận các nang noãn lành."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

add_card(s12, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bảo Tồn Sinh Sản (Fertility Preservation) - Clinical Pearl",
         ["• Nguyên tắc vàng: Ở bệnh nhân trẻ tuổi chưa có con, có u OMA 2 bên hoặc AMH đang suy giảm nhanh nhưng bắt buộc phải phẫu thuật:",
          "• BẮT BUỘC TƯ VẤN: Kích thích buồng trứng và Trữ đông noãn hoặc phôi TRƯỚC KHI bước vào phòng mổ.",
          "• Ý nghĩa: Đảm bảo người phụ nữ vẫn giữ được nguồn giao tử/phôi chất lượng cao ngay cả khi buồng trứng bị suy giảm chức năng sau phẫu thuật."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

# ==============================================================================
# SLIDE 13: CHƯƠNG 3 - KỸ THUẬT TIÊM XƠ BẰNG CỒN (EST) & LASER
# ==============================================================================
s13 = prs.slides.add_slide(blank_layout)
add_header(s13, "Kỹ Thuật Tiêm Xơ Cồn (EST) & Bốc Hơi Laser CO2 Bảo Tồn AMH", "CHƯƠNG 3: QUẢN LÝ ENDOMETRIOMA TRƯỚC ART")
add_card(s13, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Quy Trình 4 Bước Tiêm Xơ Cồn (EST)",
         ["1. Chọc hút sạch dịch: Hút triệt để toàn bộ dịch sô-cô-la qua ngả âm đạo dưới hướng dẫn siêu âm.",
          "2. Bơm rửa sạch lòng nang: Bơm rửa bằng nước muối sinh lý NaCl 0.9% 2-3 lần đến khi dịch trong.",
          "3. Bơm cồn 95-99%: Bơm cồn y tế (thể tích ~ 60-80% lượng dịch hút ra), ngâm lưu trong nang 10 - 15 phút.",
          "4. Hút cạn cồn: Hút sạch toàn bộ cồn ra ngoài, không để rò rỉ vào ổ bụng.",
          "• Cơ chế: Cồn làm đông vón protein và phá hủy tế bào nội mạc chế tiết mà không tước đi mô buồng trứng lành."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

add_card(s13, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bằng Chứng EBM Về Bảo Tồn AMH",
         ["• Bennet et al. 2026 (PMID: 42471696): Tiêm xơ cồn EST giúp bảo tồn nồng độ AMH tốt hơn rõ rệt và thu được số noãn cao hơn trong các chu kỳ IVF tiếp theo so với bóc nang.",
          "• Zhang et al. 2022 (PMID: 36334993): Bốc hơi lòng nang bằng Laser CO2 hoặc Plasma chỉ hủy lớp niêm mạc nông (1-2 mm), duy trì AMH sau mổ cao hơn nhiều so với bóc vỏ nang kết hợp đốt điện."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

# ==============================================================================
# SLIDE 14: CHƯƠNG 4 - PHÁC ĐỒ ANTAGONIST & PPOS
# ==============================================================================
s14 = prs.slides.add_slide(blank_layout)
add_header(s14, "Kích Thích Buồng Trứng: Phác Đồ Antagonist Linh Hoạt & PPOS", "CHƯƠNG 4: KÍCH THÍCH BUỒNG TRỨNG (COS)")
add_card(s14, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Phác Đồ GnRH Antagonist Linh Hoạt",
         ["• Bắt đầu tiêm Gonadotropin (phối hợp rFSH + hMG để bổ sung hoạt tính LH cho bệnh nhân LNMTC) từ ngày 2-3 chu kỳ.",
          "• Bắt đầu tiêm GnRH Antagonist (0.25 mg/ngày) khi nang vượt trội đạt >= 14 mm hoặc E2 > 500 pg/mL.",
          "• Trưởng thành noãn (Trigger) bằng GnRH Agonist (Triptorelin 0.2 mg) kết hợp Freeze-all để triệt tiêu hoàn toàn nguy cơ Quá kích buồng trứng (OHSS)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s14, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Phác Đồ PPOS (Progestin-Primed Ovarian Stimulation)",
         ["• Sử dụng Progestin đường uống (Medroxyprogesterone 10 mg/ngày hoặc Dydrogesterone 20 mg/ngày) ngay từ ngày đầu kích trứng cùng Gonadotropin.",
          "• Progestin ức chế hiệu quả đỉnh LH sớm mà không cần tiêm Antagonist.",
          "• Ưu điểm: Chi phí thấp, giảm số mũi tiêm, rất thuận tiện cho bệnh nhân Endometriosis gom noãn/phôi Freeze-all."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

# ==============================================================================
# SLIDE 15: CHƯƠNG 4 - PHÁC ĐỒ DUOSTIM CHO DOR
# ==============================================================================
s15 = prs.slides.add_slide(blank_layout)
add_header(s15, "Phác Đồ DuoStim: Gom Noãn Khẩn Cấp Cho Bệnh Nhân DOR", "CHƯƠNG 4: KÍCH THÍCH BUỒNG TRỨNG (COS)")
add_card(s15, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Lược Đồ 2 Đợt Kích Trứng Trong 1 Chu Kỳ",
         ["• Đợt 1 (Pha nang noãn - FPS): Kích trứng từ ngày 2-3 chu kỳ -> Trigger Agonist -> Chọc hút noãn đợt 1 (OPU-1).",
          "• Đợt 2 (Pha hoàng thể - LPS): Nghỉ 2-5 ngày sau OPU-1, bắt đầu kích trứng đợt 2 ngay trong pha hoàng thể -> Trigger -> Chọc hút noãn đợt 2 (OPU-2).",
          "• Toàn bộ noãn thu được thụ tinh ICSI, nuôi cấy phôi ngày 5 và Freeze-all."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

add_card(s15, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Giá Trị Cứu Cánh Lâm Sàng (Clinical Pearl)",
         ["• Rút ngắn thời gian gom noãn: Gom được số phôi mục tiêu chỉ trong 1 tháng thay vì 3-4 tháng.",
          "• 'Chạy đua với thời gian': Ngăn chặn nguy cơ bệnh LNMTC tiến triển nặng hơn hoặc buồng trứng cạn kiệt nang noãn trong thời gian chờ đợi.",
          "• Tối ưu cho phụ nữ lớn tuổi (>= 35 tuổi) hoặc có AMH thấp (< 1.2 ng/mL)."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

# ==============================================================================
# SLIDE 16: CHƯƠNG 4 - AN TOÀN OPU & XỬ TRÍ SỰ CỐ CHỌC NHẦM NANG OMA
# ==============================================================================
s16 = prs.slides.add_slide(blank_layout)
add_header(s16, "An Toàn Chọc Hút Noãn (OPU) & Kịch Bản Xử Trí Chọc Nhầm OMA", "CHƯƠNG 4: KÍCH THÍCH BUỒNG TRỨNG (COS)")
add_card(s16, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Nguyên Tắc An Toàn Thủ Thuật OPU",
         ["• Tuyệt đối tránh đâm kim xuyên qua nang u lạc nội mạc buồng trứng.",
          "• Khử khuẩn âm đạo bằng dung dịch Povidone-iodine pha loãng, sau đó BẮT BUỘC rửa sạch lại bằng nước muối sinh lý ấm (tránh độc noãn).",
          "• Sử dụng kháng sinh dự phòng tĩnh mạch phổ rộng (Ceftriaxone 1g + Metronidazole 500mg) ngay trước chọc hút để phòng ngừa áp xe buồng trứng."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s16, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Kịch Bản Xử Trí Khi Chọc Nhầm Vào OMA (Clinical Pearl)",
         ["• HÀNH ĐỘNG TỨC THÌ: KHÔNG ĐƯỢC hút dịch sô-cô-la lẫn vào ống nghiệm chứa dịch noãn.",
          "• Rút kim ra ngoài, thay kim mới hoặc súc rửa kỹ đầu kim bằng môi trường nuôi cấy.",
          "• Chuyển sang chọc các nang noãn lành ở buồng trứng đối diện trước.",
          "• Bơm rửa sạch túi cùng Douglas bằng nước muối sinh lý ấm sau OPU nếu có rò rỉ dịch u để phòng viêm phúc mạc."],
         RED_BG, RED_BORDER, RED_TITLE)

# ==============================================================================
# SLIDE 17: CHƯƠNG 5 - TẠI SAO BẮT BUỘC PHẢI FREEZE-ALL CHO ADENOMYOSIS?
# ==============================================================================
s17 = prs.slides.add_slide(blank_layout)
add_header(s17, "Tại Sao Bắt Buộc Phải Freeze-All Ở Bệnh Nhân Adenomyosis?", "CHƯƠNG 5: CHUẨN BỊ NIÊM MẠC & CHUYỂN PHÔI FET")
add_card(s17, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Tác Hại Của Môi Trường Kích Trứng Tươi",
         ["• Nồng độ Estradiol trong chu kỳ kích trứng tươi tăng vọt lên mức siêu sinh lý (> 3000 - 5000 pg/mL).",
          "• Estrogen cao kích thích trực tiếp thụ thể hormone trong cơ tử cung, làm bùng phát phản ứng viêm mạn tính.",
          "• Các ổ u cơ tuyến bị phù nề, tăng co bóp cơ tử cung dữ dội, phá hủy cửa sổ làm tổ.",
          "• Chuyển phôi tươi ở bệnh nhân Adenomyosis có tỷ lệ thất bại làm tổ và sảy thai rất cao."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s17, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bằng Chứng EBM Về Chiến Lược Freeze-All",
         ["• Han et al. 2025 (PMID: 40438397 - Phân tích gộp trên Front Endocrinol - phân nhóm Lạc nội mạc TC):",
          "  - Tăng tỷ lệ làm tổ: OR = 1.27 (95% CI: 1.05 - 1.54).",
          "  - Tăng tỷ lệ thai lâm sàng: OR = 1.25 (95% CI: 1.11 - 1.40).",
          "  - Tăng tỷ lệ trẻ sinh sống: OR = 1.31 (95% CI: 1.15 - 1.49).",
          "• Kết luận: Đông toàn bộ phôi nuôi ngày 5 và chuẩn bị niêm mạc chuyển phôi đông lạnh (FET) là lựa chọn chuẩn mực."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

# ==============================================================================
# SLIDE 18: CHƯƠNG 5 - PHÁC ĐỒ ULTRA-LONG GNRH AGONIST
# ==============================================================================
s18 = prs.slides.add_slide(blank_layout)
add_header(s18, "Phác Đồ Ultra-Long GnRH Agonist: Chỉ Định Chọn Lọc Cho Thể Lan Tỏa Nặng", "CHƯƠNG 5: CHUẨN BỊ NIÊM MẠC & CHUYỂN PHÔI FET")
add_card(s18, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Cơ Chế Phục Hồi Cửa Sổ Làm Tổ (WOI)",
         ["• Tiêm bắp GnRHa Depot 3.75 mg (Triptorelin/Leuprolide) từ 1-3 mũi cách nhau 28 ngày.",
          "• Đưa cơ thể về trạng thái mãn kinh tạm thời, cắt đứt nguồn cung Estrogen.",
          "• Tác dụng:",
          "  1. Thu nhỏ kích thước và thể tích khối u cơ tuyến.",
          "  2. Ức chế enzyme Aromatase và các cytokine gây viêm tại cơ tử cung.",
          "  3. Giảm co bóp cơ tử cung bất thường.",
          "  4. Tái thiết lập thụ thể PR-B, mở lại cửa sổ làm tổ (WOI)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s18, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bằng Chứng Hiệu Quả Lâm Sàng",
         ["• Latif et al. 2024 (PMID: 39116480 - Meta-analysis trên EJOGRB): Hạ điều hòa bằng GnRHa kéo dài trước chuyển phôi cải thiện đáng kể tỷ lệ làm tổ và tỷ lệ trẻ sinh sống ở bệnh nhân Adenomyosis.",
          "• González-Comadran et al. 2025 (PMID: 40674550): Phác đồ Ultra-long GnRHa làm tăng tỷ lệ thai lâm sàng với Cải thiện tỷ lệ làm tổ và thai lâm sàng (Latif 2024)."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

# ==============================================================================
# SLIDE 19: CHƯƠNG 5 - CÁ THỂ HÓA ĐIỀU TRỊ & ĐÁNH GIÁ LẠI JZ
# ==============================================================================
s19 = prs.slides.add_slide(blank_layout)
add_header(s19, "Cá Thể Hóa Chuẩn Bị Niêm Mạc & Bước Đánh Giá Lại JZ Bắt Buộc", "CHƯƠNG 5: CHUẨN BỊ NIÊM MẠC & CHUYỂN PHÔI FET")
add_card(s19, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Phân Tầng Nguy Cơ Cá Thể Hóa",
         ["• Thể nhẹ / Khu trú nhỏ (< 2 cm, JZ < 12 mm):",
          "  - Không nhất thiết phải tiêm GnRHa kéo dài 3 tháng.",
          "  - Chuẩn bị niêm mạc bằng HRT chuẩn hoặc chu kỳ tự nhiên cải biên kết hợp Letrozole.",
          "• Thể lan tỏa nặng (Tử cung to > 8 cm, JZ >= 12 mm):",
          "  - Bắt buộc áp dụng phác đồ Ultra-long GnRHa 2-3 tháng."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

add_card(s19, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Bước Đánh Giá Lại Tử Cung (Clinical Pearl)",
         ["• Sau 2-3 mũi GnRHa: BẮT BUỘC siêu âm ngả âm đạo đo lại thể tích tử cung và độ dày JZ.",
          "• Nếu tử cung co nhỏ tốt & JZ giảm rõ -> Tiến hành uống Estrogen (Progynova 4-6 mg/ngày).",
          "• Nếu tử cung vẫn to và phù nề -> Cân nhắc tiêm thêm mũi thứ 3 hoặc hội chẩn bổ trợ."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

# ==============================================================================
# SLIDE 20: CHƯƠNG 5 - TỐI ƯU HOÀNG THỂ (LPS) TRONG FET
# ==============================================================================
s20 = prs.slides.add_slide(blank_layout)
add_header(s20, "Tối Ưu Hóa Hỗ Trợ Hoàng Thể (LPS) & Mục Tiêu Progesterone", "CHƯƠNG 5: CHUẨN BỊ NIÊM MẠC & CHUYỂN PHÔI FET")
add_card(s20, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Chế Độ Bổ Sung Progesterone Mạnh Mẽ",
         ["• Do tình trạng đề kháng Progesterone nội tại, bệnh nhân Adenomyosis cần liều hoàng thể cao hơn bình thường.",
          "• Phối hợp đa đường dùng:",
          "  - Progesterone đặt âm đạo (Micro-progesterone 800 mg/ngày).",
          "  - KẾT HỢP Progesterone tiêm bắp (50 mg/ngày) hoặc tiêm dưới da (Prolutex 25 mg/ngày)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s20, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Mục Tiêu Nồng Độ Progesterone Huyết Thanh",
         ["• Định lượng Progesterone huyết thanh vào buổi sáng ngày chuyển phôi.",
          "• MỤC TIÊU: Nồng độ P4 huyết thanh phải đạt > 10 - 15 ng/mL.",
          "• Nếu P4 < 10 ng/mL: Cần tăng ngay liều Progesterone tiêm để cứu vãn chu kỳ chuyển phôi.",
          "• Thời điểm chuyển phôi: Sau đúng 120 giờ tiếp xúc Progesterone (đối với phôi nang ngày 5)."],
         GREEN_BG, GREEN_BORDER, GREEN_TITLE)

# ==============================================================================
# SLIDE 21: CHƯƠNG 6 - QUẢN LÝ THAI KỲ NGUY CƠ CAO (QUÝ 1 & QUÝ 2)
# ==============================================================================
s21 = prs.slides.add_slide(blank_layout)
add_header(s21, "Quản Lý Thai Kỳ Nguy Cơ Cao: Quý 1 & Quý 2", "CHƯƠNG 6: QUẢN LÝ BIẾN CHỨNG SẢN KHOA")
add_card(s21, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Quý 1 (Tuần 1 - 13): Phòng Ngừa Sảy Thai",
         ["• Nguy cơ sảy thai tự nhiên tăng gấp đôi (RR ≈ 2.17) do tăng co bóp cơ tử cung và môi trường viêm.",
          "• Duy trì hỗ trợ hoàng thể bằng Progesterone liên tục đến tuần thai thứ 10 - 12.",
          "• Dự phòng Tiền sản giật: Bắt đầu uống Aspirin liều thấp (100 - 150 mg/ngày) vào buổi tối từ tuần thai thứ 12."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

add_card(s21, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Quý 2 (Tuần 14 - 27): Tầm Soát Sinh Non",
         ["• Nguy cơ sinh non trước 37 tuần tăng 1.5 - 1.8 lần.",
          "• Siêu âm ngả âm đạo đo chiều dài kênh cổ tử cung (Cervical Length - CL) định kỳ mỗi 2 tuần từ tuần 16 đến 24.",
          "• Nếu CL < 25 mm: Can thiệp ngay bằng Progesterone đặt âm đạo, đặt vòng nâng pessary hoặc khâu vòng cổ tử cung."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

# ==============================================================================
# SLIDE 22: CHƯƠNG 6 - NGUY CƠ BĂNG HUYẾT SAU SINH (PPH) & VỠ TỬ CUNG
# ==============================================================================
s22 = prs.slides.add_slide(blank_layout)
add_header(s22, "Cơ Chế Băng Huyết Sau Sinh (PPH) & Cảnh Giác Vỡ Tử Cung", "CHƯƠNG 6: QUẢN LÝ BIẾN CHỨNG SẢN KHOA")
add_card(s22, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Cơ Chế Băng Huyết (PPH) Do Đờ Tử Cung",
         ["• Tuyến lạc chỗ tiết Prostaglandin và enzyme tiêu protein (MMPs) phá hủy mạng lưới collagen và sợi cơ trơn.",
          "• Cơ tử cung xơ hóa cứng đờ, mất hoàn toàn khả năng co rút sinh lý ('Living ligatures' - nút thắt sống) sau khi sổ rau.",
          "• Gruber et al. 2026 (PMID: 42453498): Tăng nguy cơ PPH rõ rệt.",
          "• Dự phòng: Chuẩn bị Oxytocin liều cao, Carbetocin, bóng chèn Bakri hoặc phẫu thuật thắt mạch."],
         RED_BG, RED_BORDER, RED_TITLE)

add_card(s22, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Cảnh Giác Nguy Cơ Vỡ Tử Cung",
         ["• Ở bệnh nhân có tiền sử phẫu thuật bóc u tuyến cơ tử cung (Adenomyomectomy):",
          "• Sẹo mổ ở cơ tử cung rất kém bền vững do mô cơ xung quanh bị xơ hóa không lành tốt.",
          "• Nguy cơ vỡ tử cung tự phát trong quý 3 hoặc khi bắt đầu chuyển dạ.",
          "• Chỉ định: Mổ lấy thai chủ động ở tuần 37-38, không thử thách sinh đường âm đạo."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

# ==============================================================================
# SLIDE 23: LƯỢNG GIÁ LÂM SÀNG - CASE 1 & CASE 2
# ==============================================================================
s23 = prs.slides.add_slide(blank_layout)
add_header(s23, "Lượng Giá Lâm Sàng (Self-Assessment MCQs) - Phần 1", "TỔNG KẾT & LƯỢNG GIÁ")
add_card(s23, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2),
         "Case 1: Xử Trí Endometrioma Trước IVF",
         ["Bệnh nhân nữ 29 tuổi, chưa có con, vô sinh 2 năm, AMH = 1.2 ng/mL. Siêu âm thấy u OMA phải 4 cm dạng kính mờ, không đau bụng, buồng trứng trái bình thường.",
          "👉 Chiến lược đúng đắn nhất:",
          "A. Mổ nội soi bóc u buồng trứng trước để tăng tỷ lệ thai.",
          "B. Tiến hành kích thích buồng trứng làm IVF trực tiếp, không mổ.",
          "C. Tiêm GnRHa 6 tháng cho u tiêu rồi mới làm IVF.",
          "✅ ĐÁP ÁN: B (Tránh suy buồng trứng sớm vì AMH thấp)."],
         BLUE_BG, BLUE_BORDER, BLUE_TITLE)

add_card(s23, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2),
         "Case 2: Dấu Hiệu Trực Tiếp MUSA",
         ["Dấu hiệu nào sau đây trên siêu âm ngả âm đạo được MUSA xếp vào nhóm 'Dấu hiệu trực tiếp' của Adenomyosis?",
          "A. Thành cơ tử cung dày bất đối xứng trước - sau.",
          "B. Tử cung to biến dạng hình cầu.",
          "C. Nang cơ tử cung (Myometrial cysts) & đảo tăng âm.",
          "D. Mạch máu đâm xuyên tổn thương trên Doppler.",
          "✅ ĐÁP ÁN: C (Phản ánh trực tiếp mô tuyến & xuất huyết trong cơ)."],
         AMBER_BG, AMBER_BORDER, AMBER_TITLE)

# ==============================================================================
# SLIDE 24: LƯỢNG GIÁ LÂM SÀNG - CASE 3
# ==============================================================================
s24 = prs.slides.add_slide(blank_layout)
add_header(s24, "Lượng Giá Lâm Sàng (Self-Assessment MCQs) - Phần 2", "TỔNG KẾT & LƯỢNG GIÁ")
add_card(s24, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.2),
         "Case 3: Lựa Chọn Phác Đồ Chuẩn Bị Niêm Mạc Cho Adenomyosis Nặng",
         ["Bệnh nhân 34 tuổi làm IVF có Adenomyosis thể lan tỏa nặng (tử cung to 9 cm, JZ = 14 mm trên MRI), đã có 4 phôi nang ngày 5 đông lạnh chất lượng tốt. Phác đồ chuẩn bị nội mạc tử cung chuyển phôi nào mang lại tỷ lệ thai lâm sàng và sinh sống cao nhất theo EBM?",
          "",
          "A. Chuyển phôi tươi ngay trong chu kỳ kích thích buồng trứng.",
          "B. Chuẩn bị nội mạc bằng chu kỳ tự nhiên không dùng thuốc.",
          "C. Chuẩn bị nội mạc bằng liệu pháp nội tiết thay thế (HRT) đơn thuần trong 14 ngày rồi chuyển phôi ngay.",
          "D. Hạ điều hòa tuyến yên bằng GnRH Agonist Depot 3.75 mg từ 2-3 tháng trước khi chuẩn bị nội mạc bằng HRT (Ultra-long protocol).",
          "",
          "✅ ĐÁP ÁN ĐÚNG: D",
          "💡 Giải thích chuyên môn: Phác đồ Ultra-long GnRHa 2-3 tháng giúp ức chế môi trường viêm, thu nhỏ thể tích cơ tử cung, giảm co thắt nghịch thường và đảo ngược tình trạng đề kháng Progesterone, tái mở cửa sổ làm tổ (WOI) cho thể lan tỏa nặng."],
         PURPLE_BG, PURPLE_BORDER, PURPLE_TITLE)

# ==============================================================================
# SLIDE 25: TỔNG KẾT BÀI GIẢNG - 5 NGUYÊN TẮC VÀNG
# ==============================================================================
s25 = prs.slides.add_slide(blank_layout)
add_header(s25, "Thông Điệp Thực Hành Lâm Sàng Cốt Lõi (Key Takeaways)", "TỔNG KẾT BÀI GIẢNG")
add_card(s25, Inches(0.8), Inches(1.7), Inches(11.7), Inches(5.2),
         "5 Nguyên Tắc 'Sống Còn' Dành Cho Bác Sĩ Thực Hành Lâm Sàng",
         ["1. KHÔNG MỔ BÓC NANG OMA THƯỜNG QUY: Chỉ mổ khi có chỉ định rõ ràng; luôn ưu tiên Bảo tồn sinh sản (Trữ đông noãn/phôi) TRƯỚC KHI mổ.",
          "2. AN TOÀN CHỌC HÚT NOÃN: Không đâm kim xuyên qua nang OMA; nếu vô tình chọc nhầm, lập tức ngừng hút, thay kim và rửa sạch túi cùng sau.",
          "3. TẬN DỤNG PHÁC ĐỒ DUOSTIM: Gom tối đa noãn/phôi trong 1 tháng cho bệnh nhân Endometriosis suy giảm dự trữ buồng trứng.",
          "4. CÁ THỂ HÓA ĐIỀU TRỊ ADENOMYOSIS: Freeze-all phôi ngày 5; áp dụng Ultra-long GnRHa 2-3 tháng cho thể lan tỏa nặng và bắt buộc siêu âm đánh giá lại JZ trước khi chuyển phôi.",
          "5. QUẢN LÝ SẢN KHOA CHỦ ĐỘNG: Dự phòng Tiền sản giật bằng Aspirin từ tuần 12, tầm soát sinh non và chủ động phòng ngừa Băng huyết sau sinh do đờ tử cung."],
         DARK_BG, PRIMARY_BLUE, RGBColor(0xF8, 0xFA, 0xFC))

prs.save(str(OUT_PPTX))
print(f"Master Deck successfully compiled: {OUT_PPTX} ({OUT_PPTX.stat().st_size} bytes, {len(prs.slides)} slides)")
