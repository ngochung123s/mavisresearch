# -*- coding: utf-8 -*-
"""ped21_cards_data.py - Master deck PED-21: Viêm phổi mắc phải cộng đồng (CAP) ở trẻ em.
Basic-first; cloze chỉ là thẻ nhắc phụ (giữ legacy_note_id)."""


def r(x):
    return f'<span style="color:#ff6b6b"><b>{x}</b></span>'


def y(x):
    return f'<span style="color:#ffd43b"><b>{x}</b></span>'


def g(x):
    return f'<span style="color:#51cf66"><b>{x}</b></span>'


def c(x):
    return f'<span style="color:#74c0fc"><b>{x}</b></span>'


ALGO = {"badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH", "badge_class": "badge-algo"}
EBM = {"badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG", "badge_class": "badge-ebm"}

_cards = []


def B(cid, sec, tier, cat, front, items, why, extra, algo=False):
    back = "<b>🎯 Trả lời cốt lõi:</b><br>" + "<br>".join(f"{i + 1}) {t}" for i, t in enumerate(items))
    back += "<br><br><b>💡 Giải thích của AI:</b><br>" + why
    d = {"id": cid, "type": "basic", "track": "ebm", "section": sec, "category": cat, "tier": tier}
    d.update(ALGO if algo else EBM)
    d.update({"front": front, "back": back, "extra": "📖 Nguồn: PED-21 — " + extra,
              "tags": ["PED-21", sec, "ALGO" if algo else "EBM"]})
    _cards.append(d)


# ───────────────────────── B0: Tổng quan & nền tảng ─────────────────────────
B("PED21-B0-01", "B0", 1, "Tổng quan",
  f"Với {c('CAP ở trẻ em')}: nêu {y('3 ý khung tổng quan')} của bài (tầm quan trọng/dịch tễ, {r('2 sai lầm đối lập')} ở cấp cứu, và bài học cung cấp những năng lực nào)?",
  [f"{c('CAP')} là một trong những nguyên nhân hàng đầu gây khám bệnh, nhập viện và tử vong ở trẻ {y('dưới 5 tuổi')} toàn cầu; tình huống sốt + ho + khó thở là phổ biến nhất ở cấp cứu/phòng khám Nhi.",
   f"Hai sai lầm đối lập: {r('báo động giả/lạm dụng')} (kháng sinh phổ rộng, X-quang thường quy) và {r('bỏ sót suy sụp/trì hoãn cấp cứu')}.",
   f"Khung năng lực: sinh lý bệnh → phân tầng nặng theo {c('WHO, PIDS/IDSA, BTS')} → {g('phác đồ dùng thuốc từng mg theo cân nặng')}."],
  "Nhớ bài theo hai đầu cân: một đầu là làm quá (thuốc/phim không cần), một đầu là làm thiếu (đếm sai nhịp thở, liều thấp) — cả hai đều hại trẻ.",
  "Phần 0 Tổng quan")
B("PED21-B0-02", "B0", 2, "Tổng quan",
  f"Hai sai lầm đối lập trong tiếp cận trẻ sốt + ho + khó thở: mỗi sai lầm gồm {r('những hành vi cụ thể nào')} và {r('hậu quả')} gì?",
  [f"{r('Báo động giả & lạm dụng')}: kê {c('Cephalosporin thế hệ 3 uống, Co-amoxiclav')} hoặc chụp {c('X-quang phổi thẳng thường quy')} cho nhiễm virus hô hấp không biến chứng → quá tải chi phí, phơi nhiễm bức xạ, thúc đẩy kháng thuốc.",
   f"{r('Bỏ sót suy sụp & trì hoãn cấp cứu')}: không đếm trọn {y('60 giây')} khi trẻ nằm yên; bỏ qua rút lõm tinh tế ở nhũ nhi; dùng Amoxicillin {y('40–50')} thay vì {y('80–90 mg/kg/ngày')}.",
   f"Hậu quả của sai lầm thứ hai: thất bại với phế cầu kháng trung gian → {r('tràn mủ màng phổi, viêm phổi hoại tử, suy hô hấp cấp')}."],
  "Liều dưới chuẩn không chỉ 'kém hiệu quả' mà còn đẩy bác sĩ vào vòng xoáy đổi thuốc sai, làm bệnh tiến triển thành biến chứng.",
  "Phần 0 Tổng quan")
B("PED21-B0-03", "B0", 2, "Thuật ngữ nền tảng",
  f"Định nghĩa 4 khái niệm nền: {c('CAP')}, {r('thở nhanh')} (kèm 3 mốc WHO), {r('rút lõm lồng ngực')}, {r('thở rên')}?",
  [f"{c('CAP')}: nhiễm trùng cấp tính nhu mô phổi ở trẻ {y('không nằm viện trong 14 ngày trước đó')}.",
   f"{r('Thở nhanh')}: dấu hiệu khách quan, nhạy nhất, phản ánh giảm độ giãn nở phổi; WHO: {y('&lt; 2 tháng ≥ 60')}, {y('2–11 tháng ≥ 50')}, {y('1–5 tuổi ≥ 40')} lần/phút.",
   f"{r('Rút lõm lồng ngực')}: phần dưới lồng ngực (bờ sườn, mũi ức) lõm vào ở {y('thì hít vào')}; do lồng ngực nhũ nhi mềm, xương sườn nằm ngang + áp lực âm màng phổi tăng khi phổi đông đặc, kém đàn hồi.",
   f"{r('Thở rên')}: tiếng ngắn, trầm ở {y('thì thở ra')} khi thanh môn khép một phần → tạo {g('PEEP sinh lý')} giữ phế nang viêm không xẹp."],
  "Thở rên là phản xạ tự bảo vệ, không phải triệu chứng 'nhẹ': trẻ đang tự tạo PEEP vì phế nang sắp xẹp.",
  "Phần 0.1 Nền tảng tối thiểu")
B("PED21-B0-04", "B0", 2, "Thuật ngữ nền tảng",
  f"Định nghĩa {c('shunt trong phổi')}, {c('MIC')} (và nguyên lý diệt khuẩn của Beta-lactam), và {r('trần liều người lớn')} kèm 2 ví dụ?",
  [f"{c('Shunt trong phổi')}: máu tĩnh mạch tim phải đi qua phế nang đông đặc chứa dịch viêm, không trao đổi oxy, trở về tim trái → máu thiếu oxy ({y('VA/Q → 0')}).",
   f"{c('MIC')}: nồng độ ức chế tối thiểu của kháng sinh với vi khuẩn; Beta-lactam (Amoxicillin) diệt khuẩn phụ thuộc {y('thời gian nồng độ thuốc tự do trên MIC (T > MIC)')}.",
   f"{r('Trần liều người lớn')}: liều tối đa mg/ngày không được vượt qua dù nhân theo cân nặng (kể cả trẻ béo phì). Ví dụ: {g('Ceftriaxone tối đa 2 g/ngày')}; {g('Amoxicillin tối đa 2–3 g/ngày')}."],
  "Ba khái niệm này là 'bản lề' của cả bài: shunt giải thích hạ oxy trơ, T > MIC giải thích liều cao Amoxicillin, trần liều giải thích bẫy kê đơn theo mg/kg.",
  "Phần 0.1 Nền tảng tối thiểu")
B("PED21-B0-05", "B0", 2, "Cờ đỏ cấp cứu",
  f"Liệt kê {y('7 dấu hiệu')} của {r('BOX ĐỎ báo động cấp cứu')} khi tiếp nhận trẻ nghi viêm phổi và {g('hành động cần làm ngay')} nếu có BẤT KỲ MỘT dấu hiệu?",
  [f"{r('Không uống được / bỏ bú hoàn toàn')}.", f"{r('Nôn tất cả mọi thứ')} sau ăn/uống.", f"{r('Co giật')} hoặc trạng thái sau co giật.",
   f"{r('Li bì, lơ mơ, hôn mê')} khó đánh thức.", f"{r('Thở rên liên tục')} khi nằm yên.",
   f"{r('Tím tái trung ương')} (môi, lưỡi, niêm mạc miệng) hoặc {y('SpO2 &lt; 90%')} khí phòng.", f"{r('Rút lõm lồng ngực rất nặng')} kèm phập phồng cánh mũi, đầu gật gù theo nhịp thở.",
   f"{g('Hành động')}: DỪNG thăm khám thông thường, kích hoạt cấp cứu, cho {g('thở oxy')}, {g('lập đường truyền tĩnh mạch')}, chuyển phòng hồi sức."],
  "Chỉ cần MỘT dấu hiệu là đủ: các dấu hiệu này đều phản ánh kiệt sức hô hấp, thiếu oxy não hoặc nhiễm khuẩn huyết.",
  "Phần 0.1 Box đỏ")

# ───────────────────────── B1: Định nghĩa & phân loại ─────────────────────────
B("PED21-B1-01", "B1", 1, "Phân loại",
  f"Khung phân loại CAP gồm {y('3 nhánh')}: tiêu chuẩn {c('WHO')}, tiêu chuẩn {c('PIDS/IDSA & BTS')}, và {c('căn nguyên theo nhóm tuổi')} — mỗi nhánh gồm những gì (tóm tắt)?",
  [f"{c('WHO')}: 3 nhóm — {c('không phải viêm phổi')} (không thở nhanh, không rút lõm), {c('viêm phổi')} (ngoại trú), {c('viêm phổi nặng')} (nhập viện).",
   f"{c('PIDS/IDSA & BTS')}: {c('nhẹ–trung bình')} vs {r('nặng')} (≥ 1 trong 6 tiêu chí; SpO2 &lt; 92% theo BTS, &lt; 90% theo WHO).",
   f"{c('Căn nguyên')}: 4 nhóm tuổi — sơ sinh, 1–3 tháng, 3 tháng–5 tuổi, &gt; 5 tuổi."],
  "WHO tối ưu độ nhạy cho tuyến ban đầu (không cần X-quang/xét nghiệm); PIDS/IDSA và BTS chi tiết hơn nhờ khám thực thể và SpO2.",
  "Phần 1 Định nghĩa và phân loại")
B("PED21-B1-02", "B1", 2, "Phân loại WHO",
  f"Theo {c('WHO (2014) và Pocket Book')}: định nghĩa {c('Viêm phổi')}, {r('Viêm phổi nặng')}, trường hợp {g('không phải viêm phổi')} — tiêu chí và nơi điều trị mỗi nhóm; WHO đã làm gì với nhóm 'viêm phổi rất nặng'?",
  [f"{c('Viêm phổi')}: ho/khó thở + {y('thở nhanh theo tuổi')} và/hoặc {r('rút lõm lồng ngực')}, KHÔNG có dấu hiệu nguy hiểm toàn thân → {g('điều trị ngoại trú Amoxicillin uống liều cao')}.",
   f"{r('Viêm phổi nặng')}: ho/khó thở + BẤT KỲ MỘT dấu hiệu nguy hiểm toàn thân, HOẶC thở rên, HOẶC tím tái, HOẶC {y('SpO2 &lt; 90%')} → {g('nhập viện, kháng sinh đường tiêm, hỗ trợ hô hấp')}.",
   f"{c('Không phải viêm phổi')}: không thở nhanh, không rút lõm (nhiễm khuẩn hô hấp trên) → chăm sóc tại nhà, hạ sốt, dặn dấu hiệu tái khám.",
   f"WHO đã {y('gộp')} nhóm 'viêm phổi rất nặng' vào {r('viêm phổi nặng')} để đơn giản hóa quyết định nhập viện."],
  "Lưu đồ WHO: đếm nhịp thở 60 giây + quan sát cơ học thở → có thở nhanh? → rút lõm? → có dấu hiệu nguy hiểm? Dấu hiệu nguy hiểm là 'công tắc' chuyển từ ngoại trú sang nhập viện.",
  "Phần 1.1 Định nghĩa WHO")
B("PED21-B1-03", "B1", 2, "Phân loại PIDS/BTS",
  f"Theo {c('PIDS/IDSA & BTS')}: {c('viêm phổi nhẹ đến trung bình')} được mô tả bằng {y('những đặc điểm nào')} (sốt, nhịp thở, co kéo, nghe phổi, SpO2, uống, tri giác)?",
  [f"Sốt nhẹ hoặc vừa; {r('thở nhanh')}; co kéo cơ hô hấp {y('nhẹ')}.", f"Nghe phổi: {r('ran ẩm')} hoặc giảm âm phế nang cục bộ.",
   f"{y('SpO2 ≥ 92%')} khi thở khí phòng.", "Trẻ còn uống được nước; tri giác tỉnh táo."],
  "Đây là nhóm có thể ngoại trú: điểm then chốt là SpO2 ≥ 92%, uống được, tỉnh táo.",
  "Phần 1.2 Phân loại PIDS/IDSA và BTS")
B("PED21-B1-04", "B1", 2, "Phân loại PIDS/BTS",
  f"Liệt kê {y('6 tiêu chí')} của {r('viêm phổi nặng')} theo PIDS/IDSA & BTS (cần ít nhất 1), gồm cả {y('ngưỡng SpO2 và nhịp thở rất nhanh')}?",
  [f"{r('Thở co kéo lồng ngực rõ, phập phồng cánh mũi, đầu gật gù')} theo nhịp thở.",
   f"{y('SpO2 &lt; 92% (BTS)')} hoặc {y('&lt; 90% (WHO)')} khi thở khí phòng.",
   f"{y('Nhịp thở rất nhanh')}: trẻ {y('&lt; 1 tuổi &gt; 70 lần/phút')}; trẻ {y('&gt; 1 tuổi &gt; 50 lần/phút')}.",
   f"{r('Nhịp tim nhanh không tương xứng thân nhiệt')} (cảnh báo sốc nhiễm khuẩn).",
   f"{r('Mất nước, li bì, bỏ bú')} hoặc nôn nhiều không uống được thuốc.",
   f"{r('Tràn dịch màng phổi')} hoặc tổn thương nhiều thùy phổi trên X-quang."],
  "Hai ngưỡng SpO2 khác nhau (92% BTS, 90% WHO) — khi đọc bài/đề phải xem hệ quy chiếu; nhịp tim nhanh quá mức so với sốt là gợi ý sớm của sốc nhiễm khuẩn.",
  "Phần 1.2 Phân loại PIDS/IDSA và BTS")
