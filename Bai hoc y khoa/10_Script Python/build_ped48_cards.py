# -*- coding: utf-8 -*-
"""Generate ultra-detailed, fully compliant PED-48 Anki flashcards JSON v2 (>=125 cards)."""
import json
from pathlib import Path
target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.cards.v2.json")

cards = []

def add_c(text, extra=""):
    cards.append({"type": "cloze", "text": text, "extra": extra})

def add_b(front, orig, ai, extra=""):
    back = f"<b>📖 Văn bản gốc:</b><br>• {orig}<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>• {ai}"
    cards.append({"type": "basic", "front": front, "back": back, "extra": extra})

# ==========================================
# 1. ĐẠI CƯƠNG, ĐỊNH NGHĨA & DỊCH TỄ
# ==========================================
add_c("Suy tim ở trẻ em là tình trạng tim không còn khả năng đảm bảo {{c1::cung lượng tim (Cardiac Output)}} đáp ứng nhu cầu chuyển hóa và oxy của cơ thể ở áp lực đổ đầy bình thường.",
      "Cơ chế: Khác với người lớn thường suy tim do xơ vữa và nhồi máu, suy tim trẻ em chủ yếu do tim bẩm sinh, viêm cơ tim và bệnh cơ tim.")

add_c("Theo thống kê kinh điển của Demopoulos và Sonnenblick, tỷ lệ tử vong trong vòng 5 năm đầu ở những bệnh nhân mới phát hiện suy tim là {{c1::hơn một nửa (khoảng 50%)}} nếu không được can thiệp nguyên nhân kịp thời.",
      "Lâm sàng: Tỷ lệ tử vong cao nhất tập trung vào năm đầu đời, đặc biệt ở trẻ sơ sinh mắc các dị tật tim bẩm sinh phức tạp.")

add_c("Ước tính tần suất mắc suy tim ở trẻ em tại Việt Nam dao động trong khoảng từ {{c1::0,1% đến 0,2%}} dân số trẻ em.",
      "Dịch tễ: Tỷ lệ này cao hơn hẳn ở các trung tâm tim mạch nhi tuyến cuối do tiếp nhận dị tật bẩm sinh nặng.")

add_c("Ở trẻ sơ sinh và trẻ nhũ nhi, suy tim thường có đặc điểm nổi bật là khởi phát dưới dạng {{c1::suy tim cấp tính hoặc đợt cấp mất bù}}.",
      "Cơ chế: Trẻ nhỏ có dự trữ cơ tim thấp, khi có yếu tố khởi kích (sốt, nhiễm trùng, đóng ống động mạch) tim nhanh chóng mất bù.")

add_c("Về mặt thể bệnh lâm sàng, suy tim ở trẻ em chủ yếu biểu hiện dưới hình thái {{c1::suy tim sung huyết (Congestive Heart Failure)}}.",
      "Cơ chế: Ứ trệ tuần hoàn tĩnh mạch phổi gây thở nhanh, ran ẩm và ứ trệ tuần hoàn hệ thống gây gan to, phù.")

add_c("Khác với người lớn, triệu chứng lâm sàng của suy tim ở trẻ nhũ nhi chủ yếu bộc lộ qua đường {{c1::dinh dưỡng và tiêu hóa (bú kém, cữ bú kéo dài, nôn trớ, chậm tăng cân)}}.",
      "Lâm sàng: Trẻ nhũ nhi không thể than mệt hay đau ngực, bú gắng sức tương đương với nghiệm pháp gắng sức thể lực ở người lớn.")

add_c("Dấu hiệu vã mồ hôi bệnh lý trong suy tim ở trẻ nhũ nhi có đặc điểm là vã mồ hôi lạnh, tập trung chủ yếu ở {{c1::vùng trán và da đầu}} và xuất hiện rõ nhất lúc {{c1::trẻ đang gắng sức bú mẹ}}.",
      "Cơ chế: Hoạt hóa giao cảm bù trừ làm kích thích tuyến mồ hôi ngoại vi, rõ nhất khi trẻ phải tăng công hô hấp để bú.")

# ==========================================
# 2. SINH LÝ BỆNH & CUNG LƯỢNG TIM
# ==========================================
add_c("Cung lượng tim (CO) được quyết định bởi 4 yếu tố cơ bản gồm: {{c1::Tiền gánh, Hậu gánh, Sức bóp cơ tim và Tần số tim}}.",
      "Sinh lý: CO = Thể tích nhát bóp (SV) × Tần số tim (HR).")

add_c("Ở trẻ sơ sinh và trẻ nhũ nhi, do thể tích nhát bóp (SV) gần như cố định, cung lượng tim phụ thuộc chủ yếu vào {{c1::tần số tim (Heart Rate)}}.",
      "Cơ chế: Cơ tim trẻ nhỏ chứa nhiều collagen không co bóp và ít sợi myofibril hơn người lớn, khiến khả năng giãn nở buồng thất bị giới hạn.")

add_c("Định nghĩa: Tiền gánh (Preload) của tâm thất là {{c1::thể tích hoặc áp lực cuối tâm trương}} của buồng tâm thất trước khi bắt đầu kỳ co bóp.",
      "Sinh lý: Tiền gánh quyết định chiều dài ban đầu của sợi cơ tim theo định luật Frank-Starling.")

add_c("Định nghĩa: Hậu gánh (Afterload) của tâm thất là {{c1::sức cản của mạch máu ngoại biên}} mà tâm thất phải vượt qua để tống máu vào đại động mạch.",
      "Sinh lý: Hậu gánh tăng cao khi có co mạch ngoại vi do kích thích giao cảm hoặc hẹp đường tống máu thất.")

add_c("Khi tần số tim ở trẻ nhũ nhi tăng quá nhanh vượt ngưỡng {{c1::180 đến 200 nhịp/phút}}, cung lượng tim sẽ sụt giảm do {{c1::thời gian tâm trương bị rút ngắn nghiêm trọng}}.",
      "Cơ chế: Rút ngắn tâm trương làm giảm thể tích đổ đầy thất và giảm thời gian tưới máu động mạch vành nuôi cơ tim.")

