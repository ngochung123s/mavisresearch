# -*- coding: utf-8 -*-
"""build_deep_hs09.py - Generate 83 exhaustive master flashcards for HS-09 (Hem Biosynthesis, Hemoglobin Degradation & Jaundice)"""
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
        "tags": ["hoasinh", "HS09", section]
    }

cards = []

# ==============================================================================
# SECTION B1: CẤU TRÚC NHÓM NGOẠI HEM & 8 BƯỚC SINH TỔNG HỢP HEM (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B1-01",
    "Khái niệm nhóm ngoại Hem và các hemoprotein chức năng",
    "CẤU TRÚC NHÓM NGOẠI HEM",
    "Định nghĩa nhóm ngoại Hem và kể tên 5 nhóm hemoprotein quan trọng nhất trong cơ thể người?",
    [
        "<b>Định nghĩa nhóm ngoại Hem —</b> Là một phức hợp phối trí giữa vòng Protoporphyrin IX hữu cơ và cation sắt hóa trị II (Fe²⁺), đóng vai trò nhóm ngoại prosthetic gắn chặt với apo-protein.",
        "<b>Hemoglobin và Myoglobin —</b> Chuyên trách vận chuyển oxy trong hệ mạch máu và dự trữ oxy nội bào tại mô cơ vân, cơ tim.",
        "<b>Hệ enzym Cytochrom P450 (CYP450) tại gan —</b> Tham gia chuyển hóa thuốc, giải độc hóa chất ngoại sinh và sinh tổng hợp hormon steroid tại lưới nội sinh chất.",
        "<b>Cytochrom c và Cytochrom Oxidase —</b> Thành phần vận chuyển điện tử cốt lõi trong chuỗi hô hấp tế bào ty thể để sinh tổng hợp ATP.",
        "<b>Enzym chống oxy hóa Catalase và Peroxidase —</b> Chứa nhân Hem tại trung tâm hoạt động để phân hủy các gốc oxy hóa tự do độc hại H2O2 thành H2O và O2."
    ],
    "Mặc dù Hemoglobin chiếm tới trên 85% tổng lượng Hem của cơ thể, sự hiện diện của Hem trong Cytochrom P450 và chuỗi hô hấp tế bào là điều kiện tiên quyết cho sự sinh tồn của mọi tế bào nhân thực."
))

cards.append(make_card(
    "HS09-B1-02",
    "Cấu trúc phân tử Protoporphyrin IX và dải hấp thụ Soret",
    "CẤU TRÚC PROTOPORPHYRIN IX",
    "Mô tả cấu tạo hóa học của Protoporphyrin IX, trật tự 8 nhóm thế và đặc tính quang phổ dải Soret?",
    [
        "<b>Khung tetrapyrrol phẳng —</b> Cấu tạo từ 4 vòng dị vòng Pyrrol (I, II, III, IV) liên kết với nhau qua 4 cầu nối methenyl (-CH=) tạo nên một mặt phẳng cứng nhắc.",
        "<b>8 nhóm thế đối xứng đặc thù —</b> Gồm 4 gốc Methyl (-CH3, M), 2 gốc Vinyl (-CH=CH2, V), và 2 gốc Propionat (-CH2-CH2-COOH, P).",
        "<b>Trật tự sắp xếp M-V-M-V-M-P-P-M —</b> Vòng pyrrol thứ IV có sự đảo vị trí của nhóm Propionat, xác định đây là đồng phân tự nhiên duy nhất thuộc dãy isomer IX (hoặc isomer III) có hoạt tính sinh học.",
        "<b>Dải hấp thụ quang phổ Soret (400 - 410 nm) —</b> Hệ thống liên kết đôi liên hợp khép kín toàn diện giúp vòng porphyrin hấp thụ photon ánh sáng cực mạnh ở bước sóng 400 - 410 nm, tạo màu đỏ đặc trưng của máu."
    ],
    "Cấu trúc liên hợp vòng porphyrin hoạt động như một 'đám mây electron π bất định xứ', cho phép phân bố lại mật độ điện tích khi gắn oxy hoặc ion kim loại sắt."
))

cards.append(make_card(
    "HS09-B1-03",
    "Khối lượng và vị trí cơ quan sinh tổng hợp Hem",
    "SINH TỔNG HỢP HEM",
    "Nêu khối lượng Hem được sinh tổng hợp mỗi ngày và so sánh tỷ lệ tổng hợp giữa Tủy xương và Gan?",
    [
        "<b>Khối lượng tổng hợp hằng ngày —</b> Trong cơ thể người trưởng thành khỏe mạnh, mỗi ngày có khoảng 6 đến 7 g Hemoglobin (tương đương khoảng 300 mg hay ~500 µmol Hem) được tổng hợp mới.",
        "<b>Tủy xương tạo máu (Khoảng 85%) —</b> Diễn ra trong các tế bào tiền thân dòng hồng cầu (nguyên hồng cầu ái kiềm, nguyên hồng cầu đa sắc); tốc độ tổng hợp phối hợp nhịp nhàng với quá trình tổng hợp chuỗi globin.",
        "<b>Tế bào gan (Khoảng 15%) —</b> Tổng hợp phục vụ cho nhu cầu đổi mới liên tục của hệ enzym Cytochrom P450 và các cytochrom ty thể; tốc độ tổng hợp biến động nhanh theo nhu cầu chuyển hóa thuốc.",
        "<b>Các mô khác (< 1%) —</b> Tổng hợp lượng rất nhỏ phục vụ hô hấp tế bào và catalase nội bào."
    ],
    "Hồng cầu trưởng thành lưu hành trong máu ngoại vi hoàn toàn không thể tổng hợp được Hem vì chúng đã thoái hóa mất nhân và mất toàn bộ bào quan ty thể."
))

cards.append(make_card(
    "HS09-B1-04",
    "Vị trí nội bào hai ngăn của con đường Sinh tổng hợp Hem",
    "ĐỊNH VỊ NỘI BÀO SINH TỔNG HỢP HEM",
    "Mô tả sự luân chuyển không gian giữa Ty thể và Bào tương trong 8 bước sinh tổng hợp Hem?",
    [
        "<b>Bước 1 mở đầu trong CHẤT NỀN TY THỂ —</b> Ngưng tụ Succinyl-CoA và Glycin tạo Acid δ-aminolevulinic (ALA) nhờ enzym ALAS.",
        "<b>Bước 2 đến Bước 5 ngoài BÀO TƯƠNG TẾ BÀO —</b> Phân tử ALA ra ngoài bào tương: Bước 2 tạo PBG; Bước 3 tạo HMB mạch thẳng; Bước 4 đóng vòng tạo Uroporphyrinogen III; Bước 5 khử carboxyl tạo Coproporphyrinogen III.",
        "<b>Bước 6 đến Bước 8 quay trở lại CHẤT NỀN TY THỂ —</b> Coproporphyrinogen III tái nhập ty thể: Bước 6 tạo Protoporphyrinogen IX; Bước 7 oxy hóa tạo Protoporphyrin IX; Bước 8 gắn Fe²⁺ tạo Hem hoàn chỉnh.",
        "<b>Ý nghĩa sinh học —</b> Tận dụng cơ chất Succinyl-CoA của chu trình Krebs trong ty thể và phối hợp với nguồn sắt Fe²⁺ trong ty thể để lắp ráp Hem."
    ],
    "Sự phân chia 2 ngăn nội bào đòi hỏi các protein vận chuyển màng ty thể chuyên biệt để xuất ALA ra ngoài và nhập Coproporphyrinogen III vào trong."
))

cards.append(make_card(
    "HS09-B1-05",
    "Bước 1: Tổng hợp Acid δ-Aminolevulinic (ALA) trong ty thể",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Trình bày phương trình phản ứng, cơ chất, coenzym và vai trò kiểm soát của enzym ALA Synthase (ALAS)?",
    [
        "<b>Vị trí phản ứng —</b> Chất nền ty thể tế bào tủy xương và tế bào gan.",
        "<b>Cơ chất ban đầu —</b> Glycin (acid amin đơn giản nhất) và Succinyl-CoA (sản phẩm trung gian giàu năng lượng của chu trình Krebs).",
        "<b>Enzym và Coenzym —</b> Enzym δ-AMINOLEVULINIC ACID SYNTHASE (ALAS), bắt buộc cần coenzym PYRIDOXAL PHOSPHAT (PLP / Vitamin B6).",
        "<b>Phương trình phản ứng —</b> Succinyl-CoA + Glycin → δ-Aminolevulinic acid (ALA) + CoA-SH + CO2.",
        "<b>Bước giới hạn tốc độ (Rate-Limiting Step) —</b> ALAS là enzym then chốt kiểm soát tốc độ của toàn bộ con đường sinh tổng hợp Hem trong cơ thể."
    ],
    "Glycin gắn vào coenzym PLP tạo Base Schiff aldimin, hoạt hóa carbon α để tấn công liên kết thioester của Succinyl-CoA; phản ứng khử carboxyl giải phóng CO2 kéo phản ứng diễn ra một chiều không thuận nghịch."
))

cards.append(make_card(
    "HS09-B1-06",
    "Cơ chế điều hòa của ALAS-1 tại Gan và cảm ứng bởi thuốc CYP450",
    "ĐIỀU HÒA ALAS TẠI GAN",
    "Phân tích cơ chế ức chế ngược bởi Hem (Hemin) lên ALAS-1 tại gan và giải thích vì sao thuốc cảm ứng CYP450 kích hoạt cơn Porphyria?",
    [
        "<b>Đặc điểm ALAS-1 tại gan —</b> Mã hóa bởi gen trên nhiễm sắc thể thường số 3; cung cấp Hem cho cytochrom P450.",
        "<b>Ức chế ngược bởi Hemin (Fe³⁺) ở 3 cấp độ —</b> Khi nồng độ Hem tự do cao: 1) Ức chế dị lập thể trực tiếp hoạt tính ALAS-1; 2) Ức chế phiên mã và làm mất tính bền vững của mRNA ALAS-1; 3) Ngăn chặn protein tiền chất ALAS-1 nhập vào ty thể.",
        "<b>Cơ chế cảm ứng bởi thuốc chuyển hóa qua gan —</b> Khi dùng thuốc chuyển hóa qua CYP450 (Barbiturat, Phenytoin, Rifampicin, rượu), gan tăng cường tiêu thụ Hem để tạo CYP450.",
        "<b>Bùng phát cơn Porphyria cấp —</b> Nồng độ Hem tự do sụt giảm làm mất sự ức chế ngược, ALAS-1 được tổng hợp tăng vọt gấp nhiều lần, đẩy mạnh sản xuất các tiền chất porphyrin độc hại kích hoạt cơn đau Porphyria cấp tính."
    ],
    "Đây là lý do sống còn trên lâm sàng: bệnh nhân mang gen Porphyria cấp từng cơn (AIP) bị chống chỉ định tuyệt đối với các thuốc an thần nhóm Barbiturat hoặc thuốc cảm ứng men gan."
))

cards.append(make_card(
    "HS09-B1-07",
    "Cơ chế điều hòa của ALAS-2 tại Tủy xương theo nồng độ Sắt",
    "ĐIỀU HÒA ALAS TỦY XƯƠNG",
    "Phân tích cơ chế điều hòa dịch mã của ALAS-2 theo nồng độ Sắt nội bào và bệnh lý Thiếu máu nguyên bào sắt liên kết NST X?",
    [
        "<b>Đặc điểm ALAS-2 dòng hồng cầu —</b> Mã hóa bởi gen trên NHIỄM SẮC THỂ GIỚI TÍNH X (Xp11.21); chiếm 85% tổng lượng Hem cơ thể; HOÀN TOÀN KHÔNG BỊ ỨC CHẾ NGƯỢC BỞI HEM.",
        "<b>Kiểm soát dịch mã qua yếu tố IRE ở đầu 5'-UTR —</b> Trên mRNA của ALAS-2 có trình tự cấu trúc kẹp tóc gọi là Yếu tố đáp ứng với sắt (Iron-Responsive Element - IRE).",
        "<b>Khi nồng độ Sắt thấp —</b> Protein IRP bám chặt vào IRE ở đầu 5', ngăn chặn ribosome tiếp cận dịch mã, tạm dừng tổng hợp ALAS-2 để tránh lãng phí porphyrin khi thiếu sắt.",
        "<b>Khi nồng độ Sắt dồi dào —</b> Fe²⁺ gắn vào IRP làm nó tách rời khỏi IRE, giải phóng mRNA để dịch mã ồ ạt ALAS-2 phục vụ tạo hemoglobin.",
        "<b>Thiếu máu nguyên bào sắt liên kết X (XLSA) —</b> Đột biến mất chức năng gen ALAS-2 gây ứ đọng sắt trong ty thể tạo nguyên hồng cầu sắt dạng vòng (Ringed Sideroblasts); điều trị đáp ứng một phần với Vitamin B6 liều cao."
    ],
    "Sự tách biệt điều hòa giữa ALAS-1 (điều hòa theo nhu cầu giải độc gan qua feedback của Hem) và ALAS-2 (điều hòa theo nguồn cung cấp sắt ở tủy xương) là một thiết kế tiến hóa hoàn hảo."
))

cards.append(make_card(
    "HS09-B1-08",
    "Bước 2: Ngưng tụ tạo Porphobilinogen (PBG) bởi ALA Dehydratase",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Trình bày phản ứng tạo Porphobilinogen ngoài bào tương và giải thích vì sao enzym này cực kỳ nhạy cảm với Chì?",
    [
        "<b>Enzym xúc tác —</b> δ-AMINOLEVULINIC ACID DEHYDRATASE (ALA Dehydratase hay PBG Synthase), định vị tại bào tương tế bào.",
        "<b>Cofactor bắt buộc —</b> Chứa cation Kẽm (Zn²⁺) và các gốc sulfhydryl (-SH) hoạt động tại trung tâm xúc tác.",
        "<b>Phương trình phản ứng —</b> 2 phân tử δ-Aminolevulinic acid (ALA) ngưng tụ tách loại 2 phân tử H2O tạo thành 1 phân tử PORPHOBILINOGEN (PBG).",
        "<b>Cấu trúc PBG —</b> Mang một vòng pyrrol đơn độc gắn 1 gốc Acetat (-CH2-COOH) và 1 gốc Propionat (-CH2-CH2-COOH).",
        "<b>Điểm tấn công của Chì (Pb²⁺) —</b> Ion chì đẩy văng ion Zn²⁺ và liên kết bất thuận nghịch vào các nhóm -SH, làm tê liệt hoàn toàn ALA Dehydratase, dẫn đến ứ đọng ALA nồng độ cao trong máu."
    ],
    "Sự ứ đọng ALA trong ngộ độc chì gây ra các cơn đau bụng quặn thắt và triệu chứng thần kinh do ALA có cấu trúc không gian tương tự chất dẫn truyền thần kinh GABA."
))

cards.append(make_card(
    "HS09-B1-09",
    "Bước 3: Ngưng tụ 4 PBG tạo Hydroxymethylbilane (HMB) bởi PBG Deaminase",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Trình bày phản ứng tạo chuỗi tetrapyrrol mạch thẳng HMB và bệnh lý di truyền kinh điển liên quan?",
    [
        "<b>Enzym xúc tác —</b> PORPHOBILINOGEN DEAMINASE (PBG Deaminase hay HMB Synthase, trước đây gọi là Uroporphyrinogen I Synthase), định vị trong bào tương.",
        "<b>Cơ chế ngưng tụ nối tiếp —</b> Nối đầu - đuôi tuần tự 4 phân tử PBG với nhau, giải phóng 4 cation Amoni (NH4⁺).",
        "<b>Sản phẩm tạo thành —</b> HYDROXYMETHYLBILANE (HMB), là một chuỗi tetrapyrrol mạch thẳng chưa đóng vòng.",
        "<b>Bệnh học di truyền liên quan —</b> Khiếm khuyết di truyền enzym PBG Deaminase dẫn đến bệnh PORPHYRIA CẤP TỪNG CƠN (Acute Intermittent Porphyria - AIP), gây ứ đọng ALA và PBG."
    ],
    "Enzym PBG Deaminase sử dụng một cofactor đặc biệt gắn đồng hóa trị là dipyrromethane để neo và lắp ráp lần lượt từng phân tử PBG."
))

cards.append(make_card(
    "HS09-B1-10",
    "Bước 4: Đóng vòng tạo Uroporphyrinogen III bởi Uroporphyrinogen III Synthase",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Mô tả phản ứng đóng vòng tạo Uroporphyrinogen III và giải thích hậu quả khi thiếu hụt enzym này?",
    [
        "<b>Enzym xúc tác —</b> UROPORPHYRINOGEN III SYNTHASE, định vị trong bào tương tế bào.",
        "<b>Phản ứng đảo ngược cấu hình vòng IV —</b> Enzym thực hiện một thao tác không gian tinh vi: đảo ngược 180° cấu hình của vòng pyrrol thứ tư trước khi đóng vòng khép kín chuỗi HMB.",
        "<b>Tạo đồng phân Isomer III bất đối xứng —</b> Sản phẩm là UROPORPHYRINOGEN III với trật tự các chuỗi bên Acetat (A) và Propionat (P) là: A-P, A-P, A-P, P-A.",
        "<b>Hậu quả khi thiếu enzym (Bệnh Gunther) —</b> HMB tự đóng vòng phi enzym tạo Uroporphyrinogen I (dãy isomer đối xứng hoàn toàn A-P, A-P, A-P, A-P); isomer I là con đường cụt không tạo được Hem chức năng, gây bệnh Porphyria bẩm sinh tạo hồng cầu (Bệnh Gunther) với biến dạng da khủng khiếp."
    ],
    "Chỉ có các dẫn xuất thuộc dãy đồng phân isomer III mới có thể tiếp tục đi vào các bước chuyển hóa hạ lưu để tạo ra Hem có hoạt tính sinh học."
))

cards.append(make_card(
    "HS09-B1-11",
    "Bước 5: Khử carboxyl tạo Coproporphyrinogen III bởi UROD",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Trình bày phản ứng khử carboxyl tạo Coproporphyrinogen III và bệnh lý Porphyria phổ biến nhất?",
    [
        "<b>Enzym xúc tác —</b> UROPORPHYRINOGEN DECARBOXYLASE (UROD), định vị trong bào tương tế bào.",
        "<b>Cơ chế khử 4 nhóm carboxyl —</b> Cắt bỏ tuần tự 4 nhóm -COOH từ 4 chuỗi bên Acetat (-CH2-COOH → -CH3 + CO2), biến đổi 4 gốc Acetat thành 4 gốc METHYL (M).",
        "<b>Sản phẩm tạo thành —</b> COPROPORPHYRINOGEN III mang 4 gốc Methyl và 4 gốc Propionat (trật tự chuỗi bên: M-P, M-P, M-P, P-M).",
        "<b>Bệnh học liên quan —</b> Suy giảm hoạt tính enzym UROD là nguyên nhân gây bệnh PORPHYRIA DA CHẬM (Porphyria Cutanea Tarda - PCT), thể Porphyria phổ biến nhất trong thực hành lâm sàng."
    ],
    "Sau phản ứng của UROD, phân tử Coproporphyrinogen III được vận chuyển tái nhập trở lại vào trong ty thể để tiếp tục 3 bước oxy hóa cuối cùng."
))

