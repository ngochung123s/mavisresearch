# -*- coding: utf-8 -*-
"""build_deep_hs07.py - Generate 76 exhaustive master flashcards for HS-07 (Protein & Hemoglobin)"""
import json
import re
from pathlib import Path

def clean_label(t):
    # Ensure items don't have colons that trigger G_ASKS_MISSING
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
        "extra": extra or "Nguồn: Giáo trình Hóa Sinh Y Học - Bộ môn Hóa sinh ĐHYHN, Lehninger Principles of Biochemistry 8th ed, Harper's Illustrated Biochemistry 32nd ed.",
        "tags": ["hoasinh", "HS07", section]
    }

cards = []

# ==============================================================================
# SECTION B1: 20 ACID AMIN TIÊU CHUẨN (15 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B1-01",
    "Cấu trúc chung của L-α-acid amin",
    "CẤU TRÚC PHÂN TỬ ACID AMIN",
    "Trình bày cấu tạo chung của một L-α-acid amin tiêu chuẩn và vai trò của 4 nhóm thế gắn trên carbon α?",
    [
        "<b>Carbon trung tâm Cα —</b> Là nguyên tử carbon bất đối xứng (trừ Glycin), liên kết cộng hóa trị đồng thời với 4 nhóm thế khác nhau trong không gian 3 chiều.",
        "<b>Nhóm carboxyl mang tính acid (-COOH) —</b> Có pK1 dao động từ 1,8 đến 2,4; ở pH sinh lý 7,4 phân ly mất proton thành ion carboxylat (-COO⁻).",
        "<b>Nhóm amin mang tính base (-NH2) —</b> Có pK2 dao động từ 8,8 đến 10,6; ở pH sinh lý 7,4 nhận thêm proton biến thành ion amoni (-NH3⁺).",
        "<b>Nguyên tử Hydro (-H) và Chuỗi bên biến thiên (-R) —</b> Chuỗi R quyết định toàn bộ đặc tính lý hóa độc nhất (tính phân cực, điện tích, kích thước, độ kỵ nước) và hoạt tính sinh học của từng acid amin."
    ],
    "Tất cả 20 acid amin tiêu chuẩn đều là α-acid amin vì nhóm amin gắn trực tiếp vào nguyên tử carbon ngay sát nhóm carboxyl (Cα). Ở pH sinh lý nội bào 7,4, phân tử luôn tồn tại ở dạng ion lưỡng cực (Zwitterion) với cả hai nhóm -COO⁻ và -NH3⁺ đều mang điện tích."
))

cards.append(make_card(
    "HS07-B1-02",
    "Đồng phân quang học và quy luật tiến hóa",
    "ĐỒNG PHÂN QUANG HỌC ACID AMIN",
    "Phân tích đặc tính đồng phân quang học của các acid amin tiêu chuẩn và nêu quy luật cấu tạo protein trong tế bào người?",
    [
        "<b>Carbon bất đối xứng (C*) —</b> 19 trong số 20 acid amin có ít nhất 1 carbon bất đối Cα gắn 4 nhóm khác nhau nên có tính hoạt quang (quay mặt phẳng ánh sáng phân cực).",
        "<b>Hai trường hợp đặc biệt về C* —</b> Glycin không có C* (chuỗi R là -H, Cα gắn 2 nguyên tử H nên không hoạt quang); Isoleucin và Threonin có tới 2 trung tâm bất đối (Cα và 1 carbon trên chuỗi R).",
        "<b>Quy ước Fischer dạng L —</b> Dạng L-enantiomer có nhóm -NH3⁺ nằm ở bên trái Cα khi mạch chính đặt thẳng đứng với nhóm -COO⁻ ở trên đỉnh (tương ứng cấu hình L-glyceraldehyd).",
        "<b>Quy luật tiến hóa sinh học —</b> Toàn bộ protein trong tế bào người và sinh vật bậc cao đều cấu tạo ĐỘC QUYỀN từ L-α-acid amin; D-acid amin chỉ xuất hiện hãn hữu ở vách tế bào vi khuẩn hoặc kháng sinh peptit phi ribosome."
    ],
    "Cơ chế ribosome và các enzym aminoacyl-tRNA synthetase trong sinh vật bậc cao có tính đặc hiệu lập thể tuyệt đối 100% với dạng L. Nếu một D-acid amin lọt vào chuỗi polypeptid, nó sẽ làm gãy góc liên kết và phá vỡ hoàn toàn cấu trúc bậc 2 và bậc 3 của protein."
))

cards.append(make_card(
    "HS07-B1-03",
    "Cấu trúc dị vòng đặc biệt của Prolin",
    "IMINO ACID ĐẶC BIỆT",
    "Phân tích cấu trúc phân tử đặc biệt của Prolin và giải thích vì sao Prolin đóng vai trò phá vỡ cấu trúc xoắn α?",
    [
        "<b>Bản chất là α-imino acid —</b> Prolin không phải là amin bậc 1 thông thường mà là một amin bậc 2 (imino acid) với nhóm amin thứ cấp.",
        "<b>Vòng dị vòng pyrrolidin 5 cạnh —</b> Chuỗi bên aliphatic gồm 3 carbon uốn cong vòng lại và liên kết cộng hóa trị ngược vào nguyên tử Nitơ của nhóm amin chính.",
        "<b>Hạn chế góc quay tự do N-Cα —</b> Vòng dị vòng cố định khóa cứng liên kết N-Cα, tạo nên nếp gập (conformational kink/bend) cưỡng bức trên khung xương polypeptid.",
        "<b>Thiếu Hydro amid tạo liên kết —</b> Khi tham gia liên kết peptid, nguyên tử Nitơ của Prolin không còn nguyên tử Hydro tự do để tạo liên kết hydro nội chuỗi, do đó đóng vai trò kẻ phá vỡ cấu trúc xoắn α (α-helix breaker)."
    ],
    "Prolin là acid amin duy nhất có chuỗi bên nối vòng với nhóm amin khung chính. Do thiếu H amid và có góc quay phi bị cố định ở khoảng -60°, Prolin không thể vừa vặn trong cấu trúc xoắn α đều đặn nhưng lại là thành phần cốt lõi của khúc cuộn β-turn và cấu trúc bộ ba xoắn collagen."
))

cards.append(make_card(
    "HS07-B1-04",
    "Nhóm 1: Acid amin không phân cực, kỵ nước",
    "PHÂN LOẠI ACID AMIN",
    "Kể tên 7 acid amin thuộc nhóm kỵ nước aliphat không phân cực và phân tích vai trò của hiệu ứng kỵ nước?",
    [
        "<b>7 acid amin nhóm 1 —</b> Glycin (Gly, G), Alanin (Ala, A), Valin (Val, V), Leucin (Leu, L), Isoleucin (Ile, I), Prolin (Pro, P), và Methionin (Met, M).",
        "<b>Bản chất chuỗi R —</b> Chuỗi hydrocacbon no mạch thẳng hoặc mạch nhánh, vòng pyrrolidin (Pro), hoặc liên kết thioether (Met), không có khả năng tạo liên kết hydro với nước.",
        "<b>Hiệu ứng kỵ nước (Hydrophobic Effect) —</b> Khi protein cuộn gập trong dịch nội bào, các chuỗi bên kỵ nước bị ép vùi sâu vào lõi bên trong để tránh tiếp xúc với nước.",
        "<b>Động lực nhiệt động học —</b> Sự vùi các gốc kỵ nước vào lõi giải phóng các phân tử nước có trật tự cao bao quanh chúng, làm tăng mạnh entropy toàn phần (ΔS > 0), là động lực then chốt làm bền cấu trúc 3 chiều của protein."
    ],
    "Hiệu ứng kỵ nước không phải là lực hút tĩnh điện mà là một hiện tượng nhiệt động học do entropy chi phối. Các gốc Val, Leu, Ile, Phe luôn tạo thành 'trọng tâm kỵ nước' (hydrophobic core) ổn định bên trong lòng các protein hình cầu tan trong nước."
))

cards.append(make_card(
    "HS07-B1-05",
    "Methionin và vai trò mở đầu dịch mã",
    "ACID AMIN CHỨA LƯU HUỲNH",
    "Trình bày cấu tạo chuỗi bên của Methionin và vai trò sinh học của nó trong sinh tổng hợp protein và chu trình methyl hóa?",
    [
        "<b>Cấu tạo chuỗi R —</b> Chứa liên kết thioether không phân cực: -CH2-CH2-S-CH3, mang nguyên tử lưu huỳnh ở vị trí δ bị che chắn bởi nhóm methyl.",
        "<b>Acid amin mở đầu dịch mã —</b> Codon khởi đầu AUG trên mARN mã hóa đặc hiệu cho Methionin (ở sinh vật nhân thực) hoặc N-formylmethionin (fMet ở vi khuẩn và ty thể).",
        "<b>Tiền chất của S-Adenosylmethionin (SAM) —</b> Phản ứng kết hợp Methionin với ATP tạo SAM, chất nhượng nhóm methyl (-CH3) hoạt hóa vạn năng cho các phản ứng methyl hóa ADN, ARN, phospholipid và tổng hợp adrenalin/creatin.",
        "<b>Không tạo cầu disulfur —</b> Do nguyên tử lưu huỳnh đã bị methyl hóa thành thioether (-S-CH3), Methionin hoàn toàn không có nhóm thiol (-SH) tự do nên không thể tạo cầu nối disulfur như Cystein."
    ],
    "Methionin là 1 trong 8 acid amin thiết yếu. Trong lâm sàng, con đường chuyển hóa Methionin tạo chất trung gian Homocystein; tăng homocystein máu do thiếu vitamin B12/folat hoặc đột biến enzym là yếu tố nguy cơ độc lập gây xơ vữa động mạch và huyết khối tắc mạch."
))

cards.append(make_card(
    "HS07-B1-06",
    "Axit amin chuỗi nhánh (BCAA) và bệnh MSUD",
    "CHUYỂN HÓA ACID AMIN MẠCH NHÁNH",
    "Kể tên 3 acid amin chuỗi nhánh (BCAA), nêu vị trí chuyển hóa chủ yếu và bệnh lý di truyền kinh điển liên quan?",
    [
        "<b>3 acid amin chuỗi nhánh BCAA —</b> Valin (Val, V), Leucin (Leu, L), và Isoleucin (Ile, I); đều là các acid amin thiết yếu có chuỗi bên hydrocacbon phân nhánh kỵ nước.",
        "<b>Chuyển hóa ưu thế tại cơ xương —</b> Khác với đa số acid amin khác bị thoái hóa tại gan, BCAA được chuyển hóa oxy hóa chủ yếu tại mô cơ xương nhờ enzym Branched-Chain Aminotransferase (BCAT) giàu ở cơ.",
        "<b>Bệnh nước tiểu siro phong (MSUD — Maple Syrup Urine Disease) —</b> Bệnh di truyền lặn trên NST thường do thiếu hụt phức hợp enzym Branched-Chain α-Keto Acid Dehydrogenase (BCKDH).",
        "<b>Hậu quả lâm sàng MSUD —</b> Ứ đọng nghiêm trọng Val, Leu, Ile và các dẫn xuất α-keto tương ứng trong máu và dịch não tủy, gây nước tiểu có mùi ngọt siro cây phong đặc trưng, nhiễm toan ceton, chậm phát triển trí tuệ nặng và tử vong sớm nếu không điều trị ăn kiêng kịp thời."
    ],
    "Leucin là acid amin thuần túy sinh ceton (ketogenic), trong khi Valin thuần túy sinh đường (glucogenic) và Isoleucin vừa sinh đường vừa sinh ceton. Trong suy gan mạn tính, tỷ lệ BCAA/AAA (Fischer's ratio) giảm thấp dự báo hội chứng não gan."
))

cards.append(make_card(
    "HS07-B1-07",
    "Nhóm 2: Acid amin có chuỗi bên nhân thơm",
    "PHÂN LOẠI ACID AMIN",
    "Nêu tên 3 acid amin có nhân thơm và so sánh đặc tính phân cực, chức năng sinh học của từng acid amin?",
    [
        "<b>3 acid amin nhân thơm —</b> Phenylalanin (Phe, F), Tyrosin (Tyr, Y), và Tryptophan (Trp, W); đều chứa vòng thơm liên hợp hấp thụ ánh sáng tử ngoại.",
        "<b>Phenylalanin (Phe) —</b> Chứa vòng benzen gắn vào -CH2-, kỵ nước mạnh nhất trong 3 chất; là tiền chất tổng hợp Tyrosin nhờ enzym Phenylalanin Hydroxylase (thiếu hụt gây bệnh Phenylceton niệu PKU).",
        "<b>Tyrosin (Tyr) —</b> Có thêm nhóm hydroxyl phenolic (-OH) với pKR = 10,07; có tính phân cực nhẹ, là vị trí tiếp nhận phản ứng phosphoryl hóa điều hòa tín hiệu bởi thụ thể Tyrosine Kinase, tiền chất tạo Melanin, Dopamin, Noradrenalin, Adrenalin và hormon tuyến giáp T3/T4.",
        "<b>Tryptophan (Trp) —</b> Chứa dị vòng indol lưỡng vòng cồng kềnh; là acid amin thơm lớn nhất, tiền chất sinh tổng hợp chất dẫn truyền thần kinh Serotonin, hormon Melatonin và một phần Vitamin B3 (Niacin)."
    ],
    "Phenylalanin và Tryptophan là 2 acid amin thiết yếu tuyệt đối. Tyrosin là acid amin bán thiết yếu vì cơ thể người có thể tự tổng hợp được từ Phenylalanin nhờ enzym Phenylalanine Hydroxylase (PAH) phụ thuộc coenzym Tetrahydrobiopterin (BH4)."
))

cards.append(make_card(
    "HS07-B1-08",
    "Đặc tính hấp thụ tử ngoại UV ở bước sóng 280 nm",
    "QUANG PHỔ TỬ NGOẠI PROTEIN",
    "Giải thích cơ sở hóa lý của phương pháp định lượng protein toàn phần bằng quang phổ tử ngoại ở bước sóng 280 nm?",
    [
        "<b>Bản chất hiện tượng —</b> Các electron π bất định xứ trong vòng nhân thơm liên hợp của Tryptophan và Tyrosin (và một phần rất nhỏ Phenylalanin) hấp thụ mạnh photon ánh sáng tử ngoại vùng 260 - 280 nm.",
        "<b>Đỉnh hấp thụ cực đại λ = 280 nm —</b> Tryptophan có độ hấp thụ phân tử lớn nhất, kế đến là Tyrosin; đỉnh hấp thụ cực đại của đa số protein tự nhiên nằm đúng tại bước sóng 280 nm (A280).",
        "<b>Ứng dụng định luật Beer-Lambert —</b> Mật độ quang A280 tỷ lệ thuận trực tiếp với nồng độ protein trong dung dịch: A280 = ε × b × c (ε là hệ số hấp thụ phân tử, b là bề dày cuvet, c là nồng độ).",
        "<b>Phân biệt với Acid Nucleic (A260) —</b> Acid nucleic (ADN/ARN) hấp thụ cực đại ở λ = 260 nm do các base nitơ purin/pyrimidin; tỷ số A260/A280 được dùng làm chỉ số chuẩn đánh giá độ tinh sạch của chế phẩm protein hoặc ADN."
    ],
    "Ưu điểm vượt trội của phương pháp đo A280 là nhanh chóng, không phá hủy mẫu protein và không cần dùng hóa chất tạo màu. Tuy nhiên, nếu protein không chứa gốc Trp hoặc Tyr (như gelatin/collagen) thì phương pháp đo A280 hoàn toàn mất tác dụng."
))

cards.append(make_card(
    "HS07-B1-09",
    "Nhóm 3: Acid amin phân cực, không tích điện",
    "PHÂN LOẠI ACID AMIN",
    "Kể tên 5 acid amin thuộc nhóm phân cực không tích điện ở pH 7.4 và nêu các nhóm chức phân cực đặc trưng?",
    [
        "<b>5 acid amin nhóm 3 —</b> Serin (Ser, S), Threonin (Thr, T), Cystein (Cys, C), Asparagin (Asn, N), và Glutamin (Gln, Q).",
        "<b>Serin và Threonin —</b> Chứa nhóm hydroxyl phân cực (-OH); làm tăng tính ưa nước của protein và là vị trí gắn nhóm phosphat điều hòa tín hiệu nội bào.",
        "<b>Cystein —</b> Chứa nhóm sulfhydryl (thiol, -SH, pKR ≈ 8,18); phân cực yếu, có tính khử mạnh và khả năng tạo cầu nối disulfur.",
        "<b>Asparagin và Glutamin —</b> Chứa nhóm chức amid tương ứng (-CONH2) của acid aspartic và acid glutamic; nhóm amid có cực tính cao, tạo liên kết hydro mạnh nhưng không bị ion hóa ở pH sinh lý.",
        "<b>Vai trò tăng tính tan —</b> Các acid amin nhóm này thường phân bố trên bề mặt ngoài của protein hình cầu tiếp xúc với môi trường nước dịch thể, tạo vỏ hydrat hóa ổn định phân tử."
    ],
    "Khác với nhóm acid và base, chuỗi bên của Ser, Thr, Asn, Gln hoàn toàn không mang điện tích thực (+ hay -) ở pH sinh lý 7,4, mặc dù mật độ điện tích cục bộ phân bố không đều tạo nên các lưỡng cực vĩnh cửu có khả năng tạo liên kết hydro rất bền với nước."
))

cards.append(make_card(
    "HS07-B1-10",
    "Cystein, nhóm Thiol và Cầu nối Disulfur",
    "LIÊN KẾT CỘNG HÓA TRỊ TRONG PROTEIN",
    "Trình bày phản ứng tạo cầu nối disulfur giữa hai phân tử Cystein và nêu ý nghĩa sinh học làm bền cấu trúc protein?",
    [
        "<b>Nhóm Sulfhydryl (-SH) —</b> Chuỗi bên Cystein là -CH2-SH, có pKR ≈ 8,18; nhóm thiol dễ bị oxy hóa khử thuận nghịch.",
        "<b>Phương trình phản ứng tạo Cystin —</b> 2 Cys-SH + [O] ⇌ Cys-S-S-Cys (Cystin) + 2H⁺ + 2e⁻; hai phân tử Cystein kết hợp tạo thành phân tử Cystin liên kết bởi cầu disulfur (-S-S-).",
        "<b>Bản chất liên kết cộng hóa trị —</b> Cầu disulfur là LIÊN KẾT CỘNG HÓA TRỊ duy nhất tham gia làm bền cấu trúc không gian bậc 3 và bậc 4 của chuỗi polypeptid.",
        "<b>Ý nghĩa sinh học trên protein tiết —</b> Khóa chặt cấu trúc không gian của các protein hoạt động ngoài tế bào (Insulin gồm 2 cầu liên chuỗi và 1 cầu nội chuỗi, Kháng thể IgG, Albumin), giúp chống lại sự biến tính nhiệt và phân hủy bởi enzym protease ngoại bào."
    ],
    "Trong bào tương (môi trường khử giàu GSH), cầu disulfur hiếm khi tồn tại tự do vì bị khử thành -SH. Ngược lại, trong lòng lưới nội sinh chất (ER) có môi trường oxy hóa, enzym Protein Disulfide Isomerase (PDI) xúc tác tạo lập các cầu disulfur chính xác cho protein tiết."
))

