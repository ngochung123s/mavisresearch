# -*- coding: utf-8 -*-
"""build_clean_detailed_slider3636.py — Build 52 in-depth slides using slider3636 engine with NO footer, NO page numbers, and textbook-level detail."""
import json
import sys
from pathlib import Path

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\46_Endometrioma_Adenomyosis_ART_Infertility")
OUTPUTS_DIR = TARGET_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
sys.path.insert(0, str(SCRIPT_DIR))

import slider3636

# Override footer in slider3636 to be completely clean (no text, no divider line, no page numbers)
def clean_empty_footer(slide, left="", page_num=None, total=None):
    pass

slider3636.footer = clean_empty_footer

deck_data = {
    "meta": {
        "title": "",
        "subtitle": "",
        "author": ""
    },
    "slides": [
        # Slide 1: Title
        {
            "type": "title",
            "variant": "split_dark",
            "title": "U Lạc Nội Mạc Buồng Trứng & Lạc Nội Mạc Tử Cung Trong Cơ",
            "subtitle": "Tối Ưu Hóa Điều Trị Vô Sinh & Hỗ Trợ Sinh Sản (ART) Dựa Trên Y Học Chứng Cứ",
            "author": "Giáo Trình Lâm Sàng Chi Tiết Toàn Diện",
            "specialty": "Hỗ Trợ Sinh Sản & Phụ Khoa",
            "date": "2026"
        },
        # Slide 2: Key Message Paradigm Shift
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "SỰ CHUYỂN DỊCH QUAN ĐIỂM Y HỌC CHỨNG CỨ",
            "message": "Không Mổ Bóc U Buồng Trứng Thường Quy\nƯu Tiên Bảo Tồn Dự Trữ Noãn & Tái Mở Cửa Sổ Làm Tổ"
        },
        # Slide 3: Objectives
        {
            "type": "objectives",
            "variant": "numbered_circles",
            "title": "Mục Tiêu Học Tập & Chuẩn Đầu Ra Lâm Sàng",
            "objectives": [
                "Nắm vững cơ chế sinh bệnh học phân tử: stress oxy hóa OMA, tổn thương JZ và đề kháng Progesterone.",
                "Thành thạo chẩn đoán hình ảnh chuyên sâu: 4 dấu hiệu trực tiếp & 3 dấu hiệu gián tiếp MUSA, phân loại #Enzian.",
                "Áp dụng chính xác phác đồ can thiệp: kỹ thuật tiêm xơ cồn EST, kích trứng kép DuoStim và Ultra-long GnRHa.",
                "Chủ động nhận diện, dự phòng và xử trí các biến chứng sản khoa: tiền sản giật, đờ tử cung gây băng huyết (PPH)."
            ]
        },
        # Slide 4: Outline 6 Chapters
        {
            "type": "outline",
            "variant": "numbered",
            "title": "Nội Dung Bài Học: 6 Chương Toàn Diện",
            "chapters": [
                "Chương 1: Đại cương & Cơ chế bệnh sinh học phân tử",
                "Chương 2: Chẩn đoán hình ảnh nâng cao (MUSA, #Enzian, MRI)",
                "Chương 3: Chiến lược quản lý Endometrioma trước ART",
                "Chương 4: Kích thích buồng trứng & Kỹ thuật chọc hút noãn an toàn",
                "Chương 5: Chuẩn bị niêm mạc & Chuyển phôi đông lạnh (FET)",
                "Chương 6: Quản lý thai kỳ nguy cơ cao & Dự phòng biến chứng sản khoa"
            ]
        },

        # --- CHƯƠNG 1 ---
        # Slide 5: Section 1
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "01",
            "part_title": "Cơ Chế Bệnh Sinh Học Phân Tử",
            "part_subtitle": "Giải Phẫu JZ, Stress Oxy Hóa Dịch Nang & Đề Kháng Progesterone"
        },
        # Slide 6: Big Number Dịch tễ
        {
            "type": "big_number",
            "variant": "single_hero",
            "title": "Gánh Nặng Dịch Tễ Học Trong Vô Sinh",
            "stats": [
                {
                    "number": "30 - 50%",
                    "label": "Tỷ lệ phụ nữ vô sinh hiếm muộn mắc Lạc nội mạc tử cung",
                    "context": "Chiếm 10% phụ nữ trong độ tuổi sinh sản. Đồng mắc Adenomyosis ở 30-40% trường hợp."
                }
            ]
        },
        # Slide 7: Definition Eutopic vs Endometriosis
        {
            "type": "definition",
            "variant": "term_box",
            "title": "Định Nghĩa Bệnh Học Cơ Bản",
            "term": "Lạc Nội Mạc Tử Cung (Endometriosis)",
            "pronunciation": "en-doe-me-tree-O-sis",
            "definition": "Tình trạng các tuyến và mô đệm nội mạc tử cung xuất hiện và phát triển bên ngoài buồng tử cung (phúc mạc chậu, buồng trứng, vòi tử cung, bàng quang, trực tràng). Chảy máu chu kỳ gây phản ứng viêm mạn tính và xơ dính vùng chậu.",
            "note": "Khác với nội mạc bình thường (Eutopic endometrium) chỉ lót trong lòng tử cung."
        },
        # Slide 8: Definition OMA vs Adenomyosis
        {
            "type": "definition",
            "variant": "term_box",
            "title": "Định Nghĩa Thể Tổn Thương Đặc Thù",
            "term": "Endometrioma & Adenomyosis",
            "pronunciation": "En-do-me-tri-o-ma & Ad-e-no-my-o-sis",
            "definition": "Endometrioma (OMA) là khối u nang chứa máu thoái hóa màu sô-cô-la nằm trong nhu mô buồng trứng. Adenomyosis là tình trạng tuyến nội mạc đáy xâm lấn sâu vào lớp cơ tử cung kèm phì đại xơ hóa cơ trơn xung quanh.",
            "note": "Bộ đôi tổn thương tàn phá chức năng sinh sản kép: vừa giảm chất lượng noãn, vừa hỏng cửa sổ làm tổ."
        },
        # Slide 9: Two Column JZ Anatomy
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Giải Phẫu Thành Tử Cung & Vùng Chuyển Tiếp (JZ)",
            "left_title": "3 Lớp Cấu Trúc Thành Tử Cung",
            "left_points": [
                "Lớp cơ ngoài: Sợi cơ đan chéo, chức năng co hồi cầm máu sau sổ rau.",
                "Vùng chuyển tiếp (JZ): Lớp cơ trong bao quanh lòng tử cung, nguồn gốc ống Müller.",
                "Lớp nội mạc: Gồm lớp đáy sát JZ và lớp chức năng bong tróc tạo kinh."
            ],
            "right_title": "Ý Nghĩa Sinh Lý Bệnh Của JZ",
            "right_points": [
                "Sinh lý bình thường: Độ dày JZ < 8 mm, tạo sóng nhu động nhẹ hướng lên đáy hút tinh trùng.",
                "Bệnh lý Adenomyosis: JZ bị phá vỡ cấu trúc và dày bất thường (JZ >= 12 mm trên MRI).",
                "Hậu quả: Gây tăng co bóp nghịch thường (Dysperistalsis) tống phôi ra ngoài."
            ]
        },
        # Slide 10: Big Number JZ Thickness
        {
            "type": "big_number",
            "variant": "single_hero",
            "title": "Tiêu Chuẩn Vàng Bề Dày Vùng Chuyển Tiếp (JZ)",
            "stats": [
                {
                    "number": "≥ 12 mm",
                    "label": "Ngưỡng chẩn đoán xác định Adenomyosis trên MRI / 3D TVS",
                    "context": "Bình thường JZ < 8 mm. Mốc chênh lệch JZ_diff (JZmax - JZmin) >= 5 mm khẳng định tổn thương nặng."
                }
            ]
        },
        # Slide 11: Mechanism OMA Toxic Milieu
        {
            "type": "mechanism",
            "variant": "horizontal_steps",
            "title": "Cơ Chế Vi Môi Trường Dịch Nang Độc Hại của OMA",
            "steps": [
                {
                    "step": "1",
                    "title": "Tích Tụ Sắt Tự Do",
                    "text": "Dịch sô-cô-la chứa nồng độ Sắt tự do (Fe2+) cực cao từ máu thoái hóa chu kỳ."
                },
                {
                    "step": "2",
                    "title": "Phản Ứng Fenton",
                    "text": "Fe2+ xúc tác bùng phát các gốc oxy hóa tự do (ROS) và cytokine viêm (TNF-α, IL-6, IL-8)."
                },
                {
                    "step": "3",
                    "title": "Độc Tế Bào Noãn",
                    "text": "Gây đứt gãy thoi vô sắc, phân mảnh DNA giao tử và giảm tỷ lệ phát triển phôi nang."
                }
            ]
        },
        # Slide 12: Two Column Cortical Fibrosis
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Xơ Hóa Mô Vỏ & Cạn Kiệt Nang Noãn ('Burnout' Effect)",
            "left_title": "Xơ Hóa Nhu Mô Vỏ (Cortical Fibrosis)",
            "left_points": [
                "Viêm mạn tính kích thích nguyên bào sợi lắng đọng collagen quá mức quanh u OMA.",
                "Mô vỏ buồng trứng bị xơ cứng, làm tắc nghẽn các vi mạch nuôi dưỡng nang noãn nguyên thủy."
            ],
            "right_title": "Hiện Tượng Cạn Kiệt Nang Noãn ('Burnout')",
            "right_points": [
                "Môi trường viêm kích hoạt bất thường các nang noãn nguyên thủy thức giấc đồng loạt.",
                "Nang noãn sau đó thoái hóa hàng loạt làm suy giảm nhanh nồng độ AMH và số lượng nang AFC."
            ]
        },
        # Slide 13: Mechanism Adenomyosis Implantation Failure
        {
            "type": "mechanism",
            "variant": "horizontal_steps",
            "title": "Cơ Chế Thất Bại Làm Tổ Ở Bệnh Nhân Adenomyosis",
            "steps": [
                {
                    "step": "1",
                    "title": "Đề Kháng Progesterone",
                    "text": "Suy giảm thụ thể PR-B tại nội mạc làm gián đoạn quá trình màng rụng hóa (Decidualization)."
                },
                {
                    "step": "2",
                    "title": "Suy Giảm Yếu Tố Bám Dính",
                    "text": "Nội mạc giảm biểu hiện HOXA10, Leukemia Inhibitory Factor (LIF) và integrin αvβ3."
                },
                {
                    "step": "3",
                    "title": "Tăng Nhu Động Tử Cung",
                    "text": "Tử cung co bóp bất thường (Dysperistalsis) tống xuất phôi thai trước khi kịp bám dính."
                }
            ]
        },
        # Slide 14: Key Message Cozzolino 2022
        {
            "type": "key_message",
            "variant": "accent_band",
            "kicker": "BẰNG CHỨNG EBM (Cozzolino et al., 2022 - PMID: 34981458)",
            "message": "Adenomyosis Làm Giảm 31% Tỷ Lệ Trẻ Sinh Sống (LBR RR 0.69)\nVà Làm Tăng Gấp Đôi Nguy Cơ Sảy Thai Tự Nhiên (RR 2.17)"
        },

        # --- CHƯƠNG 2 ---
        # Slide 15: Section 2
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "02",
            "part_title": "Chẩn Đoán Hình Ảnh Nâng Cao",
            "part_subtitle": "Tiêu Chuẩn Siêu Âm MUSA, Phân Loại #Enzian & Đánh Giá MRI"
        },
        # Slide 16: Content OMA Ultrasound
        {
            "type": "content",
            "variant": "bullets",
            "title": "Đặc Điểm Siêu Âm Ngả Âm Đạo (TVS) Của Endometrioma",
            "points": [
                "Khối dạng nang tròn hoặc bầu dục, bờ đều đặn, thành nang dày.",
                "Cấu trúc hồi âm kém đồng nhất dạng 'kính mờ' (Ground-glass echogenicity) đặc trưng.",
                "Hoàn toàn không có tín hiệu mạch máu bên trong lòng nang trên Doppler màu.",
                "Cảnh giác ác tính theo quy chuẩn IOTA: Khối u có chồi sùi đặc, tăng sinh mạch máu Doppler score 3-4."
            ]
        },
        # Slide 17: Table MUSA Direct Signs
        {
            "type": "table",
            "variant": "standard",
            "title": "Đồng Thuận MUSA: 4 Dấu Hiệu Trực Tiếp Chẩn Đoán Adenomyosis",
            "headers": ["Dấu Hiệu Siêu Âm", "Hình Ảnh Đặc Trưng", "Bản Chất Mô Bệnh Học"],
            "rows": [
                ["1. Nang cơ tử cung", "Ổ trống âm nhỏ 1 - 5 mm trong cơ", "Tuyến nội mạc lạc chỗ chảy máu tích tụ"],
                ["2. Đảo tăng âm", "Nốt tăng âm nhỏ rải rác", "Mô đệm nội mạc lạc chỗ trong cơ"],
                ["3. Bóng lưng hình quạt", "Dải cản âm song song như nan quạt", "Phản ứng xơ hóa sợi cơ quanh tổn thương"],
                ["4. Vệt tăng âm dưới niêm", "Đường chồi gai đâm xuyên vào cơ", "Tuyến nội mạc đáy xâm lấn qua JZ"]
            ]
        },
        # Slide 18: Table MUSA Indirect Signs
        {
            "type": "table",
            "variant": "standard",
            "title": "Đồng Thuận MUSA: 3 Dấu Hiệu Gián Tiếp",
            "headers": ["Dấu Hiệu Siêu Âm", "Tiêu Chuẩn Đo Lường", "Phân Biệt Lâm Sàng"],
            "rows": [
                ["1. Thành dày bất đối xứng", "Thành trước/sau chênh lệch > 1.5-2 lần", "Gặp phổ biến ở thành sau tử cung"],
                ["2. Tử cung to hình cầu", "Tử cung mất dạng quả lê, tròn căng", "Tăng đường kính trước - sau"],
                ["3. Mạch máu xuyên cơ", "Doppler: Mạch máu chạy thẳng góc đâm xuyên", "Khác u xơ có mạch máu chạy vòng bao quanh"]
            ]
        },
        # Slide 19: Two Column Focal vs Diffuse
        {
            "type": "two_column",
            "variant": "vs_compare",
            "title": "Phân Biệt Adenomyosis Khu Trú vs Thể Lan Tỏa",
            "left_title": "Adenomyosis Khu Trú (Adenomyoma)",
            "left_points": [
                "Tổn thương tụ thành khối khu trú, có ranh giới tương đối.",
                "Không có vỏ bao giả như u xơ tử cung.",
                "Ảnh hưởng vừa phải đến làm tổ nếu nằm xa niêm mạc.",
                "Phác đồ FET: Có thể dùng HRT chuẩn hoặc Letrozole."
            ],
            "right_title": "Adenomyosis Lan Tỏa (Diffuse)",
            "right_points": [
                "Tổn thương lan rộng toàn bộ thành tử cung hình cầu.",
                "Phá hủy hoàn toàn cấu trúc Vùng chuyển tiếp (JZ).",
                "Nguyên nhân chính gây thất bại làm tổ tái phát (RIF).",
                "Phác đồ FET: Bắt buộc Ultra-long GnRHa 2-3 tháng."
            ]
        },
        # Slide 20: Three Column Enzian
        {
            "type": "three_column",
            "variant": "pillars",
            "title": "Hệ Thống Phân Loại #Enzian Trên Siêu Âm (Keckstein 2023)",
            "columns": [
                {
                    "title": "#Enzian O (Buồng trứng)",
                    "points": ["O1: U nang < 3 cm", "O2: U nang 3 - 7 cm", "O3: U nang > 7 cm"]
                },
                {
                    "title": "#Enzian U (Cơ tử cung)",
                    "points": ["U: Lạc nội mạc cơ tử cung", "Đánh giá mức độ lan tỏa", "Tương quan độ dày JZ"]
                },
                {
                    "title": "#Enzian A, B, C (DIE Khoang sau)",
                    "points": ["A: Âm đạo & vách trực tràng", "B: Dây chằng tử cung - cùng", "C: Trực tràng & đại tràng"]
                }
            ]
        },
        # Slide 21: Quote MRI Junctional Zone
        {
            "type": "quote",
            "variant": "guideline_box",
            "title": "Giá Trị Chẩn Đoán Của CHT Vùng Chậu (Pelvic MRI)",
            "quote": "Bề dày Vùng chuyển tiếp JZmax ≥ 12 mm trên chuỗi xung T2-weighted là tiêu chuẩn vàng chẩn đoán xác định Adenomyosis và phân tầng nguy cơ thất bại làm tổ trong hỗ trợ sinh sản.",
            "author": "Đồng thuận Hội Chẩn Đoán Hình Ảnh Phụ Khoa Quốc Tế",
            "source": "ISGE Recommendations & Human Reproduction"
        },

        # --- CHƯƠNG 3 ---
        # Slide 22: Section 3
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "03",
            "part_title": "Chiến Lược Quản Lý Endometrioma",
            "part_subtitle": "Hạn Chế Phẫu Thuật, Bảo Tồn Sinh Sản & Kỹ Thuật Tiêm Xơ EST"
        },
        # Slide 23: Evidence ESHRE Guideline 2022
        {
            "type": "evidence",
            "variant": "recommendation_box",
            "title": "Khuyến Cáo ESHRE 2022 Về Phẫu Thuật U Buồng Trứng",
            "items": [
                {
                    "recommendation": "Không khuyến cáo phẫu thuật bóc u lạc nội mạc buồng trứng thường quy trước khi thực hiện IVF/ICSI chỉ nhằm mục đích tăng tỷ lệ có thai, do phẫu thuật làm suy giảm dự trữ buồng trứng (giảm AMH/AFC).",
                    "class_rec": "Khuyến cáo mạnh (Strong recommendation)",
                    "level_ev": "Độ tin cậy vừa đến thấp (Moderate/Low certainty)",
                    "source": "ESHRE Endometriosis Guideline 2022 (PMID: 35350465)"
                }
            ]
        },
        # Slide 24: Two Column Stripping Damage
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Tại Sao Mổ Bóc Nang (Stripping) Làm Hại Dự Trữ Buồng Trứng?",
            "left_title": "Tước Mất Mô Buồng Trứng Lành",
            "left_points": [
                "Vỏ u OMA không có ranh giới tự nhiên rõ ràng với nhu mô lành.",
                "Khi bóc tách vỏ u (stripping), dải mô buồng trứng lành dính chặt theo vỏ nang bị tước đi.",
                "> 90% mảnh vỏ u bóc ra chứa nang noãn nguyên thủy lành lặn."
            ],
            "right_title": "Tổn Thương Mạch Máu Do Đốt Điện",
            "right_points": [
                "Cầm máu bằng dao đốt điện lưỡng cực (bipolar) phá hủy vi mạch rốn buồng trứng.",
                "Mô buồng trứng còn lại bị thiếu máu nuôi và teo xơ.",
                "Muzii / Riemma: Giảm AMH trung bình 0.57 ng/mL, giảm noãn thu được mà không tăng LBR."
            ]
        },
        # Slide 25: Content 4 Surgical Indications
        {
            "type": "content",
            "variant": "numbered",
            "title": "4 Chỉ Định Phẫu Thuật U Buồng Trứng Bắt Buộc",
            "points": [
                "Cấp cứu ngoại khoa: Xoắn buồng trứng hoặc vỡ nang OMA gây viêm phúc mạc cấp tính.",
                "Nghi ngờ ác tính: Khối u có chồi sùi, tăng sinh mạch máu Doppler (IOTA score 3-4), u tăng nhanh ở phụ nữ > 40 tuổi.",
                "Đau vùng chậu dữ dội kháng trị: Đau bụng kinh nặng, đau giao hợp sâu không đáp ứng nội khoa.",
                "Trở ngại cơ học cho chọc hút noãn: U nang quá lớn (> 5-6 cm) che khuất không thể tiếp cận các nang noãn lành."
            ]
        },
        # Slide 26: Key Message Fertility Preservation
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "CLINICAL PEARL - NGUYÊN TẮC BẢO TỒN SINH SẢN",
            "message": "Bắt Buộc Kích Trứng & Trữ Đông Noãn / Phôi\nTRƯỚC KHI Bắt Đầu Phẫu Thuật Bóc U Buồng Trứng"
        },
        # Slide 27: Algorithm Ethanol Sclerotherapy (EST)
        {
            "type": "algorithm",
            "variant": "linear_flow",
            "title": "Quy Trình 4 Bước Tiêm Xơ Bằng Cồn (EST)",
            "nodes": [
                {"text": "1. Chọc hút sạch triệt để dịch sô-cô-la trong u OMA dưới hướng dẫn siêu âm", "type": "start"},
                {"text": "2. Bơm rửa lòng nang bằng nước muối sinh lý NaCl 0.9% 2-3 lần đến khi dịch trong", "type": "process"},
                {"text": "3. Bơm cồn y tế 95-99% (thể tích 60-80% lượng hút ra), ngâm lưu 10-15 phút", "type": "decision"},
                {"text": "4. Hút cạn sạch toàn bộ lượng cồn ra ngoài, bảo tồn tối đa mô buồng trứng lành", "type": "end"}
            ]
        },
        # Slide 28: Two Column EST vs Cystectomy
        {
            "type": "two_column",
            "variant": "vs_compare",
            "title": "So Sánh Tiêm Xơ Cồn (EST) vs Phẫu Thuật Bóc Nang",
            "left_title": "Tiêm Xơ Bằng Cồn (EST)",
            "left_points": [
                "Bảo tồn nồng độ AMH sau thủ thuật vượt trội.",
                "Thu được số noãn cao hơn trong chu kỳ IVF tiếp theo.",
                "Không cần gây mê toàn thân, thực hiện ngả âm đạo.",
                "Bằng chứng Bennet 2026 (PMID: 42471696)."
            ],
            "right_title": "Phẫu Thuật Bóc Nang (Cystectomy)",
            "right_points": [
                "Sụt giảm AMH rõ rệt do mất mô lành và đốt điện.",
                "Giảm số noãn thu được khi làm IVF.",
                "Thời gian hồi phục lâu hơn, chi phí cao hơn.",
                "Không cải thiện tỷ lệ trẻ sinh sống (LBR OR 0.89)."
            ]
        },

        # --- CHƯƠNG 4 ---
        # Slide 29: Section 4
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "04",
            "part_title": "Kích Thích Buồng Trứng & An Toàn OPU",
            "part_subtitle": "Phác Đồ Antagonist, DuoStim & Kịch Bản Xử Trí Chọc Nhầm OMA"
        },
        # Slide 30: Two Column Antagonist vs PPOS
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Lựa Chọn Phác Đồ Kích Thích Buồng Trứng (COS)",
            "left_title": "Phác Đồ GnRH Antagonist Linh Hoạt",
            "left_points": [
                "Tiêm rFSH + hMG từ ngày 2-3 chu kỳ.",
                "Bắt đầu Antagonist (0.25 mg/ngày) khi nang >= 14 mm hoặc E2 > 500 pg/mL.",
                "Trigger bằng GnRH Agonist (Triptorelin 0.2 mg) + Freeze-all triệt tiêu OHSS."
            ],
            "right_title": "Phác Đồ PPOS (Progestin-Primed)",
            "right_points": [
                "Uống Medroxyprogesterone 10 mg/ngày hoặc Dydrogesterone 20 mg/ngày từ ngày đầu kích trứng.",
                "Ức chế đỉnh LH hiệu quả bằng đường uống, giảm số mũi tiêm.",
                "Chi phí thấp, tối ưu cho chu kỳ gom noãn/phôi Freeze-all."
            ]
        },
        # Slide 31: Timeline DuoStim
        {
            "type": "timeline",
            "variant": "horizontal_milestones",
            "title": "Phác Đồ DuoStim: Gom Noãn Khẩn Cấp Trong 1 Tháng Cho DOR",
            "events": [
                {"phase": "Đợt 1 (FPS)", "title": "Pha Nang Noãn", "text": "Kích trứng ngày 2 -> Trigger Agonist -> Chọc hút noãn OPU-1."},
                {"phase": "Nghỉ Ngắn", "title": "Giai Đoạn Nghỉ", "text": "Nghỉ 2 - 5 ngày sau OPU-1 để buồng trứng ổn định."},
                {"phase": "Đợt 2 (LPS)", "title": "Pha Hoàng Thể", "text": "Kích trứng đợt 2 trong pha hoàng thể -> Trigger -> Chọc hút noãn OPU-2."},
                {"phase": "Kết Cục", "title": "Freeze-All", "text": "Gom toàn bộ phôi ngày 5, rút ngắn thời gian gom noãn chỉ còn 1 tháng."}
            ]
        },
        # Slide 32: Three Column OPU Prep
        {
            "type": "three_column",
            "variant": "steps",
            "title": "3 Bước Chuẩn Bị & Khử Khuẩn Âm Đạo An Toàn Trước OPU",
            "columns": [
                {
                    "title": "1. Khử Khuẩn Âm Đạo",
                    "points": ["Sát trùng âm đạo bằng dung dịch Povidone-iodine pha loãng kỹ lưỡng."]
                },
                {
                    "title": "2. Rửa Sạch Bằng Nước Muối",
                    "points": ["BẮT BUỘC rửa sạch hoàn toàn Povidone bằng nước muối ấm (tránh độc noãn)."]
                },
                {
                    "title": "3. Kháng Sinh Dự Phòng",
                    "points": ["Tiêm Ceftriaxone 1g + Metronidazole 500mg ngừa áp xe buồng trứng."]
                }
            ]
        },
        # Slide 33: Two Column OMA Puncture Incident
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Kịch Bản Xử Trí Khi Vô Tình Chọc Nhầm Vào Nang OMA",
            "left_title": "Hành Động Tức Thì",
            "left_points": [
                "TUYỆT ĐỐI KHÔNG HÚT dịch sô-cô-la lẫn vào ống nghiệm chứa dịch noãn.",
                "Rút kim ra ngoài ngay lập tức.",
                "Thay kim chọc hút mới hoặc súc rửa kỹ bằng môi trường nuôi cấy."
            ],
            "right_title": "Xử Trí Tiếp Theo",
            "right_points": [
                "Chuyển sang chọc các nang noãn lành ở buồng trứng đối diện trước.",
                "Sau khi kết thúc OPU: Bơm rửa sạch túi cùng Douglas bằng nước muối sinh lý ấm.",
                "Duy trì kháng sinh dự phòng đầy đủ sau thủ thuật."
            ]
        },

        # --- CHƯƠNG 5 ---
        # Slide 34: Section 5
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "05",
            "part_title": "Chuẩn Bị Niêm Mạc & Chuyển Phôi FET",
            "part_subtitle": "Chiến Lược Freeze-All, Phác Đồ Ultra-Long GnRHa & Tối Ưu LPS"
        },
        # Slide 35: Key Message Why Freeze-all
        {
            "type": "key_message",
            "variant": "accent_band",
            "kicker": "NGUYÊN TẮC VÀNG TRONG ADENOMYOSIS",
            "message": "Bắt Buộc Đông Phôi Toàn Bộ (Freeze-All)\nTránh Nồng Độ Estrogen Siêu Sinh Lý Kích Hoạt Viêm Cơ Tử Cung"
        },
        # Slide 36: Mechanism Ultra-long Reversal
        {
            "type": "mechanism",
            "variant": "horizontal_steps",
            "title": "Cơ Chế Phục Hồi Cửa Sổ Làm Tổ Của Ultra-Long GnRHa",
            "steps": [
                {
                    "step": "1",
                    "title": "Cắt Nguồn Estrogen",
                    "text": "GnRHa Depot ức chế tuyến yên, đưa cơ thể về trạng thái mãn kinh tạm thời 2-3 tháng."
                },
                {
                    "step": "2",
                    "title": "Thu Nhỏ & Chống Viêm",
                    "text": "Thu nhỏ u cơ tuyến, ức chế enzyme Aromatase và giảm co thắt tử cung bất thường."
                },
                {
                    "step": "3",
                    "title": "Tái Lập Thụ Thể PR-B",
                    "text": "Khôi phục độ nhạy Progesterone, mở lại cửa sổ làm tổ (WOI) giúp phôi bám dính."
                }
            ]
        },
        # Slide 37: Timeline Ultra-long Protocol
        {
            "type": "timeline",
            "variant": "horizontal_milestones",
            "title": "Lược Đồ Phác Đồ Ultra-Long GnRH Agonist + HRT",
            "events": [
                {"phase": "Hạ Điều Hòa", "title": "GnRHa Depot", "text": "Tiêm GnRHa Depot 3.75mg (1-3 mũi cách nhau 28 ngày)."},
                {"phase": "Đánh Giá", "title": "Siêu Âm JZ", "text": "Siêu âm đo lại JZ và thể tích tử cung sau 2-3 tháng."},
                {"phase": "Tăng Sinh", "title": "Estrogen HRT", "text": "Uống Estradiol 4-6 mg/ngày đến khi niêm mạc >= 8mm 3 lá."},
                {"phase": "Chuyển Phôi", "title": "Progesterone", "text": "Bổ sung Progesterone và chuyển phôi sau đúng 120h P4."}
            ]
        },
        # Slide 38: QA Clinical Pearl Re-evaluate JZ
        {
            "type": "qa_clinical",
            "variant": "pearl_card",
            "title": "Clinical Pearl: Đánh Giá Lại Tử Cung Sau Hạ Điều Hòa",
            "pearl": "Sau 2-3 mũi GnRH Agonist, BẮT BUỘC phải siêu âm ngả âm đạo kiểm tra lại thể tích tử cung và độ dày JZ xem tổn thương đã thoái triển đạt chuẩn chưa trước khi quyết định bắt đầu uống Estrogen HRT."
        },
        # Slide 39: Two Column Individualized FET
        {
            "type": "two_column",
            "variant": "vs_compare",
            "title": "Cá Thể Hóa Chuẩn Bị Niêm Mạc Chuyển Phôi FET",
            "left_title": "Thể Nhẹ / Khu Trú (< 2 cm)",
            "left_points": [
                "Độ dày JZ < 12 mm, tử cung không to.",
                "Không nhất thiết tiêm GnRHa kéo dài 3 tháng.",
                "Chuẩn bị niêm mạc bằng HRT thông thường hoặc Letrozole.",
                "Rút ngắn thời gian và chi phí điều trị."
            ],
            "right_title": "Thể Lan Tỏa Nặng (JZ >= 12 mm)",
            "right_points": [
                "Tử cung to hình cầu > 8 cm.",
                "Cân nhắc áp dụng Ultra-long GnRHa 2-3 tháng sau tư vấn kỹ.",
                "Cải thiện tỷ lệ làm tổ (OR = 1.69) và thai lâm sàng (OR = 1.42 - Latif 2024).",
                "Đạt tỷ lệ trẻ sinh sống tối ưu."
            ]
        },
        # Slide 40: Medication LPS Target
        {
            "type": "medication",
            "variant": "quick_reference",
            "title": "Tối Ưu Hóa Hoàng Thể (LPS) & Mục Tiêu Progesterone Huyết Thanh",
            "drugs": [
                {
                    "name": "Micro-Progesterone Âm Đạo",
                    "dose": "800 mg/ngày (chia 2-4 lần)",
                    "route": "Đặt âm đạo",
                    "note": "Nồng độ tại mô nội mạc tử cung cao"
                },
                {
                    "name": "Progesterone Tiêm (Prolutex / Dầu)",
                    "dose": "25 mg SC hoặc 50 mg IM/ngày",
                    "route": "Tiêm dưới da / Tiêm bắp",
                    "note": "Bù đắp nồng độ Progesterone huyết thanh"
                }
            ]
        },

        # --- CHƯƠNG 6 ---
        # Slide 41: Section 6
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "06",
            "part_title": "Quản Lý Thai Kỳ & Biến Chứng Sản Khoa",
            "part_subtitle": "Dự Phòng Tiền Sản Giật, Tầm Soát Sinh Non & Cơ Chế PPH"
        },
        # Slide 42: Two Column Trimester 1 & 2
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Quản Lý Thai Kỳ Nguy Cơ Cao: Quý 1 & Quý 2",
            "left_title": "Quý 1 (Tuần 1 - 13): Phòng Sảy Thai",
            "left_points": [
                "Nguy cơ sảy thai tăng gấp đôi (RR ≈ 2.17) do co bóp và viêm cơ tử cung.",
                "Duy trì Progesterone hoàng thể liên tục đến tuần thai thứ 10 - 12.",
                "Khởi động Aspirin liều thấp (100-150 mg/ngày) từ tuần 12."
            ],
            "right_title": "Quý 2 (Tuần 14 - 27): Tầm Soát Sinh Non",
            "right_points": [
                "Nguy cơ sinh non trước 37 tuần tăng 1.5 - 1.8 lần.",
                "Đo chiều dài cổ tử cung (CL) qua siêu âm định kỳ mỗi 2 tuần từ tuần 16-24.",
                "Nếu CL < 25 mm: Đặt Progesterone, đặt vòng nâng hoặc khâu vòng CTC."
            ]
        },
        # Slide 43: Content Preeclampsia Prophylaxis
        {
            "type": "content",
            "variant": "numbered",
            "title": "Phác Đồ Dự Phòng Tiền Sản Giật & Bất Thường Bánh Rau",
            "points": [
                "Uống Aspirin liều thấp (100 - 150 mg/ngày) vào buổi tối trước khi đi ngủ từ tuần 12 đến tuần 36.",
                "Aspirin cải thiện quá trình tái cấu trúc động mạch xoắn bánh rau bị khiếm khuyết trong LNMTC.",
                "Khảo sát Doppler màu bánh rau định kỳ ở quý 2 và quý 3.",
                "Tầm soát sớm các dấu hiệu Rau tiền đạo và Rau cài răng lược (Placenta Accreta Spectrum - PAS)."
            ]
        },
        # Slide 44: Mechanism PPH Uterine Atony
        {
            "type": "mechanism",
            "variant": "horizontal_steps",
            "title": "Cơ Chế Băng Huyết Sau Sinh (PPH) Do Đờ Tử Cung ở Adenomyosis",
            "steps": [
                {
                    "step": "1",
                    "title": "Tiết Enzyme MMPs",
                    "text": "Mô tuyến lạc chỗ tiết ra enzyme tiêu protein (MMPs) phá hủy mạng lưới collagen cơ tử cung."
                },
                {
                    "step": "2",
                    "title": "Xơ Hóa & Thoái Hóa Cơ",
                    "text": "Sợi cơ trơn bị thoái hóa và xơ hóa cứng đờ, mất tính đàn hồi tự nhiên."
                },
                {
                    "step": "3",
                    "title": "Mất 'Nút Thắt Sống'",
                    "text": "Cơ tử cung mất hoàn toàn khả năng co rút thắt nút mạch máu sau sổ rau -> Băng huyết ồ ạt (PPH)."
                }
            ]
        },
        # Slide 45: Two Column Uterine Rupture
        {
            "type": "two_column",
            "variant": "cards",
            "title": "Cảnh Giác Nguy Cơ Vỡ Tử Cung & Chiến Lược Đỡ Đẻ",
            "left_title": "Nguy Cơ Vỡ Tử Cung",
            "left_points": [
                "Gặp ở bệnh nhân có tiền sử phẫu thuật bóc u tuyến cơ tử cung (Adenomyomectomy).",
                "Sẹo mổ ở cơ tử cung xơ hóa rất kém bền vững.",
                "Nguy cơ vỡ tử cung tự phát trong quý 3 hoặc khi chuyển dạ."
            ],
            "right_title": "Chiến Lược Đỡ Đẻ An Toàn",
            "right_points": [
                "Chỉ định mổ lấy thai chủ động ở tuần 37 - 38, không thử thách sinh đường âm đạo.",
                "Chủ động chuẩn bị thuốc tăng co tích cực (Oxytocin liều cao, Carbetocin, Misoprostol).",
                "Sẵn sàng bóng chèn Bakri và phương án thắt mạch tử cung."
            ]
        },

        # --- LƯỢNG GIÁ & TỔNG KẾT ---
        # Slide 46: Section 7
        {
            "type": "section",
            "variant": "number_block",
            "part_number": "07",
            "part_title": "Lượng Giá Lâm Sàng & Tổng Kết",
            "part_subtitle": "Case Study MCQs & 5 Thông Điệp Thực Hành Cốt Lõi"
        },
        # Slide 47: MCQ Case 1
        {
            "type": "qa_clinical",
            "variant": "mcq_5option",
            "title": "Lượng Giá Lâm Sàng: Case 1 - Xử Trí Endometrioma Trước IVF",
            "question": "Bệnh nhân nữ 29 tuổi, chưa có con, vô sinh 2 năm, AMH = 1.2 ng/mL. Siêu âm thấy u OMA phải 4 cm dạng kính mờ, không đau bụng, buồng trứng trái bình thường. Chiến lược điều trị nào sau đây đúng đắn nhất theo EBM?",
            "options": [
                "A. Phẫu thuật nội soi bóc u buồng trứng phải trước để làm tăng tỷ lệ thành công IVF",
                "B. Tiến hành kích thích buồng trứng làm IVF trực tiếp, không phẫu thuật bóc u trước",
                "C. Tiêm GnRH Agonist 6 tháng cho u nang tiêu hết rồi mới kích trứng làm IVF",
                "D. Phẫu thuật cắt buồng trứng phải để loại bỏ hoàn toàn ổ viêm",
                "E. Chọc hút nang đơn thuần không dùng cồn rồi chuyển phôi tươi"
            ],
            "answer": "B — Tiến hành kích thích buồng trứng làm IVF trực tiếp, không phẫu thuật bóc u trước",
            "show_answer": True,
            "why": "Theo ESHRE 2022 và các phân tích gộp, u OMA 4cm không triệu chứng không có chỉ định mổ trước IVF vì mổ bóc nang ở bệnh nhân có AMH thấp 1.2 ng/mL sẽ gây nguy cơ suy buồng trứng sớm mà không làm tăng tỷ lệ sinh sống."
        },
        # Slide 48: MCQ Case 2
        {
            "type": "qa_clinical",
            "variant": "mcq_5option",
            "title": "Lượng Giá Lâm Sàng: Case 2 - Phác Đồ Niêm Mạc Cho Adenomyosis Nặng",
            "question": "Bệnh nhân 34 tuổi làm IVF có Adenomyosis thể lan tỏa nặng (tử cung to 9 cm, JZ = 14 mm trên MRI), đã có 4 phôi nang ngày 5 đông lạnh chất lượng tốt. Phác đồ chuẩn bị nội mạc tử cung chuyển phôi nào mang lại tỷ lệ thai lâm sàng cao nhất?",
            "options": [
                "A. Chuyển phôi tươi ngay trong chu kỳ kích thích buồng trứng",
                "B. Chuẩn bị nội mạc bằng chu kỳ tự nhiên không dùng thuốc",
                "C. Chuẩn bị nội mạc bằng thuốc nội tiết thay thế (HRT) đơn thuần trong 14 ngày",
                "D. Hạ điều hòa tuyến yên bằng GnRH Agonist Depot 3.75 mg từ 2-3 tháng trước khi chuẩn bị nội mạc bằng HRT (Ultra-long protocol)",
                "E. Bơm huyết tương giàu tiểu cầu (PRP) buồng tử cung rồi chuyển phôi ngay"
            ],
            "answer": "D — Hạ điều hòa tuyến yên bằng GnRH Agonist Depot 3.75 mg từ 2-3 tháng trước khi chuẩn bị nội mạc bằng HRT (Ultra-long protocol)",
            "show_answer": True,
            "why": "Phác đồ Ultra-long GnRHa 2-3 tháng giúp ức chế môi trường viêm, thu nhỏ thể tích cơ tử cung, giảm co thắt nghịch thường và đảo ngược tình trạng đề kháng Progesterone, tái mở cửa sổ làm tổ (WOI) cho thể lan tỏa nặng."
        },
        # Slide 49: Summary Takeaways
        {
            "type": "summary",
            "variant": "dark_takeaways",
            "title": "5 Thông Điệp Thực Hành Lâm Sàng Cốt Lõi (Key Takeaways)",
            "points": [
                "1. KHÔNG MỔ BÓC NANG OMA THƯỜNG QUY: Luôn ưu tiên Bảo tồn sinh sản (Trữ đông noãn/phôi) TRƯỚC KHI mổ nếu bắt buộc phải can thiệp.",
                "2. AN TOÀN CHỌC HÚT NOÃN: Không đâm kim xuyên qua nang OMA; nếu chọc nhầm, lập tức ngừng hút, thay kim và rửa sạch túi cùng sau.",
                "3. TẬN DỤNG DUOSTIM: Gom tối đa số noãn/phôi trong 1 tháng cho bệnh nhân Endometriosis suy giảm dự trữ buồng trứng (DOR).",
                "4. CÁ THỂ HÓA ADENOMYOSIS: Freeze-all phôi ngày 5; Ultra-long GnRHa 2-3 tháng cho thể lan tỏa và bắt buộc siêu âm đánh giá lại JZ trước FET.",
                "5. QUẢN LÝ SẢN KHOA CHỦ ĐỘNG: Dự phòng Tiền sản giật bằng Aspirin từ tuần 12 và chủ động phòng ngừa Băng huyết sau sinh do đờ tử cung."
            ]
        },
        # Slide 50: References
        {
            "type": "references",
            "variant": "numbered",
            "title": "Tài Liệu Tham Khảo Y Học Chứng Cứ Nền Tảng (EBM)",
            "refs": [
                "Becker CM, Bokor A, et al. ESHRE guideline: endometriosis. Hum Reprod Open. 2022; PMID: 35350465.",
                "Muzii L, Di Tucci C, et al. Surgery for endometrioma on ovarian reserve AFC meta-analysis. Hum Reprod. 2014; PMID: 25085800.",
                "Zhang Y, Zhang S, et al. Cystectomy versus ablation for endometrioma on AMH. Fertil Steril. 2022; PMID: 36334993.",
                "Bennet SLM, Nagenthiran S, et al. Ethanol sclerotherapy versus cystectomy. BMC Womens Health. 2026; PMID: 42471696.",
                "Cozzolino M, Tartaglia S, et al. The Effect of Uterine Adenomyosis on IVF Outcomes. Reprod Sci. 2022; PMID: 34981458.",
                "Latif S, Kastora S, et al. Prolonged downregulation with GnRHa in adenomyosis. EJOGRB. 2024; PMID: 39116480.",
                "Van den Bosch T, Dueholm M, et al. MUSA consensus sonographic features. Ultrasound Obstet Gynecol. 2015; PMID: 25652685."
            ]
        }
    ]
}

deck_json_path = TARGET_DIR / "slider3636_deck.json"
deck_json_path.write_text(json.dumps(deck_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved deck JSON ({len(deck_data['slides'])} slides): {deck_json_path}")

slider3636.set_theme("Medical Teal", "Segoe UI", "Standard — mặc định", show_pagenum=False)
out_file = OUTPUTS_DIR / "Endometrioma_Adenomyosis_ART_Slider3636_Full_Mastery.pptx"
out_path, rendered = slider3636.build_presentation(deck_data, str(out_file))
print(f"\n🎉 Successfully rendered {rendered} slides via slider3636 engine with CLEAN FOOTER!")
print(f"Output PPTX: {out_file} ({out_file.stat().st_size} bytes)")
