# -*- coding: utf-8 -*-
"""
ped55_cards_data.py
Bo the MASTER DUAL-TRACK cho PED-55 Xuat huyet tieu hoa o tre em.
Gop 2 luong trong 1 file duy nhat:
- Track 1 [BAREM GOC Y THAI BINH]: 51 the Basic bao phu 100% cau chu giao trinh (Trang 87 - 99).
- Track 2 [EBM HIEN DAI & LAM SANG]: 17 the Basic giai quyet cap cuu soc, Baveno VII, Meckel, 5 cam bay.
Tong cong: 68 the Basic chuyen sau, xuong dong ro rang, khong sot bat ky chi tiet nao.
"""

cards_data = [
    {
        "id": "PED55-B01",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Mục tiêu bài học",
        "front": "5 mục tiêu học tập chính của bài Xuất huyết tiêu hóa ở trẻ em theo giáo trình Y Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trình bày được các triệu chứng lâm sàng của xuất huyết tiêu hóa.<br>2) Trình bày được các xét nghiệm cận lâm sàng chẩn đoán xuất huyết tiêu hóa.<br>3) Trình bày được nguyên nhân xuất huyết đường tiêu hóa trên.<br>4) Trình bày các nguyên nhân gây xuất huyết đường tiêu hóa dưới theo vị trí và lứa tuổi.<br>5) Trình bày được phác đồ điều trị xuất huyết tiêu hóa ở trẻ em.<br><br><b>💡 Giải thích của AI:</b><br>Khung 5 mục tiêu này bao quát từ triệu chứng lâm sàng, chẩn đoán phân biệt, phân tầng theo lứa tuổi đến quy trình hồi sức cấp cứu tại giường.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục tiêu bài học)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Muc-tieu"
        ]
    },
    {
        "id": "PED55-B02",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Định nghĩa - Nôn máu",
        "front": "Định nghĩa Nôn ra máu và giới hạn giải phẫu của xuất huyết tiêu hóa trên theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Giới hạn giải phẫu: Xuất huyết đường tiêu hóa trên được tính từ MIỆNG, HẦU HỌNG TỚI GÓC TREITZ (góc tá hỗng tràng).<br>• Định nghĩa nôn ra máu: Được xác định khi có xuất hiện máu trong chất nôn của bệnh nhi, tính chất có thể là máu loãng, máu đỏ tươi, máu đen hay máu cục.<br><br><b>💡 Giải thích của AI:</b><br>Góc Treitz là ranh giới phân định giải phẫu kinh điển: mọi tổn thương chảy máu từ góc Treitz trở lên trên đều xếp vào xuất huyết tiêu hóa trên.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 1 - Định nghĩa)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dinh-nghia",
            "Non-mau",
            "Goc-Treitz"
        ]
    },
    {
        "id": "PED55-B03",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Định nghĩa - Đại tiện máu đen",
        "front": "Định nghĩa Đại tiện máu đen và phạm vi vị trí tổn thương chảy máu có thể gặp theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Phạm vi tổn thương: Là biểu hiện chảy máu có thể bắt nguồn TỪ HẦU HỌNG CHO TỚI ĐẠI TRÀNG.<br>• Tính chất phân: Phân có màu nâu sẫm, màu bã cà phê, hoặc đen nhánh như bồ hóng, hắc ín.<br>• Ý nghĩa phối hợp: Nếu ỉa máu đen đi kèm với nôn ra máu thì CHẮC CHẮN là xuất huyết đường tiêu hóa trên.<br><br><b>💡 Giải thích của AI:</b><br>Màu đen như bồ hóng là do Hemoglobin tiếp xúc với acid dạ dày và vi khuẩn đường ruột bị thoái giáng thành Hematin.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 1 - Định nghĩa)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dinh-nghia",
            "Phan-den"
        ]
    },
    {
        "id": "PED55-B04",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Định nghĩa - Phân có máu",
        "front": "Định nghĩa Đại tiện phân có máu và ý nghĩa khi phân có dây máu đỏ bám ngoài theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đại tiện phân có máu: Là biểu hiện chảy máu đường tiêu hóa DƯỚI (dưới góc Treitz), điển hình là từ ruột non hoặc đại tràng.<br>• Phân có dây máu đỏ bám ngoài: Là biểu hiện vị trí chảy máu ở TRỰC TRÀNG hoặc HẬU MÔN (máu chưa kịp hòa lẫn vào phân).<br><br><b>💡 Giải thích của AI:</b><br>Máu hòa lẫn vào phân gợi ý tổn thương ở cao (đại tràng phải hoặc ruột non); máu đỏ tươi bọc ngoài khuôn phân gợi ý tổn thương thấp ở trực tràng/hậu môn.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 1 - Định nghĩa)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dinh-nghia",
            "Phan-co-mau"
        ]
    },
    {
        "id": "PED55-B05",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Định nghĩa - Chảy máu vi thể",
        "front": "Đặc điểm và hậu quả của tình trạng 'Chảy máu tiêu hóa không nhìn thấy' theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đặc điểm: Là tình trạng chảy máu số lượng ít, rỉ rả từ từ, không làm thay đổi màu sắc quan sát được của phân (mắt thường không nhận biết được).<br>• Hậu quả: Nếu chảy máu kéo dài mạn tính sẽ dẫn đến THIẾU MÁU THIẾU SẮT ở trẻ em.<br>• Phát hiện: Phát hiện bằng xét nghiệm tìm máu ẩn trong phân (FOBT).<br><br><b>💡 Giải thích của AI:</b><br>Trẻ có thiếu máu thiếu sắt không rõ nguyên nhân ăn uống bắt buộc phải làm xét nghiệm tìm máu ẩn trong phân để loại trừ chảy máu tiêu hóa vi thể (polyp, giun móc, Meckel).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 1 - Định nghĩa)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dinh-nghia",
            "Mau-an",
            "Thieu-sat"
        ]
    },
    {
        "id": "PED55-B06",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Khai thác lâm sàng nôn máu",
        "front": "4 đặc điểm cần xác định khi hỏi bệnh và quan sát trẻ Nôn ra máu theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hoàn cảnh xuất hiện: Lần đầu tiên hay tái phát nhiều lần, khoảng cách giữa các lần nôn và thời gian kéo dài của đợt nôn.<br>2) Khối lượng máu nôn: Cần ước lượng cụ thể số lượng máu mất.<br>3) Tính chất và màu sắc máu: Máu đỏ tươi, máu đen, máu cục hay máu loãng có lẫn thức ăn.<br>4) Các triệu chứng kèm theo: Đau bụng (loét dạ dày), sốt và vàng da (chảy máu đường mật, xơ gan).<br><br><b>💡 Giải thích của AI:</b><br>Máu đỏ tươi nôn ồ ạt gợi ý vỡ giãn tĩnh mạch thực quản; máu đen bã cà phê gợi ý viêm loét dạ dày tá tràng rỉ rả.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 2.1 - Nôn ra máu)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Non-ra-mau",
            "Khai-thac-lam-sang"
        ]
    },
    {
        "id": "PED55-B07",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nôn máu giả",
        "front": "3 tình huống 'Nôn ra máu giả' cần chẩn đoán phân biệt nhanh chóng theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trẻ nôn ra thức ăn có màu đỏ giống máu: Ăn tiết canh, chè đỗ đen, quả dền, dưa hấu, nước ngọt phẩm màu đỏ → Phân biệt bằng hỏi kỹ tiền sử ăn uống.<br>2) Nuốt máu từ đường hô hấp trên: Chảy máu mũi (chảy máu cam) hoặc chảy máu vùng miệng/răng họng, trẻ nuốt vào dạ dày rồi nôn ra → Phân biệt bằng khám kỹ mũi họng.<br>3) Trẻ sơ sinh nuốt máu mẹ: Hít/nuốt máu mẹ trong quá trình chuyển dạ hoặc khi bú mẹ bị nứt cổ gà núm vú → Phân biệt bằng nghiệm pháp Apt-Downey.<br><br><b>💡 Giải thích của AI:</b><br>Bước 1 trước khi tiến hành hồi sức xuất huyết tiêu hóa luôn luôn là loại trừ nôn máu giả để tránh chẩn đoán nhầm tai hại.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87, Mục 2.1 - Nôn ra máu)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Non-mau-gia",
            "Phan-biet"
        ]
    },
    {
        "id": "PED55-B08",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nghiệm pháp Apt-Downey",
        "front": "Nguyên lý, cách tiến hành và tiêu chuẩn đọc kết quả Nghiệm pháp Apt-Downey để phân biệt máu mẹ vs máu con ở trẻ sơ sinh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nguyên lý: Dựa trên sự khác biệt về tính kháng kiềm giữa Hemoglobin người lớn (HbA) và Hemoglobin thai nhi (HbF).<br>• Cách tiến hành: Lấy dịch nôn hoặc phân có máu của trẻ sơ sinh, hòa loãng với nước cất, sau đó cho thêm vài giọt dung dịch kiềm Natri Hydroxyd (NaOH 1%).<br>• Đọc kết quả sau 2 phút:<br>1) Dung dịch chuyển sang màu VÀNG NÂU: Là MÁU MẸ (HbA bị kiềm phá hủy biến tính thành hematin kiềm).<br>2) Dung dịch GIỮ NGUYÊN MÀU HỒNG: Là MÁU CỦA TRẺ SƠ SINH (HbF có tính chất kháng kiềm không bị đổi màu) → Xác định trẻ thực sự bị xuất huyết tiêu hóa.<br><br><b>💡 Giải thích của AI:</b><br>Nghiệm pháp Apt-Downey là xét nghiệm tại giường siêu nhanh và rẻ tiền giúp trẻ sơ sinh nuốt máu mẹ tránh được các cuộc nội soi hay truyền dịch không cần thiết.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 87 - 88, Mục 2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Apt-Downey",
            "Mau-me-vs-con",
            "So-sinh"
        ]
    },
    {
        "id": "PED55-B09",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Phân biệt Nôn máu vs Ho máu",
        "front": "Phân biệt Nôn ra máu với Ho ra máu (Khái huyết) theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ho ra máu (Khái huyết):<br>1) Máu tống ra sau khi ho hoặc có cảm giác ngứa cổ họng, nóng rát sau xương ức.<br>2) Tính chất máu: Máu ĐỎ TƯƠI, CÓ BỌT KHÍ, tính kiềm, KHÔNG LẪN THỨC ĂN.<br>3) Diễn biến: Có 'đuôi khái huyết' (những ngày sau khạc đờm lẫn vệt máu sẫm màu dần).<br>• Nôn ra máu:<br>1) Máu tống ra sau khi buồn nôn và nôn ói.<br>2) Tính chất máu: Máu đỏ sẫm hoặc đen bã cà phê, máu cục, tính acid, LẪN THỨC ĂN và dịch vị.<br>3) Diễn biến: Không có đuôi khái huyết; sau đó trẻ đi ngoài phân đen.<br><br><b>💡 Giải thích của AI:</b><br>Đặc tính 'máu có bọt khí + kiềm tính + có đuôi khái huyết' là bộ ba dấu hiệu loại trừ chắc chắn xuất huyết tiêu hóa.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 88, Mục 2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Phan-biet",
            "Non-mau-vs-Khai-huyet"
        ]
    },
    {
        "id": "PED55-B10",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Phân biệt Đại tiện phân đen giả",
        "front": "Phân biệt Đại tiện phân đen do xuất huyết tiêu hóa với các chất làm đen hoặc đỏ phân giả tạo?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Phân đen giả:<br>1) Do uống các chế phẩm sắt: Phân có màu đen xám hoặc xanh đen, phân khô chắc, không bóng, KHÔNG CÓ MÙI KHẮM bồ hóng, xét nghiệm tìm máu ẩn âm tính.<br>2) Do dùng thuốc Bismuth (thuốc trị dạ dày) hoặc ăn nhiều cam thảo.<br>• Phân đỏ giả: Do dùng kháng sinh Rifampicin (thuốc bài tiết làm nước tiểu và phân có màu đỏ cam).<br>• Phân đen do xuất huyết tiêu hóa: Màu đen bóng như bồ hóng, ướt nhão, MÙI KHẮM NỒNG NẶC đặc trưng của máu thối rữa.<br><br><b>💡 Giải thích của AI:</b><br>Hỏi kỹ tiền sử dùng thuốc bổ máu (sắt) hoặc thuốc dạ dày (Bismuth) giúp loại trừ ngay phân đen giả.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 88, Mục 2.2 - Ỉa ra máu)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Phan-den-gia",
            "Sat",
            "Bismuth",
            "Rifampicin"
        ]
    },
    {
        "id": "PED55-B11",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Chảy máu hậu môn trực tràng",
        "front": "Đặc điểm lâm sàng của Chảy máu do nguyên nhân hậu môn và trực tràng theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tính chất máu: Máu bao giờ cũng ĐỎ TƯƠI, ra ngay ở đầu bãi phân hoặc cuối bãi phân THÀNH VỆT BAO PHỦ NGOÀI KHUÔN PHÂN (máu không trộn lẫn vào phân).<br>• Các nguyên nhân thường gặp: Nứt kẽ hậu môn, polyp hậu môn - trực tràng, trĩ, loét hậu môn.<br>• Triệu chứng kèm theo: Trẻ rặn nhiều, táo bón khóc thét khi đi cầu (nứt kẽ hậu môn) hoặc đau quặn bụng mót rặn (hội chứng lỵ).<br>• Ảnh hưởng toàn thân: Lượng máu mất thường ít, hiếm khi gây ảnh hưởng tới huyết động hay toàn trạng.<br><br><b>💡 Giải thích của AI:</b><br>Chảy máu do nứt kẽ hậu môn là nguyên nhân số 1 ở trẻ táo bón; chỉ cần điều trị mềm phân và bôi thuốc là khỏi hoàn toàn.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 88, Mục 2.3 - Hậu môn trực tràng)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Hau-mon-truc-trang",
            "Nut-ke-hau-mon",
            "Polyp"
        ]
    },
    {
        "id": "PED55-B12",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Đánh giá thiếu máu & sốc",
        "front": "Các dấu hiệu lâm sàng quan trọng cần đánh giá tình trạng thiếu máu và sốc mất máu cấp tính ở trẻ theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Da và niêm mạc xanh nhợt, lòng bàn tay của trẻ mất màu hồng.<br>2) Các đầu chi lạnh, thời gian phục hồi màu da móng tay chậm (CRT > 2 giây).<br>3) Khát nước dữ dội và vã mồ hôi trộm.<br>4) Rối loạn tri giác (bứt rứt, kích thích, li bì, hôn mê) và tiến tới sốc mất máu.<br>5) Mạch nhanh nhỏ, huyết áp tụt kẹp.<br><br><b>💡 Giải thích của AI:</b><br>Khát nước dữ dội và CRT kéo dài > 2s là 2 dấu hiệu lâm sàng sớm cảnh báo giảm thể tích tuần hoàn trước khi huyết áp tụt.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 88 - 89, Mục 2.4.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Thieu-mau",
            "Soc-mat-mau",
            "Huyet-dong"
        ]
    },
    {
        "id": "PED55-B13",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Quy luật số 100",
        "front": "Quy luật số 100 ở trẻ lớn giúp ước tính mất khoảng bao nhiêu % thể tích máu theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ở trẻ lớn, khi phát hiện đồng thời:<br>1) Huyết áp tâm thu giảm xuống DƯỚI 100 mmHg.<br>2) Mạch nhanh tăng lên TRÊN 100 lần/phút.<br>• Ý nghĩa: Trẻ ĐÃ MẤT KHOẢNG 20% KHỐI LƯỢNG MÁU TOÀN CƠ THỂ!<br><br><b>💡 Giải thích của AI:</b><br>Mất 20% thể tích máu là ngưỡng bắt đầu xuất hiện mất bù tuần hoàn, đòi hỏi phải lập ngay đường truyền tĩnh mạch để bồi phụ thể tích cấp cứu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89, Mục 2.4.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Quy-luat-100",
            "Mat-20-phan-tram-mau"
        ]
    },
    {
        "id": "PED55-B14",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Dấu hiệu mất máu tiếp diễn",
        "front": "Biểu hiện lâm sàng nào qua theo dõi 2 thời điểm chứng tỏ trẻ đang mất tiếp một khối lượng máu đáng kể?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khi theo dõi qua 2 thời điểm liên tiếp phát hiện:<br>• Mạch tăng nhanh thêm TRÊN 20 LẦN/PHÚT.<br>• Đồng thời Huyết áp tâm thu GIẢM ĐI 10 mmHg.<br>→ Khẳng định trẻ ĐÃ MẤT TIẾP MỘT KHỐI LƯỢNG MÁU ĐÁNG KỂ và xuất huyết vẫn đang tiếp diễn dữ dội.<br><br><b>💡 Giải thích của AI:</b><br>Mạch leo thang và huyết áp trượt dốc là chỉ dấu xuất huyết chưa cầm, phải chuẩn bị máu khẩn và hội chẩn nội soi/phẫu thuật cấp cứu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89, Mục 2.4.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Mat-mau-tiep-dien",
            "Mach-tang-HA-giam"
        ]
    },
    {
        "id": "PED55-B15",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Đánh giá máu còn chảy qua Sonde",
        "front": "Các dấu hiệu theo dõi lâm sàng và vai trò của sonde dạ dày trong đánh giá xuất huyết tiêu hóa đã ngừng hay còn tiếp tục chảy?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dấu hiệu lâm sàng: Theo dõi mạch, huyết áp, lượng nước tiểu mỗi 15 - 30 phút/lần; nếu trẻ còn vật vã li bì, mạch nhanh huyết áp dao động, nôn/ỉa máu tiếp là máu còn chảy.<br>• Vai trò đặt sonde dạ dày: Nếu do nguyên nhân dạ dày tá tràng, đặt sonde dạ dày hút ra: nếu sau 3 - 6 TIẾNG VẪN THẤY CÓ MÁU ĐỎ TƯƠI thì chứng tỏ MÁU VẪN ĐANG TIẾP TỤC CHẢY.<br>• Xét nghiệm: Hemoglobin và Hematocrit giảm dần qua các thời điểm thử lại trong ngày.<br><br><b>💡 Giải thích của AI:</b><br>Hút sonde dạ dày sau 3 - 6 giờ có máu tươi là tiêu chuẩn khách quan khẳng định ổ loét hoặc búi giãn tĩnh mạch chưa cầm máu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89, Mục 2.4.3)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Sonde-da-day",
            "Mau-con-chay",
            "3-6-gio"
        ]
    },
    {
        "id": "PED55-B16",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Dấu hiệu định hướng nguyên nhân",
        "front": "Các biểu hiện lâm sàng định hướng nguyên nhân loét dạ dày, tăng áp lực tĩnh mạch cửa và chảy máu đường mật?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Viêm loét dạ dày tá tràng: Tiền sử đau bụng thượng vị theo chu kỳ hoặc liên quan bữa ăn, ợ chua.<br>2) Xuất huyết do giãn tĩnh mạch thực quản: Hội chứng tăng áp lực tĩnh mạch cửa trong xơ gan hoặc teo hẹp tĩnh mạch cửa gồm Lách to, Cổ trướng, Tuần hoàn bàng hệ cửa - chủ ở bụng.<br>3) Chảy máu đường mật: sốt, gan to, nhiễm khuẩn đường mật.<br><br><b>💡 Giải thích của AI:</b><br>Khám thấy lách to kèm tuần hoàn bàng hệ định hướng nôn máu do vỡ giãn tĩnh mạch thực quản. Ngoài barem: tam chứng kinh điển của chảy máu đường mật (tam chứng Quincke/Sandblom) là đau hạ sườn phải, vàng da, xuất huyết tiêu hóa.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89, Mục 2.5 - Biểu hiện khác)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Tang-ap-cua",
            "Sandblom",
            "Loet-da-day"
        ]
    },
    {
        "id": "PED55-B17",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Nội soi tiêu hóa cấp cứu",
        "front": "Thời điểm chỉ định, tỷ lệ chẩn đoán và lưu ý an toàn trước khi tiến hành Nội soi tiêu hóa cấp cứu ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thời điểm tiến hành: Trong 24 GIỜ ĐẦU TIÊN sau khi tình trạng huyết động đã được hồi sức ổn định.<br>• Tỷ lệ chẩn đoán nguyên nhân: Đạt 70% ở trẻ em (và 85 - 95% ở người lớn); nội soi muộn thường chỉ thấy tổn thương phối hợp không còn chảy máu.<br>• Lưu ý an toàn sinh tử:<br>1) KHÔNG nội soi ngay khi bệnh nhân đang chảy máu ồ ạt trụy mạch cần mổ khẩn.<br>2) Nếu trẻ rối loạn tri giác: Bắt buộc gây mê toàn thân và đặt nội khí quản bảo vệ đường thở.<br>3) Trước khi nội soi: BẮT BUỘC CHỤP PHIM BỤNG KHÔNG CHUẨN BỊ ĐỂ LOẠI TRỪ TẮC RUỘT HOẶC TRÀN KHÍ PHÚC MẠC (chống chỉ định nội soi).<br><br><b>💡 Giải thích của AI:</b><br>Bơm hơi nội soi khi đã có thủng tạng rỗng sẽ làm tràn khí màng bụng ồ ạt gây chèn ép tim phổi tử vong.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89, Mục 3.1 - Nội soi)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Noi-soi",
            "24-gio",
            "Chong-chi-dinh"
        ]
    },
    {
        "id": "PED55-B18",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "X-quang dạ dày cản quang",
        "front": "Vì sao Chụp dạ dày - thực quản cản quang cổ điển không còn được đặt ra đầu tiên trong chẩn đoán xuất huyết tiêu hóa theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạn chế kỹ thuật: Chụp cản quang cổ điển không thể phát hiện được:<br>1) Các tổn thương niêm mạc nông cấp tính và trợt loét cấp.<br>2) Đa số các vết loét thực quản nông.<br>3) Bỏ sót tới 50% các trường hợp giãn tĩnh mạch thực quản.<br>• Độ nhạy thấp: Chỉ phát hiện được 45% loét dạ dày, 60% loét tá tràng và miệng nối.<br>• Không chứng minh được chảy máu: Thấy ổ loét trên X-quang cũng không khẳng định được ổ loét đó có đang gây chảy máu hay không.<br><br><b>💡 Giải thích của AI:</b><br>Nội soi tiêu hóa mềm đã thay thế hoàn toàn X-quang cản quang trong chẩn đoán xuất huyết tiêu hóa.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 89 - 90, Mục 3.2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "X-quang-can-quang",
            "Han-che"
        ]
    },
    {
        "id": "PED55-B19",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Chụp động mạch chọn lọc",
        "front": "Vai trò của Chụp động mạch chọn lọc trong chẩn đoán xuất huyết tiêu hóa theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kỹ thuật: Chụp chọn lọc động mạch thân tạng, động mạch mạc treo tràng trên và động mạch mạc treo tràng dưới.<br>• Vai trò: Giúp xác định chính xác vị trí mạch máu đang thoát thuốc cản quang (vị trí chảy máu).<br>• Phát hiện nguyên nhân: Đôi khi phát hiện trực tiếp được các nguyên nhân dị dạng mạch máu (u mạch, phình mạch, dị dạng động tĩnh mạch AVM) hoặc các khối u đường tiêu hóa.<br><br><b>💡 Giải thích của AI:</b><br>Chụp mạch chọn lọc vừa có giá trị chẩn đoán vừa mở đường cho can thiệp nút mạch (thuyên tắc mạch cầm máu) mà không cần mổ mở.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 90, Mục 3.2.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Chup-mach-chon-loc",
            "Di-dang-mach"
        ]
    },
    {
        "id": "PED55-B20",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Chụp xạ hình Tc99m",
        "front": "Nguyên lý, tốc độ chảy máu phát hiện được và độ chính xác của Chụp nhấp nháy bằng Technetium-99m (Tc99m)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nguyên lý: Tiêm tĩnh mạch hỗn dịch Tc99m (chất đồng vị phóng xạ có thời gian bán phân hủy ngắn trong mạch &lt; 25 phút), chất này sẽ tập trung vào vị trí đang chảy máu và được máy chụp ghi lại.<br>• Khả năng phát hiện: Rất nhạy, phát hiện được dòng chảy máu siêu nhỏ với tốc độ chỉ từ 0,1 ml/phút.<br>• Độ chính xác: Độ đặc hiệu 95%, độ nhạy 85%.<br>• Nguyên nhân âm tính giả: Nồng độ phóng xạ quá loãng do máu chảy quá nhanh; hoặc giảm tưới máu thứ phát túi thừa Meckel do xoắn ruột, lồng ruột kèm theo.<br><br><b>💡 Giải thích của AI:</b><br>Chụp xạ hình Tc99m pertechnetate là tiêu chuẩn vàng chẩn đoán Túi thừa Meckel vì chất này bắt giữ đặc hiệu các tế bào niêm mạc dạ dày lạc chỗ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 90, Mục 3.2.3)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Xa-hinh-Tc99m",
            "Meckel",
            "0-1-ml-phut"
        ]
    },
    {
        "id": "PED55-B21",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Mổ thăm dò",
        "front": "Chỉ định Soi đại tràng và Mổ thăm dò trong xuất huyết tiêu hóa ở trẻ em theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Soi trực tràng sigma và toàn bộ đại tràng: Chỉ định khi bệnh nhi có chảy máu đường tiêu hóa dưới và xuất huyết trực tràng, đại tràng.<br>• Mổ thăm dò: Chỉ định khi tất cả các biện pháp thăm dò không xâm nhập và nội soi thất bại không tìm được nguyên nhân chảy máu; phẫu thuật mở nhằm mục đích VỪA TIẾN HÀNH CHẨN ĐOÁN, VỪA TIẾN HÀNH ĐIỀU TRỊ CẦM MÁU.<br><br><b>💡 Giải thích của AI:</b><br>Mổ thăm dò là quyết định sống còn cuối cùng khi bệnh nhân mất máu ồ ạt đe dọa tử vong mà các phương tiện nội soi/chụp mạch không định vị được tổn thương.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 90, Mục 3.3 & 3.4)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Soi-dai-trang",
            "Mo-tham-do"
        ]
    },
    {
        "id": "PED55-B22",
        "track": "barem_goc",
        "type": "basic",
        "section": "B4",
        "category": "Sơ đồ tiếp cận XHTH Trên",
        "front": "Sơ đồ các bước tiếp cận chẩn đoán xuất huyết tiêu hóa TRÊN và biện luận kết quả dịch hút sonde dạ dày?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Các bước tiếp cận: Đánh giá bệnh sử → Triệu chứng lâm sàng → Dấu hiệu sinh tồn & Huyết động → Xét nghiệm cơ bản → ĐẶT SONDE DẠ DÀY HÚT.<br>• Biện luận kết quả dịch hút sonde dạ dày:<br>1) Dịch hút có MÀU VÀNG CỦA MẬT và KHÔNG CÓ MÁU: Chắc chắn loại trừ chảy máu trên góc Treitz.<br>2) Dịch hút TRONG KHÔNG CÓ MÁU nhưng KHÔNG CÓ MẬT: CHƯA THỂ LOẠI TRỪ xuất huyết ở tá tràng (máu ở tá tràng chưa trào ngược vào dạ dày).<br>3) Dịch hút CÓ MÁU: Khẳng định xuất huyết tiêu hóa trên.<br><br><b>💡 Giải thích của AI:</b><br>Bẫy thi lâm sàng: Hút sonde dạ dày dịch trong không có máu thì CHƯA ĐƯỢC loại trừ loét tá tràng, chỉ khi nào thấy dịch vàng có mật mới chắc chắn loại trừ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 90 - 91, Mục 4 - Tiếp cận)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Tiep-can-XHTH-Tren",
            "Sonde-da-day",
            "Dich-mat"
        ]
    },
    {
        "id": "PED55-B23",
        "track": "barem_goc",
        "type": "basic",
        "section": "B4",
        "category": "Sơ đồ tiếp cận XHTH Dưới",
        "front": "Sơ đồ phân nhánh tiếp cận chẩn đoán xuất huyết tiêu hóa DƯỚI theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chia thành 4 nhánh tiếp cận:<br>1) Nhánh triệu chứng bụng cấp (lồng ruột, xoắn ruột): Ổn định huyết động → Chuyển trung tâm ngoại khoa → Siêu âm, X-quang.<br>2) Nhánh mất máu nặng hoặc đang chảy máu dữ dội: Ổn định huyết động → Tầm soát Meckel, XHTH trên ồ ạt → Xạ hình, nội soi tiêu hóa, nội soi ổ bụng.<br>3) Nhánh triệu chứng viêm đại tràng: Phân định &gt; 7 ngày (nội soi) vs &lt; 5 ngày (cấy phân tìm vi khuẩn lỵ/ký sinh trùng).<br>4) Nhánh chảy máu trực tràng hậu môn: Khám hậu môn phân định có táo bón (nứt kẽ hậu môn) vs không táo bón (nội soi tìm polyp).<br><br><b>💡 Giải thích của AI:</b><br>Sơ đồ phân 4 nhánh này giúp phân loại cực nhanh bệnh nhân thuộc diện ngoại khoa cấp cứu, nhiễm trùng hay bệnh lý hậu môn lành tính.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 91, Sơ đồ XHTH dưới)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Tiep-can-XHTH-Duoi",
            "4-nhanh"
        ]
    },
    {
        "id": "PED55-B24",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "Phân định <span style=\"color:#74c0fc\"><b>XHTH trên</b></span> và <span style=\"color:#74c0fc\"><b>XHTH dưới</b></span> theo mốc giải phẫu nào? Dấu hiệu lâm sàng đặc hiệu của XHTH trên?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• XHTH trên: tổn thương xuất huyết từ <span style=\"color:#74c0fc\"><b>góc Treitz tới miệng</b></span>.<br>• XHTH dưới: tổn thương chảy máu từ <span style=\"color:#74c0fc\"><b>góc Treitz tới hậu môn</b></span>.<br>• Dấu hiệu đặc hiệu của XHTH trên: <span style=\"color:#ff6b6b\"><b>nôn ra máu</b></span> và <span style=\"color:#ff6b6b\"><b>ỉa phân đen</b></span>.<br>• Chảy máu ít: có thể không nôn ra máu. Chảy máu nhiều: nôn ra máu tươi hoặc ỉa máu đỏ sẫm.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5 và 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "XHTH-tren", "Goc-Treitz"]
    },
    {
        "id": "PED55-B25",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Viêm loét thực quản</b></span> gây XHTH ở trẻ em: cơ chế, biểu hiện, chẩn đoán và điều trị theo tuổi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: biến chứng của <span style=\"color:#74c0fc\"><b>trào ngược dạ dày thực quản (RGO)</b></span>.<br>• Biểu hiện: trẻ trớ hoặc nôn ra máu lẫn thức ăn; thường chảy máu ít, rỉ rỉ, kèm <span style=\"color:#ff6b6b\"><b>thiếu máu nhược sắc</b></span>.<br>• Chẩn đoán xác định: <span style=\"color:#51cf66\"><b>nội soi</b></span>.<br>• Điều trị:<br>– Trẻ <span style=\"color:#ffd43b\"><b>trước 18 tháng</b></span>: nội khoa bằng primperan hoặc motilium kết hợp tagamet hoặc ranitidin, prepulsif.<br>– Trẻ <span style=\"color:#ffd43b\"><b>sau 18 tháng</b></span>: điều trị nội khoa không đỡ cần phẫu thuật.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Hướng dẫn trào ngược ở trẻ em NASPGHAN/ESPGHAN 2018 (Rosen et al., JPGN 2018) không khuyến cáo dùng metoclopramid (primperan) hay domperidon (motilium) thường quy vì lợi ích không rõ và nguy cơ tác dụng phụ; thuốc ức chế acid ưu tiên là PPI. Ranitidin đã bị rút khỏi thị trường nhiều nước từ 2020 (tạp chất NDMA). Khi thi ghi phác đồ barem.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Viem-loet-thuc-quan", "RGO"]
    },
    {
        "id": "PED55-B26",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Viêm loét thực quản do uống thuốc</b></span> thường do những thuốc nào và cơ chế gây loét?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thuốc hay gặp: <span style=\"color:#74c0fc\"><b>doxycyclin</b></span>, <span style=\"color:#74c0fc\"><b>tetracyclin</b></span>, <span style=\"color:#74c0fc\"><b>aspirin</b></span>.<br>• Cơ chế: uống thuốc <span style=\"color:#ff6b6b\"><b>không uống nước kèm theo</b></span> làm viên thuốc tắc lại ở thực quản, gây loét cấp do tiếp xúc.<br><br><b>💡 Giải thích của AI:</b><br>Phòng ngừa: uống thuốc với nhiều nước và không nằm ngay sau uống (Ngoài barem).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Loet-thuc-quan-do-thuoc"]
    },
    {
        "id": "PED55-B27",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Vỡ giãn tĩnh mạch thực quản</b></span> trong tăng áp lực tĩnh mạch cửa: hình ảnh nội soi, các vị trí giãn khác và biểu hiện lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nội soi: đám chảy máu thành tia hoặc mảng, đám máu đông, tụ máu hoặc tĩnh mạch giãn bị sói mòn.<br>• Vị trí khác: giãn, vỡ đám rối tĩnh mạch <span style=\"color:#74c0fc\"><b>tâm phình vị</b></span> (thấy khi soi ngược lại); hiếm hơn là vỡ phình giãn tĩnh mạch <span style=\"color:#74c0fc\"><b>tá tràng</b></span>.<br>• Lâm sàng: <span style=\"color:#ff6b6b\"><b>nôn máu tươi, nhiều, nặng</b></span>, kèm triệu chứng tăng áp lực tĩnh mạch cửa: <span style=\"color:#74c0fc\"><b>tuần hoàn bàng hệ</b></span>, <span style=\"color:#74c0fc\"><b>cổ trướng</b></span>, <span style=\"color:#74c0fc\"><b>gan lách to</b></span>, xơ gan.<br>• Tăng áp lực tĩnh mạch cửa trước gan do khối u hoặc tắc tĩnh mạch cửa; sau gan: <span style=\"color:#ff6b6b\"><b>hội chứng Budd-Chiari</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Gian-TMTQ", "Tang-ap-cua"]
    },
    {
        "id": "PED55-B28",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Hội chứng Mallory-Weiss</b></span>: hoàn cảnh xuất hiện, tổn thương và nguyên tắc điều trị theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hoàn cảnh: thường thứ phát sau <span style=\"color:#74c0fc\"><b>nôn dữ dội</b></span>.<br>• Tổn thương: <span style=\"color:#ff6b6b\"><b>vết nứt dọc tâm vị</b></span>, đau xuất hiện cùng nôn ra máu.<br>• Điều trị: để trẻ <span style=\"color:#51cf66\"><b>nghỉ ngơi</b></span>, dùng <span style=\"color:#51cf66\"><b>thuốc chống nôn</b></span> tránh làm vết nứt nặng thêm.<br><br><b>💡 Giải thích của AI:</b><br>Phần lớn chảy máu Mallory-Weiss tự cầm.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Mallory-Weiss"]
    },
    {
        "id": "PED55-B29",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Viêm dạ dày - tá tràng</b></span> gây XHTH thường gặp trong những hoàn cảnh nào? Hình thái tổn thương?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hoàn cảnh: <span style=\"color:#74c0fc\"><b>ngộ độc</b></span>, <span style=\"color:#74c0fc\"><b>stress</b></span>, <span style=\"color:#74c0fc\"><b>nhiễm khuẩn nặng</b></span>, Scholein–Henoch, dị ứng thức ăn, thuốc, <span style=\"color:#74c0fc\"><b>hội chứng huyết tán tăng ure huyết</b></span>.<br>• Hay gặp ở <span style=\"color:#ffd43b\"><b>giai đoạn sơ sinh</b></span>: yếu tố nguy cơ là nhiễm khuẩn, đẻ non, thiếu O₂, stress, dị ứng, kèm hội chứng xuất huyết ở trẻ sơ sinh.<br>• Hình thái: xuất huyết dạng chấm, vết trợt nhỏ hoặc vết loét hoại tử niêm mạc dạ dày, gọi là <span style=\"color:#74c0fc\"><b>loét cấp tính</b></span> hay <span style=\"color:#74c0fc\"><b>loét thứ phát</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Viem-da-day"]
    },
    {
        "id": "PED55-B30",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Loét dạ dày - tá tràng</b></span> gây XHTH ở trẻ em: tỷ lệ, phân loại nguyên nhân, vị trí và khi nào nghĩ tới hội chứng Zollinger-Ellison?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tỷ lệ: chiếm <span style=\"color:#ffd43b\"><b>30 - 40%</b></span> nôn ra máu nhiều ở trẻ em.<br>• Loét cấp tính hoặc thứ phát: do stress, sau mổ, bỏng rộng hoặc do thuốc (aspirin, cortisol).<br>• Loét tiên phát, mạn tính: liên quan đau bụng kéo dài.<br>• Vị trí loét chảy máu: dạ dày <span style=\"color:#ffd43b\"><b>1/3</b></span>, tá tràng <span style=\"color:#ffd43b\"><b>2/3</b></span>.<br>• Nhiều vết loét mạn tính khu trú ở hành tá tràng → tìm <span style=\"color:#ff6b6b\"><b>hội chứng Zollinger – Ellison</b></span>.<br>• Nội soi: mô tả tổn thương, tìm dấu hiệu chảy máu tái phát, các mạch máu, điểm mạch chảy máu ở miệng ổ loét.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: loét tiên phát ở trẻ lớn hay liên quan Helicobacter pylori.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Loet-DDTT", "Zollinger-Ellison"]
    },
    {
        "id": "PED55-B31",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên",
        "front": "<span style=\"color:#ff6b6b\"><b>Chảy máu đường mật</b></span> ở trẻ em: nguyên nhân, biểu hiện lâm sàng và tiên lượng theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nguyên nhân: biến chứng của <span style=\"color:#74c0fc\"><b>nhiễm khuẩn đường mật</b></span>, <span style=\"color:#74c0fc\"><b>áp xe gan do giun</b></span>, ung thư gan mật hoặc viêm đường mật xuất huyết.<br>• Lâm sàng: cơn đau bụng dữ dội, sốt, gan to, thể trạng nhiễm trùng, <span style=\"color:#ff6b6b\"><b>nôn ra máu tái phát nhiều lần ngày càng gần nhau</b></span> và ỉa phân đen.<br>• Tiên lượng: thường nặng, trẻ dễ bị <span style=\"color:#ff6b6b\"><b>sốc</b></span>, thường cần chỉ định <span style=\"color:#51cf66\"><b>phẫu thuật</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Mục 5.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Chay-mau-duong-mat"]
    },
    {
        "id": "PED55-B32",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH trên",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH trên</b></span> ở <span style=\"color:#ffd43b\"><b>trẻ nhũ nhi</b></span> gồm những gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dạ dày: <span style=\"color:#74c0fc\"><b>viêm dạ dày do stress</b></span>.<br>• Vị trí khác: <span style=\"color:#74c0fc\"><b>thiếu hụt vitamin K</b></span>, nhiễm trùng huyết, chấn thương (đặt sonde mũi dạ dày), dị ứng đạm sữa bò.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Bảng nguyên nhân XHTH trên)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-tren", "Nhu-nhi"]
    },
    {
        "id": "PED55-B33",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH trên",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH trên</b></span> ở trẻ <span style=\"color:#ffd43b\"><b>2 - 5 tuổi</b></span> theo vị trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thực quản: viêm thực quản; giãn tĩnh mạch thực quản; hội chứng Mallory-Weiss.<br>• Dạ dày: viêm dạ dày; loét dạ dày; giãn tĩnh mạch dạ dày.<br>• Tá tràng: viêm tá tràng; loét tá tràng.<br>• Vị trí khác: nuốt hóa chất ăn mòn; dị vật đường tiêu hóa; dùng thuốc NSAIDs.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Bảng nguyên nhân XHTH trên)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-tren", "2-5-tuoi"]
    },
    {
        "id": "PED55-B34",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH trên",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH trên</b></span> ở <span style=\"color:#ffd43b\"><b>trẻ lớn</b></span> theo vị trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thực quản: viêm thực quản; hội chứng Mallory-Weiss; giãn tĩnh mạch thực quản.<br>• Dạ dày: dị dạng mạch ở dạ dày (<span style=\"color:#74c0fc\"><b>Dieulafoy</b></span>); giãn tĩnh mạch dạ dày trong tăng áp lực tĩnh mạch cửa.<br>• Tá tràng: bệnh máu khó đông.<br>• Vị trí khác: polyps; bệnh Crohn; giãn tĩnh mạch; dị ứng đạm sữa bò; rối loạn đông máu; nuốt hóa chất ăn mòn; dị vật tiêu hóa; dùng thuốc NSAIDs.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Bảng nguyên nhân XHTH trên)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-tren", "Tre-lon"]
    },
    {
        "id": "PED55-B35",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "Hai dấu hiệu chủ yếu của <span style=\"color:#ff6b6b\"><b>XHTH dưới</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Ỉa máu toàn bãi</b></span>: máu đã tiêu hóa màu đen, nâu hoặc chưa kịp tiêu hóa màu đỏ sẫm, đỏ tươi khi chảy nhiều; không nôn ra máu; nội soi thực quản dạ dày tá tràng không có tổn thương. Vị trí càng thấp, chảy càng nhiều thì phân càng đỏ tươi. Tổn thương thường ở hỗng tràng, hồi tràng hoặc đại tràng.<br>2) <span style=\"color:#74c0fc\"><b>Chảy máu hậu môn, trực tràng</b></span>: máu đỏ tươi ở đầu, cuối bãi hoặc bao ngoài phân, <span style=\"color:#ff6b6b\"><b>không bao giờ toàn bãi</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93 - 94, Mục 5.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "XHTH-duoi"]
    },
    {
        "id": "PED55-B36",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "Kể các nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới tại ruột non</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>U máu ruột non</b></span> (Angiome).<br>2) <span style=\"color:#ff6b6b\"><b>Viêm ruột hoại tử</b></span>: trẻ lớn – trẻ sơ sinh; phân đen khắm, nhiễm trùng – nhiễm độc, bụng chướng hoặc biểu hiện viêm phúc mạc thủng ruột, có thể sốc.<br>3) <span style=\"color:#74c0fc\"><b>Nhiễm khuẩn đường tiêu hóa</b></span>: tiêu chảy xâm nhập (Coli gây bệnh, Salmonella, lị trực trùng, lị amibe).<br>4) <span style=\"color:#ff6b6b\"><b>Lồng ruột</b></span>.<br>5) <span style=\"color:#74c0fc\"><b>Viêm loét túi thừa Meckel</b></span>.<br>6) <span style=\"color:#74c0fc\"><b>Bệnh Schonlein – Henoch</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Ruot-non"]
    },
    {
        "id": "PED55-B37",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "<span style=\"color:#ff6b6b\"><b>Lồng ruột</b></span> gây XHTH dưới: biểu hiện giai đoạn sớm, giai đoạn muộn và các tỷ lệ theo tuổi trong barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sớm: nôn, đau bụng từng cơn, sờ thấy búi lồng, thăm hậu môn trực tràng rỗng.<br>• Muộn: ỉa máu phân màu đỏ sẫm, bụng chướng, khó sờ búi lồng.<br>• Tỷ lệ: <span style=\"color:#ffd43b\"><b>&gt; 80%</b></span> lồng ruột ở trẻ <span style=\"color:#ffd43b\"><b>dưới 2 tuổi</b></span>; <span style=\"color:#ffd43b\"><b>45%</b></span> từ <span style=\"color:#ffd43b\"><b>4 – 10 tháng</b></span>; ỉa máu nhầy ở <span style=\"color:#ffd43b\"><b>36%</b></span> trẻ &lt; 1 tuổi.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94 - 95, Mục 5.2.1 và 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Long-ruot"]
    },
    {
        "id": "PED55-B38",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "<span style=\"color:#ff6b6b\"><b>Viêm loét túi thừa Meckel</b></span> gây XHTH: cơ chế, đặc điểm chảy máu, tỷ lệ theo tuổi và xét nghiệm chẩn đoán xác định?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: niêm mạc túi thừa là <span style=\"color:#74c0fc\"><b>niêm mạc dạ dày lạc chỗ</b></span>, gây loét, chảy máu.<br>• Đặc điểm (trẻ &lt; 18 tháng): chảy máu <span style=\"color:#ff6b6b\"><b>không kèm đau bụng</b></span>, thường chảy nhiều phải truyền máu, hoặc chảy ít nhưng hay tái phát.<br>• Tỷ lệ: <span style=\"color:#ffd43b\"><b>60%</b></span> chảy máu do Meckel xảy ra ở trẻ <span style=\"color:#ffd43b\"><b>&lt; 2 tuổi</b></span>; <span style=\"color:#ffd43b\"><b>40%</b></span> có nhiều đợt tái phát.<br>• Chẩn đoán xác định: <span style=\"color:#51cf66\"><b>chụp nhấp nháy đồng vị phóng xạ Tc99</b></span>.",
        "extra": "<b>⚖️ Đối chiếu:</b> Barem tự mâu thuẫn: mục 5.2.1 ghi \"trẻ có cơn đau bụng, xuất huyết vừa và nặng\", mục 5.2.2 ghi \"chảy máu không kèm theo đau bụng\". Kinh điển và Nelson 22e: chảy máu do Meckel thường không đau. Khi thi nêu \"không kèm đau bụng\".<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94 - 95, Mục 5.2.1 và 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Meckel", "Tc99"]
    },
    {
        "id": "PED55-B39",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "XHTH trong <span style=\"color:#ff6b6b\"><b>bệnh Schonlein – Henoch</b></span>: tỷ lệ, tổn thương, vị trí hay gặp và cách xác định chẩn đoán trên lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tỷ lệ: <span style=\"color:#ffd43b\"><b>30%</b></span> trường hợp ban xuất huyết khớp có tổn thương đường tiêu hóa (đau bụng, nôn, ỉa ra máu).<br>• Tổn thương: chấm máu, đám máu tụ thành ruột; hay gặp ở <span style=\"color:#74c0fc\"><b>hỗng, hồi tràng</b></span>, hiếm ở tá tràng hoặc đại tràng.<br>• Biểu hiện: đau bụng dữ dội, nôn nhiều, ỉa phân đen hoặc xuất huyết trực tràng; xuất huyết thường không nhiều, ít khi phải truyền máu.<br>• Biểu hiện tiêu hóa thường <span style=\"color:#ff6b6b\"><b>đi trước</b></span>; <span style=\"color:#74c0fc\"><b>ban xuất huyết cân đối ở các chi</b></span> (2 chi dưới, chi trên) cho phép xác định chẩn đoán trên lâm sàng.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94 - 95, Mục 5.2.1 và 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Henoch"]
    },
    {
        "id": "PED55-B40",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới",
        "front": "Nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH do đại tràng, trực tràng</b></span> theo barem và đặc điểm từng nguyên nhân?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Viêm đại tràng chảy máu</b></span>: do nhiễm khuẩn, dị ứng thức ăn, sữa bò hoặc bệnh Crohn (đau bụng, giảm cân, sốt, ỉa phân lỏng có máu kéo dài).<br>2) <span style=\"color:#74c0fc\"><b>Polyp trực tràng</b></span>: polyp đơn độc (<span style=\"color:#ffd43b\"><b>2/3</b></span>); khu trú trực tràng, đại tràng sigma (<span style=\"color:#ffd43b\"><b>3/4</b></span>); máu tươi ra cuối bãi; có thể là bệnh polyp (<span style=\"color:#ff6b6b\"><b>hội chứng Peutz – Jeghers</b></span>).<br>3) <span style=\"color:#74c0fc\"><b>Nứt hậu môn</b></span>: rất thường gặp, nhất là sau táo bón; máu ra trước khi ỉa hoặc thành vệt ở đoạn phân, kèm đau; vị trí nứt thường ở <span style=\"color:#ffd43b\"><b>6 – 12 giờ</b></span>.",
        "extra": "<b>⚖️ Đối chiếu:</b> Barem ghi hai cách khác nhau: mục 5.2.1 \"polyp đơn độc 2/3, ở trực tràng – sigma 3/4\", mục 5.2.2 \"2/3 polyp ở trực tràng và sigma, 3/4 là polyp đơn độc\". Polyp thiếu niên ở trẻ em phần lớn là đơn độc và nằm ở đại tràng trái/trực tràng (Nelson 22e).<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.1)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Dai-truc-trang", "Polyp", "Nut-hau-mon"]
    },
    {
        "id": "PED55-B41",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới theo tuổi",
        "front": "Nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới ở trẻ sơ sinh</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• XHTH vào <span style=\"color:#ffd43b\"><b>ngày thứ 2 – 3</b></span>: biểu hiện xuất huyết toàn thân do <span style=\"color:#ff6b6b\"><b>thiếu vitamin K</b></span> (đông máu thiếu yếu tố <span style=\"color:#ffd43b\"><b>II, VII, IX và X</b></span>).<br>• <span style=\"color:#ff6b6b\"><b>Viêm ruột non hoại tử</b></span> ở trẻ sơ sinh, đẻ non.<br>• <span style=\"color:#ff6b6b\"><b>Xoắn toàn bộ ruột non</b></span> do quay, cuốn bất thường mạc treo ruột.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "So-sinh", "Vitamin-K"]
    },
    {
        "id": "PED55-B42",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới theo tuổi",
        "front": "Nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới ở trẻ bú mẹ dưới 18 tháng</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Ỉa chảy nhiễm khuẩn (hội chứng lị)</b></span>: Salmonella, trực trùng lị, Campylobacter, E. coli xâm nhập; ỉa phân có máu mũi.<br>2) <span style=\"color:#ff6b6b\"><b>Lồng ruột cấp tính</b></span>.<br>3) <span style=\"color:#74c0fc\"><b>Không dung nạp protein sữa bò hoặc đậu nành</b></span>: ỉa phân lỏng có máu sau khi ăn sữa, biểu hiện viêm đại tràng.<br>4) <span style=\"color:#74c0fc\"><b>Loét túi thừa Meckel</b></span>: chảy máu không đau.<br>5) <span style=\"color:#74c0fc\"><b>Nứt hậu môn</b></span> khi trẻ táo bón.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Duoi-18-thang"]
    },
    {
        "id": "PED55-B43",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới theo tuổi",
        "front": "Nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới ở trẻ trước tuổi đi học (&lt; 6 tuổi)</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Viêm trực tràng, đại tràng do nhiễm khuẩn, nhiễm kí sinh khuẩn.<br>2) <span style=\"color:#ff6b6b\"><b>Viêm ruột non hoại tử trẻ lớn</b></span>: <span style=\"color:#74c0fc\"><b>hội chứng Pigbel</b></span>.<br>3) XHTH trong <span style=\"color:#74c0fc\"><b>bệnh Schonlein – Henoch</b></span>.<br>4) <span style=\"color:#74c0fc\"><b>Polyp trực tràng, đại tràng</b></span>: máu tươi ra đầu hoặc cuối bãi, bao ngoài cục phân, chảy ít nhưng hay tái phát; <span style=\"color:#ffd43b\"><b>2/3</b></span> ở trực tràng và sigma; <span style=\"color:#ffd43b\"><b>3/4</b></span> là polyp đơn độc.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "Duoi-6-tuoi", "Pigbel"]
    },
    {
        "id": "PED55-B44",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH dưới theo tuổi",
        "front": "Nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới ở trẻ tuổi học đường (6 - 18 tuổi)</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Viêm ruột xuất huyết</b></span>: viêm ruột hoại tử, amibe, lị → phân máu nhầy toàn bãi; viêm hậu môn, trực tràng → phân máu tươi nhầy.<br>2) Nguyên nhân khác: viêm loét túi thừa Meckel, vỡ túi máu ở ruột non, viêm đại tràng, chảy máu...",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục 5.2.2)",
        "tags": ["PED-55", "Barem-goc", "Nguyen-nhan", "6-18-tuoi"]
    },
    {
        "id": "PED55-B45",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH dưới",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới</b></span> thường gặp ở <span style=\"color:#ffd43b\"><b>trẻ nhũ nhi</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Viêm đại tràng không đặc hiệu; nứt kẽ hậu môn; dị ứng sữa; ruột đôi; xoắn ruột; bệnh Hirschsprung; viêm ruột hoại tử; chảy máu do can thiệp.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Bảng nguyên nhân XHTH dưới)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-duoi", "Nhu-nhi"]
    },
    {
        "id": "PED55-B46",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH dưới",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới</b></span> thường gặp ở trẻ <span style=\"color:#ffd43b\"><b>2 - 5 tuổi</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Polyps; nứt kẽ hậu môn; nhiễm trùng đường ruột; lồng ruột; viêm loét túi thừa Meckel; Scholein Henoch; huyết tán ure máu cao; u bạch huyết; tăng sản mạch máu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Bảng nguyên nhân XHTH dưới)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-duoi", "2-5-tuoi"]
    },
    {
        "id": "PED55-E01",
        "track": "ebm",
        "type": "basic",
        "section": "E0",
        "category": "Phân tầng mức độ mất máu",
        "front": "Bảng phân tầng mức độ mất máu trong xuất huyết tiêu hóa ở trẻ em theo % thể tích tuần hoàn và dấu hiệu lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Mức độ Nhẹ (Mất &lt; 10% thể tích máu): Mạch và huyết áp hoàn toàn bình thường, trẻ tỉnh táo, CRT &lt; 2s.<br>2) Mức độ Vừa (Mất 10 - 20% thể tích máu): Mạch nhanh nhẹ, huyết áp tư thế giảm, da xanh nhẹ, khát nước, CRT 2 - 3s.<br>3) Mức độ Nặng - Sốc mất máu (Mất > 20% thể tích máu): Trẻ li bì/vật vã, mạch nhanh nhỏ khó bắt, huyết áp tâm thu tụt hoặc kẹp, chi lạnh ẩm, CRT > 3s, thiểu niệu hoặc vô niệu.<br><br><b>💡 Giải thích của AI:</b><br>Thể tích máu của trẻ em khoảng 70 - 80 ml/kg; tính nhanh thể tích tuần hoàn giúp bác sĩ ước lượng chính xác lượng máu mất và thể tích dịch cần bù.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Phân tầng mức độ mất máu nhi khoa (Nelson Pediatrics)",
        "tags": [
            "PED-55",
            "EBM",
            "Phan-tang-mat-mau",
            "Soc-mat-mau"
        ]
    },
    {
        "id": "PED55-E02",
        "track": "ebm",
        "type": "basic",
        "section": "E1",
        "category": "Tỷ lệ BUN / Creatinine",
        "front": "Cơ chế sinh hóa và ý nghĩa của tỷ lệ BUN / Creatinine máu trong phân biệt xuất huyết tiêu hóa TRÊN với DƯỚI khi trẻ không nôn máu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế sinh hóa: Khi máu chảy ở đường tiêu hóa trên (dạ dày, tá tràng), lượng lớn protein trong hồng cầu bị tiêu hóa ở ruột non giải phóng acid amin, vi khuẩn ruột thoái giáng thành amoniac hấp thu về gan tổng hợp thành Urê (BUN); trong khi chức năng lọc của cầu thận vẫn bình thường (Creatinine máu không tăng).<br>• Ý nghĩa chẩn đoán: TỶ LỆ BUN / CREATININE > 30 (hoặc Ure / Creatinine > 100 theo mmol/L) gợi ý mạnh xuất huyết tiêu hóa TRÊN dù trẻ chỉ đi ngoài phân đen mà không nôn ra máu.<br><br><b>💡 Giải thích của AI:</b><br>Trong xuất huyết tiêu hóa dưới, máu thoát nhanh ra ngoài qua đại tràng không bị tái hấp thu protein nên tỷ lệ BUN/Creatinine hoàn toàn bình thường (&lt; 20 - 30).",
        "extra": "📖 Nguồn: EBM Lâm sàng — Tỷ lệ BUN/Creatinine trong chẩn đoán XHTH",
        "tags": [
            "PED-55",
            "EBM",
            "BUN-Creatinine",
            "Phan-biet-Tren-Duoi"
        ]
    },
    {
        "id": "PED55-E03",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Tháo lồng ruột bằng hơi",
        "front": "Quy trình tháo lồng ruột bằng hơi dưới màn huỳnh quang tăng sáng: áp lực bơm hơi an toàn và dấu hiệu tháo lồng thành công?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kỹ thuật: Đặt ống thông hậu môn có bóng chèn, bơm hơi từ từ vào đại tràng dưới hướng dẫn của màn huỳnh quang tăng sáng (hoặc siêu âm).<br>• Áp lực bơm hơi: Tăng dần từ từ, giới hạn áp lực theo quy trình của từng trung tâm và luôn tuân thủ hướng dẫn của khoa (không dùng con số cố định trong thẻ này).<br>• Dấu hiệu tháo lồng thành công:<br>1) Thấy khối lồng thụt lùi dần qua góc gan, manh tràng rồi biến mất hoàn toàn.<br>2) Hơi ào ạt tràn vào các quai hồi tràng ở giữa bụng.<br>3) Bụng trẻ xẹp mềm, trẻ hết khóc thét và ngủ yên.<br><br><b>💡 Giải thích của AI:</b><br>Tháo lồng bằng hơi là lựa chọn điều trị đầu tay của lồng ruột cấp ở trẻ không có chống chỉ định, giúp trẻ tránh được phẫu thuật mở bụng; áp lực cụ thể cần theo protocol của đơn vị và điều kiện an toàn.",
        "extra": "📖 Nguồn: Khuyến cáo lồng ruột ở trẻ em (Ministry/ESPGHAN/ESPR) — tham chiếu hướng dẫn đơn vị. [Số áp lực cụ thể chưa được xác minh bằng nguồn tin cậy — đã bỏ khỏi thẻ.]",
        "tags": [
            "PED-55",
            "EBM",
            "Thao-long-bang-hoi",
            "Long-ruot",
            "Ap-luc-an-toan"
        ]
    },
    {
        "id": "PED55-E04",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Chống chỉ định tháo lồng bằng hơi",
        "front": "Các chống chỉ định tuyệt đối của thủ thuật Tháo lồng ruột bằng hơi ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Gồm 4 chống chỉ định tuyệt đối:<br>1) Có dấu hiệu Viêm phúc mạc (bụng chướng căng, đề kháng thành bụng, phản ứng phúc mạc).<br>2) Đã có biến chứng Thủng ruột (hình ảnh liềm hơi dưới cơ hoành trên X-quang bụng đứng).<br>3) Trẻ trong tình trạng Sốc nhiễm trùng nhiễm độc nặng hoặc sốc giảm thể tích chưa hồi sức.<br>4) Lồng ruột đến muộn có dấu hiệu hoại tử ruột rõ rệt.<br><br><b>💡 Giải thích của AI:</b><br>Bơm hơi khi ruột đã hoại tử hoặc thủng sẽ làm vỡ toác ruột, gây tràn khí tràn phân ồ ạt vào ổ phúc mạc dẫn đến tử vong nhanh chóng.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Chống chỉ định tháo lồng bằng hơi",
        "tags": [
            "PED-55",
            "EBM",
            "Chong-chi-dinh",
            "Thao-long-hoi",
            "Thung-ruot"
        ]
    },
    {
        "id": "PED55-E05",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Baveno VII - Tam giác xử trí vỡ giãn",
        "front": "Quy tắc 'Tam giác xử trí vỡ giãn tĩnh mạch thực quản' theo đồng thuận Baveno VII cập nhật?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Gồm 3 mũi nhọn phối hợp sớm (khuyến cáo đặt mục tiêu trong 12 giờ đầu):<br>1) Dược lý co mạch tạng: Khởi động Octreotide truyền tĩnh mạch liên tục ngay khi nghi ngờ vỡ giãn (trước cả khi nội soi).<br>2) Kháng sinh dự phòng sớm: Ceftriaxone đường tĩnh mạch (1 g/24 giờ) cho bệnh nhân xuất huyết tiêu hóa do tăng áp cửa, bắt đầu từ lúc nhập viện.<br>3) Nội soi can thiệp cầm máu: Thắt vòng cao su EVL sau khi ổn định huyết động.<br><br><b>💡 Giải thích của AI:</b><br>Theo Baveno VII, dùng thuốc co mạch tạng và kháng sinh NGAY TẠI THỜI ĐIỂM TIẾP NHẬN làm giảm áp lực tĩnh mạch cửa và nguy cơ nhiễm trùng trước khi đưa máy nội soi vào can thiệp.",
        "extra": "📖 Nguồn: de Franchis R et al. Baveno VII — Renewing consensus in portal hypertension. J Hepatol 2022;76(4):959–974, PMID 35120736.",
        "tags": [
            "PED-55",
            "EBM",
            "Baveno-VII",
            "Tam-giac-xu-tri",
            "Gian-TMTQ"
        ]
    },
    {
        "id": "PED55-E06",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Baveno VII - Kháng sinh dự phòng",
        "front": "Vì sao mọi bệnh nhân vỡ giãn TMTQ do tăng áp cửa bắt buộc phải dùng Kháng sinh dự phòng (Ceftriaxone) ngay khi nhập viện?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: Xuất huyết tiêu hóa làm suy giảm miễn dịch, tạo điều kiện cho vi khuẩn đường ruột chuyển vị vào máu và dịch báng.<br>• Lợi ích theo khuyến cáo Baveno VII: Kháng sinh dự phòng (thường Ceftriaxone) giúp:<br>1) Giảm nguy cơ nhiễm trùng huyết và viêm phúc mạc tiên phát do vi khuẩn (SBP).<br>2) Giảm tỷ lệ tái xuất huyết sớm trong tuần đầu.<br>3) Cải thiện tỷ lệ sống còn ở bệnh nhân xơ gan xuất huyết tiêu hóa.<br><br><b>💡 Giải thích của AI:</b><br>Nhiễm trùng giải phóng nội độc tố kích hoạt co mạch gan và tăng áp lực cửa thứ phát làm bục búi giãn; dùng kháng sinh là biện pháp gián tiếp hạ áp lực cửa.",
        "extra": "📖 Nguồn: de Franchis R et al. J Hepatol 2022;76(4):959–974, PMID 35120736 (kháng sinh dự phòng từ lúc nhập viện; ceftriaxone 1 g/24 h).",
        "tags": [
            "PED-55",
            "EBM",
            "Ceftriaxone",
            "Khang-sinh-du-phong",
            "Baveno-VII"
        ]
    },
    {
        "id": "PED55-E07",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Cạm bẫy phân đỏ/đen giả",
        "front": "Cạm bẫy lâm sàng số 1: Nhầm lẫn phân đen/đỏ do thức ăn, thuốc hoặc nuốt máu với xuất huyết tiêu hóa thực sự?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cạm bẫy: Thấy phân có màu đen hoặc đỏ vội vàng chẩn đoán xuất huyết tiêu hóa và truyền dịch/nội soi không cần thiết.<br>• Phản xạ kiểm tra bắt buộc:<br>1) Soi kỹ mũi họng xem có ổ chảy máu cam nuốt xuống không.<br>2) Hỏi kỹ tiền sử ăn uống (tiết canh, đỗ đen, cam thảo) và dùng thuốc (viên sắt, Bismuth, Rifampicin).<br>3) Ở trẻ sơ sinh: Bắt buộc làm test Apt-Downey loại trừ nuốt máu mẹ.<br>4) Xét nghiệm tìm máu ẩn trong phân (FOBT) để khẳng định có thành phần hồng cầu thực sự.<br><br><b>💡 Giải thích của AI:</b><br>Bình tĩnh hỏi bệnh sử dùng thuốc và khám mũi họng giúp tránh được 30% các ca nhập viện 'xuất huyết tiêu hóa giả'.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy chẩn đoán xuất huyết tiêu hóa giả (Phần IV)",
        "tags": [
            "PED-55",
            "EBM",
            "Cam-bay",
            "Phan-den-gia",
            "Apt-Downey"
        ]
    },
    {
        "id": "PED55-E08",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Cạm bẫy ỉa máu đỏ tươi từ dạ dày",
        "front": "Cạm bẫy lâm sàng số 2: Vì sao bệnh nhân chảy máu ở Dạ dày - tá tràng lại có thể biểu hiện bằng ĐẠI TIỆN RA MÁU ĐỎ TƯƠI Ồ ẠT?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: Khi tổn thương ở dạ dày tá tràng chảy máu với tốc độ CỰC KỲ NHANH VÀ LƯỢNG MÁU CỰC LỚN (> 1000 ml ở người lớn hoặc > 20% thể tích máu ở trẻ em), máu là chất nhuận tràng mạnh kích thích nhu động ruột tăng bóp dữ dội.<br>• Hậu quả: Dòng máu bị tống qua toàn bộ chiều dài ruột non và đại tràng chỉ trong 1 - 2 giờ, men tiêu hóa và vi khuẩn ruột CHƯA KỊP THOÁI GIÁNG HEMOGLOBIN thành hematin màu đen → Trẻ đi ngoài ra máu đỏ tươi toàn bãi kèm tụt huyết áp.<br>• Phản xạ lâm sàng: Bệnh nhân đi ngoài ra máu đỏ tươi kèm tụt huyết áp/sốc bắt buộc phải đặt sonde dạ dày hút loại trừ xuất huyết tiêu hóa TRÊN ồ ạt trước khi soi đại tràng.<br><br><b>💡 Giải thích của AI:</b><br>Khoảng 10 - 15% các ca đại tiện máu đỏ tươi ồ ạt kèm tụt huyết áp có nguồn gốc thực sự từ đường tiêu hóa TRÊN.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy đại tiện máu tươi do XHTH trên ồ ạt",
        "tags": [
            "PED-55",
            "EBM",
            "Cam-bay",
            "Mau-tuoi-tu-da-day",
            "Soc-mat-mau"
        ]
    },
    {
        "id": "PED55-E09",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Cạm bẫy bỏ sót Túi thừa Meckel",
        "front": "Cạm bẫy lâm sàng số 3: Vì sao Túi thừa Meckel là nguyên nhân rất hay bị bỏ sót hoặc chẩn đoán muộn ở trẻ nhỏ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trẻ hoàn toàn không đau bụng, không sốt, không nôn; ngoài đợt đi ngoài ra máu trẻ chơi đùa ăn uống bình thường.<br>2) Nội soi dạ dày và nội soi đại tràng thông thường HOÀN TOÀN ÂM TÍNH (vì túi thừa nằm ở đoạn giữa hồi tràng ruột non không với tới được).<br>3) Siêu âm ổ bụng thông thường rất khó phát hiện túi thừa Meckel.<br>• Phản xạ chuẩn: Trẻ nhỏ &lt; 5 tuổi đi ngoài ra máu đỏ tái diễn từng đợt không đau bụng kèm nội soi trên/dưới âm tính → BẮT BUỘC CHỈ ĐỊNH XẠ HÌNH Tc99m PERTECHNETATE để tìm niêm mạc dạ dày lạc chỗ.<br><br><b>💡 Giải thích của AI:</b><br>Càng nội soi đại tràng nhiều lần càng bỏ sót Meckel; chỉ có xạ hình Tc99m hoặc phẫu thuật nội soi ổ bụng mới giải quyết được chẩn đoán.",
        "extra": "<b>⚖️ Đối chiếu:</b> Giáo trình (barem) ghi xạ hình Tc99m có độ nhạy khoảng 85%, độ đặc hiệu khoảng 95%. Meta-analysis trẻ em (Yan P, Jiang S. J Pediatr (Rio J) 2023;99(5):425–431, PMID 37277097; 16 nghiên cứu, 1.115 trẻ) ghi nhận độ nhạy gộp 80% (95% CI 0,73–0,86), độ đặc hiệu gộp 95% (95% CI 0,86–0,98). Kết luận: xạ hình Tc99m có giá trị chẩn đoán tốt nhưng bỏ sót một phần; âm tính không loại trừ hoàn toàn Meckel.",
        "tags": [
            "PED-55",
            "EBM",
            "Cam-bay",
            "Meckel",
            "Xa-hinh-Tc99m"
        ]
    },
    {
        "id": "PED55-E10",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Cạm bẫy dịch truyền chống sốc",
        "front": "Cạm bẫy lâm sàng số 4: Sai lầm tai hại khi dùng dung dịch Glucose hoặc dung dịch nhược trương để chống sốc mất máu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sai lầm: Truyền dung dịch Glucose 5% hoặc NaCl nhược trương 0,45% để bù thể tích cho trẻ đang sốc mất máu.<br>• Hậu quả tai hại:<br>1) Dung dịch nhược trương và đường không giữ được trong lòng mạch, thoát nhanh vào mô kẽ và tế bào.<br>2) Gây hạ Natri máu cấp tính dẫn đến PHÙ NÃO CẤP, CO GIẬT VÀ TỬ VONG.<br>3) Làm loãng máu trầm trọng nhưng không nâng được thể tích tuần hoàn hiệu dụng.<br>• Nguyên tắc bất di bất dịch: CHỈ DÙNG DỊCH TINH THỂ ĐẲNG TRƯƠNG (NaCl 0,9% hoặc Ringer Lactat) liều 20 ml/kg để chống sốc mất máu.<br><br><b>💡 Giải thích của AI:</b><br>Một đứa trẻ sốc mất máu tử vong vì phù não do truyền dịch ngọt là thảm họa y khoa hoàn toàn có thể phòng tránh được.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy dịch truyền chống sốc (ESPGHAN)",
        "tags": [
            "PED-55",
            "EBM",
            "Cam-bay",
            "Cam-Glucose",
            "Phu-nao"
        ]
    },
    {
        "id": "PED55-E11",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Cạm bẫy lưu bóng Sengstaken quá hạn",
        "front": "Cạm bẫy lâm sàng số 5: Biến chứng chết người khi quên xả bóng chèn ép thực quản (Sonde Sengstaken-Blakemore) quá 48 giờ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Biến chứng chết người: Hoại tử thiếu máu cục bộ thành thực quản dẫn đến LOÉT VÀ THỦNG THỰC QUẢN, gây viêm trung thất mủ tối cấp tử vong.<br>• Quy tắc an toàn nghiêm ngặt:<br>1) Bơm bóng thực quản áp lực vừa đủ 25 - 30 mmHg (đo bằng áp kế).<br>2) Cứ sau mỗi 12 giờ phải xả bóng thực quản tạm thời 10 - 15 phút để hồi phục tưới máu niêm mạc.<br>3) TUYỆT ĐỐI KHÔNG ĐƯỢC LƯU BÓNG QUÁ 24 - 48 GIỜ.<br>4) Sau 24 giờ phải chuyển bệnh nhân đi nội soi thắt vòng cao su hoặc phẫu thuật.<br><br><b>💡 Giải thích của AI:</b><br>Sonde chèn ép bóng chỉ mua thời gian quý giá trong 24 giờ đầu để đưa bệnh nhân đến trung tâm nội soi can thiệp, không phải là biện pháp điều trị duy trì.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy lưu bóng Sengstaken-Blakemore",
        "tags": [
            "PED-55",
            "EBM",
            "Cam-bay",
            "Sengstaken",
            "Hoai-tu-thuc-quan"
        ]
    },
    {
        "id": "PED55-E12",
        "track": "ebm",
        "type": "basic",
        "section": "E5",
        "category": "Phân loại Forrest trong loét dạ dày",
        "front": "Ý nghĩa của Bảng phân loại Forrest trong nội soi loét dạ dày tá tràng và nguy cơ tái xuất huyết?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Forrest I (Đang chảy máu hoạt động):<br>1) Ia: Máu phun thành tia (nguy cơ tái chảy máu cao nhất).<br>2) Ib: Máu rỉ rả liên tục (nguy cơ tái chảy máu cao).<br>• Forrest II (Dấu hiệu chảy máu gần đây):<br>1) IIa: Mạch máu lộ trần không chảy máu (nguy cơ trung bình-cao).<br>2) IIb: Cục máu đông bám đáy ổ loét (nguy cơ trung bình).<br>3) IIc: Cặn sắc tố đen đáy ổ loét (nguy cơ thấp).<br>• Forrest III: Đáy ổ loét sạch, phủ giả mạc trắng (nguy cơ thấp nhất).<br>• Chỉ định can thiệp nội soi: BẮT BUỘC cầm máu với Forrest Ia, Ib, IIa; cân nhắc với IIb.<br><br><b>💡 Giải thích của AI:</b><br>Phân loại Forrest định hướng quyết định có cần cầm máu nội soi hay không. Các tỷ lệ tái chảy máu cụ thể theo từng nhóm khác nhau giữa các nghiên cứu nên không đưa con số cố định vào thẻ này.",
        "extra": "📖 Nguồn: Forrest classification (Forrest JA et al., Lancet 1974); khuyến cáo nội soi ESGE/ESPGHAN: Thomson M, Tringali A et al. JPGN 2017;64(1):133–153, PMID 27622898.",
        "tags": [
            "PED-55",
            "EBM",
            "Forrest",
            "Noi-soi",
            "Loet-da-day"
        ]
    },
    {
        "id": "PED55-E13",
        "track": "ebm",
        "type": "basic",
        "section": "E5",
        "category": "Quản lý Dị ứng đạm sữa bò",
        "front": "Nguyên tắc chuyển đổi sữa và điều trị xuất huyết tiêu hóa do Dị ứng đạm sữa bò ở trẻ nhũ nhi theo khuyến cáo ESPGHAN?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trẻ bú mẹ hoàn toàn: Tiếp tục cho bú mẹ, MẸ BẮT BUỘC KIÊNG HOÀN TOÀN SỮA BÒ và tất cả các chế phẩm từ sữa bò (phô mai, sữa chua, bơ) trong ít nhất 2 - 4 tuần.<br>2) Trẻ ăn sữa công thức:<br>• Lựa chọn hàng đầu: Chuyển sang SỮA THỦY PHÂN HOÀN TOÀN (Extensively Hydrolyzed Formula - eHF).<br>• Lựa chọn cho thể nặng/thất bại eHF: Chuyển sang SỮA CÔNG THỨC ACID AMIN (Amino Acid-based Formula - AAF).<br>3) Không dùng sữa đậu nành cho trẻ &lt; 6 tháng tuổi vì nguy cơ dị ứng chéo cao.<br>• Tiên lượng: Thường lành tính; tỷ lệ dung nạp lại sữa bò tăng theo tuổi (khoảng 50% lúc 1 tuổi, &gt; 75% lúc 3 tuổi, &gt; 90% lúc 6 tuổi).<br><br><b>💡 Giải thích của AI:</b><br>Dị ứng đạm sữa bò gây viêm trực tràng đại tràng dị ứng (FPIAP) là bệnh lý lành tính, thường đáp ứng sau vài ngày đổi chế độ ăn/sữa.",
        "extra": "📖 Nguồn: ESPGHAN Committee on Nutrition — Koletzko S et al. JPGN 2012;55(2):221–229, PMID 22569527 (tỷ lệ dung nạp theo tuổi).",
        "tags": [
            "PED-55",
            "EBM",
            "Di-ung-sua-bo",
            "eHF",
            "AAF",
            "ESPGHAN"
        ]
    },
    {
        "id": "PED55-E14",
        "track": "ebm",
        "type": "basic",
        "section": "E5",
        "category": "Thuật toán 4 bước cấp cứu",
        "front": "4 bước trong Thuật toán tiếp cận cấp cứu một trẻ Xuất huyết tiêu hóa cấp tính tại khoa cấp cứu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bước 1: Hồi sức cấp cứu ABCD (Đường thở, Oxy, 2 đường truyền ngoại vi kim lớn, Dịch tinh thể đẳng trương 20 ml/kg chống sốc).<br>• Bước 2: Đánh giá độ nặng và Lấy máu xét nghiệm khẩn (Công thức máu, Nhóm máu, Phản ứng chéo, Đông máu, Khí máu, Đặt sonde dạ dày hút).<br>• Bước 3: Dược lý đặc hiệu sớm:<br>1) Nếu nghi xuất huyết trên do loét: PPI (Omeprazole 1 mg/kg TM).<br>2) Nếu nghi tăng áp cửa / vỡ giãn TMTQ: Octreotide TM + Kháng sinh Ceftriaxone.<br>3) Sơ sinh/nhũ nhi: Tiêm Vitamin K1 1 - 5 mg.<br>• Bước 4: Hội chẩn can thiệp đích (Nội soi cầm máu trong 12 - 24 giờ sau khi ổn định huyết động; Chụp mạch can thiệp hoặc Phẫu thuật mở nếu thất bại nội soi).<br><br><b>💡 Giải thích của AI:</b><br>Thứ tự vàng: Hồi sức huyết động LUÔN ĐI TRƯỚC chẩn đoán nguyên nhân; huyết động chưa ổn định thì không được đưa trẻ đi nội soi.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Thuật toán tiếp cận cấp cứu XHTH nhi khoa",
        "tags": [
            "PED-55",
            "EBM",
            "Thuat-toan-cap-cuu",
            "4-buoc",
            "ABCD"
        ]
    },
    {
        "id": "PED55-B47",
        "track": "ebm",
        "type": "basic",
        "section": "B1",
        "category": "Thăm trực tràng",
        "front": "Vai trò và những thông tin giá trị thu được từ động tác Thăm trực tràng bằng tay trong xuất huyết tiêu hóa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Xác định trực tiếp sự hiện diện và màu sắc của máu dính trên găng (máu đỏ tươi, mận chín hay phân đen).<br>2) Phát hiện các tổn thương thực thể tại chỗ: Nứt kẽ hậu môn, polyp trực tràng thấp có cuống, búi trĩ, loét trực tràng.<br>3) Trong lồng ruột cấp: Phát hiện nhầy máu màu mận chín dính găng (thậm chí sờ thấy đầu khối lồng nếu lồng ruột xuống thấp tới bóng trực tràng).<br><br><b>💡 Giải thích của AI:</b><br>Thăm trực tràng bằng ngón tay trỏ đeo găng có bôi trơn là động tác khám bắt buộc không được bỏ qua ở mọi trẻ có xuất huyết tiêu hóa.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 88, Mục 2.3)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Tham-truc-trang",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED55-B48",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng nguyên nhân XHTH dưới",
        "front": "Theo bảng tổng hợp của barem, nguyên nhân <span style=\"color:#ff6b6b\"><b>XHTH dưới</b></span> thường gặp ở <span style=\"color:#ffd43b\"><b>trẻ lớn</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nứt kẽ hậu môn; nhiễm trùng đường ruột; polyps; ruột viêm (IBD); u bạch huyết; Scholein Henoch; tăng sản mạch máu; huyết tán ure máu cao; chảy máu do can thiệp.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Bảng nguyên nhân XHTH dưới)",
        "tags": ["PED-55", "Barem-goc", "Bang", "XHTH-duoi", "Tre-lon"]
    },
    {
        "id": "PED55-B49",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Đánh giá",
        "front": "Điều quan trọng nhất khi đánh giá XHTH là gì? Dấu hiệu lâm sàng tốt nhất đánh giá tình trạng <span style=\"color:#ff6b6b\"><b>mất máu</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Quan trọng nhất: xác định <span style=\"color:#74c0fc\"><b>mức độ và tốc độ mất máu</b></span> và <span style=\"color:#74c0fc\"><b>yếu tố nguy cơ</b></span>.<br>• Dấu hiệu tốt nhất: thay đổi nhịp tim và huyết áp khi chuyển trẻ từ <span style=\"color:#74c0fc\"><b>nằm ngửa sang ngồi</b></span>: nhịp tim tăng <span style=\"color:#ffd43b\"><b>20 nhịp/phút</b></span> hoặc huyết áp tâm thu giảm từ <span style=\"color:#ffd43b\"><b>10 mmHg</b></span> trở lên.<br>• Yếu tố nguy cơ: rối loạn đông máu, nhiễm trùng huyết, chấn thương; dấu hiệu liên quan: bệnh gan lách, vàng da, xơ gan.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6)",
        "tags": ["PED-55", "Barem-goc", "Dieu-tri", "Danh-gia-mat-mau"]
    },
    {
        "id": "PED55-B50",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Đánh giá",
        "front": "XHTH <span style=\"color:#74c0fc\"><b>không ảnh hưởng huyết động</b></span>: cần làm xét nghiệm gì? Nêu các mục đích của <span style=\"color:#51cf66\"><b>đặt sonde dạ dày, hút và rửa nước muối</b></span> trong XHTH trên?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Xét nghiệm cơ bản: công thức máu, nhóm máu, chức năng gan và thận, đông máu.<br>• Mục đích đặt sonde dạ dày, hút và rửa:<br>1) Chẩn đoán.<br>2) Xác định tốc độ chảy máu.<br>3) Kiểm tra chảy máu liên tục hoặc tái phát.<br>4) Làm sạch dạ dày trước nội soi.<br>5) Ngăn ngừa <span style=\"color:#ff6b6b\"><b>bệnh não gan</b></span> ở bệnh nhân xơ gan.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6)",
        "tags": ["PED-55", "Barem-goc", "Dieu-tri", "Sonde-da-day"]
    },
    {
        "id": "PED55-B51",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Đông máu",
        "front": "Chỉ định <span style=\"color:#51cf66\"><b>vitamin K</b></span> và xử trí <span style=\"color:#ff6b6b\"><b>rối loạn đông máu</b></span> trong XHTH trẻ em theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vitamin K tiêm <span style=\"color:#ffd43b\"><b>1 - 2 mg/liều</b></span>: khuyến cáo cho <span style=\"color:#74c0fc\"><b>trẻ sơ sinh</b></span>, ngay cả khi chưa có kết quả đông máu.<br>• Rối loạn đông máu (<span style=\"color:#ffd43b\"><b>INR &gt; 1,5</b></span> hoặc thời gian thromboplastin một phần bất thường): <span style=\"color:#51cf66\"><b>huyết tương tươi đông lạnh</b></span> <span style=\"color:#ffd43b\"><b>10 ml/kg</b></span> ban đầu.<br>• Rối loạn đông máu nặng, nhất là khi phải hạn chế dịch: thử dùng <span style=\"color:#51cf66\"><b>huyết tương kết tủa lạnh</b></span>.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6)",
        "tags": ["PED-55", "Barem-goc", "Dieu-tri", "Vitamin-K", "Dong-mau"]
    },
    {
        "id": "PED55-E15",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "So sánh thuốc co mạch tạng",
        "front": "So sánh cơ chế và ưu nhược điểm của Octreotide vs Terlipressin vs Vasopressin trong điều trị vỡ giãn tĩnh mạch thực quản?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Octreotide (Chất đồng vận Somatostatin tổng hợp): Lựa chọn hàng đầu ở trẻ em; co mạch tạng chọn lọc cao, rất an toàn, ít tác dụng phụ toàn thân; nhược điểm là thời gian bán hủy ngắn cần truyền liên tục.<br>2) Terlipressin (Chất đồng vận Vasopressin tổng hợp tác dụng kéo dài): Tiêm tĩnh mạch ngắt quãng mỗi 4 - 6 giờ (thuận tiện khi không có bơm tiêm điện); hiệu quả hạ áp lực cửa tương đương Octreotide; ít co mạch vành hơn Vasopressin cổ điển.<br>3) Vasopressin cổ điển: Hiện nay ít sử dụng vì gây co mạch toàn thân dữ dội, nguy cơ thiếu máu cơ tim và thiếu máu cục bộ tạng ruột.<br><br><b>💡 Giải thích của AI:</b><br>Ở bệnh nhi, Octreotide truyền liên tục là lựa chọn an toàn nhất do không gây biến chứng tim mạch như Vasopressin.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Dược lý co mạch tạng (Baveno VII / ESPGHAN)",
        "tags": [
            "PED-55",
            "EBM",
            "Octreotide",
            "Terlipressin",
            "Baveno-VII"
        ]
    },
    {
        "id": "PED55-E16",
        "track": "ebm",
        "type": "basic",
        "section": "E5",
        "category": "Xử trí XHTH trong NEC",
        "front": "Phác đồ hồi sức nội khoa toàn diện khi trẻ sơ sinh bị xuất huyết tiêu hóa do Viêm ruột hoại tử (NEC)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Ngừng ăn đường miệng hoàn toàn (NPO): Nhịn ăn tối thiểu 7 - 14 ngày.<br>2) Đặt sonde dạ dày cỡ lớn hút liên tục giảm áp ổ bụng.<br>3) Kháng sinh phổ rộng đường tĩnh mạch bao phủ vi khuẩn Gram âm, Gram dương và kỵ khí (Ampicillin + Gentamicin + Metronidazol; hoặc Meropenem + Vancomycin).<br>4) Nuôi dưỡng tĩnh mạch hoàn toàn (TPN).<br>5) Bồi phụ thể tích, duy trì huyết động và truyền chế phẩm máu (tiểu cầu, huyết tương tươi).<br>6) Chụp X-quang bụng mỗi 6 - 8 giờ để theo dõi dấu hiệu thủng ruột (liềm hơi dưới hoành).<br><br><b>💡 Giải thích của AI:</b><br>Ngừng ăn đường miệng và giảm áp dạ dày là chìa khóa cho quai ruột được nghỉ ngơi phục hồi tưới máu mô.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Xử trí nội khoa Viêm ruột hoại tử NEC",
        "tags": [
            "PED-55",
            "EBM",
            "NEC",
            "Hoi-suc-noi-khoa"
        ]
    },
    {
        "id": "PED55-E17",
        "track": "ebm",
        "type": "basic",
        "section": "E5",
        "category": "10 Quy tắc vàng thực chiến",
        "front": "Kể tên 5 trong số các Quy tắc vàng thực chiến tại giường khi xử trí trẻ xuất huyết tiêu hóa cấp tính?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hồi sức huyết động LUÔN ĐI TRƯỚC chẩn đoán nguyên nhân (không nội soi khi huyết động chưa ổn).<br>2) Tuyệt đối cấm dùng dịch truyền Glucose hoặc dung dịch nhược trương để chống sốc mất máu.<br>3) Luôn đặt sonde dạ dày kiểm tra dịch: Dịch trong không có máu CHƯA LOẠI TRỪ loét tá tràng.<br>4) Trẻ nhỏ đại tiện máu đỏ ồ ạt mà bụng mềm hoàn toàn không đau → nghĩ ngay Túi thừa Meckel.<br>5) Không lưu bóng chèn ép thực quản Sengstaken-Blakemore quá 24 - 48 giờ vì nguy cơ hoại tử thủng thực quản.<br><br><b>💡 Giải thích của AI:</b><br>5 quy tắc này đúc kết từ những sai lầm lâm sàng nguy hiểm nhất, giúp bác sĩ cấp cứu hành động an toàn và quyết đoán.",
        "extra": "📖 Nguồn: EBM Lâm sàng — 10 Quy tắc vàng thực chiến tại giường",
        "tags": [
            "PED-55",
            "EBM",
            "Quy-tac-vang",
            "Thuc-chien"
        ]
    },
    {
        "id": "PED55-B52",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Hồi sức",
        "front": "Các biện pháp <span style=\"color:#ff6b6b\"><b>hồi sức ổn định huyết động</b></span> cho trẻ XHTH mất nhiều máu theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tư thế, oxy: <span style=\"color:#51cf66\"><b>ủ ấm</b></span>, đầu thấp chân cao, <span style=\"color:#51cf66\"><b>thở O₂</b></span>. Nếu có nôn máu: kê đầu cao <span style=\"color:#ffd43b\"><b>30 - 40°</b></span> phòng hít máu vào phổi. Xuất huyết nặng: <span style=\"color:#51cf66\"><b>đặt nội khí quản</b></span> bảo đảm đường thở.<br>• Đường truyền: đặt <span style=\"color:#ffd43b\"><b>2 đường truyền tĩnh mạch</b></span> – tĩnh mạch trung tâm, đo áp lực tĩnh mạch trung tâm.<br>• Xét nghiệm cấp: nhóm máu, tế bào máu, tiểu cầu, thời gian prothrombin, hemoglobin, khí máu.<br>• Theo dõi: mạch, huyết áp, tinh thần, khối lượng máu tiếp tục mất, nôn, ỉa máu.<br><br><b>💡 Giải thích của AI:</b><br>Hemoglobin lúc đầu chưa phản ánh trung thực lượng máu mất (giai đoạn đầu chưa pha loãng), sau đó có thể giảm do truyền dịch.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Hoi-suc"
        ]
    },
    {
        "id": "PED55-B53",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Truyền dịch",
        "front": "Hai mục đích của <span style=\"color:#51cf66\"><b>truyền máu</b></span> trong XHTH và dịch truyền dùng giai đoạn đầu khi chờ máu theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Mục đích: (1) <span style=\"color:#74c0fc\"><b>phục hồi khối lượng tuần hoàn</b></span> (đánh giá qua mạch, huyết áp); (2) <span style=\"color:#74c0fc\"><b>bảo đảm lượng O₂ cung cấp cho tổ chức</b></span> (đánh giá qua hemoglobin, hematocrit).<br>• Mục tiêu 1 đạt được bằng dịch phân tử lượng cao, dịch thay thế máu; mục tiêu 2 chỉ đạt được nhờ truyền máu.<br>• Giai đoạn đầu khi chờ máu: <span style=\"color:#51cf66\"><b>dung dịch mặn đẳng trương hoặc Ringer lactat</b></span> <span style=\"color:#ffd43b\"><b>20 ml/kg/giờ</b></span> cho tới khi khối lượng tuần hoàn tối thiểu hồi phục (huyết áp tăng), mất dấu hiệu co mạch ngoại biên (vân tím trên da).",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Thực hành nhi hiện nay bù dịch theo từng bolus 10–20 ml/kg trong 5–20 phút và đánh giá lại sau mỗi lần; với sốc mất máu ưu tiên truyền máu sớm (PALS/AHA). Khi thi ghi mốc barem 20 ml/kg/giờ.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96 - 97, Mục 6.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Truyen-dich",
            "Truyen-mau"
        ]
    },
    {
        "id": "PED55-B54",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Truyền dịch",
        "front": "Barem nêu gì về <span style=\"color:#74c0fc\"><b>albumin, plasma, dextran và hetastarch</b></span> trong XHTH?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Albumin và plasma: chỉ dùng khi mất máu nhiều và tiếp tục, vì giai đoạn này có thể suy thở hay sốc phổi do giảm áp lực keo.<br>• Dextran: thận trọng vì có thể ảnh hưởng chức năng tiểu cầu.<br>• Hetastarch: nhũ tương keo nhân tạo, barem ghi dùng có hiệu quả và an toàn.<br>• Lưu ý: truyền khối lượng tuần hoàn nguy hiểm nhất với xuất huyết do <span style=\"color:#ff6b6b\"><b>giãn tĩnh mạch thực quản</b></span>, do loét.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Dung dịch HES (hetastarch) làm tăng tổn thương thận và tử vong ở bệnh nhân nặng; Cơ quan Dược phẩm châu Âu (EMA) đã hạn chế (2013) và khuyến nghị đình chỉ (2022). Hiện không khuyến cáo dùng HES. Với giãn tĩnh mạch thực quản, bù dịch và máu quá mức làm tăng áp lực cửa và nguy cơ chảy máu lại (Baveno VII). Khi thi ghi theo barem.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97, Mục 6.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Dich-keo"
        ]
    },
    {
        "id": "PED55-B55",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Truyền máu",
        "front": "<span style=\"color:#51cf66\"><b>Truyền máu</b></span> sau khi đã phục hồi khối lượng tuần hoàn theo barem: đích hematocrit, liều khối hồng cầu, trường hợp xơ gan và xử trí sau truyền khối lượng lớn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đích: truyền máu chậm đưa <span style=\"color:#ffd43b\"><b>hematocrit lên 30%</b></span> (khối hồng cầu <span style=\"color:#ffd43b\"><b>10 ml/kg</b></span> ban đầu) hoặc truyền máu; tốc độ phụ thuộc khối lượng máu mất.<br>• Xơ gan (tránh tăng amoniac): truyền <span style=\"color:#74c0fc\"><b>khối hồng cầu</b></span> (ít NH₃ hơn máu toàn phần).<br>• Máu toàn phần có thể gây tăng citrat máu, acid lactic, giảm yếu tố đông máu, giảm tiểu cầu.<br>• Sau mỗi lần truyền <span style=\"color:#ffd43b\"><b>40 - 50 ml/kg</b></span> khối hồng cầu hoặc máu toàn phần: cho <span style=\"color:#51cf66\"><b>calci</b></span>, <span style=\"color:#51cf66\"><b>huyết tương tươi đông lạnh 10 ml/kg</b></span>, tiểu cầu và theo dõi tiểu cầu.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Xu hướng hiện nay là truyền máu hạn chế: ngưỡng Hb khoảng 70 g/L (đích 70–90 g/L) ở bệnh nhân ổn định; với giãn tĩnh mạch thực quản tránh truyền quá mức (Baveno VII, de Franchis et al., J Hepatol 2022, PMID 35120736). Khi thi ghi mốc barem.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97, Mục 6.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Truyen-mau"
        ]
    },
    {
        "id": "PED55-B56",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Thuốc",
        "front": "<span style=\"color:#51cf66\"><b>Thuốc ức chế bơm proton (PPI)</b></span> trong XHTH trẻ em theo barem: các thuốc, đường dùng, liều, mục tiêu pH và tác dụng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thuốc: esomeprazole, lansoprazole, omeprazole, pantoprazole, rabeprazole.<br>• Đường dùng: <span style=\"color:#51cf66\"><b>tiêm tĩnh mạch</b></span>, truyền trong 1 giờ, liều <span style=\"color:#ffd43b\"><b>1 - 3 mg/kg</b></span> để duy trì <span style=\"color:#ffd43b\"><b>pH dạ dày &gt; 6</b></span> trong 24 giờ khi chảy máu hoạt động.<br>• Vượt trội hơn thuốc đối kháng H2 trong chảy máu do loét, XHTH trên.<br>• Tác dụng: giảm nguy cơ tái phát và cần phẫu thuật nhưng <span style=\"color:#ff6b6b\"><b>không ảnh hưởng tỷ lệ tử vong</b></span>; giảm tái phát, nhu cầu truyền máu, thời gian nằm viện; hiệu quả với XHTH ở trẻ em do NSAID.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97, Mục 6.2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "PPI"
        ]
    },
    {
        "id": "PED55-B57",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Thuốc",
        "front": "<span style=\"color:#51cf66\"><b>Thuốc co mạch</b></span> trong XHTH do tăng áp cửa theo barem: hiệu quả, các thuốc, đặc điểm terlipressin và liều octreotide?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ định: cân nhắc <span style=\"color:#ff6b6b\"><b>càng sớm càng tốt</b></span> khi nghi tăng áp cửa là nguyên nhân XHTH; cầm máu <span style=\"color:#ffd43b\"><b>75 - 80%</b></span> trường hợp.<br>• 3 thuốc: terlipressin, somatostatin, octreotide (giảm lưu lượng máu và áp lực mạch máu).<br>• Terlipressin: co mạch toàn thân, nhất là động mạch lách; giảm áp lực tĩnh mạch khoảng <span style=\"color:#ffd43b\"><b>20%</b></span>; ít dùng ở trẻ em; tác dụng phụ <span style=\"color:#ff6b6b\"><b>hạ natri máu, co giật</b></span>.<br>• Octreotide (dẫn xuất somatostatin): co mạch chọn lọc; liều <span style=\"color:#ffd43b\"><b>2 - 5 mcg/kg/giờ</b></span> truyền liên tục, có thể bắt đầu bằng bolus, truyền <span style=\"color:#ffd43b\"><b>ít nhất 5 ngày</b></span> ở bệnh nhân nguy cơ tái phát.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Nhiều phác đồ nhi dùng octreotide bolus 1–2 mcg/kg rồi truyền 1–2 mcg/kg/giờ, kéo dài 2–5 ngày (Baveno VII cho người lớn: 2–5 ngày). Khi thi ghi liều barem.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97 - 98, Mục 6.2.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Thuoc-co-mach",
            "Octreotide"
        ]
    },
    {
        "id": "PED55-B58",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Thuốc",
        "front": "<span style=\"color:#51cf66\"><b>Thuốc chẹn beta giao cảm</b></span> trong tăng áp cửa theo barem: các thuốc, cơ chế và liều ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thuốc: <span style=\"color:#74c0fc\"><b>propranolol</b></span>, nadolol, <span style=\"color:#74c0fc\"><b>carvedilol</b></span> (nghiên cứu nhiều ở người lớn tăng áp cửa).<br>• Cơ chế: giảm cung lượng tim (chẹn β1) và co mạch tạng (chẹn β2) → giảm áp lực cửa; carvedilol có vẻ giảm áp lực tĩnh mạch gan tốt hơn.<br>• Trẻ em: ít dữ liệu, liều dao động <span style=\"color:#ffd43b\"><b>2 - 8 mg/ngày</b></span>.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Chẹn beta không chọn lọc dùng để dự phòng chảy máu lại, không dùng trong giai đoạn đang chảy máu cấp. Ở trẻ em liều propranolol thường tính theo cân nặng và chỉnh để giảm nhịp tim khoảng 25%; dữ liệu nhi còn hạn chế.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 98, Mục 6.2.3)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Chen-beta"
        ]
    },
    {
        "id": "PED55-B59",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị - Nội soi",
        "front": "<span style=\"color:#51cf66\"><b>Nội soi can thiệp</b></span> trong XHTH theo barem: mục đích, thời điểm, các kỹ thuật và hiệu quả?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Mục đích: <span style=\"color:#74c0fc\"><b>cầm máu và ngăn ngừa tái phát</b></span>.<br>• Thời điểm: khi bệnh nhân đã ổn định, tốt nhất <span style=\"color:#ffd43b\"><b>trong vòng 24 giờ</b></span> sau khi xuất hiện chảy máu.<br>• Kỹ thuật: liệu pháp tiêm (epinephrine, chất xơ cứng pha loãng), trị liệu cắt bỏ, liệu pháp cơ học; chọn theo đặc điểm chảy máu (phun thành tia, rỉ rả, không thấy mạch máu).<br>• Tiêm epinephrine hiệu quả khoảng <span style=\"color:#ffd43b\"><b>80%</b></span> chảy máu không do giãn; phối hợp epinephrine với phương pháp thứ hai tốt hơn đơn thuần, giảm tái phát xuống khoảng <span style=\"color:#ffd43b\"><b>10%</b></span>.<br>• <span style=\"color:#74c0fc\"><b>Endoclips</b></span>: liệu pháp cơ học được ưa thích cho XHTH không do giãn tĩnh mạch; Dieulafoy: nội soi là lựa chọn đầu tiên.<br>• Giãn tĩnh mạch cấp: <span style=\"color:#51cf66\"><b>thắt tĩnh mạch qua nội soi</b></span> là lựa chọn.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 98 - 99, Mục 6.2.4)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Noi-soi-can-thiep"
        ]
    },
    {
        "id": "PED55-B60",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị nguyên nhân",
        "front": "Điều trị <span style=\"color:#ff6b6b\"><b>chảy máu do giãn vỡ tĩnh mạch thực quản</b></span> bằng <span style=\"color:#51cf66\"><b>vasopressin</b></span> và <span style=\"color:#51cf66\"><b>sonde Blakemore</b></span> theo barem?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vasopressin <span style=\"color:#ffd43b\"><b>0,3 đv/kg</b></span> truyền tĩnh mạch:<br>– Trẻ dưới 5 tuổi: <span style=\"color:#ffd43b\"><b>0,05 đv/phút/giờ</b></span>, tối đa 0,2 đv/phút/giờ.<br>– Trẻ &lt; 12 tuổi: <span style=\"color:#ffd43b\"><b>0,3 đv/phút/giờ</b></span>; trẻ &gt; 12 tuổi: <span style=\"color:#ffd43b\"><b>0,4 đv/phút/giờ</b></span>.<br>– Hoặc 0,2 – 0,4 đv/1,73 m² da/phút; pha dextrose 5%, an toàn nhất qua tĩnh mạch trung tâm; có thể duy trì 12 – 24 giờ sau khi máu ngừng chảy.<br>– Tác dụng phụ: <span style=\"color:#ff6b6b\"><b>thiếu máu cơ tim, loạn nhịp</b></span>, co thắt mạch, giữ nước, tím đầu chi.<br>• Sonde Blakemore: ép chỗ vỡ, cầm máu ban đầu <span style=\"color:#ffd43b\"><b>50 - 80%</b></span>; biến chứng <span style=\"color:#ffd43b\"><b>9 – 35%</b></span>.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Vasopressin hiện ít dùng vì tác dụng phụ tim mạch; octreotide (hoặc terlipressin) phối hợp thắt tĩnh mạch qua nội soi là điều trị chuẩn. Sonde chèn bóng chỉ là biện pháp tạm thời khi chảy máu không kiểm soát (Baveno VII). Barem ghi \"0,05 đv/phút/giờ\" là đơn vị chưa chuẩn (nhiều tài liệu dùng đv/kg/phút).<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 99, Mục 7.2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Vasopressin",
            "Blakemore"
        ]
    },
    {
        "id": "PED55-B61",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị nguyên nhân",
        "front": "Điều trị <span style=\"color:#ff6b6b\"><b>chảy máu do viêm loét dạ dày - tá tràng</b></span> theo barem: rửa dạ dày và các thuốc giảm acid?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#51cf66\"><b>Rửa dạ dày</b></span> bằng dung dịch muối đẳng trương lạnh (tác dụng như ở nhiệt độ thường) – dung dịch <span style=\"color:#74c0fc\"><b>noradrenalin</b></span> (4 ống trong 500 ml) để cầm máu.<br>• Rửa <span style=\"color:#ffd43b\"><b>15 - 20 phút</b></span> mà dịch không sạch máu → rửa không có tác dụng; để sonde hút kiểm tra <span style=\"color:#ffd43b\"><b>15 – 30 phút</b></span> một lần.<br>• Thuốc kháng acid: <span style=\"color:#ffd43b\"><b>15 ml</b></span> trẻ nhỏ, <span style=\"color:#ffd43b\"><b>30 ml</b></span> trẻ trước tuổi đi học, <span style=\"color:#ffd43b\"><b>60 ml</b></span> trẻ lớn, để pH từ 1 lên 3,5.<br>• Kháng H2: Tagamet IV <span style=\"color:#ffd43b\"><b>30 – 50 mg/kg/ngày</b></span>; ranitidin <span style=\"color:#ffd43b\"><b>5 – 10 mg/kg/ngày</b></span>.<br>• PPI tiêm tĩnh mạch <span style=\"color:#ffd43b\"><b>1 - 3 mg/kg/ngày</b></span>.",
        "extra": "<b>⚖️ Đối chiếu (Ngoài barem):</b> Rửa dạ dày bằng nước muối lạnh không còn được khuyến cáo để cầm máu (không hiệu quả, có thể gây hạ thân nhiệt). PPI tĩnh mạch kết hợp nội soi cầm máu là điều trị chính; ranitidin đã bị rút khỏi thị trường nhiều nước (2020). Khi thi ghi theo barem.<br>📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 99, Mục 7.2.2)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dieu-tri",
            "Loet-DDTT",
            "Rua-da-day"
        ]
    },
]
