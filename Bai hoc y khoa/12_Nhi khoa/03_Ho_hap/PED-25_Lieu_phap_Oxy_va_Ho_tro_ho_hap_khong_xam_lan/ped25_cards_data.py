# -*- coding: utf-8 -*-
"""ped25_cards_data.py — Thẻ Anki Master PED-25: Liệu pháp Oxy & Hỗ trợ hô hấp không xâm lấn (Basic-first)."""


def _s(color, t):
    return '<span style="color:%s"><b>%s</b></span>' % (color, t)


def R(t):  # đỏ: cờ đỏ / triệu chứng
    return _s("#ff6b6b", t)


def Y(t):  # vàng: con số / tuổi / phủ định
    return _s("#ffd43b", t)


def G(t):  # xanh lá: xử trí / thuốc / chuẩn vàng
    return _s("#51cf66", t)


def N(t):  # xanh dương: tên bệnh / giải phẫu / phân loại
    return _s("#74c0fc", t)


ALGO = {"badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH", "badge_class": "badge-algo"}
EBM = {"badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG", "badge_class": "badge-ebm"}

_SEC = {
    "B0": "Tổng quan & nền tảng", "B1": "Sinh lý & đích SpO2", "B2": "Oxy dòng thấp",
    "B3": "Cơ chế HFNC", "B4": "Vận hành HFNC", "B5": "nCPAP", "B6": "Bậc thang & chọn thiết bị",
    "B7": "Chỉ số ROX", "B8": "Biến chứng", "B9": "Sai lầm & checkpoint", "B10": "Ca lâm sàng",
    "B11": "Tips thực hành", "B12": "Cai máy & xuất viện", "B13": "Bằng chứng",
}

cards_data = []


def B(cid, tier, front, answers, why, extra, algo=False):
    sec = cid.split("-")[1]
    back = "<b>🎯 Trả lời cốt lõi:</b><br>" + "<br>".join(
        "%d) %s" % (i + 1, a) for i, a in enumerate(answers)
    ) + "<br><br><b>💡 Giải thích của AI:</b><br>" + why
    card = {
        "id": cid, "type": "basic", "track": "ebm", "section": sec, "category": _SEC[sec],
        "tier": tier, "front": front, "back": back, "extra": "📖 Nguồn: " + extra,
        "tags": ["PED-25", sec, "EBM"],
    }
    card.update(ALGO if algo else EBM)
    cards_data.append(card)


def C(cid, sec, text, extra, legacy):
    cards_data.append({
        "id": cid, "type": "cloze", "section": sec, "text": text,
        "extra": "📖 Nguồn: " + extra, "legacy_note_id": legacy,
    })


# =============================== B0 — Tổng quan & nền tảng
B("PED25-B0-01", 1,
  "Vì sao trẻ em " + R("tụt oxy máu rất nhanh") + " khi đường thở tổn thương? Nêu " + Y("3 đặc điểm sinh lý") + " (tiêu thụ O2, FRC, lồng ngực) so với người lớn.",
  ["Tiêu thụ oxy chuyển hóa theo cân nặng: " + Y("6 - 8 mL/kg/phút") + " so với " + Y("3 mL/kg/phút") + " ở người lớn (cao gấp 2 đến 3 lần).",
   "Dung tích cặn chức năng " + N("(FRC)") + " nhỏ.",
   "Lồng ngực có độ giãn nở quá lớn.",
   "Hệ quả: khi đường thở tổn thương hoặc phế nang đông đặc, trẻ có thể tụt oxy máu chỉ trong " + Y("vài phút") + "."],
  "Dự trữ oxy ít mà tiêu thụ lại cao nên đệm an toàn rất mỏng; suy hô hấp là nguyên nhân hàng đầu dẫn đến kiệt sức, ngừng tuần hoàn hô hấp và tử vong.",
  "PED-25 RELEASE v1, mục 0")

B("PED25-B0-02", 1,
  "Liệu pháp oxy và hỗ trợ hô hấp không xâm lấn (NRS) hay bị dùng như can thiệp 'mặc định'. Nêu " + R("2 thái cực sai lầm") + " tại giường và " + G("triết lý điều trị 4 vế") + " của bài.",
  [R("Lạm dụng thụ động:") + " cho thở oxy nồng độ cao bừa bãi, không nắm đích SpO2, không kiểm soát FiO2 → ngộ độc oxy, xẹp phổi hấp thu, co thắt mạch vành/mạch não.",
   R("Trì hoãn mù quáng:") + " tăng vô hạn lưu lượng qua gọng mũi/mặt nạ ở trẻ đã kiệt sức cơ hô hấp → " + R("'thất bại thầm lặng'") + " rồi đặt NKQ trong tình huống ngừng thở hoảng loạn.",
   "Triết lý: " + G("Đúng thiết bị — Đúng lưu lượng — Đúng đích SpO2 — Đánh giá lại liên tục") + " để nâng bậc hoặc hạ bậc kịp thời."],
  "HFNC và nCPAP là nhịp cầu giữa oxy thông thường và thở máy xâm lấn, giúp nhiều trẻ tránh đặt NKQ; nhưng chỉ hiệu quả khi dùng đúng thiết bị, đúng liều và đánh giá lại liên tục.",
  "PED-25 RELEASE v1, mục 0")

B("PED25-B0-03", 1,
  "Liệt kê " + Y("7 khái niệm nền tảng") + " cần nắm trước khi vận hành bất kỳ thiết bị " + N("hỗ trợ hô hấp") + " nào tại giường.",
  [N("FiO2") + " (phân suất oxy trong khí hít vào).",
   N("PEEP") + " (áp lực dương cuối thì thở ra).",
   N("FRC") + " (dung tích cặn chức năng).",
   N("Kháng lực đường thở (Raw)") + " theo định luật Poiseuille.",
   N("Hiệu ứng rửa trôi khoảng chết (CO2 washout)") + ".",
   N("Shunt trong phổi") + ".",
   N("Chỉ số ROX") + "."],
  "Mỗi khái niệm giải thích một lý do chọn thiết bị: PEEP/FRC/shunt → nCPAP; Raw/washout → HFNC; FiO2 → loại thiết bị; ROX → quyết định nâng bậc.",
  "PED-25 RELEASE v1, mục 0.1")

B("PED25-B0-04", 2,
  N("FiO2") + " là gì, " + Y("giá trị trong khí trời") + " là bao nhiêu và " + G("thiết bị nào kiểm soát chính xác") + " còn thiết bị nào bị pha loãng?",
  ["FiO2 = tỷ lệ phần trăm thể tích oxy nguyên chất trong hỗn hợp khí hít vào.",
   "Khí trời: " + Y("0.21 (21%)") + ".",
   "Dụng cụ " + R("dòng thấp") + ": FiO2 thực tế luôn bị pha loãng vì trẻ hít thêm khí trời qua miệng và mũi.",
   "Hệ thống " + G("dòng cao (HFNC) hoặc CPAP kín có buồng trộn (blender)") + ": kiểm soát chính xác từ " + Y("0.21 đến 1.0 (21% đến 100%)") + "."],
  "Vì dòng thấp không đủ đáp ứng dòng hít vào của trẻ nên FiO2 phế nang không cố định; muốn FiO2 chắc chắn phải dùng hệ thống có blender.",
  "PED-25 RELEASE v1, mục 0.1")

B("PED25-B0-05", 2,
  N("PEEP") + ", " + N("FRC") + " và " + N("shunt trong phổi") + ": mỗi khái niệm là gì và " + G("biện pháp duy nhất nào") + " phục hồi FRC / triệt tiêu shunt?",
  [N("PEEP") + ": áp lực duy trì trong đường thở lúc cuối thì thở ra (đơn vị cmH2O), giữ phế nang không xẹp hoàn toàn, ngăn chấn thương xẹp mở chu kỳ (atelectrauma).",
   N("FRC") + ": thể tích khí còn lại sau thở ra bình thường; ở trẻ nhỏ khoảng " + Y("30 mL/kg") + ", sát thể tích đóng phế nang nên dễ xẹp khi giảm thông khí hoặc nằm ngửa.",
   N("Shunt") + ": máu tĩnh mạch qua mao mạch phổi không tiếp xúc phế nang có thông khí (" + Y("V/Q = 0") + "); gặp trong viêm phổi đông đặc, ARDS, xẹp phổi.",
   G("Chỉ có áp lực dương (CPAP/PEEP)") + " mới phục hồi FRC và mở lại phế nang để triệt tiêu shunt."],
  "Shunt lớn làm thiếu oxy máu trơ với oxy dòng thấp vì phế nang đông đặc/xẹp không nhận được khí dù FiO2 cao.",
  "PED-25 RELEASE v1, mục 0.1")

B("PED25-B0-06", 2,
  "Giải thích " + N("kháng lực đường thở (định luật Poiseuille)") + " và " + N("hiệu ứng rửa trôi khoảng chết (CO2 washout)") + ": " + Y("con số then chốt") + " ở trẻ nhũ nhi là gì và dòng khí liên tục giải quyết ra sao?",
  ["Poiseuille: kháng lực tỷ lệ nghịch với " + Y("lũy thừa bậc 4 của bán kính (r^4)") + " → đường thở hẹp ở nhũ nhi làm kháng lực tăng rất mạnh.",
   "Vùng mũi hầu chiếm tới " + Y("50%") + " tổng kháng lực đường thở của nhũ nhi.",
   "Khoảng chết giải phẫu " + N("(VD)") + " chiếm " + Y("VD/VT khoảng 30 - 40%") + " thể tích lưu thông ở trẻ em.",
   G("Dòng khí liên tục") + " quét qua mũi hầu rửa sạch khí giàu CO2 đọng lại, biến hầu họng thành kho dự trữ khí giàu oxy cho nhịp hít vào kế tiếp."],
  "Dòng khí ấm ẩm lưu lượng lớn triệt tiêu kháng lực mũi hầu; đây là nền tảng sinh lý để HFNC giảm công thở.",
  "PED-25 RELEASE v1, mục 0.1")

B("PED25-B0-07", 2,
  R("BOX ĐỎ:") + " Liệt kê " + R("7 cờ đỏ") + " dọa ngừng thở / thất bại hỗ trợ không xâm lấn và " + G("hành động bắt buộc") + " khi có " + Y("bất kỳ 1 dấu hiệu") + ".",
  ["Cơn ngừng thở (apnea) kéo dài " + Y("> 20 giây") + ", hoặc ngừng thở kèm nhịp tim chậm, tím tái tái diễn.",
   R("Rối loạn tri giác cấp:") + " li bì, lơ mơ, hôn mê, không phản ứng với kích thích đau, hoặc vật vã mất bù.",
   R("Kiệt sức cơ hô hấp:") + " nhịp thở chậm bất thường theo tuổi (nhũ nhi thở " + Y("< 20 lần/phút") + " sau giai đoạn thở nhanh co kéo dữ dội), mất co kéo nhưng tím tăng (ngực im lặng - silent chest).",
   R("Toan hô hấp mất bù nặng:") + " pH " + Y("< 7.20") + " và PaCO2 " + Y("> 65 mmHg") + " dù đã tối ưu thông khí không xâm lấn.",
   R("Oxy hóa trơ:") + " SpO2 " + Y("< 88%") + " dù nCPAP với PEEP " + Y("≥ 8 cmH2O") + " và FiO2 " + Y("≥ 60%") + ".",
   R("Huyết động không ổn định:") + " sốc mất bù, tụt huyết áp, nhịp tim chậm tiến triển, cần vận mạch liều cao.",
   R("Tràn khí màng phổi áp lực") + " chưa được dẫn lưu giải áp.",
   "Hành động: " + G("dừng mọi nỗ lực tăng bậc không xâm lấn, đặt nội khí quản thở máy cấp cứu ngay.")],
  "Mỗi dấu hiệu phản ánh não thiếu oxy, toan nặng hoặc cơ hô hấp kiệt sức mà tăng bậc không xâm lấn không đảo ngược được; chần chừ làm tăng nguy cơ ngừng tim lúc đặt ống.",
  "PED-25 RELEASE v1, Box đỏ cấp cứu")

# =============================== B1 — Sinh lý & đích SpO2
B("PED25-B1-01", 1,
  "Phần sinh lý hô hấp trẻ em gồm " + Y("3 nhánh") + " nào cần nhớ để đặt " + G("đích SpO2") + " tại giường?",
  [N("Đặc điểm giải phẫu - sinh lý khác người lớn") + ": thành ngực, cơ hoành, FRC và thể tích đóng.",
   N("Đường cong phân ly oxyhemoglobin") + ": đoạn dốc đứng và đoạn cao nguyên.",
   G("Đích SpO2 mục tiêu theo nhóm bệnh nhân") + " (5 nhóm)."],
  "Hiểu 3 nhánh này giúp biết tại sao tụt oxy nhanh, tại sao SpO2 100% không có nghĩa an toàn và tại sao mỗi nhóm bệnh có đích riêng.",
  "PED-25 RELEASE v1, mục 1")

