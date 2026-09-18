import json
from pathlib import Path

cards_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_2026-09-19_RELEASE_v1.cards.v2.json")
cards = json.loads(cards_path.read_text(encoding="utf-8"))

def add_c(text, extra=""):
    cards.append({"type": "cloze", "text": text, "extra": extra})

# Additional 80 atomic cards
add_c("Chỉ định phẫu thuật đóng thông liên thất (VSD) dựa trên tỷ số lưu lượng máu phổi trên lưu lượng máu hệ thống (Qp/Qs) khi tỷ số này đạt từ {{c1::Qp/Qs ≥ 1,5:1}} trở lên.",
      "Huyết động: Phản ánh luồng shunt Trái - Phải có ý nghĩa huyết động gây quá tải thể tích thất trái.")

add_c("Trong thông liên thất phần phễu (dưới van), biến chứng hở van động mạch chủ tiến triển xảy ra do lá van {{c1::động mạch chủ bên phải}} bị hút sa vào lỗ thông liên thất.",
      "Cơ chế: Hiệu ứng Venturi tạo áp lực âm kéo tụt lá van phải vào buồng thất phải.")

add_c("Khác với thông liên thất phần màng và phần cơ, thông liên thất phần buồng nhận (Inlet VSD) có đặc tính là {{c1::không bao giờ tự đóng tự nhiên}}.",
      "Giải phẫu: Thuộc bệnh cảnh khuyết gối nội tâm mạc, liên quan chặt chẽ đến van nhĩ thất.")

add_c("Ở trẻ sơ sinh mắc thông liên thất lớn, tình trạng tăng áp lực động mạch phổi ác tính cố định (Eisenmenger) thường không xảy ra ngay lúc mới sinh mà phát triển dần sau {{c1::sau 1 đến 2 tuổi}}.",
      "Cơ chế: Cần thời gian để các mạch máu phổi phì đại lớp cơ trơn và xơ hóa nội mạc cố định.")

add_c("Hội chứng Eisenmenger là tình trạng {{c1::tăng áp lực mạch máu phổi cố định không hồi phục}}, làm áp lực buồng tim phải vượt buồng tim trái và đảo chiều luồng shunt thành {{c1::Phải - Trái}}.",
      "Chống chỉ định: Bệnh nhân mất chỉ định phẫu thuật sửa chữa tim hở hoàn toàn.")

add_c("Dị tật Thông sàn nhĩ thất (AVSD) hay kênh nhĩ thất đặc biệt phổ biến ở trẻ mắc hội chứng di truyền {{c1::Hội chứng Down (Trisomy 21)}} với tỷ lệ lên tới {{c1::40%}}.",
      "Di truyền: Chiếm khoảng 4% đến 5% tổng số các trường hợp tim bẩm sinh nói chung.")

add_c("Thông sàn nhĩ thất bán phần (Partial AVSD) bao gồm hai tổn thương giải phẫu cơ bản là: {{c1::thông liên nhĩ lỗ tiên phát (Ostium primum ASD) và chẻ lá trước van hai lá (Cleft mitral valve)}}.",
      "Lâm sàng: Gây luồng shunt ở tầng nhĩ và hở van hai lá bẩm sinh.")

add_c("Thời điểm vàng phẫu thuật sửa chữa triệt để cho trẻ mắc Thông sàn nhĩ thất hoàn toàn (Complete AVSD) là lúc trẻ {{c1::3 đến 6 tháng tuổi}}.",
      "Kỹ thuật: Phẫu thuật vá hai miếng (Two-patch technique) tái tạo vách liên nhĩ, vách liên thất và chia tách van nhĩ thất chung.")

add_c("Biến chứng muộn thường gặp nhất sau phẫu thuật sửa chữa thông sàn nhĩ thất đòi hỏi theo dõi suốt đời là {{c1::hở van hai lá tiến triển}} (gặp ở khoảng 15% bệnh nhân).",
      "Tiên lượng: Do cấu trúc giải phẫu của van hai lá bất thường bẩm sinh khó phục hồi sinh lý hoàn toàn.")

add_c("Ống động mạch ở trẻ đủ tháng khỏe mạnh thường bắt đầu co thắt chức năng trong vòng 10 đến 15 giờ đầu sau sinh và đóng kín về mặt giải phẫu sau {{c1::vài ngày đến 2 tuần đầu}}.",
      "Cơ chế: Nồng độ oxy máu tăng vọt sau sinh ức chế kênh kali và làm giảm nồng độ Prostaglandin E2 nội sinh.")

