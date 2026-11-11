# -*- coding: utf-8 -*-
"""surgr1_cards_data.py — SURG-R1: Sốc Nhiễm Khuẩn (100% nguyên bản barem 08).
Cấu trúc chuẩn LIGHT_CSS (Dual-mode Light/Dark), mặt sau 🎯 + 💡, 4 thẻ ⚡ THUẬT TOÁN QUYẾT ĐỊNH,
đầy đủ thẻ bẫy & cờ đỏ, phủ 23/23 mã barem [B0.01]–[B7.05].
"""

def _c(hex_color, text):
    return f'<span style="color: {hex_color}; font-weight: 600;">{text}</span>'

def R(t): return _c("#ff6b6b", t)   # Đỏ cảnh báo / ngưỡng bệnh lý / chống chỉ định
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
        "category": f"SURG-R1 · {section}",
        "badge": badge,
        "badge_class": "badge-red" if red_flag else "",
        "front": front,
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R1", section] + tags,
    }

def algo(cid, section, topic, tier, front, core, ai, barem, tags):
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "category": f"SURG-R1 · {section}",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-amber",
        "front": f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {B(topic)}<br>{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R1", section, "Thuat-toan"] + tags,
    }

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False):
    prefix = f"{R('🛑 CỜ ĐỎ')} — " if red_flag else f"{Y('❌ Bẫy lâm sàng')} — "
    return {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": 1,
        "category": f"SURG-R1 · {section}",
        "badge": "🛑 CỜ ĐỎ" if red_flag else "❌ Bẫy lâm sàng",
        "badge_class": "badge-red" if red_flag else "badge-amber",
        "front": f"{prefix}{front}",
        "back": f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}",
        "extra": f"[{barem}]",
        "tags": ["SURG-R1", section, "Bay-lam-sang"] + tags,
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
        "category": f"SURG-R1 · {section}",
        "badge": "Cloze",
        "badge_class": "badge-blue",
        "text": text,
        "extra": f"[{barem}]",
        "tags": ["SURG-R1", section, "Cloze"] + tags,
    }


