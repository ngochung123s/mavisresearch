# -*- coding: utf-8 -*-
"""Append 42 detailed atomic cards to PED-43 to reach 161 cards total."""
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

# 1. Chi tiết Thân chung động mạch (Truncus Arteriosus)
add_c("[PED - Lâm sàng] Trong Thân chung động mạch (Truncus Arteriosus), phân loại Collett-Edwards chia thành 4 tuýp dựa vào {{c1::vị trí xuất phát của các nhánh động mạch phổi từ thân chung}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Phân loại:</b> Tuýp I thân ĐMP chung xuất phát từ thân chung; Tuýp II hai nhánh ĐMP xuất phát sát nhau ở mặt sau; Tuýp III xuất phát riêng rẽ hai bên.",
      ["Truncus-phan-loai"], "PED")

add_c("[PED - Lâm sàng] Khám tim ở bệnh nhân Thân chung động mạch nghe thấy tiếng thổi tâm thu tống máu cạnh trái ức và đặc biệt có {{c1::tiếng click tống máu}} ngay sau T1 do dòng máu dội qua van thân chung loạn sản.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Thính chẩn:</b> Nếu kèm hở van thân chung sẽ nghe thấy tiếng thổi tâm trương kèm mạch nảy chìm sâu.",
      ["Truncus-thinh-chan"], "PED")

add_c("[PED - Lâm sàng] Bệnh nhân Thân chung động mạch có kèm theo mất mạch bẹn ở cả hai bên là dấu hiệu cảnh báo tổn thương phối hợp cực kỳ nặng nề là {{c1::đứt đoạn quai động mạch chủ (Interrupted Aortic Arch)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Cấp cứu:</b> Bắt buộc truyền PGE1 và phẫu thuật sửa chữa toàn bộ khẩn cấp.",
      ["Truncus-dut-doan-quai"], "PED")

# 2. Chi tiết TAPVC (Bất thường hồi lưu TM phổi)
add_c("[PED - Lâm sàng] Bốn thể giải phẫu của Bất thường hồi lưu tĩnh mạch phổi hoàn toàn (TAPVC) gồm: {{c1::Thể trên tim (Supracardiac), Thể trong tim (Cardiac), Thể dưới tim (Infracardiac) và Thể hỗn hợp (Mixed)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Dịch tễ:</b> Thể trên tim đổ vào tĩnh mạch vô danh là thể thường gặp nhất (chiếm 45-50%).",
      ["TAPVC-4-the"], "PED")

add_c("[PED - Lâm sàng] Trong TAPVC thể dưới tim, các tĩnh mạch phổi hợp lưu thành một thân chung chui qua cơ hoành đi xuống để đổ vào {{c1::hệ thống tĩnh mạch cửa hoặc tĩnh mạch chủ dưới}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Cơ chế:</b> Thân tĩnh mạch bị chèn ép khi chui qua lỗ cơ hoành và chịu áp lực cao của giường mao mạch gan gây tăng áp phổi ác tính.",
      ["TAPVC-duoi-tim-co-che"], "PED")

add_c("[PED - Lâm sàng] Hình ảnh X-quang 'Người tuyết' (Snowman sign) trong TAPVC thể trên tim được tạo thành bởi: Nửa trên là {{c1::tĩnh mạch dọc bất thường, tĩnh mạch vô danh và tĩnh mạch chủ trên giãn to}}; Nửa dưới là {{c1::bóng tim to toàn bộ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Hình ảnh:</b> Dấu hiệu số 8 kinh điển xuất hiện rõ ở trẻ sau vài tháng tuổi.",
      ["TAPVC-nguoi-tuyet"], "PED")

# 3. Chi tiết Bệnh Ebstein
add_c("[PED - Lâm sàng] Trong bệnh Ebstein, lá van ba lá duy nhất bám đúng vị trí vòng van nhĩ thất giải phẫu, có kích thước phì đại rất lớn và di động tự do dạng cánh buồm là {{c1::lá van trước (Anterior leaflet)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Giải phẫu:</b> Trong khi lá vách và lá sau bị dính chặt bám thấp sâu vào cơ tâm thất phải.",
      ["Ebstein-la-truoc"], "PED")

add_c("[PED - Lâm sàng] Cơ chế gây tím tái trong bệnh Ebstein là do luồng shunt Phải - Trái qua lỗ bầu dục hoặc thông liên nhĩ, hình thành khi {{c1::áp lực tâm nhĩ phải tăng cao vượt áp lực tâm nhĩ trái do ứ trệ máu và hở ba lá nặng}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Huyết động:</b> Máu đen từ nhĩ phải tràn sang nhĩ trái gây tím trung ương.",
      ["Ebstein-co-che-tim"], "PED")

