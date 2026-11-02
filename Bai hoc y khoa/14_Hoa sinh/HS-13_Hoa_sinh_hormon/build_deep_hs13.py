# -*- coding: utf-8 -*-
"""build_deep_hs13.py - Generate 85 exhaustive master flashcards for HS-13 (Cơ chế thụ thể, truyền tín hiệu tế bào và hóa sinh hormon)"""
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
  <span style="background-color: #ffd43b; color: #212529; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Gợi ý</span> Nhớ lại cơ chế hóa sinh phân tử và ý nghĩa lâm sàng BSNT.
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
        "extra": extra or "Nguồn: Giáo trình Hóa Sinh Y Học - ĐHYHN (GS. Tạ Thành Văn, Tr. 267-302), Lehninger Principles of Biochemistry 8th ed (Chap 12), Harper's Illustrated Biochemistry 32nd ed (Chap 41-44).",
        "tags": ["hoasinh", "HS13", section]
    }

cards = []

# ==============================================================================
# SECTION B1: ĐẠI CƯƠNG HỆ NỘI TIẾT & PHÂN LOẠI HORMON (11 thẻ: HS13-B1-01 -> HS13-B1-11)
# ==============================================================================

cards.append(make_card(
    "HS13-B1-01",
    "Định nghĩa Hormon và Đặc trưng Nồng độ Sinh lý",
    "ĐẠI CƯƠNG HỆ NỘI TIẾT",
    "Định nghĩa chuẩn hóa học của hormon và đặc trưng nồng độ hoạt động sinh lý trong tuần hoàn máu?",
    [
        "<b>Khái niệm phân tử —</b> Hormon là những hợp chất hữu cơ có hoạt tính sinh học cực cao, do các tế bào nội tiết chuyên biệt bài tiết trực tiếp vào tuần hoàn máu.",
        "<b>Đặc trưng nồng độ —</b> Hoạt động ở nồng độ cực thấp trong huyết tương, dao động từ 10^-12 mol/L (picomolar - pM) đến 10^-9 mol/L (nanomolar - nM).",
        "<b>Đặc hiệu thụ thể —</b> Tác động chọn lọc lên các tế bào/mô đích thông qua sự liên kết đặc hiệu với thụ thể tương ứng để điều biến chuyển hóa và duy trì nội môi.",
        "<b>Bản chất tín hiệu —</b> Đóng vai trò là chất truyền tin hóa học (chemical messenger) kết nối và phối hợp chức năng đa bào của cơ thể."
    ],
    "Từ gốc Hy Lạp 'hormao' nghĩa là kích thích, thúc đẩy. Mặc dù nồng độ trong máu cực loãng, thụ thể đích có ái lực rất cao (hằng số phân ly Kd từ 10^-9 đến 10^-12 M) giúp nhận diện và khuếch đại tín hiệu chính xác tuyệt đối."
))

cards.append(make_card(
    "HS13-B1-02",
    "5 Phương thức Truyền tin Gian bào (Intercellular Signaling)",
    "HÌNH THỨC TRUYỀN TIN",
    "Đặc điểm phân biệt 5 phương thức truyền tín hiệu hóa học giữa các tế bào trong cơ thể đa bào?",
    [
        "<b>Nội tiết (Endocrine) —</b> Hormon được bài tiết vào dòng máu tuần hoàn để tác động lên tế bào đích ở khoảng cách rất xa (ví dụ Insulin từ đảo tụy đến gan, cơ, mỡ; TSH từ tuyến yên đến tuyến giáp).",
        "<b>Cận tiết (Paracrine) —</b> Phân tử tín hiệu khuếch tán qua dịch gian bào tác động lên các tế bào lân cận trong cùng một mô (ví dụ Somatostatin ức chế tiết Insulin và Glucagon lân cận; Histamin từ tế bào ECL kích thích tế bào thành dạ dày).",
        "<b>Tự tiết (Autocrine) —</b> Phân tử tín hiệu gắn trực tiếp lên thụ thể của chính tế bào bài tiết nó (ví dụ IL-2 tự kích thích dòng lympho T tăng sinh; tế bào ung thư tự kích thích nhân đôi).",
        "<b>Tiếp xúc trực tiếp (Juxtacrine) —</b> Đòi hỏi tiếp xúc màng - đối - màng qua protein liên kết (Notch-Delta) hoặc qua cầu nối liên bào Gap Junction cho phép Ca2+, cAMP di chuyển trực tiếp giữa các tế bào cơ tim.",
        "<b>Thần kinh - nội tiết (Neuroendocrine) —</b> Tế bào thần kinh giải phóng hormon thần kinh từ cúc tận cùng sợi trục vào máu đến cơ quan đích xa (ví dụ TRH, GnRH đổ vào hệ mạch cửa hạ đồi; ADH, Oxytocin phóng thích từ thùy sau tuyến yên)."
    ],
    "Sự phân loại dựa trên khoảng cách và lộ trình phát tán tín hiệu. Đây là nền tảng giúp hiểu rõ cơ chế khu trú hay toàn thân của các bệnh lý nội tiết và ung bướu."
))

cards.append(make_card(
    "HS13-B1-03",
    "4 Dạng Nhịp Sinh học Bài tiết Hormon",
    "ĐỘNG HỌC BÀI TIẾT",
    "Đặc điểm và đại diện của 4 dạng nhịp sinh học chỉ huy sự bài tiết hormon trong cơ thể?",
    [
        "<b>Nhịp ngày - đêm (Circadian rhythm, chu kỳ 24h) —</b> Do nhân trên chéo (SCN) vùng hạ đồi chỉ huy; Cortisol đạt đỉnh 6:00 - 8:00 sáng, chạm đáy nửa đêm 23:00 - 0:00 (đòi hỏi lấy máu đúng giờ chuẩn để chẩn đoán Cushing/Addison).",
        "<b>Nhịp dạng xung (Pulsatile / Circhoral, chu kỳ 1 - 2h) —</b> Phóng thích ngắt quãng từng đợt; GH tăng vọt vào giấc ngủ sâu (NREM); GnRH bắt buộc phải bài tiết dạng xung để duy trì đáp ứng thụ thể tuyến yên (tiết liên tục sẽ trơ hóa thụ thể).",
        "<b>Nhịp tháng (Infradian rhythm, chu kỳ ~28 ngày) —</b> Biến thiên chu kỳ của FSH, LH, Estradiol và Progesteron điều hòa chu kỳ kinh nguyệt và phóng noãn ở phụ nữ.",
        "<b>Nhịp theo mùa (Seasonal rhythm) —</b> T3 và T4 có xu hướng tăng nhẹ vào mùa lạnh nhằm tăng cường chuyển hóa sinh nhiệt thích nghi môi trường."
    ],
    "Hiểu rõ nhịp sinh học có ý nghĩa quyết định khi lấy mẫu bệnh phẩm nội tiết (ví dụ định lượng Cortisol máu sáng 8h vs đêm 20h) và ứng dụng điều trị (ví dụ dùng thuốc GnRH agonist dạng giải phóng kéo dài để ức chế trục sinh dục trong ung thư tiền liệt tuyến)."
))

cards.append(make_card(
    "HS13-B1-04",
    "4 Nhóm Hormon theo Cấu trúc Hóa học",
    "PHÂN LOẠI HÓA HỌC",
    "Cơ sở phân chia và đại diện của 4 nhóm hormon theo bản chất hóa học trong cơ thể người?",
    [
        "<b>Nhóm 1 (Peptid / Protein) —</b> Chuỗi oligopeptid đến polypeptide lớn hoặc glycoprotein: TRH (3 aa), ADH/Oxytocin (9 aa), Insulin (51 aa), Glucagon (29 aa), GH (191 aa), PTH, TSH, LH, FSH.",
        "<b>Nhóm 2 (Dẫn xuất Acid amin) —</b> Phân tử lượng nhỏ từ L-Tyrosin (Catecholamin: Dopamin, Noradrenalin, Adrenalin; Hormon giáp: T3, T4) hoặc từ L-Tryptophan (Melatonin, Serotonin).",
        "<b>Nhóm 3 (Hormon Steroid) —</b> Mang nhân đa vòng Cyclopentanoperhydrophenanthren (nhân Gonan) bắt nguồn từ Cholesterol: Cortisol, Aldosteron, Testosteron, Estradiol, Progesteron, Calcitriol.",
        "<b>Nhóm 4 (Dẫn xuất Acid béo - Eicosanoid) —</b> Phân tử lipid 20 carbon từ quá trình oxy hóa Acid Arachidonic: Prostaglandin (PGE2, PGI2), Thromboxan (TXA2), Leukotriene (LTB4, LTC4)."
    ],
    "Cấu trúc hóa học quyết định trực tiếp tính tan, phương thức vận chuyển trong tuần hoàn, thời gian bán hủy và vị trí thụ thể tiếp nhận tương ứng."
))

cards.append(make_card(
    "HS13-B1-05",
    "Đối chiếu Hormon Nhóm I (Lipophilic) vs Hormon Nhóm II (Hydrophilic)",
    "PHÂN LOẠI CHỨC NĂNG",
    "Bảng đối chiếu toàn diện về tính tan, vận chuyển và cơ chế giữa Hormon Nhóm I và Nhóm II?",
    [
        "<b>Bản chất hóa học —</b> Nhóm I gồm Steroid, T3/T4, Calcitriol, Acid Retinoic; Nhóm II gồm Polypeptid, Protein, Glycoprotein, Catecholamin.",
        "<b>Tính chất hòa tan —</b> Nhóm I kỵ nước (tan trong lipid); Nhóm II ưa nước (tan trong nước).",
        "<b>Protein vận chuyển huyết tương —</b> Nhóm I bắt buộc phải gắn protein tải (TBG, CBG, SHBG, Albumin), dạng tự do dưới 2%; Nhóm II lưu thông tự do không cần protein mang (trừ GH, IGF-1).",
        "<b>Thời gian bán hủy (t1/2) —</b> Nhóm I dài từ vài chục phút đến nhiều ngày (T4 khoảng 7 ngày); Nhóm II ngắn từ vài phút (Insulin 3 - 5 phút, Catecholamin 1 - 2 phút).",
        "<b>Vị trí thụ thể đích —</b> Nhóm I nằm trong nội bào (bào tương hoặc nhân); Nhóm II nằm ở mặt ngoài màng sinh chất."
    ],
    "Quy luật tính tan là chìa khóa then chốt: chất tan trong lipid dễ dàng vượt qua lớp kép phospholipid màng tế bào, trong khi chất tan trong nước bị chặn lại ở mặt ngoài và buộc phải dùng chất truyền tin thứ hai."
))

cards.append(make_card(
    "HS13-B1-06",
    "Cơ chế Tác động Phân tử: Nhóm I vs Nhóm II",
    "CƠ CHẾ PHÂN TỬ",
    "Sự khác biệt về cơ chế phát động tín hiệu, phân tử truyền tin và tốc độ đáp ứng giữa Nhóm I và Nhóm II?",
    [
        "<b>Phân tử truyền tin —</b> Nhóm I không dùng second messenger (phức hợp Hormon - Thụ thể tác động trực tiếp); Nhóm II dùng chất truyền tin thứ hai (cAMP, cGMP, IP3, DAG, Ca2+) hoặc chuỗi kinase.",
        "<b>Cơ chế tác động phân tử —</b> Nhóm I gắn trình tự HRE trên DNA để điều hòa sao chép mRNA và dịch mã protein mới; Nhóm II làm biến đổi trạng thái phosphoryl hóa của các enzym chuyển hóa sẵn có.",
        "<b>Tốc độ khởi phát —</b> Nhóm I chậm (sau vài giờ đến vài ngày do cần thời gian biểu hiện gen); Nhóm II cực nhanh tức thời (vài giây đến vài phút).",
        "<b>Độ kéo dài hiệu ứng —</b> Nhóm I duy trì bền bỉ nhiều ngày đến nhiều tuần; Nhóm II thoái lui nhanh chóng khi hormon bị enzym giáng hóa."
    ],
    "Đây là lý do cấp cứu hạ đường huyết hoặc sốc phản vệ dùng Adrenalin (Nhóm II - tác dụng tức thì trong 1 phút), trong khi điều trị kháng viêm mạn dùng Corticoid (Nhóm I - tác dụng sau vài giờ nhưng kéo dài)."
))

cards.append(make_card(
    "HS13-B1-07",
    "Đặc điểm Sinh học của Hormon Peptid và Protein",
    "HÓA SINH PEPTID",
    "Quá trình sinh tổng hợp, dự trữ và bài xuất của các hormon thuộc nhóm Peptid/Protein?",
    [
        "<b>Dòng chảy sinh tổng hợp —</b> Tổng hợp tại lưới nội chất hạt dưới dạng Preprohormon → Cắt peptid tín hiệu tại lòng lưới nội chất tạo Prohormon → Đóng gói tại bộ máy Golgi thành bóng chế tiết.",
        "<b>Cắt giải phóng hoạt tính —</b> Các enzym protease trong bóng chế tiết thủy phân Prohormon tạo hormon trưởng thành (ví dụ Preproinsulin → Proinsulin → Insulin + C-peptide).",
        "<b>Dự trữ nội bào —</b> Được tích trữ trong các bọc hạt chế tiết (secretory granules) với số lượng lớn sẵn sàng chờ tín hiệu phóng thích.",
        "<b>Cơ chế xuất bào —</b> Xuất bào (exocytosis) phụ thuộc ion Ca2+ khi có tín hiệu kích hoạt khử cực màng tế bào.",
        "<b>Lưu thông máu —</b> Hòa tan tự do trong huyết tương, thời gian bán hủy ngắn (vài phút), thoái hóa chủ yếu nhờ protease tại gan và thận."
    ],
    "Nhờ được dự trữ sẵn dưới dạng hạt chế tiết, tuyến nội tiết peptid có thể giải phóng ồ ạt hormon trong vài giây khi cơ thể phát tín hiệu kích thích khẩn cấp."
))

cards.append(make_card(
    "HS13-B1-08",
    "Ngoại lệ Thú vị: Hormon Tuyến Giáp (T3/T4)",
    "HÓA HỌC TUYẾN GIÁP",
    "Vì sao hormon tuyến giáp (T3, T4) là dẫn xuất acid amin nhưng lại có cơ chế sinh học thuộc Nhóm I?",
    [
        "<b>Nguồn gốc hóa học —</b> Là dẫn xuất của acid amin L-Tyrosin được gắn thêm các nguyên tử Iod (I) thơm hóa.",
        "<b>Đặc tính lý hóa —</b> Cấu trúc kỵ nước cao độ do mang 2 vòng benzen và các nguyên tử Iod cồng kềnh, rất kém tan trong nước.",
        "<b>Vận chuyển trong máu —</b> Bắt buộc phải gắn chặt với protein vận chuyển huyết tương (TBG vận chuyển 75%, Transthyretin 15%, Albumin 10%); dạng tự do FT4 chỉ chiếm 0,03%, FT3 chiếm 0,3%.",
        "<b>Thời gian bán hủy cực dài —</b> T4 có t1/2 khoảng 7 ngày, T3 khoảng 1 ngày (dài nhất trong toàn bộ hệ thống hormon người).",
        "<b>Vị trí thụ thể và cơ chế —</b> Gắn trực tiếp vào thụ thể nhân (Thyroid Hormone Receptor - TR), liên kết DNA và điều hòa phiên mã gen như một hormon Nhóm I điển hình."
    ],
    "T3 và T4 là trường hợp đặc biệt duy nhất: bản chất là dẫn xuất acid amin nhưng quy luật vận chuyển, thụ thể và cơ chế hoạt động hoàn toàn tuân theo hormon Nhóm I."
))

cards.append(make_card(
    "HS13-B1-09",
    "Đặc điểm Sinh tổng hợp và Giải phóng Hormon Steroid",
    "HÓA SINH STEROID",
    "Quy luật sinh tổng hợp, dự trữ và bài tiết của hormon steroid có điểm gì khác biệt cốt lõi so với hormon peptid?",
    [
        "<b>Nguồn gốc phân tử —</b> Bắt nguồn từ Cholesterol tự do hoặc este hóa (nhận từ LDL huyết tương hoặc tổng hợp từ Acetyl-CoA).",
        "<b>Không có kho dự trữ hạt —</b> Hormon steroid kỵ nước, hòa tan tự do qua màng lipid nên tế bào KHÔNG THỂ dự trữ trong các túi bóng xuất bào như hormon peptid.",
        "<b>Cơ chế đáp ứng tiết —</b> Khi bị kích thích (ví dụ ACTH), tế bào lập tức tăng tốc tổng hợp mới qua phản ứng mở đầu cắt chuỗi nhánh Cholesterol (nhờ StAR và CYP11A1) và khuếch tán thẳng ra máu.",
        "<b>Vận chuyển trong tuần hoàn —</b> Gắn với protein tải chuyên biệt như CBG (cho cortisol), SHBG (cho testosteron, estradiol) và Albumin để tránh bị lọc đào thải sớm ở cầu thận.",
        "<b>Chuyển hóa khử hoạt —</b> Thoái hóa tại gan qua các phản ứng khử và liên hợp với acid glucuronic hoặc sulfat để chuyển thành dạng tan trong nước đào thải qua nước tiểu."
    ],
    "Vì không có kho dự trữ sẵn dạng hạt, sự tăng nồng độ steroid trong máu sau kích thích thường cần vài phút đến nửa giờ để mạng lưới enzym ty thể và lưới nội chất tổng hợp mới."
))

cards.append(make_card(
    "HS13-B1-10",
    "Hóa sinh Eicosanoid và Cơ chế Tác dụng Tại chỗ",
    "HÓA SINH EICOSANOID",
    "Đặc tính sinh hóa, phân loại và cơ chế hoạt động của nhóm hormon tác dụng tại chỗ Eicosanoid?",
    [
        "<b>Tiền thân phân tử —</b> Dẫn xuất 20 carbon từ quá trình giải phóng Acid Arachidonic (20:4 delta 5,8,11,14) từ phospholipid màng tế bào nhờ enzym Phospholipase A2 (PLA2).",
        "<b>Nhánh Cyclooxygenase (COX-1, COX-2) —</b> Tạo Prostanoid gồm Prostaglandin (PGE2 gây sốt, viêm; PGF2alpha gây co tử cung), Prostacyclin (PGI2 giãn mạch, chống đông), Thromboxan (TXA2 co mạch, đông máu).",
        "<b>Nhánh Lipoxygenase (5-LOX) —</b> Tạo Leukotriene (LTB4 hóa ứng động bạch cầu; LTC4, LTD4, LTE4 gây co thắt phế quản dữ dội trong hen phế quản).",
        "<b>Đặc tính động học —</b> Thời gian bán hủy siêu ngắn (vài giây đến vài phút), tác dụng cực kỳ khu trú theo kiểu cận tiết (paracrine) hoặc tự tiết (autocrine) và bị giáng hóa tức thì tại phổi, gan.",
        "<b>Ứng dụng dược lý —</b> Corticoid kích thích Lipocortin ức chế PLA2; Aspirin ức chế không hồi phục COX-1/2; NSAIDs ức chế thuận nghịch COX; Montelukast đối kháng thụ thể Leukotriene."
    ],
    "Eicosanoid là hormon mô tại chỗ tối quan trọng điều hòa trương lực mạch máu, đông cầm máu, phản ứng viêm và đáp ứng miễn dịch của cơ thể."
))

cards.append(make_card(
    "HS13-B1-11",
    "Khái niệm Dạng Tự do (Free Hormone) và Ý nghĩa Lâm sàng",
    "HÓA SINH LÂM SÀNG",
    "Định nghĩa dạng hormon tự do, tỷ lệ cân bằng và vì sao xét nghiệm chẩn đoán luôn ưu tiên định lượng dạng tự do (FT4, FT3)?",
    [
        "<b>Trạng thái cân bằng động —</b> [Hormon tự do] + [Protein tải] ⇌ [Phức hợp Hormon - Protein]. Trạng thái cân bằng này tuân theo định luật tác dụng khối lượng.",
        "<b>Hoạt tính sinh học độc quyền —</b> CHỈ CÓ dạng hormon tự do (Free hormone) mới có kích thước và tính chất cho phép khuếch tán qua mao mạch đến mô đích, gắn thụ thể và tạo đáp ứng sinh học.",
        "<b>Cơ chế đệm bảo vệ —</b> Hormon gắn protein đóng vai trò kho dự trữ đệm lưu thông trong máu, giúp nồng độ hormon tự do ổn định tránh dao động thất thường và bảo vệ hormon khỏi bị giáng hóa sớm.",
        "<b>Bẫy xét nghiệm protein tải —</b> Khi nồng độ protein tải thay đổi (ví dụ TBG tăng cao khi có thai hoặc dùng thuốc tránh thai estrogen), nồng độ hormon TOÀN PHẦN (Total T4) tăng giả tạo nhưng bệnh nhân hoàn toàn bình giáp.",
        "<b>Ưu thế xét nghiệm dạng tự do —</b> Định lượng FT4 và FT3 phản ánh chính xác 100% tình trạng chức năng tuyến giáp mà không bị nhiễu bởi sự biến động nồng độ protein huyết tương."
    ],
    "Đây là nguyên tắc kinh điển trong thực hành nội tiết: luôn biện luận chức năng tuyến nội tiết dựa trên nồng độ hormon tự do (Free T4, Free Cortisol, Free Testosterone)."
))

# ==============================================================================
# SECTION B2: GPCR, G-PROTEIN, SECOND MESSENGERS & ĐỘC TỐ (13 thẻ: HS13-B2-01 -> HS13-B2-13)
# ==============================================================================

