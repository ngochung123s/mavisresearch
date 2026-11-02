# -*- coding: utf-8 -*-
"""build_deep_hs14.py - Generate 71 exhaustive master flashcards for HS-14 (Cấu trúc màng tế bào, kênh ion, vận chuyển tích cực và bệnh lý màng)"""
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
  <span style="background-color: #ffd43b; color: #212529; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Gợi ý</span> Nhớ lại cấu trúc hóa sinh màng, cơ chế kênh ion và bệnh lý phân tử.
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
        "extra": extra or "Nguồn: Giáo trình Hóa Sinh Y Học - ĐHYHN (GS. Tạ Thành Văn, Tr. 304-322), Lehninger Principles of Biochemistry 8th ed (Chap 11), Harper's Illustrated Biochemistry 32nd ed (Chap 40).",
        "tags": ["hoasinh", "HS14", section]
    }

cards = []

# ==============================================================================
# B1: CẤU TRÚC VÀ ĐẶC TÍNH SINH HỌC CỦA MÀNG TẾ BÀO (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B1-01", "Mô hình Khảm động", "CẤU TRÚC MÀNG",
    "Nêu 2 đặc trưng cốt lõi của Mô hình Khảm động (Fluid Mosaic Model) theo Singer & Nicolson (1972)?",
    [
        "Tính chất khảm (Mosaic): Màng cấu tạo từ lớp lipid kép đóng vai trò nền tảng, xen kẽ các phân tử protein xuyên màng (integral) hoặc protein ngoại vi (peripheral) phân bố bất đối xứng.",
        "Tính chất lỏng động (Fluid): Lớp lipid kép và protein tồn tại ở trạng thái tinh thể lỏng ở 37°C, có khả năng chuyển động nhiệt tự do linh hoạt trong mặt phẳng màng."
    ],
    "Mô hình khảm động ra đời năm 1972 đã thay thế hoàn toàn mô hình bánh kẹp tĩnh (sandwich) của Davson-Danielli, giải thích trọn vẹn khả năng biến dạng, hòa màng và truyền tín hiệu tế bào."
))

cards.append(make_card(
    "HS14-B1-02", "Thành phần Glycerophospholipid", "LIPID MÀNG",
    "Nêu đặc điểm phân bố và vai trò sinh học của 5 loại Glycerophospholipid chính cấu thành màng tế bào?",
    [
        "Phosphatidylcholin (PC / Lecithin): Chiếm tỷ lệ cao nhất ở lá ngoài, zwitterion trung hòa điện tích ở pH sinh lý.",
        "Phosphatidylethanolamin (PE / Cephalin): Chiếm ưu thế ở lá trong, đầu phân cực nhỏ giúp tạo độ uốn cong màng.",
        "Phosphatidylserin (PS): Phân bố độc quyền ở lá trong tế bào bình thường, mang điện tích âm thuần (-1) ở pH sinh lý.",
        "Phosphatidylinositol (PI): Ở lá trong, tiền chất của PIP2 bị cắt bởi Phospholipase C tạo IP3 và DAG truyền tin.",
        "Cardiolipin (Diphosphatidylglycerol): Phospholipid đặc hiệu chứa 4 chuỗi acyl béo, chiếm 20% lipid màng trong ty thể, ổn định chuỗi hô hấp tế bào."
    ],
    "Cardiolipin chỉ có ở màng trong ty thể và màng vi khuẩn (bằng chứng thuyết nội cộng sinh); kháng thể kháng cardiolipin gặp trong hội chứng kháng phospholipid (APS)."
))

cards.append(make_card(
    "HS14-B1-03", "Sphingolipid & Glycolipid", "LIPID MÀNG",
    "Phân biệt cấu tạo và vai trò của Sphingomyelin và Glycolipid trên màng tế bào?",
    [
        "Sphingomyelin (SM): Khung sphingosine gắn acid béo qua liên kết amid (ceramide) và este hóa với phosphorylcholin, phân bố chủ yếu ở lá ngoài và bao myelin thần kinh.",
        "Glycolipid (Cerebroside, Ganglioside): Chỉ phân bố độc quyền ở lá ngoài màng bào tương, chuỗi carbohydrat chìa ra ngoài tạo áo glycocalyx.",
        "Vai trò thụ thể nhận diện: Ganglioside GM1 ở lá ngoài màng ruột là thụ thể gắn đặc hiệu của ngoại độc tố tả (Cholera toxin)."
    ],
    "Tất cả glycolipid màng đều quay phần đường ra ngoại bào, không bao giờ quay vào bào tương, tạo tính bất đối xứng tuyệt đối của carbohydrat màng."
))

cards.append(make_card(
    "HS14-B1-04", "Cholesterol màng", "LIPID MÀNG",
    "Giải thích vai trò của Cholesterol như một 'Chất đệm tính lỏng' (Fluidity Buffer) của màng sinh học?",
    [
        "Cấu trúc lưỡng ái độc đáo: Nhóm -OH phân cực nhỏ tại C3 gắn vào đầu este phospholipid, khung steroid 4 vòng phẳng cứng chèn giữa các chuỗi acyl béo.",
        "Ở nhiệt độ sinh lý cao (37°C): Khung steroid cứng hạn chế chuyển động xoay của chuỗi acid béo → giảm tính lỏng quá mức, giảm tính thấm với phân tử tan trong nước.",
        "Ở nhiệt độ thấp: Cholesterol ngăn cản các chuỗi acid béo áp sát kết tinh pha gel rắn → chống đông đặc màng, duy trì tính lỏng sinh học."
    ],
    "Màng bào tương chứa tới 30-50% mol cholesterol, trong khi màng trong ty thể hầu như không có cholesterol (giúp màng trong ty thể mềm dẻo tạo nếp gấp mào cristae)."
))

cards.append(make_card(
    "HS14-B1-05", "Động học Phân tử Lipid", "TÍNH LỎNG MÀNG",
    "Nêu 4 kiểu chuyển động của phân tử lipid màng và giải thích tại sao chuyển động lật mặt (Flip-flop) lại cực kỳ hiếm gặp tự phát?",
    [
        "Khuếch tán ngang (Lateral diffusion): Đổi chỗ trên cùng một lá màng cực nhanh (10^7 lần/giây, đi 2 µm trong 1 giây).",
        "Xoay trục (Rotational motion): Phân tử tự quay quanh trục dọc kỵ nước của chính nó.",
        "Dao động uốn dẻo (Flexion): Các chuỗi hydrocarbon vung vẩy linh hoạt nhất ở phần đuôi kỵ nước sâu trong lòng màng.",
        "Chuyển động lật mặt (Flip-flop): Đổi lá màng cực hiếm tự phát (chu kỳ bán rã tính bằng ngày-tháng) vì đầu ưa nước phân cực phải vượt qua lõi kỵ nước có rào cản năng lượng tự do rất lớn."
    ],
    "Vì rào cản năng lượng của flip-flop tự phát quá lớn, tế bào bắt buộc phải tiến hóa các enzyme vận chuyển đặc hiệu (Flippase, Floppase, Scramblase) để điều hòa sự phân bố lipid giữa hai lá màng."
))

cards.append(make_card(
    "HS14-B1-06", "Yếu tố Điều hòa Tính lỏng", "TÍNH LỎNG MÀNG",
    "Nêu 4 yếu tố hóa lý quyết định tính lỏng linh động của màng tế bào?",
    [
        "Nhiệt độ môi trường: Nhiệt độ tăng làm tăng động năng, phá vỡ liên kết Van der Waals → tăng tính lỏng; nhiệt độ giảm làm màng đóng băng pha gel rắn.",
        "Độ dài chuỗi acid béo: Chuỗi ngắn (14-16 carbon) ít diện tích tiếp xúc Van der Waals → nhiệt độ nóng chảy (Tm) thấp, màng lỏng hơn chuỗi dài (18-24 carbon).",
        "Tỷ lệ liên kết đôi cis: Nối đôi cis tạo góc gập 120° ngăn các chuỗi kỵ nước xếp chặt song song → hạ thấp Tm, làm màng duy trì tính lỏng cao ngay cả ở nhiệt độ mát.",
        "Nồng độ Cholesterol: Đóng vai trò chất đệm tính lỏng ở cả hai thái cực nhiệt độ."
    ],
    "Vi khuẩn và động vật biến nhiệt tự thích nghi với môi trường lạnh bằng cách kích hoạt enzyme desaturase tổng hợp nhiều acid béo chưa bão hòa cis để giữ màng không bị đông cứng."
))

cards.append(make_card(
    "HS14-B1-07", "Tính Bất đối xứng của Màng", "BẤT ĐỐI XỨNG MÀNG",
    "Phân tích sự phân bố bất đối xứng của các phân tử lipid giữa lá ngoài và lá trong màng bào tương?",
    [
        "Lá ngoài (Outer leaflet - tiếp xúc ngoại bào): Giàu Phosphatidylcholin (PC), Sphingomyelin (SM) và toàn bộ Glycolipid màng.",
        "Lá trong (Inner leaflet - tiếp xúc bào tương): Giàu Phosphatidylethanolamin (PE), Phosphatidylserin (PS) và Phosphatidylinositol (PI).",
        "Bề mặt tích điện âm nội bào: Điện tích âm của Phosphatidylserin ở lá trong tạo điện thế bề mặt thuận lợi cho tương tác với các protein truyền tin nội bào."
    ],
    "Sự phá vỡ tính bất đối xứng này (PS lộ ra ngoài) là một sự kiện bệnh lý hoặc tín hiệu sinh học đặc hiệu trong quá trình chết tế bào hoặc đông máu."
))

cards.append(make_card(
    "HS14-B1-08", "Enzym Vận chuyển Lipid", "BẤT ĐỐI XỨNG MÀNG",
    "Phân biệt cơ chế tác dụng và nhu cầu năng lượng của 3 enzyme vận chuyển lipid màng: Flippase, Floppase và Scramblase?",
    [
        "Flippase (P4-type ATPase): Bơm tiêu tốn ATP đặc hiệu, chuyển ngược dòng aminophospholipid (PS và PE) từ lá ngoài vào lá trong.",
        "Floppase (ABC transporter): Bơm tiêu tốn ATP, chuyển phospholipid (PC, sphingomyelin) và cholesterol từ lá trong ra lá ngoài.",
        "Scramblase: Protein không phụ thuộc ATP, kích hoạt bởi nồng độ Ca2+ nội bào tăng cao, cho phép phospholipid trượt tự do hai chiều theo gradient nồng độ phá vỡ tính bất đối xứng."
    ],
    "Flippase giữ cho mặt ngoài màng không có PS. Khi tế bào cạn ATP (hoặc bị enzyme Caspase-3 cắt Flippase trong apoptosis), Scramblase hoạt hóa lật PS ra ngoài."
))

cards.append(make_card(
    "HS14-B1-09", "Dấu ấn Apoptosis", "BỆNH HỌC PHÂN TỬ",
    "Giải thích cơ chế phân tử của hiện tượng lộ diện Phosphatidylserin (PS) làm tín hiệu 'Eat-me' trong Chết theo chương trình (Apoptosis)?",
    [
        "Bất hoạt Flippase & kích hoạt Scramblase: Tín hiệu apoptosis làm tăng Ca2+ nội bào và kích hoạt Caspase-3 phân cắt Flippase, đồng thời hoạt hóa mạnh Scramblase.",
        "Lật Phosphatidylserin ra lá ngoài: PS tích điện âm bị đẩy ra bề mặt ngoài của màng tế bào.",
        "Tín hiệu 'Eat-me' cho đại thực bào: Các đại thực bào mang thụ thể nhận diện PS (TIM-4, MerTK) thực bào nuốt trọn tế bào chết êm thấm, không gây giải phóng chất trung gian gây viêm (khác hoại tử necrosis)."
    ],
    "Hiện tượng lộ diện PS cũng diễn ra trên màng tiểu cầu khi được kích hoạt đông máu, tạo bề mặt tích điện âm neo giữ phức hợp Tenase và Prothrombinase để tạo Thrombin."
))

cards.append(make_card(
    "HS14-B1-10", "Nhuộm Huỳnh quang Annexin V", "CẬN LÂM SÀNG",
    "Nguyên lý và ứng dụng của kỹ thuật nhuộm đôi Annexin V / Propidium Iodide (PI) trong đếm tế bào dòng chảy (Flow Cytometry)?",
    [
        "Annexin V: Protein gắn đặc hiệu có ái lực rất cao với Phosphatidylserin (PS) khi có mặt ion Ca2+.",
        "Propidium Iodide (PI): Thuốc nhuộm nhân không qua được màng tế bào nguyên vẹn, chỉ ngấm vào tế bào đã thủng màng (chết hoại tử).",
        "Phân tầng tế bào: Tế bào sống bình thường (Annexin V- / PI-); Apoptosis giai đoạn sớm (Annexin V+ / PI-); Apoptosis giai đoạn muộn hoặc hoại tử (Annexin V+ / PI+)."
    ],
    "Kỹ thuật Annexin V / PI là tiêu chuẩn vàng đánh giá hiệu quả gây chết tế bào ung thư của các thuốc hóa trị liệu trong nghiên cứu dược lý và sinh học phân tử."
))