add_c("Tiếng thổi liên tục kinh điển trong còn ống động mạch (PDA) còn có tên gọi là tiếng thổi {{c1::Gibson}} (hoặc tiếng thổi giàn máy - Machinery murmur).",
      "Âm học: Cường độ tăng dần về cuối tâm thu, đạt đỉnh ở T2 và giảm dần trong tâm trương.")

add_c("Chênh lệch huyết áp (hiệu số huyết áp tâm thu trừ tâm trương) ở trẻ mắc còn ống động mạch lớn thường mở rộng vượt quá {{c1::> 30 đến 40 mmHg}}.",
      "Khám: Huyết áp tâm thu có thể bình thường nhưng huyết áp tâm trương tụt sâu xuống 20-30 mmHg.")

add_c("Bên cạnh Indomethacin và Ibuprofen, hoạt chất hạ sốt giảm đau thông thường {{c1::Paracetamol (Acetaminophen)}} đường uống hoặc truyền tĩnh mạch cũng được chứng minh có hiệu quả đóng ống động mạch ở trẻ sinh non.",
      "Chỉ định: Lựa chọn thay thế an toàn khi trẻ non tháng có giảm tiểu cầu nặng hoặc nguy cơ xuất huyết tiêu hóa.")

add_c("Hội chứng thanh gươm Thổ Nhĩ Kỳ (Scimitar syndrome) là một thể của bất thường hồi lưu tĩnh mạch phổi bán phần, trong đó tĩnh mạch phổi dưới phải đổ bất thường vào {{c1::tĩnh mạch chủ dưới (IVC)}}.",
      "Hình ảnh: Bóng tĩnh mạch phổi bất thường tạo hình ảnh dải mờ cong cong như thanh gươm Scimitar dọc bờ phải tim trên X-quang.")

add_c("Trong Tứ chứng Fallot, phì đại tâm thất phải là tổn thương {{c1::thứ phát}} hình thành do thất phải phải co bóp chống lại tình trạng hẹp đường ra thất phải.",
      "Cơ chế: Giúp tâm thất phải tạo áp lực tống máu tương đương áp lực thất trái.")

add_c("Thể lâm sàng Fallot hồng (Pink Fallot) xuất hiện khi mức độ hẹp đường ra thất phải còn nhẹ, áp lực thất phải thấp hơn thất trái nên luồng shunt qua VSD chủ yếu là {{c1::Trái - Phải (không gây tím)}}.",
      "Tiên lượng: Bệnh nhân có biểu hiện suy tim tăng lưu lượng phổi giống như thông liên thất lớn.")

add_c("Chỉ số Hematocrit ở trẻ Tứ chứng Fallot tím mạn tính tăng cao bù trừ trên {{c1::> 65%}} làm tăng vọt độ nhớt máu và đòi hỏi phải {{c1::bù dịch chống mất nước hoặc trích máu thay thế dịch đẳng trương}}.",
      "Cảnh báo: Nguy cơ huyết khối tắc mạch não và đột quỵ nhồi máu não.")

add_c("Biến chứng nhiễm trùng thần kinh nguy hiểm thường gặp ở trẻ lớn mắc Tứ chứng Fallot có tím mạn tính là {{c1::áp xe não (Brain Abscess)}}.",
      "Cơ chế: Máu tĩnh mạch hệ thống không qua hệ thống lọc mao mạch phổi nên vi khuẩn xâm nhập thẳng vào tuần hoàn động mạch não.")

add_c("Thuốc chẹn beta Propranolol giúp cắt cơn tím Fallot nhờ tác dụng {{c1::ức chế thụ thể beta-1 adrenergic, làm giãn cơ trơn phễu đường ra thất phải}}.",
      "Dược lý: Cắt đứt tác động co thắt phễu của nồng độ Catecholamine tăng vọt.")

add_c("Phác đồ liều của thuốc Morphin Sulfate tiêm dưới da hoặc tiêm bắp trong cấp cứu cơn tím Fallot là {{c1::0,1 mg/kg}}.",
      "Cấp cứu: Có thể nhắc lại sau 15 đến 30 phút nếu cơn tím chưa dứt hoàn toàn.")

add_c("Cầu nối Blalock-Taussig cải tiến (mBT shunt) dùng đoạn mạch nhân tạo Gore-Tex nối giữa {{c1::động mạch dưới đòn}} và {{c1::nhánh động mạch phổi cùng bên}}.",
      "Phẫu thuật: Cung cấp dòng máu có áp lực từ đại tuần hoàn lên phổi giúp các nhánh động mạch phổi phát triển.")