cards.append(make_card(
    "HS07-B1-11",
    "Biến đổi sau dịch mã trên Serin, Threonin và Asparagin",
    "BIẾN ĐỔI SAU DỊCH MÃ (PTM)",
    "Nêu vai trò sinh học của các gốc Serin, Threonin và Asparagin trong các biến đổi sau dịch mã (PTM) trọng yếu?",
    [
        "<b>O-Phosphoryl hóa trên Serin và Threonin —</b> Nhóm -OH của Ser/Thr là cơ chất tiếp nhận nhóm phosphat (-PO4²⁻) từ ATP xúc tác bởi các enzym Serine/Threonine Kinase.",
        "<b>Ý nghĩa công tắc phân tử —</b> Việc gắn/tháo gốc phosphat tích điện âm làm thay đổi biến hình lập thể protein, hoạt hóa hoặc bất hoạt các enzym chuyển hóa (Glycogen Phosphorylase, Glycogen Synthase) và thụ thể truyền tin nội bào.",
        "<b>N-Glycosyl hóa trên Asparagin (Asn) —</b> Nhóm amid (-CONH2) của Asparagin nằm trong motif đồng thuận Asn-X-Ser/Thr là vị trí gắn chuỗi oligosaccharid trong lòng lưới nội sinh chất (ER).",
        "<b>Ý nghĩa glycoprotein —</b> Quyết định sự cuộn gập chính xác, bảo vệ protein khỏi bị phân hủy, định vị vận chuyển tới màng tế bào hoặc tiêu thể, và đóng vai trò kháng nguyên bề mặt nhận diện miễn dịch."
    ],
    "Sự kết hợp giữa O-phosphorylation (trên Ser, Thr, Tyr) và N-glycosylation (trên Asn) hoặc O-glycosylation (trên Ser, Thr) là cơ chế tinh vi bậc nhất của tế bào để đa dạng hóa chức năng của cùng một chuỗi polypeptid sau khi dịch mã từ mARN."
))

cards.append(make_card(
    "HS07-B1-12",
    "Nhóm 4: Acid amin kiềm tích điện dương ở pH 7.4",
    "PHÂN LOẠI ACID AMIN",
    "Kể tên 3 acid amin có tính kiềm, nêu cấu tạo nhóm chức chuỗi bên và giá trị pKR tương ứng?",
    [
        "<b>Lysin (Lys, K) —</b> Mang nhóm ε-amin mạch thẳng -CH2-CH2-CH2-CH2-NH3⁺ có pKR = 10,53; ở pH 7,4 nhóm này bị proton hóa hoàn toàn, tích điện dương (+1).",
        "<b>Arginin (Arg, R) —</b> Mang nhóm guanidino có pKR = 12,48; là acid amin có tính kiềm mạnh nhất, luôn tích điện dương (+1) bền vững trong mọi điều kiện sinh lý do điện tích dương được giải tỏa cộng hưởng trên 3 nguyên tử nitơ.",
        "<b>Histidin (His, H) —</b> Mang vòng dị vòng imidazol có pKR = 6,00; ở pH 7,4 chỉ có khoảng 4% ở dạng tích điện dương (+1) và 96% ở dạng trung hòa không tích điện (0).",
        "<b>Cầu muối ion tĩnh điện —</b> Các gốc Lys và Arg tích điện dương trên bề mặt protein liên kết với các gốc Asp và Glu tích điện âm tạo nên các cầu muối ion (salt bridges) làm bền cấu trúc protein."
    ],
    "Histon là các protein kiềm liên kết với ADN trong chất nhiễm sắc (chromatin). Chuỗi bên giàu Lysin và Arginin của Histon mang điện tích dương dày đặc tạo lực hút tĩnh điện cực mạnh với khung đường-phosphat mang điện tích âm của chuỗi xoắn kép ADN."
))

cards.append(make_card(
    "HS07-B1-13",
    "Histidin và vai trò hệ đệm acid-base sinh lý",
    "ĐỆM NỘI BÀO VÀ ENZYM",
    "Giải thích vì sao Histidin là acid amin duy nhất đóng vai trò chất đệm sinh lý tối ưu của cơ thể ở pH 7.4?",
    [
        "<b>Giá trị pKR gần sát pH sinh lý —</b> Vòng imidazol của Histidin có pKR = 6,00 (trong chuỗi polypeptid có thể dao động từ 6,0 đến 7,5 tùy môi trường vi mô lân cận), là acid amin duy nhất có pKR tiệm cận pH máu 7,35 - 7,45.",
        "<b>Khả năng nhận/nhả proton linh hoạt —</b> Ở pH sinh lý, vòng imidazol có thể dễ dàng nhận thêm một proton để trở thành cation mang điện dương hoặc nhả proton để trở thành dạng trung hòa mà không cần biến thiên pH quá lớn.",
        "<b>Hệ đệm chính trong phân tử Hemoglobin —</b> Hemoglobin chứa tới 38 gốc Histidin; sự thay đổi trạng thái proton hóa của các gốc Histidin (đặc biệt His146 chuỗi β) giúp hồng cầu đệm proton H⁺ sinh ra từ chuyển hóa mô.",
        "<b>Trung tâm hoạt động xúc tác enzym —</b> Nhờ khả năng vừa là chất cho proton vừa là chất nhận proton (xúc tác acid-base tổng quát), Histidin xuất hiện ở trung tâm hoạt động của hầu hết enzym tiêu hóa và chuyển hóa (như Chymotrypsin, Carbonic Anhydrase)."
    ],
    "Theo nguyên lý dung dịch đệm, một chất có khả năng đệm tối ưu khi pH môi trường nằm trong khoảng pKa ± 1. Do mọi acid amin khác đều có pKR quá acid (< 4,5) hoặc quá kiềm (> 10), chỉ duy nhất Histidin thỏa mãn điều kiện đệm acid-base ở pH sinh lý người."
))

cards.append(make_card(
    "HS07-B1-14",
    "Nhóm 5: Acid amin acid tích điện âm ở pH 7.4",
    "PHÂN LOẠI ACID AMIN",
    "Kể tên 2 acid amin có tính acid, nêu cấu tạo chuỗi bên, giá trị pKR và vai trò tạo cầu muối phối trí kim loại?",
    [
        "<b>2 acid amin có tính acid —</b> Aspartat (Asp, D) với chuỗi bên -CH2-COOH (pKR = 3,65) và Glutamat (Glu, E) với chuỗi bên -CH2-CH2-COOH (pKR = 4,25).",
        "<b>Điện tích thực ở pH sinh lý 7,4 —</b> Do pH 7,4 cao hơn rất nhiều so với pKR, cả hai nhóm carboxyl chuỗi bên đều phân ly hoàn toàn thành ion carboxylat (-COO⁻), mang điện tích âm (-1).",
        "<b>Tạo cầu muối ion tĩnh điện —</b> Thường nằm trên bề mặt ngoài của protein tan trong nước, liên kết ion mạnh với các gốc kiềm (Lys⁺, Arg⁺) để ổn định cấu trúc bậc 3 và bậc 4.",
        "<b>Phối trí ion kim loại hóa trị 2 —</b> Các nhóm -COO⁻ của Asp và Glu đóng vai trò phối tử chelate hóa hoàn hảo để giữ các ion kim loại như Mg²⁺, Ca²⁺, Fe²⁺/Fe³⁺, Zn²⁺ trong trung tâm hoạt động của enzym (như ADN Polymerase dùng 2 gốc Asp phối trí 2 ion Mg²⁺)."
    ],
    "Glutamat là chất dẫn truyền thần kinh kích thích phong phú nhất trong hệ thần kinh trung ương. Khi bị khử carboxyl bởi enzym Glutamat Decarboxylase (GAD phụ thuộc Vitamin B6), Glutamat chuyển thành GABA (gamma-aminobutyric acid), chất dẫn truyền thần kinh ức chế chính của não bộ."
))

cards.append(make_card(
    "HS07-B1-15",
    "Acid amin thiết yếu và acid amin đặc biệt (Sec, Hyp)",
    "DINH DƯỠNG VÀ ACID AMIN ĐẶC BIỆT",
    "Nêu danh sách 8 acid amin thiết yếu tuyệt đối ở người lớn, 2 acid amin bán thiết yếu và cấu tạo acid amin thứ 21 (Selenocystein)?",
    [
        "<b>8 acid amin thiết yếu tuyệt đối —</b> Valin, Leucin, Isoleucin, Methionin, Threonin, Phenylalanin, Tryptophan, Lysin (Mẹo nhớ kinh điển: TV TILL PM hoặc PVT TIM HaLL).",
        "<b>2 acid amin bán thiết yếu —</b> Arginin và Histidin; cơ thể tự tổng hợp được nhưng không đủ tốc độ đáp ứng nhu cầu phát triển cực lớn ở trẻ sơ sinh, trẻ nhỏ và giai đoạn hồi phục chấn thương.",
        "<b>4-Hydroxyprolin và 5-Hydroxylysin —</b> Hình thành nhờ hydroxyl hóa Pro và Lys trong ER nhờ enzym phụ thuộc Vitamin C và Fe²⁺; tạo liên kết hydro làm bền bộ ba xoắn collagen, thiếu Vitamin C gây bệnh Scorbut.",
        "<b>Selenocystein (Sec, U) - Acid amin thứ 21 —</b> Mã hóa bởi bộ ba UGA trên mARN với cấu trúc SECIS hairpin; chuỗi bên chứa nhóm selenol (-SeH) có thế oxy hóa khử thấp hơn thiol (-SH), là trung tâm xúc tác của Glutathione Peroxidase và Thioredoxin Reductase."
    ],
    "Cơ thể người thiếu các con đường enzym để tổng hợp khung carbon của các acid amin thiết yếu (như chuỗi nhánh của BCAA, nhân thơm của Phe/Trp, lưu huỳnh của Met). Thiếu hụt dù chỉ 1 acid amin thiết yếu trong khẩu phần ăn sẽ dẫn đến cân bằng nitơ âm tính và teo cơ suy dinh dưỡng Kwashiorkor."
))

# ==============================================================================
# SECTION B2: ĐIỆN LY, ĐIỂM ĐẲNG ĐIỆN (pI) VÀ ĐIỆN DI PROTEIN (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B2-01",
    "Bản chất lưỡng tính và dạng Zwitterion",
    "TÍNH CHẤT ĐIỆN LY ACID AMIN",
    "Định nghĩa ion lưỡng cực (Zwitterion) và phân tích trạng thái phân ly của acid amin theo pH môi trường?",
    [
        "<b>Định nghĩa Zwitterion (Dipolar ion) —</b> Là dạng phân tử mang đồng thời cả điện tích âm (-COO⁻) và điện tích dương (-NH3⁺) trên cùng một phân tử, tổng điện tích thực bằng 0.",
        "<b>Không tồn tại dạng phân tử trung hòa —</b> Trong dung dịch nước, acid amin không bao giờ tồn tại dưới dạng trung hòa không phân ly NH2-CHR-COOH.",
        "<b>Ở môi trường acid mạnh (pH < pK1) —</b> Nồng độ H⁺ cao ép nhóm carboxyl nhận proton thành -COOH, phân tử tồn tại chủ yếu ở dạng CATION tích điện dương (+1): H3N⁺-CHR-COOH.",
        "<b>Ở môi trường kiềm mạnh (pH > pK2) —</b> Nồng độ OH⁻ cao làm nhóm amoni mất proton thành -NH2, phân tử tồn tại chủ yếu ở dạng ANION tích điện âm (-1): H2N-CHR-COO⁻."
    ],
    "Phương trình cân bằng Henderson-Hasselbalch chi phối tỷ lệ giữa các dạng ion hóa: pH = pKa + log([Base liên hợp] / [Acid liên hợp]). Khi pH = pKa, nồng độ dạng cho proton bằng đúng nồng độ dạng nhận proton (tỷ lệ 1:1)."
))

cards.append(make_card(
    "HS07-B2-02",
    "Cân bằng ion và biến thiên điện tích theo pH",
    "CÂN BẰNG PHÂN LY ION",
    "Mô tả sơ đồ 2 nấc phân ly của một acid amin đơn giản và mối tương quan giữa nồng độ proton với điện tích thực?",
    [
        "<b>Sơ đồ cân bằng 2 nấc —</b> Cation (+1) ⇌ [pK1] ⇌ Zwitterion (0) ⇌ [pK2] ⇌ Anion (-1).",
        "<b>Nấc phân ly thứ nhất pK1 (-COOH) —</b> Thường nằm trong khoảng 1,8 đến 2,4; nhóm carboxyl có tính acid mạnh hơn acid acetic (pKa = 4,76) do lực hút electron của nhóm -NH3⁺ kế cận.",
        "<b>Nấc phân ly thứ hai pK2 (-NH3⁺) —</b> Thường nằm trong khoảng 8,8 đến 10,6; nhóm amoni nhường proton để chuyển thành nhóm amin tự do ở môi trường kiềm.",
        "<b>Quy luật di chuyển điện trường —</b> Ở pH < pI phân tử tích điện dương chạy về cực âm (Catot); ở pH > pI phân tử tích điện âm chạy về cực dương (Anot); ở pH = pI phân tử đứng yên không di chuyển."
    ],
    "Điện tích thực của phân tử acid amin biến thiên liên tục từ dương sang âm khi pH dung dịch tăng dần. Tại giá trị pH sinh lý máu (7,4), hầu hết các acid amin trung tính đều mang điện tích thực xấp xỉ bằng 0 nhưng hơi lệch nhẹ về phía anion âm."
))

cards.append(make_card(
    "HS07-B2-03",
    "Định nghĩa Điểm đẳng điện (pI - Isoelectric Point)",
    "ĐIỂM ĐẲNG ĐIỆN ACID AMIN",
    "Định nghĩa Điểm đẳng điện (pI) của acid amin/protein và nêu các đặc tính vật lý đặc trưng của phân tử tại giá trị pI?",
    [
        "<b>Định nghĩa Điểm đẳng điện (pI) —</b> Là giá trị pH của môi trường mà tại đó tổng điện tích thực (net charge) của phân tử bằng 0, nồng độ cation bằng đúng nồng độ anion.",
        "<b>Không di chuyển trong điện trường —</b> Dưới tác dụng của điện trường một chiều, tại pH = pI phân tử không di chuyển về cực dương (Anot) lẫn cực âm (Catot).",
        "<b>Độ tan đạt cực tiểu —</b> Tại pI, các phân tử không đẩy nhau tĩnh điện do triệt tiêu điện tích bề mặt, lực hút van der Waals chiếm ưu thế làm các phân tử dễ kết tụ và kết tủa nhất.",
        "<b>Độ nhớt và áp suất thẩm thấu thấp nhất —</b> Lớp vỏ hydrat hóa bao quanh phân tử mỏng nhất tại pI, làm giảm độ nhớt của dung dịch protein và hạ thấp áp suất thẩm thấu keo."
    ],
    "Ứng dụng lâm sàng và công nghệ: Phương pháp kết tủa đẳng điện (isoelectric precipitation) điều chỉnh pH dung dịch về đúng pI của protein mục tiêu để tách chiết và tinh sạch protein mà không làm biến tính cấu trúc bậc 1 của chúng."
))

cards.append(make_card(
    "HS07-B2-04",
    "Công thức tính pI cho acid amin có chuỗi R không ion hóa",
    "TÍNH TOÁN ĐIỂM ĐẲNG ĐIỆN",
    "Trình bày công thức tính điểm đẳng điện pI cho acid amin có chuỗi bên R không ion hóa và lấy ví dụ tính pI của Alanin?",
    [
        "<b>Hai nấc phân ly duy nhất —</b> Đối với 13 acid amin có chuỗi R không ion hóa (Gly, Ala, Val, Leu, Ile, Phe, Trp, Pro, Met, Ser, Thr, Asn, Gln), phân tử chỉ có 2 giá trị pKa là pK1 (-COOH) và pK2 (-NH3⁺).",
        "<b>Công thức tính pI —</b> pI là trung bình cộng của 2 giá trị pKa: pI = (pK1 + pK2) / 2.",
        "<b>Ví dụ Alanin —</b> Cho pK1 (-COOH) = 2,34 và pK2 (-NH3⁺) = 9,69.",
        "<b>Tính toán cụ thể —</b> pI = (2,34 + 9,69) / 2 = 12,03 / 2 = 6,015 ≈ 6,02."
    ],
    "Tại pH = 6,02, 100% phân tử Alanin tồn tại ở dạng Zwitterion (+H3N-CH(CH3)-COO⁻). Khi đưa Alanin vào dung dịch đệm có pH = 7,4 (pH > pI), Alanin sẽ mất một phần proton mang điện tích âm nhỏ và di chuyển chậm về cực dương Anot."
))

cards.append(make_card(
    "HS07-B2-05",
    "Công thức tính pI cho acid amin có tính acid (Asp, Glu)",
    "TÍNH TOÁN ĐIỂM ĐẲNG ĐIỆN",
    "Trình bày công thức tính pI cho các acid amin có tính acid và giải thích vì sao Glutamat mang điện tích âm ở pH sinh lý?",
    [
        "<b>3 nấc phân ly —</b> Chuỗi bên mang thêm nhóm carboxyl thứ hai (-COOH chuỗi R có giá trị pKR). Acid amin có 3 nấc phân ly tương ứng pK1, pKR và pK2.",
        "<b>Quy tắc chọn cặp pKa —</b> Dạng Zwitterion trung hòa điện tích (0) nằm kẹp giữa 2 nấc phân ly của 2 nhóm carboxyl có tính acid (pK1 và pKR).",
        "<b>Công thức tính pI acid —</b> pI = (pK1 + pKR) / 2.",
        "<b>Ví dụ Glutamat —</b> pK1 = 2,19; pKR = 4,25; pK2 = 9,67. Suy ra: pI = (2,19 + 4,25) / 2 = 6,44 / 2 = 3,22; do pI = 3,22 rất thấp so với pH sinh lý 7,4 (pH >> pI), Glutamat phân ly hoàn toàn mang điện tích âm (-1)."
    ],
    "Tương tự với Aspartat: pK1 = 1,88, pKR = 3,65, pK2 = 9,60 -> pI = (1,88 + 3,65)/2 = 2,77. Điểm đẳng điện của Asp và Glu cực kỳ thấp (< 3,3) giải thích vì sao trong điện di ở mọi môi trường đệm sinh lý, Asp và Glu luôn tích điện âm mạnh nhất và chạy nhanh nhất về cực dương Anot."
))

cards.append(make_card(
    "HS07-B2-06",
    "Công thức tính pI cho acid amin có tính base (Lys, Arg, His)",
    "TÍNH TOÁN ĐIỂM ĐẲNG ĐIỆN",
    "Trình bày công thức tính pI cho các acid amin có tính base và tính toán pI của Lysin và Histidin?",
    [
        "<b>Quy tắc chọn cặp pKa kiềm —</b> Trạng thái trung hòa điện tích (0) nằm kẹp giữa nấc phân ly của nhóm amin chuỗi bên (pKR) và nhóm α-amin (pK2).",
        "<b>Công thức tính pI base —</b> pI = (pKR + pK2) / 2.",
        "<b>Tính toán Lysin —</b> Cho pK1 = 2,18; pK2 = 8,95; pKR = 10,53. Suy ra pI = (8,95 + 10,53) / 2 = 19,48 / 2 = 9,74.",
        "<b>Tính toán Histidin —</b> Vòng imidazol có pKR = 6,00; pK2 (-NH3⁺) = 9,17; pK1 (-COOH) = 1,82. Suy ra pI = (6,00 + 9,17) / 2 = 15,17 / 2 = 7,59."
    ],
    "Với Arginin: pK2 = 9,04 và pKR = 12,48 -> pI = (9,04 + 12,48)/2 = 10,76. Do pI của Lysin (9,74) và Arginin (10,76) cao hơn rất nhiều so với pH 7,4 (pH << pI), cả hai acid amin này luôn nhận proton và mang điện tích dương (+1) bền vững trong tế bào."
))

cards.append(make_card(
    "HS07-B2-07",
    "Đường cong chuẩn độ acid-base của Glycin",
    "CHUẨN ĐỘ ACID-BASE",
    "Mô tả diễn biến đường cong chuẩn độ acid-base của Glycin và xác định các vùng đệm tối ưu trên đồ thị?",
    [
        "<b>Dạng khởi đầu ở pH < 1 —</b> Phân tử tồn tại 100% ở dạng cation (+1): +H3N-CH2-COOH.",
        "<b>Vùng đệm thứ nhất quanh pK1 —</b> Thêm 0,5 đương lượng OH⁻ đạt pH = pK1 = 2,34; tại đây [Cation +1] = [Zwitterion 0], dung dịch có dung lượng đệm tối đa chống thay đổi pH ở vùng acid.",
        "<b>Điểm uốn đẳng điện pI —</b> Thêm đúng 1,0 đương lượng OH⁻ đạt điểm uốn pI = 5,97; tại đây 100% phân tử chuyển thành Zwitterion (+H3N-CH2-COO⁻), dung dịch mất hoàn toàn khả năng đệm.",
        "<b>Vùng đệm thứ hai quanh pK2 —</b> Thêm 1,5 đương lượng OH⁻ đạt pH = pK2 = 9,60; tại đây [Zwitterion 0] = [Anion -1], dung dịch đệm tối ưu ở vùng kiềm; thêm 2,0 đương lượng OH⁻ chuyển 100% sang anion H2N-CH2-COO⁻ (-1)."
    ],
    "Đường cong chuẩn độ của một acid amin đơn giản gồm hai vùng đệm dẹt phẳng (buffering regions) nằm trong khoảng pKa ± 1 và một điểm uốn dốc đứng duy nhất ứng với giá trị điểm đẳng điện pI."
))