cards.append(make_card(
    "HS09-B1-12",
    "Ba bước cuối cùng trong Ty thể hoàn tất phân tử Hem",
    "TÁM BƯỚC SINH TỔNG HỢP HEM",
    "Mô tả 3 phản ứng cuối cùng (Bước 6, 7, 8) diễn ra trong ty thể để hoàn tất phân tử Hem?",
    [
        "<b>Bước 6: Tạo Protoporphyrinogen IX (CPOX) —</b> Enzym Coproporphyrinogen Oxidase tại màng trong ty thể khử carboxyl oxy hóa 2 gốc Propionat thành 2 gốc VINYL (-CH=CH2), tạo Protoporphyrinogen IX (M-V, M-V, M-P, P-M).",
        "<b>Bước 7: Tạo Protoporphyrin IX (PPOX) —</b> Enzym Protoporphyrinogen Oxidase tách 6 nguyên tử hydro chuyển cho oxy, làm xuất hiện hệ thống liên kết đôi liên hợp khép kín, biến chất không màu thành PROTOPORPHYRIN IX phẳng có màu đỏ sẫm hấp thụ ánh sáng huỳnh quang.",
        "<b>Bước 8: Lắp ráp Fe²⁺ tạo Hem (Ferrochelatase) —</b> Enzym FERROCHELATASE (Heme Synthase) đưa cation sắt Fe²⁺ vào tâm vòng porphyrin, gắn phối trí với 4 nguyên tử nitơ pyrrol để hoàn tất phân tử HEM.",
        "<b>Điểm tấn công của Chì —</b> Enzym Ferrochelatase chứa các nhóm -SH hoạt động và cũng bị ion Chì (Pb²⁺) ức chế mạnh mẽ tương tự ALA dehydratase."
    ],
    "Sau khi được tổng hợp hoàn chỉnh tại màng trong ty thể, phân tử Hem được xuất bào ra ngoài bào tương để gắn phối hợp với các chuỗi polypeptid Globin tạo thành Hemoglobin hoàn chỉnh."
))

# ==============================================================================
# SECTION B2: NGỘ ĐỘC CHÌ & RỐI LOẠN PORPHYRIA (AIP vs PCT) (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B2-01",
    "Cơ chế phân tử của Ngộ độc Chì (Lead Poisoning) trên tổng hợp Hem",
    "NGỘ ĐỘC CHÌ LÂM SÀNG",
    "Phân tích cơ chế phân tử giải thích vì sao ion Chì (Pb2+) làm tê liệt quá trình sinh tổng hợp Hem?",
    [
        "<b>Độc chất môi trường và công nghiệp —</b> Chì xâm nhập qua đường hô hấp hoặc tiêu hóa (sơn cũ, ắc quy, nguồn nước nhiễm chì, đạn chì).",
        "<b>Gắn bất thuận nghịch vào nhóm -SH —</b> Ion Pb²⁺ có ái lực cực cao với các nhóm sulfhydryl (-SH) tự do, làm biến tính protein và bất hoạt enzym không hồi phục.",
        "<b>Ức chế enzym Bước 2: δ-ALA Dehydratase —</b> Chì cạnh tranh và đẩy văng cation cofactor Kẽm (Zn²⁺) đồng thời khóa nhóm -SH, gây ứ đọng nồng độ rất cao của Acid δ-aminolevulinic (ALA) trong máu và nước tiểu.",
        "<b>Ức chế enzym Bước 8: Ferrochelatase —</b> Chì ức chế bước đưa Fe²⁺ vào Protoporphyrin IX, làm sắt bị ứ đọng thừa thãi trong ty thể và Protoporphyrin không được gắn sắt."
    ],
    "Sự ức chế đồng thời cả bước 2 và bước 8 tạo ra bức tranh sinh hóa đặc trưng của ngộ độc chì: tăng vọt ALA niệu kết hợp tăng Protoporphyrin tự do trong hồng cầu."
))

cards.append(make_card(
    "HS09-B2-02",
    "Hậu quả tích tụ ALA và Kẽm-Protoporphyrin (ZPP) trong ngộ độc Chì",
    "NGỘ ĐỘC CHÌ LÂM SÀNG",
    "Giải thích cơ chế gây đau bụng, tổn thương thần kinh và xét nghiệm sàng lọc Kẽm-Protoporphyrin (ZPP) trong ngộ độc Chì?",
    [
        "<b>ALA tương đồng cấu trúc với GABA —</b> Phân tử Acid δ-aminolevulinic (ALA) có cấu trúc không gian rất giống chất dẫn truyền thần kinh GABA; ALA tích tụ kích hoạt thụ thể GABA ở hệ thần kinh và cơ trơn.",
        "<b>Cơn đau quặn bụng do chì (Lead Colic) —</b> Co thắt dữ dội cơ trơn mạch máu và ruột gây đau bụng quặn cơn dữ dội kèm táo bón nặng.",
        "<b>Tạo Kẽm-Protoporphyrin (ZPP / FEP) —</b> Do Ferrochelatase bị ức chế không thể gắn Fe²⁺, ion Kẽm (Zn²⁺) sẽ nhảy vào thế chỗ gắn với Protoporphyrin IX tạo KẼM-PROTOPORPHYRIN (ZPP).",
        "<b>Xét nghiệm sàng lọc giá trị cao —</b> Định lượng ZPP trong hồng cầu bằng máy đo huỳnh quang là xét nghiệm sàng lọc ngộ độc chì nghề nghiệp nhạy và tin cậy."
    ],
    "Thiếu hụt Hem do ngộ độc chì dẫn đến thiếu máu hồng cầu nhỏ nhược sắc kèm theo phản ứng bù trừ làm tăng bài tiết erythropoietin nhưng không hiệu quả do thiếu nguyên liệu tạo Hem."
))

cards.append(make_card(
    "HS09-B2-03",
    "Các dấu hiệu lâm sàng và huyết học kinh điển của Ngộ độc Chì",
    "NGỘ ĐỘC CHÌ LÂM SÀNG",
    "Kể tên các dấu hiệu lâm sàng và cận lâm sàng kinh điển giúp nhận diện bệnh nhân ngộ độc Chì?",
    [
        "<b>Nguyên hồng cầu sắt dạng vòng (Ringed Sideroblasts) —</b> Sắt Fe²⁺ không gắn được vào Hem bị ứ đọng lắng đọng bao quanh nhân tế bào tiền thân dòng hồng cầu trong tủy xương, phát hiện trên nhuộm xanh Perls (Prussian blue).",
        "<b>Hạt kiềm trong hồng cầu (Basophilic Stippling) —</b> Chì ức chế enzym Pyrimidine 5'-Nucleotidase làm ứ đọng các mảnh ARN ribosome thoái hóa tạo các chấm hạt bắt màu kiềm rải rác trong hồng cầu trên lam máu ngoại vi.",
        "<b>Đường viền nướu Burton (Burton's Line) —</b> Đường viền màu xanh đen hoặc xám chì chạy dọc bờ lợi chân răng, do chì phản ứng với H2S sinh ra từ vi khuẩn mảng bám răng tạo kết tủa chì sulfua (PbS).",
        "<b>Liệt thần kinh quay gây Bàn tay rủ (Wrist Drop) —</b> Tổn thương thoái hóa myelin thần kinh vận động ngoại biên gây yếu cơ duỗi cổ tay và ngón tay; ở trẻ em gây bệnh não chì (phù não, co giật, chậm phát triển trí tuệ vĩnh viễn)."
    ],
    "Mẹo nhớ kinh điển các triệu chứng ngộ độc chì: 'LEAD' = L (Lead lines on gingiva/bones), E (Encephalopathy & Erythrocyte basophilic stippling), A (Abdominal colic & Anemia), D (Drops of wrist and foot; Dimercaprol/EDTA treatment)."
))

cards.append(make_card(
    "HS09-B2-04",
    "Khái niệm phân loại nhóm bệnh Rối loạn chuyển hóa Porphyrin (Porphyria)",
    "RỐI LOẠN CHUYỂN HÓA PORPHYRIN",
    "Định nghĩa Porphyria và phân biệt hai nhóm hội chứng lâm sàng: Thể thần kinh cấp tính vs. Thể nhạy cảm ánh sáng da?",
    [
        "<b>Định nghĩa Porphyria —</b> Là nhóm bệnh lý di truyền (hoặc mắc phải) do khiếm khuyết hoạt tính của một trong các enzym trên con đường sinh tổng hợp Hem, dẫn đến sự tích tụ và bài xuất bất thường các tiền chất porphyrin.",
        "<b>1. Thể Thần kinh cấp tính (Neuropsychiatric Porphyrias) —</b> Tắc nghẽn ở các bước đầu (trước khi đóng vòng hoàn chỉnh); tích tụ các tiền chất phân tử nhỏ như ALA và PBG; biểu hiện đau bụng cấp, liệt thần kinh, loạn thần; HOÀN TOÀN KHÔNG CÓ TỔN THƯƠNG DA (Điển hình: Porphyria cấp từng cơn - AIP).",
        "<b>2. Thể Nhạy cảm ánh sáng da (Cutaneous / Photosensitive Porphyrias) —</b> Tắc nghẽn ở các bước sau; tích tụ các phân tử Porphyrinogen và Porphyrin có vòng khép kín; các vòng này lắng đọng ở da hấp thụ ánh sáng sinh gốc tự do gây bọng nước, trợt loét hoại tử da (Điển hình: Porphyria da chậm - PCT).",
        "<b>Thể hỗn hợp —</b> Một số thể tắc nghẽn ở bước 6 hoặc 7 (Hereditary Coproporphyria, Porphyria Variegata) biểu hiện phối hợp cả triệu chứng thần kinh và tổn thương da."
    ],
    "Quy tắc vàng chẩn đoán: Porphyria gây tích tụ tiền chất chưa đóng vòng (ALA, PBG) thì không nhạy cảm ánh sáng; Porphyria gây tích tụ các hợp chất đã có vòng porphyrin hoàn chỉnh thì luôn đi kèm nhạy cảm ánh sáng da dữ dội."
))

cards.append(make_card(
    "HS09-B2-05",
    "Porphyria cấp từng cơn (AIP): Đột biến gen PBG Deaminase",
    "PORPHYRIA CẤP TỪNG CƠN (AIP)",
    "Nêu bản chất di truyền, enzym khiếm khuyết và các chất chuyển hóa ứ đọng trong Porphyria cấp từng cơn (AIP)?",
    [
        "<b>Di truyền trội trên NST thường —</b> Đột biến dị hợp tử trên gen HMBS nằm trên nhiễm sắc thể thường số 11; độ xâm nhập lâm sàng thấp (chỉ khoảng 10 - 20% người mang gen biểu hiện cơn bệnh).",
        "<b>Enzym khiếm khuyết —</b> PORPHOBILINOGEN DEAMINASE (PBG Deaminase hay HMB Synthase) ở Bước 3 của con đường sinh tổng hợp Hem tại gan.",
        "<b>Các chất ứ đọng bệnh lý —</b> Sự tắc nghẽn làm ứ đọng nồng độ rất cao của PORPHOBILINOGEN (PBG) và chất thượng nguồn là ACID δ-AMINOLEVULINIC (ALA) trong máu và bài xuất ồ ạt qua nước tiểu.",
        "<b>HOÀN TOÀN KHÔNG CÓ TRIỆU CHỨNG DA —</b> Do HMB không được tạo thành, không có sự tích tụ của các vòng porphyrin đóng kín nên bệnh nhân AIP tuyệt đối không bao giờ bị bọng nước hay nhạy cảm ánh sáng mặt trời."
    ],
    "Tên gọi 'từng cơn' (intermittent) phản ánh đặc điểm lâm sàng: bệnh nhân hoàn toàn bình thường giữa các đợt bùng phát; cơn cấp chỉ xuất hiện khi có yếu tố kích thích làm cạn kiệt Hem và cảm ứng ALAS-1."
))

cards.append(make_card(
    "HS09-B2-06",
    "Biểu hiện lâm sàng và Nước tiểu đổi màu trong bệnh AIP",
    "PORPHYRIA CẤP TỪNG CƠN (AIP)",
    "Mô tả tam chứng lâm sàng cốt lõi và hiện tượng đổi màu nước tiểu đặc trưng trong cơn Porphyria cấp từng cơn (AIP)?",
    [
        "<b>1. Đau bụng cấp dữ dội —</b> Triệu chứng phổ biến nhất (> 90%); đau bụng dữ dội liên tục lan tỏa khắp bụng nhưng KHÁM BỤNG HOÀN TOÀN MỀM KHÔNG CÓ PHẢN ỨNG THÀNH BỤNG (dễ bị mổ nhầm viêm ruột thừa cấp).",
        "<b>2. Bệnh lý thần kinh ngoại biên và tự chủ —</b> Nhịp tim nhanh, tăng huyết áp kịch phát, vã mồ hôi; yếu cơ gốc chi đối xứng tiến triển có thể dẫn đến liệt tứ chi và suy hô hấp đe dọa tính mạng.",
        "<b>3. Rối loạn tâm thần kinh cấp tính —</b> Lo âu dữ dội, mất ngủ, ảo giác, mê sảng, hoang tưởng, co giật; kèm hạ natri máu do tăng tiết SIADH không thích hợp.",
        "<b>Hiện tượng nước tiểu đổi màu đỏ sẫm —</b> Nước tiểu khi mới lấy ra có màu vàng trong bình thường; nhưng KHI ĐỂ NGOÀI KHÔNG KHÍ HOẶC PHƠI NẮNG, PBG bị oxy hóa tự phát thành chất màu đỏ nâu gọi là PORPHOBILIN, biến nước tiểu thành màu đỏ sẫm như màu rượu vang Port."
    ],
    "Nhiều nhà sử học y học cho rằng Vua George III của nước Anh bị mắc căn bệnh Porphyria cấp từng cơn (AIP), giải thích cho những cơn 'điên loạn' và đau bụng dữ dội từng đợt được ghi chép trong lịch sử hoàng gia."
))

cards.append(make_card(
    "HS09-B2-07",
    "Các yếu tố kích hoạt và Điều trị đặc hiệu cơn AIP",
    "ĐIỀU TRỊ CƠN AIP",
    "Kể tên các yếu tố kích hoạt cơn bùng phát AIP và trình bày cơ chế phân tử của phác đồ điều trị bằng Hemin và Glucose?",
    [
        "<b>Các yếu tố kích hoạt cơn cấp (5 chữ P) —</b> 1) Pills (thuốc cảm ứng CYP450: Barbiturat, Phenytoin, Sulfamid); 2) Poor food (nhịn đói, ăn kiêng giảm cân đột ngột); 3) Psychological stress; 4) Progesterone (giai đoạn hoàng thể chu kỳ kinh nguyệt); 5) Pain/Infection.",
        "<b>Cơ chế bùng phát chung —</b> Các yếu tố trên kích hoạt tiêu hao Hem tại gan, giải phóng ALAS-1 khỏi sự ức chế ngược, làm ALAS-1 hoạt động bùng nổ sản xuất ồ ạt ALA và PBG.",
        "<b>Thuốc giải độc đặc hiệu: Truyền tĩnh mạch HEMIN (Panhematin) —</b> Cung cấp nguồn Hemin (Fe³⁺) ngoại sinh vào gan; Hemin lập tức thực hiện cơ chế ức chế ngược dị lập thể và ức chế phiên mã ALAS-1, dập tắt tận gốc quá trình sản sinh độc tố.",
        "<b>Truyền dung dịch Glucose nồng độ cao (10 - 20%) —</b> Glucose làm tăng nồng độ insulin và ức chế protein PGC-1α (coactivator phiên mã của ALAS-1), giúp ức chế phiên mã gen ALAS-1 tại gan, dùng cho các cơn cấp mức độ nhẹ đến vừa."
    ],
    "Nguyên tắc điều trị AIP: ngừng ngay lập tức toàn bộ các thuốc nghi ngờ cảm ứng CYP450, truyền glucose tĩnh mạch trong khi chờ chế phẩm Hemin, và kiểm soát đau bằng morphin (an toàn trong AIP)."
))

cards.append(make_card(
    "HS09-B2-08",
    "Porphyria da chậm (PCT): Khiếm khuyết enzym UROD",
    "PORPHYRIA DA CHẬM (PCT)",
    "Nêu bản chất di truyền, enzym khiếm khuyết và các yếu tố cảm ứng kích hoạt bệnh Porphyria da chậm (PCT)?",
    [
        "<b>Thể Porphyria phổ biến nhất —</b> Chiếm tỷ lệ áp đảo trong các bệnh lý porphyria lâm sàng; gồm 2 thể: thể mắc phải (Type I, chiếm 80%) và thể di truyền lặn/trội (Type II, chiếm 20%).",
        "<b>Enzym khiếm khuyết —</b> UROPORPHYRINOGEN DECARBOXYLASE (UROD) ở Bước 5 của quá trình tổng hợp Hem.",
        "<b>Chất ứ đọng bệnh lý —</b> Uroporphyrinogen III và các porphyrinogen carboxyl hóa trung gian bị ứ đọng nồng độ rất cao tại gan, sau đó tràn vào máu và lắng đọng tại lớp trung bì da.",
        "<b>Các yếu tố nguy cơ và cảm ứng mắc phải —</b> Nghiện rượu mạn tính, hút thuốc lá, nhiễm virus Viêm gan C (HCV > 50% bệnh nhân PCT), tình trạng quá tải sắt (bệnh ứ sắt di truyền HFE Hemochromatosis), và sử dụng Estrogen (thuốc tránh thai)."
    ],
    "Trong thể mắc phải, sự kết hợp giữa rượu, virus viêm gan C và quá tải sắt tạo ra chất ức chế enzym UROD mang tên Uroporphomethene, làm tê liệt hoạt tính UROD tại tế bào gan."
))

cards.append(make_card(
    "HS09-B2-09",
    "Cơ chế Nhạy cảm ánh sáng da dữ dội và Nước tiểu huỳnh quang trong PCT",
    "PORPHYRIA DA CHẬM (PCT)",
    "Phân tích cơ chế gây bọng nước ngoài da do ánh sáng mặt trời và đặc điểm huỳnh quang nước tiểu của bệnh nhân PCT?",
    [
        "<b>Cơ chế tạo gốc oxy hóa tự do —</b> Phân tử Uroporphyrinogen lắng đọng dưới da bị oxy hóa thành Uroporphyrin mang vòng porphyrin khép kín; vòng này hấp thụ cực mạnh photon tia cực tím (dải Soret 400 - 410 nm).",
        "<b>Tạo Oxy đơn bội (Singlet Oxygen) —</b> Phân tử porphyrin kích thích truyền năng lượng cho oxy hòa tan tạo Oxy đơn bội (¹O2) và các gốc tự do ROS phá hủy màng tế bào, kích hoạt giải phóng enzym tiêu thể làm hoại tử lớp thượng bì da.",
        "<b>Tổn thương da ở vùng phơi nắng —</b> Xuất hiện các bọng nước dễ vỡ ở mu bàn tay, cẳng tay, mặt và cổ sau khi tiếp xúc nắng; lành để lại vết trợt loét, sẹo teo, hạt kê (milia), tăng sắc tố và rậm lông vùng thái dương mặt (Hypertrichosis).",
        "<b>Nước tiểu phát huỳnh quang màu hồng đỏ —</b> Nước tiểu có màu đỏ nâu như màu trà sẫm hoặc rượu vang; khi soi dưới đèn ánh sáng cực tím Wood (Wood's lamp λ = 365 nm), các phân tử porphyrin PHÁT HUỲNH QUANG MÀU ĐỎ HỒNG RỰC RỠ đặc trưng."
    ],
    "Hình ảnh tổn thương da trợt loét hoại tử kèm rậm lông mặt và sợ ánh sáng mặt trời trong các thể Porphyria da nặng thời cổ đại được xem là nguồn gốc khởi thủy của truyền thuyết dân gian về 'Ma cà rồng' (Vampires)."
))