B("PED25-B1-02", 2,
  "Trẻ nhỏ khác người lớn thế nào về " + N("thành ngực") + ", " + N("cơ hoành") + " (tỷ lệ sợi cơ loại I) và " + N("FRC so với thể tích đóng") + "? Trẻ bù trừ bằng cơ chế gì?",
  [N("Thành ngực:") + " chủ yếu sụn, xương sườn nằm ngang, cơ liên sườn kém → giãn nở rất cao; khi phổi giảm giãn nở, thành ngực lõm vào thì hít vào (co kéo), công thở tăng vọt.",
   N("Cơ hoành") + " là cơ hô hấp chính, sợi loại I (co chậm, kháng mỏi) chỉ " + Y("10 - 25%") + " ở sơ sinh so với " + Y("55%") + " ở người lớn → rất dễ kiệt sức.",
   "FRC " + Y("30 mL/kg") + " rất sát thể tích đóng " + Y("35 mL/kg") + " → đường thở nhỏ ở đáy phổi có xu hướng đóng cuối thì thở ra.",
   "Bù trừ bằng " + G("Auto-PEEP") + ": khép dây thanh thì thở ra (" + R("rên gừ - grunting") + ") hoặc thở nhanh; khi cơ mỏi, Auto-PEEP mất và phổi xẹp hàng loạt."],
  "Rên gừ là nỗ lực tự tạo PEEP; thấy trẻ ngừng rên mà không khá lên là dấu hiệu kiệt sức chứ không phải hồi phục.",
  "PED-25 RELEASE v1, mục 1.1")

B("PED25-B1-03", 2,
  "Trên " + N("đường cong phân ly oxyhemoglobin") + ", đoạn " + R("dốc đứng") + " và đoạn " + Y("cao nguyên") + " ứng với SpO2/PaO2 nào và " + R("nguy cơ") + " ở mỗi đoạn là gì?",
  [N("Đoạn dốc đứng:") + " SpO2 " + Y("< 90%") + " ↔ PaO2 " + Y("< 60 mmHg") + "; PaO2 giảm rất ít cũng làm SpO2 và bão hòa mô tụt nặng → " + R("SpO2 90% là 'bờ vực sinh tử'") + ".",
   N("Đoạn cao nguyên:") + " SpO2 " + Y("> 95%") + " ↔ PaO2 " + Y("> 80 mmHg") + ".",
   "Ở cao nguyên, tăng PaO2 lên " + Y("150 - 300 mmHg") + " (thở oxy 100% kéo dài) chỉ làm SpO2 từ " + Y("98% lên 100%") + " nhưng oxy hòa tan tăng cao gây " + R("ngộ độc oxy mà máy SpO2 không phát hiện") + "."],
  "Đường cong hình chữ S nên SpO2 'đẹp' có thể che giấu tăng oxy máu; vì vậy phải chuẩn độ về khoảng đích chứ không cho oxy tối đa.",
  "PED-25 RELEASE v1, mục 1.2")

B("PED25-B1-04", 1,
  "Nêu " + Y("đích SpO2 mục tiêu") + " cho " + Y("5 nhóm") + ": trẻ bình thường/viêm phổi chung, " + N("viêm tiểu phế quản") + ", " + N("tim bẩm sinh tím shunt Phải - Trái") + ", " + N("tim bẩm sinh phụ thuộc ống động mạch") + ", " + N("trẻ sinh non NICU") + ".",
  ["Trẻ bình thường / viêm phổi chung: " + Y("94 - 98%") + " (PaO2 an toàn 70 - 90 mmHg).",
   "Viêm tiểu phế quản cấp: " + Y("90 - 94%") + " (đích ≥ 90% an toàn, rút ngắn thời gian nằm viện).",
   "Tim bẩm sinh tím có shunt Phải - Trái: " + Y("75 - 85%") + " (hoặc đích riêng).",
   "Tim bẩm sinh phụ thuộc ống động mạch (PDA-dependent): " + Y("80 - 85%") + " (tối đa " + Y("88%") + ").",
   "Sinh non tại NICU: " + Y("91 - 95%") + ", báo động khi " + Y("< 89%") + " hoặc " + Y("> 95%") + "."],
  "Mỗi nhóm có lý do sinh lý riêng: tránh hyperoxia ở trẻ thường, tránh lạm dụng oxy ở bronchiolitis, bảo vệ cân bằng tuần hoàn ở tim bẩm sinh, tránh ROP/BPD ở sinh non.",
  "PED-25 RELEASE v1, mục 1.3")

B("PED25-B1-05", 2,
  "Vì sao " + N("tim bẩm sinh tím shunt Phải - Trái") + ", " + N("tim bẩm sinh phụ thuộc ống động mạch") + " và " + N("trẻ sinh non") + " có đích SpO2 thấp hơn? Điều " + R("cấm tuyệt đối") + " với nhóm phụ thuộc ống động mạch là gì?",
  ["Shunt Phải - Trái: oxy nồng độ cao làm giãn mạch phổi, giảm áp lực phổi, máu lên phổi quá nhiều → " + R("ứ huyết phổi, phù phổi cấp") + " và giảm lưu lượng máu hệ thống.",
   "PDA-dependent: " + R("tuyệt đối cấm oxy 100%") + " vì oxy là chất co mạch cực mạnh trên cơ trơn ống động mạch → ống đóng đột ngột → ngừng tim tử vong.",
   "Sinh non: nguy cơ " + R("bệnh võng mạc trẻ sinh non (ROP)") + " và " + R("loạn sản phế quản phổi (BPD)") + " khi SpO2 " + Y("> 95%") + " kéo dài."],
  "Ở các nhóm này oxy 'thừa' làm thay đổi huyết động hoặc gây độc mô, nên đích thấp là biện pháp bảo vệ chứ không phải chấp nhận thiếu oxy.",
  "PED-25 RELEASE v1, mục 1.3")

B("PED25-B1-06", 2,
  "Lập " + G("bảng bỏ túi") + " đích SpO2 theo nhóm: nhóm nào ứng với khoảng nào (5 dòng) và cảnh báo lâm sàng chính của từng dòng?",
  ["Viêm phổi chung " + Y("94 - 98%") + " → tránh hyperoxia.",
   "Bronchiolitis " + Y("90 - 94%") + " → tránh oxy kéo dài không cần thiết.",
   "Tim tím R-L " + Y("75 - 85%") + " → oxy cao gây phù phổi cấp.",
   "PDA-dependent " + Y("80 - 85% (tối đa 88%)") + " → " + R("cấm oxy 100%") + ".",
   "Sinh non NICU " + Y("91 - 95%") + " (báo động " + Y("< 89% hoặc > 95%") + ") → ROP, BPD."],
  "Bảng này gom khoảng đích và cảnh báo đi kèm để ra quyết định nhanh tại giường mà không phải nhớ cả đoạn lý thuyết.",
  "PED-25 RELEASE v1, mục 1.3", algo=True)

# =============================== B2 — Oxy dòng thấp
B("PED25-B2-01", 1,
  "Hệ thống oxy " + N("dòng thấp") + " gồm " + Y("3 thiết bị") + " nào, mỗi thiết bị đặt " + Y("lưu lượng") + " và cho " + Y("FiO2") + " ra sao?",
  [N("Canula mũi") + ": " + Y("0.5 - 2 L/phút") + " (trẻ nhỏ), " + Y("1 - 4 L/phút") + " (trẻ lớn); FiO2 " + Y("24 - 35%") + ".",
   N("Mặt nạ đơn giản") + ": " + Y("5 - 8 L/phút") + "; FiO2 " + Y("35 - 50%") + ".",
   N("Mặt nạ túi không thở lại (NRM)") + ": " + Y("10 - 15 L/phút") + "; FiO2 " + Y("80 - 95%") + "."],
  "Bậc thang từ canula → mặt nạ đơn giản → NRM tăng dần FiO2 nhưng FiO2 thực tế ở hệ dòng thấp luôn biến thiên vì pha loãng khí trời.",
  "PED-25 RELEASE v1, mục 2")

B("PED25-B2-02", 2,
  "Định nghĩa hệ thống " + N("dòng thấp") + " bằng " + Y("lưu lượng đỉnh hít vào (PIFR)") + ", cho ví dụ nhũ nhi " + Y("10 kg") + " và nêu " + Y("3 yếu tố") + " làm FiO2 phế nang thay đổi.",
  ["Dòng thấp = lưu lượng thiết bị cung cấp " + Y("thấp hơn PIFR") + " của trẻ.",
   "Ví dụ: nhũ nhi 10 kg có VT khoảng " + Y("70 mL") + ", Ti khoảng " + Y("0.4 giây") + ", PIFR " + Y("10 - 15 L/phút") + "; canula " + Y("1 - 2 L/phút") + " chỉ đáp ứng một phần nhỏ, phần còn lại trẻ hít khí trời bù.",
   "FiO2 phế nang phụ thuộc: " + N("tần số thở và thể tích lưu thông") + "; " + N("tỷ lệ Ti/Te") + "; " + N("thở miệng hay thở mũi") + "."],
  "Trẻ thở càng nhanh, càng hít miệng thì khí trời pha loãng càng nhiều; vì vậy tăng lưu lượng canula không tạo FiO2 cao.",
  "PED-25 RELEASE v1, mục 2.1")

B("PED25-B2-03", 2,
  N("Canula mũi") + ": " + Y("lưu lượng quy chuẩn theo tuổi") + " (sơ sinh/nhũ nhi/trẻ lớn), " + G("ưu điểm") + " và " + R("hạn chế") + " khi vượt " + Y("2 L/phút") + "?",
  ["Sơ sinh " + Y("0.25 - 1.0 L/phút") + " (lưu lượng kế vi thể " + Y("0.1 - 1 L/phút") + "); nhũ nhi " + Y("0.5 - 2.0 L/phút") + "; trẻ lớn " + Y("1.0 - 4.0 L/phút") + ".",
   G("Ưu điểm:") + " tiện, rẻ, dung nạp tốt, không cản ăn bú/giao tiếp, ít sợ ngột ngạt hơn mặt nạ.",
   R("Hạn chế:") + " > 2 L/phút ở trẻ nhỏ → khí lạnh khô gây kích ứng, khô rát mũi, chảy máu cam, co thắt phế quản phản xạ; không cung cấp được FiO2 cao khi suy hô hấp nặng."],
  "Khoang mũi hầu chỉ là buồng chứa nhỏ (khoảng 1 - 2 mL/kg) nên canula không thể là phương tiện cho suy hô hấp nặng.",
  "PED-25 RELEASE v1, mục 2.2")

B("PED25-B2-04", 2,
  N("Mặt nạ đơn giản") + ": " + Y("lưu lượng bắt buộc") + ", " + Y("FiO2") + " và " + R("điều cấm tuyệt đối") + " về lưu lượng cùng " + R("hậu quả") + "?",
  ["Lưu lượng bắt buộc " + Y("5 - 8 L/phút") + ", FiO2 khoảng " + Y("35 - 50%") + ".",
   R("CẤM cài lưu lượng < 5 L/phút") + ".",
   "Lý do: dòng vào không đủ quét khí thở ra ra khỏi lỗ thoát; buồng mặt nạ (" + Y("100 - 200 mL") + ") thành khoảng chết khổng lồ → trẻ hít lại CO2 → " + R("toan hô hấp tăng carbonic cấp") + ".",
   "Muốn dùng dòng thấp phải đổi sang " + G("gọng mũi canula") + "."],
  "Mặt nạ cần dòng đủ lớn để rửa buồng; canula không có buồng chứa khí chết nên an toàn ở dòng thấp.",
  "PED-25 RELEASE v1, mục 2.3 và sai lầm 2")

B("PED25-B2-05", 2,
  N("Mặt nạ túi không thở lại (NRM)") + ": " + Y("3 thành phần cấu tạo") + ", " + Y("lưu lượng - FiO2 - dấu hiệu túi") + " và " + G("chỉ định") + "?",
  ["Cấu tạo: (1) túi dự trữ; (2) " + N("van một chiều giữa túi và mặt nạ") + " (mở khi hít vào, đóng khi thở ra); (3) " + N("van một chiều ở lỗ thoát hai bên") + " (mở khi thở ra, đóng khi hít vào).",
   "Lưu lượng " + Y("10 - 15 L/phút") + ", giữ túi luôn căng ít nhất " + Y("2/3") + " thể tích; FiO2 " + Y("80 - 95%") + ".",
   G("Chỉ định:") + " suy hô hấp giảm oxy máu nặng, sốc mất bù, ngộ độc CO, phù phổi cấp, hoặc làm cầu nối trong khi chuẩn bị đặt NKQ.",
   "Nhược điểm: cần nguồn dòng lớn, chỉ dùng ngắn hạn."],
  "Hai nhóm van làm FiO2 gần tối đa vì ngăn khí thở ra vào túi và ngăn khí trời lọt vào; túi xẹp nghĩa là dòng không đủ.",
  "PED-25 RELEASE v1, mục 2.4")

