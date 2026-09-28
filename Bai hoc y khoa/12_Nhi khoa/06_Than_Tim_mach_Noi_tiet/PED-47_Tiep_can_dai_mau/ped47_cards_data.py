# -*- coding: utf-8 -*-
"""PED-47 MASTER deck cards data: Track 1 barem YTB + Track 2 EBM.
Fields: id, track (barem_goc|ebm), type (basic|cloze), category, section,
front/back (basic) or text (cloze), extra, tags.
Section codes B0-B6 (PEDYTB) + E0-E7 (RELEASE lesson). Coverage gate requires >=1 card per section.
"""
cards_data = [
    # =========================================================================
    # TRACK 1: BAREM GOC Y THAI BINH — B0 MUC TIEU
    # =========================================================================
    {
        "id": "PED47-B01",
        "track": "barem_goc",
        "type": "basic",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "front": "4 mục tiêu của bài Đái máu theo giáo trình Nhi Thái Bình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Định nghĩa, cơ chế; 2) Nguyên nhân; 3) Lâm sàng, cận lâm sàng; 4) Cách tiếp cận bệnh nhân đái máu.<br><br><b>💡 Lưu ý:</b><br>Đi thi tự luận bám đúng 4 mục tiêu này để đạt trọn điểm.",
        "extra": "Văn bản gốc: MỤC TIÊU 1-4 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Muc-tieu"]
    },
    {
        "id": "PED47-B02",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Mục tiêu bài học",
        "section": "B0",
        "text": "[Barem gốc] Bài Đái máu gồm 4 mục tiêu: định nghĩa & cơ chế, {{c1::nguyên nhân}}, lâm sàng & cận lâm sàng, và {{c1::cách tiếp cận bệnh nhân đái máu}}.",
        "extra": "Văn bản gốc: MỤC TIÊU (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Muc-tieu"]
    },

    # =========================================================================
    # TRACK 1: B1 DINH NGHIA DAI MAU
    # =========================================================================
    {
        "id": "PED47-B03",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Định nghĩa",
        "section": "B1",
        "text": "[Barem gốc] Đái máu là hiện tượng có {{c1::máu hay hồng cầu}} trong nước tiểu, có thể biểu hiện dưới dạng đại thể hoặc vi thể.",
        "extra": "Văn bản gốc mục 1 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Dinh-nghia"]
    },
    {
        "id": "PED47-B04",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Định nghĩa",
        "section": "B1",
        "text": "[Barem gốc] Đái máu đại thể là hiện tượng nước tiểu có hồng cầu làm biến đổi màu sắc, phát hiện được bằng {{c1::mắt thường}}.",
        "extra": "Văn bản gốc mục 1 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Dinh-nghia"]
    },
    {
        "id": "PED47-B05",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Định nghĩa",
        "section": "B1",
        "text": "[Barem gốc] Đái máu vi thể được xác định bằng soi kính hiển vi, khi soi nước tiểu tươi giữa dòng có {{c1::≥ 5 hồng cầu/ml}}.",
        "extra": "Văn bản gốc mục 1 (trang 18); tiêu chuẩn trên nước tiểu tươi không ly tâm.",
        "tags": ["PED-47", "Barem-goc", "Dinh-nghia"]
    },
    {
        "id": "PED47-B06",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Định nghĩa",
        "section": "B1",
        "text": "[Barem gốc] Đái máu vi thể xác định khi có {{c1::trên 3 hồng cầu/vi trường}} trong mẫu quay ly tâm 10 ml nước tiểu tươi lấy giữa dòng.",
        "extra": "Văn bản gốc mục 1 (trang 18); tiêu chuẩn trên mẫu ly tâm 10 ml.",
        "tags": ["PED-47", "Barem-goc", "Dinh-nghia"]
    },

    # =========================================================================
    # TRACK 1: B2 CO CHE HONG CAU TRONG NUOC TIEU
    # =========================================================================
    {
        "id": "PED47-B07",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Cơ chế cầu thận",
        "section": "B2",
        "text": "[Barem gốc] Cơ chế đái máu tại cầu thận: do tổn thương {{c1::màng đáy cầu thận}}, làm các lỗ lọc rộng hơn và tăng {{c1::tính thấm thành mạch}}.",
        "extra": "Văn bản gốc mục 2 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Co-che"]
    },
    {
        "id": "PED47-B08",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Cơ chế ngoài cầu thận",
        "section": "B2",
        "text": "[Barem gốc] Trong đái máu ngoài cầu thận, do hồng cầu vào nước tiểu trực tiếp không qua lỗ màng đáy nên hồng cầu vẫn {{c1::giữ nguyên hình dạng và kích thước}} như máu ngoại vi.",
        "extra": "Văn bản gốc mục 2 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Co-che"]
    },
    {
        "id": "PED47-B09",
        "track": "barem_goc",
        "type": "basic",
        "category": "Cơ chế thành mạch",
        "section": "B2",
        "front": "Vì sao trẻ nhỏ dễ bị tổn thương vỡ mạch máu đường tiết niệu gây đái máu ngoài cầu thận theo sách?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì ở trẻ nhỏ cấu trúc thành mạch chưa bền vững và tính thấm thành mạch cao, dễ vỡ khi gặp tác nhân lý hóa quá mức.<br><br><b>💡 Cơ chế:</b><br>Mạch máu vỡ ở niệu quản, bàng quang, đài bể thận đưa hồng cầu trực tiếp vào nước tiểu.",
        "extra": "Văn bản gốc mục 2 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Co-che"]
    },

    # =========================================================================
    # TRACK 1: B3 NGUYEN NHAN GAY DAI MAU
    # =========================================================================
    {
        "id": "PED47-B10",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Nguyên nhân cầu thận",
        "section": "B3",
        "text": "[Barem gốc] Bệnh đái máu lành tính có tính chất gia đình do tổn thương cầu thận trong giáo trình in nhầm là bệnh {{c1::móng màng đáy}} (đúng là màng đáy mỏng).",
        "extra": "Văn bản gốc bảng mục 3 (trang 18); lỗi in ấn cần lưu ý khi thi tự luận.",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },
    {
        "id": "PED47-B11",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Nguyên nhân cầu thận",
        "section": "B3",
        "text": "[Barem gốc] Các nguyên nhân đái máu tại cầu thận trong sách: đái máu lành tính gia đình, viêm cầu thận cấp sau nhiễm trùng, {{c1::viêm cầu thận tăng sinh màng}}, viêm cầu thận tiến triển nhanh, {{c1::bệnh thận IgA}}.",
        "extra": "Văn bản gốc bảng mục 3 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },
    {
        "id": "PED47-B12",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Nguyên nhân cầu thận",
        "section": "B3",
        "text": "[Barem gốc] Các bệnh hệ thống và di truyền gây đái máu tại cầu thận gồm: viêm thận Schonlein-Henoch, viêm thận Lupus, hội chứng HUS và {{c1::hội chứng Alport}}.",
        "extra": "Văn bản gốc bảng mục 3 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },
    {
        "id": "PED47-B13",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Nguyên nhân ngoài cầu thận",
        "section": "B3",
        "text": "[Barem gốc] Các nguyên nhân ngoài cầu thận thường gặp theo sách: nhiễm trùng tiết niệu, {{c1::tăng canxi niệu}}, sỏi thận, chấn thương và do {{c1::tập thể dục}}.",
        "extra": "Văn bản gốc bảng mục 3 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },
    {
        "id": "PED47-B14",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Nguyên nhân khối u",
        "section": "B3",
        "text": "[Barem gốc] Khối u ác tính ngoài cầu thận gây đái máu thường gặp nhất ở trẻ em trong bảng nguyên nhân là {{c1::u nguyên bào thận (Wilms)}}.",
        "extra": "Văn bản gốc bảng mục 3 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },
    {
        "id": "PED47-B15",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Bất thường mạch máu",
        "section": "B3",
        "text": "[Barem gốc] Dị tật chèn ép mạch máu gây đái máu ngoài cầu thận được liệt kê trong bảng nguyên nhân là {{c1::hội chứng Nutcracker}}.",
        "extra": "Văn bản gốc bảng mục 3 (trang 18).",
        "tags": ["PED-47", "Barem-goc", "Nguyen-nhan"]
    },

    # =========================================================================
    # TRACK 1: B4 DAC DIEM LAM SANG
    # =========================================================================
    {
        "id": "PED47-B16",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Màu sắc nước tiểu",
        "section": "B4",
        "text": "[Barem gốc] Nước tiểu đái máu đại thể có thể màu đỏ như nước rửa thịt, màu {{c1::coca-cola}}, hoặc sẫm như nước chè; để lâu sẽ có {{c1::lắng cặn hồng cầu}}.",
        "extra": "Văn bản gốc mục 4 (trang 19-20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B17",
        "track": "barem_goc",
        "type": "basic",
        "category": "Nghiệm pháp 3 cốc",
        "section": "B4",
        "front": "Cách phân định vị trí đái máu đại thể bằng nghiệm pháp 3 cốc theo giáo trình?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đái máu đầu bãi: niệu đạo; đái máu cuối bãi: bàng quang; đái máu toàn bãi: viêm cầu thận, niệu quản, bàng quang hoặc bệnh về máu.<br><br><b>💡 Lưu ý:</b><br>Đái máu đỏ tươi, có máu cục gợi ý nguyên nhân ngoài cầu thận.",
        "extra": "Văn bản gốc mục 4 Đái máu (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B18",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Tính chất đái máu",
        "section": "B4",
        "text": "[Barem gốc] Đái máu đại thể có tính chất đỏ tươi và có {{c1::máu cục}} gợi ý nguyên nhân chảy máu từ {{c1::đường tiết niệu (ngoài cầu thận)}}.",
        "extra": "Văn bản gốc mục 4 Đái máu (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B19",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Đặc điểm phù",
        "section": "B4",
        "text": "[Barem gốc] Phù trong bệnh lý cầu thận thường có tính chất là phù {{c1::trắng, phù mềm, ấn lõm}}.",
        "extra": "Văn bản gốc mục 4 Phù (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B20",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Đánh giá mức độ phù",
        "section": "B4",
        "text": "[Barem gốc] Phân độ mức độ phù theo cân nặng cơ thể: phù nhẹ tăng cân &lt; {{c1::10%}}, phù vừa tăng từ {{c1::10–20%}}, phù nặng tăng &gt; {{c1::20%}}.",
        "extra": "Văn bản gốc mục 4 Phù (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B21",
        "track": "barem_goc",
        "type": "basic",
        "category": "Đặc điểm đau khớp",
        "section": "B4",
        "front": "Đặc điểm tổn thương khớp trong đái máu do Lupus ban đỏ theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đau nhiều khớp nhỏ các chi, chuyển từ khớp này sang khớp khác, không cứng khớp buổi sáng, không sưng nóng đỏ đau và không biến dạng khớp.<br><br><b>💡 Lưu ý:</b><br>Khác với viêm khớp dạng thấp (cứng khớp sáng, sưng nóng biến dạng).",
        "extra": "Văn bản gốc mục 4 Đau khớp (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B22",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Ban Schonlein-Henoch",
        "section": "B4",
        "text": "[Barem gốc] Đái máu kèm xuất huyết cẳng chân dạng {{c1::đi bốt}} nghĩ nhiều nhất đến bệnh {{c1::Schonlein-Henoch}}.",
        "extra": "Văn bản gốc mục 4 Xuất huyết da, niêm (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B23",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hồng ban Lupus",
        "section": "B4",
        "text": "[Barem gốc] Đái máu kèm {{c1::ban cánh bướm}} ở mặt khu trú hai gò má cánh mũi, ban hình đĩa, nhạy cảm ánh sáng, loét miệng họng là dấu hiệu của {{c1::Lupus ban đỏ}}.",
        "extra": "Văn bản gốc mục 4 Hồng ban (trang 20).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B24",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Đau bụng & tiết niệu",
        "section": "B4",
        "text": "[Barem gốc] Đái máu kèm đau vùng mạng sườn quặn thắt nghĩ nhiều đến {{c1::sỏi niệu quản, thận ứ nước}} hoặc tắc nghẽn đường tiểu.",
        "extra": "Văn bản gốc mục 4 Đau bụng (trang 20-21).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },
    {
        "id": "PED47-B25",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Đái máu kèm sốt",
        "section": "B4",
        "text": "[Barem gốc] Đái máu đại thể tái phát kết hợp với nhiễm trùng đường hô hấp trên thường là: {{c1::Bệnh thận do IgA}}, {{c1::Bệnh màng đáy mỏng}} hay {{c1::Hội chứng Alport}}.",
        "extra": "Văn bản gốc mục 4 Sốt (trang 21).",
        "tags": ["PED-47", "Barem-goc", "Lam-sang"]
    },

    # =========================================================================
    # TRACK 1: B5 CAN LAM SANG & CHI DINH SINH THIET THAN
    # =========================================================================
    {
        "id": "PED47-B26",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Cặn nước tiểu",
        "section": "B5",
        "text": "[Barem gốc] Trong xét nghiệm nước tiểu, sự xuất hiện của {{c1::trụ hồng cầu}} là bằng chứng chắc chắn tổn thương tại cầu thận.",
        "extra": "Văn bản gốc mục 5.1 Xét nghiệm nước tiểu (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Can-lam-sang"]
    },
    {
        "id": "PED47-B27",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Hình dáng hồng cầu",
        "section": "B5",
        "text": "[Barem gốc] Soi hình dáng hồng cầu niệu giúp định vị: hồng cầu biến dạng gặp trong tổn thương tại {{c1::cầu thận}}, hồng cầu đồng dạng gặp trong tổn thương {{c1::ngoài cầu thận}}.",
        "extra": "Văn bản gốc mục 5.1 (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Can-lam-sang"]
    },
    {
        "id": "PED47-B28",
        "track": "barem_goc",
        "type": "basic",
        "category": "Xét nghiệm máu",
        "section": "B5",
        "front": "Kể tên các xét nghiệm miễn dịch máu cần làm theo sách khi nghi ngờ đái máu do tổn thương cầu thận?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>ASLO, Bổ thể C3, C4; định lượng IgA; kháng thể ANA và Anti-dsDNA nếu nghi Lupus ban đỏ.<br><br><b>💡 Lưu ý:</b><br>Phối hợp Ure, Creatinin, điện giải đồ và đông máu toàn bộ.",
        "extra": "Văn bản gốc mục 5.2 Xét nghiệm máu (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Can-lam-sang"]
    },
    {
        "id": "PED47-B29",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 1: Khi protein niệu &gt; {{c1::1 g/1,73 m²/ngày}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B30",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 2: Khi bổ thể C3 thấp kéo dài trên {{c1::3 tháng}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B31",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 3: Khi mức lọc cầu thận giảm &lt; {{c1::80 ml/phút/1,73 m²}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B32",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 4: Chỉ định trên bệnh nhân nghi ngờ {{c1::viêm thận Lupus}} hoặc {{c1::viêm thận Schonlein-Henoch}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B33",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 5: Tiền sử gia đình có bệnh thận nghi ngờ {{c1::hội chứng Alport}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B34",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 6: Đái máu đại thể {{c1::tái phát mà không rõ nguyên nhân}}.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-B35",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "section": "B5",
        "text": "[Barem gốc] Chỉ định sinh thiết thận 7: Đái máu do cầu thận mà {{c1::gia đình thiết tha muốn biết nguyên nhân}} và tiên lượng của bệnh mặc dù protein niệu không cao.",
        "extra": "Văn bản gốc mục 5.4 Chỉ định Sinh thiết thận (trang 22).",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than"]
    },

    # =========================================================================
    # TRACK 1: B6 CACH TIEP CAN BENH NHAN DAI MAU (5 BUOC)
    # =========================================================================
    {
        "id": "PED47-B36",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thuật toán Bước 1",
        "section": "B6",
        "front": "Bước 1 trong sơ đồ tiếp cận đái máu của giáo trình là gì và phân loại kết quả như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Que thử (Dipstick) + Soi kính hiển vi: Que thử (+) soi tươi (-) → tìm Hemoglobin hoặc Myoglobin niệu; Que thử (+) soi tươi (+) → đái máu thực sự (chuyển Bước 2).<br><br><b>💡 Lưu ý:</b><br>Tránh nhầm sắc tố tự do với tế bào hồng cầu.",
        "extra": "Văn bản gốc mục 6 Sơ đồ thuật toán Bước 1 (trang 23).",
        "tags": ["PED-47", "Barem-goc", "Tiep-can"]
    },
    {
        "id": "PED47-B37",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thuật toán Bước 2",
        "section": "B6",
        "text": "[Barem gốc] Bước 2 thuật toán tiếp cận: Tìm dấu hiệu viêm cầu thận cấp gồm tam chứng: {{c1::phù, tăng huyết áp, đái ít}}.",
        "extra": "Văn bản gốc mục 6 Sơ đồ thuật toán Bước 2 (trang 23).",
        "tags": ["PED-47", "Barem-goc", "Tiep-can"]
    },
    {
        "id": "PED47-B38",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thuật toán Bước 3",
        "section": "B6",
        "text": "[Barem gốc] Bước 3 thuật toán: Phân loại lâm sàng: đái máu đại thể loại trừ {{c1::gắng sức thể dục}}; đái máu vi thể đơn độc làm lại nước tiểu hàng tuần trong {{c1::2 tuần}} (không tập thể dục).",
        "extra": "Văn bản gốc mục 6 Sơ đồ thuật toán Bước 3 (trang 23).",
        "tags": ["PED-47", "Barem-goc", "Tiep-can"]
    },
    {
        "id": "PED47-B39",
        "track": "barem_goc",
        "type": "cloze",
        "category": "Thuật toán Bước 4",
        "section": "B6",
        "text": "[Barem gốc] Bước 4 thuật toán: Xác định nguyên nhân tại cầu thận khi có hồng cầu biến đổi hình thái &gt; {{c1::80%}}, kèm theo {{c1::protein niệu (+)}} và {{c1::trụ hồng cầu (+)}}.",
        "extra": "Văn bản gốc mục 6 Sơ đồ thuật toán Bước 4 (trang 23).",
        "tags": ["PED-47", "Barem-goc", "Tiep-can"]
    },
    {
        "id": "PED47-B40",
        "track": "barem_goc",
        "type": "basic",
        "category": "Thuật toán Bước 5",
        "section": "B6",
        "front": "Bước 5 thuật toán: Các xét nghiệm tìm nguyên nhân ngoài cầu thận theo giáo trình là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tỷ lệ Canxi/Creatinine niệu, cấy nước tiểu (vi khuẩn, Adenovirus), siêu âm Doppler mạch thận, đông máu toàn bộ, X-quang KUB, CT ổ bụng.<br><br><b>💡 Lưu ý:</b><br>Nếu tất cả bình thường kết luận đái máu thoáng qua và theo dõi định kỳ hàng năm.",
        "extra": "Văn bản gốc mục 6 Sơ đồ thuật toán Bước 5 (trang 23).",
        "tags": ["PED-47", "Barem-goc", "Tiep-can"]
    },

    # =========================================================================
    # TRACK 2: EBM HIEN DAI — E0 TONG QUAN CỐT LÕI
    # =========================================================================
    {
        "id": "PED47-E01",
        "track": "ebm",
        "type": "cloze",
        "category": "Ngưỡng đổi màu",
        "section": "E0",
        "text": "[EBM] Đái máu đại thể xảy ra khi chỉ cần {{c1::1 mL}} máu toàn phần hòa tan trong {{c1::1 lít}} nước tiểu đã đủ làm nước tiểu đổi màu mắt thường nhìn thấy.",
        "extra": "Nelson Textbook of Pediatrics 21st Ch.538.",
        "tags": ["PED-47", "EBM", "Tong-quan"]
    },
    {
        "id": "PED47-E02",
        "track": "ebm",
        "type": "basic",
        "category": "Định nghĩa EBM",
        "section": "E0",
        "front": "Tiêu chuẩn chẩn đoán đái máu vi thể chuẩn EBM quốc tế là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>> 3 hồng cầu/vi trường (HPF 400×) trên cặn ly tâm 10 mL nước tiểu HOẶC ≥ 5 hồng cầu/mL soi tươi, trên ít nhất 2–3 mẫu độc lập cách nhau 1–2 tuần.<br><br><b>💡 Cơ chế:</b><br>Một mẫu đơn độc có thể chỉ là đái máu thoáng qua do sốt cao hoặc vận động.",
        "extra": "Nelson 21st Ch.538 + Feld 1997.",
        "tags": ["PED-47", "EBM", "Dinh-nghia"]
    },
    {
        "id": "PED47-E03",
        "track": "ebm",
        "type": "basic",
        "category": "Màu sắc nước tiểu",
        "section": "E0",
        "front": "Vì sao đái máu nguồn gốc cầu thận có màu nước coca-cola hoặc nước rửa thịt mà không đỏ tươi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do Hemoglobin bị oxy hóa thành Methemoglobin trong môi trường toan và thẩm thấu ưu trương của lòng ống lượn thận.<br><br><b>💡 Cơ chế:</b><br>Máu ngoài cầu thận chảy trực tiếp từ đường niệu chưa bị toan hóa nên giữ màu đỏ tươi.",
        "extra": "Sinh lý bệnh nước tiểu toan hóa trong ống thận.",
        "tags": ["PED-47", "EBM", "Mau-sac"]
    },
    {
        "id": "PED47-E04",
        "track": "ebm",
        "type": "basic",
        "category": "Cục máu đông",
        "section": "E0",
        "front": "Vì sao đái máu cầu thận KHÔNG BAO GIỜ hình thành cục máu đông (clots)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do tế bào biểu mô cầu thận và ống thận tiết enzyme tiêu sợi huyết Urokinase phá hủy fibrin ngay lập tức.<br><br><b>💡 Lâm sàng:</b><br>Thấy máu cục = chắc chắn tổn thương đường dẫn niệu ngoài cầu thận.",
        "extra": "Enzyme Urokinase nội sinh tại cầu thận và ống thận.",
        "tags": ["PED-47", "EBM", "Mau-cuc"]
    },

    # =========================================================================
    # TRACK 2: E1 SÀNG LỌC ĐÁI MÁU THỰC SỰ & CỜ ĐỎ
    # =========================================================================
    {
        "id": "PED47-E05",
        "track": "ebm",
        "type": "cloze",
        "category": "Nguyên lý Dipstick",
        "section": "E1",
        "text": "[EBM] Que thử Dipstick phát hiện đái máu qua hoạt tính {{c1::Heme Peroxidase}}, nên sẽ dương tính giả với cả {{c1::Hemoglobin tự do}} (tán huyết) và {{c1::Myoglobin}} (tiêu cơ vân).",
        "extra": "Phản ứng peroxidase nhân Heme xúc tác chất oxy hóa đổi màu que thử.",
        "tags": ["PED-47", "EBM", "Dipstick"]
    },
    {
        "id": "PED47-E06",
        "track": "ebm",
        "type": "basic",
        "category": "Hemoglobin vs Myoglobin",
        "section": "E1",
        "front": "Cách phân biệt nhanh giữa Hemoglobin niệu (tán huyết) và Myoglobin niệu (tiêu cơ vân)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Quan sát huyết tương sau ly tâm máu: huyết tương màu hồng/đỏ là Hemoglobin niệu (Haptoglobin bão hòa); huyết tương trong suốt là Myoglobin niệu (đào thải cực nhanh).<br><br><b>💡 Lâm sàng:</b><br>Tiêu cơ vân có CK tăng vọt, nguy cơ hoại tử ống thận cấp.",
        "extra": "Động học gắn Haptoglobin huyết tương.",
        "tags": ["PED-47", "EBM", "Phan-biet"]
    },
    {
        "id": "PED47-E07",
        "track": "ebm",
        "type": "cloze",
        "category": "Nước tiểu đỏ giả",
        "section": "E1",
        "text": "[EBM] Nước tiểu màu đỏ nhưng Dipstick (-) và Soi (-) do thực phẩm ({{c1::củ dền, thanh long đỏ}}) hoặc chuyển hóa thuốc ({{c1::Rifampicin, Metronidazole, Sulfamethoxazole}}).",
        "extra": "Nelson 21st Ch.538 Table 538.1.",
        "tags": ["PED-47", "EBM", "Dai-mau-gia"]
    },
    {
        "id": "PED47-E08",
        "track": "ebm",
        "type": "basic",
        "category": "Cờ đỏ RPGN",
        "section": "E1",
        "front": "Viêm cầu thận tiến triển nhanh (RPGN): tam chứng cảnh báo và cơ chế mô học là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Đái máu + Thiểu niệu/vô niệu + Creatinine tăng gấp đôi trong vài ngày/tuần. Cơ chế: Hoại tử mao mạch cầu thận và tăng sinh liềm tế bào (crescent) bóp nghẹt nang Bowman.<br><br><b>💡 Xử trí:</b><br>Cấp cứu thận học: Pulse Methylprednisolone liều cao ± lọc máu/thay huyết tương ngay.",
        "extra": "KDIGO 2021 Glomerular Diseases.",
        "tags": ["PED-47", "EBM", "RPGN"]
    },

    # =========================================================================
    # TRACK 2: E2 PHÂN BIỆT CẦU THẬN VS NGOÀI CẦU THẬN
    # =========================================================================
    {
        "id": "PED47-E09",
        "track": "ebm",
        "type": "cloze",
        "category": "Hình thái hồng cầu",
        "section": "E2",
        "text": "[EBM] Trong đái máu cầu thận, tế bào {{c1::Acanthocyte}} (hồng cầu hình nhẫn có chồi bọng) với tỷ lệ &gt; {{c1::5%}} là tiêu chuẩn hình thái có độ đặc hiệu cao nhất cho tổn thương cầu thận.",
        "extra": "Độ đặc hiệu > 98% cho viêm cầu thận (Nelson 21st Ch.538).",
        "tags": ["PED-47", "EBM", "Acanthocyte"]
    },
    {
        "id": "PED47-E10",
        "track": "ebm",
        "type": "basic",
        "category": "Cơ chế biến dạng",
        "section": "E2",
        "front": "Tại sao hồng cầu từ cầu thận lại bị biến dạng đa hình thái (dysmorphic)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do hồng cầu bị ép cơ học khi chui qua lỗ màng đáy cầu thận bị rách, cộng với áp suất thẩm thấu và pH thay đổi liên tục dọc ống thận.<br><br><b>💡 Cơ chế:</b><br>Hồng cầu ngoài cầu thận chảy thẳng vào đường niệu nên giữ nguyên hình đĩa lõm 2 mặt (isomorphic).",
        "extra": "Cơ chế biến dạng hồng cầu cầu thận.",
        "tags": ["PED-47", "EBM", "Co-che"]
    },
    {
        "id": "PED47-E11",
        "track": "ebm",
        "type": "basic",
        "category": "Trụ hồng cầu",
        "section": "E2",
        "front": "Bản chất sinh lý bệnh của Trụ hồng cầu (RBC Casts) và ý nghĩa lâm sàng là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hình thành do hồng cầu kết tụ với glycoprotein Tamm-Horsfall (uromodulin) trong lòng ống lượn xa và ống góp. Độ đặc hiệu 100% cho viêm cầu thận.<br><br><b>💡 Lưu ý:</b><br>Trụ hồng cầu rất dễ vỡ, phải soi ngay trên mẫu nước tiểu mới lấy, ly tâm nhẹ.",
        "extra": "Protein Tamm-Horsfall làm khuôn tạo trụ ống thận.",
        "tags": ["PED-47", "EBM", "Tru-hong-cau"]
    },
    {
        "id": "PED47-E12",
        "track": "ebm",
        "type": "cloze",
        "category": "Protein niệu phân biệt",
        "section": "E2",
        "text": "[EBM] Phân biệt protein niệu đi kèm: Đái máu cầu thận thường có tỷ lệ Protein/Creatinine niệu (UPr/UCr) &gt; {{c1::0,2 mg/mg}}; đái máu ngoài cầu thận thường có UPr/UCr &lt; {{c1::0,2 mg/mg}}.",
        "extra": "Tỷ lệ protein niệu/creatinine niệu ngẫu nhiên.",
        "tags": ["PED-47", "EBM", "Protein-nieu"]
    },

    # =========================================================================
    # TRACK 2: E3 NGUYÊN NHÂN ĐÁI MÁU CHI TIẾT
    # =========================================================================
    {
        "id": "PED47-E13",
        "track": "ebm",
        "type": "basic",
        "category": "Thời gian tiềm tàng APSGN",
        "section": "E3",
        "front": "Thời gian tiềm tàng (latent period) từ khi nhiễm liên cầu đến khi đái máu trong APSGN là bao lâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sau viêm họng liên cầu: 1–3 tuần (trung bình 10 ngày); sau nhiễm trùng da (chốc lở): 3–6 tuần (trung bình 3 tuần).<br><br><b>💡 Cơ chế:</b><br>Cần thời gian để cơ thể sinh kháng thể và tạo phức hợp miễn dịch lắng đọng cầu thận.",
        "extra": "Nelson 21st Ch.539 Glomerulonephritis.",
        "tags": ["PED-47", "EBM", "APSGN"]
    },
    {
        "id": "PED47-E14",
        "track": "ebm",
        "type": "cloze",
        "category": "Kháng thể APSGN",
        "section": "E3",
        "text": "[EBM] Trong APSGN, kháng thể {{c1::ASLO}} tăng chủ yếu sau viêm họng, trong khi kháng thể {{c1::Anti-DNase B}} có độ nhạy rất cao sau cả viêm họng và nhiễm trùng ngoài da.",
        "extra": "Anti-DNase B có giá trị nhất trong viêm cầu thận sau chốc lở.",
        "tags": ["PED-47", "EBM", "APSGN"]
    },
    {
        "id": "PED47-E15",
        "track": "ebm",
        "type": "basic",
        "category": "Động học C3 trong APSGN",
        "section": "E3",
        "front": "Động học bổ thể C3 trong Viêm cầu thận cấp hậu liên cầu (APSGN) và cạm bẫy lâm sàng là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>C3 giảm sâu trong đợt cấp và bắt buộc hồi phục về bình thường sau 6–8 tuần. Nếu C3 giảm kéo dài quá 8–12 tuần, bắt buộc sinh thiết thận vì nghi ngờ MPGN hoặc Lupus.<br><br><b>💡 Cơ chế:</b><br>APSGN hoạt hóa con đường bổ thể nhánh thay thế (alternative pathway).",
        "extra": "Động học C3 là tiêu chuẩn theo dõi bắt buộc trong APSGN.",
        "tags": ["PED-47", "EBM", "APSGN", "C3"]
    },
    {
        "id": "PED47-E16",
        "track": "ebm",
        "type": "basic",
        "category": "IgA vs APSGN",
        "section": "E3",
        "front": "Phân biệt đái máu đại thể trong Bệnh thận IgA với APSGN dựa vào mốc thời gian và bổ thể C3?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>IgA bùng phát ngay trong 1–2 ngày đầu viêm họng (synpharyngitic) và C3 bình thường; APSGN xuất hiện sau 1–3 tuần và C3 giảm sâu.<br><br><b>💡 Bí quyết:</b><br>'Đồng hành cùng sốt họng = IgA; đi sau 1–3 tuần = APSGN'.",
        "extra": "Cặp bệnh cầu thận thường gặp nhất ở trẻ em.",
        "tags": ["PED-47", "EBM", "IgA-vs-APSGN"]
    },
    {
        "id": "PED47-E17",
        "track": "ebm",
        "type": "cloze",
        "category": "Cơ chế bệnh thận IgA",
        "section": "E3",
        "text": "[EBM] Bệnh thận IgA đặc trưng bởi sự lắng đọng phức hợp miễn dịch chứa {{c1::IgA1 khiếm khuyết galactose}} tại vùng {{c1::gian mạch (mesangium)}} cầu thận.",
        "extra": "Lắng đọng Gd-IgA1 kích hoạt phản ứng tự kháng thể IgG chống IgA1.",
        "tags": ["PED-47", "EBM", "IgA"]
    },
    {
        "id": "PED47-E18",
        "track": "ebm",
        "type": "cloze",
        "category": "Tứ chứng Schonlein-Henoch",
        "section": "E3",
        "text": "[EBM] Tứ chứng kinh điển của Viêm mạch Schonlein-Henoch (HSPN): ban xuất huyết gồ hai cẳng chân/mông, {{c1::đau/viêm khớp}}, {{c1::đau bụng/xuất huyết tiêu hóa}} và {{c1::tổn thương thận (đái máu, protein niệu)}}.",
        "extra": "Viêm mạch vi mạch qua trung gian IgA toàn thân.",
        "tags": ["PED-47", "EBM", "HSPN"]
    },
    {
        "id": "PED47-E19",
        "track": "ebm",
        "type": "basic",
        "category": "Bệnh màng đáy mỏng",
        "section": "E3",
        "front": "Bệnh màng đáy mỏng (Thin Basement Membrane Disease): cơ chế di truyền và tiên lượng lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Di truyền trội trên NST thường do đột biến gen COL4A3/COL4A4; tiên lượng lành tính tuyệt đối, protein niệu (-), huyết áp và chức năng thận bình thường suốt đời.<br><br><b>💡 Chẩn đoán:</b><br>Soi nước tiểu bố hoặc mẹ thấy đái máu vi thể tương tự không triệu chứng.",
        "extra": "Benign Familial Hematuria - không có chỉ định sinh thiết thận nếu điển hình.",
        "tags": ["PED-47", "EBM", "Mang-day-mong"]
    },
    {
        "id": "PED47-E20",
        "track": "ebm",
        "type": "basic",
        "category": "Hội chứng Alport",
        "section": "E3",
        "front": "Tam chứng kinh điển của Hội chứng Alport là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Đái máu tiến triển kèm suy thận mạn (nặng ở trẻ trai, đột biến COL4A5 trên NST X); 2) Điếc tiếp nhận thần kinh tần số cao; 3) Tổn thương mắt (thể thủy tinh hình nón trước).<br><br><b>💡 Cơ chế:</b><br>Đột biến collagen type IV làm màng đáy cầu thận bị xé rách và xơ hóa dần.",
        "extra": "Nelson 21st Ch.538.5 Alport Syndrome.",
        "tags": ["PED-47", "EBM", "Alport"]
    },
    {
        "id": "PED47-E21",
        "track": "ebm",
        "type": "cloze",
        "category": "Tăng canxi niệu vô căn",
        "section": "E3",
        "text": "[EBM] Tiêu chuẩn chẩn đoán Tăng canxi niệu vô căn ở trẻ &gt; 2 tuổi: tỷ lệ Canxi/Creatinine nước tiểu ngẫu nhiên (UCa/UCr) &gt; {{c1::0,2 mg/mg}} hoặc Canxi niệu 24h &gt; {{c1::4 mg/kg/ngày}}.",
        "extra": "Nguyên nhân ngoài cầu thận không triệu chứng phổ biến nhất ở trẻ em.",
        "tags": ["PED-47", "EBM", "Tang-canxi-nieu"]
    },
    {
        "id": "PED47-E22",
        "track": "ebm",
        "type": "basic",
        "category": "Hội chứng Nutcracker",
        "section": "E3",
        "front": "Cơ chế bệnh sinh và lâm sàng của Hội chứng Nutcracker (kẹp tĩnh mạch thận) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tĩnh mạch thận trái bị kẹp giữa Động mạch mạc treo tràng trên và Động mạch chủ bụng, làm ứ trệ tuần hoàn tĩnh mạch thận trái gây vỡ vi mạch đổ vào đài thận.<br><br><b>💡 Lâm sàng:</b><br>Trẻ gầy cao đái máu sau vận động, đau hông lưng trái, bé trai có thể kèm giãn tĩnh mạch thừng tinh trái.",
        "extra": "Left renal vein entrapment syndrome.",
        "tags": ["PED-47", "EBM", "Nutcracker"]
    },
    {
        "id": "PED47-E23",
        "track": "ebm",
        "type": "cloze",
        "category": "Đặc tính hồng cầu liềm",
        "section": "E3",
        "text": "[EBM] Trẻ mang đặc tính hồng cầu hình liềm (Sickle Cell Trait): môi trường tủy thận ưu trương và toan hóa làm hồng cầu biến dạng liềm gây tắc vi mạch và {{c1::hoại tử nhú thận (papillary necrosis)}}.",
        "extra": "Gây đái máu đại thể không đau từng đợt, hay gặp ở thận trái.",
        "tags": ["PED-47", "EBM", "Sickle-cell"]
    },
    {
        "id": "PED47-E24",
        "track": "ebm",
        "type": "basic",
        "category": "Nguyên lý ALARA",
        "section": "E3",
        "front": "Nguyên lý ALARA trong chẩn đoán hình ảnh đái máu ở trẻ em quy định chỉ định đầu tay là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Siêu âm Doppler hệ tiết niệu là lựa chọn số 1 (không nhiễm xạ, phát hiện sỏi cản/không cản quang, ứ nước, nang, u Wilms, mạch máu Nutcracker); hạn chế tối đa X-quang KUB và CT.<br><br><b>💡 Lưu ý:</b><br>Chỉ chụp CT khi chấn thương bụng kín nặng hoặc nghi u ác tính xâm lấn.",
        "extra": "ALARA = As Low As Reasonably Achievable.",
        "tags": ["PED-47", "EBM", "ALARA"]
    },

    # =========================================================================
    # TRACK 2: E4 7 CHỈ ĐỊNH SINH THIẾT THẬN & ĐIỀU KIỆN AN TOÀN
    # =========================================================================
    {
        "id": "PED47-E25",
        "track": "ebm",
        "type": "cloze",
        "category": "Chỉ định protein niệu",
        "section": "E4",
        "text": "[EBM] Ngưỡng protein niệu chỉ định sinh thiết thận theo barem là: Protein niệu 24h &gt; {{c1::1 g/1,73 m²/ngày}} hoặc tỷ lệ UPr/UCr &gt; {{c1::1,0 mg/mg}} kéo dài.",
        "extra": "Nelson 21st Ch.538 + Barem Bộ môn Nhi.",
        "tags": ["PED-47", "EBM", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-E26",
        "track": "ebm",
        "type": "cloze",
        "category": "Chỉ định bổ thể C3",
        "section": "E4",
        "text": "[EBM] Mốc thời gian bổ thể C3 thấp kéo dài bắt buộc phải sinh thiết thận theo barem là trên {{c1::3 tháng}} (để chẩn đoán xác định MPGN hoặc Viêm thận Lupus).",
        "extra": "Bổ thể thấp kéo dài loại trừ APSGN (APSGN phục hồi sau 6-8 tuần).",
        "tags": ["PED-47", "EBM", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-E27",
        "track": "ebm",
        "type": "cloze",
        "category": "Chỉ định mức lọc cầu thận",
        "section": "E4",
        "text": "[EBM] Mức lọc cầu thận (eGFR) giảm kéo dài dưới ngưỡng &lt; {{c1::80 ml/phút/1,73 m²}} là chỉ định sinh thiết thận để đánh giá xơ hóa mô bệnh học.",
        "extra": "Barem 7 chỉ định sinh thiết thận Bộ môn Nhi.",
        "tags": ["PED-47", "EBM", "Sinh-thiet-than"]
    },
    {
        "id": "PED47-E28",
        "track": "ebm",
        "type": "basic",
        "category": "An toàn sinh thiết",
        "section": "E4",
        "front": "4 điều kiện an toàn bắt buộc phải kiểm tra trước khi thực hiện sinh thiết thận ở trẻ em?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Có đủ 2 thận bình thường trên siêu âm; 2) Huyết áp kiểm soát ổn định; 3) Đông máu an toàn (Tiểu cầu > 100.000/µL, INR < 1.2, aPTT bình thường); 4) Không nhiễm trùng huyết/vùng lưng.<br><br><b>💡 Cảnh báo:</b><br>Sinh thiết thận độc nhất tiềm ẩn nguy cơ mất toàn bộ chức năng thận nếu biến chứng.",
        "extra": "Quy chuẩn an toàn thủ thuật thận học nhi.",
        "tags": ["PED-47", "EBM", "Sinh-thiet-than", "An-toan"]
    },

    # =========================================================================
    # TRACK 2: E5 THUẬT TOÁN TIẾP CẬN 5 BƯỚC THỰC CHIẾN
    # =========================================================================
    {
        "id": "PED47-E29",
        "track": "ebm",
        "type": "basic",
        "category": "Sàng lọc Bước 2",
        "section": "E5",
        "front": "Trong thuật toán 5 bước thực chiến, sau khi khẳng định đái máu thực sự (Bước 1), Bước 2 phải sàng lọc ngay hội chứng gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Sàng lọc Hội chứng Viêm cầu thận cấp: tìm Phù (mi mắt buổi sáng), Tăng huyết áp và Thiểu niệu để xử trí cấp cứu kịp thời.<br><br><b>💡 Hành động:</b><br>Làm ngay UPr/UCr, Creatinin, Điện giải đồ, C3, C4, ASLO.",
        "extra": "Thuật toán tiếp cận đái máu thực chiến 5 bước.",
        "tags": ["PED-47", "EBM", "Tiep-can"]
    },
    {
        "id": "PED47-E30",
        "track": "ebm",
        "type": "basic",
        "category": "Đái máu vi thể đơn độc",
        "section": "E5",
        "front": "Ở trẻ đái máu vi thể đơn độc không triệu chứng, bước tiếp cận chuẩn tiếp theo là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Kiểm tra lại ít nhất 2 mẫu nước tiểu trong 2 tuần tiếp theo và xét nghiệm nước tiểu của bố mẹ, anh chị em ruột.<br><br><b>💡 Ý nghĩa:</b><br>Loại trừ đái máu thoáng qua và phát hiện sớm bệnh màng đáy mỏng có tính chất gia đình.",
        "extra": "Nelson 21st Ch.538 - Asymptomatic Microscopic Hematuria.",
        "tags": ["PED-47", "EBM", "Tiep-can"]
    },
    {
        "id": "PED47-E31",
        "track": "ebm",
        "type": "cloze",
        "category": "Sàng lọc ngoài cầu thận",
        "section": "E5",
        "text": "[EBM] Trong thuật toán tiếp cận nguyên nhân ngoài cầu thận (Bước 5), xét nghiệm sàng lọc nguyên nhân chuyển hóa phổ biến nhất là {{c1::tỷ lệ Canxi/Creatinine niệu (UCa/UCr)}}.",
        "extra": "Phát hiện sớm tăng canxi niệu vô căn trước khi hình thành sỏi niệu.",
        "tags": ["PED-47", "EBM", "Tiep-can"]
    },

    # =========================================================================
    # TRACK 2: E6 ROSETTA STONE ĐỐI CHIẾU THUẬT NGỮ
    # =========================================================================
    {
        "id": "PED47-E32",
        "track": "ebm",
        "type": "basic",
        "category": "Rosetta Stone 1",
        "section": "E6",
        "front": "Barem ghi 'Bệnh móng màng đáy' — bản chất EBM quốc tế là gì và cách viết bài thi tự luận?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tên đúng là Bệnh màng đáy mỏng (Thin Basement Membrane Disease) do đột biến gen collagen COL4A3/COL4A4, gây đái máu lành tính gia đình.<br><br><b>💡 Điểm thi:</b><br>Viết 'Bệnh màng đáy mỏng (sách in nhầm là móng màng đáy) - đái máu lành tính gia đình, chức năng thận bình thường'.",
        "extra": "Bảng đối chiếu Rosetta Stone PED-47.",
        "tags": ["PED-47", "EBM", "Rosetta-Stone"]
    },
    {
        "id": "PED47-E33",
        "track": "ebm",
        "type": "basic",
        "category": "Rosetta Stone 2",
        "section": "E6",
        "front": "Barem ghi 'Scholein Henoch' — danh pháp quốc tế hiện đại là gì và cơ chế miễn dịch?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Tên chuẩn quốc tế hiện nay là Viêm mạch IgA (IgA Vasculitis / Henoch-Schonlein Purpura), do lắng đọng phức hợp miễn dịch IgA gây viêm mạch nhỏ toàn thân.<br><br><b>💡 Lâm sàng:</b><br>Thể toàn thân của bệnh thận IgA với ban xuất huyết hoại tử cẳng chân và mông.",
        "extra": "Bảng đối chiếu Rosetta Stone PED-47.",
        "tags": ["PED-47", "EBM", "Rosetta-Stone"]
    },
    {
        "id": "PED47-E34",
        "track": "ebm",
        "type": "basic",
        "category": "Rosetta Stone 3",
        "section": "E6",
        "front": "Barem ghi 'Đái máu do tập thể dục' — bản chất lâm sàng và nghiệm pháp xác nhận là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Exercise-induced hematuria do thiếu máu cục bộ thận tạm thời hoặc va chạm thành bàng quang khi vận động mạnh.<br><br><b>💡 Nghiệm pháp:</b><br>Làm lại xét nghiệm nước tiểu sau 48–72 giờ nghỉ ngơi hoàn toàn, nếu hết đái máu là lành tính.",
        "extra": "Bảng đối chiếu Rosetta Stone PED-47.",
        "tags": ["PED-47", "EBM", "Rosetta-Stone"]
    },
    {
        "id": "PED47-E35",
        "track": "ebm",
        "type": "basic",
        "category": "Rosetta Stone 4",
        "section": "E6",
        "front": "'Factitious hematuria' (Đái máu giả tạo) là gì và cách xử trí xác nhận trên lâm sàng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Hiện tượng bệnh nhi hoặc người nhà cố tình nhỏ máu hoặc chất tạo màu vào mẫu nước tiểu.<br><br><b>💡 Xử trí:</b><br>Giám sát lấy nước tiểu trực tiếp tại buồng bệnh hoặc thông tiểu lấy mẫu khi lâm sàng và xét nghiệm mâu thuẫn nhau.",
        "extra": "Bảng đối chiếu Rosetta Stone PED-47.",
        "tags": ["PED-47", "EBM", "Rosetta-Stone"]
    },

    # =========================================================================
    # TRACK 2: E7 CẠM BẪY LÂM SÀNG SINH TỬ
    # =========================================================================
    {
        "id": "PED47-E36",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy que thử Dipstick",
        "section": "E7",
        "front": "Cạm bẫy: Que thử Dipstick dương tính 3+ với máu — vì sao không được vội vàng kết luận bệnh nhân đái máu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì que thử phản ứng chéo với Hemoglobin tự do và Myoglobin tự do. Bắt buộc phải soi kính hiển vi thấy hồng cầu mới khẳng định đái máu thực sự.<br><br><b>💡 Nguy hiểm:</b><br>Bỏ sót tiêu cơ vân cấp (Myoglobin) có thể gây hoại tử ống thận cấp suy thận không hồi phục.",
        "extra": "Cạm bẫy lâm sàng sinh tử số 1.",
        "tags": ["PED-47", "EBM", "Bay-lam-sang"]
    },
    {
        "id": "PED47-E37",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy xét nghiệm 1 lần",
        "section": "E7",
        "front": "Cạm bẫy: Vì sao không bao giờ được chẩn đoán đái máu vi thể bệnh lý chỉ dựa trên một mẫu nước tiểu duy nhất?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Vì 1–2% trẻ em bình thường có đái máu vi thể thoáng qua sau sốt virus, vận động thể lực hoặc chấn thương nhẹ.<br><br><b>💡 Quy tắc:</b><br>Bắt buộc xác nhận trên ít nhất 2–3 mẫu nước tiểu độc lập cách nhau 1–2 tuần.",
        "extra": "Cạm bẫy lâm sàng sinh tử số 2.",
        "tags": ["PED-47", "EBM", "Bay-lam-sang"]
    },
    {
        "id": "PED47-E38",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy tiền sử gia đình",
        "section": "E7",
        "front": "Cạm bẫy: Trẻ có đái máu vi thể đơn độc, việc bỏ qua xét nghiệm nước tiểu của bố mẹ dẫn đến hậu quả gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Dễ chỉ định sinh thiết thận xâm lấn không cần thiết ở trẻ bị Bệnh màng đáy mỏng lành tính di truyền từ bố/mẹ.<br><br><b>💡 Ngược lại:</b><br>Nếu gia đình có người chạy thận nhân tạo hoặc điếc → phát hiện sớm Hội chứng Alport.",
        "extra": "Cạm bẫy lâm sàng sinh tử số 3.",
        "tags": ["PED-47", "EBM", "Bay-lam-sang"]
    },
    {
        "id": "PED47-E39",
        "track": "ebm",
        "type": "basic",
        "category": "Bẫy bổ thể C3",
        "section": "E7",
        "front": "Cạm bẫy: Trẻ chẩn đoán viêm cầu thận cấp hậu liên cầu (APSGN), điều kiện tiên quyết nào để xác nhận chẩn đoán cuối cùng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>Bổ thể C3 bắt buộc phải hồi phục về bình thường sau 6–8 tuần. Nếu sau 8–12 tuần C3 vẫn thấp, chẩn đoán coi như sai và phải sinh thiết thận tìm MPGN hoặc Lupus.<br><br><b>💡 Lưu ý:</b><br>APSGN chỉ là chẩn đoán tạm thời cho đến khi C3 về bình thường.",
        "extra": "Cạm bẫy lâm sàng sinh tử số 4.",
        "tags": ["PED-47", "EBM", "Bay-lam-sang"]
    },
]
