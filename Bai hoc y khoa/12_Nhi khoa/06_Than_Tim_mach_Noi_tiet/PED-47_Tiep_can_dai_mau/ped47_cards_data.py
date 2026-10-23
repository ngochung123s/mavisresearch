# -*- coding: utf-8 -*-
"""
ped47_cards_data.py
Bộ dữ liệu thẻ Anki Master cho PED-47: Tiếp cận đái máu ở trẻ em.
Tuân thủ 100% Medical Flashcard Governance (Basic-First Architecture, Zero-Spoiler Cloze, Fast Decision Algorithms).
"""

cards_data = [
  {
    "id": "PED47-B01",
    "track": "barem_goc",
    "type": "basic",
    "category": "Mục tiêu bài học",
    "section": "B0",
    "front": "<span style=\"color:#ffd43b\"><b>4 mục tiêu cốt lõi</b></span> của bài <span style=\"color:#74c0fc\"><b>Đái máu</b></span> theo giáo trình Nhi Thái Bình là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Định nghĩa & cơ chế</b></span> hồng cầu trong nước tiểu.<br>2) <span style=\"color:#ff6b6b\"><b>Nguyên nhân</b></span> gây đái máu (tại cầu thận & ngoài cầu thận).<br>3) <span style=\"color:#ff6b6b\"><b>Lâm sàng</b></span> & <span style=\"color:#ffd43b\"><b>cận lâm sàng</b></span>.<br>4) <span style=\"color:#51cf66\"><b>Cách tiếp cận</b></span> bệnh nhân đái máu (sơ đồ thuật toán 5 bước).<br><br><b>💡 Giải thích của AI:</b><br>Bốn mục tiêu này thiết lập khung xương tư duy toàn diện: bắt đầu từ định nghĩa ngưỡng tế bào, bản chất tổn thương màng lọc, phân loại căn nguyên theo giải phẫu đến lưu đồ hành động thực chiến tại giường bệnh.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục tiêu 1-4)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Muc-tieu"
    ]
  },
  {
    "id": "PED47-B02",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Mục tiêu bài học",
    "section": "B0",
    "text": "[Barem gốc] Bài <span style=\"color:#74c0fc\"><b>Đái máu</b></span> gồm <span style=\"color:#ffd43b\"><b>4 mục tiêu cốt lõi</b></span>: {{c1::<span style=\"color:#74c0fc\"><b>định nghĩa & cơ chế</b></span>, <span style=\"color:#ff6b6b\"><b>nguyên nhân</b></span>, <span style=\"color:#ffd43b\"><b>lâm sàng & cận lâm sàng</b></span>, và <span style=\"color:#51cf66\"><b>cách tiếp cận bệnh nhân đái máu</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Che trọn vẹn cả 4 mục tiêu để active recall toàn phần cấu trúc bài học, không để lộ mớm đáp án.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục tiêu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Muc-tieu"
    ]
  },
  {
    "id": "PED47-B03",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Định nghĩa đái máu",
    "section": "B1",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu</b></span> là hiện tượng có {{c1::<span style=\"color:#ff6b6b\"><b>máu hay hồng cầu</b></span>}} trong nước tiểu, có thể biểu hiện dưới dạng <span style=\"color:#ff6b6b\"><b>đại thể</b></span> hoặc <span style=\"color:#ffd43b\"><b>vi thể</b></span>.",
    "extra": "<b>💡 Giải thích của AI:</b> Phân định rõ hai hình thái đại thể (nhìn thấy bằng mắt thường) và vi thể (chỉ phát hiện qua kính hiển vi) là bước đầu tiên trong tiếp cận.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Dinh-nghia"
    ]
  },
  {
    "id": "PED47-B04",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Định nghĩa đái máu",
    "section": "B1",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu đại thể</b></span> là hiện tượng nước tiểu có <span style=\"color:#ff6b6b\"><b>hồng cầu</b></span> làm biến đổi màu sắc, phát hiện được bằng {{c1::<span style=\"color:#ffd43b\"><b>mắt thường</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Khi lượng hồng cầu đủ lớn làm đổi màu nước tiểu (đỏ tươi, nâu sẫm, nước rửa thịt, nước coca-cola), mắt thường quan sát được ngay không cần kính hiển vi.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Dinh-nghia"
    ]
  },
  {
    "id": "PED47-B05",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Định nghĩa đái máu",
    "section": "B1",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu vi thể</b></span> được xác định bằng soi kính hiển vi, khi soi nước tiểu tươi giữa dòng có {{c1::<span style=\"color:#ffd43b\"><b>≥ 5 hồng cầu/ml</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Barem quy định ngưỡng trên mẫu nước tiểu tươi giữa dòng (không quay ly tâm) là từ 5 hồng cầu trở lên.<br><b>⚖️ Đối chiếu (Ngoài barem):</b> đơn vị chuẩn quốc tế là <b>≥ 5 hồng cầu/µL</b> (= /mm³) nước tiểu không ly tâm; trên cặn ly tâm tài liệu dùng ngưỡng <b>&gt; 3–5 hồng cầu/vi trường</b> (barem: &gt; 3). \"5 hồng cầu/ml\" nhiều khả năng là lỗi in đơn vị (nước tiểu bình thường đã có tới vài nghìn hồng cầu/ml). Khi thi chép đúng như barem.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 1); Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Dinh-nghia",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B06",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Định nghĩa đái máu",
    "section": "B1",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu vi thể</b></span> xác định khi có {{c1::<span style=\"color:#ffd43b\"><b>trên 3 hồng cầu/vi trường</b></span>}} trong mẫu quay ly tâm <span style=\"color:#ffd43b\"><b>10 ml</b></span> nước tiểu tươi lấy giữa dòng.",
    "extra": "<b>💡 Giải thích của AI:</b> Quy trình chuẩn: lấy 10 ml nước tiểu giữa dòng, quay ly tâm 1500–2000 vòng/phút trong 5 phút, gạn lấy cặn soi độ phóng đại lớn (HPF 400×).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Dinh-nghia",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B07",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Cơ chế đái máu",
    "section": "B2",
    "text": "[Barem gốc] Cơ chế <span style=\"color:#74c0fc\"><b>đái máu tại cầu thận</b></span>: do tổn thương {{c1::<span style=\"color:#74c0fc\"><b>màng đáy cầu thận</b></span>}}, làm các lỗ lọc rộng hơn và tăng {{c1::<span style=\"color:#ff6b6b\"><b>tính thấm thành mạch</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Phức hợp miễn dịch hoặc tự kháng thể tấn công màng đáy làm phá vỡ rào cản điện tích và cơ học, khiến hồng cầu bị ép chui qua lỗ lọc rách hẹp.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 2)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Co-che"
    ]
  },
  {
    "id": "PED47-B08",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Cơ chế đái máu",
    "section": "B2",
    "text": "[Barem gốc] Trong <span style=\"color:#74c0fc\"><b>đái máu ngoài cầu thận</b></span>, do hồng cầu vào nước tiểu trực tiếp không qua lỗ màng đáy nên hồng cầu vẫn {{c1::<span style=\"color:#51cf66\"><b>giữ nguyên hình dạng và kích thước</b></span>}} như máu ngoại vi.",
    "extra": "<b>💡 Giải thích của AI:</b> Máu chảy trực tiếp từ tổn thương biểu mô đường dẫn niệu (đài bể thận, niệu quản, bàng quang, niệu đạo) nên hồng cầu đồng dạng, không chịu áp lực thẩm thấu ống thận.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 2)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Co-che"
    ]
  },
  {
    "id": "PED47-B09",
    "track": "barem_goc",
    "type": "basic",
    "category": "Cơ chế đái máu",
    "section": "B2",
    "front": "Vì sao <span style=\"color:#ffd43b\"><b>trẻ nhỏ</b></span> lại dễ bị tổn thương vỡ mạch máu đường tiết niệu gây <span style=\"color:#74c0fc\"><b>đái máu ngoài cầu thận</b></span> theo giáo trình?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>Do ở trẻ nhỏ, <span style=\"color:#74c0fc\"><b>cấu trúc thành mạch chưa bền vững</b></span> và <span style=\"color:#ff6b6b\"><b>tính thấm thành mạch cao</b></span>, khiến mạch máu rất dễ vỡ khi gặp các tác nhân lý hóa quá mức.<br><br><b>💡 Giải thích của AI:</b><br>Hệ mạch máu niệu mạc của trẻ em đang trong giai đoạn phát triển, các liên kết nội mô lỏng lẻo hơn người lớn. Khi có tăng áp lực dòng nước tiểu, nhiễm trùng, chấn thương nhẹ hoặc sỏi cọ xát, các mao mạch biểu mô dễ bị bục vỡ đưa máu trực tiếp vào lòng đường tiểu.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 2)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Co-che"
    ]
  },
  {
    "id": "PED47-B10",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu lành tính có tính chất gia đình</b></span> (nguyên nhân tại cầu thận) là bệnh {{c1::<span style=\"color:#ffd43b\"><b>màng đáy mỏng</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Sách in nhầm thành \"móng màng đáy\"; khi thi viết \"bệnh màng đáy mỏng\" (Thin Basement Membrane Nephropathy). Bệnh do đột biến dị hợp gen COL4A3/COL4A4; bố hoặc mẹ thường cũng có đái máu vi thể.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan",
      "Loi-in-an"
    ]
  },
  {
    "id": "PED47-B11",
    "track": "barem_goc",
    "type": "basic",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan"
    ],
    "front": "Kể tên các nguyên nhân đái máu <span style=\"color:#74c0fc\"><b>tại cầu thận</b></span> thuộc nhóm <span style=\"color:#51cf66\"><b>đái máu lành tính</b></span> và nhóm <span style=\"color:#ff6b6b\"><b>viêm cầu thận / bệnh thận IgA</b></span> theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Đái máu lành tính có tính chất gia đình</b></span> (bệnh màng đáy mỏng).<br>2) <span style=\"color:#51cf66\"><b>Đái máu lành tính không có tính chất gia đình</b></span>.<br>3) <span style=\"color:#ff6b6b\"><b>Viêm cầu thận cấp sau nhiễm trùng</b></span>.<br>4) <span style=\"color:#ff6b6b\"><b>Viêm cầu thận tăng sinh màng</b></span>.<br>5) <span style=\"color:#ff6b6b\"><b>Viêm cầu thận tiến triển nhanh</b></span>.<br>6) <span style=\"color:#74c0fc\"><b>Bệnh thận IgA</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Barem liệt kê liền 13 nguyên nhân tại cầu thận. AI tách làm 2 thẻ cho dễ nhớ: thẻ này gồm 6 bệnh \"của riêng cầu thận\" (2 lành tính + 3 viêm cầu thận + IgA); thẻ sau gồm 7 bệnh hệ thống, mạch máu, di truyền và bệnh thận khác."
  },
  {
    "id": "PED47-B12",
    "track": "barem_goc",
    "type": "basic",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan"
    ],
    "front": "Kể tên các nguyên nhân đái máu <span style=\"color:#74c0fc\"><b>tại cầu thận</b></span> thuộc nhóm <span style=\"color:#ff6b6b\"><b>bệnh hệ thống, mạch máu, di truyền</b></span> và các bệnh thận khác theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Viêm thận Schönlein–Henoch</b></span>.<br>2) <span style=\"color:#ff6b6b\"><b>Viêm thận Lupus</b></span>.<br>3) <span style=\"color:#ff6b6b\"><b>Viêm mao mạch hoại tử</b></span>.<br>4) <span style=\"color:#ff6b6b\"><b>Hội chứng huyết tán ure máu cao (HUS)</b></span>.<br>5) <span style=\"color:#74c0fc\"><b>Hội chứng Alport</b></span>.<br>6) <span style=\"color:#ffd43b\"><b>Tắc mạch thận, viêm thận kẽ</b></span>.<br>7) <span style=\"color:#ffd43b\"><b>Nang thận</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Mẹo đọc liền: \"Henoch – Lupus – Mao mạch – HUS – Alport – Tắc/Kẽ – Nang\". Ngoài barem: Alport do đột biến collagen type IV (khoảng 80% là gen COL4A5 liên kết X), kèm điếc tiếp nhận và tổn thương mắt; nhóm này cần khám ngoài thận (da, khớp, thính lực, mắt)."
  },
  {
    "id": "PED47-B13",
    "track": "barem_goc",
    "type": "basic",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan"
    ],
    "front": "Kể tên các nguyên nhân đái máu <span style=\"color:#74c0fc\"><b>ngoài cầu thận</b></span> theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Nhiễm trùng tiết niệu</b></span>.<br>2) <span style=\"color:#ffd43b\"><b>Tăng canxi niệu</b></span>.<br>3) <span style=\"color:#ff6b6b\"><b>Sỏi thận</b></span>.<br>4) <span style=\"color:#ff6b6b\"><b>Chấn thương</b></span>.<br>5) <span style=\"color:#51cf66\"><b>Do tập thể dục</b></span>.<br>6) <span style=\"color:#ff6b6b\"><b>Rối loạn đông máu</b></span>.<br>7) <span style=\"color:#74c0fc\"><b>Dị tật mạch máu</b></span>.<br>8) <span style=\"color:#74c0fc\"><b>Hội chứng Nutcracker</b></span>.<br>9) <span style=\"color:#ff6b6b\"><b>Khối u ác tính</b></span>: u nguyên bào thận (Wilms), ung thư tế bào thận, ung thư bàng quang.<br>10) <span style=\"color:#51cf66\"><b>Kinh nguyệt</b></span>.<br>11) <span style=\"color:#51cf66\"><b>Factitious</b></span> (đái máu giả tạo do đưa máu vào hoặc dùng phẩm màu).<br><br><b>💡 Giải thích của AI:</b><br>Mẹo nhớ theo cụm: \"Nhiễm – Canxi – Sỏi\" (trong lòng đường tiểu); \"Chấn thương – Tập – Đông máu\" (cơ học, cầm máu); \"Mạch – Nutcracker\" (mạch máu); \"U\"; cuối cùng 2 nguồn không thật sự từ đường tiểu là kinh nguyệt và giả tạo, cần loại trừ đầu tiên."
  },
  {
    "id": "PED47-B14",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "text": "[Barem gốc] Các <span style=\"color:#74c0fc\"><b>khối u ác tính</b></span> gây đái máu ngoài cầu thận theo barem gồm: {{c1::<span style=\"color:#ff6b6b\"><b>u nguyên bào thận (Wilms), ung thư tế bào thận, ung thư bàng quang</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> U Wilms hay gặp ở trẻ dưới 5 tuổi, biểu hiện bằng khối u bụng sờ nắn không đau kèm đái máu đại thể hoặc vi thể.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan"
    ]
  },
  {
    "id": "PED47-B15",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Nguyên nhân đái máu",
    "section": "B3",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Dị tật chèn ép mạch máu</b></span> gây đái máu ngoài cầu thận là hội chứng {{c1::<span style=\"color:#74c0fc\"><b>Nutcracker</b></span>}} (kẹp tĩnh mạch thận trái giữa động mạch mạc treo tràng trên và động mạch chủ bụng).",
    "extra": "<b>💡 Giải thích của AI:</b> Chèn ép làm tăng áp lực tĩnh mạch thận trái dẫn đến vỡ các mao mạch giãn vào bể thận, gây đái máu từng đợt kèm đau hông lưng trái.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Bảng mục 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Nguyen-nhan"
    ]
  },
  {
    "id": "PED47-B16",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] Nước tiểu <span style=\"color:#74c0fc\"><b>đái máu đại thể</b></span> có thể có màu {{c1::<span style=\"color:#ff6b6b\"><b>đỏ như nước rửa thịt</b></span>, <span style=\"color:#ffd43b\"><b>màu coca-cola</b></span>, sẫm như nước chè}}; nếu để lâu sẽ có <span style=\"color:#74c0fc\"><b>lắng cặn hồng cầu</b></span>.",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: màu đỏ tươi gợi ý máu mới chảy ở đường dẫn niệu; màu coca-cola, nước chè gợi ý hồng cầu đã lưu lâu trong ống thận bị toan hóa (thường nguồn gốc cầu thận).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 19, Mục 4 Đái máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B17",
    "track": "barem_goc",
    "type": "basic",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "front": "Đái máu <span style=\"color:#74c0fc\"><b>đầu bãi</b></span>, <span style=\"color:#74c0fc\"><b>cuối bãi</b></span> và <span style=\"color:#74c0fc\"><b>toàn bãi</b></span> gợi ý tổn thương ở đâu theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Đầu bãi:</b> tổn thương <span style=\"color:#74c0fc\"><b>niệu đạo</b></span>.<br>2) <b>Cuối bãi:</b> tổn thương <span style=\"color:#74c0fc\"><b>bàng quang</b></span>.<br>3) <b>Toàn bãi:</b> <span style=\"color:#ff6b6b\"><b>viêm cầu thận</b></span>, niệu quản, bàng quang, <span style=\"color:#ff6b6b\"><b>bệnh về máu</b></span>, <span style=\"color:#ffd43b\"><b>đái máu do thuốc</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Ngoài barem: trên lâm sàng phân biệt bằng nghiệm pháp 3 cốc (cốc 1 = đầu bãi, cốc 3 = cuối bãi, cả 3 cốc = toàn bãi). Đầu bãi do dòng nước tiểu đầu cuốn máu đọng ở niệu đạo; cuối bãi do bàng quang co bóp tống máu ở cuối; toàn bãi khi máu đã hòa đều từ phía trên (hoặc chảy nhiều từ bàng quang).",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Đái máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B18",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu đại thể</b></span> có tính chất đỏ tươi và có {{c1::<span style=\"color:#ff6b6b\"><b>máu cục (cục máu đông)</b></span>}} gợi ý vị trí tổn thương thuộc {{c1::<span style=\"color:#74c0fc\"><b>ngoài cầu thận</b></span>}} (đường dẫn niệu dưới).",
    "extra": "<b>💡 Giải thích của AI:</b> Cục máu đông chỉ hình thành khi máu chảy ồ ạt ở đường niệu dưới không có enzyme tiêu sợi huyết urokinase của mô thận.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Đái máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B19",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#ff6b6b\"><b>Phù</b></span> trong bệnh thận thường là phù {{c1::<span style=\"color:#ffd43b\"><b>trắng, mềm, ấn lõm</b></span>}}; hay gặp trong tổn thương cầu thận như <span style=\"color:#74c0fc\"><b>viêm cầu thận cấp, hội chứng thận hư</b></span>.",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: phù cầu thận thường rõ nhất ở mi mắt buổi sáng khi ngủ dậy do mô quanh hốc mắt lỏng lẻo.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Phù)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B20",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] Phân độ <span style=\"color:#ff6b6b\"><b>phù</b></span> theo cân nặng: phù nhẹ khi cân nặng tăng {{c1::<span style=\"color:#ffd43b\"><b>&lt; 10%</b></span>}}; phù vừa khi tăng {{c1::<span style=\"color:#ffd43b\"><b>10 – 20%</b></span>}}; phù nặng khi tăng {{c1::<span style=\"color:#ffd43b\"><b>&gt; 20%</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Mẹo: chỉ có 2 mốc 10% và 20% chia 3 mức. Cân nặng hằng ngày là chỉ số khách quan nhất để theo dõi ứ dịch và đáp ứng lợi tiểu.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Phù)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B21",
    "track": "barem_goc",
    "type": "basic",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "front": "Đặc điểm <span style=\"color:#ff6b6b\"><b>tổn thương khớp</b></span> trong đái máu do <span style=\"color:#74c0fc\"><b>Lupus ban đỏ hệ thống</b></span> theo giáo trình là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Đau khớp đơn thuần hoặc đau nhiều khớp nhỏ</b></span> các chi, có thể <span style=\"color:#74c0fc\"><b>chuyển từ khớp này sang khớp khác</b></span>.<br>2) <span style=\"color:#ffd43b\"><b>Không cứng khớp buổi sáng</b></span>, <span style=\"color:#ffd43b\"><b>không sưng nóng đỏ đau</b></span>.<br>3) <span style=\"color:#51cf66\"><b>Không biến dạng khớp</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Khác viêm khớp dạng thấp (cứng khớp buổi sáng kéo dài, bào mòn và biến dạng khớp), viêm khớp Lupus không bào mòn. Ngoài barem: một số ít ca Lupus có biến dạng kiểu Jaccoud nhưng nắn lại được và không tổn thương xương.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Đau khớp)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B22",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu</b></span> kèm xuất huyết cẳng chân dạng {{c1::<span style=\"color:#ff6b6b\"><b>đi bốt</b></span>}} nghĩ nhiều đến {{c1::<span style=\"color:#74c0fc\"><b>Schönlein–Henoch</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Sách in \"Scholein Henoch\"; tên đúng là Schönlein–Henoch, nay gọi là viêm mạch IgA. Ngoài barem: ban xuất huyết sờ thấy gồ, đối xứng, ở vùng chịu trọng lực (cẳng chân, mông).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Xuất huyết da, niêm)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B23",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu</b></span> kèm ban {{c1::<span style=\"color:#ff6b6b\"><b>cánh bướm</b></span>}} ở mặt (hai bên cánh mũi, hai gò má) hoặc ban hình đĩa, da nhạy cảm ánh sáng, loét miệng họng là dấu hiệu của bệnh {{c1::<span style=\"color:#74c0fc\"><b>Lupus ban đỏ</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: ban cánh bướm điển hình chừa nếp mũi má, giúp phân biệt với viêm da dầu.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Hồng ban)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B24",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu kèm đau</b></span>: đau vùng mạng sườn, đau quặn nghĩ đến {{c1::<span style=\"color:#ff6b6b\"><b>sỏi niệu quản, thận ứ nước, tắc nghẽn đường tiểu</b></span>}}; đau vùng hạ vị nghĩ đến {{c1::<span style=\"color:#ffd43b\"><b>viêm bàng quang hoặc cầu bàng quang</b></span>}}; đau bụng âm ỉ đến dữ dội nghĩ đến {{c1::<span style=\"color:#74c0fc\"><b>Schönlein–Henoch</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Barem nhấn mạnh: đái máu không đau cũng không loại trừ sỏi hay tắc nghẽn. Đái máu kèm đái rắt, đái buốt, đái khó thường gặp trong nhiễm trùng đường tiểu.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20-21, Mục 4 Đau bụng)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B25",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] <span style=\"color:#74c0fc\"><b>Đái máu đại thể tái phát</b></span> kết hợp với <span style=\"color:#ff6b6b\"><b>nhiễm trùng đường hô hấp trên</b></span> thường là: {{c1::<span style=\"color:#74c0fc\"><b>bệnh thận IgA</b></span>, <span style=\"color:#ffd43b\"><b>bệnh màng đáy mỏng</b></span>, <span style=\"color:#ff6b6b\"><b>hội chứng Alport</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: trong bệnh thận IgA, đái máu xuất hiện cùng lúc hoặc trong 1–2 ngày sau nhiễm trùng hô hấp (đái máu đồng thì), khác viêm cầu thận cấp sau nhiễm liên cầu (sau 1–3 tuần, C3 giảm).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 21, Mục 4 Sốt)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B26",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Cận lâm sàng",
    "section": "B5",
    "text": "[Barem gốc] Trong xét nghiệm nước tiểu, {{c1::<span style=\"color:#ff6b6b\"><b>trụ hồng cầu</b></span>}} là bằng chứng chắc chắn tổn thương tại <span style=\"color:#74c0fc\"><b>cầu thận</b></span>.",
    "extra": "<b>💡 Giải thích của AI:</b> Trụ hồng cầu được đúc trong ống thận từ protein Tamm-Horsfall và hồng cầu đã đi qua màng lọc cầu thận. Hồng cầu biến dạng &gt; 80% (Bước 4 sơ đồ) chỉ là dấu hiệu gợi ý mạnh, không \"chắc chắn\" như trụ hồng cầu.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.1 Xét nghiệm nước tiểu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B27",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Cận lâm sàng",
    "section": "B5",
    "text": "[Barem gốc] Soi hình dáng hồng cầu niệu giúp định vị: hồng cầu <span style=\"color:#ff6b6b\"><b>biến dạng đa hình thái</b></span> gợi ý nguồn gốc {{c1::<span style=\"color:#74c0fc\"><b>cầu thận</b></span>}}; hồng cầu <span style=\"color:#51cf66\"><b>đồng dạng tròn đều</b></span> gợi ý nguồn gốc {{c1::<span style=\"color:#74c0fc\"><b>ngoài cầu thận</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Kính hiển vi đối pha (Phase-contrast microscopy) soi cặn lắng nước tiểu tươi là xét nghiệm hàng đầu để phân loại vị trí tổn thương.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B28",
    "track": "barem_goc",
    "type": "basic",
    "category": "Cận lâm sàng",
    "section": "B5",
    "front": "Kể tên các <span style=\"color:#51cf66\"><b>xét nghiệm miễn dịch máu</b></span> cần làm theo sách khi nghi ngờ <span style=\"color:#74c0fc\"><b>đái máu do tổn thương cầu thận</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>ASLO</b></span> (tìm bằng chứng nhiễm liên cầu).<br>2) <span style=\"color:#ffd43b\"><b>Bổ thể C3, C4</b></span>.<br>3) <span style=\"color:#51cf66\"><b>Định lượng nồng độ IgA</b></span>.<br>4) <span style=\"color:#51cf66\"><b>ANA, Anti-dsDNA</b></span> nếu nghi Lupus ban đỏ.<br><br><b>💡 Giải thích của AI:</b><br>C3 giảm, C4 bình thường: nghĩ viêm cầu thận cấp sau nhiễm liên cầu; C3 và C4 cùng giảm: nghĩ Lupus. Ngoài barem: IgA huyết thanh chỉ tăng ở khoảng một nửa bệnh nhân bệnh thận IgA, nên IgA bình thường không loại trừ bệnh.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.2 Xét nghiệm máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B29",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 1: <span style=\"color:#ff6b6b\"><b>protein niệu</b></span> {{c1::<span style=\"color:#ffd43b\"><b>&gt; 1 g/1,73 m²/ngày</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Protein niệu nhiều và dai dẳng gợi ý tổn thương cầu thận lan tỏa cần mô bệnh học để định hướng điều trị.<br><b>⚖️ Đối chiếu (Ngoài barem):</b> 1 g/1,73 m²/ngày ≈ 24 mg/m²/giờ, tức protein niệu đáng kể nhưng chưa tới ngưỡng thận hư (KDIGO 2021: UPCR ≥ 2 mg/mg hay ≥ 200 mg/mmol, hoặc ≥ 40 mg/m²/giờ). Khi thi ghi đúng mốc barem.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận); KDIGO 2021 Glomerular Diseases",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B30",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 2: <span style=\"color:#ffd43b\"><b>bổ thể C3 thấp kéo dài</b></span> {{c1::<span style=\"color:#ffd43b\"><b>trên 3 tháng</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> C3 thấp kéo dài gợi ý bệnh không phải viêm cầu thận cấp sau nhiễm liên cầu (ví dụ viêm cầu thận tăng sinh màng/bệnh cầu thận C3, viêm thận Lupus).<br><b>⚖️ Đối chiếu (Ngoài barem):</b> trong viêm cầu thận cấp sau nhiễm liên cầu, C3 thường về bình thường trong 6–8 tuần, nên nhiều tài liệu cân nhắc sinh thiết sớm hơn nếu C3 vẫn thấp sau 8 tuần. Khi thi ghi mốc barem: trên 3 tháng.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận); Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B31",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 3: <span style=\"color:#ff6b6b\"><b>mức lọc cầu thận giảm</b></span> {{c1::<span style=\"color:#ffd43b\"><b>&lt; 80 ml/phút/1,73 m²</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Suy giảm chức năng thận là dấu hiệu tổn thương cầu thận có thể tiến triển, cần mô bệnh học.<br><b>⚖️ Đối chiếu:</b> mốc &lt; 60 ml/phút/1,73 m² là ngưỡng bệnh thận mạn giai đoạn G3 của KDIGO, không phải ngưỡng sinh thiết của barem; đừng nhầm hai mốc.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B32",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 4: {{c1::<span style=\"color:#ff6b6b\"><b>viêm thận Lupus, viêm thận Schönlein–Henoch</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Mô bệnh học phân loại tổn thương thận Lupus (Class I đến VI theo ISN/RPS) quyết định trực tiếp phác đồ ức chế miễn dịch sống còn.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than"
    ]
  },
  {
    "id": "PED47-B33",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 5: <span style=\"color:#74c0fc\"><b>tiền sử gia đình</b></span> có bệnh thận nghi ngờ {{c1::<span style=\"color:#74c0fc\"><b>hội chứng Alport</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Giúp chẩn đoán xác định các bệnh lý cấu trúc màng đáy di truyền như Hội chứng Alport (đột biến chuỗi alpha collagen type IV).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than"
    ]
  },
  {
    "id": "PED47-B34",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 6: {{c1::<span style=\"color:#74c0fc\"><b>đái máu đại thể tái phát</b></span> mà không rõ nguyên nhân}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Thường để phân biệt bệnh thận IgA với bệnh màng đáy mỏng hoặc Alport (cả 3 đều có thể đái máu đại thể tái phát khi nhiễm trùng hô hấp trên).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than"
    ]
  },
  {
    "id": "PED47-B35",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "text": "[Barem gốc] Chỉ định sinh thiết thận 7: <span style=\"color:#74c0fc\"><b>đái máu do cầu thận</b></span> mà {{c1::<span style=\"color:#ffd43b\"><b>gia đình thiết tha muốn biết nguyên nhân và tiên lượng</b></span>}}, mặc dù protein niệu không cao.",
    "extra": "<b>💡 Giải thích của AI:</b> Chỉ định \"theo nguyện vọng gia đình\" là điểm đặc trưng của barem; nhớ kèm vế \"dù protein niệu không cao\".<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định Sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B36",
    "track": "barem_goc",
    "type": "basic",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "front": "<span style=\"color:#51cf66\"><b>Bước 1</b></span> trong sơ đồ tiếp cận đái máu của giáo trình Nhi Thái Bình là gì, <span style=\"color:#74c0fc\"><b>phân loại kết quả</b></span> và định hướng <span style=\"color:#51cf66\"><b>xử trí</b></span> ban đầu như thế nào?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Nội dung Bước 1:</b> Phối hợp làm <span style=\"color:#51cf66\"><b>Que thử (Dipstick)</b></span> + <span style=\"color:#51cf66\"><b>Soi kính hiển vi nước tiểu</b></span> tươi.<br>2) <b>Phân loại kết quả:</b><br>• <b>Dipstick (+) nhưng Soi (-):</b> Không có tế bào hồng cầu → tìm <span style=\"color:#ff6b6b\"><b>Hemoglobin niệu hoặc Myoglobin niệu</b></span>.<br>• <b>Dipstick (+) và Soi (+):</b> Khẳng định <span style=\"color:#74c0fc\"><b>đái máu thực sự</b></span> → chuyển tiếp sang Bước 2.<br><br><b>💡 Giải thích của AI:</b><br>Bước 1 là chốt chặn phân loại sống còn nhằm loại trừ đái sắc tố (tán huyết nội mạch hoặc tiêu cơ vân) và đái đổi màu giả tạo do thuốc/thực phẩm trước khi tiến hành các thăm dò thận học tốn kém.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B37",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "text": "[Barem gốc] <span style=\"color:#51cf66\"><b>Bước 2</b></span> sơ đồ tiếp cận: tìm dấu hiệu <span style=\"color:#74c0fc\"><b>viêm cầu thận cấp</b></span> gồm: {{c1::<span style=\"color:#ff6b6b\"><b>phù, tăng huyết áp, đái ít</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Che trọn vẹn cả tam chứng để active recall toàn phần, không mớm lộ vế nào.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ tiếp cận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B38",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "text": "[Barem gốc] <span style=\"color:#51cf66\"><b>Bước 3</b></span> (khi không có viêm cầu thận cấp) – phân loại lâm sàng: <span style=\"color:#74c0fc\"><b>đái máu đại thể</b></span> → {{c1::<span style=\"color:#ff6b6b\"><b>loại trừ gắng sức thể dục thể thao</b></span>}}; <span style=\"color:#74c0fc\"><b>đái máu vi thể đơn độc</b></span> → {{c1::<span style=\"color:#ffd43b\"><b>làm lại xét nghiệm nước tiểu hằng tuần trong 2 tuần (không tập thể dục)</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Mục đích Bước 3 là loại đái máu thoáng qua (do gắng sức, sốt…) trước khi thăm dò sâu. Ngoài barem: tài liệu quốc tế cũng yêu cầu ≥ 2–3 mẫu dương tính cách nhau vài tuần mới gọi là đái máu vi thể dai dẳng.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 3)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B39",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "text": "[Barem gốc] <span style=\"color:#51cf66\"><b>Bước 4</b></span> sơ đồ: soi {{c1::<span style=\"color:#51cf66\"><b>hình dáng hồng cầu</b></span>}} và định lượng {{c1::<span style=\"color:#51cf66\"><b>protein/creatinin niệu</b></span>}} để phân biệt nguyên nhân <span style=\"color:#74c0fc\"><b>tại cầu thận</b></span> với <span style=\"color:#74c0fc\"><b>ngoài cầu thận</b></span>.",
    "extra": "<b>💡 Giải thích của AI:</b> Đây là \"bản lề\" của sơ đồ: kết quả Bước 4 quyết định đi nhánh cầu thận (xét nghiệm chuyên sâu, sinh thiết nếu có chỉ định) hay sang Bước 5 tìm nguyên nhân ngoài cầu thận.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 4)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B40",
    "track": "barem_goc",
    "type": "basic",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "front": "<span style=\"color:#51cf66\"><b>Bước 5</b></span> sơ đồ: các xét nghiệm tìm <span style=\"color:#74c0fc\"><b>nguyên nhân ngoài cầu thận</b></span> và kết luận khi tất cả bình thường theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Tỷ lệ canxi/creatinin niệu</b></span> (tăng canxi niệu).<br>2) <span style=\"color:#51cf66\"><b>Cấy nước tiểu</b></span> tìm vi khuẩn, cấy Adenovirus.<br>3) <span style=\"color:#51cf66\"><b>Siêu âm Doppler mạch thận</b></span> (Nutcracker).<br>4) <span style=\"color:#51cf66\"><b>Xét nghiệm đông máu toàn bộ</b></span>.<br>5) <span style=\"color:#51cf66\"><b>X-quang bụng KUB</b></span> (sỏi cản quang).<br>6) <span style=\"color:#51cf66\"><b>Nước tiểu 24 giờ</b></span>: Ca, acid uric, oxalat, cystin.<br>7) <span style=\"color:#51cf66\"><b>CT ổ bụng</b></span> (chấn thương, u Wilms).<br>8) <span style=\"color:#51cf66\"><b>Chụp MRI mạch thận</b></span>.<br>→ Nếu tất cả bình thường: <span style=\"color:#ffd43b\"><b>đái máu thoáng qua, theo dõi định kỳ hằng năm</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Đi theo thứ tự nguyên nhân: chuyển hóa (canxi, nước tiểu 24 giờ) → nhiễm trùng (cấy) → mạch máu (Doppler, MRI) → đông máu → sỏi (KUB) → chấn thương, u (CT). Ngoài barem: Adenovirus có thể gây viêm bàng quang xuất huyết ở trẻ.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 5)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B41",
    "track": "barem_goc",
    "type": "basic",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "front": "Triệu chứng thường đi kèm đái máu do bệnh lý <span style=\"color:#74c0fc\"><b>cầu thận</b></span> và do bệnh lý <span style=\"color:#51cf66\"><b>không cầu thận</b></span> theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) Bệnh lý <span style=\"color:#74c0fc\"><b>cầu thận</b></span>: <span style=\"color:#ff6b6b\"><b>phù, cao huyết áp, ban, đau khớp, đau bụng</b></span>...<br>2) Bệnh lý <span style=\"color:#51cf66\"><b>không cầu thận</b></span>: <span style=\"color:#ffd43b\"><b>sốt, đái rắt, đái buốt, đau bụng</b></span>...<br>3) Ngoài ra có triệu chứng toàn thể: chán ăn, mệt mỏi.<br><br><b>💡 Giải thích của AI:</b><br>Đau bụng có mặt ở cả hai nhóm nên không giúp phân biệt. Nhóm cầu thận \"phù – huyết áp – ban – khớp\" gợi ý viêm cầu thận và bệnh hệ thống; nhóm không cầu thận \"sốt – rắt – buốt\" gợi ý nhiễm trùng đường tiểu.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 19, Mục 4 Đặc điểm lâm sàng)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B42",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] Đái máu kèm <span style=\"color:#ff6b6b\"><b>cao huyết áp</b></span> thường gặp trong {{c1::<span style=\"color:#74c0fc\"><b>bệnh cầu thận cấp tính tiên phát hoặc thứ phát, bệnh thận mạn, thận đa nang, thận ứ nước</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Barem lưu ý huyết áp có thể tăng rất cao gây biến chứng suy tim, đôi khi chỉ tăng nhẹ.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Cao huyết áp)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B43",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] Đái máu kèm <span style=\"color:#ff6b6b\"><b>xuất huyết dưới da, niêm mạc, khớp</b></span> nghĩ nhiều đến các bệnh về máu: {{c1::<span style=\"color:#ff6b6b\"><b>xuất huyết giảm tiểu cầu, hemophilia, bạch cầu cấp, suy tủy</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Xuất huyết có thể dạng chấm, nốt, mảng. Riêng xuất huyết cẳng chân dạng đi bốt thì nghĩ Schönlein–Henoch (thẻ riêng).<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 20, Mục 4 Xuất huyết da, niêm)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B44",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "text": "[Barem gốc] Đái máu kèm <span style=\"color:#ff6b6b\"><b>sốt</b></span> hay gặp trong {{c1::<span style=\"color:#74c0fc\"><b>nhiễm khuẩn đường tiểu</b></span>}} (trẻ sơ sinh có thể hạ nhiệt độ); <span style=\"color:#ffd43b\"><b>sốt kéo dài</b></span> không rõ nguyên nhân kèm gầy sút, mệt mỏi, kém ăn có thể là {{c1::<span style=\"color:#ff6b6b\"><b>Lupus ban đỏ</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Ở trẻ sơ sinh nhiễm khuẩn có thể biểu hiện hạ thân nhiệt thay vì sốt, nên không có sốt chưa loại trừ nhiễm khuẩn tiết niệu.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 21, Mục 4 Sốt)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B45",
    "track": "barem_goc",
    "type": "basic",
    "category": "Lâm sàng đái máu",
    "section": "B4",
    "front": "Các <span style=\"color:#74c0fc\"><b>triệu chứng khác</b></span> (thần kinh, hô hấp, tiêu hóa, tiết niệu, cơ quan tạo máu) đi kèm đái máu gợi ý bệnh gì theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Thần kinh</b></span>: viêm cầu thận thể tăng huyết áp (hội chứng não – màng não), Lupus ban đỏ.<br>2) <span style=\"color:#74c0fc\"><b>Hô hấp</b></span>: đái máu nguồn gốc cầu thận; từ viêm đường hô hấp trên đến viêm phổi.<br>3) <span style=\"color:#ffd43b\"><b>Tiêu hóa</b></span>: nhiễm trùng đường tiểu, thận hư, Schönlein–Henoch.<br>4) <span style=\"color:#51cf66\"><b>Tiết niệu</b></span>: thường gặp trong đái máu không cầu thận.<br>5) <span style=\"color:#ff6b6b\"><b>Cơ quan tạo máu</b></span>: Lupus, bạch cầu cấp, suy tủy, xuất huyết giảm tiểu cầu, hemophilia.<br><br><b>💡 Giải thích của AI:</b><br>Mẹo: triệu chứng tiết niệu → nghĩ ngoài cầu thận; triệu chứng thần kinh, hô hấp → nghĩ cầu thận hoặc bệnh hệ thống. Lupus xuất hiện ở cả thần kinh và tạo máu, nhớ Lupus là bệnh \"đa cơ quan\".",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 21, Mục 4 Các triệu chứng khác)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Lam-sang"
    ]
  },
  {
    "id": "PED47-B46",
    "track": "barem_goc",
    "type": "basic",
    "category": "Cận lâm sàng",
    "section": "B5",
    "front": "<span style=\"color:#51cf66\"><b>Xét nghiệm nước tiểu</b></span> trong đái máu đánh giá những gì theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Màu sắc</b></span>: đỏ tươi, hồng, sẫm như nước chè, coca-cola (tùy mức độ và vị trí).<br>2) <span style=\"color:#ffd43b\"><b>Số lượng nước tiểu</b></span>: bình thường, giảm, thiểu niệu, vô niệu.<br>3) <span style=\"color:#74c0fc\"><b>Thành phần</b></span>: hồng cầu rải rác hoặc dày đặc; <span style=\"color:#51cf66\"><b>soi hình dáng hồng cầu</b></span> (biến dạng vs đồng dạng); <span style=\"color:#ff6b6b\"><b>trụ hồng cầu</b></span> (bằng chứng chắc chắn tổn thương cầu thận); <span style=\"color:#51cf66\"><b>protein niệu 24 giờ</b></span> hoặc chỉ số UPr/UCr.<br><br><b>💡 Giải thích của AI:</b><br>Ba câu hỏi khi cầm mẫu nước tiểu: màu gì, bao nhiêu, trong có gì. Phần \"thành phần\" là phần giúp định vị cầu thận hay ngoài cầu thận.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 21-22, Mục 5.1 Xét nghiệm nước tiểu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B47",
    "track": "barem_goc",
    "type": "basic",
    "category": "Cận lâm sàng",
    "section": "B5",
    "front": "Kể tên các <span style=\"color:#51cf66\"><b>xét nghiệm máu</b></span> trong đái máu theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Chức năng thận</b></span>: ure, creatinin.<br>2) <span style=\"color:#51cf66\"><b>Điện giải đồ</b></span>: Na⁺, K⁺, Cl⁻, Ca, Ca²⁺.<br>3) <span style=\"color:#51cf66\"><b>Protein, albumin, lipid, cholesterol</b></span>.<br>4) <span style=\"color:#ffd43b\"><b>ASLO, bổ thể C3, C4</b></span>.<br>5) <span style=\"color:#ffd43b\"><b>Định lượng nồng độ IgA</b></span>.<br>6) <span style=\"color:#ff6b6b\"><b>Đông máu</b></span>: PT, aPTT, fibrinogen.<br>7) <span style=\"color:#ffd43b\"><b>ANA, anti-dsDNA</b></span> nếu nghi Lupus ban đỏ.<br>8) <span style=\"color:#51cf66\"><b>Công thức máu</b></span> (kèm tiểu cầu).<br><br><b>💡 Giải thích của AI:</b><br>Nhớ theo 3 tầng: chức năng (ure, creatinin, điện giải, protein/lipid) → miễn dịch (ASLO, C3, C4, IgA, ANA, anti-dsDNA) → máu (đông máu, công thức máu).",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.2 Xét nghiệm máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B48",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Cận lâm sàng",
    "section": "B5",
    "text": "[Barem gốc] <span style=\"color:#51cf66\"><b>Chẩn đoán hình ảnh</b></span> trong đái máu gồm: {{c1::<span style=\"color:#51cf66\"><b>siêu âm thận – tiết niệu (Doppler mạch thận), X-quang hệ tiết niệu không chuẩn bị (KUB), CT nếu nghi bất thường giải phẫu hoặc khối u</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: siêu âm là lựa chọn đầu tay ở trẻ em vì không nhiễm xạ; CT chỉ dùng khi có chỉ định rõ.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.3 Chẩn đoán hình ảnh)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-B49",
    "track": "barem_goc",
    "type": "basic",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "front": "Ở <span style=\"color:#51cf66\"><b>Bước 2</b></span>, khi có dấu hiệu <span style=\"color:#ff6b6b\"><b>viêm cầu thận cấp</b></span>, barem chỉ định làm những xét nghiệm gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>UPr/UCr</b></span>.<br>2) <span style=\"color:#51cf66\"><b>Ure, creatinin, điện giải, albumin</b></span>.<br>3) <span style=\"color:#ffd43b\"><b>C3, C4</b></span>.<br>4) <span style=\"color:#ffd43b\"><b>ASLO, anti-DNase B</b></span>.<br>5) <span style=\"color:#ff6b6b\"><b>ANA, ANCA</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Bộ xét nghiệm trả lời 3 câu: thận suy tới đâu (UPr/UCr, ure, creatinin, điện giải, albumin); có phải sau nhiễm liên cầu không (C3, C4, ASLO, anti-DNase B); có bệnh tự miễn, viêm mạch không (ANA, ANCA).",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 2)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B50",
    "track": "barem_goc",
    "type": "cloze",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "text": "[Barem gốc] Bước 4 xếp vào nhóm <span style=\"color:#74c0fc\"><b>nguyên nhân tại cầu thận</b></span> khi hồng cầu biến đổi hình thái {{c1::<span style=\"color:#ffd43b\"><b>&gt; 80%</b></span>}} kèm protein niệu (+) và trụ hồng cầu (+).",
    "extra": "<b>💡 Giải thích của AI:</b> Ngoài barem: tài liệu quốc tế còn dùng acanthocyte (hồng cầu hình nhẫn có chồi) ≥ 5% là dấu hiệu rất đặc hiệu của cầu thận (độ đặc hiệu ~98% nhưng độ nhạy chỉ ~52%, Köhler 1991). Khi thi dùng mốc barem &gt; 80%.<br>📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 4); Köhler H et al. Kidney Int 1991;40:115–120 (PMID 1921146)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan",
      "Con-so"
    ]
  },
  {
    "id": "PED47-B51",
    "track": "barem_goc",
    "type": "basic",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "front": "Khi Bước 4 xác định <span style=\"color:#74c0fc\"><b>nguyên nhân tại cầu thận</b></span>, barem chỉ định làm tiếp những gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Ure, creatinin, điện giải đồ</b></span>.<br>2) <span style=\"color:#51cf66\"><b>Protein niệu 24 giờ, C3, C4, IgA</b></span>.<br>3) <span style=\"color:#51cf66\"><b>Siêu âm thận</b></span>.<br>4) <span style=\"color:#ffd43b\"><b>Xét nghiệm nước tiểu bố mẹ, anh chị em</b></span>.<br>5) <span style=\"color:#ffd43b\"><b>Kiểm tra thính học</b></span> (Alport).<br>6) <span style=\"color:#ff6b6b\"><b>Sinh thiết thận</b></span> nếu có chỉ định.<br><br><b>💡 Giải thích của AI:</b><br>Hai mục dễ quên nhất là xét nghiệm nước tiểu người nhà (tìm bệnh màng đáy mỏng, Alport) và đo thính lực (Alport có điếc tiếp nhận). Cả hai rẻ, không xâm lấn và có thể tránh sinh thiết không cần thiết.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ thuật toán Bước 4)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan"
    ]
  },
  {
    "id": "PED47-B52",
    "track": "barem_goc",
    "type": "basic",
    "category": "Định nghĩa đái máu",
    "section": "B1",
    "front": "<span style=\"color:#74c0fc\"><b>Đái máu</b></span> là gì, phân biệt <span style=\"color:#ff6b6b\"><b>đại thể</b></span> và <span style=\"color:#ffd43b\"><b>vi thể</b></span> theo barem?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Đái máu</b></span>: có máu hay hồng cầu trong nước tiểu.<br>2) <span style=\"color:#ff6b6b\"><b>Đại thể</b></span>: phát hiện được bằng mắt thường.<br>3) <span style=\"color:#ffd43b\"><b>Vi thể</b></span>: xác định bằng kính hiển vi khi nước tiểu tươi giữa dòng có ≥ 5 hồng cầu/ml, hoặc trên 3 hồng cầu/vi trường trong mẫu quay ly tâm 10 ml nước tiểu tươi giữa dòng.<br><br><b>💡 Giải thích của AI:</b><br>Hai tiêu chuẩn vi thể tương ứng hai cách làm: soi tươi không ly tâm và soi cặn sau ly tâm. Đơn vị \"/ml\" trong barem nhiều khả năng là lỗi in (chuẩn quốc tế là /µL), nhưng khi thi chép đúng barem.",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 18, Mục 1)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Dinh-nghia"
    ]
  },
  {
    "id": "PED47-E01",
    "track": "ebm",
    "type": "cloze",
    "category": "Ngưỡng đổi màu",
    "section": "E0",
    "text": "[EBM] <span style=\"color:#74c0fc\"><b>Đái máu đại thể</b></span> xảy ra khi chỉ cần {{c1::<span style=\"color:#ffd43b\"><b>1 mL</b></span>}} máu toàn phần hòa tan trong {{c1::<span style=\"color:#ffd43b\"><b>1 lít</b></span>}} nước tiểu đã đủ làm nước tiểu đổi màu mắt thường nhìn thấy rõ.",
    "extra": "<b>💡 Giải thích của AI:</b> Độ nhạy thị giác với hồng cầu rất cao, lượng máu vi thể thất thoát thực tế thường ít hơn rất nhiều so với nỗi hoảng loạn của phụ huynh.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Tong-quan"
    ]
  },
  {
    "id": "PED47-E02",
    "track": "ebm",
    "type": "basic",
    "category": "Định nghĩa EBM",
    "section": "E0",
    "front": "<span style=\"color:#ffd43b\"><b>Tiêu chuẩn tế bào</b></span> và <span style=\"color:#ffd43b\"><b>tiêu chuẩn thời gian</b></span> để chẩn đoán <span style=\"color:#74c0fc\"><b>đái máu vi thể</b></span> theo EBM quốc tế là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tiêu chuẩn tế bào:</b> <span style=\"color:#ffd43b\"><b>&gt; 5 hồng cầu/vi trường</b></span> (400×) trên cặn ly tâm 10 mL nước tiểu tươi, hoặc <span style=\"color:#ffd43b\"><b>≥ 5 hồng cầu/µL</b></span> nước tiểu không ly tâm (buồng đếm).<br>2) <b>Tiêu chuẩn thời gian:</b> xác nhận trên ít nhất <span style=\"color:#ffd43b\"><b>2–3 mẫu nước tiểu</b></span> lấy cách nhau vài tuần.<br><br><b>💡 Giải thích của AI:</b><br>Một mẫu đơn độc có thể chỉ là đái máu thoáng qua do sốt, vận động mạnh hoặc chấn thương nhẹ. ⚖️ Đối chiếu barem: barem dùng \"trên 3 hồng cầu/vi trường\" và \"≥ 5 hồng cầu/ml\" (đơn vị /ml nhiều khả năng là lỗi in của /µL); khi thi viết theo barem.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 22e; Feld LG et al. Pediatrics 1997",
    "asks": [
      "Tiêu chuẩn tế bào",
      "Tiêu chuẩn thời gian"
    ],
    "tags": [
      "PED-47",
      "EBM",
      "Dinh-nghia"
    ]
  },
  {
    "id": "PED47-E03",
    "track": "ebm",
    "type": "basic",
    "category": "Màu sắc nước tiểu",
    "section": "E0",
    "front": "Vì sao <span style=\"color:#74c0fc\"><b>đái máu nguồn gốc cầu thận</b></span> có màu <span style=\"color:#ffd43b\"><b>nước coca-cola</b></span> hoặc <span style=\"color:#ff6b6b\"><b>nước rửa thịt</b></span> mà không có màu đỏ tươi?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thời gian lưu chuyển kéo dài:</b> Hồng cầu lưu lại lâu trong lòng hệ thống ống thận.<br>2) <b>Quá trình toan hóa:</b> Môi trường toan hóa của nước tiểu ở ống lượn xa và ống góp làm oxy hóa <span style=\"color:#74c0fc\"><b>Hemoglobin</b></span> thành <span style=\"color:#ffd43b\"><b>Methemoglobin</b></span> có màu nâu sẫm.<br><br><b>💡 Giải thích của AI:</b><br>Hiện tượng chuyển hóa Hemoglobin thành Methemoglobin trong môi trường toan là dấu chỉ thị sinh hóa kinh điển phân biệt máu chảy từ cuộn mao mạch cầu thận (chảy chậm, qua ống thận toan) với máu từ niệu quản bàng quang (máu tươi, thoát nhanh ra ngoài).",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Mau-sac"
    ]
  },
  {
    "id": "PED47-E04",
    "track": "ebm",
    "type": "basic",
    "category": "Cục máu đông",
    "section": "E0",
    "front": "Vì sao <span style=\"color:#74c0fc\"><b>đái máu cầu thận</b></span> hầu như không có <span style=\"color:#ff6b6b\"><b>cục máu đông (blood clots)</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tác dụng enzyme Urokinase:</b> Tế bào biểu mô ống thận sản xuất <span style=\"color:#51cf66\"><b>Urokinase</b></span> phân hủy sợi fibrin ngay khi vừa hình thành.<br>2) <b>Máu hòa tan từ từ:</b> Hồng cầu rò rỉ rải rác trong thể tích dịch lọc lớn, không đủ fibrinogen tập trung để đông.<br><br><b>💡 Giải thích của AI:</b><br>Quy tắc lâm sàng: thấy cục máu đông trong nước tiểu thì nghĩ trước hết đến chảy máu từ đường dẫn niệu (ngoài cầu thận). Đây là quy tắc gợi ý mạnh chứ không tuyệt đối 100%, nên vẫn cần soi hình dạng hồng cầu.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Co-che"
    ]
  },
  {
    "id": "PED47-E05",
    "track": "ebm",
    "type": "cloze",
    "category": "Que thử Dipstick",
    "section": "E1",
    "text": "[EBM] Que thử Dipstick phát hiện đái máu qua hoạt tính {{c1::<span style=\"color:#51cf66\"><b>pseudoperoxidase của nhân Heme</b></span>}}, có độ nhạy cực cao phát hiện được chỉ từ {{c1::<span style=\"color:#ffd43b\"><b>5 – 10 hồng cầu/µL</b></span>}} nước tiểu.",
    "extra": "<b>💡 Giải thích của AI:</b> Nhân Heme xúc tác phản ứng oxy hóa chất chỉ thị màu trên que thử; tuy nhiên dipstick không phân biệt được Heme trong hồng cầu nguyên vẹn, Hemoglobin tự do hay Myoglobin.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Dipstick"
    ]
  },
  {
    "id": "PED47-E06",
    "track": "ebm",
    "type": "basic",
    "category": "Đái sắc tố",
    "section": "E1",
    "front": "Cách phân biệt nhanh giữa <span style=\"color:#ff6b6b\"><b>Hemoglobin niệu</b></span> (tán huyết) và <span style=\"color:#ff6b6b\"><b>Myoglobin niệu</b></span> (tiêu cơ vân) trên lâm sàng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Quan sát màu huyết tương:</b><br>• <span style=\"color:#ff6b6b\"><b>Hemoglobin:</b></span> Phân tử lớn gắn Haptoglobin làm <span style=\"color:#ff6b6b\"><b>huyết tương có màu hồng/đỏ</b></span>.<br>• <span style=\"color:#ffd43b\"><b>Myoglobin:</b></span> Phân tử nhỏ không gắn Haptoglobin, đào thải nhanh qua thận làm <span style=\"color:#51cf66\"><b>huyết tương trong suốt</b></span>.<br>2) <b>Xét nghiệm men cơ:</b> Myoglobin niệu luôn đi kèm <span style=\"color:#ff6b6b\"><b>CK (Creatine Kinase) máu tăng vọt</b></span> gấp hàng chục đến hàng trăm lần.<br><br><b>💡 Giải thích của AI:</b><br>Trọng lượng phân tử Myoglobin chỉ 17 kDa (rất nhỏ) nên lọc tức thì qua cầu thận làm nước tiểu đỏ nhưng huyết tương hoàn toàn trong; ngược lại Hb (64 kDa) gắn Haptoglobin tích tụ trong máu làm huyết tương nhuộm đỏ.",
    "extra": "📖 Nguồn: Nelson 21st Ch.538; UpToDate: Clinical evaluation of active hematuria in children",
    "tags": [
      "PED-47",
      "EBM",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-E07",
    "track": "ebm",
    "type": "cloze",
    "category": "Đái màu giả tạo",
    "section": "E1",
    "text": "[EBM] Nước tiểu màu đỏ nhưng <span style=\"color:#ffd43b\"><b>Dipstick (-)</b></span> và <span style=\"color:#ffd43b\"><b>Soi (-)</b></span> thường do thực phẩm ({{c1::<span style=\"color:#ff6b6b\"><b>củ dền đỏ</b></span>}}, phẩm màu) hoặc do các thuốc như {{c1::<span style=\"color:#51cf66\"><b>Rifampicin</b></span>}}, Metronidazole.",
    "extra": "<b>💡 Giải thích của AI:</b> Sắc tố Betanin trong củ dền đào thải qua nước tiểu gây màu đỏ giả (Beeturia) khiến người nhà hốt hoảng nhưng dipstick âm tính hoàn toàn vì không chứa nhân Heme.<br>📖 Nguồn: Nelson 21st Ch.538 Table 538.1",
    "tags": [
      "PED-47",
      "EBM",
      "Dipstick"
    ]
  },
  {
    "id": "PED47-E08",
    "track": "ebm",
    "type": "basic",
    "category": "Cờ đỏ cấp cứu RPGN",
    "section": "E1",
    "front": "Đặc điểm <span style=\"color:#ff6b6b\"><b>tam chứng cảnh báo</b></span>, <span style=\"color:#74c0fc\"><b>cơ chế mô học</b></span> và hướng <span style=\"color:#51cf66\"><b>xử trí cấp cứu</b></span> của <span style=\"color:#74c0fc\"><b>Viêm cầu thận tiến triển nhanh (RPGN)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tam chứng cảnh báo:</b> <span style=\"color:#ff6b6b\"><b>Đái máu</b></span> + <span style=\"color:#ffd43b\"><b>Thiểu niệu/vô niệu</b></span> + <span style=\"color:#ffd43b\"><b>Creatinine huyết thanh tăng gấp đôi</b></span> trong vài ngày đến vài tuần.<br>2) <b>Cơ chế mô học:</b> Hoại tử mao mạch cầu thận và <span style=\"color:#74c0fc\"><b>tăng sinh liềm tế bào (Crescents)</b></span> bóp nghẹt khoang Bowman trên ≥ 50% số cầu thận.<br>3) <b>Xử trí cấp cứu:</b> <span style=\"color:#51cf66\"><b>Pulse Methylprednisolone liều cao</b></span> tĩnh mạch ± <span style=\"color:#51cf66\"><b>lọc máu / thay huyết tương</b></span> khẩn cấp.<br><br><b>💡 Giải thích của AI:</b><br>RPGN là một cấp cứu nội thận tối khẩn. Nếu không can thiệp ức chế miễn dịch mạnh mẽ kịp thời trong những ngày đầu, các liềm tế bào sẽ xơ hóa vĩnh viễn dẫn đến suy thận giai đoạn cuối không hồi phục.",
    "extra": "📖 Nguồn: KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases",
    "tags": [
      "PED-47",
      "EBM",
      "Cap-cuu",
      "RPGN"
    ]
  },
  {
    "id": "PED47-E09",
    "track": "ebm",
    "type": "cloze",
    "category": "Hình thái hồng cầu",
    "section": "E2",
    "text": "[EBM] Trong đái máu cầu thận, {{c1::<span style=\"color:#74c0fc\"><b>acanthocyte</b></span>}} (hồng cầu hình nhẫn có các bọng chồi ra như tai chuột Mickey) chiếm ≥ {{c1::<span style=\"color:#ffd43b\"><b>5%</b></span>}} có độ đặc hiệu khoảng 98% cho bệnh cầu thận.",
    "extra": "<b>💡 Giải thích của AI:</b> Độ đặc hiệu cao nhưng độ nhạy chỉ khoảng 52% (một mẫu), nên không thấy acanthocyte chưa loại trừ bệnh cầu thận.<br><b>⚖️ Đối chiếu barem:</b> barem không dùng acanthocyte mà dùng \"hồng cầu biến đổi hình thái &gt; 80%\" ở Bước 4; khi thi ghi mốc &gt; 80%.<br>📖 Nguồn: Köhler H, Wandel E, Brunck B. Acanthocyturia – a characteristic marker for glomerular bleeding. Kidney Int 1991;40:115–120 (PMID 1921146)",
    "tags": [
      "PED-47",
      "EBM",
      "Can-lam-sang",
      "Hinh-thai"
    ]
  },
  {
    "id": "PED47-E10",
    "track": "ebm",
    "type": "basic",
    "category": "Hình thái hồng cầu",
    "section": "E2",
    "front": "Tại sao <span style=\"color:#74c0fc\"><b>hồng cầu từ cầu thận</b></span> lại bị biến dạng đa hình thái (<span style=\"color:#ff6b6b\"><b>Dysmorphic RBCs</b></span>)?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sang chấn cơ học:</b> Hồng cầu bị ép biến dạng khi chui qua các lỗ rách siêu nhỏ của <span style=\"color:#74c0fc\"><b>màng đáy cầu thận</b></span>.<br>2) <b>Stress thẩm thấu và pH:</b> Hồng cầu di chuyển dọc hệ thống ống thận chịu áp lực thẩm thấu dao động dữ dội (từ nhược trương quai Henle đến ưu trương tủy thận) và môi trường toan hóa.<br><br><b>💡 Giải thích của AI:</b><br>Sự kết hợp giữa sang chấn xé cơ học tại màng đáy và sốc thẩm thấu khắc nghiệt trong ống thận làm màng tế bào hồng cầu vỡ nứt, mất đối xứng hình đĩa lõm hai mặt thông thường.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Co-che"
    ]
  },
  {
    "id": "PED47-E11",
    "track": "ebm",
    "type": "basic",
    "category": "Trụ hồng cầu",
    "section": "E2",
    "front": "<span style=\"color:#74c0fc\"><b>Bản chất sinh lý bệnh</b></span> của <span style=\"color:#ff6b6b\"><b>Trụ hồng cầu (RBC Casts)</b></span> và ý nghĩa lâm sàng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất:</b> Hình thành khi các tế bào hồng cầu kết tụ dính vào chất nền glycoprotein <span style=\"color:#74c0fc\"><b>Tamm-Horsfall</b></span> trong lòng ống thận, khi dòng nước tiểu chậm và cô đặc.<br>2) <b>Ý nghĩa lâm sàng:</b> Là bằng chứng <span style=\"color:#51cf66\"><b>rất đặc hiệu</b></span> cho thấy đái máu bắt nguồn từ cầu thận (viêm cầu thận).<br><br><b>💡 Giải thích của AI:</b><br>Trụ niệu chỉ được đúc khuôn trong lòng ống thận, nên trụ hồng cầu gần như loại trừ chảy máu từ niệu quản hay bàng quang. Ngược lại, không thấy trụ hồng cầu chưa loại trừ bệnh cầu thận vì trụ dễ vỡ, dễ bị bỏ sót.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-E12",
    "track": "ebm",
    "type": "cloze",
    "category": "Protein niệu đi kèm",
    "section": "E2",
    "text": "[EBM] Phân biệt protein niệu đi kèm: Đái máu cầu thận thường có protein niệu {{c1::<span style=\"color:#ff6b6b\"><b>đáng kể (UPr/UCr &gt; 0.2 mg/mg)</b></span>}}; đái máu ngoài cầu thận protein niệu chỉ ở mức {{c1::<span style=\"color:#ffd43b\"><b>vết hoặc âm tính</b></span>}} trừ khi có tiểu máu cực kỳ ồ ạt.",
    "extra": "<b>💡 Giải thích của AI:</b> Đái máu đơn độc hoàn toàn không có protein niệu là dấu hiệu đặc trưng giúp bác sĩ tự tin nghĩ tới nguyên nhân đường niệu dưới.<br>📖 Nguồn: UpToDate: Evaluation of microscopic hematuria in children",
    "tags": [
      "PED-47",
      "EBM",
      "Can-lam-sang"
    ]
  },
  {
    "id": "PED47-E13",
    "track": "ebm",
    "type": "basic",
    "category": "APSGN",
    "section": "E3",
    "front": "<span style=\"color:#ffd43b\"><b>Thời gian tiềm tàng (Latent period)</b></span> từ khi nhiễm liên cầu đến khi xuất hiện đái máu trong <span style=\"color:#74c0fc\"><b>APSGN</b></span> là bao lâu?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sau viêm họng do liên cầu:</b> Từ <span style=\"color:#ffd43b\"><b>1 đến 2 tuần</b></span> (trung bình 10 ngày).<br>2) <b>Sau nhiễm trùng da (chốc lở):</b> Từ <span style=\"color:#ffd43b\"><b>3 đến 6 tuần</b></span> (trung bình 3 tuần).<br><br><b>💡 Giải thích của AI:</b><br>Khoảng lặng này là thời gian cần thiết để hệ miễn dịch nhận diện kháng nguyên liên cầu (SPE B), sản sinh kháng thể IgG và hình thành phức hợp miễn dịch lưu hành lắng đọng dưới biểu mô màng đáy cầu thận.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.539",
    "tags": [
      "PED-47",
      "EBM",
      "APSGN",
      "Con-so"
    ]
  },
  {
    "id": "PED47-E14",
    "track": "ebm",
    "type": "cloze",
    "category": "APSGN",
    "section": "E3",
    "text": "[EBM] Trong APSGN, kháng thể {{c1::<span style=\"color:#51cf66\"><b>ASLO</b></span>}} tăng chủ yếu sau viêm họng (độ nhạy 80%), còn sau nhiễm trùng da chốc lở thì xét nghiệm {{c1::<span style=\"color:#51cf66\"><b>Anti-DNase B</b></span>}} có độ nhạy cao hơn hẳn (trên 90%).",
    "extra": "<b>💡 Giải thích của AI:</b> Lipid trên da ức chế tính sinh miễn dịch của Streptolysin O nên hiệu giá ASLO thường thấp sau nhiễm trùng da; Anti-DNase B là xét nghiệm chỉ định chuẩn sau viêm da chốc lở.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.539",
    "tags": [
      "PED-47",
      "EBM",
      "APSGN",
      "Xet-nghiem"
    ]
  },
  {
    "id": "PED47-E15",
    "track": "ebm",
    "type": "basic",
    "category": "Động học C3",
    "section": "E3",
    "front": "<span style=\"color:#ffd43b\"><b>Động học bổ thể C3</b></span> trong <span style=\"color:#74c0fc\"><b>APSGN</b></span> và cạm bẫy lâm sàng cần cảnh giác là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Động học chuẩn:</b> Bổ thể C3 <span style=\"color:#ff6b6b\"><b>giảm sâu trong giai đoạn cấp</b></span> (&gt; 90% ca bệnh) và <span style=\"color:#51cf66\"><b>tự phục hồi về mức bình thường sau 6–8 tuần</b></span>.<br>2) <b>Cạm bẫy lâm sàng:</b> Nếu sau 8 tuần C3 <span style=\"color:#ff6b6b\"><b>vẫn tiếp tục thấp kéo dài</b></span>, bắt buộc phải <span style=\"color:#51cf66\"><b>chỉ định sinh thiết thận</b></span> để loại trừ Viêm cầu thận màng tăng sinh (MPGN) hoặc Viêm thận Lupus.<br><br><b>💡 Giải thích của AI:</b><br>APSGN kích hoạt bổ thể theo con đường nhánh (Alternative pathway). Sự phục hồi C3 là mốc kiểm chứng lâm sàng tối hậu khẳng định tính chất lành tính tự giới hạn của bệnh.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.539",
    "tags": [
      "PED-47",
      "EBM",
      "APSGN",
      "Bo-the"
    ]
  },
  {
    "id": "PED47-E16",
    "track": "ebm",
    "type": "basic",
    "category": "Bệnh thận IgA",
    "section": "E3",
    "front": "Phân biệt <span style=\"color:#ff6b6b\"><b>đái máu đại thể</b></span> trong <span style=\"color:#74c0fc\"><b>Bệnh thận IgA</b></span> với <span style=\"color:#74c0fc\"><b>APSGN</b></span> dựa vào <span style=\"color:#ffd43b\"><b>mốc thời gian</b></span> và <span style=\"color:#51cf66\"><b>bổ thể C3</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Mốc thời gian mọc đái máu:</b><br>• <span style=\"color:#74c0fc\"><b>Bệnh thận IgA:</b></span> Đái máu <span style=\"color:#ffd43b\"><b>đồng thời (1–2 ngày)</b></span> ngay trong đợt sốt viêm đường hô hấp trên.<br>• <span style=\"color:#74c0fc\"><b>APSGN:</b></span> Đái máu xuất hiện muộn sau khoảng lặng <span style=\"color:#ffd43b\"><b>1–2 tuần</b></span> sau viêm họng.<br>2) <b>Bổ thể C3 huyết thanh:</b><br>• <span style=\"color:#74c0fc\"><b>Bệnh thận IgA:</b></span> Bổ thể C3 luôn ở mức <span style=\"color:#51cf66\"><b>bình thường</b></span>.<br>• <span style=\"color:#74c0fc\"><b>APSGN:</b></span> Bổ thể C3 <span style=\"color:#ff6b6b\"><b>giảm thấp rõ rệt</b></span> trong 6–8 tuần đầu.<br><br><b>💡 Giải thích của AI:</b><br>Đây là cặp bệnh cầu thận thường gặp nhất ở trẻ em. Quy tắc 'IgA = đái máu đồng thì + C3 bình thường; APSGN = đái máu hậu nhiễm trùng + C3 tụt sâu' là chìa khóa chẩn đoán phân biệt nhanh tại giường.",
    "extra": "📖 Nguồn: Nelson 21st Ch.538; Wyatt RJ et al. NEJM 2013",
    "tags": [
      "PED-47",
      "EBM",
      "IgA",
      "APSGN"
    ]
  },
  {
    "id": "PED47-E17",
    "track": "ebm",
    "type": "cloze",
    "category": "Bệnh thận IgA",
    "section": "E3",
    "text": "[EBM] <span style=\"color:#74c0fc\"><b>Bệnh thận IgA</b></span> đặc trưng bởi sự lắng đọng phức hợp miễn dịch chứa phân tử {{c1::<span style=\"color:#74c0fc\"><b>IgA1 khiếm khuyết galactose (Gd-IgA1)</b></span>}} tại vùng {{c1::<span style=\"color:#74c0fc\"><b>gian mạch cầu thận (mesangium)</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Giảm galactose hóa chuỗi nhánh O-glycan của IgA1 kích hoạt hệ miễn dịch sinh tự kháng thể IgG chống lại Gd-IgA1, tạo phức hợp miễn dịch kẹt lại ở vùng gian mạch.<br>📖 Nguồn: Wyatt RJ, Julian BA. IgA Nephropathy. N Engl J Med 2013",
    "tags": [
      "PED-47",
      "EBM",
      "IgA",
      "Co-che"
    ]
  },
  {
    "id": "PED47-E18",
    "track": "ebm",
    "type": "cloze",
    "category": "Viêm mạch Henoch",
    "section": "E3",
    "text": "[EBM] Tiêu chuẩn chẩn đoán <span style=\"color:#74c0fc\"><b>viêm mạch IgA (Schönlein–Henoch)</b></span> ở trẻ em (EULAR/PRINTO/PRES 2010): bắt buộc có {{c1::<span style=\"color:#ff6b6b\"><b>ban xuất huyết sờ thấy ưu thế ở chi dưới</b></span>}}, kèm ít nhất 1 trong 4: {{c1::<span style=\"color:#ffd43b\"><b>đau bụng, viêm khớp/đau khớp, tổn thương thận (đái máu, protein niệu), mô bệnh học lắng đọng IgA</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Ban xuất huyết là tiêu chuẩn bắt buộc; đau bụng thường do viêm mạch thành ruột và có thể biến chứng lồng ruột.<br>📖 Nguồn: Ozen S et al. EULAR/PRINTO/PRES criteria. Ann Rheum Dis 2010;69:798–806",
    "tags": [
      "PED-47",
      "EBM",
      "HSP"
    ]
  },
  {
    "id": "PED47-E19",
    "track": "ebm",
    "type": "basic",
    "category": "Bệnh màng đáy mỏng",
    "section": "E3",
    "front": "<span style=\"color:#74c0fc\"><b>Bệnh màng đáy mỏng (Thin Basement Membrane Disease)</b></span>: cơ chế di truyền và <span style=\"color:#51cf66\"><b>tiên lượng lâm sàng</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế di truyền:</b> Đột biến dị hợp tử gen <span style=\"color:#74c0fc\"><b>COL4A3 hoặc COL4A4</b></span> (trội nhiễm sắc thể thường), làm màng đáy cầu thận mỏng lan tỏa.<br>2) <b>Tiên lượng lâm sàng:</b> <span style=\"color:#51cf66\"><b>Phần lớn lành tính</b></span>, chức năng thận bình thường; nhưng <span style=\"color:#ff6b6b\"><b>một số ít</b></span> tiến triển protein niệu, tăng huyết áp, suy thận khi lớn tuổi.<br><br><b>💡 Giải thích của AI:</b><br>Còn gọi là đái máu gia đình lành tính; bố hoặc mẹ thường cũng có đái máu vi thể. Vì có nguy cơ tiến triển nhỏ, xu hướng mới xếp người mang đột biến dị hợp COL4A3/A4 vào phổ \"Alport trội nhiễm sắc thể thường\" và vẫn cần theo dõi huyết áp, protein niệu định kỳ.",
    "extra": "📖 Nguồn: Savige J et al. Expert guidelines for the management of Alport syndrome and thin basement membrane nephropathy. J Am Soc Nephrol 2013;24:364–375 (PMID 23349312); Kashtan CE et al. Kidney Int 2018",
    "asks": [
      "Cơ chế di truyền",
      "Tiên lượng lâm sàng"
    ],
    "tags": [
      "PED-47",
      "EBM",
      "Di-truyen"
    ]
  },
  {
    "id": "PED47-E20",
    "track": "ebm",
    "type": "basic",
    "category": "Hội chứng Alport",
    "section": "E3",
    "front": "<span style=\"color:#ff6b6b\"><b>Tam chứng kinh điển</b></span> của <span style=\"color:#74c0fc\"><b>Hội chứng Alport</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Viêm thận tiến triển</b></span> (đái máu vi thể dai dẳng → protein niệu → suy thận mạn giai đoạn cuối).<br>2) <span style=\"color:#ff6b6b\"><b>Điếc tiếp nhận</b></span> hai bên (khởi đầu ở tần số cao).<br>3) <span style=\"color:#ff6b6b\"><b>Bất thường ở mắt</b></span>: thể thủy tinh hình chóp trước (anterior lenticonus), chấm đốm võng mạc.<br><br><b>💡 Giải thích của AI:</b><br>Bệnh do đột biến collagen type IV (cấu tạo màng đáy cầu thận, ốc tai, bao thể thủy tinh). Khoảng 80% là gen COL4A5 liên kết X (nam nặng hơn nữ); phần còn lại do COL4A3/COL4A4 di truyền lặn hoặc trội nhiễm sắc thể thường.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538.5 Alport Syndrome",
    "tags": [
      "PED-47",
      "EBM",
      "Alport"
    ]
  },
  {
    "id": "PED47-E21",
    "track": "ebm",
    "type": "cloze",
    "category": "Tăng canxi niệu vô căn",
    "section": "E3",
    "text": "[EBM] Tiêu chuẩn chẩn đoán <span style=\"color:#74c0fc\"><b>Tăng canxi niệu vô căn (Idiopathic Hypercalciuria)</b></span> ở trẻ &gt; 2 tuổi là tỷ lệ {{c1::<span style=\"color:#51cf66\"><b>Canxi niệu / Creatinine niệu (UCa/UCr) &gt; 0.2 mg/mg</b></span>}} trên mẫu nước tiểu ngẫu nhiên (hoặc &gt; <span style=\"color:#ffd43b\"><b>4 mg/kg/ngày</b></span> trong nước tiểu 24h).",
    "extra": "<b>💡 Giải thích của AI:</b> Là nguyên nhân ngoài cầu thận không triệu chứng phổ biến nhất ở trẻ em; các vi tinh thể canxi oxalat cọ xát gây xước vi mạch ống thận và đài bể thận.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Con-so"
    ]
  },
  {
    "id": "PED47-E22",
    "track": "ebm",
    "type": "basic",
    "category": "Hội chứng Nutcracker",
    "section": "E3",
    "front": "<span style=\"color:#74c0fc\"><b>Cơ chế bệnh sinh</b></span> và <span style=\"color:#ff6b6b\"><b>biểu hiện lâm sàng</b></span> của <span style=\"color:#74c0fc\"><b>Hội chứng Nutcracker (Kẹp tĩnh mạch thận)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế bệnh sinh:</b> <span style=\"color:#74c0fc\"><b>Tĩnh mạch thận trái</b></span> bị chèn ép khi đi qua khe góc nhọn tạo bởi <span style=\"color:#74c0fc\"><b>Động mạch chủ bụng</b></span> và <span style=\"color:#74c0fc\"><b>Động mạch mạc treo tràng trên</b></span>.<br>2) <b>Biểu hiện lâm sàng:</b> <span style=\"color:#ff6b6b\"><b>Đái máu đại thể hoặc vi thể từng đợt</b></span>, kèm theo <span style=\"color:#ff6b6b\"><b>đau tức vùng mạn sườn trái</b></span>, giãn tĩnh mạch thừng tinh ở trẻ nam.<br><br><b>💡 Giải thích của AI:</b><br>Tương tự như chiếc kẹp hạt dẻ (nutcracker), sự chèn ép làm ứ máu tĩnh mạch thận trái nghiêm trọng, áp lực tăng cao dẫn đến vỡ các nhánh tĩnh mạch mỏng manh quanh đài bể thận vào đường dẫn niệu.",
    "extra": "📖 Nguồn: Kurklinsky AK, Rooke TW. Nutcracker Phenomenon and Nutcracker Syndrome. Mayo Clin Proc 2010",
    "tags": [
      "PED-47",
      "EBM",
      "Nutcracker"
    ]
  },
  {
    "id": "PED47-E23",
    "track": "ebm",
    "type": "cloze",
    "category": "Hồng cầu hình liềm",
    "section": "E3",
    "text": "[EBM] Trẻ mang đặc tính hồng cầu hình liềm (Sickle Cell Trait) có thể bị đái máu đại thể không đau từng đợt do hiện tượng {{c1::<span style=\"color:#ff6b6b\"><b>nhồi máu và hoại tử gai thận (papillary necrosis)</b></span>}} trong môi trường ưu trương toan hóa của tủy thận.",
    "extra": "<b>💡 Giải thích của AI:</b> Tủy thận có nồng độ oxy rất thấp và áp lực thẩm thấu rất cao kích hoạt hồng cầu chứa HbS biến thành hình liềm làm tắc các mạch thẳng vasa recta.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Sickle-cell"
    ]
  },
  {
    "id": "PED47-E24",
    "track": "ebm",
    "type": "basic",
    "category": "Nguyên lý ALARA",
    "section": "E3",
    "front": "<span style=\"color:#51cf66\"><b>Nguyên lý ALARA</b></span> trong chẩn đoán hình ảnh đái máu ở trẻ em quy định chỉ định đầu tay là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Nguyên lý ALARA:</b> 'As Low As Reasonably Achievable' — giảm thiểu tối đa phơi nhiễm bức xạ ion hóa cho cơ thể trẻ em.<br>2) <b>Chỉ định đầu tay:</b> <span style=\"color:#51cf66\"><b>Siêu âm bụng và hệ tiết niệu (Ultrasound)</b></span> luôn là lựa chọn hàng đầu.<br>3) <b>Hạn chế tối đa:</b> Tuyệt đối <span style=\"color:#ff6b6b\"><b>không lạm dụng chụp CT scan bụng</b></span> hoặc chụp X-quang hệ tiết niệu UIV bừa bãi khi chưa có chỉ định ngoại khoa khẩn cấp.<br><br><b>💡 Giải thích của AI:</b><br>Trẻ em có các tế bào đang phân chia mạnh mẽ và nhạy cảm gấp nhiều lần người lớn với tia xạ. Siêu âm 2D kết hợp Doppler có độ nhạy rất cao phát hiện sỏi niệu, u Wilms, viêm thận và tắc mạch mà hoàn toàn không xâm lấn.",
    "extra": "📖 Nguồn: Image Gently Campaign; ACR Appropriateness Criteria: Hematuria - Child",
    "tags": [
      "PED-47",
      "EBM",
      "Chan-doan-hinh-anh",
      "ALARA"
    ]
  },
  {
    "id": "PED47-E25",
    "track": "ebm",
    "type": "cloze",
    "category": "Chỉ định sinh thiết EBM",
    "section": "E4",
    "text": "[EBM] Ngưỡng protein niệu chỉ định sinh thiết thận theo barem là &gt; 1 g/1,73 m²/ngày; còn ngưỡng <span style=\"color:#ff6b6b\"><b>protein niệu thận hư</b></span> ở trẻ em theo KDIGO 2021 là {{c1::<span style=\"color:#ffd43b\"><b>UPr/UCr ≥ 2 mg/mg (≥ 200 mg/mmol)</b></span>}}.",
    "extra": "<b>💡 Giải thích của AI:</b> Hai ngưỡng khác nhau: 1 g/1,73 m²/ngày (≈ 24 mg/m²/giờ) là protein niệu đáng kể; ngưỡng thận hư cao hơn (≥ 40 mg/m²/giờ). Đái máu kèm protein niệu nhiều là dấu hiệu báo động tổn thương cầu thận nặng.<br>📖 Nguồn: KDIGO 2021 Clinical Practice Guideline for Glomerular Diseases",
    "tags": [
      "PED-47",
      "EBM",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-E26",
    "track": "ebm",
    "type": "cloze",
    "category": "Chỉ định sinh thiết EBM",
    "section": "E4",
    "text": "[EBM] Trong viêm cầu thận cấp sau nhiễm liên cầu, bổ thể C3 thường về bình thường sau {{c1::<span style=\"color:#ffd43b\"><b>6 – 8 tuần</b></span>}}; C3 vẫn thấp sau mốc này gợi ý chẩn đoán khác và cần cân nhắc sinh thiết thận.",
    "extra": "<b>💡 Giải thích của AI:</b> C3 thấp dai dẳng hướng tới viêm cầu thận tăng sinh màng / bệnh cầu thận C3 hoặc viêm thận Lupus.<br><b>⚖️ Đối chiếu barem:</b> chỉ định sinh thiết của barem là C3 thấp kéo dài <b>trên 3 tháng</b>; khi thi ghi mốc barem.<br>📖 Nguồn: Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "EBM",
      "Sinh-thiet-than",
      "Con-so"
    ]
  },
  {
    "id": "PED47-E27",
    "track": "ebm",
    "type": "cloze",
    "category": "Chỉ định sinh thiết EBM",
    "section": "E4",
    "text": "[EBM] Mức lọc cầu thận &lt; 60 ml/phút/1,73 m² kéo dài &gt; 3 tháng tương ứng {{c1::<span style=\"color:#ff6b6b\"><b>bệnh thận mạn giai đoạn G3</b></span>}} theo KDIGO.",
    "extra": "<b>💡 Giải thích của AI:</b> Bệnh thận mạn được định nghĩa khi bất thường cấu trúc hoặc chức năng thận kéo dài trên 3 tháng.<br><b>⚖️ Đối chiếu barem:</b> mốc sinh thiết thận của barem là mức lọc cầu thận &lt; <b>80</b> ml/phút/1,73 m², không phải &lt; 60; đừng nhầm hai mốc.<br>📖 Nguồn: KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD",
    "tags": [
      "PED-47",
      "EBM",
      "Sinh-thiet-than"
    ]
  },
  {
    "id": "PED47-E28",
    "track": "ebm",
    "type": "basic",
    "category": "An toàn sinh thiết",
    "section": "E4",
    "front": "<span style=\"color:#ffd43b\"><b>4 điều kiện an toàn bắt buộc</b></span> phải kiểm tra trước khi thực hiện <span style=\"color:#51cf66\"><b>sinh thiết thận</b></span> ở trẻ em?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Đông cầm máu:</b> <span style=\"color:#51cf66\"><b>tiểu cầu, PT, aPTT bình thường</b></span> (nhiều cơ sở yêu cầu tiểu cầu &gt; 100.000/µL); ngừng thuốc chống đông, chống ngưng tập tiểu cầu.<br>2) <b>Kiểm soát huyết áp:</b> <span style=\"color:#51cf66\"><b>huyết áp được kiểm soát</b></span> trước thủ thuật.<br>3) <b>Giải phẫu thận:</b> siêu âm xác định <span style=\"color:#74c0fc\"><b>có 2 thận</b></span>, kích thước và vị trí phù hợp, không có nang lớn hay thận ứ nước nặng tại vị trí chọc.<br>4) <b>Không có nhiễm trùng:</b> không nhiễm khuẩn huyết hoặc nhiễm trùng da tại vị trí chọc kim.<br><br><b>💡 Giải thích của AI:</b><br>Thận nhận khoảng 20% cung lượng tim nên biến chứng chính của sinh thiết là chảy máu; tăng huyết áp chưa kiểm soát và rối loạn đông máu làm tăng nguy cơ này. Ngưỡng tiểu cầu cụ thể khác nhau giữa các cơ sở.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 22e; thực hành sinh thiết thận qua da ở trẻ em (ngưỡng xét nghiệm tùy cơ sở)",
    "tags": [
      "PED-47",
      "EBM",
      "Sinh-thiet-than",
      "An-toan"
    ]
  },
  {
    "id": "PED47-E29",
    "track": "ebm",
    "type": "basic",
    "category": "Thực chiến 5 bước",
    "section": "E5",
    "front": "Trong <span style=\"color:#74c0fc\"><b>thuật toán 5 bước thực chiến</b></span>, sau khi khẳng định <span style=\"color:#ff6b6b\"><b>đái máu thực sự</b></span> (Bước 1), Bước 2 phải sàng lọc ngay <span style=\"color:#74c0fc\"><b>hội chứng gì</b></span> và chỉ định <span style=\"color:#51cf66\"><b>xét nghiệm khẩn nào</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Hội chứng cần sàng lọc:</b> <span style=\"color:#74c0fc\"><b>viêm cầu thận cấp</b></span>, khám tìm <span style=\"color:#ff6b6b\"><b>phù</b></span>, <span style=\"color:#ff6b6b\"><b>tăng huyết áp</b></span>, <span style=\"color:#ffd43b\"><b>đái ít</b></span>.<br>2) <b>Xét nghiệm khẩn:</b> <span style=\"color:#51cf66\"><b>UPr/UCr, ure, creatinin, điện giải, albumin</b></span>; <span style=\"color:#51cf66\"><b>C3, C4, ASLO, anti-DNase B</b></span>; <span style=\"color:#51cf66\"><b>ANA, ANCA</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Viêm cầu thận cấp có nguy cơ suy thận cấp, phù phổi cấp hoặc bệnh não do tăng huyết áp trong những ngày đầu nên phải xử lý trước mọi thăm dò sâu khác. Danh sách xét nghiệm trên khớp với Bước 2 của barem.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Thuc-chien"
    ]
  },
  {
    "id": "PED47-E30",
    "track": "ebm",
    "type": "basic",
    "category": "Đái máu vi thể đơn độc",
    "section": "E5",
    "front": "Ở trẻ có <span style=\"color:#74c0fc\"><b>đái máu vi thể đơn độc không triệu chứng</b></span> (Asymptomatic Microscopic Hematuria), bước tiếp cận chuẩn tiếp theo là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Xét nghiệm nước tiểu gia đình:</b> tổng phân tích nước tiểu của <span style=\"color:#74c0fc\"><b>bố mẹ, anh chị em</b></span> (sàng lọc bệnh màng đáy mỏng, Alport).<br>2) <b>Sàng lọc chuyển hóa:</b> <span style=\"color:#51cf66\"><b>tỷ lệ canxi/creatinin niệu</b></span> (tăng canxi niệu).<br>3) <b>Chiến lược theo dõi:</b> nếu không có protein niệu, tăng huyết áp hay suy thận → <span style=\"color:#51cf66\"><b>theo dõi định kỳ huyết áp, nước tiểu</b></span>, không làm thủ thuật xâm lấn.<br><br><b>💡 Giải thích của AI:</b><br>Đái máu vi thể đơn độc không có protein niệu thường có tiên lượng tốt; nhiều trường hợp tự hết. Dấu hiệu cần thăm dò sâu: xuất hiện protein niệu, tăng huyết áp, giảm mức lọc cầu thận hoặc đái máu đại thể.",
    "extra": "📖 Nguồn: Nelson 21st Ch.538; Feld LG et al. Pediatrics 1997",
    "tags": [
      "PED-47",
      "EBM",
      "Tiep-can"
    ]
  },
  {
    "id": "PED47-E31",
    "track": "ebm",
    "type": "cloze",
    "category": "Tăng canxi niệu",
    "section": "E5",
    "text": "[EBM] Trong thuật toán tiếp cận nguyên nhân ngoài cầu thận, xét nghiệm định lượng tỷ lệ {{c1::<span style=\"color:#51cf66\"><b>Canxi/Creatinine niệu (UCa/UCr)</b></span>}} là công cụ sàng lọc đầu tay để phát hiện sớm bệnh lý <span style=\"color:#74c0fc\"><b>Tăng canxi niệu vô căn</b></span> trước khi sỏi cản quang hình thành trên phim chụp.",
    "extra": "<b>💡 Giải thích của AI:</b> Phát hiện sớm tăng canxi niệu giúp can thiệp bằng điều chỉnh chế độ ăn uống (uống nhiều nước, hạn chế muối natri) trước khi kết tinh thành sỏi thận lớn.<br>📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Thuc-chien"
    ]
  },
  {
    "id": "PED47-E32",
    "track": "ebm",
    "type": "basic",
    "category": "Đối chiếu thuật ngữ",
    "section": "E6",
    "front": "Barem giáo trình ghi thuật ngữ <span style=\"color:#ff6b6b\"><b>'Bệnh móng màng đáy'</b></span> — bản chất EBM quốc tế là gì và cách viết bài thi tự luận đạt điểm tối đa?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất EBM:</b> Đây là lỗi in ấn tài liệu cho thuật ngữ <span style=\"color:#74c0fc\"><b>Bệnh màng đáy mỏng (Thin Basement Membrane Disease - TBMD)</b></span> hoặc Đái máu gia đình lành tính.<br>2) <b>Cách viết bài thi:</b> Ghi rõ: <span style=\"color:#51cf66\"><b>'Bệnh màng đáy mỏng (sách gốc in nhầm là móng màng đáy)'</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Viết như vậy vừa thể hiện sự tôn trọng tuyệt đối đáp án chấm thi của Bộ môn vừa chứng minh kiến thức chuyên môn chính xác theo danh pháp quốc tế.",
    "extra": "📖 Nguồn: Đối chiếu Barem Nhi YTB trang 18 & Nelson 21st Ch.538.4",
    "tags": [
      "PED-47",
      "EBM",
      "Rosetta"
    ]
  },
  {
    "id": "PED47-E33",
    "track": "ebm",
    "type": "basic",
    "category": "Đối chiếu thuật ngữ",
    "section": "E6",
    "front": "Barem giáo trình ghi thuật ngữ <span style=\"color:#ff6b6b\"><b>'Scholein Henoch'</b></span> — danh pháp quốc tế hiện đại là gì và cơ chế miễn dịch?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Danh pháp hiện đại:</b> <span style=\"color:#74c0fc\"><b>Viêm mạch IgA (IgA Vasculitis - IgAV)</b></span> theo đồng thuận Hội nghị Quốc tế Chapel Hill 2012.<br>2) <b>Cơ chế miễn dịch:</b> Viêm các mạch máu nhỏ qua trung gian lắng đọng phức hợp miễn dịch chứa <span style=\"color:#74c0fc\"><b>kháng thể IgA1</b></span> tại da, khớp, ruột và thận.<br><br><b>💡 Giải thích của AI:</b><br>Danh pháp mới thay thế tên riêng Scholein-Henoch bằng bản chất cơ chế bệnh học miễn dịch của bệnh, đồng bộ với phân loại quốc tế hiện hành.",
    "extra": "📖 Nguồn: 2012 Revised International Chapel Hill Consensus Conference Nomenclature of Vasculitides",
    "tags": [
      "PED-47",
      "EBM",
      "Rosetta"
    ]
  },
  {
    "id": "PED47-E34",
    "track": "ebm",
    "type": "basic",
    "category": "Đối chiếu thuật ngữ",
    "section": "E6",
    "front": "Barem ghi <span style=\"color:#74c0fc\"><b>'Đái máu do tập thể dục'</b></span> — bản chất lâm sàng và nghiệm pháp xác nhận là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất lâm sàng:</b> <span style=\"color:#74c0fc\"><b>Đái máu do gắng sức (Exercise-induced hematuria)</b></span>, xuất hiện sau vận động cường độ cao (chạy marathon, bóng đá).<br>2) <b>Nghiệm pháp xác nhận:</b> Cho bệnh nhi <span style=\"color:#51cf66\"><b>nghỉ ngơi hoàn toàn tại giường trong 48–72 giờ</b></span> rồi xét nghiệm lại nước tiểu; nước tiểu sẽ <span style=\"color:#51cf66\"><b>hồi phục âm tính hoàn toàn</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Cơ chế do thiếu máu cục bộ thoáng qua ở thận kết hợp sang chấn cơ học cọ xát đáy bàng quang rỗng khi chạy nhảy. Bệnh hoàn toàn vô hại và không đòi hỏi thăm dò chuyên sâu nếu tự thoái lui sau nghỉ ngơi.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Rosetta"
    ]
  },
  {
    "id": "PED47-E35",
    "track": "ebm",
    "type": "basic",
    "category": "Đối chiếu thuật ngữ",
    "section": "E6",
    "front": "<span style=\"color:#ff6b6b\"><b>'Factitious hematuria' (Đái máu giả tạo)</b></span> là gì và cách xử trí xác nhận trên lâm sàng?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất:</b> Bệnh nhân (hoặc người chăm sóc trong hội chứng Munchausen by proxy) <span style=\"color:#ff6b6b\"><b>tự cho máu hoặc chất màu vào lọ nước tiểu</b></span> để giả bệnh.<br>2) <b>Cách xác nhận lâm sàng:</b> Cho nhân viên y tế <span style=\"color:#51cf66\"><b>trực tiếp giám sát lấy mẫu nước tiểu tươi</b></span> tại buồng vệ sinh hoặc thực hiện đặt sonde bàng quang lấy mẫu trực tiếp.<br><br><b>💡 Giải thích của AI:</b><br>Nghi ngờ khi có sự bất tương xứng hoàn toàn giữa kết quả đái máu đại thể ồ ạt với tình trạng lâm sàng bình thường, công thức máu không giảm và không có bất kỳ tổn thương thận nào trên chẩn đoán hình ảnh.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Rosetta"
    ]
  },
  {
    "id": "PED47-E36",
    "track": "ebm",
    "type": "basic",
    "category": "Cạm bẫy sinh tử",
    "section": "E7",
    "front": "Cạm bẫy: <span style=\"color:#51cf66\"><b>Que thử Dipstick dương tính 3+ với máu</b></span> — vì sao không được vội vàng kết luận đái máu và ảnh hưởng gì đến hướng <span style=\"color:#51cf66\"><b>điều trị</b></span> cấp cứu?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Lý do:</b> Dipstick chỉ phát hiện nhân heme, không phân biệt được hồng cầu nguyên vẹn với <span style=\"color:#ff6b6b\"><b>hemoglobin tự do (tán huyết)</b></span> hoặc <span style=\"color:#ff6b6b\"><b>myoglobin (tiêu cơ vân)</b></span>.<br>2) <b>Hành động bắt buộc:</b> phải <span style=\"color:#51cf66\"><b>soi cặn nước tiểu dưới kính hiển vi</b></span>; chỉ kết luận đái máu khi thấy hồng cầu.<br><br><b>💡 Giải thích của AI:</b><br>Nhầm tiêu cơ vân (sau co giật, chấn thương, viêm cơ) thành đái máu sẽ làm chậm bù dịch tích cực để bảo vệ ống thận. Đây chính là nhánh \"que thử (+), soi tươi (−)\" ở Bước 1 của barem.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "EBM",
      "Cam-bay"
    ]
  },
  {
    "id": "PED47-E37",
    "track": "ebm",
    "type": "basic",
    "category": "Cạm bẫy sinh tử",
    "section": "E7",
    "front": "Cạm bẫy: Vì sao không bao giờ được chẩn đoán <span style=\"color:#74c0fc\"><b>đái máu vi thể bệnh lý</b></span> chỉ dựa trên <span style=\"color:#ffd43b\"><b>một mẫu nước tiểu duy nhất</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Lý do:</b> đái máu vi thể thoáng qua rất hay gặp: khoảng <span style=\"color:#ffd43b\"><b>3–4%</b></span> trẻ đi học có hồng cầu niệu ở một mẫu, nhưng chỉ khoảng <span style=\"color:#ffd43b\"><b>1%</b></span> còn dương tính khi xét nghiệm lặp lại; nguyên nhân thoáng qua: <span style=\"color:#ffd43b\"><b>sốt, vận động mạnh, chấn thương nhẹ</b></span>.<br>2) <b>Quy tắc chẩn đoán:</b> lặp lại xét nghiệm trên <span style=\"color:#ffd43b\"><b>2–3 mẫu nước tiểu cách nhau vài tuần</b></span>; chỉ thăm dò sâu khi hồng cầu niệu dai dẳng.<br><br><b>💡 Giải thích của AI:</b><br>Khớp với Bước 3 của barem: đái máu vi thể đơn độc → làm lại xét nghiệm nước tiểu hằng tuần trong 2 tuần, không tập thể dục. Tránh làm hàng loạt xét nghiệm, chụp chiếu cho một trẻ khỏe mạnh chỉ vì một mẫu bất thường.",
    "extra": "📖 Nguồn: Dodge WF et al. Proteinuria and hematuria in schoolchildren. J Pediatr 1976;88:327–347; Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "EBM",
      "Cam-bay"
    ]
  },
  {
    "id": "PED47-E38",
    "track": "ebm",
    "type": "basic",
    "category": "Cạm bẫy sinh tử",
    "section": "E7",
    "front": "Cạm bẫy: Trẻ có đái máu vi thể đơn độc, việc <span style=\"color:#ff6b6b\"><b>bỏ qua xét nghiệm nước tiểu của bố mẹ</b></span> dẫn đến hậu quả gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Hậu quả:</b> Bỏ sót chẩn đoán <span style=\"color:#74c0fc\"><b>Bệnh màng đáy mỏng (Thin Basement Membrane Disease)</b></span> hoặc <span style=\"color:#74c0fc\"><b>Hội chứng Alport giai đoạn sớm</b></span>.<br>2) <b>Ý nghĩa lâm sàng:</b> Nếu bố hoặc mẹ có đái máu vi thể không triệu chứng → định hướng ngay bệnh di truyền, <span style=\"color:#51cf66\"><b>giúp tránh được chỉ định sinh thiết thận không cần thiết</b></span> cho trẻ.<br><br><b>💡 Giải thích của AI:</b><br>Xét nghiệm nước tiểu cho bố mẹ là một 'nghiệm pháp sinh thiết không xâm lấn' rẻ tiền nhưng cực kỳ giá trị trong tiếp cận đái máu vi thể gia đình ở trẻ em.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538",
    "tags": [
      "PED-47",
      "EBM",
      "Cam-bay"
    ]
  },
  {
    "id": "PED47-E39",
    "track": "ebm",
    "type": "basic",
    "category": "Cạm bẫy sinh tử",
    "section": "E7",
    "front": "Cạm bẫy: Trẻ chẩn đoán viêm cầu thận cấp hậu liên cầu (APSGN), <span style=\"color:#51cf66\"><b>điều kiện tiên quyết nào</b></span> để xác nhận chẩn đoán cuối cùng trước khi cho kết thúc theo dõi?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Điều kiện tiên quyết:</b> <span style=\"color:#ffd43b\"><b>bổ thể C3 phải trở về bình thường</b></span>, thường trong <span style=\"color:#ffd43b\"><b>6 – 8 tuần</b></span>.<br>2) <b>Hành động khi C3 không hồi phục:</b> <span style=\"color:#ff6b6b\"><b>xem lại chẩn đoán</b></span> và cân nhắc <span style=\"color:#51cf66\"><b>sinh thiết thận</b></span> để tìm viêm cầu thận tăng sinh màng / bệnh cầu thận C3 hoặc viêm thận Lupus.<br><br><b>💡 Giải thích của AI:</b><br>Nhiều ca viêm cầu thận tăng sinh màng hoặc Lupus giai đoạn đầu giống hệt viêm cầu thận cấp sau nhiễm liên cầu, nên không kết thúc theo dõi khi chưa có C3 bình thường. ⚖️ Đối chiếu barem: chỉ định sinh thiết của barem là C3 thấp kéo dài <b>trên 3 tháng</b>.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 22e",
    "tags": [
      "PED-47",
      "EBM",
      "Cam-bay"
    ]
  },
  {
    "id": "PED47-B29-ALL",
    "track": "barem_goc",
    "type": "basic",
    "category": "Chỉ định sinh thiết thận",
    "section": "B5",
    "front": "Kể tên <span style=\"color:#ffd43b\"><b>7 chỉ định sinh thiết thận kinh điển</b></span> ở trẻ em đái máu theo giáo trình Nhi Thái Bình?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Protein niệu</b></span> &gt; <span style=\"color:#ffd43b\"><b>1 g/1,73 m²/ngày</b></span>.<br>2) <span style=\"color:#ffd43b\"><b>Bổ thể C3 thấp kéo dài</b></span> trên <span style=\"color:#ffd43b\"><b>3 tháng</b></span>.<br>3) <span style=\"color:#ff6b6b\"><b>Mức lọc cầu thận giảm</b></span> &lt; <span style=\"color:#ffd43b\"><b>80 ml/phút/1,73 m²</b></span>.<br>4) <span style=\"color:#74c0fc\"><b>Viêm thận Lupus, viêm thận Schönlein–Henoch</b></span>.<br>5) <span style=\"color:#74c0fc\"><b>Tiền sử gia đình</b></span> có bệnh thận nghi ngờ hội chứng Alport.<br>6) <span style=\"color:#ff6b6b\"><b>Đái máu đại thể tái phát</b></span> mà không rõ nguyên nhân.<br>7) <span style=\"color:#74c0fc\"><b>Đái máu do cầu thận</b></span> mà gia đình thiết tha muốn biết nguyên nhân và tiên lượng, mặc dù protein niệu không cao.<br><br><b>💡 Giải thích của AI:</b><br>Mẹo nhớ: 3 con số (protein 1 g – C3 3 tháng – mức lọc 80) + 2 bệnh (Lupus, Henoch) + 1 gia đình Alport + 2 kiểu đái máu (đại thể tái phát; cầu thận mà gia đình muốn biết).",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 22, Mục 5.4 Chỉ định sinh thiết thận)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Sinh-thiet-than",
      "Chi-dinh-tong-quan"
    ]
  },
  {
    "id": "PED47-B36-ALL",
    "track": "barem_goc",
    "type": "basic",
    "category": "Thuật toán tiếp cận",
    "section": "B6",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-algo",
    "front": "Trình bày sơ đồ <span style=\"color:#51cf66\"><b>5 bước tiếp cận bệnh nhân đái máu</b></span> theo giáo trình Nhi Thái Bình?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Bước 1 – Xác định đái máu</b></span>: que thử + soi kính hiển vi. Que thử (+), soi tươi (−) → tìm huyết sắc tố niệu (Hb hoặc myoglobin niệu).<br>2) <span style=\"color:#ff6b6b\"><b>Bước 2 – Tìm dấu hiệu viêm cầu thận cấp</b></span> (phù, tăng HA, đái ít). Có → chẩn đoán viêm cầu thận cấp và làm xét nghiệm.<br>3) <span style=\"color:#74c0fc\"><b>Bước 3 – Phân loại lâm sàng</b></span>: đại thể → loại trừ gắng sức; vi thể đơn độc → làm lại nước tiểu hằng tuần trong 2 tuần (không tập thể dục).<br>4) <span style=\"color:#ffd43b\"><b>Bước 4 – Soi hình dáng hồng cầu và định lượng protein/creatinin niệu</b></span> → tại cầu thận hay ngoài cầu thận.<br>5) <span style=\"color:#51cf66\"><b>Bước 5 – Tìm nguyên nhân ngoài cầu thận</b></span>; tất cả bình thường → đái máu thoáng qua, theo dõi hằng năm.<br><br><b>💡 Giải thích của AI:</b><br>Mẹo: \"Có thật không → Có cấp không → Có kéo dài không → Ở đâu → Do gì\". Lưu ý Bước 5 của barem là tìm nguyên nhân ngoài cầu thận, không phải \"điều trị\".",
    "extra": "📖 Nguồn: Giáo trình Nhi YTB (Trang 23, Sơ đồ tiếp cận bệnh nhân đái máu)",
    "tags": [
      "PED-47",
      "Barem-goc",
      "Thuat-toan-5-buoc"
    ]
  },
  {
    "id": "PED47-ALG-01",
    "track": "ebm",
    "type": "basic",
    "section": "E7",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Thuật toán 30 giây:</b></span> Phân biệt tức thì <span style=\"color:#ff6b6b\"><b>Đái máu thật</b></span> vs <span style=\"color:#ffd43b\"><b>Đái máu giả</b></span> tại phòng cấp cứu bằng que thử Dipstick và soi cặn lắng?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ffd43b\"><b>KỊCH BẢN 1 (nước tiểu đỏ + dipstick ÂM TÍNH):</b></span> → <span style=\"color:#51cf66\"><b>không phải heme</b></span>: sắc tố thực phẩm (củ dền), thuốc (rifampicin, metronidazol), tinh thể urat ở trẻ nhỏ. Hiếm khi cần thăm dò thận.<br>• <span style=\"color:#ffd43b\"><b>KỊCH BẢN 2 (dipstick DƯƠNG TÍNH nhưng soi KHÔNG CÓ HỒNG CẦU):</b></span> → đái sắc tố: <span style=\"color:#ff6b6b\"><b>hemoglobin tự do</b></span> (tán huyết nội mạch) hoặc <span style=\"color:#ff6b6b\"><b>myoglobin</b></span> (tiêu cơ vân). Xử trí: bù dịch tích cực bảo vệ ống thận, tìm nguyên nhân.<br>• <span style=\"color:#ff6b6b\"><b>KỊCH BẢN 3 (dipstick DƯƠNG TÍNH + soi CÓ HỒNG CẦU):</b></span> → <span style=\"color:#ff6b6b\"><b>ĐÁI MÁU THẬT SỰ</b></span>, phân loại cầu thận hay ngoài cầu thận.<br><br><b>💡 Giải thích của AI:</b><br>Kịch bản 2 và 3 chính là Bước 1 của sơ đồ barem. Lưu ý: vitamin C liều cao có thể làm dipstick âm tính giả, nên nước tiểu đỏ mà dipstick âm vẫn nên soi kính hiển vi nếu nghi ngờ.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.538 (PED-47, Thuật toán quyết định)",
    "tags": [
      "PED-47",
      "Thuat-toan",
      "Dai-mau-that-gia"
    ]
  },
  {
    "id": "PED47-ALG-02",
    "track": "ebm",
    "type": "basic",
    "section": "E7",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Ma trận quyết định nhị phân:</b></span> Bảng 5 tiêu chí phân định tức thì <span style=\"color:#74c0fc\"><b>Đái máu tại cầu thận</b></span> vs <span style=\"color:#51cf66\"><b>Đái máu ngoài cầu thận</b></span> tại giường bệnh là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ffd43b\"><b>Màu sắc nước tiểu:</b></span> cầu thận → nâu sẫm, coca-cola, nước chè; ngoài cầu thận → đỏ tươi, hồng.<br>2) <span style=\"color:#ffd43b\"><b>Máu cục:</b></span> cầu thận → <span style=\"color:#51cf66\"><b>hầu như không có</b></span> (urokinase ống thận làm tan fibrin); ngoài cầu thận → <span style=\"color:#ff6b6b\"><b>có thể có máu cục</b></span>.<br>3) <span style=\"color:#ffd43b\"><b>Protein niệu đi kèm:</b></span> cầu thận → <span style=\"color:#ff6b6b\"><b>có (UPr/UCr &gt; 0,2 mg/mg)</b></span>; ngoài cầu thận → âm tính hoặc vết.<br>4) <span style=\"color:#ffd43b\"><b>Hình thái hồng cầu:</b></span> cầu thận → <span style=\"color:#ff6b6b\"><b>biến đổi hình thái &gt; 80%</b></span> (mốc barem); ngoài cầu thận → <span style=\"color:#51cf66\"><b>đồng dạng</b></span>.<br>5) <span style=\"color:#ffd43b\"><b>Trụ hồng cầu:</b></span> cầu thận → <span style=\"color:#ff6b6b\"><b>DƯƠNG TÍNH</b></span> (bằng chứng chắc chắn); ngoài cầu thận → <span style=\"color:#51cf66\"><b>ÂM TÍNH</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Mục 3–5 là tiêu chuẩn Bước 4 của barem. Ngoài barem: acanthocyte ≥ 5% rất đặc hiệu cho cầu thận (Köhler 1991). Cầu thận → chuyển chuyên khoa thận nhi; ngoài cầu thận → thăm dò tiết niệu, ngoại nhi.",
    "extra": "📖 Nguồn: Nelson 21st Ch.538 & Harriet Lane Handbook (PED-47, Thuật toán quyết định)",
    "tags": [
      "PED-47",
      "Thuat-toan",
      "Phan-dinh-cau-than"
    ]
  }
]
