# -*- coding: utf-8 -*-
"""
ped63_cards_data.py
Bộ dữ liệu thẻ Anki Master cho PED-63: Biến thiên công thức bạch cầu theo tuổi & Nhận định Nhiễm trùng vs Virus.
Tuân thủ 100% Medical Flashcard Governance (52 Master Basic cards across B0-B9 incl. Fast Decision Algorithms).
"""

cards_data = [
  {
    "id": "PED63-B0-01",
    "type": "basic",
    "section": "B0",
    "category": "Nguyên lý tạo máu nhi khoa",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#ffd43b\"><b>3 lý do cốt tử</b></span> vì sao bác sĩ lâm sàng Nhi khoa tuyệt đối không được áp dụng <span style=\"color:#ff6b6b\"><b>khoảng tham chiếu công thức bạch cầu của người lớn</b></span> cho trẻ em?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Khoảng tham chiếu máy in sẵn là của người lớn:</b></span> Các máy đếm huyết học tự động thường cài mặc định chuẩn người lớn (Neutrophil 60% – 70%, Lymphocyte 20% – 30%); nếu áp vào trẻ dưới 5 tuổi sẽ chẩn đoán nhầm thành 'suy tủy' hoặc 'giảm bạch cầu đa nhân bệnh lý'.<br>2) <span style=\"color:#ffd43b\"><b>Ảo tưởng về tỷ lệ phần trăm (%):</b></span> Tỷ lệ % chỉ mang tính tương đối; một trẻ có Neutrophil 25% nhưng tổng bạch cầu 30.000/mm³ thì số lượng tuyệt đối ANC lên tới 7.500/mm³ (đang tăng bạch cầu hạt dữ dội).<br>3) <span style=\"color:#74c0fc\"><b>Bỏ sót dấu ấn vi thể trên lam máu:</b></span> Máy đếm laser tự động không nhận diện được các biến đổi hình thái học sinh tử: hạt độc tính, không bào, thể Döhle hay tỷ lệ tế bào non (chuyển trái).<br><br><b>💡 Giải thích của AI:</b><br>Hệ tạo máu của trẻ em là một thực thể động (Dynamic System) biến đổi liên tục theo từng mốc phát triển. Áp đặt tiêu chuẩn người lớn lên trẻ em là một trong những nguyên nhân phổ biến nhất dẫn tới các chỉ định chọc tủy hoặc dùng kháng sinh sai lầm.",
    "extra": "📖 Nguồn: Giáo trình Nhi khoa ĐHYHN & Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 0.1)",
    "tags": [
      "PED-63",
      "B0-Nguyen-ly",
      "EBM-Master"
    ]
  },
  {
    "id": "PED63-B0-02",
    "type": "basic",
    "section": "B0",
    "category": "Nguyên lý tạo máu nhi khoa",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Bản chất của <span style=\"color:#74c0fc\"><b>hệ miễn dịch động (Dynamic System)</b></span> và đặc điểm <span style=\"color:#ffd43b\"><b>dự trữ tủy xương của trẻ nhỏ</b></span> so với người lớn là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Hệ miễn dịch động:</b> Trẻ chuyển đổi từ trạng thái được mẹ bảo vệ thụ động qua nhau thai sang tự đối đầu với thế giới kháng nguyên phong phú của môi trường bên ngoài.<br>2) <b>Dự trữ tủy xương thấp nhưng huy động cực nhanh:</b> Dung tích tủy tạo máu ở trẻ nhỏ gần như chiếm trọn toàn bộ tủy xương (tủy đỏ chiếm ưu thế), <span style=\"color:#ffd43b\"><b>nguồn dự trữ bạch cầu hạt trưởng thành (Storage pool) hạn chế hơn người lớn</b></span>.<br>3) <b>Hậu quả khi nhiễm khuẩn nặng:</b> Tủy xương nhanh chóng bị cạn kiệt nguồn dự trữ, buộc phải giải phóng ồ ạt các tế bào non ra máu ngoại vi (gây hiện tượng chuyển trái mạnh mẽ), hoặc thậm chí tụt giảm bạch cầu trong sốc nhiễm khuẩn.<br><br><b>💡 Giải thích của AI:</b><br>Vì kho dự trữ hạn chế, trẻ sơ sinh và trẻ nhỏ khi nhiễm khuẩn nặng có thể cạn kiệt bạch cầu trung tính chỉ sau 24-48 giờ, biểu hiện bằng hạ bạch cầu thay vì tăng bạch cầu như ở trẻ lớn và người lớn.",
    "extra": "📖 Nguồn: Nathan and Oski's Hematology and Oncology of Infancy and Childhood (PED-63, Mục 0.1)",
    "tags": [
      "PED-63",
      "B0-Nguyen-ly",
      "Tuy-xuong"
    ]
  },
  {
    "id": "PED63-B0-03",
    "type": "basic",
    "section": "B0",
    "category": "Nguyên lý tạo máu nhi khoa",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Tại sao <span style=\"color:#51cf66\"><b>Số lượng tuyệt đối (Absolute Count)</b></span> luôn luôn là <span style=\"color:#ffd43b\"><b>chân lý tối cao</b></span> và vượt trội hơn <span style=\"color:#ff6b6b\"><b>Tỷ lệ phần trăm (%)</b></span> trong công thức bạch cầu nhi khoa?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tỷ lệ % là một phân số phụ thuộc:</b> Tỷ lệ % của một dòng tế bào có thể tăng hoặc giảm giả tạo do sự thay đổi số lượng của các dòng tế bào khác đi kèm.<br>2) <b>Số lượng tuyệt đối phản ánh thực tế khối tế bào chức năng:</b> Chỉ có số lượng tuyệt đối mới thể hiện chính xác khả năng thực bào (ANC) hoặc đáp ứng miễn dịch thích ứng (ALC) của cơ thể.<br>3) <b>Ví dụ minh họa thực chiến:</b><br>• Trẻ A: WBC 4.000/mm³, Neutro 60% → ANC = 2.400/mm³ (bình thường).<br>• Trẻ B: WBC 25.000/mm³, Neutro 20% → ANC = 5.000/mm³ (tăng bạch cầu trung tính thực sự dù % rất thấp).<br><br><b>💡 Giải thích của AI:</b><br>Luôn luôn lấy bút tính hoặc nhìn vào cột số lượng tuyệt đối (G/L hoặc /mm³) trước khi đưa ra bất kỳ kết luận nào về tình trạng viêm hay suy tủy của bệnh nhi.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 0.1)",
    "tags": [
      "PED-63",
      "B0-Nguyen-ly",
      "Con-so-tuyet-doi"
    ]
  },
  {
    "id": "PED63-B1-01",
    "type": "basic",
    "section": "B1",
    "category": "Biến thiên tổng bạch cầu theo tuổi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Khoảng tham chiếu chuẩn của <span style=\"color:#ffd43b\"><b>Số lượng tổng bạch cầu (WBC)</b></span> ở <span style=\"color:#74c0fc\"><b>trẻ sơ sinh lúc mới đẻ</b></span> và <span style=\"color:#ffd43b\"><b>trong 24 – 48 giờ đầu sau sinh</b></span> là bao nhiêu?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ffd43b\"><b>Lúc mới sinh (máu cuống rốn / sơ sinh ngày 1):</b></span> Dao động từ <span style=\"color:#ffd43b\"><b>10.000 đến 30.000 /mm³</b></span> (trung bình khoảng <b>18.000 – 20.000 /mm³</b>).<br>• <span style=\"color:#ffd43b\"><b>Đỉnh cao trong 24 – 48 giờ đầu:</b></span> Có thể vọt lên <span style=\"color:#ff6b6b\"><b>25.000 – 30.000 /mm³</b></span> do phản ứng sinh lý với quá trình chuyển dạ, co bóp tử cung và kích thích giải phóng catecholamin/corticoid nội sinh.<br><br><b>💡 Giải thích của AI:</b><br>Một đứa trẻ sơ sinh 24 giờ tuổi có WBC 26.000/mm³ mà toàn trạng hồng hào, khóc to, bú mẹ tốt là hoàn toàn sinh lý bình thường; không được coi là nhiễm trùng huyết nếu không có các dấu hiệu lâm sàng cờ đỏ đi kèm.",
    "extra": "📖 Nguồn: Fanaroff and Martin's Neonatal-Perinatal Medicine & Nelson Ch.503 (PED-63, Mục 1)",
    "tags": [
      "PED-63",
      "B1-WBC-theo-tuoi",
      "So-sinh"
    ]
  },
  {
    "id": "PED63-B1-02",
    "type": "basic",
    "section": "B1",
    "category": "Biến thiên tổng bạch cầu theo tuổi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Khoảng tham chiếu của <span style=\"color:#ffd43b\"><b>Số lượng tổng bạch cầu (WBC)</b></span> ở trẻ từ <span style=\"color:#ffd43b\"><b>1 tuần đến 1 tháng</b></span> và ở <span style=\"color:#ffd43b\"><b>trẻ nhũ nhi (1 đến 12 tháng)</b></span> là bao nhiêu?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ffd43b\"><b>Từ 1 tuần đến 1 tháng tuổi:</b></span> Bạch cầu giảm dần về mức <span style=\"color:#ffd43b\"><b>10.000 đến 15.000 /mm³</b></span>.<br>• <span style=\"color:#ffd43b\"><b>Trẻ nhũ nhi (1 đến 12 tháng tuổi):</b></span> Dao động ổn định từ <span style=\"color:#ffd43b\"><b>6.000 đến 14.000 /mm³</b></span> (trung bình khoảng 10.000 – 12.000 /mm³).<br><br><b>💡 Giải thích của AI:</b><br>Sau tuần đầu tiên, tác động của stress sinh nở hết hẳn và tủy xương thiết lập trạng thái ổn định mới. Ở trẻ dưới 1 tuổi, mức bạch cầu 13.000/mm³ vẫn nằm hoàn toàn trong giới hạn sinh lý bình thường.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 & Giáo trình Nhi YTB (PED-63, Mục 1)",
    "tags": [
      "PED-63",
      "B1-WBC-theo-tuoi",
      "Nhu-nhi"
    ]
  },
  {
    "id": "PED63-B1-03",
    "type": "basic",
    "section": "B1",
    "category": "Biến thiên tổng bạch cầu theo tuổi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Khoảng tham chiếu của <span style=\"color:#ffd43b\"><b>Tổng bạch cầu (WBC)</b></span> ở trẻ <span style=\"color:#ffd43b\"><b>1 đến 5 tuổi</b></span> và trẻ <span style=\"color:#ffd43b\"><b>trên 6 tuổi đến tuổi trưởng thành</b></span> là bao nhiêu?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ffd43b\"><b>Trẻ từ 1 đến 5 tuổi:</b></span> Dao động từ <span style=\"color:#ffd43b\"><b>6.000 đến 12.000 /mm³</b></span>.<br>• <span style=\"color:#ffd43b\"><b>Trẻ trên 6 tuổi và thanh thiếu niên:</b></span> Dao động từ <span style=\"color:#ffd43b\"><b>4.500 đến 10.000 /mm³</b></span> (tiệm cận và đạt mức tham chiếu chuẩn của người lớn).<br><br><b>💡 Giải thích của AI:</b><br>Từ 6 tuổi trở đi, hệ thống miễn dịch của trẻ đã tiếp xúc với hầu hết các mầm bệnh thông thường, mô lympho bắt đầu thoái triển dần và công thức bạch cầu đạt đến trạng thái trưởng thành ổn định.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 1)",
    "tags": [
      "PED-63",
      "B1-WBC-theo-tuoi",
      "Tre-lon"
    ]
  },
  {
    "id": "PED63-B1-04",
    "type": "basic",
    "section": "B1",
    "category": "Biến thiên tổng bạch cầu theo tuổi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ý nghĩa lâm sàng của hiện tượng <span style=\"color:#ff6b6b\"><b>Giảm bạch cầu (Leukopenia)</b></span> ở <span style=\"color:#ffd43b\"><b>trẻ sơ sinh & nhũ nhi</b></span> nguy hiểm hơn rất nhiều so với người lớn như thế nào?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Định nghĩa giảm bạch cầu ở sơ sinh:</b> Khi <span style=\"color:#ff6b6b\"><b>WBC &lt; 5.000 /mm³</b></span> (hoặc ANC &lt; 1.000 – 1.500 /mm³).<br>2) <b>Ý nghĩa sinh bệnh học:</b> Là dấu hiệu chỉ điểm <span style=\"color:#ff6b6b\"><b>nhiễm khuẩn tối cấp dẫn đến cạn kiệt tủy xương cấp tính</b></span>; tủy không kịp sản sinh tế bào bù đắp lượng bạch cầu bị tiêu hủy ồ ạt tại ổ viêm.<br>3) <b>Tiên lượng:</b> Hạ bạch cầu ở sơ sinh có độ đặc hiệu và giá trị dự báo tử vong cao hơn nhiều so với tăng bạch cầu.<br><br><b>💡 Giải thích của AI:</b><br>Đừng bao giờ thở phào khi thấy một trẻ sơ sinh sốt hoặc hạ thân nhiệt có bạch cầu 'đẹp' ở mức 4.000/mm³. Đó không phải là bình thường mà là dấu hiệu cờ đỏ cấp cứu báo hiệu sốc nhiễm khuẩn huyết.",
    "extra": "📖 Nguồn: Manroe BL et al. J Pediatr 1979 & Nelson 21st Ch.132 (PED-63, Mục 1 & Mục 4)",
    "tags": [
      "PED-63",
      "B1-WBC-theo-tuoi",
      "Giam-bach-cau",
      "Cap-cuu"
    ]
  },
  {
    "id": "PED63-B2-01",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#74c0fc\"><b>Khung tổng quan:</b></span> Bản chất của <span style=\"color:#ffd43b\"><b>Hiện tượng 2 lần bắt chéo kinh điển</b></span> giữa Neutrophil và Lymphocyte trong huyết học Nhi khoa là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>Là sự tráo đổi vị trí ưu thế tỷ lệ giữa hai dòng bạch cầu chủ lực theo tuổi:<br>• Lúc mới sinh: <span style=\"color:#74c0fc\"><b>Neutrophil chiếm ưu thế</b></span> (giống người lớn).<br>• <span style=\"color:#ffd43b\"><b>LẦN BẮT CHÉO 1 (Ngày 5 – 7 sau sinh):</b></span> Tỷ lệ Neutrophil và Lympho gặp nhau cân bằng ở mức <span style=\"color:#ffd43b\"><b>xấp xỉ 45% – 45%</b></span>.<br>• Từ sau ngày 5–7 đến 5–7 tuổi: <span style=\"color:#74c0fc\"><b>Lymphocyte chiếm ưu thế tuyệt đối (60% – 70%)</b></span>.<br>• <span style=\"color:#ffd43b\"><b>LẦN BẮT CHÉO 2 (Lúc 5 – 7 tuổi):</b></span> Hai dòng gặp lại nhau lần thứ 2 cân bằng ở mức <span style=\"color:#ffd43b\"><b>xấp xỉ 45% – 45%</b></span>.<br>• Sau 7 tuổi đến lớn: <span style=\"color:#74c0fc\"><b>Neutrophil quay lại chiếm ưu thế (60% – 70%)</b></span> như người lớn.<br><br><b>💡 Giải thích của AI:</b><br>Quy tắc ghi nhớ nhanh '5 ngày - 5 tuổi': Ngày thứ 5 bắt chéo lần 1, 5 tuổi bắt chéo lần 2. Nằm giữa hai mốc này (từ sơ sinh đến 5 tuổi), công thức bạch cầu của trẻ bình thường luôn có Lympho nhiều gấp đôi Neutrophil.",
    "extra": "📖 Nguồn: Giáo trình Nhi khoa ĐHYHN & Nhi Y Thái Bình (PED-63, Mục 2.1)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Tong-quan"
    ]
  },
  {
    "id": "PED63-B2-02",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm tỷ lệ của <span style=\"color:#74c0fc\"><b>Giai đoạn 1 (Lúc sinh đến ngày thứ 4 sau sinh)</b></span> trước lần bắt chéo thứ nhất là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#74c0fc\"><b>Dòng chiếm ưu thế:</b></span> <span style=\"color:#74c0fc\"><b>Bạch cầu đa nhân trung tính (Neutrophil)</b></span> chiếm khoảng <span style=\"color:#ffd43b\"><b>60% – 65%</b></span>.<br>• <b>Dòng Lymphocyte:</b> Chỉ chiếm tỷ lệ thấp khoảng <span style=\"color:#ffd43b\"><b>20% – 30%</b></span>.<br>• <b>Cơ chế sinh học:</b> Do ảnh hưởng của hormone mẹ qua nhau thai (estrogen, glucocorticoid) kích thích tủy xương tăng sinh dòng hạt, kết hợp với phản ứng stress tự nhiên trong cuộc đẻ giải phóng bạch cầu dự trữ.<br><br><b>💡 Giải thích của AI:</b><br>Trong 4 ngày đầu đời, công thức bạch cầu của trẻ sơ sinh trông rất giống người lớn. Đây là cơ chế bảo vệ tự nhiên trang bị đội quân thực bào tinh nhuệ nhất để chống lại sự xâm lấn của vi khuẩn da và đường ruột ngay khi chào đời.",
    "extra": "📖 Nguồn: Nathan and Oski's Hematology of Infancy and Childhood (PED-63, Mục 2.2)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Giai-doan-1"
    ]
  },
  {
    "id": "PED63-B2-03",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm và ý nghĩa của <span style=\"color:#ffd43b\"><b>Mốc bắt chéo lần thứ 1 (Ngày thứ 5 – 7 sau sinh)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Thời điểm xuất hiện:</b> Xảy ra vào <span style=\"color:#ffd43b\"><b>ngày thứ 5 đến ngày thứ 7 sau khi sinh</b></span>.<br>• <b>Tỷ lệ tại điểm giao cắt:</b> Tỷ lệ phần trăm của Neutrophil và Lymphocyte đạt điểm cân bằng bằng nhau, xấp xỉ <span style=\"color:#ffd43b\"><b>40% – 45% cho mỗi dòng</b></span>.<br>• <b>Ý nghĩa sinh học:</b> Đánh dấu sự thoái lui ảnh hưởng của hormone người mẹ và khởi đầu giai đoạn tủy xương chuyển hướng ưu tiên sang phát triển các cơ quan lympho ngoại vi thích ứng.<br><br><b>💡 Giải thích của AI:</b><br>Tại thời điểm giao cắt này, Neutrophil đang trên đà lao dốc nhanh chóng từ 65% xuống 30%, trong khi Lymphocyte đang tăng tốc từ 25% lên 60%.",
    "extra": "📖 Nguồn: Giáo trình Nhi khoa ĐHYHN (PED-63, Mục 2.2)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Lan-1"
    ]
  },
  {
    "id": "PED63-B2-04",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm tỷ lệ và <span style=\"color:#74c0fc\"><b>cơ chế sinh học</b></span> của <span style=\"color:#74c0fc\"><b>Giai đoạn 2 (Sau ngày 5–7 đến trước 5–7 tuổi)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#74c0fc\"><b>Dòng chiếm ưu thế tuyệt đối:</b></span> <span style=\"color:#74c0fc\"><b>Bạch cầu Lympho (Lymphocyte)</b></span>, chiếm khoảng <span style=\"color:#ffd43b\"><b>60% – 70%</b></span> (đạt đỉnh cao nhất lúc 1–2 tuổi); trong khi Neutrophil chỉ chiếm khoảng <span style=\"color:#ffd43b\"><b>25% – 30%</b></span>.<br>• <b>Cơ chế sinh học:</b> Sau khi sinh, trẻ bắt đầu tiếp xúc liên tục với hàng tỷ kháng nguyên môi trường (thức ăn, vi khuẩn chí đường ruột, vaccine, virus hô hấp). Tuyến ức (Thymus) và toàn bộ các nang lympho ngoại vi (hạch, lách, mảng Peyer) hoạt động hết công suất để phân chia, biệt hóa tế bào T và B nhằm thiết lập trí nhớ miễn dịch thích ứng.<br><br><b>💡 Giải thích của AI:</b><br>Đây là giai đoạn tạo 'thư viện kháng thể' của đời người. Nhìn thấy tỷ lệ Lympho 65% ở trẻ 1 tuổi là dấu hiệu đáng mừng cho thấy hệ miễn dịch đang huấn luyện tích cực, không được chẩn đoán nhầm thành 'nhiễm virus'!",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 2.2)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Giai-doan-2"
    ]
  },
  {
    "id": "PED63-B2-05",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm và ý nghĩa của <span style=\"color:#ffd43b\"><b>Mốc bắt chéo lần thứ 2 (Lúc 5 – 7 tuổi)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Thời điểm xuất hiện:</b> Xảy ra quanh mốc <span style=\"color:#ffd43b\"><b>5 đến 7 tuổi</b></span>.<br>• <b>Tỷ lệ tại điểm giao cắt:</b> Tỷ lệ Neutrophil và Lymphocyte gặp nhau lần thứ hai ở điểm cân bằng, xấp xỉ <span style=\"color:#ffd43b\"><b>40% – 45% cho mỗi dòng</b></span>.<br>• <b>Ý nghĩa sinh học:</b> Đánh dấu sự hoàn thiện cơ bản của hệ thống miễn dịch thích ứng; nhu cầu sản sinh lympho giảm dần và tủy xương tái lập ưu thế sản sinh dòng bạch cầu hạt diệt khuẩn bảo vệ cơ thể.<br><br><b>💡 Giải thích của AI:</b><br>Sau mốc 5-7 tuổi, đường cong tỷ lệ Neutrophil tiếp tục đi lên và vượt qua Lymphocyte để đưa công thức máu trở về cấu trúc giống người lớn.",
    "extra": "📖 Nguồn: Giáo trình Nhi khoa ĐHYHN (PED-63, Mục 2.2)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Lan-2"
    ]
  },
  {
    "id": "PED63-B2-06",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm tỷ lệ của <span style=\"color:#74c0fc\"><b>Giai đoạn 3 (Từ sau 7 tuổi đến tuổi trưởng thành)</b></span> sau lần bắt chéo thứ hai là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#74c0fc\"><b>Dòng chiếm ưu thế:</b></span> <span style=\"color:#74c0fc\"><b>Bạch cầu đa nhân trung tính (Neutrophil)</b></span> quay trở lại vị trí áp đảo, ổn định ở mức <span style=\"color:#ffd43b\"><b>60% – 70%</b></span>.<br>• <b>Dòng Lymphocyte:</b> Giảm tỷ lệ tương đối và ổn định ở mức <span style=\"color:#ffd43b\"><b>20% – 30%</b></span>.<br>• <b>Ý nghĩa thực hành:</b> Từ sau 7 tuổi trở đi, bác sĩ lâm sàng có thể bắt đầu áp dụng các tiêu chuẩn phân tích tỷ lệ công thức máu tương tự như ở người lớn.<br><br><b>💡 Giải thích của AI:</b><br>Ở lứa tuổi này, nếu một trẻ có tỷ lệ Lymphocyte tăng cao vọt trên 60% thì mới thực sự là bất thường (cần nghĩ đến nhiễm virus cấp tính, ho gà hoặc bệnh lý ác tính dòng lympho).",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 2.2)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Giai-doan-3"
    ]
  },
  {
    "id": "PED63-B2-07",
    "type": "basic",
    "section": "B2",
    "category": "Bắt chéo Neutrophil - Lymphocyte",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Sai lầm chẩn đoán kinh điển nào xảy ra khi bác sĩ <span style=\"color:#ff6b6b\"><b>quên mất hiện tượng 2 lần bắt chéo</b></span> ở một trẻ 2 tuổi bị sốt nhẹ?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sai lầm thường gặp:</b> Thấy kết quả xét nghiệm máu in ra Neutrophil 30% và Lympho 65%, bác sĩ vội vàng kết luận: <span style=\"color:#ff6b6b\"><b>'Bệnh nhân bị nhiễm virus vì Lympho tăng cao lấn át Neutrophil'</b></span>, hoặc chẩn đoán <span style=\"color:#ff6b6b\"><b>'Giảm bạch cầu hạt bệnh lý / Suy tủy'</b></span>.<br>2) <b>Bản chất thực tế:</b> Đây là <span style=\"color:#51cf66\"><b>công thức máu hoàn toàn bình thường 100% của một đứa trẻ 2 tuổi khỏe mạnh</b></span>.<br>3) <b>Nguy cơ cho bệnh nhân:</b> Có thể bỏ sót một ổ nhiễm trùng vi khuẩn nặng nếu chỉ nhìn tỷ lệ % mà không tính ANC và không tìm các dấu hiệu chuyển trái hoặc hạt độc tính.<br><br><b>💡 Giải thích của AI:</b><br>Ở trẻ 2 tuổi, tỷ lệ Lympho 65% là sinh lý; muốn biết có nhiễm khuẩn hay không phải nhân tổng bạch cầu để tính ANC và đối chiếu với lâm sàng.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 2.2 & Bẫy lâm sàng)",
    "tags": [
      "PED-63",
      "B2-Bat-cheo",
      "Cam-bay"
    ]
  },
  {
    "id": "PED63-B3-01",
    "type": "basic",
    "section": "B3",
    "category": "Các dòng bạch cầu khác",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Tỷ lệ bình thường, khoảng tham chiếu số lượng tuyệt đối và ý nghĩa lâm sàng của dòng <span style=\"color:#74c0fc\"><b>Bạch cầu ái toan (Eosinophil)</b></span> ở trẻ em là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Tỷ lệ & Số lượng bình thường:</b> Chiếm <span style=\"color:#ffd43b\"><b>1% – 4%</b></span> tổng bạch cầu; số lượng tuyệt đối <span style=\"color:#ffd43b\"><b>&lt; 500 /mm³</b></span> (hoặc &lt; 0.5 G/L).<br>• <b>Ý nghĩa khi TĂNG bạch cầu ái toan (Eosinophilia &gt; 500 /mm³):</b><br>1) <span style=\"color:#74c0fc\"><b>Bệnh lý dị ứng:</b></span> Hen phế quản, viêm mũi dị ứng, viêm da cơ địa (chàm), dị ứng đạm sữa bò, dị ứng thuốc.<br>2) <span style=\"color:#ff6b6b\"><b>Nhiễm ký sinh trùng giun sán xâm nhập mô:</b></span> <i>Toxocara</i> (giun đũa chó mèo), giun lươn, ấu trùng giun đũa chu du ở phổi (hội chứng Löffler).<br>3) <span style=\"color:#ff6b6b\"><b>Bệnh lý ác tính & suy giảm miễn dịch:</b></span> Hội chứng tăng IgE (Job syndrome), bạch cầu cấp dòng tủy.<br><br><b>💡 Giải thích của AI:</b><br>Ký sinh trùng chỉ sống đơn thuần trong lòng ruột không xâm lấn (như giun kim) thường không làm tăng Eosinophil. Khi Eosinophil tăng cao > 1.500/mm³, phải ưu tiên tìm sán lá gan, ấu trùng Toxocara hoặc giun lươn.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.147 & 503 (PED-63, Mục 3)",
    "tags": [
      "PED-63",
      "B3-Dong-khac",
      "Eosinophil"
    ]
  },
  {
    "id": "PED63-B3-02",
    "type": "basic",
    "section": "B3",
    "category": "Các dòng bạch cầu khác",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Tỷ lệ bình thường và vai trò sinh học của <span style=\"color:#74c0fc\"><b>Bạch cầu ái kiềm (Basophil)</b></span> trong các phản ứng cấp cứu dị ứng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Tỷ lệ & Số lượng bình thường:</b> Là dòng bạch cầu hiếm nhất trong máu ngoại vi, chiếm <span style=\"color:#ffd43b\"><b>0% – 1%</b></span>; số lượng tuyệt đối <span style=\"color:#ffd43b\"><b>&lt; 100 – 200 /mm³</b></span>.<br>• <b>Vai trò sinh học cốt tử:</b> Bề mặt màng Basophil gắn dày đặc các thụ thể có ái lực cực cao với đoạn Fc của kháng thể IgE (<span style=\"color:#74c0fc\"><b>FcεRI receptors</b></span>).<br>• <b>Cơ chế trong sốc phản vệ:</b> Khi kháng nguyên (dị nguyên thuốc, nọc ong, thức ăn) gắn bắt chéo 2 phân tử IgE bề mặt, Basophil lập tức phóng hạt ồ ạt giải phóng các chất trung gian hóa học cực mạnh: <span style=\"color:#ff6b6b\"><b>Histamine, Leukotriene (LTC4, LTD4), PAF</b></span> gây giãn mạch tụt huyết áp, co thắt phế quản và phù thanh quản cấp cứu.<br><br><b>💡 Giải thích của AI:</b><br>Basophil trong máu tuần hoàn là người anh em song sinh của Dưỡng bào (Mast cell) trong mô bì; sự phóng hạt ồ ạt của chúng là nguồn gốc của các triệu chứng sốc phản vệ đe dọa tử vong.",
    "extra": "📖 Nguồn: Abbas Cellular and Molecular Immunology 10th & Nelson (PED-63, Mục 3)",
    "tags": [
      "PED-63",
      "B3-Dong-khac",
      "Basophil",
      "Phan-ve"
    ]
  },
  {
    "id": "PED63-B3-03",
    "type": "basic",
    "section": "B3",
    "category": "Các dòng bạch cầu khác",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Tỷ lệ bình thường và ý nghĩa chẩn đoán khi <span style=\"color:#74c0fc\"><b>Bạch cầu Mono (Monocyte)</b></span> tăng cao ở trẻ em là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Tỷ lệ & Số lượng bình thường:</b> Chiếm <span style=\"color:#ffd43b\"><b>4% – 8%</b></span> tổng bạch cầu; số lượng tuyệt đối <span style=\"color:#ffd43b\"><b>&lt; 1.000 /mm³</b></span>.<br>• <b>Bản chất sinh học:</b> Là tiền thân của hệ thống Đại thực bào mô (Macrophages), chuyên trách thực bào vi khuẩn nội bào, dọn dẹp tế bào chết và trình diện kháng nguyên.<br>• <span style=\"color:#ff6b6b\"><b>Ý nghĩa khi TĂNG Monocyte (Monocytosis &gt; 1.000 /mm³):</b></span><br>1) <span style=\"color:#ff6b6b\"><b>Nhiễm trùng bán cấp và mạn tính:</b></span> Bệnh Lao (<i>Tuberculosis</i>), Viêm nội tâm mạc nhiễm khuẩn bán cấp (SBE).<br>2) <span style=\"color:#74c0fc\"><b>Nhiễm virus mạn / nội bào:</b></span> EBV, CMV, virus viêm gan.<br>3) <span style=\"color:#51cf66\"><b>Giai đoạn hồi phục tủy:</b></span> Tăng Mono thường là dấu hiệu chỉ điểm tủy xương đang hồi phục sau đợt ức chế do hóa trị hoặc nhiễm trùng nặng.<br><br><b>💡 Giải thích của AI:</b><br>Ở một trẻ sốt kéo dài không rõ nguyên nhân, số lượng Monocyte tăng cao kết hợp tốc độ máu lắng tăng vọt là chỉ dấu kinh điển hướng tới bệnh Lao hoặc viêm nội tâm mạc.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 3)",
    "tags": [
      "PED-63",
      "B3-Dong-khac",
      "Monocyte"
    ]
  },
  {
    "id": "PED63-B4-01",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Công thức chuẩn xác</b></span> để tính <span style=\"color:#74c0fc\"><b>Số lượng tuyệt đối bạch cầu đa nhân trung tính (ANC)</b></span> là gì và tại sao bắt buộc phải cộng cả tỷ lệ bạch cầu đũa (Bands)?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#51cf66\"><b>Công thức tính ANC:</b></span><br><div style=\"text-align:center;font-weight:bold;color:#ffd43b;margin:6px 0;\">ANC (/mm³) = WBC (/mm³) × (% Neutrophil Segs + % Bands) / 100</div><br>• <b>Lý do bắt buộc phải cộng cả % Bands:</b> Bạch cầu đũa (Band neutrophil) là tế bào bạch cầu trung tính non vừa được tủy xương phóng thích; chúng <span style=\"color:#51cf66\"><b>đã có đầy đủ khả năng thực bào diệt khuẩn</b></span> như bạch cầu đoạn trưởng thành (Segs). Nếu bỏ qua Bands, bác sĩ sẽ đánh giá thấp nghiêm trọng năng lực bảo vệ của hệ tạo máu.<br><br><b>💡 Giải thích của AI:</b><br>Ví dụ: Trẻ có WBC 10.000/mm³, Segs 20%, Bands 30%. Nếu chỉ tính Segs thì ANC = 2.000/mm³ (bình thường); nhưng thực tế ANC = 10.000 × (20 + 30)% = 5.000/mm³ (bạch cầu hạt đang được huy động mạnh mẽ chống nhiễm trùng).",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 4.1)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "ANC",
      "Cong-thuc"
    ]
  },
  {
    "id": "PED63-B4-02",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Các <span style=\"color:#ffd43b\"><b>ngưỡng phân loại giảm bạch cầu trung tính (Neutropenia)</b></span> theo mức độ ANC ở trẻ em là bao nhiêu và <span style=\"color:#ff6b6b\"><b>ngưỡng nào báo động đỏ nguy kịch</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ffd43b\"><b>Mức độ nhẹ:</b></span> ANC từ <span style=\"color:#ffd43b\"><b>1.000 đến 1.500 /mm³</b></span> (ít có nguy cơ nhiễm trùng cơ hội).<br>• <span style=\"color:#ffd43b\"><b>Mức độ vừa:</b></span> ANC từ <span style=\"color:#ffd43b\"><b>500 đến 1.000 /mm³</b></span> (nguy cơ nhiễm trùng tăng lên, cần theo dõi sát).<br>• <span style=\"color:#ff6b6b\"><b>Mức độ NẶNG (Báo động đỏ):</b></span> <span style=\"color:#ff6b6b\"><b>ANC &lt; 500 /mm³</b></span> (hoặc &lt; 0.5 G/L).<br>• <b>Nguy cơ khi ANC &lt; 500:</b> Bệnh nhi đối mặt với nguy cơ tử vong cực cao do nhiễm trùng cơ hội tối cấp từ vi khuẩn nội sinh đường ruột (<i>Pseudomonas</i>, trực khuẩn Gram âm) và nấm xâm lấn.<br><br><b>💡 Giải thích của AI:</b><br>Khi ANC &lt; 500/mm³ kèm sốt (Sốt giảm bạch cầu hạt - Febrile Neutropenia), đây là một cấp cứu nội khoa tối khẩn đòi hỏi phải cấy máu và dùng ngay kháng sinh diệt trực khuẩn mủ xanh tĩnh mạch phổ rộng (như Cefepime hoặc Meropenem) trong vòng 60 phút đầu tiên.",
    "extra": "📖 Nguồn: IDSA Clinical Practice Guideline for the Use of Antimicrobial Agents in Neutropenic Patients with Cancer (PED-63, Mục 4.1)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "ANC",
      "Neutropenia",
      "Cap-cuu"
    ]
  },
  {
    "id": "PED63-B4-03",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Bản chất của <span style=\"color:#ff6b6b\"><b>Hiện tượng Chuyển trái (Left Shift)</b></span> trong công thức bạch cầu là gì và tại sao lại mang tên 'chuyển trái'?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Bản chất sinh học:</b> Là sự xuất hiện với tỷ lệ bất thường của các <span style=\"color:#ff6b6b\"><b>dạng tế bào bạch cầu trung tính non chưa trưởng thành</b></span> trong máu ngoại vi, bao gồm: <span style=\"color:#ff6b6b\"><b>Bạch cầu đũa (Bands), Hậu tủy bào (Metamyelocytes), Tủy bào (Myelocytes)</b></span> và đôi khi là Tiền tủy bào.<br>• <b>Nguồn gốc tên gọi 'Chuyển trái':</b> Trên sơ đồ phân loại huyết học kinh điển theo thuyết Schilling, các tế bào non nhất được xếp ở cột bên trái và các tế bào trưởng thành xếp ở bên phải. Khi tủy xương bị kích thích giải phóng tế bào non ra máu, đường cong phân bố lệch dịch chuyển hẳn về phía bên trái.<br><br><b>💡 Giải thích của AI:</b><br>Chuyển trái là bằng chứng rõ nhất cho thấy tủy xương đang hoạt động trong tình trạng khẩn cấp: nhu cầu tiêu thụ bạch cầu tại ổ nhiễm trùng quá lớn vượt quá khả năng cung ứng tế bào trưởng thành.",
    "extra": "📖 Nguồn: Wintrobe's Clinical Hematology 14th & Nelson (PED-63, Mục 4.2)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "Chuyen-trai"
    ]
  },
  {
    "id": "PED63-B4-04",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Công thức tính <span style=\"color:#51cf66\"><b>Chỉ số I/T ratio</b></span> là gì và <span style=\"color:#ff6b6b\"><b>ngưỡng cờ đỏ ở trẻ sơ sinh</b></span> chỉ điểm nguy cơ gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#51cf66\"><b>Công thức tính I/T ratio (Immature to Total Neutrophil ratio):</b></span><br><div style=\"text-align:center;font-weight:bold;color:#ffd43b;margin:6px 0;\">I/T ratio = Tổng tế bào non (Immature) / Tổng số Neutrophil</div>Trong đó: Immature = Bands + Metamyelocytes + Myelocytes; Tổng số Neutrophil = Immature + Mature Segs.<br>• <span style=\"color:#ff6b6b\"><b>Ngưỡng cờ đỏ báo động ở trẻ sơ sinh:</b></span> Khi <span style=\"color:#ff6b6b\"><b>I/T ratio &gt; 0.20</b></span> (nghĩa là tế bào non chiếm trên 20% tổng số dòng bạch cầu hạt).<br>• <b>Ý nghĩa lâm sàng:</b> Chỉ điểm nguy cơ rất cao của <span style=\"color:#ff6b6b\"><b>Nhiễm khuẩn huyết sơ sinh sớm (Early-Onset Neonatal Sepsis)</b></span>, có độ nhạy và giá trị dự báo âm tính (NPV) cực cao (&gt; 95% – 99%).<br><br><b>💡 Giải thích của AI:</b><br>Ở trẻ sơ sinh, I/T ratio > 0.20 có giá trị chẩn đoán nhiễm trùng vượt trội hơn bản thân tổng bạch cầu. Khi kết hợp với các triệu chứng lâm sàng (bú kém, hạ thân nhiệt, thở rên), đây là chỉ định bắt buộc phải cấy máu và dùng kháng sinh phổ rộng ngay lập tức.",
    "extra": "📖 Nguồn: Manroe BL et al. J Pediatr 1979 & Rodwell RL et al. J Pediatr 1988 (PED-63, Mục 4.2)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "IT-ratio",
      "So-sinh"
    ]
  },
  {
    "id": "PED63-B4-05",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm hình thái và cơ chế bệnh sinh của <span style=\"color:#ff6b6b\"><b>Hạt độc tính (Toxic Granulations)</b></span> trong bào tương Neutrophil khi nhiễm khuẩn nặng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Đặc điểm hình thái:</b> Các hạt thô to, có màu tím sẫm hoặc xanh đen phân bố rải rác trong bào tương của bạch cầu đa nhân trung tính khi nhuộm Giemsa/Wright.<br>• <b>Cơ chế bệnh sinh:</b> Dưới kích thích của bão cytokine viêm (G-CSF, IL-6), thời gian sinh bạch cầu tại tủy xương bị rút ngắn từ 14 ngày xuống chỉ còn 2–3 ngày. Các <span style=\"color:#ff6b6b\"><b>hạt nguyên sinh sơ cấp (Primary azurophilic granules)</b></span> giàu enzyme diệt khuẩn (Myeloperoxidase, Lysozyme, Acid phosphatase) không kịp trưởng thành bình thường mà tồn dư dưới dạng các hạt thô bắt màu kiềm đậm.<br><br><b>💡 Giải thích của AI:</b><br>Hạt độc tính là bằng chứng vi thể trực tiếp cho thấy tế bào đang ở trạng thái 'chiến đấu' cao độ để tiêu diệt vi khuẩn, có giá trị khẳng định nhiễm trùng vi khuẩn nặng vượt trội hơn con số số lượng đơn thuần.",
    "extra": "📖 Nguồn: Wintrobe's Clinical Hematology 14th Ed. (PED-63, Mục 4.3)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "Hat-doc",
      "Hinh-thai"
    ]
  },
  {
    "id": "PED63-B4-06",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm hình thái và ý nghĩa sinh tử của <span style=\"color:#ff6b6b\"><b>Không bào độc tính (Toxic Vacuolization)</b></span> trong bào tương Neutrophil là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Đặc điểm hình thái:</b> Các hốc tròn rỗng sáng màu, không bắt màu thuốc nhuộm, xuất hiện trong khối bào tương của Neutrophil.<br>• <b>Cơ chế bệnh sinh:</b> Là dấu tích còn lại của các <span style=\"color:#ff6b6b\"><b>túi thực bào (Phagolysosomes)</b></span> sau khi tế bào nuốt và tự tiêu hóa vi khuẩn, hoặc do độc tố vi khuẩn làm tổn thương màng tế bào gây hiện tượng tự thực bào (Autophagy).<br>• <b>Ý nghĩa lâm sàng:</b> Có <span style=\"color:#ff6b6b\"><b>độ đặc hiệu cực cao cho nhiễm trùng huyết (Sepsis) hoặc nhiễm khuẩn xâm lấn hoại tử mô</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Sự xuất hiện của không bào trong > 10% số lượng Neutrophil trên lam máu ngoại vi là một hồi chuông cảnh báo vi khuẩn đã xâm nhập vào máu và đang bị thực bào trực tiếp, đòi hỏi phải can thiệp kháng sinh tĩnh mạch liều cao ngay lập tức.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 4.3)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "Khong-bao",
      "Hinh-thai"
    ]
  },
  {
    "id": "PED63-B4-07",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Đặc điểm nhận diện và bản chất vi thể của <span style=\"color:#74c0fc\"><b>Thể Döhle (Döhle bodies)</b></span> trong bạch cầu trung tính là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Đặc điểm nhận diện:</b> Các thể vùi đơn độc hoặc đôi hình bầu dục/hình tròn nhỏ, có <span style=\"color:#74c0fc\"><b>màu xanh lam nhạt hoặc xám xanh</b></span> nằm ở vùng rìa sát màng tế bào của Neutrophil.<br>• <b>Bản chất vi thể:</b> Là các mảnh tàn dư của <span style=\"color:#74c0fc\"><b>lưới nội chất hạt thô (Rough Endoplasmic Reticulum) chứa RNA ribosome</b></span> còn sót lại do tế bào bị đẩy ra máu ngoại vi quá vội vã khi chưa hoàn tất quá trình thoái biến bào quan.<br>• <b>Bệnh cảnh xuất hiện:</b> Nhiễm trùng vi khuẩn nặng, bỏng diện rộng, chấn thương mô nặng hoặc stress thai kỳ.<br><br><b>💡 Giải thích của AI:</b><br>Thể Döhle thường xuất hiện đồng thời cùng hạt độc tính. Bộ ba vi thể 'Hạt độc + Thể Döhle + Không bào' được mệnh danh là 'Tam chứng biến đổi nhiễm độc' của bạch cầu trung tính trong Sepsis.",
    "extra": "📖 Nguồn: Wintrobe's Clinical Hematology 14th Ed. (PED-63, Mục 4.3)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "The-Dohle",
      "Hinh-thai"
    ]
  },
  {
    "id": "PED63-B4-08",
    "type": "basic",
    "section": "B4",
    "category": "Tiếp cận Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Bản chất miễn dịch học và hình thái của <span style=\"color:#74c0fc\"><b>Tế bào Lympho không điển hình / Phản ứng (Atypical / Reactive Lymphocytes / Downey cells)</b></span> trong nhiễm virus là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Bản chất miễn dịch học:</b> KHÔNG PHẢI tế bào ác tính; đó chính là các <span style=\"color:#74c0fc\"><b>tế bào Lympho T gây độc (CD8+ Cytotoxic T cells) và tế bào NK</b></span> đã được kích hoạt mạnh mẽ để chống lại sự nhân lên của virus nội bào.<br>• <b>Đặc điểm hình thái học:</b> Kích thước tế bào to gấp đôi bình thường, bào tương rất rộng bắt màu kiềm đậm ở vùng rìa nơi viền quanh các hồng cầu lân cận (hình ảnh 'ôm ấp hồng cầu'), nhân to mềm mại.<br>• <b>Căn nguyên kinh điển:</b> Gặp tỷ lệ cao trong <span style=\"color:#74c0fc\"><b>Nhiễm virus Epstein-Barr (EBV - Bệnh tăng bạch cầu đơn nhân nhiễm khuẩn)</b></span>, CMV, Sốt xuất huyết Dengue, Virus viêm gan, HIV cấp.<br><br><b>💡 Giải thích của AI:</b><br>Khi thấy tỷ lệ Lympho phản ứng > 10% trên lam máu ở một bệnh nhi sốt, viêm họng giả mạc và nổi hạch cổ, bác sĩ có thể tự tin định hướng đến EBV và tránh được việc dùng kháng sinh Ampicillin/Amoxicillin (vốn sẽ gây phát ban dát đỏ toàn thân dị ứng ở bệnh nhân EBV).",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.282 (PED-63, Mục 4.4)",
    "tags": [
      "PED-63",
      "B4-Tiep-can",
      "Downey-cells",
      "Virus"
    ]
  },
  {
    "id": "PED63-B5-01",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "⚠️ Ngoại lệ 1: Tại sao bệnh <span style=\"color:#74c0fc\"><b>Ho gà (Bordetella pertussis)</b></span> do VI KHUẨN gây ra nhưng công thức máu lại có biểu hiện <span style=\"color:#ff6b6b\"><b>tăng vọt bạch cầu khủng khiếp với ưu thế tuyệt đối dòng Lympho</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Hiện tượng huyết học nghịch lý:</b> Tổng bạch cầu tăng cực cao từ <span style=\"color:#ff6b6b\"><b>30.000 đến 100.000 /mm³</b></span> (phản ứng dạng bạch cầu cấp - Leukemoid reaction), trong đó <span style=\"color:#74c0fc\"><b>tế bào Lymphocyte chiếm tới 70% – 85%</b></span>.<br>2) <b>Cơ chế độc tố vi khuẩn:</b> Vi khuẩn tiết ra <span style=\"color:#ff6b6b\"><b>Độc tố Ho gà (Pertussis Toxin - PT)</b></span> làm bất hoạt protein Gi, dẫn tới ức chế sự di chuyển xuyên mạch của tế bào lympho từ máu tuần hoàn trở về các hạch bạch huyết. Các tế bào lympho bị bẫy lại hoàn toàn trong lòng mạch máu và tích tụ với số lượng khổng lồ.<br>3) <b>Ý nghĩa tiên lượng tử vong:</b> Ở trẻ nhũ nhi chưa tiêm chủng, bạch cầu tăng &gt; 50.000 – 100.000/mm³ gây hiện tượng tắc mạch máu phổi (Leukostasis), tăng áp lực động mạch phổi ác tính và suy tim cấp đe dọa tính mạng.<br><br><b>💡 Giải thích của AI:</b><br>Ho gà là vi khuẩn duy nhất 'đội lốt' virus về mặt huyết học. Khi thấy trẻ nhỏ ho cơn đỏ mặt kèm bạch cầu 50.000 với 80% lympho, đừng nhầm với bệnh bạch cầu cấp dòng lympho (ALL) hay nhiễm virus mà phải nghĩ ngay đến Ho gà để lọc máu thay thế hoặc dùng sớm Macrolide.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.218 & CDC Pertussis Guidelines (PED-63, Mục 5.1)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "Ho-ga",
      "Pertussis"
    ]
  },
  {
    "id": "PED63-B5-02",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "⚠️ Ngoại lệ 2: Tại sao bệnh <span style=\"color:#74c0fc\"><b>Thương hàn (Salmonella Typhi)</b></span> là nhiễm trùng VI KHUẨN xâm lấn đường ruột nặng nhưng công thức máu lại <span style=\"color:#ff6b6b\"><b>GIẢM BẠCH CẦU</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Hiện tượng huyết học nghịch lý:</b> Bệnh nhân sốt cao liên tục hình cao nguyên, nhiễm độc nặng nhưng tổng bạch cầu lại <span style=\"color:#ff6b6b\"><b>GIẢM (WBC &lt; 4.000 – 5.000 /mm³)</b></span> kèm theo <span style=\"color:#ff6b6b\"><b>giảm bạch cầu đa nhân trung tính và biến mất hoàn toàn bạch cầu ái toan (Aneutrophilia & Aneosinophilia)</b></span>.<br>2) <b>Cơ chế bệnh sinh:</b><br>• <span style=\"color:#ff6b6b\"><b>Nội độc tố LPS của Salmonella:</b></span> Gây ức chế trực tiếp quá trình phân chia tế bào tủy xương.<br>• <span style=\"color:#74c0fc\"><b>Hiện tượng thực bào máu (Hemophagocytosis):</b></span> Vi khuẩn kích hoạt mạnh mẽ hệ thống đại thực bào tại gan, lách và tủy xương nuốt và tiêu hủy các tế bào bạch cầu và hồng cầu non.<br><br><b>💡 Giải thích của AI:</b><br>Dấu hiệu 'Sốt cao + Mạch nhiệt phân ly (mạch chậm tương đối so với nhiệt độ) + Bạch cầu giảm + Bạch cầu ái toan bằng 0%' là tứ chứng kinh điển giúp chẩn đoán Thương hàn trước khi có kết quả cấy máu.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.216 (PED-63, Mục 5.2)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "Thuong-han",
      "Salmonella"
    ]
  },
  {
    "id": "PED63-B5-03",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "⚠️ Ngoại lệ 3: Cơ chế nào khiến <span style=\"color:#ff6b6b\"><b>Sốc nhiễm khuẩn tối cấp (Septic Shock)</b></span> ở trẻ em có biểu hiện <span style=\"color:#ff6b6b\"><b>bạch cầu tụt dốc thảm hại</b></span> và ý nghĩa tiên lượng của nó?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế tụt dốc bạch cầu:</b> Do sự phối hợp của 2 cơ chế tối cấp:<br>• <span style=\"color:#ff6b6b\"><b>Tiêu thụ ngoại vi ồ ạt:</b></span> Vi khuẩn và nội độc tố trong máu làm hoạt hóa đồng loạt các phân tử kết dính (Selectin, Integrin), khiến toàn bộ bạch cầu trung tính bám dính vào thành mạch máu và thoát mạch ồ ạt vào các mô cơ quan tổn thương.<br>• <span style=\"color:#ff6b6b\"><b>Cạn kiệt tủy xương cấp tính:</b></span> Nhu cầu quá lớn vượt xa kho dự trữ tế bào của tủy xương trẻ nhỏ, dẫn tới suy kiệt sản xuất.<br>2) <b>Ý nghĩa tiên lượng tử vong:</b> Bạch cầu tụt dốc <span style=\"color:#ff6b6b\"><b>&lt; 4.000 /mm³ (đặc biệt &lt; 1.000 – 2.000 /mm³)</b></span> trong sốc nhiễm trùng là <span style=\"color:#ff6b6b\"><b>dấu hiệu tiên lượng tử vong cực kỳ xấu</b></span>, nguy cơ suy đa tạng tử vong tăng gấp 4–5 lần so với tăng bạch cầu.<br><br><b>💡 Giải thích của AI:</b><br>Đừng bao giờ để số lượng bạch cầu thấp đánh lừa là 'không có nhiễm trùng'. Trong bối cảnh sốc tụt huyết áp, chân tay lạnh ngắt, nổi vân tím thì bạch cầu càng thấp chứng tỏ nhiễm trùng càng tối cấp và dữ dội.",
    "extra": "📖 Nguồn: Surviving Sepsis Campaign Pediatric Guidelines 2020 & Nelson (PED-63, Mục 5.3)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "Soc-nhiem-khuan",
      "Cap-cuu"
    ]
  },
  {
    "id": "PED63-B5-04",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "⚠️ Ngoại lệ 4: Bản chất của hiện tượng <span style=\"color:#ffd43b\"><b>'Chuyển trái sinh lý' do Stress sơ sinh</b></span> trong 24 – 48 giờ đầu sau sinh là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất hiện tượng:</b> Trong <span style=\"color:#ffd43b\"><b>24 – 48 giờ đầu tiên sau đẻ</b></span>, tỷ lệ bạch cầu đũa (Bands) và các tế bào tủy non có thể tăng nhẹ thoáng qua trong máu ngoại vi (I/T ratio có thể chạm ngưỡng 0.16 – 0.18).<br>2) <b>Cơ chế sinh học:</b> Quá trình chuyển dạ, thiếu oxy sinh lý thoáng qua khi lọt qua ống đẻ và cơn tăng tiết Catecholamin/Cortisol ồ ạt kích thích tủy xương giải phóng vội vã một phần dòng tế bào hạt chưa kịp phân đoạn.<br>3) <b>Thái độ lâm sàng đúng đắn:</b> Nếu trẻ sơ sinh hoàn toàn không có triệu chứng lâm sàng (tự thở tốt, da hồng, bú tốt, trương lực cơ tốt), chỉ số này sẽ tự ổn định và giảm nhanh về bình thường sau 48–72 giờ mà <span style=\"color:#51cf66\"><b>không cần dùng kháng sinh</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Để không dùng kháng sinh oan cho trẻ sơ sinh khỏe mạnh trong 48h đầu, luôn phải đối chiếu I/T ratio với biểu đồ tham chiếu theo giờ tuổi của Manroe/Rodwell.",
    "extra": "📖 Nguồn: Manroe BL et al. J Pediatr 1979 & Gomella's Neonatology 8th (PED-63, Mục 5.4)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "So-sinh",
      "Chuyen-trai-sinh-ly"
    ]
  },
  {
    "id": "PED63-B5-05",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "⚠️ Ngoại lệ 5: Cơ chế nào khiến <span style=\"color:#ff6b6b\"><b>Corticoid (Dexamethasone, Methylprednisolone)</b></span> gây ra hiện tượng <span style=\"color:#ff6b6b\"><b>TĂNG BẠCH CẦU GIẢ TẠO</b></span> ở trẻ em?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế bóc tróc tế bào (Demargination):</b> Bình thường có khoảng 50% số lượng Neutrophil trong lòng mạch bám dính lỏng lẻo vào nội mô mao mạch (Marginal pool). Corticoid ức chế các phân tử kết dính (L-selectin, Mac-1), làm <span style=\"color:#ff6b6b\"><b>tróc toàn bộ số bạch cầu bám mạch này hòa vào dòng tuần hoàn tự do (Circulating pool)</b></span>, khiến máy đếm ghi nhận số lượng tăng vọt lên 15.000 – 25.000/mm³.<br>2) <b>Ức chế thoát mạch:</b> Corticoid ngăn cản bạch cầu trung tính rời mạch máu để đi vào mô.<br>3) <span style=\"color:#51cf66\"><b>Đặc điểm phân biệt với nhiễm khuẩn thực sự:</b></span> Tăng bạch cầu do Corticoid <span style=\"color:#51cf66\"><b>HOÀN TOÀN KHÔNG CÓ CHUYỂN TRÁI</b></span> (không tăng Bands, I/T &lt; 0.10) và <span style=\"color:#51cf66\"><b>HOÀN TOÀN KHÔNG CÓ HẠT ĐỘC TÍNH HAY KHÔNG BÀO</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Khi thấy một trẻ Hen phế quản hoặc Viêm thanh khí phế quản cấp sau tiêm Dexamethasone có bạch cầu tăng vọt 20.000/mm³, bác sĩ phải bình tĩnh: đây là hiệu ứng Demargination kinh điển của Corticoid chứ không phải bội nhiễm vi khuẩn.",
    "extra": "📖 Nguồn: Dale DC et al. J Clin Invest 1974 & Nelson 21st Ch.503 (PED-63, Mục 5.5)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "Corticoid",
      "Demargination"
    ]
  },
  {
    "id": "PED63-B5-06",
    "type": "basic",
    "section": "B5",
    "category": "5 Ngoại lệ kinh điển",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Cạm bẫy lâm sàng: Một trẻ 10 tháng tuổi có công thức máu <span style=\"color:#ffd43b\"><b>WBC 18.000/mm³, Neutrophil 25%, Lymphocyte 70%</b></span> — Phân tích sai lầm nếu vội vàng kết luận nhiễm virus?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sai lầm kết luận theo %:</b> Nhìn thấy Lympho 70% vội phán đoán 'nhiễm virus', bỏ qua nhiễm khuẩn.<br>2) <b>Tính toán số lượng tuyệt đối ANC:</b><br>• ANC = 18.000 × 25% = <span style=\"color:#ff6b6b\"><b>4.500 /mm³</b></span> (hoàn toàn bình thường hoặc tăng nhẹ ở trẻ nhũ nhi).<br>• Nhưng tổng bạch cầu 18.000/mm³ là tăng cao so với giới hạn trên sinh lý của lứa tuổi 10 tháng (bình thường 6.000 – 14.000/mm³).<br>3) <b>Hành động bắt buộc:</b> Bắt buộc phải <span style=\"color:#51cf66\"><b>soi lam máu tìm chuyển trái (tỷ lệ Bands) và hạt độc tính</b></span>, đồng thời kiểm tra nồng độ <span style=\"color:#51cf66\"><b>CRP hoặc Procalcitonin</b></span>; nếu trẻ có sốt cao kèm ổ nhiễm trùng khu trú (viêm tai giữa, viêm phổi) thì vẫn có thể là nhiễm vi khuẩn điển hình.<br><br><b>💡 Giải thích của AI:</b><br>Tỷ lệ Lympho 70% ở trẻ 10 tháng là cấu trúc nền tảng sinh lý của lứa tuổi; khi có nhiễm trùng, cả Neutrophil và Lympho đều có thể cùng tăng khiến tỷ lệ % không bị xáo trộn nhiều.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 5)",
    "tags": [
      "PED-63",
      "B5-Ngoai-le",
      "Cam-bay",
      "Nhu-nhi"
    ]
  },
  {
    "id": "PED63-B6-01",
    "type": "basic",
    "section": "B6",
    "category": "Ma trận đối đầu Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "So sánh đối đầu: Biến đổi của <span style=\"color:#ffd43b\"><b>Tổng bạch cầu (WBC)</b></span>, <span style=\"color:#74c0fc\"><b>Số lượng tuyệt đối ANC</b></span> và <span style=\"color:#ff6b6b\"><b>Hiện tượng Chuyển trái</b></span> giữa <span style=\"color:#ff6b6b\"><b>Nhiễm Vi khuẩn điển hình</b></span> vs <span style=\"color:#74c0fc\"><b>Nhiễm Virus</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ffd43b\"><b>Tổng bạch cầu (WBC):</b></span><br>• <b>Vi khuẩn:</b> Thường tăng cao vượt ngưỡng tuổi (thường &gt; 15.000 /mm³), hoặc giảm sâu (&lt; 4.000 /mm³) trong sốc tối cấp.<br>• <b>Virus:</b> Thường bình thường hoặc giảm nhẹ, ít khi tăng cao (ngoại trừ Adenovirus, Enterovirus).<br>2) <span style=\"color:#74c0fc\"><b>ANC (Số lượng tuyệt đối Neutrophil):</b></span><br>• <b>Vi khuẩn:</b> Tăng mạnh mẽ (&gt; 7.000 – 10.000 /mm³ ở trẻ lớn).<br>• <b>Virus:</b> Bình thường hoặc giảm nhẹ.<br>3) <span style=\"color:#ff6b6b\"><b>Chuyển trái (Left shift & I/T ratio):</b></span><br>• <b>Vi khuẩn:</b> Xuất hiện rõ rệt, tỷ lệ Bands &gt; 10%, I/T ratio &gt; 0.20 ở sơ sinh.<br>• <b>Virus:</b> Hoàn toàn KHÔNG có chuyển trái (I/T ratio bình thường &lt; 0.10).<br><br><b>💡 Giải thích của AI:</b><br>Chuyển trái là dấu hiệu có độ đặc hiệu cho nhiễm khuẩn cao hơn nhiều so với việc chỉ nhìn con số tổng bạch cầu đơn thuần.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 6)",
    "tags": [
      "PED-63",
      "B6-Ma-tran",
      "WBC-ANC-Chuyen-trai"
    ]
  },
  {
    "id": "PED63-B6-02",
    "type": "basic",
    "section": "B6",
    "category": "Ma trận đối đầu Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "So sánh đối đầu: Biến đổi về <span style=\"color:#ff6b6b\"><b>Dấu ấn hình thái học tế bào</b></span> và <span style=\"color:#74c0fc\"><b>Phản ứng dòng Lympho</b></span> giữa <span style=\"color:#ff6b6b\"><b>Nhiễm Vi khuẩn</b></span> vs <span style=\"color:#74c0fc\"><b>Nhiễm Virus</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Dấu ấn hình thái học vi thể:</b></span><br>• <b>Vi khuẩn:</b> Xuất hiện tam chứng nhiễm độc tế bào: <span style=\"color:#ff6b6b\"><b>Hạt độc tính dày đặc, Không bào tiêu hóa vi khuẩn, Thể Döhle</b></span>.<br>• <b>Virus:</b> Bào tương Neutrophil hoàn toàn bình thường, không có hạt độc, không có không bào.<br>2) <span style=\"color:#74c0fc\"><b>Phản ứng dòng Lymphocyte:</b></span><br>• <b>Vi khuẩn:</b> Số lượng và tỷ lệ Lympho tương đối giảm (Lymphopenia do tủy tập trung dồn sản sinh dòng hạt).<br>• <b>Virus:</b> Tăng số lượng tuyệt đối ALC, xuất hiện <span style=\"color:#74c0fc\"><b>Tế bào Lympho không điển hình / Phản ứng (Atypical lymphocytes &gt; 10%)</b></span> với bào tương rộng ưa kiềm.<br><br><b>💡 Giải thích của AI:</b><br>Soi lam máu kính hiển vi là 'tiêu chuẩn vàng' giúp phân định dứt khoát hai bệnh cảnh khi kết quả máy đếm tự động còn mơ hồ.",
    "extra": "📖 Nguồn: Wintrobe's Clinical Hematology 14th Ed. (PED-63, Mục 6)",
    "tags": [
      "PED-63",
      "B6-Ma-tran",
      "Hinh-thai-Lympho"
    ]
  },
  {
    "id": "PED63-B6-03",
    "type": "basic",
    "section": "B6",
    "category": "Ma trận đối đầu Vi khuẩn vs Virus",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "So sánh đối đầu: Đáp ứng của <span style=\"color:#ffd43b\"><b>Biomarker viêm (CRP, Procalcitonin)</b></span> và <span style=\"color:#51cf66\"><b>Chiến lược xử trí kháng sinh</b></span> giữa <span style=\"color:#ff6b6b\"><b>Nhiễm Vi khuẩn</b></span> vs <span style=\"color:#74c0fc\"><b>Nhiễm Virus</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ffd43b\"><b>Biomarker viêm (CRP & Procalcitonin):</b></span><br>• <b>Vi khuẩn:</b> CRP tăng cao (&gt; 40 – 60 mg/L), đặc biệt <span style=\"color:#ff6b6b\"><b>Procalcitonin tăng rất cao &gt; 0.5 – 2.0 ng/mL</b></span>.<br>• <b>Virus:</b> CRP thường thấp (&lt; 20 mg/L) trừ ngoại lệ Adenovirus; <span style=\"color:#51cf66\"><b>Procalcitonin luôn ở mức rất thấp (&lt; 0.25 – 0.5 ng/mL)</b></span> do bị IFN-γ ức chế.<br>2) <span style=\"color:#51cf66\"><b>Chiến lược điều trị:</b></span><br>• <b>Vi khuẩn:</b> Bắt buộc chỉ định <span style=\"color:#51cf66\"><b>kháng sinh đích kịp thời đúng liều lượng</b></span> (đầu tay là Beta-lactam).<br>• <b>Virus:</b> <span style=\"color:#51cf66\"><b>Trì hoãn kháng sinh</b></span>; tập trung điều trị triệu chứng, chăm sóc hỗ trợ dinh dưỡng và theo dõi sát phát hiện bội nhiễm.<br><br><b>💡 Giải thích của AI:</b><br>Sự kết hợp giữa lâm sàng + công thức máu + Procalcitonin là vũ khí mạnh nhất giúp bác sĩ ra quyết định giữ hay dùng kháng sinh chính xác tới 90%.",
    "extra": "📖 Nguồn: Schuetz P et al. Cochrane Review 2017 & PIDS Guidelines (PED-63, Mục 6)",
    "tags": [
      "PED-63",
      "B6-Ma-tran",
      "Biomarker-Dieu-tri"
    ]
  },
  {
    "id": "PED63-B7-01",
    "type": "basic",
    "section": "B7",
    "category": "Biomarkers viêm phối hợp",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nguồn gốc sản xuất, <span style=\"color:#ffd43b\"><b>động học thời gian tăng / đạt đỉnh</b></span> và các <span style=\"color:#ffd43b\"><b>ngưỡng nồng độ giá trị lâm sàng</b></span> của <span style=\"color:#74c0fc\"><b>CRP (C-Reactive Protein)</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Nguồn gốc & Kích thích:</b> Do tế bào gan tổng hợp chủ yếu dưới sự kích thích của cytokine <span style=\"color:#74c0fc\"><b>Interleukin-6 (IL-6)</b></span>.<br>• <span style=\"color:#ffd43b\"><b>Động học thời gian:</b></span> Bắt đầu tăng sau <span style=\"color:#ffd43b\"><b>6 – 8 giờ</b></span> kể từ khi khởi phát phản ứng viêm; đạt đỉnh cao nhất sau <span style=\"color:#ffd43b\"><b>24 – 48 giờ</b></span>; thời gian bán thải khoảng 19 giờ.<br>• <span style=\"color:#ffd43b\"><b>Các ngưỡng giá trị lâm sàng:</b></span><br>1) <b>&lt; 10 mg/L:</b> Mức bình thường, không có phản ứng viêm hệ thống rõ rệt.<br>2) <b>20 – 40 mg/L:</b> Viêm nhẹ đến vừa; có thể gặp trong nhiễm virus đường thở hoặc viêm nhiễm vi khuẩn khu trú.<br>3) <span style=\"color:#ff6b6b\"><b>&gt; 60 – 100 mg/L:</b></span> Gợi ý mạnh mẽ <span style=\"color:#ff6b6b\"><b>Nhiễm khuẩn vi khuẩn xâm lấn nặng</b></span> (viêm phổi thùy, viêm màng não mủ, viêm khớp mủ), hoặc ngoại lệ bão cytokine do Adenovirus.<br><br><b>💡 Giải thích của AI:</b><br>Vì CRP cần 6-8 giờ mới bắt đầu tăng, nếu xét nghiệm quá sớm trong 2-4 giờ đầu của một ca sốt cấp tính, CRP có thể vẫn âm tính giả bình thường; cần hẹn xét nghiệm lại sau 12-24 giờ.",
    "extra": "📖 Nguồn: Pepys MB, Hirschfield GM. J Clin Invest 2003 & Nelson Ch.503 (PED-63, Mục 7)",
    "tags": [
      "PED-63",
      "B7-Biomarkers",
      "CRP"
    ]
  },
  {
    "id": "PED63-B7-02",
    "type": "basic",
    "section": "B7",
    "category": "Biomarkers viêm phối hợp",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nguồn gốc tế bào, <span style=\"color:#ffd43b\"><b>động học siêu nhanh</b></span> và lý do vì sao <span style=\"color:#51cf66\"><b>Procalcitonin (PCT)</b></span> lại có độ đặc hiệu vượt trội cho <span style=\"color:#ff6b6b\"><b>Nhiễm vi khuẩn</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <b>Nguồn gốc tế bào:</b> Bình thường chỉ do tế bào C tuyến giáp tiết (nồng độ trong máu &lt; 0.05 ng/mL). Khi có nhiễm khuẩn, <span style=\"color:#74c0fc\"><b>TOÀN BỘ CÁC MÔ NHU MÔ TRONG CƠ THỂ</b></span> (gan, phổi, ruột, cơ) đồng loạt tiết PCT dưới kích thích của nội độc tố LPS và IL-1β/TNF-α.<br>• <span style=\"color:#ffd43b\"><b>Động học siêu nhanh:</b></span> Bắt đầu tăng rất sớm chỉ sau <span style=\"color:#ffd43b\"><b>2 – 4 giờ</b></span> (nhanh gấp 2–3 lần CRP); đạt đỉnh sau <span style=\"color:#ffd43b\"><b>12 – 24 giờ</b></span>; thời gian bán hủy 24 giờ.<br>• <span style=\"color:#51cf66\"><b>Lý do đặc hiệu cho Vi khuẩn:</b></span> Trong các nhiễm trùng do virus, cơ thể tăng tiết mạnh mẽ <span style=\"color:#51cf66\"><b>Interferon-gamma (IFN-γ)</b></span>; chất này ức chế trực tiếp sự tổng hợp Procalcitonin tại các mô. Do đó, nhiễm virus dù sốt cao đến đâu thì PCT vẫn bị 'khóa' ở mức rất thấp.<br><br><b>💡 Giải thích của AI:</b><br>Tính chất 'bị ức chế bởi virus, được kích hoạt bởi vi khuẩn' biến PCT thành chỉ số vàng độc nhất vô nhị để phân định nhiễm khuẩn vi khuẩn thực sự tại phòng cấp cứu.",
    "extra": "📖 Nguồn: Schuetz P et al. Lancet Infect Dis 2011 & Cochrane Review 2017 (PED-63, Mục 7)",
    "tags": [
      "PED-63",
      "B7-Biomarkers",
      "Procalcitonin",
      "PCT"
    ]
  },
  {
    "id": "PED63-B7-03",
    "type": "basic",
    "section": "B7",
    "category": "Biomarkers viêm phối hợp",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Các <span style=\"color:#ffd43b\"><b>ngưỡng Cut-off nồng độ của Procalcitonin (PCT)</b></span> hướng dẫn quyết định sử dụng kháng sinh trong thực hành lâm sàng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#51cf66\"><b>&lt; 0.25 ng/mL:</b></span> <span style=\"color:#51cf66\"><b>Rất ít khả năng nhiễm khuẩn vi khuẩn</b></span> (NPV &gt; 95%); khuyến cáo <b>KHÔNG DÙNG kháng sinh</b>, chỉ theo dõi và tìm nguyên nhân virus.<br>• <span style=\"color:#ffd43b\"><b>0.25 – 0.50 ng/mL:</b></span> Vùng xám (nghi ngờ nhiễm khuẩn nhẹ hoặc nhiễm khuẩn giai đoạn rất sớm); cân nhắc dựa vào lâm sàng.<br>• <span style=\"color:#ff6b6b\"><b>0.50 – 2.0 ng/mL:</b></span> <span style=\"color:#ff6b6b\"><b>Gợi ý mạnh mẽ nhiễm vi khuẩn</b></span>; khuyến cáo <b>BẮT ĐẦU sử dụng kháng sinh</b>.<br>• <span style=\"color:#ff6b6b\"><b>&gt; 2.0 – 10.0 ng/mL:</b></span> <span style=\"color:#ff6b6b\"><b>Nhiễm khuẩn vi khuẩn nặng / Nhiễm khuẩn huyết / Nguy cơ cao suy đa tạng</b></span>; bắt buộc dùng kháng sinh tĩnh mạch phổ rộng liều cao ngay lập tức.<br><br><b>💡 Giải thích của AI:</b><br>Áp dụng thuật toán PCT cut-off 0.25 ng/mL giúp các bệnh viện nhi cắt giảm được 40-50% số đơn thuốc kháng sinh không cần thiết trong các bệnh cảnh viêm phế quản và viêm đường hô hấp trên.",
    "extra": "📖 Nguồn: Schuetz P et al. Cochrane Database Syst Rev 2017 (PED-63, Mục 7)",
    "tags": [
      "PED-63",
      "B7-Biomarkers",
      "PCT-Cutoff",
      "Khang-sinh"
    ]
  },
  {
    "id": "PED63-B7-04",
    "type": "basic",
    "section": "B7",
    "category": "Biomarkers viêm phối hợp",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ý nghĩa lâm sàng của xét nghiệm <span style=\"color:#74c0fc\"><b>Ferritin huyết thanh</b></span> khi tăng cao vọt ở trẻ sốt nhiễm trùng nặng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bản chất kép của Ferritin:</b> Vừa là protein dự trữ sắt nội bào, vừa là một <span style=\"color:#ffd43b\"><b>chất phản ứng viêm pha cấp (Positive acute phase reactant)</b></span> được đại thực bào giải phóng dưới tác động của cytokine.<br>2) <span style=\"color:#ff6b6b\"><b>Ý nghĩa khi Ferritin &gt; 500 – 1.000 ng/mL:</b></span> Chỉ điểm phản ứng viêm toàn thân dữ dội, bão cytokine (gặp trong Sepsis nặng, viêm phổi Adenovirus hoại tử, nhiễm SARS-CoV-2/MIS-C).<br>3) <span style=\"color:#ff6b6b\"><b>Cờ đỏ tử vong khi Ferritin &gt; 2.000 – 10.000 ng/mL:</b></span> Là tiêu chuẩn chẩn đoán cốt tử của <span style=\"color:#ff6b6b\"><b>Hội chứng hoạt hóa đại thực bào (Macrophage Activation Syndrome - MAS)</b></span> hoặc Hội chứng thực bào máu (HLH); đòi hỏi can thiệp corticoid liều xung (Pulse Methylprednisolone) hoặc lọc máu cấp cứu.<br><br><b>💡 Giải thích của AI:</b><br>Khi bệnh nhi sốt kéo dài có biểu hiện suy tạng, một xét nghiệm Ferritin tăng vọt > 3.000 ng/mL là bằng chứng vàng chỉ điểm cơ thể đang tự hủy hoại bởi bão cytokine của đại thực bào.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.146 & HLH-2004 Criteria (PED-63, Mục 7)",
    "tags": [
      "PED-63",
      "B7-Biomarkers",
      "Ferritin",
      "HLH-MAS"
    ]
  },
  {
    "id": "PED63-B7-05",
    "type": "basic",
    "section": "B7",
    "category": "Biomarkers viêm phối hợp",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Bảng tổng hợp chiến lược phối hợp <span style=\"color:#ffd43b\"><b>Tam giác chẩn đoán: Công thức máu + CRP + Procalcitonin</b></span> giúp ra quyết định tại giường như thế nào?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Kịch bản 1 (Thuần túy Virus):</b></span> WBC bình thường/giảm, ANC thấp, không chuyển trái + CRP &lt; 20 mg/L + PCT &lt; 0.25 ng/mL → <span style=\"color:#51cf66\"><b>KHÔNG DÙNG kháng sinh, theo dõi ngoại trú</b></span>.<br>2) <span style=\"color:#ff6b6b\"><b>Kịch bản 2 (Vi khuẩn điển hình):</b></span> WBC tăng cao, ANC tăng, chuyển trái (Bands &gt; 10%), hạt độc tính + CRP &gt; 60 mg/L + PCT &gt; 0.5 – 2.0 ng/mL → <span style=\"color:#ff6b6b\"><b>BẮT BUỘC dùng kháng sinh diệt khuẩn ngay</b></span>.<br>3) <span style=\"color:#74c0fc\"><b>Kịch bản 3 (Bão cytokine / Adenovirus):</b></span> WBC tăng, không chuyển trái + <span style=\"color:#ff6b6b\"><b>CRP tăng vọt &gt; 100 mg/L</b></span> nhưng <span style=\"color:#51cf66\"><b>PCT thấp &lt; 0.5 ng/mL</b></span> → <span style=\"color:#74c0fc\"><b>Cảnh giác virus độc lực cao, tìm PCR, tránh leo thang kháng sinh mù quáng</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Tam giác này bù trừ hoàn hảo cho nhau: Công thức máu đánh giá tế bào học, CRP phản ánh mức độ viêm toàn thể, Procalcitonin định danh chính xác bản chất vi khuẩn.",
    "extra": "📖 Nguồn: PIDS/IDSA CAP Guidelines & Surviving Sepsis Campaign (PED-63, Mục 7)",
    "tags": [
      "PED-63",
      "B7-Biomarkers",
      "Tam-giac-chan-doan"
    ]
  },
  {
    "id": "PED63-B8-01",
    "type": "basic",
    "section": "B8",
    "category": "Hạt ngọc lâm sàng bỏ túi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nội dung và ý nghĩa của <span style=\"color:#ffd43b\"><b>Clinical Pearl 1 & 2</b></span>: 'Đừng đọc công thức máu nhi bằng mắt người lớn' và 'Tỷ lệ % là ảo tưởng, số lượng tuyệt đối là chân lý' là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#74c0fc\"><b>Pearl 1 ('Đừng đọc bằng mắt người lớn'):</b></span> Mọi giá trị bình thường của người lớn đều có thể là bệnh lý ở trẻ nhỏ (và ngược lại); luôn mang theo bảng tham chiếu theo lứa tuổi khi đi buồng bệnh.<br>• <span style=\"color:#ffd43b\"><b>Pearl 2 ('% là ảo tưởng, tuyệt đối là chân lý'):</b></span> Không bao giờ đưa ra chẩn đoán dựa trên tỷ lệ % đơn thuần; luôn tính ANC trước khi kết luận tăng hay giảm bạch cầu trung tính.<br><br><b>💡 Giải thích của AI:</b><br>Hai viên ngọc nền tảng này giúp bác sĩ giải thoát khỏi tư duy rập khuôn và bảo vệ bệnh nhi khỏi các phán đoán vội vàng khi nhìn vào tờ kết quả xét nghiệm in sẵn.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 8)",
    "tags": [
      "PED-63",
      "B8-Clinical-Pearls"
    ]
  },
  {
    "id": "PED63-B8-02",
    "type": "basic",
    "section": "B8",
    "category": "Hạt ngọc lâm sàng bỏ túi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nội dung và ý nghĩa của <span style=\"color:#ffd43b\"><b>Clinical Pearl 3 & 4</b></span>: 'Quy tắc 5 ngày – 5 tuổi' và 'I/T ratio &gt; 0.20 ở trẻ sơ sinh là phát súng báo động đỏ' là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#74c0fc\"><b>Pearl 3 ('Quy tắc 5 ngày – 5 tuổi'):</b></span> Ghi nhớ hai mốc giao cắt cân bằng 45%–45% giữa Neutrophil và Lymphocyte: Ngày thứ 5 sau sinh và năm 5 tuổi; nằm giữa hai mốc này Lympho luôn nhiều hơn Neutrophil.<br>• <span style=\"color:#ff6b6b\"><b>Pearl 4 ('I/T ratio &gt; 0.20 là báo động đỏ'):</b></span> Ở trẻ sơ sinh nghi ngờ nhiễm trùng, I/T ratio &gt; 0.20 là chỉ dấu nhạy nhất chỉ điểm nhiễm khuẩn huyết sớm; tuyệt đối không trì hoãn kháng sinh để đợi kết quả cấy máu.<br><br><b>💡 Giải thích của AI:</b><br>Pearl 3 giải quyết nhanh câu hỏi cấu trúc công thức máu sinh lý; Pearl 4 thiết lập phản xạ cấp cứu cứu sống trẻ sơ sinh trong những giờ vàng đầu tiên.",
    "extra": "📖 Nguồn: Manroe BL et al. & Nelson Textbook of Pediatrics (PED-63, Mục 8)",
    "tags": [
      "PED-63",
      "B8-Clinical-Pearls"
    ]
  },
  {
    "id": "PED63-B8-03",
    "type": "basic",
    "section": "B8",
    "category": "Hạt ngọc lâm sàng bỏ túi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nội dung và ý nghĩa của <span style=\"color:#ffd43b\"><b>Clinical Pearl 5 & 6</b></span>: 'Ho gà là vi khuẩn đội lốt virus' và 'Thương hàn và Sốc nhiễm khuẩn: Bạch cầu càng thấp, bệnh càng nặng' là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ff6b6b\"><b>Pearl 5 ('Ho gà là vi khuẩn đội lốt virus'):</b></span> Ho gà là vi khuẩn nhưng gây tăng vọt bạch cầu 50.000 với 80% lympho do độc tố PT bẫy lympho trong máu; cẩn thận nguy cơ tắc mạch phổi tử vong ở trẻ nhũ nhi.<br>• <span style=\"color:#ff6b6b\"><b>Pearl 6 ('Bạch cầu càng thấp, bệnh càng nặng'):</b></span> Trong bối cảnh nhiễm trùng nặng hoặc sốc tụt áp, hạ bạch cầu (&lt; 4.000/mm³) không phải là nhẹ mà là tiên lượng cạn kiệt tủy tử vong cực cao.<br><br><b>💡 Giải thích của AI:</b><br>Hai nghịch lý huyết học này là vũ khí giúp bác sĩ không bị rơi vào bẫy 'bạch cầu thấp là nhẹ' hay 'tăng lympho là virus'.",
    "extra": "📖 Nguồn: Surviving Sepsis Campaign & Nelson Ch.218 (PED-63, Mục 8)",
    "tags": [
      "PED-63",
      "B8-Clinical-Pearls"
    ]
  },
  {
    "id": "PED63-B8-04",
    "type": "basic",
    "section": "B8",
    "category": "Hạt ngọc lâm sàng bỏ túi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nội dung và ý nghĩa của <span style=\"color:#ffd43b\"><b>Clinical Pearl 7 & 8</b></span>: 'Hạt độc và Không bào có giá trị hơn mọi con số' và 'Corticoid làm tăng bạch cầu giả tạo' là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ff6b6b\"><b>Pearl 7 ('Hạt độc và Không bào hơn mọi con số'):</b></span> Sự biến đổi chất lượng tế bào (hạt độc, thể Döhle, không bào) phản ánh trung thực bản chất nhiễm khuẩn nặng hơn là sự thay đổi số lượng đơn thuần.<br>• <span style=\"color:#51cf66\"><b>Pearl 8 ('Corticoid gây tăng bạch cầu giả tạo'):</b></span> Tăng bạch cầu sau dùng Corticoid là do hiệu ứng tróc mạch (Demargination) chứ không phải nhiễm trùng mới; phân biệt bằng việc không có chuyển trái và không có hạt độc.<br><br><b>💡 Giải thích của AI:</b><br>Pearl 7 tôn vinh giá trị của xét nghiệm soi lam kính hiển vi thủ công; Pearl 8 giải oan cho các ca tăng bạch cầu sau tiêm Corticoid.",
    "extra": "📖 Nguồn: Wintrobe's Hematology & Dale DC et al. (PED-63, Mục 8)",
    "tags": [
      "PED-63",
      "B8-Clinical-Pearls"
    ]
  },
  {
    "id": "PED63-B8-05",
    "type": "basic",
    "section": "B8",
    "category": "Hạt ngọc lâm sàng bỏ túi",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Nội dung và ý nghĩa của <span style=\"color:#ffd43b\"><b>Clinical Pearl 9 & 10</b></span>: 'Procalcitonin là trọng tài công tâm nhất' và 'Không bao giờ điều trị một tờ giấy xét nghiệm' là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#51cf66\"><b>Pearl 9 ('PCT là trọng tài công tâm nhất'):</b></span> Khi CRP tăng rất cao mà phân vân giữa vi khuẩn và Adenovirus, hãy nhìn vào Procalcitonin: PCT &lt; 0.25 ng/mL là tấm khiên vững chắc giúp bạn trì hoãn kháng sinh an toàn.<br>• <span style=\"color:#51cf66\"><b>Pearl 10 ('Không bao giờ điều trị một tờ giấy xét nghiệm'):</b></span> Luôn luôn điều trị toàn diện đứa trẻ: một đứa trẻ hồng hào, tươi tỉnh, bú tốt với một con số xét nghiệm bất thường thì hãy tin vào đứa trẻ trước tiên.<br><br><b>💡 Giải thích của AI:</b><br>Đây là tôn chỉ hành nghề tối cao của người thầy thuốc Nhi khoa: lâm sàng luôn luôn là thuyền trưởng định hướng mọi quyết định can thiệp y khoa.",
    "extra": "📖 Nguồn: Schuetz P et al. & Nelson Textbook of Pediatrics (PED-63, Mục 8)",
    "tags": [
      "PED-63",
      "B8-Clinical-Pearls"
    ]
  },
  {
    "id": "PED63-B9-01",
    "type": "basic",
    "section": "B9",
    "category": "Ca lâm sàng thực chiến",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ca lâm sàng 1 (Bước 1 & 2): Trẻ 8 tháng tuổi sốt 39°C, chảy mũi trong, ho húng hắng 2 ngày; khám phổi thở đều không co kéo; xét nghiệm: <span style=\"color:#ffd43b\"><b>WBC 15.000 /mm³, Neutrophil 28%, Lymphocyte 65%, Monocyte 7%</b></span> — Phân tích <span style=\"color:#ff6b6b\"><b>bẫy chẩn đoán nếu đọc theo chuẩn người lớn</b></span> và <span style=\"color:#51cf66\"><b>đánh giá chuẩn theo tuổi</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Bước 1 (Bẫy chẩn đoán nếu áp chuẩn người lớn):</b></span> Bác sĩ nhìn thấy Neutrophil 28% (chuẩn người lớn 60%–70%) vội vàng kết luận 'Bệnh nhân bị giảm bạch cầu hạt / Suy tủy / Nhiễm virus nặng lấn át tủy'.<br>2) <span style=\"color:#51cf66\"><b>Bước 2 (Đánh giá chuẩn theo lứa tuổi 8 tháng):</b></span><br>• Ở lứa tuổi 8 tháng (nằm giữa 5 ngày và 5 tuổi), <span style=\"color:#51cf66\"><b>Lymphocyte 60% – 70% và Neutrophil 25% – 30% là tỷ lệ sinh lý hoàn toàn bình thường</b></span>.<br>• Tính số lượng tuyệt đối: <span style=\"color:#ffd43b\"><b>ANC = 15.000 × 28% = 4.200 /mm³</b></span> → số lượng bạch cầu trung tính hoàn toàn bình thường, không hề bị suy giảm.<br><br><b>💡 Giải thích của AI:</b><br>Hiểu đúng sinh lý bắt chéo giúp bác sĩ nhận ra đứa trẻ hoàn toàn không có bất thường về tỷ lệ dòng tế bào, giải tỏa nỗi lo âu vô lý cho phụ huynh.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Mục 9, Ca 1)",
    "tags": [
      "PED-63",
      "B9-Ca-lam-sang",
      "Ca-1",
      "Dien-giai-sinh-ly"
    ]
  },
  {
    "id": "PED63-B9-02",
    "type": "basic",
    "section": "B9",
    "category": "Ca lâm sàng thực chiến",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ca lâm sàng 1 (Bước 3, 4 & 5): Kết quả <span style=\"color:#ffd43b\"><b>CRP 8 mg/L</b></span> ở trẻ 8 tháng tuổi nói trên — Phân tích <span style=\"color:#74c0fc\"><b>bản chất nhiễm trùng</b></span> và kế hoạch <span style=\"color:#51cf66\"><b>xử trí kháng sinh an toàn</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#74c0fc\"><b>Bước 3 (Phân tích chỉ số viêm CRP):</b></span> Nồng độ CRP 8 mg/L (&lt; 10 mg/L) khẳng định không có phản ứng viêm pha cấp hệ thống của nhiễm khuẩn nặng.<br>2) <span style=\"color:#74c0fc\"><b>Bước 4 (Kết luận bản chất):</b></span> Trẻ bị <span style=\"color:#74c0fc\"><b>Viêm đường hô hấp trên cấp tính do virus thông thường</b></span> (WBC tăng nhẹ do phản ứng sốt cấp, tỷ lệ bạch cầu bình thường theo tuổi, CRP âm tính).<br>3) <span style=\"color:#51cf66\"><b>Bước 5 (Kế hoạch xử trí an toàn):</b></span> <span style=\"color:#51cf66\"><b>TUYỆT ĐỐI KHÔNG DÙNG KHÁNG SINH</b></span>; chỉ định hạ sốt bằng Paracetamol (10–15 mg/kg mỗi 4–6h khi sốt ≥ 38.5°C), nhỏ mũi nước muối sinh lý, bú mẹ tăng cường và hướng dẫn theo dõi các dấu hiệu cảnh báo cần tái khám (thở nhanh, bỏ bú, li bì).<br><br><b>💡 Giải thích của AI:</b><br>Đây là quyết định kê đơn thực chứng mẫu mực: một xét nghiệm máu không có dấu ấn vi khuẩn kết hợp với lâm sàng hô hấp trên cho phép an tâm trì hoãn hoàn toàn kháng sinh.",
    "extra": "📖 Nguồn: AAP Guidelines & Clinical Case Records (PED-63, Mục 9, Ca 1)",
    "tags": [
      "PED-63",
      "B9-Ca-lam-sang",
      "Ca-1",
      "Dieu-tri"
    ]
  },
  {
    "id": "PED63-B9-03",
    "type": "basic",
    "section": "B9",
    "category": "Ca lâm sàng thực chiến",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ca lâm sàng 2 (Bước 1 & 2): Trẻ sơ sinh 3 ngày tuổi vào viện vì bỏ bú, hạ thân nhiệt 35.8°C, da tái nổi vân tím nhẹ, thở rên (Grunting); xét nghiệm: <span style=\"color:#ff6b6b\"><b>WBC 4.800 /mm³, Neutrophil đoạn (Segs) 35%, Bạch cầu đũa (Bands) 25%, Hậu tủy bào (Metamyelocytes) 5%</b></span> — Phân tích các <span style=\"color:#ff6b6b\"><b>dấu hiệu cờ đỏ lâm sàng</b></span> và <span style=\"color:#ff6b6b\"><b>tình trạng huyết học</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#ff6b6b\"><b>Bước 1 (Nhận diện cờ đỏ lâm sàng tối khẩn):</b></span> Tam chứng <span style=\"color:#ff6b6b\"><b>Hạ thân nhiệt (35.8°C) + Thở rên (Grunting) + Da nổi vân tím</b></span> ở trẻ sơ sinh 3 ngày tuổi là các dấu hiệu cờ đỏ báo hiệu <span style=\"color:#ff6b6b\"><b>Nhiễm khuẩn huyết sơ sinh sớm (Early-Onset Sepsis - EOS) kèm sốc nhiễm trùng</b></span> đe dọa ngừng thở tử vong.<br>2) <span style=\"color:#ff6b6b\"><b>Bước 2 (Phân tích huyết học - Giảm bạch cầu nguy kịch):</b></span> Ở trẻ sơ sinh 3 ngày tuổi, mức bạch cầu sinh lý phải từ 10.000 đến 25.000 /mm³. Kết quả <span style=\"color:#ff6b6b\"><b>WBC 4.800 /mm³ là tình trạng GIẢM BẠCH CẦU NẶNG NỀ</b></span>, chỉ điểm tủy xương đã cạn kiệt nguồn dự trữ tế bào hạt do ổ nhiễm trùng tiêu thụ quá ồ ạt.<br><br><b>💡 Giải thích của AI:</b><br>Hạ thân nhiệt và hạ bạch cầu ở sơ sinh nguy hiểm gấp bội so với sốt cao và tăng bạch cầu; đây là biểu hiện của suy sụp khả năng tự vệ của cơ thể sơ sinh non nớt.",
    "extra": "📖 Nguồn: Gomella's Neonatology 8th & Nelson 21st Ch.132 (PED-63, Mục 9, Ca 2)",
    "tags": [
      "PED-63",
      "B9-Ca-lam-sang",
      "Ca-2",
      "So-sinh-Sepsis"
    ]
  },
  {
    "id": "PED63-B9-04",
    "type": "basic",
    "section": "B9",
    "category": "Ca lâm sàng thực chiến",
    "badge": "EBM Master",
    "badge_class": "badge-ebm",
    "front": "Ca lâm sàng 2 (Bước 3, 4 & 5): Tính toán <span style=\"color:#51cf66\"><b>Chỉ số I/T ratio</b></span> và thiết lập kế hoạch <span style=\"color:#51cf66\"><b>hồi sức cấp cứu & kháng sinh theo kinh nghiệm</b></span> cho trẻ sơ sinh 3 ngày tuổi nói trên?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Bước 3 (Tính toán chỉ số I/T ratio):</b></span><br>• Tổng tế bào non (Immature) = Bands 25% + Metamyelocytes 5% = 30%.<br>• Tổng số Neutrophil = Immature 30% + Segs 35% = 65%.<br>• <div style=\"font-weight:bold;color:#ff6b6b;margin:4px 0;\">I/T ratio = 30 / 65 = 0.46 (vượt xa ngưỡng cờ đỏ 0.20)</div> → Khẳng định hiện tượng <span style=\"color:#ff6b6b\"><b>Chuyển trái cực độ</b></span>, xác nhận 99% nhiễm khuẩn huyết sơ sinh tối cấp.<br>2) <span style=\"color:#51cf66\"><b>Bước 4 (Cận lâm sàng cấp cứu):</b></span> Cấy máu ngay 2 vị trí, chọc dò tủy sống lấy dịch não tủy (CSF) tìm viêm màng não mủ, cấy nước tiểu, định lượng Procalcitonin và khí máu động mạch.<br>3) <span style=\"color:#51cf66\"><b>Bước 5 (Kế hoạch hồi sức & Kháng sinh tĩnh mạch khẩn cấp):</b></span><br>• Ủ ấm lồng ấp, hỗ trợ hô hấp bằng CPAP hoặc thở máy qua nội khí quản.<br>• Bắt đầu ngay kháng sinh tĩnh mạch phổ rộng kết hợp diệt GBS và trực khuẩn Gram âm: <span style=\"color:#51cf66\"><b>Ampicillin (100–150 mg/kg/ngày) + Gentamicin (4–5 mg/kg/ngày)</b></span> hoặc Cefotaxime trong vòng 60 phút đầu tiên.<br><br><b>💡 Giải thích của AI:</b><br>Chỉ số I/T ratio = 0.46 là bằng chứng đanh thép nhất buộc bác sĩ phải hành động cấp cứu ngay mà không được phép chần chừ đợi kết quả vi sinh.",
    "extra": "📖 Nguồn: AAP Committee on Fetus and Newborn & CDC Neonatal Sepsis Guidelines (PED-63, Mục 9, Ca 2)",
    "tags": [
      "PED-63",
      "B9-Ca-lam-sang",
      "Ca-2",
      "IT-ratio",
      "Cap-cuu"
    ]
  },
  {
    "id": "PED63-ALG-01",
    "type": "basic",
    "section": "B4",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Thuật toán 30 giây:</b></span> <span style=\"color:#ffd43b\"><b>Công thức tính nhanh</b></span> và <span style=\"color:#ff6b6b\"><b>bảng giải mã 4 ngưỡng ANC</b></span> để ra quyết định xử trí nhiễm trùng tại giường là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Công thức tính nhanh ANC:</b></span><br><div style=\"text-align:center;font-weight:bold;color:#ffd43b;margin:4px 0;\">ANC (/mm³) = WBC (/mm³) × (% Segs + % Bands) / 100</div><br>2) <span style=\"color:#ff6b6b\"><b>Bảng giải mã 4 ngưỡng hành động lâm sàng:</b></span><br>• <span style=\"color:#ff6b6b\"><b>ANC &lt; 500 /mm³ (CỜ ĐỎ TỐI KHẨN):</b></span> Sốt giảm bạch cầu hạt nặng → Cấy máu ngay + Bắt đầu kháng sinh diệt trực khuẩn mủ xanh tĩnh mạch trong 60 phút (Cefepime/Meropenem).<br>• <span style=\"color:#ffd43b\"><b>ANC 500 – 1.000 /mm³:</b></span> Nguy cơ nhiễm trùng vừa → Theo dõi sát sinh hiệu, cách ly phòng sạch, hạn chế thủ thuật xâm lấn.<br>• <span style=\"color:#ffd43b\"><b>ANC 1.000 – 1.500 /mm³:</b></span> Giảm nhẹ → Tìm nguyên nhân (thuốc, virus thoáng qua), theo dõi công thức máu sau 48–72h.<br>• <span style=\"color:#51cf66\"><b>ANC &gt; 7.000 – 8.000 /mm³ (trẻ nhỏ) hoặc &gt; 10.000 /mm³ (trẻ lớn):</b></span> Tăng bạch cầu hạt thực sự → Định hướng ổ nhiễm trùng vi khuẩn.<br><br><b>💡 Giải thích của AI:</b><br>Thuật toán 30 giây này giúp bác sĩ tại phòng khám cấp cứu định lượng chính xác nguy cơ nhiễm khuẩn của trẻ, không bị đánh lừa bởi tỷ lệ % trên giấy in sẵn.",
    "extra": "📖 Nguồn: IDSA Guidelines for Neutropenic Patients & Nelson Textbook (PED-63, Thuật toán quyết định)",
    "tags": [
      "PED-63",
      "Thuat-toan",
      "ANC",
      "Cap-cuu"
    ]
  },
  {
    "id": "PED63-ALG-02",
    "type": "basic",
    "section": "B4",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Thuật toán sơ sinh:</b></span> <span style=\"color:#ffd43b\"><b>Công thức tính I/T ratio</b></span>, <span style=\"color:#ff6b6b\"><b>ngưỡng cờ đỏ chỉ điểm EOS</b></span> và <span style=\"color:#51cf66\"><b>gói hành động cấp cứu 60 phút đầu</b></span> là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <span style=\"color:#51cf66\"><b>Công thức:</b></span><br><div style=\"text-align:center;font-weight:bold;color:#ffd43b;margin:4px 0;\">I/T ratio = (Bands + Metas + Myelos) / (Tổng Neutrophil = Immature + Segs)</div><br>2) <span style=\"color:#ff6b6b\"><b>Điểm cắt cờ đỏ:</b></span> <span style=\"color:#ff6b6b\"><b>I/T ratio &gt; 0.20</b></span> (ở trẻ sơ sinh nghi ngờ nhiễm khuẩn huyết sớm EOS).<br>3) <span style=\"color:#51cf66\"><b>Gói hành động cấp cứu 60 phút đầu (EOS Bundle):</b></span><br>• Cấy máu 2 vị trí trước khi dùng kháng sinh.<br>• Chọc dò dịch não tủy (CSF) nếu trẻ có triệu chứng thần kinh hoặc huyết động ổn định.<br>• <span style=\"color:#51cf66\"><b>Kháng sinh tĩnh mạch kinh nghiệm ngay trong 60 phút:</b></span> Ampicillin (100–150 mg/kg/ngày) + Gentamicin (4–5 mg/kg/ngày).<br>• Hồi sức sinh tồn: Giữ ấm lồng ấp, hỗ trợ hô hấp CPAP, kiểm soát tốc độ truyền đường GIR.<br><br><b>💡 Giải thích của AI:</b><br>I/T ratio > 0.20 có độ nhạy vượt trội trong 72 giờ đầu đời; đây là chỉ định kích hoạt gói hành động cấp cứu EOS không được phép trì hoãn.",
    "extra": "📖 Nguồn: AAP Neonatal Sepsis Guidelines & CDC (PED-63, Thuật toán quyết định)",
    "tags": [
      "PED-63",
      "Thuat-toan",
      "IT-ratio",
      "So-sinh"
    ]
  },
  {
    "id": "PED63-ALG-03",
    "type": "basic",
    "section": "B7",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Lưu đồ quyết định nhị phân:</b></span> Phác đồ 3 nhánh quyết định <span style=\"color:#51cf66\"><b>DÙNG KHÁNG SINH</b></span> hay <span style=\"color:#ffd43b\"><b>TRÌ HOÃN KHÁNG SINH</b></span> tại giường dựa trên <span style=\"color:#74c0fc\"><b>Tam giác chẩn đoán (Lâm sàng + ANC + Procalcitonin/CRP)</b></span>?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>• <span style=\"color:#ff6b6b\"><b>NHÁNH 1 (BẮT BUỘC DÙNG KHÁNG SINH):</b></span><br>Lâm sàng có ổ nhiễm khuẩn rõ hoặc dấu hiệu cờ đỏ + ANC tăng cao (kèm chuyển trái/hạt độc) + <span style=\"color:#ff6b6b\"><b>Procalcitonin &gt; 0.5 – 2.0 ng/mL</b></span> (hoặc CRP &gt; 40–60 mg/L) → <span style=\"color:#51cf66\"><b>Kháng sinh đích sớm đúng liều</b></span>.<br>• <span style=\"color:#51cf66\"><b>NHÁNH 2 (TRÌ HOÃN KHÁNG SINH AN TOÀN):</b></span><br>Lâm sàng tươi tỉnh, không suy hô hấp, không ổ mủ + ANC bình thường theo tuổi (không chuyển trái, không hạt độc) + <span style=\"color:#51cf66\"><b>Procalcitonin &lt; 0.25 ng/mL + CRP &lt; 10–20 mg/L</b></span> → <span style=\"color:#51cf66\"><b>KHÔNG DÙNG kháng sinh</b></span>, chăm sóc triệu chứng, theo dõi ngoại trú.<br>• <span style=\"color:#74c0fc\"><b>NHÁNH 3 (BẪY BÃO ADENOVIRUS / VIRUS ĐỘC LỰC CAO):</b></span><br>Sốt cao liên tục, <span style=\"color:#ff6b6b\"><b>CRP tăng vọt &gt; 100 mg/L</b></span> NHƯNG <span style=\"color:#51cf66\"><b>Procalcitonin &lt; 0.5 ng/mL</b></span>, không chuyển trái → <span style=\"color:#74c0fc\"><b>Không leo thang kháng sinh mù quáng</b></span>; test PCR virus, điều trị nâng đỡ.<br><br><b>💡 Giải thích của AI:</b><br>Lưu đồ 3 nhánh này là chuẩn mực tối thượng để thực hành kháng sinh an toàn (Antimicrobial Stewardship), bảo vệ trẻ khỏi tình trạng lạm dụng kháng sinh vô ích.",
    "extra": "📖 Nguồn: PIDS/IDSA CAP Guidelines & Surviving Sepsis Campaign (PED-63, Thuật toán quyết định)",
    "tags": [
      "PED-63",
      "Thuat-toan",
      "Tam-giac-chan-doan",
      "Khang-sinh"
    ]
  },
  {
    "id": "PED63-ALG-04",
    "type": "basic",
    "section": "B5",
    "category": "Thuật toán ra quyết định nhanh",
    "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "badge_class": "badge-ebm",
    "front": "<span style=\"color:#51cf66\"><b>Lưu đồ phản xạ loại trừ:</b></span> 4 bước nhận diện các <span style=\"color:#ff6b6b\"><b>bẫy ngoại lệ huyết học kinh điển</b></span> khi công thức bạch cầu mâu thuẫn với lâm sàng là gì?",
    "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sốt + Bạch cầu GIẢM (&lt; 4.000/mm³):</b> Loại trừ ngay <span style=\"color:#ff6b6b\"><b>Thương hàn</b></span> (kiểm tra bạch cầu ái toan = 0%, mạch nhiệt phân ly) hoặc <span style=\"color:#ff6b6b\"><b>Sốc nhiễm khuẩn tối cấp</b></span> (cạn kiệt tủy, nổi vân tím).<br>2) <b>Ho dữ dội + Bạch cầu TĂNG VỌT (&gt; 30.000 – 50.000/mm³) ưu thế Lympho:</b> Nghĩ ngay đến <span style=\"color:#ff6b6b\"><b>Ho gà (Bordetella pertussis)</b></span> do độc tố PT bẫy lympho trong máu; cẩn thận nguy cơ tắc mạch phổi.<br>3) <b>Trẻ &lt; 5 tuổi có Lympho 60% – 70%:</b> Khẳng định đây là <span style=\"color:#51cf66\"><b>sinh lý bắt chéo bình thường</b></span>; chỉ kết luận nhiễm khuẩn khi ANC tăng hoặc có chuyển trái và hạt độc.<br>4) <b>Bạch cầu tăng vọt sau khí dung/tiêm Corticoid:</b> Khẳng định <span style=\"color:#51cf66\"><b>hiệu ứng bóc tróc mạch (Demargination)</b></span> nếu không có chuyển trái và không có hạt độc.<br><br><b>💡 Giải thích của AI:</b><br>Bốn phản xạ này giúp bác sĩ luôn cảnh giác với các ngoại lệ huyết học, không để những kết quả xét nghiệm bất thường đánh lừa tư duy lâm sàng.",
    "extra": "📖 Nguồn: Nelson Textbook of Pediatrics 21st Ch.503 (PED-63, Thuật toán quyết định)",
    "tags": [
      "PED-63",
      "Thuat-toan",
      "Ngoai-le",
      "Phan-xa"
    ]
  }
]
