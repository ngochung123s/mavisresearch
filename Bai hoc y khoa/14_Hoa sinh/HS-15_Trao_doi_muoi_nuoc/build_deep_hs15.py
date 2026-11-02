# -*- coding: utf-8 -*-
"""build_deep_hs15.py - Generate 75 exhaustive master flashcards for HS-15 (Phân bố nước, điện giải, áp suất thẩm thấu và rối loạn thăng bằng dịch)"""
import json
import re
from pathlib import Path

def clean_label(t):
    if t.startswith('<b>'):
        m = re.match(r'^<b>(.*?)(?:\s*—|:)?</b>:?\s*(.*)', t)
        if m:
            head = m.group(1).replace(':', ' - ').strip()
            tail = m.group(2)
            return f"<b>{head} —</b> {tail}"
        return t
    m = re.match(r'^([^:<]{2,60}):\s*(.*)', t)
    if m:
        head = m.group(1).replace(':', ' - ').strip()
        tail = m.group(2)
        return f"<b>{head} —</b> {tail}"
    return t

def make_card(cid, front_title, front_badge, question, answers, explanation, algo=False, extra=""):
    ans_html = "<br>".join([f"{i+1}) {clean_label(a)}" for i, a in enumerate(answers)])
    badge_color = "#e03131" if algo else "#1971c2"
    badge_text = "⚡ THUẬT TOÁN QUYẾT ĐỊNH" if algo else front_badge
    
    if "ALGO" in cid: section = "B_ALGO"
    elif "-B1-" in cid: section = "B1"
    elif "-B2-" in cid: section = "B2"
    elif "-B3-" in cid: section = "B3"
    elif "-B4-" in cid: section = "B4"
    elif "-B5-" in cid: section = "B5"
    elif "-B6-" in cid: section = "B6"
    elif "-B7-" in cid: section = "B7"
    else: section = "B1"

    front = f"""<div style="font-size: 13px; font-weight: bold; color: {badge_color}; text-transform: uppercase; margin-bottom: 8px;">[{badge_text}] {front_title}</div>
<div style="font-size: 16px; font-weight: 600; color: #212529; line-height: 1.5;">{question}</div>
<div style="margin-top: 10px; font-size: 12px; color: #495057;">
  <span style="background-color: #ffd43b; color: #212529; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Gợi ý</span> Nhớ lại hóa sinh muối nước, áp suất thẩm thấu và cấp cứu rối loạn điện giải BSNT.
</div>"""

    back = f"""<div style="margin-bottom: 12px;">
  <span style="background-color: #51cf66; color: #087f5b; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">HÓA SINH Y HỌC</span>
  <span style="background-color: #74c0fc; color: #1864ab; padding: 2px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-left: 4px;">BSNT CHUYÊN SÂU</span>
</div>
<div style="font-size: 15px; color: #212529; line-height: 1.6;">
<b>🎯 Trả lời cốt lõi:</b><br>
{ans_html}
<br><br>
<b>💡 Giải thích của AI:</b><br>
<span style="color: #495057; font-size: 14px;">{explanation}</span>
</div>"""

    return {
        "id": cid,
        "track": "algo" if algo else "barem",
        "badge": badge_text,
        "badge_class": "badge-danger" if algo else "badge-info",
        "type": "basic",
        "section": section,
        "category": "HoaSinh",
        "tier": 1,
        "front": front,
        "back": back,
        "extra": extra or "Nguồn: Giáo trình Hóa Sinh Y Học - ĐHYHN (GS. Tạ Thành Văn, Tr. 323-338), Harrison's Principles of Internal Medicine 21st ed (Chap 52), Guyton & Hall Textbook of Medical Physiology 14th ed (Chap 25).",
        "tags": ["hoasinh", "HS15", section]
    }

cards = []

# ==============================================================================
# B1: NƯỚC TRONG CƠ THỂ (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B1-01", "Cấu tạo & Tính chất Lý hóa của Nước", "HÓA LÝ SINH HỌC",
    "Nêu cấu tạo phân tử lưỡng cực và 4 đặc tính lý hóa dị thường của Nước giúp duy trì sự sống?",
    [
        "Cấu trúc lưỡng cực dạng chữ V: Góc liên kết H-O-H xấp xỉ 104.5°, độ âm điện oxy lớn làm đôi electron lệch về phía oxy tạo mômen lưỡng cực mạnh (1.85 Debye).",
        "Hằng số điện môi cao (D ~ 80 ở 20°C): Làm giảm mạnh lực hút tĩnh điện giữa các ion, biến nước thành dung môi vạn năng hòa tan muối vô cơ và phân tử phân cực.",
        "Nhiệt dung riêng cao (1 cal/g/°C = 4.184 J/g/°C): Đóng vai trò bộ đệm nhiệt khổng lồ, bảo vệ cơ thể khỏi những dao động nhiệt độ đột ngột của môi trường.",
        "Nhiệt bay hơi cao (540 cal/g ở 100°C, ~580 cal/g ở 37°C): Bay hơi mồ hôi qua da và hơi thở là phương thức thải nhiệt hiệu quả sống còn khi sốt cao hoặc gắng sức.",
        "Mạng lưới liên kết hydro linh động: Mỗi phân tử nước tạo tối đa 4 liên kết hydro với các phân tử lân cận, tạo sức căng bề mặt lớn và độ nhớt thích hợp cho dòng máu mao mạch."
    ],
    "Nhờ hằng số điện môi cực cao (D=80), nước làm suy yếu lực hút Coulomb giữa Na+ và Cl- tới 80 lần, giúp muối NaCl tự phân ly hoàn toàn thành các ion tự do khi hòa tan."
))

cards.append(make_card(
    "HS15-B1-02", "Nước Tự do vs Nước Kết hợp", "HÓA SINH NƯỚC",
    "Phân biệt tỷ lệ, đặc tính lý hóa và vai trò sinh học giữa Nước tự do và Nước kết hợp trong cơ thể?",
    [
        "Nước tự do (Chiếm 90 - 95% TBW): Tồn tại linh động, đóng băng ở 0°C; làm dung môi hòa tan chất dinh dưỡng, chất chuyển hóa, là môi trường diễn ra mọi phản ứng hóa sinh và bài xuất cặn bã qua nước tiểu/phân.",
        "Nước kết hợp / Áo hydrat hóa (Chiếm 5 - 10% TBW): Liên kết tĩnh điện hoặc lưỡng cực chặt chẽ với các nhóm tích điện trên bề mặt protein, acid nucleic, glycogen, proteoglycan.",
        "Đặc điểm của nước kết hợp: Không đóng băng ở 0°C, không tham gia làm dung môi hòa tan, tốc độ khuếch tán bị hạn chế tối đa.",
        "Vai trò của nước kết hợp: Tạo 'áo hydrat hóa' bảo vệ cấu trúc bậc 3, bậc 4 của protein enzym không bị biến tính hay kết tủa; duy trì trạng thái gel đàn hồi của chất nền mô liên kết."
    ],
    "Mất lớp áo hydrat hóa (ví dụ khi thêm cồn hoặc muối nồng độ cao) làm các phân tử protein bộc lộ bề mặt kỵ nước, dính lại với nhau và kết tủa (hiện tượng muối tích phân - salting out)."
))

cards.append(make_card(
    "HS15-B1-03", "Tổng Lượng Nước Cơ thể (TBW)", "PHÂN BỐ THỂ DỊCH",
    "Tổng lượng nước cơ thể (TBW) chiếm bao nhiêu phần trăm trọng lượng và các yếu tố sinh lý ảnh hưởng như thế nào?",
    [
        "Tỷ lệ chuẩn ở người trưởng thành: TBW trung bình chiếm 60% trọng lượng cơ thể (khoảng 42 lít ở người nặng 70 kg).",
        "Tuổi tác: Trẻ sơ sinh TBW chiếm 75 - 80% (rất dễ sốc mất nước khi nôn trớ/tiêu chảy); Người cao tuổi (> 65 tuổi) TBW giảm chỉ còn 45 - 50% do giảm khối cơ và tăng tỷ lệ mỡ.",
        "Giới tính: Nam giới (~60%) cao hơn Nữ giới (~50 - 55%) do phụ nữ có tỷ lệ mô mỡ dưới da cao hơn dưới ảnh hưởng của estrogen.",
        "Thể trạng mô mỡ vs mô cơ: Mô cơ bắp chứa tới 73 - 75% nước, trong khi mô mỡ chỉ chứa khoảng 10% nước → người béo phì có tỷ lệ TBW trên tổng trọng lượng thấp hơn nhiều so với người gầy."
    ],
    "Ở bệnh nhân béo phì, khi tính liều bù dịch hoặc tính liều thuốc tan trong nước (như Aminoglycoside, Vancomycin), bắt buộc phải tính theo Cân nặng lý tưởng (Ideal Body Weight) để tránh quá liều ngộ độc."
))

cards.append(make_card(
    "HS15-B1-04", "Phân bố Dịch Nội bào vs Ngoại bào", "PHÂN BỐ THỂ DỊCH",
    "Trình bày thể tích và thành phần ion đặc trưng phân biệt giữa Dịch nội bào (ICF) và Dịch ngoại bào (ECF)?",
    [
        "Dịch nội bào (ICF): Chiếm 55 - 60% TBW (~35 - 40% trọng lượng cơ thể, ~28 lít ở người 70 kg); Nằm bên trong tất cả tế bào.",
        "Ion đặc trưng của ICF: Cation chính là K+ và Mg2+; Anion chính là Phosphat hữu cơ (HPO4 2-, ATP) và Proteinat tích điện âm; Nồng độ Na+ và Cl- rất thấp.",
        "Dịch ngoại bào (ECF): Chiếm 40 - 45% TBW (~20% trọng lượng cơ thể, ~14 lít ở người 70 kg); Là môi trường nội môi trực tiếp của tế bào.",
        "Ion đặc trưng của ECF: Cation chính là Na+; Anion chính là Cl- và Bicarbonat (HCO3-)."
    ],
    "Màng tế bào bán thấm ngăn cách giữa ICF và ECF, cho phép nước thẩm thấu tự do nhưng duy trì sự bất đối xứng ion tuyệt đối nhờ hoạt động liên tục của bơm Na+-K+-ATPase."
))

cards.append(make_card(
    "HS15-B1-05", "Các Khoang Dịch Ngoại bào (ECF)", "PHÂN BỐ THỂ DỊCH",
    "Phân chia các ngăn dịch thuộc Dịch ngoại bào (ECF) và khái niệm Khoang thứ ba (Third Spacing)?",
    [
        "Dịch kẽ (Interstitial Fluid - ISF): Chiếm 3/4 ECF (~15% trọng lượng cơ thể, ~10.5 lít); Bao quanh tế bào và mạch bạch huyết, là cầu nối trao đổi chất trực tiếp giữa mao mạch và tế bào.",
        "Huyết tương (Plasma): Chiếm 1/4 ECF (~4 - 5% trọng lượng cơ thể, ~3.5 lít); Là phần dịch lỏng của máu lưu thông trong lòng mạch (thể tích máu toàn phần ~5 lít gồm huyết tương và hồng cầu).",
        "Dịch xuyên bào (Transcellular Fluid): Thể tích nhỏ (~1 - 2 lít), bài tiết qua biểu mô vào các khoang kín: dịch não tủy, dịch khớp, dịch màng phổi, màng bụng, dịch tiêu hóa.",
        "Hiện tượng Khoang thứ ba (Third Spacing): Sự tích tụ bất thường một lượng dịch khổng lồ vào khoang xuyên bào (viêm phúc mạc, tắc ruột, viêm tụy cấp, bỏng rộng) gây suy giảm thể tích tuần hoàn hiệu dụng dẫn đến sốc giảm thể tích."
    ],
    "Dịch kẽ và huyết tương có thành phần ion giống hệt nhau, chỉ khác biệt duy nhất là huyết tương có nồng độ protein (Albumin) cao hơn nhiều, tạo áp suất keo giữ nước trong lòng mạch."
))

cards.append(make_card(
    "HS15-B1-06", "Bilan Nước Xuất - Nhập", "CÂN BẰNG THỂ DỊCH",
    "Các đường nhập và xuất nước trong cân bằng Bilan nước hàng ngày ở người trưởng thành khỏe mạnh (2.000 - 2.500 mL/ngày)?",
    [
        "Đường nhập nước: Nước uống trực tiếp (1.200 - 1.500 mL) + Nước trong thức ăn (700 - 1.000 mL) + Nước nội sinh do oxy hóa chuyển hóa (200 - 300 mL). Tổng nhập: 2.100 - 2.800 mL/ngày.",
        "Đường xuất nước: Nước tiểu qua thận (1.200 - 1.500 mL) + Mồ hôi bài tiết qua da (400 - 500 mL) + Hơi ẩm thở qua phổi (300 - 400 mL) + Phân qua đường tiêu hóa (100 - 200 mL). Tổng xuất: 2.100 - 2.800 mL/ngày.",
        "Nước nội sinh chuyển hóa: Oxy hóa 100g Lipid tạo 107g H2O; 100g Glucid tạo 60g H2O; 100g Protid tạo 41g H2O.",
        "Nguyên tắc cân bằng: Tổng nhập = Tổng xuất (Bilan = 0) giúp duy trì hằng định thể tích dịch cơ thể."
    ],
    "Lạc đà có thể nhịn uống nước nhiều tuần giữa sa mạc nhờ chuyển hóa nguồn mỡ khổng lồ ở bướu để sinh ra lượng nước nội sinh nuôi sống cơ thể."
))

cards.append(make_card(
    "HS15-B1-07", "Mất nước Vô cảm & Ảnh hưởng của Sốt", "LÂM SÀNG THỂ DỊCH",
    "Định nghĩa Mất nước vô cảm (Insensible Water Loss) và sự biến đổi của nó khi bệnh nhân sốt cao?",
    [
        "Định nghĩa: Lượng nước bay hơi liên tục không cảm nhận được qua bề mặt da (không phải mồ hôi hoạt động) và qua hơi ẩm thở của đường hô hấp.",
        "Thể tích bình thường: Dao động khoảng 700 - 900 mL/ngày (trong đó qua da ~400 - 500 mL, qua phổi ~300 - 400 mL).",
        "Đặc tính sinh hóa: Là nước nguyên chất tinh khiết, hoàn toàn không chứa muối điện giải.",
        "Biến đổi khi sốt: Cứ mỗi khi thân nhiệt tăng thêm 1°C trên 37°C, lượng nước mất vô cảm tăng thêm 10 - 13% (khoảng 100 - 150 mL/ngày); thở nhanh sâu cũng làm tăng mất nước qua phổi."
    ],
    "Khi lập bilan dịch cho bệnh nhân sốt cao, thở máy hoặc nằm phòng điều hòa khô, bác sĩ bắt buộc phải tính bù thêm lượng mất nước vô cảm này để tránh mất nước ưu trương tiềm ẩn."
))

cards.append(make_card(
    "HS15-B1-08", "Nước tiểu Tối thiểu Bắt buộc", "SINH LÝ HÓA SINH THẬN",
    "Khái niệm Thể tích nước tiểu tối thiểu bắt buộc (Obligatory Urine Volume) và công thức tính toán dựa trên tải chất tan?",
    [
        "Khái niệm: Lượng nước tiểu ít nhất mà thận bắt buộc phải bài xuất mỗi ngày để hòa tan và đào thải toàn bộ chất cặn bã chuyển hóa (urê, creatinin, acid uric, muối điện giải).",
        "Tải chất tan chuyển hóa hàng ngày: Một người trưởng thành bình thường tạo ra khoảng 600 mOsm chất tan cần bài tiết mỗi ngày.",
        "Khả năng cô đặc tối đa của thận: Ống thận người có thể cô đặc nước tiểu tối đa đạt 1.200 mOsm/kg H2O.",
        "Công thức tính thể tích tối thiểu: Thể tích = 600 mOsm/ngày ÷ 1.200 mOsm/L = 0.5 L/ngày = 500 mL/ngày.",
        "Ý nghĩa lâm sàng: Nếu lượng nước tiểu < 500 mL/ngày (thiểu niệu), thận không thể thải hết chất tan chuyển hóa, bệnh nhân sẽ nhanh chóng bị ứ trệ độc chất nitơ máu (tăng urê, creatinin máu)."
    ],
    "Người cao tuổi hoặc bệnh nhân suy thận mạn có khả năng cô đặc nước tiểu kém (tối đa chỉ 400-600 mOsm/L), do đó thể tích nước tiểu bắt buộc phải cao hơn (1-1.5 lít/ngày) để tránh suy thận tiến triển."
))

cards.append(make_card(
    "HS15-B1-09", "Cơ chế Trao đổi Dịch giữa ICF và ECF", "ĐỘNG HỌC THỂ DỊCH",
    "Quy luật trao đổi nước giữa Dịch nội bào (ICF) và Dịch ngoại bào (ECF) phụ thuộc vào yếu tố nào?",
    [
        "Màng tế bào bán thấm hoàn toàn với nước: Nước tự do thẩm thấu qua màng tế bào cực nhanh (nhờ kênh Aquaporin) cho đến khi áp suất thẩm thấu giữa ICF và ECF đạt trạng thái cân bằng tuyệt đối.",
        "Yếu tố quyết định dịch chuyển: Áp suất thẩm thấu hiệu dụng (Tonicity) của dịch ngoại bào ECF.",
        "Khi ECF ưu trương (tăng nồng độ chất tan không qua màng như Na+, glucose): Nước bị kéo từ trong tế bào ICF ra ECF → tế bào bị teo rút mất nước nội bào.",
        "Khi ECF nhược trương (hạ nồng độ chất tan hoặc thừa nước tự do): Nước từ ECF ồ ạt tràn vào trong tế bào ICF → tế bào trương phồng, phù nề nội bào (nguy hiểm nhất ở tế bào não)."
    ],
    "Áp suất thẩm thấu ở trạng thái cân bằng giữa ICF và ECF luôn bằng nhau. Sự thay đổi thẩm thấu ban đầu luôn bắt đầu từ ngăn ngoại bào ECF, sau đó kéo theo sự dịch chuyển nước của ngăn nội bào ICF."
))

