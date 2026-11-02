# -*- coding: utf-8 -*-
"""build_deep_hs12.py - Generate 81 exhaustive master flashcards for HS-12 (Purine, Pyrimidine, Uric Acid Metabolism & Gout)"""
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
        "extra": extra or "Nguồn: Giáo trình Hóa Sinh Y Học - ĐHYHN (GS. Tạ Thành Văn, Tr. 246-266), Lehninger Principles of Biochemistry 8th ed (Chap 22, 25), Harper's Illustrated Biochemistry 32nd ed (Chap 33, 35).",
        "tags": ["hoasinh", "HS12", section]
    }

cards = []

# ==============================================================================
# SECTION B1: TIÊU HÓA ACID NUCLEIC & NGUỒN GỐC NHÂN PURIN (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B1-01",
    "Tiêu hóa Acid Nucleic tại Dạ dày và Tụy",
    "TIÊU HÓA & HẤP THU",
    "Quá trình biến tính và thủy phân acid nucleic ngoại sinh diễn ra tại dạ dày và dịch tụy như thế nào?",
    [
        "<b>Tại dạ dày —</b> Môi trường acid dịch vị (pH xấp xỉ 1.5 - 2.0) làm biến tính nucleoprotein phức tạp thành acid nucleic tự do và protein, nhưng các liên kết phosphodiester hầu như không bị phân cắt.",
        "<b>Tại tá tràng & ruột non —</b> Dịch tụy tiết endonuclease gồm Ribonuclease (RNase) và Deoxyribonuclease (DNase) xúc tác thủy phân liên kết phosphodiester nội chuỗi, biến DNA và RNA dài thành các mẩu Oligonucleotide ngắn.",
        "<b>Điểm cốt lõi —</b> Dạ dày chỉ đóng vai trò phân ly phức hợp protein - acid nucleic; sự thủy phân khung nucleic acid chính thức bắt đầu từ ruột non nhờ enzyme dịch tụy."
    ],
    "Môi trường acid dạ dày không đủ để bẻ gãy liên kết cộng hóa trị phosphodiester bền vững. Endonuclease tụy (DNase/RNase) cắt ngẫu nhiên các liên kết nội chuỗi tạo ra các đoạn oligonucleotide có đầu 3'-hydroxyl hoặc 5'-phosphate."
))

cards.append(make_card(
    "HS12-B1-02",
    "Thủy phân tại Ruột: Phosphodiesterase & Nucleotidase",
    "TIÊU HÓA & HẤP THU",
    "Enzyme Phosphodiesterase và Nucleotidase tại ruột non xúc tác các bước phân giải nào?",
    [
        "<b>Phosphodiesterase ruột —</b> Do niêm mạc ruột non tiết ra, tiếp tục cắt các oligonucleotide thành các Mononucleotide tự do.",
        "<b>Nucleotidase bờ bàn chải —</b> Các nucleotidase đặc hiệu và phosphatase kiềm màng tế bào biểu mô ruột cắt bỏ nhóm phosphate, chuyển mononucleotide thành Nucleosid.",
        "<b>Số phận nucleosid —</b> Nucleosid có thể được hấp thu trực tiếp qua các kênh vận chuyển nucleoside chuyên biệt hoặc tiếp tục bị cắt giải phóng base nitơ tự do."
    ],
    "Sự phân giải acid nucleic diễn ra tuần tự từ polyme (DNA/RNA) → oligomer (Oligonucleotide) → monomer (Mononucleotide) → Nucleoside → Base nitơ tự do và pentose."
))

cards.append(make_card(
    "HS12-B1-03",
    "Phản ứng của Nucleoside Phosphorylase tại Bờ Bàn Chải",
    "TIÊU HÓA & HẤP THU",
    "Enzyme Nucleoside Phosphorylase xúc tác phản ứng giải phóng base nitơ tự do như thế nào?",
    [
        "<b>Phương trình phản ứng —</b> Nucleosid + Pi (phosphate vô cơ) ↔ Base tự do + Ribose-1-phosphate (hoặc Deoxyribose-1-phosphate).",
        "<b>Bản chất xúc tác —</b> Phân cắt liên kết N-glycosidic bằng con đường phosphoryl phân (phosphorolysis) thay vì thủy phân, bảo tồn một phần năng lượng liên kết dưới dạng đường phosphat hóa.",
        "<b>Chuyển hóa tiếp theo —</b> Ribose-1-P được enzyme Phosphopentomutase đồng phân hóa thành Ribose-5-P, đi vào con đường Pentose Phosphate hoặc tổng hợp PRPP."
    ],
    "Sự phosphoryl phân liên kết N-glycosidic là phản ứng thuận nghịch. Enzyme Purine Nucleoside Phosphorylase (PNP) đóng vai trò trung tâm trong cả tiêu hóa ruột và thoái hóa purin nội bào."
))

cards.append(make_card(
    "HS12-B1-04",
    "Số phận Sinh hóa của Purin Ngoại sinh từ Thức ăn",
    "CHUYỂN HÓA PURIN",
    "Số phận sinh hóa của hơn 95% base Purin ngoại sinh hấp thu từ ống tiêu hóa là gì?",
    [
        "<b>Thoái hóa tại chỗ tại ruột —</b> Hơn 95% base Purin ngoại sinh từ thức ăn không được sử dụng để tổng hợp acid nucleic của tế bào cơ thể, mà bị thoái hóa ngay tại tế bào biểu mô ruột thành Acid Uric.",
        "<b>Đào thải —</b> Acid Uric theo tĩnh mạch cửa về gan, vào tuần hoàn chung và bài xuất ra ngoài chủ yếu qua nước tiểu.",
        "<b>Khả năng tự tổng hợp —</b> Toàn bộ mô cơ thể người hoàn toàn có khả năng tự tổng hợp toàn bộ lượng purin và pyrimidin nucleotide cần thiết từ các tiền chất đơn giản qua con đường tân tạo (de novo) và trục vớt (salvage)."
    ],
    "Đây là lý do chế độ ăn quá nhiều purin (thịt đỏ, phủ tạng, bia rượu, hải sản) trực tiếp làm bùng nổ nồng độ Acid Uric máu mà không làm tăng nguồn nucleotide nội bào của cơ thể."
))

cards.append(make_card(
    "HS12-B1-05",
    "Nguồn gốc Nguyên tử N1 của Nhân Purin",
    "CẤU TRÚC NHÂN PURIN",
    "Nguyên tử Nitơ số 1 (N1) trong nhân Purin có nguồn gốc từ tiền chất nào?",
    [
        "<b>Tiền chất cung cấp —</b> Nhóm amin của acid amin Aspartat (Acid Aspartic).",
        "<b>Phản ứng gắn —</b> CAIR kết hợp với Aspartat nhờ enzyme SACAIR Synthetase (tiêu tốn 1 ATP) tạo thành SACAIR.",
        "<b>Tách fumarat —</b> Enzyme Adenylosuccinate lyase cắt khung carbon của Aspartat rời đi dưới dạng Fumarat, để lại nguyên tử N1 gắn vĩnh viễn trên nhân purin."
    ],
    "Cơ chế mượn nitơ của Aspartat rồi trả lại khung carbon dưới dạng Fumarat tương tự như bước kết hợp Citrulline với Aspartat trong chu trình Urê tại gan."
))

cards.append(make_card(
    "HS12-B1-06",
    "Nguồn gốc Nguyên tử C2 và C8 của Nhân Purin",
    "CẤU TRÚC NHÂN PURIN",
    "Nguyên tử Carbon số 2 (C2) và số 8 (C8) trong nhân Purin có nguồn gốc từ tiền chất nào?",
    [
        "<b>Tiền chất cung cấp —</b> Nhóm formyl (-CHO) của N10-formyl-tetrahydrofolate (N10-formyl-THF), dẫn xuất hoạt hóa của Acid Folic (Vitamin B9).",
        "<b>Gắn nguyên tử C8 —</b> Enzyme GAR Transformylase chuyển nhóm formyl từ N10-formyl-THF vào GAR tạo thành FGAR.",
        "<b>Gắn nguyên tử C2 —</b> Enzyme AICAR Transformylase chuyển nhóm formyl từ N10-formyl-THF vào AICAR tạo thành FAICAR."
    ],
    "Cả hai nguyên tử C2 và C8 đều có nguồn gốc từ chuyển hóa một carbon phụ thuộc Folate. Đây là đích ức chế phân tử của các thuốc kháng folate (Methotrexate) trong điều trị ung thư."
))

cards.append(make_card(
    "HS12-B1-07",
    "Nguồn gốc Nguyên tử N3 và N9 của Nhân Purin",
    "CẤU TRÚC NHÂN PURIN",
    "Nguyên tử Nitơ số 3 (N3) và số 9 (N9) trong nhân Purin có nguồn gốc từ tiền chất nào?",
    [
        "<b>Tiền chất cung cấp —</b> Nhóm amide ở chuỗi bên của acid amin Glutamin.",
        "<b>Nguyên tử N9 —</b> Phản ứng chuyển amid của Glutamin thế chỗ pyrophosphate của PRPP tạo 5-Phosphoribosylamine (PRA) xúc tác bởi Glutamine-PRPP Amidotransferase (bước quyết định tốc độ).",
        "<b>Nguyên tử N3 —</b> Phản ứng chuyển amid của Glutamin gắn vào FGAR tạo Formylglycinamidine ribotide (FGAM) nhờ FGAM Synthetase (tiêu tốn 1 ATP)."
    ],
    "Glutamin đóng góp 2 nguyên tử nitơ (N3 và N9). Thuốc kháng chuyển hóa tương tự glutamine (như Azaserine, DON) có tác dụng ức chế mạnh mẽ tổng hợp purin."
))

cards.append(make_card(
    "HS12-B1-08",
    "Nguồn gốc Khung 3 Nguyên tử C4, C5 và N7 của Nhân Purin",
    "CẤU TRÚC NHÂN PURIN",
    "Khung 3 nguyên tử C4, C5 và N7 trong nhân Purin có nguồn gốc từ tiền chất nào?",
    [
        "<b>Tiền chất cung cấp —</b> Đóng góp trọn vẹn từ toàn bộ một phân tử acid amin Glycin.",
        "<b>Phản ứng gắn —</b> Phân tử 5-Phosphoribosylamine (PRA) kết hợp với Glycin nhờ enzyme GAR Synthetase với sự tiêu tốn 1 phân tử ATP.",
        "<b>Sản phẩm tạo thành —</b> Glycinamide ribotide (GAR), tích hợp nguyên vẹn cả 3 nguyên tử C4, C5 và N7 vào nhân purin đang hình thành."
    ],
    "Glycin là acid amin duy nhất được tích hợp toàn bộ khung phân tử (C-C-N) vào nhân purin mà không bị cắt tỉa hay chỉ mượn nhóm chức."
))

cards.append(make_card(
    "HS12-B1-09",
    "Nguồn gốc Nguyên tử C6 của Nhân Purin",
    "CẤU TRÚC NHÂN PURIN",
    "Nguyên tử Carbon số 6 (C6) trong nhân Purin có nguồn gốc từ tiền chất nào?",
    [
        "<b>Tiền chất cung cấp —</b> Bicarbonate vô cơ (HCO3-) hoặc khí CO2 hòa tan trong dịch tế bào.",
        "<b>Phản ứng carboxyl hóa —</b> AIR kết hợp với CO2 nhờ enzyme AIR Carboxylase để tạo thành Carboxyaminoimidazole ribotide (CAIR).",
        "<b>Đặc điểm xúc tác —</b> Phản ứng carboxyl hóa này ở động vật nhân thực không cần cofactor Biotin (Vitamin B7) như các enzyme carboxylase thông thường."
    ],
    "Phản ứng carboxyl hóa đưa nguyên tử carbon C6 vào đỉnh của vòng 6 cạnh pyrimidine trong cấu trúc đôi của nhân purin."
))

cards.append(make_card(
    "HS12-B1-10",
    "Ứng dụng Dược lý: Ức chế Chuyển hóa Folate trong Tổng hợp Purin",
    "DƯỢC LÝ & UNG THƯ",
    "Tại sao các thuốc kháng Folate (Methotrexate, Sulfonamid) làm ngừng trệ sinh tổng hợp Purin?",
    [
        "<b>Cơ chế Methotrexate —</b> Ức chế cạnh tranh mạnh mẽ enzyme Dihydrofolate Reductase (DHFR), ngăn cản tái tạo Tetrahydrofolate (THF), làm cạn kiệt nguồn N10-formyl-THF.",
        "<b>Hậu quả trên Purin de novo —</b> Khi thiếu N10-formyl-THF, cả hai phản ứng formyl hóa gắn C8 (bởi GAR Transformylase) và C2 (bởi AICAR Transformylase) đều bị phong bế hoàn toàn.",
        "<b>Ý nghĩa lâm sàng —</b> Tế bào ung thư đang tăng sinh phân chia mạnh mẽ bị cạn kiệt nucleotide purin để nhân đôi DNA, dẫn tới ngừng chu kỳ tế bào và chết theo chương trình (apoptosis)."
    ],
    "Methotrexate cũng đồng thời ức chế tổng hợp dTMP (thymidylate), tạo ra tác động 'đòn kép' dập tắt cả purin và pyrimidin trong tế bào khối u."
))

# ==============================================================================
# SECTION B2: SINH TỔNG HỢP PURIN DE NOVO & ĐIỀU HÒA TƯƠNG HỖ (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B2-01",
    "Nguyên lý Nền tảng Con đường Purin De Novo",
    "PURIN DE NOVO",
    "Nguyên lý nền tảng của con đường sinh tổng hợp Purin De Novo khác gì so với Pyrimidin De Novo?",
    [
        "<b>Nguyên lý Purin —</b> Nhân Purin không được tổng hợp ở dạng base tự do trước, mà được xây dựng từng bước trực tiếp ngay trên bộ khung alpha-D-ribose-5-phosphate tại bào tương.",
        "<b>Ngược lại ở Pyrimidin —</b> Nhân Pyrimidin 6 cạnh tự do (Acid Orotic) được tổng hợp hoàn chỉnh trước, sau đó mới gắn vào khung PRPP.",
        "<b>Sản phẩm đầu tiên —</b> Sản phẩm hoàn chỉnh đầu tiên của con đường purin de novo là nucleotid Inosine Monophosphate (IMP) chứa base Hypoxanthine."
    ],
    "Xây dựng nhân trực tiếp trên đường pentose giúp bảo vệ các chất trung gian khỏi bị khuếch tán ra ngoài tế bào và định hướng cấu hình đồng phân beta-glycosidic ngay từ đầu."
))