cards.append(make_card(
    "HS13-B2-01",
    "Cấu trúc Thụ thể 7 Đoạn Xuyên Màng (GPCR / 7-TM)",
    "CẤU TRÚC GPCR",
    "Đặc điểm cấu tạo không gian bậc 3 của siêu họ thụ thể bắt cặp G-protein (GPCR)?",
    [
        "<b>Khung 7 chuỗi xoắn alpha —</b> Chuỗi polypeptide đơn cuộn thành 7 đoạn xoắn alpha kỵ nước cắm xuyên qua lớp phospholipid kép của màng sinh chất.",
        "<b>Đầu tận ngoại bào (-NH2) —</b> Hướng ra dịch ngoại bào, thường được glycosyl hóa và phối hợp các quai ngoại bào tạo thành túi gắn đặc hiệu với phân tử hormon.",
        "<b>Đầu tận nội bào (-COOH) —</b> Hướng vào dịch bào tương, chứa các gốc Serin/Threonin là vị trí bị phosphoryl hóa bởi GRK để điều hòa trơ hóa thụ thể.",
        "<b>Các quai nội bào (Intracellular loops) —</b> Đặc biệt là quai thứ ba (i3 loop) tiếp xúc trực tiếp và quyết định tính đặc hiệu tương tác với phức hợp Heterotrimeric G-protein."
    ],
    "GPCR là họ thụ thể lớn nhất trong bộ gen người (hơn 800 gen mã hóa) và là đích tác động của hơn 30 - 40% các loại thuốc điều trị hiện đại trên thị trường."
))

cards.append(make_card(
    "HS13-B2-02",
    "Cấu trúc Heterotrimeric G-protein và Vai trò Các Tiểu đơn vị",
    "CẤU TRÚC G-PROTEIN",
    "Cấu tạo 3 tiểu đơn vị của Heterotrimeric G-protein và vai trò chức năng của từng tiểu đơn vị?",
    [
        "<b>Tiểu đơn vị G-alpha (39 - 52 kDa) —</b> Là trung tâm điều hành mang vị trí gắn guanine nucleotid (GDP hoặc GTP); sở hữu hoạt tính enzym thủy phân GTPase nội tại.",
        "<b>Tiểu đơn vị G-beta (35 - 36 kDa) —</b> Cấu trúc cánh quạt beta (beta-propeller 7 cánh), liên kết chặt chẽ không tách rời với tiểu đơn vị gamma.",
        "<b>Tiểu đơn vị G-gamma (7 - 10 kDa) —</b> Là một peptide ngắn được gắn thêm gốc lipid (prenyl hóa) neo chặt phức hợp G-beta-gamma vào mặt trong màng sinh chất.",
        "<b>Phức hợp dị nhị tụ G-beta-gamma —</b> Giữ G-alpha ở trạng thái bất hoạt khi tế bào nghỉ; khi phân ly có thể trực tiếp điều hòa kênh ion K+, Ca2+ hoặc enzym hiệu ứng."
    ],
    "Tính đặc thù của đáp ứng tế bào chủ yếu được phân loại theo tiểu đơn vị G-alpha (gồm 4 họ chính: Gs-alpha, Gi-alpha, Gq-alpha và G12/13-alpha)."
))

cards.append(make_card(
    "HS13-B2-03",
    "Chu trình Vận hành Phân tử của G-protein (GDP/GTP Cycle)",
    "CHU TRÌNH G-PROTEIN",
    "Các bước chuyển đổi phân tử tuần hoàn trong chu kỳ hoạt hóa và tự tắt tín hiệu của G-protein?",
    [
        "<b>Bước 1 (Trạng thái nghỉ) —</b> Tiểu đơn vị alpha gắn chặt GDP và liên kết với dị nhị tụ beta-gamma tạo phức hợp dị tam tụ alpha-beta-gamma-GDP bất hoạt.",
        "<b>Bước 2 (Trao đổi GDP lấy GTP) —</b> Hormon gắn GPCR làm biến đổi cấu hình thụ thể; GPCR hoạt động như một GEF thúc đẩy alpha giải phóng GDP và nạp GTP từ bào tương.",
        "<b>Bước 3 (Phân ly tiểu đơn vị) —</b> G-alpha-GTP biến đổi cấu hình, tách rời khỏi phức hợp G-beta-gamma tạo thành hai nhánh truyền tin độc lập dọc mặt trong màng.",
        "<b>Bước 4 (Kích hoạt enzym hiệu ứng) —</b> G-alpha-GTP tương tác kích hoạt hoặc ức chế các enzym hiệu ứng màng như Adenylate Cyclase hoặc Phospholipase C.",
        "<b>Bước 5 (Tự tắt bởi đồng hồ GTPase) —</b> Hoạt tính GTPase nội tại của G-alpha tự thủy phân GTP thành GDP + Pi sau vài giây; được thúc đẩy nhanh gấp hàng ngàn lần bởi protein RGS (GAP).",
        "<b>Bước 6 (Tái tổ hợp trạng thái nghỉ) —</b> G-alpha-GDP mất ái lực với enzym hiệu ứng, quay lại gắn chặt với G-beta-gamma để sẵn sàng cho chu kỳ mới."
    ],
    "Hoạt tính GTPase nội tại của G-alpha đóng vai trò như một 'chiếc đồng hồ hẹn giờ phân tử' (molecular timer) giúp đảm bảo tín hiệu tế bào chỉ tồn tại trong thời gian ngắn có kiểm soát."
))

cards.append(make_card(
    "HS13-B2-04",
    "Đối kháng Chức năng Giữa Gs và Gi trong Hệ Adenylate Cyclase",
    "ĐỐI KHÁNG Gs VS Gi",
    "Sự tác động đối kháng giữa protein Gs và Gi lên enzym Adenylate Cyclase và danh mục hormon tương ứng?",
    [
        "<b>Protein Gs (Kích thích) —</b> Tiểu đơn vị Gs-alpha-GTP kích hoạt Adenylate Cyclase làm tăng bùng nổ nồng độ cAMP nội bào.",
        "<b>Danh mục hormon qua Gs —</b> Glucagon, Adrenalin (thụ thể beta-1, beta-2), ACTH, TSH, LH, FSH, PTH, Calcitonin, ADH (thụ thể V2 ở ống thận).",
        "<b>Protein Gi (Ức chế) —</b> Tiểu đơn vị Gi-alpha-GTP ức chế enzym Adenylate Cyclase; đồng thời phức hợp G-beta-gamma của Gi gắn bẫy Gs-alpha tự do làm hạ nồng độ cAMP.",
        "<b>Danh mục phân tử qua Gi —</b> Somatostatin, Adrenalin / Noradrenalin (thụ thể alpha-2), Acetylcholin (thụ thể Muscarinic M2), Adenosin (thụ thể A1)."
    ],
    "Mô hình đối kháng kép này cho phép tế bào điều chỉnh linh hoạt nồng độ cAMP nội bào như một chiếc bàn đạp ga (Gs) và phanh hãm (Gi) chuẩn xác."
))

cards.append(make_card(
    "HS13-B2-05",
    "Tổng hợp cAMP bởi Adenylate Cyclase và Thoái hóa bởi Phosphodiesterase",
    "CHUYỂN HÓA cAMP",
    "Phương trình phản ứng tổng hợp cAMP của Adenylate Cyclase và thoái hóa bởi Phosphodiesterase?",
    [
        "<b>Tổng hợp bởi Adenylate Cyclase —</b> ATP → cAMP (Adenosin-3',5'-cyclic monophosphat) + PPi (cần ion Mg2+). PPi lập tức bị Pyrophosphatase thủy phân thành 2 Pi kéo phản ứng một chiều.",
        "<b>Thoái hóa bởi Phosphodiesterase (PDE) —</b> cAMP + H2O → 5'-AMP (không còn hoạt tính truyền tin thứ hai).",
        "<b>Ức chế bởi Methylxanthine —</b> Caffeine, Theophylline, Theobromine ức chế cạnh tranh enzym Phosphodiesterase, ngăn cản sự phân hủy cAMP.",
        "<b>Hệ quả dược lý Methylxanthine —</b> cAMP tích lũy kéo dài khuếch đại tác dụng Catecholamin, làm tăng co bóp cơ tim, giãn cơ trơn phế quản và gây hưng phấn hệ thần kinh trung ương."
    ],
    "Theophylline từng là thuốc giãn phế quản đường uống kinh điển trong điều trị hen suyễn nhờ cơ chế duy trì nồng độ cAMP kéo dài trong tế bào cơ trơn đường thở."
))

cards.append(make_card(
    "HS13-B2-06",
    "Cấu trúc Tứ tụ và Cơ chế Hoạt hóa Protein Kinase A (PKA)",
    "HOẠT HÓA PKA",
    "Cấu tạo phân tử của Protein Kinase A ở trạng thái nghỉ và cơ chế kích hoạt khi có mặt phân tử cAMP?",
    [
        "<b>Cấu trúc nghỉ bất hoạt —</b> Là một phức hợp tứ tụ (tetramer) gồm 2 tiểu đơn vị điều hòa (R) và 2 tiểu đơn vị xúc tác (C): dạng R2C2. Mỗi tiểu đơn vị R có 2 vị trí gắn cAMP.",
        "<b>Cơ chế gắn đồng hóa cAMP —</b> Khi cAMP tăng cao, 4 phân tử cAMP gắn đồng hóa (cooperative) vào 2 tiểu đơn vị R: R2C2 + 4 cAMP ⇌ R2(cAMP)4 + 2 C (tự do hoạt động).",
        "<b>Giải phóng tiểu đơn vị xúc tác —</b> Sự gắn cAMP làm biến đổi cấu hình R, giải phóng 2 tiểu đơn vị C dưới dạng monomer có hoạt tính xúc tác tối đa.",
        "<b>Cơ chế phản ứng xúc tác của C —</b> Sử dụng ATP để phosphoryl hóa các gốc Serin hoặc Threonin trên các protein enzym đích: Protein-OH + ATP → Protein-O-PO3(2-) + ADP.",
        "<b>Tác động tại nhân tế bào —</b> Tiểu đơn vị C khuếch tán vào nhân, phosphoryl hóa yếu tố phiên mã CREB gắn vào đoạn CRE trên DNA kích thích phiên mã gen (như PEPCK, G6Pase)."
    ],
    "Sự gắn đồng hóa 4 phân tử cAMP cho phép hệ thống đáp ứng cực kỳ nhạy bén (dạng đường cong sigmoid) ngay khi nồng độ cAMP trong tế bào chỉ biến thiên nhẹ."
))

cards.append(make_card(
    "HS13-B2-07",
    "Khuếch đại Tín hiệu Hình tháp: Mô hình Adrenalin / Glucagon Gan",
    "KHUẾCH ĐẠI TÍN HIỆU",
    "Dòng thác khuếch đại tín hiệu từng tầng từ 1 phân tử hormon đến hàng triệu phân tử glucose giải phóng?",
    [
        "<b>Tầng 1 (Hormon gắn thụ thể) —</b> 1 phân tử Adrenalin hoặc Glucagon gắn vào GPCR trên màng tế bào gan.",
        "<b>Tầng 2 (Hoạt hóa G-protein) —</b> Thụ thể hoạt hóa kích hoạt hàng chục đến hàng trăm phân tử protein Gs.",
        "<b>Tầng 3 (Tổng hợp cAMP) —</b> Mỗi Gs-alpha-GTP kích hoạt Adenylate Cyclase tạo hàng ngàn phân tử cAMP.",
        "<b>Tầng 4 (Hoạt hóa PKA) —</b> cAMP hoạt hóa hàng trăm phân tử enzym Protein Kinase A.",
        "<b>Tầng 5 (Dòng thác Kinase) —</b> PKA phosphoryl hóa hoạt hóa hàng ngàn phân tử Phosphorylase Kinase.",
        "<b>Tầng 6 (Hoạt hóa Glycogen Phosphorylase) —</b> Phosphorylase Kinase chuyển hàng vạn Glycogen Phosphorylase b thành thể a.",
        "<b>Tầng 7 (Giải phóng Glucose) —</b> Glycogen Phosphorylase a phân giải hàng triệu gốc Glucose-1-P chuyển thành Glucose tự do vào máu."
    ],
    "Tính chất khuếch đại đa tầng (cascade amplification) giải thích vì sao nồng độ hormon chỉ cần ở mức picomolar (10^-12 M) vẫn tạo ra đáp ứng sinh học khổng lồ tức thì."
))

cards.append(make_card(
    "HS13-B2-08",
    "Bệnh học Phân tử Độc tố Tả (Cholera Toxin)",
    "ĐỘC TỐ TẢ",
    "Cơ chế hóa sinh phân tử của độc tố vi khuẩn tả (Vibrio cholerae) tác động lên chu trình G-protein?",
    [
        "<b>Cấu trúc độc tố —</b> Phức hợp độc tố ruột AB5 (1 tiểu phần enzym A và 5 tiểu phần B gắn thụ thể ganglioside GM1 biểu mô ruột).",
        "<b>Cơ chất đích phân tử —</b> Tác động đặc hiệu lên tiểu đơn vị Gs-alpha của protein G kích thích.",
        "<b>Cơ chế phản ứng —</b> Xúc tác ADP-ribosyl hóa chuyển gốc ADP-ribose từ NAD+ gắn vĩnh viễn vào gốc Arginin của Gs-alpha: NAD+ + Gs-alpha-(Arg) → ADP-ribosyl-Gs-alpha + Nicotinamid + H+.",
        "<b>Hậu quả phân tử —</b> Làm mất hoàn toàn hoạt tính enzym GTPase nội tại của Gs-alpha; Gs-alpha bị khóa chết ở trạng thái gắn GTP luôn luôn bật.",
        "<b>Hậu quả lâm sàng —</b> Adenylate Cyclase bị kích hoạt liên tục, nồng độ cAMP tăng vọt gấp hơn 100 lần, PKA kích thích mở toang kênh CFTR bài tiết Cl-, Na+ và nước ồ ạt gây tiêu chảy mất nước trụy mạch (15 - 20 L/ngày)."
    ],
    "Hiểu rõ cơ chế ADP-ribosyl hóa của độc tố tả là ví dụ y khoa kinh điển về sự phá hủy cơ chế tự tắt tín hiệu (GTPase clock) của G-protein."
))

cards.append(make_card(
    "HS13-B2-09",
    "Bệnh học Phân tử Độc tố Ho gà (Pertussis Toxin)",
    "ĐỘC TỐ HO GÀ",
    "Cơ chế hóa sinh phân tử của độc tố ho gà (Bordetella pertussis) và sự khác biệt then chốt so với độc tố tả?",
    [
        "<b>Cơ chất đích phân tử —</b> Tác động đặc hiệu lên tiểu đơn vị Gi-alpha của protein G ức chế (trong khi độc tố tả tác động lên Gs-alpha).",
        "<b>Cơ chế phản ứng —</b> Xúc tác ADP-ribosyl hóa chuyển gốc ADP-ribose từ NAD+ gắn vào gốc Cystein ở đầu C của Gi-alpha: NAD+ + Gi-alpha-(Cys) → ADP-ribosyl-Gi-alpha + Nicotinamid + H+.",
        "<b>Hậu quả phân tử —</b> Ngăn cản Gi-alpha tương tác với thụ thể GPCR, khóa chết Gi-alpha ở trạng thái gắn GDP bất hoạt (luôn luôn tắt).",
        "<b>Hậu quả nồng độ cAMP —</b> Làm mất hoàn toàn cơ chế phanh hãm ức chế Adenylate Cyclase, dẫn đến nồng độ cAMP tích lũy tăng cao kéo dài.",
        "<b>Biểu hiện bệnh lý —</b> Ức chế hóa ứng động bạch cầu lympho, giảm thanh thải đường hô hấp, gây tăng bạch cầu lympho máu và các cơn ho rũ rượi đặc trưng."
    ],
    "Cả hai độc tố đều làm tăng nồng độ cAMP nội bào, nhưng bằng hai cơ chế đối nghịch: Độc tố tả khóa Gs BẬT, còn Độc tố ho gà khóa Gi TẮT."
))

cards.append(make_card(
    "HS13-B2-10",
    "Con đường Phospholipase C (PLC) - IP3 / DAG qua Gq",
    "CON ĐƯỜNG Gq - PLC",
    "Chuỗi phản ứng phát động dòng thác tín hiệu từ GPCR bắt cặp Gq đến sự tạo thành IP3 và DAG?",
    [
        "<b>Phối tử đặc hiệu qua Gq —</b> Oxytocin, Vasopressin (thụ thể V1), Angiotensin II (thụ thể AT1), Noradrenalin (thụ thể alpha-1), TRH, GnRH.",
        "<b>Hoạt hóa Gq —</b> Hormon gắn GPCR kích thích Gq-alpha nạp GTP, phân ly kích hoạt enzym Phospholipase C-beta (PLC-beta) gắn màng.",
        "<b>Thủy phân cơ chất lipid màng —</b> PLC thủy phân liên kết phosphodiester của Phosphatidylinositol 4,5-bisphosphat (PIP2) tạo 2 chất truyền tin thứ hai: PIP2 + H2O → IP3 + DAG.",
        "<b>Đặc tính IP3 —</b> Inositol 1,4,5-triphosphat là phân tử phân cực nhỏ tan trong nước, khuếch tán nhanh vào dịch bào tương.",
        "<b>Đặc tính DAG —</b> 1,2-Diacylglycerol là lipid kỵ nước chứa 2 chuỗi acid béo bám chặt và di chuyển trên bình diện màng tế bào."
    ],
    "Cắt một phân tử PIP2 màng sinh chất tạo ra đồng thời 2 chất truyền tin thứ hai với số phận và đích tác động nội bào hoàn toàn khác biệt."
))

cards.append(make_card(
    "HS13-B2-11",
    "Vai trò của IP3 trong Giải phóng Ca2+ và Bơm SERCA",
    "IP3 VÀ CANXI NỘI BÀO",
    "Cơ chế IP3 kích thích giải phóng Ca2+ từ lưới nội chất và vai trò của các bơm Ca2+-ATPase duy trì gradient?",
    [
        "<b>Nồng độ Ca2+ trạng thái nghỉ —</b> Được duy trì cực thấp trong bào tương (khoảng 100 nM = 10^-7 M) nhờ bơm PMCA (đẩy ra ngoài tế bào) và bơm SERCA (bơm vào lòng túi lưới nội chất).",
        "<b>Gắn thụ thể IP3 Receptor —</b> IP3 khuếch tán đến màng lưới nội chất, gắn đặc hiệu vào kênh Ca2+ phụ thuộc phối tử (IP3R).",
        "<b>Giải phóng Ca2+ bùng nổ —</b> Kênh mở cho phép ion Ca2+ tuôn ồ ạt từ lòng lưới nội chất ra bào tương theo gradient nồng độ, làm nồng độ Ca2+ bào tương tăng vọt gấp 10 - 100 lần (>1 µM).",
        "<b>Tái lập nồng độ nghỉ —</b> Khi tín hiệu chấm dứt, bơm Ca2+-ATPase lưới nội bào (SERCA) tích cực gom Ca2+ nhốt trở lại lòng lưới nội chất và enzym 5-phosphatase giáng hóa IP3."
    ],
    "Sự chênh lệch nồng độ ion Ca2+ giữa dịch ngoại bào/lòng lưới nội chất (~1 - 2 mM) và dịch bào tương (100 nM) là 10.000 lần, biến Ca2+ thành chất truyền tin thứ hai có tốc độ phát tín hiệu nhanh nhất cơ thể."
))

cards.append(make_card(
    "HS13-B2-12",
    "Cơ chế Hoạt hóa Protein Kinase C (PKC) và Phức hợp Ca2+-Calmodulin",
    "HOẠT HÓA PKC VÀ CALMODULIN",
    "Cơ chế phối hợp hoạt hóa Protein Kinase C (PKC) và chức năng của phức hợp Ca2+-Calmodulin?",
    [
        "<b>Hoạt hóa Protein Kinase C (PKC) —</b> Ca2+ bào tương tăng làm PKC chuyển dịch từ bào tương ra màng; tại màng PKC gắn kết với DAG và Phosphatidylserin để chuyển sang trạng thái hoạt động tối đa.",
        "<b>Tác động của PKC —</b> Phosphoryl hóa các gốc Serin/Threonin trên các enzym điều hòa chu kỳ tế bào, biệt hóa mô và co cơ trơn.",
        "<b>Cấu trúc Calmodulin (CaM) —</b> Protein cảm biến ion canxi (17 kDa) chứa 4 vị trí gắn Ca2+ cấu trúc ngón tay 'EF-hand' với ái lực rất cao.",
        "<b>Biến đổi cấu hình khi gắn Ca2+ —</b> Gắn đủ 4 ion Ca2+ làm Calmodulin bộc lộ rãnh kỵ nước kẹp lấy enzym Myosin Light Chain Kinase (MLCK) hoặc CaMKII.",
        "<b>Hiệu ứng co cơ trơn —</b> MLCK được hoạt hóa phosphoryl hóa chuỗi nhẹ myosin, kích hoạt tương tác actin-myosin gây co cơ trơn tử cung (Oxytocin) hoặc co mạch (Vasopressin V1, Angiotensin II)."
    ],
    "Cơ chế hiệp đồng giữa Ca2+ và DAG đảm bảo PKC chỉ hoạt hóa tại đúng thời điểm và vị trí màng tế bào cần phát động đáp ứng."
))