cards.append(make_card(
    "HS15-B1-10", "Dịch Xuyên bào & Khoang thứ ba", "LÂM SÀNG NGOẠI KHOA",
    "Hậu quả sinh lý bệnh của hiện tượng thoát dịch vào Khoang thứ ba (Third Spacing) trong viêm tụy cấp và tắc ruột?",
    [
        "Bản chất hiện tượng: Dịch huyết tương và điện giải thoát quản ồ ạt tích tụ vào các khoang cơ thể không tham gia trao đổi dịch bình thường (lòng ruột giãn chướng, khoang phúc mạc, khoang sau phúc mạc).",
        "Mất nước không làm thay đổi cân nặng: Thể tích dịch này vẫn nằm trong cơ thể nên cân nặng bệnh nhân không giảm, nhưng hoàn toàn mất khỏi tuần hoàn chức năng.",
        "Hậu quả huyết động: Tụt giảm thể tích tuần hoàn hiệu dụng (Effective Circulating Volume) → tụt huyết áp, giảm tưới máu thận, suy thận cấp trước thận và sốc giảm thể tích.",
        "Chiến lược hồi sức: Đòi hỏi bù một lượng lớn dung dịch tinh thể đẳng trương (NaCl 0.9% hoặc Ringer Lactate) theo dõi sát áp lực tĩnh mạch trung tâm (CVP) và lượng nước tiểu."
    ],
    "Trong viêm tụy cấp thể hoại tử nặng, lượng dịch thoát vào khoang sau phúc mạc và khoang phúc mạc có thể lên tới 4 - 6 lít trong 24 giờ đầu."
))

# ==============================================================================
# B2: ÁP SUẤT THẨM THẤU, ÁP SUẤT KEO & ĐỘNG HỌC TRAO ĐỔI DỊCH (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B2-01", "Áp suất Thẩm thấu Sinh lý", "ÁP SUẤT THẨM THẤU",
    "Nêu khoảng giá trị sinh lý của Áp suất thẩm thấu huyết tương và công thức tính Áp suất thẩm thấu lý thuyết?",
    [
        "Giá trị sinh lý bình thường: Áp suất thẩm thấu huyết tương dao động từ 280 đến 295 mOsm/kg H2O.",
        "Công thức tính áp suất thẩm thấu lý thuyết (Posm tính toán): Posm = 2 × [Na+] + Glucose + Ure (với tất cả nồng độ tính bằng mmol/L).",
        "Hệ số 2 của ion Natri: Nhân đôi nồng độ Natri vì để cân bằng điện tích, mỗi cation Na+ luôn đi kèm một anion tương đương (chủ yếu là Cl- và HCO3-).",
        "Đóng góp của Natri: Muối Natri đóng góp tới > 90% tổng áp suất thẩm thấu của dịch ngoại bào."
    ],
    "Nếu tính theo đơn vị mg/dL: Posm = 2 × [Na+] (mEq/L) + Glucose (mg/dL)/18 + BUN (mg/dL)/2.8."
))

cards.append(make_card(
    "HS15-B2-02", "Áp suất Thẩm thấu Hiệu dụng (Tonicity)", "ÁP SUẤT THẨM THẤU",
    "Phân biệt Áp suất thẩm thấu toàn phần (Osmolality) và Áp suất thẩm thấu hiệu dụng (Tonicity)?",
    [
        "Áp suất thẩm thấu toàn phần (Osmolality): Tổng nồng độ của TẤT CẢ các chất tan hòa tan trong dung dịch (gồm Na+, Cl-, HCO3-, Glucose và Ure).",
        "Áp suất thẩm thấu hiệu dụng (Tonicity): Chỉ tính nồng độ của các chất tan KHÔNG THỂ thấm tự do qua màng tế bào (chủ yếu là Na+ và Glucose), có khả năng tạo lực hút kéo nước qua màng.",
        "Công thức tính Tonicity: Tonicity = 2 × [Na+] + Glucose (mmol/L).",
        "Tại sao loại trừ Ure khỏi Tonicity: Ure là một chất tan thẩm thấu không hiệu dụng (ineffective osmole) vì nó khuếch tán tự do qua màng tế bào theo kênh UT, nồng độ ure trong và ngoài tế bào nhanh chóng cân bằng nên không tạo lực kéo nước."
    ],
    "Tăng Ure máu đơn thuần (trong suy thận) làm tăng áp suất thẩm thấu toàn phần nhưng không làm thay đổi Tonicity, do đó không gây teo rút tế bào não."
))

cards.append(make_card(
    "HS15-B2-03", "Khoảng trống Thẩm thấu (Osmolar Gap)", "XÉT NGHIỆM ĐỘC CHẤT",
    "Định nghĩa Khoảng trống Thẩm thấu (Osmolar Gap) và ý nghĩa lâm sàng trong chẩn đoán ngộ độc cồn độc?",
    [
        "Định nghĩa: Hiệu số giữa Áp suất thẩm thấu đo được trực tiếp bằng máy đo độ hạ băng điểm (Posm đo) và Áp suất thẩm thấu tính toán theo công thức lý thuyết (Posm tính).",
        "Công thức: Khoảng trống thẩm thấu = Posm đo - Posm tính toán.",
        "Giá trị bình thường: Dưới 10 mOsm/kg H2O (do sự có mặt của một lượng nhỏ ion Ca2+, Mg2+, acid amin).",
        "Ý nghĩa khi Khoảng trống thẩm thấu > 10 mOsm/kg: Báo hiệu sự hiện diện của các phân tử lạ có trọng lượng phân tử nhỏ chưa được tính đến, kinh điển nhất là ngộ độc cồn độc: Methanol (cồn công nghiệp), Ethylene glycol (dung dịch chống đông), Isopropanol, Ethanol hoặc truyền nhiều Mannitol/Propylene glycol."
    ],
    "Bệnh nhân toan chuyển hóa tăng khoảng trống anion (High Anion Gap Metabolic Acidosis) kèm tăng khoảng trống thẩm thấu (> 10) là dấu hiệu khẳng định ngộ độc Methanol hoặc Ethylene glycol."
))

cards.append(make_card(
    "HS15-B2-04", "Áp suất Keo Huyết tương", "ÁP SUẤT KEO",
    "Nêu giá trị sinh lý của Áp suất keo huyết tương (Oncotic Pressure) và vai trò quyết định của protein Albumin?",
    [
        "Giá trị sinh lý: Áp suất keo huyết tương dao động từ 25 đến 28 mmHg.",
        "Bản chất: Là phần áp suất thẩm thấu được tạo ra bởi các đại phân tử protein huyết tương không thể lọt qua các khe hở nội mô mao mạch bình thường.",
        "Vai trò áp đảo của Albumin: Albumin đảm nhiệm tới 75 - 80% tổng áp suất keo huyết tương nhờ 2 yếu tố: (1) Nồng độ phân tử cao nhất trong huyết tương (35 - 50 g/L); (2) Trọng lượng phân tử nhỏ nhất (66.5 kDa) nên tạo số lượng hạt thẩm thấu lớn nhất trên một đơn vị khối lượng.",
        "Hiệu ứng Gibbs-Donnan: Albumin tích điện âm ở pH 7.4 giữ lại một lượng lớn cation Na+ xung quanh, làm tăng thêm áp suất thẩm thấu keo thực tế thêm khoảng 50% so với lý thuyết thuần túy."
    ],
    "Globulin có nồng độ thấp hơn và trọng lượng phân tử lớn hơn nhiều (150-900 kDa), do đó đóng góp vào áp suất keo rất ít so với Albumin."
))

cards.append(make_card(
    "HS15-B2-05", "Định luật Starling Mao mạch", "TRAO ĐỔI DỊCH MAO MẠCH",
    "Phương trình Định luật Starling về sự trao đổi dịch qua thành mao mạch và ý nghĩa các thông số?",
    [
        "Phương trình Starling: Jv = Kf × [(Pc - Pi) - σ × (πc - πi)].",
        "Jv: Lưu lượng dịch di chuyển ròng qua thành mao mạch (dương = lọc dịch ra khoang kẽ; âm = tái hấp thu vào lòng mạch).",
        "Kf (Hệ số lọc mao mạch): Phụ thuộc diện tích bề mặt và tính thấm nước của thành mao mạch.",
        "Pc và Pi: Áp lực thủy tĩnh của lòng mao mạch (Pc) và của dịch kẽ (Pi) → Lực đẩy dịch ra ngoài.",
        "πc và πi: Áp suất keo của huyết tương (πc) và của dịch kẽ (πi) → Lực kéo dịch giữ lại lòng mạch.",
        "σ (Hệ số phản xạ protein): Dao động từ 0 (thấm tự do) đến 1 (màng cản protein hoàn toàn, mao mạch bình thường σ ~ 0.9 - 0.95)."
    ],
    "Ở đầu mao động mạch: Pc (35 mmHg) > πc (25 mmHg) → áp lực lọc dương (~10 mmHg) đẩy dịch ra mô kẽ. Ở đầu mao tĩnh mạch: Pc tụt xuống 15 mmHg < πc (25 mmHg) → áp lực hút âm (~9 mmHg) kéo dịch trở lại mao mạch."
))

cards.append(make_card(
    "HS15-B2-06", "Vai trò Dẫn lưu Bạch huyết", "SINH LÝ THỂ DỊCH",
    "Vai trò của Hệ tuần hoàn bạch huyết trong việc duy trì cân bằng dịch kẽ và phòng ngừa phù nề?",
    [
        "Thu gom lượng dịch lọc dư thừa: Bình thường mỗi ngày có khoảng 20 lít dịch được lọc ra mô kẽ ở đầu mao động mạch, nhưng chỉ có 17 lít được tái hấp thu ở đầu mao tĩnh mạch.",
        "Dẫn lưu 3 lít dịch/ngày: Lượng dịch dư thừa 2 - 3 lít/ngày cùng toàn bộ các phân tử protein bị rò rỉ ra dịch kẽ được các mao mạch bạch huyết thu gom đưa về ống ngực đổ vào tĩnh mạch dưới đòn.",
        "Duy trì áp suất keo dịch kẽ thấp: Bạch huyết là con đường DUY NHẤT dọn sạch protein bị rò rỉ ra khỏi dịch kẽ, giữ cho áp suất keo dịch kẽ (πi) luôn ở mức rất thấp (~1 - 3 mmHg).",
        "Hậu quả khi tắc bạch huyết: Tắc nghẽn mạch bạch huyết làm protein tích tụ trong mô kẽ, kéo nước ra ngoài gây phù bạch huyết (Lymphedema) trơ lì không lõm."
    ],
    "Nếu hệ bạch huyết ngừng hoạt động, một người bình thường sẽ chết trong vòng 24 giờ do cạn kiệt thể tích huyết tương tuần hoàn và phù nề mô kẽ toàn thân."
))

cards.append(make_card(
    "HS15-B2-07", "Cơ chế Phù do Giảm Áp suất Keo", "BỆNH SINH PHÂN TỬ",
    "Cơ chế bệnh sinh phân tử gây Phù toàn thân do Giảm áp suất keo huyết tương trong Hội chứng thận hư và Xơ gan?",
    [
        "Nguyên nhân suy giảm Albumin huyết tương: Hội chứng thận hư (mất qua màng lọc cầu thận tổn thương > 3.5 g/24h); Xơ gan (tế bào gan suy thoái giảm tổng hợp albumin < 25 g/L); Suy dinh dưỡng thiếu đạm (Kwashiorkor).",
        "Áp suất keo huyết tương tụt giảm (πc < 15 - 20 mmHg): Lực giữ nước trong lòng mạch bị phá vỡ, áp lực lọc theo định luật Starling vượt trội kéo nước và muối ồ ạt thoát ra mô kẽ.",
        "Phù toàn thân mềm trắng ấn lõm: Phù phân bố toàn thân, xuất hiện đầu tiên ở mô lỏng lẻo (mi mắt, mặt) rồi lan xuống chi dưới và tràn dịch đa màng (cổ trướng, màng phổi).",
        "Vòng xoắn bệnh lý kích hoạt RAAS: Thoát dịch làm giảm thể tích tuần hoàn hiệu dụng → kích hoạt hệ thống thần kinh giao cảm và hệ RAAS tăng giữ muối nước tại thận, làm phù ngày càng trầm trọng."
    ],
    "Điều trị phù trong hội chứng thận hư bằng thuốc lợi tiểu đơn thuần có thể gây tụt huyết áp và suy thận cấp; bắt buộc phải phối hợp truyền Albumin nồng độ cao (20%) để kéo nước từ mô kẽ vào lòng mạch trước khi dùng lợi tiểu."
))

cards.append(make_card(
    "HS15-B2-08", "Cơ chế Phù do Tăng Áp lực Thủy tĩnh", "BỆNH SINH PHÂN TỬ",
    "Cơ chế bệnh sinh của Phù do Tăng áp lực thủy tĩnh mao mạch trong Suy tim ứ huyết?",
    [
        "Suy tim ứ trệ tuần hoàn: Thất phải hoặc thất trái suy giảm chức năng bơm máu làm ứ trệ máu ở hệ tĩnh mạch ngoại vi hoặc tuần hoàn phổi.",
        "Tăng áp lực tĩnh mạch trung tâm và mao mạch (Pc tăng cao): Pc ở đầu mao mạch tăng vượt quá áp suất keo huyết tương πc dọc theo toàn bộ chiều dài mao mạch.",
        "Dịch thoát liên tục ra mô kẽ: Sự tái hấp thu dịch ở đầu mao tĩnh mạch bị triệt tiêu hoàn toàn, dịch thoát ra mô kẽ vượt quá khả năng dẫn lưu tối đa của hệ bạch huyết.",
        "Suy tim trái gây Phù phổi cấp: Tăng áp lực mao mạch phổi bít (PCWP > 20 - 25 mmHg) đẩy dịch vào phế nang gây ngạt thở; Suy tim phải gây Phù ngoại vi chi dưới, gan to ứ máu và phản hồi gan - tĩnh mạch cổ dương tính."
    ],
    "Cơ chế tự bảo vệ của mô kẽ khi áp lực thủy tĩnh tăng là rửa trôi protein dịch kẽ (washdown), làm giảm πi giúp hạn chế phần nào mức độ phù nề."
))

cards.append(make_card(
    "HS15-B2-09", "Phù do Tăng Tính thấm & Tắc Bạch huyết", "BỆNH SINH PHÂN TỬ",
    "Phân biệt cơ chế và đặc điểm phù giữa Tăng tính thấm thành mạch và Tắc nghẽn mạch bạch huyết?",
    [
        "Cơ chế Tăng tính thấm thành mạch (Kf tăng, σ giảm): Các chất trung gian hóa học gây viêm (Histamin, Bradykinin, Leukotriene) làm co tế bào nội mô, mở rộng khe hở nội mô mao mạch.",
        "Đặc điểm phù tăng tính thấm: Protein huyết tương thoát tự do ra dịch kẽ làm tăng áp suất keo mô kẽ (πi tăng) kéo nước ồ ạt theo; phù thường khu trú tại ổ viêm kèm sưng nóng đỏ đau hoặc phù mạch dị ứng (Quincke), sốc phản vệ, bỏng nặng.",
        "Cơ chế Tắc nghẽn mạch bạch huyết: Tắc đường dẫn lưu bạch huyết do ấu trùng giun chỉ Wuchereria bancrofti, tế bào ung thư di căn hoặc nạo vét hạch phẫu thuật, xạ trị.",
        "Đặc điểm phù bạch huyết (Lymphedema): Phù khu trú một bên chi, giai đoạn muộn mô kẽ bị xơ hóa làm da dày cứng xù xì không ấn lõm (bệnh chân voi)."
    ],
    "Phù trong phản vệ là cấp cứu tối khẩn; tiêm bắp Adrenalin (Epinephrine) là thuốc cứu sinh số 1 giúp co mạch làm giảm áp lực thủy tĩnh mao mạch và ổn định tế bào mast."
))

cards.append(make_card(
    "HS15-B2-10", "Dịch Thấm vs Dịch Tiết", "CẬN LÂM SÀNG",
    "Tiêu chuẩn phân biệt giữa Dịch thấm (Transudate) và Dịch tiết (Exudate) trong tràn dịch màng theo Tiêu chuẩn Light?",
    [
        "Bản chất cơ chế hình thành: Dịch thấm do rối loạn các yếu tố huyết động cơ học (tăng áp lực thủy tĩnh Pc hoặc giảm áp suất keo πc, màng mao mạch còn nguyên vẹn); Dịch tiết do tổn thương viêm hoặc tăng tính thấm thành mạch (viêm màng phổi, ung thư, lao).",
        "Tiêu chuẩn Light (Dịch màng phổi là Dịch tiết khi thỏa mãn ít nhất 1 trong 3 tiêu chuẩn):",
        "   - 1) Tỷ lệ Protein dịch màng / Protein huyết thanh > 0.5.",
        "   - 2) Tỷ lệ LDH dịch màng / LDH huyết thanh > 0.6.",
        "   - 3) Nồng độ LDH dịch màng > 2/3 giới hạn trên bình thường của LDH huyết thanh.",
        "Đặc điểm dịch thấm: Protein < 30 g/L, Rivalta âm tính, tế bào ít (< 1.000/µL), LDH thấp; Điển hình trong suy tim, xơ gan, hội chứng thận hư."
    ],
    "Định lượng Protein và LDH dịch màng là bước phân loại đầu tiên bắt buộc giúp bác sĩ định hướng nguyên nhân toàn thân (dịch thấm) hay nguyên nhân tổn thương tại chỗ (dịch tiết)."
))