B("PED21-B1-05", "B1", 2, "Căn nguyên",
  f"Căn nguyên CAP ở {c('sơ sinh (&lt; 1 tháng)')} và {c('nhũ nhi 1–3 tháng')}: {c('tác nhân thường gặp')} và {r('đặc điểm lâm sàng gợi ý')}?",
  [f"{c('Sơ sinh')}: {c('Liên cầu nhóm B (S. agalactiae), E. coli, Listeria monocytogenes, Klebsiella')}; lâm sàng mơ hồ — {r('hạ thân nhiệt, bỏ bú, thở rên, cơn ngừng thở')}; thường lây từ mẹ lúc sinh.",
   f"{c('1–3 tháng')}: {c('Chlamydia trachomatis, RSV, virus cúm, S. pneumoniae, Bordetella pertussis')}.",
   f"{c('C. trachomatis')}: viêm phổi bán cấp {y('không sốt')}, {r('ho cơn dồn dập')}, tiền sử viêm kết mạc sơ sinh, tăng bạch cầu ái toan."],
  "Nhóm tuổi quyết định tác nhân: sơ sinh nhiễm từ đường sinh dục mẹ; 1–3 tháng có bộ ba gợi ý Chlamydia (không sốt + ho cơn + viêm kết mạc cũ).",
  "Phần 1.3 Căn nguyên vi sinh theo nhóm tuổi")
B("PED21-B1-06", "B1", 2, "Căn nguyên",
  f"Căn nguyên CAP ở trẻ {c('3 tháng–5 tuổi')} và trẻ {c('&gt; 5 tuổi')}: {c('tác nhân')} và {r('manh mối lâm sàng phân biệt vi khuẩn vs virus / không điển hình')}?",
  [f"{c('3 tháng–5 tuổi')}: {y('virus 60–80%')} (RSV, Adenovirus, Cúm, Á cúm, Metapneumovirus); vi khuẩn: {c('S. pneumoniae (hàng đầu), H. influenzae không định type, S. aureus')}.",
   f"{r('Gợi ý vi khuẩn')}: sốt đột ngột, cao, rét run, thở nhanh, đau ngực, ran ẩm khu trú. {r('Gợi ý virus')}: khởi đầu viêm long hô hấp, khò khè lan tỏa.",
   f"{c('&gt; 5 tuổi')}: không điển hình {c('Mycoplasma pneumoniae, Chlamydia pneumoniae')}; điển hình {c('S. pneumoniae')}.",
   f"{r('Gợi ý không điển hình')}: khởi phát từ từ, sốt nhẹ–vừa, đau đầu, viêm họng, đau cơ, ho khan dữ dội dai dẳng, ran rải rác phong phú hơn nhiều so với lâm sàng nghèo nàn."],
  "Tương phản 'ồn ào ở phổi, nghèo ở tổng trạng' là chữ ký của Mycoplasma ở trẻ lớn; ngược lại sốt cao đột ngột + ran khu trú là chữ ký của phế cầu.",
  "Phần 1.3 Căn nguyên vi sinh theo nhóm tuổi")

# ───────────────────────── B2: Sinh lý bệnh ─────────────────────────
B("PED21-B2-01", "B2", 1, "Sinh lý bệnh",
  f"Bài có {y('4 chuỗi nhân quả')} sinh lý bệnh: mỗi chuỗi đi từ cơ chế nào đến {r('hậu quả/quyết định lâm sàng')} nào?",
  [f"Chuỗi 1: xuất tiết phế nang → giảm độ giãn nở → {r('rút lõm lồng ngực')}.",
   f"Chuỗi 2: đông đặc phế nang → {c('shunt VA/Q = 0')} → {r('hạ oxy máu trơ')} → nâng bậc {g('HFNC/CPAP')}.",
   f"Chuỗi 3: ổ nhiễm khuẩn dưới màng phổi → {c('tràn mủ màng phổi')} → {g('siêu âm + dẫn lưu sớm')}.",
   f"Chuỗi 4: đột biến {c('PBP')} → MIC tăng → cần {g('Amoxicillin liều cao 80–90 mg/kg/ngày')}."],
  "Mỗi chuỗi kết thúc bằng một quyết định giường bệnh: thở oxy/phân độ nặng, nâng bậc thông khí, dẫn lưu mủ, nâng liều kháng sinh.",
  "Phần 2 Cơ chế sinh lý bệnh")
B("PED21-B2-02", "B2", 2, "Sinh lý bệnh",
  f"{c('Chuỗi 1')} (rút lõm lồng ngực): cơ chế qua các tầng — {c('tế bào')}, {c('cơ học')}, {r('lâm sàng')}, quyết định, và {r('hậu quả nếu làm sai')}?",
  [f"Phế cầu/vi khuẩn xâm nhập phế nang; {c('Pneumolysin + PAMPs')} kích hoạt đại thực bào tiết {c('IL-1, TNF-alpha, IL-8')}; bạch cầu đa nhân vào phế nang, tạo dịch rỉ viêm giàu protein và fibrin.",
   f"Dịch rỉ làm {r('mất hoạt tính Surfactant')} → sức căng bề mặt tăng → giảm độ giãn nở (C = ΔV/ΔP) → phổi cứng, cần áp lực âm lớn hơn.",
   f"Để giữ thông khí phút (VE = RR × VT) cơ thể {y('tăng tần số thở')}; cơ hoành + cơ hô hấp phụ (liên sườn, ức đòn chũm) co tối đa.",
   f"Khung sụn mềm của trẻ nhỏ bị kéo thụt → {r('rút lõm lồng ngực')} → nhận diện tăng công thở, {g('cho thở oxy và phân độ viêm phổi nặng')}.",
   f"Nếu xem nhẹ: cơ hoành kiệt sức → ngừng co kéo → {r('ứ CO2, toan hô hấp mất bù, ngừng thở đột ngột')}."],
  "Thở nhanh là phản xạ bù ít tốn năng lượng nhất; rút lõm là bằng chứng của tăng công thở; khi lồng ngực 'yên lại' vì kiệt sức thì nguy hiểm nhất.",
  "Phần 2 Chuỗi 1")
B("PED21-B2-03", "B2", 2, "Sinh lý bệnh",
  f"{c('Chuỗi 2')} (shunt trong phổi): cơ chế từ phế nang đến khí máu, vai trò của {c('HPV')}, và {g('vì sao cần nâng bậc áp lực dương')}?",
  [f"Phế nang chứa mủ/tế bào hoại tử, mất thông khí nhưng mao mạch vẫn được tưới → {c('VA/Q = 0')}: máu tĩnh mạch không nhận O2 và không thải CO2.",
   f"Máu chưa oxy hóa trộn vào máu động mạch → {c('shunt phải–trái trong phổi')}; {c('HPV (co mạch phổi do thiếu oxy)')} tái phân phối máu sang vùng lành nhưng {r('quá tải khi tổn thương rộng')} → {y('SpO2 tụt dưới 90%')}.",
   f"Shunt lớn không đáp ứng canula oxy thường → cần {g('HFNC hoặc nCPAP')} để mở phế nang xẹp lân cận + tăng FiO2.",
   f"Nếu chỉ duy trì canula liều thấp: {r('thiếu oxy mô, toan lactic, suy tim sung huyết, tổn thương não không hồi phục')}."],
  "Khác bất tương xứng V/Q thông thường (đáp ứng oxy nhanh), shunt thật sự cần tăng áp lực đường thở — oxy đơn thuần không 'đến được' phế nang đông đặc.",
  "Phần 2 Chuỗi 2")
B("PED21-B2-04", "B2", 2, "Sinh lý bệnh",
  f"{c('Chuỗi 3')} (tràn mủ màng phổi): {c('vi sinh/serotype')}, {c('3 giai đoạn')}, biểu hiện {r('lâm sàng')}, quyết định {g('xử trí')} và hậu quả nếu {r('trì hoãn')}?",
  [f"Phế cầu ({y('serotype 1, 3, 19A')}) hoặc {c('S. aureus')} gây hoại tử nhu mô sát màng phổi tạng.",
   f"{c('Giai đoạn 1')} xuất tiết (dịch thanh tơ vô khuẩn); {c('giai đoạn 2')} mủ sợi huyết (vi khuẩn xâm nhập, mủ đặc, fibrin tạo {y('vách ngăn/loculations')}); {c('giai đoạn 3')} hóa sợi, vỏ bọc (Peel).",
   f"Lâm sàng: {r('sốt cao liên tục dù kháng sinh 48–72 giờ, thở nông nhanh, đau ngực kiểu màng phổi, hội chứng ba giảm')} (gõ đục, rung thanh giảm, mất rì rào); xẹp phổi thụ động, đẩy lệch trung thất.",
   f"Xử trí: {g('siêu âm màng phổi')} (tiêu chuẩn vàng thấy vách fibrin) + X-quang; {g('chọc hút')} làm xét nghiệm (tế bào, protein, LDH, pH, Gram, cấy); {g('ống dẫn lưu + tiêu sợi huyết (Alteplase/Urokinase) hoặc VATS')}.",
   f"Nếu chỉ đổi kháng sinh: sang giai đoạn 3 → {r('vỏ xơ, phổi bị giam (trapped lung), lồng ngực co rút, phải mổ mở bóc vỏ')}."],
  "Mủ có vách fibrin thì kháng sinh khó thấm; thời gian là yếu tố quyết định giữa dẫn lưu đơn giản và đại phẫu bóc vỏ.",
  "Phần 2 Chuỗi 3")
B("PED21-B2-05", "B2", 2, "Sinh lý bệnh",
  f"{c('Chuỗi 4')}: phế cầu kháng Beta-lactam bằng {c('cơ chế nào')}, MIC thay đổi ra sao, vì sao {g('Amoxicillin 80–90 mg/kg/ngày')} cứu được, và {r('hậu quả của liều 40–50')}?",
  [f"Không sinh Beta-lactamase mà {c('tái tổ hợp tương đồng làm biến đổi PBP1a, PBP2b, PBP2x')} → ái lực với Penicillin/Amoxicillin giảm.",
   f"MIC tăng từ {y('≤ 0.06 µg/mL')} (nhạy) lên {y('2–4 µg/mL')} (kháng trung gian/cao).",
   f"PK/PD: Amoxicillin diệt khuẩn phụ thuộc thời gian, cần {y('T > MIC ≥ 40–50% khoảng giữa các liều')}; liều 40–50 mg/kg/ngày chỉ đạt đỉnh {y('4–5 µg/mL')}, tụt dưới MIC sau {y('2–3 giờ')}.",
   f"{g('Nâng gấp đôi lên 80–90 mg/kg/ngày')} (chia 2–3 lần): đỉnh {y('8–10 µg/mL')}, duy trì T > MIC trên 50% khoảng liều, không cần kháng sinh đắt/phổ rộng.",
   f"Liều thấp → {r('sốt kéo dài, tổn thương lan sau 48 giờ')}, bác sĩ lầm tưởng kháng Amoxicillin và đổi sang {c('Cefixime')} (ái lực PBP phế cầu kém hơn) → thất bại nặng hơn."],
  "Đề kháng ở đây là 'giảm ái lực' chứ không phải 'phá thuốc', nên bù bằng nồng độ cao hơn là giải pháp hợp lý.",
  "Phần 2 Chuỗi 4")

# ───────────────────────── B3: Chẩn đoán ─────────────────────────
B("PED21-B3-01", "B3", 1, "Chẩn đoán",
  f"Tiếp cận chẩn đoán CAP tại giường gồm {y('3 khối')}: quy trình {c('đếm nhịp thở')}, {c('khám thực thể lồng ngực')} và {c('chỉ định X-quang phổi thẳng')} — mỗi khối gồm gì (tóm tắt)?",
  [f"{c('Đếm nhịp thở')}: 4 bước (nằm yên, bộc lộ ngực bụng, đếm trọn {y('60 giây')}, đối chiếu ngưỡng WHO theo tuổi).",
   f"{c('Khám thực thể')}: cánh mũi, các mức co kéo, đầu gật gù, nghe ran ẩm nhỏ hạt/tiếng thổi ống/giảm rì rào.",
   f"{c('X-quang')}: {r('không thường quy')} ở viêm phổi nhẹ ngoại trú; {g('chỉ định bắt buộc')} cho 5 nhóm tình huống."],
  "Chẩn đoán CAP nhẹ là chẩn đoán lâm sàng; phim chỉ dành cho ca nặng, nghi biến chứng hoặc thất bại điều trị.",
  "Phần 3 Tiếp cận chẩn đoán")
B("PED21-B3-02", "B3", 2, "Chẩn đoán",
  f"{c('Quy trình đếm nhịp thở 4 bước')}: mỗi bước làm gì, {y('điều kiện hạ sốt cụ thể')} (ngưỡng nhiệt độ, thuốc, liều, thời gian chờ) và {r('điều tuyệt đối không được làm')} vì sao?",
  [f"{y('Bước 1')} trẻ {y('nằm yên')}: không đếm khi khóc, quấy, vừa bú no, sốt cao co giật. Nếu sốt {y('≥ 38.5 °C')} → cho {g('Paracetamol 10–15 mg/kg')}, đợi {y('30–45 phút')} rồi đếm.",
   f"{y('Bước 2')} bộc lộ ngực và bụng: trẻ nhỏ thở bụng (cơ hoành) nên nhìn thành bụng dễ nhất.",
   f"{y('Bước 3')} đếm trọn {y('60 giây')} bằng đồng hồ/bộ đếm; {r('KHÔNG đếm 15 giây × 4 hoặc 30 giây × 2')}.",
   f"{y('Bước 4')} đối chiếu ngưỡng WHO theo tuổi."],
  "Nhũ nhi có thở ngắt quãng sinh lý (periodic breathing): nhân nhẩm khuếch đại sai số lên gấp bội và dẫn tới chẩn đoán sai.",
  "Phần 3.1 Quy trình đếm nhịp thở")