# 4. Chi tiết Teo van ba lá (Tricuspid Atresia)
add_c("[PED - Lâm sàng] Ở trẻ sơ sinh mắc Teo van ba lá kèm hẹp nặng van động mạch phổi, lưu lượng máu lên phổi quá ít gây tím tái trầm trọng, biện pháp phẫu thuật tạm thời cấp cứu giai đoạn sơ sinh là {{c1::làm cầu nối Blalock-Taussig cải tiến (mBT shunt)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Ngoại khoa:</b> Ngược lại nếu không hẹp ĐMP máu lên phổi quá nhiều gây suy tim, phải làm phẫu thuật thắt đai ĐMP (PA banding).",
      ["Teo-van-3-la-BT-shunt"], "PED")

add_c("[PED - Lâm sàng] Điều kiện huyết động học bắt buộc để thực hiện phẫu thuật Fontan thành công là sức cản mạch máu phổi (PVR) phải thấp dưới {{c1::< 2 đến 3 đơn vị Wood}} và áp lực động mạch phổi trung bình phải dưới {{c1::< 15 mmHg}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Tiêu chuẩn:</b> Do dòng máu tĩnh mạch về phổi hoàn toàn thụ động không có lực đẩy của tâm thất.",
      ["Fontan-tieu-chuan-PVR"], "PED")

# 5. Chi tiết Hội chứng thiểu sản thất trái (HLHS)
add_c("[PED - Lâm sàng] Trong phẫu thuật Norwood điều trị HLHS giai đoạn 1, thì tái tạo đường tống máu đại tuần hoàn được thực hiện bằng cách {{c1::nối thân động mạch phổi vào quai động mạch chủ thiểu sản để tạo thành một động mạch chủ mới (Neoaorta)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Kỹ thuật:</b> Đưa tâm thất phải duy nhất làm nhiệm vụ tống máu nuôi toàn bộ cơ thể.",
      ["Norwood-Neoaorta"], "PED")

add_c("[PED - Lâm sàng] Cải tiến Sano trong phẫu thuật Norwood giai đoạn 1 sử dụng một đoạn ống ghép nhân tạo không van nối từ {{c1::tâm thất phải}} lên {{c1::ngã ba thân động mạch phổi}} thay thế cho cầu nối Blalock-Taussig.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Ưu điểm:</b> Giữ vững áp lực tâm trương động mạch chủ, cải thiện tưới máu mạch vành và giảm nguy cơ sốc tim.",
      ["Norwood-Sano-shunt"], "PED")

# 6. Chi tiết Hẹp eo ĐMC (CoA) & LVOTO
add_c("[PED - Lâm sàng] Cơ chế gây tăng huyết áp chi trên trong Hẹp eo động mạch chủ gồm hai cơ chế phối hợp: {{c1::cản trở cơ học dòng máu qua chỗ hẹp}} và {{c1::thiếu máu tưới nuôi thận mạn tính kích hoạt giải phóng Renin từ hệ RAAS}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Sinh lý:</b> Giải thích tại sao nhiều bệnh nhân vẫn còn tăng huyết áp tồn dư sau phẫu thuật giải tỏa chỗ hẹp.",
      ["CoA-co-che-tang-HA"], "PED")

add_c("[PED - Lâm sàng] Mọi trẻ gái được chẩn đoán Hẹp eo động mạch chủ đều có chỉ định bắt buộc làm xét nghiệm di truyền {{c1::nhiễm sắc thể đồ (Karyotype)}} để tầm soát Hội chứng Turner (45,XO).",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Di truyền:</b> Ngược lại, mọi trẻ gái mắc Turner đều phải siêu âm tim kiểm tra quai động mạch chủ.",
      ["CoA-Turner-Karyotype"], "PED")

add_c("[PED - Lâm sàng] Bốn thể giải phẫu của tắc nghẽn đường ra thất trái (LVOTO) gồm: {{c1::Hẹp tại van động mạch chủ, Hẹp trên van ĐMC, Hẹp dưới van ĐMC dạng gờ xơ cơ và Hẹp dưới van ĐMC dạng đường hầm}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Giải phẫu:</b> Hẹp tại van chiếm đa số các trường hợp.",
      ["LVOTO-4-the"], "PED")

add_c("[PED - Lâm sàng] Hội chứng Williams (Williams-Beuren) do mất đoạn gen Elastin trên nhiễm sắc thể 7q11.23 thường phối hợp kinh điển với tổn thương tim mạch là {{c1::hẹp trên van động mạch chủ (Supravalvular AS)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Lâm sàng:</b> Trẻ có khuôn mặt giống chú lùn (Elfin face), tính cách cởi mở và tăng canxi máu thời thơ ấu.",
      ["Hoi-chung-Williams"], "PED")