cards.append(make_card(
    "HS07-B2-08",
    "Đường cong chuẩn độ 3 nấc của Histidin",
    "CHUẨN ĐỘ ACID-BASE",
    "Phân tích 3 nấc chuẩn độ của Histidin và giải thích vì sao Histidin có dạng tích điện +2 ở môi trường acid mạnh?",
    [
        "<b>Dạng cation +2 ở pH < 1 —</b> Cả nhóm α-carboxyl (-COOH), vòng imidazol (+H-Im) và nhóm α-amoni (-NH3⁺) đều bị proton hóa hoàn toàn, mang tổng cộng +2 điện tích dương.",
        "<b>Nấc chuẩn độ 1 (pK1 = 1,82) —</b> Nhóm α-carboxyl nhường proton chuyển thành -COO⁻, phân tử chuyển từ dạng (+2) thành cation (+1).",
        "<b>Nấc chuẩn độ 2 (pKR = 6,00) —</b> Vòng imidazol nhường proton khử điện dương, phân tử chuyển từ dạng (+1) sang dạng Zwitterion trung hòa (0); điểm uốn pI đạt tại pH = 7,59.",
        "<b>Nấc chuẩn độ 3 (pK2 = 9,17) —</b> Nhóm α-amoni nhường proton cuối cùng thành -NH2, phân tử chuyển hoàn toàn thành anion mang điện tích âm (-1)."
    ],
    "Histidin là ví dụ điển hình của acid amin đa chức năng. Sự hiện diện của nấc phân ly pKR = 6,00 nằm ngay trong khoảng pH sinh lý cho phép Histidin hấp thu hoặc phóng thích ion H⁺ cực kỳ nhạy bén trong các phản ứng xúc tác sinh học."
))

cards.append(make_card(
    "HS07-B2-09",
    "Nguyên lý Điện di Protein huyết thanh (SPEP) ở pH 8.6",
    "ĐIỆN DI PROTEIN LÂM SÀNG",
    "Trình bày nguyên lý kỹ thuật điện di protein huyết thanh (SPEP) trong đệm kiềm barbital ở pH 8.6?",
    [
        "<b>Nguyên lý điện trường —</b> Đặt mẫu protein huyết thanh vào một điện trường một chiều trên giá thể gel agarose hoặc màng cellulose acetat.",
        "<b>Môi trường đệm kiềm pH = 8,6 —</b> Ở pH 8,6, giá trị pH môi trường cao hơn điểm đẳng điện pI của toàn bộ các protein huyết thanh (ví dụ Albumin pI ≈ 4,7; Globulin pI từ 5,2 đến 7,3).",
        "<b>Toàn bộ protein tích điện âm —</b> Do pH > pI, tất cả protein huyết thanh đều phân ly mất proton thành các ANION tích điện âm và CÙNG DI CHUYỂN VỀ PHÍA CỰC DƯƠNG (ANOT +).",
        "<b>Yếu tố quyết định tốc độ di chuyển —</b> Protein nào có pI càng thấp (tích điện âm càng đậm đặc) và kích thước phân tử càng nhỏ gọn sẽ di chuyển nhanh nhất và xa nhất về phía cực Anot."
    ],
    "Trong điện di màng cellulose acetat hoặc gel agarose, dòng dịch chuyển nội thẩm tích (electroendosmosis) của dung môi ngược chiều về phía cực âm Catot có thể làm dịch chuyển nhẹ phân đoạn gamma-globulin lùi về sau vạch xuất phát."
))

cards.append(make_card(
    "HS07-B2-10",
    "Năm phân đoạn protein huyết thanh kinh điển trên SPEP",
    "ĐIỆN DI PROTEIN LÂM SÀNG",
    "Kể tên 5 phân đoạn protein huyết thanh theo thứ tự từ Anot (+) về Catot (-) và nêu tỷ lệ phần trăm bình thường?",
    [
        "<b>1. Albumin (55 - 65%) —</b> Chạy nhanh nhất và xa nhất về phía cực dương Anot (+), pI thấp nhất (4,7), nồng độ cao nhất tạo đỉnh nhọn hoắt cao nhất trên biểu đồ điện di.",
        "<b>2. α1-globulin (3 - 5%) —</b> Chạy kế tiếp Albumin; thành phần chính gồm α1-antitrypsin (ức chế elastase bạch cầu) và α1-acid glycoprotein.",
        "<b>3. α2-globulin (7 - 13%) —</b> Chạy ở giữa; thành phần chính gồm Haptoglobin (gắn Hb tự do), α2-macroglobulin (ức chế protease trọng lượng lớn 720 kDa), và Ceruloplasmin (vận chuyển đồng).",
        "<b>4. β-globulin (8 - 14%) —</b> Thường tách thành 2 đỉnh β1 và β2; thành phần chính gồm Transferrin (vận chuyển sắt), β-lipoprotein (LDL), và Bổ thể C3.",
        "<b>5. γ-globulin (12 - 20%) —</b> Nằm gần vạch xuất phát nhất (sát cực âm Catot); thành phần chính gồm các globulin miễn dịch (IgG chiếm ưu thế, IgA, IgM, IgD, IgE) do tương bào tiết ra."
    ],
    "Biểu đồ SPEP bình thường có hình thái đặc trưng: 1 đỉnh Albumin cao vút thanh thoát, sau đó là 4 ngọn đồi thấp thoai thoải trải dài từ alpha-1, alpha-2, beta đến gamma. Bất kỳ sự xáo trộn nào về chiều cao hay hình thái đỉnh đều gợi ý bệnh lý cơ quan."
))

cards.append(make_card(
    "HS07-B2-11",
    "Biến đổi SPEP trong Hội chứng thận hư",
    "BỆNH HỌC LÂM SÀNG SPEP",
    "Phân tích sự biến đổi đặc trưng của biểu đồ điện di protein huyết thanh ở bệnh nhân Hội chứng thận hư?",
    [
        "<b>Albumin giảm sâu trầm trọng —</b> Tổn thương màng đáy cầu thận làm mất hàng rào điện tích âm và mở rộng lỗ lọc, khiến Albumin (kích thước nhỏ 66 kDa) thất thoát ồ ạt qua nước tiểu (> 3,5 g/24h), đỉnh Albumin trên SPEP sụt giảm nghiêm trọng.",
        "<b>Đỉnh α2-globulin tăng vọt bù trừ —</b> Đỉnh α2-macroglobulin tăng rất cao và nhọn bất thường; do phân tử α2-macroglobulin có kích thước khổng lồ (720 kDa) không thể lọt qua màng lọc cầu thận bị tổn thương.",
        "<b>Phản ứng bù trừ áp suất keo của gan —</b> Tế bào gan tăng cường tổng hợp toàn bộ protein huyết tương để bù đắp áp suất keo bị sụt giảm, dẫn đến sự tích tụ các đại phân tử như α2-macroglobulin và Lipoprotein.",
        "<b>γ-globulin thường giảm nhẹ —</b> Các kháng thể IgG có kích thước trung bình (150 kDa) cũng bị thất thoát một phần qua nước tiểu, khiến bệnh nhân thận hư dễ bị nhiễm trùng."
    ],
    "Hình ảnh 'Albumin sụt sâu + α2-macroglobulin tăng vút hình tháp' trên biểu đồ SPEP là dấu ấn kinh điển giúp bác sĩ nhận diện ngay Hội chứng thận hư ngay cả trước khi có kết quả định lượng protein niệu 24 giờ."
))

cards.append(make_card(
    "HS07-B2-12",
    "Biến đổi SPEP trong Xơ gan và Đa u tủy xương",
    "BỆNH HỌC LÂM SÀNG SPEP",
    "Phân biệt biến đổi SPEP trong bệnh Xơ gan (hiện tượng cầu nối β-γ) và Đa u tủy xương (đỉnh đơn dòng M-spike)?",
    [
        "<b>Xơ gan: Albumin giảm nặng —</b> Suy tế bào gan làm giảm sút nghiêm trọng khả năng sinh tổng hợp Albumin nội sinh.",
        "<b>Xơ gan: Hiện tượng cầu nối β-γ (Beta-Gamma Bridging) —</b> Tăng sinh polyclonal các globulin miễn dịch (đặc biệt là IgA tiết từ ruột không được gan thanh thải) làm lấp đầy khoảng trũng giữa đỉnh β và γ, tạo thành một dải liên tục không có ranh giới phân cách.",
        "<b>Đa u tủy xương (Kahler / Multiple Myeloma) —</b> Tăng sinh ác tính đơn dòng (monoclonal) của một dòng tương bào trong tủy xương.",
        "<b>Đặc điểm đỉnh M (M-Spike) —</b> Xuất hiện một đỉnh cực kỳ nhọn hoắt, đáy hẹp, bờ đứng thẳng đứng nằm ở vùng γ-globulin (hoặc đôi khi ở vùng β), đại diện cho một loại globulin miễn dịch đơn dòng (thường là IgG hoặc IgA đơn dòng)."
    ],
    "Khác biệt mấu chốt: Xơ gan tạo đỉnh gamma rộng đáy bè (tăng đa dòng polyclonal nhiều loại kháng thể), trong khi Đa u tủy xương tạo đỉnh M hẹp đáy nhọn hoắt (tăng đơn dòng monoclonal của đúng 1 clone tế bào tương bào ác tính)."
))

# ==============================================================================
# SECTION B3: LIÊN KẾT PEPTID VÀ PHẢN ỨNG HÓA HỌC (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B3-01",
    "Phản ứng hình thành liên kết peptid",
    "CẤU TẠO LIÊN KẾT PEPTID",
    "Trình bày phản ứng ngưng tụ hình thành liên kết peptid và bản chất nhiệt động học của liên kết này?",
    [
        "<b>Phản ứng ngưng tụ tách nước —</b> Nhóm α-carboxyl (-COO⁻) của acid amin thứ nhất phản ứng với nhóm α-amin (-NH3⁺) của acid amin thứ hai, loại đi một phân tử nước H2O tạo liên kết cộng hóa trị amid -CO-NH-.",
        "<b>Chi phí năng lượng nhiệt động học —</b> Phản ứng tạo liên kết peptid có biến thiên năng lượng tự do Gibbs dương (ΔG°' ≈ +10 đến +15 kJ/mol), là phản ứng thu công đòi hỏi phải tiêu tốn năng lượng.",
        "<b>Hoạt hóa qua aminoacyl-tRNA —</b> Trong tế bào sống, phản ứng không xảy ra trực tiếp giữa các acid amin tự do mà bắt buộc phải hoạt hóa acid amin bằng ATP gắn lên tRNA đặc hiệu.",
        "<b>Độ bền thủy phân cao —</b> Mặc dù về mặt nhiệt động học sự thủy phân peptid là thuận lợi (ΔG < 0), nhưng năng lượng hoạt hóa của phản ứng thủy phân rất cao, giúp liên kết peptid cực kỳ bền vững trong dung dịch nước ở điều kiện sinh lý (thời gian bán hủy lên tới hàng thế kỷ nếu không có enzym protease)."
    ],
    "Ribosome đóng vai trò enzym Peptidyl Transferase (bản chất là một Ribozyme tạo bởi ARN 28S ở nhân thực) xúc tác hình thành liên kết peptid với tốc độ hàng chục liên kết mỗi giây trong quá trình dịch mã."
))

cards.append(make_card(
    "HS07-B3-02",
    "Đặc tính phẳng và 40% liên kết đôi của liên kết peptid",
    "ĐẶC TÍNH VẬT LÝ LIÊN KẾT PEPTID",
    "Phân tích các nghiên cứu của Linus Pauling về tính chất phẳng và 40% liên kết đôi của liên kết C-N trong peptid?",
    [
        "<b>Cộng hưởng electron π —</b> Cặp electron tự do không liên kết trên nguyên tử Nitơ của nhóm amid có sự giải tỏa cộng hưởng mạnh mẽ vào nhóm carbonyl C=O.",
        "<b>Độ dài liên kết C-N ngắn —</b> Độ dài liên kết C-N trong peptid là 1,32 Å, ngắn hơn đáng kể so với liên kết đơn C-N thông thường (1,47 Å) và tiệm cận liên kết đôi C=N (1,28 Å).",
        "<b>Mang khoảng 40% tính chất liên kết đôi —</b> Do tính chất liên kết đôi một phần, KHÔNG CÓ SỰ QUAY TỰ DO QUANH TRỤC LIÊN KẾT C-N của khung xương peptid.",
        "<b>Mặt phẳng peptid cứng nhắc —</b> Sáu nguyên tử nằm trên cùng một mặt phẳng cứng: Cα1, C carbonyl, O carbonyl, N amid, H amid, và Cα2; tạo nên các đơn vị mặt phẳng nối tiếp nhau."
    ],
    "Khám phá của Linus Pauling và Robert Corey về tính chất phẳng của liên kết peptid đã đặt nền móng tuyệt đối cho sinh học phân tử hiện đại, chứng minh rằng khung xương protein không thể uốn cong tùy tiện mà bị giới hạn nghiêm ngặt bởi các mặt phẳng cứng."
))

cards.append(make_card(
    "HS07-B3-03",
    "Cấu hình trans ưu thế của liên kết peptid",
    "CẤU HÌNH KHÔNG GIAN PEPTID",
    "Giải thích vì sao liên kết peptid hầu như luôn tồn tại ở cấu hình trans và nêu ngoại lệ duy nhất với Prolin?",
    [
        "<b>Định nghĩa cấu hình trans —</b> Hai nguyên tử Cα kế cận (cũng như O carbonyl và H amid) nằm về hai phía đối diện của trục liên kết liên kết peptid C-N.",
        "<b>Tránh cản trở không gian —</b> Ở cấu hình cis, hai chuỗi bên R của hai acid amin kế tiếp nằm cùng một phía sẽ va chạm lập thể dữ dội và đẩy nhau mạnh mẽ làm tăng thế năng của phân tử.",
        "<b>Tỷ lệ áp đảo trong tự nhiên —</b> Hơn 99,6% liên kết peptid thông thường trong protein tự nhiên đều tồn tại ở cấu hình trans bền vững.",
        "<b>Ngoại lệ liên kết X-Pro —</b> Ở liên kết peptid đứng trước gốc Prolin (X-Pro), cấu hình cis xuất hiện với tỷ lệ từ 6% đến 10% do dị vòng pyrrolidin của Prolin làm giảm sự chênh lệch năng lượng giữa dạng cis và trans; enzym Peptidyl Prolyl cis-trans Isomerase (PPIase) xúc tác sự chuyển đổi này trong cuộn gập protein."
    ],
    "Sự chuyển đổi cis-trans ở các liên kết X-Pro thường là bước giới hạn tốc độ (rate-limiting step) trong quá trình cuộn gập hoàn chỉnh của các phân tử protein lớn như kháng thể hoặc collagen."
))

cards.append(make_card(
    "HS07-B3-04",
    "Góc quay Phi (φ), Psi (ψ) và Biểu đồ Ramachandran",
    "BIỂU ĐỒ RAMACHANDRAN",
    "Định nghĩa hai góc quay tự do φ và ψ của khung xương polypeptid và nêu ý nghĩa của Biểu đồ Ramachandran?",
    [
        "<b>Góc quay Phi (φ) —</b> Là góc quay tự do quanh trục liên kết đơn giữa nguyên tử Nitơ amid và Carbon α (liên kết N - Cα).",
        "<b>Góc quay Psi (ψ) —</b> Là góc quay tự do quanh trục liên kết đơn giữa Carbon α và Carbon carbonyl (liên kết Cα - C).",
        "<b>Khung xương quay quanh Cα —</b> Mặc dù liên kết peptid C-N bị khóa cứng, khung xương polypeptid vẫn có thể quay linh hoạt quanh 2 liên kết đơn gắn vào Cα tạo nên vô số cấu hình không gian.",
        "<b>Biểu đồ Ramachandran —</b> Biểu diễn tọa độ 2 chiều của cặp góc (φ, ψ) được phép về mặt lập thể (không bị va chạm chướng ngại không gian giữa các nguyên tử); xác định chính xác vùng tọa độ đặc trưng của xoắn α (vùng âm) và phiến gấp β (vùng trên bên trái)."
    ],
    "Nhờ Biểu đồ Ramachandran, các nhà sinh học tính toán có thể kiểm tra độ tin cậy của mô hình cấu trúc 3D protein giải mã bằng tinh thể học tia X hoặc trí tuệ nhân tạo (AlphaFold); cấu trúc chuẩn phải có trên 90% các gốc acid amin nằm trong vùng cho phép."
))

cards.append(make_card(
    "HS07-B3-05",
    "Quy ước danh pháp và cấu trúc chuỗi polypeptid",
    "DANH PHÁP CHUỖI POLYPEPTID",
    "Nêu quy ước định hướng hai đầu tận cùng của chuỗi polypeptid và quy tắc gọi tên chuỗi peptid?",
    [
        "<b>Đầu N-tận (Amino-terminus) —</b> Là đầu mang nhóm α-amin tự do (-NH3⁺), luôn được quy ước đánh số là acid amin số 1 và viết ở phía BÊN TRÁI của chuỗi.",
        "<b>Đầu C-tận (Carboxyl-terminus) —</b> Là đầu mang nhóm α-carboxyl tự do (-COO⁻), mang số thứ tự cuối cùng (n) và viết ở phía BÊN PHẢI của chuỗi.",
        "<b>Hướng tổng hợp sinh học —</b> Dịch mã trên ribosome và sinh tổng hợp protein luôn tiến hành theo chiều từ đầu N-tận đến đầu C-tận.",
        "<b>Quy tắc gọi tên —</b> Đổi đuôi -in hoặc -at của các acid amin thành đuôi -yl và giữ nguyên tên của acid amin cuối cùng ở đầu C-tận (Ví dụ: Tripeptid gồm Glycin, Alanin, Serin được gọi là Glycyl-alanyl-serin hay Gly-Ala-Ser)."
    ],
    "Khi chuỗi polypeptid có trên 50 gốc acid amin và khối lượng phân tử trên 5000 Da, hợp chất thường được định danh chính thức là một phân tử Protein hoàn chỉnh."
))

cards.append(make_card(
    "HS07-B3-06",
    "Glutathion (GSH) và hệ thống chống oxy hóa hồng cầu",
    "PEPTID HOẠT TÍNH LÂM SÀNG",
    "Trình bày cấu trúc đặc biệt của Glutathion (GSH) và vai trò của nó trong việc bảo vệ màng hồng cầu chống tan máu?",
    [
        "<b>Cấu trúc tripeptid đặc biệt —</b> Glutathion là γ-L-Glutamyl-L-cysteinyl-glycin; điểm độc đáo là nhóm carboxyl ở vị trí γ của Glutamat (thay vì vị trí α thông thường) tạo liên kết peptid với nhóm amin của Cystein.",
        "<b>Nhóm -SH đóng vai trò lá chắn khử —</b> Nhóm thiol tự do của Cystein cung cấp electron khử các gốc tự do peroxide độc hại: 2 GSH + H2O2 → GSSG + 2 H2O (xúc tác bởi enzym Glutathione Peroxidase chứa Selen).",
        "<b>Tái tạo GSH nhờ NADPH —</b> Phân tử GSSG bị oxy hóa được tái tạo trở lại dạng khử GSH nhờ enzym Glutathione Reductase sử dụng coenzym NADPH sinh ra từ con đường Pentose Phosphat (nhờ men G6PD).",
        "<b>Ý nghĩa trong bệnh thiếu men G6PD —</b> Thiếu enzym G6PD làm cạn kiệt NADPH, khiến hồng cầu không tái tạo được GSH; khi tiếp xúc thuốc oxy hóa (Primaquin, Dapsone), hemoglobin bị oxy hóa kết tủa thành thể Heinz và gây tan máu cấp dữ dội."
    ],
    "Glutathion là chất chống oxy hóa nội sinh phong phú nhất trong tế bào (nồng độ lên tới 5 mM). Liên kết gamma-peptid bất thường giúp phân tử GSH đề kháng hoàn toàn với sự phân hủy của các enzym protease nội bào thông thường."
))