B("PED25-B2-06", 2,
  "Lập " + G("bảng bỏ túi 3 thiết bị dòng thấp") + ": lưu lượng, FiO2 và " + R("bẫy lâm sàng") + " của canula, mặt nạ đơn giản và NRM.",
  ["Canula: " + Y("0.5 - 2 L/phút (nhỏ), 1 - 4 (lớn)") + "; " + Y("24 - 35%") + "; " + R("khô niêm mạc nếu > 2 L/phút, FiO2 không ổn định") + ".",
   "Mặt nạ đơn giản: " + Y("5 - 8 L/phút") + "; " + Y("35 - 50%") + "; " + R("ứ CO2 nếu dòng < 5 L/phút") + ".",
   "NRM: " + Y("10 - 15 L/phút") + "; " + Y("80 - 95%") + "; " + R("túi phải luôn phồng ≥ 2/3, chỉ dùng ngắn hạn") + "."],
  "Ba dòng này là bảng tra nhanh khi chọn thiết bị theo mức nặng của suy hô hấp.",
  "PED-25 RELEASE v1, mục 2.4 (bảng tổng hợp)", algo=True)

B("PED25-B2-07", 2,
  "Mô hình sinh lý bệnh " + Y("5 tầng") + " của suy hô hấp giảm oxy ở trẻ em đi theo thứ tự nào?",
  ["Tầng 1: " + R("viêm phù nề, tắc nghẽn đường thở nhỏ") + " hoặc đông đặc phế nang.",
   "Tầng 2: mất cân xứng " + N("V/Q") + " và tăng " + N("shunt nội phổi") + ".",
   "Tầng 3: " + N("FRC") + " giảm xuống dưới thể tích đóng của phổi.",
   "Tầng 4: tăng công hô hấp bù trừ → kiệt sức cơ hoành và cơ liên sườn.",
   "Tầng 5: giảm thông khí phế nang toàn bộ, toan hô hấp hỗn hợp, " + R("ngừng thở - ngừng tim") + "."],
  "Mỗi thiết bị can thiệp vào một tầng: HFNC chủ yếu tầng 1 và 4, nCPAP chủ yếu tầng 2 và 3.",
  "PED-25 RELEASE v1, mục 2 (mô hình 5 tầng)")

# =============================== B3 — Cơ chế HFNC
B("PED25-B3-01", 1,
  "HFNC là gì (" + Y("3 thành phần") + ") và có " + Y("5 cơ chế") + " sinh lý bệnh nào giải thích hiệu quả?",
  ["Bản chất: hệ thống khí thở hoàn chỉnh = " + G("lưu lượng vượt đỉnh hít vào + kiểm soát chính xác FiO2 qua blender + sưởi ấm làm ẩm bão hòa chủ động") + ".",
   "5 cơ chế: (1) " + N("sưởi ấm 37°C và làm ẩm bão hòa") + "; (2) " + N("rửa trôi khoảng chết mũi hầu (CO2 washout)") + "; (3) " + N("triệt tiêu kháng lực đường thở thì hít vào") + "; (4) " + N("tạo PEEP động") + "; (5) " + N("tăng dung nạp và tương tác lâm sàng") + "."],
  "HFNC không đơn thuần là oxy lưu lượng lớn; thiếu bất kỳ thành phần nào (đặc biệt làm ẩm nhiệt) sẽ mất hiệu quả hoặc gây hại.",
  "PED-25 RELEASE v1, mục 3")

B("PED25-B3-02", 2,
  "Cơ chế 1 của HFNC: " + Y("nhiệt độ và độ ẩm chuẩn") + ", vì sao khí khô lạnh " + R("gây hại") + " và " + G("chuỗi tác động") + " của khí ấm ẩm?",
  ["Chuẩn: " + Y("37°C") + ", " + Y("100% độ ẩm tương đối (44 mg H2O/L khí)") + ".",
   "Khí khô lạnh làm tê liệt biểu mô lông chuyển, mất nước lớp nhầy → dịch tiết cô đặc thành " + R("nút nhầy tắc đường thở nhỏ") + ".",
   "Chuỗi: " + G("khí ấm ẩm → bảo tồn thang máy lông chuyển → làm loãng đờm, chống nút nhầy → giảm tiêu hao năng lượng chuyển hóa sưởi ấm khí") + "."],
  "Khi HFNC trả lại điều kiện phế nang sinh lý, trẻ không phải tốn năng lượng sưởi ấm khí và đờm không đóng vón.",
  "PED-25 RELEASE v1, mục 3.1")

B("PED25-B3-03", 2,
  "Cơ chế 2 của HFNC: " + N("khoang mũi hầu") + " gây vấn đề gì lúc cuối thì thở ra và " + G("rửa trôi CO2") + " giúp ích ra sao?",
  ["Cuối thì thở ra khoang mũi hầu chứa đầy khí phế nang giàu CO2; nhịp hít vào kế tiếp trẻ " + R("hít lại toàn bộ khí này") + " trước khi khí mới vào phổi.",
   "HFNC thổi dòng khí cao liên tục, quét sạch CO2 cũ ra qua miệng hoặc khe quanh lỗ mũi.",
   "Chuỗi: " + G("dòng khí cao liên tục → rửa sạch CO2 hầu họng → hầu họng thành kho dự trữ khí giàu O2 → tăng hiệu quả thông khí phế nang, giảm công thở thông khí phút") + "."],
  "Vì khoảng chết chiếm 30 - 40% thể tích lưu thông ở trẻ, giảm khoảng chết hiệu dụng giúp giảm công thở rõ rệt.",
  "PED-25 RELEASE v1, mục 3.2")

B("PED25-B3-04", 2,
  "Cơ chế 3 của HFNC: " + R("hậu quả khi dòng thiết bị không đáp ứng đỉnh hít vào") + " và " + Y("mức lưu lượng") + " HFNC cần đạt để " + G("triệt tiêu kháng lực mũi hầu") + "?",
  ["Khi suy hô hấp, lưu lượng đỉnh hít vào tăng vọt; nếu thiết bị không đáp ứng, trẻ dùng cơ hô hấp phụ co kéo, tạo " + R("áp lực âm lồng ngực rất lớn làm hẹp đường thở trên") + ".",
   "HFNC cung cấp lưu lượng bằng hoặc vượt PIFR: " + Y("1.5 - 2 L/kg/phút") + ".",
   "Kết quả: trẻ không cần gắng sức hút khí, " + G("triệt tiêu kháng lực đường thở vùng mũi hầu") + "."],
  "Dòng đáp ứng tức thì nhu cầu phế nang nên không còn áp lực âm gây xẹp đường thở trên.",
  "PED-25 RELEASE v1, mục 3.3")

B("PED25-B3-05", 2,
  "Cơ chế 4 của HFNC: vì sao hệ thống " + N("mở") + " vẫn tạo " + N("PEEP động") + ", " + Y("mức PEEP") + " bao nhiêu (kể cả khi ngậm miệng) và " + G("chuỗi lợi ích") + "?",
  ["Ma sát giữa dòng khí vào và luồng khí thở ra qua khe mũi cản dòng thở ra → áp lực dương cuối thì thở ra (" + N("Dynamic PEEP") + ").",
   "PEEP khoảng " + Y("2 - 4 cmH2O") + "; khi trẻ ngậm miệng có thể " + Y("5 - 6 cmH2O") + ".",
   "Chuỗi: " + G("giữ phế nang không xẹp cuối thở ra → tăng FRC → cải thiện V/Q và oxy hóa máu") + "."],
  "PEEP động nhẹ nên HFNC hợp với tắc nghẽn đường thở nhỏ hơn là xẹp phế nang nặng cần PEEP thật.",
  "PED-25 RELEASE v1, mục 3.4")

B("PED25-B3-06", 2,
  "Cơ chế 5 của HFNC: " + G("lợi thế dung nạp") + " so với mặt nạ CPAP và " + G("vì sao nó làm giảm tiêu thụ oxy") + "?",
  ["Gọng mũi nhỏ gọn mềm mại; mặt nạ CPAP ôm chặt gây " + R("đau rát, loét sống mũi, cản trở hoàn toàn ăn uống") + ".",
   "Trẻ HFNC vẫn bú mẹ, uống sữa, nói chuyện, tương tác với cha mẹ.",
   "Giảm stress tâm lý, giảm kích thích vật vã → " + G("giảm trực tiếp tiêu thụ oxy toàn thân") + "."],
  "Trẻ yên tĩnh tiêu thụ ít oxy hơn, nên dung nạp tốt cũng là cơ chế điều trị chứ không chỉ là sự thoải mái.",
  "PED-25 RELEASE v1, mục 3.5")

# =============================== B4 — Vận hành HFNC
B("PED25-B4-01", 1,
  "Quy trình HFNC tại giường gồm " + Y("4 phần") + " nào (cài lưu lượng, FiO2, nhiệt ẩm, cai) và nguyên tắc vàng khi cai là gì?",
  [G("Lưu lượng khởi đầu") + " theo cân nặng (≤ 10 kg và > 10 kg).",
   G("FiO2 khởi đầu và chuẩn độ") + " về đích SpO2.",
   G("Nhiệt ẩm") + " 37°C bằng buồng ẩm có dây đốt nhiệt.",
   G("Cai 2 bước:") + " " + Y("cai FiO2 trước — cai lưu lượng sau") + "."],
  "Lưu lượng tạo PEEP động và washout nên được giữ đến cuối; FiO2 là biến số nên hạ trước.",
  "PED-25 RELEASE v1, mục 4")

B("PED25-B4-02", 2,
  "Tính " + Y("lưu lượng HFNC khởi đầu") + " cho trẻ " + Y("≤ 10 kg") + " và trẻ " + Y("> 10 kg") + ", " + Y("ví dụ trẻ 14 kg") + " và " + Y("giới hạn tối đa") + "?",
  ["≤ 10 kg: " + Y("1.5 - 2.0 L/kg/phút") + " (thông dụng bắt đầu ngay " + Y("2.0 L/kg/phút") + " để đạt PEEP và washout tối ưu).",
   "> 10 kg: " + G("2.0 L/kg/phút cho 10 kg đầu + 0.5 L/kg/phút cho mỗi kg vượt trên 10 kg") + ".",
   "Ví dụ 14 kg: 10 × 2 + 4 × 0.5 = 20 + 2 = " + Y("22 L/phút") + ".",
   "Giới hạn tối đa: thông thường " + Y("50 - 60 L/phút") + " ở trẻ vị thành niên."],
  "Công thức bậc thang tránh cho trẻ lớn lưu lượng quá cao tính thẳng theo cân nặng.",
  "PED-25 RELEASE v1, mục 4.1")

B("PED25-B4-03", 2,
  "Lập " + G("công cụ tính lưu lượng HFNC bỏ túi") + ": 2 nhánh cân nặng, " + Y("ví dụ 14 kg") + " và ví dụ " + Y("7 kg") + " của ca lâm sàng.",
  ["≤ 10 kg: " + Y("2.0 L/kg/phút") + " × cân nặng; ví dụ 7.0 kg → " + Y("14.0 L/phút") + ".",
   "> 10 kg: " + Y("2.0 × 10 + 0.5 × (cân nặng − 10)") + "; ví dụ 14 kg → " + Y("22 L/phút") + ".",
   "Trần lưu lượng " + Y("50 - 60 L/phút") + "."],
  "Bảng tra nhanh này gom hai nhánh tính để cài máy đúng liều ngay từ đầu.",
  "PED-25 RELEASE v1, mục 4.1 và ca lâm sàng 1", algo=True)

B("PED25-B4-04", 2,
  "HFNC: " + Y("FiO2 khởi đầu") + ", cách " + G("chuẩn độ") + " (bước và nhịp), " + Y("đích SpO2") + " và " + Y("nhiệt độ") + " cài đặt?",
  ["FiO2 khởi đầu " + Y("40 - 60%") + " (cao hơn nếu trẻ tím tái nặng).",
   "Chuẩn độ tăng/giảm " + Y("5 - 10% mỗi 10 - 15 phút") + ".",
   "Đích SpO2 " + Y("92 - 96%") + " (" + Y("90 - 94%") + " ở viêm tiểu phế quản).",
   "Nhiệt độ " + Y("37°C") + " với buồng ẩm có dây đốt nhiệt."],
  "Chuẩn độ từng bước tránh vừa thiếu oxy vừa tăng oxy máu; đích riêng của bronchiolitis thấp hơn để tránh lạm dụng oxy.",
  "PED-25 RELEASE v1, mục 4.2")

