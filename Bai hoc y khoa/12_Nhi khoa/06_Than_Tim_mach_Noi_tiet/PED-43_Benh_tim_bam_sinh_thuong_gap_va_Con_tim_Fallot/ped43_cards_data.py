# -*- coding: utf-8 -*-
"""PED-43 MASTER deck cards data: Track 1 barem YTB + Track 2 EBM.
Fields: id, track (barem_goc|ebm), type (basic|cloze), category, section,
front/back (basic) or text (cloze), extra, tags.
Section codes:
- B0-B18: 19 sections for PEDYTB scan textbook
- E0-E15: 16 sections for 2026-09-19 RELEASE lesson
Coverage gate requires >= 1 card per section (target >= 2 cards).
"""

cards_data = [
    # =========================================================================
    # TRACK 1: BAREM GỐC Y THÁI BÌNH (PEDYTB Scan)
    # =========================================================================

    # --- B0: Mục tiêu bài học (Trang 8) ---
    {
        "id": "PED43-B01",
        "track": "barem_goc",
        "type": "basic",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "front": "5 mục tiêu học tập của bài Tim bẩm sinh ở trẻ em theo giáo trình Y Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Phân loại tim bẩm sinh; 2) Đặc điểm chung shunt Trái - Phải; 3) Đặc điểm chung shunt Phải - Trái; 4) Đặc điểm tổn thương tắc nghẽn; 5) Triệu chứng, cận lâm sàng, chẩn đoán và điều trị 4 bệnh thường gặp: VSD, ASD, PDA, Fallot.<br><br><b>💡 Lưu ý:</b><br>Đi thi tự luận bám sát đúng 5 mục tiêu này để đạt trọn điểm.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục MỤC TIÊU).",
        "tags": ["PED-43", "Barem-goc", "Muc-tieu"]
    },
    {
        "id": "PED43-B02",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "text": "[Barem gốc] 4 bệnh tim bẩm sinh thường gặp được đặt trọng tâm trong mục tiêu học tập lâm sàng là: {{c1::thông liên thất}}, {{c1::thông liên nhĩ}}, {{c1::còn ống động mạch}} và {{c1::tứ chứng Fallot}}.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục tiêu 5).",
        "tags": ["PED-43", "Barem-goc", "Muc-tieu"]
    },

    # --- B1: Giới thiệu & Lịch sử (Trang 8) ---
    {
        "id": "PED43-B03",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Giới thiệu & Dịch tễ",
        "section": "B1",
        "text": "[Barem gốc] Tim bẩm sinh là dị tật phổ biến nhất lúc sinh, tuy rằng tỷ lệ tim bẩm sinh thấp khoảng {{c1::0,8% trẻ sống}}.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục I). Tương đương khoảng 8/1000 trẻ sinh sống.",
        "tags": ["PED-43", "Barem-goc", "Dich-te"]
    },
    {
        "id": "PED43-B04",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chẩn đoán tiền sản",
        "section": "B1",
        "text": "[Barem gốc] Phát hiện tim bẩm sinh có thể thực hiện bằng siêu âm vào {{c1::quý thứ hai}} của thời kỳ có thai và khám lâm sàng cho trẻ sau khi sinh.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục I).",
        "tags": ["PED-43", "Barem-goc", "Tien-san"]
    },
    {
        "id": "PED43-B05",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Lịch sử phẫu thuật",
        "section": "B1",
        "text": "[Barem gốc] Phẫu thuật tim lần đầu tiên được tiến hành ở {{c1::Đại học Minnesota}} vào năm {{c1::1950}} với máy tim phổi nhân tạo.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục I).",
        "tags": ["PED-43", "Barem-goc", "Lich-su"]
    },

    # --- B2: Phân loại tim bẩm sinh chung (Trang 8 - 9) ---
    {
        "id": "PED43-B06",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Phân loại TBS",
        "section": "B2",
        "text": "[Barem gốc] Đặc điểm nhóm tim bẩm sinh shunt Trái - Phải: máu đi từ {{c1::bên trái sang bên phải}}, lượng máu lên phổi {{c1::tăng}} và thường {{c1::không có tím}}.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục II.1).",
        "tags": ["PED-43", "Barem-goc", "Phan-loai"]
    },
    {
        "id": "PED43-B07",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hội chứng Eisenmenger",
        "section": "B2",
        "front": "Cơ chế xuất hiện tím muộn trong nhóm tim bẩm sinh shunt Trái - Phải theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tổn thương lớn không được phẫu thuật gây tắc nghẽn mạch phổi tiến triển, làm đảo ngược chiều shunt thành Phải - Trái (Hội chứng Eisenmenger).<br><br><b>💡 Lưu ý:</b><br>Khi đã có hội chứng Eisenmenger cố định, phẫu thuật đóng lỗ thông bị chống chỉ định tuyệt đối.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục II.1).",
        "tags": ["PED-43", "Barem-goc", "Eisenmenger"]
    },
    {
        "id": "PED43-B08",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Phân loại TBS",
        "section": "B2",
        "text": "[Barem gốc] Đặc điểm nhóm tim bẩm sinh shunt Phải - Trái: máu {{c1::chưa được oxy hóa}} đi vào {{c1::động mạch chủ}}, lượng máu tới phổi có thể {{c1::tăng hoặc giảm}}.",
        "extra": "Giáo trình Nhi khoa (Trang 8 - Mục II.2).",
        "tags": ["PED-43", "Barem-goc", "Phan-loai"]
    },
    {
        "id": "PED43-B09",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Phân loại TBS",
        "section": "B2",
        "text": "[Barem gốc] 4 tổn thương tắc nghẽn tại van và không tại van được phân loại gồm: tắc nghẽn đường ra thất trái (LVOTO), {{c1::hẹp eo động mạch chủ}}, {{c1::hẹp van động mạch phổi}} và {{c1::hẹp van động mạch chủ}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục II.3).",
        "tags": ["PED-43", "Barem-goc", "Phan-loai"]
    },

    # --- B3: Thông liên thất (VSD) (Trang 9) ---
    {
        "id": "PED43-B10",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Thông liên thất là dị tật phổ biến nhất của tim bẩm sinh, chiếm tới {{c1::20%}} tất cả các trường hợp tim bẩm sinh (trừ van ĐMC 2 lá và sa van 2 lá).",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD"]
    },
    {
        "id": "PED43-B11",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Phân loại vị trí VSD: phần quanh màng có thể đóng tự nhiên do sự bọc lại của {{c1::lá vách van ba lá}}; phần cơ hầu hết đóng trước {{c1::2 tuổi}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD"]
    },
    {
        "id": "PED43-B12",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thông liên thất",
        "section": "B3",
        "front": "Tại sao thông liên thất phần phễu và phần quanh màng có thể gây sa và hở van động mạch chủ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do lỗ thông nằm rất gần lá van động mạch chủ bên phải, dòng máu qua lỗ thông tạo hiệu ứng Venturi hút sa lá van vào lỗ thông, gây hở van ĐMC tiến triển.<br><br><b>💡 Lưu ý:</b><br>Biến chứng sa lá van ĐMC là chỉ định phẫu thuật đóng VSD sớm để bảo tồn van.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD", "Venturi"]
    },
    {
        "id": "PED43-B13",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Ở trẻ thông liên thất lỗ lớn, triệu chứng tăng lưu lượng phổi (thở nhanh, nhịp nhanh, không lên cân) xuất hiện khi áp lực mạch phổi giảm xuống vào lúc {{c1::6 – 8 tuần tuổi}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD"]
    },
    {
        "id": "PED43-B14",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Nghe tim trong VSD lớn có thể thấy tiếng thổi giữa tâm trương (rung tâm trương cơ năng) ở mỏm tim do {{c1::tăng lưu lượng máu qua van hai lá}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD"]
    },
    {
        "id": "PED43-B15",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Trên điện tâm đồ, thông liên thất phần {{c1::buồng nhận (Inlet)}} thường có biểu hiện {{c1::trục trái}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD", "ECG"]
    },
    {
        "id": "PED43-B16",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "B3",
        "text": "[Barem gốc] Thời điểm phẫu thuật VSD lớn: trẻ tăng lưu lượng phổi nhiều, không lên cân cần mổ lúc {{c1::1 – 4 tháng tuổi}}; hầu hết VSD lớn cần phẫu thuật lúc {{c1::6 – 9 tháng tuổi}}.",
        "extra": "Giáo trình Nhi khoa (Trang 9 - Mục III.3.1).",
        "tags": ["PED-43", "Barem-goc", "VSD", "Dieu-tri"]
    },

    # --- B4: Thông liên nhĩ (ASD) (Trang 10) ---
    {
        "id": "PED43-B17",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên nhĩ",
        "section": "B4",
        "text": "[Barem gốc] Thông liên nhĩ chiếm tỷ lệ {{c1::6 – 10%}} tim bẩm sinh, với tỷ lệ giới tính Nữ : Nam = {{c1::2 : 1}}.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.2).",
        "tags": ["PED-43", "Barem-goc", "ASD"]
    },
    {
        "id": "PED43-B18",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên nhĩ",
        "section": "B4",
        "text": "[Barem gốc] Thể thông liên nhĩ hay gặp nhất là {{c1::thông liên nhĩ thứ phát (Ostium secundum)}}, chiếm {{c1::60 – 70%}} các trường hợp thông liên nhĩ.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.2).",
        "tags": ["PED-43", "Barem-goc", "ASD"]
    },
    {
        "id": "PED43-B19",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên nhĩ",
        "section": "B4",
        "text": "[Barem gốc] Hai dạng khuyết vách nhĩ không được coi là thông liên nhĩ thực sự theo giáo trình là: {{c1::thể xoang tĩnh mạch (Sinus venosus)}} và {{c1::thể khuyết nóc xoang vành (Coronary sinus defect)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.2).",
        "tags": ["PED-43", "Barem-goc", "ASD"]
    },
    {
        "id": "PED43-B20",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thông liên nhĩ",
        "section": "B4",
        "front": "Dấu hiệu nghe tim kinh điển và bản chất tiếng thổi tâm thu trong thông liên nhĩ là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Dấu hiệu kinh điển: Tiếng tim thứ hai T₂ tách đôi cố định. Tiếng thổi tâm thu ở khoang liên sườn 2 bờ trái ức do tăng lưu lượng máu qua van động mạch phổi, KHÔNG PHẢI do dòng máu qua lỗ thông liên nhĩ.<br><br><b>💡 Lưu ý:</b><br>Chênh áp qua vách liên nhĩ rất thấp nên bản thân lỗ ASD không tự phát sinh tiếng thổi.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.2).",
        "tags": ["PED-43", "Barem-goc", "ASD", "Trieu-chung"]
    },
    {
        "id": "PED43-B21",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông liên nhĩ",
        "section": "B4",
        "text": "[Barem gốc] Trên điện tâm đồ, đa số ASD có trục phải dày thất phải, nhưng riêng thông liên nhĩ lỗ tiên phát lại có biểu hiện {{c1::trục trái}} và khử cực ngược chiều kim đồng hồ.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.2).",
        "tags": ["PED-43", "Barem-goc", "ASD", "ECG"]
    },

    # --- B5: Thông sàn nhĩ thất (AVSD) (Trang 10) ---
    {
        "id": "PED43-B22",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông sàn nhĩ thất",
        "section": "B5",
        "text": "[Barem gốc] Thông sàn nhĩ thất chiếm 4 – 5% tim bẩm sinh, và đặc biệt gặp ở {{c1::40%}} trẻ bị {{c1::hội chứng Down}}.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.3). Còn gọi là kênh nhĩ thất hoặc khuyết gối nội tâm mạc.",
        "tags": ["PED-43", "Barem-goc", "AVSD", "Down"]
    },
    {
        "id": "PED43-B23",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông sàn nhĩ thất",
        "section": "B5",
        "text": "[Barem gốc] Thông sàn nhĩ thất hoàn toàn bao gồm: {{c1::thông liên nhĩ tiền phát}} và {{c1::thông liên thất phần buồng nhận}}, kèm bất thường van nhĩ thất chung.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.3).",
        "tags": ["PED-43", "Barem-goc", "AVSD"]
    },
    {
        "id": "PED43-B24",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thông sàn nhĩ thất",
        "section": "B5",
        "text": "[Barem gốc] Thời điểm phẫu thuật cho thông sàn nhĩ thất (AVSD) là lúc trẻ {{c1::3 – 6 tháng tuổi}}.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.3). Cần theo dõi lâu dài vì 15% dẫn đến hở van nhĩ thất hoặc LVOTO.",
        "tags": ["PED-43", "Barem-goc", "AVSD", "Dieu-tri"]
    },

    # --- B6: Còn ống động mạch (PDA) (Trang 10 - 11) ---
    {
        "id": "PED43-B25",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "B6",
        "text": "[Barem gốc] Còn ống động mạch chiếm 9 – 12% tim bẩm sinh; tỷ lệ ở trẻ non tháng theo cân nặng: 500 – 999 g là {{c1::42%}}, 1000 – 1499 g là {{c1::21%}}, 1500 – 1750 g là {{c1::7%}}.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.4).",
        "tags": ["PED-43", "Barem-goc", "PDA", "Dich-te"]
    },
    {
        "id": "PED43-B26",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "B6",
        "text": "[Barem gốc] Tỷ lệ còn ống động mạch ở những trẻ sống trên vùng núi cao gấp {{c1::30 lần}} trẻ sống ở vùng đồng bằng.",
        "extra": "Giáo trình Nhi khoa (Trang 10 - Mục III.3.4). Do thiếu oxy mạn tính ở độ cao làm chậm co thắt đóng ống.",
        "tags": ["PED-43", "Barem-goc", "PDA"]
    },
    {
        "id": "PED43-B27",
        "track": "barem_goc",
        "type": "basic",
        "category": "Còn ống động mạch",
        "section": "B6",
        "front": "Đặc điểm mạch ngoại vi và cơ chế tiếng thổi nghe tim trong còn ống động mạch lớn là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Mạch nảy mạnh chìm sâu (mạch Corrigan) do tụt huyết áp tâm trương. Nghe tim có tiếng thổi liên tục ở khoang liên sườn dưới đòn trái do áp lực ĐMC luôn cao hơn ĐMP cả tâm thu và tâm trương.<br><br><b>💡 Lưu ý:</b><br>Ở sơ sinh và trẻ non tháng có thể chỉ nghe tiếng thổi tâm thu tương tự VSD do sức cản mạch phổi còn cao.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.4).",
        "tags": ["PED-43", "Barem-goc", "PDA", "Trieu-chung"]
    },
    {
        "id": "PED43-B28",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "B6",
        "text": "[Barem gốc] Biểu hiện tím trong Hội chứng Eisenmenger do còn ống động mạch đảo chiều shunt là {{c1::tím nửa dưới cơ thể (chân tím hơn tay)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.4). Do ống động mạch đổ vào ĐMC xuống sau nhánh dưới đòn trái.",
        "tags": ["PED-43", "Barem-goc", "PDA", "Eisenmenger"]
    },
    {
        "id": "PED43-B29",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "B6",
        "text": "[Barem gốc] Ở trẻ sơ sinh non tháng, ống động mạch có thể đóng bằng thuốc uống {{c1::Indomethacin}} hoặc {{c1::Ibuprofen}}; chuyển phẫu thuật nếu thất bại.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.4).",
        "tags": ["PED-43", "Barem-goc", "PDA", "Dieu-tri"]
    },
    {
        "id": "PED43-B30",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "B6",
        "text": "[Barem gốc] Ở trẻ lớn và người lớn, phương pháp điều trị còn ống động mạch lựa chọn là đóng bằng {{c1::coil hoặc dụng cụ (dù qua da)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.4).",
        "tags": ["PED-43", "Barem-goc", "PDA", "Dieu-tri"]
    },

    # --- B7: Bất thường tĩnh mạch phổi một phần (PAPVC) (Trang 11) ---
    {
        "id": "PED43-B31",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bất thường tĩnh mạch phổi",
        "section": "B7",
        "text": "[Barem gốc] PAPVC xảy ra khi có {{c1::≥ 1 (nhưng không phải tất cả)}} tĩnh mạch phổi nối với tĩnh mạch hệ thống hoặc nhĩ phải, chiếm tỷ lệ {{c1::≤ 1%}} tim bẩm sinh.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.5).",
        "tags": ["PED-43", "Barem-goc", "PAPVC"]
    },
    {
        "id": "PED43-B32",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hội chứng Scimitar",
        "section": "B7",
        "front": "Tổn thương giải phẫu của Hội chứng thanh gươm Thổ Nhĩ Kỳ (Scimitar syndrome) theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nối tĩnh mạch phổi dưới bên phải với tĩnh mạch chủ dưới (IVC), nằm trong bệnh cảnh bất thường tĩnh mạch phổi một phần.<br><br><b>💡 Lưu ý:</b><br>Biểu hiện lâm sàng thay đổi từ tăng áp phổi rất nặng ở sơ sinh đến không triệu chứng ở người lớn.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.5).",
        "tags": ["PED-43", "Barem-goc", "PAPVC", "Scimitar"]
    },
    {
        "id": "PED43-B33",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bất thường tĩnh mạch phổi",
        "section": "B7",
        "text": "[Barem gốc] Để chẩn đoán chính xác PAPVC ở người lớn khi siêu âm qua thành ngực hạn chế, cần sử dụng thêm: {{c1::siêu âm qua thực quản, CT hoặc MRI}}.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.5).",
        "tags": ["PED-43", "Barem-goc", "PAPVC", "Chan-doan"]
    },

    # --- B8: Tứ chứng Fallot & Cơn tím Fallot (Trang 11 - 12) ---
    {
        "id": "PED43-B34",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "B8",
        "text": "[Barem gốc] Tứ chứng Fallot chiếm 4 – 8% tim bẩm sinh, gồm 4 tổn thương: 1) Thông liên thất phần phễu lớn; 2) {{c1::Hẹp đường ra thất phải}}; 3) {{c1::Động mạch chủ cưỡi ngựa}}; 4) {{c1::Phì đại thất phải}}.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot", "Giai-phau"]
    },
    {
        "id": "PED43-B35",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "B8",
        "text": "[Barem gốc] Trong tứ chứng Fallot, bệnh nhân không có tím khi hẹp đường ra thất phải nhẹ được gọi là thể lâm sàng {{c1::Fallot hồng}}.",
        "extra": "Giáo trình Nhi khoa (Trang 11 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot"]
    },
    {
        "id": "PED43-B36",
        "track": "barem_goc",
        "type": "basic",
        "category": "Tứ chứng Fallot",
        "section": "B8",
        "front": "Bản chất tiếng thổi tâm thu nghe được trong tứ chứng Fallot xuất phát từ tổn thương nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tiếng thổi tâm thu ở cạnh ức trái trên do hẹp đường ra thất phải, KHÔNG PHẢI do dòng máu qua lỗ thông liên thất.<br><br><b>💡 Lưu ý:</b><br>Trong cơn tím nặng, tiếng thổi này nhỏ đi hoặc biến mất hoàn toàn vì máu không tống được lên phổi.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot", "Nghe-tim"]
    },
    {
        "id": "PED43-B37",
        "track": "barem_goc",
        "type": "basic",
        "category": "Cơn tím Fallot",
        "section": "B8",
        "front": "Cơ chế sinh bệnh của Cơn tím thiếu oxy cấp (Hypoxic spell / Tet spell) trong Fallot là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Xảy ra do co thắt cơ phễu đường ra thất phải làm giảm lượng máu lên phổi trầm trọng, đồng thời làm tăng mạnh dòng shunt Phải - Trái qua lỗ thông liên thất.<br><br><b>💡 Lưu ý:</b><br>Biểu hiện: đột ngột thở nhanh sâu, tăng tím tái, kích thích, có thể dẫn đến hôn mê, co giật và tắc mạch não.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Tet-spell", "Co-che"]
    },
    {
        "id": "PED43-B38",
        "track": "barem_goc",
        "type": "basic",
        "category": "Cơn tím Fallot",
        "section": "B8",
        "front": "Vì sao tư thế ngồi xổm (Squatting) hoặc ngực gối (Knee-chest) giúp cắt cơn tím ở trẻ Fallot?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Làm gập động mạch đùi, tăng sức cản ngoại vi (SVR), giảm dòng shunt Phải - Trái và ép máu từ thất phải vượt qua phễu hẹp lên động mạch phổi nhiều hơn.<br><br><b>💡 Lưu ý:</b><br>Đây là phản xạ bản năng tại giường quan trọng nhất phải thực hiện ngay lập tức.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Tet-spell", "Ngoi-xom"]
    },
    {
        "id": "PED43-B39",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Cấp cứu cơn tím",
        "section": "B8",
        "text": "[Barem gốc] Liều Morphin tiêm dưới da hoặc tiêm bắp trong cấp cứu cơn tím Fallot theo giáo trình là {{c1::0,1 mg/kg}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6). Tác dụng: ức chế trung tâm hô hấp, giảm kích thích, giãn phễu thất phải.",
        "tags": ["PED-43", "Barem-goc", "Tet-spell", "Cap-cuu"]
    },
    {
        "id": "PED43-B40",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Cấp cứu cơn tím",
        "section": "B8",
        "text": "[Barem gốc] Thuốc chẹn beta giao cảm tiêm tĩnh mạch chậm trong cấp cứu cơn tím Fallot để giảm co thắt đường ra thất phải là {{c1::Propranolol}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Tet-spell", "Cap-cuu"]
    },
    {
        "id": "PED43-B41",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Dự phòng cơn tím",
        "section": "B8",
        "text": "[Barem gốc] Dự phòng cơn tím Fallot tái phát bằng Propranolol đường uống với liều {{c1::1 – 2 mg/kg/ngày}} chia {{c1::2 – 4 lần}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot", "Du-phong"]
    },
    {
        "id": "PED43-B42",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "B8",
        "text": "[Barem gốc] Hình ảnh tim trên X-quang điển hình của tứ chứng Fallot là {{c1::hình chiếc ủng (coeur en sabot)}}, với mỏm tim hếch lên, cung ĐMP lõm và trường phổi sáng.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot", "X-quang"]
    },
    {
        "id": "PED43-B43",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "B8",
        "text": "[Barem gốc] Phẫu thuật triệt để Fallot (vá VSD và mở rộng đường ra thất phải) thường tiến hành lúc trẻ {{c1::4 – 6 tháng tuổi}}; phẫu thuật tạm thời là làm cầu nối {{c1::Blalock-Taussig cải tiến}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.6).",
        "tags": ["PED-43", "Barem-goc", "Fallot", "Phau-thuat"]
    },

    # --- B9: Teo tịt van động mạch phổi (PA-VSD & PA-IVS) (Trang 12 - 13) ---
    {
        "id": "PED43-B44",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Teo tịt van ĐMP",
        "section": "B9",
        "text": "[Barem gốc] Teo tịt van ĐMP kèm thông liên thất (PA-VSD) là dạng nặng nhất của tứ chứng Fallot, máu lên phổi phụ thuộc hoàn toàn vào {{c1::ống động mạch (PDA)}} hoặc {{c1::tuần hoàn bàng hệ chủ - phổi (MAPCAs)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.7).",
        "tags": ["PED-43", "Barem-goc", "PA-VSD"]
    },
    {
        "id": "PED43-B45",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Teo tịt van ĐMP",
        "section": "B9",
        "text": "[Barem gốc] Thuốc dùng để duy trì mở ống động mạch ngay sau sinh ở trẻ teo tịt van động mạch phổi là truyền tĩnh mạch {{c1::Prostaglandin E1 (PGE1)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 12 - Mục III.3.7).",
        "tags": ["PED-43", "Barem-goc", "PGE1"]
    },
    {
        "id": "PED43-B46",
        "track": "barem_goc",
        "type": "basic",
        "category": "Teo tịt van ĐMP",
        "section": "B9",
        "front": "Điểm khác biệt giải phẫu và hướng xử trí giữa PA-VSD và PA-IVS là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>PA-IVS có vách liên thất lành lặn nên thất phải bị thiểu sản nặng ở các mức độ; nếu có đường rò động mạch vành vào thất phải thì bắt buộc phải phẫu thuật kiểu Fontan cải tiến.<br><br><b>💡 Lưu ý:</b><br>PA-VSD có lỗ VSD giải áp cho thất phải nên thất phải phát triển tốt hơn và hướng tới sửa chữa triệt để.",
        "extra": "Giáo trình Nhi khoa (Trang 12-13 - Mục III.3.7 & III.3.8).",
        "tags": ["PED-43", "Barem-goc", "PA-IVS"]
    },

    # --- B10: Chuyển gốc động mạch (d-TGA) (Trang 13) ---
    {
        "id": "PED43-B47",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "text": "[Barem gốc] Trong d-TGA, động mạch chủ xuất phát từ {{c1::thất phải}} và động mạch phổi xuất phát từ {{c1::thất trái}}, tạo thành hai vòng tuần hoàn {{c1::song song}}.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9). Chiếm 4% tim bẩm sinh.",
        "tags": ["PED-43", "Barem-goc", "TGA", "Giai-phau"]
    },
    {
        "id": "PED43-B48",
        "track": "barem_goc",
        "type": "basic",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "front": "Điều kiện tiên quyết để một trẻ sơ sinh mắc d-TGA có thể sống sót sau sinh là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bắt buộc phải có các tổn thương phối hợp để pha trộn máu giữa hai vòng tuần hoàn: thông liên thất, thông liên nhĩ hoặc còn ống động mạch.<br><br><b>💡 Lưu ý:</b><br>Nếu không có trộn máu, máu giàu oxy quẩn quanh phổi và máu đen quẩn quanh cơ thể gây tử vong trong 24 giờ đầu.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9).",
        "tags": ["PED-43", "Barem-goc", "TGA", "Huyet-dong"]
    },
    {
        "id": "PED43-B49",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "text": "[Barem gốc] Khám tim ở trẻ sơ sinh mắc d-TGA đơn thuần thường nghe thấy tiếng thứ hai (T₂) {{c1::đơn độc}} ở van động mạch chủ.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9).",
        "tags": ["PED-43", "Barem-goc", "TGA", "Nghe-tim"]
    },
    {
        "id": "PED43-B50",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "text": "[Barem gốc] Hai biện pháp xử trí cấp cứu ban đầu cho sơ sinh d-TGA tím tái nặng là: truyền {{c1::PGE1}} giữ mở ống động mạch và phá vách liên nhĩ bằng bóng (thủ thuật {{c1::Rashkind}}).",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9).",
        "tags": ["PED-43", "Barem-goc", "TGA", "Cap-cuu"]
    },
    {
        "id": "PED43-B51",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "text": "[Barem gốc] Phẫu thuật lựa chọn hàng đầu cho d-TGA là {{c1::phẫu thuật chuyển gốc động mạch (Arterial Switch / Jatene)}}, tiến hành ngay trong {{c1::tuần đầu tiên sau sinh}}.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9). Trước khi áp lực thất trái thoái triển.",
        "tags": ["PED-43", "Barem-goc", "TGA", "Phau-thuat"]
    },
    {
        "id": "PED43-B52",
        "track": "barem_goc",
        "type": "basic",
        "category": "Chuyển gốc động mạch",
        "section": "B10",
        "front": "Nhược điểm lâu dài của phẫu thuật chuyển tầng nhĩ kinh điển (Senning, Mustard) ở bệnh nhân TGA khi trưởng thành là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tắc nghẽn đường về tĩnh mạch, rối loạn nhịp tim và suy chức năng thất phải muộn do thất phải phải đảm nhận gánh nặng bơm máu đại tuần hoàn suốt đời.<br><br><b>💡 Lưu ý:</b><br>Đó là lý do phẫu thuật Jatene (đưa thất trái về bơm hệ thống) đã thay thế hoàn toàn chuyển tầng nhĩ.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.9).",
        "tags": ["PED-43", "Barem-goc", "TGA", "Senning-Mustard"]
    },

    # --- B11: Thân chung động mạch (Truncus Arteriosus) (Trang 13) ---
    {
        "id": "PED43-B53",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thân chung động mạch",
        "section": "B11",
        "text": "[Barem gốc] Thân chung động mạch chiếm < 1% tim bẩm sinh, bao gồm 1 VSD phần phễu lớn và 1 thân chung cưỡi ngựa chia ra: {{c1::động mạch vành, động mạch phổi và động mạch chủ}}.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.10).",
        "tags": ["PED-43", "Barem-goc", "Truncus"]
    },
    {
        "id": "PED43-B54",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thân chung động mạch",
        "section": "B11",
        "text": "[Barem gốc] Thân chung động mạch hay kết hợp với {{c1::Hội chứng DiGeorge}} do mất đoạn nhiễm sắc thể {{c1::22q11}}.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.10).",
        "tags": ["PED-43", "Barem-goc", "Truncus", "DiGeorge"]
    },
    {
        "id": "PED43-B55",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thân chung động mạch",
        "section": "B11",
        "front": "Dấu hiệu nghe tim đặc trưng trong thân chung động mạch là gì và khi nào tiếng thổi tâm thu bị giảm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nghe thấy tiếng thổi tâm thu tống máu cạnh trái xương ức và tiếng click tống máu qua van thân chung; tiếng thổi tâm thu bị giảm cường độ khi có kèm hở van thân chung động mạch.<br><br><b>💡 Lưu ý:</b><br>Nếu kèm gián đoạn quai ĐMC sẽ mất mạch bẹn hai bên.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.10).",
        "tags": ["PED-43", "Barem-goc", "Truncus", "Nghe-tim"]
    },
    {
        "id": "PED43-B56",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thân chung động mạch",
        "section": "B11",
        "text": "[Barem gốc] Phẫu thuật triệt để thân chung động mạch (đặt Conduit nối RV với PA) phải tiến hành sớm trước khi trẻ {{c1::2 – 3 tháng tuổi}} để phòng bệnh lý tắc nghẽn mạch phổi cố định.",
        "extra": "Giáo trình Nhi khoa (Trang 13 - Mục III.3.10).",
        "tags": ["PED-43", "Barem-goc", "Truncus", "Phau-thuat"]
    },

    # --- B12: Bệnh Ebstein (Trang 14) ---
    {
        "id": "PED43-B57",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "B12",
        "text": "[Barem gốc] Bệnh Ebstein có đặc điểm giải phẫu là sự bám thấp bất thường của {{c1::lá vách và lá sau}} van ba lá về phía mỏm thất phải, dẫn đến {{c1::nhĩ hóa}} một phần thất phải.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.11). Gây hở nặng van ba lá.",
        "tags": ["PED-43", "Barem-goc", "Ebstein", "Giai-phau"]
    },
    {
        "id": "PED43-B58",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "B12",
        "text": "[Barem gốc] Dấu hiệu nghe tim điển hình của bệnh Ebstein gồm: {{c1::tiếng T₁ và T₂ tách đôi rộng}} và {{c1::tiếng ngựa phi nhĩ}}.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.11).",
        "tags": ["PED-43", "Barem-goc", "Ebstein", "Nghe-tim"]
    },
    {
        "id": "PED43-B59",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "B12",
        "text": "[Barem gốc] X-quang ngực trong Ebstein có bóng tim phải to khổng lồ hình {{c1::\"quả bóng bàn\" hoặc \"hình bình nước\"}}, phế trường phổi sáng giảm tưới máu.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.11).",
        "tags": ["PED-43", "Barem-goc", "Ebstein", "X-quang"]
    },
    {
        "id": "PED43-B60",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "B12",
        "text": "[Barem gốc] Bất thường điện tâm đồ đặc biệt ở 15% bệnh nhân Ebstein là {{c1::Hội chứng Wolff-Parkinson-White (WPW)}}, kèm sóng P khổng lồ kiểu dãy Himalaya ở DII.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.11).",
        "tags": ["PED-43", "Barem-goc", "Ebstein", "ECG", "WPW"]
    },
    {
        "id": "PED43-B61",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "B12",
        "text": "[Barem gốc] Phương pháp phẫu thuật tạo hình sửa van ba lá mang lại hiệu quả cao hiện nay trong bệnh Ebstein là {{c1::phương pháp Cone (Cone procedure)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.11).",
        "tags": ["PED-43", "Barem-goc", "Ebstein", "Phau-thuat"]
    },

    # --- B13: Bất thường tĩnh mạch phổi hoàn toàn (TAPVC) (Trang 14) ---
    {
        "id": "PED43-B62",
        "track": "barem_goc",
        "type": "cloze",
        "category": "TAPVC",
        "section": "B13",
        "text": "[Barem gốc] 4 thể giải phẫu của TAPVC gồm: thể trên tim (hay gặp nhất), {{c1::thể trong tim}}, {{c1::thể dưới tim}} và {{c1::thể hỗn hợp}}.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.12).",
        "tags": ["PED-43", "Barem-goc", "TAPVC"]
    },
    {
        "id": "PED43-B63",
        "track": "barem_goc",
        "type": "basic",
        "category": "TAPVC",
        "section": "B13",
        "front": "Vì sao bệnh nhân TAPVC bắt buộc phải có thông liên nhĩ (ASD) để duy trì sự sống?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Toàn bộ máu giàu oxy từ phổi đổ bất thường về nhĩ phải; nếu không có ASD máu không thể sang tim trái để tống vào đại tuần hoàn nuôi cơ thể.<br><br><b>💡 Lưu ý:</b><br>Bệnh nhân sống sót nhờ sự pha trộn máu hoàn toàn ở tầng nhĩ trước khi xuống thất.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.12).",
        "tags": ["PED-43", "Barem-goc", "TAPVC", "Huyet-dong"]
    },
    {
        "id": "PED43-B64",
        "track": "barem_goc",
        "type": "cloze",
        "category": "TAPVC",
        "section": "B13",
        "text": "[Barem gốc] Hình ảnh X-quang kinh điển trong TAPVC thể trên tim không tắc nghẽn là {{c1::\"hình người tuyết\" (Snowman sign)}} hoặc hình số 8.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.12).",
        "tags": ["PED-43", "Barem-goc", "TAPVC", "X-quang"]
    },
    {
        "id": "PED43-B65",
        "track": "barem_goc",
        "type": "cloze",
        "category": "TAPVC",
        "section": "B13",
        "text": "[Barem gốc] TAPVC thể {{c1::dưới tim}} thường gây tắc nghẽn tĩnh mạch phổi nặng nề, phù phổi cấp dữ dội ở sơ sinh cần {{c1::phẫu thuật cấp cứu tối khẩn}} với tử vong lên đến 40%.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.12).",
        "tags": ["PED-43", "Barem-goc", "TAPVC", "Cap-cuu"]
    },

    # --- B14: Teo tịt van ba lá (Tricuspid Atresia) (Trang 14) ---
    {
        "id": "PED43-B66",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Teo van ba lá",
        "section": "B14",
        "text": "[Barem gốc] Teo van ba lá chiếm 3% tim bẩm sinh; thất phải thường {{c1::thiểu sản nặng}}, trong khi thất trái {{c1::phì đại lớn}} gánh toàn bộ tuần hoàn.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.13).",
        "tags": ["PED-43", "Barem-goc", "Teo-van-3-la"]
    },
    {
        "id": "PED43-B67",
        "track": "barem_goc",
        "type": "basic",
        "category": "Teo van ba lá",
        "section": "B14",
        "front": "Dấu hiệu điện tâm đồ kinh điển khác biệt của teo van ba lá so với đa số các bệnh tim bẩm sinh có tím khác là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Trục trái và dày thất trái (trong khi hầu hết các bệnh tim bẩm sinh có tím khác đều có trục phải và dày thất phải).<br><br><b>💡 Lưu ý:</b><br>Gặp một trẻ sơ sinh tím tái có trục trái trên ĐTĐ phải nghĩ ngay đến teo van ba lá.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.13).",
        "tags": ["PED-43", "Barem-goc", "Teo-van-3-la", "ECG"]
    },
    {
        "id": "PED43-B68",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Teo van ba lá",
        "section": "B14",
        "text": "[Barem gốc] Máu từ nhĩ phải trong teo van ba lá bắt buộc phải qua {{c1::lỗ bầu dục hoặc thông liên nhĩ}} để sang nhĩ trái hòa trộn với máu tĩnh mạch phổi.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.13).",
        "tags": ["PED-43", "Barem-goc", "Teo-van-3-la"]
    },
    {
        "id": "PED43-B69",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Teo van ba lá",
        "section": "B14",
        "text": "[Barem gốc] Phẫu thuật đích cuối cùng cho teo van ba lá là {{c1::Phẫu thuật Fontan cải tiến}}, nối tĩnh mạch chủ vào ĐMP với tỷ lệ sống sót > 85% sau 10 năm.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.13).",
        "tags": ["PED-43", "Barem-goc", "Teo-van-3-la", "Fontan"]
    },

    # --- B15: Hội chứng thiểu sản thất trái (HLHS) (Trang 14 - 15) ---
    {
        "id": "PED43-B70",
        "track": "barem_goc",
        "type": "cloze",
        "category": "HLHS",
        "section": "B15",
        "text": "[Barem gốc] Hội chứng HLHS gồm: teo/hẹp nặng van 2 lá, teo/hẹp van ĐMC, {{c1::thất trái thiểu sản nặng}} và thường kèm {{c1::hẹp eo động mạch chủ}}.",
        "extra": "Giáo trình Nhi khoa (Trang 14 - Mục III.3.14).",
        "tags": ["PED-43", "Barem-goc", "HLHS"]
    },
    {
        "id": "PED43-B71",
        "track": "barem_goc",
        "type": "basic",
        "category": "HLHS",
        "section": "B15",
        "front": "Giải thích vì sao trẻ sơ sinh mắc HLHS rơi vào sốc tim trụy mạch tử vong khi ống động mạch đóng lại?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thất trái không hoạt động, toàn bộ đại tuần hoàn phụ thuộc vào thất phải bơm qua ống động mạch (PDA) vào ĐMC xuống và chảy ngược nuôi vành, não; khi PDA đóng, cơ thể mất hoàn toàn nguồn tưới máu dẫn đến sốc và toan nặng.<br><br><b>💡 Lưu ý:</b><br>Xử trí cấp cứu đầu tay bắt buộc là truyền tĩnh mạch liên tục PGE1 để mở lại ống động mạch.",
        "extra": "Giáo trình Nhi khoa (Trang 14-15 - Mục III.3.14).",
        "tags": ["PED-43", "Barem-goc", "HLHS", "Huyet-dong"]
    },
    {
        "id": "PED43-B72",
        "track": "barem_goc",
        "type": "cloze",
        "category": "HLHS",
        "section": "B15",
        "text": "[Barem gốc] Phẫu thuật tái tạo giai đoạn 1 trong tuần đầu sau sinh cho trẻ HLHS là {{c1::phẫu thuật Norwood}} (tạo hình quai ĐMC mới từ thân ĐMP và tạo nguồn cấp máu lên phổi qua BT shunt hoặc Sano).",
        "extra": "Giáo trình Nhi khoa (Trang 15 - Mục III.3.14).",
        "tags": ["PED-43", "Barem-goc", "HLHS", "Norwood"]
    },
    {
        "id": "PED43-B73",
        "track": "barem_goc",
        "type": "cloze",
        "category": "HLHS",
        "section": "B15",
        "text": "[Barem gốc] Giai đoạn 2 và 3 trong phẫu thuật tái tạo 3 giai đoạn cho HLHS lần lượt là: phẫu thuật {{c1::Glenn hai hướng}} (lúc 3–6 tháng) và phẫu thuật {{c1::Fontan}} (lúc 2–4 tuổi).",
        "extra": "Giáo trình Nhi khoa (Trang 15 - Mục III.3.14).",
        "tags": ["PED-43", "Barem-goc", "HLHS", "Fontan"]
    },

    # --- B16: Tắc nghẽn đường ra thất trái (LVOTO) & Hẹp van ĐMC (Trang 15 - 16) ---
    {
        "id": "PED43-B74",
        "track": "barem_goc",
        "type": "cloze",
        "category": "LVOTO",
        "section": "B16",
        "text": "[Barem gốc] Hẹp trên van động mạch chủ thường phối hợp với {{c1::Hội chứng Williams}} do bất thường nhiễm sắc thể số {{c1::7}}.",
        "extra": "Giáo trình Nhi khoa (Trang 15 - Mục III.3.15).",
        "tags": ["PED-43", "Barem-goc", "LVOTO", "Williams"]
    },
    {
        "id": "PED43-B75",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp van ĐMC",
        "section": "B16",
        "text": "[Barem gốc] Tỷ lệ van động mạch chủ hai lá (Bicuspid aortic valve) trong cộng đồng chiếm khoảng {{c1::2% dân số}}, có thể diễn tiến hẹp hoặc hở van khi lớn.",
        "extra": "Giáo trình Nhi khoa (Trang 15 - Mục III.3.15).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMC"]
    },
    {
        "id": "PED43-B76",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hẹp van ĐMC",
        "section": "B16",
        "front": "Đặc điểm của tiếng click tống máu trong hẹp van động mạch chủ giúp phân biệt với hẹp van động mạch phổi là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tiếng click tống máu của van ĐMC xuất hiện ngay sau T₁ và KHÔNG thay đổi theo chu kỳ hô hấp (trong khi click van ĐMP nhỏ đi khi hít vào).<br><br><b>💡 Lưu ý:</b><br>Nghe rõ nhất ở liên sườn 2 bờ phải xương ức lan lên động mạch cảnh hai bên cổ.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.15).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMC", "Click"]
    },
    {
        "id": "PED43-B77",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp van ĐMC",
        "section": "B16",
        "text": "[Barem gốc] Biện pháp cấp cứu sơ sinh hẹp van động mạch chủ nặng là {{c1::nong van bằng bóng qua da}}; ở trẻ lớn có thể phẫu thuật {{c1::Ross}} (thay van tự thân) hoặc thay van cơ học/sinh học.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.15).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMC", "Dieu-tri"]
    },

    # --- B17: Hẹp eo động mạch chủ (CoA) (Trang 16) ---
    {
        "id": "PED43-B78",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp eo ĐMC",
        "section": "B17",
        "text": "[Barem gốc] Hẹp eo động mạch chủ chiếm 5% tim bẩm sinh, hay gặp ở trẻ trai; ở trẻ gái rất hay phối hợp với {{c1::Hội chứng Turner (45,XO)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.16).",
        "tags": ["PED-43", "Barem-goc", "Hep-eo-DMC", "Turner"]
    },
    {
        "id": "PED43-B79",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp eo ĐMC",
        "section": "B17",
        "text": "[Barem gốc] Khoảng {{c1::70%}} trường hợp hẹp eo động mạch chủ có phối hợp với dị tật {{c1::van động mạch chủ hai lá}}.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.16).",
        "tags": ["PED-43", "Barem-goc", "Hep-eo-DMC"]
    },
    {
        "id": "PED43-B80",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hẹp eo ĐMC",
        "section": "B17",
        "front": "Dấu hiệu lâm sàng tim mạch đặc trưng nhất giúp chẩn đoán hẹp eo động mạch chủ ở trẻ lớn là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tăng huyết áp chi trên kết hợp huyết áp chi dưới thấp, chênh lệch huyết áp tay - chân > 20 mmHg; mạch đùi bắt yếu hoặc đến chậm so với mạch quay (Radio-femoral delay).<br><br><b>💡 Lưu ý:</b><br>Bắt mạch bẹn hai bên và đo huyết áp 4 chi là thao tác bắt buộc ở mọi trẻ suy tim hoặc tăng huyết áp.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.16).",
        "tags": ["PED-43", "Barem-goc", "Hep-eo-DMC", "Mach-ben"]
    },
    {
        "id": "PED43-B81",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp eo ĐMC",
        "section": "B17",
        "text": "[Barem gốc] Dấu hiệu X-quang kinh điển ở trẻ lớn mắc hẹp eo ĐMC là {{c1::\"khuyết bờ dưới các xương sườn\" (Rib notching / Dấu hiệu Roesler)}} do tuần hoàn bàng hệ động mạch liên sườn bào mòn xương.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.16).",
        "tags": ["PED-43", "Barem-goc", "Hep-eo-DMC", "X-quang"]
    },
    {
        "id": "PED43-B82",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp eo ĐMC",
        "section": "B17",
        "text": "[Barem gốc] Dấu hiệu quai động mạch chủ trên phim X-quang ngực thẳng gợi ý hẹp eo ĐMC là {{c1::dấu hiệu số 3 (Figure of 3 sign)}}.",
        "extra": "Giáo trình Nhi khoa (Trang 16 - Mục III.3.16).",
        "tags": ["PED-43", "Barem-goc", "Hep-eo-DMC", "X-quang"]
    },

    # --- B18: Hẹp van động mạch phổi (PS) (Trang 17) ---
    {
        "id": "PED43-B83",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp van ĐMP",
        "section": "B18",
        "text": "[Barem gốc] Hẹp van động mạch phổi chiếm 8% tim bẩm sinh, thường phối hợp với {{c1::Hội chứng Noonan}}.",
        "extra": "Giáo trình Nhi khoa (Trang 17 - Mục III.3.17).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMP", "Noonan"]
    },
    {
        "id": "PED43-B84",
        "track": "barem_goc",
        "type": "basic",
        "category": "Hẹp van ĐMP",
        "section": "B18",
        "front": "Tiếng click tống máu trong hẹp van động mạch phổi có đặc điểm thay đổi theo hô hấp như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tiếng click tống máu van ĐMP nhỏ đi hoặc biến mất khi hít vào (do hít vào làm tăng hồi lưu tĩnh mạch về tim phải, đẩy van mở sớm trước kỳ tâm thu).<br><br><b>💡 Lưu ý:</b><br>Đây là điểm mấu chốt phân biệt với tiếng click van động mạch chủ (không thay đổi theo hô hấp).",
        "extra": "Giáo trình Nhi khoa (Trang 17 - Mục III.3.17).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMP", "Click"]
    },
    {
        "id": "PED43-B85",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp van ĐMP",
        "section": "B18",
        "text": "[Barem gốc] Nghe tim trong hẹp van ĐMP: tiếng tim thứ hai (T₂) {{c1::tách đôi rộng}}, thành phần van ĐMP (P₂) {{c1::mờ hoặc mất}} trong trường hợp hẹp nặng.",
        "extra": "Giáo trình Nhi khoa (Trang 17 - Mục III.3.17).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMP", "Nghe-tim"]
    },
    {
        "id": "PED43-B86",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hẹp van ĐMP",
        "section": "B18",
        "text": "[Barem gốc] Biện pháp điều trị lựa chọn hàng đầu cho hẹp van động mạch phổi là {{c1::nong van bằng bóng qua da (Balloon pulmonary valvuloplasty)}}, thành công lâu dài ở {{c1::85%}} các trường hợp.",
        "extra": "Giáo trình Nhi khoa (Trang 17 - Mục III.3.17).",
        "tags": ["PED-43", "Barem-goc", "Hep-van-DMP", "Dieu-tri"]
    },

    # =========================================================================
    # TRACK 2: EBM HIỆN ĐẠI & LÂM SÀNG (RELEASE Lesson)
    # =========================================================================

    # --- E0: Tổng quan & Box an toàn cấp cứu (Mục 0) ---
    {
        "id": "PED43-E01",
        "track": "ebm",
        "type": "basic",
        "category": "Box an toàn",
        "section": "E0",
        "front": "Vì sao tuyệt đối CẤM đóng ống động mạch bằng Indomethacin hoặc Ibuprofen ở trẻ sơ sinh mắc tim bẩm sinh phụ thuộc ống?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ở các bệnh như HLHS, TGA chưa sửa, teo van ĐMP, coarctation nặng, ống động mạch là nguồn tưới máu duy nhất nuôi cơ thể hoặc lên phổi; đóng ống sẽ gây trụy mạch và tử vong ngay lập tức.<br><br><b>💡 Lưu ý:</b><br>Bắt buộc truyền tĩnh mạch liên tục Prostaglandin E1 để giữ mở ống động mạch khi nghi ngờ.",
        "extra": "Box đỏ an toàn (Mục 0 RELEASE). Cảnh báo khẩn cấp cấp cứu sơ sinh.",
        "tags": ["PED-43", "EBM", "Box-an-toan", "PGE1"]
    },
    {
        "id": "PED43-E02",
        "track": "ebm",
        "type": "basic",
        "category": "Box an toàn",
        "section": "E0",
        "front": "Tại sao tuyệt đối CẤM đè ép ngực hoặc ép trẻ nằm ngửa khi đang lên cơn tím thiếu oxy Fallot (Tet spell)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ép ngực hoặc nằm ngửa làm giảm hồi lưu tĩnh mạch về tim, kích thích trẻ khóc thét và tăng tiêu thụ oxy, làm trầm trọng thêm luồng shunt Phải - Trái và thiếu máu não.<br><br><b>💡 Lưu ý:</b><br>Bắt buộc đặt trẻ ở tư thế ngực gối (Knee-chest) hoặc bế gập hai đùi sát bụng trẻ.",
        "extra": "Box đỏ an toàn (Mục 0 RELEASE). Phản xạ tư thế sống còn trong Tet spell.",
        "tags": ["PED-43", "EBM", "Box-an-toan", "Tet-spell"]
    },
    {
        "id": "PED43-E03",
        "track": "ebm",
        "type": "basic",
        "category": "Box an toàn",
        "section": "E0",
        "front": "Vì sao Propranolol tiêm tĩnh mạch trong cơn tím Fallot bắt buộc phải tiêm rất chậm dưới monitor theo dõi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tiêm nhanh có thể gây nhịp chậm xoang kịch phát, block nhĩ thất hoàn toàn và ngừng tim đột ngột do ức chế thụ thể beta giao cảm cơ tim quá mức.<br><br><b>💡 Lưu ý:</b><br>Liều: 0,05–0,1 mg/kg tiêm tĩnh mạch chậm trong 5–10 phút dưới sự giám sát liên tục của monitor.",
        "extra": "Box đỏ an toàn (Mục 0 RELEASE). Quy tắc an toàn tim mạch.",
        "tags": ["PED-43", "EBM", "Box-an-toan", "Propranolol"]
    },
    {
        "id": "PED43-E04",
        "track": "ebm",
        "type": "basic",
        "category": "Box an toàn",
        "section": "E0",
        "front": "Vì sao chống chỉ định tuyệt đối phẫu thuật đóng lỗ thông tim khi bệnh nhân đã chuyển sang Hội chứng Eisenmenger cố định?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sức cản mạch phổi đã xơ hóa cố định, lỗ thông đóng vai trò van giải áp bảo vệ tâm thất; đóng lỗ thông sẽ gây suy thất cấp không thể đảo ngược và tử vong ngay trên bàn mổ.<br><br><b>💡 Lưu ý:</b><br>Bệnh nhân Eisenmenger chỉ còn chỉ định điều trị hạ áp phổi nội khoa hoặc ghép tim - phổi.",
        "extra": "Box đỏ an toàn (Mục 0 RELEASE). Chống chỉ định ngoại khoa kinh điển.",
        "tags": ["PED-43", "EBM", "Box-an-toan", "Eisenmenger"]
    },

    # --- E1: Định nghĩa & Dịch tễ học toàn cầu (Mục 1) ---
    {
        "id": "PED43-E05",
        "track": "ebm",
        "type": "cloze",
        "category": "Dịch tễ học",
        "section": "E1",
        "text": "[EBM] Nghiên cứu dịch tễ của Hoffman & Kaplan ước tính tỷ lệ mới mắc của các thể bệnh tim bẩm sinh nặng khoảng {{c1::8 trên 1.000 trẻ sinh sống}}.",
        "extra": "PMID: 12084585 (Hoffman JI, Kaplan S. J Am Coll Cardiol 2002).",
        "tags": ["PED-43", "EBM", "Dich-te", "PMID-12084585"]
    },
    {
        "id": "PED43-E06",
        "track": "ebm",
        "type": "cloze",
        "category": "Dịch tễ học",
        "section": "E1",
        "text": "[EBM] Tổng quan hệ thống và meta-analysis toàn cầu của van der Linde xác định tỷ lệ lưu hành lúc sinh của bệnh tim bẩm sinh là {{c1::9,1 trên 1.000 trẻ sinh sống}}.",
        "extra": "PMID: 22078432 (van der Linde D, et al. J Am Coll Cardiol 2011).",
        "tags": ["PED-43", "EBM", "Dich-te", "PMID-22078432"]
    },
    {
        "id": "PED43-E07",
        "track": "ebm",
        "type": "cloze",
        "category": "Khuyến cáo hướng dẫn",
        "section": "E1",
        "text": "[EBM] Hướng dẫn thực hành lâm sàng toàn diện cập nhật năm 2025 về quản lý tim bẩm sinh người lớn (ACHD) thay thế hướng dẫn 2018 là của hiệp hội {{c1::ACC/AHA}}.",
        "extra": "PMID: 41411480 (2025 ACC/AHA ACHD Guideline, J Am Coll Cardiol 2025).",
        "tags": ["PED-43", "EBM", "Guideline", "PMID-41411480"]
    },
    {
        "id": "PED43-E08",
        "track": "ebm",
        "type": "basic",
        "category": "Chuyển tiếp huyết động",
        "section": "E1",
        "front": "Ngay sau khi trẻ cất tiếng khóc chào đời, sự biến chuyển sinh lý nào diễn ra ở sức cản mạch phổi (PVR) và sức cản hệ thống (SVR)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khi phổi nở ra, sức cản mạch máu phổi (PVR) sụt giảm đột ngột; đồng thời tuần hoàn nhau thai bị kẹp cắt đứt làm sức cản hệ thống (SVR) tăng vọt.<br><br><b>💡 Lưu ý:</b><br>Sự thay đổi áp lực này phơi bày các luồng thông máu Trái - Phải và khởi động quá trình đóng ống động mạch sinh lý.",
        "extra": "Mục 0 & Mục 1.1 RELEASE.",
        "tags": ["PED-43", "EBM", "Huyet-dong", "So-sinh"]
    },
    {
        "id": "PED43-E09",
        "track": "ebm",
        "type": "basic",
        "category": "Phân loại huyết động",
        "section": "E1",
        "front": "Phân biệt 3 nhóm huyết động học tim bẩm sinh theo biểu hiện tím và lưu lượng máu lên phổi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Shunt Trái - Phải (không tím, tăng lưu lượng phổi: VSD, ASD, PDA); 2) Shunt Phải - Trái (có tím: giảm máu phổi như Fallot/teo van ĐMP, hoặc tăng máu phổi như TGA/Truncus); 3) Tắc nghẽn đường ra (không tím, cản trở cơ học: CoA, hẹp van ĐMC, hẹp van ĐMP).<br><br><b>💡 Lưu ý:</b><br>Đây là lưu đồ tiếp cận lâm sàng chuẩn mực tại giường bệnh.",
        "extra": "Mục 1.2 RELEASE.",
        "tags": ["PED-43", "EBM", "Phan-loai"]
    },

    # --- E2: Cơ chế sinh lý bệnh & Huyết động học chuyên sâu (Mục 2) ---
    {
        "id": "PED43-E10",
        "track": "ebm",
        "type": "basic",
        "category": "Sinh lý bệnh huyết động",
        "section": "E2",
        "front": "Theo định luật huyết động học, hai yếu tố nào quyết định chiều và lưu lượng dòng máu qua một lỗ thông tim bẩm sinh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Kích thước lỗ thông và tỷ số chênh lệch sức cản giữa sức cản mạch hệ thống (SVR) và sức cản mạch máu phổi (PVR).<br><br><b>💡 Lưu ý:</b><br>Dòng máu luôn ưu tiên chảy từ nơi có áp lực cao/sức cản cao sang nơi có áp lực thấp/sức cản thấp.",
        "extra": "Mục 2 RELEASE.",
        "tags": ["PED-43", "EBM", "Sinh-ly-benh", "PVR-SVR"]
    },
    {
        "id": "PED43-E11",
        "track": "ebm",
        "type": "basic",
        "category": "Hội chứng Eisenmenger",
        "section": "E2",
        "front": "Giải thích chuỗi cơ chế bệnh sinh dẫn đến Hội chứng Eisenmenger ở bệnh nhân shunt Trái - Phải lớn không điều trị?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Shunt Trái - Phải lớn tràn máu lên phổi → tăng áp tiểu động mạch phổi → phì đại lớp cơ trơn và nội mạc → xơ hóa cố định lòng mạch → PVR vượt SVR làm đảo shunt thành Phải - Trái gây tím tái vĩnh viễn.<br><br><b>💡 Lưu ý:</b><br>Khi đã đảo shunt cố định, phẫu thuật đóng lỗ thông bị chống chỉ định tuyệt đối vì gây suy thất cấp tử vong.",
        "extra": "Mục 2 RELEASE.",
        "tags": ["PED-43", "EBM", "Eisenmenger", "Co-che"]
    },
    {
        "id": "PED43-E12",
        "track": "ebm",
        "type": "basic",
        "category": "Suy tim huyết động",
        "section": "E2",
        "front": "Tại sao shunt Trái - Phải lưu lượng lớn kéo dài lại dẫn đến suy tim sung huyết theo định luật Frank-Starling?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Máu shunt sang tim phải lên phổi rồi dồn ngược về thất trái gây quá tải thể tích thất trái cuối tâm trương; khi thể tích vượt quá ngưỡng bù trừ của định luật Frank-Starling thì cơ tim suy giảm sức co bóp dẫn đến suy tim sung huyết.<br><br><b>💡 Lưu ý:</b><br>Thất trái là buồng tim bị quá tải thể tích trực tiếp nhất trong VSD và PDA lớn.",
        "extra": "Mục 2 RELEASE.",
        "tags": ["PED-43", "EBM", "Suy-tim", "Frank-Starling"]
    },
    {
        "id": "PED43-E13",
        "track": "ebm",
        "type": "basic",
        "category": "Còn ống động mạch",
        "section": "E2",
        "front": "Giải thích cơ chế vì sao ở trẻ sinh non có PDA lớn lại có nguy cơ cao bị biến chứng viêm ruột hoại tử (NEC)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hiện tượng \"cướp máu tâm trương\": dòng máu liên tục thoát nhanh từ động mạch chủ sang động mạch phổi trong thì tâm trương làm tụt huyết áp tâm trương hệ thống, dẫn đến thiếu máu tưới mạc treo ruột kéo dài.<br><br><b>💡 Lưu ý:</b><br>Tương tự, tưới máu não và thận cũng bị đe dọa do hiện tượng tụt huyết áp tâm trương này.",
        "extra": "Mục 2 (Ví dụ 4) RELEASE.",
        "tags": ["PED-43", "EBM", "PDA", "NEC", "Cuop-mau"]
    },
    {
        "id": "PED43-E14",
        "track": "ebm",
        "type": "basic",
        "category": "Chuyển gốc động mạch",
        "section": "E2",
        "front": "Giải thích cơ chế huyết động vì sao trong chuyển gốc đại động mạch (d-TGA) nếu không có sự pha trộn máu thì trẻ sẽ tử vong nhanh chóng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì hai vòng tuần hoàn hoạt động song song độc lập: máu giàu oxy tuần hoàn khép kín giữa tim trái và phổi, trong khi máu nghèo oxy tuần hoàn khép kín giữa tim phải và cơ thể → thiếu oxy mô toàn thân tối cấp.<br><br><b>💡 Lưu ý:</b><br>Lỗ thông liên nhĩ hoặc ống động mạch là chiếc cầu nối sống còn duy nhất cho phép máu giàu oxy sang đại tuần hoàn.",
        "extra": "Mục 2 (Ví dụ 3) RELEASE.",
        "tags": ["PED-43", "EBM", "TGA", "Tuan-hoan-song-song"]
    },

    # --- E3: Tiếp cận chẩn đoán lâm sàng 4 bước & Cận lâm sàng (Mục 3) ---
    {
        "id": "PED43-E15",
        "track": "ebm",
        "type": "basic",
        "category": "Tiếp cận lâm sàng",
        "section": "E3",
        "front": "Kể tên 4 bước tiếp cận chẩn đoán tim bẩm sinh tại giường theo khuyến cáo?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bước 1: Đánh giá tím trung ương hay ngoại vi; Bước 2: Đo SpO₂ đồng thời ở tay phải và chân; Bước 3: Bắt mạch và đo huyết áp 4 chi (so sánh mạch bẹn và mạch quay); Bước 4: Nghe tim có hệ thống (T₂, click, tiếng thổi).<br><br><b>💡 Lưu ý:</b><br>Luôn đo SpO₂ tay phải vì tay phải nhận máu trước vị trí ống động mạch (pre-ductal).",
        "extra": "Mục 3.1 RELEASE.",
        "tags": ["PED-43", "EBM", "Tiep-can", "Kham-lam-sang"]
    },
    {
        "id": "PED43-E16",
        "track": "ebm",
        "type": "basic",
        "category": "Nghiệm pháp Hyperoxia",
        "section": "E3",
        "front": "Cách tiến hành và tiêu chuẩn biện luận của Nghiệm pháp thở oxy 100% (Hyperoxia test) ở trẻ sơ sinh tím tái?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Cho thở oxy 100% qua mask kín có túi dự trữ trong 10–15 phút rồi đo PaO₂ khí máu: Nếu PaO₂ tăng vọt (> 150–200 mmHg) là do bệnh lý phổi; Nếu PaO₂ không vượt qua 100–150 mmHg khẳng định tim bẩm sinh có shunt Phải - Trái.<br><br><b>💡 Lưu ý:</b><br>Xét nghiệm nhanh tại giường giúp định hướng khẩn cấp giữa suy hô hấp sơ sinh và tim bẩm sinh tím.",
        "extra": "Mục 3.2 RELEASE.",
        "tags": ["PED-43", "EBM", "Hyperoxia-test", "Khi-mau"]
    },
    {
        "id": "PED43-E17",
        "track": "ebm",
        "type": "basic",
        "category": "Chẩn đoán hình ảnh",
        "section": "E3",
        "front": "Phương tiện cận lâm sàng nào là tiêu chuẩn vàng tuyệt đối để chẩn đoán xác định cấu trúc giải phẫu và huyết động tim bẩm sinh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Siêu âm tim Doppler màu qua thành ngực (TTE): xác định cấu trúc giải phẫu, kích thước lỗ thông, hướng luồng shunt, tính phân suất tống máu và đo chênh áp qua van.<br><br><b>💡 Lưu ý:</b><br>CT đa dãy hoặc MRI tim dùng bổ trợ khi cần đánh giá quai ĐMC, tĩnh mạch phổi hoặc bàng hệ MAPCAs.",
        "extra": "Mục 3.3 RELEASE.",
        "tags": ["PED-43", "EBM", "Sieu-am-tim", "Tieu-chuan-vang"]
    },
    {
        "id": "PED43-E18",
        "track": "ebm",
        "type": "cloze",
        "category": "Nhận diện tím",
        "section": "E3",
        "text": "[EBM] Tím trung ương được nhận diện tại giường khi thấy tím ở {{c1::niêm mạc miệng, lưỡi và kết mạc}} đi kèm với {{c1::SpO₂ giảm}}; trong khi tím ngoại vi chỉ ở đầu chi lạnh và niêm mạc vẫn hồng.",
        "extra": "Mục 3.1 & Checkpoint 3 RELEASE.",
        "tags": ["PED-43", "EBM", "Nhan-dien-tim"]
    },
    {
        "id": "PED43-E19",
        "track": "ebm",
        "type": "basic",
        "category": "Sàng lọc SpO2",
        "section": "E3",
        "front": "Tại sao đo SpO₂ sàng lọc tim bẩm sinh ở trẻ sơ sinh bắt buộc phải đo ở tay phải (pre-ductal) và một trong hai chân (post-ductal)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tay phải nhận máu từ thân cánh tay đầu trước chỗ đổ của ống động mạch; chân nhận máu sau ống động mạch. Sự chênh lệch SpO₂ (> 3%) giúp phát hiện tổn thương phụ thuộc ống hoặc đảo chiều shunt nửa dưới cơ thể.<br><br><b>💡 Lưu ý:</b><br>Ví dụ: hẹp eo ĐMC nặng hoặc PDA tăng áp phổi sẽ có SpO₂ chân thấp hơn tay phải rõ rệt.",
        "extra": "Mục 3.1 & Tip 2 RELEASE.",
        "tags": ["PED-43", "EBM", "SpO2-screening", "Pre-post-ductal"]
    },

    # --- E4: Thông liên thất (VSD) - Huyết động & Can thiệp (Mục 4) ---
    {
        "id": "PED43-E20",
        "track": "ebm",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "E4",
        "text": "[EBM] Tổng quan Minette & Sahn khẳng định: Thông liên thất là dị tật tim bẩm sinh phổ biến nhất, với biểu hiện lâm sàng phụ thuộc vào {{c1::kích thước lỗ thông}} và {{c1::sức cản mạch máu phổi (PVR)}}.",
        "extra": "PMID: 17101870 (Minette MS, Sahn DJ. Circulation 2006).",
        "tags": ["PED-43", "EBM", "VSD", "PMID-17101870"]
    },
    {
        "id": "PED43-E21",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên thất",
        "section": "E4",
        "front": "Vì sao trẻ mắc thông liên thất lớn thường không có triệu chứng lúc mới sinh mà đến 6–8 tuần tuổi mới xuất hiện suy tim thở nhanh bú kém?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ở sơ sinh, sức cản mạch phổi (PVR) còn cao tương đương sức cản hệ thống nên lượng máu shunt T-P rất ít. Đến 6–8 tuần tuổi, PVR giảm sinh lý làm chênh áp tăng vọt, luồng shunt T-P tràn ngập lên phổi gây suy tim sung huyết.<br><br><b>💡 Lưu ý:</b><br>Đây là lý do VSD lớn hiếm khi suy tim ngay tuần đầu sau sinh.",
        "extra": "Mục 4.2 RELEASE.",
        "tags": ["PED-43", "EBM", "VSD", "Sinh-ly-PVR"]
    },
    {
        "id": "PED43-E22",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên thất",
        "section": "E4",
        "front": "Phác đồ điều trị nội khoa suy tim sung huyết ở trẻ mắc thông liên thất lớn gồm những nhóm thuốc nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thuốc lợi tiểu quai (Furosemid) phối hợp kháng Aldosterone (Spironolacton) để giảm ứ huyết phổi, kết hợp thuốc giãn mạch ức chế men chuyển (Captopril) để giảm hậu gánh thất trái làm giảm dòng shunt.<br><br><b>💡 Lưu ý:</b><br>Đồng thời bắt buộc tăng đậm độ năng lượng khẩu phần ăn lên 120–150 kcal/kg/ngày.",
        "extra": "Mục 4.3 RELEASE.",
        "tags": ["PED-43", "EBM", "VSD", "Noi-khoa"]
    },
    {
        "id": "PED43-E23",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên thất",
        "section": "E4",
        "front": "Vì sao thông liên thất phần phễu (dưới van ĐMC) dù kích thước nhỏ vẫn có chỉ định can thiệp phẫu thuật sớm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do hiệu ứng Venturi của dòng phụt xoáy liên tục hút sa lá van động mạch chủ bên phải vào lỗ thông, gây biến dạng van và hở van động mạch chủ tiến triển không hồi phục.<br><br><b>💡 Lưu ý:</b><br>Xuất hiện sa lá van ĐMC là chỉ định phẫu thuật ngay không chờ đợi.",
        "extra": "Mục 4.1 RELEASE.",
        "tags": ["PED-43", "EBM", "VSD", "Venturi", "Ho-chu"]
    },
    {
        "id": "PED43-E24",
        "track": "ebm",
        "type": "cloze",
        "category": "Thông liên thất",
        "section": "E4",
        "text": "[EBM] Thời điểm phẫu thuật triệt để vá VSD lớn có tăng áp phổi là trước {{c1::6 – 9 tháng tuổi}} để ngăn ngừa tổn thương mạch máu phổi xơ hóa cố định không hồi phục (Eisenmenger).",
        "extra": "Mục 4.3 RELEASE.",
        "tags": ["PED-43", "EBM", "VSD", "Thoi-diem-mo"]
    },

    # --- E5: Thông liên nhĩ (ASD) - Giải phẫu & T2 tách đôi cố định (Mục 5) ---
    {
        "id": "PED43-E25",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên nhĩ",
        "section": "E5",
        "front": "Giải thích cơ chế sinh lý vì sao tiếng tim thứ hai T₂ tách đôi cố định (không thay đổi theo hô hấp) trong thông liên nhĩ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bình thường khi hít vào máu về thất phải tăng làm chậm đóng van ĐMP. Trong ASD, luồng shunt T-P liên tục cung cấp thể tích dồi dào cho thất phải cả thì hít vào và thở ra, khiến thời gian tống máu thất phải luôn kéo dài cố định.<br><br><b>💡 Lưu ý:</b><br>T₂ tách đôi cố định là dấu hiệu lâm sàng đặc hiệu nhất của ASD.",
        "extra": "Mục 5.2 RELEASE.",
        "tags": ["PED-43", "EBM", "ASD", "T2-tach-doi"]
    },
    {
        "id": "PED43-E26",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên nhĩ",
        "section": "E5",
        "front": "Tại sao tiếng thổi tâm thu nghe được ở khoang liên sườn 2 bờ trái ức trong ASD không phải là tiếng thổi qua vách liên nhĩ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chênh áp giữa hai tâm nhĩ rất nhỏ (chỉ vài mmHg) nên dòng máu qua lỗ ASD không tạo ra xoáy đủ lớn để phát thành tiếng; tiếng thổi thực chất là do tăng lưu lượng máu lớn tống qua van động mạch phổi bình thường (hẹp phổi cơ năng).<br><br><b>💡 Lưu ý:</b><br>Do đó lỗ ASD càng to thì tiếng thổi qua van ĐMP càng rõ.",
        "extra": "Mục 5.2 RELEASE.",
        "tags": ["PED-43", "EBM", "ASD", "Tieng-thoi-co-nang"]
    },
    {
        "id": "PED43-E27",
        "track": "ebm",
        "type": "basic",
        "category": "Thông liên nhĩ",
        "section": "E5",
        "front": "Biến đổi điện tâm đồ nào là dấu hiệu đặc trưng giúp phân biệt ASD lỗ tiên phát với ASD lỗ thứ phát?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>ASD lỗ thứ phát có trục phải và dày thất phải; trong khi ASD lỗ tiên phát có trục trái và khử cực ngược chiều kim đồng hồ (do khuyết gối nội tâm mạc làm thay đổi mạng lưới dẫn truyền).<br><br><b>💡 Lưu ý:</b><br>Dấu hiệu trục trái ở trẻ nghi ngờ ASD gợi ý ngay thể tiên phát / kênh nhĩ thất.",
        "extra": "Mục 5.2 & Checkpoint 2 RELEASE.",
        "tags": ["PED-43", "EBM", "ASD", "ECG", "Phan-biet"]
    },
    {
        "id": "PED43-E28",
        "track": "ebm",
        "type": "cloze",
        "category": "Thông liên nhĩ",
        "section": "E5",
        "text": "[EBM] Thời điểm can thiệp bít dù qua da (Amplatzer) lý tưởng cho trẻ thông liên nhĩ lỗ thứ phát là lúc trẻ {{c1::3 – 5 tuổi}} trước khi trẻ đến tuổi đi học.",
        "extra": "Mục 5.3 & Bảng 9.1 RELEASE.",
        "tags": ["PED-43", "EBM", "ASD", "Bit-du"]
    },

    # --- E6: Còn ống động mạch (PDA) - Cơ chế & Đóng ống (Mục 6) ---
    {
        "id": "PED43-E29",
        "track": "ebm",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "E6",
        "text": "[EBM] Tổng quan hệ thống Cochrane của Ohlsson khẳng định: {{c1::Ibuprofen}} có hiệu quả đóng ống động mạch tương đương {{c1::indomethacin}} ở trẻ sơ sinh non tháng với ít tác dụng không mong muốn trên thận và tiêu hóa hơn.",
        "extra": "PMID: 30264852 (Ohlsson A, Walia R, Shah SS. Cochrane Database Syst Rev 2018).",
        "tags": ["PED-43", "EBM", "PDA", "Cochrane", "PMID-30264852"]
    },
    {
        "id": "PED43-E30",
        "track": "ebm",
        "type": "basic",
        "category": "Còn ống động mạch",
        "section": "E6",
        "front": "Giải thích cơ chế sinh lý tạo nên dấu hiệu mạch nảy mạnh chìm sâu (mạch Corrigan) trong còn ống động mạch lớn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tâm thu thất trái tống lượng máu lớn bù trừ vào ĐMC làm áp lực tâm thu tăng cao; tâm trương máu lập tức thoát nhanh sang ĐMP qua ống thông làm huyết áp tâm trương tụt sâu → chênh lệch áp lực mạch mở rộng tạo mạch Corrigan.<br><br><b>💡 Lưu ý:</b><br>Dấu hiệu này rất dễ nhận biết bằng bắt mạch quay hoặc mạch bẹn ở trẻ sơ sinh.",
        "extra": "Mục 6.2 RELEASE.",
        "tags": ["PED-43", "EBM", "PDA", "Mach-Corrigan"]
    },
    {
        "id": "PED43-E31",
        "track": "ebm",
        "type": "basic",
        "category": "Còn ống động mạch",
        "section": "E6",
        "front": "Giải thích cơ chế vì sao trong hội chứng Eisenmenger do PDA lại xuất hiện tím chuyên biệt ở nửa dưới cơ thể (chân tím hơn tay)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Lỗ đổ của ống động mạch vào ĐMC nằm sau chỗ xuất phát của động mạch dưới đòn trái nuôi chi trên. Khi đảo shunt P-T, máu đen từ ĐMP qua PDA đổ thẳng vào ĐMC xuống nuôi nửa dưới cơ thể, trong khi đầu và tay phải vẫn nhận máu đỏ từ quai ĐMC.<br><br><b>💡 Lưu ý:</b><br>Đây là dấu hiệu lâm sàng độc nhất vô nhị chỉ có ở PDA đảo shunt.",
        "extra": "Mục 6.2 RELEASE.",
        "tags": ["PED-43", "EBM", "PDA", "Tim-chuyen-biet"]
    },
    {
        "id": "PED43-E32",
        "track": "ebm",
        "type": "basic",
        "category": "Còn ống động mạch",
        "section": "E6",
        "front": "Thuốc đóng ống động mạch bằng ức chế tổng hợp Prostaglandin có hiệu quả ở lứa tuổi nào và cơ chế tác dụng là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chỉ có hiệu quả ở trẻ sơ sinh non tháng trong những tuần đầu đời vì tế bào cơ trơn thành ống còn khả năng đáp ứng co thắt khi bị ức chế enzym Cyclooxygenase làm giảm nồng độ Prostaglandin nội sinh.<br><br><b>💡 Lưu ý:</b><br>Ở trẻ đủ tháng và trẻ lớn, cấu trúc ống đã xơ hóa không còn đáp ứng với thuốc, bắt buộc can thiệp dù hoặc phẫu thuật.",
        "extra": "Mục 6.3 & Tip 5 RELEASE.",
        "tags": ["PED-43", "EBM", "PDA", "Dong-ong-thuoc"]
    },
    {
        "id": "PED43-E33",
        "track": "ebm",
        "type": "cloze",
        "category": "Còn ống động mạch",
        "section": "E6",
        "text": "[EBM] Liệu trình đóng ống động mạch bằng Ibuprofen đường tĩnh mạch chuẩn mực ở trẻ sơ sinh non tháng gồm {{c1::3 liều}} dùng cách nhau {{c1::24 giờ}} (liều đầu 10 mg/kg, hai liều sau 5 mg/kg).",
        "extra": "Mục 12 (Case 2) RELEASE & Cochrane 2018.",
        "tags": ["PED-43", "EBM", "PDA", "Ibuprofen-dose"]
    },

    # --- E7: Tứ chứng Fallot (TOF) & Cấp cứu Cơn tím kịch phát (Mục 7) ---
    {
        "id": "PED43-E34",
        "track": "ebm",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "E7",
        "text": "[EBM] Tổng quan Orphanet của Bailliard & Anderson xác định tứ chứng Fallot bao gồm 4 dị tật kinh điển: {{c1::thông liên thất}}, {{c1::hẹp đường ra thất phải}}, {{c1::động mạch chủ cưỡi ngựa}} và {{c1::phì đại thất phải}}.",
        "extra": "PMID: 19144126 (Bailliard F, Anderson RH. Orphanet J Rare Dis 2009).",
        "tags": ["PED-43", "EBM", "Fallot", "PMID-19144126"]
    },
    {
        "id": "PED43-E35",
        "track": "ebm",
        "type": "cloze",
        "category": "Tứ chứng Fallot",
        "section": "E7",
        "text": "[EBM] Tổng quan của Apitz trên tạp chí Lancet khẳng định: Những tiến bộ trong chẩn đoán và phẫu thuật đã giúp {{c1::hầu hết trẻ}} sinh ra mắc tứ chứng Fallot sống sót đến {{c1::tuổi trưởng thành}}.",
        "extra": "PMID: 19683809 (Apitz C, Webb GD, Redington AN. Lancet 2009).",
        "tags": ["PED-43", "EBM", "Fallot", "PMID-19683809"]
    },
    {
        "id": "PED43-E36",
        "track": "ebm",
        "type": "basic",
        "category": "Cơn tím Fallot",
        "section": "E7",
        "front": "Tại sao tiếng thổi tâm thu trong tứ chứng Fallot lại đột ngột nhỏ đi hoặc biến mất hoàn toàn khi trẻ rơi vào cơn tím cấp (Tet spell)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Cơ phễu đường ra thất phải co thắt cực độ cắt đứt gần như hoàn toàn lưu lượng máu lên động mạch phổi; không còn dòng máu tống qua chỗ hẹp phễu nên tiếng thổi tâm thu biến mất.<br><br><b>💡 Lưu ý:</b><br>Tiếng thổi tim biến mất là dấu hiệu cảnh báo cơn tím đang ở mức độ tối nguy kịch.",
        "extra": "Mục 7.3 & Tip 12 RELEASE.",
        "tags": ["PED-43", "EBM", "Tet-spell", "Tieng-thoi-bien-mat"]
    },
    {
        "id": "PED43-E37",
        "track": "ebm",
        "type": "basic",
        "category": "Cấp cứu cơn tím",
        "section": "E7",
        "front": "Trình bày thứ tự 6 bước cấp cứu xử trí cơn tím Fallot kịch phát tại giường?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Tư thế ngực gối (Knee-chest) ngay lập tức; 2) Thở oxy 100% qua mask kín; 3) Tiêm Morphine sulfate 0,1 mg/kg SC/IM; 4) Truyền dịch NaCl 0,9% 10–15 mL/kg tĩnh mạch nhanh; 5) Tiêm TM chậm Propranolol 0,05–0,1 mg/kg trong 5–10 phút; 6) Natri bicarbonat nếu toan nặng.<br><br><b>💡 Lưu ý:</b><br>Thuộc nằm lòng thứ tự này để cấp cứu trong vòng 3 phút đầu.",
        "extra": "Mục 7.3 Lưu đồ cấp cứu RELEASE.",
        "tags": ["PED-43", "EBM", "Tet-spell", "Cap-cuu-6-buoc"]
    },
    {
        "id": "PED43-E38",
        "track": "ebm",
        "type": "basic",
        "category": "Cấp cứu cơn tím",
        "section": "E7",
        "front": "Tác dụng điều trị của Morphine sulfate trong cấp cứu cơn tím Fallot là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ức chế trung tâm hô hấp làm giảm nhịp thở nhanh sâu, trấn tĩnh an thần trẻ giúp cắt đứt phản xạ tăng tiết Catecholamine giao cảm, từ đó làm giãn cơ phễu đường ra thất phải.<br><br><b>💡 Lưu ý:</b><br>Liều chuẩn: 0,1 mg/kg tiêm dưới da hoặc tiêm bắp.",
        "extra": "Mục 7.3 RELEASE.",
        "tags": ["PED-43", "EBM", "Tet-spell", "Morphine"]
    },
    {
        "id": "PED43-E39",
        "track": "ebm",
        "type": "cloze",
        "category": "Cấp cứu cơn tím",
        "section": "E7",
        "text": "[EBM] Liều truyền dịch muối đẳng trương NaCl 0,9% trong cấp cứu cơn tím Fallot là {{c1::10 – 15 mL/kg}} truyền tĩnh mạch nhanh để tăng tiền gánh thất phải và chống cô đặc máu.",
        "extra": "Mục 7.3 RELEASE.",
        "tags": ["PED-43", "EBM", "Tet-spell", "Truyen-dich"]
    },
    {
        "id": "PED43-E40",
        "track": "ebm",
        "type": "cloze",
        "category": "Phẫu thuật Fallot",
        "section": "E7",
        "text": "[EBM] Thời điểm vàng phẫu thuật sửa chữa toàn bộ triệt để cho trẻ mắc tứ chứng Fallot là lúc {{c1::4 – 6 tháng tuổi}}.",
        "extra": "Mục 7.4 & Bảng 9.1 RELEASE.",
        "tags": ["PED-43", "EBM", "Fallot", "Thoi-diem-mo"]
    },

    # --- E8: Các bệnh tim bẩm sinh phức tạp khác (Mục 8) ---
    {
        "id": "PED43-E41",
        "track": "ebm",
        "type": "cloze",
        "category": "Chuyển gốc động mạch",
        "section": "E8",
        "text": "[EBM] Tổng quan của Villafañe trên JACC khẳng định: Phẫu thuật chuyển gốc động mạch Jatene đã {{c1::thay thế hoàn toàn}} phẫu thuật chuyển tầng nhĩ trong điều trị d-TGA, giúp bệnh nhân sống sót đến tuổi trưởng thành.",
        "extra": "PMID: 25082585 (Villafañe J, et al. J Am Coll Cardiol 2014).",
        "tags": ["PED-43", "EBM", "TGA", "Jatene", "PMID-25082585"]
    },
    {
        "id": "PED43-E42",
        "track": "ebm",
        "type": "basic",
        "category": "Chuyển gốc động mạch",
        "section": "E8",
        "front": "Tại sao phẫu thuật Jatene (Arterial switch) cho trẻ chuyển gốc đại động mạch (d-TGA) bắt buộc phải tiến hành trong tuần đầu sau sinh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì sau sinh sức cản mạch phổi giảm làm áp lực buồng thất trái tụt giảm nhanh; nếu mổ muộn sau tuần đầu cơ thất trái sẽ bị thoái triển không còn đủ sức gánh áp lực đại tuần hoàn hệ thống.<br><br><b>💡 Lưu ý:</b><br>Mổ sau tuần đầu đòi hỏi phải luyện tập thất trái phức tạp trước mổ.",
        "extra": "Mục 8.1 RELEASE.",
        "tags": ["PED-43", "EBM", "TGA", "Jatene", "Thoi-diem-vang"]
    },
    {
        "id": "PED43-E43",
        "track": "ebm",
        "type": "basic",
        "category": "HLHS",
        "section": "E8",
        "front": "Trình bày quy trình phẫu thuật tái tạo 3 giai đoạn hướng tới tuần hoàn Fontan ở trẻ mắc Hội chứng thiểu sản thất trái (HLHS)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Giai đoạn 1 (tuần đầu sau sinh): Phẫu thuật Norwood tạo đường tống máu đại tuần hoàn; Giai đoạn 2 (3–6 tháng): Phẫu thuật Glenn hai hướng nối SVC vào ĐMP; Giai đoạn 3 (2–4 tuổi): Phẫu thuật Fontan nối IVC vào ĐMP.<br><br><b>💡 Lưu ý:</b><br>Mục tiêu là đưa tâm thất phải duy nhất đảm nhận bơm máu đại tuần hoàn.",
        "extra": "Mục 8.2 & Bảng 9.1 RELEASE.",
        "tags": ["PED-43", "EBM", "HLHS", "Norwood-Glenn-Fontan"]
    },
    {
        "id": "PED43-E44",
        "track": "ebm",
        "type": "basic",
        "category": "TAPVC",
        "section": "E8",
        "front": "Phân biệt hai thể lâm sàng của bất thường hồi lưu tĩnh mạch phổi hoàn toàn (TAPVC): thể tắc nghẽn và thể không tắc nghẽn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thể không tắc nghẽn (trên tim): tím nhẹ, tăng máu phổi, suy tim sung huyết, X-quang hình người tuyết; Thể có tắc nghẽn (dưới tim): tắc nghẽn tĩnh mạch phổi gây tăng áp phổi ác tính, phù phổi cấp dữ dội ở sơ sinh cần mổ cấp cứu tối khẩn.<br><br><b>💡 Lưu ý:</b><br>Thể dưới tim tắc nghẽn có tỷ lệ tử vong sơ sinh lên đến 40%.",
        "extra": "Mục 8 RELEASE & PEDYTB mục 3.12.",
        "tags": ["PED-43", "EBM", "TAPVC", "Phu-phoi-cap"]
    },
    {
        "id": "PED43-E45",
        "track": "ebm",
        "type": "cloze",
        "category": "Bệnh Ebstein",
        "section": "E8",
        "text": "[EBM] Dấu hiệu điện tâm đồ đặc trưng của bệnh Ebstein là {{c1::sóng P khổng lồ (kiểu dãy Himalaya)}} ở chuyển đạo DII, kèm nguy cơ xuất hiện cơn nhịp nhanh do {{c1::hội chứng Wolff-Parkinson-White (WPW)}} ở 15% bệnh nhân.",
        "extra": "Mục 8 RELEASE & PEDYTB mục 3.11.",
        "tags": ["PED-43", "EBM", "Ebstein", "WPW", "ECG"]
    },

    # --- E9: Nguyên tắc điều trị nội khoa & Thời điểm vàng can thiệp (Mục 9) ---
    {
        "id": "PED43-E46",
        "track": "ebm",
        "type": "basic",
        "category": "Thời điểm can thiệp",
        "section": "E9",
        "front": "Thời điểm vàng can thiệp phẫu thuật hoặc bít dù của 4 bệnh tim bẩm sinh thường gặp (VSD, ASD, PDA non tháng, Fallot) là khi nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>VSD lớn: 1–4 tháng (suy tim nặng) hoặc trước 6–9 tháng; ASD thứ phát: 3–5 tuổi; PDA sơ sinh non tháng: tuần 1–2 sau sinh (đóng thuốc); Tứ chứng Fallot: 4–6 tháng tuổi.<br><br><b>💡 Lưu ý:</b><br>Nắm chắc bảng thời điểm vàng để tư vấn và chuyển tuyến can thiệp kịp thời.",
        "extra": "Bảng 9.1 RELEASE.",
        "tags": ["PED-43", "EBM", "Thoi-diem-vang", "Can-thiep"]
    },
    {
        "id": "PED43-E47",
        "track": "ebm",
        "type": "basic",
        "category": "Phẫu thuật tạm thời",
        "section": "E9",
        "front": "Khi nào có chỉ định làm phẫu thuật tạm thời cầu nối Blalock-Taussig cải tiến thay vì sửa chữa triệt để ngay trong tim bẩm sinh tím?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khi trẻ có tím nặng đe dọa tính mạng nhưng cân nặng quá thấp hoặc các nhánh động mạch phổi còn quá nhỏ/thiểu sản chưa đủ kích thước để chịu lưu lượng sửa chữa triệt để một thì.<br><br><b>💡 Lưu ý:</b><br>Cầu nối BT giúp cấp máu tạm thời nuôi các nhánh ĐMP phát triển trước khi mổ triệt để.",
        "extra": "Mục 9.2 RELEASE.",
        "tags": ["PED-43", "EBM", "BT-shunt", "Phau-thuat-tam-thoi"]
    },
    {
        "id": "PED43-E48",
        "track": "ebm",
        "type": "basic",
        "category": "Can thiệp qua da",
        "section": "E9",
        "front": "Nhóm dị tật tim bẩm sinh nào hiện nay có chỉ định bít dù qua da thay thế phẫu thuật mở tim hở?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thông liên nhĩ lỗ thứ phát có gờ mô xung quanh đầy đủ, còn ống động mạch (PDA) ở trẻ lớn, và một số thể thông liên thất phần cơ hoặc quanh màng thuận lợi giải phẫu.<br><br><b>💡 Lưu ý:</b><br>Can thiệp qua da giúp trẻ hồi phục nhanh, không cần mở xương ức và không chạy máy tim phổi nhân tạo.",
        "extra": "Mục 9.2 RELEASE.",
        "tags": ["PED-43", "EBM", "Bit-du-qua-da"]
    },
    {
        "id": "PED43-E49",
        "track": "ebm",
        "type": "cloze",
        "category": "Cấp cứu sơ sinh",
        "section": "E9",
        "text": "[EBM] Thuốc cấp cứu hàng đầu duy trì mở ống động mạch để cứu sống trẻ sơ sinh mắc bệnh tim bẩm sinh phụ thuộc ống là truyền liên tục {{c1::Prostaglandin E1 (Alprostadil)}} với liều khởi đầu 0,05 – 0,1 µg/kg/phút.",
        "extra": "Mục 9 RELEASE & Box an toàn.",
        "tags": ["PED-43", "EBM", "PGE1", "Lieu-thuoc"]
    },

    # --- E10: 10 Cạm bẫy lâm sàng thường gặp (Mục 10) ---
    {
        "id": "PED43-E50",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 1: Có phải mọi bệnh tim bẩm sinh đều nghe thấy tiếng thổi ở tim không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Không. Những bệnh cực kỳ nguy kịch như chuyển gốc đại động mạch (d-TGA) đơn thuần hoặc TAPVC thể tắc nghẽn có thể hoàn toàn không có tiếng thổi ở tim do không có dòng xoáy tạo tiếng.<br><br><b>💡 Lưu ý:</b><br>Trẻ sơ sinh tím tái nặng dù tim không tiếng thổi vẫn phải nghĩ ngay tới tim bẩm sinh tím.",
        "extra": "Mục 10 (Cạm bẫy 1) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Tieng-thoi"]
    },
    {
        "id": "PED43-E51",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 2: Sai lầm chết người khi dùng thuốc hạ sốt hoặc chỉ cho thở oxy để điều trị cơn tím Fallot là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Cơn tím không phải do sốt hay thiếu oxy đơn thuần mà do co thắt phễu đường ra thất phải; oxy liều cao không qua được phổi bị tắc nghẽn; bắt buộc phải dùng tư thế ngực gối, Morphine và bù dịch để phá vỡ vòng xoắn co thắt.<br><br><b>💡 Lưu ý:</b><br>Chỉ loay hoay cho thở oxy mà không gập gối sẽ làm trẻ tử vong.",
        "extra": "Mục 10 (Cạm bẫy 2) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Tet-spell"]
    },
    {
        "id": "PED43-E52",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 4: Tại sao chẩn đoán nhầm trẻ suy tim do shunt Trái - Phải lớn thành viêm phổi là sai lầm rất phổ biến?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Cả hai đều có thở nhanh, co kéo và nghe rale ẩm ở phổi do ứ dịch; tuy nhiên trẻ tim bẩm sinh có thêm bú ngắt quãng vã mồ hôi, gan to và tiếng thổi ở tim.<br><br><b>💡 Lưu ý:</b><br>Điều trị kháng sinh kéo dài không giải quyết được gốc rễ suy tim huyết động.",
        "extra": "Mục 10 (Cạm bẫy 4) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Viem-phoi-nham"]
    },
    {
        "id": "PED43-E53",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 7: Tại sao cho thở oxy nồng độ cao bừa bãi ở trẻ có shunt Trái - Phải lớn (VSD, PDA lớn) lại nguy hiểm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Oxy nồng độ cao là chất giãn mạch phổi cực mạnh, làm tụt sức cản mạch phổi (PVR), khiến luồng shunt Trái - Phải càng tràn ngập dữ dội lên phổi gây ngập lụt phù phổi và sốc tim.<br><br><b>💡 Lưu ý:</b><br>Chỉ cho thở oxy khi có giảm oxy máu thực sự và duy trì SpO₂ mục tiêu vừa phải.",
        "extra": "Mục 10 (Cạm bẫy 7) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Oxy-lieu-cao"]
    },
    {
        "id": "PED43-E54",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 9: Nhầm lẫn tiếng thổi tâm thu trong Fallot là do dòng máu qua lỗ VSD dẫn đến sai lầm gì trong theo dõi cơn tím?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thực chất tiếng thổi là do hẹp đường ra thất phải. Trong cơn tím, tiếng thổi nhỏ đi báo hiệu co thắt phễu nặng cắt máu lên phổi; nếu lầm tưởng tiếng thổi giảm là bệnh tự thuyên giảm sẽ bỏ lỡ thời cơ cấp cứu tối khẩn.<br><br><b>💡 Lưu ý:</b><br>Tiếng thổi nhỏ đi ở trẻ Fallot tím tái là dấu hiệu báo động đỏ.",
        "extra": "Mục 10 (Cạm bẫy 9) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Tieng-thoi-Fallot"]
    },
    {
        "id": "PED43-E55",
        "track": "ebm",
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "section": "E10",
        "front": "Cạm bẫy lâm sàng 10: Hậu quả của việc trì hoãn phẫu thuật thông liên thất lớn có tăng áp phổi quá 9 tháng tuổi là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Các mạch máu phổi bị phì đại và xơ hóa lòng mạch cố định (Hội chứng Eisenmenger); trẻ mất vĩnh viễn cơ hội phẫu thuật sửa chữa và phải đối mặt với suy tim, tím tái và tử vong sớm.<br><br><b>💡 Lưu ý:</b><br>Phải chủ động chuyển phẫu thuật tim trước mốc 6–9 tháng tuổi.",
        "extra": "Mục 10 (Cạm bẫy 10) RELEASE.",
        "tags": ["PED-43", "EBM", "Cam-bay", "Tri-hoan-mo-VSD"]
    },

    # --- E11: 4 Checkpoint tư duy phản biện tại giường (Mục 11) ---
    {
        "id": "PED43-E56",
        "track": "ebm",
        "type": "basic",
        "category": "Checkpoint tư duy",
        "section": "E11",
        "front": "Checkpoint 1: Vì sao trẻ mắc tứ chứng Fallot có bản năng tự ngồi xổm khi đang chơi đùa bị mệt?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ngồi xổm gập các động mạch đùi và động mạch chậu, làm tăng sức cản mạch hệ thống (SVR) đột ngột, ép dòng máu từ thất phải vượt qua phễu hẹp lên động mạch phổi để tăng lượng oxy máu trao đổi.<br><br><b>💡 Lưu ý:</b><br>Trẻ tự học được phản xạ này từ khoảng 1–2 tuổi khi bắt đầu biết đi.",
        "extra": "Mục 11 (Checkpoint 1) RELEASE.",
        "tags": ["PED-43", "EBM", "Checkpoint", "Ngoi-xom"]
    },
    {
        "id": "PED43-E57",
        "track": "ebm",
        "type": "basic",
        "category": "Checkpoint tư duy",
        "section": "E11",
        "front": "Checkpoint 2: Dấu hiệu điện tâm đồ nào giúp phân biệt chắc chắn giữa ASD lỗ tiên phát và ASD lỗ thứ phát tại giường?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>ASD lỗ thứ phát có trục phải và dày thất phải; ASD lỗ tiên phát có trục trái (hoặc trục vô định) và khử cực ngược chiều kim đồng hồ do khuyết gối nội tâm mạc làm lệch đường dẫn truyền.<br><br><b>💡 Lưu ý:</b><br>Nhìn trục điện tim trên chuyển đạo DII, DIII, aVF giúp phân định thể giải phẫu ngay lập tức.",
        "extra": "Mục 11 (Checkpoint 2) RELEASE.",
        "tags": ["PED-43", "EBM", "Checkpoint", "ECG-ASD"]
    },
    {
        "id": "PED43-E58",
        "track": "ebm",
        "type": "basic",
        "category": "Checkpoint tư duy",
        "section": "E11",
        "front": "Checkpoint 3: Hai đặc điểm thăm khám tại giường giúp phân biệt chính xác giữa tím trung ương và tím ngoại vi là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Vị trí: Tím trung ương thấy ở niêm mạc miệng, lưỡi và kết mạc mắt; tím ngoại vi chỉ khu trú ở đầu ngón tay/chân lạnh. 2) SpO₂: Tím trung ương có SpO₂ giảm; tím ngoại vi SpO₂ ở mô ấm bình thường.<br><br><b>💡 Lưu ý:</b><br>Luôn quan sát niêm mạc lưỡi và mặt trong má để tìm tím trung ương.",
        "extra": "Mục 11 (Checkpoint 3) RELEASE.",
        "tags": ["PED-43", "EBM", "Checkpoint", "Tim-trung-uong-ngoai-vi"]
    },
    {
        "id": "PED43-E59",
        "track": "ebm",
        "type": "basic",
        "category": "Checkpoint tư duy",
        "section": "E11",
        "front": "Checkpoint 4: Giải thích vì sao trong bệnh hẹp eo động mạch chủ huyết áp chi trên lại cao hơn huyết áp chi dưới?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vị trí eo hẹp nằm sau chỗ xuất phát của động mạch dưới đòn trái nuôi chi trên: chi trên nhận máu trước chỗ hẹp với áp lực cản cao, trong khi chi dưới nhận máu sau chỗ hẹp bị giảm áp lực tưới máu nghiêm trọng.<br><br><b>💡 Lưu ý:</b><br>Chênh lệch huyết áp tâm thu tay - chân > 20 mmHg là tiêu chuẩn chẩn đoán quan trọng.",
        "extra": "Mục 11 (Checkpoint 4) RELEASE.",
        "tags": ["PED-43", "EBM", "Checkpoint", "Chenh-lech-HA-CoA"]
    },

    # --- E12: 2 Ca lâm sàng thực chiến kèm biện luận chi tiết (Mục 12) ---
    {
        "id": "PED43-E60",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng",
        "section": "E12",
        "front": "Case 1: Trẻ 10 tháng Fallot sau khóc thét đột ngột thở nhanh 68 l/p, môi tím đen, lơ mơ, tiếng thổi tâm thu mờ nhạt — Chẩn đoán và 2 việc cần làm ngay lập tức tại giường là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chẩn đoán: Cơn tím thiếu oxy cấp (Tet spell). Xử trí tức thì: 1) Lập tức đặt trẻ ở tư thế ngực gối (gấp hai đùi sát vào ngực); 2) Cho thở oxy 100% qua mặt nạ có túi dự trữ.<br><br><b>💡 Lưu ý:</b><br>Thực hiện hai động tác này trong 30 giây đầu tiên trước khi tiêm thuốc.",
        "extra": "Mục 12 (Case 1) RELEASE.",
        "tags": ["PED-43", "EBM", "Case-study", "Tet-spell-cap-cuu"]
    },
    {
        "id": "PED43-E61",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng",
        "section": "E12",
        "front": "Case 1: Vì sao sau khi tiêm Morphine và truyền dịch cấp cứu cơn tím Fallot thành công, tiếng thổi tâm thu lại nghe to rõ trở lại?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Morphine và bù dịch làm an thần, giảm giao cảm và giãn cơ phễu đường ra thất phải; dòng máu được tái lập lưu thông mạnh mẽ từ thất phải qua chỗ phễu lên động mạch phổi tạo lại tiếng thổi tâm thu.<br><br><b>💡 Lưu ý:</b><br>Tiếng thổi rõ trở lại là bằng chứng huyết động chứng minh cơn co thắt phễu đã được giải tỏa.",
        "extra": "Mục 12 (Case 1) RELEASE.",
        "tags": ["PED-43", "EBM", "Case-study", "Giai-toa-pheu"]
    },
    {
        "id": "PED43-E62",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng",
        "section": "E12",
        "front": "Case 2: Trẻ sơ sinh 29 tuần, 1200g, thở CPAP ngày thứ 6 xuất hiện ngừng thở, phụ thuộc oxy tăng, mạch bẹn nảy mạnh chìm sâu, thổi liên tục dưới đòn trái — Chẩn đoán xác định là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Còn ống động mạch lớn có ý nghĩa huyết động (hsPDA - Hemodynamically Significant PDA) ở trẻ sơ sinh non tháng.<br><br><b>💡 Lưu ý:</b><br>Mạch nảy mạnh chìm sâu và hiệu số huyết áp rộng là dấu hiệu lâm sàng đặc hiệu.",
        "extra": "Mục 12 (Case 2) RELEASE.",
        "tags": ["PED-43", "EBM", "Case-study", "PDA-non-thang"]
    },
    {
        "id": "PED43-E63",
        "track": "ebm",
        "type": "basic",
        "category": "Ca lâm sàng",
        "section": "E12",
        "front": "Case 2: Phác đồ xử trí đóng ống động mạch bằng thuốc ở trẻ sơ sinh non tháng 29 tuần này gồm những bước gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hạn chế dịch nhập, tăng áp lực dương CPAP chống phù phổi; chỉ định Ibuprofen tĩnh mạch liệu trình 3 liều (10 - 5 - 5 mg/kg cách nhau 24 giờ); theo dõi sát chức năng thận và xuất huyết tiêu hóa.<br><br><b>💡 Lưu ý:</b><br>Sau liệu trình siêu âm Doppler kiểm tra mức độ đóng ống.",
        "extra": "Mục 12 (Case 2) RELEASE.",
        "tags": ["PED-43", "EBM", "Case-study", "Ibuprofen-protocol"]
    },

    # --- E13: Tips thực hành lâm sàng & Theo dõi điều dưỡng (Mục 13) ---
    {
        "id": "PED43-E64",
        "track": "ebm",
        "type": "basic",
        "category": "Tips thực hành",
        "section": "E13",
        "front": "Phản xạ xử trí tức thì đầu tiên của điều dưỡng khi phát hiện trẻ Fallot khóc quấy xuất hiện cơn tím tái đậm là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Lập tức gập chặt hai đầu gối trẻ áp sát vào ngực (tư thế ngực gối) và gọi hỗ trợ, TUYỆT ĐỐI KHÔNG bỏ đi tìm thuốc hay loay hoay lấy ven trước.<br><br><b>💡 Lưu ý:</b><br>Động tác gập gối làm tăng SVR tức thì cắt cơn thiếu oxy não.",
        "extra": "Tip 1 & Tip 8 RELEASE.",
        "tags": ["PED-43", "EBM", "Tips-thuc-hanh", "Dieu-duong"]
    },
    {
        "id": "PED43-E65",
        "track": "ebm",
        "type": "basic",
        "category": "Tips thực hành",
        "section": "E13",
        "front": "Tại sao cần đo huyết áp đồng thời ở cả tay phải và một trong hai chân ở mọi trẻ tăng huyết áp hoặc suy tim?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Để không bỏ sót bệnh hẹp eo động mạch chủ (CoA) — bệnh lý gây tăng huyết áp chi trên nhưng tụt huyết áp chi dưới với chênh lệch > 20 mmHg.<br><br><b>💡 Lưu ý:</b><br>Đo huyết áp một tay rất dễ chẩn đoán nhầm thành tăng huyết áp vô căn.",
        "extra": "Tip 2 RELEASE.",
        "tags": ["PED-43", "EBM", "Tips-thuc-hanh", "Do-HA-4-chi"]
    },
    {
        "id": "PED43-E66",
        "track": "ebm",
        "type": "basic",
        "category": "Tips thực hành",
        "section": "E13",
        "front": "Tại sao đối với trẻ mắc tứ chứng Fallot phải tuyệt đối tránh để trẻ bị mất nước và sốt cao kéo dài?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Trẻ Fallot có đa hồng cầu thứ phát; mất nước sẽ làm máu bị cô đặc dữ dội, tăng độ nhớt máu vọt lên gây biến chứng tắc mạch máu não và áp xe não nguy hiểm.<br><br><b>💡 Lưu ý:</b><br>Khi trẻ sốt hoặc tiêu chảy phải bù dịch đầy đủ và theo dõi Hematocrit sát.",
        "extra": "Tip 9 RELEASE.",
        "tags": ["PED-43", "EBM", "Tips-thuc-hanh", "Tac-mach-nao"]
    },
    {
        "id": "PED43-E67",
        "track": "ebm",
        "type": "basic",
        "category": "Tips thực hành",
        "section": "E13",
        "front": "Hướng dẫn chăm sóc nuôi dưỡng cho trẻ mắc tim bẩm sinh có luồng shunt Trái - Phải lớn gồm những nguyên tắc gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chia nhỏ cữ bú làm nhiều bữa, cho bú ở tư thế nửa nằm nửa ngồi để giảm công thở, dùng sữa có đậm độ năng lượng cao (120–150 kcal/kg/ngày) và không ép trẻ bú kéo dài quá 30 phút mỗi cữ.<br><br><b>💡 Lưu ý:</b><br>Bú kéo dài làm trẻ tiêu hao năng lượng nhiều hơn năng lượng nạp vào.",
        "extra": "Tip 11 & Khuyến cáo dinh dưỡng RELEASE.",
        "tags": ["PED-43", "EBM", "Tips-thuc-hanh", "Dinh-duong"]
    },

    # --- E14: Tóm tắt thực hành & Tiêu chuẩn xuất viện (Mục 14) ---
    {
        "id": "PED43-E68",
        "track": "ebm",
        "type": "basic",
        "category": "Tiêu chuẩn xuất viện",
        "section": "E14",
        "front": "5 tiêu chuẩn xuất viện an toàn cho một bệnh nhi tim bẩm sinh sau đợt điều trị nội khoa suy tim hoặc cơn tím là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trẻ bú tốt, không khó thở khi ăn, tăng cân ổn định; 2) Triệu chứng suy tim được kiểm soát bằng thuốc uống > 48 giờ; 3) SpO₂ và huyết động ổn định theo bệnh; 4) Gia đình thành thạo kỹ năng xử trí cơn tím tại nhà; 5) Có kế hoạch can thiệp/phẫu thuật cụ thể.<br><br><b>💡 Lưu ý:</b><br>Đảm bảo an toàn tuyệt đối trước khi cho trẻ về cộng đồng.",
        "extra": "Mục 14.2 RELEASE.",
        "tags": ["PED-43", "EBM", "Xuat-vien-an-toan"]
    },
    {
        "id": "PED43-E69",
        "track": "ebm",
        "type": "basic",
        "category": "Phòng ngừa viêm nội tâm mạc",
        "section": "E14",
        "front": "Ba biện pháp cốt lõi phòng ngừa viêm nội tâm mạc nhiễm khuẩn (IE) ở trẻ mắc tim bẩm sinh là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Vệ sinh răng miệng hàng ngày cẩn thận và khám nha khoa định kỳ; 2) Điều trị triệt để các ổ nhiễm trùng ngoài da và mô mềm; 3) Dùng kháng sinh dự phòng trước các can thiệp nha khoa xâm lấn ở đối tượng nguy cơ cao.<br><br><b>💡 Lưu ý:</b><br>Viêm nội tâm mạc là biến chứng nhiễm trùng đe dọa tính mạng người bệnh tim bẩm sinh.",
        "extra": "Mục 14 & Tip 10 RELEASE.",
        "tags": ["PED-43", "EBM", "Phong-IE"]
    },
    {
        "id": "PED43-E70",
        "track": "ebm",
        "type": "cloze",
        "category": "Tóm tắt xử trí",
        "section": "E14",
        "text": "[EBM] Tóm tắt 5 bước xử trí cơn tím Fallot tại giường theo thứ tự ưu tiên: 1) {{c1::Tư thế ngực gối}} → 2) {{c1::Thở oxy}} → 3) {{c1::Morphine}} → 4) {{c1::Bù dịch đẳng trương}} → 5) {{c1::Propranolol TM chậm}}.",
        "extra": "Mục 14.1 RELEASE.",
        "tags": ["PED-43", "EBM", "Tom-tat", "Tet-spell"]
    },
    {
        "id": "PED43-E71",
        "track": "ebm",
        "type": "cloze",
        "category": "Dinh dưỡng tim mạch",
        "section": "E14",
        "text": "[EBM] Nhu cầu năng lượng ở trẻ tim bẩm sinh có shunt Trái - Phải lớn tăng cao do tăng công hô hấp và tuần hoàn, cần cung cấp chế độ ăn đạt {{c1::120 – 150 kcal/kg/ngày}}.",
        "extra": "Mục 0.1 & Mục 14 RELEASE.",
        "tags": ["PED-43", "EBM", "Dinh-duong"]
    },

    # --- E15: Tài liệu tham khảo & Bằng chứng y học (Mục 15) ---
    {
        "id": "PED43-E72",
        "track": "ebm",
        "type": "cloze",
        "category": "Bằng chứng y học",
        "section": "E15",
        "text": "[EBM] Văn bản hướng dẫn thực hành lâm sàng toàn diện năm 2025 của ACC/AHA về quản lý tim bẩm sinh ở người trưởng thành (ACHD) được công bố với mã định danh PubMed là {{c1::PMID 41411480}}.",
        "extra": "Mục 15 RELEASE (ACC/AHA Guideline 2025).",
        "tags": ["PED-43", "EBM", "Bang-chung", "PMID-41411480"]
    },
    {
        "id": "PED43-E73",
        "track": "ebm",
        "type": "cloze",
        "category": "Bằng chứng y học",
        "section": "E15",
        "text": "[EBM] Bằng chứng mức độ I từ tổng quan hệ thống Cochrane khẳng định Ibuprofen có hiệu quả đóng ống động mạch tương đương Indomethacin ở trẻ non tháng mang mã định danh {{c1::PMID 30264852}}.",
        "extra": "Mục 15 RELEASE (Ohlsson et al., Cochrane 2018).",
        "tags": ["PED-43", "EBM", "Bang-chung", "PMID-30264852"]
    },
    {
        "id": "PED43-E74",
        "track": "ebm",
        "type": "cloze",
        "category": "Bằng chứng y học",
        "section": "E15",
        "text": "[EBM] Hai công trình kinh điển về giải phẫu và tiến bộ phẫu thuật sửa chữa toàn bộ Fallot mang tính bước ngoặt trên Orphanet và The Lancet lần lượt là {{c1::PMID 19144126}} và {{c1::PMID 19683809}}.",
        "extra": "Mục 15 RELEASE (Bailliard 2009 & Apitz 2009).",
        "tags": ["PED-43", "EBM", "Bang-chung", "PMID-19144126", "PMID-19683809"]
    },
    {
        "id": "PED43-E75",
        "track": "ebm",
        "type": "cloze",
        "category": "Bằng chứng y học",
        "section": "E15",
        "text": "[EBM] Nghiên cứu dịch tễ kinh điển của Hoffman & Kaplan trên JACC năm 2002 xác định tỷ lệ tim bẩm sinh nặng khoảng 8/1.000 trẻ sinh sống có mã định danh là {{c1::PMID 12084585}}.",
        "extra": "Mục 15 RELEASE (Hoffman & Kaplan, JACC 2002).",
        "tags": ["PED-43", "EBM", "Bang-chung", "PMID-12084585"]
    }
]