add_c("Dị tật Teo van động mạch phổi kèm thông liên thất (PA-VSD) được coi là thể giải phẫu nặng nề nhất của quang phổ bệnh lý {{c1::Tứ chứng Fallot}}.",
      "Huyết động: Máu lên phổi hoàn toàn phụ thuộc vào ống động mạch hoặc tuần hoàn bàng hệ chủ - phổi (MAPCAs).")

add_c("Thuốc duy trì mở ống động mạch cứu mạng ở trẻ sơ sinh mắc bệnh tim phụ thuộc ống động mạch là {{c1::Prostaglandin E1 (Alprostadil / PGE1)}} với liều truyền tĩnh mạch từ {{c1::0,01 đến 0,05 µg/kg/phút}}.",
      "Tác dụng phụ: Có thể gây cơn ngừng thở (Apnea), sốt và tụt huyết áp; cần chuẩn bị sẵn bóng bóp và nội khí quản.")

add_c("Trong chuyển gốc đại động mạch (d-TGA), nghiệm pháp thở oxy 100% (Hyperoxia test) có kết quả đặc trưng là: PaO2 máu động mạch {{c1::hầu như không tăng (vẫn < 100 - 150 mmHg)}}.",
      "Chẩn đoán: Khẳng định tím do tim có luồng shunt Phải - Trái chứ không phải suy hô hấp do bệnh nhu mô phổi.")

add_c("Thủ thuật xé vách liên nhĩ bằng bóng Rashkind đưa ống thông có bóng qua đường tĩnh mạch đùi hoặc tĩnh mạch rốn vào {{c1::tâm nhĩ trái}}, bơm căng bóng rồi giật mạnh về {{c1::tâm nhĩ phải}}.",
      "Huyết động: Xé rách van lỗ bầu dục tạo lỗ thông liên nhĩ lớn cho phép máu giàu oxy sang tuần hoàn hệ thống.")

add_c("Phẫu thuật chuyển gốc động mạch Jatene bao gồm các thì phẫu thuật chính: Cắt rời đại động mạch, chuyển ĐMC về thất trái, chuyển ĐMP về thất phải, {{c1::cắm lại cuống động mạch vành}} và làm nghiệm pháp Lecompte.",
      "Kỹ thuật: Phức tạp nhất là thì chuyển gốc hai động mạch vành mà không làm xoắn vặn hay tắc hẹp lòng mạch.")

add_c("Hội chứng DiGeorge (mất đoạn nhiễm sắc thể 22q11.2) có liên quan di truyền rất chặt chẽ với dị tật tim bẩm sinh {{c1::Thân chung động mạch (Truncus Arteriosus)}} và đứt đoạn quai động mạch chủ.",
      "Di truyền: Kèm theo thiểu sản tuyến ức suy giảm miễn dịch và hạ canxi máu do suy tuyến cận giáp.")

add_c("Trong bệnh Thân chung động mạch (Truncus Arteriosus), phẫu thuật triệt để phải được tiến hành sớm trước {{c1::2 đến 3 tháng tuổi}} để tránh bệnh lý tắc nghẽn mạch máu phổi cố định.",
      "Kỹ thuật: Phẫu thuật đóng VSD và đặt ống ghép có van (Conduit) nối từ thất phải lên động mạch phổi.")

add_c("Hiện tượng 'nhĩ hóa thất phải' trong bệnh Ebstein có nghĩa là {{c1::một phần buồng tâm thất phải phía trên chỗ bám bất thường của van ba lá bị sáp nhập vào buồng tâm nhĩ phải}}.",
      "Giải phẫu: Khiến phần buồng thất phải chức năng co bóp tống máu còn lại bị teo nhỏ và giảm động.")

add_c("Trên phim X-quang tim phổi thẳng của bệnh nhân Ebstein nặng, bóng tim phải giãn to khổng lồ chiếm gần hết lồng ngực được ví như hình ảnh {{c1::quả bóng bàn (hoặc hình bình nước)}}.",
      "Hình ảnh: Hai phế trường phổi sáng do lượng máu lên phổi bị sụt giảm nghiêm trọng.")

