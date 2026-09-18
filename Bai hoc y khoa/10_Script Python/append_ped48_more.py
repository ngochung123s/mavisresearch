# -*- coding: utf-8 -*-
"""Append 38 atomic cards to PED-48 to reach 135 cards total."""
import json
from pathlib import Path

p_rel = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.cards.v2.json")
p_mas = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_MASTER_v1.cards.v2.json")

cards = json.loads(p_rel.read_text(encoding="utf-8"))

def add_c(text, extra="", tags=None, source="PEDYTB"):
    tag_list = ["PED-48", source]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "cloze", "text": text, "extra": extra, "tags": tag_list})

# 1. Thuốc lợi tiểu & Dược lý chuyên sâu
add_c("[PED - Lâm sàng] Thuốc lợi tiểu Thiazide thường dùng duy trì ở trẻ em là {{c1::Hydrochlorothiazide}}, với liều lượng từ {{c1::1 đến 2 mg/kg/ngày}} uống chia làm 2 lần.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Tác động lên đoạn đầu ống lượn xa, hiệu quả vừa phải và luôn cần theo dõi bù Kali.",
      ["Loi-tieu-Thiazide"], "PED")

add_c("[PED - Lâm sàng] Trong điều trị kháng thuốc lợi tiểu ở trẻ suy tim nặng, thuốc lợi tiểu thiazide-like đường uống thường được phối hợp với Furosemid là {{c1::Metolazone}}, với liều dùng từ {{c1::0,2 đến 0,4 mg/kg/ngày}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Cơ chế:</b> Phong bế nephron tuần tự, ức chế tái hấp thu muối nước bù trừ tại ống lượn xa.",
      ["Khang-loi-tieu"], "PED")

add_c("[PED - Lâm sàng] Bên cạnh tác dụng lợi tiểu giữ Kali, Spironolacton còn có vai trò bảo vệ tim mạch lâu dài quan trọng là {{c1::chống xơ hóa cơ tim và ức chế tái cấu trúc thất trái}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Cơ chế:</b> Kháng tác động gây xơ hóa và chết tế bào của Aldosterone trên mô kẽ cơ tim.",
      ["Spironolacton"], "PED")

add_c("[PED - Lâm sàng] Thuốc ức chế men chuyển tác dụng kéo dài dùng cho trẻ lớn có thể uống 1 đến 2 lần mỗi ngày là {{c1::Enalapril}}, với liều duy trì từ {{c1::0,1 đến 0,5 mg/kg/ngày}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Được chuyển hóa tại gan thành Enalaprilat có hoạt tính, tiện lợi trong điều trị ngoại trú dài hạn.",
      ["Enalapril"], "PED")

add_c("[PED - Lâm sàng] Mục tiêu liều đích duy trì của thuốc chẹn beta Carvedilol trong điều trị suy tim mạn tính ở trẻ em là {{c1::0,2 đến 0,4 mg/kg/ngày}} (chia làm 2 lần uống).",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Thực hành:</b> Bắt đầu từ liều thăm dò 0,05 mg/kg/liều và tăng gấp đôi liều mỗi 2 tuần nếu dung nạp tốt.",
      ["Carvedilol"], "PED")

add_c("[PED - Lâm sàng] Cơ chế phân tử của Milrinone là ức chế enzyme Phosphodiesterase-3 (PDE-3), dẫn đến làm tăng nồng độ chất truyền tin thứ hai {{c1::cAMP (cyclic AMP)}} bên trong tế bào cơ tim và cơ trơn mạch máu.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> cAMP tăng làm tăng dòng canxi vào cơ tim (tăng co bóp) và giãn cơ trơn thành mạch (giảm tiền gánh và hậu gánh).",
      ["Milrinone"], "PED")

add_c("[PED - Lâm sàng] Thuốc tăng co bóp cơ tim Dobutamin tác động kích thích chủ yếu và chọn lọc lên thụ thể {{c1::beta-1 adrenergic}} trên màng tế bào cơ tim.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Kích thích thụ thể này làm tăng nồng độ canxi nội bào qua trung gian protein Gs, tăng sức co bóp mà ít gây co mạch ngoại biên.",
      ["Dobutamin"], "PED")

add_c("[PED - Lâm sàng] Thuốc vận mạch Dopamin ở dải liều thấp (1 đến 3 µg/kg/phút) kích thích chọn lọc lên thụ thể {{c1::Dopaminergic tại giường mạch thận và tạng}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Liều này làm giãn mạch thận, nhưng hiện nay không còn được khuyến cáo dùng đơn độc chỉ để bảo vệ thận.",
      ["Dopamin"], "PED")

