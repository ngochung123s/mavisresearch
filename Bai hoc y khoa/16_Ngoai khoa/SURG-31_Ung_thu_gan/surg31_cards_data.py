"""
Dữ liệu thẻ Anki chuẩn hóa cho bài SURG-31: Ung Thư Gan
Rebuild 100% từ barem: SURG-31_Ung_thu_gan_BAREM.md
"""

def _c(hex_col: str, text: str) -> str:
    return f'<span style="color: {hex_col}; font-weight: bold;">{text}</span>'

def R(text: str) -> str:
    return _c("#ff6b6b", text)

def Y(text: str) -> str:
    return _c("#ffd43b", text)

def G(text: str) -> str:
    return _c("#51cf66", text)

def B(text: str) -> str:
    return _c("#74c0fc", text)

def clz(n: int, inner: str) -> str:
    return f"{{{{c{n}::{inner}}}}}"

def basic(cid, section, topic, tier, front, core, ai, barem, tags, red_flag=False, asks=None):
    b_tag = f"Ngoai::SURG-31::{section}"
    t_tag = f"Tier-{tier}"
    all_tags = [b_tag, t_tag] + [f"Ngoai::{t}" for t in tags]
    if red_flag:
        all_tags.append("Ngoai::Co-do")
    
    back = f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}"
    
    res = {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "front": front,
        "back": back,
        "extra": f"[{barem}]",
        "tags": all_tags,
    }
    if asks:
        res["asks"] = asks
    return res

def algo(cid, section, category, title, core, ai, barem, tags, asks=None):
    front = f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {G(category)}: {Y(title)}"
    return basic(
        cid, section, f"Thuật toán: {title}", 1,
        front, core, ai, barem, tags + ["Thuat-toan-Quyet-dinh"], asks=asks
    )

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False, asks=None):
    prefix = f"🛑 {R('CỜ ĐỎ CẤP CỨU')} — " if red_flag else f"❌ {Y('BẪY LÂM SÀNG')} — "
    full_front = f"{prefix}{front}"
    return basic(
        cid, section, f"Bẫy: {topic}", 1,
        full_front, core, ai, barem, tags + (["Co-do"] if red_flag else ["Bay-lam-sang"]),
        red_flag=red_flag, asks=asks
    )

def cloze(cid, section, topic, text, barem, tags):
    b_tag = f"Ngoai::SURG-31::{section}"
    all_tags = [b_tag, "Tier-2"] + [f"Ngoai::{t}" for t in tags]
    return {
        "id": cid,
        "type": "cloze",
        "section": section,
        "topic": topic,
        "tier": 2,
        "text": text,
        "extra": f"[{barem}]",
        "tags": all_tags,
    }

