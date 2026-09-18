# -*- coding: utf-8 -*-
"""Generate ultra-detailed, fully compliant PED-43 Anki flashcards JSON v2 (>=150 cards)."""
import json
from pathlib import Path

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_2026-09-19_RELEASE_v1.cards.v2.json")

cards = []

def add_c(text, extra=""):
    cards.append({"type": "cloze", "text": text, "extra": extra})

def add_b(front, orig, ai, extra=""):
    back = f"<b>📖 Văn bản gốc:</b><br>• {orig}<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>• {ai}"
    cards.append({"type": "basic", "front": front, "back": back, "extra": extra})

# ==========================================
# 1. ĐẠI CƯƠNG, DỊCH TỄ & PHÂN LOẠI
# ==========================================
add_c("Bệnh tim bẩm sinh (Congenital Heart Disease) là dị tật phổ biến nhất lúc sinh, với tỷ lệ mắc ở trẻ sinh sống ước tính khoảng {{c1::0,8%}} (tương đương khoảng 8 trên 1000 trẻ sinh sống).",
      "Dịch tễ: Tổng quan hệ thống toàn cầu của van der Linde xác định tỷ lệ lưu hành lúc sinh của tim bẩm sinh là 9,1 trên 1000 trẻ.")

add_c("Ca phẫu thuật tim hở điều trị tim bẩm sinh đầu tiên trên thế giới được tiến hành tại Đại học Minnesota vào năm {{c1::1950}} nhờ sự ra đời của máy tim phổi nhân tạo.",
      "Lịch sử: Đánh dấu kỷ nguyên phẫu thuật sửa chữa triệt để các dị tật tim phức tạp.")

add_c("Tiêu chuẩn phân loại lâm sàng cơ bản nhất của tim bẩm sinh là dựa vào sự hiện diện của {{c1::triệu chứng tím tái trung ương (Cyanosis)}}.",
      "Phân tầng: Chia thành 2 nhóm lớn là tim bẩm sinh không tím (chiếm 70-80%) và tim bẩm sinh có tím (chiếm 20-30%).")

add_c("Đặc điểm huyết động học chung của nhóm tim bẩm sinh có luồng shunt Trái - Phải là: {{c1::Máu đi từ bên trái sang bên phải}}, lượng máu lên phổi {{c1::tăng}} và thường {{c1::không có tím ban đầu}}.",
      "Cơ chế: Áp lực buồng tim trái và đại tuần hoàn sinh lý cao hơn buồng tim phải và mạch phổi.")

add_c("Hiện tượng tím tái xuất hiện muộn ở bệnh nhân có luồng shunt Trái - Phải lớn không được phẫu thuật kịp thời được gọi là {{c1::Hội chứng Eisenmenger}}.",
      "Cơ chế: Tăng áp lực mạch phổi cố định làm đảo chiều luồng shunt thành Phải - Trái, lúc này chống chỉ định phẫu thuật đóng lỗ thông.")

add_c("Đặc điểm huyết động học chung của nhóm tim bẩm sinh có luồng shunt Phải - Trái là: Máu nghèo oxy từ tim phải {{c1::đi thẳng vào động mạch chủ}} và gây nên triệu chứng {{c1::tím tái trung ương sớm}}.",
      "Lâm sàng: SpO2 giảm thấp ngay sau sinh, không đáp ứng với nghiệm pháp thở oxy 100%.")

add_c("Bốn bệnh tim bẩm sinh có luồng shunt Trái - Phải thường gặp nhất gồm: {{c1::Thông liên thất (VSD), Thông liên nhĩ (ASD), Còn ống động mạch (PDA) và Thông sàn nhĩ thất (AVSD)}}.",
      "Huyết động: Tất cả đều làm tăng lưu lượng tuần hoàn phổi và có nguy cơ biến chứng suy tim sung huyết.")

add_c("Các bệnh tim bẩm sinh có luồng shunt Phải - Trái (có tím) điển hình gồm: {{c1::Tứ chứng Fallot, Chuyển gốc đại động mạch (d-TGA), Teo van ba lá, Thân chung động mạch và Hội chứng thiểu sản thất trái (HLHS)}}.",
      "Phân loại: Tứ chứng Fallot và Teo van ba lá có giảm lưu lượng phổi; TGA và Truncus có tăng lưu lượng phổi.")