cards.append(make_card(
    "HS07-B3-07",
    "Oxytocin và Vasopressin (ADH)",
    "PEPTID HOẠT TÍNH LÂM SÀNG",
    "So sánh cấu tạo nonapeptid của Oxytocin và Vasopressin (ADH) và nêu cơ chế gây bệnh Đái tháo nhạt trung ương?",
    [
        "<b>Cấu trúc nonapeptid chung —</b> Đều gồm 9 acid amin do vùng dưới đồi tổng hợp, dự trữ tại thùy sau tuyến yên, chứa 1 cầu nối disulfur nội chuỗi giữa Cys1 và Cys6 tạo vòng 6 acid amin và đuôi 3 acid amin.",
        "<b>Khác biệt ở 2 acid amin —</b> Oxytocin có Ile ở vị trí 3 và Leu ở vị trí 8; trong khi Vasopressin (ADH) có Phe ở vị trí 3 và Arg ở vị trí 8.",
        "<b>Tác dụng sinh lý Oxytocin —</b> Gắn lên thụ thể cơ trơn tử cung gây co bóp mạnh trong chuyển dạ đẻ và co thắt tế bào cơ biểu mô tuyến vú tống xuất sữa.",
        "<b>Tác dụng ADH và Đái tháo nhạt —</b> ADH gắn thụ thể V2 ở ống góp thận chèn kênh nước Aquaporin-2 tăng tái hấp thu nước; tổn thương vùng dưới đồi-tuyến yên gây thiếu ADH dẫn đến Đái tháo nhạt trung ương (tiểu nhiều 5 - 15 L/ngày, nước tiểu tỷ trọng rất thấp)."
    ],
    "Sự khác biệt chỉ ở 2 gốc acid amin (vị trí 3 và 8) đã biến đổi hoàn toàn tác dụng dược lý: Phe3 và Arg8 tạo cho ADH hoạt tính co mạch tăng huyết áp và giữ nước tại thận, trong khi Ile3 và Leu8 hướng Oxytocin đặc hiệu vào cơ quan sinh sản nữ."
))

cards.append(make_card(
    "HS07-B3-08",
    "Brain Natriuretic Peptide (BNP) và Endorphin",
    "PEPTID HOẠT TÍNH LÂM SÀNG",
    "Nêu vai trò của Brain Natriuretic Peptide (BNP) trong chẩn đoán suy tim và tác dụng của các pentapeptid Endorphin/Enkephalin?",
    [
        "<b>Bản chất phân tử BNP —</b> Là một polypeptid gồm 32 acid amin có một vòng disulfur 17 acid amin, tiết ra chủ yếu từ các tế bào cơ tâm thất khi thành tim bị căng giãn do quá tải thể tích hoặc áp lực.",
        "<b>Tác dụng sinh học của BNP —</b> Tăng bài xuất natri và nước qua thận, giãn mạch hệ thống, ức chế hệ Renin-Angiotensin-Aldosteron và hệ thần kinh giao cảm nhằm giảm tiền gánh và hậu gánh.",
        "<b>Dấu ấn sinh học vàng trong Suy tim —</b> Nồng độ BNP và mảnh phân cắt trơ NT-proBNP trong huyết tương là tiêu chuẩn vàng sinh học giúp chẩn đoán phân biệt khó thở do suy tim cấp với khó thở do bệnh phổi.",
        "<b>Endorphin và Enkephalin —</b> Các pentapeptid opiat nội sinh (như Met-enkephalin: Tyr-Gly-Gly-Phe-Met) gắn lên thụ thể morphin (μ, δ) ở tủy sống và não bộ, ức chế dẫn truyền cảm giác đau mạnh hơn thuốc phiện."
    ],
    "NT-proBNP có thời gian bán hủy dài hơn (khoảng 70 phút so với 20 phút của BNP) và nồng độ huyết tương ổn định hơn nên rất được ưa chuộng trong các xét nghiệm cấp cứu tim mạch lâm sàng."
))

cards.append(make_card(
    "HS07-B3-09",
    "Phản ứng Biuret định lượng protein toàn phần",
    "PHẢN ỨNG MÀU ĐỊNH LƯỢNG PROTEIN",
    "Trình bày nguyên lý, điều kiện và ý nghĩa lâm sàng của phản ứng Biuret trong xét nghiệm hóa sinh thường quy?",
    [
        "<b>Nguyên lý phản ứng —</b> Trong môi trường kiềm mạnh, các phân tử chứa từ 2 liên kết peptid trở lên sẽ tạo phức chất phối trí màu tím hoa cà (tím violet) với ion đồng Cu²⁺.",
        "<b>Cấu tạo thuốc thử Biuret —</b> Chứa CuSO4 (cung cấp ion Cu²⁺), NaOH (tạo môi trường kiềm mạnh), và muối Tartrat kali natri (giữ ion Cu²⁺ hòa tan không bị kết tủa thành Cu(OH)2).",
        "<b>Điều kiện tối thiểu —</b> Phải có ít nhất HAI LIÊN KẾT PEPTID (tức từ tripeptid trở lên); acid amin tự do và dipeptid hoàn toàn âm tính với phản ứng Biuret.",
        "<b>Ý nghĩa lâm sàng —</b> Cường độ màu tím tỷ lệ thuận với số lượng liên kết peptid, đo quang ở bước sóng λ = 540 nm; là phương pháp chuẩn định lượng Protein toàn phần huyết thanh (bình thường: 65 - 82 g/L)."
    ],
    "Tên gọi 'Biuret' bắt nguồn từ hợp chất hóa học biuret (H2N-CO-NH-CO-NH2) được tạo thành khi đun nóng urê; hợp chất này cho phản ứng màu tím tương tự với ion Cu²⁺ trong kiềm."
))

cards.append(make_card(
    "HS07-B3-10",
    "Các phản ứng màu đặc hiệu của chuỗi bên R",
    "PHẢN ỨNG ĐỊNH TÍNH ACID AMIN",
    "Nêu nguyên lý và hiện tượng của các phản ứng: Ninhydrin, Xanthoprotein, Millon, Sakaguchi và Chì sulfua?",
    [
        "<b>Phản ứng Ninhydrin (Phát hiện nhóm α-amin) —</b> Ninhydrin oxy hóa khử nhóm α-amin tự do giải phóng NH3 tạo phức Ruhemann màu tím xanh (λ = 570 nm); riêng Prolin cho màu vàng tươi (λ = 440 nm).",
        "<b>Phản ứng Xanthoprotein (Nhân thơm) —</b> Acid nitric đặc HNO3 nitro hóa vòng thơm của Phe, Tyr, Trp tạo màu vàng; chuyển sang màu da cam đậm khi thêm kiềm NaOH.",
        "<b>Phản ứng Millon (Tyrosin) —</b> Thuốc thử Hg(NO3)2 trong HNO3 phản ứng đặc hiệu với nhóm phenolic của Tyrosin tạo kết tủa màu đỏ thịt.",
        "<b>Phản ứng Sakaguchi (Arginin) —</b> Thuốc thử α-naphtol và natri hypoclorit (NaClO) trong kiềm phản ứng với nhóm guanidino của Arginin tạo màu đỏ thắm.",
        "<b>Phản ứng chì sulfua (Cystein) —</b> Đun nóng với NaOH giải phóng lưu huỳnh thành Na2S, phản ứng với chì acetat (CH3COO)2Pb tạo kết tủa màu đen chì sulfua (PbS ↓)."
    ],
    "Phản ứng Pauly: Phản ứng diazo hóa giữa acid sulfanilic với vòng imidazol của Histidin hoặc phenol của Tyrosin trong môi trường kiềm tạo sản phẩm có màu đỏ anh đào đặc trưng."
))

# ==============================================================================
# SECTION B4: BỐN BẬC CẤU TRÚC PROTEIN VÀ ĐỘNG HỌC CUỘN GẬP (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B4-01",
    "Cấu trúc bậc I (Primary Structure) và ý nghĩa di truyền",
    "BỐN BẬC CẤU TRÚC PROTEIN",
    "Định nghĩa Cấu trúc bậc I của protein và giải thích vì sao cấu trúc bậc I quyết định các bậc cấu trúc cao hơn?",
    [
        "<b>Định nghĩa Cấu trúc bậc I —</b> Là trật tự sắp xếp tuyến tính tuần tự của các gốc acid amin trong chuỗi polypeptid từ đầu N-tận đến đầu C-tận.",
        "<b>Các liên kết làm bền —</b> Được liên kết cộng hóa trị bền vững bởi các LIÊN KẾT PEPTID (và các CẦU NỐI DISULFUR nếu có).",
        "<b>Bản thiết kế mã hóa di truyền —</b> Trình tự bậc 1 được dịch mã trực tiếp từ trình tự bộ ba nucleotid trên mARN theo mã di truyền.",
        "<b>Quyết định các bậc cấu trúc không gian —</b> Cấu trúc bậc 1 chứa đựng toàn bộ thông tin cần và đủ để định hướng chuỗi polypeptid tự động cuộn gập thành cấu trúc bậc 2, 3 và 4 chính xác."
    ],
    "Tầm quan trọng trong đột biến gen: Một sự thay đổi dù chỉ một acid amin duy nhất trên cấu trúc bậc 1 (như thay Glu thành Val ở vị trí số 6 chuỗi β-globin) có thể làm đảo lộn cấu trúc không gian và dẫn đến bệnh cảnh lâm sàng nghiêm trọng như Hồng cầu hình liềm."
))

cards.append(make_card(
    "HS07-B4-02",
    "Các phương pháp xác định cấu trúc bậc I",
    "PHƯƠNG PHÁP NGHIÊN CỨU PROTEIN",
    "Trình bày 3 phương pháp hiện đại xác định cấu trúc bậc I của phân tử protein?",
    [
        "<b>1. Phương pháp thoái biến Edman (Edman Degradation) —</b> Sử dụng thuốc thử Phenylisothiocyanat (PITC) gắn đặc hiệu vào nhóm α-amin ở đầu N-tận, cắt rời tuần tự từng acid amin từ đầu N mà không làm vỡ các liên kết peptid còn lại.",
        "<b>2. Phương pháp giải trình tự gen (Genomics / cDNA) —</b> Giải trình tự chuỗi nucleotid trên gen ADN hoặc cARN thông qua công nghệ PCR và giải trình tự gen thế hệ mới (NGS), sau đó suy diễn ra trình tự acid amin theo bảng mã di truyền.",
        "<b>3. Phương pháp khối phổ song song (Tandem MS / MS-MS) —</b> Ion hóa chuỗi peptid bằng kỹ thuật MALDI hoặc ESI, bắn vỡ các ion peptid thành các mảnh nhỏ trong buồng va chạm và đo chính xác tỷ lệ khối lượng/điện tích (m/z) để đọc trực tiếp trình tự acid amin.",
        "<b>Ưu thế của khối phổ —</b> Phương pháp MS/MS cực kỳ nhạy, tốc độ cao và phát hiện được chính xác các biến đổi sau dịch mã (phosphoryl hóa, acetyl hóa, glycosyl hóa) mà phương pháp giải trình tự gen không thể thấy được."
    ],
    "Thoái biến Edman từng giúp Pehr Edman và sau đó là Frederick Sanger xác định cấu trúc bậc 1 của Insulin (Giải Nobel Hóa học 1958). Hiện nay khối phổ MS/MS là công cụ chủ lực của ngành Proteomics hiện đại."
))

cards.append(make_card(
    "HS07-B4-03",
    "Cấu trúc bậc II (Secondary Structure) và liên kết hydro",
    "BỐN BẬC CẤU TRÚC PROTEIN",
    "Định nghĩa Cấu trúc bậc II của protein và nêu bản chất lực liên kết làm bền cấu trúc này?",
    [
        "<b>Định nghĩa Cấu trúc bậc II —</b> Là sự cuộn xoắn hoặc gấp nếp tuần hoàn đều đặn cục bộ của khung xương polypeptid chính (N - Cα - C).",
        "<b>Bản chất liên kết hydro —</b> Được làm bền chủ yếu bởi các LIÊN KẾT HYDRO hình thành giữa nhóm carbonyl (C=O) và nhóm imin (N-H) của chính khung xương polypeptid.",
        "<b>Không phụ thuộc chuỗi bên R —</b> Các liên kết hydro làm bền cấu trúc bậc 2 hoàn toàn chỉ diễn ra giữa các nguyên tử của khung xương chính, không có sự tham gia của chuỗi bên R.",
        "<b>3 dạng cấu trúc bậc II chủ yếu —</b> Cấu trúc xoắn α (α-helix), cấu trúc phiến gấp β (β-pleated sheet), và cấu trúc khúc cuộn β (β-turn hay β-bend)."
    ],
    "Mặc dù mỗi liên kết hydro riêng lẻ có năng lượng liên kết khá yếu (chỉ khoảng 12 - 30 kJ/mol), nhưng hàng trăm liên kết hydro phân bố tuần hoàn liên tục dọc theo khung xương đã tạo nên độ bền cơ học phi thường cho cấu trúc bậc 2."
))

cards.append(make_card(
    "HS07-B4-04",
    "Cấu trúc xoắn α (Alpha-Helix) và các thông số hình học",
    "CẤU TRÚC BẬC HAI PROTEIN",
    "Mô tả cấu trúc xoắn α và nêu 4 thông số hình học kinh điển do Linus Pauling khám phá?",
    [
        "<b>Dạng xoắn phải (Right-handed) —</b> Khung xương polypeptid xoắn chặt chẽ theo chiều kim đồng hồ, các chuỗi bên R vươn thẳng ra phía ngoài trục xoắn để giảm lực cản không gian.",
        "<b>Quy luật liên kết hydro n → n+4 —</b> Nhóm C=O của acid amin thứ n luôn tạo liên kết hydro nội chuỗi song song với trục xoắn với nhóm N-H của acid amin thứ n+4 phía trước nó.",
        "<b>Số gốc acid amin mỗi vòng xoắn —</b> Mỗi vòng xoắn trọn vẹn 360° gồm đúng 3,6 gốc acid amin.",
        "<b>Bước xoắn và khoảng cách tịnh tiến —</b> Bước xoắn (pitch) có độ dài 5,4 Å (0,54 nm); khoảng cách tịnh tiến giữa hai gốc acid amin dọc theo trục xoắn là 1,5 Å (0,15 nm)."
    ],
    "Cấu trúc xoắn α là cấu trúc bậc 2 phong phú nhất trong protein hình cầu (chiếm khoảng 30% cấu trúc của Myoglobin và Hemoglobin). Khung xoắn chặt chẽ không có lỗ rỗng ở giữa vì các nguyên tử van der Waals tiếp xúc khít khao."
))

cards.append(make_card(
    "HS07-B4-05",
    "Các yếu tố phá vỡ cấu trúc xoắn α (Helix Breakers)",
    "CẤU TRÚC BẬC HAI PROTEIN",
    "Phân tích 4 yếu tố gây phá vỡ cấu trúc xoắn α (Helix Breakers) trong chuỗi polypeptid?",
    [
        "<b>1. Sự hiện diện của Prolin —</b> Dị vòng pyrrolidin cố định góc quay N-Cα và thiếu nguyên tử Hydro trên Nitơ amid để tạo liên kết hydro, tạo nên nếp gấp gãy (kink) chấm dứt đoạn xoắn α.",
        "<b>2. Sự hiện diện của Glycin —</b> Chuỗi bên quá nhỏ (R = H) khiến khung xương quá mềm dẻo và linh động cao về mặt entropy, không duy trì được cấu trúc xoắn chặt cố định.",
        "<b>3. Lực đẩy tĩnh điện giữa các chuỗi bên cùng dấu —</b> Cụm các acid amin mang điện tích cùng dấu nằm kế cận nhau (như chuỗi Lys⁺/Arg⁺ hoặc Glu⁻/Asp⁻) sẽ đẩy nhau tĩnh điện làm bung xoắn.",
        "<b>4. Cản trở không gian của các chuỗi bên cồng kềnh —</b> Sự tập trung các acid amin có chuỗi bên phân nhánh gần Cα (Val, Ile, Thr) gây va chạm lập thể nghiêm trọng với khung xương xoắn."
    ],
    "Khi phân tích cấu trúc protein, người ta thường thấy Prolin và Glycin nằm ở vị trí kết thúc đoạn xoắn α hoặc nằm ở các khúc quanh beta-turn kết nối giữa các cấu trúc bậc 2 khác nhau."
))

cards.append(make_card(
    "HS07-B4-06",
    "Cấu trúc phiến gấp β (Beta-Pleated Sheet) song song và đối song",
    "CẤU TRÚC BẬC HAI PROTEIN",
    "So sánh đặc điểm cấu tạo của Phiến gấp β song song và Phiến gấp β đối song?",
    [
        "<b>Dạng chuỗi β duỗi dài —</b> Khung xương polypeptid duỗi dài theo hình dích dắc ziczac (khoảng cách tịnh tiến giữa 2 acid amin lên tới 3,5 Å); chuỗi bên R nhô luân phiên lên mặt trên và mặt dưới phiến.",
        "<b>Liên kết hydro liên chuỗi —</b> Khác với xoắn α (liên kết hydro nội chuỗi), phiến gấp β được làm bền bởi các liên kết hydro hình thành GIỮA CÁC CHUỖI β KHÁC NHAU đặt cạnh nhau.",
        "<b>Phiến β đối song (Antiparallel β-sheet) —</b> Các chuỗi β chạy ngược chiều nhau (N→C xen kẽ C→N); các liên kết hydro nằm thẳng hàng trực diện vuông góc với trục chuỗi, tạo cấu trúc BỀN VỮNG VÀ ỔN ĐỊNH HƠN NHIỀU.",
        "<b>Phiến β song song (Parallel β-sheet) —</b> Các chuỗi β chạy cùng chiều (cùng hướng N→C); các liên kết hydro nằm chéo góc nghiêng so với trục chuỗi nên độ bền kém hơn dạng đối song."
    ],
    "Phiến gấp β chiếm ưu thế trong các protein sợi cấu trúc (như fibroin của tơ tằm) và lõi của nhiều enzym (như cấu trúc thùng beta barrel trong porin màng vi khuẩn)."
))

cards.append(make_card(
    "HS07-B4-07",
    "Cấu trúc khúc cuộn β-turn và vòng lặp (Loops)",
    "CẤU TRÚC BẬC HAI PROTEIN",
    "Mô tả cấu tạo của khúc cuộn β-turn và giải thích vai trò của Glycin và Prolin trong cấu trúc này?",
    [
        "<b>Đổi chiều khung xương 180° —</b> Cấu trúc β-turn gồm đúng 4 gốc acid amin, thực hiện bước ngoặt đảo chiều 180° của khung xương polypeptid để kết nối hai chuỗi β đối song hoặc đổi hướng chuỗi trong protein cầu.",
        "<b>Liên kết hydro n → n+3 —</b> Được làm bền bởi một liên kết hydro hình thành giữa nhóm C=O của gốc thứ 1 với nhóm N-H của gốc thứ 4.",
        "<b>Tần suất áp đảo của Prolin —</b> Prolin (thường ở vị trí 2) dễ dàng tạo cấu hình cis ở liên kết peptid, tạo góc bẻ nhọn cần thiết cho khúc quanh gấp.",
        "<b>Tần suất áp đảo của Glycin —</b> Glycin (thường ở vị trí 3) có kích thước nguyên tử cực nhỏ (R = H), không gây cản trở không gian ở góc uốn hẹp của khúc cuộn."
    ],
    "Khúc cuộn β-turn và các vòng lặp (loops) thường nằm ở bề mặt ngoài của protein hình cầu, là nơi tiếp xúc trực tiếp với kháng thể hoặc cơ chất và thường tham gia cấu tạo các epitope nhận diện miễn dịch."
))

