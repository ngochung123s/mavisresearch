# -*- coding: utf-8 -*-
"""build_deep_hs10.py - Generate 71 exhaustive master flashcards for HS-10 (Protein Biosynthesis & Gene Expression Regulation)"""
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
    else: section = "B1"

    front = f"""<div style="font-size: 13px; font-weight: bold; color: {badge_color}; text-transform: uppercase; margin-bottom: 8px;">[{badge_text}] {front_title}</div>
<div style="font-size: 16px; font-weight: 600; color: #212529; line-height: 1.5;">{question}</div>
<div style="margin-top: 10px; font-size: 12px; color: #495057;">
  <span style="background-color: #ffd43b; color: #212529; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Gợi ý</span> Nhớ lại cơ chế sinh học phân tử và ý nghĩa lâm sàng BSNT.
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
        "tags": ["hoasinh", "HS10", section]
    }

cards = []

# ==============================================================================
# SECTION B1: MÃ DI TRUYỀN & THUYẾT DAO ĐỘNG WOBBLE (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B1-01",
    "Bốn đặc tính cốt lõi của Mã di truyền",
    "MÃ DI TRUYỀN",
    "Trình bày 4 đặc tính nền tảng của Mã di truyền (Mã bộ ba, Không gối, Thoái hóa và Vạn năng)?",
    [
        "<b>1. Tính mã bộ ba (Triplet Code) —</b> Cứ 3 nucleotide kế tiếp nhau trên mRNA theo chiều 5' → 3' tạo thành một bộ ba mã sao (Codon) quy định một acid amin trên chuỗi polypeptid; có 4³ = 64 codon.",
        "<b>2. Tính liên tục không chồng gối (Non-overlapping, Comma-less) —</b> Mã di truyền được đọc tuần tự từng cụm 3 nucleotide một, không có dấu phẩy ngăn cách và các nucleotide không dùng chung cho hai codon liền kề.",
        "<b>3. Tính thoái hóa hay dư thừa (Degeneracy) —</b> Nhiều codon đồng nghĩa khác nhau cùng mã hóa cho một loại acid amin (ngoại lệ duy nhất: Methionin AUG và Tryptophan UGG chỉ có đúng 1 codon duy nhất).",
        "<b>4. Tính vạn năng (Universal) —</b> Toàn bộ sinh giới từ vi khuẩn, virus, thực vật đến động vật và con người đều dùng chung một bảng từ điển mã di truyền (minh chứng nguồn gốc tiến hóa chung)."
    ],
    "Khám phá về mã di truyền của Marshall Nirenberg và Har Gobind Khorana (Giải Nobel Y học 1968) đã giải mã trọn vẹn từ điển ngôn ngữ của sự sống."
))

cards.append(make_card(
    "HS10-B1-02",
    "Các ngoại lệ của tính vạn năng trong Ty thể",
    "NGOẠI LỆ MÃ DI TRUYỀN",
    "Kể tên các ngoại lệ kinh điển của mã di truyền trong hệ gen Ty thể người so với mã chuẩn?",
    [
        "<b>Bộ gen ty thể (mtDNA) độc lập —</b> Ty thể sở hữu hệ thống dịch mã riêng biệt với bộ t-RNA và ribosom ty thể riêng; mã di truyền ty thể có một số biến thể so với mã chuẩn nhân tế bào.",
        "<b>Codon UGA mã hóa Tryptophan —</b> Trong bảng mã chuẩn UGA là codon kết thúc dừng dịch mã (Opal); trong ty thể UGA mã hóa cho acid amin TRYPTOPHAN.",
        "<b>Codon AUA mã hóa Methionin —</b> Trong bảng mã chuẩn AUA mã hóa cho Isoleucin; trong ty thể AUA mã hóa cho METHIONIN (và có thể đóng vai trò codon mở đầu).",
        "<b>Codon AGA và AGG là codon kết thúc —</b> Trong bảng mã chuẩn AGA và AGG mã hóa cho Arginin; trong ty thể người chúng đóng vai trò là CODON KẾT THÚC (Stop codon)."
    ],
    "Các ngoại lệ này ủng hộ thuyết nội cộng sinh (Endosymbiotic Theory): ty thể vốn là vi khuẩn cổ cộng sinh trong tế bào nhân thực nguyên thủy và vẫn lưu giữ các tàn tích mã hóa riêng."
))

cards.append(make_card(
    "HS10-B1-03",
    "Phân loại 64 Codon: Codon mở đầu và 3 Codon kết thúc",
    "BẢNG MÃ CODON",
    "Nêu vai trò của codon mở đầu AUG và đặc tính của 3 codon kết thúc (Codon vô nghĩa)?",
    [
        "<b>Tổng số 64 Codon —</b> Gồm 61 codon có nghĩa (sense codons) mã hóa cho 20 acid amin và 3 codon vô nghĩa (nonsense codons) làm tín hiệu kết thúc.",
        "<b>Codon mở đầu AUG —</b> Mã hóa cho METHIONIN ở sinh vật nhân thực và N-FORMYLMETHIONIN (fMet) ở sinh vật nhân sơ; luôn định vị khung đọc mở (Open Reading Frame - ORF) chuẩn xác.",
        "<b>Ba Codon kết thúc: UAA, UAG, UGA —</b> UAA (Ochre), UAG (Amber), và UGA (Opal); không có tRNA nào mang anticodon tương ứng trong tế bào chất bình thường.",
        "<b>Tín hiệu dừng dịch mã —</b> Khi một trong 3 codon kết thúc tiến vào vị trí A của ribosom, các yếu tố giải phóng protein (Release Factors) sẽ gắn vào kích hoạt giải phóng chuỗi polypeptid."
    ],
    "Đột biến làm biến đổi một codon có nghĩa thành một codon kết thúc sớm được gọi là Đột biến vô nghĩa (Nonsense mutation), dẫn đến chuỗi polypeptid bị cắt ngắn cụt mất chức năng."
))

cards.append(make_card(
    "HS10-B1-04",
    "Thuyết dao động Wobble của Francis Crick (1966)",
    "THUYẾT DAO ĐỘNG WOBBLE",
    "Trình bày nội dung của Thuyết dao động Wobble và giải thích vì sao tế bào chỉ cần 30 - 45 loại tRNA cho 61 codon?",
    [
        "<b>Nghịch lý số lượng tRNA —</b> Có tới 61 codon mã hóa acid amin nhưng hầu hết tế bào chỉ sở hữu khoảng 30 đến 45 phân tử tRNA khác nhau.",
        "<b>Bắt cặp nghiêm ngặt ở 2 base đầu —</b> Hai nucleotide đầu tiên (vị trí 1 và 2 tính từ đầu 5' của codon trên mRNA) luôn bắt cặp bổ sung rất khắt khe theo quy tắc Watson-Crick (A=U, G≡C) với vị trí 3 và 2 của anticodon.",
        "<b>Dao động linh hoạt ở base thứ 3 của Codon —</b> Vị trí nucleotide thứ 3 ở đầu 3' của codon (tương ứng vị trí thứ nhất ở đầu 5' của anticodon trên tRNA) có sự lỏng lẻo về mặt không gian, cho phép bắt cặp không chuẩn tắc.",
        "<b>Quy tắc dao động Wobble —</b> Base 5' của anticodon là U có thể bắt cặp với A hoặc G của codon; Base 5' là G có thể bắt cặp với C hoặc U; Base 5' là I (Inosine) có thể bắt cặp với cả U, C, hoặc A."
    ],
    "Nhờ thuyết dao động Wobble, một phân tử tRNA duy nhất có thể nhận diện và dịch mã chính xác cho 2 đến 3 codon đồng nghĩa khác nhau, giúp tiết kiệm bộ máy di truyền của tế bào."
))

cards.append(make_card(
    "HS10-B1-05",
    "Vai trò của nucleoside biến đổi Inosine (I) trên tRNA",
    "THUYẾT DAO ĐỘNG WOBBLE",
    "Mô tả cấu tạo của Inosine trên vòng anticodon của tRNA và khả năng bắt cặp dao động linh hoạt của nó?",
    [
        "<b>Bản chất phân tử Inosine (I) —</b> Chứa base nitơ Hypoxanthine; được tạo thành từ phản ứng khử amin của Adenosine nhờ enzym tRNA-specific Adenosine Deaminase (ADAT) sau phiên mã.",
        "<b>Vị trí đắc địa tại đầu 5' của Anticodon —</b> Inosine thường nằm đúng tại vị trí số 34 (vị trí dao động thứ nhất ở đầu 5' của vòng đối mã anticodon).",
        "<b>Khả năng bắt cặp linh hoạt với 3 base —</b> Phân tử Inosine có thể tạo liên kết hydro ổn định với cả ba loại nucleotide: URACIL (U), CYTOSINE (C), và ADENINE (A) ở vị trí thứ 3 của codon trên mRNA.",
        "<b>Ví dụ thực tế —</b> Một phân tử tRNA mang anticodon 5'-IGC-3' có thể nhận diện và bắt cặp hoàn hảo với cả 3 codon đồng nghĩa mã hóa cho Alanin: 5'-GCU-3', 5'-GCC-3', và 5'-GCA-3'."
    ],
    "Inosine đóng vai trò như một 'kẻ đa năng lập thể', giúp tối thiểu hóa số lượng gen mã hóa tRNA trong hệ gen mà vẫn đảm bảo độ chính xác tuyệt đối của quá trình dịch mã."
))

cards.append(make_card(
    "HS10-B1-06",
    "Ý nghĩa sinh học của Tính thoái hóa (Degeneracy) trong phòng vệ đột biến",
    "TIẾN HÓA PHÂN TỬ",
    "Phân tích ý nghĩa sinh học của tính thoái hóa của mã di truyền trong việc giảm thiểu hậu quả của đột biến gen?",
    [
        "<b>Đa số codon đồng nghĩa chỉ khác nhau ở base thứ 3 —</b> Ví dụ cả 4 codon GUU, GUC, GUA, GUG đều cùng mã hóa cho Valin; 4 codon GCU, GCC, GCA, GCG cùng mã hóa cho Alanin.",
        "<b>Tạo Đột biến đồng nghĩa (Silent Mutation) —</b> Một đột biến điểm thay thế ngẫu nhiên ở vị trí nucleotide thứ 3 của codon hầu như không làm thay đổi acid amin tương ứng trên chuỗi polypeptid.",
        "<b>Duy trì cấu trúc protein bình thường —</b> Hoạt tính sinh học của protein được bảo toàn 100%, bảo vệ tế bào khỏi tác hại của các đột biến điểm ngẫu nhiên.",
        "<b>Bảo tồn tính chất hóa lý nếu có đột biến —</b> Nếu đột biến xảy ra ở base thứ nhất hoặc thứ hai, acid amin mới thường có tính chất hóa lý tương tự acid amin cũ (ví dụ acid amin kỵ nước này thay bằng acid amin kỵ nước khác)."
    ],
    "Tính thoái hóa của mã di truyền là một 'tấm đệm giảm xóc phân tử' kỳ diệu của tự nhiên, giúp sinh vật chịu đựng được tốc độ đột biến nền mà không bị tuyệt chủng."
))

cards.append(make_card(
    "HS10-B1-07",
    "Bốn loại đột biến điểm trên phân tử gen (Point Mutations)",
    "ĐỘT BIẾN GEN",
    "Phân biệt 4 dạng đột biến điểm: Đột biến đồng nghĩa, Sai nghĩa, Vô nghĩa và Dịch khung?",
    [
        "<b>1. Đột biến đồng nghĩa (Silent mutation) —</b> Thay thế một nucleotide nhưng codon mới vẫn mã hóa cho CÙNG MỘT ACID AMIN ban đầu; không làm thay đổi chuỗi protein.",
        "<b>2. Đột biến sai nghĩa (Missense mutation) —</b> Thay thế nucleotide làm codon mã hóa cho MỘT ACID AMIN KHÁC (ví dụ: đột biến HbS thay GAG mã hóa Glu thành GUG mã hóa Val tại vị trí số 6 chuỗi β-globin).",
        "<b>3. Đột biến vô nghĩa (Nonsense mutation) —</b> Thay thế nucleotide biến codon có nghĩa thành CODON KẾT THÚC SỚM (UAA, UAG, UGA), làm dịch mã dừng đột ngột tạo chuỗi protein cụt ngủn bất hoạt.",
        "<b>4. Đột biến dịch khung (Frameshift mutation) —</b> Thêm hoặc mất số nucleotide KHÔNG PHẢI BỘI SỐ CỦA 3 (như thêm/mất 1 hoặc 2 nt); làm đảo lộn toàn bộ khung đọc mở từ vị trí đột biến về sau, tạo chuỗi acid amin sai lạc hoàn toàn."
    ],
    "Đột biến dịch khung và đột biến vô nghĩa thường gây ra các kiểu hình bệnh lý di truyền nặng nề nhất (như bệnh Thalassemia thể nặng hoặc bệnh Loạn dưỡng cơ Duchenne) do phá hủy hoàn toàn cấu trúc protein."
))

cards.append(make_card(
    "HS10-B1-08",
    "Khái niệm Khung đọc mở (Open Reading Frame - ORF)",
    "KHUNG ĐỌC MỞ ORF",
    "Định nghĩa Khung đọc mở (ORF) và phân tích tầm quan trọng của việc duy trì đúng khung đọc trong dịch mã?",
    [
        "<b>Định nghĩa Khung đọc mở (ORF) —</b> Là một đoạn trình tự nucleotide liên tục trên mRNA bắt đầu bằng một codon mở đầu (AUG), tiếp theo là chuỗi các codon mã hóa acid amin, và kết thúc bằng một codon dừng (UAA, UAG, UGA).",
        "<b>Ba khung đọc tiềm năng trên mỗi sợi đơn RNA —</b> Vì mã di truyền đọc theo từng bộ ba, một chuỗi RNA bất kỳ có thể đọc theo 3 khung đọc khác nhau tùy thuộc vào vị trí nucleotide bắt đầu (khung +1, +2, +3).",
        "<b>Quyết định bởi Codon mở đầu —</b> Vị trí của codon AUG mở đầu chuẩn tắc sẽ khóa chặt và xác lập duy nhất MỘT KHUNG ĐỌC CHÍNH XÁC cho toàn bộ chuỗi polypeptide.",
        "<b>Hậu quả của sự lệch khung đọc —</b> Nếu ribosom trượt lệch đi 1 nucleotide, toàn bộ thông tin di truyền phía sau sẽ bị đọc sai hoàn toàn, dẫn đến chuỗi acid amin vô nghĩa hoặc gặp codon dừng sớm."
    ],
    "Trong tin sinh học, việc quét tìm các khung đọc mở dài (Long ORFs > 100 codon) trên trình tự hệ gen là bước đầu tiên để nhận diện các gen mã hóa protein mới."
))

cards.append(make_card(
    "HS10-B1-09",
    "Cơ chế dịch mã của Selenocystein (Acid amin thứ 21)",
    "SELENOCYSTEIN DỊCH MÃ",
    "Trình bày cơ chế sinh học phân tử đặc biệt cho phép codon dừng UGA dịch mã tạo Selenocystein?",
    [
        "<b>Acid amin thứ 21 trong mã di truyền —</b> Selenocystein (Sec, U) chứa nguyên tử Selen thay cho lưu huỳnh của Cys; là trung tâm xúc tác của Glutathione Peroxidase và Thioredoxin Reductase.",
        "<b>Mã hóa bởi codon UGA (Vốn là codon dừng) —</b> Bình thường UGA là tín hiệu kết thúc; nhưng trong các gen selenoprotein, UGA được tái lập trình để mã hóa cho Selenocystein.",
        "<b>Cấu trúc kẹp tóc SECIS (SECIS Element) —</b> Phía sau codon UGA (ở vùng 3'-UTR của mRNA ở nhân thực) có một cấu trúc bậc 2 hình kẹp tóc đặc hiệu gọi là Yếu tố chèn Selenocystein (SECIS).",
        "<b>Protein chuyên biệt SBP2 và Yếu tố kéo dài eEFSec —</b> Cấu trúc SECIS liên kết với protein SBP2; phức hợp này tuyển dụng yếu tố kéo dài chuyên biệt eEFSec đưa phân tử Sec-tRNA^[Sec] vào vị trí A để chèn Selenocystein vào chuỗi thay vì dừng dịch mã."
    ],
    "Tái lập trình mã dịch mã (translational reprogramming) của Selenocystein là ví dụ phi thường về sự linh hoạt của bộ máy di truyền: ngữ cảnh cấu trúc bậc hai của mRNA có thể biến một codon dừng thành codon mã hóa acid amin."
))

cards.append(make_card(
    "HS10-B1-10",
    "Pyrrolysine (Acid amin thứ 22) ở vi sinh vật cổ",
    "ACID AMIN THỨ 22",
    "Nêu đặc điểm của acid amin thứ 22 (Pyrrolysine) và codon mã hóa tương ứng?",
    [
        "<b>Acid amin thứ 22 —</b> Pyrrolysine (Pyl, O); là một dẫn xuất của Lysin mang vòng pyrroline gắn vào nhóm ε-amino.",
        "<b>Phân bố hạn chế —</b> Chỉ xuất hiện ở một số vi sinh vật cổ sinh methan (Methanogenic archaea) và một vài vi khuẩn đặc biệt trong các enzym khử methyl.",
        "<b>Mã hóa bởi codon dừng UAG (Amber) —</b> Codon dừng UAG được tái lập trình nhờ yếu tố cấu trúc PYLIS trên mRNA.",
        "<b>Hệ thống tRNA và Synthetase riêng biệt —</b> Sinh vật sở hữu tRNA^[Pyl] và enzym Pyrrolysyl-tRNA synthetase chuyên biệt để hoạt hóa và gắn trực tiếp Pyrrolysine vào tRNA."
    ],
    "Khám phá về Selenocystein (UGA) và Pyrrolysine (UAG) chứng minh rằng từ điển 64 codon không hoàn toàn bất biến mà có thể được tiến hóa mở rộng để tiếp nhận các acid amin chuyên biệt."
))

# ==============================================================================
# SECTION B2: CÁC THÀNH PHẦN THAM GIA DỊCH MÃ: mRNA, tRNA, RIBOSOM (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B2-01",
    "Đặc điểm phân tử mRNA ở Sinh vật nhân sơ: Polycistronic và Shine-Dalgarno",
    "mRNA NHÂN SƠ",
    "Mô tả cấu trúc của phân tử mRNA ở vi khuẩn (nhân sơ) và vai trò của trình tự Shine-Dalgarno?",
    [
        "<b>Bản chất Polycistronic —</b> Một phân tử mRNA vi khuẩn thường chứa trình tự mã hóa cho NHIỀU CHUỖI POLYPEPTIDE KHÁC NHAU cùng thuộc một cụm operon chức năng; mỗi đoạn mã hóa có codon mở đầu và kết thúc riêng.",
        "<b>Không có mũ 5'-cap và đuôi polyA dài —</b> Đầu 5' giữ nguyên nhóm triphosphat (pppG/pppA); thời gian bán hủy rất ngắn (chỉ vài phút).",
        "<b>Trình tự Shine-Dalgarno (SD sequence) —</b> Nằm phía trước codon mở đầu AUG khoảng 8 đến 10 nucleotide; là một đoạn ngắn giàu purin có trình tự đồng thuận: 5'-AGGAGGU-3'.",
        "<b>Định vị chuẩn xác tiểu đơn vị 30S —</b> Trình tự SD bắt cặp bổ sung trực tiếp với đoạn giàu pyrimidine ở đầu 3' của rRNA 16S (3'-UCCUCCA-5') thuộc tiểu phần 30S, giúp ribosom bắt đúng codon AUG vào vị trí P."
    ],
    "Ở vi khuẩn, do không có màng nhân ngăn cách, quá trình dịch mã diễn ra đồng thời cùng lúc với quá trình phiên mã (Coupled Transcription-Translation): ribosome bám vào dịch mã ngay khi mRNA vừa trồi ra khỏi RNA polymerase."
))

cards.append(make_card(
    "HS10-B2-02",
    "Đặc điểm phân tử mRNA ở Sinh vật nhân thực: Mũ 5'-cap, Đuôi PolyA và Trình tự Kozak",
    "mRNA NHÂN THỰC",
    "Mô tả 3 đặc điểm cấu trúc biến đổi trưởng thành của phân tử mRNA ở sinh vật nhân thực?",
    [
        "<b>Bản chất Monocistronic —</b> Hầu hết mọi mRNA nhân thực đều chỉ mã hóa cho DUY NHẤT MỘT CHUỖI POLYPEPTIDE; phiên mã trong nhân và dịch mã ngoài bào tương tách biệt hoàn toàn.",
        "<b>Mũ 5'-m7Gppp (7-methylguanosine cap) —</b> Được gắn vào đầu 5' qua liên kết 5'-5' triphosphat đặc biệt; bảo vệ mRNA khỏi bị phân hủy bởi exonuclease và là vị trí nhận diện cho phức hợp mở đầu dịch mã eIF4F.",
        "<b>Đuôi Poly(A) ở đầu 3' —</b> Chuỗi 150 đến 250 gốc adenylate do enzym Poly(A) Polymerase gắn vào sau phản ứng cắt; bảo vệ đầu 3' và phối hợp với mũ 5' tạo vòng tròn mRNA thúc đẩy dịch mã lặp lại.",
        "<b>Trình tự đồng thuận Kozak —</b> Codon mở đầu AUG được bao quanh bởi trình tự đồng thuận 5'-ACCAUGG-3' (đặc biệt nucleotide purin A/G ở vị trí -3 và G ở vị trí +4); giúp tiểu đơn vị 40S nhận diện đúng vị trí bắt đầu dịch mã."
    ],
    "Cấu trúc vòng tròn khép kín (closed-loop model) của mRNA nhân thực tạo bởi tương tác giữa eIF4E (ở mũ 5'), eIF4G và protein PABP (ở đuôi polyA) đảm bảo rằng chỉ những mRNA còn nguyên vẹn 2 đầu mới được phép dịch mã."
))

cards.append(make_card(
    "HS10-B2-03",
    "Cấu trúc bậc hai lá chẻ ba (Cloverleaf) và bậc ba chữ L của tRNA",
    "CẤU TRÚC PHÂN TỬ tRNA",
    "Mô tả cấu trúc không gian và 4 vùng chức năng đặc thù trên phân tử tRNA vận chuyển?",
    [
        "<b>Cấu trúc bậc hai hình lá chẻ ba (Cloverleaf) —</b> Chuỗi đơn RNA dài 73 - 93 nucleotide tự cuộn gập tạo 4 nhánh tay và các vòng lặp nhờ các liên kết hydro nội chuỗi.",
        "<b>Cấu trúc bậc ba hình chữ L ngược —</b> Hai nhánh xoắn kép xếp vuông góc với nhau tạo hình chữ L ngược; một đầu mang acid amin, đầu đối diện mang bộ ba đối mã anticodon cách nhau khoảng 70 Å.",
        "<b>1. Nhánh tiếp nhận acid amin (Acceptor stem) —</b> Tận cùng bằng bộ ba nucleotide đơn sợi không bắt cặp 5'-CCA-3'; nhóm -OH của Adenosin tận cùng là nơi gắn acid amin.",
        "<b>2. Vòng đối mã (Anticodon loop) —</b> Chứa bộ ba anticodon ở đỉnh vòng (vị trí 34, 35, 36) chịu trách nhiệm nhận diện và bắt cặp bổ sung với codon trên mRNA.",
        "<b>3. Nhánh D (D arm) và Nhánh TψC (T arm) —</b> Nhánh D chứa base lạ Dihydrouracil (D); nhánh T chứa Ribothymidine (T) và Pseudouridine (ψ); tham gia định hình cấu trúc 3 chiều và nhận diện ribosome."
    ],
    "Các base biến đổi lạ (D, T, ψ, Inosine) chiếm tới 10% số nucleotide trên tRNA, được tạo thành nhờ các phản ứng biến đổi hóa sinh sau phiên mã giúp ổn định cấu hình lập thể của phân tử."
))

cards.append(make_card(
    "HS10-B2-04",
    "Đầu tiếp nhận 5'-CCA-3' của tRNA và liên kết este cao năng",
    "ĐẦU TIẾP NHẬN TRÊN tRNA",
    "Mô tả cấu tạo đầu 5'-CCA-3' của tRNA và bản chất của liên kết giữa acid amin với tRNA?",
    [
        "<b>Bộ ba tận cùng 5'-CCA-3' bất biến —</b> Mọi phân tử tRNA chức năng đều kết thúc ở đầu 3' bằng trình tự nucleotide CCA-3' (ở nhân thực được thêm vào sau phiên mã bởi enzym tRNA nucleotidyltransferase).",
        "<b>Vị trí gắn Adenosine tận cùng —</b> Gốc Adenosine tận cùng chứa hai nhóm hydroxyl (-OH) tự do tại vị trí 2' và 3' của vòng đường ribose.",
        "<b>Liên kết Este giàu năng lượng —</b> Nhóm carboxyl (-COOH) của acid amin đã hoạt hóa tạo liên kết ester cộng hóa trị với nhóm 2'-OH hoặc 3'-OH của ribose tận cùng.",
        "<b>Bảo tồn năng lượng ATP —</b> Năng lượng tự do từ sự thủy phân ATP trong phản ứng hoạt hóa được bảo tồn nguyên vẹn trong liên kết ester này, cung cấp năng lượng nhiệt động học trực tiếp cho sự tạo thành liên kết peptid sau này trên ribosome mà KHÔNG CẦN TIÊU TỐN THÊM ATP."
    ],
    "Phân tử tRNA gắn acid amin được gọi là Aminoacyl-tRNA hay 'tRNA nạp điện' (charged tRNA); liên kết este mang thế năng chuyển nhóm cao giúp acid amin ở trạng thái hoạt hóa sẵn sàng phản ứng."
))

cards.append(make_card(
    "HS10-B2-05",
    "So sánh cấu trúc Ribosom Nhân sơ (70S) và Ribosom Nhân thực (80S)",
    "CẤU TRÚC RIBOSOM",
    "Lập bảng so sánh hệ số lắng, thành phần rRNA và protein giữa Ribosom 70S của vi khuẩn và Ribosom 80S của tế bào người?",
    [
        "<b>Ribosom hoàn chỉnh —</b> Vi khuẩn là 70S (khối lượng 2,7 MDa); Nhân thực người là 80S (khối lượng 4,2 MDa).",
        "<b>Tiểu đơn vị nhỏ —</b> Vi khuẩn là TIỂU PHẦN 30S (gồm rRNA 16S [1540 nt] + 21 protein S1-S21); Nhân thực là TIỂU PHẦN 40S (gồm rRNA 18S [1870 nt] + 33 protein).",
        "<b>Tiểu đơn vị lớn —</b> Vi khuẩn là TIỂU PHẦN 50S (gồm 2 loại rRNA: rRNA 23S [2900 nt] và rRNA 5S [120 nt] + 31 protein L1-L31); Nhân thực là TIỂU PHẦN 60S (gồm 3 loại rRNA: rRNA 28S [4800 nt], rRNA 5,8S [160 nt], và rRNA 5S [120 nt] + 47 protein).",
        "<b>Nền tảng độc tính chọn lọc kháng sinh —</b> Sự sai khác sâu sắc về kích thước, cấu trúc phân tử và trình tự rRNA là cơ sở để thuốc kháng sinh tiêu diệt chọn lọc vi khuẩn mà không làm tổn thương tế bào người."
    ],
    "Lưu ý: Hệ số lắng Svedberg (S) phụ thuộc vào cả khối lượng và hình dạng ma sát không gian, do đó giá trị S của phức hợp không bằng tổng số học của hai tiểu phần (50S + 30S = 70S; 60S + 40S = 80S)."
))

cards.append(make_card(
    "HS10-B2-06",
    "Ba vị trí chức năng của Ribosom: Vị trí A, P và E",
    "BA VỊ TRÍ TRÊN RIBOSOM",
    "Mô tả chức năng sinh học của 3 vị trí gắn tRNA trên Ribosom (Vị trí A, P và E)?",
    [
        "<b>Vị trí A (Aminoacyl site - Vị trí Tiếp nhận) —</b> Là nơi tiếp nhận phân tử Aminoacyl-tRNA mới đi vào mang acid amin kế tiếp tương ứng với codon đang chờ đọc trên mRNA.",
        "<b>Vị trí P (Peptidyl site - Vị trí Tạo liên kết) —</b> Là nơi giữ phân tử Peptidyl-tRNA đang gắn với chuỗi polypeptide đang kéo dài (hoặc phân tử Met-tRNA mở đầu trong giai đoạn khởi đầu).",
        "<b>Vị trí E (Exit site - Vị trí Giải phóng) —</b> Là nơi tiếp nhận phân tử tRNA đã bị khử acyl (sau khi đã nhượng chuỗi peptide) trước khi nó tách rời hoàn toàn và bị đẩy ra khỏi ribosom.",
        "<b>Định hướng không gian —</b> Cả 3 vị trí nằm kẹp giữa giao diện của tiểu đơn vị nhỏ (chịu trách nhiệm giải mã codon) và tiểu đơn vị lớn (chịu trách nhiệm xúc tác tạo liên kết peptid)."
    ],
    "Mẹo nhớ kinh điển theo chiều dịch chuyển của tRNA: 'A → P → E' = Acceptor (Tiếp nhận) → Peptide (Tạo chuỗi) → Exit (Lối thoát ra)."
))

cards.append(make_card(
    "HS10-B2-07",
    "Peptidyl Transferase là một Ribozyme (rRNA 23S / 28S)",
    "HOẠT TÍNH RIBOZYME",
    "Trình bày bằng chứng cấu trúc chứng minh Peptidyl Transferase là một Ribozyme chứ không phải enzyme protein?",
    [
        "<b>Khám phá tinh thể học tia X của Thomas Steitz (Nobel 2009) —</b> Phân tích tinh thể học cấu trúc ribosom ở độ phân giải nguyên tử cho thấy trung tâm xúc tác Peptidyl Transferase nằm sâu trong lòng tiểu phần lớn.",
        "<b>Không có bất kỳ chuỗi bên protein nào trong bán kính 18 Å —</b> Xung quanh trung tâm xúc tác vị trí tạo liên kết peptid hoàn toàn không có chuỗi bên acid amin của bất kỳ phân tử protein nào trong bán kính 18 Å.",
        "<b>Phân tử rRNA 23S / 28S đảm nhận toàn bộ xúc tác —</b> Hoạt tính xúc tác tạo liên kết peptid hoàn toàn do các nucleotide của phân tử rRNA 23S (ở vi khuẩn) hoặc rRNA 28S (ở nhân thực) trực tiếp thực hiện.",
        "<b>Bản chất là một Đại Ribozyme —</b> Ribosom thực chất là một Ribozyme khổng lồ; các protein ribosom chỉ đóng vai trò giàn giáo cấu trúc làm bền khung RNA."
    ],
    "Khám phá này củng cố mạnh mẽ Giả thuyết Thế giới RNA (RNA World Hypothesis): RNA là phân tử sinh học nguyên thủy xuất hiện trước tiên trong lịch sử sự sống, vừa mang thông tin di truyền vừa có khả năng xúc tác phản ứng."
))

cards.append(make_card(
    "HS10-B2-08",
    "Đặc tính của Ribosom Ty thể (Mitoribosome) và ngộ độc kháng sinh",
    "RIBOSOM TY THỂ",
    "Mô tả cấu trúc của Ribosom Ty thể và giải thích cơ chế tác dụng phụ gây độc của một số kháng sinh lên tế bào người?",
    [
        "<b>Bản chất 55S ở động vật có vú —</b> Ribosom ty thể người có hệ số lắng 55S (gồm tiểu phần nhỏ 28S chứa rRNA 12S và tiểu phần lớn 39S chứa rRNA 16S); có nguồn gốc tiến hóa từ vi khuẩn cổ.",
        "<b>Tương đồng cấu trúc với Ribosom 70S vi khuẩn —</b> Cấu trúc không gian của ribosom ty thể giống ribosom 70S của vi khuẩn hơn là ribosom 80S trong bào tương tế bào người.",
        "<b>Cơ chế tác dụng phụ của Chloramphenicol —</b> Chloramphenicol ức chế tiểu phần 50S vi khuẩn nhưng ở liều cao cũng ức chế chéo lên ribosom 55S của ty thể, làm tê liệt tổng hợp các enzym chuỗi hô hấp tế bào ở tủy xương gây suy tủy bất sản và Hội chứng xám ở trẻ sơ sinh (Gray baby syndrome).",
        "<b>Độc tính tai và thận của Aminoglycosid —</b> Kháng sinh Aminoglycosid (Gentamicin) có thể gây đột biến hoặc ức chế dịch mã ty thể tại tế bào lông ốc tai và tế bào ống thận, gây điếc tiếp nhận vĩnh viễn và suy thận cấp."
    ],
    "Hiểu rõ sự tương đồng giữa ribosom ty thể và ribosom vi khuẩn giúp các bác sĩ lâm sàng tiên lượng và phòng tránh các độc tính nguy hiểm của nhóm thuốc ức chế dịch mã."
))

cards.append(make_card(
    "HS10-B2-09",
    "Khái niệm Polysome (Polyribosome) và hiệu suất dịch mã",
    "PHỨC HỢP POLYSOME",
    "Định nghĩa phức hợp Polyribosome (Polysome) và ý nghĩa sinh học trong việc tối ưu hóa hiệu suất dịch mã?",
    [
        "<b>Định nghĩa Polyribosome (Polysome) —</b> Là phức hợp gồm nhiều phân tử ribosom cùng bám vào và đồng thời dịch mã trên một phân tử mRNA duy nhất theo chiều từ đầu 5' đến 3'.",
        "<b>Mật độ phân bố ribosom —</b> Trên phân tử mRNA, các ribosom xếp cách nhau khoảng 80 đến 100 nucleotide (tương đương kích thước chiếm chỗ của một ribosom).",
        "<b>Độ dài chuỗi tăng dần —</b> Ribosom ở gần đầu 5' mang chuỗi polypeptide ngắn mới sinh; ribosom càng tiến dần về phía đầu 3' mang chuỗi polypeptide càng dài gần hoàn chỉnh.",
        "<b>Ý nghĩa sinh học tối ưu hóa —</b> Cho phép tế bào tổng hợp ồ ạt hàng chục phân tử protein giống hệt nhau cùng một lúc từ một bản sao mRNA duy nhất trong khoảng thời gian rất ngắn, tiết kiệm tối đa năng lượng phiên mã."
    ],
    "Dưới kính hiển vi điện tử, phức hợp polysome hiển thị như một chuỗi hạt ngọc uốn lượn; ở nhân thực polysome thường cuộn thành hình xoắn ốc tròn nhờ sự liên kết giữa đầu 5'-cap và đuôi 3'-polyA."
))

cards.append(make_card(
    "HS10-B2-10",
    "Tính đặc hiệu nhận diện của bộ ba Anticodon trên tRNA",
    "ĐỐI MÃ ANTICODON",
    "Phân tích chiều đọc phân tử và nguyên tắc bắt cặp bổ sung giữa Codon trên mRNA và Anticodon trên tRNA?",
    [
        "<b>Định hướng ngược chiều (Đối song song - Antiparallel) —</b> Chiều đọc của codon trên mRNA luôn là 5' → 3'; do đó anticodon trên tRNA bắt buộc phải định hướng và bắt cặp theo chiều ngược lại là 3' → 5'.",
        "<b>Quy tắc đánh số nucleotide —</b> Base số 1, 2, 3 của codon (tính từ đầu 5' của mRNA) bắt cặp tương ứng với base số 3, 2, 1 của anticodon (tính từ đầu 5' của tRNA).",
        "<b>Ví dụ kinh điển Codon mở đầu —</b> Codon mở đầu trên mRNA là 5'-AUG-3'; anticodon bổ sung chính xác trên tRNA mở đầu là 3'-UAC-5' (thường được viết theo quy ước 5' → 3' là 5'-CAU-3').",
        "<b>Đảm bảo độ chính xác dịch mã —</b> Sự tương tác bắt cặp bổ sung hình thành mạng lưới liên kết hydro chính xác là điều kiện bắt buộc để ribosom kích hoạt bước kéo dài liên kết peptid."
    ],
    "Lưu ý bẫy thi trắc nghiệm: Khi đề bài cho trình tự anticodon, luôn phải quan sát kỹ đầu 5' và 3' để đảo chiều tương ứng trước khi tra bảng mã di truyền chuẩn."
))

# ==============================================================================
# SECTION B3: CƠ CHẾ PHÂN TỬ 4 GIAI ĐOẠN DỊCH MÃ & CÂN BẰNG NĂNG LƯỢNG (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B3-01",
    "Giai đoạn 1: Hoạt hóa acid amin bởi Aminoacyl-tRNA Synthetase (aaRS)",
    "HOẠT HÓA ACID AMIN",
    "Trình bày 2 bước phản ứng enzym trong quá trình hoạt hóa acid amin và gắn vào tRNA tương ứng?",
    [
        "<b>Họ enzym chuyên biệt —</b> Gồm 20 enzym Aminoacyl-tRNA Synthetase (aaRS) khác nhau trong tế bào tương, mỗi enzym có tính đặc hiệu tuyệt đối cho một loại acid amin và tRNA tương ứng.",
        "<b>Bước 1: Tạo Aminoacyl-AMP trung gian —</b> Acid amin phản ứng với ATP, giải phóng Pyrophosphat vô cơ (PPi) và tạo phức hợp giàu năng lượng Aminoacyl-AMP gắn chặt tại trung tâm hoạt động: Acid amin + ATP ⇌ Aminoacyl-AMP + PPi.",
        "<b>Thủy phân PPi kéo phản ứng một chiều —</b> Enzym Pyrophosphatase lập tức thủy phân PPi → 2 Pi (ΔG°' ≈ -19 kJ/mol), kéo phản ứng dịch chuyển hoàn toàn theo chiều hoạt hóa.",
        "<b>Bước 2: Chuyển acid amin sang đầu 3'-CCA của tRNA —</b> Nhóm acyl của Aminoacyl-AMP được chuyển sang gắn vào nhóm -OH của gốc Adenosin tận cùng ở đầu 3' của tRNA: Aminoacyl-AMP + tRNA ⇌ Aminoacyl-tRNA + AMP.",
        "<b>Chi phí năng lượng tương đương 2 ATP —</b> Do ATP bị bẻ gãy thành AMP và PPi, bước hoạt hóa tiêu tốn tương đương 2 LIÊN KẾT PHOSPHAT CAO NĂNG (~P)."
    ],
    "Giai đoạn hoạt hóa acid amin là bước duy nhất trong sinh tổng hợp protein tiêu tốn năng lượng ATP trực tiếp; toàn bộ các bước sau trên ribosome chỉ tiêu tốn năng lượng GTP."
))

cards.append(make_card(
    "HS10-B3-02",
    "Cơ chế sửa sai kép (Double-Sieve Proofreading) của enzym aaRS",
    "ĐỘ CHÍNH XÁC DỊCH MÃ",
    "Giải thích cơ chế sàng lọc kép hai túi (Double-Sieve Mechanism) giúp enzym aaRS đạt độ chính xác phi thường?",
    [
        "<b>Thách thức nhận diện các acid amin tương đồng —</b> Các acid amin có cấu trúc rất giống nhau (như Valin và Isoleucin chỉ khác nhau đúng 1 nhóm -CH2-) khiến nguy cơ gắn nhầm rất cao.",
        "<b>Túi sàng lọc thứ nhất (Túi hoạt hóa - Activation site) —</b> Kích thước túi vừa khít với acid amin đích; các acid amin LỚN HƠN acid amin đích bị loại bỏ hoàn toàn do cản trở không gian không lọt vào túi được.",
        "<b>Túi sàng lọc thứ hai (Túi sửa sai / Biên tập - Editing site) —</b> Nằm kề bên túi hoạt hóa; chỉ cho phép các acid amin NHỎ HƠN lọt vào.",
        "<b>Thủy phân tức thì sản phẩm gắn sai —</b> Nếu một acid amin nhỏ hơn (như Valin) lọt vào túi hoạt hóa và bị gắn nhầm vào tRNA của Isoleucin, phức hợp Val-tRNA^[Ile] sẽ lập tức bị ép lọt vào túi biên tập và bị THỦY PHÂN CẮT BỎ NGAY LẬP TỨC.",
        "<b>Độ chính xác phi thường —</b> Cơ chế sàng lọc kép nâng độ chính xác của quá trình nạp acid amin lên tới sai số dưới 1/10.000 đến 1/50.000."
    ],
    "Cơ chế sửa sai kép của aaRS được xem là 'người gác cổng di truyền' bảo đảm tính trung thực tuyệt đối của bản dịch protein trước khi acid amin được đưa lên nhà máy ribosome."
))

cards.append(make_card(
    "HS10-B3-03",
    "Giai đoạn 2: Mở đầu dịch mã ở Vi khuẩn (IF1, IF2, IF3 và fMet-tRNA)",
    "MỞ ĐẦU DỊCH MÃ NHÂN SƠ",
    "Mô tả các bước phân tử trong giai đoạn mở đầu dịch mã ở tế bào vi khuẩn (nhân sơ)?",
    [
        "<b>1. Phân ly tiểu phần nhờ IF3 —</b> Yếu tố IF3 gắn vào tiểu phần 30S tự do, ngăn chặn tiểu phần 50S kết hợp sớm.",
        "<b>2. Nhận diện mRNA qua Shine-Dalgarno —</b> Tiểu phần 30S nhận diện trình tự Shine-Dalgarno trên mRNA, định vị codon mở đầu 5'-AUG-3' chuẩn xác vào vị trí P; yếu tố IF1 gắn vào vị trí A để phong bế tạm thời vị trí này.",
        "<b>3. Đưa fMet-tRNA vào vị trí P nhờ IF2-GTP —</b> Acid amin mở đầu là N-FORMYLMETHIONIN (fMet); yếu tố IF2 gắn GTP vận chuyển đặc hiệu phân tử fMet-tRNA_f^[Met] tiến thẳng vào codon AUG tại VỊ TRÍ P.",
        "<b>4. Kết hợp tiểu phần 50S và Thủy phân GTP —</b> IF3 tách rời; tiểu phần lớn 50S tiến vào kết hợp với 30S tạo phức hợp hoàn chỉnh 70S; kích hoạt hoạt tính GTPase của IF2 thủy phân GTP → GDP + Pi; IF1 và IF2-GDP tách rời khỏi ribosom.",
        "<b>Trạng thái sẵn sàng —</b> Ribosom 70S hoàn chỉnh mang fMet-tRNA ở vị trí P và vị trí A hoàn toàn trống trơn sẵn sàng bước vào giai đoạn kéo dài."
    ],
    "fMet-tRNA_f^[Met] là phân tử aminoacyl-tRNA DUY NHẤT trong toàn bộ quá trình dịch mã có khả năng tiến thẳng vào vị trí P của ribosome mà không cần qua vị trí A."
))

cards.append(make_card(
    "HS10-B3-04",
    "Giai đoạn 2: Mở đầu dịch mã ở Sinh vật nhân thực (Phức hợp eIF4F và Quét AUG)",
    "MỞ ĐẦU DỊCH MÃ NHÂN THỰC",
    "Trình bày cơ chế mở đầu dịch mã ở sinh vật nhân thực: Vai trò của Phức hợp tiền mở đầu 43S và Phức hợp nhận diện mũ eIF4F?",
    [
        "<b>Phức hợp tiền mở đầu 43S —</b> Tiểu phần nhỏ 40S gắn với eIF3, eIF1, eIF1A và phức hợp tam phân gồm [eIF2 · GTP · Met-tRNA_i^[Met]] (Methionin nhân thực không bị formyl hóa).",
        "<b>Phức hợp nhận diện mũ eIF4F —</b> Bám vào đầu 5' của mRNA, gồm: eIF4E (gắn trực tiếp vào mũ m7G-cap), eIF4G (protein giàn giáo gắn với PABP ở đuôi polyA tạo vòng tròn mRNA), và eIF4A (enzym helicase tháo xoắn cấu trúc kẹp tóc của mRNA tiêu tốn ATP).",
        "<b>Tuyển dụng 43S lên mRNA —</b> eIF4G liên kết với eIF3, kéo phức hợp 43S bám vào đầu 5' của mRNA tạo thành phức hợp mở đầu 48S.",
        "<b>Quá trình quét tìm Codon mở đầu (Scanning) —</b> Phức hợp 48S trượt dọc theo phân tử mRNA theo chiều 5' → 3' để quét tìm codon AUG mở đầu đầu tiên nằm trong trình tự đồng thuận Kozak.",
        "<b>Lắp ráp Ribosom 80S —</b> Khi anticodon của Met-tRNA bắt cặp chính xác với AUG, eIF2 thủy phân GTP thành GDP; giải phóng toàn bộ các eIFs; tiểu phần lớn 60S kết hợp tạo ribosom 80S hoàn chỉnh với Met-tRNA ngự tại vị trí P."
    ],
    "Cơ chế quét tìm codon mở đầu (scanning mechanism) phụ thuộc mũ 5'-cap là đặc trưng tiến hóa tối thượng của tế bào nhân thực, giúp kiểm soát chặt chẽ biểu hiện gen ở mức độ dịch mã."
))

cards.append(make_card(
    "HS10-B3-05",
    "Giai đoạn 3: Bước 1 của Kéo dài - Đưa Aminoacyl-tRNA vào vị trí A nhờ EF-Tu / eEF1A",
    "KÉO DÀI DỊCH MÃ",
    "Trình bày cơ chế đưa Aminoacyl-tRNA mới vào vị trí A của ribosom bởi yếu tố EF-Tu (ở vi khuẩn) hoặc eEF1A (ở nhân thực)?",
    [
        "<b>Phức hợp tam phân vận chuyển —</b> Aminoacyl-tRNA mới không tự di chuyển vào ribosom mà được bảo vệ và vận chuyển dưới dạng phức hợp ba phần: [EF-Tu · GTP · Aminoacyl-tRNA] (ở vi khuẩn) hoặc [eEF1A · GTP · Aminoacyl-tRNA] (ở nhân thực).",
        "<b>Tiến vào vị trí A —</b> Phức hợp đưa aminoacyl-tRNA vào vị trí A của ribosom nơi codon tiếp theo của mRNA đang chờ đợi.",
        "<b>Kiểm tra tính bổ sung (Decoding) —</b> Anticodon của tRNA thử bắt cặp với codon; nếu bắt cặp sai, phức hợp lập tức bị đẩy ra ngoài.",
        "<b>Thủy phân GTP kích hoạt giải phóng —</b> Nếu bắt cặp bổ sung chính xác, cấu hình ribosom thay đổi kích hoạt hoạt tính GTPase của EF-Tu; thủy phân 1 GTP → GDP + Pi; EF-Tu-GDP tách rời khỏi ribosom, để lại aminoacyl-tRNA nằm khít khao trong vị trí A.",
        "<b>Tái tạo yếu tố bởi EF-Ts —</b> Phân tử EF-Tu-GDP sau đó được yếu tố EF-Ts trao đổi nucleotide loại bỏ GDP và nạp GTP mới để tái tạo EF-Tu-GTP hoạt động."
    ],
    "Khoảng thời gian trễ giữa lúc thủy phân GTP và giải phóng EF-Tu đóng vai trò là một 'bước kiểm tra sửa sai động học' (kinetic proofreading) thứ hai trên ribosome để loại bỏ các tRNA bắt cặp lỏng lẻo."
))

cards.append(make_card(
    "HS10-B3-06",
    "Giai đoạn 3: Bước 2 của Kéo dài - Hình thành Liên kết Peptid và Năng lượng xúc tác",
    "TẠO LIÊN KẾT PEPTID",
    "Mô tả phản ứng tấn công ái nhân hình thành liên kết peptid và giải thích nguồn gốc năng lượng cung cấp cho phản ứng này?",
    [
        "<b>Tấn công ái nhân (Nucleophilic Attack) —</b> Nhóm α-amin (-NH2) tự do của aminoacyl-tRNA tại vị trí A thực hiện phản ứng tấn công ái nhân vào nhóm carbonyl ester (-C=O) của peptidyl-tRNA đang nằm ở vị trí P.",
        "<b>Bẻ gãy liên kết este và tạo liên kết peptid —</b> Cắt đứt liên kết ester giữa chuỗi peptide với tRNA ở vị trí P; đồng thời hình thành liên kết amid cộng hóa trị (liên kết peptid -CO-NH-) nối chuỗi peptide vào acid amin mới ở vị trí A.",
        "<b>Sản phẩm chuyển dịch —</b> Chuỗi polypeptid được kéo dài thêm 1 acid amin và hiện đang gắn với tRNA ngự tại vị trí A; trong khi ở vị trí P chỉ còn lại một phân tử tRNA rỗng bị khử acyl (deacylated tRNA).",
        "<b>Nguồn năng lượng trực tiếp —</b> Phản ứng KHÔNG TIÊU TỐN THÊM ATP HOẶC GTP TẠI CHỖ; năng lượng tự do được lấy trực tiếp từ sự giải phóng liên kết ester giàu năng lượng giữa tRNA và acid amin đã được tích lũy từ bước hoạt hóa trước đó."
    ],
    "Quá trình kéo dài chuỗi polypeptide luôn diễn ra theo chiều tổng hợp từ đầu N-tận đến đầu C-tận: acid amin mới luôn được gắn nối tiếp vào đầu carboxyl tận cùng của chuỗi."
))

cards.append(make_card(
    "HS10-B3-07",
    "Giai đoạn 3: Bước 3 của Kéo dài - Chuyển vị Ribosom nhờ EF-G / eEF2",
    "CHUYỂN VỊ DỊCH MÃ",
    "Trình bày cơ chế chuyển vị (Translocation) của Ribosom dọc theo mRNA bởi yếu tố EF-G (eEF2) và chi phí năng lượng GTP?",
    [
        "<b>Mục đích chuyển vị —</b> Để tiếp tục chu kỳ dịch mã, ribosom bắt buộc phải dịch chuyển chính xác 3 nucleotide (1 codon) dọc theo phân tử mRNA theo chiều 5' → 3'.",
        "<b>Yếu tố chuyển vị gắn GTP —</b> Đòi hỏi yếu tố kéo dài EF-G (ở vi khuẩn) hoặc eEF2 (ở nhân thực) gắn với phân tử GTP tiến vào ribosom.",
        "<b>Bắt chước phân tử (Molecular Mimicry) —</b> Phức hợp EF-G-GTP có hình dạng không gian 3D giống hệt phức hợp [EF-Tu-GTP-tRNA], cho phép nó lọt khít khao vào vị trí A.",
        "<b>Thủy phân GTP tạo lực cơ học —</b> Sự thủy phân 1 GTP → GDP + Pi cung cấp năng lượng cơ học làm xoay hai tiểu phần của ribosom trượt lên nhau: đẩy tRNA rỗng từ vị trí P sang vị trí E, và đẩy peptidyl-tRNA từ vị trí A sang vị trí P.",
        "<b>Vị trí A mở trống —</b> Codon tiếp theo trên mRNA lộ ra tại vị trí A; tRNA rỗng ở vị trí E rời khỏi ribosom; ribosom sẵn sàng cho chu kỳ kéo dài tiếp theo."
    ],
    "Chuyển vị là một chuyển động cơ học phân tử chính xác đến từng ångström, đảm bảo khung đọc mở không bị xê dịch dù chỉ 1 nucleotide trong suốt quá trình tổng hợp hàng ngàn acid amin."
))

cards.append(make_card(
    "HS10-B3-08",
    "Giai đoạn 4: Kết thúc Dịch mã và Giải phóng chuỗi Polypeptide",
    "KẾT THÚC DỊCH MÃ",
    "Mô tả cơ chế nhận diện codon dừng và giải phóng chuỗi polypeptide bởi các Yếu tố giải phóng (Release Factors)?",
    [
        "<b>Codon kết thúc vào vị trí A —</b> Khi một trong 3 codon dừng (UAA, UAG, UGA) tiến vào vị trí A của ribosom, không có tRNA nào tiếp nhận.",
        "<b>Yếu tố giải phóng protein gắn vào vị trí A —</b> Yếu tố Release Factor lớp 1 (RF1 nhận diện UAA/UAG; RF2 nhận diện UAA/UGA ở vi khuẩn; eRF1 nhận diện cả 3 codon dừng ở nhân thực) gắn vào vị trí A nhờ bắt chước hình thái tRNA.",
        "<b>Chuyển đổi Peptidyl Transferase thành Hydrolase —</b> Motif amino acid GGQ trên yếu tố giải phóng tiến vào trung tâm xúc tác peptidyl transferase, bắt buộc enzym này sử dụng một PHÂN TỬ NƯỚC (H2O) thay vì nhóm amin để tấn công liên kết este.",
        "<b>Giải phóng chuỗi Polypeptid —</b> Thủy phân liên kết ester giữa chuỗi peptide và tRNA ở vị trí P, giải phóng chuỗi polypeptide hoàn chỉnh rời khỏi ribosom.",
        "<b>Tháo rời phức hợp Ribosom —</b> Yếu tố RF3-GTP thúc đẩy giải phóng RF1/RF2; sau đó yếu tố tái chế ribosome RRF (Ribosome Recycling Factor) và EF-G thủy phân GTP tháo rời hoàn toàn tiểu phần lớn, tiểu phần nhỏ, tRNA rỗng và mRNA."
    ],
    "Cơ chế nhận diện codon dừng là một ví dụ tuyệt đẹp về sự tương tác protein-RNA: yếu tố protein nhận diện trực tiếp các base nitơ của codon dừng thông qua mạng lưới liên kết hydro đặc hiệu."
))

cards.append(make_card(
    "HS10-B3-09",
    "Cân bằng Năng lượng chi tiết của Sinh tổng hợp Protein",
    "CÂN BẰNG NĂNG LƯỢNG DỊCH MÃ",
    "Tính toán chi tiết số lượng liên kết phosphat cao năng tiêu tốn để gắn kết một acid amin vào chuỗi polypeptide?",
    [
        "<b>Tiêu tốn tối thiểu 4 LIÊN KẾT PHOSPHAT CAO NĂNG (~P tương đương 4 ATP/GTP) cho mỗi acid amin —</b> Được phân bổ cụ thể qua 3 khâu:",
        "<b>1. Hai liên kết cao năng từ ATP khi Hoạt hóa Acid amin —</b> Enzym aaRS thủy phân 1 ATP → AMP + PPi, sau đó PPi → 2 Pi; tương đương tiêu tốn 2 ~P.",
        "<b>2. Một liên kết cao năng từ GTP khi Gắn tRNA vào vị trí A —</b> Yếu tố EF-Tu (eEF1A) thủy phân 1 GTP → GDP + Pi để nạp aminoacyl-tRNA vào vị trí A.",
        "<b>3. Một liên kết cao năng từ GTP khi Chuyển vị Ribosom —</b> Yếu tố EF-G (eEF2) thủy phân 1 GTP → GDP + Pi để dịch chuyển ribosom tiến thêm 1 codon.",
        "<b>Năng lượng khởi đầu và kết thúc —</b> Tiêu tốn thêm 1 GTP cho giai đoạn mở đầu (IF2/eIF2) và 1 đến 2 GTP cho giai đoạn kết thúc và tháo rời ribosome (RF3/RRF)."
    ],
    "Sinh tổng hợp protein là quá trình tiêu tốn nhiều năng lượng trao đổi chất nhất trong toàn bộ tế bào sống (chiếm tới 80 - 90% tổng năng lượng sinh tổng hợp của một tế bào đang tăng sinh)."
))

cards.append(make_card(
    "HS10-B3-10",
    "Tính toán năng lượng tổng hợp một protein cụ thể (Ví dụ chuỗi 100 acid amin)",
    "BÀI TOÁN NĂNG LƯỢNG PROTEIN",
    "Tính toán tổng số liên kết phosphat cao năng cần thiết để sinh tổng hợp hoàn chỉnh một chuỗi polypeptide gồm 100 acid amin?",
    [
        "<b>1. Năng lượng hoạt hóa 100 acid amin —</b> 100 acid amin × 2 ~P (từ ATP) = 200 liên kết cao năng.",
        "<b>2. Năng lượng mở đầu chuỗi —</b> 1 ~P (từ 1 GTP do IF2/eIF2 thủy phân) = 1 liên kết cao năng.",
        "<b>3. Năng lượng gắn vào vị trí A (99 lần kéo dài) —</b> 99 acid amin tiếp theo × 1 ~P (từ 1 GTP do EF-Tu) = 99 liên kết cao năng.",
        "<b>4. Năng lượng chuyển vị ribosom (99 lần chuyển vị) —</b> 99 chu kỳ chuyển vị × 1 ~P (từ 1 GTP do EF-G) = 99 liên kết cao năng.",
        "<b>5. Năng lượng kết thúc và giải phóng chuỗi —</b> Khoảng 1 đến 2 ~P (từ GTP do RF3/eRF3 và RRF).",
        "<b>Tổng chi phí năng lượng —</b> 200 + 1 + 99 + 99 + 1 = đúng 400 LIÊN KẾT CAO NĂNG (Công thức tính nhanh: Số ~P ≈ 4 × N, với N là số lượng acid amin của chuỗi)."
    ],
    "Công thức tính nhanh cho kỳ thi BSNT: Để tổng hợp chuỗi polypeptid gồm N acid amin, tổng số liên kết phosphat cao năng tiêu hao xấp xỉ bằng 4N."
))

cards.append(make_card(
    "HS10-B3-11",
    "Tốc độ và Độ chính xác của Bộ máy Dịch mã",
    "ĐỘNG HỌC DỊCH MÃ",
    "Nêu tốc độ dịch mã ở vi khuẩn so với tế bào nhân thực và phân tích các cơ chế kiểm soát sai sót?",
    [
        "<b>Tốc độ dịch mã ở Vi khuẩn —</b> Cực kỳ nhanh chóng: khoảng 15 đến 20 acid amin được gắn vào chuỗi mỗi giây trên một ribosome (tương đương tốc độ phiên mã của RNA polymerase 60 nt/giây).",
        "<b>Tốc độ dịch mã ở Tế bào nhân thực —</b> Chậm hơn và cẩn trọng hơn: khoảng 2 đến 6 acid amin mỗi giây trên một ribosome.",
        "<b>Tần suất sai sót cực thấp —</b> Sai sót gắn nhầm acid amin chỉ dao động từ 1/1.000 đến 1/10.000 (đủ chính xác để dịch mã một protein lớn 1.000 acid amin mà không có lỗi sai).",
        "<b>Ba tầng kiểm soát độ chính xác —</b> 1) Túi sàng lọc kép của enzym aaRS khi nạp tRNA; 2) Bắt cặp bổ sung kiểm tra codon-anticodon tại vị trí A; 3) Bước kiểm tra động học (Kinetic proofreading) trước khi EF-Tu thủy phân GTP giải phóng."
    ],
    "Khác với sao chép DNA (có cơ chế đọc sửa sai exonuclease 3'→5' đạt sai sót 1/10^9), dịch mã chấp nhận sai số cao hơn (1/10^4) vì protein chỉ là bản sao tạm thời có thời gian bán hủy ngắn và được thay thế liên tục."
))

cards.append(make_card(
    "HS10-B3-12",
    "Hiện tượng Đọc thông Codon dừng (Nonsense Suppression / Readthrough)",
    "HIỆN TƯỢNG ĐỌC THÔNG MÃ",
    "Định nghĩa hiện tượng Đọc thông codon dừng (Readthrough) và ứng dụng thuốc trong điều trị bệnh di truyền đột biến vô nghĩa?",
    [
        "<b>Bản chất hiện tượng Readthrough —</b> Ribosom không dừng lại tại codon kết thúc sớm (Premature Stop Codon - PTC) mà gắn một aminoacyl-tRNA bắt cặp lỏng lẻo vào vị trí A, tiếp tục dịch mã tạo chuỗi protein đủ chiều dài.",
        "<b>Xảy ra tự nhiên ở mức độ thấp —</b> Thường chỉ xảy ra với tần suất < 1% ở các codon dừng tự nhiên.",
        "<b>Kích thích nhân tạo bằng thuốc —</b> Kháng sinh nhóm Aminoglycosid (Gentamicin, G418) hoặc phân tử nhỏ ATALUREN (PTC124) làm lỏng lẻo độ chính xác của vị trí giải mã trên ribosome, thúc đẩy hiện tượng đọc thông codon dừng.",
        "<b>Ứng dụng điều trị Bệnh Xơ nang và Loạn dưỡng cơ Duchenne —</b> Ở bệnh nhân mang đột biến vô nghĩa tạo codon dừng sớm, thuốc giúp tế bào đọc vượt qua codon dừng đột biến để tái tạo một lượng nhỏ protein chức năng (CFTR hoặc Dystrophin) giúp cải thiện triệu chứng."
    ],
    "Liệu pháp đọc thông qua codon dừng (Stop codon readthrough therapy) mở ra hy vọng điều trị bằng thuốc uống cho các bệnh di truyền đơn gen do đột biến vô nghĩa."
))

# ==============================================================================
# SECTION B4: HOÀN THIỆN VÀ BIẾN ĐỔI CHUỖI POLYPEPTIDE SAU DỊCH MÃ (PTM) (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B4-01",
    "Cắt peptid tín hiệu (Signal Peptide) và Hạt nhận diện tín hiệu SRP",
    "ĐỊNH VỊ VẬN CHUYỂN PROTEIN",
    "Mô tả cơ chế dẫn đường của Hạt nhận diện tín hiệu (SRP) và sự cắt bỏ peptid tín hiệu tại lưới nội chất hạt?",
    [
        "<b>Đặc điểm Peptid tín hiệu (Signal Peptide) —</b> Đoạn peptide gồm 15 đến 30 acid amin giàu gốc kỵ nước nằm ở đầu N-tận của các protein được định mệnh bài tiết ra ngoài, gắn màng sinh chất hoặc đưa vào lysosome.",
        "<b>Nhận diện bởi Hạt SRP —</b> Khi peptid tín hiệu trồi ra khỏi ribosome, phức hợp ribonucleoprotein SRP (Signal Recognition Particle) lập tức gắn vào, tạm dừng quá trình dịch mã.",
        "<b>Dẫn đường đến màng RER —</b> Phức hợp [Ribosom-SRP] di chuyển đến màng lưới nội chất hạt (RER), gắn vào THỤ THỂ SRP (SRP Receptor) trên màng.",
        "<b>Đẩy chuỗi vào kênh Translocon (Sec61) —</b> SRP tách rời; ribosome tiếp tục dịch mã đẩy chuỗi polypeptid đang kéo dài xuyên qua kênh Sec61 vào trong lòng RER.",
        "<b>Cắt bỏ bởi Signal Peptidase —</b> Enzym Signal Peptidase gắn trên màng trong của RER cắt đứt liên kết giải phóng chuỗi polypeptide tự do trong lòng RER."
    ],
    "Khám phá về peptide tín hiệu dẫn đường của Günter Blobel (Giải Nobel Y học 1999) đã làm sáng tỏ cơ chế 'mã bưu chính phân tử' giúp tế bào phân loại và gửi protein đến đúng bào quan đích."
))

cards.append(make_card(
    "HS10-B4-02",
    "Hình thành cầu nối Disulfua (-S-S-) bởi Protein Disulfide Isomerase (PDI)",
    "HOÀN THIỆN PROTEIN TẠI RER",
    "Trình bày vai trò của enzym Protein Disulfide Isomerase (PDI) trong lòng lưới nội chất hạt?",
    [
        "<b>Môi trường oxy hóa trong lòng RER —</b> Khác với bào tương có tính khử mạnh (giàu GSH), lòng lưới nội chất hạt có tỷ số GSSG/GSH cao, là môi trường oxy hóa lý tưởng để hình thành cầu nối disulfua (-S-S-).",
        "<b>Enzym xúc tác PDI —</b> Protein Disulfide Isomerase (PDI) định vị trong lòng RER, chứa các motif hoạt động Cys-Gly-His-Cys.",
        "<b>Xúc tác hình thành cầu disulfua —</b> Oxy hóa các nhóm thiol (-SH) của 2 gốc Cysteine tạo cầu disulfua cộng hóa trị.",
        "<b>Chức năng sửa sai đồng phân hóa —</b> Nếu các gốc Cys bắt cặp sai lệch trong quá trình cuộn gập ban đầu, PDI có hoạt tính isomerase cắt đứt liên kết sai và tạo điều kiện cho các cầu disulfua bắt cặp lại theo đúng cấu hình bản địa bền vững nhất."
    ],
    "Cầu disulfua là dấu ấn đặc trưng của các protein tiết ngoại bào (như Kháng thể, Insulin, Albumin), giúp phân tử chống chịu được sự biến tính trong môi trường ngoại bào khắc nghiệt."
))

cards.append(make_card(
    "HS10-B4-03",
    "Chaperone phân tử hỗ trợ cuộn gập và Con đường thoái hóa ERAD",
    "CUỘN GẬP VÀ THOÁI HÓA PROTEIN",
    "Mô tả vai trò của Chaperone phân tử trong lòng RER và con đường tiêu hủy protein cuộn gập sai (ERAD)?",
    [
        "<b>Chaperone phân tử trong RER —</b> Các protein kèm cặp như BiP (thuộc họ Hsp70 trong lòng RER), Calnexin và Calreticulin liên kết với các vùng kỵ nước chưa cuộn gập, tiêu tốn ATP hỗ trợ chuỗi polypeptid cuộn gập đúng cấu hình 3D tự nhiên.",
        "<b>Con đường kiểm soát chất lượng ERAD (ER-Associated Degradation) —</b> Nếu protein bị đột biến hoặc cuộn gập sai thất bại sau nhiều lần thử, nó bị hệ thống giám sát nhận diện là protein phế thải.",
        "<b>Xuất ngược ra Bào tương (Retrotranslocation) —</b> Protein hỏng bị đẩy ngược từ lòng RER qua kênh chuyển vị ra ngoài bào tương.",
        "<b>Ubiquitin hóa và Phá hủy tại Proteasome 26S —</b> Tại bào tương, protein hỏng bị enzym E3 ligase gắn chuỗi Polyubiquitin và đưa vào phức hợp Proteasome 26S để băm nhỏ tiêu hủy triệt để."
    ],
    "Trong bệnh Xơ nang (Cystic Fibrosis), đột biến mất gốc Phe508 trên kênh CFTR (ΔF508) làm protein cuộn gập chậm nhẹ; mặc dù protein vẫn có thể hoạt động nhưng hệ thống ERAD nhận diện sai và tiêu hủy hoàn toàn kênh CFTR dẫn đến bệnh cảnh lâm sàng."
))

cards.append(make_card(
    "HS10-B4-04",
    "Biến đổi Phosphoryl hóa (Phosphorylation) trên Ser, Thr và Tyr",
    "BIẾN ĐỔI SAU DỊCH MÃ",
    "Trình bày phản ứng phosphoryl hóa protein và ý nghĩa của nó như một 'công tắc phân tử' điều hòa tín hiệu?",
    [
        "<b>Nhóm acid amin tiếp nhận —</b> Nhóm hydroxyl (-OH) phân cực của ba gốc acid amin: SERIN, THREONIN, và TYROSIN.",
        "<b>Enzym xúc tác: Protein Kinase —</b> Chuyển nhóm phosphat tích điện âm (-PO4²⁻) từ phân tử ATP gắn đồng hóa trị vào nhóm -OH của protein đích.",
        "<b>Phản ứng đảo ngược: Protein Phosphatase —</b> Thủy phân cắt bỏ nhóm phosphat, hoàn trả lại protein trạng thái ban đầu.",
        "<b>Bản chất 'Công tắc phân tử' (Molecular Switch) —</b> Việc gắn 2 điện tích âm đậm đặc của gốc phosphat làm thay đổi biến hình lập thể không gian của protein, chuyển đổi trạng thái giữa HOẠT HÓA và BẤT HOẠT của hàng ngàn enzym chuyển hóa và yếu tố phiên mã.",
        "<b>Ứng dụng ung thư học —</b> Đột biến hoạt hóa liên tục các thụ thể Tyrosine Kinase (như EGFR, HER2, BCR-ABL) là cơ chế sinh ung thư hàng đầu; điều trị trúng đích bằng các thuốc ức chế kinase (Imatinib, Erlotinib)."
    ],
    "Phosphoryl hóa là biến đổi sau dịch mã phổ biến nhất và năng động nhất trong tế bào động vật có vú, chi phối hầu hết mọi con đường dẫn truyền tín hiệu từ màng tế bào vào nhân."
))

cards.append(make_card(
    "HS10-B4-05",
    "So sánh N-Glycosyl hóa và O-Glycosyl hóa Protein",
    "GLYCOSYL HÓA PROTEIN",
    "Phân biệt đặc điểm sinh hóa giữa N-Glycosyl hóa và O-Glycosyl hóa protein?",
    [
        "<b>N-Glycosyl hóa (N-linked Glycosylation) —</b> Chuỗi đường gắn vào nguyên tử NITƠ AMIDE của gốc ASPARAGINE (Asn, N) nằm trong trình tự đồng thuận: Asn - X - Ser/Thr (với X là bất kỳ acid amin nào trừ Prolin).",
        "<b>Vị trí diễn ra N-glycosyl hóa —</b> Bắt đầu ngay trong lòng LƯỚI NỘI CHẤT HẠT (RER) bằng cách chuyển cả khối oligosaccharide tiền chất 14 gốc đường từ lipid màng Dolichol Phosphate, sau đó hoàn thiện gọt giũa tại Bộ máy Golgi.",
        "<b>O-Glycosyl hóa (O-linked Glycosylation) —</b> Chuỗi đường gắn vào nguyên tử OXY HYDROXYL của gốc SERIN hoặc THREONIN.",
        "<b>Vị trí diễn ra O-glycosyl hóa —</b> Diễn ra hoàn toàn tại BỘ MÁY GOLGI; các gốc đường đơn lẻ (như N-acetylgalactosamine) được gắn tuần tự từng gốc một bởi các enzym Glycosyltransferase.",
        "<b>Ý nghĩa sinh học —</b> Tăng độ hòa tan của protein, bảo vệ chống protease, định hướng vận chuyển nội bào, và đóng vai trò kháng nguyên nhóm máu hệ ABO trên màng hồng cầu."
    ],
    "Bệnh tích tụ tiêu thể I-cell (I-cell disease): Đột biến thiếu enzym Phosphotransferase tại Golgi không thể gắn thẻ Mannose-6-Phosphat lên các enzym tiêu thể N-glycosyl hóa, khiến các enzym này bị bài tiết nhầm ra ngoài tế bào thay vì vào lysosome."
))

cards.append(make_card(
    "HS10-B4-06",
    "Phân cắt chuỗi tiền chất Zymogen trong hệ tiêu hóa",
    "PHÂN CẮT TIỀN CHẤT PROTEIN",
    "Trình bày cơ chế hoạt hóa chuỗi tiền chất bất hoạt Zymogen của các protease tụy tại tá tràng?",
    [
        "<b>Khái niệm Zymogen (Tiền enzyme) —</b> Dạng tiền chất bất hoạt của enzyme; được tổng hợp có thêm một đoạn peptide ức chế che chắn trung tâm hoạt động.",
        "<b>Mục đích bảo vệ mô tụy —</b> Tuyến tụy ngoại tiết bài tiết các enzyme tiêu hóa protein (Trypsinogen, Chymotrypsinogen, Procarboxypeptidase) dưới dạng zymogen bất hoạt để ngăn ngừa enzyme tự tiêu hủy phá hủy chính mô tụy.",
        "<b>Ngòi nổ hoạt hóa Enteropeptidase tại tá tràng —</b> Khi dịch tụy đổ vào tá tràng, enzym ENTEROPEPTIDASE (Enterokinase) nằm trên màng tế bào biểu mô niêm mạc ruột non cắt bỏ một đoạn hexapeptide ở đầu N của Trypsinogen để tạo thành TRYPSIN HOẠT ĐỘNG.",
        "<b>Phản ứng hoạt hóa dây chuyền —</b> Trypsin hoạt động đóng vai trò là enzyme chìa khóa, xúc tác cắt mở hoạt hóa hàng loạt toàn bộ các zymogen còn lại (biến Chymotrypsinogen → Chymotrypsin, Proelastase → Elastase, Procarboxypeptidase → Carboxypeptidase, và tự hoạt hóa thêm Trypsinogen)."
    ],
    "Trong bệnh Viêm tụy cấp (Acute Pancreatitis), sự tắc nghẽn ống tụy hoặc tổn thương do rượu làm Trypsinogen bị hoạt hóa sớm bất thường ngay bên trong mô tụy, kích hoạt chuỗi tự tiêu hủy gây hoại tử tụy và sốc nhiễm độc."
))

cards.append(make_card(
    "HS10-B4-07",
    "Sinh tổng hợp Insulin: Từ Preproinsulin đến Insulin hoạt tính và C-peptide",
    "SINH TỔNG HỢP INSULIN",
    "Mô tả các giai đoạn biến đổi sau dịch mã từ Preproinsulin thành Insulin hoạt tính và ý nghĩa xét nghiệm định lượng C-peptide?",
    [
        "<b>1. Preproinsulin (110 acid amin) —</b> Được dịch mã trên ribosome bám màng RER của tế bào β đảo tụy; mang một chuỗi peptide tín hiệu 24 acid amin kỵ nước ở đầu N.",
        "<b>2. Cắt peptide tín hiệu tạo Proinsulin (86 acid amin) —</b> Khi trồi vào lòng RER, enzym Signal Peptidase cắt bỏ peptide tín hiệu tạo Proinsulin; Proinsulin tự cuộn gập và enzym PDI xúc tác HÌNH THÀNH CHÍNH XÁC 3 CẦU NỐI DISULFUA (2 cầu liên chuỗi và 1 cầu nội chuỗi).",
        "<b>3. Đóng gói vào túi tiết tại Golgi —</b> Proinsulin được vận chuyển sang bộ máy Golgi và đóng gói vào các hạt bài tiết (secretory granules).",
        "<b>4. Cắt đoạn C-peptide tạo Insulin hoạt tính —</b> Trong hạt bài tiết, các enzym nội protease (Prohormone Convertase PC1/PC2 và Carboxypeptidase E) cắt bỏ đoạn PEPTIDE C (C-peptide gồm 31 acid amin), giải phóng phân tử INSULIN HOÀN CHỈNH gồm 2 chuỗi: Chuỗi A (21 acid amin) và Chuỗi B (30 acid amin) nối với nhau bởi 2 cầu disulfua liên chuỗi.",
        "<b>Ý nghĩa lâm sàng định lượng C-peptide —</b> C-peptide và Insulin được xuất bào đồng phân tử (tỷ lệ 1:1); C-peptide không bị gan bắt giữ và có thời gian bán hủy dài hơn, là CHỈ SỐ VÀNG ĐÁNH GIÁ CHÍNH XÁC CHỨC NĂNG TIẾT INSULIN NỘI SINH CỦA TẾ BÀO β (giúp phân biệt Đái tháo đường Type 1 cạn kiệt C-peptide với Type 2 còn C-peptide; phân biệt hạ đường huyết do u đảo tụy Insulinoma với hạ đường huyết do tiêm Insulin ngoại lai)."
    ],
    "Nếu bệnh nhân bị hạ đường huyết do tự tiêm insulin ngoại lai (Factitious hypoglycemia), nồng độ Insulin máu sẽ tăng vọt nhưng C-peptide huyết thanh sụt giảm về 0 do insulin đóng chai không chứa C-peptide."
))

cards.append(make_card(
    "HS10-B4-08",
    "Biến đổi Hydroxyl hóa Prolin/Lysin và vai trò của Vitamin C trong tạo Collagen",
    "BIẾN ĐỔI COLLAGEN",
    "Trình bày phản ứng hydroxyl hóa Prolin và Lysin trong lòng RER và cơ chế bệnh sinh của bệnh Scorbut?",
    [
        "<b>Hydroxyl hóa trong lòng RER —</b> Chuỗi tiền chất Procollagen được enzym Prolyl Hydroxylase và Lysyl Hydroxylase xúc tác gắn nhóm -OH tạo 4-Hydroxyprolin và 5-Hydroxylysin.",
        "<b>Đồng yếu tố bắt buộc: Vitamin C và Fe²⁺ —</b> Enzym đòi hỏi ion sắt hóa trị 2 (Fe²⁺) và VITAMIN C (Acid Ascorbic); Vitamin C đóng vai trò chất khử giữ ion sắt luôn ở trạng thái khử Fe²⁺ (nếu Fe²⁺ bị oxy hóa thành Fe³⁺ enzym sẽ bị bất hoạt vĩnh viễn).",
        "<b>Tạo mạng lưới liên kết hydro bền vững —</b> Các gốc Hydroxyprolin tạo mạng lưới liên kết hydro liên chuỗi cực kỳ dày đặc làm bền cấu trúc bộ ba xoắn collagen (Triple Helix).",
        "<b>Bệnh học Scorbut (Scurvy) —</b> Thiếu hụt Vitamin C trong khẩu phần ăn làm tê liệt phản ứng hydroxyl hóa; các chuỗi collagen không cuộn xoắn bền vững được và bị phân hủy ở nhiệt độ cơ thể, dẫn đến thành mạch máu giòn dễ vỡ, xuất huyết dưới da, chảy máu chân răng rụng răng và vết thương không thể lành."
    ],
    "Gốc Hydroxylysin sau đó còn được glycosyl hóa và tham gia vào phản ứng tạo liên kết chéo cộng hóa trị ngoại bào nhờ enzym Lysyl Oxidase (phụ thuộc Đồng Cu²⁺) để tạo nên độ bền kéo của sợi collagen."
))

cards.append(make_card(
    "HS10-B4-09",
    "Biến đổi Carboxyl hóa Glutamat và vai trò của Vitamin K trong đông máu",
    "BIẾN ĐỔI YẾU TỐ ĐÔNG MÁU",
    "Trình bày phản ứng γ-carboxyl hóa gốc Glutamat phụ thuộc Vitamin K và cơ chế tác dụng của thuốc chống đông Warfarin?",
    [
        "<b>Tạo gốc γ-Carboxyglutamat (Gla) —</b> Enzym Glutamyl Carboxylase tại lưới nội chất tế bào gan xúc tác gắn thêm một nhóm carboxyl (-COO⁻) vào carbon γ của gốc Glutamat trên chuỗi tiền chất của các yếu tố đông máu II, VII, IX, X và Protein C, S.",
        "<b>Coenzym Vitamin K dạng khử (Hydroquinone) —</b> Phản ứng bắt buộc cần Vitamin K dạng khử (Vitamin KH2) và CO2; sau phản ứng Vitamin K bị oxy hóa thành Vitamin K Epoxide.",
        "<b>Tái sinh Vitamin K nhờ VKOR —</b> Enzym Vitamin K Epoxide Reductase (VKOR) khử epoxide tái sinh trở lại Vitamin K hydroquinone để tiếp tục chu trình xúc tác.",
        "<b>Tạo vị trí chelate hóa ion Canxi (Ca²⁺) —</b> Gốc Gla mang 2 nhóm carboxylat tích điện âm kề nhau (-CH(COO⁻)2), tạo 'gọng kìm' ái lực cực cao bắt giữ ion Ca²⁺; cầu nối Ca²⁺ giúp các yếu tố đông máu gắn chặt lên bề mặt màng phospholipid tiểu cầu hoạt hóa để khởi động dòng thác đông máu.",
        "<b>Cơ chế thuốc chống đông Warfarin —</b> Warfarin ức chế cạnh tranh bất thuận nghịch enzym VKOR, ngăn chặn tái sinh Vitamin K khử, làm gan bài tiết các yếu tố đông máu không được carboxyl hóa (yếu tố PIVKA) mất hoàn toàn hoạt tính đông máu."
    ],
    "Bệnh nhân dùng quá liều Warfarin bị xuất huyết có thể được giải độc nhanh chóng bằng cách bổ sung Vitamin K1 liều cao đường tiêm hoặc truyền huyết tương tươi đông lạnh chứa sẵn các yếu tố đông máu hoàn chỉnh."
))

cards.append(make_card(
    "HS10-B4-10",
    "Biến đổi gắn Lipid màng (Lipidation) và Ubiquitin hóa",
    "BIẾN ĐỔI GẮN LIPID VÀ UBIQUITIN",
    "Nêu vai trò của biến đổi gắn gốc Lipid màng (Myristoylation, Farnesylation) và Ubiquitin hóa trong định vị và điều hòa protein?",
    [
        "<b>Gắn gốc Myristoyl (Myristoylation) —</b> Gắn acid béo bão hòa 14 carbon (Myristic acid) vào gốc Glycin đầu N-tận; đóng vai trò như 'mỏ neo kỵ nước' cắm protein vào bề mặt trong của màng sinh chất (như protein G, protein tyrosine kinase Src).",
        "<b>Gắn gốc Farnesyl (Farnesylation / Prenylation) —</b> Gắn nhóm isoprenoid 15 carbon (Farnesyl pyrophosphat) vào gốc Cysteine gần đầu C-tận; đặc biệt thiết yếu cho sự định vị màng và hoạt tính sinh ung thư của protein Ras (đích tác dụng của thuốc ức chế farnesyltransferase).",
        "<b>Ubiquitin hóa (Ubiquitination) —</b> Gắn chuỗi polyubiquitin vào nhóm ε-amino của gốc Lysin; đóng vai trò như 'tem nhãn tử thần' định vị đưa protein đến phức hợp Proteasome 26S để phá hủy.",
        "<b>Ý nghĩa sinh học tổng thể —</b> Các biến đổi PTM gắn lipid và ubiquitin quyết định chính xác tọa độ không gian tế bào và thời gian sống còn của từng phân tử protein."
    ],
    "Sự kết hợp linh hoạt của hơn 200 loại biến đổi sau dịch mã (PTM) khác nhau cho phép bộ gen người chỉ với khoảng 20.000 gen mã hóa có thể tạo ra hơn 1.000.000 biến thể protein chức năng (proteoforms)."
))

# ==============================================================================
# SECTION B5: CƠ CHẾ PHÂN TỬ CỦA KHÁNG SINH VÀ ĐỘC TỐ ỨC CHẾ DỊCH MÃ (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B5-01",
    "Nguyên lý Độc tính chọn lọc (Selective Toxicity) của Kháng sinh ức chế dịch mã",
    "KHÁNG SINH ỨC CHẾ DỊCH MÃ",
    "Trình bày cơ sở sinh học phân tử của tính độc tính chọn lọc ở các thuốc kháng sinh tác động lên bộ máy dịch mã?",
    [
        "<b>Khái niệm Độc tính chọn lọc —</b> Khả năng của thuốc ức chế hoặc tiêu diệt mầm bệnh vi khuẩn mà không gây tổn hại đáng kể đến tế bào của cơ thể vật chủ người.",
        "<b>Khác biệt cấu trúc Ribosom 70S vs. 80S —</b> Ribosom vi khuẩn là 70S (gồm tiểu phần 30S và 50S) với các phân tử rRNA và protein đặc thù; trong khi tế bào người là ribosom 80S (tiểu phần 40S và 60S).",
        "<b>Kháng sinh gắn đặc hiệu vào rãnh phân tử vi khuẩn —</b> Các phân tử kháng sinh được thiết kế để khớp khít hoàn hảo vào các túi liên kết đặc hiệu trên rRNA 16S hoặc rRNA 23S của vi khuẩn mà không gắn được vào rRNA tương ứng của người.",
        "<b>Phân loại theo đích tác động —</b> 1) Nhóm ức chế tiểu phần nhỏ 30S (Aminoglycosid, Tetracyclin); 2) Nhóm ức chế tiểu phần lớn 50S (Chloramphenicol, Macrolid, Clindamycin, Linezolid)."
    ],
    "Mẹo nhớ kinh điển của sinh viên y khoa quốc tế: 'Buy AT 30, CCELL at 50' = Aminoglycosid & Tetracyclin tác động lên 30S; Chloramphenicol, Clindamycin, Erythromycin (Macrolid), Linezolid tác động lên 50S."
))

cards.append(make_card(
    "HS10-B5-02",
    "Cơ chế tác dụng phân tử của nhóm Aminoglycosid (Streptomycin, Gentamicin)",
    "KHÁNG SINH NHÓM AMINOGLYCOSID",
    "Trình bày cơ chế tác động lên tiểu phần 30S và giải thích vì sao Aminoglycosid có tính chất diệt khuẩn (Bactericidal)?",
    [
        "<b>Đích tác động phân tử —</b> Gắn bất thuận nghịch vào phân tử rRNA 16S của tiểu đơn vị nhỏ 30S ribosom vi khuẩn.",
        "<b>Cơ chế 1: Đông cứng phức hợp mở đầu —</b> Khóa chặt phức hợp mở đầu 70S, ngăn cản ribosom bước vào giai đoạn kéo dài.",
        "<b>Cơ chế 2: Gây đọc sai mã di truyền (Mistranslation) —</b> Làm biến dạng trung tâm giải mã tại vị trí A, khiến ribosom chấp nhận các aminoacyl-tRNA bắt cặp sai lệch với codon trên mRNA.",
        "<b>Tổng hợp protein độc hại và Diệt khuẩn —</b> Quá trình đọc sai mã tạo ra các chuỗi polypeptide đột biến sai lạc; các protein hỏng này chèn vào màng sinh chất vi khuẩn tạo các lỗ thủng màng, làm rò rỉ ion và DIỆT KHUẨN NHANH CHÓNG (Bactericidal).",
        "<b>Độc tính lâm sàng —</b> Độc tính chọn lọc kém hơn ở nồng độ cao gây độc thận (hoại tử ống thận cấp) và độc tính ốc tai tiền đình không hồi phục do ức chế ty thể."
    ],
    "Khác với hầu hết các kháng sinh ức chế dịch mã khác chỉ có tính kìm khuẩn (bacteriostatic), Aminoglycosid là nhóm duy nhất có tác dụng diệt khuẩn mạnh nhờ cơ chế tạo protein độc thủng màng."
))

cards.append(make_card(
    "HS10-B5-03",
    "Cơ chế tác dụng phân tử của nhóm Tetracyclin (Doxycycline)",
    "KHÁNG SINH NHÓM TETRACYCLIN",
    "Trình bày cơ chế ức chế dịch mã của nhóm Tetracyclin tại vị trí A của tiểu phần 30S?",
    [
        "<b>Đích tác động phân tử —</b> Gắn thuận nghịch vào tiểu phần nhỏ 30S của ribosom vi khuẩn.",
        "<b>Phong bế không gian vị trí A —</b> Phân tử Tetracyclin nằm chắn ngay tại vị trí A của ribosom, tạo chướng ngại lập thể ngăn không cho phức hợp Aminoacyl-tRNA mới tiến vào vị trí A.",
        "<b>Đình trệ kéo dài chuỗi —</b> Do không có acid amin mới được đưa vào, chuỗi polypeptide không thể kéo dài tiếp.",
        "<b>Tính chất kìm khuẩn (Bacteriostatic) —</b> Ức chế sự phát triển và nhân lên của vi khuẩn để hệ miễn dịch cơ thể tiêu diệt mầm bệnh.",
        "<b>Tác dụng phụ lâm sàng —</b> Tetracyclin chelate hóa tạo phức rất bền với ion Canxi (Ca²⁺); do đó lắng đọng vào xương và mầm răng đang phát triển gây biến màu men răng vàng nâu vĩnh viễn và chậm phát triển xương; CHỐNG CHỈ ĐỊNH CHO PHỤ NỮ CÓ THAI VÀ TRẺ EM DƯỚI 8 TUỔI."
    ],
    "Cơ chế đề kháng Tetracyclin phổ biến nhất của vi khuẩn là tổng hợp các bơm tống thuốc chủ động (efflux pumps mã hóa bởi gen tetA) đẩy thuốc ra ngoài tế bào."
))

cards.append(make_card(
    "HS10-B5-04",
    "Cơ chế tác dụng của Chloramphenicol và Hội chứng xám ở trẻ sơ sinh",
    "KHÁNG SINH CHLORAMPHENICOL",
    "Trình bày cơ chế ức chế Peptidyl Transferase của Chloramphenicol và cơ chế gây Hội chứng xám (Gray Baby Syndrome)?",
    [
        "<b>Đích tác động —</b> Gắn thuận nghịch vào phân tử rRNA 23S của tiểu đơn vị lớn 50S ribosom vi khuẩn.",
        "<b>Ức chế trực tiếp enzym Peptidyl Transferase —</b> Khóa chặt trung tâm xúc tác peptidyl transferase, ngăn cản hoàn toàn sự hình thành liên kết peptid giữa acid amin mới ở vị trí A với chuỗi peptide ở vị trí P.",
        "<b>Độc tính ức chế tủy xương —</b> 1) Độc tính ức chế tủy phụ thuộc liều (thiếu máu có hồi phục); 2) Thiếu máu bất sản tủy vô căn không hồi phục (Aplastic anemia) không phụ thuộc liều cực kỳ nguy hiểm.",
        "<b>Cơ chế Hội chứng xám ở trẻ sơ sinh (Gray Baby Syndrome) —</b> Gan trẻ sơ sinh chưa hoàn thiện enzym UGT1A1 để liên hợp thải trừ chloramphenicol; thuốc tích tụ nồng độ cao ức chế ribosom 55S của ty thể cơ tim, gây trụy tim mạch cấp tính, da tím tái màu xám tro, hạ thân nhiệt và tử vong."
    ],
    "Do độc tính tủy xương và hội chứng xám nguy hiểm, Chloramphenicol hiện nay chỉ còn được dùng hạn chế cho các trường hợp nhiễm trùng đe dọa tính mạng (viêm màng não mủ, sốt mò rickettsia) khi không còn thuốc thay thế."
))

cards.append(make_card(
    "HS10-B5-05",
    "Cơ chế tác dụng của nhóm Macrolid (Azithromycin, Erythromycin) và Clindamycin",
    "KHÁNG SINH NHÓM MACROLID",
    "Trình bày cơ chế ức chế chuyển vị ribosom của nhóm Macrolid và Clindamycin tại tiểu phần 50S?",
    [
        "<b>Đích tác động phân tử —</b> Gắn vào phân tử rRNA 23S của tiểu đơn vị lớn 50S tại vùng gần lối vào của đường hầm thoát peptide (Polypeptide Exit Tunnel).",
        "<b>Cơ chế tắc nghẽn đường hầm —</b> Hoạt động như một 'nút chai' bít kín đường hầm thoát, khiến chuỗi peptide mới sinh dài khoảng 3 - 4 acid amin bị mắc kẹt không thể dài thêm và rơi rụng sớm.",
        "<b>Ức chế bước Chuyển vị Ribosom (Translocation) —</b> Cản trở sự dịch chuyển của ribosom dọc theo phân tử mRNA.",
        "<b>Tương tác cạnh tranh vị trí —</b> Cả Macrolid, Clindamycin và Chloramphenicol đều có vị trí gắn rất gần nhau trên 50S; do đó CHỐNG CHỈ ĐỊNH PHỐI HỢP CÙNG LÚC các thuốc này vì chúng sẽ cạnh tranh chiếm chỗ và triệt tiêu tác dụng của nhau.",
        "<b>Cơ chế đề kháng qua Methyl hóa rRNA —</b> Vi khuẩn đột biến mang gen erm tiết enzym methyltransferase gắn nhóm methyl vào adenine trên rRNA 23S, làm giảm ái lực của Macrolid và Clindamycin (kiểu hình kháng chéo MLSB)."
    ],
    "Azithromycin là một trong những kháng sinh được kê đơn phổ biến nhất hiện nay nhờ phổ kháng khuẩn rộng trên vi khuẩn không điển hình (Mycoplasma, Chlamydia) và thời gian bán hủy mô cực dài."
))

cards.append(make_card(
    "HS10-B5-06",
    "Cơ chế tác dụng của Kháng sinh Linezolid (Oxazolidinon)",
    "KHÁNG SINH LINEZOLID",
    "Trình bày cơ chế tác động độc đáo của Linezolid lên phức hợp ribosom và phổ kháng khuẩn đặc hiệu?",
    [
        "<b>Kháng sinh nhóm Oxazolidinon tổng hợp —</b> Được phát triển để đối phó với các chủng vi khuẩn gram dương đa kháng thuốc.",
        "<b>Cơ chế độc đáo ngăn cản tạo phức hợp 70S —</b> Gắn đặc hiệu vào phân tử rRNA 23S của tiểu phần 50S tại vị trí tiếp giáp; ngăn chặn tiểu phần 50S kết hợp với tiểu phần 30S để hình thành phức hợp ribosom 70S chức năng.",
        "<b>Tác động ở giai đoạn rất sớm —</b> Đình trệ quá trình dịch mã ngay từ khâu lắp ráp mở đầu, trước khi chuỗi peptide bắt đầu được tổng hợp.",
        "<b>Vũ khí đặc trị vi khuẩn siêu kháng —</b> Là lựa chọn hàng đầu điều trị Tụ cầu vàng kháng Methicillin (MRSA) và Enterococcus kháng Vancomycin (VRE).",
        "<b>Tác dụng phụ ức chế MAO —</b> Linezolid là chất ức chế enzym Monoamine Oxidase (MAO); khi dùng chung với thuốc chống trầm cảm SSRI có thể kích hoạt Hội chứng Serotonin nguy hiểm."
    ],
    "Do có cơ chế tác động hoàn toàn mới ở khâu lắp ráp ribosom, Linezolid không bị kháng chéo bởi các chủng vi khuẩn đã kháng các nhóm kháng sinh ức chế dịch mã cổ điển khác."
))

cards.append(make_card(
    "HS10-B5-07",
    "Cơ chế gây độc của Ngoại độc tố Bạch hầu (Diphtheria Toxin)",
    "ĐỘC TỐ SINH HỌC DỊCH MÃ",
    "Trình bày cơ chế phân tử của Ngoại độc tố Bạch hầu trong việc làm tê liệt yếu tố kéo dài eEF2 của tế bào nhân thực?",
    [
        "<b>Nguồn gốc vi khuẩn —</b> Tiết ra từ vi khuẩn Bạch hầu Corynebacterium diphtheriae (khi vi khuẩn bị nhiễm thực khuẩn thể mang gen tox).",
        "<b>Cấu trúc độc tố A-B —</b> Tiểu phần B gắn vào thụ thể bề mặt tế bào đưa độc tố vào nội bào; tiểu phần A có hoạt tính enzym giải phóng vào bào tương.",
        "<b>Hoạt tính enzym ADP-Ribosyltransferase —</b> Tiểu phần A xúc tác phản ứng chuyển gốc ADP-ribose từ phân tử NAD⁺ của tế bào vật chủ gắn vào phân tử eEF2: NAD⁺ + eEF2 → ADP-ribosyl-eEF2 + Nicotinamide + H⁺.",
        "<b>Đích gắn đặc hiệu acid amin Diphthamide —</b> Gốc ADP-ribose gắn đồng hóa trị vào Diphthamide (một gốc Histidin biến đổi sau dịch mã độc nhất chỉ có trên yếu tố kéo dài eEF2).",
        "<b>Bất hoạt vĩnh viễn eEF2 và Chết tế bào —</b> eEF2 bị bất hoạt vĩnh viễn không thể thực hiện phản ứng chuyển vị ribosom; đình trệ 100% quá trình sinh tổng hợp protein của tế bào nhân thực, gây hoại tử niêm mạc tạo mảng giả mạc màu xám dai dẳng ở hầu họng, viêm cơ tim cấp suy tim và liệt dây thần kinh."
    ],
    "Chỉ cần đúng MỘT PHÂN TỬ tiểu phần A của ngoại độc tố bạch hầu lọt vào bào tương cũng đủ sức làm tê liệt toàn bộ phân tử eEF2 và giết chết một tế bào nhân thực trong vòng vài giờ."
))

cards.append(make_card(
    "HS10-B5-08",
    "Ngoại độc tố A của Trực khuẩn mủ xanh (Pseudomonas Exotoxin A)",
    "ĐỘC TỐ SINH HỌC DỊCH MÃ",
    "So sánh cơ chế tác dụng phân tử của Exotoxin A của Pseudomonas aeruginosa với Ngoại độc tố Bạch hầu?",
    [
        "<b>Cơ chế phân tử HOÀN TOÀN GIỐNG HỆT BẠCH HẦU —</b> Exotoxin A của Trực khuẩn mủ xanh cũng là một độc tố cấu trúc A-B có hoạt tính enzym ADP-ribosyltransferase.",
        "<b>Cùng tấn công đích eEF2 —</b> Xúc tác chuyển nhóm ADP-ribose từ NAD⁺ gắn vào gốc Diphthamide trên yếu tố kéo dài eEF2 của tế bào nhân thực.",
        "<b>Đình trệ hoàn toàn dịch mã —</b> Gây chết tế bào theo cơ chế ngừng tổng hợp protein.",
        "<b>Khác biệt ở thụ thể tiếp nhận —</b> Exotoxin A gắn vào thụ thể LRP1 (CD91) trên bề mặt tế bào (trong khi độc tố bạch hầu gắn vào thụ thể HB-EGF).",
        "<b>Biểu hiện lâm sàng —</b> Góp phần gây hoại tử mô rộng lớn trong viêm phổi thở máy, nhiễm trùng huyết bỏng nặng và tổn thương loét giác mạc do Pseudomonas."
    ],
    "Cả hai vi khuẩn hoàn toàn khác nhau (vi khuẩn gram dương bạch hầu và vi khuẩn gram âm mủ xanh) đều sở hữu cùng một vũ khí phân tử tối thượng: ADP-ribosyl hóa bất hoạt eEF2."
))

cards.append(make_card(
    "HS10-B5-09",
    "Cơ chế gây độc của Ricin (Độc tố hạt Thầu dầu Ricinus communis)",
    "ĐỘC TỐ SINH HỌC DỊCH MÃ",
    "Trình bày cơ chế phân tử phá hủy ribosom 80S của độc tố Ricin từ hạt thầu dầu?",
    [
        "<b>Nguồn gốc tự nhiên —</b> Là một protein cực độc chiết xuất từ hạt cây thầu dầu (Ricinus communis); là một trong những vũ khí sinh học nguy hiểm nhất.",
        "<b>Cấu trúc heterodimer hai chuỗi —</b> Chuỗi B là một lectin gắn vào gốc galactose màng tế bào kích hoạt nhập bào; chuỗi A là enzym gây độc nội bào.",
        "<b>Hoạt tính enzym N-Glycosidase —</b> Chuỗi A của Ricin là một enzym N-glycosidase cực kỳ đặc hiệu đối với rRNA 28S của tiểu phần lớn 60S ribosom nhân thực.",
        "<b>Cắt đứt duy nhất một gốc Adenine A4324 —</b> Cắt đứt liên kết glycosid bẻ gãy duy nhất một gốc Adenine tại vị trí A4324 nằm trong vòng lặp sarcin-ricin được bảo tồn cao của rRNA 28S.",
        "<b>Tê liệt hoàn toàn Ribosom 80S —</b> Mất gốc adenine này làm ribosom không thể liên kết với các yếu tố kéo dài eEF1A và eEF2, dập tắt vĩnh viễn quá trình dịch mã, dẫn đến suy đa tạng tử vong nhanh chóng."
    ],
    "Tốc độ phá hủy của Ricin vô cùng khủng khiếp: một phân tử chuỗi A của Ricin có thể làm bất hoạt tới 1.500 ribosome mỗi phút."
))

cards.append(make_card(
    "HS10-B5-10",
    "Cơ chế làm đứt gãy dịch mã sớm của Puromycin",
    "CÔNG CỤ NGHIÊN CỨU DỊCH MÃ",
    "Trình bày cơ chế phân tử bắt chước aminoacyl-tRNA của Puromycin gây kết thúc dịch mã sớm?",
    [
        "<b>Kháng sinh chiết xuất từ Streptomyces alboniger —</b> Có cấu trúc hóa học tương đồng kỳ lạ với phần đầu 3' của phân tử Tyrosyl-tRNA.",
        "<b>Tiến thẳng vào vị trí A của Ribosom —</b> Nhờ hình dạng giống aminoacyl-tRNA, Puromycin tiến thẳng vào vị trí A của ribosom mà không cần yếu tố vận chuyển EF-Tu.",
        "<b>Tham gia tạo liên kết peptid —</b> Nhóm amin của Puromycin thực hiện phản ứng tấn công ái nhân vào chuỗi peptide tại vị trí P, tạo thành phân tử PEPTIDYL-PUROMYCIN.",
        "<b>Cắt đứt và giải phóng chuỗi cụt —</b> Liên kết giữa acid amin và phần còn lại của Puromycin là liên kết amide bền vững (thay vì liên kết este); chuỗi peptidyl-puromycin không thể chuyển vị và lập tức rơi ra khỏi ribosom, làm ngừng trệ dịch mã sớm.",
        "<b>Tác động lên CẢ NHÂN SƠ VÀ NHÂN THỰC —</b> Do cơ chế gắn tương đồng cấu trúc đơn giản, Puromycin ức chế dịch mã ở cả vi khuẩn lẫn tế bào người nên không dùng làm thuốc chữa bệnh mà là công cụ nghiên cứu sinh học phân tử kinh điển."
    ],
    "Trong công nghệ sinh học, gen kháng puromycin (pac mã hóa enzym puromycin N-acetyltransferase) thường được dùng làm dấu ấn chọn lọc để tìm các dòng tế bào chuyển gen thành công."
))

cards.append(make_card(
    "HS10-B5-11",
    "Cơ chế tác dụng của Kháng sinh Dược lý Cycloheximide",
    "CÔNG CỤ NGHIÊN CỨU DỊCH MÃ",
    "Nêu đích tác động và ứng dụng của Cycloheximide trong nghiên cứu sinh học phân tử?",
    [
        "<b>Đích tác động đặc hiệu trên Ribosom 80S —</b> Cycloheximide ức chế chọn lọc tiểu phần lớn 60S của ribosom tế bào NHÂN THỰC; hoàn toàn không có tác dụng lên ribosom 70S của vi khuẩn.",
        "<b>Ức chế bước chuyển vị (Translocation) —</b> Khóa chặt sự chuyển vị của tRNA và mRNA trên ribosome nhân thực.",
        "<b>Đình trệ kéo dài dịch mã —</b> Ngừng tức thì quá trình tổng hợp protein của tế bào động vật và nấm men.",
        "<b>Công cụ nghiên cứu thời gian bán hủy của Protein —</b> Thêm cycloheximide vào môi trường nuôi cấy tế bào để chặn đứng tổng hợp protein mới; sau đó đo sự suy giảm nồng độ protein theo thời gian qua Western blot để xác định chính xác tốc độ thoái hóa và thời gian bán hủy (t1/2) của protein mục tiêu."
    ],
    "Thí nghiệm Cycloheximide Chase là tiêu chuẩn vàng kinh điển để chứng minh một protein bị điều hòa thoái hóa qua con đường Proteasome hay con đường tiêu thể."
))

cards.append(make_card(
    "HS10-B5-12",
    "Tổng kết bảng đối chiếu cơ chế các Kháng sinh và Độc tố trên Ribosom",
    "TỔNG KẾT DƯỢC LÝ DỊCH MÃ",
    "Lập bảng đối chiếu phân loại đích tác động của các kháng sinh và độc chất sinh học chính trên bộ máy dịch mã?",
    [
        "<b>1. Tiểu phần 30S vi khuẩn —</b> Aminoglycosid (Streptomycin, Gentamicin: gây đọc sai mã và cố định phức hợp mở đầu); Tetracyclin (Doxycycline: phong bế vị trí A ngăn tRNA mới vào).",
        "<b>2. Tiểu phần 50S vi khuẩn —</b> Chloramphenicol (ức chế Peptidyl Transferase); Macrolid (Azithromycin, Erythromycin) & Clindamycin (tắc nghẽn đường hầm thoát và ức chế chuyển vị); Linezolid (ngăn chặn lắp ráp 70S).",
        "<b>3. Yếu tố kéo dài eEF2 nhân thực —</b> Ngoại độc tố Bạch hầu (Diphtheria toxin) và Exotoxin A của Pseudomonas (ADP-ribosyl hóa bất hoạt vĩnh viễn eEF2).",
        "<b>4. Tiểu phần 60S / rRNA 28S nhân thực —</b> Độc tố Ricin (cắt bỏ adenine A4324 của rRNA 28S); Cycloheximide (ức chế chuyển vị 80S).",
        "<b>5. Tác động cả Nhân sơ và Nhân thực —</b> Puromycin (gắn vị trí A làm kết thúc dịch mã sớm giải phóng chuỗi peptide cụt)."
    ],
    "Bảng đối chiếu này là nội dung xuất hiện thường trực trong các đề thi tuyển sinh Bác sĩ Nội trú và các kỳ thi cấp chứng chỉ hành nghề y khoa quốc tế."
))

# ==============================================================================
# SECTION B6: ĐIỀU HÒA BIỂU HIỆN GEN Ở NHÂN SƠ VÀ NHÂN THỰC (12 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-B6-01",
    "Khái niệm Cụm gen Operon ở Sinh vật nhân sơ",
    "ĐIỀU HÒA GEN NHÂN SƠ",
    "Định nghĩa cấu trúc Operon ở vi khuẩn và nêu chức năng của Promoter, Operator và các gen cấu trúc?",
    [
        "<b>Khái niệm Operon —</b> Cụm các gen cấu trúc có chức năng liên quan trong cùng một con đường chuyển hóa, được xếp kề nhau trên DNA và chịu sự điều hòa chung bởi một Promoter và một Operator duy nhất.",
        "<b>Vùng khởi động Promoter (P) —</b> Đoạn trình tự DNA đặc hiệu nơi enzyme RNA Polymerase nhận diện và liên kết để khởi đầu phiên mã.",
        "<b>Vùng vận hành Operator (O) —</b> Đoạn trình tự DNA nằm xen giữa hoặc kế tiếp Promoter; là vị trí liên kết đặc hiệu của Protein điều hòa (Protein ức chế Repressor hoặc Protein hoạt hóa Activator).",
        "<b>Các gen cấu trúc (Structural genes) —</b> Trình tự mã hóa cho các chuỗi polypeptide enzyme; được phiên mã cùng nhau thành một phân tử mRNA polycistronic duy nhất.",
        "<b>Gen điều hòa (Regulatory gene) —</b> Nằm ngoài operon; liên tục phiên mã mức độ nền tạo protein điều hòa."
    ],
    "Cấu trúc operon giúp vi khuẩn phản ứng cực kỳ nhanh nhạy với sự thay đổi của môi trường: chỉ cần bật hoặc tắt một công tắc duy nhất là điều khiển đồng loạt toàn bộ con đường enzyme."
))

cards.append(make_card(
    "HS10-B6-02",
    "Cấu trúc Operon Lac và chức năng của 3 gen lacZ, lacY, lacA",
    "MÔ HÌNH OPERON LAC",
    "Mô tả cấu trúc của Operon Lac ở E. coli và nêu chức năng sinh hóa của 3 enzyme do lacZ, lacY, lacA mã hóa?",
    [
        "<b>Mô hình cảm ứng kinh điển của Jacob & Monod (Nobel 1965) —</b> Kiểm soát quá trình vận chuyển và thoái hóa đường Lactose ở vi khuẩn E. coli.",
        "<b>Gen cấu trúc lacZ —</b> Mã hóa enzyme β-GALACTOSIDASE; xúc tác thủy phân lactose thành Glucose và Galactose; đồng thời xúc tác phản ứng phụ đồng phân hóa một lượng nhỏ lactose thành ALLOLACTOSE.",
        "<b>Gen cấu trúc lacY —</b> Mã hóa protein vận chuyển màng LACTOSE PERMEASE; bơm chủ động đưa đường lactose từ môi trường xuyên qua màng sinh chất vào trong tế bào chất.",
        "<b>Gen cấu trúc lacA —</b> Mã hóa enzyme THIOGALACTOSIDE TRANSACETYLASE; chuyển nhóm acetyl giải độc các dẫn xuất thiogalactoside phi chuyển hóa.",
        "<b>Gen điều hòa lacI —</b> Nằm phía trước operon; mã hóa protein ức chế LacI liên tục được tổng hợp ở trạng thái hoạt tính."
    ],
    "Cả 3 gen lacZ, lacY, lacA được phiên mã chung thành một phân tử mRNA polycistronic dài; sự biểu hiện của chúng tăng vọt gấp hơn 1.000 lần khi môi trường có lactose."
))

cards.append(make_card(
    "HS10-B6-03",
    "Điều hòa âm tính Operon Lac: Vai trò của Protein ức chế LacI và Allolactose",
    "MÔ HÌNH OPERON LAC",
    "Trình bày cơ chế điều hòa âm tính của Operon Lac khi môi trường không có Lactose so với khi có Lactose?",
    [
        "<b>Khi môi trường KHÔNG CÓ LACTOSE (Operon bị Khóa) —</b> Protein ức chế LacI tự do ở cấu hình hoạt động, gắn chặt vào vùng Operator (O); sự hiện diện của LacI chắn đường đi của RNA Polymerase, ngăn không cho enzyme phiên mã cụm gen lacZ, lacY, lacA (chỉ có rò rỉ phiên mã mức nền cực thấp).",
        "<b>Khi môi trường CÓ LACTOSE (Operon được Mở) —</b> Một lượng nhỏ lactose vào tế bào được β-galactosidase chuyển thành chất đồng phân ALLOLACTOSE.",
        "<b>Allolactose là Chất cảm ứng (Inducer) —</b> Allolactose gắn dị lập thể vào protein ức chế LacI, làm biến đổi cấu hình không gian của LacI.",
        "<b>LacI tách rời khỏi Operator —</b> Phức hợp [LacI - Allolactose] mất ái lực và tách rời khỏi vùng Operator; giải phóng lối đi cho RNA Polymerase bắt đầu phiên mã."
    ],
    "Chất cảm ứng nhân tạo IPTG (Isopropyl β-D-1-thiogalactopyranoside) có cấu trúc tương tự allolactose nhưng không bị β-galactosidase phân hủy, được dùng phổ biến trong phòng thí nghiệm để kích thích biểu hiện protein tái tổ hợp."
))

cards.append(make_card(
    "HS10-B6-04",
    "Điều hòa dương tính Operon Lac qua nồng độ Glucose, cAMP và Protein CAP",
    "MÔ HÌNH OPERON LAC",
    "Giải thích cơ chế ức chế dị hóa (Catabolite Repression) của Glucose thông qua phân tử tín hiệu cAMP và protein CAP?",
    [
        "<b>Ưu tiên sử dụng Glucose (Chất chuyển hóa ưa thích số 1) —</b> E. coli ưu tiên sử dụng glucose; nếu môi trường có sẵn glucose, vi khuẩn sẽ không lãng phí năng lượng để thoái hóa lactose.",
        "<b>Khi nồng độ Glucose CAO —</b> Sự vận chuyển glucose vào tế bào ức chế enzyme Adenylyl Cyclase; nồng độ cAMP nội bào GIẢM RẤT THẤP.",
        "<b>Khi nồng độ Glucose THẤP HOẶC CẠN KIỆT —</b> Enzyme Adenylyl Cyclase được kích hoạt giải phóng; nồng độ cAMP nội bào TĂNG VỌT.",
        "<b>Phức hợp cAMP - CAP (Catabolite Activator Protein) —</b> Phân tử cAMP gắn vào protein hoạt hóa CAP (còn gọi là CRP), kích hoạt CAP chuyển sang cấu hình hoạt động.",
        "<b>Gắn vào vị trí CAP trên Promoter —</b> Phức hợp [cAMP-CAP] gắn vào vị trí gắn đặc hiệu phía trước Promoter, làm bẻ cong DNA một góc 90°, giúp tuyển dụng và tăng cường ái lực gắn của RNA Polymerase lên Promoter gấp hàng chục lần."
    ],
    "Sự kết hợp giữa điều hòa âm tính (qua LacI) và điều hòa dương tính (qua cAMP-CAP) hoạt động như một mạch logic nhị phân tinh vi (Cổng AND): gen chỉ được bật phiên mã mạnh nhất khi THIẾU GLUCOSE VÀ CÓ MẶT LACTOSE."
))

cards.append(make_card(
    "HS10-B6-05",
    "Bốn trạng thái chuyển hóa của Operon Lac trong tự nhiên",
    "MÔ HÌNH OPERON LAC",
    "Phân tích trạng thái hoạt động của Operon Lac trong 4 điều kiện môi trường dinh dưỡng khác nhau?",
    [
        "<b>1. Có Glucose và Không có Lactose —</b> LacI gắn vào Operator; cAMP thấp nên CAP không gắn; OPERON BỊ KHÓA HOÀN TOÀN (Phiên mã = 0).",
        "<b>2. Không có Glucose và Không có Lactose —</b> cAMP cao nên cAMP-CAP gắn vào Promoter, NHƯNG LacI vẫn gắn chặt vào Operator chặn đường; OPERON VẪN BỊ KHÓA (Phiên mã = 0).",
        "<b>3. Có Glucose và Có Lactose —</b> Allolactose tách LacI khỏi Operator; nhưng Glucose cao làm cAMP thấp nên CAP không gắn kích hoạt; OPERON CHỈ PHIÊN MÃ Ở MỨC ĐỘ NỀN THẤP (Low basal level).",
        "<b>4. KHÔNG CÓ GLUCOSE VÀ CÓ LACTOSE (Trạng thái tối ưu duy nhất) —</b> LacI bị allolactose tách rời khỏi Operator VÀ phức hợp cAMP-CAP gắn chặt vào Promoter; OPERON PHIÊN MÃ TỐI ĐA BÙNG NỔ (High transcription level)."
    ],
    "Đây là câu hỏi kinh điển luôn có mặt trong các kỳ thi: nhớ rõ rằng có mặt lactose đơn thuần chưa đủ để operon phiên mã tối đa, bắt buộc phải kèm theo điều kiện nồng độ glucose môi trường sụt giảm."
))

cards.append(make_card(
    "HS10-B6-06",
    "Mô hình Operon Tryptophan (Operon Trp) và Cơ chế Suy giảm (Attenuation)",
    "OPERON TRYPTOPHAN",
    "So sánh Operon Trp (operon kìm hãm) với Operon Lac và giải thích cơ chế suy giảm phiên mã (Attenuation)?",
    [
        "<b>Operon kìm hãm tổng hợp (Repressible Operon) —</b> Mã hóa 5 enzyme sinh tổng hợp acid amin Tryptophan; hoạt động khi thiếu Trp và bị dập tắt khi môi trường dư thừa Trp.",
        "<b>Trp là Chất đồng ức chế (Corepressor) —</b> Khi Tryptophan dư thừa, nó gắn vào protein ức chế TrpR aporepressor biến đổi thành cấu hình hoạt tính gắn vào Operator chặn phiên mã.",
        "<b>Cơ chế suy giảm phiên mã (Attenuation) —</b> Cơ chế tinh chỉnh phụ thuộc vào sự bắt cặp đồng thời giữa dịch mã đoạn peptide dẫn đầu (Leader peptide) và phiên mã.",
        "<b>Khi nồng độ Tryptophan CAO —</b> Ribosome dịch mã nhanh chóng qua 2 codon Trp trên đoạn dẫn đầu, che phủ vùng 2; làm vùng 3 bắt cặp với vùng 4 tạo CẤU TRÚC KẸP TÓC KẾT THÚC PHIÊN MÃ (3-4 Terminator hairpin), đẩy RNA Polymerase rơi ra khỏi DNA chấm dứt sớm phiên mã.",
        "<b>Khi nồng độ Tryptophan THẤP —</b> Ribosome bị khựng lại tại 2 codon Trp do thiếu Trp-tRNA; vùng 2 rảnh rỗi bắt cặp với vùng 3 tạo CẤU TRÚC KẸP TÓC CHỐNG DỪNG (2-3 Antiterminator hairpin), cho phép RNA Polymerase tiếp tục phiên mã toàn bộ operon."
    ],
    "Cơ chế Attenuation chỉ có thể tồn tại ở sinh vật nhân sơ nhờ hiện tượng phiên mã và dịch mã diễn ra song hành cùng lúc trong cùng một khoang tế bào chất."
))

cards.append(make_card(
    "HS10-B6-07",
    "Điều hòa Dịch mã ở Sinh vật nhân thực qua Phosphoryl hóa Yếu tố eIF2",
    "ĐIỀU HÒA DỊCH MÃ NHÂN THỰC",
    "Trình bày cơ chế điều hòa tốc độ dịch mã chung của tế bào nhân thực thông qua quá trình phosphoryl hóa yếu tố mở đầu eIF2?",
    [
        "<b>Yếu tố eIF2 và Chu trình GTP —</b> eIF2 gắn GTP vận chuyển Met-tRNA vào tiểu phần 40S; sau khi thủy phân GTP tạo eIF2-GDP, yếu tố trao đổi nucleotide eIF2B phải nạp lại GTP cho eIF2.",
        "<b>Phosphoryl hóa tiểu phần α của eIF2 —</b> Khi tế bào gặp stress (nhiễm virus, đói acid amin, tích tụ protein hỏng trong ER), các enzyme kinase chuyên biệt phosphoryl hóa gốc Serin 51 trên tiểu phần α của eIF2 (tạo eIF2-P).",
        "<b>Bẫy và Bất hoạt yếu tố eIF2B —</b> Phân tử eIF2-P liên kết cực kỳ chặt chẽ với eIF2B và không giải phóng; do nồng độ eIF2B trong tế bào thấp hơn eIF2 nhiều lần, toàn bộ eIF2B bị bẫy và bất hoạt hoàn toàn.",
        "<b>Đình trệ dịch mã toàn thể tế bào —</b> Không thể tái tạo eIF2-GTP, tốc độ dịch mã chung của toàn bộ tế bào sụt giảm mạnh mẽ để bảo tồn năng lượng vượt qua stress."
    ],
    "Khi tế bào bị nhiễm virus, thụ thể PKR kinase nhận diện RNA sợi đôi của virus và lập tức phosphoryl hóa eIF2, chặn đứng cỗ máy dịch mã để ngăn cản virus nhân lên."
))

cards.append(make_card(
    "HS10-B6-08",
    "Điều hòa tổng hợp Globin bởi Heme qua Kinase HRI trong tế bào hồng cầu",
    "ĐIỀU HÒA TỔNG HỢP GLOBIN",
    "Phân tích cơ chế phân tử giúp hồng cầu đồng bộ hóa tốc độ tổng hợp chuỗi Globin với lượng Hem sẵn có nhờ Kinase HRI?",
    [
        "<b>Mục đích sinh học —</b> Chuỗi Globin chỉ được phép tổng hợp khi có đủ nhóm ngoại Hem để tạo Hemoglobin; nếu thiếu Hem mà vẫn tổng hợp Globin, chuỗi Globin tự do sẽ bị kết tủa thành các thể vùi làm vỡ hồng cầu.",
        "<b>Enzym HRI (Heme-Regulated Inhibitor kinase) —</b> Là một protein kinase chuyên biệt có mặt trong các tế bào tiền thân hồng cầu, có khả năng cảm biến trực tiếp nồng độ Hem nội bào.",
        "<b>Khi nồng độ Hem DỒI DÀO —</b> Phân tử Hem gắn trực tiếp vào hai vị trí điều hòa trên enzym HRI, BẤT HOẠT HOÀN TOÀN KINASE HRI; eIF2 không bị phosphoryl hóa nên quá trình dịch mã chuỗi Globin diễn ra với công suất tối đa.",
        "<b>Khi nồng độ Hem THIẾU HỤT —</b> HRI tự do được giải phóng và tự phosphoryl hóa hoạt hóa; HRI hoạt động phosphoryl hóa eIF2, làm bất hoạt eIF2B và ĐÌNH TRỆ NGAY LẬP TỨC QUÁ TRÌNH DỊCH MÃ CHUỖI GLOBIN."
    ],
    "Cơ chế điều hòa bởi kinase HRI bảo đảm sự cân bằng tuyệt đối giữa tốc độ tổng hợp phần hem và phần globin trong quá trình tạo máu."
))

cards.append(make_card(
    "HS10-B6-09",
    "Điều hòa Biểu sinh (Epigenetics): Acetyl hóa Histone bởi HAT vs. HDAC",
    "ĐIỀU HÒA BIỂU SINH EPIGENETICS",
    "Phân tích cơ chế phân tử của quá trình Acetyl hóa và Deacetyl hóa Histone tác động lên cấu trúc Chromatin và phiên mã gen?",
    [
        "<b>Điện tích dương của đuôi Histone —</b> Các phân tử protein Histone (H2A, H2B, H3, H4) giàu các acid amin kiềm tích điện dương (Lysin, Arginin), tạo lực hút tĩnh điện cực mạnh với khung đường-phosphat mang điện tích âm của DNA tạo chất nhiễm sắc đóng chặt (Heterochromatin).",
        "<b>Enzym Histone Acetyltransferase (HAT) —</b> Chuyển nhóm acetyl (-COCH3) từ Acetyl-CoA gắn vào nhóm ε-amino của gốc Lysin trên đuôi histone; phản ứng này TRUNG HÒA HOÀN TOÀN ĐIỆN TÍCH DƯƠNG của Lysin.",
        "<b>Mở lỏng Chromatin (Euchromatin) và Kích hoạt Phiên mã —</b> Mất lực hút tĩnh điện làm chuỗi DNA bung tháo lỏng lẻo rời khỏi hạt nucleosome, cho phép RNA Polymerase và các yếu tố phiên mã tiếp cận gen để HOẠT HÓA PHIÊN MÃ.",
        "<b>Enzym Histone Deacetylase (HDAC) —</b> Cắt bỏ nhóm acetyl, hoàn trả lại điện tích dương cho histone; làm DNA cuộn chặt trở lại thành dị nhiễm sắc (Heterochromatin), GÂY CÂM LẶNG PHIÊN MÃ GEN.",
        "<b>Ứng dụng dược lý điều trị ung thư —</b> Thuốc ức chế HDAC (HDAC Inhibitors như Vorinostat, Romidepsin) giữ chromatin ở trạng thái mở, tái kích hoạt các gen ức chế khối u bị câm lặng, dùng điều trị u lympho tế bào T."
    ],
    "Quy tắc nhớ cốt tử: Acetyl hóa Histone = Mở gen (Kích hoạt phiên mã); Deacetyl hóa Histone = Đóng gen (Câm lặng phiên mã)."
))

cards.append(make_card(
    "HS10-B6-10",
    "Điều hòa Biểu sinh: Methyl hóa DNA tại các đảo CpG và Câm lặng gen",
    "METHYL HÓA DNA",
    "Trình bày cơ chế methyl hóa DNA tại các đảo CpG bởi enzym DNMT và các hiện tượng sinh học liên quan?",
    [
        "<b>Enzym DNA Methyltransferase (DNMT) —</b> Xúc tác chuyển nhóm methyl (-CH3) từ phân tử SAM gắn vào vị trí carbon số 5 của vòng base Cytosine, tạo thành 5-METHYLCYTOSINE (5-mC).",
        "<b>Vị trí đảo CpG (CpG Islands) —</b> Phản ứng xảy ra chủ yếu tại các dinucleotide CpG (cytosine đi trước guanine nối qua liên kết phosphat); các đảo CpG thường tập trung mật độ cao tại vùng Promoter của các gen.",
        "<b>Cơ chế câm lặng gen bền vững —</b> Nhóm methyl nhô vào rãnh lớn của chuỗi xoắn kép DNA, ngăn cản trực tiếp các yếu tố phiên mã liên kết; đồng thời thu hút các protein gắn methyl (MeCP2) tuyển dụng phức hợp HDAC đóng chặt chromatin, GÂY DẬP TẮT VĨNH VIỄN PHIÊN MÃ GEN.",
        "<b>Di truyền qua phân bào (Epigenetic Inheritance) —</b> Mô hình methyl hóa được enzym duy trì DNMT1 sao chép chính xác sang sợi DNA mới sau mỗi lần nhân đôi tế bào.",
        "<b>Các hiện tượng sinh học kinh điển —</b> Hiện tượng bất hoạt một nhiễm sắc thể X ở nữ giới tạo thể Barr; Dấu ấn di truyền theo nguồn gốc bố mẹ (Genomic Imprinting trong hội chứng Prader-Willi / Angelman); và sự câm lặng bất thường của các gen ức chế khối u trong ung thư học."
    ],
    "Thuốc ức chế men DNA methyltransferase (như Azacitidine, Decitabine) làm giảm methyl hóa DNA, giúp tái kích hoạt các gen ức chế khối u, là vũ khí điều trị Hội chứng rối loạn sinh tủy (MDS) và bệnh bạch cầu cấp."
))

cards.append(make_card(
    "HS10-B6-11",
    "Can thiệp RNA (RNA Interference - RNAi) qua MicroRNA (miRNA)",
    "CAN THIỆP RNA VÀ miRNA",
    "Trình bày con đường sinh tổng hợp của MicroRNA (miRNA) và cơ chế ức chế biểu hiện gen của Phức hợp RISC?",
    [
        "<b>Bản chất phân tử miRNA —</b> Là các phân tử RNA sợi đơn ngắn gồm 21 đến 25 nucleotide không mã hóa protein, được phiên mã từ hệ gen nội sinh của tế bào nhân thực.",
        "<b>Xử lý qua hai bước enzym —</b> 1) Trong nhân: enzym Drosha cắt tiền chất pri-miRNA thành pre-miRNA hình kẹp tóc; pre-miRNA được xuất ra bào tương qua Exportin-5; 2) Ngoài bào tương: enzym endonuclease DICER cắt pre-miRNA thành đoạn duplex miRNA ngắn 22 bp.",
        "<b>Tích hợp vào Phức hợp RISC —</b> Đoạn RNA sợi đơn dẫn đường được nạp vào Phức hợp câm lặng gen cảm ứng bởi RNA (RNA-Induced Silencing Complex - RISC) chứa protein cốt lõi ARGONAUTE (Ago).",
        "<b>Cơ chế ức chế biểu hiện gen —</b> Phức hợp [RISC-miRNA] tìm đến bắt cặp bổ sung (thường không hoàn toàn) với vùng 3'-UTR của các phân tử mRNA đích.",
        "<b>Hậu quả phân tử —</b> Bắt cặp bổ sung không hoàn toàn dẫn tới ỨC CHẾ DỊCH MÃ và thúc đẩy cắt ngắn đuôi polyA làm thoái hóa mRNA; nếu bắt cặp hoàn hảo 100% (như ở siRNA) protein Argonaute sẽ trực tiếp cắt đứt đôi phân tử mRNA."
    ],
    "Khám phá về hiện tượng Can thiệp RNA của Andrew Fire và Craig Mello (Giải Nobel Y học 2006) và phát hiện ra MicroRNA của Victor Ambros và Gary Ruvkun (Giải Nobel Y học 2024) đã mở ra kỷ nguyên mới về liệu pháp gen sử dụng RNA can thiệp (siRNA therapeutics)."
))

cards.append(make_card(
    "HS10-B6-12",
    "Tổng kết các tầng mức điều hòa biểu hiện gen ở Sinh vật nhân thực",
    "TỔNG KẾT ĐIỀU HÒA BIỂU HIỆN GEN",
    "Liệt kê 6 tầng mức kiểm soát biểu hiện gen từ DNA đến Protein hoạt tính ở tế bào nhân thực?",
    [
        "<b>1. Mức độ Cấu trúc Chromatin & Biểu sinh —</b> Đóng mở chất nhiễm sắc qua Acetyl hóa Histone (HAT/HDAC) và Methyl hóa DNA đảo CpG.",
        "<b>2. Mức độ Khởi đầu Phiên mã (Quan trọng nhất) —</b> Tương tác giữa các yếu tố phiên mã đặc hiệu (Activators, Repressors) với các vùng tăng cường (Enhancers) và vùng bất hoạt (Silencers).",
        "<b>3. Mức độ Hoàn thiện và Cắt nối sau phiên mã —</b> Cắt nối chọn lọc (Alternative Splicing tạo nhiều protein từ 1 gen), biên tập RNA (RNA editing như tạo ApoB-48 ở ruột vs ApoB-100 ở gan).",
        "<b>4. Mức độ Vận chuyển và Định vị mRNA —</b> Kiểm soát xuất mRNA qua lỗ màng nhân ra tế bào chất.",
        "<b>5. Mức độ Dịch mã —</b> Điều hòa qua phosphoryl hóa yếu tố mở đầu eIF2/eIF4E; can thiệp RNA qua MicroRNA (miRNA) gắn vùng 3'-UTR.",
        "<b>6. Mức độ Sau dịch mã và Thoái hóa Protein —</b> Biến đổi cộng hóa trị PTM (phosphoryl hóa, zymogen) và thoái hóa có chọn lọc qua hệ thống Ubiquitin - Proteasome 26S."
    ],
    "Mạng lưới điều hòa đa tầng đảm bảo rằng mỗi loại tế bào biệt hóa trong cơ thể (như tế bào nơ-ron, tế bào gan, tế bào cơ) dù mang cùng một bộ gen DNA giống hệt nhau nhưng biểu hiện ra các bộ protein hoàn toàn khác biệt."
))

# ==============================================================================
# SECTION B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS10-ALGO-01",
    "Phân tầng Kháng sinh theo vị trí đích tác động trên Ribosom vi khuẩn",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước phân tầng các nhóm Kháng sinh ức chế dịch mã theo đích tác động trên Ribosom 70S?",
    [
        "<b>Bước 1 (Xác định nhóm tác động lên TIỂU PHẦN NHỎ 30S) —</b> Mẹo nhớ: 'AT 30' = AMINOGLYCOSID (Streptomycin, Gentamicin: gắn 16S rRNA gây đọc sai mã diệt khuẩn) và TETRACYCLIN (Doxycycline: phong bế vị trí A ngăn aminoacyl-tRNA vào kìm khuẩn).",
        "<b>Bước 2 (Xác định nhóm ức chế Peptidyl Transferase trên TIỂU PHẦN 50S) —</b> CHLORAMPHENICOL: gắn rRNA 23S khóa tạo liên kết peptid (nguy cơ ức chế tủy xương và hội chứng xám).",
        "<b>Bước 3 (Xác định nhóm ức chế Chuyển vị Ribosom trên TIỂU PHẦN 50S) —</b> Mẹo nhớ: 'CEL 50' = CLINDAMYCIN và MACROLID (Erythromycin, Azithromycin: tắc nghẽn đường hầm thoát peptid và chặn chuyển vị).",
        "<b>Bước 4 (Xác định nhóm ngăn chặn Lắp ráp phức hợp 70S) —</b> LINEZOLID: gắn 50S ức chế tạo phức hợp 70S mở đầu (đặc trị MRSA và VRE)."
    ],
    "Cây quyết định phân loại kháng sinh ribosome 70S: 30S (Aminoglycosid, Tetracyclin) vs 50S (Chloramphenicol, Macrolid, Clindamycin, Linezolid) là sơ đồ phản xạ không thể thiếu trong các kỳ thi lâm sàng.",
    algo=True
))

cards.append(make_card(
    "HS10-ALGO-02",
    "Lưu đồ 4 trạng thái hoạt động của Operon Lac theo nguồn Carbon",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán quyết định trạng thái hoạt động của Operon Lac dựa trên nồng độ Glucose và Lactose môi trường?",
    [
        "<b>Bước 1 (Kiểm tra sự có mặt của Lactose) —</b> Nếu KHÔNG CÓ LACTOSE → Protein ức chế LacI gắn chặt vào Operator → OPERON BỊ KHÓA HOÀN TOÀN (Phiên mã = 0) bất kể nồng độ glucose cao hay thấp.",
        "<b>Bước 2 (Nếu CÓ LACTOSE: Allolactose tách LacI khỏi Operator) —</b> Bước tiếp theo phụ thuộc hoàn toàn vào nồng độ GLUCOSE để quyết định mức độ phiên mã.",
        "<b>Bước 3 (Nếu CÓ GLUCOSE CAO) —</b> Adenylyl cyclase bị ức chế → cAMP nội bào thấp → CAP không hoạt hóa → Không có phức hợp cAMP-CAP hỗ trợ → OPERON CHỈ PHIÊN MÃ MỨC ĐỘ NỀN THẤP (Low basal transcription).",
        "<b>Bước 4 (Nếu THIẾU GLUCOSE: Trạng thái bùng nổ tối đa) —</b> cAMP tăng vọt → Phức hợp cAMP-CAP bám vào Promoter thu hút RNA Polymerase → OPERON PHIÊN MÃ MẠNH MẼ BÙNG NỔ (High transcription level)."
    ],
    "Quy tắc vàng phân tích câu hỏi Operon Lac: Kiểm tra Operator (Lactose có/không) trước để biết gen có bị khóa không; sau đó kiểm tra Promoter (Glucose có/không qua cAMP-CAP) để biết mức độ phiên mã mạnh hay yếu.",
    algo=True
))

cards.append(make_card(
    "HS10-ALGO-03",
    "Phân biệt cơ chế tác dụng phân tử của các Độc tố sinh học ức chế dịch mã",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước phân biệt cơ chế phân tử của Ngoại độc tố Bạch hầu, Exotoxin A, Ricin và Puromycin?",
    [
        "<b>Bước 1 (Cơ chế ADP-ribosyl hóa yếu tố eEF2) —</b> Ngoại độc tố Bạch hầu (Corynebacterium diphtheriae) và Exotoxin A (Pseudomonas aeruginosa): chuyển ADP-ribose từ NAD⁺ gắn vào Diphthamide trên eEF2, bất hoạt vĩnh viễn eEF2 làm ngừng chuyển vị dịch mã nhân thực.",
        "<b>Bước 2 (Cơ chế cắt RNA phân giải rRNA 28S) —</b> Độc tố RICIN (hạt thầu dầu): hoạt tính N-glycosidase cắt bỏ duy nhất gốc Adenine A4324 khỏi rRNA 28S của tiểu phần 60S làm tê liệt ribosom 80S nhân thực.",
        "<b>Bước 3 (Cơ chế gắn vào vị trí A tạo chuỗi peptide cụt) —</b> PUROMYCIN: bắt chước hình thái tyrosyl-tRNA tiến vào vị trí A tạo liên kết peptidyl-puromycin làm đứt gãy kết thúc dịch mã sớm ở cả nhân sơ và nhân thực.",
        "<b>Bước 4 (Cơ chế ức chế ribosome 60S đặc hiệu nhân thực) —</b> CYCLOHEXIMIDE: ức chế chọn lọc chuyển vị trên ribosome 80S nhân thực, dùng làm công cụ nghiên cứu thời gian bán hủy protein."
    ],
    "Cây quyết định giúp phân loại nhanh chóng các độc chất sinh học: ADP-ribosyl hóa eEF2 (Bạch hầu, Pseudomonas) vs Cắt rRNA 28S (Ricin) vs Bắt chước tRNA kết thúc sớm (Puromycin).",
    algo=True
))

cards.append(make_card(
    "HS10-ALGO-04",
    "Lưu đồ 4 giai đoạn Dịch mã và Tính toán năng lượng ATP/GTP",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 giai đoạn dịch mã và công thức tính toán chi phí năng lượng tổng hợp chuỗi polypeptid?",
    [
        "<b>Giai đoạn 1 (Hoạt hóa Acid amin ngoài bào tương) —</b> Acid amin + ATP + tRNA → Aminoacyl-tRNA + AMP + 2 Pi (Tiêu tốn 2 liên kết cao năng ~P từ ATP).",
        "<b>Giai đoạn 2 (Mở đầu chuỗi tại Ribosom) —</b> Lắp ráp ribosom và đưa fMet/Met-tRNA vào vị trí P (Tiêu tốn 1 liên kết cao năng từ 1 GTP do IF2/eIF2).",
        "<b>Giai đoạn 3 (Kéo dài chuỗi - 3 bước tuần hoàn lặp lại) —</b> Mỗi chu kỳ gắn thêm 1 acid amin tiêu tốn: 1 GTP (đưa tRNA vào vị trí A nhờ EF-Tu/eEF1A) + 1 GTP (chuyển vị ribosom nhờ EF-G/eEF2); Tổng cộng 2 liên kết cao năng ~P từ GTP cho mỗi acid amin kéo dài.",
        "<b>Giai đoạn 4 (Kết thúc chuỗi) —</b> Nhận diện codon dừng qua Release Factors và tháo rời ribosome (Tiêu tốn 1 liên kết cao năng từ 1 GTP).",
        "<b>Công thức tính toán tổng năng lượng —</b> Tổng số liên kết phosphat cao năng (~P) để tổng hợp chuỗi polypeptide gồm N acid amin: Tổng ~P = 4N (với 2N từ ATP và 2N từ GTP)."
    ],
    "Lưu đồ và công thức 4N là công cụ bỏ túi giúp tính toán chính xác tuyệt đối bất kỳ bài toán năng lượng dịch mã nào trong các kỳ thi lý thuyết sinh hóa.",
    algo=True
))

cards.append(make_card(
    "HS10-ALGO-05",
    "Phân tầng các cơ chế Điều hòa Biểu sinh (Epigenetics)",
    "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
    "Lưu đồ thuật toán 4 bước phân tầng các cơ chế biến đổi Biểu sinh kiểm soát biểu hiện gen?",
    [
        "<b>Bước 1 (Đánh giá Acetyl hóa Histone qua enzym HAT vs HDAC) —</b> HAT (Histone Acetyltransferase) trung hòa điện tích dương Lysin → MỞ CHROMATIN (Euchromatin) → KÍCH HOẠT PHIÊN MÃ; HDAC (Histone Deacetylase) phục hồi điện tích dương → ĐÓNG CHẶT CHROMATIN (Heterochromatin) → CÂM LẶNG PHIÊN MÃ.",
        "<b>Bước 2 (Đánh giá Methyl hóa DNA qua enzym DNMT) —</b> DNMT gắn nhóm methyl vào carbon 5 của cytosine tại các đảo CpG vùng Promoter → Thu hút protein gắn methyl MeCP2 tuyển dụng HDAC → CÂM LẶNG PHIÊN MÃ BỀN VỮNG qua phân bào (bất hoạt NST X thể Barr, imprinting).",
        "<b>Bước 3 (Đánh giá Methyl hóa Histone) —</b> Phức tạp tùy vị trí acid amin: H3K4me3 kích hoạt phiên mã; ngược lại H3K9me3 và H3K27me3 câm lặng phiên mã bền vững.",
        "<b>Bước 4 (Đánh giá Can thiệp RNA qua MicroRNA - miRNA) —</b> Dicer cắt tạo miRNA ngắn 22 nt → nạp vào phức hợp RISC (Argonaute) → bắt cặp bổ sung vùng 3'-UTR của mRNA đích → ỨC CHẾ DỊCH MÃ HOẶC PHÂN HỦY mRNA."
    ],
    "Cây quyết định giúp tổng kết trọn vẹn 3 trụ cột của Di truyền Biểu sinh hiện đại: Biến đổi đuôi Histone (Acetyl/Methyl) + Methyl hóa DNA + Can thiệp RNA không mã hóa (miRNA/siRNA).",
    algo=True
))

# ==============================================================================
# XUẤT FILE CARDS V2 JSON
# ==============================================================================

out_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-10_Sinh_tong_hop_protein")
cards_file = out_dir / "HS-10_Sinh_tong_hop_protein.cards.v2.json"

output_data = {
    "cards": cards,
    "total": len(cards),
    "version": "v2"
}

with open(cards_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Đã tạo thành công {len(cards)} thẻ Master chuyên sâu cho HS-10 tại:")
print(f"-> {cards_file}")
