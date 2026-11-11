# -*- coding: utf-8 -*-
"""SURG-20B: Ung thư thực quản — nguồn thẻ duy nhất xây dựng hoàn toàn từ barem ôn thi.
Nguồn barem: C:\\Users\\THANHANH\\Desktop\\barem\\01_Ung_thu_thuc_quan_barem.md (TS. Phan Văn Cương, tr. 5–13).
Mã barem từng dòng lưu trong SURG-20B_Ung_thu_thuc_quan_BAREM.md ([B1.01]..[B10.04]).
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

BADGE = ("🏛️ BAREM ÔN THI · UNG THƯ THỰC QUẢN", "badge-barem")
SRC = "📖 Nguồn: Barem Ôn thi Ung thư thực quản — TS. Phan Văn Cương (tr. 5–13). Barem: "


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
        "tags": ["SURG-20B", "Ung-thu-thuc-quan", "Barem-goc", section] + tags,
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
        "tags": ["SURG-20B", "Ung-thu-thuc-quan", "Barem-goc", "Cloze-phu", section] + tags,
    }


cards_data = [
    # ============================================================
    # B1. ĐẠI CƯƠNG
    # ============================================================
    basic(
        "SURG20B-B1-01", "B1", "Đại cương & Dịch tễ", 1,
        f"{B('[Đại cương UT thực quản]')} Xếp hạng {Y('mắc mới')} và {R('tử vong')}, tiên lượng phát hiện sớm so với giai đoạn muộn, và {Y('thời gian sống thêm trung bình')} khi đã có triệu chứng tại chỗ là bao nhiêu?",
        f"1) <b>Thứ hạng chung:</b> Hay gặp xếp hàng {Y('thứ 9')} trong các bệnh ung thư; nguyên nhân gây tử vong vì ung thư đứng {R('thứ 6')}.<br>"
        f"2) <b>Phát hiện &amp; tiên lượng:</b> Tỉ lệ {G('điều trị khỏi cao')} nếu phát hiện sớm, nhưng thường phát hiện ở {R('giai đoạn muộn')}.<br>"
        f"3) <b>Sống thêm trung bình:</b> Ở bệnh nhân đã có triệu chứng tại chỗ không lớn hơn {Y('18 tháng')} (dù 2 thập kỷ qua có nhiều tiến bộ trong chẩn đoán và điều trị).<br>"
        f"4) <b>Xu hướng nghiên cứu điều trị:</b> Gần đây tập trung vào {G('hóa xạ trị đồng thời')} và {G('điều trị bổ trợ')}.",
        "Ung thư thực quản tiến triển âm thầm vì lòng ống tiêu hóa giãn bù trừ tốt. Khi xuất hiện nuốt nghẹn rõ, u thường đã chiếm phần lớn chu vi và xâm lấn qua thành, khiến thời gian sống thêm trung bình chỉ ≤ 18 tháng.",
        "B1.01, B1.02, B1.03", ["Dai-cuong", "Dich-te"],
    ),
    basic(
        "SURG20B-B1-02", "B1", "Dịch tễ học tại Mỹ (2008)", 2,
        f"{B('[Dịch tễ UT thực quản tại Mỹ — năm 2008]')} Nêu {Y('tỷ lệ')} chiếm trong tổng số ung thư / UT ống tiêu hóa, số ca mắc – tử vong, {Y('tuổi trung bình')}, chênh lệch {B('giới tính')} và {Y('tỉ lệ sống 5 năm')}?",
        f"1) <b>Tỉ trọng &amp; số ca (2008):</b> Chiếm {Y('1%')} tổng số ung thư và {Y('6%')} các loại UT ống tiêu hóa; có {Y('16.470')} ca mới mắc và {R('14.280')} BN tử vong.<br>"
        f"2) <b>Tuổi mắc bệnh:</b> Tuổi trung bình là {Y('69')}, hiếm gặp ở bệnh nhân dưới {Y('25 tuổi')}.<br>"
        f"3) <b>Giới tính:</b> Nam nhiều gấp {Y('4 lần')} nữ giới; riêng UT biểu mô tuyến ở nam nhiều gấp {Y('8–9 lần')} nữ giới.<br>"
        f"4) <b>Sống 5 năm tại Mỹ:</b> Khoảng {Y('5%')} (1975–1977), tăng {Y('10%')} (1984–1986) và {Y('10%')} (1996–2003).",
        "Sự chênh lệch giới tính rất rõ (nam gấp 4 lần chung và 8–9 lần ở thể tuyến) phản ánh phơi nhiễm thuốc lá, rượu, béo phì và GERD kéo dài ở nam giới. Con số ca tử vong (14.280) gần xấp xỉ ca mắc mới (16.470) cho thấy độ ác tính rất cao.",
        "B1.04, B1.05, B1.06", ["Dai-cuong", "Dich-te-My"],
    ),
    basic(
        "SURG20B-B1-03", "B1", "Dịch tễ Quốc tế & Việt Nam", 2,
        f"{B('[Dịch tễ Quốc tế & Việt Nam]')} Những quốc gia nào có tỷ lệ mắc cao, sự chuyển dịch giữa {B('UT biểu mô vảy')} và {B('UT biểu mô tuyến')}, và số liệu {Y('GLOBOCAN 2008 tại Việt Nam')} ra sao?",
        f"1) <b>Quốc gia tỷ lệ mắc cao:</b> {B('Trung Quốc, Iran, Pháp và Nam Phi')}.<br>"
        f"2) <b>Chuyển dịch mô bệnh học:</b> Những năm 70, khoảng {Y('90%')} UT thực quản là {B('UT biểu mô vảy')}; những năm gần đây, {B('UT biểu mô tuyến')} tăng nhanh và chiếm {Y('60%–70%')}.<br>"
        f"3) <b>Tại Việt Nam (GLOBOCAN 2008):</b> Mới mắc cả 2 giới khoảng {Y('1.511')} ca, tử vong {R('1.157')} ca; tỷ lệ mắc chuẩn theo tuổi {Y('1,9/100.000')} dân và tử vong chuẩn theo tuổi {R('1,4/100.000')} dân.",
        "Vành đai ung thư thực quản (Trung Quốc, Iran...) gắn với thói quen ăn uống thực phẩm nóng/ngâm ủ và yếu tố môi trường gây thể vảy, trong khi phương Tây chứng kiến sự trỗi dậy của thể tuyến (60–70%) do béo phì và trào ngược GERD.",
        "B1.07, B1.08", ["Dai-cuong", "Dich-te-VN"],
    ),
    trap(
        "SURG20B-B1-04", "B1", "Bẫy số liệu dịch tễ",
        "Nhầm lẫn tỉ lệ sống 5 năm (5% năm 1975–1977; tăng 10% giai đoạn 1984–1986 và 1996–2003) với thời gian sống thêm trung bình khi đã có triệu chứng tại chỗ (≤ 18 tháng), hoặc nhầm tỉ lệ chuyển dịch thể vảy (90% thập niên 70) sang thể tuyến (60–70% gần đây).",
        f"1) <b>Sống thêm trung bình (có triệu chứng tại chỗ):</b> Không lớn hơn {Y('18 tháng')}.<br>"
        f"2) <b>Sống 5 năm tại Mỹ:</b> Khoảng {Y('5%')} (1975–1977), tăng {Y('10%')} (1984–1986) và {Y('10%')} (1996–2003).<br>"
        f"3) <b>Xu hướng mô học:</b> Thập niên 70 khoảng {Y('90%')} là biểu mô vảy; gần đây biểu mô tuyến tăng chiếm {Y('60%–70%')}.",
        "Đọc kỹ mốc hỏi trong đề thi: sống thêm trung bình tính bằng tháng (≤ 18 tháng) ở ca có triệu chứng, còn sống 5 năm là tỉ lệ % theo từng giai đoạn thống kê tại Mỹ.",
        "B1.02, B1.06, B1.07", ["Nguong-so", "Dich-te"],
    ),
    cloze(
        "SURG20B-B1-05", "B1", "Con số dịch tễ",
        f"Thời gian sống thêm trung bình của bệnh nhân ung thư thực quản đã có triệu chứng tại chỗ không lớn hơn {clz(1, Y('18 tháng'))}.",
        "B1.02", ["Nguong-so"],
    ),
    cloze(
        "SURG20B-B1-06", "B1", "Con số dịch tễ Mỹ",
        f"Tại Mỹ năm 2008, ung thư thực quản có tuổi trung bình là {clz(1, Y('69'))}, hiếm gặp dưới {clz(2, Y('25 tuổi'))}; nam nhiều gấp {clz(3, Y('4 lần'))} nữ, riêng ung thư biểu mô tuyến nam gấp {clz(4, Y('8–9 lần'))} nữ.",
        "B1.05", ["Nguong-so", "Dich-te-My"],
    ),
    cloze(
        "SURG20B-B1-07", "B1", "Con số dịch tễ Việt Nam",
        f"Theo số liệu GLOBOCAN 2008 tại Việt Nam, ung thư thực quản có khoảng {clz(1, Y('1.511 ca mới mắc') + ' và ' + R('1.157 ca tử vong'))}, tỷ lệ mắc chuẩn và tử vong chuẩn theo tuổi lần lượt là {clz(2, Y('1,9/100.000') + ' và ' + R('1,4/100.000 dân'))}.",
        "B1.08", ["Nguong-so", "Viet-Nam"],
    ),

    # ============================================================
    # B2. NHẮC LẠI GIẢI PHẪU THỰC QUẢN
    # ============================================================
    basic(
        "SURG20B-B2-01", "B2", "Giải phẫu đại cương thực quản", 1,
        f"{B('[Giải phẫu thực quản]')} Chiều dài, mốc khoảng cách tính từ {B('cung răng')}, {B('miệng thực quản')} là gì, và cấu trúc đoạn cuối chống trào ngược gồm những thành phần nào?",
        f"1) <b>Kích thước &amp; mốc cung răng:</b> Ống cơ dài {Y('25–30 cm')}, đi từ miệng thực quản (cách cung răng khoảng {Y('15 cm')}) đến tâm vị (cách cung răng khoảng {Y('40 cm')}).<br>"
        f"2) <b>Miệng thực quản:</b> Còn gọi là {B('miệng Kilian')}, được bao bọc bởi các cơ co thắt hầu tạo thành 1 khe; hai đầu khe là các {B('xoang lê')} của hầu.<br>"
        f"3) <b>Vị trí &amp; đoạn cuối:</b> Phần lớn nằm trong lồng ngực; {Y('2–4 cm')} cuối nằm dưới {B('van Gubaroff')} và {B('góc His')} chống lại sự trào ngược dịch dạ dày lên thực quản.",
        "Mốc 15 cm (miệng Kilian) và 40 cm (tâm vị) là thước đo chuẩn khi nội soi xác định vị trí khối u, từ đó quy đổi trực tiếp ra 1/3 trên, giữa hay dưới.",
        "B2.01, B2.02", ["Giai-phau"],
    ),
    basic(
        "SURG20B-B2-02", "B2", "Chỗ hẹp sinh lý thực quản", 1,
        f"{B('[Giải phẫu thực quản]')} Kể tên {Y('4 chỗ hẹp sinh lý')} của thực quản từ trên xuống dưới?",
        f"1) {B('Sụn nhẫn')}.<br>"
        f"2) {B('Quai động mạch chủ')}.<br>"
        f"3) {B('Phế quản trái')}.<br>"
        f"4) {B('Cơ hoành')}.",
        "Tại 4 chỗ hẹp sinh lý này, dị vật hay hóa chất dễ mắc lại gây tổn thương niêm mạc, đồng thời là các mốc có nguy cơ thủng cao nhất khi đưa ống soi hoặc dụng cụ nong thực quản.",
        "B2.03", ["Giai-phau", "Cho-hep"],
    ),
    basic(
        "SURG20B-B2-03", "B2", "Phân đoạn giải phẫu & lâm sàng", 1,
        f"{B('[Phân đoạn thực quản]')} Phân chia {Y('4 đoạn theo giải phẫu học')} (giới hạn, chiều dài) và {Y('3 đoạn trên lâm sàng')} tính từ {B('cung răng')} như thế nào?",
        f"1) <b>4 đoạn giải phẫu học:</b><br>"
        f"• {B('Đoạn cổ')}: từ ngang sụn nhẫn đến bờ trên hõm ức, dài {Y('5–6 cm')}.<br>"
        f"• {B('Đoạn ngực')}: dài {Y('16–25 cm')}, tiếp theo đoạn trên đến ngang cơ hoành.<br>"
        f"• {B('Đoạn hoành')}: dài {Y('1–1,5 cm')}, chui qua lỗ thực quản của cơ hoành, gắn chặt vào cơ hoành bởi các sợi và mô liên kết.<br>"
        f"• {B('Đoạn bụng')}: dài {Y('2–3 cm')}, từ lỗ cơ hoành đến lỗ tâm vị dạ dày.<br>"
        f"2) <b>3 đoạn lâm sàng (tính từ cung răng):</b><br>"
        f"• {B('1/3 trên')}: {Y('15–25 cm')}.<br>"
        f"• {B('1/3 giữa')}: {Y('26–32 cm')}.<br>"
        f"• {B('1/3 dưới')}: {Y('33 cm')} đến cơ thắt tâm vị.",
        "4 đoạn giải phẫu định hướng đường mổ (cổ, ngực, bụng), còn 3 đoạn tính từ cung răng là quy ước trên nội soi tiêu hóa để chọn phác đồ theo vị trí 1/3 trên – giữa – dưới.",
        "B2.04, B2.05", ["Giai-phau", "Phan-doan"],
    ),
    basic(
        "SURG20B-B2-04", "B2", "Mạch máu thực quản", 2,
        f"{B('[Mạch máu thực quản]')} Thực quản nhận máu từ các {B('động mạch')} nào, và máu {R('tĩnh mạch')} của từng đoạn 1/3 đổ về đâu?",
        f"1) <b>Tưới máu động mạch:</b> Từ các nhánh nhỏ của {B('động mạch chủ ngực')}: các nhánh của {B('động mạch hoành dưới')}, {B('động mạch vành vị')}, {B('động mạch giáp dưới')} và {B('động mạch thực quản giữa')}.<br>"
        f"2) <b>Dẫn lưu tĩnh mạch theo 3 đoạn:</b><br>"
        f"• {B('1/3 trên')} → đổ vào {R('tĩnh mạch chủ trên')}.<br>"
        f"• {B('1/3 giữa')} → đổ vào {R('tĩnh mạch Azygos')}.<br>"
        f"• {B('1/3 dưới')} → đổ vào {R('tĩnh mạch cửa')} (qua các tĩnh mạch dạ dày).",
        "Hệ tĩnh mạch phân vùng giải thích hướng di căn đường máu và vòng nối cửa–chủ tại 1/3 dưới: u 1/3 dưới theo tĩnh mạch cửa về gan, còn 1/3 trên và giữa đổ về tĩnh mạch chủ trên và Azygos.",
        "B2.06, B2.07", ["Giai-phau", "Mach-mau"],
    ),
    basic(
        "SURG20B-B2-05", "B2", "Thần kinh & Cấu trúc thành", 2,
        f"{B('[Thần kinh & Thành thực quản]')} Mô tả chi phối {B('thần kinh phó giao cảm')}, {B('thần kinh giao cảm')} (lưu ý vai trò vận động) và {Y('4 lớp thành thực quản')} từ trong ra ngoài?",
        f"1) <b>Thần kinh phó giao cảm:</b> Bắt đầu từ {B('dây X')} và các nhánh của nó, tiếp nối với {B('đám rối thần kinh Auerbach')}.<br>"
        f"2) <b>Thần kinh giao cảm:</b> Bắt nguồn từ các {B('rễ cổ lưng')}, tiếp nối ở hạch cổ trên, giữa và {B('hạch sao ngực')} để tới thực quản; {R('không tham gia vận động')}, chỉ có tác động {B('dẫn truyền cảm giác')}.<br>"
        f"3) <b>Cấu trúc thành thực quản (4 lớp từ trong ra ngoài):</b> 1) {B('Niêm mạc')}; 2) {B('Dưới niêm mạc')}; 3) {B('Lớp cơ')}; 4) {B('Lớp thanh mạc')}.",
        "Đám rối Auerbach điều phối nhu động cơ thành thực quản, còn thần kinh giao cảm chỉ dẫn truyền cảm giác. Khi làm bài thi phải liệt kê đúng đủ 4 lớp từ trong ra ngoài theo đúng barem.",
        "B2.08, B2.09", ["Giai-phau", "Than-kinh", "Thanh-thuc-quan"],
    ),
    trap(
        "SURG20B-B2-06", "B2", "Bẫy giải phẫu thần kinh & phân đoạn",
        "Nhầm thần kinh giao cảm có tham gia vận động nhu động thực quản, hoặc nhầm lẫn chiều dài đoạn hoành (1–1,5 cm) với đoạn bụng (2–3 cm) và đoạn cổ (5–6 cm).",
        f"1) <b>Thần kinh giao cảm:</b> {R('Không tham gia vào chức năng vận động')} của thực quản, {B('chỉ có tác động dẫn truyền cảm giác')}; vận động do dây X tiếp nối đám rối {B('Auerbach')}.<br>"
        f"2) <b>Chiều dài 4 đoạn giải phẫu:</b> Cổ {Y('5–6 cm')}, ngực {Y('16–25 cm')}, hoành {Y('1–1,5 cm')} (gắn chặt vào cơ hoành bởi các sợi và mô liên kết), bụng {Y('2–3 cm')}.",
        "Câu hỏi trắc nghiệm rất hay đánh bẫy vai trò vận động của hệ giao cảm và hoán đổi con số chiều dài đoạn hoành (1–1,5 cm) với đoạn bụng (2–3 cm).",
        "B2.04, B2.08", ["Giai-phau", "Than-kinh"],
    ),
    cloze(
        "SURG20B-B2-07", "B2", "Thuật ngữ giải phẫu",
        f"Miệng thực quản còn được gọi là {clz(1, B('miệng Kilian'))}, được bao bọc bởi các cơ co thắt hầu tạo thành khe có hai đầu là các {clz(2, B('xoang lê'))}.",
        "B2.02", ["Giai-phau", "Thuat-ngu"],
    ),
    cloze(
        "SURG20B-B2-08", "B2", "Chỗ hẹp sinh lý",
        f"Thực quản có 4 chỗ hẹp sinh lý tương ứng với {clz(1, B('sụn nhẫn, quai động mạch chủ, phế quản trái và cơ hoành'))}.",
        "B2.03", ["Giai-phau", "Cho-hep"],
    ),
    cloze(
        "SURG20B-B2-09", "B2", "Khoảng cách giải phẫu",
        f"Trên thực tế lâm sàng tính từ cung răng: 1/3 trên nằm trong khoảng {clz(1, Y('15–25 cm'))}, 1/3 giữa {clz(2, Y('26–32 cm'))}, và 1/3 dưới {clz(3, Y('33 cm đến cơ thắt tâm vị'))}.",
        "B2.05", ["Giai-phau", "Nguong-so"],
    ),

    # ============================================================
    # B3. NHẮC LẠI SINH LÝ THỰC QUẢN
    # ============================================================
    basic(
        "SURG20B-B3-01", "B3", "Sinh lý thực quản", 1,
        f"{B('[Sinh lý thực quản]')} Kể {Y('hai chức năng chính')} của thực quản và bộ phận đảm nhiệm từng chức năng?",
        f"1) <b>Chức năng vận chuyển:</b> Đưa viên nuốt từ thực quản đến dạ dày, hoàn thành nhờ {G('các cơ nhu động')} của thực quản.<br>"
        f"2) <b>Chức năng ngăn dòng trào ngược:</b> Ngăn dòng chảy ngược các chất chứa trong dạ dày-ruột, được ngăn bởi {B('hai cơ thắt của thực quản')} (vẫn đóng giữa các lần nuốt).",
        "Sự phối hợp giữa nhu động đẩy xuôi chiều và hai cơ thắt đóng kín giữa các lần nuốt giúp bảo vệ niêm mạc khỏi dịch dạ dày và tránh trào ngược hít sặc.",
        "B3.01", ["Sinh-ly"],
    ),
    basic(
        "SURG20B-B3-02", "B3", "Cơ chế hai cơ thắt", 2,
        f"{B('[Sinh lý cơ thắt thực quản]')} Phân tích cơ chế đóng – mở của {B('cơ thắt thực quản trên')}, {B('cơ thắt thực quản dưới')} và {G('cơ chế bổ sung')} của cơ hoành?",
        f"1) <b>Cơ thắt thực quản trên:</b> Luôn đóng nhờ tính đàn hồi của thành và trương lực {B('cơ nhẫn hầu')} và các {B('cơ hầu dưới')}. Khi nuốt: ức chế co cơ nhẫn hầu, dãn cơ hầu dưới và thanh quản di chuyển ra trước nhờ {B('các cơ trên móng')}.<br>"
        f"2) <b>Cơ thắt thực quản dưới:</b> Đóng phần lớn nhờ {B('trương lực cơ sinh nội tại')}. Các sợi {B('đối giao cảm trước hạch')} trong dây phế vị và các {B('nơron ức chế/kích thích sau hạch')} trong thành thực quản phân bố vào cơ thắt dưới gây thư giãn và co tương ứng.<br>"
        f"3) <b>Cơ chế bổ sung:</b> {G('Các cột cơ hoành')} bao quanh cơ thắt dưới; áp lực trong cơ thắt dưới giảm phản xạ trong {B('phản xạ ợ hơi')} và {B('căng dạ dày')}.",
        "Nhờ đối giao cảm trước hạch dây X + nơron ức chế/kích thích sau hạch thành thực quản mà LES mở nhịp nhàng khi viên nuốt tới. Suy yếu trương lực cơ sinh nội tại hoặc cột cơ hoành tạo điều kiện cho trào ngược GERD kéo dài.",
        "B3.02, B3.03, B3.04", ["Sinh-ly", "Co-che"],
        asks=["cơ thắt thực quản trên", "cơ thắt thực quản dưới", "cơ chế bổ sung"],
    ),
    trap(
        "SURG20B-B3-03", "B3", "Bẫy cơ chế đóng cơ thắt dưới",
        "Cho rằng cơ thắt thực quản dưới đóng chủ yếu nhờ các cột cơ hoành bao quanh, hoặc áp lực cơ thắt dưới tăng lên khi ợ hơi và căng dạ dày.",
        f"1) <b>Vai trò chính:</b> Cơ thắt thực quản dưới đóng phần lớn nhờ {B('trương lực cơ sinh nội tại')} của nó.<br>"
        f"2) <b>Vai trò cơ hoành &amp; phản xạ:</b> {G('Các cột cơ hoành')} chỉ là cơ chế bổ sung; áp lực trong cơ thắt dưới {R('giảm một cách phản xạ')} trong thời gian {B('phản xạ ợ hơi và căng dạ dày')}.",
        "Khi dạ dày căng hơi hoặc dịch, phản xạ làm giãn (giảm áp lực) cơ thắt dưới để thoát khí; nếu cơ chế này kéo dài quá mức sẽ thúc đẩy trào ngược mạn tính.",
        "B3.03, B3.04", ["Sinh-ly", "Co-that-duoi"],
    ),
    cloze(
        "SURG20B-B3-04", "B3", "Sinh lý cơ thắt",
        f"Cơ chế bổ sung cho cơ thắt thực quản dưới là {clz(1, G('các cột cơ hoành bao quanh'))}, và áp lực cơ thắt dưới giảm phản xạ khi {clz(2, B('ợ hơi và căng dạ dày'))}.",
        "B3.04", ["Sinh-ly", "Thuat-ngu"],
    ),

    # ============================================================
    # B4. BỆNH NGUYÊN
    # ============================================================
    basic(
        "SURG20B-B4-01", "B4", "Bệnh nguyên UT biểu mô tuyến", 1,
        f"{B('[Bệnh nguyên UT thực quản]')} Kể tên {Y('3 yếu tố nguy cơ')} của {B('ung thư biểu mô tuyến')} thực quản và yếu tố nào quan trọng nhất?",
        f"1) {R('Viêm loét thực quản Barrett (Barrett’s esophagus)')}: chủ yếu là hậu quả của viêm trào ngược dạ dày - thực quản, là {R('yếu tố nguy cơ quan trọng nhất')}.<br>"
        f"2) {R('Béo phì')}.<br>"
        f"3) {R('Hội chứng trào ngược dạ dày - thực quản (GERD)')}.",
        "🔄 <b>Chuỗi cơ chế:</b> Béo phì + suy yếu van chống trào ngược → GERD mạn tính → Tổn thương acid-mật lên 1/3 dưới → Viêm loét thực quản Barrett (yếu tố nguy cơ quan trọng nhất) → Loạn sản → Ung thư biểu mô tuyến.",
        "B4.01", ["Benh-nguyen", "Bieu-mo-tuyen"],
    ),
    basic(
        "SURG20B-B4-02", "B4", "Bệnh nguyên UT biểu mô vảy", 1,
        f"{B('[Bệnh nguyên UT thực quản]')} Liệt kê {Y('2 yếu tố chính')} và {Y('6 yếu tố khác')} gây {B('ung thư biểu mô vảy')} thực quản theo barem?",
        f"1) <b>2 yếu tố chính:</b> {R('Hút thuốc lá')} và {R('Uống rượu')}.<br>"
        f"2) <b>6 yếu tố khác:</b><br>"
        f"• {R('Sự tăng sừng hóa')}.<br>"
        f"• {R('Nhược cơ')}.<br>"
        f"• {R('Virus HPV')}.<br>"
        f"• {R('Các bệnh thuộc vùng ổ bụng')}.<br>"
        f"• {R('Môi trường làm việc ở các nhà máy tiếp xúc hóa chất')}.<br>"
        f"• {R('Loạn sản nặng')} (cần nội soi thực quản định kỳ {Y('3 tháng/lần')}).",
        "Thuốc lá và rượu là hai trụ cột bệnh nguyên hàng đầu của biểu mô vảy; 6 yếu tố khác trong barem cần ghi nhớ nguyên văn đầy đủ để không mất điểm liệt kê.",
        "B4.02, B4.03", ["Benh-nguyen", "Bieu-mo-vay"],
    ),
    trap(
        "SURG20B-B4-03", "B4", "Bẫy phân biệt bệnh nguyên tuyến vs vảy",
        "Nhầm lẫn yếu tố nguy cơ quan trọng nhất của ung thư biểu mô tuyến với ung thư biểu mô vảy (ví dụ gắn Barrett/GERD cho thể vảy hoặc hút thuốc/rượu là yếu tố chính của thể tuyến).",
        f"1) <b>UT biểu mô tuyến:</b> {R('Viêm loét thực quản Barrett')} (quan trọng nhất, hậu quả viêm trào ngược), {R('béo phì')}, {R('GERD')}.<br>"
        f"2) <b>UT biểu mô vảy:</b> Chính là {R('hút thuốc lá')} và {R('uống rượu')}, kèm 6 yếu tố khác (tăng sừng hóa, nhược cơ, virus HPV, bệnh vùng ổ bụng, nhà máy hóa chất, loạn sản nặng).",
        "Thể tuyến gắn chặt trục trào ngược acid ở 1/3 dưới (GERD – Barrett – béo phì), còn thể vảy gắn với chất kích thích tiếp xúc trực tiếp niêm mạc (thuốc lá – rượu – hóa chất).",
        "B4.01, B4.02, B4.03", ["Benh-nguyen", "So-sanh"],
    ),
    trap(
        "SURG20B-B4-04", "B4", "Cảnh báo loạn sản nặng",
        "Phát hiện loạn sản nặng ở thực quản nhưng chỉ dặn bệnh nhân khám lại mỗi năm hoặc khi có nuốt nghẹn sẽ dẫn tới hậu quả gì, và xử trí mốc nội soi đúng là bao lâu?",
        f"1) <b>Hậu quả:</b> Bỏ lỡ cửa sổ can thiệp giai đoạn tiền ung thư trước khi tiến triển thành {R('ung thư biểu mô xâm nhập giai đoạn muộn')}.<br>"
        f"2) <b>Xử trí bắt buộc:</b> Phải nội soi thực quản định kỳ {Y('3 tháng/lần')} khi có {R('loạn sản nặng')}.",
        "Loạn sản nặng là ngưỡng báo động sát ung thư tại chỗ; theo dõi 3 tháng/lần giúp phát hiện chuyển dạng ác tính ngay khi chưa xâm lấn lớp cơ.",
        "B4.03", ["Loan-san-nang", "Theo-doi"], red_flag=True, asks=["Hậu quả", "Xử trí"],
    ),
    cloze(
        "SURG20B-B4-05", "B4", "Ngưỡng theo dõi",
        f"Bệnh nhân có tổn thương {clz(1, R('loạn sản nặng'))} ở thực quản cần nội soi thực quản định kỳ {clz(2, Y('3 tháng/lần'))}.",
        "B4.03", ["Nguong-so", "Loan-san"],
    ),

    # ============================================================
    # B5. GIẢI PHẪU BỆNH
    # ============================================================
    basic(
        "SURG20B-B5-01", "B5", "Giải phẫu bệnh đại thể & vi thể", 1,
        f"{B('[Giải phẫu bệnh UT thực quản]')} Tổn thương khởi đầu đại thể có màu sắc gì, phân chia {Y('3 dạng đại thể')} (tỉ lệ %) và {B('vi thể')} ra sao?",
        f"1) <b>Khởi đầu đại thể:</b> Một vùng dày lên của niêm mạc có màu {B('trắng xám')}; sau vài tháng đến vài năm phát triển thành 3 dạng (riêng biệt hoặc phối hợp):<br>"
        f"• {B('Dạng chồi sùi nhô vào lòng ống')} ({Y('60%')}): hay gặp nhất.<br>"
        f"• {R('Dạng loét')} ({Y('25%')}): u hoại tử, ăn sâu xuống dưới → có thể làm {R('thủng cây phế quản, động mạch chủ hoặc màng bao tim')}.<br>"
        f"• {B('Dạng thâm nhiễm lan tỏa')} ({Y('15%')}): làm dày cứng thành thực quản và hẹp lòng ống.<br>"
        f"2) <b>Vi thể:</b> Hầu hết là {B('ung thư biểu mô')} ({B('biểu mô tuyến')} hoặc {B('biểu mô vảy')}); ít hơn {Y('1%')} là lymphoma, u hắc tố (melanoma), ung thư tế bào nhỏ...",
        "Ba hình thái đại thể quyết định biến chứng lâm sàng: chồi sùi (60%) sớm bít lòng ống gây nuốt nghẹn; loét (25%) dễ xuất huyết và ăn thủng tạng trung thất; thâm nhiễm (15%) làm xơ cứng thành ống.",
        "B5.01, B5.02", ["Giai-phau-benh", "Dai-the", "Vi-the"],
    ),
    trap(
        "SURG20B-B5-02", "B5", "Biến chứng đe dọa tính mạng của dạng loét",
        "Phân tích cơ chế bệnh sinh và biến chứng thủng của khối u thực quản dạng loét (25%) vào các cấu trúc sống còn trong trung thất?",
        f"1) <b>Cơ chế bệnh sinh:</b> Khối u bị {R('hoại tử và ăn sâu xuống dưới')} xuyên thành thực quản.<br>"
        f"2) <b>Biến chứng thủng:</b> Có thể làm thủng {R('cây phế quản')} (dò khí–phế quản–thực quản), {R('động mạch chủ')} (chảy máu ồ ạt tử vong), hoặc {R('màng bao tim')} (viêm mủ/chèn ép màng tim).",
        "Thực quản nằm kẹp sát sau khí–phế quản, cạnh động mạch chủ xuống và sau màng tim. U dạng loét ăn sâu rất dễ tạo đường dò chết người vào các tạng này.",
        "B5.01", ["Bien-chung", "Dang-loet"], red_flag=True, asks=["Cơ chế bệnh sinh", "Biến chứng thủng"],
    ),
    cloze(
        "SURG20B-B5-03", "B5", "Tỉ lệ 3 dạng đại thể",
        f"Về đại thể, ung thư thực quản phát triển thành 3 dạng: {clz(1, B('dạng chồi sùi nhô vào lòng ống (60%), dạng loét (25%) và dạng thâm nhiễm lan tỏa (15%)'))}.",
        "B5.01", ["Dai-the", "Nguong-so"],
    ),
    cloze(
        "SURG20B-B5-04", "B5", "Tỉ lệ vi thể hiếm",
        f"Các loại mô học hiếm gặp như lymphoma, u hắc tố (melanoma) và ung thư tế bào nhỏ chỉ chiếm {clz(1, Y('ít hơn 1%'))} tổng số ung thư thực quản.",
        "B5.02", ["Vi-the", "Nguong-so"],
    ),

    # ============================================================
    # B6. TRIỆU CHỨNG LÂM SÀNG
    # ============================================================
    basic(
        "SURG20B-B6-01", "B6", "Triệu chứng toàn thân", 1,
        f"{B('[Lâm sàng — Toàn thân]')} Biểu hiện toàn thân của ung thư thực quản ở {B('giai đoạn đầu')} và {R('giai đoạn sau')} gồm những gì?",
        f"1) <b>Giai đoạn đầu:</b> Thường {Y('không có biểu hiện gì đặc biệt')}.<br>"
        f"2) <b>Giai đoạn sau:</b><br>"
        f"• {R('Sụt cân nhanh chóng')} do bệnh nhân không ăn uống được.<br>"
        f"• {R('Hội chứng thở ống')}.<br>"
        f"• {R('Hạch thượng đòn trái (hạch Virchow - Troisier)')}.",
        "Giai đoạn đầu hoàn toàn thầm lặng khiến đa số bệnh nhân đi khám muộn. Hạch Virchow - Troisier ở hố thượng đòn trái là dấu hiệu kinh điển do bạch huyết từ vùng bụng–ngực đổ qua ống ngực lên hội lưu tĩnh mạch trái.",
        "B6.01", ["Lam-sang", "Toan-than"],
    ),
    basic(
        "SURG20B-B6-02", "B6", "Triệu chứng cơ năng — Nuốt nghẹn", 1,
        f"{B('[Lâm sàng — Cơ năng]')} Mô tả tần suất, đặc điểm cảm giác ban đầu và diễn tiến kinh điển của triệu chứng {R('nuốt nghẹn')}?",
        f"1) <b>Tần suất &amp; ý nghĩa giai đoạn:</b> Gặp tới {Y('90%')}, là triệu chứng chính nhưng thường xuất hiện ở {R('giai đoạn muộn')}.<br>"
        f"2) <b>Cảm giác ban đầu:</b> Tức nghẹn khi nuốt, vật nuốt dừng lại {R('sau xương ức')}, uống nước thì cảm giác này mất đi.<br>"
        f"3) <b>Diễn tiến đặc trưng:</b> {R('Nghẹn tăng dần')} — lúc đầu nghẹn {B('thức ăn đặc')}, về sau nghẹn cả {R('thức ăn lỏng và nước uống')}.",
        "🔄 <b>Chuỗi cơ chế:</b> Khối u lấp dần lòng thực quản → Ban đầu viên thức ăn rắn mắc lại, nước vẫn lách qua giúp đẩy trôi → U chiếm gần trọn chu vi → Tắc khít → Nghẹn cả thức ăn lỏng và nước → Sụt cân suy kiệt.",
        "B6.02", ["Lam-sang", "Co-nang", "Nuot-nghen"],
    ),
    basic(
        "SURG20B-B6-03", "B6", "Triệu chứng muộn & Thực thể", 2,
        f"{B('[Lâm sàng — Giai đoạn muộn]')} Kể {Y('6 nhóm triệu chứng cơ năng muộn')} (kèm giải thích khàn tiếng/hơi thở hôi) và các dấu hiệu {R('thực thể')} giai đoạn muộn?",
        f"1) <b>6 triệu chứng cơ năng muộn:</b><br>"
        f"• {R('Ợ, trào ngược thức ăn qua đường miệng')} (do ứ đọng và giãn thực quản trên u).<br>"
        f"• {R('Cơn nấc hoặc đau quặn sau xương ức')}.<br>"
        f"• {R('Nuốt khó, nuốt đau')}.<br>"
        f"• {R('Nôn máu')}.<br>"
        f"• {R('Khàn tiếng')} (do u xâm lấn {B('thần kinh quặt ngược thanh quản')}).<br>"
        f"• {R('Khó thở, hơi thở có mùi hôi thối')} (do khối u hoại tử).<br>"
        f"2) <b>Thực thể giai đoạn muộn:</b> Sờ thấy {R('khối u di căn gan')}, {R('tràn dịch màng phổi')}, dấu hiệu {R('di căn xương')}, {R('hạch ngoại vi')}.",
        "Mỗi dấu hiệu muộn tương ứng với một bước lan tỏa giải phẫu: ứ đọng đoạn trên gây ợ/trào ngược, xâm lấn dây quặt ngược thanh quản gây khàn tiếng, hoại tử gây hơi thở thối, và di căn xa biểu hiện ở gan, màng phổi, xương, hạch.",
        "B6.03, B6.04", ["Lam-sang", "Thuc-the", "Giai-doan-muon"],
    ),
    trap(
        "SURG20B-B6-04", "B6", "Cảnh báo lâm sàng giai đoạn muộn",
        "Bệnh nhân nuốt nghẹn kèm khàn tiếng hoặc sờ thấy hạch thượng đòn trái (hạch Virchow - Troisier) hoặc hơi thở mùi hôi thối báo động điều gì?",
        f"1) {R('Khàn tiếng')}: Khối u đã {R('xâm lấn thần kinh quặt ngược thanh quản')} ngoài thành thực quản.<br>"
        f"2) {R('Hạch Virchow - Troisier')}: Di căn hạch thượng đòn trái ở giai đoạn sau.<br>"
        f"3) {R('Khó thở, hơi thở mùi hôi thối')}: Khối u đã {R('hoại tử')} và chèn ép/ăn lan đường thở.",
        "Không được xem nhẹ các triệu chứng ngoài thực quản như khàn tiếng hay nấc kéo dài trên người bệnh nuốt nghẹn — đó là các chỉ điểm xâm lấn tại vùng hoặc di căn hạch muộn.",
        "B6.01, B6.03", ["Khan-tieng", "Hach-Virchow"], red_flag=True,
    ),
    trap(
        "SURG20B-B6-05", "B6", "Bẫy chờ triệu chứng thực thể",
        "Chủ quan loại trừ ung thư thực quản chỉ vì khám toàn thân và thực thể hoàn toàn bình thường (chưa sụt cân, chưa sờ thấy gan to hay hạch cổ).",
        f"1) <b>Sự thật giai đoạn đầu:</b> Toàn thân {Y('không có biểu hiện gì đặc biệt')}; khám thực thể chủ yếu chỉ thấy bất thường ở {R('giai đoạn muộn')} (gan to di căn, tràn dịch màng phổi, di căn xương, hạch ngoại vi).<br>"
        f"2) <b>Thái độ đúng:</b> Hễ có {R('cảm giác tức nghẹn dừng sau xương ức')} hoặc thuộc nhóm nguy cơ cao phải cho thăm dò ngay.",
        "Ngay cả nuốt nghẹn (gặp tới 90%) cũng thường chỉ xuất hiện khi bệnh đã vào giai đoạn muộn; chờ đến lúc khám tay thấy u gan hay hạch thượng đòn là quá trễ.",
        "B6.01, B6.02, B6.04", ["Bay-chan-doan", "Lam-sang"],
    ),
    cloze(
        "SURG20B-B6-06", "B6", "Thuật ngữ & con số lâm sàng",
        f"Trong ung thư thực quản, triệu chứng chính là {clz(1, R('nuốt nghẹn'))} (gặp tới {clz(2, Y('90%'))}), và di căn hạch thường sờ thấy ở {clz(3, R('hạch thượng đòn trái (hạch Virchow - Troisier)'))}.",
        "B6.01, B6.02", ["Lam-sang", "Nguong-so"],
    ),

    # ============================================================
    # B7. CẬN LÂM SÀNG
    # ============================================================
    basic(
        "SURG20B-B7-01", "B7", "Cận lâm sàng chẩn đoán", 1,
        f"{B('[Cận lâm sàng UT thực quản]')} Phương pháp nào là {G('tiêu chuẩn vàng')} chẩn đoán (độ chính xác), và vai trò của {B('chụp thực quản có cản quang (Barium swallow)')} là gì?",
        f"1) {G('Nội soi sinh thiết chẩn đoán')}: Là {G('tiêu chuẩn vàng')} để chẩn đoán; kết hợp nội soi và sinh thiết bờ tổn thương cho kết quả chính xác đến {Y('90%')}.<br>"
        f"2) {B('Chụp thực quản có cản quang (Barium swallow)')}: Hình ảnh u lồi vào lòng thực quản, thâm nhiễm cứng, ổ loét thành thực quản; có ích để {G('định hướng trước khi soi')}, giúp {R('tránh biến chứng thủng khi soi')}.",
        "Sinh thiết bờ tổn thương tránh mô hoại tử ở tâm loét để đạt độ chính xác tới 90%. Phim cản quang đóng vai trò bản đồ tiền trạm chỉ ra vị trí hẹp/túi thừa/loét nhằm tránh làm thủng thực quản khi đưa ống soi.",
        "B7.01, B7.02", ["Can-lam-sang", "Noi-soi", "Barium"],
    ),
    basic(
        "SURG20B-B7-02", "B7", "Cận lâm sàng đánh giá giai đoạn", 1,
        f"{B('[Cận lâm sàng đánh giá giai đoạn]')} Vai trò riêng của {B('CT ngực - bụng')}, {B('MRI')}, {B('Siêu âm nội soi (EUS)')} và {B('PET / PET-CT')} trong ung thư thực quản?",
        f"1) {B('CT Scanner ngực - bụng')}: Đánh giá xâm lấn u ra xung quanh và phát hiện di căn hạch, {R('gan (35%)')}, {R('phổi (20%)')}, {R('xương (9%)')}.<br>"
        f"2) {B('MRI')}: Cho kết quả {Y('tương đương CT')}.<br>"
        f"3) {G('Siêu âm nội soi (EUS)')}: Có giá trị rất cao đánh giá giai đoạn {B('xâm lấn tại chỗ (T)')} và {B('hạch vùng (N)')} khi chưa có di căn xa.<br>"
        f"4) {B('PET / PET-CT')}: Đánh giá toàn diện tình trạng {R('di căn toàn thân')}.",
        "EUS là mắt thần phân tách độ sâu xâm lấn từng lớp thành (T) và hạch cạnh thực quản (N) khi chưa M1, còn CT/MRI/PET-CT rà soát di căn tạng xa mà tỷ lệ hay gặp nhất trên CT là gan (35%), phổi (20%) và xương (9%).",
        "B7.03, B7.04, B7.05, B7.06", ["Can-lam-sang", "EUS", "CT", "PET"],
    ),
    trap(
        "SURG20B-B7-03", "B7", "An toàn thủ thuật nội soi & vai trò Barium",
        "Hai sai lầm ngược chiều khi dùng X-quang thực quản có cản quang: (1) kết luận chẩn đoán xác định ung thư chỉ bằng phim cản quang; (2) bỏ qua định hướng cản quang khi bệnh nhân nghẹn nặng khiến nội soi gây thủng.",
        f"1) <b>Không thay thế mô bệnh học:</b> Chụp cản quang chỉ thấy hình ảnh gián tiếp (u lồi, thâm nhiễm cứng, ổ loét), KHÔNG thể thay {G('nội soi sinh thiết')} (tiêu chuẩn vàng).<br>"
        f"2) <b>An toàn trước soi:</b> Phim cản quang có ích để {G('định hướng trước khi soi')}, giúp {R('tránh biến chứng thủng khi soi')}.",
        "Phim Barium và nội soi sinh thiết bổ sung cho nhau chứ không thay thế nhau: Barium định hướng bản đồ an toàn, nội soi sinh thiết xác lập chẩn đoán vàng.",
        "B7.01, B7.02, B8.01", ["An-toan-soi", "Tieu-chuan-vang"],
    ),
    cloze(
        "SURG20B-B7-04", "B7", "Tỷ lệ di căn trên CT",
        f"Chụp CT Scanner ngực - bụng trong ung thư thực quản giúp phát hiện di căn xa tới gan ({clz(1, Y('35%'))}), phổi ({clz(2, Y('20%'))}), và xương ({clz(3, Y('9%'))}).",
        "B7.03", ["Can-lam-sang", "Nguong-so"],
    ),
    cloze(
        "SURG20B-B7-05", "B7", "Giá trị siêu âm nội soi",
        f"Khi chưa có di căn xa, {clz(1, G('siêu âm nội soi (EUS)'))} có giá trị rất cao để đánh giá {clz(2, B('xâm lấn tại chỗ (T) và hạch vùng (N)'))}.",
        "B7.05", ["Can-lam-sang", "EUS"],
    ),

    # ============================================================
    # B8. CHẨN ĐOÁN (XÁC ĐỊNH, TNM, PHÂN BIỆT)
    # ============================================================
    basic(
        "SURG20B-B8-01", "B8", "Chẩn đoán xác định & phân biệt", 1,
        f"{B('[Chẩn đoán UT thực quản]')} {G('Chẩn đoán xác định')} dựa trên 3 trụ cột nào, và cần {B('chẩn đoán phân biệt')} với {Y('7 bệnh lý')} nào?",
        f"1) <b>Chẩn đoán xác định:</b> Lâm sàng ({R('nuốt khó, nuốt nghẹn tăng dần, gầy sút cân, hạch cổ')}) + {G('nội soi thực quản')} + {G('kết quả giải phẫu bệnh qua sinh thiết')}.<br>"
        f"2) <b>Chẩn đoán phân biệt (7 bệnh):</b><br>"
        f"• {B('Túi thừa thực quản')}.<br>"
        f"• {B('Co thắt tâm vị (Achalasia)')}.<br>"
        f"• {B('Nuốt nghẹn chức năng / rối loạn tâm thần')}.<br>"
        f"• {B('Viêm hẹp thực quản do trào ngược dạ dày')}.<br>"
        f"• {B('Sẹo hẹp thực quản do bỏng kiềm/axit')}.<br>"
        f"• {B('U trung thất hoặc cơ quan lân cận đè từ ngoài vào')}.<br>"
        f"• {B('Ung thư tâm vị, phình vị dạ dày lan lên thực quản')}.",
        "Có thể nhóm 7 bệnh phân biệt theo giải phẫu từ trong ra ngoài: lòng/niêm mạc (viêm hẹp trào ngược, sẹo bỏng kiềm/axit), thành cơ (túi thừa, achalasia, nuốt nghẹn chức năng), vùng nối (UT tâm vị–phình vị lan lên), và chèn ép ngoài thành (u trung thất).",
        "B8.01, B8.03", ["Chan-doan", "Phan-biet"], asks=["Chẩn đoán xác định", "Chẩn đoán phân biệt"],
    ),
    basic(
        "SURG20B-B8-02", "B8", "Phân loại giai đoạn TNM (0 – IIA)", 1,
        f"{B('[Bảng xếp giai đoạn TNM — phần đầu]')} Trình bày ký hiệu TNM và đặc điểm giải phẫu của {B('Giai đoạn 0, Giai đoạn I (T1a/T1b) và Giai đoạn IIA')} theo barem?",
        f"1) {B('Giai đoạn 0 (Tis N0 M0)')}: Ung thư biểu mô tại chỗ.<br>"
        f"2) {B('Giai đoạn I (T1a N0 M0 / T1b N0 M0)')}: U xâm lấn lớp {B('niêm mạc (T1a)')} hoặc {B('dưới niêm mạc (T1b)')}, chưa di căn hạch.<br>"
        f"3) {B('Giai đoạn IIA (T2/T3 N0 M0)')}: U xâm lấn {B('lớp cơ (T2)')} hoặc {B('màng bao quanh (T3)')}, chưa di căn hạch.",
        "Cả 3 bậc 0, I, IIA đều chưa di căn hạch (N0) và chưa di căn xa (M0). Ranh giới từ lớp dưới niêm mạc (T1b) sang lớp cơ (T2) quyết định việc nâng từ phẫu thuật đơn thuần lên hóa-xạ trị tiền phẫu.",
        "B8.02", ["TNM", "Giai-doan"],
    ),
    basic(
        "SURG20B-B8-03", "B8", "Phân loại giai đoạn TNM (IIB – IVB)", 1,
        f"{B('[Bảng xếp giai đoạn TNM — phần sau]')} Trình bày ký hiệu TNM và đặc điểm của {B('Giai đoạn IIB, Giai đoạn III và Giai đoạn IV (IVA, IVB)')} theo barem?",
        f"1) {B('Giai đoạn IIB (T1/T2 N1 M0)')}: U {B('T1–T2')} kèm di căn {R('hạch vùng (N1)')}.<br>"
        f"2) {B('Giai đoạn III (T3 N1 M0 / T4 N0 M0)')}: U xâm lấn sâu kèm hạch hoặc xâm lấn {R('cơ quan lân cận')}.<br>"
        f"3) {R('Giai đoạn IV (T0–4 N0/1 M1)')}: Đã có di căn xa:<br>"
        f"• {R('Giai đoạn IVA (T0–4 N0/1 M1a)')}: Di căn {R('hạch xa')}.<br>"
        f"• {R('Giai đoạn IVB (T0–4 N0/1 M1b)')}: Di căn các {R('tạng xa')} (gan, phổi, xương...).",
        "Từ IIB bắt đầu xuất hiện hạch vùng N1 (với T1–T2); giai đoạn III là u sâu có hạch (T3N1) hoặc xâm lấn cơ quan lân cận (T4N0); giai đoạn IV tách M1a (hạch xa) và M1b (tạng xa).",
        "B8.02", ["TNM", "Giai-doan"],
    ),
    trap(
        "SURG20B-B8-04", "B8", "Bẫy lâm sàng chẩn đoán phân biệt",
        "Bệnh nhân than nuốt nghẹn nhưng còn trẻ hoặc đáp ứng từng lúc với nước; nếu vội chẩn đoán là co thắt tâm vị hoặc nuốt nghẹn chức năng mà không nội soi sinh thiết thì rủi ro thế nào?",
        f"1) <b>Bẫy bỏ sót u ác:</b> {B('Co thắt tâm vị (Achalasia)')}, {B('nuốt nghẹn chức năng')} và {B('UT tâm vị/phình vị lan lên')} đều gây nuốt nghẹn dễ trùng lấp trên lâm sàng.<br>"
        f"2) <b>Nguyên tắc loại trừ bắt buộc:</b> Mọi ca nuốt nghẹn cần {G('nội soi thực quản và sinh thiết bờ tổn thương')} (tiêu chuẩn vàng, chính xác {Y('90%')}) để loại trừ ung thư trước khi kết luận lành tính.",
        "Ung thư tâm vị lan lên có thể tạo hình ảnh giả co thắt tâm vị trên phim cản quang; chỉ mô bệnh học từ sinh thiết mới phân định dứt khoát.",
        "B7.01, B8.01, B8.03", ["Chan-doan-phan-biet", "Achalasia"],
    ),
    trap(
        "SURG20B-B8-05", "B8", "Bẫy phân biệt TNM IIA vs IIB và IVA vs IVB",
        "Nhầm lẫn xếp T2 N0 M0 vào Giai đoạn IIB hoặc nhầm T3 N0 M0 vào Giai đoạn III, và nhầm di căn hạch xa (M1a) với di căn tạng xa (M1b).",
        f"1) {B('Giai đoạn IIA')}: {B('T2/T3 N0 M0')} (chưa di căn hạch).<br>"
        f"2) {B('Giai đoạn IIB')}: {B('T1/T2 N1 M0')} (u T1–T2 nhưng ĐÃ có hạch vùng N1).<br>"
        f"3) {R('Giai đoạn IVA vs IVB')}: {R('IVA (M1a)')} là di căn hạch xa, còn {R('IVB (M1b)')} là di căn các tạng xa (gan, phổi, xương...).",
        "Nhớ mẹo chia giai đoạn theo barem: IIA còn N0 (T2/T3); IIB đã nhảy sang N1 (T1/T2); III có T3N1 hoặc T4N0; IV chia M1a = hạch xa, M1b = tạng xa.",
        "B8.02", ["TNM", "Bay-phan-giai-doan"],
    ),
    cloze(
        "SURG20B-B8-06", "B8", "Phân biệt TNM trong barem",
        f"Trong bảng phân giai đoạn TNM theo barem: Giai đoạn IIA là {clz(1, B('T2/T3 N0 M0'))} (u xâm lấn lớp cơ T2 hoặc màng bao quanh T3, chưa hạch), còn Giai đoạn IIB là {clz(2, B('T1/T2 N1 M0'))} (u T1–T2 kèm hạch vùng N1).",
        "B8.02", ["TNM", "Nguong-so"],
    ),

    # ============================================================
    # B9. ĐIỀU TRỊ
    # ============================================================
    basic(
        "SURG20B-B9-01", "B9", "Nguyên tắc & Phác đồ theo giai đoạn", 1,
        f"{B('[Điều trị UT thực quản]')} Nêu {G('nguyên tắc điều trị')} chung và phác đồ đặc hiệu cho {B('giai đoạn rất sớm')}, {B('giai đoạn I')} và {B('giai đoạn II, III')} (kèm chuẩn diện cắt)?",
        f"1) <b>Nguyên tắc chung:</b> {G('Điều trị đa mô thức')}, phối hợp chặt chẽ giữa {G('phẫu thuật, xạ trị và hóa trị')}.<br>"
        f"2) <b>Giai đoạn rất sớm (chưa xâm lấn lớp cơ):</b> {G('Cắt hớt niêm mạc qua nội soi (EMR/ESD)')}, {G('laser')} hoặc {G('quang đông lạnh (cryotherapy)')}.<br>"
        f"3) <b>Giai đoạn I:</b> {G('Phẫu thuật cắt thực quản triệt căn')}, tạo hình {G('ống cuốn dạ dày')} đưa lên thay thế.<br>"
        f"4) <b>Giai đoạn II, III:</b> Phối hợp {G('hóa - xạ trị tiền phẫu')} sau đó phẫu thuật; diện cắt triệt căn phải {Y('cách u > 5 cm')}, đạt {G('diện cắt âm tính (R0)')} và {G('nạo vét hạch vùng triệt để')}.",
        "Vì tế bào ung thư dễ lan xa theo mạng bạch mạch dưới niêm mạc, phẫu thuật triệt căn đòi hỏi diện cắt cách u > 5 cm đạt R0 và vét hạch triệt để.",
        "B9.01, B9.02", ["Dieu-tri", "Phau-thuat"],
    ),
    basic(
        "SURG20B-B9-02", "B9", "Chiến lược theo vị trí khối u", 1,
        f"{B('[Phẫu thuật theo vị trí giải phẫu]')} So sánh chiến lược điều trị giữa u ở {B('đoạn cổ')}, {B('1/3 trên')}, {B('1/3 giữa')} và {B('1/3 dưới')} thực quản?",
        f"1) <b>Đoạn cổ:</b> Cắt thực quản nguyên khối với {G('hạ họng - thanh quản')}, {R('mở khí quản vĩnh viễn')}, tái tạo ống tiêu hóa bằng {G('vạt ruột non vi phẫu')} hoặc {G('kéo đại tràng lên')}.<br>"
        f"2) <b>1/3 trên:</b> Khó cắt rộng triệt căn, nguy cơ tai biến cao → {G('Xạ trị / Hóa xạ đồng thời')} được ưu tiên hàng đầu.<br>"
        f"3) <b>1/3 giữa:</b> {G('Cắt thực quản toàn bộ')}, tái tạo đường tiêu hóa bằng {G('dạ dày hoặc quai đại tràng')} đưa lên ngực/cổ, kết hợp {G('xạ trị và hóa chất')}.<br>"
        f"4) <b>1/3 dưới:</b> Phẫu thuật {G('cắt đoạn thực quản dưới và cực trên dạ dày')}, lập lại lưu thông tiêu hóa bằng {G('nối dạ dày - thực quản trong lồng ngực')}.",
        "Vị trí khối u quyết định trực tiếp cơ quan tái tạo và đường mổ: đoạn cổ phải cắt kèm hạ họng-thanh quản và mở khí quản vĩnh viễn; 1/3 trên ưu tiên hóa xạ đồng thời thay vì cố mổ; 1/3 giữa cắt toàn bộ thực quản; 1/3 dưới cắt đoạn dưới + cực trên dạ dày nối trong lồng ngực.",
        "B9.03", ["Dieu-tri", "Phau-thuat-vi-tri"],
    ),
    basic(
        "SURG20B-B9-03", "B9", "Điều trị giảm nhẹ & Kỹ thuật xạ trị", 2,
        f"{B('[Điều trị giảm nhẹ giai đoạn muộn]')} Kể {Y('5 biện pháp giảm nhẹ và kỹ thuật xạ trị hiện đại')} cho bệnh nhân có {R('di căn xa')} hoặc mất khả năng ăn đường miệng?",
        f"1) {G('Hóa chất toàn thân')} hoặc {G('chăm sóc giảm nhẹ')}.<br>"
        f"2) {G('Xạ trị giảm nhẹ')} triệu chứng {R('đau, chảy máu')}.<br>"
        f"3) Đặt {G('stent kim loại tự nở')} lòng thực quản để giải quyết nuốt nghẹn.<br>"
        f"4) {G('Mở thông dạ dày hoặc hỗng tràng nuôi dưỡng')} khi không còn khả năng ăn qua đường miệng.<br>"
        f"5) Kỹ thuật xạ trị hiện đại: {B('IMRT')} (xạ trị điều biến liều) và {B('VMAT')} (xạ trị quay điều biến thể tích) giúp kiểm soát u tốt và {G('giảm tối đa biến chứng mô lành')}.",
        "Ở bệnh nhân đã M1, không đặt vấn đề mổ triệt căn mà tập trung cải thiện chất lượng sống, duy trì dinh dưỡng (stent hoặc mở thông) và bảo vệ tim-phổi bằng xạ trị điều biến liều IMRT/VMAT.",
        "B9.04", ["Dieu-tri", "Giam-nhe", "IMRT", "VMAT"],
    ),
    trap(
        "SURG20B-B9-04", "B9", "Bẫy chỉ định phẫu thuật 1/3 trên & diện cắt R0",
        "Hai sai lầm phẫu thuật nghiêm trọng: (1) cố cắt rộng triệt căn u 1/3 trên bằng mọi giá; (2) mổ thẳng giai đoạn II–III không hóa-xạ tiền phẫu hoặc cắt sát u ≤ 5 cm.",
        f"1) <b>U 1/3 trên:</b> Do khó cắt rộng triệt căn và nguy cơ tai biến cao → {G('xạ trị / hóa xạ đồng thời')} là lựa chọn ưu tiên hàng đầu.<br>"
        f"2) <b>Giai đoạn II–III:</b> Bắt buộc phối hợp {G('hóa - xạ trị tiền phẫu')} trước phẫu thuật; diện cắt triệt căn phải {Y('cách u > 5 cm')}, đạt {G('diện cắt âm tính (R0)')} và {G('nạo vét hạch vùng triệt để')}.",
        "Cố mổ u 1/3 trên dễ gây tai biến đường thở – mạch máu lớn và khó đạt R0; còn ở giai đoạn II–III, hóa xạ tiền phẫu làm giảm kích thước u giúp tăng tỉ lệ cắt sạch R0 (> 5 cm).",
        "B9.02, B9.03", ["Bay-phau-thuat", "R0"],
    ),
    trap(
        "SURG20B-B9-05", "B9", "Cờ đỏ chọn sai chỉ định cực đoan theo giai đoạn",
        "Chỉ định cắt thực quản triệt căn cho tổn thương rất sớm chưa xâm lấn lớp cơ, HOẶC chỉ định cắt thực quản triệt căn khi bệnh nhân đã có di căn xa (M1).",
        f"1) <b>Tổn thương rất sớm (chưa xâm lấn lớp cơ):</b> Điều trị bảo tồn bằng {G('cắt hớt niêm mạc qua nội soi (EMR/ESD)')}, {G('laser')} hoặc {G('quang đông lạnh (cryotherapy)')}, tránh đại phẫu nặng nề.<br>"
        f"2) <b>Giai đoạn muộn đã có di căn xa (M1):</b> Chống chỉ định mổ triệt căn nặng nề vô ích; chuyển sang {G('điều trị giảm nhẹ')} (hóa chất toàn thân, xạ giảm đau/chảy máu, stent tự nở, mở thông nuôi dưỡng).",
        "Phẫu thuật cắt thực quản là đại phẫu ngực–bụng tỷ lệ biến chứng cao: quá tay ở giai đoạn tại chỗ (EMR/ESD làm được) hoặc cố mổ ở giai đoạn M1 đều gây hại cho người bệnh.",
        "B9.02, B9.04", ["Co-do", "Chi-dinh-mo"], red_flag=True,
    ),
    cloze(
        "SURG20B-B9-06", "B9", "Chuẩn diện cắt phẫu thuật",
        f"Trong phẫu thuật triệt căn ung thư thực quản, diện cắt phải cách u {clz(1, Y('> 5 cm'))}, đạt diện cắt âm tính ({clz(2, G('R0'))}) và nạo vét hạch vùng triệt để.",
        "B9.02", ["Phau-thuat", "Nguong-so"],
    ),

    # ============================================================
    # B10. PHÒNG BỆNH VÀ THEO DÕI
    # ============================================================
    basic(
        "SURG20B-B10-01", "B10", "Phòng bệnh & Theo dõi sau mổ", 1,
        f"{B('[Phòng bệnh & Theo dõi UT thực quản]')} Trình bày biện pháp {G('phòng bệnh cấp 1')}, {G('phòng bệnh cấp 2')} và {Y('lịch + thăm dò theo dõi')} sau phẫu thuật triệt căn?",
        f"1) <b>Phòng bệnh cấp 1:</b> {G('Bỏ thuốc lá')}, {G('hạn chế rượu bia')}, {G('điều trị dứt điểm GERD')}, {G('kiểm soát cân nặng')}.<br>"
        f"2) <b>Phòng bệnh cấp 2:</b> {G('Tầm soát phát hiện sớm')} ở nhóm nguy cơ cao ({R('loạn sản Barrett')}, gia đình có người mắc, người nghiện rượu thuốc lá lâu năm).<br>"
        f"3) <b>Lịch theo dõi sau phẫu thuật triệt căn:</b><br>"
        f"• Năm đầu tiên: khám lâm sàng và xét nghiệm cơ bản định kỳ {Y('4 tháng/lần')}.<br>"
        f"• 2 năm tiếp theo: định kỳ {Y('6 tháng/lần')}.<br>"
        f"4) <b>Thăm dò định kỳ:</b> Chụp {B('X-quang phổi')}, {B('CT ngực - bụng')}, {G('nội soi thực quản dạ dày kiểm tra miệng nối')}.",
        "Phòng bệnh cấp 1 đánh vào yếu tố nguy cơ sửa được (thuốc lá, rượu, GERD, béo phì); cấp 2 phát hiện sớm trên nhóm nguy cơ cao; theo dõi sau mổ dày nhất trong năm đầu (4 tháng/lần) để phát hiện sớm tái phát miệng nối và di căn xa.",
        "B10.01, B10.02, B10.03", ["Phong-benh", "Theo-doi"],
    ),
    basic(
        "SURG20B-B10-02", "B10", "Tài liệu tham khảo barem", 2,
        f"{B('[Tài liệu tham khảo chuẩn]')} Liệt kê {Y('6 tài liệu tham khảo')} được dẫn trong barem Ung thư thực quản?",
        f"1) {B('Bài giảng ung thư học')} — Trường ĐH Y Hà Nội, Bộ môn Ung thư (2001).<br>"
        f"2) {B('Điều trị nội khoa bệnh ung thư')} — Nguyễn Bá Đức, Trần Văn Thuấn, Nguyễn Tuyết Mai (2010).<br>"
        f"3) {B('Điều trị phẫu thuật bệnh ung thư')} — Nguyễn Văn Hiếu (2010).<br>"
        f"4) {B('IARC WHO (2015)')} — Global morbidity and mortality (Globocan cancer factsheet).<br>"
        f"5) {B('Edge SB, Compton CC (2010)')} — AJCC 7th edition cancer staging manual (Ann Surg Oncol).<br>"
        f"6) {B('Engholm GFJ, Christensen N, et al (2015)')} — Cancer Incidence, Mortality, Prevalence and Survival in the Nordic Countries.",
        "Nắm bộ nguồn trích dẫn chuẩn giúp biết hệ quy chiếu của các bảng dịch tễ, phân loại TNM AJCC 7th và phác đồ điều trị trong tài liệu thi.",
        "B10.04", ["Tai-lieu-tham-khao"],
    ),
    cloze(
        "SURG20B-B10-03", "B10", "Lịch tái khám sau mổ",
        f"Theo dõi sau phẫu thuật triệt căn ung thư thực quản: trong năm đầu tiên khám định kỳ {clz(1, Y('4 tháng/lần'))}. Trong 2 năm tiếp theo, khám định kỳ {clz(2, Y('6 tháng/lần'))}.",
        "B10.03", ["Theo-doi", "Nguong-so"],
    ),

    # ============================================================
    # 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (≥ 3 BẮT BUỘC THEO GATE 2.8)
    # ============================================================
    algo(
        "SURG20B-ALGO-01", "B7", "Thuật toán chẩn đoán",
        "Tiếp cận bệnh nhân nghi ung thư thực quản (Nuốt nghẹn tăng dần)",
        f"1) <b>Bước 1 — Nghi ngờ lâm sàng:</b> {R('Nuốt nghẹn tăng dần')} (đặc → lỏng), dừng sau xương ức, kèm {R('sụt cân nhanh, hạch Virchow - Troisier, khàn tiếng')}.<br>"
        f"2) <b>Bước 2 — Định hướng an toàn trước soi:</b> {B('Chụp thực quản có cản quang (Barium swallow)')} tìm hình ảnh u lồi, thâm nhiễm cứng, ổ loét để {G('tránh biến chứng thủng khi soi')}.<br>"
        f"3) <b>Bước 3 — Khẳng định tiêu chuẩn vàng:</b> {G('Nội soi thực quản kết hợp sinh thiết bờ tổn thương')} (chính xác đến {Y('90%')}) lấy giải phẫu bệnh.<br>"
        f"4) <b>Bước 4 — Đánh giá giai đoạn TNM:</b> {B('CT ngực - bụng')} (tìm di căn hạch, gan {Y('35%')}, phổi {Y('20%')}, xương {Y('9%')}), {B('MRI')} tương đương, {G('EUS')} đánh giá T &amp; N vùng khi chưa M1, {B('PET/PET-CT')} đánh giá di căn toàn thân.",
        "Không bao giờ đảo ngược bước khẳng định mô bệnh học hay bỏ qua đánh giá an toàn trước soi khi bệnh nhân nuốt nghẹn khít; trình tự Barium → Nội soi sinh thiết → CT/EUS/PET giúp vừa an toàn vừa phân loại TNM chính xác.",
        "B6.01, B6.02, B7.01, B7.02, B7.03, B7.04, B7.05, B7.06, B8.01", ["Chan-doan"],
    ),
    algo(
        "SURG20B-ALGO-02", "B9", "Thuật toán điều trị theo giai đoạn",
        "Chọn phác đồ điều trị ung thư thực quản theo giai đoạn TNM",
        f"1) <b>Rất sớm (chưa xâm lấn lớp cơ — Tis/T1a N0 M0):</b> {G('Cắt hớt niêm mạc qua nội soi (EMR/ESD)')}, laser hoặc quang đông lạnh ({G('cryotherapy')}).<br>"
        f"2) <b>Giai đoạn I (T1a/T1b N0 M0):</b> {G('Phẫu thuật cắt thực quản triệt căn')}, tạo hình {G('ống cuốn dạ dày')} đưa lên thay thế.<br>"
        f"3) <b>Giai đoạn II, III (IIA/IIB/III):</b> {G('Hóa - xạ trị tiền phẫu')} → sau đó {G('phẫu thuật triệt căn')} với diện cắt {Y('cách u > 5 cm')}, đạt {G('R0')} và nạo vét hạch vùng triệt để.<br>"
        f"4) <b>Giai đoạn IV (di căn xa M1):</b> Chỉ {G('điều trị giảm nhẹ')} (hóa chất toàn thân, xạ giảm đau/chảy máu, đặt stent kim loại tự nở, mở thông dạ dày/hỗng tràng, xạ trị IMRT/VMAT).",
        "Nguyên tắc xuyên suốt là điều trị đa mô thức tùy theo độ sâu xâm lấn thành (T), hạch (N) và di căn xa (M): chưa qua cơ bảo tồn bằng EMR/ESD; qua dưới niêm mạc mổ triệt căn; xâm lấn cơ/hạch vùng cần hóa-xạ tiền phẫu trước mổ; có M1 ngừng mổ triệt căn chuyển sang giảm nhẹ.",
        "B8.02, B9.01, B9.02, B9.04", ["Dieu-tri", "TNM"],
    ),
    algo(
        "SURG20B-ALGO-03", "B9", "Thuật toán phẫu thuật theo vị trí",
        "Chọn chiến lược phẫu thuật & điều trị theo vị trí u (Cổ – 1/3 trên – giữa – dưới)",
        f"1) <b>Đoạn cổ:</b> Cắt thực quản nguyên khối với {G('hạ họng - thanh quản')} + {R('mở khí quản vĩnh viễn')}, tái tạo bằng {G('vạt ruột non vi phẫu')} hoặc {G('kéo đại tràng lên')}.<br>"
        f"2) <b>1/3 trên ({Y('15–25 cm')} từ cung răng):</b> Khó cắt rộng triệt căn, tai biến cao → Ưu tiên hàng đầu {G('xạ trị / hóa xạ đồng thời')}.<br>"
        f"3) <b>1/3 giữa ({Y('26–32 cm')}):</b> {G('Cắt thực quản toàn bộ')}, tái tạo bằng {G('dạ dày hoặc quai đại tràng')} đưa lên ngực/cổ, kết hợp xạ trị và hóa chất.<br>"
        f"4) <b>1/3 dưới ({Y('33 cm')} đến tâm vị):</b> {G('Cắt đoạn thực quản dưới và cực trên dạ dày')}, nối dạ dày - thực quản trong lồng ngực.",
        "Vị trí tính từ cung răng chia rõ ranh giới kỹ thuật: 1/3 trên né mổ ưu tiên xạ/hóa xạ; đoạn cổ phải hy sinh thanh quản kèm vi phẫu ruột non/đại tràng; 1/3 giữa cắt toàn bộ thực quản; 1/3 dưới cắt đoạn dưới kèm cực trên dạ dày.",
        "B2.05, B9.03", ["Phau-thuat", "Vi-tri-u"],
    ),
    algo(
        "SURG20B-ALGO-04", "B9", "Thuật toán giảm nhẹ & tắc nghẽn",
        "Xử trí ung thư thực quản giai đoạn muộn, nuốt nghẹn nặng hoặc mất khả năng ăn đường miệng",
        f"1) <b>Nếu còn ăn lỏng được nhưng nghẹn do hẹp lòng ống:</b> Đặt {G('stent kim loại tự nở')} lòng thực quản giải quyết nuốt nghẹn.<br>"
        f"2) <b>Nếu không còn khả năng ăn qua đường miệng:</b> {G('Mở thông dạ dày hoặc hỗng tràng nuôi dưỡng')} để duy trì dinh dưỡng.<br>"
        f"3) <b>Nếu có đau hoặc chảy máu tại u:</b> {G('Xạ trị giảm nhẹ triệu chứng')}, cân nhắc kỹ thuật {B('IMRT / VMAT')} để bảo vệ tối đa mô lành.<br>"
        f"4) <b>Toàn thân:</b> Phối hợp {G('hóa chất toàn thân')} hoặc {G('chăm sóc giảm nhẹ')}.",
        "Chiến lược phân tầng theo mục tiêu triệu chứng: giải áp lòng ống (stent) vs đường nuôi dưỡng thay thế khi tắc hoàn toàn (mở thông dạ dày/hỗng tràng) vs kiểm soát đau/chảy máu (xạ IMRT/VMAT).",
        "B9.04", ["Giam-nhe", "Stent"],
    ),
    algo(
        "SURG20B-ALGO-05", "B10", "Thuật toán dự phòng & tái khám",
        "Chiến lược phòng bệnh (cấp 1, 2) và theo dõi sau phẫu thuật triệt căn",
        f"1) <b>Phòng bệnh cấp 1 (toàn dân):</b> {G('Bỏ thuốc lá')}, hạn chế rượu bia, điều trị dứt điểm {G('GERD')}, kiểm soát cân nặng.<br>"
        f"2) <b>Phòng bệnh cấp 2 (nguy cơ cao):</b> Tầm soát phát hiện sớm ở người {R('loạn sản Barrett')}, tiền sử gia đình, nghiện rượu thuốc lá lâu năm; riêng {R('loạn sản nặng')} nội soi định kỳ {Y('3 tháng/lần')}.<br>"
        f"3) <b>Sau phẫu thuật triệt căn — Năm 1:</b> Khám lâm sàng &amp; XN cơ bản {Y('4 tháng/lần')}.<br>"
        f"4) <b>Năm 2 – 3 (2 năm tiếp theo):</b> Khám định kỳ {Y('6 tháng/lần')}; thực hiện {B('X-quang phổi')}, {B('CT ngực - bụng')}, {G('nội soi kiểm tra miệng nối')}.",
        "Liên kết xuyên suốt 3 tầng thời gian: trước khi mắc (kiểm soát yếu tố nguy cơ), tiền ung thư (tầm soát nhóm nguy cơ và soi 3 tháng khi loạn sản nặng), và sau mổ (theo dõi sát 4 tháng/lần năm đầu rồi 6 tháng/lần trong 2 năm kế).",
        "B4.03, B10.01, B10.02, B10.03", ["Phong-benh", "Theo-doi"],
    ),
]