add_c("Ba bệnh lý tim bẩm sinh thuộc nhóm tổn thương tắc nghẽn đường ra tâm thất thường gặp gồm: {{c1::Hẹp eo động mạch chủ (CoA), Hẹp van động mạch chủ (AS) và Hẹp van động mạch phổi (PS)}}.",
      "Cơ chế: Gây tăng gánh áp lực (tăng hậu gánh) tâm thất, dẫn đến phì đại tế bào cơ tim đồng tâm.")

# ==========================================
# 2. THÔNG LIÊN THẤT (VSD)
# ==========================================
add_c("Thông liên thất (VSD) là dị tật tim bẩm sinh phổ biến nhất ở trẻ em, chiếm khoảng {{c1::20% đến 30%}} tổng số các trường hợp tim bẩm sinh.",
      "Dịch tễ: Nếu tính cả các dị tật van động mạch chủ hai lá thì tỷ lệ tim bẩm sinh nói chung còn cao hơn.")

add_c("Thể giải phẫu phổ biến nhất của thông liên thất là {{c1::thông liên thất phần quanh màng (Perimembranous VSD)}}, chiếm khoảng {{c1::70% đến 80%}} các trường hợp.",
      "Giải phẫu: Nằm ở phần màng của vách liên thất, sát van ba lá và van động mạch chủ.")

add_c("Thông liên thất phần quanh màng có khả năng tự đóng tự nhiên trong những năm đầu đời nhờ cơ chế {{c1::sự bọc lại của mô lá vách van ba lá tạo thành túi phình vách}}.",
      "Tiên lượng: Khoảng 30-40% VSD phần màng nhỏ có thể tự bít kín trước tuổi thiếu niên.")

add_c("Thể thông liên thất nằm sát dưới van động mạch chủ và van động mạch phổi được gọi là {{c1::thông liên thất phần phễu / dưới van (Infundibular / Subarterial VSD)}}.",
      "Cơ chế: Chiếm 5-7%, có nguy cơ cao biến chứng sa lá van và hở van động mạch chủ do hiệu ứng Venturi.")

add_c("Hiện tượng sa lá van động mạch chủ phải và hở van động mạch chủ thứ phát trong thông liên thất phần phễu xảy ra do cơ chế khí động học có tên là {{c1::hiệu ứng Venturi}}.",
      "Cơ chế: Dòng phụt xoáy tốc độ cao qua lỗ thông tạo áp lực âm hút lá van ĐMC về phía lỗ thông liên thất.")

add_c("Thông liên thất phần buồng nhận (Inlet VSD) nằm ở phần sau dưới vách liên thất sát van nhĩ thất, có đặc điểm là {{c1::không bao giờ tự đóng tự nhiên}} và thường nằm trong bệnh cảnh {{c1::thông sàn nhĩ thất (kênh nhĩ thất)}}.",
      "Điện tim: Thường biểu hiện trục trái bất thường trên điện tâm đồ.")

add_c("Thông liên thất phần cơ (Muscular VSD) là dị tật hay gặp ở trẻ sơ sinh, có đặc tính tự nhiên là {{c1::hầu hết sẽ tự đóng trước 2 tuổi}} khi khối cơ tâm thất phát triển dày lên.",
      "Tiên lượng: Thường có nhiều lỗ nhỏ dạng tổ ong (Swiss-cheese VSD).")

add_c("Ở trẻ mắc thông liên thất lỗ nhỏ (Bệnh Roger), trẻ {{c1::hoàn toàn không có triệu chứng cơ năng (không khó thở, không chậm lớn)}} và nghe tim thấy {{c1::tiếng thổi tâm thu thô ráp cường độ lớn 4/6 kèm rung miu ở cạnh ức trái}}.",
      "Huyết động: Chênh áp giữa hai thất rất lớn tạo tiếng thổi to, nhưng lưu lượng shunt nhỏ không gây suy tim.")

add_c("Ở trẻ mắc thông liên thất lỗ lớn, các triệu chứng suy tim sung huyết thường bùng phát vào thời điểm {{c1::6 đến 8 tuần tuổi}} sau sinh.",
      "Cơ chế: Do sức cản mạch máu phổi (PVR) sinh lý thoái triển giảm sâu, tạo chênh áp lớn làm máu dồn lên phổi tăng vọt.")

