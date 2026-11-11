# -*- coding: utf-8 -*-
"""surgr3_cards_data.py — SURG-R3: Hồi Sức Suy Tuần Hoàn Trong Ngoại Khoa (100% barem 09).
Cấu trúc chuẩn LIGHT_CSS (Dual-mode Light/Dark), 4 màu PALETTE (#ff6b6b, #ffd43b, #51cf66, #74c0fc),
mặt sau 🎯 + 💡, 4 thẻ ⚡ THUẬT TOÁN QUYẾT ĐỊNH, 8 thẻ ❌/🛑 Bẫy & Cờ đỏ, 3 Cloze, phủ 23/23 mã barem.
"""

def _c(hex_color, text):
    return f'<span style="color: {hex_color}; font-weight: 600;">{text}</span>'

def R(t): return _c("#ff6b6b", t)   # Đỏ cảnh báo / ngưỡng bệnh lý / cấp cứu
def Y(t): return _c("#ffd43b", t)   # Vàng lưu ý / ranh giới / theo dõi
def G(t): return _c("#51cf66", t)   # Xanh lá chuẩn bình thường / đích đạt / lựa chọn ưu tiên
def B(t): return _c("#74c0fc", t)   # Xanh dương khái niệm / cơ chế / phân loại

def clz(n, t):
    return f"{{{{c{n}::{t}}}}}"

def basic(cid, section, topic, tier, front, core, ai, barem, tags, red_flag=False):
    badge = "🔴 CỜ ĐỎ" if red_flag else ""
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "category": f"SURG-R3 · {section}",
        "badge": badge,
        "badge_class": "badge-red" if red_flag else "",
        "front": front,
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R3", section] + tags,
    }

def algo(cid, section, topic, tier, front, core, ai, barem, tags):
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "category": f"SURG-R3 · {section}",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-amber",
        "front": f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {B(topic)}<br>{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R3", section, "Thuat-toan"] + tags,
    }

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False):
    prefix = f"{R('🛑 CỜ ĐỎ')} — " if red_flag else f"{Y('❌ Bẫy lâm sàng')} — "
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": 1,
        "category": f"SURG-R3 · {section}",
        "badge": "🛑 CỜ ĐỎ" if red_flag else "❌ Bẫy lâm sàng",
        "badge_class": "badge-red" if red_flag else "badge-amber",
        "front": f"{prefix}{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R3", section, "Bay-lam-sang"] + tags,
    }

def redflag(cid, section, topic, front, core, ai, barem, tags):
    return trap(cid, section, topic, front, core, ai, barem, tags, red_flag=True)

def cloze(cid, section, topic, text, barem, tags):
    return {
        "id": cid,
        "type": "cloze",
        "section": section,
        "topic": topic,
        "tier": 1,
        "category": f"SURG-R3 · {section}",
        "badge": "Cloze",
        "badge_class": "badge-blue",
        "text": text,
        "extra": f"[{barem}]",
        "tags": ["SURG-R3", section, "Cloze"] + tags,
    }


