# -*- coding: utf-8 -*-
"""surgr4_cards_data.py — SURG-R4: Suy Hô Hấp Cấp (ARF) (100% barem 10).
Cấu trúc chuẩn LIGHT_CSS (Dual-mode Light/Dark), 4 màu PALETTE (#ff6b6b, #ffd43b, #51cf66, #74c0fc),
mặt sau 🎯 + 💡, 4 thẻ ⚡ THUẬT TOÁN QUYẾT ĐỊNH, 8 thẻ ❌/🛑 Bẫy & Cờ đỏ, 3 Cloze, phủ 18/18 mã barem.
"""

def _c(hex_color, text):
    return f'<span style="color: {hex_color}; font-weight: 600;">{text}</span>'

def R(t): return _c("#ff6b6b", t)   # Đỏ cảnh báo / ngưỡng bệnh lý / nguy kịch
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
        "category": f"SURG-R4 · {section}",
        "badge": badge,
        "badge_class": "badge-red" if red_flag else "",
        "front": front,
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R4", section] + tags,
    }

def algo(cid, section, topic, tier, front, core, ai, barem, tags):
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "category": f"SURG-R4 · {section}",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-amber",
        "front": f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {B(topic)}<br>{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R4", section, "Thuat-toan"] + tags,
    }

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False):
    prefix = f"{R('🛑 CỜ ĐỎ')} — " if red_flag else f"{Y('❌ Bẫy lâm sàng')} — "
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": 1,
        "category": f"SURG-R4 · {section}",
        "badge": "🛑 CỜ ĐỎ" if red_flag else "❌ Bẫy lâm sàng",
        "badge_class": "badge-red" if red_flag else "badge-amber",
        "front": f"{prefix}{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R4", section, "Bay-lam-sang"] + tags,
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
        "category": f"SURG-R4 · {section}",
        "badge": "Cloze",
        "badge_class": "badge-blue",
        "text": text,
        "extra": f"[{barem}]",
        "tags": ["SURG-R4", section, "Cloze"] + tags,
    }


