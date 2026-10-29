# -*- coding: utf-8 -*-
# PED-69 Viêm phổi trẻ em – Chẩn đoán căn nguyên & Lựa chọn kháng sinh (bản chi tiết) — nguồn thẻ duy nhất.
# Chuyên đề EBM quốc tế, KHÔNG phải barem trường. Nội dung: PED-69_..._TONG_ON_EBM.pdf
# (WHO 2024; PIDS/IDSA 2011; BTS 2011; EPIC 2015; CAP-IT 2021; SAFER 2021; SCOUT-CAP 2022; guideline Mycoplasma
#  Trung Quốc 2023; CDC oseltamivir; AAP Red Book; BTS pleural infection 2005; đồng thuận vancomycin 2020).
# Bổ sung cho PED-21 (CAP cơ bản) và PED-62 (5 tác nhân) — không lặp lại thẻ của 2 bài đó.


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý / sai lầm
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / tuổi / thời gian
    return _c("#ffd43b", t)


def G(t):  # thuốc / xử trí / xét nghiệm nên làm
    return _c("#51cf66", t)


def B(t):  # tác nhân / bệnh / phân loại
    return _c("#74c0fc", t)


BADGE = ("📘 CHUYÊN ĐỀ EBM · VIÊM PHỔI", "badge-ebm")
SRC = ("📖 Nguồn: Chuyên đề PED-69 Viêm phổi trẻ em – Tổng ôn EBM (WHO 2024; PIDS/IDSA 2011; BTS 2011; EPIC 2015; "
       "CAP-IT, SAFER, SCOUT-CAP; guideline Mycoplasma Trung Quốc 2023). Mục: ")
WARN = " · ⚠️ Con số/khuyến cáo khác nhau giữa các guideline hoặc ngoài chỉ định; đi thi dùng đúng barem trường, lâm sàng theo phác đồ bệnh viện."
TAG = ["PED-69", "Chuyen-de-EBM", "Viem-phoi"]


def basic(cid, section, category, tier, front, core, ai, muc, tags, asks=None, warn=False):
    card = {
        "id": cid, "track": "ebm", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": SRC + muc + (WARN if warn else ""),
        "tags": TAG + tags,
    }
    if asks:
        card["asks"] = asks
    return card


def algo(cid, section, category, title, core, ai, muc, tags, warn=False):
    card = basic(cid, section, category, 1, "⚡ THUẬT TOÁN QUYẾT ĐỊNH — " + B(title), core, ai, muc,
                 tags + ["Thuat-toan"], warn=warn)
    card.pop("badge")
    card.pop("badge_class")
    return card


def cloze(cid, section, category, text, muc, tags, warn=False):
    return {
        "id": cid, "track": "ebm", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "cloze", "section": section, "category": category, "tier": 2,
        "text": text, "extra": SRC + muc + (WARN if warn else ""),
        "tags": TAG + ["Cloze-phu"] + tags,
    }


