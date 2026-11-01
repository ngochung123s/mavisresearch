# -*- coding: utf-8 -*-
# PED-66 Suy giáp bẩm sinh — nguồn thẻ duy nhất (barem gốc, bản cô đọng ôn thi).
# Barem: PED-66_Suy_giap_bam_sinh_BAREM.md (Bài 53, mục 5.2 → 11). Mã mục barem ghi ở `extra`.


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý / triệu chứng
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / mốc
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc / xét nghiệm / tiêu chuẩn
    return _c("#51cf66", t)


def B(t):  # tên bệnh / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("🏛️ BAREM GỐC · GIÁO TRÌNH NHI BÀI 53", "badge-barem")
SRC = ("📖 Nguồn: Giáo trình Nhi khoa — Chương 5. Thận – Nội tiết, Bài 53. Suy giáp bẩm sinh "
       "(ảnh chụp tr. 710–716, nhận qua Telegram 29/10/2026). Barem mục: ")
TAG = ["PED-66", "Barem-goc"]


def basic(cid, section, category, tier, front, core, ai, barem, tags, asks=None):
    card = {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": SRC + barem,
        "tags": TAG + tags,
    }
    if asks:
        card["asks"] = asks
    return card


def algo(cid, section, category, title, core, ai, barem, tags):
    card = basic(cid, section, category, 1, "⚡ THUẬT TOÁN QUYẾT ĐỊNH — " + B(title), core, ai, barem,
                 tags + ["Thuat-toan"])
    card.pop("badge")
    card.pop("badge_class")
    return card


def cloze(cid, section, category, text, barem, tags):
    return {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "cloze", "section": section, "category": category, "tier": 2,
        "text": text, "extra": SRC + barem,
        "tags": TAG + ["Cloze-phu"] + tags,
    }


