# -*- coding: utf-8 -*-
"""SURG-21: Ung thư dạ dày — nguồn thẻ duy nhất xây dựng hoàn toàn từ barem ôn thi.
Nguồn barem: C:\\Users\\THANHANH\\Desktop\\barem\\02_Ung_thu_da_day_barem.md (tr. 14–25).
Mã barem từng dòng lưu trong SURG-21_Ung_thu_da_day_BAREM.md ([B0.01]..[B7.05]).
"""


def _c(color: str, text: str) -> str:
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t: str) -> str:  # cờ đỏ / triệu chứng / biến chứng / chống chỉ định
    return _c("#ff6b6b", t)


def Y(t: str) -> str:  # con số / ngưỡng / tỷ lệ / mốc thời gian
    return _c("#ffd43b", t)


def G(t: str) -> str:  # xử trí / chẩn đoán vàng / phẫu thuật / phòng bệnh
    return _c("#51cf66", t)


def B(t: str) -> str:  # thực thể / giải phẫu / phân loại / giai đoạn
    return _c("#74c0fc", t)


def clz(n: int, inner: str) -> str:
    return f"{{{{c{n}::{inner}}}}}"


BADGE = ("🏛️ BAREM ÔN THI · UNG THƯ DẠ DÀY", "badge-barem")
SRC = "📖 Nguồn: Barem Ôn thi Ung thư dạ dày — Bộ môn Ngoại / Ung bướu (tr. 14–25). Barem: "


def basic(cid, section, category, tier, front, core, ai, barem, tags, asks=None):
    card = {
        "id": cid,
        "track": "barem_goc",
        "badge": BADGE[0],
        "badge_class": BADGE[1],
        "type": "basic",
        "section": section,
        "category": category,
        "tier": tier,
        "front": front,
        "back": f"<b>🎯 Trả lời cốt lõi:</b><br>{core}<br><br><b>💡 Giải thích của AI:</b><br>{ai}",
        "extra": SRC + barem,
        "tags": ["SURG-21", "Ung-thu-da-day", "Barem-goc", section] + tags,
    }
    if asks:
        card["asks"] = asks
    return card


def algo(cid, section, category, title, core, ai, barem, tags):
    card = basic(
        cid, section, category, 1,
        f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {B(title)}",
        core, ai, barem, tags + ["Thuat-toan"],
    )
    card.pop("badge")
    card.pop("badge_class")
    return card


def trap(cid, section, category, title, core, ai, barem, tags, red_flag=False, asks=None):
    prefix = f"🛑 <b>CỜ ĐỎ TUYỆT ĐỐI:</b> {R(title)}" if red_flag else f"❌ <b>Bẫy lâm sàng:</b> {R(title)}"
    return basic(cid, section, category, 2, prefix, core, ai, barem, tags + ["Bay-lam-sang" if not red_flag else "Co-do"], asks=asks)


def cloze(cid, section, category, text, barem, tags):
    return {
        "id": cid,
        "track": "barem_goc",
        "badge": BADGE[0],
        "badge_class": BADGE[1],
        "type": "cloze",
        "section": section,
        "category": category,
        "tier": 2,
        "text": text,
        "extra": SRC + barem,
        "tags": ["SURG-21", "Ung-thu-da-day", "Barem-goc", "Cloze-phu", section] + tags,
    }