cards.append(make_card(
    "HS07-B4-08",
    "Cấu trúc bậc III (Tertiary Structure) và 5 lực liên kết",
    "BỐN BẬC CẤU TRÚC PROTEIN",
    "Định nghĩa Cấu trúc bậc III của protein và phân tích 5 lực liên kết tham gia làm bền cấu trúc không gian 3 chiều?",
    [
        "<b>Định nghĩa Cấu trúc bậc III —</b> Là cấu trúc không gian 3 chiều hoàn chỉnh của toàn bộ một chuỗi polypeptid đơn lẻ, bao gồm sự cuộn gập phức tạp của các cấu trúc bậc 2 tạo nên hình thái hình cầu hoặc hình sợi.",
        "<b>1. Hiệu ứng kỵ nước (Động lực cốt lõi) —</b> Các chuỗi bên kỵ nước (Leu, Ile, Val, Phe, Met) co cụm vùi sâu vào lõi trong, làm tăng entropy của nước (ΔS > 0), là động lực nhiệt động học chính làm bền cấu trúc.",
        "<b>2. Liên kết hydro —</b> Hình thành giữa các chuỗi bên phân cực (như -OH của Ser/Thr với amid của Gln/Asn).",
        "<b>3. Cầu muối ion tĩnh điện —</b> Lực hút tĩnh điện mạnh giữa các nhóm tích điện trái dấu ở chuỗi bên (như -COO⁻ của Asp/Glu với -NH3⁺ của Lys hoặc guanidino của Arg).",
        "<b>4. Cầu nối disulfur (-S-S-) —</b> Liên kết cộng hóa trị duy nhất làm bền cấu trúc bậc 3, nối giữa hai gốc Cystein ở xa nhau trên chuỗi bậc 1; kết hợp với lực hút van der Waals yếu giữa các nguyên tử tiếp xúc sát nhau."
    ],
    "Khái niệm Miền cấu trúc (Domain): Trong các protein lớn (> 200 acid amin), chuỗi polypeptid thường cuộn thành các khối cấu trúc độc lập gọi là Domain; mỗi domain có thể tự gấp độc lập và đảm nhận một chức năng sinh học riêng biệt."
))

cards.append(make_card(
    "HS07-B4-09",
    "Cấu trúc bậc IV (Quaternary Structure) và tính hợp tác",
    "BỐN BẬC CẤU TRÚC PROTEIN",
    "Định nghĩa Cấu trúc bậc IV của protein và nêu ý nghĩa sinh học của cấu trúc này trong điều hòa dị lập thể?",
    [
        "<b>Định nghĩa Cấu trúc bậc IV —</b> Là sự kết hợp và sắp xếp trong không gian của hai hay nhiều chuỗi polypeptid riêng biệt (được gọi là các tiểu đơn vị - subunits hay protomers) đã có sẵn cấu trúc bậc 3 hoàn chỉnh.",
        "<b>Bản chất lực liên kết —</b> Các tiểu đơn vị gắn kết với nhau chủ yếu bằng CÁC LIÊN KẾT PHI CỘNG HÓA TRỊ (tương tác kỵ nước tại bề mặt tiếp xúc, liên kết hydro, cầu muối) và đôi khi có cầu disulfur liên chuỗi (như Kháng thể IgG).",
        "<b>Điều hòa dị lập thể (Allosteric Regulation) —</b> Cấu trúc bậc 4 cho phép phân tử tiếp nhận các tín hiệu điều hòa: sự gắn một chất điều phối lên một tiểu đơn vị làm biến đổi không gian lan tỏa sang các tiểu đơn vị khác.",
        "<b>Tính hợp tác (Cooperativity) —</b> Sự gắn một phối tử lên một vị trí làm tăng hoặc giảm ái lực của các vị trí còn lại (điển hình như tính hợp tác gắn oxy của 4 tiểu đơn vị trong tetramer Hemoglobin α2β2)."
    ],
    "Không phải mọi protein đều có cấu trúc bậc 4. Myoglobin chỉ có cấu trúc bậc 3 (đơn chuỗi), trong khi Hemoglobin bắt buộc phải có cấu trúc bậc 4 (tetramer 4 chuỗi) mới có thể thực hiện chức năng vận chuyển và điều hòa oxy tinh vi."
))

cards.append(make_card(
    "HS07-B4-10",
    "Thí nghiệm kinh điển Christian Anfinsen và Định đề Anfinsen",
    "ĐỘNG HỌC CUỘN GẬP PROTEIN",
    "Mô tả các bước trong thí nghiệm Anfinsen trên Ribonuclease A và nêu nội dung cốt tử của Định đề Anfinsen?",
    [
        "<b>Mô hình thí nghiệm RNase A —</b> Sử dụng enzym Ribonuclease A tụy bò gồm chuỗi đơn 124 acid amin với đúng 4 cầu nối disulfur (-S-S-) cố định.",
        "<b>Bước 1: Gây biến tính hoàn toàn —</b> Xử lý bằng Urê 8 M (phá vỡ mọi liên kết hydro và tương tác kỵ nước) kết hợp chất khử β-mercaptoethanol (cắt đứt hoàn toàn 4 cầu disulfur thành 8 nhóm -SH); RNase A bung thẳng và mất 100% hoạt tính.",
        "<b>Bước 2: Hồi tính tự phát —</b> Thẩm tích loại bỏ Urê và β-mercaptoethanol rồi cho tiếp xúc oxy không khí; RNase A tự động cuộn gập trở lại đúng cấu trúc 3D tự nhiên, 4 cầu disulfur tái tạo chính xác tuyệt đối (xác suất ngẫu nhiên chỉ 1/105 ≈ 1%) và phục hồi 100% hoạt tính.",
        "<b>Nội dung Định đề Anfinsen —</b> Toàn bộ thông tin cần thiết để xác định cấu trúc không gian 3 chiều bản địa (native conformation) của protein đã được mã hóa sẵn trong cấu trúc bậc I (trình tự acid amin) của nó."
    ],
    "Định đề Anfinsen khẳng định trạng thái bản địa có hoạt tính sinh học của protein là trạng thái có mức năng lượng tự do Gibbs thấp nhất về mặt nhiệt động học, chứng minh tính tất yếu của quá trình cuộn gập tự phát."
))

cards.append(make_card(
    "HS07-B4-11",
    "Hiện tượng Biến tính Protein (Denaturation)",
    "TÍNH CHẤT HÓA LÝ PROTEIN",
    "Định nghĩa hiện tượng Biến tính protein và phân tích tác động của nhiệt độ, pH cực đoan và ion kim loại nặng?",
    [
        "<b>Định nghĩa biến tính —</b> Là sự phá vỡ các bậc cấu trúc bậc 2, bậc 3 và bậc 4 dẫn đến mất hình thái không gian tự nhiên và mất chức năng sinh học, nhưng HOÀN TOÀN KHÔNG LÀM ĐỨT GÃY LIÊN KẾT PEPTID (cấu trúc bậc 1 vẫn nguyên vẹn).",
        "<b>Nhiệt độ cao —</b> Cung cấp động năng nhiệt vượt quá năng lượng của các liên kết hydro và tương tác van der Waals yếu, làm bung tháo chuỗi protein (như lòng trắng trứng bị đông tụ rắn lại khi đun sôi).",
        "<b>pH cực đoan (Acid mạnh, kiềm mạnh) —</b> Làm thay đổi trạng thái proton hóa của các chuỗi bên (như ion hóa -COOH hoặc khử proton -NH3⁺), phá vỡ toàn bộ các cầu muối ion và liên kết hydro.",
        "<b>Ion kim loại nặng (Pb²⁺, Hg²⁺, Ag⁺) —</b> Phản ứng tạo phức chelate cực bền với nhóm -SH của Cystein, làm biến dạng cấu trúc không gian, kết tủa protein và bất hoạt enzym không hồi phục (cơ chế gây độc của chì và thủy ngân)."
    ],
    "Biến tính thuận nghịch xảy ra khi loại bỏ tác nhân biến tính protein có thể tự cuộn gập lại (như RNase A). Biến tính không thuận nghịch xảy ra khi các lõi kỵ nước bị phơi ra ngoài kết tụ vón cục vĩnh viễn không thể hòa tan lại."
))

cards.append(make_card(
    "HS07-B4-12",
    "Chaperone phân tử và Bệnh lý cuộn gập sai (Prion, Amyloidosis)",
    "BỆNH HỌC PHÂN TỬ PROTEIN",
    "Trình bày vai trò của Chaperone phân tử và cơ chế gây bệnh của Bệnh Prion và Bệnh Alzheimer do protein cuộn gập sai?",
    [
        "<b>Vai trò Chaperone phân tử —</b> Các họ protein hỗ trợ (Hsp70, Chaperonin GroEL/GroES) tiêu tốn năng lượng ATP để gắn và bảo vệ các vùng kỵ nước chưa cuộn gập, ngăn chặn sự kết tụ bất thường trong môi trường đông đúc của tế bào.",
        "<b>Cơ chế Bệnh Prion (Bệnh bò điên, Kuru, Creutzfeldt-Jakob) —</b> Protein Prion bình thường (PrP^C) giàu xoắn α bị biến đổi hình thể bất thường thành dạng gây bệnh (PrP^Sc) giàu phiến gấp β.",
        "<b>Tính chất lây nhiễm PrP^Sc —</b> PrP^Sc đóng vai trò khuôn mẫu độc hại cảm ứng các phân tử PrP^C bình thường biến đổi thành PrP^Sc, tạo các sợi amyloid không tan đề kháng protease, đục thủng mô não dạng bọt biển.",
        "<b>Bệnh Alzheimer —</b> Sự cuộn gập sai và vón tụ của chuỗi peptid β-Amyloid (Aβ42) tạo các mảng lão hóa ngoài tế bào, kết hợp protein Tau bị tăng phosphoryl hóa tạo các đám rối sợi thần kinh trong tế bào não gây thoái hóa nơ-ron tiến triển."
    ],
    "Bệnh lý cuộn gập sai (Protein Misfolding Diseases hay Proteopathies) mở ra một kỷ nguyên mới trong y học phân tử: một protein có cấu trúc bậc 1 hoàn toàn bình thường vẫn có thể gây bệnh chết người chỉ do thay đổi hình thái cuộn gập không gian bậc 2 và bậc 3."
))

# ==============================================================================
# SECTION B5: HÓA SINH CHUYÊN BIỆT CỦA HEMOGLOBIN VÀ MYOGLOBIN (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B5-01",
    "Đặc tính cấu trúc và phân bố của Myoglobin (Mb)",
    "HÓA SINH MYOGLOBIN",
    "Trình bày cấu tạo phân tử, phân bố mô học và chức năng sinh lý của Myoglobin?",
    [
        "<b>Phân bố mô học —</b> Hiện diện phong phú trong tế bào cơ vân (cơ xương) và cơ tim, chiếm khoảng 2% tổng lượng protein hòa tan của tế bào cơ.",
        "<b>Cấu trúc Monomer đơn chuỗi —</b> Trọng lượng phân tử 17 kDa, gồm duy nhất một chuỗi polypeptid gồm 153 acid amin kết hợp với 1 nhân Hem duy nhất.",
        "<b>8 đoạn xoắn α (A đến H) —</b> Chiếm tới 75 - 80% chiều dài chuỗi polypeptid, uốn thành 8 đoạn xoắn α đặt tên từ A đến H; các đoạn ngoặt nối tiếp được đặt tên ghép (AB, CD, EF, FG, GH).",
        "<b>Chức năng sinh học cốt lõi —</b> Dự trữ oxy nội bào tại mô cơ và hỗ trợ khuếch tán oxy nhanh chóng từ màng tế bào tới ty thể khi cơ bắp co rút mạnh tiêu thụ oxy tốc độ cao."
    ],
    "Myoglobin là protein đầu tiên trong lịch sử nhân loại được giải mã cấu trúc 3 chiều bằng tinh thể học tia X bởi John Kendrew (Giải Nobel Hóa học 1962). Cấu trúc của Myoglobin đặc biệt chặt chẽ, không có liên kết disulfur."
))

cards.append(make_card(
    "HS07-B5-02",
    "Túi kỵ nước của Myoglobin bảo vệ Fe2+",
    "HÓA SINH MYOGLOBIN",
    "Mô tả cấu tạo túi kỵ nước của Myoglobin và giải thích vì sao túi này bảo vệ ion Fe2+ không bị oxy hóa thành Fe3+?",
    [
        "<b>Lõi kỵ nước bao bọc nhân Hem —</b> Lõi phân tử Myoglobin chứa gần như tuyệt đối các acid amin kỵ nước không phân cực (Leu, Ile, Val, Phe), tạo nên một túi kỵ nước sâu kín.",
        "<b>Ngăn cách với môi trường nước —</b> Hai nhóm propionat tích điện âm của nhân Hem quay ra ngoài tiếp xúc với dung dịch, trong khi phần nhân porphyrin kỵ nước vùi sâu vào túi.",
        "<b>Bảo vệ trạng thái khử Ferrous (Fe²⁺) —</b> Trong dung dịch nước tự do, ion Fe²⁺ rất dễ bị phân tử nước và oxy oxy hóa nhanh chóng thành Fe³⁺ (trạng thái Ferric không gắn được oxy).",
        "<b>Duy trì chức năng gắn oxy thuận nghịch —</b> Túi kỵ nước ngăn chặn sự xâm nhập của các phân tử nước vào vị trí phối trí của sắt, cho phép phân tử oxy gắn kết và giải phóng một cách hoàn toàn thuận nghịch."
    ],
    "Nếu protein globin bị biến tính làm hở túi kỵ nước, nhân Hem sẽ lập tức tiếp xúc với nước và ion Fe²⁺ bị oxy hóa tức thì thành Fe³⁺, biến Myoglobin thành Metmyoglobin mất hoàn toàn chức năng hô hấp."
))

cards.append(make_card(
    "HS07-B5-03",
    "Cấu trúc Tetramer Bậc IV của Hemoglobin A (HbA)",
    "HÓA SINH HEMOGLOBIN",
    "Trình bày cấu tạo tetramer bậc IV của phân tử Hemoglobin A (HbA) ở người trưởng thành?",
    [
        "<b>Công thức phân tử tetramer α2β2 —</b> Trọng lượng phân tử 64,5 kDa, gồm 4 chuỗi polypeptid: hai chuỗi α và hai chuỗi β kết hợp chặt chẽ.",
        "<b>Chuỗi α (141 acid amin) —</b> Gồm 141 gốc acid amin, cuộn thành 7 đoạn xoắn α (thiếu đoạn xoắn D so với Myoglobin).",
        "<b>Chuỗi β (146 acid amin) —</b> Gồm 146 gốc acid amin, cuộn thành 8 đoạn xoắn α (từ A đến H, cấu trúc bậc 3 cực kỳ tương đồng với Myoglobin).",
        "<b>4 nhân Hem gắn tối đa 4 phân tử Oxy —</b> Mỗi chuỗi globin gắn với 1 nhân Hem riêng biệt; do đó một phân tử Hemoglobin tetramer chứa đúng 4 nhân Hem và có khả năng gắn tối đa 4 phân tử O2: Hb + 4 O2 ⇌ Hb(O2)4."
    ],
    "Mặc dù trình tự acid amin bậc 1 giữa chuỗi α, chuỗi β của Hemoglobin và Myoglobin chỉ tương đồng khoảng 18%, nhưng cấu trúc không gian 3 chiều bậc 3 của chúng lại giống hệt nhau (globin fold), minh chứng cho quy luật cấu trúc được bảo tồn chặt chẽ hơn trình tự."
))

cards.append(make_card(
    "HS07-B5-04",
    "Hai loại mặt tiếp xúc giữa các tiểu đơn vị của Hemoglobin",
    "HÓA SINH HEMOGLOBIN",
    "Phân biệt đặc điểm cấu tạo và chức năng của mặt tiếp xúc α1β1 so với mặt tiếp xúc α1β2 trong phân tử Hemoglobin?",
    [
        "<b>Hemoglobin là một dị tứ dimer —</b> Phân tử được xem như một phức hợp tạo bởi hai dimer bán phần: (α1β1) và (α2β2).",
        "<b>Mặt tiếp xúc α1β1 (và α2β2) —</b> Chứa hơn 30 gốc acid amin tiếp xúc cực kỳ chặt chẽ chủ yếu bởi các tương tác kỵ nước và liên kết hydro bền vững; KHÔNG THAY ĐỔI VỊ TRÍ trong suốt chu trình gắn nhả oxy.",
        "<b>Mặt tiếp xúc α1β2 (và α2β1) —</b> Chỉ chứa khoảng 19 gốc acid amin liên kết lỏng lẻo hơn bằng các cầu muối ion và liên kết hydro linh hoạt.",
        "<b>Bản lề trượt xoay 15° (Sliding Switch) —</b> Khi oxy gắn vào, mặt tiếp xúc α1β2 đóng vai trò bản lề cho phép hai dimer (α1β1) và (α2β2) xoay và trượt một góc 15° so với nhau, làm thay đổi cấu trúc toàn phân tử giữa dạng T và dạng R."
    ],
    "Đột biến tại các acid amin nằm trên mặt tiếp xúc α1β2 thường phá hủy tính hợp tác dị lập thể của Hemoglobin, khiến phân tử bị khóa cứng ở trạng thái ái lực cao hoặc ái lực thấp, gây đa hồng cầu hoặc thiếu máu."
))

cards.append(make_card(
    "HS07-B5-05",
    "Cấu tạo nhân Hem và vòng Protoporphyrin IX",
    "CẤU TẠO NHÂN HEM",
    "Mô tả cấu tạo hóa học của nhân Hem (Protoporphyrin IX) và trật tự phân bố các nhóm thế trên vòng?",
    [
        "<b>Nhân Porphin cơ bản —</b> Gồm 4 vòng dị vòng pyrrol (đánh số La Mã I đến IV) liên kết với nhau qua 4 cầu nối methenyl (-CH=), ký hiệu bằng các chữ Hy Lạp α, β, γ, δ.",
        "<b>8 nhóm thế trên Protoporphyrin IX —</b> Gồm 4 nhóm Methyl (-CH3, ký hiệu M ở vị trí 1, 3, 5, 8), 2 nhóm Vinyl (-CH=CH2, ký hiệu V ở vị trí 2, 4), và 2 nhóm Propionat (-CH2-CH2-COO⁻, ký hiệu P ở vị trí 6, 7).",
        "<b>Trật tự phân bố M-V-M-V-M-P-P-M —</b> Trật tự sắp xếp bất đối xứng đặc trưng của đồng phân IX trong tự nhiên.",
        "<b>Định hướng không gian trong túi globin —</b> Hai gốc Propionat mang điện tích âm quay ra phía ngoài tiếp xúc môi trường phân cực; các nhóm Methyl và Vinyl kỵ nước vùi sâu vào túi globin tương tác với chuỗi protein."
    ],
    "Ion sắt Fe²⁺ nằm ở chính giữa trung tâm của vòng protoporphyrin IX, liên kết với 4 nguyên tử Nitơ của 4 vòng pyrrol để tạo thành phân tử Hem hoàn chỉnh."
))

cards.append(make_card(
    "HS07-B5-06",
    "Sáu liên kết phối trí bát diện của ion Fe2+ trong Hem",
    "PHỐI TRÍ ION SẮT",
    "Mô tả 6 liên kết phối trí hình bát diện của ion Fe2+ trong phân tử Hemoglobin?",
    [
        "<b>Trạng thái sắt Ferrous (Fe²⁺) —</b> Ion sắt mang hóa trị 2, có 6 số phối trí phân bố theo hình bát diện không gian.",
        "<b>4 liên kết phối trí trong mặt phẳng (1 đến 4) —</b> Tạo bởi 4 nguyên tử Nitơ của 4 vòng pyrrol trong mặt phẳng phẳng của vòng protoporphyrin IX.",
        "<b>Liên kết phối trí thứ 5 (Vị trí trục đáy) —</b> Phối trí trực tiếp với nguyên tử Nitơ của gốc Histidin F8 (Histidin gần — Proximal Histidine).",
        "<b>Liên kết phối trí thứ 6 (Vị trí trục đỉnh) —</b> Là vị trí hở tự do để gắn kết thuận nghịch với một phân tử Oxy (O2) khi oxy hóa phân tử."
    ],
    "Sự chiếm chỗ của phân tử oxy tại vị trí phối trí thứ 6 làm thay đổi cấu hình trường phối tử electron của ion Fe²⁺, biến ion này từ trạng thái spin cao (bán kính lớn) sang trạng thái spin thấp (bán kính nhỏ)."
))