cards.append(make_card(
    "HS12-B2-02",
    "Phản ứng Tạo PRPP bởi PRPP Synthetase",
    "PURIN DE NOVO",
    "Phản ứng tạo PRPP do PRPP Synthetase xúc tác diễn ra như thế nào và được điều hòa ra sao?",
    [
        "<b>Phương trình phản ứng —</b> alpha-D-Ribose-5-phosphate + ATP → 5-Phosphoribosyl-alpha-pyrophosphate (PRPP) + AMP (xúc tác bởi PRPP Synthetase).",
        "<b>Cơ chế truyền nhóm —</b> Chuyển trọn vẹn nhóm pyrophosphate từ ATP vào nhóm OH ở vị trí C1 của Ribose-5-P.",
        "<b>Điều hòa dị lập thể âm —</b> Enzyme bị ức chế feedback allosteric mạnh bởi các sản phẩm purin nucleotide gồm AMP, ADP, GMP và GDP."
    ],
    "PRPP là chất hoạt hóa trung tâm cung cấp khung ribose-phosphate cho cả 3 con đường: tân tạo purin, tân tạo pyrimidin và con đường trục vớt base nitơ."
))

cards.append(make_card(
    "HS12-B2-03",
    "Bước Quyết định Tốc độ: Glutamine-PRPP Amidotransferase",
    "PURIN DE NOVO",
    "Phản ứng quyết định tốc độ (Committed Step) của con đường tân tạo Purin là gì và được điều hòa thế nào?",
    [
        "<b>Phương trình phản ứng —</b> PRPP + Glutamin + H2O → 5-Phosphoribosyl-beta-amine (PRA) + Glutamat + PPi (xúc tác bởi Glutamine-PRPP Amidotransferase - GPA).",
        "<b>Đặc điểm hóa học —</b> Nhóm amide của Glutamin thế chỗ nhóm pyrophosphate tại C1, đồng thời đảo cấu hình anomer từ alpha sang beta (đây chính là nguyên tử N9 của purin).",
        "<b>Điều hòa then chốt —</b> Bị ức chế allosteric feedback hiệp đồng bởi AMP, GMP và IMP; được hoạt hóa allosteric mạnh mẽ bởi chính cơ chất PRPP."
    ],
    "Khi nồng độ PRPP nội bào tăng cao (như trong hội chứng Lesch-Nyhan), enzyme GPA bị kích hoạt tối đa, làm tăng vọt tốc độ sản xuất purin và acid uric."
))

cards.append(make_card(
    "HS12-B2-04",
    "Giai đoạn Tạo Vòng Imidazole 5 cạnh",
    "PURIN DE NOVO",
    "Giai đoạn tạo vòng Imidazole 5 cạnh từ PRA gồm các bước phản ứng cơ bản nào?",
    [
        "<b>Bước 3 (Gắn Glycin) —</b> PRA + Glycin + ATP → Glycinamide ribotide (GAR) + ADP + Pi (xúc tác bởi GAR Synthetase).",
        "<b>Bước 4 (Formyl hóa C8) —</b> GAR + N10-formyl-THF → Formylglycinamide ribotide (FGAR) + THF (xúc tác bởi GAR Transformylase).",
        "<b>Bước 5 (Amin hóa N3) —</b> FGAR + Glutamin + ATP → Formylglycinamidine ribotide (FGAM) + Glutamat + ADP + Pi (xúc tác bởi FGAM Synthetase).",
        "<b>Bước 6 (Đóng vòng Imidazole) —</b> FGAM + ATP → 5-Aminoimidazole ribotide (AIR) + ADP + Pi + H2O (xúc tác bởi AIR Synthetase)."
    ],
    "Kết thúc bước 6, vòng 5 cạnh Imidazole đã được khép kín hoàn chỉnh trên phân tử ribose-5-phosphate, sẵn sàng cho việc lắp ráp tiếp vòng 6 cạnh Pyrimidine."
))

cards.append(make_card(
    "HS12-B2-05",
    "Giai đoạn Lắp ráp Vòng 6 cạnh và Tạo IMP",
    "PURIN DE NOVO",
    "Giai đoạn tạo vòng 6 cạnh và hoàn thành phân tử Inosine Monophosphate (IMP) diễn ra như thế nào?",
    [
        "<b>Bước 7 (Carboxyl hóa C6) —</b> AIR + HCO3- + ATP → CAIR + ADP + Pi (AIR Carboxylase).",
        "<b>Bước 8 & 9 (Gắn N1 và tách Fumarat) —</b> CAIR + Aspartat + ATP → SACAIR → tách Fumarat tạo AICAR (Adenylosuccinate lyase).",
        "<b>Bước 10 (Formyl hóa C2) —</b> AICAR + N10-formyl-THF → FAICAR + THF (AICAR Transformylase).",
        "<b>Bước 11 (Đóng vòng Pyrimidine) —</b> FAICAR khử nước đóng vòng tạo Inosine Monophosphate (IMP) hoàn chỉnh (IMP Cyclohydrolase)."
    ],
    "Tổng cộng 11 phản ứng tuần tự đã xây dựng hoàn chỉnh phân tử IMP mang nhân Hypoxanthine, là ngã ba đường để tổng hợp AMP và GMP."
))

cards.append(make_card(
    "HS12-B2-06",
    "Vị trí Ngã ba Đường của Inosine Monophosphate (IMP)",
    "PURIN DE NOVO",
    "Cấu trúc và ý nghĩa ngã ba đường chuyển hóa của Inosine Monophosphate (IMP) là gì?",
    [
        "<b>Cấu trúc —</b> IMP gồm base purin Hypoxanthine liên kết qua liên kết beta-N9-glycosidic với Ribose-5-phosphate.",
        "<b>Ngã ba đường —</b> IMP là tiền thân chung trực tiếp để phân nhánh tổng hợp nên cả hai ribonucleotide purin thiết yếu: Adenosine monophosphate (AMP) và Guanosine monophosphate (GMP).",
        "<b>Điều hòa ngã ba —</b> Sự phân chia tỷ lệ IMP đi vào nhánh AMP hay GMP được kiểm soát chặt chẽ bởi cơ chế điều hòa tương hỗ (reciprocal regulation) phụ thuộc GTP và ATP."
    ],
    "IMP không tích lũy với số lượng lớn trong tế bào mà nhanh chóng được chuyển hóa thành AMP hoặc GMP, hoặc thoái hóa thành acid uric."
))

cards.append(make_card(
    "HS12-B2-07",
    "Con đường Tổng hợp AMP từ IMP",
    "PURIN DE NOVO",
    "Nhánh tổng hợp AMP từ IMP diễn ra qua các phản ứng nào và sử dụng nguồn năng lượng gì?",
    [
        "<b>Phản ứng 1 (Gắn Aspartat) —</b> IMP + Aspartat + GTP → Adenylosuccinate + GDP + Pi (xúc tác bởi Adenylosuccinate Synthetase).",
        "<b>Phản ứng 2 (Tách Fumarat) —</b> Adenylosuccinate → AMP + Fumarat (xúc tác bởi Adenylosuccinate Lyase).",
        "<b>Năng lượng đặc thù —</b> Bắt buộc phải sử dụng nguồn năng lượng cao năng là GTP (thay vì ATP).",
        "<b>Ức chế ngược —</b> AMP ức chế feedback dị lập thể enzyme Adenylosuccinate Synthetase."
    ],
    "Khung carbon của Aspartat rời đi dưới dạng Fumarat đi vào chu trình Krebs, để lại nhóm amin ở vị trí C6 tạo nên Adenine."
))

cards.append(make_card(
    "HS12-B2-08",
    "Con đường Tổng hợp GMP từ IMP",
    "PURIN DE NOVO",
    "Nhánh tổng hợp GMP từ IMP diễn ra qua các phản ứng nào và sử dụng nguồn năng lượng gì?",
    [
        "<b>Phản ứng 1 (Oxy hóa tạo XMP) —</b> IMP + NAD+ + H2O → Xanthosine monophosphate (XMP) + NADH + H+ (xúc tác bởi IMP Dehydrogenase).",
        "<b>Phản ứng 2 (Amin hóa XMP) —</b> XMP + Glutamin + ATP + H2O → GMP + Glutamat + AMP + PPi (xúc tác bởi GMP Synthetase).",
        "<b>Năng lượng đặc thù —</b> Bắt buộc phải sử dụng nguồn năng lượng cao năng là ATP (thay vì GTP).",
        "<b>Ức chế ngược —</b> GMP ức chế feedback dị lập thể enzyme IMP Dehydrogenase."
    ],
    "Enzyme IMP Dehydrogenase là đích ức chế phân tử chọn lọc của thuốc ức chế miễn dịch Mycophenolate Mofetil."
))

cards.append(make_card(
    "HS12-B2-09",
    "Cơ chế Điều hòa Tương hỗ (Reciprocal Regulation) giữa AMP và GMP",
    "ĐIỀU HÒA CHUYỂN HÓA",
    "Bản chất và ý nghĩa sinh học của cơ chế Điều hòa Tương hỗ (Reciprocal Regulation) giữa AMP và GMP là gì?",
    [
        "<b>Kiểm soát chéo năng lượng —</b> Tổng hợp AMP cần năng lượng từ GTP; ngược lại, tổng hợp GMP cần năng lượng từ ATP.",
        "<b>Cơ chế tự cân bằng —</b> Khi tế bào dư thừa GTP → kích hoạt mạnh mẽ tổng hợp AMP; khi tế bào dư thừa ATP → kích hoạt mạnh mẽ tổng hợp GMP.",
        "<b>Ý nghĩa sinh học —</b> Đảm bảo hai loại nucleotide purin luôn luôn được sản xuất với tỷ lệ cân bằng xấp xỉ 1:1, sẵn sàng cho sự tái bản DNA và phiên mã RNA mà không gây đột biến lệch cặp."
    ],
    "Sự mất cân đối giữa các bể chứa dNTP nội bào là một trong những nguyên nhân hàng đầu gây đột biến sao chép và chết tế bào."
))

cards.append(make_card(
    "HS12-B2-10",
    "Hệ thống Điều hòa Dị lập thể Đa tầng của Con đường Purin",
    "ĐIỀU HÒA CHUYỂN HÓA",
    "Con đường tân tạo Purin De Novo được kiểm soát bởi các mức độ ức chế dị lập thể nào?",
    [
        "<b>Tầng 1 (PRPP Synthetase) —</b> Bị ức chế dị lập thể bởi ADP và GDP.",
        "<b>Tầng 2 (Glutamine-PRPP Amidotransferase) —</b> Bị ức chế feedback hiệp đồng mạnh mẽ bởi AMP, GMP và IMP; kích hoạt bởi PRPP.",
        "<b>Tầng 3 (Phân nhánh IMP) —</b> AMP ức chế Adenylosuccinate Synthetase; GMP ức chế IMP Dehydrogenase.",
        "<b>Ý nghĩa —</b> Hệ thống kiểm soát đa tầng đảm bảo tế bào không lãng phí năng lượng tổng hợp purin khi nguồn nucleotide đã dồi dào."
    ],
    "Khi cả AMP và GMP cùng tích lũy, chúng ức chế enzyme GPA ở hai vị trí dị lập thể riêng biệt, tạo ra hiệu ứng ức chế hiệp đồng (synergistic inhibition) mạnh gấp bội."
))

cards.append(make_card(
    "HS12-B2-11",
    "Cơ chế Dược lý của Mycophenolate Mofetil (MMF)",
    "DƯỢC LÝ & GHÉP TẠNG",
    "Cơ chế phân tử và ứng dụng lâm sàng của thuốc ức chế miễn dịch Mycophenolate Mofetil (MMF) là gì?",
    [
        "<b>Đích tác dụng —</b> Ức chế chọn lọc, thuận nghịch và không cạnh tranh enzyme IMP Dehydrogenase tại bào tương.",
        "<b>Hậu quả sinh hóa —</b> Cắt đứt sự chuyển hóa từ IMP thành XMP, làm cạn kiệt hoàn toàn nguồn GMP và dGTP nội bào.",
        "<b>Tính chọn lọc tế bào —</b> Lympho bào T và B phụ thuộc gần như tuyệt đối vào con đường tân tạo purin (không có con đường trục vớt hiệu quả) → bị ức chế phân chia chọn lọc.",
        "<b>Ứng dụng lâm sàng —</b> Thuốc trụ cột chống thải ghép cơ quan (ghép thận, tim, gan) và điều trị các bệnh tự miễn nặng như viêm thận Lupus."
    ],
    "Khác với tế bào lympho, các tế bào khác trong cơ thể có thể sử dụng con đường trục vớt purin nên ít bị độc tính của Mycophenolate mofetil hơn."
))

cards.append(make_card(
    "HS12-B2-12",
    "Chi phí Năng lượng của Con đường Purin De Novo",
    "SINH NĂNG LƯỢNG",
    "Chi phí năng lượng cao năng (ATP/GTP) cho việc tổng hợp 1 phân tử AMP hoặc GMP từ đầu là bao nhiêu?",
    [
        "<b>Tạo IMP —</b> Tiêu tốn ít nhất 6 liên kết phosphate cao năng (1 ATP tạo PRPP, 1 ATP tạo GAR, 1 ATP tạo FGAM, 1 ATP đóng vòng AIR, 1 ATP tạo CAIR, 1 ATP tạo SACAIR).",
        "<b>Từ IMP thành AMP —</b> Tiêu tốn thêm 1 phân tử GTP.",
        "<b>Từ IMP thành GMP —</b> Tiêu tốn thêm 1 phân tử ATP (thủy phân thành AMP + PPi tương đương 2 liên kết cao năng).",
        "<b>Ý nghĩa tiến hóa —</b> Tổng hợp de novo tiêu tốn năng lượng cực lớn (~7-8 ATP), giải thích vì sao tế bào luôn ưu tiên sử dụng con đường trục vớt (Salvage) tiết kiệm năng lượng khi có base tự do."
    ],
    "Sự tiến hóa của con đường trục vớt là một bước thích nghi năng lượng sống còn của tế bào sống, đặc biệt là ở những mô có nhu cầu trao đổi chất cao như não bộ."
))

# ==============================================================================
# SECTION B3: TRỤC VỚT PURIN & HỘI CHỨNG LESCH-NYHAN (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B3-01",
    "Nguyên lý và Ưu thế của Con đường Trục vớt Purin",
    "CON ĐƯỜNG TRỤC VỚT",
    "Nguyên lý phản ứng và ưu thế sinh học của Con đường Trục vớt Purin (Salvage Pathway) là gì?",
    [
        "<b>Nguyên lý chung —</b> Base Purin tự do + PRPP → Purin Nucleotide + PPi (xúc tác bởi enzyme Phosphoribosyltransferase).",
        "<b>Tái sử dụng nguyên liệu —</b> Tận dụng trực tiếp các base Adenin, Hypoxanthine và Guanin giải phóng từ quá trình thoái hóa acid nucleic nội bào.",
        "<b>Tiết kiệm năng lượng —</b> Chỉ tiêu tốn 1 phân tử PRPP cho mỗi nucleotide, không tiêu tốn chuỗi 11 phản ứng và 6-7 ATP như con đường tân tạo de novo.",
        "<b>Bảo vệ tế bào —</b> Ngăn cản sự tích lũy quá mức của các base purin tự do thoái hóa thành acid uric gây độc."
    ],
    "Thủy phân PPi bởi pyrophosphatase vô cơ giải phóng năng lượng lớn, kéo phản ứng trục vớt diễn ra hoàn toàn theo chiều tạo nucleotide."
))

