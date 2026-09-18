# -*- coding: utf-8 -*-
"""Generate harmonized, source-tagged Anki flashcards for PED-43 (Tim bẩm sinh thường gặp & Cơn tím Fallot).
Harmonizes PEDYTB (Giáo trình Bộ môn Nhi Thái Bình - Trang 8 - 17) & PED (Chuẩn hóa lâm sàng quốc tế).
"""
import json
from pathlib import Path

target_release = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_2026-09-19_RELEASE_v1.cards.v2.json")
target_master = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_MASTER_v1.cards.v2.json")

cards = []

def add_c(text, extra="", tags=None, source="PEDYTB"):
    tag_list = ["PED-43", source]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "cloze", "text": text, "extra": extra, "tags": tag_list})

def add_b(front, orig, ai, extra="", tags=None):
    back = f"<b>📖 Văn bản gốc [PEDYTB - Giáo trình Nhi Thái Bình]:</b><br>• {orig}<br><br><b>🔍 Góc nhìn bổ sung [PED - Chuẩn hóa Lâm sàng Quốc tế]:</b><br>• {ai}"
    tag_list = ["PED-43", "Basic-Card", "Dung-hoa-2-phien-ban"]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "basic", "front": front, "back": back, "extra": extra, "tags": tag_list})

# ==============================================================================
# KHỐI 1: ĐẠI CƯƠNG & PHÂN LOẠI TIM BẨM SINH (PEDYTB vs PED) (12 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Tỷ lệ mắc tim bẩm sinh lúc sinh ở trẻ sống theo giáo trình là khoảng {{c1::0,8% trẻ sống}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục I).<br><b>🔍 Đối chiếu PED:</b> Tương đương khoảng 8 đến 10 trẻ trên 1000 trẻ sinh sống. Meta-analysis toàn cầu của van der Linde xác định tỷ lệ là 9,1 trên 1000.",
      ["Dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thời điểm phát hiện tim bẩm sinh bằng siêu âm tiền sản theo giáo trình là vào {{c1::quý thứ hai của thời kỳ có thai}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục I).<br><b>🔍 Đối chiếu PED:</b> Siêu âm tim thai hình thái học tối ưu nhất ở tuần thai thứ 18 đến 22.",
      ["Sieu-am-tien-san", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phẫu thuật tim hở lần đầu tiên trên thế giới được tiến hành ở Đại học Minnesota vào năm {{c1::1950}} với máy tim phổi nhân tạo.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục I).<br><b>🔍 Đối chiếu PED:</b> Mốc lịch sử mở ra kỷ nguyên phẫu thuật sửa chữa triệt để tim bẩm sinh.",
      ["Lich-su-phau-thuat", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung của nhóm tim bẩm sinh shunt Trái - Phải là: {{c1::Máu đi từ bên trái sang bên phải}}, lượng máu lên phổi {{c1::tăng}} và thường {{c1::không có tím}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục II.1).<br><b>🔍 Đối chiếu PED:</b> Do áp lực và sức cản đại tuần hoàn sinh lý cao hơn tuần hoàn phổi.",
      ["Shunt-Trai-Phai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hiện tượng tím muộn trong nhóm tim bẩm sinh shunt Trái - Phải xảy ra khi tổn thương lớn không được phẫu thuật gây tắc nghẽn mạch phổi, được gọi là {{c1::Hội chứng Eisenmenger}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục II.1).<br><b>🔍 Đối chiếu PED:</b> Tăng áp lực mạch phổi cố định làm đảo ngược luồng shunt thành Phải - Trái, chống chỉ định mổ tim hở đóng lỗ thông.",
      ["Hoi-chung-Eisenmenger", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Danh mục các bệnh tim bẩm sinh shunt Trái - Phải trong giáo trình gồm 5 bệnh: {{c1::Thông liên thất (VSD), Thông liên nhĩ (ASD), Còn ống động mạch (PDA), Thông sàn nhĩ thất (AVSD) và Bất thường tĩnh mạch phổi bán phần (PAPVC)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục II.1).<br><b>🔍 Đối chiếu PED:</b> 5 bệnh lý shunt Trái - Phải kinh điển cần ghi nhớ khi thi.",
      ["Phan-loai-Shunt-TP", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung của nhóm tim bẩm sinh shunt Phải - Trái là: {{c1::Máu chưa được oxy hóa đi vào động mạch chủ}}, lượng máu tới phổi có thể {{c1::tăng hoặc giảm}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục II.2).<br><b>🔍 Đối chiếu PED:</b> Gây triệu chứng tím tái trung ương sớm ngay sau sinh.",
      ["Shunt-Phai-Trai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Danh mục 7 bệnh tim bẩm sinh shunt Phải - Trái (có tím) trong giáo trình gồm: {{c1::Tứ chứng Fallot, Teo van ĐMP kèm/không kèm VSD, Chuyển gốc ĐM (TGA), Thân chung ĐM, Bệnh Ebstein, TAPVC toàn phần và Thiểu sản thất trái (HLHS)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 8 - Mục II.2).<br><b>🔍 Đối chiếu PED:</b> Cần phân biệt nhóm giảm lưu lượng phổi (Fallot, Teo van ĐMP) và nhóm tăng lưu lượng phổi (TGA, Truncus).",
      ["Phan-loai-Shunt-PT", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Nhóm tổn thương tắc nghẽn tại van và không tại van trong giáo trình gồm: {{c1::Tắc nghẽn đường ra thất trái (LVOTO), Thiểu sản quai ĐMC / hẹp eo ĐMC, Hẹp van ĐMP và Hẹp van ĐMC}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục II.3).<br><b>🔍 Đối chiếu PED:</b> Nhóm bệnh gây tăng gánh áp lực đơn thuần không có luồng shunt ban đầu.",
      ["Ton-thuong-tac-nghen", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Nghiệm pháp thở oxy 100% (Hyperoxia test) có giá trị chẩn đoán: Nếu PaO2 sau 10 phút thở oxy vẫn dưới {{c1::< 100 đến 150 mmHg}} khẳng định nguyên nhân tím là do {{c1::tim bẩm sinh có luồng shunt Phải - Trái}}.",
      "<b>📚 Nguồn:</b> PED (Mục 3.2).<br><b>🔍 Phân biệt:</b> Nếu PaO2 tăng vọt > 200 mmHg chứng tỏ tím do bệnh lý suy hô hấp của nhu mô phổi.",
      ["Hyperoxia-test"], "PED")

# ==============================================================================
# KHỐI 2: THÔNG LIÊN THẤT (VSD - PEDYTB) (16 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Thông liên thất (VSD) là dị tật phổ biến nhất của tim bẩm sinh, chiếm tới {{c1::20%}} tất cả các trường hợp tim bẩm sinh (trừ van ĐMC hai lá và sa van hai lá).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Là dị tật bẩm sinh hay gặp nhất ở các phòng khám tim mạch nhi.",
      ["VSD-dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Giáo trình phân loại thông liên thất thành 4 vị trí giải phẫu: {{c1::Phần quanh màng (Perimembranous), Phần phễu / Dưới van (Infundibular), Phần buồng nhận (Inlet) và Phần cơ (Muscular)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> 4 vị trí giải phẫu chuẩn mực bắt buộc thuộc lòng.",
      ["VSD-vi-tri", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thông liên thất phần quanh màng có đặc tính tự nhiên là {{c1::có thể đóng tự nhiên do sự bọc lại của lá vách van ba lá}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Tạo thành cấu trúc túi phình vách ngăn bảo vệ trên siêu âm tim.",
      ["VSD-phan-mang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Cả thông liên thất phần màng và phần phễu đều rất gần với lá van động mạch chủ bên phải; do {{c1::hiệu ứng Venturi}} gây sa và hở van động mạch chủ, hạn chế dòng máu qua VSD.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Áp lực âm do dòng phụt xoáy tốc độ cao hút tụt lá van động mạch chủ.",
      ["Hieu-ung-Venturi", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thông liên thất phần buồng nhận có đặc điểm là {{c1::không đóng tự nhiên được}} và thường phối hợp với {{c1::thông sàn nhĩ thất hoặc hở van nhĩ thất}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> ĐTĐ thường biểu hiện trục trái đặc thù.",
      ["VSD-buong-nhan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thông liên thất phần cơ là dị tật hay gặp ở trẻ sơ sinh và {{c1::hầu hết sẽ đóng trước 2 tuổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Khối cơ bè tâm thất dày lên sinh lý ép bít các lỗ thông cơ nhỏ.",
      ["VSD-phan-co", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trẻ thông liên thất lỗ nhỏ có đặc điểm: {{c1::Không có triệu chứng lâm sàng}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Bệnh Roger, chỉ nghe thấy tiếng thổi tâm thu thô ráp 4/6 kèm rung miu.",
      ["VSD-lo-nho", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trẻ thông liên thất lỗ lớn có triệu chứng thở nhanh, nhịp tim nhanh, không lên cân xuất hiện ngay khi áp lực mạch máu phổi giảm xuống vào lúc trẻ {{c1::6 - 8 tuần tuổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Mốc 6-8 tuần tuổi là mốc kinh điển bùng phát suy tim trong VSD lớn.",
      ["VSD-lo-lon", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bệnh lý tắc nghẽn mạch máu phổi không xảy ra ở trẻ sơ sinh nhưng có thể phát triển khi trẻ được {{c1::2 tuổi}}; Hội chứng Eisenmenger xảy ra muộn gây shunt Phải - Trái và lúc đó {{c1::không còn chỉ định phẫu thuật}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Chống chỉ định phẫu thuật đóng lỗ thông khi đã có Eisenmenger.",
      ["VSD-Eisenmenger", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Nghe tim trong thông liên thất: Tiếng thổi tâm thu từ nhẹ đến vừa; trường hợp lưu lượng shunt Trái - Phải lớn có thể nghe thấy {{c1::tiếng thổi giữa tâm trương do tăng lưu lượng qua van hai lá}} (rung tâm trương cơ năng).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Là bằng chứng gián tiếp của luồng shunt lớn Qp/Qs ≥ 2:1.",
      ["VSD-nghe-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Mục tiêu điều trị thông liên thất là: {{c1::Đảm bảo sự phát triển bình thường của cơ thể}} và {{c1::phòng tránh bệnh lý tắc nghẽn mạch phổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Hai mục tiêu chiến lược trong quản lý VSD.",
      ["VSD-muc-tieu", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thời điểm phẫu thuật VSD theo giáo trình: Trẻ có tăng lưu lượng phổi nhiều, không lên cân cần phẫu thuật lúc {{c1::1 - 4 tháng tuổi}}; Hầu hết thông liên thất lớn cần phẫu thuật lúc {{c1::6 - 9 tháng tuổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 9 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Hai mốc thời điểm phẫu thuật kinh điển cần ghi nhớ chính xác khi thi.",
      ["VSD-thoi-diem-mo", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 3: THÔNG LIÊN NHĨ (ASD - PEDYTB) (12 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Thông liên nhĩ (ASD) chiếm tỷ lệ {{c1::6 - 10%}} tim bẩm sinh, với tỷ lệ giới tính {{c1::Nữ : Nam = 2 : 1}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Dị tật không tím hay gặp nhất ở người lớn.",
      ["ASD-dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Giáo trình phân loại thông liên nhĩ thành 4 nhóm giải phẫu: 1. {{c1::Thông liên nhĩ thứ phát (Ostium secundum, chiếm 60 - 70%)}}; 2. {{c1::Thông liên nhĩ tiền phát (Ostium primum)}}; 3. {{c1::Thể xoang tĩnh mạch (Sinus venosus)}}; 4. {{c1::Khuyết nóc xoang vành (Coronary sinus defect)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Thể xoang tĩnh mạch và khuyết nóc xoang vành không được coi là ASD thực sự.",
      ["ASD-giai-phau", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thông liên nhĩ đơn thuần thường {{c1::không có triệu chứng}}, thường không được phát hiện ở tuổi trẻ; nếu không điều trị sẽ dẫn đến mất bù khi gắng sức, loạn nhịp nhĩ, tắc nghẽn mạch phổi sau {{c1::3 đến 4 thập kỷ}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Tiến triển âm thầm đến tuổi 30-40 mới bộc lộ biến chứng.",
      ["ASD-lam-sang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu nghe tim kinh điển của thông liên nhĩ lỗ trung bình - lớn: {{c1::Tiếng tim thứ hai (T2) tách đôi cố định}} và {{c1::tiếng thổi tâm thu ở đầu trên xương ức do tăng lưu lượng qua van ĐMP}} (không phải do máu qua lỗ ASD).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Tiếng T2 tách đôi không đổi theo hô hấp là triệu chứng chìa khóa.",
      ["ASD-nghe-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trong thông liên nhĩ lớn, nghe tim có thể thấy tiếng thổi tâm trương ở phần dưới xương ức do {{c1::tăng lưu lượng máu qua van 3 lá}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Rung tâm trương cơ năng van 3 lá.",
      ["ASD-nghe-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Điện tâm đồ trong thông liên nhĩ lỗ tiên phát (Ostium primum) có dấu hiệu đặc trưng là {{c1::trục trái và khử cực ngược chiều kim đồng hồ}} (khác với lỗ thứ phát thường là trục phải).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Phản ánh bất thường dẫn truyền của hệ thống His-Purkinje do khuyết gối nội tâm mạc.",
      ["ASD-ECG", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Điều trị thông liên nhĩ theo giáo trình gồm hai phương pháp: {{c1::Phẫu thuật hoặc đóng bằng dụng cụ dưới da (qua da)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Đóng dù qua da là lựa chọn hàng đầu cho thể thứ phát có gờ mô > 5 mm.",
      ["ASD-dieu-tri", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 4: THÔNG SÀN NHĨ THẤT & CÒN ỐNG ĐỘNG MẠCH (14 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Thông sàn nhĩ thất (AVSD / kênh nhĩ thất) chiếm 4 - 5% tim bẩm sinh, và đặc biệt gặp ở {{c1::40% trẻ bị Down}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.3).<br><b>🔍 Đối chiếu PED:</b> Có tên gọi khác là khuyết gối nội tâm mạc (Endocardial cushion defect).",
      ["AVSD-Down", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phân loại thông sàn nhĩ thất theo giáo trình: Thể bán phần có tuýp 1 là {{c1::thông liên nhĩ tiền phát}}; Thể hoàn toàn bao gồm {{c1::thông liên nhĩ tiền phát và thông liên thất phần buồng nhận}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.3).<br><b>🔍 Đối chiếu PED:</b> Thể hoàn toàn kèm một van nhĩ thất chung duy nhất bắc cầu.",
      ["AVSD-phan-loai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thời điểm phẫu thuật điều trị thông sàn nhĩ thất theo giáo trình là lúc trẻ {{c1::3 - 6 tháng tuổi}}; cần theo dõi lâu dài vì có {{c1::15%}} dẫn đến hở van nhĩ thất hoặc tắc nghẽn LVOTO.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.3).<br><b>🔍 Đối chiếu PED:</b> Mổ sớm trước 6 tháng để phòng tăng áp phổi nặng ở trẻ Down.",
      ["AVSD-phau-thuat", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dịch tễ Còn ống động mạch (PDA): Chiếm 9 - 12% tim bẩm sinh; tỷ lệ 1 : 5000 ở trẻ đủ tháng nhưng rất cao ở trẻ non tháng theo cân nặng: Trẻ 500 - 999 g là {{c1::42%}}; Trẻ 1000 - 1499 g là {{c1::21%}}; Trẻ 1500 - 1750 g là {{c1::7%}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Bộ ba số liệu non tháng theo cân nặng kinh điển của giáo trình.",
      ["PDA-non-thang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tỷ lệ còn ống động mạch ở những trẻ sống trên vùng núi cao có thể cao gấp {{c1::30 lần}} trẻ sống ở vùng đồng bằng.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 10 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Áp lực riêng phần oxy thấp tại vùng núi cao cản trở đóng ống động mạch sinh lý.",
      ["PDA-nui-cao", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu mạch ngoại vi đặc trưng của còn ống động mạch lớn là {{c1::mạch nẩy mạnh chìm sâu (Corrigan)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Máu thoát nhanh từ ĐMC sang ĐMP trong thời kỳ tâm trương làm tụt huyết áp tâm trương.",
      ["PDA-mach-Corrigan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tiếng thổi kinh điển của còn ống động mạch là {{c1::tiếng thổi liên tục}} ở đầu trong xương đòn bên trái (dưới đòn trái); ở trẻ sơ sinh và non tháng có thể chỉ nghe thấy {{c1::tiếng thổi tâm thu}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Tiếng thổi liên tục Gibson (tiếng máy xay).",
      ["PDA-nghe-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Biểu hiện của Hội chứng Eisenmenger trong còn ống động mạch là {{c1::tím nửa dưới cơ thể (chân tím hơn tay)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Tím chuyên biệt (Differential cyanosis) do máu đen đổ vào ĐMC xuống sau nhánh dưới đòn trái.",
      ["PDA-Eisenmenger", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Điều trị đóng ống động mạch: Ở trẻ non tháng dùng thuốc {{c1::Indomethacin, Ibuprofen}} (chuyển phẫu thuật nếu thất bại); Ở trẻ lớn đóng bằng {{c1::coil hoặc dụng cụ (dù qua da)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Cochrane Review xác nhận Ibuprofen an toàn cho thận hơn Indomethacin.",
      ["PDA-dieu-tri", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 5: TỨ CHỨNG FALLOT & CẤP CỨU CƠN TÍM (PEDYTB CHUẨN) (20 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Tứ chứng Fallot chiếm tỷ lệ {{c1::4 - 8%}} tim bẩm sinh, là một trong các dạng phổ biến nhất của bệnh tim bẩm sinh có tím.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Tim bẩm sinh tím phổ biến nhất sau thời kỳ sơ sinh.",
      ["TOF-dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tứ chứng Fallot bao gồm 4 tổn thương: 1. {{c1::Thông liên thất phần phễu lớn}}; 2. {{c1::Hẹp đường ra thất phải}}; 3. {{c1::Động mạch chủ cưỡi ngựa trên vách liên thất}}; 4. {{c1::Phì đại thất phải do hẹp đường ra thất phải}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> 4 tổn thương kinh điển do lệch vách nón phễu.",
      ["TOF-4-ton-thuong", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Khái niệm Fallot hồng (Pink Fallot): Xảy ra khi {{c1::hẹp đường ra thất phải nhẹ}}, bệnh nhân không có tím.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Luồng shunt chủ yếu là Trái - Phải, biểu hiện giống VSD lớn.",
      ["Fallot-hong", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tiếng thổi tâm thu nghe được ở cạnh ức trái trên trong Fallot là do {{c1::hẹp đường ra thất phải}}, giáo trình nhấn mạnh {{c1::không phải do tiếng thổi qua lỗ thông liên thất}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Câu hỏi thi bẫy kinh điển: Thổi tâm thu là do hẹp đường ra thất phải.",
      ["TOF-thoi-tam-thu", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hình ảnh X-quang tim phổi kinh điển trong Fallot là {{c1::tim hình chiếc ủng (coeur en sabot)}} do mỏm tim hếch lên vì phì đại thất phải, cung ĐMP lõm và trường phổi sáng do giảm lưu lượng máu lên phổi.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> ĐTĐ thấy trục phải và dày thất phải.",
      ["TOF-Xquang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Cơ chế phát động Cơn tím thiếu oxy cấp (Hypoxic spell) ở trẻ Fallot là do {{c1::co thắt đường ra thất phải làm giảm lượng máu lên phổi trầm trọng và làm tăng dòng shunt Phải - Trái qua VSD}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Co thắt phễu cắt đứt dòng máu lên phổi.",
      ["Con-tim-co-che", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Biểu hiện của cơn tím Fallot gồm: Đột ngột {{c1::thở nhanh nông, kích thích, thở sâu và tăng tím}}; trường hợp nặng có thể dẫn đến {{c1::hôn mê, co giật, tai biến mạch não do tắc mạch (huyết khối/áp xe não)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 11-12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Biến chứng tắc mạch do tăng Hematocrit máu.",
      ["Con-tim-bieu-hien", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Cơ chế của tư thế ngồi xổm (Squatting) hoặc ngực gối: Làm {{c1::tăng hậu gánh (tăng sức cản ngoại vi)}} và làm {{c1::giảm dòng shunt Phải - Trái}}, đẩy máu qua phổi nhiều hơn.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Tăng SVR ép máu từ thất phải vượt qua phễu lên ĐMP.",
      ["Ngoi-xom-co-che", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Sáu bước xử trí cấp cứu Cơn tím Fallot theo giáo trình: 1. {{c1::Tư thế ngực gối (Knee-chest)}}; 2. {{c1::Thở oxy qua mặt nạ}}; 3. {{c1::Morphin 0,1 mg/kg tiêm dưới da hoặc tiêm bắp}}; 4. {{c1::Truyền dịch}}; 5. {{c1::Propranolol tiêm tĩnh mạch chậm}}; 6. {{c1::Natri bicarbonat nếu có toan chuyển hóa nặng}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Phác đồ 6 bước cấp cứu tại giường bắt buộc thuộc lòng khi đi thi.",
      ["Cap-cuu-con-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thuốc và liều dùng dự phòng cơn tím Fallot theo giáo trình là {{c1::Propranolol đường uống}} với liều {{c1::1 - 2 mg/kg/ngày chia 2 - 4 lần}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Dùng duy trì cho trẻ chờ phẫu thuật triệt để.",
      ["Du-phong-con-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thời điểm phẫu thuật triệt để (sửa chữa toàn bộ) đóng VSD và mở rộng đường ra thất phải trong Fallot theo giáo trình là lúc trẻ {{c1::4 - 6 tháng tuổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 12 - Mục 3.6).<br><b>🔍 Đối chiếu PED:</b> Mổ tạm thời làm cầu nối Blalock-Taussig cải tiến nếu giải phẫu nhánh ĐMP quá nhỏ.",
      ["TOF-phau-thuat", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 6: TGA, HLHS, EBSTEIN, TAPVC & TEO VAN BA LÁ (18 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Trong Chuyển gốc đại động mạch (d-TGA), động mạch chủ xuất phát từ {{c1::thất phải}} và động mạch phổi xuất phát từ {{c1::thất trái}}; hai vòng tuần hoàn chảy {{c1::song song với nhau}} thay vì nối tiếp.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Chiếm 4% tim bẩm sinh.",
      ["TGA-giai-phau", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Để bệnh nhân TGA tồn tại được, bắt buộc phải có các tổn thương phối hợp để {{c1::pha trộn máu (thông liên thất, thông liên nhĩ, còn ống động mạch)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Không có lỗ pha trộn máu trẻ sẽ tử vong trong vài giờ đầu.",
      ["TGA-pha-tron-mau", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Xử trí cấp cứu TGA sơ sinh gồm: Truyền {{c1::PGE1}} để duy trì mở ống động mạch và {{c1::phá vách liên nhĩ cấp cứu bằng bóng (Thủ thuật Rashkind)}} để đảm bảo pha trộn máu tầng nhĩ.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Hai biện pháp hồi sức cấp cứu sống còn tại giường.",
      ["TGA-cap-cuu", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phẫu thuật chuyển lại gốc động mạch ({{c1::Phẫu thuật Jatene / Arterial Switch}}) ngay {{c1::tuần đầu tiên sau sinh}} là lựa chọn tốt nhất cho bệnh nhân TGA không có VSD và không hẹp ĐMP.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Tuần đầu thất trái chưa bị thoái triển áp lực tống máu.",
      ["TGA-Jatene", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hai phương pháp phẫu thuật chuyển tầng nhĩ kinh điển trong TGA là phương pháp {{c1::Senning và Mustard}}; biến chứng lâu dài gồm tắc nghẽn tĩnh mạch, rối loạn nhịp và {{c1::suy chức năng thất phải (thất phải gánh hệ thống)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.9).<br><b>🔍 Đối chiếu PED:</b> Khoảng 80% có kết quả tốt ban đầu nhưng bộc lộ suy tim khi lớn.",
      ["TGA-Senning-Mustard", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Thân chung động mạch (Truncus Arteriosus) chiếm < 1% tim bẩm sinh, hay kết hợp với {{c1::Hội chứng DiGeorge (mất đoạn NST 22q11)}}; phẫu thuật triệt để phải tiến hành sớm trước {{c1::2 - 3 tháng tuổi}} để đề phòng bệnh mạch máu phổi cố định.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 13 - Mục 3.10).<br><b>🔍 Đối chiếu PED:</b> Gồm 1 VSD phễu lớn và 1 thân chung ĐM duy nhất cưỡi ngựa.",
      ["Truncus-Arteriosus", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bệnh Ebstein là bệnh hiếm gặp do sự bám thấp bất thường của {{c1::lá vách và lá sau van ba lá}} về phía mỏm thất phải, dẫn đến {{c1::nhĩ hóa một phần thất phải}} và gây hở nặng van ba lá.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Một dạng bệnh cơ tim của thất phải.",
      ["Ebstein-giai-phau", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Điện tâm đồ trong bệnh Ebstein: Sóng P khổng lồ ({{c1::sóng P kiểu dãy Himalaya}}) ở DII, block nhánh phải, và đặc biệt {{c1::Hội chứng Wolff-Parkinson-White (WPW)}} phát hiện ở {{c1::15%}} bệnh nhân.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> X-quang tim to hình bóng bàn hoặc bình nước.",
      ["Ebstein-ECG", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phương pháp phẫu thuật sửa van ba lá hiệu quả trong bệnh Ebstein là phương pháp {{c1::Cone (Cone procedure)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.11).<br><b>🔍 Đối chiếu PED:</b> Tạo hình van 3 lá dạng hình nón sinh lý.",
      ["Ebstein-Cone", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trong Bất thường hồi lưu tĩnh mạch phổi hoàn toàn (TAPVC), thể có tắc nghẽn (đặc biệt là {{c1::thể dưới tim ở trẻ sơ sinh}}) gây tăng áp phổi ác tính, phù phổi cấp dữ dội và đòi hỏi {{c1::phẫu thuật cấp cứu tối khẩn (tử vong lên đến 40%)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.12).<br><b>🔍 Đối chiếu PED:</b> Thể trên tim không tắc nghẽn có hình người tuyết (snowman sign).",
      ["TAPVC-duoi-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu điện tâm đồ kinh điển đặc biệt nhất của Teo tịt van ba lá (Tricuspid Atresia) là {{c1::trục trái và dày thất trái}} (rất đặc biệt vì hầu hết tim bẩm sinh có tím là trục phải/dày thất phải).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.13).<br><b>🔍 Đối chiếu PED:</b> Thất phải thiểu sản nặng, thất trái lớn đảm đương chức năng bơm máu duy nhất.",
      ["Teo-van-3-la-ECG", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Phẫu thuật điều trị Teo van ba lá theo quy trình nhiều giai đoạn hướng tới {{c1::Phẫu thuật Fontan cải tiến}} (nối tĩnh mạch chủ vào động mạch phổi, đưa thất trái duy nhất bơm máu hệ thống) với tỷ lệ sống sót {{c1::> 85% sau 10 năm}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14 - Mục 3.13).<br><b>🔍 Đối chiếu PED:</b> Phẫu thuật kinh điển cho sinh lý thất duy nhất.",
      ["Teo-van-3-la-Fontan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Trong Hội chứng thiểu sản thất trái (HLHS), tuần hoàn nuôi cơ thể phụ thuộc hoàn toàn vào {{c1::thất phải bơm máu qua ống động mạch (PDA) vào động mạch chủ xuống và chảy ngược nuôi não, vành}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 14-15 - Mục 3.14).<br><b>🔍 Đối chiếu PED:</b> Cấp cứu sơ sinh bắt buộc truyền PGE1 mở lại ống động mạch.",
      ["HLHS-tuan-hoan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Ba giai đoạn phẫu thuật tái tạo điều trị HLHS theo giáo trình: Giai đoạn 1 (tuần đầu sau sinh) là {{c1::phẫu thuật Norwood}}; Giai đoạn 2 (3 - 6 tháng tuổi) là {{c1::phẫu thuật Glenn hai hướng}}; Giai đoạn 3 (2 - 4 tuổi) là {{c1::phẫu thuật Fontan}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 15 - Mục 3.14).<br><b>🔍 Đối chiếu PED:</b> 3 giai đoạn phẫu thuật chuẩn mực điều trị tim một thất.",
      ["HLHS-3-giai-doan", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 7: HẸP EO ĐMC, HẸP VAN ĐMC & HẸP VAN ĐMP (14 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Hẹp eo động mạch chủ chiếm 5% tim bẩm sinh, hay gặp ở trẻ trai; ở trẻ gái rất hay phối hợp với {{c1::Hội chứng Turner (45,XO)}}; có tới {{c1::70%}} trường hợp phối hợp van ĐMC hai lá.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Vị trí hẹp đối diện ống động mạch dưới nhánh dưới đòn trái.",
      ["Hep-eo-DMC-dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Dấu hiệu lâm sàng kinh điển của Hẹp eo ĐMC ở trẻ lớn: Tăng huyết áp chi trên nhưng chi dưới thấp; {{c1::chênh lệch huyết áp tay - chân > 20 mmHg}}; mạch đùi yếu hoặc đến chậm so với mạch quay ({{c1::Radio-femoral delay}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Nghe tim có tiếng thổi tâm thu khoang liên sườn 2 bờ trái ức lan sau liên bả.",
      ["Hep-eo-DMC-lam-sang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hình ảnh X-quang đặc trưng của Hẹp eo ĐMC ở trẻ lớn là {{c1::dấu hiệu khuyết bờ dưới các xương sườn (Rib notching / Dấu hiệu Roesler)}} do tuần hoàn bàng hệ ĐM liên sườn giãn lớn bào mòn xương và {{c1::dấu hiệu số 3 (Figure of 3 sign)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 16 - Mục 3.16).<br><b>🔍 Đối chiếu PED:</b> Hai dấu hiệu X-quang kinh điển trong câu hỏi thi.",
      ["Hep-eo-DMC-Xquang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hẹp van động mạch phổi chiếm 8% tim bẩm sinh, thường phối hợp với {{c1::Hội chứng Noonan}}; nghe tim có {{c1::tiếng click tống máu nhỏ đi khi hít vào}} và tiếng thổi tâm thu tống máu khoang liên sườn 2 trái lan sau lưng.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 17 - Mục 3.17).<br><b>🔍 Đối chiếu PED:</b> Tiếng T2 tách đôi rộng, P2 mờ hoặc mất trong hẹp nặng.",
      ["Hep-van-DMP-lam-sang", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Biện pháp điều trị lựa chọn hàng đầu cho Hẹp van động mạch phổi là {{c1::nong van động mạch phổi bằng bóng qua da (Balloon pulmonary valvuloplasty)}} mang lại thành công lâu dài ở {{c1::85%}} các trường hợp.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 17 - Mục 3.17).<br><b>🔍 Đối chiếu PED:</b> An toàn, hiệu quả, tránh được phẫu thuật tim hở.",
      ["Hep-van-DMP-nong-bong", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Chế độ kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn đường uống tiêu chuẩn trước thủ thuật răng miệng là {{c1::Amoxicillin liều 50 mg/kg (tối đa 2 g)}} uống một liều duy nhất trước thủ thuật {{c1::30 đến 60 phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Nếu dị ứng Penicillin chuyển sang Clindamycin 20 mg/kg hoặc Azithromycin 15 mg/kg.",
      ["Khang-sinh-du-phong-IE"], "PED")

# ==============================================================================
# KHỐI 8: CÁC THẺ BASIC HỎI ĐÁP DUNG HÒA PEDYTB & PED (8 thẻ)
# ==============================================================================
add_b("Trình bày 4 dị tật giải phẫu bệnh học kinh điển hợp thành Tứ chứng Fallot?",
      "Bao gồm 4 tổn thương: 1. Thông liên thất phần phễu lớn. 2. Hẹp đường ra thất phải. 3. Động mạch chủ cưỡi ngựa trên vách liên thất. 4. Phì đại thất phải do hẹp đường ra thất phải.",
      "Nguồn gốc phôi thai học duy nhất của Tứ chứng Fallot là sự lệch vách nón phễu ra trước và lên trên. Tổn thương hẹp đường ra thất phải quyết định mức độ tím và tiên lượng của bệnh nhi.")

add_b("Trình bày chuỗi phản xạ cấp cứu Cơn tím Fallot cấp (Tet spell) tại giường bệnh?",
      "1. Đặt trẻ ở tư thế ngực gối (Knee-chest position). 2. Thở oxy qua mặt nạ. 3. Morphin 0,1 mg/kg tiêm dưới da hoặc tiêm bắp. 4. Truyền dịch duy trì thể tích tuần hoàn và chống cô đặc máu. 5. Propranolol tiêm tĩnh mạch chậm để giảm co thắt đường ra thất phải. 6. Natri bicarbonat nếu có toan chuyển hóa nặng.",
      "Tư thế ngực gối là động tác vật lý đầu tiên giúp tăng sức cản mạch hệ thống SVR ngay tức thì, ép máu từ thất phải vượt qua phễu lên phổi. Morphin giúp cắt đứt vòng xoắn kích thích giao cảm làm giãn cơ phễu thất phải.")

add_b("Giải thích cơ chế tại sao trẻ lớn mắc Tứ chứng Fallot lại có động tác ngồi xổm (Squatting)?",
      "Trẻ lớn có tư thế ngồi xổm (ngực gối) để làm tăng hậu gánh (tăng sức cản ngoại vi) và làm giảm dòng shunt Phải - Trái, đẩy máu qua phổi nhiều hơn.",
      "Ngồi xổm làm gập động mạch đùi và động mạch chậu, tăng áp lực động mạch hệ thống vượt qua áp lực thất phải. Nhờ đó, lượng máu đen bị đẩy sang động mạch chủ giảm đi, máu buộc phải tìm đường qua chỗ hẹp phễu lên động mạch phổi để hấp thu oxy.")

add_b("Trình bày dấu hiệu nghe tim kinh điển của Thông liên nhĩ và giải thích cơ chế?",
      "Tăng gánh tâm trương thất phải; Tiếng tim thứ hai (T2) tách đôi cố định; Tiếng thổi tâm thu ở đầu trên xương ức do tăng lưu lượng máu qua van động mạch phổi; Trong thông liên nhĩ lớn có thể có tiếng thổi tâm trương ở phần dưới xương ức do tăng lưu lượng máu qua van 3 lá.",
      "T2 tách đôi cố định là dấu hiệu then chốt nhất: Thất phải nhận máu liên tục từ nhĩ trái sang trong cả hai thì hô hấp, khiến thể tích tống máu thất phải luôn dư thừa và van động mạch phổi luôn đóng muộn một khoảng thời gian cố định so với van chủ.")

add_b("Mô tả triệu chứng mạch và huyết áp đặc trưng trong Còn ống động mạch (PDA) lớn?",
      "Mạch ngoại vi nẩy mạnh chìm sâu (Corrigan).",
      "Trong PDA lớn, thất trái tống một lượng thể tích máu rất lớn vào động mạch chủ trong kỳ tâm thu tạo sóng mạch nảy vọt. Đến kỳ tâm trương, máu thoát nhanh chóng và liên tục qua ống động mạch sang phổi làm áp lực tâm trương tụt giảm sâu. Chênh lệch huyết áp tâm thu và tâm trương mở rộng tạo nên mạch nảy mạnh chìm sâu.")

add_b("Vì sao trong Chuyển gốc đại động mạch (d-TGA), phẫu thuật chuyển gốc Jatene bắt buộc phải thực hiện trong tuần đầu sau sinh?",
      "Ngay tuần đầu tiên sau sinh là lựa chọn tốt nhất cho bệnh nhân TGA không có thông liên thất và không hẹp động mạch phổi. Ngay khi áp lực tuần hoàn phổi giảm xuống, thất trái phải đủ điều kiện để bơm máu vào tuần hoàn hệ thống với áp lực lớn hơn.",
      "Trong tuần đầu, thất trái vẫn còn chịu áp lực mạch phổi cao của thời kỳ bào thai nên cơ thất còn dày. Sau 1-2 tuần, sức cản phổi giảm làm thất trái thoái triển thành mỏng (deconditioned LV). Nếu mổ muộn sau tuần đầu, thất trái mỏng sẽ không đủ sức đảm đương áp lực hệ thống và bệnh nhân sẽ tử vong vì suy thất trái cấp sau mổ.")

add_b("Trình bày đặc điểm lâm sàng và cận lâm sàng giúp nhận diện Hẹp eo động mạch chủ ở trẻ lớn?",
      "Tăng huyết áp chi trên nhưng chi dưới huyết áp thấp hoặc không đo được; Chênh lệch huyết áp tay - chân > 20 mmHg; Mạch đùi bắt yếu hoặc đến chậm so với mạch quay (Radio-femoral delay); Tiếng thổi tâm thu khoang liên sườn 2 bờ trái ức lan ra sau lưng; X-quang có dấu hiệu khuyết bờ dưới các xương sườn (dấu hiệu Roesler) và dấu hiệu số 3.",
      "Khám mạch bẹn hai bên là bước thăm khám bắt buộc ở mọi trẻ tăng huyết áp hoặc suy tim. Khuyết bờ dưới xương sườn hình thành do tuần hoàn bàng hệ động mạch liên sườn giãn to ngoằn ngoèo để đưa máu qua chỗ hẹp nuôi nửa dưới cơ thể.")

add_b("Nêu nguyên tắc dự phòng viêm nội tâm mạc nhiễm khuẩn (IE) ở trẻ mắc bệnh tim bẩm sinh?",
      "Kháng sinh dự phòng trước các thủ thuật răng miệng hoặc can thiệp đường thở có chảy máu.",
      "Kháng sinh đầu tay là Amoxicillin liều 50 mg/kg uống trước thủ thuật 30-60 phút. Dòng máu chảy xoáy với vận tốc cao qua các lỗ thông hoặc chỗ hẹp làm tổn thương lớp nội mạc mạch máu, tạo điều kiện cho vi khuẩn bám dính hình thành sùi nhiễm trùng.")

# Save both files
target_release.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
target_master.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(cards)} harmonized cards for PED-43 successfully at both release and master paths!")
