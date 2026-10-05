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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Viêm loét dạ dày tá tràng: Tiền sử đau bụng thượng vị theo chu kỳ hoặc liên quan bữa ăn, ợ chua.<br>2) Xuất huyết do giãn tĩnh mạch thực quản: Hội chứng tăng áp lực tĩnh mạch cửa trong xơ gan hoặc teo hẹp tĩnh mạch cửa gồm Lách to, Cổ trướng, Tuần hoàn bàng hệ cửa - chủ ở bụng.<br>3) Chảy máu đường mật: Sốt, gan to đau, vàng da, nhiễm khuẩn đường mật tái diễn sau chấn thương gan (Tam chứng Sandblom).<br><br><b>💡 Giải thích của AI:</b><br>Khám thấy lách to kèm tuần hoàn bàng hệ lập tức định hướng nôn máu là do vỡ giãn tĩnh mạch thực quản.",
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
        "category": "Nguyên nhân XHTH trên ở Sơ sinh",
        "front": "3 nguyên nhân gây xuất huyết tiêu hóa TRÊN thường gặp nhất ở trẻ SƠ SINH theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Nuốt máu mẹ: Trong chuyển dạ hoặc khi bú mẹ nứt núm vú (phân biệt bằng test Apt-Downey).<br>2) Bệnh lý xuất huyết do thiếu vitamin K: Chảy máu tiêu hóa kèm chảy máu rốn, nội sọ.<br>3) Viêm loét dạ dày - tá tràng do stress: Gặp ở trẻ sơ sinh bị ngạt nặng, suy hô hấp, hạ thân nhiệt, nhiễm khuẩn huyết.<br><br><b>💡 Giải thích của AI:</b><br>Ở sơ sinh, nuốt máu mẹ là nguyên nhân lành tính hay gặp nhất, trong khi thiếu vitamin K là bệnh lý mắc phải nguy hiểm hàng đầu cần tiêm dự phòng ngay sau sinh.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1.1 - Sơ sinh)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "XHTH-Tren",
            "So-sinh",
            "Vitamin-K"
        ]
    },
    {
        "id": "PED55-B25",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Xuất huyết do thiếu Vitamin K",
        "front": "Đặc điểm xuất huyết tiêu hóa do Thiếu vitamin K ở trẻ sơ sinh qua 2 thể khởi phát và biện pháp xử trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• 2 thể lâm sàng:<br>1) Thể sớm: Xuất hiện trong tuần đầu sau sinh (ngày thứ 2 đến thứ 7).<br>2) Thể muộn: Xuất hiện ở tuần thứ 2 đến tuần thứ 8 sau sinh (đặc biệt trẻ bú mẹ hoàn toàn không được tiêm phòng vitamin K).<br>• Đặc điểm: Chảy máu đa vị trí kết hợp: nôn máu, ỉa máu đen, chảy máu rốn kéo dài, bầm máu dưới da và đặc biệt biến chứng Xuất huyết não - màng não.<br>• Xử trí: Tiêm bắp hoặc tĩnh mạch chậm Vitamin K1 liều 1 - 5 mg ngay lập tức.<br><br><b>💡 Giải thích của AI:</b><br>Trẻ sơ sinh có dự trữ vitamin K thấp và ruột chưa có hệ vi khuẩn tổng hợp vitamin K, tiêm bắp 1 mg Vitamin K1 sau sinh là quy chuẩn bắt buộc.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, 97, Mục Thiếu vitamin K)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Vitamin-K",
            "So-sinh",
            "2-the"
        ]
    },
    {
        "id": "PED55-B26",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên ở Nhũ nhi",
        "front": "4 nguyên nhân xuất huyết tiêu hóa TRÊN thường gặp ở trẻ NHŨ NHI (1 tháng - 1 tuổi) theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Viêm thực quản trào ngược (GERD): Kèm nôn trớ tái diễn, chậm tăng cân, khóc thét khi bú.<br>2) Viêm dạ dày cấp: Do dùng thuốc kháng viêm NSAID, Corticoid hoặc sau nhiễm khuẩn nặng.<br>3) Loét dạ dày - tá tràng: Thường thứ phát sau stress hoặc bệnh lý toàn thân nặng.<br>4) Hội chứng Mallory-Weiss: Rách niêm mạc vùng nối tâm vị thực quản sau những đợt nôn ói dữ dội, nôn khan kéo dài.<br><br><b>💡 Giải thích của AI:</b><br>Hội chứng Mallory-Weiss đặc trưng bởi lần nôn đầu chỉ ra thức ăn bình thường, sau những cơn nôn gắng sức tiếp theo mới xuất hiện nôn ra máu tươi.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục 5.1.2 - Nhũ nhi)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "XHTH-Tren",
            "Nhu-nhi",
            "Mallory-Weiss",
            "GERD"
        ]
    },
    {
        "id": "PED55-B27",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Nguyên nhân XHTH trên ở Trẻ lớn",
        "front": "3 nguyên nhân xuất huyết tiêu hóa TRÊN hàng đầu ở TRẺ LỚN (> 5 tuổi) theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Giãn vỡ tĩnh mạch thực quản: Nguyên nhân hàng đầu gây xuất huyết ồ ạt đe dọa tính mạng ở trẻ có tăng áp lực tĩnh mạch cửa (xơ gan, teo hẹp/huyết khối tĩnh mạch cửa). Lâm sàng: nôn máu đỏ tươi ồ ạt kèm máu cục, lách to, tuần hoàn bàng hệ.<br>2) Loét dạ dày - tá tràng: Thường liên quan đến nhiễm vi khuẩn Helicobacter pylori (H. pylori) hoặc sau dùng thuốc NSAID.<br>3) Chảy máu đường mật (Hemobilia): Xuất huyết tiêu hóa kèm tam chứng Sandblom sau chấn thương gan.<br><br><b>💡 Giải thích của AI:</b><br>Ở trẻ lớn, vỡ giãn tĩnh mạch thực quản và loét dạ dày tá tràng chiếm đa số các ca nôn ra máu nhập viện cấp cứu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92 - 93, Mục 5.1.3 - Trẻ lớn)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "XHTH-Tren",
            "Tre-lon",
            "Gian-TMTQ",
            "H-pylori"
        ]
    },
    {
        "id": "PED55-B28",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Chảy máu đường mật - Sandblom",
        "front": "Bệnh cảnh lâm sàng và Tam chứng Sandblom kinh điển của Chảy máu đường mật (Hemobilia) theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bản chất: Chảy máu từ các nhánh mạch máu gan vào trong đường dẫn mật rồi đổ xuống ruột non.<br>• Tam chứng Sandblom kinh điển gồm 3 triệu chứng:<br>1) Đau quặn gan (đau hạ sườn phải từng cơn dữ dội do cục máu đông di chuyển làm tắc ống mật).<br>2) Vàng da tắc mật thoáng qua.<br>3) Xuất huyết tiêu hóa (nôn máu hoặc đại tiện phân đen).<br>• Hoàn cảnh xuất hiện: Thường xảy ra sau chấn thương đụng dập gan hoặc sau can thiệp phẫu thuật/thủ thuật đường mật.<br><br><b>💡 Giải thích của AI:</b><br>Tam chứng Đau hạ sườn phải + Vàng da + Xuất huyết tiêu hóa sau tiền sử chấn thương gan là câu hỏi điểm 10 phân biệt xuất huyết tiêu hóa trên.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 92, Mục Chảy máu đường mật)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Chay-mau-duong-mat",
            "Sandblom",
            "Hemobilia"
        ]
    },
    {
        "id": "PED55-B29",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Viêm ruột hoại tử - NEC",
        "front": "Bệnh cảnh lâm sàng và dấu hiệu X-quang kinh điển của Viêm ruột hoại tử (NEC) ở trẻ sơ sinh theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đối tượng nguy cơ: Hay gặp nhất ở trẻ sơ sinh non tháng, nhẹ cân nuôi ăn nhân tạo.<br>• Biểu hiện lâm sàng:<br>1) Bụng chướng căng, nổi ban đỏ thành bụng.<br>2) Nôn dịch mật hoặc dịch ứ trệ dạ dày.<br>3) Đi ngoài phân nhầy lẫn máu (máu tươi hoặc đen).<br>4) Toàn thân nhiễm trùng nhiễm độc nặng, hạ thân nhiệt, cơn ngừng thở.<br>• Dấu hiệu X-quang bụng kinh điển: Hình ảnh HƠI TRONG THÀNH RUỘT (Pneumatosis intestinalis) hoặc hơi trong hệ tĩnh mạch cửa.<br><br><b>💡 Giải thích của AI:</b><br>Dấu hiệu hơi trong thành ruột trên X-quang là tiêu chuẩn vàng chẩn đoán NEC giai đoạn II (Bell stage) trở lên, cần ngừng ăn đường miệng và dùng kháng sinh phổ rộng ngay.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.1 - Sơ sinh)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "NEC",
            "Viem-ruot-hoai-tu",
            "Pneumatosis"
        ]
    },
    {
        "id": "PED55-B30",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Lồng ruột cấp - Tam chứng",
        "front": "Đối tượng hay gặp và Tam chứng lâm sàng kinh điển của Lồng ruột cấp ở trẻ nhũ nhi theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đối tượng: Là nguyên nhân ngoại khoa thường gặp nhất ở trẻ từ 4 đến 9 tháng tuổi, hay gặp ở các bé trai bụ bẫm.<br>• Tam chứng lâm sàng kinh điển:<br>1) Đau bụng khóc thét từng cơn: Trẻ đang chơi đột ngột khóc thét dữ dội, ưỡn người, co hai chân lên bụng, sau đó tạm yên rồi lại khóc cơn tiếp theo.<br>2) Nôn: Ban đầu nôn ra thức ăn/sữa, về sau nôn ra dịch mật màu xanh vàng.<br>3) Ỉa phân nhầy máu: Thường xuất hiện muộn sau 6 - 12 giờ, phân nhầy lẫn máu màu mận chín (màu siro dâu).<br><br><b>💡 Giải thích của AI:</b><br>Đau bụng khóc thét từng cơn ở trẻ nhũ nhi bụ bẫm 4 - 9 tháng phải nghĩ ngay đến Lồng ruột trước khi phân có máu xuất hiện.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.2 - Lồng ruột)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Long-ruot-cap",
            "Tam-chung",
            "Nhu-nhi"
        ]
    },
    {
        "id": "PED55-B31",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Lồng ruột cấp - Khám & Siêu âm",
        "front": "Dấu hiệu khám thực thể và hình ảnh Siêu âm kinh điển của Lồng ruột cấp theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Khám thực thể:<br>1) Sờ thấy Khối lồng hình quả chuối (hoặc hình xúc xích), mật độ chắc, di động nhẹ, thường nằm dọc khung đại tràng hoặc ở hạ sườn phải.<br>2) Dấu hiệu Dance dương tính: Hố chậu phải rỗng (do manh tràng và hồi tràng đã lồng chui lên trên).<br>3) Thăm trực tràng: Găng có nhầy máu màu mận chín.<br>• Siêu âm ổ bụng: Tiêu chuẩn vàng có giá trị chẩn đoán xác định cao nhất:<br>1) Mặt cắt ngang: Hình ảnh 'bia bắn' (Target sign) hoặc hình 'bánh donut'.<br>2) Mặt cắt dọc: Hình ảnh 'bánh kẹp' (Sandwich sign) hoặc 'hình quả thận giả'.<br><br><b>💡 Giải thích của AI:</b><br>Siêu âm có độ nhạy và đặc hiệu gần 100% trong chẩn đoán lồng ruột, giúp phát hiện sớm khi chưa có ỉa máu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.2 - Lồng ruột)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Long-ruot",
            "Khoi-long",
            "Sieu-am-bia-ban"
        ]
    },
    {
        "id": "PED55-B32",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Túi thừa Meckel",
        "front": "Bản chất phôi thai học, cơ chế gây loét và tính chất chảy máu kinh điển của Túi thừa Meckel?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bản chất phôi thai: Do sự thoái hóa không hoàn toàn của ống noãn hoàng (ống rốn tràng), tạo thành một túi thừa ở bờ tự do của hồi tràng (cách van hồi manh tràng khoảng 50 - 100 cm).<br>• Cơ chế gây loét: Khoảng 50% túi thừa Meckel có chứa NIÊM MẠC DẠ DÀY LẠC CHỖ tiết acid clohydric gây loét và thủng thành hồi tràng kế cận.<br>• Tính chất chảy máu kinh điển:<br>1) Đại tiện ra máu đỏ tươi hoặc màu mận chín ồ ạt, tái diễn từng đợt.<br>2) ĐẶC ĐIỂM SỐNG CÒN: HOÀN TOÀN KHÔNG ĐAU BỤNG và không sốt (chảy máu ồ ạt trên một đứa trẻ êm ả không đau).<br>• Chẩn đoán xác định: Chụp xạ hình nhấp nháy Tc99m pertechnetate.<br><br><b>💡 Giải thích của AI:</b><br>Bẫy thi lâm sàng: Trẻ nhỏ đi ngoài ra máu đỏ ồ ạt mà bụng mềm hoàn toàn không đau, không sốt → chẩn đoán số 1 là Túi thừa Meckel.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94 - 95, Mục Meckel)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Meckel",
            "Ong-noan-hoang",
            "Khong-dau-bung"
        ]
    },
    {
        "id": "PED55-B33",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Polyp đại trực tràng thiếu niên",
        "front": "Bản chất, vị trí giải phẫu và đặc điểm chảy máu của Polyp đại trực tràng thiếu niên (Juvenile polyp)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bản chất: Là polyp dạng u mô thừa (Hamartoma) lành tính, thường đơn độc.<br>• Vị trí giải phẫu: Thường nằm ở vùng trực tràng hoặc đại tràng sigma (chiếm > 80%).<br>• Đặc điểm chảy máu:<br>1) Chảy máu tươi xuất hiện ở CUỐI BÃI PHÂN hoặc máu bao quanh khuôn phân.<br>2) HOÀN TOÀN KHÔNG ĐAU BỤNG.<br>3) Chảy máu dai dẳng kéo dài nhiều tuần đến nhiều tháng làm trẻ bị thiếu máu thiếu sắt nhẹ.<br>4) Thăm trực tràng hoặc nội soi đại tràng phát hiện polyp có cuống.<br><br><b>💡 Giải thích của AI:</b><br>Polyp thiếu niên lành tính và có thể tự rụng cuống, cắt polyp qua nội soi đại tràng ống mềm là phương pháp điều trị triệt căn.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục 5.2.3 - Polyp)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Polyp",
            "Juvenile-polyp",
            "Cuoi-bai-phan"
        ]
    },
    {
        "id": "PED55-B34",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Dị ứng đạm sữa bò",
        "front": "Đặc điểm xuất huyết tiêu hóa do Dị ứng đạm sữa bò ở trẻ nhũ nhi theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Thời điểm khởi phát: Thường xuất hiện trong vài tuần đầu sau khi trẻ bắt đầu ăn dặm hoặc đổi sang sữa công thức nguồn gốc sữa bò.<br>2) Tính chất phân: Phân lỏng nhiều lần, có sợi máu đỏ tươi dạng dây nhầy lẫn trong phân.<br>3) Triệu chứng đi kèm: Trẻ quấy khóc khi bú, nôn trớ, chậm tăng cân, có thể kèm dị ứng ngoài da (chàm da, mày đay).<br>4) Xét nghiệm & Thử thách: Xét nghiệm phân có bạch cầu ái toan; triệu chứng biến mất khi ngưng sữa bò và xuất hiện lại khi thử thách lại sữa bò.<br><br><b>💡 Giải thích của AI:</b><br>Xử trí đơn giản và hiệu quả nhất là chuyển sang sữa mẹ hoàn toàn (mẹ kiêng sữa bò) hoặc dùng sữa thủy phân hoàn toàn đạm whey/casein.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục Dị ứng đạm sữa)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Di-ung-sua-bo",
            "Nhu-nhi",
            "Soi-mau"
        ]
    },
    {
        "id": "PED55-B35",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Viêm mạch Henoch-Schonlein",
        "front": "Bệnh cảnh lâm sàng toàn thân và tổn thương ruột trong Viêm mạch Henoch-Schonlein (HSP) gây xuất huyết tiêu hóa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tổn thương mạch máu ruột: Viêm các vi mạch mạc treo và thành ruột gây thiếu máu cục bộ, phù nề và xuất huyết niêm mạc ruột.<br>• Tứ chứng lâm sàng toàn thân:<br>1) Ban xuất huyết ngoài da dạng sẩn gồ hoại tử đối xứng ở hai cẳng chân, mông.<br>2) Đau bụng từng cơn dữ dội quanh rốn (có thể đi ngoài phân đen hoặc phân máu, biến chứng lồng ruột).<br>3) Sưng đau các khớp lớn (khớp gối, cổ chân).<br>4) Tổn thương thận (đái máu vi thể/đại thể, protein niệu).<br><br><b>💡 Giải thích của AI:</b><br>Xuất huyết tiêu hóa trong Henoch-Schönlein có thể xuất hiện trước khi ban da bùng phát, rất dễ chẩn đoán nhầm với bụng ngoại khoa cấp cứu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục Henoch-Schonlein)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Henoch-Schonlein",
            "HSP",
            "Viem-mach"
        ]
    },
    {
        "id": "PED55-B36",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Hội chứng lỵ vi khuẩn",
        "front": "Các căn nguyên vi khuẩn gây Hội chứng lỵ xuất huyết tiêu hóa dưới và đặc điểm phân theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Các căn nguyên vi khuẩn thường gặp: Shigella (lỵ trực trùng), Salmonella, Campylobacter jejuni, E. coli gây chảy máu ruột (EHEC / EIEC), Entamoeba histolytica (lỵ amip).<br>• Đặc điểm lâm sàng & phân:<br>1) Sốt cao, nhiễm trùng độc hại.<br>2) Đau quặn bụng dọc khung đại tràng, mót rặn liên tục.<br>3) Phân nhiều lần, số lượng phân ít, phân chứa NHIỀU NƯỚC LẪN CHẤT NHẦY, MỦ VÀ MÁU ĐỎ TƯƠI.<br><br><b>💡 Giải thích của AI:</b><br>E. coli O157:H7 (EHEC) tiết độc tố Shiga có thể gây Hội chứng tan máu ure huyết cao (HUS), chống chỉ định dùng kháng sinh bừa bãi khi nghi ngờ EHEC.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục Hội chứng lỵ)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Hoi-chung-ly",
            "Shigella",
            "EHEC"
        ]
    },
    {
        "id": "PED55-B37",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bảng tổng hợp XHTH Dưới",
        "front": "Bảng tổng hợp các nguyên nhân xuất huyết tiêu hóa DƯỚI phổ biến vs nguy hiểm cần loại trừ theo 4 nhóm tuổi trong giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Sơ sinh:<br>• Phổ biến: Nuốt máu mẹ, nứt kẽ hậu môn.<br>• Nguy hiểm cần loại trừ: Viêm ruột hoại tử (NEC), Xoắn ruột do quay bất toàn, Phình đại tràng Hirschsprung.<br>2) Nhũ nhi (&lt; 1 tuổi):<br>• Phổ biến: Nứt kẽ hậu môn, Dị ứng đạm sữa bò.<br>• Nguy hiểm cần loại trừ: LỒNG RUỘT CẤP, Túi thừa Meckel, Viêm ruột hoại tử.<br>3) Trẻ nhỏ (1 - 5 tuổi):<br>• Phổ biến: Nứt kẽ hậu môn, Polyp đại trực tràng.<br>• Nguy hiểm cần loại trừ: Túi thừa Meckel, Lồng ruột, Hội chứng lỵ.<br>4) Trẻ lớn (> 5 tuổi):<br>• Phổ biến: Táo bón nứt hậu môn, Polyp.<br>• Nguy hiểm cần loại trừ: Viêm ruột mạn tính (IBD), Viêm mạch Henoch-Schonlein, Trĩ.<br><br><b>💡 Giải thích của AI:</b><br>Bảng phân tầng theo tuổi này là kim chỉ nam giúp bác sĩ không bao giờ bỏ sót các cấp cứu ngoại khoa nguy hiểm như Lồng ruột hay NEC.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Bảng XHTH dưới theo tuổi)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Bang-tong-hop-XHTH-duoi",
            "4-nhom-tuoi"
        ]
    },
    {
        "id": "PED55-B38",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Hồi sức đường thở & Đường truyền",
        "front": "Quy trình bảo đảm đường thở và thiết lập đường truyền tĩnh mạch trong cấp cứu xuất huyết tiêu hóa theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bảo đảm đường thở và oxy:<br>1) Đặt trẻ nằm ĐẦU THẤP NGHIÊNG SANG MỘT BÊN để tránh sặc máu và chất nôn vào đường hô hấp.<br>2) Thở oxy qua canula hoặc mặt nạ.<br>3) Nếu có rối loạn tri giác (hôn mê) hoặc nôn máu ồ ạt: BẮT BUỘC ĐẶT NỘI KHÍ QUẢN bảo vệ đường thở trước khi làm thủ thuật.<br>• Thiết lập đường truyền tĩnh mạch:<br>1) Đặt ngay 2 ĐƯỜNG TRUYỀN TĨNH MẠCH NGOẠI VI KIM LỚN (cỡ kim 18G - 22G).<br>2) Đặt catheter tĩnh mạch trung tâm nếu không lấy được ven ngoại vi.<br>3) Lấy máu xét nghiệm khẩn: Công thức máu, nhóm máu, phản ứng chéo, đông máu, chức năng gan thận, điện giải đồ.<br><br><b>💡 Giải thích của AI:</b><br>Hai đường truyền kim lớn là yêu cầu bắt buộc để có thể xả dịch tốc độ cao khi trẻ rơi vào sốc mất máu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6.1 - Hồi sức)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Hoi-suc",
            "Duong-tho",
            "Duong-truyen-TM"
        ]
    },
    {
        "id": "PED55-B39",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Bồi phụ thể tích chống sốc",
        "front": "Phác đồ dịch truyền bồi phụ thể tích chống sốc mất máu và những loại dịch CẤM DÙNG theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Loại dịch chỉ định: Dịch tinh thể đẳng trương gồm Natri Clorid 0,9% hoặc Ringer Lactat.<br>• Liều lượng và tốc độ: Liều 20 ml/kg truyền tĩnh mạch nhanh trong 20 - 30 phút. Có thể lặp lại lần 2 nếu huyết áp và tưới máu chưa cải thiện.<br>• CÁC LOẠI DỊCH CẤM DÙNG ĐỂ CHỐNG SỐC MẤT MÁU: Tránh dùng dịch nhược trương hoặc Glucose (dung dịch đường) để truyền bù thể tích.<br><br><b>💡 Giải thích của AI:</b><br>Dịch nhược trương và Glucose sẽ nhanh chóng thoát mạch vào gian bào gây phù não và hạ natri máu, hoàn toàn không giữ được thể tích trong lòng mạch.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6.1 - Bồi phụ thể tích)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Dich-truyen",
            "Chong-soc",
            "20-ml-kg",
            "Cam-Glucose"
        ]
    },
    {
        "id": "PED55-B40",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Chỉ định truyền máu",
        "front": "Chỉ định, liều lượng và nồng độ Hemoglobin đích khi truyền Khối hồng cầu trong xuất huyết tiêu hóa nhi theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ định truyền khối hồng cầu:<br>1) Trẻ mất máu nặng có biểu hiện sốc giảm thể tích không đáp ứng sau khi truyền dịch tinh thể.<br>2) Nồng độ Hemoglobin (Hb) giảm dưới 70 - 80 g/L (Hematocrit &lt; 25%).<br>3) Ở trẻ có bệnh tim bẩm sinh hoặc đang chảy máu dữ dội: Cần duy trì Hb > 100 g/L.<br>• Liều lượng truyền: Khối hồng cầu 10 - 15 ml/kg truyền tĩnh mạch chậm.<br><br><b>💡 Giải thích của AI:</b><br>Mốc Hb &lt; 70 - 80 g/L ở trẻ bình thường và Hb > 100 g/L ở trẻ tim bẩm sinh là 2 ngưỡng truyền máu kinh điển cần ghi nhớ chính xác.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 96, Mục 6.1 - Truyền máu)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Truyen-mau",
            "Khoi-hong-cau",
            "Chi-dinh-Hb"
        ]
    },
    {
        "id": "PED55-B41",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Bồi phụ yếu tố đông máu",
        "front": "Chỉ định và liều dùng Huyết tương tươi đông lạnh (FFP), Khối tiểu cầu và Vitamin K1 theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Huyết tương tươi đông lạnh (FFP): Liều 10 - 15 ml/kg khi có rối loạn đông máu phối hợp (INR > 1,5 hoặc tỷ lệ Prothrombin kéo dài) hoặc chảy máu ồ ạt sau truyền dịch lượng lớn.<br>2) Khối tiểu cầu: Chỉ định khi số lượng tiểu cầu giảm dưới 50 × 10⁹/L (&lt; 50.000/μL) và đang có chảy máu tiến triển.<br>3) Vitamin K1: Tiêm tĩnh mạch chậm hoặc tiêm bắp liều 1 - 5 mg cho mọi trẻ sơ sinh và nhũ nhi nghi ngờ thiếu vitamin K.<br><br><b>💡 Giải thích của AI:</b><br>Trong chảy máu ồ ạt, bồi phụ đông máu song song với hồng cầu giúp ngăn chặn vòng xoắn bệnh lý rối loạn đông máu tiêu thụ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97, Mục 6.1 - Bồi phụ đông máu)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "FFP",
            "Tieu-cau",
            "Vitamin-K1"
        ]
    },
    {
        "id": "PED55-B42",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Thuốc ức chế acid PPI",
        "front": "Phác đồ sử dụng thuốc ức chế bơm proton PPI (Omeprazole / Esomeprazole) và mục tiêu pH dạ dày trong điều trị loét dạ dày tá tràng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Liều lượng PPI (Omeprazole hoặc Esomeprazole):<br>1) Liều tấn công (Bolus): 1 mg/kg tiêm tĩnh mạch chậm (tối đa 40 mg).<br>2) Liều duy trì: 1 - 2 mg/kg/ngày chia 2 lần tiêm TM hoặc truyền tĩnh mạch liên tục 0,1 - 0,2 mg/kg/giờ.<br>• Mục tiêu pH dạ dày: Phải duy trì pH dạ dày > 6,0 liên tục.<br>• Cơ chế: Khi pH dạ dày > 6,0, men Pepsin bị bất hoạt và tiểu cầu kết tập tạo cục máu đông bền vững che phủ ổ loét (ở pH acid &lt; 5,0 cục máu đông sẽ bị tiêu hủy ngay).<br><br><b>💡 Giải thích của AI:</b><br>Duy trì pH > 6.0 là nguyên lý vàng giải thích vì sao phải dùng PPI liều cao truyền liên tục trong xuất huyết dạ dày tá tràng tiến triển.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 97, Mục 6.2.1 - Thuốc PPI)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "PPI",
            "Omeprazole",
            "pH-da-day-tren-6"
        ]
    },
    {
        "id": "PED55-B43",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Thuốc co mạch tạng Octreotide",
        "front": "Chỉ định, liều bolus và liều duy trì của Octreotide trong điều trị vỡ giãn tĩnh mạch thực quản theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ định: Ngay khi nghi ngờ xuất huyết do tăng áp lực tĩnh mạch cửa (trẻ có xơ gan, lách to, tuần hoàn bàng hệ hoặc nôn máu đỏ tươi ồ ạt).<br>• Liều lượng Octreotide:<br>1) Liều Bolus ban đầu: 1 - 2 µg/kg tiêm tĩnh mạch chậm trong 5 phút.<br>2) Liều duy trì: Truyền tĩnh mạch liên tục 1 - 2 µg/kg/giờ (tối đa 50 µg/giờ).<br>• Thời gian duy trì: Duy trì liên tục trong 48 - 72 GIỜ sau khi máu đã cầm hoàn toàn, sau đó giảm liều dần rồi ngừng.<br><br><b>💡 Giải thích của AI:</b><br>Octreotide gây co mạch tạng chọn lọc làm giảm lưu lượng máu đổ về tĩnh mạch cửa, hạ áp lực búi giãn tĩnh mạch thực quản giúp cầm máu nhanh chóng.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 98, Mục 6.2.2 - Octreotide)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Octreotide",
            "Co-mach-tang",
            "Gian-TMTQ",
            "48-72-gio"
        ]
    },
    {
        "id": "PED55-B44",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Propranolol phòng ngừa vỡ giãn",
        "front": "Chỉ định và liều dùng của Propranolol trong dự phòng vỡ giãn tĩnh mạch thực quản theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ định: Dự phòng tiên phát và thứ phát vỡ giãn tĩnh mạch thực quản SAU KHI XUẤT HUYẾT CẤP ĐÃ ĐƯỢC KIỂM SOÁT HOÀN TOÀN ỔN ĐỊNH.<br>• Liều lượng: Liều khởi đầu 1 mg/kg/ngày chia làm 2 - 3 lần uống.<br>• Đích điều chỉnh liều: Chỉnh liều tăng dần để đạt mục tiêu GIẢM NHỊP TIM LÚC NGHỈ 25% so với nhịp tim ban đầu.<br><br><b>💡 Giải thích của AI:</b><br>Propranolol chẹn thụ thể beta-1 làm giảm cung lượng tim và chẹn beta-2 gây co mạch tạng, giúp hạ áp lực tĩnh mạch cửa lâu dài.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 98, Mục 6.2.3 - Propranolol)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Propranolol",
            "Du-phong-tai-phat",
            "Dich-nhip-tim"
        ]
    },
    {
        "id": "PED55-B45",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Nội soi can thiệp cầm máu",
        "front": "Các kỹ thuật nội soi can thiệp cầm máu trong vỡ giãn tĩnh mạch thực quản và trong loét dạ dày tá tràng theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thời điểm: Tiến hành sớm trong vòng 12 - 24 giờ sau hồi sức ổn định huyết động.<br>• Trong vỡ giãn tĩnh mạch thực quản:<br>1) Thắt vòng cao su nội soi (Endoscopic Variceal Ligation - EVL): Là tiêu chuẩn vàng lựa chọn hàng đầu.<br>2) Tiêm xơ (Sclerotherapy): Áp dụng khi thắt vòng khó thực hiện ở trẻ nhỏ.<br>• Trong ổ loét dạ dày tá tràng: Tiêm cầm máu bằng dung dịch Adrenaline 1/10.000 quanh ổ loét kết hợp kẹp Clip cầm máu (Hemoclip) hoặc đầu dò nhiệt đốt điện.<br><br><b>💡 Giải thích của AI:</b><br>Thắt vòng cao su EVL có tỷ lệ cầm máu cao hơn và ít biến chứng loét hẹp thực quản hơn so với tiêm xơ xơ hóa tĩnh mạch.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 98, Mục 6.2.4 - Noi soi can thiep)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Noi-soi-can-thiep",
            "EVL",
            "Hemoclip"
        ]
    },
    {
        "id": "PED55-B46",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Sonde Sengstaken-Blakemore",
        "front": "Chỉ định, thể tích bơm bóng và lưu ý an toàn sinh tử khi đặt Sonde Sengstaken-Blakemore chèn ép bóng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ định: Biện pháp cứu cánh tạm thời khi vỡ giãn tĩnh mạch thực quản chảy máu ồ ạt đe dọa tính mạng không kiểm soát được bằng thuốc co mạch và nội soi can thiệp chưa thể thực hiện ngay.<br>• Kỹ thuật bơm bóng:<br>1) Bơm bóng dạ dày trước với thể tích 100 - 150 ml không khí, kéo nhẹ cố định vào tâm vị.<br>2) Nếu máu vẫn tiếp tục chảy: Bơm tiếp bóng thực quản duy trì áp lực 25 - 30 mmHg.<br>• LƯU Ý AN TOÀN SINH TỬ: TUYỆT ĐỐI KHÔNG ĐƯỢC LƯU BÓNG CHÈN ÉP QUÁ 24 - 48 GIỜ.<br>• Nguy cơ: Lưu bóng quá 48 giờ sẽ gây thiếu máu cục bộ, hoại tử và loét thủng thực quản gây tử vong.<br><br><b>💡 Giải thích của AI:</b><br>Sonde Blakemore chỉ là cầu nối hồi sức tạm thời trong khi chờ chuyển phòng mổ hoặc phòng nội soi can thiệp, phải xả bóng sau mỗi vài giờ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 99, Mục 6.3 - Sonde Sengstaken)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Sengstaken-Blakemore",
            "Chen-ep-bong",
            "Cam-qua-48-gio"
        ]
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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kỹ thuật: Đặt ống thông hậu môn có bóng chèn, bơm hơi từ từ vào đại tràng dưới hướng dẫn của màn huỳnh quang tăng sáng (hoặc siêu âm).<br>• Áp lực bơm hơi an toàn: Bắt đầu từ 60 - 80 mmHg, tối đa không vượt quá 100 - 120 mmHg (ở trẻ nhũ nhi).<br>• Dấu hiệu tháo lồng thành công:<br>1) Thấy khối lồng thụt lùi dần qua góc gan, manh tràng rồi biến mất hoàn toàn.<br>2) Hơi ào ạt tràn vào các quai hồi tràng ở giữa bụng.<br>3) Bụng trẻ xẹp mềm, trẻ hết khóc thét và ngủ yên.<br><br><b>💡 Giải thích của AI:</b><br>Tháo lồng bằng hơi là tiêu chuẩn vàng điều trị lồng ruột cấp với tỷ lệ thành công > 90 - 95%, giúp trẻ tránh được một cuộc phẫu thuật mở bụng.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Tháo lồng ruột bằng hơi ở trẻ nhũ nhi (ESPGHAN)",
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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Gồm 3 mũi nhọn phối hợp đồng thời trong 12 giờ đầu:<br>1) Dược lý co mạch tạng: Khởi động Octreotide truyền tĩnh mạch liên tục ngay khi nghi ngờ vỡ giãn (trước cả khi nội soi).<br>2) Kháng sinh dự phòng sớm: Bắt buộc dùng Ceftriaxone đường tĩnh mạch trong 5 - 7 ngày cho mọi bệnh nhân tăng áp cửa xuất huyết tiêu hóa.<br>3) Nội soi can thiệp cầm máu: Thực hiện thắt vòng cao su EVL trong vòng 12 giờ sau khi ổn định huyết động.<br><br><b>💡 Giải thích của AI:</b><br>Theo Baveno VII, dùng thuốc co mạch tạng và kháng sinh NGAY TẠI THỜI ĐIỂM TIẾP NHẬN làm giảm đáng kể áp lực tĩnh mạch cửa trước khi đưa máy nội soi vào can thiệp.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Khuyến cáo Baveno VII về Tăng áp lực tĩnh mạch cửa",
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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: Xuất huyết tiêu hóa làm suy giảm miễn dịch nghiêm trọng, tạo điều kiện cho vi khuẩn đường ruột chuyển vị vào máu và dịch báng.<br>• Lợi ích chứng minh bằng chứng (EBM): Dùng Ceftriaxone dự phòng sớm giúp:<br>1) Giảm 50% nguy cơ nhiễm trùng huyết và viêm phúc mạc tiên phát do vi khuẩn (SBP).<br>2) Giảm đáng kể tỷ lệ tái xuất huyết sớm trong tuần đầu.<br>3) Giảm tỷ lệ tử vong toàn bộ ở bệnh nhân xơ gan xuất huyết tiêu hóa.<br><br><b>💡 Giải thích của AI:</b><br>Nhiễm trùng giải phóng nội độc tố kích hoạt co mạch gan và tăng áp lực cửa thứ phát làm bục búi giãn; dùng kháng sinh là biện pháp gián tiếp hạ áp lực cửa.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Khuyến cáo Baveno VII & Ceftriaxone dự phòng",
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
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy bỏ sót Túi thừa Meckel",
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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Forrest I (Đang chảy máu hoạt động):<br>1) Ia: Máu phun thành tia (Nguy cơ tái chảy máu 90%).<br>2) Ib: Máu chảy rỉ rả liên tục (Nguy cơ 60 - 80%).<br>• Forrest II (Dấu hiệu chảy máu gần đây):<br>1) IIa: Nhìn thấy mạch máu nổi không chảy máu (Nguy cơ 50%).<br>2) IIb: Cục máu đông bám chặt đáy ổ loét (Nguy cơ 25 - 30%).<br>3) IIc: Cặn sắc tố đen đáy ổ loét (Nguy cơ 5 - 10%).<br>• Forrest III: Đáy ổ loét sạch, phủ giả mạc trắng (Nguy cơ tái chảy máu &lt; 5%).<br>• Chỉ định can thiệp nội soi: BẮT BUỘC can thiệp cầm máu đối với Forrest Ia, Ib, IIa và cân nhắc bóc cục máu đông ở IIb.<br><br><b>💡 Giải thích của AI:</b><br>Phân loại Forrest là ngôn ngữ quốc tế định hướng có cần kẹp Clip hay tiêm Adrenaline cầm máu qua nội soi hay không.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Phân loại Forrest trong nội soi loét dạ dày tá tràng",
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
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trẻ bú mẹ hoàn toàn: Tiếp tục cho bú mẹ, MẸ BẮT BUỘC KIÊNG HOÀN TOÀN SỮA BÒ và tất cả các chế phẩm từ sữa bò (phô mai, sữa chua, bơ) trong ít nhất 2 - 4 tuần.<br>2) Trẻ ăn sữa công thức:<br>• Lựa chọn hàng đầu: Chuyển sang SỮA THỦY PHÂN HOÀN TOÀN (Extensively Hydrolyzed Formula - eHF).<br>• Lựa chọn cho thể nặng/thất bại eHF: Chuyển sang SỮA CÔNG THỨC ACID AMIN (Amino Acid-based Formula - AAF).<br>3) Không dùng sữa đậu nành cho trẻ &lt; 6 tháng tuổi vì nguy cơ dị ứng chéo cao.<br>• Tiên lượng: Rất tốt, hầu hết 85 - 90% trẻ sẽ dung nạp lại được sữa bò khi được 1 - 3 tuổi.<br><br><b>💡 Giải thích của AI:</b><br>Dị ứng đạm sữa bò gây viêm trực tràng đại tràng dị ứng (FPIAP) là bệnh lý lành tính, đáp ứng ngoạn mục sau 48 - 72 giờ đổi sữa.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Khuyến cáo ESPGHAN về Dị ứng đạm sữa bò",
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
        "track": "barem_goc",
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
        "category": "Bảng tổng hợp XHTH Trên",
        "front": "Bảng tổng hợp các nguyên nhân xuất huyết tiêu hóa TRÊN ít gặp ở 4 nhóm tuổi theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Sơ sinh: Dị tật mạch máu bẩm sinh, Dị tật nhân đôi đường tiêu hóa, Rối loạn đông máu bẩm sinh (Hemophilia).<br>2) Nhũ nhi (1 tháng - 1 tuổi): Dị vật đường tiêu hóa, Giãn tĩnh mạch thực quản bẩm sinh, U máu đường tiêu hóa.<br>3) Trẻ nhỏ (1 - 5 tuổi): Giãn vỡ tĩnh mạch thực quản do tăng áp cửa, Nuốt dị vật sắc nhọn, Dị dạng mạch máu ruột.<br>4) Trẻ lớn (> 5 tuổi): Chảy máu đường mật, Hội chứng Schönlein-Henoch, U tụy, U tá tràng.<br><br><b>💡 Giải thích của AI:</b><br>Dị vật đường tiêu hóa (như pin cúc áo, nam châm, xương cá) là nguyên nhân cơ học nguy hiểm cần khai thác kỹ ở trẻ tuổi tập bò và nhà trẻ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 93, Bảng tổng hợp XHTH trên)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "XHTH-tren-it-gap",
            "Bang-tong-hop"
        ]
    },
    {
        "id": "PED55-B49",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Xoắn ruột & Hirschsprung",
        "front": "Biểu hiện xuất huyết tiêu hóa dưới trong Xoắn ruột do quay bất toàn và Phình đại tràng bẩm sinh biến chứng viêm ruột?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Xoắn ruột do ruột quay bất toàn:<br>1) Hay gặp ở trẻ sơ sinh trong tháng đầu.<br>2) Nôn dịch mật xanh đen ồ ạt, bụng chướng, đi ngoài phân máu sẫm hoặc máu tươi.<br>3) Siêu âm bụng thấy dấu hiệu 'xoáy nước' (Whirlpool sign) mạc treo tràng; cấp cứu ngoại khoa tối khẩn.<br>• Phình đại tràng bẩm sinh biến chứng viêm ruột (Hirschsprung enterocolitis):<br>1) Trẻ sơ sinh chậm đi phân su > 24 giờ sau sinh, tiền sử táo bón bụng chướng to.<br>2) Đột ngột sốt cao, tiêu chảy phân tóe nước mùi khắm thối lẫn máu, chướng bụng dữ dội và sốc nhiễm trùng.<br><br><b>💡 Giải thích của AI:</b><br>Viêm ruột do Hirschsprung là biến chứng tử vong hàng đầu ở trẻ phình đại tràng; cần đặt ống thông trực tràng thụt tháo giải áp khẩn cấp và dùng kháng sinh mạnh.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 94, Mục 5.2.1)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Xoan-ruot",
            "Hirschsprung"
        ]
    },
    {
        "id": "PED55-B50",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Bệnh viêm ruột mạn - IBD",
        "front": "Phân biệt tổn thương đường tiêu hóa giữa Bệnh Crohn và Viêm loét đại trực tràng chảy máu (UC) ở trẻ lớn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bệnh Crohn:<br>1) Phạm vi: Tổn thương có thể ở BẤT KỲ VỊ TRÍ NÀO từ miệng đến hậu môn (thường gặp nhất ở đoạn cuối hồi tràng và manh tràng).<br>2) Tính chất: Tổn thương NGẮT QUÃNG ('nhảy cóc'), thâm nhiễm TOÀN BỘ BỀ DÀY THÀNH RUỘT.<br>3) Biến chứng: Rất hay có nứt kẽ, rò và áp xe quanh hậu môn, hẹp ruột.<br>• Viêm loét đại trực tràng chảy máu (UC):<br>1) Phạm vi: CHỈ TỔN THƯƠNG Ở ĐẠI TRÀNG VÀ TRỰC TRÀNG (bắt đầu từ trực tràng lan liên tục lên trên).<br>2) Tính chất: Tổn thương LIÊN TỤC KHÔNG NHẢY CÓC, CHỈ KHU TRÚ Ở LỚP NIÊM MẠC.<br>3) Biểu hiện: Đi ngoài phân lỏng nhiều máu đỏ tươi và chất nhầy mủ rầm rộ.<br><br><b>💡 Giải thích của AI:</b><br>Tổn thương nhảy cóc xuyên thành là đặc trưng của Crohn; tổn thương liên tục nông ở niêm mạc đại tràng là đặc trưng của UC.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 95, Mục IBD)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "IBD",
            "Crohn",
            "UC"
        ]
    },
    {
        "id": "PED55-B51",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Rửa dạ dày & Ngoại khoa",
        "front": "Kỹ thuật Rửa dạ dày bằng nước muối lạnh và 2 nhóm chỉ định Điều trị ngoại khoa cấp cứu trong xuất huyết tiêu hóa theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kỹ thuật rửa dạ dày nước muối lạnh: Đặt sonde dạ dày hút sạch máu đọng, sau đó bơm rửa nhẹ nhàng bằng dung dịch Natri Clorid 0,9% lạnh (4 - 8°C); tác dụng làm co mạch tạm thời niêm mạc dạ dày và theo dõi tốc độ chảy máu tiếp diễn.<br>• 2 nhóm chỉ định điều trị ngoại khoa cấp cứu:<br>1) Nhóm thất bại nội khoa: Xuất huyết tiêu hóa chảy máu ồ ạt không cầm sau khi đã hồi sức tích cực tối đa và thất bại với nội soi can thiệp.<br>2) Nhóm bệnh lý ngoại khoa cấp tính: Lồng ruột hoại tử hoặc tháo lồng thất bại, xoắn ruột, túi thừa Meckel loét thủng chảy máu, thủng ổ loét dạ dày tá tràng.<br><br><b>💡 Giải thích của AI:</b><br>Rửa dạ dày bằng nước muối lạnh còn giúp làm sạch thức ăn và máu đọng để cuộc nội soi tiêu hóa cấp cứu sau đó quan sát ổ loét rõ ràng nhất.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 99, Mục 6.4 & 6.5)",
        "tags": [
            "PED-55",
            "Barem-goc",
            "Rua-da-day",
            "Dieu-tri-ngoai-khoa"
        ]
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
    }
]