cards.append(make_card(
    "HS09-B2-10",
    "Phác đồ điều trị bệnh Porphyria da chậm (PCT)",
    "ĐIỀU TRỊ BỆNH PCT",
    "Trình bày 2 biện pháp điều trị nền tảng của Porphyria da chậm: Trích máu tĩnh mạch và Hydroxychloroquine liều thấp?",
    [
        "<b>1. Trích máu tĩnh mạch định kỳ (Phlebotomy - Lựa chọn số 1) —</b> Rút 450 - 500 ml máu mỗi 1 - 2 tuần cho đến khi nồng độ Ferritin huyết thanh hạ xuống mức đích 20 µg/L.",
        "<b>Cơ chế trích máu —</b> Giảm bớt lượng sắt dự trữ tại gan; sắt giảm làm giảm stress oxy hóa và giải phóng enzym UROD khỏi sự ức chế của uroporphomethene, giúp phục hồi hoạt tính UROD và làm sạch porphyrin máu.",
        "<b>2. Hydroxychloroquine hoặc Chloroquine LIỀU THẤP —</b> Dùng liều thấp (100 mg x 2 lần/tuần; tuyệt đối không dùng liều cao thông thường vì có thể gây hoại tử gan cấp do giải phóng ồ ạt porphyrin).",
        "<b>Cơ chế thuốc chống sốt rét —</b> Hydroxychloroquine tạo phức chất phối trí hòa tan với porphyrin trong lysosome tế bào gan, kích thích sự bài xuất porphyrin ra nước tiểu.",
        "<b>Các biện pháp phối hợp —</b> Ngừng tuyệt đối rượu bia, ngừng thuốc chứa estrogen, điều trị triệt để viêm gan virus C bằng thuốc kháng virus tác dụng trực tiếp (DAA), và che chắn nắng nghiêm ngặt."
    ],
    "Điều trị bằng trích máu hoặc hydroxychloroquine liều thấp đem lại hiệu quả lâm sàng ngoạn mục: các bọng nước da biến mất hoàn toàn sau vài tháng và bệnh nhân có thể phơi nắng trở lại bình thường."
))

# ==============================================================================
# SECTION B3: THOÁI HÓA HEMOGLOBIN TẠI ĐẠI THỰC BÀO (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B3-01",
    "Tuổi thọ hồng cầu và Hệ liên võng nội mô tiêu hủy",
    "THOÁI HÓA HEMOGLOBIN",
    "Nêu tuổi thọ trung bình của hồng cầu và phân tích vai trò của Hệ liên võng nội mô trong việc dọn dẹp hồng cầu già?",
    [
        "<b>Đời sống hồng cầu 120 ngày —</b> Hồng cầu trưởng thành lưu hành trong máu trung bình khoảng 120 ngày; khi già màng tế bào mất tính mềm dẻo, giảm enzym chống oxy hóa và bộc lộ phosphatidylserin ở lớp ngoài màng.",
        "<b>Hệ thống đại thực bào liên võng nội mô (RES / MPS) —</b> Tiêu hủy hồng cầu già chủ yếu tại ĐẠI THỰC BÀO Ở LÁCH (các dây tủy lách Red pulp lọc giữ hồng cầu cứng), TỦY XƯƠNG và TẾ BÀO KUPFFER TẠI GAN.",
        "<b>Khối lượng thoái hóa hằng ngày —</b> Hằng ngày có khoảng 1 - 2 x 10¹¹ hồng cầu già bị tiêu hủy, tương ứng giải phóng khoảng 6 đến 7 g Hemoglobin.",
        "<b>Bảo toàn nguyên liệu —</b> Quá trình thoái hóa được kiểm soát chặt chẽ nhằm thu hồi tối đa lượng sắt quý giá và tái sử dụng toàn bộ chuỗi acid amin của globin."
    ],
    "Lách được mệnh danh là 'nghĩa trang của hồng cầu': cấu trúc xoang lách với các khe hẹp chỉ 2 - 3 µm buộc hồng cầu phải biến dạng tối đa để đi qua; các hồng cầu già cứng ngắc sẽ bị kẹt lại và bị đại thực bào lách nuốt chửng."
))

cards.append(make_card(
    "HS09-B3-02",
    "Số phận phân giải ban đầu của phân tử Hemoglobin",
    "THOÁI HÓA HEMOGLOBIN",
    "Mô tả bước tách rời ban đầu giữa Globin và nhóm ngoại Hem bên trong túi thực bào?",
    [
        "<b>Tách rời liên kết phối trí —</b> Sau khi hồng cầu bị đại thực bào thực bào, phân tử Hemoglobin bị phân tách thành 2 thành phần độc lập: phần protein GLOBIN và nhóm ngoại HEM.",
        "<b>Thủy phân chuỗi Globin —</b> Các enzym protease nội tiêu thể (Cathepsin) của đại thực bào thủy phân triệt để các chuỗi polypeptid α và β của globin thành các ACID AMIN TỰ DO.",
        "<b>Tái hòa nhập Quỹ acid amin —</b> Toàn bộ acid amin giải phóng được đưa trở lại dòng máu hòa vào Quỹ acid amin chung của cơ thể để phục vụ tổng hợp protein mới.",
        "<b>Chuyển tiếp nhóm ngoại Hem —</b> Phân tử Hem chứa ion sắt tự do được chuyển ngay đến màng lưới nội sinh chất để enzym Heme Oxygenase xử lý mở vòng."
    ],
    "Globin chiếm tới 96% trọng lượng của phân tử hemoglobin; việc tái thu hồi toàn bộ acid amin của globin giúp cơ thể tiết kiệm một lượng lớn nitơ dinh dưỡng hàng ngày."
))

cards.append(make_card(
    "HS09-B3-03",
    "Bước 1: Enzym Heme Oxygenase (HO) mở vòng Hem tạo Biliverdin",
    "THOÁI HÓA HEM",
    "Trình bày phương trình phản ứng, vị trí nội bào và cơ chế mở vòng của enzym Heme Oxygenase?",
    [
        "<b>Vị trí nội bào —</b> Định vị trên màng lưới nội sinh chất trơn của đại thực bào; là một phức hợp enzym phụ thuộc Cytochrom P450.",
        "<b>Đồng cơ chất bắt buộc —</b> Đòi hỏi 3 phân tử Oxy phân tử (O2) và chất khử NADPH + H⁺.",
        "<b>Phương trình phản ứng —</b> Hem + 3 O2 + 3 NADPH + 3 H⁺ → Biliverdin + Fe³⁺ + CO + 3 NADP⁺ + 3 H2O.",
        "<b>Cắt mở chọn lọc cầu nối α-methenyl —</b> Heme Oxygenase tấn công oxy hóa chọn lọc vào cầu nối α-methenyl (nằm giữa vòng pyrrol I và II), bẻ gãy cấu trúc vòng kín và giải phóng nguyên tử carbon này dưới dạng khí Carbon Monoxide (CO).",
        "<b>Sản phẩm Biliverdin —</b> Tạo thành sắc tố mật mạch thẳng gồm 4 vòng pyrrol mang tên BILIVERDIN có MÀU XANH LỤC đặc trưng."
    ],
    "Enzym Heme Oxygenase có 2 dạng đồng phân: HO-1 là dạng cảm ứng (tăng vọt khi có tan máu, stress oxy hóa, thiếu máu cục bộ) và HO-2 là dạng cấu tạo biểu hiện liên tục tại não và tinh hoàn."
))

cards.append(make_card(
    "HS09-B3-04",
    "Ba sản phẩm then chốt giải phóng từ phản ứng Heme Oxygenase",
    "THOÁI HÓA HEM",
    "Nêu số phận và ý nghĩa sinh học của 3 sản phẩm giải phóng từ phản ứng mở vòng Hem bởi Heme Oxygenase?",
    [
        "<b>1. Ion Sắt (Fe³⁺) —</b> Sắt được giải phóng ở dạng Ferric (Fe³⁺); được xuất bào ra máu gắn ngay vào protein vận chuyển TRANSFERRIN đưa về tủy xương tái sinh hồng cầu mới, hoặc dự trữ an toàn trong mô dưới dạng FERRITIN.",
        "<b>2. Khí Carbon Monoxide (CO) —</b> Phản ứng Heme Oxygenase là NGUỒN NỘI SINH DUY NHẤT trong cơ thể người sản sinh ra khí CO; lượng CO này khuếch tán vào máu gắn nhẹ với hemoglobin (tạo Carboxy-Hb sinh lý 0,5 - 1%) và đào thải hoàn toàn qua phổi.",
        "<b>Vai trò sinh lý của CO nội sinh —</b> Đóng vai trò chất truyền tin thứ hai (tương tự khí NO) kích hoạt guanylyl cyclase tạo cGMP gây giãn mạch máu, chống viêm và ức chế kết tập tiểu cầu.",
        "<b>3. Sắc tố mật Biliverdin —</b> Sắc tố mạch thẳng màu xanh lục; lập tức được chuyển sang phản ứng khử thứ hai trong bào tương."
    ],
    "Đo nồng độ khí CO trong khí thở ra (end-tidal CO) là một phương pháp đo lường không xâm lấn chính xác tốc độ tan máu và thoái hóa hemoglobin trong cơ thể."
))

cards.append(make_card(
    "HS09-B3-05",
    "Bước 2: Enzym Biliverdin Reductase khử Biliverdin tạo Bilirubin",
    "THOÁI HÓA HEM",
    "Trình bày phản ứng khử Biliverdin tạo Bilirubin tự do bởi enzym Biliverdin Reductase?",
    [
        "<b>Vị trí phản ứng —</b> Trong dịch bào tương của đại thực bào hệ liên võng nội mô.",
        "<b>Enzym xúc tác —</b> BILIVERDIN REDUCTASE (sử dụng coenzym NADPH hoặc NADH).",
        "<b>Phương trình phản ứng —</b> Biliverdin + NADPH + H⁺ → Bilirubin (IXα) + NADP⁺.",
        "<b>Cơ chế biến đổi cấu trúc —</b> Enzym bơm thêm 2 nguyên tử hydro vào cầu nối methenyl trung tâm (cầu nối γ), chuyển liên kết đôi thành liên kết đơn methylen (-CH2-).",
        "<b>Biến đổi màu sắc —</b> Phân tử Biliverdin màu xanh lục được chuyển hóa thành phân tử BILIRUBIN TỰ DO mang MÀU VÀNG CAM đặc trưng."
    ],
    "Ở các loài chim, bò sát và động vật lưỡng cư, quá trình thoái hóa dừng lại ở Biliverdin (tan trong nước và bài tiết thẳng ra ngoài phân làm phân chim có màu xanh). Động vật có vú tiêu tốn thêm năng lượng NADPH để chuyển Biliverdin thành Bilirubin kỵ nước."
))

cards.append(make_card(
    "HS09-B3-06",
    "Cấu trúc 6 liên kết hydro nội phân tử của Bilirubin tự do",
    "CẤU TRÚC PHÂN TỬ BILIRUBIN",
    "Phân tích cấu trúc không gian 3 chiều và vai trò của 6 liên kết hydro nội phân tử của phân tử Bilirubin tự do?",
    [
        "<b>Công thức hóa học mang tính phân cực trên mặt phẳng —</b> Mang 2 nhóm carboxyl (-COOH) của chuỗi bên propionat và các nhóm amin/lactam nhô ra ngoài.",
        "<b>Tự cuộn gập hình chữ V khép kín —</b> Trong không gian 3D, phân tử Bilirubin tự gập nếp uốn cong hình sống mái nhà hoặc hình chữ V khép kín.",
        "<b>Mạng lưới 6 liên kết hydro nội phân tử —</b> Hai nhóm -COOH tạo liên kết hydro nội tại cực kỳ bền vững với các nguyên tử nitơ và oxy của các vòng pyrrol đối diện (mỗi nhóm carboxyl tạo 3 liên kết hydro, tổng cộng 6 liên kết).",
        "<b>Hiệu ứng 'Giấu kín nhóm ưa nước' —</b> Hệ thống liên kết hydro nội phân tử giấu kín hoàn toàn các nhóm phân cực vào bên trong lòng phân tử, quay toàn bộ các khung hydrocacbon kỵ nước ra ngoài tiếp xúc với dung môi."
    ],
    "Sự tồn tại của 6 liên kết hydro nội phân tử là lời giải thích duy nhất cho nghịch lý hóa học: tại sao một phân tử mang tới 2 nhóm carboxyl acid (-COOH) lại hoàn toàn không tan trong nước."
))

cards.append(make_card(
    "HS09-B3-07",
    "Bản chất kỵ nước tuyệt đối của Bilirubin tự do và độc tính màng",
    "TÍNH CHẤT BILIRUBIN TỰ DO",
    "Nêu các đặc tính lý hóa và độc tính tế bào của Bilirubin tự do (Bilirubin gián tiếp)?",
    [
        "<b>Hoàn toàn không tan trong nước ở pH sinh lý —</b> Độ tan trong nước ở pH 7,4 cực kỳ thấp (< 0,1 µmol/L).",
        "<b>Hòa tan mạnh trong lipid màng tế bào —</b> Tính kỵ nước cao giúp Bilirubin tự do hòa tan dễ dàng vào lớp màng phospholipid kép của tế bào và mô mỡ.",
        "<b>Độc tính thần kinh cao —</b> Dễ dàng ngấm qua màng tế bào nơ-ron và chèn vào màng ty thể, gây ức chế chuỗi hô hấp tế bào, ngừng tổng hợp ATP và kích hoạt chết tế bào nơ-ron theo chương trình (Apoptosis).",
        "<b>Không thể lọc qua cầu thận —</b> Do kỵ nước và gắn chặt với Albumin, Bilirubin tự do HOÀN TOÀN KHÔNG THỂ LỌC QUA MÀNG LỌC CẦU THẬN; do đó nước tiểu của người bình thường và người vàng da tan máu tuyệt đối không có sắc tố mật."
    ],
    "Bilirubin tự do ở nồng độ sinh lý thấp được xem là một chất chống oxy hóa nội sinh mạnh mẽ bảo vệ lipid màng khỏi bị peroxy hóa; nhưng khi nồng độ tăng cao vượt sức chứa của albumin nó trở thành độc chất thần kinh chết người."
))

cards.append(make_card(
    "HS09-B3-08",
    "Sự chuyển biến màu sắc của Vết bầm tím dưới da (Hematoma)",
    "HÓA SINH LÂM SÀNG",
    "Giải thích cơ chế hóa sinh giải thích sự thay đổi màu sắc tuần tự của vết bầm máu dưới da theo thời gian?",
    [
        "<b>Giai đoạn 1 (Ngay sau chấn thương: Màu đỏ tía / Xanh đen) —</b> Mạch máu nhỏ bị vỡ, hồng cầu thoát mạch tụ lại dưới da; màu đỏ sẫm là màu của Oxyhemoglobin và Deoxyhemoglobin thoát mạch.",
        "<b>Giai đoạn 2 (Sau 1 - 2 ngày: Chuyển sang màu Xanh lục) —</b> Các đại thực bào mô di chuyển đến thực bào hồng cầu; enzym Heme Oxygenase mở vòng Hem tạo sắc tố BILIVERDIN CÓ MÀU XANH LỤC.",
        "<b>Giai đoạn 3 (Sau 3 - 5 ngày: Chuyển sang màu Vàng cam) —</b> Enzym Biliverdin Reductase khử biliverdin thành BILIRUBIN TỰ DO CÓ MÀU VÀNG CAM.",
        "<b>Giai đoạn 4 (Sau 1 - 2 tuần: Vàng nhạt rồi biến mất) —</b> Bilirubin được đại thực bào giải phóng vào máu đưa về gan xử lý hoặc oxy hóa thành các sản phẩm hòa tan không màu, vết bầm lành lặn hoàn toàn."
    ],
    "Vết bầm tím dưới da (Hematoma) là một 'phòng thí nghiệm hóa sinh sống động' ngay trước mắt bác sĩ, minh họa trọn vẹn chuỗi phản ứng thoái hóa từ Hem → Biliverdin → Bilirubin."
))

cards.append(make_card(
    "HS09-B3-09",
    "Thoái hóa Hemoglobin nội mạch (< 10%) và vai trò của Haptoglobin",
    "THOÁI HÓA NỘI MẠCH",
    "Mô tả con đường thoái hóa Hemoglobin nội mạch và vai trò dọn dẹp bảo vệ thận của Haptoglobin và Hemopexin?",
    [
        "<b>Thoái hóa nội mạch sinh lý (< 10%) —</b> Một lượng nhỏ hồng cầu bị vỡ trực tiếp ngay trong lòng mạch máu, giải phóng các dimer dị phần (αβ) của Hemoglobin tự do vào huyết tương.",
        "<b>Bắt giữ bởi Haptoglobin —</b> Phân tử HAPTOGLOBIN (một α2-globulin do gan tiết ra) liên kết cộng hóa trị ái lực cực cao với dimer Hemoglobin tự do tạo phức hợp [Haptoglobin - Hemoglobin] kích thước lớn.",
        "<b>Ngăn ngừa tổn thương ống thận —</b> Phức hợp kích thước lớn không thể lọc qua cầu thận, ngăn cản Hemoglobin thất thoát ra nước tiểu và ngăn chặn độc tính làm tắc nghẽn hoại tử ống thận cấp.",
        "<b>Thanh thải tại tế bào gan —</b> Phức hợp được tế bào gan nhận diện qua thụ thể CD163 của đại thực bào và tiêu hủy an toàn; nồng độ Haptoglobin huyết tương SỤT GIẢM VỀ 0 là dấu ấn sinh hóa nhạy nhất xác định có TAN MÁU NỘI MẠCH.",
        "<b>Vai trò của Hemopexin —</b> Khi Haptoglobin cạn kiệt, Hem tự do bị oxy hóa thành Methemoglobin giải phóng Hem tự do; Hemopexin (β-globulin) liên kết với Hem tự do đưa về gan bảo tồn sắt."
    ],
    "Khi cả Haptoglobin và Hemopexin đều bị bão hòa cạn kiệt trong các cơn tan máu nội mạch ồ ạt, Hemoglobin tự do sẽ lọc qua cầu thận gây Hemoglobin niệu (nước tiểu màu xá xị hoặc màu nâu đen) và suy thận cấp."
))

cards.append(make_card(
    "HS09-B3-10",
    "Tổng kết sơ đồ luân chuyển từ Đại thực bào về Gan",
    "SƠ ĐỒ CHUYỂN HÓA SẮC TỐ MẬT",
    "Tóm tắt hành trình của sắc tố mật từ khi hồng cầu bị đại thực bào tiêu hủy cho đến khi đến màng tế bào gan?",
    [
        "<b>Tại Đại thực bào (Lách/Tủy xương/Kupffer) —</b> Hồng cầu già → Hemoglobin → Tách Globin (thủy phân thành acid amin) + Hem → Heme Oxygenase tạo Biliverdin + Fe³⁺ + CO → Biliverdin Reductase tạo Bilirubin tự do.",
        "<b>Xuất bào vào dòng máu —</b> Bilirubin tự do kỵ nước khuếch tán ra khỏi đại thực bào vào huyết tương mao mạch.",
        "<b>Vận chuyển trong huyết tương —</b> Gắn lập tức với Albumin huyết thanh tạo phức hợp hòa tan không độc [Albumin - Bilirubin].",
        "<b>Đến xoang mao mạch gan —</b> Theo dòng máu tuần hoàn đổ vào các xoang mao mạch gan, tiến vào khoang Disse nằm sát bề mặt tế bào gan.",
        "<b>Tách rời để tiếp nhận —</b> Bilirubin tách rời khỏi Albumin tại khoang Disse để chuẩn bị vận chuyển qua màng đáy xoang vào trong tế bào gan."
    ],
    "Toàn bộ giai đoạn này diễn ra ngoài gan; mọi rối loạn làm tăng phá hủy hồng cầu ở giai đoạn này đều làm tăng vọt nồng độ Bilirubin tự do (gián tiếp) trong máu."
))

# ==============================================================================
# SECTION B4: VẬN CHUYỂN ALBUMIN, BẮT GIỮ OATP, LIÊN HỢP UGT1A1 & BÀI TIẾT MRP2 (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B4-01",
    "Cơ chế vận chuyển Bilirubin tự do trong máu nhờ Albumin",
    "VẬN CHUYỂN QUA ALBUMIN",
    "Trình bày đặc tính liên kết của phân tử Albumin huyết thanh với Bilirubin tự do và sức chứa tối đa?",
    [
        "<b>Liên kết phi cộng hóa trị thuận nghịch —</b> Bilirubin tự do kỵ nước liên kết với Albumin thông qua các tương tác kỵ nước và liên kết tĩnh điện ion.",
        "<b>Vị trí gắn kết ái lực cao —</b> Mỗi phân tử Albumin sở hữu một vị trí gắn kết có ái lực cực kỳ cao với hằng số phân ly Kd ≈ 10⁻⁸ M, đảm bảo gần như 99,9% Bilirubin tự do trong máu đều ở trạng thái gắn Albumin.",
        "<b>Vị trí gắn kết ái lực thấp —</b> Có thêm 1 đến 2 vị trí phụ với ái lực yếu hơn, chỉ tham gia gắn khi nồng độ Bilirubin trong máu tăng rất cao.",
        "<b>Sức chứa gắn kết tối đa —</b> Ở người bình thường với nồng độ Albumin máu 40 g/L (~600 µmol/L), Albumin có khả năng gắn kết tối đa tới 25 - 30 mg/dL (> 400 µmol/L) Bilirubin."
    ],
    "Nhờ có Albumin làm 'xe chuyên chở', phân tử Bilirubin kỵ nước có thể lưu hành an toàn trong lòng mạch nước mà không bị kết tủa và không ngấm vào các màng tế bào."
))