cards.append(make_card(
    "HS13-B2-13",
    "Hệ Guanylate Cyclase - cGMP - PKG: Màng (ANP) vs Bào tương (NO)",
    "HỆ GUANYLATE CYCLASE",
    "So sánh hai dạng enzym Guanylate Cyclase, chất truyền tin cGMP và ứng dụng dược lý thuốc Nitrate, PDE5i?",
    [
        "<b>Guanylate Cyclase màng (Receptor GC) —</b> Protein xuyên màng đơn độc tiếp nhận ANP/BNP của tim; kích hoạt domain xúc tác nội bào chuyển GTP → cGMP; kích hoạt PKG gây bài niệu Na+ ở ống thận, hạ huyết áp.",
        "<b>Guanylate Cyclase bào tương (sGC) —</b> Enzym hòa tan chứa nhóm ngoại Heme (Fe2+), được kích hoạt bởi khí Nitric Oxide (NO) do tế bào nội mô tạo từ L-Arginin (nhờ eNOS).",
        "<b>Cơ chế giãn mạch của cGMP —</b> cGMP kích hoạt Protein Kinase G (PKG) làm giảm Ca2+ nội bào và kích hoạt Phosphatase chuỗi nhẹ myosin (MLCP) gây giãn cơ trơn mạch máu toàn thân.",
        "<b>Thuốc giãn mạch Nitrate —</b> Nitroglycerin giải phóng khí NO, kích hoạt sGC tạo cGMP gây giãn tĩnh mạch và động mạch vành, cắt cơn đau thắt ngực.",
        "<b>Thuốc ức chế PDE5 —</b> Sildenafil, Tadalafil ức chế enzym Phosphodiesterase typ 5 giáng hóa cGMP thành 5'-GMP, duy trì nồng độ cGMP kéo dài gây giãn mạch thể hang (chữa rối loạn cương) và hạ áp phổi."
    ],
    "Hệ cGMP/PKG là đích điều trị của hai nhóm thuốc tim mạch - nam khoa nổi tiếng nhất lịch sử dược lý học: Nitroglycerin (khám phá giải Nobel 1998) và Sildenafil (Viagra)."
))

# ==============================================================================
# SECTION B3: THỤ THỂ TYROSINE KINASE (RTK) & CON ĐƯỜNG JAK/STAT (11 thẻ: HS13-B3-01 -> HS13-B3-11)
# ==============================================================================

cards.append(make_card(
    "HS13-B3-01",
    "Đặc điểm Chung của Thụ thể Tyrosine Kinase (RTK)",
    "ĐẠI CƯƠNG RTK",
    "Đặc điểm cấu trúc chung và cơ chế kích hoạt của siêu họ thụ thể gắn enzym Tyrosine Kinase nội tại?",
    [
        "<b>Hoạt tính enzym nội tại —</b> Sở hữu domain enzym Tyrosine Kinase nằm ngay trong cấu trúc chuỗi polypeptide nội bào của chính thụ thể (không cần tuyển mộ kinase ngoài).",
        "<b>Các phối tử điển hình —</b> Insulin, IGF-1, Yếu tố tăng trưởng biểu bì (EGF), Yếu tố tăng trưởng từ tiểu cầu (PDGF), Yếu tố tăng trưởng nội mô mạch máu (VEGF), FGF.",
        "<b>Hiện tượng nhị hợp hóa (Dimerization) —</b> Đa số tồn tại dạng monomer trên màng; khi phối tử gắn vào sẽ kéo 2 phân tử thụ thể lại gần tạo phức hợp nhị tụ (dimer).",
        "<b>Tự phosphoryl hóa chéo (Trans-autophosphorylation) —</b> Mỗi chuỗi polypeptide dùng ATP để phosphoryl hóa các gốc Tyrosin trên chuỗi đối diện, bộc lộ hoàn toàn trung tâm xúc tác.",
        "<b>Tạo điểm neo giữ SH2 —</b> Các gốc Phospho-Tyrosin trên thụ thể trở thành vị trí gắn đặc hiệu cho các protein chuyển tiếp mang domain nhận diện SH2 (Src Homology 2)."
    ],
    "Cơ chế tự phosphoryl hóa chéo trên gốc Tyrosine là nguyên lý kích hoạt phổ biến của hầu hết các thụ thể yếu tố tăng trưởng điều hòa chu kỳ tế bào và sinh ung."
))

cards.append(make_card(
    "HS13-B3-02",
    "Cấu trúc Phân tử Dị Tứ tụ của Thụ thể Insulin",
    "CẤU TRÚC THỤ THỂ INSULIN",
    "Cấu tạo không gian của thụ thể Insulin có điểm gì đặc biệt so với các thụ thể RTK khác?",
    [
        "<b>Cấu trúc dị tứ tụ có sẵn —</b> Khác với các RTK khác ở dạng monomer, thụ thể Insulin tồn tại sẵn trên màng tế bào dưới dạng một phức hợp dị tứ tụ: alpha2-beta2.",
        "<b>Hai tiểu đơn vị alpha (135 kDa mỗi chuỗi) —</b> Nằm hoàn toàn ở phía ngoại bào, chứa túi gắn đặc hiệu với phân tử Insulin.",
        "<b>Hai tiểu đơn vị beta (95 kDa mỗi chuỗi) —</b> Là các protein xuyên màng, có domain ngắn xuyên màng và domain nội bào lớn chứa hoạt tính enzym Tyrosine Kinase.",
        "<b>Cầu nối Disulfua (-S-S-) —</b> Hai tiểu đơn vị alpha liên kết với nhau bằng cầu disulfua, và mỗi chuỗi alpha liên kết với một chuỗi beta bằng cầu disulfua liên chuỗi.",
        "<b>Cơ chế kích hoạt —</b> Khi Insulin gắn vào 2 tiểu đơn vị alpha, nó làm thay đổi cấu hình kéo 2 domain beta lại gần nhau để thực hiện tự phosphoryl hóa chéo."
    ],
    "Nhờ có sẵn cấu trúc tứ tụ alpha2-beta2, thụ thể Insulin không cần phải trải qua giai đoạn dimer hóa chậm chạp mà có thể lập tức tự phosphoryl hóa ngay khi Insulin gắn kết."
))

cards.append(make_card(
    "HS13-B3-03",
    "Vai trò Cơ chất Thụ thể Insulin (IRS-1 và IRS-2)",
    "CƠ CHẤT IRS",
    "Đặc điểm phân tử và vai trò đóng vai trò trung tâm điều phối tín hiệu của các protein IRS?",
    [
        "<b>Bản chất IRS —</b> Insulin Receptor Substrates (chủ yếu là IRS-1 ở cơ/mỡ và IRS-2 ở gan) là các protein neo giữ trung gian trong bào tương.",
        "<b>Domain gắn thụ thể —</b> Mang domain PTB (Phosphotyrosine-Binding) và domain PH (Pleckstrin Homology) giúp nhận diện và bám vào thụ thể Insulin đã hoạt hóa.",
        "<b>Phosphoryl hóa đa điểm trên Tyrosin —</b> Thụ thể Insulin phosphoryl hóa IRS trên nhiều gốc Tyrosin đặc thù (ít nhất 8 gốc Tyrosin được gắn phosphat).",
        "<b>Trung tâm phân nhánh tín hiệu —</b> Các gốc Phospho-Tyrosin trên IRS trở thành các ổ cắm gắn kết các protein chuyển tiếp mang domain SH2 (như p85 của PI3K, Grb2, SHP2).",
        "<b>Điều hòa ngược ức chế —</b> Phosphoryl hóa các gốc Serin/Threonin trên IRS-1 (do stress, acid béo tự do, TNF-alpha) làm mất khả năng tương tác với thụ thể, gây đề kháng insulin."
    ],
    "IRS-1 hoạt động như một 'bảng vi mạch trung tâm' chuyển tiếp và phân luồng dòng thông tin từ thụ thể Insulin tới các mạng lưới enzym chuyển hóa nội bào."
))

cards.append(make_card(
    "HS13-B3-04",
    "Nhánh Tín hiệu PI3K / Akt và Sự Tạo thành PIP3",
    "CON ĐƯỜNG PI3K / AKT",
    "Các bước hoạt hóa enzym Phosphoinositide 3-Kinase (PI3K) và phân tử lipid màng PIP3?",
    [
        "<b>Tuyển mộ PI3K —</b> Tiểu đơn vị điều hòa p85 của PI3K mang domain SH2 gắn vào gốc Phospho-Tyrosin trên IRS-1, kéo tiểu đơn vị xúc tác p110 đến áp sát màng tế bào.",
        "<b>Phosphoryl hóa PIP2 tạo PIP3 —</b> PI3K xúc tác gắn thêm gốc phosphat vào vị trí carbon số 3 của vòng inositol trên PIP2 màng để tạo Phosphatidylinositol 3,4,5-trisphosphat (PIP3).",
        "<b>Tuyển mộ kinase mang domain PH —</b> PIP3 đóng vai trò là điểm neo giữ màng thu hút PDK-1 (Phosphoinositide-Dependent Kinase-1) và Akt (Protein Kinase B).",
        "<b>Hoạt hóa hoàn toàn Akt —</b> PDK-1 phosphoryl hóa Akt tại gốc Threonin-308, kết hợp phức hợp mTORC2 phosphoryl hóa Akt tại Serin-473 kích hoạt Akt tối đa.",
        "<b>Tách khỏi màng —</b> Akt sau khi hoạt hóa sẽ tách rời khỏi màng tế bào, di chuyển vào bào tương và nhân để phosphoryl hóa hàng loạt enzym đích."
    ],
    "Chuyển đổi PIP2 thành PIP3 bởi PI3K là công tắc phân tử cốt tử điều khiển toàn bộ đáp ứng chuyển hóa đồng hóa của Insulin trong cơ thể."
))

cards.append(make_card(
    "HS13-B3-05",
    "Cơ chế Chuyển vị Kênh GLUT4 ra Màng nhờ Akt",
    "CHUYỂN VỊ GLUT4",
    "Cơ chế phân tử giúp Insulin kích thích đưa kênh vận chuyển Glucose GLUT4 ra màng tế bào cơ và mỡ?",
    [
        "<b>Trạng thái nghỉ không có Insulin —</b> Kênh GLUT4 nằm ẩn bên trong các túi bóng nội bào (vesicles) trong bào tương của tế bào cơ vân và mô mỡ.",
        "<b>Vai trò protein AS160 —</b> Protein AS160 (Akt Substrate of 160 kDa) hoạt động như một GAP giữ protein G nhỏ Rab ở trạng thái bất hoạt gắn GDP, ngăn cản bóng chuyển vị.",
        "<b>Phosphoryl hóa ức chế AS160 bởi Akt —</b> Akt hoạt hóa phosphoryl hóa làm bất hoạt AS160, cho phép Rab nạp GTP sang trạng thái hoạt động.",
        "<b>Hòa màng bóng chứa GLUT4 —</b> Rab-GTP chỉ huy các túi chứa GLUT4 tiến tới và hòa nhập màng sinh chất nhờ phức hợp SNARE, phơi bày hàng vạn kênh GLUT4 ra bề mặt ngoài.",
        "<b>Tăng thu nạp Glucose —</b> Tốc độ vận chuyển glucose từ máu vào cơ và mỡ tăng vọt từ 10 đến 40 lần, làm hạ nhanh nồng độ đường huyết sau bữa ăn."
    ],
    "Mô cơ vân và mô mỡ là nơi tiêu thụ hơn 80% lượng glucose sau ăn; sự chuyển vị hoàn hảo của GLUT4 phụ thuộc tuyệt đối vào con đường tín hiệu Akt/AS160."
))

cards.append(make_card(
    "HS13-B3-06",
    "Hoạt hóa Glycogen Synthase qua Ức chế GSK-3 bởi Akt",
    "TỔNG HỢP GLYCOGEN",
    "Cơ chế 'ức chế một chất ức chế' (Disinhibition) giúp Insulin kích hoạt enzym Glycogen Synthase?",
    [
        "<b>Trạng thái nghỉ bất hoạt —</b> Enzym Glycogen Synthase Kinase-3 (GSK-3) liên tục phosphoryl hóa enzym Glycogen Synthase, giữ Glycogen Synthase ở dạng b (bất hoạt).",
        "<b>Phosphoryl hóa GSK-3 bởi Akt —</b> Khi có tín hiệu Insulin, Akt tiến hành phosphoryl hóa một gốc Serin đặc hiệu trên enzym GSK-3 làm bất hoạt hoàn toàn GSK-3.",
        "<b>Mất sự kìm hãm —</b> Khi GSK-3 bị vô hiệu hóa, nó không thể tiếp tục phosphoryl hóa Glycogen Synthase.",
        "<b>Khử phosphat bởi PP-1 —</b> Enzym Protein Phosphatase-1 (PP-1) chiếm ưu thế, khử bỏ các gốc phosphat trên Glycogen Synthase, chuyển nó sang dạng a (hoạt động hoàn toàn).",
        "<b>Tăng tốc tổng hợp Glycogen —</b> Glycogen Synthase a xúc tác gắn các gốc UDP-Glucose vào chuỗi glycogen dự trữ tại gan và cơ vân."
    ],
    "Đây là nguyên lý sinh hóa kinh điển 'kích hoạt bằng cách ức chế chất kìm hãm': Akt ức chế GSK-3 để giải phóng Glycogen Synthase sang trạng thái hoạt động."
))

cards.append(make_card(
    "HS13-B3-07",
    "Các Tác động Đồng hóa Khác của Akt: mTORC1 và SREBP-1c",
    "ĐỒNG HÓA QUA AKT",
    "Các hiệu ứng đồng hóa lipid, protein và chống dị hóa then chốt được điều hòa qua nhánh Akt?",
    [
        "<b>Kích thích tổng hợp Protein —</b> Akt phosphoryl hóa làm bất hoạt phức hợp TSC1/TSC2, giải phóng Rheb-GTP kích hoạt phức hợp mTORC1; mTORC1 phosphoryl hóa p70S6K và 4E-BP1 đẩy mạnh dịch mã tổng hợp protein cơ vân.",
        "<b>Kích thích tổng hợp Lipid —</b> Kích hoạt yếu tố phiên mã SREBP-1c tại gan, kích thích phiên mã các enzym sinh tổng hợp acid béo và triglycerid (Acetyl-CoA Carboxylase, Fatty Acid Synthase).",
        "<b>Ức chế tân tạo đường tại gan —</b> Akt phosphoryl hóa yếu tố phiên mã FoxO1 làm FoxO1 bị đẩy ra khỏi nhân tế bào vào bào tương, ức chế phiên mã gen PEPCK và Glucose-6-phosphatase.",
        "<b>Chống chết theo chương trình (Anti-apoptosis) —</b> Akt phosphoryl hóa làm bất hoạt protein tiền chết theo chương trình Bad và Caspase-9, thúc đẩy sự sinh tồn của tế bào."
    ],
    "Insulin là hormon đồng hóa (anabolic hormone) mạnh nhất trong cơ thể; nhánh Akt phụ trách toàn bộ các nhiệm vụ tích trữ năng lượng dưới dạng glycogen, mỡ và cơ."
))

cards.append(make_card(
    "HS13-B3-08",
    "Tắt Tín hiệu và Khử Hoạt Thụ thể RTK: Vai trò PTEN và PTP1B",
    "ĐIỀU HÒA TẮT TÍN HIỆU",
    "Các cơ chế phân tử chịu trách nhiệm dập tắt tín hiệu thụ thể Tyrosine Kinase và vai trò enzym phosphatase?",
    [
        "<b>Enzym PTEN (Phosphatase and Tensin Homolog) —</b> Khử gốc phosphat ở vị trí carbon số 3 của lipid màng PIP3 để chuyển ngược lại thành PIP2, đóng vai trò là phanh hãm dập tắt con đường PI3K/Akt.",
        "<b>Đột biến gen PTEN —</b> Đột biến mất chức năng của PTEN khiến PIP3 tích lũy vô tổ chức, Akt bị kích hoạt quá mức dẫn đến tăng sinh tế bào ác tính và ung thư.",
        "<b>Enzym PTP1B (Protein Tyrosine Phosphatase 1B) —</b> Khử bỏ các gốc phosphat trên các gốc Tyrosin của thụ thể Insulin và phân tử IRS-1, đưa chúng trở về trạng thái nghỉ bất hoạt.",
        "<b>Nhập bào và thoái hóa thụ thể —</b> Thụ thể Insulin bị ubiquitin hóa bởi ligase E3 (Cbl) và nhập bào qua bóng bọc Clathrin; một phần được tái chế ra màng, phần lớn bị phân hủy tại Lysosome."
    ],
    "Cân bằng động giữa hoạt tính Kinase và Phosphatase quyết định chính xác biên độ và thời gian tồn tại của tín hiệu chuyển hóa trong tế bào."
))

cards.append(make_card(
    "HS13-B3-09",
    "Nhánh Tín hiệu Ras - Raf - MEK - ERK (MAPK Pathway)",
    "CON ĐƯỜNG RAS / MAPK",
    "Dòng thác truyền tin phân bào và sinh trưởng tế bào từ thụ thể RTK qua chuỗi protein kinase MAPK?",
    [
        "<b>Phức hợp Grb2 - SOS —</b> Protein chuyển tiếp Grb2 dùng domain SH2 gắn vào Phospho-Tyrosin trên RTK (hoặc IRS-1) và dùng domain SH3 tuyển mộ yếu tố trao đổi SOS (Son of Sevenless).",
        "<b>Hoạt hóa protein Ras —</b> SOS hoạt động như một GEF thúc đẩy protein G đơn phân tử Ras nhả GDP nạp GTP chuyển sang dạng Ras-GTP hoạt động.",
        "<b>Kích hoạt Raf (MAPKKK) —</b> Ras-GTP tuyển mộ và kích hoạt Serin/Threonin kinase Raf (MAP kinase kinase kinase) tại màng sinh chất.",
        "<b>Kích hoạt MEK (MAPKK) —</b> Raf phosphoryl hóa hoạt hóa enzym kép MEK 1/2 (MAP kinase kinase).",
        "<b>Kích hoạt ERK 1/2 (MAPK) —</b> MEK phosphoryl hóa cả gốc Threonin và Tyrosin trên enzym ERK 1/2 (Extracellular signal-Regulated Kinase).",
        "<b>Biểu hiện gen phân bào —</b> ERK di chuyển vào nhân tế bào phosphoryl hóa các yếu tố phiên mã c-Fos, c-Jun, c-Myc kích thích chu kỳ tế bào và tăng sinh mô."
    ],
    "Đột biến hoạt hóa gen Ras (như K-Ras) bị khóa chết ở trạng thái gắn GTP luôn luôn bật là một trong những nguyên nhân khởi phát phổ biến nhất trong ung thư đại trực tràng và ung thư tụy."
))

cards.append(make_card(
    "HS13-B3-10",
    "Họ Thụ thể Tuyển mộ Kinase Bào tương: Con đường JAK / STAT",
    "CON ĐƯỜNG JAK / STAT",
    "Đặc điểm các thụ thể không có kinase nội tại và cơ chế kích hoạt con đường JAK/STAT?",
    [
        "<b>Đặc điểm thụ thể —</b> Các chuỗi protein xuyên màng đơn độc không có hoạt tính enzym kinase nội tại, nhưng gắn sẵn enzym Tyrosine Kinase tế bào thuộc họ Janus Kinase (JAK1, JAK2, JAK3, Tyk2).",
        "<b>Danh mục hormon và cytokine qua JAK/STAT —</b> Growth Hormone (GH), Prolactin (PRL), Erythropoietin (EPO), Leptin, Interferon (IFN-alpha, beta, gamma), Interleukin (IL-2, IL-6).",
        "<b>Dimer hóa và tự phosphoryl hóa JAK —</b> Khi hormon gắn vào, 2 thụ thể kéo lại gần nhau tạo dimer; 2 phân tử JAK đi kèm áp sát tự phosphoryl hóa chéo (trans-phosphorylation) kích hoạt lẫn nhau.",
        "<b>Tạo điểm neo giữ cho STAT —</b> JAK hoạt hóa phosphoryl hóa các gốc Tyrosin trên đuôi bào tương của thụ thể, tạo vị trí neo cho các yếu tố phiên mã STAT (Signal Transducers and Activators of Transcription) qua domain SH2 của STAT."
    ],
    "Janus Kinase được đặt tên theo thần La Mã Janus (vị thần hai mặt) vì phân tử enzym này sở hữu hai domain giống kinase đối xứng nhau."
))

cards.append(make_card(
    "HS13-B3-11",
    "Cơ chế Chuyển nhân của Phức hợp STAT Dimer và Điều hòa Gen",
    "CHUYỂN NHÂN STAT",
    "Các bước tiếp theo từ lúc STAT bị phosphoryl hóa đến khi hoàn tất kích hoạt phiên mã gen mục tiêu?",
    [
        "<b>Phosphoryl hóa STAT bởi JAK —</b> Sau khi neo vào thụ thể, enzym JAK phosphoryl hóa một gốc Tyrosin đặc hiệu ở đầu C của phân tử STAT.",
        "<b>Tách rời và nhị hợp hóa STAT —</b> STAT bị phosphoryl hóa tách rời khỏi thụ thể; hai phân tử Phospho-STAT tương tác qua lại domain SH2 tạo thành phức hợp STAT dimer (đồng nhị tụ hoặc dị nhị tụ).",
        "<b>Bộc lộ tín hiệu định vị nhân (NLS) —</b> Sự tạo dimer bộc lộ trình tự định vị nhân NLS, cho phép phức hợp STAT dimer đi qua phức hợp lỗ màng nhân vào trong nhân.",
        "<b>Gắn trình tự điều hòa DNA —</b> STAT dimer gắn đặc hiệu vào các trình tự điều hòa trên promoter gen mục tiêu (ví dụ GH kích hoạt gan phiên mã gen tổng hợp IGF-1).",
        "<b>Cơ chế phanh dập tắt SOCS —</b> Sản phẩm protein phiên mã bao gồm họ protein SOCS (Suppressor of Cytokine Signaling) quay lại ức chế JAK và thụ thể để hoàn tất chu trình hồi tiếp âm."
    ],
    "Con đường JAK/STAT là lộ trình truyền tin ngắn nhất và trực tiếp nhất từ bề mặt màng tế bào thẳng vào bộ máy phiên mã trong nhân mà không cần qua nhiều tầng kinase trung gian."
))

# ==============================================================================
# SECTION B4: THỤ THỂ NỘI BÀO & SIÊU HỌ THỤ THỂ NHÂN (11 thẻ: HS13-B4-01 -> HS13-B4-11)
# ==============================================================================