# ==============================================================================
# B3: CÁC ION ĐIỆN GIẢI CHỦ YẾU TRONG CƠ THỂ (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B3-01", "Hóa sinh Ion Natri (Na+)", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và 3 vai trò sinh học tối quan trọng của Ion Natri (Na+)?",
    [
        "Nồng độ sinh lý bình thường: 135 đến 145 mmol/L (mEq/L); là cation dồi dào nhất của dịch ngoại bào ECF.",
        "Quyết định thể tích dịch ngoại bào ECF: Natri cùng anion đi kèm chiếm > 90% tổng số hạt thẩm thấu ECF; tổng lượng Natri trong cơ thể quyết định trực tiếp thể tích dịch ngoại bào và huyết áp động mạch.",
        "Quyết định Áp suất thẩm thấu hiệu dụng (Tonicity): Mọi sự biến thiên nồng độ Na+ máu đều gây xáo trộn thẩm thấu kéo theo sự dịch chuyển nước giữa tế bào và dịch kẽ.",
        "Tạo thế năng điện hóa cho màng: Dòng Na+ đi vào qua kênh Nav phát sinh điện thế hoạt động khử cực tế bào cơ tim và thần kinh; cung cấp năng lượng cho hệ thống vận chuyển tích cực thứ phát (SGLT, NCX, NHE1)."
    ],
    "Cơ thể có hệ thống cảm biến thể tích dịch (Baroreceptors) và cảm biến thẩm thấu (Osmoreceptors) tinh vi phối hợp để điều hòa nồng độ Natri máu trong ranh giới cực kỳ hẹp."
))

cards.append(make_card(
    "HS15-B3-02", "Hóa sinh Ion Kali (K+)", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và vai trò của tỷ số Kali nội bào / ngoại bào trong điện thế nghỉ màng tế bào?",
    [
        "Nồng độ sinh lý bình thường: 3.5 đến 5.0 mmol/L; là cation chiếm ưu thế tuyệt đối của dịch nội bào ICF (140 - 150 mmol/L).",
        "Phân bố phân tử: Khoảng 98% tổng lượng Kali cơ thể nằm trong nội bào tế bào, chỉ có 2% nằm ở dịch ngoại bào.",
        "Quyết định điện thế nghỉ màng (Em): Tỷ số nồng độ [K+] nội bào / [K+] ngoại bào quyết định điện thế nghỉ của màng tế bào thần kinh và cơ theo Phương trình Nernst: Em = -61 × log([K+]in / [K+]out) ≈ -70 đến -90 mV.",
        "Tính nhạy cảm sinh tử: Vì lượng K+ ngoại bào rất nhỏ, chỉ cần sự thay đổi nhỏ nồng độ K+ huyết tương (tăng hoặc giảm 1-2 mmol/L) cũng làm đảo lộn tỷ số [K+]in/[K+]out, gây biến đổi sâu sắc tính hưng phấn cơ tim dẫn đến loạn nhịp tim tử vong."
    ],
    "Cơ thể duy trì nồng độ K+ ngoại bào thấp nhờ hoạt động liên tục của bơm Na+-K+-ATPase và sự điều hòa bài tiết K+ tại ống góp thận bởi hormone Aldosteron."
))

cards.append(make_card(
    "HS15-B3-03", "Hóa sinh Ion Clorid (Cl-)", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và 3 vai trò sinh học chủ chốt của Ion Clorid (Cl-)?",
    [
        "Nồng độ sinh lý bình thường: 98 đến 106 mmol/L; là anion chính chiếm ưu thế của dịch ngoại bào ECF.",
        "Duy trì trung hòa điện tích: Đồng hành với cation Na+ duy trì cân bằng điện tích dịch ngoại bào; biến đổi nồng độ Cl- thường song hành cùng Na+.",
        "Quan hệ đối vận với Bicarbonat: Để duy trì cân bằng anion ngoại bào, khi nồng độ HCO3- giảm (trong toan chuyển hóa bình thường anion gap) thì nồng độ Cl- tăng bù trừ (toan chuyển hóa tăng clo máu) và ngược lại.",
        "Tham gia bài tiết acid dịch vị và chức năng màng: Là cơ chất của bơm proton dạ dày tạo HCl và thành phần của kênh CFTR điều hòa độ quánh dịch nhầy biểu mô."
    ],
    "Mất dịch dạ dày do nôn ói nhiều làm mất một lượng lớn ion Cl- và H+, gây ra rối loạn kiềm chuyển hóa kèm hạ clo máu (Hypochloremic metabolic alkalosis)."
))

cards.append(make_card(
    "HS15-B3-04", "Hóa sinh Ion Bicarbonat (HCO3-)", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và vai trò của Hệ đệm Bicarbonat (HCO3-/CO2) trong cân bằng Acid-Base?",
    [
        "Nồng độ sinh lý bình thường: 22 đến 26 mmol/L (mEq/L); là anion đệm chủ lực của dịch ngoại bào.",
        "Thành phần của hệ đệm mở hoàn hảo: Phối hợp giữa HCO3- (điều hòa bởi thận) và CO2 hòa tan (điều hòa bởi phổi) theo phương trình Henderson-Hasselbalch: pH = 6.1 + log([HCO3-] / 0.03 × PaCO2).",
        "Tái hấp thu tại thận: Khoảng 85 - 90% lượng HCO3- lọc qua cầu thận được tái hấp thu ở ống lượn gần nhờ enzyme Carbonic Anhydrase (CA); phần còn lại được tái hấp thu và sinh mới tại ống lượn xa và ống góp.",
        "Ý nghĩa trong khí máu: Nồng độ HCO3- máu phản ánh trực tiếp thành phần chuyển hóa của thăng bằng toan kiềm (giảm trong toan chuyển hóa, tăng trong kiềm chuyển hóa)."
    ],
    "Hệ đệm Bicarbonat là hệ đệm quyền lực nhất cơ thể không phải vì pKa gần pH sinh lý (pKa=6.1), mà vì nồng độ cả hai thành phần axit (CO2 qua thở) và bazo (HCO3- qua thận) đều được điều hòa độc lập bởi hai cơ quan sống còn."
))

cards.append(make_card(
    "HS15-B3-05", "Calci Toàn phần vs Calci Ion hóa", "ĐIỆN GIẢI HỌC",
    "Phân biệt các dạng Calci trong máu và Công thức hiệu chỉnh Calci toàn phần theo nồng độ Albumin huyết tương?",
    [
        "Nồng độ Calci toàn phần: 2.15 đến 2.55 mmol/L (8.5 - 10.2 mg/dL).",
        "Ba dạng tồn tại trong huyết tương: Calci ion hóa tự do (Ca2+ tự do chiếm 50%, ~1.15 - 1.35 mmol/L, là dạng DUY NHẤT có hoạt tính sinh học); Calci gắn Protein (chiếm 40 - 45%, chủ yếu gắn Albumin); Calci phức hợp với anion hữu cơ (chiếm 5 - 10%, phức hợp với citrate, phosphat).",
        "Ảnh hưởng của Albumin: Cứ mỗi khi Albumin huyết tương giảm 10 g/L (hoặc 1 g/dL), nồng độ Calci toàn phần giảm giả tạo khoảng 0.2 mmol/L (0.8 mg/dL) trong khi Calci ion hóa tự do vẫn hoàn toàn bình thường.",
        "Công thức hiệu chỉnh Calci theo Albumin: Ca hiệu chỉnh (mmol/L) = Ca đo được (mmol/L) + 0.02 × (40 - Albumin g/L). Hoặc theo đơn vị mg/dL: Ca hiệu chỉnh = Ca đo được + 0.8 × (4.0 - Albumin g/dL)."
    ],
    "Ở bệnh nhân suy dinh dưỡng, xơ gan hoặc hội chứng thận hư có Albumin máu giảm nặng, bắt buộc phải định lượng trực tiếp Calci ion hóa (iCa) hoặc tính Ca hiệu chỉnh để tránh chẩn đoán nhầm hạ calci máu."
))

cards.append(make_card(
    "HS15-B3-06", "Điều hòa Calci Máu (PTH, Calcitriol, Calcitonin)", "HÓA SINH NỘI TIẾT",
    "Tác động đối kháng và hiệp đồng của 3 hormone PTH, Calcitriol và Calcitonin trong điều hòa nồng độ Calci máu?",
    [
        "PTH (Parathyroid Hormone do tuyến cận giáp tiết khi Ca2+ giảm): Tăng huy động Ca2+ từ xương (kích hoạt hủy cốt bào); Tăng tái hấp thu Ca2+ và ức chế tái hấp thu Phosphat tại ống thận; Kích hoạt enzyme 1-alpha-hydroxylase tại thận chuyển hóa Vitamin D thành Calcitriol.",
        "Calcitriol (1,25-(OH)2-D3): Tăng cường hấp thu tích cực cả Calci và Phosphat tại niêm mạc ruột non; phối hợp với PTH kích thích huy động muối khoáng xương.",
        "Calcitonin (Tế bào C cận nang tuyến giáp tiết khi Ca2+ tăng cao): Ức chế hoạt động tiêu xương của hủy cốt bào, tăng đào thải Calci qua nước tiểu, hạ nồng độ Ca2+ máu tức thời.",
        "Hậu quả: PTH và Calcitriol hiệp đồng làm tăng Calci máu; Calcitonin đóng vai trò thứ yếu đối kháng làm hạ Calci máu."
    ],
    "PTH vừa làm tăng Ca2+ máu vừa làm giảm Phosphat máu (tác dụng bài phosphat niệu - phosphaturic effect), ngăn ngừa tích tụ tích số [Ca] × [P] gây lắng đọng vôi hóa lạc chỗ ở mô mềm."
))

cards.append(make_card(
    "HS15-B3-07", "Hóa sinh Ion Magie (Mg2+)", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và vai trò sinh học then chốt của Ion Magie (Mg2+)?",
    [
        "Nồng độ sinh lý bình thường: 0.75 đến 1.05 mmol/L (1.5 - 2.5 mg/dL); là cation nội bào phong phú thứ hai sau Kali.",
        "Cofactor thiết yếu cho enzyme sử dụng ATP: Mọi phản ứng enzyme sử dụng hoặc tổng hợp ATP (kinase, ATPase, tổng hợp DNA/RNA) đều bắt buộc cần cơ chất là phức hợp Mg2+-ATP.",
        "Ổn định tính hưng phấn màng thần kinh - cơ: Magie là chất chẹn tự nhiên kênh Canxi tiền synap, ức chế giải phóng Acetylcholine tại bản vận động cơ.",
        "Dấu hiệu thiếu hụt: Hạ Magie máu gây tăng kích thích thần kinh cơ (dấu hiệu Chvostek, Trousseau dương tính, co giật, run cơ tương tự hạ calci máu) và kéo dài khoảng QT gây loạn nhịp xoắn đỉnh."
    ],
    "Magie sulfat (MgSO4) tiêm tĩnh mạch là thuốc điều trị đặc hiệu hàng đầu để cắt cơn co giật trong sản giật (preeclampsia/eclampsia) và cắt cơn loạn nhịp xoắn đỉnh (Torsades de Pointes)."
))

cards.append(make_card(
    "HS15-B3-08", "Cơ chế Hạ Kali Máu Kháng trị do Hạ Magie", "BỆNH SINH PHÂN TỬ",
    "Giải thích cơ chế phân tử tại sao Hạ Magie máu lại gây Hạ Kali máu đề kháng với việc bù Kali đơn thuần?",
    [
        "Bình thường Mg2+ ức chế kênh ROMK: Nồng độ ion Magie nội bào bình thường gắn vào và ức chế kênh rò rỉ Kali ROMK ở tế bào chính ống góp thận.",
        "Hạ Magie nội bào mở toang kênh ROMK: Khi thiếu Magie, sự ức chế kênh ROMK bị giải trừ hoàn toàn → ion K+ tự do rò rỉ ồ ạt từ trong tế bào chất ống góp thoát ra lòng ống thận đào thải theo nước tiểu.",
        "Hạ hoạt tính bơm Na+-K+-ATPase: Thiếu cofactor Mg2+ làm bơm Na+-K+-ATPase giảm hoạt động, không thể giữ Kali trong tế bào.",
        "Hậu quả lâm sàng: Bù Kali đường uống hoặc tĩnh mạch bao nhiêu cũng bị thận đào thải bấy nhiêu qua kênh ROMK đang mở toang.",
        "Quy tắc vàng cấp cứu: Ở mọi bệnh nhân hạ Kali máu khó hồi phục, BẮT BUỘC phải định lượng và bù Magie đồng thời thì nồng độ Kali máu mới có thể trở về bình thường."
    ],
    "Đây là câu hỏi kinh điển trong kỳ thi BSNT: 'Hạ Kali máu trơ lì với bù Kali là do thiếu nguyên tố vi lượng nào?' → Đáp án luôn là Magie."
))

cards.append(make_card(
    "HS15-B3-09", "Hóa sinh Ion Phosphat", "ĐIỆN GIẢI HỌC",
    "Nồng độ sinh lý huyết tương và vai trò của Hệ đệm Phosphat và hormone FGF23 trong điều hòa Phosphat máu?",
    [
        "Nồng độ sinh lý bình thường: 0.8 đến 1.5 mmol/L (2.5 - 4.5 mg/dL) dưới dạng phosphat vô cơ (Pi: HPO4 2- và H2PO4-).",
        "Hệ đệm Phosphat nội bào và nước tiểu: Tỷ lệ HPO4 2- / H2PO4- có pKa = 6.8 rất gần pH sinh lý, là hệ đệm acid-base chủ lực trong dịch nội bào và là chất đệm chuẩn độ chính của nước tiểu giúp thận bài tiết acid.",
        "Cấu thành phân tử giàu năng lượng: Thành phần cấu tạo của ATP, GTP, creatine phosphat, 2,3-BPG hồng cầu và khung xương acid nucleic DNA/RNA.",
        "Hormone FGF23 (Fibroblast Growth Factor 23 do xương tiết): Tăng đào thải phosphat qua nước tiểu (ức chế chất đồng vận Na-Pi IIa/IIc ở ống thận) và ức chế 1-alpha-hydroxylase làm giảm Calcitriol, đóng vai trò chính hạ Phosphat máu."
    ],
    "Hội chứng tái nuôi dưỡng (Refeeding Syndrome) ở bệnh nhân suy dinh dưỡng nặng ăn bù nhiều carbohydrate làm insulin tăng vọt đẩy toàn bộ phosphat vào tế bào tổng hợp ATP, gây hạ phosphat máu cấp tính trụy hô hấp và ngừng tim."
))

cards.append(make_card(
    "HS15-B3-10", "Khoảng trống Anion (Anion Gap)", "XÉT NGHIỆM ĐIỆN GIẢI",
    "Công thức tính Khoảng trống Anion huyết tương (Serum Anion Gap) và ý nghĩa lâm sàng phân loại Toan chuyển hóa?",
    [
        "Nguyên lý trung hòa điện tích: Tổng số cation luôn bằng tổng số anion trong huyết tương ([Na+] + [K+] + [Cation không đo] = [Cl-] + [HCO3-] + [Anion không đo]).",
        "Công thức tính chuẩn: Anion Gap (AG) = [Na+] - ([Cl-] + [HCO3-]). (Nếu tính cả K+: AG = ([Na+] + [K+]) - ([Cl-] + [HCO3-])).",
        "Giá trị bình thường: 8 đến 12 mmol/L (đại diện cho các anion không đo được thường quy như Albumin mang điện âm, phosphat, sulfat, lactat).",
        "Ý nghĩa phân loại Toan chuyển hóa: Toan chuyển hóa tăng Anion Gap (AG > 12: do tích tụ acid lạ như Acid Lactic, Thể Ceton ĐTĐ, độc chất Methanol/Ethylene glycol, suy thận ứ sulfat) vs Toan chuyển hóa Anion Gap bình thường / tăng Clo máu (AG 8-12: do mất trực tiếp HCO3- qua tiêu chảy hoặc toan hóa ống thận RTA)."
    ],
    "Vì Albumin là anion không đo chính đóng góp vào Anion Gap (~2.5 mEq/L cho mỗi 10 g/L albumin), khi bệnh nhân hạ albumin máu nặng, Anion Gap tính toán sẽ bị thấp giả tạo; cần hiệu chỉnh: AG hiệu chỉnh = AG tính + 0.25 × (40 - Albumin g/L)."
))