cards.append(make_card(
    "HS09-B4-02",
    "Hiện tượng Cạnh tranh vị trí gắn Albumin và Nguy cơ Vàng da nhân não",
    "DƯỢC LÝ LÂM SÀNG SƠ SINH",
    "Giải thích cơ chế phân tử vì sao các thuốc như Sulfamid và Ceftriaxone có thể kích hoạt Vàng da nhân não ở trẻ sơ sinh?",
    [
        "<b>Thuốc có ái lực cao với cùng vị trí trên Albumin —</b> Các thuốc có tính acid anion như Sulfamid kháng khuẩn (Sulfamethoxazol), Ceftriaxone, Salicylat/Aspirin, và thuốc chống viêm NSAIDs liên kết mạnh vào vị trí gắn Bilirubin trên Albumin.",
        "<b>Đẩy bật Bilirubin tự do ra ngoài —</b> Thuốc cạnh tranh và chiếm chỗ, đẩy Bilirubin ra khỏi phân tử Albumin vào huyết tương dưới dạng phân tử tự do không liên kết (Free Unbound Bilirubin).",
        "<b>Xuyên qua Hàng rào máu - não non nớt —</b> Phân tử Bilirubin tự do không liên kết cực kỳ kỵ nước, dễ dàng ngấm xuyên qua lớp tế bào nội mô hàng rào máu - não của trẻ sơ sinh.",
        "<b>Kích hoạt Vàng da nhân não (Kernicterus) —</b> Lắng đọng vào các nhân xám đáy não gây hoại tử nơ-ron và di chứng bại não vĩnh viễn, dù xét nghiệm nồng độ Bilirubin toàn phần đo được có thể chưa vượt ngưỡng chiếu đèn!"
    ],
    "Cảnh báo dược lý lâm sàng tuyệt đối: Chống chỉ định dùng Ceftriaxone và các kháng sinh nhóm Sulfamid cho trẻ sơ sinh dưới 28 ngày tuổi, đặc biệt trẻ sơ sinh đang có vàng da."
))

cards.append(make_card(
    "HS09-B4-03",
    "Quá trình bắt giữ Bilirubin tại màng xoang tế bào gan nhờ OATP1B1 và OATP1B3",
    "BẮT GIỮ BILIRUBIN TẠI GAN",
    "Mô tả cơ chế bắt giữ Bilirubin từ xoang mạch gan vào bào tương tế bào gan nhờ các protein OATP?",
    [
        "<b>Tách rời tại khoang Disse —</b> Khi phức hợp [Albumin - Bilirubin] di chuyển vào xoang mao mạch gan, tại khoang Disse phân tử Bilirubin tách rời khỏi Albumin.",
        "<b>Protein vận chuyển OATP1B1 và OATP1B3 —</b> Bilirubin được vận chuyển qua màng đáy xoang vào trong tế bào chất nhờ 2 chất vận chuyển anion hữu cơ đặc hiệu tại màng tế bào gan: OATP1B1 (mã hóa bởi gen SLCO1B1) và OATP1B3 (SLCO1B3).",
        "<b>Cơ chế khuếch tán thuận hóa —</b> Vận chuyển theo chiều gradient nồng độ không tiêu tốn trực tiếp ATP.",
        "<b>Ý nghĩa bệnh học —</b> Đột biến bất hoạt đồng thời cả hai gen SLCO1B1 và SLCO1B3 làm gan mất khả năng bắt giữ Bilirubin, gây ra BỆNH HỘI CHỨNG ROTOR."
    ],
    "Các thuốc như Rifampicin hoặc thuốc ức chế protease điều trị HIV có thể ức chế cạnh tranh với OATP1B1/3, gây tăng Bilirubin máu thoáng qua khi bắt đầu dùng thuốc."
))

cards.append(make_card(
    "HS09-B4-04",
    "Vai trò của Ligandin (Protein Y) và Protein Z nội bào gan",
    "VẬN CHUYỂN NỘI BÀO GAN",
    "Nêu vai trò của Ligandin (Protein Y) và Protein Z trong việc vận chuyển Bilirubin bên trong bào tương tế bào gan?",
    [
        "<b>Bản chất Ligandin —</b> Là một protein hòa tan phong phú trong bào tương tế bào gan, thuộc họ enzym Glutathione S-Transferase B1 (GSTB1, trước đây gọi là Protein Y).",
        "<b>Gắn giữ Bilirubin ái lực cao —</b> Ngay khi Bilirubin vừa qua màng xoang vào bào tương, Ligandin gắn chặt vào phân tử Bilirubin với ái lực cao.",
        "<b>Ngăn ngừa khuếch tán ngược —</b> Việc gắn kết giữ nồng độ Bilirubin tự do dạng hòa tan trong bào tương ở mức cực thấp, ngăn không cho Bilirubin khuếch tán ngược trở lại máu xoang gan.",
        "<b>Vận chuyển đến Lưới nội chất —</b> Ligandin đóng vai trò như người dẫn đường, vận chuyển an toàn phân tử Bilirubin từ màng xoang đến màng lưới nội sinh chất để thực hiện phản ứng liên hợp.",
        "<b>Protein Z —</b> Một protein gắn acid béo (FABP) đóng vai trò hỗ trợ phụ khi lượng Bilirubin trong tế bào gan tăng cao."
    ],
    "Ở trẻ sơ sinh, lượng protein Ligandin trong tế bào gan chưa được biểu hiện đầy đủ lúc mới sinh; sự thiếu hụt tương đối này góp phần làm chậm trễ khâu thanh thải Bilirubin gây vàng da sinh lý sơ sinh."
))

cards.append(make_card(
    "HS09-B4-05",
    "Mục đích sinh học và Vị trí của Phản ứng Liên hợp Bilirubin",
    "LIÊN HỢP BILIRUBIN",
    "Trình bày mục đích sinh học và vị trí nội bào của phản ứng liên hợp Bilirubin tại tế bào gan?",
    [
        "<b>Mục đích sinh học sống còn —</b> Chuyển hóa phân tử Bilirubin tự do kỵ nước, không tan trong nước, độc thần kinh thành dạng BILIRUBIN LIÊN HỢP HOÀN TOÀN TAN TRONG NƯỚC, mất độc tính và có thể đào thải ra ngoài theo dịch mật.",
        "<b>Vị trí nội bào —</b> Định vị tại màng LƯỚI NỘI SINH CHẤT TRƠN VÀ HẠT (Endoplasmic Reticulum) của tế bào biểu mô gan.",
        "<b>Bản chất hóa học —</b> Gắn các gốc phân cực Acid Glucuronic vào các nhóm carboxyl propionat của phân tử Bilirubin.",
        "<b>Phá vỡ liên kết hydro nội tại —</b> Sự gắn nhóm glucuronat cồng kềnh tích điện âm phá vỡ hoàn toàn mạng lưới 6 liên kết hydro nội phân tử, phơi bày các nhóm ưa nước ra ngoài tiếp xúc với dung môi nước."
    ],
    "Không có phản ứng liên hợp tại lưới nội chất tế bào gan, cơ thể hoàn toàn bất lực trong việc đào thải sắc tố mật ra ngoài môi trường."
))

cards.append(make_card(
    "HS09-B4-06",
    "Cơ chất UDP-Acid Glucuronic (UDPGA) và con đường Acid Uronic",
    "CƠ CHẤT LIÊN HỢP",
    "Trình bày nguồn gốc sinh tổng hợp của cơ chất UDP-Acid Glucuronic (UDPGA) trong tế bào gan?",
    [
        "<b>Nguồn gốc từ Glucose —</b> UDP-Acid Glucuronic (UDPGA) được tổng hợp tại bào tương tế bào gan thông qua nhánh chuyển hóa Con đường Acid Uronic từ Glucose.",
        "<b>Chuỗi phản ứng sinh tổng hợp —</b> Glucose → Glucose-6-Phosphat → Glucose-1-Phosphat → UDP-Glucose.",
        "<b>Oxy hóa bởi UDP-Glucose Dehydrogenase —</b> Enzym UDP-Glucose Dehydrogenase tại gan xúc tác oxy hóa nhóm rượu bậc 1 (-CH2OH) ở C6 của UDP-Glucose thành nhóm carboxyl (-COOH), sử dụng 2 phân tử NAD⁺ để tạo thành UDP-ACID GLUCURONIC (UDPGA).",
        "<b>Chất cho nhóm Glucuronyl hoạt hóa —</b> UDPGA là chất nhượng gốc acid glucuronic hoạt hóa vạn năng cho các phản ứng liên hợp glucuronid giải độc thuốc, bilirubin và hormon steroid."
    ],
    "Con đường acid uronic ở người không thể tổng hợp được Vitamin C (Acid Ascorbic) do thiếu enzym L-Gulonolactone Oxidase; toàn bộ UDPGA phục vụ cho liên hợp giải độc tại gan và tổng hợp proteoglycan."
))

cards.append(make_card(
    "HS09-B4-07",
    "Enzym UDP-Glucuronosyltransferase 1A1 (UGT1A1) và hai bước liên hợp",
    "ENZYM UGT1A1",
    "Mô tả hai bước phản ứng liên hợp tạo Bilirubin Diglucuronid xúc tác bởi enzym UGT1A1?",
    [
        "<b>Enzym xúc tác —</b> UDP-GLUCURONOSYLTRANSFERASE 1A1 (UGT1A1), gắn trên màng lưới nội sinh chất tế bào gan, mã hóa bởi cụm gen UGT1A trên NST số 2.",
        "<b>Bước 1: Tạo Bilirubin Monoglucuronid (BMG) —</b> UGT1A1 chuyển 1 gốc acid glucuronic từ UDPGA gắn vào 1 nhóm carboxyl propionat của Bilirubin qua liên kết ester: Bilirubin + UDPGA → Bilirubin Monoglucuronid (BMG) + UDP.",
        "<b>Bước 2: Tạo Bilirubin Diglucuronid (BDG) —</b> Tiếp tục gắn gốc acid glucuronic thứ hai vào nhóm carboxyl propionat còn lại: BMG + UDPGA → BILIRUBIN DIGLUCURONID (BDG) + UDP.",
        "<b>Tỷ lệ sản phẩm trong dịch mật bình thường —</b> Khoảng 85% là Bilirubin Diglucuronid (BDG) và khoảng 15% là Bilirubin Monoglucuronid (BMG)."
    ],
    "Khi chức năng gan bị suy giảm nhẹ hoặc ở trẻ sơ sinh, tỷ lệ BMG trong dịch mật có thể tăng lên do bước gắn gốc thứ hai bị chậm trễ."
))

cards.append(make_card(
    "HS09-B4-08",
    "Đặc tính lý hóa khác biệt của Bilirubin liên hợp (Bilirubin trực tiếp)",
    "ĐẶC TÍNH BILIRUBIN LIÊN HỢP",
    "So sánh các đặc tính lý hóa và sinh học căn bản giữa Bilirubin liên hợp (trực tiếp) và Bilirubin tự do (gián tiếp)?",
    [
        "<b>Độ tan trong nước —</b> Bilirubin liên hợp TAN HOÀN TOÀN TRONG NƯỚC; Bilirubin tự do hoàn toàn không tan trong nước.",
        "<b>Khả năng gắn Albumin trong máu —</b> Bilirubin liên hợp liên kết lỏng lẻo với Albumin; Bilirubin tự do gắn liên kết phi cộng hóa trị cực kỳ chặt chẽ với Albumin.",
        "<b>Độc tính thần kinh —</b> Bilirubin liên hợp KHÔNG CÓ ĐỘC TÍNH THẦN KINH và không ngấm qua hàng rào máu não; Bilirubin tự do có độc tính thần kinh rất cao.",
        "<b>Khả năng bài xuất qua nước tiểu —</b> Bilirubin liên hợp khi tăng cao trong máu DỄ DÀNG LỌC QUA CẦU THẬN làm nước tiểu có màu vàng sẫm bọt vàng (sắc tố mật dương tính); Bilirubin tự do tuyệt đối không thể lọc qua cầu thận.",
        "<b>Đào thải qua mật —</b> Bilirubin liên hợp sẵn sàng được bài tiết qua màng vi mật quản xuống ruột; Bilirubin tự do không thể bài tiết trực tiếp vào mật."
    ],
    "Sự biến đổi từ dạng tự do kỵ nước sang dạng liên hợp tan trong nước là bước ngoặt quyết định cho phép cơ thể tống xuất hoàn toàn chất thải sắc tố mật ra ngoài."
))

cards.append(make_card(
    "HS09-B4-09",
    "Phản ứng Diazo Van den Bergh phân biệt Bilirubin Trực tiếp vs. Gián tiếp",
    "XÉT NGHIỆM VAN DEN BERGH",
    "Giải thích nguyên lý phản ứng Diazo Van den Bergh và cách tính nồng độ Bilirubin gián tiếp trong phòng xét nghiệm?",
    [
        "<b>Thuốc thử Diazo Van den Bergh —</b> Hỗn hợp acid sulfanilic diazo hóa (sulfanilic acid + natri nitrit trong HCl); phản ứng với bilirubin tạo phức chất màu hồng tím (azobilirubin).",
        "<b>Phản ứng Trực tiếp (Direct Bilirubin) —</b> Bilirubin liên hợp tan tốt trong nước nên PHẢN ỨNG NGAY LẬP TỨC TRONG VÒNG 1 PHÚT với thuốc thử diazo trong dung dịch nước; do đó được định danh là BILIRUBIN TRỰC TIẾP.",
        "<b>Phản ứng Toàn phần (Total Bilirubin) —</b> Thêm dung môi cồn (methanol) hoặc chất gia tốc (caffein) để phá vỡ các liên kết hydro nội phân tử và tách Bilirubin tự do khỏi Albumin, cho phép TOÀN BỘ BILIRUBIN phản ứng tạo màu.",
        "<b>Cách tính Bilirubin Gián tiếp (Indirect Bilirubin) —</b> Bilirubin gián tiếp không đo trực tiếp mà được tính bằng công thức hiệu số: [Bilirubin Gián tiếp] = [Bilirubin Toàn phần] - [Bilirubin Trực tiếp]."
    ],
    "Tên gọi lâm sàng 'Bilirubin trực tiếp' và 'Bilirubin gián tiếp' hoàn toàn bắt nguồn từ đặc tính phản ứng diazo hóa của kỹ thuật xét nghiệm kinh điển Van den Bergh từ năm 1916."
))

cards.append(make_card(
    "HS09-B4-10",
    "Bước bài tiết Bilirubin liên hợp qua màng vi mật quản nhờ bơm MRP2",
    "BÀI TIẾT QUA VI MẬT QUẢN",
    "Mô tả cơ chế bài tiết chủ động của Bilirubin liên hợp qua màng vi mật quản bởi bơm vận chuyển MRP2?",
    [
        "<b>Bơm MRP2 (ABCC2) —</b> Là protein vận chuyển gắn màng vi mật quản của tế bào gan, thuộc họ bơm vận chuyển mang hộp gắn ATP (ABC Transporter).",
        "<b>Vận chuyển chủ động chống gradient nồng độ —</b> Sử dụng năng lượng từ sự thủy phân ATP để bơm tích cực Bilirubin diglucuronid từ bào tương vào trong lòng các vi mật quản (bile canaliculi).",
        "<b>Gradient nồng độ cực lớn —</b> Nồng độ Bilirubin trong dịch mật cao gấp hàng trăm lần nồng độ trong bào tương tế bào gan.",
        "<b>Ý nghĩa bệnh học —</b> Đột biến gen ABCC2 làm bất hoạt bơm MRP2 dẫn đến bệnh di truyền HỘI CHỨNG DUBIN-JOHNSON, khiến Bilirubin trực tiếp bị ứ đọng trào ngược vào máu."
    ],
    "Bơm MRP2 không chỉ bài tiết bilirubin diglucuronid mà còn tham gia bài xuất nhiều chất chuyển hóa liên hợp glucuronid và glutathion của thuốc ra dịch mật."
))

cards.append(make_card(
    "HS09-B4-11",
    "MRP2 là bước giới hạn tốc độ thanh thải Bilirubin tại gan",
    "ĐỘNG HỌC THANH THẢI BILIRUBIN",
    "Giải thích vì sao bước bài tiết qua màng vi mật quản là bước giới hạn tốc độ và hậu quả khi tế bào gan bị tổn thương?",
    [
        "<b>Bước chậm nhất của quá trình thanh thải —</b> Tế bào gan có khả năng bắt giữ và liên hợp Bilirubin với công suất rất lớn; nhưng tốc độ bài tiết qua bơm MRP2 vào vi mật quản có giới hạn và là BƯỚC CHẬM NHẤT TRONG CHUỖI.",
        "<b>Tổn thương gan gây ứ trệ đầu tiên —</b> Khi tế bào gan bị tổn thương lan tỏa do virus, rượu, thuốc hoặc ứ mật, khâu bài tiết qua vi mật quản này luôn bị ẢNH HƯỞNG NẶNG NỀ VÀ SỚM NHẤT.",
        "<b>Trào ngược Bilirubin trực tiếp vào máu —</b> Bilirubin diglucuronid đã được tạo ra trong lưới nội chất không thể bơm ra mật, bị ứ đọng và trào ngược qua màng xoang mạch gan đi vào tuần hoàn chung.",
        "<b>Bức tranh tăng Bilirubin hỗn hợp —</b> Giải thích vì sao trong các bệnh viêm gan cấp và xơ gan, mặc dù tổn thương tế bào gan nhưng xét nghiệm máu luôn thấy nồng độ Bilirubin trực tiếp tăng rất cao."
    ],
    "Khả năng dự trữ của khâu liên hợp UGT1A1 lớn hơn khâu bài tiết MRP2 gấp nhiều lần; do đó khi tế bào gan suy yếu nhẹ, khâu bài tiết mật luôn bị quá tải trước tiên."
))

cards.append(make_card(
    "HS09-B4-12",
    "Con đường bài tiết phụ qua MRP3 khi có tắc mật",
    "BÀI TIẾT PHỤ QUA MRP3",
    "Mô tả cơ chế cứu hộ của chất vận chuyển MRP3 tại màng xoang tế bào gan khi đường mật bị tắc nghẽn?",
    [
        "<b>Vị trí chất vận chuyển MRP3 —</b> Định vị tại màng đáy xoang (basolateral membrane) của tế bào gan tiếp giáp với máu xoang gan.",
        "<b>Cảm ứng biểu hiện khi ứ mật —</b> Bình thường MRP3 biểu hiện mức độ thấp; khi áp lực đường mật tăng cao do tắc mật hoặc ứ đọng acid mật nội bào, gen mã hóa MRP3 được kích hoạt phiên mã mạnh mẽ.",
        "<b>Bơm Bilirubin trực tiếp ngược vào máu xoang —</b> MRP3 sử dụng ATP bơm tích cực Bilirubin diglucuronid từ tế bào gan ngược trở lại vào dòng máu xoang gan.",
        "<b>Lối thoát hiểm qua Thận —</b> Bilirubin trực tiếp hòa tan vào máu, được thận lọc và đào thải ra ngoài qua nước tiểu, giúp giải tỏa áp lực độc chất cho tế bào gan khỏi bị hoại tử do ứ đọng mật."
    ],
    "Cơ chế cứu hộ qua MRP3 biến thận thành 'cơ quan giải độc mật phụ' khi đường mật chính bị bế tắc hoàn toàn, biểu hiện qua dấu hiệu nước tiểu sẫm màu có sắc tố mật."
))