# ==============================================================================
# B2: PROTEIN MÀNG TẾ BÀO & ÁO GLYCOCALYX (9 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B2-01", "Phân loại Protein Màng", "PROTEIN MÀNG",
    "Nêu 3 nhóm protein màng tế bào phân loại theo bản chất liên kết với lớp lipid kép?",
    [
        "Protein xuyên màng (Integral / Transmembrane): Chiếm 70%, đâm xuyên qua màng bằng chuỗi xoắn alpha kỵ nước hoặc thùng beta, chỉ tách được bằng chất tẩy rửa (SDS, Triton X-100).",
        "Protein ngoại vi (Peripheral): Liên kết tĩnh điện hoặc liên kết hydro bề mặt với đầu phân cực phospholipid hoặc protein xuyên màng, dễ tách bằng rửa muối hoặc thay đổi pH.",
        "Protein neo lipid (Lipid-anchored): Nằm ở bề mặt màng nhưng liên kết cộng hóa trị với phân tử lipid neo sâu vào màng (GPI anchor, myristoylation, palmitoylation, prenylation)."
    ],
    "Mặc dù lipid chiếm khoảng 50% khối lượng màng, nhưng kích thước phân tử lipid nhỏ hơn protein rất nhiều nên cứ 1 phân tử protein màng sẽ có khoảng 50 phân tử lipid bao bọc xung quanh."
))

cards.append(make_card(
    "HS14-B2-02", "Chuỗi xoắn Alpha Xuyên màng", "PROTEIN MÀNG",
    "Đặc điểm cấu tạo không gian của chuỗi xoắn alpha kỵ nước ở các protein xuyên màng?",
    [
        "Độ dài phân tử: Gồm 20 - 25 acid amin mang chuỗi bên kỵ nước không phân cực (Leu, Ile, Val, Phe, Ala) vừa đủ chiều dày 3 - 4 nm của lõi kỵ nước màng.",
        "Bão hòa liên kết hydro nội chuỗi: Liên kết hydro giữa nhóm C=O và N-H nằm khép kín bên trong lõi xoắn alpha, che chắn khung peptide phân cực khỏi lipid.",
        "Phân loại đơn xuyên vs đa xuyên: Protein đơn xuyên (Glycophorin A, RTK) chỉ có 1 chuỗi xoắn; protein đa xuyên (GPCR có 7 đoạn, kênh ion có 10-12 đoạn) thường tạo vòng tròn ưa nước ở tâm."
    ],
    "Biểu đồ Hydropathy plot (độ kỵ nước) quét trình tự acid amin là công cụ tin sinh học kinh điển để dự đoán số lượng đoạn xoắn alpha xuyên màng của một protein mới phát hiện."
))

cards.append(make_card(
    "HS14-B2-03", "Thùng Beta & Porin", "PROTEIN MÀNG",
    "Cấu trúc và vị trí phân bố của protein xuyên màng dạng Thùng Beta (Beta-Barrel)?",
    [
        "Cấu trúc thùng beta: Cấu tạo từ 8 đến 22 dải beta đối song cuộn tròn thành hình ống trụ rỗng.",
        "Tính chất bề mặt: Mặt ngoài tiếp xúc với lipid chứa acid amin kỵ nước; lòng trong chứa acid amin ưa nước tạo lỗ thủng cho nước và chất tan nhỏ đi qua.",
        "Vị trí phân bố chọn lọc: Không gặp ở màng tương eukaryote; phân bố chủ yếu ở protein Porin của màng ngoài ty thể, lục lạp và màng ngoài vi khuẩn Gram âm."
    ],
    "Màng ngoài ty thể chứa nhiều Porin thùng beta nên thấm tự do với các phân tử nhỏ < 5 kDa, trong khi màng trong ty thể không có Porin nên có tính thấm chọn lọc cực kỳ nghiêm ngặt."
))

cards.append(make_card(
    "HS14-B2-04", "Protein Neo Lipid", "PROTEIN MÀNG",
    "Phân biệt 4 kiểu liên kết cộng hóa trị của Protein neo lipid vào màng tế bào?",
    [
        "Neo GPI (Glycosylphosphatidylinositol): Neo duy nhất ở lá ngoài màng bào tương, gắn vào đầu C-tận của protein qua cầu phosphoethanolamin-oligosaccharid.",
        "Myristoylation: Gắn acid béo myristate (14C) qua liên kết amid vào gốc Glycine ở đầu N-tận ở lá trong.",
        "Palmitoylation: Gắn acid béo palmitate (16C) qua liên kết thioester vào gốc Cysteine nội chuỗi ở lá trong.",
        "Prenylation: Gắn gốc farnesyl (15C) hoặc geranylgeranyl (20C) qua liên kết thioether vào gốc Cysteine thuộc motif CAAX đầu C-tận (điển hình ở protein Ras)."
    ],
    "Thuốc ức chế farnesyltransferase (FTI) từng được phát triển để ngăn protein ung thư Ras neo vào màng tế bào nhằm triệt tiêu tín hiệu sinh ung."
))

cards.append(make_card(
    "HS14-B2-05", "Lớp áo Glycocalyx", "MÀNG SINH CHẤT",
    "Cấu tạo hóa học và 3 chức năng sinh học của lớp áo Glycocalyx bề mặt tế bào?",
    [
        "Cấu tạo hóa học: Lớp 'áo đường' bề mặt ngoài màng tế bào, gồm các chuỗi oligosaccharid gắn cộng hóa trị vào protein (glycoprotein, proteoglycan) và lipid (glycolipid).",
        "Bảo vệ cơ học và bôi trơn: Hút nước tạo lớp gel trơn nhầy bảo vệ tế bào khỏi ma sát vật lý và tấn công của enzyme tiêu protein.",
        "Nhận diện tế bào và kết dính: Cung cấp các phân tử nhận diện cho bạch cầu xuyên mạch (Selectin) và kháng nguyên nhận diện mô.",
        "Quy định tính kháng nguyên nhóm máu: Các chuỗi đường tận cùng quyết định tính kháng nguyên nhóm máu ABO."
    ],
    "Tế bào nội mô mạch máu có lớp glycocalyx rất dày; tổn thương lớp glycocalyx này do tăng đường huyết hoặc sốc nhiễm khuẩn là khởi đầu của biến chứng tắc mạch và thoát dịch phù nề."
))

cards.append(make_card(
    "HS14-B2-06", "Kháng nguyên Nhóm máu ABO", "HÓA SINH MIỄN DỊCH",
    "Cấu trúc hóa học của Khung chất H tiền thân quy định kháng nguyên nhóm máu ABO trên màng hồng cầu?",
    [
        "Khung oligosaccharid cơ bản: Chuỗi lipid-ceramide gắn Glucose - Galactose - N-acetylglucosamine - Galactose.",
        "Enzyme Fucosyltransferase (gen FUT1 mã hóa): Gắn một phân tử L-Fucose vào gốc Galactose tận cùng qua liên kết alpha-1,2-glycosid.",
        "Kháng nguyên H hoàn chỉnh: Khung mang Fucose tận cùng là cơ chất bắt buộc để các enzyme glycosyltransferase nhóm máu gắn thêm đường tiếp theo."
    ],
    "Người nhóm máu O vẫn có kháng nguyên H nguyên vẹn trên màng hồng cầu; nhóm máu O chỉ thiếu enzyme gắn thêm đường A hoặc đường B lên khung H."
))

cards.append(make_card(
    "HS14-B2-07", "Cơ sở Enzym Nhóm máu A, B, O", "HÓA SINH DI TRUYỀN",
    "Bản chất enzym học phân tử phân biệt giữa 3 alen nhóm máu A, B và O?",
    [
        "Alen A (Alpha-1,3-N-acetylgalactosaminyltransferase): Gắn N-acetylgalactosamine (GalNAc) vào Galactose của chất H tạo Kháng nguyên A.",
        "Alen B (Alpha-1,3-galactosyltransferase): Đột biến 4 acid amin làm đổi tính đặc hiệu cơ chất, gắn D-Galactose vào Galactose của chất H tạo Kháng nguyên B.",
        "Alen O: Đột biến mất 1 nucleotide (mất guanine codon 258) gây dịch khung mã đọc tạo protein cụt mất hoàn toàn hoạt tính enzyme → giữ nguyên Kháng nguyên H không đổi."
    ],
    "Sự khác biệt giữa enzym A và enzym B chỉ do 4 acid amin bị thay thế (Leu266Met, Gly268Ala) làm thay đổi kích thước khoang gắn cơ chất đường tận cùng."
))

cards.append(make_card(
    "HS14-B2-08", "Kiểu hình Bombay (Oh)", "BỆNH HỌC PHÂN TỬ",
    "Giải thích cơ chế di truyền phân tử và ý nghĩa truyền máu của Kiểu hình Nhóm máu Bombay (Oh)?",
    [
        "Đột biến gen FUT1 (đồng hợp tử lặn hh): Mất hoàn toàn hoạt tính enzyme alpha-1,2-fucosyltransferase → không thể tổng hợp được Kháng nguyên H tiền thân.",
        "Mất cả kháng nguyên A, B và H: Dù cá thể có mang alen A hay B thì enzyme A/B cũng không có chất H để gắn đường → màng hồng cầu trơ hoàn toàn với A, B, H.",
        "Huyết thanh chứa kháng thể anti-H cực mạnh: Tự nhiên sinh kháng thể kháng H, chống A và chống B → truyền máu nhóm O thông thường sẽ gây tan máu nội mạch cấp tử vong.",
        "Nguyên tắc truyền máu: Người mang kiểu hình Bombay chỉ có thể nhận máu từ một người mang kiểu hình Bombay khác."
    ],
    "Khi định nhóm máu ABO thông thường tại giường, kiểu hình Bombay cho kết quả như nhóm O nhưng khi làm phản ứng chéo chéo với máu nhóm O lại bị ngưng kết dữ dội do kháng thể anti-H."
))

cards.append(make_card(
    "HS14-B2-09", "Lipid Raft (Bè Lipid)", "TỔ CHỨC MÀNG",
    "Cấu tạo và vai trò của Bè Lipid (Lipid Raft) trên màng sinh chất?",
    [
        "Cấu tạo giàu Sphingolipid và Cholesterol: Các chuỗi acyl bão hòa dài của sphingolipid xếp chặt với cholesterol tạo các vi miền (microdomains) dày hơn và ít lỏng hơn màng xung quanh.",
        "Nền tảng tập trung tín hiệu tế bào: Neo giữ chọn lọc các protein truyền tin (thụ thể GPI, protein G, kinase họ Src).",
        "Caveolae: Dạng đặc biệt của bè lipid lõm vào trong màng nhờ protein Caveolin, tham gia ẩm bào và truyền tín hiệu qua màng."
    ],
    "Bè lipid nổi bồng bềnh trên lớp lipid lỏng xung quanh, hoạt động như các bến cảng tập trung các phức hợp thụ thể để kích hoạt phản ứng truyền tin nhanh chóng và chuẩn xác."
))

# ==============================================================================
# B3: KHUNG XƯƠNG MÀNG & BỆNH LÝ HỒNG CẦU DI TRUYỀN (8 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B3-01", "Khung xương Màng Hồng cầu", "KHUNG XƯƠNG MÀNG",
    "Cấu trúc mạng lưới hai chiều nâng đỡ màng hồng cầu gồm các protein chủ chốt nào?",
    [
        "Spectrin: Heterodimer gồm chuỗi alpha và beta xoắn đối song bện vào nhau, hai heterodimer kết hợp đầu-đầu tạo heterotetramer dài 100 nm tạo lưới khung xương.",
        "Ankyrin: Protein cầu nối liên kết Spectrin với miền tế bào chất của protein xuyên màng Band 3 (neo dọc chính).",
        "Protein 4.1 và Actin: Tạo nút nối oligomer F-actin ngắn liên kết đầu kia của tetramer Spectrin với protein xuyên màng Glycophorin C (neo dọc phụ)."
    ],
    "Khung xương màng không nằm trong lớp lipid mà trải thành một mạng lưới đan sợi 2 chiều ở mặt trong bào tương, gắn với màng lipid qua hai điểm neo Ankyrin và Protein 4.1."
))

cards.append(make_card(
    "HS14-B3-02", "Protein Band 3", "PROTEIN MÀNG",
    "Cấu trúc và chức năng kép của Protein Band 3 trên màng hồng cầu?",
    [
        "Kênh trao đổi anion Cl-/HCO3- (AE1): Đổi 1 ion Cl- lấy 1 ion HCO3- qua màng hồng cầu không tiêu tốn ATP, phục vụ vận chuyển CO2 từ mô về phổi (hiện tượng Hamburger).",
        "Điểm neo khung xương màng: Miền N-tận tế bào chất tương tác trực tiếp với Ankyrin, Protein 4.2 và enzyme đường phân (GAPDH).",
        "Độ phong phú: Là protein màng dồi dào nhất của hồng cầu (khoảng 1 triệu phân tử/tế bào, chiếm 25% protein màng)."
    ],
    "Đột biến Band 3 vừa có thể gây bệnh hồng cầu hình cầu di truyền (mất neo khung xương) vừa có thể gây toan hóa ống thận type 1 (dRTA do mất vận chuyển HCO3- ở thận)."
))

