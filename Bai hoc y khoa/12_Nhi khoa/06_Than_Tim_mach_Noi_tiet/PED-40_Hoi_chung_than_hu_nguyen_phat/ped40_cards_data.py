# -*- coding: utf-8 -*-
# PED-40 Hội chứng thận hư nguyên phát ở trẻ em — nguồn thẻ duy nhất (track ebm).
# Rebuild 2026-10-27: chuẩn hóa Basic-first, màu, nguồn ở Extra, ⚡; sửa các điểm lệch IPNA 2023/2020
# (albumin < 30 g/L, FRNS ≥ 3/12 tháng, CR ≤ 0,2 mg/mg, đích CsA/Tac, không giảm liều dần, albumin 4–5% khi sốc,
# không dự phòng chống đông/canxi–vitamin D thường quy, muối, đạm). `legacy_note_id` giữ lịch sử ôn của 98 note cũ.


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / bệnh lý
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / tuổi
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc
    return _c("#51cf66", t)


def B(t):  # thực thể / phân loại
    return _c("#74c0fc", t)


IPNA23 = "IPNA 2023 — HCTH nhạy cảm steroid (Trautmann và cs., Pediatr Nephrol 2023; PMID 36269406)"
IPNA20 = "IPNA 2020 — HCTH kháng steroid (Trautmann và cs., Pediatr Nephrol 2020; PMID 32382828)"
KDIGO = "KDIGO 2021 bệnh cầu thận (PMID 34556256)"
COCH = "Cochrane 2020, Hahn và cs. (PMID 35659203)"
KERLIN = "Kerlin và cs. 2009, MWPNC (PMID 19394032)"
BYT = "Bộ Y tế, QĐ 3312/QĐ-BYT — Hội chứng thận hư tiên phát ở trẻ em"
BAI = "Bài PED-40 RELEASE v1 (nội dung bài, chưa đối chiếu nguồn gốc)"
LEGACY_BASE = 1789990725646  # note Anki cũ: id = LEGACY_BASE + 2 × (số thứ tự thẻ cũ − 1)


def _src(*parts):
    return "📖 Nguồn: " + "; ".join(parts) + "."


def basic(n, section, category, tier, front, core, ai, src, tags, asks=None):
    card = {
        "id": f"PED40-{n:03d}" if isinstance(n, int) else f"PED40-{n}",
        "track": "ebm", "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": _src(*src), "tags": ["PED-40", "EBM"] + tags,
    }
    if isinstance(n, int):
        card["legacy_note_id"] = LEGACY_BASE + 2 * (n - 1)
    if asks:
        card["asks"] = asks
    return card


def algo(code, section, category, title, core, ai, src, tags):
    return basic(code, section, category, 1, "⚡ THUẬT TOÁN QUYẾT ĐỊNH — " + B(title), core, ai, src,
                 tags + ["Thuat-toan"])


def cloze(n, section, category, text, src, tags):
    return {
        "id": f"PED40-{n:03d}", "track": "ebm", "type": "cloze", "section": section, "category": category,
        "tier": 2, "text": text, "extra": _src(*src), "tags": ["PED-40", "EBM", "Cloze-phu"] + tags,
        "legacy_note_id": LEGACY_BASE + 2 * (n - 1),
    }


def cz(t, k=1):
    return "{{c%d::%s}}" % (k, t)


