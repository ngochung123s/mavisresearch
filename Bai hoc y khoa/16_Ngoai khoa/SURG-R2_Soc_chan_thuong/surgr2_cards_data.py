# -*- coding: utf-8 -*-
"""surgr2_cards_data.py — SURG-R2: Sốc Chấn Thương (100% barem 11).
Cấu trúc chuẩn LIGHT_CSS (Dual-mode Light/Dark), 4 màu PALETTE (#ff6b6b, #ffd43b, #51cf66, #74c0fc),
mặt sau 🎯 + 💡, 4 thẻ ⚡ THUẬT TOÁN QUYẾT ĐỊNH, 8 thẻ ❌/🛑 Bẫy & Cờ đỏ, 3 Cloze, phủ 18/18 mã barem.
"""

def _c(hex_color, text):
    return f'<span style="color: {hex_color}; font-weight: 600;">{text}</span>'

def R(t): return _c("#ff6b6b", t)   # Đỏ cảnh báo / ngưỡng bệnh lý / tử vong
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
        "category": f"SURG-R2 · {section}",
        "badge": badge,
        "badge_class": "badge-red" if red_flag else "",
        "front": front,
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R2", section] + tags,
    }

def algo(cid, section, topic, tier, front, core, ai, barem, tags):
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "category": f"SURG-R2 · {section}",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-amber",
        "front": f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {B(topic)}<br>{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R2", section, "Thuat-toan"] + tags,
    }

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False):
    prefix = f"{R('🛑 CỜ ĐỎ')} — " if red_flag else f"{Y('❌ Bẫy lâm sàng')} — "
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": 1,
        "category": f"SURG-R2 · {section}",
        "badge": "🛑 CỜ ĐỎ" if red_flag else "❌ Bẫy lâm sàng",
        "badge_class": "badge-red" if red_flag else "badge-amber",
        "front": f"{prefix}{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R2", section, "Bay-lam-sang"] + tags,
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
        "category": f"SURG-R2 · {section}",
        "badge": "Cloze",
        "badge_class": "badge-blue",
        "text": text,
        "extra": f"[{barem}]",
        "tags": ["SURG-R2", section, "Cloze"] + tags,
    }


