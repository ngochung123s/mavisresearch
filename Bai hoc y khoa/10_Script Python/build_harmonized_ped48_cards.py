# -*- coding: utf-8 -*-
"""Generate complete harmonized, source-tagged Anki flashcards for PED-48 (130 cards).
Harmonizes PEDYTB (Giáo trình Bộ môn Nhi Thái Bình) & PED (Chuẩn hóa lâm sàng quốc tế).
"""
import json
from pathlib import Path

target_release = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.cards.v2.json")
target_master = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_MASTER_v1.cards.v2.json")

cards = []

def add_c(text, extra="", tags=None, source="PEDYTB"):
    tag_list = ["PED-48", source]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "cloze", "text": text, "extra": extra, "tags": tag_list})

def add_b(front, orig, ai, extra="", tags=None):
    back = f"<b>📖 Văn bản gốc [PEDYTB - Giáo trình Nhi Thái Bình]:</b><br>• {orig}<br><br><b>🔍 Góc nhìn bổ sung [PED - Chuẩn hóa Lâm sàng Quốc tế]:</b><br>• {ai}"
    tag_list = ["PED-48", "Basic-Card", "Dung-hoa-2-phien-ban"]
    if tags:
        tag_list.extend(tags)
    cards.append({"type": "basic", "front": front, "back": back, "extra": extra, "tags": tag_list})