# ==============================================================================
# SECTION B5: CHU TRUYỀN TẠI RUỘT & CHU TRÌNH RUỘT - GAN CỦA UROBILINOGEN (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B5-01",
    "Dòng dịch mật đổ vào tá tràng và tính vô khuẩn đường mật",
    "CHUYỂN HÓA TẠI RUỘT",
    "Mô tả đường đi của Bilirubin liên hợp từ vi mật quản xuống ruột non và đặc điểm vi sinh học của dịch mật?",
    [
        "<b>Đường dẫn mật ngoài gan —</b> Bilirubin diglucuronid từ các vi mật quản gom vào các ống mật trong gan → Ống gan phải và trái → Ống gan chung → phối hợp với túi mật tạo Ống mật chủ.",
        "<b>Đổ vào Tá tràng qua cơ vòng Oddi —</b> Khi có thức ăn (đặc biệt chất béo) kích thích tiết hormon Cholecystokinin (CCK), cơ túi mật co bóp và cơ vòng Oddi giãn mở, tống xuất dịch mật vào khúc II tá tràng.",
        "<b>Tính vô khuẩn sinh lý —</b> Dịch mật trong đường mật và dịch tá tràng bình thường HOÀN TOÀN VÔ KHUẨN.",
        "<b>Chưa bị biến đổi ở ruột non trên —</b> Tại tá tràng và hỗng tràng, phân tử Bilirubin diglucuronid vẫn giữ nguyên cấu trúc liên hợp và di chuyển thụ động dọc theo lòng ruột non cùng với dưỡng trấp."
    ],
    "Nếu đường mật bị nhiễm trùng ngược dòng bởi vi khuẩn đường ruột (viêm đường mật cấp do sỏi), enzym β-glucuronidase vi khuẩn sẽ giải phóng bilirubin tự do ngay trong túi mật, kết hợp với canxi tạo sỏi mật sắc tố đen hoặc nâu."
))

cards.append(make_card(
    "HS09-B5-02",
    "Khử liên hợp bởi enzym β-Glucuronidase của vi khuẩn kỵ khí ruột",
    "CHUYỂN HÓA TẠI RUỘT",
    "Trình bày phản ứng khử liên hợp của Bilirubin diglucuronid tại đại tràng bởi hệ vi sinh vật đường ruột?",
    [
        "<b>Vị trí chuyển hóa —</b> Đoạn cuối hồi tràng và toàn bộ khung ĐẠI TRÀNG.",
        "<b>Hệ vi khuẩn kỵ khí phong phú —</b> Gặp gỡ hệ vi sinh vật đại tràng khổng lồ, chủ yếu là các chủng vi khuẩn kỵ khí như Bacteroides fragilis, Clostridium perfringens.",
        "<b>Enzym β-Glucuronidase vi khuẩn —</b> Các vi khuẩn này tiết ra enzym β-GLUCURONIDASE thủy phân bẻ gãy liên kết ester giữa acid glucuronic và bilirubin.",
        "<b>Giải phóng Bilirubin tự do —</b> Cắt bỏ hoàn toàn 2 gốc glucuronat, hoàn trả lại phân tử Bilirubin tự do không liên hợp trong lòng đại tràng để chuẩn bị cho chuỗi phản ứng khử tiếp theo."
    ],
    "Kháng sinh phổ rộng đường uống (như ciprofloxacin, amoxicillin/clavulanat) tiêu diệt hệ vi khuẩn đại tràng làm suy giảm phản ứng khử liên hợp, khiến bilirubin diglucuronid bị tống xuất nguyên vẹn ra phân."
))

cards.append(make_card(
    "HS09-B5-03",
    "Chuỗi phản ứng khử hydro hóa tạo Urobilinogen và Stercobilinogen",
    "CHUYỂN HÓA TẠI RUỘT",
    "Mô tả các bước khử hydro hóa liên tiếp của vi khuẩn biến đổi Bilirubin thành Urobilinogen không màu?",
    [
        "<b>Chuỗi phản ứng khử liên tiếp —</b> Các enzym khử của vi khuẩn kỵ khí bơm liên tục các nguyên tử hydro vào các cầu nối methenyl và các liên kết đôi của chuỗi tetrapyrrol.",
        "<b>Các sản phẩm trung gian —</b> Bilirubin (vàng cam) → Mesobilirubin → Mesobilirubinogen.",
        "<b>Tạo Urobilinogen và Stercobilinogen —</b> Tiếp tục khử hydro tạo thành hỗn hợp các hợp chất tetrapyrrol bão hòa không màu mang tên UROBILINOGEN và STERCOBILINOGEN.",
        "<b>Mất hoàn toàn màu sắc —</b> Do mất hệ thống liên kết đôi liên hợp dài, phân tử Urobilinogen và Stercobilinogen HOÀN TOÀN KHÔNG CÓ MÀU SẮC trong lòng ruột."
    ],
    "Urobilinogen là một nhóm gồm nhiều đồng phân lập thể tương đồng (chủ yếu là Urobilinogen, Mesobilirubinogen, và Stercobilinogen), đều có tính khử mạnh và dễ bị oxy hóa trở lại."
))

cards.append(make_card(
    "HS09-B5-04",
    "Sự tạo thành Stercobilin và nguồn gốc màu nâu của Phân",
    "SẮC TỐ PHÂN STERCOBILIN",
    "Giải thích nguồn gốc màu nâu đặc trưng của phân người bình thường và khối lượng đào thải mỗi ngày?",
    [
        "<b>Số phận 80 - 90% lượng sắc tố tại đại tràng —</b> Đại đa số lượng Stercobilinogen và Urobilinogen ở lại trong lòng đại tràng và di chuyển dần xuống trực tràng.",
        "<b>Phản ứng oxy hóa tự phát ngoài không khí —</b> Dưới tác động của oxy hòa tan và vi khuẩn đoạn xa, Stercobilinogen bị oxy hóa tách hydro biến thành STERCOBILIN.",
        "<b>Màu nâu sẫm đặc trưng —</b> Phân tử Stercobilin có màu nâu sẫm, chính là SẮC TỐ CỐT LÕI TẠO NÊN MÀU NÂU ĐẶC TRƯNG CỦA PHÂN NGƯỜI BÌNH THƯỜNG.",
        "<b>Khối lượng đào thải hằng ngày —</b> Mỗi ngày có khoảng 100 đến 250 mg Stercobilin được bài xuất ra ngoài theo phân."
    ],
    "Ở trẻ sơ sinh bú sữa mẹ trong vài ngày đầu, do chưa có hệ vi khuẩn đại tràng để tạo stercobilin, phân su và phân của trẻ có màu xanh lục hoặc vàng tươi của chính biliverdin và bilirubin."
))

cards.append(make_card(
    "HS09-B5-05",
    "Ý nghĩa lâm sàng của Dấu hiệu Phân bạc màu đất sét (Clay-Colored Stool)",
    "TRIỆU CHỨNG HỌC LÂM SÀNG",
    "Giải thích cơ chế bệnh sinh của dấu hiệu phân bạc màu như đất sét (phân cò) trong tắc mật cơ học?",
    [
        "<b>Tắc nghẽn lưu thông đường mật hoàn toàn —</b> Gặp trong u đầu tụy chèn ép ống mật chủ, ung thư biểu mô đường mật (Cholangiocarcinoma), sỏi kẹt ống mật chủ, hoặc teo đường mật bẩm sinh ở trẻ sơ sinh.",
        "<b>Không có Bilirubin xuống ruột —</b> Dòng dịch mật bị chặn đứng tuyệt đối, không có bất kỳ phân tử Bilirubin nào xuống được tá tràng và đại tràng.",
        "<b>Thiếu vắng hoàn toàn Stercobilin —</b> Vi khuẩn ruột không có cơ chất để tạo Stercobilinogen và Stercobilin.",
        "<b>Biểu hiện lâm sàng: Phân bạc màu —</b> Phân mất sạch màu nâu vàng, chuyển sang màu trắng đục, màu xám tro hoặc MÀU TRẮNG BẠC NHƯ ĐẤT SÉT (Clay-colored / Acholic stool); là dấu hiệu chỉ điểm vàng da sau gan tắc mật."
    ],
    "Dấu hiệu phân bạc màu như đất sét kết hợp với nước tiểu vàng sẫm như nước trà đặc và ngứa dữ dội là 'tam chứng vàng' kinh điển của hội chứng tắc mật cơ học ngoài gan."
))

cards.append(make_card(
    "HS09-B5-06",
    "Chu trình Ruột - Gan (Enterohepatic Circulation) của Urobilinogen",
    "CHU TRÌNH RUỘT - GAN",
    "Mô tả con đường tái hấp thu và số phận của Urobilinogen trong Chu trình Ruột - Gan?",
    [
        "<b>Tái hấp thu 10 - 20% tại đại tràng —</b> Khoảng 10 đến 20% lượng Urobilinogen sinh ra được niêm mạc đại tràng tái hấp thu thụ động vào hệ thống mao mạch mạc treo.",
        "<b>Theo tĩnh mạch cửa về Gan —</b> Dòng máu tĩnh mạch mạc treo đưa Urobilinogen hòa vào dòng máu của Tĩnh mạch cửa trở về gan.",
        "<b>Gan khỏe mạnh bắt giữ tái bài tiết (> 90%) —</b> Đại đa số lượng Urobilinogen này được các tế bào biểu mô gan khỏe mạnh bắt giữ triệt để và bài tiết trở lại vào dịch mật, khép kín Chu trình Ruột - Gan.",
        "<b>Ý nghĩa sinh lý —</b> Tái sử dụng và thanh thải tuần hoàn các sản phẩm thoái hóa của sắc tố mật mà không để lọt vào tuần hoàn hệ thống."
    ],
    "Chu trình ruột - gan của Urobilinogen hoạt động tương tự chu trình ruột - gan của acid mật, tạo nên dòng tuần hoàn liên tục giữa gan và ruột non."
))

cards.append(make_card(
    "HS09-B5-07",
    "Urobilinogen thoát tuần hoàn và Nguồn gốc màu vàng rơm của Nước tiểu",
    "SẮC TỐ NƯỚC TIỂU UROBILIN",
    "Giải thích vì sao nước tiểu bình thường có chứa một lượng vết Urobilinogen và nguồn gốc màu vàng rơm của nước tiểu?",
    [
        "<b>Thoát khỏi sự bắt giữ của gan (< 5 - 10%) —</b> Một lượng rất nhỏ Urobilinogen tái hấp thu thoát khỏi sự bắt giữ của gan, đi vào tĩnh mạch chủ dưới hòa vào đại tuần hoàn.",
        "<b>Lọc tự do qua cầu thận —</b> Do có kích thước phân tử nhỏ, không gắn chặt với protein và tan được trong nước, Urobilinogen được màng lọc cầu thận lọc tự do ra nước tiểu.",
        "<b>Khối lượng bài xuất sinh lý bình thường —</b> Rất nhỏ, chỉ khoảng dưới 4 mg/ngày (xét nghiệm que thử nước tiểu thường ở mức vết hoặc bình thường 0,2 - 1,0 Ehrlich units/dL).",
        "<b>Oxy hóa tạo Urobilin (Màu vàng rơm) —</b> Trong nước tiểu khi tiếp xúc với oxy không khí, Urobilinogen bị oxy hóa thành UROBILIN màu vàng; cùng với sắc tố Urochrome tạo nên MÀU VÀNG RƠM SINH LÝ CỦA NƯỚC TIỂU."
    ],
    "Urobilinogen trong nước tiểu là hoàn toàn sinh lý; sự biến mất hoàn toàn của Urobilinogen niệu (= 0) hoặc sự tăng vọt quá mức đều là các dấu hiệu bệnh lý."
))

cards.append(make_card(
    "HS09-B5-08",
    "Biến thiên Urobilinogen nước tiểu trong Hội chứng Tan máu (Trước gan)",
    "BỆNH HỌC LÂM SÀNG NƯỚC TIỂU",
    "Giải thích cơ chế giải thích vì sao Urobilinogen nước tiểu tăng rất cao trong khi Bilirubin nước tiểu lại âm tính ở bệnh nhân tan máu?",
    [
        "<b>Quá tải sản sinh Bilirubin —</b> Tan máu ồ ạt sản sinh lượng khổng lồ Bilirubin tự do đưa về gan liên hợp; gan tăng cường bài tiết lượng lớn Bilirubin xuống ruột non.",
        "<b>Tăng vọt tạo Urobilinogen tại ruột —</b> Vi khuẩn đại tràng chuyển hóa lượng sắc tố dồi dào này thành lượng khổng lồ Urobilinogen và Stercobilinogen (phân màu nâu rất đậm).",
        "<b>Chu trình ruột - gan bị quá tải —</b> Lượng Urobilinogen tái hấp thu vào tĩnh mạch cửa vượt quá công suất bắt giữ của gan, khiến lượng lớn Urobilinogen tràn vào máu đến thận.",
        "<b>Urobilinogen niệu tăng rất mạnh —</b> Nước tiểu có Urobilinogen tăng vọt (dương tính đậm).",
        "<b>Bilirubin nước tiểu ÂM TÍNH HOÀN TOÀN —</b> Do Bilirubin tăng trong máu là dạng gián tiếp kỵ nước gắn Albumin không lọc qua cầu thận; nước tiểu không có sắc tố mật."
    ],
    "Dấu hiệu 'Nước tiểu có Urobilinogen tăng cao nhưng Bilirubin âm tính' là bằng chứng thép chẩn đoán xác định vàng da trước gan do tan máu."
))

cards.append(make_card(
    "HS09-B5-09",
    "Biến thiên Urobilinogen nước tiểu trong Viêm gan tổn thương nhu mô",
    "BỆNH HỌC LÂM SÀNG NƯỚC TIỂU",
    "Phân tích sự biến thiên hai pha của Urobilinogen nước tiểu ở bệnh nhân Viêm gan virus cấp tính?",
    [
        "<b>Giai đoạn đầu tổn thương gan: Urobilinogen TĂNG CAO —</b> Dòng mật vẫn còn lưu thông xuống ruột tạo Urobilinogen bình thường; nhưng tế bào gan bị hoại tử suy giảm khả năng bắt giữ Urobilinogen tái hấp thu từ tĩnh mạch cửa, khiến Urobilinogen đi thẳng vào đại tuần hoàn đào thải qua nước tiểu tăng vọt.",
        "<b>Giai đoạn toàn phát ứ mật nặng: Urobilinogen CÓ THỂ GIẢM HOẶC BIẾN MẤT —</b> Phù nề tế bào gan chèn ép các vi mật quản gây tắc mật tại gan nặng nề; lượng mật xuống ruột giảm sút làm giảm sinh Urobilinogen tại ruột.",
        "<b>Giai đoạn hồi phục: Urobilinogen TĂNG TRỞ LẠI —</b> Khi vi mật quản thông thoáng trở lại, sắc tố mật lại xuống ruột tạo Urobilinogen tái hấp thu, sau đó giảm dần về bình thường khi tế bào gan hồi phục hoàn toàn chức năng bắt giữ.",
        "<b>Song hành với Bilirubin trực tiếp niệu —</b> Trong suốt các giai đoạn viêm gan, Bilirubin nước tiểu luôn DƯƠNG TÍNH làm nước tiểu sẫm màu."
    ],
    "Sự biến thiên hình sin của Urobilinogen niệu kết hợp với động học nồng độ men gan ALT giúp bác sĩ theo dõi chính xác các giai đoạn tiến triển và thoái lui của đợt viêm gan cấp."
))

cards.append(make_card(
    "HS09-B5-10",
    "Tác động của Kháng sinh phổ rộng đường ruột lên chuyển hóa sắc tố mật",
    "DƯỢC LÝ HÓA SINH RUỘT",
    "Giải thích hiện tượng thay đổi màu phân và biến mất Urobilinogen nước tiểu khi bệnh nhân dùng Kháng sinh phổ rộng đường uống?",
    [
        "<b>Tiêu diệt hệ vi sinh vật kỵ khí đại tràng —</b> Kháng sinh phổ rộng (như Neomycin, Ciprofloxacin, Metronidazol) tiêu diệt phần lớn vi khuẩn Clostridium, Bacteroides ở ruột.",
        "<b>Mất enzym β-Glucuronidase và Dehydrogenase vi khuẩn —</b> Không còn vi khuẩn thực hiện phản ứng khử liên hợp và hydro hóa Bilirubin.",
        "<b>Không tạo thành Urobilinogen và Stercobilinogen —</b> Quá trình tạo Urobilinogen tại đại tràng bị chặn đứng hoàn toàn.",
        "<b>Hậu quả kép —</b> 1) Phân mất màu nâu của Stercobilin, chuyển sang màu vàng tươi hoặc màu xanh lục của chính Bilirubin chưa chuyển hóa; 2) Không có Urobilinogen tái hấp thu nên Urobilinogen trong nước tiểu GIẢM SÚT HOẶC BIẾN MẤT HOÀN TOÀN (= 0)."
    ],
    "Khi xét nghiệm nước tiểu thấy Urobilinogen âm tính, bác sĩ cần khai thác kỹ tiền sử dùng kháng sinh đường ruột trước khi vội vã kết luận bệnh nhân bị tắc nghẽn đường mật cơ học."
))

# ==============================================================================
# SECTION B6: HỘI CHỨNG VÀNG DA: PHÂN BIỆT TRƯỚC GAN, TẠI GAN VÀ SAU GAN (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B6-01",
    "Định nghĩa Vàng da và Ngưỡng phát hiện tại Củng mạc mắt",
    "HỘI CHỨNG VÀNG DA",
    "Nêu định nghĩa Hội chứng Vàng da, các ngưỡng nồng độ Bilirubin máu và giải thích vì sao củng mạc mắt phát hiện sớm nhất?",
    [
        "<b>Định nghĩa Vàng da (Jaundice / Icterus) —</b> Tình trạng nhuộm màu vàng ở da, niêm mạc và củng mạc mắt do sự lắng đọng phân tử Bilirubin khi nồng độ Bilirubin máu tăng cao.",
        "<b>Nồng độ sinh lý bình thường —</b> Bilirubin toàn phần < 1,0 mg/dL (< 17 µmol/L); Bilirubin gián tiếp chiếm ưu thế (70 - 85%), Bilirubin trực tiếp chiếm 15 - 30%.",
        "<b>Vàng da dưới lâm sàng (Subclinical) —</b> Nồng độ Bilirubin từ 1,0 đến 2,0 mg/dL (17 - 34 µmol/L); mắt thường chưa nhìn thấy nhưng xét nghiệm sinh hóa đã phát hiện.",
        "<b>Vàng da lâm sàng rõ rệt —</b> Khi Bilirubin toàn phần vượt quá 2,0 - 2,5 mg/dL (> 34 - 43 µmol/L).",
        "<b>Củng mạc mắt phát hiện đầu tiên —</b> Củng mạc mắt (sclera) chứa hàm lượng rất cao protein ELASTIN; Elastin có ái lực liên kết hóa học đặc biệt cao với phân tử Bilirubin, làm củng mạc bắt màu vàng sớm nhất trước khi thấy vàng ở da."
    ],
    "Khám củng mạc mắt dưới ánh sáng tự nhiên ban ngày là kỹ năng lâm sàng chuẩn mực để phát hiện vàng da sớm nhất; không được khám dưới ánh sáng đèn vàng vì dễ bị sai lệch."
))