cards.append(make_card(
    "HS12-B3-02",
    "Enzyme APRT và Bệnh Sỏi 2,8-Dihydroxyadenine",
    "CON ĐƯỜNG TRỤC VỚT",
    "Enzyme APRT xúc tác phản ứng nào và khiếm khuyết di truyền enzyme này dẫn tới bệnh lý gì?",
    [
        "<b>Phản ứng xúc tác —</b> Adenin + PRPP → AMP + PPi (xúc tác bởi Adenine Phosphoribosyltransferase - APRT).",
        "<b>Khiếm khuyết APRT —</b> Bệnh lý di truyền lặn trên nhiễm sắc thể thường gây thiếu hụt enzyme APRT.",
        "<b>Cơ chế bệnh sinh —</b> Adenin không được trục vớt bị enzyme Xanthine Oxidase oxy hóa thành 8-hydroxyadenine rồi thành 2,8-dihydroxyadenine (2,8-DHA).",
        "<b>Lâm sàng —</b> 2,8-DHA cực kỳ khó tan trong nước, kết tinh tạo thành sỏi đường tiết niệu 2,8-DHA (dễ nhầm với sỏi urat) gây suy thận."
    ],
    "Sỏi 2,8-DHA cũng không cản quang trên X-quang thường giống sỏi acid uric, nhưng điều trị bằng Allopurinol có thể ngăn cản sự hình thành 2,8-DHA từ adenin."
))

cards.append(make_card(
    "HS12-B3-03",
    "Hai Phản ứng Xúc tác của Enzyme HGPRT",
    "CON ĐƯỜNG TRỤC VỚT",
    "Enzyme HGPRT xúc tác hai phản ứng trục vớt nào trong tế bào?",
    [
        "<b>Trục vớt Hypoxanthine —</b> Hypoxanthine + PRPP → Inosine Monophosphate (IMP) + PPi.",
        "<b>Trục vớt Guanin —</b> Guanin + PRPP → Guanosine Monophosphate (GMP) + PPi.",
        "<b>Tên đầy đủ của enzyme —</b> Hypoxanthine-Guanine Phosphoribosyltransferase (HGPRT).",
        "<b>Ý nghĩa trung tâm —</b> Tái tạo đồng thời cả IMP và GMP, cung cấp nguồn nucleotide purin thiết yếu và kiểm soát nồng độ PRPP nội bào."
    ],
    "HGPRT không trục vớt Adenine. Khả năng tái chế cả hai purin quan trọng nhất làm cho HGPRT trở thành enzyme trục vớt then chốt nhất của cơ thể."
))

cards.append(make_card(
    "HS12-B3-04",
    "Sự Phụ thuộc Sinh tử của Não bộ vào Enzyme HGPRT",
    "HÓA SINH NÃO BỘ",
    "Tại sao tế bào thần kinh não bộ lại phụ thuộc sống còn vào con đường trục vớt qua HGPRT?",
    [
        "<b>Hoạt tính De Novo cực yếu —</b> Tế bào thần kinh não bộ (đặc biệt là các hạch nền - basal ganglia) có hoạt tính của các enzyme con đường tân tạo Purin de novo cực kỳ thấp.",
        "<b>Phụ thuộc Salvage —</b> Não bộ phụ thuộc gần như 100% vào con đường trục vớt qua enzyme HGPRT để duy trì nguồn nucleotide cho sự sống và phát triển synap.",
        "<b>Hệ Dopaminergic —</b> Thiếu hụt nucleotide purin tại não làm suy giảm nghiêm trọng sự phát triển và chức năng của các nơ-ron Dopaminergic tại thể vân (striatum)."
    ],
    "Đây là nguyên nhân cốt tử giải thích vì sao khi thiếu hụt enzyme HGPRT, biểu hiện tổn thương thần kinh và hành vi ngoại tháp lại xuất hiện cực kỳ nặng nề."
))

cards.append(make_card(
    "HS12-B3-05",
    "Di truyền học & Bản chất Phân tử Hội chứng Lesch-Nyhan",
    "BỆNH DI TRUYỀN",
    "Đặc điểm di truyền học và khiếm khuyết phân tử của Hội chứng Lesch-Nyhan là gì?",
    [
        "<b>Quy luật di truyền —</b> Di truyền lặn liên kết nhiễm sắc thể giới tính X (X-linked recessive), hầu như chỉ gặp ở trẻ trai.",
        "<b>Gen đột biến —</b> Đột biến mất chức năng trên gen HPRT1 nằm tại vị trí Xq26 - q27 trên nhánh dài nhiễm sắc thể X.",
        "<b>Hậu quả enzyme —</b> Thiếu hụt hoàn toàn hoặc gần như hoàn toàn (hoạt tính còn lại dưới 1.5 - 2%) enzyme HGPRT trong mọi mô của cơ thể.",
        "<b>Tần suất —</b> Hiếm gặp, khoảng 1 trên 380.000 trẻ sơ sinh sinh sống."
    ],
    "Mẹ của bệnh nhân thường là người mang gen dị hợp tử không có triệu chứng (trừ nguy cơ tăng nhẹ acid uric máu sau mãn kinh)."
))

cards.append(make_card(
    "HS12-B3-06",
    "Cơ chế Bùng nổ Tân tạo Purin De Novo trong Lesch-Nyhan",
    "BỆNH SINH PHÂN TỬ",
    "Tại sao thiếu hụt HGPRT trong Hội chứng Lesch-Nyhan lại làm tăng vọt con đường tân tạo Purin De Novo?",
    [
        "<b>Ứ đọng PRPP cơ chất —</b> Do HGPRT không hoạt động, PRPP không được sử dụng để trục vớt hypoxanthine và guanine, dẫn tới nồng độ PRPP nội bào tăng vọt gấp 10 - 20 lần.",
        "<b>Hoạt hóa GPA cực mạnh —</b> PRPP nồng độ cao là chất hoạt hóa dị lập thể cực mạnh đối với enzyme Glutamine-PRPP Amidotransferase (GPA).",
        "<b>Mất ức chế Feedback —</b> Nồng độ IMP và GMP nội bào suy giảm làm mất hoàn toàn sự ức chế feedback allosteric lên GPA.",
        "<b>Hậu quả —</b> Tốc độ con đường tân tạo purin de novo tăng vọt gấp nhiều lần, sản xuất một lượng purin dư thừa khổng lồ bị đẩy vào thoái hóa."
    ],
    "Đây là một nghịch lý sinh hóa kinh điển: mất con đường trục vớt lại dẫn tới bùng nổ con đường tân tạo, đẩy sản xuất acid uric lên mức ác tính."
))

cards.append(make_card(
    "HS12-B3-07",
    "Cơ chế Tăng Acid Uric Máu Ác tính trong Lesch-Nyhan",
    "BỆNH SINH PHÂN TỬ",
    "Cơ chế gây tăng acid uric máu ác tính ở bệnh nhân Hội chứng Lesch-Nyhan là gì?",
    [
        "<b>Nguồn 1 (Purin không được trục vớt) —</b> Toàn bộ lượng Hypoxanthine và Guanin giải phóng từ thoái hóa nội bào không thể tái chế, bị enzyme Xanthine Oxidase oxy hóa ồ ạt thành Acid Uric.",
        "<b>Nguồn 2 (Bùng nổ Purin De Novo) —</b> Lượng purin sản xuất dư thừa từ con đường tân tạo không thể tích lũy, tiếp tục bị thoái hóa tạo thêm một lượng khổng lồ Acid Uric.",
        "<b>Nồng độ huyết thanh —</b> Acid uric máu tăng vọt lên rất cao (> 600 - 1000 µmol/L), bài xuất acid uric niệu gấp nhiều lần bình thường.",
        "<b>Lắng đọng sớm —</b> Tinh thể urat kết tủa ngay trong những tháng đầu đời, gây sỏi thận urat và suy thận tiến triển."
    ],
    "Tăng sản xuất acid uric trong Lesch-Nyhan là một trong những mức tăng acid uric nội sinh cao nhất được ghi nhận trong y học."
))

cards.append(make_card(
    "HS12-B3-08",
    "Hành vi Tự Hủy hoại Bản thân trong Lesch-Nyhan",
    "LÂM SÀNG BSNT",
    "Đặc điểm và cơ chế của triệu chứng Hành vi Tự Hủy hoại Bản thân (Self-mutilation) trong Hội chứng Lesch-Nyhan là gì?",
    [
        "<b>Biểu hiện lâm sàng —</b> Khởi phát điển hình từ 2 - 3 tuổi; bệnh nhân có xung động tâm thần không thể cưỡng lại, tự cắn nát môi dưới, cắn đứt đầu ngón tay, đập đầu vào vật cứng.",
        "<b>Cảm giác đau đớn —</b> Bệnh nhân hoàn toàn cảm nhận được sự đau đớn và sợ hãi, thường la hét cầu xin người xung quanh giữ tay mình lại để không tự cắn.",
        "<b>Cơ chế phân tử —</b> Thiếu hụt nucleotide purin tại hạch nền não bộ gây thoái hóa và rối loạn chức năng nghiêm trọng của hệ dẫn truyền thần kinh Dopaminergic tại thể vân.",
        "<b>Xử trí bảo vệ —</b> Thường phải nhổ bỏ răng cửa hoặc bọc nẹp cố định tay để ngăn bệnh nhân tự làm tổn thương tàn tật."
    ],
    "Hành vi tự hủy hoại bản thân là dấu hiệu đặc trưng tuyệt đối (pathognomonic) của Hội chứng Lesch-Nyhan, không gặp ở bất kỳ rối loạn chuyển hóa purin nào khác."
))

cards.append(make_card(
    "HS12-B3-09",
    "Dấu hiệu Cát Cam Tã Lót và Biểu hiện Thận của Lesch-Nyhan",
    "LÂM SÀNG BSNT",
    "Dấu hiệu cảnh báo sớm nhất trên tã lót của trẻ mắc Lesch-Nyhan và các biến chứng thận là gì?",
    [
        "<b>Cặn lắng màu da cam (Orange sand) —</b> Trong những tháng đầu đời, cha mẹ phát hiện trên tã lót của trẻ có các vết cặn lắng màu da cam như hạt cát mịn (tinh thể acid uric kết tủa trong nước tiểu toan).",
        "<b>Sỏi đường tiết niệu —</b> Sỏi acid uric xuất hiện rất sớm, gây đái máu tái diễn, nhiễm khuẩn tiết niệu và tắc nghẽn niệu quản.",
        "<b>Viêm thận kẽ mạn tính —</b> Tinh thể urat lắng đọng trong tủy thận gây suy thận mạn tính tiến triển nếu không điều trị.",
        "<b>Gout vị thành niên —</b> Viêm khớp Gout cấp và hạt tophi xuất hiện rất sớm ngay ở lứa tuổi thiếu niên."
    ],
    "Dấu hiệu 'cát cam trên tã lót' là một gợi ý sinh hóa kinh điển giúp bác sĩ nhi khoa nghĩ ngay tới khiếm khuyết chuyển hóa purin trước khi các triệu chứng thần kinh bùng phát."
))

cards.append(make_card(
    "HS12-B3-10",
    "Hội chứng Kelley-Seegmiller vs Lesch-Nyhan",
    "CHẨN ĐOÁN PHÂN BIỆT",
    "Hội chứng Kelley-Seegmiller khác biệt gì so với Hội chứng Lesch-Nyhan cổ điển?",
    [
        "<b>Bản chất phân tử —</b> Cùng đột biến trên gen HPRT1, nhưng Kelley-Seegmiller chỉ gây thiếu hụt một phần hoạt tính HGPRT (hoạt tính còn lại khoảng 8 - 20%).",
        "<b>Biểu hiện lâm sàng —</b> Bệnh nhân có tăng acid uric máu nặng, sỏi urat thận tái diễn và bệnh Gout khởi phát sớm ở tuổi thanh niên.",
        "<b>Điểm khác biệt cốt tử —</b> Bệnh nhân Kelley-Seegmiller HOÀN TOÀN KHÔNG CÓ hành vi tự hủy hoại bản thân và chức năng thần kinh/trí tuệ bình thường hoặc chỉ suy giảm rất nhẹ.",
        "<b>Ý nghĩa —</b> Chỉ cần duy trì được một lượng nhỏ hoạt tính HGPRT (> 8%) là đủ để bảo vệ các nơ-ron hạch nền khỏi tổn thương thoái hóa dopaminergic."
    ],
    "Kelley-Seegmiller là thể nhẹ của khiếm khuyết HGPRT, minh chứng cho mối tương quan chặt chẽ giữa mức độ hoạt tính enzyme còn sót lại và kiểu hình lâm sàng."
))

# ==============================================================================
# SECTION B4: THOÁI HÓA PURIN & MẤT URICASE Ở NGƯỜI (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B4-01",
    "Con đường Thoái hóa AMP thành Hypoxanthine",
    "THOÁI HÓA PURIN",
    "Chuỗi phản ứng thoái hóa từ AMP thành Hypoxanthine diễn ra qua các enzyme nào?",
    [
        "<b>Bước 1 (Khử phosphate) —</b> AMP bị enzyme 5'-Nucleotidase thủy phân cắt bỏ gốc phosphate tạo thành Adenosine.",
        "<b>Bước 2 (Khử amin) —</b> Adenosine bị enzyme Adenosine Deaminase (ADA) khử nhóm amin tạo thành Inosine.",
        "<b>Bước 3 (Phosphoryl phân) —</b> Inosine bị Purine Nucleoside Phosphorylase (PNP) cắt liên kết N-glycosidic giải phóng base Hypoxanthine và Ribose-1-P.",
        "<b>Con đường phụ —</b> AMP cũng có thể bị khử amin trực tiếp bởi AMP Deaminase tạo IMP, sau đó IMP bị 5'-nucleotidase khử phosphate tạo Inosine."
    ],
    "Enzyme Adenosine Deaminase (ADA) là mắt xích sống còn trong con đường này, có vai trò bảo vệ tế bào miễn dịch khỏi tích lũy độc chất deoxyadenosine."
))