add_c("[PED - Lâm sàng] Thuốc vận mạch co mạch đầu tay được lựa chọn khi suy tim cấp có tụt huyết áp nặng trơ với Dopamin và Dobutamin là {{c1::Norepinephrine (Noradrenalin)}} với liều truyền từ {{c1::0,05 đến 0,1 µg/kg/phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Kích thích mạnh thụ thể alpha-1 gây co mạch nâng huyết áp trung bình, kèm kích thích nhẹ beta-1 hỗ trợ co bóp cơ tim.",
      ["Norepinephrine"], "PED")

add_c("[PED - Lâm sàng] Khi truyền Nitroprusside kéo dài trên 48 đến 72 giờ hoặc ở bệnh nhân có suy giảm chức năng thận, cần cảnh giác nguy cơ ngộ độc chuyển hóa do tích lũy {{c1::Cyanide và Thiocyanate}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Cảnh báo:</b> Biểu hiện ngộ độc gồm toan lactic tiến triển, lú lẫn, co giật và tụt huyết áp trơ.",
      ["Nitroprusside"], "PED")

# 2. Ngộ độc Digoxin & Điện sinh lý
add_c("[PED - Lâm sàng] Triệu chứng ngộ độc Digoxin trên thị giác ở trẻ lớn có hiện tượng nhìn thấy quầng màu vàng hoặc màu xanh lá cây quanh nguồn sáng, thuật ngữ y khoa gọi là {{c1::Xanthopsia}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Cơ chế:</b> Độc tính ức chế bơm ion Na+/K+-ATPase trên tế bào nón của võng mạc mắt.",
      ["Xanthopsia"], "PED")

add_c("[PED - Lâm sàng] Rối loạn nhịp tim được coi là đặc trưng nhất và gợi ý cao nhất cho ngộ độc Digitalis trên điện tâm đồ là {{c1::nhịp nhanh nhĩ kèm block nhĩ thất (PAT with block)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Điện tim:</b> Vừa tăng tính tự động của ổ ngoại vị nhĩ vừa ức chế dẫn truyền qua nút nhĩ thất.",
      ["PAT-block"], "PED")

add_c("[PED - Lâm sàng] Kháng thể DigiFab trung hòa độc tính của Digoxin bằng cách gắn kết với phân tử Digoxin tự do với ái lực cao hơn thụ thể Na+/K+-ATPase của cơ tim tới {{c1::1000 lần}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Tạo phức hợp kháng nguyên - kháng thể trơ không độc và được đào thải nhanh chóng qua nước tiểu.",
      ["DigiFab"], "PED")

# 3. Hồi sức & Thở máy áp lực dương
add_c("[PED - Lâm sàng] Thở áp lực dương liên tục (CPAP) trong suy tim cấp có ứ huyết phổi giúp cải thiện chức năng thất trái nhờ cơ chế {{c1::làm tăng áp lực trong lồng ngực, từ đó làm giảm áp lực xuyên thành thất trái (giảm hậu gánh thất trái)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7).<br><b>🔍 Cơ chế:</b> Đồng thời đẩy dịch phế nang ngược trở lại mô kẽ và tuần hoàn bạch huyết.",
      ["CPAP-suy-tim"], "PED")

# 4. Thang điểm Ross chi tiết
add_c("[PED - Lâm sàng] Trong thang điểm Ross cải tiến, tiêu chí tần số tim lúc nghỉ ngơi được tính 2 điểm khi tần số tim tăng cao hơn bình thường theo tuổi trên {{c1::> 20 nhịp/phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Phân tầng:</b> Tăng 10-20 nhịp/phút tính 1 điểm; bình thường theo tuổi tính 0 điểm.",
      ["Ross-HR"], "PED")

add_c("[PED - Lâm sàng] Trong thang điểm Ross cải tiến, tiêu chí tần số thở lúc nghỉ ngơi được tính 2 điểm khi tần số thở tăng cao hơn giới hạn bình thường theo tuổi trên {{c1::> 20 nhịp/phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Phân tầng:</b> Thở nhanh > 20 nhịp so với ngưỡng sinh lý là dấu hiệu suy tim tiến triển.",
      ["Ross-RR"], "PED")

add_c("[PED - Lâm sàng] Trong thang điểm Ross cải tiến, tiêu chí kích thước gan to dưới bờ sườn phải được tính 2 điểm khi bờ dưới gan vượt quá {{c1::> 3 cm}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Phân tầng:</b> Gan < 2 cm tính 0 điểm; gan 2-3 cm tính 1 điểm.",
      ["Ross-gan"], "PED")