B("PED25-B4-05", 2,
  "Quy trình " + G("cai HFNC 2 bước") + ": " + Y("điều kiện, nhịp giảm") + " từng bước của FiO2 rồi lưu lượng và " + Y("mức FiO2 an toàn") + " trước khi đụng vào lưu lượng?",
  ["Bước 1 " + G("cai FiO2") + ": khi trẻ ổn định (nhịp thở giảm, hết co kéo, SpO2 ổn trong đích) hạ FiO2 " + Y("5% mỗi 1 - 2 giờ") + ".",
   "Mục tiêu: FiO2 " + Y("≤ 30 - 40%") + " trước khi chạm vào lưu lượng.",
   "Bước 2 " + G("cai lưu lượng") + ": khi FiO2 ≤ 30 - 40% và trẻ thoải mái, giảm " + Y("0.5 L/kg/phút mỗi 2 - 4 giờ") + ".",
   "Nguyên tắc: " + Y("một thông số tại một thời điểm") + "."],
  "Lưu lượng tạo PEEP động và washout; cắt dòng sớm khi phổi chưa hồi phục làm phế nang xẹp lại và công thở tăng vọt.",
  "PED-25 RELEASE v1, mục 4.3 và sai lầm 5")

B("PED25-B4-06", 2,
  Y("Ngưỡng ngừng HFNC") + ": lưu lượng và FiO2 phải đạt bao nhiêu, và " + G("chuyển sang") + " phương thức nào?",
  ["Lưu lượng " + Y("≤ 0.5 L/kg/phút") + " (hoặc tổng lưu lượng " + Y("< 4 L/phút") + " ở nhũ nhi).",
   "FiO2 " + Y("≤ 30%") + ".",
   "Ngắt HFNC → " + G("canula mũi thông thường hoặc khí trời hoàn toàn") + "."],
  "Ở ngưỡng này PEEP động và washout gần như không còn đáng kể nên trẻ có thể tự đảm nhận công thở.",
  "PED-25 RELEASE v1, mục 4.3")

# =============================== B5 — nCPAP
B("PED25-B5-01", 1,
  "nCPAP khác HFNC ở bản chất nào, có " + Y("4 tác động sinh lý") + " nào, hệ thống " + N("Bubble CPAP") + " là gì và " + G("cài đặt khởi đầu") + " gồm những gì?",
  ["nCPAP là phương thức " + N("kín") + " duy trì áp lực dương cố định suốt cả thì hít vào lẫn thở ra khi trẻ tự thở (HFNC là hệ mở dựa vào lưu lượng).",
   "4 tác động: phục hồi thể tích phổi/FRC; tối ưu V/Q; giảm công thở; hỗ trợ huyết động suy tim.",
   N("Bubble CPAP") + ": khí thở ra sục qua cột nước, PEEP theo chiều sâu.",
   G("Cài đặt:") + " PEEP khởi đầu " + Y("4 - 5 cmH2O") + ", FiO2 " + Y("40 - 60%") + ", dòng nguồn " + Y("6 - 10 L/phút") + "."],
  "Áp lực dương thật là điểm khác biệt cho phép nCPAP mở phế nang xẹp/đông đặc mà HFNC không làm được.",
  "PED-25 RELEASE v1, mục 5")

B("PED25-B5-02", 2,
  "Nêu " + Y("4 tác động sinh lý") + " quyết định của " + N("nCPAP") + " và vì sao nCPAP " + G("có lợi ở bệnh nhân suy tim") + ".",
  [G("Phục hồi thể tích phổi và FRC:") + " áp lực xuyên phổi liên tục thắng lực căng bề mặt, mở lại phế nang xẹp và giữ không xẹp lại cuối thở ra.",
   G("Tối ưu V/Q:") + " mở rộng diện tích phế nang trao đổi khí, giảm shunt từ vùng đông đặc/xẹp.",
   G("Giảm công thở:") + " đưa phổi về đoạn dốc tối ưu của đường cong áp lực - thể tích, nơi độ giãn nở cao nhất.",
   G("Hỗ trợ huyết động:") + " áp lực dương giảm áp lực xuyên thành thất trái → " + Y("giảm hậu gánh thất trái") + " (phù phổi huyết động, suy tim sung huyết)."],
  "Ở độ giãn nở tối ưu, cơ hoành cần ít lực hơn để tạo cùng thể tích lưu thông, nên công thở giảm.",
  "PED-25 RELEASE v1, mục 5.1")

B("PED25-B5-03", 2,
  N("Bubble CPAP") + ": " + Y("độ sâu cột nước") + " quyết định gì, " + Y("tần số dao động áp lực") + " bao nhiêu và vì sao " + G("tăng thải CO2 và oxy hóa") + "?",
  ["Khí thở ra sục vào cột nước sâu " + Y("4 - 8 cm") + "; " + Y("1 cm nước = 1 cmH2O") + " PEEP.",
   "Bọt khí vỡ liên tục tạo " + N("dao động áp lực vi thể") + " tần số " + Y("15 - 30 Hz") + ".",
   "Sóng dao động lan ngược vào phế nang, hòa trộn khí tương tự HFOV → tăng khuếch tán CO2 và oxy hóa " + G("mà không cần tăng áp lực đỉnh") + "."],
  "Bubble CPAP được mô tả là hiệu quả trao đổi khí vượt trội so với CPAP van cơ học nhờ cơ chế dao động áp lực.",
  "PED-25 RELEASE v1, mục 5.2")

B("PED25-B5-04", 2,
  "Cài đặt " + G("nCPAP") + ": " + N("giao diện") + ", " + Y("PEEP khởi đầu") + ", " + G("chuẩn độ") + ", PEEP tối ưu/tối đa, FiO2 và " + Y("dòng nguồn") + "?",
  ["Giao diện: gọng mũi ngắn hai lỗ hoặc mặt nạ mũi, vừa khít không rò khí.",
   "PEEP khởi đầu " + Y("4 - 5 cmH2O") + ".",
   "Còn co kéo, SpO2 chưa đạt → tăng " + Y("1 cmH2O mỗi 15 - 30 phút") + ".",
   "PEEP tối ưu " + Y("5 - 7 cmH2O") + "; tối đa " + Y("8 cmH2O") + " (vượt mức này tăng " + R("chấn thương áp lực, cản máu tĩnh mạch về tim") + ").",
   "FiO2 " + Y("40 - 60%") + ", đích SpO2 " + Y("92 - 96%") + "; dòng nguồn " + Y("6 - 10 L/phút") + " để cột nước sục liên tục ngay cả khi trẻ hít vào gắng sức."],
  "Tăng PEEP từng bước nhỏ cho phép đánh giá đáp ứng mà không vượt ngưỡng gây hại huyết động.",
  "PED-25 RELEASE v1, mục 5.3")

# =============================== B6 — Bậc thang & chọn thiết bị
B("PED25-B6-01", 1,
  "Vẽ " + G("bậc thang nâng bậc hỗ trợ hô hấp") + " từ khí trời: " + Y("tiêu chí thất bại canula") + ", hai nhánh đầu tay, " + Y("thời điểm đánh giá lại") + " và điểm cuối khi thất bại.",
  ["Khí trời (SpO2 " + Y("< 92 - 94%") + ", thở nhanh nhẹ) → canula " + Y("0.5 - 2 L/phút, FiO2 24 - 35%") + "; đáp ứng thì duy trì rồi giảm dần.",
   "Thất bại canula: SpO2 " + Y("< 92%") + ", co kéo ngực tăng, thở nhanh tăng → chọn nhánh theo bệnh sinh (" + N("HFNC") + " hoặc " + N("nCPAP") + ").",
   "Đánh giá lại tại " + Y("1 - 2 giờ") + " bằng ROX và khí máu.",
   "Thành công (ROX ≥ 4.88): duy trì và cai dần; thất bại (ROX < 3.85, toan hô hấp tăng, kiệt sức cơ) → " + R("đặt NKQ thở máy cấp cứu") + "."],
  "Lưu đồ giữ nguyên tắc 'đánh giá lại liên tục' để nâng bậc đúng lúc thay vì tăng lưu lượng vô hạn.",
  "PED-25 RELEASE v1, mục 6")

B("PED25-B6-02", 2,
  "Bệnh nào " + N("ưu tiên HFNC đầu tay") + " và bệnh nào " + N("ưu tiên nCPAP đầu tay") + "? Kèm " + Y("thông số khởi đầu") + " của mỗi nhánh.",
  [N("HFNC:") + " viêm tiểu phế quản cấp; khò khè tắc nghẽn đường thở nhỏ; trẻ kích thích cần bú mẹ; lưu lượng " + Y("1.5 - 2 L/kg/phút") + ".",
   N("nCPAP:") + " viêm phổi thùy đông đặc nặng; xẹp phổi diện rộng; phù phổi cấp huyết động / ARDS; PEEP " + Y("4 - 6 cmH2O") + "."],
  "Tắc nghẽn đường thở nhỏ và tăng khoảng chết cần dòng/washout; xẹp phế nang và shunt lớn cần PEEP thật.",
  "PED-25 RELEASE v1, mục 6 (lưu đồ)")

B("PED25-B6-03", 2,
  "Bảng phân định " + N("HFNC") + " hay " + N("nCPAP") + " đầu tay theo " + Y("4 tiêu chí") + ": bệnh lý điển hình, cơ chế bệnh sinh, mức hợp tác của trẻ, dung nạp & biến chứng.",
  ["Bệnh lý: HFNC — viêm tiểu phế quản cấp, croup sau rút ống, khò khè hen nhẹ - vừa; nCPAP — viêm phổi nặng đông đặc, xẹp phổi phế nang, phù phổi, ARDS nhi khoa.",
   "Bệnh sinh: HFNC — tắc nghẽn đường thở nhỏ do đờm, tăng kháng lực mũi hầu, tăng khoảng chết; nCPAP — xẹp phế nang hàng loạt, shunt lớn, giảm FRC trầm trọng.",
   "Hợp tác: HFNC — trẻ bứt rứt, sợ mặt nạ, cần bú; nCPAP — trẻ chấp nhận đeo mặt nạ chặt, có thể đặt sonde dạ dày giải áp.",
   "Dung nạp: HFNC — dung nạp rất cao (" + Y("> 90%") + "), ít tổn thương da mũi; nCPAP — " + R("dễ loét vách ngăn mũi, chướng bụng") + ", cần theo dõi điều dưỡng sát."],
  "Chọn theo bệnh sinh trước, rồi mới theo mức hợp tác của trẻ.",
  "PED-25 RELEASE v1, mục 6 (bảng phân định)")

B("PED25-B6-04", 2,
  "Trẻ đang HFNC liều tối ưu " + Y("2 L/kg/phút") + ", FiO2 " + Y("60%") + " không cải thiện sau " + Y("2 giờ") + ": khi nào " + G("chuyển nCPAP") + " và khi nào " + R("đặt NKQ ngay") + "?",
  [G("Chuyển nCPAP") + " khi: trẻ còn tỉnh táo; cơ hô hấp chưa kiệt (còn thở nhanh, co kéo bù trừ tốt); không toan nặng (" + Y("pH > 7.25") + "); bệnh nền là xẹp phổi hoặc đông đặc phế nang cần PEEP thật.",
   R("Đặt NKQ ngay") + " khi: kiệt sức cơ hô hấp (thở chậm dần, cơn ngừng thở ngắn); toan mất bù nặng (" + Y("pH < 7.20, PaCO2 > 65 mmHg") + "); rối loạn tri giác (li bì, không tiếp xúc); hoặc ARDS nặng tiến triển nhanh.",
   "Chuyển nCPAP trong nhóm thứ hai chỉ " + R("mất thời gian quý và dẫn đến ngừng thở đột ngột") + "."],
  "Quyết định chia đôi: còn dự trữ cơ hô hấp thì thử nCPAP; đã kiệt sức thì không còn thời gian cho thử nghiệm.",
  "PED-25 RELEASE v1, mục 10 (checkpoint 4)", algo=True)

# =============================== B7 — ROX
B("PED25-B7-01", 1,
  "Chỉ số " + N("ROX") + ": " + Y("công thức") + ", " + Y("quy đổi đơn vị") + ", " + Y("ví dụ") + " và " + Y("3 vùng ngưỡng") + " dự báo?",
  ["ROX = " + Y("(SpO2 / FiO2) ÷ tần số thở (lần/phút)") + "; SpO2 theo % (95%→95), FiO2 dạng thập phân (40%→0.40).",
   "Ví dụ SpO2 94%, FiO2 0.50, thở 40 lần/phút: (94 / 0.50) / 40 = 188 / 40 = " + Y("4.70") + ".",
   "Ngưỡng: " + G("≥ 4.88 an toàn") + "; " + Y("3.85 - 4.88 cảnh báo xám") + "; " + R("< 3.85 báo động thất bại") + "."],
  "ROX tính tại giường không cần máu, gộp oxy hóa máu và công thở trong một con số.",
  "PED-25 RELEASE v1, mục 7.1")

B("PED25-B7-02", 2,
  "Ý nghĩa sinh học của " + N("tử số") + " và " + N("mẫu số") + " trong ROX, và vì sao ROX " + G("tăng vọt") + " ở trẻ đáp ứng tốt còn " + R("sụt giảm") + " ở trẻ thất bại?",
  ["Tử số (" + Y("SpO2/FiO2") + ") phản ánh mức oxy hóa máu.",
   "Mẫu số (" + Y("tần số thở") + ") phản ánh công thở bù trừ.",
   "Đáp ứng tốt: oxy hóa tăng (tử số tăng) và nhịp thở chậm lại (mẫu số giảm) → ROX tăng vọt.",
   "Thất bại: oxy hóa tụt trong khi thở dồn dập → " + R("ROX sụt giảm nghiêm trọng") + "."],
  "Vì có tần số thở trong công thức, ROX phát hiện được thất bại thầm lặng mà SpO2 đơn độc bị FiO2 che đậy.",
  "PED-25 RELEASE v1, mục 7.1")