cards_data = [
    # ------------------------------------------------------------ S1. Nguyên nhân (5.2)
    basic(
        "PED66-S1-01", "S1", "Nguyên nhân", 1,
        f"{B('[Nguyên nhân SGBS]')} Kể {Y('3 nhóm')} nguyên nhân sinh bệnh của suy giáp bẩm sinh và tỉ lệ của 2 nhóm chính.",
        f"1) {B('Loạn sản tuyến giáp')}: {Y('80–90%')} — hay gặp nhất.<br>"
        f"2) {B('Rối loạn tổng hợp hormon giáp')}: {Y('10–15%')}.<br>"
        f"3) {B('Nhóm khác')}: tuyến không đáp ứng TSH, mô đề kháng hormon giáp, do mẹ trong thai kỳ.",
        "Nhớ theo trục: tuyến không có/không đúng chỗ (loạn sản) → có tuyến nhưng không làm ra hormon (rối loạn tổng hợp) "
        "→ có hormon nhưng thụ thể hỏng hoặc bị yếu tố từ mẹ ức chế.",
        "5.2", ["Nguyen-nhan"],
    ),
    basic(
        "PED66-S1-02", "S1", "Nguyên nhân", 1,
        f"{B('[Loạn sản tuyến giáp]')} Kể {Y('3 thể')} loạn sản tuyến giáp, tỉ lệ và đặc điểm từng thể.",
        f"1) {B('Bất sản')}: {Y('30%')}, không tìm thấy mô giáp, {R('khởi bệnh sớm và nặng')}.<br>"
        f"2) {B('Giảm sản')}: {Y('15%')}, tuyến giáp teo nhỏ.<br>"
        f"3) {B('Lạc chỗ')}: {Y('55%')} (nhiều nhất), thường ở {B('đáy lưỡi')}.",
        "Lạc chỗ là thể gặp nhiều nhất nhưng còn ít mô giáp nên thường phát hiện muộn; bất sản không còn mô giáp "
        "nên biểu hiện sớm và nặng nhất.",
        "5.2", ["Nguyen-nhan", "Loan-san"],
    ),
    basic(
        "PED66-S1-03", "S1", "Nguyên nhân", 1,
        f"{B('[Rối loạn tổng hợp hormon giáp]')} Nêu đặc điểm chung (bướu giáp, tính gia đình, kiểu di truyền) và kể "
        f"{Y('5 type')} kèm đặc điểm từng type.",
        f"<b>Đặc điểm chung</b>: {R('bướu giáp lan tỏa')}, có tính gia đình, di truyền {B('NST thường, lặn')}.<br>"
        f"1) {B('Type 1 – rối loạn gắn iod')}: độ tập trung iod phóng xạ tại tuyến {R('giảm/không có')}.<br>"
        f"2) {B('Type 2 – rối loạn hữu cơ hóa iod')} = {B('hội chứng Pendred')}: thiếu {G('peroxydase')}, "
        f"{R('bướu cổ gia đình + điếc')} (dây VIII).<br>"
        f"3) {B('Type 3 – rối loạn kết đôi tyrosin')}: chẩn đoán bằng {G('sinh thiết phân tích hợp chất có iod')} tại tuyến.<br>"
        f"4) {B('Type 4 – thiếu deiodinase')}: {R('mất iodotyrosin qua nước tiểu')}.<br>"
        f"5) {B('Type 5 – tạo iodoprotein')}: iod gắn protein bất thường → hormon bất hoạt ({B('thyroalbumin')}).",
        "5 type đi theo đúng chuỗi tổng hợp: bắt iod → hữu cơ hóa → kết đôi → tái chế iod (deiodinase) → hormon thành phẩm. "
        "Tuyến vẫn còn và bị TSH kích thích liên tục nên nhóm này có bướu, khác với loạn sản.",
        "5.2", ["Nguyen-nhan", "Tong-hop-hormon"],
    ),
    basic(
        "PED66-S1-04", "S1", "Nguyên nhân", 2,
        f"{B('[Nguyên nhân khác]')} Ngoài loạn sản và rối loạn tổng hợp, kể {Y('3')} nguyên nhân khác của suy giáp bẩm sinh.",
        f"1) {R('Tuyến không đáp ứng TSH')} do thiếu thụ thể TSH tại tuyến ({Y('thường không có bướu')}).<br>"
        f"2) {R('Mô giảm đáp ứng hormon giáp')} do thiếu thụ thể hormon.<br>"
        f"3) {R('Do mẹ trong thai kỳ')}: dùng {G('thuốc kháng giáp trạng, thuốc có iod')}; {Y('2%')} do "
        f"{B('kháng thể TRAb')} từ mẹ qua nhau thai.",
        "Thiếu thụ thể TSH thì tuyến không bị kích thích phát triển nên không có bướu. Nhóm do mẹ thường gây suy giáp thoáng qua "
        "(xem thẻ xét nghiệm TRAb).",
        "5.2", ["Nguyen-nhan"],
    ),
    cloze(
        "PED66-S1-C1", "S1", "Nguyên nhân",
        f"Loạn sản tuyến giáp chiếm {{{{c1::{Y('80–90%')}}}}} suy giáp bẩm sinh: bất sản {{{{c2::{Y('30%')}}}}}, "
        f"giảm sản {{{{c3::{Y('15%')}}}}}, lạc chỗ {{{{c4::{Y('55%')}}}}}. Rối loạn tổng hợp hormon giáp chiếm "
        f"{{{{c5::{Y('10–15%')}}}}}.",
        "5.2", ["So-lieu"],
    ),
    cloze(
        "PED66-S1-C2", "S1", "Nguyên nhân",
        f"Tuyến giáp lạc chỗ thường nằm ở {{{{c1::{B('đáy lưỡi')}}}}}.",
        "5.2", ["Loan-san"],
    ),
    cloze(
        "PED66-S1-C3", "S1", "Nguyên nhân",
        f"Hội chứng {{{{c1::{B('Pendred')}}}}} là rối loạn hữu cơ hóa iod (type 2) do thiếu men {{{{c2::{G('peroxydase')}}}}}.",
        "5.2", ["Tong-hop-hormon"],
    ),

    # ------------------------------------------------------------ S2. Yếu tố nguy cơ (5.3)
    basic(
        "PED66-S2-01", "S2", "Yếu tố nguy cơ", 1,
        f"{B('[Yếu tố nguy cơ loạn sản tuyến giáp]')} Nêu yếu tố nguy cơ về {Y('khí hậu, chủng tộc, giới, bệnh lý của mẹ và HLA')}.",
        f"1) Khí hậu: tăng vào {Y('mùa thu, đông')}.<br>"
        f"2) Chủng tộc: {Y('da đen mắc ít hơn da trắng')}.<br>"
        f"3) Giới: hay gặp ở {Y('trẻ gái')}.<br>"
        f"4) Mẹ: {R('mẹ bệnh tự miễn')}, mẹ hoặc người trong gia đình {R('có bệnh tuyến giáp')}.<br>"
        f"5) {B('HLA AW24')}: nguy cơ tăng {Y('6–8 lần')}.",
        "Mẹo nhớ “Thu-đông, Trắng, Gái, Mẹ tự miễn, AW24”. Yếu tố mẹ tự miễn cũng là lý do hỏi tiền sử tuyến giáp của mẹ "
        "khi chẩn đoán sớm.",
        "5.3", ["Nguy-co"],
    ),
    basic(
        "PED66-S2-02", "S2", "Yếu tố nguy cơ", 2,
        f"{B('[Yếu tố làm nặng suy giáp]')} Suy giáp nặng hơn khi trẻ ở tình trạng nào và tiếp xúc những chất kháng giáp nào "
        f"(thức ăn, dược chất)?",
        f"1) Tình trạng trẻ: {R('đói')}, {R('bệnh mạn tính đường tiết niệu, tiêu hóa')}.<br>"
        f"2) Thức ăn kháng giáp: {R('họ cải, khoai mì')}.<br>"
        f"3) Dược chất: {R('PTU, PAS, steroid')}.",
        "Họ cải và khoai mì chứa chất sinh bướu (goitrogen) cạnh tranh bắt iod; PTU ức chế tổng hợp hormon. Thiếu dinh dưỡng "
        "và bệnh mạn làm giảm dự trữ, nên suy giáp lộ rõ hơn.",
        "5.3", ["Nguy-co"],
    ),
    cloze(
        "PED66-S2-C1", "S2", "Yếu tố nguy cơ",
        f"Người mang {{{{c1::{B('HLA AW24')}}}}} có nguy cơ suy giáp bẩm sinh tăng {{{{c2::{Y('6–8 lần')}}}}}.",
        "5.3", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S3. Sinh lý bệnh (6)
    basic(
        "PED66-S3-01", "S3", "Sinh lý bệnh", 1,
        f"{B('[Phân loại sinh lý bệnh]')} Phân loại suy giáp thành {Y('3 loại')} theo vị trí tổn thương và nêu thay đổi TSH của từng loại.",
        f"1) {B('Tiên phát')}: tổn thương {B('tại tuyến giáp')} → {R('TSH tăng')}.<br>"
        f"2) {B('Thứ phát')}: tổn thương {B('tuyến yên')} → {Y('TSH giảm')}.<br>"
        f"3) {B('Đệ tam cấp')}: tổn thương {B('vùng dưới đồi')} → {Y('TSH giảm')}.",
        "Thứ phát và đệ tam cấp gộp là suy giáp do tổn thương ở não (trung ương): não không phát lệnh nên TSH thấp. "
        "Đây là lý do tầm soát chỉ bằng TSH sẽ bỏ sót suy giáp trung ương.",
        "6", ["Sinh-ly-benh"],
    ),
    basic(
        "PED66-S3-02", "S3", "Sinh lý bệnh", 2,
        f"{B('[Bướu giáp trong SGBS]')} Đa số suy giáp bẩm sinh có bướu giáp không? Kể {Y('2')} ngoại lệ có bướu.",
        f"{Y('Đa số KHÔNG có bướu giáp')}, trừ:<br>1) {B('Rối loạn tổng hợp hormon giáp')}.<br>2) {B('Kháng T4 ở ngoại vi')}.",
        "Bướu chỉ xuất hiện khi còn mô giáp bị TSH kích thích kéo dài. Loạn sản (không có hoặc ít mô) thì không có bướu.",
        "6", ["Sinh-ly-benh"],
    ),
    basic(
        "PED66-S3-03", "S3", "Sinh lý bệnh", 1,
        f"{B('[Hậu quả thiếu hormon giáp]')} Thiếu hormon giáp gây {Y('3')} hậu quả chính nào?",
        f"1) {R('Chậm phát triển hệ xương và thần kinh')}.<br>2) {R('Giảm chuyển hóa tế bào')}.<br>"
        f"3) {R('Thâm nhiễm chất dạng nhầy')} ở da, niêm mạc và các cơ quan (phù niêm).",
        "Ba hậu quả này giải thích toàn bộ lâm sàng: lùn, chậm cốt hóa, chậm trí tuệ (1); lạnh, chậm nhịp tim, táo bón (2); "
        "mặt phù, lưỡi to, giọng khàn (3).",
        "6", ["Sinh-ly-benh"],
    ),

    # ------------------------------------------------------------ S4. Lâm sàng phát hiện sớm (7.1)
    basic(
        "PED66-S4-01", "S4", "Lâm sàng sơ sinh", 1,
        f"{B('[SGBS thời kỳ sơ sinh]')} Suy giáp phát hiện sớm (năm đầu) thường do nguyên nhân gì? Tỉ lệ sơ sinh không/ít triệu chứng "
        f"và lý do?",
        f"1) Nguyên nhân thường gặp: {B('bất sản tuyến giáp')}.<br>"
        f"2) Tỉ lệ: {Y('95%')} sơ sinh không có hoặc rất ít triệu chứng.<br>"
        f"3) Lý do: {B('T4 của mẹ qua nhau thai')} → chẩn đoán lâm sàng khó.",
        "Vì lâm sàng sơ sinh gần như im lặng, không thể chờ triệu chứng; phải dựa vào sàng lọc sơ sinh.",
        "7.1, 7.1.1", ["Lam-sang"], asks=["nguyên nhân", "tỉ lệ", "lý do"],
    ),
    basic(
        "PED66-S4-02", "S4", "Lâm sàng sơ sinh", 1,
        f"{B('[Triệu chứng giai đoạn sơ sinh]')} Kể các triệu chứng suy giáp bẩm sinh ở thời kỳ sơ sinh (giai đoạn khởi đầu).",
        f"1) Lúc sinh: {R('cân nặng lớn')} (do phù niêm), {R('vòng đầu lớn')}, có thể {R('nhịp tim giảm')}.<br>"
        f"2) Hành vi: {R('ngủ nhiều, biếng ăn, ít cử động, ít khóc')}.<br>"
        f"3) Toàn thân: {R('giọng khàn, thân nhiệt giảm, da lạnh khô')}.<br>"
        f"4) Khám: {R('vàng da kéo dài, thóp rộng, mặt tròn, lưỡi to, táo bón, giảm trương lực cơ')}.",
        "Trẻ “ngoan bất thường”: ngủ nhiều, ít khóc, ít đòi ăn — kèm vàng da kéo dài và táo bón là bộ ba cần nghĩ ngay tới suy giáp.",
        "7.1.1", ["Lam-sang", "So-sinh"],
    ),
    basic(
        "PED66-S4-03", "S4", "Lâm sàng toàn phát", 1,
        f"{B('[Giai đoạn toàn phát]')} Từ tháng thứ 2 trở đi, suy giáp bẩm sinh có {Y('3 nhóm')} triệu chứng chính nào và "
        f"các triệu chứng kèm theo nào?",
        f"1) {R('Thay đổi da niêm')}.<br>2) {R('Chậm phát triển thể chất, vận động và tâm thần')}.<br>"
        f"3) {R('Không có tuyến giáp')}.<br>Kèm theo: {R('tim to, nhịp tim chậm, thiếu máu')}.",
        "Da niêm = thâm nhiễm nhầy; chậm phát triển = thiếu hormon cho xương và não; không sờ thấy tuyến vì nguyên nhân chủ yếu là loạn sản.",
        "7.1.2", ["Lam-sang", "Toan-phat"],
    ),
    basic(
        "PED66-S4-04", "S4", "Lâm sàng toàn phát", 1,
        f"{B('[Thay đổi da niêm]')} Mô tả thay đổi da niêm ở giai đoạn toàn phát (phù niêm, da, mặt, cổ).",
        f"1) Phù niêm: {R('rõ dần ở mặt, chi')}.<br>2) Da: {R('dày, khô, lạnh, có vân tím')}.<br>"
        f"3) Mặt: {R('tròn, mí mắt phù, mũi xẹp, môi dày, lưỡi to thè ra, chân tóc thấp')}, {R('giọng khàn')}.<br>"
        f"4) Cổ: {R('to, ngắn, tụ mỡ trên xương đòn, cổ và vai')}.",
        "Tất cả là hậu quả thâm nhiễm chất dạng nhầy. Lưỡi to thè ra và giọng khàn cũng do niêm mạc lưỡi, thanh quản bị phù niêm.",
        "7.1.2", ["Lam-sang", "Da-niem"],
    ),
    basic(
        "PED66-S4-05", "S4", "Lâm sàng toàn phát", 1,
        f"{B('[Chậm phát triển]')} Mô tả chậm phát triển thể chất, vận động và tâm thần ở giai đoạn toàn phát.",
        f"1) Mức độ: {Y('nặng dần theo tuổi')}.<br>2) Thể chất: {R('chậm lớn, lùn, chi ngắn mập')}.<br>"
        f"3) Vận động: {R('thóp chậm đóng, chậm mọc răng, trương lực cơ giảm, chậm biết đi đứng, ít hoạt động')}.<br>"
        f"4) Tâm thần: {R('ít chú ý, trí khôn kém, phát âm khó')}.",
        "Lùn do thiếu hormon giáp là lùn không cân đối (chi ngắn so với thân), khác lùn do dinh dưỡng. Càng để lâu tổn thương não càng không hồi phục.",
        "7.1.2", ["Lam-sang", "Cham-phat-trien"],
    ),
    basic(
        "PED66-S4-06", "S4", "Diễn tiến", 1,
        f"{B('[Diễn tiến SGBS]')} Diễn tiến của trẻ khi điều trị {Y('trước 3 tháng tuổi')}, khi {R('không điều trị')} và khi {R('điều trị muộn')}?",
        f"1) Điều trị trước 3 tháng tuổi: {G('phát triển bình thường thể chất và tinh thần')}.<br>"
        f"2) Không điều trị: {R('tử vong')} do {R('hôn mê phù niêm, nhiễm trùng, tắc nghẽn đường hô hấp')}.<br>"
        f"3) Điều trị muộn: {R('di chứng nặng nề tâm thần và thể chất')}.",
        "Mốc 3 tháng là “cửa sổ vàng” của não; đây cũng là mốc nguyên tắc điều trị và mốc chẩn đoán sớm khi không được tầm soát.",
        "7.1.3", ["Dien-tien", "Tien-luong"],
        asks=["điều trị trước 3 tháng tuổi", "không điều trị", "điều trị muộn"],
    ),
    cloze(
        "PED66-S4-C2", "S4", "Lâm sàng sơ sinh",
        f"Biểu hiện lâm sàng suy giáp bẩm sinh thay đổi tùy theo {{{{c1::{Y('nguyên nhân, mức độ và thời gian bị bệnh')}}}}}.",
        "7", ["Lam-sang"],
    ),
    cloze(
        "PED66-S4-C1", "S4", "Lâm sàng sơ sinh",
        f"{{{{c1::{Y('95%')}}}}} trẻ sơ sinh suy giáp bẩm sinh không có hoặc có rất ít triệu chứng; điều trị trước "
        f"{{{{c2::{Y('3 tháng tuổi')}}}}} thì trẻ phát triển bình thường.",
        "7.1.1, 7.1.3", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S5. Phát hiện muộn (7.2)
    basic(
        "PED66-S5-01", "S5", "Phát hiện muộn", 1,
        f"{B('[Suy giáp phát hiện muộn]')} Nêu nguyên nhân thường gặp, dự hậu và triệu chứng chủ yếu.",
        f"1) Nguyên nhân: {B('tuyến giáp lạc chỗ')} hoặc {B('rối loạn tổng hợp hormon giáp')}.<br>"
        f"2) Dự hậu: {G('tốt hơn')} thể phát hiện sớm.<br>"
        f"3) Triệu chứng: {R('chậm phát triển thể chất')} (lùn không cân đối, đầu to, nét mặt thô) và {R('chậm phát triển tinh thần')}.",
        "Hai nguyên nhân này còn mô giáp tạo một phần hormon nên bệnh lộ muộn và nhẹ hơn bất sản.",
        "7.2", ["Phat-hien-muon"], asks=["nguyên nhân", "dự hậu", "triệu chứng"],
    ),
    basic(
        "PED66-S5-02", "S5", "Phát hiện muộn", 2,
        f"{B('[Dị tật kèm theo]')} Tỉ lệ trẻ suy giáp bẩm sinh có dị tật kèm theo và các cơ quan hay gặp?",
        f"1) Tỉ lệ: gần {Y('8,4%')}.<br>2) Cơ quan: thường gặp nhất {R('tim, thận, tiêu hóa, hệ xương')}; "
        f"cũng ghi nhận {R('thần kinh, mắt, thính lực')}.",
        "Khi chẩn đoán SGBS cần khám toàn diện tìm dị tật tim, thận… vì gần 1/12 trẻ có dị tật đi kèm.",
        "7.2", ["Di-tat"], asks=["tỉ lệ", "cơ quan"],
    ),
    cloze(
        "PED66-S5-C1", "S5", "Phát hiện muộn",
        f"Gần {{{{c1::{Y('8,4%')}}}}} trẻ suy giáp bẩm sinh có dị tật kèm theo, thường gặp nhất là dị tật "
        f"{{{{c2::{R('tim, thận, tiêu hóa, hệ xương')}}}}}.",
        "7.2", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S6. Xét nghiệm (8)
    basic(
        "PED66-S6-01", "S6", "Xét nghiệm máu", 1,
        f"{B('[Xét nghiệm máu thường quy]')} Kết quả T3/T4, TSH, công thức máu, cholesterol và đường huyết trong suy giáp bẩm sinh?",
        f"1) T3, T4: {R('giảm')} (mức thay đổi T4 tùy nguyên nhân, thời gian bệnh).<br>"
        f"2) TSH: {R('tăng')} trong tiên phát, {Y('giảm')} trong thứ phát.<br>"
        f"3) Công thức máu: {R('thiếu máu đẳng sắc đẳng bào')}.<br>"
        f"4) Cholesterol: {R('tăng')} (ở trẻ {Y('> 2 tuổi')}).<br>"
        f"5) Đường huyết: {R('giảm')}.",
        "Giảm chuyển hóa → giảm tạo hồng cầu (thiếu máu), giảm thoái hóa cholesterol (tăng), giảm tân tạo đường (hạ đường huyết).",
        "8.1", ["Xet-nghiem"],
    ),
    basic(
        "PED66-S6-02", "S6", "Xét nghiệm máu", 1,
        f"{B('[Xét nghiệm chuyên sâu]')} Nêu chỉ định và ý nghĩa của {G('kháng thể TRAb')}, {G('thyroglobulin huyết thanh')} và "
        f"{G('iod niệu')}.",
        f"1) {G('TRAb')}: sơ sinh có {R('mẹ bệnh tự miễn tuyến giáp')} hoặc {R('anh chị em suy giáp thoáng qua')} → chẩn đoán "
        f"{B('SGBS thoáng qua')}.<br>"
        f"2) {G('Thyroglobulin')}: phân biệt nguyên nhân — {R('không có tuyến')} trên hình ảnh + Tg thấp = {B('bất sản')}; "
        f"{R('tuyến lớn')} + Tg thấp = {B('khiếm khuyết gen thyroglobulin')}.<br>"
        f"3) {G('Iod niệu')}: tiền sử {R('phơi nhiễm iod')} hoặc sinh ở {R('vùng bướu cổ địa phương')} → xác nhận thừa/thiếu iod.",
        "Tg là “dấu vết” của mô giáp: không có mô thì Tg thấp. Nếu tuyến to mà Tg vẫn thấp thì lỗi nằm ở gen tạo Tg.",
        "8.1", ["Xet-nghiem"],
    ),
    basic(
        "PED66-S6-03", "S6", "Hình ảnh & khác", 1,
        f"{B('[X-quang hệ xương]')} Hình ảnh X-quang xương trong suy giáp bẩm sinh và vị trí thường chụp?",
        f"1) Hình ảnh: {R('xương chậm trưởng thành')}, {R('điểm cốt hóa xuất hiện muộn')}, {R('loạn sản các đầu xương')}.<br>"
        f"2) Vị trí: {G('cổ tay – bàn tay')}.",
        "Tuổi xương chậm là dấu ấn khách quan của thiếu hormon giáp kéo dài; cũng dùng để theo dõi điều trị (mỗi 6 tháng).",
        "8.2", ["Xet-nghiem", "X-quang"],
    ),
    basic(
        "PED66-S6-04", "S6", "Hình ảnh & khác", 1,
        f"{B('[Xét nghiệm khác]')} Kết quả hoặc ý nghĩa của {G('siêu âm')}, {G('xạ hình tuyến giáp')}, {G('độ tập trung I131')} và "
        f"{G('điện tim')}?",
        f"1) Siêu âm: thường {R('không có tuyến giáp')}.<br>"
        f"2) Xạ hình: phát hiện {B('bất sản, giảm sản, lạc chỗ')}.<br>"
        f"3) Độ tập trung I131: chẩn đoán {B('rối loạn tổng hợp hormon giáp')}.<br>"
        f"4) Điện tim: {R('nhịp xoang chậm, điện thế thấp, PR dài')}.",
        "Xạ hình trả lời câu hỏi “tuyến ở đâu, còn bao nhiêu”; I131 trả lời “tuyến có bắt/giữ iod không”, nên dùng cho nhóm rối loạn tổng hợp.",
        "8.3", ["Xet-nghiem"],
    ),
    cloze(
        "PED66-S6-C1", "S6", "Hình ảnh & khác",
        f"Điện tim trong suy giáp bẩm sinh: {{{{c1::{R('nhịp xoang chậm, điện thế thấp, PR dài')}}}}}.",
        "8.3", ["Dien-tim"],
    ),
    cloze(
        "PED66-S6-C2", "S6", "Xét nghiệm máu",
        f"Cholesterol máu tăng trong suy giáp bẩm sinh ở trẻ {{{{c1::{Y('trên 2 tuổi')}}}}}; thiếu máu thường "
        f"{{{{c2::{R('đẳng sắc đẳng bào')}}}}}.",
        "8.1", ["Xet-nghiem"],
    ),

    # ------------------------------------------------------------ S7. Chẩn đoán xác định (9.1)
    basic(
        "PED66-S7-01", "S7", "Chẩn đoán xác định", 1,
        f"{B('[Chẩn đoán sớm khi không tầm soát]')} Trẻ không được tầm soát, chẩn đoán sớm trong {Y('3 tháng đầu')} dựa vào "
        f"{Y('3')} yếu tố nào? Kể các triệu chứng lâm sàng gợi ý.",
        f"1) {R('Tiền sử bệnh lý tuyến giáp của mẹ')}.<br>"
        f"2) {R('Triệu chứng lâm sàng')} gợi ý — {R('táo bón, vàng da kéo dài, phù niêm, chậm phát triển thể chất – tâm thần, thóp rộng, da nổi vân tím')}, "
        f"{R('cân nặng lúc sinh')} {Y('> 3.500 g')}.<br>"
        f"3) {G('Định lượng TSH, T4 hoặc TSH, FT4')}.",
        "Cách tốt nhất vẫn là chương trình tầm soát sơ sinh; 3 yếu tố này là “lưới an toàn” cho trẻ bị lọt sàng lọc.",
        "9.1", ["Chan-doan"],
    ),
    algo(
        "PED66-A1", "S7", "Chẩn đoán xác định", "Đọc kết quả TSH – FT4 ở trẻ nghi suy giáp",
        f"1) {R('TSH tăng + FT4 giảm')} → {B('suy giáp')} → {G('điều trị ngay')}.<br>"
        f"2) {Y('TSH tăng + FT4 bình thường')} → {B('suy giáp dưới lâm sàng')} → xử trí theo ngưỡng TSH (thẻ ⚡ kế tiếp).<br>"
        f"3) {R('TSH bình thường/thấp + FT4 thấp')} → {B('suy giáp trung ương')} → {G('điều trị')}, "
        f"{Y('TRỪ')} trẻ {Y('sinh non')} hoặc có {Y('bệnh ngoài tuyến giáp')} giải thích được.<br>"
        f"⚠️ TSH, FT4 sơ sinh {Y('thay đổi theo ngày tuổi và phương pháp xét nghiệm')}.",
        "Đọc FT4 trước để biết có suy giáp thật không, rồi nhìn TSH để biết tổn thương ở tuyến (TSH cao) hay ở não (TSH không tăng). "
        "Sinh non và bệnh nặng ngoài tuyến giáp có thể làm FT4 thấp tạm thời nên là ngoại lệ.",
        "9.1", ["Chan-doan", "TSH-FT4"],
    ),
    algo(
        "PED66-A2", "S7", "Chẩn đoán xác định", "Suy giáp dưới lâm sàng (TSH tăng, FT4 bình thường): khi nào điều trị?",
        f"1) TSH {Y('> 20 mUI/mL')} → {G('bắt đầu điều trị')}.<br>"
        f"2) TSH {Y('6 – < 20 mUI/mL')} → {G('theo dõi sát lâm sàng, xét nghiệm lại sau 1 tuần')}.<br>"
        f"3) Sau {Y('4 tuần')} TSH vẫn {Y('> 10 mUI/mL')} → {G('khuyến cáo điều trị')}.",
        "Mẹo nhớ “20 – 6 – 1 – 4 – 10”: trên 20 làm ngay; 6 đến dưới 20 chờ 1 tuần thử lại; tới 4 tuần còn trên 10 thì điều trị.",
        "9.1", ["Chan-doan", "Duoi-lam-sang"],
    ),
    cloze(
        "PED66-S7-C3", "S7", "Chẩn đoán xác định",
        f"Để chẩn đoán sớm suy giáp bẩm sinh, tốt nhất là dựa vào {{{{c1::{G('chương trình tầm soát suy giáp sơ sinh')}}}}}.",
        "9.1", ["Chan-doan", "Sang-loc"],
    ),
    cloze(
        "PED66-S7-C1", "S7", "Chẩn đoán xác định",
        f"Suy giáp dưới lâm sàng: TSH {{{{c1::{Y('> 20 mUI/mL')}}}}} → điều trị; TSH {{{{c2::{Y('6 – < 20 mUI/mL')}}}}} → "
        f"xét nghiệm lại sau {{{{c3::{Y('1 tuần')}}}}}; sau {{{{c4::{Y('4 tuần')}}}}} TSH vẫn {{{{c5::{Y('> 10 mUI/mL')}}}}} → điều trị.",
        "9.1", ["So-lieu", "Duoi-lam-sang"],
    ),
    cloze(
        "PED66-S7-C2", "S7", "Chẩn đoán xác định",
        f"Cân nặng lúc sinh {{{{c1::{Y('trên 3.500 g')}}}}} là một dấu hiệu gợi ý suy giáp bẩm sinh khi trẻ không được tầm soát.",
        "9.1", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S8. Chẩn đoán phân biệt (9.2)
    basic(
        "PED66-S8-01", "S8", "Chẩn đoán phân biệt", 1,
        f"{B('[Chẩn đoán phân biệt]')} Phân biệt suy giáp bẩm sinh với {B('còi xương')}: đặc điểm lâm sàng và cận lâm sàng?",
        f"1) Lâm sàng: {Y('da không khô, không táo bón, tinh thần bình thường')}.<br>"
        f"2) Cận lâm sàng: {R('phosphatase kiềm tăng')}, {R('X-quang có hình ảnh còi xương')}.",
        "Còi xương cũng chậm phát triển xương, thóp rộng; nhưng không có “bộ mặt suy giáp” (da khô, táo bón, chậm trí tuệ).",
        "9.2", ["Phan-biet"], asks=["lâm sàng", "cận lâm sàng"],
    ),
    basic(
        "PED66-S8-02", "S8", "Chẩn đoán phân biệt", 1,
        f"{B('[Chẩn đoán phân biệt]')} Phân biệt suy giáp bẩm sinh với {B('hội chứng Down')}: đặc điểm lâm sàng và xét nghiệm xác định?",
        f"1) Lâm sàng: {R('bộ mặt đặc biệt')}; {Y('da không khô, không táo bón, thân nhiệt không hạ')}.<br>"
        f"2) Xét nghiệm: {G('NST đồ')} có {R('3 NST 21')}.",
        "Down cũng lưỡi to, giảm trương lực, chậm trí tuệ nên dễ nhầm; điểm khác là không có dấu giảm chuyển hóa (da khô, lạnh, táo bón).",
        "9.2", ["Phan-biet"], asks=["lâm sàng", "xét nghiệm"],
    ),
    basic(
        "PED66-S8-03", "S8", "Chẩn đoán phân biệt", 1,
        f"{B('[Chẩn đoán phân biệt]')} Phân biệt suy giáp bẩm sinh với {B('lùn ngắn xương chi')}: đặc điểm chi, bàn tay và da – tinh thần?",
        f"1) Chi: {R('các chi ngắn')}.<br>2) Bàn tay: {R('bàn tay, chân vuông; ngón tay hình chĩa ba')}.<br>"
        f"3) Da – tinh thần: {Y('da không khô, tinh thần bình thường')}.",
        "Cả ba chẩn đoán phân biệt có chung “mẫu số”: da không khô và tinh thần bình thường — hai điểm chống lại suy giáp.",
        "9.2", ["Phan-biet"],
    ),

    # ------------------------------------------------------------ S9. Sàng lọc (9.3)
    basic(
        "PED66-S9-01", "S9", "Sàng lọc", 1,
        f"{B('[Sàng lọc SGBS]')} Sàng lọc suy giáp bẩm sinh thực hiện vào thời điểm nào và lấy mẫu bằng cách nào?",
        f"1) Thời điểm: {Y('2–5 ngày sau sinh')}.<br>"
        f"2) Cách lấy: {G('máu gót chân nhỏ vào giấy thấm')} → gửi phòng xét nghiệm.",
        "Không lấy quá sớm (ngày đầu) vì TSH tăng sinh lý ngay sau sinh dễ gây dương tính giả.",
        "9.3", ["Sang-loc"],
    ),
    basic(
        "PED66-S9-02", "S9", "Sàng lọc", 1,
        f"{B('[3 chiến lược tầm soát]')} Kể {Y('3')} chiến lược tầm soát suy giáp bẩm sinh và nhược điểm của từng chiến lược.",
        f"1) {G('T4 trước')} → thử TSH nếu T4 thấp ({Y('< bách phân vị 10')}): {R('bỏ sót suy giáp dưới lâm sàng')}.<br>"
        f"2) {G('TSH trước')} → thử T4 nếu TSH tăng: {R('bỏ sót suy giáp trung ương')}.<br>"
        f"3) {G('Cả T4 và TSH')}: phát hiện cả tiên phát lẫn trung ương nhưng {R('tăng dương tính giả')}.",
        "Suy giáp dưới lâm sàng có T4 bình thường nên lọt qua chiến lược T4; suy giáp trung ương có TSH không tăng nên lọt qua chiến lược TSH.",
        "9.3", ["Sang-loc"],
    ),
    basic(
        "PED66-S9-03", "S9", "Sàng lọc", 2,
        f"{B('[Sàng lọc tại Việt Nam]')} Việt Nam sàng lọc suy giáp bẩm sinh bằng xét nghiệm gì, vào ngày nào, bắt đầu ở đâu và năm nào?",
        f"1) Xét nghiệm: {G('TSH')}.<br>2) Ngày: {Y('ngày 2–5 sau sinh')}.<br>"
        f"3) Bắt đầu: {B('Hà Nội')} năm {Y('2000')}, {B('TP. Hồ Chí Minh')} năm {Y('2002')}.",
        "Việt Nam dùng chiến lược TSH trước, nên cần nhớ nhược điểm của nó là bỏ sót suy giáp trung ương.",
        "9.3", ["Sang-loc", "Viet-Nam"], asks=["xét nghiệm", "ngày", "bắt đầu"],
    ),
    cloze(
        "PED66-S9-C1", "S9", "Sàng lọc",
        f"Sàng lọc SGBS lấy máu gót chân vào ngày {{{{c1::{Y('2–5')}}}}} sau sinh; chiến lược T4 trước thử TSH khi T4 dưới bách phân vị "
        f"{{{{c2::{Y('thứ 10')}}}}}. Việt Nam bắt đầu ở Hà Nội năm {{{{c3::{Y('2000')}}}}}, TP. HCM năm {{{{c4::{Y('2002')}}}}}.",
        "9.3", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S10. Phân cấp chẩn đoán (9.4)
    basic(
        "PED66-S10-01", "S10", "Phân cấp chẩn đoán", 1,
        f"{B('[Phân cấp chẩn đoán]')} Nhiệm vụ chẩn đoán suy giáp bẩm sinh ở {B('tuyến cơ sở')}, {B('bệnh viện huyện')} và "
        f"{B('tuyến tỉnh, thành phố')}?",
        f"1) {B('Tuyến cơ sở')} (trạm y tế, nhà hộ sinh): phát hiện dấu hiệu nghi ngờ ({R('vẻ mặt, táo bón, vàng da kéo dài')}) → "
        f"{G('chuyển sớm đến cơ sở sàng lọc')}.<br>"
        f"2) {B('Bệnh viện huyện')}: {G('sàng lọc TSH trên giấy')} + {G('công thức máu, đường huyết, ECG, X-quang xương')} (tìm điểm cốt hóa) → "
        f"chuyển chuyên khoa.<br>"
        f"3) {B('Tuyến tỉnh, thành phố')}: {G('TSH, T4; siêu âm, xạ hình tuyến giáp')} → chẩn đoán nguyên nhân và "
        f"{G('điều trị càng sớm càng tốt')}.",
        "Tuyến dưới phát hiện và chuyển, tuyến huyện sàng lọc và đánh giá hậu quả, tuyến tỉnh tìm nguyên nhân và điều trị.",
        "9.4", ["Phan-cap"],
    ),

    # ------------------------------------------------------------ S11. Điều trị (10, 10.1, 10.2)
    basic(
        "PED66-S11-01", "S11", "Nguyên tắc điều trị", 1,
        f"{B('[Mục đích & nguyên tắc điều trị]')} Nêu mục đích điều trị và {Y('5')} nguyên tắc điều trị suy giáp bẩm sinh.",
        f"<b>Mục đích</b>: {G('đạt nhanh bình giáp và duy trì')} để trẻ phát triển tâm thần, vận động, thể chất bình thường.<br>"
        f"1) {G('Càng sớm càng tốt')}, trước {Y('3 tháng tuổi')}, tốt nhất {Y('tháng đầu sau sinh')}.<br>"
        f"2) {G('Hormon giáp liên tục, suốt đời')}.<br>"
        f"3) {G('Liều theo cơ địa và giai đoạn phát triển')}.<br>"
        f"4) Giữ {Y('T4 > 8 µg/dL')}.<br>"
        f"5) {G('Điều trị hỗ trợ và phục hồi chức năng')}.",
        "Mẹo nhớ “Sớm – Suốt đời – Đúng liều – T4 trên 8 – Phục hồi chức năng”. Ngưỡng T4 > 8 cũng là tiêu chuẩn xuất viện.",
        "10, 10.1", ["Dieu-tri"],
    ),
    basic(
        "PED66-S11-02", "S11", "Phác đồ LT4", 1,
        f"{B('[Mục tiêu điều trị]')} Mục tiêu điều trị ban đầu và mục tiêu sau đó khi dùng LT4?",
        f"1) Ban đầu: {Y('T4 > 10 µg/dL (> 129 nmol/L)')} hoặc {Y('FT4 ở nửa trên ngưỡng bình thường theo tuổi')}, càng sớm càng tốt.<br>"
        f"2) Sau đó: {G('bình thường hóa TSH')}, thường {Y('2–4 tuần')} sau điều trị.",
        "FT4/T4 lên nhanh trong vài ngày, còn TSH giảm chậm hơn (vài tuần) vì trục yên–giáp cần thời gian thích nghi.",
        "10.2", ["Dieu-tri", "Muc-tieu"],
    ),
    algo(
        "PED66-A3", "S11", "Phác đồ LT4", "Bảng liều Levothyroxine (LT4) bỏ túi theo tuổi",
        f"Cách dùng: {G('LT4 uống 1 lần duy nhất buổi sáng')}, liều {Y('giảm dần theo tuổi')}.<br>"
        f"1) Sơ sinh: {Y('10–15 µg/kg/ngày')} ({R('chú ý tim mạch')}); thể nhẹ {Y('8–12 µg/kg/ngày')}.<br>"
        f"2) 1–3 tháng: {Y('8 µg/kg/ngày')} → sau đó {Y('5–6 µg/kg/ngày')} đến 1 tuổi.<br>"
        f"3) 1–3 tuổi: {Y('4–6 µg/kg/ngày')}.<br>"
        f"4) 3–10 tuổi: {Y('3–5 µg/kg/ngày')}.<br>"
        f"5) > 10 tuổi: {Y('2–4 µg/kg/ngày')}.",
        "Mẹo nhớ dãy giảm dần “10–15 → 8 → 5–6 → 4–6 → 3–5 → 2–4”. Liều/kg cao nhất ở sơ sinh vì nhu cầu hormon cho não lớn nhất, "
        "nhưng liều cao dễ gây nhịp nhanh nên phải kiểm tra tim mạch.",
        "10.2", ["Dieu-tri", "LT4", "Lieu"],
    ),
    cloze(
        "PED66-S11-C1", "S11", "Phác đồ LT4",
        f"Liều LT4: sơ sinh {{{{c1::{Y('10–15 µg/kg/ngày')}}}}}; 1–3 tháng {{{{c2::{Y('8 µg/kg/ngày')}}}}} rồi "
        f"{{{{c3::{Y('5–6 µg/kg/ngày')}}}}} đến 1 tuổi; 1–3 tuổi {{{{c4::{Y('4–6 µg/kg/ngày')}}}}}; 3–10 tuổi "
        f"{{{{c5::{Y('3–5 µg/kg/ngày')}}}}}; trên 10 tuổi {{{{c6::{Y('2–4 µg/kg/ngày')}}}}}.",
        "10.2", ["So-lieu", "LT4"],
    ),
    cloze(
        "PED66-S11-C2", "S11", "Phác đồ LT4",
        f"Mục tiêu ban đầu: T4 {{{{c1::{Y('> 10 µg/dL (> 129 nmol/L)')}}}}}; TSH thường bình thường hóa "
        f"{{{{c2::{Y('2–4 tuần')}}}}} sau điều trị. Nguyên tắc: luôn giữ T4 {{{{c3::{Y('> 8 µg/dL')}}}}}.",
        "10.1, 10.2", ["So-lieu", "Muc-tieu"],
    ),

    # ------------------------------------------------------------ S12. Phân cấp điều trị & theo dõi (10.3)
    basic(
        "PED66-S12-01", "S12", "Theo dõi tuyến tỉnh", 1,
        f"{B('[Tuyến tỉnh: đánh giá đáp ứng]')} Thời gian đầu điều trị ở đâu và dấu hiệu nào cho thấy điều trị có hiệu quả?",
        f"1) Thời gian đầu: {G('nằm viện')} để đánh giá hiệu quả.<br>"
        f"2) Hiệu quả: {G('hết táo bón, nhịp tim tăng, ăn ngon, bớt phù mặt, linh hoạt hơn')}.",
        "Các dấu hiệu hiệu quả là đảo ngược trực tiếp triệu chứng giảm chuyển hóa (táo bón, nhịp chậm, biếng ăn, phù niêm, chậm chạp).",
        "10.3", ["Theo-doi"],
    ),
    basic(
        "PED66-S12-02", "S12", "Theo dõi tuyến tỉnh", 1,
        f"{B('[Tuyến tỉnh: lịch theo dõi]')} Thời điểm kiểm tra lại hormon, tiêu chuẩn xuất viện và lịch tái khám?",
        f"1) Kiểm tra lại hormon: {Y('2 và 4 tuần')} sau khi bắt đầu điều trị.<br>"
        f"2) Xuất viện khi: {Y('TSH < 10 µU/mL')} và {Y('T4 > 8 µg/dL')}.<br>"
        f"3) Tái khám: {Y('mỗi 3 tháng')} trong năm đầu, {Y('mỗi 6 tháng')} sau đó.",
        "Mốc 2–4 tuần trùng với thời gian TSH cần để bình thường hóa (mục tiêu điều trị).",
        "10.3", ["Theo-doi"], asks=["kiểm tra lại hormon", "xuất viện", "tái khám"],
    ),
    basic(
        "PED66-S12-03", "S12", "Theo dõi tuyến tỉnh", 1,
        f"{B('[Tuyến tỉnh: nội dung theo dõi]')} Kể các vấn đề cần theo dõi, khi nào gọi là điều trị không tốt, và tác dụng phụ "
        f"khi quá liều.",
        f"1) Theo dõi: {G('cân nặng, chiều cao, phát triển vận động tâm thần, TSH, T4')}; {G('tuổi xương mỗi 6 tháng')}; "
        f"{G('bú mẹ càng lâu càng tốt')}.<br>"
        f"2) Điều trị không tốt: {R('trên 2 lần T4 < 8 µg/dL')}.<br>"
        f"3) Quá liều: {R('nhịp tim nhanh, khó ngủ, quấy, tiêu chảy, tăng calci niệu')}.",
        "Tác dụng phụ quá liều chính là biểu hiện cường giáp: tăng chuyển hóa → tim nhanh, kích thích, đi ngoài nhiều.",
        "10.3", ["Theo-doi"], asks=["theo dõi", "điều trị không tốt", "quá liều"],
    ),
    basic(
        "PED66-S12-04", "S12", "Theo dõi tuyến huyện", 1,
        f"{B('[Tuyến huyện và cơ sở]')} Lịch tái khám, dấu hiệu không đủ liều, tương tác thuốc cần chú ý và bệnh kèm cần xử trí?",
        f"1) Tái khám: {Y('mỗi tháng')} trong năm đầu (phát hiện quá liều hoặc không đủ liều).<br>"
        f"2) Không đủ liều: {R('táo bón, chậm lên cân, giảm hoạt động, biếng ăn')}.<br>"
        f"3) Tương tác: hormon giáp {R('tăng tác dụng thuốc chống đông')}; {R('thuốc chống co giật làm nặng suy giáp')}.<br>"
        f"4) Bệnh kèm: xử trí, {R('đặc biệt nhiễm trùng')}.",
        "Tuyến dưới tái khám dày hơn (mỗi tháng so với mỗi 3 tháng ở tuyến tỉnh) vì ít phương tiện xét nghiệm, phải dựa vào lâm sàng.",
        "10.3", ["Theo-doi", "Tuong-tac"], asks=["tái khám", "không đủ liều", "tương tác", "bệnh kèm"],
    ),
    algo(
        "PED66-A4", "S12", "Theo dõi", "Trẻ đang dùng LT4: thiếu liều hay quá liều?",
        f"1) {R('Thiếu liều')}: táo bón, chậm lên cân, giảm hoạt động, biếng ăn; hoặc {R('> 2 lần T4 < 8 µg/dL')} → "
        f"{G('đánh giá lại, tăng liều')}.<br>"
        f"2) {R('Quá liều')}: nhịp tim nhanh, khó ngủ, quấy, tiêu chảy, tăng calci niệu → {G('giảm liều')}.<br>"
        f"3) {G('Đạt')}: hết táo bón, nhịp tim tăng (về bình thường), ăn ngon, bớt phù mặt, linh hoạt; TSH < 10 µU/mL, T4 > 8 µg/dL → "
        f"{G('giữ liều, tái khám theo lịch')}.<br>"
        f"⚠️ Đang dùng {R('thuốc chống đông')} hoặc {R('thuốc chống co giật')} → theo dõi sát hơn.",
        "Thiếu liều = vẫn còn dấu giảm chuyển hóa; quá liều = dấu tăng chuyển hóa. Hai thuốc tương tác kéo lệch kết quả theo hai hướng: "
        "hormon giáp làm chống đông mạnh hơn, chống co giật làm suy giáp nặng hơn.",
        "10.3", ["Theo-doi", "LT4"],
    ),
    cloze(
        "PED66-S12-C1", "S12", "Theo dõi tuyến tỉnh",
        f"Cho xuất viện khi TSH {{{{c1::{Y('< 10 µU/mL')}}}}} và T4 {{{{c2::{Y('> 8 µg/dL')}}}}}; kiểm tra hormon lại sau "
        f"{{{{c3::{Y('2 và 4 tuần')}}}}}; tuổi xương mỗi {{{{c4::{Y('6 tháng')}}}}}.",
        "10.3", ["So-lieu"],
    ),
    cloze(
        "PED66-S12-C2", "S12", "Theo dõi",
        f"Tuyến tỉnh tái khám mỗi {{{{c1::{Y('3 tháng')}}}}} trong năm đầu rồi mỗi {{{{c2::{Y('6 tháng')}}}}} sau đó. "
        f"Tuyến huyện và cơ sở tái khám mỗi {{{{c3::{Y('tháng')}}}}} trong năm đầu. "
        f"Điều trị không tốt khi có trên {{{{c4::{Y('2 lần')}}}}} T4 < 8 µg/dL.",
        "10.3", ["So-lieu"],
    ),

    # ------------------------------------------------------------ S13. Phòng bệnh (11)
    basic(
        "PED66-S13-01", "S13", "Phòng bệnh", 1,
        f"{B('[Tầm quan trọng của phòng bệnh]')} Vì sao phải phòng suy giáp bẩm sinh và cần phối hợp những ai?",
        f"1) Vì: suy giáp là {R('nguyên nhân chậm phát triển trí tuệ thường gặp nhất có thể dự phòng')}; chẩn đoán trễ/điều trị sai "
        f"→ {R('gánh nặng gia đình và xã hội')}.<br>"
        f"2) Phối hợp: {G('khoa sản – khoa nhi')}, {G('ngành y tế – các ban ngành đoàn thể')}.",
        "Bệnh có xét nghiệm sàng lọc rẻ và thuốc điều trị rẻ, nên mọi trường hợp chậm trí tuệ do suy giáp đều là thất bại phòng được.",
        "11", ["Phong-benh"],
    ),
    basic(
        "PED66-S13-02", "S13", "Phòng bệnh", 1,
        f"{B('[Biện pháp phòng bệnh]')} Kể {Y('6')} biện pháp phòng suy giáp bẩm sinh.",
        f"1) {G('Xác định yếu tố thuận lợi gây bướu giáp địa phương')}.<br>"
        f"2) {G('Vận động dùng muối iod')}: {Y('150–300 µg iod/ngày')} hay {Y('4 kg muối iod/người/năm')}.<br>"
        f"3) {G('Theo dõi định kỳ phụ nữ có thai')} (tổng quát và bệnh lý tuyến giáp).<br>"
        f"4) {R('KHÔNG điều trị bướu giáp đơn thuần bằng dung dịch có iod cho phụ nữ mang thai')} (gây suy giáp thai nhi).<br>"
        f"5) {G('Giáo dục sức khỏe')} cho gia đình: hiểu bệnh, cách điều trị, theo dõi định kỳ.<br>"
        f"6) {G('Tầm soát hàng loạt TSH và T4')} cho mọi trẻ sơ sinh vào {Y('ngày thứ 3')} sau sinh.",
        "Iod liều cao đột ngột gây hiệu ứng Wolff–Chaikoff, ức chế tuyến giáp thai nhi; vì vậy không dùng dung dịch iod cho thai phụ có bướu đơn thuần.",
        "11", ["Phong-benh"],
    ),
    cloze(
        "PED66-S13-C1", "S13", "Phòng bệnh",
        f"Chương trình phòng chống thiếu iod quốc gia khuyến cáo {{{{c1::{Y('150–300 µg iod/ngày')}}}}} hay "
        f"{{{{c2::{Y('4 kg muối iod/người/năm')}}}}}; tầm soát TSH và T4 cho mọi trẻ sơ sinh vào {{{{c3::{Y('ngày thứ 3')}}}}} sau sinh.",
        "11", ["So-lieu"],
    ),
]