B("PED21-B3-03", "B3", 2, "Chẩn đoán",
  f"Bảng {y('ngưỡng thở nhanh WHO')} theo {y('4 nhóm tuổi')} và {c('ý nghĩa lâm sàng')} của từng nhóm?",
  [f"{y('Dưới 2 tháng: ≥ 60 lần/phút')} → luôn coi là {r('bệnh rất nặng, nguy cơ nhiễm khuẩn huyết cao, chuyển viện ngay')}.",
   f"{y('2–11 tháng: ≥ 50')} → tiêu chuẩn vàng sàng lọc viêm phổi tại tuyến ban đầu.",
   f"{y('12–59 tháng (1–5 tuổi): ≥ 40')} → tiêu chuẩn vàng sàng lọc viêm phổi tại tuyến ban đầu.",
   f"{y('Từ 5 tuổi trở lên: ≥ 30')} → theo dõi sát, kết hợp nghe phổi và tổng trạng."],
  "Ngưỡng giảm dần theo tuổi vì nhịp thở sinh lý giảm dần: 60 → 50 → 40 → 30.",
  "Phần 3.1 Bảng ngưỡng thở nhanh")
B("PED21-B3-04", "B3", 2, "Chẩn đoán",
  f"Bảng kiểm khám {c('thở co kéo')}: {y('4 mức/dấu hiệu')} từ nhẹ đến nặng (kèm {c('phập phồng cánh mũi')}) — mỗi dấu hiệu nghĩa là gì?",
  [f"{c('Phập phồng cánh mũi')}: cánh mũi nở thì hít vào, giảm sức cản đường thở trên ở trẻ nhỏ.",
   f"{y('Co kéo liên sườn nhẹ')}.", f"{r('Rút lõm dưới sườn/bờ sườn')} — tiêu chuẩn của WHO.",
   f"{r('Rút lõm hõm ức + co kéo cơ ức đòn chũm')} — dấu hiệu tắc nghẽn hoặc suy hô hấp nặng.",
   f"{r('Đầu gật gù (Head bobbing)')}: đầu ngửa thì hít vào, gục thì thở ra — cơ ức đòn chũm co tối đa hỗ trợ cơ hoành đã kiệt sức."],
  "Vị trí co kéo càng cao (hõm ức, ức đòn chũm) thì cơ hô hấp phụ huy động càng nhiều → mức độ nặng càng cao.",
  "Phần 3.2 Bảng kiểm thăm khám thực thể")
B("PED21-B3-05", "B3", 2, "Chẩn đoán",
  f"{c('Nghe phổi')} trong CAP: {y('3 dấu hiệu')} — mô tả, {c('cơ chế')} của từng dấu hiệu?",
  [f"{r('Ran ẩm nhỏ hạt (fine crackles)')}: nghe cuối thì hít vào — phế nang bị dính mở bung đột ngột.",
   f"{r('Tiếng thổi ống (bronchial breath sounds)')}: thô ráp, nghe cả thì hít vào và thở ra — nhu mô đông đặc truyền âm từ khí quản ra thành ngực tốt hơn.",
   f"{r('Giảm rì rào phế nang khu trú')}: vùng đông đặc không thông khí hoặc bị tràn dịch màng phổi ngăn cách."],
  "Ba dấu hiệu này phản ánh ba trạng thái: phế nang đang mở ra, nhu mô đặc dẫn âm, và vùng bị 'cách ly' không thông khí.",
  "Phần 3.2 Nghe phổi")
B("PED21-B3-06", "B3", 2, "Chẩn đoán",
  f"{c('X-quang phổi thẳng')} trẻ viêm phổi: {r('khi nào KHÔNG chỉ định')} (3 điều kiện) và {g('khi nào BẮT BUỘC')} (5 nhóm tình huống)?",
  [f"{r('KHÔNG chỉ định')}: viêm phổi nhẹ điều trị ngoại trú; trẻ tỉnh táo {y('SpO2 ≥ 92%')}; đáp ứng tốt Amoxicillin uống.",
   f"{g('BẮT BUỘC')} 1: viêm phổi nặng cần nhập viện.",
   f"{g('BẮT BUỘC')} 2: nghi biến chứng — {c('tràn dịch màng phổi, áp xe phổi, tràn khí màng phổi')}.",
   f"{g('BẮT BUỘC')} 3: nghi {c('dị vật đường thở bỏ quên')}.",
   f"{g('BẮT BUỘC')} 4: sốt dai dẳng, thất bại sau {y('48–72 giờ')} kháng sinh.",
   f"{g('BẮT BUỘC')} 5: có bệnh nền — {c('tim bẩm sinh, suy giảm miễn dịch')}."],
  "Nguyên tắc: chụp khi kết quả có thể đổi quyết định điều trị; ở ca nhẹ ngoại trú phim không đổi được quyết định nào.",
  "Phần 3.3 Chỉ định X-quang phổi thẳng")
B("PED21-B3-07", "B3", 2, "Chẩn đoán",
  f"{r('Vì sao KHÔNG chụp X-quang thường quy')} cho viêm phổi nhẹ ngoại trú? Nêu {y('3 lý do')}.",
  [f"{r('Không phân biệt được vi khuẩn vs virus')}: thâm nhiễm kẽ/đông đặc không khẳng định tác nhân → dễ kê kháng sinh không cần thiết cho ca virus.",
   f"{r('Không thay đổi kết cục điều trị')}: RCT cho thấy không rút ngắn thời gian khỏi bệnh, không giảm tỷ lệ nhập viện so với chẩn đoán lâm sàng.",
   f"{r('Phơi nhiễm bức xạ ion hóa')}: trẻ nhỏ nhạy cảm với tia X; nguyên lý {c('ALARA')} (As Low As Reasonably Achievable)."],
  "Hình ảnh không đổi quyết định mà còn thêm nguy cơ (bức xạ, leo thang kháng sinh) — nên chi phí/lợi ích âm.",
  "Phần 3.3 Vì sao không chụp X-quang thường quy")
B("PED21-B3-08", "B3", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — Bộ giải mã nhanh {y('nhịp thở theo tuổi')}: ngưỡng {r('thở nhanh')} và ngưỡng {r('thở rất nhanh (nặng)')} theo PIDS/BTS?",
  [f"WHO thở nhanh: {y('&lt; 2 tháng ≥ 60')} | {y('2–11 tháng ≥ 50')} | {y('1–5 tuổi ≥ 40')} | {y('≥ 5 tuổi ≥ 30')} (lần/phút, đếm đủ 60 giây, trẻ nằm yên, đã hạ sốt).",
   f"Thở rất nhanh (tiêu chí nặng PIDS/BTS): {y('&lt; 1 tuổi &gt; 70')} | {y('&gt; 1 tuổi &gt; 50')} lần/phút.",
   f"Dưới ngưỡng và không rút lõm → {g('không phải viêm phổi')}, chăm sóc tại nhà. Đạt ngưỡng ± rút lõm, không dấu hiệu nguy hiểm → {c('viêm phổi')} ngoại trú. Có dấu hiệu nguy hiểm → {r('viêm phổi nặng')}."],
  "Học theo bậc thang 60–50–40–30 cho WHO; chữ 'rất nhanh' chỉ là ngưỡng cao hơn dùng để xếp nặng.",
  "Phần 3.1 và Phần 1.2", algo=True)

# ───────────────────────── B4: Theo dõi & biến chứng ─────────────────────────
B("PED21-B4-01", "B4", 1, "Biến chứng",
  f"Phần theo dõi sớm gồm {y('2 mảng')}: bẫy {r('cải thiện giả')} và {r('3 biến chứng')} cần nhận diện — kể tên và dấu hiệu nhận diện chính?",
  [f"{r('Cải thiện giả')}: nhịp thở giảm nhưng tri giác li bì → kiệt sức cơ hoành.",
   f"{c('Tràn mủ màng phổi')}: sốt cao &gt; 48–72 giờ kháng sinh + ba giảm.",
   f"{c('Viêm phổi hoại tử do CA-MRSA')}: tối cấp, bóng khí/hang/tràn khí màng phổi trong 24 giờ.",
   f"{c('pARDS')}: PaO2/FiO2 ≤ 300 hoặc OI ≥ 4, thâm nhiễm hai bên."],
  "Cả bốn nội dung đều là 'bệnh đang xấu đi dù có vẻ ổn' — hoặc nhịp thở trông tốt hơn, hoặc kháng sinh đúng mà vẫn sốt.",
  "Phần 4 Theo dõi và phát hiện sớm")
B("PED21-B4-02", "B4", 2, "Biến chứng",
  f"Bẫy {r('cải thiện giả')} khi cơ hoành kiệt sức: {y('diễn tiến 2 giai đoạn')} (số liệu ví dụ), {r('bản chất')} và {g('hành động cấp cứu')}?",
  [f"{y('Giai đoạn bù')}: thở ~{y('65 lần/phút')}, rút lõm rõ, quấy khóc, SpO2 {y('93–94%')} → nhận định viêm phổi nặng.",
   f"{y('Giai đoạn chuyển tiếp')}: sau {y('2–3 giờ')} nhịp thở còn {y('40 lần/phút')}, bớt rút lõm → bác sĩ thiếu kinh nghiệm tưởng 'đỡ'.",
   f"{r('Bản chất')}: cơ hoành và cơ phụ kiệt sức; nhịp thở giảm kèm {r('li bì, đáp ứng chậm, lờ đờ')} và ứ CO2 gây mê man do toan hô hấp.",
   f"{g('Hành động')}: đo ngay SpO2 + lấy khí máu, hỗ trợ bóp bóng qua mặt nạ, chuẩn bị đặt nội khí quản thở máy."],
  "Luôn đọc nhịp thở cùng tri giác và công thở: nhịp chậm lại + trẻ không tỉnh táo là dấu hiệu sắp ngừng thở, không phải bệnh thuyên giảm.",
  "Phần 4.1 Bẫy cải thiện giả")
B("PED21-B4-03", "B4", 2, "Biến chứng",
  f"{c('Tràn mủ màng phổi')} trong CAP: {r('3 dấu hiệu nghi ngờ')} và {g('phương tiện đầu tay')}?",
  [f"Sốt cao liên tục không dứt sau {y('48–72 giờ')} kháng sinh thích hợp.",
   f"{r('Thở nghiêng về bên tổn thương để giảm đau, gõ đục rõ, rung thanh giảm, mất âm phế bào')}.",
   f"{g('Siêu âm màng phổi')} là phương tiện đầu tay để phát hiện sớm dịch có vách ngăn, trước khi chụp CT lồng ngực."],
  "Siêu âm cho biết có vách ngăn hay không — thông tin quyết định cách dẫn lưu.",
  "Phần 4.2 Biến chứng — Tràn mủ màng phổi")
B("PED21-B4-04", "B4", 2, "Biến chứng",
  f"{c('Viêm phổi hoại tử do tụ cầu (CA-MRSA)')}: {r('diễn tiến lâm sàng')}, {r('hình ảnh X-quang')} và {g('kháng sinh phối hợp')} cần dùng?",
  [f"Lâm sàng {y('tối cấp')}: {r('nhiễm độc nặng, da tái xám, sốt cao liên tục, thở rên, tụt huyết áp')}.",
   f"X-quang tiến triển nhanh trong {y('24 giờ')}: đám mờ đông đặc → nhiều {c('bóng khí (pneumatocele)')}, hang hoại tử, hoặc {r('tràn khí màng phổi áp lực')} do vỡ bóng khí.",
   f"Điều trị: {g('Vancomycin hoặc Linezolid')} (diệt tụ cầu kháng Methicillin) + {g('Clindamycin')} (ức chế tổng hợp độc tố Panton-Valentine Leukocidin)."],
  "Một thuốc diệt khuẩn, một thuốc chặn độc tố — hai cơ chế bổ sung nhau cho bệnh do độc tố PVL.",
  "Phần 4.2 Biến chứng — Viêm phổi hoại tử")
B("PED21-B4-05", "B4", 2, "Biến chứng",
  f"{c('pARDS')} sau CAP: {y('định nghĩa/thời gian')}, {y('tiêu chuẩn oxy hóa')} và {r('hình ảnh X-quang')}?",
  [f"Tổn thương phế nang lan tỏa trong vòng {y('7 ngày')} sau khởi phát nhiễm trùng phổi.",
   f"Thiếu oxy nặng không tương xứng: {y('PaO2/FiO2 ≤ 300')} hoặc {y('OI ≥ 4')}.",
   f"X-quang: {r('thâm nhiễm phế nang hai bên lan tỏa')}, không do suy tim ứ huyết."],
  "Loại trừ phù phổi do tim là điều kiện để gọi là ARDS — tổn thương là viêm lan tỏa chứ không phải quá tải áp lực.",
  "Phần 4.2 Biến chứng — pARDS")