cards.append(make_card(
    "HS12-B4-02",
    "Cơ chế Bệnh sinh Bệnh SCID do Thiếu hụt ADA",
    "MIỄN DỊCH HÓA SINH",
    "Tại sao thiếu hụt enzyme Adenosine Deaminase (ADA) lại gây Bệnh suy giảm miễn dịch kết hợp trầm trọng (SCID)?",
    [
        "<b>Tích lũy độc chất —</b> Khi thiếu ADA, Adenosine và Deoxyadenosine không thể thoái hóa, bị các kinase tế bào phosphoryl hóa ngược thành dATP nồng độ cao.",
        "<b>Ức chế Ribonucleotide Reductase —</b> dATP nồng độ cao là chất ức chế dị lập thể allosteric toàn bộ enzyme Ribonucleotide Reductase (RNR).",
        "<b>Ngừng trệ tổng hợp DNA —</b> RNR bị phong bế làm cạn kiệt các dNTP khác (dCTP, dGTP, dTTP), ngăn cản hoàn toàn việc nhân đôi DNA.",
        "<b>Hậu quả lâm sàng —</b> Chết tế bào lympho T và B chọn lọc, gây suy giảm miễn dịch cả dịch thể và qua trung gian tế bào (Hội chứng em bé trong bong bóng)."
    ],
    "SCID do thiếu ADA là bệnh lý đầu tiên trên thế giới được điều trị thành công bằng liệu pháp gen (Gene Therapy) vào năm 1990."
))

cards.append(make_card(
    "HS12-B4-03",
    "Con đường Thoái hóa GMP thành Xanthine",
    "THOÁI HÓA PURIN",
    "Chuỗi phản ứng thoái hóa từ GMP thành Xanthine diễn ra qua các enzyme nào?",
    [
        "<b>Bước 1 (Khử phosphate) —</b> GMP bị enzyme 5'-Nucleotidase thủy phân cắt bỏ nhóm phosphate tạo thành Guanosine.",
        "<b>Bước 2 (Phosphoryl phân) —</b> Guanosine bị enzyme Purine Nucleoside Phosphorylase (PNP) cắt liên kết N-glycosidic giải phóng base Guanin tự do và Ribose-1-P.",
        "<b>Bước 3 (Khử amin) —</b> Guanin bị enzyme Guanase (Guanine deaminase) xúc tác khử nhóm amin giải phóng NH4+ và tạo thành Xanthine.",
        "<b>Hội tụ —</b> Tại phân tử Xanthine, nhánh thoái hóa của GMP hội tụ với nhánh thoái hóa của AMP (Hypoxanthine → Xanthine)."
    ],
    "Cả hai nhánh AMP và GMP đều hội tụ về sản phẩm chung là Xanthine, trước khi chịu sự oxy hóa tiếp theo của Xanthine Oxidase."
))

cards.append(make_card(
    "HS12-B4-04",
    "Cấu trúc Phân tử và Đồng yếu tố của Xanthine Oxidase",
    "ENZYME HỌC",
    "Cấu trúc phân tử và các cofactor xúc tác của enzyme Xanthine Oxidase (XO) gồm những gì?",
    [
        "<b>Bản chất enzyme —</b> Là một metalloenzyme homodimer phức tạp kích thước lớn (~290 kDa) khu trú chủ yếu tại gan và ruột non.",
        "<b>Các trung tâm xúc tác —</b> Mỗi tiểu phần chứa: 1 tâm Molypden (Moco - Molybdopterin), 2 trung tâm Sắt - Lưu huỳnh ([2Fe-2S]), và 1 phân tử FAD.",
        "<b>Dòng truyền electron —</b> Cơ chất chuyển electron cho nguyên tử Molypden (Mo VI → Mo IV) → truyền qua trung tâm [2Fe-2S] → đến FAD → FAD khử O2 thành H2O2 hoặc superoxide O2•-.",
        "<b>Dạng enzyme —</b> Có thể tồn tại ở dạng Xanthine Dehydrogenase (dùng NAD+) hoặc chuyển hóa thành Xanthine Oxidase (dùng O2)."
    ],
    "Tâm Molypden chính là đích gắn và bị khóa bất thuận nghịch bởi chất ức chế tự sát Oxypurinol (chuyển hóa từ Allopurinol)."
))

cards.append(make_card(
    "HS12-B4-05",
    "Hai Bước Phản ứng Xúc tác bởi Xanthine Oxidase",
    "THOÁI HÓA PURIN",
    "Enzyme Xanthine Oxidase xúc tác liên tiếp hai bước phản ứng oxy hóa nào?",
    [
        "<b>Bước 1 (Hypoxanthine → Xanthine) —</b> Hypoxanthine + O2 + H2O → Xanthine + H2O2 (đưa nhóm =O vào vị trí carbon số 2).",
        "<b>Bước 2 (Xanthine → Acid Uric) —</b> Xanthine + O2 + H2O → Acid Uric + H2O2 (đưa nhóm =O vào vị trí carbon số 8).",
        "<b>Sản phẩm phụ ROS —</b> Cả hai bước đều tạo ra Hydrogen peroxide (H2O2) và các gốc tự do oxy hóa (superoxide), đóng góp vào hiện tượng stress oxy hóa nội mạc.",
        "<b>Tính bất thuận nghịch —</b> Cả hai phản ứng đều là phản ứng oxy hóa một chiều trong điều kiện sinh lý."
    ],
    "Acid Uric (2,6,8-trioxypurine) là dạng oxy hóa cao nhất của nhân purin trong cơ thể con người."
))

cards.append(make_card(
    "HS12-B4-06",
    "Dạng Tồn tại và Hằng số Phân ly pKa của Acid Uric",
    "HÓA LÝ SINH HỌC",
    "Dạng tồn tại của Acid Uric trong máu và nước tiểu phụ thuộc vào hằng số phân ly pKa như thế nào?",
    [
        "<b>Hằng số phân ly —</b> Acid Uric là một acid yếu có pKa1 = 5.75.",
        "<b>Ở pH máu sinh lý (pH = 7.40) —</b> pH máu cao hơn pKa rất nhiều, do đó trên 98% acid uric bị phân ly thành ion Urat, kết hợp với ion Natri tạo muối Monosodium Urate (MSU) hòa tan.",
        "<b>Ở pH nước tiểu toan (pH < 5.5) —</b> pH nước tiểu thấp hơn pKa, phần lớn urat chuyển ngược thành dạng Acid Uric không phân ly.",
        "<b>Ý nghĩa độ tan —</b> Acid Uric tự do có độ tan kém hơn muối MSU rất nhiều (chỉ tan khoảng 15 mg/L ở pH 5.0) → dễ dàng kết tinh thành sỏi thận acid uric trong nước tiểu toan."
    ],
    "Nguyên lý kiềm hóa nước tiểu (nâng pH nước tiểu lên 6.5 - 7.0 bằng bicarbonate hoặc natri citrat) dựa trên việc chuyển acid uric thành dạng urat hòa tan tốt hơn gấp nhiều lần."
))

cards.append(make_card(
    "HS12-B4-07",
    "Giới hạn Hòa tan Bão hòa của Tinh thể MSU trong Huyết tương",
    "BỆNH SINH GOUT",
    "Ngưỡng hòa tan bão hòa của tinh thể Monosodium Urate (MSU) trong máu là bao nhiêu?",
    [
        "<b>Ngưỡng bão hòa tại 37°C —</b> Giới hạn hòa tan tối đa của MSU trong huyết tương là 6.8 mg/dL (tương đương 404 - 420 µmol/L).",
        "<b>Định nghĩa Tăng Acid Uric máu —</b> Khi nồng độ vượt quá ngưỡng bão hòa: Nam giới > 420 µmol/L (> 7.0 mg/dL); Nữ giới tiền mãn kinh > 360 µmol/L (> 6.0 mg/dL).",
        "<b>Vai trò của Estrogen —</b> Estrogen ở nữ giới ức chế tái hấp thu urat tại ống thận qua kênh URAT1, giúp tăng đào thải urat và duy trì nồng độ máu thấp hơn nam giới.",
        "<b>Trạng thái quá bão hòa —</b> Khi vượt quá 6.8 mg/dL, huyết tương ở trạng thái dung dịch quá bão hòa, tạo nguy cơ kết tủa tinh thể urat tại các mô."
    ],
    "Sau mãn kinh, do suy giảm nồng độ estrogen, mức acid uric máu ở nữ giới tăng dần và tiệm cận mức của nam giới, làm gia tăng tỷ lệ mắc Gout ở phụ nữ cao tuổi."
))

cards.append(make_card(
    "HS12-B4-08",
    "Đột biến Mất Uricase (Urate Oxidase) ở Người & Vượn người",
    "TIẾN HÓA HỌC",
    "Tại sao con người và các loài vượn người không thể thoái hóa tiếp Acid Uric?",
    [
        "<b>Đột biến gen UOX —</b> Trong kỷ Miocen (khoảng 15 - 20 triệu năm trước), tổ tiên loài người và vượn người cấp cao (Hominoids) đã trải qua các đột biến vô nghĩa gây bất hoạt vĩnh viễn gen Urate Oxidase (UOX).",
        "<b>Gen giả (Pseudogene) —</b> Gen UOX ở người hiện là một gen giả không còn khả năng dịch mã tạo enzyme Uricase.",
        "<b>Hậu quả sinh hóa —</b> Con người hoàn toàn không có enzyme Uricase, biến Acid Uric thành sản phẩm chuyển hóa cuối cùng của nhân Purin.",
        "<b>Nồng độ máu cao —</b> Mức acid uric máu của loài người cao gấp 10 lần các loài động vật có vú khác và tiệm cận sát giới hạn bão hòa."
    ],
    "Sự biến mất của enzyme Uricase là yếu tố cơ bản biến con người thành loài duy nhất trong giới động vật có vú tự phát phát triển bệnh Gout trong tự nhiên."
))

cards.append(make_card(
    "HS12-B4-09",
    "So sánh Thoái hóa Purin ở các Loài Động vật",
    "HÓA SINH SO SÁNH",
    "Sản phẩm thoái hóa purin cuối cùng ở các nhóm động vật khác nhau trong sinh giới là gì?",
    [
        "<b>Động vật có vú khác —</b> Có enzyme Uricase oxy hóa acid uric thành Allantoin (chất tan trong nước gấp 100 lần acid uric, đào thải dễ dàng qua thận).",
        "<b>Cá xương (Teleosts) —</b> Allantoin tiếp tục bị Allantoinase thủy phân mở vòng tạo thành Allantoat.",
        "<b>Động vật lưỡng cư & cá sụn —</b> Allantoat bị phân cắt thành Urê và Glyoxylate.",
        "<b>Động vật không xương sống biển —</b> Urê tiếp tục bị Urease thủy phân triệt để thành ion Amoniac (NH4+) và CO2."
    ],
    "Sự thoái hóa purin thể hiện một chuỗi bậc thang tiến hóa ngược: động vật bậc thấp phân giải purin hoàn toàn tới NH4+, trong khi động vật linh trưởng bậc cao lại dừng lại ở acid uric."
))

cards.append(make_card(
    "HS12-B4-10",
    "Lợi thế Tiến hóa của Nồng độ Acid Uric Cao ở Người",
    "TIẾN HÓA HỌC",
    "Giả thuyết tiến hóa nào giải thích việc loài người giữ lại mức Acid Uric máu rất cao?",
    [
        "<b>Chất chống oxy hóa mạnh —</b> Acid Uric là chất chống oxy hóa nội sinh cực mạnh trong huyết tương, chịu trách nhiệm dập tắt hơn 50% tổng lượng gốc tự do trong máu người, bảo vệ tế bào khỏi tổn thương oxy hóa và kéo dài tuổi thọ.",
        "<b>Duy trì huyết áp khi đứng thẳng —</b> Acid Uric kích hoạt hệ Renin - Angiotensin và kích thích thần kinh giao cảm giúp duy trì huyết áp động mạch khi tổ tiên loài người chuyển sang tư thế đi đứng thẳng hai chân trong môi trường khan hiếm muối.",
        "<b>Bảo vệ thần kinh —</b> Nồng độ acid uric cao có tương quan nghịch với nguy cơ mắc bệnh thoái hóa thần kinh như Parkinson và Alzheimer."
    ],
    "Đây là một ví dụ kinh điển về tính đa hiệu đối kháng (antagonistic pleiotropy): đem lại lợi thế sinh tồn trong độ tuổi sinh sản nhưng gây bệnh Gout ở lứa tuổi sau sinh sản."
))

# ==============================================================================
# SECTION B5: BỆNH SINH BỆNH GOUT & CƠ CHẾ DƯỢC LÝ (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B5-01",
    "Hai Nhóm Căn nguyên Tăng Acid Uric Máu",
    "BỆNH SINH GOUT",
    "Phân loại hai nhóm căn nguyên chính dẫn tới tình trạng Tăng Acid Uric Máu?",
    [
        "<b>Nhóm Giảm đào thải qua thận (Chiếm 90% trường hợp) —</b> Suy thận mạn, thuốc lợi tiểu (Thiazide, Furosemide), Aspirin liều thấp, nhiễm toan ceton hoặc nhiễm toan lactic (cạnh tranh kênh bài tiết urat), rượu bia.",
        "<b>Nhóm Tăng sinh tổng hợp (Chiếm 10% trường hợp) —</b> Đột biến tăng hoạt PRPP Synthetase, thiếu HGPRT (Lesch-Nyhan), bệnh Von Gierke (GSD-I), chế độ ăn quá nhiều purin (thịt đỏ, phủ tạng, bia rượu).",
        "<b>Tăng hủy hoại tế bào —</b> Bệnh lý huyết học ác tính, hóa trị ung thư gây Hội chứng Ly giải khối u (Tumor Lysis Syndrome), bệnh vẩy nến thể rộng.",
        "<b>Ý nghĩa lâm sàng —</b> Xác định cơ chế (tăng tạo hay giảm thải qua định lượng acid uric niệu 24 giờ) giúp định hướng lựa chọn nhóm thuốc hạ acid uric phù hợp."
    ],
    "Rượu bia tác động kép: vừa làm tăng dị hóa ATP thành AMP ở gan làm tăng tạo acid uric, vừa tạo nhiều acid lactic ức chế đào thải urat tại ống thận."
))

cards.append(make_card(
    "HS12-B5-02",
    "Vận chuyển Acid Uric tại Ống Lượn Gần Thận",
    "SINH LÝ THẬN",
    "Acid Uric được xử lý qua 4 bước vận chuyển nào tại ống lượn gần thận?",
    [
        "<b>Bước 1 (Lọc cầu thận) —</b> Acid Uric được lọc tự do qua màng lọc cầu thận vào khoang Bowman.",
        "<b>Bước 2 (Tái hấp thu sớm) —</b> Tái hấp thu gần như hoàn toàn (98 - 100%) tại đoạn đầu ống lượn gần qua các kênh vận chuyển URAT1 (SLC22A12) và GLUT9 (SLC2A9).",
        "<b>Bước 3 (Bài tiết tích cực) —</b> Bài tiết khoảng 50% urat từ máu vào lại lòng ống qua các kênh OAT1, OAT3 và ABCG2.",
        "<b>Bước 4 (Tái hấp thu muộn) —</b> Tái hấp thu sau bài tiết khoảng 40 - 44% tại đoạn sau ống lượn gần.",
        "<b>Bài xuất thực tế —</b> Lượng acid uric bài xuất ra nước tiểu cuối cùng chỉ chiếm khoảng 8 - 12% lượng lọc ban đầu."
    ],
    "Kênh đồng vận chuyển anion-urat URAT1 tại bờ bàn chải ống lượn gần là đích tác động chọn lọc của nhóm thuốc tăng bài xuất urat (Probenecid, Benzbromarone)."
))