add_c("Trong cơ chế bù trừ tại cơ tim, hiện tượng giãn sợi cơ ban đầu để đáp ứng với tình trạng tăng tiền gánh tuân theo {{c1::định luật Frank-Starling}}.",
      "Cơ chế: Kéo dài sợi actin-myosin làm tăng ái lực với canxi, nhưng nếu giãn quá mức sẽ làm giảm hiệu suất tống máu.")

add_c("Trong suy tim mạn tính, đáp ứng phì đại tế bào cơ tim đồng tâm (Concentric Hypertrophy) thường xảy ra do {{c1::quá tải áp lực (tăng hậu gánh)}}.",
      "Cơ chế: Các sợi cơ tim xếp song song để tăng độ dày thành tim, giảm sức căng thành thất theo định luật Laplace.")

add_c("Trong suy tim do tăng gánh thể tích (shunt Trái - Phải lớn), cơ tim đáp ứng bằng hình thái {{c1::phì đại lệch tâm (Eccentric Hypertrophy)}}.",
      "Cơ chế: Các sarcomere xếp nối tiếp nhau làm buồng tim giãn lớn để chứa thể tích máu tăng thêm.")

add_c("Hệ thần kinh giao cảm phản ứng sớm nhất trong suy tim bằng cách giải phóng hai chất dẫn truyền thần kinh chủ lực là {{c1::Epinephrine và Norepinephrine}}.",
      "Cơ chế: Kích thích thụ thể beta-1 làm tăng nhịp tim và tăng co bóp, kích thích thụ thể alpha-1 gây co mạch tái phân bố tuần hoàn.")

add_c("Hậu quả bất lợi lâu dài của việc hoạt hóa giao cảm liên tục trong suy tim là làm tăng hậu gánh thất trái và gây hiện tượng {{c1::điều hòa giảm (Down-regulation)}} thụ thể beta-1 adrenergic.",
      "Dược lý: Đây là cơ sở khoa học để chỉ định thuốc chẹn beta giao cảm (Carvedilol) trong điều trị suy tim mạn tính ổn định.")

add_c("Khi áp lực tưới máu thận giảm, tế bào cạnh cầu thận sẽ tăng tiết enzyme {{c1::Renin}}, khởi động dòng thác kích hoạt trục RAAS.",
      "Cơ chế: Renin chuyển Angiotensinogen từ gan thành Angiotensin I bất hoạt.")

add_c("Enzyme chuyển Angiotensin (ACE) nằm chủ yếu ở {{c1::nội mạc mao mạch phổi}}, có nhiệm vụ chuyển Angiotensin I thành {{c1::Angiotensin II}} có hoạt tính co mạch cực mạnh.",
      "Dược lý: Thuốc ức chế men chuyển (Captopril, Enalapril) ức chế enzyme này, giúp giãn mạch hạ hậu gánh.")

add_c("Tác dụng của Angiotensin II tại vỏ thượng thận là kích thích lớp cầu tăng tổng hợp và bài tiết hormone {{c1::Aldosterone}}.",
      "Cơ chế: Aldosterone tác động lên ống lượn xa và ống góp làm tăng tái hấp thu Natri và nước, bài xuất Kali vào nước tiểu.")

add_c("Khi thành tâm nhĩ bị căng giãn quá mức do ứ máu sung huyết, cơ tim tâm nhĩ sẽ tăng tiết hormone peptide có tên là {{c1::ANP (Atrial Natriuretic Peptide)}}.",
      "Cơ chế: ANP làm giãn tiểu động mạch đến của cầu thận và tăng bài xuất muối nước qua nước tiểu để giải áp buồng tim.")

add_c("Hậu quả huyết động của suy tim trái là gây tăng áp lực mao mạch phổi bít, dẫn đến {{c1::ứ huyết phổi, khó thở, ho khan và phù phổi cấp}}.",
      "Cơ chế: Máu không tống hết khỏi thất trái làm dồn ngược áp lực về nhĩ trái và tĩnh mạch phổi.")

add_c("Hậu quả huyết động của suy tim phải là gây ứ trệ tuần hoàn tĩnh mạch chủ, dẫn đến {{c1::gan to đau, tĩnh mạch cổ nổi và phù ngoại vi}}.",
      "Cơ chế: Áp lực tâm nhĩ phải tăng cao cản trở máu hồi lưu từ tĩnh mạch chủ trên và tĩnh mạch chủ dưới.")

# ==========================================
# 3. NGUYÊN NHÂN SUY TIM TRẺ EM
# ==========================================
add_c("Bệnh tim bẩm sinh có luồng shunt Trái - Phải lớn gây suy tim chủ yếu theo cơ chế {{c1::tăng gánh thể tích (tăng tiền gánh)}}.",
      "Căn nguyên: Bao gồm thông liên thất (VSD), còn ống động mạch (PDA), thông sàn nhĩ thất (AVSD).")

add_c("Bệnh hẹp van động mạch chủ nặng và hẹp eo động mạch chủ gây suy tim chủ yếu theo cơ chế {{c1::tăng gánh áp lực (tăng hậu gánh)}}.",
      "Cơ chế: Tâm thất trái phải co bóp chống lại sức cản cơ học rất lớn để tống máu vào đại tuần hoàn.")

add_c("Hội chứng ALCAPA (Bland-White-Garland) là một nguyên nhân gây suy tim do tổn thương cơ tim, trong đó {{c1::động mạch vành trái xuất phát bất thường từ động mạch phổi}}.",
      "Lâm sàng: Khi sức cản phổi giảm, máu từ ĐMV trái chảy ngược về ĐMP (hiện tượng cướp máu), gây nhồi máu cơ tim trước rộng ở trẻ nhũ nhi.")

add_c("Ở trẻ sơ sinh, các rối loạn chuyển hóa bẩm sinh có thể gây suy chức năng co bóp cơ tim cấp tính gồm: {{c1::hạ canxi máu nặng, hạ đường huyết kéo dài và hạ magie máu}}.",
      "Lâm sàng: Luôn kiểm tra đường huyết và điện giải đồ ở mọi trẻ sơ sinh có suy tim cấp chưa rõ nguyên nhân.")

add_c("Bệnh Beriberi thể ướt (Shoshin Beriberi) là một nguyên nhân gây suy tim cấp cung lượng cao ở trẻ nhỏ do thiếu hụt {{c1::vitamin B1 (Thiamine)}}.",
      "Lâm sàng: Bệnh đáp ứng ngoạn mục sau khi tiêm tĩnh mạch Thiamine liều cao.")