add_c("[PED - Lâm sàng] Phẫu thuật Ross điều trị bệnh van động mạch chủ nặng ở trẻ em là kỹ thuật lấy {{c1::van động mạch phổi tự thân}} chuyển sang thay thế van động mạch chủ và đặt ống ghép có van vào đường ra thất phải.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Ưu điểm:</b> Van phổi tự thân có khả năng phát triển kích thước theo sự lớn lên của đứa trẻ và không cần dùng thuốc kháng đông suốt đời.",
      ["Phau-thuat-Ross"], "PED")

# 7. Chi tiết Hẹp van ĐMP & Noonan
add_c("[PED - Lâm sàng] Tiếng click tống máu (Ejection click) trong Hẹp van động mạch phổi có đặc điểm biến đổi thính chẩn đặc biệt là {{c1::nhỏ đi hoặc biến mất hoàn toàn trong thì hít vào sâu}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Cơ chế:</b> Hít vào làm tăng hồi lưu máu về thất phải làm căng sớm lá van phổi trước khi thất co bóp.",
      ["Click-van-DMP"], "PED")

add_c("[PED - Lâm sàng] Trong Hẹp van động mạch phổi nặng, nghe tim thấy thành phần van phổi P2 của tiếng tim thứ hai có đặc điểm là {{c1::mờ nhạt hoặc biến mất hoàn toàn}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8).<br><b>🔍 Thính chẩn:</b> Tiếng T2 tách đôi rất rộng với thành phần A2 đơn độc.",
      ["P2-mo-trong-PS"], "PED")

# 8. Cơn tím Fallot & Xử trí chuyên sâu
add_c("[PED - Lâm sàng] Trong cấp cứu cơn tím Fallot, động tác ép chặt hai đùi vào bụng ở tư thế ngực gối (Knee-chest) làm tăng sức cản hệ thống SVR bằng cách {{c1::gập nếp gấp bẹn ép nghẽn cơ học động mạch đùi hai bên}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Cơ chế:</b> Đẩy dòng máu từ thất phải vượt qua phễu lên động mạch phổi để hấp thu oxy.",
      ["Nguc-goi-dong-mach-dui"], "PED")

add_c("[PED - Lâm sàng] Liều tiêm dưới da hoặc tiêm bắp của Morphin Sulfate trong cấp cứu cơn tím Fallot ở trẻ em là {{c1::0,1 mg/kg}}.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Dược lý:</b> Giúp ức chế trung tâm hô hấp làm dịu cơn thở sâu kích thích, giảm giao cảm và giãn phễu cơ thất phải.",
      ["Morphin-lieu-Fallot"], "PED")

add_c("[PED - Lâm sàng] Liều tiêm tĩnh mạch rất chậm của Propranolol trong điều trị cơn tím Fallot cấp trơ với Morphin là {{c1::0,05 đến 0,1 mg/kg}} tiêm TM trong 5 đến 10 phút dưới monitor theo dõi điện tim.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Cảnh báo:</b> Tiêm nhanh có thể gây nhịp chậm xoang kịch phát và ngừng tim.",
      ["Propranolol-TM-Fallot"], "PED")

add_c("[PED - Lâm sàng] Thuốc chẹn beta Propranolol đường uống dùng dự phòng cơn tím Fallot ở trẻ chờ phẫu thuật có liều dùng từ {{c1::1 đến 2 mg/kg/ngày}} chia làm 2 đến 4 lần.",
      "<b>📚 Nguồn:</b> PED (Mục 7.3).<br><b>🔍 Thực hành:</b> Uống đều đặn hàng ngày để ngăn chặn các cơn co thắt phễu kịch phát.",
      ["Propranolol-uong-du-phong"], "PED")

# 9. Bệnh phụ thuộc ống động mạch & PGE1
add_c("[PED - Lâm sàng] Các bệnh tim bẩm sinh phụ thuộc ống động mạch có tưới máu đại tuần hoàn (HLHS, hẹp eo ĐMC nặng, hẹp van ĐMC nguy kịch) đòi hỏi duy trì mở ống động mạch bằng {{c1::truyền tĩnh mạch liên tục Prostaglandin E1 (PGE1)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 0).<br><b>🔍 Liều dùng:</b> Bắt đầu từ 0,01 đến 0,05 µg/kg/phút qua đường truyền tĩnh mạch lớn.",
      ["PGE1-phu-thuoc-PDA"], "PED")

