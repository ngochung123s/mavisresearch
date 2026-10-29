# -*- coding: utf-8 -*-
# PED-68 Khám phát triển thể chất trẻ em theo EBM — nguồn thẻ duy nhất (chuyên đề EBM quốc tế, KHÔNG phải barem trường).
# Nội dung: PED-68_Kham_phat_trien_the_chat_tre_em_CHUYEN_DE_EBM.pdf
# (WHO Child Growth Standards 2006; WHO Growth Reference 2007; WHO 2023 guideline wasting & nutritional oedema;
#  INTERGROWTH-21st preterm postnatal standards; AAP CPG 2023 + CDC extended BMI 2022; PES 2016; Turner 2017).
# Mục chuyên đề ghi ở `extra`. Ngưỡng thực hành không có trong guideline gốc → ghi ⚠️ ở `extra`.


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý / bất thường
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / mốc / tuổi
    return _c("#ffd43b", t)


def G(t):  # xử trí / dụng cụ / kỹ thuật / tiêu chuẩn
    return _c("#51cf66", t)


def B(t):  # tên chỉ số / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("📘 CHUYÊN ĐỀ EBM · PHÁT TRIỂN THỂ CHẤT", "badge-ebm")
SRC = ("📖 Nguồn: Chuyên đề PED-68 Khám phát triển thể chất trẻ em theo EBM quốc tế (WHO Child Growth Standards 2006; "
       "WHO Growth Reference 2007; WHO 2023 Guideline on wasting and nutritional oedema; INTERGROWTH-21st; "
       "AAP CPG 2023). Mục: ")
