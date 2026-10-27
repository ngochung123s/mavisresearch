# -*- coding: utf-8 -*-
# PED-11 Rối loạn thăng bằng toan kiềm & đọc khí máu động mạch nhi — nguồn thẻ duy nhất.
# Barem gốc: 4 trang handout Bộ môn Nhi (ThS.BSCKII. Khúc Văn Lập), file ..._PEDYTB.md.
# Mã barem từng dòng [Bx.yy]: mỗi mã phải có ≥ 1 thẻ (ghi ở `extra`).


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý / triệu chứng
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / mốc
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc / hướng can thiệp
    return _c("#51cf66", t)


def B(t):  # tên bệnh / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("🏛️ BAREM GỐC · HANDOUT BỘ MÔN NHI", "badge-barem")
SRC = "📖 Nguồn: Handout slide bài giảng Bộ môn Nhi — ThS.BSCKII. Khúc Văn Lập (4 trang, nhận ngày 27/10/2026). Barem: "


def basic(cid, section, category, tier, front, core, ai, barem, tags, asks=None):
    card = {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": SRC + barem,
        "tags": ["PED-11", "Barem-goc"] + tags,
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
        "tags": ["PED-11", "Barem-goc", "Cloze-phu"] + tags,
    }


cards_data = [
    # ------------------------------------------------------------ B0. Mục tiêu
    basic(
        "PED11-B0-01", "B0", "Mục tiêu bài học", 1,
        f"{B('[Mục tiêu bài học — Toan kiềm trẻ em]')} Bài này yêu cầu trình bày {Y('3 nội dung')} nào?",
        f"1) {G('Sinh lý của thăng bằng toan kiềm')} của cơ thể trẻ em.<br>"
        f"2) {G('Khái niệm và giới hạn bình thường')} của các thuật ngữ chỉ tình trạng kiềm toan.<br>"
        f"3) {R('Nguyên nhân, lâm sàng và tình trạng')} nhiễm toan, nhiễm kiềm hay gặp ở trẻ em.",
        "Ba mục tiêu đi theo đúng trình tự học: nền sinh lý → ngưỡng bình thường để nhận biết bất thường → bệnh cảnh "
        "nhiễm toan/nhiễm kiềm thường gặp để chẩn đoán và xử trí.",
        "B0.01, B0.02, B0.03", ["Muc-tieu"],
    ),

    # ------------------------------------------------------------ B1. Khái niệm cơ bản
    basic(
        "PED11-B1-01", "B1", "Khái niệm cơ bản", 1,
        f"{B('[Khái niệm cơ bản]')} Kể các {Y('thành phần')} cốt lõi của cân bằng toan kiềm.",
        f"1) {B('pH')}.<br>2) {B('H⁺')}.<br>3) {B('HCO₃⁻')}.",
        "pH là logarit âm nồng độ H⁺; HCO₃⁻ là thành phần kiềm chính của hệ đệm. Ba đại lượng này liên kết với nhau "
        "qua phương trình Henderson–Hasselbalch (thẻ B3), là nền để đọc mọi khí máu.",
        "B1.01", ["Khai-niem"],
    ),
    basic(
        "PED11-B1-02", "B1", "Khái niệm cơ bản", 2,
        f"{B('[Khối lượng H⁺ và CO₂ mỗi ngày]')} Một ngày chuyển hóa tạo ra bao nhiêu {Y('H⁺')} và bao nhiêu {Y('CO₂')}?",
        f"1) {R('40–80 mEq H⁺')}.<br>2) {R('13.000 mmol CO₂')}.",
        "Lượng acid sinh ra mỗi ngày lớn, nên cơ thể phải có hệ đệm và cơ chế thải trừ liên tục (phổi thải CO₂, thận thải H⁺) "
        "để pH không dao động.",
        "B1.02", ["Khai-niem", "So-lieu"],
    ),
    basic(
        "PED11-B1-03", "B1", "Khái niệm cơ bản", 2,
        f"{B('[Yếu tố gây nhiễm toan ở trẻ em]')} Trẻ em có {Y('mấy')} yếu tố gây nhiễm toan và đó là những yếu tố nào?",
        f"Có {Y('3')} yếu tố:<br>1) {R('Chuyển hóa thức ăn')}.<br>2) {R('Dị hóa cho CO₂')}.<br>3) {R('Tạo xương')}.",
        "Ở trẻ, cả ba nguồn acid đều tăng tương đối so với người lớn (chuyển hóa nhanh, dị hóa mạnh, xương đang tạo mới), "
        "nên trẻ dễ bị nhiễm toan hơn khi có stress chuyển hóa.",
        "B1.03", ["Khai-niem", "Tre-em"],
    ),

    # ------------------------------------------------------------ B2. Hệ đệm
    basic(
        "PED11-B2-01", "B2", "Hệ đệm", 1,
        f"{B('[Hệ đệm]')} Kể {Y('4 hệ đệm')} của cơ thể và thành phần cụ thể của hệ đệm bicarbonat.",
        f"1) {G('Bicarbonat')}: {B('H₂CO₃/HCO₃⁻')}.<br>2) {G('Phosphat')}: {B('Na₂HPO₄⁻/NaH₂PO₄⁻')} (sic).<br>"
        f"3) {G('Hemoglobin')}: {B('Hb⁻/HHb')}.<br>4) {G('Protein')}: {B('Protein/Proteinat')}.",
        "Hệ đệm bicarbonat là quan trọng nhất ngoài tế bào (liên kết phổi – thận). Ba hệ còn lại có vai trò đệm chủ yếu "
        "trong và quanh tế bào, đặc biệt hemoglobin đệm H⁺ trong hồng cầu.",
        "B2.01, B2.02, B2.03, B2.04", ["He-dem"],
        asks=None,
    ),

    # ------------------------------------------------------------ B3. Henderson–Hasselbalch
    basic(
        "PED11-B3-01", "B3", "Phương trình Henderson–Hasselbalch", 1,
        f"{B('[Phương trình Henderson–Hasselbalch]')} Viết phương trình thể hiện mối liên hệ giữa {Y('pH')}, {Y('HCO₃⁻')} và {Y('PaCO₂')}, "
        f"kèm {Y('hằng số')} pK.",
        f"{B('pH = pK + lg HCO₃⁻ / (0,03 × PaCO₂)')} (công thức in trên handout).",
        "Đây là công thức nền để suy ra pH từ HCO₃⁻ và PaCO₂. Hằng số 0,03 là hệ số hòa tan của CO₂ trong máu "
        "(mmol/L/mmHg); phương trình cho thấy pH tỷ lệ thuận với HCO₃⁻ và tỷ lệ nghịch với PaCO₂.",
        "B3.01", ["Henderson", "Cong-thuc"],
    ),
    basic(
        "PED11-B3-02", "B3", "Phương trình Henderson–Hasselbalch", 2,
        f"{B('[Henderson–Hasselbalch — dạng với pK = 6,1]')} Viết phương trình với {Y('giá trị pK')} và {Y('hệ số')} cụ thể.",
        f"{B('pH = 6,1 + lg HCO₃⁻ / (0,03 × PaCO₂)')}.<br>"
        f"Trong đó pK = {Y('6,1')} và hệ số hòa tan CO₂ = {Y('0,03')}.",
        "Đây là dạng dùng để tính trực tiếp. Lưu ý handout in tên là 'Henderson-Hassenbach' (lỗi chính tả trong nguyên bản); "
        "tên đúng là Henderson–Hasselbalch.",
        "B3.02", ["Henderson", "Cong-thuc"],
    ),

    # ------------------------------------------------------------ B4. Vai trò phổi
    basic(
        "PED11-B4-01", "B4", "Vai trò của phổi", 1,
        f"{B('[Vai trò của phổi — vận chuyển CO₂]')} CO₂ được giải phóng trong quá trình {Y('oxy hóa')} được vận chuyển "
        f"theo {Y('bao nhiêu phần trăm')} ở mỗi dạng nào?",
        f"1) {G('5%')} được {B('hòa tan trong huyết tương')}.<br>"
        f"2) {G('70%')} được {B('gắn với nước')}.<br>"
        f"3) {G('25%')} gắn với {B('Hb tạo cacbamin')}.<br>"
        f"→ CO₂ giải phóng từ quá trình {R('oxy hóa')}.",
        "Phần lớn CO₂ đi dưới dạng HCO₃⁻ (qua nước), phần còn lại gắn Hb tạo cacbamin. Phổi thải CO₂ nên thay đổi thông "
        "khí làm thay đổi PaCO₂ rất nhanh — đây là cơ sở của rối loạn hô hấp.",
        "B4.01, B4.02, B4.03, B4.04", ["Phoi", "Van-chuyen-CO2"],
    ),

    # ------------------------------------------------------------ B5. Vai trò thận
    basic(
        "PED11-B5-01", "B5", "Vai trò của thận", 1,
        f"{B('[Vai trò của thận trong thăng bằng toan kiềm]')} Thận thực hiện {Y('những')} chức năng nào để điều chỉnh toan kiềm?",
        f"1) {G('Tái hấp thu, tái sinh HCO₃⁻')}.<br>2) {G('Đào thải H⁺')}.",
        "Thận là cơ quan điều chỉnh chậm nhưng bền vững: giữ lại HCO₃⁻ đã lọc và bài tiết H⁺ ra nước tiểu. Đây là lý do "
        "rối loạn chuyển hóa cần thời gian để thận bù trừ.",
        "B5.01, B5.02", ["Than"],
    ),

    # ------------------------------------------------------------ B6. Rối loạn
    basic(
        "PED11-B6-01", "B6", "Phân loại rối loạn toan kiềm", 1,
        f"{B('[Phân loại nhiễm toan]')} Nhiễm toan được chia theo {Y('mức bù')} và theo {Y('nguyên nhân')} như thế nào?",
        f"1) Theo mức bù: {R('còn bù')}, {R('mất bù')}.<br>"
        f"2) Theo nguyên nhân: {B('toan hô hấp')}, {B('toan chuyển hóa')}, {B('toan hỗn hợp')}.",
        "Mức bù mô tả việc cơ thể đã điều chỉnh pH về gần bình thường hay chưa. Nguyên nhân (hô hấp hay chuyển hóa) quyết "
        "định cách chẩn đoán ở thẻ B14.",
        "B6.01", ["Phan-loai"],
    ),
    basic(
        "PED11-B6-02", "B6", "Phân loại rối loạn toan kiềm", 1,
        f"{B('[Phân loại nhiễm kiềm]')} Nhiễm kiềm được chia theo {Y('mức bù')} và theo {Y('nguyên nhân')} như thế nào?",
        f"1) Theo mức bù: {R('còn bù')}, {R('mất bù')}.<br>"
        f"2) Theo nguyên nhân: {B('kiềm hô hấp')}, {B('kiềm chuyển hóa')}, {B('kiềm hỗn hợp')}.",
        "Cấu trúc phân loại giống nhiễm toan, đổi chiều: rối loạn tiên phát là hô hấp hay chuyển hóa, và cơ thể đã bù trừ "
        "đến mức nào.",
        "B6.02", ["Phan-loai"],
    ),

    # ------------------------------------------------------------ B7. pH, PaCO2, PaO2
    basic(
        "PED11-B7-01", "B7", "Khí máu — pH, PaCO₂, PaO₂", 1,
        f"{B('[pH động mạch bình thường]')} Giới hạn bình thường của {Y('pH')} là bao nhiêu?",
        f"{Y('pH: 7,35–7,45')}.",
        "Giới hạn hẹp: pH < 7,35 là nhiễm toan, pH > 7,45 là nhiễm kiềm (đối chiếu với thẻ B14 để xác định tiên phát).",
        "B7.01", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B7-02", "B7", "Khí máu — pH, PaCO₂, PaO₂", 1,
        f"{B('[PaCO₂ động mạch bình thường]')} Giới hạn bình thường của {Y('PaCO₂')} là bao nhiêu?",
        f"{Y('PaCO₂: 35–45 mmHg')}.",
        "PaCO₂ phản ánh thành phần hô hấp: > 45 gợi ý toan hô hấp, < 35 gợi ý kiềm hô hấp.",
        "B7.02", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B7-03", "B7", "Khí máu — pH, PaCO₂, PaO₂", 1,
        f"{B('[PaO₂ bình thường theo lứa tuổi]')} Giới hạn {Y('PaO₂')} bình thường ở {Y('sơ sinh')} và ở {Y('trẻ lớn')} là bao nhiêu?",
        f"1) Sơ sinh: {Y('50–70 mmHg')}.<br>2) Trẻ lớn: {Y('70–100 mmHg')}.",
        "PaO₂ bình thường của trẻ sơ sinh thấp hơn trẻ lớn và giảm dần theo tuổi; vì vậy cùng một giá trị có thể bình thường "
        "ở sơ sinh nhưng thiếu oxy ở trẻ lớn.",
        "B7.03", ["Khi-mau", "Tuoi"],
    ),
    basic(
        "PED11-B7-04", "B7", "Khí máu — pH, PaCO₂, PaO₂", 2,
        f"{B('[Công thức ước tính PaO₂ theo tuổi]')} Viết công thức ước tính {Y('PaO₂')} bình thường theo {Y('tuổi')} (tính bằng năm).",
        f"{B('PaO₂ = 109 − 0,43 × tuổi')} (tuổi tính bằng năm).",
        "Công thức cho giá trị PaO₂ kỳ vọng theo tuổi để so sánh với kết quả đo. PaO₂ thực tế thấp hơn nhiều so với giá trị "
        "kỳ vọng gợi ý giảm oxy máu.",
        "B7.04", ["Khi-mau", "Cong-thuc"],
    ),

    # ------------------------------------------------------------ B8. AaDO2, CaO2, BB
    basic(
        "PED11-B8-01", "B8", "Khí máu — AaDO₂, CaO₂, BB", 1,
        f"{B('[Chênh áp oxy phế nang–động mạch]')} {Y('AaDO₂')} (P(A-a)O₂) bình thường là bao nhiêu?",
        f"{Y('AaDO₂ hoặc P(A-a)O₂: 5–15 mmHg')}.",
        "Chênh áp phế nang – động mạch phản ánh rối loạn trao đổi khí (khuếch tán, thông khí/tưới máu). Giá trị tăng gợi ý "
        "tổn thương phổi thay vì chỉ giảm thông khí đơn thuần.",
        "B8.01", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B8-02", "B8", "Khí máu — AaDO₂, CaO₂, BB", 1,
        f"{B('[Oxy toàn phần trong máu]')} {Y('O₂CT')} hay {Y('CaO₂')} bình thường là bao nhiêu?",
        f"{Y('O₂CT hoặc CaO₂: 12–16 ml/dl')}.",
        "CaO₂ là lượng oxy tổng số trong máu (gắn với Hb và hòa tan). Giảm CaO₂ có thể do thiếu Hb (thiếu máu) dù PaO₂ bình thường.",
        "B8.02", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B8-03", "B8", "Khí máu — AaDO₂, CaO₂, BB", 1,
        f"{B('[Base Buffer — BB]')} Giới hạn bình thường của {Y('BB')} (Base Buffer) là bao nhiêu?",
        f"{Y('BB: 48–49 mmol/l máu')}.",
        "BB là tổng đệm kiềm của máu, nên nó không phụ thuộc vào thành phần hô hấp như HCO₃⁻ thực. Dùng BB để đánh giá tổng dự trữ đệm.",
        "B8.03", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B8-04", "B8", "Khí máu — AaDO₂, CaO₂, BB", 2,
        f"{B('[BB — định nghĩa]')} BB là tổng số {Y('anion đệm')} nào có khả năng nhận H⁺ trong một lít máu?",
        f"1) {B('HCO₃⁻')}.<br>2) {B('HbO₂⁻')}.<br>3) {B('Protein⁻')}.<br>4) {B('HPO₄⁻')}.<br>5) {B('NH₃')}.",
        "Năm anion/phân tử này là các đệm chính có khả năng nhận H⁺. BB là tổng của chúng, nên phản ánh toàn bộ dự trữ đệm "
        "của máu.",
        "B8.04", ["Khi-mau", "Dinh-nghia"],
    ),
    basic(
        "PED11-B8-05", "B8", "Khí máu — AaDO₂, CaO₂, BB", 2,
        f"{B('[Quan hệ BB và BE]')} Khi {Y('BB = 40')} thì {Y('BE')} bằng bao nhiêu?",
        f"Khi BB = {Y('40')} thì BE = {R('−8')}.",
        "BE = BB − NBB (thẻ B9). Với BB thấp hơn bình thường, BE âm: thiếu hụt đệm, gợi ý toan chuyển hóa.",
        "B8.05", ["Khi-mau", "Quan-he"],
    ),
    basic(
        "PED11-B8-06", "B8", "Khí máu — AaDO₂, CaO₂, BB", 2,
        f"{B('[Quan hệ BB và BE]')} Khi {Y('BB = 60')} thì {Y('BE')} bằng bao nhiêu?",
        f"Khi BB = {Y('60')} thì BE = {G('+12')}.",
        "Với BB cao hơn bình thường, BE dương: dư kiềm, gợi ý kiềm chuyển hóa. Hai ví dụ (BB 40 → BE −8, BB 60 → BE +12) "
        "minh họa BE chạy theo BB.",
        "B8.06", ["Khi-mau", "Quan-he"],
    ),

    # ------------------------------------------------------------ B9. BE
    basic(
        "PED11-B9-01", "B9", "Khí máu — BE", 1,
        f"{B('[BE — Base Excess]')} Giới hạn thực tế của {Y('BE')} (Base Excess) là bao nhiêu?",
        f"{Y('BE = ±3')}.",
        "BE trong khoảng ±3 được coi là bình thường thực tế (dù lý thuyết bằng 0). Ngoài khoảng này là có rối loạn chuyển hóa.",
        "B9.01", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B9-02", "B9", "Khí máu — BE", 2,
        f"{B('[BE — công thức]')} {Y('BE')} được tính như thế nào theo {Y('BB')} và {Y('NBB')}?",
        f"BE = {B('BB − NBB')}.",
        "BE là phần chênh giữa BB thực và NBB (BB chuẩn). Công thức này cho biết mức đệm dư hay thiếu so với chuẩn.",
        "B9.02", ["Khi-mau", "Cong-thuc"],
    ),
    basic(
        "PED11-B9-03", "B9", "Khí máu — BE", 2,
        f"{B('[NBB — định nghĩa]')} {Y('NBB')} là đại lượng nào?",
        f"NBB là {B('kiềm đệm trong điều kiện chuẩn')}.",
        "NBB (normal buffer base) là lượng đệm kiềm khi khí máu được chuẩn hóa về điều kiện chuẩn, dùng làm mốc để tính BE.",
        "B9.03", ["Khi-mau", "Dinh-nghia"],
    ),
    basic(
        "PED11-B9-04", "B9", "Khí máu — BE", 2,
        f"{B('[BE trong điều kiện bình thường]')} Trong điều kiện bình thường {Y('NBB')} và {Y('BB')} quan hệ như thế nào, "
        f"và {Y('BE')} thực tế bằng bao nhiêu?",
        f"1) Bình thường {Y('NBB = BB')} nên {Y('BE = 0')}.<br>2) Thực tế {Y('BE = ±3')}.",
        "Lý thuyết BE = 0 khi cân bằng hoàn toàn, nhưng thực tế có dao động sinh lý nên dùng khoảng ±3.",
        "B9.04", ["Khi-mau", "Gioi-han"],
    ),

    # ------------------------------------------------------------ B10. BE ecf, TCO2
    basic(
        "PED11-B10-01", "B10", "Khí máu — BE ecf, TCO₂", 1,
        f"{B('[BE ecf — kiềm dư dịch ngoại bào]')} {Y('BE ecf')} (BE of extracellular fluid) là gì và vì sao được ưu tiên hơn BE máu?",
        f"{B('BE ecf')}: kiềm dư trong {B('dịch ngoại bào')}. Đại diện cho {G('toàn bộ cơ thể')}, "
        f"{G('chính xác hơn kiềm dư trong máu')}.",
        "Dịch ngoại bào là ngăn đệm lớn hơn máu, nên BE ecf phản ánh tổng dự trữ đệm của cơ thể tốt hơn BE máu đơn thuần.",
        "B10.01", ["Khi-mau", "Dinh-nghia"],
    ),
    basic(
        "PED11-B10-02", "B10", "Khí máu — BE ecf, TCO₂", 1,
        f"{B('[TCO₂ bình thường]')} Giới hạn bình thường của {Y('TCO₂')} là bao nhiêu?",
        f"{Y('TCO₂: 25,4 mEq/l')}.",
        "TCO₂ là tổng CO₂ trong máu (phần đệm bicarbonat, CO₂ hòa tan và cacbamin). Giá trị gần bằng HCO₃⁻ + một phần CO₂.",
        "B10.02", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B10-03", "B10", "Khí máu — BE ecf, TCO₂", 2,
        f"{B('[TCO₂ — thành phần]')} TCO₂ (dự trữ kiềm) bao gồm {Y('những dạng')} nào?",
        f"1) {B('HCO₃⁻')}.<br>2) {B('CO₂')}.<br>3) {B('Cacbamin')}.",
        "TCO₂ là toàn bộ CO₂ có thể mang được (ba dạng cộng lại), nên là chỉ số tổng hơn HCO₃⁻ đơn lẻ.",
        "B10.03", ["Khi-mau", "Dinh-nghia"],
    ),

    # ------------------------------------------------------------ B11. HCO3 thực
    basic(
        "PED11-B11-01", "B11", "Khí máu — HCO₃⁻ thực", 1,
        f"{B('[HCO₃⁻ thực — actual BC]')} Giới hạn bình thường của {Y('HCO₃⁻ thực (actual BC)')} là bao nhiêu?",
        f"{Y('HCO₃⁻ (actual BC): 22–26 mEq/l')}.",
        "HCO₃⁻ thực là chỉ số phụ thuộc PaCO₂ (khác với HCO₃⁻ chuẩn ở thẻ B12). Dùng để đánh giá thành phần chuyển hóa, "
        "nhưng cần đối chiếu với PaCO₂ để tách rối loạn.",
        "B11.01", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B11-02", "B11", "Khí máu — HCO₃⁻ thực", 2,
        f"{B('[HCO₃⁻ thực — cách tính]')} Nồng độ ion bicarbonat trong huyết tương và dịch gian bào được tính như thế nào, "
        f"và {Y('vì sao')} không áp dụng chính xác cho dịch trong tế bào?",
        f"1) {G('Bằng hiệu số CO₂ toàn phần trừ đi CO₂ hòa tan')}.<br>"
        f"2) Vì {Y('phần cacbamin không đáng kể')} ở huyết tương và dịch gian bào.<br>"
        f"3) {R('Đối với dịch trong tế bào sẽ cho sai số lớn')}.",
        "Trong tế bào cacbamin đáng kể nên công thức trừ bỏ không còn chính xác. Đây là lý do HCO₃⁻ tính trong máu/huyết tương "
        "được dùng, còn đánh giá nội bào cần thận trọng.",
        "B11.02", ["Khi-mau", "Cong-thuc"],
    ),

    # ------------------------------------------------------------ B12. HCO3 chuẩn
    basic(
        "PED11-B12-01", "B12", "Khí máu — HCO₃⁻ chuẩn (SB/SBC)", 1,
        f"{B('[HCO₃⁻ chuẩn — st HCO₃⁻ (SB/SBC)]')} Giới hạn bình thường của {Y('st HCO₃⁻')} (SB/SBC) là bao nhiêu?",
        f"{Y('23,3 ± 1,2 mEq/l')}.",
        "Kiềm chuẩn là HCO₃⁻ đo ở điều kiện PaCO₂ chuẩn, nên chỉ phản ánh thành phần chuyển hóa và không đổi theo CO₂.",
        "B12.01", ["Khi-mau", "Gioi-han"],
    ),
    basic(
        "PED11-B12-02", "B12", "Khí máu — HCO₃⁻ chuẩn (SB/SBC)", 2,
        f"{B('[HCO₃⁻ chuẩn — điều kiện chuẩn]')} Nồng độ HCO₃⁻ được cân bằng ở {Y('điều kiện chuẩn')} nào?",
        f"{Y('PaCO₂ = 40 mmHg')}, {Y('nhiệt độ 37 °C')} và {Y('huyết sắc tố bão hòa oxy')}.",
        "Điều kiện chuẩn cố định PaCO₂, nhiệt độ và độ bão hòa oxy để kết quả HCO₃⁻ chuẩn có thể so sánh giữa các bệnh nhân.",
        "B12.02", ["Khi-mau", "Dieu-kien"],
    ),
    basic(
        "PED11-B12-03", "B12", "Khí máu — HCO₃⁻ chuẩn (SB/SBC)", 2,
        f"{B('[st HCO₃⁻ — ưu điểm]')} Vì sao {Y('st HCO₃⁻')} được dùng thay cho HCO₃⁻ thực khi đánh giá rối loạn chuyển hóa?",
        f"Vì HCO₃⁻ thay đổi theo mức CO₂ nên {G('st HCO₃⁻ được dùng để thay cho HCO₃⁻')}, "
        f"{G('không phụ thuộc vào sự thay đổi của CO₂')}.",
        "Khi PaCO₂ thay đổi (rối loạn hô hấp), HCO₃⁻ thực cũng đổi và che khuất rối loạn chuyển hóa. st HCO₃⁻ loại bỏ hiệu ứng này.",
        "B12.03", ["Khi-mau", "Y-nghia"],
    ),
    basic(
        "PED11-B12-04", "B12", "Khí máu — HCO₃⁻ chuẩn (SB/SBC)", 1,
        f"{B('[st HCO₃⁻ — diễn giải]')} {Y('SBC thấp')} và {Y('SBC cao')} gợi ý rối loạn chuyển hóa nào?",
        f"1) {R('SBC thấp')}: {R('toan chuyển hóa')}.<br>2) {R('SBC cao')}: {R('kiềm chuyển hóa')}.",
        "Đây là cách diễn giải nhanh: SBC phản ánh thành phần chuyển hóa, nên giảm là toan chuyển hóa, tăng là kiềm chuyển hóa.",
        "B12.04", ["Khi-mau", "Dien-giai"],
    ),

    # ------------------------------------------------------------ B13. SaO2
    basic(
        "PED11-B13-01", "B13", "Khí máu — SaO₂", 1,
        f"{B('[SaO₂ bình thường]')} Độ bão hòa oxy máu động mạch {Y('SaO₂')} bình thường là bao nhiêu?",
        f"{Y('95–98%')}.",
        "SaO₂ phản ánh phần Hb đã gắn oxy. Giảm SaO₂ gợi ý thiếu oxy máu, cần đối chiếu với PaO₂ ở thẻ B7 và bước 5 đọc khí máu.",
        "B13.01", ["Khi-mau", "Gioi-han"],
    ),

    # ------------------------------------------------------------ B14. Quy trình đọc khí máu
    algo(
        "PED11-ALGO-01", "B14", "Quy trình 5 bước đọc khí máu",
        "Quy trình 5 bước đọc khí máu",
        f"1) {G('Bước 1')}: Đánh giá {Y('tình trạng lâm sàng')} của bệnh nhân.<br>"
        f"2) {G('Bước 2')}: Đọc {Y('pH máu')} để xác định nhiễm toan hay nhiễm kiềm, còn bù hay mất bù.<br>"
        f"3) {G('Bước 3')}: Dựa vào {Y('PaCO₂ hoặc HCO₃⁻')} để xác định rối loạn tiên phát thuộc về {B('hô hấp')} "
        f"hay {B('chuyển hóa')}.<br>"
        f"4) {G('Bước 4')}: Xác định {Y('đáp ứng bù trừ')}. Nếu không phù hợp tính toán → kết luận "
        f"{R('rối loạn thăng bằng toan kiềm hỗn hợp')}.<br>"
        f"5) {G('Bước 5')}: Đánh giá {Y('tình trạng oxy')}.",
        "Thứ tự quan trọng: pH cho biết hướng (toan hay kiềm), PaCO₂/HCO₃⁻ cho biết nguyên nhân tiên phát, rồi mới kiểm tra "
        "bù trừ theo bảng B15–B16. Đáp ứng bù không khớp công thức là dấu hiệu rối loạn hỗn hợp.",
        "B14.01, B14.02, B14.03, B14.04, B14.05", ["Quy-trinh", "Doc-khi-mau"],
    ),
    algo(
        "PED11-ALGO-02", "B14", "Xác định tiên phát và bù trừ",
        "Đọc pH trước, rồi chọn tiên phát",
        f"1) {G('pH ↓')} → {R('toan')}; {G('pH ↑')} → {R('kiềm')}.<br>"
        f"2) {G('PaCO₂ đi ngược chiều pH')} (pH ↓ + PaCO₂ ↑, hoặc pH ↑ + PaCO₂ ↓) → {B('rối loạn hô hấp')} là tiên phát.<br>"
        f"3) {G('HCO₃⁻ đi cùng chiều pH')} (pH ↓ + HCO₃⁻ ↓, hoặc pH ↑ + HCO₃⁻ ↑) → {B('rối loạn chuyển hóa')} là tiên phát.<br>"
        f"4) Kiểm tra {Y('đáp ứng bù trừ')} bằng bảng B15 (chuyển hóa) hoặc B16 (hô hấp).",
        "Đây là cách rút gọn bước 2–3 của quy trình: pH cho hướng, sau đó cặp PaCO₂/HCO₃⁻ quyết định tiên phát. Bù trừ "
        "không đúng công thức là rối loạn hỗn hợp (bước 4).",
        "B14.02, B14.03, B14.04", ["Quy-trinh", "Thuat-toan-nho"],
    ),
    algo(
        "PED11-ALGO-03", "B14", "Kết luận hỗn hợp khi bù trừ sai",
        "Khi nào kết luận rối loạn hỗn hợp",
        f"1) Tính {Y('đáp ứng bù trừ kỳ vọng')} theo bảng B15 (chuyển hóa) hoặc B16 (hô hấp).<br>"
        f"2) So với giá trị {Y('đo được')}.<br>"
        f"3) {G('Phù hợp')} → rối loạn đơn thuần (tiên phát + bù trừ đúng).<br>"
        f"4) {R('Không phù hợp')} → {R('rối loạn thăng bằng toan kiềm hỗn hợp')}.",
        "Bù trừ lệch khỏi công thức cho thấy có thêm một rối loạn thứ hai. Đây là bẫy hay gặp khi đọc khí máu đơn thuần bằng pH.",
        "B14.04", ["Quy-trinh", "Hon-hop"],
    ),
    algo(
        "PED11-ALGO-04", "B14", "Đánh giá oxy sau khi đọc khí máu",
        "Đánh giá tình trạng oxy (bước 5)",
        f"1) {Y('PaO₂')}: sơ sinh {Y('50–70 mmHg')}, trẻ lớn {Y('70–100 mmHg')}; ước tính {Y('PaO₂ = 109 − 0,43 × tuổi')} (năm).<br>"
        f"2) {Y('SaO₂')}: bình thường {Y('95–98%')}.<br>"
        f"3) {Y('AaDO₂ / P(A-a)O₂')}: bình thường {Y('5–15 mmHg')}.<br>"
        f"4) {Y('O₂CT / CaO₂')}: bình thường {Y('12–16 ml/dl')}.",
        "Bước 5 không phải là phụ: một bệnh nhân pH bình thường vẫn có thể thiếu oxy. Đối chiếu lần lượt 4 chỉ số oxy của khí "
        "máu với giới hạn bình thường của barem; chỉ số nào lệch khỏi khoảng này là bất thường về oxy.",
        "B14.05, B7.03, B7.04, B8.01, B8.02, B13.01", ["Quy-trinh", "Oxy"],
    ),

    # ------------------------------------------------------------ B15. Bù trừ chuyển hóa
    basic(
        "PED11-B15-01", "B15", "Bù trừ rối loạn chuyển hóa", 1,
        f"{B('[Toan chuyển hóa — bù trừ]')} Toan chuyển hóa có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ thứ phát')} "
        f"bao nhiêu mmHg PaCO₂ cho mỗi {Y('1 mEq')} HCO₃⁻?",
        f"1) pH: {R('↓')}.<br>2) Tiên phát: {R('↓ HCO₃⁻')}.<br>"
        f"3) Bù: {G('↓ PaCO₂ 1–1,5 mmHg')} cho mỗi {Y('1 mEq HCO₃⁻ giảm')}.",
        "Toan chuyển hóa bù bằng thở nhanh (giảm PaCO₂). Mức bù 1–1,5 mmHg/mEq là chuẩn để so với PaCO₂ đo được (thẻ B15-02).",
        "B15.01", ["Bu-tru", "Chuyen-hoa"],
    ),
    basic(
        "PED11-B15-02", "B15", "Bù trừ rối loạn chuyển hóa", 2,
        f"{B('[Toan chuyển hóa — công thức bù]')} Công thức tính {Y('PaCO₂ kỳ vọng')} của toan chuyển hóa theo {Y('HCO₃⁻')} là gì?",
        f"{B('PaCO₂ = 1,5 × (HCO₃⁻) + 8 ± 2')}.",
        "Công thức thay thế cho quy tắc 1–1,5 mmHg/mEq: dự đoán PaCO₂ bù, sai số ±2. PaCO₂ đo được lệch ngoài khoảng này gợi ý "
        "rối loạn hô hấp kèm theo (hỗn hợp).",
        "B15.02", ["Bu-tru", "Cong-thuc"],
    ),
    basic(
        "PED11-B15-03", "B15", "Bù trừ rối loạn chuyển hóa", 1,
        f"{B('[Kiềm chuyển hóa — bù trừ]')} Kiềm chuyển hóa có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ thứ phát')} "
        f"bao nhiêu mmHg PaCO₂ cho mỗi {Y('1 mEq')} HCO₃⁻ tăng?",
        f"1) pH: {R('↑')}.<br>2) Tiên phát: {R('↑ HCO₃⁻')}.<br>"
        f"3) Bù: {G('↑ PaCO₂ 0,2–0,9 mmHg')} (trung bình {Y('0,7')}) cho mỗi {Y('1 mEq HCO₃⁻ tăng')}.",
        "Kiềm chuyển hóa bù yếu bằng giảm thông khí; mức bù trung bình 0,7 mmHg/mEq, dải rộng 0,2–0,9. Bù kém hơn toan chuyển hóa.",
        "B15.03", ["Bu-tru", "Chuyen-hoa"],
    ),

    # ------------------------------------------------------------ B16. Bù trừ hô hấp
    basic(
        "PED11-B16-01", "B16", "Bù trừ rối loạn hô hấp", 1,
        f"{B('[Toan hô hấp cấp]')} Toan hô hấp {Y('cấp')} có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ')} "
        f"HCO₃⁻ bao nhiêu cho mỗi {Y('10 mmHg')} PaCO₂ tăng?",
        f"1) pH: {R('↓')}.<br>2) Tiên phát: {R('↑ PaCO₂')}.<br>"
        f"3) Bù: {G('↑ HCO₃⁻ nhẹ 1 mEq/10 mmHg')} PaCO₂ tăng.",
        "Toan hô hấp cấp chưa kịp bù qua thận nên bù HCO₃⁻ rất ít: chỉ 1 mEq cho mỗi 10 mmHg PaCO₂ tăng.",
        "B16.01", ["Bu-tru", "Ho-hap"],
    ),
    basic(
        "PED11-B16-02", "B16", "Bù trừ rối loạn hô hấp", 1,
        f"{B('[Toan hô hấp mạn]')} Toan hô hấp {Y('mạn')} có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ')} "
        f"HCO₃⁻ bao nhiêu cho mỗi {Y('10 mmHg')} PaCO₂ tăng?",
        f"1) pH: {R('↓')}.<br>2) Tiên phát: {R('↑↑ PaCO₂')}.<br>"
        f"3) Bù: {G('↑ HCO₃⁻ 5 mEq/10 mmHg')} PaCO₂ tăng.",
        "Toan hô hấp mạn đã có thời gian để thận giữ HCO₃⁻, nên bù mạnh gấp ~5 lần cấp (5 mEq/10 mmHg) và pH có thể gần bình thường.",
        "B16.02", ["Bu-tru", "Ho-hap"],
    ),
    basic(
        "PED11-B16-03", "B16", "Bù trừ rối loạn hô hấp", 1,
        f"{B('[Kiềm hô hấp cấp]')} Kiềm hô hấp {Y('cấp')} có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ')} "
        f"HCO₃⁻ bao nhiêu cho mỗi {Y('10 mmHg')} PaCO₂ giảm?",
        f"1) pH: {R('↑')}.<br>2) Tiên phát: {R('↓ PaCO₂')}.<br>"
        f"3) Bù: {G('↓ HCO₃⁻ 2 mEq/10 mmHg')} PaCO₂ giảm.",
        "Kiềm hô hấp cấp: bù bằng giảm HCO₃⁻ chậm qua thận; trong cấp, bù chỉ 2 mEq/10 mmHg.",
        "B16.03", ["Bu-tru", "Ho-hap"],
    ),
    basic(
        "PED11-B16-04", "B16", "Bù trừ rối loạn hô hấp", 1,
        f"{B('[Kiềm hô hấp mạn]')} Kiềm hô hấp {Y('mạn')} có pH {Y('?')}, {Y('rối loạn tiên phát')} là gì, và {Y('bù trừ')} "
        f"HCO₃⁻ bao nhiêu cho mỗi {Y('10 mmHg')} PaCO₂ giảm?",
        f"1) pH: {Y('bình thường hoặc ↑')}.<br>2) Tiên phát: {R('↓ PaCO₂')}.<br>"
        f"3) Bù: {G('↓ HCO₃⁻ 5 mEq/10 mmHg')} PaCO₂ giảm.",
        "Kiềm hô hấp mạn: thận đã có thời gian thải HCO₃⁻ nên bù mạnh (5 mEq/10 mmHg), giữ pH gần bình thường.",
        "B16.04", ["Bu-tru", "Ho-hap"],
    ),

    # ------------------------------------------------------------ B17. Nguyên nhân toan hô hấp
    basic(
        "PED11-B17-01", "B17", "Nhiễm toan hô hấp", 1,
        f"{B('[Toan hô hấp — định nghĩa]')} Nhiễm toan hô hấp khi {Y('PaCO₂')} vượt quá bao nhiêu?",
        f"Khi {Y('PaCO₂ > 50 mmHg')}.",
        "Ngưỡng 50 mmHg là cut-off của toan hô hấp (bình thường 35–45 mmHg). Dưới đây là các nguyên nhân gây tăng PaCO₂.",
        "B17.01", ["Toan-ho-hap", "Cut-off"],
    ),
    basic(
        "PED11-B17-02", "B17", "Nhiễm toan hô hấp", 2,
        f"{B('[Toan hô hấp — nguyên nhân]')} Kể các {Y('nguyên nhân')} gây nhiễm toan hô hấp.",
        f"1) {R('Viêm phổi')}.<br>2) {R('Viêm tiểu phế quản')}.<br>3) {R('Hen phế quản')}.<br>4) {R('Nhược cơ')}.<br>"
        f"5) {R('Mảng sườn di động')}.<br>6) {R('Tràn dịch, tràn khí màng phổi')}.<br>7) {R('Viêm não')}.<br>8) {R('Xuất huyết não')}.",
        "Nhóm nguyên nhân gồm bệnh phổi (giảm thông khí/trao đổi), thần kinh trung ương và cơ–thành ngực (giảm thông khí do "
        "yếu cơ, đau, tràn khí): tất cả làm CO₂ ứ đọng.",
        "B17.02", ["Toan-ho-hap", "Nguyen-nhan"],
    ),
    cloze(
        "PED11-CL-B17-01", "B17", "Nhiễm toan hô hấp",
        "Toan hô hấp khi PaCO₂ {{c1::> 50 mmHg}}.",
        "B17.01", ["Cut-off"],
    ),

    # ------------------------------------------------------------ B18. Nguyên nhân toan chuyển hóa
    basic(
        "PED11-B18-01", "B18", "Nhiễm toan chuyển hóa", 1,
        f"{B('[Toan chuyển hóa — định nghĩa]')} Nhiễm toan chuyển hóa khi {Y('HCO₃⁻')} nhỏ hơn bao nhiêu?",
        f"Khi {Y('HCO₃⁻ < 22 mEq/l')}.",
        "Ngưỡng 22 mEq/l là cut-off của toan chuyển hóa (bình thường 22–26 mEq/l). Dưới đây là các nguyên nhân.",
        "B18.01", ["Toan-chuyen-hoa", "Cut-off"],
    ),
    basic(
        "PED11-B18-02", "B18", "Nhiễm toan chuyển hóa", 2,
        f"{B('[Toan chuyển hóa — nguyên nhân]')} Kể các {Y('nguyên nhân')} gây nhiễm toan chuyển hóa.",
        f"1) {R('Suy hô hấp')}.<br>2) {R('Shock nhiễm khuẩn')}.<br>3) {R('Tiêu chảy cấp')}.<br>"
        f"4) {R('Đái đường')}.<br>5) {R('Nhiễm toan ống thận')}.",
        "Nhóm nguyên nhân gồm tăng acid (shock, đái đường – nhiễm toan ceton), mất HCO₃⁻ (tiêu chảy, nhiễm toan ống thận) và "
        "suy hô hấp gây tích lũy acid. Phân biệt đúng nguyên nhân quyết định điều trị ở thẻ B20.",
        "B18.02", ["Toan-chuyen-hoa", "Nguyen-nhan"],
    ),
    cloze(
        "PED11-CL-B18-01", "B18", "Nhiễm toan chuyển hóa",
        "Toan chuyển hóa khi HCO₃⁻ {{c1::< 22 mEq/l}}.",
        "B18.01", ["Cut-off"],
    ),

    # ------------------------------------------------------------ B19. Triệu chứng nhiễm toan
    basic(
        "PED11-B19-01", "B19", "Triệu chứng nhiễm toan", 1,
        f"{B('[Triệu chứng lâm sàng của nhiễm toan]')} Kể các {Y('triệu chứng')} lâm sàng của nhiễm toan.",
        f"1) {R('Giãn mạch')}.<br>2) {R('Thở Kussmaul')}.<br>3) {R('Giảm huyết áp')}.<br>4) {R('Loạn nhịp tim')}.",
        "Toan gây giãn mạch ngoại vi và giảm đáp ứng với catecholamin, dẫn đến tụt huyết áp; thở Kussmaul là bù trừ hô hấp "
        "(thở sâu, nhanh) để thải CO₂; loạn nhịp do ảnh hưởng điện giải và co bóp cơ tim.",
        "B19.01", ["Trieu-chung", "Toan"],
    ),

    # ------------------------------------------------------------ B20. Điều trị nhiễm toan
    basic(
        "PED11-B20-01", "B20", "Điều trị nhiễm toan", 1,
        f"{B('[Điều trị nhiễm toan — nguyên tắc]')} Nguyên tắc điều trị nhiễm toan là gì?",
        f"{G('Điều trị theo nguyên nhân')}.",
        "Bù kiềm chỉ là hỗ trợ: phải xử trí nguyên nhân gốc (shock, đái đường, mất dịch tiêu chảy, suy hô hấp) để toan thực sự được sửa.",
        "B20.01", ["Dieu-tri", "Nguyen-tac"],
    ),
    basic(
        "PED11-B20-02", "B20", "Điều trị nhiễm toan", 2,
        f"{B('[Bù kiềm NaHCO₃ — công thức]')} Công thức tính lượng {Y('NaHCO₃')} (mEq) cần bù theo {Y('P')} và {Y('BE')} là gì?",
        f"{B('NaHCO₃ (mEq) = 0,3 × P × BE')}.<br>(P = cân nặng; BE = base excess đo được.)",
        "Công thức ước tính lượng kiềm cần thiết để đưa BE về 0 với hệ số 0,3 (phản ánh thể tích phân bố đệm). Trong thực hành "
        "thường bù một phần và đánh giá lại khí máu.",
        "B20.02", ["Dieu-tri", "Cong-thuc"],
    ),
    basic(
        "PED11-B20-03", "B20", "Điều trị nhiễm toan", 2,
        f"{B('[NaHCO₃ 8,4%]')} {Y('1 ml')} NaHCO₃ 8,4% tương đương bao nhiêu {Y('mEq')}?",
        f"{G('1 ml NaHCO₃ 8,4% = 1 mEq')}.",
        "Dung dịch 8,4% là đậm đặc (1 mEq/ml), dùng để bù nhanh khi cần, thường pha loãng khi truyền ngoại vi.",
        "B20.03", ["Dieu-tri", "Nong-do"],
    ),
    basic(
        "PED11-B20-04", "B20", "Điều trị nhiễm toan", 2,
        f"{B('[NaHCO₃ 4,2%]')} {Y('1 ml')} NaHCO₃ 4,2% tương đương bao nhiêu? (theo handout)",
        f"{G('1 ml NaHCO₃ 4,2% = 0,5 mEq/l')}. "
        f"{R('(sic — đơn vị đúng theo nồng độ là mEq/ml, không phải mEq/l)')}.",
        "Handout ghi đơn vị 'mEq/l' cho 1 ml, đây là lỗi in: nồng độ 4,2% tương ứng 0,5 mEq trên mỗi ml. Đối chiếu bảng "
        "nồng độ dung dịch trước khi tính liều thực.",
        "B20.04", ["Dieu-tri", "Nong-do", "Sic"],
    ),
    basic(
        "PED11-B20-05", "B20", "Điều trị nhiễm toan", 2,
        f"{B('[NaHCO₃ 1,4%]')} {Y('1 ml')} NaHCO₃ 1,4% tương đương bao nhiêu? (theo handout)",
        f"{G('1 ml NaHCO₃ 1,4% = 1/6 mEq/l')}. "
        f"{R('(sic — đơn vị đúng theo nồng độ là mEq/ml, không phải mEq/l)')}.",
        "Tương tự thẻ B20.04: đơn vị trong handout là lỗi in (mEq/ml đúng). Khi tính liều dùng công thức nồng độ, không dùng đơn vị in sai.",
        "B20.05", ["Dieu-tri", "Nong-do", "Sic"],
    ),

    # ------------------------------------------------------------ B21. Nhiễm kiềm hô hấp
    basic(
        "PED11-B21-01", "B21", "Nhiễm kiềm hô hấp", 1,
        f"{B('[Kiềm hô hấp — định nghĩa]')} Nhiễm kiềm hô hấp khi {Y('PaCO₂')} nhỏ hơn bao nhiêu?",
        f"Khi {Y('PaCO₂ < 35 mmHg')}.",
        "Ngưỡng 35 mmHg là cut-off kiềm hô hấp (bình thường 35–45 mmHg): thông khí quá mức đào thải CO₂.",
        "B21.01", ["Kiem-ho-hap", "Cut-off"],
    ),
    basic(
        "PED11-B21-02", "B21", "Nhiễm kiềm hô hấp", 2,
        f"{B('[Kiềm hô hấp — nguyên nhân]')} Kể các {Y('nguyên nhân')} gây nhiễm kiềm hô hấp.",
        f"1) {R('Tăng thông khí')}.<br>2) {R('Hồi hộp')}.<br>3) {R('Hen phế quản')}.<br>4) {R('Thở máy')}.",
        "Các nguyên nhân đều làm tăng thông khí phế nang (tự nhiên do lo âu/hen, hoặc do máy thở đặt quá mức), thải CO₂ quá nhiều.",
        "B21.02", ["Kiem-ho-hap", "Nguyen-nhan"],
    ),
    basic(
        "PED11-B21-03", "B21", "Nhiễm kiềm hô hấp", 2,
        f"{B('[Kiềm hô hấp — triệu chứng]')} Kể các {Y('triệu chứng')} của nhiễm kiềm hô hấp.",
        f"1) {R('Đau đầu')}.<br>2) {R('Li bì')}.<br>3) {R('Tetani')}.",
        "Kiềm làm giảm Ca²⁺ ion hóa nên dễ co cứng cơ (tetani); li bì, đau đầu do thay đổi lưu lượng máu não.",
        "B21.03", ["Trieu-chung", "Kiem"],
    ),
    basic(
        "PED11-B21-04", "B21", "Nhiễm kiềm hô hấp", 2,
        f"{B('[Kiềm hô hấp — điều trị]')} Điều trị nhiễm kiềm hô hấp bằng {Y('những biện pháp')} nào?",
        f"1) {G('Thở lại (rebreathing)')}.<br>2) {G('Điều chỉnh máy thở')}.",
        "Thở lại trong túi/mặt nạ làm tăng CO₂ hít vào; điều chỉnh máy thở giảm thể tích/tần số để bớt thải CO₂.",
        "B21.04", ["Dieu-tri", "Kiem-ho-hap"],
    ),
    cloze(
        "PED11-CL-B21-01", "B21", "Nhiễm kiềm hô hấp",
        "Kiềm hô hấp khi PaCO₂ {{c1::< 35 mmHg}}.",
        "B21.01", ["Cut-off"],
    ),

    # ------------------------------------------------------------ B22. Nhiễm kiềm chuyển hóa
    basic(
        "PED11-B22-01", "B22", "Nhiễm kiềm chuyển hóa", 1,
        f"{B('[Kiềm chuyển hóa — định nghĩa]')} Nhiễm kiềm chuyển hóa khi {Y('HCO₃⁻')} lớn hơn bao nhiêu?",
        f"Khi {Y('HCO₃⁻ > 26 mEq/l')}.",
        "Ngưỡng 26 mEq/l là cut-off kiềm chuyển hóa (bình thường 22–26 mEq/l). Dưới đây là các nguyên nhân.",
        "B22.01", ["Kiem-chuyen-hoa", "Cut-off"],
    ),
    basic(
        "PED11-B22-02", "B22", "Nhiễm kiềm chuyển hóa", 2,
        f"{B('[Kiềm chuyển hóa — nguyên nhân]')} Kể các {Y('nguyên nhân')} gây nhiễm kiềm chuyển hóa.",
        f"1) {R('Nôn nhiều')}.<br>2) {R('Hút dịch dạ dày')}.<br>3) {R('Truyền nhiều máu')}.<br>"
        f"4) {R('Penicillin')}.<br>5) {R('Hôn mê gan')}.",
        "Mất acid dạ dày (nôn, hút dạ dày) làm dư HCO₃⁻; truyền máu chứa citrat chuyển hóa thành HCO₃⁻; penicillin và hôn mê gan "
        "liên quan thay đổi bài tiết/chuyển hóa ion.",
        "B22.02", ["Kiem-chuyen-hoa", "Nguyen-nhan"],
    ),
    basic(
        "PED11-B22-03", "B22", "Nhiễm kiềm chuyển hóa", 2,
        f"{B('[Kiềm chuyển hóa — triệu chứng]')} Kể các {Y('triệu chứng')} của nhiễm kiềm chuyển hóa.",
        f"1) {R('Đau đầu')}.<br>2) {R('Li bì')}.<br>3) {R('Tetani')}.",
        "Cùng bộ ba triệu chứng với nhiễm kiềm hô hấp (thẻ B21.03): kiềm làm giảm Ca²⁺ ion hóa, gây co cứng cơ và thay đổi thần kinh.",
        "B22.03", ["Trieu-chung", "Kiem"],
    ),
    basic(
        "PED11-B22-04", "B22", "Nhiễm kiềm chuyển hóa", 2,
        f"{B('[Kiềm chuyển hóa — điều trị]')} Điều trị nhiễm kiềm chuyển hóa bằng {Y('những thuốc/dịch')} nào?",
        f"1) {G('Truyền NaCl')}.<br>2) {G('Truyền NH₄Cl')}.<br>3) {G('Canxi gluconat')}.",
        "Truyền NaCl làm đào thải HCO₃⁻ qua thận (thể tích và clo); NH₄Cl cung cấp acid; canxi gluconat xử trí tetani do Ca²⁺ ion hóa giảm.",
        "B22.04", ["Dieu-tri", "Kiem-chuyen-hoa"],
    ),
    cloze(
        "PED11-CL-B22-01", "B22", "Nhiễm kiềm chuyển hóa",
        "Kiềm chuyển hóa khi HCO₃⁻ {{c1::> 26 mEq/l}}.",
        "B22.01", ["Cut-off"],
    ),
]