add_c("[PED - Lâm sàng] Tác dụng phụ nguy hiểm thường gặp nhất khi truyền Prostaglandin E1 ở trẻ sơ sinh là {{c1::cơn ngừng thở (Apnea)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 0).<br><b>🔍 Cấp cứu:</b> Bắt buộc chuẩn bị sẵn sàng bóng bóp qua mask và dụng cụ đặt nội khí quản tại giường.",
      ["PGE1-tac-dung-phu"], "PED")

# 10. Dự phòng Viêm nội tâm mạc nhiễm khuẩn (IE)
add_c("[PED - Lâm sàng] Chỉ định dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn bắt buộc áp dụng trong vòng {{c1::6 tháng đầu sau phẫu thuật hoặc can thiệp}} đặt vật liệu nhân tạo trong tim.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Khuyến cáo:</b> Sau 6 tháng lớp nội mạc mạch máu đã bao phủ hoàn toàn bề mặt vật liệu nhân tạo.",
      ["IE-du-phong-6-thang"], "PED")

add_c("[PED - Lâm sàng] Đối với bệnh nhân tim bẩm sinh có tím chưa được phẫu thuật sửa chữa triệt để, chỉ định dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn được áp dụng {{c1::suốt đời}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Khuyến cáo:</b> Luôn duy trì vệ sinh răng miệng tốt và uống Amoxicillin 50 mg/kg trước các thủ thuật răng miệng có chảy máu.",
      ["IE-du-phong-suot-doi"], "PED")

add_c("[PED - Lâm sàng] Liều dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn đường uống bằng Amoxicillin ở trẻ em là {{c1::50 mg/kg}} (liều tối đa 2 g), uống một liều duy nhất trước thủ thuật {{c1::30 đến 60 phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Nếu dị ứng Penicillin chuyển sang Clindamycin 20 mg/kg hoặc Azithromycin 15 mg/kg.",
      ["Amoxicillin-lieu-IE"], "PED")

# 11. Ca lâm sàng thực chiến
add_c("[PED - Lâm sàng] Trong Case 1 cấp cứu cơn tím Fallot ở trẻ 10 tháng, SpO2 tụt xuống 52%, chuỗi hành động cấp cứu đầu tiên tại giường là {{c1::đặt trẻ tư thế ngực gối và thở oxy 100% qua mask có túi}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 1).<br><b>🔍 Xử trí:</b> Sau đó tiêm ngay Morphine Sulfate 0,1 mg/kg dưới da và lập đường truyền bù dịch NaCl 0,9%.",
      ["Case-1-Fallot-cap-cuu"], "PED")

add_c("[PED - Lâm sàng] Trong Case 2 phát hiện còn ống động mạch lớn ở trẻ sinh non 29 tuần, phác đồ điều trị đóng ống động mạch bằng thuốc lựa chọn hàng đầu là {{c1::Ibuprofen đường tĩnh mạch liệu trình 3 liều (10 - 5 - 5 mg/kg cách nhau 24 giờ)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 12 - Case 2).<br><b>🔍 Xử trí:</b> Giúp đóng ống động mạch thành công mà ít nguy cơ suy thận hơn Indomethacin.",
      ["Case-2-PDA-Ibuprofen"], "PED")

# 12. Checkpoint tư duy phản biện
add_c("[PED - Lâm sàng] Checkpoint: Trẻ mắc Tứ chứng Fallot có bản năng ngồi xổm khi đang chơi đùa vì động tác này làm {{c1::gập động mạch đùi, tăng sức cản mạch máu hệ thống SVR đột ngột}}, ép máu từ thất phải vượt qua phễu lên phổi để hấp thu oxy.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 1).<br><b>🔍 Cơ chế:</b> Giúp trẻ nhanh chóng tự cắt cơn thiếu oxy não và đỡ mệt.",
      ["Checkpoint-ngoi-xom"], "PED")

add_c("[PED - Lâm sàng] Checkpoint: Dấu hiệu điện tâm đồ then chốt giúp phân biệt Thông liên nhĩ lỗ tiên phát với lỗ thứ phát là {{c1::ASD lỗ tiên phát có trục trái và khử cực ngược chiều kim đồng hồ}} (trong khi lỗ thứ phát thường là trục phải).",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 2).<br><b>🔍 Điện tim:</b> Do khiếm khuyết phát triển của gối nội tâm mạc làm thay đổi hướng lan truyền khử cực.",
      ["Checkpoint-ASD-truc-trai"], "PED")