# 5. Cận lâm sàng & Chẩn đoán hình ảnh
add_c("[PED - Lâm sàng] Đường Kerley B trên X-quang ngực thẳng là các đường mờ mảnh dài 1 đến 2 cm nằm ngang sát màng phổi ở góc sườn hoành, hình thành do {{c1::sự tích tụ dịch phù nề trong các vách liên tiểu thùy phổi}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.1).<br><b>🔍 Hình ảnh:</b> Là dấu hiệu kinh điển của tình trạng ứ dịch mô kẽ mạn tính do tăng áp lực nhĩ trái.",
      ["Kerley-B"], "PED")

add_c("[PED - Lâm sàng] Tiêu chuẩn điện tâm đồ dày tâm thất phải ở trẻ nhũ nhi bao gồm: Trục điện tim chuyển sang {{c1::phải (Right Axis Deviation)}}; Sóng R ưu thế ở {{c1::chuyển đạo V1}}; và sóng T {{c1::dương ở V1 sau ngày tuổi thứ 7}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.2).<br><b>🔍 Điện tim:</b> Bình thường sóng T ở V1 phải âm từ ngày thứ 7 sau sinh đến tuổi thiếu niên.",
      ["ECG-RVH"], "PED")

add_c("[PED - Lâm sàng] Tiêu chuẩn điện tâm đồ dày tâm thất trái ở trẻ em được xác định khi chỉ số Sokolow-Lyon (biên độ sóng S ở V1 cộng biên độ sóng R ở V5 hoặc V6) vượt quá {{c1::bách phân vị thứ 98 theo lứa tuổi}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.2).<br><b>🔍 Điện tim:</b> Kèm theo dấu hiệu quá tải tâm thu thất trái (ST chênh xuống và T âm ở V5, V6).",
      ["ECG-LVH"], "PED")

add_c("[PED - Lâm sàng] Trên siêu âm tim Doppler, vận tốc tối đa của dòng hở van ba lá (V_TR) cho phép ước tính áp lực động mạch phổi tâm thu (PASP) thông qua phương trình Bernoulli cải tiến: PASP = {{c1::4 × (V_TR)^2 + RAP}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.3).<br><b>🔍 Sinh lý:</b> RAP là áp lực ước tính của tâm nhĩ phải (thường lấy mốc 5 đến 10 mmHg).",
      ["Bernoulli-PASP"], "PED")

# 6. Ca lâm sàng thực chiến
add_c("[PED - Lâm sàng] Trong Case 1 viêm cơ tim cấp gây sốc tim ở trẻ 8 tháng, phân suất tống máu LVEF giảm nặng xuống 28%, thuốc tăng co bóp inotrope đường truyền TM phối hợp đầu tay là {{c1::Dobutamin kết hợp Milrinone}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 1).<br><b>🔍 Xử trí:</b> Tuyệt đối không dùng Digoxin trong giai đoạn viêm cơ tim cấp mất bù vì cơ tim rất nhạy cảm dễ rung thất.",
      ["Case-1-Myocarditis"], "PED")

add_c("[PED - Lâm sàng] Trong Case 1 viêm cơ tim cấp, liệu pháp miễn dịch đặc hiệu liều cao giúp trung hòa kháng thể và giảm viêm cơ tim là truyền {{c1::IVIG (Immunoglobulin liều 2 g/kg trong 24 giờ)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 1).<br><b>🔍 Miễn dịch:</b> Can thiệp then chốt cải thiện tỷ lệ sống còn trong viêm cơ tim cấp do virus.",
      ["Case-1-IVIG"], "PED")

add_c("[PED - Lâm sàng] Trong Case 2 thông liên thất lớn gây suy tim độ 3 ở trẻ 2 tháng tuổi, thuốc ức chế men chuyển {{c1::Captopril}} được phối hợp với lợi tiểu nhằm mục đích {{c1::giảm hậu gánh đại tuần hoàn, từ đó làm giảm luồng shunt Trái - Phải qua lỗ thông}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 2).<br><b>🔍 Huyết động:</b> Giảm áp lực thất trái giúp giảm lượng máu tràn lên phổi.",
      ["Case-2-VSD"], "PED")

add_c("[PED - Lâm sàng] Trong Case 2 thông liên thất lớn có suy tim và suy dinh dưỡng nặng, chỉ định ngoại khoa vàng là {{c1::phẫu thuật tim hở vá lỗ thông liên thất lúc trẻ 2 đến 3 tháng tuổi}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 2).<br><b>🔍 Ngoại khoa:</b> Ngăn ngừa biến chứng tăng áp lực mạch máu phổi cố định không hồi phục (Eisenmenger).",
      ["Case-2-Phau-thuat"], "PED")

