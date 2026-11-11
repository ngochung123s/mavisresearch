# -*- coding: utf-8 -*-
"""
Dữ liệu thẻ Anki chuẩn hóa cho bài SURG-58: Ung Thư Tuyến Tiền Liệt
Rebuild 100% từ barem: SURG-58_Ung_thu_tuyen_tien_liet_BAREM.md
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
    b_tag = f"Ngoai::SURG-58::{section}"
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

def redflag(cid, section, topic, front, core, ai, barem, tags, asks=None):
    return trap(cid, section, topic, front, core, ai, barem, tags, red_flag=True, asks=asks)

def cloze(cid, section, topic, text, barem, tags):
    b_tag = f"Ngoai::SURG-58::{section}"
    return {
        "id": cid,
        "type": "cloze",
        "section": section,
        "topic": topic,
        "tier": 1,
        "text": text,
        "extra": f"[{barem}]",
        "tags": [b_tag, "Tier-1"] + [f"Ngoai::{t}" for t in tags],
    }


cards_data = [
    # =========================================================================
    # B0: ĐẠI CƯƠNG & DỊCH TỄ HỌC
    # =========================================================================
    basic(
        "SURG58-B0-01", "B0", "Thứ hạng dịch tễ, tầm soát & Tiên lượng ung thư TTL", 1,
        f"{B('[Đại cương]')} Ung thư tuyến tiền liệt đứng thứ mấy ở nam giới, được phát hiện sớm nhờ công cụ nào, tỷ lệ khỏi sớm vs sống 5 năm muộn là bao nhiêu và đặc điểm diễn biến chung?",
        f"1) <b>Thứ hạng ở nam giới:</b> Phổ biến {Y('đứng hàng thứ 2 sau ung thư phổi')}.<br>"
        f"2) <b>Công cụ phát hiện sớm:</b> Nhờ ý thức khám sớm và chương trình tầm soát bằng {G('xét nghiệm PSA')} và {G('thăm trực tràng (DRE)')}.<br>"
        f"3) <b>Khác biệt sống còn:</b> Phát hiện sớm (u còn khu trú trong tuyến, chưa phá vỡ vỏ bao) đạt tỷ lệ điều trị khỏi {G('90%')}; phát hiện muộn tỷ lệ sống sau 5 năm chỉ còn {R('dưới 30%')}.<br>"
        f"4) <b>Tính chất âm thầm:</b> Phần lớn tồn tại dưới dạng {B('tiềm tàng')}, diễn biến lâm sàng rất đa dạng gây khó khăn chẩn đoán và điều trị.",
        f"Khoảng cách sinh tử giữa {G('90% chữa khỏi')} khi u còn khu trú trong bao tuyến và {R('< 30% sống 5 năm')} khi đã xâm lấn di căn cho thấy giá trị tuyệt đối của bộ đôi tầm soát {G('PSA + DRE')}.",
        "B0.01, B0.02", ["Dai-cuong", "Dich-te"],
    ),

    # =========================================================================
    # B1: YẾU TỐ NGUY CƠ
    # =========================================================================
    basic(
        "SURG58-B1-01", "B1", "Tuổi tác & Thống kê tỷ lệ mắc vs tử thiết", 1,
        f"{B('[Nguy cơ hàng đầu — Tuổi tác]')} Yếu tố nguy cơ quan trọng nhất của ung thư tuyến tiền liệt là gì và các con số tỷ lệ mắc trên lâm sàng vs qua tử thiết (autopsies) theo từng khung tuổi?",
        f"1) <b>Yếu tố quan trọng nhất:</b> {R('Tuổi tác')} — nam giới {Y('sau 50 tuổi')} có nguy cơ cao.<br>"
        f"2) <b>Thống kê mắc lâm sàng:</b> Nhóm {Y('40 – 59 tuổi')} là {B('2,2%')}; nhóm {Y('60 – 70 tuổi')} tăng lên {B('13,7%')}.<br>"
        f"3) <b>Thống kê qua tử thiết (autopsies):</b> Cao hơn rất nhiều — nhóm {Y('50 – 60 tuổi')} là {R('20%')}; nhóm {Y('70 – 80 tuổi')} lên tới {R('50%')}.",
        f"Sự chênh lệch lớn giữa tỷ lệ phát hiện lâm sàng và tỷ lệ mổ tử thiết ({R('50%')} ở tuổi 70–80) chứng minh đa số ung thư TTL ở người cao tuổi tiến triển chậm ở dạng tiềm tàng, làm nền tảng cho chiến lược theo dõi tích cực tránh điều trị quá mức.",
        "B1.01", ["Nguyen-nhan", "Dich-te"],
    ),
    basic(
        "SURG58-B1-02", "B1", "Chủng tộc, Gia đình, Chế độ ăn & Nội tiết tố", 1,
        f"{B('[Yếu tố nguy cơ khác]')} Phân bố ung thư TTL theo chủng tộc, tiền sử gia đình (mức tăng nguy cơ), chế độ ăn và vai trò của nội tiết tố?",
        f"1) <b>Chủng tộc:</b> Đàn ông {R('da đen Châu Phi và người gốc Phi ở Châu Mỹ')} mắc cao nhất thế giới; đàn ông {G('Châu Á')} có tỷ lệ thấp hơn.<br>"
        f"2) <b>Gia đình / Di truyền:</b> Có {B('bố hoặc anh em trai')} mắc ung thư TTL → nguy cơ cao hơn gấp {R('2 – 3 lần')}.<br>"
        f"3) <b>Chế độ ăn:</b> Ăn quá nhiều {R('chất béo động vật, mỡ bão hòa')} làm tăng nguy cơ.<br>"
        f"4) <b>Nội tiết tố:</b> Nồng độ {B('Testosterone tự do cao quá mức tự nhiên kéo dài')}.",
        f"Tiền sử gia đình trực hệ (bố/anh em trai) làm tăng nguy cơ gấp 2–3 lần là cơ sở hạ mốc tuổi bắt đầu tầm soát từ {Y('50 tuổi')} xuống {G('40 – 45 tuổi')}. Chế độ ăn nhiều mỡ bão hòa kích thích stress oxy hóa và chuyển hóa nội tiết tại mô tuyến.",
        "B1.02, B1.03", ["Nguyen-nhan", "Di-truyen"],
    ),
    cloze(
        "SURG58-B1-03", "B1", "Cloze: Tỷ lệ tử thiết & Tiên lượng sống còn",
        f"{B('[Thống kê TTL]')} Phát hiện sớm còn khu trú đạt tỷ lệ điều trị khỏi {clz(1, G('90%'))}, ngược lại phát hiện muộn tỷ lệ sống 5 năm chỉ còn {clz(2, R('dưới 30%'))}. Qua tử thiết, tỷ lệ ổ ung thư tiềm tàng ở tuổi 50–60 là {clz(3, Y('20%'))} và tuổi 70–80 lên tới {clz(4, R('50%'))}.",
        "B0.02, B1.01", ["Dich-te", "Cloze"],
    ),

    # =========================================================================
    # B2: GIẢI PHẪU BỆNH & THANG ĐIỂM GLEASON
    # =========================================================================
    basic(
        "SURG58-B2-01", "B2", "Mô học Adenocarcinoma & Tổn thương tiền ung thư PIN", 1,
        f"{B('[Giải phẫu bệnh — Mô học]')} Thể mô học nào chiếm tuyệt đại đa số ung thư TTL, đặc điểm tế bào/tuyến ác tính và phân biệt 2 độ tổn thương tiền ung thư PIN?",
        f"1) <b>Thể mô học chính:</b> Tuyệt đại đa số là {B('ung thư biểu mô tuyến (Adenocarcinoma)')}.<br>"
        f"2) <b>Hình thái tế bào & cấu trúc:</b> Tế bào u tăng sắc, nhân to, hạt nhân lồi rõ, bào tương ưa kiềm; cấu trúc tuyến biến đổi hỗn loạn và {R('mất lớp tế bào đáy')}.<br>"
        f"3) <b>Tổn thương tiền ung thư (PIN):</b> Gồm {B('PIN độ 1')} và {B('PIN độ 2')} — trong đó {R('PIN độ 2 (PIN độ cao - High-grade PIN)')} là tổn thương tiền ung thư thường đi kèm ung thư TTL.",
        f"Sự {R('mất lớp tế bào đáy')} quanh tuyến là dấu ấn mô bệnh học cốt lõi phân biệt Adenocarcinoma xâm nhập với tăng sản lành tính hoặc PIN còn màng đáy nguyên vẹn.",
        "B2.01", ["Giai-phau-benh"],
    ),
    basic(
        "SURG58-B2-02", "B2", "Thang điểm Gleason (1974)", 1,
        f"{B('[Thang điểm Gleason 1974]')} Cách tính tổng điểm Gleason và ý nghĩa phân tầng độ ác tính của các mức điểm 2–4, 5–6, 7 và 8–10?",
        f"1) <b>Cách tính điểm:</b> Dựa vào mức biệt hóa tuyến, bất thường nhân và đảo lộn cấu trúc mô học; lấy {B('2 mẫu đại diện phổ biến nhất')} (mỗi mẫu từ độ {Y('1 đến độ 5')}) cộng lại → Tổng {Y('2 đến 10 điểm')}.<br>"
        f"2) <b>2 – 4 điểm:</b> Biệt hóa {G('tốt')} (độ ác tính thấp).<br>"
        f"3) <b>5 – 6 điểm:</b> Biệt hóa {Y('trung bình')}.<br>"
        f"4) <b>7 điểm:</b> Biệt hóa {Y('trung bình – kém')} ({B('3+4')} hoặc {B('4+3')}).<br>"
        f"5) <b>8 – 10 điểm:</b> Biệt hóa {R('kém')} (độ ác tính rất cao, tiến triển nhanh và di căn sớm).",
        f"Điểm Gleason 7 phân tách hai tiên lượng khác nhau: {B('3+4')} (mẫu biệt hóa vừa chiếm ưu thế) tốt hơn đáng kể so với {R('4+3')} (mẫu kém biệt hóa chiếm ưu thế). Mốc {G('Gleason ≤ 7')} là ngưỡng cân nhắc phẫu thuật triệt căn.",
        "B2.02", ["Giai-phau-benh", "Gleason"],
    ),

    # =========================================================================
    # B3: PHÂN LOẠI GIAI ĐOẠN TNM & HƯỚNG DI CĂN XƯƠNG
    # =========================================================================
    basic(
        "SURG58-B3-01", "B3", "Phân loại TNM: Tx, T0, Tis & T1 (T1a, T1b, T1c)", 1,
        f"{B('[TNM — Tx, T0, Tis & T1]')} Định nghĩa Tx, T0, Tis và chi tiết 3 dưới nhóm T1 (T1a, T1b, T1c) trong ung thư tuyến tiền liệt?",
        f"1) <b>Nhóm Tx / T0 / Tis:</b> <b>Tx:</b> không xác định được u nguyên phát; <b>T0:</b> không có bằng chứng u; <b>Tis:</b> ung thư tại chỗ ({B('Carcinoma in situ / PIN độ cao')}).<br>"
        f"2) <b>T1 (khối u tiềm tàng — KHÔNG sờ thấy qua DRE và KHÔNG thấy trên siêu âm):</b><br>"
        f"   • <b>T1a:</b> Tình cờ phát hiện qua mảnh cắt nội soi phì đại lành tính, chiếm {G('≤ 5% mô cắt')}.<br>"
        f"   • <b>T1b:</b> Tình cờ phát hiện qua mảnh cắt nội soi, chiếm {Y('> 5% mô cắt')}.<br>"
        f"   • <b>T1c:</b> Phát hiện nhờ {B('sinh thiết kim')} do {R('nồng độ PSA máu tăng cao')}.",
        f"Khối u giai đoạn T1 hoàn toàn im lặng về mặt hình thái (không sờ thấy trên DRE, không thấy ổ giảm âm trên siêu âm). Hiện nay nhờ xét nghiệm sàng lọc PSA, {B('T1c')} là giai đoạn phát hiện mới thường gặp nhất trên lâm sàng.",
        "B3.01", ["TNM", "Phan-loai"],
    ),
    basic(
        "SURG58-B3-02", "B3", "Phân loại TNM: T2, T3 & T4", 1,
        f"{B('[TNM — T2, T3 & T4]')} Phân biệt đầy đủ T2 (T2a, T2b, T2c), T3 (T3a, T3b) và T4 theo vỏ bao tuyến tiền liệt, túi tinh và các tạng lân cận?",
        f"1) <b>T2 (sờ qua DRE hoặc thấy trên siêu âm, CHƯA vượt vỏ bao TTL):</b><br>"
        f"   • <b>T2a:</b> Khu trú ở {G('≤ 1/2 một thùy')}.<br>"
        f"   • <b>T2b:</b> Lan rộng {Y('> 1/2 một thùy')} nhưng chưa sang thùy bên kia.<br>"
        f"   • <b>T2c:</b> Xâm lấn {Y('cả hai thùy TTL')}.<br>"
        f"2) <b>T3 (đã xâm lấn phá vỡ vỏ bao TTL):</b><br>"
        f"   • <b>T3a:</b> Xâm lấn {R('ra ngoài vỏ bao 1 hoặc 2 bên')}.<br>"
        f"   • <b>T3b:</b> Xâm lấn vào {R('túi tinh')}.<br>"
        f"3) <b>T4:</b> Cố định hoặc xâm lấn các cơ quan lân cận: {R('cổ bàng quang, cơ thắt ngoài, trực tràng, cơ nâng hậu môn hoặc thành chậu')}.",
        f"Đường ranh giới vàng trong điều trị ngoại khoa chính là lớp {B('vỏ bao TTL')}: T1–T2 còn nằm trong vỏ bao nên có chỉ định mổ triệt căn chữa khỏi tới 90%; từ T3 đã vỡ vỏ bao/ăn túi tinh, mục tiêu chuyển sang kiểm soát toàn thân kết hợp.",
        "B3.02", ["TNM", "Phan-loai"],
    ),
    basic(
        "SURG58-B3-03", "B3", "Hạch vùng (N), Di căn xa (M) & Thứ tự di căn xương Batson", 1,
        f"{B('[TNM — N, M & Di căn xương]')} Liệt kê 4 nhóm hạch vùng (N), phân loại M1 (M1a, M1b, M1c), đường dẫn tĩnh mạch và thứ tự 6 vị trí xương hay bị di căn?",
        f"1) <b>Hạch bạch huyết vùng (N):</b> Gồm {B('hạch hố bịt, hạch chậu trong, hạch chậu ngoài, hạch thành chậu')} (<b>Nx</b> chưa đánh giá; <b>N0</b> chưa di căn; <b>N1</b> đã di căn hạch vùng).<br>"
        f"2) <b>Di căn xa (M0 không di căn; M1 có di căn):</b><br>"
        f"   • <b>M1a:</b> Hạch ngoài vùng chậu ({B('sau phúc mạc, trung thất, thượng đòn')}).<br>"
        f"   • <b>M1b:</b> {R('Di căn vào xương')} (đặc biệt thể {R('tạo xương - osteoblastic')}).<br>"
        f"   • <b>M1c:</b> Tạng khác ({R('phổi, gan, não, tuyến thượng thận')}...).<br>"
        f"3) <b>Đường di căn & Thứ tự 6 xương đích:</b> Theo {B('đám rối tĩnh mạch Batson không có van')} trực tiếp lên xương: 1) {R('Cột sống thắt lưng')} → 2) {R('Xương chậu')} → 3) {Y('Xương đùi')} → 4) {Y('Cột sống ngực')} → 5) {B('Xương sườn, xương ức')} → 6) {B('Xương sọ, xương cánh tay')}.",
        f"Do {B('đám rối tĩnh mạch Batson')} nằm dọc cột sống không có van một chiều và thông trực tiếp với đám rối tĩnh mạch quanh tuyến tiền liệt, chỉ cần áp lực ổ bụng tăng lên (rặn tiểu, ho) tế bào u dễ dàng đi ngược dòng thẳng vào {R('cột sống thắt lưng')} và {R('xương chậu')} tạo ổ đặc xương (osteoblastic).",
        "B3.03, B3.04", ["TNM", "Di-can"],
    ),
    cloze(
        "SURG58-B3-04", "B3", "Cloze: T1a/T1b 5%, T3b túi tinh & Tĩnh mạch Batson",
        f"{B('[Mốc TNM TTL]')} Ung thư tình cờ qua mảnh cắt nội soi xếp T1a khi chiếm {clz(1, G('≤ 5%'))} mô cắt và T1b khi > 5%. Phá vỡ vỏ bao xâm lấn túi tinh xếp giai đoạn {clz(2, R('T3b'))}. Di căn xương đi theo đường {clz(3, B('đám rối tĩnh mạch Batson không có van'))}.",
        "B3.01, B3.02, B3.04", ["TNM", "Cloze"],
    ),

    # =========================================================================
    # B4: TRIỆU CHỨNG LÂM SÀNG & THĂM TRỰC TRÀNG (DRE)
    # =========================================================================
    basic(
        "SURG58-B4-01", "B4", "Triệu chứng đường tiểu dưới: Tắc nghẽn vs Kích thích", 1,
        f"{B('[Lâm sàng — Đường tiểu dưới]')} Vì sao giai đoạn sớm thường im lặng và khi u phát triển gây ra những triệu chứng nào trong Hội chứng tắc nghẽn và Hội chứng kích thích?",
        f"1) <b>Giai đoạn sớm:</b> Khối u khu trú ở {B('vùng ngoại vi')} nên thường {Y('hoàn toàn không có triệu chứng')}.<br>"
        f"2) <b>Hội chứng tắc nghẽn đường tiểu dưới:</b> {R('Tiểu khó, phải rặn')}, {R('tia tiểu yếu đứt quãng')}; tiểu són, cảm giác {Y('đi tiểu không hết bãi')}; nặng nhất là {R('bí đái cấp tính')}.<br>"
        f"3) <b>Hội chứng kích thích:</b> Tiểu nhiều lần, đặc biệt thức dậy {R('tiểu đêm nhiều lần (nocturia)')}; tiểu buốt, {R('tiểu gấp không nhịn được')}.",
        f"Khác với tăng sản lành tính (BPH) mọc ở vùng chuyển tiếp sát niệu đạo gây tiểu khó rất sớm, ~70% ung thư TTL khởi phát ở {B('vùng ngoại vi')} cách xa niệu đạo nên không gây rối loạn tiểu tiện cho đến khi u lớn ăn lan vào cổ bàng quang hoặc niệu đạo.",
        "B4.01", ["Lam-sang"],
    ),
    basic(
        "SURG58-B4-02", "B4", "5 dấu hiệu nặng khi u xâm lấn hoặc di căn", 1,
        f"{B('[Lâm sàng — Dấu hiệu nặng]')} Kể đủ 5 nhóm dấu hiệu báo động bệnh nặng hoặc đã di căn xa trong ung thư tuyến tiền liệt?",
        f"1) {R('Đái ra máu')} hoặc {R('có máu trong tinh dịch (hemospermia)')}.<br>"
        f"2) {Y('Đau rát buốt khi xuất tinh')} hoặc mất khả năng xuất tinh.<br>"
        f"3) Đau nhức vô cớ vùng {B('xương chậu, thắt lưng, hông, đùi')}.<br>"
        f"4) {R('Đau xương dai dẳng tăng về đêm')} (gợi ý di căn xương).<br>"
        f"5) {R('Yếu liệt hai chi dưới hoặc bí tiểu')} do {R('chèn ép tủy sống cấp')}.",
        f"Máu trong tinh dịch hoặc đau khi xuất tinh phản ánh khối u đã xâm lấn vào ống phóng tinh hoặc túi tinh (T3b). Đau xương tăng về đêm và dấu hiệu yếu liệt 2 chân là cờ đỏ di căn cột sống qua đám rối Batson đe dọa liệt tủy không hồi phục.",
        "B4.02", ["Lam-sang", "Co-do"],
    ),
    basic(
        "SURG58-B4-03", "B4", "Thăm trực tràng bằng tay (DRE) sớm vs muộn", 1,
        f"{B('[Thăm trực tràng DRE]')} Mô tả kết quả sờ nắn tuyến tiền liệt qua thăm trực tràng bằng tay (DRE) ở giai đoạn sớm vs giai đoạn muộn?",
        f"1) <b>Vai trò cốt tử, bắt buộc:</b> Thực hiện cho mọi trường hợp nghi ngờ.<br>"
        f"2) <b>Giai đoạn sớm:</b> Phát hiện {R('một nhân cứng chắc, ranh giới rõ')} nằm trên nền mô tuyến mềm mại (thường ở {B('thùy sau hoặc vùng ngoại vi')}).<br>"
        f"3) <b>Giai đoạn muộn:</b> Toàn bộ tuyến {R('to, gồ ghề, mất rãnh giữa, rắn chắc như đá, mất di động')} và u lan ra ngoài vỏ bao vào vùng đáy bàng quang, túi tinh.",
        f"Thùy sau và vùng ngoại vi của tuyến tiền liệt áp sát trực tiếp thành trước trực tràng, khiến ngón tay thăm trực tràng trở thành vũ khí lâm sàng đơn giản nhưng hiệu quả nhất để cảm nhận nhân cứng bất thường sớm.",
        "B4.03", ["Lam-sang", "DRE"],
    ),

    # =========================================================================
    # B5: CẬN LÂM SÀNG (PSA, MEN MÁU, SINH THIẾT & CĐHA)
    # =========================================================================
    basic(
        "SURG58-B5-01", "B5", "Bản chất PSA, 3 dạng trong máu & Giới hạn PSA theo tuổi", 1,
        f"{B('[PSA — Sinh học & Ngưỡng tuổi]')} Bản chất và mức giải phóng PSA trong ung thư TTL, 3 dạng PSA máu (tỷ lệ cPSA vs fPSA) và giới hạn tPSA bình thường theo 4 nhóm tuổi?",
        f"1) <b>Bản chất & Tốc độ thoát vào máu:</b> PSA là {B('glycoprotein')} do tế bào biểu mô ống tuyến tiết giúp làm loãng tinh dịch; ung thư phá vỡ hàng rào giải phóng PSA vào máu {R('gấp 10 lần')} bình thường.<br>"
        f"2) <b>3 dạng PSA (tPSA = cPSA + fPSA):</b> <b>cPSA</b> (phức hợp gắn α1-antichymotrypsin ACT, α2-macroglobulin — chiếm {R('60 – 90%')} trong ung thư); <b>fPSA</b> (tự do không gắn protein — chiếm {G('10 – 40%')} ở người bình thường).<br>"
        f"3) <b>Giới hạn tPSA theo lứa tuổi:</b><br>"
        f"   • <b>40 – 49 tuổi:</b> {G('≤ 2,5 ng/ml')} · <b>50 – 59 tuổi:</b> {G('≤ 3,0 ng/ml')}<br>"
        f"   • <b>60 – 69 tuổi:</b> {Y('≤ 4,0 ng/ml')} · <b>70 – 79 tuổi:</b> {Y('≤ 5,0 ng/ml')}",
        f"Khi tế bào tuyến ung thư mất màng đáy và kiến trúc ống tuyến, PSA tràn ồ ạt vào mạch máu và gắn chặt với α1-ACT thành dạng phức hợp {R('cPSA')}, làm tỷ lệ dạng tự do {G('fPSA/tPSA')} tụt giảm rõ rệt so với phì đại lành tính.",
        "B5.01, B5.02", ["Can-lam-sang", "PSA"],
    ),
    basic(
        "SURG58-B5-02", "B5", "Ý nghĩa lâm sàng 5 mốc nồng độ PSA", 1,
        f"{B('[PSA — 5 mốc lâm sàng]')} Ý nghĩa tiên lượng ung thư và hướng xử trí ứng với 5 mốc nồng độ PSA: < 4, 4–10 (vùng xám), > 10, > 20 và > 100 ng/ml?",
        f"1) <b>PSA < 4 ng/ml:</b> Ngưỡng bình thường (nguy cơ ung thư {G('< 10%')}).<br>"
        f"2) <b>PSA 4 – 10 ng/ml (Vùng xám - Gray Zone):</b> Khoảng {Y('20 – 25%')} là ung thư → Cần áp dụng thêm chỉ số phụ trợ (f/tPSA, PSAD, PSAV).<br>"
        f"3) <b>PSA > 10 ng/ml:</b> Khoảng {R('50%')} là ung thư → {R('Bắt buộc chỉ định sinh thiết TTL bất kể kết quả DRE')}.<br>"
        f"4) <b>PSA > 20 ng/ml:</b> Khả năng cao u đã {R('phá vỡ bao tuyến hoặc di căn hạch/xương')}.<br>"
        f"5) <b>PSA > 100 ng/ml:</b> Hầu hết {R('đã có di căn xa vào xương')}.",
        f"Ở ngưỡng {R('PSA > 10 ng/ml')}, xác suất ác tính vọt lên 50% nên dù ngón tay DRE chưa sờ thấy nhân cứng cũng không được phép trì hoãn sinh thiết. Ngưỡng > 20 và > 100 ng/ml giúp bác sĩ chủ động tầm soát di căn xương bằng xạ hình xương ngay.",
        "B5.03", ["Can-lam-sang", "PSA"],
    ),
    basic(
        "SURG58-B5-03", "B5", "3 chỉ số phụ trợ PSA vùng xám: f/tPSA, PSAD, PSAV", 1,
        f"{B('[PSA — Chỉ số Vùng xám 4–10 ng/ml]')} Công thức, ngưỡng cắt chỉ định sinh thiết và các giá trị tham chiếu của 3 chỉ số: Tỷ lệ fPSA/tPSA, Tỷ trọng PSAD và Tốc độ PSAV?",
        f"1) <b>Chỉ số fPSA / tPSA:</b> Giảm thấp trong ung thư; {R('< 15%')} nguy cơ ung thư rất cao → {R('sinh thiết ngay')}; {G('> 25%')} thường là phì đại lành tính.<br>"
        f"2) <b>Tỷ trọng PSA (PSAD = tPSA / thể tích TTL siêu âm, ng/ml/cm³):</b> Bình thường {G('< 0,15')}; tăng sản lành tính ~ {Y('0,218')}; ung thư ~ {R('0,572 ± 0,363')}. Ngưỡng {R('PSAD > 0,15')} → {R('cần sinh thiết')}.<br>"
        f"3) <b>Tốc độ tăng PSA (PSAV):</b> Đo qua {B('3 lần thử trong 18 – 24 tháng')}; nếu {R('PSAV > 0,75 ng/ml/năm')} → nguy cơ ung thư cao.",
        f"Vùng xám 4–10 ng/ml dễ nhầm lẫn giữa u phì đại lành tính (tuyến rất to tiết nhiều PSA) và khối u ác tính nhỏ. {B('PSAD')} hiệu chỉnh theo thể tích tuyến, còn {B('f/tPSA')} phân biệt bản chất phân tử tự do vs phức hợp.",
        "B5.04", ["Can-lam-sang", "PSA"],
    ),
    basic(
        "SURG58-B5-04", "B5", "Men máu ALP/PAP & Tiêu chuẩn vàng Sinh thiết TTL qua TRUS", 1,
        f"{B('[Men máu & Sinh thiết TTL]')} Giá trị của men Phosphatase kiềm (ALP), PAP và kỹ thuật thực hiện Tiêu chuẩn vàng chẩn đoán xác định ung thư tuyến tiền liệt?",
        f"1) <b>Men máu hỗ trợ:</b><br>"
        f"   • <b>Phosphatase kiềm (ALP):</b> Tăng cao khi {R('di căn xương gây phản ứng tạo xương')}.<br>"
        f"   • <b>Phosphatase acid TTL (PAP):</b> Chất đánh dấu cổ điển, độ nhạy kém hơn PSA.<br>"
        f"2) <b>Sinh thiết TTL — Tiêu chuẩn vàng duy nhất:</b><br>"
        f"   • Thực hiện dưới hướng dẫn {G('siêu âm qua đầu dò trực tràng (TRUS)')}.<br>"
        f"   • Bấm kim hệ thống {G('ít nhất 6 – 12 vị trí (mỗi thùy 3 – 6 mẫu)')} từ đáy, giữa đến đỉnh TTL, tập trung vùng ngoại vi nghi ngờ.",
        f"PSA hay MRI chỉ có giá trị định hướng và phân tầng nguy cơ; chỉ duy nhất giải phẫu bệnh từ {G('sinh thiết kim qua TRUS')} mới khẳng định ung thư và cung cấp điểm Gleason phục vụ điều trị.",
        "B5.05", ["Can-lam-sang", "Tieu-chuan-vang"],
    ),
    basic(
        "SURG58-B5-05", "B5", "Chẩn đoán hình ảnh: TRUS, mpMRI PI-RADS, Xạ hình xương & PET-CT", 1,
        f"{B('[Cận lâm sàng — Hình ảnh học]')} Vai trò và dấu hiệu đặc trưng của Siêu âm TRUS, mpMRI (PI-RADS), Xạ hình xương Tc-99m và CT/PET-CT PSMA?",
        f"1) <b>Siêu âm qua trực tràng (TRUS):</b> U biểu hiện bằng {B('vùng giảm âm ở vùng ngoại vi (70%)')}, khảo sát vỏ bao tuyến và túi tinh.<br>"
        f"2) <b>Cộng hưởng từ đa thông số (mpMRI):</b> Đánh giá theo thang điểm {B('PI-RADS')} ({R('PI-RADS 4–5')} nghi ngờ ác tính cao), xâm lấn vỏ bao và túi tinh.<br>"
        f"3) <b>Xạ hình xương toàn thân:</b> Dùng {G('Technetium-99m')} phát hiện sớm các ổ di căn xương thể tạo xương.<br>"
        f"4) <b>CT ngực – bụng / PET-CT PSMA:</b> Đánh giá hạch chậu và di căn tạng.",
        f"Đa số u ngoại vi hút ít sóng âm tạo vùng giảm âm trên TRUS (~70%). Trước khi sinh thiết hoặc lập kế hoạch phẫu thuật, {B('mpMRI PI-RADS')} cho hình ảnh rõ nhất về ranh giới vỏ bao và túi tinh, còn {G('Xạ hình xương Tc-99m')} là tiêu chuẩn tìm M1b.",
        "B5.06", ["Can-lam-sang"],
    ),
    cloze(
        "SURG58-B5-06", "B5", "Cloze: Các ngưỡng sinh thiết PSA & Vùng xám",
        f"{B('[Ngưỡng sinh thiết PSA]')} Bắt buộc sinh thiết bất kể kết quả DRE khi tPSA > {clz(1, R('10 ng/ml'))}. Trong vùng xám 4–10 ng/ml, sinh thiết ngay nếu fPSA/tPSA < {clz(2, R('15%'))}. Ngưỡng tỷ trọng cảnh báo ác tính là PSAD > {clz(3, R('0,15'))}. Ngưỡng tốc độ tăng cảnh báo cao là PSAV > {clz(4, R('0,75 ng/ml/năm'))}.",
        "B5.03, B5.04", ["PSA", "Cloze"],
    ),

    # =========================================================================
    # B6: CHẨN ĐOÁN PHÂN BIỆT, PHÒNG BỆNH & TẦM SOÁT
    # =========================================================================
    basic(
        "SURG58-B6-01", "B6", "4 nhóm Chẩn đoán phân biệt Ung thư TTL", 1,
        f"{B('[Chẩn đoán phân biệt]')} Làm thế nào phân biệt Ung thư tuyến tiền liệt với Tăng sản lành tính (BPH), Viêm TTL, Sỏi TTL và các bệnh lý bàng quang/niệu đạo?",
        f"1) <b>Tăng sản lành tính TTL (BPH):</b> Tuyến to đều, {G('mềm mại, rãnh giữa còn')}, tỷ lệ {G('fPSA/tPSA > 20 – 25%')}.<br>"
        f"2) <b>Viêm TTL cấp / mạn:</b> Tuyến {Y('đau tức nóng sốt')}, bạch cầu niệu cao, PSA tăng thoáng qua rồi {G('trở về bình thường sau điều trị kháng sinh')}.<br>"
        f"3) <b>Sỏi TTL:</b> Siêu âm thấy {B('bóng cản âm kèm bóng lưng rõ rệt')}.<br>"
        f"4) <b>Bệnh đường tiểu dưới khác:</b> Hẹp niệu đạo, xơ teo cổ bàng quang, bàng quang tăng hoạt (OAB).",
        f"Trên DRE, BPH phì đại đồng đều giữ nguyên rãnh giữa và mềm đàn hồi, hoàn toàn trái ngược nhân cứng hay tuyến rắn như đá mất rãnh giữa của ung thư. Viêm cấp tính phá vỡ hàng rào tế bào tạm thời làm PSA tăng giả, cần trị hết viêm mới đánh giá lại.",
        "B6.01", ["Chan-doan-phan-biet"],
    ),
    basic(
        "SURG58-B6-02", "B6", "Chương trình Tầm soát định kỳ & Lối sống phòng bệnh", 1,
        f"{B('[Tầm soát & Phòng bệnh]')} Độ tuổi bắt đầu tầm soát (thông thường vs nguy cơ gia đình), 3 bước khám định kỳ hàng năm và các chất chống oxy hóa trong dinh dưỡng phòng bệnh?",
        f"1) <b>Tuổi bắt đầu tầm soát định kỳ hàng năm:</b> Nam giới từ {Y('50 tuổi trở lên')}; bắt đầu sớm từ {R('40 – 45 tuổi')} nếu có {B('bố hoặc anh em trai mắc ung thư TTL')}.<br>"
        f"2) <b>Bộ 3 bước tầm soát hàng năm:</b> (1) {G('Thăm khám trực tràng (DRE)')}; (2) {G('Định lượng PSA máu')}; (3) {B('Siêu âm TRUS')} khi có bất thường.<br>"
        f"3) <b>Dinh dưỡng phòng bệnh:</b> Giảm mỡ động vật; tăng cường rau củ quả chứa chất chống oxy hóa ({G('Lycopene trong cà chua chín, đậu nành, trà xanh')}).",
        f"Áp dụng tầm soát sớm hơn 5–10 năm (từ 40–45 tuổi) cho nam giới có tiền sử gia đình giúp phát hiện bệnh ngay tại cửa sổ khu trú T1–T2 có khả năng chữa khỏi 90%.",
        "B6.02", ["Tam-soat", "Phong-benh"],
    ),

    # =========================================================================
    # B7: ĐIỀU TRỊ (NGUYÊN TẮC, PHẪU THUẬT, XẠ TRỊ, ADT, CRPC & CẤP CỨU)
    # =========================================================================
    basic(
        "SURG58-B7-01", "B7", "Nguyên tắc điều trị theo giai đoạn & Theo dõi tích cực", 1,
        f"{B('[Nguyên tắc & Theo dõi tích cực]')} Mục tiêu điều trị giữa giai đoạn khu trú vs tiến triển/di căn; tiêu chuẩn lựa chọn và lịch trình Theo dõi tích cực (Active Surveillance)?",
        f"1) <b>Nguyên tắc phân tầng:</b><br>"
        f"   • <b>Khu trú (T1–T2, N0, M0):</b> Mục tiêu {G('điều trị triệt căn')} (kéo dài tối đa thời gian sống hoặc chữa khỏi).<br>"
        f"   • <b>Tiến triển tại chỗ / Di căn (T3–T4, N+, M1):</b> Mục tiêu {Y('tạm thời, kiểm soát toàn thân, giảm nhẹ triệu chứng, nâng cao chất lượng sống')}.<br>"
        f"2) <b>Đối tượng Theo dõi tích cực:</b> Người bệnh {Y('cao tuổi (> 70 tuổi)')} hoặc bệnh nội khoa nặng + thể tích u nhỏ ({G('< 0,5 cm³')}) + {G('Gleason thấp (2–6)')} + {G('PSA < 10 ng/ml')}.<br>"
        f"3) <b>Lịch trình giám sát:</b> Định kỳ thử PSA mỗi {B('3 – 6 tháng')}, thăm trực tràng và sinh thiết lại khi có dấu hiệu tiến triển.",
        f"Theo dõi tích cực tránh đẩy bệnh nhân lớn tuổi có u nguy cơ cực thấp vào các tai biến phẫu thuật/xạ trị không cần thiết, trong khi vẫn can thiệp kịp thời ngay khi PSA hay sinh thiết báo hiệu u chuyển độ ác.",
        "B7.01", ["Dieu-tri", "Active-Surveillance"],
    ),
    basic(
        "SURG58-B7-02", "B7", "Phẫu thuật cắt toàn bộ tuyến tiền liệt triệt căn", 1,
        f"{B('[Phẫu thuật triệt căn]')} Đối tượng áp dụng, phạm vi giải phẫu cắt bỏ – tạo hình, tỷ lệ sống không bệnh 10 năm và các tai biến – biến chứng của Phẫu thuật cắt toàn bộ TTL triệt căn?",
        f"1) <b>Đối tượng áp dụng:</b> BN còn trẻ, {G('kỳ vọng sống > 10 năm')}, u khu trú {B('T1–T2')}, {G('Gleason ≤ 7')}.<br>"
        f"2) <b>Phạm vi cắt & tạo hình:</b> Cắt bỏ toàn bộ TTL + {B('bao tuyến')} + {B('hai túi tinh')} + {B('bóng ống dẫn tinh')} + {B('nạo vét hạch chậu hai bên')}, sau đó {G('khâu nối cổ bàng quang với niệu đạo màng')}.<br>"
        f"3) <b>Hiệu quả:</b> Sống không bệnh sau 10 năm đạt {G('70% – 85%')}.<br>"
        f"4) <b>Tai biến sớm & Biến chứng muộn:</b> Sớm: chảy máu sau mổ, thủng trực tràng, tổn thương niệu quản; muộn hay gặp nhất là {R('đái rỉ / mất tự chủ nước tiểu (Incontinence)')} và {R('rối loạn cương dương (Impotence)')}.",
        f"Vì toàn bộ TTL bị cắt rời khỏi cổ bàng quang và niệu đạo màng, cấu trúc cơ thắt niệu đạo và bó mạch thần kinh cương chạy sát vỏ bao TTL rất dễ bị ảnh hưởng, giải thích 2 biến chứng muộn kinh điển là són tiểu và liệt dương.",
        "B7.02", ["Dieu-tri", "Phau-thuat"],
    ),
    basic(
        "SURG58-B7-03", "B7", "Xạ trị (EBRT, Brachytherapy) & Phẫu thuật áp lạnh", 1,
        f"{B('[Xạ trị & Áp lạnh]')} Trình bày liều lượng của Xạ trị chiếu ngoài (EBRT), nguồn phóng xạ dùng trong Cấy hạt phóng xạ (Brachytherapy) và ngưỡng nhiệt độ của Phẫu thuật áp lạnh (Cryosurgery)?",
        f"1) <b>Xạ trị chiếu ngoài (EBRT):</b> Chiếu liều cao {G('70 – 78 Gy')} vào TTL và hạch chậu — kiểm soát u {B('tương đương phẫu thuật')} ở giai đoạn khu trú.<br>"
        f"2) <b>Cấy hạt phóng xạ vào lòng tuyến (Brachytherapy):</b> Cấy các hạt {B('Iod-125')} hoặc {B('Palladium-103')} trực tiếp vào nhu mô tuyến qua tầng sinh môn dưới hướng dẫn siêu âm.<br>"
        f"3) <b>Phẫu thuật áp lạnh (Cryosurgery):</b> Dùng kim lạnh hạ nhiệt độ từ {B('-25°C đến -50°C')} để tiêu diệt tế bào u.",
        f"EBRT và Brachytherapy đều giúp tránh cuộc đại phẫu vùng chậu cho bệnh nhân khu trú, trong đó cấy hạt {B('I-125 / Pd-103')} giải phóng tia xạ liều cao tại chỗ với bán kính tác động cực ngắn bảo vệ trực tràng và bàng quang xung quanh.",
        "B7.03", ["Dieu-tri", "Xa-tri"],
    ),
    basic(
        "SURG58-B7-04", "B7", "Liệu pháp nội tiết cắt bỏ Androgen (ADT) & Hiệu ứng Flare-up", 1,
        f"{B('[Nội tiết ADT]')} Cơ chế của ADT, so sánh Cắt 2 tinh hoàn ngoại khoa vs Đồng vận LHRH/GnRH (thuốc & hiệu ứng flare-up), Kháng Androgen và Phong bế toàn diện CAB?",
        f"1) <b>Nguyên lý:</b> Tế bào ung thư TTL phụ thuộc {B('Testosterone')} → cắt nguồn Androgen làm tế bào u teo nhỏ và ngừng phát triển.<br>"
        f"2) <b>Cắt 2 tinh hoàn ngoại khoa:</b> Đơn giản, nhanh, hạ Testosterone xuống nồng độ thiến ({G('< 50 ng/dL')}) chỉ sau {G('24 giờ')}.<br>"
        f"3) <b>Đồng vận LHRH/GnRH ({B('Goserelin/Zoladex, Leuprolide/Eligard, Triptorelin')}):</b> Ban đầu gây tăng tiết Testosterone thoáng qua ({R('hiệu ứng bùng phát \"flare-up\"')} → phải che phủ bằng kháng androgen); sau {Y('2 – 3 tuần')} mới ức chế tuyến yên hạ về mức thiến.<br>"
        f"4) <b>Kháng Androgen ({B('Bicalutamide, Flutamide')}):</b> Ngăn Testosterone gắn thụ thể tại tế bào u.<br>"
        f"5) <b>Phong bế toàn diện (CAB):</b> Kết hợp cắt tinh hoàn (hoặc đồng vận LHRH) + kháng androgen.",
        f"Phối hợp {B('CAB')} kết hợp cắt tinh hoàn (hoặc đồng vận LHRH) với thuốc kháng androgen giúp triệt tiêu toàn diện nguồn kích thích tăng trưởng khối u tại thụ thể tế bào.",
        "B7.04", ["Dieu-tri", "Noi-tiet"],
    ),
    basic(
        "SURG58-B7-05", "B7", "Điều trị giai đoạn kháng cắt tinh hoàn (CRPC)", 1,
        f"{B('[Giai đoạn kháng thiến CRPC]')} Khi ung thư tiến triển thành giai đoạn kháng cắt tinh hoàn (CRPC), những phác đồ hóa chất và thuốc nội tiết thế hệ mới nào được sử dụng?",
        f"1) <b>Hóa chất toàn thân:</b> Phác đồ phối hợp chứa {G('Docetaxel kết hợp Prednisone')}, hoặc {G('Cabazitaxel')}.<br>"
        f"2) <b>Thuốc nội tiết thế hệ mới:</b><br>"
        f"   • {G('Abiraterone acetate')}: Ức chế tổng hợp androgen.<br>"
        f"   • {G('Enzalutamide')}: Kháng thụ thể androgen thế hệ mới.",
        f"Dù Testosterone máu đã dưới mức thiến (< 50 ng/dL), tế bào u CRPC tự thích nghi bằng cách tăng nhạy thụ thể androgen hoặc tự tổng hợp androgen nội tại. Bộ đôi {B('Abiraterone / Enzalutamide')} và taxane ({B('Docetaxel / Cabazitaxel')}) khóa chặt lối thoát này.",
        "B7.05", ["Dieu-tri", "CRPC"],
    ),
    basic(
        "SURG58-B7-06", "B7", "Xử trí 4 biến chứng cấp tính & Chăm sóc giảm nhẹ", 1,
        f"{B('[Xử trí biến chứng cấp]')} Biện pháp can thiệp cụ thể cho 4 biến chứng nặng của ung thư TTL tiến triển: Bí đái cấp, Vô niệu do tắc 2 niệu quản, Đau xương di căn và Chèn ép tủy sống cấp?",
        f"1) <b>Bí đái cấp do u chèn ép:</b> Cắt nội soi giải chèn ép ({G('TURP giảm nhẹ')}) hoặc {G('mở thông bàng quang trên xương mu')}.<br>"
        f"2) <b>Vô niệu / Suy thận do chèn ép 2 niệu quản:</b> Đặt ống thông niệu quản ngược dòng ({G('sonde Double J')}) hoặc {G('mở thông thận qua da')} tối thiểu dẫn lưu nước tiểu.<br>"
        f"3) <b>Đau nhức xương dữ dội:</b> Giảm đau bậc thang ({B('Morphin')}), truyền ức chế hủy xương ({B('Zoledronic acid')}), {Y('chiếu xạ giảm đau tại chỗ')}.<br>"
        f"4) <b>Chèn ép tủy sống cấp:</b> Tiêm {R('Dexamethasone liều cao khẩn cấp')} + {R('phẫu thuật giải ép cột sống hoặc xạ trị cấp cứu trong 24 – 48 giờ')} để tránh liệt vĩnh viễn.",
        f"Các biện pháp giải áp đường niệu (TURP giảm nhẹ, JJ, dẫn lưu thận) giúp cứu chức năng thận ngay tức thì để người bệnh đủ thể trạng tiếp nhận điều trị nội tiết/hóa chất toàn thân.",
        "B7.06", ["Dieu-tri", "Cap-cuu"],
    ),

    # =========================================================================
    # THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (4 THẺ >= 3)
    # =========================================================================
    algo(
        "SURG58-ALGO-01", "B5", "Quyết định Sinh thiết TTL", "Phân tầng tPSA & Các chỉ số phụ trợ vùng xám",
        f"1) <b>PSA < 4 ng/ml + DRE bình thường:</b> Nguy cơ ung thư {G('< 10%')} → Theo dõi định kỳ hàng năm (chú ý giới hạn theo tuổi 40–79).<br>"
        f"2) <b>PSA 4 – 10 ng/ml (Vùng xám — nguy cơ 20–25%):</b> Xét tiếp 3 chỉ số phụ trợ → Chỉ định {R('sinh thiết')} nếu {R('fPSA/tPSA < 15%')}, hoặc {R('PSAD > 0,15')}, hoặc {R('PSAV > 0,75 ng/ml/năm')}; ngược lại f/tPSA > 25% hướng tới BPH.<br>"
        f"3) <b>PSA > 10 ng/ml (nguy cơ ~50%):</b> {R('BẮT BUỘC sinh thiết TTL bất kể DRE')}.<br>"
        f"4) <b>Kỹ thuật sinh thiết chuẩn:</b> Thực hiện dưới hướng dẫn {G('TRUS')}, bấm kim hệ thống {G('ít nhất 6 – 12 vị trí (mỗi thùy 3 – 6 mẫu)')} vào vùng ngoại vi từ đáy đến đỉnh.",
        f"Thuật toán giúp tránh sinh thiết oan trong vùng xám 4–10 ng/ml (nhờ f/tPSA, PSAD, PSAV) nhưng tuyệt đối không bỏ sót khi PSA đã vượt ngưỡng 10 ng/ml hoặc DRE sờ thấy nhân cứng.",
        "B5.02, B5.03, B5.04, B5.05", ["PSA", "Sinh-thiet"],
    ),
    algo(
        "SURG58-ALGO-02", "B7", "Điều trị Ung thư TTL khu trú", "Lựa chọn Theo dõi tích cực vs Phẫu thuật vs Xạ trị",
        f"1) <b>Bệnh nhân > 70 tuổi / bệnh nội khoa nặng + nguy cơ rất thấp (u < 0,5 cm³, Gleason 2–6, PSA < 10):</b> Chọn {G('Theo dõi tích cực')} (PSA mỗi 3–6 tháng, DRE & sinh thiết lại khi tiến triển).<br>"
        f"2) <b>BN trẻ, kỳ vọng sống > 10 năm + T1–T2 + Gleason ≤ 7:</b> {G('Phẫu thuật cắt toàn bộ TTL triệt căn')} (cùng bao tuyến, 2 túi tinh, bóng ống dẫn tinh, hạch chậu 2 bên; sống không bệnh 10 năm 70–85%).<br>"
        f"3) <b>Giải pháp thay thế phẫu thuật tương đương ở giai đoạn khu trú:</b> {B('Xạ trị chiếu ngoài EBRT (70–78 Gy)')}, {B('Cấy hạt phóng xạ Brachytherapy (I-125, Pd-103)')}, hoặc {Y('Áp lạnh Cryosurgery (-25 đến -50°C)')}.",
        f"Việc chọn phẫu thuật triệt căn hay xạ trị cho giai đoạn khu trú phụ thuộc chặt chẽ vào tuổi sinh học (> 10 năm kỳ vọng sống), thang điểm Gleason (≤ 7) và sự cân nhắc biến chứng són tiểu/liệt dương.",
        "B7.01, B7.02, B7.03", ["Dieu-tri", "Phau-thuat"],
    ),
    algo(
        "SURG58-ALGO-03", "B7", "Điều trị Toàn thân T3–T4 / Di căn & CRPC", "Chuỗi Liệu pháp Cắt Androgen (ADT) đến Kháng thiến",
        f"1) <b>Khởi trị cắt Testosterone nhanh tức thì (< 50 ng/dL sau 24 giờ):</b> {G('Cắt 2 tinh hoàn ngoại khoa')}.<br>"
        f"2) <b>Khởi trị nội khoa bằng đồng vận LHRH ({B('Goserelin, Leuprolide, Triptorelin')}):</b> Bắt buộc phối hợp trước/song song {R('thuốc kháng Androgen (Bicalutamide, Flutamide)')} để {R('chặn hiệu ứng flare-up')}, duy trì sau 2–3 tuần để đạt mức thiến hoặc phối hợp {G('CAB')}.<br>"
        f"3) <b>Khi tiến triển thành Kháng cắt tinh hoàn (CRPC):</b> Chuyển {G('Hóa chất Docetaxel + Prednisone / Cabazitaxel')} hoặc nội tiết thế hệ mới {G('Abiraterone acetate / Enzalutamide')}.",
        f"Cắt tinh hoàn ngoại khoa thắng về tốc độ (24 giờ) và không gây flare-up; còn phác đồ nội khoa bắt buộc chặn thụ thể bằng kháng androgen ở tuần đầu nhằm bảo vệ bệnh nhân khỏi bùng phát cơn đau xương hoặc tụt tủy sống.",
        "B7.04, B7.05", ["Dieu-tri", "Noi-tiet", "CRPC"],
    ),
    algo(
        "SURG58-ALGO-04", "B7", "Cấp cứu Ung thư TTL tiến triển", "Xử trí nhanh Bí đái, Vô niệu, Đau xương & Chèn ép tủy",
        f"1) <b>Bí đái cấp do u chèn ép niệu đạo tuyến:</b> {G('TURP giảm nhẹ')} hoặc {G('mở thông bàng quang trên xương mu')}.<br>"
        f"2) <b>Vô niệu / Suy thận do u đè bẹp 2 miệng niệu quản:</b> Đặt {G('sonde Double J ngược dòng')} hoặc {G('mở thông thận qua da tối thiểu')}.<br>"
        f"3) <b>Đau nhức xương di căn dữ dội:</b> Giảm đau bậc thang ({B('Morphin')}) + truyền {B('Zoledronic acid')} + {Y('xạ trị giảm đau tại chỗ')}.<br>"
        f"4) <b>Yếu liệt 2 chi dưới / bí tiểu do chèn ép tủy sống cấp:</b> Tiêm ngay {R('Dexamethasone liều cao')} + {R('giải ép cột sống / xạ trị cấp cứu trong 24 – 48 giờ')}.",
        f"Mọi biến chứng tắc nghẽn cơ học hay chèn ép thần kinh trong giai đoạn muộn đều đòi hỏi giải áp cơ học khẩn cấp song hành với điều trị nền, trong đó cửa sổ chèn ép tủy sống chỉ có 24–48 giờ để cứu chức năng vận động.",
        "B7.06, B4.02", ["Dieu-tri", "Cap-cuu"],
    ),

    # =========================================================================
    # BẪY LÂM SÀNG & CỜ ĐỎ CẤP CỨU (9 THẺ >= 8)
    # =========================================================================
    trap(
        "SURG58-TRAP-01", "B4", "Đợi tiểu khó / bí tiểu mới tầm soát ung thư TTL",
        f"Nam giới 55 tuổi hoàn toàn không tiểu khó, không tiểu đêm — Vì sao bác sĩ vẫn không được loại trừ ung thư TTL nếu chưa làm DRE và PSA?",
        f"1) <b>Vị trí giải phẫu vùng khởi phát:</b> Ung thư TTL giai đoạn sớm thường khu trú ở {B('vùng ngoại vi (thùy sau)')} nên {R('hoàn toàn không có triệu chứng')}.<br>"
        f"2) <b>Sự đối lập với BPH:</b> Khi bệnh nhân bắt đầu tiểu khó, bí đái, đái máu, u thường đã phát triển lớn chèn ép hoặc phá vỡ vỏ bao.",
        f"Triệu chứng đường tiểu dưới chỉ xuất hiện khi u ăn lan vào trung tâm/niệu đạo. Nếu chờ triệu chứng cơ năng mới khám thì bỏ lỡ cơ hội chữa khỏi 90% ở giai đoạn khu trú T1–T2.",
        "B4.01, B4.03, B0.02", ["Lam-sang", "Tam-soat"],
    ),
    trap(
        "SURG58-TRAP-02", "B5", "Bỏ qua sinh thiết khi PSA > 10 mà DRE bình thường (hoặc vùng xám)",
        f"Thăm trực tràng (DRE) thấy tuyến tiền liệt mềm nhẵn hoàn toàn bình thường nhưng xét nghiệm PSA máu đạt 12 ng/ml (hoặc PSA 6 ng/ml với f/tPSA = 11%) — Bẫy bỏ sót là gì?",
        f"1) <b>Sai lầm tin tuyệt đối vào DRE âm tính:</b> Khối u giai đoạn {B('T1c')} không thể sờ thấy qua DRE và không thấy trên siêu âm.<br>"
        f"2) <b>Quyết định bắt buộc:</b> Với {R('PSA > 10 ng/ml')} (nguy cơ ung thư 50%), {R('BẮT BUỘC sinh thiết TTL bất kể kết quả DRE')}; trong vùng xám 4–10 ng/ml, {R('fPSA/tPSA < 15%')} cũng đòi hỏi sinh thiết ngay.",
        f"Tỷ lệ ung thư lên tới 50% ở ngưỡng PSA > 10 ng/ml và nguy cơ rất cao khi f/tPSA tụt dưới 15%. Các ổ u nhỏ nằm ở vị trí khó sờ hoặc mặt trước chỉ có thể bắt được qua sinh thiết hệ thống.",
        "B5.03, B5.04, B3.01", ["PSA", "DRE"],
    ),
    trap(
        "SURG58-TRAP-03", "B6", "Nhầm tăng PSA do Viêm TTL cấp với Ung thư TTL",
        f"Bệnh nhân nam sốt nóng, tuyến tiền liệt sưng đau tức, bạch cầu niệu cao và xét nghiệm PSA tăng 14 ng/ml — Sai lầm xử trí là gì?",
        f"1) <b>Tăng PSA thoáng qua do viêm:</b> Trong {B('viêm tuyến tiền liệt cấp / mạn')}, PSA có thể tăng thoáng qua rất cao do tổn thương hàng rào mô tuyến.<br>"
        f"2) <b>Hướng xử trí chuẩn:</b> Điều trị {G('kháng sinh ổn định tình trạng viêm')}, sau đó kiểm tra lại nồng độ PSA — nếu là viêm đơn thuần, PSA sẽ {G('trở về bình thường')}.",
        f"Sinh thiết qua trực tràng ngay lúc tuyến đang viêm cấp không chỉ làm sai lệch đánh giá PSA mà còn tăng vọt nguy cơ nhiễm khuẩn huyết nặng. Luôn giải quyết nhiễm khuẩn trước rồi đánh giá lại.",
        "B6.01", ["Chan-doan-phan-biet", "PSA"],
    ),
    trap(
        "SURG58-TRAP-04", "B5", "Sinh thiết TTL quá ít mẫu bỏ sót vùng ngoại vi",
        f"Thấy nốt nghi ngờ ở một thùy TTL nên chỉ bấm 1–2 mẫu kim tại điểm đó và trả về lành tính — Bẫy kỹ thuật sinh thiết nằm ở đâu?",
        f"1) <b>Yêu cầu chuẩn mực:</b> Sinh thiết dưới hướng dẫn {G('TRUS')} bắt buộc bấm kim hệ thống {R('ít nhất 6 – 12 vị trí (mỗi thùy 3 – 6 mẫu)')} từ đáy, giữa đến đỉnh TTL.<br>"
        f"2) <b>Trọng tâm giải phẫu:</b> Tập trung kỹ vào {B('vùng ngoại vi')} nơi 70% khối u xuất phát (biểu hiện giảm âm trên TRUS).",
        f"Ung thư tuyến tiền liệt thường có nhiều ổ nhỏ rải rác hoặc âm thầm ở vùng ngoại vi mà siêu âm thường không thấy rõ. Chỉ bấm 1–2 mẫu gây âm tính giả rất cao và đánh giá sai thang điểm Gleason.",
        "B5.05, B5.06", ["Sinh-thiet"],
    ),
    trap(
        "SURG58-TRAP-05", "B3", "Chủ quan với Đau lưng tăng về đêm ở nam lớn tuổi",
        f"Nam giới trên 60 tuổi đau thắt lưng kéo dài tăng mạnh về đêm, xét nghiệm thấy Phosphatase kiềm (ALP) tăng cao và PSA > 100 ng/ml — Đừng điều trị nhầm như thoái hóa cột sống đơn thuần?",
        f"1) <b>Đường lan di căn xương M1b:</b> Di căn xương thể {R('tạo xương (osteoblastic)')} qua {B('đám rối tĩnh mạch Batson không có van')} với vị trí số 1 là {R('cột sống thắt lưng')}, số 2 là {R('xương chậu')}.<br>"
        f"2) <b>Xác định chẩn đoán:</b> Đau tăng về đêm + {R('ALP tăng cao')} + {R('PSA > 100 ng/ml')} → Chỉ định ngay {G('Xạ hình xương toàn thân với Technetium-99m')}.",
        f"Đau cột sống do thoái hóa cơ học thường giảm khi nằm nghỉ ban đêm, trái ngược hoàn toàn với đau do di căn xương tăng nặng về đêm. ALP tăng cao phản ánh hoạt động tạo xương phản ứng quanh ổ di căn.",
        "B3.03, B3.04, B4.02, B5.03, B5.05, B5.06", ["Di-can", "Lam-sang"],
    ),
    redflag(
        "SURG58-TRAP-06", "B7", "Tiêm đồng vận LHRH đơn độc gây hiệu ứng Flare-up",
        f"Bệnh nhân ung thư TTL di căn cột sống (M1b) được tiêm Goserelin (Zoladex) hoặc Leuprolide đơn độc ngày đầu mà không dùng thuốc kháng Androgen kèm theo — Tai biến nguy kịch nào sẽ xảy ra?",
        f"1) <b>Hiệu ứng bùng phát \"flare-up\":</b> Đồng vận LHRH/GnRH ban đầu kích thích tuyến yên gây {R('tăng tiết Testosterone thoáng qua')} trước khi ức chế được sau {Y('2 – 3 tuần')}.<br>"
        f"2) <b>Nguy cơ & Cách phòng tránh:</b> Đợt tăng Testosterone đột ngột thúc đẩy u phì đại nhanh gây {R('đau xương dữ dội, bí đái hoặc chèn ép tủy sống cấp')}. Bắt buộc {G('che phủ bằng thuốc kháng Androgen (Bicalutamide, Flutamide)')} trước/cùng lúc tiêm.",
        f"Quên kháng androgen che phủ hiệu ứng flare-up ở người đã có di căn cột sống là sai lầm điều trị nguy hiểm có thể kích hoạt liệt hai chi dưới chỉ sau vài ngày khởi trị nội tiết.",
        "B7.04", ["Noi-tiet", "Co-do"],
    ),
    redflag(
        "SURG58-TRAP-07", "B7", "Bỏ qua cửa sổ vàng Chèn ép tủy sống cấp 24–48 giờ",
        f"Bệnh nhân ung thư TTL di căn cột sống thắt lưng đột ngột than yếu hai chân và bí tiểu cấp — Nếu trì hoãn chờ hội chẩn qua vài ngày sẽ mất gì và phác đồ tối khẩn là gì?",
        f"1) <b>Cờ đỏ thần kinh:</b> {R('Hội chứng chèn ép tủy sống cấp')} — chậm trễ sẽ gây {R('liệt hai chi dưới vĩnh viễn')}.<br>"
        f"2) <b>Lệnh cấp cứu trong 24 – 48 giờ:</b> Tiêm ngay {R('Dexamethasone liều cao khẩn cấp')} kết hợp {R('phẫu thuật giải ép cột sống hoặc xạ trị cấp cứu trong vòng 24 – 48 giờ')}.",
        f"Khối u di căn từ đám rối Batson ăn vào thân đốt sống gây phù tủy và chèn ép cơ học rễ – tủy sống. Corticoid liều cao giảm phù tủy tức thì tạo thời gian vàng cho mổ giải ép hoặc xạ trị cấp cứu.",
        "B4.02, B7.06", ["Cap-cuu", "Co-do"],
    ),
    trap(
        "SURG58-TRAP-08", "B7", "Mở rộng cắt TTL triệt căn sai đối tượng / quên tư vấn biến chứng",
        f"Bệnh nhân ung thư TTL T3b (ăn túi tinh) hoặc nam giới 76 tuổi bệnh tim nặng đòi phẫu thuật cắt toàn bộ TTL triệt căn — Sai lầm nằm ở chỉ định và tư vấn nào?",
        f"1) <b>Sai chỉ định triệt căn:</b> Cắt TTL triệt căn chỉ dành cho người {G('còn trẻ, kỳ vọng sống > 10 năm, khu trú T1–T2, Gleason ≤ 7')}; giai đoạn {R('T3–T4, N+, M1')} chỉ điều trị toàn thân/giảm nhẹ.<br>"
        f"2) <b>Tư vấn bắt buộc biến chứng muộn:</b> Hai biến chứng thường gặp nhất sau mổ là {R('đái rỉ / mất tự chủ nước tiểu (Incontinence)')} và {R('rối loạn cương dương (Impotence)')}.",
        f"Ở T3b khối u đã vượt bao xâm lấn túi tinh nên mổ triệt căn đơn thuần không sạch rìa u mà làm tăng nặng tai biến rò/thủng trực tràng, chảy máu và rối loạn cơ thắt.",
        "B7.01, B7.02", ["Phau-thuat", "Dieu-tri"],
    ),
    trap(
        "SURG58-TRAP-09", "B6", "Áp dụng mốc tầm soát 50 tuổi cứng nhắc cho người có bố/anh em mắc bệnh",
        f"Nam giới 42 tuổi có bố và anh trai từng mắc ung thư TTL đến khám tổng quát, bác sĩ hẹn tới năm 50 tuổi mới làm DRE và PSA — Sai sót dự phòng ở đâu?",
        f"1) <b>Mức tăng nguy cơ:</b> Có bố hoặc anh em trai mắc ung thư TTL làm nguy cơ mắc bệnh cao hơn gấp {R('2 – 3 lần')}.<br>"
        f"2) <b>Mốc tầm soát điều chỉnh:</b> Nhóm nguy cơ gia đình bắt buộc tầm soát hàng năm ngay từ {G('40 – 45 tuổi')} (thay vì đợi đến 50 tuổi như dân số chung), gồm {B('DRE + PSA máu + TRUS khi bất thường')}.",
        f"Yếu tố di truyền thúc đẩy ung thư TTL khởi phát sớm hơn trung bình 5–10 năm. Tầm soát sớm từ 40–45 tuổi giúp bắt gọn bệnh ở ngưỡng khu trú có thể chữa khỏi 90%.",
        "B1.02, B6.02", ["Tam-soat", "Di-truyen"],
    ),
]