B("PED25-B7-03", 2,
  "ROX nên được đo ở " + Y("4 mốc thời gian") + " nào, và " + Y("3 vùng ngưỡng") + " kèm " + G("hành động") + " tương ứng là gì?",
  ["Mốc đo: " + Y("0h, 2h, 6h, 12h") + ".",
   G("An toàn (ROX ≥ 4.88):") + " thành công cao (> 85%), không nâng bậc, tiếp tục và chuẩn bị cai.",
   Y("Cảnh báo xám (3.85 ≤ ROX < 4.88):") + " theo dõi sát mỗi giờ, kiểm tra vị trí gọng mũi, hút sạch đờm hầu họng, xem xét tăng nhẹ lưu lượng hoặc PEEP.",
   R("Báo động (ROX < 3.85)") + ", đặc biệt sau " + Y("2 - 6 giờ") + " hoặc xu hướng tụt dốc liên tục: chuẩn bị kíp đặt NKQ cấp cứu ngay, không trì hoãn."],
  "Xu hướng qua các mốc có giá trị hơn một giá trị đơn lẻ; tụt dốc là tín hiệu sớm của thất bại.",
  "PED-25 RELEASE v1, mục 7.2")

B("PED25-B7-04", 2,
  "Lập " + G("bộ giải mã ROX bỏ túi") + ": ví dụ HFNC " + Y("ROX 4.35 → 3.25 ở 2 giờ") + " nghĩa là gì và " + G("xử trí") + " ra sao?",
  ["Mốc 0h: SpO2 94%, thở 48 lần/phút → ROX " + Y("4.35") + ".",
   "Mốc 2h: SpO2 93%, thở 52 lần/phút, FiO2 phải tăng lên 55% → ROX " + Y("3.25") + " (< 3.85) → " + R("thất bại sớm với HFNC") + ".",
   "Xử trí: " + G("không tăng FiO2 lên 70 - 80% để chờ; hội chẩn hồi sức; chuyển nCPAP với PEEP cao (6 - 7 cmH2O) hoặc chuẩn bị sẵn dụng cụ đặt NKQ") + "."],
  "SpO2 vẫn 93% nhưng FiO2 và nhịp thở tăng; ROX phơi bày sự suy giảm ẩn dưới con số SpO2 'ổn định'.",
  "PED-25 RELEASE v1, mục 7 và checkpoint 2", algo=True)

# =============================== B8 — Biến chứng
B("PED25-B8-01", 1,
  "Liệt kê " + Y("4 biến chứng") + " của hỗ trợ hô hấp không xâm lấn và " + G("xử trí/dự phòng chủ đạo") + " của mỗi biến chứng.",
  [R("Chướng bụng do nuốt khí") + " → " + G("ống thông dạ dày 8 - 10F mở nắp dẫn lưu tự do") + ".",
   R("Loét tì đè vách ngăn và cánh mũi") + " → prong chiếm " + Y("50 - 70%") + " lỗ mũi, miếng dán hydrocolloid.",
   R("Chấn thương áp lực (tràn khí màng phổi)") + " → chọc kim giải áp khoang liên sườn 2 rồi dẫn lưu màng phổi.",
   R("Ngộ độc oxy và xẹp phổi hấp thu") + " → tránh FiO2 80 - 100% kéo dài, chuẩn độ về khoảng đích."],
  "Không xâm lấn không đồng nghĩa không tai biến; phát hiện sớm nhờ theo dõi bụng, mũi, lồng ngực và FiO2.",
  "PED-25 RELEASE v1, mục 8")

B("PED25-B8-02", 2,
  R("Chướng bụng do nuốt khí") + ": " + Y("ngưỡng áp lực") + " gây ra, " + R("hậu quả") + " và " + G("xử trí bắt buộc") + "?",
  ["Khi áp lực đường thở (PEEP hoặc dòng HFNC lớn) vượt áp lực mở cơ thắt thực quản dưới (khoảng " + Y("6 - 8 cmH2O") + " ở trẻ nhỏ) → khí vào thực quản và dạ dày.",
   "Hậu quả: dạ dày căng đẩy cơ hoành lên, giảm thể tích lồng ngực → suy hô hấp nặng hơn, nôn trớ và hít sặc dịch vị.",
   G("Đặt ống thông dạ dày số 8 - 10F, mở nắp dẫn lưu tự do") + " cho mọi trẻ thở nCPAP hoặc HFNC lưu lượng cao kéo dài."],
  "Dẫn lưu liên tục giải phóng khí thừa nên cơ hoành vận động lại và SpO2 hồi phục mà không cần tăng PEEP.",
  "PED-25 RELEASE v1, mục 8.1")

B("PED25-B8-03", 2,
  R("Loét tì đè vách ngăn và cánh mũi") + ": " + N("cơ chế") + ", " + R("hậu quả") + " và " + G("dự phòng") + " (cỡ prong, vật liệu bảo vệ)?",
  ["Cơ chế: prong quá to ép sụn cánh mũi, hoặc bị kéo lệch trục tì đè liên tục lên vách ngăn → niêm mạc mỏng thiếu máu cục bộ hoại tử.",
   "Hậu quả: " + R("loét vách ngăn, biến dạng lỗ mũi vĩnh viễn, thủng vách ngăn mũi") + ".",
   "Dự phòng: prong có đường kính ngoài chiếm " + Y("50 - 70%") + " lỗ mũi, " + R("không bao giờ bít kín 100%") + "; dùng miếng dán " + G("hydrocolloid") + " bảo vệ da sống mũi và vách ngăn."],
  "Niêm mạc mũi trẻ rất mỏng nên áp lực tì đè liên tục gây hoại tử nhanh.",
  "PED-25 RELEASE v1, mục 8.2")

B("PED25-B8-04", 2,
  R("Chấn thương áp lực") + ": " + N("cơ chế") + ", " + R("dấu hiệu nhận biết") + " và " + G("xử trí cấp cứu") + "?",
  ["Cơ chế: áp lực dương quá cao làm phế nang căng quá mức, vỡ; khí theo bao mạch vào trung thất hoặc vào khoang màng phổi.",
   R("Dấu hiệu:") + " trẻ đột ngột tím tái, SpO2 tụt dốc không đáp ứng tăng oxy, lồng ngực một bên phồng bất đối xứng, rì rào phế nang giảm mạnh một bên, tim bị đẩy sang bên đối diện.",
   G("Xử trí:") + " chọc hút kim giải áp khoang màng phổi cấp cứu tại " + Y("khoang liên sườn 2 đường trung đòn") + ", sau đó đặt ống dẫn lưu màng phổi liên tục."],
  "Tràn khí áp lực chưa dẫn lưu giải áp là một trong 7 cờ đỏ buộc đặt NKQ; chọc kim giải áp là cứu sinh.",
  "PED-25 RELEASE v1, mục 8.3")

B("PED25-B8-05", 2,
  R("Ngộ độc oxy và xẹp phổi hấp thu") + ": " + N("cơ chế") + " khi hít FiO2 " + Y("80 - 100%") + " kéo dài?",
  ["Nitơ trong phế nang (khí trơ giữ khung phế nang) bị oxy thay thế hoàn toàn.",
   "Oxy được mao mạch phổi hấp thu rất nhanh; khi tốc độ hấp thu vượt tốc độ khí mới vào (phế nang thông khí kém) → phế nang " + R("xẹp hoàn toàn (xẹp phổi hấp thu)") + ".",
   "Đồng thời nồng độ oxy cao sinh gốc tự do oxy hóa " + R("phá hủy màng phế nang - mao mạch") + "."],
  "Vì vậy phải chuẩn độ FiO2 về khoảng đích thay vì cho oxy tối đa kéo dài.",
  "PED-25 RELEASE v1, mục 8.4")

# =============================== B9 — Sai lầm & checkpoint
B("PED25-B9-01", 1,
  "Liệt kê " + R("8 sai lầm kinh điển") + " khi dùng oxy và hỗ trợ hô hấp không xâm lấn.",
  ["Oxy nồng độ cao kéo dài cho mọi trẻ khó thở mà không kiểm soát đích SpO2.",
   "Mặt nạ đơn giản với lưu lượng " + Y("< 5 L/phút") + ".",
   "Chọn gọng mũi HFNC " + Y("bít kín 100%") + " lỗ mũi.",
   "nCPAP kéo dài mà quên ống thông dạ dày giải áp.",
   "Cai lưu lượng trước khi cai FiO2 ở HFNC.",
   "Khí HFNC không được làm ấm làm ẩm đúng chuẩn.",
   "Trì hoãn đặt NKQ khi thất bại HFNC/nCPAP.",
   "Oxy liều cao cho trẻ tim bẩm sinh tuần hoàn phụ thuộc ống động mạch."],
  "Phần lớn sai lầm đến từ tâm lý 'thừa oxy còn hơn thiếu' hoặc chần chừ nâng bậc; mỗi sai lầm có cơ chế sinh lý rõ ràng.",
  "PED-25 RELEASE v1, mục 9")

B("PED25-B9-02", 2,
  "Sai lầm " + R("oxy cao kéo dài cho mọi trẻ khó thở") + " và sai lầm " + R("oxy 100% cho tim bẩm sinh phụ thuộc ống động mạch") + ": " + N("bản chất khoa học") + " và " + G("cách làm đúng") + "?",
  ["SpO2 đã 100% thì PaO2 có thể vọt lên " + Y("200 - 400 mmHg") + " → co thắt động mạch não và vành, gốc tự do ROS gây viêm phổi hóa học → " + G("luôn chuẩn độ oxy về khoảng đích khuyến cáo") + ".",
   "Dị tật phụ thuộc ống động mạch (teo van động mạch phổi, hẹp eo động mạch chủ nặng, thiểu sản thất trái): sống nhờ luồng qua ống.",
   "Oxy là chất kích thích co mạch mạnh nhất với ống động mạch → ống đóng sụp → " + R("sốc tim và tử vong trong chốc lát") + "; " + G("không chụp mặt nạ oxy 100% xả dòng tối đa") + "."],
  "Ở nhóm tím do tim, tím không phải chỉ định xả oxy tối đa; đích SpO2 riêng bảo vệ ống động mạch.",
  "PED-25 RELEASE v1, mục 9 (sai lầm 1 và 8)")

B("PED25-B9-03", 2,
  "Ba sai lầm cài đặt thiết bị: " + R("mặt nạ đơn giản < 5 L/phút") + ", " + R("gọng HFNC bít kín 100% lỗ mũi") + ", " + R("khí HFNC lạnh khô") + ". Vì sao nguy hiểm và " + G("chuẩn đúng") + "?",
  ["Mặt nạ đơn giản: buồng " + Y("100 - 200 mL") + " + dòng " + Y("< 5 L/phút") + " → hít lại CO2 → " + R("toan hô hấp cấp") + "; bắt buộc ≥ " + Y("5 L/phút") + " hoặc đổi sang canula.",
   "HFNC là " + N("hệ thống mở") + ": bít kín 100% thì áp lực trong phổi tăng vọt theo dòng → " + R("vỡ phế nang, tràn khí màng phổi") + "; prong chỉ chiếm tối đa " + Y("50 - 70%") + " lỗ mũi.",
   "Khí lạnh khô (oxy tường qua bình làm ẩm bọt nước, tăng lên " + Y("15 - 20 L/phút") + ") → " + R("đông lông chuyển, khô rát trợt loét niêm mạc, hạ thân nhiệt, cục đờm quánh tắc phế quản") + "; HFNC bắt buộc có máy làm ẩm nhiệt chuyên dụng " + Y("37°C và 100% độ ẩm") + "."],
  "Cả ba sai lầm đều xuất phát từ việc coi thiết bị là 'chỉ cần đủ oxy' mà bỏ qua điều kiện cơ học và nhiệt ẩm.",
  "PED-25 RELEASE v1, mục 9 (sai lầm 2, 3, 6)")