cards.append(make_card(
    "HS07-B5-07",
    "Vai trò của Histidin gần F8 (Proximal Histidine)",
    "TƯƠNG TÁC GLOBIN VÀ HEM",
    "Xác định vị trí và phân tích vai trò cơ học của gốc Histidin gần F8 đối với chức năng của Hemoglobin?",
    [
        "<b>Vị trí phân tử —</b> Là gốc Histidin thứ 8 trên đoạn xoắn F của chuỗi globin (vị trí His87 trên chuỗi α hoặc His92 trên chuỗi β).",
        "<b>Chân neo liên kết trực tiếp Fe²⁺ —</b> Tạo liên kết phối trí cộng hóa trị thứ 5 với ion sắt, đóng vai trò chân neo cơ học duy nhất gắn chặt nhân Hem vào khung xương polypeptid của globin.",
        "<b>Truyền chuyển động khi gắn Oxy —</b> Khi oxy gắn vào liên kết thứ 6, ion Fe²⁺ bị kéo thụt vào mặt phẳng porphyrin, kéo theo Histidin F8 dịch chuyển khoảng 0,6 Å.",
        "<b>Kích hoạt chuyển đổi dạng T → R —</b> Sự dịch chuyển của His F8 kéo theo toàn bộ đoạn xoắn F, truyền xung lực cơ học làm đứt gãy mạng lưới cầu muối và xoay bản lề α1β2 chuyển phân tử sang trạng thái R."
    ],
    "Histidin F8 hoạt động như một 'đòn bẩy cơ học phân tử'. Không có Histidin F8, chuyển động tinh vi của nguyên tử sắt khi tiếp nhận oxy sẽ không thể truyền tải tới khung xương protein để tạo nên tính hợp tác dị lập thể."
))

cards.append(make_card(
    "HS07-B5-08",
    "Vai trò của Histidin xa E7 (Distal Histidine)",
    "TƯƠNG TÁC GLOBIN VÀ HEM",
    "Xác định vị trí và phân tích vai trò của Histidin xa E7 trong việc ổn định Oxy và ngăn ngừa ngộ độc khí CO?",
    [
        "<b>Vị trí phân tử —</b> Là gốc Histidin thứ 7 trên đoạn xoắn E của globin (vị trí His58 trên chuỗi α hoặc His63 trên chuỗi β), nằm ở phía đối diện mặt phẳng Hem.",
        "<b>Không gắn trực tiếp Fe²⁺ —</b> Nằm gần vị trí gắn oxy thứ 6 nhưng không tạo liên kết phối trí trực tiếp với ion sắt.",
        "<b>Ổn định phân tử Oxy —</b> Tạo một liên kết hydro yếu với phân tử O2 đã gắn vào Fe²⁺, giúp làm bền phức hợp Oxyhemoglobin và ngăn cản oxy thoát ra dưới dạng gốc tự do superoxide (O2•⁻).",
        "<b>Tạo chướng ngại không gian chống CO —</b> Cản trở lập thể bắt buộc phối tử gắn vào Fe²⁺ phải nằm nghiêng một góc 120°, làm suy giảm nghiêm trọng ái lực gắn của khí độc Carbon Monoxid (CO)."
    ],
    "Nếu đột biến thay thế Histidin E7 bằng một acid amin nhỏ hơn (như Glycin), tính chọn lọc oxy bị suy giảm và ái lực của hemoglobin với CO sẽ tăng vọt, khiến cơ thể dễ bị ngộ độc CO ngay cả ở nồng độ vết trong không khí."
))

cards.append(make_card(
    "HS07-B5-09",
    "Cơ chế ngăn ngừa ngộ độc khí Carbon Monoxid (CO) của Histidin E7",
    "HÓA SINH LÂM SÀNG CO",
    "Giải thích cơ chế phân tử giúp chuỗi globin làm giảm ái lực của khí CO đối với Hemoglobin từ 20.000 lần xuống còn 200 lần?",
    [
        "<b>Ái lực của Hem tự do ngoài môi trường —</b> Đối với phân tử Hem tự do nằm ngoài dung dịch, phân tử CO gắn vuông góc thẳng đứng 180° với mặt phẳng Hem, với ái lực cực mạnh GẤP 20.000 LẦN so với O2.",
        "<b>Cản trở lập thể của Histidin E7 —</b> Trong túi globin của Hb và Mb, gốc Histidin E7 nằm chắn ngay trên trục thẳng đứng, bắt buộc phối tử phải gắn nghiêng một góc khoảng 120°.",
        "<b>Oxy tự nhiên có liên kết nghiêng —</b> Phân tử O2 vốn có cấu hình liên kết phối trí nghiêng 120° nên khớp hoàn hảo với túi globin và được Histidin E7 tạo liên kết hydro ổn định.",
        "<b>CO bị ép gắn nghiêng làm giảm ái lực —</b> Khí CO bị ép phải gắn nghiêng làm biến dạng liên kết orbital, làm sụt giảm ái lực của CO với Hb xuống khoảng 100 lần, chỉ còn cao gấp khoảng 200 - 250 lần so với O2."
    ],
    "Mặc dù ái lực đã giảm 100 lần nhờ Histidin E7, tỷ lệ 200 - 250 lần vẫn đủ để CO chiếm chỗ O2 ở nồng độ thấp trong khói đám cháy hoặc khí thải xe máy, gây ngộ độc Carboxyhemoglobin đe dọa tính mạng."
))

cards.append(make_card(
    "HS07-B5-10",
    "Chức năng kép của Hemoglobin trong vận chuyển khí máu",
    "SINH LÝ HÓA SINH HÔ HẤP",
    "Phân tích chức năng kép của Hemoglobin trong việc vận chuyển Oxy và đào thải CO2 cùng ion H+?",
    [
        "<b>1. Vận chuyển Oxy từ phổi đến mô —</b> Thu nhận 4 phân tử O2 tại mao mạch phế nang phổi (phân áp pO2 cao 100 mmHg) và giải phóng O2 tại các mô ngoại vi đang chuyển hóa (pO2 thấp 20 - 40 mmHg).",
        "<b>2. Vận chuyển proton H⁺ từ mô về phổi —</b> Đệm và vận chuyển các ion H⁺ sinh ra từ acid lactic và chuyển hóa mô thông qua hiệu ứng Bohr, ngăn ngừa toan hóa máu ngoại vi.",
        "<b>3. Vận chuyển CO2 dạng Carbamin —</b> Vận chuyển trực tiếp khoảng 15% tổng lượng CO2 sinh ra từ mô dưới dạng Carbamino-Hemoglobin gắn vào đầu N-tận của các chuỗi globin.",
        "<b>Hỗ trợ hệ đệm Bicarbonat —</b> Xúc tác chuyển đổi 80% CO2 còn lại thành ion Bicarbonat (HCO3⁻) trong hồng cầu nhờ enzym Carbonic Anhydrase để hòa tan vận chuyển trong huyết tương."
    ],
    "Hemoglobin là một phương tiện vận chuyển khí máu hoàn hảo 2 chiều: chiều đi mang oxy dưỡng khí cho mô tế bào, chiều về gom sạch phế phẩm chuyển hóa (H⁺ và CO2) đưa về phổi để đào thải ra ngoài."
))

cards.append(make_card(
    "HS07-B5-11",
    "Thành phần các loại Hemoglobin ở người trưởng thành bình thường",
    "CÁC THỂ HEMOGLOBIN BÌNH THƯỜNG",
    "Nêu công thức cấu tạo và tỷ lệ phần trăm bình thường của 3 loại Hemoglobin trong máu người trưởng thành?",
    [
        "<b>1. Hemoglobin A1 (HbA1 — α2β2) —</b> Chiếm tỷ lệ áp đảo 95% đến 98% tổng lượng Hemoglobin; gồm 2 chuỗi α và 2 chuỗi β, đảm nhận vai trò vận chuyển oxy chính.",
        "<b>2. Hemoglobin A2 (HbA2 — α2δ2) —</b> Chiếm tỷ lệ nhỏ từ 1,5% đến 3,0%; gồm 2 chuỗi α và 2 chuỗi δ; tỷ lệ HbA2 > 3,5% là dấu ấn chẩn đoán xác định thể nhẹ mang gen β-Thalassemia.",
        "<b>3. Hemoglobin F (HbF — α2γ2) —</b> Chiếm tỷ lệ vết < 1% ở người lớn (thường 0,5%); gồm 2 chuỗi α và 2 chuỗi γ; là huyết sắc tố chính trong thời kỳ bào thai.",
        "<b>Hemoglobin A1c (HbA1c) —</b> Phân đoạn HbA bị gắn đường glucose không qua enzym (glycation); chiếm 4% đến 5,6% ở người bình thường, dùng để theo dõi đường huyết 3 tháng qua ở bệnh nhân đái tháo đường."
    ],
    "Cụm gen alpha-globin nằm trên nhiễm sắc thể số 16 (gồm gen zeta và 2 gen alpha), trong khi cụm gen beta-globin nằm trên nhiễm sắc thể số 11 (gồm gen epsilon, 2 gen gamma, gen delta và gen beta)."
))

cards.append(make_card(
    "HS07-B5-12",
    "Sự chuyển dịch Hemoglobin trong quá trình phát triển cá thể",
    "PHÁT TRIỂN CÁ THỂ VÀ HUYẾT SẮC TỐ",
    "Mô tả sự chuyển dịch các loại chuỗi globin từ thời kỳ phôi thai, thai nhi đến sau khi sinh?",
    [
        "<b>Thời kỳ phôi thai (Embryonic — vài tuần đầu) —</b> Tổng hợp chuỗi dạng ζ (giống α) và chuỗi ε (giống β) tạo các Hemoglobin phôi thai: Gower-1 (ζ2ε2), Gower-2 (α2ε2), và Portland (ζ2γ2).",
        "<b>Thời kỳ thai nhi (Fetal — từ tháng thứ 3 đến sinh) —</b> Gan và lách thai nhi chuyển sang tổng hợp chủ yếu chuỗi α và chuỗi γ, tạo nên Hemoglobin F (HbF — α2γ2) chiếm tới 90% lượng Hb lúc sinh.",
        "<b>Bước chuyển dịch sau sinh (Giai đoạn chuyển từ γ sang β) —</b> Từ tuần thứ 30 của thai kỳ và đặc biệt sau khi chào đời, tủy xương giảm dần tổng hợp chuỗi γ và tăng vọt tổng hợp chuỗi β.",
        "<b>Hoàn tất ở 6 tháng tuổi —</b> Đến 6 tháng sau sinh, HbF giảm xuống < 1 - 2% và HbA (α2β2) vươn lên chiếm ưu thế tuyệt đối > 95%; giải thích vì sao bệnh β-Thalassemia thể nặng chỉ biểu hiện triệu chứng thiếu máu rõ rệt từ 6 tháng tuổi trở đi."
    ],
    "Sự chuyển dịch từ tổng hợp chuỗi gamma sang chuỗi beta được điều hòa bởi các yếu tố phiên mã đặc hiệu như BCL11A. Các thuốc ức chế BCL11A hoặc kích hoạt lại tổng hợp HbF (như Hydroxyurea) là liệu pháp điều trị trúng đích cho bệnh hồng cầu hình liềm và beta-thalassemia."
))

# ==============================================================================
# SECTION B6: ĐỘNG HỌC GẮN OXY, TÍNH HỢP TÁC DỊ LẬP THỂ VÀ HIỆU ỨNG BOHR (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B6-01",
    "So sánh đường cong phân ly oxy của Myoglobin và Hemoglobin",
    "ĐỘNG HỌC GẮN OXY",
    "So sánh hình thái đường cong phân ly oxy, chỉ số P50 và hiệu suất vận chuyển oxy của Myoglobin so với Hemoglobin?",
    [
        "<b>Đường cong Myoglobin dạng Hyperbol —</b> Do Myoglobin là monomer đơn chuỗi không có tính hợp tác dị lập thể; tuân theo động học phối tử đơn giản tương tự Michaelis-Menten.",
        "<b>Chỉ số P50 của Myoglobin cực thấp (2 - 3 mmHg) —</b> Ở phân áp oxy mao mạch lúc nghỉ (pO2 = 40 mmHg), Mb bão hòa > 95% oxy; Mb giữ oxy rất chặt và chỉ chịu nhả oxy khi pO2 mô giảm sâu < 5 mmHg (thiếu oxy mô trầm trọng), đóng vai trò dự trữ oxy.",
        "<b>Đường cong Hemoglobin dạng Xích-ma chữ S —</b> Phản ánh tính hợp tác dị lập thể dương tính của tetramer; chỉ số P50 của HbA bình thường khoảng 26 - 27 mmHg.",
        "<b>Hiệu suất vận chuyển oxy vượt trội —</b> Tại phổi (pO2 = 100 mmHg) Hb bão hòa 98%; tại mô nghỉ (pO2 = 40 mmHg) bão hòa 75% (nhả 23% oxy); tại mô cơ vận động (pO2 = 20 mmHg) độ bão hòa sụt xuống 25 - 35% (nhả tới 65 - 75% oxy); hiệu suất vận chuyển gấp 1,8 lần so với protein dạng hyperbol."
    ],
    "Đoạn dốc nhất của đường cong chữ S của Hemoglobin nằm đúng trong khoảng pO2 sinh lý của các mô ngoại vi (20 - 40 mmHg), cho phép giải phóng ồ ạt oxy chỉ với một sự sụt giảm rất nhỏ của phân áp oxy mô."
))

cards.append(make_card(
    "HS07-B6-02",
    "Mô hình dị lập thể T ⇌ R của Hemoglobin (Monod - Perutz)",
    "ĐIỀU HÒA DỊ LẬP THỂ",
    "Phân tích cơ chế phân tử chuyển đổi giữa trạng thái T (Tense) và trạng thái R (Relaxed) của phân tử Hemoglobin?",
    [
        "<b>Trạng thái T (Tense state — Trạng thái Căng) —</b> Cấu trúc ưu thế của Deoxyhemoglobin; ion Fe²⁺ có bán kính lớn bị đẩy lồi ra ngoài mặt phẳng porphyrin 0,4 Å về phía His F8; tetramer bị khóa cứng bởi 8 cầu muối ion liên chuỗi; ái lực với oxy rất thấp.",
        "<b>Bước nhảy phân tử khi Oxy gắn vào —</b> Khi O2 gắn vào phối trí thứ 6, electron tái phân bố làm co bán kính Fe²⁺, kéo ion sắt tụt khít vào mặt phẳng vòng porphyrin.",
        "<b>Chuyển động cơ học của His F8 —</b> Kéo Histidin F8 dịch chuyển 0,6 Å, kéo theo đoạn xoắn F và làm đứt gãy hoàn toàn mạng lưới cầu muối ion liên chuỗi.",
        "<b>Trạng thái R (Relaxed state — Trạng thái Giãn) —</b> Hai dimer xoay 15° trượt lên nhau làm hốc trung tâm co hẹp lại; phơi bày các vị trí Hem còn lại và LÀM TĂNG ÁI LỰC GẮN OXY CỦA CÁC TIỂU ĐƠN VỊ TIẾP THEO LÊN HÀNG TRĂM LẦN."
    ],
    "Mô hình MWC (Monod-Wyman-Changeux) giải thích chuyển đổi đồng loạt toàn bộ tetramer, trong khi mô hình KNF (Koshland-Némethy-Filmer) giải thích chuyển đổi tuần tự từng tiểu đơn vị; cấu trúc thực tế của Hemoglobin kết hợp cả hai cơ chế."
))

cards.append(make_card(
    "HS07-B6-03",
    "Tính hợp tác dương và Hệ số Hill (nH)",
    "ĐỘNG HỌC PHỐI TỬ",
    "Định nghĩa tính hợp tác dương (Positive Cooperativity) trong phân tử Hemoglobin và ý nghĩa của Hệ số Hill (nH)?",
    [
        "<b>Định nghĩa tính hợp tác dương —</b> Hiện tượng việc gắn kết một phân tử phối tử (O2) đầu tiên lên một tiểu đơn vị làm biến đổi không gian lan tỏa sang các tiểu đơn vị khác, làm tăng ái lực gắn O2 của các tiểu đơn vị kế tiếp trong cùng một tetramer.",
        "<b>Hệ số Hill (nH) —</b> Chỉ số định lượng mức độ hợp tác liên chuỗi giữa các vị trí gắn phối tử trên đại phân tử.",
        "<b>nH = 1,0 ở Myoglobin —</b> Myoglobin là monomer đơn chuỗi, các vị trí hoạt động độc lập hoàn toàn không có tương tác hợp tác.",
        "<b>nH ≈ 2,8 - 3,0 ở Hemoglobin —</b> Giá trị nH thực nghiệm của Hemoglobin người đạt từ 2,8 đến 3,0 (vượt xa 1,0), phản ánh tính hợp tác dị lập thể dương tính cực kỳ mạnh mẽ."
    ],
    "Nếu hệ số Hill nH < 1 thì gọi là hợp tác âm tính (việc gắn ligand đầu tiên làm giảm ái lực các vị trí sau). Hệ số Hill tối đa về mặt lý thuyết của Hemoglobin bằng 4 (bằng số tiểu đơn vị), thực tế đạt 2,8 - 3,0 do trạng thái chuyển tiếp."
))

cards.append(make_card(
    "HS07-B6-04",
    "Cơ chế phân tử của Hiệu ứng Bohr tại mô ngoại vi",
    "HIỆU ỨNG BOHR",
    "Phân tích cơ chế phân tử của Hiệu ứng Bohr tại mao mạch mô chuyển hóa (vai trò của H+ và Histidin 146 chuỗi β)?",
    [
        "<b>Môi trường toan hóa tại mô —</b> Mô hoạt động chuyển hóa mạnh liên tục tạo CO2 và acid lactic, làm tăng nồng độ proton [H⁺] (pH giảm xuống khoảng 7,2).",
        "<b>Proton hóa Histidin 146 chuỗi β —</b> Nồng độ H⁺ cao thúc đẩy phản ứng proton hóa vòng imidazol của gốc His146 ở đầu C-tận chuỗi β, khiến gốc này tích điện dương.",
        "<b>Hình thành cầu muối khóa bền dạng T —</b> His146 tích điện dương lập tức tạo cầu muối ion cực mạnh với gốc Aspartat 94 tích điện âm nằm trên cùng chuỗi β.",
        "<b>Kích thích Hemoglobin giải phóng Oxy —</b> Cầu muối giúp khóa chặt và làm bền trạng thái T (Tense state); trạng thái T có ái lực thấp với oxy, buộc Hemoglobin phải NHẢ OXY CHO MÔ ĐANG ĐÓI DƯỠNG KHÍ; đường cong phân ly oxy dịch sang PHẢI (tăng P50)."
    ],
    "Hiệu ứng Bohr do Christian Bohr phát hiện năm 1904: Môi trường acid và tăng CO2 tại mô ngoại vi đóng vai trò 'chìa khóa' mở khóa để Hemoglobin giải phóng nguồn oxy dự trữ cho tế bào."
))

cards.append(make_card(
    "HS07-B6-05",
    "Cơ chế phân tử của Hiệu ứng Bohr tại phế nang phổi",
    "HIỆU ỨNG BOHR",
    "Trình bày cơ chế phân tử của Hiệu ứng Bohr tại mao mạch phế nang phổi giúp thu nhận oxy và đào thải CO2?",
    [
        "<b>Oxy gắn ép chuyển sang dạng R —</b> Tại phổi, phân áp pO2 cao (100 mmHg) thúc đẩy oxy gắn vào Hemoglobin, ép tetramer chuyển sang trạng thái R (Relaxed state).",
        "<b>Đứt gãy cầu muối His146 - Asp94 —</b> Sự chuyển sang dạng R làm thay đổi môi trường vi mô lân cận, làm sụt giảm giá trị pKa của His146 từ 8,0 xuống 6,5.",
        "<b>Giải phóng proton H⁺ tự do —</b> Do pKa sụt giảm xuống dưới pH máu (6,5 < 7,4), His146 buộc phải nhả proton H⁺ ra ngoài dung dịch.",
        "<b>Tái tạo CO2 đào thải ra ngoài —</b> Proton H⁺ phản ứng ngay với ion Bicarbonat (HCO3⁻) dưới xúc tác của Carbonic Anhydrase: H⁺ + HCO3⁻ ⇌ H2CO3 ⇌ H2O + CO2 ↑; khí CO2 khuếch tán ra phế nang thở ra ngoài; đường cong dịch sang TRÁI tăng tối đa ái lực nạp O2."
    ],
    "Hiệu ứng Haldane bổ trợ cho hiệu ứng Bohr: Sự gắn oxy vào Hemoglobin tại phổi thúc đẩy giải phóng CO2 ra khỏi máu; ngược lại sự khử oxy của Hemoglobin tại mô làm tăng khả năng nhận CO2 và đệm proton H⁺."
))