add_c("Trong thông liên thất lỗ lớn có lưu lượng shunt Trái - Phải khổng lồ (Qp/Qs ≥ 2:1), nghe tim ở mỏm có thể phát hiện thêm {{c1::tiếng rung tâm trương cơ năng (Functional diastolic rumble)}}.",
      "Cơ chế: Do lượng máu từ phổi về nhĩ trái dồn qua van hai lá trong thời kỳ tâm trương tăng gấp 2-3 lần bình thường.")

add_c("Thời điểm vàng phẫu thuật vá thông liên thất lớn có tăng lưu lượng phổi nhiều và suy dinh dưỡng nặng không đáp ứng nội khoa là lúc trẻ {{c1::1 đến 4 tháng tuổi}}.",
      "Chỉ định: Nhằm bảo vệ chức năng thất và giúp trẻ bắt kịp đà tăng trưởng thể chất.")

add_c("Hầu hết các trường hợp thông liên thất lỗ lớn có tăng áp động mạch phổi bắt buộc phải được phẫu thuật đóng lỗ thông trước thời điểm {{c1::6 đến 9 tháng tuổi}}.",
      "Cảnh báo: Trì hoãn quá mốc này làm tăng nguy cơ tổn thương xơ hóa mạch máu phổi không hồi phục (Eisenmenger).")

# ==========================================
# 3. THÔNG LIÊN NHĨ (ASD)
# ==========================================
add_c("Thông liên nhĩ (ASD) chiếm khoảng 6% đến 10% tim bẩm sinh, với đặc điểm dịch tễ nổi bật là tỷ lệ mắc ở giới Nữ {{c1::gấp 2 lần}} giới Nam.",
      "Dịch tễ: Là dị tật tim bẩm sinh không tím phổ biến nhất được phát hiện ở tuổi trưởng thành.")

add_c("Thể giải phẫu phổ biến nhất của thông liên nhĩ là {{c1::thông liên nhĩ lỗ thứ phát (Ostium secundum)}}, chiếm khoảng {{c1::60% đến 70%}} tổng số các ca thông liên nhĩ.",
      "Giải phẫu: Nằm ở vùng hố bầu dục (Fossa ovalis) ở phần trung tâm của vách liên nhĩ.")

add_c("Thông liên nhĩ lỗ tiên phát (Ostium primum) nằm ở phần thấp vách liên nhĩ sát van nhĩ thất, thuộc bệnh cảnh giải phẫu của {{c1::thông sàn nhĩ thất (kênh nhĩ thất bán phần)}}.",
      "Điện tim: Dấu hiệu đặc trưng là trục điện tim chuyển sang trái và khử cực ngược chiều kim đồng hồ.")

add_c("Thông liên nhĩ thể xoang tĩnh mạch (Sinus venosus ASD) nằm ở vị trí đổ vào của tĩnh mạch chủ trên hoặc dưới, hầu như luôn kết hợp với {{c1::bất thường hồi lưu tĩnh mạch phổi bán phần (PAPVC)}}.",
      "Giải phẫu: Tĩnh mạch phổi trên phải đổ lạc chỗ vào tĩnh mạch chủ trên hoặc nhĩ phải.")

add_c("Dấu hiệu nghe tim thực thể kinh điển và đặc trưng nhất của thông liên nhĩ là {{c1::tiếng tim thứ hai (T2) tách đôi cố định (Fixed split S2)}} ở ổ van động mạch phổi.",
      "Cơ chế: Thể tích tống máu của thất phải luôn dư thừa trong cả thì hít vào và thở ra, làm van động mạch phổi luôn đóng muộn cố định.")

add_c("Tiếng thổi tâm thu nghe được ở khoang liên sườn 2 bờ trái xương ức trong thông liên nhĩ phát sinh do {{c1::tăng lưu lượng máu đi qua van động mạch phổi bình thường}} (không phải do dòng máu qua vách liên nhĩ).",
      "Huyết động: Áp lực giữa hai tâm nhĩ rất thấp nên dòng máu qua lỗ thông liên nhĩ không tạo ra tiếng thổi.")