cards_data = [
    # ================================================================ E0. Cảnh báo an toàn & cấp cứu tại giường
    basic(1, "E0", "Cảnh báo an toàn", 1,
          f"{B('[HCTH — giảm thể tích tuần hoàn]')} Vì sao {R('cấm dùng Furosemid đơn độc')} khi trẻ HCTH đang giảm thể tích tuần hoàn (Underfill)?",
          f"Furosemid làm {R('sụt thêm thể tích nội mạch')}, đẩy trẻ vào {R('sốc giảm thể tích, huyết khối và tổn thương thận cấp (hoại tử ống thận)')}.",
          "Trẻ phù to nhưng lòng mạch đang thiếu dịch; thiểu niệu là phản xạ giữ dịch của thận. IPNA 2023 khuyến cáo khi có dấu hiệu "
          "giảm thể tích: tạm ngừng lợi tiểu và ngừng thuốc ức chế men chuyển/chẹn thụ thể angiotensin, bù thể tích bằng albumin trước.",
          [IPNA23], ["Canh-bao", "Furosemid"]),
    basic(2, "E0", "Cảnh báo an toàn", 1,
          f"{B('[Viêm phúc mạc tiên phát trong HCTH]')} Căn nguyên vi khuẩn {R('hàng đầu')} là gì?",
          f"{R('Phế cầu khuẩn (Streptococcus pneumoniae)')}, chiếm {Y('trên 50%')} các trường hợp.",
          "Trẻ mất IgG và yếu tố bổ thể qua nước tiểu nên giảm opson hóa vi khuẩn có vỏ. Kháng sinh đầu tay trong bài: "
          "Ceftriaxone 80–100 mg/kg/ngày tĩnh mạch, sau khi cấy máu và dịch màng bụng.",
          [BAI], ["Canh-bao", "Nhiem-trung"]),
    basic(3, "E0", "Cảnh báo an toàn", 1,
          f"{B('[Tăng đông trong HCTH]')} Cơ chế nào khiến trẻ HCTH dễ {R('huyết khối tắc mạch')}, và nhóm nguy cơ cao gồm những trẻ nào?",
          f"1) Cơ chế: {R('mất antithrombin III qua nước tiểu')}, gan {R('tăng tổng hợp fibrinogen')}, {R('máu cô đặc')} do thoát dịch ra mô kẽ.<br>"
          f"2) Nhóm nguy cơ cao: trẻ {Y('≥ 12 tuổi')}, albumin máu {Y('< 20 g/L')}, có {R('catheter tĩnh mạch trung tâm')}.",
          "Ba yếu tố của tam chứng Virchow cùng xuất hiện: tăng đông, ứ trệ do cô đặc máu, tổn thương mạch khi đặt catheter. "
          "Nghiên cứu MWPNC (326 trẻ) ghi nhận tuổi ≥ 12 lúc khởi phát là yếu tố tiên đoán độc lập, và 45% huyết khối tĩnh mạch sâu liên quan catheter.",
          [KERLIN, BAI], ["Canh-bao", "Huyet-khoi"], asks=["Cơ chế", "Nhóm nguy cơ cao"]),
    basic(4, "E0", "Cảnh báo an toàn", 1,
          f"{B('[Corticoid liều cao]')} Ngừng {R('đột ngột')} Prednisolone đang dùng liều cao kéo dài có nguy cơ gì, và nguy cơ cao nhất khi nào?",
          f"1) Nguy cơ: {R('suy thượng thận trung ương thoáng qua')} do trục hạ đồi – tuyến yên – thượng thận bị ức chế.<br>"
          f"2) Nguy cơ cao nhất khi trẻ gặp {R('stress')}: sốt, phẫu thuật gây mê, chấn thương.",
          "Phác đồ chuẩn xử lý nguy cơ này bằng cách chuyển sang liều cách ngày. IPNA 2023 không khuyến cáo giảm liều dần trong "
          "giai đoạn cách ngày: trong 775 trẻ của 4 RCT chất lượng cao chỉ có 1 ca nghi suy thượng thận.",
          [IPNA23], ["Canh-bao", "Corticoid"], asks=["Nguy cơ", "Nguy cơ cao nhất"]),
    basic(5, "E0", "Cấp cứu tại giường", 2,
          f"{B('[HCTH — tưới máu ngoại vi]')} Dấu hiệu nào cảnh báo {R('sốc giảm thể tích')} ở trẻ HCTH?",
          f"{R('Mạch nhanh nhỏ')}, {R('CRT > 3 giây')}, {R('đầu chi lạnh')}, {R('da nổi vân tím')}; thường kèm {R('huyết áp kẹp')} (hiệu áp {Y('< 20 mmHg')}) hoặc tụt huyết áp.",
          "Đừng nhìn độ phù để đánh giá dịch trong lòng mạch: bắt mạch quay, bấm CRT và sờ nhiệt độ đầu chi. Chân lạnh, CRT kéo dài "
          "là đang thiếu dịch nội mạch dù bụng báng căng.",
          [BAI], ["Cap-cuu", "Soc"]),
    basic(6, "E0", "Cấp cứu tại giường", 2,
          f"{B('[HCTH phù to]')} Trẻ kêu {R('đau bụng dữ dội quanh rốn')} kèm {R('CRT kéo dài')} gợi ý biến chứng gì?",
          f"{R('Thiếu máu cục bộ mạc treo ruột')} do {R('giảm thể tích tuần hoàn nội mạch nặng')}.",
          "IPNA 2023 xếp khó chịu vùng bụng vào nhóm dấu hiệu giảm thể tích (cùng thiểu niệu, tổn thương thận cấp, CRT kéo dài, "
          "mạch nhanh). Đây là báo động sốc mất bù cận kề; nhưng nếu kèm sốt phải loại trừ ngay viêm phúc mạc tiên phát.",
          [IPNA23], ["Cap-cuu", "Dau-bung"]),
    basic(7, "E0", "Cấp cứu tại giường", 2,
          f"{B('[HCTH sốc giảm thể tích / tụt huyết áp]')} Dùng dịch gì để chống sốc, có kèm Furosemid không, và nếu chưa có thì thay bằng gì?",
          f"1) Thở oxy, lập đường truyền; truyền {G('Albumin 4–5%')} theo IPNA 2023.<br>"
          f"2) {R('KHÔNG kèm Furosemid')} khi đang sốc/tụt huyết áp.<br>"
          f"3) Chưa có albumin: {G('NaCl 0,9% hoặc Ringer lactat')} {Y('10–20 mL/kg')} truyền nhanh trong {Y('30–60 phút')}.",
          "Albumin 20–25% (ưu trương) kèm Furosemid dành cho trẻ giảm thể tích chưa tụt huyết áp. Khi đã tụt huyết áp, ưu tiên là "
          "nâng thể tích nội mạch bằng dung dịch đẳng trương; lợi tiểu lúc này làm sốc nặng thêm.",
          [IPNA23, BAI], ["Cap-cuu", "Soc", "Albumin"]),
    basic(8, "E0", "Tiếp cận tại giường", 2,
          f"{B('[Trẻ phù mi mắt]')} Que thử nước tiểu Protein {Y('âm tính hoặc 1+')}: kết luận và làm gì tiếp?",
          f"1) {Y('Chưa chẩn đoán HCTH')}.<br>2) Tìm nguyên nhân phù khác: {B('suy tim, suy dinh dưỡng, xơ gan, dị ứng/phù mạch')}.<br>"
          f"3) {G('Thử lại sau 24–48 giờ')}.",
          "Ngưỡng thận hư trên que thử là 3+ đến 4+. Protein niệu thấp mà phù thì phải nghĩ phù ngoài thận.",
          [IPNA23, BAI], ["Tiep-can"]),
    algo("A5", "E0", "3 KHÔNG & 3 NÊN tại giường",
         "3 KHÔNG & 3 NÊN khi tiếp nhận trẻ HCTH phù",
         f"1) {R('KHÔNG')} dùng Furosemid khi còn dấu hiệu giảm thể tích (mạch nhanh, CRT kéo dài, chi lạnh, đau bụng, tiểu ít).<br>"
         f"2) {R('KHÔNG')} tiêm canxi tĩnh mạch chỉ vì canxi toàn phần thấp — tính canxi hiệu chỉnh/đo canxi ion hóa.<br>"
         f"3) {R('KHÔNG')} tiêm vắc xin sống khi đang dùng corticoid liều cao.<br>"
         f"4) {G('NÊN')} đánh giá tưới máu (mạch, CRT, nhiệt độ chi, huyết áp) trước mọi quyết định về dịch.<br>"
         f"5) {G('NÊN')} nghĩ ngay viêm phúc mạc tiên phát khi trẻ có báng bụng + sốt/đau bụng: cấy máu, chọc dịch, kháng sinh tĩnh mạch.<br>"
         f"6) {G('NÊN')} dạy gia đình thử que nước tiểu buổi sáng để phát hiện tái phát sớm.",
         "Ba sai lầm KHÔNG đều đến từ việc đọc nhầm một con số (phù to ≠ thừa dịch lòng mạch; canxi toàn phần thấp ≠ hạ canxi "
         "thật). Ba việc NÊN tập trung vào hai nguyên nhân tử vong hàng đầu: sốc giảm thể tích và nhiễm trùng.",
         [IPNA23, BAI], ["Bang-kiem"]),

    # ================================================================ E1. Dịch tễ & mô bệnh học
    cloze(9, "E1", "Dịch tễ học",
          f"Hội chứng thận hư nguyên phát ở trẻ em có đỉnh tuổi khởi phát {cz(Y('2 đến 6 tuổi'))}; tỷ lệ mắc {cz(Y('1,15–16,9 trên 100.000 trẻ/năm'), 2)}.",
          [IPNA23, BAI], ["Dich-te"]),
    cloze(10, "E1", "Mô bệnh học",
          f"Ở trẻ dưới 10 tuổi bị HCTH nguyên phát, bệnh tổn thương tối thiểu (MCD) chiếm {cz(Y('85% đến 90%'))}; xơ chai cầu thận khu trú từng phần (FSGS) chiếm {cz(Y('10% đến 15%'), 2)}.",
          [BAI], ["Mo-benh-hoc"]),
    basic(11, "E1", "Dịch tễ học", 1,
          f"{B('[HCTH trẻ em]')} Tỷ lệ {G('đáp ứng steroid ban đầu')} và tỷ lệ {R('tái phát')} là bao nhiêu?",
          f"1) Khoảng {Y('85–90%')} đạt lui bệnh hoàn toàn trong {Y('4–6 tuần')} corticoid (thể nhạy cảm steroid).<br>"
          f"2) {Y('70–80%')} trong số đó sẽ tái phát ít nhất một đợt.",
          "Bệnh mạn tính tái diễn: tiên lượng sống rất tốt nhưng cần theo dõi lâu dài, dạy gia đình tự thử que nước tiểu.",
          [IPNA23, BAI], ["Dich-te", "Tien-luong"]),
    basic(12, "E1", "Mô bệnh học", 2,
          f"{B('[Bệnh tổn thương tối thiểu — MCD]')} Hình ảnh đặc trưng trên {Y('kính hiển vi điện tử')} là gì?",
          f"{R('Xóa chân lồi tế bào podocyte lan tỏa')} (diffuse foot process effacement).",
          "Kính hiển vi quang học và miễn dịch huỳnh quang bình thường, không có lắng đọng miễn dịch — vì vậy gọi là tổn thương "
          "'tối thiểu'.",
          [BAI], ["Mo-benh-hoc", "MCD"]),

    # ================================================================ E2. Màng lọc, podocyte & cơ chế
    basic(13, "E2", "Giải phẫu màng lọc", 1,
          f"{B('[Hàng rào lọc cầu thận]')} Kể {Y('3 lớp')} giải phẫu của hàng rào lọc cầu thận.",
          f"1) {B('Tế bào nội mô mao mạch')} có lỗ thủng {Y('70–100 nm')}.<br>2) {B('Màng đáy cầu thận (GBM)')} dày {Y('250–350 nm')}.<br>"
          f"3) {B('Tế bào có chân (podocyte)')} với khe lọc {B('slit diaphragm')}.",
          "Cả 3 lớp đều phủ lớp polyanion tích điện âm đẩy albumin (cũng tích điện âm) trở lại lòng mạch.",
          [BAI], ["Mang-loc"]),
    cloze(14, "E2", "Giải phẫu màng lọc",
          f"Khe lọc của màng ngăn có chân (slit diaphragm) giữa các podocyte có kích thước khoảng {cz(Y('4 đến 40 nm'))}.",
          [BAI], ["Mang-loc"]),
    basic(15, "E2", "Sinh lý bệnh podocyte", 2,
          f"{B('[Nephrin]')} Protein Nephrin do gen nào mã hóa và có vai trò gì ở slit diaphragm?",
          f"1) Gen mã hóa: {B('NPHS1')}.<br>2) Vai trò: đan chéo với chân podocyte đối diện, tạo {G('khung mắt lưới chính của khe lọc')}.",
          "Đột biến NPHS1 gây hội chứng thận hư bẩm sinh kiểu Phần Lan — lý do trẻ dưới 1 tuổi cần làm xét nghiệm gen/sinh thiết.",
          [BAI], ["Podocyte", "Di-truyen"], asks=["Gen", "Vai trò"]),
    basic(16, "E2", "Sinh lý bệnh podocyte", 2,
          f"{B('[Podocin]')} Protein Podocin do gen nào mã hóa và có vai trò gì ở slit diaphragm?",
          f"1) Gen mã hóa: {B('NPHS2')}.<br>2) Vai trò: {G('neo giữ và điều hòa tín hiệu của Nephrin')} với khung xương actin nội bào.",
          "Đột biến NPHS2 gây HCTH kháng steroid có tính gia đình — một lý do IPNA 2020 khuyến cáo xét nghiệm gen ở SRNS.",
          [BAI], ["Podocyte", "Di-truyen"], asks=["Gen", "Vai trò"]),
    basic(17, "E2", "Sinh lý bệnh học", 2,
          f"{B('[Chọn lọc điện tích]')} Cơ chế chọn lọc điện tích (charge selectivity) của màng lọc cầu thận là gì?",
          f"Lớp {B('polyanion (heparan sulfate)')} tích điện âm trên màng lọc {G('đẩy albumin (cũng tích điện âm)')} trở lại lòng mạch bằng lực đẩy tĩnh điện.",
          "Mất lớp điện tích âm trong MCD gây protein niệu chọn lọc cao (chủ yếu albumin).",
          [BAI], ["Co-che"]),
    basic(18, "E2", "Sinh lý bệnh học", 2,
          f"{B('[Protein niệu chọn lọc]')} Phân biệt {Y('protein niệu chọn lọc cao')} và {R('protein niệu không chọn lọc')}.",
          f"1) Chọn lọc cao: thoát {Y('chủ yếu albumin')} do mất điện tích âm — gặp trong {B('MCD')}.<br>"
          f"2) Không chọn lọc: thoát cả {R('đại phân tử IgG, transferrin')} do tổn thương cấu trúc màng lọc — gặp trong {B('FSGS')}.",
          "Protein niệu không chọn lọc gợi ý tổn thương cầu thận thực thể nặng hơn và đáp ứng steroid kém hơn.",
          [BAI], ["Co-che"]),
    basic(19, "E2", "Sinh lý bệnh học", 1,
          f"{B('[Thuyết Underfill]')} Chuỗi cơ chế hình thành phù theo thuyết Underfill là gì?",
          f"{R('Mất albumin nặng')} → {R('giảm áp lực keo')} → dịch thoát ra mô kẽ → {R('giảm thể tích nội mạch hiệu dụng')} → {G('kích hoạt RAAS')} giữ muối nước thứ phát.",
          "Hay gặp ở trẻ nhỏ mắc MCD: mạch nhanh, CRT kéo dài, huyết áp thấp — đây là trẻ cần albumin chứ không phải lợi tiểu.",
          [BAI], ["Co-che", "Phu"]),
    basic(20, "E2", "Sinh lý bệnh học", 1,
          f"{B('[Thuyết Overfill]')} Chuỗi cơ chế hình thành phù theo thuyết Overfill là gì?",
          f"{R('Giữ natri nguyên phát tại ống góp (kênh ENaC)')} → ứ muối nước → {R('tăng thể tích nội mạch')} → {G('ức chế RAAS')}.",
          "Hay gặp ở trẻ lớn, FSGS: huyết áp cao, tĩnh mạch cổ nổi; nhóm này đáp ứng với lợi tiểu kèm hạn chế muối nước.",
          [BAI], ["Co-che", "Phu"]),
    basic(21, "E2", "Chuỗi cơ chế", 2,
          f"{B('[Rối loạn lipid máu trong HCTH]')} Cơ chế tăng lipid máu là gì?",
          f"{R('Giảm albumin, giảm áp lực keo')} kích thích gan {R('tăng tổng hợp lipoprotein')}, kèm {R('mất enzym giáng hóa mỡ qua nước tiểu')}.",
          "Hậu quả: cholesterol toàn phần > 5,2 mmol/L, tăng triglyceride và LDL; góp phần tăng nguy cơ tắc mạch.",
          [BAI], ["Co-che", "Lipid"]),
    basic(22, "E2", "Chuỗi cơ chế", 2,
          f"{B('[Hạ canxi giả tạo]')} Vì sao trẻ HCTH {R('giảm canxi toàn phần')} nhưng {G('canxi ion hóa vẫn bình thường')}?",
          f"Khoảng {Y('40%')} canxi toàn phần gắn albumin; albumin giảm thì {R('phần canxi gắn giảm theo')}, còn {G('canxi ion hóa (dạng hoạt động)')} không đổi.",
          "Trẻ không có triệu chứng hạ canxi và không có chỉ định tiêm canxi tĩnh mạch.",
          [BAI], ["Dien-giai", "Canxi"]),

    # ================================================================ E3. Tiêu chuẩn chẩn đoán & đo protein niệu
    basic(23, "E3", "Tiêu chuẩn chẩn đoán", 1,
          f"{B('[Chẩn đoán HCTH]')} Hai tiêu chuẩn sinh hóa {R('bắt buộc')} để chẩn đoán xác định là gì (ghi rõ ngưỡng theo Bộ Y tế và IPNA 2023)?",
          f"1) {R('Protein niệu ngưỡng thận hư')}: {Y('≥ 50 mg/kg/ngày')} (hoặc ≥ 40 mg/m²/giờ, ≥ 1000 mg/m²/ngày) hoặc {Y('Up/Ucr ≥ 2 mg/mg (200 mg/mmol)')}.<br>"
          f"2) {R('Giảm albumin máu')}: {Y('≤ 25 g/L')} theo Bộ Y tế; {Y('< 30 g/L')} theo IPNA 2023.",
          "Hai tiêu chuẩn đi kèm là phù và tăng lipid máu (cholesterol > 5,2 mmol/L). IPNA 2023 còn cho phép chẩn đoán khi có "
          "protein niệu ngưỡng thận hư + phù nếu chưa có kết quả albumin.",
          [BYT, IPNA23], ["Chan-doan"]),
    cloze(24, "E3", "Tiêu chuẩn định lượng",
          f"Protein niệu ngưỡng thận hư trong nước tiểu 24 giờ ở trẻ em: {cz(Y('≥ 50 mg/kg/ngày hoặc ≥ 40 mg/m²/giờ'))}.",
          [BYT, IPNA23], ["Protein-nieu"]),
    cloze(25, "E3", "Tiêu chuẩn định lượng",
          f"Tỷ số protein/creatinin niệu (Up/Ucr) ở ngưỡng thận hư là {cz(Y('≥ 2 mg/mg (≥ 200 mg/mmol)'))}; ở trẻ bình thường Up/Ucr {cz(Y('< 0,2 mg/mg'), 2)}.",
          [IPNA23, BAI], ["Protein-nieu"]),
    cloze(26, "E3", "Tiêu chuẩn que thử",
          f"Trên que thử nước tiểu, protein niệu ngưỡng thận hư tương ứng {cz(Y('3+ (300–1000 mg/dL) đến 4+ (≥ 1000 mg/dL)'))}.",
          [IPNA23], ["Que-thu"]),
    cloze(27, "E3", "Tiêu chuẩn sinh hóa",
          f"Ngưỡng giảm albumin máu trong HCTH: theo Bộ Y tế albumin {cz(Y('≤ 25 g/L'))} kèm protein toàn phần {cz(Y('≤ 56 g/L'), 2)}; theo IPNA 2023 albumin {cz(Y('< 30 g/L'), 3)}.",
          [BYT, IPNA23], ["Albumin"]),
    cloze(28, "E3", "Tiêu chuẩn sinh hóa",
          f"Tăng lipid máu trong HCTH trẻ em: cholesterol toàn phần {cz(Y('> 5,2 mmol/L (> 200 mg/dL)'))}.",
          [BYT], ["Lipid"]),
    basic(29, "E3", "Phương pháp đo lường", 2,
          f"{B('[Up/Ucr mẫu sáng sớm]')} Vì sao ưu tiên {G('Up/Ucr mẫu nước tiểu đầu tiên buổi sáng')} hơn nước tiểu 24 giờ ở trẻ nhỏ?",
          f"1) {G('Tránh sai số')} do trẻ chưa bỏ tã, khó gom đủ 24 giờ.<br>2) {G('Có kết quả nhanh')} để xử trí.<br>3) {G('Loại trừ protein niệu tư thế')}.",
          "Up/Ucr ≥ 2 mg/mg tương quan tốt với protein niệu 24 giờ ≥ 50 mg/kg/ngày; IPNA 2023 khuyến cáo đo Up/Ucr mẫu sáng ít nhất "
          "một lần trước khi bắt đầu điều trị.",
          [IPNA23, BAI], ["Protein-nieu"]),

    # ================================================================ E4. Lâm sàng, bilan & sinh thiết
    basic(30, "E4", "Đặc điểm phù", 2,
          f"{B('[Phù trong HCTH]')} Mô tả đặc điểm phù.",
          f"{R('Phù trắng, mềm, ấn lõm, không đau, đối xứng')}; bắt đầu ở {Y('mi mắt buổi sáng')}, sau đó lan toàn thân, có thể {R('tràn dịch đa màng')}.",
          "Theo dõi lượng dịch báng bằng cân nặng và vòng bụng ngang rốn mỗi ngày.",
          [BYT, BAI], ["Lam-sang", "Phu"]),
    basic(31, "E4", "Bilan xét nghiệm", 2,
          f"{B('[Cặn lắng nước tiểu]')} Thấy {R('thể mỡ lưỡng chiết (chữ thập Maltese)')} có ý nghĩa gì?",
          f"Dấu hiệu đặc trưng của {R('lipid niệu nặng')} trong HCTH.",
          "Quan sát dưới kính hiển vi phân cực. Soi cặn còn giúp tìm trụ hồng cầu — gợi ý viêm cầu thận chứ không phải MCD.",
          [BAI], ["Can-lam-sang"]),
    basic(32, "E4", "Bilan xét nghiệm", 2,
          f"{B('[Sàng lọc lao]')} Vì sao nên làm {G('Mantoux hoặc QuantiFERON')} trước khi dùng corticoid/ức chế miễn dịch ở trẻ HCTH tại Việt Nam?",
          f"1) Để {R('phát hiện lao tiềm ẩn')}: corticoid liều cao kéo dài có thể làm bùng phát lao (lao kê, lao màng não).<br>"
          f"2) IPNA 2023 khuyến cáo {G('cân nhắc sàng lọc lao')}, đặc biệt ở {Y('vùng lưu hành như Việt Nam')}.",
          "Nếu có lao tiềm ẩn, bài khuyên điều trị dự phòng isoniazid đồng thời với corticoid.",
          [IPNA23, BAI], ["Can-lam-sang", "Lao"]),
    basic(33, "E4", "Chỉ định sinh thiết thận", 1,
          f"{B('[Sinh thiết thận]')} Vì sao {Y('không sinh thiết thường quy')} ở trẻ {Y('1 đến 10 tuổi')} khởi phát HCTH điển hình?",
          f"Vì {Y('85–90%')} trẻ nhóm này là {B('MCD')} và {G('đáp ứng corticoid')}; tránh thủ thuật xâm lấn không cần thiết.",
          "Chỉ sinh thiết khi có dấu hiệu không điển hình (tuổi, tăng huyết áp, đái máu đại thể, suy thận, bổ thể giảm, biểu hiện "
          "ngoài thận) hoặc kháng steroid.",
          [BAI], ["Sinh-thiet"]),
    basic(34, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — tuổi]')} Lứa tuổi khởi phát nào là chỉ định sinh thiết thận?",
          f"1) Trẻ {Y('< 1 tuổi')}: nghi đột biến gen podocyte.<br>2) Trẻ {Y('> 12 tuổi')}: nguy cơ cao FSGS, bệnh thận màng, lupus.",
          "Trẻ 1–12 tuổi có biểu hiện điển hình được điều trị corticoid trước.",
          [BAI], ["Sinh-thiet"]),
    basic(35, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — đái máu]')} Kiểu đái máu nào là chỉ định sinh thiết?",
          f"{R('Đái máu đại thể dai dẳng')}.",
          "Đái máu vi thể thoáng qua gặp ở khoảng 20% trẻ MCD và không phải chỉ định sinh thiết.",
          [BAI], ["Sinh-thiet"]),
    basic(36, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — huyết áp]')} Mức huyết áp nào là chỉ định sinh thiết?",
          f"{R('Tăng huyết áp kéo dài')}: {Y('> bách phân vị 95')} theo tuổi/giới, tồn tại dai dẳng.",
          "Vẫn tăng sau khi đã kiểm soát phù và ngừng thuốc gây tăng huyết áp (corticoid liều cao có thể gây tăng huyết áp thoáng qua).",
          [BAI], ["Sinh-thiet"]),
    basic(37, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — chức năng thận]')} Suy giảm chức năng thận kiểu nào là chỉ định sinh thiết?",
          f"{R('Creatinin tăng, eGFR giảm dai dẳng')}, {R('không hồi phục sau khi đã bù đủ thể tích')}.",
          "Phân biệt với tổn thương thận cấp trước thận do giảm tưới máu — loại này hồi phục nhanh sau bù albumin.",
          [BAI], ["Sinh-thiet"]),
    basic(38, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — bổ thể]')} Kết quả bổ thể nào là chỉ định sinh thiết?",
          f"{R('Giảm C3 hoặc C4')} huyết thanh.",
          "MCD có bổ thể bình thường; giảm bổ thể gợi ý viêm cầu thận màng tăng sinh, viêm cầu thận sau nhiễm liên cầu hoặc lupus.",
          [BAI], ["Sinh-thiet"]),
    basic(39, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — ngoài thận]')} Biểu hiện ngoài thận nào là chỉ định sinh thiết?",
          f"Dấu hiệu gợi ý bệnh hệ thống: {R('sốt kéo dài, ban cánh bướm, loét miệng, viêm đa khớp, ban Schönlein–Henoch')}.",
          "Gợi ý HCTH thứ phát do bệnh tự miễn hệ thống.",
          [BAI], ["Sinh-thiet"]),
    basic(40, "E4", "Chỉ định sinh thiết thận", 2,
          f"{B('[Sinh thiết thận — kháng steroid]')} Không lui bệnh sau bao lâu corticoid liều chuẩn thì chỉ định sinh thiết?",
          f"Không lui bệnh hoàn toàn sau {Y('4 tuần')} prednisolone liều chuẩn hàng ngày → {R('kháng steroid (SRNS)')}.",
          "IPNA 2020 khuyến cáo sinh thiết thận và xét nghiệm gen ở SRNS trước khi dùng thuốc ức chế miễn dịch bậc hai.",
          [IPNA20], ["Sinh-thiet", "SRNS"]),

    # ================================================================ E5. Corticoid đợt đầu
    cloze(41, "E5", "Phác đồ tấn công",
          f"Liều tấn công prednisolone đợt đầu: {cz(Y('60 mg/m²/ngày hoặc 2 mg/kg/ngày'))} (tối đa {cz(Y('60 mg/ngày'), 2)}) uống 1 lần buổi sáng trong {cz(Y('4 tuần hoặc 6 tuần'), 3)}.",
          [IPNA23, KDIGO], ["Corticoid"]),
    cloze(42, "E5", "Phác đồ duy trì",
          f"Liều cách ngày sau giai đoạn tấn công: {cz(Y('40 mg/m² hoặc 1,5 mg/kg cách ngày'))} (tối đa {cz(Y('40 mg'), 2)} theo IPNA) trong {cz(Y('4 tuần (sau tấn công 4 tuần) hoặc 6 tuần (sau tấn công 6 tuần)'), 3)}.",
          [IPNA23, KDIGO], ["Corticoid"]),
    cloze(43, "E5", "Thời gian điều trị",
          f"Tổng thời gian corticoid đợt đầu theo IPNA 2023/KDIGO 2021 là {cz(Y('8 tuần (4 + 4) hoặc 12 tuần (6 + 6)'))}.",
          [IPNA23, KDIGO], ["Corticoid"]),
    cloze(44, "E5", "Bằng chứng Cochrane",
          f"Cochrane 2020 so 2 tháng với ≥ 3 tháng prednisone đợt đầu thấy tái phát bất kỳ sau 12–24 tháng ít hoặc không khác biệt với {cz(Y('RR 0,91 (95% CI 0,78–1,06)'))}.",
          [COCH], ["Cochrane"]),
    basic(45, "E5", "Dược lý lâm sàng", 2,
          f"{B('[Prednisolone]')} Vì sao uống {G('1 lần duy nhất buổi sáng')}?",
          f"1) {G('Giảm ức chế trục hạ đồi – tuyến yên – thượng thận')} (gần nhịp tiết cortisol tự nhiên).<br>2) Giảm rối loạn giấc ngủ, dễ tuân thủ.",
          "IPNA 2023 khuyến cáo một liều buổi sáng cho đợt đầu và các đợt tái phát; chia liều không tăng hiệu quả lui bệnh.",
          [IPNA23], ["Corticoid"]),
    basic(46, "E5", "Tác dụng phụ Corticoid", 2,
          f"{B('[Corticoid kéo dài]')} Kể các {R('tác dụng phụ')} khi kéo dài corticoid đợt đầu (ví dụ lên 6 tháng).",
          f"{R('Chậm tăng trưởng chiều cao, béo phì kiểu Cushing, loãng xương, rậm lông, rạn da, tăng huyết áp, đục thủy tinh thể')}, rối loạn hành vi.",
          "Cochrane 2020: kéo dài quá 2–3 tháng không giảm tái phát (tác dụng phụ giữa các thời gian điều trị ít khác biệt trong các RCT); "
          "vì không có lợi ích mà tăng tổng liều tích lũy, phác đồ chuẩn chỉ 8 hoặc 12 tuần.",
          [COCH, IPNA23], ["Corticoid", "Tac-dung-phu"]),
    basic(47, "E5", "Quy trình ngưng thuốc", 2,
          f"{B('[Kết thúc đợt corticoid]')} Hết giai đoạn cách ngày thì {G('ngưng thuốc')} thế nào — có cần {Y('giảm liều dần')} không?",
          f"1) Hết {Y('4–6 tuần')} cách ngày thì {G('ngưng thuốc')}.<br>2) IPNA 2023 {R('không khuyến cáo giảm liều dần')} trong giai đoạn cách ngày (khuyến cáo mạnh, mức A).",
          "Các RCT chất lượng cao không giảm liều dần và gần như không ghi nhận suy thượng thận; giảm liều dần chỉ làm tăng liều tích lũy.",
          [IPNA23], ["Corticoid"]),
    basic(48, "E5", "Điều chỉnh phác đồ", 2,
          f"{B('[Đáp ứng một phần sau 4 tuần]')} Trẻ chỉ {Y('lui bệnh một phần')} sau 4 tuần prednisolone liều chuẩn thì xử trí thế nào?",
          f"1) Vào {B('giai đoạn xác nhận')} từ {Y('tuần 4 đến tuần 6')}: tiếp tục prednisolone uống ± truyền methylprednisolone, thêm thuốc ức chế RAAS.<br>"
          f"2) Lui bệnh hoàn toàn trong giai đoạn này → {G('đáp ứng muộn')}; vẫn không lui bệnh hoàn toàn đến tuần 6 → {R('SRNS')}.",
          "Trẻ không thay đổi protein niệu sau 4 tuần đã đủ tiêu chuẩn kháng steroid. Giai đoạn xác nhận chỉ dành cho trẻ đáp ứng một phần.",
          [IPNA23], ["Corticoid", "SRNS"]),
    basic(49, "E5", "Dự phòng biến chứng xương", 2,
          f"{B('[Xương khi dùng corticoid]')} Có cần {G('bổ sung canxi và vitamin D thường quy')} không, và theo dõi gì?",
          f"1) {R('Không bổ sung thường quy')}: đảm bảo {G('khẩu phần canxi đủ')}, chỉ cho canxi uống khi khẩu phần thiếu.<br>"
          f"2) Định lượng {G('25-OH-vitamin D mỗi năm')} ở thể {B('FRNS/SDNS')}, mục tiêu {Y('> 20 ng/mL (> 50 nmol/L)')}; thiếu thì điều trị theo hướng dẫn quốc gia.",
          "Dữ liệu về loãng xương do corticoid ở trẻ HCTH còn mâu thuẫn, nên IPNA 2023 không kê canxi/vitamin D cho mọi trẻ.",
          [IPNA23], ["Xuong"]),

    # ================================================================ E6. Định nghĩa đáp ứng & tái phát
    cloze(50, "E6", "Định nghĩa đáp ứng",
          f"Lui bệnh hoàn toàn: Up/Ucr mẫu sáng {cz(Y('≤ 0,2 mg/mg (≤ 20 mg/mmol)'))} hoặc que thử âm tính/vết trong {cz(Y('≥ 3 ngày liên tiếp'), 2)}.",
          [IPNA23], ["Dinh-nghia"]),
    cloze(51, "E6", "Định nghĩa đáp ứng",
          f"Tái phát: que thử {cz(Y('≥ 3+'))} hoặc Up/Ucr {cz(Y('≥ 2 mg/mg'), 2)} trong {cz(Y('3 ngày liên tiếp'), 3)} ở trẻ đã từng lui bệnh hoàn toàn.",
          [IPNA23], ["Dinh-nghia"]),
    cloze(52, "E6", "Định nghĩa đáp ứng",
          f"Tái phát thường xuyên (FRNS) theo IPNA 2023: {cz(Y('≥ 2 đợt trong 6 tháng đầu sau lui bệnh đợt đầu, hoặc ≥ 3 đợt trong bất kỳ 12 tháng nào'))}.",
          [IPNA23], ["Dinh-nghia", "FRNS"]),
    cloze(53, "E6", "Định nghĩa đáp ứng",
          f"Phụ thuộc steroid (SDNS): {cz(Y('2 đợt tái phát liên tiếp'))} trong khi đang dùng prednisolone theo phác đồ hoặc trong vòng {cz(Y('14 ngày'), 2)} sau khi ngừng.",
          [IPNA23], ["Dinh-nghia", "SDNS"]),
    cloze(54, "E6", "Định nghĩa đáp ứng",
          f"Kháng steroid (SRNS): không lui bệnh hoàn toàn sau {cz(Y('4 tuần'))} prednisolone liều chuẩn {cz(Y('60 mg/m²/ngày hoặc 2 mg/kg/ngày'), 2)}.",
          [IPNA20, IPNA23], ["Dinh-nghia", "SRNS"]),
    basic(55, "E6", "Xử trí tái phát", 1,
          f"{B('[Tái phát thông thường — SSNS]')} Phác đồ prednisolone cho một đợt tái phát không biến chứng?",
          f"1) {G('Prednisolone 60 mg/m²/ngày (2 mg/kg/ngày, tối đa 60 mg)')} cho đến khi {Y('lui bệnh hoàn toàn ≥ 3 ngày')}.<br>"
          f"2) Chuyển {G('40 mg/m² (1,5 mg/kg, tối đa 40 mg) cách ngày')} trong {Y('4 tuần')} rồi ngưng, {R('không giảm liều dần')}.",
          "Khác đợt đầu: không cần tấn công đủ 4 tuần, chỉ đến khi hết protein niệu 3 ngày.",
          [IPNA23], ["Tai-phat"]),
    basic(56, "E6", "Quản lý lâm sàng", 2,
          f"{B('[Sốt siêu vi khi đang điều trị]')} Trẻ đang duy trì steroid bị sốt siêu vi, que thử {Y('1+ hoặc 2+')}: xử trí thế nào?",
          f"1) {Y('Chưa kết luận tái phát')}.<br>2) {G('Hạ sốt, thử que mỗi sáng 3–5 ngày')}; âm tính trở lại thì {G('giữ nguyên liều')}.",
          "Tái phát đòi hỏi ≥ 3+ trong 3 ngày liên tiếp. Sốt có thể gây protein niệu phản ứng thoáng qua.",
          [IPNA23, BAI], ["Tai-phat"]),
    algo("A2", "E6", "Phân loại đáp ứng corticoid",
         "Sau 4 tuần prednisolone liều chuẩn: xếp loại đáp ứng thế nào?",
         f"1) Lui bệnh hoàn toàn trong {Y('4 tuần')} → {G('nhạy cảm steroid (SSNS)')} → chuyển cách ngày.<br>"
         f"2) Lui bệnh một phần ở tuần 4 → {B('giai đoạn xác nhận')} tuần {Y('4–6')}: prednisolone ± methylprednisolone tĩnh mạch + ức chế RAAS.<br>"
         f"3) Lui bệnh hoàn toàn đến tuần 6 → {G('đáp ứng muộn')}; vẫn chưa → {R('SRNS')}.<br>"
         f"4) SRNS → {R('sinh thiết thận + xét nghiệm gen')}, khởi động {G('thuốc ức chế calcineurin')} (IPNA 2020).",
         "Mốc 4 tuần là bắt buộc trước khi gọi kháng steroid; kết luận sau 2 tuần là sai. Giai đoạn xác nhận tránh xếp nhầm trẻ đáp ứng chậm.",
         [IPNA23, IPNA20], ["Phan-loai"]),
    algo("A4", "E6", "Phân loại diễn tiến SSNS",
         "Trẻ nhạy cảm steroid tái phát: khi nào là FRNS, SDNS và cần thuốc tiết kiệm steroid?",
         f"1) Tái phát không thường xuyên: {Y('< 2 đợt/6 tháng đầu và < 3 đợt/12 tháng')} → mỗi đợt dùng lại prednisolone.<br>"
         f"2) {B('FRNS')}: {Y('≥ 2 đợt trong 6 tháng đầu')} hoặc {Y('≥ 3 đợt trong 12 tháng')}.<br>"
         f"3) {B('SDNS')}: {Y('2 đợt liên tiếp')} khi đang dùng prednisolone hoặc trong {Y('14 ngày')} sau ngừng.<br>"
         f"4) FRNS/SDNS → {G('thuốc tiết kiệm steroid')}: levamisole, cyclophosphamide, CNI, MMF, rituximab.",
         "Mốc 12 tháng của IPNA 2023 là ≥ 3 đợt (các định nghĩa cũ dùng ≥ 4). Mục tiêu điều trị là giảm độc tính tích lũy của corticoid.",
         [IPNA23], ["Phan-loai"]),

    # ================================================================ E7. Biến chứng cấp, theo dõi
    cloze(57, "E7", "Cấp cứu biến chứng",
          f"Albumin 20% khi giảm thể tích (chưa tụt huyết áp) hoặc phù nặng: {cz(Y('0,5–1 g/kg (2,5–5 mL/kg)'))}, truyền chậm trong {cz(Y('4–6 giờ'), 2)}.",
          [IPNA23], ["Albumin"]),
    cloze(58, "E7", "Cấp cứu biến chứng",
          f"Furosemid sau albumin dùng liều {cz(Y('1–2 mg/kg tĩnh mạch'))}. Thời điểm tiêm là {cz(Y('giữa và/hoặc cuối'), 2)} buổi truyền khi thể tích đã được bù mà nước tiểu vẫn ít.",
          [IPNA23], ["Furosemid"]),
    basic(59, "E7", "Cấp cứu biến chứng", 2,
          f"{B('[Truyền albumin 20%]')} Dấu hiệu {R('quá tải thể tích / phù phổi cấp')} khi truyền là gì và xử trí ngay thế nào?",
          f"1) Dấu hiệu: {R('khó thở đột ngột, thở nhanh co kéo, SpO₂ tụt, ho bọt hồng, ran ẩm hai phổi')}.<br>"
          f"2) Xử trí: {G('ngừng truyền albumin, nằm đầu cao, thở oxy/áp lực dương, tiêm Furosemid tĩnh mạch')}.",
          "Albumin ưu trương kéo dịch về lòng mạch nhanh; IPNA 2023 nhấn mạnh theo dõi sát khi truyền để tránh tăng thể tích và phù phổi.",
          [IPNA23, BAI], ["Albumin", "Phu-phoi"], asks=["Dấu hiệu", "Xử trí"]),
    cloze(60, "E7", "Cấp cứu nhiễm trùng",
          f"Kháng sinh đầu tay cho viêm phúc mạc tiên phát: {cz(G('Ceftriaxone 80–100 mg/kg/ngày'))} tĩnh mạch 1 lần/ngày (hoặc Cefotaxim 150 mg/kg/ngày chia 3).",
          [BAI], ["Nhiem-trung"]),
    cloze(61, "E7", "Cấp cứu nhiễm trùng",
          f"Gợi ý viêm phúc mạc tiên phát khi dịch màng bụng có bạch cầu {cz(Y('> 250/mm³'))} với đa nhân trung tính {cz(Y('> 50%'), 2)}.",
          [BAI], ["Nhiem-trung"]),
    basic(62, "E7", "Nhiễm trùng da", 2,
          f"{B('[Viêm mô tế bào ở trẻ HCTH]')} Vị trí hay gặp, căn nguyên và kháng sinh lựa chọn?",
          f"1) Vị trí: {R('vùng da phù căng, nứt nẻ')} — cẳng chân, bìu/âm hộ.<br>"
          f"2) Căn nguyên: {R('liên cầu nhóm A, tụ cầu vàng')}.<br>"
          f"3) Kháng sinh: {G('oxacillin/cefazolin')}; {G('vancomycin')} nếu nghi MRSA.",
          "Da phù mất hàng rào bảo vệ cơ học, vi khuẩn dễ xâm nhập.",
          [BAI], ["Nhiem-trung"], asks=["Vị trí", "Căn nguyên", "Kháng sinh"]),
    basic(63, "E7", "Biến chứng tắc mạch", 2,
          f"{B('[Huyết khối trong HCTH]')} Kể {Y('4 vị trí')} huyết khối nguy hiểm nhất.",
          f"1) {R('Huyết khối tĩnh mạch sâu chi dưới')}.<br>2) {R('Huyết khối tĩnh mạch thận')} (đái máu, đau hông lưng, thận to).<br>"
          f"3) {R('Huyết khối xoang tĩnh mạch não')} (đau đầu dữ dội, co giật).<br>4) {R('Thuyên tắc động mạch phổi')} (khó thở đột ngột, ho máu, tụt SpO₂).",
          "Nghiên cứu MWPNC (326 trẻ) ghi nhận 9,2% có ít nhất 1 biến cố huyết khối; huyết khối tĩnh mạch sâu chiếm 76%; tuổi ≥ 12 là yếu tố tiên đoán độc lập.",
          [KERLIN, BAI], ["Huyet-khoi"]),
    basic(64, "E7", "Dự phòng chống đông", 2,
          f"{B('[Dự phòng huyết khối]')} Có dự phòng {G('chống đông/kháng tiểu cầu thường quy')} cho trẻ HCTH không, và khi nào cân nhắc?",
          f"1) {R('Không dự phòng thường quy')} trong giai đoạn thận hư cấp (IPNA 2023).<br>"
          f"2) {G('Cân nhắc trong đợt tái phát')} khi có nguy cơ cao đã xác định: tiền sử huyết khối, thrombophilia gia đình, catheter tĩnh mạch trung tâm, bất động, nhiễm trùng phải nằm viện.",
          "Chưa đủ bằng chứng cho dự phòng thường quy; cần đánh giá nguy cơ từng trẻ, tư vấn gia đình nhận biết triệu chứng huyết khối, "
          "và quyết định thuốc/liều cùng chuyên khoa.",
          [IPNA23], ["Huyet-khoi"]),
    basic(65, "E7", "Rối loạn điện giải", 2,
          f"{B('[Canxi hiệu chỉnh]')} Công thức tính canxi hiệu chỉnh theo albumin máu?",
          f"{G('Canxi hiệu chỉnh (mmol/L) = Canxi đo được + 0,02 × (40 − Albumin g/L)')}.",
          "Canxi hiệu chỉnh trong giới hạn bình thường (2,15–2,55 mmol/L) → hạ canxi giả tạo, không tiêm canxi tĩnh mạch.",
          [BAI], ["Canxi", "Cong-thuc"]),
    basic(66, "E7", "Rối loạn điện giải", 2,
          f"{B('[Tiêm canxi tĩnh mạch]')} Khi nào mới có chỉ định {G('tiêm canxi tĩnh mạch')} ở trẻ HCTH?",
          f"Khi có {R('triệu chứng hạ canxi')} (Chvostek, Trousseau, co thắt thanh quản, co giật) {Y('VÀ')} {R('canxi ion hóa thực sự giảm')}.",
          "Không tiêm chỉ dựa vào canxi toàn phần giảm.",
          [BAI], ["Canxi"]),
    basic(67, "E7", "Tác dụng phụ lợi tiểu", 2,
          f"{B('[Furosemid liều cao]')} Các rối loạn điện giải/chuyển hóa cần theo dõi?",
          f"1) {R('Hạ kali máu và kiềm chuyển hóa')}.<br>2) {R('Hạ natri máu')}.<br>3) {R('Tăng acid uric máu')}.",
          "Kiểm tra điện giải đồ sau 24–48 giờ; bù kali uống khi K⁺ < 3,5 mmol/L.",
          [BAI], ["Furosemid", "Dien-giai"]),
    basic(79, "E7", "Tiêu chuẩn xuất viện", 2,
          f"{B('[Xuất viện đợt đầu]')} Kể các {G('tiêu chuẩn xuất viện an toàn')}.",
          f"1) {G('Huyết động ổn định')}, hết dấu hiệu giảm/quá tải thể tích.<br>2) {G('Phù giảm rõ, tiểu tốt')} ({Y('> 1,5–2 mL/kg/giờ')}).<br>"
          f"3) {G('Đã loại trừ nhiễm trùng, dung nạp corticoid uống, gia đình thành thạo que thử tại nhà')}.",
          "Gia đình tự thử que nước tiểu buổi sáng là mấu chốt để phát hiện tái phát sớm.",
          [BAI], ["Xuat-vien"]),
    algo("A1", "E7", "Lưu đồ dịch truyền",
         "Trẻ HCTH có dấu hiệu giảm thể tích: albumin nào, có Furosemid không?",
         f"1) Mọi trẻ giảm thể tích: {R('ngừng lợi tiểu và ngừng ức chế men chuyển/chẹn thụ thể angiotensin')}.<br>"
         f"2) {R('Sốc / tụt huyết áp')} → {G('Albumin 4–5%')}, {R('không kèm Furosemid')} (chưa có: NaCl 0,9% {Y('10–20 mL/kg')}).<br>"
         f"3) {Y('Giảm thể tích chưa tụt huyết áp')} (thiểu niệu, CRT kéo dài, mạch nhanh, đau bụng) → {G('Albumin 20–25%')} {Y('0,5–1 g/kg')} truyền chậm.<br>"
         f"4) Thể tích đã bù mà nước tiểu vẫn ít → {G('Furosemid 1–2 mg/kg tĩnh mạch')} giữa/cuối buổi truyền; theo dõi phù phổi.",
         "Nồng độ albumin đi theo huyết áp: sốc cần dung dịch đẳng trương làm đầy lòng mạch; chưa sốc thì dùng albumin ưu trương "
         "kéo dịch từ mô kẽ về. Furosemid luôn đi sau và có điều kiện.",
         [IPNA23], ["Albumin", "Furosemid"]),

    # ================================================================ E8. Thuốc bậc hai
    cloze(68, "E8", "Thuốc bậc hai",
          f"Levamisole cho FRNS/SDNS: {cz(Y('2–2,5 mg/kg cách ngày'))} (tối đa 150 mg); tác dụng phụ cần theo dõi: {cz(R('giảm bạch cầu trung tính'), 2)}.",
          [IPNA23], ["Levamisole"]),
    cloze(69, "E8", "Thuốc bậc hai",
          f"Cyclophosphamide uống {cz(Y('2 mg/kg/ngày × 12 tuần hoặc 3 mg/kg/ngày × 8 tuần'))} trong một đợt duy nhất. Liều tích lũy tối đa là {cz(Y('168 mg/kg'), 2)}.",
          [IPNA23], ["Cyclophosphamide"]),
    cloze(70, "E8", "Thuốc bậc hai",
          f"Cyclosporin A: khởi đầu {cz(Y('3–5 mg/kg/ngày'))} chia 2 lần; nồng độ đáy mục tiêu {cz(Y('60–100 ng/mL'), 2)} ở SSNS và {cz(Y('80–120 ng/mL'), 3)} ở SRNS.",
          [IPNA23, IPNA20], ["CNI"]),
    cloze(71, "E8", "Thuốc bậc hai",
          f"Tacrolimus: khởi đầu {cz(Y('0,1–0,2 mg/kg/ngày'))} chia 2 lần; nồng độ đáy mục tiêu {cz(Y('3–7 ng/mL'), 2)} ở SSNS và {cz(Y('4–8 ng/mL'), 3)} ở SRNS.",
          [IPNA23, IPNA20], ["CNI"]),
    cloze(72, "E8", "Thuốc bậc hai",
          f"Mycophenolate mofetil cho FRNS/SDNS: {cz(Y('1200 mg/m²/ngày'))} chia 2 lần (tối đa 3000 mg); ưu điểm: {cz(G('không độc thận'), 2)}.",
          [IPNA23, BAI], ["MMF"]),
    cloze(73, "E8", "Thuốc sinh học",
          f"Rituximab dùng {cz(Y('375 mg/m²/liều'))} cách tuần với 1–4 liều mỗi đợt. Mục tiêu là làm cạn tế bào B CD19 {cz(Y('< 5 tế bào/mm³ hoặc < 1% lympho'), 2)}.",
          [IPNA23], ["Rituximab"]),
    basic(74, "E8", "So sánh thuốc", 2,
          f"{B('[CNI trong SRNS]')} IPNA 2020 chọn thuốc ức chế miễn dịch đầu tay nào cho SRNS, và chọn giữa {G('Cyclosporin A')} với {G('Tacrolimus')} dựa vào đâu?",
          f"1) Đầu tay: {G('thuốc ức chế calcineurin — Cyclosporin A hoặc Tacrolimus')}.<br>"
          f"2) Chọn theo tác dụng phụ: CsA gây {R('rậm lông, phì đại nướu')}; Tacrolimus gây {R('rối loạn dung nạp glucose, đái tháo đường')}.",
          "IPNA 2020 không xếp thuốc nào mạnh hơn. Ở trẻ lớn quan tâm thẩm mỹ thường chọn Tacrolimus; cả hai đều độc thận, phải theo dõi "
          "nồng độ đáy và creatinin. Trước CNI, IPNA 2020 khuyến cáo bắt đầu ức chế RAAS ngay khi chẩn đoán SRNS.",
          [IPNA20], ["CNI", "SRNS"]),
    algo("A3", "E8", "Bảng liều thuốc bỏ túi",
         "Bảng liều thuốc HCTH trẻ em",
         f"1) Prednisolone đợt đầu: {Y('60 mg/m² hoặc 2 mg/kg/ngày')} (tối đa 60 mg) rồi {Y('40 mg/m² hoặc 1,5 mg/kg cách ngày')} (tối đa 40 mg), phác đồ {Y('4 + 4 hoặc 6 + 6 tuần')}.<br>"
         f"2) Albumin 20–25%: {Y('0,5–1 g/kg')}; Furosemid {Y('1–2 mg/kg tĩnh mạch')} giữa/cuối truyền.<br>"
         f"3) Levamisole {Y('2–2,5 mg/kg cách ngày')}; Cyclophosphamide {Y('2 mg/kg × 12 tuần')} (tích lũy ≤ 168 mg/kg).<br>"
         f"4) CsA {Y('3–5 mg/kg/ngày')} (C0 60–100 SSNS / 80–120 SRNS); Tacrolimus {Y('0,1–0,2 mg/kg/ngày')} (C0 3–7 SSNS / 4–8 SRNS).<br>"
         f"5) MMF {Y('1200 mg/m²/ngày')}; Rituximab {Y('375 mg/m²/liều')} × 1–4.",
         "Corticoid tính theo cân nặng khô ước tính (IPNA 2023), không theo cân nặng lúc phù.",
         [IPNA23, IPNA20], ["Lieu"]),

    # ================================================================ E9. Dinh dưỡng & tiêm chủng
    cloze(75, "E9", "Chế độ dinh dưỡng",
          f"Khi tái phát có phù vừa hoặc nặng thì natri tối đa {cz(Y('2–3 mEq/kg/ngày (khoảng 2000 mg/ngày ở trẻ lớn)'))}. Khi lui bệnh thì {cz(G('ăn muối bình thường'), 2)}.",
          [IPNA23], ["Dinh-duong"]),
    basic(76, "E9", "Chế độ dinh dưỡng", 2,
          f"{B('[Đạm trong HCTH]')} Lượng đạm khuyến cáo là bao nhiêu, và vì sao {R('không ép ăn nhiều đạm')}?",
          f"1) Lượng đạm {G('như khuyến nghị cho trẻ khỏe cùng tuổi')} (IPNA 2023).<br>"
          f"2) Ép ăn nhiều đạm {R('tăng gánh lọc cầu thận và protein niệu')}, không bù được albumin mất.",
          "Kiêng đạm thì trẻ suy dinh dưỡng, teo cơ; ăn quá nhiều đạm thì tăng protein niệu. Đúng nhất là ăn như trẻ khỏe cùng tuổi.",
          [IPNA23, BAI], ["Dinh-duong"]),
    basic(77, "E9", "Tiêm chủng vắc xin", 2,
          f"{B('[Vắc xin sống]')} Nguyên tắc tiêm vắc xin sống giảm độc lực cho trẻ HCTH đang điều trị?",
          f"1) {R('Không tiêm')} khi đang dùng ức chế miễn dịch liều cao (prednisolone {Y('≥ 2 mg/kg/ngày hoặc ≥ 20 mg/ngày')}) và trong {Y('6 tháng')} sau rituximab.<br>"
          f"2) Sau ngừng corticoid liều cao, đợi {Y('ít nhất 1–3 tháng')}; theo hướng dẫn tiêm chủng quốc gia.",
          "IPNA 2023 khuyến cáo tiêm vắc xin sống cho người sống cùng nhà nếu trẻ chưa tiêm được, để tạo vòng bảo vệ.",
          [IPNA23, BAI], ["Tiem-chung"]),
    basic(78, "E9", "Tiêm chủng vắc xin", 2,
          f"{B('[Vắc xin bất hoạt]')} Vắc xin nào cần ưu tiên cho trẻ HCTH?",
          f"{G('Phế cầu (PCV13, nhắc PPSV23)')} và {G('cúm mùa hằng năm')}; hoàn thành lịch cho vi khuẩn có vỏ (não mô cầu, Hib), viêm gan B, thủy đậu.",
          "Phòng viêm phúc mạc do phế cầu và giảm tái phát do nhiễm virus; IPNA 2023 khuyến cáo tiêm cúm hằng năm cho cả người sống cùng nhà.",
          [IPNA23, BAI], ["Tiem-chung"]),

    # ================================================================ E10. Bẫy lâm sàng
    basic(80, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Nhận định {R('trẻ phù to nứt da là thừa dịch toàn bộ')} dẫn đến sai lầm gì?",
          f"{R('Vội dùng Furosemid liều cao')} khi lòng mạch đang thiếu dịch → {R('sốc, huyết khối não/phổi')}.",
          "Phần lớn dịch nằm ở mô kẽ; phải kiểm tra tưới máu trước khi dùng lợi tiểu.",
          [IPNA23, BAI], ["Bay"]),
    basic(81, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Trẻ HCTH {R('thiểu niệu')} mà {R('tăng liều Furosemid')} dẫn đến hậu quả gì?",
          f"{R('Tổn thương thận cấp (hoại tử ống thận), sốc giảm thể tích, huyết khối')}.",
          "Thiểu niệu là phản xạ bảo tồn dịch; khi giảm thể tích phải bù albumin trước, lợi tiểu chỉ khi đã bù đủ mà vẫn ít nước tiểu.",
          [IPNA23], ["Bay"]),
    basic(82, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Nhầm {R('viêm phúc mạc tiên phát')} với đau bụng do phù nề ruột dẫn đến nguy cơ gì?",
          f"{R('Chậm chọc dò và kháng sinh')} → {R('sốc nhiễm khuẩn do phế cầu, tử vong')}.",
          "Trẻ HCTH báng bụng có sốt hoặc đau bụng đều phải nghĩ viêm phúc mạc tiên phát.",
          [BAI], ["Bay"]),
    basic(83, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} {R('Ngừng đột ngột Prednisolone liều cao hàng ngày')} vì sợ mặt Cushing gây hậu quả gì, và cách ngưng đúng?",
          f"1) Hậu quả: nguy cơ {R('suy thượng thận trung ương thoáng qua')} (nhất là khi stress) và {R('hỏng đợt điều trị')}.<br>"
          f"2) Cách ngưng đúng: {G('chuyển liều cách ngày đúng phác đồ')} rồi ngưng; {Y('không cần giảm liều dần')} giai đoạn cách ngày (IPNA 2023).",
          "Mặt Cushing là tác dụng phụ dự kiến và hồi phục; tư vấn trước cho gia đình để tránh tự bỏ thuốc.",
          [IPNA23], ["Bay"], asks=["Hậu quả", "Cách ngưng đúng"]),
    basic(84, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Thấy {R('canxi toàn phần thấp')} mà vội {R('tiêm canxi tĩnh mạch')} có nguy cơ gì?",
          f"{R('Loạn nhịp tim')} và {R('hoại tử mô nếu thoát mạch')}, trong khi {G('canxi ion hóa bình thường')}.",
          "Đây là hạ canxi giả tạo do giảm albumin; chỉ tiêm khi có triệu chứng và canxi ion hóa thực sự giảm.",
          [BAI], ["Bay"]),
    basic(85, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} {R('Ép trẻ ăn gấp đôi đạm')} để bù protein mất qua nước tiểu có đúng không?",
          f"{R('Sai')}: tăng gánh lọc cầu thận và protein niệu; chỉ cần {G('đạm như trẻ khỏe cùng tuổi')}.",
          "Kiêng đạm cũng sai vì gây suy dinh dưỡng. IPNA 2023 khuyến cáo khẩu phần đạm như trẻ khỏe.",
          [IPNA23, BAI], ["Bay"]),
    basic(86, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Kết luận {R('kháng steroid')} khi mới tấn công {Y('2 tuần')} dẫn đến sai lầm gì?",
          f"{R('Đổi sớm sang thuốc ức chế miễn dịch bậc hai')} trong khi trẻ có thể {G('đáp ứng ở tuần 3–4')}.",
          "SRNS cần đủ 4 tuần liều chuẩn; trẻ đáp ứng một phần còn có giai đoạn xác nhận đến tuần 6.",
          [IPNA20, IPNA23], ["Bay"]),
    basic(87, "E10", "Bẫy lâm sàng", 2,
          f"{B('[Bẫy lâm sàng]')} Tiêm {R('vắc xin sống')} (thủy đậu, sởi) khi trẻ đang uống prednisolone liều cao gây hậu quả gì?",
          f"{R('Nhiễm virus vắc xin lan tỏa')}: viêm não, viêm phổi nặng, tử vong.",
          "Hoãn vắc xin sống đến ít nhất 1–3 tháng sau ngừng corticoid liều cao và 6 tháng sau rituximab.",
          [IPNA23, BAI], ["Bay"]),

    # ================================================================ E11. Tính toán & ca lâm sàng
    cloze(88, "E11", "Tính toán lâm sàng",
          f"Bé trai 3 tuổi, 15 kg: prednisolone tấn công 2 mg/kg/ngày × 15 kg = {cz(Y('30 mg/ngày'))}, tức {cz(Y('6 viên 5 mg'), 2)} uống 1 lần buổi sáng.",
          [IPNA23], ["Tinh-lieu"]),
    cloze(89, "E11", "Tính toán lâm sàng",
          f"Bé gái 6 tuổi thừa cân, diện tích da 0,95 m²: prednisolone 60 mg/m² × 0,95 = {cz(Y('57 mg/ngày'))} (không vượt {cz(Y('60 mg/ngày'), 2)}).",
          [IPNA23], ["Tinh-lieu"]),
    cloze(90, "E11", "Tính toán lâm sàng",
          f"Trẻ 14 kg khô, giảm thể tích chưa tụt huyết áp: Albumin 20% 1 g/kg = 14 g = {cz(Y('70 mL'))} truyền trong {cz(Y('4–6 giờ'), 2)}; nếu đã bù đủ mà vẫn tiểu ít thì Furosemid {cz(Y('14 mg (1 mg/kg) tĩnh mạch'), 3)}.",
          [IPNA23], ["Tinh-lieu", "Albumin"]),
    cloze(91, "E11", "Tính toán lâm sàng",
          f"Protein niệu 450 mg/dL, creatinin niệu 90 mg/dL: Up/Ucr = 450 / 90 = {cz(Y('5,0 mg/mg'))}. Kết quả này {cz(R('đạt ngưỡng thận hư (≥ 2 mg/mg)'), 2)}.",
          [IPNA23], ["Tinh-lieu", "Protein-nieu"]),
    cloze(92, "E11", "Tính toán lâm sàng",
          f"Dữ kiện: canxi toàn phần 1,65 mmol/L; albumin 12 g/L; công thức 1,65 + 0,02 × (40 − 12). Canxi hiệu chỉnh = {cz(Y('2,21 mmol/L'))}. Kết luận là {cz(G('hạ canxi giả tạo nên không tiêm canxi tĩnh mạch'), 2)}.",
          [BAI], ["Tinh-lieu", "Canxi"]),
    basic(93, "E11", "Tình huống lâm sàng", 2,
          f"{B('[Case 1]')} Trẻ 4 tuổi {R('phù to toàn thân')} nhưng {R('mạch 145 l/ph, HA 75/50 mmHg, CRT 4 giây, đau bụng quanh rốn')} — giải thích?",
          f"{R('Giảm thể tích tuần hoàn mất bù (Underfill)')}: albumin {Y('14 g/L')} làm dịch thoát ra mô kẽ (phù) trong khi {R('lòng mạch cạn dịch')}.",
          "Thiếu dịch nội mạch gây co mạch ngoại vi (CRT kéo dài, chi lạnh), tụt huyết áp và thiếu máu mạc treo gây đau bụng.",
          [IPNA23, BAI], ["Ca-lam-sang"]),
    basic(94, "E11", "Tình huống lâm sàng", 2,
          f"{B('[Case 1]')} Vì sao tiêm {R('Furosemid 20 mg tĩnh mạch đơn độc')} cho trẻ Case 1 là sai lầm nguy hiểm?",
          f"Cưỡng bức bài niệu khi {R('lòng mạch đang cạn')} → {R('trụy mạch, huyết khối, tổn thương thận cấp')}.",
          "IPNA 2023: khi có dấu hiệu giảm thể tích phải ngừng lợi tiểu; trẻ đang tụt huyết áp cần albumin 4–5%, không kèm Furosemid.",
          [IPNA23], ["Ca-lam-sang"]),
    basic(95, "E11", "Tình huống lâm sàng", 1,
          f"{B('[Case 1]')} Tóm tắt các bước {G('cấp cứu huyết động')} cho trẻ đang {R('tụt huyết áp 75/50 mmHg')}.",
          f"1) {G('Thở oxy, lập đường truyền')}.<br>"
          f"2) Chống sốc: {G('Albumin 4–5%')}, {R('không kèm Furosemid')} (chưa có: NaCl 0,9% {Y('10 mL/kg')} trong 30 phút).<br>"
          f"3) Hết tụt huyết áp mà còn giảm thể tích: {G('Albumin 20% 1 g/kg (70 mL) trong 4–6 giờ')}.<br>"
          f"4) Chỉ khi đã bù đủ mà vẫn tiểu ít: {G('Furosemid 1 mg/kg tĩnh mạch')} giữa/cuối truyền; theo dõi sinh hiệu, nước tiểu mỗi 30 phút.",
          "Không tiêm canxi tĩnh mạch vì canxi ion hóa 1,18 mmol/L bình thường. Bắt đầu prednisolone sau khi huyết động ổn và đã loại trừ nhiễm trùng.",
          [IPNA23, BAI], ["Ca-lam-sang"]),
    basic(96, "E11", "Tình huống lâm sàng", 2,
          f"{B('[Case 2]')} Trẻ 6 tuổi HCTH, {R('sốt 39,2°C, đau bụng cấp, đề kháng nhẹ')}: chẩn đoán ưu tiên và vi khuẩn hàng đầu?",
          f"1) Chẩn đoán: {R('viêm phúc mạc tiên phát')} trên nền HCTH tái phát.<br>2) Vi khuẩn: {R('phế cầu (Streptococcus pneumoniae)')}, {Y('> 50%')}.",
          "Bạch cầu 21.500/µL và CRP 96 mg/L củng cố nhiễm khuẩn cấp; cấy máu và dịch màng bụng trước kháng sinh.",
          [BAI], ["Ca-lam-sang"], asks=["Chẩn đoán", "Vi khuẩn"]),
    basic(97, "E11", "Tình huống lâm sàng", 2,
          f"{B('[Case 2]')} Trẻ Case 2 có chỉ định {R('mổ bụng thăm dò')} không? Tại sao?",
          f"{G('Không')}: viêm phúc mạc tiên phát {G('điều trị nội khoa bằng kháng sinh')}; mổ không cần thiết làm tăng nguy cơ nhiễm trùng và sốc.",
          "Siêu âm đã loại trừ viêm ruột thừa và không có liềm hơi dưới hoành; chọc dịch báng để cấy vi sinh.",
          [BAI], ["Ca-lam-sang"]),
    basic(98, "E11", "Tình huống lâm sàng", 2,
          f"{B('[Case 2]')} Kế hoạch {G('kháng sinh')} và {G('quản lý corticoid')} cho trẻ Case 2?",
          f"1) Kháng sinh: {G('Ceftriaxone 80–100 mg/kg/ngày tĩnh mạch')}.<br>"
          f"2) Corticoid: {R('không ngừng đột ngột')} — nguy cơ suy thượng thận khi stress nhiễm trùng nặng.",
          "Khi đang nhiễm trùng nặng, trục thượng thận bị ức chế không đáp ứng đủ với stress; duy trì corticoid và theo dõi huyết động.",
          [IPNA23, BAI], ["Ca-lam-sang"], asks=["Kháng sinh", "Corticoid"]),
]