cards.append(make_card(
    "HS07-B6-06",
    "Vận chuyển CO2 dạng Carbamino-Hemoglobin",
    "VẬN CHUYỂN KHÍ MÁU",
    "Mô tả cơ chế gắn kết của CO2 với phân tử Hemoglobin tạo thành Carbamino-Hemoglobin và tác động dị lập thể của nó?",
    [
        "<b>Vị trí gắn kết đầu N-tận —</b> Khoảng 15% lượng CO2 sinh ra từ chuyển hóa mô phản ứng thuận nghịch trực tiếp với các nhóm α-amin không ion hóa (-NH2) ở đầu N-tận của các chuỗi globin.",
        "<b>Phương trình phản ứng tạo Carbamat —</b> Hb-NH2 + CO2 ⇌ Hb-NH-COO⁻ + H⁺; tạo thành dẫn xuất Carbamino-Hemoglobin.",
        "<b>Giải phóng thêm proton H⁺ —</b> Phản ứng gắn carbamat tạo thêm ion H⁺, góp phần khuếch đại hiệu ứng Bohr kích thích nhả thêm oxy.",
        "<b>Khóa bền trạng thái T —</b> Nhóm carbamat mang điện tích âm (-COO⁻) ở đầu N-tận tham gia hình thành thêm các cầu muối ion liên chuỗi, giúp khóa chặt trạng thái Tense T và thúc đẩy giải phóng oxy nhả cho mô."
    ],
    "Tại mao mạch phổi, phân áp pO2 cao ép Hemoglobin chuyển sang trạng thái R, làm phá vỡ các cầu muối liên chuỗi và làm đảo chiều phản ứng carbamat, giải phóng CO2 tự do khuếch tán vào phế nang để thở ra ngoài."
))

cards.append(make_card(
    "HS07-B6-07",
    "Nguồn gốc sinh hóa và cấu trúc gắn của 2,3-Bisphosphoglycerat (2,3-BPG)",
    "ĐIỀU HÒA DỊ LẬP THỂ 2,3-BPG",
    "Trình bày nguồn gốc sinh hóa của 2,3-BPG trong hồng cầu và cơ chế phân tử khi nó gắn vào khoang trung tâm của Hemoglobin?",
    [
        "<b>Nguồn gốc từ nhánh Rapoport-Luebering —</b> Trong hồng cầu, chất trung gian 1,3-BPG của đường phân chuyển thành 2,3-BPG nhờ enzym lưỡng chức BPG Mutase/Phosphatase; nồng độ 2,3-BPG trong hồng cầu rất cao (khoảng 5 mmol/L).",
        "<b>Cấu trúc anion đậm đặc —</b> Phân tử 2,3-BPG mang tổng cộng 5 ĐIỆN TÍCH ÂM ở pH sinh lý 7,4 (gồm 1 nhóm carboxylat và 2 nhóm phosphat).",
        "<b>Vị trí gắn khoang trung tâm (Central Cavity) —</b> Ở trạng thái T (Deoxy-Hb), giữa 2 chuỗi β mở ra một khoang rỗng trung tâm được lót bởi các acid amin tích điện dương: hai gốc His2, hai gốc Lys82, hai gốc His143 và hai nhóm amin đầu Val1.",
        "<b>Cơ chế 'Then chốt cài cửa' —</b> Đúng MỘT phân tử 2,3-BPG lọt vào khoang trung tâm tạo mạng lưới liên kết ion tĩnh điện dày đặc với 2 chuỗi β, KHÓA CHẶT TRẠNG THÁI T, LÀM GIẢM ÁI LỰC VỚI OXY VÀ KÉO ĐƯỜNG CONG SANG PHẢI."
    ],
    "Khi oxy gắn vào ép phân tử chuyển sang trạng thái R, hai dimer xoay trượt làm khoang trung tâm co hẹp lại, phân tử 2,3-BPG bị đẩy văng ra ngoài dung dịch."
))

cards.append(make_card(
    "HS07-B6-08",
    "Ý nghĩa lâm sàng của 2,3-BPG: Thích nghi độ cao và Máu lưu trữ",
    "HÓA SINH LÂM SÀNG 2,3-BPG",
    "Phân tích vai trò của 2,3-BPG trong sự thích nghi khi lên vùng núi cao và giải thích hiện tượng suy kiệt 2,3-BPG trong máu truyền lưu trữ?",
    [
        "<b>Thích nghi vùng núi cao (> 4000 m) —</b> Không khí loãng gây giảm pO2 máu; trong vòng 24 - 48 giờ cơ thể phản ứng bằng cách tăng tổng hợp 2,3-BPG trong hồng cầu từ 5 mM lên 8 mM.",
        "<b>Tác động thích nghi —</b> 2,3-BPG tăng cao kéo đường cong phân ly oxy sang PHẢI (tăng P50 từ 26 lên 31 mmHg), giúp hồng cầu dễ dàng nhả thêm oxy cho các mô cơ quan đang đói dưỡng khí.",
        "<b>Suy kiệt 2,3-BPG trong máu lưu trữ —</b> Máu bảo quản trong ngân hàng máu quá 1 - 2 tuần bị cạn kiệt 2,3-BPG do đường phân bị ức chế trong môi trường toan bảo quản.",
        "<b>Hậu quả truyền máu lưu trữ lâu —</b> Hemoglobin thiếu 2,3-BPG có ái lực quá cao với oxy (đường cong lệch sâu sang TRÁI, P50 giảm sâu), dẫn đến hiện tượng 'bắt giữ oxy' không chịu nhả cho mô của bệnh nhân nhận máu, có thể gây thiếu oxy mô cấp; ngân hàng máu hiện đại bổ sung Inosine để duy trì tổng hợp 2,3-BPG."
    ],
    "Inosine có thể đi qua màng hồng cầu và chuyển hóa thành Ribose-5-phosphat rồi đi vào con đường đường phân để tái tạo 2,3-BPG và ATP trong các túi máu lưu trữ kéo dài."
))

cards.append(make_card(
    "HS07-B6-09",
    "Cơ chế phân tử giúp Hemoglobin thai nhi (HbF) có ái lực oxy cao hơn HbA",
    "HÓA SINH HEMOGLOBIN THAI NHI",
    "Giải thích cơ chế sinh học phân tử vì sao Hemoglobin F (HbF) có ái lực oxy cao hơn Hemoglobin A của người mẹ?",
    [
        "<b>Cấu trúc chuỗi γ của HbF (α2γ2) —</b> HbF gồm 2 chuỗi α và 2 chuỗi γ (thay vì 2 chuỗi β như ở người lớn).",
        "<b>Đột biến thay thế vị trí 143 —</b> Trên chuỗi γ của HbF, vị trí số 143 là Serin (trung hòa không mang điện) thay vì Histidin 143 (tích điện dương) như trên chuỗi β của HbA.",
        "<b>Mất 2 điện tích dương ở khoang trung tâm —</b> Khoang trung tâm của HbF mất đi hai điện tích dương đối xứng, khiến HbF GẮN RẤT LỎNG LẺO VỚI PHÂN TỬ 2,3-BPG.",
        "<b>Hậu quả ái lực oxy cao vượt trội —</b> Do ít bị chất ức chế dị lập thể 2,3-BPG kìm hãm, đường cong của HbF lệch sang TRÁI với P50 ≈ 19 mmHg (so với P50 = 26 - 27 mmHg của mẹ), tạo lực hút oxy một chiều rút oxy từ máu mẹ qua rau thai sang máu thai nhi."
    ],
    "Nếu đo phân tử Hemoglobin tinh khiết không có mặt 2,3-BPG trong ống nghiệm, HbA và HbF có ái lực gắn oxy ngang ngửa nhau. Sự khác biệt về ái lực sinh lý hoàn toàn bắt nguồn từ sự tương tác khác biệt với 2,3-BPG nội bào."
))

cards.append(make_card(
    "HS07-B6-10",
    "Tổng kết các yếu tố làm dịch chuyển đường cong Barcroft",
    "ĐƯỜNG CONG BARCROFT",
    "Tổng hợp các yếu tố làm dịch chuyển đường cong phân ly Oxy sang PHẢI và sang TRÁI theo quy tắc CADET?",
    [
        "<b>Dịch chuyển sang PHẢI (Right shift — Tăng P50, Giảm ái lực, Kích thích NHẢ OXY) —</b> Tăng nồng độ H⁺ (giảm pH - toan máu), Tăng phân áp pCO2, Tăng nhiệt độ cơ thể (sốt, vận động), Tăng nồng độ 2,3-BPG (vùng cao, thiếu máu mạn).",
        "<b>Mẹo nhớ kinh điển 'CADET, face Right' —</b> CO2, Acid, 2,3-DPG, Exercise, Temperature tăng đều làm đường cong quay sang PHẢI.",
        "<b>Dịch chuyển sang TRÁI (Left shift — Giảm P50, Tăng ái lực, BẮT GIỮ OXY) —</b> Giảm H⁺ (tăng pH - kiềm máu), Giảm pCO2 (tăng thông khí), Hạ thân nhiệt, Giảm 2,3-BPG (máu truyền lưu trữ), Hemoglobin thai nhi (HbF).",
        "<b>Ngộ độc Carbon Monoxid (CO) và Methemoglobin —</b> Vừa làm đường cong dịch chuyển lệch sang TRÁI vừa làm DẸT ĐỈNH tối đa; giữ chặt oxy ở các vị trí còn lại và ngăn chặn hoàn toàn sự nhả oxy cho mô."
    ],
    "Quy luật sinh lý học: Bất kỳ tình trạng nào làm tăng nhu cầu chuyển hóa năng lượng của mô (vận động gắng sức sinh acid lactic, tăng thân nhiệt, tạo CO2) đều kéo đường cong sang Phải để ưu tiên cấp oxy tối đa cho mô."
))

# ==============================================================================
# SECTION B7: BỆNH HỌC PHÂN TỬ CỦA HEMOGLOBIN (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-B7-01",
    "Bệnh Hồng cầu hình liềm (HbS): Đột biến gen và cấu trúc phân tử",
    "BỆNH HỌC PHÂN TỬ HEMOGLOBIN",
    "Trình bày bản chất đột biến gen và biến đổi cấu trúc bậc I của chuỗi β-globin trong Bệnh Hồng cầu hình liềm (HbS)?",
    [
        "<b>Đột biến điểm đơn nucleotid —</b> Đột biến thay thế một base đơn lẻ trên gen HBB mã hóa chuỗi β-globin (nằm trên nhánh ngắn NST số 11): codon thứ 6 bị đột biến từ GAG chuyển thành GTG.",
        "<b>Thay thế acid amin β6 Glu → Val (E6V) —</b> Gốc Glutamat (mang điện tích âm, ưa nước cao) tại vị trí số 6 chuỗi β bị thay thế bằng gốc Valin (không phân cực, kỵ nước).",
        "<b>Công thức phân tử HbS —</b> Ký hiệu là α2β2^S; phân tử chứa 2 chuỗi α bình thường và 2 chuỗi β mang đột biến E6V.",
        "<b>Trạng thái hòa tan khi gắn Oxy —</b> Khi phân tử HbS ở trạng thái bão hòa oxy (Oxy-HbS, dạng R), phân tử vẫn duy trì trạng thái hòa tan tương đối bình thường trong tế bào hồng cầu."
    ],
    "Bệnh Hồng cầu hình liềm là bệnh lý phân tử đầu tiên được Linus Pauling định danh là 'Molecular Disease' vào năm 1949, mở ra kỷ nguyên y học phân tử dựa trên bằng chứng đột biến gen."
))

cards.append(make_card(
    "HS07-B7-02",
    "Cơ chế trùng hợp sợi polymer của Deoxy-HbS",
    "BỆNH HỌC PHÂN TỬ HEMOGLOBIN",
    "Phân tích cơ chế bệnh sinh phân tử dẫn đến sự trùng hợp tạo sợi polymer không tan của Deoxy-HbS?",
    [
        "<b>Chuyển sang dạng Deoxy (trạng thái T) —</b> Khi hồng cầu đi qua các mô ngoại vi có pO2 thấp hoặc toan máu, HbS nhả oxy và chuyển sang trạng thái khử oxy Deoxy-HbS (dạng T).",
        "<b>Lộ diện hốc kỵ nước Phe85 - Leu88 —</b> Ở trạng thái T, trên bề mặt chuỗi β1 xuất hiện một 'chỗ lõm kỵ nước' tự nhiên tạo bởi các gốc Phe85 và Leu88.",
        "<b>Valin 6 cắm khít vào hốc kỵ nước —</b> Gốc đột biến Valin 6 kỵ nước bất thường của chuỗi β trên phân tử Deoxy-HbS kế cận khớp khít hoàn hảo vào chỗ lõm kỵ nước này thông qua tương tác kỵ nước.",
        "<b>Trùng hợp chuỗi polymer dạng sợi (Tactoids) —</b> Kích hoạt phản ứng dây chuyền tự lắp ráp: hàng ngàn phân tử Deoxy-HbS vón tụ tạo thành các sợi polymer xoắn dài không tan, làm biến dạng hồng cầu mềm mại thành hình lưỡi liềm cứng quắc."
    ],
    "Tốc độ trùng hợp phụ thuộc vào lũy thừa bậc cao của nồng độ Deoxy-HbS (khoảng lũy thừa bậc 30). Do đó, chỉ cần một sự sụt giảm nhẹ oxy máu hoặc mất nước làm cô đặc hồng cầu sẽ kích hoạt phản ứng trùng hợp bùng nổ tức thì."
))

cards.append(make_card(
    "HS07-B7-03",
    "Hậu quả lâm sàng của Bệnh Hồng cầu hình liềm",
    "BỆNH HỌC LÂM SÀNG HEMOGLOBIN",
    "Trình bày 3 hậu quả lâm sàng kinh điển của Bệnh Hồng cầu hình liềm (cơn tắc mạch, tan máu mạn và teo lách tự nhiên)?",
    [
        "<b>1. Cơn đau tắc mạch (Vaso-occlusive Crises) —</b> Hồng cầu hình liềm cứng ngắc, mất tính đàn hồi bị kẹt lại tại các vi mao mạch, gây tắc mạch máu nuôi dưỡng cục bộ, đau xương khớp dữ dội, hoại tử vô mạch chỏm xương đùi và hội chứng ngực cấp (Acute Chest Syndrome).",
        "<b>2. Thiếu máu tan máu mạn tính —</b> Hồng cầu hình liềm bị đại thực bào hệ võng nội mô nhận diện và tiêu hủy ồ ạt tại lách và gan, rút ngắn đời sống hồng cầu từ 120 ngày xuống chỉ còn 10 - 20 ngày, gây vàng da tăng bilirubin gián tiếp và sỏi mật sắc tố.",
        "<b>3. Teo lách tự nhiên (Autosplenectomy) —</b> Các ổ nhồi máu lách vi thể tái diễn liên tục trong những năm đầu đời làm mô lách bị xơ hóa và teo biến mất hoàn toàn trước 6 - 8 tuổi.",
        "<b>Nguy cơ nhiễm trùng huyết vi khuẩn có vỏ —</b> Mất chức năng lọc miễn dịch của lách khiến bệnh nhân có nguy cơ tử vong rất cao do nhiễm trùng huyết bởi vi khuẩn có vỏ bọc (Streptococcus pneumoniae, Haemophilus influenzae, Salmonella gây viêm tủy xương)."
    ],
    "Tại sao gen đột biến HbS vẫn tồn tại với tần số cao ở vùng Châu Phi cận Sahara? Người mang gen dị hợp tử HbS (HbAS - Sickle cell trait) có khả năng đề kháng chọn lọc tự nhiên chống lại thể ác tính của ký sinh trùng sốt rét Plasmodium falciparum."
))

cards.append(make_card(
    "HS07-B7-04",
    "Điện di Hemoglobin phân biệt HbA, HbS và HbC ở pH 8.6",
    "ĐIỆN DI HUYẾT SẮC TỐ",
    "So sánh tốc độ di chuyển trên điện di ở pH 8.6 của HbA, HbS và HbC dựa trên điện tích phân tử?",
    [
        "<b>Nguyên lý điện di đệm kiềm pH = 8,6 —</b> Các phân tử hemoglobin tích điện âm và cùng di chuyển về phía cực dương Anot (+).",
        "<b>Hemoglobin A (HbA) —</b> Mang 2 gốc Glutamat tích điện âm (-1 mỗi chuỗi β); tích điện âm mạnh nhất trong 3 loại nên DI CHUYỂN NHANH NHẤT VỀ PHÍA ANOT (+).",
        "<b>Hemoglobin S (HbS) —</b> Đột biến Glu (-1) → Val (0); tetramer mất 2 điện tích âm so với HbA nên tích điện âm ít hơn, DI CHUYỂN CHẬM HƠN HBA về phía Anot.",
        "<b>Hemoglobin C (HbC) —</b> Đột biến Glu (-1) → Lys (+1); tetramer mất tới 4 điện tích âm so với HbA, tích điện âm yếu nhất nên DI CHUYỂN CHẬM NHẤT trong số các biến thể (Thứ tự tốc độ chạy điện di: HbA > HbS > HbC; mẹo nhớ: A Fat Santa Claus)."
    ],
    "Trên kết quả điện di hemoglobin ở pH kiềm, dải HbA nằm xa nhất về phía Anot, dải HbS nằm ở vị trí trung gian, và dải HbC nằm gần vạch xuất phát Catot nhất."
))

cards.append(make_card(
    "HS07-B7-05",
    "Biến thể Hemoglobin C (HbC) và Hemoglobin E (HbE)",
    "BIẾN THỂ HEMOGLOBIN",
    "Nêu bản chất đột biến và đặc điểm bệnh học lâm sàng của Hemoglobin C (HbC) và Hemoglobin E (HbE)?",
    [
        "<b>Hemoglobin C (HbC): Đột biến β6 Glu → Lys —</b> Thay thế Glutamat bằng Lysin tích điện dương tại codon số 6 chuỗi β; không tạo sợi polymer hình liềm nhưng kết tinh tạo các tinh thể lục giác trong hồng cầu, gây thiếu máu tan máu nhẹ và xuất hiện nhiều tế bào hồng cầu hình bia (target cells).",
        "<b>Hemoglobin E (HbE): Đột biến β26 Glu → Lys —</b> Thay thế Glutamat bằng Lysin tại codon số 26 chuỗi β.",
        "<b>Kích hoạt vị trí cắt nối giả (Cryptic Splice Site) —</b> Đột biến HbE tạo ra một vị trí cắt nối giả trên tiền mARN, làm giảm số lượng mARN chức năng của chuỗi β, biểu hiện kiểu hình tương tự thể nhẹ của β-Thalassemia.",
        "<b>Dịch tễ học HbE tại Đông Nam Á —</b> HbE cực kỳ phổ biến tại Việt Nam và Đông Nam Á (tỷ lệ mang gen ở một số dân tộc lên tới 30 - 50%); khi kết hợp với gen β-Thalassemia tạo thể dị hợp tử kép β-Thal/HbE có bệnh cảnh thiếu máu tan máu rất nặng tương đương Cooley."
    ],
    "Biến thể HbC phổ biến ở người gốc Tây Phi, trong khi HbE là biến thể hemoglobin phổ biến nhất tại vùng Đông Nam Á. Cả hai biến thể đều tạo nhiều tế bào hình bia trên lam máu ngoại vi."
))