cards.append(make_card(
    "HS13-B4-01",
    "Siêu họ Thụ thể Nhân (Nuclear Receptor Superfamily)",
    "ĐẠI CƯƠNG THỤ THỂ NHÂN",
    "Định nghĩa, danh mục các phối tử điển hình và vai trò sinh học của siêu họ thụ thể nội bào / nhân?",
    [
        "<b>Định nghĩa phân tử —</b> Là một siêu họ các yếu tố phiên mã nội bào hoạt hóa phụ thuộc phối tử (ligand-activated transcription factors).",
        "<b>Các phối tử điển hình —</b> Hormon Steroid (Cortisol, Aldosteron, Testosteron, Estradiol, Progesteron), Hormon Tuyến giáp (T3, T4), Calcitriol (1,25-(OH)2-D3), Acid Retinoic (dẫn xuất vitamin A).",
        "<b>Vượt màng tế bào —</b> Do bản chất kỵ nước tan tốt trong lipid, các phối tử này dễ dàng khuếch tán tự do trực tiếp qua lớp kép phospholipid màng sinh chất.",
        "<b>Đích tác động tối thượng —</b> Tương tác trực tiếp với bộ máy phiên mã của nhân tế bào, điều hòa tốc độ biểu hiện của hàng trăm đến hàng ngàn gen mục tiêu.",
        "<b>Đặc tính đáp ứng —</b> Khởi phát chậm sau vài giờ đến vài ngày (thời gian sao chép mRNA và dịch mã protein mới), nhưng duy trì hiệu ứng sinh học bền bỉ lâu dài."
    ],
    "Siêu họ thụ thể nhân bao gồm khoảng 48 thụ thể ở người, kiểm soát toàn diện các quá trình phát triển phôi, biệt hóa tế bào, chuyển hóa nội môi và sinh sản."
))

cards.append(make_card(
    "HS13-B4-02",
    "Cấu trúc 5 Miền Chức năng (Domains A - E) của Thụ thể Nhân",
    "CẤU TRÚC MIỀN THỤ THỂ",
    "Cấu trúc không gian module hóa gồm 5 miền chức năng (A đến E) của các thụ thể nhân?",
    [
        "<b>Miền A/B (Đầu tận N / NTD) —</b> Chứa vùng hoạt hóa phiên mã độc lập phối tử AF-1 (Activation Function-1), có cấu trúc biến thiên cao nhất, tương tác đặc thù theo từng loại mô.",
        "<b>Miền C (Miền gắn DNA - DBD) —</b> Miền bảo tồn tiến hóa cao nhất, chứa 2 cấu trúc ngón tay kẽm (Zinc Fingers) khớp chính xác vào rãnh lớn của chuỗi xoắn kép DNA.",
        "<b>Miền D (Vùng bản lề - Hinge region) —</b> Đoạn peptide linh hoạt kết nối DBD và LBD, chứa trình tự tín hiệu định vị nhân (NLS - Nuclear Localization Signal).",
        "<b>Miền E (Miền gắn phối tử - LBD) —</b> Nằm ở phía đầu C, tạo túi kỵ nước gắn đặc hiệu với hormon; chứa vùng hoạt hóa phụ thuộc phối tử AF-2 và bề mặt tuyển mộ Coactivator / Corepressor.",
        "<b>Miền F (Đầu tận C) —</b> Đoạn peptide đuôi ngắn ở một số thụ thể, tham gia điều biến cấu hình không gian."
    ],
    "Cấu trúc module hóa này cho phép các nhà sinh học phân tử tạo ra các thụ thể dung hợp nhân tạo (chimeric receptors) bằng cách ghép DBD của thụ thể này với LBD của thụ thể khác."
))

cards.append(make_card(
    "HS13-B4-03",
    "Cấu trúc Ngón tay Kẽm (Zinc Finger) trong Miền DBD",
    "NGÓN TAY KẼM",
    "Cấu tạo hóa học và nguyên lý tương tác với chuỗi xoắn kép DNA của cấu trúc ngón tay kẽm?",
    [
        "<b>Phối trí nguyên tử Kẽm —</b> Mỗi ngón tay kẽm được tạo thành bởi 1 nguyên tử kẽm (Zn2+) phối trí tứ diện bền vững với 4 gốc acid amin Cystein (C4-type zinc finger).",
        "<b>Số lượng trên mỗi thụ thể —</b> Miền DBD của mỗi thụ thể nhân chứa chính xác 2 cấu trúc ngón tay kẽm độc lập.",
        "<b>Ngón tay kẽm thứ nhất (Nhận diện base) —</b> Chứa đoạn xoắn alpha 'P-box' (Recognition helix) cắm khít trực tiếp vào rãnh lớn (major groove) của DNA, nhận diện các cặp base đặc hiệu.",
        "<b>Ngón tay kẽm thứ hai (Tạo dimer) —</b> Chứa quai 'D-box' tham gia vào sự tương tác tiếp xúc giữa hai phân tử thụ thể khi tạo phức hợp nhị tụ (dimerization) trên DNA.",
        "<b>Ý nghĩa sinh học —</b> Đảm bảo độ đặc hiệu tuyệt đối: mỗi loại thụ thể chỉ gắn đúng vào đoạn trình tự HRE của các gen mà nó có nhiệm vụ chỉ huy."
    ],
    "Kẽm (Zinc) là nguyên tố vi lượng tối cần thiết cho cấu trúc bậc 3 này; thiếu kẽm nặng có thể làm biến dạng miền DBD và rối loạn biểu hiện gen phụ thuộc hormon steroid."
))

cards.append(make_card(
    "HS13-B4-04",
    "Vai trò Protein Sốc Nhiệt HSP90 và Trạng thái Nghỉ của Thụ thể Steroid",
    "CHAPERONE HSP90",
    "Vị trí cư trú và chức năng của phức hợp chaperone HSP90 đối với thụ thể hormon steroid ở trạng thái nghỉ?",
    [
        "<b>Vị trí phân bố nghỉ —</b> Nằm trong dịch bào tương (Cytosol) của tế bào đích khi chưa có mặt phân tử hormon.",
        "<b>Liên kết phức hợp chaperone —</b> Thụ thể (như GR, MR, AR) gắn chặt với phức hợp protein sốc nhiệt gồm Hsp90, Hsp70 và immunophilin FKBP51/52.",
        "<b>Bảo vệ cấu hình gắn phối tử —</b> Hsp90 giữ túi LBD của thụ thể ở trạng thái mở tối ưu để sẵn sàng đón nhận phân tử hormon khuếch tán vào.",
        "<b>Che lấp các tín hiệu chức năng —</b> Phức hợp Hsp90 che lấp hoàn toàn miền gắn DNA (DBD) và trình tự định vị nhân (NLS), ngăn chặn thụ thể di chuyển sớm vào nhân.",
        "<b>Giải phóng khi có hormon —</b> Khi hormon steroid gắn vào túi LBD, cấu hình thay đổi làm phức hợp Hsp90 lập tức tách rời hoàn toàn khỏi thụ thể."
    ],
    "Hsp90 đóng vai trò như chiếc vỏ bọc an toàn vừa bảo vệ cấu hình vừa 'khóa chốt' không cho thụ thể steroid xâm nhập vào nhân khi chưa được kích hoạt."
))

cards.append(make_card(
    "HS13-B4-05",
    "Trình tự Định vị Nhân (NLS) và Sự Chuyển dịch vào Nhân",
    "CHUYỂN NHÂN NLS",
    "Cơ chế bộc lộ tín hiệu NLS và quá trình vận chuyển phức hợp Hormon - Thụ thể qua màng nhân?",
    [
        "<b>Bản chất NLS —</b> Nuclear Localization Signal là một đoạn peptide ngắn giàu các acid amin tích điện dương (Lysin và Arginin) nằm ở vùng bản lề của thụ thể.",
        "<b>Bộc lộ NLS —</b> Sự tách rời của Hsp90 cùng với sự tạo homodimer làm bộc lộ hoàn toàn trình tự NLS ra bề mặt ngoài.",
        "<b>Gắn protein vận chuyển Importin —</b> Trình tự NLS được nhận diện và gắn kết đặc hiệu bởi phức hợp protein vận chuyển nhân Importin-alpha và Importin-beta.",
        "<b>Vượt qua phức hợp lỗ màng nhân (NPC) —</b> Importin hộ tống phức hợp Hormon - Thụ thể đi qua các protein Nucleoporin của lỗ màng nhân vào sâu trong chất nhân.",
        "<b>Phân ly bởi Ran-GTP —</b> Trong chất nhân, protein G nhỏ Ran-GTP gắn vào Importin giải phóng phức hợp Hormon - Thụ thể tự do tiến tới liên kết với sợi chromatin."
    ],
    "Đây là cơ chế vận chuyển nhân chủ động phụ thuộc năng lượng, đảm bảo 100% thụ thể sau khi gắn hormon steroid được tập trung trọn vẹn vào nhân tế bào."
))

cards.append(make_card(
    "HS13-B4-06",
    "Yếu tố Đáp ứng Hormon (HRE - Hormone Response Element) trên DNA",
    "TRÌNH TỰ HRE",
    "Đặc điểm cấu trúc của các đoạn trình tự HRE trên vùng promoter DNA và cơ chế nhận diện của thụ thể?",
    [
        "<b>Định nghĩa HRE —</b> Là các đoạn trình tự DNA đặc hiệu nằm ở vùng khởi động (promoter) hoặc vùng tăng cường (enhancer) của các gen chịu sự điều hòa bởi hormon.",
        "<b>Cấu trúc Inverted Repeat (Đối xứng đảo ngược / Palindrome) —</b> Điển hình cho thụ thể Steroid Typ I: 2 đoạn lặp lại 6 nucleotide đối xứng nhau qua 3 nucleotide đệm (ví dụ GRE: 5'-GGTACAnnnTGTTCT-3').",
        "<b>Cấu trúc Direct Repeat (Lặp lại cùng chiều) —</b> Điển hình cho thụ thể Typ II (TR, VDR, RAR): 2 đoạn lặp lại trực tiếp cùng hướng phân cách nhau từ 1 đến 5 nucleotide.",
        "<b>Sự khớp đôi ngón tay kẽm —</b> Mỗi monome trong dimer thụ thể cắm một ngón tay kẽm vào một nửa vị trí nhận diện (half-site) của đoạn HRE.",
        "<b>Điều biến ái lực —</b> Trình tự HRE quyết định độ bền liên kết và góc bẻ cong DNA, ảnh hưởng trực tiếp đến hiệu suất tuyển mộ bộ máy phiên mã."
    ],
    "Sự khác biệt về khoảng cách đệm giữa các nửa vị trí nhận diện (quy tắc 1 - 5 nucleotide) là chìa khóa giúp các thụ thể nhân khác nhau phân biệt chính xác gen đích của mình."
))

cards.append(make_card(
    "HS13-B4-07",
    "Tuyển mộ Coactivator / Corepressor và Tái cấu trúc Chromatin (HAT vs HDAC)",
    "ĐIỀU HÒA PHIÊN MÃ",
    "Cơ chế thụ thể nhân điều biến chất nhiễm sắc thông qua tuyển mộ protein đồng hoạt hóa (Coactivator) và đồng ức chế (Corepressor)?",
    [
        "<b>Tuyển mộ Coactivator (Khi có hormon) —</b> Vùng AF-2 của thụ thể thay đổi cấu hình tạo rãnh kẹp lấy mô-típ LXXLL của các protein đồng hoạt hóa như p300/CBP, SRC-1.",
        "<b>Hoạt tính Histone Acetyltransferase (HAT) —</b> Coactivator mang hoạt tính HAT gắn nhóm acetyl vào Lysin trên đuôi Histone, trung hòa điện tích dương làm lỏng lẻo sợi chromatin.",
        "<b>Khởi động phiên mã mạnh mẽ —</b> Chromatin tháo xoắn bộc lộ DNA, tạo điều kiện cho RNA Polymerase II và các yếu tố phiên mã chung bám vào khởi động tổng hợp mRNA.",
        "<b>Tuyển mộ Corepressor (Khi vắng mặt hormon ở thụ thể Typ II) —</b> Thụ thể gắn với các protein đồng ức chế như NCoR và SMRT.",
        "<b>Hoạt tính Histone Deacetylase (HDAC) —</b> Corepressor tuyển mộ HDAC gỡ bỏ nhóm acetyl trên Histone, làm chromatin cuộn xoắn chặt chẽ, đóng băng hoàn toàn quá trình phiên mã."
    ],
    "Cơ chế biểu sinh (epigenetics) thông qua cân bằng acetyl hóa/khử acetyl hóa histone là trái tim điều khiển bật/tắt gen của siêu họ thụ thể nhân."
))

cards.append(make_card(
    "HS13-B4-08",
    "So sánh Thụ thể Steroid (Typ I) vs Thụ thể Hormon Giáp TR (Typ II)",
    "ĐỐI CHIẾU TYP I VS TYP II",
    "Sự khác biệt căn bản về vị trí nghỉ, trạng thái liên kết DNA và đối tác nhị hợp giữa Thụ thể Typ I và Typ II?",
    [
        "<b>Đại diện điển hình —</b> Typ I gồm thụ thể Steroid (GR, MR, AR, PR, ER); Typ II gồm thụ thể Hormon Giáp (TR), Calcitriol (VDR), Acid Retinoic (RAR).",
        "<b>Vị trí phân bố khi nghỉ —</b> Typ I nằm trong dịch bào tương gắn phức hợp Hsp90; Typ II nằm thường trực bên trong nhân tế bào ngay cả khi không có hormon.",
        "<b>Trình diện trên DNA —</b> Typ I không gắn DNA khi chưa có hormon; Typ II liên kết sẵn trên DNA ngay cả khi vắng mặt hormon (gắn kèm Corepressor để kìm hãm phiên mã nền).",
        "<b>Dạng nhị hợp hóa —</b> Typ I tạo Đồng nhị tụ (Homodimer) như GR-GR, MR-MR; Typ II bắt buộc tạo Dị nhị tụ (Heterodimer) với thụ thể RXR (Retinoid X Receptor: TR-RXR, VDR-RXR).",
        "<b>Hành vi khi có hormon —</b> Typ I di chuyển từ bào tương vào nhân; Typ II chỉ thay đổi cấu hình tống xuất Corepressor/HDAC nạp Coactivator/HAT ngay tại chỗ trên DNA."
    ],
    "Thụ thể Hormon Giáp (TR) không bao giờ rời khỏi DNA trong nhân: khi không có T3 nó ức chế gen, khi có T3 nó lập tức biến thành cỗ máy kích hoạt gen bùng nổ."
))

cards.append(make_card(
    "HS13-B4-09",
    "Cơ chế Kháng viêm Mạnh mẽ của Glucocorticoid: Transactivation vs Transrepression",
    "CƠ CHẾ CORTICOID",
    "Hai cơ chế phân tử độc lập giải thích tác dụng tăng đường huyết (Transactivation) và kháng viêm cực mạnh (Transrepression) của Corticoid?",
    [
        "<b>Cơ chế hoạt hóa gen (Transactivation) —</b> Dimer GR-GR gắn vào trình tự GRE trên DNA tuyển mộ Coactivator kích thích phiên mã các gen enzym tân tạo đường (PEPCK, G6Pase) gây tăng đường huyết.",
        "<b>Cơ chế ức chế gen chéo (Transrepression) —</b> Monomer GR tương tác trực tiếp với các yếu tố phiên mã gây viêm then chốt trong tế bào như NF-kB và AP-1.",
        "<b>Khóa hoạt tính NF-kB —</b> Sự bắt cặp trực tiếp này ngăn cản NF-kB gắn vào promoter các gen tiền viêm, chặn đứng sự tổng hợp các Cytokine (IL-1, IL-6, TNF-alpha), enzym COX-2 và iNOS.",
        "<b>Cảm ứng tổng hợp I-kappa-B-alpha —</b> GR kích thích phiên mã gen mã hóa I-kB-alpha, một protein kìm hãm nhốt chặt NF-kB trong bào tương.",
        "<b>Ý nghĩa dược lý —</b> Giải thích tác dụng ức chế miễn dịch và kháng viêm tối cao của thuốc Corticoid (Prednisolon, Dexamethason) trên lâm sàng."
    ],
    "Các nhà nghiên cứu dược lý đang nỗ lực tìm kiếm các chất điều biến chọn lọc thụ thể GR (SEGRMs) chỉ kích hoạt nhánh Transrepression (kháng viêm) mà không kích hoạt nhánh Transactivation (tránh tác dụng phụ tiểu đường, loãng xương)."
))

cards.append(make_card(
    "HS13-B4-10",
    "Thụ thể Estrogen (ER-alpha và ER-beta) và Thuốc SERM",
    "THỤ THỂ ESTROGEN",
    "Đặc tính phân tử của thụ thể Estrogen và cơ chế tác dụng chọn lọc mô của các thuốc SERM (Tamoxifen, Raloxifene)?",
    [
        "<b>Hai đồng phân thụ thể —</b> ER-alpha (chiếm ưu thế ở tử cung, tuyến vú, vùng hạ đồi) và ER-beta (chiếm ưu thế ở buồng trứng, xương, hệ tim mạch).",
        "<b>Cấu hình AF-2 thay đổi theo phối tử —</b> Các phân tử gắn kết khác nhau ép vùng AF-2 gấp cuộn theo các hình thể không gian đặc thù khác biệt.",
        "<b>Bản chất thuốc SERM —</b> Selective Estrogen Receptor Modulators là các chất chủ vận hoặc đối kháng thụ thể estrogen có tính chọn lọc mô.",
        "<b>Cơ chế Tamoxifen tại tuyến vú —</b> Gắn vào ER tại mô vú làm AF-2 tuyển mộ Corepressor → Ức chế phiên mã và chặn đứng sự phân bào của tế bào ung thư vú nhạy cảm nội tiết.",
        "<b>Tác dụng Tamoxifen tại xương và nội mạc tử cung —</b> Hoạt động như chất chủ vận yếu, kích thích bảo tồn mật độ xương nhưng có thể làm tăng nhẹ nguy cơ tăng sinh nội mạc tử cung."
    ],
    "Cơ chế SERM minh họa cho tính mềm dẻo của thụ thể nhân: cấu hình không gian do phối tử áp đặt quyết định thụ thể sẽ tuyển mộ Coactivator hay Corepressor tùy vào bối cảnh protein của từng mô."
))

cards.append(make_card(
    "HS13-B4-11",
    "Tác dụng Ngoài gen Siêu nhanh của Hormon Steroid (Non-genomic Actions)",
    "TÁC DỤNG NGOÀI GEN",
    "Bằng chứng và cơ chế giải thích các tác dụng sinh học xuất hiện trong vài giây đến vài phút của hormon steroid?",
    [
        "<b>Nghịch lý thời gian —</b> Tác dụng qua biểu hiện gen kinh điển cần từ 30 phút đến nhiều giờ, nhưng một số đáp ứng của steroid (như Aldosteron gây co mạch, Estrogen giãn mạch) xuất hiện trong vài chục giây.",
        "<b>Thụ thể Steroid gắn màng (mPR, GPER/GPR30) —</b> Tồn tại các thụ thể steroid nằm ngay trên màng sinh chất thuộc họ GPCR (ví dụ GPER bắt cặp với Gs/Gq).",
        "<b>Thụ thể nhân định vị tại màng —</b> Một tỷ lệ nhỏ thụ thể nhân cổ điển (như ER, PR) được palmitoyl hóa gắn vào các bè lipid (lipid rafts) ở màng tế bào.",
        "<b>Phát động dòng thác kinase —</b> Hormon gắn thụ thể màng kích hoạt nhanh chóng dòng thác PLC/Ca2+, PI3K/Akt hoặc kích thích tế bào nội mô giải phóng khí NO giãn mạch tức thì.",
        "<b>Độc lập với phiên mã —</b> Các tác dụng siêu nhanh này hoàn toàn không bị ức chế bởi các chất ức chế phiên mã như Actinomycin D hay ức chế dịch mã Cycloheximide."
    ],
    "Khái niệm tác dụng ngoài gen (Non-genomic actions) mở rộng hoàn toàn hiểu biết hiện đại: hormon steroid vừa có tác dụng chậm kéo dài qua nhân, vừa có tác dụng nhanh tức thời qua màng."
))

# ==============================================================================
# SECTION B5: TRỤC HẠ ĐỒI - TUYẾN YÊN & CƠ CHẾ ĐIỀU HÒA FEEDBACK (11 thẻ: HS13-B5-01 -> HS13-B5-11)
# ==============================================================================

cards.append(make_card(
    "HS13-B5-01",
    "Trục Hạ đồi - Tuyến yên - Tuyến đích: Khái niệm và Hệ Mạch cửa",
    "ĐẠI CƯƠNG TRỤC NỘI TIẾT",
    "Cấu trúc giải phẫu chức năng và vai trò của hệ tuần hoàn mạch cửa Hạ đồi - Tuyến yên (Hypophyseal Portal System)?",
    [
        "<b>Trung tâm tích hợp cao cấp —</b> Vùng hạ đồi nhận các tín hiệu thần kinh từ não bộ, chuyển đổi thành các tín hiệu thể dịch là các hormon giải phóng (RH) và ức chế (IH).",
        "<b>Cấu trúc hệ mạch cửa hạ đồi —</b> Đám rối mao mạch thứ nhất tại lồi giữa (median eminence) gom vào các tĩnh mạch cửa hạ đồi đi xuống cuống tuyến yên, tỏa thành đám rối mao mạch thứ hai tại thùy trước tuyến yên.",
        "<b>Ưu thế tuần hoàn tại chỗ —</b> Giúp các hormon vùng hạ đồi (nồng độ cực nhỏ) đi thẳng trực tiếp đến các tế bào thùy trước tuyến yên với nồng độ cao mà không bị pha loãng trong tuần hoàn toàn thân.",
        "<b>Đáp ứng chính xác —</b> Tế bào tuyến yên tiếp nhận nồng độ hormon giải phóng đậm đặc để điều biến sự tổng hợp và bài xuất các hormon hướng tuyến (tropic hormones).",
        "<b>Tổn thương đứt cuống tuyến yên —</b> Làm mất tín hiệu hạ đồi: giảm tiết hầu hết hormon tuyến yên trừ Prolactin (tăng vọt do mất tác dụng ức chế thường trực của Dopamine)."
    ],
    "Hệ mạch cửa Hạ đồi - Tuyến yên là cầu nối giải phẫu - sinh lý vi diệu nhất trong cơ thể kết nối trực tiếp hệ thần kinh trung ương với hệ thống nội tiết toàn thân."
))