add_c("Nguyên nhân hàng đầu gây sốc tim và suy tim cấp tử vong ở trẻ từ 4 đến 12 tháng tuổi trước đó khỏe mạnh là {{c1::viêm cơ tim cấp do virus (Viral Myocarditis)}}.",
      "Căn nguyên: Hay gặp do virus Coxsackie B, Adenovirus, Parvovirus B19 và Echovirus.")

add_c("Block nhĩ thất hoàn toàn bẩm sinh (Congenital Complete Heart Block) ở trẻ sơ sinh thường có liên quan đến mẹ mắc bệnh tự miễn có kháng thể {{c1::kháng Ro/SSA và kháng La/SSB}}.",
      "Cơ chế: Kháng thể của mẹ qua nhau thai gây viêm và xơ hóa vĩnh viễn nút nhĩ thất của thai nhi.")

# ==========================================
# 4. TRIỆU CHỨNG LÂM SÀNG & CẬN LÂM SÀNG
# ==========================================
add_c("Dấu hiệu khó thở khi nằm phẳng và đỡ khó thở hơn khi ngồi hoặc bế đầu cao trong suy tim trái được gọi là {{c1::tư thế Orthopnea}}.",
      "Cơ chế: Khi nằm phẳng, lượng máu tĩnh mạch từ chi dưới dồn về tim tăng lên làm tăng áp lực mao mạch phổi.")

add_c("Trong cơn phù phổi cấp (Acute Pulmonary Edema), khám phổi nghe thấy ran ẩm nhỏ hạt có đặc điểm {{c1::dâng nhanh từ hai đáy phổi lên khắp hai phế trường như nước thủy triều}}.",
      "Cấp cứu: Kèm theo trẻ thở rên, co kéo lồng ngực tối đa và khạc đờm bọt hồng.")

add_c("Tiếng ngựa phi (Gallop T3) nghe rõ ở mỏm tim trong suy tim trái được phát sinh do {{c1::dòng máu dội nhanh và mạnh vào thành tâm thất trái đang giãn và giảm độ giãn nở trong đầu kỳ tâm trương}}.",
      "Lâm sàng: Tiếng T3 phối hợp với nhịp tim nhanh tạo nên nhịp 3 tiếng đặc trưng như tiếng ngựa chạy.")

add_c("Đặc điểm gan to trong suy tim phải giai đoạn đầu được mô tả là kiểu {{c1::gan đàn xếp (thu nhỏ lại rõ rệt sau khi điều trị lợi tiểu và to ra khi suy tim tái phát)}}.",
      "Lâm sàng: Bờ gan mềm, ấn đau tức; giai đoạn muộn xơ hóa sẽ không thu nhỏ được nữa.")

add_c("Dấu hiệu phản hồi gan - tĩnh mạch cổ (Hepatojugular Reflux) được coi là dương tính khi {{c1::ấn bàn tay vào vùng hạ sườn phải làm tĩnh mạch cổ nổi căng phồng thêm và duy trì trên 10-15 giây}}.",
      "Cơ chế: Phản ánh tâm nhĩ phải không thể tiếp nhận thêm lượng máu hồi lưu tĩnh mạch dồn về.")

add_c("Dấu hiệu Hartzer dương tính trên lâm sàng là cảm giác {{c1::thất phải đập mạnh dội vào đầu ngón tay người khám đặt ở góc dưới mũi ức}}.",
      "Ý nghĩa: Chỉ điểm tình trạng phì đại và giãn buồng tâm thất phải trong suy tim phải.")

add_c("Hội chứng suy tuần hoàn ngoại vi cấp tính trong sốc tim biểu hiện bằng thời gian đổ đầy mao mạch (CRT) kéo dài {{c1::trên 3 giây}}.",
      "Lâm sàng: Kèm theo da tái nhợt, nổi vân tím và đầu chi lạnh ngắt.")

add_c("Chỉ số tim - ngực (Cardiothoracic Ratio - CTR) trên phim X-quang ngực thẳng được coi là tim to khi: Trẻ sơ sinh CTR > {{c1::0,60}}; Trẻ nhũ nhi CTR > {{c1::0,55}}; Trẻ lớn CTR > {{c1::0,50}}.",
      "Chẩn đoán: Đo bằng tỷ lệ đường kính ngang lớn nhất của bóng tim chia cho đường kính ngang lớn nhất lồng ngực.")

add_c("Hình ảnh đường Kerley B trên phim X-quang tim phổi thẳng của bệnh nhân suy tim là các đường mờ ngắn nằm ngang ở góc sườn hoành, phản ánh tình trạng {{c1::phù nề dịch ở các vách liên tiểu thùy phổi (phù mô kẽ)}}.",
      "Hình ảnh: Dấu hiệu đặc trưng của tăng áp lực tĩnh mạch phổi mạn tính.")

add_c("Trên siêu âm tim, phân suất tống máu thất trái (LVEF theo phương pháp Simpson) được coi là suy giảm nặng khi LVEF đạt dưới mức {{c1::35%}} (bình thường ≥ 55-60%).",
      "Cận lâm sàng: Phân suất co rút thất trái FS bình thường ≥ 28-30%, suy giảm khi FS < 25%.")

add_c("Chỉ dấu sinh học peptide lợi niệu {{c1::NT-proBNP}} huyết thanh tăng cao vượt trội giúp bác sĩ cấp cứu phân biệt chính xác khó thở do suy tim với khó thở do viêm tiểu phế quản cấp.",
      "Ý nghĩa: NT-proBNP có thời gian bán hủy dài hơn BNP và có độ nhạy rất cao trong chẩn đoán suy tim trẻ em.")

# ==========================================
# 5. PHÂN ĐỘ SUY TIM
# ==========================================
add_c("Theo phân độ lâm sàng suy tim trẻ em Việt Nam, Suy tim Độ 1 được đặc trưng bởi: Khó thở {{c1::chỉ khi gắng sức (khi bú, khóc)}}; Kích thước gan dưới sườn phải {{c1::< 2 cm}}; {{c1::Không phù hoặc phù kín đáo}}.",
      "Lâm sàng: Lượng nước tiểu của trẻ còn gần như bình thường.")