# ───────────────────────── B5: Điều trị ─────────────────────────
B("PED21-B5-01", "B5", 1, "Điều trị",
  f"Điều trị CAP chia {y('2 nhánh')}: {c('ngoại trú (viêm phổi không nặng)')} và {r('nội trú (viêm phổi nặng)')} — mỗi nhánh gồm những thành phần nào (tóm tắt)?",
  [f"{c('Ngoại trú')}: {g('Amoxicillin liều cao 80–90 mg/kg/ngày × 5 ngày')}; Co-amoxiclav tỷ lệ 7:1/8:1 nếu nghi Beta-lactamase; Azithromycin/Clarithromycin nếu &gt; 5 tuổi nghi không điển hình.",
   f"{r('Nội trú')}: hỗ trợ hô hấp (oxy → HFNC/CPAP), kháng sinh TM ({g('Ampicillin / Cefotaxime / Ceftriaxone')}), phối hợp {g('Vancomycin + Clindamycin')} nếu nghi CA-MRSA, hạn chế dịch {y('80%')}."],
  "Quyết định rẽ nhánh dựa vào: dấu hiệu nguy hiểm, SpO2 ≥ 92%, uống được thuốc.",
  "Phần 5 Phác đồ điều trị")
B("PED21-B5-02", "B5", 2, "Điều trị",
  f"{g('Amoxicillin uống')} điều trị viêm phổi ngoại trú: {y('điều kiện áp dụng')}, {y('liều, cách chia, thời gian')}, {r('trần liều')}, bằng chứng cho 5 ngày, và dạng bào chế?",
  [f"Áp dụng: Viêm phổi (thở nhanh và/hoặc rút lõm nhẹ), không dấu hiệu nguy hiểm, {y('SpO2 ≥ 92%')}, còn bú/uống được thuốc. Trẻ {y('2 tháng–5 tuổi')} (tác nhân chính phế cầu).",
   f"Liều {y('80–90 mg/kg/ngày')}, chia {y('2 lần (mỗi 12 giờ) hoặc 3 lần (mỗi 8 giờ)')}.",
   f"Thời gian {y('5 ngày')} (CAP-IT và SAFER: tương đương 7–10 ngày, ít kháng thuốc và ít tác dụng phụ tiêu hóa).",
   f"{r('Trần liều')} {y('2000–3000 mg/ngày')} (liều người lớn).",
   "Dạng bào chế: gói cốm/hỗn dịch 250 mg, 500 mg hoặc viên 500 mg."],
  "Liều cao để đạt T > MIC với phế cầu kháng trung gian; 5 ngày là đủ cho ca đáp ứng tốt nên không kéo dài 10–14 ngày theo thói quen.",
  "Phần 5.1 Phác đồ ngoại trú")
B("PED21-B5-03", "B5", 2, "Điều trị",
  f"Khi nghi vi khuẩn tiết {c('Beta-lactamase')}: {r('2 tình huống gợi ý')}, thuốc chọn, {y('liều Amoxicillin')}, và {r('lưu ý sống còn về tỷ lệ bào chế')} (vì sao)?",
  [f"Gợi ý: {r('dùng Amoxicillin trong 30 ngày qua')}; {r('viêm tai giữa kèm theo')}.",
   f"Thuốc: {g('Amoxicillin-Clavulanic acid (Co-amoxiclav)')}, vẫn phải đạt Amoxicillin {y('80–90 mg/kg/ngày')}.",
   f"Chọn tỷ lệ Amoxicillin:Clavulanate {y('7:1 hoặc 8:1')} (gói 400/57 mg hoặc 200/28.5 mg).",
   f"Dạng cũ {y('4:1')} (gói 250/62.5 mg): để đạt 90 mg/kg lượng Clavulanate quá cao → {r('tiêu chảy thẩm thấu dữ dội')}."],
  "Clavulanate là thành phần gây tiêu chảy; muốn tăng Amoxicillin mà không tăng Clavulanate thì phải chọn tỷ lệ ít Clavulanate hơn.",
  "Phần 5.1 Chi tiết thuốc")
B("PED21-B5-04", "B5", 2, "Điều trị",
  f"Trẻ {y('&gt; 5 tuổi')} nghi viêm phổi {c('không điển hình (Mycoplasma)')}: {g('Azithromycin')} liều ngày 1, ngày 2–5 (kèm trần) và phương án thay thế {g('Clarithromycin')}?",
  [f"{g('Azithromycin')}: ngày 1 {y('10 mg/kg/ngày × 1 lần (tối đa 500 mg)')}; ngày 2–5 {y('5 mg/kg/ngày × 1 lần (tối đa 250 mg/ngày)')}.",
   f"{g('Clarithromycin')}: {y('15 mg/kg/ngày chia 2 lần')}, {y('7–10 ngày')}, tối đa {y('1000 mg/ngày')}.",
   f"Chọn nhánh: nghi phế cầu (sốt cao, đông đặc thùy) → Amoxicillin liều cao; nghi không điển hình (ho dai dẳng, thâm nhiễm kẽ lan tỏa) → Azithromycin {y('10 mg/kg/ngày')}."],
  "Macrolide chỉ dành cho trẻ lớn có bệnh cảnh không điển hình; ở trẻ nhỏ không dùng thường quy (xem phần bằng chứng EPIC).",
  "Phần 5.1 Trẻ trên 5 tuổi")
B("PED21-B5-05", "B5", 2, "Điều trị",
  f"Viêm phổi nặng nội trú — {g('hỗ trợ hô hấp')}: tư thế, {y('oxy canula (khởi đầu, SpO2 mục tiêu)')}, và {g('khi nào nâng bậc')} HFNC/CPAP với thông số?",
  [f"Nằm {y('đầu cao 30 độ')}, cổ thẳng, thông thoáng đường thở.",
   f"Oxy canula mũi: khởi đầu {y('0.5–2 L/phút')}, SpO2 mục tiêu {y('94–98%')} (tim bẩm sinh tím có mục tiêu riêng).",
   f"Nếu SpO2 không đạt hoặc trẻ co kéo kiệt sức: {g('HFNC 1.5–2 L/kg/phút')} hoặc {g('CPAP 4–6 cmH2O')}."],
  "Mở phế nang xẹp lân cận bằng áp lực dương là điều oxy canula không làm được trong shunt.",
  "Phần 5.2 Hỗ trợ hô hấp")
B("PED21-B5-06", "B5", 2, "Điều trị",
  f"Kháng sinh {g('tĩnh mạch đầu tay')} cho viêm phổi nặng: {y('3 lựa chọn')} (liều, số lần chia, lưu ý ưu tiên)?",
  [f"{g('Ampicillin')} {y('150–200 mg/kg/ngày chia 4 lần (mỗi 6 giờ)')} — lựa chọn đầu tay nếu phế cầu địa phương còn nhạy.",
   f"{g('Cefotaxime')} {y('100–150 mg/kg/ngày chia 3 lần (mỗi 8 giờ)')} TM chậm — ưu tiên cho trẻ nhỏ và sơ sinh.",
   f"{g('Ceftriaxone')} {y('50–80 mg/kg/ngày')} TM {y('1 lần/ngày')} (truyền 30 phút)."],
  "Chọn theo độ nhạy phế cầu địa phương và nhóm tuổi; Ceftriaxone tiện (1 lần/ngày) nhưng có trần liều và chống chỉ định ở sơ sinh.",
  "Phần 5.2 Kháng sinh tĩnh mạch")
B("PED21-B5-07", "B5", 2, "Điều trị",
  f"{r('Ceftriaxone')}: {y('trần liều')}, ví dụ minh họa trẻ 35 kg, hậu quả vượt trần, và {r('chống chỉ định tuyệt đối')} (độ tuổi, vì sao)?",
  [f"Trần: {y('2000 mg/ngày (2 g/ngày)')}.",
   f"Ví dụ: trẻ {y('35 kg')} × 80 mg/kg = {y('2800 mg')} → bắt buộc kéo về {y('2000 mg/ngày')} để tránh {r('ngộ độc thận và bùn mật')}.",
   f"{r('CHỐNG CHỈ ĐỊNH')}: trẻ sơ sinh {y('&lt; 28 ngày tuổi')} (gây {r('vàng da nhân não')} và {r('kết tủa Calci-Ceftriaxone')} tại phổi và thận)."],
  "Công thức mg/kg không biết dừng ở đâu — trẻ lớn 35–40 kg dễ vượt liều người lớn nếu không đối chiếu trần.",
  "Phần 5.2 Kháng sinh tĩnh mạch")
B("PED21-B5-08", "B5", 2, "Điều trị",
  f"Khi nghi {c('tụ cầu hoại tử / CA-MRSA')}: {g('Vancomycin')} (liều, chia, thời gian truyền, nồng độ đáy mục tiêu) và {g('Clindamycin')} (liều, mục đích)?",
  [f"{g('Vancomycin')} {y('40–60 mg/kg/ngày chia 4 lần')}, truyền chậm tối thiểu {y('60 phút')}, theo dõi nồng độ đáy (Trough) {y('15–20 mcg/mL')}.",
   f"{g('Clindamycin')} {y('30–40 mg/kg/ngày chia 3–4 lần')} để ức chế tổng hợp độc tố {c('PVL')} của tụ cầu."],
  "Phối hợp, không thay thế: Vancomycin diệt vi khuẩn, Clindamycin giảm độc tố.",
  "Phần 5.2 Phối hợp kháng sinh")
B("PED21-B5-09", "B5", 2, "Điều trị",
  f"{c('Dịch truyền và dinh dưỡng')} trong viêm phổi nặng: {r('nguy cơ nào')} cần tránh, {y('mức hạn chế')} và {g('loại dịch')}?",
  [f"Tránh truyền thừa: viêm phổi nặng hay có {r('SIADH')} → quá tải thể tích, {r('phù phổi kẽ')}.",
   f"Hạn chế ở {y('80% nhu cầu duy trì cơ bản')}.", f"Dùng dung dịch {g('đẳng trương: Glucose 5% pha trong NaCl 0.9%')}."],
  "SIADH giữ nước nên cùng một lượng dịch 'bình thường' đã là quá tải với phổi đang viêm.",
  "Phần 5.2 Dinh dưỡng và bù dịch")
B("PED21-B5-10", "B5", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — {g('Bảng liều bỏ túi')} các kháng sinh CAP: thuốc, đường dùng, liều, số lần chia, thời gian/trần liều?",
  [f"{g('Amoxicillin uống')}: {y('80–90 mg/kg/ngày')}, chia 2–3 lần, {y('5 ngày')}, trần {y('2000–3000 mg/ngày')}.",
   f"{g('Azithromycin uống (&gt; 5 tuổi)')}: ngày 1 {y('10 mg/kg (max 500 mg)')}; ngày 2–5 {y('5 mg/kg (max 250 mg)')}. {g('Clarithromycin')} {y('15 mg/kg/ngày chia 2, 7–10 ngày, max 1000 mg/ngày')}.",
   f"{g('Ampicillin TM')} {y('150–200 mg/kg/ngày chia 4')}; {g('Cefotaxime TM')} {y('100–150 mg/kg/ngày chia 3')}; {g('Ceftriaxone TM')} {y('50–80 mg/kg/ngày × 1, max 2000 mg/ngày')}.",
   f"{g('Vancomycin TM')} {y('40–60 mg/kg/ngày chia 4 (trough 15–20)')}; {g('Clindamycin')} {y('30–40 mg/kg/ngày chia 3–4')}."],
  "Học theo cặp 'số chia': 2–3 (Amoxicillin), 1 (Azithro/Ceftriaxone), 4 (Ampicillin/Vancomycin), 3 (Cefotaxime) và nhớ trần liều của Amoxicillin/Ceftriaxone/Azithromycin.",
  "Phần 5.1 và Phần 5.2", algo=True)
B("PED21-B5-11", "B5", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — {g('Công thức tính liều nhanh')} và bước {r('kiểm trần liều')}: ví dụ trẻ 10 kg, 14 kg (Amoxicillin) và trẻ 40 kg (Ceftriaxone)?",
  [f"Công thức: {y('liều/ngày = cân nặng (kg) × mg/kg/ngày')} → chia số lần → {r('so với trần liều người lớn, lấy giá trị nhỏ hơn')}.",
   f"Trẻ {y('10 kg')} × 90 = {y('900 mg/ngày')} → {y('450 mg × 2 lần')} (cách 12 giờ), 5 ngày.",
   f"Trẻ {y('14 kg')} × 90 = {y('1260 mg/ngày')} → khoảng {y('600–650 mg × 2 lần')}.",
   f"Trẻ {y('40 kg')} × 80 = {y('3200 mg')} → {r('kê 2 g/ngày (2000 mg)')}, pha trong 100 mL NaCl 0.9% truyền chậm 30 phút, 1 lần/ngày."],
  "Hai bước luôn đi liền: tính theo cân nặng rồi chặn bằng trần; bước thứ hai thường bị quên ở trẻ lớn.",
  "Phần 5, Phần 9 Checkpoint 2–3, Phần 10", algo=True)

# ───────────────────────── B6: Lưu đồ & nguồn lực ─────────────────────────
B("PED21-B6-01", "B6", 1, "Lưu đồ",
  f"Lưu đồ tại buồng bệnh gồm {y('4 bước')} từ tiếp nhận đến đánh giá lại và {c('kế hoạch theo nguồn lực')} — tên và nội dung chính mỗi bước?",
  [f"{r('Bước 0')}: sàng lọc cờ đỏ cấp cứu.", f"{y('Bước 1')}: đếm nhịp thở chuẩn 60 giây + khám co kéo.",
   f"{y('Bước 2')}: có thở nhanh và/hoặc rút lõm → phân {r('nặng')} (nhập viện) hay {c('không nặng')} (ngoại trú).",
   f"{y('Đánh giá lại sau 48–72 giờ')}: cải thiện hay thất bại.", f"{c('Plan A')} (đủ nguồn lực) và {c('Plan B')} (trạm y tế)."],
  "Lưu đồ đặt an toàn lên trước: cờ đỏ trước, đo lường chuẩn sau, rồi mới chọn nơi điều trị.",
  "Phần 6 Lưu đồ quyết định")