B("PED25-B9-04", 2,
  "Ba sai lầm vận hành: " + R("nCPAP quên ống thông dạ dày") + ", " + R("cai lưu lượng trước FiO2") + ", " + R("trì hoãn đặt NKQ") + ". " + N("Bản chất") + " và " + G("xử trí đúng") + "?",
  ["Trẻ nCPAP trướng bụng, SpO2 tụt: không tăng PEEP/FiO2 mà " + G("đặt ống thông dạ dày mở nắp xả khí") + "; dạ dày phình đẩy cơ hoành, giảm FRC; bụng xẹp và SpO2 hồi phục.",
   "Ví dụ hạ dòng từ " + Y("15 xuống 8 L/phút") + " khi FiO2 còn " + Y("60%") + ": phế nang xẹp lại, công thở tăng; " + G("hạ FiO2 về ≤ 30 - 40% trước, rồi mới hạ lưu lượng") + ".",
   "ROX tụt, trẻ kiệt sức mà vẫn tăng dòng hoặc FiO2 100%: chỉ che đậy thiếu oxy tạm thời, không giải quyết kiệt sức cơ và toan → " + R("tăng nguy cơ ngưng tim lúc đặt ống và tử vong") + "."],
  "Ba sai lầm đều là kéo dài thời gian trước khi hành động đúng; sửa nguyên nhân (khí dạ dày, thứ tự cai, nâng bậc) thay vì tăng thông số.",
  "PED-25 RELEASE v1, mục 9 (sai lầm 4, 5, 7)")

B("PED25-B9-05", 2,
  "Checkpoint 1: trẻ " + Y("8 tháng, 8 kg") + ", viêm phế quản phổi, SpO2 " + Y("86%") + " khí trời, canula " + Y("2 L/phút") + " sau 15 phút thở rên, co kéo, SpO2 " + Y("88%") + ". Tăng canula lên " + Y("4 L/phút") + " hay đổi thiết bị? Hành động đúng?",
  ["Canula ở trẻ 8 kg tối đa " + Y("2 L/phút") + " (FiO2 tối đa khoảng " + Y("30 - 35%") + "); tăng lên 4 L/phút chỉ " + R("khô niêm mạc, rát mũi") + " mà không tăng FiO2 vì trẻ thở nhanh bị pha loãng khí trời.",
   "Suy hô hấp nặng co kéo dữ dội và SpO2 < 90% cần FiO2 cao tức thì để bảo vệ não.",
   G("Chuyển ngay sang NRM") + " lưu lượng " + Y("10 - 12 L/phút") + " (túi phồng ≥ 2/3) để đạt FiO2 khoảng " + Y("85 - 90%") + ", đồng thời chuẩn bị HFNC hoặc nCPAP để hỗ trợ áp lực."],
  "Canula không thể thắng thở nhanh và dòng đỉnh hít vào lớn; nâng bậc thiết bị đúng hơn tăng liều trên thiết bị sai.",
  "PED-25 RELEASE v1, mục 10 (checkpoint 1)")

B("PED25-B9-06", 2,
  "Checkpoint 3: bé " + Y("4 tháng") + " viêm tiểu phế quản nặng, nCPAP " + Y("PEEP 6, FiO2 40%") + ", sau " + Y("4 giờ") + " bụng trướng căng gõ vang, SpO2 " + Y("95% → 89%") + ". " + R("Phản xạ sai") + " và " + G("hành động đúng") + "?",
  [R("Phản xạ sai:") + " nghĩ phổi nặng hơn rồi tăng PEEP lên " + Y("7 - 8") + " và FiO2 lên " + Y("60%") + " → khí vào dạ dày nhiều hơn, cơ hoành đẩy cao, phổi xẹp nặng hơn.",
   "Nguyên nhân: PEEP đưa khí vào dạ dày gây chướng bụng cơ học cấp, cản cơ hoành (cơ hô hấp chính của nhũ nhi).",
   G("Hành động đúng:") + " đặt ngay sonde dạ dày số " + Y("8F") + ", hút ra " + Y("150 mL") + " khí và dịch sữa loãng, rồi để hở nối túi dẫn lưu tự do.",
   "Kết quả: bụng mềm, cơ hoành cử động, SpO2 lên " + Y("96%") + " mà không cần tăng PEEP."],
  "Khi SpO2 tụt kèm bụng chướng ở trẻ nCPAP, tìm nguyên nhân cơ học trước khi tăng thông số.",
  "PED-25 RELEASE v1, mục 10 (checkpoint 3)")

# =============================== B10 — Ca lâm sàng
B("PED25-B10-01", 1,
  "Hai ca lâm sàng của bài: " + N("ca 1") + " và " + N("ca 2") + " khác nhau thế nào về " + Y("tuổi/cân nặng") + ", " + N("chẩn đoán") + ", " + G("thiết bị đầu tay") + " và " + Y("kết cục") + "?",
  ["Ca 1: bé trai " + Y("5 tháng, 7.0 kg") + ", viêm tiểu phế quản cấp nặng → " + G("HFNC đầu tay") + " → đáp ứng, ngắt HFNC, xuất viện sau " + Y("4 ngày") + ".",
   "Ca 2: bé gái " + Y("3 tuổi, 14.0 kg") + ", viêm phổi thùy biến chứng PARDS nặng → " + G("nCPAP có kiểm soát") + " → thất bại tại 2 giờ → " + R("đặt NKQ cấp cứu") + ", cai máy thở sau " + Y("6 ngày") + "."],
  "Cùng bậc thang nhưng khác bệnh sinh: tắc nghẽn đường thở nhỏ ở ca 1 phù hợp HFNC; đông đặc lan tỏa ở ca 2 cần PEEP thật và nhận ra thất bại sớm.",
  "PED-25 RELEASE v1, mục 11")

B("PED25-B10-02", 2,
  "Ca 1 (" + Y("7.0 kg") + ", SpO2 " + Y("87%") + " khí trời, nhịp thở " + Y("68") + "): vì sao " + G("HFNC đầu tay") + ", " + Y("cài đặt") + " ra sao, " + Y("ROX 2 giờ") + " bao nhiêu và " + G("kế hoạch cai") + "?",
  ["Canula " + Y("1.5 L/phút") + " thất bại (SpO2 " + Y("89 - 90%") + ", thở " + Y("70") + ", mệt cơ); cơ chế phù nề tiểu phế quản, ứ đờm, tăng khoảng chết → " + G("HFNC đầu tay") + ".",
   "Cài: prong cỡ nhũ nhi chiếm khoảng " + Y("60%") + " lỗ mũi; lưu lượng " + Y("2.0 × 7.0 = 14.0 L/phút") + "; FiO2 " + Y("50%") + "; ẩm " + Y("37°C") + ".",
   "Sau 1 giờ: thở " + Y("52") + ", SpO2 " + Y("95%") + "; ROX 2 giờ = (95 / 0.40) / 48 = " + Y("4.95 (> 4.88)") + " → đáp ứng tốt.",
   "Cai: ngày 2 hạ FiO2 " + Y("30%") + ", dòng " + Y("14 → 10 → 7 L/phút") + "; ngày 3 dòng " + Y("3.5 L/phút (0.5 L/kg/phút)") + ", FiO2 " + Y("25%") + " → ngắt, khí trời."],
  "Quy trình đúng: chọn theo bệnh sinh, tính liều theo cân nặng, đánh giá ROX tại 2 giờ rồi cai FiO2 trước.",
  "PED-25 RELEASE v1, mục 11 (ca 1)")

B("PED25-B10-03", 2,
  "Ca 2 (" + Y("14 kg") + ", SpO2 " + Y("86%") + " dù NRM 10 L/phút, P/F khoảng " + Y("100") + "): " + G("can thiệp nCPAP") + " ban đầu, " + R("tiêu chí thất bại tại 2 giờ") + " và " + G("xử trí quyết định") + "?",
  ["Đánh giá: viêm phổi nặng biến chứng " + N("PARDS nặng (PALICC-2)") + ", shunt rất lớn, giảm FRC trầm trọng; HFNC không đủ PEEP cao.",
   "nCPAP mặt nạ mũi: PEEP " + Y("6") + ", FiO2 " + Y("70%") + ", dòng " + Y("10 L/phút") + ", sonde dạ dày " + Y("10F") + "; sau 30 phút PEEP " + Y("7") + ", FiO2 " + Y("80%") + ", SpO2 " + Y("90%") + ", nhịp thở " + Y("56") + ".",
   "Thất bại 2 giờ: khí máu pH " + Y("7.18") + ", PaCO2 " + Y("66") + ", SpO2 " + Y("88%") + " với FiO2 " + Y("85%") + "; ROX = (88 / 0.85) / 56 = " + R("1.85 (< 3.85)") + ".",
   G("Xử trí:") + " không tăng PEEP 8 - 9 hay FiO2 100%; kích hoạt kíp, đặt NKQ có bóng số " + Y("4.5") + ", Ketamine + Rocuronium; thở máy bảo vệ phổi VT " + Y("6 mL/kg") + ", PEEP " + Y("10 cmH2O") + "."],
  "Toan hô hấp mất bù cộng ROX rất thấp là thất bại tuyệt đối với thông khí không xâm lấn; tăng thông số chỉ làm mất cơ hội cứu sống.",
  "PED-25 RELEASE v1, mục 11 (ca 2)")

# =============================== B11 — Tips
B("PED25-B11-01", 1,
  "Liệt kê " + Y("10 tips thực hành") + " tại giường theo " + N("2 nhóm") + ": kỹ thuật thiết bị và theo dõi lâm sàng.",
  [N("Kỹ thuật thiết bị:") + " quy tắc prong 50 - 70%; xả bẫy nước; mở nắp ống thông dạ dày khi CPAP; pha oxy khi không có blender; xử trí rò khí qua miệng khi nCPAP; cố định dây máy.",
   N("Theo dõi:") + " đừng tin mù quáng SpO2 (nhìn sóng mạch); nhận diện bẫy khí ở hen khi HFNC; quy tắc một thông số một thời điểm khi cai; nhận diện thất bại thầm lặng."],
  "Các tips chuyển từ lý thuyết sang thao tác điều dưỡng cụ thể để phòng biến chứng.",
  "PED-25 RELEASE v1, mục 12")

B("PED25-B11-02", 2,
  "Tips " + N("kỹ thuật thiết bị") + ": quy tắc prong " + Y("50 - 70%") + ", " + N("bẫy nước") + ", ống thông dạ dày, " + N("pha oxy khi không có blender") + ", " + N("rò khí miệng") + ", cố định dây máy.",
  ["Thử prong trước khi bật máy: đường kính ngoài " + Y("1/2 đến 2/3 (50 - 70%)") + " lỗ mũi; cánh mũi bè/căng phồng là quá to → đổi cỡ nhỏ.",
   "Xả bẫy nước thường xuyên: nước ngưng tụ bị dòng khí đẩy vào mũi gây sặc cấp hoặc tắc dòng, báo động liên tục.",
   "Khi nCPAP, ống thông dạ dày " + G("nối túi dẫn lưu mở tự do") + ", không gập hay đậy nắp.",
   "Không có blender: Lưu lượng Oxy = Tổng lưu lượng × " + Y("(FiO2 − 0.21) / 0.79") + ".",
   "Trẻ há miệng làm rò PEEP: dùng " + G("đai giữ cằm hoặc núm vú giả") + " để ngậm miệng.",
   "Móc dây máy vào áo/ga giường để trọng lượng dây không kéo gọng xuống, ngừa loét tì đè vách ngăn."],
  "Mỗi mẹo chặn một biến chứng cụ thể: tràn khí, sặc nước, chướng bụng, mất PEEP và loét mũi.",
  "PED-25 RELEASE v1, mục 12 (tip 1 - 5 và 8)")

B("PED25-B11-03", 2,
  "Tips " + N("theo dõi lâm sàng") + ": SpO2 " + R("không đáng tin") + " khi nào, " + R("bẫy khí ở hen") + " khi dùng HFNC, quy tắc cai " + Y("một thông số") + ", và " + R("thất bại thầm lặng") + "?",
  ["Sốc, co mạch ngoại vi nặng, hạ thân nhiệt: sóng mạch dẹt/nhiễu nên SpO2 không đáng tin; luôn kiểm tra sóng đều, đỉnh rõ, đồng nhịp tim nghe được.",
   "Hen cấp nặng: dòng HFNC liên tục có thể làm nặng thêm căng giãn phổi (Auto-PEEP) và bẫy khí; lồng ngực ngày càng căng, rì rào giảm → " + G("chuyển ngay phương thức hỗ trợ") + ".",
   "Không giảm đồng thời lưu lượng và FiO2 trong một lần chỉnh; " + G("giảm FiO2 trước") + ".",
   R("Thất bại thầm lặng:") + " HFNC mà nhịp thở không giảm sau " + Y("2 giờ") + ", co kéo không đỡ, dù SpO2 " + Y("93 - 94%") + " nhờ liên tục tăng FiO2 → nhìn công thở và sự tỉnh táo, đừng tin riêng SpO2."],
  "Đây là các cạm bẫy theo dõi khiến bác sĩ yên tâm giả tạo.",
  "PED-25 RELEASE v1, mục 12 (tip 6, 7, 9, 10)")