cards.append(make_card(
    "HS13-B5-02",
    "Hệ thống Hormon Vùng Hạ đồi: Phân loại và Tác dụng",
    "HORMON HẠ ĐỒI",
    "Cấu trúc và tác động đặc hiệu của 6 hormon điều hòa chính do vùng hạ đồi tiết ra?",
    [
        "<b>TRH (Tripeptid: PyroGlu-His-Pro-NH2) —</b> Kích thích tế bào tuyến yên tổng hợp và bài tiết TSH, đồng thời kích thích giải phóng Prolactin.",
        "<b>CRH (Polypeptid 41 acid amin) —</b> Kích thích tế bào tuyến yên tổng hợp tiền chất POMC và bài tiết ACTH cùng beta-endorphin; tăng tiết mạnh khi có stress, hạ đường huyết.",
        "<b>GnRH (Decapeptid 10 acid amin) —</b> Bài tiết dạng xung kích thích thùy trước tuyến yên bài tiết LH và FSH điều hòa sinh dục.",
        "<b>GHRH (44 acid amin) —</b> Kích thích tế bào ưa acid tuyến yên bài tiết Hormon tăng trưởng (GH).",
        "<b>Somatostatin (GHIH, 14 acid amin) —</b> Ức chế mạnh mẽ bài tiết GH và TSH của tuyến yên; ức chế tiết Insulin, Glucagon tại tụy và Gastrin dạ dày.",
        "<b>Dopamine (PIH, dẫn xuất Tyrosin) —</b> Bài tiết liên tục tác động qua thụ thể D2 ức chế bài tiết Prolactin của tuyến yên."
    ],
    "Ngoại trừ Dopamine là dẫn xuất amin, toàn bộ các hormon hạ đồi còn lại đều là các chuỗi peptid ngắn với độ nhạy thụ thể cực cao."
))

cards.append(make_card(
    "HS13-B5-03",
    "Thùy trước Tuyến yên: 3 Nhóm Hormon Cấu trúc và Nguồn gốc POMC",
    "HORMON TUYẾN YÊN TRƯỚC",
    "Đặc điểm cấu trúc của 3 nhóm hormon thùy trước tuyến yên và quá trình cắt tiền chất POMC tạo ACTH?",
    [
        "<b>Nhóm Glycoprotein (TSH, LH, FSH) —</b> Cấu tạo từ 2 tiểu đơn vị: chuỗi alpha hoàn toàn đồng nhất giữa các hormon; chuỗi beta riêng biệt quyết định tính đặc hiệu sinh học và vị trí gắn thụ thể.",
        "<b>Nhóm Somatomammotropin (GH và Prolactin) —</b> Các chuỗi đơn polypeptide (GH: 191 aa, PRL: 199 aa) có cấu trúc xoắn và tính tương đồng trình tự rất cao.",
        "<b>Tiền chất POMC (Pro-opiomelanocortin) —</b> Là một đại phân tử polypeptide tiền thân được cắt bởi enzym Prohormone Convertase 1 (PC1) tại thùy trước tuyến yên.",
        "<b>Các mảnh cắt từ POMC —</b> Tạo ra ACTH (39 acid amin), beta-Lipotropin, beta-Endorphin và các mảnh N-terminal.",
        "<b>Hoạt tính sinh học của ACTH —</b> Chỉ cần đoạn 24 acid amin đầu N (1 - 24) là mang trọn vẹn hoạt tính sinh học kích thích vỏ thượng thận (chế phẩm Synacthen)."
    ],
    "Sự tương đồng về chuỗi alpha giữa TSH, LH, FSH và hCG giải thích vì sao khi phụ nữ có thai nồng độ hCG tăng cực cao có thể kích hoạt nhẹ thụ thể TSH gây cường giáp thoáng qua."
))

cards.append(make_card(
    "HS13-B5-04",
    "Thùy sau Tuyến yên: Nguồn gốc và Hai Hormon Nonapeptid (ADH & Oxytocin)",
    "HORMON TUYẾN YÊN SAU",
    "Nguồn gốc phôi học, quá trình vận chuyển sợi trục và tác dụng của ADH và Oxytocin?",
    [
        "<b>Bản chất mô thần kinh —</b> Thùy sau tuyến yên không tự tổng hợp hormon mà là nơi tích trữ và phóng thích hormon do nhân trên thị và nhân cạnh não thất vùng hạ đồi tổng hợp.",
        "<b>Vận chuyển sợi trục —</b> Hormon đi kèm protein tải chuyên biệt Neurophysin dọc theo các sợi trục thần kinh xuống cúc tận cùng tại thùy sau tuyến yên.",
        "<b>Cấu trúc Nonapeptid —</b> Cả ADH (Vasopressin) và Oxytocin đều gồm 9 acid amin, có 1 cầu disulfua nội chuỗi tạo vòng 6 cạnh, chỉ khác nhau 2 acid amin ở vị trí 3 và 8.",
        "<b>Tác dụng của Oxytocin —</b> Kích thích co bóp mạnh cơ trơn tử cung (chuyển dạ) và co bóp tế bào cơ biểu mô nang tuyến vú (phản xạ tống sữa khi bú).",
        "<b>Tác dụng của ADH (Vasopressin) —</b> Thụ thể V2 ở ống góp thận (qua Gs/cAMP) chuyển kênh Aquaporin-2 ra màng tăng tái hấp thu nước; thụ thể V1 ở cơ trơn mạch máu (qua Gq) gây co mạch nâng huyết áp."
    ],
    "Chỉ khác biệt 2 acid amin nhưng ADH và Oxytocin đảm nhiệm hai sứ mệnh sinh học hoàn toàn khác biệt: một bên điều hòa áp suất thẩm thấu muối nước, một bên điều khiển sinh sản và tình mẫu tử."
))

cards.append(make_card(
    "HS13-B5-05",
    "Cơ chế Feedback Âm tính (Negative Feedback): Vòng Dài, Ngắn và Cực Ngắn",
    "FEEDBACK ÂM TÍNH",
    "Định nghĩa và sự phân biệt giữa 3 cấp độ vòng điều hòa ngược âm tính trong hệ nội tiết?",
    [
        "<b>Nguyên lý Feedback âm tính —</b> Khi nồng độ hormon tuyến đích tăng cao trong máu, nó quay lại ức chế sự bài tiết của tầng chỉ huy cấp cao hơn nhằm đưa nồng độ trở về khoảng bình thường.",
        "<b>Vòng dài (Long-loop feedback) —</b> Hormon tuyến đích (như Cortisol, T3/T4, Testosteron, Estradiol) tác động ngược lên ức chế cả vùng hạ đồi (giảm tiết CRH, TRH, GnRH) VÀ thùy trước tuyến yên (giảm tiết ACTH, TSH, LH/FSH).",
        "<b>Vòng ngắn (Short-loop feedback) —</b> Hormon tuyến yên (như ACTH, TSH, GH, LH) tác động ngược trực tiếp lên vùng hạ đồi làm giảm tiết hormon giải phóng tương ứng.",
        "<b>Vòng cực ngắn (Ultra-short-loop feedback) —</b> Hormon giải phóng vùng hạ đồi (như GnRH, CRH) tự tác động lên các neuron lân cận của chính vùng hạ đồi để ức chế sự bài xuất tiếp theo của chính nó.",
        "<b>Ý nghĩa hằng định nội môi —</b> Ngăn ngừa tình trạng hoạt động quá mức hoặc tích lũy hormon độc hại, duy trì nồng độ hormon trong máu ở giới hạn sinh lý cực kỳ ổn định."
    ],
    "Cơ chế điều hòa ngược âm tính vòng dài là quy luật chủ đạo chi phối hơn 95% hoạt động của toàn bộ mạng lưới nội tiết trong cơ thể người."
))

cards.append(make_card(
    "HS13-B5-06",
    "Cơ chế Feedback Dương tính (Positive Feedback): Đỉnh LH và Oxytocin",
    "FEEDBACK DƯƠNG TÍNH",
    "Bản chất của phản hồi dương tính và cơ chế phân tử của 2 ví dụ sinh lý hiếm hoi: Đỉnh LH và phản xạ Ferguson?",
    [
        "<b>Bản chất sinh lý —</b> Là hiện tượng sản phẩm bài tiết quay lại kích thích làm tăng cường mạnh mẽ hơn nữa sự bài tiết của tầng chỉ huy, tạo ra một vụ nổ sinh học tự khuếch đại có giới hạn thời gian rõ rệt.",
        "<b>Đỉnh phóng noãn LH (LH Surge) —</b> Cuối pha nang trứng, nang de Graaf chín tiết Estradiol đạt ngưỡng cực cao (>200 pg/mL duy trì >36 - 48h) đảo ngược tác dụng thành kích thích hạ đồi tăng tiết xung GnRH và tuyến yên tăng tiết ồ ạt LH gây phóng noãn.",
        "<b>Phản xạ Ferguson của Oxytocin —</b> Đầu thai nhi tỳ vào cổ tử cung phát xung thần kinh lên hạ đồi kích thích bài tiết Oxytocin → Oxytocin làm cơ tử cung co bóp mạnh hơn → Thai đẩy tỳ mạnh hơn → Kích thích tiết nhiều Oxytocin hơn nữa.",
        "<b>Điểm kết thúc tự nhiên —</b> Vòng lặp dừng lại hoàn toàn khi mục tiêu sinh học được hoàn tất (trứng được giải phóng khỏi nang, thai nhi được tống xuất hoàn toàn ra ngoài).",
        "<b>Khác biệt với bệnh lý —</b> Positive feedback sinh lý luôn có điểm dừng sinh học xác định; nếu không có điểm dừng nó sẽ biến thành vòng xoắn bệnh lý nguy hiểm."
    ],
    "Phản hồi dương tính sinh lý là giải pháp tiến hóa hoàn hảo để cơ thể thực hiện các biến cố sống còn đòi hỏi lực kích hoạt cực đại trong một thời khắc ngắn hạn."
))

cards.append(make_card(
    "HS13-B5-07",
    "Trục Hạ đồi - Tuyến yên - Vỏ Thượng Thận (HPA Axis)",
    "TRỤC HPA",
    "Động học dòng chảy tín hiệu của trục HPA và cơ chế kiểm soát tiết Cortisol theo stress và nhịp sinh học?",
    [
        "<b>Tín hiệu khởi phát —</b> CRH từ nhân cạnh não thất vùng hạ đồi bài tiết vào hệ mạch cửa theo nhịp ngày - đêm và đáp ứng với các kích thích stress thể chất, tâm lý, nhiễm trùng, hạ đường huyết.",
        "<b>Kích hoạt tuyến yên —</b> CRH gắn thụ thể GPCR (Gs) trên tế bào ưa base thùy trước tuyến yên kích thích phân cắt POMC giải phóng ACTH vào tuần hoàn.",
        "<b>Tác động tại vỏ thượng thận —</b> ACTH gắn thụ thể MC2R (GPCR/Gs/cAMP) tại lớp bó và lớp lưới kích hoạt vận chuyển cholesterol qua protein StAR và enzym CYP11A1 để tổng hợp và bài tiết Cortisol.",
        "<b>Vòng ức chế ngược —</b> Cortisol tự do trong máu khuếch tán vào tế bào tuyến yên và hạ đồi gắn thụ thể GR, ức chế phiên mã gen POMC và gen CRH.",
        "<b>Hậu quả khi dùng thuốc Corticoid ngoại sinh kéo dài —</b> Nồng độ corticoid cao liên tục ức chế mạn tính trục HPA làm tuyến yên ngừng tiết ACTH, dẫn đến teo tế bào vỏ thượng thận hai bên (suy thượng thận thứ phát do thuốc khi ngừng đột ngột)."
    ],
    "Trục HPA là trục sinh tồn cốt tử giúp cơ thể chống đỡ stress; lạm dụng thuốc Corticoid ngoại sinh là nguyên nhân hàng đầu gây ức chế và làm suy kiệt trục này trên lâm sàng."
))

cards.append(make_card(
    "HS13-B5-08",
    "Trục Hạ đồi - Tuyến yên - Tuyến Giáp (HPT Axis)",
    "TRỤC HPT",
    "Dòng chảy tín hiệu của trục HPT, cơ chế điều hòa tiết T3/T4 và sự tương tác enzym Deiodinase tại tuyến yên?",
    [
        "<b>Khởi phát từ hạ đồi —</b> TRH được giải phóng từ hạ đồi kích thích tế bào ưa kiềm tuyến yên qua hệ Gq/PLC/Ca2+ tổng hợp và bài xuất hormon TSH.",
        "<b>Tác động tại tuyến giáp —</b> TSH gắn thụ thể TSHR (GPCR bắt cặp Gs) trên màng đáy tế bào nang giáp làm tăng cAMP, kích thích toàn bộ 4 giai đoạn bắt giữ iod, hữu cơ hóa, trùng ngưng và giải phóng T3, T4.",
        "<b>Feedback ngược âm tính —</b> Nồng độ FT4 và FT3 trong máu quay lại ức chế tế bào tuyến yên làm giảm tiết TSH và ức chế hạ đồi giảm tiết TRH.",
        "<b>Vai trò enzym Deiodinase typ 2 (D2) tại tuyến yên —</b> Tế bào tuyến yên hấp thu T4 từ máu và nhờ enzym D2 nội bào khử iod chuyển T4 thành T3 nội bào; chính T3 nội bào này gắn thụ thể TR-beta ức chế trực tiếp phiên mã gen chuỗi alpha và beta của TSH.",
        "<b>Độ nhạy logarit - tuyến tính —</b> TSH có mối liên hệ logarit nghịch đảo cực nhạy với FT4: một sự thay đổi rất nhỏ của FT4 sẽ dẫn đến sự biến thiên gấp hàng chục lần của nồng độ TSH."
    ],
    "Nhờ mối quan hệ logarit cực nhạy này, định lượng TSH huyết tương là xét nghiệm nhạy cảm nhất và xuất sắc nhất để phát hiện rối loạn chức năng tuyến giáp ngay từ giai đoạn dưới lâm sàng."
))

cards.append(make_card(
    "HS13-B5-09",
    "Trục Hạ đồi - Tuyến yên - Tuyến Sinh Dục (HPG Axis)",
    "TRỤC HPG",
    "Cơ chế điều hòa nhịp xung của GnRH, vai trò phân chia của LH/FSH và cơ chế feedback của Steroid sinh dục cùng Inhibin?",
    [
        "<b>Nhịp xung bắt buộc của GnRH —</b> Vùng hạ đồi phát xung GnRH mỗi 90 - 120 phút; nhịp xung chậm ưu tiên kích thích bài tiết FSH, nhịp xung nhanh ưu tiên kích thích bài tiết LH.",
        "<b>Tác động tại Tinh hoàn (Nam) —</b> LH kích thích tế bào kẽ Leydig tổng hợp Testosteron; FSH kích thích tế bào Sertoli hỗ trợ sinh tinh và bài tiết protein kết hợp androgen (ABP) cùng peptid Inhibin B.",
        "<b>Tác động tại Buồng trứng (Nữ) —</b> LH kích thích tế bào vỏ tổng hợp Androgen; FSH kích thích tế bào hạt thơm hóa androgen thành Estradiol và bài tiết Inhibin B.",
        "<b>Feedback âm tính của Steroid sinh dục —</b> Testosteron (ở nam) và Progesteron/Estradiol (ở nữ) ức chế ngược lên hạ đồi (giảm xung GnRH) và tuyến yên (giảm tiết LH/FSH).",
        "<b>Vai trò đặc hiệu của Inhibin B —</b> Được tiết từ tế bào Sertoli hoặc tế bào hạt, quay lại tuần hoàn ức chế chọn lọc tuyệt đối sự bài tiết FSH của tuyến yên mà không ảnh hưởng đến LH."
    ],
    "Cơ chế điều hòa chọn lọc của Inhibin cho phép cơ thể kiểm soát độc lập quá trình sinh tinh/phát triển nang trứng (qua FSH) tách biệt với quá trình sản xuất hormon steroid (qua LH)."
))

cards.append(make_card(
    "HS13-B5-10",
    "Trục Hormon Tăng Trưởng (GHRH / SS - GH - IGF-1)",
    "TRỤC GH - IGF-1",
    "Sự chỉ huy đối kháng kép tại hạ đồi và vai trò chuyển tiếp của IGF-1 gan trong trục phát triển thể chất?",
    [
        "<b>Kiểm soát đối kháng kép tại hạ đồi —</b> GHRH kích thích tiết GH, trong khi Somatostatin (SS) ức chế tiết GH; cân bằng giữa hai tín hiệu này định hình các đợt phát xung GH ban đêm.",
        "<b>Tác động trực tiếp của GH —</b> GH gắn thụ thể qua con đường JAK2/STAT5, gây đề kháng insulin (chống thu nạp glucose vào cơ), tăng ly giải mỡ giải phóng acid béo tự do để bảo tồn glucose cho não.",
        "<b>Tác động gián tiếp qua IGF-1 —</b> GH kích thích tế bào gan tổng hợp và bài xuất yếu tố tăng trưởng giống insulin-1 (IGF-1 / Somatomedin C) vào máu.",
        "<b>Tác dụng tăng trưởng của IGF-1 —</b> IGF-1 gắn thụ thể RTK kích thích phân bào, phát triển mô sụn, cốt hóa xương dài và tăng sinh khối cơ vân ở trẻ em và thanh thiếu niên.",
        "<b>Feedback ngược âm tính —</b> IGF-1 ức chế tế bào tuyến yên giảm tiết GH, đồng thời kích thích vùng hạ đồi tăng tiết Somatostatin để phanh hãm GH."
    ],
    "Vì GH bài tiết theo từng nhịp xung ngắn ngắt quãng (nửa đời t1/2 chỉ 20 phút), định lượng IGF-1 huyết tương (nồng độ ổn định suốt ngày) là tiêu chuẩn vàng sinh hóa để đánh giá sự thừa hoặc thiếu GH mạn tính."
))

cards.append(make_card(
    "HS13-B5-11",
    "Ứng dụng Phân biệt Suy/Cường Tuyến: Nguyên phát vs Thứ phát",
    "CHẨN ĐOÁN PHÂN BIỆT TRỤC",
    "Quy luật logic phân tích cặp xét nghiệm Hormon Tuyến yên và Tuyến đích để phân tầng vị trí tổn thương nguyên phát vs thứ phát?",
    [
        "<b>Quy tắc lệch chiều (Nguyên phát tại tuyến đích) —</b> Tổn thương nằm tại chính tuyến đích (tuyến giáp, thượng thận, buồng trứng/tinh hoàn); hormon tuyến đích và hormon tuyến yên biến thiên NGƯỢC CHIỀU nhau.",
        "<b>Ví dụ Nguyên phát —</b> Suy giáp nguyên phát: FT4 giảm → Mất ức chế ngược → TSH tăng rất cao; Cường giáp nguyên phát (Basedow): FT4 tăng vọt → Ức chế ngược → TSH bị triệt tiêu (<0,01 µIU/mL).",
        "<b>Quy tắc cùng chiều (Thứ phát tại tuyến yên hoặc vùng hạ đồi) —</b> Tổn thương nằm tại tuyến chỉ huy cấp trên (tuyến yên hoặc hạ đồi); hormon tuyến đích và hormon tuyến yên biến thiên CÙNG CHIỀU nhau.",
        "<b>Ví dụ Thứ phát —</b> Suy thượng thận thứ phát (do u tuyến yên hoặc dùng corticoid kéo dài): ACTH giảm/bình thường thấp → Cortisol máu giảm thấp; U tuyến yên tiết ACTH (Bệnh Cushing): ACTH tăng → Kích thích Cortisol tăng vọt.",
        "<b>Ý nghĩa lâm sàng sống còn —</b> Giúp bác sĩ định vị chính xác tổn thương tại tuyến nội tiết ngoại vi hay tại não bộ để chỉ định chụp chiếu đúng cơ quan đích."
    ],
    "Đây là thuật toán tư duy nội tiết căn bản và mạnh mẽ nhất: Lệch chiều = Tại tuyến đích (Nguyên phát); Cùng chiều = Tại tuyến yên/hạ đồi (Thứ phát)."
))

# ==============================================================================
# SECTION B6: HÓA SINH HORMON TUYẾN GIÁP, TỦY & VỎ THƯỢNG THẬN (13 thẻ: HS13-B6-01 -> HS13-B6-13)
# ==============================================================================