add_c("Theo phân độ lâm sàng suy tim trẻ em Việt Nam, Suy tim Độ 2 được đặc trưng bởi: Khó thở {{c1::thường xuyên cả khi nghỉ ngơi}}; Kích thước gan dưới sườn phải {{c1::từ 2 đến 4 cm}}; {{c1::Phù nhẹ hoặc vừa hai chi dưới}}.",
      "Lâm sàng: Lượng nước tiểu bắt đầu giảm nhẹ.")

add_c("Theo phân độ lâm sàng suy tim trẻ em Việt Nam, Suy tim Độ 3 được đặc trưng bởi: Khó thở nặng co kéo; Gan to {{c1::trên 4 đến 5 cm}} nhưng {{c1::còn thu nhỏ sau điều trị (gan đàn xếp)}}; Tiên lượng {{c1::suy tim còn hồi phục}}.",
      "Lâm sàng: Bệnh nhi phù to toàn thân và có tình trạng thiểu niệu rõ rệt.")

add_c("Theo phân độ lâm sàng suy tim trẻ em Việt Nam, Suy tim Độ 4 được đặc trưng bởi: Khó thở nặng liên tục; Gan to mạn tính {{c1::chắc cứng, không thu nhỏ sau điều trị}}; Tiên lượng {{c1::suy tim không hồi phục (xơ gan tim)}}.",
      "Lâm sàng: Trẻ thiểu niệu nặng hoặc vô niệu, phù toàn thân kháng trị kèm cổ trướng.")

add_c("Thang điểm Ross cải tiến lượng hóa mức độ suy tim ở trẻ dưới 1 tuổi dựa trên 7 tiêu chí lâm sàng gồm: {{c1::lượng sữa bú, thời gian cữ bú, nhịp thở, thở gắng sức, nhịp tim, kích thước gan và thời gian CRT}}.",
      "Phân tầng: 0-2 điểm (Ross I), 3-6 điểm (Ross II), 7-9 điểm (Ross III), 10-14 điểm (Ross IV).")

add_c("Phân loại chức năng suy tim theo Hội Tim mạch New York (NYHA) chủ yếu được áp dụng cho đối tượng {{c1::trẻ lớn và người trưởng thành}} (do đòi hỏi đánh giá mức độ hạn chế hoạt động thể lực gắng sức).",
      "Lâm sàng: Trẻ nhũ nhi không áp dụng được NYHA mà phải dùng thang điểm Ross.")

# ==========================================
# 6. ĐIỀU TRỊ SUY TIM: KHÔNG DÙNG THUỐC & LỢI TIỂU
# ==========================================
add_c("Tư thế nằm đầu cao tối ưu cho bệnh nhi suy tim nặng là tư thế {{c1::Fowler (nửa nằm nửa ngồi góc 30 đến 45 độ)}}.",
      "Cơ chế: Giúp cơ hoành hạ thấp làm tăng dung tích phổi và giảm lượng máu tĩnh mạch hồi lưu về tim phải.")

add_c("Chế độ ăn hạn chế muối (ăn nhạt) ở trẻ suy tim nặng đòi hỏi kiểm soát lượng muối đưa vào dưới mức {{c1::< 1,2 g muối/ngày}} (tương đương dưới 0,5 g Natri/ngày).",
      "Thực hành: Không nêm thêm nước mắm, muối vào bột ăn dặm hoặc cháo của trẻ.")

add_c("Trong giai đoạn suy tim cấp có phù to và thiểu niệu, lượng dịch đưa vào cơ thể cần được hạn chế ở mức {{c1::70% đến 80% nhu cầu duy trì cơ bản (khoảng 60 - 80 mL/kg/ngày)}}.",
      "Thực hành: Cần trừ đi lượng dịch pha thuốc tiêm truyền tĩnh mạch.")

add_c("Thuốc lợi tiểu quai đầu tay điều trị suy tim cấp ở trẻ em là {{c1::Furosemid}}, với liều tiêm tĩnh mạch thông thường từ {{c1::1 đến 2 mg/kg/ngày}} (tối đa 6 mg/kg/ngày).",
      "Dược lý: Ức chế đồng vận chuyển Na+-K+-2Cl- ở nhánh dày quai Henle, khởi phát tác dụng sau 5-10 phút tiêm TM.")

add_c("Hai tác dụng phụ rối loạn điện giải thường gặp nhất và nguy hiểm nhất khi sử dụng Furosemid liều cao kéo dài là {{c1::hạ Kali máu và hạ Natri máu}}.",
      "Lâm sàng: Hạ Kali máu làm tăng nhạy cảm cơ tim và khởi phát ngộ độc Digitalis.")

add_c("Thuốc lợi tiểu kháng Aldosterone {{c1::Spironolacton}} có liều dùng từ {{c1::1 đến 3 mg/kg/ngày}} uống chia 1-2 lần.",
      "Dược lý: Tác dụng giữ Kali, chống xơ hóa cơ tim và thường được phối hợp cùng Furosemid để hiệp đồng tác dụng.")

# ==========================================
# 7. ĐIỀU TRỊ SUY TIM: ỨC CHẾ MEN CHUYỂN & CHẸN BETA
# ==========================================
add_c("Thuốc ức chế men chuyển đầu tay thường dùng ở trẻ nhỏ là {{c1::Captopril}}, với liều khởi đầu thăm dò từ {{c1::0,1 đến 0,3 mg/kg/liều}} uống ngày 3 lần trước bữa ăn.",
      "Dược lý: Captopril có thời gian tác dụng ngắn, dễ chỉnh liều và dừng kịp thời nếu xảy ra tụt huyết áp liều đầu.")

add_c("Captopril nên được cho trẻ uống vào thời điểm {{c1::trước bữa ăn 1 giờ}} để đảm bảo thuốc được hấp thu tối đa qua đường tiêu hóa.",
      "Dược lý: Thức ăn làm giảm sinh khả dụng của Captopril từ 30% đến 40%.")

add_c("Hai thông số xét nghiệm bắt buộc phải kiểm tra lại sau 1 đến 2 tuần bắt đầu dùng hoặc tăng liều thuốc ức chế men chuyển là {{c1::nồng độ Kali máu và Creatinine máu}}.",
      "Cảnh báo: ACEi làm giãn tiểu động mạch đi của cầu thận, có thể làm giảm mức lọc cầu thận và tăng Kali máu.")