cards_data = [
    # =========================================================================
    # B0 — TỔNG QUAN & MỤC TIÊU HỌC TẬP
    # =========================================================================
    basic(
        "SURGR1-B0-01", "B0", "Khung đồng thuận quốc tế & Bậc thang tử vong", 1,
        f"{B('[Tổng quan — Chuẩn Sepsis-3 & SSC 2018]')} Theo các đồng thuận quốc tế (Sepsis-3, Surviving Sepsis Campaign Bundle 2018), tiến trình diễn biến của nhiễm khuẩn nặng gồm các nấc nào và tỷ lệ tử vong khác nhau ra sao?",
        f"1) <b>Khung tham chiếu:</b> Áp dụng đồng thuận <b>Sepsis-3</b> và <b>Surviving Sepsis Campaign (SSC) Bundle 2018</b>.<br>"
        f"2) <b>Bốn nấc bậc thang:</b> {B('SIRS')} → {B('Nhiễm khuẩn (Infection)')} → {Y('Nhiễm khuẩn huyết (Sepsis)')} (tử vong bệnh viện {Y('~ 10%')}) → {R('Sốc nhiễm khuẩn (Septic Shock)')} (tử vong {R('> 40%')}).",
        f"Sự nhảy vọt tỷ lệ tử vong từ khoảng 10% lên trên 40% khi chuyển sang sốc nhiễm khuẩn bắt nguồn từ tụt huyết áp kháng dịch kèm rối loạn chuyển hóa tế bào sâu sắc (tăng Lactat). Do đó mọi can thiệp hồi sức và phẫu thuật giải quyết ổ nhiễm đều tính bằng phút và giờ vàng đầu tiên.",
        "B0.01", ["Tong-quan", "Sepsis-3"],
    ),
    basic(
        "SURGR1-B0-02", "B0", "Bốn mục tiêu thực hành lâm sàng Sốc nhiễm khuẩn", 2,
        f"{B('[Tổng quan — Mục tiêu học tập]')} Nêu 4 mục tiêu trọng tâm cần nắm vững khi tiếp cận người bệnh sốc nhiễm khuẩn trong ngoại khoa & hồi sức?",
        f"1) <b>Nền tảng lý thuyết:</b> Trình bày định nghĩa và giải thích {B('cơ chế sinh lý bệnh')} sốc nhiễm khuẩn.<br>"
        f"2) <b>Khám & Xét nghiệm:</b> Nhận diện đầy đủ các dấu hiệu {Y('lâm sàng và cận lâm sàng')}.<br>"
        f"3) <b>Xác lập bệnh danh:</b> Chẩn đoán chính xác sốc nhiễm khuẩn (qua {B('Sepsis-3, qSOFA và MSOFA')}).<br>"
        f"4) <b>Chiến lược hồi sức:</b> Phân tích ý nghĩa các {G('đích hồi sức')} và vận hành trọn vẹn chuỗi hồi sức giờ đầu cùng {R('phẫu thuật loại bỏ ổ nhiễm trùng')}.",
        f"Ở bệnh nhân ngoại khoa (viêm phúc mạc, áp xe, sỏi mật nhiễm trùng), hồi sức nội khoa và kiểm soát nguồn nhiễm khuẩn ngoại khoa phải diễn ra song hành ngay từ giờ đầu thay vì chờ hết sốc mới mổ.",
        "B0.02", ["Tong-quan"],
    ),

    # =========================================================================
    # B1 — ĐỊNH NGHĨA SEPSIS-3
    # =========================================================================
    basic(
        "SURGR1-B1-01", "B1", "Hội chứng đáp ứng viêm hệ thống (SIRS)", 1,
        f"{B('[SIRS]')} Hội chứng đáp ứng viêm hệ thống (SIRS) được xác định khi có tối thiểu bao nhiêu trên 4 tiêu chuẩn nào?",
        f"Có {Y('ít nhất 2 trong 4 thông số')} sau (không tìm được nguyên nhân nào khác):<br>"
        f"1) <b>Nhiệt độ:</b> {R('> 38°C')} hoặc {R('< 36°C')}.<br>"
        f"2) <b>Tần số tim:</b> {R('> 90 lần/phút')}.<br>"
        f"3) <b>Tần số thở & Khí máu:</b> Tần số thở {R('> 20 lần/phút')} hoặc {R('PaCO₂ < 32 mmHg')}.<br>"
        f"4) <b>Bạch cầu máu:</b> {R('> 12.000/mm³')} hoặc {R('< 4.000/mm³')}, hoặc tỷ lệ bạch cầu non ({B('dạng dải - band')}) {R('> 10%')}.",
        f"SIRS phản ánh tình trạng phản ứng viêm lan tỏa của cơ thể trước nhiều tác nhân (nhiễm trùng, chấn thương, bỏng, viêm tụy cấp). Cả hai cực tăng cao lẫn sụt giảm sâu (thân nhiệt < 36°C hoặc bạch cầu < 4.000/mm³) đều cảnh báo nặng tương đương nhau.",
        "B1.01", ["Dinh-nghia", "SIRS"],
    ),
    basic(
        "SURGR1-B1-02", "B1", "Nhiễm khuẩn (Infection) & Nhiễm khuẩn huyết (Sepsis-3)", 1,
        f"{B('[Sepsis-3]')} Phân biệt khái niệm Nhiễm khuẩn (Infection) với Nhiễm khuẩn huyết (Sepsis) theo đồng thuận Sepsis-3 về bản chất và tiêu chuẩn điểm SOFA?",
        f"1) <b>Nhiễm khuẩn (Infection):</b> Là khi hội chứng đáp ứng viêm hệ thống (SIRS) xảy ra do nguyên nhân vi sinh vật ({B('vi khuẩn, virus, nấm, ký sinh trùng')}).<br>"
        f"2) <b>Nhiễm khuẩn huyết (Sepsis):</b> Là đáp ứng của ký chủ đối với nhiễm khuẩn bị {R('mất kiểm soát')}, gây {R('rối loạn chức năng tạng đe dọa tính mạng')}.<br>"
        f"3) <b>Mốc xác nhận suy tạng:</b> Thay đổi cấp tính {R('SOFA ≥ 2 điểm')} (tính từ điểm nền {G('0 điểm')} nếu trước đó chưa có suy tạng), tương ứng tử vong bệnh viện {Y('~ 10%')}.",
        f"Điểm mới cốt lõi của Sepsis-3 là bỏ khái niệm 'Sepsis nặng' cũ và lấy chính sự rối loạn chức năng tạng (ΔSOFA ≥ 2 điểm) làm ranh giới phân biệt nhiễm khuẩn thông thường với nhiễm khuẩn huyết thực thụ.",
        "B1.02, B1.03", ["Dinh-nghia", "Sepsis-3", "SOFA"],
    ),
    basic(
        "SURGR1-B1-03", "B1", "Định nghĩa & 2 Tiêu chuẩn Sốc nhiễm khuẩn (Septic Shock)", 1,
        f"{R('[Sốc nhiễm khuẩn — Tiêu chuẩn Sepsis-3]')} Sốc nhiễm khuẩn là gì và cần thỏa đồng thời 2 tiêu chuẩn lâm sàng nào để xác lập chẩn đoán?",
        f"1) <b>Bản chất & Tiên lượng:</b> Diễn tiến nặng của nhiễm khuẩn huyết kèm bất thường sâu sắc về tuần hoàn và chuyển hóa tế bào, đẩy nguy cơ tử vong vượt trội {R('> 40%')}.<br>"
        f"2) <b>Huyết động kháng dịch:</b> Tụt huyết áp dai dẳng {R('cần dùng thuốc vận mạch để duy trì MAP ≥ 65 mmHg')} dù đã được bù đủ thể tích dịch truyền.<br>"
        f"3) <b>Chuyển hóa tế bào:</b> Kèm bằng chứng giảm tưới máu tổ chức với {R('nồng độ Lactat máu > 2 mmol/L (18 mg/dL)')}.",
        f"Việc đòi hỏi đồng thời cả hai tiêu chuẩn (cần vận mạch giữ MAP ≥ 65 mmHg dù đã bù đủ dịch VÀ Lactat > 2 mmol/L) giúp nhận diện đúng nhóm suy sụp kép cả huyết động lẫn hô hấp tế bào có tỷ lệ tử vong > 40%.",
        "B1.03, B1.04", ["Dinh-nghia", "Sepsis-3"], red_flag=True,
    ),
    cloze(
        "SURGR1-B1-04", "B1", "Cloze: Các ngưỡng định nghĩa SIRS, Sepsis & Septic Shock",
        f"{B('[Mốc Sepsis-3 & SIRS]')} Theo SIRS, cần ít nhất 2/4 dấu hiệu gồm nhiệt độ > 38°C hoặc < 36°C, nhịp tim > {clz(1, R('90 lần/phút'))}, nhịp thở > 20 lần/phút hoặc PaCO₂ < {clz(2, R('32 mmHg'))}, và bạch cầu > 12.000 hoặc < 4.000/mm³ hoặc band > 10%. Rối loạn chức năng tạng trong Sepsis được xác nhận khi thang điểm SOFA thay đổi cấp tính {clz(3, R('≥ 2 điểm'))}, tương ứng tử vong khoảng {clz(4, Y('10%'))}. Trong sốc nhiễm khuẩn (tử vong > {clz(5, R('40%'))}), người bệnh cần dùng vận mạch duy trì {clz(6, G('MAP ≥ 65 mmHg'))} dù đã bù đủ dịch kèm nồng độ {clz(7, R('Lactat máu > 2 mmol/L (18 mg/dL)'))}.",
        "B1.01, B1.03, B1.04", ["Dinh-nghia", "Cloze"],
    ),

    # =========================================================================
    # B2 — SINH LÝ BỆNH SỐC NHIỄM KHUẨN
    # =========================================================================
    basic(
        "SURGR1-B2-01", "B2", "Chất trung gian hóa học & Cơn bão Cytokine", 2,
        f"{B('[Sinh lý bệnh — Chất trung gian]')} Các tế bào và hệ thống dịch thể nào bị hoạt hóa đầu tiên, dẫn tới phóng thích những nhóm chất trung gian hóa học nào trong sốc nhiễm khuẩn?",
        f"1) <b>Hệ thống bị hoạt hóa:</b> {B('Đại thực bào, bạch cầu, tiểu cầu, tế bào nội mạc')} cùng các hệ thống dịch thể ({B('bổ thể, đông máu')}).<br>"
        f"2) <b>Cytokine tiền viêm phóng thích ồ ạt:</b> {R('TNF-α, IL-1β, IL-6, IL-8')}.<br>"
        f"3) <b>Chất trung gian gây giãn mạch:</b> {Y('Nitric Oxide (NO), PAF, Prostacyclin')}.",
        f"Sự bùng phát đồng thời các cytokine tiền viêm (TNF-α, IL-1β, IL-6, IL-8) và chất giãn mạch mạnh (đặc biệt là NO nội mạc) khởi phát phản ứng dây chuyền làm giãn mạch hệ thống, thoát dịch qua kẽ nội mạc và hoạt hóa đông máu rải rác.",
        "B2.01", ["Sinh-ly-benh"],
    ),
    basic(
        "SURGR1-B2-02", "B2", "3 rối loạn đại tuần hoàn & chức năng co bóp cơ tim", 1,
        f"{B('[Sinh lý bệnh — Tuần hoàn lớn & Tim]')} Giải thích cách sốc nhiễm khuẩn gây giảm thể tích lòng mạch 'kép' (thực sự + tương đối) và suy giảm co bóp cơ tim?",
        f"1) <b>Tăng tính thấm mao mạch:</b> Thoát dịch và protein huyết tương ra khoang gian bào → gây phù mô và {R('giảm thể tích lòng mạch thực sự')}.<br>"
        f"2) <b>Giãn mạch hệ thống lan tỏa:</b> Giảm nặng {R('sức cản mạch hệ thống (SVR)')} → gây {R('giảm thể tích tuần hoàn tương đối')}.<br>"
        f"3) <b>Suy giảm co bóp cơ tim:</b> Do {B('yếu tố ức chế cơ tim (Myocardial Depressant Factor - MDF)')}, toan chuyển hóa và giảm tưới máu mạch vành.",
        f"Vì người bệnh đồng thời bị thoát dịch ra mô kẽ (thiếu dịch thực) và giãn mạch ngoại vi (giãn bể chứa tương đối), bù dịch đơn thuần không thể kéo huyết áp lên nếu thành mạch mất trương lực, buộc phải phối hợp sớm vận mạch co mạch.",
        "B2.02", ["Sinh-ly-benh", "Huyet-dong"],
    ),
    basic(
        "SURGR1-B2-03", "B2", "Rối loạn vi tuần hoàn & Đông máu nội mạch rải rác (DIC)", 2,
        f"{B('[Sinh lý bệnh — Vi tuần hoàn & Đông máu]')} Tại sao tế bào mô vẫn thiếu oxy dù lưu lượng tuần hoàn có thể còn cao, và biến chứng DIC gặp ở tỷ lệ bao nhiêu phần trăm ca sốc nhiễm khuẩn?",
        f"1) <b>Rối loạn vi tuần hoàn:</b> Giãn mao mạch, mất phân bố vi mạch, hình thành {R('vi huyết khối')} và xuất hiện {R('shunt tuần hoàn')} khiến máu đi tắt qua mà oxy không tới được tế bào mô.<br>"
        f"2) <b>Đông máu nội mạch rải rác (DIC):</b> Hoạt hóa đông máu toàn thân dẫn đến tắc vi mạch và chảy máu tiêu thụ, gặp ở {R('khoảng 30%')} trường hợp.",
        f"Đây là lý do dù nâng được huyết áp đại tuần hoàn (MAP), bệnh nhân vẫn có thể tử vong nếu vi huyết khối và shunt vi mạch chưa cải thiện — buộc phải theo dõi chặt Lactat và ScvO₂ để kiểm chứng oxy thực sự tới được tế bào.",
        "B2.02", ["Sinh-ly-benh", "DIC"],
    ),
    basic(
        "SURGR1-B2-04", "B2", "Tổn thương 5 cơ quan đích trong sốc nhiễm khuẩn", 2,
        f"{B('[Sinh lý bệnh — Suy đa tạng]')} Liệt kê diễn tiến tổn thương tại 5 cơ quan đích (Phổi, Thận, Thần kinh, Gan, Tiêu hóa) do sốc nhiễm khuẩn?",
        f"1) <b>Phổi:</b> Tổn thương phổi cấp ({Y('ALI')}) → Hội chứng suy hô hấp cấp tiến triển ({R('ARDS')}).<br>"
        f"2) <b>Thận:</b> Suy thận cấp chức năng (do tụt huyết áp) tiến triển thành {R('hoại tử ống thận cấp thực thể')}.<br>"
        f"3) <b>Hệ thần kinh:</b> Thiếu máu não gây {Y('lơ mơ, lú lẫn, mê sảng hoặc hôn mê')}.<br>"
        f"4) <b>Gan:</b> Hoại tử tế bào gan, {R('suy gan cấp, vàng da, rối loạn đông máu')}.<br>"
        f"5) <b>Hệ tiêu hóa:</b> {Y('Liệt ruột, loét và xuất huyết tiêu hóa do stress')}.",
        f"Nhận diện sớm chuyển biến từ suy chức năng sang tổn thương thực thể (ALI → ARDS, suy thận chức năng → hoại tử ống thận cấp) giúp thầy thuốc dự phòng thở máy bảo vệ phổi, dự phòng loét dạ dày stress và tránh thuốc độc thận như HES.",
        "B2.03", ["Sinh-ly-benh", "Suy-da-tang"],
    ),

    # =========================================================================
    # B3 — TRIỆU CHỨNG LÂM SÀNG & ĐƯỜNG VÀO VI KHUẨN
    # =========================================================================
    basic(
        "SURGR1-B3-01", "B3", "Hội chứng giảm tưới máu tổ chức (5 hệ cơ quan)", 1,
        f"{B('[Lâm sàng — Hội chứng Sốc]')} Mô tả 5 nhóm biểu hiện lâm sàng của hội chứng giảm tưới máu tổ chức (tinh thần, da, huyết áp, mạch, nước tiểu) ở bệnh nhân sốc nhiễm khuẩn?",
        f"1) <b>Tinh thần:</b> Kích động, vật vã hốt hoảng hoặc li bì, lơ mơ, hôn mê.<br>"
        f"2) <b>Da ngoại vi:</b> Lạnh, ẩm, nổi vân tím; thời gian hồi phục màu da mao mạch kéo dài ({R('Refill > 2 giây')}).<br>"
        f"3) <b>Huyết áp tụt:</b> {R('HATT < 90 mmHg')} hoặc {R('giảm > 40 mmHg so với huyết áp nền')}, cần vận mạch giữ {G('MAP ≥ 65 mmHg')}.<br>"
        f"4) <b>Mạch:</b> Nhanh nhỏ khó bắt hoặc chậm rời rạc.<br>"
        f"5) <b>Bài niệu:</b> {R('Thiểu niệu (< 0,5 ml/kg/giờ)')} hoặc vô niệu.",
        f"Ở người tăng huyết áp mạn tính (ví dụ nền 160/90 mmHg), tụt xuống 110/70 mmHg đã tương ứng mức giảm > 40 mmHg và gây giảm tưới máu thận — đừng đợi HATT < 90 mmHg mới chẩn đoán tụt huyết áp!",
        "B3.01", ["Lam-sang", "Soc"],
    ),
    basic(
        "SURGR1-B3-02", "B3", "Hội chứng nhiễm khuẩn trên lâm sàng", 2,
        f"{B('[Lâm sàng — Hội chứng nhiễm khuẩn]')} Các dấu hiệu toàn thân thuộc hội chứng nhiễm khuẩn ở bệnh nhân sốc nhiễm khuẩn gồm những gì?",
        f"1) <b>Thân nhiệt:</b> {R('Sốt cao gai rét')} hoặc ngược lại {R('hạ thân nhiệt (< 36°C)')}.<br>"
        f"2) <b>Hô hấp:</b> {Y('Thở nhanh nông')} (thường là dấu hiệu sớm của bù trừ toan chuyển hóa và kích thích trung tâm hô hấp).",
        f"Hạ thân nhiệt (< 36°C) thường gặp ở người già, suy kiệt hoặc nhiễm khuẩn gram âm nặng và có tiên lượng xấu hơn sốt cao do mất khả năng đáp ứng sinh nhiệt của cơ thể.",
        "B3.02", ["Lam-sang"],
    ),
    basic(
        "SURGR1-B3-03", "B3", "6 đường vào vi khuẩn & Tỷ lệ phân bố", 2,
        f"{B('[Đường vào vi khuẩn]')} Trình bày 6 đường vào của vi khuẩn gây sốc nhiễm khuẩn theo thứ tự tỷ lệ phần trăm từ cao xuống thấp?",
        f"1) <b>Hô hấp:</b> {R('40%')} (chiếm tỷ lệ cao nhất).<br>"
        f"2) <b>Tiêu hóa – Gan mật:</b> {R('30%')}.<br>"
        f"3) <b>Tiết niệu:</b> {Y('10%')}.<br>"
        f"4) <b>Da – mô mềm:</b> {B('5%')}.<br>"
        f"5) <b>Catheter / thủ thuật xâm lấn:</b> {B('5%')}.<br>"
        f"6) <b>Không rõ đường vào:</b> {Y('15 – 20%')}.",
        f"Ba ổ nhiễm dẫn đầu (Hô hấp 40%, Tiêu hóa–Gan mật 30%, Tiết niệu 10%) chiếm tới 80% các đường vào xác định được; trong ngoại khoa, đường tiêu hóa – gan mật (viêm phúc mạc, tắc mật mủ) luôn phải được siêu âm/CT rà soát đầu tiên để dẫn lưu cấp cứu.",
        "B3.03", ["Duong-vao"],
    ),

    # =========================================================================
    # B4 — THANG ĐIỂM ĐÁNH GIÁ (qSOFA & MSOFA)
    # =========================================================================
    basic(
        "SURGR1-B4-01", "B4", "Thang điểm sàng lọc nhanh qSOFA tại giường", 1,
        f"{B('[Thang điểm qSOFA]')} Nêu 3 tiêu chí của thang điểm qSOFA dùng đánh giá nhanh tại giường và ngưỡng điểm nghi ngờ Sepsis?",
        f"Nghi ngờ Sepsis khi đạt {R('qSOFA ≥ 2 điểm')} trên 3 tiêu chí sau (mỗi tiêu chí 1 điểm):<br>"
        f"1) <b>Nhịp thở:</b> {R('Tần số thở ≥ 22 lần/phút')}.<br>"
        f"2) <b>Thần kinh:</b> {R('Rối loạn ý thức (GCS < 15)')}.<br>"
        f"3) <b>Huyết động:</b> {R('Huyết áp tâm thu ≤ 100 mmHg')}.",
        f"qSOFA không cần xét nghiệm máu, giúp phát hiện nhanh ngay tại phòng cấp cứu hoặc buồng bệnh ngoại khoa bệnh nhân có nguy cơ diễn biến xấu. Tuy nhiên qSOFA chỉ là công cụ sàng lọc cảnh báo, chẩn đoán xác định Sepsis vẫn dựa vào ΔSOFA ≥ 2 điểm.",
        "B4.01", ["qSOFA", "Thang-diem"],
    ),
    basic(
        "SURGR1-B4-02", "B4", "Thang điểm MSOFA: Hô hấp, Đông máu, Gan, Thận (0–4 điểm)", 2,
        f"{B('[Thang điểm MSOFA — 4 tạng cận lâm sàng]')} Trình bày chi tiết ngưỡng 0–4 điểm của 4 cơ quan Hô hấp, Đông máu, Gan và Thận trong thang điểm MSOFA?",
        f"1) <b>Hô hấp (PaO₂/FiO₂):</b> {G('>400')} (0đ) · {B('301–400')} (1đ) · {Y('201–300')} (2đ) · {R('101–200')} (3đ) · {R('≤ 100')} (4đ).<br>"
        f"2) <b>Đông máu (Tiểu cầu × 10³/µL):</b> {G('>150')} (0đ) · {B('101–150')} (1đ) · {Y('51–100')} (2đ) · {R('21–50')} (3đ) · {R('≤ 20')} (4đ).<br>"
        f"3) <b>Gan (Bilirubin TP mg/dL):</b> {G('<1,2')} (0đ) · {B('1,2–1,9')} (1đ) · {Y('2,0–5,9')} (2đ) · {R('6,0–11,9')} (3đ) · {R('≥ 12,0')} (4đ).<br>"
        f"4) <b>Thận (Creatinine mg/dL):</b> {G('<1,2')} (0đ) · {B('1,2–1,9')} (1đ) · {Y('2,0–3,4')} (2đ) · {R('3,5–4,9')} (3đ) · {R('> 5,0')} (4đ).",
        f"Lưu ý sự tinh giản của MSOFA so với SOFA gốc: bỏ cột thần kinh (GCS) để tập trung vào 4 thông số cận lâm sàng dễ định lượng lặp lại kết hợp với liều thuốc vận mạch đánh giá mức độ suy đa tạng.",
        "B4.02", ["MSOFA", "Thang-diem"],
    ),
    basic(
        "SURGR1-B4-03", "B4", "Thang điểm MSOFA: Tuần hoàn & Liều vận mạch (0–4 điểm)", 1,
        f"{B('[Thang điểm MSOFA — Tuần hoàn]')} Thang điểm MSOFA chấm 0 đến 4 điểm cho cơ quan Tuần hoàn dựa trên loại và liều thuốc vận mạch như thế nào?",
        f"1) <b>0 điểm:</b> {G('Không dùng thuốc vận mạch')}.<br>"
        f"2) <b>1 điểm:</b> Dùng {B('bất kỳ vận mạch nào')} (hoặc khởi trị hỗ trợ huyết áp).<br>"
        f"3) <b>2 điểm:</b> {Y('Dopamine < 5 µg/kg/phút')} hoặc {Y('Dobutamine')}.<br>"
        f"4) <b>3 điểm:</b> {R('Dopamine 5 – 15 µg/kg/phút')} hoặc {R('Epinephrine / Norepinephrine ≤ 0,1 µg/kg/phút')}.<br>"
        f"5) <b>4 điểm:</b> {R('Dopamine > 15 µg/kg/phút')} hoặc {R('Epinephrine / Norepinephrine > 0,1 µg/kg/phút')}.",
        f"Điểm khác biệt đặc trưng của MSOFA ở cột Tuần hoàn là cho ngay 1 điểm nếu dùng bất kỳ vận mạch nào (thay cho ngưỡng MAP < 70 mmHg ở SOFA kinh điển) và phân tầng mạnh 3–4 điểm quanh ngưỡng Norepinephrine/Epinephrine 0,1 µg/kg/phút.",
        "B4.02", ["MSOFA", "Van-mach"],
    ),
    cloze(
        "SURGR1-B4-04", "B4", "Cloze: qSOFA & Điểm tối đa (4 điểm) của MSOFA",
        f"{B('[Thang điểm qSOFA & MSOFA]')} Thang điểm qSOFA nghi ngờ Sepsis khi đạt ≥ 2 điểm với các mốc: tần số thở {clz(1, R('≥ 22 lần/phút'))}. Rối loạn ý thức đánh giá là {clz(2, R('GCS < 15'))}. Mốc huyết áp tâm thu là {clz(3, R('≤ 100 mmHg'))}. Trong MSOFA mức 4 điểm, tỷ số PaO₂/FiO₂ là {clz(4, R('≤ 100'))}. Ngưỡng tiểu cầu 4 điểm là {clz(5, R('≤ 20 × 10³/µL'))}. Ngưỡng Bilirubin 4 điểm là {clz(6, R('≥ 12,0 mg/dL'))}. Ngưỡng Creatinine 4 điểm là {clz(7, R('> 5,0 mg/dL'))}. Mốc liều Dopamine > 15 hoặc Epi/Norepi mức 4 điểm là {clz(8, R('> 0,1 µg/kg/phút'))}.",
        "B4.01, B4.02", ["qSOFA", "MSOFA", "Cloze"],
    ),

    # =========================================================================
    # B5 — CẬN LÂM SÀNG CHẨN ĐOÁN & THEO DÕI
    # =========================================================================
    basic(
        "SURGR1-B5-01", "B5", "Công thức máu & Dấu ấn viêm nhiễm (PCT, CRP)", 1,
        f"{B('[Cận lâm sàng — Máu & Viêm]')} Bạch cầu máu và các dấu ấn viêm nhiễm (Procalcitonin, CRP) biến đổi như thế nào trong sốc nhiễm khuẩn?",
        f"1) <b>Công thức bạch cầu:</b> Số lượng bạch cầu máu {R('tăng cao hoặc hạ thấp')}; tỷ lệ bạch cầu trung tính và bạch cầu non ({B('dạng dải - band')}) tăng.<br>"
        f"2) <b>Dấu ấn sinh học viêm:</b> {R('Procalcitonin (PCT) ≥ 2 ng/ml')} (rất đặc hiệu cho nhiễm khuẩn nặng) và {Y('CRP tăng cao')}.",
        f"Procalcitonin vượt trội CRP ở tính đặc hiệu với nhiễm khuẩn hệ thống và động học biến thiên nhanh, vừa giúp củng cố chẩn đoán nhiễm khuẩn nặng (PCT ≥ 2 ng/ml) vừa theo dõi đáp ứng để hỗ trợ quyết định xuống thang hoặc ngừng kháng sinh.",
        "B5.01", ["Can-lam-sang", "PCT"],
    ),
    basic(
        "SURGR1-B5-02", "B5", "Lactat máu & Nhịp độ theo dõi đáp ứng hồi sức", 1,
        f"{B('[Cận lâm sàng — Lactat máu]')} Ngưỡng Lactat máu gợi ý giảm tưới máu mô là bao nhiêu và cần xét nghiệm lại theo chu kỳ nào trong quá trình hồi sức?",
        f"1) <b>Ngưỡng cảnh báo thiếu oxy tổ chức:</b> {R('Lactat máu ≥ 2 mmol/L')} (tiêu chuẩn sốc nhiễm khuẩn đòi hỏi > 2 mmol/L).<br>"
        f"2) <b>Chu kỳ kiểm tra lại:</b> Theo dõi định kỳ {G('mỗi 2 – 4 giờ')} để đánh giá tốc độ thanh thải Lactat và đáp ứng hồi sức dịch/vận mạch.",
        f"Lactat phản ánh trực tiếp tình trạng chuyển hóa yếm khí của tế bào. Đo lặp lại mỗi 2 – 4 giờ giúp phát hiện kịp thời tình trạng tụt tưới máu ngầm ngay cả khi huyết áp trên monitor trông có vẻ ổn.",
        "B5.02", ["Can-lam-sang", "Lactat"],
    ),
    basic(
        "SURGR1-B5-03", "B5", "Bilan đông máu (DIC) & Khí máu động mạch", 2,
        f"{B('[Cận lâm sàng — Đông máu & Khí máu]')} Bilan đông máu và khí máu động mạch thể hiện những bất thường điển hình nào ở bệnh nhân sốc nhiễm khuẩn?",
        f"1) <b>Bộ xét nghiệm đông máu (DIC):</b> {R('Tiểu cầu giảm, PT kéo dài, Fibrinogen giảm, D-dimer tăng cao')}.<br>"
        f"2) <b>Khí máu động mạch (ABG):</b> {R('Toan chuyển hóa')} ({B('pH giảm, HCO₃⁻ giảm, BE âm tính')}) kèm tỷ số {R('PaO₂/FiO₂ giảm')}.<br>"
        f"3) <b>Lưu ý mẫu bệnh phẩm:</b> Cần làm {G('khí máu động mạch')} vì khí máu tĩnh mạch ít đặc hiệu hơn cho đánh giá oxy hóa máu (PaO₂/FiO₂) và thăng bằng toan kiềm hệ thống.",
        f"Sự sụt giảm cùng lúc tiểu cầu và fibrinogen kèm tăng D-dimer chứng tỏ tiêu thụ yếu tố đông máu và tiêu sợi huyết thứ phát trong DIC; còn chỉ số PaO₂/FiO₂ trên khí máu động mạch giúp chấm điểm suy hô hấp MSOFA và chẩn đoán ARDS.",
        "B5.03", ["Can-lam-sang", "DIC", "Khi-mau"],
    ),
    basic(
        "SURGR1-B5-04", "B5", "Cấy máu (2 mẫu) & Cấy bệnh phẩm + Kháng sinh đồ", 1,
        f"{B('[Cận lâm sàng — Vi sinh]')} Nguyên tắc lấy mẫu cấy máu, cấy bệnh phẩm nghi ngờ và kháng sinh đồ trong chẩn đoán sốc nhiễm khuẩn là gì?",
        f"1) <b>Tiêu chuẩn vàng vi sinh:</b> {G('Cấy máu ít nhất 2 mẫu (gồm cả chai ưa khí và kỵ khí)')}.<br>"
        f"2) <b>Cấy bệnh phẩm tại ổ nhiễm:</b> Cấy {B('đờm, nước tiểu, dịch mủ...')} tại vị trí nghi ngờ.<br>"
        f"3) <b>Thời điểm & Mục tiêu:</b> Lấy bệnh phẩm cấy {R('trước khi dùng kháng sinh')} và thực hiện {G('kháng sinh đồ')} để làm căn cứ xuống thang kháng sinh đúng đích.",
        f"Lấy tối thiểu 2 bộ cấy máu (ưa khí + kỵ khí) trước khi tiêm liều kháng sinh đầu tiên giúp tối đa hóa khả năng bắt được vi khuẩn gây bệnh và phân biệt với tạp nhiễm da, miễn sao không làm chậm quá 45 phút – 1 giờ vàng kháng sinh.",
        "B5.04", ["Can-lam-sang", "Vi-sinh"],
    ),

    # =========================================================================
    # B6 — ĐÍCH HỒI SỨC & CHẨN ĐOÁN PHÂN BIỆT
    # =========================================================================
    basic(
        "SURGR1-B6-01", "B6", "6 Đích hồi sức cần đạt trong sốc nhiễm khuẩn", 1,
        f"{G('[Đích hồi sức SSC]')} Trình bày đầy đủ 6 đích thông số huyết động, oxy hóa mô, bài niệu, Lactat và Hemoglobin cần đạt khi hồi sức sốc nhiễm khuẩn?",
        f"1) <b>Huyết áp trung bình:</b> {G('MAP ≥ 65 mmHg')}.<br>"
        f"2) <b>Bài niệu:</b> Lượng nước tiểu {G('≥ 0,5 ml/kg/giờ')}.<br>"
        f"3) <b>Áp lực tĩnh mạch trung tâm (CVP):</b> {G('8 – 12 mmHg')} (nếu thở máy: {B('12 – 15 mmHg')}).<br>"
        f"4) <b>Bão hòa oxy máu tĩnh mạch:</b> {G('ScvO₂ ≥ 70%')} (hoặc {G('SvO₂ ≥ 65%')}).<br>"
        f"5) <b>Thanh thải Lactat máu:</b> Trở về bình thường hoặc {G('giảm ≥ 20% sau mỗi 2 giờ')}.<br>"
        f"6) <b>Hemoglobin (Hb):</b> Duy trì {G('> 70 g/L')} (đích {B('70 – 90 g/L')}).",
        f"Nhìn tổng thể 6 đích này sẽ thấy logic hồi sức: CVP bảo đảm đủ tiền gánh; MAP đảm bảo áp lực tưới máu tạng; ScvO₂ và Lactat xác nhận tế bào thực sự nhận và sử dụng được oxy; nước tiểu phản ánh trực tiếp tưới máu thận tại giường.",
        "B6.01", ["Dich-hoi-suc"],
    ),
    cloze(
        "SURGR1-B6-02", "B6", "Cloze: Toàn bộ các con số đích hồi sức sốc nhiễm khuẩn",
        f"{B('[Đích hồi sức cần đạt]')} Mục tiêu huyết áp trong sốc nhiễm khuẩn là duy trì {clz(1, G('MAP ≥ 65 mmHg'))}. Lượng nước tiểu tối thiểu cần đạt là {clz(2, G('≥ 0,5 ml/kg/giờ'))}. Áp lực tĩnh mạch trung tâm (CVP) giữ ở mức {clz(3, G('8 – 12 mmHg'))}. Khi người bệnh thở máy thì giữ CVP ở mức {clz(4, B('12 – 15 mmHg'))}. Độ bão hòa oxy tĩnh mạch trung tâm cần đạt {clz(5, G('ScvO₂ ≥ 70%'))} hoặc độ bão hòa tĩnh mạch trộn {clz(6, G('SvO₂ ≥ 65%'))}. Lactat máu phải về bình thường hoặc giảm {clz(7, G('≥ 20% sau mỗi 2 giờ'))}. Mục tiêu duy trì Hemoglobin là {clz(8, G('> 70 g/L (70 – 90 g/L)'))}.",
        "B6.01", ["Dich-hoi-suc", "Cloze"],
    ),

    # =========================================================================
    # B7 — ĐIỀU TRỊ (SSC BUNDLE 1 GIỜ ĐẦU & NGOẠI KHOA)
    # =========================================================================
    basic(
        "SURGR1-B7-01", "B7", "Bù dịch khẩn cấp: Loại dịch, Liều 30 ml/kg & Chống chỉ định", 1,
        f"{B('[Điều trị — Bù dịch khẩn cấp]')} Chiến lược lựa chọn dịch truyền, liều lượng, thời gian và các dung dịch cần tránh trong hồi sức sốc nhiễm khuẩn là gì?",
        f"1) <b>Mức truyền khẩn cấp đầu tiên:</b> Bắt đầu ngay lập tức {G('30 ml/kg dung dịch tinh thể')} trong {Y('3 giờ đầu')}.<br>"
        f"2) <b>Dung dịch tinh thể ưu tiên:</b> {G('Ringer Lactat')} (dung dịch tinh thể cân bằng) hoặc {G('NaCl 0,9%')}.<br>"
        f"3) <b>Phối hợp keo tự nhiên:</b> Cân nhắc thêm {B('Albumin 5% – 20%')} khi cần truyền khối lượng dịch lớn.<br>"
        f"4) <b>Dung dịch tránh dùng:</b> {R('Chống chỉ định dung dịch keo nhân tạo HES (Hydroxyethyl Starch / Heasteril 6%)')} do gây tổn thương thận và tăng tử vong; {R('không lựa chọn Gelatin')}.",
        f"Tinh thể cân bằng (Ringer Lactat) hay NaCl 0,9% giúp lấp đầy nhanh thể tích lòng mạch bị mất do giãn mạch và thoát dịch mà không gây độc ống thận hay rối loạn đông máu như nhóm tinh bột HES hay Gelatin.",
        "B7.01", ["Dieu-tri", "Bu-dich"],
    ),
    basic(
        "SURGR1-B7-02", "B7", "Thuốc vận mạch & Tăng co bóp cơ tim", 1,
        f"{B('[Điều trị — Vận mạch & Tăng co bóp]')} Nêu thuốc vận mạch hàng đầu (liều khởi đầu), các thuốc phối hợp hàng hai, chỉ định Dobutamine và khuyến cáo về Dopamine?",
        f"1) <b>Thuốc hàng đầu (First-line):</b> {G('Norepinephrine')} khởi đầu liều {B('0,05 – 0,1 µg/kg/phút')}, chỉnh liều giữ {G('MAP ≥ 65 mmHg')}.<br>"
        f"2) <b>Thuốc phối hợp nâng MAP:</b> Thêm {Y('Vasopressin')} (liều cố định {B('0,03 đv/phút')}) hoặc {Y('Epinephrine')} nếu chưa đạt đích MAP.<br>"
        f"3) <b>Thuốc tăng co bóp cơ tim:</b> Thêm {B('Dobutamine (2,5 – 20 µg/kg/phút)')} khi có suy chức năng co bóp cơ tim hoặc {R('ScvO₂ < 70% dù đã bù đủ dịch')}.<br>"
        f"4) <b>Lưu ý Dopamine:</b> {R('Không dùng Dopamine liều thấp')} với mục đích 'bảo vệ thận'.",
        f"Norepinephrine tác động chủ yếu co mạch alpha-1 kèm chút beta-1 giúp nâng SVR nhanh mà ít gây rối loạn nhịp hơn Dopamine. Dobutamine không phải thuốc nâng huyết áp mà là thuốc tăng sức bóp (inotrop) dành cho trường hợp cung lượng tim vẫn thấp (ScvO₂ < 70%).",
        "B7.02", ["Dieu-tri", "Van-mach"],
    ),
    basic(
        "SURGR1-B7-03", "B7", "Liệu pháp kháng sinh sớm (Giờ vàng 1 giờ đầu)", 1,
        f"{B('[Điều trị — Kháng sinh]')} Nguyên tắc sử dụng kháng sinh về đường dùng, mốc thời gian bắt buộc, cách chọn phổ thuốc, xuống thang và tổng thời gian?",
        f"1) <b>Đường dùng & Thời gian vàng:</b> {R('Bắt buộc tiêm tĩnh mạch trong vòng 1 giờ đầu tiên')}.<br>"
        f"2) <b>Lựa chọn ban đầu:</b> Dùng {B('kháng sinh phổ rộng theo kinh nghiệm')} phủ các tác nhân nghi ngờ từ đường vào.<br>"
        f"3) <b>Điều chỉnh & Thời gian liệu trình:</b> {G('Xuống thang theo kết quả kháng sinh đồ')}; thời gian điều trị thông thường {B('7 – 10 ngày')}.",
        f"Mỗi giờ chậm trễ kháng sinh đường tĩnh mạch làm tỷ lệ tử vong tăng vọt rõ rệt. Lấy cấy máu trước nhưng tuyệt đối không để thủ tục lấy mẫu trì hoãn quá mốc 60 phút đầu tiên.",
        "B7.03", ["Dieu-tri", "Khang-sinh"],
    ),
    basic(
        "SURGR1-B7-04", "B7", "Kiểm soát ổ nhiễm khuẩn ngoại khoa cấp cứu", 1,
        f"{R('[Điều trị — Kiểm soát nguồn nhiễm]')} Vai trò và thời điểm can thiệp ngoại khoa đối với các ổ nhiễm trùng ngoại khoa trong sốc nhiễm khuẩn là gì?",
        f"1) <b>Nguyên tắc sống còn:</b> {R('Kháng sinh đơn thuần không thể chữa khỏi')} nếu chưa giải quyết được ổ mủ / nguồn nhiễm khuẩn ngoại khoa.<br>"
        f"2) <b>Thời điểm mổ/can thiệp:</b> Thực hiện {R('phẫu thuật cấp cứu ngay khi bắt đầu hồi sức dịch')}.<br>"
        f"3) <b>Các thủ thuật điển hình:</b> Dẫn lưu ổ áp xe, cắt ruột thừa viêm mủ, dẫn lưu mủ màng phổi, giải áp sỏi mật nhiễm trùng...",
        f"Ổ áp xe hoặc đường mật ứ mủ có vỏ xơ, pH toan và áp lực cao làm kháng sinh hầu như không thấm vào diệt khuẩn nổi, đồng thời liên tục phóng thích nội độc tố vào tuần hoàn. Chỉ cần khởi động bù dịch ổn định bước đầu là phải giải quyết ổ nhiễm ngay.",
        "B7.04", ["Dieu-tri", "Ngoai-khoa"], red_flag=True,
    ),
    basic(
        "SURGR1-B7-05", "B7", "4 biện pháp điều trị hỗ trợ (Thở máy, Hydrocortisone, Đường huyết, Hồng cầu)", 2,
        f"{B('[Điều trị — Hỗ trợ khác]')} Trình bày 4 ngưỡng và mục tiêu cụ thể của thở máy, Corticosteroid, kiểm soát đường huyết và truyền máu trong sốc nhiễm khuẩn?",
        f"1) <b>Thở máy bảo vệ phổi (khi có ARDS):</b> Thể tích khí lưu thông {G('Vt thấp 6 ml/kg')} kèm {B('PEEP phù hợp')}.<br>"
        f"2) <b>Corticosteroid:</b> Chỉ dùng {Y('Hydrocortisone 200 mg/ngày')} khi huyết động {R('không đáp ứng với bù dịch và vận mạch liều cao')}.<br>"
        f"3) <b>Kiểm soát đường huyết:</b> Giữ mục tiêu đường huyết {G('< 10 mmol/L (180 mg/dL)')}.<br>"
        f"4) <b>Truyền hồng cầu khối:</b> Chỉ truyền khi {R('Hemoglobin < 70 g/L')}, với đích duy trì {G('70 – 90 g/L')}.",
        f"Các ngưỡng hỗ trợ này đều bảo đảm cân bằng giữa lợi ích và tác hại: Vt 6 ml/kg tránh chấn thương áp lực phổi ARDS, Hydrocortisone 200 mg/ngày chỉ dành cho sốc trơ vận mạch, còn ngưỡng truyền Hb < 70 g/L tránh biến chứng quá tải tuần hoàn do truyền máu thừa.",
        "B7.05", ["Dieu-tri", "Ho-tro"],
    ),

    # =========================================================================
    # 4 THẺ ⚡ THUẬT TOÁN QUYẾT ĐỊNH
    # =========================================================================
    algo(
        "SURGR1-ALGO-01", "B4", "Quyết định sàng lọc & phân tầng Sepsis-3 tại cấp cứu", 1,
        f"Bệnh nhân có ổ nghi ngờ nhiễm khuẩn vào cấp cứu — Quy trình sàng lọc nhanh từ SIRS / qSOFA đến xác lập Sepsis và Septic Shock theo các bước nào?",
        f"1) <b>Sàng lọc ban đầu:</b> Đếm dấu hiệu {B('SIRS')} (≥ 2/4: T° >38/<36°C, mạch >90, thở >20/PaCO₂ <32, BC >12k/<4k/band >10%) và bấm ngay {B('qSOFA')} tại giường ({R('nhịp thở ≥ 22, GCS < 15, HATT ≤ 100')}; ≥ 2đ nghi Sepsis).<br>"
        f"2) <b>Xác lập Sepsis:</b> Đánh giá bảng điểm {Y('SOFA / MSOFA')} (5 cơ quan); nếu thay đổi cấp tính {R('≥ 2 điểm')} từ nền 0 → chẩn đoán xác định {Y('Sepsis')} (nguy cơ tử vong ~10%).<br>"
        f"3) <b>Xác lập Septic Shock:</b> Bù dịch đầy đủ nhưng vẫn cần vận mạch giữ {G('MAP ≥ 65 mmHg')} VÀ {R('Lactat > 2 mmol/L')} → chẩn đoán {R('Sốc nhiễm khuẩn')} (tử vong >40%).",
        f"Luồng ra quyết định đi từ công cụ lâm sàng thuần túy không tốn thời gian chờ xét nghiệm (qSOFA) sang đánh giá suy tạng định lượng (SOFA/MSOFA) rồi cuối cùng nhận diện sốc kháng dịch kèm tăng Lactat.",
        "B1.01, B1.03, B1.04, B4.01, B4.02", ["SIRS", "qSOFA", "MSOFA"],
    ),
    algo(
        "SURGR1-ALGO-02", "B7", "Gói hồi sức 1 giờ đầu (Hour-1 Bundle) & Kiểm soát nguồn nhiễm ngoại khoa", 1,
        f"Ngay khi nhận diện Sốc nhiễm khuẩn tại cấp cứu ngoại khoa — Thứ tự hành động khẩn cấp trong Gói 1 giờ đầu (Hour-1 Bundle) và phẫu thuật xử lý ổ nhiễm là gì?",
        f"1) <b>Đo Lactat & Lấy mẫu vi sinh:</b> Định lượng {B('Lactat máu')} (lặp lại mỗi 2–4 giờ) và lấy {G('≥ 2 mẫu cấy máu ưa/kỵ khí')} + cấy mủ/đờm/nước tiểu ngay trước khi tiêm thuốc.<br>"
        f"2) <b>Tiêm thuốc đường tĩnh mạch < 1 giờ:</b> Tiêm tĩnh mạch ngay {R('kháng sinh phổ rộng theo kinh nghiệm')} trong vòng 1 giờ đầu tiên.<br>"
        f"3) <b>Bù dịch & Vận mạch:</b> Truyền nhanh {G('30 ml/kg tinh thể')} (Ringer Lactat hoặc NaCl 0,9%) trong 3 giờ đầu; khởi trị sớm {G('Norepinephrine')} giữ {G('MAP ≥ 65 mmHg')} nếu vẫn tụt huyết áp.<br>"
        f"4) <b>Chuyển mổ kiểm soát ổ nhiễm:</b> Triển khai {R('dẫn lưu ổ áp xe / cắt ruột thừa mủ / dẫn lưu mủ màng phổi / giải áp đường mật')} ngay khi hồi sức dịch bắt đầu.",
        f"Đừng chờ kết quả kháng sinh đồ hay chờ dịch truyền hết 3 giờ mới xử trí các bước tiếp theo: 4 mũi nhọn (Lactat + Cấy máu, Kháng sinh IV <1h, Dịch 30 ml/kg + Norepinephrine, Phẫu thuật kiểm soát nguồn nhiễm) phải kích hoạt đồng bộ như dây chuyền cấp cứu.",
        "B5.02, B5.04, B7.01, B7.02, B7.03, B7.04", ["Hour-1-Bundle", "Cap-cuu"],
    ),
    algo(
        "SURGR1-ALGO-03", "B7", "Thang bậc leo thang Vận mạch – Tăng co bóp – Hydrocortisone", 1,
        f"Sau khi bắt đầu Norepinephrine mà huyết động hoặc oxy hóa mô vẫn chưa đạt đích — Quy trình leo thang thuốc từng nấc thực hiện thế nào?",
        f"1) <b>Nấc 1 (Khởi trị đầu tay):</b> Truyền {G('Norepinephrine 0,05 – 0,1 µg/kg/phút')}, chỉnh liều nhằm đạt {G('MAP ≥ 65 mmHg')}.<br>"
        f"2) <b>Nấc 2 (Chưa đạt MAP ≥ 65):</b> Phối hợp thêm {Y('Vasopressin 0,03 đv/phút')} (liều cố định) hoặc {Y('Epinephrine')}; tránh dùng Dopamine liều thấp bảo vệ thận.<br>"
        f"3) <b>Nấc 3 (Suy co bóp cơ tim / ScvO₂ < 70% dù đủ dịch):</b> Bổ sung {B('Dobutamine 2,5 – 20 µg/kg/phút')}.<br>"
        f"4) <b>Nấc 4 (Sốc trơ dịch & vận mạch liều cao):</b> Chỉ định {R('Hydrocortisone 200 mg/ngày')}.",
        f"Phân biệt rõ chức năng từng thuốc tránh cộng dồn sai cơ chế: Vasopressin/Epinephrine giải quyết liệt mạch để giữ MAP ≥ 65, Dobutamine giải quyết cung lượng tim thấp gây ScvO₂ < 70%, còn Hydrocortisone giúp phục hồi đáp ứng thụ thể giao cảm khi sốc kháng trị.",
        "B7.02, B7.05", ["Van-mach", "Corticoid"],
    ),
    algo(
        "SURGR1-ALGO-04", "B6", "Đánh giá đáp ứng hồi sức sau 2 – 4 giờ & Xử lý khi thông số lệch đích", 1,
        f"Tại thời điểm 2 – 4 giờ sau hồi sức tích cực — Cách đọc bộ đích hồi sức và hành động điều chỉnh tương ứng cho từng thông số chưa đạt?",
        f"1) <b>Thanh thải Lactat < 20% mỗi 2 giờ hoặc CVP thấp (< 8–12 / < 12–15 mmHg thở máy):</b> Đánh giá lại thể tích tuần hoàn (dịch tinh thể / cân nhắc Albumin nếu cần lượng lớn) và rà soát ổ nhiễm ngoại khoa chưa được dẫn lưu hết.<br>"
        f"2) <b>ScvO₂ < 70% (hoặc SvO₂ < 65%) & Hb giảm:</b> Kiểm tra {R('Hemoglobin < 70 g/L')} để truyền hồng cầu khối (đích {G('70 – 90 g/L')}); nếu Hb & tiền gánh đã đủ mà ScvO₂ vẫn < 70% thì bổ sung {B('Dobutamine')}.<br>"
        f"3) <b>PaO₂/FiO₂ giảm tiến triển ARDS:</b> Chuyển chiến lược thở máy bảo vệ phổi ({G('Vt 6 ml/kg + PEEP phù hợp')}).",
        f"Theo dõi cặp thông số động (Lactat mỗi 2–4h + ScvO₂ + bài niệu ≥ 0,5 ml/kg/h) ngăn chặn tình trạng điều trị 'mù', xác định chính xác khâu nào đang nghẽn giữa tiền gánh (CVP), vận chuyển oxy (Hb), bơm tim (Dobutamine) hay kiểm soát ổ nhiễm.",
        "B5.02, B5.03, B6.01, B7.05", ["Dich-hoi-suc", "Theo-doi"],
    ),

    # =========================================================================
    # 8 THẺ ❌ BẪY LÂM SÀNG & 🛑 CỜ ĐỎ (GỒM CẢ 4 CÂU LƯỢNG GIÁ ÔN TẬP)
    # =========================================================================
    trap(
        "SURGR1-TRAP-01", "B3", "Chờ sốt cao tăng bạch cầu mới nghĩ đến Sốc nhiễm khuẩn",
        f"Bệnh nhân cao tuổi sau mổ tiêu hóa lơ mơ, da nổi vân tím, tụt huyết áp, nhiệt độ đo 35,5°C và bạch cầu 3.200/mm³ — Sai lầm chẩn đoán nào dễ cướp đi giờ vàng?",
        f"1) <b>Ngộ nhận hay gặp:</b> Nghĩ không sốt cao và không tăng bạch cầu là 'không nhiễm trùng'.<br>"
        f"2) <b>Sự thật lâm sàng:</b> Cả {R('hạ thân nhiệt < 36°C')} lẫn {R('bạch cầu tụt < 4.000/mm³')} (hoặc band > 10%) đều là tiêu chuẩn chính thức của SIRS và thường gặp ở sốc nhiễm khuẩn thể nặng, suy giảm miễn dịch.",
        f"Chờ đến khi bệnh nhân sốt cao rét run mới cấy máu và dùng kháng sinh ở nhóm hạ thân nhiệt sẽ bỏ lỡ toàn bộ cửa sổ 1 giờ đầu tiên, đẩy tỷ lệ tử vong lên rất cao.",
        "B1.01, B3.02, B6.02", ["SIRS", "Lam-sang"],
    ),
    trap(
        "SURGR1-TRAP-02", "B4", "Nhầm lẫn giữa SIRS, qSOFA và dùng qSOFA = 1 để loại trừ Sepsis",
        f"Đừng đánh đồng 4 tiêu chuẩn SIRS với 3 tiêu chuẩn qSOFA hoặc thấy qSOFA chỉ 1 điểm mà loại trừ ngay Nhiễm khuẩn huyết?",
        f"1) <b>Khác biệt ngưỡng thông số:</b> SIRS dùng mạch >90, nhiệt >38/<36°C, BC, thở {B('> 20/phút')} (hoặc PaCO₂ <32); còn qSOFA chỉ dùng 3 dấu hiệu lâm sàng gồm thở {R('≥ 22/phút')}, {R('GCS < 15')} và {R('HATT ≤ 100 mmHg')}.<br>"
        f"2) <b>Giới hạn qSOFA:</b> qSOFA ≥ 2 là công cụ sàng lọc nhanh nguy cơ xấu tại giường; khi nghi ngờ lâm sàng dù qSOFA < 2 vẫn phải tính bảng {G('SOFA / MSOFA')} (ΔSOFA ≥ 2 điểm) để xác định Sepsis.",
        f"qSOFA có độ đặc hiệu khá tốt nhưng độ nhạy không tuyệt đối ở giai đoạn sớm; loại trừ Sepsis chỉ dựa vào qSOFA = 1 dễ bỏ sót các ca suy thận/tăng Bilirubin hoặc tụt tiểu cầu sớm.",
        "B1.01, B1.03, B4.01, B6.02", ["qSOFA", "SIRS"],
    ),
    trap(
        "SURGR1-TRAP-03", "B6", "Nhầm đích HATT ≥ 65 mmHg hoặc ScvO₂ ≤ 70% trong câu hỏi lượng giá",
        f"Trong bộ đích hồi sức sốc nhiễm khuẩn, hai thông số 'HATT ≥ 65 mmHg' và 'ScvO₂ ≤ 70%' sai ở điểm nào (bẫy kinh điển trong đề thi)?",
        f"1) <b>Lỗi thứ nhất (Huyết áp):</b> Đích bắt buộc là {G('Huyết áp động mạch trung bình (MAP) ≥ 65 mmHg')}, KHÔNG phải huyết áp tâm thu (HATT) ≥ 65 mmHg.<br>"
        f"2) <b>Lỗi thứ hai (Oxy tĩnh mạch):</b> Đích bắt buộc là {G('ScvO₂ ≥ 70%')} (hoặc {G('SvO₂ ≥ 65%')}) — ScvO₂ ≤ 70% chứng tỏ mô vẫn thiếu oxy nghiêm trọng chứ không phải đích đạt.<br>"
        f"3) <b>Nhắc lại đích máu đi kèm:</b> Hemoglobin phải duy trì {G('> 70 g/L')} (đích 70 – 90 g/L).",
        f"HATT chỉ 65 mmHg tương ứng MAP tụt xuống ~45–50 mmHg, gây ngừng lọc cầu thận và thiếu máu não tức thì. Còn ScvO₂ ≤ 70% cho thấy mô rút cạn oxy từ máu mao mạch do cung lượng tim/Hb/tưới máu chưa đủ.",
        "B6.01, B6.02", ["Dich-hoi-suc", "Luong-gia"],
    ),
    redflag(
        "SURGR1-TRAP-04", "B7", "Truyền dung dịch keo nhân tạo HES (Heasteril 6%) hoặc Gelatin để bù dịch sốc nhiễm khuẩn",
        f"Để nâng huyết áp nhanh cho bệnh nhân sốc nhiễm khuẩn tụt HA nặng, vì sao tuyệt đối KHÔNG được truyền Heasteril 6% (HES) hay Gelatin?",
        f"1) <b>Cấm tuyệt đối HES:</b> Dung dịch keo nhân tạo {R('HES (Hydroxyethyl Starch / Heasteril 6%) bị chống chỉ định')} trong sốc nhiễm khuẩn vì gây {R('tổn thương thận cấp nặng và làm tăng tỷ lệ tử vong')}.<br>"
        f"2) <b>Không chọn Gelatin:</b> Các dung dịch Gelatin không nằm trong lựa chọn ưu tiên.<br>"
        f"3) <b>Dung dịch chuẩn cần truyền:</b> Bù nhanh 30 ml/kg bằng {G('Ringer Lactat')} hoặc {G('NaCl 0,9%')}, có thể phối hợp {G('Albumin')} khi cần lượng dịch lớn.",
        f"Cơ chế lắng đọng phân tử tinh bột cao phân tử HES tại tế bào ống thận làm tắc nghẽn và hoại tử ống thận nặng nề hơn trên nền thận đang thiếu máu do sốc.",
        "B7.01, B6.02", ["Bu-dich", "Chong-chi-dinh", "Luong-gia"],
    ),
    trap(
        "SURGR1-TRAP-05", "B7", "Chọn Dopamine làm vận mạch đầu tay hoặc dùng 'Dopamine liều thấp bảo vệ thận'",
        f"Vì sao không dùng Dopamine làm lựa chọn hàng đầu cũng như không duy trì Dopamine liều thấp để 'bảo vệ thận' ở bệnh nhân sốc nhiễm khuẩn?",
        f"1) <b>Lựa chọn đầu tay chuẩn xác:</b> {G('Norepinephrine')} là vận mạch hàng đầu (First-line) bắt buộc lựa chọn (liều 0,05 – 0,1 µg/kg/phút) để duy trì MAP ≥ 65 mmHg.<br>"
        f"2) <b>Từ bỏ quan niệm cũ về Dopamine:</b> {R('Không dùng Dopamine liều thấp để bảo vệ thận')} vì không chứng minh được hiệu quả bảo vệ thận thực sự mà lại dễ kích hoạt loạn nhịp tim hơn Norepinephrine.",
        f"Trong các đề thi trắc nghiệm lẫn thực hành hồi sức hiện đại, khi hỏi thuốc vận mạch đầu tiên điều trị sốc nhiễm khuẩn, đáp án duy nhất đúng luôn là Norepinephrine — tránh bẫy chọn Dopamine hay Epinephrine làm hàng đầu.",
        "B7.02, B6.02", ["Van-mach", "Luong-gia"],
    ),
    trap(
        "SURGR1-TRAP-06", "B5", "Chẩn đoán bằng Khí máu tĩnh mạch hoặc Tiêm kháng sinh trước khi lấy Cấy máu",
        f"Trong chuỗi cận lâm sàng xác định sốc nhiễm khuẩn (Công thức máu, Khí máu động mạch, Cấy máu, Kháng sinh đồ), sai sót thao tác nào với Khí máu và Cấy máu sẽ làm hỏng giá trị chẩn đoán?",
        f"1) <b>Thứ tự trước – sau:</b> Phải lấy {G('cấy máu ít nhất 2 mẫu (ưa khí & kỵ khí)')} — tiêu chuẩn vàng vi sinh — và cấy bệnh phẩm trước khi tiêm liều kháng sinh đầu tiên (không trì hoãn quá mốc 1 giờ).<br>"
        f"2) <b>Đúng loại khí máu:</b> Phải làm {G('khí máu động mạch')} để đánh giá chính xác toan chuyển hóa và {B('PaO₂/FiO₂')}; {R('khí máu tĩnh mạch ít đặc hiệu hơn')}, không thay thế được.",
        f"Nếu tiêm kháng sinh phổ rộng rồi mới cấy máu, vi khuẩn bị ức chế mọc khiến tỷ lệ âm tính giả tăng cao, mất dữ liệu kháng sinh đồ để xuống thang chính xác về sau.",
        "B5.03, B5.04", ["Can-lam-sang", "Vi-sinh", "Luong-gia"],
    ),
    redflag(
        "SURGR1-TRAP-07", "B7", "Trì hoãn mổ giải quyết ổ nhiễm ngoại khoa để 'chờ điều trị nội khoa cho hết sốc trước'",
        f"Bệnh nhân sốc nhiễm khuẩn do sỏi mật nhiễm trùng (viêm đường mật mủ) hoặc áp xe ổ bụng — Sai lầm chết người nào xảy ra nếu giữ lại hồi sức nội khoa 1–2 ngày cho 'hết sốc hẳn' mới chuyển phòng mổ?",
        f"1) <b>Giới hạn tuyệt đối của thuốc:</b> {R('Kháng sinh đơn thuần không thể chữa khỏi')} nếu chưa dẫn lưu hoặc loại bỏ ổ mủ ngoại khoa.<br>"
        f"2) <b>Hành động chuẩn xác:</b> Tiến hành {R('phẫu thuật / can thiệp giải áp cấp cứu ngay khi hồi sức dịch bắt đầu')} (dẫn lưu áp xe, cắt ruột thừa viêm mủ, dẫn lưu mủ màng phổi, giải áp đường mật...).",
        f"Ổ nhiễm trùng kín như quả bom liên tục bơm vi khuẩn và nội độc tố vào máu. Trì hoãn kiểm soát nguồn nhiễm làm bệnh nhân rơi nhanh vào sốc trơ vận mạch và suy đa tạng không hồi phục.",
        "B7.03, B7.04", ["Ngoai-khoa", "Cap-cuu"],
    ),
    redflag(
        "SURGR1-TRAP-08", "B7", "Lạm dụng Corticoid từ đầu hoặc Truyền hồng cầu khi Hb còn > 70 g/L",
        f"Vì sao không tiêm Hydrocortisone thường quy cho mọi ca sốc nhiễm khuẩn từ phút đầu tiên, và không truyền hồng cầu khối khi Hemoglobin còn 85 g/L?",
        f"1) <b>Giới hạn chỉ định Hydrocortisone:</b> Chỉ dùng {Y('Hydrocortisone 200 mg/ngày')} khi {R('huyết động không đáp ứng với bù dịch và thuốc vận mạch liều cao')} (sốc trơ).<br>"
        f"2) <b>Ngưỡng truyền hồng cầu khối:</b> Chỉ truyền khi {R('Hemoglobin < 70 g/L')} với mục tiêu duy trì vừa đủ trong khoảng {G('70 – 90 g/L')}.",
        f"Dùng Corticoid bừa bãi sớm làm tăng nguy cơ bội nhiễm và tăng đường huyết (mục tiêu cần giữ < 10 mmol/L [180 mg/dL]); còn truyền máu quá ngưỡng 70–90 g/L không cải thiện sống còn mà tăng nguy cơ tổn thương phổi liên quan truyền máu (TRALI) và quá tải dịch.",
        "B7.05, B6.01", ["Ho-tro", "Corticoid", "Truyen-mau"],
    ),
]