add_c("[PED - Lâm sàng] Checkpoint: Dấu hiệu lâm sàng tại giường phân biệt tím trung ương do tim với tím ngoại vi do lạnh là: Tím trung ương xuất hiện ở cả {{c1::niêm mạc lưỡi, kết mạc mắt và đầu chi với SpO2 giảm}} và không đổi sau khi sưởi ấm.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 3).<br><b>🔍 Khám:</b> Tím ngoại vi chỉ xuất hiện ở đầu chi lạnh do co mạch, niêm mạc miệng vẫn hồng hào và SpO2 bình thường.",
      ["Checkpoint-phan-biet-tim"], "PED")

add_c("[PED - Lâm sàng] Checkpoint: Trong Hẹp eo động mạch chủ, huyết áp chi trên cao hơn huyết áp chi dưới vì {{c1::vị trí hẹp nằm dưới chỗ xuất phát của động mạch dưới đòn trái, khiến chi trên nhận máu trước chỗ hẹp có áp lực cao và chi dưới nhận máu sau chỗ hẹp có áp lực thấp}}.",
      "<b>📚 Nguồn:</b> PED (Mục 11 - Checkpoint 4).<br><b>🔍 Huyết động:</b> Tạo chênh lệch huyết áp tay - chân > 20 mmHg.",
      ["Checkpoint-CoA-huyet-ap"], "PED")

# 13. Tips thực hành lâm sàng
add_c("[PED - Lâm sàng] Tip thực hành: Khi trẻ Fallot khóc quấy xuất hiện cơn tím tái đậm, phản xạ đầu tiên của điều dưỡng là {{c1::lập tức gập chặt hai đầu gối trẻ áp sát vào ngực}} trước khi đi tìm thuốc.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 1).<br><b>🔍 Phản xạ:</b> Động tác vật lý tăng SVR ngay tức thì để cứu tế bào não.",
      ["Tip-nguc-goi-dau-tien"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Không bao giờ đo huyết áp chỉ ở một tay; luôn đo huyết áp ở {{c1::cả tay phải và một trong hai chân}} để không bao giờ bỏ sót bệnh hẹp eo động mạch chủ.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 2).<br><b>🔍 Khám:</b> Chênh lệch HA tay - chân > 20 mmHg là tiêu chuẩn vàng chẩn đoán lâm sàng.",
      ["Tip-do-HA-4-chi"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Tiếng tim T2 tách đôi cố định không thay đổi theo nhịp hô hấp là chìa khóa vàng thính chẩn chẩn đoán {{c1::Thông liên nhĩ lỗ lớn}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 4).<br><b>🔍 Thính chẩn:</b> Dấu hiệu kinh điển không bao giờ thay đổi theo chu kỳ hít thở.",
      ["Tip-T2-tach-doi-co-dinh"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Dấu hiệu mạch nảy rất mạnh và chìm sâu (mạch Corrigan) ở trẻ sơ sinh là chỉ điểm lâm sàng kinh điển của {{c1::Còn ống động mạch lớn có ý nghĩa huyết động}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 5).<br><b>🔍 Khám:</b> Sờ mạch bẹn thấy dội mạnh vào ngón tay và tụt nhanh.",
      ["Tip-mach-Corrigan-PDA"], "PED")

add_c("[PED - Lâm sàng] Tip thực hành: Khi nghe thấy tiếng thổi tâm thu ở tim đột ngột nhỏ đi bất thường ở một trẻ Fallot đang khó thở, phải coi chừng trẻ đang rơi vào {{c1::cơn co thắt cơ phễu đường ra thất phải cắt đứt dòng máu lên phổi (cơn tím cấp)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 12).<br><b>🔍 Cảnh báo:</b> Tiếng thổi nhỏ đi là dấu hiệu nguy kịch đe dọa ngừng tim chứ không phải thuyên giảm bệnh.",
      ["Tip-thoi-nho-di-Fallot"], "PED")

add_c("[PED - Lâm sàng] Tiêu chuẩn xuất viện an toàn của trẻ tim bẩm sinh: Trẻ không còn khó thở khi ăn bú, tăng cân ổn định, không có cơn tím tái tại viện, phác đồ thuốc uống duy trì ổn định tối thiểu {{c1::48 giờ}}, và có {{c1::lịch hẹn can thiệp hoặc phẫu thuật cụ thể}}.",
      "<b>📚 Nguồn:</b> PED (Mục 14.2).<br><b>🔍 Xuất viện:</b> Gia đình nắm vững kỹ năng sơ cứu tư thế ngực gối tại nhà.",
      ["Tieu-chuan-xuat-vien-CHD"], "PED")

# Write to both files
p_rel.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
p_mas.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-43: {len(cards)} cards successfully generated!")