# ==============================================================================
# KHỐI 1: PEDYTB - ĐẠI CƯƠNG, ĐỊNH NGHĨA & DỊCH TỄ (10 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Định nghĩa suy tim ở trẻ em trong giáo trình là tình trạng tim không còn khả năng đảm bảo {{c1::cung lượng tim}} đáp ứng nhu cầu của cơ thể.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.1).<br><b>🔍 Đối chiếu PED:</b> Cung lượng tim không đủ đáp ứng nhu cầu oxy của mô ở áp lực đổ đầy bình thường, hoặc chỉ đáp ứng được khi áp lực tâm thất tăng cao bất thường.",
      ["Dinh-nghia", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Theo thống kê kinh điển của Demopoulos và Sonnenblick (1995) tại Mỹ trong giáo trình, số người suy tim ước tính lên đến {{c1::6 triệu người}} vào năm 2000 với {{c1::400.000 ca mới mỗi năm}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.2).<br><b>🔍 Đối chiếu PED:</b> Cung cấp số liệu dịch tễ học nền tảng trong giáo trình giảng dạy của trường.",
      ["Dich-te", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tại Việt Nam, tần suất suy tim ở trẻ em ước tính trong khoảng {{c1::0,1% - 0,2%}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.2).<br><b>🔍 Đối chiếu PED:</b> Con số ước tính dịch tễ học nhi khoa tại Việt Nam được Bộ môn Nhi Thái Bình sử dụng làm chuẩn giảng dạy và ra đề thi.",
      ["Dich-te-VN", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Về tiên lượng, tỷ lệ tử vong ở những người suy tim nặng lên đến {{c1::50%}}; ngay cả những người mới bị suy tim thì hơn một nửa sẽ chết trong vòng {{c1::5 năm}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.2).<br><b>🔍 Đối chiếu PED:</b> Nhấn mạnh gánh nặng tử vong rất cao của suy tim ở trẻ em nếu không được điều trị nguyên nhân kịp thời.",
      ["Tien-luong", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung thứ nhất của suy tim trẻ em trong giáo trình là: Thường gặp {{c1::suy tim cấp}} (hay gặp do viêm cầu thận cấp tăng HA, thiếu vitamin B1, ngộ độc giáp, viêm cơ tim virus, hẹp eo ĐMC, còn ống ĐM lớn).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.3).<br><b>🔍 Đối chiếu PED:</b> Khác với người lớn thường suy tim mạn tính do xơ vữa mạch vành, trẻ em có dự trữ cơ tim thấp nên thường bùng phát suy tim cấp tính.",
      ["Dac-diem-chung", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung thứ hai của suy tim trẻ em trong giáo trình là: Thể bệnh chủ yếu trên lâm sàng là {{c1::suy tim sung huyết}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.3).<br><b>🔍 Đối chiếu PED:</b> Tình trạng ứ trệ tuần hoàn tĩnh mạch phổi (gây khó thở, ho) và tĩnh mạch hệ thống (gây gan to, phù) chiếm ưu thế tuyệt đối.",
      ["Dac-diem-chung", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung thứ ba của suy tim trẻ em trong giáo trình là: Suy tim từ từ mạn tính hay gặp do {{c1::thấp tim, bệnh tim bẩm sinh, bệnh van tim hậu thấp}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.3).<br><b>🔍 Đối chiếu PED:</b> Nhóm nguyên nhân tiến triển âm thầm theo thời gian.",
      ["Dac-diem-chung", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Đặc điểm chung thứ tư của suy tim trẻ em trong giáo trình là: Triệu chứng lâm sàng không giống người lớn mà chủ yếu biểu hiện bằng {{c1::triệu chứng toàn thân và tiêu hóa (kém ăn, nôn nhiều, chậm lên cân)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 1 - Mục 1.3).<br><b>🔍 Đối chiếu PED:</b> Trẻ nhũ nhi không thể than khó thở khi gắng sức; cữ bú kéo dài > 30 phút và vã mồ hôi trán là tương đương nghiệm pháp gắng sức ở người lớn.",
      ["Dac-diem-chung", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Theo hướng dẫn ISHLT 2025 cập nhật, suy tim trẻ em thứ phát sau bệnh cơ tim, bệnh tim mắc phải và tim bẩm sinh gắn liền với {{c1::tỷ lệ mắc bệnh và tử vong đáng kể}}.",
      "<b>📚 Nguồn:</b> ISHLT 2025 Guideline (PMID: 40838915).<br><b>🔍 Khuyến cáo:</b> Đòi hỏi tiếp cận đa chuyên khoa và phân tầng nguy cơ theo kiểu hình huyết động.",
      ["ISHLT-2025", "Lam-sang-chuyen-sau"], "PED")

add_c("[PED - Lâm sàng] Dấu hiệu vã mồ hôi bệnh lý trong suy tim ở trẻ nhũ nhi có đặc điểm là {{c1::vã mồ hôi lạnh}}, tập trung chủ yếu ở {{c1::vùng trán và da đầu}} và xuất hiện rõ nhất lúc {{c1::trẻ đang gắng sức bú mẹ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 10).<br><b>🔍 Cơ chế:</b> Phản ánh tình trạng cường giao cảm bù trừ kích thích tuyến mồ hôi ngoại biên.",
      ["Lam-sang-chuyen-sau"], "PED")

# ==============================================================================
# KHỐI 2: PEDYTB - SINH LÝ BỆNH & 4 YẾU TỐ HUYẾT ĐỘNG (12 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Trong điều kiện bình thường, cung lượng tim được đảm bảo nhờ 4 yếu tố: {{c1::Tiền gánh, Hậu gánh, Tần số tim và Sức bóp của tim}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.1).<br><b>🔍 Đối chiếu PED:</b> CO = Thể tích nhát bóp (SV) × Tần số tim (HR).",
      ["Sinh-ly-benh", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Giáo trình định nghĩa: Tiền gánh là {{c1::thể tích hoặc áp lực cuối tâm trương}} của tâm thất.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.1).<br><b>🔍 Đối chiếu PED:</b> Quyết định độ dài ban đầu của sợi cơ tim trước khi co bóp theo định luật Frank-Starling.",
      ["Tien-ganh", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Giáo trình định nghĩa: Hậu gánh là {{c1::sức cản của mạch máu}} với sức bóp của tâm thất.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.1).<br><b>🔍 Đối chiếu PED:</b> Là toàn bộ trở lực mạch hệ thống hoặc mạch phổi mà tâm thất phải vượt qua để mở van bán nguyệt tống máu.",
      ["Hau-ganh", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Ở trẻ sơ sinh và trẻ nhũ nhi, do thể tích nhát bóp (SV) gần như cố định, cung lượng tim phụ thuộc chủ yếu vào {{c1::tần số tim (Heart Rate)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 0).<br><b>🔍 Cơ chế:</b> Cơ tim trẻ nhỏ chứa nhiều collagen không co bóp và ít sợi myofibril hơn người lớn, khiến khả năng giãn nở buồng thất bị giới hạn.",
      ["Sinh-ly-nhi", "Lam-sang-chuyen-sau"], "PED")

add_c("[PED - Lâm sàng] Khi tần số tim ở trẻ nhũ nhi tăng quá nhanh vượt ngưỡng {{c1::180 đến 200 nhịp/phút}}, cung lượng tim sẽ sụt giảm do {{c1::thời gian tâm trương bị rút ngắn nghiêm trọng}}.",
      "<b>📚 Nguồn:</b> PED (Mục 0).<br><b>🔍 Cơ chế:</b> Rút ngắn tâm trương làm giảm thể tích đổ đầy thất và giảm thời gian tưới máu động mạch vành nuôi cơ tim.",
      ["Sinh-ly-nhi", "Lam-sang-chuyen-sau"], "PED")

add_c("[PEDYTB - Ôn thi] Cơ chế bù trừ tại tim trong suy tim gồm 3 cơ chế: {{c1::Giãn sợi cơ}} để đáp ứng tiền gánh; {{c1::Phì đại các tế bào cơ tim}}; và {{c1::Hệ thần kinh giao cảm (tăng epinephrin và norepinephrin)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.2).<br><b>🔍 Đối chiếu PED:</b> Giao cảm giúp tăng nhịp và co bóp, tái phân bố máu nuôi tim và não; nhưng kéo dài gây tăng hậu gánh do co mạch ngoại vi.",
      ["Bu-tru-tai-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Trong suy tim mạn tính, đáp ứng phì đại tế bào cơ tim đồng tâm (Concentric) thường do {{c1::quá tải áp lực (tăng hậu gánh)}}; trong khi phì đại lệch tâm (Eccentric) do {{c1::quá tải thể tích (tăng tiền gánh)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 2).<br><b>🔍 Cơ chế:</b> Phì đại lệch tâm do các sarcomere xếp nối tiếp nhau làm buồng tim giãn lớn để chứa thể tích máu tăng thêm.",
      ["Lam-sang-chuyen-sau"], "PED")

add_c("[PEDYTB - Ôn thi] Cơ chế bù trừ ngoài tim thứ nhất là hệ RAAS: Giảm tưới máu thận khởi động hệ {{c1::Renin - Angiotensin - Aldosteron}} càng gây co mạch, ứ muối và nước.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.2).<br><b>🔍 Đối chiếu PED:</b> Vòng xoắn bệnh lý làm tăng cả tiền gánh và hậu gánh, là cơ sở dùng thuốc ACEi và Spironolacton.",
      ["Bu-tru-ngoai-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Cơ chế bù trừ ngoài tim thứ hai là: Ứ máu ở thành tâm nhĩ gây kích thích tăng tiết các yếu tố gây bài xuất natri qua nước tiểu (giáo trình ghi: {{c1::atrial natrium factor / ANF}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.2).<br><b>🔍 Đối chiếu PED:</b> Thuật ngữ hiện đại là Atrial Natriuretic Peptide (ANP) và Brain Natriuretic Peptide (BNP/NT-proBNP).",
      ["Bu-tru-ngoai-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Cơ chế bù trừ ngoài tim thứ ba trong suy tim là: Tăng khả năng {{c1::tách và sử dụng O2 tại tổ chức}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.2).<br><b>🔍 Đối chiếu PED:</b> Tăng chênh lệch oxy động - tĩnh mạch để thích nghi với tình trạng giảm cung lượng tim.",
      ["Bu-tru-ngoai-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Hậu quả của suy tim: Giảm cung lượng tim làm giảm oxy tới các mô và {{c1::ưu tiên oxy cho não và động mạch vành}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.3).<br><b>🔍 Đối chiếu PED:</b> Cơ chế tái phân bố tuần hoàn của hệ giao cảm giúp bảo vệ cơ quan sống còn.",
      ["Hau-qua-suy-tim", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Tăng áp lực tĩnh mạch ngoại vi gây hậu quả: Suy tim phải gây {{c1::phù, gan to, tĩnh mạch cổ nổi}}; Suy tim trái gây {{c1::khó thở, có thể ho ra máu, phù phổi}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 2 - Mục 2.3).<br><b>🔍 Đối chiếu PED:</b> Suy tim phải gây ứ trệ đại tuần hoàn; suy tim trái gây ứ trệ tiểu tuần hoàn.",
      ["Hau-qua-suy-tim", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 3: PEDYTB - NGUYÊN NHÂN SUY TIM (4 NHÓM KINH ĐIỂN) (10 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Nhóm nguyên nhân do tăng gánh thể tích (tăng tiền gánh) gồm: Bệnh tim bẩm sinh có shunt Trái - Phải ({{c1::PDA, VSD, ASD}}) và nguyên nhân suy tim sớm ({{c1::dò động tĩnh mạch lớn, thân chung ĐM, chuyển gốc ĐM, teo van ba lá}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 3.1).<br><b>🔍 Đối chiếu PED:</b> Gây tăng thể tích máu đổ về các buồng tim, giãn sợi cơ theo Frank-Starling.",
      ["Nguyen-nhan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Nhóm nguyên nhân do tăng gánh áp lực (tăng hậu gánh) gồm: Hẹp van ĐMC nặng, hẹp eo ĐMC nặng; các bệnh gây tắc tĩnh mạch phổi ({{c1::tim ba nhĩ, bất thường hồi lưu TM phổi, teo van ba lá}}); tăng áp ĐMP sơ sinh, hẹp van ĐMP gây suy tim phải.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 3.2).<br><b>🔍 Đối chiếu PED:</b> Cản trở đường tống máu ra khỏi tâm thất.",
      ["Nguyen-nhan", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Nhóm nguyên nhân tại cơ tim gồm: Viêm cơ tim ({{c1::do thấp, nhiễm khuẩn, nhiễm độc}}), bệnh cơ tim, bất thường động mạch vành trái ({{c1::ALCAPA}}); ở trẻ sơ sinh có thể do rối loạn chuyển hóa ({{c1::hạ đường huyết, hạ canxi huyết, hạ magie huyết nặng}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 3.3).<br><b>🔍 Đối chiếu PED:</b> Suy giảm sức co bóp nội tại của tế bào cơ tim.",
      ["Nguyen-nhan", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Hội chứng ALCAPA (Bland-White-Garland) là dị tật động mạch vành trái xuất phát từ {{c1::động mạch phổi}}, khi sức cản phổi giảm sẽ gây hiện tượng {{c1::cướp máu động mạch vành}} dẫn đến nhồi máu cơ tim ở trẻ nhũ nhi.",
      "<b>📚 Nguồn:</b> PED (Mục 3.1).<br><b>🔍 Lâm sàng:</b> Trẻ nhũ nhi 2-3 tháng khóc thét khi bú (cơn đau thắt ngực nhũ nhi) kèm suy tim nặng và ST chênh lên ở DI, aVL.",
      ["ALCAPA", "Lam-sang-chuyen-sau"], "PED")

add_c("[PED - Lâm sàng] Bệnh Beriberi thể ướt (Shoshin Beriberi) là nguyên nhân suy tim cấp cung lượng cao ở trẻ nhỏ do thiếu hụt {{c1::vitamin B1 (Thiamine)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 3.1).<br><b>🔍 Lâm sàng:</b> Bệnh đáp ứng ngoạn mục sau khi tiêm tĩnh mạch Thiamine liều cao.",
      ["Beriberi", "Lam-sang-chuyen-sau"], "PED")

add_c("[PEDYTB - Ôn thi] Nhóm nguyên nhân do rối loạn nhịp tim gồm: Nhịp tim nhanh ({{c1::Basedow, do thuốc}}); Nhịp tim chậm ({{c1::suy giáp bẩm sinh, ngộ độc digitalis, morphin}}); và các rối loạn nhịp tim khác.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 3.4).<br><b>🔍 Đối chiếu PED:</b> Nhịp quá nhanh rút ngắn tâm trương; nhịp quá chậm không bù được thể tích nhát bóp.",
      ["Nguyen-nhan", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Block nhĩ thất hoàn toàn bẩm sinh ở trẻ sơ sinh thường có liên quan chặt chẽ đến mẹ mắc bệnh tự miễn có kháng thể {{c1::kháng Ro/SSA và kháng La/SSB}}.",
      "<b>📚 Nguồn:</b> PED (Mục 3.1).<br><b>🔍 Cơ chế:</b> Kháng thể mẹ qua nhau thai gây viêm và xơ hóa vĩnh viễn nút nhĩ thất của thai nhi.",
      ["Block-AV", "Lam-sang-chuyen-sau"], "PED")

add_c("[PED - Lâm sàng] Sốc tim ở trẻ sơ sinh trong tuần đầu sau sinh ngay khi ống động mạch đóng lại là dấu hiệu cảnh báo của {{c1::các bệnh tim bẩm sinh tắc nghẽn phụ thuộc ống động mạch (HLHS, hẹp eo ĐMC nặng, hẹp van ĐMC nguy kịch)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 3.2).<br><b>🔍 Cấp cứu:</b> Bắt buộc truyền Prostaglandin E1 khẩn cấp để mở lại ống động mạch.",
      ["Soc-tim-so-sinh", "Lam-sang-chuyen-sau"], "PED")

# ==============================================================================
# KHỐI 4: PEDYTB - TRIỆU CHỨNG LÂM SÀNG & CẬN LÂM SÀNG (16 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Khám tim trong suy tim trái: Mỏm tim lệch trái, nhịp tim nhanh, có thể có tiếng {{c1::ngựa phi (gallop)}}; thường có tiếng thổi tâm thu ở mỏm do {{c1::hở van hai lá cơ năng vì giãn buồng tim}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 4.1.1).<br><b>🔍 Đối chiếu PED:</b> Giãn vòng van hai lá thứ phát do buồng thất trái giãn lớn.",
      ["Suy-tim-trai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Khám phổi trong suy tim trái: Thường thấy {{c1::ran ẩm ở đáy phổi}}; cơn hen tim có {{c1::ran rít, ran ẩm hai phổi}}; trong phù phổi cấp có ran ẩm to nhỏ hạt dâng như {{c1::nước thủy triều}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 4.1.1).<br><b>🔍 Đối chiếu PED:</b> Phản ánh dịch thoát từ mao mạch phổi vào mô kẽ và phế nang.",
      ["Suy-tim-trai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Huyết áp trong suy tim trái có đặc điểm: Huyết áp tối đa (tâm thu) {{c1::giảm}} nhưng tối thiểu (tâm trương) lại {{c1::bình thường}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 4.1.1).<br><b>🔍 Đối chiếu PED:</b> Tạo nên hiệu số huyết áp kẹt do giảm thể tích tống máu.",
      ["Suy-tim-trai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] X-quang ngực trong suy tim trái: Tim to, nhất là tim trái; cả hai rốn phổi mờ, có thể gặp {{c1::đường Kerley}} hoặc hình {{c1::cánh bướm}} ở rốn phổi.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 3 - Mục 4.1.1).<br><b>🔍 Đối chiếu PED:</b> Đường Kerley B là phù mô kẽ vách liên tiểu thùy; cánh bướm là phù phế nang cấp.",
      ["Suy-tim-trai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Triệu chứng thực thể của suy tim phải: Gan to (lúc đầu kiểu {{c1::gan đàn xếp}}, sau cứng không nhỏ); tĩnh mạch cổ nổi và phản hồi gan - TM cổ (+); tăng áp lực CVP; tím; phù (lúc đầu hai chi dưới, sau toàn thân/đa màng); đái ít sẫm màu; dấu hiệu {{c1::Hartzer (+)}}; huyết áp tối đa bình thường, tối thiểu {{c1::thường tăng (kẹt huyết áp)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 4 - Mục 4.1.2).<br><b>🔍 Đối chiếu PED:</b> Toàn bộ hội chứng ứ trệ tuần hoàn ngoại vi kinh điển.",
      ["Suy-tim-phai", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Đính chính]: Phim X-quang nghiêng trái trong suy tim phải bản in gốc ghi nhầm 'thất trái giãn làm khoảng sáng sau tim hẹp lại', thực tế lâm sàng chuẩn xác là {{c1::thất phải giãn làm khoảng sáng sau xương ức hẹp lại}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 4 - Mục 4.1.2 ghi chú đính chính).<br><b>🔍 Giải phẫu X-quang:</b> Thất phải nằm ngay sau xương ức, khi giãn sẽ lấp đầy khoảng sáng sau xương ức trên phim nghiêng.",
      ["Dinh-chinh", "X-quang"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bệnh cảnh suy tim cấp ở trẻ em: Thường gặp suy tim trái hoặc toàn bộ tiến triển nhanh chóng, bệnh cảnh giống như {{c1::sốc tim}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 4 - Mục 4.2.1).<br><b>🔍 Đối chiếu PED:</b> Giảm nặng cung lượng tim đột ngột không bù trừ.",
      ["Suy-tim-cap", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Triệu chứng suy tuần hoàn ngoại vi trong suy tim cấp: Tinh thần kích thích vật vã; trẻ tái nhợt, chi lạnh, vã mồ hôi, vân tím; mạch nhanh nhỏ khó bắt; thời gian CRT {{c1::> 3 giây}}; huyết áp {{c1::hạ hoặc không đo được}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 4 - Mục 4.2.1).<br><b>🔍 Đối chiếu PED:</b> Tình trạng tưới máu mô cơ quan sụp đổ.",
      ["Suy-tim-cap", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Triệu chứng suy tim từ từ (suy tim mạn) ở trẻ nhũ nhi: Toàn thân (mệt mỏi, khóc yếu); Hô hấp (thở nhanh, thở rên, co kéo); Dinh dưỡng & tiêu hóa ({{c1::ăn bú kém, chậm lên cân, ra mồ hôi nhiều nhất là khi bú}}); Ứ trệ (TM cổ nổi, gan to, phù, đái ít).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Mục 4.2.2).<br><b>🔍 Đối chiếu PED:</b> Tam chứng bú ngắt quãng - thở nhanh co kéo - chậm tăng cân là chỉ điểm sớm nhất của suy tim nhũ nhi.",
      ["Suy-tim-man", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Chỉ số tim - ngực (CTR) trên phim X-quang ngực thẳng được coi là tim to bệnh lý khi: Trẻ sơ sinh CTR > {{c1::0,60}}; Trẻ nhũ nhi CTR > {{c1::0,55}}; Trẻ lớn CTR > {{c1::0,50}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.1).<br><b>🔍 Chẩn đoán:</b> Tỷ lệ đường kính ngang lớn nhất của tim chia đường kính lồng ngực.",
      ["CTR-Xquang"], "PED")

add_c("[PED - Lâm sàng] Trên siêu âm tim Doppler theo Simpson biplane, phân suất tống máu thất trái (LVEF) được phân độ: Bình thường LVEF ≥ 55-60%; Suy tim nhẹ LVEF {{c1::45 - 54%}}; Suy tim vừa LVEF {{c1::35 - 44%}}; Suy tim nặng LVEF {{c1::< 35%}}.",
      "<b>📚 Nguồn:</b> PED (Mục 5.3).<br><b>🔍 Siêu âm tim:</b> Phân suất co rút FS bình thường ≥ 28-30%, suy giảm khi FS < 25%.",
      ["LVEF-Sieu-am"], "PED")

add_c("[PED - Lâm sàng] Chỉ dấu sinh học peptide lợi niệu {{c1::NT-proBNP}} huyết thanh tăng cao vượt trội giúp bác sĩ cấp cứu phân biệt chính xác khó thở do suy tim với khó thở do viêm tiểu phế quản cấp.",
      "<b>📚 Nguồn:</b> PED (Mục 5.4).<br><b>🔍 Ý nghĩa:</b> NT-proBNP có độ nhạy rất cao trong chẩn đoán suy tim trẻ em.",
      ["NT-proBNP"], "PED")

# ==============================================================================
# KHỐI 5: PEDYTB - PHÂN ĐỘ SUY TIM (NYHA & LÂM SÀNG VIỆT NAM) (10 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Đánh giá mức độ suy tim theo NYHA gồm 4 độ: Độ I (có bệnh tim nhưng {{c1::không hạn chế hoạt động thông thường}}); Độ II (triệu chứng chỉ xuất hiện khi {{c1::gắng sức, giảm nhẹ hoạt động}}); Độ III (triệu chứng xuất hiện cả khi {{c1::gắng sức rất ít, hạn chế nhiều}}); Độ IV (triệu chứng xuất hiện {{c1::ngay cả lúc nghỉ ngơi}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Mục 5.1).<br><b>🔍 Đối chiếu PED:</b> Chủ yếu áp dụng cho trẻ lớn và người lớn.",
      ["Phan-do-NYHA", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bảng phân độ suy tim trẻ em Việt Nam - Độ 1: Khó thở {{c1::chỉ khi gắng sức}}; Kích thước gan {{c1::< 2 cm dưới bờ sườn phải}}; Phù {{c1::không phù hoặc phù kín đáo}}; Nước tiểu {{c1::gần như bình thường}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Bảng mục 5.2).<br><b>🔍 Đối chiếu PED:</b> Thể suy tim nhẹ nhất, đáp ứng tốt với nghỉ ngơi và ăn nhạt.",
      ["Phan-do-VN", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bảng phân độ suy tim trẻ em Việt Nam - Độ 2: Khó thở {{c1::thường xuyên}}; Kích thước gan {{c1::2 - 4 cm dưới bờ sườn phải}}; Phù {{c1::phù nhẹ hoặc phù vừa}}; Nước tiểu {{c1::giảm nhẹ}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Bảng mục 5.2).<br><b>🔍 Đối chiếu PED:</b> Bắt đầu cần điều trị thuốc lợi tiểu và ức chế men chuyển.",
      ["Phan-do-VN", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bảng phân độ suy tim trẻ em Việt Nam - Độ 3: Khó thở {{c1::nặng}}; Kích thước gan {{c1::> 4 - 5 cm dưới bờ sườn phải, nhưng CÒN THU NHỎ sau điều trị (gan đàn xếp)}}; Phù {{c1::phù to, phù toàn thân}}; Nước tiểu {{c1::rất ít}}; Tiên lượng {{c1::suy tim CÒN HỒI PHỤC}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Bảng mục 5.2).<br><b>🔍 Đối chiếu PED:</b> Trọng tâm thi cử: Gan còn thu nhỏ = suy tim còn hồi phục.",
      ["Phan-do-VN", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Bảng phân độ suy tim trẻ em Việt Nam - Độ 4: Khó thở {{c1::nặng liên tục}}; Kích thước gan {{c1::to mạn tính KHÔNG THU NHỎ}}; Phù {{c1::phù to toàn thân, cổ trướng}}; Nước tiểu {{c1::thiểu niệu / vô niệu}}; Tiên lượng {{c1::rất ít hiệu quả, suy tim KHÔNG HỒI PHỤC, xơ gan do tim}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 5 - Bảng mục 5.2).<br><b>🔍 Đối chiếu PED:</b> Trọng tâm thi cử: Gan cứng không thu nhỏ = suy tim không hồi phục (xơ gan tim).",
      ["Phan-do-VN", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Thang điểm Ross cải tiến lượng hóa mức độ suy tim ở trẻ dưới 1 tuổi dựa trên 7 tiêu chí: {{c1::lượng sữa bú, thời gian cữ bú, nhịp thở, thở gắng sức, nhịp tim, kích thước gan và thời gian CRT}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Phân tầng:</b> 0-2đ (Ross I), 3-6đ (Ross II - nhẹ), 7-9đ (Ross III - vừa), 10-14đ (Ross IV - nặng).",
      ["Thang-diem-Ross"], "PED")

add_c("[PED - Lâm sàng] Trong thang điểm Ross cải tiến, tiêu chí lượng sữa bú mỗi cữ được tính 2 điểm khi giảm xuống mức {{c1::< 70 mL/cữ}} (bình thường > 100 mL/cữ tính 0 điểm).",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Lượng hóa:</b> Trẻ giảm lượng bú phản ánh suy tim đang tiến triển.",
      ["Thang-diem-Ross"], "PED")

add_c("[PED - Lâm sàng] Trong thang điểm Ross cải tiến, thời gian mỗi cữ bú ở trẻ nhũ nhi được tính 2 điểm khi thời gian cữ bú kéo dài vượt quá {{c1::> 40 phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 6.2).<br><b>🔍 Lượng hóa:</b> Thời gian bú 20-40 phút tính 1 điểm; bú nhanh dưới 20 phút tính 0 điểm.",
      ["Thang-diem-Ross"], "PED")

# ==============================================================================
# KHỐI 6: PEDYTB - ĐIỀU TRỊ KHÔNG DÙNG THUỐC & THUỐC LỢI TIỂU (12 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Chế độ ăn nhạt (hạn chế muối) trong suy tim theo giáo trình: Suy tim nhẹ giảm muối {{c1::< 3 g muối/ngày}}; Suy tim nặng ăn nhạt gần như hoàn toàn {{c1::< 1,2 g muối/ngày}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.1).<br><b>🔍 Đối chiếu PED:</b> Tương đương < 0,5 g Natri/ngày trong suy tim nặng.",
      ["Che-do-an-nhat", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Tư thế nằm đầu cao tối ưu cho bệnh nhi suy tim nặng là tư thế {{c1::Fowler (nửa nằm nửa ngồi góc 30 đến 45 độ)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.1).<br><b>🔍 Cơ chế:</b> Giúp cơ hoành hạ thấp làm tăng dung tích phổi và giảm lượng máu tĩnh mạch hồi lưu về tim phải.",
      ["Tu-the-Fowler"], "PED")

add_c("[PED - Lâm sàng] Trong giai đoạn suy tim cấp có phù to và thiểu niệu, lượng dịch đưa vào cơ thể cần được hạn chế ở mức {{c1::70% đến 80% nhu cầu duy trì cơ bản (khoảng 60 - 80 mL/kg/ngày)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.1).<br><b>🔍 Thực hành:</b> Cần trừ đi lượng dịch pha thuốc tiêm truyền tĩnh mạch.",
      ["Han-che-dich"], "PED")

add_c("[PEDYTB - Ôn thi] Liều dùng thuốc lợi tiểu quai Furosemid theo giáo trình là {{c1::1 - 2 mg/kg/ngày}}; chú ý cần đề phòng {{c1::hạ kali máu, hạ natri máu}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.A).<br><b>🔍 Đối chiếu PED:</b> Thuốc tác dụng nhanh, mạnh, giảm nhanh tiền gánh.",
      ["Loi-tieu-Furosemid", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Liều dùng thuốc lợi tiểu Thiazide theo giáo trình là {{c1::1 - 2 mg/kg/ngày}}; chú ý {{c1::cần bổ sung kali}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.A).<br><b>🔍 Đối chiếu PED:</b> Lợi tiểu mức độ trung bình, dùng trong điều trị duy trì.",
      ["Loi-tieu-Thiazide", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Liều dùng thuốc lợi tiểu Spironolacton theo giáo trình là {{c1::1 - 3 mg/kg/ngày}}; Liều dùng Triamteren là {{c1::2 - 4 mg/kg/ngày}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.A).<br><b>🔍 Đối chiếu PED:</b> Thuộc nhóm lợi tiểu giữ kali (kháng aldosterone hoặc ức chế kênh Na biểu mô).",
      ["Loi-tieu-giu-K", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Trong điều trị suy tim trẻ em bằng Furosemid đường uống, sinh khả dụng chỉ đạt khoảng 50% so với đường tiêm tĩnh mạch, do đó liều uống thường {{c1::gấp đôi liều tiêm tĩnh mạch}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Cần lưu ý khi chuyển đổi từ phác đồ Furosemid tiêm TM sang phác đồ uống xuất viện.",
      ["Duoc-ly-Furosemid"], "PED")

add_c("[PED - Lâm sàng] Hiện tượng kháng thuốc lợi tiểu (Diuretic Resistance) được khắc phục bằng chiến lược phong bế nephron tuần tự, phối hợp Furosemid với {{c1::Thiazide hoặc Spironolacton}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Cơ chế:</b> Ức chế tái hấp thu Natri bù trừ tại các đoạn ống thận xa.",
      ["Khang-loi-tieu"], "PED")

# ==============================================================================
# KHỐI 7: PEDYTB - DIGOXIN & CẤP CỨU NGỘ ĐỘC DIGITALIS (16 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Tác dụng của Glycosid trợ tim (Digoxin) trên tim gồm 4 tác dụng: Làm tăng {{c1::tính co bóp cơ tim (inotropic dương)}}; làm chậm {{c1::dẫn truyền nhĩ - thất (dromotropic âm)}}; làm chậm {{c1::nhịp xoang (chronotropic âm)}}; làm tăng {{c1::tính tự động cơ thất (bathmotropic dương - nguy cơ loạn nhịp)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.B.1).<br><b>🔍 Đối chiếu PED:</b> Bốn tác dụng kinh điển cần thuộc lòng khi đi thi.",
      ["Digoxin-tac-dung", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Liều tấn công số hóa nhanh của Digoxin theo giáo trình là {{c1::0,04 - 0,06 mg/kg/ngày}} chia làm 3 lần cách nhau 8 giờ theo tỷ lệ: Lần 1 uống {{c1::1/2 tổng liều}}; Lần 2 (sau 8h) uống {{c1::1/4 tổng liều}}; Lần 3 (sau 8h tiếp) uống {{c1::1/4 tổng liều còn lại}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.B.1).<br><b>🔍 Đối chiếu PED:</b> Quy tắc 1/2 - 1/4 - 1/4 là câu hỏi thi cực kỳ kinh điển của Bộ môn Nhi Thái Bình.",
      ["Digoxin-lieu-tan-cong", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Liều duy trì của Digoxin theo giáo trình là {{c1::0,01 - 0,02 mg/kg/ngày}} chia làm {{c1::2 lần cách nhau 12 giờ}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 6 - Mục 6.1.2.B.1).<br><b>🔍 Đối chiếu PED:</b> Bắt đầu sau liều tấn công cuối cùng 12 giờ.",
      ["Digoxin-lieu-duy-tri", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Ở trẻ sơ sinh non tháng hoặc bệnh nhi có suy giảm chức năng thận, tổng liều tấn công số hóa Digoxin cần được giảm bớt {{c1::50%}} xuống còn {{c1::0,02 đến 0,03 mg/kg}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.1).<br><b>🔍 Dược lý:</b> Trẻ non tháng có độ thanh thải Digoxin qua thận giảm mạnh, nguy cơ ngộ độc rất cao.",
      ["Digoxin-non-thang"], "PED")

add_c("[PED - Lâm sàng] Khi chuyển đổi thuốc Digoxin từ đường uống sang đường tiêm tĩnh mạch, liều tiêm tĩnh mạch chỉ bằng {{c1::75% liều uống}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.1).<br><b>🔍 Dược lý:</b> Do sinh khả dụng đường uống chỉ đạt 70-80% so với tiêm tĩnh mạch.",
      ["Digoxin-chuyen-lieu"], "PED")

add_c("[PED - Lâm sàng] Nồng độ trị liệu an toàn của Digoxin trong huyết thanh nằm trong khoảng hẹp từ {{c1::0,5 đến 0,9 ng/mL}} (nguy cơ ngộ độc tăng vọt khi nồng độ > 1,2 - 2,0 ng/mL).",
      "<b>📚 Nguồn:</b> PED (Mục 9.1).<br><b>🔍 Xét nghiệm:</b> Lấy máu định lượng nồng độ Digoxin sau liều uống ít nhất 6 đến 8 giờ.",
      ["Digoxin-nong-do"], "PED")

add_c("[PEDYTB - Ôn thi] Yếu tố thuận lợi gây ngộ độc Digoxin theo giáo trình gồm: Quá liều, suy thận, rối loạn điện giải như {{c1::hạ kali máu, hạ magie máu, tăng canxi máu}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.2).<br><b>🔍 Đối chiếu PED:</b> Hạ Kali máu là yếu tố nguy hiểm nhất và hay gặp nhất khi dùng kèm Furosemid.",
      ["Ngo-doc-Digoxin", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Triệu chứng lâm sàng ngộ độc Digoxin theo giáo trình: Tiêu hóa ({{c1::biếng ăn, buồn nôn, nôn mửa, đau bụng}}); Thần kinh - thị giác ({{c1::nhìn mờ, sợ ánh sáng, nhìn thấy quầng màu vàng, màu cam}}); Tim mạch ({{c1::mạch chậm, nhịp tim không đều, ngoại tâm thu}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.2).<br><b>🔍 Đối chiếu PED:</b> Biếng ăn và nôn là dấu hiệu cảnh báo sớm nhất.",
      ["Ngo-doc-Digoxin", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Điện tâm đồ trong ngộ độc Digoxin theo giáo trình: Khoảng PR kéo dài (PQ kéo dài); ngoại tâm thu thất (nhất là {{c1::nhịp đôi, nhịp ba}}); nhịp nhanh trên thất kèm block AV; rung thất; dấu hiệu 'ngấm digitalis' là {{c1::ST chênh xuống dạng đáy chén}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.2).<br><b>🔍 Đối chiếu PED:</b> ST đáy chén là ngấm thuốc; nhịp đôi và PAT with block là ngộ độc thực sự.",
      ["ECG-Digoxin", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Năm bước điều trị ngộ độc Digoxin theo giáo trình: 1. {{c1::Ngừng thuốc ngay lập tức; rửa dạ dày}}; 2. {{c1::Lấy máu đo nồng độ Digoxin và điện giải (K+, Na+, Mg2+, Ca2+)}}; 3. {{c1::Theo dõi liên tục ĐTĐ}}; 4. {{c1::Bù kali}}; 5. {{c1::Điều trị rối loạn nhịp (Phenytoin/Lidocain/DigiFab)}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.2).<br><b>🔍 Đối chiếu PED:</b> 5 bước điều trị chuẩn cần trình bày chính xác khi thi tự luận.",
      ["Dieu-tri-ngo-doc-Digoxin", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Quy tắc bù kali trong điều trị ngộ độc Digoxin theo giáo trình: Uống hoặc truyền dung dịch có kali với nồng độ {{c1::40 mEq/lít}} với tốc độ tối đa {{c1::0,3 mEq/kg/giờ}} (chống chỉ định nếu có {{c1::block nhĩ thất độ cao hoặc K+ máu > 5 mEq/L}}).",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.2).<br><b>🔍 Đối chiếu PED:</b> Con số nồng độ 40 mEq/L và tốc độ 0,3 mEq/kg/h là chuẩn mực thi cử.",
      ["Bu-kali", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Thuốc chống loạn nhịp hàng đầu được lựa chọn để điều trị loạn nhịp thất do ngộ độc Digoxin ở trẻ em là {{c1::Phenytoin (1,25 mg/kg truyền TM)}} hoặc {{c1::Lidocain (1 mg/kg tiêm TM bolus)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Phenytoin phục hồi hoạt tính bơm Na+/K+-ATPase và cải thiện dẫn truyền nhĩ thất.",
      ["Phenytoin-Digoxin"], "PED")

add_c("[PED - Lâm sàng] Thuốc đặc trị giải độc đặc hiệu duy nhất trong ngộ độc Digoxin nặng đe dọa tính mạng là {{c1::kháng thể kháng Digoxin Fab (DigiFab)}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Dược lý:</b> Các mảnh phân tử Fab gắn kết với Digoxin tự do trong tuần hoàn tạo phức hợp trơ đào thải qua thận.",
      ["DigiFab"], "PED")

add_c("[PED - Lâm sàng] Công thức ước tính số lọ kháng thể DigiFab cần dùng khi biết nồng độ Digoxin huyết thanh là: Số lọ Fab = {{c1::(Nồng độ Digoxin ng/mL × Cân nặng kg) / 100}}.",
      "<b>📚 Nguồn:</b> PED (Mục 9.2).<br><b>🔍 Cấp cứu:</b> Nếu không rõ nồng độ huyết thanh trong tình huống ngừng tim, trẻ nhỏ tiêm ngay 1 đến 2 lọ DigiFab.",
      ["DigiFab-cong-thuc"], "PED")

add_c("[PED - Lâm sàng] Ở bệnh nhân ngộ độc Digoxin xuất hiện loạn nhịp tim, thủ thuật {{c1::sốc điện khử rung chuyển nhịp (Cardioversion)}} bị CHỐNG CHỈ ĐỊNH tương đối vì có thể kích hoạt rung thất trơ không thể hồi phục.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 7).<br><b>🔍 Cấp cứu:</b> Chỉ sốc điện khi bệnh nhân đã rơi vào rung thất mất mạch thực sự sau khi đã tiêm kháng thể DigiFab.",
      ["Chong-chi-dinh-soc-dien"], "PED")

# ==============================================================================
# KHỐI 8: PEDYTB - CATECHOLAMINE & THUỐC GIÃN MẠCH (14 thẻ)
# ==============================================================================
add_c("[PEDYTB - Ôn thi] Liều truyền tĩnh mạch liên tục của Dopamin theo giáo trình là {{c1::5 - 10 µg/kg/phút}}; Liều của Dobutamin là {{c1::2,5 - 10 µg/kg/phút}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.3).<br><b>🔍 Đối chiếu PED:</b> Dopamin liều 5-10 kích thích beta-1; Dobutamin chọn lọc beta-1.",
      ["Catecholamine", "On-thi-YTB"], "PEDYTB")

add_c("[PEDYTB - Đính chính]: Bản in giáo trình gốc in nhầm đơn vị Norepinephrin là '0,25 - 1 mg/kg/phút', thực tế lâm sàng bắt buộc phải là {{c1::0,25 - 1 µg/kg/phút (microgam)}} truyền tĩnh mạch.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.3 ghi chú đính chính).<br><b>🔍 Cảnh báo dược lý:</b> Liều miligam (mg) sẽ gây co mạch hoại tử tử vong tức thì, liều chuẩn lâm sàng là microgam (µg).",
      ["Dinh-chinh", "Norepinephrine"], "PEDYTB")

add_c("[PEDYTB - Ôn thi] Liều dùng các thuốc giãn mạch theo giáo trình: Nitroprusside {{c1::0,5 - 8 µg/kg/phút}} (truyền TM chậm bọc giấy bạc); Hydralazine {{c1::0,5 - 7 mg/kg/ngày}} chia 3 lần; Prazosine ban đầu {{c1::0,2 - 0,4 mg/ngày}}, duy trì {{c1::6 - 15 mg/kg/ngày}} chia 4 lần; Captopril {{c1::0,5 - 6 mg/kg/ngày}} chia 3 lần.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục 6.1.2.B.4).<br><b>🔍 Đối chiếu PED:</b> Bảng liều thuốc giãn mạch kinh điển trong giáo trình.",
      ["Thuoc-gian-mach", "On-thi-YTB"], "PEDYTB")

add_c("[PED - Lâm sàng] Thuốc ức chế men chuyển Captopril nên được cho trẻ uống vào thời điểm {{c1::trước bữa ăn 1 giờ}} để đảm bảo thuốc được hấp thu tối đa.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Thức ăn làm giảm sinh khả dụng của Captopril từ 30% đến 40%.",
      ["Captopril-uong"], "PED")

add_c("[PED - Lâm sàng] Thuốc inotrope ức chế enzyme Phosphodiesterase-3 được ưu tiên hàng đầu trong suy tim cấp có huyết áp còn ổn định là {{c1::Milrinone}}, với liều truyền duy trì từ {{c1::0,25 đến 0,75 µg/kg/phút}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Milrinone vừa làm tăng sức co bóp cơ tim vừa làm giãn tiểu động mạch ngoại vi và động mạch phổi (Inodilator).",
      ["Milrinone"], "PED")

add_c("[PED - Lâm sàng] Ở bệnh nhân suy tim cấp có huyết áp tâm thu còn thấp hoặc ranh giới, khi bắt đầu truyền Milrinone nên {{c1::bỏ qua liều tấn công (bolus)}} để phòng ngừa nguy cơ tụt huyết áp cấp tính.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Lâm sàng:</b> Liều bolus 50 µg/kg trong 30-60 phút dễ gây giãn mạch hệ thống đột ngột.",
      ["Milrinone-bolus"], "PED")

add_c("[PED - Lâm sàng] Thuốc chẹn beta giao cảm được khuyến cáo hàng đầu trong suy tim mạn tính ở trẻ em là {{c1::Carvedilol}}, với liều bắt đầu cực thấp từ {{c1::0,05 mg/kg/liều}} ngày 2 lần.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Dược lý:</b> Carvedilol chẹn không chọn lọc thụ thể beta-1, beta-2 và chẹn alpha-1 gây giãn mạch.",
      ["Carvedilol"], "PED")

add_c("[PED - Lâm sàng] Nguyên tắc bất di bất dịch khi chỉ định Carvedilol cho trẻ suy tim là {{c1::tuyệt đối không khởi trị trong giai đoạn suy tim cấp mất bù}} và chỉ bắt đầu khi {{c1::bệnh nhân đã hết ứ dịch hoàn toàn và huyết động ổn định}}.",
      "<b>📚 Nguồn:</b> PED (Mục 8.2).<br><b>🔍 Cơ chế:</b> Tác dụng ức chế co bóp ban đầu của chẹn beta có thể gây sụp đổ cung lượng tim và sốc tim tử vong.",
      ["Carvedilol-nguyen-tac"], "PED")

add_c("[PEDYTB - Ôn thi] Các biện pháp phòng bệnh suy tim theo giáo trình gồm: 1. Giải quyết sớm nguyên nhân và yếu tố thuận lợi; 2. Phòng tim bẩm sinh ({{c1::tiêm phòng Rubella, tránh hóa chất độc hại, chụp X-quang, dùng thuốc thận trọng khi mang thai}}); 3. Quản lý và điều trị dự phòng viêm họng liên cầu để {{c1::phòng thấp tim và bệnh van tim hậu thấp}}.",
      "<b>📚 Nguồn:</b> PEDYTB (Trang 7 - Mục VII).<br><b>🔍 Đối chiếu PED:</b> Ba trụ cột dự phòng suy tim nhi khoa.",
      ["Phong-benh", "On-thi-YTB"], "PEDYTB")

# ==============================================================================
# KHỐI 9: CẠM BẪY LÂM SÀNG & TIPS THỰC HÀNH (12 thẻ)
# ==============================================================================
add_c("[PED - Lâm sàng] Sai lầm chết người thường gặp ở trẻ suy tim thở nhanh kèm ran ẩm ở phổi là chẩn đoán nhầm thành {{c1::viêm phế quản phổi}} và điều trị bằng kháng sinh kéo dài vô ích.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 1).<br><b>🔍 Cạm bẫy:</b> Luôn sờ bờ dưới gan, đo SpO2 và nghe kỹ tiếng tim trước khi kết luận khó thở do phổi.",
      ["Cam-bay-lam-sang"], "PED")

add_c("[PED - Lâm sàng] Ở trẻ tim bẩm sinh có luồng shunt Trái - Phải lớn (như VSD lớn), việc cho thở oxy nồng độ cao (FiO2 100%) là sai lầm nguy hiểm vì {{c1::oxy gây giãn mạch phổi mạnh, làm tụt sức cản phổi và tăng lượng máu ngập lụt lên phổi}}.",
      "<b>📚 Nguồn:</b> PED (Mục 10 - Cạm bẫy 6).<br><b>🔍 Cạm bẫy:</b> Làm nặng thêm phù phổi cấp và cướp máu của tuần hoàn đại thể.",
      ["Cam-bay-lam-sang"], "PED")

add_c("[PED - Lâm sàng] Quy tắc điều dưỡng an toàn trước khi cho trẻ uống Digoxin là phải dùng ống nghe đếm nhịp tim ở mỏm trọn vẹn 1 phút; tạm dừng thuốc ngay nếu nhịp tim dưới {{c1::< 100 nhịp/phút}} ở trẻ nhũ nhi hoặc dưới {{c1::< 70 nhịp/phút}} ở trẻ lớn.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 3).<br><b>🔍 Thực hành:</b> Báo cáo bác sĩ ngay để kiểm tra điện tim và nồng độ thuốc máu.",
      ["Tip-dieu-duong"], "PED")

add_c("[PED - Lâm sàng] Để tránh hiện tượng tụt huyết áp tư thế phối hợp đột ngột, thuốc ức chế men chuyển Captopril nên được cho uống cách thời điểm tiêm hoặc uống Furosemid ít nhất {{c1::1 đến 2 giờ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 8).<br><b>🔍 Dược lý:</b> Tránh tác dụng cộng gộp hạ tiền gánh và hạ hậu gánh cùng một lúc.",
      ["Tip-dieu-duong"], "PED")

add_c("[PED - Lâm sàng] Ở bệnh nhi suy tim nặng đang điều trị nội khoa, việc cân trẻ mỗi sáng giúp phát hiện sớm tình trạng ứ dịch nếu cân nặng tăng đột ngột trên {{c1::> 30 đến 50 g/ngày}} ở trẻ nhũ nhi.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 4).<br><b>🔍 Thực hành:</b> Cân vào cùng một giờ mỗi sáng sau khi đi tiểu và trước cữ ăn đầu tiên.",
      ["Tip-dieu-duong"], "PED")

add_c("[PED - Lâm sàng] Khi theo dõi trẻ suy tim cấp được truyền thuốc tăng co bóp inotrope, lượng nước tiểu qua sonde tiểu lưu cần được đo mỗi giờ và duy trì đạt đích tối thiểu trên {{c1::> 1 mL/kg/giờ}}.",
      "<b>📚 Nguồn:</b> PED (Mục 13 - Tip 9).<br><b>🔍 Hồi sức:</b> Nước tiểu là thước đo nhạy cảm nhất của mức lọc cầu thận và tưới máu cơ quan đích.",
      ["Tip-dieu-duong"], "PED")

# ==============================================================================
# KHỐI 10: CÁC THẺ BASIC HỎI ĐÁP TOÀN DIỆN DUNG HÒA (10 thẻ)
# ==============================================================================
add_b("Trình bày định nghĩa và 4 đặc điểm chung của suy tim ở trẻ em?",
      "Định nghĩa: Tình trạng tim không còn khả năng đảm bảo cung lượng đáp ứng nhu cầu của cơ thể. 4 đặc điểm: 1. Thường gặp suy tim cấp (viêm cầu thận cấp, thiếu B1, viêm cơ tim, hẹp eo ĐMC, PDA lớn...). 2. Chủ yếu là suy tim sung huyết. 3. Suy tim mạn hay gặp do thấp tim, tim bẩm sinh, van tim hậu thấp. 4. Lâm sàng không giống người lớn: biểu hiện chủ yếu bằng kém ăn, nôn nhiều, chậm lên cân.",
      "Trẻ nhỏ có sức co bóp dự trữ thấp và thể tích nhát bóp cố định nên phụ thuộc vào tần số tim. Suy tim ở trẻ nhũ nhi bộc lộ gián tiếp qua cữ bú kéo dài > 30 phút kèm vã mồ hôi trán.")

add_b("Trình bày 4 yếu tố đảm bảo cung lượng tim và các cơ chế bù trừ trong suy tim?",
      "4 yếu tố: Tiền gánh, Hậu gánh, Tần số tim, Sức bóp cơ tim. Bù trừ tại tim: Giãn sợi cơ (Frank-Starling), phì đại tế bào cơ tim, hệ giao cảm (tăng epinephrin/norepinephrin). Bù trừ ngoài tim: Hệ RAAS (co mạch, ứ muối nước), tăng tiết yếu tố bài xuất natri qua nước tiểu (ANF/ANP), tăng tách và sử dụng O2 tại tổ chức.",
      "Hoạt hóa giao cảm và trục RAAS bù trừ ban đầu giúp giữ huyết áp nuôi não và mạch vành, nhưng nồng độ Catecholamine và Angiotensin II cao kéo dài sẽ gây độc tế bào cơ tim, tái cấu trúc buồng tim và tăng cả tiền gánh lẫn hậu gánh.")

add_b("Trình bày 4 nhóm nguyên nhân gây suy tim ở trẻ em theo giáo trình?",
      "1. Tăng gánh thể tích (tiền gánh): Shunt Trái - Phải (PDA, VSD, ASD), rò ĐTM lớn, thân chung ĐM, chuyển gốc ĐM, teo van ba lá. 2. Tăng gánh áp lực (hậu gánh): Hẹp van ĐMC, hẹp eo ĐMC, tắc TM phổi (tim 3 nhĩ, TAPVC, teo van ba lá), tăng áp ĐMP sơ sinh, hẹp van ĐMP. 3. Tại cơ tim: Viêm cơ tim (thấp, nhiễm khuẩn, nhiễm độc), bệnh cơ tim, ALCAPA, rối loạn chuyển hóa sơ sinh (hạ đường huyết, hạ Ca, hạ Mg). 4. Do rối loạn nhịp tim: Nhịp nhanh (Basedow, thuốc), nhịp chậm (suy giáp bẩm sinh, ngộ độc digitalis, morphin), loạn nhịp.",
      "Xác định đúng nhóm cơ chế quyết định phác đồ: Tăng tiền gánh dùng lợi tiểu; Tăng hậu gánh dùng giãn mạch; Giảm co bóp cơ tim dùng inotrope (Dobutamin, Milrinone); Rối loạn chuyển hóa sơ sinh cần bù ngay Canxi/Glucose.")

add_b("Trình bày triệu chứng lâm sàng và cận lâm sàng của suy tim trái?",
      "Cơ năng: Khó thở (gắng sức bú, thường xuyên, Orthopnea, hen tim, phù phổi cấp); Ho (khan ban đêm, đờm lẫn máu). Thực thể: Tim to lệch trái, nhịp nhanh, gallop T3, thổi tâm thu ở mỏm do hở hai lá cơ năng; Phổi có ran ẩm đáy phổi (phù phổi cấp ran dâng như thủy triều); Huyết áp tâm thu giảm, tâm trương bình thường (huyết áp kẹt). X-quang: Tim to bên trái, rốn phổi mờ, đường Kerley, cánh bướm. ĐTĐ: Dày thất trái. Siêu âm: Giãn thất trái, nhĩ trái, đo EF, FS.",
      "Khó thở trong suy tim trái là do ứ huyết tiểu tuần hoàn (tăng áp lực mao mạch phổi bít). Ở trẻ nhũ nhi, khó thở khi bú và cữ bú kéo dài > 30 phút là dấu hiệu tương đương khó thở khi gắng sức ở người lớn.")

add_b("Trình bày triệu chứng lâm sàng và cận lâm sàng của suy tim phải?",
      "Cơ năng: Khó thở thường xuyên tăng dần; Đau tức hạ sườn phải do gan to. Thực thể: Gan to (lúc đầu kiểu gan đàn xếp, sau cứng không nhỏ); Tĩnh mạch cổ nổi, phản hồi gan - TM cổ (+); Tăng áp lực CVP; Tím da niêm mạc; Phù mềm (lúc đầu hai chi dưới, sau toàn thân/đa màng); Đái ít sẫm màu; Hartzer (+), thổi tâm thu nhẹ mũi ức do hở ba lá cơ năng; Huyết áp tối đa bình thường, tối thiểu tăng (kẹt HA). X-quang: Cung dưới phải giãn, mỏm tim hếch lên, ĐMP giãn, phổi ứ huyết; phim nghiêng hẹp khoảng sáng sau tim (chuẩn xác là sau xương ức). ĐTĐ: Dày nhĩ phải, dày thất phải, trục phải. Siêu âm: Thất phải giãn, tăng áp ĐMP.",
      "Suy tim phải gây ứ trệ đại tuần hoàn. Gan đàn xếp là tiêu chuẩn lâm sàng vô cùng nhạy bén để đánh giá đáp ứng điều trị: bờ gan co nhỏ sau tiêm Furosemid là bằng chứng của suy tim còn hồi phục.")

add_b("Trình bày Bảng phân độ suy tim trẻ em Việt Nam (Độ 1 đến Độ 4)?",
      "Độ 1: Khó thở khi gắng sức, gan < 2 cm, không phù/kín đáo, nước tiểu gần bình thường. Độ 2: Khó thở thường xuyên, gan 2-4 cm, phù nhẹ/vừa, nước tiểu giảm nhẹ. Độ 3: Khó thở nặng, gan > 4-5 cm (CÒN THU NHỎ sau điều trị - gan đàn xếp), phù to toàn thân, nước tiểu rất ít, điều trị tích cực triệu chứng giảm (CÒN HỒI PHỤC). Độ 4: Khó thở nặng liên tục, gan to mạn tính KHÔNG THU NHỎ, phù to cổ trướng, thiểu niệu/vô niệu, điều trị rất ít hiệu quả (KHÔNG HỒI PHỤC - xơ gan tim).",
      "Trọng tâm thi cử: Phân định giữa suy tim còn hồi phục (Độ 3: gan đàn xếp còn co nhỏ) và suy tim không hồi phục (Độ 4: gan xơ cứng không thu nhỏ). Trẻ nhũ nhi có thể dùng thêm thang điểm Ross cải tiến (Ross I đến IV).")

add_b("Trình bày phác đồ số hóa nhanh liều tấn công và liều duy trì của Digoxin?",
      "Liều tấn công: 0,04 - 0,06 mg/kg/ngày đường uống chia 3 lần cách 8 giờ: Lần 1 uống 1/2 tổng liều; Lần 2 (sau 8h) uống 1/4 tổng liều; Lần 3 (sau 8h tiếp) uống 1/4 tổng liều. Liều duy trì: 0,01 - 0,02 mg/kg/ngày chia 2 lần cách nhau 12 giờ.",
      "Tác dụng của Digoxin: Tăng co bóp (inotropic dương), chậm dẫn truyền AV (dromotropic âm), chậm nhịp xoang (chronotropic âm), tăng tính tự động thất (bathmotropic dương). Trước khi cho uống mỗi liều, điều dưỡng bắt buộc phải đếm nhịp tim qua ống nghe trọn 1 phút.")

add_b("Trình bày các bước điều trị ngộ độc Digoxin và quy tắc bù kali?",
      "5 bước: 1. Ngừng thuốc ngay lập tức, rửa dạ dày. 2. Lấy máu đo nồng độ Digoxin và điện giải (K, Na, Mg, Ca). 3. Theo dõi liên tục ĐTĐ. 4. Bù kali: Uống hoặc truyền dung dịch có nồng độ 40 mEq/lít, tốc độ tối đa 0,3 mEq/kg/giờ (chống chỉ định nếu block AV độ cao hoặc K+ > 5 mEq/L). 5. Điều trị loạn nhịp (Phenytoin hoặc Lidocain; dùng DigiFab nếu ngộ độc nặng đe dọa tính mạng).",
      "Tuyệt đối chống chỉ định sốc điện khử rung khi ngộ độc Digoxin vì dễ gây rung thất trơ tử vong. Kháng thể DigiFab gắn kết đặc hiệu với Digoxin tự do đào thải qua thận.")

add_b("Chỉ ra điểm đính chính quan trọng về liều Norepinephrin và hình ảnh X-quang trong giáo trình gốc?",
      "1. Liều Norepinephrin: Bản in giáo trình in nhầm là '0,25 - 1 mg/kg/phút', thực tế lâm sàng chuẩn xác bắt buộc phải là '0,25 - 1 µg/kg/phút' (microgam). 2. Phim X-quang nghiêng trái trong suy tim phải: Bản in gốc ghi nhầm 'thất trái giãn làm khoảng sáng sau tim hẹp lại', thực tế lâm sàng chuẩn xác là 'thất phải giãn làm khoảng sáng sau xương ức hẹp lại'.",
      "Đây là 2 cạm bẫy in ấn kinh điển trong giáo trình. Đi thi hoặc làm bài lâm sàng cần nhớ rõ con số chuẩn để không bị mất điểm oan và đảm bảo an toàn tuyệt đối khi kê đơn thuốc hồi sức.")

# Save both to release and master files
target_release.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
target_master.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(cards)} harmonized cards for PED-48 successfully at both release and master paths!")
