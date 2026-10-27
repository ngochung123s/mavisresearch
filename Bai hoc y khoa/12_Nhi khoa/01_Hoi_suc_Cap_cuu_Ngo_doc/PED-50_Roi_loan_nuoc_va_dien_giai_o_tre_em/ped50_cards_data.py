# -*- coding: utf-8 -*-
# PED-50 Rối loạn chuyển hóa nước điện giải ở trẻ em — nguồn thẻ duy nhất (barem gốc: handout slide Bộ môn Nhi).
# Mã barem từng dòng: PED-50_Roi_loan_nuoc_va_dien_giai_o_tre_em_PEDYTB.md (mỗi mã [Bx.yy] phải có ≥ 1 thẻ, ghi ở `extra`).


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / triệu chứng bệnh lý / chống chỉ định
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / lứa tuổi
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc
    return _c("#51cf66", t)


def B(t):  # tên bệnh / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("🏛️ BAREM GỐC · SLIDE BỘ MÔN NHI", "badge-barem")
SRC = "📖 Nguồn: Handout slide bài giảng Rối loạn nước điện giải ở trẻ em — Bộ môn Nhi ĐHYDTB (ThS.BSCKII. Khúc Văn Lập). Barem: "


def basic(cid, section, category, tier, front, core, ai, barem, tags, asks=None):
    card = {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": SRC + barem,
        "tags": ["PED-50", "Barem-goc"] + tags,
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
        "tags": ["PED-50", "Barem-goc", "Cloze-phu"] + tags,
    }