# ==============================================================================
# B4: HỆ THỐNG ĐIỀU HÒA THĂNG BẰNG MUỐI NƯỚC TÍCH HỢP (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B4-01", "Trung tâm Khát Vùng Hạ đồi", "ĐIỀU HÒA NỘI MÔI",
    "Cơ chế kích hoạt Trung tâm Khát (Thirst Center) tại vùng hạ đồi của não bộ?",
    [
        "Vị trí giải phẫu: Định vị tại các cơ quan quanh não thất thiếu hàng rào máu não (cơ quan mạch máu tận cùng lá cùng OVLT và cơ quan dưới vòm SFO) thuộc vùng hạ đồi trước.",
        "Kích thích thẩm thấu (Osmotic trigger - Cực kỳ nhạy cảm): Thụ thể thẩm thấu (Osmoreceptors) bị co rút thể tích kích hoạt phản xạ khát chỉ khi áp suất thẩm thấu ECF tăng nhẹ 1 đến 2%.",
        "Kích thích huyết động / thể tích (Hemodynamic trigger): Thụ thể áp lực (Baroreceptors) tại quai động mạch chủ và xoang cảnh truyền tín hiệu kích hoạt khi thể tích máu hoặc huyết áp tụt giảm > 10%.",
        "Tác động của Angiotensin II: Angiotensin II đi qua hàng rào máu não tại SFO kích thích trực tiếp trung tâm khát, thôi thúc hành vi tìm nước uống bù thể tích."
    ],
    "Ngưỡng kích thích khát xuất hiện khi Posm vượt quá 290 - 295 mOsm/kg H2O. Người cao tuổi thường bị suy giảm thụ thể khát nên rất dễ rơi vào tình trạng mất nước ưu trương mà không hề có cảm giác khát."
))

cards.append(make_card(
    "HS15-B4-02", "Hormon ADH (Vasopressin)", "HÓA SINH NỘI TIẾT",
    "Nguồn gốc sinh tổng hợp, dự trữ và hai yếu tố sinh lý chính kích thích giải phóng Hormon chống bài niệu (ADH)?",
    [
        "Nơi sinh tổng hợp: Các thân neuron của nhân trên thị (Supraoptic nucleus) và nhân cạnh não thất (Paraventricular nucleus) thuộc vùng hạ đồi dưới dạng tiền chất prepro-vasopressin.",
        "Nơi dự trữ và bài xuất: Di chuyển dọc sợi trục thần kinh gắn protein tải Neurophysin II xuống dự trữ và giải phóng vào máu tại thùy sau tuyến yên (Neurohypophysis).",
        "Kích thích thẩm thấu (Chủ lực nhạy bén): Tăng áp suất thẩm thấu hiệu dụng huyết tương kích thích thụ thể osmoreceptors làm tăng tiết ADH theo hàm tuyến tính dốc đứng ngay khi Posm > 280 mOsm/kg.",
        "Kích thích thể tích / áp lực: Giảm thể tích máu hoặc tụt huyết áp kích thích giải phóng một lượng khổng lồ ADH qua trung gian thần kinh phế vị (dù kém nhạy hơn thẩm thấu nhưng khi tụt huyết áp nặng thì tín hiệu thể tích sẽ đè bẹp tín hiệu thẩm thấu)."
    ],
    "Cồn Ethanol trong rượu ức chế trực tiếp sự giải phóng ADH từ tuyến yên, giải thích tại sao sau khi uống nhiều rượu bia người ta đi tiểu liên tục và sáng hôm sau thức dậy với cảm giác khát khô miệng dữ dội."
))

cards.append(make_card(
    "HS15-B4-03", "Cơ chế Thụ thể V2 của ADH tại Ống góp", "HÓA SINH NỘI TIẾT",
    "Trình bày con đường truyền tín hiệu phân tử của ADH qua Thụ thể V2 kích thích chuyển vị kênh Aquaporin-2 tại ống góp thận?",
    [
        "Gắn thụ thể V2 màng đáy bên: ADH gắn thụ thể V2 (GPCR) ở màng đáy bên của tế bào chính ống góp thận.",
        "Hoạt hóa con đường Gs / cAMP / PKA: Kích hoạt protein Gs → tăng Adenylate Cyclase → tăng cAMP nội bào → hoạt hóa Protein Kinase A (PKA).",
        "Phosphoryl hóa và chuyển vị Aquaporin-2: PKA phosphoryl hóa Ser256 trên kênh nước Aquaporin-2 (AQP2) nằm trong các túi nội bào sẵn có.",
        "Hòa màng đỉnh tái hấp thu nước tự do: Các túi nội bào hòa màng đưa AQP2 cắm vào màng đỉnh (màng tiếp xúc lòng ống nước tiểu) → nước tự do thẩm thấu nhanh chóng từ lòng ống vào tế bào và qua AQP3/AQP4 màng đáy vào dịch kẽ tủy thận.",
        "Chấm dứt tác dụng: Khi nồng độ ADH giảm, AQP2 nhập bào ngược trở lại bào tương cất giữ, màng đỉnh trở lại trạng thái không thấm nước."
    ],
    "Nhờ kênh AQP2, thận có thể cô đặc nước tiểu lên tới 1.200 mOsm/kg H2O để giữ nước tối đa cho cơ thể khi bị thiếu nước."
))

cards.append(make_card(
    "HS15-B4-04", "Thụ thể V1a của ADH", "HÓA SINH NỘI TIẾT",
    "So sánh vị trí phân bố, cơ chế truyền tin và tác dụng sinh lý giữa Thụ thể V1a và V2 của Vasopressin (ADH)?",
    [
        "Thụ thể V1a: Phân bố trên cơ trơn mạch máu; truyền tin qua protein Gq → Phospholipase C (PLC) → IP3 và DAG → tăng nồng độ Ca2+ nội bào.",
        "Tác dụng sinh lý V1a: Co thắt cơ trơn mạch máu ngoại vi gây co mạch mạnh mẽ làm tăng huyết áp (do đó hormon có tên là Vasopressin).",
        "Thụ thể V2: Phân bố trên tế bào biểu mô ống góp thận; truyền tin qua protein Gs → Adenylate Cyclase → tăng cAMP → hoạt hóa PKA.",
        "Tác dụng sinh lý V2: Chuyển vị Aquaporin-2 màng đỉnh, tăng tái hấp thu nước tự do chống bài niệu (do đó có tên là Antidiuretic Hormone - ADH).",
        "Ứng dụng lâm sàng: Thuốc Terlipressin gắn ưu thế V1a dùng điều trị co mạch cầm máu trong xuất huyết tiêu hóa do vỡ giãn tĩnh mạch thực quản và hội chứng gan thận."
    ],
    "Nồng độ ADH sinh lý bình thường chỉ đủ để kích hoạt thụ thể V2 giữ nước; chỉ khi cơ thể bị sốc mất máu nặng hoặc tụt huyết áp sâu thì nồng độ ADH mới tăng vọt gấp hàng trăm lần để kích hoạt thêm thụ thể V1a gây co mạch cứu huyết áp."
))

cards.append(make_card(
    "HS15-B4-05", "Dòng thác Hệ thống RAAS", "HỆ NỘI TIẾT THẬN",
    "Các bước trong Dòng thác kích hoạt Hệ thống Renin - Angiotensin - Aldosteron (RAAS)?",
    [
        "Giải phóng Renin tại thận: Phức hợp cận cầu thận (JGA) giải phóng enzyme Renin vào máu khi: (1) Tụt huyết áp động mạch thận; (2) Giảm dòng nạp NaCl qua vết đặc macula densa; (3) Kích thích thần kinh giao cảm qua thụ thể beta-1.",
        "Tạo Angiotensin I: Renin là một protease cắt đứt liên kết peptid của protein Angiotensinogen (do gan sản xuất liên tục) tạo decapeptid Angiotensin I (bất hoạt).",
        "Chuyển thành Angiotensin II: Enzyme chuyển Angiotensin (ACE - Angiotensin-Converting Enzyme) định vị dày đặc trên bề mặt nội mô mao mạch phổi cắt 2 acid amin đầu C tạo octapeptid Angiotensin II (hoạt tính cực mạnh).",
        "Kích thích tiết Aldosteron: Angiotensin II gắn thụ thể AT1 kích thích lớp cầu vỏ thượng thận tăng sinh tổng hợp và bài tiết hormone Aldosteron."
    ],
    "Thuốc ức chế men chuyển (ACEi: Captopril, Enalapril) và thuốc chẹn thụ thể Angiotensin II (ARB: Losartan) là nền tảng điều trị tăng huyết áp, suy tim và bảo vệ thận trong đái tháo đường."
))

cards.append(make_card(
    "HS15-B4-06", "Tác dụng của Angiotensin II", "SINH LÝ HÓA SINH",
    "Bốn tác động sinh học phân tử chủ chốt của Angiotensin II thông qua Thụ thể AT1?",
    [
        "Co tiểu động mạch đi cầu thận (Efferent arteriole): Co chọn lọc tiểu động mạch đi mạnh hơn tiểu động mạch đến, làm tăng áp lực thủy tĩnh trong mao mạch cầu thận giúp duy trì mức lọc cầu thận (GFR) khi tụt huyết áp toàn thân.",
        "Co mạch ngoại vi toàn thân: Gây co thắt các tiểu động mạch toàn thân cực mạnh (mạnh gấp 40 lần Noradrenalin) làm tăng sức cản mạch hệ thống và nâng huyết áp.",
        "Kích thích vỏ thượng thận tiết Aldosteron: Tăng cường tái hấp thu Natri và nước tại ống thận.",
        "Kích thích thần kinh trung ương: Đi vào vùng dưới đồi kích thích trung tâm khát tìm nước uống và kích thích thùy sau tuyến yên tăng tiết ADH."
    ],
    "Khi bệnh nhân bị hẹp động mạch thận hai bên dùng thuốc ức chế men chuyển (ACEi), sự co tiểu động mạch đi bị triệt tiêu làm tụt áp lực lọc cầu thận đột ngột gây suy thận cấp."
))

cards.append(make_card(
    "HS15-B4-07", "Cơ chế Tác dụng của Aldosteron", "HÓA SINH NỘI TIẾT",
    "Cơ chế thụ thể nhân và tác dụng điều hòa vận chuyển ion của Aldosteron tại Ống lượn xa và Ống góp?",
    [
        "Khuếch tán qua màng gắn thụ thể Mineralocorticoid (MR): Hormon steroid Aldosteron khuếch tán vào tế bào chính gắn thụ thể MR trong bào tương, phức hợp chuyển vào nhân.",
        "Kích hoạt phiên mã protein AIP (Aldosterone-Induced Proteins): Tăng tổng hợp và mở kênh Natri biểu mô (ENaC) ở màng đỉnh, tăng tổng hợp bơm Na+-K+-ATPase ở màng đáy.",
        "Tăng tái hấp thu Natri và nước: Kênh ENaC cho dòng Na+ ồ ạt từ nước tiểu vào tế bào, sau đó được bơm Na+-K+-ATPase tống ra dịch kẽ kéo theo nước thụ động.",
        "Tăng bài tiết Kali và Proton H+: Thu nhận Na+ tạo điện thế lòng ống âm tính kéo ion K+ thoát ra qua kênh ROMK và kích thích bơm H+-ATPase bài tiết H+ ra nước tiểu.",
        "Hậu quả sinh học: Giữ muối Natri, giữ nước làm tăng thể tích tuần hoàn và huyết áp, đồng thời gây mất Kali và mất H+ (gây kiềm chuyển hóa)."
    ],
    "Thuốc lợi tiểu Spironolactone và Eplerenone đối kháng cạnh tranh thụ thể MR, ngăn chặn tác dụng của Aldosteron, do đó có tác dụng lợi tiểu thải natri nhưng lại giữ lại Kali (lợi tiểu giữ kali)."
))

cards.append(make_card(
    "HS15-B4-08", "Peptid Lợi niệu ANP và BNP", "ĐIỀU HÒA THỂ DỊCH",
    "Nguồn gốc bài tiết, cơ chế phân tử và tác dụng lợi niệu natri của ANP và BNP?",
    [
        "Nguồn gốc bài tiết: ANP (Atrial Natriuretic Peptide) tiết từ tế bào cơ tâm nhĩ; BNP (B-type Natriuretic Peptide) tiết từ tế bào cơ tâm thất khi thành tim bị căng giãn do quá tải thể tích hoặc tăng áp lực buồng tim.",
        "Cơ chế truyền tin qua cGMP: Gắn thụ thể xuyên màng NPR-A sở hữu hoạt tính enzyme Guanylate Cyclase nội tại → tăng tổng hợp cGMP nội bào → hoạt hóa Protein Kinase G (PKG).",
        "Tác dụng trên mạch máu và thận: Làm giãn tiểu động mạch đến và co nhẹ tiểu động mạch đi cầu thận → tăng áp lực lọc và tăng mức lọc cầu thận GFR; Ức chế trực tiếp kênh ENaC ở ống góp làm giảm tái hấp thu Natri.",
        "Tác dụng nội tiết đối kháng: Ức chế trực tiếp sự giải phóng Renin từ thận, ức chế tiết Aldosteron từ vỏ thượng thận và ức chế tiết ADH từ tuyến yên.",
        "Hậu quả sinh học tổng thể: Tăng đào thải Natri và nước qua nước tiểu (Natriuresis & Diuresis), làm giảm thể tích tuần hoàn và hạ huyết áp bảo vệ tim."
    ],
    "Định lượng NT-proBNP hoặc BNP huyết tương là dấu ấn sinh học cận lâm sàng tiêu chuẩn vàng để chẩn đoán xác định, phân độ suy tim và theo dõi đáp ứng điều trị suy tim."
))

cards.append(make_card(
    "HS15-B4-09", "Đối kháng giữa RAAS và ANP/BNP", "ĐIỀU HÒA TÍCH HỢP",
    "Bảng so sánh đối kháng chức năng toàn diện giữa Hệ thống RAAS và Hệ thống Peptid Lợi niệu (ANP/BNP)?",
    [
        "Tín hiệu kích hoạt — Hệ RAAS kích hoạt khi giảm thể tích và tụt áp; Hệ ANP/BNP kích hoạt khi quá tải thể tích và tăng áp lực buồng tim.",
        "Chất truyền tin thứ hai — Hệ RAAS truyền tin qua IP3/DAG/Ca2+; Hệ ANP/BNP truyền tin qua cGMP/PKG.",
        "Tác động trên mạch máu — Hệ RAAS gây co thắt tiểu động mạch mạnh mẽ; Hệ ANP/BNP gây giãn mạch toàn thân.",
        "Tác động trên ống thận — Hệ RAAS tăng tái hấp thu Na+ và nước, tăng thải K+; Hệ ANP/BNP tăng đào thải Na+ và nước ra nước tiểu.",
        "Tác động trên GFR — Hệ RAAS duy trì GFR khi tụt áp; Hệ ANP/BNP tăng GFR để tăng lọc thải nước.",
        "Biến đổi huyết áp cuối cùng — Hệ RAAS nâng huyết áp và giữ dịch; Hệ ANP/BNP hạ huyết áp và giảm tải thể tích."
    ],
    "Thuốc phối hợp ARNI (Sacubitril/Valsartan) là bước đột phá điều trị suy tim: vừa ức chế thụ thể AT1 (Valsartan) vừa ức chế enzyme Neprilysin phân hủy ANP/BNP (Sacubitril) để tăng cường tác dụng bảo vệ tim của BNP."
))

cards.append(make_card(
    "HS15-B4-10", "Đáp ứng Tích hợp khi Mất máu Cấp", "SINH LÝ BỆNH HỌC",
    "Sự phối hợp thần kinh - thể dịch của cơ thể nhằm bảo vệ huyết áp và tưới máu cơ quan khi mất máu cấp tính?",
    [
        "Phản xạ thần kinh giao cảm tức thì (Vài giây): Thụ thể áp lực xoang cảnh giảm xung ức chế → kích hoạt thần kinh giao cảm tăng nhịp tim, tăng co bóp cơ tim và co mạch ngoại vi chọn lọc tái phân bố máu về não và tim.",
        "Kích hoạt hệ thống RAAS (Vài phút): Giảm tưới máu thận kích thích JGA giải phóng Renin → nồng độ Angiotensin II tăng vọt gây co mạch và co tiểu động mạch đi duy trì GFR.",
        "Giải phóng ADH ồ ạt: Nồng độ ADH tăng gấp hàng chục lần kích hoạt đồng thời thụ thể V2 (giữ nước tối đa ở ống góp) và thụ thể V1a (co mạch ngoại vi hỗ trợ huyết áp).",
        "Kích hoạt Aldosteron (Vài giờ): Kích thích ống thận giữ muối Natri và nước bù đắp thể tích dịch ngoại bào.",
        "Kích thích trung tâm khát: Thôi thúc bệnh nhân tìm kiếm nước uống để phục hồi thể tích tuần hoàn."
    ],
    "Cơ chế tự bù trừ này giúp cơ thể chịu đựng được tình trạng mất tới 15 - 20% thể tích máu mà huyết áp động mạch vẫn chưa bị tụt ở giai đoạn đầu."
))