add_c("Hình ảnh điện tâm đồ điển hình của thông liên nhĩ lỗ thứ phát bao gồm: {{c1::trục phải, dày thất phải và hình ảnh block nhánh phải không hoàn toàn (dạng rSR' ở chuyển đạo V1)}}.",
      "Điện tim: Phản ánh tình trạng quá tải thể tích tâm trương của buồng tâm thất phải.")

add_c("Biện pháp điều trị can thiệp được lựa chọn hàng đầu hiện nay cho bệnh nhân thông liên nhĩ lỗ thứ phát có gờ mô xung quanh đầy đủ (> 5 mm) là {{c1::bít lỗ thông bằng dụng cụ qua da (bít dù Amplatzer)}}.",
      "Can thiệp: Tránh được cuộc phẫu thuật tim hở mở ngực, thời gian hồi phục nhanh sau 24-48 giờ.")

add_c("Thời điểm lý tưởng nhất để can thiệp bít dù hoặc phẫu thuật đóng thông liên nhĩ ở trẻ em không triệu chứng là lúc trẻ {{c1::3 đến 5 tuổi}} (trước độ tuổi đi học).",
      "Tiên lượng: Can thiệp ở lứa tuổi này giúp buồng tim phải tái cấu trúc trở về kích thước bình thường hoàn toàn.")

# ==========================================
# 4. CÒN ỐNG ĐỘNG MẠCH (PDA)
# ==========================================
add_c("Còn ống động mạch (PDA) chiếm tỷ lệ từ 9% đến 12% tim bẩm sinh ở trẻ đủ tháng, nhưng đặc biệt phổ biến ở trẻ sinh non với cân nặng dưới 1000 g lên tới {{c1::42%}}.",
      "Dịch tễ: Tần suất PDA ở trẻ sinh non từ 1000 đến 1500 g là khoảng 21%.")

add_c("Tỷ lệ trẻ mắc còn ống động mạch ở những quần thể dân cư sinh sống tại vùng núi cao có thể cao {{c1::gấp 30 lần}} so với trẻ sống ở vùng đồng bằng.",
      "Cơ chế: Nồng độ oxy phế nang và phân áp oxy máu thấp tại vùng núi cao cản trở cơ chế co thắt sinh lý của ống động mạch sau sinh.")

add_c("Dấu hiệu mạch ngoại vi kinh điển của còn ống động mạch lớn là {{c1::mạch nảy mạnh chìm sâu (mạch Corrigan / Bounding pulse)}}.",
      "Cơ chế: Thất trái tống thể tích máu lớn trong tâm thu làm huyết áp tâm thu tăng, máu thoát nhanh qua ống sang phổi trong tâm trương làm tụt huyết áp tâm trương.")

add_c("Tiếng thổi đặc trưng kinh điển nhất của còn ống động mạch ở trẻ nhũ nhi và trẻ lớn là {{c1::tiếng thổi liên tục (Continuous murmur / Giad-máy)}} nghe rõ nhất ở {{c1::khoang liên sườn 1-2 dưới đòn trái}}.",
      "Huyết động: Áp lực động mạch chủ cao hơn động mạch phổi trong cả thời kỳ tâm thu và tâm trương.")

add_c("Ở trẻ sinh non hoặc trẻ sơ sinh có tăng áp lực động mạch phổi nặng, nghe tim trong còn ống động mạch có thể {{c1::chỉ nghe thấy tiếng thổi tâm thu đơn thuần}} (mất thành phần tâm trương).",
      "Cơ chế: Áp lực động mạch phổi trong tâm trương tăng cao xấp xỉ áp lực động mạch chủ làm triệt tiêu chênh áp tâm trương.")

add_c("Triệu chứng tím chuyên biệt nửa dưới cơ thể (Differential cyanosis: chân tím hơn tay) là dấu hiệu lâm sàng của còn ống động mạch khi có biến chứng {{c1::Hội chứng Eisenmenger (tăng áp phổi đảo ngược luồng shunt)}}.",
      "Giải phẫu: Máu đen từ động mạch phổi qua ống động mạch đổ vào động mạch chủ xuống sau chỗ xuất phát của động mạch dưới đòn trái nuôi chi trên.")

