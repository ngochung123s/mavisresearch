# -*- coding: utf-8 -*-
"""
ped54_ebm_cards_data.py
Bộ thẻ Anki EBM Update cho bài học PED-54:
Tiếp cận Trẻ Đau khớp & Đi khập khiễng (Thang điểm Kocher, JIA, SCFE, Cờ đỏ ác tính).
Quy chuẩn: 1 thẻ 1 ý, back <= 3-4 dòng (3-5s), 100% Unicode.
"""

cards_data = [
    {
        "id": "PED54-EBM-001",
        "type": "basic",
        "section": "EBM_DinhNghia",
        "category": "Đau khớp vs Viêm khớp",
        "front": "Tiêu chuẩn lâm sàng then chốt để phân biệt Viêm khớp (Arthritis) với Đau khớp đơn thuần (Arthralgia) ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Viêm khớp bắt buộc có sưng khớp khách quan hoặc hạn chế biên độ vận động thụ động kèm đau/nóng.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Đau khớp đơn thuần hoàn toàn không sưng, không nóng đỏ và biên độ thụ động trọn vẹn.",
        "extra": "Không bao giờ chẩn đoán viêm khớp nếu chỉ dựa vào lời kêu đau chủ quan của trẻ.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Dinh-nghia"
        ]
    },
    {
        "id": "PED54-EBM-002",
        "type": "cloze",
        "section": "EBM_KhamKhop",
        "category": "Khám nhiệt độ khớp",
        "text": "Khi thăm khám nhiệt độ tại khớp để phát hiện phản ứng viêm, bác sĩ bắt buộc phải dùng {{c1::mu bàn tay}} áp lên khớp tổn thương và so sánh ngay với {{c1::khớp đối bên lành}}.",
        "extra": "Mu bàn tay có lớp da mỏng và mật độ thụ cảm nhiệt độ nhạy hơn nhiều so với lòng bàn tay.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-003",
        "type": "basic",
        "section": "EBM_KhamKhop",
        "category": "Nghiệm pháp Log-roll",
        "front": "Mục đích và cách thực hiện nghiệm pháp lăn đùi (Log-roll test) ở trẻ đau khớp háng là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Trẻ nằm ngửa duỗi thẳng chân, nhẹ nhàng lăn cẳng chân xoay trong - ngoài như khúc gỗ; đau hoặc co cứng cơ chỉ điểm viêm bao khớp háng.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Đây là nghiệm pháp thụ động nhạy cảm nhất phát hiện kích thích màng hoạt dịch khớp háng.",
        "extra": "Khớp háng nằm sâu không nhìn thấy sưng đỏ từ bên ngoài.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-004",
        "type": "basic",
        "section": "EBM_KhamKhop",
        "category": "Nghiệm pháp FABER",
        "front": "Nghiệm pháp FABER (Test Patrick - tư thế số 4) giúp phân định tổn thương tại hai vị trí giải phẫu nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đau bẹn trước: tổn thương khớp háng; Đau mông/thắt lưng sau: viêm khớp cùng chậu (Sacroiliitis).<br><b>💡 Cơ chế:</b> Gập - Giạng - Xoay ngoài làm căng tối đa bao khớp háng và khớp cùng chậu.",
        "extra": "Rất có giá trị trong thể JIA viêm điểm bám gân (ERA).",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-005",
        "type": "basic",
        "section": "EBM_KhamKhop",
        "category": "Dáng đi Trendelenburg",
        "front": "Dấu hiệu dáng đi Trendelenburg ở trẻ đi khập khiễng biểu hiện như thế nào và chỉ điểm tổn thương gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khung chậu bên lành bị sụp xuống khi trẻ đứng tỳ trọng lượng lên chân bệnh, chỉ điểm suy yếu cơ mông nhỡ hoặc biến dạng khớp háng.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Cơ mông nhỡ bên tỳ đè không đủ lực kéo giữ khung chậu nằm ngang.",
        "extra": "Thường gặp trong Trật khớp háng bẩm sinh (DDH) hoặc di chứng bệnh Perthes.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Dang-di"
        ]
    },
    {
        "id": "PED54-EBM-006",
        "type": "cloze",
        "section": "EBM_Kocher",
        "category": "5 Tiêu chuẩn Kocher cải tiến",
        "text": "5 tiêu chuẩn trong Thang điểm Kocher cải tiến phân biệt Viêm khớp nhiễm khuẩn háng gồm: (1) Sốt > 38.5°C; (2) {{c1::Không thể tỳ đè bước đi}}; (3) ESR > 40 mm/h; (4) {{c1::WBC > 12.000/µL}}; (5) {{c1::CRP > 20 mg/L}}.",
        "extra": "CRP > 20 mg/L là chỉ số xét nghiệm độc lập có độ nhạy và độ đặc hiệu cao nhất.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kocher",
            "Cap-cuu"
        ]
    },
    {
        "id": "PED54-EBM-007",
        "type": "cloze",
        "section": "EBM_Kocher",
        "category": "Xác suất theo điểm Kocher",
        "text": "Trong thang điểm Kocher: trẻ thỏa mãn 3 tiêu chuẩn có xác suất Viêm khớp nhiễm khuẩn khoảng {{c1::93%}}, và thỏa mãn 4-5 tiêu chuẩn có xác suất lên tới {{c1::99%}}.",
        "extra": "Nếu đạt ≥ 3 điểm, bắt buộc chỉ định chọc hút dịch khớp háng khẩn cấp.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kocher"
        ]
    },
    {
        "id": "PED54-EBM-008",
        "type": "basic",
        "section": "EBM_Kocher",
        "category": "Thời gian vàng cứu sụn",
        "front": "Tại sao Viêm khớp nhiễm khuẩn được coi là một cấp cứu ngoại khoa tối khẩn phải xử trí trong 24 giờ đầu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì enzyme tiêu protein từ mủ và áp lực nội khớp tăng cao sẽ ăn mòn và phá hủy toàn bộ sụn khớp vĩnh viễn chỉ sau 24-48 giờ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Chậm trễ tháo mủ dẫn đến tiêu chỏm xương đùi và tàn phế khớp suốt đời.",
        "extra": "Bắt buộc chọc hút tháo mủ giải áp hoặc phẫu thuật mở bao khớp rửa sạch.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Cap-cuu",
            "Co-do"
        ]
    },
    {
        "id": "PED54-EBM-009",
        "type": "cloze",
        "section": "EBM_DichKhop",
        "category": "Bạch cầu dịch khớp nhiễm khuẩn",
        "text": "Xét nghiệm dịch khớp khẳng định Viêm khớp nhiễm khuẩn khi số lượng bạch cầu thường {{c1::> 50.000/µL}} (thường > 100.000/µL) với tỷ lệ bạch cầu đa nhân trung tính (PMN) {{c1::≥ 75%}}.",
        "extra": "Dịch khớp có màu đục ngầu như mủ hoặc sữa đục, nồng độ glucose dịch khớp giảm sâu.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Xet-nghiem"
        ]
    },
    {
        "id": "PED54-EBM-010",
        "type": "cloze",
        "section": "EBM_ViKhuan",
        "category": "Căn nguyên vi khuẩn hàng đầu",
        "text": "Vi khuẩn sinh mủ hàng đầu gây Viêm khớp nhiễm khuẩn ở trẻ em trên 3 tháng tuổi là {{c1::Staphylococcus aureus (Tụ cầu vàng)}}, tiếp theo là {{c1::Streptococcus pyogenes}} và Kingella kingae.",
        "extra": "Ở trẻ vị thành niên có hoạt động tình dục, luôn cảnh giác vi khuẩn lậu Neisseria gonorrhoeae.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Vi-khuan"
        ]
    },
    {
        "id": "PED54-EBM-011",
        "type": "basic",
        "section": "EBM_ViemThoangQua",
        "category": "Viêm màng hoạt dịch thoáng qua",
        "front": "Đặc điểm phân biệt của Viêm màng hoạt dịch thoáng qua (Transient Synovitis) so với Viêm khớp nhiễm khuẩn là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Trẻ không sốt hoặc sốt nhẹ, vẫn chịu tỳ chân bước đi khập khiễng nhẹ, các chỉ số viêm (CRP, ESR, WBC) bình thường hoặc tăng nhẹ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Phản ứng viêm vô khuẩn tự giới hạn sau nhiễm virus hô hấp trên; tự khỏi sau 7-10 ngày nghỉ ngơi.",
        "extra": "Điểm Kocher thường chỉ đạt 0 hoặc 1 điểm.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-012",
        "type": "basic",
        "section": "EBM_SCFE",
        "category": "Bẫy đau chuyển vị trong SCFE",
        "front": "Tại sao trẻ vị thành niên bị Trượt đầu trên xương đùi (SCFE) lại thường chỉ than phiền đau ở khớp gối?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do hiện tượng đau chuyển vị (Referred pain) qua nhánh cảm giác của thần kinh bịt (Obturator nerve) chi phối chung cho cả khớp háng và gối.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bác sĩ chỉ khám gối thấy bình thường sẽ bỏ sót tổn thương trượt sụn tiếp hợp ở khớp háng.",
        "extra": "Quy tắc vàng: Đau gối ở thiếu niên thừa cân bắt buộc phải khám khớp háng cùng bên.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE",
            "Bay-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-013",
        "type": "cloze",
        "section": "EBM_SCFE",
        "category": "Dấu hiệu khám khớp háng trong SCFE",
        "text": "Khám khớp háng ở bệnh nhi Trượt đầu trên xương đùi (SCFE) đặc trưng bởi sự hạn chế nghiêm trọng động tác {{c1::xoay trong (Internal rotation)}} và khép đùi.",
        "extra": "Khi thụ động gập đùi vào bụng, đùi trẻ tự động bị đẩy xoay ngoài và giạng ra (Dấu hiệu Drehmann dương tính).",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE"
        ]
    },
    {
        "id": "PED54-EBM-014",
        "type": "basic",
        "section": "EBM_SCFE",
        "category": "Tư thế chụp X-quang SCFE",
        "front": "Tư thế chụp X-quang khớp háng nào là bắt buộc để không bỏ sót Trượt đầu trên xương đùi (SCFE) giai đoạn sớm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Chụp X-quang khung chậu tư thế thẳng VÀ tư thế chân ếch (Frog-leg lateral view).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Phim thẳng có thể bình thường ở giai đoạn trượt nhẹ ra sau; phim chân ếch bộc lộ rõ hình ảnh trượt đĩa sụn.",
        "extra": "Đường kẻ Klein dọc bờ trên cổ xương đùi không cắt qua mép ngoài chỏm xương đùi.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE",
            "X-quang"
        ]
    },
    {
        "id": "PED54-EBM-015",
        "type": "cloze",
        "section": "EBM_SCFE",
        "category": "Xử trí cấp cứu ban đầu SCFE",
        "text": "Ngay khi nghi ngờ Trượt đầu trên xương đùi (SCFE), hành động cấp cứu đầu tiên là {{c1::tuyệt đối cấm bệnh nhi tự bước đi tỳ chân}} và bất động chuyển viện mổ ghim nẹp in situ.",
        "extra": "Tỳ đè thêm sẽ làm trượt hoàn toàn và xé rách mạch máu nuôi gây hoại tử vô mạch chỏm xương đùi vĩnh viễn.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE",
            "Cap-cuu"
        ]
    },
    {
        "id": "PED54-EBM-016",
        "type": "basic",
        "section": "EBM_ChinhHinh",
        "category": "Bệnh Legg-Calvé-Perthes",
        "front": "Đặc điểm dịch tễ và lâm sàng điển hình của Bệnh Legg-Calvé-Perthes ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bé trai 4-8 tuổi, khởi phát âm thầm với dáng đi khập khiễng nhẹ, ít đau hoặc không đau, đau tăng nhẹ cuối ngày.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Hoại tử vô mạch tự phát chỏm xương đùi do thiếu máu nuôi tạm thời, dẫn đến xẹp và biến dạng chỏm xương đùi.",
        "extra": "Khác với SCFE (gặp ở tuổi 10-14 thừa cân béo phì), Perthes gặp ở lứa tuổi 4-8 nhỏ con.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Chinh-hinh"
        ]
    },
    {
        "id": "PED54-EBM-017",
        "type": "basic",
        "section": "EBM_ChinhHinh",
        "category": "Bệnh Osgood-Schlatter",
        "front": "Vị trí ấn đau chói cục bộ đặc trưng trong Bệnh Osgood-Schlatter nằm ở đâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tại lồi củ trước xương chày (Tibial tubercle), dưới xương bánh chè khoảng 2 cm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do lực co kéo lặp đi lặp lại của gân bánh chè vào sụn tiếp hợp lồi củ chày ở thiếu niên chơi thể thao chạy nhảy.",
        "extra": "Khớp gối hoàn toàn bình thường, không có tràn dịch màng hoạt dịch.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Chinh-hinh"
        ]
    },
    {
        "id": "PED54-EBM-018",
        "type": "cloze",
        "section": "EBM_JIA",
        "category": "Định nghĩa chuẩn JIA",
        "text": "Tiêu chuẩn chẩn đoán Viêm khớp tự phát thiếu niên (JIA) đòi hỏi viêm khớp khởi phát trước {{c1::16 tuổi}}, kéo dài liên tục tối thiểu {{c1::6 tuần}}, và đã loại trừ các nguyên nhân khác.",
        "extra": "Nếu viêm khớp dưới 6 tuần, ưu tiên tìm nguyên nhân nhiễm trùng, sau nhiễm virus hoặc phản ứng.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA",
            "Dinh-nghia"
        ]
    },
    {
        "id": "PED54-EBM-019",
        "type": "basic",
        "section": "EBM_JIA",
        "category": "JIA thể ít khớp",
        "front": "Đặc điểm lâm sàng và biến chứng nguy hiểm nhất của JIA thể ít khớp (Oligoarthritis) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Viêm ≤ 4 khớp lớn chi dưới; biến chứng nguy hiểm nhất là Viêm màng bồ đào trước mạn tính câm lặng gây mù lòa.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ có ANA(+) có nguy cơ viêm màng bồ đào cao nhất; mắt hoàn toàn không đỏ không đau nhức bên ngoài.",
        "extra": "Bắt buộc khám đèn khe (Slit-lamp) định kỳ mỗi 3-6 tháng.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA",
            "Mat"
        ]
    },
    {
        "id": "PED54-EBM-020",
        "type": "cloze",
        "section": "EBM_JIA",
        "category": "Sốt và ban trong sJIA",
        "text": "Viêm khớp thiếu niên thể hệ thống (sJIA / Bệnh Still) đặc trưng bởi cơn sốt cao hình gai nhọn xuất hiện 1-2 lần/ngày kèm theo {{c1::ban đỏ màu hồng cá hồi (salmon-pink)}} lặn nhanh theo cơn sốt.",
        "extra": "Thường kèm theo gan to, lách to, hạch to và nồng độ Ferritin máu tăng cực cao.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-021",
        "type": "basic",
        "section": "EBM_JIA",
        "category": "Biến chứng MAS trong sJIA",
        "front": "Biến chứng cấp tính đe dọa tính mạng thường gặp trong JIA thể hệ thống (sJIA) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hội chứng kích hoạt đại thực bào (Macrophage Activation Syndrome - MAS).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Cơn bão cytokine gây suy đa tạng, giảm tế bào máu 3 dòng, tụt Fibrinogen, tăng vọt Ferritin máu và rối loạn đông máu.",
        "extra": "Điều trị khẩn cấp bằng Corticoid liều xung phối hợp Cyclosporine A hoặc thuốc kháng IL-1 (Anakinra).",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA",
            "Cap-cuu"
        ]
    },
    {
        "id": "PED54-EBM-022",
        "type": "basic",
        "section": "EBM_JIA",
        "category": "JIA thể viêm điểm bám gân",
        "front": "Đặc điểm lâm sàng đặc thù của JIA thể Viêm điểm bám gân (Enthesitis-related arthritis - ERA) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Viêm khớp lớn chi dưới kèm đau ấn tại các điểm bám gân (gân gót Achilles, cân gan chân), liên quan mạnh với HLA-B27.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Thường gặp ở trẻ trai > 6 tuổi; có nguy cơ tiến triển thành Viêm cột sống dính khớp và viêm khớp cùng chậu.",
        "extra": "Đau cứng cột sống thắt lưng tăng vào buổi sáng.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-023",
        "type": "basic",
        "section": "EBM_JIA",
        "category": "Dấu hiệu Dactylitis",
        "front": "Dấu hiệu viêm ngón tay hoặc ngón chân hình khúc dồi (Dactylitis) đặc trưng cho thể bệnh nào của JIA?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thể Viêm khớp vảy nến (Psoriatic arthritis).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do phản ứng viêm đồng thời cả màng hoạt dịch khớp và bao gân gấp ngón tay/chân.",
        "extra": "Thường kèm theo dấu hiệu rỗ móng tay (Nail pitting) hoặc tiền sử gia đình có người bị vảy nến.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-024",
        "type": "basic",
        "section": "EBM_CoDoAcTinh",
        "category": "Đau xương trong Bạch cầu cấp ALL",
        "front": "Đặc điểm đau cơ xương nào ở trẻ em là cờ đỏ cảnh báo mạnh mẽ bệnh lý Bạch cầu cấp (ALL)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đau sâu trong thân xương dài, đau dữ dội về đêm đánh thức trẻ dậy khóc thét, không tương xứng với dấu hiệu viêm khớp.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tế bào lymphoblast ác tính tăng sinh ồ ạt trong tủy chèn ép và phá hủy vỏ màng xương.",
        "extra": "Kèm tam chứng suy tủy: thiếu máu xanh xao, chấm xuất huyết giảm tiểu cầu, sốt kéo dài.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Bach-cau-cap",
            "Co-do"
        ]
    },
    {
        "id": "PED54-EBM-025",
        "type": "basic",
        "section": "EBM_BayLamSang",
        "category": "Cấm dùng Corticoid mù",
        "front": "Tại sao tuyệt đối chống chỉ định dùng Corticoid (Dexamethasone/Prednisolone) để giảm đau khớp chưa rõ nguyên nhân ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì Corticoid tiêu diệt tạm thời tế bào non blast trong Bạch cầu cấp (ALL), làm biến đổi tủy đồ âm tính giả và gây kháng thuốc hóa trị sau này.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ đỡ đau khớp vài ngày nhưng sau đó bệnh ung thư bùng phát dữ dội mất thời gian vàng cứu chữa.",
        "extra": "Chỉ dùng Corticoid khi đã loại trừ hoàn toàn ALL bằng huyết đồ và tủy đồ.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Bay-lam-sang",
            "Co-do"
        ]
    },
    {
        "id": "PED54-EBM-026",
        "type": "basic",
        "section": "EBM_BayLamSang",
        "category": "Đau xương tăng trưởng",
        "front": "4 tiêu chuẩn giúp chẩn đoán đúng Đau xương phát triển lành tính (Growing pains) ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Tuổi 3-12. 2) Đau cơ bắp chân hai bên (không đau khớp). 3) Chỉ đau chiều tối/ban đêm, sáng dậy bình thường. 4) Khám ban ngày bình thường 100%.<br><b>💡 Lưu ý:</b> Nếu trẻ đau 1 bên hoặc đi khập khiễng → Tuyệt đối không được chẩn đoán đau phát triển.",
        "extra": "Trấn an phụ huynh, xoa bóp cơ nhẹ nhàng và chườm ấm.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-027",
        "type": "basic",
        "section": "EBM_BayLamSang",
        "category": "Thấp tim vs JIA",
        "front": "Đặc điểm viêm khớp nào giúp phân biệt Thấp tim cấp (Jones criteria) với Viêm khớp tự phát thiếu niên (JIA)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thấp tim: Viêm đa khớp di chuyển nhanh, đáp ứng ngoạn mục sau 24-48h dùng Aspirin/Naproxen; JIA: Viêm khớp cố định liên tục ≥ 6 tuần.<br><b>💡 Lưu ý:</b> Thấp tim thường có tăng ASO và tổn thương van tim trên siêu âm.",
        "extra": "Tham chiếu bài PED-51 (Thấp tim ở trẻ em).",
        "tags": [
            "PED-54",
            "PED-51",
            "EBM-Update",
            "Thap-tim"
        ]
    },
    {
        "id": "PED54-EBM-028",
        "type": "cloze",
        "section": "EBM_DieuTri",
        "category": "Kháng sinh đầu tay viêm khớp mủ",
        "text": "Kháng sinh tĩnh mạch đầu tay điều trị Viêm khớp nhiễm khuẩn cấp do tụ cầu nhạy cảm Methicillin (MSSA) ở trẻ > 3 tháng tuổi là {{c1::Cefazolin}} với liều {{c1::100 - 150 mg/kg/ngày}} chia 3 lần.",
        "extra": "Nếu nghi ngờ CA-MRSA (sốc, cấy mọc tụ cầu kháng thuốc), phối hợp ngay Vancomycin liều 40-60 mg/kg/ngày.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "Cap-cuu"
        ]
    },
    {
        "id": "PED54-EBM-029",
        "type": "cloze",
        "section": "EBM_DieuTri",
        "category": "Liều Naproxen trong JIA",
        "text": "Thuốc chống viêm không Steroid (NSAID) đầu tay được ưu tiên lựa chọn trong điều trị Viêm khớp tự phát thiếu niên (JIA) là {{c1::Naproxen}} với liều lượng {{c1::10 - 20 mg/kg/ngày}} chia 2 lần uống (tối đa 1000 mg/ngày).",
        "extra": "Uống ngay sau ăn no; thời gian bán hủy dài cho phép dùng 2 lần/ngày rất thuận tiện cho trẻ đi học.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-030",
        "type": "cloze",
        "section": "EBM_DieuTri",
        "category": "Methotrexate và Acid Folic trong JIA",
        "text": "Khi điều trị JIA bằng Methotrexate liều {{c1::10 - 15 mg/m²/tuần}} (uống hoặc tiêm dưới da 1 lần duy nhất mỗi tuần), bắt buộc phải bổ sung {{c1::Acid Folic 1 mg/ngày}} để dự phòng loét miệng và độc tính gan.",
        "extra": "Methotrexate là thuốc DMARD kinh điển đầu tay kiểm soát tiến triển bào mòn khớp.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-031",
        "type": "basic",
        "section": "EBM_DieuTri",
        "category": "Tiêm Corticoid nội khớp",
        "front": "Thuốc Corticoid tiêm nội khớp được khuyến cáo lựa chọn hàng đầu cho JIA thể ít khớp là thuốc gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Triamcinolone hexacetonide (hoặc Triamcinolone acetonide).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Độ tan trong dịch khớp cực thấp giúp thuốc lưu giữ và giải phóng kéo dài tại bao khớp nhiều tháng mà không ngấm vào máu gây tác dụng phụ toàn thân.",
        "extra": "Cho trẻ nghỉ ngơi bất động khớp tương đối trong 24-48 giờ sau tiêm.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-032",
        "type": "basic",
        "section": "EBM_DieuTri",
        "category": "Thuốc sinh học trong sJIA",
        "front": "Hai nhóm thuốc sinh học nào có hiệu quả điều trị đặc hiệu nhất để cắt sốt và kiểm soát JIA thể hệ thống (sJIA)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Thuốc kháng IL-1 (Anakinra, Canakinumab) và Thuốc kháng IL-6 (Tocilizumab).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>sJIA là bệnh lý tự viêm (Autoinflammatory) bùng nổ quá mức hai cytokine then chốt là IL-1 và IL-6.",
        "extra": "Thuốc sinh học kháng TNF-alpha (Adalimumab) ít hiệu quả trong thể hệ thống hơn thể đa khớp.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-033",
        "type": "cloze",
        "section": "EBM_TamSoatMat",
        "category": "Lịch khám đèn khe JIA nguy cơ rất cao",
        "text": "Trẻ mắc JIA thể ít khớp có kháng thể ANA(+) khởi phát bệnh trước 6 tuổi được xếp vào nhóm nguy cơ viêm màng bồ đào rất cao, bắt buộc phải khám mắt bằng sinh hiển vi đèn khe định kỳ {{c1::mỗi 3 tháng một lần}}.",
        "extra": "Kéo dài tối thiểu trong 4 năm đầu mắc bệnh; sau đó giãn ra mỗi 6 tháng.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Mat",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-034",
        "type": "basic",
        "section": "EBM_QuyTacVang",
        "category": "Quy tắc khám gối phải khám háng",
        "front": "Nêu quy tắc vàng số 1 khi thăm khám một đứa trẻ than phiền đau khớp gối đơn độc?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bắt buộc phải bộc lộ và khám toàn diện khớp háng cùng bên (kiểm tra biên độ xoay trong và gập đùi).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Đau khớp gối rất thường là đau chuyển vị từ khớp háng qua thần kinh bịt (gặp trong SCFE, Perthes, Viêm khớp nhiễm khuẩn).",
        "extra": "Bỏ sót khám khớp háng là nguyên nhân hàng đầu dẫn đến tàn tật do SCFE.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Quy-tac-vang"
        ]
    },
    {
        "id": "PED54-EBM-035",
        "type": "basic",
        "section": "EBM_SieuAmKhop",
        "category": "Dấu hiệu siêu âm tràn dịch khớp háng",
        "front": "Tiêu chuẩn siêu âm xác định có tràn dịch bao khớp háng ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khoảng cách bao khớp trước đo được > 5 mm hoặc dày hơn bên đối diện từ 2 mm trở lên.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Siêu âm là phương tiện không xâm nhập nhạy nhất để phát hiện dịch và hướng dẫn chọc hút chính xác.",
        "extra": "Không thể phân biệt dịch mủ hay dịch viêm vô khuẩn chỉ dựa vào siêu âm đơn thuần.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Sieu-am"
        ]
    },
    {
        "id": "PED54-EBM-036",
        "type": "cloze",
        "section": "EBM_SCFE",
        "category": "Đường kẻ Klein trên X-quang",
        "text": "Trên phim X-quang khớp háng thẳng, {{c1::đường kẻ Klein}} vẽ dọc theo bờ trên của cổ xương đùi bình thường phải cắt qua một phần chỏm xương đùi; nếu không cắt qua là dấu hiệu chỉ điểm {{c1::Trượt đầu trên xương đùi (SCFE)}}.",
        "extra": "Cần so sánh đối chiếu với khớp háng bên lành.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE",
            "X-quang"
        ]
    },
    {
        "id": "PED54-EBM-037",
        "type": "basic",
        "section": "EBM_SCFE",
        "category": "Dấu hiệu Drehmann",
        "front": "Dấu hiệu Drehmann (Drehmann sign) trong khám khớp háng biểu hiện như thế nào và đặc trưng cho bệnh gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Khi thầy thuốc thụ động gập đùi trẻ vào bụng, đùi tự động bị đẩy xoay ngoài và giạng ra; đặc trưng cho Trượt đầu trên xương đùi (SCFE).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do cổ xương đùi bị trượt chếch ra trước cấn vào bờ ổ cối khi gập thẳng trục.",
        "extra": "Chỉ điểm tổn thương sụn tiếp hợp cấp hoặc bán cấp.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "SCFE",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-038",
        "type": "basic",
        "section": "EBM_ViemMach",
        "category": "Đau khớp trong Viêm mạch Henoch-Schonlein",
        "front": "Đặc điểm tổn thương khớp trong Viêm mạch Henoch-Schonlein (HSP / IgA Vasculitis) ở trẻ em có gì đặc biệt?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sưng đau quanh khớp (chủ yếu cổ chân và gối), đau nhiều nhưng không phá hủy sụn khớp và tự thoái lui hoàn toàn không để lại di chứng.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do lắng đọng phức hợp miễn dịch IgA gây viêm mạch máu quanh bao khớp.",
        "extra": "Đi kèm ban xuất huyết dạng sẩn gồ ở hai cẳng chân và mông, đau bụng cơn và tổn thương thận.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Viem-mach"
        ]
    },
    {
        "id": "PED54-EBM-039",
        "type": "basic",
        "section": "EBM_CoChe",
        "category": "Viêm khớp phản ứng sau nhiễm khuẩn",
        "front": "Viêm khớp phản ứng (Reactive Arthritis) ở trẻ em thường khởi phát sau những loại nhiễm trùng nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Nhiễm trùng tiêu hóa (Salmonella, Shigella, Campylobacter, Yersinia). 2) Nhiễm trùng tiết niệu - sinh dục (Chlamydia).<br><b>💡 Cơ chế:</b> Phản ứng miễn dịch vô khuẩn xuất hiện sau nhiễm trùng 1-4 tuần, liên quan HLA-B27.",
        "extra": "Có thể kèm tam chứng Reiter: viêm khớp, viêm niệu đạo và viêm kết mạc.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Co-che"
        ]
    },
    {
        "id": "PED54-EBM-040",
        "type": "cloze",
        "section": "EBM_BenhLyme",
        "category": "Viêm khớp trong bệnh Lyme",
        "text": "Viêm khớp trong bệnh Lyme do xoắn khuẩn {{c1::Borrelia burgdorferi}} truyền qua ve cắn, đặc trưng bởi đợt tràn dịch khớp lớn (thường là {{c1::khớp gối}}) tái diễn, dịch rất nhiều nhưng ít đau nhức hơn viêm khớp mủ.",
        "extra": "Chẩn đoán xác định bằng xét nghiệm huyết thanh ELISA và Western blot; điều trị bằng Doxycycline hoặc Amoxicillin trong 28 ngày.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Lyme"
        ]
    },
    {
        "id": "PED54-EBM-041",
        "type": "basic",
        "section": "EBM_BenhHeThong",
        "category": "Viêm da cơ vị thành niên",
        "front": "Dấu hiệu da kinh điển nào gợi ý bệnh Viêm da cơ vị thành niên (Juvenile Dermatomyositis) ở trẻ có yếu cơ và đau khớp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Ban màu tím hoa cà quanh mí mắt kèm phù mi (Heliotrope rash) và sẩn Gottron gồ trên các khớp bàn ngón tay.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bệnh tự miễn tổn thương vi mạch ở da và cơ vân; trẻ có yếu cơ gốc chi đối xứng (khó chải đầu, khó đứng dậy từ sàn).",
        "extra": "Xét nghiệm thấy men cơ (CK, LDH, AST) tăng rất cao.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Benh-he-thong"
        ]
    },
    {
        "id": "PED54-EBM-042",
        "type": "cloze",
        "section": "EBM_JIA",
        "category": "Tiêu chuẩn xét nghiệm Ferritin trong MAS",
        "text": "Biến chứng Hội chứng kích hoạt đại thực bào (MAS) trong sJIA được gợi ý mạnh mẽ khi trẻ đột ngột tụt số lượng tiểu cầu, tụt tốc độ máu lắng ESR giả tạo và nồng độ {{c1::Ferritin máu tăng vọt (thường > 5000 - 10.000 µg/L)}}.",
        "extra": "ESR tụt do tiêu thụ cạn kiệt Fibrinogen trong cơn bão cytokine.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "JIA",
            "MAS"
        ]
    },
    {
        "id": "PED54-EBM-043",
        "type": "basic",
        "section": "EBM_ChinhHinh",
        "category": "Hội chứng đau bánh chè đùi",
        "front": "Hội chứng đau bánh chè - đùi (Patellofemoral pain syndrome) thường biểu hiện như thế nào ở trẻ vị thành niên?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đau âm ỉ quanh hoặc sau xương bánh chè ở cả hai bên, đau tăng khi đi cầu thang, ngồi xổm hoặc ngồi lâu gập gối (Dấu hiệu xem phim - Movie theater sign).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do mất cân bằng lực kéo cơ tứ đầu đùi làm trượt lệch rãnh xương bánh chè; hoàn toàn không có tràn dịch khớp.",
        "extra": "Điều trị chủ yếu bằng tập vật lý trị liệu tăng cường cơ rộng trong (VMO).",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Chinh-hinh"
        ]
    },
    {
        "id": "PED54-EBM-044",
        "type": "cloze",
        "section": "EBM_DuocLy",
        "category": "Theo dõi nồng độ Vancomycin",
        "text": "Khi sử dụng Vancomycin điều trị Viêm khớp nhiễm khuẩn nghi ngờ tụ cầu kháng thuốc (CA-MRSA), bắt buộc phải định lượng nồng độ đáy (Trough level) trong huyết thanh đạt mục tiêu {{c1::15 - 20 µg/mL}}.",
        "extra": "Lấy mẫu máu ngay trước liều thứ 4 để đảm bảo nồng độ thuốc ngấm đủ vào khoang khớp màng hoạt dịch.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly"
        ]
    },
    {
        "id": "PED54-EBM-045",
        "type": "basic",
        "section": "EBM_ViemTuyXuong",
        "category": "Viêm khớp nhiễm khuẩn vs Viêm tủy xương",
        "front": "Điểm khác biệt khi thăm khám giữa Viêm khớp nhiễm khuẩn và Viêm xương tủy xương cấp tính (Osteomyelitis) ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Viêm khớp nhiễm khuẩn: Đau và hạn chế mọi hướng xoay; Viêm tủy xương: Ấn đau chói hành xương dài, biên độ thụ động khớp còn bảo tồn.<br><b>💡 Cơ chế:</b> Trẻ &lt; 1 tuổi vi khuẩn từ hành xương có thể lan trực tiếp qua sụn tiếp hợp vào ổ khớp.",
        "extra": "Chụp MRI giúp phân định tổn thương xương và ổ dịch khớp sớm nhất.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Kham-lam-sang"
        ]
    },
    {
        "id": "PED54-EBM-046",
        "type": "basic",
        "section": "EBM_DieuTri",
        "category": "Thuốc sinh học kháng TNF",
        "front": "Tác dụng phụ nguy hiểm nào cần sàng lọc trước khi khởi trị thuốc sinh học kháng TNF-alpha (Adalimumab/Etanercept) cho trẻ mắc JIA?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Nguy cơ tái bùng phát nhiễm trùng cơ hội, đặc biệt là bệnh Lao tiềm ẩn và Viêm gan virus B.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>TNF-alpha là cytokine then chốt giúp duy trì vỏ bọc u hạt giam giữ vi khuẩn lao; ức chế TNF làm vỡ u hạt giải phóng vi khuẩn lao toàn thể.",
        "extra": "Bắt buộc làm test Mantoux (TST) hoặc IGRA và chụp X-quang phổi trước khi dùng thuốc.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Duoc-ly",
            "JIA"
        ]
    },
    {
        "id": "PED54-EBM-047",
        "type": "cloze",
        "section": "EBM_QuyTacVang",
        "category": "Quy tắc cấm chích rạch mù",
        "text": "Bác sĩ tuyệt đối {{c1::không được chích rạch mù ổ sưng khớp háng tại phòng khám}}, mọi thủ thuật chọc hút khớp háng bắt buộc phải thực hiện trong phòng thủ thuật vô trùng dưới hướng dẫn của {{c1::siêu âm hoặc màn tăng sáng C-arm}}.",
        "extra": "Tránh nguy cơ đâm vào bó mạch thần kinh đùi nằm ngay phía trước bao khớp háng.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "An-toan-thu-thuat"
        ]
    },
    {
        "id": "PED54-EBM-048",
        "type": "basic",
        "section": "EBM_QuyTacVang",
        "category": "Hội chứng chèn ép khoang",
        "front": "Dấu hiệu lâm sàng nhạy nhất báo động sớm Hội chứng chèn ép khoang (Compartment syndrome) sau chấn thương chi là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đau buốt dữ dội không tương xứng với mức độ tổn thương bên ngoài, đau tăng vọt khi kéo căng cơ thụ động.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Áp lực mô trong khoang cân tăng cao làm thiếu máu cục bộ cơ và dây thần kinh; mất mạch ngoại vi là dấu hiệu quá muộn.",
        "extra": "Cấp cứu ngoại khoa: rạch mở cân giải áp khẩn cấp trong 6 giờ đầu.",
        "tags": [
            "PED-54",
            "EBM-Update",
            "Cap-cuu",
            "Co-do"
        ]
    }
]