# ==============================================================================
# B5: RỐI LOẠN CHUYỂN HÓA NATRI MÁU (11 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B5-01", "Phân loại Hạ Natri Máu theo ASTT", "RỐI LOẠN NATRI",
    "Lưu đồ phân loại Hạ Natri máu ([Na+] < 135 mmol/L) dựa trên Áp suất thẩm thấu huyết tương (Posm)?",
    [
        "Hạ Natri máu ưu trương (Posm > 295 mOsm/kg): Do sự hiện diện của các chất tan không thấm kéo nước từ trong tế bào ra ECF làm pha loãng Na+, kinh điển nhất là Tăng đường huyết cấp tính (Đái tháo đường) hoặc truyền Mannitol.",
        "Giả hạ Natri máu / Đẳng trương (Posm 280 - 295 mOsm/kg): Do tăng lipid máu nặng (Triglyceride > 15-20 mmol/L) hoặc tăng protein máu (Đa u tủy xương Paraproteinemia) chiếm thể tích huyết tương làm sai lệch phép đo gián tiếp.",
        "Hạ Natri máu nhược trương thực sự (Posm < 280 mOsm/kg): Là thể lâm sàng phổ biến và nguy hiểm nhất, đòi hỏi phải đánh giá tiếp thể tích dịch ngoại bào (ECF volume) để tìm nguyên nhân."
    ],
    "Bước đầu tiên bắt buộc khi thấy xét nghiệm Natri máu giảm là phải kiểm tra ngay Áp suất thẩm thấu huyết tương hoặc Glucose máu để loại trừ hạ Natri máu ưu trương và giả hạ Natri máu."
))

cards.append(make_card(
    "HS15-B5-02", "Cơ chế Giả hạ Natri Máu", "CẬN LÂM SÀNG",
    "Giải thích cơ chế phân tử của hiện tượng Giả hạ Natri máu (Pseudohyponatremia) và cách phòng tránh sai số?",
    [
        "Thành phần huyết tương bình thường: Gồm 93% thể tích là nước và 7% thể tích là các đại phân tử chất rắn (protein và lipid); ion Natri chỉ hòa tan trong pha nước.",
        "Hiện tượng pha rắn tăng cao bất thường: Khi Triglyceride tăng rất cao (> 1.500 mg/dL) hoặc Protein máu tăng vọt (đa u tủy xương), pha chất rắn có thể chiếm tới 20 - 25% thể tích mẫu máu.",
        "Sai số do phương pháp đo gián tiếp (Indirect ISE): Máy xét nghiệm tự động pha loãng mẫu máu trước khi đo, tính nồng độ Na+ chia cho toàn bộ thể tích huyết tương làm kết quả bị hạ thấp giả tạo dù nồng độ Na+ thực sự trong pha nước hoàn toàn bình thường.",
        "Phương pháp khắc phục: Đo điện giải bằng điện cực chọn lọc trực tiếp (Direct ISE) trên máy đo khí máu động mạch (không pha loãng mẫu) sẽ cho kết quả nồng độ Natri máu thực sự chính xác."
    ],
    "Bệnh nhân giả hạ natri máu hoàn toàn không có triệu chứng thần kinh của hạ natri máu; truyền muối ưu trương cho những bệnh nhân này sẽ dẫn đến ngộ độc thừa muối nguy hiểm."
))

cards.append(make_card(
    "HS15-B5-03", "Hạ Natri Máu do Tăng Đường Huyết", "RỐI LOẠN NATRI",
    "Cơ chế phân tử và Công thức hiệu chỉnh nồng độ Natri máu khi bệnh nhân bị tăng đường huyết cấp tính (Công thức Katz)?",
    [
        "Cơ chế kéo nước thẩm thấu: Glucose là chất tan thẩm thấu hiệu dụng; khi đường huyết tăng cao vượt ngưỡng, glucose làm tăng áp suất thẩm thấu dịch ngoại bào ECF kéo nước từ trong tế bào ICF thoát ra ngoài làm pha loãng nồng độ Natri máu.",
        "Quy tắc chuyển dịch: Cứ mỗi khi nồng độ Glucose máu tăng thêm 5.55 mmol/L (hoặc 100 mg/dL) trên mức bình thường (5.5 mmol/L hoặc 100 mg/dL), nồng độ Natri máu sẽ giảm sinh lý khoảng 1.6 mmol/L.",
        "Công thức hiệu chỉnh Katz: [Na+] hiệu chỉnh = [Na+] đo được + 0.016 × (Glucose mg/dL - 100). Hoặc theo mmol/L: [Na+] hiệu chỉnh = [Na+] đo được + 1.6 × (Glucose mmol/L - 5.5) ÷ 5.55.",
        "Ý nghĩa xử trí: Khi hạ đường huyết về bình thường bằng truyền Insulin, nước sẽ tự động quay trở lại vào trong tế bào và nồng độ Natri máu sẽ tự động tăng trở lại mức hiệu chỉnh mà không cần truyền muối."
    ],
    "Trong toan ceton đái tháo đường (DKA), nếu Natri đo được bình thường hoặc tăng nhẹ thì nồng độ Natri hiệu chỉnh thực tế là cực kỳ cao, phản ánh tình trạng mất nước ưu trương trầm trọng."
))

cards.append(make_card(
    "HS15-B5-04", "Hạ Natri Máu Nhược trương theo Thể tích", "RỐI LOẠN NATRI",
    "Phân loại và nguyên nhân của 3 thể Hạ Natri máu nhược trương dựa trên thể tích dịch ngoại bào ECF?",
    [
        "Thể Giảm thể tích (Hypovolemic hyponatremia - Dấu hiệu véo da mất chậm, tụt áp, mạch nhanh): Mất muối nhiều hơn mất nước; Phân biệt qua Natri niệu: (1) Mất qua thận (Na niệu > 20 mmol/L do dùng lợi tiểu, suy vỏ thượng thận Addison); (2) Mất ngoài thận (Na niệu < 20 mmol/L do nôn ói, ỉa chảy cấp, bỏng, khoang thứ ba).",
        "Thể Đẳng thể tích (Euvolemic hyponatremia - Không phù, không mất nước lâm sàng): Thừa nước tự do đơn thuần; Điển hình nhất là Hội chứng tiết ADH không thích hợp (SIADH), Suy giáp nặng (Myxedema), Suy tuyến yên thứ phát, Chứng cuồng uống nước tâm thần (Psychogenic polydipsia).",
        "Thể Tăng thể tích (Hypervolemic hyponatremia - Có phù toàn thân, ứ dịch mô kẽ): Thừa cả muối và nước nhưng thừa nước nhiều hơn; Gặp trong Suy tim ứ huyết, Xơ gan mất bù cổ trướng và Hội chứng thận hư (Na niệu < 20 mmol/L do giảm thể tích tuần hoàn hiệu dụng) hoặc Suy thận cấp/mạn (Na niệu > 20 mmol/L do thận mất khả năng bài xuất)."
    ],
    "Đánh giá lâm sàng thể tích dịch ngoại bào kết hợp định lượng Natri niệu và Áp suất thẩm thấu niệu là chìa khóa vàng giúp tìm ra nguyên nhân gốc rễ của hạ natri máu."
))

cards.append(make_card(
    "HS15-B5-05", "Hội chứng SIADH", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế bệnh sinh phân tử và 4 tiêu chuẩn chẩn đoán cốt lõi của Hội chứng tiết ADH không thích hợp (SIADH)?",
    [
        "Cơ chế bệnh sinh: Tuyến yên hoặc khối u bài tiết ADH liên tục và độc lập, không chịu sự kiểm soát ức chế của áp suất thẩm thấu máu thấp → nước tự do bị tái hấp thu liên tục ở ống góp thận gây pha loãng máu.",
        "Tiêu chuẩn 1 - Hạ Natri máu nhược trương: [Na+] máu < 135 mmol/L và Posm huyết tương < 275 mOsm/kg H2O.",
        "Tiêu chuẩn 2 - Nước tiểu cô đặc không thích hợp: Áp suất thẩm thấu nước tiểu Posm niệu > 100 mOsm/kg H2O (thường > 300 mOsm/kg) chứng tỏ thận vẫn đang giữ nước dù máu đang bị pha loãng.",
        "Tiêu chuẩn 3 - Thể tích dịch bình thường trên lâm sàng (Euvolemia): Không có dấu hiệu phù ngoại vi, không có dấu hiệu mất nước tĩnh mạch cổ.",
        "Tiêu chuẩn 4 - Natri niệu cao: Nồng độ Natri niệu > 20 - 40 mmol/L (do thể tích ECF tăng nhẹ kích hoạt giải phóng ANP gây thải natri qua nước tiểu); Chức năng tuyến giáp, tuyến thượng thận và thận hoàn toàn bình thường."
    ],
    "Nguyên nhân thường gặp của SIADH gồm: Ung thư biểu mô phổi tế bào nhỏ (tiết ADH lạc chỗ), tổn thương hệ thần kinh trung ương (viêm màng não, chấn thương sọ não, đột quỵ) và các thuốc hướng thần (SSRI, Carbamazepine)."
))

cards.append(make_card(
    "HS15-B5-06", "Cơ chế Phù Não Cấp do Hạ Natri Máu", "CẤP CỨU THẦN KINH",
    "Cơ chế phân tử gây Phù não cấp tính trong Hạ Natri máu cấp (< 48 giờ) và các triệu chứng lâm sàng đe dọa tử vong?",
    [
        "Gradient thẩm thấu nội bào não: Hạ Natri máu cấp làm áp suất thẩm thấu dịch ngoại bào ECF tụt dốc nhanh chóng trong khi dịch nội bào tế bào não vẫn giữ ASTT cao.",
        "Nước tràn vào tế bào não: Chênh lệch áp suất thẩm thấu kéo nước ồ ạt từ lòng mạch và dịch kẽ vào trong tế bào thần kinh đệm (Astrocytes) qua kênh Aquaporin-4 (AQP4).",
        "Tế bào não phù nề trong hộp sọ cứng: Thể tích mô não tăng nhanh chóng bị giới hạn bởi hộp sọ xương cứng không đàn hồi → tăng áp lực nội sọ cấp tính, chèn ép mao mạch não gây thiếu máu não cục bộ.",
        "Triệu chứng lâm sàng nặng: Đau đầu dữ dội, buồn nôn, kích thích lú lẫn, co giật toàn thể, suy hô hấp, hôn mê và tử vong do tụt kẹt hạnh nhân tiểu não qua lỗ chẩm.",
        "Chỉ định cấp cứu: Hạ Natri máu cấp có triệu chứng thần kinh nặng là chỉ định tối khẩn cấp truyền tĩnh mạch dung dịch Natri Clorid ưu trương 3% để kéo nước giải áp não."
    ],
    "Não bộ trẻ em và phụ nữ tiền mãn kinh dễ bị phù não tử vong do hạ natri máu cấp hơn nam giới do hoạt tính bơm Na+-K+-ATPase não bộ bị estrogen ức chế."
))

cards.append(make_card(
    "HS15-B5-07", "Hội chứng Hủy Myelin Cầu Não (ODS)", "TAI BIẾN ĐIỀU TRỊ",
    "Cơ chế bệnh sinh phân tử của Hội chứng Hủy Myelin Thẩm thấu (ODS / Central Pontine Myelinolysis) do Bù muối quá nhanh?",
    [
        "Sự thích ứng của não trong hạ Natri mạn tính (> 48 giờ): Tế bào não tự vệ bằng cách tống xuất các chất thẩm thấu hữu cơ (Organic Osmolytes: Myo-inositol, Taurine, Glutamate, Betaine) ra ngoài để hạ ASTT nội bào ngang bằng với ECF, giúp não trở về thể tích bình thường.",
        "Bù muối ưu trương quá nhanh: Khi truyền Natri ưu trương nâng Na+ máu tăng vọt đột ngột, ECF trở nên ưu trương nhanh chóng.",
        "Tế bào não bị teo rút thẩm thấu: Tế bào não không thể tái tổng hợp và thu nhận lại các chất thẩm thấu hữu cơ kịp thời (cần vài ngày) → nước bị hút mạnh từ tế bào não ra ngoài làm tế bào não bị teo rút mất nước co cụm cấp tính.",
        "Bong tróc màng bọc Myelin cầu não: Sự co rút xé rách các nhánh bào tương của tế bào ít nhánh (Oligodendrocytes) tại cầu não → gây hủy hoại bao myelin không phục hồi.",
        "Hậu quả lâm sàng thảm khốc: Sau 2 - 6 ngày bệnh nhân xuất hiện liệt tứ chi co cứng, liệt hành tủy giả (khó nói, nuốt khó), hội chứng 'Khóa trong' (Locked-in syndrome: hoàn toàn tỉnh táo nhưng bất động toàn thân chỉ cử động được mắt) và tử vong."
    ],
    "Hội chứng hủy myelin cầu não là tai biến điều trị y khoa kinh hoàng nhất trong cấp cứu nội khoa, hoàn toàn có thể phòng ngừa nếu tuân thủ giới hạn tốc độ bù muối."
))

cards.append(make_card(
    "HS15-B5-08", "Quy tắc An toàn Nâng Natri Máu", "HỒI SỨC CẤP CỨU",
    "Quy tắc an toàn về mục tiêu và tốc độ nâng nồng độ Natri máu trong điều trị Hạ Natri máu mạn tính?",
    [
        "Giới hạn tốc độ tối đa trong 24 giờ đầu: Tuyệt đối KHÔNG nâng nồng độ Natri máu quá 8 đến 10 mmol/L trong 24 giờ đầu (ở bệnh nhân nguy cơ cao suy dinh dưỡng, nghiện rượu, xơ gan giới hạn là 6 - 8 mmol/L/24h).",
        "Giới hạn tốc độ trong 48 giờ: Không nâng quá 18 mmol/L trong 48 giờ đầu.",
        "Mục tiêu điều trị cấp cứu khi có co giật/hôn mê: Chỉ cần nâng nồng độ Natri máu lên 4 - 6 mmol/L trong 1 đến 2 giờ đầu bằng cách truyền bolus Natri Clorid 3% (100 mL truyền trong 10-15 phút, lặp lại tối đa 3 lần) là đủ để cắt cơn co giật và ngăn ngừa tụt kẹt não.",
        "Xử trí khi nồng độ Natri tăng quá nhanh (> 10 mmol/L/24h): Lập tức ngừng truyền dịch ưu trương, truyền dịch nhược trương Glucose 5% hoặc dùng thuốc Desmopressin (dDAVP) để hạ Natri máu trở lại ngưỡng an toàn."
    ],
    "Nguyên tắc cốt tử: 'Hạ Natri máu chậm thì phải nâng chậm; Hạ Natri máu nhanh cấp tính thì được phép nâng nhanh một đoạn ngắn để cứu não, nhưng sau đó phải kiểm soát tốc độ nghiêm ngặt'."
))

cards.append(make_card(
    "HS15-B5-09", "Cơ chế Tăng Natri Máu", "RỐI LOẠN NATRI",
    "Nguyên nhân và cơ chế bệnh sinh phân tử của Tăng Natri máu ([Na+] > 145 mmol/L)?",
    [
        "Bản chất luôn là tình trạng ưu trương: Tăng Natri máu luôn đồng nghĩa với tăng áp suất thẩm thấu dịch ngoại bào (Posm > 295 mOsm/kg), kéo nước ra khỏi tế bào gây teo tế bào nội bào.",
        "Cơ chế 1 - Mất nước tự do (Phổ biến nhất): Mất nước qua thận do Đái tháo nhạt (trung ương hoặc do thận), lợi niệu thẩm thấu (tăng áp lực thẩm thấu do glucose máu); Mất nước ngoài thận do vã mồ hôi nhiều, bỏng, tiêu chảy thẩm thấu.",
        "Cơ chế 2 - Không tiếp cận được nguồn nước: Tăng Natri máu hầu như CHỈ xảy ra ở những người không thể tự uống nước khi có phản xạ khát (trẻ sơ sinh, người già sa sút trí tuệ, bệnh nhân hôn mê, người bị trói/bỏ rơi).",
        "Cơ chế 3 - Nạp thừa muối Natri ưu trương: Do truyền nhầm dung dịch Natri Clorid 3% hoặc Natri Bicarbonat ưu trương, uống nước biển."
    ],
    "Một người có trung tâm khát bình thường và tự do uống nước sẽ hầu như không bao giờ bị tăng natri máu kéo dài, vì phản xạ khát sẽ thôi thúc uống nước bù đắp ngay lập tức."
))

cards.append(make_card(
    "HS15-B5-10", "Biểu hiện Thần kinh của Tăng Natri Máu", "LÂM SÀNG THẦN KINH",
    "Cơ chế phân tử của các tổn thương thần kinh trung ương và biến chứng xuất huyết não trong Tăng Natri máu cấp tính?",
    [
        "Teo rút tế bào não cấp tính: Nước bị kéo nhanh chóng từ trong tế bào thần kinh ra dịch ngoại bào ưu trương làm thể tích mô não co nhỏ lại.",
        "Căng giãn và rách các tĩnh mạch bắc cầu: Sự co rút của nhu mô não kéo căng các tĩnh mạch cầu nối (bridging veins) từ bề mặt vỏ não đổ vào xoang tĩnh mạch màng cứng → rách vỡ mạch máu gây Xuất huyết dưới màng nhện (SAH) và Tụ máu dưới màng cứng (SDH).",
        "Triệu chứng lâm sàng: Kích thích vật vã, tăng trương lực cơ, co giật, sốt cao trung ương, li bì hôn mê và tử vong.",
        "Sự thích ứng mạn tính của não: Sau 48 giờ, tế bào não tích tụ các chất thẩm thấu hữu cơ (Idiogenic Osmoles) để tự giữ nước cân bằng thể tích."
    ],
    "Do sự tích tụ các chất thẩm thấu hữu cơ bảo vệ não, việc hạ Natri máu quá nhanh bằng dịch nhược trương sẽ làm nước ồ ạt tràn vào tế bào não gây Phù não cấp tính thứ phát."
))