cards.append(make_card(
    "HS13-B6-01",
    "Bơm Bắt giữ Iod NIS (Na+/I- Symporter) và Điểm Can thiệp Dược lý",
    "BƠM IOD NIS",
    "Cơ chế vận chuyển chủ động của bơm NIS tại tế bào nang giáp và các chất ức chế cạnh tranh?",
    [
        "<b>Bản chất phân tử NIS —</b> Kênh đồng vận chuyển Natri - Iodua (Sodium-Iodide Symporter) định vị tại màng đáy của tế bào nang giáp.",
        "<b>Cơ chế năng lượng thứ phát —</b> Vận chuyển đồng thời 2 ion Na+ cùng chiều với 1 ion I- vào tế bào, sử dụng năng lượng gradient nồng độ Na+ do bơm Na+/K+-ATPase duy trì.",
        "<b>Hệ số cô đặc —</b> Tích lũy Iodua nội bào cao gấp 20 đến 50 lần nồng độ trong huyết tương (khi bị TSH kích thích có thể vọt lên trên 100 lần).",
        "<b>Kênh Pendrin ở màng đỉnh —</b> Vận chuyển ion I- từ bào tương qua màng đỉnh vào trong lòng lòng chất keo nang giáp.",
        "<b>Ức chế dược lý cạnh tranh —</b> Các anion có kích thước bán kính ion tương đương như Perchlorate (ClO4-) và Thiocyanate (SCN-) ức chế cạnh tranh bơm NIS, ngăn cản sự thu nạp Iod vào tuyến giáp."
    ],
    "Bơm NIS là cửa ngõ đầu tiên và bắt buộc của toàn bộ chu trình tổng hợp hormon giáp; đột biến gen NIS gây suy giáp bẩm sinh do mất khả năng cô đặc iod."
))

cards.append(make_card(
    "HS13-B6-02",
    "Oxy hóa và Gắn Iod vào Thyroglobulin bởi Thyroid Peroxidase (TPO)",
    "ENZYM TPO VÀ HỮU CƠ HÓA",
    "Vai trò xúc tác trung tâm của enzym Thyroid Peroxidase (TPO) và cơ chế thuốc kháng giáp tổng hợp?",
    [
        "<b>Vị trí định vị TPO —</b> Là một enzym gắn màng nằm ở bề mặt tiếp xúc màng đỉnh giữa tế bào nang giáp và lòng dịch keo.",
        "<b>Cung cấp nguồn oxy hóa H2O2 —</b> Enzym NADPH Oxidase kép (DUOX2) ở màng đỉnh sản xuất liên tục phân tử H2O2 để làm chất nhận electron cho TPO.",
        "<b>Oxy hóa ion I- —</b> TPO oxy hóa ion Iodua (I-) thành dạng Iod nguyên tử hoạt động (I0 hoặc I+).",
        "<b>Hữu cơ hóa gốc Tyrosyl trên Thyroglobulin —</b> TPO gắn nhanh chóng nguyên tử Iod vào vị trí carbon số 3 và số 5 của các gốc L-Tyrosin trên chuỗi Thyroglobulin tạo ra MIT (3-Monoiodotyrosin) và DIT (3,5-Diiodotyrosin).",
        "<b>Ức chế bởi thuốc kháng giáp tổng hợp —</b> Thionamide (Methimazole, Propylthiouracil - PTU) ức chế cạnh tranh trung tâm hoạt động của TPO, chặn đứng quá trình gắn iod và phản ứng ngưng tụ."
    ],
    "TPO là enzym chìa khóa quyết định toàn bộ quá trình hữu cơ hóa Iod; kháng thể kháng TPO (anti-TPO) là dấu ấn sinh học hàng đầu trong bệnh viêm tuyến giáp tự miễn Hashimoto."
))

cards.append(make_card(
    "HS13-B6-03",
    "Phản ứng Trùng ngưng Ghép đôi (Coupling) và Tích trữ Hormon Giáp",
    "TRÙNG NGƯNG TẠO T3 VÀ T4",
    "Cơ chế ghép đôi các gốc MIT, DIT trên khung Thyroglobulin và đặc điểm kho dự trữ chất keo?",
    [
        "<b>Ghép đôi tạo T4 (Thyroxin) —</b> TPO xúc tác phản ứng ngưng tụ giữa hai phân tử DIT liền kề trên cùng một phân tử Thyroglobulin: DIT + DIT → T4 (Tetraiodothyronin) + Alanin.",
        "<b>Ghép đôi tạo T3 (Triiodothyronin) —</b> TPO xúc tác phản ứng ngưng tụ giữa một phân tử MIT và một phân tử DIT: MIT + DIT → T3 (Triiodothyronin) + Alanin.",
        "<b>Tỷ lệ sản phẩm —</b> Phản ứng ưu tiên tạo T4 với tỷ lệ vượt trội: khoảng 10 - 15 phân tử T4 cho mỗi 1 phân tử T3 trên một phân tử Thyroglobulin.",
        "<b>Tích trữ ngoại bào trong lòng nang —</b> Thyroglobulin gắn T3/T4 được lưu trữ dưới dạng chất keo keo đặc trong lòng nang giáp.",
        "<b>Dung lượng dự trữ khổng lồ —</b> Lượng hormon giáp tích trữ trong lòng nang đủ đáp ứng nhu cầu sinh lý của cơ thể trong 2 đến 3 tháng mà không sợ thiếu hụt cấp tính."
    ],
    "Tuyến giáp là tuyến nội tiết duy nhất trong cơ thể tích trữ lượng hormon lớn bên ngoài tế bào (trong lòng dịch keo nang tuyến) với dung lượng dự trữ tính bằng tháng."
))

cards.append(make_card(
    "HS13-B6-04",
    "Hệ thống Enzym Deiodinase (D1, D2, D3) và Chuyển hóa T4 thành T3 Ngoại vi",
    "CHUYỂN HÓA DEIODINASE",
    "Đặc tính phân bố mô và chức năng điều hòa của 3 enzym Deiodinase chứa Selen trong cơ thể?",
    [
        "<b>Bản chất selenoprotein —</b> Cả 3 enzym Deiodinase đều chứa acid amin hiếm Selenocystein tại trung tâm hoạt động; thiếu hụt nguyên tố Selen làm giảm chuyển hóa T4 thành T3.",
        "<b>Deiodinase typ 1 (D1 - Gan, Thận, Tuyến giáp) —</b> Khử iod ở vòng ngoài của T4 tạo T3; chịu trách nhiệm tạo ra phần lớn T3 lưu thông trong huyết tương.",
        "<b>Deiodinase typ 2 (D2 - Não, Tuyến yên, Cơ vân, Mỡ nâu) —</b> Khử iod vòng ngoài của T4 tạo T3 nội bào; duy trì nồng độ T3 ổn định tại mô thần kinh và thực hiện feedback ức chế TSH tại tuyến yên.",
        "<b>Deiodinase typ 3 (D3 - Nhau thai, Da, Não) —</b> Khử iod ở vòng TRONG của T4 tạo Reverse T3 (rT3 bất hoạt), và khử T3 thành T2; đóng vai trò enzym bất hoạt bảo vệ cơ thể khỏi quá tải hormon.",
        "<b>Hội chứng bệnh giáp bình thường (Euthyroid Sick Syndrome) —</b> Khi bệnh nặng, đói ăn hoặc sốc nhiễm trùng, hoạt tính D1 giảm nhưng D3 tăng làm nồng độ T3 máu giảm mạnh và rT3 tăng vọt để tiết kiệm năng lượng."
    ],
    "T4 chỉ là một prohormon lưu thông bền vững; chuyển đổi T4 thành T3 hoạt tính ở ngoại vi thông qua enzym D1 và D2 là bước kiểm soát tốc độ sinh nhiệt và chuyển hóa tế bào."
))

cards.append(make_card(
    "HS13-B6-05",
    "Bệnh học Tự miễn Tuyến Giáp: Bệnh Basedow (Graves) vs Viêm Giáp Hashimoto",
    "TỰ MIỄN TUYẾN GIÁP",
    "Đối chiếu cơ chế tự miễn, tự kháng thể đặc hiệu và biến đổi sinh hóa giữa Basedow và Hashimoto?",
    [
        "<b>Bệnh Basedow (Graves - Cường giáp tự miễn) —</b> Xuất hiện tự kháng thể kích thích thụ thể TSH (TRAb / TSI) gắn vào và kích hoạt liên tục thụ thể TSH qua hệ Gs/cAMP.",
        "<b>Sinh hóa Basedow —</b> T3 và T4 tăng vọt, TSH bị ức chế triệt để (<0,01 µIU/mL); bướu giáp to lan tỏa tăng sinh mạch máu, lồi mắt do thâm nhiễm nguyên bào sợi hốc mắt.",
        "<b>Viêm tuyến giáp Hashimoto (Suy giáp tự miễn) —</b> Phản ứng tự miễn qua tế bào T thâm nhiễm phá hủy tế bào nang giáp; xuất hiện tự kháng thể anti-TPO và anti-Thyroglobulin (anti-Tg).",
        "<b>Sinh hóa Hashimoto —</b> Giai đoạn muộn FT4 giảm thấp, TSH tăng rất cao bù trừ; bướu giáp chắc gồ ghề kèm triệu chứng suy giáp (phù niêm, chậm chạp, sợ lạnh, tăng cân).",
        "<b>Ý nghĩa chẩn đoán phân biệt —</b> Đo hiệu số TRAb khẳng định Basedow; đo anti-TPO khẳng định nguồn gốc tự miễn của suy giáp Hashimoto."
    ],
    "Hai diện mạo tự miễn đối lập: Basedow là tự kháng thể 'chủ vận' kích thích tuyến phì đại sản xuất quá mức; Hashimoto là phản ứng tự miễn 'phá hủy' làm tiêu vong mô tuyến."
))

cards.append(make_card(
    "HS13-B6-06",
    "Chuỗi Phản ứng Sinh tổng hợp Catecholamin từ Tyrosine",
    "SINH TỔNG HỢP CATECHOLAMIN",
    "Chuỗi phản ứng 5 bước từ L-Tyrosin tạo Adrenalin tại tủy thượng thận và enzym giới hạn tốc độ?",
    [
        "<b>Bước 1 (L-Tyrosin → L-DOPA) —</b> Xúc tác bởi Tyrosin Hydroxylase (cần Tetrahydrobiopterin - BH4, Fe2+, O2). ĐÂY LÀ PHẢN ỨNG GIỚI HẠN TỐC ĐỘ (Rate-limiting step) của toàn chuỗi.",
        "<b>Bước 2 (L-DOPA → Dopamin) —</b> Khử carboxyl xúc tác bởi DOPA Decarboxylase (cần coenzym Pyridoxal phosphat - Vitamin B6) diễn ra trong bào tương.",
        "<b>Bước 3 (Dopamin vào túi hạt) —</b> Dopamin được bơm vào trong lòng các túi hạt chế tiết (chromaffin granules) qua chất vận chuyển VMAT2.",
        "<b>Bước 4 (Dopamin → Noradrenalin) —</b> Xúc tác bởi enzym Dopamin beta-Hydroxylase (nằm trong túi hạt, cần Vitamin C và Cu2+).",
        "<b>Bước 5 (Noradrenalin → Adrenalin) —</b> Noradrenalin khuếch tán ra bào tương, nhận nhóm methyl từ S-Adenosylmethionin (SAM) nhờ enzym PNMT (được cảm ứng mạnh mẽ bởi Cortisol từ vỏ thượng thận).",
        "<b>Tỷ lệ bài tiết sinh lý —</b> Tủy thượng thận người bài tiết khoảng 80% Adrenalin và 20% Noradrenalin."
    ],
    "Sự kề cận giải phẫu giữa vỏ và tủy thượng thận có mục đích sinh hóa sâu sắc: nồng độ Cortisol đậm đặc từ vỏ thượng thận kích hoạt enzym PNMT để chuyển Noradrenalin thành Adrenalin."
))

cards.append(make_card(
    "HS13-B6-07",
    "Con đường Thoái hóa Catecholamin qua MAO, COMT và Ý nghĩa VMA Niệu",
    "THOÁI HÓA CATECHOLAMIN",
    "Cơ chế thoái hóa catecholamin nhờ sự phối hợp của MAO và COMT cùng giá trị chẩn đoán của VMA?",
    [
        "<b>Thời gian bán hủy —</b> Catecholamin trong máu có đời sống cực ngắn (1 - 2 phút), bị thoái hóa nhanh chóng chủ yếu tại tế bào gan và thận.",
        "<b>Enzym COMT (Catechol-O-Methyltransferase) —</b> Chuyển nhóm methyl từ SAM vào nhóm -OH vị trí C-3 của vòng catechol (tạo Metanephrin từ Adrenalin, Normetanephrin từ Noradrenalin).",
        "<b>Enzym MAO (Monoamine Oxidase) —</b> Khử amin oxy hóa chuỗi ethylamin tạo andehit tương ứng, sau đó oxy hóa thành acid carboxylic.",
        "<b>Sản phẩm thoái hóa cuối cùng bền vững —</b> Acid Vanillylmandelic (VMA / 4-hydroxy-3-methoxymandelic acid) và các dẫn xuất Metanephrin liên hợp được bài tiết hoàn toàn qua nước tiểu.",
        "<b>Ý nghĩa chẩn đoán vàng —</b> Định lượng Metanephrin tự do huyết tương và VMA trong nước tiểu 24 giờ là xét nghiệm tiêu chuẩn vàng để phát hiện u tủy thượng thận (Pheochromocytoma)."
    ],
    "Vì catecholamin bài tiết theo từng cơn ngắn, việc đo nồng độ trong máu lúc bình thường dễ bị âm tính giả; đo tổng lượng Metanephrin và VMA tích lũy trong nước tiểu 24 giờ cho độ tin cậy tuyệt đối."
))

cards.append(make_card(
    "HS13-B6-08",
    "U Tủy Thượng Thận (Pheochromocytoma): Cơ chế Phân tử và Tam chứng Cổ điển",
    "U TỦY THƯỢNG THẬN",
    "Cơ chế tác động thụ thể adrenergic giải thích tam chứng lâm sàng của bệnh Pheochromocytoma?",
    [
        "<b>Bản chất khối u —</b> Khối u tăng sinh lành tính hoặc ác tính của các tế bào ưa crôm (chromaffin cells) tủy thượng thận hoặc hạch giao cảm, bài tiết ồ ạt Adrenalin và Noradrenalin.",
        "<b>Tam chứng cổ điển điển hình —</b> Nhức đầu dữ dội (Headache) - Vã mồ hôi đầm đìa (Sweating) - Tim đập nhanh/hồi hộp (Tachycardia), xuất hiện từng cơn.",
        "<b>Tác động qua thụ thể alpha-1 —</b> Co thắt mạch máu ngoại vi dữ dội gây các cơn tăng huyết áp kịch phát (huyết áp có thể >220/120 mmHg), da tái nhợt đầu chi.",
        "<b>Tác động qua thụ thể beta-1 —</b> Tăng nhịp tim, tăng co bóp cơ tim, gây cảm giác tim đập mạnh như nhảy ra khỏi lồng ngực, tăng nguy cơ loạn nhịp thất.",
        "<b>Tác động qua thụ thể beta-2 và alpha-2 —</b> Tăng phân giải glycogen gan và ức chế tiết insulin tụy dẫn đến tăng đường huyết rõ rệt trong và sau cơn bão catecholamin."
    ],
    "Quy tắc 10% kinh điển của Pheochromocytoma: 10% ngoài tuyến thượng thận, 10% ở hai bên, 10% ác tính, 10% có tính chất gia đình di truyền (kèm hội chứng MEN 2, VHL, NF1)."
))

cards.append(make_card(
    "HS13-B6-09",
    "Cấu trúc 3 Lớp Vỏ Thượng Thận và Sự Phân vùng Chức năng",
    "CẤU TRÚC VỎ THƯỢNG THẬN",
    "Giải phẫu chức năng 3 lớp tế bào của vỏ thượng thận (Cầu, Bó, Lưới) và các hormon tương ứng?",
    [
        "<b>Lớp Cầu ngoài cùng (Zona Glomerulosa, 15%) —</b> Chịu sự điều hòa của Angiotensin II và ion K+ máu; tiết Mineralocorticoid chủ yếu là Aldosteron (nhờ enzym độc quyền Aldosteron Synthase).",
        "<b>Lớp Bó ở giữa (Zona Fasciculata, 75%) —</b> Lớp dày nhất, chịu sự điều hòa của ACTH tuyến yên; tiết Glucocorticoid chủ yếu là Cortisol và Corticosteron.",
        "<b>Lớp Lưới trong cùng (Zona Reticularis, 10%) —</b> Nằm sát tủy thượng thận, chịu kích thích của ACTH; tiết Androgen thượng thận chủ yếu là DHEA, DHEA-S và Androstenedion.",
        "<b>Cơ sở phân vùng sinh hóa —</b> Sự biểu hiện đặc hiệu mô của các enzym hydroxylase (CYP11B2 chỉ có ở lớp Cầu; CYP17A1 chỉ có ở lớp Bó và Lưới).",
        "<b>Mẹo ghi nhớ quốc tế —</b> GFR tương ứng M-G-A (Glomerulosa tiết Mineralocorticoids, Fasciculata tiết Glucocorticoids, Reticularis tiết Androgens: 'Salt, Sugar, Sex')."
    ],
    "Sự phân vùng enzym độc đáo đảm bảo mỗi lớp tế bào vỏ thượng thận chuyên biệt hóa hoàn toàn cho một nhiệm vụ sinh học sống còn riêng biệt."
))

cards.append(make_card(
    "HS13-B6-10",
    "Enzym Mở đầu Then chốt: StAR và CYP11A1 (Cholesterol Desmolase)",
    "BƯỚC MỞ ĐẦU STEROID",
    "Cơ chế phản ứng bẻ gãy chuỗi nhánh cholesterol mở đầu toàn bộ chuỗi sinh tổng hợp steroid?",
    [
        "<b>Protein vận chuyển StAR —</b> Steroidogenic Acute Regulatory protein đưa Cholesterol kỵ nước từ màng ngoài xuyên qua khoang gian màng vào màng trong ty thể (đây là bước hạn chế tốc độ thực sự).",
        "<b>Enzym CYP11A1 (Cholesterol Desmolase / SCC) —</b> Phức hợp enzym cytochrom P450 liên kết màng trong ty thể cần NADPH và enzym phụ trợ Ferredoxin/Ferredoxin Reductase.",
        "<b>Cơ chế bẻ gãy liên kết C20 - C22 —</b> Hydroxyl hóa liên tiếp tại vị trí C-20 và C-22, sau đó cắt bỏ chuỗi nhánh 6 carbon (Isocaproic aldehyde) khỏi phân tử Cholesterol (27 Carbon).",
        "<b>Sản phẩm tạo thành —</b> Biến Cholesterol (27C) thành Pregnenolon (21C), hợp chất tiền thân chung của toàn bộ hormon steroid.",
        "<b>Kích hoạt bởi hormon hướng tuyến —</b> ACTH kích hoạt StAR và CYP11A1 tại vỏ thượng thận; LH kích hoạt tại tế bào Leydig tinh hoàn và tế bào vỏ buồng trứng."
    ],
    "Toàn bộ con đường tổng hợp hormon steroid trong cơ thể đều bắt buộc phải vượt qua cánh cửa duy nhất mang tên CYP11A1; bất hoạt enzym này sẽ triệt tiêu hoàn toàn khả năng tạo steroid của cơ thể."
))

cards.append(make_card(
    "HS13-B6-11",
    "Tăng sinh Tuyến Thượng Thận Bẩm sinh (CAH) do Thiếu 21-Hydroxylase",
    "BỆNH HỌC CAH 21-OH",
    "Cơ chế chuyển hướng con đường sinh hóa, tích tụ 17-OHP và biểu hiện lâm sàng của thể thiếu 21-hydroxylase?",
    [
        "<b>Tần suất di truyền —</b> Chiếm trên 90% các trường hợp CAH do đột biến gen CYP21A2 trên nhánh ngắn nhiễm sắc thể 6 (di truyền lặn trên NST thường).",
        "<b>Vị trí tắc nghẽn enzym —</b> Thiếu enzym 21-hydroxylase ngăn cản chuyển Progesteron → 11-DOC (tổng hợp Aldosteron) và 17-OH-Progesteron → 11-Deoxycortisol (tổng hợp Cortisol).",
        "<b>Kích thích trục HPA quá mức —</b> Nồng độ Cortisol sụt giảm làm mất ức chế ngược, tuyến yên tăng tiết ồ ạt ACTH kích thích vỏ thượng thận phì đại to hai bên.",
        "<b>Hiện tượng tràn dòng sang Androgen —</b> Toàn bộ cơ chất ứ đọng phía trên (17-OHP) bị đẩy tràn sang nhánh lớp Lưới tổng hợp DHEA, Androstenedion và Testosteron.",
        "<b>Biểu hiện lâm sàng —</b> Nam hóa bộ phận sinh dục ngoài ở bé gái sơ sinh (phì đại âm vật, dính môi lớn như bìu), dậy thì sớm ở bé trai; thể mất muối nặng gây mất nước, tụt huyết áp, tăng kali máu tử vong trong 2 tuần đầu sau sinh."
    ],
    "Định lượng nồng độ 17-Hydroxyprogesterone (17-OHP) máu gót chân là xét nghiệm sàng lọc sơ sinh bắt buộc để phát hiện sớm và cứu sống trẻ mắc hội chứng CAH."
))

cards.append(make_card(
    "HS13-B6-12",
    "Hội chứng Conn (Cường Aldosteron Tiên phát): ARR và Cơ chế ENaC",
    "HỘI CHỨNG CONN",
    "Cơ chế sinh học phân tử của Aldosteron tại ống thận và xét nghiệm tỷ số ARR trong chẩn đoán Hội chứng Conn?",
    [
        "<b>Bản chất bệnh lý —</b> U tuyến vỏ thượng thận tiết aldosteron tự chủ (Adenoma chiếm 60%) hoặc tăng sản lớp cầu hai bên, tiết aldosteron độc lập với hệ Renin-Angiotensin.",
        "<b>Tác động qua thụ thể MR —</b> Aldosteron gắn thụ thể Mineralocorticoid ở tế bào chính ống góp, kích thích phiên mã kênh ENaC ở màng đỉnh và bơm Na+/K+-ATPase ở màng đáy.",
        "<b>Hậu quả tái hấp thu —</b> Tăng tối đa giữ Na+ vào máu và tăng đào thải K+, H+ qua nước tiểu qua kênh ROMK và bơm H+-ATPase.",
        "<b>Biểu hiện lâm sàng và điện giải —</b> Tăng huyết áp kháng trị (do tăng thể tích tuần hoàn), hạ Kali máu (yếu cơ, sóng U điện tâm đồ), kiềm chuyển hóa.",
        "<b>Chỉ số vàng ARR (Aldosterone-to-Renin Ratio) —</b> Tỷ số nồng độ Aldosteron / Hoạt độ Renin huyết tương tăng vọt (Aldosteron máu cao bất thường trong khi Renin bị ức chế triệt để về gần 0)."
    ],
    "Tỷ số ARR là xét nghiệm sàng lọc số 1 đối với mọi bệnh nhân tăng huyết áp kháng trị kèm hạ kali máu nhằm phát hiện nguyên nhân có thể phẫu thuật triệt căn."
))

