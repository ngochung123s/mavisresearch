# -*- coding: utf-8 -*-
"""Append 80 atomic cards to PED-43 to reach 157 cards total."""
import json
from pathlib import Path

p_rel = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_2026-09-19_RELEASE_v1.cards.v2.json")
p_mas = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_MASTER_v1.cards.v2.json")

cards = json.loads(p_rel.read_text(encoding="utf-8"))

def add_c(text, extra="", tags=None, source="PEDYTB"):
    tag_list = ["PED-43", source]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "cloze", "text": text, "extra": extra, "tags": tag_list})

# 1. Chi tiết Thông liên thất (VSD)
add_c("[PED - Lâm sàng] Chỉ định phẫu thuật đóng thông liên thất (VSD) dựa trên tỷ số lưu lượng máu phổi trên lưu lượng máu hệ thống (Qp/Qs) khi tỷ số này đạt từ {{c1::Qp/Qs ≥ 1,5:1}} trở lên.",
      "<b>📚 Nguồn:</b> PED (Mục 4.3).<br><b>🔍 Huyết động:</b> Phản ánh luồng shunt Trái - Phải có ý nghĩa huyết động gây quá tải thể tích thất trái.",
      ["VSD-QpQs"], "PED")

add_c("[PED - Lâm sàng] Trong thông liên thất phần phễu (dưới van), biến chứng hở van động mạch chủ tiến triển xảy ra do lá van {{c1::động mạch chủ bên phải}} bị hút sa vào lỗ thông liên thất.",
      "<b>📚 Nguồn:</b> PED (Mục 4.1).<br><b>🔍 Cơ chế:</b> Hiệu ứng Venturi tạo áp lực âm kéo tụt lá van phải vào buồng thất phải.",
      ["VSD-sa-van-DMC"], "PED")