add_c("Bất thường hồi lưu tĩnh mạch phổi hoàn toàn (TAPVC) thể dưới tim (Infracardiac type) thường xuyên bị biến chứng {{c1::tắc nghẽn đường về tĩnh mạch phổi}}, gây phù phổi cấp dữ dội ở trẻ sơ sinh.",
      "Cấp cứu: Đòi hỏi phải phẫu thuật cấp cứu khẩn cấp trong vòng 24 giờ đầu, tỷ lệ tử vong lên tới 40% nếu chậm trễ.")

add_c("Hình ảnh X-quang tim phổi kinh điển của TAPVC thể trên tim (đổ vào tĩnh mạch vô danh) được gọi là dấu hiệu {{c1::hình người tuyết (Snowman sign) hoặc hình số 8}}.",
      "Hình ảnh: Nửa trên số 8 tạo bởi tĩnh mạch dọc bất thường, tĩnh mạch vô danh và TMC trên giãn lớn; nửa dưới là bóng tim.")

add_c("Trong Teo van ba lá (Tricuspid Atresia), máu từ nhĩ phải muốn sang tuần hoàn đại thể bắt buộc phải qua {{c1::lỗ bầu dục hoặc lỗ thông liên nhĩ (ASD)}} để sang tâm nhĩ trái.",
      "Huyết động: Toàn bộ máu trở về tim trái, thất trái giãn lớn và đảm đương chức năng bơm máu duy nhất.")

add_c("Dấu hiệu điện tâm đồ đặc biệt nhất của Teo van ba lá giúp phân biệt với hầu hết các bệnh tim bẩm sinh có tím khác là {{c1::trục điện tim chuyển trái (Left Axis Deviation) và dày thất trái}}.",
      "Điện tim: Phần lớn tim bẩm sinh có tím là trục phải và dày thất phải, riêng Teo van ba lá là trục trái.")

add_c("Phẫu thuật Glenn hai hướng (Bidirectional Glenn) trong quy trình Fontan là phẫu thuật nối trực tiếp {{c1::tĩnh mạch chủ trên (SVC)}} vào {{c1::động mạch phổi phải}}.",
      "Huyết động: Đưa máu nửa trên cơ thể về phổi thụ động không cần qua tâm thất, thực hiện lúc 3 đến 6 tháng tuổi.")

add_c("Phẫu thuật Fontan hoàn tất là kỹ thuật nối trực tiếp {{c1::tĩnh mạch chủ dưới (IVC)}} vào {{c1::động mạch phổi}} thông qua ống ghép nhân tạo ngoài tim (Extracardiac conduit).",
      "Huyết động: Tách rời hoàn toàn máu tĩnh mạch hệ thống không qua tim, đưa tâm thất duy nhất làm nhiệm vụ bơm máu động mạch chủ.")

add_c("Trong Hẹp eo động mạch chủ (CoA), vị trí chỗ hẹp giải phẫu thường nằm ở {{c1::ngay đối diện hoặc dưới chỗ xuất phát của động mạch dưới đòn trái (vùng eo động mạch chủ)}}.",
      "Giải phẫu: Tương ứng với vị trí bám của dây chằng động mạch.")

add_c("Dấu hiệu mạch kinh điển trong Hẹp eo động mạch chủ là hiện tượng {{c1::mạch bẹn / mạch đùi bắt yếu hoặc đến chậm so với mạch quay (Radio-femoral delay)}}.",
      "Lâm sàng: Do sóng mạch đi qua chỗ hẹp bị cản trở và giảm vận tốc truyền âm.")

add_c("Hình ảnh 'dấu hiệu số 3' (Figure-of-3 sign) trên phim X-quang ngực thẳng của bệnh nhân hẹp eo ĐMC hình thành do {{c1::giãn quai ĐMC trước chỗ hẹp, lõm tại chỗ hẹp eo và giãn phình ĐMC xuống sau chỗ hẹp}}.",
      "Hình ảnh: Dấu hiệu hình ảnh gián tiếp đặc thù của hẹp eo động mạch chủ.")

add_c("Hẹp van động mạch chủ bẩm sinh nguy kịch ở trẻ sơ sinh (Critical AS) gây sốc tim suy thất trái nặng nề, biện pháp can thiệp cấp cứu đầu tay là {{c1::nong van động mạch chủ bằng bóng qua da}}.",
      "Can thiệp: Giúp giải áp khẩn cấp buồng thất trái trước khi xem xét phẫu thuật Ross hoặc sửa van.")