cards.append(make_card(
    "HS12-B5-03",
    "Vì sao Cơn Gout Cấp Thường Gặp ở Khớp Bàn Ngón Chân Cái",
    "BỆNH SINH GOUT",
    "Các yếu tố lý hóa nào giải thích việc tinh thể MSU ưu tiên kết tinh tại khớp bàn ngón chân cái (Podagra)?",
    [
        "<b>Nhiệt độ ngoại vi thấp —</b> Nhiệt độ tại ngón chân xa tim chỉ khoảng 30 - 32°C (so với 37°C ở trung tâm); độ tan của tinh thể MSU giảm mạnh khi nhiệt độ giảm.",
        "<b>Áp lực dòng máu và vi chấn thương —</b> Khớp bàn ngón chân cái chịu tải trọng cơ học lớn nhất khi đi lại, dễ xảy ra các vi chấn thương sụn khớp tạo nhân kết tinh.",
        "<b>Tái hấp thu nước dịch khớp về đêm —</b> Ban đêm khi nằm ngủ, nước trong dịch khớp bị tái hấp thu nhanh hơn urat, làm nồng độ urat tại chỗ tăng vọt tạm thời.",
        "<b>Toan hóa nhẹ dịch khớp —</b> Chuyển hóa kỵ khí tại mô khớp ngoại vi làm giảm nhẹ pH, thúc đẩy sự tạo nhân tinh thể."
    ],
    "Sự kết hợp giữa nhiệt độ thấp và nồng độ muối cao làm cho dịch khớp bàn ngón 1 trở thành vị trí đầu tiên vượt ngưỡng kết tinh vi tinh thể MSU hình kim."
))

cards.append(make_card(
    "HS12-B5-04",
    "Kích hoạt Thể viêm NLRP3 Inflammasome trong Cơn Gout Cấp",
    "MIỄN DỊCH BỆNH SINH",
    "Chuỗi sự kiện phân tử kích hoạt phức hợp Thể viêm NLRP3 Inflammasome trong cơn Gout cấp là gì?",
    [
        "<b>Thực bào tinh thể MSU —</b> Đại thực bào màng hoạt dịch khớp nuốt các vi tinh thể MSU hình kim nhọn qua cơ chế thực bào.",
        "<b>Vỡ màng tiêu thể (Lysosome) —</b> Tinh thể hình kim làm tổn thương cơ học và đâm thủng màng lysosome, giải phóng enzyme protease Cathepsin B vào bào tương.",
        "<b>Lắp ráp NLRP3 —</b> Cathepsin B và sự thoát ion Kali (K+ efflux) kích hoạt sự lắp ráp phức hợp Thể viêm NLRP3 Inflammasome (gồm cảm biến NLRP3, protein tiếp hợp ASC và Procaspase-1).",
        "<b>Hoạt hóa Caspase-1 —</b> Phức hợp NLRP3 xúc tác cắt Procaspase-1 thành enzyme Caspase-1 hoạt tính.",
        "<b>Giải phóng IL-1beta —</b> Caspase-1 phân cắt tiền chất pro-IL-1beta thành Interleukin-1beta (IL-1beta) hoạt tính phóng thích ồ ạt ra ngoài tế bào."
    ],
    "NLRP3 Inflammasome là trung tâm chỉ huy của đáp ứng viêm bẩm sinh trong bệnh Gout, biến kích thích hóa lý (tinh thể muối) thành bão cytokine gây viêm."
))

cards.append(make_card(
    "HS12-B5-05",
    "Vai trò của IL-1beta và Bạch cầu Đa nhân Trung tính",
    "BỆNH SINH GOUT",
    "Vai trò của Interleukin-1beta (IL-1beta) và Bạch cầu đa nhân trung tính trong cơn Gout cấp tính là gì?",
    [
        "<b>Tác động của IL-1beta —</b> Kích hoạt tế bào nội mô mao mạch màng hoạt dịch tăng biểu hiện phân tử kết dính (E-selectin, ICAM-1) và tiết hóa ứng động bạch cầu CXCL8 (IL-8).",
        "<b>Huy động Neutrophils —</b> Hàng triệu bạch cầu đa nhân trung tính từ tuần hoàn ùa vào khoang dịch khớp.",
        "<b>Thực bào và bùng nổ viêm —</b> Neutrophils thực bào tinh thể MSU, giải phóng ồ ạt các enzyme tiêu thể, gốc tự do oxy hóa (ROS), Prostaglandin và bẫy ngoại bào (NETs).",
        "<b>Lâm sàng —</b> Khớp sưng to, nóng bỏng, đỏ ửng và đau đớn dữ dội đến mức không chạm được vào ga trải giường (cơn viêm khớp Gout cấp)."
    ],
    "Neutrophil là 'kẻ thi hành' chính gây ra các triệu chứng lâm sàng rầm rộ của cơn Gout cấp; dập tắt sự xâm nhập của neutrophil là mục tiêu hàng đầu của Colchicine."
))

cards.append(make_card(
    "HS12-B5-06",
    "Bản chất Mô bệnh học của Hạt Tophi và Sỏi Acid Uric",
    "GIẢI PHẪU BỆNH GOUT",
    "Bản chất mô bệnh học của Hạt Tophi và đặc điểm của sỏi thận do Acid Uric là gì?",
    [
        "<b>Hạt Tophi —</b> Là các u hạt viêm mạn tính hình thành do lắng đọng khối lớn tinh thể urat tại sụn và mô mềm, bao quanh bởi phản ứng viêm tế bào khổng lồ đa nhân ăn dị vật (Foreign body giant cells) và mô xơ sẹo.",
        "<b>Vị trí tophi thường gặp —</b> Vành tai, quanh khớp bàn ngón chân cái, gân gót Achille, bao gân mu bàn tay, gây biến dạng và tiêu hủy xương khớp.",
        "<b>Sỏi thận Acid Uric —</b> Hình thành trong môi trường nước tiểu toan (pH < 5.5) làm acid uric kết tinh thành sỏi.",
        "<b>Đặc tính X-quang sống còn —</b> Sỏi acid uric KHÔNG CẢN QUANG trên phim X-quang thường (không nhìn thấy được, phân biệt với sỏi calci cản quang), chỉ phát hiện được qua siêu âm hoặc chụp CT-scan."
    ],
    "Hạt tophi là dấu hiệu của bệnh Gout mạn tính tiến triển nặng, đóng vai trò như một kho dự trữ urat khổng lồ liên tục hòa tan vào máu."
))

cards.append(make_card(
    "HS12-B5-07",
    "Cơ chế Cơ chất Tự sát của Allopurinol",
    "DƯỢC LÝ ĐIỀU TRỊ GOUT",
    "Tại sao Allopurinol được gọi là 'Cơ chất tự sát' (Suicide Substrate) của enzyme Xanthine Oxidase?",
    [
        "<b>Cấu trúc đồng phân —</b> Allopurinol là đồng phân cấu trúc của hypoxanthine (đổi chỗ nguyên tử carbon 7 và nitơ 8).",
        "<b>Bị oxy hóa thành Oxypurinol —</b> Ban đầu Allopurinol đóng vai trò là cơ chất gắn vào tâm hoạt động của Xanthine Oxidase và bị enzyme oxy hóa thành Oxypurinol (Alloxanthine).",
        "<b>Khóa tâm Molypden —</b> Oxypurinol có ái lực cực mạnh, gắn chặt không thuận nghịch vào ion Molypden ở trạng thái khử Mo(IV) tại tâm xúc tác của enzyme, phong bế vĩnh viễn Xanthine Oxidase.",
        "<b>Hậu quả sinh hóa —</b> Dập tắt sản xuất acid uric; các tiền chất tích lũy là Hypoxanthine và Xanthine có độ tan trong nước cao gấp nhiều lần acid uric nên dễ dàng đào thải an toàn qua nước tiểu."
    ],
    "Cơ chế ức chế dựa trên cơ chế (Mechanism-based inhibition / suicide inhibition) giúp Allopurinol có hiệu lực ức chế cực kỳ bền vững kéo dài ngay cả khi nồng độ thuốc trong máu đã giảm."
))

cards.append(make_card(
    "HS12-B5-08",
    "Cảnh báo An toàn Alen HLA-B*58:01 với Allopurinol",
    "DƯỢC DI TRUYỀN HỌC",
    "Nguy cơ lâm sàng của alen HLA-B*58:01 khi sử dụng thuốc Allopurinol là gì?",
    [
        "<b>Phản ứng quá mẫn nặng (SCARs) —</b> Người mang alen HLA-B*5801 có nguy cơ rất cao bị hội chứng quá mẫn nghiêm trọng với Allopurinol, bao gồm Hội chứng Stevens-Johnson (SJS), Hoại tử thượng bì nhiễm độc (TEN) và Hội chứng DRESS.",
        "<b>Tỷ lệ tử vong cao —</b> Hội chứng SJS/TEN do Allopurinol có tỷ lệ tử vong lên tới 20 - 30% do hoại tử da niêm mạc diện rộng và suy đa tạng.",
        "<b>Dịch tễ học —</b> Tần suất mang alen HLA-B*5801 rất cao ở người gốc Việt Nam, người Hán và người Đông Nam Á (khoảng 8 - 15%).",
        "<b>Khuyến cáo lâm sàng —</b> Sàng lọc xét nghiệm gen HLA-B*5801 trước khi khởi đầu điều trị Allopurinol cho bệnh nhân có nguy cơ cao; nếu dương tính, chuyển sang dùng Febuxostat."
    ],
    "Đây là một trong những chỉ định xét nghiệm dược di truyền học (Pharmacogenomics) quan trọng nhất trong thực hành chuyên khoa Cơ Xương Khớp tại Việt Nam."
))

cards.append(make_card(
    "HS12-B5-09",
    "Cơ chế và Ưu điểm của Febuxostat",
    "DƯỢC LÝ ĐIỀU TRỊ GOUT",
    "Cơ chế tác dụng phân tử và ưu điểm lâm sàng của Febuxostat so với Allopurinol là gì?",
    [
        "<b>Bản chất hóa học —</b> Là chất ức chế chọn lọc không mang nhân purin (Non-purine selective inhibitor).",
        "<b>Cơ chế gắn —</b> Gắn chặn trực tiếp vào rãnh dẫn tới tâm hoạt động của Xanthine Oxidase, khóa chặt cả dạng oxy hóa Mo(VI) và dạng khử Mo(IV) của enzyme.",
        "<b>Hiệu lực ức chế —</b> Ức chế mạnh mẽ và chọn lọc hơn Allopurinol, hạ acid uric máu nhanh và sâu hơn.",
        "<b>Ưu điểm lâm sàng —</b> Không gây phản ứng dị ứng qua trung gian alen HLA-B*5801; chuyển hóa chủ yếu qua gan nên an toàn, không cần chỉnh liều ở bệnh nhân suy thận nhẹ đến vừa."
    ],
    "Febuxostat là lựa chọn hàng đầu thay thế Allopurinol ở bệnh nhân dị ứng Allopurinol, bệnh nhân mang alen HLA-B*5801 hoặc bệnh nhân suy giảm chức năng thận."
))

cards.append(make_card(
    "HS12-B5-10",
    "Cơ chế Nhóm Tăng Bài xuất Urat qua Thận: Probenecid",
    "DƯỢC LÝ ĐIỀU TRỊ GOUT",
    "Cơ chế phân tử và các lưu ý lâm sàng của thuốc tăng đào thải acid uric Probenecid là gì?",
    [
        "<b>Đích tác động —</b> Ức chế chọn lọc protein đồng vận chuyển tái hấp thu urat URAT1 (SLC22A12) và GLUT9 tại màng đỉnh tế bào ống lượn gần.",
        "<b>Tác dụng sinh hóa —</b> Ngăn cản tái hấp thu urat từ dịch lòng ống vào máu, làm tăng tống khứ acid uric ra ngoài theo nước tiểu.",
        "<b>Chống chỉ định —</b> Chống chỉ định ở bệnh nhân có tiền sử sỏi thận acid uric, suy giảm chức năng thận (eGFR < 30 mL/phút) hoặc nhóm tăng sinh tổng hợp acid uric (acid uric niệu > 800 mg/24h).",
        "<b>Nguyên tắc sử dụng —</b> Bắt buộc bệnh nhân phải uống nhiều nước (> 2 lít/ngày) và phối hợp kiềm hóa nước tiểu để tránh nguy cơ kết tủa tạo sỏi urat cấp trong đường niệu."
    ],
    "Probenecid cũng ức chế bài tiết kháng sinh nhóm beta-lactam (Penicillin) qua thận, từng được dùng trong Thế chiến II để kéo dài thời gian bán thải của Penicillin."
))

cards.append(make_card(
    "HS12-B5-11",
    "Cơ chế Tiêu Urat của Enzyme Tái tổ hợp Pegloticase",
    "DƯỢC LÝ ĐIỀU TRỊ GOUT",
    "Cơ chế tác dụng phân tử và chỉ định của thuốc tiêu urat tái tổ hợp Pegloticase là gì?",
    [
        "<b>Bản chất sinh học —</b> Là enzyme Urate Oxidase (Uricase) tái tổ hợp từ nấm men, được gắn thêm các chuỗi Polyethylene Glycol (PEG hóa) để giảm tính sinh miễn dịch và kéo dài thời gian bán thải.",
        "<b>Phản ứng xúc tác —</b> Acid Uric + O2 + H2O → Allantoin + H2O2 + CO2.",
        "<b>Ưu thế của Allantoin —</b> Allantoin có độ tan trong nước cao gấp gần 100 lần acid uric, không bao giờ kết tinh và đào thải cực nhanh qua nước tiểu.",
        "<b>Chỉ định lâm sàng —</b> Dùng đường truyền tĩnh mạch cho bệnh nhân Gout mạn tính kháng trị nặng có hạt tophi khổng lồ phá hủy khớp, hoặc Rasburicase dự phòng hội chứng ly giải khối u."
    ],
    "Pegloticase có thể hòa tan nhanh chóng các hạt tophi lâu năm chỉ sau vài tháng điều trị, nhưng cần theo dõi kháng thể kháng thuốc có thể gây phản ứng phản vệ."
))