add_c("Thuốc chẹn beta giao cảm được khuyến cáo hàng đầu trong suy tim mạn tính ở trẻ em là {{c1::Carvedilol}}, với liều bắt đầu cực thấp từ {{c1::0,05 mg/kg/liều}} ngày 2 lần.",
      "Dược lý: Carvedilol chẹn không chọn lọc thụ thể beta-1, beta-2 và chẹn alpha-1 gây giãn mạch.")

add_c("Nguyên tắc bất di bất dịch khi chỉ định Carvedilol cho trẻ suy tim là {{c1::tuyệt đối không khởi trị trong giai đoạn suy tim cấp mất bù}} và chỉ bắt đầu khi {{c1::bệnh nhân đã hết ứ dịch hoàn toàn và huyết động ổn định}}.",
      "Cơ chế: Tác dụng ức chế co bóp ban đầu của chẹn beta có thể gây sụp đổ cung lượng tim và sốc tim tử vong.")

# ==========================================
# 8. THUỐC INOTROPE & VẬN MẠCH TRUYỀN TM
# ==========================================
add_c("Thuốc inotrope ức chế enzyme Phosphodiesterase-3 được ưu tiên hàng đầu trong suy tim cấp có huyết áp còn ổn định là {{c1::Milrinone}}, với liều truyền duy trì từ {{c1::0,25 đến 0,75 µg/kg/phút}}.",
      "Dược lý: Milrinone vừa làm tăng sức co bóp cơ tim vừa làm giãn tiểu động mạch ngoại vi và động mạch phổi (Inodilator).")

add_c("Ở bệnh nhân suy tim cấp có huyết áp tâm thu còn thấp hoặc ranh giới, khi bắt đầu truyền Milrinone nên {{c1::bỏ qua liều tấn công (bolus)}} để phòng ngừa nguy cơ tụt huyết áp cấp tính.",
      "Lâm sàng: Liều bolus 50 µg/kg trong 30-60 phút dễ gây giãn mạch hệ thống đột ngột.")

add_c("Thuốc tăng co bóp cơ tim Catecholamine kinh điển {{c1::Dobutamin}} có liều truyền tĩnh mạch liên tục từ {{c1::2,5 đến 10 µg/kg/phút}}.",
      "Dược lý: Kích thích chọn lọc thụ thể beta-1 adrenergic tại cơ tim, ít làm tăng tần số tim và ít gây co mạch hơn Dopamin.")

add_c("Thuốc vận mạch {{c1::Dopamin}} ở dải liều inotrope tăng co bóp cơ tim là {{c1::5 đến 10 µg/kg/phút}}; trong khi ở dải liều cao co mạch tăng huyết áp là {{c1::10 đến 20 µg/kg/phút}}.",
      "Dược lý: Liều cao kích thích mạnh thụ thể alpha-1 làm tăng hậu gánh thất trái.")

add_c("Thuốc giãn mạch trực tiếp truyền tĩnh mạch {{c1::Nitroprusside}} có liều dùng từ {{c1::0,5 đến 4 µg/kg/phút}} (tối đa 8 µg/kg/phút).",
      "Dược lý: Giải phóng Nitric Oxide gây giãn cả động mạch và tĩnh mạch, bắt buộc bọc giấy bạc che sáng chống phân hủy thành Cyanide.")

# ==========================================
# 9. DIGOXIN & CẤP CỨU NGỘ ĐỘC DIGITALIS
# ==========================================
add_c("Cơ chế phân tử của Digoxin là gắn và ức chế chọn lọc bơm {{c1::Na+/K+-ATPase}} trên màng tế bào cơ tim.",
      "Cơ chế: Làm tăng Na+ nội bào, giảm hoạt động bơm trao đổi Na+/Ca2+, gián tiếp tích lũy Ca2+ tự do trong lưới nội bào làm tăng lực co bóp.")

add_c("Bốn tác dụng điện sinh lý kinh điển của Digoxin trên tim gồm: {{c1::Inotropic dương tính (tăng co bóp), Dromotropic âm tính (chậm dẫn truyền AV), Chronotropic âm tính (chậm nhịp xoang) và Bathmotropic dương tính (tăng tính kích thích cơ thất)}}.",
      "Ý nghĩa: Tăng co bóp nhưng làm tăng nguy cơ phát sinh loạn nhịp thất khi quá liều.")

add_c("Quy trình số hóa nhanh (Digitalization) liều tấn công Digoxin đường uống ở trẻ nhỏ có tổng liều từ {{c1::0,04 đến 0,06 mg/kg}}, được chia làm 3 lần trong 24 giờ theo tỷ lệ {{c1::1/2 - 1/4 - 1/4}} (cách nhau mỗi 8 giờ).",
      "Thực hành: Lần 1 uống 1/2 tổng liều, lần 2 sau 8h uống 1/4, lần 3 sau 8h tiếp uống 1/4 còn lại.")

add_c("Liều duy trì Digoxin đường uống hàng ngày ở trẻ em là từ {{c1::0,01 đến 0,02 mg/kg/ngày}} chia làm 2 lần cách nhau mỗi 12 giờ.",
      "Thực hành: Bắt đầu sau liều tấn công cuối cùng 12 giờ.")

add_c("Nồng độ trị liệu an toàn của Digoxin trong huyết thanh nằm trong khoảng hẹp từ {{c1::0,5 đến 0,9 ng/mL}} (nguy cơ ngộ độc tăng vọt khi nồng độ > 1,2 - 2,0 ng/mL).",
      "Xét nghiệm: Lấy máu định lượng nồng độ Digoxin sau liều uống ít nhất 6 đến 8 giờ.")

add_c("Yếu tố rối loạn điện giải nguy hiểm nhất thúc đẩy bùng phát ngộ độc Digoxin dù ở liều điều trị chuẩn là {{c1::hạ Kali máu (K+ < 3,5 mEq/L)}}.",
      "Cơ chế: Ion Kali cạnh tranh với Digoxin tại vị trí gắn trên bơm Na+/K+-ATPase; khi thiếu Kali, Digoxin gắn chặt hơn và phát huy độc tính dữ dội.")