WARN = " · ⚠️ Ngưỡng thực hành lâm sàng, không phải tiêu chí chẩn đoán của guideline; barem trường có thể ghi khác."
TAG = ["PED-68", "Chuyen-de-EBM"]


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
    # ------------------------------------------------------------ S1. Nguyên tắc & chuẩn tham chiếu
    basic(
        "PED68-S1-01", "S1", "Nguyên tắc", 1,
        f"{B('[Nguyên tắc EBM]')} Theo EBM, đánh giá phát triển thể chất trẻ em dựa trên 3 nguyên tắc nào "
        f"(thay cho {R('công thức ước tính theo tuổi')})?",
        f"1) {G('Đo đúng kỹ thuật chuẩn hoá')}: dụng cụ, tư thế, độ chính xác, đo lặp.<br>"
        f"2) {G('Quy đổi ra Z-score / bách phân vị')} trên {B('chuẩn tham chiếu đúng')} theo tuổi, giới "
        f"(và {Y('tuổi hiệu chỉnh')} nếu sinh non).<br>"
        f"3) {G('Diễn giải động')}: đường tăng trưởng qua nhiều lần đo, tốc độ tăng trưởng, so với tiềm năng di truyền — "
        f"{R('không kết luận từ một lần đo')}.",
        f"Công thức kiểu {R('“9 + 2(N−1)” kg')} hay {R('“75 + 5(N−1)” cm')} chỉ cho con số trung bình, không cho biết trẻ lệch "
        f"bao nhiêu so với quần thể chuẩn. Z-score trả lời đúng câu hỏi đó: trẻ cách trung vị bao nhiêu độ lệch chuẩn. "
        f"Mốc dễ nhớ: {Y('−2 SD ≈ bách phân vị 2,3')}, {Y('+2 SD ≈ bách phân vị 97,7')}, {Y('−3 SD ≈ bách phân vị 0,1')}.",
        "Nguyên tắc cốt lõi", ["Nguyen-tac"],
    ),
    basic(
        "PED68-S1-02", "S1", "Chuẩn tham chiếu", 1,
        f"{B('[Chuẩn tham chiếu]')} Dùng chuẩn nào cho: {Y('trẻ 0–5 tuổi')}, {Y('trẻ 5–19 tuổi')}, "
        f"{Y('trẻ sinh non')} và khi cần {R('phân độ béo phì nặng')}?",
        f"1) {Y('Trẻ 0–5 tuổi')}: {B('WHO Child Growth Standards (2006)')}.<br>"
        f"2) {Y('Trẻ 5–19 tuổi')}: {B('WHO Growth Reference (2007)')} — BMI/tuổi, chiều cao/tuổi.<br>"
        f"3) {Y('Trẻ sinh non')}: {B('INTERGROWTH-21st Postnatal Growth Standards for Preterm Infants')} đến "
        f"{Y('64 tuần PMA')}, sau đó chuyển sang WHO theo {Y('tuổi hiệu chỉnh')}.<br>"
        f"4) {R('Béo phì nặng')} cần phân độ (tham khảo): {B('AAP CPG 2023 + CDC Extended BMI-for-age (2022)')}, trẻ 2–19 tuổi.",
        f"Ở Việt Nam đánh giá thường quy vẫn theo {B('WHO Z-score')}; khi dùng AAP/CDC phải ghi rõ chuẩn đã dùng trong bệnh án. "
        f"Fenton (2013) là biểu đồ sinh non thay thế phổ biến trong NICU.",
        "1. Chuẩn tham chiếu", ["Chuan-tham-chieu"],
    ),
    basic(
        "PED68-S1-03", "S1", "Chuẩn tham chiếu", 2,
        f"{B('[WHO 2006]')} Vì sao {B('WHO Child Growth Standards 2006')} được gọi là “chuẩn” (standard) chứ không chỉ là "
        f"“tham chiếu”? Trẻ trong mẫu xây dựng có đặc điểm gì?",
        f"1) Mẫu: trẻ {G('bú mẹ')}, sống trong {G('môi trường tối ưu')} (dinh dưỡng, y tế, không hút thuốc), từ "
        f"{Y('6 quốc gia')}.<br>"
        f"2) Ý nghĩa: mô tả trẻ {G('nên lớn thế nào')} (chuẩn quy định), không chỉ trẻ {R('đang lớn thế nào')}.",
        f"Vì mẫu được chọn trong điều kiện tối ưu ở nhiều châu lục, chuẩn WHO áp dụng được cho mọi trẻ bất kể chủng tộc — "
        f"trẻ Việt Nam lệch khỏi chuẩn là do môi trường/bệnh, không phải “gen người Việt nhỏ”. Ngược lại, "
        f"{B('WHO 2007')} cho 5–19 tuổi là {B('tham chiếu')} (reference) dựng lại từ số liệu NCHS 1977.",
        "1. Chuẩn tham chiếu", ["Chuan-tham-chieu"],
    ),
    basic(
        "PED68-S1-04", "S1", "Công cụ", 2,
        f"{B('[Công cụ tính Z-score]')} Kể các công cụ tính Z-score cho {Y('0–5 tuổi')}, {Y('5–19 tuổi')}, {Y('trẻ sinh non')} "
        f"và lý do không nên ước lượng bằng mắt trên biểu đồ.",
        f"1) {Y('0–5 tuổi')}: {G('WHO Anthro')}.<br>"
        f"2) {Y('5–19 tuổi')}: {G('WHO AnthroPlus')}.<br>"
        f"3) {Y('Sinh non')}: {G('INTERGROWTH-21st online calculator')}.<br>"
        f"4) Lý do: tính {G('Z-score chính xác')}, tránh {R('sai số nội suy bằng mắt')}.",
        "Khi chấm tay, sai lệch nửa ô lưới ở vùng gần −2 SD có thể đổi kết luận từ “bình thường” sang “SDD vừa”. "
        "Phần mềm dùng phương pháp LMS của WHO nên xử lý đúng cả phân bố lệch của cân nặng.",
        "1. Chuẩn tham chiếu", ["Cong-cu"],
    ),
    basic(
        "PED68-S1-05", "S1", "Chuẩn tham chiếu", 2,
        f"{B('[WHO 2007]')} Với trẻ 5–19 tuổi, chỉ số {B('cân nặng/tuổi')} dùng được đến bao nhiêu tuổi và sau đó thay bằng chỉ số nào?",
        f"1) {B('CN/tuổi')} chỉ có đến {Y('10 tuổi')}.<br>"
        f"2) Sau {Y('10 tuổi')}: dùng {B('BMI/tuổi')}.",
        "Từ khoảng 10 tuổi, cân nặng bị dậy thì chi phối mạnh (trẻ cao nhanh nặng nhanh) nên CN/tuổi không còn phân biệt được "
        "trẻ gầy với trẻ chỉ đơn giản là thấp/chưa dậy thì; BMI/tuổi điều chỉnh theo chiều cao nên phù hợp hơn.",
        "1. Chuẩn tham chiếu", ["Chuan-tham-chieu"],
    ),
    cloze(
        "PED68-S1-C1", "S1", "Sinh non",
        f"Trẻ sinh non chấm trên INTERGROWTH-21st đến {{{{c1::{Y('64 tuần tuổi sau kinh cuối (PMA) – tức 6 tháng tuổi hiệu chỉnh')}}}}}, "
        f"rồi chuyển sang biểu đồ WHO.",
        "1. Chuẩn tham chiếu", ["Sinh-non"],
    ),

    # ------------------------------------------------------------ S2. Hỏi bệnh
    basic(
        "PED68-S2-01", "S2", "Hỏi bệnh", 1,
        f"{B('[Hỏi bệnh]')} Hỏi bệnh khi khám phát triển thể chất nhằm 3 mục tiêu nào và gồm 6 nhóm nội dung nào?",
        f"1) {B('Mục tiêu')}: xác định {Y('tuổi chính xác')}, {G('tiềm năng tăng trưởng')} (chu sinh, di truyền) và "
        f"{R('yếu tố làm lệch đường tăng trưởng')} (dinh dưỡng, bệnh, thuốc, tâm lý xã hội).<br>"
        f"2) {B('Nội dung (6 nhóm)')}: {Y('tuổi')} — {B('tiền sử chu sinh')} — {G('dinh dưỡng')} — {R('bệnh lý và thuốc')} — "
        f"{B('gia đình')} — {G('số đo cũ')}.",
        "Thứ tự hỏi đi từ “trẻ bắt đầu từ đâu” (tuổi, chu sinh, di truyền) đến “điều gì kéo trẻ lệch đi” (ăn, bệnh, thuốc, "
        "hoàn cảnh), cuối cùng là bằng chứng lệch thế nào (số đo cũ).",
        "2. Hỏi bệnh", ["Hoi-benh"], asks=["Mục tiêu", "Nội dung"],
    ),
    basic(
        "PED68-S2-02", "S2", "Tuổi", 1,
        f"{B('[Tuổi hiệu chỉnh]')} Viết công thức tính {Y('tuổi hiệu chỉnh')} cho trẻ sinh non, cho biết dùng đến bao lâu, "
        f"và tính ví dụ: sinh {Y('32 tuần')}, nay {Y('6 tháng')} tuổi thực.",
        f"1) {G('Công thức')}: tuổi hiệu chỉnh = tuổi thực − ({Y('40')} − tuổi thai lúc sinh) tuần.<br>"
        f"2) {G('Thời gian dùng')}: cho mọi chỉ số đến {Y('ít nhất 24 tháng')}.<br>"
        f"3) {G('Ví dụ')}: non {Y('8 tuần (≈ 2 tháng)')} → tuổi hiệu chỉnh ≈ {Y('4 tháng')}.",
        f"Không hiệu chỉnh tuổi sẽ so trẻ sinh non với trẻ đủ tháng lớn hơn → {R('chẩn đoán nhầm SDD/thấp còi')}. "
        f"Ngày sinh cũng phải lấy chính xác đến ngày: ở nhũ nhi, sai vài tuần tuổi đã làm Z-score lệch đáng kể.",
        "2.1 Tuổi", ["Tuoi", "Sinh-non"],
    ),
    basic(
        "PED68-S2-03", "S2", "Chu sinh", 1,
        f"{B('[Tiền sử chu sinh]')} Khi khám phát triển thể chất cần hỏi những gì về giai đoạn chu sinh?",
        f"1) {Y('Tuổi thai')}; {Y('cân nặng – chiều dài – vòng đầu lúc sinh')} → phân loại {B('SGA / AGA / LGA')} "
        f"(INTERGROWTH-21st newborn size standards).<br>"
        f"2) Bệnh lý thai kỳ: {R('tiền sản giật')}, {R('đái tháo đường')}, {R('nhiễm trùng bào thai')}, {R('rượu / thuốc lá')}.<br>"
        f"3) {R('Ngạt')}, bệnh lý sơ sinh: {R('BPD')}, {R('NEC')}, {R('nuôi dưỡng tĩnh mạch kéo dài')}.",
        "Cân nặng lúc sinh cho biết điểm xuất phát; tuổi thai cho biết phải hiệu chỉnh tuổi hay không; còn các bệnh sơ sinh "
        "nặng (loạn sản phế quản phổi, viêm ruột hoại tử) là nguyên nhân hay gặp của chậm lớn kéo dài ở trẻ sinh non.",
        "2.2 Chu sinh", ["Chu-sinh"],
    ),
    basic(
        "PED68-S2-04", "S2", "SGA", 2,
        f"{B('[Trẻ SGA]')} Đa số trẻ {B('SGA')} bắt kịp tăng trưởng trong khoảng thời gian nào, và khi nào cần đánh giá chuyên khoa nội tiết?",
        f"1) Đa số {G('bắt kịp')} trong {Y('2 năm đầu')}.<br>"
        f"2) {R('Không bắt kịp ở tuổi 2–4')} → đánh giá {G('chuyên khoa nội tiết')}.",
        "Trẻ SGA bắt kịp thường tăng tốc mạnh trong 6–12 tháng đầu. Nhóm không bắt kịp có nguy cơ thấp kéo dài đến tuổi "
        "trưởng thành và là một chỉ định điều trị hormon tăng trưởng được công nhận, nên cần chuyển sớm để không lỡ thời điểm.",
        "2.2 Chu sinh", ["Chu-sinh", "SGA"],
    ),
    basic(
        "PED68-S2-05", "S2", "Sơ sinh", 2,
        f"{B('[Sụt cân sinh lý]')} Trẻ sơ sinh thường về lại cân nặng lúc sinh sau bao lâu, và khi nào sụt cân cần đánh giá?",
        f"1) Thường về lại cân nặng lúc sinh trong khoảng {Y('10–14 ngày')}.<br>"
        f"2) {R('Sụt cân nhiều hoặc kéo dài')} → {G('đánh giá bú mẹ')}.",
        "Sụt cân những ngày đầu là do mất nước ngoại bào và phân su. Trẻ chưa lấy lại cân nặng lúc sinh sau 2 tuần là dấu hiệu "
        "sớm nhất của bú không hiệu quả, cần quan sát một cữ bú thực tế.",
        "2.2 Chu sinh", ["So-sinh"],
    ),
    basic(
        "PED68-S2-06", "S2", "Dinh dưỡng", 1,
        f"{B('[Hỏi dinh dưỡng]')} Hỏi dinh dưỡng gồm những nội dung nào: {Y('bú sữa')}, {Y('ăn bổ sung')}, "
        f"{R('hành vi ăn')} và {Y('trẻ lớn')}?",
        f"1) {Y('Bú sữa')}: bú mẹ hoàn toàn / hỗn hợp, số cữ, dấu hiệu bú hiệu quả ({G('ngậm bắt vú, nuốt, số tã ướt')}); "
        f"sữa công thức: loại, cách pha, thể tích/ngày.<br>"
        f"2) {Y('Ăn bổ sung')}: thời điểm, chất lượng (đa dạng nhóm thực phẩm, tần suất, độ đặc), {G('hỏi khẩu phần 24 giờ')}.<br>"
        f"3) {R('Hành vi ăn')}: biếng ăn, ăn kéo dài, ép ăn, {R('nước ngọt / nước trái cây quá nhiều')}, "
        f"{R('uống sữa quá nhiều')} (thiếu sắt).<br>"
        f"4) {Y('Trẻ lớn')}: bữa phụ, đồ ăn nhanh, {R('thời gian màn hình')}, vận động, giấc ngủ.",
        "Hỏi khẩu phần 24 giờ cụ thể (sáng ăn gì, bao nhiêu) cho thông tin đáng tin hơn câu hỏi “cháu ăn có tốt không”. "
        "Uống quá nhiều sữa bò làm no, giảm ăn thực phẩm giàu sắt và gây mất máu ẩn qua ruột ở trẻ nhỏ.",
        "2.3 Dinh dưỡng", ["Dinh-duong"],
    ),
    basic(
        "PED68-S2-07", "S2", "Bệnh mạn", 1,
        f"{B('[Bệnh mạn gây chậm lớn]')} Kể các triệu chứng gợi ý bệnh mạn tính gây chậm lớn cần hỏi "
        f"(nhiễm trùng, tiêu hoá, thận, tim, phổi, ruột).",
        f"1) {R('Nhiễm trùng tái diễn')}, {R('tiêu chảy kéo dài')}, {R('nôn trớ')}.<br>"
        f"2) {B('Kém hấp thu')}: {R('phân mỡ, chướng bụng')} (celiac, xơ nang).<br>"
        f"3) {B('Bệnh thận')}: {R('đa niệu, phù')}.<br>"
        f"4) {B('Tim bẩm sinh')}: {R('bú mệt, vã mồ hôi')}.<br>"
        f"5) {B('Hen / bệnh phổi mạn')}.<br>"
        f"6) {B('Bệnh viêm ruột')}.",
        "Bệnh mạn làm chậm lớn qua 3 đường: ăn vào ít (chán ăn, khó thở khi bú), mất đi nhiều (kém hấp thu, tiểu đạm) và "
        "tiêu hao tăng (viêm, tăng công thở). Kiểu hình thường là cân nặng giảm trước chiều cao.",
        "2.4 Bệnh lý", ["Benh-man"],
    ),
    basic(
        "PED68-S2-08", "S2", "Nội tiết", 1,
        f"{B('[Gợi ý nội tiết]')} Triệu chứng nào khi hỏi bệnh gợi ý {B('suy giáp')}, {B('u vùng tuyến yên (craniopharyngioma)')} "
        f"và {B('Cushing')}?",
        f"1) {B('Suy giáp')}: {R('mệt, táo bón, chậm chạp')}.<br>"
        f"2) {B('U vùng tuyến yên')}: {R('đau đầu, nôn, giảm thị lực, đa niệu')}.<br>"
        f"3) {B('Cushing')}: {R('tăng cân + giảm tốc độ tăng chiều cao')}.",
        "Ba bệnh này chung một kiểu hình: chiều cao chững lại trong khi cân nặng giữ hoặc tăng. Đa niệu ở trẻ có u vùng "
        "tuyến yên gợi ý đái tháo nhạt trung ương do khối u chèn ép.",
        "2.4 Bệnh lý", ["Noi-tiet"],
    ),
    basic(
        "PED68-S2-09", "S2", "Thuốc", 2,
        f"{B('[Thuốc]')} Kể các nhóm thuốc cần hỏi vì ảnh hưởng tăng trưởng hoặc cân nặng.",
        f"1) {R('Glucocorticoid kéo dài')} (cả {R('dạng hít liều cao')}).<br>"
        f"2) {R('Thuốc kích thích điều trị ADHD')}.<br>"
        f"3) {R('Thuốc chống động kinh')}.<br>"
        f"4) {R('Thuốc gây tăng cân')}: corticoid, một số thuốc an thần kinh.",
        "Corticoid ức chế trục GH–IGF-1 và trực tiếp ức chế sụn tăng trưởng; thuốc kích thích giảm cảm giác thèm ăn. "
        "Hỏi cả corticoid hít ở trẻ hen dùng liều cao kéo dài — hay bị bỏ sót.",
        "2.4 Bệnh lý", ["Thuoc"],
    ),
    basic(
        "PED68-S2-10", "S2", "Phát triển & tâm lý", 2,
        f"{B('[Phát triển và tâm lý xã hội]')} Ngoài bệnh và thuốc, cần hỏi thêm về {Y('phát triển')} và {R('hoàn cảnh tâm lý xã hội')} "
        f"những gì? Vì sao?",
        f"1) {Y('Phát triển tâm vận động')}; {Y('mốc dậy thì')} (trẻ lớn).<br>"
        f"2) {R('Hoàn cảnh gia đình, người chăm sóc, sang chấn, bỏ bê')}.<br>"
        f"3) Lý do: {R('thiếu hụt tâm lý xã hội có thể gây chậm lớn')}.",
        "Chậm lớn do tâm lý xã hội (psychosocial dwarfism) có thể kèm giảm tiết GH có hồi phục; trẻ thường lớn bắt kịp nhanh "
        "khi được đưa vào môi trường chăm sóc tốt.",
        "2.4 Bệnh lý", ["Tam-ly-xa-hoi"],
    ),
    basic(
        "PED68-S2-11", "S2", "Gia đình", 1,
        f"{B('[Tiền sử gia đình]')} Cần hỏi gì về gia đình khi khám phát triển thể chất, và vì sao nên {G('đo trực tiếp')} "
        f"chiều cao bố mẹ?",
        f"1) {G('Chiều cao bố và mẹ — nên đo trực tiếp')} vì {R('chiều cao tự khai thường sai lệch')}.<br>"
        f"2) {Y('Tuổi dậy thì của bố mẹ')}: tuổi có kinh của mẹ; bố “lớn muộn”? → gợi ý {B('chậm tăng trưởng thể tạng')}.<br>"
        f"3) Bệnh trong gia đình: {B('lùn, bệnh xương, bệnh nội tiết')}, {B('béo phì, đái tháo đường type 2, rối loạn lipid')}.",
        "Chiều cao bố mẹ dùng để tính chiều cao đích; sai vài cm khi tự khai làm lệch cả khoảng đích. Tiền sử “bố cũng thấp "
        "rồi đến 16–17 tuổi mới vọt lên” là manh mối mạnh của chậm dậy thì thể tạng.",
        "2.5 Gia đình", ["Gia-dinh"],
    ),
    basic(
        "PED68-S2-12", "S2", "Số đo cũ", 2,
        f"{B('[Số đo cũ]')} Lấy số đo cũ của trẻ ở đâu và dùng chúng thế nào?",
        f"1) Nơi lấy: {G('sổ theo dõi sức khoẻ bà mẹ – trẻ em')}, {G('sổ tiêm chủng')}, {G('hồ sơ khám')}.<br>"
        f"2) Cách dùng: {G('chấm tất cả lên biểu đồ')} — {Y('một chuỗi số đo có giá trị hơn nhiều một lần đo đơn lẻ')}.",
        "Một lần đo chỉ cho vị trí; chuỗi số đo cho hướng đi và tốc độ. Trẻ ở −1,5 SD đi ngang đều từ nhỏ khác hẳn trẻ ở −1,5 SD "
        "vừa tụt xuống từ +0,5 SD.",
        "2.6 Số đo cũ", ["So-do-cu"],
    ),
    cloze(
        "PED68-S2-C1", "S2", "Tuổi hiệu chỉnh",
        f"Trẻ sinh non dùng tuổi hiệu chỉnh cho mọi chỉ số tăng trưởng đến ít nhất {{{{c1::{Y('24 tháng')}}}}}.",
        "2.1 Tuổi", ["Sinh-non"],
    ),

    # ------------------------------------------------------------ S3. Đo nhân trắc chuẩn hoá
    basic(
        "PED68-S3-01", "S3", "Nguyên tắc đo", 1,
        f"{B('[Nguyên tắc đo]')} Nêu các nguyên tắc chung khi đo nhân trắc trẻ em (dụng cụ, trang phục, số lần đo, cách ghi).",
        f"1) Dụng cụ {G('được chuẩn hoá / hiệu chỉnh định kỳ')}.<br>"
        f"2) Trẻ {G('mặc tối thiểu')}, {G('không giày')}, {G('không kẹp / búi tóc')}.<br>"
        f"3) {G('Đo 2 lần')}; chênh lệch vượt ngưỡng cho phép thì {G('đo lần 3')}; ghi {G('giá trị trung bình')}.<br>"
        f"4) {G('Ghi ngay')}, kèm {Y('ngày đo')} và {Y('tư thế đo')}.",
        "Sai số đo thường lớn hơn mức thay đổi thật giữa hai lần khám — đó là lý do phải đo lặp và ghi tư thế. "
        "Búi tóc có thể làm sai chiều cao vài cm.",
        "3. Đo nhân trắc", ["Ky-thuat-do"],
    ),
    basic(
        "PED68-S3-02", "S3", "Cân nặng", 1,
        f"{B('[Cân nặng]')} Cân trẻ bằng dụng cụ gì, độ chính xác bao nhiêu, kỹ thuật với trẻ chưa đứng được, và cần ghi chú gì?",
        f"1) Dụng cụ: {G('cân điện tử')}, đọc đến {Y('0,1 kg')} (cân nhũ nhi: {Y('10–20 g')}).<br>"
        f"2) Kỹ thuật: {G('cởi tã, mặc tối thiểu')}; trẻ chưa đứng: {G('cân nhũ nhi')} hoặc {G('cân mẹ – con')} "
        f"(cân mẹ, trừ bì, rồi bế trẻ).<br>"
        f"3) Ghi chú: {Y('giờ cân')}, tình trạng ({R('sau ăn, phù, mất nước')}).",
        "Phù và mất nước làm cân nặng không phản ánh đúng khối mô: trẻ phù dinh dưỡng có thể “nặng bình thường” dù rất gầy. "
        "Cân mẹ – con dùng chức năng trừ bì để chỉ hiện cân nặng của trẻ.",
        "3. Đo nhân trắc", ["Can-nang"],
    ),
    basic(
        "PED68-S3-03", "S3", "Chiều dài nằm", 1,
        f"{B('[Chiều dài nằm]')} Đo chiều dài nằm áp dụng cho trẻ bao nhiêu tuổi, dùng dụng cụ gì, độ chính xác bao nhiêu, "
        f"kỹ thuật 2 người thế nào và cách đo nào {R('không đạt chuẩn')}?",
        f"1) Áp dụng: trẻ {Y('dưới 2 tuổi')}.<br>"
        f"2) Dụng cụ: {G('thước đo chiều dài (length board)')} có chặn đầu cố định, chặn chân di động; đọc đến {Y('0,1 cm')}.<br>"
        f"3) {G('2 người đo')}: người 1 giữ đầu sát chặn đầu, {G('mặt phẳng Frankfurt thẳng đứng')}; người 2 ấn nhẹ gối duỗi "
        f"thẳng, áp chặn chân vuông góc vào gót.<br>"
        f"4) {R('Thước dây / đo trên giường')} → không đạt chuẩn.",
        "Mặt phẳng Frankfurt là đường nối lỗ tai ngoài với bờ dưới hốc mắt. Một người đo không giữ được đồng thời đầu và gối "
        "của trẻ quấy khóc, nên sai số rất lớn; thước dây trên giường bị võng và không có chặn vuông góc.",
        "3. Đo nhân trắc", ["Chieu-dai"],
    ),
    basic(
        "PED68-S3-04", "S3", "Chiều cao đứng", 1,
        f"{B('[Chiều cao đứng]')} Đo chiều cao đứng áp dụng từ tuổi nào, dụng cụ gì, độ chính xác bao nhiêu và tư thế chuẩn thế nào?",
        f"1) Áp dụng: trẻ {Y('từ 2 tuổi')}.<br>"
        f"2) Dụng cụ: {G('thước đo đứng gắn tường (stadiometer)')}; đọc đến {Y('0,1 cm')}.<br>"
        f"3) Tư thế: {G('chân trần, gót chụm')}; {G('gót – mông – vai – chẩm (nếu được) chạm thước')}; "
        f"{G('mặt phẳng Frankfurt nằm ngang')}; hít vào nhẹ; hạ chặn đầu ép tóc.<br>"
        f"4) Khi theo dõi: đo {Y('cùng thời điểm trong ngày')} (chiều cao giảm nhẹ về chiều).",
        "Đĩa đệm cột sống bị nén dần trong ngày nên chiều cao buổi chiều thấp hơn buổi sáng một chút; đo vào giờ khác nhau "
        "giữa hai lần khám có thể tạo ra “chậm lớn” giả.",
        "3. Đo nhân trắc", ["Chieu-cao"],
    ),
    basic(
        "PED68-S3-05", "S3", "Hiệu chỉnh tư thế", 1,
        f"{B('[Hiệu chỉnh tư thế WHO]')} Khi đo sai tư thế so với tuổi, phải hiệu chỉnh số đo thế nào trước khi tra chuẩn WHO?",
        f"1) Trẻ {Y('dưới 2 tuổi')} nhưng {R('đo đứng')}: {G('cộng 0,7 cm')}.<br>"
        f"2) Trẻ {Y('từ 2 tuổi')} nhưng {R('đo nằm')}: {G('trừ 0,7 cm')}.",
        "Chiều dài nằm luôn lớn hơn chiều cao đứng của cùng một trẻ khoảng 0,7 cm (cột sống và gót không chịu lực). "
        "Chuẩn WHO đổi từ chiều dài sang chiều cao đúng ở mốc 2 tuổi nên phải quy về đúng tư thế của chuẩn.",
        "3. Đo nhân trắc", ["Hieu-chinh"],
    ),
    basic(
        "PED68-S3-06", "S3", "Vòng đầu", 1,
        f"{B('[Vòng đầu]')} Đo vòng đầu bằng dụng cụ gì, độ chính xác bao nhiêu, ở vị trí nào, đo mấy lần, và bắt buộc đo đến tuổi nào?",
        f"1) Dụng cụ: {G('thước dây không giãn')}; đọc đến {Y('0,1 cm')}.<br>"
        f"2) Vị trí: {G('chu vi chẩm – trán lớn nhất')} — ngay trên cung mày, qua chỗ nhô nhất của xương chẩm.<br>"
        f"3) {G('Đo 3 lần, lấy giá trị lớn nhất')}.<br>"
        f"4) Bắt buộc ở mọi lần khám đến {Y('2 tuổi')} (chuẩn WHO có đến {Y('5 tuổi')}).",
        "Vòng đầu là chỉ điểm gián tiếp của sự lớn của não, tăng nhanh nhất trong 2 năm đầu — đây là cửa sổ phát hiện "
        "đầu nhỏ, não úng thuỷ. Lấy giá trị lớn nhất vì đặt lệch thước chỉ làm số đo nhỏ đi.",
        "3. Đo nhân trắc", ["Vong-dau"],
    ),
    basic(
        "PED68-S3-07", "S3", "MUAC", 1,
        f"{B('[MUAC]')} Đo chu vi vòng cánh tay (MUAC) bằng dụng cụ gì, độ chính xác bao nhiêu, kỹ thuật thế nào và "
        f"dùng cho trẻ từ bao nhiêu tuổi?",
        f"1) Dụng cụ: {G('thước MUAC chuyên dụng')}; đọc đến {Y('1 mm')}.<br>"
        f"2) Kỹ thuật: {G('tay trái buông thõng')}; đánh dấu {G('điểm giữa mỏm cùng vai – mỏm khuỷu')} "
        f"(gấp khuỷu {Y('90°')} khi đánh dấu); quấn thước {G('vừa khít, không ép lõm da')}.<br>"
        f"3) Đối tượng: trẻ {Y('từ 6 tuần tuổi')} — {R('không dùng dưới 6 tuần')}.",
        "Dưới 6 tuần, MUAC bị ảnh hưởng bởi dịch chuyển nước sau sinh và khối cơ còn ít nên chưa có ngưỡng đáng tin. "
        "Quấn quá chặt làm MUAC nhỏ giả → chẩn đoán SDD oan.",
        "3. Đo nhân trắc", ["MUAC"],
    ),
    basic(
        "PED68-S3-08", "S3", "Phù dinh dưỡng", 1,
        f"{B('[Phù dinh dưỡng]')} Cách khám phù dinh dưỡng, phân độ (+, ++, +++) và ý nghĩa khi có phù hai bên?",
        f"1) Cách khám: {G('ấn đồng thời cả hai mu bàn chân')} khoảng {Y('3 giây')}; {R('lõm cả hai bên')} = phù dinh dưỡng.<br>"
        f"2) Phân độ: {Y('+')} bàn chân; {Y('++')} thêm cẳng chân / bàn tay / cẳng tay; {Y('+++')} toàn thân kể cả mặt.<br>"
        f"3) Ý nghĩa: {R('phù 2 bên = SDD cấp nặng bất kể nhân trắc')}; cân nặng lúc có phù {R('không phản ánh đúng dinh dưỡng')}.",
        "Phù dinh dưỡng (kiểu kwashiorkor) là dấu hiệu tử vong cao độc lập với WHZ, nên không cần chờ cân đo để phân loại nặng. "
        "Phải ấn cả hai bên để phân biệt với phù một bên do viêm, chấn thương.",
        "3. Đo nhân trắc", ["Phu"], asks=["Cách khám", "Phân độ", "Ý nghĩa"],
    ),
    basic(
        "PED68-S3-09", "S3", "BMI", 2,
        f"{B('[BMI]')} Tính BMI thế nào và diễn giải BMI ở trẻ em khác người lớn ra sao?",
        f"1) {G('BMI = CN (kg) / CC² (m²)')}.<br>"
        f"2) Diễn giải theo {B('BMI/tuổi/giới')} — {R('không dùng ngưỡng người lớn')}.",
        "BMI sinh lý của trẻ thay đổi mạnh theo tuổi (tăng trong năm đầu, giảm đến khoảng 5–6 tuổi rồi tăng lại — "
        "“adiposity rebound”), nên cùng một BMI có thể bình thường ở tuổi này và béo phì ở tuổi khác.",
        "3. Đo nhân trắc", ["BMI"],
    ),
    basic(
        "PED68-S3-10", "S3", "Tỷ lệ cơ thể", 2,
        f"{B('[Tỷ lệ cơ thể]')} Khi trẻ thấp, đo những tỷ lệ cơ thể nào và bất thường gợi ý bệnh gì?",
        f"1) {G('Chiều cao ngồi')} → tỷ lệ chiều cao ngồi / chiều cao.<br>"
        f"2) {G('Tỷ lệ đoạn trên / đoạn dưới')} (đoạn dưới = khớp mu → gót).<br>"
        f"3) {G('Sải tay')} so với chiều cao.<br>"
        f"4) Bất thường gợi ý {B('loạn sản xương')} (vd {B('thiếu hụt SHOX')}, {B('achondroplasia')}).",
        "Trẻ thấp cân đối thường do dinh dưỡng, nội tiết, di truyền gia đình; trẻ thấp không cân đối (chi ngắn so với thân) "
        "gợi ý bệnh của sụn tiếp hợp chi. Thiếu hụt SHOX có thể chỉ biểu hiện bằng cẳng tay ngắn kín đáo.",
        "3. Đo nhân trắc", ["Ty-le-co-the"],
    ),
    basic(
        "PED68-S3-11", "S3", "Dậy thì", 2,
        f"{B('[Đánh giá dậy thì]')} Đánh giá dậy thì bằng gì ở {Y('trẻ gái')} và {Y('trẻ trai')}? Dấu hiệu bắt đầu dậy thì ở trẻ trai là gì?",
        f"1) {Y('Trẻ gái')}: {B('Tanner')} vú ({Y('B1–5')}), lông mu ({Y('PH1–5')}).<br>"
        f"2) {Y('Trẻ trai')}: thể tích tinh hoàn bằng {G('thước Prader')}, dương vật/bìu ({Y('G1–5')}), lông mu.<br>"
        f"3) Bắt đầu dậy thì ở trai: {Y('tinh hoàn ≥ 4 ml')}.",
        "Ở trẻ gái dấu hiệu đầu tiên là nụ vú (B2). Ở trẻ trai, tinh hoàn to lên trước lông mu và dương vật — nên lông mu "
        "đơn độc không có tinh hoàn to gợi ý nguồn androgen thượng thận chứ không phải dậy thì trung ương.",
        "3. Đo nhân trắc", ["Day-thi"],
    ),
    basic(
        "PED68-S3-12", "S3", "Chất lượng số đo", 1,
        f"{B('[Kiểm tra chất lượng số đo]')} Ngưỡng Z-score “cờ” trong WHO Anthro cho {B('HAZ')}, {B('WHZ')}, {B('WAZ')} là bao nhiêu, "
        f"gặp thì làm gì, và chiều cao “giảm” giữa hai lần đo được hiểu thế nào?",
        f"1) {B('HAZ')} {Y('< −6 hoặc > +6')}.<br>"
        f"2) {B('WHZ')} {Y('< −5 hoặc > +5')}.<br>"
        f"3) {B('WAZ')} {Y('< −6 hoặc > +5')}.<br>"
        f"4) Gặp cờ → {G('đo lại trước khi kết luận')} (nhiều khả năng sai số đo / nhập liệu).<br>"
        f"5) {R('Chiều cao “giảm”')} giữa hai lần đo = {R('sai số')} cho đến khi chứng minh ngược lại.",
        "Z-score cực đoan như vậy gần như không gặp ở trẻ sống; hay gặp nhất là nhập nhầm ngày sinh, đảo cm/mm, nhầm giới. "
        "Chiều cao sinh học không giảm ở trẻ đang lớn.",
        "3. Đo nhân trắc", ["Chat-luong"],
    ),
    cloze(
        "PED68-S3-C1", "S3", "Hiệu chỉnh",
        f"Trẻ dưới 2 tuổi đo đứng phải {{{{c1::{G('cộng 0,7 cm')}}}}}; trẻ từ 2 tuổi đo nằm phải {{{{c2::{G('trừ 0,7 cm')}}}}} "
        f"trước khi tra chuẩn WHO.",
        "3. Đo nhân trắc", ["Hieu-chinh"],
    ),
    cloze(
        "PED68-S3-C2", "S3", "Độ chính xác",
        f"Chiều dài, chiều cao và vòng đầu đọc chính xác đến {{{{c1::{Y('0,1 cm')}}}}}.",
        "3. Đo nhân trắc", ["Ky-thuat-do"],
    ),
    cloze(
        "PED68-S3-C3", "S3", "Độ chính xác",
        f"MUAC đọc chính xác đến {{{{c1::{Y('1 mm')}}}}}.",
        "3. Đo nhân trắc", ["MUAC"],
    ),

    # ------------------------------------------------------------ S4. Ý nghĩa chỉ số & phân loại 0–59 tháng
    basic(
        "PED68-S4-01", "S4", "Ý nghĩa chỉ số", 1,
        f"{B('[Ý nghĩa chỉ số]')} Mỗi chỉ số {B('CN/CC (WHZ)')}, {B('CC/T (HAZ)')}, {B('CN/T (WAZ)')}, {B('MUAC')}, "
        f"{B('vòng đầu/tuổi')} phản ánh điều gì?",
        f"1) {B('WHZ')} (hoặc BMI/tuổi): dinh dưỡng {R('cấp')} (gầy còm) hoặc {R('thừa cân')}.<br>"
        f"2) {B('HAZ')}: tăng trưởng tuyến tính, thiếu hụt {R('mạn')} (thấp còi).<br>"
        f"3) {B('WAZ')}: chỉ số {Y('tổng hợp')} (cấp + mạn).<br>"
        f"4) {B('MUAC')}: khối cơ – mỡ; {R('tiên lượng tử vong mạnh')}.<br>"
        f"5) {B('Vòng đầu/tuổi')}: phát triển não – hộp sọ.",
        "Gầy còm là mất mô nhanh (tuần – tháng); thấp còi là hậu quả tích luỹ của nhiều tháng – năm. Vì vậy một trẻ có thể "
        "thấp còi mà không gầy, hoặc gầy mà chưa thấp.",
        "4.1 Ý nghĩa chỉ số", ["Chi-so"],
    ),
    basic(
        "PED68-S4-02", "S4", "Ý nghĩa chỉ số", 2,
        f"{B('[Giới hạn từng chỉ số]')} Nêu ưu điểm/giới hạn khi dùng {B('WHZ')}, {B('HAZ')}, {B('WAZ')}, {B('MUAC')}, {B('vòng đầu')}.",
        f"1) {B('WHZ')}: {G('độc lập với tuổi')} → hữu ích khi không rõ tuổi; {R('sai lệch khi có phù')}.<br>"
        f"2) {B('HAZ')}: phản ánh tích luỹ của {Y('dinh dưỡng, nhiễm trùng, chu sinh, di truyền, nội tiết')}.<br>"
        f"3) {B('WAZ')}: {R('không phân biệt gầy với thấp')}; {R('không dùng chẩn đoán thừa cân')}; chỉ đến {Y('10 tuổi')}.<br>"
        f"4) {B('MUAC')}: tiêu chí {G('độc lập với WHZ')} ({Y('6–59 tháng')}) — trẻ có thể đạt tiêu chí này mà không đạt tiêu chí kia.<br>"
        f"5) {B('Vòng đầu')}: diễn giải {G('cùng chiều dài và vòng đầu bố mẹ')}, theo dõi tốc độ.",
        "WHZ và MUAC chọn ra hai nhóm trẻ chồng lấn một phần: MUAC hay bắt trẻ nhỏ tuổi, trẻ gái; WHZ hay bắt trẻ chân dài "
        "so với thân (tỷ lệ chiều cao ngồi thấp). Vì vậy chỉ cần đạt một tiêu chí là đủ chẩn đoán SDD cấp.",
        "4.1 Ý nghĩa chỉ số", ["Chi-so"],
    ),
    basic(
        "PED68-S4-03", "S4", "SDD cấp", 1,
        f"{B('[SDD cấp – gầy còm]')} Tiêu chuẩn chẩn đoán SDD cấp ở trẻ {Y('6–59 tháng')} theo WHO và tiêu chí mức {Y('vừa')} / {R('nặng')}?",
        f"1) Tiêu chuẩn chẩn đoán: {R('WHZ < −2 SD')} hoặc {R('MUAC < 125 mm')} hoặc {R('phù dinh dưỡng 2 bên')}.<br>"
        f"2) {Y('Vừa')}: {Y('−3 ≤ WHZ < −2')} hoặc {Y('MUAC 115 – < 125 mm')}, {Y('không phù')}.<br>"
        f"3) {R('Nặng')}: {R('WHZ < −3')} hoặc {R('MUAC < 115 mm')} hoặc {R('phù 2 bên')}.",
        "Ba tiêu chí độc lập, chỉ cần một là đủ. Phù hai bên luôn xếp mức nặng dù WHZ và MUAC bình thường, vì phù che giấu "
        "mức hao mòn thật và có tử vong cao.",
        "4.2 Phân loại 0–59 tháng", ["SDD-cap"], asks=["Tiêu chuẩn chẩn đoán", "Vừa", "Nặng"],
    ),
    basic(
        "PED68-S4-04", "S4", "Thấp còi & nhẹ cân", 1,
        f"{B('[Thấp còi và nhẹ cân]')} Tiêu chí {B('thấp còi')} và {B('nhẹ cân')} theo WHO, mức {Y('vừa')} và {R('nặng')}?",
        f"1) {B('Thấp còi')} (stunting): {R('HAZ (LAZ) < −2 SD')}; vừa {Y('−3 đến < −2')}, nặng {R('< −3')}.<br>"
        f"2) {B('Nhẹ cân')} (underweight): {R('WAZ < −2 SD')}; vừa {Y('−3 đến < −2')}, nặng {R('< −3')}.",
        "Nhẹ cân là chỉ số dùng nhiều trong y tế công cộng nhưng lâm sàng ít giá trị: trẻ nhẹ cân có thể chỉ là thấp còi "
        "mà cân đối, hoặc gầy còm cấp — hai tình trạng cần xử trí rất khác nhau.",
        "4.2 Phân loại 0–59 tháng", ["Thap-coi"],
    ),
    basic(
        "PED68-S4-05", "S4", "Thừa cân <5 tuổi", 1,
        f"{B('[Thừa cân – béo phì dưới 5 tuổi]')} Theo WHO, ngưỡng {Y('nguy cơ thừa cân')}, {R('thừa cân')}, {R('béo phì')} "
        f"ở trẻ dưới 5 tuổi là bao nhiêu?",
        f"1) {Y('Nguy cơ thừa cân')}: WHZ (hoặc BMIz) {Y('> +1 SD')} → theo dõi, tư vấn.<br>"
        f"2) {R('Thừa cân')}: {R('> +2 SD')}.<br>"
        f"3) {R('Béo phì')}: {R('> +3 SD')}.",
        "Ngưỡng ở trẻ dưới 5 tuổi cao hơn trẻ 5–19 tuổi (+2/+3 thay vì +1/+2) vì trẻ nhỏ có tăng mỡ sinh lý và bằng chứng "
        "về hậu quả lâu dài khi chỉ ở +1 SD chưa đủ mạnh. Không dùng CN/T để chẩn đoán thừa cân.",
        "4.2 Phân loại 0–59 tháng", ["Thua-can"],
    ),
    basic(
        "PED68-S4-06", "S4", "Vòng đầu", 2,
        f"{B('[Đầu nhỏ – đầu to]')} Ngưỡng vòng đầu/tuổi xác định {R('đầu nhỏ')}, {R('đầu nhỏ nặng')} và {R('đầu to')}?",
        f"1) {R('Đầu nhỏ')}: {Y('< −2 SD')}.<br>"
        f"2) {R('Đầu nhỏ nặng')}: {Y('< −3 SD')}.<br>"
        f"3) {R('Đầu to')}: {Y('> +2 SD')}.",
        "Trước khi kết luận cần đo vòng đầu bố mẹ (đầu to gia đình lành tính rất hay gặp) và xem tốc độ: vòng đầu cắt lên "
        "nhanh qua các đường gợi ý não úng thuỷ; đầu nhỏ dần lại gợi ý tổn thương não mắc phải.",
        "4.2 Phân loại 0–59 tháng", ["Vong-dau"],
    ),
    basic(
        "PED68-S4-07", "S4", "Trẻ < 6 tháng", 1,
        f"{B('[Trẻ dưới 6 tháng – WHO 2023]')} Khái niệm mới cho trẻ dưới 6 tháng là gì, nhận diện bằng những tiêu chí nào, "
        f"và theo dõi hồi phục bằng gì?",
        f"1) Khái niệm: {B('“trẻ có nguy cơ tăng trưởng và phát triển kém”')} (thay khái niệm SDD cấp nặng hẹp).<br>"
        f"2) Tiêu chí nhân trắc: {R('MUAC < 110 mm')} ({Y('chỉ 6 tuần – < 6 tháng')}), {R('WAZ < −2')}, {R('WLZ < −2')}, "
        f"{R('chững cân / không tăng cân qua các lần khám')}, {R('phù dinh dưỡng 2 bên')}.<br>"
        f"3) Tiêu chí kèm theo: {R('bú mẹ không hiệu quả')}, {R('nhẹ cân lúc sinh / sinh non')}, yếu tố từ mẹ "
        f"({R('bệnh, trầm cảm, hoàn cảnh')}).<br>"
        f"4) Theo dõi: {G('tốc độ tăng cân')} và tình trạng lâm sàng — {R('không dùng MUAC')} để theo dõi hồi phục.",
        "Ở nhũ nhi nhỏ, vấn đề thường nằm ở cặp mẹ – con (bú, sức khoẻ tâm thần của mẹ) chứ không chỉ ở trẻ, nên WHO 2023 "
        "chuyển từ chẩn đoán “SDD” sang đánh giá nguy cơ toàn diện. MUAC thay đổi chậm nên không nhạy để theo dõi đáp ứng.",
        "4.2 Trẻ dưới 6 tháng (WHO 2023)", ["Duoi-6-thang"], asks=["Khái niệm", "Tiêu chí", "Theo dõi"],
    ),
    cloze(
        "PED68-S4-C1", "S4", "MUAC",
        f"Trẻ 6–59 tháng: MUAC {{{{c1::{Y('< 115 mm')}}}}} là SDD cấp nặng; MUAC {{{{c2::{Y('115 – < 125 mm')}}}}} là SDD cấp vừa.",
        "4.2 Phân loại 0–59 tháng", ["SDD-cap"],
    ),
    cloze(
        "PED68-S4-C2", "S4", "Trẻ < 6 tháng",
        f"WHO 2023: trẻ từ 6 tuần đến dưới 6 tháng có MUAC {{{{c1::{Y('< 110 mm')}}}}} được xếp vào nhóm nguy cơ tăng trưởng và phát triển kém.",
        "4.2 Trẻ dưới 6 tháng (WHO 2023)", ["Duoi-6-thang"],
    ),

    # ------------------------------------------------------------ S5. 5–19 tuổi & AAP
    basic(
        "PED68-S5-01", "S5", "BMI 5–19 tuổi", 1,
        f"{B('[Trẻ 5–19 tuổi – WHO 2007]')} Phân loại theo {B('BMI/tuổi')} ở các ngưỡng {Y('< −3')}, {Y('< −2')}, {Y('> +1')}, {Y('> +2')} SD; "
        f"thừa cân và béo phì tương đương BMI người lớn bao nhiêu ở tuổi 19?",
        f"1) {Y('< −3 SD')}: {R('gầy nặng')}.<br>"
        f"2) {Y('< −2 SD')}: {R('gầy')}.<br>"
        f"3) {Y('> +1 SD')}: {R('thừa cân')} (≈ {Y('BMI 25')} ở tuổi 19).<br>"
        f"4) {Y('> +2 SD')}: {R('béo phì')} (≈ {Y('BMI 30')} ở tuổi 19).",
        "WHO dựng đường cong sao cho +1 SD và +2 SD nối liền với ngưỡng BMI 25 và 30 của người lớn ở tuổi 19 — giúp phân loại "
        "liên tục từ trẻ sang người lớn.",
        "4.3 Trẻ 5–19 tuổi", ["BMI"],
    ),
    basic(
        "PED68-S5-02", "S5", "Chiều cao 5–19 tuổi", 2,
        f"{B('[CC/tuổi 5–19 tuổi]')} Phân loại chiều cao/tuổi ở trẻ 5–19 tuổi: ngưỡng {R('thấp còi')}, {R('thấp còi nặng')}, "
        f"và ý nghĩa của {Y('CC/tuổi > +2 SD')}?",
        f"1) {R('Thấp còi')}: {Y('< −2 SD')}.<br>"
        f"2) {R('Thấp còi nặng')}: {Y('< −3 SD')}.<br>"
        f"3) {Y('> +2 SD')}: {G('thường bình thường')} (bố mẹ cao); cân nhắc nguyên nhân nếu kèm {R('dậy thì sớm')}, "
        f"{R('dị hình')}, {R('tốc độ cao tăng bất thường')}.",
        "Trẻ cao hiếm khi là bệnh; nhưng trẻ cao vọt lên khỏi kênh cũ kèm dậy thì sớm (tuổi xương nhanh) thực ra sẽ thấp khi "
        "trưởng thành vì sụn tiếp hợp đóng sớm. Dị hình gợi ý Marfan, Klinefelter, Sotos.",
        "4.3 Trẻ 5–19 tuổi", ["Chieu-cao"],
    ),
    basic(
        "PED68-S5-03", "S5", "AAP 2023", 1,
        f"{B('[AAP 2023 – biểu đồ CDC]')} Phân loại {R('thừa cân')}, {R('béo phì')}, {R('béo phì nặng độ 2')}, {R('độ 3')} ở trẻ 2–19 tuổi "
        f"theo AAP 2023, và vì sao dùng {Y('%BMIp95')}?",
        f"1) {R('Thừa cân')}: BMI bách phân vị {Y('85 – < 95')}.<br>"
        f"2) {R('Béo phì')}: {Y('≥ 95')}.<br>"
        f"3) {R('Béo phì nặng độ 2')}: {Y('≥ 120% của bách phân vị 95')} (hoặc {Y('BMI ≥ 35')}).<br>"
        f"4) {R('Độ 3')}: {Y('≥ 140%')} (hoặc {Y('BMI ≥ 40')}).<br>"
        f"5) Lý do dùng %BMIp95: {G('Z-score / bách phân vị bị nén ở vùng cực trị')} → không theo dõi được trẻ béo phì nặng.",
        "Ở vùng trên bách phân vị 97, Z-score gần như không đổi dù BMI tăng thêm nhiều; %BMIp95 là thang tuyến tính nên thấy "
        "rõ trẻ nặng lên hay cải thiện. Ở Việt Nam, đánh giá thường quy vẫn theo WHO Z-score.",
        "4.3 AAP 2023", ["Beo-phi"],
    ),
    cloze(
        "PED68-S5-C1", "S5", "AAP 2023",
        f"Theo AAP 2023, béo phì nặng độ 2 là BMI {{{{c1::{Y('≥ 120% của bách phân vị 95')}}}}}; độ 3 là "
        f"{{{{c2::{Y('≥ 140% của bách phân vị 95')}}}}}.",
        "4.3 AAP 2023", ["Beo-phi"],
    ),

    # ------------------------------------------------------------ S6. Diễn giải động, tiềm năng di truyền, nguyên nhân, dậy thì
    basic(
        "PED68-S6-01", "S6", "Đường tăng trưởng", 1,
        f"{B('[Chững tăng trưởng]')} Thế nào là {R('chững tăng trưởng (growth faltering)')} trên biểu đồ, và có cần chờ Z-score < −2 "
        f"mới đánh giá không?",
        f"1) Trẻ khoẻ thường {G('đi song song một kênh')} bách phân vị / Z-score.<br>"
        f"2) {R('Chững tăng trưởng')}: đường {R('đi ngang')}, hoặc {R('cắt xuống ≥ 2 đường bách phân vị chính')} (vd 50 → 9).<br>"
        f"3) {R('Không chờ')}: cần đánh giá {R('ngay cả khi Z-score vẫn > −2')}.",
        "Trẻ từ bách phân vị 75 tụt xuống 10 vẫn “bình thường” nếu chỉ nhìn một lần đo, nhưng đã mất rất nhiều so với tiềm "
        "năng của chính nó. Phát hiện theo xu hướng giúp can thiệp trước khi thành SDD.",
        "4.4 Diễn giải động", ["Duong-tang-truong"],
    ),
    basic(
        "PED68-S6-02", "S6", "Đường tăng trưởng", 2,
        f"{B('[Chuyển kênh sinh lý]')} Những tình huống nào trẻ có thể “chuyển kênh” trên biểu đồ mà vẫn là sinh lý?",
        f"1) Trong {Y('2–3 năm đầu')}: chuyển kênh lên/xuống về {G('kênh di truyền')} ({B('canalization')}) — nhất là trẻ "
        f"{Y('to / nhỏ lúc sinh')}; sau đó tốc độ ổn định và trẻ khoẻ mạnh.<br>"
        f"2) {B('Dậy thì sớm / muộn')}: làm lệch kênh tạm thời.",
        "Cân nặng lúc sinh phản ánh môi trường tử cung nhiều hơn gen; sau sinh trẻ dần tìm về kênh của bố mẹ. Chìa khoá phân "
        "biệt với bệnh lý: sau khi chuyển kênh, trẻ đi ổn định theo kênh mới và hoàn toàn khoẻ mạnh.",
        "4.4 Diễn giải động", ["Duong-tang-truong"],
    ),
    basic(
        "PED68-S6-03", "S6", "Tốc độ tăng trưởng", 1,
        f"{B('[Tốc độ tăng chiều cao]')} Tốc độ tăng chiều cao phải tính trên khoảng thời gian bao lâu, so với gì, "
        f"và ngưỡng thực hành nào đáng lưu ý ở trẻ trước dậy thì?",
        f"1) Khoảng tính: {Y('≥ 6 tháng')} (lý tưởng {Y('12 tháng')}) — khoảng ngắn hơn thì {R('sai số đo lấn át')}.<br>"
        f"2) So với {G('chuẩn tốc độ theo tuổi – giới')}.<br>"
        f"3) Ngưỡng thực hành: trẻ từ khoảng {Y('3–4 tuổi')} đến trước dậy thì tăng {R('< 4–5 cm/năm kéo dài')} là đáng lưu ý.",
        "Sai số mỗi lần đo cỡ vài mm; nếu hai lần đo cách nhau chỉ 2 tháng (trẻ lớn khoảng 1 cm) thì sai số chiếm phần lớn "
        "chênh lệch đo được. Tốc độ thấp kéo dài là dấu hiệu nhạy của bệnh nội tiết, kể cả khi chiều cao còn trong giới hạn.",
        "4.4 Diễn giải động", ["Toc-do"], warn=True,
    ),
    basic(
        "PED68-S6-04", "S6", "Chiều cao đích", 1,
        f"{B('[Chiều cao đích – MPH]')} Viết công thức chiều cao đích (mid-parental height), khoảng đích, và cách dùng để phát hiện "
        f"bất thường.",
        f"1) {G('MPH')} = (chiều cao bố + chiều cao mẹ {Y('± 13 cm')}) / 2 — {Y('+13')} cho trai, {Y('−13')} cho gái.<br>"
        f"2) Khoảng đích ≈ {G('MPH ± 8,5 cm')} (≈ ± 2 SD).<br>"
        f"3) HAZ của trẻ thấp hơn rõ rệt so với Z-score của MPH ({R('chênh > ~2 SD')}) là {R('bất thường')} dù bản thân HAZ chưa < −2.",
        "13 cm là chênh lệch chiều cao trung bình giữa nam và nữ trưởng thành. Ví dụ bố 168, mẹ 155: con trai "
        "(168 + 155 + 13)/2 = 168 cm (159,5–176,5); con gái (168 + 155 − 13)/2 = 155 cm (146,5–163,5). "
        "Trẻ có bố mẹ cao mà nằm ở −1,8 SD vẫn phải tìm nguyên nhân.",
        "4.5 Tiềm năng di truyền", ["MPH"],
    ),
    basic(
        "PED68-S6-05", "S6", "Kiểu hình", 1,
        f"{B('[Cân trước hay cao trước]')} Phân biệt kiểu {R('cân nặng giảm trước')} với kiểu {R('chiều cao giảm trước')}: "
        f"mỗi kiểu gợi ý nhóm nguyên nhân nào?",
        f"1) {R('Cân nặng giảm trước, chiều cao giảm sau')}; {Y('WHZ / BMI thấp')} → {B('thiếu năng lượng')}: ăn không đủ, "
        f"kém hấp thu, bệnh mạn tiêu hao, tâm lý xã hội.<br>"
        f"2) {R('Chiều cao giảm trước, cân nặng giữ hoặc tăng')}; {Y('BMI bình thường / cao')} → {B('nội tiết')}: "
        f"{B('suy giáp')}, {B('thiếu GH')}, {B('thừa glucocorticoid')} (Cushing, corticoid ngoại sinh).",
        "Khi thiếu năng lượng, cơ thể hy sinh cân nặng trước rồi mới ngừng lớn chiều cao. Ngược lại, hormon chi phối sụn "
        "tăng trưởng (GH, thyroxin) giảm hoặc cortisol thừa làm ngừng lớn chiều cao trước, còn mỡ vẫn tích luỹ → trẻ “thấp mũm mĩm”.",
        "4.6 Kiểu hình – nguyên nhân", ["Kieu-hinh"],
    ),
    basic(
        "PED68-S6-06", "S6", "Kiểu hình", 1,
        f"{B('[CDGP và thấp gia đình]')} Phân biệt {B('chậm tăng trưởng – dậy thì thể tạng (CDGP)')} với {B('thấp do gia đình')} "
        f"dựa vào tốc độ, tuổi xương và tiền sử gia đình.",
        f"1) {B('CDGP')}: thấp, {G('tốc độ bình thường')}, {R('tuổi xương chậm')}, {Y('gia đình dậy thì muộn')}.<br>"
        f"2) {B('Thấp gia đình')}: thấp, {G('tốc độ bình thường')}, {Y('tuổi xương ≈ tuổi thực')}, {Y('phù hợp MPH thấp')}.",
        "Cả hai đều là biến thể bình thường. Tuổi xương chậm nghĩa là còn nhiều thời gian lớn → trẻ CDGP thường đạt chiều cao "
        "trưởng thành trong khoảng đích, chỉ muộn hơn bạn bè. Trẻ thấp gia đình lớn đúng hạn nhưng đích vốn thấp.",
        "4.6 Kiểu hình – nguyên nhân", ["Kieu-hinh", "Thap"],
    ),
    basic(
        "PED68-S6-07", "S6", "Kiểu hình", 2,
        f"{B('[Kiểu hình đặc biệt]')} Gợi ý nguyên nhân của: {R('thấp không cân đối')}, {R('trẻ gái thấp không giải thích được')}, "
        f"{R('cao / BMI cao kèm dậy thì sớm')}.",
        f"1) {R('Thấp không cân đối')} (tỷ lệ đoạn / sải tay bất thường) → {B('loạn sản xương')}: {B('SHOX')}, "
        f"{B('achondroplasia / hypochondroplasia')}.<br>"
        f"2) {R('Trẻ gái thấp không giải thích được')} → {B('hội chứng Turner')}: {G('làm karyotype')} dù không có dị hình rõ.<br>"
        f"3) {R('Cao / BMI cao + dậy thì sớm')} → {B('dậy thì sớm')} (tăng tốc độ cao + tuổi xương nhanh).",
        "Turner có thể chỉ biểu hiện bằng thấp đơn độc trước tuổi dậy thì — guideline Turner khuyến cáo làm karyotype cho mọi "
        "trẻ gái thấp chưa rõ nguyên nhân để không bỏ sót suy buồng trứng và dị tật tim, thận đi kèm.",
        "4.6 Kiểu hình – nguyên nhân", ["Kieu-hinh"],
    ),
    basic(
        "PED68-S6-08", "S6", "Dậy thì", 1,
        f"{B('[Dậy thì sớm, muộn và tuổi xương]')} Ngưỡng tuổi {R('dậy thì sớm')} và {R('dậy thì muộn')} ở trẻ gái, trẻ trai? "
        f"Chụp {G('tuổi xương')} thế nào và khi nào?",
        f"1) {R('Dậy thì sớm')}: dấu hiệu dậy thì trước {Y('8 tuổi ở nữ')} (vú B2), trước {Y('9 tuổi ở nam')} (tinh hoàn ≥ 4 ml).<br>"
        f"2) {R('Dậy thì muộn')}: chưa có vú ở nữ {Y('13 tuổi')}; tinh hoàn {Y('< 4 ml')} ở nam {Y('14 tuổi')}.<br>"
        f"3) {G('Tuổi xương')}: X-quang {G('bàn tay – cổ tay trái')}, đọc theo {G('Greulich–Pyle hoặc TW3')}; chụp khi "
        f"{R('thấp')}, {R('cao bất thường')}, {R('dậy thì sớm / muộn')} — để đánh giá {Y('tiềm năng tăng trưởng còn lại')}.",
        "Mốc 8/9 và 13/14 tuổi tương ứng khoảng 2–2,5 SD sớm hơn / muộn hơn tuổi khởi phát dậy thì trung bình. Tuổi xương là “đồng hồ sinh học”: "
        "chênh giữa tuổi xương và tuổi thực cho biết trẻ còn lớn được bao lâu.",
        "4.7 Dậy thì", ["Day-thi"],
    ),
    cloze(
        "PED68-S6-C1", "S6", "Chiều cao đích",
        f"Chiều cao đích = (bố + mẹ {{{{c1::{Y('+ 13 cm')}}}}}) / 2 cho trẻ trai; khoảng đích ≈ MPH {{{{c2::{Y('± 8,5 cm')}}}}}.",
        "4.5 Tiềm năng di truyền", ["MPH"],
    ),
    cloze(
        "PED68-S6-C2", "S6", "Đường tăng trưởng",
        f"Chững tăng trưởng khi đường tăng trưởng cắt xuống {{{{c1::{Y('≥ 2 đường bách phân vị chính')}}}}} — đánh giá ngay cả khi Z-score còn > −2.",
        "4.4 Diễn giải động", ["Duong-tang-truong"],
    ),
    cloze(
        "PED68-S6-C3", "S6", "Tốc độ",
        f"Tốc độ tăng chiều cao phải tính trên khoảng thời gian ít nhất {{{{c1::{Y('6 tháng')}}}}}, lý tưởng "
        f"{{{{c2::{Y('12 tháng')}}}}}.",
        "4.4 Diễn giải động", ["Toc-do"],
    ),

    # ------------------------------------------------------------ S7. Chuyển khám, bệnh án, cách cũ cần bỏ
    basic(
        "PED68-S7-01", "S7", "Chuyển khám", 1,
        f"{B('[SDD cấp nặng]')} Trẻ {R('SDD cấp nặng')} nào cần điều trị nội trú, và khi nhập viện phải đánh giá ngay những gì?",
        f"1) Nội trú: SDD cấp nặng ({R('WHZ < −3')}, {R('MUAC < 115 mm')}, {R('phù 2 bên')}) nhất là khi "
        f"{R('có biến chứng')}, {R('không đạt thử nghiệm thèm ăn')}, hoặc trẻ {Y('dưới 6 tháng')}.<br>"
        f"2) Đánh giá ngay: {R('nhiễm trùng')}, {R('hạ đường huyết')}, {R('hạ thân nhiệt')}, {R('mất nước')}; "
        f"điều trị theo {G('phác đồ WHO / Bộ Y tế')}.",
        "Trẻ SDD nặng giảm đáp ứng viêm: nhiễm trùng nặng có thể không sốt, hạ đường huyết và hạ thân nhiệt hay gặp về đêm. "
        "Thử nghiệm thèm ăn (ăn thử chế phẩm điều trị) phân luồng trẻ đủ điều kiện điều trị ngoại trú.",
        "5. Chuyển khám", ["Chuyen-kham", "SDD-cap"],
    ),
    basic(
        "PED68-S7-02", "S7", "Chuyển khám", 1,
        f"{B('[Thăm dò trẻ thấp]')} Khi nào trẻ thấp cần thăm dò nguyên nhân, và gồm những xét nghiệm nào?",
        f"1) Khi nào: {R('HAZ < −3 SD')}, hoặc {R('HAZ < −2 SD kèm tốc độ tăng chiều cao thấp')}.<br>"
        f"2) Xét nghiệm: {G('CTM')}, {G('sinh hoá')}, {G('TSH / FT4')}, {G('IGF-1')}, {G('sàng lọc celiac')}, "
        f"{G('tổng phân tích nước tiểu')}, {G('tuổi xương')}; {G('karyotype ở nữ')}.",
        "Bộ xét nghiệm ban đầu nhằm loại trừ các bệnh “thầm lặng” chỉ biểu hiện bằng chậm lớn: thiếu máu, bệnh thận, nhiễm toan "
        "ống thận, suy giáp, celiac, Turner. IGF-1 thấp gợi ý thiếu GH nhưng cũng thấp khi SDD.",
        "5. Chuyển khám", ["Chuyen-kham", "Thap"], asks=["Khi nào", "Xét nghiệm"],
    ),
    basic(
        "PED68-S7-03", "S7", "Chuyển khám", 1,
        f"{B('[Dấu hiệu chuyển khám – tăng trưởng]')} Kể các dấu hiệu về đường tăng trưởng, chiều cao đích, tỷ lệ cơ thể và vòng đầu "
        f"cần chuyển chuyên khoa / thăm dò thêm.",
        f"1) {R('Cắt ≥ 2 đường bách phân vị')} (ngoài giai đoạn chuyển kênh sinh lý) → tìm nguyên nhân bệnh lý / dinh dưỡng / "
        f"tâm lý xã hội.<br>"
        f"2) {R('Chênh với chiều cao đích > ~2 SD')} → đánh giá {G('nội tiết – di truyền')}.<br>"
        f"3) {R('Thấp không cân đối, dị hình')} → {G('di truyền / chỉnh hình')}.<br>"
        f"4) {R('Vòng đầu < −2 SD hoặc > +2 SD')}, hoặc tăng/giảm tốc độ bất thường → {G('thần kinh nhi')}; "
        f"{G('siêu âm qua thóp / chẩn đoán hình ảnh')}, đánh giá phát triển.",
        "Nhóm dấu hiệu này đều nói về “hướng đi” và “so với chính trẻ / gia đình trẻ”, không phụ thuộc trẻ đã dưới ngưỡng "
        "−2 SD hay chưa.",
        "5. Chuyển khám", ["Chuyen-kham"],
    ),
    basic(
        "PED68-S7-04", "S7", "Chuyển khám", 2,
        f"{B('[Dấu hiệu chuyển khám – béo phì và dậy thì]')} Xử trí khi gặp {R('béo phì kèm thấp / giảm tốc độ cao')}, "
        f"{R('béo phì nặng hoặc có bệnh đi kèm')}, {R('dậy thì sớm / muộn')}?",
        f"1) {R('Béo phì kèm thấp hoặc giảm tốc độ cao')} → {G('loại trừ nguyên nhân nội tiết / di truyền')} "
        f"(béo phì đơn thuần thường {Y('cao hơn so với tuổi')}).<br>"
        f"2) {R('Béo phì nặng / có bệnh đi kèm')} → {G('đánh giá biến chứng')}: huyết áp, lipid, glucose / HbA1c, men gan, "
        f"ngưng thở khi ngủ; can thiệp tích cực theo {G('AAP 2023')}.<br>"
        f"3) {R('Dậy thì sớm / muộn')} → {G('nội tiết nhi')}.",
        "Trẻ béo phì do ăn nhiều thường cao hơn bạn (dư năng lượng thúc đẩy tăng trưởng và dậy thì sớm). Béo phì mà lại thấp "
        "là “cờ đỏ” của suy giáp, Cushing, thiếu GH hoặc hội chứng di truyền (Prader–Willi).",
        "5. Chuyển khám", ["Chuyen-kham", "Beo-phi"],
    ),
    basic(
        "PED68-S7-05", "S7", "Bệnh án", 2,
        f"{B('[Mẫu bệnh án]')} Phần phát triển thể chất trong bệnh án cần ghi những mục nào?",
        f"1) {Y('Tuổi')} (tuổi hiệu chỉnh nếu sinh non), {Y('giới')}.<br>"
        f"2) {B('CN')} (WAZ), {B('CD/CC')} + {G('tư thế đo')} (HAZ), {B('WHZ')}, {B('BMI')} (BMIz).<br>"
        f"3) {B('Vòng đầu')} (HCZ), {B('MUAC')}, {R('phù dinh dưỡng')} (không / +, ++, +++).<br>"
        f"4) {G('Xu hướng')}: theo kênh / cắt mấy đường từ tháng nào; tốc độ CC (cm/năm, khoảng đo).<br>"
        f"5) {G('Chiều cao đích')} và khoảng; trẻ trong / ngoài khoảng đích.<br>"
        f"6) {B('Tanner')}, {B('tuổi xương')} (nếu có).<br>"
        f"7) {G('Kết luận')}: theo chuẩn WHO 2006/2007 — bình thường / SDD cấp mức … / thấp còi mức … / thừa cân / béo phì, "
        f"xu hướng, nghi nguyên nhân.",
        "Ghi Z-score cạnh mỗi số đo và nêu tên chuẩn đã dùng giúp người đọc sau kiểm tra lại được; kết luận phải có đủ "
        "3 tầng: phân loại hiện tại, xu hướng, nghi nguyên nhân.",
        "6. Mẫu bệnh án", ["Benh-an"],
    ),
    basic(
        "PED68-S7-06", "S7", "Cách cũ cần bỏ", 1,
        f"{B('[Cách cũ cần bỏ]')} Kể 6 cách đánh giá tăng trưởng “cũ” và cách làm tương ứng theo EBM hiện nay.",
        f"1) {R('Công thức ước tính CN, CC theo tuổi')} để kết luận → chỉ ước lượng nhanh (vd tính liều cấp cứu khi không cân được); "
        f"{G('chẩn đoán dùng Z-score')}.<br>"
        f"2) {R('Phân loại SDD theo % cân nặng chuẩn (Gomez, Waterlow)')} → {G('Z-score WHO + MUAC + phù')}.<br>"
        f"3) {R('Đánh giá một lần đo')} → {G('đường tăng trưởng, tốc độ, chiều cao đích')}.<br>"
        f"4) {R('Mốc thóp, mọc răng, vòng ngực/vòng đầu')} để đánh giá tăng trưởng → {Y('biên độ bình thường rất rộng')}, "
        f"chỉ có giá trị khi kèm bất thường khác.<br>"
        f"5) {R('Không hiệu chỉnh tuổi trẻ sinh non')} → {G('tuổi hiệu chỉnh đến ≥ 24 tháng')}; INTERGROWTH-21st đến 64 tuần PMA.<br>"
        f"6) {R('Đo chiều dài trẻ nhỏ bằng thước dây trên giường')} → {G('thước đo chiều dài chuẩn, 2 người đo')}.",
        "Gomez/Waterlow dùng % so với trung vị nên không so sánh được giữa các tuổi và không chuẩn hoá theo độ phân tán; "
        "Z-score khắc phục cả hai. Khi đi thi, kiểm tra barem trường vì nhiều tài liệu cũ vẫn dạy công thức ước tính.",
        "7. Cách cũ cần bỏ", ["Cach-cu"],
    ),

    # ------------------------------------------------------------ ⚡ Thuật toán quyết định
    algo(
        "PED68-A-01", "S4", "Giải mã Z-score",
        "Giải mã nhanh Z-score trẻ 0–59 tháng",
        f"1) {R('Phù 2 bên')} hoặc {R('WHZ < −3')} hoặc {R('MUAC < 115 mm')} → {R('SDD cấp nặng')}.<br>"
        f"2) {Y('−3 ≤ WHZ < −2')} hoặc {Y('MUAC 115 – < 125 mm')}, không phù → {B('SDD cấp vừa')}.<br>"
        f"3) {R('HAZ < −2')} → {B('thấp còi')} ({R('< −3')}: nặng) — đánh giá độc lập với WHZ.<br>"
        f"4) {Y('WHZ > +1')} nguy cơ thừa cân; {R('> +2')} thừa cân; {R('> +3')} béo phì.<br>"
        f"5) Dưới 6 tháng: {R('MUAC < 110 mm')} (từ 6 tuần), WAZ/WLZ < −2, chững cân → {B('nguy cơ tăng trưởng – phát triển kém')}.",
        "Thứ tự đọc: phù trước (vì phù làm sai cân nặng) → WHZ/MUAC (cấp) → HAZ (mạn) → phía trên (thừa cân). "
        "Một trẻ có thể vừa SDD cấp vừa thấp còi — ghi cả hai.",
        "4.2 Phân loại", ["Phan-loai"],
    ),
    algo(
        "PED68-A-02", "S1", "Chọn chuẩn và tuổi",
        "Chọn chuẩn tham chiếu và tuổi để tra",
        f"1) Trẻ {Y('sinh non')}? → {B('INTERGROWTH-21st')} theo {Y('PMA')} đến {Y('64 tuần')} → chuyển {B('WHO')} theo "
        f"{Y('tuổi hiệu chỉnh')} đến {Y('≥ 24 tháng')}.<br>"
        f"2) {Y('0–5 tuổi')} → {B('WHO 2006')}: dưới 2 tuổi {G('đo nằm')}, từ 2 tuổi {G('đo đứng')} (sai tư thế → ± 0,7 cm).<br>"
        f"3) {Y('5–19 tuổi')} → {B('WHO 2007')}: {B('BMI/tuổi')} + {B('CC/tuổi')}; CN/tuổi chỉ đến {Y('10 tuổi')}.<br>"
        f"4) Cần {R('phân độ béo phì nặng')} → tham khảo {B('AAP 2023 / CDC extended')} (%BMIp95), ghi rõ chuẩn.",
        "Sai chuẩn hoặc sai tuổi là lỗi nền: mọi Z-score phía sau đều sai theo. Kiểm tra hai điều này trước khi đọc số.",
        "1. Chuẩn tham chiếu", ["Chuan-tham-chieu"],
    ),
    algo(
        "PED68-A-03", "S6", "Công thức bỏ túi",
        "Công thức bỏ túi khám phát triển thể chất",
        f"1) {G('Tuổi hiệu chỉnh')} = tuổi thực − ({Y('40')} − tuổi thai lúc sinh) tuần.<br>"
        f"2) {G('MPH')} = (bố + mẹ {Y('± 13')}) / 2; khoảng đích {Y('± 8,5 cm')}.<br>"
        f"3) {G('Hiệu chỉnh tư thế')}: dưới 2 tuổi đo đứng {Y('+ 0,7 cm')}; từ 2 tuổi đo nằm {Y('− 0,7 cm')}.<br>"
        f"4) {G('BMI')} = CN (kg) / CC² (m²).<br>"
        f"5) {G('%BMIp95')} = BMI / BMI bách phân vị 95 × 100; {Y('≥ 120%')} độ 2, {Y('≥ 140%')} độ 3.<br>"
        f"6) {G('Tốc độ CC')} = chênh chiều cao / khoảng thời gian (năm), khoảng {Y('≥ 6 tháng')}.",
        "Mốc Z-score ↔ bách phân vị: −2 SD ≈ 2,3; −1 SD ≈ 15,9; +1 SD ≈ 84,1; +2 SD ≈ 97,7.",
        "Tổng hợp công thức", ["Cong-thuc"],
    ),
    algo(
        "PED68-A-04", "S6", "Lưu đồ trẻ thấp",
        "Trẻ thấp: lưu đồ tiếp cận 5 bước",
        f"1) {G('Đo lại đúng kỹ thuật')}, đúng tư thế, đúng tuổi (hiệu chỉnh nếu sinh non).<br>"
        f"2) {G('Xem tỷ lệ cơ thể')}: {R('không cân đối')} → {B('loạn sản xương')} (SHOX, achondroplasia).<br>"
        f"3) {G('Cân nặng so với chiều cao')}: {R('gầy trước')} → {B('dinh dưỡng / bệnh mạn')}; {R('thấp mà mũm mĩm')} → {B('nội tiết')}.<br>"
        f"4) {G('Tốc độ + tuổi xương + MPH')}: tốc độ bình thường + tuổi xương chậm → {B('CDGP')}; tốc độ bình thường + tuổi xương "
        f"≈ tuổi thực + MPH thấp → {B('thấp gia đình')}.<br>"
        f"5) {R('HAZ < −3')}, {R('tốc độ thấp')}, {R('chênh MPH > ~2 SD')}, {R('trẻ gái chưa rõ nguyên nhân')} → "
        f"{G('thăm dò')} (CTM, sinh hoá, TSH/FT4, IGF-1, celiac, nước tiểu, tuổi xương, karyotype nữ).",
        "Mục tiêu: không làm xét nghiệm tràn lan cho trẻ thấp sinh lý (CDGP, gia đình), và không bỏ sót trẻ có tốc độ thấp "
        "kéo dài hoặc trẻ gái Turner.",
        "4.6 + 5 Tổng hợp", ["Thap", "Tiep-can"],
    ),
    algo(
        "PED68-A-05", "S3", "Đo nhân trắc",
        "Đo nhân trắc: 3 NÊN & 3 KHÔNG",
        f"1) {G('NÊN')}: {G('đo 2 lần')}, ghi trung bình, ghi {Y('ngày + tư thế')}.<br>"
        f"2) {G('NÊN')}: trẻ dưới 2 tuổi đo nằm bằng {G('thước đo chiều dài, 2 người')}.<br>"
        f"3) {G('NÊN')}: khám {G('phù 2 mu bàn chân')} trước khi diễn giải cân nặng.<br>"
        f"4) {R('KHÔNG')}: đo chiều dài bằng {R('thước dây trên giường')}.<br>"
        f"5) {R('KHÔNG')}: đo {R('MUAC ở trẻ dưới 6 tuần')} hoặc {R('quấn thước ép lõm da')}.<br>"
        f"6) {R('KHÔNG')}: kết luận khi gặp {R('Z-score cờ')} (HAZ ±6, WHZ ±5, WAZ −6/+5) hay {R('chiều cao “giảm”')} — đo lại trước.",
        "Phần lớn “bất thường” trên biểu đồ ở phòng khám là lỗi đo hoặc nhập liệu. Ba KHÔNG ở trên chặn ba nguồn sai số hay gặp nhất.",
        "3. Đo nhân trắc", ["Ky-thuat-do"],
    ),
]