cards.append(make_card(
    "HS12-B5-12",
    "Cơ chế Colchicine & Bùng phát Cơn Gout Cấp khi Khởi đầu ULT",
    "DƯỢC LÝ & LÂM SÀNG",
    "Cơ chế tác dụng của Colchicine và giải thích hiện tượng bùng phát cơn Gout cấp khi mới bắt đầu dùng thuốc hạ acid uric?",
    [
        "<b>Cơ chế Colchicine —</b> Gắn với ái lực cao vào tiểu đơn vị beta-tubulin, ức chế sự trùng hợp vi ống tế bào (microtubules) → ngăn chặn sự biến dạng, hóa ứng động di chuyển và thực bào của Neutrophil vào ổ khớp, dập tắt thể viêm NLRP3.",
        "<b>Cơ chế bùng phát cơn cấp do thuốc —</b> Khi bắt đầu dùng Allopurinol/Febuxostat, acid uric máu hạ nhanh làm thay đổi cân bằng dung dịch → hòa tan lớp ngoài của các ổ tophi cũ → các khối tinh thể bị nứt vỡ, giải phóng các vi tinh thể MSU trần vào dịch khớp kích hoạt đợt viêm cấp mới.",
        "<b>Chiến lược dự phòng bắt buộc —</b> (1) Không khởi đầu thuốc hạ urat ngay trong cơn cấp; (2) Bắt đầu liều thấp tăng dần; (3) Bắt buộc phối hợp Colchicine liều thấp (0.5 - 1 mg/ngày) dự phòng trong 3 - 6 tháng đầu."
    ],
    "Nếu không được giải thích trước, bệnh nhân có thể nghĩ thuốc làm bệnh nặng hơn và tự ý bỏ điều trị. Phối hợp Colchicine dự phòng là tiêu chuẩn vàng trong mọi guideline điều trị Gout."
))

# ==============================================================================
# SECTION B6: SINH TỔNG HỢP & THOÁI HÓA PYRIMIDIN (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B6-01",
    "Nguyên lý Khác biệt của Sinh tổng hợp Pyrimidin De Novo",
    "PYRIMIDIN DE NOVO",
    "Điểm khác biệt căn bản nhất giữa con đường tân tạo Pyrimidin De Novo so với Purin De Novo là gì?",
    [
        "<b>Nguyên lý Pyrimidin —</b> Vòng Pyrimidin 6 cạnh tự do được tổng hợp và đóng vòng hoàn chỉnh trước (dưới dạng Acid Orotic), sau đó mới được gắn vào bộ khung ribose-phosphate của PRPP.",
        "<b>Ngược lại ở Purin —</b> Bắt đầu ngay từ PRPP, nhân Purin được xây dựng từng bước trực tiếp trên khung ribose-phosphate.",
        "<b>Nguồn gốc nguyên tử Pyrimidin —</b> Vòng 6 cạnh chỉ xuất phát từ 2 tiền chất: Carbamoyl phosphate (cung cấp N1 và C2) và Aspartat trọn vẹn (cung cấp N3, C4, C5, C6)."
    ],
    "Sự đơn giản hơn về nguồn nguyên liệu phản ánh cấu trúc nhân đơn 6 cạnh của pyrimidin so với nhân kép 9 nguyên tử phức tạp của purin."
))

cards.append(make_card(
    "HS12-B6-02",
    "So sánh Sống còn: CPS-I (Chu trình Ure) vs CPS-II (Pyrimidin)",
    "ENZYME ĐỐI CHIẾU",
    "Bảng phân biệt các đặc điểm phân tử giữa enzyme CPS-I và CPS-II?",
    [
        "<b>Vị trí dưới tế bào —</b> CPS-I nằm tại Chất nền Ty thể (Mitochondrial matrix); CPS-II nằm tại Bào tương (Cytosol).",
        "<b>Con đường chuyển hóa —</b> CPS-I thuộc Chu trình Urê (chủ yếu ở tế bào gan); CPS-II thuộc con đường sinh tổng hợp Pyrimidin (ở mọi tế bào phân chia).",
        "<b>Cơ chất cung cấp Nitơ —</b> CPS-I sử dụng Amoniac tự do (NH4+); CPS-II sử dụng nhóm amide của acid amin Glutamin.",
        "<b>Chất điều hòa dị lập thể —</b> CPS-I bắt buộc phải có N-acetylglutamat (NAG) hoạt hóa; CPS-II bị ức chế bởi UTP và được hoạt hóa bởi PRPP và ATP."
    ],
    "Phân biệt CPS-I và CPS-II là câu hỏi kinh điển luôn xuất hiện trong các kỳ thi BSNT và USMLE Step 1."
))

cards.append(make_card(
    "HS12-B6-03",
    "Cấu trúc Phức hợp Đa chức năng CAD ở Động vật Nhân thực",
    "ENZYME HỌC",
    "Cấu trúc và chức năng của Phức hợp đa enzyme CAD trong con đường Pyrimidin là gì?",
    [
        "<b>Tên gọi CAD —</b> Là từ viết tắt của 3 hoạt tính enzyme: Carbamoyl phosphate synthetase II (C), Aspartate transcarbamoylase (A), và Dihydroorotase (D).",
        "<b>Bản chất phân tử —</b> Cả 3 hoạt tính enzyme của 3 bước phản ứng đầu tiên đều nằm trên cùng một chuỗi polypeptide đa chức năng khổng lồ (~243 kDa) tại bào tương.",
        "<b>Ưu thế chuyển kênh cơ chất —</b> Cấu trúc đa enzyme giúp chuyển kênh cơ chất (substrate channeling) trực tiếp giữa các tâm xúc tác mà không bị thất thoát ra ngoài dịch bào tương.",
        "<b>Phản ứng tạo ra —</b> Biến đổi Glutamin, CO2 và Aspartat thành phân tử Dihydroorotat."
    ],
    "Phức hợp CAD được điều hòa bởi con đường tín hiệu MAPK và mTOR, phối hợp tăng sinh nucleotide khi tế bào nhận tín hiệu phân chia."
))

cards.append(make_card(
    "HS12-B6-04",
    "Vị trí Đặc biệt của Dihydroorotate Dehydrogenase (DHODH) & Thuốc Leflunomide",
    "ENZYME & DƯỢC LÝ",
    "Vị trí dưới tế bào đặc biệt của DHODH và cơ chế của thuốc Leflunomide là gì?",
    [
        "<b>Vị trí duy nhất ở ty thể —</b> Dihydroorotate Dehydrogenase (DHODH) là enzyme duy nhất trong con đường tổng hợp pyrimidin khu trú tại Màng trong Ty thể (Mitochondrial inner membrane).",
        "<b>Liên kết chuỗi hô hấp —</b> Phản ứng oxy hóa Dihydroorotat thành Orotat chuyển electron trực tiếp cho Coenzyme Q (Ubiquinone) trong chuỗi chuyền điện tử.",
        "<b>Cơ chế Leflunomide & Teriflunomide —</b> Ức chế chọn lọc enzyme DHODH, làm cạn kiệt nguồn pyrimidin của các tế bào lympho T tự miễn đang tăng sinh mạnh.",
        "<b>Ứng dụng lâm sàng —</b> Thuốc DMARD kinh điển điều trị Viêm khớp dạng thấp (Leflunomide) và Đa xơ cứng (Teriflunomide)."
    ],
    "Sự liên kết của DHODH với Coenzyme Q gắn kết trực tiếp tốc độ tổng hợp pyrimidin với trạng thái năng lượng và hoạt động của chuỗi hô hấp tế bào."
))

cards.append(make_card(
    "HS12-B6-05",
    "Phức hợp UMP Synthase: OPRT và OMP Decarboxylase",
    "PYRIMIDIN DE NOVO",
    "Hai phản ứng xúc tác của Phức hợp đa chức năng UMP Synthase là gì?",
    [
        "<b>Hoạt tính 1 (OPRT) —</b> Orotate Phosphoribosyltransferase xúc tác: Orotat (Acid Orotic) + PRPP → Orotidine-5'-monophosphate (OMP) + PPi.",
        "<b>Hoạt tính 2 (OMP Decarboxylase) —</b> Xúc tác phản ứng khử carboxyl: OMP → Uridine Monophosphate (UMP) + CO2.",
        "<b>Bản chất cấu trúc —</b> Ở động vật có vú, cả hai hoạt tính enzyme này đều nằm trên một chuỗi polypeptide duy nhất gọi là UMP Synthase.",
        "<b>Sản phẩm UMP —</b> UMP là nucleotide pyrimidin đầu tiên được tạo thành, làm khuôn để tổng hợp CTP và dTMP."
    ],
    "Khử carboxyl của OMP là một trong những phản ứng hóa học tự nhiên có tốc độ xúc tác enzyme tăng cường mạnh nhất trong sinh học (tăng tốc độ gấp 10^17 lần)."
))

cards.append(make_card(
    "HS12-B6-06",
    "Bệnh Acid Orotic Niệu Di truyền (Hereditary Orotic Aciduria)",
    "BỆNH DI TRUYỀN",
    "Cơ chế bệnh sinh phân tử của Bệnh Acid Orotic Niệu Di truyền là gì?",
    [
        "<b>Đột biến gen —</b> Bệnh di truyền lặn trên nhiễm sắc thể thường gây khiếm khuyết protein đa chức năng UMP Synthase (giảm hoạt tính cả OPRT và OMP Decarboxylase).",
        "<b>Ứ đọng Acid Orotic —</b> Không thể chuyển hóa Orotat thành OMP/UMP → Acid Orotic tích lũy nồng độ cực cao trong máu và bài xuất ồ ạt qua nước tiểu.",
        "<b>Cạn kiệt Pyrimidin —</b> Thiếu hụt UMP dẫn tới thiếu hụt toàn bộ nguồn cung cấp pyrimidin nucleotide (CTP, dTMP) trong cơ thể.",
        "<b>Ảnh hưởng tủy xương —</b> Các tế bào tiền thân dòng hồng cầu trong tủy xương thiếu thymidylate để nhân đôi DNA, gây ứ trệ chu kỳ tế bào ở pha S."
    ],
    "Đây là bệnh lý di truyền hiếm gặp nhưng có ý nghĩa sư phạm kinh điển về mối liên hệ giữa chuyển hóa nucleotide và tạo máu."
))

cards.append(make_card(
    "HS12-B6-07",
    "Đặc điểm Lâm sàng & Huyết học của Acid Orotic Niệu Di truyền",
    "LÂM SÀNG BSNT",
    "Các biểu hiện lâm sàng và huyết học điển hình của Bệnh Acid Orotic Niệu Di truyền là gì?",
    [
        "<b>Chậm phát triển —</b> Trẻ chậm lớn, chậm phát triển thể chất và tinh thần nghiêm trọng.",
        "<b>Thiếu máu hồng cầu to trơ —</b> Thiếu máu đẳng sắc hồng cầu to (MCV tăng rất cao > 110 fL) kèm theo hình ảnh tủy phì đại tế bào khổng lồ (megaloblastic changes).",
        "<b>Kháng Vitamin B12 và Folat —</b> Tình trạng thiếu máu hoàn toàn KHÔNG đáp ứng khi điều trị bằng Vitamin B12 và Acid Folic liều cao.",
        "<b>Sỏi niệu Acid Orotic —</b> Tinh thể acid orotic kết tinh trong đường tiết niệu gây đái ra tinh thể trắng và tắc nghẽn niệu quản."
    ],
    "Dấu hiệu 'thiếu máu hồng cầu to trơ với Folat và B12' ở trẻ nhỏ bắt buộc bác sĩ phải kiểm tra ngay định lượng acid orotic trong nước tiểu."
))

cards.append(make_card(
    "HS12-B6-08",
    "Chẩn đoán Phân biệt Cốt tử: Thiếu UMP Synthase vs Thiếu OTC",
    "CHẨN ĐOÁN PHÂN BIỆT",
    "Cách phân biệt cốt tử giữa Bệnh Acid Orotic Niệu Di truyền và Bệnh Thiếu hụt Ornithine Transcarbamylase (OTC)?",
    [
        "<b>Điểm giống nhau —</b> Cả hai bệnh lý đều có nồng độ Acid Orotic trong nước tiểu tăng rất cao.",
        "<b>Cơ chế tạo acid orotic ở thiếu OTC —</b> Thiếu OTC trong chu trình Urê khiến Carbamoyl phosphate tích lũy trong ty thể tràn ra bào tương, kích hoạt con đường tổng hợp pyrimidin tạo nhiều Acid Orotic.",
        "<b>Nồng độ Amoniac máu (Điểm phân biệt then chốt) —</b> Thiếu OTC gây TĂNG AMONIAC MÁU NẶNG NỀ (nguy cơ hôn mê gan, tử vong); trong khi thiếu UMP Synthase nồng độ Amoniac máu HOÀN TOÀN BÌNH THƯỜNG.",
        "<b>Huyết học —</b> Thiếu UMP Synthase có thiếu máu hồng cầu to; thiếu OTC không có thiếu máu hồng cầu to."
    ],
    "Đo nồng độ Amoniac máu (NH3) là bước đầu tiên và quan trọng nhất để phân biệt hai tình trạng này trên lâm sàng cấp cứu nhi khoa."
))

cards.append(make_card(
    "HS12-B6-09",
    "Nguyên lý Điều trị Bệnh Acid Orotic Niệu bằng Uridine",
    "ĐIỀU TRỊ CHUYỂN HÓA",
    "Tại sao bổ sung Uridine đường uống lại điều trị khỏi hoàn toàn Bệnh Acid Orotic Niệu Di truyền?",
    [
        "<b>Trục vớt Uridine —</b> Uridine ngoại sinh hấp thu vào máu được enzyme Uridine Kinase phosphoryl hóa trực tiếp thành UMP, vượt qua bước khiếm khuyết của UMP Synthase.",
        "<b>Khắc phục thiếu máu —</b> UMP được chuyển thành UTP, CTP và dTMP, cung cấp đủ nguyên liệu cho tủy xương nhân đôi DNA, chữa khỏi hoàn toàn tình trạng thiếu máu hồng cầu to.",
        "<b>Dập tắt Acid Orotic qua Feedback —</b> UTP tạo thành là chất ức chế dị lập thể allosteric tự nhiên của enzyme CPS-II tại bào tương → dập tắt sự tạo mới Carbamoyl phosphate → chấm dứt sản xuất quá mức Acid Orotic.",
        "<b>Hiệu quả —</b> Trẻ phát triển thể chất và trí tuệ bình thường trở lại, acid orotic niệu biến mất."
    ],
    "Liệu pháp Uridine là một ví dụ mẫu mực về ứng dụng sinh hóa điều trị bệnh di truyền: vừa bù đắp sản phẩm thiếu hụt, vừa dùng cơ chế feedback tự nhiên để dập tắt tích lũy độc chất."
))

