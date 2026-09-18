import json
from pathlib import Path

cards_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.cards.v2.json")
cards = json.loads(cards_path.read_text(encoding="utf-8"))

def add_c(text, extra=""):
    cards.append({"type": "cloze", "text": text, "extra": extra})

add_c("Thuốc lợi tiểu Thiazide thường dùng duy trì ở trẻ em là {{c1::Hydrochlorothiazide}}, với liều lượng từ {{c1::1 đến 2 mg/kg/ngày}} uống chia làm 2 lần.",
      "Dược lý: Tác động lên đoạn đầu ống lượn xa, hiệu quả vừa phải và luôn cần theo dõi bù Kali.")

add_c("Trong điều trị kháng thuốc lợi tiểu ở trẻ suy tim nặng, thuốc lợi tiểu thiazide-like đường uống thường được phối hợp với Furosemid là {{c1::Metolazone}}, với liều dùng từ {{c1::0,2 đến 0,4 mg/kg/ngày}}.",
      "Cơ chế: Phong bế nephron tuần tự, ức chế tái hấp thu muối nước bù trừ tại ống lượn xa.")

add_c("Bên cạnh tác dụng lợi tiểu giữ Kali, Spironolacton còn có vai trò bảo vệ tim mạch lâu dài quan trọng là {{c1::chống xơ hóa cơ tim và ức chế tái cấu trúc thất trái}}.",
      "Cơ chế: Kháng tác động gây xơ hóa và chết tế bào của Aldosterone trên mô kẽ cơ tim.")

add_c("Thuốc ức chế men chuyển tác dụng kéo dài dùng cho trẻ lớn có thể uống 1 đến 2 lần mỗi ngày là {{c1::Enalapril}}, với liều duy trì từ {{c1::0,1 đến 0,5 mg/kg/ngày}}.",
      "Dược lý: Được chuyển hóa tại gan thành Enalaprilat có hoạt tính, tiện lợi trong điều trị ngoại trú dài hạn.")

add_c("Mục tiêu liều đích duy trì của thuốc chẹn beta Carvedilol trong điều trị suy tim mạn tính ở trẻ em là {{c1::0,2 đến 0,4 mg/kg/ngày}} (chia làm 2 lần uống).",
      "Thực hành: Bắt đầu từ liều thăm dò 0,05 mg/kg/liều và tăng gấp đôi liều mỗi 2 tuần nếu dung nạp tốt.")

add_c("Cơ chế phân tử của Milrinone là ức chế enzyme Phosphodiesterase-3 (PDE-3), dẫn đến làm tăng nồng độ chất truyền tin thứ hai {{c1::cAMP (cyclic AMP)}} bên trong tế bào cơ tim và cơ trơn mạch máu.",
      "Dược lý: cAMP tăng làm tăng dòng canxi vào cơ tim (tăng co bóp) và giãn cơ trơn thành mạch (giảm tiền gánh và hậu gánh).")

add_c("Thuốc tăng co bóp cơ tim Dobutamin tác động kích thích chủ yếu và chọn lọc lên thụ thể {{c1::beta-1 adrenergic}} trên màng tế bào cơ tim.",
      "Dược lý: Kích thích thụ thể này làm tăng nồng độ canxi nội bào qua trung gian protein Gs, tăng sức co bóp mà ít gây co mạch ngoại biên.")

add_c("Thuốc vận mạch Dopamin ở dải liều thấp (1 đến 3 µg/kg/phút) kích thích chọn lọc lên thụ thể {{c1::Dopaminergic tại giường mạch thận và tạng}}.",
      "Dược lý: Liều này làm giãn mạch thận, nhưng hiện nay không còn được khuyến cáo dùng đơn độc chỉ để bảo vệ thận.")

add_c("Thuốc vận mạch co mạch đầu tay được lựa chọn khi suy tim cấp có tụt huyết áp nặng trơ với Dopamin và Dobutamin là {{c1::Norepinephrine (Noradrenalin)}} với liều truyền từ {{c1::0,05 đến 0,1 µg/kg/phút}}.",
      "Dược lý: Kích thích mạnh thụ thể alpha-1 gây co mạch nâng huyết áp trung bình, kèm kích thích nhẹ beta-1 hỗ trợ co bóp cơ tim.")

add_c("Khi truyền Nitroprusside kéo dài trên 48 đến 72 giờ hoặc ở bệnh nhân có suy giảm chức năng thận, cần cảnh giác nguy cơ ngộ độc chuyển hóa do tích lũy {{c1::Cyanide và Thiocyanate}}.",
      "Cảnh báo: Biểu hiện ngộ độc gồm toan lactic tiến triển, lú lẫn, co giật và tụt huyết áp trơ.")

add_c("Ở trẻ sơ sinh non tháng hoặc bệnh nhi có suy giảm chức năng thận, tổng liều tấn công số hóa Digoxin cần được giảm bớt {{c1::50%}} xuống còn {{c1::0,02 đến 0,03 mg/kg}}.",
      "Dược lý: Trẻ non tháng và suy thận có độ thanh thải Digoxin qua cầu thận giảm mạnh, nguy cơ ngộ độc rất cao.")

add_c("Khi chuyển đổi thuốc Digoxin từ đường uống sang đường tiêm tĩnh mạch, liều tiêm tĩnh mạch chỉ bằng {{c1::75% liều uống}}.",
      "Dược lý: Do sinh khả dụng của dạng cồn ngọt hoặc viên nén Digoxin đường uống chỉ đạt khoảng 70% đến 80% so với tiêm TM.")