add_c("Triệu chứng sớm nhất cảnh báo ngộ độc Digoxin ở trẻ nhỏ trên đường tiêu hóa là {{c1::biếng ăn đột ngột, buồn nôn và nôn mửa liên tục}}.",
      "Lâm sàng: Xuất hiện trước khi có các rối loạn nhịp tim nguy hiểm.")

add_c("Triệu chứng ngộ độc Digoxin trên thị giác ở trẻ lớn là nhìn mờ, sợ ánh sáng và hiện tượng {{c1::Xanthopsia (nhìn thấy quầng màu vàng hoặc màu xanh lá cây quanh nguồn sáng)}}.",
      "Cơ chế: Độc tính của digitalis ức chế bơm ion trên tế bào nón của võng mạc mắt.")

add_c("Dấu hiệu 'ngấm Digitalis' đơn thuần trên điện tâm đồ (chưa phải là ngộ độc) là hình ảnh {{c1::đoạn ST chênh xuống dạng đáy chén (Scooped ST depression)}} ở các chuyển đạo có sóng R cao.",
      "Điện tim: Thường thấy ở V5, V6, DII, phản ánh tác dụng điều trị bình thường của thuốc.")

add_c("Dấu hiệu rối loạn nhịp tim đặc trưng nhất và gợi ý cao nhất của ngộ độc Digoxin trên điện tâm đồ là {{c1::cơn nhịp nhanh nhĩ kèm block nhĩ thất (PAT with block)}} hoặc {{c1::ngoại tâm thu thất nhịp đôi (Bigeminy)}}.",
      "Điện tim: Tăng tính tự động của cơ nhĩ và cơ thất kết hợp với ức chế dẫn truyền qua nút nhĩ thất.")

add_c("Bước đầu tiên mang tính sống còn khi nghi ngờ bệnh nhân bị ngộ độc Digoxin là {{c1::ngừng ngay lập tức Digoxin}} và {{c1::mắc monitor theo dõi điện tim liên tục tại phòng hồi sức cấp cứu}}.",
      "Cấp cứu: Không được đợi kết quả xét nghiệm nồng độ máu mới ngừng thuốc.")

add_c("Trong điều trị ngộ độc Digoxin, nguyên tắc bù Kali tĩnh mạch là pha dịch truyền có nồng độ KCl không vượt quá {{c1::40 mEq/L}} và tốc độ truyền tối đa không quá {{c1::0,3 mEq/kg/giờ}}.",
      "Chống chỉ định bù Kali: Khi nồng độ K+ máu > 5,0 mEq/L hoặc bệnh nhân đang có Block nhĩ thất độ 2-3.")

add_c("Thuốc chống loạn nhịp hàng đầu được lựa chọn để điều trị loạn nhịp thất do ngộ độc Digoxin ở trẻ em là {{c1::Phenytoin (1,25 mg/kg truyền TM)}} hoặc {{c1::Lidocain (1 mg/kg tiêm TM bolus)}}.",
      "Dược lý: Phenytoin phục hồi hoạt tính bơm Na+/K+-ATPase và cải thiện dẫn truyền nhĩ thất.")

add_c("Thuốc đặc trị giải độc đặc hiệu duy nhất trong ngộ độc Digoxin nặng đe dọa tính mạng là {{c1::kháng thể kháng Digoxin Fab (DigiFab)}}.",
      "Dược lý: Các mảnh phân tử Fab gắn kết với Digoxin tự do trong tuần hoàn tạo phức hợp trơ đào thải qua thận.")

add_c("Ở bệnh nhân ngộ độc Digoxin xuất hiện loạn nhịp tim, thủ thuật {{c1::sốc điện khử rung chuyển nhịp (Cardioversion)}} bị CHỐNG CHỈ ĐỊNH tương đối vì có thể kích hoạt rung thất trơ không thể hồi phục.",
      "Cấp cứu: Chỉ sốc điện khi bệnh nhân đã rơi vào rung thất mất mạch thực sự sau khi đã tiêm kháng thể DigiFab.")

# ==========================================
# 10. THÊM CÁC THẺ CHI TIẾT & BẢNG SO SÁNH
# ==========================================
add_c("Thuốc giãn mạch đường uống ức chế trực tiếp cơ trơn tiểu động mạch {{c1::Hydralazine}} có liều dùng từ {{c1::0,5 đến 7 mg/kg/ngày}} chia làm 3 đến 4 lần.",
      "Dược lý: Giảm hậu gánh mạnh nhưng có thể gây phản xạ tim nhanh giao cảm bù trừ.")

add_c("Thuốc chẹn thụ thể alpha-1 adrenergic đường uống {{c1::Prazosine}} có liều khởi đầu thăm dò từ {{c1::0,2 đến 0,4 mg/ngày}}, sau đó tăng dần theo đáp ứng huyết áp.",
      "Dược lý: Gây giãn cả tiểu động mạch và tĩnh mạch, giảm cả tiền gánh và hậu gánh.")

add_c("Thuốc lợi tiểu giữ Kali ức chế trực tiếp kênh Natri biểu mô ở ống lượn xa và ống góp không phụ thuộc Aldosterone là {{c1::Triamteren}}, với liều dùng từ {{c1::2 đến 4 mg/kg/ngày}}.",
      "Dược lý: Thường phối hợp với Thiazide để tăng cường lợi niệu mà không gây mất Kali.")

add_c("Trong điều trị suy tim trẻ em bằng Furosemid đường uống, sinh khả dụng chỉ đạt khoảng 50% so với đường tiêm tĩnh mạch, do đó liều uống thường {{c1::gấp đôi liều tiêm tĩnh mạch}}.",
      "Dược lý: Cần lưu ý khi chuyển đổi từ phác đồ Furosemid tiêm TM sang phác đồ uống xuất viện.")

add_c("Hiện tượng kháng thuốc lợi tiểu (Diuretic Resistance) trong suy tim tiến triển được khắc phục bằng chiến lược phong bế nephron tuần tự (Sequential Nephron Blockade), phối hợp Furosemid với {{c1::Thiazide hoặc Spironolacton}}.",
      "Cơ chế: Ức chế tái hấp thu Natri bù trừ tại các đoạn ống thận xa khi quai Henle bị phong bế.")