cards.append(make_card(
    "HS14-B3-03", "Cơ chế Bệnh Hồng cầu Hình cầu", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế bệnh sinh phân tử của Bệnh hồng cầu hình cầu di truyền (Hereditary Spherocytosis - HS)?",
    [
        "Đột biến protein neo dọc: Khiếm khuyết Ankyrin (50%), Spectrin (SPTB/SPTA1) hoặc Band 3 làm suy yếu liên kết dọc giữa khung xương và lớp lipid kép.",
        "Bong bóng màng lipid: Lớp lipid kép mất nâng đỡ bị tách rời tạo các vi túi lipid bong ra ngoài làm mất diện tích bề mặt màng.",
        "Hồng cầu hình cầu hóa: Tỷ lệ diện tích bề mặt/thể tích (S/V) giảm tối đa, hồng cầu biến thành hình cầu căng tròn mất tính mềm dẻo biến dạng.",
        "Ứ đọng và tiêu hủy tại lách: Hồng cầu hình cầu không thể uốn mình chui qua khe hở 1-2 µm của xoang lách → bị kẹt lại trong môi trường toan, cạn glucose và bị đại thực bào lách tiêu hủy (tan máu ngoài mạch)."
    ],
    "Hồng cầu bình thường có dạng đĩa lõm hai mặt với diện tích bề mặt dư thừa 40% giúp nó uốn cong dễ dàng qua các mao mạch nhỏ hơn đường kính của chính nó."
))

cards.append(make_card(
    "HS14-B3-04", "Đặc điểm Cận lâm sàng HS", "CẬN LÂM SÀNG",
    "Nêu 4 biến đổi cận lâm sàng kinh điển giúp chẩn đoán Bệnh hồng cầu hình cầu di truyền (HS)?",
    [
        "Tăng MCHC (Mean Corpuscular Hemoglobin Concentration): MCHC > 36 g/dL (chỉ số duy nhất tăng nồng độ Hb do tế bào bị mất nước cô đặc).",
        "Hồng cầu hình cầu trên tiêu bản máu ngoại vi: Mất vùng sáng trung tâm, tế bào tròn đậm màu, kích thước nhỏ hơn bình thường (microspherocytes).",
        "Tăng sức bền thẩm thấu hồng cầu nhược trương: Hồng cầu hình cầu dễ vỡ sớm ở nồng độ muối NaCl cao hơn người bình thường (nghiệm pháp sức bền thẩm thấu dịch chuyển sang phải).",
        "Test đo dòng chảy EMA (Eosin-5-maleimide binding test): Giảm tín hiệu huỳnh quang EMA gắn vào Band 3 (độ nhạy và độ đặc hiệu > 95%)."
    ],
    "Tăng MCHC kèm RDW tăng là gợi ý số 1 trên công thức máu tự động hướng tới hồng cầu hình cầu di truyền."
))

cards.append(make_card(
    "HS14-B3-05", "Tam chứng Lâm sàng HS", "LÂM SÀNG",
    "Tam chứng lâm sàng kinh điển và biến chứng thường gặp của Bệnh hồng cầu hình cầu di truyền?",
    [
        "Tam chứng kinh điển: Thiếu máu tan máu + Vàng da từng đợt (tăng Bilirubin gián tiếp) + Lách to (Splenomegaly do ứ đọng hồng cầu tại xoang lách).",
        "Biến chứng sỏi mật sắc tố: Tăng giáng hóa Heme kéo dài tạo nhiều Bilirubin liên hợp lắng đọng thành sỏi mật sắc tố đen (Bilirubinate Calci) ngay từ tuổi trẻ.",
        "Cơn bất sản (Aplastic crisis): Nhiễm Parvovirus B19 ức chế tủy xương tạm thời gây tụt giảm Hemoglobin cấp tính đe dọa tính mạng."
    ],
    "Người bệnh trẻ tuổi xuất hiện sỏi túi mật tái phát kèm lách to luôn cần được tầm soát bệnh lý màng hồng cầu di truyền."
))

cards.append(make_card(
    "HS14-B3-06", "Hồng cầu Hình Elip Di truyền", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế phân tử phân biệt giữa Bệnh hồng cầu hình elip di truyền (HE) và Hồng cầu hình cầu di truyền (HS)?",
    [
        "Vị trí khiếm khuyết liên kết: HS do khiếm khuyết liên kết dọc (khung xương neo màng: Ankyrin, Band 3); HE do khiếm khuyết liên kết ngang (tự kết hợp khung xương).",
        "Cơ chế phân tử HE: Đột biến miền tự kết hợp của chuỗi alpha-spectrin hoặc beta-spectrin ngăn cản dimer kết hợp thành tetramer.",
        "Hậu quả hình thái: Mạng lưới khung xương mất khả năng đàn hồi hồi phục hình dạng sau khi bị kéo giãn khi đi qua mao mạch → hồng cầu bị biến dạng vĩnh viễn thành hình elip/bầu dục."
    ],
    "Đa số bệnh nhân HE không có triệu chứng hoặc tan máu nhẹ hơn nhiều so với HS do hồng cầu hình elip vẫn bảo tồn được tỷ lệ diện tích bề mặt/thể tích tốt hơn."
))

cards.append(make_card(
    "HS14-B3-07", "Chỉ định Cắt lách trong HS", "ĐIỀU TRỊ BSNT",
    "Nguyên lý điều trị và chỉ định Cắt lách (Splenectomy) trong Bệnh hồng cầu hình cầu di truyền?",
    [
        "Nguyên lý điều trị: Cắt lách không chữa khỏi khiếm khuyết màng di truyền (hồng cầu vẫn hình cầu), nhưng loại bỏ cơ quan bắt giữ và tiêu hủy hồng cầu → chấm dứt tan máu, hồi phục đời sống hồng cầu.",
        "Chỉ định: Thể vừa và nặng (thiếu máu phụ thuộc truyền máu, chậm phát triển thể chất, sỏi mật tái diễn, lách to ứ máu).",
        "Thời điểm can thiệp an toàn: Trì hoãn cắt lách đến sau 5-6 tuổi để hoàn thiện hệ miễn dịch, bắt buộc tiêm phòng vaccine phòng vi khuẩn có vỏ (Phế cầu, Não mô cầu, Hib) trước mổ."
    ],
    "Sau cắt lách, máu ngoại vi sẽ xuất hiện nhiều thể Howell-Jolly (mảnh nhân sót trong hồng cầu không còn lách dọn dẹp) và nguy cơ nhiễm trùng huyết bùng phát sau cắt lách (OPSI)."
))

cards.append(make_card(
    "HS14-B3-08", "Hiện tượng Hamburger", "SINH LÝ HÓA SINH",
    "Giải thích Hiện tượng dịch chuyển Clorid (Hiện tượng Hamburger) nhờ protein Band 3 tại mô ngoại vi và tại phổi?",
    [
        "Tại mô ngoại vi (Máu nhận CO2): CO2 từ mô vào hồng cầu, carbonic anhydrase tạo H+ và HCO3-. Band 3 bơm HCO3- ra huyết tương đổi 1 ion Cl- từ huyết tương vào trong hồng cầu.",
        "Tại phổi (Máu nhả CO2): Ngược lại, Band 3 bơm Cl- từ hồng cầu ra huyết tương để đưa HCO3- từ huyết tương trở lại vào hồng cầu tạo CO2 đào thải ra phế nang.",
        "Cân bằng điện tích: Giúp huyết tương vận chuyển an toàn 70% lượng CO2 dưới dạng đệm HCO3- mà không làm thay đổi pH hồng cầu."
    ],
    "Sự dịch chuyển Cl- vào trong hồng cầu ở máu tĩnh mạch làm tăng áp suất thẩm thấu nội bào, kéo nước vào làm hồng cầu tĩnh mạch phồng to nhẹ so với hồng cầu động mạch."
))

# ==============================================================================
# B4: VẬN CHUYỂN THỤ ĐỘNG QUA MÀNG (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B4-01", "Khuếch tán Đơn thuần & Định luật Fick", "VẬN CHUYỂN THỤ ĐỘNG",
    "Nêu bản chất của Khuếch tán đơn thuần (Simple Diffusion) và các biến số trong Định luật Fick?",
    [
        "Bản chất: Chất tan tự do vượt qua lớp lipid kép theo chiều gradient điện hóa (từ nơi nồng độ cao đến thấp), không cần protein mang, không tiêu tốn ATP, không có tính bão hòa.",
        "Định luật Fick (Tốc độ khuếch tán J): J = P × A × (C1 - C2), trong đó P là hệ số thấm, A là diện tích bề mặt màng, (C1 - C2) là chênh lệch nồng độ.",
        "Các chất khuếch tán đơn thuần điển hình: Khí không phân cực (O2, CO2, N2), chất kỵ nước tan trong lipid (hormon steroid, vitamin A, D, E, K), phân tử nhỏ không tích điện (ethanol, glycerol)."
    ],
    "Tốc độ khuếch tán đơn thuần tăng tuyến tính vô hạn theo nồng độ chất tan, hoàn toàn không có điểm bão hòa Vmax như khuếch tán thuận hóa."
))

cards.append(make_card(
    "HS14-B4-02", "Khuếch tán Thuận hóa", "VẬN CHUYỂN THỤ ĐỘNG",
    "So sánh sự khác biệt căn bản giữa Khuếch tán thuận hóa (Facilitated Diffusion) và Khuếch tán đơn thuần?",
    [
        "Đòi hỏi protein vận chuyển chuyên biệt: Cần protein chất mang (Carrier/Transporter) hoặc kênh ion (Channel) tạo lối đi ưa nước xuyên qua màng.",
        "Đặc tính động học bão hòa: Tốc độ vận chuyển tuân theo đường cong hyperbol (động học Michaelis-Menten), đạt tốc độ tối đa Vmax khi các chất mang bị bão hòa cơ chất.",
        "Tính đặc hiệu lập thể cao: Nhận diện chính xác đồng phân quang học (ví dụ GLUT nhận D-glucose, hoàn toàn trơ với L-glucose).",
        "Có thể bị ức chế cạnh tranh: Bị ức chế bởi các phân tử có cấu trúc tương tự cạnh tranh vị trí gắn trên protein mang."
    ],
    "Cả khuếch tán đơn thuần và khuếch tán thuận hóa đều là vận chuyển thụ động: ΔG < 0, tự phát theo chiều giảm của thế năng điện hóa, hoàn toàn không tiêu tốn ATP."
))

cards.append(make_card(
    "HS14-B4-03", "Kênh Ion có Cổng", "KÊNH ION",
    "Nêu 3 cơ chế đóng mở cổng (Gating) của các kênh ion màng tế bào?",
    [
        "Cổng điện thế (Voltage-gated): Đóng mở theo sự biến đổi điện thế màng (kênh Na+, K+, Ca2+ phát sinh điện thế hoạt động sợi thần kinh và cơ tim).",
        "Cổng phối tử (Ligand-gated / Ionotropic receptors): Đóng mở khi có phân tử hóa học gắn đặc hiệu vào thụ thể (thụ thể nicotinic nAChR mở khi gắn Acetylcholine, thụ thể GABA-A mở khi gắn GABA).",
        "Cổng cơ học (Mechanosensitive / Stretch-gated): Đóng mở khi màng tế bào chịu lực căng, kéo giãn cơ học (thụ thể cảm nhận thính giác tế bào lông tai trong, thụ thể nhận cảm áp lực baroreceptor)."
    ],
    "Kênh ion có tốc độ vận chuyển cực kỳ khủng khiếp (10^7 - 10^8 ion/giây), nhanh gấp hàng nghìn lần so với protein chất mang (carrier), đạt gần tốc độ khuếch tán tự do trong nước."
))

cards.append(make_card(
    "HS14-B4-04", "Bộ lọc Chọn lọc Kênh Kali", "KÊNH ION",
    "Giải thích cơ chế phân tử của Bộ lọc chọn lọc (Selectivity Filter) giúp Kênh K+ cho ion K+ đi qua nhưng chặn đứng ion Na+ nhỏ hơn?",
    [
        "Motif bảo tồn TVGYG: Bộ lọc chọn lọc cấu tạo từ chuỗi 5 acid amin Thr-Val-Gly-Tyr-Gly lót trong lòng kênh hẹp.",
        "Khoảng cách oxy carbonyl hoàn hảo: Các nguyên tử oxy carbonyl (C=O) chĩa vào tâm kênh tạo lồng phối trí khoảng cách chính xác 0.27 nm tương đương vỏ áo nước hydrate hóa của ion K+.",
        "Khử áo nước bù trừ năng lượng: Ion K+ dễ dàng lột bỏ các phân tử nước để tạo phối trí thay thế với các oxy carbonyl mà không tiêu tốn năng lượng tự do.",
        "Từ chối ion Na+ nhỏ hơn: Ion Na+ (bán kính 0.095 nm) quá nhỏ, không thể tiếp xúc đồng thời với các oxy carbonyl của kênh → rào cản năng lượng lột áo nước quá lớn khiến Na+ bị đẩy ngược lại."
    ],
    "Công trình giải mã cấu trúc tinh thể kênh K+ của Roderick MacKinnon đã vinh dự đoạt giải Nobel Hóa học năm 2003, làm sáng tỏ một nghịch lý sinh học kinh điển hàng thập kỷ."
))

