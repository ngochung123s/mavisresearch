# -*- coding: utf-8 -*-
"""
Dữ liệu thẻ Anki chuẩn hóa cho bài SURG-56: Ung Thư Thận (RCC)
Rebuild 100% từ barem: SURG-56_Ung_thu_than_BAREM.md
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
    b_tag = f"Ngoai::SURG-56::{section}"
    t_tag = f"Tier-{tier}"
    all_tags = [b_tag, t_tag] + [f"Ngoai::{t}" for t in tags]
    if red_flag:
        all_tags.append("Ngoai::Co-do")
    
    back = f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}"
    
    res = {
        "id": cid,
        "type": "basic",
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
    b_tag = f"Ngoai::SURG-56::{section}"
    return {
        "id": cid,
        "type": "cloze",
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
        "SURG56-B0-01", "B0", "Phân loại u ác tính nguyên phát thận & Dịch tễ RCC", 1,
        f"{B('[Đại cương]')} Các loại u ác tính nguyên phát ở thận, tỷ lệ chiếm ưu thế của Ung thư biểu mô tế bào thận (RCC), thứ hạng tiết niệu và tỷ lệ trong ung thư người lớn?",
        f"1) <b>Nhóm u ác tính nguyên phát:</b> Gồm {B('ung thư tế bào thận')}, {B('sarcoma thận')} và {B('u lympho thận nguyên phát')}..., trong đó {B('ung thư tế bào thận (RCC)')} chiếm tới {Y('90%')}.<br>"
        f"2) <b>Thứ hạng tiết niệu:</b> RCC đứng hàng thứ {Y('2')} trong các bệnh ác tính hệ tiết niệu (sau {B('ung thư bàng quang')}).<br>"
        f"3) <b>Tỷ trọng chung:</b> Chiếm {Y('1 – 2%')} toàn bộ các loại ung thư ở người lớn.",
        f"Vì biểu mô ống thận là thành phần chiếm đa số khối lượng nhu mô thận và liên tục tiếp xúc với các chất độc hại được lọc/cô đặc qua nước tiểu, nên {B('RCC')} áp đảo tới {Y('90%')} so với sarcoma mô liên kết hay lymphoma. Trên lâm sàng tiết niệu, thứ tự phổ biến thường gặp là bàng quang rồi mới đến nhu mô thận.",
        "B0.01, B0.02", ["Dai-cuong", "Dich-te"],
    ),
    basic(
        "SURG56-B0-02", "B0", "Tuổi khởi phát & Tỷ lệ giới tính RCC", 1,
        f"{B('[Dịch tễ]')} Độ tuổi thường khởi phát và tỷ lệ phân bố nam/nữ của ung thư biểu mô tế bào thận?",
        f"1) <b>Khung tuổi hay gặp:</b> Bệnh thường xuất hiện ở người lớn {Y('trên 40 tuổi')}.<br>"
        f"2) <b>Giới tính:</b> Nam giới gặp nhiều hơn nữ giới với tỷ lệ nam/nữ là {Y('2/1')}.",
        f"Nam giới mắc gấp đôi nữ giới phản ánh rõ ảnh hưởng tích lũy của các yếu tố phơi nhiễm ngoại sinh theo thời gian ở tuổi trung niên trở lên, nổi bật nhất là thói quen hút thuốc lá và nghề nghiệp tiếp xúc hóa chất công nghiệp, dung môi hữu cơ.",
        "B0.03", ["Dich-te"],
    ),
    cloze(
        "SURG56-B0-03", "B0", "Cloze: Tỷ lệ RCC & Tỷ lệ nam/nữ",
        f"{B('[Dịch tễ RCC]')} Ung thư tế bào thận (RCC) chiếm tới {clz(1, Y('90%'))} các u ác tính nguyên phát ở thận, đứng hàng thứ {clz(2, Y('2'))} hệ tiết niệu (sau ung thư bàng quang), chiếm {clz(3, Y('1 – 2%'))} ung thư người lớn và tỷ lệ nam/nữ là {clz(4, Y('2/1'))}.",
        "B0.01, B0.02, B0.03", ["Dich-te", "Cloze"],
    ),

    # =========================================================================
    # B1: NGUYÊN NHÂN VÀ CƠ CHẾ BỆNH SINH
    # =========================================================================
    basic(
        "SURG56-B1-01", "B1", "Hút thuốc lá & Hydrocarbon thơm đa vòng", 1,
        f"{B('[Yếu tố nguy cơ hàng đầu]')} Dù nguyên nhân gây ung thư thận chưa được làm rõ hoàn toàn, yếu tố nguy cơ hàng đầu là gì và cơ chế gây ung thư từ yếu tố này diễn ra ra sao?",
        f"1) <b>Yếu tố hàng đầu:</b> {R('Hút thuốc lá')}.<br>"
        f"2) <b>Chất sinh ung trong khói thuốc:</b> Khói thuốc lá chứa nồng độ cao chất sinh ung nhóm {R('hydrocarbon thơm đa vòng (pyrene)')}, gây {R('tổn thương gen')} và làm tăng nguy cơ mắc ung thư nói chung cũng như ung thư thận nói riêng.",
        f"Các dẫn xuất {B('pyrene')} hít từ khói thuốc lá được hấp thu vào máu, chuyển hóa và bài tiết qua thận. Khi đi qua ống thận, nồng độ chất sinh ung tăng cao do quá trình cô đặc nước tiểu, trực tiếp làm tổn thương DNA biểu mô ống thận.",
        "B1.01", ["Nguyen-nhan", "Sinh-ly-benh"],
    ),
    basic(
        "SURG56-B1-02", "B1", "Hóa chất nghề nghiệp & Di truyền VHL", 1,
        f"{B('[Nguy cơ nghề nghiệp & Di truyền]')} Kể tên đầy đủ các nhóm hóa chất/nghề nghiệp phơi nhiễm và các yếu tố di truyền liên quan đến ung thư thận?",
        f"1) <b>Phơi nhiễm hóa chất độc hại:</b> Thường xuyên tiếp xúc với {R('dung môi hữu cơ')}, {Y('thợ in')}, {Y('thợ nhuộm')}, {Y('làm tóc')}, {Y('công nhân hóa chất')}, tiếp xúc với {R('xăng dầu')}.<br>"
        f"2) <b>Di truyền gia đình:</b> Bệnh {B('Von Hippel-Lindau (VHL)')} và {B('ung thư thận tế bào sáng có tính chất gia đình')}.",
        f"Người làm việc trong môi trường dung môi hữu cơ, thuốc nhuộm, xăng dầu hấp thu độc chất qua đường hô hấp/da rồi thải trừ qua đường niệu, làm biến đổi biểu mô ống lượn gần. Trong bệnh {B('VHL')}, đột biến gen ức chế u VHL gây hoạt hóa con đường thiếu oxy (HIF), kích thích tăng sinh mạch máu và hình thành khối u thận giàu mạch.",
        "B1.02, B1.03", ["Nguyen-nhan", "Di-truyen"],
    ),

    # =========================================================================
    # B2: GIẢI PHẪU BỆNH (ĐẠI THỂ, MÔ HỌC, VI THỂ)
    # =========================================================================
    basic(
        "SURG56-B2-01", "B2", "Đại thể khối u ung thư thận", 1,
        f"{B('[Giải phẫu bệnh — Đại thể]')} Mô tả đầy đủ kích thước, vị trí trên thận, vỏ bọc, màu sắc diện cắt và đặc điểm mạch máu/nhu mô bên trong của khối u thận?",
        f"1) <b>Kích thước & Vị trí:</b> Kích thước thay đổi từ {Y('1 – 10 cm')}, thường nằm ở các cực ({B('cực trên hoặc cực dưới')}), đôi khi phát triển lồi ra ngoài thận.<br>"
        f"2) <b>Hình dáng & Vỏ bọc:</b> Khối u thường tròn, có {B('vỏ bọc giả')}.<br>"
        f"3) <b>Diện cắt & Tổn thương trong u:</b> Diện cắt màu {Y('vàng hoặc xám loang lổ')}, {R('nhiều mạch máu tân tạo')}, thường kèm theo {R('ổ hoại tử và chảy máu bên trong')}.",
        f"Màu vàng đặc trưng trên diện cắt chính là do tế bào u sáng tích tụ rất nhiều {B('lipid và glycogen')}. U tăng sinh mạch cực mạnh nhưng hệ mạch tân tạo mong manh nên dễ vỡ gây xuất huyết, hoại tử tạo hình ảnh loang lổ và có nguy cơ vỡ tự phát gây chảy máu sau phúc mạc.",
        "B2.01", ["Giai-phau-benh"],
    ),
    basic(
        "SURG56-B2-02", "B2", "Phân loại mô học RCC", 1,
        f"{B('[Giải phẫu bệnh — Mô học]')} Liệt kê 4 thể mô học của ung thư biểu mô thận cùng tỷ lệ và đặc điểm mức độ ác tính nổi bật?",
        f"1) <b>Thể hay gặp nhất:</b> {B('Ung thư biểu mô tế bào sáng (Clear cell RCC)')} chiếm {Y('75 – 85%')}.<br>"
        f"2) <b>Thể nhú:</b> {B('Papillary RCC')}.<br>"
        f"3) <b>Thể kỵ màu:</b> {B('Chromophobe RCC')}.<br>"
        f"4) <b>Thể ống góp:</b> {R('Ung thư ống góp Bellini')} — {R('rất hiếm và ác tính cao')}.",
        f"Sự phân chia mô học phản ánh nguồn gốc giải phẫu khác nhau dọc theo nephron: Clear cell và Papillary thường xuất phát từ ống lượn gần, Chromophobe từ vùng vỏ ống góp, còn ung thư ống góp {B('Bellini')} bắt nguồn từ tủy thận với tiên lượng cực xấu và diễn tiến xâm lấn rất nhanh.",
        "B2.02", ["Giai-phau-benh"],
    ),
    basic(
        "SURG56-B2-03", "B2", "Vi thể tế bào ung thư thận", 1,
        f"{B('[Giải phẫu bệnh — Vi thể]')} Mô tả hình thái vi thể, cấu trúc sắp xếp, thành phần bào tương, đặc điểm nhân và các tế bào biến thể đi kèm của RCC?",
        f"1) <b>Cấu trúc sắp xếp:</b> Tế bào u đa dạng, kết hợp vùng {B('nhú')}, {B('bè')} và {B('xốp')}.<br>"
        f"2) <b>Bào tương & Nhân tế bào sáng:</b> Bào tương chứa nhiều {Y('glycogen và lipid')}, nhân {R('to tăng sắc')}.<br>"
        f"3) <b>Tế bào đi kèm:</b> Có khi kèm {B('tế bào hạt ưa acid')} hoặc {R('tế bào dạng sarcomatoid')}.",
        f"Trong quá trình xử lý tiêu bản mô học thường quy (paraffin), lipid và glycogen trong bào tương bị hòa tan để lại khoảng sáng trong suốt dưới kính hiển vi — đó là nguồn gốc tên gọi {B('tế bào sáng')}. Sự xuất hiện thành phần {R('dạng sarcomatoid')} báo hiệu độ ác tính cao và tiên lượng xấu hơn.",
        "B2.03", ["Giai-phau-benh"],
    ),
    cloze(
        "SURG56-B2-04", "B2", "Cloze: Tỷ lệ Clear cell RCC & Thành phần bào tương",
        f"{B('[Mô học — Vi thể]')} Thể giải phẫu bệnh thường gặp nhất là ung thư biểu mô tế bào sáng chiếm {clz(1, Y('75 – 85%'))}; trên vi thể bào tương chứa nhiều {clz(2, B('glycogen và lipid'))}.",
        "B2.02, B2.03", ["Giai-phau-benh", "Cloze"],
    ),

    # =========================================================================
    # B3: PHÂN LOẠI GIAI ĐOẠN TNM
    # =========================================================================
    basic(
        "SURG56-B3-01", "B3", "Phân loại T1 & T2 trong TNM ung thư thận", 1,
        f"{B('[TNM — T1 & T2]')} Trình bày tiêu chuẩn kích thước và giới hạn giải phẫu của T1 (T1a, T1b) và T2 (T2a, T2b) trong ung thư thận?",
        f"1) <b>T1 (≤ 7 cm, giới hạn trong thận):</b><br>"
        f"   • <b>T1a:</b> U {Y('≤ 4 cm')}, giới hạn ở thận.<br>"
        f"   • <b>T1b:</b> U {Y('> 4 cm nhưng ≤ 7 cm')}, giới hạn ở thận.<br>"
        f"2) <b>T2 (> 7 cm, giới hạn ở thận):</b><br>"
        f"   • <b>T2a:</b> U {Y('> 7 cm nhưng ≤ 10 cm')}.<br>"
        f"   • <b>T2b:</b> U {Y('> 10 cm')}, giới hạn ở thận.",
        f"Bộ số mốc kích thước T1–T2 bám chặt ba ngưỡng cắt: {Y('4 cm')} – {Y('7 cm')} – {Y('10 cm')}. Điều kiện tiên quyết của cả T1 và T2 là khối u vẫn còn {G('khu trú hoàn toàn trong nhu mô/bao thận')}, chưa xâm lấn ra mô mỡ quanh thận hay tĩnh mạch lớn. Ngưỡng {Y('T1a ≤ 4 cm')} là mốc vàng chỉ định phẫu thuật cắt thận bán phần.",
        "B3.01", ["TNM", "Phan-loai"],
    ),
    basic(
        "SURG56-B3-02", "B3", "Phân loại T3 & T4 trong TNM ung thư thận", 1,
        f"{B('[TNM — T3 & T4]')} Phân biệt chi tiết T3 (T3a, T3b, T3c) và T4 trong ung thư thận dựa trên cấu trúc giải phẫu xâm lấn?",
        f"1) <b>T3 (lan tĩnh mạch lớn hoặc mô quanh thận, CHƯA vượt cân Gerota):</b><br>"
        f"   • <b>T3a:</b> Xâm lấn {R('tĩnh mạch thận hoặc các nhánh tĩnh mạch trong thận')}, hoặc xâm lấn {R('lớp mỡ quanh thận / mỡ rốn thận')} nhưng chưa vượt quá cân Gerota.<br>"
        f"   • <b>T3b:</b> Lan vào {R('tĩnh mạch chủ dưới đoạn dưới cơ hoành')}.<br>"
        f"   • <b>T3c:</b> Lan vào {R('tĩnh mạch chủ dưới đoạn trên cơ hoành')} hoặc {R('xâm lấn thành tĩnh mạch chủ')}.<br>"
        f"2) <b>T4:</b> U {R('xâm lấn vượt qua cân Gerota')} hoặc {R('xâm lấn trực tiếp vào tuyến thượng thận cùng bên')}.",
        f"Ranh giới quyết định giữa T3 và T4 là lớp {B('cân Gerota')} và {B('tuyến thượng thận cùng bên')}: còn nằm trong cân Gerota hoặc mới tạo chồi huyết khối trong lòng tĩnh mạch thận/tĩnh mạch chủ dưới thì vẫn xếp T3; khi đã xuyên thủng cân Gerota hoặc ăn trực tiếp vào thượng thận cùng bên là T4.",
        "B3.02", ["TNM", "Phan-loai"],
    ),
    basic(
        "SURG56-B3-03", "B3", "Phân loại Hạch vùng (N) & Di căn xa (M)", 1,
        f"{B('[TNM — N & M]')} Định nghĩa hạch vùng (Nx, N0, N1) kèm vị trí hạch chặng đầu và phân loại di căn xa (M0, M1) kèm tỷ lệ các cơ quan đích?",
        f"1) <b>Hạch bạch huyết vùng (N):</b><br>"
        f"   • <b>Nx:</b> Không đánh giá được hạch vùng; <b>N0:</b> Không di căn hạch vùng.<br>"
        f"   • <b>N1:</b> Có di căn hạch vùng ({B('hạch rốn thận, quanh động mạch chủ / tĩnh mạch chủ')}).<br>"
        f"2) <b>Di căn xa (M):</b><br>"
        f"   • <b>M0:</b> Không có di căn xa; <b>M1:</b> Có di căn xa tại {R('phổi (50%)')}, {R('xương (30 – 40%)')}, {R('gan')}, {R('não')}...",
        f"Vì tĩnh mạch thận đổ trực tiếp vào tĩnh mạch chủ dưới về tim phải rồi lên thẳng tuần hoàn phổi, nên {R('phổi (50%)')} là đích di căn xa số một của RCC, theo sau là {R('xương (30 – 40%)')}. Việc nắm đúng chuỗi hạch rốn thận và quanh ĐMC/TMC giúp định hướng phạm vi nạo hạch trong phẫu thuật Robson.",
        "B3.03", ["TNM", "Di-can"],
    ),
    cloze(
        "SURG56-B3-04", "B3", "Cloze: 3 ngưỡng kích thước T1–T2 của RCC",
        f"{B('[Ngưỡng TNM]')} Khối u giới hạn trong thận xếp T1a khi kích thước ≤ {clz(1, Y('4 cm'))}. Ranh giới chuyển tiếp giữa T1b và T2a là mốc {clz(2, Y('7 cm'))}. Ranh giới chuyển tiếp giữa T2a và T2b là mốc {clz(3, Y('10 cm'))}.",
        "B3.01", ["TNM", "Cloze"],
    ),

    # =========================================================================
    # B4: TRIỆU CHỨNG LÂM SÀNG & HỘI CHỨNG CẬN UNG THƯ
    # =========================================================================
    basic(
        "SURG56-B4-01", "B4", "Diễn biến sớm & Tần suất Tam chứng Guyon", 1,
        f"{B('[Diễn biến lâm sàng]')} Diễn biến giai đoạn sớm của ung thư thận có đặc điểm gì, tỷ lệ phát hiện tình cờ hiện nay và tỷ lệ gặp Tam chứng cổ điển Guyon?",
        f"1) <b>Giai đoạn sớm:</b> Thường diễn biến {Y('âm thầm không triệu chứng')}.<br>"
        f"2) <b>Phát hiện tình cờ:</b> Khoảng {G('50% RCC')} ngày nay được phát hiện tình cờ qua {G('siêu âm ổ bụng')}.<br>"
        f"3) <b>Tam chứng cổ điển Guyon:</b> Thường chỉ gặp ở {R('giai đoạn muộn')}, chiếm khoảng {Y('10 – 15%')} bệnh nhân.",
        f"Thận nằm sâu ở khoang sau phúc mạc được bao quanh bởi lớp mỡ dày, nên u nhỏ phát triển âm thầm không gây đau hay triệu chứng tiết niệu cho đến khi đạt kích thước lớn hoặc ăn thông vào đài bể thận. Phổ cập siêu âm giúp phát hiện sớm một nửa số ca trước khi xuất hiện đủ tam chứng muộn.",
        "B4.01", ["Lam-sang"],
    ),
    basic(
        "SURG56-B4-02", "B4", "Tam chứng Guyon (1): Đái máu đại thể", 1,
        f"{B('[Tam chứng Guyon — Triệu chứng 1]')} Trong Tam chứng cổ điển Guyon (Đái máu đại thể, Đau thắt lưng, Khối u vùng thắt lưng), triệu chứng nào thường gặp nhất và mang 5 tính chất đặc trưng gì?",
        f"1) <b>Thường gặp nhất:</b> {R('Đái máu đại thể')}.<br>"
        f"2) <b>5 tính chất đặc trưng:</b> Đái máu {R('tự nhiên')}, {R('toàn bãi')}, {R('đột ngột')}, {Y('không kèm đau buốt')}; nước tiểu đỏ tươi hoặc có máu cục ({B('khuôn niệu quản')}), có thể {Y('tự cầm rồi tái phát nhiều lần')}.",
        f"Khối u ăn mòn trực tiếp mạch máu tân tạo vào đài bể thận nên máu hòa đều vào toàn bộ nước tiểu ngay từ đầu đến cuối dòng ({R('toàn bãi')}), không kích thích bàng quang nên {Y('không đau buốt')}. Cục máu đông đọng dài theo lòng ống niệu quản tạo nên {B('máu cục khuôn niệu quản')}. Hiện tượng tự cầm là do cục máu bít tạm chỗ vỡ hoặc u hoại tử bong tróc theo từng đợt.",
        "B4.02", ["Lam-sang", "Tam-chung-Guyon"],
    ),
    basic(
        "SURG56-B4-03", "B4", "Tam chứng Guyon (2 & 3): Đau thắt lưng & Khối u thắt lưng", 1,
        f"{B('[Tam chứng Guyon — Triệu chứng 2 & 3]')} Phân tích 2 cơ chế gây Đau thắt lưng và các đặc điểm thăm khám Khối u vùng thắt lưng theo từng giai đoạn?",
        f"1) <b>Đau thắt lưng (2 kiểu đau):</b><br>"
        f"   • Đau {Y('âm ỉ thắt lưng')} do u to làm {B('căng bao thận')}.<br>"
        f"   • Hoặc {R('đau quặn thận dữ dội')} khi có {B('máu cục di chuyển làm tắc nghẽn niệu quản')}.<br>"
        f"2) <b>Khối u vùng thắt lưng:</b><br>"
        f"   • Sờ thấy khối u vùng hố thắt lưng: {B('chắc, gồ ghề, di động theo nhịp thở')}.<br>"
        f"   • Ở giai đoạn muộn: khối u {R('dính chặt không di động')}.",
        f"Khác với cơn đau quặn thận do sỏi thuần túy, trong RCC đau có thể âm ỉ kéo dài khi bao xơ thận bị căng giãn từ từ, nhưng bùng phát thành cơn đau quặn dữ dội mỗi khi mảnh u hoại tử hay máu cục trôi xuống nút tắc niệu quản. Khối u mất di động theo nhịp thở là dấu hiệu báo động đã xâm lấn dính cố định vào mô xung quanh.",
        "B4.03", ["Lam-sang", "Tam-chung-Guyon"],
    ),
    basic(
        "SURG56-B4-04", "B4", "Giãn tĩnh mạch thừng tinh & Hội chứng Wunderlich", 1,
        f"{B('[Triệu chứng đặc thù khác]')} Cơ chế giải phẫu bên trái vs bên phải và tính chất nằm ngửa của Giãn tĩnh mạch thừng tinh do RCC; Hội chứng Wunderlich là gì?",
        f"1) <b>Giãn tĩnh mạch thừng tinh cùng bên u:</b><br>"
        f"   • <b>Cơ chế theo bên:</b> Do khối u hoặc huyết khối chèn ép / xâm lấn {B('tĩnh mạch thận (bên trái)')} hoặc {B('tĩnh mạch chủ (bên phải)')}.<br>"
        f"   • <b>Dấu hiệu đặc hiệu:</b> {R('Nằm ngửa tĩnh mạch không xẹp')}.<br>"
        f"2) <b>Hội chứng Wunderlich:</b> Tình trạng {R('chảy máu sau phúc mạc dữ dội')} khi khối u hoại tử vỡ đột ngột.",
        f"Giải phẫu học cho thấy tĩnh mạch tinh hoàn trái đổ vuông góc vào tĩnh mạch thận trái, còn tĩnh mạch tinh hoàn phải đổ trực tiếp vào tĩnh mạch chủ dưới. Vì tắc nghẽn cơ học cố định bởi u/huyết khối chứ không phải suy van đơn thuần, nên khi bệnh nhân nằm ngửa trọng lực mất đi nhưng búi tĩnh mạch thừng tinh vẫn căng phồng không xẹp.",
        "B4.04", ["Lam-sang", "Co-do"],
    ),
    basic(
        "SURG56-B4-05", "B4", "Hội chứng cận ung thư RCC (6 nhóm biểu hiện)", 1,
        f"{B('[Hội chứng cận ung thư]')} Tỷ lệ gặp Hội chứng cận ung thư ở bệnh nhân RCC và cơ chế sinh học của từng biểu hiện toàn thân (ngoài Stauffer)?",
        f"1) <b>Tần suất xuất hiện:</b> Khoảng {Y('20 – 30%')} bệnh nhân ung thư thận (do tế bào u tiết chất có hoạt tính sinh học).<br>"
        f"2) <b>Sốt kéo dài không rõ nguyên nhân:</b> Chiếm {Y('20%')}.<br>"
        f"3) <b>Tăng huyết áp:</b> Do tăng tiết {B('Renin')} hoặc chèn ép động mạch thận.<br>"
        f"4) <b>Bất thường hồng cầu:</b> {B('Đa hồng cầu')} (tăng tiết {B('Erythropoietin')}) hoặc {Y('thiếu máu nhược sắc')}.<br>"
        f"5) <b>Tăng canxi máu:</b> Do tiết chất giống PTH ({B('PTHrP')}).<br>"
        f"6) <b>Toàn thân & Viêm:</b> Sút cân, mệt mỏi, suy mòn, {Y('tốc độ lắng máu tăng cao')}.",
        f"Thận vốn là cơ quan nội tiết tiết Renin và Erythropoietin tự nhiên, nên khi tế bào ống thận chuyển dạng ác tính, chúng tiết mất kiểm soát các hormon này cùng cytokine gây sốt và {B('PTHrP')} gây tăng canxi máu dù hoàn toàn chưa có di căn xương hay tuyến cận giáp.",
        "B4.05", ["Can-ung-thu", "Lam-sang"],
    ),
    basic(
        "SURG56-B4-06", "B4", "Hội chứng Stauffer", 1,
        f"{B('[Hội chứng Stauffer]')} Định nghĩa, 4 biểu hiện đặc trưng và diễn tiến tiên lượng sau mổ của Hội chứng Stauffer trong ung thư thận?",
        f"1) <b>Bản chất:</b> {B('Rối loạn chức năng gan KHÔNG do di căn')}.<br>"
        f"2) <b>4 biểu hiện đặc trưng:</b> {R('Gan to')}, {R('Phosphatase kiềm tăng')}, {R('men gan tăng')}, {R('chức năng đông máu kéo dài')}.<br>"
        f"3) <b>Diễn tiến sau phẫu thuật:</b> Các chỉ số gan này {G('trở về bình thường sau khi cắt bỏ thận có u')}.",
        f"Hội chứng Stauffer gây ra bởi các cytokine (như IL-6) do khối u thận giải phóng tác động độc lên tế bào gan từ xa mà không có bất kỳ nhân di căn nhu mô gan nào. Chính vì vậy, việc nhận diện đúng giúp tránh chẩn đoán nhầm giai đoạn M1 không mổ được — các chỉ số sẽ tự hồi phục sau cắt thận triệt căn.",
        "B4.05", ["Can-ung-thu", "Stauffer"],
    ),

    # =========================================================================
    # B5: CẬN LÂM SÀNG
    # =========================================================================
    basic(
        "SURG56-B5-01", "B5", "Siêu âm ổ bụng & Chụp niệu đồ tĩnh mạch (UIV)", 1,
        f"{B('[Cận lâm sàng — Siêu âm & UIV]')} Trình bày vai trò cùng các thông số khảo sát của Siêu âm ổ bụng và hình ảnh kinh điển của chụp niệu đồ tĩnh mạch (UIV) trong ung thư thận?",
        f"1) <b>Siêu âm ổ bụng:</b> Là {G('phương tiện sàng lọc ban đầu hàng đầu')} có độ tin cậy cao:<br>"
        f"   • Xác định vị trí, kích thước, cấu trúc âm ({B('u đặc hay u nang, bờ không đều, tăng âm hoặc hỗn hợp âm')}).<br>"
        f"   • Khảo sát {R('chồi u trong tĩnh mạch thận / tĩnh mạch chủ')}.<br>"
        f"2) <b>Chụp niệu đồ tĩnh mạch (UIV):</b><br>"
        f"   • Thấy hình ảnh đè đẩy, chèn ép làm biến dạng các đài bể thận (hình chèn ép, kéo dài, {Y('hình \"chân nhện\"')}).<br>"
        f"   • Hiện nay {Y('ít dùng')} do đã có CT Scanner.",
        f"Siêu âm vừa rẻ tiền, không xâm lấn vừa phát hiện tới nửa số ca RCC không triệu chứng hiện nay, đồng thời siêu âm Doppler có thể nhìn thấy sớm huyết khối u bò trong lòng tĩnh mạch thận. Dấu hiệu \"chân nhện\" trên UIV phản ánh các cổ đài thận bị khối u nhu mô đẩy giãn dài và uốn cong ôm lấy u.",
        "B5.01, B5.02", ["Can-lam-sang"],
    ),
    basic(
        "SURG56-B5-02", "B5", "CT Scanner có cản quang — Tiêu chuẩn vàng", 1,
        f"{B('[Cận lâm sàng — Tiêu chuẩn vàng]')} Phương tiện nào là tiêu chuẩn vàng chẩn đoán ung thư thận; mô tả đặc điểm ngấm/thải thuốc đặc hiệu và 4 thông số đánh giá lan tràn?",
        f"1) <b>Tiêu chuẩn vàng:</b> {G('Chụp cắt lớp vi tính (CT Scanner) có cản quang')}.<br>"
        f"2) <b>Động học thuốc cản quang:</b> Khối u đặc {R('ngấm thuốc cản quang mạnh và không đồng nhất ở thì động mạch')}, sau đó {Y('thải thuốc ở thì muộn')}.<br>"
        f"3) <b>4 thông số lan tràn đánh giá chính xác:</b><br>"
        f"   • Xâm lấn qua bao thận ra {B('lớp mỡ quanh thận')}.<br>"
        f"   • Xâm lấn {B('cân Gerota')}.<br>"
        f"   • {B('Di căn hạch')}.<br>"
        f"   • Phát hiện {R('chồi huyết khối trong tĩnh mạch thận và tĩnh mạch chủ dưới')}.",
        f"Do RCC tăng sinh mạch máu phong phú (đặc biệt thể tế bào sáng), khối u bắt thuốc cực nhanh và rực rỡ ở thì động mạch, xen kẽ vùng không ngấm thuốc tương ứng với các ổ hoại tử/chảy máu trung tâm, rồi rửa trôi nhanh ở thì tĩnh mạch – bài xuất.",
        "B5.03", ["Can-lam-sang", "Tieu-chuan-vang"],
    ),
    basic(
        "SURG56-B5-03", "B5", "Vai trò MRI & Chụp động mạch thận", 1,
        f"{B('[Cận lâm sàng — MRI & Chụp mạch]')} Khi nào chụp Cộng hưởng từ (MRI) và Chụp động mạch thận được chỉ định trong ung thư thận?",
        f"1) <b>Cộng hưởng từ (MRI):</b><br>"
        f"   • Rất có giá trị khi bệnh nhân {R('dị ứng thuốc cản quang')} hoặc {R('suy thận')}.<br>"
        f"   • Đặc biệt ưu thế đánh giá mức độ lan rộng của {R('chồi huyết khối trong lòng tĩnh mạch chủ dưới')} lên tới {B('cơ hoành hoặc tâm nhĩ phải')}.<br>"
        f"2) <b>Chụp động mạch thận:</b> Chỉ định khi u quá to dự kiến {G('cắt bán phần')}, hoặc chụp để {G('nút mạch (tắc mạch u trước mổ)')} nhằm {G('giảm lượng máu mất trong mổ')}.",
        f"MRI xác định ranh giới đầu trên của chồi huyết khối tĩnh mạch chủ dưới cực kỳ sắc nét trên mặt phẳng đứng dọc/đứng ngang mà không cần thuốc cản quang iod gây độc thận — thông tin sống còn để kíp mổ quyết định có cần phối hợp phẫu thuật tim – lồng ngực mở nhĩ phải hay chỉ mở tĩnh mạch chủ bụng.",
        "B5.04, B5.05", ["Can-lam-sang"],
    ),

    # =========================================================================
    # B6: CHẨN ĐOÁN PHÂN BIỆT
    # =========================================================================
    basic(
        "SURG56-B6-01", "B6", "U cơ mỡ mạch thận (Angiomyolipoma - AML)", 1,
        f"{B('[Chẩn đoán phân biệt]')} Bản chất mô học, đặc điểm dịch tễ gợi ý và dấu hiệu khẳng định trên CT của U cơ mỡ mạch thận (AML)?",
        f"1) <b>Bản chất lành tính:</b> Khối u lành tính ở thận cấu tạo từ 3 thành phần: {B('mỡ')}, {B('mạch máu')} và {B('cơ')}.<br>"
        f"2) <b>Bối cảnh lâm sàng gợi ý:</b> {Y('80% gặp ở nữ')}, thường đơn độc ở {Y('bên phải')}.<br>"
        f"3) <b>Hình ảnh khẳng định trên CT:</b> Thấy rõ thành phần {G('tỷ trọng mỡ âm tính (-20 đến -80 HU)')} trong khối u.",
        f"Điểm chốt phân biệt AML lành tính với RCC ác tính trên CT không nằm ở việc u có tăng sinh mạch hay không (cả hai đều nhiều mạch!), mà là sự hiện diện của {G('mỡ đại thể có tỷ trọng âm -20 đến -80 HU')}. Nhận diện chính xác giúp bảo tồn thận cho người bệnh.",
        "B6.01", ["Chan-doan-phan-biet"],
    ),
    basic(
        "SURG56-B6-02", "B6", "Phân biệt Nang thận đơn độc, Thận đa nang & U ngoài nhu mô", 1,
        f"{B('[Chẩn đoán phân biệt]')} Đặc điểm phân biệt RCC với Nang thận đơn độc lành tính, Bệnh thận đa nang và Khối u sau phúc mạc / u tuyến thượng thận?",
        f"1) <b>Nang thận đơn độc lành tính:</b> {Y('Không đái máu')}; siêu âm thành mỏng, dịch đồng nhất, tăng âm phía sau; CT {G('không ngấm thuốc cản quang')} (phân loại {B('Bosniak I–II')}).<br>"
        f"2) <b>Bệnh thận đa nang:</b> Thường tổn thương {B('cả 2 bên thận')}, kèm {B('đa nang gan')} và {R('suy thận tiến triển')}.<br>"
        f"3) <b>U sau phúc mạc hoặc u tuyến thượng thận:</b> Chụp {G('CT / MRI')} phân định rõ nguồn gốc khối u nằm {B('ngoài nhu mô thận')}.",
        f"Chìa khóa loại trừ nang thận đơn độc Bosniak I–II là tính chất dịch đồng nhất tăng âm sau trên siêu âm và {G('hoàn toàn không ngấm thuốc cản quang')} trên CT. Với khối u cực trên thận, cần dựng hình đa lát cắt CT/MRI để tránh nhầm u tuyến thượng thận đè đẩy cực trên thận thành RCC.",
        "B6.02, B6.03", ["Chan-doan-phan-biet"],
    ),

    # =========================================================================
    # B7: ĐIỀU TRỊ PHẪU THUẬT & ĐIỀU TRỊ TOÀN THÂN
    # =========================================================================
    basic(
        "SURG56-B7-01", "B7", "Phẫu thuật cắt thận triệt căn (Robson)", 1,
        f"{B('[Phẫu thuật triệt căn]')} Trình bày chỉ định, phạm vi mô cắt bỏ và nguyên tắc kiểm soát mạch máu – huyết khối tĩnh mạch chủ của Phẫu thuật cắt thận triệt căn (Robson)?",
        f"1) <b>Vai trò chung:</b> Phẫu thuật là phương pháp điều trị {G('cơ bản và hiệu quả nhất')} trong ung thư thận.<br>"
        f"2) <b>Đối tượng áp dụng Robson:</b> Giai đoạn {Y('I, II, III')} ({B('T2, T3')} hoặc {B('T1 không đủ điều kiện cắt bán phần')}).<br>"
        f"3) <b>Phạm vi cắt bỏ:</b> Toàn bộ thận + {B('lớp mỡ quanh thận nằm trong cân Gerota')} + {B('tuyến thượng thận cùng bên')} + {B('nạo vét hạch cuống thận dọc động mạch chủ / tĩnh mạch chủ')}.<br>"
        f"4) <b>Nguyên tắc thao tác & Xử lý huyết khối:</b> Bắt buộc {R('thắt động mạch và tĩnh mạch thận trước')} khi đụng chạm giải phóng khối u; nếu có huyết khối tĩnh mạch chủ thì phối hợp {R('mở tĩnh mạch chủ dưới lấy sạch huyết khối u')}.",
        f"Thao tác nắn bóp bóc tách thận có u trước khi thắt tĩnh mạch thận sẽ đẩy tế bào ung thư trôi thẳng vào tĩnh mạch chủ dưới gây thuyên tắc và di căn ồ ạt. Lấy bỏ trọn vẹn khối nằm trong bao {B('cân Gerota')} ngăn tái phát tại chỗ.",
        "B7.01", ["Dieu-tri", "Phau-thuat"],
    ),
    basic(
        "SURG56-B7-02", "B7", "Cắt thận bán phần (NSS) & Can thiệp tối thiểu (RFA/Cryo)", 1,
        f"{B('[Phẫu thuật bảo tồn & Xâm lấn tối thiểu]')} Chỉ định bắt buộc và tương đối của Phẫu thuật cắt thận bán phần (NSS) cũng như đối tượng áp dụng Đốt sóng cao tần (RFA) / Áp lạnh (Cryoablation)?",
        f"1) <b>Cắt thận bán phần / bảo tồn nhu mô (NSS):</b><br>"
        f"   • <b>Bắt buộc bảo tồn:</b> Khối u ở {R('thận duy nhất')}, ung thư {R('cả 2 bên thận')}, hoặc bệnh nhân {R('suy thận mãn tính')}.<br>"
        f"   • <b>Tương đối:</b> U thận giai đoạn sớm {G('T1a (kích thước ≤ 4 cm)')}, nằm ở vị trí {B('ngoại vi hoặc cực thận')}.<br>"
        f"2) <b>Đốt sóng cao tần (RFA) / Áp lạnh (Cryoablation):</b> Dành cho {Y('bệnh nhân già yếu')}, u nhỏ {Y('< 3 – 4 cm')} không thể chịu đựng cuộc mổ lớn.",
        f"Với u nhỏ ngoại vi ≤ 4 cm, kết quả kiểm soát ung thư của NSS tương đương cắt thận triệt căn nhưng bảo vệ tối đa đơn vị thận (nephron), giảm nguy cơ suy thận mạn và tử vong tim mạch về lâu dài. RFA/Cryoablation là cứu cánh ít xâm lấn khi bệnh nhân không đủ sức khỏe gây mê phẫu thuật lớn.",
        "B7.02, B7.03", ["Dieu-tri", "Bao-ton-than"],
    ),
    basic(
        "SURG56-B7-03", "B7", "Đề kháng hóa xạ & Liệu pháp nhắm trúng đích (TKI, mTOR)", 1,
        f"{B('[Điều trị toàn thân — Nhắm trúng đích]')} Đáp ứng của RCC với hóa trị/xạ trị truyền thống ra sao và kể tên 2 nhóm thuốc Liệu pháp nhắm trúng đích trong RCC di căn?",
        f"1) <b>Đặc tính đề kháng:</b> Ung thư tế bào thận {R('rất kháng với hóa trị và xạ trị truyền thống')}.<br>"
        f"2) <b>Thuốc ức chế tăng sinh mạch (TKI - Tyrosine Kinase Inhibitors):</b> {G('Sunitinib, Sorafenib, Pazopanib, Axitinib')}.<br>"
        f"3) <b>Thuốc ức chế mTOR:</b> {G('Everolimus, Temsirolimus')}.",
        f"Tế bào RCC biểu hiện mạnh protein kháng đa thuốc (P-glycoprotein) nên hầu như trơ với hóa chất độc tế bào kinh điển. Ngược lại, do con đường VHL–HIF kích hoạt quá mức VEGF tạo mạch máu tân tạo và trục tăng trưởng tế bào mTOR, các thuốc {B('TKI')} và {B('ức chế mTOR')} đánh trúng đích sinh học của khối u.",
        "B7.04", ["Dieu-tri", "Dich"],
    ),
    basic(
        "SURG56-B7-04", "B7", "Liệu pháp miễn dịch & Vai trò Xạ trị trong RCC", 1,
        f"{B('[Miễn dịch & Xạ trị giảm nhẹ]')} Liệt kê các thuốc Liệu pháp miễn dịch (cổ điển và hiện đại) cùng 2 chỉ định còn lại của Xạ trị trong ung thư thận di căn?",
        f"1) <b>Liệu pháp miễn dịch cổ điển:</b> {B('Interleukin-2 (IL-2 liều cao)')}, {B('Interferon-alpha')}.<br>"
        f"2) <b>Miễn dịch hiện đại (Checkpoint inhibitors):</b> {G('Nivolumab, Pembrolizumab, Ipilimumab')}.<br>"
        f"3) <b>Vai trò Xạ trị:</b> Chỉ dùng để {Y('xạ giảm đau trong di căn xương')} hoặc {Y('giảm áp lực trong di căn não')}.",
        f"RCC là một trong những khối u sinh miễn dịch mạnh nhất (từng ghi nhận hiếm hoi ca thoái lui tự phát nhờ đáp ứng miễn dịch), do đó tiến hóa từ cytokine độc tính cao (IL-2, IFN-α) sang thế hệ ức chế điểm kiểm soát miễn dịch ({G('PD-1 / CTLA-4')}) đã thay đổi ngoạn mục tiên lượng thể di căn.",
        "B7.05", ["Dieu-tri", "Mien-dich"],
    ),

    # =========================================================================
    # THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (4 THẺ >= 3)
    # =========================================================================
    algo(
        "SURG56-ALGO-01", "B5", "Chẩn đoán hình ảnh U thận", "Lựa chọn CĐHA từ Sàng lọc đến Tiền phẫu",
        f"1) <b>Bước 1 (Sàng lọc ban đầu):</b> {G('Siêu âm ổ bụng')} phát hiện u đặc/nang, bờ không đều, khảo sát sơ bộ chồi u tĩnh mạch.<br>"
        f"2) <b>Bước 2 (Tiêu chuẩn vàng):</b> {G('CT Scanner có cản quang')} nếu chức năng thận bình thường và không dị ứng thuốc → Đánh giá ngấm thuốc thì động mạch, thải thuốc thì muộn, cân Gerota, hạch, huyết khối TM thận/TMC dưới và phân biệt AML ({Y('-20 đến -80 HU')}).<br>"
        f"3) <b>Bước 3 (Thay thế / Đánh giá tim-hoành):</b> Chuyển sang {B('MRI')} khi {R('dị ứng thuốc cản quang')}, {R('suy thận')} hoặc cần xác định chồi huyết khối TMC dưới lan lên {R('cơ hoành / tâm nhĩ phải')}.<br>"
        f"4) <b>Bước 4 (Chuẩn bị mổ u rất to):</b> {B('Chụp động mạch thận')} khi dự kiến cắt bán phần hoặc {G('nút mạch trước mổ')} để giảm mất máu.",
        f"Lưu đồ hình ảnh học tuân theo bậc thang an toàn – chính xác: Siêu âm mở màn không tia xạ → CT cản quang làm xương sống chẩn đoán & TNM → MRI giải cứu bệnh nhân suy thận/dị ứng và định vị đỉnh huyết khối ngang tim → Chụp mạch máu phục vụ chiến thuật phẫu thuật mạch lớn.",
        "B5.01, B5.03, B5.04, B5.05, B6.01", ["Can-lam-sang"],
    ),
    algo(
        "SURG56-ALGO-02", "B7", "Xử trí U thận khu trú", "Phẫu thuật Bảo tồn vs Triệt căn vs Xâm lấn tối thiểu",
        f"1) <b>Nhóm BẮT BUỘC bảo tồn (NSS):</b> U ở {R('thận duy nhất')}, u {R('cả 2 bên thận')} hoặc {R('suy thận mãn tính')} → Bắt buộc {G('Cắt thận bán phần (NSS)')}.<br>"
        f"2) <b>U nhỏ ≤ 4 cm (T1a) trên BN đủ sức khỏe:</b> Nếu vị trí {B('ngoại vi hoặc cực thận')} → Chọn {G('Cắt thận bán phần (NSS)')}; nếu không đủ điều kiện bảo tồn → Chuyển {B('Cắt thận triệt căn Robson')}.<br>"
        f"3) <b>Bệnh nhân già yếu không mổ lớn được + u < 3–4 cm:</b> Chọn {Y('Đốt sóng cao tần (RFA)')} hoặc {Y('Áp lạnh (Cryoablation)')}.<br>"
        f"4) <b>Giai đoạn I–II–III (T2, T3):</b> {G('Phẫu thuật cắt thận triệt căn Robson')} (thận + mỡ quanh thận trong cân Gerota + thượng thận cùng bên + hạch cuống thận).",
        f"Triết lý ngoại khoa thận hiện đại đặt cân bằng giữa {G('triệt căn ung thư học')} và {B('bảo tồn dự trữ lọc cầu thận')}. Luôn ưu tiên NSS nếu kích thước ≤ 4 cm thuận lợi hoặc trong 3 tình huống bắt buộc không thể để mất hoàn toàn một bên thận.",
        "B7.01, B7.02, B7.03", ["Dieu-tri", "Phau-thuat"],
    ),
    algo(
        "SURG56-ALGO-03", "B7", "U thận có huyết khối TMC", "Quy trình mổ Robson khi nghi ngờ chồi u tĩnh mạch (T3b–T3c)",
        f"1) <b>Bước 1 (Định vị đỉnh huyết khối trước mổ):</b> Dùng {G('CT cản quang')} hoặc ưu thế nhất là {B('MRI')} để phân biệt lan tĩnh mạch thận ({Y('T3a')}), TMC dưới dưới cơ hoành ({Y('T3b')}) hay trên cơ hoành / tâm nhĩ phải ({R('T3c')}).<br>"
        f"2) <b>Bước 2 (Tiếp cận mạch máu ưu tiên):</b> Thực hiện nguyên tắc bất di bất dịch: {R('Thắt động mạch và tĩnh mạch thận TRƯỚC')} khi đụng chạm giải phóng khối u.<br>"
        f"3) <b>Bước 3 (Xử lý huyết khối TMC dưới):</b> Phối hợp {G('mở tĩnh mạch chủ dưới lấy sạch hoàn toàn huyết khối u')} cùng với cắt thận triệt căn khối Gerota.",
        f"Thắt động mạch thận sớm giúp khối u và chồi huyết khối xẹp bớt sung huyết, ngăn chặn chảy máu ồ ạt từ tĩnh mạch bàng hệ và loại bỏ nguy cơ bung trôi mảnh huyết khối gây thuyên tắc động mạch phổi tử vong ngay trên bàn mổ.",
        "B3.02, B5.04, B7.01", ["Phau-thuat", "TNM"],
    ),
    algo(
        "SURG56-ALGO-04", "B7", "Ung thư thận di căn (M1)", "Chiến lược điều trị Toàn thân & Xạ trị giảm nhẹ",
        f"1) <b>Loại trừ phác đồ sai:</b> {R('KHÔNG dùng hóa trị hay xạ trị truyền thống')} vì RCC đề kháng rất mạnh.<br>"
        f"2) <b>Nhắm trúng đích (Targeted Therapy):</b> Chọn {G('TKI (Sunitinib, Sorafenib, Pazopanib, Axitinib)')} hoặc {G('ức chế mTOR (Everolimus, Temsirolimus)')}.<br>"
        f"3) <b>Liệu pháp miễn dịch:</b> Dùng {G('Checkpoint inhibitors (Nivolumab, Pembrolizumab, Ipilimumab)')} (thế hệ mới) hoặc {B('IL-2 liều cao / Interferon-alpha')} (cổ điển).<br>"
        f"4) <b>Xạ trị chọn lọc khi có biến chứng đích:</b> Chỉ dùng để {Y('xạ giảm đau trong di căn xương')} hoặc {Y('giảm áp lực trong di căn não')}.",
        f"Hiểu rõ cơ chế đề kháng hóa trị giúp bác sĩ chuyển thẳng bệnh nhân sang vũ khí trúng đích mạch máu/mTOR và ức chế điểm kiểm soát miễn dịch thay vì lãng phí thời gian độc tính hóa chất. Xạ trị chỉ giữ vai trò điều trị triệu chứng tại xương (30–40%) và não.",
        "B3.03, B7.04, B7.05", ["Dieu-tri", "Di-can"],
    ),

    # =========================================================================
    # BẪY LÂM SÀNG & CỜ ĐỎ CẤP CỨU (9 THẺ >= 8)
    # =========================================================================
    redflag(
        "SURG56-TRAP-01", "B4", "Chờ đợi đủ Tam chứng Guyon",
        f"Bệnh nhân có khối u thận phát hiện trên siêu âm hoặc đái máu đơn độc — Tại sao tuyệt đối không được chờ đủ cả 3 triệu chứng của Tam chứng Guyon mới chẩn đoán RCC?",
        f"1) <b>Thực tế tỷ lệ:</b> Tam chứng cổ điển Guyon (đái máu đại thể + đau thắt lưng + sờ thấy khối u) thường chỉ gặp ở {R('giai đoạn muộn')} với tỷ lệ chỉ {Y('10 – 15%')}.<br>"
        f"2) <b>Xu hướng chẩn đoán sớm:</b> Khoảng {G('50% RCC')} hiện nay biểu hiện âm thầm và được phát hiện {G('tình cờ qua siêu âm ổ bụng')}.",
        f"Đợi đến khi khối u sờ thấy gồ ghề ở thắt lưng kèm đau và đái máu là lúc bệnh nhân đã bỏ lỡ cửa sổ T1a phẫu thuật bảo tồn thận, thậm chí khối u đã dính cố định hoặc di căn phổi, xương.",
        "B4.01", ["Lam-sang", "Tam-chung-Guyon"],
    ),
    trap(
        "SURG56-TRAP-02", "B4", "Chủ quan khi đái máu tự cầm",
        f"Bệnh nhân đái máu đỏ tươi toàn bãi đột ngột không đau buốt, sau đó tự hết nước tiểu trong lại hoàn toàn — Bẫy lâm sàng chết người nào dễ xảy ra?",
        f"1) <b>Bản chất triệu chứng:</b> Đái máu đại thể trong RCC có đặc điểm {R('tự nhiên, toàn bãi, không đau buốt')} và {R('có thể tự cầm rồi tái phát nhiều lần')}.<br>"
        f"2) <b>Hành động bắt buộc:</b> Không được kết luận khỏi bệnh khi nước tiểu tự trong; bắt buộc làm {G('siêu âm và CT hệ tiết niệu')} tầm soát khối u thận (và bàng quang).",
        f"Hiện tượng đái máu không đau buốt tự cầm dễ khiến người bệnh và thầy thuốc chủ quan nghĩ do sỏi nhỏ hoặc viêm nhẹ đã qua. Trong ung thư thận, đợt chảy máu ngưng lại chỉ là tạm thời trước khi khối u lại hoại tử vỡ mạch đợt tiếp theo.",
        "B4.02", ["Lam-sang"],
    ),
    trap(
        "SURG56-TRAP-03", "B4", "Giãn tĩnh mạch thừng tinh nằm ngửa không xẹp",
        f"Nam giới trên 40 tuổi mới xuất hiện giãn tĩnh mạch thừng tinh (đặc biệt bên phải hoặc nặng lên nhanh) và khi nằm ngửa không xẹp — Sai lầm gì cần tránh?",
        f"1) <b>Cảnh báo bẫy:</b> Tuyệt đối không chẩn đoán sơ sài là giãn tĩnh mạch thừng tinh nguyên phát lành tính.<br>"
        f"2) <b>Vị trí chèn ép theo bên:</b> Dấu hiệu {R('nằm ngửa tĩnh mạch không xẹp')} chứng tỏ tĩnh mạch bị {R('khối u hoặc huyết khối chèn ép/xâm lấn')} vào {B('tĩnh mạch thận (bên trái)')} hoặc {B('tĩnh mạch chủ (bên phải)')}.",
        f"Giãn tĩnh mạch thừng tinh thông thường ở người trẻ xẹp rõ khi nằm ngửa do giảm áp lực thủy tĩnh. Khi búi tĩnh mạch vẫn căng cứng ở tư thế nằm trên người lớn tuổi, đó là dấu chỉ điểm tắc nghẽn dòng về ở sau phúc mạc do RCC tiến triển.",
        "B4.04, B0.03", ["Lam-sang"],
    ),
    redflag(
        "SURG56-TRAP-04", "B4", "Hội chứng Wunderlich vỡ u sau phúc mạc",
        f"Bệnh nhân đột ngột đau hố thắt lưng dữ dội kèm tụt huyết áp, sốc mất máu cấp mà không có chấn thương — Cấp cứu nào đang đe dọa tính mạng ở người có u thận?",
        f"1) <b>Tên hội chứng cấp cứu:</b> {R('Hội chứng Wunderlich')} — {R('chảy máu sau phúc mạc dữ dội')} do khối u thận hoại tử {R('vỡ đột ngột')}.<br>"
        f"2) <b>Bản chất nền:</b> Khối u thận giàu mạch máu tân tạo kèm ổ hoại tử và xuất huyết bên trong.",
        f"Vỡ tự phát khoang sau phúc mạc gây mất máu khối lượng lớn rất nhanh vào khoang sau phúc mạc (thậm chí không thấy bầm máu ngoài da ngay lúc đầu). Hồi sức tích cực, CT cấp cứu và nút mạch/phẫu thuật cầm máu là cứu cánh duy nhất.",
        "B4.04, B2.01", ["Cap-cuu", "Lam-sang"],
    ),
    trap(
        "SURG56-TRAP-05", "B4", "Nhầm Hội chứng Stauffer với Di căn gan",
        f"Bệnh nhân u thận có gan to, men gan tăng, Phosphatase kiềm tăng, đông máu kéo dài hoặc sốt kéo dài 20% — Bẫy tiên lượng sai lầm nào khiến bệnh nhân mất cơ hội phẫu thuật?",
        f"1) <b>Cạm bẫy:</b> Vội kết luận khối u thận đã {R('di căn gan (M1)')} không còn khả năng mổ triệt căn hoặc chỉ tập trung tìm ổ nhiễm trùng khi sốt kéo dài.<br>"
        f"2) <b>Thực chất:</b> Đây là {B('Hội chứng cận ung thư (Stauffer)')} — {G('rối loạn chức năng gan KHÔNG do di căn')}; toàn bộ chỉ số gan sẽ {G('trở về bình thường sau khi cắt bỏ thận có u')}.",
        f"Chụp CT/MRI gan không thấy nhân di căn kết hợp bộ men gan và phosphatase kiềm tăng cao là manh mối vàng của hội chứng Stauffer. Cắt thận có u giải quyết được nguyên nhân tiết cytokine gây ứ mật/viêm gan phản ứng này.",
        "B4.05", ["Can-ung-thu", "Stauffer"],
    ),
    trap(
        "SURG56-TRAP-06", "B5", "Chụp CT cản quang khi suy thận / dị ứng / u lên tâm nhĩ",
        f"Bệnh nhân nghi ngờ ung thư thận có suy thận hoặc dị ứng thuốc cản quang, hoặc nghi huyết khối tĩnh mạch chủ dưới lan cao — Sai lầm trong chỉ định CĐHA là gì?",
        f"1) <b>Tránh lạm dụng sai đối tượng:</b> Không cố tiêm thuốc cản quang chụp CT trên bệnh nhân {R('dị ứng thuốc cản quang')} hoặc {R('suy thận')}.<br>"
        f"2) <b>Lựa chọn chuẩn:</b> Chuyển sang {G('Chụp cộng hưởng từ (MRI)')} — đồng thời MRI {G('ưu thế vượt trội')} đánh giá độ lan của {B('chồi huyết khối trong lòng tĩnh mạch chủ dưới lên cơ hoành hoặc tâm nhĩ phải')}.",
        f"Thuốc cản quang iod có thể làm suy sụp chức năng thận nền hoặc gây sốc phản vệ. Hơn nữa, MRI khắc họa dòng chảy và ranh giới đỉnh cục huyết khối u sát buồng tim chính xác hơn, quyết định đường mổ bụng đơn thuần hay phối hợp ngực.",
        "B5.03, B5.04", ["Can-lam-sang"],
    ),
    trap(
        "SURG56-TRAP-07", "B6", "Chẩn đoán nhầm U cơ mỡ mạch thận (AML) thành RCC",
        f"Nữ giới có khối u thận đơn độc bên phải, siêu âm tăng âm — Làm thế nào tránh sai lầm cắt bỏ oan một bên thận lành tính?",
        f"1) <b>Thực thể cần loại trừ:</b> Kiểm tra kỹ {B('U cơ mỡ mạch thận (AML)')} gồm mỡ, mạch máu và cơ ({Y('80% ở nữ, đơn độc bên phải')}).<br>"
        f"2) <b>Chốt chặn CT Scanner:</b> Tìm thành phần {G('tỷ trọng mỡ âm tính (-20 đến -80 HU)')} trong khối u — nếu có mỡ âm tính, đây là {G('u lành tính AML')}, không phải RCC.",
        f"Cả AML và RCC đều có thể tăng âm trên siêu âm và giàu mạch máu khi bơm thuốc cản quang. Điểm phân biệt quyết định nằm ở việc đo trị số Hounsfield tìm vùng {G('tỷ trọng mỡ âm tính (-20 đến -80 HU)')} trên phim CT không thuốc/có thuốc.",
        "B6.01", ["Chan-doan-phan-biet"],
    ),
    redflag(
        "SURG56-TRAP-08", "B7", "Bóc tách giải phóng u trước khi thắt cuống mạch",
        f"Trong phẫu thuật cắt thận triệt căn Robson, phẫu thuật viên nắn bóp bóc tách giải phóng khối u thận cho di động rồi mới thắt động – tĩnh mạch thận — Hậu quả chết người là gì?",
        f"1) <b>Nguy cơ tai biến tức thì:</b> Làm {R('phát tán tế bào ung thư vào hệ tuần hoàn')} (và có thể gây bung chồi huyết khối tĩnh mạch chủ dưới).<br>"
        f"2) <b>Nguyên tắc vàng bất di bất dịch:</b> Phải {G('thắt động mạch và tĩnh mạch thận TRƯỚC')} khi đụng chạm giải phóng khối u.",
        f"Tĩnh mạch thận có khẩu kính lớn và lưu lượng máu qua thận cực cao (khoảng 20% cung lượng tim). Mọi thao tác chạm bóp vào khối u khi đường thoát tĩnh mạch còn mở sẽ bơm trực tiếp tế bào ung thư về tĩnh mạch chủ và lên phổi.",
        "B7.01", ["Phau-thuat", "Co-do"],
    ),
    trap(
        "SURG56-TRAP-09", "B7", "Dùng hóa xạ trị truyền thống làm phác đồ nền RCC di căn",
        f"Bệnh nhân ung thư biểu mô tế bào thận giai đoạn di căn phổi, xương được đề xuất truyền hóa chất toàn thân hoặc xạ trị khối u thận — Sai lầm nằm ở đâu?",
        f"1) <b>Sai lầm kinh điển:</b> Ung thư tế bào thận {R('rất kháng với hóa trị và xạ trị truyền thống')}.<br>"
        f"2) <b>Hướng toàn thân hiệu quả:</b> Toàn thân phải dùng {G('nhắm trúng đích (TKI, ức chế mTOR)')} và {G('liệu pháp miễn dịch (Checkpoint inhibitors / IL-2, IFN-α)')}; {Y('xạ trị')} chỉ dùng để {Y('giảm đau di căn xương')} hoặc {Y('giảm áp lực di căn não')}.",
        f"Sử dụng hóa trị truyền thống cho RCC không chỉ thất bại trong kiểm soát khối u mà còn làm người bệnh kiệt quệ vì độc tính tủy xương/niêm mạc. Xạ trị chỉ có giá trị triệu chứng khu trú tại xương và não.",
        "B7.04, B7.05", ["Dieu-tri"],
    ),
]