cards.append(make_card(
    "HS09-B6-02",
    "Vàng da Trước gan (Tan máu): Cơ chế bệnh sinh và Căn nguyên",
    "VÀNG DA TRƯỚC GAN",
    "Trình bày cơ chế bệnh sinh phân tử và kể tên 5 căn nguyên kinh điển của Hội chứng Vàng da Trước gan?",
    [
        "<b>Cơ chế bệnh sinh cốt lõi —</b> Tốc độ phá hủy hồng cầu ngoại mạch hoặc nội mạch tăng vọt ồ ạt, giải phóng lượng khổng lồ Hemoglobin vượt quá công suất tối đa của enzym UGT1A1 tại tế bào gan.",
        "<b>Căn nguyên 1: Nhiễm trùng —</b> Sốt rét ác tính (Plasmodium falciparum phá vỡ hồng cầu hàng loạt), nhiễm trùng huyết tan máu do Clostridium perfringens.",
        "<b>Căn nguyên 2: Miễn dịch —</b> Truyền nhầm nhóm máu hệ ABO, bất đồng nhóm máu yếu tố Rh mẹ - con, thiếu máu tan máu tự miễn (AIHA Coombs dương tính).",
        "<b>Căn nguyên 3: Thiếu hụt enzym hồng cầu —</b> Bệnh thiếu men G6PD (tan máu cấp khi dùng thuốc oxy hóa như Primaquin, Dapsone hoặc ăn đậu tằm Fava), thiếu men Pyruvat Kinase.",
        "<b>Căn nguyên 4 & 5: Bệnh lý huyết sắc tố và Màng hồng cầu —</b> Thalassemia thể nặng, Bệnh hồng cầu hình liềm (HbSS), Bệnh hồng cầu hình cầu di truyền (Hereditary Spherocytosis)."
    ],
    "Trong vàng da trước gan, tế bào gan và đường mật hoàn toàn khỏe mạnh bình thường; tình trạng vàng da hoàn toàn là hậu quả thụ động của sự quá tải nguyên liệu Hem thượng nguồn."
))

cards.append(make_card(
    "HS09-B6-03",
    "Bức tranh xét nghiệm sinh hóa đặc trưng của Vàng da Trước gan",
    "VÀNG DA TRƯỚC GAN",
    "Phân tích bức tranh sinh hóa 5 chỉ số đặc trưng của Vàng da Trước gan (Bilirubin máu, Bilirubin niệu, Urobilinogen, Men gan)?",
    [
        "<b>1. Bilirubin máu —</b> TĂNG CAO CHỦ YẾU LÀ BILIRUBIN GIÁN TIẾP (Tự do), chiếm ưu thế tuyệt đối > 80% tổng lượng Bilirubin; Bilirubin trực tiếp bình thường hoặc tăng rất nhẹ.",
        "<b>2. Bilirubin nước tiểu (Sắc tố mật) —</b> HOÀN TOÀN ÂM TÍNH (Nước tiểu không có sắc tố mật, bọt nước tiểu màu trắng), do Bilirubin gián tiếp kỵ nước gắn chặt Albumin không lọc qua màng lọc cầu thận.",
        "<b>3. Urobilinogen nước tiểu —</b> TĂNG RẤT MẠNH (Dương tính đậm), do chu trình ruột - gan bị quá tải bởi lượng lớn sắc tố xuống ruột.",
        "<b>4. Màu sắc Phân —</b> PHÂN CÓ MÀU SẪM HOẶC NÂU ĐẬM do tăng đào thải Stercobilin.",
        "<b>5. Enzym Gan (ALT, AST, ALP, GGT) —</b> HOÀN TOÀN BÌNH THƯỜNG; kèm theo các dấu hiệu tan máu: Hemoglobin máu giảm, Hồng cầu lưới tăng vọt, Haptoglobin huyết tương sụt giảm về 0, LDH máu tăng cao."
    ],
    "Thuật ngữ cổ điển 'Vàng da không có sắc tố mật niệu' (Acholuric Jaundice) là tên gọi chuẩn xác mô tả vàng da do tan máu."
))

cards.append(make_card(
    "HS09-B6-04",
    "Vàng da Tại gan (Tổn thương nhu mô): Cơ chế bệnh sinh và Căn nguyên",
    "VÀNG DA TẠI GAN",
    "Trình bày cơ chế bệnh sinh phân tử và kể tên các căn nguyên phổ biến của Hội chứng Vàng da Tại gan?",
    [
        "<b>Cơ chế bệnh sinh phức hợp —</b> Tế bào gan bị hoại tử hoặc suy giảm chức năng, gây suy giảm đồng thời cả 3 khâu: Giảm bắt giữ Bilirubin, Giảm hoạt tính liên hợp UGT1A1, và Phù nề vi mật quản làm ứ trệ bài tiết khiến Bilirubin trực tiếp trào ngược vào máu xoang.",
        "<b>Căn nguyên Viêm gan virus cấp —</b> Virus viêm gan A, B, C, D, E; Epstein-Barr Virus (EBV), Cytomegalovirus (CMV).",
        "<b>Căn nguyên Ngộ độc thuốc và Hóa chất —</b> Ngộ độc Paracetamol liều cao làm cạn kiệt Glutathion, ngộ độc nấm độc tán trắng Amanita phalloides, thuốc chống lao (Rifampicin, Isoniazid), rượu.",
        "<b>Căn nguyên Tự miễn và Chuyển hóa —</b> Viêm gan tự miễn, Viêm gan thoái hóa mỡ do rượu (ASH), Viêm gan thoái hóa mỡ không do rượu (MASH), Bệnh ứ đồng Wilson, Bệnh ứ sắt Hemochromatosis.",
        "<b>Xơ gan giai đoạn mất bù —</b> Khối lượng tế bào gan lành suy giảm nghiêm trọng."
    ],
    "Vàng da tại gan là một bức tranh hỗn hợp đan xen: vừa có khiếm khuyết liên hợp của tế bào gan, vừa có hiện tượng tắc mật vi thể nội sinh do hoại tử và phù nề nhu mô."
))

cards.append(make_card(
    "HS09-B6-05",
    "Bức tranh xét nghiệm sinh hóa đặc trưng của Vàng da Tại gan",
    "VÀNG DA TẠI GAN",
    "Phân tích bức tranh xét nghiệm sinh hóa đặc trưng của Vàng da Tại gan (Bilirubin, Men gan hoại tử, Sắc tố mật niệu)?",
    [
        "<b>1. Bilirubin máu —</b> TĂNG HỖN HỢP CẢ BILIRUBIN TRỰC TIẾP VÀ GIÁN TIẾP; tỷ lệ Bilirubin trực tiếp thường dao động từ 30% đến 60% tổng lượng.",
        "<b>2. Enzym hoại tử tế bào gan (ALT, AST) —</b> TĂNG RẤT CAO, thường tăng gấp > 10 đến 20 lần giới hạn trên bình thường (> 1000 U/L trong viêm gan virus cấp hoặc ngộ độc paracetamol).",
        "<b>3. Bilirubin nước tiểu (Sắc tố mật) —</b> DƯƠNG TÍNH (Nước tiểu có màu vàng sẫm bọt vàng), do Bilirubin liên hợp trào ngược vào máu lọc được qua cầu thận.",
        "<b>4. Urobilinogen nước tiểu —</b> BIẾN THIÊN THEO GIAI ĐOẠN: Giai đoạn đầu tăng cao do gan giảm bắt giữ; giai đoạn ứ mật nặng có thể giảm.",
        "<b>5. Màu sắc Phân —</b> Nhạt màu hơn bình thường nhưng ít khi bạc màu hoàn toàn.",
        "<b>6. Rối loạn chức năng tổng hợp —</b> Giảm Albumin máu, Tỷ lệ Prothrombin (PT%) giảm kéo dài INR (không hồi phục hoàn toàn khi tiêm bắp Vitamin K)."
    ],
    "Sự kết hợp giữa 'Men gan ALT/AST tăng vọt hàng ngàn' và 'Bilirubin tăng hỗn hợp' là dấu ấn đặc trưng giúp nhận diện ngay tổn thương cấp tính tại nhu mô gan."
))

cards.append(make_card(
    "HS09-B6-06",
    "Vàng da Sau gan (Tắc mật cơ học): Cơ chế bệnh sinh và Căn nguyên",
    "VÀNG DA SAU GAN",
    "Trình bày cơ chế bệnh sinh và kể tên 4 căn nguyên ngoại khoa kinh điển của Hội chứng Vàng da Sau gan?",
    [
        "<b>Cơ chế bệnh sinh cốt lõi —</b> Tắc nghẽn cơ học hoàn toàn hoặc không hoàn toàn lưu thông của dòng dịch mật trên hệ thống đường mật ngoài gan (ống gan chung, ống mật chủ) hoặc ngã ba đường mật.",
        "<b>Áp lực đường mật tăng cao trào ngược —</b> Áp lực trong đường mật tăng vọt, phá vỡ các mối nối vòng kín của vi mật quản; Bilirubin diglucuronid đã liên hợp hoàn chỉnh bị ứ đọng và trào ngược ồ ạt qua màng xoang mạch gan đi vào hệ tuần hoàn.",
        "<b>Căn nguyên Sỏi ống mật chủ (Choledocholithiasis) —</b> Sỏi từ túi mật rơi xuống hoặc sỏi hình thành nguyên phát tại ống mật chủ gây tắc mật kèm nhiễm trùng đường mật (Tam chứng Charcot: Đau bụng - Sốt - Vàng da).",
        "<b>Căn nguyên U đầu tụy (Pancreatic Head Adenocarcinoma) —</b> Khối u chèn ép từ từ vào đoạn ống mật chủ trong tụy gây vàng da tắc mật tăng dần không đau kèm túi mật căng to (Định luật Courvoisier).",
        "<b>Căn nguyên Ung thư đường mật (Cholangiocarcinoma) —</b> Khối u tế bào biểu mô đường mật, đặc biệt u ngã ba rốn gan (U Klatskin).",
        "<b>Teo đường mật bẩm sinh (Biliary Atresia) —</b> Tắc nghẽn xơ hóa đường mật tiến triển ở trẻ sơ sinh từ 2 - 6 tuần tuổi."
    ],
    "Vàng da sau gan là một cấp cứu ngoại khoa tiêu hóa: việc giải tỏa bế tắc dòng mật (bằng nội soi mật tụy ngược dòng ERCP, đặt stent hoặc phẫu thuật) là biện pháp điều trị triệt để duy nhất."
))

cards.append(make_card(
    "HS09-B6-07",
    "Bức tranh xét nghiệm sinh hóa đặc trưng của Vàng da Sau gan",
    "VÀNG DA SAU GAN",
    "Phân tích bức tranh xét nghiệm sinh hóa đặc trưng của Vàng da Sau gan (Bilirubin, Sắc tố mật niệu, Urobilinogen, Phân bạc màu)?",
    [
        "<b>1. Bilirubin máu —</b> TĂNG RẤT CAO, TRONG ĐÓ BILIRUBIN TRỰC TIẾP TĂNG VỌT ÁP ĐẢO (thường chiếm > 50 - 60%, có thể đạt 70 - 80% tổng lượng Bilirubin; nồng độ có thể lên tới 20 - 30 mg/dL).",
        "<b>2. Bilirubin nước tiểu (Sắc tố mật) —</b> DƯƠNG TÍNH RẤT ĐẬM (Nước tiểu có màu như nước trà đặc, nước vối, lắc lên bọt có màu vàng kim lâu tan).",
        "<b>3. Urobilinogen nước tiểu —</b> HOÀN TOÀN BIẾN MẤT (= 0 / Âm tính tuyệt đối) trong tắc mật cơ học hoàn toàn, do Bilirubin không xuống được đại tràng để tạo Urobilinogen.",
        "<b>4. Màu sắc Phân —</b> PHÂN BẠC MÀU TRẮNG NHƯ ĐẤT SÉT (Clay-colored / Phân cò) do hoàn toàn thiếu vắng sắc tố Stercobilin.",
        "<b>5. Enzym Ứ mật (ALP, GGT) —</b> TĂNG RẤT CAO ƯU THẾ VƯỢT TRỘI (> 3 - 5 lần giới hạn trên); ALT/AST chỉ bình thường hoặc tăng nhẹ thứ phát giai đoạn đầu."
    ],
    "Cặp đôi dấu hiệu 'Bilirubin trực tiếp niệu dương tính đậm + Urobilinogen niệu âm tính tuyệt đối (= 0)' kết hợp phân bạc màu đất sét là bằng chứng chắc chắn 100% của tắc mật cơ học hoàn toàn."
))

cards.append(make_card(
    "HS09-B6-08",
    "Đặc tính enzym Ứ mật (ALP và GGT) trong Vàng da Sau gan",
    "ENZYM Ứ MẬT LÂM SÀNG",
    "Giải thích cơ chế sinh hóa giải thích vì sao Phosphatase kiềm (ALP) và GGT tăng rất cao trong tắc mật?",
    [
        "<b>Định vị màng tế bào biểu mô ống mật —</b> Phosphatase kiềm (ALP) và Gamma-Glutamyl Transferase (GGT) là các enzym gắn trên màng đỉnh của tế bào biểu mô đường mật và màng vi mật quản.",
        "<b>Cơ chế cảm ứng tổng hợp bởi Acid mật —</b> Sự ứ đọng dịch mật làm nồng độ muối mật và acid mật nội bào tăng cao; acid mật kích hoạt sự phiên mã và tổng hợp mới enzym ALP tại tế bào biểu mô đường mật.",
        "<b>Tác dụng tẩy rửa của Muối mật hòa tan enzym —</b> Hoạt tính diện hoạt của muối mật làm bong và hòa tan các phân tử enzym ALP và GGT từ màng tế bào vào dòng dịch mật, sau đó trào ngược vào máu xoang gan làm nồng độ huyết thanh tăng vọt.",
        "<b>Phân biệt nguồn gốc ALP bằng GGT —</b> ALP có mặt ở cả Xương (nguyên bào xương), Ruột và Nhau thai; nếu ALP tăng kết hợp GGT TĂNG CAO khẳng định 100% ALP CÓ NGUỒN GỐC TỪ GAN MẬT (nếu ALP tăng mà GGT bình thường gợi ý bệnh lý xương như còi xương, bệnh Paget xương)."
    ],
    "Tỷ lệ tăng ưu thế của ALP/GGT so với ALT/AST (R value < 2) là tiêu chuẩn chuẩn quốc tế để phân loại tổn thương gan dạng ứ mật (Cholestatic pattern)."
))

cards.append(make_card(
    "HS09-B6-09",
    "Cơ chế triệu chứng Ngứa ngoài da dữ dội (Pruritus) trong Tắc mật",
    "TRIỆU CHỨNG HỌC LÂM SÀNG",
    "Giải thích cơ chế phân tử của triệu chứng Ngứa dữ dội ngoài da ở bệnh nhân tắc mật?",
    [
        "<b>Không phải do Bilirubin —</b> Bản thân phân tử Bilirubin không gây ngứa; triệu chứng ngứa hoàn toàn do SỰ Ứ ĐỌNG CỦA CÁC CHẤT KHÁC TRONG DỊCH MẬT trào ngược vào máu.",
        "<b>Vai trò của Muối mật và Acid mật —</b> Nồng độ acid mật huyết thanh tăng cao (tăng gấp hàng chục lần), lắng đọng dưới lớp biểu bì da.",
        "<b>Kích hoạt thụ thể ngứa TGR5 —</b> Acid mật gắn và kích hoạt thụ thể gắn protein G đặc hiệu mang tên TGR5 (GPBAR1) biểu hiện trên các đầu tận cùng sợi thần kinh cảm giác C hướng tâm tại da.",
        "<b>Vai trò của Autotaxin và Acid Lysophosphatidic (LPA) —</b> Ứ mật kích thích tăng enzym Autotaxin chuyển hóa lipid màng tạo LPA; LPA kích hoạt các thụ thể thần kinh nơ-ron gây cảm giác NGỨA DỮ DỘI, DAI DẲNG KHÔNG ĐÁP ỨNG VỚI THUỐC KHÁNG HISTAMIN.",
        "<b>Điều trị đặc hiệu —</b> Sử dụng Cholestyramine (nhựa trao đổi anion gắn bẫy acid mật trong lòng ruột tống xuất ra phân), Rifampicin (cảm ứng enzym chuyển hóa acid mật) hoặc thuốc ức chế vận chuyển acid mật IBAT."
    ],
    "Bệnh nhân ngứa do tắc mật thường có các vết cào gãi rách da chằng chịt khắp người, ngứa tăng nhiều về đêm làm mất ngủ suy nhược trầm trọng."
))

cards.append(make_card(
    "HS09-B6-10",
    "Rối loạn đông máu do kém hấp thu Vitamin K trong tắc mật kéo dài",
    "HÓA SINH DINH DƯỠNG",
    "Phân tích cơ chế suy giảm đông máu do kém hấp thu Vitamin K ở bệnh nhân tắc mật kéo dài?",
    [
        "<b>Vai trò của Muối mật trong hấp thu lipid —</b> Muối mật là chất nhũ hóa lipid thiết yếu; tạo các hạt micelle hòa tan để giúp ruột non hấp thu các chất béo và CÁC VITAMIN TAN TRONG DẦU (A, D, E, K).",
        "<b>Mất muối mật tại ruột —</b> Tắc mật cơ học kéo dài làm dịch mật không xuống được ruột non, gây hội chứng KÉM HẤP THU CHẤT BÉO (biểu hiện phân mỡ Steatorrhea).",
        "<b>Thiếu hụt Vitamin K cơ thể —</b> Không hấp thu được Vitamin K từ thức ăn và vi khuẩn ruột, gây cạn kiệt lượng Vitamin K dự trữ tại gan sau vài tuần.",
        "<b>Mất phản ứng Carboxyl hóa các yếu tố đông máu —</b> Tế bào gan thiếu Vitamin K không thể thực hiện phản ứng γ-carboxyl hóa gốc Glutamat trên các yếu tố đông máu II (Prothrombin), VII, IX, X và Protein C, S.",
        "<b>Kéo dài thời gian Prothrombin (PT/INR) —</b> Tỷ lệ Prothrombin (PT%) sụt giảm nặng nề, INR tăng cao, bệnh nhân có nguy cơ xuất huyết dưới da, chảy máu chân răng và xuất huyết nội khoa đe dọa tính mạng khi phẫu thuật."
    ],
    "Cần phân biệt rõ: ở bệnh nhân tắc mật giai đoạn sớm, tế bào gan vẫn còn khả năng tổng hợp protein rất tốt; sự giảm đông máu hoàn toàn chỉ do thiếu hụt co-factor Vitamin K ngoại sinh."
))

cards.append(make_card(
    "HS09-B6-11",
    "Nghiệm pháp Kohler (Test Vitamin K) phân biệt Tắc mật vs. Suy gan",
    "NGHIỆM PHÁP KOHLER",
    "Trình bày nguyên lý và giá trị chẩn đoán của Nghiệm pháp Kohler (Test tiêm Vitamin K)?",
    [
        "<b>Quy trình thực hiện —</b> Tiêm bắp Vitamin K1 (Phytomenadione) liều 10 mg mỗi ngày liên tục trong 3 ngày; xét nghiệm kiểm tra lại Tỷ lệ Prothrombin (PT%) sau 24 đến 72 giờ.",
        "<b>Trường hợp 1: Tắc mật cơ học (Chức năng gan còn tốt) —</b> Khi tiêm bắp, Vitamin K đi thẳng vào tuần hoàn đến tế bào gan mà không cần qua sự hấp thu của ruột và muối mật; tế bào gan khỏe mạnh lập tức sử dụng lượng vitamin K này để tổng hợp yếu tố đông máu → TỶ LỆ PROTHROMBIN HỒI PHỤC NGOẠN MỤC (PT% tăng thêm > 30% so với ban đầu) → NGHIỆM PHÁP KOHLER DƯƠNG TÍNH.",
        "<b>Trường hợp 2: Suy tế bào gan nặng (Xơ gan mất bù / Viêm gan bùng phát) —</b> Bản thân bộ máy tế bào gan đã bị hủy hoại cạn kiệt, không còn khả năng sinh tổng hợp protein đông máu dù được cung cấp dồi dào vitamin K → TỶ LỆ PROTHROMBIN HOÀN TOÀN KHÔNG CẢI THIỆN → NGHIỆM PHÁP KOHLER ÂM TÍNH.",
        "<b>Ý nghĩa lâm sàng —</b> Nghiệm pháp đơn giản, an toàn và kinh điển giúp phân biệt dứt khoát giữa rối loạn đông máu do tắc mật kém hấp thu với suy tế bào gan hoại tử nặng."
    ],
    "Nghiệm pháp Kohler còn đóng vai trò điều trị chuẩn bị tiền phẫu bắt buộc: tiêm bù vitamin K trước khi phẫu thuật lấy sỏi hoặc mổ u tụy giúp hồi phục đông máu bình thường, tránh biến chứng chảy máu ồ ạt trong mổ."
))