cards.append(make_card(
    "HS14-B4-05", "Kênh Nước Aquaporin (AQP)", "KÊNH NƯỚC",
    "Cấu trúc phân tử của Aquaporin và cơ chế ngăn chặn rò rỉ gradient proton H+?",
    [
        "Cấu trúc Tetramer: Gồm 4 tiểu phần giống nhau, mỗi tiểu phần chứa một lỗ dẫn nước độc lập ở trung tâm với 6 chuỗi xoắn alpha xuyên màng.",
        "Motif NPA kép: Hai đoạn chứa trình tự Asparagine-Proline-Alanine (Asn-Pro-Ala) gặp nhau ở thắt hẹp trung tâm, buộc phân tử H2O xếp hàng một đi qua.",
        "Định hướng phân tử nước: Hai gốc Asparagine tạo liên kết hydro với nguyên tử oxy của phân tử nước ở giữa, buộc phân tử nước xoay ngược cực.",
        "Chặn đứng dòng proton: Thắt hẹp tích điện dương (Arg195 và histidine) phá vỡ chuỗi liên kết hydro liên tục (bước nhảy proton Grotthuss) → ngăn chặn 100% dòng proton H+ rò rỉ qua màng."
    ],
    "Peter Agre phát hiện Aquaporin năm 1992 và nhận giải Nobel Hóa học 2003; AQP cho phép 3 tỷ phân tử nước đi qua mỗi giây trong khi bảo toàn hoàn hảo gradient pH nội bào."
))

cards.append(make_card(
    "HS14-B4-06", "Aquaporin-1 vs Aquaporin-2", "KÊNH NƯỚC",
    "So sánh phân bố và cơ chế điều hòa giữa Aquaporin-1 (AQP1) và Aquaporin-2 (AQP2)?",
    [
        "Aquaporin-1 (AQP1): Phân bố thường trực ở hồng cầu, màng tế bào nội mô và ống lượn gần thận; hoạt động liên tục không phụ thuộc hormon.",
        "Aquaporin-2 (AQP2): Phân bố ở tế bào chính (principal cells) của ống góp thận; là kênh duy nhất chịu sự điều hòa chuyển vị màng bởi hormon ADH (Vasopressin).",
        "Cơ chế chuyển vị AQP2: ADH gắn thụ thể V2 → kích hoạt Gs/cAMP/PKA → phosphoryl hóa túi nội bào chứa AQP2 → hòa màng đỉnh đưa AQP2 ra màng tái hấp thu nước; hết ADH, AQP2 nhập bào cất giữ."
    ],
    "Đột biến mất chức năng thụ thể V2 (liên kết X) hoặc đột biến gen AQP2 (NST thường) gây bệnh Đái tháo nhạt do thận (NDI) đề kháng với điều trị bằng thuốc ADH ngoại sinh."
))

cards.append(make_card(
    "HS14-B4-07", "Họ Vận chuyển Glucose GLUT", "CHẤT MANG GLUCOSE",
    "Nêu vị trí phân bố và đặc tính ái lực Km của 5 chất vận chuyển Glucose thuộc họ GLUT (SLC2A)?",
    [
        "GLUT1: Hồng cầu, hàng rào máu não; Km rất thấp (~1 mM), thu nhận glucose liên tục ngay cả khi đói.",
        "GLUT2: Tế bào beta tụy, gan, màng đáy ruột và thận; Km rất cao (~15-20 mM), chỉ thu nhận glucose nhiều sau ăn, đóng vai trò cảm biến đường huyết.",
        "GLUT3: Neuron thần kinh não bộ; Km cực thấp (< 1 mM), đảm bảo não luôn được ưu tiên bắt giữ glucose tuyệt đối trong mọi hoàn cảnh.",
        "GLUT4: Cơ vân, cơ tim, mô mỡ; Km trung bình (~5 mM); là GLUT duy nhất phụ thuộc Insulin điều hòa chuyển vị ra màng.",
        "GLUT5: Bờ bàn chải ruột non và tinh trùng; chuyên chở chọn lọc Fructose, không vận chuyển glucose."
    ],
    "Km của GLUT1 và GLUT3 thấp hơn nhiều nồng độ đường huyết lúc đói (4-5 mM), đảm bảo hệ thần kinh trung ương không bao giờ bị thiếu năng lượng trừ khi hạ đường huyết nặng."
))

cards.append(make_card(
    "HS14-B4-08", "Cơ chế Chuyển vị GLUT4", "HÓA SINH NỘI TIẾT",
    "Trình bày con đường truyền tín hiệu phân tử của Insulin kích thích chuyển vị GLUT4 ra màng tế bào cơ và mỡ?",
    [
        "Thụ thể Insulin kích hoạt PI3K: Insulin gắn RTK → tự phosphoryl hóa chéo → gắn cơ chất IRS-1 → hoạt hóa Phosphoinositide 3-kinase (PI3K) tạo PIP3 màng.",
        "Hoạt hóa Akt / PKB: PIP3 tuyển mộ PDK1 và Akt ra màng → Akt được phosphoryl hóa kích hoạt.",
        "Bất hoạt AS160 giải phóng Rab: Akt phosphoryl hóa ức chế protein GAP AS160 → protein G nhỏ Rab chuyển sang dạng gắn GTP hoạt động.",
        "Dung hợp túi GLUT4: Rab-GTP kích hoạt các protein vận chuyển và phức hợp SNARE đưa túi nội bào chứa GLUT4 hòa màng sinh chất tăng thu nhận glucose gấp 10-20 lần."
    ],
    "Tập luyện thể dục thể thao co cơ kích hoạt enzyme AMPK cũng có khả năng kích thích chuyển vị GLUT4 ra màng độc lập hoàn toàn với Insulin (lợi ích vàng cho bệnh nhân ĐTĐ typ 2)."
))

cards.append(make_card(
    "HS14-B4-09", "Thụ thể Nicotinic nAChR", "KÊNH ION PHỐI TỬ",
    "Cấu trúc và cơ chế dẫn truyền ion của Thụ thể Nicotinic Acetylcholine (nAChR) tại bản vận động thần kinh - cơ?",
    [
        "Cấu trúc Pentamer: Gồm 5 tiểu phần xếp vòng tròn quanh kênh trung tâm (2 alpha, 1 beta, 1 gamma/epsilon, 1 delta).",
        "Vị trí gắn ligand: Có 2 vị trí gắn Acetylcholine nằm tại ranh giới giữa tiểu phần alpha và các tiểu phần lân cận.",
        "Cơ chế mở cổng: Khi 2 phân tử ACh gắn đồng thời → xoay trục chuỗi xoắn M2 mở rộng lòng kênh từ 0.3 nm lên 0.8 nm.",
        "Dòng ion khử cực: Cho dòng Na+ ồ ạt tràn vào và K+ đi ra theo gradient điện hóa → phát sinh điện thế bản vận động EPP gây co cơ."
    ],
    "Độc tố rắn cạp nia alpha-Bungarotoxin và curare gắn không thuận nghịch vào tiểu phần alpha của nAChR gây liệt cơ vân hô hấp dẫn đến ngạt thở."
))

cards.append(make_card(
    "HS14-B4-10", "Thụ thể GABA-A", "KÊNH ION PHỐI TỬ",
    "Cơ chế phân tử của Thụ thể GABA-A trong việc ức chế dẫn truyền thần kinh trung ương?",
    [
        "Bản chất kênh Clo chọn lọc: Là kênh ion ligand-gated pentamer chọn lọc cao cho ion Cl-.",
        "Cơ chế mở cổng: Khi chất dẫn truyền thần kinh GABA gắn vào → mở kênh cho ion Cl- từ ngoại bào tràn vào trong tế bào.",
        "Ưu cực hóa màng (Hyperpolarization): Điện thế màng nghỉ tụt sâu từ -70 mV xuống -80 mV → ngăn cản tế bào thần kinh phát sinh điện thế hoạt động (ức chế thần kinh).",
        "Vị trí gắn thuốc điều hòa: Các thuốc an thần giải lo âu (Benzodiazepin, Barbiturat, rượu Ethanol) gắn vào các vị trí dị lập thể khác nhau làm tăng tần số hoặc thời gian mở kênh Cl-."
    ],
    "Flumazenil là chất đối kháng cạnh tranh đặc hiệu tại vị trí gắn Benzodiazepin trên thụ thể GABA-A, dùng cấp cứu giải độc quá liều thuốc ngủ nhóm benzodiazepin."
))

# ==============================================================================
# B5: VẬN CHUYỂN TÍCH CỰC NGUYÊN PHÁT (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B5-01", "Phân loại Bơm ATPase", "VẬN CHUYỂN TÍCH CỰC",
    "Nêu 4 họ Bơm ATP (ATPase) vận chuyển tích cực nguyên phát trong tế bào sinh vật?",
    [
        "P-type ATPase: Tự phosphoryl hóa tạo chất trung gian acyl-phosphate trên gốc Aspartate bảo tồn (bơm Na+-K+, Ca2+-ATPase, H+-K+-ATPase dạ dày).",
        "V-type ATPase (Vacuolar): Bơm proton H+ độc lập không tạo trung gian phospho, phân bố ở màng túi lysosome, endosome để acid hóa khoang nội bào.",
        "F-type ATPase: Bơm proton vận hành theo chiều ngược lại để tổng hợp ATP từ dòng proton (ATP Synthase màng trong ty thể).",
        "ABC Transporter (ATP-Binding Cassette): Sở hữu hai domain gắn nucleotide (NBD), bơm xuất các độc chất, thuốc kháng sinh, lipid (MDR1/P-glycoprotein, CFTR, TAP)."
    ],
    "Chỉ có P-type ATPase mới bị ức chế đặc hiệu bởi chất tương tự phosphat là Vanadate do bắt chước trạng thái chuyển tiếp phosphoryl hóa của gốc Aspartate."
))

cards.append(make_card(
    "HS14-B5-02", "Cấu trúc Bơm Na+-K+-ATPase", "BƠM NGUYÊN PHÁT",
    "Cấu trúc phân tử và chức năng các tiểu phần của Bơm Na+-K+-ATPase?",
    [
        "Tiểu phần alpha (110 kDa): Tiểu phần xúc tác xuyên màng 10 đoạn, chứa vị trí gắn Na+ và ATP ở mặt trong bào tương, vị trí gắn K+ và Digoxin/Ouabain ở mặt ngoài, mang gốc Asp376 được phosphoryl hóa.",
        "Tiểu phần beta (55 kDa): Glycoprotein xuyên màng 1 đoạn, định hướng gấp cuộn chính xác và chuyển vị tiểu phần alpha cắm vào màng sinh chất.",
        "Tiểu phần gamma (FXYD protein, 10 kDa): Điều hòa ái lực của bơm đối với ion Na+ và K+ tùy theo mô cơ quan."
    ],
    "Hoạt động của bơm Na+-K+-ATPase tiêu tốn tới 25-30% tổng năng lượng ATP lúc nghỉ ngơi của toàn bộ cơ thể người (ở não bộ con số này lên tới 70%)."
))

cards.append(make_card(
    "HS14-B5-03", "Chu trình Post-Albers", "BƠM NGUYÊN PHÁT",
    "Trình bày 4 bước trong Chu trình chuyển dạng cấu hình Post-Albers (E1/E2) của Bơm Na+-K+-ATPase?",
    [
        "Dạng E1 mở vào trong gắn 3 Na+: Dạng E1 có ái lực cao với Na+ nội bào, gắn 3 Na+ kích hoạt ATP phosphoryl hóa gốc Asp tạo phức hợp E1-P(3Na+).",
        "Chuyển dạng sang E2-P tống xuất 3 Na+: Năng lượng thủy phân ATP làm bơm biến đổi cấu hình sang E2-P mở ra ngoài, ái lực Na+ giảm mạnh → giải phóng 3 Na+ ra dịch ngoại bào.",
        "Dạng E2-P gắn 2 K+ ngoại bào: E2-P có ái lực cao với K+ ngoại bào, gắn 2 K+ kích thích enzyme tự khử phosphoryl hóa giải phóng Pi vô cơ.",
        "Chuyển dạng về E1 giải phóng 2 K+: Phức hợp khử phosphat chuyển cấu hình về E1 mở vào trong, ái lực K+ giảm mạnh → giải phóng 2 K+ vào bào tương, sẵn sàng chu trình mới."
    ],
    "Cơ chế 'bẫy ion luân phiên' (alternating access) đảm bảo cổng bơm không bao giờ mở thông hai phía cùng một lúc, ngăn chặn rò rỉ ion ngược chiều gradient."
))