# 7. Cạm bẫy & Tips thực hành
add_c("[PED - Lâm sàng] Cạm bẫy lâm sàng: Khi thấy trẻ suy tim thở nhanh và nhịp tim nhanh, sai lầm chết người là truyền dịch nhanh (bolus) vì sẽ gây {{c1::quá tải thể tích tức thì và bùng phát phù phổi cấp ngừng thở}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 2).<br><b>🔍 Cảnh báo:</b> Chỉ truyền dịch bolus khi có bằng chứng chắc chắn của sốc giảm thể tích mất nước nặng.",
      ["Cam-bay-truyen-dich"], "PED")

add_c("[PED - Lâm sàng] Cạm bẫy lâm sàng: Sốc điện khử rung khi bệnh nhân ngộ độc Digoxin xuất hiện loạn nhịp tim có thể kích hoạt {{c1::rung thất trơ không thể hồi phục}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 7).<br><b>🔍 Cấp cứu:</b> Ưu tiên dùng Phenytoin, Lidocain và kháng thể đặc hiệu DigiFab.",
      ["Cam-bay-soc-dien"], "PED")

add_c("[PED - Lâm sàng] Cạm bẫy lâm sàng: Ngừng đột ngột thuốc chẹn beta giao cảm Carvedilol đang dùng duy trì sẽ gây {{c1::hiện tượng dội ngược (Rebound) nhịp nhanh kịch phát và bùng phát suy tim cấp}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 9).<br><b>🔍 Dược lý:</b> Do số lượng thụ thể beta đã bị điều hòa tăng (Upregulation) trong thời gian dùng thuốc.",
      ["Cam-bay-chen-beta"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Điều dưỡng hoặc bác sĩ nên dùng bút dạ y tế gạch một đường nhỏ đánh dấu {{c1::bờ dưới gan trên da bụng trẻ vào buổi sáng}} để theo dõi đáp ứng với Furosemid trực quan.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 2).<br><b>🔍 Thực hành:</b> Sự co nhỏ của bờ gan là bằng chứng khách quan của giảm ứ huyết đại tuần hoàn.",
      ["Tip-danh-dau-gan"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Đục lỗ núm vú bình sữa rộng hơn một chút cho trẻ suy tim bú nhằm mục đích {{c1::sữa chảy dễ dàng khi mút nhẹ, giúp tiết kiệm công thở và năng lượng}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 7).<br><b>🔍 Dinh dưỡng:</b> Giúp trẻ bú đủ no trước khi bị kiệt sức.",
      ["Tip-num-vu"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Hạn chế tối đa làm các thủ thuật gây đau đớn dồn dập cho trẻ suy tim vì {{c1::cơn khóc thét kích thích giao cảm làm tăng vọt huyết áp và tần số tim, đẩy buồng tim vào phù phổi cấp}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 12).<br><b>🔍 Chăm sóc:</b> Giữ trẻ yên tĩnh và có mẹ vỗ về bên cạnh.",
      ["Tip-tranh-kich-thich"], "PED")

# 8. Checkpoint tư duy
add_c("[PED - Lâm sàng] Checkpoint: Ở trẻ mắc thông liên thất lớn, triệu chứng suy tim sung huyết thường không xuất hiện ngay sau sinh mà bùng phát lúc 6-8 tuần tuổi vì {{c1::sức cản mạch máu phổi (PVR) sinh lý giảm dần và chạm đáy lúc 6-8 tuần tuổi, làm luồng shunt Trái - Phải đạt mức cực đại}}.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 1).<br><b>🔍 Cơ chế:</b> Chênh áp giữa hai tâm thất trở nên cực đại khi PVR giảm sâu.",
      ["Checkpoint-VSD-PVR"], "PED")

add_c("[PED - Lâm sàng] Checkpoint: Tiếng rung tâm trương ngắn nghe được ở mỏm tim trong thông liên thất lớn phản ánh tình trạng {{c1::rung tâm trương cơ năng do tăng lưu lượng máu lớn qua van hai lá (Qp/Qs ≥ 2:1)}} chứ không phải hẹp van hai lá thực thể.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 4).<br><b>🔍 Thính chẩn:</b> Là bằng chứng gián tiếp khẳng định luồng shunt Trái - Phải có lưu lượng rất lớn.",
      ["Checkpoint-rung-tam-truong"], "PED")

add_c("[PED - Lâm sàng] Tiêu chuẩn xuất viện an toàn của trẻ suy tim: Trẻ tự ăn bú tốt, hết khó thở, phổi sạch ran, gan thu nhỏ {{c1::< 2 cm dưới bờ sườn}}, và phác đồ thuốc chuyển sang đường uống ổn định tối thiểu {{c1::48 giờ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 14.2).<br><b>🔍 Xuất viện:</b> Gia đình biết cách cho uống thuốc chuẩn bằng bơm tiêm chia vạch.",
      ["Tieu-chuan-xuat-vien"], "PED")

# Write to both files
p_rel.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
p_mas.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-48: {len(cards)} cards successfully generated!")