B("PED21-B6-02", "B6", 2, "Lưu đồ",
  f"{r('Bước 0')} khi {r('CÓ cờ đỏ')}: {y('6 câu sàng lọc')} và {g('4 hành động')} kích hoạt; và nếu {c('không thở nhanh, không co kéo')} thì làm gì?",
  [f"Sàng lọc: bỏ bú/uống? nôn tất cả? co giật? li bì? tím tái? thở rên?",
   f"{g('Hành động')}: thở oxy duy trì {y('SpO2 ≥ 94%')}; lập đường truyền TM khẩn; kháng sinh TM {g('Cefotaxim / Ceftriaxone')}; chuyển phòng cấp cứu/{c('PICU')}.",
   f"Không thở nhanh, không co kéo → {c('nhiễm khuẩn hô hấp trên')}: {r('không dùng kháng sinh')}, hạ sốt, uống nhiều nước, dặn dấu hiệu tái khám."],
  "Ở bước đầu mục tiêu là ổn định, chưa cần phân loại căn nguyên.",
  "Phần 6 Bước 0–1")
B("PED21-B6-03", "B6", 2, "Lưu đồ",
  f"Bước 2: {r('viêm phổi NẶNG')} và {c('viêm phổi KHÔNG nặng')} — {y('tiêu chí')} và {g('xử trí cụ thể')} (4 việc nhập viện, 4 việc ngoại trú)?",
  [f"{r('NẶNG')}: co kéo nặng, phập phồng cánh mũi; {y('SpO2 &lt; 92%')}; không uống được thuốc.",
   f"{c('KHÔNG nặng')}: rút lõm nhẹ hoặc chỉ thở nhanh; tỉnh táo, bú/uống tốt, SpO2 ≥ 92%; gia đình theo dõi sát được.",
   f"{r('Nhập viện')}: (1) oxy canula; (2) kháng sinh TM Ampicillin hoặc Cefotaxim/Ceftriaxone; (3) {y('hạn chế dịch 80%')}; (4) chụp X-quang phổi thẳng.",
   f"{g('Ngoại trú')}: (1) Amoxicillin liều cao {y('80–90 mg/kg/ngày')}; (2) uống đúng {y('5 ngày')}; (3) hẹn tái khám sau {y('48 giờ')} hoặc khi có dấu hiệu nặng; (4) {r('KHÔNG chụp X-quang ngực')}."],
  "Ba tiêu chí thực dụng của ngoại trú: SpO2 ≥ 92%, uống/bú được, gia đình theo dõi sát được.",
  "Phần 6 Bước 2")
B("PED21-B6-04", "B6", 2, "Lưu đồ",
  f"{y('Đánh giá lại sau 48–72 giờ')} ở trẻ nhập viện: dấu hiệu {g('cải thiện')} và hành động, dấu hiệu {r('thất bại')} và hành động?",
  [f"{g('Cải thiện')}: hết sốt, nhịp thở giảm, bú tốt, cai được oxy → chuyển kháng sinh uống, hoàn thành đủ {y('7–10 ngày')}.",
   f"{r('Thất bại/xấu đi')}: sốt cao liên tục, thở nhanh hơn, SpO2 tụt, co kéo tăng → nghi {c('tràn mủ màng phổi, hoại tử, hoặc tụ cầu kháng thuốc')}.",
   f"Hành động khi thất bại: {g('Siêu âm màng phổi + X-quang; đổi Vancomycin + dẫn lưu mủ')}."],
  "Mốc 48–72 giờ là thời gian tối thiểu để kháng sinh đúng phát huy tác dụng; vượt mốc mà vẫn xấu thì phải tìm biến chứng thay vì chỉ đổi thuốc.",
  "Phần 6 Đánh giá lại")
B("PED21-B6-05", "B6", 2, "Lưu đồ",
  f"{c('Plan A')} (bệnh viện tuyến trên) và {c('Plan B')} (trạm y tế/vùng sâu): mỗi kế hoạch gồm {y('những phương tiện/hành động nào')}?",
  [f"{c('Plan A')}: SpO2 liên tục, máy khí dung, {g('siêu âm màng phổi tại giường trong 15 phút')}, Real-time PCR đa mồi, {y('Procalcitonin')}, khí máu động mạch, sẵn sàng HFNC và CPAP.",
   f"{c('Plan B')}: dựa giác quan — đếm nhịp thở bằng mắt trọn {y('60 giây')} khi trẻ ngủ yên; quan sát rút lõm khi bộc lộ ngực bụng; nhận thở rên bằng tai trần ghé sát mũi miệng.",
   f"Plan B điều trị: Amoxicillin gói/viên nghiền uống cho viêm phổi; nếu {r('rút lõm nặng hoặc bỏ bú')} → {g('tiêm bắp 1 liều Ceftriaxone hoặc Ampicillin rồi chuyển viện khẩn')}."],
  "Phân loại WHO dựa vào nhịp thở và rút lõm nên vẫn áp dụng được khi không có ống nghe, X-quang hay xét nghiệm.",
  "Phần 6 Kế hoạch hành động theo nguồn lực")
B("PED21-B6-06", "B6", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — {c('Cây quyết định nhị phân')} từ lúc tiếp nhận: {r('IF cờ đỏ')} / {c('IF không thở nhanh, không co kéo')} / {c('IF có thở nhanh ± rút lõm')} → làm gì?",
  [f"{r('IF có BẤT KỲ cờ đỏ')} (bỏ bú, nôn tất cả, co giật, li bì, tím tái, thở rên, SpO2 &lt; 90%) → {g('oxy + đường truyền + kháng sinh TM + PICU')}.",
   f"{c('IF không thở nhanh và không rút lõm')} → không phải viêm phổi: {r('không kháng sinh')}, hạ sốt, dặn tái khám.",
   f"{c('IF thở nhanh ± rút lõm, tỉnh, SpO2 ≥ 92%, uống được')} → ngoại trú: {g('Amoxicillin 80–90 mg/kg/ngày × 5 ngày')}, không X-quang, tái khám {y('48 giờ')}.",
   f"{c('IF thở nhanh ± rút lõm nhưng co kéo nặng / SpO2 &lt; 92% / không uống được')} → nhập viện, kháng sinh TM, sau {y('48–72 giờ')} không đỡ → {r('siêu âm màng phổi + nghĩ biến chứng')}."],
  "Trình tự cố định: an toàn tính mạng → có/không viêm phổi → nặng/không nặng → đánh giá lại.",
  "Phần 6 Lưu đồ", algo=True)

# ───────────────────────── B7: Bằng chứng ─────────────────────────
B("PED21-B7-01", "B7", 1, "Bằng chứng",
  f"Hai cập nhật bằng chứng 10 năm qua: {y('(1) thời gian kháng sinh')} và {c('(2) vai trò vi khuẩn không điển hình')} — mỗi cập nhật rút ra khuyến cáo gì (tóm tắt)?",
  [f"{g('Liệu trình ngắn')}: ngoại trú đáp ứng tốt chỉ cần Amoxicillin {y('5 ngày')} (CAP-IT, SAFER).",
   f"{r('Không kê Macrolide thường quy')} cho trẻ &lt; 5 tuổi (EPIC)."],
  "Hai khuyến cáo cùng hướng: kháng sinh ít hơn nhưng đúng hơn.",
  "Phần 7 Bằng chứng y học")
B("PED21-B7-02", "B7", 2, "Bằng chứng",
  f"Thử nghiệm {c('CAP-IT')} và {c('SAFER')}: {y('thiết kế/cỡ mẫu/địa điểm')}, {y('so sánh gì')}, {y('kết quả')} và {g('khuyến cáo cập nhật')}; trước đây thời gian điều trị thói quen là bao lâu?",
  [f"Trước đây thói quen {y('10–14 ngày')}.",
   f"{c('CAP-IT')} (JAMA 2021): RCT mù đôi {y('814 trẻ')} Anh và Ireland; Amoxicillin {y('3 ngày vs 7 ngày')} và liều thấp vs cao → liệu trình ngắn {r('không thua kém')} về tỷ lệ phải điều trị lại, giảm phơi nhiễm kháng sinh.",
   f"{c('SAFER')} (JAMA Pediatr 2021): Canada, Amoxicillin {y('5 ngày vs 10 ngày')} ngoại trú → khỏi bệnh lâm sàng ngày 14–21 tương đương ({y('88.6% vs 88.5%')}).",
   f"{g('Khuyến cáo')}: CAP ngoại trú đáp ứng tốt dùng Amoxicillin {y('5 ngày')}."],
  "Hai thử nghiệm cho cùng một thông điệp: rút ngắn không làm tăng thất bại mà giảm kháng thuốc và tác dụng phụ.",
  "Phần 7.1 CAP-IT & SAFER")
B("PED21-B7-03", "B7", 2, "Bằng chứng",
  f"Nghiên cứu {c('EPIC (CDC Hoa Kỳ, NEJM 2015)')}: phát hiện về {c('Mycoplasma pneumoniae')} ở trẻ {y('&lt; 5 tuổi')}, ý nghĩa của PCR dương tính và {g('khuyến cáo kê Macrolide')}?",
  [f"{c('M. pneumoniae')} {r('rất hiếm khi')} gây viêm phổi nặng ở trẻ &lt; 5 tuổi.",
   "Phần lớn PCR dương tính ở trẻ nhỏ chỉ là mang vi khuẩn không triệu chứng ở tỵ hầu.",
   f"{g('Khuyến cáo')}: {r('không kê Macrolide (Azithromycin, Clarithromycin) thường quy')} cho trẻ &lt; 5 tuổi trừ khi có bằng chứng dịch tễ rõ hoặc không đáp ứng Beta-lactam liều cao."],
  "PCR dương tính ≠ tác nhân gây bệnh; điều trị theo bệnh cảnh và dịch tễ, không theo kết quả PCR đơn thuần.",
  "Phần 7.2 EPIC")

# ───────────────────────── B8: Cạm bẫy ─────────────────────────
B("PED21-B8-01", "B8", 1, "Cạm bẫy",
  f"{y('8 cạm bẫy')} kinh điển của CAP: kể tên ngắn gọn từng bẫy?",
  [f"Đếm nhịp thở khi trẻ khóc/sốt cao {y('39.5 °C')}.", f"Đếm {y('15 giây × 4')}.", "X-quang thường quy cho viêm phổi nhẹ ngoại trú.",
   f"Amoxicillin liều thông thường {y('40–50 mg/kg/ngày')}.", f"Co-amoxiclav tỷ lệ {y('4:1')}.", f"Quên trần liều {c('Ceftriaxone')} ở trẻ lớn.",
   f"Đổi kháng sinh vội trong {y('24 giờ')}.", f"Thuốc {r('giảm ho / kháng Histamin')}."],
  "Tám bẫy chia ba nhóm: đo lường (1–2), chỉ định thừa (3), kê đơn sai (4–6, 7), điều trị hỗ trợ có hại (8).",
  "Phần 8 Cạm bẫy lâm sàng")
B("PED21-B8-02", "B8", 2, "Cạm bẫy",
  f"Bẫy {y('1 và 2')} về {c('đếm nhịp thở')}: {r('cơ chế sai lệch')} (số liệu tăng nhịp theo sốt, sai số) và {g('cách phòng ngừa')}?",
  [f"Bẫy 1 (khóc/sốt {y('39.5 °C')}): nhịp thở tăng sinh lý, khoảng {y('+10 nhịp/phút cho mỗi 1 °C')} → chẩn đoán nhầm và kê đơn oan. {g('Hạ sốt Paracetamol, đợi trẻ yên/ngủ rồi đếm 60 giây')}.",
   f"Bẫy 2 (đếm {y('15 giây × 4')}): nhũ nhi thở ngắt quãng không đều, nhân nhẩm khuếch đại sai số {y('gấp 4 lần')}. {g('Đếm trọn 60 giây bằng đồng hồ có kim giây')}."],
  "Cả hai đều làm tăng giả nhịp thở → chẩn đoán dương tính giả → kháng sinh không cần thiết.",
  "Phần 8 Cạm bẫy 1–2")
B("PED21-B8-03", "B8", 2, "Cạm bẫy",
  f"Bẫy {y('3, 4 và 5')} (X-quang, liều Amoxicillin, tỷ lệ Co-amoxiclav): {r('hậu quả')} và {g('cách phòng ngừa')} từng bẫy?",
  [f"Bẫy 3 (X-quang thường quy): bức xạ không cần thiết; hình virus bị đọc nhầm vi khuẩn → leo thang kháng sinh. {g('Chỉ chụp khi nghi biến chứng, viêm phổi nặng nhập viện, thất bại sau 48–72 giờ')}.",
   f"Bẫy 4 (liều {y('40–50 mg/kg/ngày')}): thuốc tự do không vượt MIC phế cầu kháng trung gian ({y('T &gt; MIC &lt; 40%')}) → thất bại. {g('Bắt buộc 80–90 mg/kg/ngày chia 2–3 lần')}.",
   f"Bẫy 5 (Co-amoxiclav {y('4:1')} để đạt 90 mg/kg): nhiều Clavulanic acid → viêm ruột thẩm thấu, tiêu chảy mất nước. {g('Chọn tỷ lệ 7:1 hoặc 8:1')}."],
  "Ba bẫy này là ba lỗi 'đúng ý định, sai thực hiện': muốn chẩn đoán chắc, muốn dùng đúng thuốc, muốn đạt liều.",
  "Phần 8 Cạm bẫy 3–5")