cards.append(make_card(
    "HS07-B7-06",
    "Hội chứng α-Thalassemia và 4 mức độ mất gen",
    "HỘI CHỨNG THALASSEMIA",
    "Phân loại 4 mức độ lâm sàng của Hội chứng α-Thalassemia tương ứng với số lượng gen α bị mất trên NST số 16?",
    [
        "<b>Cụm gen α trên NST 16 —</b> Bình thường mỗi người có 4 gen α (hai gen trên mỗi nhiễm sắc thể: αα/αα); cơ chế đột biến chủ yếu là do ĐOẠN MẤT GEN (deletion).",
        "<b>1. Mất 1 gen (-α/αα) —</b> Thể ẩn mang gen (Silent carrier), hoàn toàn không có triệu chứng lâm sàng, công thức máu bình thường.",
        "<b>2. Mất 2 gen (-α/-α hoặc --/αα) —</b> Thể nhẹ (α-Thal trait), thiếu máu hồng cầu nhỏ nhược sắc nhẹ, không phụ thuộc truyền máu; kiểu gen cis (--/αα) phổ biến ở người Châu Á có nguy cơ sinh con bị phù thai.",
        "<b>3. Mất 3 gen (--/-α) — Bệnh HbH —</b> Thiếu hụt nghiêm trọng chuỗi α, chuỗi β dư thừa tự kết hợp tạo tetramer 4 chuỗi β (HbH = β4); HbH có ái lực oxy cực cao không nhả cho mô và dễ kết tủa gây tan máu mạn vừa đến nặng, lách to.",
        "<b>4. Mất cả 4 gen (--/--) — Bệnh Hb Bart's (Phù thai - Hydrops Fetalis) —</b> Không tạo được chuỗi α; chuỗi γ thời phôi thai tự kết hợp tạo tetramer 4 chuỗi γ (Hb Bart = γ4) giữ chặt oxy hoàn toàn không nhả cho thai nhi, gây suy tim ứ nước toàn thân và tử vong chu sinh."
    ],
    "Tetramer β4 (HbH) và tetramer γ4 (Hb Bart's) hoàn toàn không có tính hợp tác dị lập thể và có ái lực oxy cao gấp nhiều lần bình thường, do đó chúng hoàn toàn vô dụng trong chức năng vận chuyển oxy sinh lý."
))

cards.append(make_card(
    "HS07-B7-07",
    "Hội chứng β-Thalassemia thể nhẹ vs. thể nặng (Bệnh Cooley)",
    "HỘI CHỨNG THALASSEMIA",
    "Phân biệt cơ chế sinh học phân tử và biểu hiện lâm sàng giữa β-Thalassemia thể nhẹ và β-Thalassemia thể nặng (Bệnh Cooley)?",
    [
        "<b>Cụm gen β trên NST 11 —</b> Bình thường có 2 gen β (β/β); đột biến chủ yếu là ĐỘT BIẾN ĐIỂM ảnh hưởng phiên mã, cắt nối hoặc dịch mã (ký hiệu β⁺: giảm tổng hợp; β⁰: mất hoàn toàn tổng hợp chuỗi β).",
        "<b>β-Thalassemia thể nhẹ (Minor / Trait — β/β⁺ hoặc β/β⁰) —</b> Thiếu máu hồng cầu nhỏ nhược sắc nhẹ; điện di thấy tỷ lệ HbA2 (α2δ2) tăng cao đặc trưng > 3,5% do chuỗi α dư thừa kết hợp bù với chuỗi δ.",
        "<b>β-Thalassemia thể nặng (Major / Bệnh Cooley — β⁰/β⁰) —</b> Mất hoàn toàn chuỗi β; các chuỗi α tự do dư thừa không có đối tác kết tủa tạo các thể vùi không tan phá hủy tiền thân hồng cầu ngay trong tủy xương (tạo hồng cầu không hiệu lực cực nặng).",
        "<b>Biểu hiện lâm sàng Bệnh Cooley —</b> Thiếu máu nặng từ 6 tháng tuổi, biến dạng xương sọ mặt (trán dồ, mũi tẹt, gò má cao - bộ mặt Thalassemia), lách to khổng lồ, ứ sắt toàn thân hủy hoại tim, gan, nội tiết do truyền máu định kỳ."
    ],
    "Trong bệnh Cooley, điện di hemoglobin hoàn toàn không thấy dải HbA, dải HbF tăng vọt chiếm tới 90 - 95% tổng lượng hemoglobin của bệnh nhân."
))

cards.append(make_card(
    "HS07-B7-08",
    "Bản chất phân tử của Methemoglobinemia (Ngộ độc Methemoglobin)",
    "NGỘ ĐỘC METHEMOGLOBIN",
    "Phân tích bản chất hóa học của Methemoglobin và giải thích hậu quả chức năng kép làm giảm cung cấp oxy cho mô?",
    [
        "<b>Oxy hóa Fe²⁺ thành Fe³⁺ —</b> Bình thường ion sắt trong Hem ở dạng Ferrous (Fe²⁺); khi bị chất oxy hóa tác động, Fe²⁺ mất một electron chuyển thành dạng Ferric (Fe³⁺), tạo thành Methemoglobin (MetHb).",
        "<b>Hậu quả 1: Mất khả năng gắn Oxy —</b> Tiểu đơn vị chứa ion Fe³⁺ đã mất electron nên HOÀN TOÀN MẤT KHẢ NĂNG GẮN KẾT VỚI O2.",
        "<b>Hậu quả 2: Kéo lệch sâu đường cong sang Trái —</b> Sự hiện diện của Fe³⁺ gây biến đổi dị lập thể ép các tiểu đơn vị Fe²⁺ còn lại trong cùng tetramer chuyển sang trạng thái R, làm tăng vọt ái lực gắn oxy của chúng.",
        "<b>Hậu quả lâm sàng —</b> Các vị trí Fe²⁺ giữ chặt lấy O2 và kiên quyết không chịu nhả oxy cho mô; bệnh nhân rơi vào tình trạng THIẾU OXY MÔ CỰC ĐỘ mặc dù phân áp oxy hòa tan PaO2 trong máu động mạch vẫn hoàn toàn bình thường."
    ],
    "Nghịch lý lâm sàng của Methemoglobinemia: Khí máu động mạch cho kết quả PaO2 bình thường và SpO2 đo bằng máy đo bão hòa oxy qua da thường kẹp giả tạo ở mức khoảng 85%, nhưng bệnh nhân lại tím tái và toan lactic mô dữ dội."
))

cards.append(make_card(
    "HS07-B7-09",
    "Nguyên nhân và triệu chứng của Ngộ độc Methemoglobin",
    "NGỘ ĐỘC METHEMOGLOBIN",
    "Kể tên các thuốc/hóa chất gây ngộ độc Methemoglobin mắc phải và mô tả triệu chứng lâm sàng đặc trưng?",
    [
        "<b>Thuốc và hóa chất gây bệnh mắc phải —</b> Thuốc tê cục bộ (Benzocain trong xịt họng hạt, Lidocain), kháng sinh Dapsone, thuốc sốt rét Primaquin, hóa chất nhuộm Anilin, và Nitrat/Nitrit (nước giếng khoan ô nhiễm phân bón - hội chứng trẻ xanh lét Blue Baby Syndrome).",
        "<b>Nguyên nhân bẩm sinh —</b> Thiếu enzym Cytochrome b5 Reductase (NADH-Methemoglobin Reductase) di truyền hoặc mang biến thể Hemoglobin M (HbM: đột biến His F8/E7 thay bằng Tyrosin cố định Fe³⁺).",
        "<b>Dấu hiệu máu màu nâu sô-cô-la —</b> Máu rút từ tĩnh mạch có màu nâu sô-cô-la (chocolate-brown blood) đặc trưng, KHÔNG ĐỔI MÀU ĐỎ TƯƠI khi lắc tiếp xúc với oxy ngoài không khí.",
        "<b>Triệu chứng lâm sàng —</b> Tím tái sẫm màu da niêm mạc (cyanosis) không đáp ứng với thở oxy 100%; khi MetHb > 30% xuất hiện đau đầu, khó thở, lú lẫn; MetHb > 50% gây co giật, loạn nhịp tim và tử vong nếu > 70%."
    ],
    "Nghiệm pháp giấy thấm giường bệnh: Nhỏ một giọt máu bệnh nhân lên giấy thấm trắng bên cạnh giọt máu người bình thường; máu bình thường chuyển màu đỏ tươi khi tiếp xúc không khí, trong khi máu chứa Methemoglobin vẫn giữ nguyên màu nâu chocolate sẫm."
))

cards.append(make_card(
    "HS07-B7-10",
    "Phác đồ điều trị đặc hiệu ngộ độc Methemoglobin",
    "ĐIỀU TRỊ CẤP CỨU METHEMOGLOBIN",
    "Nêu thuốc giải độc đặc hiệu của ngộ độc Methemoglobin, cơ chế tác dụng và chống chỉ định sống còn cần lưu ý?",
    [
        "<b>Thuốc giải độc đặc hiệu —</b> Xanh Methylen (Methylene Blue), tiêm truyền tĩnh mạch liều 1 - 2 mg/kg trong 5 phút.",
        "<b>Cơ chế tác dụng phân tử —</b> Xanh methylen đóng vai trò chất nhận electron nhân tạo; được enzym NADPH-Methemoglobin Reductase khử thành Leukomethylene blue; Leukomethylene blue sau đó khử trực tiếp ion Fe³⁺ trở lại Fe²⁺ trong Hemoglobin.",
        "<b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI —</b> Chống chỉ định dùng Xanh Methylen ở bệnh nhân THIẾU MEN G6PD.",
        "<b>Nguy cơ khi dùng ở bệnh nhân thiếu G6PD —</b> Thiếu G6PD làm cạn kiệt NADPH, khiến Xanh Methylen không thể chuyển thành dạng khử mà tồn tại ở dạng oxy hóa, kích hoạt phản ứng tan máu cấp dữ dội làm trầm trọng thêm tình trạng thiếu oxy mô; trường hợp này phải dùng Vitamin C liều cao hoặc thay máu."
    ],
    "Vitamin C (Acid Ascorbic) liều cao đường uống hoặc tiêm tĩnh mạch có khả năng khử hóa học trực tiếp Fe³⁺ về Fe²⁺ không phụ thuộc NADPH, dùng làm liệu pháp hỗ trợ hoặc thay thế khi có chống chỉ định Xanh Methylen."
))

# ==============================================================================
# SECTION B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS07-ALGO-01",
    "Thuật toán 3 bước tính nhanh Điểm đẳng điện pI cho acid amin bất kỳ",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Trình bày lưu đồ thuật toán 3 bước tính nhanh chính xác Điểm đẳng điện (pI) cho bất kỳ acid amin nào?",
    [
        "<b>Bước 1 (Xác định tính chất chuỗi R) —</b> Kiểm tra chuỗi bên R thuộc nhóm nào: R không ion hóa (13 acid amin), R acid (Asp, Glu), hay R base (Lys, Arg, His).",
        "<b>Bước 2 (Chọn cặp pKa kẹp quanh Zwitterion trung hòa 0) —</b> Nếu R không ion hóa: chọn pK1 (-COOH) và pK2 (-NH3⁺); Nếu R acid (Asp, Glu): chọn 2 giá trị pKa acid thấp nhất là pK1 và pKR; Nếu R base (Lys, Arg, His): chọn 2 giá trị pKa kiềm cao nhất là pKR và pK2.",
        "<b>Bước 3 (Lấy trung bình cộng) —</b> Áp dụng công thức pI = (pKa_A + pKa_B) / 2.",
        "<b>Kiểm tra chéo điện tích ở pH sinh lý 7,4 —</b> Nếu pH 7,4 > pI → phân tử tích điện âm (Anion, chạy về Anot +); Nếu pH 7,4 < pI → phân tử tích điện dương (Cation, chạy về Catot -)."
    ],
    "Mẹo nhớ công thức: Nhóm acid chọn 2 pKa nhỏ nhất (pK1 + pKR)/2; nhóm base chọn 2 pKa lớn nhất (pKR + pK2)/2; nhóm trung tính lấy 2 đầu (pK1 + pK2)/2.",
    algo=True
))

cards.append(make_card(
    "HS07-ALGO-02",
    "Phân tầng chẩn đoán biến thể Hemoglobin qua Điện di huyết sắc tố ở pH 8.6",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước biện luận phân tầng kết quả Điện di Hemoglobin ở pH 8.6 kết hợp chỉ số hồng cầu?",
    [
        "<b>Bước 1 (Đánh giá dải di chuyển Anot +) —</b> Nhận diện vị trí dải băng chính: Tốc độ chạy giảm dần theo thứ tự HbA > HbS > HbC (Mẹo: A Fat Santa Claus).",
        "<b>Bước 2 (Kiểm tra tỷ lệ HbA2) —</b> Nếu dải HbA2 > 3,5% trên bệnh nhân thiếu máu hồng cầu nhỏ (MCV < 80 fL) → Khẳng định chẩn đoán thể nhẹ β-Thalassemia trait.",
        "<b>Bước 3 (Phân tích dải HbS và HbF) —</b> Nếu chỉ có dải HbS (80 - 90%) kèm HbF mà KHÔNG CÓ HbA → Bệnh Hồng cầu hình liềm đồng hợp tử (HbSS); Nếu có cả HbA (60%) và HbS (40%) → Thể dị hợp tử mang gen Sickle cell trait (HbAS).",
        "<b>Bước 4 (Phát hiện dải bất thường HbH và Hb Bart's) —</b> Dải HbH (β4) hoặc Hb Bart's (γ4) di chuyển cực nhanh vượt qua cả HbA về phía Anot → Chẩn đoán xác định bệnh α-Thalassemia (HbH disease hoặc Phù thai)."
    ],
    "Thuật toán điện di hemoglobin kết hợp công thức máu giúp phân biệt chính xác 100% giữa thiếu máu thiếu sắt (HbA2 bình thường/giảm, ferritin giảm) với mang gen Thalassemia (HbA2 tăng > 3,5%, ferritin bình thường).",
    algo=True
))

cards.append(make_card(
    "HS07-ALGO-03",
    "Tiếp cận cấp cứu và xử trí ngộ độc Methemoglobin cấp tính",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán cấp cứu 4 bước tiếp cận chẩn đoán và điều trị bệnh nhân ngộ độc Methemoglobin?",
    [
        "<b>Bước 1 (Nhận diện tam chứng gợi ý) —</b> Bệnh nhân tím tái đột ngột sau dùng thuốc tê/dapsone/nước giếng + SpO2 kẹp da tụt quanh 85% không tăng khi thở oxy 100% + Máu tĩnh mạch màu nâu chocolate sẫm.",
        "<b>Bước 2 (Đo Co-oximetry xác định tỷ lệ MetHb %) —</b> Làm khí máu động mạch có đo quang phổ Co-oximetry đo trực tiếp % MetHb (PaO2 hòa tan vẫn bình thường là dấu hiệu kinh điển).",
        "<b>Bước 3 (Chỉ định giải độc đặc hiệu) —</b> Khi MetHb > 20 - 30% hoặc bệnh nhân có triệu chứng thần kinh/tim mạch: Tiêm tĩnh mạch ngay XANH METHYLEN liều 1 - 2 mg/kg trong 5 phút.",
        "<b>Bước 4 (Sàng lọc cờ đỏ thiếu G6PD) —</b> Nếu bệnh nhân có tiền sử thiếu men G6PD: CHỐNG CHỈ ĐỊNH XANH METHYLEN; chuyển ngay sang dùng Vitamin C liều cao truyền tĩnh mạch (1 - 2 g mỗi 6 giờ) hoặc lọc máu / thay máu cấp cứu."
    ],
    "Cảnh báo lâm sàng: Đo SpO2 thông thường bằng 2 bước sóng (660 và 940 nm) không phân biệt được MetHb, máy sẽ đo sai lệch và dừng cố định ở mức khoảng 85%. Bắt buộc phải dùng máy đo khí máu Co-oximeter đa bước sóng để định lượng chính xác MetHb.",
    algo=True
))

cards.append(make_card(
    "HS07-ALGO-04",
    "Lưu đồ các yếu tố dịch chuyển đường cong Barcroft (Oxy-Hb)",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán ghi nhớ quy tắc 'CADET, face Right' dịch chuyển đường cong phân ly Oxy?",
    [
        "<b>Trục hoành pO2 và Trục tung % Bão hòa Oxy —</b> P50 bình thường = 26 - 27 mmHg ứng với 50% bão hòa.",
        "<b>Quy tắc CADET Lệch PHẢI (Tăng P50, Giảm ái lực, Tăng nhả Oxy cho mô) —</b> C (CO2 tăng), A (Acid / H⁺ tăng, pH giảm), D (DPG / 2,3-BPG tăng), E (Exercise - vận động gắng sức), T (Temperature - thân nhiệt tăng/sốt).",
        "<b>Lưu đồ Lệch TRÁI (Giảm P50, Tăng ái lực, Bắt giữ Oxy không chịu nhả) —</b> Giảm CO2 (kiềm hô hấp), Giảm H⁺ (kiềm chuyển hóa, pH tăng), Giảm 2,3-BPG (máu truyền lưu trữ), Hạ thân nhiệt, Hemoglobin thai nhi (HbF).",
        "<b>Cờ đỏ Ngộ độc CO và MetHb —</b> Lệch TRÁI nặng nề + ĐỈNH BỊ CẮT CỤT DẸT XUỐNG; vừa chiếm chỗ oxy vừa giữ chặt oxy ở các vị trí còn lại, chặn đứng dòng cấp oxy cho mô."
    ],
    "Khi gặp câu hỏi tình huống: Bệnh nhân sốt cao, toan lactic do vận động cơ bắp dữ dội → Nhận diện ngay đường cong dịch chuyển sang PHẢI, P50 tăng lên 35 mmHg, giúp tăng tỷ lệ nhả oxy cho cơ từ 25% lên tới 75%.",
    algo=True
))

cards.append(make_card(
    "HS07-ALGO-05",
    "Biện luận phân tầng kết quả Điện di Protein huyết thanh SPEP",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước biện luận phân tầng hình thái bệnh lý trên biểu đồ điện di protein huyết thanh SPEP?",
    [
        "<b>Bước 1 (Đánh giá đỉnh Albumin) —</b> Bình thường 55 - 65%; Nếu Albumin giảm sâu: kiểm tra ngay phân đoạn α2 và nước tiểu (Hội chứng thận hư nếu có protein niệu > 3,5 g; hoặc Xơ gan suy dinh dưỡng).",
        "<b>Bước 2 (Kiểm tra đỉnh α2-globulin) —</b> Nếu đỉnh Albumin sụt sâu kèm ĐỈNH α2-MACROGLOBULIN TĂNG VỌT NHỌN HOẮT → Chẩn đoán xác định Hội chứng thận hư.",
        "<b>Bước 3 (Kiểm tra vùng liên kết β-γ) —</b> Nếu mất khoảng trũng giữa đỉnh β và γ tạo thành một dải đồi liền mạch (Hiện tượng cầu nối Beta-Gamma Bridging do tăng IgA) → Chẩn đoán Xơ gan tiến triển.",
        "<b>Bước 4 (Kiểm tra vùng γ-globulin tìm đỉnh M) —</b> Nếu xuất hiện một đỉnh hẹp đáy, nhọn hoắt đứng thẳng (Đỉnh M / M-spike) → Chẩn đoán bệnh lý tăng sinh tương bào đơn dòng: Đa u tủy xương (Kahler), Bệnh Waldenström hoặc MGUS; chỉ định ngay điện di cố định miễn dịch (IFE) và tủy đồ."
    ],
    "Lưu đồ SPEP 4 bước giúp bác sĩ nội khoa rà soát nhanh chóng và chính xác 3 hội chứng bệnh lý lớn của nội khoa: Hội chứng thận hư (thận), Xơ gan (gan), và Đa u tủy xương (huyết học).",
    algo=True
))

# ==============================================================================
# XUẤT FILE CARDS V2 JSON VÀ KIỂM TRA
# ==============================================================================

out_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-07_Hoa_hoc_protein")
cards_file = out_dir / "HS-07_Hoa_hoc_protein.cards.v2.json"

output_data = {
    "cards": cards,
    "total": len(cards),
    "version": "v2"
}

with open(cards_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Đã tạo thành công {len(cards)} thẻ Master chuyên sâu cho HS-07 tại:")
print(f"-> {cards_file}")