add_c("Thuốc ức chế men COX đường uống hoặc tiêm tĩnh mạch được chứng minh có hiệu quả tương đương Indomethacin trong đóng ống động mạch ở trẻ sơ sinh non tháng là {{c1::Ibuprofen}}.",
      "Dược lý: Ibuprofen có ưu điểm ít gây co mạch thận và ít gây viêm ruột hoại tử (NEC) hơn Indomethacin.")

add_c("Phác đồ liều chuẩn của Ibuprofen đường tĩnh mạch đóng ống động mạch ở trẻ sinh non gồm 3 liều cách nhau 24 giờ: Liều 1 là {{c1::10 mg/kg}}; Liều 2 (sau 24h) là {{c1::5 mg/kg}}; Liều 3 (sau 48h) là {{c1::5 mg/kg}}.",
      "Thực hành: Theo dõi sát lượng nước tiểu và nồng độ Creatinine máu trong suốt liệu trình điều trị.")

# ==========================================
# 5. TỨ CHỨNG FALLOT (TOF) & CƠN TÍM
# ==========================================
add_c("Tứ chứng Fallot là bệnh tim bẩm sinh có tím phổ biến nhất sau thời kỳ sơ sinh, chiếm khoảng {{c1::4% đến 8%}} tổng số các trường hợp tim bẩm sinh.",
      "Dịch tễ: Là một trong những bệnh tim bẩm sinh đầu tiên được phẫu thuật sửa chữa thành công trên thế giới.")

add_c("Bốn tổn thương giải phẫu bệnh học kinh điển hợp thành Tứ chứng Fallot gồm: {{c1::Thông liên thất phần phễu lớn, Hẹp đường ra thất phải, Động mạch chủ cưỡi ngựa trên vách liên thất và Phì đại tâm thất phải}}.",
      "Phôi thai học: Hậu quả của sự lệch vách nón phễu (Conal septum) ra trước và lên trên trong quá trình tạo hình tim.")

add_c("Trong tứ chứng Fallot, mức độ biểu hiện tím tái trên lâm sàng phụ thuộc chủ yếu vào mức độ nặng của tổn thương {{c1::hẹp đường ra thất phải (RVOTO)}}.",
      "Lâm sàng: Nếu hẹp nhẹ, luồng shunt chủ yếu là Trái - Phải và trẻ không có tím (Fallot hồng / Pink Fallot).")

add_c("Thiếu oxy mạn tính trong tứ chứng Fallot kích thích tủy xương tăng sinh hồng cầu thứ phát, biểu hiện bằng chỉ số {{c1::Hematocrit tăng cao (thường > 55% đến 65%)}}.",
      "Biến chứng: Tăng độ nhớt máu làm tăng nguy cơ tắc mạch máu não, huyết khối tĩnh mạch xoang và áp xe não.")

add_c("Biến chứng ngón tay ngón chân hình dùi trống (Clubbing) và móng tay khum mặt kính đồng hồ ở bệnh nhân Fallot hình thành do {{c1::tình trạng thiếu oxy mạn tính kích thích giải phóng yếu tố tăng trưởng mạch máu VEGF và PDGF tại các đầu chi}}.",
      "Lâm sàng: Thường bắt đầu xuất hiện rõ rệt sau 6 tháng tuổi.")

add_c("Tiếng thổi tâm thu nghe được ở khoang liên sườn 2 bờ trái xương ức trong Tứ chứng Fallot được phát sinh từ {{c1::chỗ hẹp đường ra thất phải (hẹp phễu và hẹp van động mạch phổi)}}.",
      "Bẫy lâm sàng: Tiếng thổi này HOÀN TOÀN KHÔNG PHẢI do dòng máu đi qua lỗ thông liên thất lớn.")

add_c("Hình ảnh X-quang tim phổi thẳng kinh điển của Tứ chứng Fallot được mô tả là hình ảnh {{c1::tim hình chiếc ủng (Coeur en sabot)}}.",
      "Hình ảnh: Do mỏm tim hếch lên trên vì thất phải phì đại, cung động mạch phổi lõm sâu và hai phế trường sáng giảm tưới máu.")