# =============================== B12 — Cai máy & xuất viện
B("PED25-B12-01", 1,
  "Quy trình kết thúc điều trị gồm " + Y("3 chặng") + " nào: tiêu chuẩn cai máy, chuyển tầng PICU ra khoa thường, xuất viện?",
  [G("Tiêu chuẩn cai máy:") + " thỏa đồng thời 6 tiêu chí (bệnh nền, lâm sàng, nhịp thở, thông số tối thiểu, SpO2, dung nạp ăn).",
   G("Chuyển tầng:") + " cai thành công, canula " + Y("≤ 1 L/phút") + " hoặc khí trời, huyết động ổn định.",
   G("Xuất viện:") + " 4 tiêu chí (khí trời 24 giờ, hết sốt 24 giờ, ăn bú tốt, cha mẹ hiểu cách chăm sóc)."],
  "Mỗi chặng có ngưỡng định lượng để tránh cai sớm và tái phát.",
  "PED-25 RELEASE v1, mục 13")

B("PED25-B12-02", 2,
  "Liệt kê " + Y("6 tiêu chuẩn thỏa đồng thời") + " để ngắt hoàn toàn thiết bị hỗ trợ không xâm lấn, gồm " + Y("thông số tối thiểu") + " của HFNC và nCPAP.",
  ["Bệnh nền đã thoái lui hoặc kiểm soát ổn định.",
   "Trẻ tỉnh, hồng, tự thở êm, không còn co kéo cơ phụ (hoặc chỉ còn nhẹ).",
   "Nhịp thở trong giới hạn bình thường theo tuổi.",
   "Thông số tối thiểu: HFNC " + Y("≤ 0.5 L/kg/phút và FiO2 ≤ 30%") + "; nCPAP " + Y("PEEP ≤ 4 cmH2O và FiO2 ≤ 30%") + ".",
   "SpO2 " + Y("≥ 94%") + " (hoặc " + Y("≥ 90 - 92%") + " ở viêm tiểu phế quản) liên tục ít nhất " + Y("4 - 6 giờ") + " sau chuyển sang khí trời.",
   "Dung nạp ăn qua đường miệng hoặc bú mẹ tốt, không khó thở hay tụt SpO2."],
  "Yêu cầu thỏa đồng thời nhằm chứng minh công thở và oxy hóa ổn định ngay cả khi ăn bú.",
  "PED-25 RELEASE v1, mục 13.1")

B("PED25-B12-03", 2,
  "Tiêu chuẩn " + G("chuyển từ PICU ra khoa thường") + " và " + G("4 tiêu chuẩn xuất viện an toàn") + " (khí trời, sốt, ăn bú, cha mẹ)?",
  ["Chuyển tầng: thở canula thường " + Y("≤ 1 L/phút") + " hoặc khí trời, huyết động ổn định không cần theo dõi xâm lấn.",
   "Tự thở khí trời hoàn toàn ít nhất " + Y("24 giờ") + " với SpO2 " + Y("≥ 94%") + ".",
   "Hết sốt ít nhất " + Y("24 giờ") + " không dùng thuốc hạ sốt.",
   "Bú tốt, ăn đạt " + Y("≥ 75%") + " nhu cầu cơ bản hàng ngày, không nôn trớ.",
   "Cha mẹ hiểu cách chăm sóc, nhận biết dấu hiệu khó thở tái phát và biết đưa trẻ tái khám ngay."],
  "Quan sát 24 giờ không oxy và không sốt giảm nguy cơ tái phát suy hô hấp sau xuất viện.",
  "PED-25 RELEASE v1, mục 13.2")

# =============================== B13 — Bằng chứng
B("PED25-B13-01", 1,
  "Bài dựa trên " + Y("7 bằng chứng chính") + " nào (PARIS, PARIS-2, FIRST-ABC Step-Up, FIRST-ABC Post-Extubation, Cochrane CPAP bronchiolitis, network meta-analysis, PALICC-2) và kết luận cốt lõi của mỗi bằng chứng?",
  [N("PARIS:") + " HFNC giảm thất bại điều trị so với oxy chuẩn ở bronchiolitis dưới 12 tháng.",
   N("PARIS-2:") + " HFNC sớm ở trẻ 1 - 4 tuổi suy hô hấp giảm oxy " + R("không rút ngắn") + " thời gian nằm viện.",
   N("FIRST-ABC Step-Up:") + " HFNC " + G("không kém hơn") + " CPAP là hỗ trợ đầu tay ở PICU.",
   N("FIRST-ABC Post-Extubation:") + " HFNC " + R("không đạt không kém hơn") + " CPAP sau rút ống.",
   N("Cochrane:") + " nCPAP giảm nhịp thở ở viêm tiểu phế quản.",
   N("Network meta-analysis:") + " CPAP và HFNC đều hơn oxy thường trong giảm thất bại rút ống.",
   N("PALICC-2:") + " định nghĩa PARDS không xâm lấn, tránh trì hoãn đặt NKQ."],
  "Các thử nghiệm cho thấy bối cảnh quyết định lựa chọn: HFNC cho bronchiolitis và đầu tay ở PICU, CPAP vượt trội sau rút ống.",
  "PED-25 RELEASE v1, mục 14")

B("PED25-B13-02", 2,
  "Thử nghiệm " + N("PARIS") + " (HFNC vs oxy chuẩn, bronchiolitis): " + Y("cỡ mẫu") + ", " + Y("tỷ lệ thất bại 2 nhóm") + ", " + Y("chênh lệch nguy cơ") + " và " + G("tỷ lệ cứu hộ thành công") + "?",
  ["Cỡ mẫu " + Y("1.472") + " trẻ dưới 12 tháng mắc viêm tiểu phế quản cấp ở khoa bệnh phòng thông thường.",
   "Thất bại điều trị cần nâng bậc: HFNC " + Y("12%") + " so với oxy chuẩn " + Y("23%") + ".",
   "Chênh lệch nguy cơ " + Y("−11 điểm phần trăm") + " (KTC 95% " + Y("−15 đến −7") + ", p < 0.001).",
   "Trong " + Y("167") + " trẻ thất bại ở nhóm oxy chuẩn, " + Y("61%") + " đáp ứng với HFNC cứu hộ mà không cần đặt NKQ hay vào ICU."],
  "HFNC làm giảm tỷ lệ thất bại cần nâng bậc và là liệu pháp cứu hộ hiệu quả.",
  "Franklin D và cs, NEJM 2018 (PARIS)")

B("PED25-B13-03", 2,
  "Thử nghiệm " + N("PARIS-2") + " (HFNC sớm, trẻ " + Y("1 - 4 tuổi") + "): " + Y("cỡ mẫu") + ", " + R("thời gian nằm viện") + ", " + R("thời gian thở oxy") + " và " + G("kết luận thực hành") + "?",
  ["Phân tích chính " + Y("1.517") + " trẻ.",
   "Thời gian nằm viện HFNC sớm trung vị " + Y("1.77 ngày so với 1.50 ngày") + "; adjusted HR " + Y("0.83") + " (KTC 95% " + Y("0.75 - 0.92") + ", p < 0.001) → " + R("không ngắn hơn mà dài hơn") + ".",
   "Thời gian thở oxy trung vị " + Y("1.07 so với 0.75 ngày") + ".",
   G("Không khuyến cáo HFNC sớm thường quy") + " cho mọi trẻ 1 - 4 tuổi suy hô hấp giảm oxy khi chưa có chỉ định nâng bậc."],
  "HFNC không phải chiếc đũa thần dùng bừa bãi; cần chỉ định đúng nhóm bệnh nhân.",
  "Franklin D và cs, JAMA 2023 (PARIS-2)")

B("PED25-B13-04", 2,
  "Thử nghiệm " + N("FIRST-ABC Step-Up") + " (HFNC vs CPAP đầu tay ở PICU): " + Y("cỡ mẫu và số khoa") + ", " + Y("thời gian giải phóng hỗ trợ") + ", " + Y("adjusted HR") + " và " + G("tỷ lệ dùng an thần") + "?",
  ["Cỡ mẫu " + Y("573") + " trẻ tại " + Y("24") + " khoa PICU.",
   "Thời gian giải phóng hỗ trợ: HFNC " + Y("52.9 giờ") + " so với CPAP " + Y("47.9 giờ") + "; adjusted HR " + Y("1.03") + ", KTC một phía 97.5% " + Y("0.86 đến vô cực") + " → " + G("đạt không kém hơn") + ".",
   "Tỷ lệ dùng thuốc an thần: HFNC " + Y("27.7%") + " so với CPAP " + Y("37.0%") + "; adjusted OR " + Y("0.59") + " (KTC 95% " + Y("0.39 - 0.88") + ")."],
  "HFNC là lựa chọn đầu tay chấp nhận được tại PICU, dễ chịu hơn và giảm nhu cầu an thần.",
  "Ramnarayan P và cs, JAMA 2022 (FIRST-ABC Step-Up)")

B("PED25-B13-05", 2,
  "Thử nghiệm " + N("FIRST-ABC Post-Extubation") + " (HFNC vs CPAP sau rút ống): " + Y("cỡ mẫu") + ", " + R("kết quả không kém hơn") + ", " + Y("thời gian giải phóng") + " và " + Y("tỷ lệ đặt lại NKQ 48 giờ") + "?",
  ["Cỡ mẫu " + Y("553") + " trẻ sau rút nội khí quản.",
   "HFNC " + R("không đạt tiêu chuẩn không kém hơn") + " CPAP.",
   "Thời gian giải phóng trung vị " + Y("50.5 giờ (HFNC) so với 42.9 giờ (CPAP)") + "; adjusted HR " + Y("0.83") + ", KTC một phía 97.5% " + Y("0.70 đến vô cực") + ".",
   "Đặt lại NKQ trong " + Y("48 giờ") + " tương đương: " + Y("13.3% (HFNC) so với 11.5% (CPAP)") + "."],
  "Sau thở máy kéo dài, áp lực dương thật của CPAP có vai trò không thể thay thế trong tái mở phế nang xẹp.",
  "Ramnarayan P và cs, JAMA 2022 (FIRST-ABC Post-Extubation)")

B("PED25-B13-06", 2,
  "Cochrane (CPAP bronchiolitis), network meta-analysis (thất bại rút ống) và " + N("PALICC-2") + ": " + Y("số liệu then chốt") + " và " + G("thông điệp lâm sàng") + " của mỗi nguồn?",
  [N("Cochrane:") + " 91 trẻ từ 2 RCT, nCPAP giảm nhịp thở, chênh lệch trung bình " + Y("−3.81 lần/phút") + " (KTC 95% " + Y("−5.78 đến −1.84") + "); bằng chứng giảm nhu cầu thở máy xâm lấn còn chưa chắc chắn do cỡ mẫu nhỏ.",
   N("Network meta-analysis:") + " 9 thử nghiệm, " + Y("1.421") + " bệnh nhi; so với oxy thường CPAP có OR " + Y("0.43") + " (KTC 95% " + Y("0.17 - 1.0") + "), HFNC có OR " + Y("0.64") + " (KTC 95% " + Y("0.24 - 1.0") + "); CPAP xác suất tối ưu cao nhất, SUCRA " + Y("0.83") + ".",
   N("PALICC-2:") + " PARDS không xâm lấn khi nhận CPAP hoặc HFNC lưu lượng " + Y("≥ 1.5 L/kg/phút") + " kèm giảm SpO2/FiO2 thỏa tiêu chuẩn thiếu oxy; " + R("tuyệt đối tránh trì hoãn đặt NKQ") + " khi thông khí không xâm lấn không cải thiện."],
  "Tổng hợp bằng chứng củng cố: CPAP và HFNC đều tốt hơn oxy thường, CPAP tối ưu hơn sau rút ống, và luôn cần theo dõi để không trì hoãn đặt NKQ.",
  "Jat KR 2022 (Cochrane); Wang Z 2023 (JAMA Pediatr); PALICC-2 2023")