cards.append(make_card(
    "HS09-B6-12",
    "Khái niệm Delta-Bilirubin (Biliprotein) trong Vàng da tắc mật kéo dài",
    "DELTA-BILIRUBIN",
    "Định nghĩa Delta-Bilirubin (Biliprotein) và giải thích hiện tượng vàng da tồn tại kéo dài sau khi đã giải quyết tắc mật?",
    [
        "<b>Bản chất Delta-Bilirubin (δ-Bilirubin / Biliprotein) —</b> Là phân tử Bilirubin liên hợp (Bilirubin diglucuronid) LIÊN KẾT CỘNG HÓA TRỊ BỀN VỮNG VỚI PHÂN TỬ ALBUMIN huyết thanh.",
        "<b>Cơ chế hình thành phi enzym —</b> Chỉ hình thành khi có tình trạng tăng Bilirubin trực tiếp máu kéo dài (vàng da tắc mật mạn tính hoặc viêm gan nặng); liên kết este giữa nhóm glucuronat và gốc lysin của albumin tự phát chuyển vị tạo liên kết amide cộng hóa trị vĩnh viễn.",
        "<b>Thời gian bán hủy bằng thời gian bán hủy Albumin —</b> Delta-Bilirubin KHÔNG THỂ LỌC QUA CẦU THẬN và không bài tiết qua mật; nó chỉ bị phân hủy cùng với sự thoái hóa tự nhiên của phân tử Albumin mang nó (thời gian bán hủy t1/2 kéo dài tới 14 - 21 NGÀY).",
        "<b>Hiện tượng lâm sàng 'Vàng da chậm biến mất' —</b> Sau khi phẫu thuật lấy sỏi thành công, nước tiểu đã hết sắc tố mật và enzym gan đã hồi phục, nhưng bệnh nhân VẪN CÒN VÀNG DA VÀ BILIRUBIN MÁU VẪN CÒN CAO TRONG SUỐT 2 - 3 TUẦN TIẾP THEO do Delta-Bilirubin tồn lưu."
    ],
    "Bác sĩ cần nắm vững cơ chế của Delta-Bilirubin để tránh lo lắng không cần thiết hoặc chỉ định nội soi can thiệp lại khi thấy vàng da chậm thoái lui sau phẫu thuật giải áp đường mật."
))

# ==============================================================================
# SECTION B7: CÁC HỘI CHỨNG VÀNG DA DI TRUYỀN & VÀNG DA SƠ SINH (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-B7-01",
    "Hội chứng Gilbert: Đột biến promoter hộp TATA của gen UGT1A1",
    "HỘI CHỨNG GILBERT",
    "Trình bày tần suất, bản chất đột biến di truyền và mức độ suy giảm hoạt tính enzym trong Hội chứng Gilbert?",
    [
        "<b>Tần suất rất phổ biến —</b> Chiếm khoảng 5% đến 10% dân số nói chung; di truyền theo tính trạng lặn trên nhiễm sắc thể thường.",
        "<b>Đột biến vùng promoter hộp TATA —</b> Phổ biến nhất là đột biến chèn thêm 2 cặp base dinucleotid (TA) vào vùng promoter của gen UGT1A1: kiểu gen bình thường mang 6 đoạn lặp [(TA)6TAA], kiểu gen Gilbert mang 7 đoạn lặp [(TA)7TAA] (ký hiệu alen UGT1A1*28).",
        "<b>Giảm hiệu quả gắn yếu tố phiên mã —</b> Sự kéo dài hộp TATA làm cản trở yếu tố phiên mã TFIID liên kết, dẫn đến giảm tốc độ phiên mã gen.",
        "<b>Suy giảm 60 - 70% hoạt tính enzym —</b> Hoạt tính của enzym UGT1A1 trong tế bào gan chỉ còn khoảng 30% so với người bình thường, làm giảm khả năng liên hợp khi có tải lượng bilirubin tăng."
    ],
    "Hội chứng Gilbert hoàn toàn không phải là một bệnh lý nguy hiểm mà chỉ là một biến thể di truyền lành tính của chuyển hóa; người mang alen Gilbert thậm chí còn có tỷ lệ mắc bệnh tim mạch xơ vữa thấp hơn nhờ tác dụng chống oxy hóa nhẹ của bilirubin."
))

cards.append(make_card(
    "HS09-B7-02",
    "Biểu hiện lâm sàng và Yếu tố kích hoạt cơn vàng da trong Hội chứng Gilbert",
    "HỘI CHỨNG GILBERT",
    "Mô tả đặc điểm lâm sàng, các yếu tố kích hoạt và nguyên tắc xử trí Hội chứng Gilbert?",
    [
        "<b>Đặc điểm lâm sàng —</b> Vàng da nhẹ, thoáng qua, lành tính hoàn toàn; nồng độ Bilirubin gián tiếp dao động từ 1,5 đến 3,0 mg/dL (hiếm khi vượt quá 4 - 5 mg/dL).",
        "<b>Các yếu tố kích hoạt cơn vàng da —</b> Cơn vàng mắt xuất hiện rõ khi có các kích thích: NHỊN ĐÓI (Fasting), ăn kiêng giảm cân đột ngột, gắng sức thể thao quá mức, stress tâm lý căng thẳng, mất ngủ, sốt nhiễm trùng, mất nước hoặc uống rượu.",
        "<b>Cơ chế cơn khi nhịn đói —</b> Nhịn đói làm tăng acid béo tự do trong máu cạnh tranh gắn albumin và cạnh tranh chất vận chuyển OATP tại gan, đồng thời giảm cơ chất UDPGA nội bào.",
        "<b>Các xét nghiệm hoàn toàn bình thường —</b> Men gan ALT, AST, ALP bình thường; không có tan máu (Hb, hồng cầu lưới, haptoglobin bình thường); mô học gan hoàn toàn bình thường.",
        "<b>Xử trí lâm sàng —</b> TUYỆT ĐỐI KHÔNG CẦN BẤT KỲ THUỐC HAY CAN THIỆP ĐIỀU TRỊ NÀO; chỉ cần giải thích trấn an để bệnh nhân và gia đình không hoang mang lo lắng."
    ],
    "Test nhịn đói (Fasting test): Cho bệnh nhân nhịn đói chỉ ăn 400 kcal/ngày trong 48 giờ; nồng độ Bilirubin gián tiếp trong máu sẽ tăng vọt gấp đôi, là nghiệm pháp cổ điển giúp khẳng định chẩn đoán Gilbert."
))

cards.append(make_card(
    "HS09-B7-03",
    "Hội chứng Crigler-Najjar Type I (CN-I): Mất hoàn toàn hoạt tính UGT1A1",
    "HỘI CHỨNG CRIGLER-NAJJAR",
    "Trình bày cơ chế di truyền, mức độ tăng Bilirubin và nguy cơ tử vong trong Hội chứng Crigler-Najjar Type I?",
    [
        "<b>Đột biến mất hoàn toàn chức năng —</b> Di truyền lặn trên NST thường, do đột biến dịch khung, xóa đoạn hoặc đột biến vô nghĩa tạo codon kết thúc sớm trên gen UGT1A1.",
        "<b>Hoạt tính enzym bằng 0% —</b> Tế bào gan hoàn toàn mất 100% hoạt tính enzym UGT1A1, không tổng hợp được bất kỳ phân tử Bilirubin liên hợp nào.",
        "<b>Tăng Bilirubin gián tiếp cực kỳ khủng khiếp —</b> Xuất hiện ngay từ những ngày đầu sau sinh; nồng độ Bilirubin gián tiếp trong máu tăng vọt từ 20 đến 45 mg/dL (340 - 760 µmol/L).",
        "<b>HOÀN TOÀN KHÔNG ĐÁP ỨNG PHENOBARBITAL —</b> Do không có phân tử enzym nào được tạo ra, thuốc cảm ứng phiên mã Phenobarbital hoàn toàn không có tác dụng hạ bilirubin máu.",
        "<b>Nguy cơ tử vong do Vàng da nhân não —</b> Trẻ sơ sinh có nguy cơ tử vong rất sớm do biến chứng Kernicterus; phương pháp cứu sống duy nhất là chiếu đèn quang trị liệu 12 - 18 giờ/ngày để chờ GHÉP GAN (Liver Transplantation)."
    ],
    "Ghép gan là biện pháp điều trị triệt để dứt điểm duy nhất cho bệnh nhân Crigler-Najjar Type I, cung cấp tế bào gan mang enzym UGT1A1 bình thường giúp cứu sống trẻ."
))

cards.append(make_card(
    "HS09-B7-04",
    "Hội chứng Crigler-Najjar Type II (Hội chứng Arias) và Đáp ứng Phenobarbital",
    "HỘI CHỨNG CRIGLER-NAJJAR",
    "So sánh Hội chứng Crigler-Najjar Type II với Type I và giải thích cơ chế test đáp ứng với Phenobarbital?",
    [
        "<b>Hoạt tính enzym còn sót lại (< 10%) —</b> Đột biến điểm sai nghĩa trên gen UGT1A1 làm enzym bị suy giảm nghiêm trọng nhưng vẫn giữ lại được một phần nhỏ hoạt tính (< 10% mức bình thường).",
        "<b>Nồng độ Bilirubin máu trung bình —</b> Bilirubin gián tiếp dao động từ 6 đến 20 mg/dL (100 - 340 µmol/L); trẻ thường sống sót qua tuổi trưởng thành mà không bị vàng da nhân nếu không có biến cố stress nặng.",
        "<b>ĐÁP ỨNG NGOẠN MỤC VỚI PHENOBARBITAL —</b> Thuốc ngủ Phenobarbital gắn vào thụ thể nhân CAR (Constitutive Androstane Receptor), kích hoạt mạnh mẽ sự phiên mã gen UGT1A1.",
        "<b>Hạ > 25 - 30% Bilirubin máu —</b> Sau vài ngày dùng Phenobarbital, hoạt tính enzym còn sót lại được nhân lên gấp bội, làm nồng độ Bilirubin máu sụt giảm mạnh trên 25 - 30%.",
        "<b>Test phân biệt dứt khoát Type I vs Type II —</b> Không đáp ứng với Phenobarbital = Type I; đáp ứng giảm mạnh Bilirubin = Type II (Hội chứng Arias)."
    ],
    "Bệnh nhân Crigler-Najjar Type II có thể duy trì cuộc sống tương đối bình thường bằng cách sử dụng Phenobarbital liều thấp duy trì kết hợp tránh các stress."
))

cards.append(make_card(
    "HS09-B7-05",
    "Hội chứng Dubin-Johnson: Đột biến bơm bài tiết MRP2 và Dấu hiệu Gan đen",
    "HỘI CHỨNG DUBIN-JOHNSON",
    "Trình bày cơ chế bệnh sinh, hình thái mô học Gan đen và rối loạn Coproporphyrin trong Hội chứng Dubin-Johnson?",
    [
        "<b>Đột biến gen ABCC2 —</b> Di truyền lặn trên NST thường; gây đột biến mất chức năng protein vận chuyển bơm màng vi mật quản MRP2 (ABCC2).",
        "<b>Tê liệt khâu bài tiết vi mật quản —</b> Tế bào gan liên hợp Bilirubin diglucuronid hoàn toàn bình thường nhưng không thể bơm được sắc tố vào vi mật quản; Bilirubin trực tiếp trào ngược vào máu làm TĂNG BILIRUBIN TRỰC TIẾP MẠN TÍNH (2 - 5 mg/dL), nước tiểu có sắc tố mật.",
        "<b>Dấu hiệu mô học kinh điển: GAN ĐEN TUYỀN (Black Liver) —</b> Khi quan sát đại thể nội soi hoặc sinh thiết, nhu mô gan có màu đen tuyền như than đá; do sự ứ đọng một loại sắc tố hạt màu nâu đen (melanin-like pigment) tích tụ trong lysosome tế bào gan (do các chất chuyển hóa epinephrine không bài tiết được qua MRP2).",
        "<b>Đảo lộn tỷ lệ Coproporphyrin nước tiểu —</b> Tổng lượng coproporphyrin niệu bình thường, nhưng tỷ lệ COPROPORPHYRIN I TĂNG VỌT CHIẾM > 80% (bình thường Coproporphyrin III chiếm ưu thế 75%).",
        "<b>Tiên lượng lành tính —</b> Tuổi thọ hoàn toàn bình thường, không tiến triển xơ gan."
    ],
    "Dấu hiệu gan đen tuyền trên hình ảnh đại thể khi mổ ổ bụng là hình ảnh gây ấn tượng sâu sắc nhất của Hội chứng Dubin-Johnson."
))

cards.append(make_card(
    "HS09-B7-06",
    "Hội chứng Rotor: Đột biến protein OATP và phân biệt với Dubin-Johnson",
    "HỘI CHỨNG ROTOR",
    "Trình bày cơ chế di truyền của Hội chứng Rotor và lập bảng so sánh phân biệt giữa Dubin-Johnson và Rotor?",
    [
        "<b>Đột biến kép gen OATP —</b> Di truyền lặn trên NST thường; do đột biến đồng hợp tử làm bất hoạt đồng thời cả 2 gen SLCO1B1 và SLCO1B3 mã hóa protein vận chuyển bắt giữ anion hữu cơ OATP1B1 và OATP1B3 tại màng xoang gan.",
        "<b>Cơ chế bế tắc bắt giữ —</b> Gan không thể bắt giữ hiệu quả các sắc tố mật để tái hấp thu, khiến Bilirubin liên hợp bị tích tụ trong máu.",
        "<b>Đặc tính màu sắc gan —</b> Dubin-Johnson có GAN ĐEN TUYỀN (Black liver) do ứ đọng sắc tố lysosome; Rotor có GAN BÌNH THƯỜNG KHÔNG ĐỔI MÀU (Normal histology).",
        "<b>Đặc tính Coproporphyrin nước tiểu —</b> Dubin-Johnson có tổng lượng bình thường với Coproporphyrin I chiếm > 80%; Rotor có TỔNG LƯỢNG COPROPORPHYRIN TĂNG RẤT CAO (> 2 - 5 lần) với Coproporphyrin I chiếm < 70%.",
        "<b>Điểm chung —</b> Đều là vàng da tăng Bilirubin trực tiếp lành tính, chức năng gan bình thường, tuổi thọ bình thường."
    ],
    "Chỉ cần nhớ 2 từ khóa: Dubin-Johnson = Đột biến MRP2 + Gan Đen; Rotor = Đột biến OATP + Gan Bình thường."
))

cards.append(make_card(
    "HS09-B7-07",
    "Bốn cơ chế sinh hóa học của Vàng da Sinh lý ở trẻ sơ sinh",
    "VÀNG DA SINH LÝ SƠ SINH",
    "Phân tích sự phối hợp của 4 cơ chế sinh hóa dẫn đến hiện tượng Vàng da Sinh lý ở trẻ sơ sinh?",
    [
        "<b>1. Tăng tải lượng Bilirubin do vỡ hồng cầu —</b> Trẻ sơ sinh có số lượng hồng cầu cao (5 - 6 T/L); đời sống hồng cầu chứa HbF ngắn hơn hồng cầu người lớn (chỉ 70 - 90 ngày so với 120 ngày); làm sản sinh lượng Bilirubin mỗi ngày cao gấp 2 đến 3 lần người lớn (8 - 10 mg/kg/ngày).",
        "<b>2. Hoạt tính UGT1A1 gan non yếu —</b> Hoạt tính của enzym UGT1A1 lúc mới sinh chỉ bằng khoảng 1% so với người lớn; gen UGT1A1 cần 1 đến 2 tuần sau sinh mới được kích hoạt biểu hiện hoàn thiện.",
        "<b>3. Thiếu hụt Ligandin nội bào gan —</b> Nồng độ protein Ligandin (Protein Y) trong tế bào gan trẻ sơ sinh rất thấp, làm giảm tốc độ bắt giữ Bilirubin vào bào tương.",
        "<b>4. Chu trình Ruột - Gan tăng cường mạnh mẽ —</b> Ruột trẻ sơ sinh vô khuẩn chưa có vi khuẩn chuyển bilirubin thành urobilinogen; đồng thời niêm mạc ruột và sữa mẹ giàu enzym β-GLUCURONIDASE thủy phân bilirubin liên hợp thành bilirubin tự do tái hấp thu ngược vào máu."
    ],
    "Vàng da sinh lý gặp ở 60% trẻ đủ tháng và 80% trẻ sinh non; là một hiện tượng quá độ bình thường của quá trình thích nghi từ tuần hoàn thai nhi sang tuần hoàn ngoài tử cung."
))

cards.append(make_card(
    "HS09-B7-08",
    "Tiêu chuẩn phân biệt Vàng da Sinh lý vs. Vàng da Bệnh lý sơ sinh",
    "CHẨN ĐOÁN VÀNG DA SƠ SINH",
    "Nêu 5 tiêu chuẩn kinh điển giúp phân biệt Vàng da Sinh lý với Vàng da Bệnh lý ở trẻ sơ sinh?",
    [
        "<b>1. Thời điểm khởi phát —</b> Vàng da sinh lý: Xuất hiện SAU 24 GIỜ ĐẦU (thường từ ngày thứ 2 - 3); Vàng da bệnh lý: XUẤT HIỆN RẤT SỚM TRONG VÒNG 24 GIỜ ĐẦU SAU SINH (luôn là bệnh lý do tan máu bất đồng nhóm máu ABO/Rh hoặc nhiễm trùng bào thai).",
        "<b>2. Tốc độ tăng Bilirubin —</b> Sinh lý: Tăng chậm; Bệnh lý: TĂNG RẤT NHANH (> 5 mg/dL/ngày hay > 0,2 mg/dL/giờ).",
        "<b>3. Nồng độ đỉnh Bilirubin toàn phần —</b> Sinh lý: Đạt đỉnh ngày 4 - 5 với nồng độ < 12 - 15 mg/dL; Bệnh lý: VƯỢT QUÁ 15 mg/dL ở trẻ đủ tháng hoặc > 17 mg/dL ở trẻ sinh non.",
        "<b>4. Loại Bilirubin chiếm ưu thế —</b> Sinh lý: Tăng thuần túy Bilirubin gián tiếp (Bilirubin trực tiếp < 1,5 - 2 mg/dL hoặc < 20%); Bệnh lý: Bất kỳ khi nào BILIRUBIN TRỰC TIẾP > 2 mg/dL đều là bệnh lý (teo đường mật, viêm gan sơ sinh).",
        "<b>5. Thời gian tồn tại kéo dài —</b> Sinh lý: Tự hết sau 1 - 2 tuần ở trẻ đủ tháng (sau 3 tuần ở trẻ sinh non); Bệnh lý: VÀNG DA KÉO DÀI TRÊN 2 TUẦN ở trẻ đủ tháng kèm triệu chứng bất thường (bú kém, li bì, phân bạc màu)."
    ],
    "Bất kỳ trẻ sơ sinh nào xuất hiện vàng da trong vòng 24 giờ đầu sau sinh bắt buộc phải được xử trí như một cấp cứu sơ sinh để tìm nguyên nhân tan máu miễn dịch và chiếu đèn ngay lập tức."
))