cards_data = [
    # ------------------------------------------------------------ B0. Mục tiêu
    basic(
        "PED50-B0-01", "B0", "Mục tiêu bài học", 1,
        f"{B('[Mục tiêu bài học]')} Ba mục tiêu của bài Rối loạn nước điện giải ở trẻ em là gì?",
        f"1) Trình bày {G('sinh lý của chuyển hóa nước điện giải')} ở trẻ em.<br>"
        f"2) Trình bày {R('tình trạng mất nước')} ở trẻ em.<br>"
        f"3) Trình bày {G('cách điều trị tình trạng rối loạn nước điện giải')} ở trẻ em.",
        "Ba mục tiêu đi theo một trình tự: nền sinh lý (nước và điện giải phân bố thế nào), rồi đến bệnh cảnh mất nước, "
        "cuối cùng là cách xử trí. Học theo đúng trình tự này sẽ dễ hiểu lý do vì sao bước điều trị cần đến các con số của "
        "phần sinh lý.",
        "B0.01, B0.02, B0.03", ["Muc-tieu"],
    ),

    # ------------------------------------------------------------ B1. Khối lượng nước trong cơ thể
    basic(
        "PED50-B1-01", "B1", "Khối lượng nước trong cơ thể", 1,
        f"{B('[Khối lượng nước trong cơ thể trẻ em]')} Công thức ước tính khối lượng nước trong cơ thể trẻ em theo cân nặng là gì?",
        f"{G('V (lít) = 0,6 × P (kg) + 0,25')}.",
        "Công thức này là nền của các phép tính sau (B11–B13): hệ số 0,6 là tỷ lệ nước trung bình của cơ thể theo cân nặng, "
        "còn 0,25 là phần hiệu chỉnh cộng thêm. Cần nhớ công thức này để tính được thể tích nước của trẻ khi mất nước.",
        "B1.01", ["Khoi-luong-nuoc"],
    ),
    basic(
        "PED50-B1-02", "B1", "Khối lượng nước trong cơ thể", 2,
        f"{B('[Lượng nước theo tuổi]')} Lượng nước (% cân nặng) theo tuổi là bao nhiêu ở 1 tháng, 6 tháng, 12 tháng, 5 tuổi và 15 tuổi?",
        f"1) 1 tháng: {Y('70%')}.<br>2) 6 tháng: {Y('70%')}.<br>3) 12 tháng: {Y('65%')}.<br>"
        f"4) 5 tuổi: {Y('60%')}.<br>5) 15 tuổi: {Y('60%')}.",
        "Tỷ lệ nước giảm dần khi trẻ lớn: trẻ càng nhỏ, mô mỡ càng ít và tỷ lệ nước trên cân nặng càng cao. Vì vậy một lượng "
        "mất nước tính theo % cân nặng ở trẻ nhỏ đại diện cho một tỷ lệ nước cơ thể lớn hơn.",
        "B1.02", ["Luong-nuoc-theo-tuoi"],
    ),
    basic(
        "PED50-B1-03", "B1", "Khối lượng nước trong cơ thể", 2,
        f"{B('[Nước ngoài tế bào theo tuổi]')} Theo bảng barem, chỉ số nước ngoài tế bào ở 1 tháng, 6 tháng, 12 tháng, 5 tuổi và 15 tuổi là bao nhiêu?",
        f"1) 1 tháng: {Y('60')}.<br>2) 6 tháng: {Y('50')}.<br>3) 12 tháng: {Y('47')}.<br>"
        f"4) 5 tuổi: {Y('45')}.<br>5) 15 tuổi: {Y('36')}.",
        "Giá trị ghi đúng như bảng barem (bảng không ghi đơn vị của hàng này). Lưu ý: ở ảnh chụp slide, hai ô đầu (1 tháng và "
        "6 tháng) đọc được là 60 và 50 nhưng ảnh bị mờ nên chưa chắc chắn tuyệt đối. Quy luật chung vẫn là giảm dần theo tuổi, "
        "giống với lượng nước toàn phần.",
        "B1.03", ["Nuoc-ngoai-te-bao"],
    ),
    basic(
        "PED50-B1-04", "B1", "Khối lượng nước trong cơ thể", 2,
        f"{B('[Thể tích máu và huyết tương]')} Thể tích máu và thể tích huyết tương của trẻ em bằng bao nhiêu phần trăm trọng lượng?",
        f"1) Thể tích máu: {Y('8% trọng lượng')}.<br>2) Thể tích huyết tương: {Y('5% trọng lượng')}.",
        "Thể tích máu lớn gấp khoảng 1,6 lần thể tích huyết tương (8/5). Đây là lý do khi mất dịch, phần giảm đi trước tiên "
        "là khối lượng tuần hoàn — biểu hiện bằng huyết áp và tưới máu, sẽ được dùng ở B9.",
        "B1.04", ["The-tich-mau"],
    ),

    # ------------------------------------------------------------ B2. Nhu cầu nước theo cân nặng
    basic(
        "PED50-B2-01", "B2", "Nhu cầu nước theo cân nặng", 1,
        f"{B('[Nhu cầu nước theo cân nặng]')} Nhu cầu nước (ml/kg/24h) theo các khoảng cân nặng: dưới 10 kg, từ 10–40 kg và trên 40 kg là bao nhiêu?",
        f"1) Trẻ {Y('< 10 kg')}: {G('120–150 ml/kg/24h')}.<br>2) Trẻ {Y('10–40 kg')}: {G('70–110 ml/kg/24h')}.<br>"
        f"3) Trẻ {Y('> 40 kg')}: {G('40–50 ml/kg/24h')}.",
        "Nhu cầu nước tính trên mỗi kg giảm dần khi cân nặng tăng: trẻ càng nhỏ, chuyển hóa tính theo khối lượng càng cao "
        "nên cần nhiều nước hơn trên mỗi kg.",
        "B2.01, B2.02, B2.03", ["Nhu-cau-nuoc"],
    ),
    basic(
        "PED50-B2-02", "B2", "Nhu cầu nước theo cân nặng", 2,
        f"{B('[Nhu cầu nước]')} Nhu cầu nước của trẻ phụ thuộc vào những yếu tố nào?",
        f"1) {G('Chuyển hóa')}.<br>2) {G('Khối lượng thức ăn')}.<br>3) {G('Hoạt động cơ thể')}.<br>"
        f"4) {G('Tốc độ lớn')}.<br>5) {G('Nhiệt độ môi trường')}.",
        "Năm yếu tố này đều làm thay đổi lượng nước cơ thể sử dụng và mất đi mỗi ngày. Khi trẻ sốt, hoạt động nhiều, ăn nhiều "
        "hoặc môi trường nóng, nhu cầu nước tăng so với mức chuẩn ở B2.01–B2.03.",
        "B2.04", ["Nhu-cau-nuoc"],
    ),

    # ------------------------------------------------------------ B3. Nguồn nước và nhu cầu duy trì
    basic(
        "PED50-B3-01", "B3", "Nguồn nước và nhu cầu duy trì", 1,
        f"{B('[Nguồn nước của trẻ]')} Nước của trẻ được thỏa mãn từ những nguồn nào?",
        f"1) {G('Ăn')}.<br>2) {G('Uống')}.<br>3) {G('Chuyển hóa')}.",
        "Ba nguồn này bù lại lượng nước đã mất đi hằng ngày. Nguồn chuyển hóa là nước được tạo ra từ phản ứng oxy hóa các chất "
        "dinh dưỡng, được tính riêng ở B3.02.",
        "B3.01", ["Nguon-nuoc"],
    ),
    basic(
        "PED50-B3-02", "B3", "Nguồn nước và nhu cầu duy trì", 2,
        f"{B('[Nước chuyển hóa]')} Mỗi 100 g Protid, Glucid và Lipid cho được bao nhiêu ml nước?",
        f"1) 100 g {B('Protid')} cho {Y('56 ml')} nước.<br>2) 100 g {B('Glucid')} cho {Y('42 ml')} nước.<br>"
        f"3) 100 g {B('Lipid')} cho {Y('107 ml')} nước.",
        "Lipid cho nhiều nước chuyển hóa nhất trên mỗi 100 g, rồi đến Protid, Glucid. Nước chuyển hóa là nguồn đóng góp trong "
        "phép tính nhu cầu duy trì ở B3.03.",
        "B3.02", ["Nuoc-chuyen-hoa"],
    ),
    basic(
        "PED50-B3-03", "B3", "Nguồn nước và nhu cầu duy trì", 1,
        f"{B('[Nhu cầu nước duy trì]')} Nhu cầu nước duy trì được tính theo công thức nào?",
        f"{G('Nhu cầu nước duy trì = Nước mất vô hình + Nước tiểu − Nước nội sinh')}.",
        "Nước nội sinh là nước được cơ thể tạo ra từ chuyển hóa, nên được trừ ra khỏi tổng nước mất. Phần còn lại là lượng nước "
        "cần đưa vào từ bên ngoài để giữ cân bằng.",
        "B3.03", ["Nhu-cau-duy-tri"],
    ),
    basic(
        "PED50-B3-04", "B3", "Nguồn nước và nhu cầu duy trì", 2,
        f"{B('[Nước mất vô hình]')} Nước mất vô hình qua các đường nào và chiếm tỷ lệ bao nhiêu phần trăm?",
        f"1) Qua da: {Y('30%')}.<br>2) Qua phổi: {Y('15%')}.<br>3) Qua phân: {Y('5%')}.",
        "Mất vô hình là lượng nước mất mà người bệnh không nhận thấy. Da là đường mất lớn nhất; khi sốt hoặc ra nhiều mồ hôi, "
        "phần qua da tăng mạnh.",
        "B3.04", ["Mat-vo-hinh"],
    ),
    basic(
        "PED50-B3-05", "B3", "Nguồn nước và nhu cầu duy trì", 2,
        f"{B('[Nước mất qua nước tiểu]')} Nước mất qua nước tiểu chiếm bao nhiêu phần trăm?",
        f"{Y('50%')} lượng nước mất (qua nước tiểu).",
        "Nước tiểu là đường mất lớn thứ hai sau mất vô hình qua da. Khi bệnh lý làm tăng thể tích nước tiểu thì phần này tăng và "
        "làm tăng nhu cầu duy trì.",
        "B3.05", ["Nuoc-tieu"],
    ),
    basic(
        "PED50-B3-06", "B3", "Nguồn nước và nhu cầu duy trì", 2,
        f"{B('[Mất vô hình tăng khi nào]')} Nước mất vô hình tăng lên trong những trường hợp nào?",
        f"1) {R('Sốt')}.<br>2) {R('Ra nhiều mồ hôi')}.<br>3) {R('Nhiệt độ môi trường tăng cao')}, …",
        "Barem liệt kê ba yếu tố rồi kết thúc bằng dấu '…'. Cả ba đều làm tăng bốc hơi qua da và phổi — hai đường chiếm tới 45% "
        "nước mất vô hình — nên trẻ sốt hoặc nằm phòng nóng cần thêm dịch so với nhu cầu duy trì.",
        "B3.06", ["Mat-vo-hinh"],
    ),

    # ------------------------------------------------------------ B4. Ước tính nhu cầu nước duy trì
    basic(
        "PED50-B4-01", "B4", "Cách ước tính nhu cầu nước duy trì", 1,
        f"{B('[Ước tính theo diện tích da]')} Nhu cầu nước duy trì ước tính theo diện tích da là bao nhiêu?",
        f"{Y('1500 ml/m²/24h')}.",
        "Phương pháp diện tích da thường dùng khi cần một con số nhanh và tương đối ổn định cho trẻ có cân nặng và chiều cao "
        "bình thường; các phương pháp khác dùng để đối chiếu.",
        "B4.01", ["Dien-tich-da"],
    ),
    basic(
        "PED50-B4-02", "B4", "Cách ước tính nhu cầu nước duy trì", 2,
        f"{B('[Ước tính theo năng lượng]')} Nhu cầu nước duy trì ước tính theo năng lượng là bao nhiêu?",
        f"{Y('100–150 ml/100 kcal')}.",
        "Cách tính theo năng lượng liên hệ trực tiếp với lượng calo trẻ tiêu thụ: mỗi 100 kcal tiêu thụ cần khoảng 100–150 ml nước.",
        "B4.02", ["Theo-nang-luong"],
    ),
    basic(
        "PED50-B4-03", "B4", "Cách ước tính nhu cầu nước duy trì", 1,
        f"{B('[Holliday–Segar theo cân nặng]')} Theo Holliday–Segar, nhu cầu nước duy trì (ml/kg/24h) theo các khoảng cân nặng là bao nhiêu?",
        f"1) {Y('10 kg đầu')}: {G('100 ml/kg/24h')}.<br>2) {Y('10 kg tiếp theo')}: {G('50 ml/kg/24h')}.<br>"
        f"3) {Y('Sau 20 kg')}: {G('20 ml/kg/24h')}.",
        "Đây là cách tính theo bậc cân nặng: 10 kg đầu tính 100 ml/kg, 10 kg tiếp theo tính 50 ml/kg, phần còn lại tính 20 ml/kg. "
        "Đây là công thức được dùng nhiều nhất để tính nhu cầu duy trì khi cần một con số theo cân nặng.",
        "B4.03", ["Holliday-Segar"],
    ),
    algo(
        "PED50-ALGO-01", "B4", "Công thức Holliday–Segar",
        "Holliday–Segar: tính nhu cầu duy trì 24h theo cân nặng như thế nào?",
        f"1) {Y('10 kg đầu')}: {G('100 ml/kg/24h')} → nhân với cân nặng ở phần này.<br>"
        f"2) {Y('10 kg tiếp theo')}: {G('50 ml/kg/24h')} → nhân với phần cân nặng trong 10 kg tiếp theo.<br>"
        f"3) {Y('Phần còn lại (sau 20 kg)')}: {G('20 ml/kg/24h')} → nhân với phần cân nặng vượt 20 kg.<br>"
        f"4) Cộng ba phần lại để có nhu cầu duy trì tổng 24h.",
        "Chia cân nặng thành ba bậc rồi cộng. Ví dụ trẻ 5 kg: 5 × 100 = 500 ml/24h — đây là cách tính áp dụng trong VD1 và VD2 ở B11–B12.",
        "B4.03", ["Holliday-Segar"],
    ),

    # ------------------------------------------------------------ B5. Phân bố điện giải
    basic(
        "PED50-B5-01", "B5", "Phân bố điện giải trong cơ thể", 1,
        f"{B('[Phân bố Na⁺ và K⁺]')} Nồng độ Na⁺ và K⁺ trong huyết tương và trong tế bào (mEq/l) là bao nhiêu?",
        f"1) {B('Na⁺')}: huyết tương {Y('145')}; trong tế bào {Y('5–10')}.<br>"
        f"2) {B('K⁺')}: huyết tương {Y('3–5')}; trong tế bào {Y('150')}.",
        "Đây là cặp ion quan trọng nhất của bài: Na⁺ chủ yếu ở ngoài tế bào, K⁺ chủ yếu ở trong tế bào. Sự chênh lệch hai ion này "
        "tạo ra điện thế màng và giải thích vì sao rối loạn Na⁺ và K⁺ có biểu hiện khác nhau.",
        "B5.01", ["Phan-bo-dien-giai"],
    ),
    basic(
        "PED50-B5-02", "B5", "Phân bố điện giải trong cơ thể", 2,
        f"{B('[Phân bố Ca⁺⁺ và Mg⁺⁺]')} Nồng độ Ca⁺⁺ và Mg⁺⁺ (mEq/l) trong huyết tương và trong tế bào là bao nhiêu?",
        f"1) {B('Ca⁺⁺')}: huyết tương {Y('3–5')}; trong tế bào {Y('3')}.<br>"
        f"2) {B('Mg⁺⁺')}: huyết tương {Y('2')}; trong tế bào {Y('30')}.",
        "Mg⁺⁺ nội bào cao hơn nhiều so với huyết tương, trong khi Ca⁺⁺ hai bên xấp xỉ nhau. Điều này cho thấy Mg⁺⁺ chủ yếu là ion "
        "nội bào.",
        "B5.02", ["Phan-bo-dien-giai"],
    ),
    basic(
        "PED50-B5-03", "B5", "Phân bố điện giải trong cơ thể", 2,
        f"{B('[Phân bố Cl⁻ và HCO₃⁻]')} Nồng độ Cl⁻ và HCO₃⁻ (mEq/l) trong huyết tương và trong tế bào là bao nhiêu?",
        f"1) {B('Cl⁻')}: huyết tương {Y('103')}; trong tế bào {Y('5–10')}.<br>"
        f"2) {B('HCO₃⁻')}: huyết tương {Y('26')}; trong tế bào {Y('10')}.",
        "Cl⁻ và HCO₃⁻ là anion chủ yếu ngoài tế bào (Cl⁻) và bảo tồn cân bằng toan kiềm (HCO₃⁻). Nồng độ nội bào thấp hơn "
        "nhiều so với huyết tương.",
        "B5.03", ["Phan-bo-dien-giai"],
    ),

    # ------------------------------------------------------------ B6. Nhu cầu điện giải
    basic(
        "PED50-B6-01", "B6", "Nhu cầu điện giải", 1,
        f"{B('[Nhu cầu điện giải theo cân nặng]')} Nhu cầu Na⁺, K⁺, Mg⁺⁺ và Ca⁺⁺ mỗi ngày là bao nhiêu (theo kg/24h)?",
        f"1) {B('Na⁺')}: {G('2–3 mEq/kg/24h')}.<br>2) {B('K⁺')}: {G('1–2 mEq/kg/24h')}.<br>"
        f"3) {B('Mg⁺⁺')}: {G('0,4–0,8 mEq/kg/24h')}.<br>4) {B('Ca⁺⁺')}: {G('50–200 mg/kg/24h')}.",
        "Nhu cầu Na⁺ cao nhất trong bốn ion, phản ánh vai trò chính của Na⁺ trong thể tích ngoại bào. Các con số này là nhu cầu "
        "duy trì, dùng để tính điện giải đưa vào trong dịch truyền (xem B11–B13).",
        "B6.01, B6.02, B6.03, B6.04", ["Nhu-cau-dien-giai"],
    ),
    basic(
        "PED50-B6-02", "B6", "Nhu cầu điện giải", 2,
        f"{B('[Nhu cầu Na⁺]')} Nhu cầu Na⁺ mỗi ngày (mEq/kg/24h) là bao nhiêu?",
        f"{G('2–3 mEq/kg/24h')}.",
        "Na⁺ là ion cần nhiều nhất và là ion điều hòa thể tích dịch ngoại bào; vì vậy nhu cầu Na⁺ là một thành phần chính của "
        "phép tính dịch điều trị ở B11–B13.",
        "B6.01", ["Nhu-cau-Na"],
    ),
    basic(
        "PED50-B6-03", "B6", "Nhu cầu điện giải", 2,
        f"{B('[Nhu cầu K⁺ và Mg⁺⁺]')} Nhu cầu K⁺ và Mg⁺⁺ mỗi ngày là bao nhiêu (mEq/kg/24h)?",
        f"1) {B('K⁺')}: {G('1–2 mEq/kg/24h')}.<br>2) {B('Mg⁺⁺')}: {G('0,4–0,8 mEq/kg/24h')}.",
        "K⁺ là ion nội bào và cần duy trì đều đặn để giữ điện thế màng. Mg⁺⁺ cũng là ion nội bào, nhu cầu thấp hơn K⁺.",
        "B6.02, B6.03", ["Nhu-cau-K-Mg"],
    ),
    basic(
        "PED50-B6-04", "B6", "Nhu cầu điện giải", 2,
        f"{B('[Nhu cầu Ca⁺⁺]')} Nhu cầu Ca⁺⁺ mỗi ngày là bao nhiêu (mg/kg/24h)?",
        f"{G('50–200 mg/kg/24h')}.",
        "Đơn vị của canxi là mg chứ không phải mEq như các ion khác trong barem này. Khi tính dịch cần chú ý đổi đơn vị "
        "cho đúng.",
        "B6.04", ["Nhu-cau-Ca"],
    ),
    cloze(
        "PED50-B6-05", "B6", "Nhu cầu điện giải",
        f"Nhu cầu Na⁺ mỗi ngày là {{{{c1::{Y('2–3 mEq/kg/24h')}}}}}.",
        "B6.01", ["Nhu-cau-Na"],
    ),

    # ------------------------------------------------------------ B7. Đánh giá mức độ mất nước (bảng)
    basic(
        "PED50-B7-01", "B7", "Đánh giá mức độ mất nước", 1,
        f"{B('[Cân nặng giảm theo mức độ mất nước]')} Tỷ lệ cân nặng giảm (%) ở các mức: chưa mất nước, mất nước nhẹ–vừa, mất nước nặng và nguy kịch là bao nhiêu?",
        f"1) Chưa mất nước: {Y('≤ 5%')}.<br>2) Mất nước nhẹ và vừa: {Y('6–9%')}.<br>"
        f"3) Mất nước nặng: {Y('10–15%')}.<br>4) Nguy kịch: {R('≥ 15%')}.",
        "Cân nặng giảm là tiêu chí định lượng đầu tiên để phân độ mất nước. Mức nặng và nguy kịch đều liên quan đến rối loạn huyết động.",
        "B7.01", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-02", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Tinh thần theo mức độ mất nước]')} Biểu hiện tinh thần ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch là gì?",
        f"1) Chưa mất nước: {G('bình thường')}.<br>2) Mất nước nhẹ và vừa: {Y('kích thích')}.<br>"
        f"3) Mất nước nặng: {R('mệt, li bì')}.<br>4) Nguy kịch: {R('hôn mê')}.",
        "Tinh thần đi từ bình thường đến kích thích rồi li bì và hôn mê khi mất nước càng nặng. Hôn mê là dấu hiệu nguy kịch.",
        "B7.02", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-03", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Khát theo mức độ mất nước]')} Biểu hiện khát ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch là gì?",
        f"1) Chưa mất nước: {G('uống bình thường')}.<br>2) Mất nước nhẹ và vừa: {Y('khát, uống háo hức')}.<br>"
        f"3) Mất nước nặng: {R('uống kém, không uống được')}.<br>4) Nguy kịch: không ghi trong barem (ô trống).",
        "Khát tăng khi mất nước nhẹ–vừa (uống háo hức), rồi giảm hẳn khi mất nước nặng, lúc trẻ không uống được. Ô nguy kịch "
        "trong barem để trống nên không có mô tả.",
        "B7.03", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-04", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Miệng lưỡi theo mức độ mất nước]')} Biểu hiện miệng lưỡi ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch là gì?",
        f"1) Chưa mất nước: {G('ướt')}.<br>2) Mất nước nhẹ và vừa: {Y('khô')}.<br>"
        f"3) Mất nước nặng: {R('rất khô')}.<br>4) Nguy kịch: {R('rất khô')}.",
        "Miệng lưỡi khô tăng dần theo mức độ mất nước. Biểu hiện này nhìn thấy được và kiểm tra nhanh tại giường.",
        "B7.04", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-05", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Mắt theo mức độ mất nước]')} Biểu hiện mắt ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch là gì?",
        f"1) Chưa mất nước: {G('bình thường')}.<br>2) Mất nước nhẹ và vừa: {Y('trũng')}.<br>"
        f"3) Mất nước nặng: {R('rất trũng')}.<br>4) Nguy kịch: {R('rất trũng')}.",
        "Mắt trũng là dấu hiệu nhạy để nhận ra mất nước ở trẻ nhỏ, khi nhãn cầu bị lún xuống do mất thể tích.",
        "B7.05", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-06", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Nước mắt theo mức độ mất nước]')} Biểu hiện nước mắt ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch là gì?",
        f"1) Chưa mất nước: {G('bình thường')}.<br>2) Mất nước nhẹ và vừa: {Y('ít')}.<br>"
        f"3) Mất nước nặng: {R('không có')}.<br>4) Nguy kịch: {R('không có')}.",
        "Nước mắt giảm dần rồi mất hẳn khi mất nước nặng. Biểu hiện này phản ánh thể tích dịch giảm.",
        "B7.06", ["Phan-do-mat-nuoc"],
    ),
    basic(
        "PED50-B7-07", "B7", "Đánh giá mức độ mất nước", 2,
        f"{B('[Nếp véo da theo mức độ mất nước]')} Nếp véo da mất đi nhanh hay chậm ở các mức: chưa mất nước, mất nước nhẹ–vừa, nặng và nguy kịch?",
        f"1) Chưa mất nước: {G('mất nhanh')}.<br>2) Mất nước nhẹ và vừa: {Y('mất chậm')}.<br>"
        f"3) Mất nước nặng: {R('mất rất chậm')}.<br>4) Nguy kịch: {R('mất rất chậm')}.",
        "Nếp véo da mất càng chậm khi da càng mất đàn hồi do mất nước. Đây là dấu hiệu lâm sàng được dùng nhiều nhất để đánh giá "
        "mất nước ở trẻ nhỏ.",
        "B7.07", ["Phan-do-mat-nuoc"],
    ),
    cloze(
        "PED50-B7-08", "B7", "Đánh giá mức độ mất nước",
        f"Mất nước nặng khi cân nặng giảm {{{{c1::{Y('10–15%')}}}}}.",
        "B7.01", ["Phan-do-mat-nuoc"],
    ),

    # ------------------------------------------------------------ B8. Các loại mất nước (bảng)
    basic(
        "PED50-B8-01", "B8", "Các loại mất nước", 1,
        f"{B('[Đẳng trương, ưu trương, nhược trương — biểu hiện lâm sàng]')} Biểu hiện lâm sàng của mất nước đẳng trương, ưu trương và nhược trương là gì?",
        f"1) {B('Đẳng trương')}: {Y('khát, Casper (+)')}.<br>2) {B('Ưu trương')}: {Y('kích thích, khát, Casper (+/−)')}.<br>"
        f"3) {B('Nhược trương')}: {R('li bì, uống kém, Casper (++), cơ địa SDD')}.",
        "Mất nước ưu trương gây kích thích và khát vì thẩm thấu máu tăng; mất nước nhược trương gây li bì vì não bị phù. Casper "
        "là dấu hiệu tăng trương lực mô, càng rõ ở mất nước nhược trương.",
        "B8.01", ["Phan-loai-mat-nuoc"],
    ),
    basic(
        "PED50-B8-02", "B8", "Các loại mất nước", 2,
        f"{B('[Nguyên nhân các loại mất nước]')} Nguyên nhân của mất nước đẳng trương, ưu trương và nhược trương là gì?",
        f"1) {B('Đẳng trương')}: {G('tiêu chảy, nôn')}.<br>2) {B('Ưu trương')}: {G('say nóng, nắng, ra nhiều mồ hôi, đái nhạt, đái đường')}.<br>"
        f"3) {B('Nhược trương')}: {G('tiêu chảy')}.",
        "Mất nước đẳng trương và nhược trương hay gặp do tiêu chảy, nôn. Mất nước ưu trương thường do mất nhiều nước hơn điện giải "
        "(say nóng, ra mồ hôi, đái nhạt, đái đường).",
        "B8.02", ["Phan-loai-mat-nuoc"],
    ),
    basic(
        "PED50-B8-03", "B8", "Các loại mất nước", 2,
        f"{B('[Lượng nước mất theo loại mất nước]')} Lượng nước mất (ml/kg) của mất nước đẳng trương, ưu trương và nhược trương là bao nhiêu?",
        f"1) {B('Đẳng trương')}: {Y('100–150 ml/kg')}.<br>2) {B('Ưu trương')}: {Y('120–170 ml/kg')}.<br>"
        f"3) {B('Nhược trương')}: {Y('40–80 ml/kg')}.",
        "Lượng nước mất ở ưu trương lớn nhất, nhược trương nhỏ nhất. Đây là số liệu dùng để ước tính lượng nước cần bù.",
        "B8.03", ["Phan-loai-mat-nuoc"],
    ),
    basic(
        "PED50-B8-04", "B8", "Các loại mất nước", 2,
        f"{B('[Lượng Na mất theo loại mất nước]')} Lượng Na mất (mEq/kg) của mất nước đẳng trương, ưu trương và nhược trương là bao nhiêu?",
        f"1) {B('Đẳng trương')}: {Y('7–11 mEq/kg')}.<br>2) {B('Ưu trương')}: {Y('2–5 mEq/kg')}.<br>"
        f"3) {B('Nhược trương')}: {Y('10–14 mEq/kg')}.",
        "Mất nước nhược trương mất nhiều Na⁺ trên mỗi kg (10–14), còn mất nước ưu trương mất ít Na⁺ (2–5). Điều này khớp với "
        "chiều thay đổi natri máu ở B8.05.",
        "B8.04", ["Phan-loai-mat-nuoc"],
    ),
    basic(
        "PED50-B8-05", "B8", "Các loại mất nước", 2,
        f"{B('[Na máu theo loại mất nước]')} Natri máu (mEq/l) của mất nước đẳng trương, ưu trương và nhược trương là bao nhiêu?",
        f"1) {B('Đẳng trương')}: {Y('130–150')}.<br>2) {B('Ưu trương')}: {Y('> 150')}.<br>"
        f"3) {B('Nhược trương')}: {Y('< 130')}.",
        "Na máu là tiêu chí phân loại chính: đẳng trương trong khoảng bình thường, ưu trương cao hơn 150, nhược trương thấp hơn 130.",
        "B8.05", ["Phan-loai-mat-nuoc"],
    ),
    basic(
        "PED50-B8-06", "B8", "Các loại mất nước", 2,
        f"{B('[Áp lực thẩm thấu máu theo loại mất nước]')} Áp lực thẩm thấu máu (mOsmol/l) của mất nước đẳng trương, ưu trương và nhược trương là bao nhiêu?",
        f"1) {B('Đẳng trương')}: {Y('275–295')}.<br>2) {B('Ưu trương')}: {Y('> 310')}.<br>"
        f"3) {B('Nhược trương')}: {Y('< 275')}.",
        "Áp lực thẩm thấu máu cùng chiều với natri máu: ưu trương tăng cao, nhược trương giảm thấp, đẳng trương nằm trong khoảng "
        "bình thường.",
        "B8.06", ["Phan-loai-mat-nuoc"],
    ),
    cloze(
        "PED50-B8-07", "B8", "Các loại mất nước",
        f"Mất nước nhược trương khi Na máu {{{{c1::{Y('< 130 mEq/l')}}}}}.",
        "B8.05", ["Phan-loai-mat-nuoc"],
    ),

    # ------------------------------------------------------------ B9. Hậu quả của mất nước
    basic(
        "PED50-B9-01", "B9", "Hậu quả của mất nước", 1,
        f"{B('[Giảm khối lượng tuần hoàn]')} Mất nước gây giảm khối lượng tuần hoàn với những biểu hiện nào?",
        f"1) {R('Huyết áp hạ')}.<br>2) {R('Đái ít')}.<br>3) {R('Cô đặc máu')}.<br>4) {R('Trụy mạch')}.",
        "Đây là chuỗi hậu quả đầu tiên: giảm thể tích tuần hoàn làm huyết áp hạ, thận đái ít, máu cô đặc và cuối cùng là trụy mạch.",
        "B9.01", ["Hau-qua-mat-nuoc"],
    ),
    basic(
        "PED50-B9-02", "B9", "Hậu quả của mất nước", 2,
        f"{B('[Rối loạn thẩm thấu và trao đổi chất]')} Mất nước gây rối loạn những gì tiếp theo?",
        f"1) {R('Rối loạn áp lực thẩm thấu')}.<br>2) {R('Rối loạn trao đổi chất')}.",
        "Khi thể tích và thẩm thấu thay đổi, các quá trình chuyển hóa trong tế bào bị rối loạn theo.",
        "B9.02", ["Hau-qua-mat-nuoc"],
    ),
    basic(
        "PED50-B9-03", "B9", "Hậu quả của mất nước", 2,
        f"{B('[Rối loạn ion chức năng]')} Mất nước gây rối loạn những gì ở các ion chức năng?",
        f"{R('Rối loạn các Ion chức năng')}.",
        "Các ion chức năng (Na⁺, K⁺, Ca⁺⁺…) cần cho điện thế màng và co cơ; khi chúng rối loạn thì biểu hiện thần kinh và cơ "
        "sẽ xuất hiện (xem B14–B24).",
        "B9.03", ["Hau-qua-mat-nuoc"],
    ),
    basic(
        "PED50-B9-04", "B9", "Hậu quả của mất nước", 1,
        f"{B('[Tổn thương tế bào]')} Hậu quả cuối cùng của mất nước là gì?",
        f"{R('Tổn thương tế bào')}.",
        "Khi các rối loạn thể tích, thẩm thấu và ion kéo dài thì tế bào bị tổn thương. Đây là hậu quả cuối và cũng là lý do cần xử trí "
        "sớm mất nước.",
        "B9.04", ["Hau-qua-mat-nuoc"],
    ),

    # ------------------------------------------------------------ B10. Điều trị mất nước
    basic(
        "PED50-B10-01", "B10", "Điều trị mất nước", 1,
        f"{B('[Phác đồ điều trị mất nước]')} Điều trị mất nước theo phác đồ nào?",
        f"{G('Phác đồ A, B, C')}.",
        "Barem chỉ ghi tên phác đồ A, B, C mà không có nội dung chi tiết trong bản nhập. Khi thi cần đối chiếu lại slide gốc để biết "
        "nội dung từng phác đồ; không tự suy diễn nội dung trong thẻ này.",
        "B10.01", ["Dieu-tri-mat-nuoc"],
    ),

    # ------------------------------------------------------------ B11. VD1 — mất nước đẳng trương
    basic(
        "PED50-B11-01", "B11", "VD1 — Mất nước đẳng trương", 1,
        f"{B('[VD1 — đề bài đẳng trương]')} Trẻ {Y('5 kg')} mất {Y('10%')} trọng lượng cơ thể. Hãy tính lượng nước mất và nhu cầu duy trì.",
        f"1) Đề: trẻ 5 kg, mất 10% cân nặng.<br>2) Lượng nước mất = 5 × 10% = {G('500 ml')}.<br>"
        f"3) Nhu cầu duy trì = 100 × 5 = {G('500 ml')}.",
        "Ví dụ đẳng trương dùng cùng phép tính mất nước (5 kg × 10%) và Holliday–Segar cho 5 kg (100 ml/kg). Hai số 500 ml này "
        "là nền cho các bước tính Na⁺ ở thẻ tiếp theo.",
        "B11.01, B11.02", ["VD1-dang-truong"],
    ),
    algo(
        "PED50-ALGO-02", "B11", "VD1 — Từng bước tính dịch đẳng trương",
        "VD1 (trẻ 5 kg, mất 10%, đẳng trương): tính dịch 1000 ml từng bước như thế nào?",
        f"1) Nước mất = 5 kg × 10% = {G('500 ml')}; nhu cầu duy trì = 100 × 5 = {G('500 ml')}.<br>"
        f"2) Nhu cầu duy trì Na = 3 × 5 = {G('15 mEq')}.<br>"
        f"3) Lượng Na mất = 154 × 0,5 (l) = {G('77 mEq')}.<br>"
        f"4) Trong 1000 ml dịch: {G('92 mEq Na')} (= 600 ml NaCl 9‰), còn lại là {G('Glucose 5%')}.",
        "Vì mất đẳng trương, Na⁺ mất cùng tỷ lệ với nước nên bù Na⁺ đúng bằng lượng đã mất. Con số 92 mEq trong 1000 ml là "
        "tổng Na⁺ cần thiết trong dịch truyền theo barem. Phần còn lại của 1000 ml là Glucose 5%.",
        "B11.02, B11.03, B11.04", ["VD1-dang-truong", "Tinh-dich"],
    ),

    # ------------------------------------------------------------ B12. VD2 — mất nước nhược trương
    basic(
        "PED50-B12-01", "B12", "VD2 — Mất nước nhược trương", 1,
        f"{B('[VD2 — đề bài nhược trương]')} Trẻ {Y('5 kg')} mất {Y('10%')} cân nặng, {R('Na máu 125 mEq/l')}. Tính lượng nước mất, nhu cầu nước duy trì và nhu cầu Na duy trì.",
        f"1) Đề: trẻ 5 kg, mất 10%, Na máu 125 mEq/l.<br>2) Nước mất = 5 × 10% = {G('0,5 l = 500 ml')}; "
        f"nhu cầu duy trì = 100 × 5 = {G('500 ml')}; nhu cầu duy trì Na = 3 × 5 = {G('15 mEq')}.",
        "Khác với VD1, Na máu đã thấp nên cần bù thêm phần Na⁺ bị thiếu so với 135 mEq/l. Chỉ số 135 là giá trị Na⁺ huyết tương bình "
        "thường được dùng làm mốc trong công thức.",
        "B12.01, B12.02", ["VD2-nhuoc-truong"],
    ),
    algo(
        "PED50-ALGO-03", "B12", "VD2 — Từng bước tính Na⁺ mất nhược trương",
        "VD2 (trẻ 5 kg, mất 10%, Na máu 125): tính Na⁺ cho 1000 ml từng bước như thế nào?",
        f"1) Na mất = {G('Na cần điều chỉnh')} + {G('Na mất theo đẳng trương')}.<br>"
        f"2) Na cần điều chỉnh = (Na mm − Na Bn) × 0,6 × Po = (135 − 125) × 0,6 × 5 = {G('30 mEq')}.<br>"
        f"3) Na mất theo đẳng trương = {G('77 mEq')} (như VD1).<br>"
        f"4) Na mất tổng = 30 + 77 = {G('107 mEq')}.<br>"
        f"5) Trong 1000 ml dịch cần: 107 + 15 = {G('122 mEq Na')}.",
        "Na cần điều chỉnh là lượng Na⁺ để đưa Na máu từ 125 lên 135. Cộng với phần mất theo đẳng trương (77) rồi cộng nhu cầu duy trì (15) "
        "được tổng 122 mEq trong 1000 ml. Cần đối chiếu công thức với barem gốc vì đây là phép tính nhiều bước.",
        "B12.03, B12.04, B12.05, B12.06", ["VD2-nhuoc-truong", "Tinh-dich"],
    ),

    # ------------------------------------------------------------ B13. VD3 — mất nước ưu trương
    basic(
        "PED50-B13-01", "B13", "VD3 — Mất nước ưu trương", 1,
        f"{B('[VD3 — đề bài ưu trương]')} Trẻ {Y('5 kg')} mất {Y('10%')} cân nặng, {R('Na máu 170 mEq/l')}. Tính lượng nước mất, nhu cầu nước duy trì và nhu cầu Na duy trì.",
        f"1) Đề: trẻ 5 kg, mất 10%, Na máu 170 mEq/l.<br>2) Nước mất = 5 × 10% = {G('500 ml')}; "
        f"nhu cầu duy trì = {G('500 ml')}; nhu cầu duy trì Na = {G('15 mEq')}.",
        "Đề VD3 cho Na máu cao (170), nên phần lớn lượng nước cần bù là nước không điện giải (không chứa Na⁺), còn một phần dịch "
        "có điện giải. Dòng 'Chú ý' cuối slide VD3 trong barem để trống nên không có nội dung thêm.",
        "B13.01, B13.02", ["VD3-uong-truong"],
    ),
    algo(
        "PED50-ALGO-04", "B13", "VD3 — Từng bước tính dịch ưu trương",
        "VD3 (trẻ 5 kg, mất 10%, Na máu 170): tính nước không điện giải và dịch có điện giải từng bước như thế nào?",
        f"1) Nước không điện giải = Na Bn / Na mm × [0,6P − 0,6 Po] = 170/145 × [(0,6 × 5) − (0,6 × 4,5)] = {G('0,35 l (350 ml)')}.<br>"
        f"2) Dịch có điện giải = 500 − 350 = {G('150 ml')}.<br>"
        f"3) Na mất = 154 × 0,15 = {G('23 mEq')}.<br>"
        f"4) Trong 1000 ml dịch cần: 15 + 23 = {G('38 mEq Na')}.",
        "Với Na máu cao, lượng nước không điện giải lớn; chỉ 150 ml là dịch có điện giải và 23 mEq Na⁺ được bù qua phần này. "
        "Tổng 38 mEq trong 1000 ml gồm nhu cầu duy trì Na (15) và Na⁺ mất (23).",
        "B13.03, B13.04, B13.05", ["VD3-uong-truong", "Tinh-dich"],
    ),

    # ------------------------------------------------------------ B14. Hạ natri — định nghĩa, nguyên nhân
    basic(
        "PED50-B14-01", "B14", "Hạ natri máu — định nghĩa, nguyên nhân", 1,
        f"{B('[Hạ natri máu]')} Định nghĩa hạ natri máu và điều trị chung là gì?",
        f"1) Định nghĩa: {Y('Na < 130 mEq/l')}.<br>2) Điều trị: {G('điều chỉnh Na cùng với bù dịch ngoại bào')}.",
        "Hạ natri máu là Na⁺ huyết tương dưới 130 mEq/l. Điều trị phải vừa điều chỉnh Na⁺ vừa bù thể tích ngoại bào, vì Na⁺ và thể "
        "tích gắn chặt với nhau.",
        "B14.01, B14.03", ["Ha-natri"], asks=["Định nghĩa", "Điều trị"],
    ),
    basic(
        "PED50-B14-02", "B14", "Hạ natri máu — định nghĩa, nguyên nhân", 2,
        f"{B('[Nguyên nhân hạ natri máu]')} Các nguyên nhân gây hạ natri máu là gì?",
        f"1) {R('Tiêu chảy')}.<br>2) {R('Rửa dạ dày')}.<br>3) {R('Truyền nhiều dịch không điện giải')}.<br>"
        f"4) {R('Suy thận')}.<br>5) {R('Suy tim')}.<br>6) {R('Tăng sản tuyến thượng thận bẩm sinh')}.<br>"
        f"7) {R('SIADH')}.<br>8) {R('Điều trị lợi tiểu')}.",
        "Nhóm đầu là mất natri qua đường tiêu hóa (tiêu chảy, rửa dạ dày). Nhóm giữa là ứ nước do bệnh thận, tim hoặc truyền "
        "dịch không điện giải. SIADH và tăng sản thượng thận bẩm sinh là các nguyên nhân nội tiết. Thuốc lợi tiểu cũng làm mất natri.",
        "B14.02", ["Ha-natri"],
    ),
    cloze(
        "PED50-B14-03", "B14", "Hạ natri máu — định nghĩa, nguyên nhân",
        f"Hạ natri máu khi Na {{{{c1::{Y('< 130 mEq/l')}}}}}.",
        "B14.01", ["Ha-natri"],
    ),

    # ------------------------------------------------------------ B15. Hạ natri — phân loại theo KLTH
    basic(
        "PED50-B15-01", "B15", "Hạ natri — phân loại theo khối lượng tuần hoàn", 1,
        f"{B('[KLTH giảm, natri niệu < 20]')} Hạ natri máu khi khối lượng tuần hoàn giảm và natri niệu < 20 mEq/l thường do những nguyên nhân nào (nhóm mất natri ngoài thận)?",
        f"{G('Tiêu chảy, bỏng, lợi tiểu kéo dài, xơ nang tụy')}.",
        "Khi thể tích tuần hoàn giảm và thận giữ natri (natri niệu thấp), nguyên nhân thường là mất natri ngoài thận: tiêu chảy, bỏng, "
        "xơ nang tụy, hoặc lợi tiểu kéo dài.",
        "B15.01", ["Phan-loai-Ha-natri"],
    ),
    basic(
        "PED50-B15-02", "B15", "Hạ natri — phân loại theo khối lượng tuần hoàn", 1,
        f"{B('[KLTH giảm, natri niệu > 20]')} Hạ natri máu khi khối lượng tuần hoàn giảm và natri niệu > 20 mEq/l thường do những nguyên nhân nào (nhóm thận thải natri)?",
        f"{G('Lợi tiểu mạnh, suy thượng thận')}.",
        "Khi thể tích giảm mà thận vẫn thải natri (natri niệu cao), nguyên nhân là thuốc lợi tiểu mạnh hoặc suy thượng thận (mất muối).",
        "B15.02", ["Phan-loai-Ha-natri"],
    ),
    basic(
        "PED50-B15-03", "B15", "Hạ natri — phân loại theo KLTH", 1,
        f"{B('[KLTH bình thường/tăng, natri niệu < 20]')} Hạ natri máu khi khối lượng tuần hoàn bình thường hoặc tăng và natri niệu < 20 mEq/l do những nguyên nhân nào?",
        f"{G('HCTH, xơ gan, suy tim')}.",
        "Khi thể tích bình thường hoặc tăng nhưng thận giữ natri, nguyên nhân là các bệnh gây phù (hội chứng thận hư, xơ gan, suy tim).",
        "B15.03", ["Phan-loai-Ha-natri"],
    ),
    basic(
        "PED50-B15-04", "B15", "Hạ natri — phân loại theo KLTH", 1,
        f"{B('[KLTH bình thường/tăng, natri niệu > 20]')} Hạ natri máu khi khối lượng tuần hoàn bình thường hoặc tăng và natri niệu > 20 mEq/l do nguyên nhân nào?",
        f"{G('SIADH')}.",
        "SIADH là hội chứng tiết ADH không thích hợp: thận giữ nước và thải natri, nên thể tích tăng hoặc bình thường và natri niệu cao.",
        "B15.04", ["Phan-loai-Ha-natri"],
    ),
    basic(
        "PED50-B15-05", "B15", "Hạ natri — phân loại theo KLTH", 1,
        f"{B('[Điều trị nhóm KLTH giảm]')} Điều trị hạ natri máu ở nhóm khối lượng tuần hoàn giảm gồm những gì?",
        f"1) {G('Điều trị rối loạn huyết động')}.<br>2) {G('Truyền dịch như mất nước nhược trương')}.<br>"
        f"3) {G('Điều trị nguyên nhân')}.",
        "Nhóm này thiếu thể tích nên cần hồi sức huyết động và bù dịch như mất nước nhược trương (xem B8), đồng thời điều trị nguyên nhân.",
        "B15.05", ["Dieu-tri-Ha-natri"],
    ),
    basic(
        "PED50-B15-06", "B15", "Hạ natri — phân loại theo KLTH", 1,
        f"{B('[Điều trị nhóm KLTH bình thường/tăng]')} Điều trị hạ natri máu ở nhóm khối lượng tuần hoàn bình thường hoặc tăng gồm những gì?",
        f"1) {G('Hạn chế nước')}.<br>2) {G('Điều trị theo nguyên nhân')}.",
        "Nhóm này thừa nước nên trọng tâm là hạn chế nước đưa vào và điều trị nguyên nhân nền (suy tim, xơ gan, hội chứng thận hư, SIADH).",
        "B15.06", ["Dieu-tri-Ha-natri"],
    ),
    algo(
        "PED50-ALGO-05", "B15", "Hạ natri theo khối lượng tuần hoàn và natri niệu",
        "Hạ natri máu (Na < 130): nhánh nào khi KLTH giảm, nhánh nào khi KLTH bình thường/tăng?",
        f"1) {Y('KLTH giảm')} + natri niệu {G('< 20')} → {R('tiêu chảy, bỏng, lợi tiểu kéo dài, xơ nang tụy')}; điều trị: "
        f"{G('huyết động + truyền dịch như mất nước nhược trương + điều trị nguyên nhân')}.<br>"
        f"2) {Y('KLTH giảm')} + natri niệu {G('> 20')} → {R('lợi tiểu mạnh, suy thượng thận')}; điều trị như nhánh 1.<br>"
        f"3) {Y('KLTH bình thường/tăng')} + natri niệu {G('< 20')} → {R('HCTH, xơ gan, suy tim')}; điều trị: "
        f"{G('hạn chế nước + điều trị nguyên nhân')}.<br>"
        f"4) {Y('KLTH bình thường/tăng')} + natri niệu {G('> 20')} → {R('SIADH')}; điều trị: {G('hạn chế nước + điều trị nguyên nhân')}.",
        "Hai trục quyết định là khối lượng tuần hoàn và natri niệu với mốc 20 mEq/l. Ở nhóm thể tích giảm mà natri niệu thấp thì mất "
        "natri ngoài thận; natri niệu cao là do thuốc hoặc nội tiết. Ở nhóm thể tích bình thường/tăng, SIADH là nguyên nhân duy nhất "
        "có natri niệu cao, đồng thời thể tích không thiếu nên điều trị là hạn chế nước.",
        "B15.01, B15.02, B15.03, B15.04, B15.05, B15.06", ["Luu-do", "Ha-natri"],
    ),

    # ------------------------------------------------------------ B16. Hạ natri — có shock / triệu chứng thần kinh
    basic(
        "PED50-B16-01", "B16", "Hạ natri — có shock hoặc triệu chứng thần kinh", 1,
        f"{B('[Hạ natri có shock do mất nước]')} Hạ natri máu có shock do mất nước được xử trí như thế nào?",
        f"{G('Bolus NaCl 0,9% 20 ml/kg/lần')} → huyết động ổn định.",
        "Shock là ưu tiên hàng đầu: bolus NaCl 0,9% để khôi phục thể tích tuần hoàn trước, rồi đánh giá lại huyết động.",
        "B16.01", ["Ha-natri-shock"],
    ),
    basic(
        "PED50-B16-02", "B16", "Hạ natri — có shock hoặc triệu chứng thần kinh", 1,
        f"{B('[Hạ natri không shock, có triệu chứng thần kinh]')} Hạ natri máu không shock nhưng có triệu chứng thần kinh do Na < 120 mEq/l được xử trí như thế nào?",
        f"1) Truyền {G('NaCl 3% 6–10 ml/kg/h bằng BTĐ')}.<br>2) {Y('4 ml/kg')} ↑ Na lên {Y('3 mEq/l')}.<br>"
        f"3) Kiểm tra lại điện giải đồ (ĐGĐ).<br>4) Nếu cần, lặp lại liều 2.<br>5) Mục tiêu: {G('Na máu > 125 mEq/l')}.",
        "Triệu chứng thần kinh do Na < 120 là cấp cứu: dùng NaCl 3% tăng Na nhanh và có kiểm soát, đo lại ĐGĐ sau mỗi liều. "
        "Mục tiêu tạm thời là Na máu trên 125 để giảm nguy cơ phù não.",
        "B16.02", ["Ha-natri-than-kinh"],
    ),
    algo(
        "PED50-ALGO-06", "B16", "Hạ natri — xử trí theo shock và triệu chứng thần kinh",
        "Hạ natri máu có shock hoặc triệu chứng thần kinh: xử trí theo nhánh nào?",
        f"1) {R('Có shock do mất nước')} → {G('Bolus NaCl 0,9% 20 ml/kg/lần')} → huyết động ổn định.<br>"
        f"2) {Y('Không shock, có triệu chứng thần kinh do Na < 120')} → {G('NaCl 3% 6–10 ml/kg/h bằng BTĐ')} "
        f"({Y('4 ml/kg ↑ Na 3 mEq/l')}) → kiểm tra ĐGĐ → lặp liều 2 → {G('Na máu > 125 mEq/l')}.",
        "Nhánh shock luôn ưu tiên bù thể tích trước; nhánh thần kinh là hạ natri nặng cần tăng natri có kiểm soát bằng NaCl 3%. "
        "Hai nhánh đều đo lại ĐGĐ sau khi can thiệp.",
        "B16.01, B16.02", ["Luu-do", "Ha-natri-shock"],
    ),

    # ------------------------------------------------------------ B17. Hạ natri — không shock, không triệu chứng thần kinh
    basic(
        "PED50-B17-01", "B17", "Hạ natri — không shock, không triệu chứng thần kinh", 1,
        f"{B('[Công thức Na⁺ thiếu]')} Lượng Na⁺ thiếu (mEq) được tính theo công thức nào?",
        f"{G('Na⁺ thiếu = 0,6 × P × (135 − Na⁺bn)')}.",
        "Công thức này tính lượng Na⁺ cần bổ sung để đưa Na⁺ từ giá trị hiện tại về 135 mEq/l, dựa trên thể tích phân bố "
        "0,6 × cân nặng.",
        "B17.01", ["Na-thieu"],
    ),
    basic(
        "PED50-B17-02", "B17", "Hạ natri — không shock, không triệu chứng thần kinh", 1,
        f"{B('[Natri cho trong 24h]')} Lượng natri cho trong 24h được tính như thế nào?",
        f"{G('Natri cho trong 24h = Na thiếu + Na nhu cầu')}.",
        "Tổng Na⁺ cần trong ngày gồm phần thiếu (tính ở công thức trước) cộng với nhu cầu duy trì Na⁺ hằng ngày.",
        "B17.02", ["Natri-24h"],
    ),
    basic(
        "PED50-B17-03", "B17", "Hạ natri — không shock, không triệu chứng thần kinh", 2,
        f"{B('[Cách truyền natri]')} Lượng natri 24h được truyền theo phân bổ thời gian nào?",
        f"1) {G('1/2 lượng')} truyền trong {Y('8 giờ đầu')}.<br>2) {G('1/2 lượng còn lại')} truyền trong {Y('16 giờ kế tiếp')}.",
        "Truyền không đều: nửa đầu nhanh trong 8 giờ để nâng natri, nửa sau chậm hơn trong 16 giờ để tránh tăng natri quá nhanh.",
        "B17.03", ["Cach-truyen-natri"],
    ),
    cloze(
        "PED50-B17-04", "B17", "Hạ natri — không shock, không triệu chứng thần kinh",
        f"Nửa lượng natri 24h truyền trong {{{{c1::{Y('8 giờ đầu')}}}}}.",
        "B17.03", ["Cach-truyen-natri"],
    ),

    # ------------------------------------------------------------ B18. Hạ natri do SIADH
    basic(
        "PED50-B18-01", "B18", "Hạ natri do SIADH", 1,
        f"{B('[SIADH — xử trí]')} Xử trí hạ natri do SIADH gồm những gì (bù Na, hạn chế dịch, Na theo nhu cầu, furosemid)?",
        f"1) {G('Không cần bù Na trừ khi có biểu hiện thần kinh')}.<br>2) {G('Hạn chế dịch: cho 50% nhu cầu')}.<br>"
        f"3) {G('Cho Na theo nhu cầu: 3 mEq/100 ml dịch truyền')}.<br>4) {G('Furosemid: 0,5 mg/kg/TM')}.",
        "SIADH thừa nước nên chủ yếu hạn chế dịch đến 50% nhu cầu. Chỉ bù Na⁺ khi có triệu chứng thần kinh; furosemid giúp thải nước.",
        "B18.01, B18.02, B18.03, B18.04", ["SIADH"],
    ),
    cloze(
        "PED50-B18-02", "B18", "Hạ natri do SIADH",
        f"SIADH: hạn chế dịch cho {{{{c1::{Y('50% nhu cầu')}}}}}.",
        "B18.02", ["SIADH"],
    ),

    # ------------------------------------------------------------ B19. Tăng natri máu
    basic(
        "PED50-B19-01", "B19", "Tăng natri máu", 1,
        f"{B('[Tăng natri máu]')} Định nghĩa tăng natri máu là gì?",
        f"1) Định nghĩa: {Y('Na > 150 mEq/l')}.",
        "Tăng natri cần hạ từ từ: giảm quá nhanh có thể gây phù não. Mức giảm tối đa barem ghi là 12–15 mEq/l trong 24 giờ; "
        "đây là ý dùng để xử trí ở B19.02–B19.05, không thuộc nội dung thẻ định nghĩa này.",
        "B19.01, B19.02", ["Tang-natri"], asks=["Định nghĩa"],
    ),
    basic(
        "PED50-B19-02", "B19", "Tăng natri máu", 1,
        f"{B('[Tăng natri máu có shock do mất nước]')} Tăng natri máu có shock do mất nước được xử trí như thế nào?",
        f"1) {G('NaCl 0,9% hoặc Ringer lactat 20 ml/kg/lần')} → huyết động ổn định.<br>"
        f"2) Sau đó truyền {G('G5% in NaCl 0,45%')}.<br>3) Nếu nước tiểu tốt có thể truyền {G('G5% in NaCl 0,2%')}.",
        "Trước tiên bù thể tích bằng NaCl 0,9% hoặc Ringer lactat để ổn định shock, sau đó chuyển sang dịch hạ tonicity dần (G5% in NaCl 0,45%) "
        "để hạ natri từ từ.",
        "B19.03", ["Tang-natri-shock"],
    ),
    basic(
        "PED50-B19-03", "B19", "Tăng natri máu", 1,
        f"{B('[Tăng natri máu không shock]')} Tăng natri máu không shock được xử trí bằng dịch gì?",
        f"{G('G5% in NaCl 0,2%')}.",
        "Không có shock nên dùng ngay dịch hạ natri nhẹ (G5% in NaCl 0,2%) để hạ Na từ từ theo giới hạn 12–15 mEq/l/24h.",
        "B19.04", ["Tang-natri"],
    ),
    basic(
        "PED50-B19-04", "B19", "Tăng natri máu", 2,
        f"{B('[Furosemid trong tăng natri máu]')} Khi thể tích ngoại bào bình thường, có thể dùng furosemid liều bao nhiêu?",
        f"{G('Furosemid 0,5 mg/kg/lần')}.",
        "Furosemid thải nước khi thể tích ngoại bào bình thường (không mất nước), giúp hạ Na⁺ mà không gây thiếu thể tích.",
        "B19.05", ["Tang-natri"],
    ),
    algo(
        "PED50-ALGO-07", "B19", "Tăng natri máu — chọn dịch theo shock",
        "Tăng natri máu (Na > 150): chọn dịch theo có shock hay không như thế nào?",
        f"1) {R('Có shock mất nước')} → {G('NaCl 0,9% hoặc Ringer lactat 20 ml/kg/lần')} → ổn định → {G('G5% in NaCl 0,45%')}; "
        f"nước tiểu tốt → {G('G5% in NaCl 0,2%')}.<br>"
        f"2) {Y('Không shock')} → {G('G5% in NaCl 0,2%')}.<br>"
        f"3) {Y('Không shock')}, nếu {Y('thể tích dịch ngoại bào bình thường')} → có thể cho {G('Furosemid 0,5 mg/kg/lần')}.<br>"
        f"4) Giới hạn: hạ Na {R('không quá 12–15 mEq/l/24h')}.",
        "Shock thì bù thể tích trước bằng dịch đẳng trương, sau đó hạ natri dần. Không shock thì dùng ngay dịch hạ natri nhẹ. "
        "Furosemid chỉ thêm khi thể tích bình thường. Luôn tôn trọng giới hạn hạ Na 12–15 mEq/l trong 24 giờ.",
        "B19.01, B19.02, B19.03, B19.04, B19.05", ["Luu-do", "Tang-natri"],
    ),

    # ------------------------------------------------------------ B20. Hạ kali — định nghĩa, nguyên nhân, điều trị nhẹ
    basic(
        "PED50-B20-01", "B20", "Hạ kali máu — định nghĩa, nguyên nhân", 1,
        f"{B('[Hạ kali máu]')} Định nghĩa hạ kali máu và các nguyên nhân chính là gì?",
        f"1) Định nghĩa: {Y('K⁺ < 3,5 mEq/l')}.<br>2) Nguyên nhân: {R('bệnh lý ống thận')}; {R('nôn nhiều, tiêu chảy, dùng lợi tiểu kéo dài')}; "
        f"{R('nhiễm toan, đái đường')}.",
        "K⁺ thấp do mất qua đường tiêu hóa (nôn, tiêu chảy), mất qua thận (lợi tiểu, bệnh ống thận, đái đường) hoặc chuyển K⁺ vào "
        "tế bào trong nhiễm toan.",
        "B20.01, B20.02", ["Ha-kali"], asks=["Định nghĩa", "Nguyên nhân"],
    ),
    basic(
        "PED50-B20-02", "B20", "Hạ kali máu — định nghĩa, nguyên nhân", 1,
        f"{B('[Hạ kali 2,5–3,5 — điều trị uống]')} Hạ kali khi K⁺ từ 2,5 đến 3,5 mEq/l được điều trị bằng gì?",
        f"{G('Uống K 3–5 mEq/kg/24h trong 3–5 ngày')}.",
        "Khi K⁺ chỉ thấp vừa, điều trị bằng đường uống đủ hiệu quả và an toàn. Liều tính theo cân nặng ngày, kéo dài 3–5 ngày.",
        "B20.03", ["Ha-kali-uong"],
    ),
    cloze(
        "PED50-B20-03", "B20", "Hạ kali máu — định nghĩa, nguyên nhân",
        f"Hạ kali máu khi K⁺ {{{{c1::{Y('< 3,5 mEq/l')}}}}}.",
        "B20.01", ["Ha-kali"],
    ),

    # ------------------------------------------------------------ B21. Hạ kali — K⁺ < 2,5
    basic(
        "PED50-B21-01", "B21", "Hạ kali máu — K⁺ < 2,5", 1,
        f"{B('[K⁺ < 2,5 không triệu chứng tim mạch]')} Nếu K⁺ < 2,5 mmol/l không có triệu chứng tim mạch, truyền KCl như thế nào?",
        f"KCl 10% liều {G('0,3 mEq/kg/h × 4h')}, pha với Dd {G('Glucose 5% tỉ lệ 1:3')}, truyền trong {Y('4 giờ')}.",
        "Đây là truyền KCl có kiểm soát trong 4 giờ, liều 0,3 mEq/kg/h. Pha loãng và truyền chậm để tránh tăng kali máu đột ngột "
        "và tổn thương tĩnh mạch.",
        "B21.01", ["Ha-kali-nang"],
    ),
    basic(
        "PED50-B21-02", "B21", "Hạ kali máu — K⁺ < 2,5", 1,
        f"{B('[K⁺ < 2,5 có triệu chứng tim mạch]')} Nếu K⁺ < 2,5 mmol/l có triệu chứng tim mạch, truyền KCl như thế nào?",
        f"KCl 10% liều {G('0,3–0,5 mEq/kg/h × 4h')}, pha với Dd {G('Glucose 5% tỉ lệ 1:3')}, truyền trong {Y('4 giờ')}.",
        "Khi có triệu chứng tim mạch, liều cao hơn một chút (0,3–0,5 mEq/kg/h) để nhanh chóng ổn định nhịp tim, vẫn truyền trong 4 giờ "
        "và pha loãng như nhánh trước.",
        "B21.02", ["Ha-kali-nang"],
    ),
    basic(
        "PED50-B21-03", "B21", "Hạ kali máu — K⁺ < 2,5", 2,
        f"{B('[Công thức KCl 10%]')} Số ml KCl 10% cần dùng được tính theo công thức nào?",
        f"{G('X ml KCl 10% = (4,5 − K Bn) × P/10')}.",
        "Công thức tính ml KCl 10% cần thiết để đưa K⁺ từ giá trị hiện tại lên mốc 4,5 mEq/l, theo cân nặng. "
        "Barem ghi hệ số 4,5 làm mốc đích; đây là công thức theo barem gốc.",
        "B21.03", ["Cong-thuc-KCl"],
    ),
    basic(
        "PED50-B21-04", "B21", "Hạ kali máu — K⁺ < 2,5", 2,
        f"{B('[Pha loãng KCl 10%]')} Cách pha loãng KCl 10% để truyền tĩnh mạch trong 4 giờ?",
        f"Pha {G('1 ml KCl 10% với 9 ml G5%')}, truyền tĩnh mạch trong {Y('4 giờ')} bằng {G('bơm tiêm điện')}.",
        "Pha loãng 10 lần để giảm nồng độ KCl trong dịch truyền; dùng bơm tiêm điện để kiểm soát tốc độ đúng 4 giờ.",
        "B21.04", ["Pha-KCl"],
    ),
    algo(
        "PED50-ALGO-08", "B21", "Hạ kali máu — truyền KCl theo mức K⁺ và triệu chứng tim mạch",
        "Hạ kali máu (K⁺ < 2,5): truyền KCl như thế nào theo có hay không triệu chứng tim mạch?",
        f"1) {Y('K⁺ < 2,5 không triệu chứng tim mạch')} → KCl 10% {G('0,3 mEq/kg/h × 4h')}.<br>"
        f"2) {R('K⁺ < 2,5 có triệu chứng tim mạch')} → KCl 10% {G('0,3–0,5 mEq/kg/h × 4h')}.<br>"
        f"3) Cả hai: pha với {G('Dd Glucose 5% tỉ lệ 1:3')}, truyền trong {Y('4 giờ')}.<br>"
        f"4) Lượng KCl 10% (ml) = {G('(4,5 − K Bn) × P/10')}.<br>"
        f"5) Pha loãng {G('1 ml KCl 10% với 9 ml G5%')}, truyền tĩnh mạch trong {Y('4h')} bằng {G('bơm tiêm điện')}.",
        "Triệu chứng tim mạch quyết định liều trên (0,3 hay 0,3–0,5 mEq/kg/h). Barem ghi hai cách pha ở hai slide khác nhau "
        "(pha G5% tỉ lệ 1:3 và pha 1 ml KCl 10% với 9 ml G5%) — nhớ đúng từng câu, không gộp làm một. Mọi trường hợp đều "
        "truyền trong 4 giờ để tránh tăng kali nhanh.",
        "B21.01, B21.02, B21.03, B21.04", ["Luu-do", "Ha-kali-nang"],
    ),

    # ------------------------------------------------------------ B22. Tăng kali máu
    basic(
        "PED50-B22-01", "B22", "Tăng kali máu", 1,
        f"{B('[Tăng kali máu — định nghĩa, nguyên nhân]')} Định nghĩa tăng kali máu và các nguyên nhân chính là gì?",
        f"1) Định nghĩa: {Y('K⁺ > 5,5 mEq/l')}.<br>2) Nguyên nhân: {R('suy thận')}, {R('suy thượng thận')}, {R('toan máu')}.",
        "K⁺ tăng khi thận không thải được (suy thận, suy thượng thận do mất aldosteron) hoặc K⁺ chuyển từ trong tế bào ra ngoài "
        "trong toan máu.",
        "B22.01, B22.02", ["Tang-kali"], asks=["Định nghĩa", "Nguyên nhân"],
    ),
    basic(
        "PED50-B22-02", "B22", "Tăng kali máu", 1,
        f"{B('[Tăng kali máu — điều trị]')} Điều trị tăng kali máu gồm những bước nào?",
        f"1) {G('Ngừng nguồn cung cấp K⁺')}.<br>2) {G('Tiêm chậm CaCl₂ 25 mg/kg')}.<br>"
        f"3) {G('Truyền Glucose và Insulin (0,5 g/kg và 0,1 UI/kg)')}.<br>4) {G('Thải K⁺ bằng Kayexalat')}.<br>"
        f"5) {G('Lọc màng bụng')}.<br>6) {G('Điều trị nguyên nhân')}.",
        "Trình tự ưu tiên: ngừng nguồn K⁺ và bảo vệ tim (CaCl₂ tiêm chậm), sau đó đưa K⁺ vào tế bào (Glucose + Insulin), rồi thải K⁺ "
        "ra ngoài (Kayexalat, lọc màng bụng), cuối cùng điều trị nguyên nhân nền.",
        "B22.03", ["Dieu-tri-tang-kali"],
    ),
    algo(
        "PED50-ALGO-09", "B22", "Tăng kali máu — trình tự xử trí",
        "Tăng kali máu (K⁺ > 5,5): trình tự xử trí cấp cứu theo thứ tự nào?",
        f"1) {R('Ngừng nguồn cung cấp K⁺')}.<br>"
        f"2) {G('Tiêm chậm CaCl₂ 25 mg/kg')}.<br>"
        f"3) {G('Truyền Glucose và Insulin')} ({Y('0,5 g/kg')} và {Y('0,1 UI/kg')}).<br>"
        f"4) {G('Thải K⁺ bằng Kayexalat')}.<br>"
        f"5) {G('Lọc màng bụng')}.<br>"
        f"6) {G('Điều trị nguyên nhân')} ({R('suy thận, suy thượng thận, toan máu')}).",
        "Đúng thứ tự barem. Logic: CaCl₂ ổn định màng tế bào cơ tim trước; Glucose + Insulin kéo K⁺ vào trong tế bào; "
        "Kayexalat và lọc màng bụng mới thực sự thải K⁺ ra khỏi cơ thể; cuối cùng xử lý nguyên nhân nền để K⁺ không tăng lại.",
        "B22.01, B22.02, B22.03", ["Luu-do", "Tang-kali"],
    ),
    cloze(
        "PED50-B22-03", "B22", "Tăng kali máu",
        f"Tăng kali máu khi K⁺ {{{{c1::{Y('> 5,5 mEq/l')}}}}}.",
        "B22.01", ["Tang-kali"],
    ),

    # ------------------------------------------------------------ B23. Hạ canxi máu
    basic(
        "PED50-B23-01", "B23", "Hạ canxi máu", 1,
        f"{B('[Hạ canxi máu — định nghĩa]')} Định nghĩa hạ canxi máu theo canxi toàn phần và theo Ca⁺⁺ ion hóa là gì?",
        f"1) Canxi toàn phần {Y('< 2,5 mEq/l')}.<br>2) Ca⁺⁺ {Y('< 1,1 mEq/l')}.",
        "Có hai cách đo: canxi toàn phần (tổng cả phần gắn protein) và Ca⁺⁺ ion hóa (phần có hoạt tính sinh học). Barem ghi cả hai ngưỡng.",
        "B23.01", ["Ha-canxi"],
    ),
    basic(
        "PED50-B23-02", "B23", "Hạ canxi máu", 2,
        f"{B('[Hạ canxi máu — nguyên nhân]')} Các nguyên nhân gây hạ canxi máu là gì?",
        f"1) {R('Thiếu vitamin D')}.<br>2) {R('Hội chứng ruột ngắn')}.<br>3) {R('Suy cận giáp')}.<br>4) {R('Kiềm hô hấp')}.",
        "Thiếu vitamin D và hội chứng ruột ngắn làm giảm hấp thu canxi; suy cận giáp làm giảm PTH; kiềm hô hấp làm canxi gắn chặt "
        "hơn với albumin nên Ca⁺⁺ ion hóa giảm.",
        "B23.02", ["Ha-canxi"],
    ),
    basic(
        "PED50-B23-03", "B23", "Hạ canxi máu", 1,
        f"{B('[Hạ canxi máu — lâm sàng]')} Biểu hiện lâm sàng của hạ canxi máu là gì?",
        f"1) {R('Co giật')}.<br>2) {R('Tetanie')}.",
        "Canxi ion hóa cần cho dẫn truyền thần kinh cơ; khi thiếu, thần kinh cơ hưng phấn quá mức gây co giật và tetanie.",
        "B23.03", ["Ha-canxi"],
    ),
    basic(
        "PED50-B23-04", "B23", "Hạ canxi máu", 1,
        f"{B('[Hạ canxi máu — điều trị]')} Điều trị hạ canxi máu gồm những gì?",
        f"1) {G('An thần')}.<br>2) {G('Thở lại')} (rebreathing).<br>3) {G('Canxi gluconate 10% 0,5–1 ml/kg/TMC')}.<br>"
        f"4) {G('Canxi clorua 10% 0,2–0,3 ml/kg/TMC')}.",
        "\"Thở lại\" là cho trẻ hít lại khí thở ra (rebreathing) để tăng CO₂ — dùng khi hạ canxi ion hóa do kiềm hô hấp (một "
        "nguyên nhân trong barem), vì kiềm làm canxi ion hóa gắn nhiều hơn vào albumin. Sau đó tiêm tĩnh mạch chậm canxi; "
        "canxi clorua có liều ml/kg thấp hơn canxi gluconate.",
        "B23.04", ["Dieu-tri-ha-canxi"],
    ),
    cloze(
        "PED50-B23-05", "B23", "Hạ canxi máu",
        f"Hạ canxi máu khi Ca⁺⁺ {{{{c1::{Y('< 1,1 mEq/l')}}}}}.",
        "B23.01", ["Ha-canxi"],
    ),
    algo(
        "PED50-ALGO-10", "B23", "Hạ canxi máu — chọn canxi và liều",
        "Hạ canxi máu có co giật hoặc tetanie: xử trí theo trình tự và chọn muối canxi nào?",
        f"1) {R('Co giật / tetanie')} → {G('an thần')}, {G('thở lại')} (rebreathing).<br>"
        f"2) Tiêm TMC chậm: {G('Canxi gluconate 10% 0,5–1 ml/kg')}.<br>"
        f"3) Hoặc: {G('Canxi clorua 10% 0,2–0,3 ml/kg')}.<br>"
        f"4) Ngưỡng xác định: canxi toàn phần {Y('< 2,5')} hoặc Ca⁺⁺ {Y('< 1,1 mEq/l')}.",
        "Co giật là cấp cứu: an thần, thở lại (khi do kiềm hô hấp), rồi bù canxi tĩnh mạch chậm. Hai muối canxi có liều khác "
        "nhau theo cân nặng và barem đều ghi đủ.",
        "B23.01, B23.02, B23.03, B23.04", ["Luu-do", "Ha-canxi"],
    ),

    # ------------------------------------------------------------ B24. Tăng canxi máu
    basic(
        "PED50-B24-01", "B24", "Tăng canxi máu", 1,
        f"{B('[Tăng canxi máu — nguyên nhân]')} Nguyên nhân gây tăng canxi máu là gì?",
        f"1) {R('Đáp ứng mạnh với Vitamin D')}.<br>2) {R('Rối loạn chuyển hóa canxi')}.",
        "Tăng canxi thường do thừa vitamin D (tăng hấp thu canxi ở ruột) hoặc các rối loạn chuyển hóa làm tăng canxi máu.",
        "B24.01", ["Tang-canxi"],
    ),
    basic(
        "PED50-B24-02", "B24", "Tăng canxi máu", 1,
        f"{B('[Tăng canxi máu — triệu chứng]')} Triệu chứng của tăng canxi máu là gì?",
        f"1) {R('Nhược cơ')}.<br>2) {R('Nôn')}.<br>3) {R('Táo bón')}.<br>4) {R('Đái dầm')}.",
        "Các triệu chứng này đều liên quan đến canxi cao làm giảm dẫn truyền thần kinh cơ và co trơn đường tiêu hóa, bàng quang.",
        "B24.02", ["Tang-canxi"],
    ),
    basic(
        "PED50-B24-03", "B24", "Tăng canxi máu", 1,
        f"{B('[Tăng canxi máu — điều trị]')} Điều trị tăng canxi máu gồm những gì?",
        f"1) {G('Ngừng cung cấp canxi')}.<br>2) {G('Ngừng vitamin D')}.<br>3) {G('Corticoid 1 mg/kg/24h')}.",
        "Ngừng nguồn canxi và vitamin D là bước đầu; corticoid giúp giảm hấp thu canxi ở ruột và tăng đào thải canxi qua thận.",
        "B24.03", ["Dieu-tri-tang-canxi"],
    ),
    cloze(
        "PED50-B24-04", "B24", "Tăng canxi máu",
        f"Corticoid điều trị tăng canxi máu liều {{{{c1::{Y('1 mg/kg/24h')}}}}}.",
        "B24.03", ["Dieu-tri-tang-canxi"],
    ),
]