# =============================== Cloze phụ (giữ từ APKG cũ — chỉ ngưỡng/mốc/định nghĩa 1 mệnh đề)
_X = "PED-25 RELEASE v1, "
C("PED25-B0-C01", "B0", "Phân suất oxy trong khí trời (FiO2) cố định ở mức {{c1::21% (hoặc 0.21)}}.", _X + "mục 0.1", 1789648255191)
C("PED25-B0-C02", "B0", "Áp lực dương cuối thì thở ra (PEEP) là áp lực duy trì bên trong đường dẫn khí tại thời điểm {{c1::kết thúc thì thở ra}}.", _X + "mục 0.1", 1789648255193)
C("PED25-B0-C03", "B0", "Dung tích cặn chức năng (FRC) sinh lý ở trẻ nhỏ khoảng {{c1::30 mL/kg}}, sát thể tích đóng của đường thở.", _X + "mục 0.1", 1789648255195)
C("PED25-B0-C04", "B0", "Ở trẻ nhũ nhi, vùng mũi hầu chiếm tới {{c1::50% tổng kháng lực đường thở}}.", _X + "mục 0.1", 1789648255199)
C("PED25-B0-C05", "B0", "Shunt trong phổi xảy ra khi máu mao mạch phổi đi qua các phế nang {{c1::không được thông khí (tỷ lệ V/Q = 0)}}.", _X + "mục 0.1", 1789648255203)
C("PED25-B0-C06", "B0", "Cơn ngừng thở (apnea) kéo dài trên {{c1::20 giây}} là dấu hiệu bắt buộc dừng hỗ trợ không xâm lấn để đặt nội khí quản.", _X + "Box đỏ cấp cứu", 1789648255277)
C("PED25-B0-C07", "B0", "Tỷ lệ khoảng chết trên thể tích lưu thông (VD/VT) ở trẻ em khoảng {{c1::30% đến 40%}}.", _X + "mục 0.1", 1789648255357)
C("PED25-B1-C01", "B1", "Mốc dốc đứng nguy hiểm trên đường cong phân ly oxyhemoglobin là SpO2 {{c1::dưới 90% (tương ứng PaO2 dưới 60 mmHg)}}.", _X + "mục 1.2", 1789648255205)
C("PED25-B1-C02", "B1", "Đích SpO2 cho trẻ viêm phổi hoặc suy hô hấp thông thường là {{c1::94% đến 98%}}.", _X + "mục 1.3", 1789648255207)
C("PED25-B1-C03", "B1", "Đích SpO2 cho bệnh nhi viêm tiểu phế quản cấp là {{c1::90% đến 94%}}.", _X + "mục 1.3", 1789648255209)
C("PED25-B1-C04", "B1", "Đích SpO2 ở trẻ tim bẩm sinh tím có shunt Phải - Trái thường là {{c1::75% đến 85%}}.", _X + "mục 1.3", 1789648255211)
C("PED25-B1-C05", "B1", "Đích SpO2 ở trẻ tim bẩm sinh tuần hoàn phụ thuộc ống động mạch là {{c1::80% đến 85% (tối đa không quá 88%)}}.", _X + "mục 1.3", 1789648255213)
C("PED25-B1-C06", "B1", "Đích SpO2 ở trẻ sinh non điều trị tại NICU là {{c1::91% đến 95%}}.", _X + "mục 1.3", 1789648255217)
C("PED25-B2-C01", "B2", "Lưu lượng oxy canula mũi quy chuẩn ở nhũ nhi là {{c1::0.5 đến 2.0 L/phút}}.", _X + "mục 2.2", 1789648255219)
C("PED25-B2-C02", "B2", "Canula mũi thông thường cho FiO2 ước tính {{c1::24% đến 35%}}.", _X + "mục 2.4", 1789648255221)
C("PED25-B2-C03", "B2", "Lưu lượng bắt buộc khi dùng mặt nạ đơn giản là {{c1::5 đến 8 L/phút}}.", _X + "mục 2.3", 1789648255223)
C("PED25-B2-C04", "B2", "Cấm cài lưu lượng dưới 5 L/phút ở mặt nạ đơn giản vì nguy cơ {{c1::ứ đọng và hít lại khí CO2 (rebreathing)}}.", _X + "mục 2.3", 1789648255225)
C("PED25-B2-C05", "B2", "Mặt nạ đơn giản cung cấp FiO2 ước tính {{c1::35% đến 50%}}.", _X + "mục 2.3", 1789648255227)
C("PED25-B2-C06", "B2", "Lưu lượng bắt buộc cho mặt nạ túi không thở lại (NRM) là {{c1::10 đến 15 L/phút}}.", _X + "mục 2.4", 1789648255229)
C("PED25-B2-C07", "B2", "Với NRM, túi dự trữ phải luôn căng ít nhất {{c1::2/3 thể tích}}.", _X + "mục 2.4", 1789648255231)
C("PED25-B2-C08", "B2", "NRM cung cấp FiO2 tối đa khoảng {{c1::80% đến 95%}}.", _X + "mục 2.4", 1789648255233)
C("PED25-B2-C09", "B2", "Muốn cấp oxy dòng thấp dưới 5 L/phút thì dùng {{c1::gọng mũi oxy (canula)}} thay cho mặt nạ đơn giản.", _X + "sai lầm 2", 1789648255371)
C("PED25-B3-C01", "B3", "Dòng khí HFNC được cài ở nhiệt độ và độ ẩm {{c1::37°C và 100% độ ẩm tương đối}}.", _X + "mục 3.1", 1789648255239)
C("PED25-B3-C02", "B3", "Khí ẩm bão hòa 100% ở 37°C chứa {{c1::44 mg H2O trong mỗi lít khí}}.", _X + "mục 3.1", 1789648255355)
C("PED25-B3-C03", "B3", "Hiệu ứng CO2 washout của HFNC quét sạch khí CO2 đọng tại {{c1::khoang mũi hầu}} vào cuối thì thở ra.", _X + "mục 3.2", 1789648255201)
C("PED25-B3-C04", "B3", "Dynamic PEEP do HFNC tạo ra khoảng {{c1::2 đến 4 cmH2O}}.", _X + "mục 3.4", 1789648255249)
C("PED25-B3-C05", "B3", "Khi trẻ ngậm miệng, PEEP động của HFNC có thể lên tới {{c1::5 đến 6 cmH2O}}.", _X + "mục 3.4", 1789648255363)
C("PED25-B4-C01", "B4", "Lưu lượng khởi đầu HFNC ở trẻ cân nặng ≤ 10 kg là {{c1::1.5 đến 2.0 L/kg/phút}}.", _X + "mục 4.1", 1789648255241)
C("PED25-B4-C02", "B4", "Ở trẻ > 10 kg, lưu lượng HFNC = 2.0 L/kg/phút cho 10 kg đầu cộng {{c1::0.5 L/kg/phút cho mỗi kg vượt trên 10 kg}}.", _X + "mục 4.1", 1789648255243)
C("PED25-B4-C03", "B4", "Giới hạn lưu lượng HFNC tối đa thông thường ở trẻ vị thành niên là {{c1::50 đến 60 L/phút}}.", _X + "mục 4.1", 1789648255245)
C("PED25-B4-C04", "B4", "FiO2 khởi đầu thông thường của HFNC là {{c1::40% đến 60%}}.", _X + "mục 4.2", 1789648255247)
C("PED25-B4-C05", "B4", "Nguyên tắc vàng khi cai HFNC là: {{c1::Cai FiO2 trước — Cai lưu lượng dòng sau}}.", _X + "mục 4.3", 1789648255255)
C("PED25-B4-C06", "B4", "FiO2 an toàn cần đạt trước khi hạ lưu lượng HFNC là {{c1::≤ 30% đến 40%}}.", _X + "mục 4.3", 1789648255257)
C("PED25-B4-C07", "B4", "Tốc độ giảm lưu lượng khi cai HFNC là {{c1::0.5 L/kg/phút mỗi 2 đến 4 giờ}}.", _X + "mục 4.3", 1789648255259)
C("PED25-B4-C08", "B4", "Ngưỡng ngừng HFNC ở nhũ nhi là lưu lượng {{c1::≤ 0.5 L/kg/phút (hoặc tổng < 4 L/phút)}} với FiO2 ≤ 30%.", _X + "mục 4.3", 1789648255261)
C("PED25-B4-C09", "B4", "Khi cài prong HFNC, đường kính ngoài chỉ được chiếm tối đa {{c1::50% đến 70% đường kính lỗ mũi}}.", _X + "mục 12, tip 1", 1789648255251)
C("PED25-B5-C01", "B5", "nCPAP duy trì áp lực dương liên tục trong {{c1::cả thì hít vào lẫn thì thở ra}} khi trẻ tự thở.", _X + "mục 5.1", 1789648255263)
C("PED25-B5-C02", "B5", "PEEP khởi đầu thông dụng của nCPAP là {{c1::4 đến 5 cmH2O}}.", _X + "mục 5.3", 1789648255265)
C("PED25-B5-C03", "B5", "Khi chuẩn độ nCPAP, tăng PEEP {{c1::1 cmH2O mỗi 15 đến 30 phút}}.", _X + "mục 5.3", 1789648255267)
C("PED25-B5-C04", "B5", "PEEP tối đa cho phép trong nCPAP thông thường là {{c1::8 cmH2O}}.", _X + "mục 5.3", 1789648255269)
C("PED25-B5-C05", "B5", "Lợi ích huyết động của nCPAP ở bệnh nhi suy tim là {{c1::làm giảm hậu gánh thất trái}}.", _X + "mục 5.1", 1789648255271)
C("PED25-B5-C06", "B5", "Bubble CPAP sinh dao động áp lực vi thể với tần số {{c1::15 đến 30 Hz}}.", _X + "mục 5.2", 1789648255351)
C("PED25-B7-C01", "B7", "ROX Index = {{c1::(SpO2 / FiO2) chia cho tần số thở (lần/phút)}}.", _X + "mục 7.1", 1789648255279)
C("PED25-B7-C02", "B7", "Bốn mốc đánh giá ROX là {{c1::0h, 2h, 6h và 12h}}.", _X + "mục 7.2", 1789648255281)
C("PED25-B7-C03", "B7", "Ngưỡng ROX dự báo thành công cao là {{c1::ROX ≥ 4.88}}.", _X + "mục 7.2", 1789648255283)
C("PED25-B7-C04", "B7", "Ngưỡng ROX báo động thất bại là {{c1::ROX < 3.85}}.", _X + "mục 7.2", 1789648255285)
C("PED25-B8-C01", "B8", "Xử trí cấp cứu tràn khí màng phổi áp lực là {{c1::chọc kim giải áp khoang liên sườn 2}} rồi đặt ống dẫn lưu.", _X + "mục 8.3", 1789648255275)
C("PED25-B8-C02", "B8", "Xẹp phổi hấp thu xảy ra khi oxy cao thay thế hoàn toàn {{c1::khí Nitơ}} trong phế nang.", _X + "mục 8.4", 1789648255359)
C("PED25-B8-C03", "B8", "Can thiệp điều dưỡng bắt buộc khi thở nCPAP là {{c1::đặt ống thông dạ dày giải áp liên tục}}.", _X + "mục 8.1", 1789648255273)
C("PED25-B9-C01", "B9", "Hiện tượng SpO2 vẫn đạt 93% nhưng FiO2 và nhịp thở tăng dần là {{c1::thất bại thầm lặng}}.", _X + "mục 12, tip 10", 1789648255399)
C("PED25-B9-C02", "B9", "Pha oxy khi không có blender: Lưu lượng Oxy = Tổng lưu lượng × {{c1::(FiO2 − 0.21) / 0.79}}.", _X + "mục 12, tip 4", 1789648255407)
C("PED25-B9-C03", "B9", "Trẻ nCPAP há miệng làm rò PEEP thì cho ngậm {{c1::núm vú giả (pacifier)}} hoặc đeo đai giữ cằm.", _X + "mục 12, tip 5", 1789648255409)
C("PED25-B10-C01", "B10", "Ca 1 (5 tháng, 7.0 kg): lưu lượng HFNC khởi đầu = 2.0 × 7.0 = {{c1::14.0 L/phút}}.", _X + "mục 11", 1789648255413)
C("PED25-B10-C02", "B10", "Ca 1: ROX tại 2 giờ = (95 / 0.40) / 48 = {{c1::4.95}}.", _X + "mục 11", 1789648255419)
C("PED25-B10-C03", "B10", "Ca 2 (3 tuổi, 14 kg): ROX sau 2 giờ nCPAP = (88 / 0.85) / 56 = {{c1::1.85}}.", _X + "mục 11", 1789648255431)
C("PED25-B13-C01", "B13", "Trong PARIS, thất bại điều trị HFNC so với oxy chuẩn là {{c1::12% so với 23%}}.", _X + "mục 14", 1789648255289)
C("PED25-B13-C02", "B13", "Trong PARIS, chênh lệch nguy cơ thất bại điều trị giữa HFNC và oxy chuẩn là {{c1::−11 điểm phần trăm}}.", _X + "mục 14", 1789648255291)
C("PED25-B13-C03", "B13", "Trong PARIS-2, thời gian nằm viện nhóm HFNC sớm là {{c1::1.77 ngày so với 1.50 ngày}} ở nhóm oxy chuẩn.", _X + "mục 14", 1789648255303)
C("PED25-B13-C04", "B13", "Trong FIRST-ABC Step-Up, tỷ lệ dùng an thần HFNC so với CPAP là {{c1::27.7% so với 37.0%}}.", _X + "mục 14", 1789648255317)
C("PED25-B13-C05", "B13", "Trong FIRST-ABC Post-Extubation, thời gian giải phóng hỗ trợ HFNC so với CPAP là {{c1::50.5 giờ so với 42.9 giờ}}.", _X + "mục 14", 1789648255325)
C("PED25-B13-C06", "B13", "Cochrane 2022: nCPAP làm giảm nhịp thở ở viêm tiểu phế quản với chênh lệch trung bình {{c1::−3.81 lần/phút}}.", _X + "mục 14", 1789648255331)
C("PED25-B13-C07", "B13", "Network meta-analysis 2023: CPAP có xác suất tối ưu cao nhất dự phòng thất bại rút ống với SUCRA {{c1::0.83}}.", _X + "mục 14", 1789648255341)
C("PED25-B13-C08", "B13", "PALICC-2: PARDS không xâm lấn khi nhận CPAP hoặc HFNC lưu lượng {{c1::≥ 1.5 L/kg/phút}}.", _X + "mục 14", 1789648255347)