cards.append(make_card(
    "HS13-B6-13",
    "Bệnh Addison (Suy Vỏ Thượng Thận Tiên Phát) vs Hội chứng Cushing",
    "ADDISON VS CUSHING",
    "Đối chiếu cơ chế phân tử và biểu hiện sinh hóa giữa Bệnh Addison và Hội chứng Cushing?",
    [
        "<b>Bệnh Addison (Suy vỏ tiên phát) —</b> Phá hủy tự miễn hoặc lao phá hủy trên 90% vỏ thượng thận → Thiếu hụt toàn bộ Cortisol và Aldosteron.",
        "<b>Sinh hóa Addison —</b> Hạ Natri máu, Tăng Kali máu, Toan chuyển hóa nhẹ, Hạ đường huyết lúc đói, ACTH tăng vọt (do mất feedback âm tính).",
        "<b>Cơ chế sạm da đặc trưng ở Addison —</b> Tuyến yên tăng tiết tiền chất POMC để tạo ACTH; các peptide này mang đoạn trình tự alpha-MSH kích thích tế bào hắc tố tổng hợp Melanin (sạm niêm mạc má, nếp gấp bàn tay, sẹo mới).",
        "<b>Hội chứng Cushing (Cường Cortisol mạn) —</b> Nồng độ Cortisol tăng cao kéo dài do u thượng thận, u tuyến yên tiết ACTH (Bệnh Cushing) hoặc dùng thuốc ngoại sinh.",
        "<b>Sinh hóa Cushing —</b> Tăng tân tạo đường (đái tháo đường steroid), dị hóa protein (teo cơ gốc chi, vết rạn da đỏ tím rộng), tái phân bố mỡ trung tâm (mặt tròn như trăng, bướu trâu gáy), loãng xương."
    ],
    "Hai thái cực kinh điển của chức năng vỏ thượng thận: một bên suy sụp kiệt quệ sinh lực và sạm da (Addison), một bên bùng nổ dị hóa và biến dạng hình thể (Cushing)."
))

# ==============================================================================
# SECTION B7: HÓA SINH INSULIN, GLUCAGON & ĐIỀU HÒA ĐƯỜNG HUYẾT (13 thẻ: HS13-B7-01 -> HS13-B7-13)
# ==============================================================================

cards.append(make_card(
    "HS13-B7-01",
    "Cấu trúc Bậc 1 và Các Cầu Disulfua của Phân tử Insulin",
    "CẤU TRÚC INSULIN",
    "Cấu tạo chuỗi polypeptide, số lượng acid amin và vị trí các cầu disulfua (-S-S-) của phân tử Insulin người?",
    [
        "<b>Chuỗi A (21 acid amin) —</b> Chuỗi ngắn chứa một cầu disulfua nội chuỗi (Intrachain) nối giữa Cystein vị trí A6 và A11.",
        "<b>Chuỗi B (30 acid amin) —</b> Chuỗi dài hơn mang các gốc acid amin tham gia vào bề mặt tương tác với thụ thể và tạo dạng hexamer.",
        "<b>Hai cầu nối disulfua liên chuỗi (Interchain) —</b> Nối bền vững giữa chuỗi A và B: một cầu nối A7 với B7, một cầu nối A20 với B19.",
        "<b>Tổng số acid amin và liên kết —</b> Phân tử Insulin hoàn chỉnh gồm 51 acid amin liên kết bởi tổng cộng 3 cầu nối disulfua (-S-S-).",
        "<b>Ý nghĩa cấu trúc —</b> Bất kỳ sự phá vỡ cầu disulfua nào (nhờ chất khử mercaptoethanol) đều làm phân tử duỗi xoắn và mất hoàn toàn hoạt tính sinh học."
    ],
    "Insulin là phân tử protein đầu tiên trong lịch sử nhân loại được xác định trọn vẹn trình tự acid amin bậc 1 bởi Frederick Sanger vào năm 1953 (đoạt giải Nobel Hóa học 1958)."
))

cards.append(make_card(
    "HS13-B7-02",
    "Sinh tổng hợp Insulin: Từ Preproinsulin, Proinsulin đến C-Peptide",
    "QUÁ TRÌNH SINH TỔNG HỢP",
    "Các giai đoạn hoàn thiện phân tử Insulin từ tiền chất trong tế bào beta đảo tụy và vai trò C-peptide?",
    [
        "<b>Preproinsulin (110 aa) —</b> Tổng hợp tại ribosome lưới nội chất hạt, mang một đoạn peptide tín hiệu kỵ nước (Signal peptide 24 aa) ở đầu N.",
        "<b>Cắt tạo Proinsulin (86 aa) —</b> Peptidase tại màng lưới nội chất cắt bỏ peptide tín hiệu; phân tử gấp cuộn hình thành 3 cầu disulfua chuẩn xác tạo Proinsulin.",
        "<b>Đóng gói tại bộ máy Golgi —</b> Proinsulin được vận chuyển đến thể Golgi và đóng gói vào trong các túi bóng chế tiết giàu ion Kẽm (Zn2+).",
        "<b>Cắt bởi Prohormone Convertase (PC1/3 và PC2) —</b> Các endopeptidase phối hợp Carboxypeptidase E cắt bỏ chuỗi nối C (Connecting peptide / C-peptide 31 aa) giải phóng Insulin và C-peptide theo tỷ lệ equimolar 1:1.",
        "<b>Dạng tinh thể Hexamer —</b> 6 phân tử Insulin kết hợp với 2 ion Kẽm (Zn2+) tạo thành phức hợp hexamer kết tinh ổn định trong lòng túi tiết chờ phóng thích."
    ],
    "Tỷ lệ bài xuất equimolar 1:1 giữa Insulin và C-peptide là tiền đề cho xét nghiệm định lượng C-peptide phản ánh chính xác hoạt động bài tiết của tế bào beta tụy."
))

cards.append(make_card(
    "HS13-B7-03",
    "Giá trị Lâm sàng của Định lượng C-Peptide Huyết tương",
    "Ý NGHĨA C-PEPTIDE",
    "Vì sao định lượng C-peptide huyết tương là chỉ số vàng đánh giá chức năng bài tiết Insulin nội sinh?",
    [
        "<b>Tỷ lệ bài tiết tương đương —</b> Tế bào beta giải phóng Insulin và C-peptide vào tĩnh mạch cửa theo tỷ lệ phân tử chính xác 1:1.",
        "<b>Không bị gan bắt giữ bước đầu —</b> Gan bắt giữ và giáng hóa tới 50 - 60% lượng Insulin ngay trong lần tuần hoàn đầu tiên qua tĩnh mạch cửa, nhưng gan HOÀN TOÀN KHÔNG bắt giữ C-peptide.",
        "<b>Thời gian bán hủy kéo dài —</b> C-peptide có thời gian bán hủy dài hơn nhiều (khoảng 20 - 30 phút so với 3 - 5 phút của Insulin) và nồng độ huyết tương ổn định hơn.",
        "<b>Không bị nhiễu bởi Insulin ngoại sinh —</b> Các chế phẩm tiêm Insulin điều trị (nhân tạo) không chứa C-peptide; xét nghiệm kháng thể Insulin cũng không bắt chéo với C-peptide.",
        "<b>Ứng dụng phân loại Đái tháo đường —</b> C-peptide cực thấp/không đo được xác định Đái tháo đường Typ 1 (thiếu insulin tuyệt đối); C-peptide bình thường hoặc tăng cao xác định Đái tháo đường Typ 2 (đề kháng insulin)."
    ],
    "Định lượng C-peptide là phương tiện duy nhất giúp thầy thuốc phân định chính xác lượng Insulin trong máu bệnh nhân là do cơ thể tự tiết ra hay do mũi tiêm thuốc đưa vào."
))

cards.append(make_card(
    "HS13-B7-04",
    "Cơ chế Tiết Insulin Phụ thuộc Glucose ở Tế bào Beta Đảo Tụy",
    "CƠ CHẾ TIẾT PHÂN TỬ",
    "Chuỗi sự kiện ghép nối chuyển hóa - điện thế màng chỉ huy sự xuất bào Insulin khi nồng độ Glucose máu tăng cao?",
    [
        "<b>Bước 1 (Glucose vào tế bào) —</b> Glucose khuếch tán được tạo điều kiện qua kênh vận chuyển GLUT2 (ái lực thấp, dung lượng cao) vào trong bào tương tế bào beta.",
        "<b>Bước 2 (Cảm biến bởi Glucokinase) —</b> Enzym Glucokinase (Km cao ~10 mM) phosphoryl hóa Glucose thành G6P; tốc độ đường phân tăng tỷ lệ thuận trực tiếp với nồng độ glucose máu.",
        "<b>Bước 3 (Tăng tỷ số ATP/ADP) —</b> Chu trình Krebs và chuỗi hô hấp tế bào sản xuất lượng lớn ATP, làm tăng vọt tỷ số ATP/ADP trong bào tương.",
        "<b>Bước 4 (Đóng kênh K_ATP) —</b> Nồng độ ATP cao gắn vào tiểu đơn vị Kir6.2 làm ĐÓNG kênh Kali nhạy cảm ATP (K_ATP channel).",
        "<b>Bước 5 (Khử cực màng tế bào) —</b> Ion K+ bị giữ lại trong tế bào làm điện thế màng chuyển từ -70 mV lên -30 mV (khử cực màng sinh chất).",
        "<b>Bước 6 (Mở kênh Ca2+ và xuất bào) —</b> Khử cực kích hoạt mở kênh Canxi phụ thuộc điện thế (VDCC); dòng Ca2+ ngoại bào tuôn vào kích thích các bọc tiết chứa Insulin hòa màng xuất bào."
    ],
    "Enzym Glucokinase hoạt động như một 'nhiệt kế cảm biến glucose' (glucose sensor) của cơ thể; mọi đột biến gen Glucokinase đều làm thay đổi ngưỡng bài tiết insulin (bệnh MODY 2)."
))

cards.append(make_card(
    "HS13-B7-05",
    "Điểm Can thiệp Dược lý Kênh K_ATP: Nhóm Thuốc Sulfonylurea và Diazoxide",
    "DƯỢC LÝ KÊNH K_ATP",
    "Cấu trúc kênh K_ATP nhạy cảm ATP và cơ chế tác dụng đối kháng của nhóm thuốc Sulfonylurea vs Diazoxide?",
    [
        "<b>Cấu trúc kênh octamer —</b> Gồm 4 tiểu đơn vị tạo lỗ dẫn ion Kir6.2 liên kết với 4 tiểu đơn vị thụ thể điều hòa SUR1 (Sulfonylurea Receptor 1).",
        "<b>Cơ chế thuốc Sulfonylurea (Gliclazide, Glimepiride) —</b> Gắn đặc hiệu vào tiểu đơn vị SUR1, bắt chước tác dụng của ATP làm ĐÓNG kênh K_ATP ngay cả khi nồng độ glucose máu không cao.",
        "<b>Hệ quả Sulfonylurea —</b> Khử cực màng tế bào beta, mở kênh Ca2+ và kích thích giải phóng ồ ạt Insulin nội sinh vào máu, làm hạ nhanh đường huyết (nguy cơ hạ đường huyết quá mức).",
        "<b>Cơ chế thuốc Diazoxide —</b> Là chất mở kênh (K_ATP channel opener) gắn vào SUR1 giữ kênh K_ATP luôn ở trạng thái MỞ.",
        "<b>Hệ quả Diazoxide —</b> Tăng phân cực màng (hyperpolarization), ngăn cản kênh Ca2+ mở, ức chế triệt để sự bài tiết Insulin; được dùng để điều trị hạ đường huyết nặng do u tế bào beta đảo tụy (Insulinoma)."
    ],
    "Sulfonylurea là nhóm thuốc uống điều trị đái tháo đường lâu đời nhất; hiểu rõ kênh K_ATP giải thích trọn vẹn cả hiệu lực hạ đường huyết lẫn biến chứng hạ đường huyết đáng sợ của nhóm thuốc này."
))

cards.append(make_card(
    "HS13-B7-06",
    "Mạng lưới Kênh Vận chuyển Glucose (Họ GLUT: GLUT1 đến GLUT5)",
    "HỌ KÊNH GLUT",
    "Phân bố mô, đặc tính ái lực và sự phụ thuộc Insulin của 5 kênh vận chuyển Glucose dòng GLUT chính?",
    [
        "<b>GLUT1 (Km ~1 mM, ái lực cao) —</b> Phân bố ở màng hồng cầu, hàng rào máu não (BBB), thận; đảm bảo cung cấp glucose nền liên tục cho não và tế bào máu, KHÔNG phụ thuộc insulin.",
        "<b>GLUT2 (Km ~15 - 20 mM, ái lực rất thấp) —</b> Phân bố ở tế bào beta đảo tụy, gan, màng đáy ruột và thận; chỉ vận chuyển glucose nhanh khi đường máu tăng cao (đóng vai trò cảm biến glucose), KHÔNG phụ thuộc insulin.",
        "<b>GLUT3 (Km <1 mM, ái lực cao nhất) —</b> Phân bố chuyên biệt ở neuron thần kinh; ưu tiên tối đa thu nhận glucose cho não ngay cả khi đường huyết hạ thấp, KHÔNG phụ thuộc insulin.",
        "<b>GLUT4 (Km ~5 mM, nhạy cảm Insulin) —</b> Phân bố độc quyền tại Cơ vân, Cơ tim và Mô mỡ; BẮT BUỘC PHẢI CÓ INSULIN (hoặc co cơ vận động) kích hoạt Akt mới chuyển vị từ túi nội bào ra màng tế bào.",
        "<b>GLUT5 —</b> Kênh chuyên biệt vận chuyển Fructose phân bố ở bờ bàn chải niêm mạc ruột non và tinh trùng."
    ],
    "Trong toàn bộ các kênh vận chuyển đường, CHỈ CÓ DUY NHẤT GLUT4 ở cơ và mỡ là phụ thuộc vào hormon Insulin để phơi bày lên màng tế bào."
))

cards.append(make_card(
    "HS13-B7-07",
    "Tác động Chuyển hóa của Insulin tại Gan: Tân tạo, Tổng hợp Glycogen và Mỡ",
    "TÁC ĐỘNG INSULIN TẠI GAN",
    "Insulin điều hòa các enzym chuyển hóa then chốt tại tế bào gan như thế nào để hạ đường huyết sau ăn?",
    [
        "<b>Kích hoạt tổng hợp Glycogen —</b> Kích thích Protein Phosphatase-1 (PP-1) khử phosphat hoạt hóa Glycogen Synthase, đồng thời khử phosphat bất hoạt Glycogen Phosphorylase.",
        "<b>Thúc đẩy đường phân —</b> Cảm ứng sinh tổng hợp Glucokinase; hoạt hóa enzym kép PFK-2/FBPase-2 làm tăng Fructose-2,6-bisphosphat kích hoạt dị lập thể mạnh mẽ enzym PFK-1.",
        "<b>Khóa chặt tân tạo đường —</b> Ức chế phiên mã gen các enzym giới hạn tốc độ tân tạo glucose: Phosphoenolpyruvate Carboxykinase (PEPCK) và Glucose-6-Phosphatase.",
        "<b>Thúc đẩy tổng hợp Acid béo —</b> Hoạt hóa enzym Acetyl-CoA Carboxylase (ACC) khử phosphat tạo Malonyl-CoA; Malonyl-CoA ức chế enzym CPT-1 chặn đứng quá trình oxy hóa acid béo vào ty thể.",
        "<b>Tăng đóng gói VLDL —</b> Thúc đẩy este hóa triglycerid và bài xuất lipoprotein tỷ trọng rất thấp (VLDL) vào máu."
    ],
    "Tại gan, Insulin biến cơ quan này từ một 'nhà máy sản xuất và giải phóng đường' trong lúc đói thành một 'kho tích trữ khổng lồ glucose dưới dạng glycogen và lipid' sau bữa ăn."
))

cards.append(make_card(
    "HS13-B7-08",
    "Hóa sinh Glucagon: Nguồn gốc, Cấu trúc và Thụ thể GPCR Gs",
    "HÓA SINH GLUCAGON",
    "Đặc tính cấu trúc của Glucagon, thụ thể tiếp nhận và cơ chế đối kháng sinh học với Insulin?",
    [
        "<b>Nơi sản xuất —</b> Do các tế bào alpha (chiếm khoảng 20% đảo tụy Langerhans) tổng hợp và bài tiết khi nồng độ glucose máu giảm xuống dưới 4,0 mmol/L (70 mg/dL).",
        "<b>Cấu trúc phân tử —</b> Là một chuỗi đơn polypeptide thẳng gồm 29 acid amin (khối lượng 3485 Da), không có cầu nối disulfua.",
        "<b>Thụ thể tiếp nhận —</b> Gắn đặc hiệu vào thụ thể Glucagon Receptor trên màng tế bào gan, thuộc họ GPCR bắt cặp với Protein Gs.",
        "<b>Phát động tín hiệu —</b> Gs-alpha-GTP kích hoạt Adenylate Cyclase tạo bùng nổ cAMP, hoạt hóa Protein Kinase A (PKA).",
        "<b>Cơ quan đích độc quyền —</b> Tác động chuyển hóa carbohydrate hầu như chỉ khu trú tại Gan (tế bào cơ vân KHÔNG CÓ thụ thể glucagon).",
        "<b>Đáp ứng sinh học —</b> Kích hoạt đồng thời phân giải Glycogen và Tân tạo Glucose giải phóng glucose tự do vào máu, nâng nhanh đường huyết chống hôn mê."
    ],
    "Glucagon là 'kỵ binh cứu viện' hàng đầu bảo vệ não bộ khỏi tổn thương không hồi phục mỗi khi cơ thể rơi vào tình trạng hạ đường huyết cấp tính."
))

cards.append(make_card(
    "HS13-B7-09",
    "Cơ chế Phân tử Đối kháng Insulin vs Glucagon: Phosphoryl hóa vs Khử Phosphat",
    "ĐỐI KHÁNG PHÂN TỬ",
    "Nguyên lý đối kháng phân tử toàn diện giữa trạng thái no (Insulin) và đói (Glucagon) thông qua mạng lưới enzym kinase/phosphatase?",
    [
        "<b>Quy tắc vạn năng của Glucagon (Trạng thái đói) —</b> Glucagon → cAMP → PKA kích hoạt → CÁC ENZYM CHUYỂN HÓA BỊ GẮN THÊM GỐC PHOSPHAT (Phosphorylated state).",
        "<b>Trạng thái hoạt động khi bị gắn phosphat —</b> Các enzym dị hóa và giải phóng năng lượng được BẬT: Glycogen Phosphorylase (hoạt động), FBPase-2 (hoạt động), Hormone-Sensitive Lipase (hoạt động).",
        "<b>Trạng thái bất hoạt khi bị gắn phosphat —</b> Các enzym đồng hóa tích trữ bị TẮT: Glycogen Synthase (bất hoạt), PFK-2 (bất hoạt), Pyruvate Kinase (bất hoạt), ACC (bất hoạt).",
        "<b>Quy tắc vạn năng của Insulin (Trạng thái no) —</b> Insulin → Akt → Kích hoạt Protein Phosphatase (PP-1) → CÁC ENZYM ĐƯỢC CẮT BỎ GỐC PHOSPHAT (Dephosphorylated state).",
        "<b>Ý nghĩa hệ thống —</b> Cơ chế chuyển đổi trạng thái cộng hóa trị phosphoryl hóa/khử phosphat đảm bảo hai con đường đối kháng không bao giờ diễn ra đồng thời, triệt tiêu chu trình vô ích (futile cycles)."
    ],
    "Chỉ cần nắm vững câu thần chú sinh hóa này: 'Glucagon gắn phosphat để kích hoạt phân giải; Insulin gỡ phosphat để kích hoạt tổng hợp'."
))

cards.append(make_card(
    "HS13-B7-10",
    "Điều hòa Enzym Kép PFK-2 / FBPase-2 và Fructose-2,6-Bisphosphat",
    "ĐIỀU HÒA ENZYM KÉP",
    "Cơ chế chuyển đổi hoạt tính của enzym hai đầu PFK-2/FBPase-2 dưới tác dụng của Insulin và Glucagon?",
    [
        "<b>Cấu trúc enzym lưỡng chức năng —</b> Một chuỗi polypeptide duy nhất mang hai trung tâm xúc tác đối lập: đầu kinase (PFK-2) và đầu phosphatase (FBPase-2).",
        "<b>Tác dụng của Fructose-2,6-bisphosphat (F-2,6-BP) —</b> Là chất điều hòa dị lập thể dương mạnh nhất của PFK-1 (kích thích đường phân), và ức chế dị lập thể mạnh nhất FBPase-1 (khóa tân tạo đường).",
        "<b>Khi nồng độ Glucagon cao (Đói) —</b> PKA phosphoryl hóa enzym kép → Bất hoạt đầu PFK-2, Kích hoạt đầu FBPase-2 → Giảm nồng độ F-2,6-BP → Ức chế đường phân, kích hoạt tân tạo glucose giải phóng ra máu.",
        "<b>Khi nồng độ Insulin cao (No) —</b> PP-1 khử phosphat enzym kép → Kích hoạt đầu PFK-2, Bất hoạt đầu FBPase-2 → Tăng vọt F-2,6-BP → Kích hoạt cực mạnh PFK-1, thúc đẩy đường phân tiêu thụ glucose tại gan."
    ],
    "F-2,6-BP là 'chiếc van điều áp lưu lượng' tối cao tại ngã tư đường phân và tân tạo đường; enzym kép PFK-2/FBPase-2 chính là bộ vi xử lý nhận lệnh trực tiếp từ cặp bài trùng Insulin - Glucagon."
))