add_c("Triệu chứng ngộ độc Digoxin trên thị giác ở trẻ lớn có hiện tượng nhìn thấy quầng màu vàng hoặc màu xanh lá cây quanh nguồn sáng, thuật ngữ y khoa gọi là {{c1::Xanthopsia}}.",
      "Cơ chế: Độc tính ức chế bơm ion Na+/K+-ATPase trên tế bào nón của võng mạc mắt.")

add_c("Các triệu chứng ngộ độc Digoxin trên đường tiêu hóa thường xuất hiện sớm nhất bao gồm: {{c1::biếng ăn đột ngột, buồn nôn, nôn mửa liên tục và đau bụng}}.",
      "Lâm sàng: Khi trẻ đang dùng Digoxin có nôn trớ bất thường, phản xạ đầu tiên là phải tạm dừng thuốc và kiểm tra nồng độ thuốc máu.")

add_c("Rối loạn nhịp tim được coi là đặc trưng nhất và gợi ý cao nhất cho ngộ độc Digitalis trên điện tâm đồ là {{c1::nhịp nhanh nhĩ kèm block nhĩ thất (PAT with block)}}.",
      "Điện tim: Vừa tăng tính tự động của ổ ngoại vị nhĩ vừa ức chế dẫn truyền qua nút nhĩ thất.")

add_c("Kháng thể DigiFab trung hòa độc tính của Digoxin bằng cách gắn kết với phân tử Digoxin tự do với ái lực cao hơn thụ thể Na+/K+-ATPase của cơ tim tới {{c1::1000 lần}}.",
      "Dược lý: Tạo phức hợp kháng nguyên - kháng thể trơ không độc và được đào thải nhanh chóng qua nước tiểu.")

add_c("Trong xử trí cơn phù phổi cấp do suy tim trái, tư thế nằm đầu cao Fowler góc 30 đến 45 độ giúp làm giảm tải lượng máu tĩnh mạch hồi lưu từ hai chi dưới về buồng tim phải theo cơ chế {{c1::trọng lực}}.",
      "Cơ chế: Giảm tiền gánh thất phải gián tiếp làm giảm lượng máu ứ ngập lên mao mạch phổi.")

add_c("Thở áp lực dương liên tục (CPAP) trong suy tim cấp có ứ huyết phổi giúp cải thiện chức năng thất trái nhờ cơ chế {{c1::làm tăng áp lực trong lồng ngực, từ đó làm giảm áp lực xuyên thành thất trái (giảm hậu gánh thất trái)}}.",
      "Cơ chế: Đồng thời đẩy dịch phế nang ngược trở lại mô kẽ và tuần hoàn bạch huyết.")

add_c("Trong thang điểm Ross cải tiến, tiêu chí tần số tim lúc nghỉ ngơi được tính 2 điểm khi tần số tim tăng cao hơn bình thường theo tuổi trên {{c1::> 20 nhịp/phút}}.",
      "Phân tầng: Tăng 10-20 nhịp/phút tính 1 điểm; bình thường theo tuổi tính 0 điểm.")

add_c("Trong thang điểm Ross cải tiến, tiêu chí tần số thở lúc nghỉ ngơi được tính 2 điểm khi tần số thở tăng cao hơn giới hạn bình thường theo tuổi trên {{c1::> 20 nhịp/phút}}.",
      "Phân tầng: Thở nhanh > 20 nhịp so với ngưỡng sinh lý là dấu hiệu suy tim tiến triển.")

add_c("Chỉ số tim - ngực (CTR) trên phim X-quang tim phổi thẳng ở trẻ sơ sinh được coi là bóng tim to bệnh lý khi tỷ lệ này vượt quá {{c1::> 0,60}}.",
      "Chẩn đoán: Ở trẻ sơ sinh lồng ngực hình trụ và cơ hoành nằm ngang nên chỉ số tim ngực sinh lý cao hơn trẻ lớn.")

add_c("Đường Kerley B trên X-quang ngực thẳng là các đường mờ mảnh dài 1 đến 2 cm nằm ngang sát màng phổi ở góc sườn hoành, hình thành do {{c1::sự tích tụ dịch phù nề trong các vách liên tiểu thùy phổi}}.",
      "Hình ảnh: Là dấu hiệu kinh điển của tình trạng ứ dịch mô kẽ mạn tính do tăng áp lực nhĩ trái.")

add_c("Hội chứng suy tuần hoàn ngoại vi trong sốc tim được xác định khi thời gian đổ đầy mao mạch (Capillary Refill Time - CRT) kéo dài trên {{c1::> 3 giây}}.",
      "Lâm sàng: Khám bằng cách ấn ngón tay cái lên xương ức hoặc gan bàn chân trẻ trong 5 giây rồi buông ra đếm thời gian hồng trở lại.")

add_c("Ở bệnh nhi suy tim nhũ nhi đang điều trị nội khoa, mức tăng cân đột ngột vượt quá {{c1::> 30 đến 50 g/ngày}} phản ánh tình trạng ứ dịch chứ không phải tăng trưởng dinh dưỡng.",
      "Theo dõi: Đòi hỏi bác sĩ phải tăng liều thuốc lợi tiểu Furosemid hoặc siết chặt lượng dịch vào.")

add_c("Để tránh tiêu hao năng lượng quá mức cho công hô hấp ở trẻ suy tim nhũ nhi, thời gian cho mỗi cữ bú bình hoặc bú mẹ tuyệt đối không nên kéo dài quá {{c1::30 phút}}.",
      "Dinh dưỡng: Nếu sau 20-30 phút trẻ chưa bú hết lượng sữa cần thiết, phần sữa còn lại nên được cho ăn qua ống thông dạ dày.")

cards_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-48: {len(cards)} cards!")