cards_data = [
    # ============================================================
    # B0. ĐẠI CƯƠNG (HCC & HEPATOBLASTOMA)
    # ============================================================
    basic(
        "SURG31-B0-01", "B0", "Đại cương & Bệnh sinh HCC", 1,
        f"{B('[Đại cương Ung thư gan]')} Ung thư biểu mô tế bào gan ({G('HCC')}) xuất phát từ đâu, xuất hiện trên nền bệnh lý gì và vai trò của {R('Virus viêm gan B (HBV)')}?",
        f"1) <b>Nguồn gốc tế bào:</b> Xuất phát từ {G('tế bào biểu mô của gan')}; là loại ung thư gan hay gặp và chủ yếu nhất.<br>"
        f"2) <b>Nền tảng bệnh sinh:</b> Nhu mô gan bình thường rất hiếm sinh ung thư — hầu hết xuất hiện trên {R('nền xơ gan')} (hậu quả của xơ gan hoặc đồng thời xuất hiện cùng xơ gan).<br>"
        f"3) <b>Vai trò virus HBV:</b> {R('Virus viêm gan B (HBV)')} lây qua đường máu (tiêm truyền, mẹ truyền sang con khi đẻ) gây viêm gan cấp → viêm gan mạn tiến triển âm thầm nhiều năm → xơ gan và ung thư gan.",
        "Tại Việt Nam, tỷ lệ nhiễm HBV trong cộng đồng rất cao là căn nguyên gốc rễ khiến HCC đứng hàng đầu trong các bệnh ác tính đường tiêu hóa.",
        "B0.01, B0.02, B0.03", ["Dai-cuong", "HBV", "Benh-sinh"],
    ),
    basic(
        "SURG31-B0-02", "B0", "Dịch tễ & Tiên lượng HCC", 1,
        f"{B('[Dịch tễ & Tiên lượng HCC]')} Thứ hạng mắc tại Việt Nam, {Y('giới tính, lứa tuổi')}, giải pháp phòng bệnh và vì sao {R('tiên lượng u ám')}?",
        f"1) <b>Tình hình tại Việt Nam:</b> Chiếm {Y('vị trí thứ 3')} trong tất cả các ung thư; nam gặp nhiều hơn nữ; độ tuổi thường gặp từ {Y('50 đến 60 tuổi')}.<br>"
        f"2) <b>Phòng tránh:</b> {G('Tiêm phòng vắc-xin viêm gan B')} và {G('hạn chế bia rượu')} là giải pháp thực tiễn hiệu quả nhất.<br>"
        f"3) <b>Bối cảnh tiên lượng:</b> Tình trạng {R('xơ gan phối hợp')} với ung thư nhiều ổ, độc ác tính cao, tiến triển nhanh nên rất khó điều trị triệt căn (chỉ 5–10% cắt được).",
        "Xơ gan làm giảm sút chức năng gan khiến bệnh nhân dễ suy gan mất bù sau phẫu thuật, cộng với đặc tính di căn vi mạch cửa sớm làm tiên lượng điều trị rất dè dặt.",
        "B0.04, B0.05", ["Dich-te", "Tien-luong"],
    ),
    basic(
        "SURG31-B0-03", "B0", "Ung thư nguyên bào gan trẻ em", 1,
        f"{B('[Ung thư nguyên bào gan trẻ em]')} Nguồn gốc, mối liên quan {Y('HBV')}, đặc điểm mô học, tính nhạy cảm {G('hóa trị')} và lứa tuổi mắc?",
        f"1) <b>Nguồn gốc tế bào:</b> Xuất phát từ {B('nguyên bào gan')} (dạng tế bào bào thai gần như không biệt hóa ở trẻ em).<br>"
        f"2) <b>Mối liên quan HBV:</b> {R('Hoàn toàn không liên quan đến virus viêm gan B')}.<br>"
        f"3) <b>Tính chất nhạy hóa trị:</b> Phát triển rất nhanh nhưng {G('rất nhạy cảm với hóa trị chống ung thư')} — đặc điểm {Y('trái ngược hoàn toàn với HCC')} (HCC gần như không đáp ứng hóa chất).<br>"
        f"4) <b>Tần suất &amp; lứa tuổi:</b> Tỷ lệ mắc {Y('11,2 / 1.000.000 trẻ sơ sinh')}; {R('95% gặp ở trẻ dưới 4 tuổi')} (chỉ 5% trên 4 tuổi); tuổi chẩn đoán trung bình {Y('19 tháng tuổi')}.",
        "Hepatoblastoma là một trong những thành tựu lớn của ung thư nhi khoa nhờ khối u co nhỏ ngoạn mục sau hóa trị tân bổ trợ, giúp biến khối u không cắt được thành cắt được an toàn.",
        "B0.06, B0.07", ["Hepatoblastoma", "Nhi-khoa", "Hoa-tri"],
    ),
    cloze(
        "SURG31-B0-04", "B0", "Con số dịch tễ Hepatoblastoma",
        f"Ung thư nguyên bào gan trẻ em có tỷ lệ mắc {clz(1, Y('11,2/1.000.000 trẻ sơ sinh'))}, trong đó bệnh nhân dưới 4 tuổi chiếm {clz(2, R('95%'))} và tuổi chẩn đoán trung bình là {clz(3, Y('19 tháng tuổi'))}.",
        "B0.07", ["Hepatoblastoma", "Nguong-so"],
    ),

    # ============================================================
    # B1. CHẨN ĐOÁN HCC
    # ============================================================
    basic(
        "SURG31-B1-01", "B1", "Lâm sàng & Tầm soát sớm HCC", 1,
        f"{B('[Lâm sàng & Tầm soát HCC]')} Vì sao chẩn đoán sớm HCC rất khó, công cụ nào giúp {G('phát hiện sớm')} và {Y('10 triệu chứng lâm sàng')} khi bệnh xuất hiện muộn?",
        f"1) <b>Khó khăn chẩn đoán sớm:</b> Bệnh tiến triển âm thầm không triệu chứng; khi xuất hiện triệu chứng lâm sàng rầm rộ thường đã {R('hết khả năng điều trị khỏi')}.<br>"
        f"2) <b>Chiến lược phát hiện sớm:</b> {G('Siêu âm gan định kỳ')} chủ động phát hiện khối u nhỏ ở nhóm nguy cơ cao (xơ gan, viêm gan B mạn).<br>"
        f"3) <b>Hội chứng lâm sàng muộn:</b> Đau tức nặng vùng gan, {Y('đau xuyên lên vai phải')}, đau lưng, {R('gan to dưới bờ sườn')}, mệt mỏi kém ăn, sốt nhẹ về chiều, vàng da vàng mắt, {R('cổ trướng')}, phù hai chi dưới, mất vui thú, gầy sút không rõ lý do.",
        "Đau xuyên lên vai phải là do tổn thương gan kích thích thần kinh hoành mặt dưới cơ hoành. Khi có cổ trướng và vàng da thì hầu như u đã ở giai đoạn Child-Pugh B, C.",
        "B1.01, B1.02", ["Lam-sang", "Sieu-am", "Tam-soat"],
    ),
    basic(
        "SURG31-B1-02", "B1", "Siêu âm & CT Scanner trong HCC", 1,
        f"{B('[Chẩn đoán hình ảnh HCC]')} Giá trị của {G('Siêu âm (ngưỡng kích thước, quầng giảm âm)')} và dấu hiệu kinh điển trên {B('CT Scanner')}?",
        f"1) <b>Siêu âm thường &amp; Doppler:</b> Phát hiện u có kích thước {Y('≥ 1 cm')}; dấu hiệu {G('quầng giảm siêu âm quanh u')} tương đối đặc hiệu (nhiều khi tốt hơn CT); Doppler màu giúp {B('phân biệt HCC với u máu lành tính')}; phát hiện {R('huyết khối tĩnh mạch cửa')}.<br>"
        f"2) <b>CT Scanner gan có cản quang:</b> Dấu hiệu kinh điển là {G('ngấm thuốc nhanh thì động mạch và thải thuốc nhanh thì tĩnh mạch (wash-out)')}.<br>"
        f"3) <b>Vai trò CT:</b> Xác định vị trí, số lượng, định khu hạ phân thùy, đánh giá khả năng cắt u, di căn/ổ vệ tinh, xơ gan, lách to, cổ trướng.",
        "Hiện tượng wash-out phản ánh khối ung thư được nuôi chủ yếu bằng động mạch gan và các mạch máu xung quanh, tương phản với mô hình cấp máu của nhu mô gan lành.",
        "B1.03, B1.04", ["Sieu-am", "CT-Scanner", "Wash-out"],
    ),
    basic(
        "SURG31-B1-03", "B1", "Xét nghiệm AFP & Sinh thiết Menghini", 1,
        f"{B('[Xét nghiệm & Sinh thiết HCC]')} Ngưỡng {Y('AFP dương tính')}, tỷ lệ AFP cao {R('> 3.500 ng/ml')}, chỉ định {G('sinh thiết kim Menghini')} và 2 công thức chẩn đoán thực tế?",
        f"1) <b>Dấu ấn sinh học AFP:</b> Nồng độ {Y('AFP > 200 ng/ml')} được coi là dương tính; khoảng {R('70% bệnh nhân')} có AFP cao {R('> 3.500 ng/ml')}; AFP(+) kèm {B('HBsAg(+)')} giá trị càng cao.<br>"
        f"2) <b>Kỹ thuật sinh thiết Menghini:</b> Chỉ định dưới hướng dẫn siêu âm khi có khối u nghi ngờ HCC nhưng {Y('AFP âm tính')}; nếu u nhỏ/vị trí khó thì mổ thăm dò + sinh thiết tức thì.<br>"
        f"3) <b>Hai công thức chẩn đoán thực tế:</b><br>"
        f"   • {G('Khối u gan + AFP > 200 ng/ml = Ung thư biểu mô tế bào gan (HCC)')}.<br>"
        f"   • {G('Khối u gan + Sinh thiết HCC = Ung thư gan')}.",
        "Nếu AFP âm tính nhưng bệnh nhân có HBsAg(+) và khối u trên siêu âm thì tuyệt đối không được loại trừ ung thư mà phải làm sinh thiết kim hoặc chụp CT đa dãy đối chiếu.",
        "B1.05, B1.06, B1.07", ["AFP", "Sinh-thiet", "Cong-thuc"],
    ),
    basic(
        "SURG31-B1-04", "B1", "Chẩn đoán phân biệt HCC", 1,
        f"{B('[Chẩn đoán phân biệt HCC]')} Cần phân biệt ung thư biểu mô tế bào gan với {Y('5 nhóm tổn thương gan')} nào?",
        f"1) {G('Áp xe gan')}.<br>"
        f"2) {G('U máu gan lành tính (Hemangioma)')} (phân biệt nhờ siêu âm Doppler màu và chụp CT Scanner).<br>"
        f"3) {G('U nang gan')}.<br>"
        f"4) {Y('Ung thư đường mật trong gan (Cholangiocarcinoma)')}.<br>"
        f"5) {R('Ung thư di căn gan')} (từ {B('dạ dày, đại tràng, trực tràng...')}).",
        "Trên bệnh nhân có xơ gan và nhiễm virus viêm gan B mạn, bất kỳ khối u đặc mới xuất hiện nào cũng phải ưu tiên nghĩ tới HCC đầu tiên cho đến khi có bằng chứng ngược lại.",
        "B1.08", ["Chan-doan-phan-biet", "Hemangioma", "Di-can-gan"],
    ),
    cloze(
        "SURG31-B1-05", "B1", "Ngưỡng số AFP & Siêu âm",
        f"Siêu âm có khả năng phát hiện khá cao khối u gan kích thước {clz(1, Y('≥ 1 cm'))}; nồng độ AFP trên {clz(2, Y('200 ng/ml'))} được coi là dương tính và khoảng {clz(3, R('70%'))} bệnh nhân HCC có nồng độ AFP cao trên {clz(4, R('3.500 ng/ml'))}.",
        "B1.03, B1.05", ["AFP", "Nguong-so"],
    ),

    # ============================================================
    # B2. ĐÁNH GIÁ XƠ GAN PHỐI HỢP (THANG ĐIỂM CHILD-PUGH)
    # ============================================================
    basic(
        "SURG31-B2-01", "B2", "Phân loại Child-Pugh A, B, C", 1,
        f"{B('[Đánh giá xơ gan Child-Pugh]')} Điểm số và mức độ của {G('Child-Pugh A')}, {Y('Child-Pugh B')} và {R('Child-Pugh C')}?",
        f"1) {G('Xơ gan Child-Pugh A')}: {G('5 – 6 điểm')} — mức độ {G('nhẹ')} (chức năng gan còn bù tốt, là ứng viên tốt nhất cho phẫu thuật cắt gan).<br>"
        f"2) {Y('Xơ gan Child-Pugh B')}: {Y('7 – 9 điểm')} — mức độ {Y('vừa')} (suy giảm chức năng gan trung bình, cân nhắc can thiệp thận trọng).<br>"
        f"3) {R('Xơ gan Child-Pugh C')}: {R('≥ 10 điểm')} — mức độ {R('nặng')} (suy gan mất bù nặng, chống chỉ định phẫu thuật cắt gan, chỉ điều trị giảm nhẹ hoặc ghép gan).",
        "Thang điểm Child-Pugh là yếu tố tiên quyết quyết định sống còn bệnh nhân trước mọi chỉ định can thiệp ngoại khoa hay tắc mạch.",
        "B2.01", ["Child-Pugh", "Phan-do"],
    ),
    basic(
        "SURG31-B2-02", "B2", "5 chỉ số bảng điểm Child-Pugh", 1,
        f"{B('[Bảng điểm Child-Pugh]')} Kể tên {Y('5 chỉ số')} đánh giá và tiêu chuẩn tương ứng mức {G('1 điểm')} của từng chỉ số?",
        f"1) <b>Bilirubin máu:</b> {G('< 35 µmol/L')} (1 điểm).<br>"
        f"2) <b>Cổ trướng:</b> {G('Không có (0)')} (1 điểm).<br>"
        f"3) <b>Albumin máu:</b> {G('> 35 g/L')} (1 điểm).<br>"
        f"4) <b>Hội chứng não gan:</b> {G('Không có (0)')} (1 điểm).<br>"
        f"5) <b>Đông máu (Tỷ lệ Prothrombin):</b> {G('100 – 55%')} (1 điểm).",
        "Mức 1 điểm phản ánh tình trạng chức năng gan còn hoàn toàn bình thường hoặc suy giảm không đáng kể trên cả 5 phương diện lâm sàng và xét nghiệm.",
        "B2.02, B2.03", ["Child-Pugh", "Chi-so", "1-diem"],
    ),
    basic(
        "SURG31-B2-03", "B2", "Mốc 2 điểm và 3 điểm Child-Pugh", 1,
        f"{B('[Bảng điểm Child-Pugh]')} Chi tiết ngưỡng giá trị {Y('2 điểm')} và {R('3 điểm')} cho cả 5 chỉ số của Child-Pugh?",
        f"1) <b>Bilirubin máu:</b> {Y('35 – 50 µmol/L')} (2 điểm) | {R('> 50 µmol/L')} (3 điểm).<br>"
        f"2) <b>Cổ trướng:</b> {Y('Ít (+/-)')} (2 điểm) | {R('Nhiều (++)')} (3 điểm).<br>"
        f"3) <b>Albumin máu:</b> {Y('28 – 35 g/L')} (2 điểm) | {R('< 28 g/L')} (3 điểm).<br>"
        f"4) <b>Hội chứng não gan:</b> {Y('Độ 1 – 2 (+)')} (2 điểm) | {R('Độ 3 – 4 (++)')} (3 điểm).<br>"
        f"5) <b>Đông máu (Tỷ lệ Prothrombin):</b> {Y('53 – 45%')} (2 điểm) | {R('< 45%')} (3 điểm).",
        "Ghi nhớ các mốc đối xứng: Bilirubin 35-50, Albumin 28-35 g/L, và Prothrombin 45-53% là các khoảng phân chia ranh giới giữa 1, 2 và 3 điểm.",
        "B2.04", ["Child-Pugh", "Nguong-so", "Bang-diem"],
    ),
    cloze(
        "SURG31-B2-04", "B2", "Khoảng điểm Child-Pugh",
        f"Thang điểm Child-Pugh phân loại: Child-Pugh A từ {clz(1, G('5 – 6 điểm'))} (nhẹ); Child-Pugh B từ {clz(2, Y('7 – 9 điểm'))} (vừa); Child-Pugh C khi đạt {clz(3, R('≥ 10 điểm'))} (nặng).",
        "B2.01", ["Child-Pugh", "Nguong-so"],
    ),

    # ============================================================
    # B3. PHÂN LOẠI TNM & GIAI ĐOẠN AJCC 2010 (HCC)
    # ============================================================
    basic(
        "SURG31-B3-01", "B3", "Phân loại T theo AJCC 2010", 1,
        f"{B('[Phân loại TNM AJCC 2010]')} Định nghĩa các mức {G('T1')}, {Y('T2')}, {Y('T3a')}, {R('T3b')} và {R('T4')} trong ung thư biểu mô tế bào gan?",
        f"1) {G('T1')}: Khối u đơn độc {G('chưa xâm lấn mạch máu')}.<br>"
        f"2) {Y('T2')}: Khối u đơn độc {Y('có xâm lấn mạch máu')} HOẶC {Y('nhiều u kích thước ≤ 5 cm')}.<br>"
        f"3) {Y('T3a')}: {Y('Nhiều u kích thước > 5 cm')}.<br>"
        f"4) {R('T3b')}: Một hay nhiều u kích thước bất kỳ {R('liên quan với nhánh chính tĩnh mạch cửa hoặc tĩnh mạch gan')}.<br>"
        f"5) {R('T4')}: U {R('xâm lấn trực tiếp cơ quan lân cận')} (trừ túi mật) hoặc {R('xuyên qua phúc mạc tạng')}.",
        "Lưu ý bẫy trắc nghiệm: U xâm lấn túi mật KHÔNG xếp vào T4 vì túi mật nằm sát giường gan sinh lý; T4 phải xâm lấn cơ quan khác hoặc thủng phúc mạc.",
        "B3.01", ["TNM", "T-stage", "AJCC2010"],
    ),
    basic(
        "SURG31-B3-02", "B3", "Các giai đoạn TNM (AJCC 2010)", 1,
        f"{B('[Xếp giai đoạn AJCC 2010]')} Ghép cặp tương ứng các giai đoạn {G('I')}, {Y('II')}, {Y('IIIA/B/C')} và {R('IVA/B')} với tổ hợp TNM?",
        f"1) {G('Giai đoạn I')}: {G('T1 N0 M0')}.<br>"
        f"2) {Y('Giai đoạn II')}: {Y('T2 N0 M0')}.<br>"
        f"3) {Y('Giai đoạn IIIA')}: {Y('T3a N0 M0')} | {Y('Giai đoạn IIIB')}: {Y('T3b N0 M0')} | {Y('Giai đoạn IIIC')}: {Y('T4 N0 M0')}.<br>"
        f"4) {R('Giai đoạn IVA')}: {R('T bất kỳ N1 M0')} (đã có di căn hạch vùng).<br>"
        f"5) {R('Giai đoạn IVB')}: {R('T bất kỳ N bất kỳ M1')} (đã có di căn xa).",
        "Chỉ cần có hạch vùng N1 là xếp ngay IVA; có bất kỳ di căn xa M1 nào lập tức là giai đoạn IVB.",
        "B3.02, B3.03, B3.04", ["TNM", "Giai-doan", "AJCC2010"],
    ),
    basic(
        "SURG31-B3-03", "B3", "Tiêu chuẩn T2 và T3a theo AJCC 2010", 2,
        f"{B('[Phân loại T AJCC 2010]')} Tiêu chuẩn phân định giữa {Y('T2')} và {R('T3a')} trong ung thư biểu mô tế bào gan?",
        f"1) <b>T2 (u đơn độc mạch máu hoặc nhiều u ≤ 5 cm):</b> Khối u đơn độc {Y('có xâm lấn mạch máu')} HOẶC {Y('nhiều u kích thước ≤ 5 cm')}.<br>"
        f"2) <b>T3a (nhiều u kích thước > 5 cm):</b> {R('Nhiều khối u kích thước lớn hơn 5 cm')}.",
        "Ngưỡng 5 cm là ranh giới sống còn: nhiều u nhưng tất cả ≤ 5 cm vẫn xếp T2, chỉ cần có nhiều u > 5 cm là chuyển sang T3a.",
        "B3.01", ["TNM", "T2", "T3a"],
    ),

    # ============================================================
    # B4. CHẨN ĐOÁN & XẾP LOẠI HEPATOBLASTOMA Ở TRẺ EM
    # ============================================================
    basic(
        "SURG31-B4-01", "B4", "Đặc điểm chẩn đoán Hepatoblastoma", 1,
        f"{B('[Chẩn đoán Ung thư nguyên bào gan]')} Triệu chứng lâm sàng, hình ảnh u trên {B('CT/Siêu âm')}, xét nghiệm {Y('AFP & HBsAg')} và vai trò {G('sinh thiết kim')}?",
        f"1) <b>Khám lâm sàng:</b> Chẩn đoán tương đối dễ hơn HCC; bệnh nhi {Y('≤ 4 tuổi (95%)')} có {R('khối u gan lớn dưới bờ sườn')}, ít khi gây vàng da tắc mật.<br>"
        f"2) <b>Hình ảnh:</b> Siêu âm/CT thấy khối u gan lớn, {G('thường 1 ổ, cá biệt 2 ổ')}, u chiếm phần lớn thể tích gan.<br>"
        f"3) <b>Dấu ấn sinh học:</b> {R('AFP rất cao')}, kháng nguyên bề mặt {G('HBsAg âm tính')} (không liên quan viêm gan B).<br>"
        f"4) <b>Sinh thiết kim:</b> Cần thiết để xác định chẩn đoán giúp {G('chỉ định hóa trị trước mổ (tân bổ trợ)')}.",
        "Khác với HCC thường đa ổ rải rác trên gan xơ, Hepatoblastoma thường là khối u đơn độc khổng lồ phát triển trên nền gan lành của trẻ nhỏ.",
        "B4.01, B4.02", ["Hepatoblastoma", "Lam-sang", "AFP"],
    ),
    basic(
        "SURG31-B4-02", "B4", "Phân loại Nhi khoa 1995 (Giai đoạn I–IV)", 1,
        f"{B('[Phân loại Ung thư nhi khoa 1995]')} Tiêu chuẩn xếp loại 4 giai đoạn {G('I')}, {Y('II')}, {Y('III')} và {R('IV')} của Ung thư nguyên bào gan?",
        f"1) {G('Giai đoạn I')}: Cắt bỏ được hoàn toàn, dạng bào thai thuần túy, độ mô học thấp, có {G('< 2 nhân chia / 1 vi trường')}.<br>"
        f"2) {Y('Giai đoạn II')}: Cắt bỏ được hoàn toàn, dạng bào thai thuần túy, độ mô học cao, có {Y('> 2 nhân chia / 1 vi trường')}.<br>"
        f"3) {Y('Giai đoạn III')}: Lấy bỏ hết đại thể nhưng {Y('sót u về vi thể')} HOẶC u giai đoạn I, II nhưng {R('đã vỡ u trước mổ')}.<br>"
        f"4) {R('Giai đoạn IV')}: Khối u {R('không thể cắt được')} HOẶC {R('có di căn hạch / di căn phổi hoặc cơ quan khác')}.",
        "Mốc 2 nhân chia/vi trường là ranh giới giữa GĐ I và II; vỡ u trước mổ tự động nâng giai đoạn bệnh lên Giai đoạn III.",
        "B4.03, B4.04", ["Hepatoblastoma", "Giai-doan", "Nhi-khoa"],
    ),
    basic(
        "SURG31-B4-03", "B4", "Mốc nhân chia & Vỡ u trong Hepatoblastoma", 2,
        f"{B('[Xếp giai đoạn Hepatoblastoma 1995]')} Mốc {G('số lượng nhân chia')} phân biệt Giai đoạn I vs II và sự kiện nào khiến u Giai đoạn I, II chuyển thành {R('Giai đoạn III')}?",
        f"1) <b>Mốc nhân chia vi thể:</b> Giai đoạn I có {G('< 2 nhân chia / vi trường')} (độ mô học thấp); Giai đoạn II có {Y('> 2 nhân chia / vi trường')} (độ mô học cao).<br>"
        f"2) <b>Sự kiện nâng giai đoạn III:</b> Bệnh nhân có khối u ban đầu thuộc giai đoạn I hoặc II nhưng {R('đã vỡ u trước mổ')} (hoặc sót u vi thể diện cắt) lập tức được xếp vào {R('Giai đoạn III')}.",
        "Hiện tượng vỡ u làm tràn tế bào ung thư vào khoang phúc mạc khiến nguy cơ tái phát tại chỗ và di căn màng bụng tăng vọt, đòi hỏi nâng phác đồ điều trị lên Giai đoạn III.",
        "B4.03, B4.04", ["Hepatoblastoma", "Nguong-so"],
    ),

    # ============================================================
    # B5. ĐIỀU TRỊ NGOẠI KHOA & CAN THIỆP TẠI CHỖ (HCC)
    # ============================================================
    basic(
        "SURG31-B5-01", "B5", "Chỉ định & Kỹ thuật mổ cắt gan HCC", 1,
        f"{B('[Phẫu thuật cắt gan HCC]')} Tỷ lệ u cắt được, {G('5 tiêu chuẩn chỉ định')}, các đường mổ, {Y('nghiệm pháp Pringle')} và loại chỉ khâu diện cắt?",
        f"1) <b>Khả năng cắt bỏ:</b> Chỉ khoảng {R('5 – 10%')} u có khả năng cắt triệt căn; {R('90% không thể cắt bỏ được')}.<br>"
        f"2) <b>Điều kiện phẫu thuật:</b> Khối u đơn độc, kích thước càng nhỏ càng tốt, khu trú ở {G('thùy gan trái')} hoặc {G('1 hạ phân thùy gan phải')}, xa rốn gan, {G('Child-Pugh A tốt hơn B')}, {Y('tuổi dưới 75')}.<br>"
        f"3) <b>Kỹ thuật mổ:</b> Đường mổ {B('chữ J')} hoặc {B('dưới sườn phải')}; đặt garô cuống gan ({Y('Pringle ngắt quãng ~8 phút')}); cắt theo cuống Glisson hoặc phân thùy Tôn Thất Tùng.<br>"
        f"4) <b>Khâu diện cắt:</b> Khâu cầm máu diện cắt bằng {G('chỉ tiêu Vicryl số 0')}.",
        "Nghiệm pháp Pringle tạm thời kẹp cuống gan (ĐM gan và TM cửa) để giảm mất máu khi cắt nhu mô gan, phải ngắt quãng ~8 phút để tránh hoại tử tế bào gan do thiếu máu.",
        "B5.01, B5.02", ["Phau-thuat", "Cat-gan", "Pringle"],
    ),
    basic(
        "SURG31-B5-02", "B5", "Ghép gan & Tiêu chuẩn Milan", 1,
        f"{B('[Ghép gan trong HCC]')} Ghép gan là hy vọng tốt nhất cho trường hợp nào và theo tiêu chuẩn nào?",
        f"1) <b>Đối tượng chỉ định:</b> Là hy vọng tốt nhất cho trường hợp {G('khối u gan còn khu trú')} nhưng {R('kèm theo xơ gan nặng (Child-Pugh B, C)')} không thể chịu đựng được cuộc phẫu thuật cắt gan.<br>"
        f"2) <b>Nguyên tắc triển khai:</b> Đang từng bước phát triển áp dụng theo {B('tiêu chuẩn Milan')}.",
        "Ghép gan vừa giải quyết triệt để khối ung thư vừa loại bỏ hoàn toàn ổ bệnh xơ gan nền mạn tính.",
        "B5.03", ["Ghep-gan", "Milan"],
    ),
    basic(
        "SURG31-B5-03", "B5", "Tiêm cồn tuyệt đối qua da (PEI)", 1,
        f"{B('[Can thiệp tại chỗ PEI]')} Nguyên lý, chỉ định, {R('4 chống chỉ định')}, công thức tính thể tích cồn và phác đồ tiêm?",
        f"1) <b>Nguyên lý:</b> Dùng {G('Ethanol 99%')} làm đông vón protein và gây tắc vi mạch nuôi u, làm hoại tử tế bào ung thư dưới hướng dẫn siêu âm.<br>"
        f"2) <b>Điều kiện tiêm:</b> U {G('≤ 3 khối')}, đường kính u {G('< 3 cm (tối đa < 5 cm)')}, nằm sâu trong nhu mô {Y('xa bao gan và rốn gan')}.<br>"
        f"3) <b>Tình huống cấm tiêm:</b> {R('Cổ trướng nhiều')}, {R('rối loạn đông máu')}, {R('vàng da tắc mật')}, {R('huyết khối tĩnh mạch cửa')}.<br>"
        f"4) <b>Quy cách tính thể tích:</b> Tính theo thể tích khối cầu V = 4/3 × π × (r + 0,5)³; u < 3 cm tiêm {Y('8 ml')}; u 4–10 cm tiêm {Y('12–20 ml')} chia nhiều lần ({Y('2 lần/tuần, tiêm từ 2 đến 6 lần')}).",
        "Tiêm cồn sát bao gan dễ gây đau chói do rò cồn vào phúc mạc, tiêm gần rốn gan nguy cơ hoại tử đường mật và mạch máu chính.",
        "B5.04, B5.05", ["PEI", "Tiem-con", "Chong-chi-dinh"],
    ),
    basic(
        "SURG31-B5-04", "B5", "Đốt nhiệt sóng cao tần (RFA)", 1,
        f"{B('[Can thiệp tại chỗ RFA]')} Nguyên lý nhiệt độ, chỉ định và kết quả hoại tử u &amp; sống 2 năm?",
        f"1) <b>Nguyên lý:</b> Dùng dòng điện xoay chiều tần số cao tạo nhiệt độ {R('60 – 100°C')} làm đông hủy hoại tử khối u.<br>"
        f"2) <b>Kích thước u phù hợp:</b> U đơn độc {G('< 3 cm')} (hoặc {G('≤ 3 khối u ≤ 3 cm')}).<br>"
        f"3) <b>Kết quả:</b> Khối u < 3 cm đạt tỷ lệ {G('hoại tử hoàn toàn 50%')}; tỷ lệ sống thêm sau 2 năm đạt {G('61%')}.",
        "Nhiệt độ trên 60°C gây biến tính protein và phá hủy màng tế bào tức thì, tạo vùng hoại tử đông vô trùng thay thế khối u.",
        "B5.06", ["RFA", "Dot-nhiet", "Nhiet-do"],
    ),
    basic(
        "SURG31-B5-05", "B5", "Hóa dầu tắc mạch (TACE) & Xạ trị", 1,
        f"{B('[TACE & Xạ trị trong HCC]')} Nguyên lý {G('TACE (hóa chất, Lipiodol, Spongel)')}, chỉ định, tác dụng và vai trò của {Y('xạ trị ngoài')}?",
        f"1) <b>Nguyên lý TACE:</b> Bơm hỗn hợp hóa chất ({B('Doxorubicin, Cisplatin, Mitomycin C')}) pha với dầu cản quang {G('Lipiodol')} vào động mạch nuôi u, sau đó nút mạch bằng {Y('Spongel / Gelatin')} để cắt nguồn máu nuôi và lưu giữ hóa chất tại chỗ.<br>"
        f"2) <b>Đối tượng áp dụng:</b> Khối u lớn {R('không thể cắt bỏ')}, nhiều ổ nhưng {G('chưa có huyết khối tĩnh mạch cửa')}, {G('Child-Pugh A hoặc B')}.<br>"
        f"3) <b>Tác dụng:</b> Kéo dài thời gian sống, làm co nhỏ u tạo cơ hội phẫu thuật hoặc {R('cầm máu khi khối u vỡ')}.<br>"
        f"4) <b>Xạ trị ngoài:</b> Ít tác dụng trên gan xơ; chỉ định hạn chế liều {Y('60 – 70 Gy')} nhằm giảm đau, giảm chèn ép trong u có huyết khối nhánh tĩnh mạch cửa.",
        "TACE chống chỉ định tuyệt đối khi có huyết khối thân chính tĩnh mạch cửa vì gan sẽ bị nhồi máu hoại tử cấp do mất cả hai nguồn cấp máu.",
        "B5.07, B5.08", ["TACE", "Tac-mach", "Xa-tri"],
    ),
    cloze(
        "SURG31-B5-06", "B5", "Thông số kỹ thuật PEI & RFA",
        f"Đốt sóng cao tần RFA tạo nhiệt độ {clz(1, R('60 – 100°C'))} làm đông hủy u; trong khi tiêm cồn PEI u < 3 cm dùng liều {clz(2, Y('8 ml'))} và u 4–10 cm dùng {clz(3, Y('12 – 20 ml'))} chia {clz(4, Y('2 lần/tuần'))} từ 2 đến 6 lần.",
        "B5.05, B5.06", ["PEI", "RFA", "Nguong-so"],
    ),

    # ============================================================
    # B6. ĐIỀU TRỊ UNG THƯ NGUYÊN BÀO GAN (TRẺ EM)
    # ============================================================
    basic(
        "SURG31-B6-01", "B6", "Phác đồ PLADO & Cisplatin/5-FU/Vincristine", 1,
        f"{B('[Hóa trị Hepatoblastoma]')} Chi tiết thuốc, liều và chu kỳ của {G('phác đồ PLADO (SIOPEL-1)')} và {Y('phác đồ Cisplatin + 5-FU + Vincristine')}?",
        f"1) <b>Công thức PLADO (SIOPEL-1):</b><br>"
        f"   • {G('Cisplatin')}: {Y('80 mg/m² da')}, truyền tĩnh mạch {B('Ngày 1')}.<br>"
        f"   • {G('Doxorubicin')}: {Y('30 mg/m² da')}, truyền tĩnh mạch {B('Ngày 2 và Ngày 3')}.<br>"
        f"   • Chu kỳ: Mỗi đợt cách nhau {Y('21 ngày')}, dùng {Y('4 – 6 đợt')}.<br>"
        f"2) <b>Công thức Cisplatin + 5-FU + Vincristine:</b><br>"
        f"   • Cisplatin: {Y('90 mg/m²')} (hoặc 30 mg/kg) truyền TM 6h {B('Ngày 1')}.<br>"
        f"   • Vincristine: {Y('1,5 mg/m²')} truyền TM 6h {B('Ngày 2')} + 5-FU: {Y('600 mg/m²')} truyền TM {B('Ngày 2')}.<br>"
        f"   • Chu kỳ: Mỗi đợt cách nhau {Y('21 ngày')}, dùng {Y('4 – 6 đợt')}.",
        "Sự phối hợp giữa dẫn chất platin (Cisplatin) và anthracycline (Doxorubicin) tạo hiệu ứng hiệp đồng tiêu diệt nguyên bào gan chưa biệt hóa cực kỳ mạnh mẽ.",
        "B6.01, B6.02", ["PLADO", "Cisplatin", "Doxorubicin"],
    ),
    basic(
        "SURG31-B6-02", "B6", "Chiến lược đa mô thức Hepatoblastoma", 1,
        f"{B('[Chiến lược điều trị Hepatoblastoma]')} Trình bày sự phối hợp 3 bước giữa {G('Hóa trị tân bổ trợ')}, {B('Phẫu thuật')} và {Y('Hóa trị bổ trợ')}?",
        f"1) <b>Bước 1 — Hóa trị tân bổ trợ (tiền phẫu):</b> Làm khối u {G('co nhỏ đáng kể')} (down-staging), biến tổn thương u khổng lồ không cắt được thành cắt được an toàn.<br>"
        f"2) <b>Bước 2 — Phẫu thuật:</b> Thực hiện {B('cắt bỏ triệt để khối u')} khi u đã khu trú và nhu mô gan lành phì đại bù trừ.<br>"
        f"3) <b>Bước 3 — Hóa trị bổ trợ (sau mổ):</b> Dùng tiếp {Y('đủ 4 – 6 đợt')} để tiêu diệt các vi ổ ung thư lưu hành, ngăn ngừa tái phát.",
        "Nhờ tính chất cực kỳ nhạy hóa chất của Hepatoblastoma, chiến lược tân bổ trợ trước mổ là tiêu chuẩn vàng bắt buộc cho hầu hết các khối u gan trẻ em lớn.",
        "B6.03", ["Chien-luoc", "Da-mo-thuc", "Tan-bo-tro"],
    ),
    cloze(
        "SURG31-B6-03", "B6", "Liều phác đồ PLADO",
        f"Phác đồ PLADO điều trị Hepatoblastoma gồm {clz(1, G('Cisplatin 80 mg/m²'))} truyền TM Ngày 1 và {clz(2, G('Doxorubicin 30 mg/m²'))} truyền TM Ngày 2 và 3, chu kỳ {clz(3, Y('21 ngày'))} dùng từ {clz(4, Y('4 – 6 đợt'))}.",
        "B6.01", ["PLADO", "Nguong-so"],
    ),

    # ============================================================
    # B7. PHÁC ĐỒ ĐIỀU TRỊ TỔNG QUÁT THEO BAREM
    # ============================================================
    basic(
        "SURG31-B7-01", "B7", "Phác đồ HCC giai đoạn T1-2 và T3", 1,
        f"{B('[Phác đồ tổng quát HCC]')} Hướng xử trí cho bệnh nhân {G('T1-2 N0 M0 / Child A-B')} và {Y('T3 N0 M0 / Child A-B')} theo tuổi và bệnh kèm?",
        f"1) <b>T1-2 N0 M0 / Child-Pugh A, B:</b><br>"
        f"   • Không bệnh nội khoa nặng, tuổi < 75 → {G('Phẫu thuật triệt căn')}.<br>"
        f"   • Từ chối mổ HOẶC có bệnh nội khoa nặng, tuổi > 75 → {Y('Tiêm Ethanol qua da (PEI) / Đốt nhiệt cao tần (RFA)')}.<br>"
        f"2) <b>T3 N0 M0 / Child-Pugh A, B:</b> → {Y('Tiêm Ethanol qua da / Hóa dầu tắc mạch (TACE)')}.",
        "Ở bệnh nhân cao tuổi (> 75) hoặc có bệnh tim phổi nặng, can thiệp tại chỗ RFA/PEI mang lại kết quả sống tương đương cắt gan mà tránh được biến chứng gây mê hồi sức lớn.",
        "B7.01, B7.02", ["Phac-do", "T1-2", "T3"],
    ),
    basic(
        "SURG31-B7-02", "B7", "Phác đồ HCC giai đoạn muộn & Child-Pugh C", 1,
        f"{B('[Phác đồ tổng quát HCC]')} Chỉ định điều trị cho bệnh nhân {R('T4 N0 M0, di căn hạch N1, di căn xa M1 hoặc Child-Pugh C')}?",
        f"1) <b>Các trường hợp bệnh tiến xa:</b> {R('T4 N0 M0')} (u xâm lấn tạng lân cận/phúc mạc), {R('T bất kỳ N1 M0')} (di căn hạch), hoặc {R('M1')} (di căn xa).<br>"
        f"2) <b>Trường hợp xơ gan mất bù:</b> {R('Xơ gan Child-Pugh C')} (≥ 10 điểm).<br>"
        f"3) <b>Định hướng chăm sóc:</b> Chuyển sang {R('Điều trị triệu chứng / Chăm sóc giảm nhẹ')}.",
        "Giai đoạn Child-Pugh C dự trữ chức năng gan còn lại quá yếu, can thiệp phẫu thuật hay TACE đều sẽ đẩy bệnh nhân vào hôn mê gan tử vong ngay lập tức.",
        "B7.03", ["Phac-do", "Giam-nhe", "Child-C"],
    ),
    basic(
        "SURG31-B7-03", "B7", "Phác đồ HCC nhiều ổ theo Huyết khối TM cửa", 1,
        f"{B('[Phác đồ tổng quát HCC]')} Chiến lược điều trị HCC nhiều ổ (Child-Pugh A, B) khi {G('chưa có')} vs {R('đã có huyết khối tĩnh mạch cửa')}?",
        f"1) <b>Nhiều ổ, KHÔNG huyết khối tĩnh mạch cửa:</b><br>"
        f"   • U cùng một phân thùy: {G('Phẫu thuật cắt phân thùy')}.<br>"
        f"   • U khác phân thùy: {Y('Hóa tắc mạch khối u (TACE)')}, tiêm cồn với {G('u < 3 cm')}.<br>"
        f"2) <b>Nhiều ổ, CÓ huyết khối tĩnh mạch cửa:</b> → Chống chỉ định TACE, chuyển sang {R('Xạ trị ngoài / Điều trị đích (Sorafenib)')}.",
        "Huyết khối tĩnh mạch cửa là ngã rẽ sống còn: chưa có huyết khối thì TACE là số 1; đã có huyết khối thì TACE gây nhồi máu gan, phải dùng Sorafenib hoặc xạ trị ngoài.",
        "B7.04, B7.05", ["Phac-do", "Nhieu-o", "Huyet-khoi-TM-cua"],
    ),
    basic(
        "SURG31-B7-04", "B7", "Phác đồ Hepatoblastoma theo Giai đoạn I–IV", 1,
        f"{B('[Phác đồ Ung thư nguyên bào gan]')} Chiến lược điều trị chi tiết cho từng giai đoạn {G('I')}, {Y('II (ngoại vi vs trung tâm)')}, {Y('III')} và {R('IV')}?",
        f"1) <b>Giai đoạn I &amp; Giai đoạn II (u ngoại vi):</b> {G('Phẫu thuật triệt căn')} → {Y('Hóa trị bổ trợ 6 đợt')}.<br>"
        f"2) <b>Giai đoạn II (u trung tâm khó cắt):</b> {Y('Hóa trị tiền phẫu 2 – 4 đợt')} → {G('Phẫu thuật cắt bỏ u')} → {Y('Hóa trị bổ trợ cho đủ 6 đợt')}.<br>"
        f"3) <b>Giai đoạn III:</b> {Y('Hóa trị tiền phẫu 6 đợt')} → {G('Phẫu thuật lấy tàn tích khối u')}.<br>"
        f"4) <b>Giai đoạn IV:</b> {R('Hóa trị đơn thuần 3 đợt')} → Sinh thiết đánh giá đáp ứng hóa trị → Nếu có hoại tử u: tiếp tục hóa trị 3 đợt; nếu không đáp ứng: {R('chuyển điều trị triệu chứng')}.",
        "Mọi trường hợp Hepatoblastoma đều cần tích lũy tổng cộng 6 đợt hóa trị chuẩn (ngoại trừ GĐ IV không đáp ứng chuyển điều trị triệu chứng).",
        "B7.06", ["Phac-do", "Hepatoblastoma", "Giai-doan"],
    ),

    # ============================================================
    # BẪY LÂM SÀNG & CỜ ĐỎ (TRAP / RED FLAG)
    # ============================================================
    trap(
        "SURG31-TRAP-01", "B1", "Bẫy bỏ sót HCC giai đoạn sớm",
        "Bệnh nhân có xơ gan HBV mạn tính đến khám với lý do đau tức vùng gan, vàng da rõ và cổ trướng — liệu có thể đặt mục tiêu phẫu thuật triệt căn?",
        f"1) <b>Bẫy lâm sàng:</b> Tuyệt đối không — khi xuất hiện các triệu chứng rầm rộ (vàng da, cổ trướng, suy kiệt) thì u thường đã ở giai đoạn muộn và {R('hết khả năng điều trị khỏi')}.<br>"
        f"2) <b>Hành động đúng:</b> Muốn phát hiện sớm phải chủ động {G('siêu âm gan định kỳ')} ở nhóm có nguy cơ cao để phát hiện khối u kích thước nhỏ {Y('≥ 1 cm')}.",
        "Chẩn đoán sớm HCC là cuộc rượt đuổi chủ động bằng siêu âm định kỳ trên người lành mang virus, không thể chờ bệnh nhân có triệu chứng mới đi khám.",
        "B1.01, B1.02", ["Bay-lam-sang", "Tam-soat-som"],
    ),
    trap(
        "SURG31-TRAP-02", "B0", "Bẫy nhầm lẫn đáp ứng hóa trị HCC vs Hepatoblastoma",
        "Một bác sĩ đề xuất chỉ định đa hóa trị toàn thân cho bệnh nhân ung thư biểu mô tế bào gan (HCC) giai đoạn tiến triển tương tự như phác đồ ung thư nguyên bào gan trẻ em — sai lầm ở đâu?",
        f"1) <b>Bẫy nhầm lẫn:</b> {R('HCC gần như không đáp ứng với hóa trị toàn thân')}, trong khi Hepatoblastoma {G('rất nhạy cảm với hóa chất')} (nhờ tính chất nguyên bào bào thai chưa biệt hóa).<br>"
        f"2) <b>Phương án chuẩn:</b> Với HCC tiến triển không cắt được, can thiệp chuẩn là {Y('TACE')}, {Y('điều trị đích (Sorafenib)')} hoặc {Y('RFA/PEI')}, không dùng hóa trị toàn thân kinh điển.",
        "Đây là một trong những câu hỏi bẫy kinh điển phân biệt bản chất sinh học hoàn toàn đối lập giữa ung thư biểu mô gan người lớn và ung thư nguyên bào gan trẻ nhỏ.",
        "B0.06, B5.07", ["Bay-lam-sang", "Hoa-tri"],
    ),
    trap(
        "SURG31-TRAP-03", "B1", "Bẫy loại trừ ung thư khi AFP bình thường",
        "Bệnh nhân nam 55 tuổi có HBsAg(+), siêu âm thấy khối giảm âm ở hạ phân thùy VI đường kính 2,5 cm, nhưng xét nghiệm AFP chỉ 12 ng/ml (bình thường). Có được kết luận loại trừ ung thư gan?",
        f"1) <b>Bẫy lâm sàng:</b> {R('Tuyệt đối không được loại trừ ung thư')} — barem ghi nhận khoảng 70% bệnh nhân HCC có AFP > 3.500 ng/ml, vẫn còn nhiều trường hợp AFP âm tính.<br>"
        f"2) <b>Hành động đúng:</b> Bệnh nhân có khối u gan kèm HBsAg(+) dù AFP âm tính vẫn phải chỉ định {G('chụp CT Scanner gan đa dãy (tìm dấu hiệu wash-out)')} và {G('sinh thiết kim Menghini dưới hướng dẫn siêu âm')} để xác định chẩn đoán.",
        "Công thức chẩn đoán thứ 2: Hình ảnh khối u + Sinh thiết HCC = Ung thư gan. Không phụ thuộc hoàn toàn vào AFP đơn độc.",
        "B1.05, B1.06, B1.07", ["Bay-lam-sang", "AFP-am-tinh"],
    ),
    trap(
        "SURG31-TRAP-04", "B5", "Bẫy chống chỉ định tiêm cồn Ethanol (PEI)",
        "Tại sao không được chỉ định tiêm cồn tuyệt đối (PEI) cho khối u gan nằm sát bề mặt bao gan hoặc ở bệnh nhân có cổ trướng nhiều và rối loạn đông máu?",
        f"1) <b>Khối u sát bao gan / rốn gan:</b> Không đáp ứng tiêu chuẩn an toàn của PEI (chỉ định đòi hỏi u nằm sâu trong nhu mô gan xa bao gan và rốn gan).<br>"
        f"2) <b>4 chống chỉ định bắt buộc thuộc:</b> {R('Cổ trướng nhiều')}, {R('rối loạn đông máu')}, {R('vàng da tắc mật')} và {R('huyết khối tĩnh mạch cửa')}.",
        "Chỉ định PEI lý tưởng: u ≤ 3 khối, đường kính < 3 cm, nằm sâu trong nhu mô gan xa bao gan và rốn gan.",
        "B5.04", ["Bay-lam-sang", "PEI", "Chong-chi-dinh"],
    ),
    trap(
        "SURG31-TRAP-05", "B5", "Cờ đỏ — Bẫy chỉ định TACE khi có Huyết khối Tĩnh mạch cửa",
        "Bệnh nhân HCC nhiều ổ, Child-Pugh A, CT Scanner phát hiện có huyết khối xâm lấn thân chính tĩnh mạch cửa. Tại sao tuyệt đối chống chỉ định làm TACE?",
        f"1) <b>Cờ đỏ huyết động:</b> Khi đã có {R('huyết khối tĩnh mạch cửa')}, dòng máu cửa suy giảm nghiêm trọng khiến nhu mô gan sống dựa vào động mạch gan.<br>"
        f"2) <b>Tai biến nếu làm TACE:</b> Bơm hóa dầu nút tắc động mạch gan sẽ làm {R('hoại tử toàn bộ nhu mô gan cấp tính')}, dẫn tới suy gan bùng phát và tử vong nhanh chóng.<br>"
        f"3) <b>Hướng xử trí đúng:</b> Chuyển sang {G('Xạ trị ngoài liều 60–70 Gy')} hoặc {G('Điều trị đích (Sorafenib)')}.",
        "Huyết khối tĩnh mạch cửa là cờ đỏ tối khẩn cấp loại trừ hoàn toàn chỉ định làm hóa dầu nút mạch TACE.",
        "B5.07, B7.05", ["Co-do", "TACE", "Huyet-khoi-TM-cua"], red_flag=True,
    ),
    trap(
        "SURG31-TRAP-06", "B2", "Cờ đỏ — Chỉ định phẫu thuật cắt gan ở bệnh nhân Child-Pugh C",
        "Bệnh nhân HCC đơn độc kích thước 3 cm ở hạ phân thùy VI, nhưng xét nghiệm có Bilirubin 65 µmol/L, Albumin 24 g/L, cổ trướng nhiều (++) — đạt 11 điểm Child-Pugh C. Có nên chỉ định mổ cắt u?",
        f"1) <b>Cờ đỏ chống chỉ định mổ:</b> {R('Tuyệt đối chống chỉ định phẫu thuật cắt gan')} — bệnh nhân xơ gan Child-Pugh C (≥ 10 điểm) không còn dự trữ chức năng gan.<br>"
        f"2) <b>Nguy cơ chu phẫu:</b> Bất kỳ can thiệp phẫu thuật cắt gan nào cũng gây {R('suy gan cấp mất bù, hôn mê gan và tử vong')} trên bàn mổ hoặc hậu phẫu sớm.<br>"
        f"3) <b>Phương án chuẩn:</b> Chỉ {Y('điều trị triệu chứng / chăm sóc giảm nhẹ')} hoặc xem xét {G('ghép gan')} nếu khối u thỏa mãn tiêu chuẩn Milan.",
        "Tiêu chuẩn phẫu thuật cắt gan trong barem yêu cầu rõ: Child-Pugh A tốt hơn B; Child-Pugh C hoàn toàn chuyển sang điều trị giảm nhẹ.",
        "B2.01, B5.01, B7.03", ["Co-do", "Child-C", "Chong-chi-dinh"], red_flag=True,
    ),

    # ============================================================
    # THUẬT TOÁN QUYẾT ĐỊNH (ALGORITHMS)
    # ============================================================
    algo(
        "SURG31-ALGO-01", "B1", "Chẩn đoán khối u gan",
        "Thuật toán tiếp cận chẩn đoán xác định khối u gan trên nền bệnh gan mạn",
        f"1) <b>Bước 1 — Phát hiện u:</b> Siêu âm gan phát hiện khối u {Y('≥ 1 cm')} (tìm dấu hiệu quầng giảm âm quanh u, Doppler màu loại trừ u máu).<br>"
        f"2) <b>Bước 2 — Định danh huyết thanh:</b> Định lượng {G('AFP')} và kháng nguyên bề mặt {G('HBsAg')}. Nếu khối u gan kèm {G('AFP > 200 ng/ml')} → Chẩn đoán xác định {G('Ung thư biểu mô tế bào gan (HCC)')}.<br>"
        f"3) <b>Bước 3 — Khảo sát mạch máu:</b> Chụp {B('CT Scanner gan')} tìm dấu hiệu ngấm nhanh thì ĐM và thải nhanh thì TM ({Y('wash-out')}), định khu hạ phân thùy, kiểm tra huyết khối TM cửa.<br>"
        f"4) <b>Bước 4 — Sinh thiết khi AFP âm tính:</b> Nếu u nghi ngờ nhưng AFP ≤ 200 ng/ml → Chỉ định {G('sinh thiết kim Menghini')} dưới hướng dẫn siêu âm (hoặc mổ thăm dò sinh thiết tức thì).",
        "Hai công thức thực tế trong barem: U gan + AFP > 200 ng/ml = HCC; U gan + Sinh thiết HCC = Ung thư gan.",
        "B1.03, B1.04, B1.05, B1.06, B1.07", ["Thuat-toan", "Chan-doan-u-gan"],
    ),
    algo(
        "SURG31-ALGO-02", "B7", "Lựa chọn phương pháp điều trị HCC",
        "Thuật toán phân tầng xử trí HCC theo giai đoạn TNM, Child-Pugh và tuổi bệnh nhân",
        f"1) <b>Nhánh 1 — T1-2 N0 M0 / Child-Pugh A, B:</b><br>"
        f"   • Không bệnh nội khoa nặng, tuổi < 75 → {G('Phẫu thuật cắt gan triệt căn')}.<br>"
        f"   • Có bệnh nội khoa nặng, tuổi > 75 hoặc từ chối mổ → {Y('Tiêm cồn PEI hoặc Đốt sóng cao tần RFA')}.<br>"
        f"2) <b>Nhánh 2 — T3 N0 M0 / Child-Pugh A, B:</b> → {Y('Tiêm cồn PEI hoặc Hóa dầu nút mạch TACE')}.<br>"
        f"3) <b>Nhánh 3 — U nhiều ổ (Child-Pugh A, B):</b><br>"
        f"   • Chưa có huyết khối TM cửa: Cùng phân thùy → {G('Cắt phân thùy')}; khác phân thùy → {Y('TACE + PEI u < 3cm')}.<br>"
        f"   • Đã có huyết khối TM cửa → {R('Xạ trị ngoài liều 60–70 Gy hoặc Điều trị đích Sorafenib')}.<br>"
        f"4) <b>Nhánh 4 — Giai đoạn muộn (T4, N1, M1) hoặc Child-Pugh C:</b> → {R('Điều trị triệu chứng / Chăm sóc giảm nhẹ')}.",
        "Thuật toán bám sát 100% sơ đồ phác đồ tổng quát trong bài học, thể hiện sự phối hợp chặt chẽ giữa ngoại khoa, can thiệp mạch và chăm sóc giảm nhẹ.",
        "B7.01, B7.02, B7.03, B7.04, B7.05", ["Thuat-toan", "Dieu-tri-HCC"],
    ),
    algo(
        "SURG31-ALGO-03", "B7", "Bậc thang điều trị Ung thư nguyên bào gan trẻ em",
        "Thuật toán xử trí đa mô thức Ung thư nguyên bào gan theo 4 giai đoạn phân loại Nhi khoa 1995",
        f"1) <b>Giai đoạn I &amp; Giai đoạn II ngoại vi:</b> {G('Phẫu thuật cắt u triệt căn')} ngay từ đầu → {Y('Hóa trị bổ trợ 6 đợt')} (phác đồ PLADO hoặc Cisplatin + 5-FU + Vincristine).<br>"
        f"2) <b>Giai đoạn II trung tâm khó cắt:</b> {Y('Hóa trị tiền phẫu 2 – 4 đợt')} làm u co nhỏ → {G('Phẫu thuật cắt bỏ u')} → {Y('Hóa trị bổ trợ đủ 6 đợt')}.<br>"
        f"3) <b>Giai đoạn III (sót vi thể hoặc vỡ u trước mổ):</b> {Y('Hóa trị tiền phẫu 6 đợt')} → {G('Phẫu thuật lấy tàn tích u')}.<br>"
        f"4) <b>Giai đoạn IV (không cắt được hoặc di căn xa):</b> {R('Hóa trị đơn thuần 3 đợt')} → Sinh thiết đánh giá hoại tử u: nếu đáp ứng tốt → Tiếp tục hóa trị 3 đợt; nếu không đáp ứng → {R('Chuyển điều trị triệu chứng')}.",
        "Chiến lược điều trị nguyên bào gan trẻ em luôn coi hóa trị là chìa khóa then chốt đưa khối u về mức độ an toàn để phẫu thuật viên cắt bỏ sạch sẽ.",
        "B6.01, B6.02, B6.03, B7.06", ["Thuat-toan", "Hepatoblastoma"],
    ),
]