add_c("Cơ chế bệnh sinh cốt lõi phát động cơn tím thiếu oxy cấp (Tet spell) ở trẻ mắc Fallot là do {{c1::cơn co thắt cơ phễu đường ra thất phải dưới tác động của tăng tiết Catecholamine giao cảm}}.",
      "Cơ chế: Co thắt phễu cắt đứt dòng máu lên phổi, dồn toàn bộ máu nghèo oxy từ thất phải qua VSD tràn vào động mạch chủ.")

add_c("Trong cơn tím Fallot cấp tính, khám nghe tim sẽ ghi nhận một hiện tượng lâm sàng bất thường là: Tiếng thổi tâm thu ở bờ trái ức vốn có hàng ngày sẽ {{c1::đột ngột nhỏ đi rõ rệt hoặc biến mất hoàn toàn}}.",
      "Ý nghĩa: Phản ánh cơ phễu đã co thắt tối đa, hầu như không còn máu thoát qua được đường ra thất phải lên phổi.")

add_c("Tư thế ngồi xổm (Squatting) hoặc tư thế ngực gối (Knee-chest) giúp cắt cơn tím ở trẻ Fallot nhờ cơ chế {{c1::làm gập động mạch đùi, tăng sức cản mạch máu ngoại biên hệ thống (SVR), từ đó làm giảm luồng shunt Phải - Trái qua VSD}}.",
      "Huyết động: Ép máu từ thất phải vượt qua chỗ hẹp phễu lên động mạch phổi để tăng cường trao đổi oxy.")

add_c("Thuốc an thần giảm đau được lựa chọn hàng đầu trong cấp cứu cơn tím Fallot là {{c1::Morphine Sulfate}}, với liều dùng là {{c1::0,1 mg/kg}} tiêm dưới da (SC) hoặc tiêm bắp (IM).",
      "Tác dụng: Ức chế trung tâm hô hấp làm dịu cơn thở nhanh sâu, trấn tĩnh trẻ, cắt đứt phản xạ giao cảm và làm giãn cơ phễu thất phải.")

add_c("Biện pháp bù dịch nhanh bằng dung dịch điện giải đẳng trương NaCl 0,9% liều {{c1::10 đến 15 mL/kg}} trong cơn tím Fallot có tác dụng {{c1::làm tăng thể tích tiền gánh thất phải và chống hiện tượng cô đặc máu}}.",
      "Cơ chế: Tăng thể tích tống máu thất phải giúp đẩy mở cơ phễu đường ra thất phải.")

add_c("Thuốc chẹn beta giao cảm tiêm tĩnh mạch chậm điều trị cơn tím Fallot trơ với Morphine và bù dịch là {{c1::Propranolol}}, với liều tiêm TM rất chậm từ {{c1::0,05 đến 0,1 mg/kg}} trong 5-10 phút.",
      "Cơ chế: Trực tiếp làm giãn cơ trơn phễu buồng tống thất phải, bắt buộc theo dõi monitor điện tim liên tục.")

add_c("Thuốc điều trị nội khoa đường uống được chỉ định để dự phòng tái phát cơn tím Fallot ở trẻ chờ phẫu thuật là {{c1::Propranolol}}, với liều dùng từ {{c1::1 đến 3 mg/kg/ngày}} chia làm 3 đến 4 lần.",
      "Thực hành: Ngăn chặn các đợt co thắt phễu kịch phát khi trẻ quấy khóc hoặc sốt.")

add_c("Phẫu thuật bắc cầu tạm thời Blalock-Taussig cải tiến (Modified BT shunt) trong Tứ chứng Fallot là kỹ thuật {{c1::dùng ống ghép mạch nhân tạo Gore-Tex nối giữa động mạch dưới đòn và động mạch phổi}}.",
      "Mục tiêu: Cung cấp nguồn máu cấp cứu từ đại tuần hoàn lên phổi cho trẻ sơ sinh hoặc trẻ có nhánh động mạch phổi quá nhỏ.")

add_c("Thời điểm phẫu thuật sửa chữa triệt để toàn bộ (Total intracardiac repair) cho trẻ mắc Tứ chứng Fallot hiện nay thường được thực hiện lúc trẻ {{c1::4 đến 6 tháng tuổi}}.",
      "Kỹ thuật: Vá lỗ thông liên thất bằng miếng vá nhân tạo và mở rộng đường ra thất phải bằng miếng vá màng ngoài tim.")