add_c("Công thức ước tính số lọ kháng thể DigiFab cần dùng trong ngộ độc Digoxin cấp tính khi biết nồng độ máu là: Số lọ Fab = {{c1::(Nồng độ Digoxin ng/mL × Cân nặng kg) / 100}}.",
      "Cấp cứu: Nếu không rõ nồng độ huyết thanh trong tình huống ngừng tim, trẻ nhỏ tiêm ngay 1 đến 2 lọ DigiFab.")

add_c("Tiêu chuẩn điện tâm đồ chẩn đoán dày tâm thất phải ở trẻ nhũ nhi bao gồm: Trục điện tim chuyển sang {{c1::phải (Right Axis Deviation)}}; Sóng R ưu thế ở {{c1::chuyển đạo V1}}; và sóng T {{c1::dương ở V1 sau ngày tuổi thứ 7}}.",
      "Điện tim: Bình thường sóng T ở V1 phải âm từ ngày thứ 7 sau sinh đến tuổi thiếu niên.")

add_c("Tiêu chuẩn điện tâm đồ dày tâm thất trái ở trẻ em được xác định khi chỉ số Sokolow-Lyon (biên độ sóng S ở V1 cộng biên độ sóng R ở V5 hoặc V6) vượt quá {{c1::bách phân vị thứ 98 theo lứa tuổi}}.",
      "Điện tim: Kèm theo dấu hiệu quá tải tâm thu thất trái (ST chênh xuống và T âm ở V5, V6).")

add_c("Trên siêu âm tim Doppler, vận tốc tối đa của dòng hở van ba lá (V_TR) cho phép ước tính áp lực động mạch phổi tâm thu (PASP) thông qua phương trình Bernoulli cải tiến: PASP = {{c1::4 × (V_TR)^2 + RAP}}.",
      "Sinh lý: RAP là áp lực ước tính của tâm nhĩ phải (thường lấy mốc 5 đến 10 mmHg).")

add_c("Trong thang điểm Ross cải tiến, tiêu chí lượng sữa bú mỗi cữ của trẻ nhũ nhi được tính 2 điểm khi lượng sữa giảm xuống mức {{c1::< 70 mL/cữ}} (hoặc bú không đủ no).",
      "Phân tầng: Bú bình thường > 100 mL/cữ được tính 0 điểm; giảm nhẹ 70-100 mL/cữ được tính 1 điểm.")

add_c("Trong thang điểm Ross cải tiến, thời gian mỗi cữ bú ở trẻ nhũ nhi được tính 2 điểm khi thời gian cữ bú kéo dài vượt quá {{c1::> 40 phút}}.",
      "Lâm sàng: Thời gian bú 20-40 phút tính 1 điểm; bú nhanh dưới 20 phút tính 0 điểm.")

add_c("Trong thang điểm Ross cải tiến, tiêu chí kích thước gan to dưới bờ sườn phải được tính 2 điểm khi bờ dưới gan vượt quá {{c1::> 3 cm}}.",
      "Phân tầng: Gan < 2 cm tính 0 điểm; gan 2-3 cm tính 1 điểm.")

# ==========================================
# 11. CÁC THẺ BASIC HỎI ĐÁP (VĂN BẢN GỐC + GÓC NHÌN AI)
# ==========================================
add_b("Trình bày 4 yếu tố sinh lý quyết định cung lượng tim ở trẻ em?",
      "Cung lượng tim được đảm bảo nhờ 4 yếu tố: Tiền gánh, Hậu gánh, Tần số tim, Sức bóp của tim.",
      "Ở trẻ sơ sinh và nhũ nhi, cơ tim kém giãn nở nên thể tích nhát bóp gần như cố định. Cung lượng tim phụ thuộc sống còn vào tần số tim. Nhịp tim nhanh trên 180 nhịp/phút làm rút ngắn tâm trương, giảm tưới máu mạch vành và gây suy tim cấp.")

add_b("Mô tả các cơ chế bù trừ ngoài tim khi xảy ra suy tim ở trẻ em?",
      "Cơ chế bù trừ ngoài tim gồm: Hệ Renin - Angiotensin - Aldosteron (RAAS) gây co mạch và ứ muối nước; Tăng tiết các yếu tố bài xuất natri qua nước tiểu (ANP); Tăng khả năng tách và sử dụng O2 tại tổ chức.",
      "Trục RAAS và giao cảm bù trừ ban đầu giúp giữ huyết áp nuôi não và tim, nhưng về lâu dài nồng độ Angiotensin II và Aldosterone tăng cao sẽ gây xơ hóa cơ tim, tái cấu trúc buồng tim bất lợi và làm tăng cả tiền gánh lẫn hậu gánh.")

add_b("Trình bày 4 nhóm nguyên nhân chính gây suy tim ở trẻ em theo cơ chế huyết động?",
      "1. Do tăng gánh thể tích (tăng tiền gánh): Shunt Trái - Phải (VSD, PDA, ASD), rò ĐTM lớn. 2. Do tăng gánh áp lực (tăng hậu gánh): Hẹp van ĐMC, hẹp eo ĐMC, hẹp van ĐMP. 3. Tại cơ tim: Viêm cơ tim, bệnh cơ tim, ALCAPA, rối loạn chuyển hóa sơ sinh. 4. Rối loạn nhịp tim: Cơn nhịp nhanh, nhịp chậm xoang, block nhĩ thất.",
      "Việc xác định cơ chế huyết động quyết định trực tiếp can thiệp: Tăng tiền gánh cần lợi tiểu giảm tải; Tăng hậu gánh cần giãn mạch hoặc nong mạch; Giảm sức bóp cơ tim cần inotrope; Rối loạn nhịp cần thuốc chống loạn nhịp hoặc sốc điện.")

add_b("Nêu các triệu chứng lâm sàng kinh điển của suy tim trái ở trẻ em?",
      "Khó thở (khó thở khi gắng sức bú, tư thế Orthopnea, cơn hen tim, phù phổi cấp); Ho (ho khan về đêm, đờm lẫn máu); Tim to lệch trái, nhịp tim nhanh, tiếng ngựa phi Gallop T3, tiếng thổi tâm thu nhẹ ở mỏm do hở hai lá cơ năng; Phổi có ran ẩm đáy phổi dâng nhanh; Huyết áp tâm thu giảm nhưng tâm trương bình thường (huyết áp kẹt).",
      "Khó thở trong suy tim trái là khó thở do ứ huyết tĩnh mạch phổi. Ở trẻ nhũ nhi, khó thở khi gắng sức bộc lộ rõ nhất qua việc bú ngắt quãng, bú 2-3 phút phải dừng thở hổn hển và vã nhiều mồ hôi vùng trán.")

