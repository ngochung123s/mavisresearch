import json
from pathlib import Path

cards_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_2026-09-19_RELEASE_v1.cards.v2.json")
cards = json.loads(cards_path.read_text(encoding="utf-8"))

def add_c(text, extra=""):
    cards.append({"type": "cloze", "text": text, "extra": extra})

add_c("Trong Thân chung động mạch (Truncus Arteriosus), phân loại Collett-Edwards chia thành 4 tuýp dựa vào {{c1::vị trí xuất phát của các nhánh động mạch phổi từ thân chung}}.",
      "Phân loại: Tuýp I thân ĐMP chung xuất phát từ thân chung; Tuýp II hai nhánh ĐMP xuất phát sát nhau ở mặt sau; Tuýp III xuất phát riêng rẽ hai bên.")

add_c("Trong bệnh dị tật Ebstein của van ba lá, lá van ba lá thường có kích thước rất lớn, di động dạng cánh buồm (Sail-like leaflet) và bám đúng vị trí vòng van là {{c1::lá van trước (Anterior leaflet)}}.",
      "Giải phẫu: Trong khi lá vách và lá sau bị bám thấp sâu về phía mỏm tim.")

add_c("Trong phẫu thuật Norwood điều trị HLHS giai đoạn 1, cải tiến Sano sử dụng một ống nối nhân tạo không van nối từ {{c1::tâm thất phải}} lên {{c1::thân động mạch phổi}} (thay thế cho cầu nối Blalock-Taussig).",
      "Kỹ thuật: Giúp duy trì huyết áp tâm trương tốt hơn và cải thiện tưới máu động mạch vành.")

add_c("Phẫu thuật Glenn hai hướng trong quy trình Fontan đưa dòng máu tĩnh mạch chủ trên về phổi thụ động, điều kiện tiên quyết là sức cản mạch máu phổi (PVR) phải thấp dưới {{c1::< 2 đến 3 đơn vị Wood}}.",
      "Huyết động: Tuần hoàn Fontan không có bơm thất phải nên lưu lượng máu qua phổi phụ thuộc hoàn toàn vào gradient áp lực tĩnh mạch.")

add_c("Cơ chế tăng huyết áp chi trên trong Hẹp eo động mạch chủ bao gồm hai cơ chế phối hợp: cản trở cơ học cơ học dòng máu và {{c1::thiếu máu tưới nuôi thận mạn tính kích hoạt hệ RAAS}}.",
      "Sinh lý: Giải thích tại sao một số bệnh nhân vẫn còn tăng huyết áp tồn dư sau khi đã phẫu thuật giải tỏa chỗ hẹp.")

add_c("Biến chứng tăng huyết áp tồn dư sau phẫu thuật hoặc can thiệp hẹp eo động mạch chủ xảy ra ở khoảng 20% đến 30% bệnh nhân do {{c1::rối loạn độ chun giãn mạch máu và thay đổi thụ cảm thể áp lực xoang cảnh}}.",
      "Theo dõi: Đòi hỏi bệnh nhân phải được theo dõi huyết áp định kỳ suốt đời.")

add_c("Mọi trẻ gái được chẩn đoán Hẹp eo động mạch chủ đều có chỉ định bắt buộc làm xét nghiệm di truyền {{c1::nhiễm sắc thể đồ (Karyotype)}} để tầm soát Hội chứng Turner.",
      "Di truyền: Ngược lại, mọi trẻ gái mắc Turner đều phải được siêu âm tim tầm soát hẹp eo ĐMC và van ĐMC hai lá.")

add_c("Hội chứng Williams (Williams-Beuren) do đột biến mất đoạn gen Elastin trên nhiễm sắc thể 7q11.23, có đặc điểm lâm sàng điển hình gồm khuôn mặt giống chú lùn, tính cách cởi mở và dị tật tim mạch {{c1::hẹp trên van động mạch chủ}}.",
      "Lâm sàng: Thường kèm tăng canxi máu thời kỳ nhũ nhi.")