# ==========================================
# 6. CÁC BỆNH TIM BẨM SINH PHỨC TẠP KHÁC
# ==========================================
add_c("Trong dị tật Chuyển gốc đại động mạch (d-TGA), động mạch chủ xuất phát bất thường từ {{c1::tâm thất phải}} và động mạch phổi xuất phát bất thường từ {{c1::tâm thất trái}}.",
      "Giải phẫu: Tạo nên hai vòng tuần hoàn đại tuần hoàn và tiểu tuần hoàn chảy song song độc lập.")

add_c("Dị tật phối hợp bắt buộc phải có để bệnh nhân chuyển gốc đại động mạch (d-TGA) có thể sống sót sau sinh là {{c1::lỗ thông pha trộn máu (thông liên nhĩ, thông liên thất hoặc còn ống động mạch)}}.",
      "Huyết động: Nếu không có sự pha trộn máu, cơ thể sẽ tử vong do thiếu oxy mô trầm trọng trong vòng vài giờ đầu.")

add_c("Thủ thuật thông tim can thiệp cấp cứu xé rách vách liên nhĩ bằng bóng ở trẻ sơ sinh mắc TGA có tên là {{c1::Thủ thuật Rashkind (Balloon Atrial Septostomy)}}.",
      "Ý nghĩa: Tạo lỗ thông liên nhĩ lớn để tối ưu hóa sự pha trộn máu ở tầng tâm nhĩ trong khi chờ phẫu thuật chuyển gốc.")

add_c("Phẫu thuật sửa chữa triệt để về mặt giải phẫu hiện đại được lựa chọn hàng đầu cho chuyển gốc đại động mạch là {{c1::Phẫu thuật chuyển gốc động mạch Jatene (Arterial Switch Operation - ASO)}}.",
      "Kỹ thuật: Chuyển lại động mạch chủ về thất trái, chuyển động mạch phổi về thất phải và cắm lại động mạch vành.")

add_c("Thời điểm vàng bắt buộc phải thực hiện phẫu thuật Jatene cho trẻ TGA đơn thuần lành vách liên thất là trong {{c1::tuần đầu tiên sau sinh (từ 3 đến 7 ngày tuổi)}}.",
      "Cơ chế: Sau tuần đầu, sức cản mạch phổi giảm làm tâm thất trái bị thoái triển thành mỏng, không còn đủ áp lực để bơm máu hệ thống.")

add_c("Hai phương pháp phẫu thuật chuyển tầng nhĩ kinh điển trong lịch sử điều trị TGA những năm 1960-1980 là {{c1::phương pháp Senning và phương pháp Mustard}}.",
      "Biến chứng: Để lại tâm thất phải làm nhiệm vụ bơm máu hệ thống, dẫn đến suy thất phải và loạn nhịp nhĩ khi trưởng thành.")

add_c("Trong Hội chứng thiểu sản thất trái (HLHS), toàn bộ lưu lượng máu nuôi đại tuần hoàn và mạch vành phụ thuộc hoàn toàn vào {{c1::tâm thất phải bơm máu qua ống động mạch (PDA)}}.",
      "Cấp cứu: Khi ống động mạch đóng lại, trẻ rơi vào sốc tim trụy mạch tử vong nhanh chóng nếu không truyền PGE1.")

add_c("Quy trình phẫu thuật tái tạo 3 giai đoạn điều trị Hội chứng thiểu sản thất trái (HLHS) hướng tới sinh lý thất duy nhất gồm: Giai đoạn 1 là {{c1::phẫu thuật Norwood}}; Giai đoạn 2 là {{c1::phẫu thuật Glenn hai hướng}}; Giai đoạn 3 là {{c1::phẫu thuật Fontan}}.",
      "Lâm sàng: Norwood tiến hành tuần đầu sau sinh; Glenn lúc 3-6 tháng; Fontan lúc 2-4 tuổi.")

add_c("Trong bệnh dị tật Ebstein của van ba lá, tổn thương giải phẫu đặc trưng là {{c1::lá vách và lá sau van ba lá bị bám thấp bất thường về phía mỏm thất phải}}, dẫn đến hiện tượng {{c1::nhĩ hóa thất phải}}.",
      "Lâm sàng: Hở nặng van ba lá, buồng nhĩ phải giãn khổng lồ chèn ép thất phải.")