cards.append(make_card(
    "HS15-B5-11", "Quy tắc Điều trị Tăng Natri Máu", "HỒI SỨC CẤP CỨU",
    "Nguyên tắc tính toán lượng nước thiếu hụt (Free Water Deficit) và tốc độ hạ Natri máu an toàn trong điều trị Tăng Natri máu?",
    [
        "Công thức tính lượng nước thiếu hụt: Lượng nước thiếu (Lít) = TBW × (([Na+] bệnh nhân ÷ 140) - 1). Trong đó TBW = Trọng lượng cơ thể (kg) × hệ số (nam 0.6, nữ 0.5, người già 0.5/0.45).",
        "Tốc độ hạ Natri máu tối đa cho phép: Tuyệt đối KHÔNG hạ nồng độ Natri máu quá 10 đến 12 mmol/L trong 24 giờ (tốc độ an toàn khoảng 0.5 mmol/L mỗi giờ).",
        "Lựa chọn dung dịch bù nước: Ưu tiên đường uống hoặc sonde dạ dày bằng nước lọc tinh khiết; nếu truyền tĩnh mạch dùng dung dịch nhược trương Glucose 5% hoặc Natri Clorid 0.45%.",
        "Nguy cơ khi hạ Natri quá nhanh: Gây Phù não cấp, co giật và tử vong do tế bào não đang chứa nhiều chất thẩm thấu hữu cơ hút nước vào quá mức."
    ],
    "Nguyên tắc: Bù một nửa lượng nước thiếu hụt trong 24 giờ đầu, nửa còn lại bù rải đều trong 24 - 48 giờ tiếp theo để não bộ có đủ thời gian đào thải các chất thẩm thấu hữu cơ thích nghi."
))

# ==============================================================================
# B6: RỐI LOẠN CHUYỂN HÓA KALI MÁU (11 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B6-01", "Cơ chế Hạ Kali Máu", "RỐI LOẠN KALI",
    "Phân biệt hai nhóm cơ chế bệnh sinh chính dẫn đến Hạ Kali máu ([K+] < 3.5 mmol/L)?",
    [
        "Nhóm 1 - Dịch chuyển Kali từ ngoại bào vào trong tế bào (Không làm thay đổi tổng lượng K+ cơ thể): Kiềm chuyển hóa (trao đổi H+/K+ qua màng); Tăng nồng độ Insulin (kích hoạt bơm Na+-K+-ATPase); Kích thích thần kinh giao cảm beta-2 (thuốc Salbutamol, Terbutaline); Hạ thân nhiệt; Liệt chu kỳ hạ kali máu gia đình.",
        "Nhóm 2 - Mất Kali thực sự ra ngoài cơ thể (Làm suy kiệt tổng lượng K+ cơ thể):",
        "   - Mất qua đường tiêu hóa: Tiêu chảy mất dịch ruột giàu K+; Nôn mửa kéo dài gây kiềm chuyển hóa làm thận tăng thải K+.",
        "   - Mất qua đường thận: Dùng thuốc lợi tiểu quai (Furosemide) hoặc Thiazide; Hội chứng Cường Aldosteron; Hội chứng Cushing; Hội chứng Bartter, Gitelman.",
        "Hạ Magie máu phối hợp: Luôn đi kèm làm trầm trọng thêm tình trạng mất Kali qua thận."
    ],
    "Đo nồng độ Kali trong nước tiểu 24 giờ (hoặc tỷ số K/Creatinin niệu) giúp phân biệt nhanh: K niệu < 20 mmol/ngày chứng tỏ mất ngoài thận hoặc do dịch chuyển nội bào; K niệu > 20 mmol/ngày khẳng định mất qua thận."
))

cards.append(make_card(
    "HS15-B6-02", "Cơ chế Dịch chuyển Kali Nội bào", "BỆNH SINH PHÂN TỬ",
    "Giải thích cơ chế phân tử của hiện tượng Kiềm chuyển hóa và Insulin làm dịch chuyển ion Kali vào trong tế bào?",
    [
        "Cơ chế của Kiềm chuyển hóa (Alkalosis): Khi pH máu tăng, nồng độ H+ ngoại bào giảm; tế bào đệm bằng cách đẩy proton H+ từ trong tế bào ra ngoài để trung hòa, đồng thời bắt buộc phải kéo ion K+ từ ngoại bào vào trong tế bào để duy trì cân bằng điện thế màng → gây hạ Kali máu.",
        "Quy tắc chuyển dịch pH: Cứ mỗi khi pH máu tăng thêm 0.1 đơn vị, nồng độ Kali huyết tương giảm khoảng 0.3 đến 0.5 mmol/L.",
        "Cơ chế của Insulin: Insulin gắn thụ thể RTK kích hoạt con đường IRS-1/PI3K/Akt kích thích trực tiếp bơm Na+-K+-ATPase màng tế bào bơm 2 K+ vào nội bào.",
        "Ứng dụng lâm sàng: Truyền Insulin kết hợp Glucose là biện pháp cấp cứu kinh điển để hạ nhanh Kali máu trong các cơn tăng Kali máu nguy kịch."
    ],
    "Ngược lại trong toan chuyển hóa máu (Acidosis), proton H+ tràn vào tế bào đẩy ion K+ ra dịch ngoại bào, gây tăng nồng độ Kali máu giả tạo dù tổng lượng K+ cơ thể có thể đang bị thiếu hụt."
))

cards.append(make_card(
    "HS15-B6-03", "Mất Kali do Nôn ói vs Tiêu chảy", "LÂM SÀNG TIÊU HÓA",
    "So sánh cơ chế phân tử gây Hạ Kali máu do Nôn ói kéo dài và do Tiêu chảy cấp?",
    [
        "Hạ Kali do Tiêu chảy: Dịch phân và dịch đại tràng chứa nồng độ K+ rất cao (30 - 50 mmol/L) cùng dịch kiềm Bicarbonat → tiêu chảy gây MẤT TRỰC TIẾP Kali qua đường tiêu hóa kèm Toan chuyển hóa bình thường Anion Gap.",
        "Hạ Kali do Nôn ói (Cơ chế gián tiếp qua thận): Dịch dạ dày chứa nồng độ K+ rất thấp (~10 mmol/L), nôn ói mất HCl gây Kiềm chuyển hóa và giảm thể tích máu.",
        "Kích hoạt Aldosteron thận thải Kali: Giảm thể tích máu kích hoạt hệ RAAS tiết nhiều Aldosteron; lượng lớn HCO3- lọc qua cầu thận không được tái hấp thu hết làm lòng ống lượn xa tích điện âm mạnh → kéo ion K+ và H+ bài tiết ồ ạt ra nước tiểu.",
        "Hậu quả: Bệnh nhân nôn ói bị mất phần lớn Kali qua NƯỚC TIỂU chứ không phải qua dịch nôn, kèm theo Kiềm chuyển hóa hạ clo máu."
    ],
    "Bệnh nhân hẹp môn vị nôn nhiều ngày có biểu hiện kinh điển: Kiềm chuyển hóa, hạ Clo máu, hạ Kali máu nhưng nước tiểu lại có tính acid nghịch ngôn (Paradoxical aciduria do ống thận ưu tiên giữ Na+ và thải H+)."
))

cards.append(make_card(
    "HS15-B6-04", "Biến đổi Điện tâm đồ (ECG) trong Hạ Kali", "ĐIỆN TÂM ĐỒ",
    "Bốn biến đổi Điện tâm đồ (ECG) kinh điển theo trình tự mức độ nặng dần của Hạ Kali máu?",
    [
        "Sóng T dẹt hoặc đảo ngược: Quá trình tái cực cơ thất bị kéo dài làm sóng T giảm biên độ, trở nên dẹt hoặc đảo ngược âm tính.",
        "Đoạn ST chênh xuống: Đoạn ST chênh xuống dạng nằm ngang hoặc dốc xuống (dễ nhầm với thiếu máu cơ tim).",
        "Xuất hiện sóng U nổi rõ: Sóng U biên độ cao (> 1 mm hoặc > 50% biên độ sóng T) xuất hiện ngay sau sóng T, nhìn rõ nhất ở các chuyển đạo trước tim V2 đến V4.",
        "Kéo dài khoảng QU và Loạn nhịp thất: Sóng T hòa lẫn với sóng U tạo khoảng QU kéo dài (giả QT kéo dài) → kích phát các rối loạn nhịp thất nguy hiểm: Ngoại tâm thu thất đa ổ, Nhịp nhanh thất, Xoắn đỉnh (Torsades de Pointes) và Rung thất."
    ],
    "Sóng U là dấu hiệu nhận diện đặc trưng số 1 của hạ kali máu trên điện tâm đồ; khi K+ < 2.5 mmol/L, sóng U có thể cao vượt cả sóng T đi trước."
))

cards.append(make_card(
    "HS15-B6-05", "Nguyên tắc Bù Kali An toàn", "HỒI SỨC CẤP CỨU",
    "Các nguyên tắc sống còn và giới hạn tốc độ truyền tĩnh mạch ion Kali (KCl) trong điều trị Hạ Kali máu?",
    [
        "Ưu tiên đường uống: Hạ kali máu nhẹ đến vừa (K+ 3.0 - 3.4 mmol/L) không có biến đổi ECG bắt buộc ưu tiên bù bằng đường uống (muối KCl) vì an toàn tuyệt đối, tránh nguy cơ tăng kali máu quá mức đột ngột.",
        "Chỉ định truyền tĩnh mạch: Khi hạ kali máu nặng (K+ < 2.5 mmol/L), có rối loạn nhịp tim hoặc biến đổi ECG cấp tính, hoặc bệnh nhân hôn mê, liệt ruột tắc ruột không uống được.",
        "Pha loãng bắt buộc trong dung dịch NaCl 0.9%: Tuyệt đối KHÔNG pha Kali vào dung dịch Glucose vì đường kích thích tiết insulin làm K+ chạy vào tế bào làm K+ máu tụt sâu hơn.",
        "Giới hạn nồng độ và tốc độ truyền ngoại vi: Nồng độ tối đa qua đường truyền tĩnh mạch ngoại vi là 40 mmol/L (để tránh gây viêm xơ tắc tĩnh mạch và bỏng rát dữ dội); Tốc độ truyền tối đa an toàn qua tĩnh mạch ngoại vi là 10 đến 20 mmol/giờ và bắt buộc phải theo dõi liên tục trên Monitor điện tim.",
        "Tuyệt đối CẤM tiêm tĩnh mạch trực tiếp (Bolus) KCl: Tiêm tĩnh mạch trực tiếp KCl sẽ gây ngừng tim tức thì trong tâm trương (phương thức hành quyết tử tù)."
    ],
    "Ước tính mức độ thiếu hụt: Cứ mỗi khi nồng độ Kali huyết tương giảm 1.0 mmol/L (từ 4.0 xuống 3.0), tổng lượng Kali thiếu hụt trong toàn bộ cơ thể là khoảng 200 đến 400 mmol."
))

cards.append(make_card(
    "HS15-B6-06", "Cơ chế Tăng Kali Máu", "RỐI LOẠN KALI",
    "Phân biệt hai nhóm nguyên nhân chính gây Tăng Kali máu ([K+] > 5.0 mmol/L, cấp cứu khi > 6.5 mmol/L)?",
    [
        "Nhóm 1 - Dịch chuyển Kali từ trong tế bào ra ngoài ECF: Toan chuyển hóa (đặc biệt toan chuyển hóa vô cơ do proton H+ vào tế bào đẩy K+ ra); Thiếu hụt Insulin nặng (toan ceton ĐTĐ); Tiêu cơ vân cấp (Rhabdomyolysis phóng thích lượng K+ cơ bắp khổng lồ); Tan máu nội mạch cấp tính; Bỏng diện rộng hoặc hội chứng ly giải u (Tumor Lysis Syndrome); Liệt cơ do dùng thuốc Succinylcholine.",
        "Nhóm 2 - Giảm đào thải Kali qua thận (Phổ biến nhất):",
        "   - Suy thận cấp hoặc Suy thận mạn giai đoạn cuối (GFR < 15 mL/phút).",
        "   - Bệnh suy vỏ thượng thận Addison (thiếu hụt hoàn toàn hormone Aldosteron).",
        "   - Tác dụng phụ của thuốc ức chế hệ RAAS: Thuốc ức chế men chuyển (ACEi), thuốc chẹn thụ thể (ARB), thuốc chẹn beta giao cảm, thuốc lợi tiểu giữ kali (Spironolactone, Amiloride), thuốc kháng viêm NSAIDs.",
        "Giả tăng Kali máu (Pseudohyperkalemia): Tan máu mẫu thử do garo quá chặt, đặt ống nghiệm lâu, hoặc tăng tiểu cầu (> 1.000 G/L), tăng bạch cầu (> 50 G/L) phóng thích K+ khi máu đông in vitro."
    ],
    "Trước khi cấp cứu tăng Kali máu ở bệnh nhân không có biến đổi ECG và chức năng thận bình thường, luôn phải kiểm tra xem mẫu máu có bị vỡ hồng cầu (tan máu ống nghiệm) hay không."
))

cards.append(make_card(
    "HS15-B6-07", "Động học Biến đổi ECG trong Tăng Kali", "ĐIỆN TÂM ĐỒ",
    "Trình bày 5 giai đoạn biến đổi Điện tâm đồ (ECG) theo từng nấc nồng độ Kali máu tăng dần?",
    [
        "Giai đoạn 1 (K+ 5.5 - 6.5 mmol/L): Sóng T cao nhọn đối xứng, đáy hẹp hình lều (nhìn rõ nhất ở chuyển đạo trước tim V2-V4).",
        "Giai đoạn 2 (K+ 6.5 - 7.0 mmol/L): Sóng P dẹt dần, biên độ giảm; Khoảng PR kéo dài (Block nhĩ thất độ I).",
        "Giai đoạn 3 (K+ 7.0 - 8.0 mmol/L): Sóng P biến mất hoàn toàn (liệt nhĩ); Phức bộ QRS giãn rộng dần (> 0.12s), chậm dẫn truyền trong thất.",
        "Giai đoạn 4 (K+ > 8.0 mmol/L): Phức bộ QRS giãn cực rộng hòa lẫn với sóng T tạo thành Sóng hình sin liên tục (Sine wave pattern).",
        "Giai đoạn 5 (Tử vong): Rung thất (Ventricular Fibrillation), nhịp tự thất chậm hoặc ngừng tim vô tâm thu (Asystole) trong thì tâm trương."
    ],
    "Biến đổi ECG trong tăng Kali máu không phải lúc nào cũng tuân theo nấc nồng độ lý thuyết; một bệnh nhân K+ 6.2 mmol/L tăng cấp tính có thể đột ngột chuyển sang sóng hình sin và ngừng tim mà không báo trước."
))

cards.append(make_card(
    "HS15-B6-08", "Bộ ba Cấp cứu Tăng Kali Máu", "HỒI SỨC CẤP CỨU",
    "Trình bày 3 bước chiến lược trong Phác đồ cấp cứu Tăng Kali máu nặng có biến đổi điện tâm đồ?",
    [
        "Mục tiêu 1 - Ổn định màng tế bào cơ tim tức thì (1 - 3 phút): Tiêm tĩnh mạch chậm 10 mL Calci Clorid 10% (hoặc Calci Gluconat 10%) trong 2-3 phút dưới theo dõi Monitor. Calci làm tăng ngưỡng điện thế hoạt động, phục hồi chênh lệch điện thế màng giúp cơ tim không bị kích phát loạn nhịp (hoàn toàn KHÔNG làm hạ nồng độ Kali máu).",
        "Mục tiêu 2 - Đẩy Kali từ ngoại bào vào trong tế bào tạm thời (15 - 30 phút):",
        "   - Tiêm tĩnh mạch nhanh 10 UI Insulin tác dụng nhanh (Actrapid) pha trong 50 mL Glucose 20 - 50% (kích hoạt bơm Na+-K+-ATPase kéo K+ vào nội bào, tác dụng duy trì 4-6 giờ).",
        "   - Khí dung thuốc đồng vận beta-2 Albuterol (Salbutamol) liều cao 10 - 20 mg trong 15 phút.",
        "   - Tiêm Natri Bicarbonat 8.4% (50 - 100 mL) nếu bệnh nhân có toan chuyển hóa máu đi kèm.",
        "Mục tiêu 3 - Đào thải Kali ra khỏi cơ thể dứt điểm (Vài giờ):",
        "   - Thuốc lợi tiểu quai Furosemide 40 - 80 mg IV nếu chức năng thận còn bài tiết nước tiểu.",
        "   - Nhựa trao đổi cation gắn Kali qua đường tiêu hóa (Lokelma, Patiromer, Resonium/Kayexalate).",
        "   - Lọc máu cấp cứu (Hemodialysis): Biện pháp dứt điểm nhanh nhất và hiệu quả nhất khi suy thận vô niệu hoặc đe dọa ngừng tim."
    ],
    "Quy tắc vàng: Calci tiêm trước để 'mua thời gian' bảo vệ quả tim; Insulin + Glucose làm hạ K+ tạm thời; Lọc máu hoặc lợi tiểu là biện pháp thải K+ ra khỏi cơ thể dứt điểm."
))