cards.append(make_card(
    "HS13-B7-11",
    "Điều hòa Chuyển hóa Lipid: Lipase Nhạy cảm Hormon (HSL) vs Lipoprotein Lipase (LPL)",
    "ĐIỀU HÒA LIPID",
    "Sự tác động đối kháng của Insulin và Catecholamin/Glucagon lên enzym HSL mô mỡ và LPL thành mạch?",
    [
        "<b>Enzym Hormone-Sensitive Lipase (HSL) tại mô mỡ —</b> Phân giải Triglycerid dự trữ trong giọt mỡ thành Acid béo tự do (FFA) và Glycerol đổ vào máu.",
        "<b>Kích hoạt HSL bởi Glucagon và Adrenalin —</b> Qua hệ cAMP/PKA, PKA phosphoryl hóa hoạt hóa HSL và protein bao giọt mỡ Perilipin, đẩy mạnh phân giải mỡ cung cấp năng lượng khi đói hoặc vận động.",
        "<b>Ức chế HSL bởi Insulin —</b> Kích hoạt Phosphatase khử phosphat bất hoạt HSL và kích hoạt PDE3B giáng hóa cAMP; chặn đứng hoàn toàn sự ly giải mỡ (tác dụng chống tạo ceton mạnh mẽ).",
        "<b>Enzym Lipoprotein Lipase (LPL) tại mao mạch mô mỡ —</b> Thủy phân Triglycerid từ Chylomicron và VLDL máu giải phóng acid béo để mô mỡ hấp thu este hóa tích trữ.",
        "<b>Kích hoạt LPL bởi Insulin —</b> Insulin kích thích mạnh mẽ sự tổng hợp và chuyển vị LPL ra nội mô mao mạch mô mỡ, dồn toàn bộ lipid thức ăn vào kho dự trữ mỡ dưới da."
    ],
    "Insulin là người bảo vệ kho mỡ tuyệt đối: nó vừa kích thích LPL nạp mỡ vào kho, vừa khóa chặt enzym HSL không cho một giọt acid béo nào thoát ra ngoài."
))

cards.append(make_card(
    "HS13-B7-12",
    "Cơ chế Phân tử của Kháng Insulin (Insulin Resistance)",
    "CƠ CHẾ ĐỀ KHÁNG INSULIN",
    "Các rối loạn phân tử nội bào cắt đứt dòng thác tín hiệu Insulin trong cơ chế bệnh sinh của Đái tháo đường Typ 2?",
    [
        "<b>Tích tụ chất trung gian Lipid —</b> Nồng độ acid béo tự do (FFA) máu cao kéo dài dẫn đến lắng đọng mỡ dị vị trong tế bào cơ và gan, làm tích tụ Diacylglycerol (DAG) và Ceramide.",
        "<b>Kích hoạt các Isoform PKC bất thường —</b> DAG hoạt hóa protein kinase C mới (PKC-theta ở cơ, PKC-epsilon ở gan) và các stress kinase (JNK, IKK-beta).",
        "<b>Phosphoryl hóa sai lệch trên gốc Serin/Threonin của IRS-1 —</b> Các kinase này phosphoryl hóa các gốc Ser/Thr trên IRS-1 (thay vì gốc Tyrosin chuẩn), làm biến dạng IRS-1.",
        "<b>Cắt đứt tín hiệu PI3K/Akt —</b> Phospho-Ser-IRS-1 mất khả năng tuyển mộ p85 của PI3K, triệt tiêu dòng thác tín hiệu Akt; kênh GLUT4 không thể chuyển vị ra màng tế bào cơ.",
        "<b>Mất ức chế FoxO1 tại gan —</b> Gan tiếp tục tân tạo glucose vô tổ chức ngay cả khi nồng độ insulin máu tăng cao, gây tăng đường huyết nghịch lý lúc đói."
    ],
    "Đề kháng insulin là bản chất cốt lõi của hội chứng chuyển hóa và đái tháo đường typ 2; hiểu rõ cơ chế phosphoryl hóa Ser/Thr trên IRS-1 mở ra các đích thuốc mới cải thiện độ nhạy cảm insulin."
))

cards.append(make_card(
    "HS13-B7-13",
    "Bệnh sinh Nhiễm toan Ceton do Đái tháo đường (Diabetic Ketoacidosis - DKA)",
    "CƠ CHẾ NHIỄM TOAN CETON",
    "Chuỗi phản ứng sinh hóa giải thích vì sao thiếu hụt Insulin tuyệt đối trong Đái tháo đường Typ 1 lại kích hoạt bùng nổ thể Ceton?",
    [
        "<b>Thiếu hụt Insulin tuyệt đối —</b> Tế bào beta đảo tụy bị tự miễn phá hủy hoàn toàn; tỷ số Insulin/Glucagon tụt dốc thảm hại.",
        "<b>Giải phóng phanh hãm enzym HSL —</b> Mất tác dụng ức chế của insulin khiến enzym HSL tại mô mỡ hoạt động cực đại, phân giải ồ ạt triglycerid phóng thích dòng thác acid béo tự do (FFA) về gan.",
        "<b>Kích hoạt kênh vận chuyển CPT-1 —</b> Nồng độ Malonyl-CoA tại gan giảm mạnh giải phóng ức chế đối với Carnitine Palmitoyltransferase-1 (CPT-1); acid béo ồ ạt tràn vào ty thể thực hiện beta-oxy hóa.",
        "<b>Ứ đọng lượng khổng lồ Acetyl-CoA —</b> Beta-oxy hóa sản sinh lượng Acetyl-CoA vượt xa khả năng dung nạp của chu trình Krebs (vốn đang cạn kiệt Oxaloacetat do bị rút đi tân tạo đường).",
        "<b>Bùng nổ sinh tổng hợp thể Ceton —</b> Acetyl-CoA dư thừa chuyển hướng tạo Acetoacetat, beta-Hydroxybutyrat và Aceton qua enzym HMG-CoA Synthase ty thể; các acid này phân ly giải phóng ion H+ gây toan chuyển hóa nặng (Anion Gap tăng vọt) đe dọa tính mạng."
    ],
    "DKA là thảm họa chuyển hóa sinh ra do sự mất kiểm soát phân giải lipid ở mô mỡ kết hợp với sự tăng tốc tạo ceton tại gan khi thiếu vắng hoàn toàn tín hiệu Insulin."
))

# ==============================================================================
# SECTION B_ALGO: 5 THUẬT TOÁN QUYẾT ĐỊNH (HS13-ALGO-01 -> HS13-ALGO-05)
# ==============================================================================

cards.append(make_card(
    "HS13-ALGO-01",
    "Phân tầng Chẩn đoán Rối loạn Tuyến Nội tiết (Nguyên phát vs Thứ phát)",
    "THUẬT TOÁN ĐỊNH VỊ TỔN THƯƠNG",
    "Lưu đồ thuật toán phân tầng chẩn đoán rối loạn chức năng tuyến nội tiết dựa trên cặp xét nghiệm Hormon Tuyến yên và Tuyến đích?",
    [
        "<b>Nhánh 1 (Lệch chiều - Giảm Hormon đích + Tăng Hormon yên) —</b> Suy tuyến NGUYÊN PHÁT tại tuyến đích do mất feedback âm tính (ví dụ TSH tăng rất cao + FT4 giảm thấp = Suy giáp nguyên phát Hashimoto; ACTH tăng cao + Cortisol giảm thấp = Suy vỏ thượng thận nguyên phát Addison).",
        "<b>Nhánh 2 (Lệch chiều - Tăng Hormon đích + Giảm/Triệt tiêu Hormon yên) —</b> Cường tuyến NGUYÊN PHÁT tại tuyến đích (ví dụ FT4/FT3 tăng vọt + TSH <0,01 µIU/mL = Cường giáp Basedow hoặc u độc tuyến giáp; Cortisol tăng vọt + ACTH <5 pg/mL = U vỏ thượng thận tiết cortisol độc lập).",
        "<b>Nhánh 3 (Cùng chiều - Giảm Hormon đích + Giảm/Bình thường Hormon yên) —</b> Suy tuyến THỨ PHÁT tại tuyến yên hoặc vùng hạ đồi (ví dụ TSH thấp/bình thường + FT4 thấp = Suy giáp thứ phát do u tuyến yên/hoại tử Sheehan; ACTH thấp + Cortisol thấp = Suy thượng thận thứ phát do dùng thuốc corticoid kéo dài).",
        "<b>Nhánh 4 (Cùng chiều - Tăng Hormon đích + Tăng Hormon yên) —</b> Cường tuyến THỨ PHÁT do u tuyến yên tăng tiết hormon hướng tuyến hoặc đề kháng hormon (ví dụ TSH tăng + FT4 tăng = U tuyến yên tiết TSH TSH-oma hoặc đề kháng hormon giáp RTH; ACTH tăng + Cortisol tăng = Bệnh Cushing do Adenoma tuyến yên tiết ACTH).",
        "<b>Quyết định định hướng cận lâm sàng —</b> Khi tổn thương Nguyên phát: chụp siêu âm/CT/MRI tập trung tại tuyến đích; Khi tổn thương Thứ phát: bắt buộc chỉ định chụp MRI tuyến yên và sọ não có tiêm thuốc đối từ."
    ],
    "Thuật toán cặp xét nghiệm hướng tuyến/tuyến đích là kim chỉ nam tối thượng trong thực hành nội tiết học, giúp phân định chính xác tầng gốc rễ bệnh sinh trong vòng 1 nốt nhạc.",
    algo=True
))

cards.append(make_card(
    "HS13-ALGO-02",
    "Thuật toán Phân loại 5 Con đường Truyền tin Màng Tế bào",
    "THUẬT TOÁN CON ĐƯỜNG TRUYỀN TIN",
    "Lưu đồ phân nhánh nhận diện và lựa chọn con đường truyền tin thứ hai của các hormon màng tế bào?",
    [
        "<b>Nhánh 1 (Con đường Gs - Adenylate Cyclase - cAMP - PKA) —</b> Hormon kích thích: Glucagon, Adrenalin (beta-1, beta-2), ACTH, TSH, LH, FSH, PTH, Calcitonin, ADH (V2) → Kích hoạt AC → Tăng cAMP → Kích hoạt PKA → Phosphoryl hóa Ser/Thr trên enzym đích và kích hoạt yếu tố phiên mã CREB.",
        "<b>Nhánh 2 (Con đường Gi - Ức chế Adenylate Cyclase) —</b> Hormon ức chế: Somatostatin, Adrenalin/Noradrenalin (alpha-2), Acetylcholin (M2), Adenosin (A1) → Ức chế AC → Giảm nồng độ cAMP nội bào.",
        "<b>Nhánh 3 (Con đường Gq - Phospholipase C - IP3/DAG - Canxi - PKC) —</b> Phối tử: Oxytocin, ADH (V1), Angiotensin II (AT1), Noradrenalin (alpha-1), TRH, GnRH → Kích hoạt PLC-beta cắt PIP2 tạo IP3 (mở kênh Ca2+ lưới nội chất) và DAG (phối hợp Ca2+ hoạt hóa PKC và Ca2+-Calmodulin kích hoạt MLCK).",
        "<b>Nhánh 4 (Con đường Tyrosine Kinase Nội tại - RTK) —</b> Phối tử: Insulin, IGF-1, EGF, PDGF, VEGF → Nhị hợp hóa, tự phosphoryl hóa chéo Tyrosin → Tuyển mộ IRS-1 kích hoạt nhánh PI3K/Akt (chuyển GLUT4, tổng hợp glycogen) và nhánh Ras/MAPK (phân bào, sinh trưởng).",
        "<b>Nhánh 5 (Con đường Tuyển mộ Kinase - JAK/STAT) —</b> Phối tử: GH, Prolactin, EPO, Leptin, Cytokine → Thụ thể không có kinase nội tại tuyển mộ Janus Kinase (JAK) phosphoryl hóa đuôi thụ thể → STAT bám vào bị phosphoryl hóa → STAT dimer hóa chuyển thẳng vào nhân kích hoạt phiên mã gen."
    ],
    "Lưu đồ thuật toán 5 nhánh bao quát toàn bộ thế giới thụ thể bề mặt màng tế bào của cơ thể người, giúp liên kết logic giữa bản chất phân tử hormon và đáp ứng sinh lý tương ứng.",
    algo=True
))

cards.append(make_card(
    "HS13-ALGO-03",
    "Phân tầng Chẩn đoán Hội chứng Cushing (Bệnh Cushing vs U Thượng Thận vs ACTH Lạc chỗ)",
    "THUẬT TOÁN HỘI CHỨNG CUSHING",
    "Lưu đồ thuật toán phân tầng chẩn đoán xác định và phân biệt nguyên nhân Hội chứng Cushing qua các nghiệm pháp Dexamethasone?",
    [
        "<b>Bước 1 (Xác định tình trạng thừa Cortisol) —</b> Cortisol tự do nước tiểu 24 giờ tăng cao; HOẶC Cortisol nước bọt nửa đêm (23h) tăng; HOẶC Nghiệm pháp Dexamethasone liều thấp qua đêm (1 mg lúc 23h): Cortisol máu sáng 8h không bị ức chế (vẫn >50 nmol/L hay >1,8 µg/dL) → Khẳng định Hội chứng Cushing.",
        "<b>Bước 2 (Định lượng nồng độ ACTH huyết tương 8h) —</b> Phân biệt phụ thuộc ACTH vs không phụ thuộc ACTH: ACTH bị ức chế (<5 pg/mL) → Hội chứng Cushing KHÔNG phụ thuộc ACTH; ACTH bình thường cao hoặc tăng (>15 - 20 pg/mL) → Hội chứng Cushing PHỤ THUỘC ACTH.",
        "<b>Bước 3 (Nhánh ACTH thấp - Không phụ thuộc ACTH) —</b> Nguyên nhân tại vỏ thượng thận: U tuyến vỏ thượng thận (Adenoma) hoặc Ung thư vỏ thượng thận (Carcinoma) → Chỉ định chụp CT ổ bụng thượng thận.",
        "<b>Bước 4 (Nhánh ACTH cao - Nghiệm pháp Dexamethasone liều cao 8 mg qua đêm) —</b> Phân biệt Bệnh Cushing tuyến yên vs U tiết ACTH lạc chỗ: Nếu Cortisol máu sáng bị ức chế >50% so với mức nền → BỆNH CUSHING TUYẾN YÊN (Cushing's disease, u tuyến yên vẫn giữ được thụ thể glucocorticoid nhưng có ngưỡng ức chế cao hơn) → Chỉ định chụp MRI tuyến yên.",
        "<b>Bước 5 (Nhánh ACTH cao - Không bị ức chế bởi liều cao) —</b> Nếu Cortisol hoàn toàn KHÔNG bị ức chế bởi Dexamethasone liều cao 8 mg → HỘI CHỨNG TIẾT ACTH LẠC CHỖ (Ectopic ACTH, thường do ung thư phổi tế bào nhỏ SCLC hoặc u carcinoid phế quản) → Chỉ định chụp CT ngực bụng tìm ổ ung thư."
    ],
    "Thuật toán Dexamethasone hai tầng (liều thấp khẳng định chẩn đoán, liều cao định vị nguyên nhân) là kinh điển tuyệt đối trong chẩn đoán phân biệt hội chứng nội tiết phức tạp nhất trên lâm sàng.",
    algo=True
))

cards.append(make_card(
    "HS13-ALGO-04",
    "Bản đồ Sinh tổng hợp Steroid và Phân biệt 3 Thể Thiếu Enzym trong CAH",
    "THUẬT TOÁN TĂNG SẢN THƯỢNG THẬN",
    "Lưu đồ thuật toán phân biệt Tăng sinh tuyến thượng thận bẩm sinh (CAH) do thiếu 21-OH vs 11beta-OH vs 17alpha-OH dựa trên Huyết áp, 17-OHP và Kali máu?",
    [
        "<b>Nhánh 1 (Thiếu 21-Hydroxylase - Chiếm >90% trường hợp) —</b> Sinh hóa: Nồng độ 17-OH-Progesterone tăng vọt cực cao; Thiếu cả Aldosteron và Cortisol; Dư thừa Androgen → Lâm sàng: BÉ GÁI NAM HÓA + MẤT MUỐI, TỤT HUYẾT ÁP, TĂNG KALI MÁU, toan chuyển hóa.",
        "<b>Nhánh 2 (Thiếu 11beta-Hydroxylase - Chiếm 5 - 8% trường hợp) —</b> Sinh hóa: Tắc nghẽn bước chuyển 11-DOC thành Corticosteron và 11-Deoxycortisol thành Cortisol; Ứ đọng lượng lớn 11-Deoxycorticosteron (11-DOC) vốn là một mineralocorticoid yếu; Dư thừa Androgen → Lâm sàng: BÉ GÁI NAM HÓA + TĂNG HUYẾT ÁP, HẠ KALI MÁU (do tác dụng giữ muối nước của 11-DOC tích tụ).",
        "<b>Nhánh 3 (Thiếu 17alpha-Hydroxylase - Chiếm <1% trường hợp) —</b> Sinh hóa: Không tổng hợp được Cortisol và KHÔNG TỔNG HỢP ĐƯỢC ANDROGEN/ESTROGEN; Toàn bộ cơ chất dồn sang lớp Cầu tạo dư thừa Corticosteron và 11-DOC → Lâm sàng: TĂNG HUYẾT ÁP, HẠ KALI MÁU + BÉ TRAI KHÔNG NAM HÓA ĐƯỢC (lưỡng giới giả nữ, cơ quan sinh dục ngoài dạng nữ) + BÉ GÁI KHÔNG DẬY THÌ.",
        "<b>Quy tắc tam giác chẩn đoán nhanh —</b> Nam hóa + Tụt huyết áp = Thiếu 21-OH; Nam hóa + Tăng huyết áp = Thiếu 11beta-OH; Không nam hóa / Kiểu hình nữ + Tăng huyết áp = Thiếu 17alpha-OH.",
        "<b>Chỉ số sàng lọc then chốt —</b> Đo 17-OHP máu gót chân phát hiện ngay lập tức thể thiếu 21-OH phổ biến nhất để bắt đầu bù Hydrocortison và Fludrocortison cứu sống trẻ."
    ],
    "Quy tắc tam giác lâm sàng (Nam hóa vs Huyết áp) giải mã hoàn hảo 3 dạng khiếm khuyết enzym bẩm sinh phức tạp trong chuỗi chuyển hóa steroid vỏ thượng thận.",
    algo=True
))

cards.append(make_card(
    "HS13-ALGO-05",
    "Lưu đồ Điều hòa Phân tử Đối kháng Insulin vs Glucagon",
    "THUẬT TOÁN ĐIỀU HÒA ĐƯỜNG HUYẾT",
    "Lưu đồ thuật toán đối kháng phân tử giữa Insulin và Glucagon qua trạng thái phosphoryl hóa của các enzym then chốt?",
    [
        "<b>Trạng thái No (Insulin chiếm ưu thế) —</b> Kích hoạt thụ thể RTK → PI3K/Akt → Kích hoạt Protein Phosphatase-1 (PP-1) → CẮT GỐC PHOSPHAT KHỎI TẤT CẢ ENZYM (Khử Phosphat).",
        "<b>Các enzym BẬT ở trạng thái khử phosphat —</b> Glycogen Synthase (hoạt động tăng tạo glycogen), PFK-2 (hoạt động tăng F-2,6-BP kích thích PFK-1 đường phân), Pyruvate Dehydrogenase (hoạt động nạp Acetyl-CoA vào Krebs), Acetyl-CoA Carboxylase (hoạt động tạo mỡ).",
        "<b>Các enzym TẮT ở trạng thái khử phosphat —</b> Glycogen Phosphorylase (bất hoạt ngừng thoái hóa glycogen), FBPase-2 (bất hoạt), Hormone-Sensitive Lipase (bất hoạt ngừng phân giải mỡ).",
        "<b>Trạng thái Đói (Glucagon chiếm ưu thế) —</b> Kích hoạt GPCR Gs → Tăng cAMP → Kích hoạt Protein Kinase A (PKA) → GẮN GỐC PHOSPHAT LÊN TẤT CẢ ENZYM (Phosphoryl hóa).",
        "<b>Các enzym BẬT ở trạng thái gắn phosphat —</b> Glycogen Phosphorylase (hoạt động giải phóng glucose-1-P), FBPase-2 (hoạt động hạ F-2,6-BP kích hoạt tân tạo đường), HSL (hoạt động ly giải mỡ tạo thể ceton).",
        "<b>Quyết định chuyển hóa hệ thống —</b> Chuyển đổi trạng thái phosphoryl hóa của các enzym then chốt đóng vai trò là chiếc công tắc phân tử hoàn hảo chuyển đổi cơ thể giữa chế độ 'tích trữ năng lượng' (No) và 'huy động năng lượng' (Đói)."
    ],
    "Đây là thuật toán tổng kết cốt tử của môn Hóa sinh Y học: chiếc cầu nối logic gắn kết chặt chẽ tín hiệu hormon màng tế bào với mạng lưới chuyển hóa năng lượng toàn cơ thể.",
    algo=True
))

# Save cards
out_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/14_Hoa sinh/HS-13_Hoa_sinh_hormon/HS-13_Hoa_sinh_hormon.cards.v2.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(cards)} cards for HS-13 into {out_path.name}")
