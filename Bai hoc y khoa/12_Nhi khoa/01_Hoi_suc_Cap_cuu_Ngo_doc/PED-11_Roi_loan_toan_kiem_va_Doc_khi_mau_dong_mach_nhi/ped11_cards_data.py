# -*- coding: utf-8 -*-
"""PED-11 MASTER deck cards data: Track 1 barem YTB + Track 2 EBM.
Fields: id, track (barem_goc|ebm), type (basic|cloze), category, section,
front/back (basic) or text (cloze), extra, tags.
Section codes B0-B9 (PEDYTB) + E0-E10 (RELEASE lesson). Coverage gate requires >=1 card per section.
"""
cards_data = [
    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B0 MUC TIEU HOC TAP
    # =========================================================================
    {
        "id": "PED11-B01",
        "track": "barem_goc",
        "type": "basic",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "front": "6 mục tiêu học tập của bài Rối loạn toan kiềm & Đọc khí máu động mạch theo giáo trình Y Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Sinh lý 3 hàng rào; 2) Chỉ số ABG & AG; 3) 4 rối loạn toan kiềm nguyên phát; 4) Cơ chế toan trong mất nước; 5) Lưu đồ 5 bước đọc ABG; 6) Phác đồ bù NaHCO3 an toàn.<br><br><b>💡 Lưu ý:</b><br>Bám sát 6 mục tiêu này khi làm bài thi tự luận hồi sức cấp cứu.",
        "extra": "Văn bản gốc: MỤC TIÊU HỌC TẬP 1-6 (trang 1).",
        "tags": ["PED-11", "Barem-goc", "Muc-tieu"]
    },
    {
        "id": "PED11-B02",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "text": "[Barem gốc] Mục tiêu số 6 yêu cầu nắm vững: chỉ định, {{c1::công thức tính}} và các nguyên tắc {{c1::an toàn tuyệt đối}} khi bù Natri Bicarbonat (NaHCO3) trong cấp cứu hồi sức nhi.",
        "extra": "Văn bản gốc: Mục tiêu học tập số 6 (trang 1).",
        "tags": ["PED-11", "Barem-goc", "Muc-tieu"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B1 SINH LY TOAN KIEM & HENDERSON - HASSELBALCH
    # =========================================================================
    {
        "id": "PED11-B03",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Khái niệm pH",
        "section": "B1",
        "text": "[Barem gốc] Nồng độ ion H+ tự do trong máu bình thường được duy trì ở mức pH {{c1::7,35 - 7,45}}, tương đương nồng độ [H+] xấp xỉ {{c1::40 nmol/L}}.",
        "extra": "Văn bản gốc mục 1.1 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Henderson-Hasselbalch"]
    },
    {
        "id": "PED11-B04",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Phương trình Henderson",
        "section": "B1",
        "text": "[Barem gốc] Phương trình Henderson - Hasselbalch mô tả thăng bằng toan kiềm: pH = {{c1::6,1 + log([HCO3-] / [0,03 × PaCO2])}}.",
        "extra": "Văn bản gốc mục 1.1 (trang 2): 6,1 là hằng số pKa của acid carbonic.",
        "tags": ["PED-11", "Barem-goc", "Henderson-Hasselbalch"]
    },
    {
        "id": "PED11-B05",
        "track": "barem_goc",
        "type": "basic",
        "category": "Phương trình Henderson",
        "section": "B1",
        "front": "Trong phương trình Henderson - Hasselbalch, tử số và mẫu số đại diện cho thành phần nào và cơ quan nào điều hòa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tử số [HCO3-] đại diện cho thành phần chuyển hóa do Thận điều hòa; mẫu số PaCO2 đại diện cho thành phần hô hấp do Phổi điều hòa.<br><br><b>💡 Lưu ý:</b><br>Nồng độ chuẩn của HCO3- ngoại bào là 26 mEq/L, PaCO2 chuẩn là 40 mmHg.",
        "extra": "Văn bản gốc mục 1.1 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Henderson-Hasselbalch"]
    },
    {
        "id": "PED11-B06",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Giá trị chuẩn",
        "section": "B1",
        "text": "[Barem gốc] Nồng độ chuẩn của HCO3- theo phương trình giáo trình là {{c1::22 - 26 mEq/L}} (chuẩn 26 mEq/L) và áp lực riêng phần PaCO2 là {{c1::35 - 45 mmHg}}.",
        "extra": "Văn bản gốc mục 1.1 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Henderson-Hasselbalch"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B2 BA HANG RAO BAO VE
    # =========================================================================
    {
        "id": "PED11-B07",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hàng rào đệm",
        "section": "B2",
        "text": "[Barem gốc] Hàng rào 1 (hệ thống đệm hóa học) có thời gian tác dụng {{c1::tức thì trong vài giây}}; hệ đệm ngoại bào quan trọng nhất là {{c1::Bicarbonat / Acid carbonic (HCO3- / H2CO3)}}.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem"]
    },
    {
        "id": "PED11-B08",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hàng rào đệm",
        "section": "B2",
        "text": "[Barem gốc] Nồng độ HCO3- trong dịch ngoại bào là {{c1::26 mEq/L}}, trong khi nồng độ HCO3- trong nội bào chỉ là {{c1::10 mEq/L}}.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem"]
    },
    {
        "id": "PED11-B09",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hàng rào đệm",
        "section": "B2",
        "front": "Các hệ đệm nội bào và hồng cầu quan trọng trong hàng rào 1 theo giáo trình gồm những hệ đệm nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hemoglobin (Hb), protein huyết tương và phosphat nội bào (HPO4(2-) / H2PO4(-)).<br><br><b>💡 Cơ chế:</b><br>Hemoglobin đệm ion H+ khi nhả oxy ở mô; phosphat đóng vai trò quan trọng trong đệm nội bào và dịch ống thận.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem"]
    },
    {
        "id": "PED11-B10",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hàng rào phổi",
        "section": "B2",
        "text": "[Barem gốc] Hàng rào 2 (phổi) phản ứng trong {{c1::vài phút đến vài giờ}}; khi toan hóa máu kích thích trung tâm hô hấp tại hành não làm trẻ {{c1::thở nhanh sâu (thở Kussmaul)}} để tăng đào thải CO2.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem"]
    },
    {
        "id": "PED11-B11",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hàng rào thận",
        "section": "B2",
        "text": "[Barem gốc] Hàng rào 3 (thận) phản ứng chậm trong {{c1::24 - 72 giờ}}, thực hiện 3 cơ chế: tái hấp thu {{c1::gần 100%}} HCO3- tại ống lượn gần, bài tiết H+ dưới dạng acid chuẩn độ/amoni, và tân tạo HCO3- mới.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem"]
    },
    {
        "id": "PED11-B12",
        "track": "barem_goc",
        "type": "basic",
        "category": "Đặc điểm trẻ nhỏ",
        "section": "B2",
        "front": "Vì sao trẻ sơ sinh và nhũ nhi rất dễ bị toan chuyển hóa nặng khi mất nước hoặc nhiễm trùng theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do ngưỡng tái hấp thu HCO3- tại ống thận của trẻ nhỏ thấp hơn người lớn (18 - 21 mEq/L so với 24 - 26 mEq/L) và khả năng đào thải acid của thận còn non nớt.<br><br><b>💡 Lưu ý:</b><br>Đặc điểm giải phẫu - sinh lý non nớt khiến dự trữ kiềm của trẻ nhỏ sụt giảm cực nhanh.",
        "extra": "Văn bản gốc mục 1.2 (trang 2).",
        "tags": ["PED-11", "Barem-goc", "Hang-rao-dem", "Tre-nho"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B3 CHI SO ABG BINH THUONG & ANION GAP
    # =========================================================================
    {
        "id": "PED11-B13",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ số ABG",
        "section": "B3",
        "text": "[Barem gốc] Chỉ số khí máu bình thường ở trẻ em: pH = {{c1::7,35 - 7,45}}; PaCO2 = {{c1::35 - 45 mmHg}} (sơ sinh: {{c1::30 - 35 mmHg}}).",
        "extra": "Văn bản gốc Bảng II (trang 3).",
        "tags": ["PED-11", "Barem-goc", "Chi-so-ABG"]
    },
    {
        "id": "PED11-B14",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ số ABG",
        "section": "B3",
        "text": "[Barem gốc] Chỉ số HCO3- bình thường ở trẻ em là {{c1::22 - 26 mEq/L}} (nhũ nhi: {{c1::20 - 24 mEq/L}}); kiềm dư (Base Excess - BE) là {{c1::-2 → +2 mEq/L}}.",
        "extra": "Văn bản gốc Bảng II (trang 3).",
        "tags": ["PED-11", "Barem-goc", "Chi-so-ABG"]
    },
    {
        "id": "PED11-B15",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ số ABG",
        "section": "B3",
        "text": "[Barem gốc] Giá trị bình thường của PaO2 là {{c1::80 - 100 mmHg}} khi thở khí trời; độ bão hòa oxy động mạch SaO2 bình thường là {{c1::≥ 95%}}.",
        "extra": "Văn bản gốc Bảng II (trang 3).",
        "tags": ["PED-11", "Barem-goc", "Chi-so-ABG"]
    },
    {
        "id": "PED11-B16",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Anion Gap",
        "section": "B3",
        "text": "[Barem gốc] Công thức tính khoảng trống Anion Gap: AG = {{c1::[Na+] - ([Cl-] + [HCO3-])}}; giá trị bình thường là {{c1::12 ± 2 mEq/L}} (hoặc 8 - 16 mEq/L).",
        "extra": "Văn bản gốc mục 2.1 (trang 3).",
        "tags": ["PED-11", "Barem-goc", "Anion-Gap"]
    },
    {
        "id": "PED11-B17",
        "track": "barem_goc",
        "type": "basic",
        "category": "Anion Gap",
        "section": "B3",
        "front": "Ý nghĩa lâm sàng của việc phân loại toan chuyển hóa dựa vào mốc Anion Gap (AG) = 16 mEq/L theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>AG &gt; 16 mEq/L: toan tăng AG do tích tụ acid cố định (lactic, ceton, suy thận, ngộ độc); AG ≤ 16 mEq/L: toan AG bình thường do mất trực tiếp Bicarbonat kèm tăng Clo.<br><br><b>💡 Lưu ý:</b><br>Mốc 16 mEq/L là ranh giới vàng phân lập nhóm nguyên nhân toan chuyển hóa trong giáo trình.",
        "extra": "Văn bản gốc mục 2.1 (trang 3).",
        "tags": ["PED-11", "Barem-goc", "Anion-Gap"]
    },
    {
        "id": "PED11-B18",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ số ABG",
        "section": "B3",
        "text": "[Barem gốc] Định nghĩa Base Excess (BE - Kiềm dư): là lượng acid hoặc base cần thêm vào để đưa 1 lít máu toàn phần về pH {{c1::7,40}} ở điều kiện PaCO2 {{c1::40 mmHg}} và nhiệt độ 37°C.",
        "extra": "Văn bản gốc Bảng II (trang 3): BE < -2 mEq/L chỉ điểm thiếu hụt kiềm chuyển hóa.",
        "tags": ["PED-11", "Barem-goc", "Chi-so-ABG"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B4 TOAN CHUYEN HOA
    # =========================================================================
    {
        "id": "PED11-B19",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Toan chuyển hóa",
        "section": "B4",
        "text": "[Barem gốc] Định nghĩa Toan chuyển hóa: pH &lt; {{c1::7,35}} và HCO3- &lt; {{c1::22 mEq/L}} (kèm BE &lt; {{c1::-2 mEq/L}}).",
        "extra": "Văn bản gốc mục 3.1 (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Toan-chuyen-hoa"]
    },
    {
        "id": "PED11-B20",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Toan chuyển hóa tăng AG",
        "section": "B4",
        "text": "[Barem gốc] 4 nhóm nguyên nhân gây toan chuyển hóa tăng Anion Gap (AG &gt; 16 mEq/L): 1) Toan Lactic; 2) {{c1::DKA (Toan ceton đái tháo đường)}}; 3) {{c1::Suy thận cấp (ứ đọng phosphat, sulfat)}}; 4) {{c1::Ngộ độc (paracetamol, salicylate, methanol)}}.",
        "extra": "Văn bản gốc mục 3.1.A (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Toan-chuyen-hoa"]
    },
    {
        "id": "PED11-B21",
        "track": "barem_goc",
        "type": "basic",
        "category": "Toan Lactic",
        "section": "B4",
        "front": "Vì sao sốc giảm thể tích và mất nước nặng gây ra Toan Lactic tăng Anion Gap ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tụt thể tích tuần hoàn làm giảm tưới máu mô → tế bào thiếu oxy chuyển sang chuyển hóa yếm khí → sinh nhiều acid lactic giải phóng ion H+ và gốc lactate tích tụ.<br><br><b>💡 Lưu ý:</b><br>Gốc lactate là anion không đo được làm giãn rộng khoảng trống Anion Gap.",
        "extra": "Văn bản gốc mục 3.1.A (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Toan-Lactic"]
    },
    {
        "id": "PED11-B22",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Toan AG bình thường",
        "section": "B4",
        "text": "[Barem gốc] Toan chuyển hóa AG bình thường (AG ≤ 16 mEq/L, toan tăng Clo) do mất trực tiếp HCO3-: mất qua tiêu hóa gặp trong {{c1::tiêu chảy cấp mất nước nặng}} (dịch phân chứa HCO3- {{c1::30 - 50 mEq/L}}); mất qua thận gặp trong {{c1::toan hóa ống thận (RTA)}}.",
        "extra": "Văn bản gốc mục 3.1.B (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Toan-chuyen-hoa"]
    },
    {
        "id": "PED11-B23",
        "track": "barem_goc",
        "type": "basic",
        "category": "Toan tăng Clo",
        "section": "B4",
        "front": "Vì sao truyền quá nhiều dung dịch NaCl 0,9% lại gây ra toan chuyển hóa tăng Clo (AG bình thường)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>NaCl 0,9% có nồng độ Clo cao (154 mEq/L) so với máu (100 mEq/L), khi truyền lượng lớn gây tăng Clo máu và hòa loãng nồng độ Bicarbonat.<br><br><b>💡 Lưu ý:</b><br>Để giữ cân bằng điện tích, khi Clo máu tăng thì thận tăng đào thải Bicarbonat gây toan chuyển hóa tăng Clo.",
        "extra": "Văn bản gốc mục 3.1.B (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Toan-chuyen-hoa", "NaCl"]
    },
    {
        "id": "PED11-B24",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Công thức Winter",
        "section": "B4",
        "text": "[Barem gốc] Công thức Winter tính PaCO2 bù trừ dự đoán trong toan chuyển hóa: PaCO2 dự đoán = {{c1::(1,5 × [HCO3-]) + 8 ± 2}}.",
        "extra": "Văn bản gốc mục 3.1.C (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Cong-thuc-Winter"]
    },
    {
        "id": "PED11-B25",
        "track": "barem_goc",
        "type": "basic",
        "category": "Công thức Winter",
        "section": "B4",
        "front": "Khi áp dụng công thức Winter trong toan chuyển hóa, kết luận gì nếu PaCO2 đo được cao hơn hoặc thấp hơn PaCO2 dự đoán?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>PaCO2 đo được &gt; PaCO2 dự đoán: kèm Toan hô hấp phối hợp (suy hô hấp, kiệt sức thở); PaCO2 đo được &lt; PaCO2 dự đoán: kèm Kiềm hô hấp phối hợp.<br><br><b>💡 Lưu ý:</b><br>Nếu PaCO2 đo được nằm trong khoảng dự đoán: bù trừ hô hấp thích hợp.",
        "extra": "Văn bản gốc mục 3.1.C (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Cong-thuc-Winter"]
    },
    {
        "id": "PED11-B26",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thở Kussmaul",
        "section": "B4",
        "text": "[Barem gốc] Trong toan chuyển hóa, cơ chế bù trừ hô hấp là phổi kích hoạt kiểu {{c1::thở nhanh sâu (Kussmaul)}} nhằm đào thải CO2 hạ PaCO2 xuống mức bù trừ dự tính.",
        "extra": "Văn bản gốc mục 3.1.C (trang 4).",
        "tags": ["PED-11", "Barem-goc", "Cong-thuc-Winter"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B5 KIEM CHUYEN HOA
    # =========================================================================
    {
        "id": "PED11-B27",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kiềm chuyển hóa",
        "section": "B5",
        "text": "[Barem gốc] Định nghĩa Kiềm chuyển hóa: pH &gt; {{c1::7,45}} và HCO3- &gt; {{c1::26 mEq/L}} (kèm BE &gt; {{c1::+2 mEq/L}}).",
        "extra": "Văn bản gốc mục 3.2 (trang 5).",
        "tags": ["PED-11", "Barem-goc", "Kiem-chuyen-hoa"]
    },
    {
        "id": "PED11-B28",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hẹp môn vị",
        "section": "B5",
        "front": "Tam chứng điện giải - thăng bằng kiềm toan kinh điển ở trẻ hẹp phì đại môn vị (HPS) theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hạ Clo máu + Hạ Kali máu + Kiềm chuyển hóa (kèm nghịch lý nước tiểu acid).<br><br><b>💡 Cơ chế:</b><br>Nôn trớ dịch dạ dày làm mất HCl và Kali; thận thiếu Kali và thể tích nên ưu tiên giữ Na+ và bài xuất H+ vào nước tiểu.",
        "extra": "Văn bản gốc mục 3.2 (trang 5).",
        "tags": ["PED-11", "Barem-goc", "Hep-mon-vi"]
    },
    {
        "id": "PED11-B29",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kiềm chuyển hóa",
        "section": "B5",
        "text": "[Barem gốc] Các nguyên nhân gây kiềm chuyển hóa kinh điển ở trẻ em: hẹp phì đại môn vị, dùng {{c1::thuốc lợi tiểu quai (Furosemide)}} kéo dài, hút dịch dạ dày liên tục không bù dịch, và uống quá nhiều Bicarbonat.",
        "extra": "Văn bản gốc mục 3.2 (trang 5).",
        "tags": ["PED-11", "Barem-goc", "Kiem-chuyen-hoa"]
    },
    {
        "id": "PED11-B30",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kiềm chuyển hóa bù trừ",
        "section": "B5",
        "text": "[Barem gốc] Đáp ứng bù trừ hô hấp trong kiềm chuyển hóa: phổi giảm thông khí nhẹ để giữ lại CO2, PaCO2 tăng khoảng {{c1::0,7 mmHg}} cho mỗi {{c1::1 mEq/L}} HCO3- tăng thêm.",
        "extra": "Văn bản gốc mục 3.2 (trang 5).",
        "tags": ["PED-11", "Barem-goc", "Kiem-chuyen-hoa"]
    },
    {
        "id": "PED11-B31",
        "track": "barem_goc",
        "type": "basic",
        "category": "Kiềm chuyển hóa bù trừ",
        "section": "B5",
        "front": "Tại sao trong kiềm chuyển hóa, phổi không thể giảm thông khí quá mức để giữ CO2 bù trừ vô hạn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì giảm thông khí quá mức sẽ dẫn tới thiếu oxy máu (hạ PaO2), kích thích thụ thể hóa học xoang cảnh bắt buộc cơ thể phải thở.<br><br><b>💡 Lưu ý:</b><br>Mức bù trừ hô hấp trong kiềm chuyển hóa có giới hạn an toàn (hiếm khi PaCO2 vượt quá 55 - 60 mmHg ở bệnh nhi tự thở).",
        "extra": "Văn bản gốc mục 3.2 (trang 5).",
        "tags": ["PED-11", "Barem-goc", "Kiem-chuyen-hoa"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B6 TOAN HO HAP & KIEM HO HAP
    # =========================================================================
    {
        "id": "PED11-B32",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Toan hô hấp",
        "section": "B6",
        "text": "[Barem gốc] Định nghĩa Toan hô hấp: pH &lt; {{c1::7,35}} và PaCO2 &gt; {{c1::45 mmHg}}; cơ chế sinh bệnh học là do {{c1::giảm thông khí phế nang}} làm ứ trệ CO2.",
        "extra": "Văn bản gốc mục 3.3 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Toan-ho-hap"]
    },
    {
        "id": "PED11-B33",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hen phế quản",
        "section": "B6",
        "front": "Trong cơn hen phế quản cấp nặng ở trẻ em, dấu hiệu nào trên khí máu động mạch chỉ điểm kiệt sức cơ hô hấp tối khẩn theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>PaCO2 bắt đầu tăng cao (&gt; 45 mmHg) hoặc trở về 'bình thường' khi trẻ vẫn đang khó thở nặng.<br><br><b>💡 Lưu ý:</b><br>Ban đầu hen phải thở nhanh hạ PaCO2; khi PaCO2 tăng chứng tỏ cơ hô hấp đã kiệt sức dọa ngừng thở.",
        "extra": "Văn bản gốc mục 3.3 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Toan-ho-hap", "Hen-phe-quan"]
    },
    {
        "id": "PED11-B34",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Toan hô hấp bù trừ",
        "section": "B6",
        "text": "[Barem gốc] Bù trừ của thận trong Toan hô hấp: toan hô hấp cấp mỗi 10 mmHg PaCO2 tăng thì HCO3- tăng {{c1::1 mEq/L}}; toan hô hấp mạn mỗi 10 mmHg PaCO2 tăng thì HCO3- tăng {{c1::3,5 - 4 mEq/L}}.",
        "extra": "Văn bản gốc mục 3.3 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Toan-ho-hap"]
    },
    {
        "id": "PED11-B35",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kiềm hô hấp",
        "section": "B6",
        "text": "[Barem gốc] Định nghĩa Kiềm hô hấp: pH &gt; {{c1::7,45}} và PaCO2 &lt; {{c1::35 mmHg}}; cơ chế là do {{c1::tăng thông khí phế nang quá mức}} làm đào thải quá nhiều CO2.",
        "extra": "Văn bản gốc mục 3.4 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Kiem-ho-hap"]
    },
    {
        "id": "PED11-B36",
        "track": "barem_goc",
        "type": "basic",
        "category": "Kiềm hô hấp",
        "section": "B6",
        "front": "Các nguyên nhân gây kiềm hô hấp thường gặp ở trẻ em theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sốt cao, đau đớn/quấy khóc hoảng sợ, thở máy thông số quá cao, nhiễm trùng huyết giai đoạn sớm, và ngộ độc Salicylate (Aspirin) giai đoạn đầu.<br><br><b>💡 Cơ chế:</b><br>Salicylate kích thích trực tiếp trung tâm hô hấp tại hành não gây tăng thông khí dữ dội.",
        "extra": "Văn bản gốc mục 3.4 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Kiem-ho-hap"]
    },
    {
        "id": "PED11-B37",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kiềm hô hấp bù trừ",
        "section": "B6",
        "text": "[Barem gốc] Bù trừ của thận trong Kiềm hô hấp: kiềm hô hấp cấp mỗi 10 mmHg PaCO2 giảm thì HCO3- giảm {{c1::2 mEq/L}}; kiềm hô hấp mạn mỗi 10 mmHg PaCO2 giảm thì HCO3- giảm {{c1::4 - 5 mEq/L}}.",
        "extra": "Văn bản gốc mục 3.4 (trang 6).",
        "tags": ["PED-11", "Barem-goc", "Kiem-ho-hap"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B7 LUU DO 5 BUOC DOC ABG & DELTA GAP
    # =========================================================================
    {
        "id": "PED11-B38",
        "track": "barem_goc",
        "type": "basic",
        "category": "Lưu đồ 5 bước",
        "section": "B7",
        "front": "5 bước đọc khí máu động mạch tại giường bệnh theo lưu đồ giáo trình gồm những bước nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bước 1: Đánh giá pH; Bước 2: Xác định rối loạn tiên phát qua PaCO2 và HCO3-; Bước 3: Đánh giá bù trừ (Winter); Bước 4: Tính Anion Gap (AG); Bước 5: Tính Delta Gap.<br><br><b>💡 Lưu ý:</b><br>Đọc tuần tự không bỏ bước để không bỏ sót rối loạn toan kiềm hỗn hợp.",
        "extra": "Văn bản gốc Phần IV (trang 7).",
        "tags": ["PED-11", "Barem-goc", "Luu-do-5-buoc"]
    },
    {
        "id": "PED11-B39",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Lưu đồ đọc ABG",
        "section": "B7",
        "text": "[Barem gốc] Bước 1 & 2 đọc ABG: Nếu pH &lt; 7,35 kèm HCO3- &lt; 22 là {{c1::Toan chuyển hóa tiên phát}}; kèm PaCO2 &gt; 45 là {{c1::Toan hô hấp tiên phát}}.",
        "extra": "Văn bản gốc Phần IV (trang 7).",
        "tags": ["PED-11", "Barem-goc", "Luu-do-5-buoc"]
    },
    {
        "id": "PED11-B40",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Lưu đồ đọc ABG",
        "section": "B7",
        "text": "[Barem gốc] Bước 1 & 2 đọc ABG: Nếu pH &gt; 7,45 kèm HCO3- &gt; 26 là {{c1::Kiềm chuyển hóa tiên phát}}; kèm PaCO2 &lt; 35 là {{c1::Kiềm hô hấp tiên phát}}.",
        "extra": "Văn bản gốc Phần IV (trang 7).",
        "tags": ["PED-11", "Barem-goc", "Luu-do-5-buoc"]
    },
    {
        "id": "PED11-B41",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Delta Gap",
        "section": "B7",
        "text": "[Barem gốc] Công thức tỷ số Delta Gap (Delta Ratio): Ratio = {{c1::(AG đo được - 12) / (24 - [HCO3-] đo được)}}.",
        "extra": "Văn bản gốc Bước 5 (trang 7): ΔAG / ΔHCO3-.",
        "tags": ["PED-11", "Barem-goc", "Delta-Gap"]
    },
    {
        "id": "PED11-B42",
        "track": "barem_goc",
        "type": "basic",
        "category": "Delta Gap",
        "section": "B7",
        "front": "Ý nghĩa của 3 khoảng giá trị Delta Ratio (Delta Gap) trong toan chuyển hóa tăng Anion Gap theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ratio &lt; 0,8: kèm toan chuyển hóa AG bình thường (mất thêm kiềm qua phân/thận); Ratio 0,8 - 2,0: toan tăng AG đơn thuần; Ratio &gt; 2,0: kèm Kiềm chuyển hóa (do nôn/dùng kiềm).<br><br><b>💡 Cơ chế:</b><br>So sánh mức tăng acid cố định bất thường với mức tiêu hao ion dự trữ kiềm Bicarbonat.",
        "extra": "Văn bản gốc Bước 5 (trang 7).",
        "tags": ["PED-11", "Barem-goc", "Delta-Gap"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B8 NGUYEN TAC XU TRI & CHI DINH BU KIEM
    # =========================================================================
    {
        "id": "PED11-B43",
        "track": "barem_goc",
        "type": "basic",
        "category": "Nguyên tắc xử trí",
        "section": "B8",
        "front": "Vì sao trong phần lớn trường hợp toan chuyển hóa ở trẻ em, bù dịch đủ bằng Ringer Lactat lại là biện pháp điều trị quan trọng nhất?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bù đủ dịch phục hồi tưới máu mô → chấm dứt chuyển hóa yếm khí → gan chuyển hóa hết acid lactic thành Bicarbonat nội sinh và thận tái hoạt động đào thải acid.<br><br><b>💡 Lưu ý:</b><br>Toan máu tự thoái lui khi huyết động phục hồi mà không cần tiêm Natri Bicarbonat.",
        "extra": "Văn bản gốc mục 5.1 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Nguyen-tac-dieu-tri"]
    },
    {
        "id": "PED11-B44",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định Bicarbonat",
        "section": "B8",
        "text": "[Barem gốc] Giáo trình nhấn mạnh: Tuyệt đối {{c1::không bù Bicarbonat thường quy}} trong mọi trường hợp toan chuyển hóa ở trẻ em.",
        "extra": "Văn bản gốc mục 5.2 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-B45",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định Bicarbonat",
        "section": "B8",
        "text": "[Barem gốc] Chỉ định 1 bù NaHCO3: Toan chuyển hóa nặng đe dọa tính mạng khi pH &lt; {{c1::7,10}} hoặc HCO3- &lt; {{c1::8 - 10 mEq/L}} có rối loạn huyết động trơ dịch truyền và giảm đáp ứng thuốc vận mạch.",
        "extra": "Văn bản gốc mục 5.2 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-B46",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thuốc vận mạch",
        "section": "B8",
        "front": "Vì sao trong môi trường toan máu nặng (pH &lt; 7,10), các thuốc vận mạch như Adrenaline và Noradrenaline bị giảm tác dụng mạnh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do toan máu làm biến đổi cấu hình, giảm ái lực và giảm độ nhạy cảm của các thụ thể adrenergic (alpha và beta) trên mạch máu và cơ tim với catecholamine.<br><br><b>💡 Lưu ý:</b><br>Nâng pH tạm thời lên mức an toàn giúp phục hồi độ nhạy của receptor vận mạch.",
        "extra": "Văn bản gốc mục 5.2 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-B47",
        "track": "barem_goc",
        "type": "basic",
        "category": "Chỉ định Bicarbonat",
        "section": "B8",
        "front": "4 chỉ định nghiêm ngặt bù Natri Bicarbonat theo giáo trình Y Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Toan nặng đe dọa tính mạng (pH &lt; 7,10 hoặc HCO3- &lt; 8-10 tụt HA trơ vận mạch); 2) Toan mất kiềm do tiêu chảy cấp/RTA không hồi phục sau bù dịch; 3) Tăng Kali máu nặng dọa ngừng tim; 4) Ngộ độc thuốc chống trầm cảm 3 vòng (TCA).<br><br><b>💡 Lưu ý:</b><br>Bù kiềm là can thiệp đặc biệt có chọn lọc, không phải điều trị đại trà.",
        "extra": "Văn bản gốc mục 5.2 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-B48",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định Bicarbonat",
        "section": "B8",
        "text": "[Barem gốc] Chỉ định bù NaHCO3 trong tăng Kali máu nặng dọa ngừng tim nhằm mục đích: kiềm hóa máu để {{c1::kéo ion K+ từ huyết tương chạy vào trong nội bào}}.",
        "extra": "Văn bản gốc mục 5.2 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Chi-dinh-Bicarbonat"]
    },

    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B9 CONG THUC BU KIEM & BIEN CHUNG
    # =========================================================================
    {
        "id": "PED11-B49",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Công thức bù kiềm",
        "section": "B9",
        "text": "[Barem gốc] Công thức tính lượng NaHCO3 cần bù: Lượng NaHCO3 (mEq) = {{c1::([HCO3- mong muốn] - [HCO3- bệnh nhân]) × 0,5 × P (kg)}}.",
        "extra": "Văn bản gốc mục 5.3 (trang 8): Hệ số phân bố Bicarbonat ở trẻ em là 0,5 (toan nặng 0,6 - 0,7).",
        "tags": ["PED-11", "Barem-goc", "Cong-thuc-bu-kiem"]
    },
    {
        "id": "PED11-B50",
        "track": "barem_goc",
        "type": "basic",
        "category": "Mục tiêu bù kiềm",
        "section": "B9",
        "front": "Mục tiêu nồng độ HCO3- mong muốn khi tính bù Bicarbonat cấp cứu là bao nhiêu và bẫy tử vong cần tránh là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chỉ đặt mục tiêu nâng HCO3- lên 12 - 15 mEq/L (hoặc nâng pH lên ~7,20).<br><br><b>🛑 BẪY TỬ VONG:</b><br>Tuyệt đối không đặt mục tiêu đưa HCO3- về mức bình thường 24 mEq/L ngay từ đầu!",
        "extra": "Văn bản gốc mục 5.3 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Cong-thuc-bu-kiem", "Bay-tu-vong"]
    },
    {
        "id": "PED11-B51",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Kỹ thuật truyền",
        "section": "B9",
        "text": "[Barem gốc] Kỹ thuật truyền NaHCO3: Chỉ truyền {{c1::1/2}} lượng tính toán trong {{c1::2 - 4 giờ}} đầu; {{c1::1/2}} còn lại truyền chậm trong 12 - 24 giờ tiếp theo dựa trên khí máu kiểm tra lại.",
        "extra": "Văn bản gốc mục 5.4 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Ky-thuat-truyen"]
    },
    {
        "id": "PED11-B52",
        "track": "barem_goc",
        "type": "basic",
        "category": "Dung dịch kiềm",
        "section": "B9",
        "front": "So sánh nồng độ và cách sử dụng dung dịch Natri Bicarbonat 1,4% và 8,4% theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1,4%: dung dịch đẳng trương (167 mEq/L, 1 ml ≈ 0,167 mEq), truyền trực tiếp; 8,4%: ưu trương rất cao (1000 mEq/L, 1 ml = 1 mEq), bắt buộc pha loãng 1:1 hoặc 1:4 với Glucose 5%.<br><br><b>💡 Cảnh báo:</b><br>Cấm tiêm thẳng 8,4% vào tĩnh mạch ngoại vi vì nguy cơ hoại tử mô và ưu trương mạch máu.",
        "extra": "Văn bản gốc mục 5.4 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Dung-dich-Bicarbonat"]
    },
    {
        "id": "PED11-B53",
        "track": "barem_goc",
        "type": "basic",
        "category": "Toan CSF nghịch thường",
        "section": "B9",
        "front": "Cơ chế sinh lý bệnh của hiện tượng Toan dịch não tủy nghịch thường (Paradoxical CSF Acidosis) khi bù Bicarbonat nhanh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>HCO3- đệm H+ sinh ra CO2; CO2 tan trong lipid khuếch tán cực nhanh qua hàng rào máu não vào CSF, trong khi HCO3- ngấm rất chậm → pH dịch não tủy tụt sâu ức chế hô hấp và tri giác.<br><br><b>💡 Lưu ý:</b><br>Máu đo thấy kiềm hơn nhưng não lại bị toan hóa nặng hơn.",
        "extra": "Văn bản gốc mục 5.5 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Bien-chung-Bicarbonat"]
    },
    {
        "id": "PED11-B54",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Biến chứng bù kiềm",
        "section": "B9",
        "text": "[Barem gốc] 5 biến chứng nguy hiểm khi bù Bicarbonat quá mức: 1) Toan dịch não tủy nghịch thường; 2) {{c1::Hạ Kali máu cấp tính}}; 3) {{c1::Hạ Canxi ion hóa máu (tetany)}}; 4) {{c1::Giảm giải phóng oxy cho mô (hiệu ứng Bohr)}}; 5) {{c1::Quá tải dịch và tăng Natri máu ưu trương}}.",
        "extra": "Văn bản gốc mục 5.5 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Bien-chung-Bicarbonat"]
    },
    {
        "id": "PED11-B55",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hiệu ứng Bohr",
        "section": "B9",
        "front": "Tại sao kiềm hóa máu lại gây giảm giải phóng oxy cho mô theo hiệu ứng Bohr?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Kiềm máu (tăng pH) làm chuyển dịch đường cong phân ly Hemoglobin - Oxy sang trái, khiến Hb giữ chặt oxy và giảm nhả oxy cho các mô đang thiếu máu.<br><br><b>💡 Lưu ý:</b><br>Làm nặng thêm tình trạng thiếu oxy tế bào dù PaO2 đo được có thể bình thường.",
        "extra": "Văn bản gốc mục 5.5 (trang 8).",
        "tags": ["PED-11", "Barem-goc", "Hieu-ung-Bohr"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E0 TONG QUAN & GUIDELINES DOI CHIEU
    # =========================================================================
    {
        "id": "PED11-E01",
        "track": "ebm",
        "type": "basic",
        "category": "Sinh lý enzyme",
        "section": "E0",
        "front": "Vì sao nồng độ ion H+ tự do trong máu phải được duy trì cực kỳ nghiêm ngặt trong khoảng pH 7,35 - 7,45?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì ion H+ tự do quyết định cấu hình không gian và hoạt tính sinh học của toàn bộ enzyme tế bào, protein vận chuyển và kênh ion màng.<br><br><b>💡 Cơ chế:</b><br>Khi pH lệch ra ngoài 7,35 - 7,45, các enzyme mất hoạt tính dẫn đến sụp đổ chuyển hóa tế bào đa cơ quan.",
        "extra": "Release lesson Mục 0.1: Nền tảng tối thiểu cần dùng ngay.",
        "tags": ["PED-11", "EBM", "Tong-quan"]
    },
    {
        "id": "PED11-E02",
        "track": "ebm",
        "type": "cloze",
        "category": "Dịch tễ tiêu chảy toan hỗn hợp",
        "section": "E0",
        "text": "[EBM] Nghiên cứu đa trung tâm Singhi S et al. 2022 (PMID 36755633, n = 312) chứng minh: toan chuyển hóa trong tiêu chảy mất nước nặng ở trẻ em gồm 2 cấu phần: toan tăng AG do toan lactic và toan AG bình thường do mất HCO3- qua phân, chiếm tỷ lệ {{c1::64,2%}}.",
        "extra": "PMID 36755633 (Singhi 2022). Cơ sở áp dụng Delta Gap bóc tách toan hỗn hợp.",
        "tags": ["PED-11", "EBM", "PMID-36755633", "Singhi-2022"]
    },
    {
        "id": "PED11-E03",
        "track": "ebm",
        "type": "cloze",
        "category": "Bicarbonat ngừng tim",
        "section": "E0",
        "text": "[EBM] Nghiên cứu đoàn hệ 10 năm tại PICU của Raymond TT et al. 2025 (PMID 40249229, n = 1.156): sử dụng sớm Natri Bicarbonat trong cấp cứu ngừng tim nhi {{c1::không cải thiện}} tỷ lệ có lại tuần hoàn tự nhiên (aOR = {{c1::0,94}}; 95% CI: 0,72 - 1,22) và không tăng tỷ lệ sống sót ra viện.",
        "extra": "PMID 40249229 (Raymond 2025). Khuyến cáo Pediatric Critical Care Medicine 2025: cấm bù thường quy.",
        "tags": ["PED-11", "EBM", "PMID-40249229", "Raymond-2025"]
    },
    {
        "id": "PED11-E04",
        "track": "ebm",
        "type": "basic",
        "category": "Tiên lượng tử vong ABG",
        "section": "E0",
        "front": "Theo nghiên cứu Lee J et al. 2023 (PMID 37511675), hai chỉ số khí máu nào trên mẫu ABG ban đầu liên quan độc lập với tiên lượng tử vong trong ngừng tuần hoàn ngoài viện ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>pH &lt; 7,00 và kiềm dư BE &lt; -18 mEq/L.<br><br><b>💡 Lưu ý lâm sàng:</b><br>Đây là các ngưỡng nguy kịch cảnh báo toan chuyển hóa mất bù cực nặng đe dọa tử vong tức thì.",
        "extra": "PMID 37511675 (Lee 2023, n = 512).",
        "tags": ["PED-11", "EBM", "PMID-37511675", "Tien-luong"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E1 DINH NGHIA & KY THUAT LAY MAU
    # =========================================================================
    {
        "id": "PED11-E05",
        "track": "ebm",
        "type": "basic",
        "category": "Chỉ số theo tuổi",
        "section": "E1",
        "front": "Khác biệt về chỉ số khí máu bình thường giữa trẻ sơ sinh so với trẻ lớn là gì và do đâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sơ sinh có PaCO2 sinh lý thấp hơn (30 - 35 vs 35 - 45 mmHg) và HCO3- thấp hơn (20 - 24 vs 22 - 26 mEq/L) do thông khí nhanh hơn và ngưỡng tái hấp thu kiềm của thận thấp hơn.<br><br><b>💡 Lưu ý:</b><br>Không nhầm lẫn PaCO2 32 mmHg ở trẻ sơ sinh là kiềm hô hấp bệnh lý.",
        "extra": "Release lesson Mục 1.2: Bảng chỉ số khí máu động mạch bình thường theo lứa tuổi.",
        "tags": ["PED-11", "EBM", "Chi-so-theo-tuoi"]
    },
    {
        "id": "PED11-E06",
        "track": "ebm",
        "type": "cloze",
        "category": "VBG so với ABG",
        "section": "E1",
        "text": "[EBM] Trong điều kiện huyết động ổn định, khí máu tĩnh mạch (VBG) có: pH thấp hơn ABG khoảng {{c1::0,03 - 0,05 đơn vị}}; PvCO2 cao hơn PaCO2 khoảng {{c1::4 - 6 mmHg}}; nồng độ HCO3- tĩnh mạch {{c1::tương đương}} máu động mạch.",
        "extra": "Release lesson Mục 1.3: So sánh ABG và VBG.",
        "tags": ["PED-11", "EBM", "VBG-vs-ABG"]
    },
    {
        "id": "PED11-E07",
        "track": "ebm",
        "type": "basic",
        "category": "VBG trong sốc nặng",
        "section": "E1",
        "front": "Vì sao trong sốc nặng hoặc ngừng tuần hoàn, khí máu tĩnh mạch (VBG) KHÔNG THỂ thay thế cho khí máu động mạch (ABG)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do ứ trệ tuần hoàn ngoại vi và chuyển hóa yếm khí cục bộ, độ chênh lệch pH và PaCO2 giữa động mạch và tĩnh mạch tăng vọt rất lớn (pH tĩnh mạch tụt sâu, PvCO2 tăng vọt).<br><br><b>💡 Lưu ý:</b><br>VBG chỉ phản ánh tình trạng ứ trệ mô ngoại vi, không phản ánh chính xác thông khí phế nang và toan kiềm trung tâm.",
        "extra": "Release lesson Mục 1.3 & Bẫy lâm sàng 6.",
        "tags": ["PED-11", "EBM", "VBG-vs-ABG", "Soc-nang"]
    },
    {
        "id": "PED11-E08",
        "track": "ebm",
        "type": "basic",
        "category": "Test Allen",
        "section": "E1",
        "front": "Mục đích của Test Allen biến đổi trước khi chọc khí máu động mạch quay ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đánh giá sự tưới máu bàng hệ của động mạch trụ cho bàn tay đề phòng nguy cơ hoại tử chi nếu động mạch quay bị tắc nghẽn hoặc co thắt.<br><br><b>💡 Lưu ý:</b><br>Nếu bàn tay hồng trở lại trong &lt; 5-10 giây: test dương tính, an toàn để chọc động mạch quay.",
        "extra": "Release lesson Mục 1.4: Kỹ thuật lấy máu động mạch an toàn.",
        "tags": ["PED-11", "EBM", "Test-Allen"]
    },
    {
        "id": "PED11-E09",
        "track": "ebm",
        "type": "cloze",
        "category": "Kỹ thuật lấy ABG",
        "section": "E1",
        "text": "[EBM] Kỹ thuật lấy ABG: dùng bơm tiêm tráng Heparin khô với thể tích không quá {{c1::0,1 ml}} cho 1 ml máu, góc kim chọc {{c1::30 - 45°}} tại động mạch quay; sau lấy máu phải đuổi bọt khí ngay và phân tích trong vòng {{c1::15 - 30 phút}}.",
        "extra": "Release lesson Mục 1.4: Dư thừa heparin lỏng làm toan máu giả tạo do pH acid của heparin.",
        "tags": ["PED-11", "EBM", "Ky-thuat-lay-ABG"]
    },
    {
        "id": "PED11-E10",
        "track": "ebm",
        "type": "basic",
        "category": "Sai số ABG",
        "section": "E1",
        "front": "Sai số xét nghiệm khí máu sẽ xảy ra như thế nào nếu mẫu máu bị lẫn bọt khí và không được phân tích ngay?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bọt khí làm oxy khuếch tán vào (PaO2 tăng giả) và CO2 khuếch tán ra (PaCO2 giảm giả, pH tăng giả); để lâu không ướp đá hồng cầu tiếp tục tiêu thụ O2 sinh CO2 làm toan hóa mẫu.<br><br><b>💡 Lưu ý:</b><br>Đuổi sạch bọt khí và ướp đá ngay lập tức nếu chưa thể chạy máy trong 15 phút.",
        "extra": "Release lesson Mục 1.4: Kỹ thuật lấy máu động mạch.",
        "tags": ["PED-11", "EBM", "Sai-so-ABG"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E2 CO CHE BENH SINH & TOAN HOA ONG THAN (RTA)
    # =========================================================================
    {
        "id": "PED11-E11",
        "track": "ebm",
        "type": "basic",
        "category": "Chuỗi cơ chế",
        "section": "E2",
        "front": "Chuỗi cơ chế bệnh sinh giải thích toan chuyển hóa tăng Anion Gap trong sốc giảm thể tích ở trẻ tiêu chảy cấp là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Mất nước nặng → tụt thể tích lòng mạch, giảm tưới máu mao mạch → tế bào thiếu oxy chuyển hóa yếm khí sinh acid lactic → tích tụ H+ và gốc lactate tự do → toan chuyển hóa tăng AG và thở Kussmaul.<br><br><b>💡 Lưu ý:</b><br>Tái lập tưới máu mô là chìa khóa then chốt đảo ngược chuỗi bệnh sinh này.",
        "extra": "Release lesson Mục 2.2: Chuỗi cơ chế 1.",
        "tags": ["PED-11", "EBM", "Chuoi-co-che", "Toan-lactic"]
    },
    {
        "id": "PED11-E12",
        "track": "ebm",
        "type": "basic",
        "category": "Chuỗi cơ chế",
        "section": "E2",
        "front": "Chuỗi cơ chế giải thích kiềm chuyển hóa giảm Clo máu và nghịch lý nước tiểu acid ở trẻ hẹp phì đại môn vị là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nôn mất HCl và nước → mất Clo, giảm thể tích → tăng Aldosterone giữ Na+ và thải K+/H+ → hạ Kali máu nặng → tế bào ống thận buộc phải bài tiết ion H+ vào nước tiểu gây toan niệu nghịch lý.<br><br><b>💡 Cơ chế:</b><br>Thận ưu tiên giữ Na+ và K+ để duy trì sự sống, hy sinh bài tiết H+ làm máu càng kiềm nặng.",
        "extra": "Release lesson Mục 2.2: Chuỗi cơ chế 3.",
        "tags": ["PED-11", "EBM", "Chuoi-co-che", "Hep-mon-vi"]
    },
    {
        "id": "PED11-E13",
        "track": "ebm",
        "type": "cloze",
        "category": "RTA typ 1",
        "section": "E2",
        "text": "[EBM] Toan hóa ống thận typ 1 (Distal RTA): cơ chế do giảm bài tiết {{c1::ion H+}} tại ống lượn xa và ống góp; đặc điểm then chốt là pH nước tiểu luôn {{c1::> 5,5}} dù cơ thể đang toan máu nặng; biến chứng điển hình là lắng đọng canxi thận và sỏi thận.",
        "extra": "Release lesson Mục 2.3: Phân loại RTA.",
        "tags": ["PED-11", "EBM", "RTA-typ-1"]
    },
    {
        "id": "PED11-E14",
        "track": "ebm",
        "type": "cloze",
        "category": "RTA typ 2",
        "section": "E2",
        "text": "[EBM] Toan hóa ống thận typ 2 (Proximal RTA): cơ chế do giảm tái hấp thu {{c1::HCO3-}} tại ống lượn gần (thường kèm hội chứng Fanconi); khi toan máu nặng thì pH nước tiểu {{c1::< 5,5}} vì ống xa vẫn toan hóa được nước tiểu.",
        "extra": "Release lesson Mục 2.3: Phân loại RTA.",
        "tags": ["PED-11", "EBM", "RTA-typ-2"]
    },
    {
        "id": "PED11-E15",
        "track": "ebm",
        "type": "basic",
        "category": "Phân biệt RTA",
        "section": "E2",
        "front": "Điểm khác biệt mấu chốt để phân biệt RTA typ 1 và RTA typ 2 qua xét nghiệm nước tiểu khi bệnh nhi đang toan máu nặng là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>RTA typ 1 ống xa bị hỏng nên pH niệu luôn &gt; 5,5 (không thể toan hóa nước tiểu); RTA typ 2 ống xa bình thường nên khi toan máu nặng pH niệu có thể hạ xuống &lt; 5,5.<br><br><b>💡 Lưu ý:</b><br>RTA typ 1 hay kèm sỏi thận/vôi hóa thận; RTA typ 2 hay kèm mất glucose, acid amin, phosphat (hội chứng Fanconi).",
        "extra": "Release lesson Mục 2.3 & Checkpoint 7.",
        "tags": ["PED-11", "EBM", "RTA", "Phan-biet"]
    },
    {
        "id": "PED11-E16",
        "track": "ebm",
        "type": "cloze",
        "category": "RTA typ 4",
        "section": "E2",
        "text": "[EBM] Toan hóa ống thận typ 4 (RTA typ 4): cơ chế do thiếu hụt hoặc đề kháng {{c1::Aldosterone}}; đặc điểm lâm sàng phân biệt với typ 1 và typ 2 là có {{c1::Tăng Kali máu}} (typ 1 và 2 đều hạ Kali máu).",
        "extra": "Release lesson Mục 2.3: Bảng so sánh 3 thể RTA.",
        "tags": ["PED-11", "EBM", "RTA-typ-4"]
    },
    {
        "id": "PED11-E17",
        "track": "ebm",
        "type": "basic",
        "category": "Chuỗi cơ chế hen",
        "section": "E2",
        "front": "Chuỗi cơ chế dẫn đến toan hô hấp cấp mất bù trong cơn hen phế quản ác tính ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Co thắt phế quản nặng và ứ khí phế nang → công thở tăng vọt kéo dài → cơ hô hấp kiệt sức hoàn toàn → giảm thông khí phế nang đột ngột → ứ trệ CO2 (PaCO2 tăng vọt) gây toan hô hấp cấp dọa ngừng tim.<br><br><b>💡 Cảnh báo:</b><br>Dấu hiệu 'lồng ngực im lặng' (silent chest) đi kèm toan hô hấp là tối khẩn cấp.",
        "extra": "Release lesson Mục 2.2: Chuỗi cơ chế 4.",
        "tags": ["PED-11", "EBM", "Chuoi-co-che", "Hen-phe-quan"]
    },
    {
        "id": "PED11-E18",
        "track": "ebm",
        "type": "cloze",
        "category": "Urine Anion Gap",
        "section": "E2",
        "text": "[EBM] RTA typ 1 có khoảng trống Anion Gap niệu (Urine AG = [Na+] + [K+] - [Cl-]) mang giá trị {{c1::dương tính (+)}}, phản ánh sự suy giảm nghiêm trọng trong đào thải amoni (NH4+) của ống lượn xa.",
        "extra": "Release lesson Mục 2.3: Urine Anion Gap trong chẩn đoán phân biệt toan tăng Clo.",
        "tags": ["PED-11", "EBM", "RTA-typ-1", "Urine-AG"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E3 VI DU TINH TOAN MINH HOA TAI GIUONG
    # =========================================================================
    {
        "id": "PED11-E19",
        "track": "ebm",
        "type": "basic",
        "category": "Anion Gap hiệu chỉnh",
        "section": "E3",
        "front": "Công thức hiệu chỉnh Anion Gap theo nồng độ Albumin máu ở trẻ em là gì và vì sao bắt buộc phải hiệu chỉnh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>AG hiệu chỉnh = AG đo được + 2,5 × (4,0 - Albumin g/dL).<br><br><b>💡 Cơ chế:</b><br>Albumin là anion không đo được chủ yếu; giảm mỗi 1 g/dL Albumin làm AG giảm giả 2,5 mEq/L, dễ che giấu toan chuyển hóa tăng AG nặng.",
        "extra": "PMID 41120922 (Wang L 2025): độ nhạy phát hiện toan tăng từ 62,1% lên 88,5% khi hiệu chỉnh.",
        "tags": ["PED-11", "EBM", "Anion-Gap-hieu-chinh", "PMID-41120922"]
    },
    {
        "id": "PED11-E20",
        "track": "ebm",
        "type": "cloze",
        "category": "Anion Gap hiệu chỉnh",
        "section": "E3",
        "text": "[EBM] Nghiên cứu PICU Wang L et al. 2025 (PMID 41120922, n = 428) chứng minh: Anion Gap hiệu chỉnh theo Albumin có độ nhạy {{c1::88,5%}} trong dự đoán tổn thương tạng và toan lactic so với chỉ {{c1::62,1%}} của Anion Gap chưa hiệu chỉnh.",
        "extra": "PMID 41120922. Bỏ qua hiệu chỉnh Albumin là bẫy lâm sàng số 7.",
        "tags": ["PED-11", "EBM", "PMID-41120922", "Wang-2025"]
    },
    {
        "id": "PED11-E21",
        "track": "ebm",
        "type": "basic",
        "category": "Ví dụ lâm sàng 1",
        "section": "E3",
        "front": "Bệnh nhi tiêu chảy có HCO3- = 12 mEq/L. Áp dụng công thức Winter tính PaCO2 dự đoán và biện luận nếu PaCO2 đo được là 35 mmHg?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>PaCO2 dự đoán = (1,5 × 12) + 8 ± 2 = 26 ± 2 mmHg (từ 24 đến 28 mmHg).<br><br><b>💡 Biện luận:</b><br>PaCO2 đo được 35 mmHg &gt; 28 mmHg → Bệnh nhi có Toan hô hấp phối hợp do suy giảm thông khí hoặc kiệt sức cơ thở.",
        "extra": "Release lesson Mục 3.2: Ví dụ lâm sàng 1.",
        "tags": ["PED-11", "EBM", "Winter", "Vi-du-lam-sang"]
    },
    {
        "id": "PED11-E22",
        "track": "ebm",
        "type": "basic",
        "category": "Ví dụ lâm sàng 3",
        "section": "E3",
        "front": "Bệnh nhi nhiễm khuẩn huyết có Albumin = 2,0 g/dL, Na+ = 130, Cl- = 105, HCO3- = 14 mEq/L. Tính AG đo được và AG hiệu chỉnh, rút ra kết luận lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>AG đo được = 130 - (105 + 14) = 11 mEq/L; AG hiệu chỉnh = 11 + 2,5 × (4,0 - 2,0) = 16 mEq/L.<br><br><b>💡 Kết luận:</b><br>Hạ Albumin máu đã che giấu sự gia tăng của anion acid cố định; thực chất bệnh nhi có toan chuyển hóa tăng AG tiềm ẩn.",
        "extra": "Release lesson Mục 3.2: Ví dụ lâm sàng 3.",
        "tags": ["PED-11", "EBM", "Anion-Gap", "Vi-du-lam-sang"]
    },
    {
        "id": "PED11-E23",
        "track": "ebm",
        "type": "basic",
        "category": "Ví dụ lâm sàng 4",
        "section": "E3",
        "front": "Bệnh nhi tiêu chảy mất nước có AG = 20 mEq/L và HCO3- = 8 mEq/L. Tính Delta Ratio và giải thích bản chất rối loạn toan kiềm hỗn hợp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Delta Ratio = (20 - 12) / (24 - 8) = 8 / 16 = 0,5.<br><br><b>💡 Biện luận:</b><br>Ratio 0,5 &lt; 0,8 chứng tỏ HCO3- sụt giảm nhiều hơn mức tăng của AG → Toan chuyển hóa hỗn hợp: toan lactic (tăng AG) kết hợp toan mất kiềm qua phân (AG bình thường).",
        "extra": "Release lesson Mục 3.2: Ví dụ lâm sàng 4.",
        "tags": ["PED-11", "EBM", "Delta-Gap", "Vi-du-lam-sang"]
    },
    {
        "id": "PED11-E24",
        "track": "ebm",
        "type": "cloze",
        "category": "Toan hô hấp mạn",
        "section": "E3",
        "text": "[EBM] Trẻ bị loạn sản phế quản phổi (BPD) có PaCO2 tăng mạn tính lên 60 mmHg (tăng 20 mmHg). Mức HCO3- thận bù trừ dự kiến là {{c1::31 mEq/L}} (24 + 2 × 3,5); nếu xét nghiệm HCO3- là 32 mEq/L và pH 7,36 thì kết luận là {{c1::toan hô hấp mạn tính bù trừ hoàn toàn}}.",
        "extra": "Release lesson Mục 3.2: Ví dụ lâm sàng 6.",
        "tags": ["PED-11", "EBM", "Toan-ho-hap-man", "BPD"]
    },
    {
        "id": "PED11-E25",
        "track": "ebm",
        "type": "cloze",
        "category": "Delta Gap",
        "section": "E3",
        "text": "[EBM] Khi Delta Ratio (ΔAG / ΔHCO3-) &gt; {{c1::2,0}}, chứng tỏ nồng độ Bicarbonat thực tế cao hơn nhiều so với dự tính, chỉ điểm có {{c1::Kiềm chuyển hóa phối hợp}} (ví dụ trẻ DKA nôn nhiều hoặc bệnh nhân đã được truyền Bicarbonat trước đó).",
        "extra": "Release lesson Mục 3.1: Bước 5 đọc khí máu.",
        "tags": ["PED-11", "EBM", "Delta-Gap"]
    },
    {
        "id": "PED11-E26",
        "track": "ebm",
        "type": "basic",
        "category": "Ví dụ lâm sàng 5",
        "section": "E3",
        "front": "Cách tính liều Natri Bicarbonat 1,4% cho bệnh nhi 10 kg có pH = 7,08 và HCO3- = 6 mEq/L trong sốc nhiễm khuẩn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Lượng NaHCO3 = (12 - 6) × 0,5 × 10 = 30 mEq. Lấy dung dịch 1,4% (0,167 mEq/ml): 30 / 0,167 = 180 ml.<br><br><b>💡 Kỹ thuật:</b><br>Truyền 1/2 liều (90 ml) trong 2 giờ đầu rồi xét nghiệm lại khí máu, không truyền hết một lần.",
        "extra": "Release lesson Mục 3.2: Ví dụ lâm sàng 5.",
        "tags": ["PED-11", "EBM", "Cong-thuc-bu-kiem", "Vi-du-lam-sang"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E4 DIEU TRI TOAN & PHAC DO BU NAHCO3 AN TOAN
    # =========================================================================
    {
        "id": "PED11-E27",
        "track": "ebm",
        "type": "basic",
        "category": "Ringer Lactat",
        "section": "E4",
        "front": "Tại sao trong sốc mất nước tiêu chảy, truyền dung dịch Ringer Lactat lại KHÔNG làm nặng thêm tình trạng toan lactic mà ngược lại giúp điều trị toan?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ringer Lactat phục hồi tưới máu mô → tế bào ngừng sinh acid lactic; đồng thời gan được cấp máu sẽ chuyển hóa muối Natri Lactat thành Bicarbonat với tỷ lệ 1:1.<br><br><b>💡 Lưu ý:</b><br>Muối Natri Lactat trong dịch truyền không phải là acid lactic tự do; chuyển hóa tại gan tiêu thụ H+ sinh HCO3-.",
        "extra": "Release lesson Mục 4.1: Nguyên tắc nền tảng điều trị toan chuyển hóa.",
        "tags": ["PED-11", "EBM", "Ringer-Lactat", "Toan-lactic"]
    },
    {
        "id": "PED11-E28",
        "track": "ebm",
        "type": "basic",
        "category": "PCCM 2025",
        "section": "E4",
        "front": "Khuyến cáo của Pediatric Critical Care Medicine 2025 về chỉ định bù Natri Bicarbonat trong toan chuyển hóa nhi khoa là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tuyệt đối không bù NaHCO3 thường quy; chỉ bù khi toan nặng đe dọa tính mạng (pH &lt; 7,10 hoặc HCO3- &lt; 8-10) kèm tụt huyết áp trơ với dịch và trơ thuốc vận mạch.<br><br><b>💡 Cơ sở chứng cứ:</b><br>Các nghiên cứu hồi cứu lớn chứng minh bù kiềm không cải thiện tỷ lệ sống sót mà gây nhiều biến chứng chuyển hóa nặng nề.",
        "extra": "Release lesson Mục 4.2: Khuyến cáo PCCM 2025.",
        "tags": ["PED-11", "EBM", "PCCM-2025", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-E29",
        "track": "ebm",
        "type": "cloze",
        "category": "Thực nghiệm Morgan 2026",
        "section": "E4",
        "text": "[EBM] Thử nghiệm thực nghiệm của Morgan RW et al. 2026 (PMID 42666620): tiêm tĩnh mạch NaHCO3 làm tăng vọt áp lực {{c1::PaCO2 trong máu}}, gây sụt giảm pH dịch não tủy nghịch thường và {{c1::hạ Canxi ion hóa máu cấp tính}} trong 10 phút đầu.",
        "extra": "PMID 42666620 (Morgan 2026). Cơ chế sinh lý bệnh thực nghiệm của biến chứng bù kiềm.",
        "tags": ["PED-11", "EBM", "PMID-42666620", "Morgan-2026"]
    },
    {
        "id": "PED11-E30",
        "track": "ebm",
        "type": "basic",
        "category": "Hạ Canxi ion hóa",
        "section": "E4",
        "front": "Tại sao tiêm Natri Bicarbonat nhanh lại dẫn tới hạ Canxi ion hóa máu cấp tính đe dọa ngừng tim?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khi pH máu tăng nhanh, các gốc acid trên Albumin nhả ion H+ ra, để lộ các vị trí tích điện âm gắn kết mạnh với ion Ca(2+) tự do → nồng độ Ca(2+) ion hóa sụt giảm đột ngột.<br><br><b>💡 Hậu quả:</b><br>Gây co giật tetany, tụt huyết áp nặng và ức chế sức co bóp cơ tim dẫn tới ngừng tim.",
        "extra": "Release lesson Mục 4.4: Biến chứng số 3.",
        "tags": ["PED-11", "EBM", "Ha-Canxi-mau", "Bien-chung-Bicarbonat"]
    },
    {
        "id": "PED11-E31",
        "track": "ebm",
        "type": "basic",
        "category": "Kết tủa Canxi",
        "section": "E4",
        "front": "Vì sao tuyệt đối KHÔNG ĐƯỢC tiêm dung dịch Canxi chung đường truyền tĩnh mạch với dung dịch Natri Bicarbonat?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ion Ca(2+) phản ứng ngay với HCO3- tạo thành kết tủa Calci Carbonat (CaCO3) màu trắng không tan làm tắc nghẽn đường truyền và hoại tử mạch máu.<br><br><b>💡 Nguyên tắc:</b><br>Bắt buộc phải dùng 2 đường truyền tĩnh mạch riêng biệt hoặc xả sạch dây truyền bằng NaCl 0,9% trước khi đổi thuốc.",
        "extra": "Release lesson Bẫy lâm sàng 9 & Mục 4.4.",
        "tags": ["PED-11", "EBM", "Ket-tua-Canxi", "Bien-chung-Bicarbonat"]
    },
    {
        "id": "PED11-E32",
        "track": "ebm",
        "type": "cloze",
        "category": "Dung dịch NaHCO3 8.4%",
        "section": "E4",
        "text": "[EBM] Dung dịch Natri Bicarbonat 8,4% có nồng độ Na+ và HCO3- là {{c1::1000 mEq/L}} (1 ml = 1 mEq), áp lực thẩm thấu lên tới {{c1::2000 mOsmol/L}} (gấp 7 lần huyết tương); bắt buộc phải pha loãng 1:4 với Glucose 5% trước khi truyền.",
        "extra": "Release lesson Mục 4.5: Bảng so sánh đặc tính dung dịch.",
        "tags": ["PED-11", "EBM", "NaHCO3-8.4%"]
    },
    {
        "id": "PED11-E33",
        "track": "ebm",
        "type": "cloze",
        "category": "Dung dịch Ringer Lactat",
        "section": "E4",
        "text": "[EBM] Dung dịch Ringer Lactat có nồng độ Na+ = {{c1::130 mEq/L}}, Cl- = {{c1::109 mEq/L}}, đệm Lactate = {{c1::28 mEq/L}}, áp lực thẩm thấu {{c1::273 mOsmol/L}} (đẳng trương); là lựa chọn hàng đầu hồi sức sốc mất nước toan chuyển hóa.",
        "extra": "Release lesson Mục 4.5: Bảng so sánh dung dịch.",
        "tags": ["PED-11", "EBM", "Ringer-Lactat"]
    },
    {
        "id": "PED11-E34",
        "track": "ebm",
        "type": "basic",
        "category": "Dung dịch NaCl 0.9%",
        "section": "E4",
        "front": "So sánh nồng độ Natri và Clo của NaCl 0,9% so với huyết tương và giải thích tại sao truyền nhiều gây toan chuyển hóa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>NaCl 0,9% có Na+ 154 và Cl- 154 mEq/L (cao hơn Clo huyết tương 100 mEq/L); truyền lượng lớn làm tăng Clo máu, thận tăng thải HCO3- giữ Clo dẫn đến toan chuyển hóa tăng Clo.<br><br><b>💡 Lưu ý:</b><br>Ringer Lactat cân bằng sinh lý hơn với Cl- 109 mEq/L nên ít gây toan tăng Clo.",
        "extra": "Release lesson Mục 4.5.",
        "tags": ["PED-11", "EBM", "NaCl-0.9%", "Toan-tang-Clo"]
    },
    {
        "id": "PED11-E35",
        "track": "ebm",
        "type": "cloze",
        "category": "Dung dịch NaHCO3 1.4%",
        "section": "E4",
        "text": "[EBM] Dung dịch Natri Bicarbonat 1,4% là dung dịch {{c1::đẳng trương}} chứa {{c1::167 mEq/L}} Na+ và 167 mEq/L HCO3- (áp lực thẩm thấu 334 mOsmol/L); 1 ml chứa xấp xỉ {{c1::0,167 mEq}} HCO3-.",
        "extra": "Release lesson Mục 4.5: Bảng so sánh dung dịch.",
        "tags": ["PED-11", "EBM", "NaHCO3-1.4%"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E5 XU TRI KIEM CHUYEN HOA, TOAN & KIEM HO HAP
    # =========================================================================
    {
        "id": "PED11-E36",
        "track": "ebm",
        "type": "basic",
        "category": "Hẹp môn vị điều trị",
        "section": "E5",
        "front": "Phác đồ hồi sức dịch trước phẫu thuật mở cơ môn vị ở trẻ nhũ nhi hẹp phì đại môn vị là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bù đủ thể tích bằng NaCl 0,9% pha thêm KCl (20 - 40 mEq/L sau khi trẻ đi tiểu được) với liều khoảng 150 ml/kg/ngày; chỉ chuyển mổ khi Cl- &gt; 100, HCO3- &lt; 30 và K+ &gt; 3,5.<br><br><b>💡 Lưu ý:</b><br>Tuyệt đối không mổ cấp cứu khi trẻ còn kiềm chuyển hóa nặng vì nguy cơ ngừng thở trong gây mê.",
        "extra": "PMID 40983691 (Hernanz-Perez 2026) & Mục 5.1.",
        "tags": ["PED-11", "EBM", "Hep-mon-vi", "PMID-40983691"]
    },
    {
        "id": "PED11-E37",
        "track": "ebm",
        "type": "cloze",
        "category": "Nghiên cứu Clo môn vị",
        "section": "E5",
        "text": "[EBM] Nghiên cứu tiến cứu trên 184 trẻ hẹp môn vị của Hernanz-Perez B et al. 2026 (PMID 40983691) chỉ ra: nồng độ Clo máu ban đầu &lt; {{c1::85 mEq/L}} là chỉ số dự báo độc lập kiềm chuyển hóa nặng đòi hỏi hồi sức dịch kéo dài trước mổ.",
        "extra": "PMID 40983691 (Hernanz-Perez 2026).",
        "tags": ["PED-11", "EBM", "PMID-40983691", "Hernanz-Perez-2026"]
    },
    {
        "id": "PED11-E38",
        "track": "ebm",
        "type": "basic",
        "category": "Chống chỉ định Bicarbonat",
        "section": "E5",
        "front": "Tại sao chống chỉ định tuyệt đối tiêm Natri Bicarbonat trong xử trí Toan hô hấp cấp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì phản ứng HCO3- + H+ → H2O + CO2; bệnh nhân toan hô hấp đang bị tắc nghẽn hoặc suy giảm thông khí không thể thải CO2, tiêm kiềm làm tích tụ thêm CO2 khiến trẻ ngạt thở tử vong.<br><br><b>💡 Nguyên tắc:</b><br>Cứu cánh duy nhất trong toan hô hấp là giải phóng đường thở và hỗ trợ thông khí (thở máy, CPAP, giãn phế quản).",
        "extra": "Release lesson Mục 5.2 & Bẫy lâm sàng 5.",
        "tags": ["PED-11", "EBM", "Toan-ho-hap", "Chong-chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-E39",
        "track": "ebm",
        "type": "cloze",
        "category": "Kiềm hô hấp xử trí",
        "section": "E5",
        "text": "[EBM] Xử trí kiềm hô hấp: khi thở máy cần {{c1::giảm tần số thở hoặc giảm thể tích lưu thông (Vt)}}; khi trẻ tự thở sốt cao cần hạ nhiệt độ và dùng thuốc giảm đau an thần để chấm dứt tình trạng tăng thông khí quá mức.",
        "extra": "Release lesson Mục 5.3: Xử trí Kiềm hô hấp.",
        "tags": ["PED-11", "EBM", "Kiem-ho-hap"]
    },
    {
        "id": "PED11-E40",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy thở oxy",
        "section": "E5",
        "front": "Vì sao thở oxy liều cao ở bệnh nhân toan hô hấp có thể tạo ra 'cảm giác an toàn giả tạo' nguy hiểm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Oxy liều cao duy trì SpO2 &gt; 95% nhưng che giấu tình trạng giảm thông khí phế nang; PaCO2 vẫn âm thầm tăng vọt làm bệnh nhi hôn mê toan hô hấp mà không được phát hiện kịp thời.<br><br><b>💡 Lưu ý:</b><br>SpO2 chỉ đo oxy hóa máu, không phản ánh thông khí phế nang; bắt buộc phải làm ABG để đo PaCO2.",
        "extra": "Release lesson Bẫy lâm sàng 11.",
        "tags": ["PED-11", "EBM", "Tho-oxy", "Bay-lam-sang"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E6 THEO DOI KHI MAU, ECG & ARTERIAL LINE
    # =========================================================================
    {
        "id": "PED11-E41",
        "track": "ebm",
        "type": "basic",
        "category": "Tần suất theo dõi ABG",
        "section": "E6",
        "front": "Tần suất xét nghiệm lại khí máu động mạch trong giai đoạn cấp cứu toan chuyển hóa nặng hoặc suy hô hấp tiến triển là bao lâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Xét nghiệm lại mỗi 1 - 2 giờ cho đến khi pH vượt trên 7,20 và huyết động ổn định; sau khi qua cơn nguy kịch kiểm tra mỗi 4 - 6 giờ kèm điện giải đồ.<br><br><b>💡 Lưu ý:</b><br>Theo dõi sát giúp phát hiện kịp thời hạ Kali và Canxi máu kịch phát do kiềm hóa máu.",
        "extra": "Release lesson Mục 6.1: Tần suất theo dõi khí máu động mạch.",
        "tags": ["PED-11", "EBM", "Theo-doi-ABG"]
    },
    {
        "id": "PED11-E42",
        "track": "ebm",
        "type": "cloze",
        "category": "ECG trong toan máu",
        "section": "E6",
        "text": "[EBM] Dấu hiệu điện tâm đồ (ECG) điển hình khi toan máu nặng (pH &lt; 7,20) kèm tăng Kali máu thứ phát gồm: sóng T {{c1::cao nhọn đối xứng}}, khoảng PR kéo dài, phức bộ QRS {{c1::giãn rộng}} và đe dọa rung thất ngừng tim.",
        "extra": "Release lesson Mục 6.2: Biến đổi ECG trong toan kiềm.",
        "tags": ["PED-11", "EBM", "ECG", "Toan-mau"]
    },
    {
        "id": "PED11-E43",
        "track": "ebm",
        "type": "basic",
        "category": "ECG trong kiềm máu",
        "section": "E6",
        "front": "Biến đổi điện tâm đồ điển hình trong kiềm máu nặng (pH &gt; 7,50) phản ánh tình trạng rối loạn điện giải nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Phản ánh Hạ Kali máu (sóng T dẹt, xuất hiện sóng U nổi bật, ST chênh xuống) và Hạ Canxi ion hóa (khoảng QT kéo dài, tăng nguy cơ xoắn đỉnh Torsades de Pointes).<br><br><b>💡 Lưu ý:</b><br>QTc kéo dài &gt; 0,44s ở trẻ lớn hoặc &gt; 0,46s ở nhũ nhi báo động nguy cơ ngừng tim.",
        "extra": "Release lesson Mục 6.2: Biến đổi ECG trong kiềm máu.",
        "tags": ["PED-11", "EBM", "ECG", "Kiem-mau"]
    },
    {
        "id": "PED11-E44",
        "track": "ebm",
        "type": "cloze",
        "category": "Monitor ECG",
        "section": "E6",
        "text": "[EBM] Bắt buộc gắn monitor theo dõi điện tim liên tục cho mọi bệnh nhi có toan chuyển hóa nặng với pH &lt; {{c1::7,15}} hoặc trong suốt quá trình truyền {{c1::Natri Bicarbonat}}.",
        "extra": "Release lesson Mục 6.2: Giám sát tim mạch liên tục.",
        "tags": ["PED-11", "EBM", "Monitor-ECG"]
    },
    {
        "id": "PED11-E45",
        "track": "ebm",
        "type": "basic",
        "category": "Arterial Line",
        "section": "E6",
        "front": "Chỉ định đặt đường truyền động mạch xâm lấn (Arterial Line) ở bệnh nhi cấp cứu hồi sức là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bệnh nhi sốc kháng dịch dùng vận mạch liều cao cần đo huyết áp liên tục (IBP); hoặc suy hô hấp nặng thở máy thông số cao cần lấy ABG nhiều lần (≥ 4 - 6 lần/24h).<br><br><b>💡 Lưu ý:</b><br>Đặt catheter giúp tránh chọc kim nhiều lần gây co thắt mạch, tụ máu và huyết khối tắc mạch chi.",
        "extra": "Release lesson Mục 6.3: Chỉ định đặt Arterial Line.",
        "tags": ["PED-11", "EBM", "Arterial-Line"]
    },
    {
        "id": "PED11-E46",
        "track": "ebm",
        "type": "cloze",
        "category": "Vị trí catheter động mạch",
        "section": "E6",
        "text": "[EBM] Vị trí ưu tiên hàng đầu để đặt catheter động mạch xâm lấn ở trẻ em là {{c1::động mạch quay}} ở cổ tay; vị trí lựa chọn thứ hai là {{c1::động mạch chày sau}} ở cổ chân.",
        "extra": "Release lesson Mục 6.3 & 1.4: An toàn mạch máu nhi khoa.",
        "tags": ["PED-11", "EBM", "Arterial-Line"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E7 LUU DO TOM TAT XU TRI NHANH
    # =========================================================================
    {
        "id": "PED11-E47",
        "track": "ebm",
        "type": "basic",
        "category": "Lưu đồ tóm tắt",
        "section": "E7",
        "front": "4 bước quyết định nhanh theo lưu đồ tóm tắt xử trí toan kiềm tại giường bệnh là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Đọc pH máu; 2) Xác định rối loạn tiên phát; 3) Phân loại toan chuyển hóa qua Anion Gap và Delta Gap; 4) Áp dụng nguyên tắc chỉ bù NaHCO3 khi pH &lt; 7,10 kèm tụt huyết áp.<br><br><b>💡 Lưu ý:</b><br>Lưu đồ giúp định hướng xử trí cấp cứu trong 60 giây đầu tại PICU.",
        "extra": "Release lesson Mục 7.1: Lưu đồ tóm tắt xử trí.",
        "tags": ["PED-11", "EBM", "Luu-do-xu-tri"]
    },
    {
        "id": "PED11-E48",
        "track": "ebm",
        "type": "cloze",
        "category": "Lưu đồ kiềm chuyển hóa",
        "section": "E7",
        "text": "[EBM] Khi kết quả ABG cho thấy Kiềm chuyển hóa (HCO3- &gt; 26 mEq/L, BE &gt; +2 mEq/L), biện pháp xử trí đầu tay là truyền {{c1::NaCl 0,9%}} kết hợp pha bù {{c1::Kali Clorid (KCl)}}.",
        "extra": "Release lesson Mục 7.1: Lưu đồ tóm tắt xử trí.",
        "tags": ["PED-11", "EBM", "Luu-do-xu-tri", "Kiem-chuyen-hoa"]
    },
    {
        "id": "PED11-E49",
        "track": "ebm",
        "type": "cloze",
        "category": "Lưu đồ bù kiềm",
        "section": "E7",
        "text": "[EBM] Trong xử trí cấp cứu toan chuyển hóa nặng, mục tiêu nồng độ HCO3- cần đạt sau bù kiềm là {{c1::12 - 15 mEq/L}}, truyền chậm 1/2 liều tính toán trong {{c1::2 - 4 giờ}}.",
        "extra": "Release lesson Mục 7.1: Lưu đồ tóm tắt xử trí.",
        "tags": ["PED-11", "EBM", "Luu-do-xu-tri", "Muc-tieu-bu-kiem"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E8 BOX DO NGUY CAP, 12 TIPS & CHECKPOINTS
    # =========================================================================
    {
        "id": "PED11-E50",
        "track": "ebm",
        "type": "basic",
        "category": "Box đỏ nguy cấp",
        "section": "E8",
        "front": "4 cảnh báo sống còn trong Box đỏ nguy cấp về sử dụng Natri Bicarbonat là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Tuyệt đối không tiêm tĩnh mạch nhanh trực tiếp; 2) Cấm dùng trong toan hô hấp; 3) Cấm đặt mục tiêu đưa HCO3- về 24 mEq/L ngay; 4) Luôn kiểm tra Kali máu trước và trong khi truyền.<br><br><b>💡 Lưu ý:</b><br>Vi phạm bất kỳ điều nào cũng có thể gây tử vong do ngừng tim hoặc phù não.",
        "extra": "Release lesson Phần 8: BOX ĐỎ NGUY CẤP.",
        "tags": ["PED-11", "EBM", "Box-do-nguy-cap"]
    },
    {
        "id": "PED11-E51",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy lâm sàng sốc",
        "section": "E8",
        "front": "Bẫy lâm sàng 1: Sai lầm phổ biến nhất của bác sĩ cấp cứu khi tiếp cận bệnh nhi sốc toan chuyển hóa là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vội vã tiêm ngay Natri Bicarbonat thay vì hồi sức dịch; bù đủ thể tích bằng Ringer Lactat mới là biện pháp chống toan tốt nhất vì toan máu tự hết khi mô được tưới máu.<br><br><b>💡 Cơ chế:</b><br>Tiêm kiềm khi chưa bù đủ dịch làm nặng thêm thiếu oxy mô và toan nội bào.",
        "extra": "Release lesson Mục 8.1: Bẫy lâm sàng 1.",
        "tags": ["PED-11", "EBM", "Bay-lam-sang", "Soc-toan"]
    },
    {
        "id": "PED11-E52",
        "track": "ebm",
        "type": "cloze",
        "category": "Bẫy hạ Kali máu",
        "section": "E8",
        "text": "[EBM] Bẫy lâm sàng 3: Bỏ quên kiểm tra Kali máu trước khi truyền kiềm. Kiềm máu kích hoạt bơm Na+/K+-ATPase kéo ion Kali chạy vào trong {{c1::nội bào}}, gây hạ Kali máu kịch phát và {{c1::loạn nhịp thất}} chết người.",
        "extra": "Release lesson Mục 8.1: Bẫy lâm sàng 3.",
        "tags": ["PED-11", "EBM", "Bay-lam-sang", "Ha-Kali-mau"]
    },
    {
        "id": "PED11-E53",
        "track": "ebm",
        "type": "basic",
        "category": "Toan niệu nghịch lý",
        "section": "E8",
        "front": "Bẫy lâm sàng 10: Vì sao nước tiểu có tính toan (pH &lt; 5,5) ở bệnh nhi hẹp môn vị lại gọi là 'nghịch lý'?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nghịch lý vì máu bệnh nhân đang bị kiềm nặng nhưng nước tiểu lại có tính toan; do thiếu hụt trầm trọng dịch và Kali, thận buộc phải ưu tiên giữ Na+ và bài xuất H+ vào nước tiểu.<br><br><b>💡 Hậu quả:</b><br>Càng bài xuất ion H+ ra nước tiểu thì kiềm máu càng trầm trọng hơn.",
        "extra": "Release lesson Mục 8.1: Bẫy lâm sàng 10 & Checkpoint 5.",
        "tags": ["PED-11", "EBM", "Bay-lam-sang", "Toan-nieu-nghich-ly"]
    },
    {
        "id": "PED11-E54",
        "track": "ebm",
        "type": "cloze",
        "category": "Bẫy mổ hẹp môn vị",
        "section": "E8",
        "text": "[EBM] Bẫy lâm sàng 12: Bỏ quên bù dịch NaCl 0,9% trước khi mổ hẹp môn vị. Bắt buộc phải điều chỉnh hết kiềm chuyển hóa và bù đủ Clo, Kali trước mổ vì kiềm máu gây {{c1::ức chế trung tâm hô hấp}} làm trẻ dễ ngừng thở khi gây mê.",
        "extra": "Release lesson Mục 8.1: Bẫy lâm sàng 12.",
        "tags": ["PED-11", "EBM", "Bay-lam-sang", "Hep-mon-vi"]
    },
    {
        "id": "PED11-E55",
        "track": "ebm",
        "type": "basic",
        "category": "Toan CSF nghịch thường",
        "section": "E8",
        "front": "Checkpoint 1: Tại sao tiêm tĩnh mạch nhanh Natri Bicarbonat có thể làm bệnh nhi lơ mơ và suy hô hấp nặng hơn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do khí CO2 sinh ra từ phản ứng đệm khuếch tán cực nhanh qua hàng rào máu não vào CSF làm toan dịch não tủy nghịch thường ức chế trung tâm hô hấp.<br><br><b>💡 Lưu ý:</b><br>Khí CO2 hòa tan trong mỡ qua màng não tức thì, trong khi ion HCO3- tích điện ngấm rất chậm.",
        "extra": "Release lesson Mục 8.2: Checkpoint 1.",
        "tags": ["PED-11", "EBM", "Checkpoint", "Toan-CSF-nghich-thuong"]
    },
    {
        "id": "PED11-E56",
        "track": "ebm",
        "type": "cloze",
        "category": "Cảnh báo NaHCO3 8.4%",
        "section": "E8",
        "text": "[EBM] Checkpoint 8: Tuyệt đối không được tiêm thẳng ống Natri Bicarbonat 8,4% nguyên chất qua tĩnh mạch ngoại vi vì áp lực thẩm thấu lên tới {{c1::2000 mOsmol/L}} gây viêm tắc tĩnh mạch, hoại tử mô dưới da và tăng thẩm thấu đột ngột gây {{c1::xuất huyết não}}.",
        "extra": "Release lesson Mục 8.2: Checkpoint 8.",
        "tags": ["PED-11", "EBM", "Checkpoint", "NaHCO3-8.4%"]
    },
    {
        "id": "PED11-E57",
        "track": "ebm",
        "type": "basic",
        "category": "Chỉ định Bicarbonat",
        "section": "E8",
        "front": "Checkpoint 6: Liệt kê đầy đủ 4 tình huống lâm sàng duy nhất có chỉ định tuyệt đối tiêm Natri Bicarbonat trong cấp cứu nhi khoa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Toan nặng pH &lt; 7,10 tụt HA trơ vận mạch; 2) Toan mất kiềm do tiêu chảy/RTA không hồi phục sau bù dịch; 3) Tăng Kali máu nặng dọa ngừng tim; 4) Ngộ độc thuốc chống trầm cảm 3 vòng (TCA).<br><br><b>💡 Lưu ý:</b><br>Ngoài 4 chỉ định này, bù Bicarbonat bị coi là lạm dụng và có hại.",
        "extra": "Release lesson Mục 8.2: Checkpoint 6.",
        "tags": ["PED-11", "EBM", "Checkpoint", "Chi-dinh-Bicarbonat"]
    },
    {
        "id": "PED11-E58",
        "track": "ebm",
        "type": "cloze",
        "category": "Mục tiêu cấp cứu",
        "section": "E8",
        "text": "[EBM] Checkpoint 3: Mục tiêu nồng độ Bicarbonat cần đạt trong pha cấp cứu toan chuyển hóa nặng là nâng lên mức an toàn {{c1::12 - 15 mEq/L}} (hoặc nâng pH đạt {{c1::7,20}}), tuyệt đối không đưa về mức bình thường 24 mEq/L.",
        "extra": "Release lesson Mục 8.2: Checkpoint 3.",
        "tags": ["PED-11", "EBM", "Checkpoint", "Muc-tieu-bu-kiem"]
    },
    {
        "id": "PED11-E59",
        "track": "ebm",
        "type": "cloze",
        "category": "Bẫy Albumin",
        "section": "E8",
        "text": "[EBM] Bẫy lâm sàng 7: Bỏ quên hiệu chỉnh Anion Gap khi trẻ bị giảm Albumin máu. Giảm mỗi 1 g/dL Albumin làm AG giảm giả tạo {{c1::2,5 mEq/L}}, có thể che giấu toan chuyển hóa tăng AG nguy hiểm.",
        "extra": "Release lesson Mục 8.1: Bẫy lâm sàng 7.",
        "tags": ["PED-11", "EBM", "Bay-lam-sang", "Anion-Gap"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E9 CAC CA LAM SANG THUC CHIEN
    # =========================================================================
    {
        "id": "PED11-E60",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng 1",
        "section": "E9",
        "front": "Case 1: Bé An 11 tháng (8,5 kg) tiêu chảy mất nước nặng, mạch 175, HA 65/40, thở Kussmaul 55 l/p; ABG: pH 7,12, PaCO2 18, HCO3- 6; Điện giải: Na 132, Cl 106. Biện luận rối loạn toan kiềm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Toan chuyển hóa nguyên phát (pH 7,12, HCO3- 6); bù trừ Winter phù hợp (PaCO2 dự đoán 17 ± 2); AG = 20 &gt; 16 (toan lactic do sốc); Delta ratio = 8/18 = 0,44 &lt; 0,8 → Toan chuyển hóa hỗn hợp (toan lactic + toan mất kiềm qua phân).<br><br><b>💡 Lưu ý:</b><br>Hồi sức dịch chống sốc bằng Ringer Lactat 20 ml/kg trong 20 phút đầu là then chốt.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 1.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-1", "Tieu-chay-soc"]
    },
    {
        "id": "PED11-E61",
        "track": "ebm",
        "type": "cloze",
        "category": "Ca lâm sàng 1",
        "section": "E9",
        "text": "[EBM] Case 1: Sau khi hồi sức dịch chống sốc cho bé An (8,5 kg), pH vẫn 7,12 và huyết áp thấp; tính liều NaHCO3 cần bù để nâng HCO3- từ 6 lên 12 mEq/L là {{c1::25,5 mEq}} ((12 - 6) × 0,5 × 8,5), truyền 1/2 liều ({{c1::78 ml}} dung dịch 1,4%) trong 2 giờ.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 1.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-1", "Lieu-Bicarbonat"]
    },
    {
        "id": "PED11-E62",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng 2",
        "section": "E9",
        "front": "Case 2: Bé Bình 5 tuần (4 kg) nôn vọt sữa không dịch mật 5 ngày, u môn vị quả ô liu; ABG: pH 7,56, PaCO2 48, HCO3- 42; Điện giải: Na 130, K 2,7, Cl 78. Biện luận khí máu và xử trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Kiềm chuyển hóa giảm Clo máu và hạ Kali máu do hẹp phì đại môn vị; PaCO2 48 phản ánh phổi giảm thông khí bù trừ.<br><br><b>💡 Xử trí:</b><br>Hoãn mổ cấp cứu; truyền NaCl 0,9% bù thâm hụt + duy trì (150 ml/kg/ngày) pha thêm KCl khi có nước tiểu; chỉ mổ Ramstedt khi Cl- &gt; 100, HCO3- &lt; 30, K+ &gt; 3,5.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 2.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-2", "Hep-mon-vi"]
    },
    {
        "id": "PED11-E63",
        "track": "ebm",
        "type": "cloze",
        "category": "Ca lâm sàng 2",
        "section": "E9",
        "text": "[EBM] Case 2: Chỉ số xét nghiệm mục tiêu cần đạt trước khi chuyển phẫu thuật mở cơ môn vị Ramstedt an toàn ở trẻ hẹp phì đại môn vị là: Clo máu &gt; {{c1::100 mEq/L}}, HCO3- &lt; {{c1::30 mEq/L}} và Kali máu &gt; {{c1::3,5 mEq/L}}.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 2.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-2", "Tieu-chuan-mo"]
    },
    {
        "id": "PED11-E64",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng 3",
        "section": "E9",
        "front": "Case 3: Bé Dũng 7 tuổi (22 kg) hen cấp nặng xịt 6 nhát salbutamol không đỡ; lơ mơ, SpO2 88%, lồng ngực im lặng; ABG: pH 7,22, PaCO2 62, HCO3- 25. Biện luận khí máu và xử trí cấp cứu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Toan hô hấp cấp nặng dọa ngừng thở do kiệt sức cơ hô hấp (PaCO2 tăng 62 mmHg khi đang khó thở dữ dội); thận chưa kịp bù trừ (HCO3- 25).<br><br><b>💡 Xử trí:</b><br>Không tiêm Bicarbonat! Khí dung Salbutamol + Ipratropium, tiêm Methylprednisolone + Magnesi Sulfat, chuẩn bị đặt nội khí quản thở máy xâm lấn ngay.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 3.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-3", "Hen-phe-quan"]
    },
    {
        "id": "PED11-E65",
        "track": "ebm",
        "type": "cloze",
        "category": "Ca lâm sàng 3",
        "section": "E9",
        "text": "[EBM] Case 3: Trong cơn hen phế quản cấp nặng ở trẻ em, dấu hiệu lâm sàng {{c1::lồng ngực im lặng (silent chest)}} đi kèm với chỉ số khí máu {{c1::PaCO2 > 45 mmHg}} là cảnh báo kiệt sức cơ thở tối khẩn đe dọa ngừng thở.",
        "extra": "Release lesson Mục 9: Ca lâm sàng 3.",
        "tags": ["PED-11", "EBM", "Ca-lam-sang-3", "Silent-chest"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E10 TAI LIEU THAM KHAO & XAC THUC CHUNG CU (PMID AUDIT)
    # =========================================================================
    {
        "id": "PED11-E66",
        "track": "ebm",
        "type": "basic",
        "category": "PMID Audit",
        "section": "E10",
        "front": "Nội dung nghiên cứu và ý nghĩa của Singhi S et al. 2022 (PMID 36755633) đối với bài học PED-11 là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nghiên cứu tiến cứu đa trung tâm PICU (n = 312) chứng minh 64,2% toan chuyển hóa trong tiêu chảy mất nước nặng là toan hỗn hợp (toan lactic tăng AG + toan mất HCO3- qua phân).<br><br><b>💡 Ứng dụng:</b><br>Xác lập cơ sở cho việc áp dụng chỉ số Delta Gap để bóc tách toan chuyển hóa hỗn hợp trong tiêu chảy cấp.",
        "extra": "PMID 36755633 (Singhi 2022).",
        "tags": ["PED-11", "EBM", "PMID-36755633", "Singhi-2022"]
    },
    {
        "id": "PED11-E67",
        "track": "ebm",
        "type": "basic",
        "category": "PMID Audit",
        "section": "E10",
        "front": "Kết quả chính của nghiên cứu Raymond TT et al. 2025 (PMID 40249229) về việc sử dụng Natri Bicarbonat trong ngừng tuần hoàn nhi khoa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nghiên cứu đoàn hệ 10 năm tại PICU (n = 1.156) cho thấy dùng sớm NaHCO3 không cải thiện tỷ lệ có lại tuần hoàn tự nhiên (aOR = 0,94; 95% CI: 0,72 - 1,22) và không tăng tỷ lệ sống sót.<br><br><b>💡 Ứng dụng:</b><br>Cung cấp bằng chứng mức độ cao chống chỉ định dùng NaHCO3 thường quy trong cấp cứu ngừng tim nhi.",
        "extra": "PMID 40249229 (Raymond 2025).",
        "tags": ["PED-11", "EBM", "PMID-40249229", "Raymond-2025"]
    },
    {
        "id": "PED11-E68",
        "track": "ebm",
        "type": "basic",
        "category": "PMID Audit",
        "section": "E10",
        "front": "Thử nghiệm của Morgan RW et al. 2026 (PMID 42666620) làm sáng tỏ cơ chế của những biến chứng nào sau tiêm NaHCO3?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chứng minh tiêm NaHCO3 làm tăng vọt PaCO2 máu, gây toan dịch não tủy nghịch thường và hạ Canxi ion hóa máu cấp tính trong 10 phút đầu.<br><br><b>💡 Ứng dụng:</b><br>Cung cấp bằng chứng thực nghiệm cho cơ chế 5 biến chứng nguy hiểm khi tiêm tĩnh mạch Bicarbonat.",
        "extra": "PMID 42666620 (Morgan 2026).",
        "tags": ["PED-11", "EBM", "PMID-42666620", "Morgan-2026"]
    },
    {
        "id": "PED11-E69",
        "track": "ebm",
        "type": "cloze",
        "category": "PMID Audit",
        "section": "E10",
        "text": "[EBM] Nghiên cứu PICU của Wang L et al. 2025 (PMID 41120922, n = 428) xác định: Anion Gap hiệu chỉnh theo Albumin máu (AG + 2,5 × [4,0 - Albumin]) đạt độ nhạy {{c1::88,5%}} phát hiện toan lactic so với chỉ {{c1::62,1%}} của AG chưa hiệu chỉnh.",
        "extra": "PMID 41120922 (Wang 2025).",
        "tags": ["PED-11", "EBM", "PMID-41120922", "Wang-2025"]
    },
    {
        "id": "PED11-E70",
        "track": "ebm",
        "type": "cloze",
        "category": "PMID Audit",
        "section": "E10",
        "text": "[EBM] Nghiên cứu trên 184 trẻ hẹp môn vị của Hernanz-Perez B et al. 2026 (PMID 40983691): nồng độ Clo máu ban đầu &lt; {{c1::85 mEq/L}} là yếu tố tiên lượng kiềm chuyển hóa nặng đòi hỏi hồi sức dịch kéo dài bằng dung dịch {{c1::NaCl 0,9%}}.",
        "extra": "PMID 40983691 (Hernanz-Perez 2026).",
        "tags": ["PED-11", "EBM", "PMID-40983691", "Hernanz-Perez-2026"]
    },
    {
        "id": "PED11-E71",
        "track": "ebm",
        "type": "cloze",
        "category": "PMID Audit",
        "section": "E10",
        "text": "[EBM] Nghiên cứu đoàn hệ 512 trẻ em của Lee J et al. 2023 (PMID 37511675): chỉ số khí máu ban đầu với pH &lt; {{c1::7,00}} và kiềm dư BE &lt; {{c1::-18 mEq/L}} là các yếu tố liên quan độc lập với tiên lượng tử vong trong ngừng tuần hoàn ngoài bệnh viện.",
        "extra": "PMID 37511675 (Lee 2023).",
        "tags": ["PED-11", "EBM", "PMID-37511675", "Lee-2023"]
    },
]