cards.append(make_card(
    "HS15-B6-09", "Cơ chế Bảo vệ Tim của Calci", "HỒI SỨC CẤP CỨU",
    "Giải thích cơ chế điện sinh lý tại sao Calci tiêm tĩnh mạch lại bảo vệ được quả tim khỏi ngừng tim trong tăng Kali máu?",
    [
        "Hậu quả của tăng Kali máu trên màng cơ tim: Nồng độ K+ ngoại bào tăng làm điện thế màng nghỉ (Em) bớt âm hơn (dịch chuyển từ -90 mV lên -70 mV), tiến sát lại ngưỡng điện thế phát sinh điện thế hoạt động (Vthreshold ~ -65 mV) → làm bất hoạt các kênh Na+ cổng điện thế khiến cơ tim mất tính hưng phấn và chậm dẫn truyền.",
        "Cơ chế đối kháng điện thế của Calci: Nồng độ ion Ca2+ ngoại bào tăng làm dịch chuyển ngưỡng điện thế kích hoạt (Vthreshold) lên mức bớt âm hơn (từ -65 mV lên -55 mV) nhờ hiệu ứng che chắn điện tích bề mặt màng.",
        "Phục hồi khoảng cách an toàn: Khoảng cách giữa điện thế nghỉ và ngưỡng kích hoạt được tái lập trở lại mức bình thường → phục hồi hoạt tính của kênh Na+, phục hồi dẫn truyền cơ thất, làm hẹp phức bộ QRS và bình thường hóa sóng T trên ECG trong vòng vài phút.",
        "Thời gian tác dụng: Tác dụng bảo vệ màng xuất hiện cực nhanh (1 - 3 phút) nhưng chỉ kéo dài ngắn (30 - 60 phút), do đó phải lặp lại liều nếu ECG tái phát xấu đi trong khi chờ các biện pháp hạ Kali phát huy tác dụng."
    ],
    "Calci tiêm tĩnh mạch không làm thay đổi dù chỉ một phần triệu nồng độ Kali trong máu; mục đích duy nhất của Calci là 'lá chắn điện học' bảo vệ cơ tim không bị rung thất."
))

cards.append(make_card(
    "HS15-B6-10", "Dược lý Nhựa Trao đổi Cation", "DƯỢC LÝ ĐIỆN GIẢI",
    "Cơ chế tác dụng và phân loại các thuốc Nhựa trao đổi ion đào thải Kali qua đường tiêu hóa?",
    [
        "Cơ chế chung: Các polymer trao đổi ion không hấp thu vào máu, di chuyển dọc đường ruột (chủ yếu ở đại tràng) nhả cation mang theo (Na+ hoặc Ca2+) để bắt giữ ion K+ tự do trong phân và đào thải ra ngoài theo phân.",
        "Sodium Polystyrene Sulfonate (SPS / Kayexalate): Trao đổi Na+ lấy K+, khởi phát tác dụng chậm (vài giờ đến 24 giờ); Nguy cơ biến chứng nặng là Hoại tử ruột (Intestinal necrosis) đặc biệt khi phối hợp với Sorbitol.",
        "Patiromer (Veltassa): Polymer hạt hình cầu không hấp thu trao đổi Ca2+ lấy K+ ở đại tràng, dung nạp tốt hơn, không gây hoại tử ruột, dùng kiểm soát tăng kali máu mạn tính ở bệnh nhân suy tim/suy thận dùng thuốc ức chế RAAS.",
        "Sodium Zirconium Cyclosilicate (SZC / Lokelma): Hợp chất tinh thể vô cơ bẫy ion chọn lọc cao vi mô cho K+ (bắt chước bộ lọc chọn lọc kênh K+), tác dụng nhanh trong vòng 1 giờ, dùng được cả trong cấp cứu và duy trì."
    ],
    "Sự ra đời của các thuốc bẫy Kali thế hệ mới (Lokelma, Patiromer) cho phép bệnh nhân suy tim và suy thận tiếp tục sử dụng các thuốc tối ưu kéo dài sống còn (như Spironolactone, ACEi, ARB) mà không bị ngừng thuốc do tăng Kali máu."
))

cards.append(make_card(
    "HS15-B6-11", "Tăng Kali Máu do Tan máu Ống nghiệm", "CẬN LÂM SÀNG",
    "Các nguyên nhân gây Giả tăng Kali máu (Pseudohyperkalemia) trong thực hành xét nghiệm và cách phát hiện?",
    [
        "Tan máu trong ống nghiệm (In vitro Hemolysis - Phổ biến nhất): Hồng cầu chứa nồng độ K+ cao gấp 30 lần huyết tương (~140 mmol/L); kỹ thuật lấy máu thô bạo, garo quá chặt lâu, hút áp lực mạnh, lắc mạnh ống nghiệm làm vỡ màng hồng cầu giải phóng K+ vào huyết thanh.",
        "Đặt ống nghiệm chậm ly tâm: Máu toàn phần để ở nhiệt độ phòng hoặc tủ lạnh quá 2 - 3 giờ làm cạn kiệt glucose và ức chế bơm Na+-K+-ATPase hồng cầu, K+ rò rỉ ra ngoài huyết thanh.",
        "Tăng sinh dòng tế bào máu quá mức: Tăng số lượng tiểu cầu cực nặng (> 1.000 G/L trong tăng tiểu cầu tiên phát) giải phóng K+ khi máu đông tạo cục máu; Tăng bạch cầu cực nặng (> 50 - 100 G/L trong bệnh bạch cầu cấp) làm bạch cầu vỡ giải phóng K+.",
        "Dấu hiệu nhận biết: Huyết thanh có màu hồng hoặc đỏ của Hemoglobin; Bệnh nhân hoàn toàn tỉnh táo khỏe mạnh, Điện tâm đồ ECG hoàn toàn bình thường không có dấu hiệu tăng K+.",
        "Cách xử lý: Lấy lại mẫu máu mới nhẹ nhàng, chống đông bằng Heparin và gửi ly tâm đo ngay lập tức."
    ],
    "Không bao giờ vội vàng tiêm Calci hay hạ Kali cấp cứu cho một bệnh nhân có ECG bình thường hoàn hảo trước khi kiểm tra lại mẫu máu chống đông không tan máu."
))

# ==============================================================================
# B7: CÁC THỂ MẤT NƯỚC VÀ THỪA DỊCH TRÊN LÂM SÀNG (9 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-B7-01", "Mất nước Đẳng trương", "CÁC THỂ MẤT NƯỚC",
    "Đặc điểm hóa sinh, biến đổi các ngăn dịch và nguyên nhân của Mất nước đẳng trương (Isotonic Dehydration)?",
    [
        "Đặc điểm sinh hóa: Nước và điện giải bị mất ra ngoài theo tỷ lệ tương đương nhau; Áp suất thẩm thấu huyết tương bình thường (280 - 295 mOsm/kg); Nồng độ Natri máu bình thường (135 - 145 mmol/L).",
        "Biến đổi các ngăn dịch: Do ASTT ngoại bào không đổi nên KHÔNG CÓ sự dịch chuyển nước qua màng tế bào → Thể tích dịch nội bào ICF hoàn toàn không đổi; Toàn bộ lượng dịch mất được trừ trực tiếp từ Dịch ngoại bào ECF (thể tích ECF giảm sút).",
        "Nguyên nhân thường gặp: Mất máu cấp tính (chấn thương, xuất huyết tiêu hóa); Nôn ói, ỉa chảy cấp giai đoạn đầu; Bỏng nông diện rộng; Mất dịch khoang thứ ba (viêm phúc mạc, tắc ruột).",
        "Dấu hiệu lâm sàng: Dấu hiệu mất nước ngoại bào điển hình: Khát vừa, da khô véo da mất chậm, mắt trũng, huyết áp tụt, mạch nhanh, thiểu niệu.",
        "Dung dịch bù lựa chọn: Dung dịch tinh thể đẳng trương: Natri Clorid 0.9% hoặc Ringer Lactate."
    ],
    "Trong mất nước đẳng trương, thể tích nội bào ICF được bảo toàn nguyên vẹn, do đó bệnh nhân hoàn toàn không có triệu chứng thần kinh co giật hay hôn mê của phù não/teo não."
))

cards.append(make_card(
    "HS15-B7-02", "Mất nước Ưu trương", "CÁC THỂ MẤT NƯỚC",
    "Đặc điểm hóa sinh, biến đổi các ngăn dịch và triệu chứng đặc trưng của Mất nước ưu trương (Hypertonic Dehydration)?",
    [
        "Đặc điểm sinh hóa: Lượng nước mất nhiều hơn lượng muối điện giải; Áp suất thẩm thấu huyết tương tăng cao (> 295 mOsm/kg); Nồng độ Natri máu tăng cao (> 145 mmol/L).",
        "Biến đổi các ngăn dịch: ECF ưu trương hút nước từ trong tế bào ICF ra ngoài → CẢ HAI NGĂN DỊCH ĐỀU BỊ GIẢM THỂ TÍCH, trong đó ngăn nội bào ICF bị teo rút mất nước trầm trọng.",
        "Nguyên nhân: Mất nước vô cảm kéo dài khi sốt cao, say nắng, thông khí nhân tạo khô; Đái tháo nhạt (thiếu ADH thải nước tiểu nhược trương); Lợi niệu thẩm thấu do tăng áp lực thẩm thấu đái tháo đường; Không được cung cấp nước uống.",
        "Triệu chứng lâm sàng nổi bật: Khát nước dữ dội không dập tắt được; Sốt cao trung ương; Niêm mạc miệng lưỡi khô ráp; Triệu chứng thần kinh ưu thế do teo tế bào não: kích thích vật vã, tăng phản xạ, mê sảng, co giật hôn mê.",
        "Dung dịch bù lựa chọn: Dung dịch nhược trương: Nước lọc qua đường tiêu hóa, hoặc truyền tĩnh mạch Glucose 5%, Natri Clorid 0.45%."
    ],
    "Mất nước ưu trương nguy hiểm nhất là tổn thương nhu mô não do teo rút tế bào và nguy cơ xuất huyết màng não do đứt tĩnh mạch bắc cầu."
))

cards.append(make_card(
    "HS15-B7-03", "Mất nước Nhược trương", "CÁC THỂ MẤT NƯỚC",
    "Đặc điểm hóa sinh, biến đổi các ngăn dịch và nguy cơ sốc trong Mất nước nhược trương (Hypotonic Dehydration)?",
    [
        "Đặc điểm sinh hóa: Lượng muối điện giải bị mất nhiều hơn lượng nước; Áp suất thẩm thấu huyết tương giảm (< 280 mOsm/kg); Nồng độ Natri máu giảm (< 135 mmol/L).",
        "Biến đổi các ngăn dịch: Dịch ngoại bào ECF nhược trương đẩy nước chạy vào trong tế bào ICF theo gradient thẩm thấu → Thể tích ECF bị giảm sút cực kỳ nghiêm trọng (giảm do mất ra ngoài + giảm do nước chạy vào tế bào), trong khi thể tích ICF lại bị ứ nước trương phồng.",
        "Nguyên nhân: Mất muối qua thận do bệnh suy thượng thận Addison (thiếu aldosteron); Lạm dụng thuốc lợi tiểu quai/thiazide; Mất dịch tiêu hóa nhưng chỉ bù bằng nước lọc tinh khiết hoặc truyền Glucose 5% kéo dài.",
        "Nguy cơ Sốc tụt huyết áp sớm: Vì ECF bị rút cạn thể tích kép, bệnh nhân nhanh chóng rơi vào sốc giảm thể tích tuần hoàn sớm và nặng nề dù lượng nước mất thực tế không quá lớn.",
        "Dấu hiệu lâm sàng: Không có cảm giác khát (do ECF nhược trương không kích thích trung tâm khát), da lạnh tái ẩm, véo da mất rất chậm, hạ huyết áp tư thế, trụy mạch.",
        "Dung dịch bù lựa chọn: Bắt buộc bù lại muối Natri bằng dung dịch đẳng trương NaCl 0.9% hoặc dung dịch ưu trương NaCl 3% nếu có co giật."
    ],
    "Sai lầm kinh điển của người nhà bệnh nhân tiêu chảy là chỉ cho trẻ uống nước lọc hay nước đường không có muối, vô tình biến mất nước đẳng trương thành mất nước nhược trương gây phù não và trụy mạch."
))

cards.append(make_card(
    "HS15-B7-04", "Bảng Đối chiếu 3 Thể Mất nước", "TỔNG HỢP LÂM SÀNG",
    "Bảng đối chiếu tổng hợp 3 thể mất nước lâm sàng dựa trên ASTT, Natri máu, thể tích ECF/ICF và dung dịch xử trí?",
    [
        "Mất nước đẳng trương: [Posm]: 280 - 295 mOsm/kg; [Na+ máu]: 135 - 145 mmol/L; [Thể tích ECF]: Giảm; [Thể tích ICF]: Không đổi; [Triệu chứng chính]: Dấu mất nước ECF, tụt áp; [Dịch bù]: NaCl 0.9%, Ringer Lactate.",
        "Mất nước ưu trương: [Posm]: > 295 mOsm/kg; [Na+ máu]: > 145 mmol/L; [Thể tích ECF]: Giảm; [Thể tích ICF]: Giảm (teo tế bào não); [Triệu chứng chính]: Khát dữ dội, sốt, co giật hôn mê; [Dịch bù]: Uống nước lọc, Glucose 5%, NaCl 0.45%.",
        "Mất nước nhược trương: [Posm]: < 280 mOsm/kg; [Na+ máu]: < 135 mmol/L; [Thể tích ECF]: Giảm nặng; [Thể tích ICF]: Tăng (phù tế bào não); [Triệu chứng chính]: Sốc trụy mạch sớm, không khát, phù não; [Dịch bù]: NaCl 0.9%, NaCl 3%."
    ],
    "Nắm chắc bảng đối chiếu 3 thể mất nước là yêu cầu bắt buộc đối với mọi bác sĩ Nhi khoa và Hồi sức cấp cứu để chỉ định đúng loại dịch truyền cứu sống người bệnh."
))

cards.append(make_card(
    "HS15-B7-05", "Ngộ độc Nước (Water Intoxication)", "RỐI LOẠN THỂ DỊCH",
    "Cơ chế bệnh sinh phân tử và biến chứng của tình trạng Thừa nước nhược trương (Ngộ độc nước)?",
    [
        "Nguyên nhân: Uống quá nhiều nước tự do trong thời gian ngắn vượt quá khả năng bài xuất nước tối đa của thận (~1 Lít/giờ), điển hình ở người mắc chứng cuồng uống nước tâm thần (Psychogenic polydipsia), uống nước thi đấu, hoặc truyền quá nhiều dịch Glucose 5% ở người suy thận.",
        "Cơ chế phân tử: Toàn bộ lượng nước thừa phân bố vào dịch ngoại bào làm nồng độ Natri máu tụt dốc cấp tính, ECF trở nên nhược trương sâu sắc.",
        "Dịch chuyển nước vào tế bào não: Nước ồ ạt thẩm thấu qua kênh Aquaporin-4 vào các tế bào thần kinh đệm não bộ.",
        "Biến chứng Phù não cấp tính: Tăng áp lực nội sọ cấp gây đau đầu dữ dội, co giật liên tục, hôn mê, thoát vị não qua lỗ chẩm và tử vong.",
        "Xử trí khẩn cấp: Hạn chế nước tuyệt đối, tiêm tĩnh mạch bolus Natri Clorid ưu trương 3% để kéo nước giải áp khẩn cấp cho nhu mô não."
    ],
    "Vận động viên chạy Marathon uống quá nhiều nước tinh khiết dọc đường chạy mà không bổ sung điện giải là đối tượng thường gặp của hội chứng hạ natri máu do gắng sức (EAH) gây tử vong do ngộ độc nước."
))

cards.append(make_card(
    "HS15-B7-06", "Đánh giá Mất nước ở Trẻ em", "NHI KHOA LÂM SÀNG",
    "Thang điểm lâm sàng đánh giá mức độ mất nước ở trẻ em theo Tổ chức Y tế Thế giới (WHO)?",
    [
        "Mất nước độ I (Nhẹ, mất < 5% trọng lượng cơ thể): Trẻ tỉnh táo, mắt bình thường, uống nước bình thường, nếp véo da mất nhanh dưới 1 giây.",
        "Mất nước độ II (Có mất nước, mất 5 - 10% trọng lượng): Trẻ kích thích, vật vã, mắt trũng sâu, uống nước háo hức, nếp véo da mất chậm (dưới 2 giây).",
        "Mất nước độ III (Mất nước nặng, mất > 10% trọng lượng): Trẻ li bì, lơ mơ hoặc hôn mê; Mắt rất trũng, khóc không có nước mắt; Không thể uống được hoặc uống rất kém; Nếp véo da mất rất chậm (> 2 giây); Mạch nhanh nhỏ, chi lạnh ẩm (dấu hiệu sốc).",
        "Xử trí theo phác đồ WHO: Phác đồ A (tại nhà bằng Oresol); Phác đồ B (bù Oresol tại cơ sở y tế); Phác đồ C (truyền tĩnh mạch cấp cứu ngay lập tức bằng Ringer Lactate 100 mL/kg)."
    ],
    "Dấu hiệu nếp véo da (Skin pinch) phải được thực hiện ở vùng da bụng dọc theo trục cơ thể, véo nhẹ bằng ngón cái và ngón trỏ rồi buông tay quan sát tốc độ phẳng lại của da."
))