cards.append(make_card(
    "HS14-B5-04", "Tính Sinh điện & Tỷ lệ Stoichiometry", "BƠM NGUYÊN PHÁT",
    "Tại sao Bơm Na+-K+-ATPase được gọi là 'Bơm sinh điện' (Electrogenic Pump) và tỷ lệ vận chuyển ion là bao nhiêu?",
    [
        "Tỷ lệ Stoichiometry cố định: Cứ mỗi phân tử ATP bị thủy phân, bơm tống xuất 3 ion Na+ ra dịch kẽ và chỉ thu nhận 2 ion K+ vào tế bào chất.",
        "Bản chất sinh điện (Electrogenic): Mất cân bằng 1 điện tích dương ròng (+1) đi ra ngoài tế bào trong mỗi chu trình.",
        "Đóng góp vào điện thế màng: Tạo dòng điện trực tiếp làm màng âm hơn bên trong khoảng -5 đến -10 mV, hỗ trợ duy trì điện thế nghỉ sinh lý (-70 mV)."
    ],
    "Vai trò quan trọng hơn của bơm không phải là dòng điện trực tiếp, mà là tạo gradient hóa điện thế khổng lồ của K+ (cao trong tế bào) để dòng K+ rò qua kênh rò rỉ K+ tạo nên phần lớn điện thế nghỉ theo phương trình Nernst."
))

cards.append(make_card(
    "HS14-B5-05", "Dược lý Digoxin trên Na+-K+-ATPase", "DƯỢC LÝ PHÂN TỬ",
    "Giải thích cơ chế phân tử tác dụng tăng sức co bóp cơ tim của thuốc Glycosid tim (Digoxin) qua bơm Na+-K+-ATPase?",
    [
        "Ức chế chọn lọc Na+-K+-ATPase: Digoxin gắn đặc hiệu vào mặt ngoài tiểu phần alpha ở trạng thái E2-P khóa cứng bơm.",
        "Tăng nồng độ Na+ nội bào: Bơm ngừng hoạt động làm Na+ tích tụ trong tế bào cơ tim, gradient Na+ ngoại bào suy giảm.",
        "Làm chậm bơm đối vận NCX: Bơm trao đổi Na+/Ca2+ (NCX) bị giảm động lực vận chuyển → ức chế tống xuất Ca2+ ra ngoài tế bào.",
        "Tăng tích lũy Ca2+ túi SERCA: Ca2+ nội bào tăng được bơm vào dự trữ trong lưới nội chất → khi có điện thế hoạt động, giải phóng lượng Ca2+ lớn hơn kích hoạt actomyosin làm tăng sức co bóp cơ tim (inotropic dương)."
    ],
    "Digoxin gắn cạnh tranh với ion K+ ở mặt ngoài bơm. Hạ Kali máu (Hypokalemia) làm tăng gắn Digoxin vào thụ thể dẫn đến nguy cơ ngộ độc Digoxin gây loạn nhịp tim nguy hiểm."
))

cards.append(make_card(
    "HS14-B5-06", "Bơm Canxi SERCA", "BƠM NGUYÊN PHÁT",
    "Cấu trúc và vai trò sinh lý của Bơm Ca2+-ATPase lưới nội chất (SERCA)?",
    [
        "Bơm P-type đặc hiệu: Định vị trên màng mạng nội cơ tương (Sarcoplasmic Reticulum - SR), tiêu tốn 1 ATP bơm 2 ion Ca2+ từ bào tương vào lòng SR đổi 2-3 proton H+ đi ra.",
        "Duy trì nồng độ Ca2+ nghỉ cực thấp: Giữ nồng độ Ca2+ bào tương ở mức sinh lý 100 nM (thấp hơn 10.000 lần so với dịch ngoại bào 1-2 mM).",
        "Vai trò giãn cơ: Sau pha co cơ, SERCA lập tức bơm thu hồi Ca2+ từ sợi cơ vào lòng SR giúp cơ vân và cơ tim giãn nghỉ.",
        "Ức chế bởi Thapsigargin: Thapsigargin là chất ức chế chọn lọc không thuận nghịch SERCA dùng trong nghiên cứu apoptosis do stress lưới nội chất."
    ],
    "Đột biến mất chức năng gen ATP2A1 mã hóa SERCA1 gây bệnh Brody (co cứng cơ vân không đau sau vận động do chậm thu hồi Ca2+)."
))

cards.append(make_card(
    "HS14-B5-07", "Điều hòa SERCA qua Phospholamban", "ĐIỀU HÒA SINH HÓA",
    "Cơ chế điều hòa bơm SERCA bởi Phospholamban (PLN) khi kích thích thần kinh giao cảm beta-adrenergic?",
    [
        "Trạng thái nghỉ (Chưa phosphoryl hóa): Protein Phospholamban gắn ức chế trực tiếp vào bơm SERCA2a ở tế bào cơ tim làm giảm ái lực với Ca2+.",
        "Kích thích giao cảm: Adrenalin/Noradrenalin gắn beta1-receptor → tăng cAMP → hoạt hóa Protein Kinase A (PKA).",
        "Phosphoryl hóa Phospholamban: PKA phosphoryl hóa Ser16 trên PLN làm PLN tách rời khỏi SERCA2a.",
        "Tăng tốc độ giãn cơ tim (Lusitropy dương): Giải phóng ức chế làm SERCA2a bơm Ca2+ vào SR với tốc độ cực nhanh, giúp cơ tim giãn nhanh đón máu về đầy tâm thất chuẩn bị cho nhịp co tiếp theo."
    ],
    "Cơ chế tăng lusitropy qua phosphoryl hóa Phospholamban là chìa khóa thích ứng giúp tim người vừa đập nhanh vừa bơm máu hiệu quả khi vận động gắng sức."
))

cards.append(make_card(
    "HS14-B5-08", "Bơm Canxi Màng Tế bào (PMCA)", "BƠM NGUYÊN PHÁT",
    "So sánh đặc điểm phân tử và chức năng giữa PMCA (Plasma Membrane Ca2+-ATPase) và NCX (Na+/Ca2+ Exchanger)?",
    [
        "Bơm PMCA: Vận chuyển tích cực nguyên phát P-type, ái lực cực cao với Ca2+ (Km ~ 100 nM) nhưng dung lượng vận chuyển thấp (low capacity), chịu điều hòa hoạt hóa bởi phức hợp Ca2+-Calmodulin, duy trì tinh chỉnh nồng độ Ca2+ nền.",
        "Bơm đối vận NCX: Vận chuyển tích cực thứ phát, ái lực thấp với Ca2+ (Km ~ 1-5 µM) nhưng dung lượng vận chuyển cực lớn (high capacity), chuyên tống xuất lượng Ca2+ khổng lồ sau pha khử cực cơ tim.",
        "Phối hợp nhịp nhàng: NCX dọn dẹp Ca2+ cấp tính số lượng lớn; PMCA dọn dẹp Ca2+ tinh chỉnh về mức nền sinh lý chuẩn xác."
    ],
    "Sự phối hợp giữa hệ thống ái lực cao dung lượng thấp (PMCA) và ái lực thấp dung lượng cao (NCX) là nguyên lý thiết kế phổ biến trong sinh học để xử lý tín hiệu nồng độ ion."
))

cards.append(make_card(
    "HS14-B5-09", "Bơm H+-K+-ATPase Dạ dày", "BƠM NGUYÊN PHÁT",
    "Cấu trúc và cơ chế tạo gradient acid dịch vị của Bơm Proton H+-K+-ATPase tế bào thành dạ dày?",
    [
        "Bơm P-type đặc hiệu: Cấu tạo dị nhị tụ gồm tiểu phần xúc tác alpha (10 đoạn xuyên màng) và tiểu phần glycoprotein beta.",
        "Cơ chế vận chuyển: Thủy phân 1 ATP để bơm 1 ion H+ vào lòng dạ dày đổi 1 ion K+ vào bào tương (K+ sau đó rò ra ngoài qua kênh K+ để tái chu chuyển).",
        "Gradient proton khổng lồ: Bơm tạo nồng độ acid dịch vị pH ~ 0.8 - 1.0 ([H+] = 160 mM) từ bào tương tế bào thành pH 7.2 ([H+] = 40 nM) → chênh lệch gradient nồng độ tới 4 triệu lần.",
        "Nguồn tạo H+: Enzyme Carbonic Anhydrase phân giải H2O + CO2 tạo H+ và HCO3-; HCO3- được bơm qua màng đáy vào máu (tạo hiện tượng 'thủy triều kiềm' sau ăn)."
    ],
    "Để tạo gradient nồng độ 4 triệu lần, bơm H+-K+-ATPase dạ dày cần năng lượng tự do nhiệt động học cực lớn, xấp xỉ giới hạn tối đa mà một phân tử ATP có thể cung cấp."
))

cards.append(make_card(
    "HS14-B5-10", "Cơ chế Tác dụng của Thuốc PPI", "DƯỢC LÝ PHÂN TỬ",
    "Giải thích cơ chế dược lý phân tử của Thuốc ức chế bơm proton (PPI: Omeprazole) trong điều trị loét dạ dày tá tràng?",
    [
        "Bản chất tiền chất (Prodrug): PPI là một bazo yếu thân dầu, lưu thông bất hoạt trong tuần hoàn máu ở pH sinh lý 7.4.",
        "Tập trung chọn lọc tại tiểu quản chế tiết: Thuốc khuếch tán vào tiểu quản chế tiết của tế bào thành có nồng độ acid cực mạnh (pH < 2) và bị proton hóa bẫy ion không quay ra được.",
        "Chuyển thành dẫn xuất Sulfenamide hoạt tính: Trong môi trường acid, PPI biến đổi cấu trúc thành cation acid sulfenic hoặc sulfenamide.",
        "Khóa không thuận nghịch bơm proton: Sulfenamide tạo liên kết disulfua cộng hóa trị (S-S) bền vững với gốc Cysteine (Cys813) trên tiểu phần alpha của H+-K+-ATPase làm ức chế bơm vĩnh viễn cho đến khi tế bào thành tổng hợp bơm mới (thời gian tác dụng 24-48 giờ)."
    ],
    "Vì PPI chỉ tích tụ và hoạt hóa khi tiểu quản chế tiết acid mạnh, thuốc đạt hiệu quả ức chế tiết acid tối ưu khi uống trước bữa ăn sáng 30-60 phút (khi các bơm proton được huy động ra màng nhiều nhất)."
))

# ==============================================================================
# B6: VẬN CHUYỂN TÍCH CỰC THỨ PHÁT & VẬN CHUYỂN KHỐI (10 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B6-01", "Vận chuyển Tích cực Thứ phát", "VẬN CHUYỂN THỨ PHÁT",
    "Định nghĩa và phân loại 2 hình thức Vận chuyển tích cực thứ phát (Secondary Active Transport)?",
    [
        "Định nghĩa: Vận chuyển chất tan ngược chiều gradient nồng độ bằng cách sử dụng thế năng điện hóa dự trữ của một ion khác (chủ yếu là Na+) do bơm nguyên phát thiết lập trước đó, không trực tiếp thủy phân ATP.",
        "Đồng vận chuyển (Symport / Cotransport): Chất tan và ion dẫn đường cùng di chuyển qua màng về MỘT hướng (ví dụ: SGLT đồng vận Na+-Glucose, NKCC2 đồng vận Na+-K+-2Cl- ở quai Henle).",
        "Đối vận chuyển (Antiport / Exchanger): Chất tan và ion dẫn đường di chuyển qua màng về HAI hướng ngược nhau (ví dụ: NCX đổi 3 Na+ vào lấy 1 Ca2+ ra, NHE1 đổi 1 Na+ vào lấy 1 H+ ra)."
    ],
    "Nếu bơm Na+-K+-ATPase bị ức chế (bởi Ouabain), gradient Na+ ngoại bào cạn kiệt thì toàn bộ hệ thống vận chuyển tích cực thứ phát sẽ ngừng trệ ngay lập tức."
))

cards.append(make_card(
    "HS14-B6-02", "Đồng vận chuyển SGLT1 vs SGLT2", "VẬN CHUYỂN THỨ PHÁT",
    "So sánh vị trí phân bố, tỷ lệ ion và đặc tính vận chuyển của SGLT1 và SGLT2?",
    [
        "SGLT1: Phân bố ở bờ bàn chải ruột non và đoạn S3 ống lượn gần thận; tỷ lệ 2 Na+ : 1 Glucose; ái lực cao (Km ~ 0.5 mM) dung lượng thấp, hấp thu kiệt cùng glucose.",
        "SGLT2: Phân bố độc quyền ở đoạn S1 ống lượn gần thận; tỷ lệ 1 Na+ : 1 Glucose; ái lực thấp (Km ~ 2-5 mM) dung lượng rất cao, chịu trách nhiệm tái hấp thu 90% glucose lọc qua cầu thận.",
        "Ứng dụng dung dịch Oresol: SGLT1 ở ruột đồng vận Na+ và Glucose kéo theo nước thụ động, là nền tảng cứu sống hàng triệu trẻ em mất nước do tiêu chảy tả."
    ],
    "Ngay cả khi độc tố tả gây bài tiết ồ ạt Cl- và nước qua kênh CFTR, kênh đồng vận SGLT1 ở ruột vẫn hoạt động bình thường, do đó cho uống Oresol (chứa muối + đường) sẽ kéo nước ngược trở lại vào cơ thể."
))