cards_data = [
    # =========================================================================
    # B0 — TỔNG QUAN & KHÁI NIỆM
    # =========================================================================
    basic(
        "SURGR2-B0-01", "B0", "Năm mục tiêu thực hành Sốc chấn thương", 2,
        f"{B('[Tổng quan — Mục tiêu học tập]')} Nêu 5 mục tiêu cốt lõi cần đạt khi học và xử trí Sốc chấn thương?",
        f"1) <b>Lý thuyết nền:</b> Trình bày chính xác {B('bản chất sốc chấn thương')}.<br>"
        f"2) <b>Sinh lý:</b> Giải thích chuỗi {Y('bệnh sinh sốc mất máu')} theo từng giai đoạn.<br>"
        f"3) <b>Khám bệnh & Xét nghiệm:</b> Trình bày {B('triệu chứng lâm sàng và cận lâm sàng')} của sốc mất máu.<br>"
        f"4) <b>Xác lập:</b> Chẩn đoán sớm sốc mất máu (phân độ ATLS, FAST).<br>"
        f"5) <b>Chiến lược:</b> Phân tích từng bước {G('xử trí ABCDE, hồi sức và phẫu thuật kiểm soát tổn thương')}.",
        f"Nắm vững trục 5 mục tiêu này giúp bác sĩ ngoại khoa phối hợp nhịp nhàng giữa hồi sức bảo toàn não–tim, cầm máu tạm thời và phá vòng xoắn Tam chứng tử thần.",
        "B0.01", ["Tong-quan"],
    ),
    basic(
        "SURGR2-B0-02", "B0", "Định nghĩa Sốc & Bản chất Sốc chấn thương", 1,
        f"{B('[Khái niệm Sốc chấn thương]')} Phân biệt khái niệm chung của 'Sốc' và định nghĩa đặc thù của 'Sốc chấn thương' (vòng xoắn bệnh lý cốt lõi là gì)?",
        f"1) <b>Sốc chung:</b> Tình trạng suy sụp toàn thân nặng nề với hội chứng {R('suy tuần hoàn cấp tính')}, không đảm bảo đủ tưới máu và oxy cho chuyển hóa tế bào và cơ quan.<br>"
        f"2) <b>Sốc chấn thương:</b> Phản ứng bệnh lý phức tạp có tính chất giai đoạn do {R('chấn thương cơ học mạnh và mất máu cấp tính')}, làm rối loạn chức năng hàng loạt cơ quan (tuần hoàn, thần kinh, hô hấp, nội tiết, chuyển hóa).<br>"
        f"3) <b>Điểm cốt lõi tạo vòng xoắn ác tính:</b> {Y('Rối loạn vi tuần hoàn')} và {R('thiếu oxy tế bào')}.",
        f"Sốc không đơn giản chỉ là 'tụt huyết áp trên máy đo' mà là suy giảm tưới máu và cung cấp oxy cấp tế bào; nếu không cắt đứt vòng xoắn thiếu oxy vi tuần hoàn thì sốc tiến triển nhanh sang giai đoạn không hồi phục.",
        "B0.02", ["Khai-niem"],
    ),

    # =========================================================================
    # B1 — 3 BỆNH CẢNH & PHÂN LOẠI SỐC CHẤN THƯƠNG
    # =========================================================================
    basic(
        "SURGR2-B1-01", "B1", "3 bệnh cảnh sốc thường gặp nhất trong cấp cứu chấn thương", 1,
        f"{B('[Bệnh cảnh lâm sàng]')} Ba bệnh cảnh sốc thường gặp nhất ở bệnh nhân đa chấn thương vào cấp cứu là gì?",
        f"1) <b>Sốc mất máu (Hypovolemic / Hemorrhagic shock):</b> {R('Chiếm đa số')}, do chảy máu trong hoặc ngoài (thuộc nhóm sốc giảm thể tích).<br>"
        f"2) <b>Sốc tắc nghẽn:</b> Do {R('chèn ép tim cấp (Tamponade)')} hoặc {R('tràn khí màng phổi áp lực')}.<br>"
        f"3) <b>Sốc thần kinh / Sốc tủy (Neurogenic shock):</b> Do {Y('tổn thương tủy sống cổ hoặc ngực cao')} gây mất trương lực giao cảm vận mạch.",
        f"Gặp bệnh nhân chấn thương tụt huyết áp, đừng mặc định 100% là chảy máu trong: luôn rà nhanh lồng ngực (Tamponade, tràn khí áp lực) và cột sống cổ/ngực cao (sốc tủy kèm mạch chậm ấm).",
        "B1.01", ["Phan-loai", "Benh-canh"],
    ),
    basic(
        "SURGR2-B1-02", "B1", "Phân loại sốc chấn thương theo Nguyên nhân, Thời gian & Diễn biến", 2,
        f"{B('[Phân loại]')} Sốc chấn thương được phân loại theo 3 trục (Nguyên nhân, Thời gian xuất hiện, Diễn biến lâm sàng) cụ thể như thế nào?",
        f"1) <b>Theo nguyên nhân:</b> Sốc mất máu, Sốc chèn ép tim cấp, Sốc tủy.<br>"
        f"2) <b>Theo thời gian:</b> {Y('Sốc tiên phát')} (ngay sau chấn thương do đau đớn và mất máu cấp) vs {R('Sốc thứ phát')} (sau vài giờ đến vài ngày do chảy máu tái phát, nhiễm trùng, tiêu cơ vân).<br>"
        f"3) <b>Theo diễn biến lâm sàng:</b> Sốc còn bù → Sốc mất bù → {R('Sốc không hồi phục')}.",
        f"Nhận diện sốc thứ phát giúp ta không chủ quan sau khi bệnh nhân qua cơn sốc đầu: chảy máu rỉ rả tái phát, nhiễm trùng vết thương hoặc tiêu cơ vân dập nát cơ đều có thể quật ngã bệnh nhân sau vài giờ đến vài ngày.",
        "B1.02", ["Phan-loai"],
    ),

    # =========================================================================
    # B2 — CƠ CHẾ BỆNH SINH 3 GIAI ĐOẠN CỦA SỐC MẤT MÁU
    # =========================================================================
    basic(
        "SURGR2-B2-01", "B2", "Giai đoạn Sốc còn bù: Phản xạ Giao cảm, Trung tâm hóa & RAAS/ADH", 1,
        f"{B('[Bệnh sinh — Sốc còn bù]')} Hệ thần kinh giao cảm và hệ nội tiết (RAAS, ADH) bù trừ thế nào ở giai đoạn sốc còn bù, và hiện tượng 'trung tâm hóa tuần hoàn' là gì?",
        f"1) <b>Phản xạ áp lực & Catecholamine:</b> Giảm tiền gánh kích thích thụ thể xoang cảnh và quai động mạch chủ (Baroreflexes) → phóng thích {Y('Adrenaline, Noradrenaline')} gây co tiểu ĐM/TM ngoại vi, tăng nhịp & tăng co bóp tim.<br>"
        f"2) <b>Trung tâm hóa tuần hoàn:</b> Co mạch tối đa ở da, cơ vân, xương, tạng ổ bụng nhằm {G('ưu tiên dòng máu nuôi tim và não')}.<br>"
        f"3) <b>Hệ nội tiết RAAS & ADH:</b> Hoạt hóa {B('Renin–Angiotensin–Aldosterone')} + tăng tiết {B('Vasopressin (ADH)')} vùng dưới đồi → giữ muối nước ở ống thận, co tiểu ĐM thận bảo tồn thể tích.",
        f"Chính nhờ hiện tượng trung tâm hóa tuần hoàn mà ở ATLS Độ I và Độ II huyết áp động mạch vẫn còn bình thường dù đã mất tới 15–30% thể tích máu (chỉ lộ qua mạch nhanh và áp lực mạch kẹp).",
        "B2.01", ["Benh-sinh", "Con-bu"],
    ),
    basic(
        "SURGR2-B2-02", "B2", "Giai đoạn Sốc mất bù: Toan Lactic, Liệt cơ thắt tiền mao mạch & MDF", 1,
        f"{B('[Bệnh sinh — Sốc mất bù]')} Khi máu mất > 30–40%, những thay đổi chuyển hóa, cơ thắt mao mạch và yếu tố ức chế cơ tim nào đẩy sốc sang mất bù?",
        f"1) <b>Chuyển hóa kỵ khí & Toan máu:</b> Mất máu quá {R('> 30 – 40%')} hoặc kéo dài → tích tụ {R('Axit Lactic gây toan chuyển hóa nặng')}.<br>"
        f"2) <b>Nghịch lý cơ thắt vi tuần hoàn:</b> Toan máu làm {R('liệt cơ thắt tiền mao mạch trong khi cơ thắt sau mao mạch vẫn co')} → máu ứ trệ mạng vi tuần hoàn, tăng tính thấm thoát dịch & protein ra mô kẽ.<br>"
        f"3) <b>Suy bơm cơ tim:</b> Xuất hiện {Y('yếu tố ức chế cơ tim (MDF)')} làm giảm co bóp và giảm cung lượng tim trầm trọng hơn.",
        f"Hiện tượng tiền mao mạch mở toang nhưng hậu mao mạch đóng chặt biến giường mao mạch thành 'đầm lầy ứ máu', vừa làm mất thêm dịch vào kẽ vừa cướp đi lượng máu hồi lưu về tim.",
        "B2.02", ["Benh-sinh", "Mat-bu"],
    ),
    basic(
        "SURGR2-B2-03", "B2", "Giai đoạn Sốc không hồi phục: DIC, Cạn ATP & Suy đa tạng MODS", 2,
        f"{R('[Bệnh sinh — Sốc không hồi phục]')} Vì sao ở giai đoạn sốc không hồi phục dù nâng được huyết áp tạm thời bệnh nhân vẫn tử vong?",
        f"1) <b>Đổ vỡ tế bào & Vi mạch:</b> Giãn mạch toàn thân trơ vận mạch, {R('đông máu nội mạch rải rác (DIC)')}, {R('cạn kiệt dự trữ năng lượng ATP')}, tổn thương màng tế bào không thể đảo ngược.<br>"
        f"2) <b>Hoại tử cơ quan đích:</b> Não, tim, phổi, thận, gan đã hoại tử không hồi phục → tử vong sau vài giờ hoặc vài ngày do {R('suy đa tạng (MODS)')}.",
        f"Đây là ranh giới chết chóc giải thích vì sao phải cầm máu và hồi sức cân bằng sớm ngay giờ vàng chứ không thể đợi tụt huyết áp sâu mới cứu.",
        "B2.03", ["Benh-sinh", "Khong-hoi-phuc"], red_flag=True,
    ),

    # =========================================================================
    # B3 — PHÂN ĐỘ MẤT MÁU THEO ATLS (ĐỘ I – ĐỘ IV)
    # =========================================================================
    basic(
        "SURGR2-B3-01", "B3", "Phân độ mất máu ATLS: Độ I (Nhẹ) vs Độ II (Vừa)", 1,
        f"{B('[Phân độ ATLS — Độ I & II]')} Nêu các thông số lượng máu mất (ml và %), mạch, huyết áp, hiệu số HA, thở, nước tiểu, tâm thần và dịch bù của Độ I và Độ II?",
        f"1) <b>Độ I (Nhẹ):</b> Mất {G('< 750 ml (< 15%)')}, mạch {G('< 100/ph')}, HA & hiệu số HA bình thường/tăng, thở 14–20, nước tiểu {G('> 30 ml/h')}, lo lắng nhẹ → bù {G('dịch tinh thể')}.<br>"
        f"2) <b>Độ II (Vừa):</b> Mất {Y('750 – 1500 ml (15 – 30%)')}, mạch {Y('> 100/ph')}, HA tâm thu bình thường nhưng {Y('áp lực mạch giảm (HA kẹp)')}, thở 20–30, nước tiểu {Y('20 – 30 ml/h')}, lo lắng vừa → bù {G('dịch tinh thể')}.",
        f"Dấu hiệu sớm nhất báo động mất máu Độ II khi huyết áp tâm thu chưa tụt là mạch vượt > 100 lần/phút và hiệu số huyết áp thu hẹp (HA kẹp).",
        "B3.01", ["ATLS", "Phan-do"],
    ),
    basic(
        "SURGR2-B3-02", "B3", "Phân độ mất máu ATLS: Độ III (Nặng) vs Độ IV (Nguy kịch)", 1,
        f"{R('[Phân độ ATLS — Độ III & IV]')} Phân biệt rạch ròi Độ III (Nặng) và Độ IV (Nguy kịch) về lượng máu mất (ml, %), mạch, huyết áp, thở, nước tiểu, tâm thần và chỉ định truyền máu?",
        f"1) <b>Độ III (Nặng):</b> Mất {R('1500 – 2000 ml (30 – 40%)')}, mạch {R('> 120/ph')}, {R('tụt huyết áp')}, áp lực mạch giảm nặng, thở 30–40, nước tiểu {R('5 – 15 ml/h (thiểu niệu)')}, kích thích lú lẫn → {Y('Dịch tinh thể + Máu')}.<br>"
        f"2) <b>Độ IV (Nguy kịch):</b> Mất {R('> 2000 ml (> 40%)')}, mạch {R('> 140/ph')}, tụt sâu/không đo được, mất áp lực mạch, thở > 35 (thở ngáp), {R('vô niệu (< 5 ml/h)')}, lờ đờ hôn mê → {R('Truyền máu tối khẩn')}.",
        f"Độ III là bước ngoặt bắt đầu sụp cơ chế bù trừ khiến huyết áp tâm thu tụt xuống và bắt buộc phải bổ sung máu; sang Độ IV nước tiểu gần như bằng 0 (< 5 ml/h) và bệnh nhân cận kề ngừng tim nếu không truyền máu tối khẩn.",
        "B3.02", ["ATLS", "Phan-do"], red_flag=True,
    ),
    cloze(
        "SURGR2-B3-03", "B3", "Cloze: Toàn bộ mốc số Phân độ mất máu ATLS (Độ I → IV)",
        f"{B('[Phân độ ATLS]')} Mất máu Độ I tương ứng lượng máu mất {clz(1, G('< 750 ml (< 15%)'))} với mạch < 100 và nước tiểu > 30 ml/h. Độ II mất {clz(2, Y('750 – 1500 ml (15 – 30%)'))} kèm mạch {clz(3, Y('> 100/phút'))} và huyết áp kẹp. Độ III mất {clz(4, R('1500 – 2000 ml (30 – 40%)'))} khiến mạch {clz(5, R('> 120/phút'))} kèm tụt huyết áp và thiểu niệu {clz(6, R('5 – 15 ml/giờ'))}. Độ IV mất {clz(7, R('> 2000 ml (> 40%)'))} kèm mạch > 140 và vô niệu {clz(8, R('< 5 ml/giờ'))}.",
        "B3.01, B3.02", ["ATLS", "Cloze"],
    ),

    # =========================================================================
    # B4 — TIẾP CẬN ABCDE & SIÊU ÂM FAST TẠI GIƯỜNG
    # =========================================================================
    basic(
        "SURGR2-B4-01", "B4", "5 bước tiếp cận ban đầu theo trình tự ABCDE trong chấn thương", 1,
        f"{B('[Xử trí — ABCDE]')} Trình bày nội dung hành động cụ thể trong 5 bước A–B–C–D–E cấp cứu ban đầu bệnh nhân sốc chấn thương?",
        f"1) <b>A (Airway + cervical spine):</b> Kiểm soát đường thở kết hợp {R('cố định cột sống cổ (nẹp cổ cứng)')}.<br>"
        f"2) <b>B (Breathing):</b> Thở oxy lưu lượng cao {G('10 – 15 lít/phút qua mask túi dự trữ')}; xử trí ngay tràn khí áp lực, tràn máu màng phổi, mảng sườn di động.<br>"
        f"3) <b>C (Circulation + hemorrhage control):</b> Băng ép, chèn gạc, garô, {G('nẹp khung chậu / xương gãy lớn')} song song bù dịch.<br>"
        f"4) <b>D (Disability):</b> Chấm nhanh {B('Glasgow')} và phản xạ đồng tử.<br>"
        f"5) <b>E (Exposure / Environment):</b> Bộc lộ tìm tổn thương và {Y('ủ ấm tích cực phòng hạ thân nhiệt')}.",
        f"Trong ABCDE chấn thương, 'A' luôn gắn kèm cố định cổ và 'C' luôn gắn kèm cầm máu ngoài / nẹp bất động khung chậu–xương đùi ngay song song truyền dịch, còn 'E' nhấn mạnh ủ ấm để tránh rơi vào Tam chứng tử thần.",
        "B4.01", ["ABCDE", "Cap-cuu"],
    ),
    basic(
        "SURGR2-B4-02", "B4", "Siêu âm FAST tại giường (2 phút) vs Chống chỉ định chụp MSCT", 1,
        f"{G('[Chẩn đoán tại giường — FAST]')} Ở bệnh nhân sốc mất máu nghi chấn thương bụng kín có huyết động không ổn định, phương tiện cận lâm sàng nào hữu ích nhất và vì sao?",
        f"1) <b>Phương tiện số 1 tại giường:</b> {G('Siêu âm FAST ngực – bụng tại giường')}.<br>"
        f"2) <b>Ưu điểm quyết định:</b> Xác định nhanh {B('dịch tự do ổ bụng / màng tim')} chỉ trong {G('vòng 2 phút')} ngay tại phòng cấp cứu mà {G('không phải di chuyển bệnh nhân')}.<br>"
        f"3) <b>Thủ thuật cấm làm lúc này:</b> Không đẩy bệnh nhân đi chụp {R('MSCT ngực – bụng')} khi huyết động chưa ổn định.",
        f"Cái chết thường xảy ra ở 'hành lang hoặc trong buồng chụp CT' (the tunnel of death) khi đẩy người bệnh đang tụt huyết áp đi chụp cắt lớp; siêu âm FAST thấy dịch tự do + sốc mất máu = chỉ định mở bụng cầm máu ngay.",
        "B4.02", ["FAST", "Can-lam-sang"],
    ),

    # =========================================================================
    # B5 — ĐƯỜNG TRUYỀN, PERMISSIVE HYPOTENSION & TRUYỀN MÁU MTP 1:1:1
    # =========================================================================
    basic(
        "SURGR2-B5-01", "B5", "2 đường truyền lớn 14G–16G & Giới hạn dịch tinh thể ấm 1000–1500 ml", 1,
        f"{B('[Hồi sức — Đường truyền & Dịch]')} Thiết lập đường truyền nào ngay lập tức ở cấp cứu chấn thương, và tại sao chỉ khởi đầu tinh thể ấm giới hạn 1000–1500 ml?",
        f"1) <b>Đường truyền:</b> Đặt ngay {G('2 đường truyền ngoại vi khẩu kính lớn (14G – 16G)')} ở hai chi trên hoặc tĩnh mạch cảnh ngoài / tĩnh mạch bẹn; {R('không làm chậm trễ cấp cứu để đặt catheter TM trung tâm')}.<br>"
        f"2) <b>Dịch tinh thể khởi đầu:</b> Dung dịch tinh thể cân bằng ấm ({G('Ringer Lactat, Ringerfundin hoặc NaCl 0,9%')}) thể tích giới hạn {Y('1000 – 1500 ml')}.<br>"
        f"3) <b>Hạn chế truyền lượng lớn:</b> Truyền quá nhiều tinh thể gây {R('toan máu do Clo cao')} và {R('pha loãng các yếu tố đông máu')}.",
        f"Bơm hàng lít nước muối NaCl 0,9% lạnh ngắt trước khi cầm máu không những làm pha loãng tiểu cầu/yếu tố đông máu mà còn gây toan chuyển hóa tăng Clo và hạ thân nhiệt (Tam chứng tử thần).",
        "B5.01", ["Hoi-suc", "Bu-dich"],
    ),
    basic(
        "SURGR2-B5-02", "B5", "Hạ huyết áp cho phép (Permissive Hypotension) & Ngoại lệ Sọ não / Tủy sống", 1,
        f"{B('[Hồi sức — Permissive Hypotension]')} Ngưỡng huyết áp của chiến lược 'Hạ huyết áp cho phép' khi chưa cầm máu phẫu thuật là bao nhiêu và ngoại lệ bắt buộc khi có CTSN / tổn thương tủy?",
        f"1) <b>Khi chưa cầm máu ngoại khoa:</b> Chỉ duy trì {Y('HATT 80 – 90 mmHg')} (hoặc {Y('MAP ≥ 65 mmHg')}) để tưới máu tạng tối thiểu, tránh {R('bật cục máu đông')} gây chảy máu ồ ạt tái phát và pha loãng máu.<br>"
        f"2) <b>Ngoại lệ Chấn thương sọ não hoặc tổn thương tủy sống kèm theo:</b> Bắt buộc duy trì {R('MAP ≥ 80 – 90 mmHg (HATT ≥ 100 – 110 mmHg)')} để bảo đảm áp lực tưới máu não ({B('CPP = MAP − ICP')}).",
        f"Nếu cố kéo HATT lên 120–130 mmHg trong lúc mạch máu nội tạng chưa được khâu kẹp, áp lực dòng máu cao sẽ thổi bay cục máu đông mới hình thành khiến bệnh nhân chảy máu ồ ạt hơn. Riêng não bị chấn thương tăng áp lực nội sọ (ICP) cần MAP cao hơn để tránh thiếu máu não thứ phát.",
        "B5.02", ["Permissive-Hypotension", "CTSN"],
    ),
    basic(
        "SURGR2-B5-03", "B5", "Quy trình truyền máu khối lượng lớn (MTP 1:1:1) & Nhóm máu O Rh−", 1,
        f"{B('[Hồi sức — Truyền máu MTP]')} Khi nào kích hoạt Truyền máu khối lượng lớn (MTP), chọn nhóm máu khẩn cấp nào, tỷ lệ cân bằng mấy:mấy:mấy và đích Hct/Hb (thường vs CTSN)?",
        f"1) <b>Đối tượng áp dụng MTP:</b> Mất máu {R('Độ III, Độ IV')} hoặc sốc mất máu tiến triển.<br>"
        f"2) <b>Nhóm máu khẩn (chưa kịp định nhóm):</b> Dùng nhóm {R('O âm tính (O Rh−)')}.<br>"
        f"3) <b>Công thức cân bằng 1:1:1:</b> {G('1 Hồng cầu khối : 1 Huyết tương tươi đông lạnh (FFP) : 1 Đơn vị tiểu cầu')} nhằm ngăn rối loạn đông máu sớm.<br>"
        f"4) <b>Đích cần đạt:</b> {G('Hematocrit 25 – 30% (Hb ≥ 80 – 90 g/L)')}; nếu có chấn thương sọ não phải duy trì {B('Hct > 30% (Hb > 100 g/L)')}.",
        f"Tỷ lệ 1:1:1 mô phỏng gần nhất thành phần máu toàn phần sinh lý giúp cung cấp song song hồng cầu vận chuyển oxy, yếu tố đông máu (FFP) và tiểu cầu ngay từ những đơn vị máu đầu tiên.",
        "B5.03", ["MTP", "Truyen-mau"],
    ),
    cloze(
        "SURGR2-B5-04", "B5", "Cloze: Ngưỡng Huyết áp cho phép, MTP 1:1:1 & Tam chứng tử thần",
        f"{B('[Chiến lược hồi sức chấn thương]')} Đặt ngay 2 đường truyền ngoại vi cỡ lớn {clz(1, G('14G – 16G'))} và giới hạn tinh thể cân bằng ấm ban đầu {clz(2, Y('1000 – 1500 ml'))}. Khi chưa phẫu thuật cầm máu thì giữ HATT cho phép ở mức {clz(3, Y('80 – 90 mmHg'))}. Khi có chấn thương sọ não đi kèm phải nâng lên {clz(4, R('MAP ≥ 80 – 90 mmHg (HATT ≥ 100 – 110 mmHg)'))}. Máu cấp cứu khi chưa kịp định nhóm dùng nhóm {clz(5, R('O âm tính (O Rh−)'))}. Tỷ lệ truyền máu khối lượng lớn hiện đại là {clz(6, G('1 Hồng cầu khối : 1 FFP : 1 Tiểu cầu (1:1:1)'))}. Đích hematocrit sau cầm máu ổn định là {clz(7, G('> 25% (Hb ≥ 80 – 90 g/L)'))} và nước tiểu {clz(8, G('> 0,5 ml/kg/giờ'))}.",
        "B5.01, B5.02, B5.03, B7.01", ["Hoi-suc", "MTP", "Cloze"],
    ),

    # =========================================================================
    # B6 — TAM CHỨNG TỬ THẦN & PHẪU THUẬT KIỂM SOÁT TỔN THƯƠNG (DCS)
    # =========================================================================
    basic(
        "SURGR2-B6-01", "B6", "Tam chứng tử thần trong chấn thương (Lethal Triad of Trauma)", 1,
        f"{R('[Báo động — Tam chứng tử thần]')} 'Tam chứng tử thần' (Lethal Triad of Trauma) ở bệnh nhân đa chấn thương gồm 3 rối loạn nào với các ngưỡng giá trị cụ thể?",
        f"1) <b>Hạ thân nhiệt:</b> Nhiệt độ cơ thể {R('< 35°C')} (làm tê liệt các men đông máu).<br>"
        f"2) <b>Toan chuyển hóa:</b> Khí máu {R('pH < 7,2')} (ức chế co bóp cơ tim và hoạt tính yếu tố đông máu).<br>"
        f"3) <b>Rối loạn đông máu (Coagulopathy):</b> Máu chảy không cầm do pha loãng, tiêu thụ và bất hoạt men đông máu.",
        f"Ba đỉnh của tam giác này khuếch đại lẫn nhau thành vòng xoắn tử thần: hạ thân nhiệt và toan hóa làm bất hoạt thác đông máu → chảy máu nhiều hơn → truyền dịch lạnh làm hạ thân nhiệt và toan hóa nặng hơn nữa.",
        "B6.01", ["Tam-chung-tu-than"], red_flag=True,
    ),
    basic(
        "SURGR2-B6-02", "B6", "3 biện pháp cắt Tam chứng tử thần: Ủ ấm, Canxi Clorid & Damage Control Surgery", 1,
        f"{B('[Điều trị — Phá Tam chứng tử thần]')} Ba biện pháp chủ lực giúp cắt đứt Tam chứng tử thần (bao gồm liều Canxi clorid theo túi máu và triết lý mổ DCS) là gì?",
        f"1) <b>Chống hạ thân nhiệt:</b> Ủ ấm bệnh nhân và dùng máy {G('sưởi ấm dịch truyền và máu')} trước khi truyền vào cơ thể.<br>"
        f"2) <b>Bổ sung Canxi chống hạ Canxi do Citrate:</b> Tiêm {Y('Canxi clorid 1 g sau mỗi 4 đơn vị máu truyền')} (do chất chống đông Citrate trong túi máu gắn kết làm tụt Canxi máu).<br>"
        f"3) <b>Phẫu thuật kiểm soát tổn thương (DCS):</b> Chỉ {R('mổ cầm máu tạm thời và đóng bụng nhanh')}, chuyển ngay về hồi sức tích cực ổn định huyết động trước khi mổ triệt để thì 2.",
        f"Canxi ion hóa (yếu tố IV) là đồng yếu tố thiết yếu của toàn bộ thác đông máu và sức co bóp cơ tim; thiếu Canxi do truyền máu khối lượng lớn giàu Citrate làm máu khó đông và tụt huyết áp kháng vận mạch.",
        "B6.02", ["Tam-chung-tu-than", "DCS", "Canxi"],
    ),
    cloze(
        "SURGR2-B6-03", "B6", "Cloze: Ngưỡng Tam chứng tử thần, Canxi clorid & Triết lý DCS",
        f"{R('[Tam chứng tử thần]')} Tam chứng tử thần trong chấn thương khởi phát với hạ thân nhiệt {clz(1, R('< 35°C'))}. Thành phần thứ hai trong tam chứng tử thần là toan chuyển hóa {clz(2, R('pH < 7,2'))} đi kèm rối loạn đông máu. Chất chống đông trong túi máu gây hạ Canxi máu là {clz(3, Y('Citrate'))}. Cần bổ sung {clz(4, Y('Canxi clorid 1 g'))} sau mỗi {clz(5, B('4 đơn vị máu truyền'))}. Mục đích của Phẫu thuật kiểm soát tổn thương (DCS) là chỉ {clz(6, G('mổ cầm máu tạm thời và đóng bụng nhanh'))} rồi chuyển hồi sức trước khi mổ thì 2.",
        "B6.01, B6.02", ["Tam-chung-tu-than", "DCS", "Cloze"],
    ),

    # =========================================================================
    # B7 — ĐÍCH HỒI SỨC SAU CẦM MÁU
    # =========================================================================
    basic(
        "SURGR2-B7-01", "B7", "3 Đích điều trị sau phẫu thuật cầm máu ổn định", 1,
        f"{G('[Đích hồi sức sau cầm máu]')} Khi nguồn chảy máu đã được phẫu thuật cầm máu ổn định, 3 thông số đích (MAP, Hct/Hb, Nước tiểu) cần duy trì là gì?",
        f"1) <b>Huyết áp động mạch trung bình:</b> {G('MAP ≥ 65 mmHg')}.<br>"
        f"2) <b>Hematocrit & Hemoglobin:</b> {G('Hematocrit > 25%')} (kèm {G('Hb ≥ 80 – 90 g/L')}; giữ > 30% / > 100 g/L nếu kèm CTSN).<br>"
        f"3) <b>Bài niệu:</b> Lượng nước tiểu {G('> 0,5 ml/kg/giờ')}.",
        f"Sau khi phẫu thuật viên đã thắt mạch/cầm máu chắc chắn, mục tiêu không còn là 'hạ huyết áp cho phép' nữa mà phải kéo MAP ≥ 65 mmHg và theo dõi sát nước tiểu > 0,5 ml/kg/giờ để hồi phục hoàn toàn tưới máu thận và các tạng.",
        "B7.01", ["Dich-hoi-suc", "Luong-gia"],
    ),

    # =========================================================================
    # 4 THẺ ⚡ THUẬT TOÁN QUYẾT ĐỊNH
    # =========================================================================
    algo(
        "SURGR2-ALGO-01", "B4", "Tiếp cận 5 phút đầu ABCDE + Siêu âm FAST tại giường", 1,
        f"Bệnh nhân tai nạn giao thông đa chấn thương vào cấp cứu da lạnh vã mồ hôi, HA tụt — Quy trình hành động theo trục ABCDE & Chẩn đoán hình ảnh tại giường?",
        f"1) <b>A–B (Thở & Cổ):</b> Nẹp cố định cổ cứng, khai thông đường thở, thở oxy mask túi {G('10 – 15 L/phút')}, giải áp ngay nếu có tràn khí áp lực / tràn máu màng phổi / mảng sườn.<br>"
        f"2) <b>C (Cầm máu & Đường truyền):</b> Băng ép cầm máu ngoài, nẹp khung chậu/xương gãy lớn + đặt {G('2 đường truyền ngoại vi 14G–16G')}, truyền giới hạn {Y('1000 – 1500 ml tinh thể cân bằng ấm')}.<br>"
        f"3) <b>Tại giường (Không đẩy đi CT):</b> Thực hiện ngay {G('Siêu âm FAST ngực – bụng trong 2 phút')} tìm dịch ổ bụng / màng tim.<br>"
        f"4) <b>D–E (Não & Thân nhiệt):</b> Chấm Glasgow, bộc lộ toàn thân và {Y('ủ ấm tích cực tránh hạ thân nhiệt < 35°C')}.",
        f"Điểm vàng của quy trình là tính song hành: trong vòng 2–5 phút đầu vừa có đường truyền lớn, vừa nẹp cổ–nẹp xương, vừa có câu trả lời từ FAST tại giường mà bệnh nhân không phải rời phòng cấp cứu nửa bước.",
        "B4.01, B4.02, B5.01", ["ABCDE", "FAST", "Cap-cuu"],
    ),
    algo(
        "SURGR2-ALGO-02", "B5", "Quyết định ngưỡng Huyết áp cho phép & Truyền máu MTP 1:1:1", 1,
        f"Bệnh nhân mất máu ATLS Độ III–IV chưa kịp lên bàn mổ cầm máu — Cách chọn ngưỡng huyết áp đích và phác đồ truyền máu khẩn cấp?",
        f"1) <b>Phân tầng sọ não / tủy trước khi chỉnh áp:</b><br>"
        f"   • Không có CTSN / tổn thương tủy: Giữ {Y('HATT 80 – 90 mmHg (MAP ≥ 65 mmHg)')} tránh bật cục máu đông.<br>"
        f"   • Có CTSN hoặc tổn thương tủy kèm theo: Nâng bắt buộc {R('MAP ≥ 80 – 90 mmHg (HATT ≥ 100 – 110 mmHg)')} bảo đảm CPP = MAP − ICP.<br>"
        f"2) <b>Kích hoạt MTP (Độ III–IV):</b> Dùng khẩn máu nhóm {R('O Rh−')} nếu chưa kịp định nhóm, truyền theo tỷ lệ {G('1 HC khối : 1 FFP : 1 Tiểu cầu (1:1:1)')}.<br>"
        f"3) <b>Bổ sung chống đông tụt Canxi:</b> Tiêm {Y('Canxi clorid 1 g sau mỗi 4 đơn vị máu truyền')}.",
        f"Hai quyết định này quyết định sống còn trước dao mổ: giữ áp lực vừa đủ không thổi bật cục máu đông (nhưng nâng cao nếu có CTSN) và cấp đủ bộ ba hồng cầu–huyết tương–tiểu cầu để máu không bị loãng thành nước.",
        "B3.02, B5.02, B5.03, B6.02", ["Permissive-Hypotension", "MTP"],
    ),
    algo(
        "SURGR2-ALGO-03", "B6", "Quyết định Phẫu thuật Kiểm soát tổn thương (DCS) khi dọa Tam chứng tử thần", 1,
        f"Trên bàn mổ vỡ gan/vỡ lách nặng, bệnh nhân tụt nhiệt độ 34,5°C, pH 7,15 và máu rỉ khắp phẫu trường — Quy trình xử trí theo chiến lược DCS?",
        f"1) <b>Xác nhận Tam chứng tử thần:</b> Đã chạm ngưỡng {R('Hạ thân nhiệt < 35°C')}, {R('Toan máu pH < 7,2')} và {R('Rối loạn đông máu')}.<br>"
        f"2) <b>Dừng mổ triệt để kéo dài:</b> Thực hiện {G('Phẫu thuật kiểm soát tổn thương (DCS)')} — chỉ cầm máu tạm thời (chèn gạc, kẹp/buộc nhanh mạch lớn) và đóng bụng tạm nhanh.<br>"
        f"3) <b>Chuyển ICU phá Tam chứng:</b> Ủ ấm chủ động, máy sưởi máu/dịch, bù Canxi clorid 1 g/4 ĐV máu, truyền MTP 1:1:1 ổn định huyết động trước khi {B('mổ triệt để thì 2')}.",
        f"Cố gắng khâu nối tỉ mỉ 3–4 tiếng khi bệnh nhân đã rơi vào Tam chứng tử thần chỉ làm bệnh nhân tử vong ngay trên bàn mổ vì rối loạn đông máu toàn thể.",
        "B6.01, B6.02", ["DCS", "Tam-chung-tu-than"],
    ),
    algo(
        "SURGR2-ALGO-04", "B1", "Phân biệt nhanh 3 bệnh cảnh Sốc Chấn thương ngay tại giường", 2,
        f"Cùng tụt huyết áp sau tai nạn giao thông — Làm sao phân tách nhanh Sốc mất máu, Sốc chèn ép tim / tràn khí áp lực và Sốc tủy?",
        f"1) <b>Sốc mất máu (chiếm đa số):</b> Da nhợt lạnh ẩm, tĩnh mạch cổ {Y('xẹp')}, {R('mạch nhanh')}, FAST có dịch ổ bụng hoặc mất máu khung chậu/xương lớn.<br>"
        f"2) <b>Sốc tắc nghẽn (Chèn ép tim cấp / Tràn khí áp lực):</b> Tĩnh mạch cổ {R('nổi căng')}, tụt HA nhanh + tiếng tim mờ (hoặc mất rì rào phế nang, khí quản lệch) → dẫn lưu/giải áp khẩn.<br>"
        f"3) <b>Sốc tủy (Tổn thương tủy cổ / ngực cao):</b> Mất trương lực giao cảm vận mạch → tụt HA nhưng {B('mạch chậm, da ấm hồng')} kèm liệt/mất cảm giác từ ngang mức tổn thương.",
        f"Nhìn tĩnh mạch cổ (xẹp vs nổi) và bắt tần số mạch (nhanh vs chậm) giúp phân định đúng ngay loại sốc để không truyền nhầm quá nhiều dịch cho Tamponade hay bỏ sót chấn thương cột sống cổ.",
        "B1.01, B1.02", ["Phan-biet", "Chan-doan"],
    ),

    # =========================================================================
    # 8 THẺ ❌ BẪY LÂM SÀNG & 🛑 CỜ ĐỎ (GỒM ĐẦY ĐỦ 4 CÂU LƯỢNG GIÁ)
    # =========================================================================
    trap(
        "SURGR2-TRAP-01", "B1", "Đưa 'Sốc phản vệ' vào danh sách 3 bệnh cảnh Sốc chấn thương (Câu 1)",
        f"Trong câu hỏi về các bệnh cảnh lâm sàng thường gặp của sốc chấn thương (Sốc mất máu, Sốc giảm thể tích, Sốc chèn ép tim cấp, Sốc thần kinh/tủy, Sốc phản vệ) — Phương án nào là bẫy sai?",
        f"1) <b>Phương án sai (Bẫy):</b> {R('Sốc phản vệ')} KHÔNG phải bệnh cảnh sốc do chấn thương cơ học gây ra.<br>"
        f"2) <b>Bốn đáp án đúng trong lượng giá:</b> {G('Sốc mất máu')} (chiếm đa số), {G('Sốc giảm thể tích')} (cùng nhóm), {G('Sốc do chèn ép tim cấp')} (Tamponade) và {G('Sốc thần kinh / sốc tủy')}.",
        f"Sốc phản vệ thuộc nhóm sốc phân bố do dị ứng phản ứng quá mẫn thuốc/dị nguyên (có thể gặp tai biến khi tiêm kháng sinh/thuốc cản quang nhưng không phải bệnh cảnh đặc trưng của chấn thương).",
        "B1.01, B7.02", ["Phan-loai", "Luong-gia"],
    ),
    trap(
        "SURGR2-TRAP-02", "B3", "Nhầm lẫn ngưỡng ATLS Độ III với Độ II và Độ IV trong đề thi (Câu 2)",
        f"Với bệnh nhân mất máu ATLS Độ III: Tại sao cặp 'Mạch > 100, tụt HA', 'Vô niệu' và 'Mất máu > 40%' đều là đáp án sai?",
        f"1) <b>Đặc trưng chuẩn của ATLS Độ III:</b> Thể tích máu mất {R('30 – 40% (1500 – 2000 ml)')}, tần số tim {R('> 120 lần/phút')}, {R('huyết áp tụt')} và nước tiểu {R('5 – 15 ml/giờ (thiểu niệu)')}.<br>"
        f"2) <b>Bóc từng bẫy sai:</b> Mạch > 100 là mốc Độ II; {Y('> 40%')} và {Y('vô niệu (< 5 ml/giờ)')} là ranh giới của Độ IV.",
        f"Độ III là 'điểm rơi' chính thức của tụt huyết áp trên lâm sàng kèm mạch > 120/phút và mất máu > 30% (nhưng chưa vượt 40% hay vô niệu hoàn toàn như Độ IV).",
        "B3.02, B7.02", ["ATLS", "Luong-gia"],
    ),
    redflag(
        "SURGR2-TRAP-03", "B4", "Đẩy bệnh nhân sốc mất máu huyết động không ổn định đi chụp MSCT bụng (Câu 3)",
        f"Bệnh nhân chấn thương bụng kín đang tụt huyết áp 75/45 mmHg, mạch 132 — Sai lầm chết người nào xảy ra nếu ra y lệnh chụp MSCT ngực–bụng hay đưa xuống phòng siêu âm?",
        f"1) <b>Y lệnh cấm tuyệt đối:</b> {R('Cấm chụp MSCT ngực – bụng')} hoặc di chuyển bệnh nhân khi huyết động không ổn định.<br>"
        f"2) <b>Phương tiện đúng duy nhất tại giường:</b> {G('Siêu âm FAST ngực – bụng tại giường')} (phát hiện dịch tự do ổ bụng / màng tim trong {G('vòng 2 phút')} không cần di chuyển).",
        f"Vận chuyển bệnh nhân đang chảy máu ồ ạt vào phòng CT làm mất kiểm soát hồi sức và có thể khiến nạn nhân ngừng tim ngay trong máy chụp.",
        "B4.02, B7.02", ["FAST", "Cap-cuu", "Luong-gia"],
    ),
    trap(
        "SURGR2-TRAP-04", "B7", "Nhầm mục tiêu MAP > 50 mmHg hoặc Hematocrit > 20% sau phẫu thuật cầm máu (Câu 4)",
        f"Sau khi phẫu thuật cầm máu ổn định cho bệnh nhân sốc mất máu, tại sao các ngưỡng 'MAP > 50 mmHg' và 'Hematocrit > 20%' không đạt yêu cầu hồi sức?",
        f"1) <b>Ba đích bắt buộc phải đạt:</b> {G('MAP ≥ 65 mmHg')}, {G('Hematocrit > 25% (Hb ≥ 80 – 90 g/L)')} và {G('lượng nước tiểu > 0,5 ml/kg/giờ')}.<br>"
        f"2) <b>Nguy cơ nếu để MAP > 50 hoặc Hct > 20%:</b> Không đủ áp lực tưới máu lọc cầu thận, tưới máu mạch vành và thiếu oxy mô kéo dài gây hoại tử ống thận / suy đa tạng.",
        f"MAP 50 mmHg nằm dưới ngưỡng tự điều hòa tưới máu của cả thận lẫn não; còn Hct ≤ 20% làm giảm nặng khả năng mang oxy lẫn độ nhớt hỗ trợ đông máu.",
        "B7.01, B7.02", ["Dich-hoi-suc", "Luong-gia"],
    ),
    redflag(
        "SURGR2-TRAP-05", "B5", "Áp dụng 'Hạ huyết áp cho phép (HATT 80–90)' cho bệnh nhân đa chấn thương có Chấn thương sọ não",
        f"Bệnh nhân vỡ lách kèm Chấn thương sọ não nặng (Glasgow 7) — Nếu máy móc duy trì HATT 80–90 mmHg theo Permissive Hypotension thì gây hậu quả thảm khốc gì cho não?",
        f"1) <b>Thảm họa thiếu máu não thứ phát:</b> HATT 80–90 mmHg khiến áp lực tưới máu não ({B('CPP = MAP − ICP')}) sụt giảm nghiêm trọng khi áp lực nội sọ (ICP) đang tăng cao.<br>"
        f"2) <b>Ngoại lệ bắt buộc khi có CTSN / Tổn thương tủy:</b> Phải duy trì {R('MAP ≥ 80 – 90 mmHg (HATT ≥ 100 – 110 mmHg)')} và nâng đích {G('Hct > 30% (Hb > 100 g/L)')}.",
        f"Não bị chấn thương mất khả năng tự điều hòa mạch máu nên cực kỳ nhạy cảm với tụt huyết áp; chỉ một cơn tụt HATT < 90 mmHg cũng nhân đôi tỷ lệ tử vong ở bệnh nhân CTSN nặng.",
        "B5.02, B5.03", ["CTSN", "Permissive-Hypotension"],
    ),
    trap(
        "SURGR2-TRAP-06", "B5", "Loay hoay đặt Catheter tĩnh mạch trung tâm trước hoặc bơm 3–4 lít NaCl 0,9% lạnh",
        f"Tại phòng cấp cứu chấn thương, hai thói quen sai lầm làm mất giờ vàng và thúc đẩy rối loạn đông máu khi thiết lập đường truyền và bù dịch là gì?",
        f"1) <b>Trì hoãn đường truyền:</b> Tuyệt đối {R('không làm chậm trễ cấp cứu để đặt catheter tĩnh mạch trung tâm')} — phải đặt ngay {G('2 đường truyền ngoại vi khẩu kính lớn (14G – 16G)')}.<br>"
        f"2) <b>Lạm dụng dịch tinh thể:</b> Chỉ khởi đầu tinh thể cân bằng ấm {Y('1000 – 1500 ml')}; truyền khối lượng lớn gây {R('toan máu do Clo cao')} và {R('pha loãng yếu tố đông máu')}.",
        f"Kim ngoại vi 14G–16G ngắn cho tốc độ truyền chảy nhanh hơn nhiều so với catheter tĩnh mạch trung tâm nòng dài; còn bơm quá nhiều dịch tinh thể lạnh sẽ kích hoạt thẳng Tam chứng tử thần.",
        "B5.01", ["Bu-dich", "Duong-truyen"],
    ),
    trap(
        "SURGR2-TRAP-07", "B6", "Truyền máu khối lượng lớn toàn Hồng cầu khối hoặc quên tiêm Canxi clorid",
        f"Khi truyền khẩn cấp 8 đơn vị hồng cầu khối liên tục mà không truyền kèm FFP/tiểu cầu và không bù Canxi clorid — Bệnh nhân sẽ gục ngã vì biến chứng gì?",
        f"1) <b>Đông máu loãng & tiêu thụ:</b> Truyền hồng cầu khối đơn độc không theo tỷ lệ {G('1 HC khối : 1 FFP : 1 Tiểu cầu (1:1:1)')} gây rối loạn đông máu nặng.<br>"
        f"2) <b>Hạ Canxi máu do Citrate:</b> Chất chống đông {Y('Citrate')} trong túi máu gắp mất Canxi → bắt buộc tiêm {G('Canxi clorid 1 g sau mỗi 4 đơn vị máu truyền')}.",
        f"Hạ Canxi máu vừa làm rối loạn thác đông máu nội sinh–ngoại sinh vừa gây suy giảm sức co bóp cơ tim và tụt huyết áp khó nâng bằng vận mạch.",
        "B5.03, B6.02", ["MTP", "Canxi"],
    ),
    trap(
        "SURGR2-TRAP-08", "B2", "Tin vào huyết áp bình thường ở ATLS Độ II để đánh giá 'bệnh nhân ổn'",
        f"Bệnh nhân chấn thương kín vừa vào viện có HA 110/80 mmHg nhưng mạch 112 lần/phút, thở 24 lần/phút, da tay hơi lạnh và lo lắng — Có được kết luận chưa mất máu nhiều?",
        f"1) <b>Mặt nạ giả của sốc còn bù:</b> Đây chính là {Y('Sốc mất máu Độ II (mất 750 – 1500 ml, 15 – 30% thể tích máu)')} — huyết áp tâm thu bình thường nhưng đã {R('hẹp hiệu số HA (HA kẹp 110/80)')} và mạch > 100.<br>"
        f"2) <b>Giải thích sinh lý:</b> Nhờ co mạch giao cảm và trung tâm hóa tuần hoàn giữ áp lực động mạch cho tim và não, nhưng nếu không hồi sức ngay sẽ tụt dốc đột ngột sang Độ III mất bù.",
        f"Tụt huyết áp tâm thu là dấu hiệu MUỘN (chỉ xuất hiện khi mất > 30% máu ở Độ III). Nhịp tim > 100 và huyết áp kẹp mới là tiếng chuông báo động sớm tại giường.",
        "B2.01, B3.01", ["ATLS", "Con-bu"],
    ),
]