cards.append(make_card(
    "HS12-B6-10",
    "Con đường Tổng hợp CTP từ UTP nhờ CTP Synthetase",
    "PYRIMIDIN DE NOVO",
    "Phản ứng tổng hợp Cytidine Triphosphate (CTP) từ UTP diễn ra như thế nào?",
    [
        "<b>Các bước phosphoryl hóa —</b> UMP được các nucleoside monophosphate kinase và diphosphate kinase phosphoryl hóa liên tiếp thành UDP rồi UTP.",
        "<b>Phản ứng amin hóa —</b> UTP + Glutamin + ATP + H2O → CTP + Glutamat + ADP + Pi (xúc tác bởi CTP Synthetase).",
        "<b>Nguồn Nitơ —</b> Nhóm amin gắn vào vị trí C4 của vòng uracil được cung cấp bởi nhóm amide của Glutamin.",
        "<b>Điều hòa —</b> CTP ức chế ngược allosteric enzyme CTP Synthetase; được kích hoạt bởi GTP (đảm bảo cân bằng giữa purin và pyrimidin)."
    ],
    "Sự hoạt hóa CTP Synthetase bởi GTP là một cơ chế phối hợp kiểm soát chéo liên con đường khác giữa purin và pyrimidin."
))

cards.append(make_card(
    "HS12-B6-11",
    "Thoái hóa Pyrimidin Mở vòng: Beta-Alanin & Beta-Aminoisobutyrat",
    "THOÁI HÓA PYRIMIDIN",
    "Nhân Pyrimidin bị thoái hóa mở vòng tạo thành các sản phẩm nào trong cơ thể?",
    [
        "<b>Khử hydro mở vòng —</b> Vòng pyrimidin bị enzyme Dihydropyrimidine Dehydrogenase (DPD) khử hydro và sau đó bị thủy phân mở vòng hoàn toàn.",
        "<b>Thoái hóa Cytosin và Uracil —</b> Bị cắt mở vòng tạo thành Beta-Alanin, sau đó chuyển hóa thành Malonyl-CoA (đi vào tổng hợp acid béo), giải phóng NH4+ và CO2.",
        "<b>Thoái hóa Thymin —</b> Bị cắt mở vòng tạo thành Beta-Aminoisobutyrat, sau đó chuyển hóa thành Methylmalonyl-CoA rồi thành Succinyl-CoA (đi vào chu trình Krebs).",
        "<b>Đặc tính lý hóa —</b> Cả Beta-Alanin và Beta-Aminoisobutyrat đều là các acid amin tan rất tốt trong nước và đào thải dễ dàng."
    ],
    "Sản phẩm thoái hóa của pyrimidin được tái sử dụng hoàn toàn cho các con đường sinh năng lượng trung gian của tế bào."
))

cards.append(make_card(
    "HS12-B6-12",
    "Vì sao Rối loạn Thoái hóa Pyrimidin Không Gây Bệnh Gout",
    "HÓA LÝ & LÂM SÀNG",
    "Tại sao các rối loạn thoái hóa Pyrimidin không bao giờ dẫn tới bệnh lý lắng đọng tinh thể như bệnh Gout?",
    [
        "<b>Khả năng mở vòng hoàn toàn —</b> Nhân pyrimidin bị phân giải triệt để thành các phân tử mạch thẳng nhỏ tan cực kỳ tốt trong nước (Beta-alanin, Beta-aminoisobutyrat).",
        "<b>Không tạo chất khó tan —</b> Không tạo ra bất kỳ sản phẩm nào có cấu trúc vòng thơm khó tan tương tự như Acid Uric.",
        "<b>Đào thải dễ dàng —</b> Mọi chất chuyển hóa của pyrimidin đều được bài xuất dễ dàng qua nước tiểu hoặc biến đổi thành các chất chuyển hóa năng lượng trung gian.",
        "<b>Ý nghĩa chẩn đoán —</b> Tăng bài xuất Beta-aminoisobutyrat niệu chỉ là một chỉ số phản ánh tốc độ phá hủy DNA (như trong xạ trị ung thư hoặc bệnh bạch cầu), hoàn toàn không gây sỏi hay viêm khớp."
    ],
    "Sự khác biệt về số phận thoái hóa giữa Purin (tạo acid uric khó tan) và Pyrimidin (tạo acid amin tan tốt) là nguyên nhân khiến bệnh Gout chỉ liên quan đến chuyển hóa Purin."
))

# ==============================================================================
# SECTION B7: SINH TỔNG HỢP dNTPs & SỬA CHỮA DNA (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-B7-01",
    "Enzyme Ribonucleotide Reductase (RNR) & Thuốc Hydroxyurea",
    "SINH TỔNG HỢP dNTPs",
    "Cơ chế xúc tác của Ribonucleotide Reductase (RNR) và đích tác dụng của Hydroxyurea là gì?",
    [
        "<b>Phản ứng khử 2'-OH —</b> Xúc tác khử nhóm 2'-hydroxyl của ribonucleoside diphosphate (NDP: ADP, GDP, CDP, UDP) thành deoxyribonucleoside diphosphate (dNDP: dADP, dGDP, dCDP, dUDP).",
        "<b>Hệ thống truyền điện tử —</b> Sử dụng electron từ NADPH qua hệ thống protein Thioredoxin và Thioredoxin Reductase.",
        "<b>Tâm xúc tác đặc biệt —</b> Phức hợp enzyme chứa một gốc tự do Tyrosyl bền vững được ổn định bởi tâm sắt đôi (Di-iron center).",
        "<b>Cơ chế Hydroxyurea —</b> Thuốc phá hủy có chọn lọc gốc tự do tyrosyl tại tâm hoạt động của RNR, làm ngừng trệ việc sản xuất toàn bộ các dNTP, phong bế tế bào ở pha S chu kỳ."
    ],
    "Hydroxyurea được sử dụng trong bệnh tăng sinh tủy và điều trị bệnh hồng cầu hình liềm (nhờ cơ chế kích thích tái biểu hiện Hemoglobin F)."
))

cards.append(make_card(
    "HS12-B7-02",
    "Sinh tổng hợp dTMP qua Thymidylate Synthase",
    "SINH TỔNG HỢP dNTPs",
    "Phản ứng tổng hợp dTMP do Thymidylate Synthase xúc tác có đặc điểm hóa học nào đặc biệt?",
    [
        "<b>Phương trình phản ứng —</b> dUMP + N5,N10-methylene-THF → dTMP + Dihydrofolate (DHF) (xúc tác bởi Thymidylate Synthase).",
        "<b>Vừa methyl hóa vừa khử —</b> N5,N10-methylene-THF không chỉ chuyển nhóm một carbon (-CH2-) mà còn chuyển trực tiếp một ion hydride (H-) để khử nhóm methylene thành nhóm methyl (-CH3).",
        "<b>Oxy hóa Folate —</b> Đây là phản ứng DUY NHẤT trong tế bào làm oxy hóa Tetrahydrofolate (THF) thành Dihydrofolate (DHF).",
        "<b>Bắt buộc tái sinh THF —</b> Tế bào bắt buộc phải sử dụng enzyme Dihydrofolate Reductase (DHFR) phụ thuộc NADPH để khử DHF trở lại thành THF duy trì chu trình."
    ],
    "Do phản ứng tiêu thụ và oxy hóa folate, sự phân chia tế bào phụ thuộc tuyệt đối vào hoạt động liên tục của enzyme DHFR."
))

cards.append(make_card(
    "HS12-B7-03",
    "Cơ chế Tác dụng của 5-Fluorouracil (5-FU)",
    "HÓA TRỊ UNG THƯ",
    "Cơ chế dược lý phân tử của thuốc chống ung thư 5-Fluorouracil (5-FU) là gì?",
    [
        "<b>Chuyển hóa nội bào —</b> 5-FU được chuyển hóa thành nucleotid hoạt tính là 5-Fluoro-2'-deoxyuridine-5'-monophosphate (5-FdUMP).",
        "<b>Ức chế tự sát (Suicide inhibition) —</b> 5-FdUMP bắt chước cơ chất dUMP gắn vào tâm hoạt động của Thymidylate Synthase cùng với N5,N10-methylene-THF.",
        "<b>Khóa liên kết đồng hóa trị —</b> Do nguyên tử Fluor có độ âm điện cực cao ở vị trí C5 không thể bị tách proton, phức hợp enzyme - giả cơ chất - cofactor bị đông cứng vĩnh viễn trong liên kết cộng hóa trị ba phần.",
        "<b>Hậu quả —</b> Cạn kiệt dTMP ('cái chết do thiếu thymin' - thymineless death), ức chế hoàn toàn tái bản DNA của tế bào ung thư (đặc trị ung thư đại trực tràng, dạ dày, vú)."
    ],
    "5-FU là một chất ức chế tự sát kinh điển được phát minh dựa trên thiết kế thuốc hợp lý (rational drug design)."
))

cards.append(make_card(
    "HS12-B7-04",
    "Cơ chế của Methotrexate và Kháng sinh Trimethoprim",
    "DƯỢC LÝ & KHÁNG SINH",
    "Cơ chế phân tử của Methotrexate và sự khác biệt chọn lọc của Trimethoprim là gì?",
    [
        "<b>Methotrexate (MTX) —</b> Có cấu trúc tương đồng acid folic, ức chế cạnh tranh với ái lực cực cao (gấp 1000 lần acid folic) đối với enzyme Dihydrofolate Reductase (DHFR) của tế bào người.",
        "<b>Hậu quả MTX —</b> Ngăn cản khử DHF thành THF, làm cạn kiệt THF → dập tắt đồng thời cả tổng hợp dTMP và tổng hợp Purin de novo.",
        "<b>Trimethoprim —</b> Ức chế chọn lọc enzyme DHFR của vi khuẩn với ái lực cao gấp 100.000 lần so với enzyme DHFR người.",
        "<b>Phối hợp Cotrimoxazole (Bactrim) —</b> Trimethoprim phối hợp với Sulfamethoxazole (ức chế Dihydropteroate synthase) tạo hiệp đồng diệt khuẩn mạnh mẽ."
    ],
    "Độc tính của liều cao Methotrexate trên tủy xương có thể được giải cứu bằng Leucovorin (Acid Folinic - N5-formyl-THF) không cần qua bước enzym DHFR."
))

cards.append(make_card(
    "HS12-B7-05",
    "Hệ thống Sửa chữa Bắt cặp Sai (MMR) & Hội chứng Lynch",
    "SỬA CHỮA DNA",
    "Cơ chế của hệ thống Mismatch Repair (MMR) và hậu quả khi khiếm khuyết trong Hội chứng Lynch là gì?",
    [
        "<b>Chức năng MMR —</b> Nhận diện và sửa chữa các base ghép đôi sai hoặc các đoạn lặp nhỏ do DNA polymerase trượt và bỏ sót trong quá trình tái bản ở pha S.",
        "<b>Các protein cốt lõi —</b> Phức hợp nhận diện MSH2/MSH6 hoặc MSH2/MSH3; phức hợp cắt sửa MLH1/PMS2 phối hợp với exonuclease.",
        "<b>Mất ổn định vi vệ tinh (MSI-H) —</b> Khi mất chức năng MMR, các trình tự lặp lại ngắn trong hệ gen (microsatellites) tích lũy hàng loạt đột biến trượt khung.",
        "<b>Hội chứng Lynch (HNPCC) —</b> Đột biến mầm di truyền trội trên NST thường của các gen MSH2, MLH1... dẫn tới ung thư đại trực tràng không polyp khởi phát sớm và ung thư nội mạc tử cung."
    ],
    "Khối u có MSI-H/dMMR sản sinh nhiều kháng nguyên đột biến lạ (neoantigens), rất nhạy cảm với liệu pháp kháng thể ức chế điểm kiểm soát miễn dịch (Anti-PD-1 như Pembrolizumab)."
))

cards.append(make_card(
    "HS12-B7-06",
    "Cơ chế Sửa chữa Cắt bỏ Base (Base Excision Repair - BER)",
    "SỬA CHỮA DNA",
    "Các bước enzym tuần tự của hệ thống Sửa chữa Cắt bỏ Base (BER) là gì?",
    [
        "<b>Bước 1 (Cắt base tổn thương) —</b> DNA Glycosylase đặc hiệu nhận diện và cắt liên kết N-glycosidic của base biến đổi (ví dụ: Cytosine bị khử amin tự phát thành Uracil trong DNA), tạo vị trí vô base (AP site: Apurinic/Apyrimidinic site).",
        "<b>Bước 2 (Cắt khung đường) —</b> AP Endonuclease cắt liên kết phosphodiester ở đầu 5' của vị trí AP; AP Lyase cắt đầu 3' loại bỏ gốc đường-phosphate rỗng.",
        "<b>Bước 3 (Lấp đầy) —</b> DNA Polymerase beta tổng hợp chèn đúng nucleotide bổ sung vào khoảng trống.",
        "<b>Bước 4 (Hàn kín) —</b> DNA Ligase hàn gắn liên kết phosphodiester hoàn thiện chuỗi kép."
    ],
    "BER là cơ chế sửa chữa chính cho các tổn thương base nhỏ do oxy hóa (8-oxo-guanine), alkyl hóa hoặc khử amin tự phát diễn ra liên tục hàng ngày."
))

cards.append(make_card(
    "HS12-B7-07",
    "Cơ chế Sửa chữa Cắt bỏ Nucleotide (NER) đối với Tia UV",
    "SỬA CHỮA DNA",
    "Hệ thống Sửa chữa Cắt bỏ Nucleotide (NER) xử lý các tổn thương do tia cực tím (UV) như thế nào?",
    [
        "<b>Tổn thương do tia UV —</b> Bức xạ tia cực tím kích thích hai gốc pyrimidine liền kề trên cùng một sợi DNA tạo liên kết cộng hóa trị thành Dimer Pyrimidine (phổ biến nhất là Dimer Thymin - Thymin, T-T dimer).",
        "<b>Biến dạng chuỗi kép —</b> Dimer pyrimidine gây cong gập biến dạng cấu trúc không gian chuỗi xoắn kép, làm tắc nghẽn DNA polymerase và RNA polymerase.",
        "<b>Cắt đoạn oligonucleotide —</b> Phức hợp protein NER (XPC, XPA, TFIIH helicase) nhận diện và dùng enzyme Excinuclease cắt hai đầu cách tổn thương một đoạn khoảng 24 - 32 nucleotide.",
        "<b>Tổng hợp thay thế —</b> DNA Polymerase delta/epsilon tổng hợp đoạn mới lấp đầy khoảng trống và DNA Ligase hàn kín chuỗi."
    ],
    "NER là hệ thống duy nhất trong tế bào người có khả năng loại bỏ các tổn thương cồng kềnh làm biến dạng chuỗi xoắn kép DNA."
))