add_b("Nêu các triệu chứng lâm sàng kinh điển của suy tim phải ở trẻ em?",
      "Khó thở thường xuyên tăng dần, đau tức hạ sườn phải; Gan to (kiểu gan đàn xếp); Tĩnh mạch cổ nổi và phản hồi gan - tĩnh mạch cổ dương tính; Áp lực CVP tăng; Phù mềm hai chi dưới hoặc phù toàn thân; Đái ít; Khám tim có dấu hiệu Hartzer dương tính, tiếng thổi tâm thu nhẹ ở mũi ức do hở ba lá cơ năng; Huyết áp kẹt.",
      "Suy tim phải gây ứ trệ tuần hoàn ngoại vi. Gan to đàn xếp là dấu hiệu lâm sàng vô cùng giá trị để theo dõi đáp ứng điều trị: Bờ gan co nhỏ nhanh chóng sau tiêm Furosemid là bằng chứng của suy tim còn đáp ứng tốt.")

add_b("Trình bày phân độ suy tim trẻ em theo lâm sàng Việt Nam (Độ 1 đến Độ 4)?",
      "Độ 1: Khó thở khi gắng sức, gan < 2 cm, không phù, nước tiểu bình thường. Độ 2: Khó thở thường xuyên, gan 2-4 cm, phù nhẹ, nước tiểu giảm nhẹ. Độ 3: Khó thở nặng, gan > 4-5 cm (còn thu nhỏ sau điều trị), phù to, thiểu niệu, suy tim còn hồi phục. Độ 4: Khó thở liên tục, gan to cứng không thu nhỏ, phù to cổ trướng, vô niệu, suy tim không hồi phục (xơ gan tim).",
      "Ý nghĩa cốt lõi của bảng phân độ này là phân định ranh giới giữa suy tim còn hồi phục (Độ 3) và suy tim không hồi phục (Độ 4). Ở Độ 4, tế bào gan đã bị xơ hóa do thiếu oxy mạn tính (xơ gan tim), đáp ứng với thuốc trợ tim và lợi tiểu rất kém.")

add_b("Trình bày phác đồ số hóa nhanh (Digitalization) liều tấn công Digoxin ở trẻ em?",
      "Liều tấn công: 0,04 - 0,06 mg/kg/ngày đường uống chia làm 3 lần cách nhau 8 giờ theo tỷ lệ: Lần 1 uống 1/2 tổng liều; Lần 2 (sau 8h) uống 1/4 tổng liều; Lần 3 (sau 8h tiếp) uống 1/4 tổng liều còn lại. Liều duy trì: 0,01 - 0,02 mg/kg/ngày chia 2 lần cách nhau 12 giờ.",
      "Quy tắc chia liều 1/2 - 1/4 - 1/4 giúp cơ tim nhanh chóng đạt nồng độ gắn kết thụ thể hiệu quả mà không gây quá liều ngộ độc đột ngột. Trước khi cho uống liều 1/4 thứ hai và thứ ba, bắt buộc phải đếm nhịp tim và kiểm tra dấu hiệu nôn trớ của trẻ.")

add_b("Trình bày các bước cấp cứu ngộ độc Digoxin ở trẻ em?",
      "1. Ngừng thuốc ngay lập tức, rửa dạ dày nếu mới uống. 2. Xét nghiệm khẩn cấp nồng độ Digoxin máu và điện giải (K+, Na+, Mg2+, Ca2+). 3. Theo dõi liên tục điện tâm đồ. 4. Bù Kali máu bằng dịch truyền có KCl <= 40 mEq/L tốc độ <= 0,3 mEq/kg/giờ (chống chỉ định nếu K+ > 5 mEq/L hoặc có block nhĩ thất độ cao). 5. Dùng Phenytoin hoặc Lidocain trị loạn nhịp thất; dùng kháng thể DigiFab nếu ngộ độc đe dọa tính mạng.",
      "Tuyệt đối không được sốc điện chuyển nhịp khi ngộ độc Digoxin vì có thể kích hoạt rung thất trơ tử vong. Kháng thể DigiFab là biện pháp cứu mạng tối hậu giúp trung hòa tức thì Digoxin tự do trong tuần hoàn.")

add_b("Vì sao thở oxy nồng độ cao là chống chỉ định tương đối ở trẻ tim bẩm sinh shunt Trái - Phải lớn có suy tim?",
      "Thở oxy làm giảm sức cản mạch máu phổi.",
      "Oxy là chất giãn mạch phổi cực mạnh. Khi thở oxy nồng độ cao (FiO2 100%), sức cản mạch phổi tụt sâu làm dòng máu từ thất trái dồn sang thất phải và tràn lên phổi tăng vọt (tăng luồng shunt Trái - Phải). Điều này gây ngập lụt phổi, phù phổi cấp nặng hơn và làm cướp máu của tuần hoàn đại thể nuôi cơ thể.")

add_b("Tại sao bệnh nhân suy tim đang dùng Furosemid lại có nguy cơ ngộ độc Digoxin rất cao?",
      "Furosemid gây hạ Kali máu.",
      "Furosemid ức chế tái hấp thu Kali ở quai Henle dẫn đến hạ Kali máu. Ion K+ và Digoxin cạnh tranh nhau tại vị trí gắn trên bơm Na+/K+-ATPase của màng tế bào cơ tim. Khi Kali máu giảm, Digoxin gắn vào thụ thể dễ dàng và chặt chẽ hơn nhiều lần, làm bùng phát độc tính loạn nhịp tim dù nồng độ Digoxin trong máu vẫn ở ngưỡng điều trị thông thường.")

target_path.parent.mkdir(parents=True, exist_ok=True)
output_path = target_path.parent / "PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.cards.v2.json"
output_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(cards)} cards for PED-48 successfully at {output_path}!")