cards.append(make_card(
    "HS15-B7-07", "Thành phần và Cơ chế Gói Oresol", "ĐIỀU TRỊ THAY THẾ",
    "Thành phần Dung dịch Bù nước Điện giải Oresol thẩm thấu thấp (Reduced Osmolarity ORS) theo khuyến cáo WHO/UNICEF?",
    [
        "Công thức thẩm thấu thấp cải tiến (Tổng ASTT = 245 mOsm/L): Natri 75 mmol/L, Glucose 75 mmol/L, Clorid 65 mmol/L, Kali 20 mmol/L, Citrate 10 mmol/L.",
        "Tỷ lệ vàng 1:1 giữa Natri và Glucose: Khớp hoàn hảo với tỷ lệ stoichiometry đồng vận chuyển của protein mang SGLT1 tại bờ bàn chải ruột non.",
        "Cơ chế kéo nước thụ động: Sự hấp thu tích cực Na+ và Glucose qua SGLT1 tạo môi trường ưu trương cục bộ ở khoảng gian bào ruột, kéo theo hàng ngàn phân tử nước thẩm thấu vào máu bất chấp độc tố tả đang kích thích bài tiết Cl-.",
        "Ưu điểm của công thức mới 245 mOsm/L so với công thức cũ 311 mOsm/L: Giảm 33% nhu cầu phải truyền dịch tĩnh mạch, giảm 20% lượng phân tiêu chảy và giảm 30% tần suất nôn trớ ở trẻ nhỏ."
    ],
    "Pha Oresol bắt buộc phải pha đúng chính xác thể tích nước quy định trên gói (thường là 1 gói pha đúng 200 mL hoặc 1 lít nước đun sôi để nguội); pha quá đặc sẽ biến dung dịch thành ưu trương gây tiêu chảy mất nước nặng hơn và teo não."
))

cards.append(make_card(
    "HS15-B7-08", "Cơ chế Khát trong Mất máu Cấp", "SINH LÝ HỌC LÂM SÀNG",
    "Tại sao một bệnh nhân bị mất máu cấp tính do chấn thương nặng lại kêu 'khát nước' dữ dội dù nồng độ Natri máu không hề tăng?",
    [
        "Tín hiệu thể tích lấn át tín hiệu thẩm thấu: Mất máu cấp làm thể tích dịch ngoại bào ECF và áp lực động mạch tụt sâu, kích hoạt mạnh mẽ thụ thể áp lực Baroreceptors tại quai động mạch chủ và xoang cảnh.",
        "Kích hoạt hệ thống RAAS: Giảm tưới máu thận kích thích giải phóng một lượng lớn Renin, tạo ra nồng độ Angiotensin II huyết tương tăng vọt.",
        "Kích thích trực tiếp trung tâm khát: Angiotensin II vượt qua cơ quan dưới vòm (SFO) kích thích trực tiếp neuron trung tâm khát vùng hạ đồi, tạo cảm giác khát mãnh liệt thôi thúc tìm nước uống.",
        "Phối hợp tiết ADH: Tín hiệu áp lực tụt sâu gửi qua dây thần kinh phế vị (dây X) lên hạ đồi kích thích giải phóng lượng tối đa ADH."
    ],
    "Triệu chứng 'khát nước' ở bệnh nhân chấn thương đa chấn thương hoặc sản phụ sau sinh là một trong những dấu hiệu lâm sàng sớm cảnh báo sốc mất máu đang diễn tiến trước khi huyết áp tụt."
))

cards.append(make_card(
    "HS15-B7-09", "Chỉ số BUN / Creatinin", "CẬN LÂM SÀNG THẬN",
    "Ý nghĩa của Tỷ số BUN / Creatinin huyết thanh (hoặc Ure / Creatinin) trong phân biệt Suy thận trước thận vs Suy thận tại thận?",
    [
        "Sinh lý tái hấp thu Ure tại thận: Bình thường khoảng 40 - 50% Ure được tái hấp thu thụ động ở ống lượn gần song hành cùng với sự tái hấp thu muối và nước; trong khi Creatinin hoàn toàn không được tái hấp thu.",
        "Suy thận trước thận do giảm thể tích / mất nước: Lưu lượng máu đến thận giảm kích thích ống thận tăng tối đa sự tái hấp thu Na+ và nước → Ure bị kéo theo tái hấp thu ồ ạt trở lại máu, trong khi Creatinin vẫn bị đào thải bình thường.",
        "Tỷ số BUN / Creatinin tăng vọt (> 20:1 theo mg/dL hoặc Ure/Creatinin > 40-50 theo mmol/L): Khẳng định suy thận chức năng do nguyên nhân trước thận (mất nước, sốc giảm thể tích, suy tim).",
        "Suy thận tại thận (Hoại tử ống thận cấp - ATN): Ống thận bị hoại tử mất khả năng tái hấp thu Ure → Tỷ số BUN / Creatinin bình thường (< 10 - 15:1 theo mg/dL)."
    ],
    "Tỷ số BUN/Creatinin > 20:1 kết hợp với Phân suất bài xuất Natri FeNa < 1% là cặp dấu ấn cận lâm sàng vàng khẳng định suy thận cấp trước thận đáp ứng hồi phục hoàn toàn khi bù đủ dịch."
))

# ==============================================================================
# B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS15-ALGO-01", "Thuật toán Tiếp cận Hạ Natri Máu", "HẠ NATRI MÁU",
    "Lưu đồ thuật toán 3 bước tiếp cận chẩn đoán phân tầng nguyên nhân Hạ Natri máu ([Na+] < 135 mmol/L)?",
    [
        "Bước 1 - Đo Áp suất thẩm thấu huyết tương (Posm):",
        "   - Nhánh [Posm > 295 mOsm/kg]: Hạ Natri máu ƯU TRƯƠNG (Tăng đường huyết cấp, truyền Mannitol) → Tính Natri hiệu chỉnh.",
        "   - Nhánh [Posm 280 - 295 mOsm/kg]: GIẢ HẠ NATRI MÁU (Tăng Triglyceride máu nặng, đa u tủy xương Paraproteinemia) → Đo bằng điện cực trực tiếp.",
        "   - Nhánh [Posm < 280 mOsm/kg]: HẠ NATRI MÁU NHƯỢC TRƯƠNG THỰC SỰ → Chuyển tiếp sang Bước 2.",
        "Bước 2 - Đánh giá Thể tích Dịch Ngoại bào (ECF Volume) trên lâm sàng:",
        "   - Nhánh [Giảm thể tích ECF - Dấu véo da (+), tụt áp]: Mất muối > Mất nước → Chuyển tiếp sang Bước 3.",
        "   - Nhánh [Đẳng thể tích ECF - Không phù, không mất nước]: Thừa nước tự do → SIADH, Suy giáp, Chứng cuồng uống nước.",
        "   - Nhánh [Tăng thể tích ECF - Có phù, cổ trướng]: Suy tim ứ huyết, Xơ gan mất bù, Hội chứng thận hư, Suy thận mạn.",
        "Bước 3 - Đo nồng độ Natri nước tiểu (UNa) ở thể Giảm thể tích:",
        "   - UNa > 20 mmol/L: Mất muối qua THẬN (Dùng thuốc lợi tiểu, suy vỏ thượng thận Addison, bệnh thận mất muối).",
        "   - UNa < 20 mmol/L: Mất muối NGOÀI THẬN (Nôn mửa, tiêu chảy cấp, bỏng rộng, thoát dịch khoang thứ ba)."
    ],
    "Thuật toán 3 bước (ASTT → Thể tích ECF → Natri niệu) là phác đồ chuẩn mực quốc tế của chuyên khoa Thận - Hồi sức giúp tìm ra chính xác căn nguyên của hạ natri máu trong mọi tình huống lâm sàng.",
    algo=True
))

cards.append(make_card(
    "HS15-ALGO-02", "Phác đồ Cấp cứu Cơn Tăng Kali Máu Nặng", "CẤP CỨU HỒI SỨC",
    "Lưu đồ thuật toán phác đồ cấp cứu Cơn Tăng Kali máu nặng (K+ > 6.5 mmol/L hoặc có biến đổi ECG) theo 3 bước chiến lược?",
    [
        "Bước 1 - ỔN ĐỊNH MÀNG TẾ BÀO CƠ TIM TỨC THÌ (Thời gian đáp ứng 1 - 3 phút):",
        "   - Tiêm tĩnh mạch chậm Calci Clorid 10% (5 - 10 mL) hoặc Calci Gluconat 10% (10 - 20 mL) trong 2 - 3 phút dưới theo dõi Monitor điện tim liên tục.",
        "   - Nếu ECG chưa cải thiện sau 5 phút: Lặp lại liều Calci thứ 2 (chú ý thận trọng ở bệnh nhân đang dùng Digoxin).",
        "Bước 2 - DỊCH CHUYỂN KALI VÀO TRONG NỘI BÀO TẠM THỜI (Thời gian đáp ứng 15 - 30 phút):",
        "   - Tiêm tĩnh mạch 10 UI Insulin nhanh (Actrapid) pha trong 50 mL Glucose 20% hoặc 30% (truyền trong 15-30 phút, theo dõi đường huyết mao mạch).",
        "   - Kết hợp Khí dung thuốc đồng vận beta-2 Albuterol (Salbutamol) liều cao 10 - 20 mg trong 15 phút.",
        "   - Tiêm Natri Bicarbonat 8.4% (50 mL IV) nếu có toan chuyển hóa máu phối hợp.",
        "Bước 3 - ĐÀO THẢI KALI RA KHỎI CƠ THỂ DỨT ĐIỂM (Bắt đầu ngay):",
        "   - Lợi tiểu quai Furosemide 40 - 80 mg IV nếu bệnh nhân còn nước tiểu.",
        "   - Uống nhựa gắn Kali trao đổi ion: Sodium Zirconium Cyclosilicate (Lokelma 10g) hoặc Patiromer hoặc Kayexalate.",
        "   - LỌC MÁU CẤP CỨU (Hemodialysis): Chỉ định ngay lập tức nếu suy thận vô niệu, toan máu nặng hoặc tăng Kali máu kháng trị đe dọa ngừng tim."
    ],
    "Thứ tự ưu tiên sống còn: Calci là thuốc đầu tiên phải rút tiêm ngay lập tức để cứu quả tim không bị rung thất; sau đó mới cho Insulin + Glucose và gọi đội lọc máu hỗ trợ.",
    algo=True
))

cards.append(make_card(
    "HS15-ALGO-03", "Phân biệt 3 Thể Mất Nước", "CHẨN ĐOÁN LÂM SÀNG",
    "Lưu đồ thuật toán phân biệt 3 thể Mất nước lâm sàng và Lựa chọn dịch truyền phục hồi tối ưu?",
    [
        "Thể 1 - MẤT NƯỚC ĐẲNG TRƯƠNG (Isotonic Dehydration):",
        "   - Tiêu chí sinh hóa: ASTT huyết tương bình thường (280 - 295 mOsm/kg), [Na+] máu 135 - 145 mmol/L.",
        "   - Động học dịch: ECF giảm, ICF bình thường (không dịch chuyển nước qua màng).",
        "   - Dịch truyền phục hồi: Dung dịch tinh thể đẳng trương: Natri Clorid 0.9% hoặc Ringer Lactate.",
        "Thể 2 - MẤT NƯỚC ƯU TRƯƠNG (Hypertonic Dehydration):",
        "   - Tiêu chí sinh hóa: ASTT huyết tương tăng (> 295 mOsm/kg), [Na+] máu tăng (> 145 mmol/L).",
        "   - Động học dịch: Cả ECF và ICF đều giảm thể tích; nước bị rút từ tế bào ra ngoài gây teo tế bào não (khát dữ dội, sốt, co giật).",
        "   - Dịch truyền phục hồi: Uống nước lọc, hoặc truyền tĩnh mạch dịch nhược trương: Glucose 5%, Natri Clorid 0.45% (hạ Na+ từ từ ≤ 10 mmol/L/24h).",
        "Thể 3 - MẤT NƯỚC NHƯỢC TRƯƠNG (Hypotonic Dehydration):",
        "   - Tiêu chí sinh hóa: ASTT huyết tương giảm (< 280 mOsm/kg), [Na+] máu giảm (< 135 mmol/L).",
        "   - Động học dịch: ECF giảm rất nặng, ICF tăng thể tích (nước chạy vào tế bào gây phù não, sốc tụt áp sớm).",
        "   - Dịch truyền phục hồi: Dung dịch đẳng trương Natri Clorid 0.9% để nâng thể tích tuần hoàn; nếu có co giật do phù não truyền bolus Natri Clorid ưu trương 3%."
    ],
    "Nhớ nhanh: Đẳng trương bù đẳng trương; Ưu trương bù nhược trương (nước tự do); Nhược trương bù muối (đẳng trương hoặc ưu trương).",
    algo=True
))

cards.append(make_card(
    "HS15-ALGO-04", "Ứng dụng Khoảng trống Thẩm thấu trong Ngộ độc", "CẬN LÂM SÀNG ĐỘC CHẤT",
    "Lưu đồ thuật toán ứng dụng Khoảng trống Thẩm thấu (Osmolar Gap) trong chẩn đoán Toan chuyển hóa tăng Anion Gap do Ngộ độc cồn độc?",
    [
        "Bước 1 - Xác định Toan chuyển hóa tăng Anion Gap: Khí máu động mạch thấy pH < 7.35, HCO3- giảm, Anion Gap = [Na+] - ([Cl-] + [HCO3-]) > 12 mmol/L.",
        "Bước 2 - Đo và Tính toán Khoảng trống Thẩm thấu (Osmolar Gap):",
        "   - Đo áp suất thẩm thấu trực tiếp bằng máy đo độ hạ băng điểm (Posm đo).",
        "   - Tính áp suất thẩm thấu lý thuyết: Posm tính = 2 × [Na+] + Glucose + Ure.",
        "   - Khoảng trống thẩm thấu = Posm đo - Posm tính toán.",
        "Bước 3 - Phân tầng chẩn đoán theo Khoảng trống Thẩm thấu:",
        "   - Nhánh [Khoảng trống Thẩm thấu BÌNH THƯỜNG (< 10 mOsm/kg)]: Toan hóa máu do các acid nội sinh thông thường: Toan Ceton ĐTĐ (DKA), Toan Lactic (sốc nhiễm khuẩn, suy tim), Suy thận urê huyết cao.",
        "   - Nhánh [Khoảng trống Thẩm thấu TĂNG CAO (> 10 mOsm/kg)]: Khẳng định ngộ độc phân tử ngoại lai tan trong nước:",
        "     * METHANOL (Cồn công nghiệp): Gây toan máu nặng, mù mắt do tổn thương thần kinh thị giác bởi acid formic.",
        "     * ETHYLENE GLYCOL (Chất chống đông xe hơi): Gây toan máu nặng, suy thận cấp do lắng đọng tinh thể Calci Oxalate hình phong bì trong nước tiểu.",
        "     * ISOPROPANOL (Cồn xoa bóp): Tăng khoảng trống thẩm thấu và ceton niệu nhưng KHÔNG gây toan máu (chuyển hóa thành aceton)."
    ],
    "Xử trí ngộ độc Methanol hoặc Ethylene glycol cần chỉ định ngay thuốc ức chế enzyme Alcohol Dehydrogenase là Fomepizole (hoặc Ethanol uống) và lọc máu cấp cứu để dọn sạch độc chất trước khi chúng chuyển hóa thành acid độc.",
    algo=True
))

cards.append(make_card(
    "HS15-ALGO-05", "Xử trí An toàn Hạ Natri Máu Nặng", "HỒI SỨC CẤP CỨU",
    "Lưu đồ thuật toán xử trí an toàn Hạ Natri máu nặng có triệu chứng thần kinh cấp tính và phòng ngừa Hội chứng Hủy Myelin Cầu Não?",
    [
        "Bước 2 - Điều trị cắt cơn cấp cứu bằng Natri Clorid 3%:",
        "   - Tiêm tĩnh mạch bolus 100 mL Natri Clorid 3% trong 10 đến 15 phút.",
        "   - Nếu triệu chứng chưa cải thiện: Có thể lặp lại liều bolus 100 mL lần 2 và lần 3 (mỗi lần cách nhau 10 phút, tối đa 3 liều).",
        "   - Mục tiêu cấp cứu: Nâng nồng độ Natri máu lên khoảng 4 đến 6 mmol/L là đủ để giảm thể tích phù não và cắt đứt cơn co giật.",
        "Bước 3 - Kiểm soát tốc độ nâng Natri trong 24 giờ để phòng ngừa HỦY MYELIN CẦU NÃO (ODS):",
        "   - Tốc độ nâng Natri tối đa: KHÔNG vượt quá 8 mmol/L trong 24 giờ đầu (đối với bệnh nhân xơ gan, suy dinh dưỡng, nghiện rượu: không quá 6 mmol/L/24h).",
        "   - Xét nghiệm điện giải máu mỗi 2 - 4 giờ một lần để điều chỉnh tốc độ truyền dịch.",
        "   - Nếu phát hiện Natri máu tăng quá nhanh (> 8 - 10 mmol/L): Ngừng ngay dung dịch ưu trương, truyền dịch nhược trương Glucose 5% hoặc dùng thuốc Desmopressin (dDAVP 1 - 2 µg tiêm tĩnh mạch) để đưa Natri trở lại ngưỡng an toàn."
    ],
    "Ghi nhớ quy tắc nằm lòng: 'Mục tiêu cấp cứu hạ natri máu chỉ là nâng 4-6 mmol/L để cứu tính mạng, tuyệt đối không được tham lam đưa Natri về mức bình thường ngay trong ngày đầu tiên'.",
    algo=True
))
manifest_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-15_Trao_doi_muoi_nuoc")
target_json = manifest_dir / "HS-15_Trao_doi_muoi_nuoc.cards.v2.json"
target_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Tong so the moi: {len(cards)} the")
print(f"Da ghi thanh cong vao {target_json}")