cards.append(make_card(
    "HS14-B6-03", "Thuốc Ức chế SGLT2 (SGLT2i)", "DƯỢC LÝ PHÂN TỬ",
    "Cơ chế tác dụng và 3 lợi ích lâm sàng đột phá của nhóm thuốc Ức chế SGLT2 (Dapagliflozin, Empagliflozin)?",
    [
        "Cơ chế tác dụng: Ức chế cạnh tranh chọn lọc chất đồng vận SGLT2 ở ống lượn gần → ngăn tái hấp thu glucose, bài tiết 70-80 g glucose/ngày ra nước tiểu (thải đường niệu).",
        "Hạ đường huyết độc lập Insulin: Hiệu quả hạ HbA1c không phụ thuộc vào chức năng tế bào beta tụy hay mức độ đề kháng insulin, hoàn toàn không gây hạ đường huyết quá mức (hypoglycemia).",
        "Giảm cân và hạ huyết áp: Thải calorie qua nước tiểu (~300 kcal/ngày) và lợi niệu thẩm thấu natri nhẹ giúp giảm cân nặng và huyết áp tâm thu.",
        "Bảo vệ tim mạch và làm chậm suy thận: Giảm áp lực lọc cầu thận, giảm gánh nặng tiền tải/hậu tải thất trái, được phê duyệt điều trị suy tim (HFrEF/HFpEF) và bệnh thận mạn (CKD) kể cả ở người không mắc đái tháo đường."
    ],
    "Tác dụng phụ cần lưu ý của SGLT2i là nhiễm nấm sinh dục đường niệu (do nước tiểu ngọt) và toan ceton đái tháo đường đường huyết bình thường (Euglycemic DKA)."
))

cards.append(make_card(
    "HS14-B6-04", "Bơm Đối vận NCX & NHE1", "VẬN CHUYỂN THỨ PHÁT",
    "Trình bày vai trò sinh học của Bơm trao đổi Na+/Ca2+ (NCX) và Bơm trao đổi Na+/H+ (NHE1)?",
    [
        "Bơm NCX (Na+/Ca2+ Exchanger): Vận chuyển 3 ion Na+ từ ngoại bào vào trong tế bào theo gradient nồng độ để tống xuất 1 ion Ca2+ ra dịch kẽ; là cơ chế chính hạ Ca2+ nhanh sau pha co cơ tim.",
        "Bơm NHE1 (Na+/H+ Exchanger): Vận chuyển 1 ion Na+ vào trong để tống xuất 1 ion H+ ra ngoài; là hệ thống chủ lực bài xuất acid nội bào bảo vệ tế bào khỏi toan hóa.",
        "Kích hoạt khi toan hóa: Khi pH nội bào giảm, NHE1 tăng hoạt tính cực mạnh để duy trì pH bào tương tối ưu 7.2 cho các enzyme chuyển hóa."
    ],
    "Trong thiếu máu cơ tim tái tưới máu, NHE1 hoạt động quá mức nạp nhiều Na+ vào tế bào làm đảo chiều hoặc liệt NCX, dẫn đến ứ đọng Ca2+ nội bào quá mức gây hoại tử tế bào cơ tim."
))

cards.append(make_card(
    "HS14-B6-05", "Nhập bào qua Áo Clathrin", "VẬN CHUYỂN KHỐI",
    "Các bước trong quá trình Nhập bào qua trung gian thụ thể (Receptor-Mediated Endocytosis) có áo Clathrin?",
    [
        "Gắn phối tử và tập trung vào hố áo: Phối tử gắn thụ thể đặc hiệu màng; phức hợp được protein tiếp hợp AP2 thu gom vào hố áo Clathrin (Clathrin-coated pit).",
        "Tạo túi áo và cắt cuống: Clathrin polymer hóa thành mạng lưới hình lục giác/ngũ giác kéo màng lõm vào trong; enzyme GTPase Dynamin co thắt cắt đứt cổ túi giải phóng túi áo Clathrin vào bào tương.",
        "Cởi áo Clathrin: Protein chaperone Hsp70 cởi bỏ vỏ áo clathrin tái sử dụng, giải phóng túi trần hòa màng với endosome sớm.",
        "Phân ly tại Endosome acid: Bơm H+-ATPase acid hóa endosome (pH 5.0 - 5.5) làm thụ thể biến đổi cấu hình nhả phối tử ra ngoài để tái chu chuyển ra màng tế bào."
    ],
    "Clathrin có cấu trúc hình chân ba (Triskelion) gồm 3 chuỗi nặng và 3 chuỗi nhẹ, tự lắp ráp thành lồng đa diện bao bọc túi màng."
))

cards.append(make_card(
    "HS14-B6-06", "Con đường Chuyển hóa Hạt LDL", "BỆNH HỌC PHÂN TỬ",
    "Mô tả con đường nhập bào và số phận phân tử của hạt Lipoprotein tỷ trọng thấp (LDL) trong tế bào gan?",
    [
        "Nhận diện thụ thể: Apoprotein B-100 trên bề mặt hạt LDL gắn đặc hiệu vào thụ thể LDL Receptor (LDL-R) tại hố áo clathrin của tế bào gan.",
        "Nhập bào và phân ly thụ thể: Hạt LDL được nhập bào qua túi clathrin; tại endosome sớm có pH acid, thụ thể LDL-R nhả hạt LDL ra và tái chu chuyển ra màng sinh chất (1 thụ thể tái sử dụng ~100 lần).",
        "Thủy phân tại Lysosome: Hạt LDL chuyển đến lysosome, enzyme protease phân giải ApoB-100 thành acid amin; Lysosomal Acid Lipase (LAL) thủy phân cholesteryl este giải phóng Cholesterol tự do.",
        "Tín hiệu điều hòa ngược: Cholesterol tự do ức chế enzyme HMG-CoA Reductase (giảm tổng hợp cholesterol nội sinh) và ức chế phiên mã gen LDL-R qua SREBP-2."
    ],
    "Khám phá con đường thụ thể LDL của Michael Brown và Joseph Goldstein đã đoạt giải Nobel Y học năm 1985, đặt nền móng cho sự ra đời của nhóm thuốc hạ mỡ máu Statin."
))

cards.append(make_card(
    "HS14-B6-07", "Tăng Cholesterol Máu Gia đình", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế phân tử và hậu quả lâm sàng của Bệnh Tăng cholesterol máu gia đình (Familial Hypercholesterolemia - FH)?",
    [
        "Đột biến gen LDL-R: Đột biến gen thụ thể LDL (chiếm 85-90%) hoặc đột biến ApoB-100 làm tế bào gan không thể thu nhận hạt LDL từ tuần hoàn.",
        "LDL-C huyết tương tăng vọt: LDL không được bắt giữ tích tụ trong máu (thể dị hợp tử: LDL-C 200-400 mg/dL; thể đồng hợp tử: LDL-C > 500-1000 mg/dL).",
        "Lắng đọng mô và u vàng: Cholesterol lắng đọng ở gân gót Achilles, mi mắt (xanthelasma) và tạo vòng cung giác mạc (arcus corneae).",
        "Xơ vữa động mạch sớm: Xơ vữa động mạch vành tiến triển cực nhanh, gây nhồi máu cơ tim từ tuổi thanh thiếu niên ở thể đồng hợp tử."
    ],
    "FH là một trong những bệnh di truyền trội trên nhiễm sắc thể thường phổ biến nhất ở người (tần suất thể dị hợp tử khoảng 1/250 - 1/300 người)."
))

cards.append(make_card(
    "HS14-B6-08", "Cơ chế của Thuốc Ức chế PCSK9", "DƯỢC LÝ PHÂN TỬ",
    "Vai trò của protein PCSK9 và cơ chế hạ cholesterol kỷ lục của thuốc Kháng thể đơn dòng ức chế PCSK9 (Evolocumab, Alirocumab)?",
    [
        "Sinh lý của PCSK9: Proprotein Convertase Subtilisin/Kexin type 9 (PCSK9) gắn vào thụ thể LDL-R trên màng gan, định hướng thụ thể đi vào lysosome để bị phân hủy tiêu hủy (ngăn thụ thể tái chu chuyển).",
        "Cơ chế kháng thể kháng PCSK9: Thuốc gắn và trung hòa PCSK9 tự do trong máu → giải phóng thụ thể LDL-R khỏi sự phân hủy.",
        "Tăng mật độ thụ thể LDL-R màng gan: Thụ thể LDL-R tự do tái chu chuyển liên tục ra màng tế bào gan bắt giữ hạt LDL với tốc độ tối đa.",
        "Hiệu quả lâm sàng: Hạ nồng độ LDL-Cholesterol huyết tương tới 50-60% kể cả trên bệnh nhân đã dùng statin liều cao dung nạp tối đa."
    ],
    "PCSK9 inhibitor dùng đường tiêm dưới da 2-4 tuần/lần, là vũ khí tối thượng hạ LDL-C cho bệnh nhân nguy cơ tim mạch rất cao hoặc mắc bệnh FH thể dị hợp tử."
))

cards.append(make_card(
    "HS14-B6-09", "Phức hợp Protein SNARE", "XUẤT BÀO",
    "Cấu trúc và cơ chế xúc tác hòa màng xuất bào của Phức hợp protein SNARE?",
    [
        "Cấu tạo phức hợp: Gồm v-SNARE (Synaptobrevin / VAMP trên màng túi tiết) và t-SNARE (Syntaxin-1 và SNAP-25 trên màng đích bào tương).",
        "Tạo bó xoắn 4 sợi bền vững: Các domain xoắn của v-SNARE và t-SNARE bện chặt vào nhau tạo bó 4 chuỗi xoắn alpha song song kéo hai màng lipid áp sát nhau.",
        "Cảm biến Ca2+ Synaptotagmin: Khi có dòng Ca2+ nội bào đi vào gắn Synaptotagmin, kích hoạt phức hợp SNARE hoàn tất dung hợp màng mở lỗ xuất bào giải phóng chất dẫn truyền thần kinh.",
        "Tháo dỡ phức hợp: Sau xuất bào, enzyme ATPase NSF phối hợp protein alpha-SNAP sử dụng năng lượng ATP tháo rời phức hợp SNARE để tái sử dụng."
    ],
    "Lực kéo của bó xoắn SNARE cực kỳ mạnh mẽ, vượt qua lực đẩy tĩnh điện giữa hai đầu phân cực của màng lipid để buộc chúng hòa tan vào nhau."
))

cards.append(make_card(
    "HS14-B6-10", "Độc tố Uốn ván vs Độc tố Botulinum", "ĐỘC CHẤT HỌC",
    "So sánh điểm tác động lên protein SNARE và biểu hiện thần kinh cơ giữa Độc tố Uốn ván (Tetanus toxin) và Độc tố Botulinum (Botox)?",
    [
        "Độc tố Uốn ván (Tetanospasmin): Di chuyển ngược dòng sợi trục về tủy sống, phân cắt Synaptobrevin tại cúc tận cùng của neuron trung gian ức chế (tế bào Renshaw) → ngăn giải phóng Glycine và GABA → mất ức chế neuron vận động gây Liệt Cứng (Spastic paralysis, co cứng cơ, hàm cứng, co giật ưỡn cong người).",
        "Độc tố Botulinum (Botox): Tác động tại chỗ ở bản vận động thần kinh - cơ ngoại vi, phân cắt SNAP-25, Syntaxin hoặc Synaptobrevin tại cúc tận cùng sợi thần kinh vận động → ngăn giải phóng Acetylcholine → gây Liệt Mềm (Flaccid paralysis, sụp mi, giãn cơ, mất trương lực cơ, suy hô hấp).",
        "Điểm chung: Đều là các metalloprotease phụ thuộc kẽm (Zn2+) có độc lực thần kinh kinh khủng nhất trong thế giới sinh học."
    ],
    "Cùng phân cắt các protein của phức hợp SNARE nhưng biểu hiện lâm sàng hoàn toàn trái ngược (Liệt cứng vs Liệt mềm) do vị trí tế bào thần kinh đích tiếp nhận khác nhau."
))