cards_data = [
    # ================================================================ S1. WHO 2024, nhập viện, ICU
    basic(
        "PED69-S1-01", "S1", "WHO 2024", 1,
        f"{B('[WHO 2024]')} Theo WHO 2024 (trẻ {Y('2–59 tháng')}), 3 phân loại viêm phổi là gì, tiêu chí từng loại và xử trí kháng sinh tương ứng?",
        f"1) {B('Viêm phổi thở nhanh')}: ho/khó thở + thở nhanh theo tuổi, không rút lõm, không dấu hiệu nguy hiểm → "
        f"{G('amoxicillin uống 40 mg/kg/lần × 2 lần/ngày')}, {Y('3 ngày')} (vùng HIV thấp) hoặc {Y('5 ngày')} (vùng HIV cao).<br>"
        f"2) {B('Viêm phổi rút lõm lồng ngực')}: rút lõm ± thở nhanh, không dấu hiệu nguy hiểm → {G('amoxicillin uống 5 ngày, ngoại trú')}.<br>"
        f"3) {B('Viêm phổi nặng')}: có ≥ 1 dấu hiệu nguy hiểm → {G('nhập viện, ampicillin (hoặc benzylpenicillin) + gentamicin')}; "
        f"{G('ceftriaxone')} là lựa chọn thứ hai.",
        f"Điểm mới so với cách dạy cũ: trẻ {Y('chỉ có rút lõm')} mà không có dấu hiệu nguy hiểm không còn bắt buộc nhập viện tiêm "
        f"kháng sinh — các thử nghiệm cho thấy amoxicillin uống tại nhà hiệu quả tương đương. Nhập viện dành cho trẻ có dấu hiệu nguy hiểm.",
        "1.1 WHO 2024", ["WHO"],
    ),
    basic(
        "PED69-S1-02", "S1", "WHO 2024", 1,
        f"{B('[Dấu hiệu nguy hiểm]')} Kể các dấu hiệu nguy hiểm toàn thân xếp trẻ ho/khó thở vào {R('viêm phổi nặng')} theo WHO 2024.",
        f"1) {R('Không uống / không bú được')}.<br>"
        f"2) {R('Nôn tất cả mọi thứ')}.<br>"
        f"3) {R('Co giật')} trong đợt bệnh.<br>"
        f"4) {R('Li bì hoặc hôn mê')}.<br>"
        f"5) {R('Thở rít khi nằm yên')}.<br>"
        f"6) {R('Giảm oxy máu nặng')}: {Y('SpO₂ < 90%')} (hoặc dấu hiệu lâm sàng khi không có máy đo).",
        "Mỗi dấu hiệu là một con đường dẫn tới tử vong: không uống → mất nước, không dùng được thuốc uống; co giật/li bì → "
        "giảm oxy não hoặc nhiễm khuẩn huyết; thở rít → tắc nghẽn đường thở trên; SpO₂ < 90% → cần oxy ngay.",
        "1.1 WHO 2024", ["WHO", "Dau-hieu-nguy-hiem"],
    ),
    basic(
        "PED69-S1-03", "S1", "WHO 2024", 2,
        f"{B('[WHO 2024 – trẻ 5–9 tuổi và y tế cộng đồng]')} WHO 2024 kết luận gì về thuật toán lâm sàng cho trẻ {Y('5–9 tuổi')}, "
        f"và khuyến cáo gì về điều trị viêm phổi rút lõm tại cộng đồng?",
        f"1) Trẻ {Y('5–9 tuổi')}: {R('chưa đủ bằng chứng')} cho một thuật toán chuẩn kiểu thở nhanh/rút lõm (khoảng trống nghiên cứu).<br>"
        f"2) Cộng đồng: nơi có nhân viên y tế cộng đồng được đào tạo, WHO {G('gợi ý điều trị tại cộng đồng')} "
        f"(đủ {Y('5 ngày')} amoxicillin + thăm lại) thay vì chỉ cho 1 liều rồi chuyển tuyến.",
        "Trẻ lớn có nhịp thở nền khác, hay có hen/khò khè và nhiều Mycoplasma hơn, nên ngưỡng thở nhanh của trẻ nhỏ không áp dụng "
        "thẳng được. Thực hành: đánh giá lâm sàng đầy đủ theo tiêu chí PIDS/BTS.",
        "1.1 WHO 2024", ["WHO"],
    ),
    basic(
        "PED69-S1-04", "S1", "Nhập viện", 1,
        f"{B('[Tiêu chí nhập viện]')} Kể các tiêu chí nhập viện cho trẻ viêm phổi theo PIDS/IDSA 2011 và BTS 2011.",
        f"1) {R('Suy hô hấp trung bình – nặng')}; {R('SpO₂ < 90%')} (PIDS) / {R('< 92%')} (BTS) khí trời.<br>"
        f"2) Nhũ nhi {Y('≤ 3–6 tháng')} nghi viêm phổi vi khuẩn.<br>"
        f"3) Nghi tác nhân độc lực cao: {B('tụ cầu (CA-MRSA)')}, {B('liên cầu nhóm A')}.<br>"
        f"4) {R('Không uống được, mất nước, li bì')}.<br>"
        f"5) {R('Gia đình không theo dõi / không tái khám được')}.<br>"
        f"6) {R('Thất bại điều trị ngoại trú 48–72 giờ')}.",
        "Hai guideline lệch nhau ở ngưỡng SpO₂ (90% vs 92%) vì BTS áp dụng cho nước có nguồn lực oxy dồi dào. Tiêu chí xã hội "
        "(không theo dõi được) là tiêu chí thật — trẻ nặng lên về đêm ở nhà xa viện có nguy cơ tử vong.",
        "1.2 Nhập viện", ["Nhap-vien"], warn=True,
    ),
    basic(
        "PED69-S1-05", "S1", "ICU", 2,
        f"{B('[Chuyển ICU]')} Những dấu hiệu nào ở trẻ viêm phổi cần chuyển hồi sức tích cực?",
        f"1) {R('Cần thở máy xâm nhập hoặc thở không xâm nhập kéo dài')}.<br>"
        f"2) {R('SpO₂ < 92% dù FiO₂ ≥ 0,5')}.<br>"
        f"3) {R('Rối loạn tri giác')}.<br>"
        f"4) {R('Sốc')}: nhịp tim nhanh kéo dài, huyết áp tụt, cần vận mạch.<br>"
        f"5) {R('Ngừng thở, thở chậm bất thường, kiệt sức')}.",
        "Trẻ cần FiO₂ ≥ 50% mà vẫn không giữ được SpO₂ 92% là có shunt lớn — oxy mũi không còn đủ, cần áp lực dương và theo dõi "
        "liên tục. Thở chậm lại ở trẻ đang suy hô hấp là kiệt sức, không phải cải thiện.",
        "1.2 Nhập viện", ["ICU"],
    ),
    cloze(
        "PED69-S1-C1", "S1", "WHO 2024",
        f"WHO 2024: viêm phổi thở nhanh ở vùng HIV thấp dùng amoxicillin uống {{{{c1::{Y('3 ngày')}}}}}; viêm phổi rút lõm lồng ngực dùng "
        f"{{{{c2::{Y('5 ngày')}}}}} tại nhà.",
        "1.1 WHO 2024", ["WHO"],
    ),
    cloze(
        "PED69-S1-C2", "S1", "WHO 2024",
        f"WHO 2024: liều amoxicillin uống cho viêm phổi trẻ 2–59 tháng là {{{{c1::{G('40 mg/kg/lần, 2 lần/ngày')}}}}}.",
        "1.1 WHO 2024", ["WHO", "Lieu"],
    ),

    # ================================================================ S2. Căn nguyên theo tuổi & bối cảnh
    basic(
        "PED69-S2-01", "S2", "EPIC", 1,
        f"{B('[Nghiên cứu EPIC]')} Nghiên cứu EPIC (CDC, NEJM 2015) trên trẻ viêm phổi nhập viện tìm thấy tác nhân ở bao nhiêu %, "
        f"tỷ lệ virus, vi khuẩn, đồng nhiễm và tác nhân đứng đầu mỗi nhóm?",
        f"1) Tìm thấy tác nhân: {Y('81%')}.<br>"
        f"2) {B('Virus')}: {Y('73%')} — đứng đầu {B('RSV')} ({Y('28%')}).<br>"
        f"3) {B('Vi khuẩn')}: {Y('15%')} — {B('Mycoplasma')} {Y('8%')}, {B('phế cầu')} {Y('4%')}.<br>"
        f"4) {B('Đồng nhiễm virus – vi khuẩn')}: {Y('7%')}.",
        f"Hàm ý: phần lớn viêm phổi trẻ nhỏ là virus, nhưng xét nghiệm hiện có {R('không đủ nhạy để loại trừ vi khuẩn')} (phế cầu "
        f"hay bị bỏ sót vì cấy máu ít dương tính). Vì vậy vẫn dùng kháng sinh kinh nghiệm khi bệnh cảnh gợi ý vi khuẩn.",
        "2.1 Căn nguyên", ["Can-nguyen", "EPIC"],
    ),
    basic(
        "PED69-S2-02", "S2", "Theo tuổi", 1,
        f"{B('[Căn nguyên theo tuổi]')} Tác nhân viêm phổi thường gặp ở 4 nhóm tuổi: {Y('0–3 tuần')}, {Y('3 tuần – 3 tháng')}, "
        f"{Y('3 tháng – 5 tuổi')}, {Y('≥ 5 tuổi')}?",
        f"1) {Y('0–3 tuần')}: {B('liên cầu nhóm B')}, {B('Gram âm đường ruột')} (E. coli, Klebsiella), {B('Listeria')}; CMV, HSV.<br>"
        f"2) {Y('3 tuần – 3 tháng')}: virus (RSV…), {B('phế cầu')}, {B('Chlamydia trachomatis')}, {B('Bordetella pertussis')}, tụ cầu.<br>"
        f"3) {Y('3 tháng – 5 tuổi')}: {B('virus chiếm đa số')}; vi khuẩn hàng đầu {B('phế cầu')}; Hib (chưa tiêm), tụ cầu, Mycoplasma tăng dần.<br>"
        f"4) {Y('≥ 5 tuổi')}: {B('Mycoplasma pneumoniae')}, {B('Chlamydia pneumoniae')}, {B('phế cầu')}, virus.",
        "Mẹo nhớ: sơ sinh = vi khuẩn đường sinh dục mẹ; 1–3 tháng = nhóm “không sốt” (Chlamydia, ho gà); trẻ nhỏ = virus + phế cầu; "
        "trẻ đi học = Mycoplasma + phế cầu. Phế cầu là đích chính của kháng sinh kinh nghiệm ở mọi tuổi > 3 tháng.",
        "2.1 Căn nguyên theo tuổi", ["Can-nguyen"],
    ),
    basic(
        "PED69-S2-03", "S2", "Bối cảnh", 1,
        f"{B('[Căn nguyên theo bối cảnh]')} Cần nghĩ thêm tác nhân nào trong các bối cảnh: {R('sau cúm/thủy đậu/sởi')}, "
        f"{R('chưa tiêm PCV/Hib')}, {R('rối loạn nuốt')}, {R('suy giảm miễn dịch')}, {R('tiếp xúc lao')}, {R('xơ nang')}, "
        f"{R('nằm viện ≥ 48 giờ')}?",
        f"1) Sau cúm/thủy đậu/sởi, nhiễm trùng da → {B('tụ cầu vàng (MSSA/MRSA)')}, {B('liên cầu nhóm A')}.<br>"
        f"2) Chưa tiêm PCV/Hib → {B('phế cầu type vắc xin')}, {B('Hib')}.<br>"
        f"3) Bệnh thần kinh, rối loạn nuốt, trào ngược, sau co giật → {B('viêm phổi hít')} (liên cầu miệng, kỵ khí miệng).<br>"
        f"4) HIV, suy giảm miễn dịch → {B('Pneumocystis jirovecii')}, CMV, nấm, Gram âm, lao.<br>"
        f"5) Tiếp xúc lao, sụt cân, ho > 2–3 tuần → {B('lao')}.<br>"
        f"6) Xơ nang, giãn phế quản → {B('Pseudomonas')}, tụ cầu.<br>"
        f"7) Nằm viện ≥ 48 giờ / thở máy → {B('Gram âm bệnh viện')} (Pseudomonas, Klebsiella, Acinetobacter), MRSA.",
        "Bối cảnh quan trọng hơn tuổi khi có mặt: một trẻ 3 tuổi viêm phổi nặng nhanh sau thủy đậu phải được phủ tụ cầu ngay, "
        "không chờ “không đáp ứng” với ampicillin.",
        "2.2 Bối cảnh đặc biệt", ["Can-nguyen", "Boi-canh"],
    ),
    basic(
        "PED69-S2-04", "S2", "Nhũ nhi nhỏ", 2,
        f"{B('[Chlamydia trachomatis và ho gà ở nhũ nhi]')} Phân biệt viêm phổi do {B('Chlamydia trachomatis')} và {B('ho gà')} ở trẻ "
        f"{Y('3 tuần – 3 tháng')} dựa vào sốt, kiểu ho, dấu hiệu kèm và công thức máu.",
        f"1) {B('Chlamydia trachomatis')}: {Y('không sốt')}, {R('ho từng tiếng (staccato)')}, {R('viêm kết mạc')} (hoặc tiền sử), "
        f"{R('tăng bạch cầu ái toan')}; X-quang thâm nhiễm kẽ, ứ khí.<br>"
        f"2) {B('Ho gà')}: thường không sốt, {R('ho cơn rũ rượi, đỏ mặt, tím')}, {R('ngừng thở')} ở nhũ nhi nhỏ, "
        f"{R('tăng bạch cầu lympho')}.",
        "Cả hai đều lây từ người lớn/mẹ và không đáp ứng β-lactam; điều trị bằng macrolid (azithromycin). Ho gà ở nhũ nhi < 3 tháng "
        "có thể tử vong do ngừng thở và tăng áp phổi — bạch cầu lympho rất cao là dấu hiệu nặng.",
        "2.1 Căn nguyên theo tuổi", ["Can-nguyen", "Chlamydia", "Ho-ga"],
    ),
    cloze(
        "PED69-S2-C1", "S2", "EPIC",
        f"Trong nghiên cứu EPIC, tác nhân gây viêm phổi nhập viện thường gặp nhất ở trẻ em là {{{{c1::{B('RSV')}}}}}.",
        "2.1 Căn nguyên", ["EPIC"],
    ),
    cloze(
        "PED69-S2-C2", "S2", "EPIC",
        f"EPIC: virus tìm thấy ở {{{{c1::{Y('73%')}}}}} và vi khuẩn ở {{{{c2::{Y('15%')}}}}} trẻ viêm phổi nhập viện.",
        "2.1 Căn nguyên", ["EPIC"],
    ),

    # ================================================================ S3. Manh mối lâm sàng – X-quang
    basic(
        "PED69-S3-01", "S3", "Virus vs vi khuẩn", 1,
        f"{B('[Virus hay vi khuẩn điển hình]')} So sánh viêm phổi {B('virus')} và {B('phế cầu / vi khuẩn điển hình')} về lâm sàng, X-quang và xét nghiệm viêm.",
        f"1) {B('Virus')}: tuổi nhỏ, {G('khởi phát từ từ')}, chảy mũi, {G('khò khè')}, người nhà cùng bệnh; X-quang {G('thâm nhiễm kẽ 2 bên, ứ khí, xẹp phổi')}; "
        f"CRP/PCT thường thấp (trừ adenovirus).<br>"
        f"2) {B('Phế cầu')}: {R('sốt cao đột ngột ≥ 38,5 °C')}, nhiễm độc, đau ngực/đau bụng, {R('ran nổ khu trú')}, {R('không khò khè')}; "
        f"X-quang {R('đông đặc thùy/phân thùy, tràn dịch')}; bạch cầu, CRP, PCT cao.",
        f"Không có dấu hiệu nào đơn độc đủ tin cậy; phải ghép nhiều manh mối. Bẫy: {R('viêm phổi tròn')} do phế cầu giống u; "
        f"adenovirus có thể sốt cao, CRP rất cao giống vi khuẩn.",
        "3. Manh mối căn nguyên", ["Manh-moi"],
    ),
    basic(
        "PED69-S3-02", "S3", "Mycoplasma", 1,
        f"{B('[Mycoplasma]')} Nêu manh mối lâm sàng, ngoài phổi, X-quang, xét nghiệm và đáp ứng điều trị gợi ý viêm phổi do {B('Mycoplasma pneumoniae')}.",
        f"1) Lâm sàng: trẻ {Y('≥ 5 tuổi')}, {R('ho dai dẳng')}, {R('đau đầu, đau họng')}, có thể khò khè.<br>"
        f"2) Ngoài phổi: {R('ban / SJS, viêm niêm mạc (MIRM)')}, {R('tan máu')}, {R('viêm não')}.<br>"
        f"3) X-quang: thâm nhiễm kẽ hoặc đông đặc, {R('“X-quang nặng hơn khám”')}.<br>"
        f"4) Xét nghiệm: {R('LDH cao')} gợi ý thể nặng.<br>"
        f"5) Điều trị: {R('không đáp ứng β-lactam')}; ở châu Á {R('phần lớn kháng macrolid')}.",
        "MIRM (Mycoplasma-induced rash and mucositis) khác SJS kinh điển: viêm niêm mạc nặng, ban da ít. Gặp viêm niêm mạc miệng – mắt "
        "ở trẻ đi học đang ho → phải nghĩ Mycoplasma.",
        "3. Manh mối căn nguyên", ["Manh-moi", "Mycoplasma"], asks=["Lâm sàng", "Ngoài phổi", "X-quang", "Xét nghiệm", "Điều trị"],
    ),
    basic(
        "PED69-S3-03", "S3", "Tụ cầu", 1,
        f"{B('[Tụ cầu vàng]')} Bệnh cảnh, diễn tiến, hình ảnh X-quang nào gợi ý viêm phổi do {B('tụ cầu vàng')}, và đáp ứng điều trị ra sao?",
        f"1) Bệnh cảnh: {R('sau cúm / thủy đậu')}, {R('nhọt, nhiễm trùng da')}.<br>"
        f"2) Diễn tiến: {R('rất nhanh')}, có thể {R('sốc')}.<br>"
        f"3) X-quang: {R('bóng khí (pneumatocele)')}, {R('hoại tử, áp xe')}, {R('tràn mủ')}, {R('tràn khí màng phổi')}.<br>"
        f"4) Điều trị: {R('đáp ứng chậm với β-lactam đơn thuần')} → cần phủ tụ cầu.",
        "Cúm làm tổn thương biểu mô và giảm chức năng bạch cầu, mở đường cho tụ cầu bám dính; chủng có độc tố PVL gây hoại tử "
        "nhu mô và tạo bóng khí. Một trẻ đang hồi phục cúm bỗng sốt lại, thở nhanh là tín hiệu bội nhiễm.",
        "3. Manh mối căn nguyên", ["Manh-moi", "Tu-cau"], asks=["Bệnh cảnh", "Diễn tiến", "X-quang", "Điều trị"],
    ),
    basic(
        "PED69-S3-04", "S3", "Hít", 2,
        f"{B('[Viêm phổi hít]')} Trẻ nào có nguy cơ viêm phổi hít, tổn thương hay nằm ở đâu trên X-quang, và khi nào {G('không cần kháng sinh')}?",
        f"1) Nguy cơ: {R('bại não, rối loạn nuốt, sặc, sau co giật/hôn mê')}, trào ngược.<br>"
        f"2) Vị trí: {B('phân thùy sau thùy trên phải')}, {B('đỉnh thùy dưới')} (hít khi nằm); {B('thùy dưới phải')} (hít khi đứng/ngồi).<br>"
        f"3) {G('Viêm phổi hóa chất')} trong những giờ đầu sau sặc dịch dạ dày → {G('không cần kháng sinh')} nếu không có bằng chứng nhiễm khuẩn.",
        "Phế quản gốc phải thẳng và to hơn nên dị vật/dịch hít vào bên phải nhiều hơn. Sặc dịch dạ dày gây viêm do axit (không phải "
        "nhiễm khuẩn) — tự cải thiện trong 24–48 giờ; chỉ dùng kháng sinh khi sốt, đờm mủ hoặc xấu đi.",
        "3. Manh mối căn nguyên", ["Manh-moi", "Hit"],
    ),
    basic(
        "PED69-S3-05", "S3", "Lao và PCP", 2,
        f"{B('[Lao và Pneumocystis]')} Manh mối gợi ý {B('lao')} và {B('viêm phổi Pneumocystis (PCP)')} ở trẻ em là gì?",
        f"1) {B('Lao')}: {R('ho > 2–3 tuần')}, {R('sụt cân')}, {R('tiếp xúc nguồn lây')}; X-quang {R('hạch rốn phổi')}, đông đặc không đáp ứng, hang, kê.<br>"
        f"2) {B('PCP')}: {Y('nhũ nhi HIV 2–6 tháng')}, thở nhanh, {R('giảm oxy nặng')} nhưng nghe phổi ít ran; X-quang {R('mờ kẽ lan tỏa 2 bên')}; {R('LDH cao')}.",
        f"Bẫy lao: dùng {R('fluoroquinolon')} cho “viêm phổi không đáp ứng” làm lao đỡ tạm thời và che lấp chẩn đoán. Bẫy PCP: viêm phổi "
        f"nặng ở trẻ HIV dưới 1 tuổi phải nghĩ PCP và thêm cotrimoxazol.",
        "3. Manh mối căn nguyên", ["Manh-moi", "Lao", "PCP"],
    ),
    basic(
        "PED69-S3-06", "S3", "Nguyên tắc BTS", 1,
        f"{B('[Nguyên tắc BTS]')} Theo BTS 2011, trẻ {Y('< 2 tuổi')} có triệu chứng hô hấp dưới nhẹ và trẻ {G('khò khè')} thường là gì; "
        f"khi nào nên nghĩ {R('viêm phổi vi khuẩn')}?",
        f"1) Trẻ {Y('< 2 tuổi')}, triệu chứng nhẹ: thường {G('không phải viêm phổi')}.<br>"
        f"2) Trẻ nhỏ {G('khò khè')}: nhiều khả năng {B('virus / hen')}, ít khả năng viêm phổi vi khuẩn.<br>"
        f"3) Nghĩ viêm phổi vi khuẩn khi: {R('sốt > 38,5 °C dai dẳng hoặc tái lại')} + {R('rút lõm')} + {R('thở nhanh')}.",
        "Nguyên tắc này giúp tránh kê kháng sinh cho viêm tiểu phế quản và khò khè do virus — nhóm chiếm phần lớn trẻ nhỏ đến khám "
        "vì ho, khó thở.",
        "3. Manh mối căn nguyên", ["Manh-moi", "BTS"],
    ),
    cloze(
        "PED69-S3-C1", "S3", "Tụ cầu",
        f"Hình ảnh {{{{c1::{R('bóng khí (pneumatocele)')}}}}} trên X-quang ở trẻ viêm phổi tiến triển nhanh sau cúm gợi ý tụ cầu vàng.",
        "3. Manh mối căn nguyên", ["Tu-cau"],
    ),
    cloze(
        "PED69-S3-C2", "S3", "Chlamydia",
        f"Viêm phổi nhũ nhi 1–3 tháng không sốt, ho từng tiếng, viêm kết mạc, tăng bạch cầu ái toan gợi ý {{{{c1::{B('Chlamydia trachomatis')}}}}}.",
        "3. Manh mối căn nguyên", ["Chlamydia"],
    ),

    # ================================================================ S4. Cận lâm sàng
    basic(
        "PED69-S4-01", "S4", "X-quang kiểm tra", 1,
        f"{B('[X-quang kiểm tra]')} Khi nào {G('cần')} và khi nào {R('không cần')} chụp X-quang ngực kiểm tra sau viêm phổi? Chụp lại sau bao lâu?",
        f"1) {R('Không cần')}: trẻ hồi phục bình thường.<br>"
        f"2) {G('Cần chụp lại sau 4–6 tuần')}: {R('viêm phổi tái diễn cùng thùy')}, {R('xẹp thùy')} (nghi dị vật, bất thường giải phẫu, u), "
        f"{R('viêm phổi tròn')}.<br>"
        f"3) {G('Chụp sớm')}: khi {R('xấu đi')} hoặc {R('sốt kéo dài không đáp ứng 48–72 giờ')}.",
        "Tổn thương X-quang tồn tại nhiều tuần sau khi trẻ đã khỏi lâm sàng — chụp lại sớm ở trẻ khỏe chỉ tạo hình ảnh “chưa sạch” và "
        "dẫn đến kéo dài kháng sinh vô ích. Tái diễn cùng một vị trí thì phải tìm nguyên nhân tại chỗ.",
        "4.1 Hình ảnh", ["X-quang"],
    ),
    basic(
        "PED69-S4-02", "S4", "Siêu âm và CT", 2,
        f"{B('[Siêu âm phổi và CT ngực]')} Vai trò của {G('siêu âm phổi – màng phổi')} và khi nào cần {G('CT ngực')} trong viêm phổi trẻ em?",
        f"1) {G('Siêu âm')}: nhạy để phát hiện đông đặc, {G('đánh giá tràn dịch và vách ngăn')}, {G('hướng dẫn chọc / đặt dẫn lưu')}; "
        f"không chiếu xạ — {G('đầu tay khi nghi tràn dịch')}.<br>"
        f"2) {G('CT')}: {R('không thường quy')}; khi nghi {R('hoại tử, áp xe, rò phế quản – màng phổi')}, {R('bất thường giải phẫu')}, "
        f"hoặc trước phẫu thuật.",
        "Siêu âm cho thấy dịch có vách hay không — điều X-quang không làm được — và quyết định dẫn lưu đơn thuần hay cần tiêu sợi "
        "huyết/VATS. CT tăng liều xạ đáng kể nên dành cho câu hỏi thật sự thay đổi xử trí.",
        "4.1 Hình ảnh", ["Sieu-am", "CT"],
    ),
    basic(
        "PED69-S4-03", "S4", "Biomarker", 1,
        f"{B('[CRP, PCT, công thức máu]')} PIDS/BTS khuyến cáo gì về dùng {G('CRP, PCT, công thức máu')} để phân biệt virus – vi khuẩn, "
        f"ở trẻ ngoại trú và ở trẻ nội trú nặng?",
        f"1) Phân biệt virus – vi khuẩn: {R('không dùng đơn độc')} (PIDS: khuyến cáo mạnh).<br>"
        f"2) Ngoại trú: {R('không đo thường quy')}.<br>"
        f"3) Nội trú nặng / biến chứng: {G('theo dõi động CRP/PCT')} giúp đánh giá đáp ứng; {G('PCT thấp')} làm giảm khả năng vi khuẩn điển hình "
        f"nhưng {R('chồng lấn lớn')}.",
        "Trung vị CRP/PCT ở viêm phổi vi khuẩn cao hơn virus, nhưng phân bố chồng lấn rộng: adenovirus và Mycoplasma có thể cho CRP "
        "rất cao, phế cầu giai đoạn sớm có thể CRP chưa tăng. Dùng xu hướng nhiều lần đo có giá trị hơn một giá trị đơn lẻ.",
        "4.2 Xét nghiệm viêm", ["Biomarker"], asks=["Phân biệt virus – vi khuẩn", "Ngoại trú", "Nội trú nặng"],
    ),
    basic(
        "PED69-S4-04", "S4", "Xét nghiệm hỗ trợ", 2,
        f"{B('[Điện giải và chức năng thận]')} Ở trẻ viêm phổi nặng, vì sao cần làm {G('điện giải đồ')} và {G('chức năng thận / công thức máu')}?",
        f"1) {G('Điện giải đồ')}: phát hiện {R('hạ natri do SIADH')}.<br>"
        f"2) {G('Chức năng thận + công thức máu + tiểu cầu')}: phát hiện {R('HUS do phế cầu')} — {R('thiếu máu tan máu, giảm tiểu cầu, suy thận')}.",
        "Viêm phổi nặng kích thích tiết ADH → giữ nước, hạ natri, co giật nếu truyền dịch nhược trương. HUS do phế cầu (neuraminidase "
        "bộc lộ kháng nguyên T) hay đi kèm tràn mủ màng phổi.",
        "4.2 Xét nghiệm viêm", ["SIADH", "HUS"],
    ),
    basic(
        "PED69-S4-05", "S4", "Cấy máu", 1,
        f"{B('[Cấy máu]')} Theo PIDS/BTS, cấy máu chỉ định cho trẻ viêm phổi nào và không cần cho trẻ nào? Tỷ lệ dương tính, "
        f"cấy lại và chờ kết quả khi ra viện?",
        f"1) {R('Không')}: trẻ ngoại trú đã tiêm chủng đủ.<br>"
        f"2) {G('Có')}: trẻ nhập viện viêm phổi {R('trung bình – nặng')}, {R('có biến chứng')}, {R('xấu đi dù điều trị')}.<br>"
        f"3) Dương tính thấp: khoảng {Y('1–3%')} ở viêm phổi không biến chứng, cao hơn ở thể có biến chứng.<br>"
        f"4) {R('Không cần cấy lại')} khi trẻ đã cải thiện.<br>"
        f"5) Kết quả đang chờ {R('không phải lý do giữ trẻ')} đã đủ tiêu chuẩn ra viện (nếu theo dõi được).",
        "Cấy máu ít dương tính vì phế cầu chỉ vào máu thoáng qua và trẻ thường đã dùng kháng sinh. Nhưng ở trẻ nặng/tràn mủ, một kết "
        "quả dương tính cho phép xuống thang chính xác (ví dụ về penicillin) — đó là giá trị thật của xét nghiệm.",
        "4.3 Xét nghiệm căn nguyên", ["Cay-mau"], warn=True,
    ),
    basic(
        "PED69-S4-06", "S4", "Virus", 1,
        f"{B('[PCR / test nhanh virus]')} Xét nghiệm virus dịch tỵ hầu nên làm cho trẻ nào, kết quả dương tính thay đổi xử trí thế nào, và "
        f"giới hạn quan trọng nhất là gì?",
        f"1) Làm cho: {G('trẻ nhập viện')}; khi kết quả {G('thay đổi xử trí')}.<br>"
        f"2) Thay đổi xử trí: {B('cúm')} → {G('oseltamivir')}; {G('cách ly')} đúng nhóm; ở trẻ ngoại trú bệnh cảnh phù hợp virus → "
        f"{G('có thể giảm kháng sinh')}.<br>"
        f"3) Giới hạn: {R('dương tính virus không loại trừ đồng nhiễm vi khuẩn')}.",
        "EPIC ghi nhận đồng nhiễm virus – vi khuẩn khoảng 7%; một trẻ có RSV dương tính nhưng đông đặc thùy, CRP rất cao vẫn cần kháng "
        "sinh. PCR đa tác nhân cũng phát hiện virus mang theo không triệu chứng (rhinovirus, adenovirus) — đọc cùng bệnh cảnh.",
        "4.3 Xét nghiệm căn nguyên", ["Virus"],
    ),
    basic(
        "PED69-S4-07", "S4", "Mycoplasma", 1,
        f"{B('[Xét nghiệm Mycoplasma]')} So sánh {G('PCR')}, {G('IgM')} và {G('huyết thanh cặp IgG')} trong chẩn đoán Mycoplasma: "
        f"ưu tiên cái nào và giới hạn của từng cái?",
        f"1) {G('PCR')} (tỵ hầu/họng): {G('ưu tiên')}, nhanh, nhạy; giới hạn: {R('mang trùng không triệu chứng')} và {R('thải DNA kéo dài hàng tuần – tháng')}.<br>"
        f"2) {G('IgM')}: {R('âm tính giả sớm')} (cần khoảng {Y('7–10 ngày')}); {R('dương tính giả')} vì IgM tồn tại lâu.<br>"
        f"3) {G('Huyết thanh cặp')}: {Y('IgG tăng ≥ 4 lần')} giữa 2 mẫu — chắc chắn nhưng {R('hồi cứu')}, không giúp quyết định cấp.",
        "Thực hành: PCR dương + bệnh cảnh phù hợp (trẻ đi học, ho kéo dài, X-quang thâm nhiễm) là đủ để điều trị. Một IgM dương đơn "
        "độc ở trẻ khò khè 2 tuổi không đủ chứng minh Mycoplasma là thủ phạm.",
        "4.3 Xét nghiệm căn nguyên", ["Mycoplasma"],
    ),
    basic(
        "PED69-S4-08", "S4", "Phế cầu niệu", 1,
        f"{B('[Kháng nguyên phế cầu niệu]')} Vì sao {R('không làm')} kháng nguyên phế cầu trong nước tiểu ở trẻ em? Mẫu nào thay thế có giá trị?",
        f"1) {R('Dương tính giả')} do {R('mang phế cầu vùng hầu họng')} (rất phổ biến ở trẻ nhỏ).<br>"
        f"2) {R('Dương tính giả sau tiêm PCV')}.<br>"
        f"3) Thay thế: {G('kháng nguyên / PCR phế cầu trong dịch màng phổi')} — giá trị cao.",
        "Ở người lớn xét nghiệm này hữu ích vì ít người mang trùng; ở trẻ nhỏ một nửa có phế cầu ở họng nên kháng nguyên vào nước tiểu "
        "mà không có viêm phổi phế cầu. Dịch màng phổi là vị trí vô khuẩn nên dương tính có nghĩa thật.",
        "4.3 Xét nghiệm căn nguyên", ["Phe-cau"],
    ),
    basic(
        "PED69-S4-09", "S4", "Dịch màng phổi", 1,
        f"{B('[Dịch màng phổi]')} Dịch màng phổi khi chọc/dẫn lưu cần gửi xét nghiệm gì, và BTS nói gì về {R('sinh hóa dịch')} ở trẻ em?",
        f"1) Gửi: {G('nhuộm Gram')}, {G('cấy')}, {G('PCR / kháng nguyên phế cầu')} (nhất là khi đã dùng kháng sinh).<br>"
        f"2) BTS: {R('sinh hóa dịch (pH, glucose, LDH) không cần')} để quyết định xử trí ở trẻ em.",
        "Dịch thường đã vô khuẩn khi cấy vì trẻ dùng kháng sinh nhiều ngày — PCR vẫn bắt được DNA phế cầu, giúp xuống thang chính xác. "
        "Ở trẻ em, quyết định dẫn lưu dựa vào kích thước, vách ngăn trên siêu âm và tình trạng hô hấp hơn là pH.",
        "4.3 Xét nghiệm căn nguyên", ["Mang-phoi"],
    ),
    basic(
        "PED69-S4-10", "S4", "Lao, HIV, đờm", 2,
        f"{B('[Đờm, lao, HIV]')} Khi nào xét nghiệm {G('đờm')}, {G('lao')} và {G('HIV')} có giá trị trong viêm phổi trẻ em, và làm xét nghiệm gì?",
        f"1) {G('Đờm')}: trẻ lớn khạc được, nhập viện; chỉ giá trị khi {G('mẫu đạt chất lượng')} (nhiều bạch cầu, ít tế bào biểu mô); "
        f"trẻ đặt nội khí quản → {G('dịch hút khí quản')} nhuộm Gram + cấy.<br>"
        f"2) {G('Lao')}: ho kéo dài, tiếp xúc, không đáp ứng, hình ảnh gợi ý → {G('Xpert MTB/RIF Ultra')} (dịch dạ dày / đờm / phân), "
        f"{G('TST / IGRA')}, X-quang.<br>"
        f"3) {G('HIV')}: viêm phổi nặng/tái diễn, nhũ nhi nghi PCP, mẹ nhiễm HIV → nếu dương tính {G('thêm cotrimoxazol')}.",
        "Trẻ nhỏ nuốt đờm nên dịch dạ dày buổi sáng là mẫu tìm lao kinh điển; Xpert Ultra trên phân là lựa chọn không xâm lấn được WHO "
        "chấp nhận.",
        "4.3 Xét nghiệm căn nguyên", ["Lao", "HIV"],
    ),
    basic(
        "PED69-S4-11", "S4", "Kháng macrolid", 2,
        f"{B('[Xét nghiệm đột biến kháng macrolid]')} Xét nghiệm gì phát hiện {B('Mycoplasma kháng macrolid')}, chỉ định khi nào và kết quả "
        f"định hướng gì?",
        f"1) Xét nghiệm: {G('PCR phát hiện đột biến 23S rRNA')} ({B('A2063G')} / {B('A2064G')}).<br>"
        f"2) Chỉ định: {R('Mycoplasma nặng')} hoặc {R('không đáp ứng 48–72 giờ')} với macrolid.<br>"
        f"3) Định hướng: chuyển {G('doxycycline / minocycline / fluoroquinolon')}.",
        "A2063G chiếm gần như toàn bộ chủng kháng ở Việt Nam và Trung Quốc. Biết sớm đột biến giúp không mất thêm 2–3 ngày với "
        "macrolid ở trẻ nặng.",
        "4.3 Xét nghiệm căn nguyên", ["Mycoplasma", "Khang-thuoc"], asks=["Xét nghiệm", "Chỉ định", "Định hướng"],
    ),
    cloze(
        "PED69-S4-C1", "S4", "Mycoplasma",
        f"Chẩn đoán huyết thanh chắc chắn Mycoplasma cần {{{{c1::{Y('IgG tăng ≥ 4 lần')}}}}} giữa mẫu cấp và mẫu hồi phục.",
        "4.3 Xét nghiệm căn nguyên", ["Mycoplasma"],
    ),
    cloze(
        "PED69-S4-C2", "S4", "X-quang",
        f"X-quang kiểm tra (khi tái diễn cùng thùy, xẹp thùy, viêm phổi tròn) nên chụp sau {{{{c1::{Y('4–6 tuần')}}}}}.",
        "4.1 Hình ảnh", ["X-quang"],
    ),
    cloze(
        "PED69-S4-C3", "S4", "Cấy máu",
        f"Tỷ lệ cấy máu dương tính ở viêm phổi trẻ em không biến chứng chỉ khoảng {{{{c1::{Y('1–3%')}}}}}.",
        "4.3 Xét nghiệm căn nguyên", ["Cay-mau"], warn=True,
    ),

    # ================================================================ S5. Nguyên tắc & phác đồ kinh nghiệm theo tình huống
    basic(
        "PED69-S5-01", "S5", "Nguyên tắc", 1,
        f"{B('[6 nguyên tắc chọn kháng sinh]')} Kể 6 câu hỏi/nguyên tắc theo thứ tự khi chọn kháng sinh cho trẻ viêm phổi.",
        f"1) {G('Có cần kháng sinh không?')} — bệnh cảnh virus rõ → không kháng sinh, hẹn đánh giá lại.<br>"
        f"2) {G('Tác nhân đích')} theo tuổi + bối cảnh (phế cầu là đích chính ở mọi tuổi > 3 tháng).<br>"
        f"3) {G('Mức độ nặng + nơi điều trị')}: uống ngoại trú hay tiêm nội trú.<br>"
        f"4) {G('Tiêm chủng + kháng thuốc tại chỗ')}: phế cầu giảm nhạy penicillin → amoxicillin liều cao; "
        f"{R('phế cầu kháng macrolid rất cao ở châu Á')} → không dùng macrolid đơn độc cho phế cầu.<br>"
        f"5) {G('Dị ứng, tuổi')} (tetracyclin, fluoroquinolon), tương tác, khả năng uống.<br>"
        f"6) {G('Đánh giá lại 48–72 giờ')}; xuống thang theo cấy; chuyển uống sớm.",
        "Thứ tự này ngăn hai sai lầm phổ biến: kê kháng sinh cho viêm phổi virus, và nâng bậc kháng sinh mạnh ngay từ đầu “cho chắc”. "
        "Phần lớn trẻ chỉ cần amoxicillin liều đúng trong 5 ngày.",
        "5.1 Nguyên tắc", ["Nguyen-tac"],
    ),
    basic(
        "PED69-S5-02", "S5", "Ngoại trú", 1,
        f"{B('[Ngoại trú]')} Kháng sinh kinh nghiệm ngoại trú cho trẻ {Y('< 5 tuổi')} và {Y('≥ 5 tuổi')} nghi vi khuẩn điển hình, "
        f"và cho trẻ nghi {B('Mycoplasma / Chlamydophila')}?",
        f"1) {Y('< 5 tuổi')}: {G('amoxicillin 90 mg/kg/ngày chia 2')} (tối đa {Y('4 g/ngày')}).<br>"
        f"2) {Y('≥ 5 tuổi')}, nghi điển hình: {G('amoxicillin liều cao')}; không đáp ứng 48 giờ hoặc bệnh cảnh không điển hình → "
        f"{G('thêm hoặc chuyển macrolid')}.<br>"
        f"3) Nghi Mycoplasma/Chlamydophila: {G('azithromycin 10 mg/kg ngày 1, 5 mg/kg ngày 2–5')}; thay thế {G('clarithromycin')}, "
        f"{G('erythromycin')}, {G('doxycycline')} (≥ 8 tuổi, hoặc đợt ngắn ≤ 21 ngày mọi tuổi theo AAP).",
        "Trẻ dưới 5 tuổi hiếm khi viêm phổi do Mycoplasma (EPIC), nên macrolid kinh nghiệm cho nhóm này chủ yếu tạo kháng thuốc. "
        "Ở trẻ lớn, chọn amoxicillin hay macrolid dựa vào bệnh cảnh: sốt cao đột ngột, đông đặc → amoxicillin; ho kéo dài, đau đầu, "
        "thâm nhiễm kẽ → macrolid.",
        "5.2 Phác đồ kinh nghiệm", ["Ngoai-tru"], warn=True,
    ),
    basic(
        "PED69-S5-03", "S5", "Amoxicillin–clavulanat", 2,
        f"{B('[Khi nào dùng amoxicillin–clavulanat]')} Kể các tình huống ngoại trú nên chọn {G('amoxicillin–clavulanat liều cao')} thay amoxicillin, "
        f"và cách chọn dạng bào chế.",
        f"1) {R('Chưa tiêm Hib')} (nguy cơ H. influenzae tiết β-lactamase).<br>"
        f"2) {R('Viêm tai giữa kèm')}.<br>"
        f"3) {R('Vừa dùng amoxicillin trong 30 ngày')}.<br>"
        f"4) Dạng: {G('tỷ lệ cao 14:1')} để clavulanat {Y('≤ 10 mg/kg/ngày')}; nếu chỉ có 7:1/8:1 → {G('ghép amoxicillin đơn chất')} "
        f"cho đủ 90 mg/kg/ngày.",
        "Clavulanat gây tiêu chảy theo liều; dùng dạng 7:1 để đạt amoxicillin 90 mg/kg/ngày sẽ đưa clavulanat lên gần 13 mg/kg/ngày. "
        "Ghép amoxicillin đơn chất giữ đủ amoxicillin mà clavulanat vẫn trong ngưỡng.",
        "5.2 Phác đồ kinh nghiệm", ["Ngoai-tru", "Amox-clav"], warn=True,
    ),
    basic(
        "PED69-S5-04", "S5", "Nội trú", 1,
        f"{B('[Nội trú]')} Kháng sinh kinh nghiệm cho trẻ viêm phổi nhập viện: (a) {G('tiêm chủng đủ, phế cầu kháng thấp')}, "
        f"(b) {R('chưa tiêm đủ / kháng cao / nặng đe dọa tính mạng')}, (c) {B('nghi kèm không điển hình')}?",
        f"1) (a): {G('ampicillin 150–200 mg/kg/ngày chia 4')} hoặc {G('penicillin G')}; WHO: {G('ampicillin + gentamicin')} cho viêm phổi nặng.<br>"
        f"2) (b): {G('ceftriaxone 50–100 mg/kg/ngày')} hoặc {G('cefotaxime 150 mg/kg/ngày')}.<br>"
        f"3) (c): {G('β-lactam + macrolid')}; ngừng macrolid nếu xét nghiệm âm tính.",
        "Ở Việt Nam, phế cầu kháng thuốc cao và PCV chưa phủ đủ nên cephalosporin thế hệ 3 là lựa chọn nội trú phổ biến. Không có "
        "lý do dùng carbapenem hay cephalosporin thế hệ 4 làm kinh nghiệm cho viêm phổi cộng đồng.",
        "5.2 Phác đồ kinh nghiệm", ["Noi-tru"],
    ),
    basic(
        "PED69-S5-05", "S5", "Tụ cầu", 1,
        f"{B('[Nghi tụ cầu / CA-MRSA]')} Phác đồ khi nghi viêm phổi do tụ cầu vàng, phương án thay thế, và xuống thang khi cấy ra {B('MSSA')}?",
        f"1) Kinh nghiệm: {G('β-lactam + vancomycin')}; {G('clindamycin')} nếu nhạy và bệnh nặng vừa.<br>"
        f"2) Thay thế: {G('linezolid')} khi không dùng được vancomycin.<br>"
        f"3) Cấy ra {B('MSSA')}: xuống {G('cefazolin hoặc oxacillin')}.",
        "Vancomycin diệt MSSA kém hơn β-lactam kháng penicillinase, nên khi kháng sinh đồ cho thấy MSSA phải chuyển ngay. "
        "Clindamycin/linezolid ức chế tổng hợp độc tố (PVL) — có lợi trong viêm phổi hoại tử.",
        "5.2 Phác đồ kinh nghiệm", ["Tu-cau", "MRSA"],
    ),
    basic(
        "PED69-S5-06", "S5", "Hít", 2,
        f"{B('[Viêm phổi hít]')} Kháng sinh cho viêm phổi hít ở trẻ em (đường tĩnh mạch, đường uống, khi dị ứng penicillin)?",
        f"1) Tĩnh mạch: {G('ampicillin–sulbactam')}.<br>"
        f"2) Uống: {G('amoxicillin–clavulanat')}.<br>"
        f"3) Dị ứng penicillin: {G('clindamycin')}.<br>"
        f"4) {R('Viêm phổi hóa chất đơn thuần')}: {G('không cần kháng sinh')}.",
        "Ampicillin–sulbactam và amoxicillin–clavulanat đã phủ liên cầu miệng và vi khuẩn kỵ khí miệng, nên không cần thêm "
        "metronidazol ở viêm phổi hít cộng đồng không áp xe.",
        "5.2 Phác đồ kinh nghiệm", ["Hit"],
    ),
    basic(
        "PED69-S5-07", "S5", "Sơ sinh và nhũ nhi nhỏ", 1,
        f"{B('[Sơ sinh và Chlamydia]')} Kháng sinh cho viêm phổi {Y('sơ sinh')} và cho viêm phổi {B('Chlamydia trachomatis')} ở trẻ "
        f"{Y('1–3 tháng')}? Lưu ý an toàn?",
        f"1) {Y('Sơ sinh')}: {G('ampicillin + gentamicin')} (± {G('cefotaxime')}); {R('tránh ceftriaxone')} (vàng da nhân, tương kỵ calci).<br>"
        f"2) {B('Chlamydia trachomatis')}: {G('azithromycin 20 mg/kg/ngày × 3 ngày')}; thay thế {G('erythromycin 50 mg/kg/ngày chia 4 × 14 ngày')}.<br>"
        f"3) Lưu ý: macrolid ở trẻ {Y('< 6 tuần')} liên quan {R('hẹp phì đại môn vị')} → dặn theo dõi nôn vọt.",
        "Ampicillin phủ liên cầu nhóm B và Listeria (Listeria kháng tự nhiên cephalosporin), gentamicin phủ Gram âm. Azithromycin được "
        "ưu tiên hơn erythromycin vì liệu trình ngắn và ít nguy cơ hẹp môn vị hơn.",
        "5.2 Phác đồ kinh nghiệm", ["So-sinh", "Chlamydia"],
    ),
    basic(
        "PED69-S5-08", "S5", "Cúm", 1,
        f"{B('[Viêm phổi do cúm]')} Xử trí kháng virus và kháng sinh cho trẻ viêm phổi do cúm: dùng oseltamivir khi nào, có cần đợi xét nghiệm "
        f"hay đang ở giờ thứ mấy, và khi nào thêm kháng sinh?",
        f"1) {G('Oseltamivir càng sớm càng tốt')}, {G('không chờ xét nghiệm')} ở trẻ nhập viện / nặng / nguy cơ cao.<br>"
        f"2) Dùng {G('kể cả khi > 48 giờ')} từ khởi phát ở trẻ nhập viện.<br>"
        f"3) Nghi bội nhiễm → {G('thêm kháng sinh phủ phế cầu + tụ cầu')}.",
        "Mốc 48 giờ áp dụng cho trẻ khỏe mạnh bệnh nhẹ; ở trẻ nặng, oseltamivir muộn vẫn giảm tử vong. Bội nhiễm sau cúm hay do "
        "phế cầu và tụ cầu (kể cả MRSA) — trẻ sốt lại sau vài ngày đỡ là tín hiệu.",
        "5.2 Phác đồ kinh nghiệm", ["Cum"],
    ),
    basic(
        "PED69-S5-09", "S5", "HIV / PCP", 2,
        f"{B('[Nhũ nhi HIV nghi PCP]')} Phác đồ bổ sung cho nhũ nhi nhiễm HIV viêm phổi nặng nghi {B('Pneumocystis')}?",
        f"1) Thêm {G('cotrimoxazol liều cao')}: {G('TMP 15–20 mg/kg/ngày chia 3–4')} × {Y('21 ngày')}.<br>"
        f"2) {G('± corticoid')} khi giảm oxy nặng.<br>"
        f"3) Kèm {G('kháng sinh viêm phổi nặng chuẩn')}.",
        "PCP ở nhũ nhi HIV có tử vong rất cao; không có xét nghiệm nhanh sẵn ở đa số nơi nên điều trị theo kinh nghiệm khi bệnh cảnh "
        "phù hợp (giảm oxy nặng, phổi ít ran, mờ kẽ lan tỏa).",
        "5.2 Phác đồ kinh nghiệm", ["HIV", "PCP"],
    ),
    basic(
        "PED69-S5-10", "S5", "Dị ứng penicillin", 1,
        f"{B('[Dị ứng penicillin]')} Lựa chọn kháng sinh cho trẻ viêm phổi theo 3 kiểu dị ứng penicillin: {Y('không nặng')}, "
        f"{R('nặng tức thì')}, {Y('không rõ')}?",
        f"1) {Y('Không nặng, không phản vệ')} (ban muộn): {G('cephalosporin')} — {G('ceftriaxone')} (TM), {G('cefpodoxime, cefuroxime')} (uống); "
        f"phản ứng chéo thấp.<br>"
        f"2) {R('Nặng tức thì')} (phản vệ, mày đay toàn thân, phù mạch): {G('levofloxacin')} hoặc {G('linezolid')}; {G('clindamycin')} nếu phế cầu nhạy; "
        f"{R('macrolid đơn độc không tin cậy')} cho phế cầu ở châu Á.<br>"
        f"3) {Y('Không rõ')}: khai thác kỹ — nhiều trẻ bị {R('dán nhãn sai')}; cân nhắc test/thử thách thuốc khi ổn định.",
        "Phản ứng chéo penicillin – cephalosporin chủ yếu do chuỗi bên giống nhau; ceftriaxone, cefpodoxime có chuỗi bên khác "
        "amoxicillin nên an toàn ở trẻ dị ứng không nặng. Nhãn “dị ứng penicillin” sai buộc trẻ dùng thuốc phổ rộng, đắt và nhiều tác dụng phụ hơn.",
        "5.3 Dị ứng penicillin", ["Di-ung"],
    ),
    cloze(
        "PED69-S5-C1", "S5", "Chlamydia",
        f"Viêm phổi do Chlamydia trachomatis ở nhũ nhi điều trị bằng azithromycin {{{{c1::{G('20 mg/kg/ngày × 3 ngày')}}}}}.",
        "5.2 Phác đồ kinh nghiệm", ["Chlamydia"],
    ),
    cloze(
        "PED69-S5-C2", "S5", "Amoxicillin–clavulanat",
        f"Khi dùng amoxicillin–clavulanat liều cao, giữ clavulanat {{{{c1::{Y('≤ 10 mg/kg/ngày')}}}}} để hạn chế tiêu chảy.",
        "5.2 Phác đồ kinh nghiệm", ["Amox-clav"], warn=True,
    ),

    # ================================================================ S6. Mycoplasma kháng macrolid
    basic(
        "PED69-S6-01", "S6", "Dịch tễ kháng", 1,
        f"{B('[Mycoplasma kháng macrolid – dịch tễ]')} Cơ chế kháng, đột biến chính, và tỷ lệ kháng ở Trung Quốc/Hàn Quốc, "
        f"Việt Nam, châu Âu/Bắc Mỹ?",
        f"1) Cơ chế: {B('đột biến 23S rRNA')} làm macrolid {R('mất gắn ribosom')}; chủ yếu {B('A2063G')}.<br>"
        f"2) Trung Quốc, Hàn Quốc: thường {Y('> 80%')}.<br>"
        f"3) Việt Nam — BV Nhi Trung ương 2021–2023: {Y('69,9%')} (A2063G chiếm {Y('98,6%')} chủng kháng).<br>"
        f"4) Châu Âu/Bắc Mỹ: thấp ({Y('< 10–15%')}).",
        "Vì vậy guideline phương Tây (macrolid đầu tay cho Mycoplasma, đổi thuốc hiếm khi cần) phải áp dụng có điều chỉnh ở Việt Nam: "
        "theo dõi sát đáp ứng 48–72 giờ và chuẩn bị phương án thay thế.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma", "Khang-thuoc"], asks=["Cơ chế", "Trung Quốc", "Việt Nam", "Châu Âu"],
    ),
    basic(
        "PED69-S6-02", "S6", "Không đáp ứng", 1,
        f"{B('[Mycoplasma không đáp ứng macrolid]')} Định nghĩa không đáp ứng macrolid, và có nên đổi thuốc ngay chỉ vì tỷ lệ kháng cao không?",
        f"1) Định nghĩa: {R('sốt kéo dài, lâm sàng/X-quang xấu đi')} sau {Y('48–72 giờ')} macrolid đúng liều.<br>"
        f"2) Đổi thuốc ngay vì sợ kháng: {R('không')} — nhiều trẻ mang chủng kháng {G('vẫn khỏi với macrolid')} (bệnh tự giới hạn + tác dụng kháng viêm của macrolid) "
        f"→ quyết định dựa vào {G('đáp ứng lâm sàng 48–72 giờ')}.",
        "Nghiên cứu ở BV Nhi Trung ương ghi nhận phần lớn trẻ mang chủng kháng vẫn cải thiện. Đổi sang doxycycline/fluoroquinolon cho "
        "mọi trẻ ngay từ đầu sẽ đẩy nhanh kháng thuốc với nhóm dự trữ.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma"], asks=["Định nghĩa", "Đổi thuốc ngay"],
    ),
    basic(
        "PED69-S6-03", "S6", "Chuyển thuốc", 1,
        f"{B('[Chuyển thuốc khi kháng macrolid]')} Chọn thuốc thay thế cho Mycoplasma không đáp ứng macrolid ở trẻ {Y('≥ 8 tuổi')} và trẻ {Y('< 8 tuổi')}? "
        f"Liều doxycycline?",
        f"1) {Y('≥ 8 tuổi')}: {G('doxycycline')} (hoặc {G('minocycline')}).<br>"
        f"2) {Y('< 8 tuổi')}: {G('doxycycline đợt ngắn')} (AAP cho phép {Y('≤ 21 ngày')} ở mọi tuổi; Trung Quốc 2023 cho phép khi cân nhắc lợi – hại), "
        f"hoặc {G('fluoroquinolon')} (levofloxacin; tosufloxacin ở Nhật) — {R('ngoài chỉ định, cần đồng thuận')}.<br>"
        f"3) Doxycycline: {G('2–4 mg/kg/ngày chia 2')}, tối đa {Y('200 mg/ngày')}.",
        "Lo ngại nhuộm răng của tetracyclin chủ yếu với tetracyclin thế hệ cũ dùng dài; doxycycline gắn calci yếu hơn và đợt ngắn "
        "không làm đổi màu răng có ý nghĩa. Tetracyclin hạ sốt nhanh hơn fluoroquinolon trong các nghiên cứu ở Nhật, Trung Quốc.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma", "Doxycycline"], warn=True,
    ),
    basic(
        "PED69-S6-04", "S6", "RMPP", 1,
        f"{B('[Viêm phổi Mycoplasma kháng trị – RMPP]')} Định nghĩa RMPP, cơ chế chính, và các xét nghiệm gợi ý?",
        f"1) Định nghĩa: {R('sốt, tiến triển lâm sàng/X-quang')} dù đã {Y('≥ 7 ngày')} điều trị phù hợp.<br>"
        f"2) Cơ chế: {R('đáp ứng viêm quá mức của cơ thể')} (miễn dịch tế bào, cytokine), không chỉ do vi khuẩn.<br>"
        f"3) Xét nghiệm gợi ý: {R('LDH, CRP, ferritin, D-dimer tăng cao')}.",
        "Vì tổn thương chủ yếu do phản ứng của cơ thể, diệt vi khuẩn đơn thuần không đủ — đây là lý do guideline Trung Quốc thêm "
        "corticoid. LDH là dấu ấn hay được dùng nhất để dự báo thể kháng trị.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma", "RMPP"], asks=["Định nghĩa", "Cơ chế", "Xét nghiệm"],
    ),
    basic(
        "PED69-S6-05", "S6", "Corticoid", 2,
        f"{B('[Corticoid trong RMPP – Trung Quốc 2023]')} Liều methylprednisolon chuẩn và liều xung cho RMPP theo guideline Trung Quốc 2023, "
        f"và mức độ bằng chứng ở phương Tây?",
        f"1) Chuẩn: {G('methylprednisolon 1–2 mg/kg/ngày')} × {Y('3–5 ngày')}.<br>"
        f"2) Rất nặng: {G('liều xung 10–30 mg/kg/ngày')} × {Y('3 ngày')} (tối đa {Y('1 g')}).<br>"
        f"3) Phương Tây: {R('chưa có trong guideline')} — chỉ là tham khảo.",
        "Corticoid làm hạ sốt nhanh và giảm viêm trong các nghiên cứu quan sát/thử nghiệm nhỏ ở Trung Quốc, nhưng chưa có thử nghiệm "
        "lớn đa quốc gia. Khi dùng phải chắc đã điều trị đúng kháng sinh và loại trừ lao, nhiễm khuẩn khác.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma", "Corticoid"], warn=True,
    ),
    basic(
        "PED69-S6-06", "S6", "Biến chứng Mycoplasma", 2,
        f"{B('[Biến chứng Mycoplasma nặng]')} Kể các biến chứng tại phổi và ngoài phổi cần tìm ở trẻ Mycoplasma nặng/kháng trị và xử trí gợi ý.",
        f"1) {R('Đông đặc lớn / xẹp phổi')}, {R('viêm phế quản tạo khuôn (plastic bronchitis)')} → {G('nội soi phế quản')}.<br>"
        f"2) {R('Hoại tử phổi')}.<br>"
        f"3) {R('Huyết khối')} (D-dimer cao).<br>"
        f"4) {R('Tràn dịch màng phổi')}.<br>"
        f"5) Ngoài phổi: {R('MIRM / SJS')}, {R('tan máu')}, {R('viêm não')}.",
        "Viêm phế quản tạo khuôn là các nút fibrin bít khuôn cây phế quản, gây xẹp cả thùy — kháng sinh không giải quyết được, cần "
        "nội soi gắp/rửa. Huyết khối (phổi, não, chi) là biến chứng ít gặp nhưng nặng.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma", "Bien-chung"],
    ),
    cloze(
        "PED69-S6-C1", "S6", "Dịch tễ kháng",
        f"Tại Bệnh viện Nhi Trung ương 2021–2023, tỷ lệ Mycoplasma kháng macrolid ở trẻ viêm phổi là {{{{c1::{Y('69,9%')}}}}}.",
        "5.4 Mycoplasma kháng macrolid", ["Khang-thuoc"],
    ),
    cloze(
        "PED69-S6-C2", "S6", "Dịch tễ kháng",
        f"Đột biến kháng macrolid chiếm ưu thế của Mycoplasma pneumoniae ở Việt Nam là {{{{c1::{B('A2063G')}}}}} trên gen 23S rRNA.",
        "5.4 Mycoplasma kháng macrolid", ["Khang-thuoc"],
    ),
    cloze(
        "PED69-S6-C3", "S6", "Không đáp ứng",
        f"Đánh giá Mycoplasma không đáp ứng macrolid sau {{{{c1::{Y('48–72 giờ')}}}}} điều trị đúng liều.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma"],
    ),

    # ================================================================ S7. Liều
    basic(
        "PED69-S7-01", "S7", "Liều uống", 1,
        f"{B('[Liều macrolid và doxycycline]')} Liều {G('azithromycin')}, {G('clarithromycin')}, {G('erythromycin')}, {G('doxycycline')} "
        f"đường uống cho viêm phổi trẻ em?",
        f"1) {G('Azithromycin')}: {Y('10 mg/kg ngày 1')} (tối đa 500 mg) → {Y('5 mg/kg ngày 2–5')} (tối đa 250 mg).<br>"
        f"2) {G('Clarithromycin')}: {Y('15 mg/kg/ngày chia 2')} × 7–14 ngày (tối đa 1 g/ngày).<br>"
        f"3) {G('Erythromycin')}: {Y('40–50 mg/kg/ngày chia 4')}.<br>"
        f"4) {G('Doxycycline')}: {Y('2–4 mg/kg/ngày chia 2')} (tối đa 200 mg/ngày).",
        "Azithromycin có thời gian bán thải mô rất dài nên 5 ngày tạo nồng độ mô kéo dài thêm nhiều ngày sau liều cuối. Erythromycin "
        "nhiều tác dụng phụ tiêu hóa (kích thích motilin) nên ít dùng.",
        "6. Bảng liều", ["Lieu"],
    ),
    basic(
        "PED69-S7-02", "S7", "Liều uống", 1,
        f"{B('[Liều thuốc thay thế đường uống]')} Liều {G('levofloxacin')}, {G('linezolid')}, {G('clindamycin')}, {G('cefpodoxime')}, "
        f"{G('cefuroxime axetil')} cho trẻ viêm phổi?",
        f"1) {G('Levofloxacin')}: {Y('6 tháng – < 5 tuổi 16–20 mg/kg/ngày chia 2')}; {Y('5–16 tuổi 8–10 mg/kg/ngày 1 lần')} (tối đa 750 mg/ngày).<br>"
        f"2) {G('Linezolid')}: {Y('< 12 tuổi 30 mg/kg/ngày chia 3')}; {Y('≥ 12 tuổi 20 mg/kg/ngày chia 2')} (tối đa 600 mg/lần).<br>"
        f"3) {G('Clindamycin')}: {Y('30–40 mg/kg/ngày chia 3–4')}.<br>"
        f"4) {G('Cefpodoxime')}: {Y('10 mg/kg/ngày chia 2')} (tối đa 400 mg).<br>"
        f"5) {G('Cefuroxime axetil')}: {Y('30 mg/kg/ngày chia 2')} (tối đa 1 g).",
        "Trẻ nhỏ thải trừ levofloxacin và linezolid nhanh hơn người lớn → phải chia nhiều lần hơn (levofloxacin 2 lần dưới 5 tuổi, "
        "linezolid 3 lần dưới 12 tuổi). Linezolid uống sinh khả dụng gần 100% nên chuyển uống không cần đổi liều.",
        "6. Bảng liều", ["Lieu"], warn=True,
    ),
    basic(
        "PED69-S7-03", "S7", "Liều tĩnh mạch", 1,
        f"{B('[Liều β-lactam tĩnh mạch]')} Liều {G('ampicillin')} (PIDS và WHO), {G('penicillin G')}, {G('ceftriaxone')} (PIDS, WHO, tối đa), "
        f"{G('cefotaxime')}, {G('ampicillin–sulbactam')}?",
        f"1) {G('Ampicillin')}: {Y('150–200 mg/kg/ngày chia 4')} (PIDS); WHO {Y('50 mg/kg mỗi 6 giờ')}; phế cầu kháng cao đến {Y('300–400 mg/kg/ngày')}.<br>"
        f"2) {G('Penicillin G')}: {Y('200.000–250.000 UI/kg/ngày chia 4–6')}.<br>"
        f"3) {G('Ceftriaxone')}: {Y('50–100 mg/kg/ngày chia 1–2')} (PIDS); WHO {Y('80 mg/kg/ngày')}; tối đa {Y('2 g/ngày')} (viêm màng não 4 g).<br>"
        f"4) {G('Cefotaxime')}: {Y('150 mg/kg/ngày chia 3')}.<br>"
        f"5) {G('Ampicillin–sulbactam')}: ampicillin {Y('150–200 mg/kg/ngày chia 4')}.",
        "β-lactam diệt khuẩn phụ thuộc thời gian trên MIC, nên ampicillin, penicillin, cefotaxime (bán thải ngắn) phải chia nhiều lần; "
        "ceftriaxone bán thải dài nên 1–2 lần/ngày đủ.",
        "6. Bảng liều", ["Lieu"],
    ),
    basic(
        "PED69-S7-04", "S7", "Liều tĩnh mạch", 2,
        f"{B('[Liều thuốc tĩnh mạch khác]')} Liều {G('gentamicin')} (WHO), {G('vancomycin')} (và cách theo dõi), {G('clindamycin')} TM, "
        f"{G('azithromycin')} TM?",
        f"1) {G('Gentamicin')}: {Y('7,5 mg/kg 1 lần/ngày')} — theo dõi thận, thính lực.<br>"
        f"2) {G('Vancomycin')}: {Y('40–60 mg/kg/ngày chia 3–4')}; theo dõi theo {Y('AUC 400–600')} (đồng thuận 2020) hoặc nồng độ đáy.<br>"
        f"3) {G('Clindamycin')}: {Y('40 mg/kg/ngày chia 3–4')}.<br>"
        f"4) {G('Azithromycin')}: {Y('10 mg/kg/ngày × 2 ngày')} rồi chuyển uống.",
        "Đồng thuận vancomycin 2020 (ASHP/IDSA/PIDS) chuyển từ nhắm nồng độ đáy 15–20 sang AUC 400–600 vì đạt hiệu quả tương đương "
        "mà ít độc thận hơn. Nơi chưa tính được AUC vẫn dùng nồng độ đáy.",
        "6. Bảng liều", ["Lieu", "Vancomycin"],
    ),
    basic(
        "PED69-S7-05", "S7", "Oseltamivir", 1,
        f"{B('[Liều oseltamivir – CDC]')} Liều oseltamivir điều trị cho trẻ {Y('< 1 tuổi')} và trẻ {Y('≥ 1 tuổi')} theo cân nặng, số lần, thời gian?",
        f"1) {Y('< 1 tuổi')}: {G('3 mg/kg/lần × 2 lần/ngày')}.<br>"
        f"2) {Y('≥ 1 tuổi')} theo cân nặng (mỗi liều, 2 lần/ngày): {Y('≤ 15 kg 30 mg')}; {Y('15–23 kg 45 mg')}; {Y('23–40 kg 60 mg')}; {Y('> 40 kg 75 mg')}.<br>"
        f"3) Thời gian: {Y('5 ngày')}.",
        "Bậc cân nặng 15 – 23 – 40 kg là mốc chuyển liều; mẹo nhớ “30 – 45 – 60 – 75” tăng đều 15 mg. Dự phòng sau phơi nhiễm dùng "
        "cùng liều nhưng 1 lần/ngày.",
        "6. Bảng liều", ["Lieu", "Cum"],
    ),
    cloze(
        "PED69-S7-C1", "S7", "Levofloxacin",
        f"Levofloxacin cho trẻ 6 tháng đến dưới 5 tuổi: {{{{c1::{Y('16–20 mg/kg/ngày chia 2')}}}}}; trẻ 5–16 tuổi: "
        f"{{{{c2::{Y('8–10 mg/kg/ngày 1 lần')}}}}}.",
        "6. Bảng liều", ["Lieu"], warn=True,
    ),
    cloze(
        "PED69-S7-C2", "S7", "Linezolid",
        f"Linezolid cho trẻ dưới 12 tuổi: {{{{c1::{Y('30 mg/kg/ngày chia 3')}}}}}.",
        "6. Bảng liều", ["Lieu"],
    ),
    cloze(
        "PED69-S7-C3", "S7", "Gentamicin",
        f"WHO: gentamicin phối hợp ampicillin cho viêm phổi nặng liều {{{{c1::{Y('7,5 mg/kg 1 lần/ngày')}}}}}.",
        "6. Bảng liều", ["Lieu"],
    ),
    cloze(
        "PED69-S7-C4", "S7", "Vancomycin",
        f"Theo đồng thuận 2020, vancomycin được chỉnh liều theo mục tiêu {{{{c1::{Y('AUC 400–600')}}}}}.",
        "6. Bảng liều", ["Vancomycin"],
    ),
    cloze(
        "PED69-S7-C5", "S7", "Amoxicillin",
        f"Amoxicillin liều cao cho viêm phổi theo PIDS: 90 mg/kg/ngày chia 2, tối đa {{{{c1::{Y('4 g/ngày')}}}}}.",
        "6. Bảng liều", ["Lieu"], warn=True,
    ),

    # ================================================================ S8. Thời gian, chuyển uống, ra viện, hỗ trợ
    basic(
        "PED69-S8-01", "S8", "Thời gian – bằng chứng", 1,
        f"{B('[SCOUT-CAP]')} Thử nghiệm SCOUT-CAP (JAMA Pediatr 2022) so sánh gì, trên đối tượng nào, kết quả và điểm mới so với CAP-IT, SAFER?",
        f"1) So sánh: kháng sinh {Y('5 ngày')} vs {Y('10 ngày')}.<br>"
        f"2) Đối tượng: trẻ {Y('6–71 tháng')} viêm phổi điều trị ngoại trú, đã cải thiện sau những ngày đầu.<br>"
        f"3) Kết quả: {G('5 ngày tốt hơn')} theo thang tổng hợp lợi – hại (DOOR/RADAR), {G('ít gen kháng thuốc')} ở hệ vi khuẩn hầu họng.<br>"
        f"4) Điểm mới: không chỉ “không thua” mà {G('có lợi hơn')} khi rút ngắn.",
        "CAP-IT chứng minh 3 ngày không thua 7 ngày, SAFER chứng minh 5 ngày không thua 10 ngày; SCOUT-CAP thêm bằng chứng rằng kéo "
        "dài gây hại (tác dụng phụ, chọn lọc kháng thuốc) mà không thêm lợi.",
        "7. Thời gian", ["Thoi-gian", "SCOUT-CAP"], asks=["So sánh", "Đối tượng", "Kết quả", "Điểm mới"],
    ),
    basic(
        "PED69-S8-02", "S8", "Thời gian", 1,
        f"{B('[Thời gian kháng sinh]')} Thời gian kháng sinh cho: viêm phổi ngoại trú không biến chứng, nội trú không biến chứng, "
        f"Mycoplasma, tràn mủ màng phổi, viêm phổi hoại tử/áp xe/tụ cầu?",
        f"1) Ngoại trú không biến chứng: {Y('5 ngày')} (hoặc {Y('3 ngày')} theo CAP-IT; WHO 3 ngày thở nhanh / 5 ngày rút lõm).<br>"
        f"2) Nội trú không biến chứng: tổng thường {Y('5–7 ngày')}, chuyển uống sớm.<br>"
        f"3) Mycoplasma: azithromycin {Y('5 ngày')}; clarithromycin/doxycycline {Y('7–14 ngày')}.<br>"
        f"4) Tràn mủ màng phổi: tổng {Y('2–4 tuần')}.<br>"
        f"5) Hoại tử, áp xe, tụ cầu: thường {Y('≥ 2–4 tuần')}, theo đáp ứng.",
        "Bằng chứng mạnh nhất là ở trẻ ngoại trú; thời gian nội trú 5–7 ngày là ngoại suy hợp lý. Biến chứng có mủ cần lâu hơn vì "
        "kháng sinh thấm kém vào ổ mủ — dẫn lưu tốt mới rút ngắn được.",
        "7. Thời gian", ["Thoi-gian"], warn=True,
    ),
    basic(
        "PED69-S8-03", "S8", "Chuyển uống", 1,
        f"{B('[Chuyển tĩnh mạch sang uống]')} Tiêu chí chuyển kháng sinh tĩnh mạch sang đường uống và cách chọn thuốc uống?",
        f"1) {G('Hết sốt hoặc cải thiện rõ')}.<br>"
        f"2) {G('Giảm thở nhanh')}, giảm công thở.<br>"
        f"3) {G('Uống được')}, không nôn.<br>"
        f"4) {G('Không có biến chứng cần thủ thuật')} đang xử trí.<br>"
        f"5) Thuốc uống {G('cùng phổ')} (thường amoxicillin liều cao; theo kết quả cấy nếu có).",
        "Không cần chờ hết sốt hoàn toàn hay CRP về bình thường; chuyển uống sớm giảm đặt lại đường truyền, nhiễm trùng catheter và "
        "rút ngắn nằm viện.",
        "7. Chuyển uống", ["Chuyen-uong"],
    ),
    basic(
        "PED69-S8-04", "S8", "Ra viện", 1,
        f"{B('[Tiêu chuẩn ra viện – PIDS]')} Kể các tiêu chuẩn cho trẻ viêm phổi ra viện theo PIDS/IDSA.",
        f"1) {G('Cải thiện chung')} (hoạt động, ăn, giảm sốt) ≥ {Y('12–24 giờ')}.<br>"
        f"2) {G('SpO₂ > 90% khí trời')} ≥ {Y('12–24 giờ')}.<br>"
        f"3) {G('Tri giác bình thường')}.<br>"
        f"4) {G('Không tăng công thở')}, nhịp thở cải thiện.<br>"
        f"5) {G('Uống được thuốc và dịch')}.<br>"
        f"6) Nếu có dẫn lưu: {G('đã rút')} ≥ {Y('12–24 giờ')} không xấu đi.<br>"
        f"7) {G('Gia đình đủ khả năng theo dõi')}, tái khám được.",
        "Kết quả cấy máu đang chờ không phải lý do giữ trẻ khi đủ các tiêu chí trên và theo dõi được.",
        "7. Ra viện", ["Ra-vien"],
    ),
    basic(
        "PED69-S8-05", "S8", "Hỗ trợ", 1,
        f"{B('[Điều trị hỗ trợ]')} Ngưỡng cho oxy (WHO, BTS), cách truyền dịch, và những biện pháp {R('không nên')} dùng trong viêm phổi trẻ em?",
        f"1) {G('Oxy')} khi {Y('SpO₂ < 90%')} (WHO) / {Y('< 92%')} (BTS); nâng bậc HFNC/CPAP khi suy hô hấp tiến triển.<br>"
        f"2) {G('Dịch')}: ưu tiên uống; nếu truyền → {G('dịch đẳng trương')}, khoảng {Y('80% nhu cầu cơ bản')}, theo dõi natri.<br>"
        f"3) {R('Không')}: vật lý trị liệu hô hấp thường quy (BTS); {R('không')} thuốc giảm ho, long đờm cho trẻ nhỏ.<br>"
        f"4) {G('Hạ sốt, giảm đau')} (đau ngực màng phổi): paracetamol / ibuprofen.",
        "Hạn chế dịch và dùng dịch đẳng trương vì nguy cơ SIADH gây hạ natri, co giật. Vỗ rung không rút ngắn bệnh ở viêm phổi cấp và "
        "làm trẻ mệt thêm.",
        "8. Hỗ trợ", ["Ho-tro"],
    ),
    cloze(
        "PED69-S8-C1", "S8", "SCOUT-CAP",
        f"SCOUT-CAP (2022): ở trẻ 6–71 tháng viêm phổi ngoại trú, kháng sinh {{{{c1::{Y('5 ngày')}}}}} tốt hơn 10 ngày và ít gen kháng thuốc hơn.",
        "7. Thời gian", ["SCOUT-CAP"],
    ),
    cloze(
        "PED69-S8-C2", "S8", "Ra viện",
        f"Tiêu chuẩn ra viện PIDS: SpO₂ {{{{c1::{Y('> 90% khí trời')}}}}} duy trì ít nhất {{{{c2::{Y('12–24 giờ')}}}}}.",
        "7. Ra viện", ["Ra-vien"],
    ),
    cloze(
        "PED69-S8-C3", "S8", "Tràn mủ",
        f"Tổng thời gian kháng sinh cho tràn mủ màng phổi ở trẻ em thường là {{{{c1::{Y('2–4 tuần')}}}}}.",
        "7. Thời gian", ["Thoi-gian"],
    ),

    # ================================================================ S9. Thất bại, biến chứng, phòng bệnh, bẫy
    basic(
        "PED69-S9-01", "S9", "Thất bại điều trị", 1,
        f"{B('[Không đáp ứng 48–72 giờ]')} Kể 4 nhóm lý do trẻ viêm phổi không đáp ứng sau 48–72 giờ và ví dụ mỗi nhóm.",
        f"1) {R('Sai chẩn đoán')}: virus, hen/khò khè, {R('dị vật')}, suy tim/viêm cơ tim, lao, bất thường bẩm sinh (CPAM, phổi biệt lập).<br>"
        f"2) {R('Sai thuốc / liều')}: amoxicillin liều thấp, tác nhân không điển hình (β-lactam vô hiệu), {B('MRSA')}, Gram âm, "
        f"{B('Mycoplasma kháng macrolid')}, nôn – không uống được.<br>"
        f"3) {R('Có biến chứng')}: {R('tràn dịch / tràn mủ')}, hoại tử, áp xe, nhiễm khuẩn huyết, ổ di bệnh (viêm màng não, viêm xương).<br>"
        f"4) {R('Cơ địa')}: suy giảm miễn dịch, HIV, xơ nang, rối loạn nuốt/hít tái diễn.",
        "Câu hỏi đúng không phải “đổi sang kháng sinh mạnh hơn nào?” mà “vì sao chưa đáp ứng?”. Phần lớn trường hợp là biến chứng "
        "tràn dịch hoặc sai tác nhân, không phải kháng sinh “yếu”.",
        "9. Không đáp ứng", ["That-bai"],
    ),
    basic(
        "PED69-S9-02", "S9", "Thất bại điều trị", 1,
        f"{B('[Hành động khi không đáp ứng]')} Khi trẻ viêm phổi không đáp ứng 48–72 giờ, cần làm gì (khám, hình ảnh, xét nghiệm, điều chỉnh thuốc)?",
        f"1) {G('Khám lại toàn diện')}.<br>"
        f"2) {G('X-quang + siêu âm màng phổi')}; {G('CT')} khi nghi hoại tử/áp xe.<br>"
        f"3) {G('CTM, CRP/PCT, cấy máu')}; {G('PCR Mycoplasma / virus')}.<br>"
        f"4) {G('Mở rộng phổ theo giả thuyết')}: thêm vancomycin/clindamycin (tụ cầu) hoặc macrolid (không điển hình), "
        f"hoặc chuyển doxycycline (Mycoplasma kháng macrolid).",
        "Mở rộng phổ phải có giả thuyết cụ thể: nâng từ ceftriaxone lên carbapenem không giải quyết tụ cầu MRSA, Mycoplasma hay tràn "
        "mủ chưa dẫn lưu.",
        "9. Không đáp ứng", ["That-bai"],
    ),
    basic(
        "PED69-S9-03", "S9", "Tràn dịch", 1,
        f"{B('[Tràn dịch cận viêm – phân loại PIDS]')} Phân loại kích thước tràn dịch cận viêm theo PIDS và xử trí mỗi mức?",
        f"1) {Y('Nhỏ')}: {Y('< 10 mm')} trên phim nằm nghiêng hoặc {Y('< ¼ nửa ngực')} → {G('kháng sinh, không chọc hút')}.<br>"
        f"2) {Y('Trung bình')}: {Y('> 10 mm nhưng < ½ nửa ngực')} → {G('dẫn lưu nếu suy hô hấp hoặc dịch là mủ')}.<br>"
        f"3) {Y('Lớn')}: {Y('≥ ½ nửa ngực')} → {G('dẫn lưu')} (ống ± tiêu sợi huyết, hoặc VATS).",
        "Kích thước dịch + tình trạng hô hấp + tính chất dịch (mủ, vách) quyết định dẫn lưu, không phải một con số sinh hóa. Dịch nhỏ "
        "đa số tự tiêu khi điều trị kháng sinh đúng.",
        "10.1 Tràn dịch – tràn mủ", ["Tran-dich"],
    ),
    basic(
        "PED69-S9-04", "S9", "Tràn mủ", 2,
        f"{B('[Tràn mủ màng phổi]')} Tác nhân thường gặp của tràn mủ màng phổi ở trẻ em, so sánh {G('tiêu sợi huyết')} với {G('VATS')}, "
        f"và kháng sinh?",
        f"1) Tác nhân: {B('phế cầu')} (serotype {Y('1, 3, 19A')}), {B('tụ cầu vàng')}, {B('liên cầu nhóm A')}.<br>"
        f"2) Tiêu sợi huyết vs VATS: {G('urokinase qua ống dẫn lưu')} và {G('VATS')} {G('hiệu quả tương đương')} trong tràn mủ có vách — chọn theo nguồn lực.<br>"
        f"3) Kháng sinh: {G('TM phủ phế cầu ± tụ cầu')}, tổng {Y('2–4 tuần')}.",
        "Serotype 3 và 19A vẫn gây tràn mủ dù đã có PCV vì vắc xin bảo vệ kém (serotype 3) hoặc thay thế serotype. Tiêu sợi huyết "
        "phá vách fibrin giúp dẫn lưu thông — tránh được phẫu thuật ở đa số trẻ.",
        "10.1 Tràn dịch – tràn mủ", ["Tran-mu"], asks=["Tác nhân", "Tiêu sợi huyết", "Kháng sinh"],
    ),
    basic(
        "PED69-S9-05", "S9", "Biến chứng khác", 2,
        f"{B('[Biến chứng khác]')} Kể các biến chứng khác của viêm phổi trẻ em (tại phổi, toàn thân) và lưu ý đặc biệt với {B('HUS do phế cầu')}.",
        f"1) {R('Viêm phổi hoại tử / áp xe')}: phế cầu, tụ cầu (PVL) — thường điều trị nội khoa kéo dài, tránh dẫn lưu áp xe nếu không cần.<br>"
        f"2) {R('Tràn khí màng phổi, rò phế quản – màng phổi')}.<br>"
        f"3) {B('HUS do phế cầu')}: thiếu máu tan máu, giảm tiểu cầu, suy thận — {R('tránh truyền huyết tương')} (kháng nguyên T bộc lộ).<br>"
        f"4) {R('SIADH – hạ natri')}; {R('nhiễm khuẩn huyết, sốc')}; {R('viêm màng não')}.<br>"
        f"5) Theo tác nhân: Mycoplasma (tạo khuôn, huyết khối, MIRM/SJS, viêm não); Adenovirus ({R('viêm tiểu phế quản tắc nghẽn – BO')}).",
        "Neuraminidase của phế cầu cắt acid sialic, bộc lộ kháng nguyên T trên hồng cầu, tiểu cầu, nội mô thận; huyết tương người lớn "
        "có sẵn kháng thể kháng T nên truyền vào làm tan máu nặng thêm.",
        "10.2 Biến chứng khác", ["Bien-chung", "HUS"],
    ),
    basic(
        "PED69-S9-06", "S9", "Phòng bệnh", 1,
        f"{B('[Phòng bệnh]')} Kể các biện pháp phòng viêm phổi trẻ em: vắc xin, phòng RSV, và biện pháp chung.",
        f"1) {G('Vắc xin')}: {G('PCV')}, {G('Hib')}, {G('ho gà')}, {G('sởi')}, {G('cúm hằng năm')} từ {Y('6 tháng')}.<br>"
        f"2) {G('RSV')}: {G('nirsevimab')} 1 liều cho nhũ nhi trong mùa RSV đầu tiên, hoặc {G('vắc xin RSV cho mẹ')} lúc {Y('32–36 tuần')} thai.<br>"
        f"3) Chung: {G('bú mẹ hoàn toàn 6 tháng')}, {R('tránh khói thuốc, khói bếp')}, rửa tay, dinh dưỡng, kẽm, vitamin A theo chương trình, "
        f"{G('dự phòng cotrimoxazol')} cho trẻ phơi nhiễm/nhiễm HIV.",
        "Sởi và ho gà là hai bệnh vắc xin phòng được nhưng gây viêm phổi tử vong cao ở trẻ nhỏ; trong các thử nghiệm, nirsevimab "
        "giảm phần lớn (khoảng 60–80%) số nhập viện do RSV.",
        "11. Phòng bệnh", ["Phong-benh"],
    ),
    basic(
        "PED69-S9-07", "S9", "Bẫy", 1,
        f"{B('[Bẫy chẩn đoán căn nguyên]')} Kể 4 bẫy về xét nghiệm căn nguyên và cách làm đúng tương ứng.",
        f"1) {R('Dùng CRP/PCT đơn độc quyết định kháng sinh')} → {G('kết hợp lâm sàng, tuổi, X-quang; biomarker chỉ hỗ trợ')}.<br>"
        f"2) {R('Làm kháng nguyên phế cầu niệu')} → {G('không làm — dương tính giả do mang trùng')}.<br>"
        f"3) {R('Kết luận Mycoplasma vì IgM dương một lần')} → {G('ưu tiên PCR')}.<br>"
        f"4) {R('Chụp X-quang kiểm tra cho mọi trẻ')} → {G('chỉ khi tái diễn, xẹp thùy, viêm phổi tròn, xấu đi')}.",
        "Cả bốn bẫy đều dẫn đến kê kháng sinh sai (thừa hoặc sai thuốc) dựa trên một xét nghiệm có giá trị dự đoán kém ở trẻ em.",
        "12. Bẫy", ["Bay"],
    ),
    basic(
        "PED69-S9-08", "S9", "Bẫy", 1,
        f"{B('[Bẫy lựa chọn kháng sinh]')} Kể 4 bẫy về lựa chọn và thời gian kháng sinh, kèm cách làm đúng.",
        f"1) {R('Macrolid đơn độc cho viêm phổi nghi phế cầu')} → {G('β-lactam')} (phế cầu kháng macrolid rất cao ở châu Á).<br>"
        f"2) {R('Đổi kháng sinh ngày 2 vì còn sốt')} → {G('đợi đủ 48–72 giờ')} nếu không xấu đi.<br>"
        f"3) {R('Tăng bậc cephalosporin khi Mycoplasma không đáp ứng')} → {G('chuyển doxycycline/fluoroquinolon, tìm biến chứng')}.<br>"
        f"4) {R('Kéo dài 10–14 ngày cho viêm phổi không biến chứng')} → {G('5 ngày (hoặc 3 ngày)')}.",
        "Sốt giảm dần trong 2–3 ngày là diễn tiến bình thường của viêm phổi vi khuẩn được điều trị đúng; đổi thuốc quá sớm làm mất "
        "khả năng đánh giá thuốc nào hiệu quả.",
        "12. Bẫy", ["Bay"],
    ),
    cloze(
        "PED69-S9-C1", "S9", "Tràn dịch",
        f"Theo PIDS, tràn dịch cận viêm lớn (≥ {{{{c1::{Y('½ nửa ngực')}}}}}) cần dẫn lưu.",
        "10.1 Tràn dịch – tràn mủ", ["Tran-dich"],
    ),
    cloze(
        "PED69-S9-C2", "S9", "HUS",
        f"Trong HUS do phế cầu cần tránh truyền {{{{c1::{R('huyết tương')}}}}} vì kháng nguyên T đã bộc lộ.",
        "10.2 Biến chứng khác", ["HUS"],
    ),
    cloze(
        "PED69-S9-C3", "S9", "Phòng bệnh",
        f"Phòng RSV cho nhũ nhi bằng kháng thể đơn dòng {{{{c1::{G('nirsevimab')}}}}} 1 liều trong mùa RSV đầu tiên.",
        "11. Phòng bệnh", ["Phong-benh"],
    ),

    # ================================================================ ⚡ Thuật toán quyết định
    algo(
        "PED69-A-01", "S5", "Chọn kháng sinh kinh nghiệm",
        "Chọn kháng sinh kinh nghiệm cho trẻ viêm phổi theo tình huống",
        f"1) {Y('Sơ sinh')} → {G('ampicillin + gentamicin')} (± cefotaxime).<br>"
        f"2) {Y('1–3 tháng')}, không sốt, ho từng tiếng → {B('Chlamydia')}: {G('azithromycin 20 mg/kg × 3 ngày')}.<br>"
        f"3) Ngoại trú, &gt; 3 tháng → {G('amoxicillin 90 mg/kg/ngày chia 2 × 5 ngày')}; bệnh cảnh không điển hình (≥ 5 tuổi) → {G('azithromycin')}.<br>"
        f"4) Nội trú → {G('ampicillin')} (tiêm chủng đủ) hoặc {G('ceftriaxone/cefotaxime')} (chưa đủ, kháng cao, nặng); ± {G('macrolid')} nếu nghi không điển hình.<br>"
        f"5) Nghi {B('tụ cầu')} (sau cúm/thủy đậu, bóng khí, hoại tử) → {G('+ vancomycin')} (hoặc clindamycin).<br>"
        f"6) {B('Hít')} → {G('ampicillin–sulbactam / amoxicillin–clavulanat')}; {B('cúm')} → {G('+ oseltamivir')}; "
        f"{B('HIV nhũ nhi')} → {G('+ cotrimoxazol')}.",
        "Đọc từ trên xuống: tuổi → nơi điều trị → bối cảnh đặc biệt. Mỗi bước chỉ thêm thuốc khi có giả thuyết tác nhân cụ thể.",
        "5. Lựa chọn kháng sinh", ["Lua-chon"],
    ),
    algo(
        "PED69-A-02", "S7", "Liều uống bỏ túi",
        "Bảng liều kháng sinh đường uống bỏ túi",
        f"1) {G('Amoxicillin')} {Y('90 mg/kg/ngày chia 2')} (tối đa 4 g); WHO 40 mg/kg/lần × 2.<br>"
        f"2) {G('Amoxicillin–clavulanat')} amoxicillin {Y('90 mg/kg/ngày chia 2')}, clavulanat ≤ 10 mg/kg/ngày.<br>"
        f"3) {G('Azithromycin')} {Y('10 → 5 mg/kg × 5 ngày')}; Chlamydia {Y('20 mg/kg × 3 ngày')}.<br>"
        f"4) {G('Clarithromycin')} {Y('15 mg/kg/ngày chia 2')}.<br>"
        f"5) {G('Doxycycline')} {Y('2–4 mg/kg/ngày chia 2')} (tối đa 200 mg).<br>"
        f"6) {G('Levofloxacin')} {Y('16–20 mg/kg/ngày chia 2')} (< 5 tuổi) / {Y('8–10 mg/kg 1 lần')} (5–16 tuổi).<br>"
        f"7) {G('Linezolid')} {Y('30 mg/kg/ngày chia 3')} (< 12 tuổi).<br>"
        f"8) {G('Oseltamivir')} {Y('30 – 45 – 60 – 75 mg × 2/ngày')} theo bậc 15 – 23 – 40 kg; < 1 tuổi 3 mg/kg × 2.",
        "Luôn kiểm tra liều tối đa người lớn sau khi nhân mg/kg — trẻ lớn, nặng cân dễ vượt trần.",
        "6. Bảng liều", ["Lieu"], warn=True,
    ),
    algo(
        "PED69-A-03", "S7", "Liều tĩnh mạch bỏ túi",
        "Bảng liều kháng sinh tĩnh mạch bỏ túi",
        f"1) {G('Ampicillin')} {Y('150–200 mg/kg/ngày chia 4')} (WHO 50 mg/kg mỗi 6 giờ).<br>"
        f"2) {G('Gentamicin')} {Y('7,5 mg/kg 1 lần/ngày')}.<br>"
        f"3) {G('Ceftriaxone')} {Y('50–100 mg/kg/ngày')} (WHO 80), tối đa {Y('2 g/ngày')}.<br>"
        f"4) {G('Cefotaxime')} {Y('150 mg/kg/ngày chia 3')}.<br>"
        f"5) {G('Vancomycin')} {Y('40–60 mg/kg/ngày chia 3–4')}, AUC 400–600.<br>"
        f"6) {G('Clindamycin')} {Y('40 mg/kg/ngày chia 3–4')}.<br>"
        f"7) {G('Ampicillin–sulbactam')} ampicillin {Y('150–200 mg/kg/ngày chia 4')}.<br>"
        f"8) {G('Cotrimoxazol')} (PCP) TMP {Y('15–20 mg/kg/ngày chia 3–4')} × 21 ngày.",
        "Thuốc bán thải ngắn (ampicillin, cefotaxime, vancomycin, clindamycin) chia nhiều lần; ceftriaxone và gentamicin (diệt khuẩn "
        "phụ thuộc nồng độ) dùng 1 lần/ngày.",
        "6. Bảng liều", ["Lieu"],
    ),
    algo(
        "PED69-A-04", "S9", "Không đáp ứng 48–72 giờ",
        "Trẻ viêm phổi không đáp ứng 48–72 giờ: lưu đồ",
        f"1) {G('Kiểm tra lại')}: đúng chẩn đoán? (dị vật, hen, tim, lao) — đúng liều? uống được?<br>"
        f"2) {G('Siêu âm màng phổi + X-quang')}: có dịch → phân loại PIDS, {G('dẫn lưu nếu lớn / mủ / suy hô hấp')}.<br>"
        f"3) Hình ảnh {R('hoại tử, bóng khí')} hoặc bối cảnh sau cúm → {G('thêm vancomycin/clindamycin')}.<br>"
        f"4) Trẻ đi học, ho kéo dài, thâm nhiễm → {G('PCR Mycoplasma')}; đang dùng macrolid mà không đáp ứng → {G('doxycycline / fluoroquinolon')}.<br>"
        f"5) Kéo dài &gt; 2–3 tuần, tiếp xúc lao, sụt cân → {G('tìm lao')}; viêm phổi nặng/tái diễn → {G('HIV, miễn dịch')}.",
        "Không đổi kháng sinh “mù”. Mỗi nhánh của lưu đồ trả lời một câu hỏi: sai bệnh, sai tác nhân, hay có biến chứng.",
        "9. Không đáp ứng", ["That-bai"],
    ),
    algo(
        "PED69-A-05", "S4", "Xét nghiệm căn nguyên",
        "Xét nghiệm căn nguyên: 3 NÊN & 3 KHÔNG",
        f"1) {G('NÊN')}: {G('cấy máu')} cho trẻ nhập viện viêm phổi trung bình – nặng / có biến chứng.<br>"
        f"2) {G('NÊN')}: {G('PCR Mycoplasma')} khi nghi Mycoplasma ở trẻ nhập viện hoặc không đáp ứng β-lactam.<br>"
        f"3) {G('NÊN')}: gửi {G('Gram, cấy, PCR phế cầu')} mọi dịch màng phổi chọc/dẫn lưu.<br>"
        f"4) {R('KHÔNG')}: cấy máu, CRP/PCT thường quy cho trẻ ngoại trú đã tiêm chủng đủ.<br>"
        f"5) {R('KHÔNG')}: làm {R('kháng nguyên phế cầu niệu')} ở trẻ em.<br>"
        f"6) {R('KHÔNG')}: dựa vào {R('IgM Mycoplasma một lần')} hoặc {R('CRP/PCT đơn độc')} để quyết định kháng sinh.",
        "Xét nghiệm chỉ đáng làm khi kết quả có thể thay đổi xử trí; ở trẻ ngoại trú nhẹ hầu như không xét nghiệm nào làm được điều đó.",
        "4.3 Xét nghiệm căn nguyên", ["Xet-nghiem"],
    ),
    algo(
        "PED69-A-06", "S6", "Mycoplasma không đáp ứng",
        "Mycoplasma nghi kháng macrolid: cây quyết định",
        f"1) Đang macrolid {Y('48–72 giờ')}, {G('cải thiện')} → {G('tiếp tục')}, không đổi vì sợ kháng.<br>"
        f"2) {R('Sốt kéo dài / xấu đi')} → {G('PCR đột biến 23S (nếu có)')}, X-quang/siêu âm tìm biến chứng.<br>"
        f"3) Chuyển thuốc: {Y('≥ 8 tuổi')} {G('doxycycline 2–4 mg/kg/ngày')}; {Y('< 8 tuổi')} {G('doxycycline đợt ngắn')} hoặc "
        f"{G('levofloxacin')} (ngoài chỉ định, đồng thuận).<br>"
        f"4) ≥ {Y('7 ngày')} vẫn tiến triển + {R('LDH, CRP, ferritin, D-dimer cao')} → {B('RMPP')}: cân nhắc "
        f"{G('methylprednisolon 1–2 mg/kg/ngày')} (Trung Quốc 2023).<br>"
        f"5) {R('Xẹp thùy / nghi khuôn phế quản')} → {G('nội soi phế quản')}; {R('D-dimer cao')} → tìm huyết khối.",
        "Thứ tự: đánh giá đáp ứng → đổi kháng sinh → điều hòa miễn dịch → can thiệp cơ học. Bỏ qua bước 3 mà dùng corticoid ngay là "
        "che triệu chứng khi vi khuẩn còn nguyên.",
        "5.4 Mycoplasma kháng macrolid", ["Mycoplasma"], warn=True,
    ),
]