add_c("Hội chứng Noonan do đột biến gen PTPN11 có biểu hiện lâm sàng gồm cổ ngắn có màng, lồng ngực lõm ức, chậm lớn và dị tật tim bẩm sinh thường gặp nhất là {{c1::hẹp van động mạch phổi}}.",
      "Lâm sàng: Thường kèm theo loạn sản các lá van động mạch phổi dày cộm.")

add_c("Hội chứng DiGeorge (mất đoạn 22q11.2) gây tam chứng kinh điển gồm: dị tật tim nón phễu (Thân chung ĐMC, đứt đoạn quai ĐMC), {{c1::hạ canxi máu sơ sinh do suy tuyến cận giáp}} và {{c1::suy giảm miễn dịch tế bào T do thiểu sản tuyến ức}}.",
      "Di truyền: Cần xét nghiệm lai huỳnh quang tại chỗ (FISH) để chẩn đoán xác định.")

add_c("Hình ảnh 'Người tuyết' (Snowman sign) trên X-quang ngực thẳng trong TAPVC thể trên tim được hình thành bởi: Đầu người tuyết tạo bởi {{c1::tĩnh mạch dọc bất thường, tĩnh mạch vô danh và tĩnh mạch chủ trên giãn to}}; Thân người tuyết là {{c1::bóng tim to}}.",
      "Hình ảnh: Dấu hiệu X-quang kinh điển phát hiện sau giai đoạn sơ sinh.")

add_c("Ở bệnh nhi mắc Teo van ba lá có lưu lượng máu lên phổi quá ít gây tím tái nặng, phẫu thuật tạm thời giai đoạn sơ sinh là {{c1::làm cầu nối Blalock-Taussig cải tiến (mBT shunt)}}.",
      "Phẫu thuật: Ngược lại, nếu lưu lượng máu lên phổi quá nhiều gây suy tim, phẫu thuật tạm thời là thắt hẹp động mạch phổi (PA banding).")

add_c("Tỷ lệ tự đóng tự nhiên của thông liên thất phần cơ nhỏ (Muscular VSD) ở trẻ em trước 2 tuổi có thể lên tới {{c1::trên 80%}}.",
      "Tiên lượng: Cơ tâm thất phì đại sinh lý ép bít các lỗ thông cơ bè nhỏ.")

add_c("Trong thông liên thất phần phễu (dưới van), định luật Bernoulli giải thích dòng máu phụt xoáy với vận tốc cao qua lỗ thông tạo nên {{c1::áp lực bên âm (áp lực hút)}} hút tụt lá van động mạch chủ.",
      "Vật lý: Đây là bản chất cơ học của hiệu ứng Venturi gây sa van và hở van động mạch chủ tiến triển.")

add_c("Tiếng thổi liên tục Gibson trong còn ống động mạch bắt đầu từ {{c1::đầu kỳ tâm thu}}, mạnh dần lên và đạt cường độ đỉnh ở {{c1::tiếng T2}}, sau đó giảm dần trong kỳ tâm trương.",
      "Âm học: Phản ánh chênh áp giữa động mạch chủ và động mạch phổi tồn tại liên tục trong suốt chu chuyển tim.")

add_c("Thuốc đóng ống động mạch (Ibuprofen, Indomethacin) hoàn toàn KHÔNG có tác dụng ở {{c1::trẻ sơ sinh đủ tháng}} mắc còn ống động mạch.",
      "Dược lý: Ống động mạch ở trẻ đủ tháng có cấu trúc mô học trưởng thành với nhiều sợi chun, cơ chế đóng ống không còn đáp ứng với ức chế men COX.")

add_c("Cơn tím thiếu oxy Fallot có đỉnh điểm xuất hiện phổ biến nhất trong độ tuổi từ {{c1::2 đến 4 tháng tuổi}} và thường hay xảy ra vào thời điểm {{c1::buổi sáng sớm sau khi ngủ dậy}}.",
      "Cơ chế: Do nồng độ Catecholamine nội sinh tăng cao theo nhịp sinh học buổi sáng kết hợp tình trạng thiếu nước tương đối sau giấc ngủ đêm.")