# ==============================================================================
# B7: BỆNH LÝ KÊNH ION & BỆNH HỌC MÀNG (9 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-B7-01", "Bệnh Xơ nang - Đột biến CFTR", "BỆNH HỌC PHÂN TỬ",
    "Bản chất di truyền và đột biến gen phổ biến nhất trong Bệnh Xơ nang (Cystic Fibrosis - CF)?",
    [
        "Bản chất di truyền: Bệnh di truyền lặn trên nhiễm sắc thể thường phổ biến nhất ở người da trắng (tần suất 1/2500 - 1/3000 trẻ sinh sống).",
        "Gen đích: Đột biến gen CFTR (Cystic Fibrosis Transmembrane Conductance Regulator) nằm trên nhánh dài nhiễm sắc thể số 7 (7q31.2).",
        "Đột biến phổ biến nhất: Đột biến ΔF508 (mất 3 cặp base CTT làm mất acid amin Phenylalanine tại vị trí 508), chiếm tới 70% các alen bệnh trên toàn cầu.",
        "Hậu quả phân tử ΔF508: Protein CFTR bị sai lệch gấp cuộn trong lưới nội chất → bị hệ thống kiểm soát chất lượng tế bào nhận diện và phân hủy bởi proteasome (hoàn toàn không lên được màng tế bào)."
    ],
    "Thuốc điều hòa CFTR thế hệ mới (như Trikafta: Elexacaftor/Tezacaftor/Ivacaftor) hoạt động như 'chaperone phân tử' giúp protein ΔF508 gấp cuộn đúng và đưa lên màng, cải thiện ngoạn mục chức năng phổi cho người bệnh."
))

cards.append(make_card(
    "HS14-B7-02", "Bản chất Kênh Kẹp Clo CFTR", "SINH HÓA PHÂN TỬ",
    "Cấu trúc và cơ chế điều hòa đóng mở của Kênh Clo CFTR trên màng tế bào biểu mô?",
    [
        "Thuộc siêu họ ABC Transporter: Khác với các protein ABC khác chuyên bơm chất tan, CFTR là thành viên duy nhất tiến hóa thành một Kênh dẫn ion Cl- và HCO3- thụ động.",
        "Cấu trúc 5 domain: Gồm 2 domain xuyên màng (MSD1, MSD2), 2 domain gắn nucleotide (NBD1, NBD2) và 1 domain điều hòa R (Regulatory domain) duy nhất trong tế bào chất.",
        "Điều hòa kép bởi PKA và ATP: Domain R bắt buộc phải được phosphoryl hóa bởi Protein Kinase A (PKA phụ thuộc cAMP) → mở đường cho 2 phân tử ATP gắn vào NBD1 và NBD2 gây nhị hợp hóa mở cổng kênh dẫn ion Cl-.",
        "Đóng kênh: Thủy phân ATP tại NBD làm tách rời hai domain NBD làm cổng kênh khép lại."
    ],
    "Độc tố tả (Cholera toxin) làm tăng vọt cAMP nội bào → kích hoạt PKA phosphoryl hóa tối đa kênh CFTR làm mở toang kênh bài xuất Cl- và nước ồ ạt vào lòng ruột gây tiêu chảy mất nước."
))

cards.append(make_card(
    "HS14-B7-03", "Cơ chế Bệnh sinh Xơ nang tại Phổi", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế sinh bệnh học phân tử của Bệnh Xơ nang tại biểu mô đường hô hấp?",
    [
        "Mất bài tiết Cl- và HCO3-: Kênh CFTR bất hoạt không thể bơm Cl- và kiềm HCO3- ra ngoài bề mặt biểu mô lòng phế quản.",
        "Mất ức chế kênh ENaC: Bình thường CFTR ức chế kênh Na+ biểu mô (ENaC). Khi mất CFTR, ENaC tăng hoạt quá mức tái hấp thu Na+ và nước ồ ạt từ lòng phế quản vào trong tế bào.",
        "Dịch nhầy mất nước đặc quánh: Lớp dịch bề mặt đường thở (ASL) bị cạn kiệt nước, chất nhầy quánh dính làm tê liệt hệ thống lông chuyển thanh thải.",
        "Nhiễm trùng hô hấp tái diễn: Chất nhầy tắc nghẽn là môi trường kỵ khí hoàn hảo cho vi khuẩn Pseudomonas aeruginosa và Staphylococcus aureus xâm nhập gây giãn phế quản và suy hô hấp mạn tính."
    ],
    "Nguyên nhân tử vong hàng đầu (> 85%) ở bệnh nhân xơ nang là suy hô hấp mạn tính do nhiễm trùng phổi tái diễn nhiều năm."
))

cards.append(make_card(
    "HS14-B7-04", "Nghiệm pháp Đo Clo Mồ hôi", "CẬN LÂM SÀNG",
    "Giải thích tại sao mồ hôi của bệnh nhân Xơ nang lại cực kỳ mặn và ngưỡng nồng độ Clo mồ hôi chẩn đoán?",
    [
        "Sinh lý biểu mô ống tuyến mồ hôi: Bình thường mồ hôi sơ cấp bài tiết đẳng trương; khi đi qua ống bài xuất, kênh CFTR trên màng đỉnh tái hấp thu Cl- kéo theo Na+ để tạo mồ hôi nhược trương không bị mất muối.",
        "Bệnh lý ở bệnh nhân xơ nang: Kênh CFTR bất hoạt không thể tái hấp thu Cl- từ lòng ống dẫn → cả Cl- và Na+ bị thải nguyên vẹn ra bề mặt da tạo vị mồ hôi rất mặn.",
        "Nghiệm pháp điện di Pilocarpine (Sweat Test): Kích thích tiết mồ hôi bằng pilocarpine và định lượng nồng độ ion Clo.",
        "Tiêu chuẩn chẩn đoán: [Cl-] mồ hôi < 30 mmol/L (bình thường); 30 - 59 mmol/L (nghi ngờ); ≥ 60 mmol/L (tiêu chuẩn vàng chẩn đoán xác định bệnh xơ nang)."
    ],
    "Câu nói dân gian châu Âu thời Trung cổ: 'Khốn khổ cho đứa trẻ nào có nụ hôn trên trán mặn chát, nó bị bỏ bùa và sẽ sớm qua đời' chính là mô tả sớm nhất về bệnh xơ nang."
))

cards.append(make_card(
    "HS14-B7-05", "Hội chứng QT Kéo dài (LQTS)", "KÊNH ION HỌC",
    "Định nghĩa và cơ chế phân tử chung dẫn đến Loạn nhịp xoắn đỉnh trong Hội chứng QT kéo dài (LQTS)?",
    [
        "Định nghĩa: Bệnh lý kênh ion tim di truyền (Channelopathy) đặc trưng bởi khoảng QT trên điện tâm đồ kéo dài (QTc > 450 ms ở nam, > 460 ms ở nữ), phản ánh sự chậm trễ trong quá trình tái cực của cơ tâm thất.",
        "Cơ chế phân tử: Hoặc do suy giảm dòng Kali đi ra (loss-of-function kênh K+) hoặc do duy trì dòng Natri đi vào kéo dài (gain-of-function kênh Na+).",
        "Hậu quả điện thế hoạt động: Kéo dài pha 2 (cao nguyên) và pha 3 của điện thế hoạt động sợi cơ thất.",
        "Loạn nhịp Xoắn đỉnh (Torsades de Pointes): Tạo điều kiện cho các khử cực sớm sau (EADs - Early Afterdepolarizations) kích phát cơn nhịp nhanh thất đa hình thái xoắn đỉnh, rung thất và đột tử."
    ],
    "Bệnh nhân LQTS thường có tiền sử ngất tái diễn khi xúc động mạnh, nghe tiếng chuông báo động hoặc gắng sức bơi lội."
))

cards.append(make_card(
    "HS14-B7-06", "Phân loại LQT1, LQT2 và LQT3", "BỆNH HỌC PHÂN TỬ",
    "So sánh gen đột biến, kênh ion và yếu tố khởi phát loạn nhịp giữa 3 thể Hội chứng QT kéo dài bẩm sinh LQT1, LQT2 và LQT3?",
    [
        "LQT1 (Chiếm 45-50%): Đột biến mất chức năng gen KCNQ1 mã hóa kênh K+ dòng chậm IKs; khởi phát loạn nhịp điển hình khi vận động gắng sức mạnh hoặc bơi lội.",
        "LQT2 (Chiếm 35-40%): Đột biến mất chức năng gen KCNH2 (HERG) mã hóa kênh K+ dòng nhanh IKr; khởi phát loạn nhịp điển hình bởi cảm xúc bất ngờ, stress tâm lý hoặc tiếng ồn lớn đột ngột (chuông đồng hồ, tiếng còi xe).",
        "LQT3 (Chiếm 5-10%): Đột biến tăng chức năng (Gain-of-function) gen SCN5A làm kênh Na+ Nav1.5 chậm đóng duy trì dòng Na+ muộn; khởi phát loạn nhịp điển hình khi ngủ hoặc nghỉ ngơi nhịp tim chậm."
    ],
    "Kênh HERG (LQT2) cực kỳ nhạy cảm với việc bị ức chế ngoài ý muốn bởi hàng loạt thuốc điều trị (kháng sinh Macrolide, Fluoroquinolone, thuốc chống loạn thần, thuốc chống nôn) gây hội chứng QT kéo dài mắc phải."
))

cards.append(make_card(
    "HS14-B7-07", "Bệnh Nhược cơ (Myasthenia Gravis)", "BỆNH HỌC TỰ MIỄN",
    "Cơ chế bệnh sinh phân tử của Bệnh Nhược cơ (Myasthenia Gravis - MG) tại bản vận động thần kinh - cơ?",
    [
        "Bản chất tự miễn: Cơ thể sinh tự kháng thể IgG kháng trực tiếp thụ thể Acetylcholine nicotinic (anti-AChR) ở màng sau synap (chiếm 85%) hoặc kháng MuSK (10%).",
        "Khóa và tăng nội bào hóa thụ thể: Kháng thể liên kết chéo làm tăng nhập bào phân hủy thụ thể AChR trên màng cơ.",
        "Kích hoạt bổ thể phá hủy cấu trúc: Phức hợp kháng thể kích hoạt bổ thể màng (MAC) san phẳng các nếp gấp sau synap, làm rộng khe synap.",
        "Giảm biên độ điện thế bản vận động: Nồng độ thụ thể chức năng giảm sút nghiêm trọng làm điện thế EPP không đạt ngưỡng kích hoạt điện thế hoạt động → yếu mỏi cơ tăng dần khi vận động lặp lại (sụp mi, nhìn đôi, yếu cơ nhai, suy cơ hô hấp)."
    ],
    "Đặc trưng lâm sàng của bệnh nhược cơ là yếu cơ mang tính biến động: nhẹ vào buổi sáng sau ngủ dậy, nặng dần về chiều tối hoặc sau khi vận động cơ kéo dài."
))

cards.append(make_card(
    "HS14-B7-08", "Chẩn đoán & Điều trị Nhược cơ", "DƯỢC LÝ LÂM SÀNG",
    "Nguyên lý chẩn đoán bằng Nghiệm pháp Tensilon (Edrophonium) và nguyên lý điều trị bệnh Nhược cơ bằng Pyridostigmine?",
    [
        "Nghiệm pháp Tensilon (Edrophonium): Tiêm tĩnh mạch Edrophonium (chất ức chế enzyme Acetylcholinesterase tác dụng siêu ngắn vài phút) → nồng độ ACh ở khe synap tăng vọt tức thì → sức cơ hồi phục ngoạn mục trong vòng 1-2 phút khẳng định chẩn đoán nhược cơ.",
        "Điều trị bằng Pyridostigmine (Mestinon): Thuốc ức chế thuận nghịch enzyme Acetylcholinesterase kéo dài, làm chậm quá trình thủy phân ACh tự nhiên tại khe synap, bù trừ cho sự thiếu hụt số lượng thụ thể AChR.",
        "Các liệu pháp phối hợp: Thuốc ức chế miễn dịch (Corticoid, Azathioprine), lọc huyết tương (Plasmapheresis dọn sạch kháng thể trong cơn nhược cơ cấp) và phẫu thuật cắt bỏ tuyến ức (Thymectomy)."
    ],
    "Quá liều Pyridostigmine có thể gây Cơn cường phó giao cảm (Cholinergic crisis: co đồng tử, tăng tiết đờm dãi, tiêu chảy, co giật cơ) dễ nhầm với Cơn nhược cơ nặng (Myasthenic crisis)."
))

cards.append(make_card(
    "HS14-B7-09", "Đái tháo nhạt do Thận (NDI)", "BỆNH HỌC PHÂN TỬ",
    "Cơ chế phân tử và chẩn đoán phân biệt Đái tháo nhạt do thận (Nephrogenic DI) vs Đái tháo nhạt trung ương (Central DI)?",
    [
        "Bản chất phân tử NDI: Tế bào ống góp thận mất hoàn toàn khả năng đáp ứng với hormon ADH, chủ yếu do đột biến gen thụ thể V2 (AVPR2 liên kết X, chiếm 90%) hoặc đột biến gen kênh nước AQP2 (NST thường, 10%).",
        "Hậu quả sinh hóa: Không thể chuyển vị Aquaporin-2 ra màng đỉnh ống góp → không tái hấp thu được nước tự do → đái nhiều (10-20 lít/ngày), nước tiểu pha loãng nhược trương (áp suất thẩm thấu niệu < 200 mOsm/kg).",
        "Nghiệm pháp Desmopressin (dDAVP) chẩn đoán phân biệt: Tiêm ADH tổng hợp dDAVP: Nếu áp suất thẩm thấu nước tiểu tăng vọt > 50% → Đái tháo nhạt trung ương (tuyến yên thiếu tiết ADH); Nếu nước tiểu vẫn nhược trương trơ lì không đổi → Đái tháo nhạt do thận (kháng ADH tại thụ thể/kênh nước).",
        "Nguyên nhân mắc phải: Thường gặp nhất do ngộ độc thuốc Lithium (Lithium tích tụ trong tế bào chính ống góp ức chế enzyme Adenylate cyclase làm mất đáp ứng với ADH)."
    ],
    "Khác với ĐTĐ trung ương đáp ứng tuyệt vời với thuốc xịt mũi Desmopressin, bệnh nhân ĐTĐ do thận không đáp ứng với Desmopressin và phải điều trị bằng lợi tiểu Thiazide phối hợp chế độ ăn giảm muối."
))

