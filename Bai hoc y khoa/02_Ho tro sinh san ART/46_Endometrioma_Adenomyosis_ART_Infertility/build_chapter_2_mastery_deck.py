# -*- coding: utf-8 -*-
"""build_chapter_2_mastery_deck.py — Build Chapter 2 standalone master slide deck with pure unnumbered bullet points, integrating MUSA 2022 & IDEA 2016/2025."""
import json
import sys
from pathlib import Path

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\46_Endometrioma_Adenomyosis_ART_Infertility")
OUTPUTS_DIR = TARGET_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
sys.path.insert(0, str(SCRIPT_DIR))

import slider3636

# Clean footer override (no text, no page number, no divider line)
def clean_empty_footer(slide, left="", page_num=None, total=None):
    pass

slider3636.footer = clean_empty_footer

pure_bullet_chapter_2 = {
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
            "title": "CHƯƠNG 2: CHẨN ĐOÁN HÌNH ẢNH CHUYÊN SÂU",
            "subtitle": "Quy Trình IDEA 2016/2025, Tiêu Chuẩn MUSA 2022, Quy Tắc IOTA, Bản Đồ #Enzian & CHT MRI",
            "author": "Giáo Trình Master Chuyên Sâu — Phần 2",
            "specialty": "Hỗ Trợ Sinh Sản & Phụ Khoa",
            "date": "2026"
        },
        # Slide 2: Key Message
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "NGUYÊN TẮC HÌNH ẢNH HỌC TRONG ART",
            "message": "Chẩn Đoán Hình Ảnh Toàn Diện & Phân Tầng Chi Tiết\nLà Chìa Khóa Vàng Quyết Định Phác Đồ Can Thiệp Lâm Sàng"
        },
        # Slide 3: Objectives
        {
            "type": "objectives",
            "variant": "numbered_circles",
            "title": "Mục Tiêu Học Tập Chương 2",
            "objectives": [
                "Thành thạo quy trình siêu âm ngả âm đạo có hệ thống 4 bước theo đồng thuận quốc tế IDEA (2016) và cập nhật thể nông (2025).",
                "Nhận diện chính xác hình ảnh siêu âm OMA và áp dụng quy tắc IOTA loại trừ thoái hóa ác tính.",
                "Nắm vững 9 tiêu chuẩn siêu âm MUSA 2022: 4 dấu hiệu trực tiếp và 5 dấu hiệu gián tiếp chẩn đoán Adenomyosis.",
                "Sử dụng thành thạo bản đồ phân loại #Enzian và tiêu chuẩn CHT MRI đánh giá Vùng chuyển tiếp (JZ)."
            ]
        },
        # Slide 4: Tổng quan quy trình IDEA
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình Tiếp Cận Siêu Âm Ngả Âm Đạo Theo Đồng Thuận IDEA (4 Bước)",
            "points": [
                "Đồng thuận IDEA (International Deep Endometriosis Analysis group): Chuẩn hóa quy trình siêu âm ngả âm đạo động (dynamic TVS) có hệ thống.",
                "Mục đích: Giúp bác sĩ siêu âm khảo sát toàn diện từ cơ quan sinh dục đến khoang phúc mạc chậu, không bỏ sót tổn thương dính và lạc nội mạc sâu.",
                "Bước 1: Khảo sát tử cung (tìm 9 dấu hiệu Adenomyosis MUSA 2022/u xơ) và buồng trứng (đo thể tích, đếm AFC, tìm OMA).",
                "Bước 2: Tìm kiếm các dấu hiệu siêu âm mềm (độ di động buồng trứng, dấu hiệu buồng trứng dính nhau).",
                "Bước 3: Đánh giá túi cùng sau bằng Dấu hiệu Trượt (Sliding Sign).",
                "Bước 4: Khảo sát Lạc nội mạc tử cung sâu (DIE) ở khoang trước và khoang sau.",
                "Cập nhật 2025: Bổ sung quy trình khảo sát Lạc nội mạc phúc mạc nông (Superficial Endometriosis - SE)."
            ]
        },
        # Slide 5: IDEA Bước 1
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình IDEA — Bước 1: Khảo Sát Tử Cung & Buồng Trứng",
            "points": [
                "Khảo sát tử cung: Đo kích thước 3 chiều (chiều dài, chiều trước - sau, chiều ngang), đánh giá độ dày thành trước/thành sau.",
                "Đánh giá cơ tử cung: Tầm soát đầy đủ 9 dấu hiệu của Adenomyosis theo MUSA 2022, phân biệt với u xơ tử cung (FIGO).",
                "Khảo sát buồng trứng: Xác định vị trí 2 buồng trứng, đếm số nang thứ cấp (Antral Follicle Count - AFC).",
                "Đo lường khối u OMA: Khi phát hiện u lạc nội mạc buồng trứng, bắt buộc đo kích thước 3 chiều và thể tích u, khảo sát cả 2 bên buồng trứng."
            ]
        },
        # Slide 6: IDEA Bước 2
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình IDEA — Bước 2: Tìm Kiếm Các Dấu Hiệu Siêu Âm Mềm (Soft Markers)",
            "points": [
                "Độ di động buồng trứng: Dùng tay ấn nhẹ vùng hạ vị kết hợp đầu dò kiểm tra buồng trứng có trượt tự do trên thành chậu hay bị dính chặt vào hố buồng trứng.",
                "Dấu hiệu buồng trứng dính nhau ('Kissing Ovaries'): Cả 2 buồng trứng bị kéo dính sát vào nhau ở đường giữa phía sau tử cung.",
                "Ý nghĩa của 'Kissing Ovaries': Là chỉ điểm hình ảnh của tình trạng dính vùng chậu nặng nề, u OMA hai bên và lạc nội mạc ở ruột.",
                "Điểm đau khu trú tại chỗ (Site-specific tenderness): Nhận biết chính xác vị trí đau chói khi đầu dò chạm vào dây chằng tử cung - cùng hoặc túi cùng Douglas."
            ]
        },
        # Slide 7: IDEA Bước 3
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình IDEA — Bước 3: Đánh Giá Túi Cùng Sau Bằng Dấu Hiệu Trượt (Sliding Sign)",
            "points": [
                "Kỹ thuật thực hiện: Đầu dò đẩy nhẹ vào cổ tử cung và thành sau âm đạo trong khi tay kia ấn nhẹ trên thành bụng để quan sát sự trượt của trực tràng.",
                "Sliding Sign dương tính (+): Thành trước trực tràng trượt êm dịu trên thành sau cổ tử cung/âm đạo → Túi cùng Douglas hoàn toàn thông thoáng.",
                "Sliding Sign âm tính (-): Trực tràng dính chặt bất động vào mặt sau tử cung → Túi cùng Douglas bị bít tắc hoàn toàn (Obliterated pouch of Douglas).",
                "Bít tắc một phần (Partial obliteration): Vùng giữa vẫn trượt được nhưng thành bên (vùng dây chằng tử cung - cùng) bị dính bất động.",
                "Cảnh báo lâm sàng: Sliding Sign âm tính là dấu hiệu báo trước nguy cơ chọc hút noãn OPU hoặc phẫu thuật bóc tách cực kỳ phức tạp."
            ]
        },
        # Slide 8: IDEA Bước 4
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình IDEA — Bước 4: Khảo Sát Lạc Nội Mạc Tử Cung Sâu (DIE)",
            "points": [
                "Khoang trước: Khảo sát thành bàng quang, tam giác bàng quang và nếp gấp tử cung - bàng quang (tìm nốt thâm nhiễm giảm âm).",
                "Khoang sau — Dây chằng tử cung - cùng: Quan sát dải giảm âm dày không đều hoặc nốt đặc gồ ghề.",
                "Khoang sau — Vách trực tràng - âm đạo: Khảo sát khoang giữa thành sau âm đạo và thành trước trực tràng.",
                "Khoang sau — Ruột: Đánh giá thành cơ trực tràng và đại tràng sigma (tìm nốt hình nón/hình liềm giảm âm làm dày lớp cơ ruột)."
            ]
        },
        # Slide 9: IDEA Cập nhật 2025
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình IDEA Cập Nhật 2025 — Khảo Sát Lạc Nội Mạc Phúc Mạc Nông (SE)",
            "points": [
                "Phá bỏ quan niệm cũ: Trước đây mặc định Lạc nội mạc nông (Superficial Endometriosis - SE) chỉ chẩn đoán được qua mổ nội soi.",
                "Quy trình chuẩn hóa 2025: Nhận diện trực tiếp tổn thương SE trên siêu âm ngả âm đạo độ phân giải cao.",
                "Đặc điểm siêu âm của SE: Các dải màng mỏng tăng âm nhẹ hoặc vùng dày màng phúc mạc bất thường, nốt phẳng nhỏ < 5 mm bám trên phúc mạc.",
                "Vị trí ưu thế: Phúc mạc túi cùng Douglas, mặt sau dây chằng rộng, hố buồng trứng và nếp gấp tử cung - bàng quang.",
                "Kỹ thuật nhận diện: Tận dụng dịch sinh lý trong ổ bụng ở pha rụng trứng và kỹ thuật ấn chẩn (palpation TVS) tìm điểm đau khu trú."
            ]
        },
        # Slide 10: Đặc điểm OMA TVS
        {
            "type": "content",
            "variant": "bullets",
            "title": "U Lạc Nội Mạc Buồng Trứng (Endometrioma) — Đặc Điểm Siêu Âm Điển Hình",
            "points": [
                "Hình dạng & Thành nang: Khối dạng nang tròn hoặc bầu dục, bờ đều đặn, thành nang dày và tăng âm nhẹ.",
                "Hồi âm dạng 'Kính Mờ' (Ground-glass echogenicity): Cấu trúc hồi âm kém đồng nhất mịn màng tạo bởi hàng triệu hồng cầu thoái hóa và hemosiderin lơ lửng.",
                "Đặc điểm Doppler màu: Hoàn toàn không có tín hiệu mạch máu bên trong lòng nang (chỉ thấy viền mạch máu ngoại vi ở vỏ buồng trứng lành).",
                "Tính chất tồn tại: Tồn tại dai dẳng qua nhiều chu kỳ kinh nguyệt liên tiếp (khác nang hoàng thể tự biến mất)."
            ]
        },
        # Slide 11: Chẩn đoán phân biệt OMA
        {
            "type": "content",
            "variant": "bullets",
            "title": "U Lạc Nội Mạc Buồng Trứng — Chẩn Đoán Phân Biệt Trên Siêu Âm",
            "points": [
                "Nang hoàng thể xuất huyết: Có mạng lưới sợi fibrin dạng mạng nhện hoặc mạng lưới tổ ong và sẽ tự tiêu biến sau 1 - 2 chu kỳ kinh.",
                "U quái buồng trứng (Dermoid cyst / Teratoma): Chứa các dải tăng âm dạng vệt tóc (dermoid mesh) hoặc nốt tăng âm kèm bóng lưng cản âm mạnh (Rokitansky nodule).",
                "U nang thanh dịch buồng trứng: Lòng nang trống âm hoàn toàn (đen tuyền), thành mỏng nhẵn, dịch trong.",
                "Áp xe buồng trứng (Tubo-ovarian abscess): Nang chứa dịch đục lợn cợn không đồng nhất kèm vách dày tăng sinh mạch máu dữ dội và hội chứng nhiễm trùng trên lâm sàng."
            ]
        },
        # Slide 12: Quy tắc IOTA loại trừ ác tính
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Tắc IOTA (International Ovarian Tumor Analysis) — Loại Trừ Thoái Hóa Ác Tính",
            "points": [
                "Nguy cơ ung thư: U OMA có nguy cơ thoái hóa thành ung thư buồng trứng dạng nội mạc hoặc tế bào sáng (Endometrioid / Clear Cell Carcinoma).",
                "Dấu hiệu báo động 1 — Chồi nhú đặc (Papillary projections): Xuất hiện phần mô đặc dạng nhú nhô từ vách vào trong lòng nang.",
                "Dấu hiệu báo động 2 — Tăng sinh mạch máu Doppler: Tín hiệu mạch máu phong phú bên trong phần nhú đặc (Color Score 3 - 4).",
                "Dấu hiệu báo động 3 — Vách ngăn dày & Cổ trướng: Vách ngăn dày bất thường (> 3 mm), nhiều thùy hoặc có dịch tự do ổ bụng.",
                "Yếu tố nguy cơ cao: Bệnh nhân trên 40 tuổi hoặc khối u OMA tăng nhanh kích thước sau mãn kinh."
            ]
        },
        # Slide 13: Tổng quan tiêu chuẩn MUSA 2022
        {
            "type": "content",
            "variant": "bullets",
            "title": "Đồng Thuận Quốc Tế MUSA 2022 — Hệ Thống 9 Tiêu Chuẩn Siêu Âm Adenomyosis",
            "points": [
                "Đồng thuận MUSA 2022 (Harmsen et al., UOG 2022): Hoàn thiện chuẩn hóa 9 đặc điểm siêu âm phân định rõ ràng giữa Dấu hiệu trực tiếp và Dấu hiệu gián tiếp.",
                "Nhóm Dấu hiệu Trực tiếp (Direct Features): Gồm 4 đặc điểm phản ánh mô bệnh học tuyến nội mạc trong cơ, có giá trị khẳng định cao.",
                "Nhóm Dấu hiệu Gián tiếp (Indirect Features): Gồm 5 đặc điểm phản ánh phản ứng phì đại xơ hóa cơ tử cung và bất thường vùng chuyển tiếp JZ.",
                "Nâng cao độ chính xác: Giúp loại bỏ sự bất đồng giữa các bác sĩ siêu âm, chuẩn hóa quy trình đánh giá Adenomyosis trước ART."
            ]
        },
        # Slide 14: MUSA 2022 Dấu hiệu trực tiếp 1 & 2
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tiêu Chuẩn MUSA 2022 — Dấu Hiệu Trực Tiếp: Nang Cơ Tử Cung & Đảo Tăng Âm",
            "points": [
                "1. Nang cơ tử cung (Myometrial cysts): Các ổ trống âm hoặc giảm âm nhỏ 1 - 5 mm nằm trong lớp cơ tử cung, được bao bọc bởi một viền tăng âm mỏng (hyperechoic rim/halo).",
                "Bản chất của Nang cơ: Tuyến nội mạc đáy lạc vào cơ chảy máu chu kỳ tích tụ thành nang máu vi thể; viền tăng âm tương ứng lớp mô đệm nội mạc bao quanh.",
                "2. Đảo tăng âm (Hyperechoic islands): Các nốt/vùng tăng âm nhỏ nằm trong nhu mô cơ tử cung, không có bóng cản âm phía sau.",
                "Bản chất của Đảo tăng âm: Tương ứng với các đám mô đệm nội mạc tử cung (endometrial stroma) lạc chỗ tập trung thành cụm trong cơ."
            ]
        },
        # Slide 15: MUSA 2022 Dấu hiệu trực tiếp 3 & 4
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tiêu Chuẩn MUSA 2022 — Dấu Hiệu Trực Tiếp: Bóng Lưng Hình Quạt & Vệt/Chồi Dưới Niêm",
            "points": [
                "3. Bóng lưng hình quạt (Fan-shaped shadowing / Linear striations): Các dải bóng cản âm giảm âm hẹp, thẳng, chạy song song với nhau tỏa ra từ vùng cơ tử cung (dạng rèm sập hoặc nan quạt).",
                "Bản chất Bóng lưng hình quạt: Hình thành do sóng siêu âm bị tán xạ khi đi qua ranh giới giữa ổ tuyến mềm và bó cơ xơ hóa cứng bao quanh.",
                "4. Vệt tăng âm và Chồi dưới nội mạc (Subendometrial lines and buds): Các đường tăng âm mỏng hoặc chồi tăng âm hình bán cầu đâm vuông góc từ lớp nội mạc đáy qua ranh giới EMI vào lớp cơ dưới nội mạc (JZ).",
                "Bản chất Vệt/Chồi tăng âm: Phản ánh trực tiếp quá trình đâm chồi xâm lấn cơ của tuyến nội mạc đáy."
            ]
        },
        # Slide 16: MUSA 2022 Dấu hiệu gián tiếp 1, 2, 3
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tiêu Chuẩn MUSA 2022 — Dấu Hiệu Gián Tiếp: Thành Bất Đối Xứng, Hình Cầu & Mạch Máu Xuyên Cơ",
            "points": [
                "5. Thành cơ tử cung dày bất đối xứng (Asymmetrical thickening): Thành trước hoặc thành sau dày bất đối xứng rõ rệt (chênh lệch > 1.5 - 2 lần không do u xơ).",
                "6. Tử cung to hình cầu (Globular uterus): Tử cung mất dạng thon quả lê bình thường, trở nên tròn căng do tăng đường kính trước - sau.",
                "7. Mạch máu đâm xuyên tổn thương (Translesional vascularity): Trên Doppler màu, các nhánh mạch máu chạy thẳng góc đâm xuyên qua vùng tổn thương vào tận nội mạc.",
                "Ý nghĩa phân biệt với U xơ: U xơ tử cung có mạch máu chạy vòng bao quanh vỏ bao giả; Adenomyosis có mạch máu chạy đâm xuyên trực tiếp."
            ]
        },
        # Slide 17: MUSA 2022 Dấu hiệu gián tiếp 4 & 5 (JZ)
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tiêu Chuẩn MUSA 2022 — Dấu Hiệu Gián Tiếp: Bất Thường Vùng Chuyển Tiếp JZ",
            "points": [
                "8. Vùng chuyển tiếp không đều / đứt đoạn (Irregular / Disrupted JZ): Dải cơ trong dưới nội mạc mất tính liên tục, bờ nham nhở không đều, bề dày dao động mạnh.",
                "9. Vùng chuyển tiếp gián đoạn hoàn toàn (Interrupted JZ): Mất hoàn toàn hình ảnh dải giảm âm bình thường của JZ trên một đoạn hoặc toàn bộ chu vi buồng tử cung.",
                "Bản chất mô học: Do sự xâm lấn phá hủy ồ ạt của các tuyến nội mạc đáy xóa nhòa ranh giới giữa lớp cơ trong và lớp cơ ngoài.",
                "Vai trò của siêu âm 3D: Mặt cắt đứng ngang Coronal plane là phương tiện tối ưu để quan sát tính liên tục của JZ."
            ]
        },
        # Slide 18: Phân loại Adenomyosis MUSA 2022
        {
            "type": "content",
            "variant": "bullets",
            "title": "Khung Báo Cáo & Phân Loại Mức Độ Adenomyosis Theo MUSA 2022",
            "points": [
                "Vị trí tổn thương: Ghi nhận rõ thành trước, thành sau, vùng đáy, thành bên Trái / Phải.",
                "Hình thái lâm sàng: Phân biệt thể khu trú (Adenomyoma không có vỏ bao giả) vs thể lan tỏa (Diffuse Adenomyosis).",
                "Tầng lớp cơ thâm nhiễm: Cơ trong (Vùng chuyển tiếp JZ: 1/3 trong), Cơ giữa (1/3 giữa), Cơ ngoài (1/3 ngoài).",
                "Mức độ chiếm chỗ: Nhẹ (< 25% thể tích cơ tử cung), Vừa (25 - 50%), Nặng (> 50% thể tích cơ tử cung).",
                "Ý nghĩa ART: Thể lan tỏa nặng (> 50% cơ, thâm nhiễm cả 3 tầng) bắt buộc dùng phác đồ Ultra-long GnRHa 2-3 tháng."
            ]
        },
        # Slide 19: Tổng quan phân loại #Enzian
        {
            "type": "content",
            "variant": "bullets",
            "title": "Hệ Thống Phân Loại #Enzian Trên Siêu Âm (Cập Nhật 2021 - 2023)",
            "points": [
                "Mục đích: Chuẩn hóa việc lập bản đồ toàn diện Lạc nội mạc tử cung vùng chậu thống nhất giữa Siêu âm và Phẫu thuật nội soi.",
                "Khắc phục nhược điểm của rASRM: rASRM bỏ sót lạc nội mạc sâu và Adenomyosis; #Enzian mô tả chi tiết từng cơ quan giải phẫu.",
                "Nguyên tắc phân nhóm: Phân chia theo cơ quan: #Enzian O (buồng trứng), #Enzian T (dính vòi - buồng trứng), #Enzian U (cơ tử cung), #Enzian A, B, C (DIE khoang sau).",
                "Độ chính xác cao: Siêu âm ngả âm đạo theo #Enzian có độ nhạy > 90% tương đương phẫu thuật."
            ]
        },
        # Slide 20: #Enzian O & T
        {
            "type": "content",
            "variant": "bullets",
            "title": "Hệ Thống #Enzian — Phân Nhóm Buồng Trứng (#Enzian O) & Vòi Trứng (#Enzian T)",
            "points": [
                "#Enzian O (Ovary - Buồng trứng): Đánh giá u nang lạc nội mạc buồng trứng (O1 < 3 cm, O2 = 3 - 7 cm, O3 > 7 cm; kèm ký hiệu L/R cho Trái/Phải).",
                "#Enzian T (Tubo-ovarian - Dính vòi - buồng trứng): Đánh giá mức độ dính giải phẫu vùng chậu.",
                "Mức độ T1: Dính nhẹ giữa vòi tử cung và buồng trứng.",
                "Mức độ T2: Dính buồng trứng vào hố buồng trứng thành bên chậu.",
                "Mức độ T3: Dính nặng buồng trứng vào mặt sau tử cung hoặc dính 2 buồng trứng sát nhau ('Kissing Ovaries')."
            ]
        },
        # Slide 21: #Enzian U & DIE Khoang sau (A, B, C)
        {
            "type": "content",
            "variant": "bullets",
            "title": "Hệ Thống #Enzian — Lạc Nội Mạc Trong Cơ (#Enzian U) & Khoang Sau (A, B, C)",
            "points": [
                "#Enzian U (Uterus): Đánh giá mức độ tổn thương Adenomyosis trong cơ tử cung.",
                "Khoang A: Lạc nội mạc sâu ở âm đạo và vách trực tràng - âm đạo (A1 < 1 cm, A2 = 1 - 3 cm, A3 > 3 cm).",
                "Khoang B: Lạc nội mạc sâu ở dây chằng tử cung - cùng và thành bên chậu (B1 < 1 cm, B2 = 1 - 3 cm, B3 > 3 cm).",
                "Khoang C: Lạc nội mạc sâu ở trực tràng và đại tràng sigma (C1, C2, C3 theo mức độ xâm lấn chu vi và chiều dài đoạn ruột)."
            ]
        },
        # Slide 22: #Enzian Ý nghĩa an toàn OPU
        {
            "type": "content",
            "variant": "bullets",
            "title": "Hệ Thống #Enzian — Ý Nghĩa An Toàn Tuyệt Đối Trong Chọc Hút Noãn (OPU)",
            "points": [
                "Nhận diện 'Đáy chậu đóng băng' (Frozen Pelvis): Khi bệnh nhân có #Enzian B hoặc C nặng kết hợp T3, buồng trứng bị kéo dính chặt ra sau tử cung.",
                "Mối nguy trực tràng: Thành trước trực tràng bị kéo dính sát vào mặt sau buồng trứng và cổ tử cung.",
                "Nguyên tắc an toàn OPU: Bác sĩ chọc hút noãn bắt buộc phải quan sát rõ ranh giới lòng trực tràng trên siêu âm trước khi tiến kim.",
                "Phòng ngừa biến chứng: Tuyệt đối không đâm kim xuyên qua tổn thương khoang C vào ruột, phòng ngừa rò phân và viêm phúc mạc nhiễm trùng huyết."
            ]
        },
        # Slide 23: CHT MRI Vùng chậu & T2W
        {
            "type": "content",
            "variant": "bullets",
            "title": "Chụp Cộng Hưởng Từ (Pelvic MRI) — Ưu Thế & Hình Ảnh Vùng Chuyển Tiếp (JZ)",
            "points": [
                "Tiêu chuẩn vàng hình ảnh: MRI là phương tiện chính xác nhất khảo sát mô mềm vùng chậu, không phụ thuộc thành bụng dày hay kinh nghiệm người làm.",
                "Chuỗi xung Sagittal T2-weighted (T2W): Cho phép phân biệt rõ nét 3 tầng cấu trúc thành tử cung.",
                "Lớp nội mạc tử cung: Tăng tín hiệu sáng màu trắng trên T2W.",
                "Vùng chuyển tiếp (Junctional Zone - JZ): Dải giảm tín hiệu đồng nhất màu đen sẫm bao quanh nội mạc.",
                "Lớp cơ ngoài tử cung: Tín hiệu trung gian màu xám."
            ]
        },
        # Slide 24: CHT MRI Tiêu chuẩn đo JZ
        {
            "type": "content",
            "variant": "bullets",
            "title": "Chụp Cộng Hưởng Từ (MRI) — Tiêu Chuẩn Đo Lường & Ngưỡng Chẩn Đoán JZ",
            "points": [
                "JZ bình thường: Bề dày tối đa JZmax < 8 mm, ranh giới rõ ràng và đồng nhất.",
                "Vùng nghi ngờ: JZmax từ 8 đến 11 mm (cần kết hợp triệu chứng đau, tuổi và siêu âm MUSA).",
                "Chẩn đoán xác định Adenomyosis: JZmax ≥ 12 mm hoặc bề dày JZ chiếm > 40% tổng bề dày cơ tử cung.",
                "Tiêu chuẩn JZdiff: Độ chênh lệch JZdiff (JZmax - JZmin) ≥ 5 mm khẳng định tổn thương dày không đều.",
                "Dấu hiệu vi xuất huyết: Xuất hiện các đốm tăng tín hiệu nhỏ trên T2W bên trong dải đen JZ (tương ứng các ổ tuyến nội mạc chảy máu)."
            ]
        },
        # Slide 25: Siêu âm 3D ngả âm đạo (3D-TVS)
        {
            "type": "content",
            "variant": "bullets",
            "title": "Siêu Âm 3D Ngả Âm Đạo (3D-TVS) — Giá Trị Của Mặt Cắt Đứng Ngang (Coronal Plane)",
            "points": [
                "Mặt cắt đứng ngang (Coronal plane): Siêu âm 3D cho phép tái tạo mặt cắt đứng ngang buồng tử cung — mặt cắt không thể quan sát trên siêu âm 2D thông thường.",
                "Đánh giá ranh giới nội - cơ (EMI): Khảo sát độ sắc nét và tính liên tục của ranh giới giữa nội mạc đáy và lớp cơ JZ.",
                "Đo lường JZ đa vị trí: Cho phép đo chính xác độ dày JZ ở vùng đáy tử cung và 2 góc sừng tử cung.",
                "Phát hiện xâm lấn sớm: Nhận diện các chồi nội mạc đâm xuyên vào JZ trước khi tử cung bị biến dạng hình cầu."
            ]
        },
        # Slide 26: Summary Chương 2
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tóm Tắt Cốt Lõi Chương 2 (Thông Điệp Master)",
            "points": [
                "Quy trình IDEA 4 bước: Tiếp cận siêu âm động có hệ thống, đánh giá buồng trứng dính nhau, Dấu hiệu Trượt (Sliding Sign) và cập nhật thể nông SE (2025).",
                "Nhận diện OMA & IOTA: Hình ảnh 'kính mờ' không mạch máu; cảnh giác ác tính khi có phần nhú đặc tăng sinh mạch Color Score 3-4.",
                "Tiêu chuẩn MUSA 2022: 4 dấu hiệu trực tiếp (nang cơ có viền tăng âm, đảo tăng âm, bóng lưng hình quạt, vệt/chồi dưới niêm) và 5 dấu hiệu gián tiếp (thành bất đối xứng, hình cầu, mạch máu xuyên cơ, JZ không đều, JZ gián đoạn).",
                "Bản đồ #Enzian: Phân nhóm O, T, U, A, B, C giúp tiên lượng dính và đảm bảo an toàn tuyệt đối khi chọc hút noãn OPU.",
                "Tiêu chuẩn MRI & 3D TVS: Bề dày JZmax ≥ 12 mm và JZdiff ≥ 5 mm là tiêu chuẩn vàng chẩn đoán xác định Adenomyosis."
            ]
        },
        # Slide 27: References Chương 2
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tài Liệu Tham Khảo Y Học Chứng Cứ Của Chương 2",
            "points": [
                "Guerriero S, Condous G, et al. Systematic approach to sonographic evaluation of the pelvis in women with suspected endometriosis (IDEA consensus). Ultrasound Obstet Gynecol. 2016;48(3):318-332. PMID: 27328744.",
                "Guerriero S, Condous G, et al. Addendum to IDEA consensus: sonographic evaluation of superficial endometriosis. Ultrasound Obstet Gynecol. 2025. PMID: 40632542.",
                "Harmsen MJ, Van den Bosch T, et al. Consensus on revised definitions of MUSA features of adenomyosis: results of modified Delphi procedure. Ultrasound Obstet Gynecol. 2022;60(1):118-131. PMID: 34651347.",
                "Keckstein J, Hoopmann M, et al. Expert opinion on the use of transvaginal sonography for presurgical staging and classification of endometriosis (#Enzian). Arch Gynecol Obstet. 2023;307(1):5-19. PMID: 36367580.",
                "Timmerman D, Valentin L, et al. Terms, definitions and measurements to describe the sonographic features of adnexal tumors (IOTA). Ultrasound Obstet Gynecol. 2000;16(5):500-505. PMID: 11169340."
            ]
        }
    ]
}

deck_ch2_json = TARGET_DIR / "chapter_2_slider3636_deck.json"
deck_ch2_json.write_text(json.dumps(pure_bullet_chapter_2, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved updated Chapter 2 deck JSON ({len(pure_bullet_chapter_2['slides'])} slides): {deck_ch2_json}")

slider3636.set_theme("Medical Teal", "Segoe UI", "Standard — mặc định", show_pagenum=False)
out_pptx_ch2 = OUTPUTS_DIR / "Chuong_02_Chan_doan_hinh_anh_MUSA_2022_Mastery.pptx"
out_path, rendered = slider3636.build_presentation(pure_bullet_chapter_2, str(out_pptx_ch2))
print(f"\n🎉 Successfully compiled updated Chapter 2 Master Deck: {out_pptx_ch2} ({out_pptx_ch2.stat().st_size} bytes, {rendered} slides rendered)")
