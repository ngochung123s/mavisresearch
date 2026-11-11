# -*- coding: utf-8 -*-
"""
Dữ liệu thẻ Anki chuẩn hóa cho bài SURG-23: Ung Thư Trực Tràng
Rebuild 100% từ barem: SURG-23_Ung_thu_truc_trang_BAREM.md
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
    b_tag = f"Ngoai::SURG-23::{section}"
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
    b_tag = f"Ngoai::SURG-23::{section}"
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
        "SURG23-B0-01", "B0", "Dịch tễ học toàn cầu UTTT 2018", 1,
        f"{B('[Dịch tễ toàn cầu 2018]')} Số ca mắc mới, tử vong, thứ hạng giới tính và phân bố địa lý của Ung thư trực tràng?",
        f"1) <b>Gánh nặng toàn cầu:</b> Khoảng {Y('704.376 ca mới mắc (3,9%)')}, đứng hàng thứ {Y('8')}; khoảng {R('310.394 ca tử vong (3,2%)')}, đứng hàng thứ {R('9')}.<br>"
        f"2) <b>Xếp hạng nam vs nữ:</b> Phổ biến thứ {Y('4 ở nam giới')} và thứ {Y('3 ở nữ giới')}.<br>"
        f"3) <b>Phân bố địa lý:</b> Cao nhất tại {G('Úc, New Zealand, Châu Âu, Bắc Mỹ')}; thấp nhất tại {G('Châu Phi và Nam – Trung Á')}.",
        "UTTT là ung thư phổ biến hàng đầu vùng tiểu khung, đặc biệt liên quan mật thiết tới lối sống công nghiệp hóa phương Tây.",
        "B0.01, B0.02", ["Dich-te", "Toan-cau", "Dia-ly"],
    ),
    basic(
        "SURG23-B0-02", "B0", "Sàng lọc, lý do phát hiện muộn & Hướng dẫn NCCN", 1,
        f"{B('[Sàng lọc & NCCN]')} Phương pháp sàng lọc phát hiện sớm UTTT, nguyên nhân hay phát hiện muộn, 3 mô thức theo NCCN và tỷ lệ sống 5 năm?",
        f"1) <b>Sàng lọc trọng tâm:</b> Dựa vào khám sàng lọc, quản lý nhóm nguy cơ cao bằng {G('thăm trực tràng bằng tay')}.<br>"
        f"2) <b>Lý do hay phát hiện muộn:</b> Thường nhầm lẫn với các bệnh lý lành tính vùng hậu môn – trực tràng như {R('trĩ, kiết lỵ, nứt kẽ hậu môn')}.<br>"
        f"3) <b>Ba mô thức NCCN &amp; Sống 5 năm:</b> Phối hợp {G('Phẫu thuật + Hóa chất + Tia xạ')}; phát hiện sớm và điều trị triệt để cho tỷ lệ sống trên 5 năm đạt {G('60% – 90%')}.",
        "Đừng bao giờ điều trị bệnh trĩ hay kiết lỵ kéo dài ở người trên 40 tuổi mà chưa đưa ngón tay vào thăm khám trực tràng.",
        "B0.03, B0.04", ["Sang-loc", "NCCN", "Chan-doan-nham", "Song-5-nam"],
    ),

    # =========================================================================
    # B1: GIẢI PHẪU VÀ SINH LÝ TRỰC TRÀNG
    # =========================================================================
    basic(
        "SURG23-B1-01", "B1", "Phân đoạn giải phẫu 3 phần trực tràng", 1,
        f"{B('[Giải phẫu trực tràng ~15 cm]')} Cách chia 3 phân đoạn Ung thư trực tràng (cao / giữa / thấp) tính từ rìa hậu môn theo Hội Phẫu thuật viên Đại trực tràng Hoa Kỳ?",
        f"1) <b>UTTT 1/3 trên (UTTT cao):</b> Bờ dưới u cách rìa hậu môn {G('11 – 15 cm')}. Đoạn này phần lớn {Y('có phúc mạc che phủ mặt trước và hai bên')}.<br>"
        f"2) <b>UTTT 1/3 giữa (UTTT giữa):</b> Bờ dưới u cách rìa hậu môn {Y('6 – 10 cm')}.<br>"
        f"3) <b>UTTT 1/3 dưới (UTTT thấp):</b> Bờ dưới u cách rìa hậu môn {R('< 6 cm')}.",
        "Vị trí 1/3 trên, giữa hay dưới tính theo khoảng cách bờ dưới khối u tới rìa hậu môn là mốc giải phẫu quyết định chỉ định xạ trị tiền phẫu và phẫu thuật bảo tồn cơ thắt.",
        "B1.01", ["Giai-phau", "Phan-doan", "Ria-hau-mon"],
    ),
    basic(
        "SURG23-B1-02", "B1", "Sinh lý trực tràng và Cơ chế đại tiện", 2,
        f"{B('[Sinh lý trực tràng]')} Vai trò chứa đựng và 4 thành phần phối hợp tạo nên phản xạ đại tiện tự chủ của con người?",
        f"1) <b>Chức năng chứa đựng:</b> Trực tràng chứa phân trước khi tống xuất ra ngoài.<br>"
        f"2) <b>Hoạt động phối hợp đại tiện:</b> Gồm {Y('phản xạ thần kinh tủy sống – vỏ não')}, {Y('nhu động co bóp bóng trực tràng')}, sự giãn mở của {G('cơ thắt trong (cơ trơn tự chủ)')} và {G('cơ thắt ngoài (cơ vân theo ý muốn)')}.",
        "Bảo tồn tối thiểu cơ thắt ngoài và dây thần kinh tự động vùng chậu trong mổ TME giúp giữ được chức năng tự chủ đại tiện sau phẫu thuật.",
        "B1.02", ["Sinh-ly", "Dai-tien", "Co-that-trong", "Co-that-ngoai"],
    ),

    # =========================================================================
    # B2: NGUYÊN NHÂN, POLYP & YẾU TỐ DI TRUYỀN
    # =========================================================================
    basic(
        "SURG23-B2-01", "B2", "Chế độ ăn uống & Hóa chất sinh ung thư", 2,
        f"{B('[Dinh dưỡng & Chất sinh ung]')} Các yếu tố thực phẩm, vitamin/khoáng chất thiếu hụt và nhóm hóa chất gây ung thư trực tràng?",
        f"1) <b>Thói quen ăn uống nguy cơ:</b> Nhiều mỡ động vật, nhiều đạm, đường tinh chế, {R('ít chất xơ và rau xanh')}.<br>"
        f"2) <b>Thiếu hụt vi chất bảo vệ:</b> Thiếu các {Y('vitamin A, B, C, E')} và {Y('thiếu canxi')}.<br>"
        f"3) <b>Hóa chất sinh ung từ thực phẩm:</b> Thực phẩm chế biến sẵn hoặc nướng cháy nhiễm {R('nitrosamine')} và {R('hydrocarbon thơm đa vòng')}.",
        "Chế độ ăn giàu chất xơ giúp pha loãng các chất sinh ung trong lòng ruột và rút ngắn thời gian tiếp xúc với niêm mạc trực tràng.",
        "B2.01", ["Dinh-duong", "Nitrosamine", "Vitamin", "Chat-xo"],
    ),
    basic(
        "SURG23-B2-02", "B2", "Polyp tăng sản vs Polyp tuyến (nguy cơ ác tính)", 1,
        f"{B('[Polyp đại trực tràng]')} So sánh tỷ lệ, hình thái và nguy cơ ác tính giữa {G('Polyp tăng sản')} và 3 nhóm {R('Polyp tuyến (đặc biệt tuyến nhung mao)')}?",
        f"1) <b>Polyp tăng sản (Hyperplastic polyp):</b> Chiếm {G('90%')} tổng số polyp, kích thước < 5 mm, {G('không có nguy cơ chuyển dạng ác tính')}.<br>"
        f"2) <b>Polyp tuyến (Adenomatous polyp - 10%):</b> Chia làm 3 dưới nhóm là {Y('tuyến ống (tubular)')}, {Y('tuyến nhung mao (villous)')} và {Y('tuyến ống – nhung mao')}.<br>"
        f"3) <b>Polyp tuyến nhung mao:</b> Tập trung chủ yếu ở {R('trực tràng')}, thường {Y('không có cuống')}, mang nguy cơ ác tính cao nhất (khi kích thước > 2 cm tỷ lệ hóa ác lên tới {R('40% – 50%')}).",
        "Polyp nhung mao trực tràng kích thước > 2 cm bắt buộc phải đánh giá sâu chân polyp bằng siêu âm nội soi trước khi cắt qua niêm mạc.",
        "B2.02", ["Polyp-nhung-mao", "Polyp-tang-san", "Polyp-tuyen", "Ac-tinh"],
    ),
    basic(
        "SURG23-B2-03", "B2", "Các hội chứng di truyền: FAP và Hội chứng Lynch", 1,
        f"{B('[Di truyền học UTTT]')} Biến thể lâm sàng, đột biến gen và vị trí nhiễm sắc thể của {R('FAP')} và {Y('Hội chứng Lynch (HNPCC)')}?",
        f"1) <b>Bệnh đa polyp tuyến gia đình (FAP):</b> Bao gồm các biến thể {Y('Gardner và Turcot')}; do đột biến {R('gen APC trên nhiễm sắc thể 5q21')}.<br>"
        f"2) <b>Hội chứng Lynch (HNPCC):</b> Ung thư đại trực tràng di truyền không đa polyp, do đột biến nhóm gen {G('sửa chữa sai lệch DNA (mismatch repair)')}.",
        "Hội chứng Gardner (FAP + u xương, u mô mềm) và hội chứng Turcot (FAP + u não) là hai biến thể ngoài đường tiêu hóa kinh điển của đột biến APC 5q21.",
        "B2.03", ["FAP", "Gardner", "Turcot", "5q21", "Lynch", "MMR"],
    ),

    # =========================================================================
    # B3: GIẢI PHẪU BỆNH VÀ HƯỚNG LAN TRÀN
    # =========================================================================
    basic(
        "SURG23-B3-01", "B3", "Mô bệnh học WHO 2000 và Độ biệt hóa Morson 1976", 1,
        f"{B('[Giải phẫu bệnh vi thể]')} Tỷ lệ các thể mô bệnh học theo WHO 2000 và 3 mức độ biệt hóa mô học theo Morson (1976)?",
        f"1) <b>Hệ thống WHO 2000:</b> {G('98% là Ung thư biểu mô tuyến (Adenocarcinoma)')} (tuyến ống, tuyến nhú, tuyến nhầy, tế bào nhẫn). Các thể hiếm gặp: U tế bào vảy, {Y('u Carcinoid thần kinh nội tiết (0,4%)')}, {Y('lymphoma (1,3%)')}, {Y('sarcoma mô liên kết (0,3%)')}.<br>"
        f"2) <b>Độ biệt hóa Morson (1976):</b> Biệt hóa cao {G('20%')}, Biệt hóa vừa {Y('60%')}, Biệt hóa kém {R('20%')}.",
        "Thể tế bào nhẫn và độ biệt hóa kém (20%) có tiên lượng xấu, dễ xâm lấn sâu và di căn hạch bạch huyết sớm.",
        "B3.01, B3.02", ["WHO-2000", "Adenocarcinoma", "Morson-1976", "Biet-hoa"],
    ),
    basic(
        "SURG23-B3-02", "B3", "Hướng xâm lấn tại chỗ và Đường di căn hạch / máu", 1,
        f"{B('[Hướng phát triển và lan tràn]')} Ba hướng xâm lấn tại chỗ, hai hướng di căn hạch bạch huyết và con đường di căn máu đến {R('Gan')} vs {Y('Phổi, Xương, Não')}?",
        f"1) <b>Xâm lấn tại chỗ:</b> Phía sau dính {Y('cân trước xương cùng, xương cùng cụt')}; phía trước nữ lan {Y('vách âm đạo, cổ tử cung')}, nam lan {Y('túi tinh, tuyến tiền liệt, bàng quang')}; phía dưới xâm lấn {R('cơ thắt hậu môn')} (quyết định bảo tồn cơ thắt).<br>"
        f"2) <b>Đường bạch huyết:</b> Theo mạch mạc treo trực tràng về {G('hạch cuống mạc treo tràng dưới (MTTT)')}; riêng UTTT thấp còn di căn sang hai bên theo {R('bó mạch chậu trong (khoang chậu hông)')}.<br>"
        f"3) <b>Đường máu:</b> TM trực tràng trên đổ về {R('hệ TM cửa → di căn gan (30% – 50%)')}; TM trực tràng giữa &amp; dưới đổ về {Y('TM chủ bụng → di căn phổi, xương, não')}.",
        "Sự dẫn lưu tĩnh mạch kép của trực tràng giải thích vì sao UTTT thấp có thể di căn thẳng lên phổi qua TM chủ mà không cần qua gan.",
        "B3.03, B3.04", ["Xam-lan", "Di-can-hach", "Di-can-mau", "Mach-chau-trong", "Gan-phoi"],
    ),

    # =========================================================================
    # B4: TRIỆU CHỨNG LÂM SÀNG VÀ CẬN LÂM SÀNG
    # =========================================================================
    basic(
        "SURG23-B4-01", "B4", "Triệu chứng cơ năng Ung thư trực tràng", 1,
        f"{B('[Lâm sàng: Triệu chứng cơ năng]')} Đặc điểm {R('Đại tiện ra máu (60,4%)')}, rối loạn đại tiện và tính chất đau vùng hạ vị – tầng sinh môn?",
        f"1) <b>Đại tiện ra máu (60,4%):</b> Triệu chứng thường gặp và xuất hiện sớm nhất; máu {R('đỏ tươi hoặc lờ lờ máu cá lẫn chất nhầy')}, đi nhiều lần/ngày, hay chẩn đoán nhầm bệnh trĩ hoặc kiết lỵ.<br>"
        f"2) <b>Rối loạn đại tiện:</b> {Y('Mót rặn thường xuyên')}, cảm giác đi ngoài không hết phân (tenesmus), biến đổi khuôn phân ({Y('phân dẹt hoặc có rãnh')}).<br>"
        f"3) <b>Đau hạ vị &amp; tầng sinh môn:</b> Đau tức nặng, buốt rát lan {R('ra sau lưng hoặc xuống đùi')} khi khối u xâm lấn {R('đám rối thần kinh cùng cụt')}.",
        "Hội chứng giả lỵ (mót rặn + đi nhiều lần + nhầy máu cá) kéo dài trên 2 tuần ở người lớn tuổi là chỉ định nội soi trực tràng khẩn.",
        "B4.01, B4.02", ["Dai-tien-ra-mau", "Mot-ran", "Phan-det", "Hoi-chung-gia-ly"],
    ),
    basic(
        "SURG23-B4-02", "B4", "Thăm trực tràng bằng tay (DRE - Digital Rectal Examination)", 1,
        f"{B('[Lâm sàng: Thăm trực tràng DRE]')} Tỷ lệ phát hiện bệnh của thăm trực tràng bằng tay và {G('5 thông số')} lâm sàng cần xác định?",
        f"1) <b>Giá trị chẩn đoán:</b> Là phương pháp kinh điển, đơn giản nhưng cho phép chẩn đoán xác định tới {G('70% trường hợp')} UTTT.<br>"
        f"2) <b>Hình thái u &amp; Vị trí thành:</b> Sờ thấy u sùi hoặc loét bờ cứng; xác định vị trí ở {Y('thành trước, thành sau hay thành bên')}.<br>"
        f"3) <b>Khoảng cách rìa hậu môn:</b> Đo bờ dưới khối u cách rìa hậu môn {G('bao nhiêu cm')} (quyết định khả năng giữ cơ thắt).<br>"
        f"4) <b>Độ di động &amp; Dính máu:</b> Đánh giá u còn {Y('di động hay đã dính cố định')} vào xung quanh; rút ngón tay kiểm tra {R('găng dính máu theo tay')}.",
        "Khoảng cách bờ dưới khối u tới rìa hậu môn đo bằng ngón tay khi DRE là thông số đầu tiên phẫu thuật viên dùng để dự kiến phương pháp mổ.",
        "B4.03", ["DRE", "Tham-truc-trang", "70-phan-tram", "Gang-dinh-mau"],
    ),
    basic(
        "SURG23-B4-03", "B4", "Nội soi trực tràng ống mềm & Siêu âm nội soi (ERUS)", 1,
        f"{B('[Cận lâm sàng: Nội soi & ERUS]')} Nhiệm vụ bắt buộc khi nội soi ống mềm và thế mạnh chuyên biệt của {Y('Siêu âm qua nội soi trực tràng (ERUS)')}?",
        f"1) <b>Nội soi trực tràng / đại trực tràng ống mềm:</b> Quan sát trực tiếp tổn thương, xác định vị trí u so với đường lược và rìa hậu môn; {R('bắt buộc bấm sinh thiết làm giải phẫu bệnh')}.<br>"
        f"2) <b>Siêu âm qua nội soi trực tràng (ERUS):</b> Đánh giá cực kỳ chính xác độ sâu xâm lấn từng lớp thành trực tràng (phân biệt rõ {G('T1, T2, T3')}) và đánh giá tình trạng xâm lấn {Y('cơ thắt hậu môn')}.",
        "ERUS vượt trội hơn MRI trong việc phân tách ranh giới giữa lớp dưới niêm mạc (T1) và lớp cơ (T2) cho các khối u giai đoạn rất sớm.",
        "B4.04, B4.05", ["Noi-soi", "Sinh-thiet", "ERUS", "T1-T2-T3"],
    ),
    basic(
        "SURG23-B4-04", "B4", "Chụp MRI tiểu khung, CT ngực - bụng / PET-CT & CEA", 1,
        f"{B('[Cận lâm sàng: MRI tiểu khung, CT & CEA]')} Tại sao MRI tiểu khung là {G('tiêu chuẩn vàng')} tiền phẫu, vai trò của CT/PET-CT và giá trị của xét nghiệm CEA?",
        f"1) <b>Chụp cộng hưởng từ (MRI) tiểu khung:</b> Là {G('tiêu chuẩn vàng hiện nay')} đánh giá giai đoạn tại chỗ (T), tình trạng xâm lấn {R('diện cắt vòng quanh (CRM)')} và hệ hạch mạc treo trực tràng.<br>"
        f"2) <b>CT Scanner ngực – bụng &amp; PET-CT:</b> Đánh giá toàn thân phát hiện {Y('di căn gan, phổi, phúc mạc')}.<br>"
        f"3) <b>Chất chỉ điểm khối u CEA:</b> Nồng độ CEA tăng cao trước mổ có giá trị lớn để {G('theo dõi tái phát sau phẫu thuật')}.",
        "Sau khi cắt triệt căn, CEA sẽ trở về bình thường sau 4–6 tuần; nếu CEA tăng vọt trở lại trong các lần tái khám là báo hiệu tái phát hoặc di căn.",
        "B4.05, B4.06", ["MRI-tieu-khung", "CRM", "CT-PET", "CEA"],
    ),

    # =========================================================================
    # B5: PHÂN LOẠI GIAI ĐOẠN TNM (AJCC 2017)
    # =========================================================================
    basic(
        "SURG23-B5-01", "B5", "Phân loại T - Khối u nguyên phát (AJCC 2017)", 1,
        f"{B('[Phân loại AJCC 2017: Khối u T]')} Tiêu chuẩn giải phẫu phân chia 6 mức độ {G('Tis')}, {G('T1')}, {Y('T2')}, {Y('T3')}, {R('T4a')} và {R('T4b')}?",
        f"1) <b>Tis:</b> Ung thư tại chỗ, khu trú hoàn toàn ở lớp niêm mạc chưa qua màng đáy.<br>"
        f"2) <b>T1 &amp; T2:</b> {G('T1')}: xâm lấn tới lớp dưới niêm mạc; {Y('T2')}: xâm lấn tới lớp cơ thành trực tràng.<br>"
        f"3) <b>T3:</b> Khối u xâm lấn xuyên qua lớp cơ tới {Y('mô mỡ mạc treo trực tràng')}.<br>"
        f"4) <b>T4a &amp; T4b:</b> {R('T4a')}: xâm lấn thủng lớp phúc mạc tạng; {R('T4b')}: xâm lấn trực tiếp vào {R('tạng lân cận')} (tuyến tiền liệt, âm đạo, bàng quang, xương cùng).",
        "Mốc T3 (ra ngoài thành cơ tới mô mỡ mạc treo) là ngưỡng bắt đầu phải cân nhắc hóa - xạ trị tiền phẫu.",
        "B5.01", ["TNM", "AJCC-2017", "Tis-T4b"],
    ),
    basic(
        "SURG23-B5-02", "B5", "Phân loại N - Hạch vùng và M - Di căn xa (AJCC 2017)", 1,
        f"{B('[Phân loại AJCC 2017: Hạch N & Di căn M]')} Số lượng hạch di căn của {G('N0, N1a, N1b, N2')} và phân nhóm di căn xa {R('M1a, M1b, M1c')}?",
        f"1) <b>Hạch vùng (N):</b> {G('N0')}: chưa di căn hạch; {Y('N1')}: di căn 1–3 hạch (trong đó {Y('N1a')}: 1 hạch, {Y('N1b')}: 2–3 hạch); {R('N2')}: di căn từ {R('4 hạch vùng trở lên')}.<br>"
        f"2) <b>Di căn xa (M):</b> {G('M0')}: chưa di căn xa; {R('M1a')}: di căn 1 tạng; {R('M1b')}: di căn nhiều tạng; {R('M1c')}: di căn phúc mạc.",
        "Di căn phúc mạc được tách riêng thành M1c trong AJCC 2017 do có tiên lượng nặng nhất trong nhóm bệnh di căn xa.",
        "B5.02", ["TNM", "AJCC-2017", "N0-N2", "M1a-M1c"],
    ),

    # =========================================================================
    # B6: NGUYÊN TẮC PHẪU THUẬT & PHÂN LOẠI RULLIER (2013)
    # =========================================================================
    basic(
        "SURG23-B6-01", "B6", "Nguyên tắc R0, CRM và Phẫu thuật TME (Heald 1982)", 1,
        f"{B('[Nguyên tắc Ngoại khoa: R0, CRM & TME]')} Ngưỡng an toàn diện cắt dọc, diện cắt vòng quanh (CRM) và ý nghĩa của kỹ thuật {G('TME (Heald 1982)')}?",
        f"1) <b>Nguyên tắc diện cắt R0:</b> Diện cắt dọc cách bờ dưới u ít nhất {G('1 – 2 cm')}; diện cắt vòng quanh ({Y('CRM âm tính > 1 mm')}).<br>"
        f"2) <b>Cắt toàn bộ mạc treo trực tràng (TME - Heald 1982):</b> Tiêu chuẩn vàng cho UTTT 1/3 giữa &amp; dưới; phẫu tích sắc bén trong {G('mặt phẳng thần thánh (holy plane)')}, giữ nguyên bao mạc treo không rách.<br>"
        f"3) <b>Hiệu quả sống còn của TME:</b> Giúp giảm ngoạn mục tỷ lệ tái phát tại chỗ từ {R('30% – 50%')} xuống chỉ còn dưới {G('5% – 8%')}.",
        "Đừng bao giờ xé rách bao mạc treo trực tràng khi phẫu tích trong tiểu khung; rách bao đồng nghĩa để sót tế bào ung thư gây tái phát vùng chậu.",
        "B6.01, B6.02", ["TME", "Heald-1982", "CRM", "Holy-plane", "R0"],
    ),
    basic(
        "SURG23-B6-02", "B6", "Phân loại phẫu thuật UTTT thấp theo Rullier (2013)", 1,
        f"{B('[Phân loại Rullier 2013]')} Phân chia {G('Type I')}, {Y('Type II')}, {Y('Type III')} và {R('Type IV')} dựa trên mối liên hệ giữa u với ống hậu môn / cơ thắt và phương pháp mổ tương ứng?",
        f"1) <b>Type I (cách ống hậu môn > 1 cm):</b> Phẫu thuật bảo tồn cơ thắt, {G('cắt trước rất thấp (ultra-LAR)')} nối trực tràng – ống hậu môn (CAA).<br>"
        f"2) <b>Type II (cách ống hậu môn < 1 cm, chưa xâm lấn cơ thắt trong):</b> Cắt một phần cơ thắt trong ({Y('Partial ISR')}) bảo tồn cơ thắt ngoài.<br>"
        f"3) <b>Type III (xâm lấn vào cơ thắt trong):</b> Cắt toàn bộ cơ thắt trong ({Y('Total ISR')}), nối đại tràng với mép hậu môn.<br>"
        f"4) <b>Type IV (xâm lấn cơ thắt ngoài hoặc cơ nâng hậu môn):</b> Không thể bảo tồn cơ thắt → Bắt buộc {R('phẫu thuật cắt cụt trực tràng (Phẫu thuật Miles)')}.",
        "Rullier đã mở rộng cơ hội giữ lại hậu môn tự nhiên cho nhiều bệnh nhân UTTT thấp nhờ kỹ thuật cắt gian cơ thắt (ISR).",
        "B6.03, B6.04", ["Rullier-2013", "Ultra-LAR", "Partial-ISR", "Total-ISR", "Miles"],
    ),

    # =========================================================================
    # B7: CÁC PHƯƠNG PHÁP MỔ CỤ THỂ & ĐIỀU TRỊ ĐA MÔ THỨC
    # =========================================================================
    basic(
        "SURG23-B7-01", "B7", "Phẫu thuật Miles (APR) và Cắt trước thấp (LAR)", 1,
        f"{B('[Phẫu thuật triệt căn: Miles vs LAR]')} Phạm vi áp dụng và thao tác kỹ thuật cốt lõi phân biệt giữa {R('Phẫu thuật Miles (APR)')} và {G('Cắt trước thấp (LAR)')}?",
        f"1) <b>Phẫu thuật Miles (APR):</b> Áp dụng cho UTTT 1/3 dưới xâm lấn cơ thắt ngoài (Rullier Type IV), u sát rìa hậu môn ({R('< 3 – 4 cm')}) không bảo tồn được hoặc người già mất tự chủ. Thao tác: Cắt bỏ toàn bộ trực tràng + cơ thắt + ống hậu môn, đóng kín tầng sinh môn, làm {R('hậu môn nhân tạo vĩnh viễn ở hố chậu trái')}.<br>"
        f"2) <b>Phẫu thuật cắt trước thấp (LAR):</b> Áp dụng cho UTTT 1/3 giữa và 1/3 trên (cách rìa hậu môn {G('> 5 – 6 cm')}). Thao tác: Cắt ĐT xích ma + trực tràng kèm TME, nối đại tràng xuống với mỏm trực tràng thấp bằng {G('máy khâu nối tròn (Stapler)')}.",
        "Điểm khác biệt sống còn: LAR bảo tồn được bộ máy cơ thắt để đi ngoài qua đường dưới, trong khi Miles phải mang hậu môn nhân tạo vĩnh viễn suốt đời.",
        "B7.01, B7.02", ["Phau-thuat-Miles", "APR", "LAR", "Stapler", "HMNT-vinh-vien"],
    ),
    basic(
        "SURG23-B7-02", "B7", "Cắt u cục bộ (TEM/TAMIS) và Phẫu thuật Hartmann", 1,
        f"{B('[Phẫu thuật chọn lọc & Cấp cứu]')} Điều kiện khắt khe để cắt u qua đường hậu môn ({G('TEM / TAMIS')}) và tình huống áp dụng {Y('Phẫu thuật Hartmann')}?",
        f"1) <b>Cắt u cục bộ qua hậu môn (TEM / TAMIS):</b> Áp dụng cho khối u giai đoạn rất sớm {G('T1N0M0')}, mô học {G('biệt hóa cao')}, kích thước nhỏ {G('< 3 cm')} và chiếm {G('< 30% chu vi')} lòng ruột.<br>"
        f"2) <b>Phẫu thuật Hartmann:</b> Cắt đoạn trực tràng mang khối u, {Y('khâu đóng kín mỏm trực tràng dưới')}, đưa đầu đại tràng trên ra làm hậu môn nhân tạo. Áp dụng trong {R('cấp cứu thủng u, tắc ruột hoặc bệnh nhân quá già yếu')}.",
        "Cắt u tại chỗ TEM/TAMIS không nạo được hạch mạc treo nên chỉ an toàn khi xác định chắc chắn qua ERUS/MRI là T1N0 và biệt hóa cao.",
        "B7.03", ["TEM", "TAMIS", "Hartmann", "T1N0M0", "Cap-cuu"],
    ),
    basic(
        "SURG23-B7-03", "B7", "Xạ trị & Hóa – xạ trị đồng thời tiền phẫu", 1,
        f"{B('[Điều trị đa mô thức: Tiền phẫu]')} Nhóm giai đoạn nào bắt buộc hóa – xạ trị tiền phẫu, hai phác đồ xạ chuẩn và 3 lợi ích mang lại cho cuộc mổ?",
        f"1) <b>Nhóm giai đoạn áp dụng:</b> Giai đoạn tiến triển tại chỗ ({R('T3, T4 hoặc N+')}).<br>"
        f"2) <b>Hai phác đồ chuẩn mực:</b> Xạ trị dài ngày ({Y('50,4 Gy kết hợp Capecitabine / 5-FU')}) hoặc xạ trị ngắn ngày ({Y('5 × 5 Gy')}).<br>"
        f"3) <b>Ba tác dụng đột phá:</b> Hạ giai đoạn khối u ({G('downstaging')}), tăng tỷ lệ cắt triệt căn sạch tế bào u ({G('R0')}) và nâng cao cơ hội {G('phẫu thuật bảo tồn cơ thắt')}.",
        "Hóa xạ trị tiền phẫu giúp thu nhỏ khối u trước khi dao kéo đụng vào, giảm hẳn độc tính ruột non và giảm nguy cơ reo rắc tế bào ung thư.",
        "B7.04", ["Xa-tri-tien-phau", "50.4-Gy", "Downstaging", "R0"],
    ),
    basic(
        "SURG23-B7-04", "B7", "Hóa chất bổ trợ sau mổ và Thuốc điều trị đích", 1,
        f"{B('[Điều trị đa mô thức: Bổ trợ & Đích]')} Phác đồ và thời gian hóa chất bổ trợ sau mổ cùng vai trò 2 nhóm thuốc sinh học điều trị đích?",
        f"1) <b>Hóa chất bổ trợ sau mổ:</b> Phác đồ {G('FOLFOX hoặc CAPOX')} duy trì đủ {Y('6 tháng')} cho bệnh nhân có hạch dương tính (N+) hoặc yếu tố nguy cơ cao.<br>"
        f"2) <b>Thuốc điều trị đích kháng EGFR:</b> Dùng {G('Cetuximab hoặc Panitumumab')} (chỉ định khi xét nghiệm có {Y('gen KRAS hoang dại / wild-type')}).<br>"
        f"3) <b>Thuốc điều trị đích kháng sinh mạch:</b> Dùng {G('Bevacizumab')} (ức chế tăng sinh mạch máu nuôi khối u).",
        "Phải kiểm tra tình trạng đột biến gen KRAS/NRAS trước khi kê Cetuximab hay Panitumumab vì bệnh nhân mang đột biến sẽ kháng thuốc hoàn toàn.",
        "B7.05", ["FOLFOX", "CAPOX", "Cetuximab", "Panitumumab", "Bevacizumab", "KRAS"],
    ),

    # =========================================================================
    # BẪY THI & CỜ ĐỎ LÂM SÀNG (TRAPS & RED FLAGS)
    # =========================================================================
    trap(
        "SURG23-TRAP-01", "B0", "Bẫy chẩn đoán nhầm với Trĩ và Kiết lỵ",
        f"Bệnh nhân 52 tuổi đi ngoài máu đỏ tươi 3 tháng, tự mua thuốc trĩ và thuốc lỵ uống không đỡ. Sai lầm lâm sàng nghiêm trọng nhất của thầy thuốc tuyến dưới là gì?",
        f"1) <b>Sai lầm chết người:</b> Nhìn thấy búi trĩ sa hoặc nhầy máu mũi vội kết luận bệnh trĩ / kiết lỵ mà {R('không thăm trực tràng bằng tay (DRE)')} và nội soi.<br>"
        f"2) <b>Sự thật lâm sàng:</b> {Y('Đại tiện ra máu (60,4%)')} kèm mót rặn là biểu hiện kinh điển sớm nhất của UTTT; DRE đơn thuần đã phát hiện tới {G('70%')} ca bệnh.<br>"
        f"3) <b>Thái độ chuẩn mực:</b> Mọi trường hợp đi máu tươi hoặc thay đổi khuôn phân kéo dài trên người trưởng thành đều phải {G('thăm trực tràng + nội soi ống mềm')}.",
        "Một câu kinh điển ngoại khoa: 'Không đút ngón tay vào hậu môn khi khám bệnh thì có ngày phải đặt chính ngón tay vào miệng hối hận'.",
        "B0.03, B4.01, B4.03", ["Bay-tri", "Kiet-ly", "DRE", "Chan-doan-muon"],
    ),
    trap(
        "SURG23-TRAP-02", "B2", "Bẫy phân biệt Polyp tăng sản vs Polyp tuyến nhung mao",
        f"Cùng phát hiện polyp ở trực tràng qua nội soi, tại sao {G('Polyp tăng sản')} an toàn còn {R('Polyp nhung mao > 2 cm')} lại là bom nổ chậm?",
        f"1) <b>Polyp tăng sản (Hyperplastic):</b> Chiếm 90%, kích thước nhỏ < 5 mm, {G('hoàn toàn không có nguy cơ chuyển dạng ác tính')}.<br>"
        f"2) <b>Polyp nhung mao (Villous):</b> Hay tập trung ở trực tràng, thường không có cuống, xác suất hóa ác cực cao: khi kích thước > 2 cm tỷ lệ ung thư hóa đạt tới {R('40% – 50%')}.<br>"
        f"3) <b>Thái độ xử lý:</b> Tuyệt đối không bỏ qua polyp không cuống trực tràng; bắt buộc sinh thiết sâu vùng đáy hoặc cắt trọn dưới niêm mạc.",
        "Polyp không cuống hình nhung mao kích thước > 2 cm ở trực tràng có gần 50% khả năng đã chứa ổ ung thư xâm nhập bên dưới.",
        "B2.02", ["Polyp-nhung-mao", "Polyp-tang-san", "Ac-tinh"],
    ),
    trap(
        "SURG23-TRAP-03", "B3", "Bẫy giải phẫu đường di căn máu: Gan vs Phổi",
        f"Tại sao một bệnh nhân Ung thư trực tràng 1/3 dưới có thể xuất hiện nốt di căn {R('phổi')} sớm mà lá {G('gan')} hoàn toàn bình thường?",
        f"1) <b>Phân luồng tĩnh mạch trực tràng trên:</b> Đổ về tĩnh mạch mạc treo tràng dưới → Hệ tĩnh mạch cửa → Dẫn lưu qua gan gây {G('di căn gan (30% – 50%)')}.<br>"
        f"2) <b>Phân luồng tĩnh mạch trực tràng giữa &amp; dưới:</b> Đổ qua tĩnh mạch chậu trong vào thẳng {R('tĩnh mạch chủ dưới')} → Bỏ qua màng lọc gan, tiến thẳng lên tim phải gây {R('di căn phổi, xương, não')}.",
        "Khối u càng nằm thấp ở 1/3 dưới trực tràng thì nguy cơ di căn phổi đơn độc qua đường tĩnh mạch chủ càng cao.",
        "B3.04", ["Di-can-phoi", "Tinh-mach-cua", "Tinh-mach-chu", "Giai-phau-mach"],
    ),
    trap(
        "SURG23-TRAP-04", "B6", "Bẫy phẫu tích sai mặt phẳng TME (Holy plane)",
        f"Hậu quả thảm khốc nào xảy ra nếu phẫu thuật viên cắt trực tràng làm rách bao mạc treo trực tràng hoặc phá vỡ {R('diện cắt vòng quanh CRM')}?",
        f"1) <b>Nếu rách bao mạc treo trực tràng:</b> Các ổ tế bào ung thư và hạch vi thể bên trong mạc treo bị rơi vãi ra khoang tiểu khung → Đẩy tỷ lệ tái phát tại chỗ vùng chậu lên tới {R('30% – 50%')} (trong khi chuẩn TME giữ nguyên bao giảm xuống < 5–8%).<br>"
        f"2) <b>Nếu CRM dương tính (≤ 1 mm):</b> Tiên lượng tái phát cực nhanh và tử vong cao; vì vậy bắt buộc phải chụp {G('MRI tiểu khung')} đánh giá CRM trước mổ để cân nhắc {Y('hóa xạ tiền phẫu')}.",
        "Diện cắt CRM dương tính (≤ 1 mm) là thất bại phẫu thuật nặng nề nhất của ngoại khoa ung thư trực tràng.",
        "B4.05, B6.01, B6.02", ["TME", "CRM", "Tai-phat-tai-cho", "Holy-plane"],
    ),
    trap(
        "SURG23-TRAP-05", "B6", "Bẫy chỉ định bảo tồn cơ thắt ở Rullier Type IV",
        f"Bệnh nhân UTTT 1/3 dưới khẩn thiết xin bác sĩ giữ lại hậu môn thật, nhưng MRI tiểu khung cho thấy u đã {R('xâm lấn cơ thắt ngoài')}. Quyết định cố giữ cơ thắt là sai lầm vì sao?",
        f"1) <b>Bản chất Rullier Type IV:</b> Khối u đã xâm lấn vào cơ thắt ngoài hoặc cơ nâng hậu môn.<br>"
        f"2) <b>Hiểm họa nếu cố nối giữ hậu môn:</b> Không thể đạt diện cắt sạch ung thư R0 (diện cắt dọc tối thiểu 1–2 cm), chắc chắn gây tái phát tại chỗ thảm khốc vùng tầng sinh môn.<br>"
        f"3) <b>Quyết định chuẩn xác:</b> Bắt buộc thực hiện {R('Phẫu thuật Miles (APR)')} cắt cụt toàn bộ trực tràng và ống hậu môn, làm hậu môn nhân tạo vĩnh viễn ở hố chậu trái.",
        "Nguyên tắc tối thượng của phẫu thuật ung thư: Tính mạng và cắt sạch R0 luôn đặt trên mong muốn thẩm mỹ hay bảo tồn cơ thắt.",
        "B6.04, B7.01", ["Rullier-IV", "Phau-thuat-Miles", "Co-that-ngoai", "R0"],
    ),
    redflag(
        "SURG23-TRAP-06", "B4", "Cờ đỏ lâm sàng: UTTT xâm lấn Đám rối thần kinh cùng cụt",
        f"Triệu chứng đau đặc hiệu nào báo động khối ung thư trực tràng đã xâm lấn ra thành sau và {R('đám rối thần kinh cùng cụt')}?",
        f"1) <b>Cảm giác đau điển hình:</b> Đau tức nặng, buốt rát dữ dội liên tục vùng {R('hạ vị và tầng sinh môn')}.<br>"
        f"2) <b>Hướng lan đặc trưng:</b> Cơn đau lan xuyên ra {R('phía sau lưng (vùng xương cùng cụt)')} hoặc chạy dọc xuống {R('mặt sau đùi')}.<br>"
        f"3) <b>Ý nghĩa tiên lượng:</b> Cảnh báo u đã chuyển sang giai đoạn tiến triển xâm lấn tại chỗ sâu ({R('T4b')} dính cố định vào xương cùng), mất khả năng cắt bỏ ngay mà cần đánh giá MRI và hóa xạ tiền phẫu.",
        "Đau buốt tầng sinh môn lan xuống đùi ở bệnh nhân UTTT là cờ đỏ báo hiệu u cố định xâm lấn đám rối thần kinh chậu.",
        "B4.02, B5.01", ["Co-do", "Dam-roi-cung-cut", "T4b", "Dau-tang-sinh-mon"],
    ),

    # =========================================================================
    # THUẬT TOÁN QUYẾT ĐỊNH (ALGORITHM CARDS)
    # =========================================================================
    algo(
        "SURG23-ALGO-01", "B4", "Chẩn đoán & Phân giai đoạn", "Quy trình Chẩn đoán xác định và Đánh giá giai đoạn UTTT",
        f"1) <b>Bước 1 — Sàng lọc lâm sàng:</b> Bệnh nhân đi ngoài máu đỏ tươi / mót rặn / phân dẹt → Thực hiện ngay {G('Thăm trực tràng bằng tay (DRE)')} (phát hiện 70% trường hợp, đo khoảng cách bờ dưới u đến rìa hậu môn).<br>"
        f"2) <b>Bước 2 — Xác định mô học:</b> {G('Nội soi đại trực tràng ống mềm + Bấm sinh thiết')} làm giải phẫu bệnh (98% Adenocarcinoma).<br>"
        f"3) <b>Bước 3 — Đánh giá tại chỗ T, N, CRM:</b> Chụp {Y('MRI tiểu khung')} (tiêu chuẩn vàng đánh giá T, CRM, hạch mạc treo) phối hợp {Y('ERUS')} (chi tiết T1–T3 và cơ thắt).<br>"
        f"4) <b>Bước 4 — Đánh giá di căn xa M &amp; Theo dõi:</b> Chụp {B('CT ngực – bụng hoặc PET-CT')} tìm di căn gan/phổi + Định lượng {B('CEA')} nền trước mổ.",
        "MRI tiểu khung + Nội soi sinh thiết + CT ngực bụng là bộ ba chẩn đoán tiền phẫu bắt buộc trước khi quyết định xạ trị hay mổ thẳng.",
        "B4.01, B4.03, B4.04, B4.05, B4.06", ["Thuat-toan", "Chan-doan", "MRI", "DRE", "ERUS"],
    ),
    algo(
        "SURG23-ALGO-02", "B6", "Phẫu thuật UTTT Thấp", "Thuật toán lựa chọn phương pháp mổ theo Phân loại Rullier (2013)",
        f"1) <b>Type I (Bờ dưới u cách ống hậu môn > 1 cm):</b><br>"
        f"   → Bảo tồn toàn bộ cơ thắt: Thực hiện {G('Cắt trước rất thấp (ultra-LAR)')} và nối trực tràng – ống hậu môn (CAA).<br>"
        f"2) <b>Type II (Cách ống hậu môn < 1 cm, CHƯA xâm lấn cơ thắt trong):</b><br>"
        f"   → Bảo tồn cơ thắt ngoài: Thực hiện {Y('Cắt một phần cơ thắt trong (Partial ISR)')}.<br>"
        f"3) <b>Type III (Đã xâm lấn VÀO cơ thắt trong):</b><br>"
        f"   → Nối mép hậu môn: Thực hiện {Y('Cắt toàn bộ cơ thắt trong (Total ISR)')} + nối đại tràng với mép hậu môn.<br>"
        f"4) <b>Type IV (Xâm lấn cơ thắt ngoài hoặc cơ nâng hậu môn):</b><br>"
        f"   → Không thể bảo tồn cơ thắt: Bắt buộc {R('Phẫu thuật Miles (APR)')} cắt cụt trực tràng, làm HMNT vĩnh viễn hố chậu trái.",
        "Phân loại Rullier giúp chuẩn hóa ranh giới giữa phẫu thuật bảo tồn cơ thắt (ISR/ultra-LAR) và phẫu thuật Miles.",
        "B6.03, B6.04, B7.01", ["Thuat-toan", "Rullier", "Ultra-LAR", "ISR", "Miles"],
    ),
    algo(
        "SURG23-ALGO-03", "B7", "Chiến lược Đa mô thức", "Thuật toán Phối hợp Hóa - Xạ trị & Phẫu thuật theo TNM (AJCC 2017)",
        f"1) <b>Nhánh 1 — U rất sớm T1 N0 M0 (< 3 cm, < 30% chu vi, biệt hóa cao):</b><br>"
        f"   → Cân nhắc {G('Cắt u cục bộ qua đường hậu môn (TEM / TAMIS)')}.<br>"
        f"2) <b>Nhánh 2 — Giai đoạn sớm T1-T2 N0 M0 (không phù hợp TEM):</b><br>"
        f"   → Phẫu thuật triệt căn ngay ({G('LAR')} nếu cách rìa > 5–6 cm; {Y('ultra-LAR/ISR/Miles')} nếu 1/3 dưới) tuân thủ cắt {G('TME')}.<br>"
        f"3) <b>Nhánh 3 — Giai đoạn tiến triển tại chỗ (T3, T4 hoặc N+):</b><br>"
        f"   → Bước 1: {Y('Hóa – xạ trị đồng thời tiền phẫu')} (50,4 Gy + Capecitabine/5-FU hoặc 5 × 5 Gy) để giảm giai đoạn downstaging.<br>"
        f"   → Bước 2: Phẫu thuật triệt căn chuẩn {G('TME')} bảo đảm {G('R0 / CRM > 1 mm')}.<br>"
        f"   → Bước 3: {G('Hóa chất bổ trợ sau mổ 6 tháng (FOLFOX / CAPOX)')}.<br>"
        f"4) <b>Nhánh 4 — Bệnh di căn xa (M1) hoặc Tắc/Thủng cấp cứu:</b><br>"
        f"   → Cấp cứu / suy kiệt: {R('Phẫu thuật Hartmann')}; điều trị toàn thân kết hợp thuốc đích ({G('Cetuximab/Panitumumab')} nếu KRAS hoang dại; {G('Bevacizumab')}).",
        "Chiến lược chuẩn NCCN đặt hóa xạ trị tiền phẫu làm nền tảng cho mọi ca UTTT T3-T4 hoặc hạch dương tính nhằm giảm tối đa tái phát.",
        "B0.04, B7.01, B7.02, B7.03, B7.04, B7.05", ["Thuat-toan", "Da-mo-thuc", "TME", "Hoa-xa-tien-phau", "NCCN"],
    ),

    # =========================================================================
    # THẺ CLOZE (HIGH YIELD NUMBERS & BAREM GỐC)
    # =========================================================================
    cloze(
        "SURG23-B1-03", "B1", "Phân chia 3 đoạn giải phẫu trực tràng",
        f"Trực tràng dài khoảng 15 cm tính từ rìa hậu môn: Ung thư 1/3 trên (UTTT cao) cách rìa {clz(1, G('11 – 15 cm'))}; Ung thư 1/3 giữa cách rìa {clz(2, Y('6 – 10 cm'))}; Ung thư 1/3 dưới (UTTT thấp) cách rìa {clz(3, R('< 6 cm'))}.",
        "B1.01", ["Giai-phau", "Phan-doan", "Cloze"],
    ),
    cloze(
        "SURG23-B3-03", "B3", "Mô bệnh học WHO 2000 & Biệt hóa Morson 1976",
        f"Theo phân loại WHO 2000, {clz(1, G('98%'))} ung thư trực tràng là ung thư biểu mô tuyến (Adenocarcinoma); nhóm hiếm gặp gồm u Carcinoid ({clz(2, Y('0,4%'))}), lymphoma ({clz(3, Y('1,3%'))}) và sarcoma ({clz(4, Y('0,3%'))}). Phân độ Morson (1976): biệt hóa cao {clz(5, G('20%'))}, biệt hóa vừa {clz(6, Y('60%'))}, biệt hóa kém {clz(7, R('20%'))}.",
        "B3.01, B3.02", ["WHO-2000", "Morson-1976", "Cloze"],
    ),
    cloze(
        "SURG23-B6-05", "B6", "Tiêu chuẩn R0, CRM và Hiệu quả phẫu thuật TME",
        f"Phẫu thuật UTTT phải đạt diện cắt dọc cách bờ dưới u tối thiểu {clz(1, G('1 – 2 cm'))} và diện cắt vòng quanh CRM âm tính {clz(2, Y('> 1 mm'))}. Kỹ thuật cắt toàn bộ mạc treo trực tràng TME (Heald 1982) đi trong 'mặt phẳng thần thánh' giúp giảm tỷ lệ tái phát tại chỗ từ {clz(3, R('30% – 50%'))} xuống dưới {clz(4, G('5% – 8%'))}.",
        "B6.01, B6.02", ["TME", "CRM", "Heald-1982", "Cloze"],
    ),
    cloze(
        "SURG23-B7-06", "B7", "Phác đồ xạ trị tiền phẫu và hóa chất bổ trợ",
        f"Hóa – xạ đồng thời tiền phẫu UTTT (T3, T4 hoặc N+) dùng phác đồ xạ dài ngày {clz(1, Y('50,4 Gy'))} kèm {clz(2, Y('Capecitabine / 5-FU'))}, hoặc xạ ngắn ngày {clz(3, Y('5 × 5 Gy'))}. Sau mổ duy trì hóa chất bổ trợ {clz(4, G('FOLFOX hoặc CAPOX'))} trong thời gian {clz(5, G('6 tháng'))}.",
        "B7.04, B7.05", ["Xa-tri", "50.4-Gy", "FOLFOX", "CAPOX", "Cloze"],
    ),
]