# ==============================================================================
# B_ALGO: 5 THẺ THUẬT TOÁN QUYẾT ĐỊNH NHANH (5 thẻ)
# ==============================================================================

cards.append(make_card(
    "HS14-ALGO-01", "Phân loại Phương thức Vận chuyển Màng", "VẬN CHUYỂN QUA MÀNG",
    "Lưu đồ thuật toán phân biệt 5 phương thức vận chuyển vật chất qua màng tế bào dựa trên 4 tiêu chí cốt lõi?",
    [
        "Khuếch tán đơn thuần: [Nhu cầu ATP]: Không; [Gradient điện hóa]: Xuôi chiều; [Protein mang]: Không cần; [Đặc tính bão hòa Vmax]: Không (tăng tuyến tính). Ví dụ: O2, CO2, steroid, ethanol.",
        "Khuếch tán thuận hóa: [Nhu cầu ATP]: Không; [Gradient điện hóa]: Xuôi chiều; [Protein mang]: Bắt buộc (kênh ion hoặc carrier); [Đặc tính bão hòa Vmax]: Có bão hòa. Ví dụ: Kênh K+, Aquaporin, GLUT1-5.",
        "Vận chuyển tích cực nguyên phát: [Nhu cầu ATP]: Trực tiếp thủy phân ATP; [Gradient điện hóa]: Ngược chiều; [Protein mang]: Bắt buộc (bơm ATPase); [Đặc tính bão hòa Vmax]: Có bão hòa. Ví dụ: Bơm Na+-K+, SERCA, H+-K+ dạ dày.",
        "Vận chuyển tích cực thứ phát: [Nhu cầu ATP]: Gián tiếp qua gradient ion do bơm nguyên phát tạo ra; [Gradient điện hóa]: Ngược chiều chất tan, xuôi chiều ion dẫn đường; [Protein mang]: Bắt buộc (symporter/antiporter); [Đặc tính bão hòa Vmax]: Có bão hòa. Ví dụ: SGLT1/2, NCX, NHE1.",
        "Vận chuyển khối (Nhập/Xuất bào): [Nhu cầu ATP]: Tiêu tốn năng lượng ATP và GTP; [Gradient điện hóa]: Độc lập gradient; [Protein mang]: Phức hợp màng (Clathrin, SNARE, Dynamin). Ví dụ: Nhập hạt LDL, xuất bào Acetylcholine."
    ],
    "Tiêu chí quyết định phân biệt giữa tích cực nguyên phát và thứ phát là sự tham gia trực tiếp của enzym ATPase thủy phân phân tử ATP tại chính thể mang đó.",
    algo=True
))

cards.append(make_card(
    "HS14-ALGO-02", "Lưu đồ Chu trình Bơm Na+-K+-ATPase & Digoxin", "CHU TRÌNH POST-ALBERS",
    "Lưu đồ thuật toán 4 pha trong chu trình Post-Albers của Bơm Na+-K+-ATPase và điểm tác động của Digoxin?",
    [
        "Pha 1 (E1 nạp Na+): Bơm ở dạng E1 mở vào trong bào tương, gắn 3 Na+ và 1 ATP → thủy phân ATP phosphoryl hóa gốc Asp376 tạo E1-P(3Na+).",
        "Pha 2 (E1-P sang E2-P tống Na+): Bơm chuyển dạng cấu hình sang E2-P mở ra dịch kẽ, ái lực Na+ giảm mạnh → giải phóng 3 Na+ ra ngoại bào.",
        "Pha 3 (E2-P nạp K+ & Điểm khóa Digoxin): E2-P mở ra ngoài gắn 2 K+ ngoại bào kích hoạt enzyme khử phosphoryl hóa giải phóng Pi. [ĐIỂM KHÓA DIGOXIN]: Thuốc gắn vào mặt ngoài trạng thái E2-P làm bất hoạt toàn bộ chu trình bơm.",
        "Pha 4 (E2 về E1 nạp K+ vào tế bào): Bơm khử phosphat chuyển cấu hình về E1 mở vào trong, giải phóng 2 K+ vào bào tương, sẵn sàng nhận phân tử ATP mới.",
        "Hệ quả tế bào cơ tim khi bị Digoxin ức chế: Na+ nội bào tăng → giảm động lực bơm đối vận NCX (3 Na+ vào / 1 Ca2+ ra) → Ca2+ ứ đọng nội bào được SERCA bơm vào SR → tăng co bóp cơ tim."
    ],
    "Nắm vững chu trình 4 pha Post-Albers giúp giải thích tại sao nồng độ Kali máu lại quyết định độc tính của Digoxin: tăng Kali máu thúc đẩy bơm chuyển về dạng E1 làm Digoxin khó gắn kết.",
    algo=True
))

cards.append(make_card(
    "HS14-ALGO-03", "Phân tầng Độc tố Uốn ván vs Độc tố Botulinum", "ĐỘC TỐ SNARE",
    "Thuật toán phân tầng phân biệt Độc tố Uốn ván (Tetanus toxin) vs Độc tố Botulinum (Botox) tác động lên phức hợp protein SNARE?",
    [
        "Tiêu chí 1 - Vị trí tác động giải phẫu: [Độc tố Uốn ván]: Neuron trung gian ức chế (tế bào Renshaw) trong sừng trước tủy sống; [Độc tố Botulinum]: Cúc tận cùng tiếp hợp thần kinh - cơ ngoại vi.",
        "Tiêu chí 2 - Protein SNARE bị cắt: [Độc tố Uốn ván]: Cắt đặc hiệu Synaptobrevin (v-SNARE); [Độc tố Botulinum]: Cắt Synaptobrevin, SNAP-25 hoặc Syntaxin (tùy serotype A đến G).",
        "Tiêu chí 3 - Chất dẫn truyền bị ức chế: [Độc tố Uốn ván]: Ức chế giải phóng Glycine và GABA (chất ức chế thần kinh); [Độc tố Botulinum]: Ức chế giải phóng Acetylcholine (chất kích thích co cơ vân).",
        "Tiêu chí 4 - Hậu quả lâm sàng: [Độc tố Uốn ván]: Mất ức chế vận động → LIỆT CỨNG (Spastic paralysis, co giật cứng, uốn cong người, co thắt thanh quản); [Độc tố Botulinum]: Mất kích thích bản vận động → LIỆT MỀM (Flaccid paralysis, sụp mi, nhìn đôi, mất trương lực cơ, liệt cơ hô hấp).",
        "Quyết định xử trí: Uốn ván cần trung hòa độc tố bằng huyết thanh SAT, tiêm kháng sinh tiêu diệt trực khuẩn và kiểm soát co giật; Ngộ độc Botulinum cần dùng thuốc giải độc kháng độc tố Botulinum phân nhóm (BAT) và hỗ trợ thông khí nhân tạo khẩn cấp."
    ],
    "Quy tắc vàng ghi nhớ nhanh: Tetanus = Tủy sống = Tiêu diệt ức chế = Tăng trương lực cơ co giật cứng; Botulinum = Bản vận động ngoại vi = Bất hoạt acetylcholine = Bại liệt mềm nhẽo.",
    algo=True
))

cards.append(make_card(
    "HS14-ALGO-04", "Lưu đồ Chẩn đoán Bệnh Xơ nang", "LÂM SÀNG & DI TRUYỀN",
    "Lưu đồ thuật toán tiếp cận chẩn đoán Bệnh Xơ nang (Cystic Fibrosis) theo Hướng dẫn Quốc tế?",
    [
        "Bước 1 - Dấu hiệu lâm sàng nghi ngờ: Trẻ nhỏ viêm phổi tái diễn nhiều lần (đặc biệt cấy ra Pseudomonas), suy dinh dưỡng tiêu phân mỡ do suy tụy ngoại tiết, tắc ruột phân su sơ sinh hoặc vô sinh nam do bất sản ống dẫn tinh hai bên (CBAVD).",
        "Bước 2 - Nghiệm pháp đo nồng độ Clo mồ hôi (Sweat Chloride Test bằng Pilocarpine điện di):",
        "   - Nhánh [Cl-] < 30 mmol/L: Bình thường, loại trừ bệnh xơ nang (trừ trường hợp đột biến hiếm thể không điển hình).",
        "   - Nhánh [Cl-] từ 30 đến 59 mmol/L: Vùng nghi ngờ (Intermediate), bắt buộc làm xét nghiệm phân tích đột biến gen CFTR.",
        "   - Nhánh [Cl-] ≥ 60 mmol/L: TIÊU CHUẨN VÀNG CHẨN ĐOÁN XÁC ĐỊNH BỆNH XƠ NANG (cần lặp lại 2 lần độc lập).",
        "Bước 3 - Phân tích đột biến gen CFTR: Định danh chính xác thể đột biến (như ΔF508) để quyết định chỉ định thuốc đích điều hòa kênh CFTR thế hệ mới (CFTR modulators: Ivacaftor, Elexacaftor, Tezacaftor)."
    ],
    "Sweat Chloride Test vẫn là tiêu chuẩn vàng chẩn đoán chức năng số 1; phân tích gen giúp xác định chính xác kiểu đột biến phục vụ tư vấn di truyền tiền sản và điều trị thuốc đích cá thể hóa.",
    algo=True
))

cards.append(make_card(
    "HS14-ALGO-05", "Bảng Đối chiếu Thuốc Ức chế Kênh & Bơm", "DƯỢC LÝ SINH HÓA",
    "Bảng đối chiếu phân tử 6 chất ức chế kinh điển tác động lên hệ thống kênh và bơm màng tế bào?",
    [
        "Digoxin / Ouabain: [Đích tác động]: Bơm Na+-K+-ATPase; [Vị trí]: Mặt ngoài tiểu phần alpha ở trạng thái E2-P; [Ứng dụng/Hậu quả]: Tăng co bóp cơ tim điều trị suy tim HFrEF; nguy cơ ngộ độc khi hạ Kali máu.",
        "Omeprazole / PPI: [Đích tác động]: Bơm H+-K+-ATPase dạ dày; [Vị trí]: Liên kết disulfua không thuận nghịch với Cys813 trên tiểu phần alpha; [Ứng dụng/Hậu quả]: Ức chế bài tiết acid dịch vị dứt điểm điều trị loét dạ dày, trào ngược GERD.",
        "Dapagliflozin / SGLT2i: [Đích tác động]: Kênh đồng vận chuyển Na+-Glucose SGLT2; [Vị trí]: Đoạn S1 ống lượn gần thận; [Ứng dụng/Hậu quả]: Thải đường qua nước tiểu, hạ đường huyết không phụ thuộc insulin, bảo vệ tim thận.",
        "Tetrodotoxin (TTX từ cá nóc): [Đích tác động]: Kênh Na+ cổng điện thế (Nav); [Vị trí]: Vòng cổng ngoài màng ngăn dòng Na+ đi vào; [Ứng dụng/Hậu quả]: Chặn đứng điện thế hoạt động sợi thần kinh, gây tê liệt vận động và ngừng thở trong vài giờ.",
        "Sulfonylurea (Gliclazide): [Đích tác động]: Kênh K+ nhạy cảm ATP (K_ATP) tế bào beta tụy; [Vị trí]: Gắn tiểu phần SUR1 làm đóng kênh K+; [Ứng dụng/Hậu quả]: Khử cực màng mở kênh Ca2+ kích thích tiết Insulin điều trị ĐTĐ typ 2.",
        "Lidocaine: [Đích tác động]: Kênh Na+ cổng điện thế tế bào thần kinh cảm giác; [Vị trí]: Khóa mặt trong lòng kênh ở trạng thái bất hoạt; [Ứng dụng/Hậu quả]: Thuốc gây tê tại chỗ và chống loạn nhịp tim nhóm IB."
    ],
    "Nắm chắc đích tác động phân tử của các chất ức chế màng tế bào là nội dung trọng tâm thường xuyên xuất hiện trong các kỳ thi Bác sĩ Nội trú và USMLE.",
    algo=True
))

# Ghi ra file JSON
manifest_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-14_Hoa_sinh_mang_te_bao")
target_json = manifest_dir / "HS-14_Hoa_sinh_mang_te_bao.cards.v2.json"
target_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Tong so the moi: {len(cards)} the")
print(f"Da ghi thanh cong vao {target_json}")
