# -*- coding: utf-8 -*-
"""
ped53_cards_data.py
Bo the MASTER DUAL-TRACK cho PED-53 Hach to o tre em.
Gop 2 luong trong 1 file duy nhat:
- Track 1 [BAREM GOC Y THAI BINH]: 42 the Basic bao phu 100% cau chu giao trinh (Trang 55 - 61).
- Track 2 [EBM HIEN DAI & LAM SANG]: 18 the Basic giai quyet co do, ALL vs EBV, sinh thiet, cam bay.
Tong cong: 60 the Basic chuyen sau, xuong dong ro rang, khong sot bat ky chi tiet nao.
"""

cards_data = [
    {
        "id": "PED53-B01",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Mục tiêu bài học",
        "front": "3 mục tiêu học tập chính của bài Hạch to ở trẻ em theo giáo trình Y Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Trình bày được các nguyên nhân gây ra hạch to.<br>2) Trình bày được cách tiếp cận chẩn đoán hạch to.<br>3) Điều trị được một số nguyên nhân gây ra hạch to thường gặp.<br><br><b>💡 Giải thích của AI:</b><br>3 mục tiêu này là khung sườn định hình cấu trúc đề thi lý thuyết và vấn đáp lâm sàng của Bộ môn Nhi ĐHYD Thái Bình.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, Mục tiêu bài học)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Muc-tieu"
        ]
    },
    {
        "id": "PED53-B02",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Định nghĩa định lượng",
        "front": "Định nghĩa định lượng Hạch to ở trẻ em theo từng vị trí giải phẫu và ngưỡng kích thước hạch bệnh lý theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bình thường: Trẻ sơ sinh phần lớn KHÔNG sờ thấy hạch; trẻ nhỏ có thể sờ thấy hạch nhỏ ở vùng cổ, nách, bẹn.<br>• Ngưỡng định nghĩa hạch to:<br>1) Vùng cổ hoặc nách: Đường kính hạch > 1 cm.<br>2) Vùng bẹn: Đường kính hạch > 1,5 cm.<br>• Ngưỡng khẳng định hạch bệnh lý: Hạch có đường kính > 2 cm HOẶC hạch có tính chất to lên dần theo thời gian.<br><br><b>💡 Giải thích của AI:</b><br>Mô lympho ở trẻ nhỏ phát triển mạnh mẽ đáp ứng với kích thích miễn dịch thông thường, do đó các hạch nhỏ &le; 1 cm ở cổ/nách hay &le; 1,5 cm ở bẹn là hạch phản ứng sinh lý.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, 58, Mục Đại cương)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Dinh-nghia",
            "Kich-thuoc-hach"
        ]
    },
    {
        "id": "PED53-B03",
        "track": "barem_goc",
        "type": "basic",
        "section": "B0",
        "category": "Cơ chế sinh bệnh chung",
        "front": "Cơ chế sinh bệnh chung dẫn đến Hạch bạch huyết to theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hạch bạch huyết to là hậu quả của 2 cơ chế chính:<br>1) Cơ chế tăng sinh: Tăng sinh các thành phần tế bào nội tại của hạch (tế bào lympho, tương bào, đại thực bào) do có kích thích của một kháng nguyên.<br>2) Cơ chế thâm nhiễm: Thâm nhiễm các tế bào từ ngoài hạch vào, bao gồm bạch cầu đa nhân (trong viêm sinh mủ) hoặc tế bào ác tính di căn.<br>• Diễn biến: Hạch to thường là đáp ứng với nhiễm khuẩn tại chỗ (khi hết kháng nguyên thì hạch nhỏ lại); nếu kháng nguyên kích thích tồn tại kéo dài sẽ làm hạch to mạn tính.<br><br><b>💡 Giải thích của AI:</b><br>Nắm chắc 2 cơ chế (tăng sinh miễn dịch nội tại vs thâm nhiễm tế bào ngoại lai) giúp phân biệt nhanh hạch phản ứng viêm với hạch ung thư thâm nhiễm.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, Mục I - Nguyên nhân)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Co-che-sinh-benh"
        ]
    },
    {
        "id": "PED53-B04",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Khung 8 nhóm nguyên nhân",
        "front": "Kể tên 8 nhóm nguyên nhân lớn gây hạch bạch huyết to ở trẻ em theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Gồm 8 nhóm nguyên nhân lớn:<br>1) Nhiễm khuẩn (Vi khuẩn, virus, đơn bào, xoắn khuẩn, nấm, bệnh Kawasaki).<br>2) Bệnh mô liên kết (Viêm khớp dạng thấp thiếu niên, Lupus ban đỏ hệ thống).<br>3) Tình trạng quá mẫn (Bệnh huyết thanh, phản ứng thuốc).<br>4) Bệnh ác tính (U lympho, Lơxêmi, di căn ung thư, bệnh tăng mô bào).<br>5) Rối loạn tăng sinh mô bạch huyết (Bệnh Castleman, Rosai-Dorfman, ALPS, u hạt lympho).<br>6) Bệnh tích lũy (Bệnh Niemann-Pick, Loạn dưỡng cystin).<br>7) Bệnh u hạt (Bệnh Sarcoidosis, Bệnh tăng u hạt mạn tính - CGD).<br>8) Nguyên nhân khác (Phơi nhiễm Beryllium, cường giáp, viêm hạch sau tiêm chủng).<br><br><b>💡 Giải thích của AI:</b><br>Khung 8 nhóm nguyên nhân này là câu hỏi lý thuyết kinh điển 10 điểm của bộ môn Nhi Thái Bình, bắt buộc phải thuộc đủ 8 đề mục.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55 - 56, Mục I - Nguyên nhân)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "8-nhom-nguyen-nhan",
            "Tong-quan"
        ]
    },
    {
        "id": "PED53-B05",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nhóm 1: Nhiễm khuẩn",
        "front": "Kể tên các căn nguyên vi sinh vật và bệnh lý thuộc nhóm Nhiễm khuẩn gây hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Vi khuẩn: Nhiễm khuẩn da, tụ cầu, liên cầu, nhiễm khuẩn huyết, lao, Mycobacteria không điển hình (NTM), Brucella, thương hàn, bạch hầu, giang mai.<br>2) Virus: Tăng bạch cầu đơn nhân nhiễm khuẩn (EBV), Cytomegalovirus (CMV), Rubella, Thủy đậu, HIV, Adenovirus, Herpes, bệnh mèo cào.<br>3) Đơn bào: Toxoplasma, Trypanosoma.<br>4) Xoắn khuẩn: Giang mai.<br>5) Nấm: Nấm da, Histoplasma.<br>6) Bệnh Kawasaki.<br><br><b>💡 Giải thích của AI:</b><br>Barem xếp bệnh mèo cào vào dòng virus; thực tế tác nhân Bartonella henselae là vi khuẩn. Khi thi, liệt kê đúng như barem.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, Mục I.1 - Nhiễm khuẩn)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Nhiem-khuan",
            "Can-nguyen"
        ]
    },
    {
        "id": "PED53-B06",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nhóm 2 & 3: Mô liên kết & Quá mẫn",
        "front": "Các bệnh mô liên kết và tình trạng quá mẫn gây hạch to ở trẻ em theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bệnh mô liên kết:<br>1) Viêm khớp dạng thấp.<br>2) Lupus ban đỏ hệ thống.<br>• Tình trạng quá mẫn:<br>1) Bệnh huyết thanh.<br>2) Phản ứng thuốc.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: ở trẻ em, viêm khớp dạng thấp tương ứng viêm khớp tự phát thiếu niên (JIA), hạch to rõ nhất ở thể hệ thống; thuốc hay gây hạch to là thuốc chống động kinh (Phenytoin, Carbamazepin).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55 - 56, Mục I.2 & I.3)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Mo-lien-ket",
            "Qua-man"
        ]
    },
    {
        "id": "PED53-B07",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nhóm 4: Bệnh ác tính",
        "front": "Kể tên các bệnh lý ác tính gây hạch to ở trẻ em theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) U lympho ác tính: U lympho Hodgkin và U lympho không Hodgkin.<br>2) Bệnh lơxêmi (Bạch cầu cấp / Ung thư máu).<br>3) Di căn ung thư (U nguyên bào thần kinh, sarcoma...).<br>4) Các bệnh tăng mô bào (Histiocytosis):<br>• Tăng mô bào tế bào Langerhans (LCH).<br>• Tăng mô bào liên võng tủy.<br>• Tăng mô bào lympho thực bào hồng cầu gia đình (HLH).<br><br><b>💡 Giải thích của AI:</b><br>Bệnh ác tính là nguyên nhân nguy hiểm nhất cần loại trừ đầu tiên khi hạch to cứng chắc, không đau, không viêm và dính tổ chức sâu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 56, Mục I.4 - Bệnh ác tính)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Ac-tinh",
            "U-lympho",
            "Loxemi"
        ]
    },
    {
        "id": "PED53-B08",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nhóm 5: Tăng sinh mô bạch huyết",
        "front": "Kể tên các bệnh lý thuộc nhóm Rối loạn tăng sinh mô bạch huyết gây hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Bệnh hạch bạch huyết nguyên bào miễn dịch mạch và loạn protein máu.<br>2) Hội chứng tăng sinh bạch huyết liên kết nhiễm sắc thể X (X-linked lymphoproliferative syndrome).<br>3) Bệnh u hạt dạng lympho (Lymphomatoid granulomatosis).<br>4) Bệnh tăng mô bào xoang với hạch bạch huyết to (Bệnh Rosai-Dorfman).<br>5) Bệnh Castleman: Quá sản hạch bạch huyết khổng lồ, quá sản hạch bạch huyết nang mạch.<br>6) Hội chứng tăng sinh bạch huyết tự miễn (ALPS).<br><br><b>💡 Giải thích của AI:</b><br>Đây là các rối loạn tăng sinh mô lympho không ác tính hiếm gặp nhưng có thể tiến triển thành u lympho thực sự nếu không theo dõi sát.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 56, Mục I.5 - Rối loạn tăng sinh)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Tang-sinh-bach-huyet",
            "Castleman",
            "Rosai-Dorfman"
        ]
    },
    {
        "id": "PED53-B09",
        "track": "barem_goc",
        "type": "basic",
        "section": "B1",
        "category": "Nhóm 6, 7 & 8: Tích lũy, U hạt & Khác",
        "front": "Kể tên các bệnh tích lũy, bệnh u hạt và các nguyên nhân khác gây hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bệnh tích lũy: Bệnh Niemann-Pick, Bệnh loạn dưỡng Cystin.<br>• Bệnh u hạt: Bệnh Sarcoidosis (bệnh sarcoid), Bệnh tăng u hạt mạn tính (CGD - Chronic Granulomatous Disease).<br>• Nguyên nhân khác:<br>1) Phơi nhiễm Beryllium.<br>2) Cường giáp (Basedow).<br>3) Loạn gamma globulin máu với bệnh hạch bạch huyết tiên phát.<br>4) Viêm hạch sau tiêm chủng (đặc biệt phản ứng hạch nách/cổ sau tiêm vắc xin phòng lao BCG).<br><br><b>💡 Giải thích của AI:</b><br>Hạch nách cùng bên sau tiêm phòng lao BCG ở trẻ nhũ nhi là tình trạng rất phổ biến, đa số tự thoái triển trong vài tháng.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 56, Mục I.6, I.7, I.8)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Tich-luy",
            "U-hat",
            "BCG"
        ]
    },
    {
        "id": "PED53-B10",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Khai thác bệnh sử nhiễm khuẩn",
        "front": "Các thông tin bệnh sử cần khai thác về tình trạng nhiễm khuẩn và định hướng bệnh Lao ở trẻ có hạch to?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thời gian xuất hiện hạch to từ bao lâu.<br>• Dấu hiệu nhiễm khuẩn chung: Có sốt không (sốt thất thường, kéo dài hay tái diễn), đau họng, viêm đường hô hấp trên, ho kéo dài, ổ nhiễm khuẩn vùng da/niêm mạc dẫn lưu bạch huyết.<br>• Dấu hiệu định hướng bệnh Lao (luôn luôn chú ý):<br>1) Hỏi tiền sử tiêm chủng vắc xin phòng lao BCG và kiểm tra sẹo tiêm phòng lao.<br>2) Tiền sử tiếp xúc với người mắc bệnh lao trong gia đình/xung quanh.<br>3) Tình trạng sụt cân, mệt mỏi, đổ mồ hôi trộm về đêm.<br><br><b>💡 Giải thích của AI:</b><br>Việt Nam là vùng dịch tễ lao cao, khai thác sẹo BCG, nguồn lây lao và triệu chứng nhiễm lao chung là bắt buộc trong mọi hồ sơ bệnh án hạch to.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 56 - 57, Mục 2.1 - Bệnh sử)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Benh-su",
            "Nhiem-khuan",
            "Lao"
        ]
    },
    {
        "id": "PED53-B11",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Khai thác bệnh sử ác tính & tự miễn",
        "front": "Các thông tin bệnh sử gợi ý Bệnh ác tính và Bệnh mô liên kết ở trẻ có hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Gợi ý bệnh ác tính (Lơxêmi, u lympho):<br>1) Sốt thất thường kéo dài không rõ nguyên nhân.<br>2) Chảy máu mũi (chảy máu cam), chảy máu chân răng.<br>3) Xuất hiện các mảng bầm tím, chấm xuất huyết ở da (biểu hiện giảm tiểu cầu).<br>• Gợi ý bệnh mô liên kết tự miễn: Đau mỏi các khớp, sưng khớp, phát ban ngoài da kèm sốt kéo dài.<br>• Thuốc & Vắc xin: Lưu ý tiền sử dùng các loại thuốc gần đây (kháng sinh, chống động kinh) và các vắc xin mới tiêm chủng.<br><br><b>💡 Giải thích của AI:</b><br>Hạch to đi kèm xuất huyết dưới da hoặc đau xương khớp là dấu hiệu cảnh báo đỏ của suy tủy do lơxêmi thâm nhiễm.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.1 - Bệnh sử)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Benh-su",
            "Ac-tinh",
            "Mo-lien-ket"
        ]
    },
    {
        "id": "PED53-B12",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Khai thác tiền sử dịch tễ đặc biệt",
        "front": "Những yếu tố tiền sử dịch tễ và tiếp xúc động vật đặc biệt cần hỏi khi trẻ có hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Bệnh sử liên quan đến nhiễm HIV.<br>2) Tiền sử bị mèo cào.<br>3) Tiền sử súc vật cắn.<br>4) Tổn thương ở da.<br>5) Mới đi chuyển từ xa về.<br><br><b>💡 Giải thích của AI:</b><br>Bệnh mèo cào là nguyên nhân hay bị bỏ sót: hạch vùng dẫn lưu (nách, cổ) to lên khoảng 1–3 tuần sau vết cào.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.1 - Bệnh sử)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Benh-su",
            "Dich-te",
            "Meo-cao"
        ]
    },
    {
        "id": "PED53-B13",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Hạch khu trú vs toàn thể",
        "front": "Phân biệt Hạch to khu trú và Hạch to toàn thể? Nguyên nhân gây hạch to toàn thể theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạch to khu trú: Hạch to ở một vùng giải phẫu duy nhất, thường do tổn thương viêm hoặc u ở khu vực dẫn lưu bạch huyết tương ứng.<br>• Hạch to toàn thể: Được định nghĩa khi HẠCH TO TRÊN HAI VÙNG HẠCH KHÔNG GẦN NHAU (không tiếp giáp nhau).<br>• Nguyên nhân hạch to toàn thể:<br>1) Nhiễm khuẩn toàn thể: Lao, thương hàn, giang mai, Brucella.<br>2) Nhiễm virus: EBV, CMV, HIV, Rubella.<br>3) Nhiễm đơn bào (Toxoplasma) hoặc nấm lan tỏa.<br>4) Bệnh tự miễn (Lupus, JIA), bệnh ác tính (Lơxêmi, U lympho), bệnh tích lũy lipid, bệnh huyết thanh, phản ứng thuốc.<br><br><b>💡 Giải thích của AI:</b><br>Định nghĩa 'trên 2 vùng hạch không gần nhau' (ví dụ hạch cổ kèm hạch bẹn) là mốc chuẩn để xác định bệnh lý mang tính chất toàn thân.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.2 - Khám xét)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Khu-tru-vs-Toan-the"
        ]
    },
    {
        "id": "PED53-B14",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Hạch ở sâu",
        "front": "Các vị trí Hạch ở sâu trong cơ thể có thể bị to và các phương tiện chẩn đoán hình ảnh để phát hiện?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Các vị trí hạch ở sâu: Hạch mạc treo ruột, hạch sau phúc mạc, hạch trung thất.<br>• Đặc điểm: Các hạch này thường to, nhiều hạch và dính thành khối; thường là biểu hiện của bệnh lý toàn thân.<br>• Phương tiện chẩn đoán: Không thể sờ thấy trên khám lâm sàng, bắt buộc phải dùng:<br>1) Chụp X-quang lồng ngực.<br>2) Siêu âm ổ bụng.<br>3) Chụp cắt lớp vi tính (CLVT / CT scan).<br>• Lưu ý: Hạch trung thất to ở trẻ em ngoài nguyên nhân do lao, PHẦN LỚN LÀ BỆNH ÁC TÍNH.<br><br><b>💡 Giải thích của AI:</b><br>Hạch trung thất to ở trẻ em là cờ đỏ báo động cấp cứu U lympho nguyên bào lympho hoặc U lympho Hodgkin chèn ép đường thở.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.2 - Khám xét)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Hach-o-sau",
            "Trung-that",
            "Mac-treo"
        ]
    },
    {
        "id": "PED53-B15",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Vùng dẫn lưu: Chẩm & Quanh tai",
        "front": "Nguyên nhân phổ biến gây hạch to ở vùng Chẩm và vùng Quanh tai theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch chẩm to: Nhiễm khuẩn vùng da đầu (chốc lở, nhọt da đầu, chấy rận), Nhiễm virus Rubella.<br>2) Hạch quanh tai (trước tai) to: Nhiễm khuẩn ở mắt (viêm kết mạc, hội chứng mắt - hạch Parinaud), Bệnh mèo cào (Bartonella henselae).<br><br><b>💡 Giải thích của AI:</b><br>Hạch chẩm to kèm phát ban mịn và sốt nhẹ là dấu hiệu lâm sàng kinh điển của bệnh Rubella ở trẻ nhỏ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.2 - Vùng hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Vung-dan-luu",
            "Hach-cham",
            "Quanh-tai"
        ]
    },
    {
        "id": "PED53-B16",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Vùng dẫn lưu: Cổ & Dưới hàm",
        "front": "Nguyên nhân phổ biến gây hạch to ở vùng Cổ và vùng Dưới hàm theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch cổ to: Viêm hạch do tụ cầu, liên cầu khuẩn, viêm amydal, viêm bạch cầu đơn nhân nhiễm khuẩn (EBV), Toxoplasma, bệnh ác tính, bệnh Kawasaki.<br>2) Hạch dưới hàm to: Lao, U lympho Hodgkin, U lympho không Hodgkin, bệnh nấm Histoplasma.<br><br><b>💡 Giải thích của AI:</b><br>Hạch cổ to một bên cấp tính kèm sốt cao ≥ 5 ngày không đáp ứng kháng sinh, mắt đỏ, môi đỏ nứt nẻ phải nghĩ ngay đến bệnh Kawasaki để điều trị IVIG phòng phình động mạch vành.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57 - 58, Mục 2.2 - Vùng hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Vung-dan-luu",
            "Hach-co",
            "Duoi-ham"
        ]
    },
    {
        "id": "PED53-B17",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Vùng dẫn lưu: Nách & Chậu bẹn",
        "front": "Nguyên nhân phổ biến gây hạch to ở vùng Nách và vùng Chậu bẹn theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch nách to: Nhiễm khuẩn vùng cánh tay, thành ngực; bệnh ác tính; bệnh mèo cào.<br>2) Hạch vùng chậu bẹn to: Nhiễm khuẩn ở chi dưới, nhiễm khuẩn vùng háng.<br><br><b>💡 Giải thích của AI:</b><br>Khi thấy hạch nách hoặc hạch bẹn to đơn độc, luôn tìm ổ xước da hoặc nhiễm trùng ở toàn bộ chi tương ứng. Ngoài barem: hạch nách cùng bên tiêm còn gặp trong viêm hạch sau tiêm BCG (xem E17).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục 2.2 - Vùng hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Vung-dan-luu",
            "Hach-nach",
            "Chau-ben"
        ]
    },
    {
        "id": "PED53-B18",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Vùng dẫn lưu: Trung thất & Ổ bụng",
        "front": "Nguyên nhân phổ biến gây hạch to ở vùng Trung thất và vùng Ổ bụng theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch trung thất to: Lao, bệnh ác tính, bệnh nấm Histoplasma, bệnh sarcoid.<br>2) Hạch bụng to: Bệnh ác tính, viêm hạch mạc treo.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: bệnh ác tính ở trung thất thường là u lympho (Hodgkin, không Hodgkin, lơxêmi dòng T); ở ổ bụng hay gặp u lympho Burkitt, khối to nhanh có thể gây lồng ruột hoặc tắc ruột.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục 2.2 - Vùng hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Vung-dan-luu",
            "Trung-that",
            "O-bung"
        ]
    },
    {
        "id": "PED53-B19",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Quy luật hạch thượng đòn",
        "front": "Ý nghĩa lâm sàng và định hướng bệnh lý của hạch to vùng thượng đòn (thượng đòn trái và thượng đòn phải) theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạch thượng đòn to: nên tìm bệnh lý ở trung thất. Sờ thấy hạch thượng đòn thì phải tìm bệnh lý ở trong lồng ngực hay trong ổ bụng.<br>1) Hạch thượng đòn trái: nhiều khi là bệnh ác tính phát triển từ trong ổ bụng lan rộng ra ống ngực tới vùng thượng đòn trái.<br>2) Hạch thượng đòn phải: chứng tỏ có tổn thương trong lồng ngực, vì hạch này dẫn lưu bạch huyết từ phổi và trung thất.<br>• Hạch thượng đòn và hạch nách cùng to: thường là tình trạng bệnh nặng.<br><br><b>💡 Giải thích của AI:</b><br>Hạch thượng đòn trái còn gọi là hạch Virchow (Troisier). Thực hành EBM coi mọi hạch thượng đòn sờ thấy là cờ đỏ (xem E01): cần đánh giá khẩn bằng X-quang ngực, siêu âm, xét nghiệm và hạ thấp ngưỡng sinh thiết; hạch Virchow cũng có thể do lao.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.2 - Khám xét)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Thuong-don",
            "Hach-Virchow",
            "Co-do"
        ]
    },
    {
        "id": "PED53-B20",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Kích thước hạch bệnh lý",
        "front": "Ngưỡng kích thước nào bắt buộc phải coi là Hạch bệnh lý theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ngưỡng kích thước: Hạch bạch huyết to trên 2 cm (> 2 cm) phải coi là bệnh lý.<br>• Tính chất tiến triển: Hạch bạch huyết to lên dần, càng ngày càng to là hạch bệnh lý.<br><br><b>💡 Giải thích của AI:</b><br>Phân biệt hai mốc dễ nhầm: > 2 cm là ngưỡng coi hạch là bệnh lý (cần tìm nguyên nhân); > 2,5 cm kèm xét nghiệm không kết luận được là một chỉ định sinh thiết (xem B26).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục Kích thước hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Kich-thuoc-benh-ly",
            "Tren-2cm"
        ]
    },
    {
        "id": "PED53-B21",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "4 Kiểu tính chất hạch",
        "front": "Phân biệt 4 kiểu tính chất sờ nắn hạch lâm sàng giúp định hướng nguyên nhân theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch to một vùng, đau phù nề quanh hạch, mặt da đỏ nóng: Viêm hạch bạch huyết cấp tính do vi khuẩn (điều trị kháng sinh 2 tuần không đỡ phải theo dõi sát).<br>2) Hạch to nhiều nơi, hạch dính vào nhau, sờ không đau, không đỏ ngoài da: Nhiễm khuẩn lan tỏa, nhiễm virus, bao gồm cả Lao và các bệnh toàn thể.<br>3) Hạch to, mật độ cứng chắc, sờ không đau, dính sâu vào tổ chức xung quanh: Nghi ngờ hạch di căn ung thư hoặc thâm nhiễm của bệnh lý ác tính.<br>4) Hạch to nhiều hạch dính chuỗi, mặt da đỏ không đều, có hạch chắc có hạch mềm, rò rỉ dịch nhầy bã đậu (không phải mủ): Nghĩ ngay tới HẠCH LAO.<br><br><b>💡 Giải thích của AI:</b><br>Mô tả 'mặt da đỏ không đều, hạch chắc lẫn hạch mềm hóa bã đậu rò dịch nhầy' là hình ảnh mô tả lâm sàng kinh điển của Bệnh tràng nhạc (lao hạch) (lao hạch).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục Tính chất hạch to)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Tinh-chat-hach",
            "4-kieu-tinh-chat"
        ]
    },
    {
        "id": "PED53-B22",
        "track": "barem_goc",
        "type": "basic",
        "section": "B4",
        "category": "Khám toàn thân kết hợp",
        "front": "Khi phát hiện trẻ có hạch to, người thầy thuốc cần khám toàn diện những cơ quan nào để tìm dấu hiệu kết hợp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Tuyến giáp: Xem tuyến giáp có phì đại to không (phát hiện cường giáp Basedow).<br>2) Khám bụng: Bắt buộc sờ nắn xem Gan và Lách có to không.<br>3) Hệ cơ xương khớp: Kiểm tra có viêm đau các khớp không (bệnh mô liên kết Lupus, JIA).<br>4) Da và niêm mạc: Tìm các ban ngoài da, chấm bầm máu xuất huyết.<br>5) Mắt: Kiểm tra có vàng mắt, vàng da hoặc viêm kết mạc mắt không.<br><br><b>💡 Giải thích của AI:</b><br>Không bao giờ được dừng lại ở việc sờ mỗi hạch cổ; khám toàn thân từ đầu đến chân mới giúp định vị bản chất bệnh lý tại chỗ hay toàn thân.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục Khám toàn thân)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Kham-toan-than"
        ]
    },
    {
        "id": "PED53-B23",
        "track": "barem_goc",
        "type": "basic",
        "section": "B4",
        "category": "Hội chứng kết hợp: Lao & Lơxêmi",
        "front": "Hai hội chứng lâm sàng kết hợp kinh điển: Hạch to định hướng bệnh Lao và Hạch to định hướng bệnh Lơxêmi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Định hướng bệnh Lao: Hạch to kèm theo sốt thất thường, kéo dài, mạn tính, cơ thể suy yếu, ho kéo dài → Cần tìm lao để xác định chẩn đoán.<br>• Định hướng bệnh Lơxêmi hoặc bệnh tăng mô bào: Hạch to toàn thể kèm theo GAN TO, LÁCH TO, XUẤT HUYẾT và THIẾU MÁU.<br><br><b>💡 Giải thích của AI:</b><br>Gan, lách, hạch to kèm thiếu máu và xuất huyết gợi ý mạnh bạch cầu cấp hoặc bệnh tăng mô bào; cần làm huyết đồ, phết máu ngoại vi và tủy đồ. EBV cũng có gan, lách, hạch to nhưng thường không suy tủy nặng (xem E04).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục Khám toàn thân)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Hoi-chung-ket-hop",
            "Lao",
            "Loxemi"
        ]
    },
    {
        "id": "PED53-B24",
        "track": "barem_goc",
        "type": "basic",
        "section": "B4",
        "category": "Hội chứng kết hợp: U lympho & HIV",
        "front": "Hai hội chứng lâm sàng kết hợp: Hạch to định hướng U lympho ác tính và Hạch to định hướng nhiễm HIV?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Định hướng U lympho ác tính: Hạch to ở ngoại biên KẾT HỢP VỚI HẠCH Ở TRONG SÂU (trung thất, ổ bụng).<br>• Định hướng nhiễm HIV: Hạch to toàn thể kèm theo sụt cân, sốt kéo dài không rõ nguyên nhân, rối loạn tiêu hóa mạn tính và lách to.<br><br><b>💡 Giải thích của AI:</b><br>U lympho thường khởi phát bằng một hạch cổ hoặc hạch nách không đau nhưng khi chụp phim ngực/bụng lại phát hiện khối hạch trong sâu khổng lồ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58, Mục Khám toàn thân)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Hoi-chung-ket-hop",
            "U-lympho",
            "HIV"
        ]
    },
    {
        "id": "PED53-B25",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Xét nghiệm chẩn đoán ban đầu",
        "front": "Các xét nghiệm cận lâm sàng không xâm nhập và chỉ định xét nghiệm tủy đồ trong chẩn đoán hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Xét nghiệm lựa chọn theo nguyên nhân nghi ngờ:<br>1) Máu ngoại biên, tốc độ máu lắng.<br>2) Các nghiệm pháp trong da phát hiện lao, bệnh mèo cào, bệnh nấm.<br>3) Cấy vi khuẩn vùng tổn thương.<br>4) Huyết thanh chẩn đoán CMV, Toxoplasma, EBV; chẩn đoán HIV.<br>5) Chụp X-quang, CLVT, siêu âm ổ bụng tìm hạch sâu, khối u.<br>6) Chọc hút hạch bạch huyết để nuôi cấy tìm vi khuẩn, xét nghiệm tế bào học.<br>• Chỉ định tủy đồ: khi nghi một bệnh huyết học như lơxêmi, bệnh tăng mô bào, u lympho, bệnh tích lũy lipid.<br><br><b>💡 Giải thích của AI:</b><br>Nguyên tắc: làm xét nghiệm không xâm nhập trước, rồi mới đến sinh thiết hạch. Ngoài barem: test da bệnh mèo cào hiện không còn dùng; thực hành nay chẩn đoán bằng huyết thanh hoặc PCR Bartonella.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59, Mục 2.3 - Xét nghiệm)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Xet-nghiem",
            "Tuy-do",
            "Huyet-thanh"
        ]
    },
    {
        "id": "PED53-B26",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Chỉ định sinh thiết hạch",
        "front": "4 chỉ định bắt buộc phải Sinh thiết hạch bạch huyết theo đúng giáo trình Nhi khoa Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sinh thiết hạch bạch huyết được chỉ định khi có 1 trong 4 điều kiện:<br>1) Nghi ngờ một bệnh lý ác tính (hạch cứng, dính, không đau, sụt cân, triệu chứng B).<br>2) Các xét nghiệm ban đầu không kết luận được VÀ kích thước hạch bạch huyết trên 2,5 cm (> 2,5 cm).<br>3) Hạch bạch huyết to kéo dài (không rõ nguyên nhân).<br>4) Hạch to đã dùng kháng sinh điều trị trong vòng 1 tháng mà hạch không lui.<br><br><b>💡 Giải thích của AI:</b><br>Mốc hạch > 2,5 cm và điều trị kháng sinh 1 tháng không lui là 2 mốc số liệu vàng khi thi lý thuyết của Bộ môn.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59, Mục Sinh thiết hạch)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Sinh-thiet-hach",
            "4-chi-dinh"
        ]
    },
    {
        "id": "PED53-B27",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Kỹ thuật sinh thiết hạch",
        "front": "4 nguyên tắc kỹ thuật quan trọng khi tiến hành lấy hạch sinh thiết theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Vị trí lấy hạch: KHÔNG NÊN sinh thiết hạch ở phần trên cổ và vùng bẹn (vì hay bị viêm phản ứng mạn xơ hóa khó đọc kết quả); NÊN sinh thiết hạch ở vùng dưới cổ và vùng nách để có kết quả tin cậy hơn.<br>2) Lựa chọn hạch: Nên sinh thiết HẠCH TO NHẤT, không phải là hạch dễ lấy nhất. Cần hội chẩn giữa chuyên khoa ung bướu và ngoại khoa để chọn hạch.<br>3) Quy cách lấy bệnh phẩm: Cần sinh thiết lấy NGUYÊN VẸN CẢ BAO HẠCH (Excisional biopsy), tuyệt đối KHÔNG lấy từng mảnh vụn.<br>4) Bảo quản và gửi bệnh phẩm: Phải gửi ngay tới nhà giải phẫu bệnh trong MÔI TRƯỜNG NUÔI CẤY TỔ CHỨC để tránh mô bị khô; KHÔNG để chỗ ánh sáng mạnh, chỗ nóng; TUYỆT ĐỐI KHÔNG BỌC TRONG GẠC KHÔ.<br><br><b>💡 Giải thích của AI:</b><br>Lấy nguyên cả bao hạch giúp nhà giải phẫu bệnh đánh giá được toàn vẹn cấu trúc nang lympho, phân biệt U lympho nang với tăng sản phản ứng lành tính.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59, Mục Chú ý sinh thiết)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Sinh-thiet-hach",
            "Ky-thuat",
            "Bao-quan"
        ]
    },
    {
        "id": "PED53-B28",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Xét nghiệm trên bệnh phẩm sinh thiết",
        "front": "Các xét nghiệm chuyên sâu cần tiến hành trên bệnh phẩm sinh thiết hạch theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Nuôi cấy và nhuộm Gram tìm vi khuẩn, virus, nấm.<br>2) Xét nghiệm virus.<br>3) Mô học.<br>4) Kính hiển vi điện tử.<br>5) Nhuộm hóa mô.<br>6) Đếm tế bào dưới dòng chảy.<br>7) Nghiên cứu gen với thụ thể tế bào T và gen globulin miễn dịch để xác định tính đơn dòng trong bệnh lơxêmi và u lympho.<br><br><b>💡 Giải thích của AI:</b><br>Tính đơn dòng (TCR, Ig) là bằng chứng hỗ trợ mạnh cho u lympho hoặc lơxêmi, nhưng phải kết hợp mô bệnh học và hóa mô miễn dịch; một số tăng sinh lành tính cũng có thể có dòng tế bào trội.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59 - 60, Mục Xét nghiệm sinh thiết)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Sinh-thiet-hach",
            "Xet-nghiem-chuyen-sau"
        ]
    },
    {
        "id": "PED53-B29",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị viêm hạch cấp vi khuẩn",
        "front": "Phác đồ kháng sinh và thời gian điều trị Viêm hạch cấp tính do vi khuẩn theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Căn nguyên: Viêm hạch cấp, đặc biệt hay gặp vùng đầu mặt cổ, thường do liên cầu khuẩn tan huyết nhóm A hoặc tụ cầu vàng (ở sơ sinh và trẻ nhỏ có thể gặp liên cầu nhóm B).<br>• Kháng sinh tác dụng với liên cầu nhóm A và tụ cầu vàng: Amoxicillin-clavulanic hoặc nhóm Cephalosporin.<br>• Nghi tụ cầu kháng Methicillin cộng đồng (CA-MRSA): Clindamycin hoặc Trimethoprim-sulfamethoxazol.<br>• Thời gian: 10–14 ngày hoặc ít nhất sau 5 ngày các dấu hiệu viêm giảm. Đường dùng: uống hoặc tiêm.<br>• Hạch có mủ: dẫn lưu mủ, nhuộm Gram tìm vi khuẩn để lựa chọn kháng sinh thích hợp.<br><br><b>💡 Giải thích của AI:</b><br>Dẫn lưu mủ KHÔNG áp dụng khi nghi lao (barem cấm rạch, dẫn lưu – xem B31). Ngoài barem: mèo cào hóa mủ và viêm hạch sau BCG cũng chỉ chọc hút kim, không rạch (xem E10, E17).",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Dieu-tri",
            "Khang-sinh",
            "Viem-hach-cap"
        ]
    },
    {
        "id": "PED53-B30",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị vi khuẩn kỵ khí",
        "front": "Phác đồ kháng sinh khi nghi ngờ nhiễm trùng vi khuẩn kỵ khí gây viêm hạch vùng đầu mặt cổ theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nguồn gốc: Thường liên quan tới các ổ nhiễm khuẩn từ vùng miệng, họng, răng hàm mặt.<br>• Kháng sinh lựa chọn: Dùng Metronidazol hoặc Clindamycin.<br>• Phối hợp: Có thể kết hợp Metronidazol/Clindamycin với nhóm Cephalosporin thế hệ 3 (như Cefotaxime hoặc Ceftriaxone) để bao phủ phổ vi khuẩn rộng.<br><br><b>💡 Giải thích của AI:</b><br>Vi khuẩn kỵ khí khoang miệng tiết nhiều men phá hủy mô mạnh, tạo dịch mủ thối và hoại tử mô nhanh chóng.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Dieu-tri",
            "Vi-khuan-ky-khi",
            "Metronidazol"
        ]
    },
    {
        "id": "PED53-B31",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị Lao hạch & NTM",
        "front": "Nguyên tắc điều trị Lao hạch và Viêm hạch do Mycobacteria không điển hình (NTM)? Quy tắc an toàn bắt buộc?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạch lao hoặc Mycobacteria gây viêm hạch khó phân biệt trên lâm sàng.<br>• Nhiều chủng Mycobacteria không điển hình (NTM) kháng với thuốc chống lao nên thường phải CẮT BỎ HẠCH.<br>• QUY TẮC AN TOÀN: TRÁNH RẠCH HOẶC DẪN LƯU HẠCH TRONG TRƯỜNG HỢP NHIỄM LAO.<br><br><b>💡 Giải thích của AI:</b><br>Rạch hạch lao hoặc NTM dễ tạo đường rò kéo dài và sẹo xấu. Lỗi kinh điển ở tuyến cơ sở: thấy hạch mềm tưởng áp xe thông thường liền rạch tháo mủ.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Dieu-tri",
            "Lao-hach",
            "NTM",
            "Cam-rach"
        ]
    },
    {
        "id": "PED53-B32",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Điều trị Mèo cào & Herpes",
        "front": "Thái độ điều trị Bệnh mèo cào và Viêm hạch do Herpes simplex theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bệnh mèo cào: viêm hạch thường tự ổn định. Ở bệnh nhân giảm miễn dịch có thể dùng kháng sinh: Azithromycin, Rifampin, Doxycyclin.<br>• Nhiễm virus Herpes simplex nặng kèm viêm hạch cục bộ: Acyclovir đường uống rút ngắn thời gian bệnh.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem (CDC): ở trẻ khỏe mạnh kháng sinh là tùy chọn; một nghiên cứu nhỏ cho thấy Azithromycin làm hạch nhỏ nhanh hơn nhưng kết cục chung không khác biệt.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60 - 61, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Dieu-tri",
            "Meo-cao",
            "Herpes",
            "Acyclovir"
        ]
    },
    {
        "id": "PED53-B33",
        "track": "barem_goc",
        "type": "basic",
        "section": "B7",
        "category": "Bẫy thi - Vị trí sinh thiết",
        "front": "Giáo trình khuyến cáo nên và không nên sinh thiết hạch ở vùng nào? Vì sao?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Không nên sinh thiết hạch phần trên cổ và hạch vùng bẹn.<br>• Nên sinh thiết hạch vùng dưới cổ và nách để có kết quả tin cậy hơn.<br><br><b>💡 Giải thích của AI:</b><br>Barem không giải thích lý do. Suy luận: hạch trên cổ và bẹn thường xuyên nhận kích thích viêm từ khoang miệng, amidan, chi dưới nên hay có viêm phản ứng mạn, dễ cho kết quả mô bệnh học không đặc hiệu.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59, Mục Chú ý sinh thiết)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Bay-thi",
            "Vi-tri-sinh-thiet"
        ]
    },
    {
        "id": "PED53-B34",
        "track": "barem_goc",
        "type": "basic",
        "section": "B7",
        "category": "Bẫy thi - Tụ cầu sơ sinh",
        "front": "Căn nguyên vi khuẩn gây viêm hạch cấp tính có hoặc không kèm viêm mô tế bào đặc thù ở trẻ sơ sinh là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ở trẻ sơ sinh và trẻ nhỏ, ngoài liên cầu nhóm A và tụ cầu vàng, có thể gặp LIÊN CẦU KHUẨN NHÓM B (Streptococcus agalactiae) gây viêm hạch có hoặc không có viêm mô tế bào.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: trẻ nhũ nhi có hội chứng viêm mô tế bào – viêm hạch do liên cầu nhóm B cần được đánh giá nhiễm khuẩn huyết và viêm màng não đi kèm.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Bay-thi",
            "Lien-cau-nhom-B",
            "So-sinh"
        ]
    },
    {
        "id": "PED53-B35",
        "track": "barem_goc",
        "type": "basic",
        "section": "B7",
        "category": "Bẫy thi - Ký sinh trùng & Nấm",
        "front": "Kể tên các căn nguyên đơn bào và nấm gây hạch to theo giáo trình Y Thái Bình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đơn bào: Toxoplasma, Trypanosoma.<br>• Nấm: Nấm da, Histoplasma (gây hạch dưới hàm, hạch trung thất to).<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: Toxoplasma lây qua phân mèo hoặc thịt chưa nấu chín, thường gây hạch cổ không đau. Sau EBV, CMV và Toxoplasma đều có thể gây hội chứng giống tăng bạch cầu đơn nhân.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, 58)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Bay-thi",
            "Toxoplasma",
            "Histoplasma"
        ]
    },
    {
        "id": "PED53-E01",
        "track": "ebm",
        "type": "basic",
        "section": "E0",
        "category": "Cờ đỏ cấp cứu & Ác tính",
        "front": "5 dấu hiệu Cờ đỏ (Red Flags) báo động hạch to ác tính hoặc chèn ép cấp cứu sinh tử ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch vùng thượng đòn (Supraclavicular node): Bất kể kích thước bao nhiêu đều là dấu hiệu ác tính cho đến khi có bằng chứng ngược lại.<br>2) Khối hạch trung thất gây ho khan, khó thở, thở rít hoặc Hội chứng tĩnh mạch chủ trên (SVCS: phù áo choàng, tĩnh mạch cổ nổi to).<br>3) Hạch có mật độ cứng như đá (stony hard), dính chặt vào mô sâu hoặc kết thành chùm bất động (matted nodes), kích thước > 2 - 3 cm.<br>4) Xuất hiện bộ ba 'Triệu chứng B' của U lympho: Sốt không rõ nguyên nhân kéo dài > 38°C, sụt cân > 10% trong 6 tháng, đổ mồ hôi trộm đêm ướt đầm áo gối.<br>5) Hạch to toàn thể đi kèm thiếu máu, xuất huyết dưới da hoặc đau xương khớp dữ dội về đêm (Cờ đỏ Bạch cầu cấp ALL).<br><br><b>💡 Giải thích của AI:</b><br>Có bất kỳ cờ đỏ nào trong số trên là chỉ định chụp X-quang ngực khẩn cấp và hội chẩn chuyên khoa Huyết học - Ung bướu ngay trong 24 giờ.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Sàng lọc cờ đỏ hạch to ác tính (Bước 0)",
        "tags": [
            "PED-53",
            "EBM",
            "Co-do",
            "Red-flags",
            "Ac-tinh"
        ]
    },
    {
        "id": "PED53-E02",
        "track": "ebm",
        "type": "basic",
        "section": "E0",
        "category": "Hội chứng SVCS do hạch trung thất",
        "front": "Hội chứng tĩnh mạch chủ trên (SVCS) do hạch trung thất khổng lồ ở trẻ em biểu hiện như thế nào và vì sao là cấp cứu sinh tử?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Biểu hiện lâm sàng: Khối hạch trung thất trước to (thường do U lympho tế bào T hoặc Hodgkin) chèn ép tĩnh mạch chủ trên gây:<br>1) Phù nề mặt, cổ và hai tay ('phù áo choàng').<br>2) Tĩnh mạch cổ nổi to, tuần hoàn bàng hệ nổi rõ ở thành ngực trên.<br>3) Khó thở tăng khi nằm ngửa, tím tái, thở rít thanh khí quản.<br>• Nguy cơ sinh tử: Có thể gây xẹp đường thở hoàn toàn và ngừng tim đột ngột khi đặt trẻ nằm ngửa hoặc khi gây mê làm thủ thuật.<br><br><b>💡 Giải thích của AI:</b><br>Để trẻ ở tư thế dễ thở (ngồi, nghiêng), giữ thở tự nhiên, tránh thuốc an thần và giãn cơ. Chỉ gây mê khi đã có kế hoạch đa chuyên khoa (gây mê – huyết học – ngoại) và sẵn nội soi phế quản cứng; mở khí quản không giải quyết được chỗ hẹp ở khí quản dưới và phế quản gốc.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cấp cứu chèn ép trung thất SVCS (Bước 0)",
        "tags": [
            "PED-53",
            "EBM",
            "SVCS",
            "Hach-trung-that",
            "Cap-cuu"
        ]
    },
    {
        "id": "PED53-E03",
        "track": "ebm",
        "type": "basic",
        "section": "E1",
        "category": "Tam giác thâm nhiễm",
        "front": "Tại sao Bạch cầu cấp (ALL) lại biểu hiện bằng Tam giác thâm nhiễm: Hạch to — Gan to — Lách to?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cơ chế: Các tế bào non ác tính dòng lympho (Lymphoblast) sinh sôi vô độ trong tủy xương rồi tràn vào dòng máu tuần hoàn.<br>• Chúng di chuyển và thâm nhiễm ồ ạt vào hệ thống liên võng nội mô của cơ thể bao gồm các hạch bạch huyết, các bè gan và tủy đỏ của lách.<br>• Sự thâm nhiễm tế bào non ngoại lai làm phá vỡ cấu trúc mô bình thường, gây phì đại đồng thời cả hạch toàn thể, gan to và lách to.<br><br><b>💡 Giải thích của AI:</b><br>Hạch trong ALL to do thâm nhiễm tế bào ác tính từ tủy xương tràn ra, khác với hạch trong nhiễm trùng to do tăng sinh miễn dịch tại chỗ.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Tam giác thâm nhiễm trong ALL (Phần III.1)",
        "tags": [
            "PED-53",
            "EBM",
            "Tam-giac-tham-nhiem",
            "ALL",
            "Gan-Lach-Hach"
        ]
    },
    {
        "id": "PED53-E04",
        "track": "ebm",
        "type": "basic",
        "section": "E1",
        "category": "Phân biệt EBV vs ALL",
        "front": "Bảng phân định lâm sàng và huyết học chi tiết: Nhiễm trùng EBV (Tăng bạch cầu đơn nhân) vs Bạch cầu cấp (ALL)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nhiễm trùng EBV (Tăng bạch cầu đơn nhân):<br>1) Lâm sàng: Viêm họng giả mạc trắng dày, hạch cổ đối xứng đau nhẹ, gan lách to nhẹ.<br>2) Huyết học: Không suy tủy nặng; có thể giảm tiểu cầu hoặc bạch cầu hạt nhẹ, thoáng qua (khoảng 50%), hiếm khi xuất huyết nặng.<br>3) Tế bào máu: Tế bào lympho không điển hình (Downey) đa hình thái, không có blast.<br>4) Xét nghiệm đặc hiệu: Kháng thể IgM VCA (+); test Monospot thường âm tính giả ở trẻ dưới 4–5 tuổi.<br>• Bạch cầu cấp (ALL):<br>1) Lâm sàng: Hạch to không đau, đau nhức xương khớp dữ dội về đêm.<br>2) Huyết học: SUY TỦY RÕ RỆT (thiếu máu nặng + giảm tiểu cầu gây xuất huyết dưới da, chảy máu mũi).<br>3) Hóa sinh: Axit uric và LDH máu tăng vọt.<br>4) Tủy đồ: Tế bào non ác tính (Blast) chiếm ≥ 20%.<br><br><b>💡 Giải thích của AI:</b><br>Chìa khóa phân biệt: EBV có lympho không điển hình đa hình thái và tế bào máu hồi phục dần; ALL có blast đơn dạng và suy tủy ngày càng nặng. Khi còn nghi ngờ, làm phết máu ngoại vi và tủy đồ.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Bảng phân định EBV vs ALL (Phần III.2)",
        "tags": [
            "PED-53",
            "EBM",
            "Phan-biet",
            "EBV",
            "ALL",
            "Tieu-cau"
        ]
    },
    {
        "id": "PED53-E05",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Cạm bẫy dùng Corticoid",
        "front": "Vì sao không được dùng corticoid thử để làm nhỏ hạch khi trẻ có hạch to chưa rõ chẩn đoán?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hiệu ứng xóa mờ chẩn đoán: Corticoid tiêu diệt tế bào non ung thư máu (Lymphoblast) rất nhanh nhưng không triệt để.<br>• Hậu quả:<br>1) Làm hạch nhỏ lại tạm thời tạo cảm giác khỏi bệnh giả tạo, nhưng bệnh ác tính vẫn tiến triển.<br>2) Tủy đồ, sinh thiết sau đó dễ âm tính giả, làm chậm trễ chẩn đoán u lympho, lơxêmi.<br>3) Có thể khởi phát Hội chứng ly giải khối u cấp (TLS) đe dọa tử vong do suy thận cấp.<br>• Ngoại lệ: khối trung thất gây suy hô hấp hoặc chèn ép tĩnh mạch chủ trên đe dọa tính mạng, không gây mê an toàn được → có thể dùng steroid theo quyết định đa chuyên khoa, sau khi đã cố lấy mẫu chẩn đoán từ vị trí khác (dịch màng phổi, tủy, hạch ngoại vi).<br><br><b>💡 Giải thích của AI:</b><br>Không kê corticoid cho trẻ có hạch to chưa rõ nguyên nhân ngoài tình huống cấp cứu đường thở nêu trên.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy dùng Corticoid thử nghiệm (Phần VI.1)",
        "tags": [
            "PED-53",
            "EBM",
            "Cam-bay",
            "Cam-Corticoid",
            "ALL"
        ]
    },
    {
        "id": "PED53-E06",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Cạm bẫy lạm dụng FNA",
        "front": "Vì sao không nên lạm dụng Chọc hút kim nhỏ (FNA) ở trẻ em có hạch to nghi ngờ u lympho?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạn chế của FNA: Chọc hút kim nhỏ chỉ lấy được tế bào rời rạc (tế bào học), không đánh giá được kiến trúc mô học của hạch (nang lympho, vùng tủy, vỏ hạch).<br>• Âm tính giả đáng kể: FNA âm tính không loại trừ được u lympho, dễ kết luận nhầm là tăng sản phản ứng lành tính.<br>• Ưu tiên sinh thiết lấy trọn hạch (Excisional biopsy) để làm mô bệnh học và hóa mô miễn dịch; sinh thiết lõi kim (core needle) dưới hướng dẫn hình ảnh khi hạch ở sâu hoặc nguy cơ gây mê cao.<br><br><b>💡 Giải thích của AI:</b><br>Barem vẫn liệt kê chọc hút hạch để nuôi cấy vi khuẩn và xét nghiệm tế bào học (xem B25); điểm cần nhớ là FNA không thay thế sinh thiết khi nghi u lympho.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Cạm bẫy lạm dụng FNA (Phần VI.2)",
        "tags": [
            "PED-53",
            "EBM",
            "Cam-bay",
            "FNA",
            "Sinh-thiet-tron-ven"
        ]
    },
    {
        "id": "PED53-E07",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Cạm bẫy chẩn đoán nhầm dị tật cổ",
        "front": "Phân biệt Hạch to vùng cổ với các Dị tật bẩm sinh vùng cổ thường gặp (Nang giáp lưỡi, Nang khe mang, U bạch mạch)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Nang ống giáp lưỡi: Nằm ở CHÍNH GIỮA CỔ (đường giữa), có đặc tính kinh điển là DI ĐỘNG LÊN XUỐNG THEO NHỊP NUỐT VÀ KHI THÈ LƯỠI.<br>2) Nang khe mang (Branchial cleft cyst): Nằm ở bờ trước cơ ức đòn chũm (thường ở 1/3 trên hoặc 1/3 giữa), tròn nhẵn, không đau trừ khi bội nhiễm.<br>3) U bạch mạch dạng nang (Cystic hygroma): Thường ở tam giác cổ sau, mật độ rất mềm, ranh giới không rõ, SOi ĐÈN CÓ TÍNH CHẤT THẤU QUANG DƯƠNG TÍNH.<br><br><b>💡 Giải thích của AI:</b><br>Nang giáp lưỡi di động theo nhịp nuốt do dính vào xương móng; U bạch mạch soi đèn thấu quang do chứa dịch bạch huyết trong suốt.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Phân biệt dị tật bẩm sinh vùng cổ (Phần VI.5)",
        "tags": [
            "PED-53",
            "EBM",
            "Cam-bay",
            "Nang-giap-luoi",
            "Nang-khe-mang",
            "Hygroma"
        ]
    },
    {
        "id": "PED53-E08",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Bệnh mô bào Langerhans - LCH",
        "front": "Tam chứng kinh điển và dấu hiệu hóa mô miễn dịch đặc hiệu của Bệnh mô bào tế bào Langerhans (LCH)? Hạch to gặp ở thể nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tam chứng kinh điển (Hand-Schüller-Christian): tổn thương xương dẹt (ổ tiêu xương đục lỗ ở xương sọ) + lồi mắt + đái tháo nhạt trung ương.<br>• Hạch to, ban vảy da đầu (dễ nhầm viêm da tiết bã, 'cứt trâu') và gan lách to là biểu hiện của thể đa hệ (Letterer-Siwe, thường ở trẻ dưới 2 tuổi), không thuộc tam chứng.<br>• Hóa mô miễn dịch đặc hiệu: CD1a dương tính và Langerin (CD207) dương tính.<br><br><b>💡 Giải thích của AI:</b><br>Thấy trẻ có hạch to kèm ban vảy da đầu dai dẳng và tổn thương đục lỗ xương sọ → nghĩ ngay đến LCH và sinh thiết tổn thương.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Bệnh mô bào tế bào Langerhans LCH (Phần XI.1); MSD Manual Professional — Langerhans Cell Histiocytosis.",
        "tags": [
            "PED-53",
            "EBM",
            "LCH",
            "Langerhans",
            "Tieu-xuong-so"
        ]
    },
    {
        "id": "PED53-E09",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Hội chứng thực bào máu - HLH",
        "front": "Hội chứng thực bào máu (HLH) ở trẻ em có các tiêu chuẩn chẩn đoán xét nghiệm sinh tử nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chẩn đoán HLH khi có đột biến gen hoặc đạt ≥ 5/8 tiêu chuẩn sau:<br>1) Sốt cao kéo dài liên tục.<br>2) Lách to.<br>3) Giảm tế bào máu ngoại vi từ 2 dòng trở lên (Hb &lt; 90 g/L, Tiểu cầu &lt; 100 G/L, Neutrophil &lt; 1 G/L).<br>4) Tăng Triglycerid máu (≥ 3 mmol/L) và/hoặc Giảm Fibrinogen máu (≤ 1,5 g/L).<br>5) Nồng độ FERRITIN HUYẾT THANH TĂNG CỰC CAO (thường &ge; 500 ng/mL, đặc biệt > 3000 - 10.000 ng/mL).<br>6) Hiện tượng thực bào tế bào máu trong tủy xương, lách hoặc hạch.<br>7) Giảm hoặc mất hoạt tính tế bào NK.<br>8) Tăng nồng độ thụ thể CD25 hòa tan (sIL-2R).<br><br><b>💡 Giải thích của AI:</b><br>Ferritin tăng hàng nghìn ng/mL kết hợp giảm Fibrinogen và lách to là cặp dấu hiệu chỉ điểm bão cytokine đe dọa tử vong của HLH.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Hội chứng thực bào máu HLH (Phần XI.2)",
        "tags": [
            "PED-53",
            "EBM",
            "HLH",
            "Thuc-bao-mau",
            "Ferritin"
        ]
    },
    {
        "id": "PED53-E10",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Bệnh mèo cào - Xử trí mủ",
        "front": "Bệnh cảnh lâm sàng điển hình của Bệnh mèo cào và nguyên tắc xử trí khi hạch bị hóa mủ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bệnh cảnh điển hình: Trẻ có tiền sử bị mèo cào hoặc liếm vào vết xước trước đó 1 - 3 tuần; xuất hiện sẩn đỏ hoặc mụn mủ tại vết cào; sau đó hạch lympho vùng dẫn lưu (hạch nách, hạch cổ, hạch bẹn) sưng to đơn độc, đau nhẹ.<br>• Xử trí khi hạch hóa mủ:<br>1) CHỈ DÙNG KIM CHỌC HÚT GIẢI ÁP để giảm đau và giải tỏa căng tức cho trẻ.<br>2) TUYỆT ĐỐI KHÔNG ĐƯỢC RẠCH MỔ DẪN LƯU HỞ.<br>• Lý do cấm rạch: Rạch hạch trong bệnh mèo cào sẽ tạo đường rò mủ kéo dài và để lại sẹo xấu xơ chai.<br><br><b>💡 Giải thích của AI:</b><br>Cùng nguyên tắc với lao hạch: hạch mèo cào hóa mủ chỉ được chọc hút bằng kim vô khuẩn, cấm rạch mổ mở.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Bệnh mèo cào và xử trí mủ (Phần VII.2, X.3)",
        "tags": [
            "PED-53",
            "EBM",
            "Meo-cao",
            "Bartonella",
            "Choc-hut-kim"
        ]
    },
    {
        "id": "PED53-E11",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Lao hạch - Bệnh tràng nhạc",
        "front": "Đặc điểm lâm sàng của Lao hạch cổ (Bệnh tràng nhạc - Scrofula) và phác đồ điều trị kháng lao chuẩn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đặc điểm lâm sàng: Thường gặp ở vùng cổ; các hạch to dần, dính vào nhau thành chuỗi hoặc chùm, không nóng không đỏ lúc đầu; sau đó nhuyễn hóa dính vào da, da tím tái rồi vỡ rò chất bã đậu, tạo vết loét lâu liền và sẹo co kéo nhăn nheo hình 'chân rết'.<br>• Phác đồ điều trị kháng lao chuẩn: Điều trị nội khoa theo phác đồ chống lao quốc gia:<br>1) Giai đoạn tấn công (2 tháng): 4 thuốc Rifampicin (R) + Isoniazid (H) + Pyrazinamid (Z) + Ethambutol (E).<br>2) Giai đoạn duy trì (4 tháng): 2 thuốc Rifampicin (R) + Isoniazid (H).<br>• Tổng thời gian điều trị: 6 tháng (2RHZE / 4RH).<br><br><b>💡 Giải thích của AI:</b><br>Lao hạch là thể lao ngoài phổi hay gặp nhất ở trẻ em; điều trị bằng thuốc kháng lao toàn thân là biện pháp cốt lõi chữa lành bệnh.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Lao hạch ngoại biên (Phần VII.3)",
        "tags": [
            "PED-53",
            "EBM",
            "Lao-hach",
            "Scrofula",
            "Trang-nhac",
            "2RHZE"
        ]
    },
    {
        "id": "PED53-E12",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Trình tự Tủy đồ vs Sinh thiết hạch",
        "front": "Quy tắc xác định trình tự ưu tiên giữa Chọc hút tủy đồ và Sinh thiết hạch khi tiếp cận trẻ có hạch to bất thường?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Quy tắc ưu tiên:<br>1) Nếu trẻ có HẠCH TO KÈM THEO GAN LÁCH TO HOẶC BẤT THƯỜNG TẾ BÀO MÁU NGOẠI BIÊN (thiếu máu, giảm tiểu cầu, tăng/giảm bạch cầu bất thường) → BẮT BUỘC CHỌC TỦY ĐỒ TRƯỚC.<br>2) Nếu Tủy đồ bình thường HOẶC bệnh nhân chỉ có hạch to đơn độc khu trú (không có biểu hiện tủy) → MỚI TIẾN HÀNH PHẪU THUẬT SINH THIẾT HẠCH.<br>• Lý do: Chọc hút tủy đồ là thủ thuật đơn giản, ít xâm lấn, cho kết quả chẩn đoán nhanh trong vài giờ; trong khi sinh thiết hạch là một cuộc phẫu thuật mở cần gây mê/tiền mê và có nguy cơ biến chứng chảy máu, nhiễm trùng.<br><br><b>💡 Giải thích của AI:</b><br>Chọc tủy đồ trước giúp chẩn đoán ngay Bạch cầu cấp ALL mà không cần phải mổ xẻ hạch của trẻ một cách không cần thiết.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Trình tự chỉ định tủy đồ vs sinh thiết (Phần X.4)",
        "tags": [
            "PED-53",
            "EBM",
            "Tuy-do-truoc",
            "Sinh-thiet-sau",
            "Trinh-tu"
        ]
    },
    {
        "id": "PED53-E13",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "10 Quy tắc vàng thực chiến tại giường",
        "front": "Kể tên 5 trong số các Quy tắc vàng thực chiến khi tiếp cận trẻ có hạch to tại giường bệnh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Hạch thượng đòn bất kể kích thước đều là cờ đỏ ác tính.<br>2) Không bao giờ dùng Corticoid để thử làm giảm kích thước hạch.<br>3) Luôn luôn sờ nắn tìm Gan to và Lách to khi thấy trẻ có hạch to.<br>4) Tránh sinh thiết hạch bẹn và hạch vùng trên cổ nếu có hạch ở vị trí khác.<br>5) Không rạch mổ hạch nghi ngờ do lao hoặc bệnh mèo cào vì sẽ gây rò mủ kéo dài.<br><br><b>💡 Giải thích của AI:</b><br>Đây là 5 quy tắc thực chiến đúc kết từ hàng nghìn ca lâm sàng, giúp bác sĩ không bao giờ mắc sai lầm chuyên môn nghiêm trọng.",
        "extra": "📖 Nguồn: EBM Lâm sàng — 10 Quy tắc vàng thực chiến (Phần X.2)",
        "tags": [
            "PED-53",
            "EBM",
            "Quy-tac-vang",
            "Thuc-chien"
        ]
    },
    {
        "id": "PED53-B36",
        "track": "ebm",
        "type": "basic",
        "section": "B1",
        "category": "Bệnh Kawasaki & Hạch to",
        "front": "Đặc điểm hạch cổ to trong Bệnh Kawasaki và các tiêu chuẩn chẩn đoán lâm sàng đi kèm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đặc điểm hạch: Hạch cổ to thường ở MỘT BÊN, kích thước ≥ 1,5 cm, khu trú tam giác cổ trước, không đau hoặc đau nhẹ, thường KHÔNG hóa mủ.<br>• Chẩn đoán: Sốt ≥ 5 ngày + ≥ 4/5 tiêu chuẩn lâm sàng (hạch cổ là 1 trong 5):<br>1) Viêm kết mạc mắt hai bên không tiết mủ.<br>2) Biến đổi khoang miệng: Môi đỏ khô nứt nẻ, lưỡi dâu tây, họng đỏ.<br>3) Biến đổi đầu chi: Phù mu bàn tay/chân, đỏ lòng bàn tay/chân ở giai đoạn cấp; bong da quanh móng ở giai đoạn bán cấp.<br>4) Phát ban đa dạng toàn thân (không có mụn nước).<br>5) Hạch cổ như trên.<br><br><b>💡 Giải thích của AI:</b><br>Barem chỉ nêu Kawasaki là nguyên nhân hạch cổ to; tiêu chuẩn chẩn đoán theo AHA 2017. Hạch là tiêu chuẩn ít gặp nhất; thể khởi đầu bằng hạch dễ nhầm viêm hạch vi khuẩn. Điều trị IVIG liều cao và Aspirin giảm biến chứng phình động mạch vành từ khoảng 25% xuống dưới 5%.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 55, 57: Kawasaki là nguyên nhân hạch cổ to); AHA Scientific Statement 2017 (McCrindle et al.) cho tiêu chuẩn chẩn đoán.",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Kawasaki",
            "Hach-co-1-ben"
        ]
    },
    {
        "id": "PED53-B37",
        "track": "ebm",
        "type": "basic",
        "section": "B3",
        "category": "Phân biệt hạch dưới hàm",
        "front": "Chẩn đoán phân biệt các nguyên nhân gây hạch dưới hàm to (giáo trình nêu 4 nguyên nhân, mở rộng thêm nhiễm khuẩn răng miệng)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Lao hạch: Hạch to dần, dính thành chuỗi, không nóng đỏ, có thể nhuyễn hóa rò bã đậu.<br>2) U lympho ác tính (Hodgkin và không Hodgkin): Hạch to nhanh, chắc, không đau, không dính da nhưng dính sâu vào mô nền.<br>3) Nhiễm nấm Histoplasma: Sốt kéo dài, hạch to kèm tổn thương loét niêm mạc miệng họng.<br>4) Nhiễm khuẩn răng miệng / Amidan: Hạch sưng nóng đỏ đau cấp tính, tìm thấy sâu răng, viêm quanh cuống hoặc áp xe quanh amidan.<br><br><b>💡 Giải thích của AI:</b><br>Khám hạch dưới hàm luôn luôn phải kết hợp soi kỹ khoang miệng và kiểm tra răng hàm mặt để tìm ổ nhiễm khuẩn tiên phát.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58: lao, U lympho Hodgkin, không Hodgkin, Histoplasma); phần mô tả lâm sàng và mục 4 là EBM mở rộng.",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Hach-duoi-ham",
            "Phan-biet"
        ]
    },
    {
        "id": "PED53-B38",
        "track": "ebm",
        "type": "basic",
        "section": "B3",
        "category": "Phân biệt hạch ổ bụng",
        "front": "Phân biệt Viêm hạch mạc treo ruột cấp tính với Hạch ổ bụng ác tính ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Viêm hạch mạc treo ruột cấp tính:<br>1) Thường xuất hiện sau đợt viêm đường hô hấp trên hoặc viêm ruột do virus.<br>2) Trẻ đau bụng từng cơn quanh rốn hoặc hố chậu phải, sốt nhẹ, không có phản ứng thành bụng thực sự.<br>3) Siêu âm bụng: Chùm hạch mạc treo to nhưng hình bầu dục, ranh giới rõ, còn rốn hạch, tự thoái lui sau 1 - 2 tuần.<br>• Hạch ổ bụng ác tính (U lympho Burkitt, u nguyên bào thần kinh):<br>1) Hạch phát triển rất nhanh thành khối lớn dính cố định, chèn ép gây bán tắc ruột, lồng ruột hoặc cổ trướng.<br>2) Siêu âm/CT: Khối hạch mất cấu trúc rốn hạch bình thường, thâm nhiễm mạc treo.<br><br><b>💡 Giải thích của AI:</b><br>Viêm hạch mạc treo là nguyên nhân thường gặp nhất gây đau bụng cấp giả viêm ruột thừa ở trẻ nhỏ; siêu âm là công cụ phân biệt tuyệt vời.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 58: hạch bụng to do bệnh ác tính, viêm hạch mạc treo); phần phân biệt lâm sàng và siêu âm là EBM mở rộng.",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Viem-hach-mac-treo",
            "Hach-o-bung"
        ]
    },
    {
        "id": "PED53-B39",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Tủy đồ trong chẩn đoán hạch to",
        "front": "Xét nghiệm Tủy đồ giúp xác định những bệnh lý huyết học và bệnh chuyển hóa nào ở trẻ có hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Bệnh lơxêmi (Bạch cầu cấp): Tủy đồ thấy các tế bào non ác tính (Blast) thâm nhiễm chiếm tỷ lệ cao (≥ 20%), ức chế các dòng tế bào tủy bình thường.<br>2) Bệnh tăng mô bào (Histiocytosis): Phát hiện các tế bào mô bào bất thường hoặc hiện tượng thực bào tế bào máu trong tủy.<br>3) U lympho ác tính: Đánh giá giai đoạn xem tế bào u lympho đã xâm lấn vào tủy xương hay chưa.<br>4) Bệnh tích lũy lipid (Bệnh Niemann-Pick, Gaucher): Phát hiện các tế bào bọt (Foam cells / Niemann-Pick cells) hoặc tế bào Gaucher chứa đầy lipid ứ đọng trong tủy xương.<br><br><b>💡 Giải thích của AI:</b><br>Tủy đồ là xét nghiệm quyết định xác lập chẩn đoán ung thư máu và các bệnh lý tích lũy bẩm sinh mà sinh thiết hạch đơn thuần không thể thay thế được.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 59, Mục 2.3 - Xét nghiệm)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Tuy-do",
            "Niemann-Pick",
            "Loxemi"
        ]
    },
    {
        "id": "PED53-B40",
        "track": "barem_goc",
        "type": "basic",
        "section": "B5",
        "category": "Xét nghiệm gen trên bệnh phẩm sinh thiết",
        "front": "Mục đích của việc nghiên cứu gen thụ thể tế bào T (TCR) và gen globulin miễn dịch (Ig) trên bệnh phẩm sinh thiết hạch theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Mục đích: XÁC ĐỊNH TÍNH ĐƠN DÒNG (Monoclonality) trong bệnh lơxêmi và u lympho.<br>• Cơ chế phân định:<br>1) Tăng sinh phản ứng (viêm): quần thể lympho mang thụ thể TCR và Ig đa dạng (đa dòng – Polyclonality).<br>2) Tăng sinh ác tính: tế bào u bắt nguồn từ một tế bào ban đầu nên mang chung một kiểu tái sắp xếp gen TCR hoặc Ig (đơn dòng).<br><br><b>💡 Giải thích của AI:</b><br>Xét nghiệm đơn dòng giúp ích nhiều ở các ca ranh giới giữa tăng sản phản ứng và u lympho sớm, nhưng không tự nó khẳng định ác tính; luôn đọc cùng mô bệnh học và hóa mô miễn dịch.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục Xét nghiệm sinh thiết)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "TCR",
            "Ig-gene",
            "Don-dong"
        ]
    },
    {
        "id": "PED53-B41",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Kháng sinh CA-MRSA",
        "front": "Khi nghi ngờ tụ cầu vàng kháng Methicillin cộng đồng (CA-MRSA) gây viêm hạch cấp tính, giáo trình khuyến cáo dùng những kháng sinh nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khuyến cáo dùng Clindamycin hoặc Trimethoprim-sulfamethoxazol (TMP-SMX).<br>• Lưu ý: Cephalosporin và Amoxicillin-clavulanic không có tác dụng với CA-MRSA.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem (IDSA 2011): Clindamycin 30–40 mg/kg/ngày chia 3–4 lần, là kháng sinh kìm khuẩn và ức chế sản xuất độc tố. TMP-SMX phủ kém liên cầu nhóm A nên khi cần phủ liên cầu phải phối hợp thêm β-lactam.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị); liều theo IDSA MRSA Guideline 2011.",
        "tags": [
            "PED-53",
            "Barem-goc",
            "CA-MRSA",
            "Clindamycin",
            "TMP-SMX"
        ]
    },
    {
        "id": "PED53-B42",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Phẫu thuật hạch NTM vs Lao",
        "front": "Vì sao viêm hạch do Mycobacteria không điển hình (NTM) thường phải phẫu thuật cắt bỏ toàn bộ hạch trong khi Lao hạch thì không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Mycobacteria không điển hình (NTM): nhiều chủng kháng với thuốc chống lao nên thường phải cắt bỏ hạch.<br>2) Lao hạch: tránh rạch hoặc dẫn lưu hạch; điều trị bằng thuốc chống lao.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: NTM (M. avium, M. scrofulaceum…) hay gặp ở trẻ 1–5 tuổi khỏe mạnh, hạch cổ một bên to dần, không triệu chứng toàn thân; cắt trọn hạch khỏi khoảng 95%. Phác đồ thuốc lao theo Chương trình chống lao quốc gia.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 60, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "NTM",
            "Cat-bo-hach"
        ]
    },
    {
        "id": "PED53-B43",
        "track": "barem_goc",
        "type": "basic",
        "section": "B2",
        "category": "Trình tự tiếp cận chẩn đoán",
        "front": "Trình tự tiếp cận chẩn đoán một trẻ có hạch to theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Khai thác kỹ bệnh sử.<br>2) Khám kỹ tính chất hạch to; hạch to khu trú hay toàn thể; các biểu hiện kèm theo.<br>3) Thăm dò các xét nghiệm không xâm nhập trước.<br>4) Sau đó mới sinh thiết hạch để nghiên cứu mô bệnh học về hình thái, mô miễn dịch học.<br><br><b>💡 Giải thích của AI:</b><br>Đây là khung trả lời cho mục tiêu 2 của bài; các thẻ bệnh sử, khám hạch, xét nghiệm và chỉ định sinh thiết đều đi theo trình tự này.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 56, Mục II - Tiếp cận chẩn đoán)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Tiep-can"
        ]
    },
    {
        "id": "PED53-B44",
        "track": "barem_goc",
        "type": "basic",
        "section": "B3",
        "category": "Hạch to khu trú",
        "front": "Hạch to khu trú một vùng thường do đâu? Nêu nguyên nhân thường gặp của hạch góc hàm, hạch cổ và hạch chẩm to theo giáo trình.",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hạch to khu trú một vùng thường do tổn thương ở khu vực dẫn lưu bạch huyết tương ứng:<br>1) Hạch góc hàm to: thường do nhiễm khuẩn ở họng, viêm amydal.<br>2) Hạch cổ to: thường thấy khi có nhiễm khuẩn đường hô hấp trên.<br>3) Hạch chẩm to và nhiều: thường do nhiễm khuẩn vùng da đầu.<br><br><b>💡 Giải thích của AI:</b><br>Khi khám hạch khu trú, luôn tìm ổ nhiễm khuẩn ở vùng mà hạch đó dẫn lưu trước khi nghĩ tới nguyên nhân toàn thân.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 57, Mục 2.2 - Khám xét)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Hach-khu-tru"
        ]
    },
    {
        "id": "PED53-B45",
        "track": "barem_goc",
        "type": "basic",
        "section": "B6",
        "category": "Hạch trong ung thư trẻ em",
        "front": "Đặc điểm hạch trong các bệnh ung thư trẻ em và thái độ xử trí theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hạch thường to, chắc, không đau.<br>• Kèm sốt không giải thích được, sụt cân, đổ mồ hôi đêm.<br>• Xử trí: nên chỉ định sinh thiết hạch để xác định nguyên nhân.<br><br><b>💡 Giải thích của AI:</b><br>Sốt, sụt cân, đổ mồ hôi đêm là nhóm triệu chứng B của u lympho; gặp bộ ba này cùng hạch chắc không đau thì không nên kéo dài điều trị kháng sinh thử.",
        "extra": "📖 Nguồn: Giáo trình Nhi khoa Y Thái Bình (Trang 61, Mục III - Điều trị)",
        "tags": [
            "PED-53",
            "Barem-goc",
            "Ung-thu"
        ]
    },
    {
        "id": "PED53-E14",
        "track": "ebm",
        "type": "basic",
        "section": "E0",
        "category": "Sinh lý mô lympho theo tuổi",
        "front": "Đặc điểm phát triển sinh lý của mô lympho theo lứa tuổi ở trẻ em và đỉnh cao phát triển ở độ tuổi nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sau sinh: Mô lympho còn nhỏ, trẻ sơ sinh phần lớn không sờ thấy hạch.<br>• Giai đoạn phát triển: Mô lympho tăng sinh trong thời thơ ấu, hạch đạt kích thước lớn nhất vào khoảng 8–12 tuổi.<br>• Giai đoạn thoái triển: Sau tuổi dậy thì, mô lympho nhỏ dần về kích thước của người trưởng thành.<br><br><b>💡 Giải thích của AI:</b><br>Vì vậy trẻ tuổi học đường hay sờ thấy vài hạch nhỏ lành tính ở cổ, nách, bẹn; điều này giúp bác sĩ trấn an gia đình khi hạch nhỏ, mềm, di động và không có dấu hiệu cảnh báo.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Phát triển mô lympho theo tuổi (Phần I.1); Ataş et al., Turk Pediatri Ars 2014 (PMC4462268).",
        "tags": [
            "PED-53",
            "EBM",
            "Sinh-ly-lympho",
            "Dinh-4-8-tuoi"
        ]
    },
    {
        "id": "PED53-E15",
        "track": "ebm",
        "type": "basic",
        "section": "E0",
        "category": "Dấu hiệu hạch Delphian",
        "front": "Hạch Delphian là gì? Vị trí giải phẫu và ý nghĩa lâm sàng đặc biệt của nó?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vị trí giải phẫu: Hạch lympho ở đường giữa cổ, phía trên eo tuyến giáp và trước màng nhẫn giáp (hạch tiền thanh quản – Prelaryngeal node).<br>• Ý nghĩa lâm sàng: Hạch Delphian to gợi ý:<br>1) Di căn ung thư tuyến giáp (đặc biệt thể nhú).<br>2) Ung thư thanh quản.<br><br><b>💡 Giải thích của AI:</b><br>Tên gọi 'Delphian' bắt nguồn từ lời sấm truyền đền Delphi: hạch này sưng to là điềm báo bệnh lý ác tính tại thanh quản hoặc tuyến giáp.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Dấu hiệu hạch Delphian (Phần I.2)",
        "tags": [
            "PED-53",
            "EBM",
            "Hach-Delphian",
            "Ung-thu-giap"
        ]
    },
    {
        "id": "PED53-E16",
        "track": "ebm",
        "type": "basic",
        "section": "E2",
        "category": "Hội chứng giả u lympho do thuốc",
        "front": "Hội chứng giả u lympho do thuốc (Drug-induced pseudolymphoma) là gì? Các thuốc thường gây ra tình trạng này?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bản chất: Hạch to toàn thân xuất hiện sau khi dùng thuốc, kèm sốt, phát ban da, tăng bạch cầu ái toan; mô bệnh học hạch có thể giống u lympho.<br>• Các thuốc thường gặp: Thuốc chống động kinh (Phenytoin, Carbamazepin, Lamotrigine, Phenobarbital), Allopurinol.<br>• Xử trí: NGỪNG THUỐC ngay; hạch thường thoái lui sau vài tuần.<br>• Cảnh giác: bệnh cảnh sốt + ban + tăng bạch cầu ái toan + hạch có thể là hội chứng DRESS, cần kiểm tra men gan, chức năng thận và các tạng.<br><br><b>💡 Giải thích của AI:</b><br>Luôn hỏi kỹ tiền sử dùng thuốc chống co giật trước khi quyết định sinh thiết hạch để tránh chẩn đoán nhầm sang u lympho.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Hội chứng giả u lympho (Phần II)",
        "tags": [
            "PED-53",
            "EBM",
            "Pseudolymphoma",
            "Phenytoin"
        ]
    },
    {
        "id": "PED53-E17",
        "track": "ebm",
        "type": "basic",
        "section": "E3",
        "category": "Viêm hạch sau tiêm BCG",
        "front": "Thái độ xử trí Viêm hạch nách sau tiêm vắc xin phòng lao BCG ở trẻ nhũ nhi theo hướng dẫn quốc tế?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Diễn tiến tự nhiên: Hạch nách cùng bên tiêm BCG sưng to là phản ứng miễn dịch thường gặp; hầu hết tự thoái triển trong vòng vài tháng mà không cần can thiệp.<br>• Nguyên tắc xử trí:<br>1) Thể không hóa mủ: Theo dõi định kỳ, KHÔNG DÙNG THUỐC KHÁNG LAO (vì chủng BCG kháng Pyrazinamid và đáp ứng kém).<br>2) Thể hóa mủ dọa vỡ da: CHỈ DÙNG KIM CHỌC HÚT VÔ KHUẨN GIẢI ÁP để tránh hạch tự vỡ loét.<br>3) TUYỆT ĐỐI CẤM RẠCH MỔ DẪN LƯU VÌ SẼ GÂY VẾT LOÉT RÒ MỦ BÃ ĐẬU KÉO DÀI.<br><br><b>💡 Giải thích của AI:</b><br>Phẫu thuật cắt bỏ hạch chỉ đặt ra khi hạch dính da tạo lỗ rò dai dẳng nhiều tháng không liền hoặc chọc hút thất bại.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Xử trí hạch sau tiêm BCG (Phần VII)",
        "tags": [
            "PED-53",
            "EBM",
            "Hach-BCG",
            "Choc-hut"
        ]
    },
    {
        "id": "PED53-E18",
        "track": "ebm",
        "type": "basic",
        "section": "E4",
        "category": "Quy trình xử lý bệnh phẩm sinh thiết",
        "front": "Quy trình xử lý bệnh phẩm sinh thiết hạch chuẩn quốc tế để đảm bảo chất lượng chẩn đoán mô bệnh học tối ưu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Lấy trọn vẹn cả bao hạch, chuyển NGAY sang giải phẫu bệnh ở trạng thái TƯƠI, KHÔNG CỐ ĐỊNH, trong môi trường nuôi cấy tổ chức (theo barem); nếu không có thì đặt trên gạc ẩm nước muối sinh lý, không để khô, không để chỗ nóng hay ánh sáng mạnh.<br>2) Chia mẫu mô vô khuẩn:<br>• Một phần gửi nuôi cấy vi sinh (vi khuẩn ái khí, kỵ khí, lao AFB, nấm).<br>• Một phần làm đếm tế bào dòng chảy (Flow cytometry) và sinh học phân tử.<br>• Phần còn lại cố định trong Formol đệm 10% để làm mô bệnh học và hóa mô miễn dịch.<br>3) Không ngâm formol toàn bộ hạch trước khi chia mẫu vi sinh.<br><br><b>💡 Giải thích của AI:</b><br>Nếu thả toàn bộ hạch vào lọ formol, vi khuẩn sẽ chết không cấy được và tế bào bị cố định không thể làm Flow cytometry.",
        "extra": "📖 Nguồn: EBM Lâm sàng — Quy trình xử lý bệnh phẩm sinh thiết (Phần XIII)",
        "tags": [
            "PED-53",
            "EBM",
            "Quy-trinh-sinh-thiet",
            "Flow-cytometry"
        ]
    }
]