cards.append(make_card(
    "HS09-B7-09",
    "Cơ chế sinh hóa của Vàng da do Sữa mẹ (Breast Milk Jaundice)",
    "VÀNG DA DO SỮA MẸ",
    "Phân biệt Vàng da do thiếu bú mẹ (Breastfeeding Jaundice) và Vàng da do Sữa mẹ (Breast Milk Jaundice)?",
    [
        "<b>1. Vàng da do Thiếu bú mẹ (Breastfeeding Failure Jaundice) —</b> Xuất hiện sớm trong tuần đầu (ngày 2 - 5); do trẻ bú không đủ lượng sữa mẹ, mất nước, chậm bài tiết phân su làm tăng tái hấp thu bilirubin qua chu trình ruột - gan; xử trí bằng cách tăng cữ bú mẹ lên 10 - 12 lần/ngày.",
        "<b>2. Vàng da do Sữa mẹ thực sự (Breast Milk Jaundice) —</b> Xuất hiện muộn hơn (từ tuần thứ 2, đạt đỉnh ngày 10 - 15 và có thể kéo dài 3 đến 12 tuần); trẻ vẫn bú tốt, tăng cân bình thường, phát triển khỏe mạnh.",
        "<b>Cơ chế của Vàng da do Sữa mẹ —</b> Sữa mẹ của một số bà mẹ chứa nồng độ cao hormon PREGNANE-3α,20β-DIOL và ACID BÉO TỰ DO CHƯA BÃO HÒA gây ức chế cạnh tranh hoạt tính enzym UGT1A1 tại gan trẻ.",
        "<b>Enzym β-Glucuronidase trong sữa mẹ —</b> Sữa mẹ giàu enzym β-glucuronidase phân giải bilirubin diglucuronid trong lòng ruột thành bilirubin tự do tái hấp thu vào máu.",
        "<b>Xử trí lâm sàng —</b> LÀNH TÍNH HOÀN TOÀN; KHÔNG CẦN NGỪNG BÚ MẸ; tiếp tục cho trẻ bú mẹ bình thường, bilirubin sẽ tự thoái lui dần."
    ],
    "Trước đây từng có quan điểm tạm ngừng bú mẹ 24 - 48 giờ để chẩn đoán, nhưng các hiệp hội nhi khoa hiện đại khuyến cáo duy trì nuôi con bằng sữa mẹ hoàn toàn vì nồng độ bilirubin hiếm khi đạt ngưỡng gây độc thần kinh."
))

cards.append(make_card(
    "HS09-B7-10",
    "Cơ chế Vàng da Nhân não (Kernicterus / Bilirubin Encephalopathy)",
    "VÀNG DA NHÂN NÃO",
    "Phân tích cơ chế phân tử giải thích vì sao Bilirubin gián tiếp tự do gây độc hủy hoại nhân xám đáy não ở trẻ sơ sinh?",
    [
        "<b>Vượt quá sức chứa gắn Albumin —</b> Khi Bilirubin gián tiếp tăng cao vượt quá khả năng gắn kết của Albumin (> 20 - 25 mg/dL ở trẻ đủ tháng, hoặc thấp hơn nhiều khi có hạ thân nhiệt, nhiễm toan, hạ albumin máu), lượng phân tử BILIRUBIN TỰ DO KHÔNG LIÊN KẾT tăng vọt.",
        "<b>Xuyên qua Hàng rào máu - não có tính thấm cao —</b> Hàng rào máu - não ở trẻ sơ sinh chưa hoàn thiện, các mối nối liên bào lỏng lẻo cho phép bilirubin kỵ nước ngấm thẳng vào nhu mô não.",
        "<b>Lắng đọng chọn lọc tại các Nhân xám đáy não —</b> Ngấm vào NHÂN BÈO (Globus pallidus), THỂ DƯỚI ĐỒI (Subthalamic nucleus), HỒI HẢI MÃ (Hippocampus) và các nhân dây thần kinh sọ ở thân não (nhân tiền đình, nhân ốc tai, nhân dây III).",
        "<b>Độc tính ty thể và kích hoạt Apoptosis —</b> Bilirubin chèn vào màng ty thể nơ-ron, làm mất ghép cặp chuỗi hô hấp tế bào (uncoupling), ức chế tổng hợp ATP, làm rò rỉ ion canxi nội bào và kích hoạt caspase gây CHẾT NƠ-RON THEO CHƯƠNG TRÌNH KHÔNG HỒI PHỤC."
    ],
    "Tên gọi 'Kernicterus' xuất phát từ tiếng Đức ('Kern' = nhân não, 'Icterus' = vàng da), do nhà bệnh học Schmorl mô tả năm 1904 khi mổ tử thi thấy các nhân xám đáy não bị nhuộm màu vàng nghệ rực rỡ."
))

cards.append(make_card(
    "HS09-B7-11",
    "Triệu chứng lâm sàng cấp tính và Di chứng thần kinh của Vàng da Nhân",
    "DI CHỨNG KERNICTERUS",
    "Mô tả các giai đoạn tiến triển lâm sàng cấp tính và 4 di chứng thần kinh vĩnh viễn của bệnh Vàng da Nhân não?",
    [
        "<b>Giai đoạn cấp 1 (Khởi phát sớm) —</b> Trẻ bú kém, nôn trớ, ngủ li bì, giảm trương lực cơ toàn thân, mất phản xạ bú và phản xạ Moro.",
        "<b>Giai đoạn cấp 2 (Tiến triển nặng) —</b> Tăng trương lực cơ dữ dội, người uốn cong ra sau (Opisthotonos), khóc thét the the chói tai (high-pitched cry), sốt cao do tổn thương trung tâm điều nhiệt, co giật toàn thân.",
        "<b>Di chứng thần kinh 1: Bại não thể Múa vờn (Choreoathetoid Cerebral Palsy) —</b> Tổn thương nhân bèo gây rối loạn vận động ngoại tháp nặng nề: cử động múa vờn không tự chủ ở các chi và cơ mặt.",
        "<b>Di chứng thần kinh 2: Điếc tiếp nhận thần kinh thính giác —</b> Tổn thương nhân ốc tai và dây thần kinh số VIII gây điếc tiếp nhận thần kinh giác quan hai bên.",
        "<b>Di chứng thần kinh 3: Liệt nhìn ngước (Parinaud's Syndrome) —</b> Tổn thương nhân dây thần kinh vận nhãn khiến hai mắt luôn nhìn xuống, không thể nhìn ngước lên trên.",
        "<b>Di chứng thần kinh 4: Loạn sản men răng và Chậm phát triển trí tuệ —</b> Tổn thương mầm răng sữa tạo rãnh xanh men răng và thiểu năng trí tuệ mức độ khác nhau."
    ],
    "Vàng da nhân não một khi đã để lại di chứng thần kinh thì hoàn toàn không có khả năng hồi phục; mọi nỗ lực của chuyên ngành sơ sinh là chiếu đèn và thay máu dự phòng trước khi bilirubin ngấm vào não."
))

cards.append(make_card(
    "HS09-B7-12",
    "Nguyên lý Sinh hóa - Quang học của Liệu pháp Chiếu đèn (Phototherapy)",
    "QUANG TRỊ LIỆU SƠ SINH",
    "Trình bày cơ chế quang hóa học của Liệu pháp Chiếu đèn và phân tích cấu trúc phân tử của Lumirubin?",
    [
        "<b>Ánh sáng xanh bước sóng 460 - 490 nm —</b> Sử dụng ánh sáng nhìn thấy xanh dương trùng khít với đỉnh hấp thụ quang phổ của phức hợp [Bilirubin - Albumin] trong các mao mạch nông dưới da.",
        "<b>1. Quang đồng phân hóa cấu hình (4Z,15Z → 4Z,15E) —</b> Năng lượng photon quay một liên kết đôi 180°, bẻ gãy một phần liên kết hydro nội phân tử; đồng phân 4Z,15E tan một phần trong nước và bài tiết qua mật mà KHÔNG CẦN GAN LIÊN HỢP (nhưng có tính thuận nghịch).",
        "<b>2. Quang đồng phân hóa cấu trúc tạo LUMIRUBIN (Phản ứng quyết định) —</b> Kích thích phản ứng đóng vòng nội phân tử bất thuận nghịch giữa gốc vinyl C3 và vòng pyrrol kế cận, tạo ra phân tử LUMIRUBIN (Cyclobilirubin).",
        "<b>Bản chất siêu ưa nước của Lumirubin —</b> Phân tử Lumirubin HOÀN TOÀN MẤT HẾT CÁC LIÊN KẾT HYDRO NỘI PHÂN TỬ, trở nên CỰC KỲ ƯA NƯỚC, hòa tan mạnh trong nước.",
        "<b>Đào thải siêu tốc qua Mật và Nước tiểu —</b> Lumirubin được đào thải rất nhanh ra khỏi máu qua cả dịch mật và nước tiểu mà HOÀN TOÀN KHÔNG CẦN QUA BẤT KỲ BƯỚC LIÊN HỢP NÀO TẠI GAN; tốc độ tạo Lumirubin quyết định hiệu quả hạ bilirubin của chiếu đèn."
    ],
    "Chiếu đèn không làm phá hủy phân tử bilirubin thành chất độc mà là một phản ứng 'chuyển dạng không gian': biến đổi một phân tử kỵ nước độc hại thành phân tử ưa nước lành tính dễ dàng đào thải."
))

# ==============================================================================
# SECTION B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS09-ALGO-01",
    "Phân tầng chẩn đoán 3 thể vàng da (Trước gan vs. Tại gan vs. Sau gan)",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Trình bày lưu đồ thuật toán 4 bước phân tầng chẩn đoán xác định 3 thể vàng da dựa trên bộ xét nghiệm sinh hóa cơ bản?",
    [
        "<b>Bước 1 (Định lượng Bilirubin Trực tiếp và Gián tiếp) —</b> Nếu Bilirubin Gián tiếp chiếm ưu thế tuyệt đối (> 80%) → Định hướng ngay VÀNG DA TRƯỚC GAN (Tan máu) hoặc Hội chứng Gilbert; Nếu Bilirubin Trực tiếp tăng vọt (> 50 - 60%) → Định hướng VÀNG DA SAU GAN (Tắc mật); Nếu tăng hỗn hợp cả hai → Định hướng VÀNG DA TẠI GAN.",
        "<b>Bước 2 (Kiểm tra Nước tiểu: Sắc tố mật & Urobilinogen) —</b> Nếu Sắc tố mật (-) và Urobilinogen (+++) → Khẳng định TAN MÁU; Nếu Sắc tố mật (+++ đậm bọt vàng) và Urobilinogen = 0 hoàn toàn → Khẳng định TẮC MẬT CƠ HỌC HOÀN TOÀN; Nếu cả hai đều (+) → TỔN THƯƠNG NHU MÔ GAN.",
        "<b>Bước 3 (Đánh giá Màu sắc Phân) —</b> Phân sẫm màu nâu đậm → Tan máu; Phân bạc màu trắng như đất sét / phân cò → Tắc mật cơ học sau gan.",
        "<b>Bước 4 (Đối chiếu Men gan ALT/AST so với Men ứ mật ALP/GGT) —</b> ALT/AST tăng vọt > 10 - 20 lần → Viêm gan cấp hoại tử; ALP và GGT tăng vọt ưu thế > 3 - 5 lần → Tắc mật cơ học sau gan."
    ],
    "Lưu đồ 4 bước phân tầng vàng da là phản xạ tư duy lâm sàng cốt tử của bác sĩ tiêu hóa và nội soi, giúp chỉ định chính xác giữa can thiệp ngoại khoa cấp cứu (lấy sỏi/stent u) hay điều trị nội khoa.",
    algo=True
))

cards.append(make_card(
    "HS09-ALGO-02",
    "Phân biệt nhanh 4 hội chứng vàng da di truyền (Gilbert, CN, Dubin-Johnson, Rotor)",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước phân biệt dứt khoát 4 hội chứng rối loạn chuyển hóa Bilirubin di truyền?",
    [
        "<b>Bước 1 (Phân loại theo loại Bilirubin tăng ưu thế) —</b> Tăng Bilirubin Gián tiếp: Nhóm Gilbert và Crigler-Najjar; Tăng Bilirubin Trực tiếp: Nhóm Dubin-Johnson và Rotor.",
        "<b>Bước 2 (Phân biệt trong nhóm Gián tiếp) —</b> Nếu vàng da nhẹ lành tính khi nhịn đói/stress (Bilirubin < 3 - 4 mg/dL) → HỘI CHỨNG GILBERT; Nếu vàng da rất nặng từ sơ sinh (> 20 mg/dL) → HỘI CHỨNG CRIGLER-NAJJAR.",
        "<b>Bước 3 (Test Phenobarbital phân biệt Crigler-Najjar Type I vs Type II) —</b> Uống Phenobarbital: Nếu Bilirubin giảm mạnh > 25 - 30% → CRIGLER-NAJJAR TYPE II (Hội chứng Arias); Nếu hoàn toàn không suy giảm → CRIGLER-NAJJAR TYPE I (Mất 100% UGT1A1).",
        "<b>Bước 4 (Phân biệt trong nhóm Trực tiếp: Dubin-Johnson vs Rotor) —</b> Kiểm tra mô học gan và Coproporphyrin niệu: Nếu GAN CÓ MÀU ĐEN TUYỀN (Black liver) + Coproporphyrin I > 80% → HỘI CHỨNG DUBIN-JOHNSON (Đột biến MRP2); Nếu GAN BÌNH THƯỜNG KHÔNG ĐỔI MÀU + Coproporphyrin niệu toàn phần tăng cao → HỘI CHỨNG ROTOR (Đột biến OATP1B1/3)."
    ],
    "Cây quyết định 4 bước giúp giải mã nhanh chóng các ca lâm sàng di truyền hóc búa trong các kỳ thi Bác sĩ Nội trú và USMLE Step 1.",
    algo=True
))

cards.append(make_card(
    "HS09-ALGO-03",
    "Lưu đồ tiếp cận và chỉ định Chiếu đèn / Thay máu ở trẻ vàng da sơ sinh",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán cấp cứu 4 bước đánh giá và can thiệp vàng da sơ sinh phòng ngừa Vàng da nhân não?",
    [
        "<b>Bước 1 (Đánh giá thời điểm xuất hiện vàng da) —</b> Nếu xuất hiện trong vòng 24 GIỜ ĐẦU SAU SINH → BÁO ĐỘNG CỜ ĐỎ CẤP CỨU: làm ngay nhóm máu mẹ - con (ABO, Rh), nghiệm pháp Coombs trực tiếp, công thức máu và nồng độ Bilirubin toàn phần.",
        "<b>Bước 2 (Đo Bilirubin toàn phần và Đối chiếu Biểu đồ giờ tuổi Bhutani) —</b> Lấy máu đo TSB (Total Serum Bilirubin); đối chiếu với biểu đồ bách phân vị giờ tuổi của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP) theo tuần thai và các yếu tố nguy cơ (tan máu miễn dịch, ngạt, nhiễm toan, hạ thân nhiệt).",
        "<b>Bước 3 (Chỉ định Chiếu đèn quang trị liệu tích cực) —</b> Khi đường cong TSB vượt ngưỡng chiếu đèn: Đặt trẻ dưới hệ thống ĐÈN ÁNH SÁNG XANH (460 - 490 nm) liên tục hai mặt, che mắt bảo vệ võng mạc, truyền đủ dịch và theo dõi TSB mỗi 4 - 6 giờ.",
        "<b>Bước 4 (Chỉ định THAY MÁU CẤP CỨU - Exchange Transfusion) —</b> Khi TSB vượt ngưỡng thay máu (thường > 20 - 25 mg/dL) hoặc trẻ có bất kỳ DẤU HIỆU THẦN KINH SỚM NÀO (bú kém, li bì, khóc thét the the, uốn cong người) → Thực hiện thay máu cấp cứu ngay lập tức để rút nhanh bilirubin tự do ra khỏi tuần hoàn cứu não."
    ],
    "Nguyên tắc vàng: Không bao giờ trì hoãn chiếu đèn để chờ kết quả xét nghiệm nếu trẻ có dấu hiệu vàng da tiến triển nhanh; hành động sớm cứu vãn tương lai thần kinh của đứa trẻ.",
    algo=True
))

cards.append(make_card(
    "HS09-ALGO-04",
    "Phân biệt Porphyria cấp từng cơn (AIP) vs. Porphyria da chậm (PCT)",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước phân biệt dứt khoát giữa Porphyria cấp từng cơn (AIP) và Porphyria da chậm (PCT)?",
    [
        "<b>Bước 1 (Đánh giá tổn thương da phơi nắng) —</b> Nếu bệnh nhân có bọng nước, trợt loét, sẹo teo, rậm lông mặt ở mu bàn tay và mặt → ĐỊNH HƯỚNG PORPHYRIA DA CHẬM (PCT); Nếu HOÀN TOÀN KHÔNG CÓ TỔN THƯƠNG DA → ĐỊNH HƯỚNG PORPHYRIA CẤP TỪNG CƠN (AIP).",
        "<b>Bước 2 (Đánh giá triệu chứng đau bụng và thần kinh) —</b> Đau quặn bụng cấp dữ dội bụng mềm, nhịp tim nhanh, liệt vận động, loạn thần kịch phát → CƠN CẤP AIP.",
        "<b>Bước 3 (Xét nghiệm Nước tiểu chuyên biệt) —</b> Xét nghiệm định lượng Porphobilinogen (PBG) và ALA niệu tăng vọt hàng chục lần → Khẳng định AIP; Nước tiểu phát huỳnh quang đỏ hồng dưới đèn cực tím Wood và Uroporphyrin niệu tăng vọt → Khẳng định PCT.",
        "<b>Bước 4 (Phác đồ can thiệp đặc hiệu đối lập) —</b> Cơn cấp AIP: Truyền tĩnh mạch HEMIN (Panhematin) hoặc GLUCOSE liều cao để ức chế ALAS-1; Bệnh PCT: TRÍCH MÁU TĨNH MẠCH định kỳ hạ sắt dự trữ hoặc dùng HYDROXYCHLOROQUINE LIỀU THẤP."
    ],
    "Cây quyết định phân biệt 2 thể Porphyria lớn: AIP = Đau bụng + Loạn thần + Không tổn thương da (Điều trị: Hemin); PCT = Bọng nước da + Nhạy cảm ánh sáng + Không đau bụng cấp (Điều trị: Trích máu).",
    algo=True
))

cards.append(make_card(
    "HS09-ALGO-05",
    "Tiếp cận chẩn đoán ngộ độc Chì dựa trên chỉ số sinh tổng hợp Hem",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước tiếp cận chẩn đoán xác định nhiễm độc Chì dựa trên các mắt xích sinh hóa tổng hợp Hem?",
    [
        "<b>Bước 1 (Nghi ngờ trên lâm sàng và yếu tố dịch tễ) —</b> Trẻ em chậm phát triển trí tuệ/co giật, người lớn đau quặn bụng cơn táo bón (Lead colic), yếu cơ bàn tay rủ (Wrist drop), đường viền nướu răng xanh đen Burton.",
        "<b>Bước 2 (Đo trực tiếp Nồng độ Chì trong máu - Blood Lead Level) —</b> Tiêu chuẩn vàng: Nồng độ chì máu (BLL) ≥ 5 µg/dL ở trẻ em hoặc ≥ 20 - 25 µg/dL ở người lớn phơi nhiễm nghề nghiệp.",
        "<b>Bước 3 (Đánh giá ức chế enzym Bước 2 và Bước 8) —</b> Đo nồng độ Acid δ-aminolevulinic (ALA) niệu tăng cao (do ức chế ALA Dehydratase); Đo Kẽm-Protoporphyrin (ZPP / FEP) trong hồng cầu tăng vọt (do ức chế Ferrochelatase).",
        "<b>Bước 4 (Đánh giá tiêu bản Huyết đồ và Tủy đồ) —</b> Quan sát thấy các chấm HẠT KIỀM (Basophilic stippling) trong hồng cầu trên lam máu ngoại vi; Nhuộm xanh Perls tủy xương phát hiện NGUYÊN HỒNG CẦU SẮT DẠNG VÒNG (Ringed Sideroblasts); Thiếu máu hồng cầu nhỏ nhược sắc."
    ],
    "Phối hợp đo Chì máu, ZPP hồng cầu và ALA niệu giúp xác định toàn diện mức độ ngộ độc chì cấp tính và sự phơi nhiễm mạn tính tích tụ trong cơ thể.",
    algo=True
))

# ==============================================================================
# XUẤT FILE CARDS V2 JSON
# ==============================================================================

out_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-09_Chuyen_hoa_hemoglobin")
cards_file = out_dir / "HS-09_Chuyen_hoa_hemoglobin.cards.v2.json"

output_data = {
    "cards": cards,
    "total": len(cards),
    "version": "v2"
}

with open(cards_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Đã tạo thành công {len(cards)} thẻ Master chuyên sâu cho HS-09 tại:")
print(f"-> {cards_file}")