B("PED21-B8-04", "B8", 2, "Cạm bẫy",
  f"Bẫy {y('6, 7 và 8')} (trần liều Ceftriaxone, đổi thuốc vội, thuốc giảm ho): {r('hậu quả')} và {g('cách phòng ngừa')}?",
  [f"Bẫy 6: trẻ {y('35 kg')} × 80 mg/kg = {y('2800 mg')} vượt trần {y('2000 mg/ngày')} → bùn mật, độc tính thận. {g('Ghi nhớ trần 2 g/ngày')}.",
   f"Bẫy 7: đổi thuốc trong {y('24 giờ')} vì còn sốt — sốt thường cần {y('48–72 giờ')} để hạ. {g('Nếu tổng trạng ổn, nhịp thở không tăng, SpO2 không tụt → kiên trì 48–72 giờ rồi đánh giá')}.",
   f"Bẫy 8: thuốc giảm ho/kháng Histamin ức chế ho sinh tồn → ứ mủ phế nang, nặng thêm suy hô hấp. {g('Không dùng Codein, Dextromethorphan; chỉ làm ẩm đường thở và vỗ rung dẫn lưu nhẹ nhàng')}."],
  "Ho là cơ chế làm sạch đường thở; dập ho là gây hại.",
  "Phần 8 Cạm bẫy 6–8")
B("PED21-B8-05", "B8", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — {r('3 KHÔNG')} và {g('3 NÊN')} khi xử trí CAP ở trẻ em?",
  [f"{r('KHÔNG')} đếm nhịp thở khi trẻ khóc/sốt cao hoặc đếm 15 giây × 4 — {g('NÊN')} hạ sốt, đếm trọn {y('60 giây')} khi trẻ yên.",
   f"{r('KHÔNG')} chụp X-quang thường quy ở viêm phổi nhẹ ngoại trú — {g('NÊN')} chụp khi viêm phổi nặng, nghi biến chứng, thất bại {y('48–72 giờ')}.",
   f"{r('KHÔNG')} dùng Amoxicillin {y('40–50 mg/kg/ngày')} hay thuốc giảm ho — {g('NÊN')} {y('80–90 mg/kg/ngày')} và chỉ làm ẩm đường thở.",
   f"Nhắc thêm: kiểm trần liều Ceftriaxone {y('2 g/ngày')}; không dùng Ceftriaxone {y('&lt; 28 ngày')}; không đổi thuốc trước {y('48–72 giờ')} nếu ổn định."],
  "Mỗi KHÔNG đi kèm một NÊN thay thế để biến lỗi thành hành động đúng ngay tại giường.",
  "Phần 8 và Phần 12", algo=True)

# ───────────────────────── B9: Checkpoints ─────────────────────────
B("PED21-B9-01", "B9", 1, "Checkpoint",
  f"Bốn {y('checkpoint tự kiểm tra')} của bài xoay quanh {y('4 tình huống nào')} và mỗi tình huống kiểm tra lỗi gì?",
  [f"CP1: trẻ 10 tháng sốt, nhịp thở 56 → xử trí nhịp thở ở trẻ {r('đang sốt')}.",
   f"CP2: trẻ 3 tuổi 14 kg → chọn {g('liều và dạng Amoxicillin')}.", f"CP3: trẻ 9 tuổi 40 kg → {r('bẫy trần liều Ceftriaxone')}.",
   f"CP4: sốt dù Cefotaxim 3 ngày, giảm âm phổi phải → chọn {c('siêu âm màng phổi')} hay CT."],
  "Mỗi tình huống ứng với một bẫy lớn: đo lường, tính liều, trần liều, chọn cận lâm sàng.",
  "Phần 9 Điểm dừng tự kiểm tra")
B("PED21-B9-02", "B9", 2, "Checkpoint",
  f"{y('CP1')}: trẻ nam 10 tháng, 9 kg, sốt {y('39.2 °C')}, ho 2 ngày, nhịp thở ban đầu {y('56')} → điều dưỡng báo viêm phổi nặng. {g('Bác sĩ làm gì')}, liều Paracetamol (mg), thời gian chờ và {r('tiêu chí chẩn đoán lại')}?",
  [f"{r('Sai quy trình')}: đếm khi đang sốt 39.2 °C (thân nhiệt kích thích trung tâm hô hấp, tăng {y('7–10 lần/phút mỗi 1 °C')}).",
   f"Cho Paracetamol {y('10–15 mg/kg (90–135 mg)')}, cởi bớt áo, chườm ấm trán–nách–bẹn.",
   f"Chờ {y('30–45 phút')}, thân nhiệt &lt; {y('38 °C')}, trẻ yên → đếm lại trọn 60 giây.",
   f"Chỉ chẩn đoán viêm phổi nếu sau hạ sốt vẫn {y('≥ 50 lần/phút')} (nhóm 2–11 tháng)."],
  "Con số 56 chưa có giá trị khi trẻ sốt cao; phải đo lại trong điều kiện chuẩn mới so với ngưỡng.",
  "Phần 9 Checkpoint 1")
B("PED21-B9-03", "B9", 2, "Checkpoint",
  f"{y('CP2')}: trẻ 3 tuổi, {y('14 kg')}, tỉnh, thở {y('44')}, rút lõm bờ sườn nhẹ, SpO2 {y('96%')}, ran ẩm đáy phải, chưa dùng kháng sinh 3 tháng qua. {g('Thuốc, liều, cách chia, dạng thuốc, thời gian')}?",
  [f"Chẩn đoán: {c('viêm phổi không nặng')} → {g('Amoxicillin liều cao 80–90 mg/kg/ngày')}.",
   f"Tính: {y('14 kg × 90 = 1260 mg/ngày')}, chia 2 lần, mỗi lần khoảng {y('600–650 mg')} (cách 12 giờ).",
   f"Kê đơn thực tế: gói {y('250 mg')} (2.5 gói/lần × 2 lần/ngày) hoặc viên {y('500 mg')} (1 viên + 1/4 viên/lần), uống đúng {y('5 ngày')}.",
   "Dặn mẹ dấu hiệu cờ đỏ để tái khám ngay."],
  "Từ liều mg/ngày phải đổi sang đơn vị thực tế (gói/viên) thì bà mẹ mới thực hiện được.",
  "Phần 9 Checkpoint 2")
B("PED21-B9-04", "B9", 2, "Checkpoint",
  f"{y('CP3')}: trẻ 9 tuổi, {y('40 kg')}, viêm phổi nặng thùy dưới trái, SpO2 {y('90%')}; y lệnh 'Ceftriaxone 3.2 g TM 1 lần/ngày'. {r('Đúng hay sai')}, vì sao, và {g('y lệnh sửa chuẩn')} (liều, dung môi, thời gian truyền)?",
  [f"{r('SAI VÀ NGUY HIỂM')}: rơi vào bẫy trần liều người lớn.",
   f"Công thức cho {y('3.2 g/ngày')} nhưng trần tuyệt đối trong nhiễm trùng hô hấp là {y('2 g/ngày (2000 mg)')}.",
   f"Nguy cơ: kết tủa muối {c('Calci-Ceftriaxone')} ở đường tiết niệu → {r('suy thận cấp sau thận')}, {r('bùn mật giả sỏi (biliary pseudolithiasis)')}.",
   f"Sửa: {g('Ceftriaxone 2 g pha trong 100 mL NaCl 0.9%, truyền TM chậm 30 phút, 1 lần/ngày')}."],
  "Dùng công thức mà quên cận trên là lỗi kê đơn phổ biến nhất ở trẻ lớn.",
  "Phần 9 Checkpoint 3")
B("PED21-B9-05", "B9", 2, "Checkpoint",
  f"{y('CP4')}: trẻ 2 tuổi, Cefotaxim {y('3 ngày')} vẫn sốt {y('39 °C')}, thở {y('52')}, giảm âm phổi phải hoàn toàn. {g('Chọn CT hay siêu âm màng phổi')}, vì sao (3 ưu điểm) và khi nào mới cần {c('CT')}?",
  [f"{g('Siêu âm màng phổi')} là chỉ định ưu tiên số 1 tại giường.",
   f"Ưu điểm: phát hiện dịch {y('nhạy hơn X-quang thường')}; {y('không nhiễm xạ')} như CT; đánh giá cấu trúc dịch (vách ngăn sợi huyết/loculations), ước tính thể tích, định vị vị trí chọc/dẫn lưu an toàn.",
   f"{c('CT lồng ngực')} chỉ dành cho nghi {r('áp xe phổi sâu')} hoặc khi siêu âm không giải thích được toàn bộ tổn thương."],
  "Trẻ nhỏ + cần theo dõi nhiều lần → ưu tiên phương tiện không bức xạ và thực hiện ngay tại giường.",
  "Phần 9 Checkpoint 4")

# ───────────────────────── B10: Ca lâm sàng ─────────────────────────
B("PED21-B10-01", "B10", 1, "Ca lâm sàng",
  f"Hai ca lâm sàng của bài: {y('ca 1')} (14 tháng) và {r('ca 2')} (3 tuổi) — mỗi ca {c('chẩn đoán')} gì và {g('xử trí chính')} gì (tóm tắt)?",
  [f"{y('Ca 1')} (bé gái 14 tháng, 10 kg): CAP {c('không nặng')}, nghi phế cầu → {g('Amoxicillin 90 mg/kg/ngày × 5 ngày')} ngoại trú, không X-quang, tái khám 48 giờ.",
   f"{r('Ca 2')} (bé trai 3 tuổi, 14 kg): viêm phổi nặng + {c('tràn mủ màng phổi phải')} + suy hô hấp cấp → oxy/HFNC, siêu âm, chọc hút/dẫn lưu, {g('Ceftriaxone + Vancomycin')}."],
  "Hai ca là hai đầu phổ: ca nhẹ thì làm ít và đúng; ca nặng thì làm nhiều theo thứ tự cứu mạng.",
  "Phần 10 Hai ca lâm sàng")
B("PED21-B10-02", "B10", 2, "Ca lâm sàng",
  f"{y('Ca 1')} (14 tháng, 10 kg, nhịp thở {y('48')}, co kéo nhẹ bờ sườn, SpO2 {y('96%')}, ran ẩm nhỏ hạt đáy phải): phân tích {y('5 bước')} — {r('cờ đỏ')}, {c('đối chiếu ngưỡng')}, {c('chẩn đoán + phân biệt')}, {g('đơn thuốc chi tiết')}, {g('dặn dò')}?",
  [f"{y('Bước 1')}: tỉnh, bú/uống tốt, không dấu hiệu nguy hiểm, SpO2 96% → chưa cần cấp cứu.",
   f"{y('Bước 2')}: tuổi 14 tháng (nhóm 12–59 tháng, ngưỡng {y('≥ 40')}), nhịp thở {y('48')} → {r('thở nhanh')}; rút lõm nhẹ; ran ẩm khu trú đáy phải.",
   f"{y('Bước 3')}: {c('CAP không nặng')}, nghi phế cầu; phân biệt {c('viêm tiểu phế quản')} (&lt; 12 tháng, khò khè lan tỏa), {c('nhiễm khuẩn hô hấp trên')} (không thở nhanh).",
   f"{y('Bước 4')}: ngoại trú; {r('không X-quang')}; Amoxicillin {y('90 mg/kg/ngày')}: 10 kg → {y('900 mg/ngày = 450 mg × 2 lần')}, gói 250 mg (gần 2 gói/lần) hoặc 500 mg (gần 1 gói/lần), {y('5 ngày')}; Paracetamol {y('10–15 mg/kg (100–150 mg)')} khi sốt ≥ 38.5 °C; bú mẹ tăng cường, nhỏ mũi NaCl 0.9% trước ăn.",
   f"{y('Bước 5')}: dặn dấu hiệu nguy hiểm (thở khó hơn, rút lõm sâu, bỏ bú, nôn mọi thứ, li bì, tím môi) → đến viện ngay; tái khám sau {y('48 giờ')}."],
  "Ca nhẹ nhưng vẫn đủ 5 bước: nhận diện nguy cơ → đối chiếu chuẩn tuổi → chẩn đoán → can thiệp → dặn dò.",
  "Phần 10 Ca lâm sàng 1")
B("PED21-B10-03", "B10", 2, "Ca lâm sàng",
  f"{r('Ca 2')} (3 tuổi, 14 kg, sốt 4 ngày dù Cefixime 3 ngày, li bì, nhịp thở {y('54')}, SpO2 {y('88%')}, gõ đục đáy phải): {r('cờ đỏ')}, {c('chẩn đoán')} và {g('xử trí cấp cứu')} (oxy/HFNC, cận lâm sàng, thủ thuật, ngưỡng pH, kháng sinh với liều, dịch)?",
  [f"{r('Cờ đỏ')}: li bì, thở rên, SpO2 88%, sốt cao nhiễm độc, co kéo hõm ức → suy hô hấp cấp nặng.",
   f"Ba giảm ở đáy phổi phải → {c('tràn dịch màng phổi')}; thất bại Cefixime (nồng độ dịch mô phổi và hoạt tính phế cầu kém) → nghi {c('tràn mủ màng phổi')}; tác nhân {c('S. pneumoniae hoặc S. aureus')}.",
   f"Oxy: mặt nạ túi dự trữ hoặc canula {y('2–3 L/phút')}, SpO2 mục tiêu {y('≥ 94%')}; nếu co kéo không giảm → {g('HFNC 20 L/phút (~1.5 L/kg/phút), FiO2 40–50%')}.",
   f"Cận lâm sàng: siêu âm màng phổi, X-quang tại giường, CTM, CRP, Procalcitonin, cấy máu trước kháng sinh mới, điện giải đồ.",
   f"Thủ thuật: chọc hút dịch xét nghiệm (màu, pH, protein, LDH, Gram, cấy); {g('mủ đặc hoặc pH &lt; 7.2 → đặt ống dẫn lưu kín hút áp lực âm liên tục')}.",
   f"Kháng sinh: {g('Ceftriaxone 14 × 80 = 1120 mg/ngày TM 1 lần')} + {g('Vancomycin 14 × 60 = 840 mg/ngày chia 4 (210 mg mỗi 6 giờ, truyền 60 phút)')}; nhịn ăn, Glucose 5% trong NaCl 0.9% {y('80%')} nhu cầu duy trì (~{y('950 mL/24 giờ')}).",
   f"{r('Chuyển PICU')} nếu sau dẫn lưu và oxy mà SpO2 {y('&lt; 92%')}, PaCO2 tăng hoặc huyết áp tụt → nội khí quản, thở máy; theo dõi liên tục SpO2, nhịp thở, lượng dịch dẫn lưu mỗi giờ."],
  "Ổ hoại tử sát màng phổi gây tràn mủ, chèn ép, đẩy lệch trung thất và tạo shunt lớn — nên vừa phải hỗ trợ hô hấp vừa dẫn lưu mủ.",
  "Phần 10 Ca lâm sàng 2")