add_c("Phẫu thuật Ross trong điều trị bệnh lý van động mạch chủ nặng ở trẻ em là kỹ thuật lấy {{c1::van động mạch phổi tự thân}} chuyển sang thay thế van động mạch chủ, và đặt ống ghép có van vào đường ra thất phải.",
      "Ưu điểm: Van động mạch phổi tự thân có khả năng tăng trưởng kích thước theo sự lớn lên của đứa trẻ.")

add_c("Hội chứng Williams (Williams-Beuren syndrome) do mất đoạn gen Elastin trên nhiễm sắc thể 7q11.23 thường phối hợp với dị tật tim mạch đặc trưng là {{c1::hẹp trên van động mạch chủ (Supravalvular Aortic Stenosis)}}.",
      "Lâm sàng: Trẻ có khuôn mặt giống chú lùn (Elfin face), tính cách cởi mở quá mức và tăng canxi máu thời thơ ấu.")

add_c("Tiếng click tống máu (Ejection click) trong Hẹp van động mạch phổi có đặc điểm điện thính học đặc biệt là {{c1::nhỏ đi hoặc biến mất trong thì hít vào sâu}}.",
      "Cơ chế: Hít vào làm tăng hồi lưu máu về thất phải làm căng sớm lá van phổi trước khi thất co bóp.")

add_c("Trong Hẹp van động mạch phổi nặng, nghe tim thấy thành phần van phổi P2 của tiếng tim thứ hai có đặc điểm là {{c1::mờ nhạt hoặc biến mất hoàn toàn}}.",
      "Lâm sàng: Tiếng T2 tách đôi rất rộng với thành phần A2 đơn độc.")

add_c("Chế độ kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn đường uống tiêu chuẩn trước thủ thuật răng miệng là {{c1::Amoxicillin liều 50 mg/kg (tối đa 2 g)}} uống một liều duy nhất trước thủ thuật {{c1::30 đến 60 phút}}.",
      "Dược lý: Nếu dị ứng Penicillin chuyển sang Clindamycin 20 mg/kg hoặc Azithromycin 15 mg/kg.")

add_c("Bệnh tim bẩm sinh tím có luồng shunt Phải - Trái làm mất chức năng của màng mao mạch phổi đóng vai trò là {{c1::bộ lọc cơ học vi khuẩn và cục máu đông}} của cơ thể.",
      "Cơ chế: Giải thích tại sao trẻ tim bẩm sinh tím có nguy cơ cao bị áp xe não và nhồi máu não nghịch thường.")

add_c("Trong cấp cứu cơn tím Fallot, tiêm Natri Bicarbonat (NaHCO3) liều 1 đến 2 mEq/kg được chỉ định khi bệnh nhi có tình trạng {{c1::toan chuyển hóa nặng}}.",
      "Cơ chế: Toan chuyển hóa kích thích trung tâm hô hấp làm thở nhanh sâu và làm tăng sức cản mạch phổi, đẩy mạnh luồng shunt Phải - Trái.")

add_c("Để tránh nhầm lẫn tiếng thổi tâm thu của thông liên thất với tiếng thổi của hở hai lá cơ năng ở mỏm tim, cần nhớ tiếng thổi của VSD nghe rõ nhất ở {{c1::khoang liên sườn 3-4 bờ trái xương ức}} và lan {{c1::hình nan quạt quanh ngực}}.",
      "Khám: Tiếng thổi hở hai lá nghe rõ ở mỏm tim và lan ra hố nách trái.")

add_c("Dấu hiệu nhận biết trẻ sơ sinh tím tái do nguyên nhân tim bẩm sinh so với tím do hạ thân nhiệt là: Tím do tim xuất hiện ở cả {{c1::niêm mạc miệng, lưỡi và kết mạc mắt}} và {{c1::không biến mất sau khi sưởi ấm trẻ}}.",
      "Khám: Tím do lạnh chỉ xuất hiện ở đầu chi, niêm mạc lưỡi vẫn hồng hào.")

add_c("Ở trẻ nhũ nhi mắc thông liên thất lớn, việc theo dõi sát biểu hiện lâm sàng ăn bú và tăng cân có giá trị hơn nghe tim vì tiếng thổi tâm thu có thể {{c1::nhỏ đi khi áp lực động mạch phổi tăng cao gần bằng áp lực thất trái}}.",
      "Bẫy lâm sàng: Tiếng thổi nhỏ đi không có nghĩa là bệnh thuyên giảm mà có thể cảnh báo tăng áp phổi nặng.")

cards_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-43: {len(cards)} cards!")