add_c("Động tác ép chặt hai đầu gối vào ngực trong tư thế ngực gối (Knee-chest) làm tăng sức cản mạch hệ thống SVR nhờ cơ chế {{c1::gập nếp gấp bẹn ép nghẽn cơ học động mạch đùi hai bên}}.",
      "Cơ chế: SVR tăng cao vượt áp lực thất phải, ép dòng máu đen qua chỗ hẹp phễu lên động mạch phổi để hấp thu oxy.")

add_c("Trong cấp cứu cơn tím Fallot, Morphin Sulfate phát huy tác dụng điều trị nhờ {{c1::ức chế trung tâm hô hấp làm dịu cơn thở nhanh sâu, giảm phản xạ giao cảm và cắt đứt cơn co thắt phễu thất phải}}.",
      "Dược lý: Cắt đứt vòng xoắn bệnh lý giữa lo âu - khóc thét - tăng giao cảm - co thắt phễu.")

add_c("Thuốc chẹn beta Propranolol tiêm tĩnh mạch trong cơn tím Fallot có tác dụng trực tiếp là {{c1::chẹn thụ thể beta-1 adrenergic làm giãn các dải cơ phễu buồng tống thất phải}}.",
      "Thực hành: Bắt buộc tiêm tĩnh mạch rất chậm trong 5 đến 10 phút dưới monitor theo dõi điện tim.")

add_c("Tiêm Natri Bicarbonat (NaHCO3) trong cơn tím Fallot nặng nhằm mục đích kiềm hóa máu, bởi vì tình trạng toan chuyển hóa là yếu tố gây {{c1::co thắt mạnh mạch máu phổi, làm tăng sức cản mạch phổi và đẩy mạnh luồng shunt Phải - Trái}}.",
      "Huyết động: Phục hồi pH máu giúp hạ sức cản mạch phổi, tạo thuận lợi cho máu lên phổi.")

add_c("Chỉ định dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn bắt buộc áp dụng trong vòng {{c1::6 tháng đầu sau phẫu thuật hoặc can thiệp}} đặt vật liệu nhân tạo trong tim.",
      "Khuyến cáo: Sau 6 tháng, lớp nội mạc mạch máu đã bao phủ hoàn toàn bề mặt vật liệu nhân tạo.")

add_c("Đối với bệnh nhân tim bẩm sinh có tím chưa được phẫu thuật sửa chữa triệt để, chỉ định dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn được áp dụng {{c1::suốt đời}}.",
      "Khuyến cáo: Luôn duy trì vệ sinh răng miệng tốt và uống Amoxicillin 50 mg/kg trước các thủ thuật răng miệng có chảy máu.")

add_c("Liều dùng kháng sinh dự phòng viêm nội tâm mạc nhiễm khuẩn đường uống bằng Amoxicillin ở trẻ em là {{c1::50 mg/kg}} (liều tối đa ở người lớn là {{c1::2 g}}), uống trước thủ thuật 30-60 phút.",
      "Dược lý: Nếu trẻ dị ứng với Penicillin, thuốc thay thế đường uống hàng đầu là Clindamycin liều 20 mg/kg.")

add_c("Một trẻ sơ sinh tím tái nặng có SpO2 65%, sau khi thở oxy 100% qua mask trong 15 phút SpO2 chỉ tăng lên 68% (nghiệm pháp thở oxy âm tính), khẳng định nguyên nhân tím là do {{c1::tim bẩm sinh có luồng shunt Phải - Trái}}.",
      "Chẩn đoán: Loại trừ các bệnh lý suy hô hấp do nhu mô phổi đơn thuần (vốn đáp ứng tăng PaO2 rõ rệt với oxy 100%).")

cards_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total cards for PED-43: {len(cards)} cards!")