cards_data = [
    # =========================================================================
    # B0 — TỔNG QUAN & MỤC TIÊU HỌC TẬP
    # =========================================================================
    basic(
        "SURGR3-B0-01", "B0", "3 mục tiêu thực hành hồi sức suy tuần hoàn ngoại khoa", 2,
        f"{B('[Tổng quan — Mục tiêu học tập]')} Nêu 3 mục tiêu cốt lõi cần nắm vững về hồi sức suy tuần hoàn trong ngoại khoa?",
        f"1) <b>Kiến thức bệnh học:</b> Trình bày đầy đủ các nhóm {B('nguyên nhân và triệu chứng')} suy tuần hoàn ngoại khoa.<br>"
        f"2) <b>Hành động cấp cứu:</b> Chẩn đoán chính xác và đưa ra {Y('cách xử trí suy tuần hoàn')} theo huyết động và ngoại khoa.<br>"
        f"3) <b>Phương tiện hồi sức:</b> Kể tên chính xác các {G('thuốc vận mạch, trợ tim và dịch truyền cơ bản')} trong điều trị.",
        f"Suy tuần hoàn ngoại khoa có điểm đặc thù là gắn liền mất máu/mất dịch, chèn ép cơ học hoặc tác động thuốc gây mê, đòi hỏi bác sĩ phải vừa bù khối lượng/ổn định huyết động vừa giải quyết nguyên nhân thực thể tại phòng mổ.",
        "B0.01", ["Tong-quan"],
    ),

    # =========================================================================
    # B1 — SINH LÝ TUẦN HOÀN & 4 YẾU TỐ QUYẾT ĐỊNH LƯU LƯỢNG TIM
    # =========================================================================
    basic(
        "SURGR3-B1-01", "B1", "5 chức năng sinh lý của hệ tuần hoàn", 2,
        f"{B('[Sinh lý đại cương]')} Hệ tuần hoàn kín đảm nhận 5 chức năng sinh lý cơ bản nào đối với cơ thể?",
        f"1) <b>Trao đổi khí:</b> Vận chuyển và trao đổi {B('O₂, CO₂')}.<br>"
        f"2) <b>Dinh dưỡng & chuyển hóa:</b> Vận chuyển các chất dinh dưỡng, nước, điện giải và các chất chuyển hóa.<br>"
        f"3) <b>Nhiệt độ cơ thể:</b> Trao đổi nhiệt giúp {G('điều hòa thân nhiệt')}.<br>"
        f"4) <b>Bảo vệ & huyết học:</b> Vận chuyển các tế bào máu, {B('globulin miễn dịch và kháng thể')} bảo vệ cơ thể.<br>"
        f"5) <b>Điều hòa thể dịch:</b> Vận chuyển các {Y('nội tiết tố (hormone)')}.",
        f"Khi lưu lượng tuần hoàn suy giảm, cả 5 chức năng này đồng loạt đổ vỡ: thiếu oxy mô (tăng Axit Lactic), hạ thân nhiệt, toan chuyển hóa do ứ đọng chất chuyển hóa và suy giảm vận chuyển kháng thể.",
        "B1.01", ["Sinh-ly"],
    ),
    basic(
        "SURGR3-B1-02", "B1", "Công thức Lưu lượng tim (CO) & Thể tích nhát bóp (VES)", 1,
        f"{B('[Sinh lý — Lưu lượng tim]')} Công thức tính Lưu lượng tim (CO) và Thể tích tống máu tâm thu (VES) theo thể tích thất?",
        f"1) <b>Lưu lượng tim (Cardiac Output - CO):</b> {G('CO = VES × f')} (tích số giữa thể tích nhát bóp và tần số tim).<br>"
        f"2) <b>Thể tích tống máu tâm thu (VES - Stroke Volume):</b> {B('VES = EDV − ESV')} (Thể tích thất cuối tâm trương trừ Thể tích thất cuối tâm thu).",
        f"Mọi nguyên nhân làm giảm EDV (mất máu giảm tiền gánh, chèn ép tim, nhịp >180 lần/phút không kịp đổ đầy), tăng ESV (tăng hậu gánh hoặc suy co bóp cơ tim) hoặc rối loạn nhịp nặng đều làm sụt CO.",
        "B1.02", ["Sinh-ly", "Luu-luong-tim"],
    ),
    basic(
        "SURGR3-B1-03", "B1", "Tiền gánh (CVP) & Hậu gánh quyết định Lưu lượng tim", 1,
        f"{B('[Sinh lý — Tiền gánh & Hậu gánh]')} Định nghĩa Tiền gánh (Preload) và Hậu gánh (Afterload), giá trị CVP bình thường và các yếu tố chi phối từng yếu tố?",
        f"1) <b>Tiền gánh (Preload):</b> Là thể tích làm đầy tâm thất cuối thì tâm trương; đo gián tiếp qua {B('CVP / PVC')}, bình thường {G('8 – 12 cmH₂O')}; phụ thuộc lượng máu tĩnh mạch về tim, độ giãn nở thất và thời gian tâm trương.<br>"
        f"2) <b>Hậu gánh (Afterload):</b> Là lực cản tâm thất phải vượt qua để tống máu vào động mạch; phụ thuộc {Y('sức cản mạch ngoại biên (SVR)')}, độ đàn hồi thành mạch và kích thước thất.",
        f"Trong thực hành ngoại khoa, tiền gánh dễ đo trực tiếp nhất tại giường qua cột áp lực tĩnh mạch trung tâm (đơn vị cmH₂O). Tiền gánh thiếu thì bù dịch, hậu gánh tụt do giãn mạch thì dùng thuốc co mạch.",
        "B1.03", ["Sinh-ly", "CVP"],
    ),
    basic(
        "SURGR3-B1-04", "B1", "Sức co bóp cơ tim (EF ≥ 60%) & Nghịch lý Tần số tim > 180 lần/phút", 1,
        f"{B('[Sinh lý — Co bóp & Tần số tim]')} Chỉ số đánh giá sức co bóp cơ tim bình thường là bao nhiêu và tại sao nhịp tim > 180 lần/phút lại làm giảm mạnh lưu lượng tim?",
        f"1) <b>Sức co bóp cơ tim (Contractility):</b> Đánh giá bằng phân số tống máu ({B('EF - Ejection Fraction')}), bình thường {G('EF ≥ 60%')}.<br>"
        f"2) <b>Ảnh hưởng tần số tim (f):</b> Tỷ lệ thuận với CO trong giới hạn sinh lý, nhưng nếu đập quá nhanh {R('> 180 lần/phút')} → CO giảm mạnh vì {R('rút ngắn thời gian tâm trương làm đầy thất và giảm tưới máu mạch vành')}.",
        f"Tưới máu cơ tim (mạch vành trái) xảy ra chủ yếu ở thì tâm trương. Nhịp vượt 180 lần/phút vừa cắt cụt máu đổ đầy thất (giảm EDV → giảm VES) vừa làm thiếu máu cơ tim cấp.",
        "B1.04", ["Sinh-ly", "EF"],
    ),

    # =========================================================================
    # B2 — NGUYÊN NHÂN SUY TUẦN HOÀN NGOẠI KHOA
    # =========================================================================
    basic(
        "SURGR3-B2-01", "B2", "Nguyên nhân Tiền gánh: Mất máu cấp tính & Mất máu mạn tính", 1,
        f"{B('[Nguyên nhân — Mất máu]')} Kể các nhóm nguyên nhân gây mất máu cấp tính (chấn thương, bệnh lý, trong mổ) và mất máu mạn tính trong ngoại khoa?",
        f"1) <b>Mất máu cấp do chấn thương:</b> Đứt mạch máu lớn, vỡ gan, vỡ lách, {R('vỡ xương chậu, gãy xương lớn (xương đùi)')}, bỏng nặng.<br>"
        f"2) <b>Mất máu cấp do bệnh lý:</b> Xuất huyết tiêu hóa (loét dạ dày–tá tràng nôn máu/ỉa phân đen), vỡ giãn tĩnh mạch thực quản, {R('chửa ngoài tử cung vỡ')}.<br>"
        f"3) <b>Mất máu cấp trong mổ:</b> Phẫu thuật tạng lớn (gan, lách, tim, não), bóc tách diện dính rộng.<br>"
        f"4) <b>Mất máu mạn tính:</b> {Y('Giun móc, trĩ chảy máu kéo dài, u xơ tử cung rong huyết, rỉ máu đường mật')}.",
        f"Phân biệt mất máu cấp ngoại khoa cần hồi sức + phẫu thuật cầm máu khẩn (chấn thương tạng đặc, gãy xương đùi/xương chậu, chửa ngoài tử cung vỡ) với mất máu mạn tính ít gây sốc giảm thể tích cấp đột ngột.",
        "B2.01", ["Nguyen-nhan", "Mat-mau"],
    ),
    basic(
        "SURGR3-B2-02", "B2", "Nguyên nhân Tiền gánh: Mất nước–điện giải & Tăng khối lượng tuần hoàn (Thừa dịch)", 2,
        f"{B('[Nguyên nhân — Nước & Thể tích]')} Trình bày các nguyên nhân làm mất nước–điện giải (kèm ngưỡng diện tích bỏng nặng) và nhóm nguyên nhân thừa dịch gây suy tuần hoàn?",
        f"1) <b>Mất nước & điện giải:</b> Nôn nhiều (tắc ruột cơ học, hẹp phì đại môn vị, nghén nặng); sốt cao kéo dài; bỏng diện rộng ({R('> 30% ở người lớn, > 15% ở trẻ em')}); dịch dẫn lưu lượng lớn, đái tháo nhạt, đa niệu sau suy thận cấp.<br>"
        f"2) <b>Thừa dịch / Tăng thể tích tuần hoàn:</b> {Y('Suy thận cấp/mạn thiểu niệu, suy tim sung huyết, xơ gan mất bù')}; truyền dịch/máu quá nhanh; tăng tiết {B('Aldosterone / ADH')} thứ phát sau chấn thương sọ não vùng dưới đồi.",
        f"Cả hai thái cực thiếu nước lẫn quá tải thể tích đều gây suy tuần hoàn: thiếu nước gây tụt tiền gánh, còn thừa dịch đẩy tim vào tình trạng quá tải và phù phổi cấp.",
        "B2.02", ["Nguyen-nhan", "Mat-nuoc"],
    ),
    basic(
        "SURGR3-B2-03", "B2", "Rối loạn vận mạch: Giãn mạch đột ngột vs Co mạch mạnh", 2,
        f"{B('[Nguyên nhân — Vận mạch]')} Phân tích 2 thái cực rối loạn vận mạch gây suy tuần hoàn ngoại khoa: Giãn mạch đột ngột (giảm V tương đối) và Co mạch mạnh đột ngột?",
        f"1) <b>Giãn mạch đột ngột (giảm V tương đối):</b> {R('Sốc nhiễm khuẩn, sốc phản vệ, sốc tủy, sốc mất bù')}; tác dụng phụ của {Y('thuốc mê, gây tê tủy sống, gây tê ngoài màng cứng, thuốc hạ áp')}; hạ thân nhiệt nặng, thiếu oxy giai đoạn cuối, thừa CO₂ giai đoạn đầu.<br>"
        f"2) <b>Co mạch mạnh / đột ngột:</b> Giai đoạn đầu của sốc (phản xạ giao cảm bù trừ), quá liều thuốc co mạch ({B('Catecholamine, Ephedrine, Phenylephrine')}), cơn đau dữ dội, hoảng loạn tinh thần quá mức.",
        f"Trong gây mê hồi sức, tụt huyết áp ngay sau gây tê tủy sống hay khởi mê là biểu hiện kinh điển của giãn mạch đột ngột gây thiếu thể tích tuần hoàn tương đối.",
        "B2.03", ["Nguyen-nhan", "Van-mach"],
    ),
    basic(
        "SURGR3-B2-04", "B2", "3 nguyên nhân Cản trở cơ học hồi lưu máu về tim (Sốc tắc nghẽn)", 1,
        f"{R('[Nguyên nhân — Sốc tắc nghẽn]')} Nêu 3 tình trạng cản trở cơ học khiến máu tĩnh mạch không hồi lưu được về tim gây suy tuần hoàn tối cấp?",
        f"1) <b>Chèn ép tim cấp (Tamponade):</b> {R('Tràn máu hoặc tràn dịch màng ngoài tim cấp tính')}.<br>"
        f"2) <b>Tràn khí màng phổi dưới áp lực (Tension pneumothorax):</b> Áp lực khoang màng phổi đẩy lệch trung thất, gập xoắn tĩnh mạch chủ.<br>"
        f"3) <b>Nhịp tim quá nhanh:</b> Tần số {Y('> 180 lần/phút')} làm thất không kịp thời gian hút máu về.",
        f"Ở cả Tamponade lẫn Tràn khí màng phổi áp lực, CVP đều vọt cao (> 15 cmH₂O) kèm tĩnh mạch cổ nổi căng nhưng cung lượng tim tụt thảm hại — bù dịch đơn thuần không giải quyết được mà phải chọc dẫn lưu giải áp tức thì!",
        "B2.04", ["Nguyen-nhan", "Soc-tac-nghen"], red_flag=True,
    ),
    basic(
        "SURGR3-B2-05", "B2", "Nguyên nhân Tại tim (bao gồm Ca²⁺/K⁺ & Thuốc mê) và Nguyên nhân do Hậu gánh", 2,
        f"{B('[Nguyên nhân — Tại tim & Hậu gánh]')} Liệt kê các nguyên nhân suy tuần hoàn xuất phát tại tim (bệnh mạch vành, thuốc/điện giải, loạn nhịp) và do tăng hậu gánh?",
        f"1) <b>Tại cơ tim:</b> Suy tim cấp / NMCT cấp (co thắt hoặc tắc mạch vành, tắc động mạch phổi PE, thiếu oxy cơ tim nặng).<br>"
        f"2) <b>Ngộ độc & Thuốc/Điện giải:</b> Tiêm tĩnh mạch quá nhanh {R('Ca²⁺ hoặc K⁺')} gây ngừng tim; thuốc mê ({Y('Halothane, Thiopental, Atropine')}) tiêm nhanh; rối loạn giao cảm–phó giao cảm, toan kiềm & điện giải.<br>"
        f"3) <b>Do hậu gánh tăng vọt:</b> {B('Tăng huyết áp kịch phát, hẹp động mạch chủ cấp, tắc mạch phổi diện rộng')}.",
        f"Tiêm tĩnh mạch nhanh Kali hay Canxi là tai biến chết người ngay tại bàn mổ hoặc phòng hồi sức do gây ngừng tim tức thì ở thì tâm thu hoặc tâm trương.",
        "B2.05", ["Nguyen-nhan", "Tai-tim", "Hau-ganh"],
    ),

    # =========================================================================
    # B3 — TRIỆU CHỨNG LÂM SÀNG SUY TUẦN HOÀN
    # =========================================================================
    basic(
        "SURGR3-B3-01", "B3", "Biểu hiện toàn thân: Bệnh nhân tỉnh vs Đang gây mê trên bàn mổ", 2,
        f"{B('[Lâm sàng — Toàn thân]')} Triệu chứng toàn thân của suy tuần hoàn ở bệnh nhân tỉnh và dấu hiệu đặc trưng trên bàn mổ ở bệnh nhân đang gây mê khác nhau thế nào?",
        f"1) <b>Bệnh nhân tỉnh:</b> Lo lắng, bồn chồn, đánh trống ngực, đau tức ngực; giai đoạn nặng hơn thì {Y('vật vã, kích thích, li bì rồi hôn mê')}.<br>"
        f"2) <b>Bệnh nhân đang gây mê:</b> Da niêm mạc nhợt nhạt, đầu chi lạnh ẩm, {R('máu chảy tại phẫu trường chuyển màu sẫm tím')}, thân nhiệt hạ.",
        f"Trên bàn mổ, người bệnh mất tri giác vì thuốc mê nên không thể than mệt hay lo lắng; do đó phẫu thuật viên và bác sĩ gây mê phát hiện suy tuần hoàn qua máu phẫu trường sẫm tím và đầu chi lạnh tụt SpO₂.",
        "B3.01", ["Lam-sang", "Gay-me"],
    ),
    basic(
        "SURGR3-B3-02", "B3", "Triệu chứng Tim mạch & Phân biệt theo chỉ số CVP (< 7 vs > 15 cmH₂O)", 1,
        f"{B('[Lâm sàng — Tim mạch & CVP]')} Các thông số mạch, huyết áp tụt và ý nghĩa hai mốc CVP (< 7 cmH₂O và > 15 cmH₂O) kèm dấu hiệu tĩnh mạch ngoại biên/cổ?",
        f"1) <b>Mạch:</b> Nhanh nhỏ, nông, khó bắt; có thể chậm hoặc loạn nhịp hoàn toàn.<br>"
        f"2) <b>Huyết áp tụt:</b> {R('HATT < 90 – 100 mmHg')}, huyết áp kẹp, hoặc {R('giảm > 30% so với huyết áp nền')}.<br>"
        f"3) <b>CVP < 7 cmH₂O:</b> Thiếu khối lượng tuần hoàn (tĩnh mạch ngoại biên {Y('xẹp')}).<br>"
        f"4) <b>CVP > 15 cmH₂O:</b> Quá tải tuần hoàn, suy tim ứ trệ hoặc chèn ép tim cấp (tĩnh mạch cổ {R('nổi căng')}).",
        f"Cặp dấu hiệu đối lập 'tĩnh mạch ngoại biên xẹp + CVP < 7 cmH₂O' vs 'tĩnh mạch cổ nổi căng + CVP > 15 cmH₂O' giúp tách đôi lập tức nhóm cần bù dịch ào ạt với nhóm tuyệt đối cấm bù dịch nhanh.",
        "B3.02", ["Lam-sang", "CVP"],
    ),
    basic(
        "SURGR3-B3-03", "B3", "Triệu chứng Hô hấp & Tiết niệu trong suy tuần hoàn", 2,
        f"{B('[Lâm sàng — Hô hấp & Tiết niệu]')} Nêu dấu hiệu hô hấp (đặc biệt dấu dọa phù phổi cấp) và biến đổi nước tiểu trong suy tuần hoàn?",
        f"1) <b>Hô hấp:</b> Thở nhanh nông, khó thở, thở ngáp cá; nghe phổi có {R('ran ẩm')} (dấu hiệu báo động {R('dọa phù phổi cấp')}).<br>"
        f"2) <b>Tiết niệu:</b> {R('Thiểu niệu (< 0,5 ml/kg/giờ)')} hoặc vô niệu; nước tiểu sẫm màu, {Y('tỷ trọng tăng cao')}.",
        f"Nghe ran ẩm hai đáy phổi khi đang truyền dịch là tín hiệu báo động ngừng truyền ngay để ngừa phù phổi cấp; còn theo dõi lượng nước tiểu theo giờ (< 0,5 ml/kg/giờ) là thước đo nhạy nhất đánh giá tưới máu tạng.",
        "B3.03", ["Lam-sang", "Tiet-nieu"],
    ),

    # =========================================================================
    # B4 — CẬN LÂM SÀNG SUY TUẦN HOÀN
    # =========================================================================
    basic(
        "SURGR3-B4-01", "B4", "Công thức máu (Mất máu vs Mất nước) & Điện tâm đồ (ECG)", 2,
        f"{B('[Cận lâm sàng — CTM & ECG]')} Biến đổi Hb/Hct trong mất máu cấp so với mất nước cô đặc máu và các bất thường trên Điện tâm đồ (ECG) là gì?",
        f"1) <b>Công thức máu:</b> {R('Hb, Hematocrit giảm')} trong mất máu cấp (biểu hiện muộn hơn sau khi bù dịch pha loãng); ngược lại {Y('Hb, Hct tăng cao')} trong cô đặc máu do mất nước.<br>"
        f"2) <b>Điện tâm đồ (ECG):</b> Dấu hiệu thiếu máu cục bộ cơ tim ({R('ST chênh')}), dày thất, {B('rung nhĩ, cuồng nhĩ, block dẫn truyền hoặc nhịp nhanh thất')}.",
        f"Ngay những phút đầu sau vỡ tạng mất máu ồ ạt, huyết tương và hồng cầu mất đồng tỷ lệ nên Hb/Hct trên CTM chưa kịp tụt; chỉ sau khi dịch kẽ kéo vào lòng mạch hoặc ta truyền dịch tinh thể mới lộ rõ mức độ tụt Hb thực.",
        "B4.01", ["Can-lam-sang", "ECG"],
    ),
    basic(
        "SURGR3-B4-02", "B4", "Sinh hóa (Lactat, Ure/Creatinine), Khí máu & X-quang ngực tại giường", 1,
        f"{B('[Cận lâm sàng — Sinh hóa, Khí máu & X-quang]')} Nêu ngưỡng Axit Lactic, các thông số toan chuyển hóa trên khí máu, chức năng thận và hình ảnh X-quang ngực tại giường trong suy tuần hoàn?",
        f"1) <b>Sinh hóa & Thận:</b> Ure, Creatinine tăng (suy thận cấp); {R('Axit Lactic tăng > 2 – 4 mmol/L')} (chứng tỏ thiếu máu tưới mô).<br>"
        f"2) <b>Khí máu động mạch:</b> Toan chuyển hóa với {R('pH < 7,35')}, {R('HCO₃⁻ < 22')} và {R('BE < −3')}.<br>"
        f"3) <b>X-quang ngực tại giường:</b> Bóng tim to, {R('phổi mờ hình cánh bướm (phù phổi cấp)')}, tràn máu hoặc tràn khí màng phổi.",
        f"Phối hợp Axit Lactic > 2–4 mmol/L với toan chuyển hóa (pH < 7,35; HCO₃⁻ < 22; BE < −3) phản ánh mô đang chuyển hóa yếm khí nặng; X-quang ngực tại giường phát hiện ngay phù phổi cánh bướm hoặc tràn máu/tràn khí màng phổi mà không phải di chuyển bệnh nhân nặng.",
        "B4.02", ["Can-lam-sang", "Lactat", "Khi-mau"],
    ),

    # =========================================================================
    # B5 — HỒI SỨC GIẢM THỂ TÍCH TUẦN HOÀN
    # =========================================================================
    basic(
        "SURGR3-B5-01", "B5", "Thiết lập 2 đường truyền lớn (14G–16G) & Liệu pháp dịch truyền", 1,
        f"{B('[Hồi sức — Đường truyền & Dịch]')} Chuẩn bị đường truyền tĩnh mạch và nguyên tắc chọn tỷ lệ dịch tinh thể / dịch keo trong hồi sức giảm thể tích là gì?",
        f"1) <b>Đường truyền cấp cứu:</b> Đặt ngay {G('ít nhất 2 đường truyền tĩnh mạch lớn (kim 14G – 16G)')} hoặc đặt catheter tĩnh mạch trung tâm.<br>"
        f"2) <b>Dịch tinh thể (Ringer Lactat, NaCl 0,9%):</b> Ưu tiên hàng đầu, {G('bù gấp 3 lần lượng máu mất ước tính')}.<br>"
        f"3) <b>Dịch keo (Albumin, Gelatin):</b> Dùng khi cần nâng thể tích lòng mạch nhanh; {Y('tránh dùng quá liều gây suy thận và rối loạn đông máu')}.",
        f"Đặt kim lớn ngắn (14G–16G) giúp bơm dịch tốc độ tối đa theo định luật Poiseuille (lưu lượng tỷ lệ lũy thừa 4 với bán kính ống); dịch tinh thể thoát 2/3 ra khoảng kẽ nên cần bù tỷ lệ 3:1 so với lượng máu mất.",
        "B5.01", ["Hoi-suc", "Bu-dich"],
    ),
    basic(
        "SURGR3-B5-02", "B5", "Chiến lược truyền máu theo ngưỡng 30% & Mục tiêu đích Hb / Hct", 1,
        f"{B('[Hồi sức — Truyền máu]')} Khi nào chỉ cần truyền dịch tinh thể, khi nào bắt buộc truyền máu (và các chế phẩm nào), đồng thời mục tiêu đích Hb và Hct cần đạt là bao nhiêu?",
        f"1) <b>Mất máu < 30% khối lượng tuần hoàn:</b> Bù {G('dịch tinh thể')} và theo dõi sát huyết động.<br>"
        f"2) <b>Mất máu > 30% khối lượng tuần hoàn:</b> {R('Bắt buộc truyền máu')} gồm {B('khối hồng cầu, huyết tương tươi đông lạnh, tiểu cầu')}.<br>"
        f"3) <b>Đích cần đạt (và để chịu được phẫu thuật):</b> Duy trì {G('Hb ≥ 90 g/L (9 g/dL)')} và {G('Hematocrit ≥ 25 – 30%')}.",
        f"Khi mất vượt quá 30% thể tích máu, truyền khối hồng cầu đơn độc sẽ làm pha loãng các yếu tố đông máu và tiểu cầu còn lại — do đó phải truyền cân bằng cả hồng cầu khối, huyết tương tươi đông lạnh và tiểu cầu, kéo Hb > 90 g/L trước khi mổ lớn.",
        "B5.02", ["Hoi-suc", "Truyen-mau"],
    ),
    basic(
        "SURGR3-B5-03", "B5", "Phác đồ hồi sức theo CVP (8 cmH₂O) & MAP (65 mmHg) + Cầm máu ngoại khoa", 1,
        f"{G('[Phác đồ CVP – MAP]')} Trình bày 3 tình huống phân tầng xử trí theo CVP (ngưỡng 8 cmH₂O) và MAP (ngưỡng 65 mmHg / HATT 90 mmHg) kèm nguyên tắc cầm máu ngoại khoa?",
        f"1) <b>CVP < 8 cmH₂O:</b> Tiếp tục {G('bù dịch nhanh')}.<br>"
        f"2) <b>CVP > 8 cmH₂O và MAP > 65 mmHg (HATT > 90 mmHg):</b> Đã đủ dịch → {B('giảm tốc độ truyền, ngừng hồi sức dịch')}.<br>"
        f"3) <b>CVP > 8 cmH₂O nhưng MAP < 65 mmHg (HATT < 90 mmHg):</b> Thất bại bù dịch / giảm co bóp cơ tim / giãn mạch → dùng {Y('thuốc vận mạch / tăng co bóp (Norepinephrine, Dobutamine, Dopamine, Adrenaline)')}.<br>"
        f"4) <b>Cầm máu ngoại khoa:</b> Song song hồi sức và đưa ngay vào phòng mổ {R('thắt mạch, khâu tạng vỡ hoặc nút mạch (DSA)')}.",
        f"Mốc CVP 8 cmH₂O là van an toàn sinh tử: khi CVP đã vượt 8 cmH₂O mà huyết áp vẫn tụt, truyền thêm dịch chỉ đẩy bệnh nhân vào phù phổi cấp — phải chuyển ngay sang thuốc vận mạch/trợ tim và kiểm tra cầm máu phẫu thuật.",
        "B5.03", ["Hoi-suc", "CVP", "Ngoai-khoa"],
    ),
    cloze(
        "SURGR3-B5-04", "B5", "Cloze: Ngưỡng Sinh lý, Lâm sàng & Đích hồi sức mất máu",
        f"{B('[Con số vàng Suy tuần hoàn]')} Áp lực tĩnh mạch trung tâm (CVP) bình thường nằm trong khoảng {clz(1, G('8 – 12 cmH₂O'))}, phân số tống máu cơ tim bình thường là {clz(2, G('EF ≥ 60%'))}. Thiếu khối lượng tuần hoàn thể hiện khi CVP {clz(3, R('< 7 cmH₂O'))}, còn quá tải tuần hoàn hay chèn ép tim cấp khi CVP {clz(4, R('> 15 cmH₂O'))}. Dịch tinh thể bù gấp {clz(5, G('3 lần'))} lượng máu mất ước tính. Mất trên {clz(6, R('30%'))} khối lượng tuần hoàn bắt buộc truyền máu để đạt đích {clz(7, G('Hb ≥ 90 g/L (9 g/dL)'))} và {clz(8, G('Hct ≥ 25 – 30%'))}.",
        "B1.03, B1.04, B3.02, B5.01, B5.02", ["CVP", "Truyen-mau", "Cloze"],
    ),

    # =========================================================================
    # B6 — XỬ TRÍ QUÁ TẢI THỂ TÍCH & TÌNH HUỐNG LÂM SÀNG NGOẠI KHOA
    # =========================================================================
    basic(
        "SURGR3-B6-01", "B6", "4 bước xử trí Quá tải thể tích / Phù phổi cấp", 1,
        f"{R('[Cấp cứu — Phù phổi cấp]')} Khi bệnh nhân suy tuần hoàn rơi vào quá tải thể tích / phù phổi cấp (ran ẩm phổi, phổi mờ cánh bướm, CVP > 15 cmH₂O), 4 bước xử trí khẩn cấp là gì?",
        f"1) <b>Bước 1 (Dịch truyền):</b> {R('Ngừng truyền dịch ngay lập tức')}.<br>"
        f"2) <b>Bước 2 (Giảm tiền gánh):</b> Dùng thuốc lợi tiểu quai ({B('Furosemide tiêm tĩnh mạch')}).<br>"
        f"3) <b>Bước 3 (Hô hấp & Tim):</b> Dùng thuốc trợ tim kết hợp {G('thở oxy áp lực dương (CPAP / BiPAP)')}.<br>"
        f"4) <b>Bước 4 (Trơ lợi tiểu):</b> Chỉ định {R('lọc máu ngoài thận cấp cứu')} khi có suy thận kèm quá tải dịch không đáp ứng lợi tiểu.",
        f"Thở máy không xâm nhập áp lực dương (CPAP/BiPAP) vừa đẩy dịch ra khỏi phế nang cải thiện trao đổi khí vừa giảm lượng máu tĩnh mạch đổ về tim làm nhẹ gánh cho thất trái.",
        "B6.01", ["Phu-phoi-cap", "Cap-cuu"], red_flag=True,
    ),

    # =========================================================================
    # B7 — CẤP CỨU NGỪNG TUẦN HOÀN (CPR)
    # =========================================================================
    basic(
        "SURGR3-B7-01", "B7", "Nhận biết Ngừng tuần hoàn & Kỹ thuật ép tim – thổi ngạt", 1,
        f"{R('[CPR — Cơ bản]')} Dấu hiệu nhận biết ngừng tuần hoàn và thông số kỹ thuật ép tim – thổi ngạt trước và sau khi đặt ống nội khí quản?",
        f"1) <b>Nhận biết:</b> Mất mạch cảnh/bẹn, mất ý thức, ngừng thở hoặc thở ngáp cá, đồng tử giãn.<br>"
        f"2) <b>Chưa đặt nội khí quản:</b> Tỷ lệ {G('30 ép tim : 2 thổi ngạt')}; ép sâu {B('5 cm')}, tần số {G('100 – 120 lần/phút')}, để lồng ngực nở hoàn toàn sau mỗi lần ép.<br>"
        f"3) <b>Đã đặt nội khí quản:</b> Ép tim {G('liên tục 100 lần/phút')}, bóp bóng {B('8 – 10 lần/phút')} và {R('không ngừng ép tim')}.",
        f"Để lồng ngực nở hoàn toàn sau mỗi nhịp ép tạo áp lực âm lồng ngực hút máu về nhĩ phải — quyết định trực tiếp lưu lượng máu lên não và mạch vành trong CPR.",
        "B7.01", ["CPR", "Cap-cuu"], red_flag=True,
    ),
    basic(
        "SURGR3-B7-02", "B7", "Xử trí Rung thất (VF) / Nhịp nhanh thất vô mạch (pVT)", 1,
        f"{R('[CPR — Nhịp sốc được]')} Trình tự xử trí cấp cứu ngừng tuần hoàn khi điện tâm đồ là Rung thất (VF) hoặc Nhịp nhanh thất vô mạch (pVT)?",
        f"1) <b>Sốc điện phá rung ngay lập tức:</b> Máy {B('1 pha 360J')} hoặc {B('2 pha 150 – 200J')}.<br>"
        f"2) <b>Ép tim ngay lập tức:</b> Không kiểm tra mạch ngay mà ép tim {G('2 phút (5 chu kỳ)')} rồi mới đánh giá lại nhịp.<br>"
        f"3) <b>Thuốc cấp cứu:</b> Tiêm {G('Adrenaline 1 mg tĩnh mạch mỗi 3 – 5 phút')} và thuốc chống loạn nhịp {Y('Amiodarone 300 mg')}.",
        f"Chậm sốc điện mỗi phút ở nhịp VF/pVT làm giảm 7–10% cơ hội sống; nhưng ngay sau cú sốc phải ép tim liền 2 phút để tái lập áp lực tưới máu mạch vành cho tim phục hồi nhịp xoang.",
        "B7.02", ["CPR", "Soc-dien"], red_flag=True,
    ),
    basic(
        "SURGR3-B7-03", "B7", "Xử trí Vô tâm thu (Asystole) / Phân ly điện cơ (PEA) & 5H – 5T", 1,
        f"{B('[CPR — Nhịp không sốc được & 5H–5T]')} Hướng xử trí Vô tâm thu (Asystole) / Phân ly điện cơ (PEA) và liệt kê đủ 10 nguyên nhân đảo ngược (5H & 5T)?",
        f"1) <b>Nguyên tắc tối quan trọng:</b> {R('KHÔNG sốc điện')}; tiếp tục ép tim liên tục và tiêm {G('Adrenaline 1 mg TM mỗi 3 – 5 phút')}.<br>"
        f"2) <b>Nhóm 5H:</b> Giảm thể tích, Thiếu oxy, Toan máu, Tăng/Hạ Kali, Hạ thân nhiệt.<br>"
        f"3) <b>Nhóm 5T:</b> Tràn khí màng phổi áp lực, Chèn ép tim cấp, Ngộ độc, Tắc mạch phổi, Tắc mạch vành.",
        f"Ở nhóm PEA/Asystole, sốc điện không có tác dụng khử cực mà chỉ làm gián đoạn ép tim và tổn thương thêm cơ tim; chìa khóa cứu sống nằm ở việc tìm và giải quyết 5H–5T (đặc biệt trong ngoại khoa là giảm thể tích, tràn khí áp lực và chèn ép tim).",
        "B7.03", ["CPR", "5H-5T"],
    ),
    cloze(
        "SURGR3-B7-04", "B7", "Cloze: Thông số kỹ thuật CPR, Năng lượng sốc điện & Thuốc cấp cứu",
        f"{R('[Thông số CPR]')} Khi chưa đặt nội khí quản, tỷ lệ ép tim – thổi ngạt chuẩn là {clz(1, G('30 : 2'))}. Ép tim cần đạt độ sâu {clz(2, B('5 cm'))} với tần số {clz(3, G('100 – 120 lần/phút'))}. Tần số bóp bóng khi đã đặt ống nội khí quản là {clz(4, B('8 – 10 lần/phút'))} song song ép tim liên tục 100 lần/phút. Năng lượng sốc điện phá rung VF/pVT là {clz(5, Y('360J (1 pha)'))} hoặc {clz(6, Y('150 – 200J (2 pha)'))}. Sau cú sốc, tiến hành ép tim ngay trong {clz(7, G('2 phút (5 chu kỳ)'))}. Thuốc vận mạch cơ bản trong CPR là {clz(8, G('Adrenaline 1 mg TM mỗi 3 – 5 phút'))}, kết hợp {clz(9, Y('Amiodarone 300 mg'))} nếu VF/pVT kháng trị.",
        "B7.01, B7.02, B7.03", ["CPR", "Cloze"],
    ),
    cloze(
        "SURGR3-B4-03", "B4", "Cloze: Ngưỡng Sinh hóa, Khí máu & Điện giải/Bỏng ngoại khoa",
        f"{B('[Ngưỡng chẩn đoán Ngoại khoa]')} Mức độ bỏng nặng gây mất nước nghiêm trọng là {clz(1, R('> 30% ở người lớn'))} và {clz(2, R('> 15% ở trẻ em'))}. Thiếu máu tưới mô trên sinh hóa biểu hiện bằng {clz(3, R('Axit Lactic > 2 – 4 mmol/L'))}. Khí máu toan chuyển hóa khi {clz(4, R('pH < 7,35'))}, giá trị {clz(5, R('HCO₃⁻ < 22'))} và kiềm dư {clz(6, R('BE < −3'))}. Tổn thương thận suy giảm bài niệu khi nước tiểu {clz(7, R('< 0,5 ml/kg/giờ'))}.",
        "B2.02, B3.03, B4.02", ["Can-lam-sang", "Cloze"],
    ),

    # =========================================================================
    # 4 THẺ ⚡ THUẬT TOÁN QUYẾT ĐỊNH
    # =========================================================================
    algo(
        "SURGR3-ALGO-01", "B5", "Phác đồ hồi sức suy tuần hoàn theo cặp CVP & MAP", 1,
        f"Bệnh nhân suy tuần hoàn ngoại khoa có 2 đường truyền lớn và catheter tĩnh mạch trung tâm — Quy trình ra quyết định bù dịch, ngừng dịch hay dùng vận mạch theo CVP & MAP?",
        f"1) <b>Nếu CVP < 8 cmH₂O:</b> Thiếu tiền gánh thực sự → {G('tiếp tục bù dịch nhanh')} (tinh thể ưu tiên gấp 3 lượng máu mất; xét truyền máu nếu mất > 30%).<br>"
        f"2) <b>Nếu CVP > 8 cmH₂O VÀ MAP > 65 mmHg (HATT > 90 mmHg):</b> Đã đủ dịch → {B('giảm tốc độ truyền, ngừng hồi sức dịch')}.<br>"
        f"3) <b>Nếu CVP > 8 cmH₂O NHƯNG MAP < 65 mmHg (HATT < 90 mmHg):</b> Thất bại bù dịch / giảm co bóp / giãn mạch → {Y('dùng ngay vận mạch / tăng co bóp (Norepinephrine, Dobutamine, Dopamine, Adrenaline)')}.<br>"
        f"4) <b>Luôn song hành ngoại khoa:</b> Nếu mất máu tiến triển → đưa ngay phòng mổ {R('thắt mạch, khâu tạng vỡ hoặc nút mạch DSA')}.",
        f"Đánh giá lặp đi lặp lại bộ đôi CVP và MAP ngăn hai thái cực tai hại: bù thiếu dịch (gây suy thận thực thể) và bù thừa dịch (đẩy CVP > 15 cmH₂O gây phù phổi cấp).",
        "B5.01, B5.02, B5.03", ["CVP", "Hoi-suc"],
    ),
    algo(
        "SURGR3-ALGO-02", "B3", "Phân loại nhanh nguyên nhân suy tuần hoàn qua CVP & Tĩnh mạch cổ", 1,
        f"Bệnh nhân tụt huyết áp (HATT < 90–100 hoặc giảm > 30% HA nền) — Cách tách nhanh 2 nhóm nguyên nhân đối lập bằng khám tĩnh mạch & CVP trước khi truyền dịch?",
        f"1) <b>Nhánh CVP thấp (< 7–8 cmH₂O) + Tĩnh mạch ngoại biên xẹp:</b> Suy giảm thể tích thực sự (mất máu cấp, mất nước/bỏng) hoặc giãn mạch mạnh → {G('bù dịch tinh thể nhanh + cầm máu')}.<br>"
        f"2) <b>Nhánh CVP cao (> 15 cmH₂O) + Tĩnh mạch cổ nổi căng:</b> Cản trở hồi lưu về tim hoặc suy bơm / thừa dịch → rà soát ngay {R('Chèn ép tim cấp (Tamponade)')}, {R('Tràn khí màng phổi áp lực')}, {R('Suy tim ứ trệ / Quá tải dịch')}.<br>"
        f"3) <b>Nhánh bất thường hô hấp đi kèm:</b> Nghe phổi ran ẩm / X-quang mờ cánh bướm → kích hoạt {R('phác đồ ngừng dịch + Furosemide + CPAP/BiPAP')}.",
        f"Chỉ cần nhìn tĩnh mạch cổ và liếc qua cột CVP là tránh được sai lầm bơm 2 lít dịch vào người bệnh đang tràn khí màng phổi áp lực hay phù phổi cấp.",
        "B2.04, B3.02, B3.03, B4.02, B6.01", ["Chan-doan", "CVP"],
    ),
    algo(
        "SURGR3-ALGO-03", "B6", "Xử trí cấp cứu chấn thương gãy xương lớn (Gãy xương đùi kín)", 1,
        f"Bệnh nhân 50 tuổi gãy xương đùi kín, đau nhiều, mạch 100, HA 100/80, Hb 80 g/L — Chuỗi xử trí từng chặng từ lúc nhập viện đến khi đủ chuẩn vào phòng mổ KHX?",
        f"1) <b>Chặng 1 (Ưu tiên số 1 ngay lúc nhập viện):</b> {G('Cố định ổ gãy (nẹp Thomas) và giảm đau')} trước tiên — giúp giảm đau sâu sắc và ngăn chảy thêm {R('1.000 – 1.500 ml máu')} vào khoang mô mềm đùi.<br>"
        f"2) <b>Chặng 2 (Hồi sức tiền phẫu):</b> Đặt đường truyền lớn, bù dịch tinh thể (xét truyền khối hồng cầu nếu cần) và theo dõi huyết động.<br>"
        f"3) <b>Chặng 3 (Mốc đủ điều kiện phẫu thuật KHX đùi):</b> Phải đạt nồng độ {G('Hb > 90 g/L')} kèm {G('Hct > 25 – 30%')}.",
        f"Nếu bỏ qua cố định nẹp Thomas và giảm đau mà chỉ lo truyền dịch/truyền máu, hai đầu xương gãy nhọn tiếp tục cọ xát xé rách cơ đùi gây đau sốc và mất máu rỉ rả không ngừng.",
        "B5.02, B6.02", ["Tinh-huong", "Chan-thuong"],
    ),
    algo(
        "SURGR3-ALGO-04", "B7", "Phác đồ Cấp cứu Ngừng tuần hoàn (CPR) theo dạng Điện tâm đồ", 1,
        f"Khi phát hiện mất mạch cảnh/bẹn, mất ý thức, ngừng thở — Trình tự điều phối CPR, sốc điện và thuốc dựa theo màn hình ECG?",
        f"1) <b>Khởi động CPR chuẩn:</b> Gọi hỗ trợ, ép tim ngay {G('30 : 2')} (sâu 5 cm, 100–120 lần/phút; hoặc liên tục 100 lần/phút + bóp bóng 8–10 lần/phút nếu đã đặt NKQ).<br>"
        f"2) <b>Nhánh VF / pVT (Nhịp sốc được):</b> {R('Sốc điện phá rung ngay')} (1 pha 360J / 2 pha 150–200J) → ép tim ngay 2 phút (5 chu kỳ) → kiểm tra nhịp → {G('Adrenaline 1 mg TM mỗi 3–5 phút')} + {Y('Amiodarone 300 mg')}.<br>"
        f"3) <b>Nhánh Asystole / PEA (Không sốc được):</b> {R('KHÔNG sốc điện')} → ép tim liên tục + {G('Adrenaline 1 mg TM mỗi 3–5 phút')} + giải quyết ngay {B('5H & 5T')}.",
        f"Mấu chốt thành công của CPR là tối thiểu hóa thời gian gián đoạn ép tim ('hands-off time') và tách rạch ròi hai nhánh ECG ngay từ giây đầu gắn điện cực.",
        "B7.01, B7.02, B7.03", ["CPR", "Cap-cuu"],
    ),

    # =========================================================================
    # 8 THẺ ❌ BẪY LÂM SÀNG & 🛑 CỜ ĐỎ (GỒM CẢ 4 CÂU LƯỢNG GIÁ & TÌNH HUỐNG)
    # =========================================================================
    trap(
        "SURGR3-TRAP-01", "B6", "Nhầm nguyên nhân mất máu cấp hay gặp nhất trong cấp cứu ngoại khoa",
        f"Giữa 4 nguyên nhân: (1) U xơ tử cung, (2) Chảy máu do trĩ, (3) Chảy máu đường mật, (4) Vỡ xương chậu / Gãy xương lớn / Chấn thương tạng đặc — Đâu là nguyên nhân mất máu cấp hay gặp nhất cấp cứu ngoại khoa?",
        f"1) <b>Đáp án chuẩn:</b> {G('Vỡ xương chậu / Gãy xương lớn / Chấn thương tạng đặc (gan, lách)')} là nhóm nguyên nhân gây suy tuần hoàn do mất máu cấp tính hay gặp nhất trong cấp cứu ngoại khoa.<br>"
        f"2) <b>Nhóm mạn tính dễ bẫy:</b> U xơ tử cung rong huyết, trĩ chảy máu kéo dài và rỉ máu đường mật là các nguyên nhân {B('mất máu mạn tính')}, ít gây sốc mất máu cấp đột ngột.",
        f"Vỡ khung chậu hoặc vỡ tạng đặc có thể làm mất hàng lít máu vào khoang sau phúc mạc hoặc ổ bụng chỉ trong vài chục phút đầu sau tai nạn.",
        "B2.01, B6.02", ["Nguyen-nhan", "Luong-gia"],
    ),
    trap(
        "SURGR3-TRAP-02", "B3", "Bẫy dấu hiệu 'PVC > 9 cmH₂O' & Chỉ số tin cậy nhất đánh giá thiếu dịch",
        f"Trong chẩn đoán suy tuần hoàn do thiếu khối lượng tuần hoàn: Vì sao 'PVC > 9 cmH₂O' là phát biểu chưa phù hợp, và thông số nào đáng tin cậy nhất xác định còn thiếu dịch?",
        f"1) <b>Phát biểu sai trong triệu chứng sốc mất dịch:</b> {R('PVC > 9 cmH₂O là chưa phù hợp')} (CVP thông thường giảm thấp trong sốc giảm thể tích; HATT < 100, HATTr < 60 và khó thở mới phù hợp).<br>"
        f"2) <b>Thông số đáng tin cậy nhất:</b> {G('PVC < 8 cmH₂O')} (CVP thấp phản ánh trực tiếp tình trạng thiếu tiền gánh, đáng tin cậy hơn HATT < 100, HATTr < 80 hay nước tiểu < 500 ml/24h).",
        f"Huyết áp có thể bị duy trì giả tạo nhờ phản xạ co mạch bù trừ ban đầu, nước tiểu phản ánh chậm, còn PVC < 8 cmH₂O đo trực tiếp áp lực đổ đầy thất phải nên khẳng định ngay bệnh nhân vẫn đang khát dịch.",
        "B3.02, B5.03, B6.02", ["CVP", "Luong-gia"],
    ),
    trap(
        "SURGR3-TRAP-03", "B6", "Truyền máu/dịch trước mà quên Cố định ổ gãy xương đùi & Giảm đau",
        f"Gặp bệnh nhân gãy xương đùi kín đau dữ dội, mạch 100, HA 100/80, Hb 80 g/L — Nếu chỉ lo cắm dây truyền dịch/truyền máu mà bỏ qua nẹp cố định ổ gãy trước thì mắc bẫy gì?",
        f"1) <b>Hành động đầu tiên đúng nhất:</b> {G('Cố định ổ gãy (nẹp Thomas) và giảm đau')} ngay lập tức.<br>"
        f"2) <b>Lý do sinh lý bệnh:</b> Bất động ổ gãy giúp giảm đau sâu sắc và ngăn chặn mất thêm {R('1.000 – 1.500 ml máu')} từ các đầu xương di lệch rách vào mô mềm đùi.",
        f"Ở huyết áp 100/80 mmHg và Hb 80 g/L bệnh nhân chưa tụt HA nặng tức thì; động tác cầm máu cơ học tại chỗ bằng bất động nẹp Thomas và giảm đau cắt nguồn chảy máu + phản xạ sốc đau hiệu quả hơn truyền đơn thuần.",
        "B2.01, B6.02", ["Tinh-huong", "Luong-gia"],
    ),
    trap(
        "SURGR3-TRAP-04", "B5", "Đưa bệnh nhân đi mổ Kết hợp xương đùi khi Hb mới 80 g/L",
        f"Bệnh nhân gãy xương đùi đã cố định giảm đau nhưng xét nghiệm Hb vẫn ở mức 80 g/L — Có thể đưa lên bàn mổ kết hợp xương ngay hay cần nâng Hb tối thiểu lên bao nhiêu?",
        f"1) <b>Không mổ khi Hb ≤ 80 g/L:</b> Bệnh nhân chưa đủ an toàn huyết động để chịu cuộc mổ lớn mất thêm máu.<br>"
        f"2) <b>Mức Hb tối thiểu bắt buộc để mổ KHX:</b> Phải hồi sức nâng đạt {G('Hb > 90 g/L (≥ 9 g/dL)')} kèm {G('Hct > 25 – 30%')}.",
        f"Phẫu thuật kết hợp xương đùi tốn thời gian gây mê và mất thêm máu đáng kể trong lúc rạch mở ổ gãy; ngưỡng tối thiểu Hb > 90 g/L đảm bảo dự trữ vận chuyển oxy an toàn suốt cuộc mổ.",
        "B5.02, B6.02", ["Truyen-mau", "Luong-gia"],
    ),
    trap(
        "SURGR3-TRAP-05", "B4", "Nhìn Hb/Hct bình thường giờ đầu sau chấn thương rồi kết luận 'Không mất máu nặng'",
        f"Bệnh nhân vỡ lách vào cấp cứu sau tai nạn 20 phút, da lạnh mạch nhanh 125 nhưng xét nghiệm Công thức máu ghi Hb 128 g/L — Sai lầm diễn giải nào rất nguy hiểm?",
        f"1) <b>Lý do dẫn tới bẫy:</b> Trong mất máu cấp tính giai đoạn rất sớm, máu toàn phần mất đồng thời cả hồng cầu lẫn huyết tương nên {Y('Hb và Hct chưa kịp tụt ngay')}.<br>"
        f"2) <b>Thời điểm lộ rõ:</b> Hb và Hct chỉ giảm muộn hơn {B('sau khi dịch kẽ dịch chuyển vào lòng mạch hoặc sau truyền dịch tinh thể')}.",
        f"Chẩn đoán mất máu cấp giờ đầu phải dựa vào lâm sàng (mạch nhanh nhỏ, HA tụt/kẹp, da lạnh ẩm, CVP < 7 cmH₂O) và siêu âm ổ bụng — tuyệt đối không chờ tụt Hb trên tờ xét nghiệm mới hồi sức!",
        "B4.01, B3.02", ["Can-lam-sang", "Mat-mau"],
    ),
    redflag(
        "SURGR3-TRAP-06", "B5", "Tiếp tục bơm dịch nhanh khi CVP đã > 8 cmH₂O nhưng MAP vẫn < 65 mmHg",
        f"Bệnh nhân mất máu đang hồi sức đã nâng CVP lên 11 cmH₂O nhưng huyết áp vẫn tụt (MAP 55 mmHg) — Nếu cứ cố truyền thêm dịch nhanh sẽ dẫn đến biến chứng gì và đổi hướng thế nào?",
        f"1) <b>Tai biến nếu cố truyền:</b> Thúc đẩy nhanh tình trạng {R('quá tải tuần hoàn và phù phổi cấp')} (ran ẩm hai phổi, phổi mờ cánh bướm).<br>"
        f"2) <b>Chuyển hướng đúng chuẩn:</b> CVP > 8 cmH₂O mà MAP vẫn < 65 mmHg chứng tỏ giảm co bóp cơ tim / giãn mạch → phải {G('chuyển sang dùng thuốc vận mạch / tăng co bóp (Norepinephrine, Dobutamine, Dopamine, Adrenaline)')}.",
        f"Khi buồng tim đã đủ tiền gánh (CVP > 8 cmH₂O) theo đường cong Frank–Starling, tăng thêm thể tích chỉ làm ứ trệ áp lực ngược lên mao mạch phổi chứ không tăng thêm được cung lượng tim.",
        "B5.03, B6.01", ["CVP", "Phu-phoi-cap"],
    ),
    redflag(
        "SURGR3-TRAP-07", "B7", "Sốc điện cho Vô tâm thu (Asystole) hoặc Phân ly điện cơ (PEA) trong CPR",
        f"Trên monitor ngừng tuần hoàn hiện đường thẳng Vô tâm thu (Asystole) hoặc nhịp chậm nhưng không bắt được mạch (PEA) — Vì sao tuyệt đối KHÔNG bấm nút sốc điện?",
        f"1) <b>Quy tắc CPR bất biến:</b> {R('Vô tâm thu (Asystole) và Phân ly điện cơ (PEA) KHÔNG có chỉ định sốc điện')}.<br>"
        f"2) <b>Hành động cứu mạng đúng:</b> Duy trì ép tim liên tục không gián đoạn, tiêm {G('Adrenaline 1 mg TM mỗi 3 – 5 phút')} và khẩn trương truy tìm sửa chữa {B('5H & 5T')}.",
        f"Sốc điện chỉ khử cực được các ổ rung loạn đồng bộ trong VF/pVT; bấm sốc điện trên Asystole/PEA làm gián đoạn ép tim quý giá và gây tổn thương nhiệt cơ tim vô ích.",
        "B7.03", ["CPR", "Cap-cuu"],
    ),
    redflag(
        "SURGR3-TRAP-08", "B2", "Tiêm tĩnh mạch nhanh Ca²⁺ / K⁺ hoặc để tần số tim vượt > 180 lần/phút kéo dài",
        f"Hai tai biến iatrogenic (do thao tác/nhịp) trên bàn mổ và phòng hồi sức: tiêm tĩnh mạch nhanh Ca²⁺/K⁺ và bỏ mặc nhịp tim > 180 lần/phút gây thảm họa huyết động nào?",
        f"1) <b>Tiêm tĩnh mạch quá nhanh Ca²⁺ hoặc K⁺:</b> Gây {R('ngừng tim đột ngột')} ngay lập tức do ngộ độc điện giải màng tế bào cơ tim.<br>"
        f"2) <b>Tần số tim > 180 lần/phút:</b> Làm {R('lưu lượng tim giảm sút nghiêm trọng')} vì tâm trương quá ngắn khiến thất không kịp hút máu về và tụt tưới máu mạch vành.",
        f"Kali phải pha loãng truyền chậm qua bơm tiêm điện có kiểm soát tốc độ; còn nhịp nhanh > 180 lần/phút (như rung nhĩ nhanh, nhịp nhanh kịch phát trên thất/thất) phải cắt cơn hoặc kiểm soát tần số sớm để cứu cung lượng tim.",
        "B1.04, B2.04, B2.05", ["Tai-bien", "Nhip-tim"],
    ),
]