# ───────────────────────── B11: Tips lâm sàng ─────────────────────────
B("PED21-B11-01", "B11", 1, "Mẹo lâm sàng",
  f"10 {y('mẹo thực hành')} của bài chia thành {y('3 nhóm')}: khám thực thể, kê đơn/điều trị hỗ trợ, và bẫy chẩn đoán — mỗi nhóm gồm những mẹo nào (tóm tắt)?",
  [f"{c('Khám')}: xoa ấm tay/ống nghe; mẹo nghe thở rên; đầu gật gù; kiểm tra sóng Plethysmogram; phân biệt stridor vs wheezing.",
   f"{g('Điều trị')}: cho uống Amoxicillin từng thìa nhỏ; không dùng thuốc tan đờm uống; bảo tồn tĩnh mạch.",
   f"{r('Bẫy')}: đau bụng sốt có thể là viêm phổi thùy dưới; viêm phổi tái đi tái lại một thùy → dị vật bỏ quên."],
  "Các mẹo đều là chi tiết nhỏ quyết định đếm nhịp thở có chuẩn không hoặc có bỏ sót chẩn đoán không.",
  "Phần 11 Clinical pearls")
B("PED21-B11-02", "B11", 2, "Mẹo lâm sàng",
  f"Mẹo {c('khám')}: (a) xoa ấm tay/ống nghe vì sao, (b) cách nghe {r('thở rên tinh tế')}, (c) {r('đầu gật gù')} ở trẻ nào và xử trí, (d) kiểm tra {c('SpO2/Plethysmogram')}, (e) phân biệt {c('Stridor vs Wheezing')}?",
  [f"(a) Lạnh làm trẻ giật mình khóc thét → mất cơ hội đếm nhịp thở và nghe ran chính xác.",
   f"(b) Thở rên sớm rất khẽ: ghé sát tai vào mũi miệng hoặc áp màng ống nghe ngay trước miệng → nghe tiếng 'hừ' ngắn ở thì {y('thở ra')}.",
   f"(c) Đầu gật gù = kiệt sức cơ hô hấp sắp xảy ra ở trẻ nhỏ {y('dưới 1 tuổi')}; {g('chuyển phòng cấp cứu ngay, không để ở phòng khám ngoại trú')}.",
   f"(d) SpO2 chỉ tin được khi sóng mạch đều và tần số mạch trên máy trùng nhịp tim nghe được; không quyết định dựa trên số nhảy loạn xạ khi trẻ giãy giụa.",
   f"(e) {r('Stridor')}: thì {y('hít vào')}, hẹp thanh/khí quản; {r('Wheezing')}: thì {y('thở ra')}, hẹp phế quản/tiểu phế quản → nhầm sẽ sai giữa {c('Croup')} và viêm phổi/hen."],
  "Mỗi mẹo ngăn một nguyên nhân sai số: trẻ khóc, âm thanh tinh tế bị bỏ sót, số đo giả, hoặc nhầm vị trí hẹp đường thở.",
  "Phần 11 Mẹo 1, 3, 5, 8, 10")
B("PED21-B11-03", "B11", 2, "Mẹo lâm sàng",
  f"Mẹo {g('điều trị')} và {r('chẩn đoán')}: (a) giảm nôn khi uống Amoxicillin, (b) vì sao {r('không dùng thuốc tan đờm uống')}, (c) {c('bảo tồn tĩnh mạch')}, (d) {r('đau bụng + sốt')}, (e) {r('viêm phổi tái đi tái lại một thùy')}?",
  [f"(a) Uống từng thìa nhỏ, sau bữa ăn nhẹ {y('15–30 phút')}, không ép uống cả cốc.",
   f"(b) {r('Acetylcysteine, Ambroxol')} tăng đờm loãng nhưng trẻ nhỏ không đủ lực cơ hoành để khạc → ngập lụt đờm, tắc nghẽn nặng hơn.",
   f"(c) Viêm phổi nặng có thể cần kháng sinh TM {y('7–14 ngày')} (nếu có mủ màng phổi): lập đường truyền ngoại vi cẩn thận, tránh chọc vỡ tĩnh mạch nhiều lần.",
   f"(d) Viêm phổi thùy dưới có thể gây {r('đau bụng dữ dội')} (kích thích thần kinh gian sườn dưới) → dễ nhầm viêm ruột thừa: {g('đếm nhịp thở và nghe đáy phổi trước khi đưa đi mổ')}.",
   f"(e) Tiền sử ho sặc sụa đột ngột vài tuần trước khi ăn lạc/hạt dưa + viêm phổi tái đi tái lại đúng một thùy → nghĩ {c('dị vật đường thở bỏ quên')} trước khi đổi kháng sinh."],
  "Các mẹo này giúp tránh thất bại điều trị không do thuốc: nôn mất liều, ứ đờm, chẩn đoán nhầm vùng bụng, bỏ sót dị vật.",
  "Phần 11 Mẹo 4, 6, 7, 2, 9")

# ───────────────────────── B12: Tóm tắt cốt lõi ─────────────────────────
B("PED21-B12-01", "B12", 1, "Tóm tắt",
  f"{y('10 điều mang vào ca trực')}: tóm tắt từng điều trong 1 cụm ngắn?",
  ["Thở nhanh là dấu hiệu nhạy nhất — đếm 60 giây khi yên, đã hạ sốt.", "Rút lõm là dấu tăng công thở.", "Cờ đỏ toàn thân → cấp cứu ngay.",
   f"Amoxicillin {y('80–90 mg/kg/ngày × 5 ngày')} ngoại trú.", "Không X-quang thường quy.", f"Bẫy trần liều: Ceftriaxone {y('2 g/ngày')}, Amoxicillin {y('2–3 g/ngày')}; CCĐ Ceftriaxone &lt; 28 ngày.",
   "Nhịp thở chậm + li bì = kiệt sức, không phải đỡ.", f"Đánh giá đáp ứng sau {y('48–72 giờ')}.", "Sốt dai dẳng + ba giảm → siêu âm màng phổi.", "Không thuốc giảm ho/tan đờm."],
  "Mười điều xếp theo trình tự lâm sàng: đo lường → phân loại → điều trị → theo dõi → tránh thuốc có hại.",
  "Phần 12 Tóm tắt cốt lõi")
B("PED21-B12-02", "B12", 2, "Tóm tắt",
  f"Điều 1–5 trong 10 điều: nêu {y('nội dung chi tiết')} (ngưỡng WHO, định nghĩa rút lõm, cờ đỏ, liều + thời gian Amoxicillin, X-quang)?",
  [f"{y('Thở nhanh')}: đếm trọn 60 giây khi nằm yên và đã hạ sốt; ngưỡng {y('&lt; 2 tháng ≥ 60, 2–11 tháng ≥ 50, 1–5 tuổi ≥ 40')}.",
   f"{r('Rút lõm lồng ngực')}: phần dưới lồng ngực lõm vào thì hít vào do áp lực âm khoang màng phổi tăng vì phổi giảm đàn hồi.",
   f"{r('Cờ đỏ')}: bỏ bú, nôn tất cả, co giật, li bì, tím tái, thở rên → kích hoạt cấp cứu, không trì hoãn.",
   f"{g('Amoxicillin')} {y('80–90 mg/kg/ngày')} chia 2–3 lần trong {y('5 ngày')}, không dùng {y('40–50 mg/kg')}.",
   f"{r('Không chụp X-quang thường quy')} ở viêm phổi nhẹ ngoại trú."],
  "Năm điều đầu là 'cổng vào': chẩn đoán đúng và kê liều đúng.",
  "Phần 12 Điều 1–5")
B("PED21-B12-03", "B12", 2, "Tóm tắt",
  f"Điều 6–10: nêu {y('nội dung chi tiết')} (trần liều và CCĐ, bẫy nhịp thở chậm, đánh giá 48–72 giờ, nghi tràn mủ, thuốc cấm)?",
  [f"{r('Trần liều')}: Ceftriaxone tối đa {y('2 g/ngày')}; Amoxicillin tối đa {y('2–3 g/ngày')}; CCĐ tuyệt đối Ceftriaxone trẻ sơ sinh {y('&lt; 28 ngày')}.",
   f"{r('Bẫy nhịp thở chậm')}: giảm từ {y('60 xuống 40')} lần/phút kèm li bì = kiệt sức cơ hoành và ứ CO2.",
   f"Kháng sinh cần {y('48–72 giờ')} để hạ sốt; không đổi vội trong 24 giờ đầu nếu trẻ không xấu đi.",
   f"{c('Tràn mủ màng phổi')}: ba giảm (gõ đục, rung thanh giảm, mất rì rào) + sốt cao liên tục sau 48–72 giờ → {g('siêu âm màng phổi khẩn')}.",
   f"{r('Không dùng thuốc ức chế ho hoặc tan đờm')} cho trẻ nhỏ viêm phổi."],
  "Năm điều sau là 'lưới an toàn': ngăn kê đơn nguy hiểm và nhận ra trẻ đang xấu đi.",
  "Phần 12 Điều 6–10")
B("PED21-B12-04", "B12", 2, "Thuật toán", f"{y('⚡ THUẬT TOÁN QUYẾT ĐỊNH')} — {g('Bảng kiểm an toàn tại buồng bệnh')} (Ward Round Checklist): {y('7 câu hỏi')} cần tự hỏi?",
  [f"Đã đếm nhịp thở {y('trọn 60 giây')} khi trẻ nằm yên chưa?", "Đã đo SpO2 khí phòng với sóng mạch chuẩn chưa?",
   f"Có {r('rút lõm lồng ngực, phập phồng cánh mũi hoặc thở rên')} không?", "Trẻ có bú/uống được thuốc không?",
   f"Liều Amoxicillin đã tính đủ {y('80–90 mg/kg/ngày')} chưa?", f"Liều Ceftriaxone có vượt trần {y('2000 mg/ngày')} không?",
   f"Gia đình đã được dặn đủ {r('dấu hiệu cờ đỏ')} cần đi cấp cứu chưa?"],
  "Bảy câu bao phủ ba lớp: đo lường chuẩn, quyết định nhập viện/ngoại trú, và an toàn liều.",
  "Phần 12 Ward Round Checklist", algo=True)