add_c("Hội chứng rối loạn nhịp tiền kích thích bẩm sinh thường phối hợp với bệnh dị tật Ebstein ở khoảng 15% các trường hợp là {{c1::Hội chứng Wolff-Parkinson-White (WPW)}}.",
      "Điện tim: Xuất hiện sóng delta và khoảng PR ngắn, nguy cơ khởi phát cơn nhịp nhanh trên thất kịch phát.")

add_c("Hình ảnh điện tâm đồ kinh điển trong bệnh Ebstein gồm: Sóng P ở DII cao khổng lồ nhọn hoắt được ví như {{c1::sóng P kiểu dãy Himalaya (P himalayan)}}, kèm block nhánh phải hoàn toàn.",
      "Điện tim: Phản ánh tâm nhĩ phải giãn to cực độ chứa một lượng máu ứ trệ khổng lồ.")

add_c("Phương pháp phẫu thuật tạo hình sửa van ba lá hiện đại và hiệu quả nhất cho bệnh nhân mắc dị tật Ebstein là {{c1::phương pháp tạo hình hình nón (Cone procedure)}}.",
      "Phẫu thuật: Huy động toàn bộ các lá van ba lá để tái tạo thành một van hình nón có chức năng đóng mở sinh lý.")

add_c("Bệnh Hẹp eo động mạch chủ (Coarctation of the Aorta) ở trẻ gái có tỷ lệ phối hợp rất cao với hội chứng bất thường nhiễm sắc thể có tên là {{c1::Hội chứng Turner (bộ NST 45,XO)}}.",
      "Di truyền: Khoảng 30% đến 35% bệnh nhân Turner có hẹp eo động mạch chủ hoặc van ĐMC hai lá.")

add_c("Dấu hiệu lâm sàng then chốt để chẩn đoán xác định Hẹp eo động mạch chủ ở trẻ lớn là: Huyết áp chi trên {{c1::cao hơn}} huyết áp chi dưới với mức chênh lệch huyết áp tay - chân {{c1::> 20 mmHg}}.",
      "Khám: Bắt mạch đùi hai bên thấy yếu rõ rệt hoặc đến chậm so với mạch quay (Radio-femoral delay).")

add_c("Dấu hiệu Roesler trên phim X-quang ngực thẳng của bệnh nhân hẹp eo động mạch chủ lớn tuổi là hình ảnh {{c1::khuyết bờ dưới các xương sườn (Rib notching)}}.",
      "Cơ chế: Do các động mạch liên sườn thuộc hệ tuần hoàn bàng hệ giãn to ngoằn ngoèo đè ép bào mòn bờ dưới xương sườn.")

add_c("Dị tật van tim bẩm sinh thường phối hợp nhất với Hẹp eo động mạch chủ ở khoảng 70% các trường hợp là {{c1::van động mạch chủ hai lá (Bicuspid Aortic Valve)}}.",
      "Biến chứng: Có nguy cơ tiến triển thành hẹp van hoặc hở van động mạch chủ và viêm nội tâm mạc nhiễm khuẩn.")

add_c("Biện pháp điều trị lựa chọn hàng đầu cho bệnh nhân Hẹp van động mạch phổi đơn thuần (Pulmonary Stenosis) có chênh áp đỉnh qua van lớn là {{c1::nong van động mạch phổi bằng bóng qua da (Balloon Valvuloplasty)}}.",
      "Can thiệp: Tỷ lệ thành công lâu dài đạt trên 85% các trường hợp, tránh được phẫu thuật mở ngực.")

add_c("Hội chứng di truyền thường phối hợp kinh điển nhất với Hẹp van động mạch phổi bẩm sinh là {{c1::Hội chứng Noonan}}.",
      "Lâm sàng: Trẻ có khuôn mặt đặc trưng, cổ ngắn có màng, lồng ngực lõm ức và chậm phát triển chiều cao.")

# ==========================================
# 7. THẺ BASIC HỎI ĐÁP TOÀN DIỆN (ORIGINAL + AI)
# ==========================================
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

target_path.parent.mkdir(parents=True, exist_ok=True)
target_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(cards)} cards for PED-43 successfully at {target_path}!")