add_c("[PEDYTB - Ôn thi] Tỷ lệ tự đóng tự nhiên của thông liên thất phần cơ nhỏ (Muscular VSD) ở trẻ em trước 2 tuổi có thể lên tới {{c1::trên 80%}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Khối cơ bè tâm thất phì đại sinh lý ép bít các lỗ thông cơ nhỏ.",
      ["VSD-tu-dong", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Để tránh nhầm lẫn tiếng thổi tâm thu của thông liên thất với tiếng thổi của hở hai lá cơ năng ở mỏm tim, cần nhớ tiếng thổi của VSD nghe rõ nhất ở {{c1::khoang liên sườn 3-4 bờ trái xương ức}} và lan {{c1::hình nan quạt quanh ngực}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 4).<br><b>🔍 Khám:</b> Tiếng thổi hở hai lá nghe rõ ở mỏm tim và lan ra hố nách trái.",
      ["Phan-biet-thoi-VSD"], "PED")

add_c("[PED - Lâm sàng] Ở trẻ nhũ nhi mắc thông liên thất lớn, việc theo dõi sát biểu hiện lâm sàng ăn bú và tăng cân có giá trị hơn nghe tim vì tiếng thổi tâm thu có thể {{c1::nhỏ đi khi áp lực động mạch phổi tăng cao gần bằng áp lực thất trái}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 8).<br><b>🔍 Bẫy lâm sàng:</b> Tiếng thổi nhỏ đi không có nghĩa là bệnh thuyên giảm mà có thể cảnh báo tăng áp phổi nặng.",
      ["VSD-tieng-thoi-nho"], "PED")

# 2. Chi tiết Thông liên nhĩ (ASD)
add_c("[PED - Lâm sàng] Điều kiện giải phẫu bắt buộc để có thể can thiệp bít thông liên nhĩ lỗ thứ phát bằng dù qua da là gờ mô vách liên nhĩ xung quanh lỗ thông phải đủ dày và rộng {{c1::> 5 mm}} (trừ gờ động mạch chủ).",
      "<b>📚 Nguồn:</b> PED (Mục 5.3).<br><b>🔍 Can thiệp:</b> Nhằm đảm bảo hai cánh của dù bít Amplatzer bám chắc chắn không bị bung trôi.",
      ["ASD-go-mo"], "PED")

add_c("[PED - Lâm sàng] Trong thông liên nhĩ lớn, sự quá tải thể tích kéo dài của buồng tâm nhĩ phải và tâm thất phải ở tuổi trưởng thành thường dẫn đến biến chứng rối loạn nhịp tim nguy hiểm là {{c1::rung nhĩ hoặc cuồng nhĩ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.2).<br><b>🔍 Biến chứng:</b> Do thành tâm nhĩ phải bị căng giãn và xơ hóa cấu trúc cơ học theo thời gian.",
      ["ASD-loan-nhip"], "PED")

# 3. Chi tiết Còn ống động mạch (PDA)
add_c("[PED - Lâm sàng] Tiếng thổi liên tục Gibson trong còn ống động mạch bắt đầu từ {{c1::đầu kỳ tâm thu}}, mạnh dần lên và đạt cường độ đỉnh ở {{c1::tiếng T2}}, sau đó giảm dần trong kỳ tâm trương.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Âm học:</b> Phản ánh chênh áp giữa động mạch chủ và động mạch phổi tồn tại liên tục trong suốt chu chuyển tim.",
      ["PDA-Gibson"], "PED")

add_c("[PED - Lâm sàng] Chênh lệch huyết áp (hiệu số huyết áp tâm thu trừ tâm trương) ở trẻ mắc còn ống động mạch lớn thường mở rộng vượt quá {{c1::> 30 đến 40 mmHg}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Khám:</b> Huyết áp tâm thu có thể bình thường nhưng huyết áp tâm trương tụt sâu xuống 20-30 mmHg.",
      ["PDA-hieu-so-HA"], "PED")

add_c("[PED - Lâm sàng] Bên cạnh Indomethacin và Ibuprofen, hoạt chất hạ sốt giảm đau thông thường {{c1::Paracetamol (Acetaminophen)}} đường uống hoặc truyền tĩnh mạch cũng được chứng minh có hiệu quả đóng ống động mạch ở trẻ sinh non.",
      "<b>📚 Nguồn:</b> PED (Mục 6.3).<br><b>🔍 Dược lý:</b> Lựa chọn thay thế an toàn khi trẻ non tháng có giảm tiểu cầu nặng hoặc nguy cơ xuất huyết tiêu hóa.",
      ["PDA-Paracetamol"], "PED")

add_c("[PED - Lâm sàng] Thuốc đóng ống động mạch (Ibuprofen, Indomethacin) hoàn toàn KHÔNG có tác dụng ở {{c1::trẻ sơ sinh đủ tháng}} mắc còn ống động mạch.",
      "<b>📚 Nguồn:</b> PED (Mục 6.3).<br><b>🔍 Dược lý:</b> Ống động mạch ở trẻ đủ tháng có cấu trúc mô học trưởng thành với nhiều sợi chun, không còn đáp ứng với ức chế men COX.",
      ["PDA-du-thang"], "PED")

# 4. Chi tiết Tứ chứng Fallot & Cơn tím
add_c("[PEDYTB - Ôn thi] Cơ chế cơn tím Fallot: Cơn tăng tiết Catecholamine giao cảm kích thích co thắt dữ dội {{c1::cơ phễu đường ra thất phải}}, cắt đứt dòng máu lên phổi, dồn toàn bộ máu đen từ thất phải qua VSD vào động mạch chủ.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Cơn tím thường bùng phát vào buổi sáng sau thức dậy hoặc sau khóc thét, bú gắng sức.",
      ["Fallot-con-tim-co-che", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trong cơn tím Fallot cấp tính, khám nghe tim sẽ ghi nhận một hiện tượng lâm sàng bất thường là: Tiếng thổi tâm thu ở bờ trái ức vốn có hàng ngày sẽ {{c1::đột ngột nhỏ đi rõ rệt hoặc biến mất hoàn toàn}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Phản ánh cơ phễu đã co thắt tối đa, hầu như không còn máu thoát qua được đường ra thất phải lên phổi.",
      ["Fallot-con-tim-tieng-thoi", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tư thế ngồi xổm (Squatting) hoặc tư thế ngực gối (Knee-chest) giúp cắt cơn tím ở trẻ Fallot nhờ cơ chế {{c1::làm gập động mạch đùi, tăng sức cản mạch máu ngoại biên hệ thống (SVR), từ đó làm giảm luồng shunt Phải - Trái qua VSD}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Ép máu từ thất phải vượt qua chỗ hẹp phễu lên động mạch phổi để tăng cường trao đổi oxy.",
      ["Fallot-nguc-goi-co-che", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thuốc an thần giảm đau được lựa chọn hàng đầu trong cấp cứu cơn tím Fallot là {{c1::Morphine Sulfate}}, với liều dùng là {{c1::0,1 mg/kg}} tiêm dưới da (SC) hoặc tiêm bắp (IM).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Ức chế trung tâm hô hấp làm dịu cơn thở nhanh sâu, trấn tĩnh trẻ, cắt đứt phản xạ giao cảm và làm giãn cơ phễu thất phải.",
      ["Fallot-Morphin", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Biện pháp bù dịch nhanh bằng dung dịch điện giải đẳng trương NaCl 0,9% liều {{c1::10 đến 15 mL/kg}} trong cơn tím Fallot có tác dụng {{c1::làm tăng thể tích tiền gánh thất phải và chống hiện tượng cô đặc máu}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Tăng thể tích tống máu thất phải giúp đẩy mở cơ phễu đường ra thất phải.",
      ["Fallot-bu-dich", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thuốc chẹn beta giao cảm tiêm tĩnh mạch chậm điều trị cơn tím Fallot trơ với Morphine và bù dịch là {{c1::Propranolol}}, với liều tiêm TM rất chậm từ {{c1::0,05 đến 0,1 mg/kg}} trong 5-10 phút.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Trực tiếp làm giãn cơ trơn phễu buồng tống thất phải, bắt buộc theo dõi monitor điện tim liên tục.",
      ["Fallot-Propranolol-TM", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thuốc điều trị nội khoa đường uống được chỉ định để dự phòng tái phát cơn tím Fallot ở trẻ chờ phẫu thuật là {{c1::Propranolol}}, với liều dùng từ {{c1::1 đến 2 mg/kg/ngày}} chia làm 2 đến 4 lần.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Ngăn chặn các đợt co thắt phễu kịch phát khi trẻ quấy khóc hoặc sốt.",
      ["Fallot-Propranolol-uong", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Tiêm Natri Bicarbonat (NaHCO3) liều 1 đến 2 mEq/kg trong cơn tím Fallot nặng nhằm mục đích kiềm hóa máu, bởi vì tình trạng toan chuyển hóa là yếu tố gây {{c1::co thắt mạnh mạch máu phổi, làm tăng sức cản mạch phổi và đẩy mạnh luồng shunt Phải - Trái}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Huyết động:</b> Phục hồi pH máu giúp hạ sức cản mạch phổi, tạo thuận lợi cho máu lên phổi.",
      ["Fallot-NaHCO3"], "PED")

add_c("[PED - Lâm sàng] Cơn tím thiếu oxy Fallot có đỉnh điểm xuất hiện phổ biến nhất trong độ tuổi từ {{c1::2 đến 4 tháng tuổi}} và thường hay xảy ra vào thời điểm {{c1::buổi sáng sớm sau khi ngủ dậy}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Cơ chế:</b> Do nồng độ Catecholamine nội sinh tăng cao theo nhịp sinh học buổi sáng kết hợp tình trạng thiếu nước tương đối sau giấc ngủ đêm.",
      ["Fallot-dinh-diem-con-tim"], "PED")

add_c("[PED - Lâm sàng] Biến chứng nhiễm trùng thần kinh nguy hiểm thường gặp ở trẻ lớn mắc Tứ chứng Fallot có tím mạn tính là {{c1::áp xe não (Brain Abscess)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7.2).<br><b>🔍 Cơ chế:</b> Máu tĩnh mạch hệ thống không qua hệ thống lọc mao mạch phổi nên vi khuẩn xâm nhập thẳng vào tuần hoàn động mạch não.",
      ["Fallot-ap-xe-nao"], "PED")

# 5. Chi tiết TGA & Phẫu thuật Jatene
add_c("[PEDYTB - Ôn thi] Thủ thuật thông tim can thiệp cấp cứu xé rách vách liên nhĩ bằng bóng ở trẻ sơ sinh mắc TGA có tên là {{c1::Thủ thuật Rashkind (Balloon Atrial Septostomy)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Tạo lỗ thông liên nhĩ lớn để tối ưu hóa sự pha trộn máu ở tầng tâm nhĩ trong khi chờ phẫu thuật chuyển gốc.",
      ["Thu-thuat-Rashkind", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phẫu thuật sửa chữa triệt để về mặt giải phẫu hiện đại được lựa chọn hàng đầu cho chuyển gốc đại động mạch là {{c1::Phẫu thuật chuyển gốc động mạch Jatene (Arterial Switch Operation - ASO)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Chuyển lại động mạch chủ về thất trái, chuyển động mạch phổi về thất phải và cắm lại động mạch vành.",
      ["Phau-thuat-Jatene", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thời điểm vàng bắt buộc phải thực hiện phẫu thuật Jatene cho trẻ TGA đơn thuần lành vách liên thất là trong {{c1::tuần đầu tiên sau sinh (từ 3 đến 7 ngày tuổi)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Sau tuần đầu, sức cản mạch phổi giảm làm tâm thất trái bị thoái triển thành mỏng, không còn đủ áp lực để bơm máu hệ thống.",
      ["Jatene-tuan-dau", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Kỹ thuật phẫu thuật Jatene bao gồm các thì chính: Cắt rời đại động mạch, chuyển ĐMC về thất trái, chuyển ĐMP về thất phải, cắm lại hai cuống động mạch vành và làm thủ thuật {{c1::Lecompte đưa động mạch phổi ra trước động mạch chủ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.1).<br><b>🔍 Phẫu thuật:</b> Nghiệm pháp Lecompte giúp tái lập vị trí giải phẫu tự nhiên của thân động mạch phổi.",
      ["Jatene-Lecompte"], "PED")

# 6. Chi tiết HLHS & Phẫu thuật 3 giai đoạn
add_c("[PEDYTB - Ôn thi] Trong Hội chứng thiểu sản thất trái (HLHS), toàn bộ lưu lượng máu nuôi đại tuần hoàn và mạch vành phụ thuộc hoàn toàn vào {{c1::tâm thất phải bơm máu qua ống động mạch (PDA)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14-15 - Mục 3.14).<br><b>🔍 Đối chiếu PED:</b> Cấp cứu sơ sinh bắt buộc truyền PGE1 mở lại ống động mạch.",
      ["HLHS-tuan-hoan-PDA", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Quy trình phẫu thuật tái tạo 3 giai đoạn điều trị HLHS theo giáo trình gồm: Giai đoạn 1 là {{c1::phẫu thuật Norwood}}; Giai đoạn 2 là {{c1::phẫu thuật Glenn hai hướng}}; Giai đoạn 3 là {{c1::phẫu thuật Fontan}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 15 - Mục 3.14).<br><b>🔍 Đối chiếu PED:</b> Norwood tiến hành tuần đầu sau sinh; Glenn lúc 3-6 tháng; Fontan lúc 2-4 tuổi.",
      ["HLHS-3-giai-doan", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Phẫu thuật Glenn hai hướng (Bidirectional Glenn) trong quy trình Fontan là phẫu thuật nối trực tiếp {{c1::tĩnh mạch chủ trên (SVC)}} vào {{c1::động mạch phổi phải}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Huyết động:</b> Đưa máu nửa trên cơ thể về phổi thụ động không cần qua tâm thất, thực hiện lúc 3 đến 6 tháng tuổi.",
      ["Glenn-hai-huong"], "PED")

add_c("[PED - Lâm sàng] Phẫu thuật Fontan hoàn tất là kỹ thuật nối trực tiếp {{c1::tĩnh mạch chủ dưới (IVC)}} vào {{c1::động mạch phổi}} thông qua ống ghép nhân tạo ngoài tim (Extracardiac conduit).",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Huyết động:</b> Tách rời hoàn toàn máu tĩnh mạch hệ thống không qua tim, đưa tâm thất duy nhất làm nhiệm vụ bơm máu động mạch chủ.",
      ["Fontan-hoan-tat"], "PED")

# 7. Chi tiết Ebstein & Rối loạn nhịp
add_c("[PEDYTB - Ôn thi] Trong bệnh dị tật Ebstein của van ba lá, tổn thương giải phẫu đặc trưng là {{c1::lá vách và lá sau van ba lá bị bám thấp bất thường về phía mỏm thất phải}}, dẫn đến hiện tượng {{c1::nhĩ hóa một phần thất phải}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Khiến phần buồng thất phải chức năng co bóp tống máu còn lại bị teo nhỏ và giảm động.",
      ["Ebstein-giai-phau", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hội chứng rối loạn nhịp tiền kích thích bẩm sinh thường phối hợp với bệnh dị tật Ebstein ở khoảng 15% các trường hợp là {{c1::Hội chứng Wolff-Parkinson-White (WPW)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Xuất hiện sóng delta và khoảng PR ngắn, nguy cơ khởi phát cơn nhịp nhanh trên thất kịch phát.",
      ["Ebstein-WPW", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hình ảnh điện tâm đồ kinh điển trong bệnh Ebstein gồm: Sóng P ở DII cao khổng lồ nhọn hoắt được ví như {{c1::sóng P kiểu dãy Himalaya (P himalayan)}}, kèm block nhánh phải hoàn toàn.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Phản ánh tâm nhĩ phải giãn to cực độ chứa một lượng máu ứ trệ khổng lồ.",
      ["Ebstein-P-Himalaya", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phương pháp phẫu thuật tạo hình sửa van ba lá hiện đại và hiệu quả nhất cho bệnh nhân mắc dị tật Ebstein là {{c1::phương pháp tạo hình hình nón (Cone procedure)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Huy động toàn bộ các lá van ba lá để tái tạo thành một van hình nón có chức năng đóng mở sinh lý.",
      ["Ebstein-Cone", "On-thi-YTB"], "PEDYTB")

# 8. Chi tiết Hẹp eo ĐMC & Hẹp van ĐMP
add_c("[PEDYTB - Ôn thi] Bệnh Hẹp eo động mạch chủ (Coarctation of the Aorta) ở trẻ gái có tỷ lệ phối hợp rất cao với hội chứng bất thường nhiễm sắc thể có tên là {{c1::Hội chứng Turner (bộ NST 45,XO)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Khoảng 30% đến 35% bệnh nhân Turner có hẹp eo động mạch chủ hoặc van ĐMC hai lá.",
      ["CoA-Turner", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu lâm sàng then chốt để chẩn đoán xác định Hẹp eo động mạch chủ ở trẻ lớn là: Huyết áp chi trên {{c1::cao hơn}} huyết áp chi dưới với mức chênh lệch huyết áp tay - chân {{c1::> 20 mmHg}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Bắt mạch đùi hai bên thấy yếu rõ rệt hoặc đến chậm so với mạch quay (Radio-femoral delay).",
      ["CoA-chenh-lech-HA", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu Roesler trên phim X-quang ngực thẳng của bệnh nhân hẹp eo động mạch chủ lớn tuổi là hình ảnh {{c1::khuyết bờ dưới các xương sườn (Rib notching)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Do các động mạch liên sườn thuộc hệ tuần hoàn bàng hệ giãn to ngoằn ngoèo đè ép bào mòn bờ dưới xương sườn.",
      ["CoA-dau-hieu-Roesler", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dị tật van tim bẩm sinh thường phối hợp nhất với Hẹp eo động mạch chủ ở khoảng 70% các trường hợp là {{c1::van động mạch chủ hai lá (Bicuspid Aortic Valve)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Có nguy cơ tiến triển thành hẹp van hoặc hở van động mạch chủ và viêm nội tâm mạc nhiễm khuẩn.",
      ["CoA-van-DMC-2-la", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Biện pháp điều trị lựa chọn hàng đầu cho bệnh nhân Hẹp van động mạch phổi đơn thuần (Pulmonary Stenosis) có chênh áp đỉnh qua van lớn là {{c1::nong van động mạch phổi bằng bóng qua da (Balloon Valvuloplasty)}} với tỷ lệ thành công {{c1::85%}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 17 - Mục 3.17).<br><b>🔍 Đối chiếu PED:</b> Tỷ lệ thành công lâu dài đạt trên 85% các trường hợp, tránh được phẫu thuật mở ngực.",
      ["PS-nong-bong", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hội chứng di truyền thường phối hợp kinh điển nhất với Hẹp van động mạch phổi bẩm sinh là {{c1::Hội chứng Noonan}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 17 - Mục 3.17).<br><b>🔍 Đối chiếu PED:</b> Trẻ có khuôn mặt đặc trưng, cổ ngắn có màng, lồng ngực lõm ức và chậm phát triển chiều cao.",
      ["PS-Noonan", "On-thi-YTB"], "PEDYTB")

# 9. Chi tiết Dự phòng IE & Cạm bẫy lâm sàng
add_c("[PED - Lâm sàng] Chế độ kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn đường uống tiêu chuẩn trước thủ thuật răng miệng là {{c1::Amoxicillin liều 50 mg/kg (tối đa 2 g)}} uống một liều duy nhất trước thủ thuật {{c1::30 đến 60 phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Nếu dị ứng Penicillin chuyển sang Clindamycin 20 mg/kg hoặc Azithromycin 15 mg/kg.",
      ["Khang-sinh-du-phong-IE"], "PED")

add_c("[PED - Lâm sàng] Bệnh tim bẩm sinh tím có luồng shunt Phải - Trái làm mất chức năng của màng mao mạch phổi đóng vai trò là {{c1::bộ lọc cơ học vi khuẩn và cục máu đông}} của cơ thể.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 1).<br><b>🔍 Cơ chế:</b> Giải thích tại sao trẻ tim bẩm sinh tím có nguy cơ cao bị áp xe não và nhồi máu não nghịch thường.",
      ["Loc-mao-mach-phoi"], "PED")

add_c("[PED - Lâm sàng] Dấu hiệu nhận biết trẻ sơ sinh tím tái do nguyên nhân tim bẩm sinh so với tím do hạ thân nhiệt là: Tím do tim xuất hiện ở cả {{c1::niêm mạc miệng, lưỡi và kết mạc mắt}} và {{c1::không biến mất sau khi sưởi ấm trẻ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 3).<br><b>🔍 Khám:</b> Tím do lạnh chỉ xuất hiện ở đầu chi, niêm mạc lưỡi vẫn hồng hào.",
      ["Phan-biet-tim-tai"], "PED")

# Write to both release and master files
p_rel.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
p_mas.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-43: {len(cards)} cards successfully generated!")