# ───────────────────────── Cloze phụ (giữ lịch sử học) ─────────────────────────
_LEGACY_BASE = 1789470880662
_CLOZES = [
  (0, "B0", "Viêm phổi mắc phải ở cộng đồng (CAP) ở trẻ em là nhiễm trùng cấp tính của nhu mô phổi xảy ra ở trẻ {{c1::không nằm viện trong vòng 14 ngày trước đó}}."),
  (1, "B0", "Theo WHO, dấu hiệu lâm sàng khách quan và nhạy nhất để sàng lọc viêm phổi tại tuyến ban đầu là {{c1::thở nhanh theo lứa tuổi}}."),
  (2, "B3", "Ngưỡng thở nhanh của WHO đối với trẻ dưới 2 tháng tuổi là {{c1::≥ 60 lần/phút}} khi đếm trọn 60 giây lúc trẻ nằm yên."),
  (3, "B3", "Ngưỡng thở nhanh của WHO đối với trẻ từ 2 đến 11 tháng tuổi là {{c1::≥ 50 lần/phút}} khi đếm trọn 60 giây lúc trẻ nằm yên."),
  (4, "B3", "Ngưỡng thở nhanh của WHO đối với trẻ từ 12 đến 59 tháng tuổi (1–5 tuổi) là {{c1::≥ 40 lần/phút}} khi đếm trọn 60 giây lúc trẻ nằm yên."),
  (5, "B3", "Ngưỡng thở nhanh ở trẻ từ 5 tuổi trở lên là {{c1::≥ 30 lần/phút}} khi nằm yên."),
  (6, "B3", "Quy trình đếm nhịp thở chuẩn ở trẻ em bắt buộc phải đếm trọn vẹn trong {{c1::60 giây}}, tuyệt đối không được đếm 15 giây nhân 4."),
  (7, "B0", "Dấu hiệu rút lõm lồng ngực được xác định khi phần dưới lồng ngực (bờ sườn và mũi ức) bị kéo lõm vào trong ở thì {{c1::hít vào}}."),
  (8, "B0", "Tiếng thở rên (Grunting) ở thì thở ra là phản xạ nhằm tạo {{c1::PEEP sinh lý (áp lực dương cuối thì thở ra)}} để chống xẹp phế nang."),
  (9, "B0", "Shunt trong phổi (Intrapulmonary Shunt) xảy ra khi máu mao mạch phổi chảy qua các phế nang bị đông đặc có tỷ lệ {{c1::VA/Q = 0}}."),
  (10, "B0", "Kháng sinh Beta-lactam như Amoxicillin có hiệu quả diệt khuẩn phụ thuộc vào {{c1::thời gian nồng độ thuốc tự do trong máu vượt trên MIC (T > MIC)}}."),
  (11, "B0", "Trần liều người lớn (Adult Ceiling Dose) nghĩa là liều tối đa mg/ngày {{c1::không được phép vượt quá liều khuyến cáo tối đa của người lớn}} ngay cả khi tính theo mg/kg ở trẻ béo phì."),
  (13, "B1", "Khi trẻ có dấu hiệu nôn tất cả mọi thứ sau khi ăn uống, trẻ được xếp vào nhóm {{c1::viêm phổi nặng}} cần nhập viện dùng kháng sinh đường tiêm."),
  (15, "B0", "Tím tái trung ương ở trẻ viêm phổi được quan sát tại vị trí {{c1::môi, lưỡi và niêm mạc khoang miệng}}."),
  (16, "B0", "Ngưỡng SpO2 khí phòng báo động đỏ cần cho thở oxy khẩn cấp theo WHO là {{c1::< 90%}}."),
  (17, "B1", "Theo phân loại WHO (2014), trẻ có ho hoặc khó thở kèm thở nhanh và/hoặc rút lõm lồng ngực nhưng KHÔNG có dấu hiệu nguy hiểm được xếp vào phân loại {{c1::Viêm phổi (Pneumonia) — điều trị ngoại trú}}."),
  (18, "B1", "Theo WHO (2014), trẻ có ho hoặc khó thở kèm theo BẤT KỲ MỘT dấu hiệu nguy hiểm toàn thân hoặc thở rên hoặc tím tái được xếp vào phân loại {{c1::Viêm phổi nặng (Severe Pneumonia) — nhập viện}}."),
  (19, "B1", "Nếu trẻ có ho hoặc khó thở nhưng KHÔNG có thở nhanh và KHÔNG có rút lõm lồng ngực thì không phải viêm phổi mà là {{c1::nhiễm khuẩn hô hấp trên}}."),
  (20, "B1", "Tác nhân vi sinh gây viêm phổi thường gặp ở trẻ sơ sinh dưới 1 tháng tuổi là {{c1::Liên cầu nhóm B (S. agalactiae), E. coli, Listeria monocytogenes và Klebsiella}}."),
  (21, "B1", "Ở trẻ từ 1 đến 3 tháng tuổi, viêm phổi bán cấp do Chlamydia trachomatis đặc trưng bởi bệnh cảnh {{c1::ho dồn dập từng cơn nhưng KHÔNG CÓ SỐT}}."),
  (22, "B1", "Ở trẻ nhỏ từ 3 tháng đến 5 tuổi, virus đường hô hấp chiếm {{c1::60–80%}} tổng số các ca viêm phổi."),
  (23, "B1", "Tác nhân vi khuẩn hàng đầu gây viêm phổi ở trẻ nhỏ từ 3 tháng đến 5 tuổi là {{c1::Streptococcus pneumoniae (Phế cầu khuẩn)}}."),
  (24, "B1", "Tác nhân vi khuẩn không điển hình thường gặp ở trẻ trên 5 tuổi là {{c1::Mycoplasma pneumoniae}} (và Chlamydia pneumoniae)."),
  (26, "B2", "Dịch rỉ viêm trong phế nang làm giảm độ giãn nở của phổi chủ yếu qua cơ chế {{c1::làm mất hoạt tính chất hoạt động bề mặt (Surfactant)}}."),
  (27, "B2", "Khung lồng ngực trẻ nhỏ cấu tạo bằng sụn mềm; áp lực âm thì hít vào gây ra {{c1::rút lõm lồng ngực}} thay vì làm nở phổi."),
  (30, "B2", "Giai đoạn 2 của tràn mủ màng phổi (giai đoạn mủ sợi huyết) đặc trưng bởi fibrin lắng đọng tạo {{c1::các vách ngăn (loculations) trong khoang màng phổi}}."),
  (31, "B2", "Nếu không dẫn lưu mủ kịp thời, tràn mủ màng phổi bước vào giai đoạn 3 (hóa sợi, vỏ bọc) gây biến chứng {{c1::phổi bị giam (Trapped lung)}}."),
  (32, "B2", "Phế cầu khuẩn đề kháng Beta-lactam bằng cách biến đổi các protein gắn Penicillin gồm {{c1::PBP1a, PBP2b và PBP2x}}."),
  (33, "B2", "Liều Amoxicillin thông thường 40–50 mg/kg/ngày chỉ tạo nồng độ đỉnh trong máu khoảng 4–5 µg/mL, không đủ để duy trì {{c1::T > MIC ≥ 40–50%}} đối với phế cầu kháng trung gian."),
  (34, "B2", "Khi nâng liều Amoxicillin lên 80–90 mg/kg/ngày, nồng độ đỉnh trong huyết thanh đạt {{c1::8–10 µg/mL}}."),
  (35, "B3", "Trước khi đếm nhịp thở ở trẻ sốt ≥ 38.5 °C, bước bắt buộc là {{c1::hạ sốt bằng Paracetamol (10–15 mg/kg) và đợi 30–45 phút}}."),
  (39, "B3", "Lý do khiến không chụp X-quang phổi thường quy cho viêm phổi nhẹ ngoại trú: X-quang {{c1::không phân biệt được căn nguyên virus với vi khuẩn}}."),
  (42, "B4", "Trẻ viêm phổi nặng thở nhanh 65 lần/phút rồi giảm còn 40 lần/phút kèm li bì là cạm bẫy {{c1::cải thiện giả do kiệt sức cơ hoành}}."),
  (43, "B4", "Dấu hiệu đầu gật gù theo nhịp thở (Head bobbing) chỉ điểm sự tham gia tối đa của {{c1::cơ ức đòn chũm}} khi cơ hoành sắp kiệt sức."),
  (44, "B4", "Hội chứng ba giảm gợi ý tràn dịch màng phổi gồm: {{c1::gõ đục, rung thanh giảm, rì rào phế nang giảm hoặc mất}}."),
  (45, "B4", "Viêm phổi hoại tử do tụ cầu vàng (CA-MRSA) có X-quang tiến triển trong 24 giờ với xuất hiện {{c1::bóng khí nhu mô phổi (pneumatocele)}}."),
  (47, "B5", "Liều Amoxicillin đường uống cho viêm phổi ngoại trú là {{c1::80–90 mg/kg/ngày}} chia 2 hoặc 3 lần."),
  (48, "B5", "Thời gian dùng Amoxicillin ngoại trú cho viêm phổi đáp ứng tốt là {{c1::5 ngày}}."),
  (49, "B5", "Trần liều tối đa hàng ngày của Amoxicillin đường uống ở trẻ có cân nặng lớn là {{c1::2000–3000 mg/ngày}}."),
  (50, "B5", "Khi chọn Co-amoxiclav liều cao (Amoxicillin 90 mg/kg/ngày), cần chọn tỷ lệ Amoxicillin:Clavulanate là {{c1::7:1 hoặc 8:1}}."),
  (51, "B5", "Azithromycin điều trị viêm phổi không điển hình ở trẻ trên 5 tuổi: ngày 1 uống {{c1::10 mg/kg (tối đa 500 mg)}}, ngày 2 đến ngày 5 uống 5 mg/kg/ngày (tối đa 250 mg)."),
  (52, "B5", "Ampicillin tĩnh mạch đầu tay cho viêm phổi nặng nhập viện có liều {{c1::150–200 mg/kg/ngày chia 4 lần (mỗi 6 giờ)}}."),
  (53, "B5", "Liều Ceftriaxone tĩnh mạch trong viêm phổi nặng ở trẻ em là {{c1::50–80 mg/kg/ngày}} tiêm hoặc truyền 1 lần duy nhất trong ngày."),
  (54, "B5", "Trần liều tối đa tuyệt đối của Ceftriaxone ở trẻ em là {{c1::2 g/ngày (2000 mg/ngày)}}."),
  (55, "B5", "Ceftriaxone bị chống chỉ định tuyệt đối ở trẻ sơ sinh dưới 28 ngày tuổi vì nguy cơ {{c1::vàng da nhân não và kết tủa Calci-Ceftriaxone tại phổi và thận}}."),
  (56, "B5", "Liều Cefotaxime tĩnh mạch trong viêm phổi nặng là {{c1::100–150 mg/kg/ngày chia 3 lần (mỗi 8 giờ)}}."),
  (57, "B5", "Khi nghi viêm phổi hoại tử do CA-MRSA, Vancomycin được phối hợp với liều {{c1::40–60 mg/kg/ngày chia 4 lần truyền chậm}}."),
  (58, "B5", "Nồng độ đáy (trough) của Vancomycin mục tiêu trong viêm phổi tụ cầu nặng là {{c1::15–20 mcg/mL}}."),
  (59, "B5", "Clindamycin được phối hợp trong viêm phổi tụ cầu nặng nhằm {{c1::ức chế tổng hợp độc tố Panton-Valentine Leukocidin (PVL)}}."),
  (60, "B5", "Trong viêm phổi nặng, thể tích dịch truyền tĩnh mạch nên hạn chế ở mức {{c1::80% nhu cầu duy trì cơ bản}}."),
  (62, "B6", "Thời gian tối thiểu để đánh giá đáp ứng lâm sàng của kháng sinh trong viêm phổi trẻ em là {{c1::48 đến 72 giờ}}."),
  (65, "B7", "Thử nghiệm CAP-IT (JAMA 2021) trên 814 trẻ chứng minh Amoxicillin {{c1::3 ngày}} không thua kém 7 ngày về tỷ lệ phải điều trị lại."),
  (66, "B7", "Thử nghiệm SAFER so sánh Amoxicillin 5 ngày với 10 ngày ở trẻ viêm phổi ngoại trú, tỷ lệ khỏi bệnh lâm sàng {{c1::tương đương (88.6% vs 88.5%)}}."),
  (67, "B7", "Nghiên cứu EPIC của CDC Hoa Kỳ cho thấy Mycoplasma pneumoniae {{c1::rất hiếm khi là tác nhân gây viêm phổi nặng ở trẻ dưới 5 tuổi}}."),
  (68, "B8", "Đếm nhịp thở khi trẻ đang khóc hoặc sốt cao 39.5 °C dẫn đến cạm bẫy {{c1::chẩn đoán nhầm viêm phổi và kê đơn oan}} do nhịp thở tăng sinh lý."),
  (69, "B8", "Kê Amoxicillin liều thấp 40–50 mg/kg/ngày cho viêm phổi phế cầu dẫn đến {{c1::thất bại điều trị do không vượt qua MIC của phế cầu kháng trung gian}}."),
  (71, "B8", "Cefixime đường uống không được dùng đầu tay cho viêm phổi vì {{c1::nồng độ trong dịch mô phổi và hoạt tính trên phế cầu kém hơn Amoxicillin}}."),
  (72, "B8", "Thuốc giảm ho trung ương (Codein, Dextromethorphan) bị chống chỉ định vì {{c1::ức chế phản xạ ho, gây ứ đọng dịch mủ trong phế nang}}."),
  (73, "B11", "Thuốc tan đờm đường uống (Acetylcysteine, Ambroxol) không dùng cho trẻ nhỏ vì {{c1::làm tăng lượng đờm loãng nhưng trẻ không đủ lực ho khạc, gây ngập lụt đờm}}."),
  (76, "B9", "Trẻ 3 tuổi nặng 14 kg viêm phổi không nặng ngoại trú: liều Amoxicillin 90 mg/kg/ngày là {{c1::1260 mg/ngày (chia 2 lần, mỗi lần khoảng 600–650 mg)}}."),
  (77, "B9", "Trẻ 9 tuổi nặng 40 kg viêm phổi nặng: tính Ceftriaxone 80 mg/kg/ngày ra 3200 mg, nhưng phải kê ở mức {{c1::2 g/ngày (2000 mg/ngày) do trần liều}}."),
  (78, "B9", "Phương tiện hình ảnh tại giường ưu tiên số 1 để đánh giá tràn dịch màng phổi có vách ngăn ở trẻ viêm phổi sốt dai dẳng là {{c1::siêu âm màng phổi}}."),
  (79, "B10", "Trẻ 14 tháng nặng 10 kg viêm phổi ngoại trú, liều Amoxicillin chuẩn là {{c1::900 mg/ngày (mỗi lần 450 mg × 2 lần/ngày trong 5 ngày)}}."),
  (80, "B10", "Ở trẻ 3 tuổi 14 kg viêm phổi nặng tràn mủ màng phổi, kháng sinh phối hợp bao phủ CA-MRSA bên cạnh Ceftriaxone là {{c1::Vancomycin (60 mg/kg/ngày chia 4 lần truyền chậm)}}."),
  (81, "B10", "Đặt ống dẫn lưu khoang màng phổi kín khi dịch màng phổi có {{c1::mủ đặc hoặc pH < 7.2}}."),
  (87, "B11", "Thở rít (Stridor) nghe rõ ở thì {{c1::hít vào}} (hẹp đường thở trên), còn khò khè (Wheezing) nghe rõ ở thì {{c2::thở ra}} (hẹp đường thở dưới)."),
  (95, "B8", "Nghi tràn mủ màng phổi khi trẻ sốt cao liên tục sau 48–72 giờ dùng kháng sinh kèm {{c1::hội chứng ba giảm (gõ đục, rung thanh giảm, mất âm phế bào)}}."),
  (99, "B5", "Ở trẻ trên 5 tuổi viêm phổi nghi không điển hình (ho dai dẳng, thâm nhiễm kẽ), kháng sinh được dùng là {{c1::Azithromycin (10 mg/kg/ngày)}}."),
]

_counter = {}
for _idx, _sec, _text in _CLOZES:
    _counter[_sec] = _counter.get(_sec, 0) + 1
    _cards.append({
        "id": f"PED21-{_sec}-C{_counter[_sec]:02d}", "type": "cloze", "section": _sec, "text": _text,
        "extra": f"📖 Nguồn: PED-21 — phần {_sec}", "legacy_note_id": _LEGACY_BASE + 2 * _idx,
        "tags": ["PED-21", _sec, "cloze"],
    })

cards_data = _cards
