# -*- coding: utf-8 -*-
# PED-67 Còi xương thiếu vitamin D — nguồn thẻ duy nhất (chuyên đề ôn thi, KHÔNG phải barem trường).
# Nội dung: PED-67_Coi_xuong_thieu_vitamin_D_CHUYEN_DE_ON_THI.pdf (khung sách Nhi Việt Nam + Đồng thuận toàn cầu 2016).
# Mục chuyên đề ghi ở `extra`. Con số liều/mốc tuổi khác nhau giữa các trường → ghi ⚠️ ở `extra`.


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý / triệu chứng
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / mốc / tuổi
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc / xét nghiệm / tiêu chuẩn
    return _c("#51cf66", t)


def B(t):  # tên bệnh / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("📘 CHUYÊN ĐỀ ÔN THI · CÒI XƯƠNG", "badge-ebm")
SRC = ("📖 Nguồn: Chuyên đề ôn thi PED-67 Còi xương thiếu vitamin D (khung sách Nhi Việt Nam; "
       "Munns CF et al. Global Consensus on Nutritional Rickets, J Clin Endocrinol Metab 2016;101(2):394–415). Mục: ")
WARN = " · ⚠️ Con số này các trường ghi khác nhau, đi thi dùng đúng số barem trường."
TAG = ["PED-67", "Chuyen-de-on-thi"]


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
    # ------------------------------------------------------------ S1. Định nghĩa, cơ chế, yếu tố nguy cơ
    basic(
        "PED67-S1-01", "S1", "Định nghĩa", 1,
        f"{B('[Còi xương]')} Định nghĩa còi xương do thiếu vitamin D: bệnh của đối tượng nào, rối loạn chuyển hóa gì, "
        f"hậu quả ở xương và các hệ cơ quan nào khác?",
        f"1) {B('Đối tượng')}: cơ thể {Y('đang lớn')} (trẻ em).<br>"
        f"2) {B('Rối loạn')}: thiếu vitamin D → rối loạn chuyển hóa {R('calci và phospho')}.<br>"
        f"3) {B('Ở xương')}: {R('sụn tăng trưởng không khoáng hóa được')}.<br>"
        f"4) {B('Hệ khác')}: {R('thần kinh, cơ, tạo máu')}.",
        f"Chỉ cơ thể có {Y('sụn tăng trưởng còn mở')} mới bị còi xương; người lớn thiếu vitamin D thì gọi là "
        f"{B('nhuyễn xương')}. Vì bệnh nằm ở sụn đang lớn nên biến dạng luôn đi theo vùng xương lớn nhanh nhất.",
        "1. Cơ chế", ["Dinh-nghia"],
    ),
    basic(
        "PED67-S1-02", "S1", "Cơ chế", 1,
        f"{B('[Chuỗi cơ chế]')} Trình bày chuỗi từ thiếu vitamin D đến {R('biến dạng xương')} và {R('co giật')} "
        f"(qua ruột, PTH, xương, thận).",
        f"1) Thiếu vitamin D → {R('giảm hấp thu Ca, P ở ruột')} → Ca máu có xu hướng giảm.<br>"
        f"2) {G('Tăng PTH')} (cường cận giáp thứ phát).<br>"
        f"3) PTH rút Ca từ xương → {R('mất vôi')}.<br>"
        f"4) PTH tăng thải P qua thận → {R('P máu giảm')}.<br>"
        f"5) Thiếu Ca và P → {R('sụn tăng trưởng không khoáng hóa')} → đầu xương phì đại, loe rộng; xương mềm, chịu lực bị cong.<br>"
        f"6) PTH bù không kịp → {R('Ca máu tụt')} → co giật, khóc lặng, tetany.",
        f"Điểm mấu chốt: nhờ PTH, {Y('Ca máu thường còn bình thường')} trong khi {R('P giảm')} và "
        f"{R('phosphatase kiềm tăng')}. Đề hay cho Ca bình thường để bẫy người chỉ nhớ 'còi xương = hạ calci'.",
        "1. Cơ chế", ["Co-che"],
    ),
    basic(
        "PED67-S1-03", "S1", "Yếu tố nguy cơ", 1,
        f"{B('[Yếu tố nguy cơ]')} Kể các yếu tố nguy cơ còi xương thiếu vitamin D (ánh nắng, nuôi dưỡng, mẹ, trẻ, bệnh và thuốc).",
        f"1) {R('Thiếu ánh nắng')}: ở trong nhà, mặc kín, mùa đông.<br>"
        f"2) {R('Bú mẹ hoàn toàn')} mà {R('không bổ sung vitamin D')}.<br>"
        f"3) {R('Mẹ thiếu vitamin D')} khi mang thai.<br>"
        f"4) Trẻ {R('đẻ non, nhẹ cân, sinh đôi')}; {R('da sẫm màu')}.<br>"
        f"5) {R('Ăn ít calci')}.<br>"
        f"6) {B('Bệnh gan mật, kém hấp thu')}.<br>"
        f"7) Thuốc {G('chống động kinh')} (phenytoin, phenobarbital).",
        "Nhóm theo cơ chế: thiếu nguồn (nắng, ăn, mẹ) — dự trữ kém (đẻ non, sinh đôi) — hấp thu kém (gan mật, ruột) — "
        "tăng chuyển hóa vitamin D (thuốc chống động kinh cảm ứng men gan).",
        "1. Yếu tố nguy cơ", ["Yeu-to-nguy-co"],
    ),
    basic(
        "PED67-S1-04", "S1", "Dịch tễ", 2,
        f"{B('[Tuổi hay gặp]')} Còi xương thiếu vitamin D gặp chủ yếu ở trẻ dưới bao nhiêu tuổi, đỉnh ở khoảng tuổi nào?",
        f"1) Chủ yếu trẻ {Y('dưới 3 tuổi')}.<br>"
        f"2) Đỉnh khoảng {Y('6–24 tháng')}.",
        "Đây là giai đoạn xương lớn nhanh nhất, nhu cầu calci cao, trong khi nguồn vitamin D từ sữa mẹ thấp và trẻ ít ra nắng.",
        "1. Yếu tố nguy cơ", ["Dich-te"], warn=True,
    ),
    cloze(
        "PED67-S1-C1", "S1", "Cơ chế",
        f"Bộ ba sinh hóa điển hình của còi xương thiếu vitamin D (nhờ tăng PTH): "
        f"{{{{c1::{Y('calci bình thường')}, {R('phospho giảm')}, {R('phosphatase kiềm tăng')}}}}}.",
        "1. Cơ chế", ["Co-che"],
    ),

    # ------------------------------------------------------------ S2. Lâm sàng 5 nhóm + hạ calci
    basic(
        "PED67-S2-01", "S2", "Lâm sàng", 1,
        f"{B('[5 nhóm triệu chứng]')} Kể {Y('5 nhóm')} triệu chứng lâm sàng của còi xương và nhóm nào xuất hiện sớm nhất.",
        f"1) {B('Thần kinh thực vật')} — {Y('sớm nhất')}.<br>"
        f"2) {B('Xương')}.<br>"
        f"3) {B('Cơ, dây chằng')}.<br>"
        f"4) {B('Máu')}.<br>"
        f"5) {B('Hô hấp')}.",
        "Mẹo: 'Thần – Xương – Cơ – Máu – Thở'. Ngoài 5 nhóm này còn có bệnh cảnh hạ calci máu cấp (co giật, khóc lặng, tetany).",
        "2. Lâm sàng", ["Lam-sang"],
    ),
    basic(
        "PED67-S2-02", "S2", "Lâm sàng", 2,
        f"{B('[Thần kinh thực vật]')} Kể các triệu chứng thần kinh thực vật của còi xương và giải thích vì sao trẻ {R('rụng tóc gáy')}.",
        f"1) {R('Quấy khóc')}, {R('ngủ không yên')}, {R('hay giật mình')}.<br>"
        f"2) {R('Ra nhiều mồ hôi')} (mồ hôi trộm).<br>"
        f"3) {R('Rụng tóc vùng gáy')} thành hình vành khăn: mồ hôi làm ngứa, trẻ {R('cọ đầu xuống gối')}.",
        "Đây là nhóm dấu hiệu sớm nhưng không đặc hiệu (trẻ khỏe cũng hay ra mồ hôi đầu). Giá trị khi đi kèm yếu tố nguy cơ và dấu hiệu xương.",
        "2. Lâm sàng", ["Lam-sang", "Than-kinh"],
    ),
    basic(
        "PED67-S2-03", "S2", "Lâm sàng", 2,
        f"{B('[Cơ, máu, hô hấp]')} Nêu biểu hiện ở {B('cơ – dây chằng')}, {B('máu')} và {B('hô hấp')} của trẻ còi xương.",
        f"1) {B('Cơ, dây chằng')}: trương lực cơ giảm, {R('bụng to bè (bụng ếch)')}, dây chằng lỏng lẻo, "
        f"{R('chậm lẫy, ngồi, bò, đứng, đi')}.<br>"
        f"2) {B('Máu')}: {R('thiếu máu')} (hay kèm thiếu sắt); thể nặng có {R('gan lách to')}.<br>"
        f"3) {B('Hô hấp')}: lồng ngực biến dạng, cơ hô hấp yếu → {R('dễ viêm phổi, viêm phổi kéo dài')}.",
        "Thiếu phospho làm cơ yếu (ATP kém) nên bụng ếch và chậm vận động. Ngực mềm, biến dạng cộng cơ yếu làm thông khí kém, "
        "nên trẻ còi xương viêm phổi dai dẳng.",
        "2. Lâm sàng", ["Lam-sang"],
    ),
    basic(
        "PED67-S2-04", "S2", "Hạ calci máu", 1,
        f"{B('[Hạ calci máu cấp]')} Nêu {Y('3')} biểu hiện của hạ calci máu cấp trong còi xương và {Y('2')} lứa tuổi hay gặp.",
        f"1) {R('Co giật')}.<br>"
        f"2) {R('Cơn khóc lặng')} (co thắt thanh quản).<br>"
        f"3) {R('Co cứng bàn tay, bàn chân (tetany)')}.<br>"
        f"4) Hay gặp ở {Y('nhũ nhi dưới 6 tháng')} và {Y('tuổi dậy thì')}.",
        "Hai lứa tuổi này là hai giai đoạn xương lớn nhanh nhất nên 'hút' calci mạnh nhất. Hạ calci có thể là biểu hiện ĐẦU TIÊN, "
        "trước khi có biến dạng xương.",
        "2. Lâm sàng", ["Lam-sang", "Ha-calci"],
    ),

    # ------------------------------------------------------------ S3. Biểu hiện theo tuổi
    basic(
        "PED67-S3-01", "S3", "Biểu hiện theo tuổi", 1,
        f"{B('[Nguyên tắc theo tuổi]')} Vì sao biểu hiện xương của còi xương thay đổi theo tuổi? Nêu thứ tự vùng xương bị theo tuổi.",
        f"1) Biến dạng xuất hiện ở {R('vùng xương đang lớn nhanh nhất')} ở lứa tuổi đó.<br>"
        f"2) {Y('0–6 tháng')}: {B('hộp sọ')}.<br>"
        f"3) {Y('6–12 tháng')}: {B('sọ, lồng ngực, cổ tay')}.<br>"
        f"4) {Y('12–24 tháng')} (tập đứng, đi): {B('chi dưới')} chịu lực.<br>"
        f"5) {Y('Trên 2 tuổi')}: {B('cột sống, khung chậu')}, di chứng chi dưới.<br>"
        f"6) {Y('Trẻ lớn, dậy thì')}: {R('đau xương')}, yếu cơ.",
        "Mẹo: 'Sọ → Ngực → Chân → Đau'. Hỏi tuổi trước rồi khám đúng vùng: trẻ 4 tháng thì sờ sọ tìm mềm sọ, trẻ 9 tháng sờ sườn "
        "và cổ tay, trẻ 18 tháng nhìn chân.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),
    basic(
        "PED67-S3-02", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[Sơ sinh và đẻ non]')} Còi xương biểu hiện thế nào ở {Y('trẻ sơ sinh')} và ở {Y('trẻ đẻ non')}?",
        f"1) {Y('Sơ sinh')}: hiếm; {B('còi xương bẩm sinh')} khi mẹ thiếu vitamin D nặng; trẻ có thể {R('hạ Ca, co giật')} sớm.<br>"
        f"2) {Y('Đẻ non')}: {B('bệnh xương chuyển hóa của trẻ đẻ non')}, lộ ra vài tuần sau sinh: {R('P thấp')}, "
        f"{R('ALP rất cao')}, {R('gãy xương sườn hoặc xương dài khi chăm sóc')}.",
        "Trẻ đẻ non mất giai đoạn 3 tháng cuối thai kỳ — lúc mẹ chuyển phần lớn calci, phospho cho thai — nên dự trữ khoáng rất thấp.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi", "De-non"],
    ),
    basic(
        "PED67-S3-03", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[0–6 tháng]')} Kể biểu hiện còi xương ở trẻ {Y('0–6 tháng')} (thần kinh, hộp sọ, thóp, hạ calci) và cách khám mềm sọ.",
        f"1) {B('Thần kinh thực vật')} rõ nhất: {R('mồ hôi trộm, rụng tóc gáy, quấy khóc')}.<br>"
        f"2) {B('Mềm xương sọ (craniotabes)')}: ấn vào {G('xương chẩm hoặc xương đỉnh')} thấy lõm rồi bật lại "
        f"{R('như ấn quả bóng bàn')}.<br>"
        f"3) {R('Thóp rộng, bờ thóp mềm')}.<br>"
        f"4) Dễ {R('hạ Ca máu')}: co giật, khóc lặng.",
        f"Ở tuổi này hộp sọ lớn nhanh nhất nên tổn thương ở sọ. Lưu ý: mềm sọ quanh đường khớp ở trẻ sơ sinh, đẻ non có thể là "
        f"{Y('sinh lý')}, không vội kết luận còi xương.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),
    basic(
        "PED67-S3-04", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[6–12 tháng]')} Kể biểu hiện còi xương ở trẻ {Y('6–12 tháng')} (sọ, lồng ngực, cổ tay, răng, vận động, bụng).",
        f"1) {R('Bướu đỉnh, bướu trán')}, đầu to, {R('đầu bẹt hoặc vuông')}.<br>"
        f"2) {R('Chuỗi hạt sườn')} (khớp sụn sườn phình to); {R('rãnh Harrison')} (lõm ngang bờ dưới lồng ngực, chỗ cơ hoành kéo).<br>"
        f"3) {R('Vòng cổ tay')}.<br>"
        f"4) {R('Chậm mọc răng')}, men răng xấu.<br>"
        f"5) {R('Chậm ngồi, chậm bò')}.<br>"
        f"6) {R('Bụng ếch')}; thóp chậm liền.",
        "Chuỗi hạt và vòng cổ tay cùng một bản chất: sụn tăng trưởng không khoáng hóa nên phì đại, phình ra ở đầu xương "
        "(sụn sườn, đầu dưới xương quay). Rãnh Harrison do cơ hoành kéo lõm phần xương sườn mềm.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),
    basic(
        "PED67-S3-05", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[12–24 tháng]')} Kể biểu hiện còi xương ở trẻ {Y('12–24 tháng')} khi tập đứng, đi (chi dưới, lồng ngực, vận động, hàm, thóp).",
        f"1) {R('Chân vòng kiềng (chữ O)')}, đôi khi {R('chân chữ X')}.<br>"
        f"2) {R('Vòng cổ chân')}.<br>"
        f"3) {R('Ngực ức gà')}.<br>"
        f"4) {R('Chậm đứng, chậm đi')}, đi lạch bạch.<br>"
        f"5) {R('Hàm trên hẹp, vòm miệng sâu, hai hàm không khớp')}.<br>"
        f"6) {R('Thóp chưa liền')} sau {Y('18 tháng')}.",
        "Khi trẻ bắt đầu chịu sức nặng cơ thể, xương chi dưới đang mềm sẽ cong — vì thế biến dạng chân chỉ rõ khi trẻ đã đứng, đi.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),
    basic(
        "PED67-S3-06", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[Trên 2 tuổi]')} Nêu biểu hiện và di chứng còi xương ở trẻ {Y('trên 2 tuổi')} (cột sống, khung chậu, chi dưới).",
        f"1) {R('Gù, vẹo cột sống')}.<br>"
        f"2) {R('Khung chậu hẹp')} — di chứng ở trẻ gái, sau này {R('dễ đẻ khó')}.<br>"
        f"3) Chân O hoặc X {R('còn lại thành di chứng')}.",
        "Khung chậu hẹp do còi xương là liên hệ Nhi – Sản hay hỏi: đây là một nguyên nhân khung chậu méo/hẹp gây đẻ khó.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi", "Di-chung"],
    ),
    basic(
        "PED67-S3-07", "S3", "Biểu hiện theo tuổi", 2,
        f"{B('[Trẻ lớn, dậy thì]')} Còi xương muộn ở {Y('trẻ lớn, tuổi dậy thì')} biểu hiện khác trẻ nhỏ thế nào?",
        f"1) {R('Đau xương, đau chân khi đi')}, mỏi.<br>"
        f"2) {R('Yếu cơ gốc chi')}, đi lạch bạch.<br>"
        f"3) {R('Chuột rút, tetany')}.<br>"
        f"4) Hay gặp {R('chân chữ X')}.<br>"
        f"5) Có thể {R('gãy xương')} do nhuyễn xương.",
        "Trẻ lớn ít biến dạng 'kinh điển' (sọ, chuỗi hạt) mà nổi bật là đau và yếu cơ — dễ bị bỏ sót hoặc nhầm 'đau tăng trưởng'.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),
    cloze(
        "PED67-S3-C1", "S3", "Biểu hiện theo tuổi",
        f"Mềm xương sọ (craniotabes) là dấu hiệu xương điển hình của trẻ {{{{c1::{Y('0–6 tháng')}}}}}; bướu đỉnh, bướu trán, "
        f"chuỗi hạt sườn gặp ở trẻ {{{{c2::{Y('6–12 tháng')}}}}}; chân chữ O rõ khi trẻ {{{{c3::{Y('12–24 tháng')}}}}} tập đứng, đi.",
        "3. Biểu hiện theo tuổi", ["Theo-tuoi"],
    ),

    # ------------------------------------------------------------ S4. Biến dạng sinh lý, phân giai đoạn
    basic(
        "PED67-S4-01", "S4", "Biến dạng sinh lý", 1,
        f"{B('[Đừng nhầm sinh lý]')} Chân O và chân X sinh lý gặp đến tuổi nào? Khi nào mới nghĩ biến dạng chân là do còi xương?",
        f"1) {B('Chân O sinh lý')}: đến khoảng {Y('2 tuổi')}.<br>"
        f"2) {B('Chân X sinh lý')}: khoảng {Y('3–4 tuổi')}, sau đó tự thẳng.<br>"
        f"3) Nghĩ còi xương khi biến dạng {R('nặng')}, {R('không đối xứng')}, {R('tồn tại quá các mốc trên')}, hoặc "
        f"{R('kèm dấu hiệu khác')} (vòng cổ tay, chuỗi hạt, ALP tăng).",
        "Trục chi dưới sinh lý đi theo trình tự: O lúc mới sinh → thẳng khoảng 18–24 tháng → X lúc 3–4 tuổi → thẳng dần. "
        "Một bên chân cong hơn hẳn bên kia thì không phải sinh lý.",
        "3. Biến dạng sinh lý", ["Phan-biet"],
    ),
    basic(
        "PED67-S4-02", "S4", "Phân giai đoạn", 1,
        f"{B('[4 giai đoạn]')} Kể {Y('4')} giai đoạn của còi xương và đặc điểm lâm sàng, sinh hóa, X quang của từng giai đoạn.",
        f"1) {B('Giai đoạn khởi phát')}: chủ yếu thần kinh thực vật, có thể mềm sọ; Ca bình thường, {R('P giảm')}, ALP bình thường hoặc tăng nhẹ; "
        f"X quang bình thường hoặc thay đổi nhẹ.<br>"
        f"2) {B('Giai đoạn toàn phát')}: thần kinh + xương + cơ rõ; Ca bình thường hoặc giảm, {R('P giảm, ALP tăng rõ')}; X quang điển hình.<br>"
        f"3) {B('Giai đoạn hồi phục')}: triệu chứng giảm; {G('P về bình thường sớm')}, ALP về chậm hơn; X quang {G('xuất hiện vạch vôi hóa')}.<br>"
        f"4) {B('Giai đoạn di chứng')}: còn biến dạng xương; sinh hóa {G('bình thường')}; không còn tổn thương hoạt động.",
        "Phospho là chỉ số 'nhạy' nhất: giảm sớm nhất và về bình thường sớm nhất. ALP phản ánh hoạt động tạo xương nên về chậm. "
        "Giai đoạn di chứng: xương đã khoáng hóa lại nhưng hình dạng đã cong thì không tự hết.",
        "3. Phân giai đoạn", ["Giai-doan"], warn=True,
    ),
    cloze(
        "PED67-S4-C1", "S4", "Phân giai đoạn",
        f"Ở giai đoạn hồi phục còi xương, chỉ số sinh hóa về bình thường sớm nhất là {{{{c1::{G('phospho')}}}}}; "
        f"X quang xuất hiện {{{{c2::{G('vạch vôi hóa')}}}}} ở đầu xương.",
        "3. Phân giai đoạn", ["Giai-doan"],
    ),

    # ------------------------------------------------------------ S5. Cận lâm sàng
    basic(
        "PED67-S5-01", "S5", "Sinh hóa", 1,
        f"{B('[Sinh hóa máu]')} Nêu thay đổi của {G('Ca, P, ALP, 25(OH)D, PTH')} và dự trữ kiềm trong còi xương thiếu vitamin D.",
        f"1) {G('Calci')}: {Y('bình thường')} hoặc giảm (giảm rõ khi có tetany, co giật).<br>"
        f"2) {G('Phospho')}: {R('giảm')} — dấu hiệu sớm.<br>"
        f"3) {G('Phosphatase kiềm (ALP)')}: {R('tăng')} — nhạy, dùng theo dõi điều trị.<br>"
        f"4) {G('25(OH)D')}: {R('giảm')}.<br>"
        f"5) {G('PTH')}: {R('tăng')} (cường cận giáp thứ phát).<br>"
        f"6) {G('Dự trữ kiềm')}: có thể giảm (toan chuyển hóa nhẹ).",
        f"ALP phải so với {Y('khoảng bình thường theo tuổi')} vì trẻ đang lớn vốn có ALP cao. Toan nhẹ do PTH làm thận thải bicarbonat.",
        "4.1 Sinh hóa máu", ["Can-lam-sang"],
    ),
    basic(
        "PED67-S5-02", "S5", "Sinh hóa", 2,
        f"{B('[25(OH)D]')} Vì sao định lượng {G('25(OH)D')} (không phải 1,25(OH)₂D) để đánh giá thiếu vitamin D? Nêu ngưỡng thiếu, "
        f"chưa đủ, đủ theo Đồng thuận 2016.",
        f"1) {G('25(OH)D')} phản ánh {B('dự trữ vitamin D')}, nồng độ ổn định.<br>"
        f"2) {B('1,25(OH)₂D')} có thể {R('bình thường hoặc tăng')} khi thiếu vitamin D (PTH kích thích 1α-hydroxylase), thời gian bán hủy ngắn.<br>"
        f"3) {R('Thiếu')}: {Y('dưới 30 nmol/L (12 ng/mL)')}.<br>"
        f"4) {Y('Chưa đủ')}: {Y('30–50 nmol/L')}.<br>"
        f"5) {G('Đủ')}: {Y('trên 50 nmol/L')}.",
        "Bẫy MCQ kinh điển: chọn 1,25(OH)₂D vì là dạng hoạt động — sai, vì cơ thể bù bằng PTH nên dạng hoạt động không phản ánh dự trữ.",
        "4.1 Sinh hóa máu", ["Can-lam-sang"],
    ),
    basic(
        "PED67-S5-03", "S5", "Nước tiểu", 2,
        f"{B('[Nước tiểu]')} Nêu thay đổi {G('phospho niệu')}, {G('calci niệu')} và acid amin niệu trong còi xương thiếu vitamin D.",
        f"1) {R('Phospho niệu tăng')}.<br>"
        f"2) {Y('Calci niệu giảm')}.<br>"
        f"3) Có thể có {R('acid amin niệu')}.",
        "Cả ba đều do PTH tăng: PTH làm ống thận thải P, giữ Ca, và giảm tái hấp thu ở ống gần (acid amin niệu).",
        "4.1 Sinh hóa máu", ["Can-lam-sang"],
    ),
    basic(
        "PED67-S5-04", "S5", "X quang", 1,
        f"{B('[X quang]')} Chụp X quang vị trí nào trong còi xương? Kể các hình ảnh tổn thương và hình ảnh khi hồi phục.",
        f"1) Vị trí chụp: {G('cổ tay hoặc khớp gối')} (nơi xương lớn nhanh).<br>"
        f"2) {R('Đầu hành xương loe rộng, lõm hình đài, bờ nham nhở')} (cupping, fraying).<br>"
        f"3) {R('Đường vôi hóa tạm thời mờ hoặc mất')}, khoảng cách đầu xương – hành xương rộng.<br>"
        f"4) {R('Mất vôi toàn bộ')}, vỏ xương mỏng, bè xương thưa.<br>"
        f"5) {R('Điểm cốt hóa xuất hiện chậm')}.<br>"
        f"6) Có thể {R('gãy cành tươi')}, {R('đường Looser')} (gãy giả).<br>"
        f"7) Hồi phục: {G('vạch vôi hóa')} xuất hiện sau khoảng {Y('2–4 tuần')} điều trị.",
        "Hình 'đài' (cupping) là hình ảnh trên phim của chính vòng cổ tay sờ thấy trên lâm sàng. Vạch vôi hóa là dấu đáp ứng sớm "
        "nhất trên phim, xuất hiện trước khi biến dạng cải thiện.",
        "4.2 X quang", ["Can-lam-sang", "X-quang"],
    ),
    cloze(
        "PED67-S5-C1", "S5", "Sinh hóa",
        f"Theo Đồng thuận 2016, thiếu vitamin D khi 25(OH)D {{{{c1::{Y('dưới 30 nmol/L (12 ng/mL)')}}}}}; đủ khi "
        f"{{{{c2::{Y('trên 50 nmol/L')}}}}}.",
        "4.1 Sinh hóa máu", ["Can-lam-sang"],
    ),
    cloze(
        "PED67-S5-C2", "S5", "X quang",
        f"Sau khi điều trị vitamin D, vạch vôi hóa xuất hiện trên X quang đầu xương sau khoảng {{{{c1::{Y('2–4 tuần')}}}}}.",
        "4.2 X quang", ["X-quang"],
    ),

    # ------------------------------------------------------------ S6. Chẩn đoán phân biệt
    basic(
        "PED67-S6-01", "S6", "Phân biệt sinh hóa", 1,
        f"{B('[Phân biệt thể giảm phosphat máu]')} Còi xương giảm phosphat máu (kháng vitamin D) khác còi xương thiếu vitamin D "
        f"thế nào về {G('Ca, P, PTH, 25(OH)D')} và đáp ứng điều trị?",
        f"1) {B('Thiếu vitamin D')}: Ca bình thường hoặc giảm, P giảm, ALP tăng nhiều, {R('PTH tăng')}, "
        f"{R('25(OH)D giảm')}; {G('đáp ứng với vitamin D liều điều trị')}.<br>"
        f"2) {B('Giảm phosphat máu (kháng D)')}, hay gặp nhất là thể {B('di truyền liên kết X')}: {Y('Ca bình thường')}, "
        f"{R('P giảm rất nặng')}, PTH bình thường hoặc tăng nhẹ, {Y('25(OH)D bình thường')}; có {R('tính gia đình')}, "
        f"{R('không đáp ứng vitamin D liều thường')}, thận mất phospho.",
        "Câu chìa khóa: Ca bình thường + P rất thấp + 25(OH)D bình thường + bố/mẹ cũng chân cong → nghĩ thể giảm phosphat máu di truyền.",
        "4.3 Phân biệt", ["Phan-biet"],
    ),
    basic(
        "PED67-S6-02", "S6", "Phân biệt sinh hóa", 2,
        f"{B('[Phụ thuộc vitamin D và do thận]')} Phân biệt còi xương {B('phụ thuộc vitamin D typ 1')}, {B('typ 2')} và "
        f"{B('còi xương do thận')} dựa vào xét nghiệm nào?",
        f"1) {B('Typ 1')} (thiếu men 1α-hydroxylase): Ca giảm, P giảm, PTH tăng, 25(OH)D bình thường, {R('1,25(OH)₂D thấp')}.<br>"
        f"2) {B('Typ 2')} (kháng thụ thể vitamin D): Ca giảm, P giảm, PTH tăng, 25(OH)D bình thường, "
        f"{R('1,25(OH)₂D rất cao')}, hay kèm {R('rụng tóc toàn bộ')}.<br>"
        f"3) {B('Do thận')} (suy thận mạn): Ca giảm, {R('P tăng')}, PTH tăng rất cao, {R('creatinin tăng')}.",
        "Đọc theo trục: 25(OH)D thấp → thiếu D; 25(OH)D bình thường mà 1,25 thấp → không chuyển hóa được (typ 1); 1,25 cao → "
        "thụ thể hỏng (typ 2). P TĂNG là dấu hiệu riêng của bệnh thận vì thận không thải được phospho.",
        "4.3 Phân biệt", ["Phan-biet"],
    ),
    basic(
        "PED67-S6-03", "S6", "Phân biệt lâm sàng", 2,
        f"{B('[Bệnh dễ nhầm]')} Phân biệt còi xương với {B('suy giáp bẩm sinh')}, {B('não úng thủy')}, {B('loạn sản sụn')} "
        f"và {B('còi xương do thiếu calci')}.",
        f"1) {B('Suy giáp bẩm sinh')}: thóp rộng, chậm phát triển nhưng có {R('lưỡi to, táo bón, vàng da kéo dài')}; {G('TSH tăng')}.<br>"
        f"2) {B('Não úng thủy')}: đầu to, {R('thóp phồng căng')} chứ không mềm.<br>"
        f"3) {B('Loạn sản sụn')}: {R('chi ngắn bẩm sinh')}, không có rối loạn sinh hóa.<br>"
        f"4) {B('Do thiếu calci')}: chế độ ăn {R('rất ít calci')}; 25(OH)D bình thường, Ca giảm hoặc bình thường, P giảm, ALP và PTH tăng.",
        "Thóp rộng gặp ở cả còi xương, suy giáp và não úng thủy: sờ bờ thóp (mềm trong còi xương) và độ căng (phồng trong não úng thủy), "
        "nhìn lưỡi, hỏi táo bón và vàng da kéo dài (suy giáp).",
        "4.3 Phân biệt", ["Phan-biet"],
    ),

    # ------------------------------------------------------------ S7. Điều trị
    basic(
        "PED67-S7-01", "S7", "Điều trị", 1,
        f"{B('[Nguyên tắc điều trị]')} Kể {Y('5')} nguyên tắc điều trị còi xương thiếu vitamin D.",
        f"1) {G('Vitamin D liều điều trị')} → chuyển {G('liều duy trì')}.<br>"
        f"2) {G('Bổ sung calci')} kèm theo.<br>"
        f"3) {G('Xử trí hạ calci máu có triệu chứng trước')}, nếu có.<br>"
        f"4) {G('Tắm nắng, dinh dưỡng')}, điều trị bệnh kèm (thiếu máu, nhiễm khuẩn hô hấp).<br>"
        f"5) {G('Theo dõi')} đáp ứng và {R('ngộ độc vitamin D')}; {G('chỉnh hình')} nếu còn di chứng.",
        "Thứ tự trong cấp cứu: co giật hạ Ca thì nâng Ca trước, rồi mới cho vitamin D — cho vitamin D trước làm xương hút Ca, tụt thêm.",
        "5.1 Nguyên tắc", ["Dieu-tri"],
    ),
    basic(
        "PED67-S7-02", "S7", "Vitamin D", 1,
        f"{B('[Vitamin D liều điều trị – Đồng thuận 2016]')} Nêu dạng vitamin D ưu tiên, thời gian tối thiểu và liều hằng ngày "
        f"theo {Y('4 nhóm tuổi')}; nhóm nào không dùng liều cao một lần?",
        f"1) Dạng ưu tiên: {G('vitamin D3 (cholecalciferol)')}; dùng ít nhất {Y('12 tuần')}.<br>"
        f"2) {Y('Dưới 3 tháng')}: {G('2.000 IU/ngày')}; {R('không dùng liều cao một lần')}.<br>"
        f"3) {Y('3–12 tháng')}: {G('2.000 IU/ngày')} hoặc {G('50.000 IU')} một lần.<br>"
        f"4) {Y('1–12 tuổi')}: {G('3.000–6.000 IU/ngày')} hoặc {G('150.000 IU')} một lần.<br>"
        f"5) {Y('Trên 12 tuổi')}: {G('6.000 IU/ngày')} hoặc {G('300.000 IU')} một lần.",
        "Liều một lần (stoss) hợp khi khó tuân thủ uống hằng ngày. Trẻ dưới 3 tháng không dùng stoss vì nguy cơ tăng calci máu.",
        "5.2 Vitamin D", ["Dieu-tri", "Lieu"], warn=True,
    ),
    basic(
        "PED67-S7-03", "S7", "Vitamin D", 1,
        f"{B('[Phác đồ Việt Nam và liều duy trì]')} Phác đồ vitamin D hay ghi trong sách Việt Nam là gì, và liều duy trì sau điều trị "
        f"theo Đồng thuận 2016?",
        f"1) Sách Việt Nam: {G('2.000–4.000 IU/ngày')} trong {Y('4–6 tuần')}, sau đó {G('400 IU/ngày')}; liều cao một lần chỉ khi "
        f"{R('không theo dõi được trẻ')}.<br>"
        f"2) Duy trì (Đồng thuận 2016): {G('400 IU/ngày')} cho trẻ {Y('dưới 1 tuổi')}, {G('600 IU/ngày')} cho trẻ {Y('từ 1 tuổi')}.",
        "Hai nguồn khác nhau ở thời gian điều trị (4–6 tuần so với ≥ 12 tuần). Đi thi viết theo số của trường; đi lâm sàng có thể "
        "tham khảo đồng thuận quốc tế.",
        "5.2 Vitamin D", ["Dieu-tri", "Lieu"], warn=True,
    ),
    basic(
        "PED67-S7-04", "S7", "Calci", 1,
        f"{B('[Calci và hội chứng xương đói]')} Liều calci đi kèm vitamin D theo Đồng thuận 2016 là bao nhiêu, và vì sao bắt buộc "
        f"bổ sung?",
        f"1) Khoảng {G('500 mg calci nguyên tố/ngày')}, qua ăn uống hoặc thuốc, dùng {G('song song với vitamin D')}.<br>"
        f"2) Lý do: vitamin D có tác dụng thì xương 'đói calci' hút calci rất mạnh ({B('hội chứng xương đói')}) → không bù thì trẻ "
        f"{R('tụt Ca máu, co giật')} trong những ngày đầu.",
        "Bẫy: cho vitamin D liều cao mà quên calci → co giật ngày thứ vài sau điều trị, gia đình tưởng 'thuốc gây co giật'.",
        "5.3 Calci", ["Dieu-tri", "Calci"],
    ),
    basic(
        "PED67-S7-05", "S7", "Hạ calci cấp", 1,
        f"{B('[Co giật, tetany do hạ Ca]')} Trình bày xử trí hạ calci máu có triệu chứng: thuốc, liều, đường dùng, tốc độ, theo dõi, "
        f"và các bước tiếp theo.",
        f"1) {G('Calci gluconat 10%')} khoảng {Y('0,5–1 mL/kg')} (50–100 mg/kg), tối đa {Y('20 mL')}.<br>"
        f"2) {G('Tiêm tĩnh mạch chậm')} trong {Y('5–10 phút')}.<br>"
        f"3) {G('Theo dõi nhịp tim')} (nguy cơ {R('chậm nhịp')}); tránh {R('thoát mạch')} (hoại tử mô).<br>"
        f"4) Kiểm tra {G('magie máu')}: thiếu magie thì calci khó lên, phải bù magie.<br>"
        f"5) Sau đó {G('calci uống')} rồi mới bắt đầu {G('vitamin D')}.",
        "Calci tiêm nhanh gây chậm nhịp, ngừng tim; thoát mạch gây hoại tử nặng — nên tiêm chậm qua đường truyền chắc chắn.",
        "5.4 Hạ calci", ["Dieu-tri", "Cap-cuu"], warn=True,
    ),
    basic(
        "PED67-S7-06", "S7", "Hỗ trợ", 2,
        f"{B('[Điều trị hỗ trợ]')} Kể các biện pháp hỗ trợ: tắm nắng, dinh dưỡng, vận động, bệnh kèm và chỉnh hình.",
        f"1) {G('Tắm nắng')} khoảng {Y('15–30 phút/ngày')} buổi sáng sớm, để hở tay, chân, lưng; {R('tránh nắng gắt buổi trưa')}.<br>"
        f"2) {G('Tiếp tục bú mẹ')}; ăn dặm đủ calci: sữa, trứng, cá, tôm, cua.<br>"
        f"3) {R('Không cho trẻ đứng, đi sớm')} khi xương còn mềm.<br>"
        f"4) Điều trị {B('thiếu máu')}, {B('nhiễm khuẩn hô hấp')} kèm theo.<br>"
        f"5) {G('Chỉnh hình')}: biến dạng nhẹ thường {G('tự thẳng')}; phẫu thuật chỉ khi biến dạng {R('nặng, kéo dài sau khi bệnh ổn định')}.",
        "Bắt trẻ đứng sớm 'cho cứng chân' là quan niệm dân gian sai — xương mềm chịu lực sẽ cong thêm.",
        "5.5 Hỗ trợ", ["Dieu-tri"],
    ),
    basic(
        "PED67-S7-07", "S7", "Theo dõi", 2,
        f"{B('[Theo dõi và không đáp ứng]')} Theo dõi đáp ứng điều trị còi xương bằng gì, khi nào; nếu điều trị đúng mà không đáp ứng "
        f"thì nghĩ đến gì?",
        f"1) {G('P và ALP')} cải thiện sau vài tuần; kiểm tra {G('Ca, P, ALP, 25(OH)D')} sau khoảng {Y('3 tháng')}.<br>"
        f"2) {G('X quang')}: vạch vôi hóa sau {Y('2–4 tuần')}; chụp lại khoảng {Y('3 tháng')}.<br>"
        f"3) Không đáp ứng dù đúng liều, đúng cách: nghĩ {B('còi xương kháng hoặc phụ thuộc vitamin D')}, {B('bệnh thận')}, "
        f"{B('kém hấp thu')}.",
        "Trước khi kết luận 'kháng', luôn hỏi lại tuân thủ: thuốc có thật sự được uống đủ không, có nôn trớ không.",
        "5.6 Theo dõi", ["Dieu-tri", "Theo-doi"],
    ),
    basic(
        "PED67-S7-08", "S7", "Ngộ độc vitamin D", 1,
        f"{B('[Ngộ độc vitamin D]')} Nêu biểu hiện ngộ độc vitamin D (tăng calci máu) và cách xử trí.",
        f"1) Biểu hiện: {R('chán ăn, nôn, táo bón')}; {R('khát nhiều, tiểu nhiều')}, sụt cân; {R('vôi hóa thận, sỏi thận')}.<br>"
        f"2) Xử trí: {G('ngừng vitamin D và calci')}, {G('truyền dịch')}, kiểm tra {G('Ca máu và Ca niệu')}.",
        "Tăng calci làm thận mất khả năng cô đặc nước tiểu → tiểu nhiều, khát; calci lắng đọng ở thận gây sỏi, vôi hóa.",
        "5.6 Theo dõi", ["Dieu-tri", "Ngo-doc"], asks=["Biểu hiện", "Xử trí"],
    ),
    cloze(
        "PED67-S7-C1", "S7", "Vitamin D",
        f"Theo Đồng thuận 2016, trẻ 1–12 tuổi bị còi xương dùng vitamin D {{{{c1::{G('3.000–6.000 IU/ngày')}}}}} trong ít nhất "
        f"{{{{c2::{Y('12 tuần')}}}}}.",
        "5.2 Vitamin D", ["Lieu"], warn=True,
    ),
    cloze(
        "PED67-S7-C2", "S7", "Hạ calci cấp",
        f"Co giật do hạ calci máu: liều calci gluconat 10% là {{{{c1::{Y('0,5–1 mL/kg')}}}}} (tối đa 20 mL).",
        "5.4 Hạ calci", ["Cap-cuu"], warn=True,
    ),

    # ------------------------------------------------------------ S8. Phòng bệnh
    basic(
        "PED67-S8-01", "S8", "Phòng bệnh", 1,
        f"{B('[Phòng bệnh]')} Nêu các biện pháp phòng còi xương cho {Y('bà mẹ mang thai')}, {Y('trẻ bú mẹ')} và {Y('trẻ đẻ non')}.",
        f"1) {Y('Bà mẹ mang thai')}: tắm nắng, ăn đủ chất, {G('bổ sung vitamin D trong 3 tháng cuối')} theo hướng dẫn.<br>"
        f"2) {Y('Trẻ bú mẹ hoàn toàn hoặc bú mẹ là chính')}: {G('vitamin D 400 IU/ngày')} từ {Y('những ngày đầu sau sinh')} "
        f"đến {Y('12 tháng tuổi')}.<br>"
        f"3) {Y('Trẻ đẻ non')}: {G('liều cao hơn')}, theo dõi Ca, P, ALP (theo phác đồ sơ sinh).<br>"
        f"4) Chung: tắm nắng hợp lý, ăn dặm đủ calci, {R('không kiêng khem')}.",
        "Sữa mẹ rất ít vitamin D, nên trẻ bú mẹ hoàn toàn cần bổ sung dù mẹ ăn uống tốt. Trẻ uống đủ sữa công thức có vitamin D "
        "thường đã đủ lượng khuyến nghị.",
        "5.7 Phòng bệnh", ["Phong-benh"], warn=True,
    ),
    cloze(
        "PED67-S8-C1", "S8", "Phòng bệnh",
        f"Trẻ bú mẹ hoàn toàn cần uống vitamin D {{{{c1::{G('400 IU/ngày')}}}}} từ những ngày đầu sau sinh đến "
        f"{{{{c2::{Y('12 tháng tuổi')}}}}}.",
        "5.7 Phòng bệnh", ["Phong-benh"],
    ),

    # ------------------------------------------------------------ ⚡ Thuật toán quyết định
    algo(
        "PED67-A-01", "S5", "Giải mã sinh hóa",
        "Giải mã nhanh Ca – P – ALP – PTH – 25(OH)D",
        f"1) {Y('Ca bình thường')} + {R('P giảm')} + {R('ALP tăng')} + {R('PTH tăng')} + {R('25(OH)D thấp')} → "
        f"{B('còi xương thiếu vitamin D')}.<br>"
        f"2) {Y('Ca bình thường')} + {R('P rất thấp')} + {Y('25(OH)D bình thường')} + tính gia đình → {B('giảm phosphat máu di truyền')}.<br>"
        f"3) 25(OH)D bình thường + {R('1,25(OH)₂D thấp')} → {B('phụ thuộc vitamin D typ 1')}; {R('1,25 rất cao')} → {B('typ 2')}.<br>"
        f"4) {R('P TĂNG')} + {R('creatinin tăng')} → {B('còi xương do thận')}.",
        "Ba câu hỏi theo thứ tự: P tăng hay giảm (tăng = thận)? 25(OH)D thấp hay bình thường (thấp = thiếu D)? Nếu bình thường "
        "thì Ca và 1,25(OH)₂D phân định thể di truyền.",
        "4.3 Phân biệt", ["Phan-biet"],
    ),
    algo(
        "PED67-A-02", "S7", "Liều bỏ túi",
        "Bảng liều bỏ túi điều trị còi xương",
        f"1) {G('Vitamin D3')} (Đồng thuận 2016, ≥ {Y('12 tuần')}): {Y('dưới 12 tháng')} {G('2.000 IU/ngày')}; "
        f"{Y('1–12 tuổi')} {G('3.000–6.000 IU/ngày')}; {Y('trên 12 tuổi')} {G('6.000 IU/ngày')}.<br>"
        f"2) Vitamin D một lần (stoss): {G('50.000 IU')} (3–12 tháng), {G('150.000 IU')} (1–12 tuổi), {G('300.000 IU')} (trên 12 tuổi); "
        f"{R('không dùng dưới 3 tháng')}.<br>"
        f"3) {G('Duy trì')}: {G('400 IU/ngày')} (dưới 1 tuổi), {G('600 IU/ngày')} (từ 1 tuổi).<br>"
        f"4) {G('Calci nguyên tố')}: khoảng {G('500 mg/ngày')}.<br>"
        f"5) {G('Calci gluconat 10%')} khi co giật: {Y('0,5–1 mL/kg')}, tối đa {Y('20 mL')}, TM chậm {Y('5–10 phút')}.",
        "Sách Việt Nam hay ghi phác đồ ngắn hơn: 2.000–4.000 IU/ngày × 4–6 tuần rồi 400 IU/ngày.",
        "5.2–5.4 Điều trị", ["Lieu"], warn=True,
    ),
    algo(
        "PED67-A-03", "S7", "Cấp cứu hạ calci",
        "Co giật do hạ calci ở trẻ còi xương: 3 NÊN & 3 KHÔNG",
        f"1) {G('NÊN')}: tiêm {G('calci gluconat 10% TM chậm')} có {G('theo dõi nhịp tim')}.<br>"
        f"2) {G('NÊN')}: kiểm tra và {G('bù magie')} nếu thấp.<br>"
        f"3) {G('NÊN')}: chuyển {G('calci uống')} rồi mới cho {G('vitamin D')} kèm calci.<br>"
        f"4) {R('KHÔNG')}: tiêm calci nhanh (nguy cơ {R('chậm nhịp, ngừng tim')}).<br>"
        f"5) {R('KHÔNG')}: để {R('thoát mạch')} calci (hoại tử mô).<br>"
        f"6) {R('KHÔNG')}: cho {R('vitamin D liều cao trước khi nâng Ca')} (xương đói calci làm Ca tụt thêm).",
        "Trình tự nhớ: 'Ca trước – Mg kiểm – D sau'.",
        "5.4 Hạ calci", ["Cap-cuu"], warn=True,
    ),
    algo(
        "PED67-A-04", "S3", "Lưu đồ chẩn đoán",
        "Trẻ nghi còi xương: lưu đồ 3 bước",
        f"1) {B('Bước 1 – Lâm sàng')}: yếu tố nguy cơ + dấu hiệu {R('đúng tuổi')} (sọ / ngực, cổ tay / chân / đau) + "
        f"loại trừ {Y('biến dạng sinh lý')}.<br>"
        f"2) {B('Bước 2 – Xét nghiệm')}: {G('Ca, P, ALP, 25(OH)D, PTH, creatinin')} + {G('X quang cổ tay hoặc gối')}.<br>"
        f"3) {B('Bước 3 – Quyết định')}: 25(OH)D thấp, P giảm, ALP tăng → {G('điều trị vitamin D + calci')}, kiểm tra lại sau "
        f"{Y('3 tháng')}; có co giật → {R('nâng Ca trước')}; điều trị đúng mà không đáp ứng → {R('tìm thể kháng, phụ thuộc, bệnh thận')}.",
        "Mục tiêu lưu đồ: không bỏ sót hạ calci cấp, không điều trị oan biến dạng sinh lý, không 'tăng liều vô hạn' khi bệnh không phải thiếu D.",
        "2–5 Tổng hợp", ["Tiep-can"],
    ),
]