cards_data = [
    # ============================================================
    # B0. MỤC TIÊU HỌC TẬP
    # ============================================================
    basic(
        "SURG21-B0-01", "B0", "Mục tiêu học tập", 1,
        f"{B('[Ung thư dạ dày]')} Nêu {Y('5 mục tiêu học tập')} cốt lõi của bài theo barem?",
        f"1) Nêu được {B('dịch tễ học, nguyên nhân và tổn thương giải phẫu bệnh')} của ung thư dạ dày.<br>"
        f"2) Trình bày được {R('triệu chứng lâm sàng')} của ung thư dạ dày.<br>"
        f"3) Nêu được giá trị của {G('nội soi dạ dày')} trong chẩn đoán ung thư dạ dày.<br>"
        f"4) {G('Chẩn đoán')} được ung thư dạ dày thể điển hình.<br>"
        f"5) Trình bày được các {G('phương pháp điều trị')} ung thư dạ dày.",
        "Năm mục tiêu định hướng toàn bộ trọng tâm thi cử: trục nền (dịch tễ, yếu tố nguy cơ, GPB) → phát hiện sớm bằng nội soi sinh thiết → chẩn đoán thể điển hình và chọn chiến lược điều trị ngoại khoa + hóa trị.",
        "B0.01", ["Muc-tieu"],
    ),

    # ============================================================
    # B1. ĐẠI CƯƠNG (DỊCH TỄ & NGUYÊN NHÂN)
    # ============================================================
    basic(
        "SURG21-B1-01", "B1", "Dịch tễ thế giới", 1,
        f"{B('[Dịch tễ UT dạ dày thế giới]')} Vị thế bệnh trong nhóm UT đường tiêu hóa, vùng {R('tỷ lệ mắc cao')} vs {G('tần số thấp')}, và các con số tại {B('Nhật Bản & Mỹ')}?",
        f"1) <b>Vị thế chung:</b> Phổ biến nhất thế giới và đứng {R('hàng đầu trong các UT đường tiêu hóa')}; nguy cơ cao ở tầng lớp kinh tế xã hội thấp.<br>"
        f"2) <b>Vùng mắc cao:</b> Nhật Bản, Nam Mỹ, Tây Ban Nha, Bồ Đào Nha, Đông Âu, Trung Quốc, Đông Nam Á (xu hướng giảm đáng kể ở Nhật, Trung Quốc, Chile, Ireland). Tại {B('Nhật')}: {Y('69/100.000')}, tuổi TB {Y('55')}; Mỹ gốc da đen/da đỏ/Tây Ban Nha gấp {Y('2 lần')} Mỹ da trắng.<br>"
        f"3) <b>Vùng tần số thấp:</b> Bắc Mỹ, Trung Đông, Ấn Độ, Úc. Tại {B('Mỹ')}: nam giảm từ {Y('28 → 5/100.000')}, nữ giảm từ {Y('27 → 2,3/100.000')}, tỉ lệ nam/nữ {Y('1,7')}, tuổi TB {Y('63')}; tử vong giảm từ {Y('33/100.000')} (1930) → {Y('3,7/100.000')} (1990).",
        "Sự sụt giảm mạnh tỉ lệ mắc và tử vong tại Mỹ (từ 33 xuống 3,7/100.000) cùng sự khác biệt giữa Nhật (69/100.000) và người Nhật di cư cho thấy vai trò áp đảo của môi trường và bảo quản thực phẩm.",
        "B1.01, B1.02", ["Dai-cuong", "Dich-te"],
    ),
    basic(
        "SURG21-B1-02", "B1", "Dịch tễ tại Việt Nam", 1,
        f"{B('[Dịch tễ UT dạ dày tại Việt Nam]')} Thứ hạng ở {B('nam và nữ')}, tần suất mắc ở {B('Hà Nội & TP.HCM')}, {Y('lứa tuổi')} và tỉ lệ {B('nam/nữ')}?",
        f"1) <b>Thứ hạng tại Việt Nam:</b> Đứng {R('thứ 2 ở nam giới')} (sau UT phế quản) và {R('thứ 2 ở nữ giới')} (sau UT vú).<br>"
        f"2) <b>Hà Nội (1993–1995):</b> Nam {Y('25,7/100.000')} dân; nữ {Y('12,5/100.000')} dân.<br>"
        f"3) <b>TP. Hồ Chí Minh (1997):</b> Nam {Y('18,8/100.000')} dân; nữ {Y('7,3/100.000')} dân.<br>"
        f"4) <b>Tuổi &amp; giới thường gặp:</b> Hay gặp khoảng {Y('50–60 tuổi')}; nam nhiều hơn nữ với tỉ lệ nam/nữ là {Y('2/1')}.",
        "Tại Việt Nam, ung thư dạ dày đứng á quân ở cả hai giới với tỉ suất miền Bắc (Hà Nội 25,7) cao hơn miền Nam (TP.HCM 18,8), nam mắc gấp đôi nữ và tập trung ở độ tuổi 50–60.",
        "B1.03", ["Dai-cuong", "Viet-Nam"],
    ),
    basic(
        "SURG21-B1-03", "B1", "Nguyên nhân môi trường, ăn uống & HP", 1,
        f"{B('[Nguyên nhân UT dạ dày]')} Trình bày vai trò của {B('môi trường')}, {R('chế độ ăn uống')}, {R('Helicobacter pylori (HP)')} và {R('béo phì')}?",
        f"1) <b>Môi trường:</b> Giữ vai trò quan trọng — người Nhật di cư sang Mỹ có tỷ lệ mắc giảm thấp theo môi trường mới.<br>"
        f"2) <b>Chế độ ăn uống:</b> Thức ăn hun khói, thức ăn khô, bảo quản nhiều muối, chứa nhiều {R('Nitrosamin, Nitrates, Nitrites')} liên quan chặt UTDD; tại Việt Nam gia tăng chủ yếu do {R('hóa chất độc hại tồn dư')} trong thực phẩm hàng ngày; {G('vitamin C (cam, chanh)')} giúp trung hòa chất gây UT.<br>"
        f"3) <b>Nhiễm Helicobacter pylori (HP):</b> Khoảng {Y('70%')} dân số nhiễm HP — làm tăng nguy cơ UTDD và là {R('yếu tố hàng đầu tại Việt Nam')}.<br>"
        f"4) <b>Béo phì:</b> Làm tăng nguy cơ mắc UTDD cao gấp {Y('2 lần')}.",
        "🔄 <b>Chuỗi cơ chế:</b> Thực phẩm nhiều muối/Nitrosamin + nhiễm HP kéo dài (70% dân số) → Viêm mạn tính, teo niêm mạc → Tăng sinh chuyển sản ruột → Loạn sản → Ung thư dạ dày (vitamin C giúp ức chế tạo nitrosamin).",
        "B1.04, B1.05, B1.06, B1.07", ["Nguyen-nhan", "HP"],
    ),
    basic(
        "SURG21-B1-04", "B1", "Bệnh lý tiền ung thư, di truyền & gen", 1,
        f"{B('[Yếu tố thuận lợi UT dạ dày]')} Liệt kê {Y('5 bệnh lý dạ dày tiền ung thư')}, yếu tố {B('di truyền (nhóm máu, dòng họ)')} và {B('đột biến gen')}?",
        f"1) <b>5 bệnh lý tiền ung thư:</b> {R('Viêm teo dạ dày mạn tính')}, {R('vô toan')}, {R('thiếu máu ác tính Biermer')}, {R('u tuyến (polyp) dạ dày')}, người từng {R('phẫu thuật cắt đoạn dạ dày sau 10–15 năm')}.<br>"
        f"2) <b>Di truyền:</b> {B('Nhóm máu A')} có tỉ lệ mắc cao hơn; gia đình di truyền (Gauser thống kê dòng họ {Y('174 người có 41 người')} UTDD; gia tộc {B('Napoléon')}).<br>"
        f"3) <b>Gen:</b> Đột biến gen ức chế khối u {R('p53')}.",
        "Cắt đoạn dạ dày cũ (sau 10–15 năm) làm trào ngược dịch mật–tụy vào mỏm dạ dày gây viêm teo mạn; thiếu máu ác tính Biermer gây vô toan và viêm teo đáy vị; đột biến gen ức chế u p53 làm mất kiểm soát chu kỳ tế bào.",
        "B1.08, B1.09", ["Tien-ung-thu", "Di-truyen", "p53"],
    ),
    cloze(
        "SURG21-B1-05", "B1", "Mốc thời gian cắt đoạn dạ dày",
        f"Người từng phẫu thuật cắt đoạn dạ dày có nguy cơ tăng mắc ung thư mỏm dạ dày sau {clz(1, Y('10–15 năm'))}, trong khi nhiễm {clz(2, R('Helicobacter pylori (HP)'))} chiếm khoảng {clz(3, Y('70%'))} dân số và là yếu tố hàng đầu tại Việt Nam.",
        "B1.06, B1.08", ["Nguong-so"],
    ),
    cloze(
        "SURG21-B1-06", "B1", "Thứ hạng & lứa tuổi tại Việt Nam",
        f"Tại Việt Nam, ung thư dạ dày đứng thứ {clz(1, Y('2'))} ở nam (sau UT phế quản) và thứ {clz(2, Y('2'))} ở nữ (sau UT vú), hay gặp ở độ tuổi {clz(3, Y('50–60 tuổi'))} với tỉ lệ nam/nữ là {clz(4, Y('2/1'))}.",
        "B1.03", ["Viet-Nam", "Nguong-so"],
    ),

    # ============================================================
    # B2. GIẢI PHẪU BỆNH
    # ============================================================
    basic(
        "SURG21-B2-01", "B2", "Vị trí, đại thể & vi thể", 1,
        f"{B('[Giải phẫu bệnh UT dạ dày]')} Phân bố {Y('vị trí khối u (%)')}, {B('3 thể đại thể')} và phân loại {B('vi thể (%)')}?",
        f"1) <b>Vị trí u:</b> Hang và môn vị {Y('50–60%')} (đa số); bờ cong nhỏ {Y('25–30%')}; tâm vị {Y('< 10%')}; bờ cong lớn rất ít gặp.<br>"
        f"2) <b>3 thể đại thể:</b><br>"
        f"• {B('Thể u (thể sùi)')}: phát triển lồi vào lòng dạ dày như súp lơ.<br>"
        f"• {R('Thể loét')}: bờ nham nhở, đáy cứng, hoại tử.<br>"
        f"• {B('Thể thâm nhiễm cứng (Linitis plastica)')}: thành dạ dày dày cứng như ống cao su, mất các nếp niêm mạc.<br>"
        f"3) <b>Vi thể:</b> {B('Ung thư tuyến (Adenocarcinoma)')} tới {Y('90%')} (tuyến ống, tuyến nhú, nhầy, tế bào nhẫn); {B('ung thư tổ chức liên kết')} (Sarcoma, Lymphoma...) khoảng {Y('10%')}.",
        "U tập trung đa số ở vùng hang-môn vị (50–60%) nên dễ sớm gây hội chứng hẹp môn vị; thể Linitis plastica thâm nhiễm cứng dưới niêm mạc làm dạ dày co nhỏ mất nhu động rất dễ bị bỏ sót nếu sinh thiết nông.",
        "B2.01, B2.02, B2.07", ["Giai-phau-benh", "Dai-the", "Vi-the"],
    ),
    basic(
        "SURG21-B2-02", "B2", "TNM — T và N trong UT dạ dày", 1,
        f"{B('[TNM UT dạ dày — T và N]')} Định nghĩa chi tiết mức độ xâm lấn {B('Tx → T4')} và phân loại hạch vùng {B('N0 → N3')} theo barem?",
        f"1) <b>T (Khối u nguyên phát):</b> {B('Tx')} không đánh giá được; {B('T0')} không có u; {B('Tis')} tại chỗ (niêm mạc, chưa tới màng đáy/dưới niêm mạc); {B('T1')} niêm mạc và dưới niêm mạc; {B('T2')} lớp cơ; {B('T3')} lan tới thanh mạc; {R('T4')} xuyên thanh mạc vào cấu trúc lân cận.<br>"
        f"2) <b>N (Hạch vùng):</b><br>"
        f"• {B('N0')}: không di căn hạch vùng.<br>"
        f"• {B('N1')}: di căn hạch cạnh dạ dày {Y('cách u ≤ 3 cm')} dọc bờ cong nhỏ và bờ cong lớn.<br>"
        f"• {B('N2')}: di căn hạch vùng {Y('vượt quá u > 3 cm')}, gồm hạch dọc ĐM vành vị, thân tạng, lách, gan chung.<br>"
        f"• {R('N3')}: di căn hạch xa: dọc ĐM chủ bụng, mạc treo ruột, sau tá tràng–đầu tụy, cuống gan, dây chằng gan–tá tràng.",
        "Lưu ý mốc phân biệt N1 vs N2 theo barem sách cũ là khoảng cách 3 cm quanh u (≤ 3 cm là N1; > 3 cm dọc thân tạng/vành vị/lách/gan chung là N2; sang cuống gan/đầu tụy/ĐM chủ bụng là N3).",
        "B2.03, B2.04", ["TNM", "Hach"],
    ),
    basic(
        "SURG21-B2-03", "B2", "TNM — M, Giai đoạn kết hợp & Đường di căn", 1,
        f"{B('[TNM UT dạ dày — M & Giai đoạn]')} Kể các vị trí {R('M1')}, bảng chia {B('Giai đoạn 0 → IV')} và {Y('5 đường thâm nhiễm di căn')}?",
        f"1) <b>M (Di căn xa):</b> {B('M0')} không; {R('M1')} có di căn xa (gan, phúc mạc, phổi, buồng trứng [{B('u Krukenberg')}], hạch trên đòn [{B('hạch Troisier')}]).<br>"
        f"2) <b>Giai đoạn TNM kết hợp:</b> 0 ({B('TisN0M0')}); Ia ({B('T1N0M0')}); Ib ({B('T1N1M0 / T2N0M0')}); II ({B('T1N2M0 / T2N1M0 / T3N0M0')}); IIIa ({B('T2N2M0 / T3N1M0 / T4N0M0')}); IIIb ({B('T3N2M0 / T4N1M0')}); IV ({R('T4N2M0 hoặc bất kỳ T, N kèm M1')}).<br>"
        f"3) <b>5 đường thâm nhiễm &amp; di căn:</b> Chiều rộng bề mặt niêm mạc; bề sâu các lớp thành dạ dày; hệ bạch huyết tới các chặng hạch; mạch máu tới tạng xa (gan, phổi, não...); xâm lấn trực tiếp tạng lân cận (tụy, gan, mạc nối, đại tràng ngang).",
        "Đừng quên T4N2M0 trong bảng TNM này đã được xếp thẳng vào Giai đoạn IV ngang hàng với M1!",
        "B2.05, B2.06, B2.08", ["TNM", "Di-can"],
    ),
    trap(
        "SURG21-B2-04", "B2", "Bẫy xếp hạng N & T4N2M0 trong bảng TNM barem",
        "Xếp hạch dọc ĐM chủ bụng hoặc hạch cuống gan vào N2, hoặc xếp T4N2M0 vào Giai đoạn IIIb thay vì Giai đoạn IV.",
        f"1) <b>N2 vs N3:</b> {B('N2')} là hạch vượt u &gt; 3 cm dọc {B('ĐM vành vị, thân tạng, lách, gan chung')}; còn hạch dọc {R('ĐM chủ bụng, mạc treo ruột, sau tá tràng–đầu tụy, cuống gan, dây chằng gan–tá tràng')} là {R('N3')}.<br>"
        f"2) <b>T4N2M0:</b> Thuộc {R('Giai đoạn IV')} (không phải IIIb; IIIb chỉ gồm T3N2M0 và T4N1M0).",
        "Học thuộc đúng 2 ranh giới dễ đánh đố này giúp ăn trọn điểm bảng phân loại TNM phòng thi.",
        "B2.04, B2.06", ["TNM", "Bay-phan-giai-doan"],
    ),
    cloze(
        "SURG21-B2-05", "B2", "Tỉ lệ vị trí & vi thể",
        f"Ung thư dạ dày gặp nhiều nhất ở vùng {clz(1, Y('hang và môn vị (50–60%)'))} và bờ cong nhỏ ({clz(2, Y('25–30%'))}); về vi thể, ung thư tuyến (Adenocarcinoma) chiếm tới {clz(3, Y('90%'))}.",
        "B2.01, B2.07", ["Giai-phau-benh", "Nguong-so"],
    ),
    trap(
        "SURG21-B2-06", "B2", "Bẫy thể thâm nhiễm cứng Linitis plastica",
        "Thấy niêm mạc dạ dày không có khối u sùi hay ổ loét rõ nhưng thành dạ dày dày cứng như ống cao su, mất các nếp niêm mạc — nhận diện thể bệnh nào và chỉ định phẫu thuật ra sao?",
        f"1) <b>Nhận diện thể bệnh:</b> Tuyệt đối không loại trừ ung thư — đây là hình thái kinh điển của {R('thể thâm nhiễm cứng (Linitis plastica)')} (thành dạ dày dày cứng như ống cao su, mất nếp niêm mạc).<br>"
        f"2) <b>Chỉ định phẫu thuật:</b> Thể thâm nhiễm lan tỏa thường chỉ định {G('cắt toàn bộ dạ dày')} theo nguyên tắc.",
        "Tế bào ung thư (thường thể nhẫn/kém biệt hóa) lan ngầm dưới niêm mạc và lớp cơ nên bề mặt niêm mạc có thể ít sùi loét nhưng trên X-quang thấy hình cao nguyên mất nhu động.",
        "B2.02, B4.01, B6.02", ["Linitis-plastica", "Dai-the"], red_flag=True, asks=["Nhận diện", "Chỉ định"],
    ),
    cloze(
        "SURG21-B2-07", "B2", "Khoảng cách hạch N1 vs N2",
        f"Trong phân loại TNM ung thư dạ dày: N1 là di căn hạch cạnh dạ dày cách u {clz(1, Y('≤ 3 cm'))} dọc bờ cong nhỏ/lớn; N2 là di căn hạch vượt quá u {clz(2, Y('> 3 cm'))} dọc ĐM vành vị, thân tạng, lách, gan chung.",
        "B2.04", ["TNM", "Nguong-so"],
    ),

    # ============================================================
    # B3. TRIỆU CHỨNG LÂM SÀNG
    # ============================================================
    basic(
        "SURG21-B3-01", "B3", "Lâm sàng sớm vs muộn", 1,
        f"{B('[Lâm sàng UT dạ dày]')} Đặc điểm {B('giai đoạn sớm')} (tỷ lệ không triệu chứng, dấu hiệu gợi ý) khác gì {R('giai đoạn muộn')} (đau, toàn thân, 4 dấu hiệu khám thực thể)?",
        f"1) <b>Giai đoạn sớm:</b> Không đặc hiệu, {Y('80%')} thường không triệu chứng; gợi ý: đau bụng mơ hồ thượng vị, đầy bụng khó tiêu, ậm ạch sau ăn, mệt mỏi, da xanh xao nhẹ, gầy sút cân không rõ nguyên nhân, giảm khả năng lao động.<br>"
        f"2) <b>Giai đoạn muộn — đau &amp; toàn thân:</b> Đau trên rốn kéo dài, liên tục tăng dần, {R('mất chu kỳ')}; gầy sút cân rõ rệt, suy mòn, thiếu máu nặng, muộn hơn có {R('da vàng rơm')}.<br>"
        f"3) <b>Thực thể muộn (4 dấu hiệu):</b> Sờ thấy khối u hoặc mảng cứng thượng vị; bụng trướng có dịch {R('cổ trướng')} (di căn phúc mạc); di căn {R('hạch thượng đòn trái (Troisier/Virchow)')}; di căn {R('buồng trứng 2 bên ở nữ (u Krukenberg)')}.",
        "Từ đau có chu kỳ theo bữa ăn (của loét lành tính) chuyển sang đau liên tục tăng dần mất chu kỳ trên rốn là tín hiệu cảnh báo chuyển ác tính. U Krukenberg di căn buồng trứng 2 bên và hạch Troisier trên đòn trái là dấu hiệu đã M1.",
        "B3.01, B3.02, B3.03", ["Lam-sang", "Krukenberg", "Troisier"],
    ),
    basic(
        "SURG21-B3-02", "B3", "Ba biến chứng cấp cứu", 1,
        f"{B('[Biến chứng UT dạ dày]')} Mô tả biểu hiện lâm sàng của {Y('3 biến chứng cấp cứu')} thường gặp trong ung thư dạ dày?",
        f"1) {R('Hẹp môn vị')}: Nôn ra thức ăn cũ của bữa trước, dấu hiệu {B('óc ách lúc đói')}, gầy rộc.<br>"
        f"2) {R('Chảy máu tiêu hóa trên')}: Nôn ra máu, đi ngoài phân đen.<br>"
        f"3) {R('Thủng dạ dày')}: Đau bụng đột ngột dữ dội như dao đâm, {R('bụng cứng như gỗ')} (thường gặp ở ung thư {B('thể loét')}).",
        "Hang môn vị chiếm 50–60% vị trí u nên hẹp môn vị rất hay xảy ra; còn ung thư thể loét hoại tử sâu dễ gây xuất huyết tiêu hóa hoặc thủng cấp cứu gây viêm phúc mạc.",
        "B3.04", ["Bien-chung", "Cap-cuu"],
    ),
    trap(
        "SURG21-B3-03", "B3", "Cảnh báo giai đoạn sớm âm thầm",
        "Loại trừ ung thư dạ dày chỉ vì bệnh nhân chưa sụt cân, không đau mất chu kỳ và không sờ thấy u thượng vị.",
        f"1) <b>Thực tế giai đoạn sớm:</b> Có tới {Y('80%')} bệnh nhân giai đoạn sớm {R('không có triệu chứng')}, số còn lại chỉ có triệu chứng mơ hồ dễ nhầm viêm loét dạ dày thông thường.<br>"
        f"2) <b>Ngưỡng cảnh giác:</b> Nhóm bệnh nhân trên {Y('40–50 tuổi')} có hội chứng dạ dày mới xuất hiện kéo dài bắt buộc chỉ định {G('nội soi dạ dày sinh thiết sớm')}.",
        "Chờ tới lúc đau mất chu kỳ, da vàng rơm, hạch Troisier hay u thượng vị mới đi soi thì bệnh đã ở giai đoạn muộn, thời gian sống trung bình rút ngắn rõ rệt.",
        "B3.01, B5.01", ["Co-do", "Tam-soat"], red_flag=True,
    ),
    cloze(
        "SURG21-B3-04", "B3", "Tỷ lệ âm thầm giai đoạn sớm",
        f"Ở giai đoạn sớm, ung thư dạ dày thường không đặc hiệu và có tới {clz(1, Y('80%'))} trường hợp thường không có triệu chứng.",
        "B3.01", ["Lam-sang", "Nguong-so"],
    ),
    trap(
        "SURG21-B3-05", "B3", "Cờ đỏ di căn xa khi khám thực thể",
        "Bệnh nhân nữ đau thượng vị kéo dài, sờ thấy khối u buồng trứng hai bên (u Krukenberg) hoặc hạch thượng đòn trái (hạch Troisier/Virchow) — ý nghĩa giai đoạn và sai lầm thường gặp?",
        f"1) <b>Ý nghĩa TNM:</b> Cả {R('u Krukenberg')} (di căn buồng trứng 2 bên) và {R('hạch Troisier/Virchow')} (hạch trên đòn trái) đều xếp vào {R('M1 — Giai đoạn IV')}.<br>"
        f"2) <b>Sai lầm cần tránh:</b> Không cắt u buồng trứng đơn thuần mà bỏ qua nội soi dạ dày tìm khối u nguyên phát.",
        "Tế bào ung thư từ dạ dày di căn theo đường phúc mạc/bạch huyết xuống hai buồng trứng tạo khối Krukenberg, hoặc theo ống ngực lên hạch thượng đòn trái.",
        "B2.05, B3.03", ["Krukenberg", "Troisier", "M1"], red_flag=True,
    ),

    # ============================================================
    # B4. CẬN LÂM SÀNG & B5. CHẨN ĐOÁN
    # ============================================================
    basic(
        "SURG21-B4-01", "B4", "X-quang dạ dày có cản quang", 1,
        f"{B('[X-quang cản quang UT dạ dày]')} Mô tả hình ảnh X-quang ở {B('giai đoạn sớm')} và {Y('3 hình ảnh kinh điển giai đoạn muộn')} tương ứng 3 thể giải phẫu bệnh?",
        f"1) <b>Giai đoạn sớm:</b> Ổ đọng thuốc nhỏ trên bề mặt, hình {B('niêm mạc hội tụ')}, một đoạn bờ cong bị cứng.<br>"
        f"2) <b>Giai đoạn muộn (3 hình ảnh):</b><br>"
        f"• {R('Ổ đọng thuốc thấu kính')} → tương ứng {B('thể loét')}.<br>"
        f"• {B('Hình khuyết bờ nham nhở')} → tương ứng {B('thể sùi')}.<br>"
        f"• {B('Hình thâm nhiễm cứng mất nhu động thành dạ dày (hình cao nguyên)')} → tương ứng {B('thể thâm nhiễm cứng')}.",
        "Đối chiếu trực tiếp GPB ↔ X-quang: ổ loét chứa thuốc thành hình thấu kính (nằm trong lòng bờ vị trí ổ loét), u sùi lồi vào lòng choán chỗ tạo hình khuyết bờ nham nhở, thâm nhiễm cứng mất sóng nhu động tạo hình cao nguyên đờ cứng.",
        "B4.01", ["Can-lam-sang", "X-quang"],
    ),
    basic(
        "SURG21-B4-02", "B4", "Nội soi, EUS, CĐHA & Tumor markers", 1,
        f"{B('[Nội soi & Xét nghiệm UT dạ dày]')} Giá trị của {G('nội soi ống mềm')} (kèm số mảnh sinh thiết), {B('EUS')}, {B('CT/PET')}, và {B('Tumor markers')} đặc hiệu nhất?",
        f"1) {G('Nội soi dạ dày ống mềm')}: Chính xác nhất, vượt trội hơn X-quang vì phát hiện tổn thương còn khu trú lớp niêm mạc; cho phép {G('sinh thiết ít nhất 6–8 mảnh quanh bờ tổn thương')} làm giải phẫu bệnh.<br>"
        f"2) {B('Siêu âm nội soi (EUS)')}: Đánh giá chính xác độ {B('xâm lấn thành dạ dày')} và {B('hạch cạnh u')}.<br>"
        f"3) {B('Siêu âm bụng, CT ngực-bụng, PET scans &amp; tế bào học')}: Đánh giá xâm lấn lân cận và di căn hạch, gan, tụy, buồng trứng, màng bụng; xét nghiệm tế bào học dịch dạ dày/màng bụng.<br>"
        f"4) {B('Tumor markers')}: {B('CEA')} tăng cao; đặc biệt {G('CA 72-4')} là marker đặc hiệu nhất cho ung thư dạ dày (phối hợp cùng CEA, CA 19-9).",
        "Sinh thiết ít nhất 6–8 mảnh quanh bờ ổ loét (tránh vùng hoại tử trung tâm) giảm tối đa âm tính giả; CA 72-4 đặc hiệu nhất cho UT dạ dày khi phối hợp CEA và CA 19-9.",
        "B4.02, B4.03", ["Can-lam-sang", "Noi-soi", "CA72-4"],
    ),
    basic(
        "SURG21-B5-01", "B5", "Chẩn đoán, tiến triển & biến chứng", 1,
        f"{B('[Chẩn đoán & Tiên lượng UT dạ dày]')} Cảnh giác {G('chẩn đoán')} sớm ở nhóm tuổi nào, {R('tiến triển')} khi không phẫu thuật, và {Y('3 biến chứng')}?",
        f"1) <b>Chẩn đoán sớm:</b> Rất khó ở giai đoạn sớm; cần chú ý nhóm bệnh nhân trên {Y('40–50 tuổi')} có hội chứng dạ dày mới xuất hiện kéo dài → chỉ định {G('nội soi dạ dày sinh thiết sớm')}.<br>"
        f"2) <b>Tiến triển tự nhiên:</b> Tiến triển nhanh; nếu {R('không phẫu thuật')}, bệnh nhân thường tử vong sau {Y('5–6 tháng')}.<br>"
        f"3) <b>Biến chứng:</b> {R('Hẹp môn vị')}, {R('xuất huyết tiêu hóa')}, {R('thủng dạ dày gây viêm phúc mạc')}.",
        "Mốc tuổi > 40–50 là ngưỡng vàng để không bao giờ điều trị triệu chứng kéo dài bằng thuốc dạ dày mà không soi loại trừ ung thư.",
        "B5.01, B5.02", ["Chan-doan", "Tien-trien"], asks=["Chẩn đoán", "Tiến triển", "Biến chứng"],
    ),
    cloze(
        "SURG21-B4-03", "B4", "Số mảnh sinh thiết & Marker đặc hiệu",
        f"Khi nội soi dạ dày nghi ung thư cần sinh thiết ít nhất {clz(1, Y('6–8 mảnh'))} quanh bờ tổn thương; chất chỉ điểm khối u đặc hiệu nhất cho ung thư dạ dày là {clz(2, G('CA 72-4'))}.",
        "B4.02, B4.03", ["Can-lam-sang", "Nguong-so"],
    ),
    trap(
        "SURG21-B4-04", "B4", "Bẫy âm tính giả khi sinh thiết nội soi & quá tin X-quang",
        "Vì sao sinh thiết chỉ bấm 1–2 mảnh ở giữa đáy ổ loét hoặc quá tin phim X-quang cản quang bình thường có thể bỏ sót ung thư dạ dày sớm?",
        f"1) <b>Bẫy sinh thiết:</b> Giữa đáy ổ loét thường là mô hoại tử/giả mạc — phải {G('sinh thiết ít nhất 6–8 mảnh quanh bờ tổn thương')}.<br>"
        f"2) <b>Bẫy X-quang:</b> {G('Nội soi dạ dày ống mềm')} vượt trội hơn hẳn X-quang vì phát hiện được tổn thương còn khu trú ở {B('lớp niêm mạc')}.",
        "Sinh thiết đủ 6–8 mảnh quanh rìa gồ của ổ loét nơi tế bào u sống đậm đặc là chìa khóa tránh chẩn đoán muộn do kết quả âm tính giả.",
        "B4.02", ["Noi-soi", "Sinh-thiet"],
    ),

    # ============================================================
    # B6. ĐIỀU TRỊ
    # ============================================================
    basic(
        "SURG21-B6-01", "B6", "Nguyên tắc phẫu thuật R0/R1/R2", 1,
        f"{B('[Nguyên tắc phẫu thuật UICC 1992]')} Phân biệt định nghĩa {G('R0')}, {Y('R1')} và {R('R2')} trong phẫu thuật ung thư dạ dày?",
        f"1) {G('Phẫu thuật R0 (No residual tumor)')}: Lấy bỏ triệt để u cả về {G('đại thể lẫn vi thể')}, diện cắt sạch tế bào ung thư.<br>"
        f"2) {Y('Phẫu thuật R1 (Microscopic residual tumor)')}: Đã lấy sạch đại thể nhưng {Y('vi thể diện cắt còn tế bào ung thư')}.<br>"
        f"3) {R('Phẫu thuật R2 (Macroscopic residual tumor)')}: Vẫn còn {R('sót mô ung thư nhìn thấy được trên đại thể')}.",
        "Mục tiêu tối thượng của mọi cuộc mổ triệt căn là đạt R0; nếu diện cắt còn tế bào trên vi thể (R1) phải phối hợp xạ trị và hóa trị bổ trợ.",
        "B6.01", ["Dieu-tri", "R0"],
    ),
    basic(
        "SURG21-B6-02", "B6", "Kỹ thuật mổ triệt căn & tạm thời", 1,
        f"{B('[Kỹ thuật phẫu thuật UT dạ dày]')} Trình bày {Y('4 phương pháp mổ triệt căn')} (chỉ định, diện cắt, nạo hạch) và {Y('3 biện pháp mổ tạm thời')}?",
        f"1) <b>Cắt đoạn dạ dày (bán phần dưới hoặc cực trên):</b> Kèm {G('nạo vét hạch D2 tỉ mỉ')}, diện cắt cách u ít nhất {Y('5–6 cm')}.<br>"
        f"2) <b>Cắt toàn bộ dạ dày:</b> Theo yêu cầu hoặc nguyên tắc khi u ở {B('1/3 trên')} hoặc {B('thể thâm nhiễm lan tỏa')}.<br>"
        f"3) <b>Cắt dạ dày mở rộng:</b> Cắt bỏ dạ dày kèm cơ quan lân cận bị u xâm lấn ({B('lách, đuôi tụy, thùy gan...')}).<br>"
        f"4) <b>Cắt hớt niêm mạc sớm (EMR/ESD):</b> Can thiệp cho tổn thương rất sớm khu trú lớp niêm mạc.<br>"
        f"5) <b>Mổ tạm thời:</b> {G('Nối vị tràng')} (khi hẹp môn vị không cắt được u), {G('mở thông dạ dày/hỗng tràng nuôi dưỡng')}, {G('cầm máu cấp cứu')}.",
        "Lưu ý quy chuẩn diện cắt an toàn cách u ít nhất 5–6 cm kèm vét hạch D2. Khi u 1/3 trên hoặc thể thâm nhiễm cứng lan tỏa (Linitis plastica) bắt buộc cắt toàn bộ dạ dày.",
        "B6.02", ["Dieu-tri", "Phau-thuat", "D2"],
    ),
    basic(
        "SURG21-B6-03", "B6", "Hóa trị, Đích & Xạ trị", 1,
        f"{B('[Hóa trị, Đích & Xạ trị UT dạ dày]')} Thuốc nền tảng, chi tiết liều &amp; chu kỳ {G('phác đồ ELF')}, các phác đồ khác, {B('nhắm trúng đích')} và chỉ định {B('xạ trị')}?",
        f"1) <b>Thuốc nền tảng:</b> {G('5-FU (5-Fluorouracil)')}.<br>"
        f"2) <b>ELF (liều &amp; chu kỳ):</b> {G('Etoposide 120 mg/m²')} + {G('Leucovorin 300 mg/m²')} + {G('5-FU 500 mg/m²')}; truyền tĩnh mạch chu kỳ {Y('21 ngày')}, {Y('6 đợt')}, mỗi đợt {Y('3 ngày')}.<br>"
        f"3) <b>Các phác đồ khác:</b> {B('PC')} (Paclitaxel + Cisplatin), {B('EAP')}, {B('FAM')}.<br>"
        f"4) <b>Miễn dịch &amp; nhắm trúng đích:</b> Kháng thể đơn dòng, nhắm trúng đích phân tử ({G('HER2-neu / Trastuzumab')}).<br>"
        f"5) <b>Xạ trị:</b> Bổ trợ phối hợp hóa chất khi u {R('xâm lấn diện cắt hoặc hạch di căn')}.",
        "Leucovorin (acid folinic) khuếch đại tác dụng ức chế thymidylate synthase của 5-FU trong phác đồ ELF; Trastuzumab nhắm vào thụ thể HER2-neu dương tính.",
        "B6.03, B6.04", ["Hoa-tri", "ELF", "HER2"],
    ),
    basic(
        "SURG21-B6-04", "B6", "Tiên lượng sống thêm sau mổ", 2,
        f"{B('[Tiên lượng UT dạ dày]')} So sánh tỉ lệ sống sau {Y('5 năm')} khi phát hiện sớm (Nhật vs Việt Nam) và sống thêm ở giai đoạn {R('phát hiện muộn')}?",
        f"1) <b>Phát hiện sớm (sống sau 5 năm):</b> Tại Nhật Bản đạt {G('97%')}, tại Việt Nam đạt {G('91%')}.<br>"
        f"2) <b>Phát hiện muộn (có cắt đoạn dạ dày):</b> Thời gian sống trung bình là {Y('14,9 tháng')}; giai đoạn 2006–2009 tỉ lệ sống sau {Y('3 năm')} đạt {Y('62,6%')}.<br>"
        f"3) <b>Không cắt được u:</b> Thời gian sống thêm trung bình chỉ khoảng {R('6 tháng')}.",
        "Khoảng cách sống 5 năm 91–97% (phát hiện sớm) so với 6 tháng (không cắt được u) chứng minh giá trị sống còn của nội soi sàng lọc sớm.",
        "B6.05", ["Tien-luong", "Song-them"],
    ),
    cloze(
        "SURG21-B6-05", "B6", "Phác đồ ELF & diện cắt D2",
        f"Phác đồ hóa trị ELF trong ung thư dạ dày gồm: {clz(1, G('Etoposide 120 mg/m², Leucovorin 300 mg/m², 5-FU 500 mg/m²'))}, truyền TM chu kỳ {clz(2, Y('21 ngày × 6 đợt'))} (mỗi đợt 3 ngày).",
        "B6.03", ["ELF", "Lieu-luong"],
    ),
    trap(
        "SURG21-B6-06", "B6", "Cờ đỏ sai lầm diện cắt và chỉ định cắt toàn bộ dạ dày",
        "Cắt đoạn dạ dày với diện cắt cách u dưới 5 cm hoặc cố giữ lại phần dạ dày lành khi u nằm ở 1/3 trên / thể thâm nhiễm lan tỏa dẫn tới hậu quả gì?",
        f"1) <b>Nguy cơ R1/R2:</b> Bỏ sót tế bào ung thư lan ngầm dưới niêm mạc tại diện cắt ({R('phẫu thuật R1 hoặc R2')}).<br>"
        f"2) <b>Quy chuẩn bắt buộc:</b> Cắt đoạn dạ dày kèm vét hạch D2 tỉ mỉ với diện cắt {Y('cách u ít nhất 5–6 cm')}; riêng u {B('1/3 trên')} hoặc {B('thể thâm nhiễm lan tỏa')} phải chỉ định {G('cắt toàn bộ dạ dày')}.",
        "Lan tràn dưới niêm mạc có thể đi xa bờ u nhìn thấy bằng mắt thường nên ranh giới 5–6 cm và chỉ định cắt toàn bộ dạ dày cho u 1/3 trên / thể thâm nhiễm là nguyên tắc sống còn.",
        "B6.01, B6.02", ["Phau-thuat", "R0"], red_flag=True,
    ),
    cloze(
        "SURG21-B6-07", "B6", "Diện cắt phẫu thuật D2",
        f"Phẫu thuật cắt đoạn dạ dày kèm nạo vét hạch D2 tỉ mỉ đòi hỏi diện cắt cách u ít nhất {clz(1, Y('5–6 cm'))}, nhằm đạt phẫu thuật {clz(2, G('R0'))} (lấy bỏ triệt để cả đại thể lẫn vi thể).",
        "B6.01, B6.02", ["Phau-thuat", "Nguong-so"],
    ),
    cloze(
        "SURG21-B6-08", "B6", "Tiên lượng sống sau 5 năm",
        f"Tiên lượng sống sau 5 năm ở ung thư dạ dày phát hiện sớm tại Nhật Bản đạt {clz(1, G('97%'))} và tại Việt Nam đạt {clz(2, G('91%'))}; nếu không cắt được u, thời gian sống thêm trung bình chỉ khoảng {clz(3, R('6 tháng'))}.",
        "B6.05", ["Tien-luong", "Nguong-so"],
    ),

    # ============================================================
    # B7. CÂU HỎI LƯỢNG GIÁ & TÀI LIỆU THAM KHẢO
    # ============================================================
    trap(
        "SURG21-B7-01", "B7", "Bẫy lượng giá — Đường lây HP & Cơ địa tiền ung thư",
        "Hai câu bẫy kinh điển trong phần lượng giá: (1) chọn 'uống nước có nhiều HP' là yếu tố nguy cơ; (2) chọn 'đã cắt dây thần kinh X' là cơ địa dễ mắc UT dạ dày.",
        f"1) <b>Yếu tố nguy cơ (NGOẠI TRỪ):</b> '{R('Uống nước có nhiều HP')}' là SAI — vì HP lây truyền qua đường {B('miệng-miệng hoặc phân-miệng')}, không gọi là uống nước có nhiều HP (còn thịt cá ướp muối/hun khói, thuốc lá, rượu, nước nhiều nitrate đều ĐÚNG).<br>"
        f"2) <b>Cơ địa dễ mắc (NGOẠI TRỪ):</b> '{R('Người đã cắt dây thần kinh X')}' là SAI — các cơ địa dễ mắc ĐÚNG gồm: đã cắt đoạn dạ dày, viêm dạ dày mạn tính, thiếu máu ác tính Biermer, teo niêm mạc vùng đáy vị.",
        "Cắt dây X làm giảm tiết acid nhưng không xếp vào nhóm cơ địa tiền ung thư kinh điển như cắt đoạn dạ dày hay thiếu máu Biermer.",
        "B7.01, B7.02", ["Luong-gia", "Bay-trac-nghiem"], asks=["yếu tố nguy cơ", "cơ địa"],
    ),
    trap(
        "SURG21-B7-02", "B7", "Bẫy lượng giá — Thể GPB & Hình ảnh X-quang",
        "Trong câu hỏi lượng giá về hình ảnh X-quang ung thư dạ dày, 'hình thoát thuốc' có phải là dấu hiệu X-quang của ung thư dạ dày không, và 5 thể GPB đúng/sai thế nào?",
        f"1) <b>Hình ảnh XQ UT dạ dày:</b> Gồm ổ đọng thuốc hình thấu kính, hình khuyết bờ nham nhở, hình thâm nhiễm cứng, hình thuốc không xuống được tá tràng (trong hẹp môn vị); còn {R('hình thoát thuốc')} là SAI (gặp trong thủng tạng rỗng/thoát cản quang ra ngoài lòng).<br>"
        f"2) <b>Thể giải phẫu bệnh:</b> Thể loét, thể thâm nhiễm cứng, thể u, thể loét thâm nhiễm và thể sùi loét đều {G('ĐÚNG')}.",
        "Ổ đọng thuốc thấu kính là thuốc đọng trong hốc loét còn nằm trong bờ dạ dày, khác hoàn toàn hình ảnh thoát thuốc cản quang tràn ra ngoài thành dạ dày.",
        "B7.03, B7.04", ["Luong-gia", "X-quang"],
    ),
    basic(
        "SURG21-B7-03", "B7", "Tài liệu tham khảo barem", 2,
        f"{B('[Tài liệu tham khảo UT dạ dày]')} Kể tên {Y('7 tài liệu tham khảo')} trong barem Ung thư dạ dày?",
        f"1) {B('Bệnh học ngoại khoa')} — NXB Y học Hà Nội (1999, tập 1).<br>"
        f"2) {B('Bách khoa thư bệnh học')} — Trung tâm QG biên soạn từ điển bách khoa VN (1991, tập 1).<br>"
        f"3) {B('Bài giảng bệnh học ngoại khoa')} — ĐH Y Dược TP.HCM (1998).<br>"
        f"4) {B('Bài giảng ung thư học')} — NXB Y học Hà Nội (1999).<br>"
        f"5) {B('Bài giảng điều trị học ngoại khoa')} — ĐH Y Dược TP.HCM (1998).<br>"
        f"6) {B('Trịnh Hồng Sơn (2001)')} — Luận án Tiến sĩ về nạo vét hạch trong điều trị phẫu thuật UT dạ dày.<br>"
        f"7) {B('Đỗ Trọng Quyết (2010)')} — Luận án Tiến sĩ về phẫu thuật kết hợp hóa chất ELF và miễn dịch trị liệu Aslem.",
        "Hai luận án tiến sĩ cuối (Trịnh Hồng Sơn 2001 và Đỗ Trọng Quyết 2010) là nguồn gốc của số liệu vét hạch D2, phác đồ ELF và tỉ lệ sống tại Việt Nam (91% phát hiện sớm; 14,9 tháng / 3 năm 62,6% phát hiện muộn).",
        "B7.05", ["Tai-lieu-tham-khao"],
    ),

    # ============================================================
    # 4 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (≥ 3 BẮT BUỘC THEO GATE 2.8)
    # ============================================================
    algo(
        "SURG21-ALGO-01", "B4", "Thuật toán tầm soát & chẩn đoán",
        "Tiếp cận bệnh nhân nghi ung thư dạ dày",
        f"1) <b>Bước 1 — Sàng lọc đối tượng nguy cơ:</b> Người {Y('> 40–50 tuổi')} có hội chứng dạ dày mới xuất hiện kéo dài, hoặc đau thượng vị chuyển từ có chu kỳ sang liên tục tăng dần {R('mất chu kỳ')}.<br>"
        f"2) <b>Bước 2 — Tiêu chuẩn khẳng định:</b> Chỉ định sớm {G('nội soi dạ dày ống mềm')} (vượt trội X-quang) kết hợp {G('sinh thiết ít nhất 6–8 mảnh quanh bờ tổn thương')}.<br>"
        f"3) <b>Bước 3 — Đánh giá TNM &amp; Marker:</b> {B('Siêu âm nội soi (EUS)')} đánh giá độ xâm lấn thành &amp; hạch cạnh u; {B('CT ngực-bụng / PET / Siêu âm')} tìm di căn gan, phúc mạc, hạch Troisier, u Krukenberg; định lượng {G('CA 72-4')} (đặc hiệu nhất) phối hợp CEA, CA 19-9.",
        "Tránh mất thời gian điều trị thử bằng PPI ở người > 40–50 tuổi khi hội chứng dạ dày kéo dài hoặc mới khởi phát; nội soi sinh thiết sớm ≥ 6–8 mảnh quanh bờ là chìa khóa bắt bệnh ở giai đoạn sống 5 năm > 90%.",
        "B3.01, B4.02, B4.03, B5.01", ["Chan-doan", "Noi-soi"],
    ),
    algo(
        "SURG21-ALGO-02", "B6", "Thuật toán chọn phương pháp phẫu thuật",
        "Chọn kỹ thuật mổ ung thư dạ dày (Triệt căn vs Tạm thời)",
        f"1) <b>Tổn thương rất sớm khu trú lớp niêm mạc:</b> {G('Cắt hớt niêm mạc qua nội soi (EMR/ESD)')}.<br>"
        f"2) <b>U mổ triệt căn được (hang-môn vị / bờ cong nhỏ):</b> {G('Cắt đoạn dạ dày')} (bán phần dưới hoặc cực trên) + {G('vét hạch D2 tỉ mỉ')} + diện cắt cách u {Y('≥ 5–6 cm')} để đạt {G('R0')}.<br>"
        f"3) <b>U 1/3 trên hoặc thể thâm nhiễm lan tỏa (Linitis plastica):</b> {G('Cắt toàn bộ dạ dày')}; nếu xâm lấn lách, đuôi tụy, thùy gan → {G('cắt dạ dày mở rộng')}.<br>"
        f"4) <b>Không cắt được u (hẹp môn vị / chảy máu / suy kiệt):</b> Mổ tạm thời — {G('nối vị tràng')}, {G('mở thông dạ dày/hỗng tràng nuôi dưỡng')}, {G('cầm máu cấp cứu')}.",
        "Ranh giới lựa chọn phẫu thuật dựa vào vị trí u (1/3 trên/lan tỏa vs hang-môn vị), độ sâu (niêm mạc → EMR/ESD) và khả năng lấy sạch R0 (cách u ≥ 5–6 cm kèm D2).",
        "B6.01, B6.02", ["Phau-thuat", "D2"],
    ),
    algo(
        "SURG21-ALGO-03", "B6", "Thuật toán điều trị bổ trợ toàn thân",
        "Chỉ định hóa trị, xạ trị và điều trị đích sau phẫu thuật ung thư dạ dày",
        f"1) <b>Bước 1 — Nền tảng hóa trị:</b> Phối hợp đa hóa trị lấy {G('5-FU')} làm thuốc nền tảng.<br>"
        f"2) <b>Bước 2 — Phác đồ chuẩn (ELF):</b> Etoposide {Y('120 mg/m²')} + Leucovorin {Y('300 mg/m²')} + 5-FU {Y('500 mg/m²')}, truyền TM chu kỳ {Y('21 ngày')}, {Y('6 đợt')} (mỗi đợt {Y('3 ngày')}); lựa chọn khác: {B('PC, EAP, FAM')}.<br>"
        f"3) <b>Bước 3 — Xạ trị bổ trợ:</b> Phối hợp hóa chất khi {R('u xâm lấn diện cắt (R1) hoặc có hạch di căn')}.<br>"
        f"4) <b>Bước 4 — Đích &amp; Miễn dịch:</b> Kháng thể đơn dòng nhắm trúng đích phân tử {G('HER2-neu / Trastuzumab')}.",
        "Đánh giá hậu phẫu phải kiểm tra tình trạng diện cắt (R0/R1), hạch di căn và dấu ấn HER2-neu để quyết định hóa-xạ bổ trợ và nhắm trúng đích.",
        "B6.01, B6.03, B6.04", ["Hoa-tri", "Xa-tri"],
    ),
    algo(
        "SURG21-ALGO-04", "B3", "Thuật toán cấp cứu ngoại khoa UTDD",
        "Nhận diện và xử trí 3 biến chứng cấp cứu của ung thư dạ dày",
        f"1) <b>Hẹp môn vị (u vùng hang-môn vị 50–60%):</b> Nhận diện qua nôn thức ăn cũ bữa trước, dấu {B('óc ách lúc đói')}, gầy rộc → Hồi sức, nếu không cắt được u thì {G('nối vị tràng')} hoặc mở thông nuôi dưỡng.<br>"
        f"2) <b>Chảy máu tiêu hóa trên:</b> Nôn máu, phân đen → Hồi sức, nội soi/phẫu thuật {G('cầm máu cấp cứu')}.<br>"
        f"3) <b>Thủng dạ dày (hay gặp thể loét):</b> Đau đột ngột dữ dội như dao đâm, {R('bụng cứng như gỗ')} (viêm phúc mạc) → {G('Phẫu thuật cấp cứu')} ngay.",
        "Trong cấp cứu bụng ngoại khoa ở bệnh nhân lớn tuổi, tam chứng nôn thức ăn cũ + óc ách (hẹp môn vị), XHTH trên, hoặc thủng dạ dày có thể là biểu hiện đầu tiên đưa bệnh nhân ung thư dạ dày tới viện.",
        "B2.01, B3.04, B5.02, B6.02", ["Cap-cuu", "Bien-chung"],
    ),
]