cards_data = [
    # =========================================================================
    # B0 — TỔNG QUAN & ĐỊNH NGHĨA
    # =========================================================================
    basic(
        "SURGR4-B0-01", "B0", "Vị trí dịch tễ cấp cứu & Nguyên tắc song hành của ARF", 2,
        f"{B('[Tổng quan — Tiếp cận ARF]')} Suy hô hấp cấp (ARF) đứng ở vị trí nào trong hồi sức cấp cứu và yêu cầu xử trí song hành cơ bản là gì?",
        f"1) <b>Tầm quan trọng lâm sàng:</b> Là bệnh lý cấp cứu thường gặp nhất tại HSCC và là {R('nguyên nhân tử vong hàng đầu')} của các bệnh nhân nặng.<br>"
        f"2) <b>Nguyên tắc hành động kép:</b> Can thiệp tức thì song song giữa {G('cấp cứu duy trì oxy não')} và {B('đánh giá chẩn đoán nguyên nhân')}.",
        f"Não chỉ chịu đựng được tình trạng thiếu oxy vài phút trước khi tổn thương không hồi phục; do đó không bao giờ được chờ có phim X-quang hay kết quả khí máu mới bắt đầu cung cấp oxy và khai thông đường thở.",
        "B0.01", ["Tong-quan"],
    ),
    basic(
        "SURGR4-B0-02", "B0", "Định nghĩa Suy hô hấp cấp theo ngưỡng Khí máu động mạch", 1,
        f"{B('[Định nghĩa ARF]')} Định nghĩa Suy hô hấp cấp (ARF) và hai ngưỡng giá trị khí máu động mạch (PaO₂, PaCO₂) xác lập chẩn đoán?",
        f"1) <b>Bản chất:</b> Hệ thống hô hấp đột ngột không đảm bảo trao đổi khí bình thường, gây rối loạn nghiêm trọng hoạt động tế bào và tạng.<br>"
        f"2) <b>Ngưỡng thiếu oxy máu:</b> {R('PaO₂ < 60 mmHg')}.<br>"
        f"3) <b>Ngưỡng ứ carbonic (kèm hoặc không kèm):</b> {R('PaCO₂ ≥ 46 mmHg')} (toan hô hấp).",
        f"Lấy mốc PaO₂ < 60 mmHg vì trên đường cong phân ly Oxyhemoglobin, từ 60 mmHg trở xuống độ bão hòa oxy (SpO₂ < 90%) bắt đầu lao dốc rất nhanh, đe dọa trực tiếp tế bào não và cơ tim.",
        "B0.02", ["Dinh-nghia", "Khi-mau"],
    ),

    # =========================================================================
    # B1 — SINH LÝ BỆNH TRAO ĐỔI KHÍ (GIẢM O₂ & TĂNG CO₂)
    # =========================================================================
    basic(
        "SURGR4-B1-01", "B1", "3 hệ thống đảm bảo cung cấp O₂ và thải CO₂", 2,
        f"{B('[Sinh lý trao đổi khí]')} Quá trình đưa O₂ tới tế bào và thải CO₂ ra môi trường ngoài phụ thuộc vào sự toàn vẹn của 3 hệ thống nào?",
        f"1) <b>Phổi:</b> Đảm nhận {G('thông khí')} và {G('khuếch tán khí')} qua màng phế nang – mao mạch.<br>"
        f"2) <b>Tuần hoàn:</b> Vận chuyển khí {B('O₂ và CO₂')} giữa phổi và các mô.<br>"
        f"3) <b>Mô / Tế bào:</b> Tách O₂ từ hồng cầu để tiêu thụ và thải CO₂ vào máu.",
        f"Suy hô hấp thực tế không chỉ xảy ra khi hỏng phổi (bộ trao đổi khí), mà còn sụp đổ nếu tuần hoàn ngừng bơm hoặc tế bào bị ngộ độc không tách/tiêu thụ được oxy.",
        "B1.01", ["Sinh-ly"],
    ),
    basic(
        "SURGR4-B1-02", "B1", "5 cơ chế gây giảm Oxy máu (PaO₂ < 60 mmHg) & Đáp ứng với FiO₂", 1,
        f"{B('[Sinh lý bệnh — Giảm Oxy máu]')} Trình bày 5 cơ chế làm giảm PaO₂, nêu cơ chế hay gặp nhất và cơ chế không đáp ứng oxy đơn thuần khi shunt > 30%?",
        f"1) <b>Shunt phải–trái trong phổi (V/Q = 0):</b> Máu tĩnh mạch qua phế nang không thông khí (xẹp phổi, đông đặc, phù phổi cấp, ARDS) — {R('không đáp ứng oxy đơn thuần khi shunt > 30% cung lượng tim')}.<br>"
        f"2) <b>Bất tương xứng thông khí/tưới máu (V/Q không đều):</b> {G('Cơ chế hay gặp nhất')} (COPD, hen, tắc mạch phổi) — {G('đáp ứng tốt khi tăng FiO₂')}.<br>"
        f"3) <b>Giảm thông khí phế nang:</b> PaO₂ giảm kèm PaCO₂ tăng tỷ lệ thuận (thuốc ức chế hô hấp, tổn thương tủy, nhược cơ); oxy cao có thể gây ngừng thở.<br>"
        f"4) <b>Rối loạn khuếch tán màng phế nang–mao mạch:</b> Hiếm gặp đơn thuần (xơ phổi kẽ tiến triển, tổn thương màng mao mạch nặng).<br>"
        f"5) <b>Giảm áp lực oxy khí thở vào:</b> Vùng núi cao hoặc môi trường kín thiếu dưỡng khí.",
        f"Phân biệt Shunt (V/Q = 0) với V/Q không đều giải thích trực tiếp lựa chọn phương tiện: V/Q không đều chỉ cần tăng FiO₂ qua kính mũi là cải thiện, còn Shunt lớn (>30%) bắt buộc phải dùng áp lực dương (CPAP/PEEP) mở lại phế nang xẹp.",
        "B1.02", ["Sinh-ly-benh", "Shunt"],
    ),
    basic(
        "SURGR4-B1-03", "B1", "3 cơ chế gây tăng CO₂ máu (PaCO₂ ≥ 46 mmHg)", 2,
        f"{B('[Sinh lý bệnh — Tăng CO₂]')} Ba nhóm cơ chế chính dẫn đến tình trạng tăng CO₂ máu (PaCO₂ ≥ 46 mmHg) là gì?",
        f"1) <b>Giảm thông khí phút (Minute Ventilation):</b> Giảm thể tích khí lưu thông hoặc giảm tần số thở.<br>"
        f"2) <b>Tăng khoảng chết (Dead space):</b> Khí vào vùng phổi được thông khí nhưng không có tưới máu trao đổi.<br>"
        f"3) <b>Tăng sản xuất CO₂ quá mức:</b> Sốt cao, co giật liên tục, sốc nhiễm khuẩn hoặc {Y('truyền quá nhiều carbohydrate')}.",
        f"Ở bệnh nhân có thông khí hạn chế (COPD nặng, đang cai máy thở), truyền năng lượng quá giàu glucose/carbohydrate làm tăng hệ số hô hấp (RQ = 1), sinh CO₂ đột biến đẩy PaCO₂ vọt tăng và khó cai máy.",
        "B1.03", ["Sinh-ly-benh", "CO2"],
    ),

    # =========================================================================
    # B2 — PHÂN LOẠI 3 TUÝP SUY HÔ HẤP CẤP
    # =========================================================================
    basic(
        "SURGR4-B2-01", "B2", "Tuýp 1 (Hypoxemic) vs Tuýp 2 (Hypercapnic) theo PaCO₂ & P(A-a)O₂", 1,
        f"{B('[Phân loại Khí máu — Tuýp 1 vs Tuýp 2]')} So sánh sự biến đổi PaO₂, PaCO₂, P(A-a)O₂ và nhóm bệnh điển hình giữa Suy hô hấp Tuýp 1 và Tuýp 2?",
        f"1) <b>Tuýp 1 (Giảm trao đổi Oxy / Hypoxemic):</b> PaO₂ {R('↓')}, PaCO₂ {G('↓ hoặc Bình thường')}, chênh áp phế nang–mao mạch P(A-a)O₂ {R('↑')}. Do rối loạn V/Q hoặc Shunt (ARDS, phù phổi cấp, viêm phổi nặng, xẹp phổi, tràn khí màng phổi, nhồi máu phổi).<br>"
        f"2) <b>Tuýp 2 (Giảm thông khí / Hypercapnic):</b> PaO₂ {R('↓')}, PaCO₂ {R('↑')}, P(A-a)O₂ {G('Bình thường')}. Do ức chế trung tâm hô hấp (tai biến mạch não, quá liều Opioid/Seduxen), liệt cơ (Guillain-Barré, nhược cơ, tủy sống cổ), mảng sườn di động.",
        f"Chỉ số vàng tách biệt hai tuýp trên khí máu là P(A-a)O₂: nếu nhu mô phổi còn nguyên vẹn và chỉ hỏng 'bơm thông khí' (Tuýp 2), hiệu áp phế nang–mao mạch P(A-a)O₂ vẫn bình thường.",
        "B2.01, B2.02", ["Phan-loai", "Khi-mau"],
    ),
    basic(
        "SURGR4-B2-02", "B2", "Tuýp 3 (Suy hô hấp hỗn hợp) & Ví dụ lâm sàng kinh điển", 2,
        f"{B('[Phân loại Khí máu — Tuýp 3]')} Đặc điểm bộ ba khí máu (PaO₂, PaCO₂, P(A-a)O₂) và các bệnh cảnh thường gặp của Suy hô hấp Tuýp 3 (Hỗn hợp)?",
        f"1) <b>Bộ ba khí máu Tuýp 3:</b> PaO₂ {R('↓')} + PaCO₂ {R('↑')} + P(A-a)O₂ {R('↑')} (tổn thương đồng thời cả màng trao đổi khí lẫn thông khí phế nang).<br>"
        f"2) <b>Bệnh cảnh điển hình:</b> {Y('Đợt cấp COPD mất bù')}, {R('hen phế quản ác tính')}, và suy hô hấp sau mổ ở bệnh nhân có bệnh phổi tắc nghẽn mạn tính từ trước.",
        f"Khác với Tuýp 2 thuần túy (P(A-a)O₂ bình thường), Tuýp 3 vừa tăng CO₂ do kiệt sức cơ hô hấp / tắc nghẽn đường thở vừa tăng P(A-a)O₂ do phá hủy phế nang – bất tương xứng V/Q nặng.",
        "B2.03", ["Phan-loai", "COPD"],
    ),

    # =========================================================================
    # B3 — TRIỆU CHỨNG LÂM SÀNG SUY HÔ HẤP CẤP
    # =========================================================================
    basic(
        "SURGR4-B3-01", "B3", "Khó thở & Tím tái (Ngưỡng Hb khử > 5 g/dL & 2 Ngoại lệ)", 1,
        f"{B('[Lâm sàng — Khó thở & Tím tái]')} Đặc điểm triệu chứng nhạy nhất (Khó thở) và quy luật xuất hiện Tím tái kèm 2 trường hợp thiếu oxy nặng nhưng KHÔNG tím?",
        f"1) <b>Khó thở (nhạy nhất & sớm nhất):</b> Thở nhanh {R('> 25 lần/phút')} hoặc chậm {R('< 12 lần/phút')}, thở nghịch thường cơ hoành, co kéo hõm ức và các cơ hô hấp phụ.<br>"
        f"2) <b>Tím tái:</b> Chỉ hiện rõ khi nồng độ {B('Hemoglobin khử trong máu mao mạch > 5 g/dL')} (tím môi và đầu chi sớm, tím toàn thân muộn).<br>"
        f"3) <b>Hai ngoại lệ không thấy tím:</b> Bệnh nhân {R('thiếu máu nặng')} (tổng Hb quá thấp không đủ tạo > 5 g/dL Hb khử) và {R('ngộ độc CO')} (tạo Carboxyhemoglobin màu đỏ anh đào).",
        f"Tình huống kinh điển dễ bị đánh lừa: bệnh nhân mất máu sau mổ kèm viêm phổi thiếu oxy trầm trọng nhưng da vẫn hồng nhạt do Hb chỉ còn 4–5 g/dL — tuyệt đối không dựa vào 'chưa tím' để chủ quan!",
        "B3.01", ["Lam-sang", "Tim-tai"],
    ),
    basic(
        "SURGR4-B3-02", "B3", "Rối loạn Tim mạch & Thần kinh – Ý thức (Dấu hiệu nặng)", 2,
        f"{B('[Lâm sàng — Tim mạch & Thần kinh]')} Hệ tim mạch và thần kinh – ý thức diễn tiến qua những giai đoạn nào khi suy hô hấp cấp nặng dần?",
        f"1) <b>Tim mạch:</b> Ban đầu mạch nhanh {Y('> 100 – 140 lần/phút')}, huyết áp tăng cao do tăng tiết Catecholamine phản xạ; sang giai đoạn nguy kịch thì {R('tụt huyết áp, loạn nhịp tim hoặc ngừng tuần hoàn')}.<br>"
        f"2) <b>Thần kinh – Ý thức (Dấu hiệu nặng):</b> Ban đầu lo lắng hốt hoảng, vã mồ hôi; sau đó {R('lờ đờ, lú lẫn, ngủ gà, hôn mê và co giật')} do phù não vì tăng CO₂ và toan máu nặng.",
        f"Ở bệnh nhân suy hô hấp, huyết áp bắt đầu tụt và tri giác chuyển từ kích thích sang ngủ gà / lơ mơ không phải là 'đang dịu lại' mà là dấu báo động não mất bù và sắp ngừng thở – ngừng tim.",
        "B3.02", ["Lam-sang", "Nguy-kich"],
    ),

    # =========================================================================
    # B4 — BẢNG PHÂN TẦNG MỨC ĐỘ SUY HÔ HẤP CẤP
    # =========================================================================
    basic(
        "SURGR4-B4-01", "B4", "Phân tầng 6 tiêu chí Lâm sàng: Trung bình / Nặng / Nguy kịch", 1,
        f"{B('[Phân tầng — Lâm sàng]')} Phân biệt 3 mức độ suy hô hấp (Trung bình, Nặng, Nguy kịch) qua 6 tiêu chí: Glasgow, Tim, Thở, Khả năng nói, Tím tái và Huyết áp?",
        f"1) <b>Glasgow:</b> TB {G('15đ')} · Nặng {Y('13–15đ (kích thích)')} · Nguy kịch {R('< 13đ, lờ đờ, hôn mê')}.<br>"
        f"2) <b>Mạch (/phút):</b> TB {G('100–120')} · Nặng {Y('120–140')} · Nguy kịch {R('> 140 hoặc chậm rời rạc')}.<br>"
        f"3) <b>Nhịp thở (/phút):</b> TB {G('25–30')} · Nặng {Y('30–40')} · Nguy kịch {R('> 40 hoặc < 10 (thở ngáp)')}.<br>"
        f"4) <b>Lời nói & Tím tái:</b> TB {G('câu dài / (+) môi')} · Nặng {Y('câu ngắn ngắt quãng / (++) môi–chi')} · Nguy kịch {R('không nói được / (+++) toàn thân')}.<br>"
        f"5) <b>Huyết áp:</b> TB {G('Bình thường')} · Nặng {Y('Tăng cao')} · Nguy kịch {R('Tụt huyết áp')}.",
        f"Bước chuyển từ 'Tăng huyết áp + kích thích + câu ngắn' (Nặng) sang 'Tụt huyết áp + thở chậm <10/ngáp + không nói được + lờ đờ' (Nguy kịch) là lằn ranh cuối phải đặt nội khí quản hoặc bóp bóng ngay.",
        "B4.01", ["Phan-do", "Lam-sang"],
    ),
    basic(
        "SURGR4-B4-02", "B4", "Phân tầng 3 tiêu chí Khí máu: Trung bình / Nặng / Nguy kịch", 1,
        f"{B('[Phân tầng — Khí máu động mạch]')} Các mốc giá trị pH, PaO₂ và PaCO₂ tương ứng với 3 mức độ suy hô hấp cấp (Trung bình, Nặng, Nguy kịch) là bao nhiêu?",
        f"1) <b>pH máu:</b> Trung bình {G('7,35 – 7,45')} · Nặng {Y('7,25 – 7,35')} · Nguy kịch {R('< 7,25')}.<br>"
        f"2) <b>PaO₂ (mmHg):</b> Trung bình {G('> 60')} · Nặng {Y('55 – 60')} · Nguy kịch {R('< 55')}.<br>"
        f"3) <b>PaCO₂ (mmHg):</b> Trung bình {G('45 – 55')} · Nặng {Y('55 – 60')} · Nguy kịch {R('> 60')}.",
        f"Điểm cắt pH < 7,25 của mức độ Nguy kịch khớp trực tiếp với một trong 5 chỉ định đặt ống nội khí quản khẩn cấp trong bài.",
        "B4.02", ["Phan-do", "Khi-mau"],
    ),
    cloze(
        "SURGR4-B4-03", "B4", "Cloze: Ngưỡng Khí máu & Lâm sàng phân mức Nguy kịch",
        f"{B('[Mốc Nguy kịch ARF]')} Định nghĩa suy hô hấp cấp dựa trên ngưỡng {clz(1, R('PaO₂ < 60 mmHg'))} kèm hoặc không kèm tăng carbonic {clz(2, R('PaCO₂ ≥ 46 mmHg'))}. Tím tái xuất hiện trên lâm sàng khi Hemoglobin khử mao mạch vượt quá {clz(3, R('5 g/dL'))}. Mức độ Nguy kịch được xác lập khi Glasgow {clz(4, R('< 13 điểm'))}, nhịp thở > 40 hoặc {clz(5, R('< 10 lần/phút (thở ngáp)'))}, đồng thời trên khí máu có pH {clz(6, R('< 7,25'))}, PaO₂ {clz(7, R('< 55 mmHg'))} và PaCO₂ {clz(8, R('> 60 mmHg'))}.",
        "B0.02, B3.01, B4.01, B4.02", ["Phan-do", "Cloze"],
    ),

    # =========================================================================
    # B5 — KHAI THÔNG ĐƯỜNG THỞ & CHỈ ĐỊNH ĐẶT NỘI KHÍ QUẢN
    # =========================================================================
    basic(
        "SURGR4-B5-01", "B5", "4 biện pháp Khai thông đường dẫn khí (Airway) ban đầu", 1,
        f"{B('[Xử trí — Đường thở]')} Bốn thao tác khai thông đường dẫn khí ban đầu trước khi quyết định đặt ống nội khí quản gồm những gì?",
        f"1) <b>Tư thế đầu – thân:</b> Đặt nằm ngửa ưỡn cổ ({R('chỉ khi không có chấn thương cột sống cổ')}) hoặc nằm nghiêng an toàn tránh hít sặc dịch nôn.<br>"
        f"2) <b>Dụng cụ chống tụt lưỡi:</b> Đặt {G('canun Guedel / Mayo')} miệng – họng.<br>"
        f"3) <b>Làm sạch đường thở:</b> Hút sạch đờm dãi và chất nôn trong họng miệng.<br>"
        f"4) <b>Giải phóng dị vật:</b> Thực hiện {Y('thủ thuật Heimlich')} ngay nếu nghi ngờ tắc dị vật đường thở.",
        f"Với nạn nhân đa chấn thương vùng đầu – cổ, tuyệt đối không ngửa cổ tối đa mà phải dùng thủ thuật nâng hàm (jaw thrust) giữ thẳng trục cột sống cổ trong khi đặt canun và hút đờm.",
        "B5.01", ["Airway", "Cap-cuu"],
    ),
    basic(
        "SURGR4-B5-02", "B5", "5 Chỉ định đặt ống Nội khí quản (Intubation) khẩn cấp", 1,
        f"{R('[Xử trí — Đặt Nội khí quản]')} Nêu chính xác 5 chỉ định bắt buộc phải đặt ống nội khí quản khẩn cấp ở bệnh nhân suy hô hấp cấp?",
        f"1) <b>Tắc nghẽn đường thở trên:</b> Không xử trí được bằng canun miệng – họng.<br>"
        f"2) <b>Mất phản xạ bảo vệ đường thở:</b> Thang điểm {R('Glasgow < 8 điểm')}.<br>"
        f"3) <b>Ứ trệ tiết:</b> Mất khả năng tự tống xuất đờm dãi.<br>"
        f"4) <b>Thiếu oxy trơ:</b> Thiếu oxy máu nặng không đáp ứng với thở oxy lưu lượng cao qua mask.<br>"
        f"5) <b>Toan hô hấp nặng:</b> Giảm thông khí nặng kèm toan hô hấp cấp với {R('pH < 7,25')}.",
        f"Khi có một trong 5 tiêu chí trên (đặc biệt Glasgow < 8 hoặc pH < 7,25), việc trì hoãn bằng thở mask hay CPAP/BiPAP dễ làm bệnh nhân ngừng thở đột ngột hoặc hít sặc nặng.",
        "B5.02", ["Noi-khi-quan", "Cap-cuu"], red_flag=True,
    ),

    # =========================================================================
    # B6 — LIỆU PHÁP OXY & KIỂM SOÁT THÔNG KHÍ
    # =========================================================================
    basic(
        "SURGR4-B6-01", "B6", "Mục tiêu SpO₂ / PaO₂ thông thường & Thở oxy trong rối loạn V/Q", 1,
        f"{G('[Xử trí — Liệu pháp Oxy]')} Mục tiêu đích oxy máu ở bệnh nhân suy hô hấp thông thường và phương thức khởi đầu cho cơ chế bất tương xứng V/Q?",
        f"1) <b>Mục tiêu đích thông thường:</b> Duy trì {G('SpO₂ 92 – 95%')} tương ứng {G('PaO₂ 60 – 80 mmHg')}.<br>"
        f"2) <b>Nhóm bất tương xứng V/Q (hen, viêm phổi, SHH thông thường):</b> Bắt đầu thở oxy qua {B('kính mũi 1 – 4 lít/phút')} ({B('FiO₂ ≈ 0,24 – 0,4')}).",
        f"Nhờ nguyên lý cơ chế V/Q không đều rất nhạy với nâng nồng độ oxy phế nang, mức FiO₂ 0,24–0,4 (kính mũi 1–4 L/ph) thường đã đủ đưa SpO₂ vào dải an toàn 92–95%.",
        "B6.01", ["Lieu-phap-oxy", "SpO2"],
    ),
    basic(
        "SURGR4-B6-02", "B6", "Oxy kiểm soát trong COPD ứ CO₂ mạn & Chiến lược Shunt phổi lớn", 1,
        f"{B('[Xử trí — COPD & Shunt lớn]')} Chế độ oxy kiểm soát bắt buộc cho COPD đợt cấp ứ CO₂ mạn khác hoàn toàn với chiến lược Shunt lớn (ARDS / phù phổi cấp nặng) như thế nào?",
        f"1) <b>COPD đợt cấp ứ CO₂ mạn:</b> Bắt buộc thở {Y('oxy liều thấp có kiểm soát')} qua kính mũi {Y('1 – 2 lít/phút')} hoặc mặt nạ {Y('Venturi FiO₂ ≤ 28 – 32%')} với đích chỉ cần {G('SpO₂ 88 – 92%')} (tránh mất kích thích hô hấp do thiếu oxy).<br>"
        f"2) <b>Shunt trong phổi lớn (ARDS, phù phổi cấp nặng):</b> Thở oxy qua {R('mặt nạ có túi dự trữ không thở lại (FiO₂ 60 – 100%)')}, thở máy không xâm nhập {B('CPAP / BiPAP')} hoặc đặt NKQ thở máy bảo vệ phổi với {R('PEEP cao')}.",
        f"Ở người bệnh COPD tăng CO₂ mạn tính, trung tâm hô hấp đã chai với CO₂ và chỉ còn thở nhờ tín hiệu thiếu oxy (hypoxic drive); đồng thời tăng FiO₂ quá mức làm co giãn mạch phổi sai lệch vùng (Haldane & V/Q) đẩy CO₂ vọt lên gây hôn mê tăng CO₂.",
        "B6.02", ["COPD", "ARDS", "PEEP"],
    ),
    cloze(
        "SURGR4-B6-03", "B6", "Cloze: Các ngưỡng đích Oxy, Nội khí quản & Phẫu thuật màng phổi",
        f"{B('[Thông số xử trí ARF]')} Chỉ định đặt nội khí quản khẩn cấp khi mất phản xạ bảo vệ đường thở với {clz(1, R('Glasgow < 8 điểm'))} hoặc toan hô hấp cấp {clz(2, R('pH < 7,25'))}. Đích oxy ở suy hô hấp thông thường là {clz(3, G('SpO₂ 92 – 95%'))} tương ứng {clz(4, G('PaO₂ 60 – 80 mmHg'))}. Với COPD đợt cấp ứ CO₂ mạn, chỉ đặt mặt nạ Venturi {clz(5, Y('FiO₂ ≤ 28 – 32%'))} hướng tới đích {clz(6, G('SpO₂ 88 – 92%'))}. Với tràn máu màng phổi đặt ống dẫn lưu cỡ {clz(7, B('28 – 32 Fr'))}, chỉ định mở ngực cầm máu nếu chảy {clz(8, R('> 200 ml/giờ trong 3 giờ liên tiếp'))}.",
        "B5.02, B6.01, B6.02, B7.02", ["Lieu-phap-oxy", "Ngoai-khoa", "Cloze"],
    ),

    # =========================================================================
    # B7 — XỬ TRÍ NGUYÊN NHÂN NGOẠI KHOA & HỒI SỨC PHỐI HỢP
    # =========================================================================
    basic(
        "SURGR4-B7-01", "B7", "Xử trí Tràn khí màng phổi áp lực & Tràn máu màng phổi", 1,
        f"{R('[Cấp cứu lồng ngực]')} Trình bày mốc giải phẫu xử trí Tràn khí màng phổi áp lực và tiêu chuẩn mở ngực cầm máu trong Tràn máu màng phổi?",
        f"1) <b>Tràn khí màng phổi áp lực:</b> Chọc kim giải áp ngay lập tức tại {R('khoang liên sườn 2 đường giữa đòn')}, sau đó đặt ống dẫn lưu màng phổi tại {B('khoang liên sườn 4–5 đường nách giữa')} hút liên tục.<br>"
        f"2) <b>Tràn máu màng phổi:</b> Đặt ống dẫn lưu màng phổi kích thước lớn ({B('28 – 32 Fr')}), hồi sức máu và {R('mổ nội soi hoặc mở ngực cầm máu khẩn cấp')} nếu máu chảy {R('> 200 ml/giờ trong 3 giờ liên tiếp')}.",
        f"Trong tràn khí màng phổi áp lực, chọc kim giải áp KLS 2 giữa đòn biến khoang áp lực dương kín thành tràn khí hở tức thì giải phóng chèn ép trung thất trước khi có thời gian chuẩn bị bộ dẫn lưu KLS 4–5.",
        "B7.01, B7.02", ["Long-nguc", "Cap-cuu"], red_flag=True,
    ),
    basic(
        "SURGR4-B7-02", "B7", "Xử trí Mảng sườn di động & Phù phổi cấp huyết động (OAP)", 1,
        f"{B('[Cấp cứu — Thành ngực & Phù phổi]')} Phương pháp xử trí đặc hiệu cho Mảng sườn di động và 5 thuốc/biện pháp cấp cứu Phù phổi cấp huyết động (OAP)?",
        f"1) <b>Mảng sườn di động:</b> Giảm đau vùng ngực ({G('gây tê ngoài màng cứng / tê thần kinh liên sườn')}), cố định thành ngực hoặc {B('thở máy áp lực dương nội khí quản (cố định trong)')}.<br>"
        f"2) <b>Phù phổi cấp huyết động (OAP):</b> {B('Thở oxy')} + {G('Furosemide tiêm tĩnh mạch')} + {G('Nitroglycerin truyền tĩnh mạch')} + {Y('Morphine')} + giảm hậu gánh tim.",
        f"Mảng sườn di động gây hô hấp đảo chiều và lắc lư trung thất rất đau; gây tê cắt đau giúp bệnh nhân dám thở sâu, còn thở máy áp lực dương đóng vai trò chiếc nẹp khí từ bên trong đẩy vững đoạn sườn gãy.",
        "B7.03", ["Mang-suon-di-dong", "Phu-phoi-cap"],
    ),

    # =========================================================================
    # 4 THẺ ⚡ THUẬT TOÁN QUYẾT ĐỊNH
    # =========================================================================
    algo(
        "SURGR4-ALGO-01", "B2", "Đọc nhanh Khí máu động mạch chẩn đoán & phân 3 Tuýp Suy hô hấp", 1,
        f"Cầm tờ kết quả Khí máu động mạch của bệnh nhân khó thở cấp — Thứ tự đọc từng thông số để chốt Tuýp 1, Tuýp 2 hay Tuýp 3 và đánh giá mức độ Nguy kịch?",
        f"1) <b>Xác lập ARF:</b> Kiểm tra {R('PaO₂ < 60 mmHg')} (giảm oxy) và {R('PaCO₂ ≥ 46 mmHg')} (ứ CO₂).<br>"
        f"2) <b>Chia Tuýp qua PaCO₂ & P(A-a)O₂:</b><br>"
        f"   • PaCO₂ ↓/BT + P(A-a)O₂ ↑ → {B('Tuýp 1 (Giảm oxy — V/Q hoặc Shunt)')}.<br>"
        f"   • PaCO₂ ↑ + P(A-a)O₂ Bình thường → {Y('Tuýp 2 (Giảm thông khí / Bơm hô hấp)')}.<br>"
        f"   • PaCO₂ ↑ + P(A-a)O₂ ↑ → {R('Tuýp 3 (Hỗn hợp — COPD mất bù, hen ác tính)')}.<br>"
        f"3) <b>Báo động Nguy kịch:</b> Kiểm tra bộ ba {R('pH < 7,25')}, {R('PaO₂ < 55 mmHg')}, {R('PaCO₂ > 60 mmHg')} để kích hoạt đặt NKQ khẩn.",
        f"Cách đọc 3 bước theo trục PaO₂ → PaCO₂/P(A-a)O₂ → pH giúp định vị ngay tổn thương nằm ở phế nang–mao mạch (Tuýp 1), trung tâm/cơ hô hấp (Tuýp 2) hay cả hai (Tuýp 3) để chọn đúng oxy hoặc hỗ trợ thông khí.",
        "B0.02, B2.01, B2.02, B2.03, B4.02", ["Khi-mau", "Phan-loai"],
    ),
    algo(
        "SURGR4-ALGO-02", "B5", "Quy trình Khai thông đường thở & Quyết định Đặt Nội khí quản", 1,
        f"Tiếp nhận bệnh nhân suy hô hấp cấp tím tái kích thích hoặc lơ mơ — Luồng quyết định từ khai thông đường thở cơ bản tới đặt ống nội khí quản?",
        f"1) <b>Bước 1 (Airway tại chỗ):</b> Ngửa đầu nâng cằm (tránh nếu nghi chấn thương cổ) hoặc nằm nghiêng an toàn → hút sạch đờm dãi/chất nôn → đặt canun Guedel/Mayo chống tụt lưỡi (Heimlich nếu dị vật).<br>"
        f"2) <b>Bước 2 (Sàng lọc 5 cờ đặt NKQ):</b> Nếu có bất kỳ dấu nào: {R('tắc nghẽn trên không qua được canun')}, {R('Glasgow < 8 điểm')}, mất tống đờm, {R('thiếu oxy trơ với mask nồng độ cao')}, hoặc {R('toan hô hấp pH < 7,25')} → {R('Đặt NKQ khẩn cấp')}.<br>"
        f"3) <b>Bước 3 (Theo dõi nếu chưa đặt NKQ):</b> Chọn chế độ oxy đúng theo cơ chế bệnh sinh và chấm lại tầng Trung bình/Nặng/Nguy kịch.",
        f"Không chờ đủ cả 5 tiêu chuẩn mới đặt nội khí quản: chỉ cần thỏa 1 tiêu chí tuyệt đối (như Glasgow < 8 hoặc pH < 7,25) là đã phải chủ động kiểm soát đường thở an toàn ngay.",
        "B5.01, B5.02, B4.01, B4.02", ["Airway", "Noi-khi-quan"],
    ),
    algo(
        "SURGR4-ALGO-03", "B6", "Chọn Phương tiện Oxy & Áp lực dương theo Cơ chế (V/Q vs COPD vs Shunt)", 1,
        f"Sau khi khai thông đường thở — Cách chọn đúng thiết bị cung cấp oxy và ngưỡng SpO₂ mục tiêu tương ứng với từng cơ chế suy hô hấp?",
        f"1) <b>Nhánh bất tương xứng V/Q thông thường (Hen, viêm phổi):</b> Khởi đầu {G('oxy kính mũi 1 – 4 L/phút (FiO₂ 0,24 – 0,4)')}, mục tiêu {G('SpO₂ 92 – 95% (PaO₂ 60 – 80 mmHg)')}.<br>"
        f"2) <b>Nhánh COPD đợt cấp ứ CO₂ mạn:</b> Chỉ dùng {Y('kính mũi 1 – 2 L/phút hoặc Venturi FiO₂ ≤ 28 – 32%')}, giữ mục tiêu khiêm tốn {G('SpO₂ 88 – 92%')} tránh ngừng thở.<br>"
        f"3) <b>Nhánh Shunt lớn (ARDS, OAP nặng):</b> {R('Mask túi không thở lại (FiO₂ 60 – 100%)')} → chuyển nhanh {B('CPAP / BiPAP')} hoặc {R('thở máy NKQ với PEEP cao')}.",
        f"Chọn sai nhánh là sai lầm hay gặp nhất trong thực hành: dùng FiO₂ 100% bừa bãi cho COPD gây hôn mê tăng CO₂, còn dùng kính mũi 3 L/ph cho ARDS shunt > 30% thì SpO₂ mãi không lên được.",
        "B1.02, B6.01, B6.02", ["Lieu-phap-oxy", "COPD", "ARDS"],
    ),
    algo(
        "SURGR4-ALGO-04", "B7", "Xử trí Cấp cứu Ngoại khoa lồng ngực gây Suy hô hấp tối cấp", 1,
        f"Bệnh nhân chấn thương ngực kín / hở suy hô hấp cấp tụt huyết áp — Cách phân biệt và ra y lệnh can thiệp tức thì cho 3 bệnh cảnh lồng ngực?",
        f"1) <b>Tràn khí màng phổi áp lực (gõ vang, mất rì rào phế nang, TM cổ nổi, tụt HA):</b> {R('Chọc kim giải áp ngay KLS 2 đường giữa đòn')} → sau đó dẫn lưu {B('KLS 4–5 đường nách giữa')}.<br>"
        f"2) <b>Tràn máu màng phổi (gõ đục, hội chứng mất máu):</b> Đặt ống dẫn lưu lớn {B('28 – 32 Fr')} + truyền máu → {R('mổ mở ngực/nội soi cầm máu')} khi ra {R('> 200 ml/giờ × 3 giờ liên tiếp')}.<br>"
        f"3) <b>Mảng sườn di động (hô hấp đảo chiều):</b> {G('Gây tê ngoài màng cứng / tê liên sườn giảm đau')} + cố định thành ngực hoặc {B('thở máy áp lực dương (cố định trong)')}.",
        f"Trong tràn khí màng phổi áp lực, không bao giờ chờ chụp phim X-quang ngực mới chọc kim giải áp — thời gian chờ phim đủ khiến trung thất bị đẩy gập tĩnh mạch chủ gây ngừng tuần hoàn.",
        "B7.01, B7.02, B7.03", ["Long-nguc", "Chan-thuong"],
    ),

    # =========================================================================
    # 8 THẺ ❌ BẪY LÂM SÀNG & 🛑 CỜ ĐỎ
    # =========================================================================
    redflag(
        "SURGR4-TRAP-01", "B6", "Xả oxy lưu lượng cao (6–10 L/ph) cho bệnh nhân COPD đợt cấp để kéo SpO₂ lên 98–100%",
        f"Bệnh nhân COPD đợt cấp vào viện SpO₂ 82% — Vì sao bơm oxy 8 lít/phút để kéo SpO₂ đạt 99% lại có thể đẩy người bệnh vào hôn mê và ngừng thở?",
        f"1) <b>Mất kích thích hô hấp (Hypoxic Drive):</b> Người COPD ứ CO₂ mạn duy trì nhịp thở chủ yếu nhờ kích thích thiếu oxy; oxy quá cao làm bệnh nhân {R('giảm thông khí, ứ CO₂ kịch phát và hôn mê')}.<br>"
        f"2) <b>Liệu pháp oxy chuẩn cho COPD:</b> Dùng liều thấp có kiểm soát (kính mũi {Y('1 – 2 L/phút')} hoặc {Y('Venturi FiO₂ ≤ 28 – 32%')}) với đích chỉ cần {G('SpO₂ 88 – 92%')}.",
        f"Ở bệnh nhân COPD mạn, SpO₂ 88–92% đã nằm ở đoạn dốc an toàn của đường cong Oxyhemoglobin đủ cung cấp oxy mô mà vẫn bảo toàn phản xạ tự thở.",
        "B1.02, B6.02", ["COPD", "Lieu-phap-oxy"],
    ),
    trap(
        "SURGR4-TRAP-02", "B3", "Thấy niêm mạc không tím tái nên loại trừ thiếu oxy máu nặng",
        f"Bệnh nhân chấn thương mất máu nặng (Hb còn 45 g/L) hoặc nạn nhân ngạt khói cháy (ngộ độc CO) thở nhanh vật vã nhưng môi không hề tím — Vì sao không thấy tím tái?",
        f"1) <b>Điều kiện sinh lý xuất hiện tím:</b> Chỉ thấy tím khi nồng độ {B('Hemoglobin khử mao mạch > 5 g/dL')}.<br>"
        f"2) <b>Hai bẫy kinh điển không tím dù thiếu oxy chết người:</b> {R('Thiếu máu nặng')} (không đủ lượng Hb để tạo > 5 g/dL Hb khử) và {R('ngộ độc khí CO')} (Carboxyhemoglobin có màu đỏ anh đào).",
        f"Khó thở và rối loạn ý thức mới là dấu hiệu nhạy và sớm; tin vào 'không tím thì chưa thiếu oxy' ở người thiếu máu nặng hay ngộ độc CO là sai lầm chết người.",
        "B3.01", ["Tim-tai", "Lam-sang"],
    ),
    trap(
        "SURGR4-TRAP-03", "B1", "Kỳ vọng thở oxy qua mask đơn thuần sẽ giải quyết được Shunt phổi lớn > 30%",
        f"Bệnh nhân ARDS hoặc phù phổi cấp nặng có shunt phải–trái trong phổi > 30% cung lượng tim — Tại sao tăng lưu lượng oxy đơn thuần vẫn không cải thiện được PaO₂?",
        f"1) <b>Lý do sinh lý bệnh:</b> Trong Shunt (V/Q = 0), máu tĩnh mạch chảy qua các phế nang bị xẹp hoặc chứa đầy dịch hoàn toàn {R('không tiếp xúc được với khí thở vào')}, nên tăng FiO₂ đơn thuần thất bại.<br>"
        f"2) <b>Giải pháp khắc phục đúng:</b> Phải dùng {G('áp lực dương (CPAP / BiPAP)')} hoặc {G('đặt NKQ thở máy bảo vệ phổi với PEEP cao')} để mở huy động lại các phế nang xẹp.",
        f"Khác với bất tương xứng V/Q (đáp ứng tốt với FiO₂), Shunt > 30% cung lượng tim kháng oxy đơn thuần chính là dấu hiệu gợi ý tại giường phải nâng cấp hỗ trợ áp lực dương ngay.",
        "B1.02, B6.02", ["Shunt", "ARDS"],
    ),
    trap(
        "SURGR4-TRAP-04", "B2", "Nhầm lẫn Suy hô hấp Tuýp 2 thuần túy với Tuýp 3 (Hỗn hợp) khi đọc P(A-a)O₂",
        f"Cả Suy hô hấp Tuýp 2 và Tuýp 3 đều có PaO₂ ↓ và PaCO₂ ↑ — Thông số nào phân định hai tuýp này và sai lầm xử trí là gì nếu bỏ sót tổn thương nhu mô của Tuýp 3?",
        f"1) <b>Thông số phân định:</b> Chênh lệch áp lực oxy phế nang – mao mạch {B('P(A-a)O₂')}: {G('Bình thường ở Tuýp 2')} (quá liều Opioid, Guillain-Barré, mảng sườn) nhưng {R('Tăng cao ở Tuýp 3')} (COPD mất bù, hen ác tính, sau mổ trên nền COPD).<br>"
        f"2) <b>Ý nghĩa lâm sàng:</b> Tuýp 3 đòi hỏi vừa giải quyết thông khí/tắc nghẽn phế quản vừa chỉnh oxy thận trọng cho phế nang tổn thương.",
        f"Chỉ nhìn PaO₂ và PaCO₂ mà quên tính P(A-a)O₂ sẽ không biết phế nang và màng trao đổi khí có đang tổn thương kèm theo hay không.",
        "B2.02, B2.03", ["Khi-mau", "Phan-loai"],
    ),
    redflag(
        "SURGR4-TRAP-05", "B4", "Chủ quan khi thấy bệnh nhân suy hô hấp từ kích thích vật vã chuyển sang 'nằm yên, thở chậm < 10 lần/phút'",
        f"Một bệnh nhân suy hô hấp đang thở 36 lần/phút, tăng huyết áp, bồn chồn — Nửa giờ sau bỗng 'nằm im lờ đờ', thở chậm còn 9 lần/phút, huyết áp tụt — Đây là dấu hiệu hồi phục hay báo tử?",
        f"1) <b>Đánh giá chuẩn xác:</b> Bệnh nhân đã sụp sang {R('Mức độ Nguy kịch')} (Glasgow < 13, thở < 10 lần/phút kiểu thở ngáp, tụt huyết áp, tím toàn thân).<br>"
        f"2) <b>Hành động tối khẩn:</b> Phải bóp bóng và {R('đặt ống nội khí quản khẩn cấp')} ngay lập tức — tuyệt đối không hiểu nhầm là 'đáp ứng thuốc đang ngủ dịu lại'.",
        f"Cơ hô hấp kiệt sức kết hợp tăng CO₂ gây ức chế trung tâm hô hấp (toan hô hấp pH < 7,25) làm bệnh nhân ngưng thở chỉ sau vài phút nếu không đặt nội khí quản kịp.",
        "B3.02, B4.01, B4.02, B5.02", ["Nguy-kich", "Noi-khi-quan"],
    ),
    redflag(
        "SURGR4-TRAP-06", "B7", "Gửi bệnh nhân Tràn khí màng phổi áp lực đi chụp X-quang trước khi chọc kim giải áp",
        f"Bệnh nhân chấn thương ngực khó thở dữ dội, tĩnh mạch cổ nổi căng, khí quản lệch bên đối diện, gõ vang phế trường bên tổn thương và tụt huyết áp — Cấm làm sai lầm gì?",
        f"1) <b>Cấm tuyệt đối:</b> Không đẩy đi chụp X-quang hay CT chờ chẩn đoán hình ảnh.<br>"
        f"2) <b>Phản xạ cứu mạng tức thì:</b> {R('Chọc kim giải áp ngay lập tức vào khoang liên sườn 2 đường giữa đòn')} ngay tại giường cấp cứu, sau đó mới đặt dẫn lưu màng phổi {B('KLS 4–5 đường nách giữa')}.",
        f"Tràn khí màng phổi áp lực gây sốc tắc nghẽn cấp tính; chọc kim giải áp là chẩn đoán đồng thời điều trị cứu sống ngay trong 10 giây.",
        "B7.01", ["Long-nguc", "Cap-cuu"],
    ),
    trap(
        "SURGR4-TRAP-07", "B7", "Đặt ống dẫn lưu màng phổi quá nhỏ trong Tràn máu màng phổi hoặc trì hoãn mở ngực khi máu ra > 200 ml/giờ",
        f"Trong xử trí Tràn máu màng phổi cấp cứu ngoại khoa, hai sai lầm kỹ thuật thường gặp về kích thước ống dẫn lưu và ngưỡng theo dõi chỉ định mổ cầm máu là gì?",
        f"1) <b>Kích thước ống dẫn lưu chuẩn:</b> Phải đặt ống dẫn lưu màng phổi cỡ lớn ({G('28 – 32 Fr')}) — đặt ống quá nhỏ dễ tắc nhanh do cục máu đông.<br>"
        f"2) <b>Ngưỡng mở ngực/nội soi cầm máu khẩn:</b> Chỉ định mổ ngay khi lưu lượng máu chảy qua dẫn lưu {R('> 200 ml/giờ trong 3 giờ liên tiếp')}.",
        f"Ống dẫn lưu lớn vừa thoát sạch máu cục ngăn đông máu màng phổi về sau vừa giúp theo dõi chính xác lượng máu chảy mỗi giờ để không bỏ lỡ ngưỡng mổ > 200 ml/giờ × 3 giờ.",
        "B7.02", ["Long-nguc", "Ngoai-khoa"],
    ),
    trap(
        "SURGR4-TRAP-08", "B1", "Truyền quá nhiều Carbohydrate cho bệnh nhân suy hô hấp mạn tính đang tăng CO₂ máu",
        f"Bệnh nhân bệnh phổi tắc nghẽn mạn đang cai máy thở đột ngột tăng PaCO₂ dai dẳng dù không sốt hay co giật — Nguyên nhân dinh dưỡng tĩnh mạch nào dễ bị bỏ qua?",
        f"1) <b>Lý do gây tăng CO₂:</b> {Y('Truyền quá nhiều carbohydrate')} (năng lượng đường cao) làm cơ thể chuyển hóa tăng sinh CO₂ quá mức.<br>"
        f"2) <b>Các nguyên nhân tăng sản xuất CO₂ đi kèm cần nhớ:</b> Sốt cao, co giật liên tục, sốc nhiễm khuẩn.",
        f"Chuyển hóa 1 phân tử glucose tạo ra lượng CO₂ nhiều hơn so với chuyển hóa lipid (RQ 1,0 vs 0,7); khi phổi hạn chế thông khí, lượng CO₂ dôi dư này đẩy thẳng bệnh nhân vào toan hô hấp.",
        "B1.03", ["Sinh-ly-benh", "CO2"],
    ),
]