cards.append(make_card(
    "HS12-B7-08",
    "Bệnh Khô da Sắc tố (Xeroderma Pigmentosum - XP)",
    "BỆNH DI TRUYỀN",
    "Cơ chế bệnh sinh phân tử và biểu hiện lâm sàng của Bệnh Khô da Sắc tố (Xeroderma Pigmentosum) là gì?",
    [
        "<b>Đột biến gen —</b> Bệnh lý di truyền lặn trên nhiễm sắc thể thường do đột biến mất chức năng các gen thuộc con đường NER (như XPA, XPB, XPC, XPD, ERCC).",
        "<b>Hậu quả phân tử —</b> Tế bào mất hoàn toàn khả năng sửa chữa các tổn thương dimer pyrimidine do tia UV ánh sáng mặt trời gây ra.",
        "<b>Biểu hiện da —</b> Cực kỳ nhạy cảm với ánh sáng mặt trời, bỏng nắng nặng nề ngay khi tiếp xúc nhẹ, tàn nhang sắc tố sẫm màu dày đặc ở vùng da hở, teo da và giãn mạch.",
        "<b>Nguy cơ ung thư cực cao —</b> Nguy cơ mắc các khối u ác tính ở da (ung thư tế bào vảy, ung thư tế bào đáy, u hắc tố ác tính Melanoma) tăng gấp hơn 1000 - 2000 lần so với người bình thường, xuất hiện ngay từ tuổi ấu thơ."
    ],
    "Bệnh nhân XP thường được gọi là 'những đứa trẻ của bóng đêm' (children of the night) vì bắt buộc phải tránh hoàn toàn ánh sáng mặt trời để sống sót."
))

cards.append(make_card(
    "HS12-B7-09",
    "Sửa chữa Đứt gãy Sợi đôi (DSB) & Đột biến Gen BRCA1/2",
    "SỬA CHỮA DNA & UNG THƯ",
    "Hai cơ chế sửa chữa đứt gãy sợi đôi DNA (DSB) và mối liên quan của gen BRCA1/BRCA2 là gì?",
    [
        "<b>Nối đầu không tương đồng (NHEJ) —</b> Gắn trực tiếp hai đầu sợi đứt gãy mà không cần khuôn mẫu; diễn ra nhanh ở pha G1 nhưng rất dễ gây mất đoạn hoặc sai sót đột biến.",
        "<b>Tái tổ hợp tương đồng (HR) —</b> Sử dụng nhiễm sắc tử chị em (sister chromatid) làm khuôn mẫu để sao chép sửa chữa chính xác tuyệt đối; chỉ diễn ra ở pha S và G2.",
        "<b>Vai trò gen BRCA1 và BRCA2 —</b> Là các protein thiết yếu tuyển mộ RAD51 thực hiện con đường tái tổ hợp tương đồng HR.",
        "<b>Đột biến BRCA1/2 & Ức chế PARP —</b> Tế bào ung thư đột biến BRCA mất cơ chế HR; khi dùng thuốc ức chế PARP (Olaparib) chặn nốt cơ chế BER → tích lũy đứt gãy sợi đôi dẫn tới tử vong tổng hợp (synthetic lethality) tiêu diệt tế bào u buồng trứng và ung thư vú."
    ],
    "Hiện tượng 'tử vong tổng hợp' khi dùng thuốc ức chế PARP trên bệnh nhân ung thư mang đột biến BRCA1/2 là bước đột phá lớn của y học chính xác."
))

cards.append(make_card(
    "HS12-B7-10",
    "Cắt nối Chọn lọc (Alternative Splicing) & Thuốc AZT",
    "BIỂU HIỆN GEN & VIRUS",
    "Ý nghĩa của Cắt nối chọn lọc tiền mRNA và cơ chế của thuốc ức chế sao chép ngược AZT là gì?",
    [
        "<b>Cắt nối chọn lọc (Alternative Splicing) —</b> Các exon của tiền mRNA được ghép nối theo nhiều cách kết hợp khác nhau dưới sự điều khiển của phức hợp Spliceosome, cho phép một gen đơn lẻ tạo ra nhiều isoform protein có chức năng khác nhau ở các mô chuyên biệt.",
        "<b>Enzyme Sao chép ngược (Reverse Transcriptase) —</b> Enzyme DNA polymerase phụ thuộc RNA của Retrovirus (như HIV), xúc tác tổng hợp chuỗi cDNA từ khuôn mẫu RNA sợi đơn của virus.",
        "<b>Cơ chế AZT (Zidovudine) —</b> Là chất đồng đẳng dideoxynucleoside của Thymidine, mang nhóm azido (-N3) thay vì nhóm 3'-OH tự do.",
        "<b>Kết thúc chuỗi sớm —</b> Khi Reverse Transcriptase gắn AZT vào chuỗi DNA đang kéo dài, do thiếu nhóm 3'-OH tự do nên liên kết phosphodiester tiếp theo không thể hình thành, làm đứt gãy kết thúc sao chép hệ gen HIV."
    ],
    "AZT có ái lực với Reverse Transcriptase của retrovirus cao hơn khoảng 100 lần so với DNA polymerase của tế bào người, tạo ra cửa sổ điều trị kháng retrovirus."
))

# ==============================================================================
# SECTION B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS12-ALGO-01",
    "Lưu đồ Phân biệt Tăng Acid Orotic Niệu: UMP Synthase vs Thiếu OTC",
    "THUẬT TOÁN CHẨN ĐOÁN",
    "Lưu đồ phân tầng chẩn đoán phân biệt bệnh nhân có Acid Orotic niệu tăng cao dựa trên Amoniac máu và Huyết học?",
    [
        "<b>Bước 1 —</b> Phát hiện Acid Orotic niệu tăng rất cao ở bệnh nhi → Chỉ định xét nghiệm khẩn cấp: Định lượng Amoniac máu (NH3) và Tổng phân tích tế bào máu (MCV).",
        "<b>Bước 2 (Nhánh 1: NH3 tăng vọt) —</b> Nếu NH3 máu tăng rất cao (> 100 - 500 µmol/L), kèm nôn trớ, li bì hôn mê, KHÔNG có thiếu máu hồng cầu to → Chẩn đoán: Thiếu hụt Ornithine Transcarbamylase (OTC) của Chu trình Urê.",
        "<b>Bước 3 (Nhánh 2: NH3 bình thường) —</b> Nếu NH3 máu HOÀN TOÀN BÌNH THƯỜNG, kèm THIẾU MÁU HỒNG CẦU TO (MCV > 110 fL) trơ với B12/Folat, chậm lớn → Chẩn đoán: Bệnh Acid Orotic Niệu Di truyền (Hereditary Orotic Aciduria do thiếu UMP Synthase).",
        "<b>Bước 4 (Xử trí đích) —</b> Nhánh OTC: Lọc máu hạ amoniac, dùng Natri benzoate/phenylbutyrate; Nhánh UMP Synthase: Bổ sung Uridine đường uống suốt đời."
    ],
    "Lưu đồ này giải quyết dứt điểm câu hỏi hóc búa nhất trong chẩn đoán phân biệt các rối loạn chuyển hóa bẩm sinh có tăng acid orotic niệu.",
    algo=True
))

cards.append(make_card(
    "HS12-ALGO-02",
    "Chiến lược Tiếp cận Xử trí Cơn Gout Cấp và Bắt đầu Hạ Urat (ULT)",
    "THUẬT TOÁN ĐIỀU TRỊ",
    "Quy trình xử trí từng bước một bệnh nhân Cơn Viêm khớp Gout Cấp và thời điểm khởi đầu Thuốc hạ Acid Uric (ULT)?",
    [
        "<b>Giai đoạn 1 (Xử trí Cơn Gout cấp) —</b> Cắt cơn viêm ngay lập tức bằng: Colchicine liều thấp (1 mg ban đầu, 0.5 mg sau 1 giờ) HOẶC NSAIDs (Indomethacin, Naproxen) HOẶC Corticosteroids (nếu suy thận/chống chỉ định NSAID).",
        "<b>Quy tắc vàng 1 —</b> TUYỆT ĐỐI KHÔNG khởi đầu thuốc hạ acid uric (Allopurinol, Febuxostat) ngay trong lúc đang có cơn viêm cấp rầm rộ (trừ khi bệnh nhân đã dùng ổn định từ trước).",
        "<b>Giai đoạn 2 (Sau khi cơn cấp lắng dịu 2 - 4 tuần) —</b> Bắt đầu chiến lược hạ acid uric máu (ULT) nếu có chỉ định (≥ 2 cơn/năm, có tophi, có sỏi thận, hoặc xói mòn xương trên X-quang).",
        "<b>Quy tắc vàng 2 (Dự phòng bắt buộc) —</b> Khởi đầu Allopurinol liều thấp (100 mg/ngày) tăng dần mỗi 2 - 4 tuần; BẮT BUỘC dùng kèm Colchicine liều thấp (0.5 - 1 mg/ngày) dự phòng trong 3 - 6 tháng đầu để tránh bùng phát cơn cấp do nứt vỡ tophi.",
        "<b>Mục tiêu điều trị —</b> Duy trì Acid Uric máu < 360 µmol/L (< 6 mg/dL); nếu có hạt tophi nặng duy trì < 300 µmol/L (< 5 mg/dL) để hòa tan tophi."
    ],
    "Quy trình tuân thủ nghiêm ngặt theo khuyến cáo của Hội Thấp khớp học Hoa Kỳ (ACR) và Hội Thấp khớp học Châu Âu (EULAR).",
    algo=True
))

cards.append(make_card(
    "HS12-ALGO-03",
    "Bản đồ Phân tầng 4 Cơ chế Sửa chữa DNA và Hội chứng Ung thư Di truyền",
    "THUẬT TOÁN PHÂN LOẠI",
    "Bản đồ đối chiếu 4 cơ chế Sửa chữa DNA với tổn thương đặc hiệu và các hội chứng ung thư di truyền tương ứng?",
    [
        "<b>Cơ chế 1 (Mismatch Repair - MMR) —</b> Sửa base ghép đôi sai sau sao chép → Khiếm khuyết gen MSH2, MLH1 → Hội chứng Lynch (Ung thư đại trực tràng không polyp HNPCC).",
        "<b>Cơ chế 2 (Base Excision Repair - BER) —</b> Sửa tổn thương base nhỏ đơn lẻ (khử amin Cytosin → Uracil, 8-oxo-G) qua DNA Glycosylase và AP Endonuclease.",
        "<b>Cơ chế 3 (Nucleotide Excision Repair - NER) —</b> Cắt bỏ tổn thương cồng kềnh làm biến dạng chuỗi kép (Dimer Pyrimidine do tia UV) → Khiếm khuyết gen XPA, XPC → Bệnh Khô da sắc tố (Xeroderma Pigmentosum, ung thư da nặng).",
        "<b>Cơ chế 4 (Double-Strand Break - HR/NHEJ) —</b> Sửa đứt gãy sợi kép; Tái tổ hợp tương đồng (HR) phụ thuộc BRCA1/BRCA2 → Đột biến gen BRCA1, BRCA2 → Ung thư Vú và Ung thư Buồng trứng di truyền (nhạy cảm thuốc ức chế PARP)."
    ],
    "Bản đồ phân tầng toàn diện giúp liên kết logic giữa cơ chế sinh hóa phân tử và các hội chứng ung thư di truyền thường gặp trên lâm sàng.",
    algo=True
))

cards.append(make_card(
    "HS12-ALGO-04",
    "Bản đồ Điểm Can thiệp Dược lý trong Bệnh Gout",
    "THUẬT TOÁN DƯỢC LÝ",
    "Bản đồ vị trí tác động phân tử của 5 nhóm thuốc điều trị bệnh Gout chính?",
    [
        "<b>Vị trí 1 (Xanthine Oxidase) —</b> Allopurinol (cơ chất tự sát biến thành Oxypurinol khóa tâm Mo) và Febuxostat (ức chế chọn lọc không purin) → Chặn đứng chuyển Hypoxanthine → Xanthine → Acid Uric.",
        "<b>Vị trí 2 (Kênh URAT1/GLUT9 ở ống thận) —</b> Probenecid, Benzbromarone, Lesinurad → Khóa tái hấp thu urat tại bờ bàn chải ống lượn gần → Tăng tống khứ acid uric ra nước tiểu.",
        "<b>Vị trí 3 (Acid Uric trong tuần hoàn) —</b> Pegloticase, Rasburicase (Uricase tái tổ hợp) → Oxy hóa trực tiếp acid uric thành Allantoin hòa tan cực cao.",
        "<b>Vị trí 4 (Vi ống tế bào Neutrophil) —</b> Colchicine gắn beta-tubulin ức chế trùng hợp vi ống → Ngăn chặn neutrophil di chuyển và thực bào trong ổ khớp.",
        "<b>Vị trí 5 (NLRP3 / Cytokine) —</b> NSAIDs/Corticoid (ức chế COX-2 và biểu hiện gen viêm); Anakinra, Canakinumab (ức chế chọn lọc thụ thể hoặc phân tử IL-1beta)."
    ],
    "Bản đồ tóm lược toàn bộ chiến lược can thiệp dược lý từ khâu sinh tổng hợp, đào thải, tiêu hủy tới ức chế phản ứng viêm trong bệnh Gout.",
    algo=True
))

cards.append(make_card(
    "HS12-ALGO-05",
    "Sơ đồ Điều hòa Tương hỗ Phân nhánh từ IMP thành AMP và GMP",
    "THUẬT TOÁN SINH HÓA",
    "Sơ đồ phân nhánh từ IMP và nguyên lý kiểm soát chéo Reciprocal Regulation giữa AMP và GMP?",
    [
        "<b>Chất ngã ba đường —</b> Inosine Monophosphate (IMP) phân nhánh thành 2 nhánh độc lập: Nhánh AMP và Nhánh GMP.",
        "<b>Nhánh AMP —</b> IMP + Aspartat + [GTP] → Adenylosuccinate → AMP + Fumarat. Bắt buộc dùng GTP làm nguồn năng lượng; AMP ức chế ngược Adenylosuccinate Synthetase.",
        "<b>Nhánh GMP —</b> IMP + NAD+ → XMP + Glutamin + [ATP] → GMP + Glutamat. Bắt buộc dùng ATP làm nguồn năng lượng; GMP ức chế ngược IMP Dehydrogenase (đích của Mycophenolate).",
        "<b>Nguyên lý điều hòa chéo —</b> Dư thừa GTP kích thích tạo AMP; dư thừa ATP kích thích tạo GMP → Tự động tái lập trạng thái cân bằng tuyệt đối tỷ lệ [AMP]/[GMP] = 1.",
        "<b>Ý nghĩa —</b> Ngăn ngừa tình trạng lệch cặp base trong quá trình sao chép DNA và phiên mã RNA của tế bào."
    ],
    "Nguyên tắc điều hòa kiểm soát chéo (Reciprocal Regulation) là minh chứng đỉnh cao cho sự tinh vi của mạng lưới kiểm soát chuyển hóa tế bào.",
    algo=True
))

# Save cards
out_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/14_Hoa sinh/HS-12_Chuyen_hoa_acid_nucleic/HS-12_Chuyen_hoa_acid_nucleic.cards.v2.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(cards)} cards for HS-12 into {out_path.name}")
