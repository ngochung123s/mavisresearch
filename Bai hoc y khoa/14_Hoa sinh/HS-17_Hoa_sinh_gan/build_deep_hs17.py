# -*- coding: utf-8 -*-
"""
Script build_deep_hs17.py:
Sinh 85 the Master chuan BSNT cho HS-17 (Hoa sinh gan, chuc nang chuyen hoa, khu doc, tao mat va xet nghiem sinh hoa gan mat)
100% Unicode, khong LaTeX $, dung dinh dang nhan ' — ' de tranh G_ASKS_MISSING.
"""

import json
from pathlib import Path

DECK_ID = 1401017001
DECK_NAME = "HungMed::Hóa Sinh Y Học::HS-17 Hóa sinh gan, chức năng chuyển hóa, khử độc, tạo mật và xét nghiệm sinh hóa gan mật"
OUTPUT_PATH = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\14_Hoa sinh\HS-17_Hoa_sinh_gan\HS-17_Hoa_sinh_gan.cards.v2.json")
EXTRA_SOURCE = "📖 Nguồn: Giáo trình Hóa sinh Y học (ĐHY Hà Nội, GS. TS. Tạ Thành Văn chủ biên, PGS. TS. Phạm Thiện Ngọc tác giả), NXB Y học, Chương 17: Hóa sinh gan."

def make_card(cid, section, category, front, items, explanation, is_algo=False, tags=None):
    if tags is None:
        tags = ["HS17", "Hoa-sinh", "Hoa-sinh-gan", section]
    
    badge_label = "⚡ THUẬT TOÁN QUYẾT ĐỊNH" if is_algo else "🔬 HÓA SINH Y HỌC · HÓA SINH GAN"
    badge_color = "#e03131" if is_algo else "#1971c2"
    badge_class = "badge-algo" if is_algo else "badge-barem"
    
    front_html = f"""<div style="font-size: 13px; font-weight: bold; color: {badge_color}; text-transform: uppercase; margin-bottom: 8px;">[{badge_label}] {category}</div>
<div style="font-size: 16px; font-weight: 600; color: #212529; line-height: 1.5;">{front}</div>
<div style="margin-top: 10px; font-size: 12px; color: #495057;">
  <span style="background-color: #ffd43b; color: #212529; padding: 2px 6px; border-radius: 4px; font-weight: 600;">Gợi ý</span> Vận dụng kiến thức sinh hóa gan, chu trình urê, chuyển hóa lipid-glucid, chức năng khử độc, tạo mật và xét nghiệm chức năng gan mật.
</div>"""

    ans_lines = []
    for idx, (label, content) in enumerate(items, 1):
        clean_label = label.replace(":", " —").strip().rstrip("—").strip()
        ans_lines.append(f"{idx}) <b>{clean_label} —</b> {content}")
    ans_html = "<br>".join(ans_lines)
    
    back_html = f"""<div style="margin-bottom: 12px;">
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
        "track": "algo" if is_algo else "barem_goc",
        "badge": badge_label,
        "badge_class": badge_class,
        "type": "basic",
        "section": section,
        "category": category,
        "tier": 1,
        "front": front_html,
        "back": back_html,
        "extra": EXTRA_SOURCE,
        "tags": tags
    }

cards = []

# ==========================================
# B1: CẤU TRÚC MÔ HỌC, VI TUẦN HOÀN VÀ TẾ BÀO HỌC GAN (11 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B1-01", "B1", "Đại cương vi tuần hoàn gan",
    "[TUẦN HOÀN KÉP] Hệ Mạch Máu Kép Của Gan<br>Nêu nguồn gốc, lưu lượng máu, tỷ lệ cung cấp oxy và đặc điểm sinh lý của hệ tuần hoàn kép độc nhất vô nhị tại gan.",
    [
        ("Tĩnh mạch cửa (Portal vein)", "Đảm nhận 75 – 80% tổng lưu lượng máu đến gan (khoảng 1000 – 1200 mL/phút); mang toàn bộ dưỡng chất, điện giải, độc chất nội sinh từ ống tiêu hóa và lách; máu nghèo oxy (pO2 ~ 40 – 50 mmHg) nhưng cung cấp khoảng 50% nhu cầu oxy của gan."),
        ("Động mạch gan (Hepatic artery)", "Cung cấp 20 – 25% lưu lượng máu đến gan (khoảng 300 – 400 mL/phút); xuất phát từ động mạch thân tạng; máu giàu oxy (pO2 ~ 95 – 100 mmHg), áp lực cao, cung cấp 50% nhu cầu oxy còn lại."),
        ("Hòa trộn tại xoang mạch (Sinusoids)", "Hai dòng máu hòa lẫn vào nhau trong lòng xoang mạch gan trước khi đổ về tĩnh mạch trung tâm tiểu thùy, giúp tế bào gan vừa nhận dưỡng chất dồi dào vừa đảm bảo đủ oxy chuyển hóa.")
    ],
    "Gan là cơ quan nội tạng lớn nhất (1.2 – 1.6 kg), nhận tới 25% cung lượng tim nhưng tiêu thụ 20 – 25% lượng oxy toàn thân lúc nghỉ ngơi."
))

cards.append(make_card(
    "HS17-B1-02", "B1", "Đơn vị chức năng gan",
    "[ĐƠN VỊ CẤU TRÚC] So Sánh 3 Mô Hình Đơn Vị Chức Năng Gan<br>Phân biệt nguyên lý xây dựng và trục trung tâm giữa Tiểu thùy gan cổ điển, Tiểu thùy cửa và Nang tuyến gan Rappaport.",
    [
        ("Tiểu thùy gan cổ điển (Kiernan)", "Lấy Tĩnh mạch trung tâm tiểu thùy làm trục trung tâm; cấu trúc hình lục lăng với các khoảng cửa nằm ở các góc; nhấn mạnh hướng dòng máu chảy từ ngoại vi vào trung tâm."),
        ("Tiểu thùy cửa (Mall)", "Lấy Khoảng cửa làm trung tâm, giới hạn bởi 3 tĩnh mạch trung tâm kế cận tạo thành hình tam giác; nhấn mạnh chức năng ngoại tiết tạo mật với dòng mật chảy từ trung tâm ra ngoại vi."),
        ("Nang tuyến gan Rappaport (Acini)", "Lấy trục mạch máu phân nhánh tận cùng của khoảng cửa làm trục trung tâm; chia nhu mô gan thành 3 vùng hình thoi dựa trên khoảng cách tới nguồn cấp máu; là mô hình phản ánh sát nhất sinh lý học và cơ chế bệnh sinh.")
    ],
    "Mô hình nang tuyến Rappaport giải thích được vì sao các bệnh lý thiếu máu cục bộ hoặc nhiễm độc chuyển hóa lại tổn thương có tính chọn lọc theo từng vùng."
))

cards.append(make_card(
    "HS17-B1-03", "B1", "Phân vùng chuyển hóa Rappaport",
    "[NANG TUYẾN RAPPAPORT] So Sánh Vùng 1 (Zone 1) và Vùng 3 (Zone 3)<br>So sánh mức độ giàu oxy, các con đường chuyển hóa chiếm ưu thế và tính nhạy cảm bệnh lý giữa Vùng 1 và Vùng 3.",
    [
        ("Vùng 1 — Quanh khoảng cửa (Periportal)", "Nhận máu giàu oxy nhất (pO2 ~ 60 – 65 mmHg) và dưỡng chất; ưu thế chuyển hóa ái khí đòi hỏi năng lượng cao: tân tạo glucose, thoái hóa glycogen, oxy hóa acid béo, chu trình urê và tạo acid mật; đề kháng tốt với thiếu oxy nhưng nhạy cảm với độc chất tác động trực tiếp."),
        ("Vùng 3 — Quanh tĩnh mạch trung tâm (Centrilobular)", "Nhận máu nghèo oxy nhất (pO2 ~ 30 – 35 mmHg); ưu thế chuyển hóa kỵ khí: đường phân, tổng hợp acid béo và triacylglycerol, chuyển hóa khử độc qua hệ CYP450 (CYP2E1); là vùng tổn thương sớm nhất khi tụt huyết áp thiếu oxy và ngộ độc Paracetamol."),
        ("Vùng 2 — Vùng trung gian (Midzonal)", "Vùng chuyển tiếp giữa Vùng 1 và Vùng 3, có đặc tính thích nghi linh hoạt tùy theo tình trạng huyết động và dinh dưỡng.")
    ],
    "Vùng 3 là nơi biểu hiện cao nhất enzym CYP2E1 tạo ra chất độc NAPQI khi quá liều Paracetamol, giải thích vì sao hoại tử gan do Paracetamol luôn bắt đầu từ trung tâm tiểu thùy."
))

cards.append(make_card(
    "HS17-B1-04", "B1", "Tế bào học nhu mô gan",
    "[TẾ BÀO NỘI MÔ XOANG MẠCH] Đặc Điểm Cấu Trúc Siêu Vi Của LSEC<br>Nêu các đặc điểm cấu trúc độc đáo của Tế bào nội mô xoang mạch gan (LSEC) và ý nghĩa sinh lý học trao đổi chất.",
    [
        ("Cửa sổ sàng lọc (Fenestrae)", "Màng tế bào LSEC có hàng nghìn lỗ thủng nhỏ đường kính 100 – 150 nm tập trung thành các tấm sàng (sieve plates), hoạt động như màng lọc cơ học."),
        ("Hoàn toàn không có màng đáy (Absence of basement membrane)", "Xoang mạch gan không có lá đáy liên tục nâng đỡ biểu mô, tạo nên mao mạch kiểu xoang không hoàn chỉnh."),
        ("Ý nghĩa sinh lý trao đổi chất", "Huyết tương mang đại phân tử hòa tan (albumin, lipoprotein, dưỡng chất) tự do tiếp xúc trực tiếp với vi nhung mao màng tế bào gan trong khoang Disse mà không gặp bất kỳ hàng rào ngăn cản nào.")
    ],
    "Hiện tượng xơ hóa mao mạch hóa (Capillarization) trong xơ gan làm xuất hiện màng đáy và bít kín các lỗ sàng, cản trở nghiêm trọng quá trình trao đổi chất của tế bào gan."
))

cards.append(make_card(
    "HS17-B1-05", "B1", "Tế bào học nhu mô gan",
    "[TẾ BÀO HÌNH SAO ITO] Vai Trò Sinh Lý Bình Thường và Bệnh Lý Xơ Hóa Gan<br>Trình bày chức năng của Tế bào hình sao Ito (Hepatic Stellate Cells) ở trạng thái bình thường và cơ chế kích hoạt gây xơ hóa gan.",
    [
        ("Vị trí cư trú", "Nằm trong khoang Disse, xen giữa tế bào nội mô xoang mạch và tế bào nhu mô gan."),
        ("Chức năng sinh lý bình thường", "Trạng thái yên lặng (quiescent): là kho dự trữ chủ yếu Vitamin A của toàn bộ cơ thể (chiếm 80% lượng vitamin A) dưới dạng các giọt mỡ chứa retinyl palmitate."),
        ("Cơ chế bệnh sinh xơ hóa gan", "Khi bị kích hoạt bởi cytokine viêm (đặc biệt là TGF-beta1 và PDGF từ đại thực bào Kupffer), tế bào Ito mất giọt mỡ vitamin A, chuyển dạng thành myofibroblast tăng sinh mạnh và bài tiết ồ ạt Collagen typ I và III gây xơ gan.")
    ],
    "Sự hoạt hóa tế bào hình sao Ito là cơ chế phân tử cốt lõi quyết định mọi quá trình xơ hóa gan mạn tính."
))

cards.append(make_card(
    "HS17-B1-06", "B1", "Tế bào học nhu mô gan",
    "[ĐẠI THỰC BÀO KUPFFER] Vị Trí, Nguồn Gốc và Chức Năng Miễn Dịch<br>Nêu nguồn gốc, vị trí và các vai trò bảo vệ cốt lõi của Tế bào Kupffer trong nhu mô gan.",
    [
        ("Nguồn gốc và vị trí", "Biệt hóa từ bạch cầu đơn nhân (monocyte) tủy xương di chuyển đến gan; cư trú cố định bám trên bề mặt trong của lòng xoang mạch tiếp xúc trực tiếp dòng máu."),
        ("Thực bào và loại bỏ dị vật", "Đảm nhận 80 – 90% khả năng thực bào của toàn bộ hệ lưới nội mô cơ thể; bắt giữ và tiêu hóa xác hồng cầu già, vi khuẩn, nội độc tố vi khuẩn (LPS) và phức hợp miễn dịch từ tĩnh mạch cửa."),
        ("Điều hòa phản ứng viêm", "Khi bị kích thích, tế bào Kupffer giải phóng các cytokine tiền viêm (TNF-alpha, IL-1, IL-6) và các gốc tự do oxy hóa (ROS), khởi động đáp ứng miễn dịch và hoạt hóa tế bào Ito.")
    ],
    "Tế bào Kupffer hoạt động như một trạm kiểm soát an ninh sinh học đầu tiên ngăn không cho vi khuẩn và độc tố từ đường ruột tràn vào tuần hoàn hệ thống."
))

cards.append(make_card(
    "HS17-B1-07", "B1", "Tế bào học nhu mô gan",
    "[TẾ BÀO NHU MÔ GAN] Cấu Trúc Phân Cực Của Hepatocytes<br>Mô tả tỷ lệ thể tích và 3 bề mặt chức năng chuyên biệt hóa của Tế bào nhu mô gan (Hepatocytes).",
    [
        ("Tỷ lệ và hình thái", "Chiếm khoảng 60% tổng số lượng tế bào và 80% thể tích nhu mô gan; cấu trúc hình đa diện với nhiều bào quan phát triển mạnh (ty thể, mạng lưới nội chất, bộ máy Golgi)."),
        ("Mặt xoang mạch (Basolateral / Sinusoidal domain)", "Chiếm 70% diện tích màng tế bào, có nhiều vi nhung mao hướng vào khoang Disse để hấp thu dinh dưỡng và bài tiết protein huyết tương."),
        ("Mặt vi quản mật (Apical / Canalicular domain)", "Chiếm 15% diện tích màng, tiếp giáp tế bào kề bên, được bịt kín bởi các mối nối vòng bịt (tight junctions / zonula occludens) tạo thành vi quản mật để bài xuất acid mật và bilirubin.")
    ],
    "15% diện tích màng còn lại là bề mặt bên (lateral domain) liên kết cơ học với các tế bào gan kế cận."
))

cards.append(make_card(
    "HS17-B1-08", "B1", "Khoang Disse và dòng bạch huyết",
    "[KHOANG DISSE] Ý Nghĩa Giải Phẫu Sinh Lý và Nguồn Gốc Dịch Bạch Huyết<br>Nêu định nghĩa khoang Disse và cơ chế sinh bệnh cổ trướng trong hội chứng tăng áp lực tĩnh mạch cửa.",
    [
        ("Vị trí và ranh giới", "Khoang kẽ hẹp nằm giữa tế bào nội mô xoang mạch (LSEC) và màng đáy của tế bào nhu mô gan; chứa đầy dịch kẽ giàu protein."),
        ("Nguồn gốc dịch bạch huyết gan", "Dịch kẽ trong khoang Disse di chuyển theo khoảng kẽ quanh khoảng cửa đổ vào các mạch bạch huyết; gan tạo ra từ 25 – 50% tổng lượng bạch huyết toàn thân đổ về ống ngực."),
        ("Cơ chế sinh cổ trướng", "Tăng áp lực xoang mạch làm tăng áp lực thủy tĩnh đẩy dịch protein từ khoang Disse rỉ qua bề mặt bao Glisson vào khoang phúc mạc, vượt quá khả năng tái hấp thu dẫn đến cổ trướng.")
    ],
    "Dịch bạch huyết từ gan có nồng độ protein cao gấp nhiều lần so với dịch bạch huyết từ các cơ quan ngoại vi khác."
))

cards.append(make_card(
    "HS17-B1-09", "B1", "Tế bào NK tại gan",
    "[TẾ BÀO PIT CELLS] Bản Chất và Chức Năng Miễn Dịch Tự Nhiên Tại Gan<br>Nêu bản chất tế bào học và vai trò miễn dịch của Tế bào Pit (Pit cells) trong xoang mạch gan.",
    [
        ("Bản chất tế bào học", "Là các tế bào giết tự nhiên (Natural Killer - NK cells) cư trú đặc hiệu tại mô gan; định vị bám vào mặt trong thành tế bào nội mô xoang mạch."),
        ("Nhận diện tế bào bất thường", "Nhận diện các tế bào bị biến đổi kháng nguyên bề mặt mà không cần kháng nguyên hòa hợp tổ chức (MHC) hạn chế."),
        ("Tiêu diệt tế bào đích", "Tiết ra Perforin và Granzyme làm thủng màng và kích hoạt con đường chết theo chương trình (apoptosis) của tế bào nhiễm virus hoặc tế bào ung thư di căn đến gan.")
    ],
    "Mật độ tế bào NK tại gan cao hơn bất kỳ cơ quan nào khác trong cơ thể, thể hiện vai trò miễn dịch bẩm sinh giám sát ung thư của gan."
))

cards.append(make_card(
    "HS17-B1-10", "B1", "Cấu trúc đường mật trong gan",
    "[HỆ THỐNG ĐƯỜNG MẬT] Con Đường Dẫn Mật Từ Vi Quản Mật Đến Ống Gan Chung<br>Mô tả đường đi và các thành phần cấu trúc của hệ thống đường mật trong nhu mô gan.",
    [
        ("Vi quản mật (Bile canaliculi)", "Không có vách biểu mô riêng; được tạo thành từ rãnh lòng màng đỉnh của hai tế bào gan liền kề bịt kín bởi các liên kết vòng bịt."),
        ("Ống Hering (Canals of Hering)", "Đoạn chuyển tiếp nối vi quản mật với ống mật tiểu thùy; được lót một phần bởi tế bào gan và một phần bởi tế bào biểu mô ống mật (cholangiocyte); chứa tế bào gốc gan."),
        ("Ống mật liên tiểu thùy (Interlobular bile ducts)", "Nằm trong khoảng cửa, thành được lót hoàn toàn bởi tế bào biểu mô ống mật hình khối đơn (cholangiocytes); hợp lưu dần tạo thành ống gan phải và ống gan trái.")
    ],
    "Tế bào biểu mô ống mật (cholangiocytes) không chỉ dẫn mật mà còn tích cực bài tiết dịch kiềm giàu HCO3- dưới tác dụng của hormon Secretin."
))

cards.append(make_card(
    "HS17-B1-11", "B1", "Phân bố dị biệt enzyme gan",
    "[DỊ BIỆT KHÔNG GIAN ENZYME] Sự Phân Bố Chọn Lọc Của Các Enzyme Gan<br>Nêu sự phân bố dị biệt (Metabolic Zonation) của các enzyme cốt lõi giữa Vùng 1 quanh khoảng cửa và Vùng 3 quanh tĩnh mạch trung tâm.",
    [
        ("Enzyme ưu thế Vùng 1 (Zone 1)", "Glucokinase, Glucose-6-phosphatase, PEPCK (tân tạo đường); Carbamoyl phosphat synthetase I - CPS-I, Alanin aminotransferase - ALT (chu trình urê); Cholesterol 7alpha-hydroxylase (tạo mật)."),
        ("Enzyme ưu thế Vùng 3 (Zone 3)", "Glutamin synthetase (bẫy amoniac sót lại); CYP450 (đặc biệt CYP2E1, CYP3A4 khử độc và chuyển hóa thuốc); Pyruvat kinase, Acetyl-CoA carboxylase (đường phân và tổng hợp acid béo)."),
        ("Ý nghĩa sinh học", "Tối ưu hóa hiệu suất chuyển hóa bằng cách tách biệt không gian các quá trình cạnh tranh cơ chất và bảo vệ cơ thể khỏi ngộ độc amoniac hoàn toàn.")
    ],
    "Hệ thống bẫy kép amoniac: CPS-I (ái lực thấp, dung lượng cao) ở Vùng 1 xử lý phần lớn NH3, còn Glutamin synthetase (ái lực rất cao) ở Vùng 3 xử lý nốt lượng NH3 rò rỉ."
))

# ==========================================
# B2: CHỨC NĂNG CHUYỂN HÓA GLUCID VÀ LIPID (12 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B2-01", "B2", "Chuyển hóa Glucid tại gan",
    "[HỆ THỐNG ĐỆM ĐƯỜNG HUYẾT] Vai Trò Kênh GLUT2 và Enzyme Glucokinase<br>Phân tích đặc tính động học của kênh vận chuyển GLUT2 và enzyme Glucokinase giúp gan đóng vai trò như một hệ thống đệm đường huyết.",
    [
        ("Kênh GLUT2 màng tế bào gan", "Khuếch tán thuận hóa không phụ thuộc insulin; chỉ số Km rất cao (15 – 20 mmol/L) và Vmax cực lớn; tốc độ nhập glucose vào tế bào gan tỷ lệ thuận trực tiếp với nồng độ glucose máu."),
        ("Enzyme Glucokinase (Hexokinase IV)", "Định vị tại tế bào gan; Km cao (10 mmol/L), không bị ức chế dị lập thể bởi sản phẩm Glucose-6-phosphat (G6P); chỉ hoạt động mạnh khi glucose máu tăng cao sau bữa ăn để bắt giữ glucose tạo glycogen."),
        ("Ý nghĩa đệm đường huyết", "Sau ăn, gan thu giữ lượng lớn glucose dư thừa; khi đói, gan không cạnh tranh sử dụng glucose mà giải phóng glucose dự trữ ra máu duy trì mức sinh lý 3.9 – 6.4 mmol/L.")
    ],
    "Hexokinase I-III ở mô ngoại vi có Km rất thấp (< 0.1 mmol/L) bị ức chế ngược bởi G6P, đảm bảo các mô thiết yếu như não luôn có đủ glucose dù đường huyết thấp."
))

cards.append(make_card(
    "HS17-B2-02", "B2", "Chuyển hóa Glycogen tại gan",
    "[TỔNG HỢP GLYCOGEN] Các Bước Sinh Tổng Hợp Glycogen và Vai Trò Glycogenin<br>Trình bày các bước phản ứng enzyme sinh tổng hợp glycogen tại gan và cơ chế điều hòa bởi hormon.",
    [
        ("Hoạt hóa tạo UDP-Glucose", "Glucose-6-phosphat chuyển thành G1P nhờ Phosphoglucomutase; G1P phản ứng với UTP tạo UDP-glucose nhờ enzyme UDP-glucose pyrophosphorylase giải phóng pyrophosphat (PPi)."),
        ("Vai trò mồi của Glycogenin", "Protein Glycogenin tự xúc tác gắn các phân tử glucose đầu tiên tạo chuỗi mồi oligo-glucose làm cơ chất cho Glycogen synthase."),
        ("Tạo mạch thẳng và phân nhánh", "Glycogen synthase tạo liên kết alpha-1,4-glucosid; Enzym phân nhánh (Amylo-alpha-1,4 chuyển sang 1,6-glucosidase) chuyển đoạn 6-8 gốc glucose tạo liên kết nhánh alpha-1,6; Insulin kích hoạt Glycogen synthase qua phản ứng khử phosphoryl.")
    ],
    "Cấu trúc phân nhánh dày đặc của glycogen tạo ra nhiều đầu tận cùng không khử, giúp enzyme phosphorylase có thể phân cắt giải phóng glucose cực kỳ nhanh chóng khi cần."
))

cards.append(make_card(
    "HS17-B2-03", "B2", "Thoái hóa Glycogen tại gan",
    "[THOÁI HÓA GLYCOGEN] Enzyme Glucose-6-Phosphatase và Khác Biệt Giữa Gan vs Cơ<br>Nêu các enzyme thoái hóa glycogen và giải thích vì sao gan giải phóng được glucose tự do vào máu trong khi cơ vân thì không.",
    [
        ("Phân cắt mạch thẳng", "Glycogen phosphorylase cắt dần các liên kết alpha-1,4 giải phóng Glucose-1-phosphat (G1P) cho đến khi cách điểm nhánh 4 gốc glucose."),
        ("Cắt nhánh", "Enzym cắt nhánh (Debranching enzyme) với 2 hoạt tính: Glucan transferase chuyển 3 gốc glucose sang mạch chính, và alpha-1,6-glucosidase thủy phân gốc glucose ở điểm nhánh giải phóng 1 phân tử Glucose tự do."),
        ("Vai trò độc nhất của G6Pase tại gan", "G1P biến thành G6P; enzym Glucose-6-phosphatase (chỉ có ở màng lưới nội chất tế bào gan và vỏ thận) thủy phân G6P tạo Glucose tự do khuếch tán ra máu; cơ vân hoàn toàn thiếu enzyme này nên G6P buộc phải đi vào đường phân sinh ATP nội bào.")
    ],
    "Đây là nguyên nhân bệnh tích trữ glycogen Typ I (Von Gierke) do thiếu G6Pase gây hạ đường huyết nặng nề khi đói kèm gan to ứ đọng glycogen."
))

cards.append(make_card(
    "HS17-B2-04", "B2", "Tân tạo Glucose tại gan",
    "[TÂN TẠO ĐƯỜNG] 3 Chướng Ngại Nhiệt Động Học và Các Tiền Chất Chính<br>Nêu các tiền chất của tân tạo glucose và 3 phản ứng vượt qua các bước không thuận nghịch của đường phân.",
    [
        ("Các tiền chất tân tạo đường", "Lactat (từ cơ và hồng cầu), Alanin và các acid amin sinh đường (từ cơ), Glycerol (từ thủy phân TAG mô mỡ)."),
        ("Vượt qua Pyruvat kinase (Bước 1)", "Pyruvat được Pyruvat carboxylase ty thể (cần Biotin và ATP) carboxyl hóa thành Oxaloacetat; Oxaloacetat biến đổi thành Malat qua màng ty thể ra bào tương rồi biến thành Phosphoenolpyruvat (PEP) nhờ PEPCK."),
        ("Vượt qua PFK-1 và Hexokinase (Bước 2 & 3)", "Fructose-1,6-bisphosphatase thủy phân F-1,6-BP thành F6P; Glucose-6-phosphatase thủy phân G6P thành Glucose tự do giải phóng vào máu.")
    ],
    "Fructose-2,6-bisphosphat là chất điều hòa dị lập thể mạnh nhất: nồng độ F-2,6-BP cao kích thích PFK-1 (đường phân) và ức chế F-1,6-BPase (tân tạo đường); Glucagon làm giảm F-2,6-BP thúc đẩy tân tạo đường."
))

cards.append(make_card(
    "HS17-B2-05", "B2", "Chu trình Cori và Chu trình Alanin",
    "[CHU TRÌNH CORI VS ALANIN] Cơ Chế Luân Chuyển Cơ Chất Giữa Cơ Vân và Gan<br>So sánh nguyên lý, cơ chất luân chuyển và vai trò bảo vệ cân bằng nội môi giữa Chu trình Cori và Chu trình Glucose-Alanin.",
    [
        ("Chu trình Cori (Lactat cycle)", "Cơ vân hoạt động kỵ khí và hồng cầu thoái hóa glucose tạo Lactat; Lactat vào máu về gan được Lactat dehydrogenase (LDH) chuyển thành Pyruvat để tân tạo Glucose; Glucose mới sinh lại vào máu đến cơ tiêu thụ; ngăn ngừa nhiễm toan lactic."),
        ("Chu trình Glucose - Alanin (Cahill cycle)", "Khi đói hoặc gắng sức, cơ phân giải protein tạo acid amin, nhóm amin được chuyển cho Pyruvat tạo Alanin; Alanin về gan được ALT chuyển amin giải phóng Pyruvat (tân tạo glucose) và Glutamat."),
        ("Khử độc nitơ trong chu trình Alanin", "Glutamat tại gan giải phóng NH4+ đi vào chu trình urê để tạo urê vô hại; do đó chu trình Alanin vừa cung cấp cơ chất tân tạo đường vừa giúp vận chuyển nitơ độc hại từ cơ về gan đào thải an toàn.")
    ],
    "Cơ vân không có chu trình urê hoàn chỉnh nên bắt buộc phải 'mượn' Alanin để chuyên chở nitơ độc về gan xử lý."
))

cards.append(make_card(
    "HS17-B2-06", "B2", "Sinh tổng hợp Lipid tại gan",
    "[SINH TỔNG HỢP ACID BÉO VÀ TAG] Con Thoi Citrat và Enzyme Giới Hạn Tốc Độ<br>Trình bày cơ chế vận chuyển Acetyl-CoA ra bào tương qua con thoi Citrat và vai trò của enzyme Acetyl-CoA Carboxylase (ACC).",
    [
        ("Con thoi Citrat (Citrate shuttle)", "Acetyl-CoA tạo ra trong ty thể không qua được màng ty thể; ngưng tụ với Oxaloacetat tạo Citrat; Citrat qua màng ra bào tương bị ATP-citrat lyase phân cắt giải phóng Acetyl-CoA và Oxaloacetat."),
        ("Enzyme giới hạn tốc độ ACC", "Acetyl-CoA Carboxylase (ACC) xúc tác carboxyl hóa Acetyl-CoA thành Malonyl-CoA (tiêu tốn ATP và cần vitamin Biotin); Malonyl-CoA là tiền chất tổng hợp Palmitat bởi Fatty Acid Synthase (FAS)."),
        ("Điều hòa enzym ACC", "Insulin và Citrat kích thích hoạt hóa ACC dạng polyme hoạt động; Glucagon, Epinephrine và nồng độ AMP cao (qua AMPK) ức chế phosphoryl hóa bất hoạt ACC; Malonyl-CoA ức chế CPT-1 ngăn cản acid béo đi vào ty thể thoái hóa.")
    ],
    "Cơ chế ức chế CPT-1 bởi Malonyl-CoA đảm bảo tế bào gan không bao giờ đồng thời vừa tổng hợp acid béo vừa oxy hóa acid béo."
))

cards.append(make_card(
    "HS17-B2-07", "B2", "Đóng gói và bài xuất VLDL",
    "[BÀI TIẾT VLDL] Vai Trò ApoB-100, Enzyme MTP và Cơ Chế Sinh Bệnh Gan Nhiễm Mỡ<br>Mô tả quá trình đóng gói lipoprotein VLDL tại gan và cơ chế sinh hóa dẫn đến ứ đọng mỡ trong tế bào gan (Hepatic Steatosis).",
    [
        ("Đóng gói hạt VLDL", "Tế bào gan không có chức năng dự trữ mỡ lâu dài; TAG mới tổng hợp được đóng gói cùng Phospholipid, Cholesterol este hóa và Apolipoprotein B-100 (ApoB-100)."),
        ("Vai trò enzyme MTP", "Microsomal Triglyceride Transfer Protein (MTP) trong lòng mạng lưới nội chất xúc tác chuyển TAG vào hạt tiền VLDL chứa ApoB-100 trước khi xuất bào qua Golgi."),
        ("Cơ chế sinh bệnh gan nhiễm mỡ", "Mất cân bằng giữa dòng vào/tổng hợp TAG với đào thải VLDL: 1) Tăng dòng acid béo về gan (béo phì, kháng insulin, đái tháo đường); 2) Giảm tổng hợp ApoB-100 hoặc thiếu choline tạo phospholipid; 3) Rượu ức chế oxy hóa acid béo và tổn thương xuất bào VLDL.")
    ],
    "Đột biến gen MTP gây bệnh không có beta-lipoprotein huyết bẩm sinh (Abetalipoproteinemia), mỡ ứ đọng nặng trong tế bào gan và ruột non."
))

cards.append(make_card(
    "HS17-B2-08", "B2", "Sinh tổng hợp Cholesterol",
    "[SINH TỔNG HỢP CHOLESTEROL] Enzyme HMG-CoA Reductase và Đích Tác Dụng Thuốc Statin<br>Trình bày phản ứng giới hạn tốc độ sinh tổng hợp cholesterol tại gan và cơ chế tác dụng hạ lipid máu của nhóm thuốc Statin.",
    [
        ("Nguồn gốc carbon", "Toàn bộ 27 nguyên tử carbon của cholesterol đều bắt nguồn từ các phân tử Acetyl-CoA bào tương; gan sản xuất 50 – 80% lượng cholesterol nội sinh của cơ thể (0.8 – 1.0 g/ngày)."),
        ("Phản ứng giới hạn tốc độ", "HMG-CoA Reductase (định vị màng lưới nội chất) khử HMG-CoA thành Mevalonat, tiêu tốn 2 phân tử NADPH; đây là bước không thuận nghịch cam kết tạo cholesterol."),
        ("Cơ chế tác dụng thuốc Statin", "Các thuốc Statin (Atorvastatin, Rosuvastatin) có cấu trúc tương tự cơ chất HMG-CoA, ức chế cạnh tranh thuận nghịch enzym HMG-CoA Reductase; làm giảm nồng độ cholesterol nội bào gan, kích thích tế bào gan tăng tổng hợp thụ thể LDL-R trên màng để tăng dọn dẹp LDL khỏi máu.")
    ],
    "Statin không chỉ giảm tổng hợp cholesterol mà quan trọng nhất là làm tăng biểu hiện thụ thể LDL receptor, kéo LDL-C huyết tương giảm mạnh."
))

cards.append(make_card(
    "HS17-B2-09", "B2", "Điều hòa Cholesterol nội bào",
    "[ĐIỀU HÒA CHOLESTEROL] Cơ Chế Phân Tử Của Hệ Thống SREBP-2 và SCAP<br>Mô tả cơ chế phiên mã điều hòa biểu hiện thụ thể LDL và HMG-CoA Reductase qua phức hợp SREBP-2 / SCAP khi nồng độ cholesterol nội bào thay đổi.",
    [
        ("Trạng thái đủ cholesterol", "Cholesterol gắn vào protein SCAP (SREBP Cleavage-Activating Protein) tại màng lưới nội chất, giữ phức hợp SREBP-2/SCAP liên kết với protein neo Insig, ngăn không cho phức hợp di chuyển."),
        ("Trạng thái thiếu hụt cholesterol", "Cholesterol rời khỏi SCAP, phức hợp SREBP-2/SCAP được giải phóng và di chuyển bằng túi vận chuyển sang bộ máy Golgi."),
        ("Kích hoạt phiên mã gen đích", "Tại Golgi, hai protease SP1 và SP2 cắt giải phóng đoạn đầu N của SREBP-2 đi vào nhân tế bào; gắn vào vùng đáp ứng SRE (Sterol Regulatory Element) kích hoạt phiên mã gen HMG-CoA Reductase và gen Thụ thể LDL (LDL-R).")
    ],
    "Hệ thống SREBP-2 hoạt động như một cảm biến phân tử tinh vi giữ cho nồng độ cholesterol tự do trong màng tế bào luôn ở mức hằng định sinh lý."
))

cards.append(make_card(
    "HS17-B2-10", "B2", "Este hóa Cholesterol",
    "[ESTE HÓA CHOLESTEROL] So Sánh Cơ Chế và Vị Trí Của Hai Enzyme LCAT vs ACAT<br>Phân biệt vị trí định vị, nguồn gốc gốc acyl, yếu tố hoạt hóa và ý nghĩa sinh học giữa hai enzyme LCAT và ACAT.",
    [
        ("LCAT (Lecithin-Cholesterol Acyltransferase)", "Định vị trong huyết tương bám trên bề mặt lipoprotein HDL; sử dụng gốc acid béo ở vị trí C2 của Lecithin (Phosphatidylcholin); cần Apolipoprotein A-I (ApoA-1) hoạt hóa; tạo cholesterol este hóa kỵ nước vùi vào lõi HDL phục vụ vận chuyển cholesterol ngược về gan."),
        ("ACAT (Acyl-CoA:Cholesterol Acyltransferase)", "Định vị nội bào tại màng mạng lưới nội chất tế bào gan và các mô; sử dụng gốc acyl từ Fatty Acyl-CoA; không cần ApoA-1; este hóa cholesterol tự do dư thừa để đóng gói vào lõi VLDL hoặc tích trữ thành giọt mỡ nội bào vô hại."),
        ("Ý nghĩa sinh học chống độc", "Cholesterol tự do dư thừa sẽ làm cứng màng tế bào và gây độc; cả hai enzyme đều có chức năng trung hòa nhóm -OH phân cực tạo ester kỵ nước an toàn.")
    ],
    "Thiếu hụt enzyme LCAT bẩm sinh (Norum disease) làm cholesterol tự do lắng đọng ở giác mạc, hồng cầu gây đục giác mạc, thiếu máu tan máu và suy thận."
))

cards.append(make_card(
    "HS17-B2-11", "B2", "Chuyển hóa Thể Ceton",
    "[SINH TỔNG HỢP THỂ CETON] Điều Kiện Kích Hoạt và Enzyme Giới Hạn Tốc Độ<br>Nêu điều kiện sinh lý bệnh thúc đẩy tạo thể ceton tại gan và các enzyme tham gia tổng hợp 3 thể ceton.",
    [
        ("Điều kiện kích hoạt", "Trạng thái nhịn đói kéo dài, đái tháo đường type 1 mất kiểm soát (DKA); khi đó nồng độ Oxaloacetat cạn kiệt do bị kéo sang tân tạo đường, chu trình Krebs ngưng trệ trong khi thoái hóa acid béo tạo lượng Acetyl-CoA khổng lồ."),
        ("Enzyme giới hạn HMG-CoA Synthase ty thể", "2 Acetyl-CoA ngưng tụ thành Acetoacetyl-CoA nhờ Thiolase; enzyme ty thể HMG-CoA Synthase gắn thêm phân tử Acetyl-CoA thứ 3 tạo HMG-CoA; sau đó HMG-CoA Lyase cắt giải phóng Acetoacetat."),
        ("3 thể ceton sinh học", "Acetoacetat (thể ceton đầu tiên); beta-hydroxybutyrat (tạo thành do khử Acetoacetat bởi beta-hydroxybutyrat dehydrogenase phụ thuộc NADH); và Aceton (sản phẩm phụ do Acetoacetat tự khử carboxyl chậm, thải qua hơi thở).")
    ],
    "HMG-CoA Synthase có 2 isoenzyme riêng biệt: dạng bào tương tham gia tổng hợp Cholesterol, còn dạng ty thể tham gia tạo Thể Ceton."
))

cards.append(make_card(
    "HS17-B2-12", "B2", "Chuyển hóa Thể Ceton",
    "[NGHỊCH LÝ THỂ CETON] Vì Sao Gan Sản Xuất Ceton Nhưng Không Thể Sử Dụng Ceton?<br>Giải thích cơ chế phân tử vì sao tế bào gan không thể thoái hóa thể ceton để sinh năng lượng cho chính mình.",
    [
        ("Quá trình hoạt hóa thể ceton ngoại vi", "Tại các mô tiêu thụ (não, cơ vân, cơ tim), Acetoacetat muốn thoái hóa phải được hoạt hóa gắn phân tử Coenzyme A tạo Acetoacetyl-CoA."),
        ("Enzyme Thiophorase (SCOT)", "Phản ứng hoạt hóa đòi hỏi enzyme Thiophorase (Succinyl-CoA:3-ketoacid CoA transferase / SCOT) chuyển gốc CoA từ Succinyl-CoA sang Acetoacetat (hoặc enzym Acetoacetat kinase)."),
        ("Sự thiếu hụt hoàn toàn tại tế bào gan", "Tế bào gan hoàn toàn KHÔNG CÓ enzyme Thiophorase; do đó gan sản xuất thể ceton nhưng không thể hoạt hóa tiêu thụ mà bắt buộc phải giải phóng toàn bộ vào máu cung cấp năng lượng cho các mô ngoại vi.")
    ],
    "Đây là sự phân công lao động sinh học tuyệt vời: gan chịu hy sinh đóng vai trò nhà máy sản xuất nhiên liệu cấp cứu cho não bộ mà không tư lợi."
))

# ==========================================
# B3: CHỨC NĂNG CHUYỂN HÓA PROTEIN VÀ CHU TRÌNH URÊ (11 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B3-01", "B3", "Sinh tổng hợp Protein huyết tương",
    "[ALBUMIN HUYẾT THANH] Năng Lực Sản Xuất, Áp Suất Keo và Động Học Bán Hủy<br>Nêu sản lượng tổng hợp albumin mỗi ngày tại gan, vai trò duy trì áp suất keo và ý nghĩa thời gian bán hủy đối với lâm sàng.",
    [
        ("Sản lượng tổng hợp", "Gan là cơ quan duy nhất tổng hợp Albumin; sản xuất từ 12 – 15 g albumin mỗi ngày (chiếm 50% tổng lượng protein gan bài tiết)."),
        ("Duy trì áp suất keo", "Albumin chiếm 55 – 65% protein huyết tương nhưng tạo nên 75 – 80% tổng áp suất keo huyết tương (25 – 30 mmHg); đóng vai trò sinh tử giữ nước trong lòng mạch ngăn phù nề."),
        ("Động học thời gian bán hủy dài", "Thời gian bán hủy của albumin khoảng 20 ngày; do đó nồng độ albumin máu KHÔNG THAY ĐỔI trong suy gan cấp mà chỉ giảm rõ rệt trong bệnh gan mạn tính (xơ gan).")
    ],
    "Albumin còn là chất chuyên chở không chuyên biệt cho acid béo tự do, bilirubin gián tiếp, ion calci, hormon steroid và nhiều loại thuốc điều trị."
))

cards.append(make_card(
    "HS17-B3-02", "B3", "Sinh tổng hợp Yếu tố đông máu",
    "[CÁC YẾU TỐ ĐÔNG MÁU] Vai Trò Của Gan và Phản Ứng Carboxyl Hóa Phụ Thuộc Vitamin K<br>Liệt kê các yếu tố đông máu do gan tổng hợp và cơ chế tác dụng của Vitamin K trong việc kích hoạt các yếu tố này.",
    [
        ("Các yếu tố do gan tổng hợp", "Yếu tố I (Fibrinogen), II (Prothrombin), V, VII, IX, X và các chất chống đông tự nhiên: Protein C, Protein S, Antithrombin III."),
        ("Nhóm phụ thuộc Vitamin K (1972)", "Yếu tố II, VII, IX, X và Protein C, Protein S đòi hỏi Vitamin K dạng khử (Hydroquinone) làm cofactor cho enzyme gamma-glutamyl carboxylase."),
        ("Tạo domain Gla gắn Calci", "Phản ứng carboxyl hóa bổ sung gốc carboxyl (-COOH) vào các gốc acid glutamic (Glu) tạo thành gamma-carboxyglutamat (Gla); các gốc Gla tích điện âm tạo phức chelat với ion Ca2+ giúp gắn yếu tố đông máu lên bề mặt màng phospholipid tiểu cầu.")
    ],
    "Thuốc chống đông kháng vitamin K (Warfarin, Sintrom) ức chế enzyme Vitamin K Epoxide Reductase (VKOR), làm cạn kiệt vitamin K dạng khử nên các yếu tố 1972 không có hoạt tính sinh học."
))

cards.append(make_card(
    "HS17-B3-03", "B3", "Độc tính thần kinh của Amoniac",
    "[ĐỘC TÍNH AMONIAC] Nguồn Gốc và Cơ Chế Gây Phù Nề Não Trong Hôn Mê Gan<br>Trình bày nguồn gốc sinh ra amoniac trong cơ thể và 3 cơ chế sinh hóa giải thích độc tính của NH3 đối với hệ thần kinh trung ương.",
    [
        ("Nguồn gốc amoniac", "Thoái hóa acid amin tại các mô (khử amin oxy hóa), thoái biến adenylat ở cơ, và đặc biệt do vi khuẩn đường ruột phân giải urê và protein thức ăn tại đại tràng (chiếm lượng lớn nhất)."),
        ("Làm cạn kiệt alpha-ketoglutarat và ATP", "NH3 vượt qua hàng rào máu não kích hoạt Glutamat dehydrogenase chuyển alpha-ketoglutarat thành Glutamat; làm cạn kiệt cơ chất của chu trình Krebs, ức chế hô hấp tế bào não và làm sụt giảm tổng hợp ATP."),
        ("Tích tụ Glutamin gây phù nề tế bào sao", "Glutamat kết hợp với NH3 thứ hai tạo Glutamin nhờ Glutamin synthetase; phân tử Glutamin tích tụ có tính thẩm thấu rất cao hút nước làm trương phồng tế bào sao (astrocyte swelling) dẫn đến phù não và tăng áp lực nội sọ.")
    ],
    "Nồng độ NH3 máu bình thường rất thấp (11 – 35 µmol/L); khi tế bào gan suy hoại tử hoặc có dòng máu thông nối cửa-chủ, NH3 tăng vọt gây Bệnh não gan (Hepatic Encephalopathy)."
))

cards.append(make_card(
    "HS17-B3-04", "B3", "Tổng quan Chu trình Urê",
    "[CHU TRÌNH URÊ] Ý Nghĩa Sinh Học, Nguồn Gốc 2 Nguyên Tử Nitơ và Năng Lượng Tiêu Tốn<br>Nêu ý nghĩa sinh học của Chu trình Urê (Krebs-Henseleit), nguồn gốc của 2 nguyên tử Nitơ trong phân tử urê và chi phí năng lượng ATP.",
    [
        ("Ý nghĩa sinh học", "Là con đường DUY NHẤT và TOÀN VẸN của cơ thể để chuyển đổi amoniac cực độc thành Urê hòa tan, trung tính, không độc và dễ dàng bài tiết qua thận."),
        ("Nguồn gốc các nguyên tử trong Urê", "Phân tử Urê (NH2-CO-NH2): 1 nguyên tử Nitơ lấy từ Amoniac tự do (NH4+); 1 nguyên tử Nitơ lấy từ acid amin Aspartat; nguyên tử Carbon lấy từ Bicarbonat (HCO3-)."),
        ("Chi phí năng lượng", "Tiêu tốn 3 phân tử ATP nhưng tương đương 4 liên kết phosphat giàu năng lượng (2 ATP tại CPS-I tạo 2 ADP, và 1 ATP tại ASS bị thủy phân thành AMP + PPi, sau đó PPi tiếp tục thủy phân giải phóng năng lượng).")
    ],
    "Chu trình urê diễn ra phối hợp giữa hai khoang dưới tế bào: 2 phản ứng đầu tiên trong ty thể và 3 phản ứng tiếp theo ngoài bào tương tế bào gan Vùng 1."
))

cards.append(make_card(
    "HS17-B3-05", "B3", "Chu trình Urê - Phản ứng 1",
    "[CHU TRÌNH URÊ - BƯỚC 1] Enzyme CPS-I và Vai Trò Hoạt Hóa Bắt Buộc Của NAG<br>Mô tả phản ứng tạo Carbamoyl phosphat trong ty thể và vai trò sinh hóa của phân tử N-acetylglutamat (NAG).",
    [
        ("Phản ứng tạo Carbamoyl phosphat", "Diễn ra trong cơ chất ty thể; enzyme Carbamoyl phosphat synthetase I (CPS-I) ngưng tụ ion NH4+ với HCO3-, tiêu tốn 2 phân tử ATP tạo thành Carbamoyl phosphat."),
        ("Enzyme giới hạn tốc độ", "CPS-I là enzyme giới hạn tốc độ (rate-limiting step) cam kết dòng chuyển hóa của toàn bộ chu trình urê."),
        ("Vai trò hoạt hóa bắt buộc của NAG", "N-acetylglutamat (NAG) là chất hoạt hóa dị lập thể dương tính bắt buộc; không có NAG, CPS-I hoàn toàn không có hoạt tính sinh học; NAG được tổng hợp từ Glutamat và Acetyl-CoA bởi enzyme NAGS (kích hoạt bởi Arginin).")
    ],
    "Thiếu hụt enzyme CPS-I hoặc thiếu enzyme tổng hợp NAG (NAGS) đều dẫn đến bệnh tăng amoniac máu bẩm sinh sơ sinh tối cấp cực kỳ nguy kịch."
))

cards.append(make_card(
    "HS17-B3-06", "B3", "Chu trình Urê - Phản ứng 2",
    "[CHU TRÌNH URÊ - BƯỚC 2] Enzyme OTC và Bệnh Rối Loạn Di Truyền Liên Kết X<br>Trình bày phản ứng tạo Citrullin và đặc điểm di truyền, xét nghiệm đặc trưng của bệnh thiếu hụt Ornithin Transcarbamoylase (OTC).",
    [
        ("Phản ứng tạo Citrullin", "Enzym Ornithin transcarbamoylase (OTC) trong ty thể chuyển nhóm carbamoyl từ Carbamoyl phosphat lên acid amin Ornithin tạo thành Citrullin."),
        ("Vận chuyển ra bào tương", "Citrullin được kênh vận chuyển đặc hiệu ORNT1 mang qua màng trong ty thể ra bào tương để tiếp tục chu trình; đồng thời trao đổi Ornithin từ bào tương đi vào ty thể."),
        ("Đặc điểm bệnh thiếu hụt OTC", "Là bệnh rối loạn chu trình urê phổ biến nhất và là thể DUY NHẤT di truyền lặn liên kết nhiễm sắc thể X; Carbamoyl phosphat ứ đọng tràn ra bào tương đi vào con đường tổng hợp pyrimidin làm TĂNG RẤT CAO NỒNG ĐỘ ACID OROTIC TRONG NƯỚC TIỂU.")
    ],
    "Acid orotic niệu tăng cao giúp phân biệt chính xác thiếu hụt OTC với thiếu hụt CPS-I (cả hai đều tăng NH3 nhưng thiếu CPS-I thì acid orotic niệu bình thường hoặc giảm)."
))

cards.append(make_card(
    "HS17-B3-07", "B3", "Chu trình Urê - Phản ứng 3",
    "[CHU TRÌNH URÊ - BƯỚC 3] Enzyme ASS và Sự Đưa Nguyên Tử Nitơ Thứ Hai Vào Urê<br>Mô tả phản ứng ngưng tụ Citrullin với Aspartat bởi enzyme Argininosuccinat Synthetase (ASS) tại bào tương.",
    [
        ("Phản ứng ngưng tụ", "Citrullin kết hợp với Aspartat tạo thành Argininosuccinat nhờ enzyme Argininosuccinat Synthetase (ASS) tại bào tương tế bào gan."),
        ("Cung cấp Nitơ thứ hai", "Phân tử Aspartat đóng góp nhóm -NH2 chính là nguồn cung cấp nguyên tử Nitơ thứ hai cho phân tử urê sau này."),
        ("Chi phí năng lượng", "Phản ứng thủy phân 1 ATP thành AMP và Pyrophosphat vô cơ (PPi); sau đó Pyrophosphatase thủy phân PPi thành 2 Pi giúp phản ứng diễn ra một chiều hoàn toàn.")
    ],
    "Thiếu hụt enzyme ASS dẫn đến bệnh Citrullin máu type 1 (Citrullinemia Type I) đặc trưng bởi tăng vọt nồng độ Citrullin trong máu và nước tiểu."
))

cards.append(make_card(
    "HS17-B3-08", "B3", "Chu trình Urê - Phản ứng 4",
    "[CHU TRÌNH URÊ - BƯỚC 4] Enzyme ASL và Cầu Nối Tạo Fumarat Sang Chu Trình Krebs<br>Trình bày phản ứng phân cắt Argininosuccinat và vai trò kết nối chuyển hóa năng lượng qua phân tử Fumarat.",
    [
        ("Phản ứng phân cắt", "Enzym Argininosuccinat Lyase (ASL) phân cắt Argininosuccinat tạo thành Arginin và giải phóng Fumarat."),
        ("Số phận của Arginin", "Arginin tiếp tục đi vào phản ứng cuối cùng của chu trình urê để tạo urê."),
        ("Số phận của Fumarat (Cầu nối Krebs)", "Fumarat được chuyển đổi thành Malat trong bào tương; Malat đi vào ty thể biến thành Oxaloacetat tham gia chu trình Krebs hoặc chuyển amin tái tạo Aspartat (tạo thành Bánh xe Krebs - Krebs Bicycle).")
    ],
    "Bánh xe Krebs kết nối chặt chẽ giữa thoái hóa nitơ và sản xuất năng lượng, bù đắp một phần năng lượng ATP tiêu tốn cho chu trình urê."
))

cards.append(make_card(
    "HS17-B3-09", "B3", "Chu trình Urê - Phản ứng 5",
    "[CHU TRÌNH URÊ - BƯỚC 5] Enzyme Arginase Thủy Phân Giải Phóng Urê<br>Mô tả phản ứng thủy phân Arginin bởi enzyme Arginase và số phận của sản phẩm tạo thành.",
    [
        ("Phản ứng thủy phân", "Enzym Arginase (chỉ biểu hiện hoạt tính cao tại tế bào gan) thủy phân Arginin với sự tham gia của 1 phân tử nước giải phóng Urê tự do và tái sinh Ornithin."),
        ("Số phận phân tử Urê", "Urê khuếch tán tự do qua màng tế bào gan vào máu, theo tuần hoàn đến thận lọc qua cầu thận và đào thải ra nước tiểu (chiếm 80 – 90% lượng nitơ bài xuất của nước tiểu)."),
        ("Tái sinh Ornithin", "Ornithin được kênh vận chuyển ORNT1 đưa trở lại vào cơ chất ty thể để tiếp tục gắn với phân tử Carbamoyl phosphat mới, khởi động một chu trình urê tiếp theo.")
    ],
    "Vì chỉ có gan mới có hàm lượng Arginase dồi dào, các mô ngoại vi dù có thể tổng hợp được Arginin cũng không thể tạo ra Urê."
))

cards.append(make_card(
    "HS17-B3-10", "B3", "Bánh xe Krebs",
    "[BÁNH XE KREBS] Mối Liên Kết Tương Hỗ Giữa Chu Trình Urê và Chu Trình Acid Citric<br>Trình bày sơ đồ luân chuyển các chất trung gian kết nối giữa Chu trình Urê và Chu trình Krebs (Krebs Bicycle).",
    [
        ("Fumarat là điểm xuất phát", "Fumarat sinh ra từ phản ứng của enzyme ASL trong chu trình urê được biến đổi thành Malat nhờ enzyme Fumarase bào tương."),
        ("Chuyển hóa tạo Oxaloacetat", "Malat vào ty thể biến thành Oxaloacetat nhờ Malat dehydrogenase sinh ra 1 NADH (tương đương 2.5 ATP bù đắp chi phí chu trình urê)."),
        ("Tái tạo Aspartat", "Oxaloacetat nhận nhóm amin từ Glutamat nhờ AST tạo thành Aspartat; Aspartat lại ra bào tương cung cấp nitơ cho phản ứng 3 của chu trình urê, khép kín vòng quay tương hỗ.")
    ],
    "Mô hình Bánh xe Krebs giải thích vì sao hoạt tính enzyme AST lại rất cao trong tế bào gan để phục vụ luân chuyển nitơ liên tục."
))

cards.append(make_card(
    "HS17-B3-11", "B3", "Hệ thống bẫy amoniac Vùng 3",
    "[DỰ PHÒNG AMONIAC VÙNG 3] Vai Trò Bẫy Amoniac Của Enzyme Glutamin Synthetase<br>Giải thích cơ chế dự phòng bảo vệ nốt lượng amoniac thoát khỏi chu trình urê tại các tế bào gan Vùng 3 quanh tĩnh mạch trung tâm.",
    [
        ("Vị trí và đặc tính động học", "Enzym Glutamin Synthetase (GS) chỉ biểu hiện độc quyền ở 2 – 3 lớp tế bào gan Vùng 3 bọc quanh tĩnh mạch trung tâm; có chỉ số Km với NH3 cực kỳ thấp (ái lực rất cao)."),
        ("Cơ chế bẫy vét amoniac", "Lượng NH3 nồng độ thấp thoát khỏi chu trình urê ở Vùng 1 khi trôi theo dòng xoang mạch về đến tĩnh mạch trung tâm sẽ bị GS thu bắt hoàn toàn, gắn vào Glutamat tạo Glutamin."),
        ("Ý nghĩa sinh học sống còn", "Bảo đảm nồng độ NH3 đi vào tĩnh mạch trên gan đổ về tim và đại tuần hoàn luôn ở mức cực thấp, tuyệt đối không gây độc cho não bộ.")
    ],
    "Sự kết hợp: Vùng 1 có hệ thống CPS-I (dung lượng lớn, ái lực vừa) xử lý phần thô, Vùng 3 có GS (dung lượng nhỏ, ái lực cao) xử lý phần tinh."
))

# ==========================================
# B4: CHỨC NĂNG KHỬ ĐỘC CỦA GAN (11 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B4-01", "B4", "Đại cương Biến đổi sinh học",
    "[BIẾN ĐỔI SINH HỌC] Mục Tiêu Cốt Lõi Của Quá Trình Chuyển Hóa Thuốc và Độc Chất<br>Nêu mục tiêu sinh hóa của quá trình Biến đổi sinh học (Biotransformation) tại gan và đặc tính lý hóa của các chất trước và sau biến đổi.",
    [
        ("Đặc tính chất độc ban đầu", "Đa số các chất độc ngoại sinh (xenobiotics) và phân tử thuốc là các hợp chất ưa mỡ (lipophilic), không phân cực, dễ tan vào màng tế bào, khó lọc qua cầu thận và bị ống thận tái hấp thu thụ động hoàn toàn."),
        ("Mục tiêu biến đổi sinh học", "Gắn thêm hoặc bộc lộ các nhóm chức phân cực cao, chuyển các phân tử ưa mỡ thành các phân tử ưa nước (hydrophilic), ion hóa ở pH sinh lý, giảm hoặc mất độc tính sinh học."),
        ("Đào thải ra ngoại vi", "Các chất chuyển hóa phân cực dễ dàng hòa tan trong nước tiểu để đào thải qua thận, hoặc đào thải qua dịch mật theo phân ra ngoài.")
    ],
    "Quá trình biến đổi sinh học diễn ra qua 2 pha liên tiếp: Pha I (chức năng hóa) và Pha II (liên hợp)."
))

cards.append(make_card(
    "HS17-B4-02", "B4", "Hệ thống Cytochrome P450",
    "[HỆ THỐNG CYP450] Cấu Trúc Siêu Họ Hemoprotein và Cơ Chế Phản Ứng Pha I<br>Nêu bản chất cấu trúc của enzyme Cytochrome P450, nguồn gốc tên gọi và phương trình phản ứng oxy hóa tổng quát trong Pha I.",
    [
        ("Bản chất cấu trúc", "Là một siêu họ hemoprotein chứa nhân Protoporphyrin IX gắn ion sắt (Fe2+/Fe3+); định vị chủ yếu tại màng mạng lưới nội chất không hạt (microsome gan) và màng trong ty thể."),
        ("Nguồn gốc tên gọi P450", "Hấp thụ quang phổ cực đại ở bước sóng 450 nm khi nhân hem ở trạng thái khử Fe2+ tạo phức hợp với khí Carbon monoxide (CO)."),
        ("Phương trình phản ứng tổng quát", "Chất độc (R-H) + O2 + NADPH + H+ phản ứng dưới xúc tác của CYP450 và NADPH-cytochrome P450 reductase tạo ra R-OH + H2O + NADP+; một nguyên tử oxy gắn vào cơ chất, một nguyên tử oxy bị khử tạo nước.")
    ],
    "CYP3A4 là isoenzyme chiếm tỷ lệ cao nhất tại gan (khoảng 30%) và tham gia chuyển hóa hơn 50% các loại thuốc điều trị hiện nay trên lâm sàng."
))

cards.append(make_card(
    "HS17-B4-03", "B4", "Cảm ứng và Ức chế CYP450",
    "[TƯƠNG TÁC THUỐC CYP450] Cơ Chế Cảm Ứng vs Ức Chế Enzyme và Ví Dụ Kinh Điển<br>Phân biệt hậu quả lâm sàng của hiện tượng Cảm ứng (Induction) và Ức chế (Inhibition) enzyme CYP450 kèm ví dụ điển hình.",
    [
        ("Hiện tượng Cảm ứng (Induction)", "Thuốc hoặc chất hóa học làm tăng sinh lượng enzyme CYP450 (qua các thụ thể nhân PXR, CAR); hậu quả: tăng tốc độ chuyển hóa thuốc dùng kèm, làm giảm nồng độ điều trị của thuốc trong máu (gây thất bại điều trị); Ví dụ: Rifampicin, Phenobarbital, Carbamazepine, rượu mạn tính."),
        ("Hiện tượng Ức chế (Inhibition)", "Thuốc cạnh tranh vị trí gắn hoặc bất hoạt trực tiếp enzyme CYP450; hậu quả: giảm độ thanh thải thuốc dùng kèm, làm tăng vọt nồng độ thuốc trong máu dẫn đến ngộ độc; Ví dụ: Ketoconazole, Cimetidine, Clarithromycin, nước ép bưởi chùm (naringin)."),
        ("Ý nghĩa lâm sàng", "Luôn phải tra cứu tương tác thuốc chuyển hóa qua CYP450 trước khi phối hợp đa thuốc cho bệnh nhân.")
    ],
    "Uống thuốc hạ huyết áp Felodipine hoặc thuốc hạ mỡ máu Simvastatin cùng nước ép bưởi chùm có thể làm nồng độ thuốc tăng gấp 3 – 5 lần gây tụt huyết áp hoặc tiêu cơ vân."
))

cards.append(make_card(
    "HS17-B4-04", "B4", "Chuyển hóa Rượu tại gan",
    "[CHUYỂN HÓA RƯỢU] 3 Hệ Enzyme Thoái Hóa Ethanol và Hậu Quả Tăng Tỷ Số NADH/NAD+<br>Trình bày các hệ enzyme chuyển hóa ethanol và cơ chế bệnh sinh của việc tăng tỷ số NADH/NAD+ gây hạ đường huyết và gan nhiễm mỡ do rượu.",
    [
        ("3 hệ enzyme oxy hóa ethanol", "1) Alcohol dehydrogenase (ADH bào tương - con đường chính tạo Acetaldehyd); 2) ALDH (ty thể chuyển Acetaldehyd thành Acetat); 3) Hệ MEOS (CYP2E1 microsome - kích hoạt mạnh khi nghiện rượu mạn tính)."),
        ("Hậu quả tăng tỷ số NADH/NAD+", "Cả ADH và ALDH đều tiêu tốn NAD+ và sinh lượng lớn NADH; tỷ số NADH/NAD+ tăng vọt làm chuyển Pyruvat thành Lactat (gây toan lactic và cạn cơ chất tân tạo đường dẫn đến hạ đường huyết khi đói)."),
        ("Ức chế beta oxy hóa gây nhiễm mỡ gan", "Tỷ số NADH/NAD+ cao ức chế chu trình Krebs và ức chế phản ứng beta-oxy hóa acid béo; acid béo tích tụ được este hóa thành Triacylglycerol gây gan nhiễm mỡ do rượu (Alcoholic Steatosis).")
    ],
    "Acetaldehyd là chất độc mạnh gây tổn thương màng tế bào, hình thành các thể vùi Mallory-Denk và kích hoạt tế bào Ito gây xơ gan do rượu."
))

cards.append(make_card(
    "HS17-B4-05", "B4", "Ngộ độc Paracetamol",
    "[NGỘ ĐỘC PARACETAMOL] Cơ Chế Chuyển Hóa Tạo Chất Độc NAPQI và Cạn Kiệt Glutathion<br>Phân tích con đường chuyển hóa paracetamol ở liều điều trị và cơ chế gây hoại tử tế bào gan Vùng 3 khi dùng quá liều.",
    [
        ("Chuyển hóa ở liều điều trị", "Khoảng 90% paracetamol được liên hợp an toàn tại Pha II với Acid Glucuronic (UGT) và Sulfat (SULT) đào thải ra nước tiểu; chỉ dưới 5 – 10% bị CYP2E1 oxy hóa tạo NAPQI."),
        ("Tạo chất độc NAPQI khi quá liều", "Liều cao làm bão hòa con đường liên hợp Pha II; lượng lớn paracetamol chuyển hướng qua CYP2E1 tạo ồ ạt chất trung gian oxy hóa cực độc N-acetyl-p-benzoquinone imine (NAPQI)."),
        ("Cạn kiệt Glutathion và hoại tử gan", "NAPQI phản ứng làm cạn kiệt kho dự trữ Glutathion (GSH) nội bào (> 70%); lượng NAPQI tự do dư thừa gắn cộng hóa trị vào protein tế bào gan gây stress oxy hóa, hủy hoại ty thể và hoại tử ồ ạt tế bào gan Vùng 3.")
    ],
    "Người nghiện rượu mạn tính hoặc dùng thuốc cảm ứng CYP2E1 có nguy cơ ngộ độc paracetamol nặng nề hơn ngay cả ở liều điều trị thông thường."
))

cards.append(make_card(
    "HS17-B4-06", "B4", "Điều trị ngộ độc Paracetamol",
    "[THUỐC GIẢI ĐỘC NAC] Cơ Chế Dược Lý Của N-Acetylcysteine và Cửa Sổ Vàng Điều Trị<br>Trình bày cơ chế giải độc của N-acetylcysteine (NAC) và tầm quan trọng của đồ thị Rumack-Matthew trên lâm sàng.",
    [
        ("Cung cấp Cysteine tổng hợp Glutathion", "NAC xâm nhập tế bào gan cung cấp L-cysteine (là acid amin giới hạn tốc độ tổng hợp Glutathion); giúp tế bào gan phục hồi nhanh chóng kho dự trữ GSH nội bào."),
        ("Bất hoạt trực tiếp NAPQI", "Nhóm sulfhydryl (-SH) tự do của NAC có thể liên kết trực tiếp với phân tử NAPQI tạo chất chuyển hóa không độc đào thải qua nước tiểu; đồng thời NAC đóng vai trò chất chống oxy hóa dọn dẹp gốc tự do ROS."),
        ("Cửa sổ vàng điều trị (Đồ thị Rumack-Matthew)", "Hiệu quả bảo vệ gan gần như 100% nếu dùng NAC trong vòng 8 – 10 giờ đầu sau khi uống quá liều paracetamol; sau 10 giờ hiệu quả giảm dần nhưng vẫn có chỉ định cứu sống tế bào gan.")
    ],
    "Phác đồ NAC đường uống 72 giờ hoặc truyền tĩnh mạch 21 giờ là tiêu chuẩn vàng xử trí ngộ độc cấp Paracetamol."
))

cards.append(make_card(
    "HS17-B4-07", "B4", "Pha II - Liên hợp Acid Glucuronic",
    "[LIÊN HỢP GLUCURONID] Enzyme UGT1A1, Cơ Chất Hoạt Hóa UDPGA và Ý Nghĩa<br>Nêu enzyme xúc tác, phân tử cơ chất hoạt hóa và các chất nội sinh/ngoại sinh tham gia phản ứng liên hợp với Acid Glucuronic.",
    [
        ("Enzyme xúc tác", "UDP-glucuronosyltransferase (họ enzym UGT, đặc biệt UGT1A1 định vị tại màng lưới nội chất)."),
        ("Cơ chất hoạt hóa cho acid glucuronic", "UDP-glucuronic acid (UDPGA), được tổng hợp từ Glucose-1-phosphat qua UDP-glucose nhờ enzyme UDP-glucose dehydrogenase phụ thuộc NAD+."),
        ("Các chất được liên hợp", "Bilirubin (tạo bilirubin diglucuronide), hormon steroid (estrogen, cortisol), morphin, paracetamol, diazepam; làm tăng tính tan trong nước và giảm hoạt tính sinh học.")
    ],
    "Liên hợp glucuronid là con đường liên hợp Pha II phổ biến nhất và có dung lượng chuyển hóa lớn nhất tại gan người."
))

cards.append(make_card(
    "HS17-B4-08", "B4", "Pha II - Liên hợp Sulfat",
    "[LIÊN HỢP SULFAT] Enzyme SULT, Cơ Chất Hoạt Hóa PAPS và Phân Biệt Với UGT<br>Trình bày phản ứng liên hợp sulfat, phân tử mang gốc sulfat hoạt hóa PAPS và so sánh đặc tính dung lượng với phản ứng glucuronid.",
    [
        ("Enzyme xúc tác", "Sulfotransferase (siêu họ SULT) định vị chủ yếu tại bào tương tế bào gan."),
        ("Cơ chất mang sulfat hoạt hóa", "3'-Phosphoadenosine-5'-phosphosulfate (PAPS), được tổng hợp từ ATP và ion Sulfat vô cơ (SO4 2-)."),
        ("Đặc tính ái lực cao - dung lượng thấp", "Hệ thống SULT có ái lực rất cao với cơ chất (chỉ số Km rất thấp) nên hoạt động tốt ở nồng độ chất độc thấp; tuy nhiên nguồn dự trữ PAPS hạn chế nên hệ thống dễ bị bão hòa nhanh chóng khi nồng độ chất độc tăng cao (nhường chỗ cho hệ UGT dung lượng lớn).")
    ],
    "SULT tham gia bất hoạt hormon steroid, catecholamin, paracetamol liều thấp và các độc chất phenolic."
))

cards.append(make_card(
    "HS17-B4-09", "B4", "Pha II - Liên hợp Glutathion",
    "[LIÊN HỢP GLUTATHION] Cấu Trúc Tripeptid GSH và Sự Tạo Thành Acid Mercapturic<br>Nêu cấu trúc phân tử của Glutathion (GSH), enzyme Glutathione S-Transferase (GST) và con đường đào thải qua dẫn xuất Acid Mercapturic.",
    [
        ("Cấu trúc phân tử Glutathion (GSH)", "Tripeptid gồm 3 acid amin: gamma-Glutamyl - Cysteinyl - Glycin; hoạt tính khử độc nằm ở nhóm sulfhydryl (-SH) tự do của gốc Cysteine."),
        ("Enzyme xúc tác GST", "Glutathione S-transferase (GST) xúc tác gắn nhóm -SH của GSH vào các phân tử ái điện tử (electrophilic) độc hại hoặc các gốc tự do ROS."),
        ("Tạo dẫn xuất Acid Mercapturic đào thải", "Phức hợp chuyển hóa qua thận bị cắt bỏ gốc glutamate và glycine, sau đó gốc cysteine còn lại được acetyl hóa tạo dẫn xuất Acid Mercapturic bài tiết an toàn qua nước tiểu.")
    ],
    "GSH nội bào là lá chắn chống oxy hóa bảo vệ tế bào gan khỏi hoại tử do các chất chuyển hóa electrophilic độc hại."
))

cards.append(make_card(
    "HS17-B4-10", "B4", "Pha II - Acetyl hóa và Đa hình NAT2",
    "[PHẢN ỨNG ACETYL HÓA] Enzyme NAT2, Cơ Chất Acetyl-CoA và Đa Hình Di Truyền Kháng Lao<br>Trình bày phản ứng acetyl hóa qua enzyme N-acetyltransferase và ý nghĩa lâm sàng của hiện tượng đa hình kiểu hình acetyl hóa nhanh vs chậm khi dùng thuốc Isoniazid (INH).",
    [
        ("Enzyme xúc tác và cơ chất", "N-acetyltransferase (NAT1 và NAT2) tại bào tương tế bào gan, sử dụng phân tử Acetyl-CoA làm chất cho gốc acetyl gắn lên nhóm amin của thuốc."),
        ("Kiểu hình Acetyl hóa chậm (Slow acetylators)", "Đột biến gen NAT2 làm giảm hoạt tính enzyme; nồng độ INH tự do trong máu duy trì ở mức cao kéo dài; nguy cơ cao gặp độc tính viêm dây thần kinh ngoại vi (do cạnh tranh Vitamin B6) và tổn thương tế bào gan."),
        ("Kiểu hình Acetyl hóa nhanh (Rapid acetylators)", "Chuyển hóa INH thành acetyl-isoniazid quá nhanh; làm giảm nồng độ điều trị trong máu gây nguy cơ thất bại điều trị lao và kháng thuốc.")
    ],
    "Tỷ lệ người acetyl hóa chậm chiếm khoảng 50% ở người da trắng và người da đen, nhưng chỉ chiếm khoảng 10 – 20% ở người Đông Á."
))

cards.append(make_card(
    "HS17-B4-11", "B4", "Pha II - Liên hợp Glycin và Methyl hóa",
    "[LIÊN HỢP GLYCIN VÀ METHYL HÓA] Acid Hippuric và Vai Trò Cơ Chất SAM<br>Nêu cơ chế tạo Acid Hippuric từ Acid Benzoic và vai trò của S-adenosylmethionine (SAM) trong phản ứng methyl hóa tại gan.",
    [
        ("Liên hợp Glycin tạo Acid Hippuric", "Acid benzoic (chất bảo quản thực phẩm) được hoạt hóa thành Benzoyl-CoA rồi ngưng tụ với Glycin nhờ enzyme Glycine N-acyltransferase tạo thành Acid Hippuric không độc đào thải qua nước tiểu (trước đây dùng làm nghiệm pháp thăm dò chức năng khử độc của gan)."),
        ("Phản ứng Methyl hóa qua SAM", "S-adenosylmethionine (SAM) là phân tử cung cấp nhóm methyl (-CH3) hoạt động nhờ enzyme Methyltransferase (như COMT); bất hoạt catecholamin, histamine và methyl hóa DNA."),
        ("Ý nghĩa sinh học", "Đảm bảo tính đa dạng của hệ thống khử độc, giúp gan xử lý được hầu như toàn bộ các cấu trúc hóa học độc chất khác nhau trong tự nhiên.")
    ],
    "Nghiệm pháp Quick cho bệnh nhân uống natri benzoat rồi định lượng acid hippuric trong nước tiểu 4 giờ để đánh giá chức năng gan hiện nay đã được thay thế bằng các xét nghiệm enzyme hiện đại."
))

# ==========================================
# B5: CHỨC NĂNG TẠO MẬT VÀ TUẦN HOÀN RUỘT GAN (12 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B5-01", "B5", "Thành phần sinh hóa dịch mật",
    "[THÀNH PHẦN DỊCH MẬT] So Sánh Mật Gan vs Mật Túi Mật và Tỷ Lệ Các Chất Hòa Tan<br>So sánh nồng độ nước giữa mật gan và mật túi mật và liệt kê các thành phần hòa tan chính cấu tạo nên dịch mật.",
    [
        ("Cô đặc tại túi mật", "Mật gan chứa 97% nước; khi lưu trữ tại túi mật, niêm mạc túi mật tích cực bơm tái hấp thu ion Na+, Cl- và kéo nước theo, cô đặc dịch mật từ 5 – 10 lần (mật túi mật chỉ còn khoảng 89% nước)."),
        ("Các chất hòa tan chính", "Muối mật chiếm tỷ lệ lớn nhất (khoảng 65 – 70% chất khô); Phospholipid (chủ yếu là Lecithin) chiếm 20%; Cholesterol tự do chiếm 4 – 5%; Sắc tố mật Bilirubin chiếm 1 – 2%; Protein và các chất điện giải."),
        ("Độ pH của dịch mật", "Mật gan có tính kiềm nhẹ (pH 7.5 – 8.0) nhờ lượng HCO3- do biểu mô ống mật tiết; mật túi mật có xu hướng toan hóa nhẹ (pH 6.0 – 7.0) do quá trình cô đặc và tái hấp thu.")
    ],
    "Chức năng chính của dịch mật là nhũ tương hóa lipid thức ăn hỗ trợ enzyme lipase tụy tiêu hóa mỡ và bài xuất cholesterol dư thừa ra khỏi cơ thể."
))

cards.append(make_card(
    "HS17-B5-02", "B5", "Sinh tổng hợp Acid mật nguyên phát",
    "[ACID MẬT NGUYÊN PHÁT] Enzyme Cholesterol 7alpha-Hydroxylase và Hai Sản Phẩm Cốt Lõi<br>Trình bày phản ứng giới hạn tốc độ sinh tổng hợp acid mật nguyên phát từ cholesterol và tên 2 phân tử acid mật nguyên phát.",
    [
        ("Cơ chất ban đầu", "Cholesterol tự do tại gan; sinh tổng hợp acid mật là con đường thoái hóa duy nhất để đào thải lượng cholesterol dư thừa ra ngoài cơ thể (khoảng 0.5 g/ngày)."),
        ("Enzyme giới hạn tốc độ CYP7A1", "Cholesterol 7alpha-hydroxylase (CYP7A1, thuộc họ CYP450 ty thể/microsome) xúc tác đưa nhóm -OH vào vị trí C7 của nhân steroid tạo 7alpha-hydroxycholesterol; phản ứng tiêu tốn O2 và NADPH."),
        ("2 acid mật nguyên phát", "Acid Cholic (chứa 3 nhóm -OH tại vị trí C3, C7, C12 - trihydroxy) và Acid Chenodeoxycholic (chứa 2 nhóm -OH tại C3, C7 - dihydroxy).")
    ],
    "Đột biến mất chức năng gen CYP7A1 dẫn đến ứ đọng cholesterol nặng trong gan, tăng cholesterol máu đề kháng statin và sỏi mật sớm."
))

cards.append(make_card(
    "HS17-B5-03", "B5", "Điều hòa tổng hợp Acid mật",
    "[ĐIỀU HÒA CYP7A1] Cơ Chế Phản Hồi Âm Tính Qua Thụ Thể Nhân FXR và Protein SHP<br>Mô tả cơ chế ức chế điều hòa ngược âm tính của acid mật đối với enzyme CYP7A1 thông qua thụ thể nhân tế bào.",
    [
        ("Kích hoạt thụ thể FXR", "Khi lượng acid mật quay về gan qua tuần hoàn ruột gan tăng cao, chúng gắn và kích hoạt thụ thể nhân Farnesoid X Receptor (FXR) trong nhân tế bào gan."),
        ("Cảm ứng protein ức chế SHP", "Phức hợp FXR kích hoạt phiên mã gen mã hóa protein ức chế Small Heterodimer Partner (SHP)."),
        ("Ức chế phiên mã CYP7A1", "Protein SHP tương tác ức chế yếu tố phiên mã LRH-1 (Liver Receptor Homolog-1), dẫn đến ngừng phiên mã gen CYP7A1; làm giảm tổng hợp acid mật mới khi lượng muối mật đã dư thừa.")
    ],
    "Thuốc đồng vận thụ thể FXR (như Obeticholic acid) đang được ứng dụng điều trị viêm đường mật nguyên phát (PBC) và viêm gan thoái hóa mỡ không do rượu (NASH)."
))

cards.append(make_card(
    "HS17-B5-04", "B5", "Tạo Muối mật qua liên hợp",
    "[TẠO MUỐI MẬT] Phản Ứng Liên Hợp Với Glycin / Taurin và Sự Giảm Trị Số pKa<br>Giải thích vì sao acid mật nguyên phát bắt buộc phải liên hợp với Glycin hoặc Taurin trước khi bài xuất vào dịch mật.",
    [
        ("Đặc tính acid mật tự do", "Acid mật tự do có chỉ số pKa ~ 6; ở pH dịch tá tràng (pH 6 – 7), phần lớn tồn tại dạng không ion hóa kỵ nước, kém tan và dễ kết tủa, không phát huy được tác dụng nhũ tương hóa mỡ."),
        ("Liên hợp với Glycin và Taurin", "Acid mật được hoạt hóa thành dẫn xuất acyl-CoA rồi liên hợp tại gan với Glycin (chiếm tỷ lệ 75%) tạo Acid Glycocholic, hoặc với Taurin (chiếm 25%) tạo Acid Taurocholic."),
        ("Hạ thấp pKa tạo Muối mật (Bile salts)", "Liên hợp Glycin hạ pKa xuống ~ 3.7; liên hợp Taurin hạ pKa xuống ~ 1.5; ở pH ruột chúng ion hóa 100% mang điện tích âm gắn với Na+/K+ tạo thành Muối mật tan hoàn toàn trong nước và có hoạt tính bề mặt lưỡng cực cực mạnh.")
    ],
    "Đầu kỵ nước gắn vào giọt mỡ, đầu ưa nước tích điện âm hướng ra môi trường nước đẩy nhau, tạo thành các hạt nhũ tương kích thước nano cho lipase tụy tiếp cận."
))

cards.append(make_card(
    "HS17-B5-05", "B5", "Sinh tổng hợp Acid mật thứ phát",
    "[ACID MẬT THỨ PHÁT] Enzyme Của Vi Khuẩn Đường Ruột BSH và 7alpha-Dehydroxylase<br>Trình bày quá trình vi khuẩn đường ruột biến đổi acid mật nguyên phát thành acid mật thứ phát tại đoạn cuối hồi tràng và đại tràng.",
    [
        ("Phản ứng cắt liên hợp (Deconjugation)", "Vi khuẩn đường ruột tiết enzyme Bile Salt Hydrolase (BSH) thủy phân liên kết peptid, tách giải phóng Glycin / Taurin và acid mật tự do."),
        ("Phản ứng khử nhóm 7alpha-OH", "Các vi khuẩn kỵ khí (Clostridium, Bacteroides) tiết enzyme 7alpha-dehydroxylase khử nhóm -OH tại vị trí C7 của phân tử acid mật nguyên phát."),
        ("2 acid mật thứ phát tạo thành", "Acid Cholic (3 nhóm -OH) bị khử thành Acid Deoxycholic (2 nhóm -OH tại C3, C12); Acid Chenodeoxycholic (2 nhóm -OH) bị khử thành Acid Lithocholic (chỉ còn 1 nhóm -OH tại C3).")
    ],
    "Acid mật thứ phát có tính kỵ nước cao hơn nhiều so với acid mật nguyên phát."
))

cards.append(make_card(
    "HS17-B5-06", "B5", "Độc tính của Acid Lithocholic",
    "[ĐỘC TÍNH LITHOCHOLIC] Đặc Tính Kỵ Nước, Cơ Chế Đào Thải và Nguy Cơ Tổn Thương Màng<br>Giải thích vì sao Acid Lithocholic lại có độc tính tế bào cao nhất và cơ chế gan bất hoạt phân tử này.",
    [
        ("Tính chất vật lý cực kỳ kỵ nước", "Chỉ mang duy nhất 1 nhóm -OH ở vị trí C3; là phân tử kỵ nước nhất trong các acid mật, dễ hòa tan phá vỡ cấu trúc lipid màng tế bào gan và niêm mạc đại tràng."),
        ("Sulfat hóa tại tế bào gan", "Một lượng nhỏ Lithocholic tái hấp thu về gan sẽ bị enzyme Sulfotransferase (SULT2A1) gắn nhóm sulfat tại C3 tạo thành dẫn xuất Sulfolithocholic."),
        ("Đào thải hoàn toàn ra phân", "Dẫn xuất sulfat không còn khả năng tái hấp thu ở ruột, bị giữ lại trong lòng đại tràng và đào thải hoàn toàn qua phân ra ngoài, bảo vệ cơ thể khỏi ngộ độc acid mật.")
    ],
    "Ngược lại, Acid Deoxycholic được tái hấp thu một phần (khoảng 30 – 50%) quay về gan tham gia vào pool acid mật toàn thân."
))

cards.append(make_card(
    "HS17-B5-07", "B5", "Tuần hoàn ruột - gan của Muối mật",
    "[TUẦN HOÀN RUỘT GAN] Kênh Vận Chuyển ASBT, Tỷ Lệ Tái Hấp Thu và Kích Thước Pool<br>Nêu số lượng muối mật bài tiết mỗi ngày, kích thước tổng pool muối mật và cơ chế tái hấp thu tích cực tại đoạn cuối hồi tràng.",
    [
        ("Kích thước Pool vs Lượng bài tiết", "Tổng lượng muối mật trong cơ thể (bile acid pool) chỉ khoảng 3 – 5 g; tuy nhiên lượng muối mật bài tiết vào ruột mỗi ngày lên tới 20 – 30 g (nhờ chu chuyển 4 – 12 chu kỳ mỗi ngày)."),
        ("Tái hấp thu tích cực qua kênh ASBT", "Khoảng 95% lượng muối mật được tái hấp thu tích cực tại đoạn cuối hồi tràng thông qua kênh đồng vận chuyển Apical Sodium-dependent Bile acid Transporter (ASBT)."),
        ("Đào thải qua phân và bù trừ", "Chỉ khoảng 5% (khoảng 0.5 g/ngày) thoát khỏi tái hấp thu và thải ra theo phân; lượng mất này được tế bào gan tổng hợp mới chính xác tương đương từ cholesterol để bù đắp.")
    ],
    "Cắt đoạn cuối hồi tràng hoặc viêm hồi tràng (bệnh Crohn) làm mất kênh ASBT, gây tiêu chảy mỡ và cạn kiệt pool muối mật dẫn đến hình thành sỏi mật."
))

cards.append(make_card(
    "HS17-B5-08", "B5", "Thuốc gắn acid mật hạ mỡ máu",
    "[THUỐC GẮN ACID MẬT] Cơ Chế Dược Lý Của Cholestyramine Hạ Cholesterol Máu<br>Giải thích cơ chế sinh hóa giúp nhóm thuốc nhựa gắn acid mật (Cholestyramine, Colestipol) làm hạ nồng độ LDL-Cholesterol huyết tương.",
    [
        ("Bắt giữ acid mật trong lòng ruột", "Nhựa gắn acid mật là các polyme tích điện dương không hấp thu; tạo phức hợp không tan liên kết ion với muối mật tích điện âm trong lòng ruột, ngăn cản tái hấp thu qua kênh ASBT."),
        ("Tăng đào thải muối mật qua phân", "Lượng muối mật bài xuất ra phân tăng gấp 3 – 10 lần, làm cắt đứt tuần hoàn ruột gan của muối mật về tế bào gan."),
        ("Kích hoạt CYP7A1 và tăng biểu hiện LDL-R", "Gan mất ức chế phản hồi âm tính, kích hoạt tối đa enzym CYP7A1 để chuyển hóa cholesterol nội bào thành acid mật mới; nồng độ cholesterol nội bào giảm kích hoạt hệ SREBP-2 tăng biểu hiện thụ thể LDL receptor kéo mạnh LDL từ máu vào gan.")
    ],
    "Tác dụng phụ thường gặp của thuốc là đầy bụng, táo bón và có thể làm tăng nhẹ triglycerid máu do kích thích gan tăng tổng hợp VLDL bù trừ."
))

cards.append(make_card(
    "HS17-B5-09", "B5", "Cân bằng hòa tan Cholesterol trong mật",
    "[TAM GIÁC ADMIRAND & SMALL] Cấu Trúc Micelle Hỗn Hợp và Tỷ Lệ Hòa Tan Tới Hạn<br>Trình bày mô hình tam giác cân bằng hòa tan Admirand & Small giữa Cholesterol, Muối mật và Lecithin trong dịch mật.",
    [
        ("Bản chất không tan của Cholesterol", "Cholesterol tự do hoàn toàn không hòa tan trong môi trường nước của mật."),
        ("Hạt Micelle hỗn hợp (Mixed micelles)", "Cholesterol kỵ nước được hòa tan vào lõi trung tâm của hạt micelle hỗn hợp, được bao bọc xung quanh bởi các phân tử Phospholipid (Lecithin) và Muối mật hướng đầu phân cực ra môi trường nước."),
        ("Tam giác Admirand & Small", "Trạng thái hòa tan phụ thuộc vào tỷ lệ nồng độ mol giữa 3 thành phần: Cholesterol, Muối mật và Phospholipid; khi tỷ lệ Cholesterol vượt quá khả năng hòa tan của micelle, mật rơi vào trạng thái bão hòa quá mức (supersaturated) và bắt đầu kết tủa tinh thể.")
    ],
    "Chỉ số bão hòa Cholesterol (Cholesterol Saturation Index - CSI) > 1.0 là điều kiện tiên quyết bắt buộc để hình thành sỏi mật cholesterol."
))

cards.append(make_card(
    "HS17-B5-10", "B5", "Cơ chế sinh sỏi Cholesterol",
    "[SỎI MẬT CHOLESTEROL] 3 Yếu Tố Bệnh Sinh Cốt Lõi và Quy Tắc 4F Lâm Sàng<br>Trình bày 3 rối loạn sinh hóa bệnh sinh cốt lõi tạo sỏi cholesterol và các yếu tố nguy cơ kinh điển trên lâm sàng.",
    [
        ("Tăng tiết Cholesterol quá mức", "Gan bài tiết lượng cholesterol vượt quá khả năng hòa tan của muối mật và phospholipid (do béo phì, chế độ ăn giàu calo, tăng hoạt tính HMG-CoA reductase)."),
        ("Giảm tiết Muối mật hoặc Phospholipid", "Suy giảm tổng hợp acid mật (thiếu CYP7A1) hoặc mất muối mật qua phân do bệnh hồi tràng; làm giảm dung lượng hòa tan của dịch mật."),
        ("Giảm co bóp ứ trệ túi mật (Gallbladder stasis)", "Túi mật đờ, co bóp kém tạo điều kiện cho các tinh thể cholesterol đơn phân ngưng tụ, tạo nhân (nucleation) và phát triển thành viên sỏi hoàn chỉnh."),
        ("Quy tắc 4F nguy cơ lâm sàng", "Female (Nữ giới - estrogen làm tăng tiết cholesterol vào mật), Forty (Tuổi trung niên >= 40), Fat (Béo phì), Fertile (Đã sinh đẻ nhiều lần).")
    ],
    "Estrogen làm tăng hấp thu cholesterol và tăng bài tiết cholesterol vào mật, trong khi progesterone làm dãn cơ trơn gây ứ đọng túi mật."
))

cards.append(make_card(
    "HS17-B5-11", "B5", "Cơ chế sinh sỏi Sắc tố mật",
    "[SỎI SẮC TỐ MẬT] Phân Biệt Cơ Chế Tạo Sỏi Sắc Tố Đen vs Sỏi Sắc Tố Nâu<br>So sánh vị trí hình thành, nguyên nhân sinh bệnh và cơ chế sinh hóa giữa Sỏi sắc tố đen và Sỏi sắc tố nâu.",
    [
        ("Sỏi sắc tố đen (Black pigment stones)", "Hình thành chủ yếu trong túi mật; mật vô trùng; gặp ở bệnh nhân tan máu mạn tính (Thalassemia, hồng cầu hình liềm) hoặc xơ gan; lượng lớn bilirubin gián tiếp dư thừa vào mật kết hợp với ion Calci tạo muối Calci Bilirubinate không tan."),
        ("Sỏi sắc tố nâu (Brown pigment stones)", "Hình thành chủ yếu trong ống mật chủ (đường mật trong và ngoài gan); luôn liên quan đến NHIỄM TRÙNG ĐƯỜNG MẬT hoặc ký sinh trùng (Giun chui ống mật, sán lá gan)."),
        ("Vai trò enzyme beta-glucuronidase", "Vi khuẩn (E. coli, Klebsiella) tiết enzyme beta-glucuronidase thủy phân Bilirubin trực tiếp thành Bilirubin tự do; đồng thời tiết Phospholipase A thủy phân lecithin tạo acid béo; chúng ngưng tụ với calci tạo sỏi sắc tố nâu mềm dạng bùn.")
    ],
    "Sỏi đen cứng, cản quang tốt trên X-quang; sỏi nâu mềm như bùn đất, không cản quang và thường gây viêm đường mật tái diễn."
))

cards.append(make_card(
    "HS17-B5-12", "B5", "Thuốc làm tan sỏi Acid Ursodeoxycholic",
    "[THUỐC UDCA] Bản Chất Cấu Trúc, Cơ Chế Hòa Tan Sỏi và Tác Dụng Bảo Vệ Gan<br>Nêu bản chất của Acid Ursodeoxycholic (UDCA / Ursodiol) và cơ chế phân tử giúp làm tan sỏi mật cholesterol và bảo vệ tế bào gan trong bệnh ứ mật.",
    [
        ("Bản chất cấu trúc", "Đồng phân 7beta-epimer của acid chenodeoxycholic; là acid mật có tính ưa nước cao nhất và hoàn toàn không độc đối với màng tế bào."),
        ("Cơ chế làm tan sỏi mật cholesterol", "UDCA ức chế hấp thu cholesterol ở ruột và ức chế bài tiết cholesterol từ gan vào mật; làm giảm chỉ số bão hòa cholesterol (CSI) của mật, phân tán cholesterol dạng tinh thể lỏng hòa tan sỏi."),
        ("Bảo vệ tế bào gan trong ứ mật", "Chiếm chỗ và đẩy các acid mật kỵ nước độc hại (cholic, deoxycholic) ra khỏi tế bào gan và đường mật; bảo vệ màng ty thể, chống apoptosis và kích thích bài tiết mật giàu bicacbonat.")
    ],
    "UDCA là thuốc điều trị đầu tay tiêu chuẩn kéo dài thời gian sống không cần ghép gan cho bệnh nhân Viêm đường mật nguyên phát (PBC)."
))

# ==========================================
# B6: XÉT NGHIỆM TỔN THƯƠNG TẾ BÀO GAN VÀ Ứ MẬT (12 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B6-01", "B6", "Enzyme Alanin Aminotransferase",
    "[ENZYME ALT] Phân Bố Tế Bào, Cơ Chế Phản Ứng và Tính Đặc Hiệu Cho Gan<br>Nêu phản ứng trao đổi amin của ALT, vị trí định vị dưới tế bào và lý do vì sao ALT đặc hiệu cho tổn thương gan hơn AST.",
    [
        ("Phản ứng trao đổi amin", "L-Alanin + alpha-Ketoglutarat phản ứng thuận nghịch tạo Pyruvat + L-Glutamat; coenzyme bắt buộc là Pyridoxal-5-phosphat (PLP / Vitamin B6)."),
        ("Phân bố tế bào", "ALT định vị gần như độc quyền tại bào tương của tế bào nhu mô gan (nồng độ trong tế bào gan cao gấp 3000 lần nồng độ trong máu)."),
        ("Tính đặc hiệu cao cho gan", "Mặc dù có lượng nhỏ ở thận, tim và cơ vân, nhưng sự tăng cao ALT huyết thanh phản ánh tính đặc hiệu rất cao cho tình trạng tổn thương hoại tử màng tế bào gan.")
    ],
    "Thời gian bán hủy của ALT trong máu khoảng 47 +- 10 giờ (dài hơn đáng kể so với AST)."
))

cards.append(make_card(
    "HS17-B6-02", "B6", "Enzyme Aspartat Aminotransferase",
    "[ENZYME AST] Hai Dạng Isoenzyme Bào Tương vs Ty Thể và Phân Bố Mô Rộng Rãi<br>Trình bày phản ứng xúc tác của AST, hai dạng isoenzyme dưới tế bào và các mô cơ quan có chứa enzyme này.",
    [
        ("Phản ứng trao đổi amin", "L-Aspartat + alpha-Ketoglutarat thuận nghịch tạo Oxaloacetat + L-Glutamat; đòi hỏi coenzyme Pyridoxal-5-phosphat (PLP)."),
        ("Hai dạng Isoenzyme dưới tế bào", "cAST (bào tương, chiếm 20 – 30% tổng hoạt độ trong gan) và mAST (ty thể, chiếm 70 – 80% tổng hoạt độ trong gan)."),
        ("Phân bố mô rộng rãi", "Có mặt với nồng độ cao ở cơ tim, tế bào gan, cơ vân xương, thận, não, tụy, phổi và hồng cầu; do đó tăng AST huyết thanh kém đặc hiệu cho gan hơn ALT (cần loại trừ nhồi máu cơ tim, tiêu cơ vân, tan máu).")
    ],
    "mAST chỉ được giải phóng vào máu khi có tổn thương hoại tử cấu trúc sâu của tế bào gan ảnh hưởng đến màng ty thể."
))

cards.append(make_card(
    "HS17-B6-03", "B6", "Biên độ tăng Men Gan trên lâm sàng",
    "[MỨC ĐỘ TĂNG TRANSAMINASE] Phân Tầng Biên Độ và Ý Nghĩa Định Hướng Nguyên Nhân<br>Nêu các mốc biên độ tăng men gan (AST, ALT) trên lâm sàng và các bệnh cảnh nguyên nhân tương ứng.",
    [
        ("Tăng nhẹ đến vừa (< 5 lần giới hạn trên bình thường - ULN)", "Hoạt độ < 200 – 250 U/L; gặp trong: Gan nhiễm mỡ không do rượu (NAFLD), Viêm gan mạn (HBV, HCV), Ứ mật, Xơ gan, Tổn thương cơ."),
        ("Tăng vừa (5 – 15 lần ULN)", "Hoạt độ 250 – 1000 U/L; gặp trong: Viêm gan do rượu, Viêm gan tự miễn, Đợt bùng phát viêm gan virus mạn."),
        ("Tăng rất cao (> 15 – 20 lần ULN đến hàng nghìn U/L)", "Hoạt độ > 1000 – 10.000 U/L; chỉ gặp trong 3 nhóm nguyên nhân cấp tính: 1) Viêm gan virus cấp (A, B, E); 2) Thiếu máu cục bộ tụt huyết áp (Ischemic hepatitis / Shock liver); 3) Nhiễm độc gan tối cấp (Paracetamol, nấm độc Amanita).")
    ],
    "Trong sốc gan hoặc ngộ độc paracetamol, transaminase tăng vọt đạt đỉnh trong 24 – 48 giờ rồi giảm rất nhanh khi tế bào gan ngừng hoại tử hoặc đã hoại tử cạn kiệt."
))

cards.append(make_card(
    "HS17-B6-04", "B6", "Tỷ số De Ritis AST/ALT",
    "[TỶ SỐ DE RITIS] Ý Nghĩa Tỷ Số AST/ALT Trong Phân Biệt Các Bệnh Lý Gan Mật<br>Nêu giá trị sinh lý bình thường của tỷ số De Ritis và ý nghĩa chẩn đoán khi tỷ số < 1, > 2 và > 1 ở bệnh gan mạn.",
    [
        ("Giá trị bình thường", "Ở người khỏe mạnh, tỷ số AST/ALT huyết thanh dao động khoảng 0.8."),
        ("Tỷ số AST/ALT < 1", "ALT tăng cao hơn AST; điển hình trong tổn thương tế bào gan cấp tính còn bù: Viêm gan virus cấp, Gan nhiễm mỡ không do rượu (NAFLD/NASH), Viêm gan mạn giai đoạn sớm."),
        ("Tỷ số AST/ALT > 2", "AST tăng cao gấp đôi ALT (trong khi hoạt độ tuyệt đối thường < 300 – 500 U/L); là dấu hiệu chỉ điểm kinh điển có giá trị gợi ý rất cao cho Viêm gan do rượu (Alcoholic hepatitis)."),
        ("Tỷ số AST/ALT > 1 ở bệnh gan mạn", "Bình thường viêm gan mạn có AST/ALT < 1; khi tỷ số đảo ngược chuyển thành > 1 là dấu hiệu sinh hóa cảnh báo bệnh nhân đã tiến triển sang giai đoạn Xơ gan (Cirrhosis).")
    ],
    "Tỷ số De Ritis là công cụ sinh hóa đơn giản nhưng cực kỳ giá trị để phân biệt bệnh gan do rượu với bệnh gan thoái hóa mỡ không do rượu."
))

cards.append(make_card(
    "HS17-B6-05", "B6", "Cơ chế De Ritis > 2 do Rượu",
    "[CƠ CHẾ DE RITIS > 2] 3 Yếu Tố Sinh Hóa Giải Thích AST Tăng Vượt Trội ALT Do Rượu<br>Phân tích 3 cơ chế sinh hóa giải thích vì sao ở bệnh nhân viêm gan do rượu thì AST lại tăng cao hơn hẳn ALT.",
    [
        ("Độc tính ty thể của rượu", "Rượu và acetaldehyd gây độc màng ty thể tế bào gan, kích thích giải phóng ồ ạt dạng isoenzyme AST ty thể (mAST) vào tuần hoàn."),
        ("Thiếu hụt Vitamin B6 (Pyridoxal phosphat)", "Bệnh nhân nghiện rượu thường suy dinh dưỡng và thiếu hụt trầm trọng Vitamin B6 (PLP); sự thiếu hụt coenzyme PLP làm giảm hoạt tính sinh tổng hợp ALT trong tế bào gan mạnh hơn nhiều so với AST (ALT nhạy cảm với thiếu B6 hơn)."),
        ("Tổn thương thanh thải AST", "Rượu gây tổn thương tế bào nội mô xoang mạch gan, làm giảm thụ thể thanh thải AST khỏi máu, khiến thời gian bán hủy của AST kéo dài hơn bình thường.")
    ],
    "Kết hợp với nồng độ ALT tuyệt đối hiếm khi vượt quá 300 – 500 U/L do thiếu enzyme dự trữ trong tế bào gan."
))

cards.append(make_card(
    "HS17-B6-06", "B6", "Chuyển hóa Bilirubin trong cơ thể",
    "[CHUYỂN HÓA BILIRUBIN] Từ Thoái Hóa Heme Đến Bài Tiết Qua Màng Vi Quản Mật<br>Trình bày các bước tạo thành Bilirubin gián tiếp tại đại thực bào, vận chuyển trong máu và phản ứng liên hợp tại tế bào gan.",
    [
        ("Thoái hóa Hem tại đại thực bào", "80 – 85% bắt nguồn từ Hemoglobin hồng cầu già; Heme oxygenase mở vòng giải phóng Fe2+, CO và tạo Biliverdin; Biliverdin reductase khử biliverdin thành Bilirubin tự do (gián tiếp)."),
        ("Vận chuyển trong máu", "Bilirubin tự do hoàn toàn không tan trong nước, gắn chặt với Albumin huyết tương để di chuyển đến gan; không lọc qua cầu thận nên không xuất hiện trong nước tiểu."),
        ("Thu nhận và liên hợp tại gan", "Albumin tách ra ở màng xoang mạch; Bilirubin vào bào tương gắn protein Ligandin (Y/Z); tại màng lưới nội chất, enzym UGT1A1 gắn 2 phân tử acid glucuronic tạo Bilirubin Diglucuronide (Bilirubin trực tiếp tan trong nước)."),
        ("Bơm chủ động qua vi quản mật", "Bilirubin liên hợp được bơm chủ động qua màng đỉnh vào vi quản mật nhờ chất vận chuyển phụ thuộc ATP MRP2 (ABCC2); đây là bước giới hạn tốc độ đào thải mật.")
    ],
    "Bilirubin tự do không tan trong nước, nếu nồng độ vượt quá khả năng gắn của albumin có thể ngấm qua hàng rào máu não gây vàng da nhân não (Kernicterus) ở trẻ sơ sinh."
))

cards.append(make_card(
    "HS17-B6-07", "B6", "Chuyển hóa Bilirubin tại ruột",
    "[SỐ PHẬN BILIRUBIN TẠI RUỘT] Urobilinogen, Stercobilin Phân và Urobilin Nước Tiểu<br>Mô tả quá trình biến đổi sinh học của Bilirubin liên hợp tại lòng ruột và nguồn gốc tạo màu sắc của phân và nước tiểu.",
    [
        ("Khử tạo Urobilinogen", "Bilirubin liên hợp đổ vào tá tràng không bị tái hấp thu; xuống hồi tràng và đại tràng bị vi khuẩn khử liên hợp và hydro hóa tạo thành các hợp chất không màu gọi chung là Urobilinogen (và Stercobilinogen)."),
        ("Tạo Stercobilin trong phân", "Phần lớn urobilinogen trong đại tràng bị oxy hóa bởi vi khuẩn tạo thành sắc tố Stercobilin màu vàng nâu, đào thải theo phân (tạo nên màu vàng nâu sinh lý của phân)."),
        ("Tuần hoàn ruột gan và Urobilin nước tiểu", "Khoảng 10 – 15% urobilinogen được tái hấp thu qua tĩnh mạch cửa về gan; phần lớn gan bắt giữ bài tiết lại vào mật; khoảng 1% thoát qua gan đi vào đại tuần hoàn đến thận lọc qua cầu thận, bị oxy hóa thành Urobilin tạo màu vàng rơm sinh lý của nước tiểu.")
    ],
    "Khi tắc mật hoàn toàn, bilirubin không xuống được ruột nên phân mất sắc tố trở nên bạc màu như đất sét trắng, và nước tiểu hoàn toàn mất urobilinogen."
))

cards.append(make_card(
    "HS17-B6-08", "B6", "Chẩn đoán phân biệt Vàng da",
    "[CHẨN ĐOÁN VÀNG DA] So Sánh Vàng Da Trước Gan, Tại Gan và Sau Gan<br>Phân tích biến đổi của Bilirubin máu, Bilirubin niệu, Urobilinogen niệu và màu sắc phân giữa 3 thể vàng da kinh điển.",
    [
        ("Vàng da trước gan (Tan máu)", "Tăng ưu thế Bilirubin GIÁN TIẾP; Bilirubin niệu ÂM TÍNH (do bilirubin gián tiếp không lọc qua cầu thận); Urobilinogen niệu TĂNG RẤT CAO (+++); Phân sẫm màu nâu đậm do tăng tạo stercobilin."),
        ("Vàng da tại gan (Viêm gan, xơ gan)", "Tăng CẢ HAI dạng Bilirubin trực tiếp và gián tiếp; Transaminase AST/ALT tăng cao; Bilirubin niệu DƯƠNG TÍNH (+); Urobilinogen niệu thay đổi (có thể tăng do gan giảm tái bắt giữ hoặc giảm nếu suy bài tiết mật)."),
        ("Vàng da sau gan (Tắc mật cơ học)", "Tăng ưu thế tuyệt đối Bilirubin TRỰC TIẾP; ALP và GGT tăng vọt; Bilirubin niệu DƯƠNG TÍNH ĐẬM (+++, nước tiểu sẫm như nước vối); Urobilinogen niệu ÂM TÍNH HOÀN TOÀN; Phân BẠC MÀU NHƯ ĐẤT SÉT (acholic stool).")
    ],
    "Quy tắc vàng: Thấy Bilirubin niệu dương tính trên que thử nước tiểu chắc chắn khẳng định có tăng Bilirubin TRỰC TIẾP trong máu."
))

cards.append(make_card(
    "HS17-B6-09", "B6", "Hội chứng tăng Bilirubin di truyền",
    "[RỐI LOẠN DI TRUYỀN BILIRUBIN GIÁN TIẾP] Phân Biệt Hội Chứng Gilbert vs Crigler-Najjar<br>So sánh cơ chế phân tử khiếm khuyết enzyme UGT1A1, mức độ tăng bilirubin và tiên lượng lâm sàng giữa Hội chứng Gilbert và Hội chứng Crigler-Najjar Typ I & II.",
    [
        ("Hội chứng Gilbert", "Đột biến promoter thêm cặp base A(TA)7TAA của gen UGT1A1 làm giảm 70 – 80% hoạt tính phiên mã; bilirubin gián tiếp tăng nhẹ (< 3 mg/dL hay < 50 µmol/L) khởi phát khi nhịn đói, mệt mỏi, stress; hoàn toàn lành tính không cần điều trị."),
        ("Crigler-Najjar Typ I", "Đột biến mất hoàn toàn hoạt tính enzyme UGT1A1 (hoạt tính = 0%); bilirubin gián tiếp tăng cực cao (20 – 50 mg/dL hay 350 – 850 µmol/L); tử vong do vàng da nhân não trong giai đoạn sơ sinh nếu không ghép gan khẩn cấp; không đáp ứng với Phenobarbital."),
        ("Crigler-Najjar Typ II (Arias)", "Hoạt tính UGT1A1 còn dưới 10%; bilirubin gián tiếp tăng 6 – 20 mg/dL; hiếm khi gây vàng da nhân não; đáp ứng tốt với Phenobarbital (giảm > 25% bilirubin do cảm ứng lượng enzyme còn lại).")
    ],
    "Nghiệm pháp nhịn đói (Fasting test) làm tăng nồng độ bilirubin gián tiếp gấp 2 – 3 lần giúp chẩn đoán xác định hội chứng Gilbert trên lâm sàng."
))

cards.append(make_card(
    "HS17-B6-10", "B6", "Hội chứng tăng Bilirubin di truyền",
    "[RỐI LOẠN DI TRUYỀN BILIRUBIN TRỰC TIẾP] Phân Biệt Dubin-Johnson vs Hội Chứng Rotor<br>Phân biệt protein vận chuyển bị đột biến, hình thái mô học đại thể gan và bài tiết coproporphyrin giữa Dubin-Johnson và Rotor.",
    [
        ("Hội chứng Dubin-Johnson", "Đột biến gen ABCC2 làm mất hoàn toàn bơm vận chuyển MRP2 trên màng vi quản mật; bilirubin trực tiếp không được bài xuất ứ lại tràn vào máu; ứ đọng sắc tố dạng melanin trong lysosome làm GAN CÓ MÀU ĐEN TUYỀN (Black liver) trên đại thể và sinh thiết."),
        ("Hội chứng Rotor", "Đột biến đồng thời cả hai gen SLCO1B1 và SLCO1B3 làm mất các kênh vận chuyển OATP1B1 và OATP1B3 ở màng xoang mạch; tế bào gan giảm thu nhận và tái bắt giữ bilirubin trực tiếp; NHU MÔ GAN HOÀN TOÀN BÌNH THƯỜNG KHÔNG BỊ ĐEN."),
        ("Điểm chung", "Cả hai đều di truyền lặn trên NST thường, tăng ưu thế Bilirubin trực tiếp, chức năng gan và men gan hoàn toàn bình thường, tiên lượng sống lành tính như người bình thường.")
    ],
    "Dubin-Johnson bài tiết Coproporphyrin typ I trong nước tiểu chiếm > 80%, trong khi ở người bình thường và Rotor thì Coproporphyrin typ III chiếm ưu thế."
))

cards.append(make_card(
    "HS17-B6-11", "B6", "Enzyme Ứ mật Phosphatase Kiềm",
    "[PHOSPHATASE KIỀM] Nguồn Gốc Phân Bố Của ALP và Cơ Chế Tăng Cao Trong Ứ Mật<br>Nêu phản ứng xúc tác của ALP, vị trí định vị trên màng tế bào, các nguồn gốc mô cơ quan ngoài gan và cơ chế giải phóng enzyme khi tắc mật.",
    [
        ("Phản ứng và pH tối ưu", "Thủy phân liên kết ester phosphat hữu cơ giải phóng phosphate vô cơ ở môi trường kiềm tối ưu (pH 9 – 10)."),
        ("Phân bố tế bào và nguồn gốc mô", "Tại gan, ALP định vị ở màng cực vi quản mật của tế bào gan và biểu mô ống mật; các mô ngoài gan giàu ALP: Xương (nguyên bào xương), Nhau thai (phụ nữ mang thai 3 tháng cuối), Niêm mạc ruột non và Thận."),
        ("Cơ chế tăng trong ứ mật", "Khi có tắc nghẽn đường mật, sự ứ đọng acid mật kích thích tăng tổng hợp enzyme ALP; đồng thời muối mật hoạt động như chất tẩy rửa hòa tan neo GPI (glycosylphosphatidylinositol) giải phóng ALP từ màng tế bào vào dòng máu.")
    ],
    "ALP tăng sinh lý ở trẻ em đang tuổi phát triển xương và phụ nữ mang thai quý 3; do đó không được dùng ALP đơn độc để chẩn đoán tắc mật nếu chưa đối chiếu enzym GGT."
))

cards.append(make_card(
    "HS17-B6-12", "B6", "Enzyme Gamma-Glutamyltransferase",
    "[ENZYME GGT] Ý Nghĩa Lâm Sàng và Vai Trò Khẳng Định Nguồn Gốc Của Men ALP<br>Trình bày chức năng sinh hóa của GGT, tính nhạy cảm với rượu/thuốc và thuật toán phối hợp ALP - GGT phân biệt nguồn gốc Gan mật vs Xương.",
    [
        ("Chức năng sinh học", "Xúc tác chuyển nhóm gamma-glutamyl từ glutathion sang acid amin trong chu trình gamma-glutamyl tái hấp thu acid amin qua màng tế bào; định vị tại lưới nội chất tế bào gan và tế bào biểu mô ống mật."),
        ("Cảm ứng bởi rượu và thuốc", "GGT cực kỳ nhạy cảm với rượu; uống rượu kích thích tăng tổng hợp GGT ngay cả khi chưa có tổn thương tế bào gan; các thuốc chống động kinh (Phenytoin, Carbamazepin) cũng gây cảm ứng tăng GGT."),
        ("Quy tắc xác nhận nguồn gốc ALP", "GGT HOÀN TOÀN KHÔNG CÓ TRONG MÔ XƯƠNG: Nếu ALP tăng kèm GGT TĂNG khẳng định chắc chắn tổn thương nguồn gốc Gan Mật; Nếu ALP tăng nhưng GGT HOÀN TOÀN BÌNH THƯỜNG gợi ý chắc chắn nguồn gốc từ Bệnh lý Xương (Paget, còi xương, u xương di căn) hoặc thai kỳ.")
    ],
    "GGT là xét nghiệm nhạy nhất để phát hiện tình trạng lạm dụng rượu mạn tính và là chìa khóa giải mã hiện tượng tăng ALP đơn độc."
))

# ==========================================
# B7: XÉT NGHIỆM CHỨC NĂNG TỔNG HỢP, NGHIỆM PHÁP KOHLER VÀ CA LÂM SÀNG (11 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-B7-01", "B7", "Đánh giá chức năng tổng hợp Albumin",
    "[ĐÁNH GIÁ CHỨC NĂNG TỔNG HỢP] Nồng Độ Albumin Huyết Thanh Trong Bệnh Gan Cấp vs Mạn<br>Giải thích vì sao nồng độ albumin máu bình thường trong suy gan cấp nhưng lại giảm sâu và có giá trị tiên lượng trong xơ gan mạn tính.",
    [
        ("Trị số sinh lý", "Nồng độ albumin huyết thanh bình thường từ 35 – 50 g/L (chiếm 55 – 65% protein toàn phần huyết tương)."),
        ("Suy gan cấp — Albumin bình thường", "Do thời gian bán hủy của albumin rất dài (khoảng 20 ngày), nên trong hoại tử gan cấp tính ồ ạt, lượng albumin đã sản xuất trước đó vẫn lưu hành trong máu; nồng độ albumin máu không kịp sụt giảm."),
        ("Bệnh gan mạn tính — Albumin giảm sâu", "Trong xơ gan, khối nhu mô gan chức năng bị suy giảm kéo dài làm giảm tổng hợp albumin thực sự; nồng độ albumin < 30 g/L phản ánh tổn thương mạn tính tiến triển và là tiêu chuẩn phân độ Child-Pugh."),
        ("Các yếu tố ngoài gan gây giảm albumin", "Cần loại trừ hội chứng thận hư (mất qua nước tiểu), suy dinh dưỡng thiếu đạm (thiếu cơ chất), bỏng diện rộng hoặc bệnh ruột mất đạm.")
    ],
    "Albumin phản ánh chức năng tổng hợp mạn tính của gan; muốn đánh giá chức năng tổng hợp cấp tính bắt buộc phải dựa vào các xét nghiệm đông máu."
))

cards.append(make_card(
    "HS17-B7-02", "B7", "Đánh giá chức năng tổng hợp PT/INR",
    "[ĐÁNH GIÁ ĐÔNG MÁU] Thời Gian Prothrombin (PT) / INR và Vai Trò Của Yếu Tố VII<br>Giải thích vì sao Thời gian Prothrombin (PT) và chỉ số INR lại là xét nghiệm nhạy nhất và sớm nhất phản ánh suy giảm chức năng gan cấp tính.",
    [
        ("Phản ánh con đường đông máu ngoại sinh", "PT và INR phản ánh con đường đông máu ngoại sinh và con đường chung, phụ thuộc nồng độ các yếu tố: I, II, V, VII và X (toàn bộ đều do gan tổng hợp)."),
        ("Thời gian bán hủy cực ngắn của Yếu tố VII", "Yếu tố VII có thời gian bán hủy ngắn nhất trong tất cả các yếu tố đông máu (chỉ từ 4 – 6 giờ); Yếu tố V bán hủy khoảng 12 – 24 giờ."),
        ("Ý nghĩa báo động sớm suy gan cấp", "Khi tế bào gan bị hoại tử ngừng tổng hợp, nồng độ Yếu tố VII sụt giảm gần như ngay lập tức, làm PT kéo dài và INR tăng vọt chỉ sau vài giờ đến 1 ngày; là tiêu chuẩn vàng định nghĩa Suy gan cấp (ALF) và tiên lượng sống còn.")
    ],
    "Yếu tố V không phụ thuộc Vitamin K; định lượng Yếu tố V giúp đánh giá chính xác chức năng gan độc lập với tình trạng thiếu hụt Vitamin K."
))

cards.append(make_card(
    "HS17-B7-03", "B7", "Nghiệm pháp Kohler",
    "[NGHIỆM PHÁP KOHLER] Phân Biệt PT Kéo Dài Do Suy Tế Bào Gan vs Tắc Mật Kéo Dài<br>Trình bày mục đích, nguyên lý sinh hóa, cách tiến hành và tiêu chuẩn biện luận kết quả của Nghiệm pháp Kohler (Test Kohler).",
    [
        ("Mục đích lâm sàng", "Phân biệt nguyên nhân gây kéo dài thời gian Prothrombin (INR > 1.5): Do tế bào gan suy hoại tử không tổng hợp được yếu tố đông máu, hay do Tắc mật làm giảm muối mật dẫn đến không hấp thu được Vitamin K tan trong dầu tại ruột."),
        ("Cách tiến hành", "Tiêm bắp (hoặc tiêm dưới da) Vitamin K1 liều 10 mg/ngày trong 3 ngày liên tiếp; sau đó xét nghiệm lại PT/INR."),
        ("Kohler Dương tính (Tắc mật)", "PT rút ngắn rõ rệt hoặc INR trở về bình thường: Do tế bào gan còn nguyên vẹn, khi được cung cấp đủ Vitamin K qua đường tiêm gan lập tức tổng hợp đủ các yếu tố 1972."),
        ("Kohler Âm tính (Suy tế bào gan)", "PT và INR không thay đổi hoặc cải thiện không đáng kể: Do nhu mô tế bào gan đã bị suy thoái nặng nề, mất khả năng tổng hợp protein dù cơ chất vitamin K thừa thãi; tiên lượng rất nặng.")
    ],
    "Đây là nghiệm pháp sinh hóa kinh điển kết hợp giữa lý thuyết hấp thu lipid và chức năng sinh tổng hợp protein của gan."
))

cards.append(make_card(
    "HS17-B7-04", "B7", "Điện di Protein huyết thanh",
    "[ĐIỆN DI PROTEIN GAN] Hiện Tượng Cầu Beta-Gamma (Beta-Gamma Bridging) Trong Xơ Gan<br>Mô tả biến đổi biểu đồ điện di protein huyết thanh ở bệnh nhân xơ gan và cơ chế tạo thành hiện tượng Cầu Beta-Gamma.",
    [
        ("Biến đổi chung biểu đồ điện di", "Dải Albumin sụt giảm rõ rệt (giảm tổng hợp); dải alpha-1 và alpha-2 globulin giảm nhẹ; dải gamma-globulin tăng cao tạo thành đỉnh rộng đa dòng (polyclonal)."),
        ("Hiện tượng Cầu Beta-Gamma", "Dải beta-globulin và gamma-globulin hòa lẫn vào nhau không còn ranh giới phân tách rõ ràng trên biểu đồ điện di."),
        ("Cơ chế sinh hóa giải thích", "Trong xơ gan, suy giảm chức năng đại thực bào Kupffer và shunt cửa-chủ làm kháng nguyên vi khuẩn đường ruột tràn vào đại tuần hoàn; kích thích hệ tương bào tủy xương tăng sản xuất ồ ạt kháng thể IgA; phân tử IgA có độ di động điện di nằm vắt ngang giữa vùng beta và gamma tạo nên hình ảnh cầu nối.")
    ],
    "Cầu beta-gamma là hình ảnh kinh điển gợi ý chẩn đoán Xơ gan tiến triển trên điện di protein huyết thanh mao quản."
))

cards.append(make_card(
    "HS17-B7-05", "B7", "Xét nghiệm Amoniac máu",
    "[XÉT NGHIỆM NH3 MÁU] Quy Trình Lấy Máu Chuẩn Xác và Ý Nghĩa Trong Hôn Mê Gan<br>Nêu nồng độ tham chiếu của Amoniac máu và các yêu cầu kỹ thuật nghiêm ngặt khi lấy mẫu bệnh phẩm xét nghiệm NH3 để tránh sai số.",
    [
        ("Giá trị tham chiếu sinh lý", "Nồng độ NH3 huyết tương bình thường từ 11 – 35 µmol/L (18 – 60 µg/dL)."),
        ("Kỹ thuật lấy máu nghiêm ngặt", "1) Lấy máu tĩnh mạch KHÔNG ĐƯỢC BUỘC GARO quá chặt hoặc co bóp bàn tay (tránh phóng thích NH3 từ cơ); 2) Chống đông bằng Heparin hoặc EDTA; 3) ĐẶT ỐNG MÁU VÀO XÔ NƯỚC ĐÁ NGAY LẬP TỨC; 4) Ly tâm tách huyết tương và phân tích trong vòng 15 – 30 phút."),
        ("Nguyên nhân sai số dương tính giả", "Nếu để mẫu máu ở nhiệt độ phòng, enzyme gamma-glutamyltransferase và deaminase trong hồng cầu sẽ tiếp tục thủy phân acid amin giải phóng amoniac tự do làm kết quả tăng vọt giả tạo.")
    ],
    "Nồng độ NH3 tăng cao tương quan với mức độ phù não và nguy cơ thoát vị não ở bệnh nhân suy gan cấp."
))

cards.append(make_card(
    "HS17-B7-06", "B7", "Ca lâm sàng Viêm gan virus cấp",
    "[CA LÂM SÀNG 1] Viêm Gan Virus Cấp Tính Bùng Phát<br>Bệnh nhân nam 26 tuổi, mệt mỏi, chán ăn, vàng mắt vàng da rõ; Xét nghiệm: ALT 2800 U/L, AST 1950 U/L, Bilirubin TP 135 µmol/L (trực tiếp chiếm 65%), INR 1.12. Biện luận cơ chế sinh hóa.",
    [
        ("Đặc điểm tổn thương hủy hoại tế bào gan", "Transaminase tăng cực cao (> 50 lần ULN) phản ánh tình trạng hoại tử tế bào gan ồ ạt do đáp ứng miễn dịch tế bào tiêu diệt tế bào gan nhiễm virus."),
        ("Tỷ số De Ritis < 1", "ALT (1950/2800 = 0.70 < 1) tăng cao hơn AST do tổn thương chủ yếu ở bào tương tế bào gan và thời gian bán hủy của ALT dài hơn."),
        ("Vàng da hỗn hợp và Chức năng tổng hợp", "Bilirubin tăng cả trực tiếp và gián tiếp do tế bào gan vừa giảm thu nhận/liên hợp vừa tổn thương vi quản mật rò rỉ sắc tố vào máu; INR 1.12 bình thường chứng tỏ chức năng tổng hợp protein đông máu của gan còn được bảo tồn tốt.")
    ],
    "Chẩn đoán phù hợp: Viêm gan virus cấp (A hoặc B); chưa có dấu hiệu suy gan cấp vì INR < 1.5 và không có bệnh não gan."
))

cards.append(make_card(
    "HS17-B7-07", "B7", "Ca lâm sàng Viêm gan do Rượu",
    "[CA LÂM SÀNG 2] Viêm Gan Do Rượu Tiến Triển Trên Bệnh Nhân Nghiện Rượu<br>Bệnh nhân nam 48 tuổi uống rượu 20 năm; Xét nghiệm: AST 320 U/L, ALT 120 U/L, GGT 950 U/L, Bilirubin TP 82 µmol/L, MCV 106 fL. Phân tích các chỉ số sinh hóa đặc trưng.",
    [
        ("Tỷ số De Ritis AST/ALT > 2", "AST/ALT = 320/120 = 2.67 (> 2); kết hợp với hoạt độ ALT tuyệt đối < 300 U/L là dấu ấn đặc trưng của tổn thương tế bào gan do rượu."),
        ("Cơ chế giải thích", "Rượu gây độc ty thể giải phóng AST ty thể, đồng thời suy dinh dưỡng gây thiếu hụt Vitamin B6 (PLP) làm giảm biểu hiện enzyme ALT bào tương."),
        ("Các chỉ dấu phối hợp", "GGT tăng rất cao (950 U/L) do cảm ứng enzyme bởi ethanol; MCV tăng cao (106 fL) phản ánh độc tính trực tiếp của rượu lên tủy xương và thiếu folate.")
    ],
    "Sự kết hợp: AST/ALT > 2, ALT < 300 U/L và GGT tăng vọt giúp chẩn đoán xác định viêm gan do rượu với độ đặc hiệu trên 90%."
))

cards.append(make_card(
    "HS17-B7-08", "B7", "Ca lâm sàng Vàng da Tắc mật U đầu tụy",
    "[CA LÂM SÀNG 3] Vàng Da Tắc Mật Sau Gan Hoàn Toàn Do U Đầu Tụy<br>Bệnh nhân nữ 64 tuổi, vàng da vàng mắt đậm không đau, ngứa dữ dội, nước tiểu sẫm như nước vối, phân bạc màu như phân cò; Xét nghiệm: Bilirubin TP 310 µmol/L, Bilirubin TT 245 µmol/L, ALP 720 U/L, GGT 510 U/L, AST 65 U/L, ALT 58 U/L. Biện luận kết quả.",
    [
        ("Hội chứng ứ mật sau gan hoàn toàn", "Bilirubin trực tiếp chiếm ưu thế tuyệt đối (245/310 = 79%); enzyme ứ mật ALP và GGT tăng rất cao (gấp 5 – 6 lần ULN); trong khi transaminase tế bào gan chỉ tăng nhẹ phản ứng."),
        ("Nước tiểu sẫm màu và Bilirubin niệu", "Bilirubin trực tiếp tan trong nước tràn vào máu lọc qua cầu thận làm Bilirubin niệu (+++); tắc mật hoàn toàn làm không có bilirubin xuống ruột, do đó Urobilinogen niệu âm tính tuyệt đối."),
        ("Phân bạc màu và ngứa da", "Lòng ruột hoàn toàn thiếu vắng sắc tố mật nên phân mất màu trở nên trắng bợt như đất sét; muối mật ứ đọng tràn vào máu lắng đọng kích thích đầu tận thần kinh cảm giác dưới da gây ngứa dữ dội.")
    ],
    "Đây là bệnh cảnh kinh điển của tắc mật cơ học ngoài gan; cần chỉ định siêu âm và chụp cắt lớp vi tính (CT/MRI) khảo sát đường mật khẩn cấp."
))

cards.append(make_card(
    "HS17-B7-09", "B7", "Ca lâm sàng Hội chứng Gilbert",
    "[CA LÂM SÀNG 4] Vàng Da Tăng Bilirubin Gián Tiếp Lành Tính Hội Chứng Gilbert<br>Nam sinh viên 21 tuổi sau khi thức đêm ôn thi thấy hơi vàng nhẹ củng mạc mắt; Xét nghiệm: Bilirubin TP 45 µmol/L, Bilirubin TT 6 µmol/L (gián tiếp 39 µmol/L, chiếm 87%), AST 24 U/L, ALT 22 U/L, ALP 65 U/L, Hb 145 g/L, Hồng cầu lưới bình thường. Biện luận chẩn đoán.",
    [
        ("Tăng Bilirubin gián tiếp đơn độc", "Bilirubin toàn phần tăng nhẹ (< 50 µmol/L), trong đó dạng gián tiếp chiếm ưu thế tuyệt đối (> 85%); không có tổn thương tế bào gan (AST, ALT bình thường) và không có ứ mật (ALP, GGT bình thường)."),
        ("Loại trừ nguyên nhân tan máu", "Nồng độ Hemoglobin bình thường, số lượng hồng cầu lưới bình thường, không có thiếu máu chứng tỏ không có hiện tượng tan máu tăng hủy hồng cầu."),
        ("Kết luận Hội chứng Gilbert", "Khởi phát sau stress/thức đêm/nhịn đói ở người trẻ tuổi; do giảm hoạt tính promoter UGT1A1; đây là biến thể di truyền lành tính, giải thích cho bệnh nhân yên tâm, hoàn toàn không cần dùng thuốc điều trị.")
    ],
    "Không bao giờ được nhầm lẫn hội chứng Gilbert với viêm gan mạn tính để tránh các chỉ định can thiệp xâm lấn không cần thiết."
))

cards.append(make_card(
    "HS17-B7-10", "B7", "Ca lâm sàng Ngộ độc Paracetamol",
    "[CA LÂM SÀNG 5] Suy Gan Cấp Do Ngộ Độc Quá Liều Paracetamol<br>Nữ 19 tuổi uống 35 viên paracetamol (17.5 g) để tự tử; 48 giờ sau vào viện lơ mơ, vàng da; Xét nghiệm: ALT 6500 U/L, AST 7200 U/L, INR 3.8, Bilirubin TP 95 µmol/L, Khí máu pH 7.24, Lactat máu 6.5 mmol/L. Biện luận mức độ nguy kịch.",
    [
        ("Hoại tử tế bào gan tối cấp", "Transaminase tăng cực cao hàng nghìn U/L do NAPQI cạn kiệt Glutathion gây hoại tử ồ ạt tế bào gan Vùng 3."),
        ("Tam chứng Suy gan cấp (ALF)", "Tổn thương gan nặng + Rối loạn đông máu nặng (INR 3.8 > 1.5) + Rối loạn tri giác (bệnh não gan) trên bệnh nhân không có xơ gan trước đó."),
        ("Tiêu chuẩn tiên lượng King's College Criteria", "Nhiễm toan chuyển hóa lactic nặng (pH 7.24 < 7.30 sau hồi sức dịch) kèm INR > 3.8 và suy tạng; bệnh nhân đạt tiêu chuẩn chỉ định GHÉP GAN CẤP CỨU KHẨN CẤP; truyền NAC tĩnh mạch liều cao lập tức.")
    ],
    "Toan máu lactic (pH < 7.30) sau 24 giờ là tiêu chuẩn tiên lượng tử vong độc lập mạnh nhất trong ngộ độc Paracetamol nếu không được ghép gan."
))

cards.append(make_card(
    "HS17-B7-11", "B7", "Ca lâm sàng Nghiệm pháp Kohler",
    "[CA LÂM SÀNG 6] Ứng Dụng Nghiệm Pháp Kohler Biện Luận Hai Ca Bệnh Kéo Dài PT<br>So sánh kết quả nghiệm pháp Kohler giữa Ca A (vàng da do sỏi kẹt ống mật chủ, INR ban đầu 2.2) và Ca B (vàng da trên nền xơ gan mất bù, INR ban đầu 2.3).",
    [
        ("Quy trình thực hiện", "Cả 2 bệnh nhân đều được tiêm bắp Vitamin K1 liều 10 mg/ngày trong 3 ngày liên tiếp."),
        ("Kết quả Ca A (Sỏi mật — Kohler Dương tính)", "Sau 3 ngày tiêm Vitamin K1, xét nghiệm lại INR rút ngắn từ 2.2 về 1.15 (bình thường); kết luận tế bào gan còn tốt, rối loạn đông máu thuần túy do tắc mật cản trở hấp thu vitamin K tại ruột."),
        ("Kết quả Ca B (Xơ gan — Kohler Âm tính)", "Sau 3 ngày tiêm Vitamin K1, xét nghiệm lại INR vẫn kéo dài ở mức 2.1; kết luận nhu mô gan xơ hóa mất bù nặng nề không còn tế bào gan chức năng để sản xuất yếu tố đông máu dù đã cung cấp thừa vitamin K; tiên lượng bệnh gan giai đoạn cuối.")
    ],
    "Nghiệm pháp Kohler cung cấp bằng chứng động học sinh hóa vững chắc giúp bác sĩ ngoại khoa tự tin phẫu thuật cho ca A và cảnh báo nguy cơ chảy máu tử vong cho ca B."
))

# ==========================================
# B_ALGO: 5 THUẬT TOÁN QUYẾT ĐỊNH LÂM SÀNG (5 THẺ)
# ==========================================

cards.append(make_card(
    "HS17-ALGO-01", "B_ALGO", "Thuật toán chẩn đoán vàng da",
    "[⚡ THUẬT TOÁN QUYẾT ĐỊNH] Quy Trình Tiếp Cận Chẩn Đoán Phân Tầng Vàng Da<br>Trình bày 4 bước chuẩn mực trong lưu đồ thuật toán tiếp cận chẩn đoán phân tầng nguyên nhân Vàng da (Jaundice Workup) tại giường bệnh.",
    [
        ("Bước 1 — Định lượng Bilirubin và Xác định thể ưu thế", "Xét nghiệm Bilirubin toàn phần, trực tiếp, gián tiếp; Nếu Bilirubin gián tiếp > 80% Bilirubin TP chuyển sang Nhánh Vàng da gián tiếp; Nếu Bilirubin trực tiếp > 50% chuyển sang Nhánh Vàng da trực tiếp."),
        ("Bước 2 — Phân tầng Nhánh Bilirubin Gián tiếp", "Kiểm tra dấu hiệu Tan máu (Công thức máu Hb, Hồng cầu lưới, Haptoglobin, Test Coombs, LDH); Nếu có tan máu → Tan máu tự miễn, thiếu G6PD, Thalassemia; Nếu không tan máu → Đánh giá Hội chứng Gilbert (tăng nhẹ khi đói/stress) hoặc Crigler-Najjar."),
        ("Bước 3 — Khảo sát hình ảnh đầu tay Nhánh Bilirubin Trực tiếp", "Chỉ định SIÊU ÂM BỤNG KHẢO SÁT HỆ THỐNG ĐƯỜNG MẬT: Phân định đường mật dãn (Tắc mật ngoài gan / Ngoại khoa) vs đường mật không dãn (Bệnh lý tại gan / Nội khoa)."),
        ("Bước 4 — Tiếp cận theo hình thái đường mật", "Đường mật dãn → Chụp MRCP hoặc CT/ERCP tìm nguyên nhân sỏi mật, u đầu tụy, u đường mật (Klatskin); Đường mật không dãn → Khảo sát bộ xét nghiệm Transaminase, Kháng thể tự miễn (ANA, ASMA, AMA), Huyết thanh virus (HBsAg, Anti-HCV) tìm viêm gan, xơ gan, viêm đường mật nguyên phát.")
    ],
    "Lưu đồ thuật toán giúp người thầy thuốc không bao giờ bỏ sót chỉ định ngoại khoa cấp cứu (viêm đường mật cấp do sỏi kẹt) và tránh các phẫu thuật nhầm lẫn cho bệnh nhân vàng da nội khoa.",
    is_algo=True
))

cards.append(make_card(
    "HS17-ALGO-02", "B_ALGO", "Thuật toán tăng men gan",
    "[⚡ THUẬT TOÁN QUYẾT ĐỊNH] Thuật Toán Phân Tích Tổn Thương Tế Bào Gan Qua Men Gan<br>Trình bày lưu đồ thuật toán 3 bước tiếp cận bệnh nhân có tăng men gan transaminase (AST, ALT).",
    [
        ("Bước 1 — Phân tầng theo Biên độ hoạt độ Men Gan", "Chia 3 mức độ: 1) Tăng nhẹ đến vừa (< 5 lần ULN < 250 U/L); 2) Tăng vừa (5 – 15 lần ULN 250 – 1000 U/L); 3) Tăng rất cao (> 15 – 20 lần ULN > 1000 U/L)."),
        ("Bước 2 — Xử trí Nhóm Tăng Men Gan Rất Cao (> 1000 U/L)", "Tầm soát ngay 3 nguyên nhân cấp cứu tối khẩn cấp: 1) Thiếu máu cục bộ tụt HA / Sốc gan (Shock liver - AST/ALT tăng vọt hàng nghìn, LDH tăng rất cao, tỷ số ALT/LDH < 1.5); 2) Nhiễm độc gan cấp (Paracetamol, nấm độc Amanita); 3) Viêm gan virus cấp (A, B, E - ALT thường cao hơn AST)."),
        ("Bước 3 — Đánh giá Tỷ số De Ritis (AST/ALT) ở nhóm tăng nhẹ và vừa", "Nếu AST/ALT > 2 (đặc biệt AST < 300 U/L, GGT tăng vọt, MCV tăng) → Định hướng Viêm gan do rượu; Nếu AST/ALT < 1 → Đánh giá Viêm gan virus mạn B/C, Gan nhiễm mỡ không do rượu (NAFLD/NASH); Nếu bệnh gan mạn có AST/ALT chuyển từ < 1 sang > 1 → Tầm soát Xơ gan tiến triển.")
    ],
    "Thuật toán kết hợp giữa biên độ tuyệt đối và tỷ số tương đối giúp khoanh vùng chính xác nguyên nhân gây hủy hoại tế bào gan trong vòng vài phút tiếp cận xét nghiệm.",
    is_algo=True
))

cards.append(make_card(
    "HS17-ALGO-03", "B_ALGO", "Thuật toán phân tầng ALP và GGT",
    "[⚡ THUẬT TOÁN QUYẾT ĐỊNH] Thuật Toán Phân Tầng Men Ứ Mật (ALP & GGT)<br>Trình bày lưu đồ thuật toán 3 bước tiếp cận và định hướng nguyên nhân khi bệnh nhân có tăng men Phosphatase Kiềm (ALP).",
    [
        ("Bước 1 — Xác nhận nguồn gốc enzyme qua GGT", "Khi phát hiện ALP huyết thanh tăng cao đơn độc, bước kế tiếp bắt buộc là định lượng men GGT; Nếu GGT bình thường → Khẳng định nguồn gốc từ XƯƠNG (Paget, u xương, gãy xương, còi xương) hoặc Nhau thai; Nếu GGT tăng song hành → Khẳng định 100% nguồn gốc Gan Mật."),
        ("Bước 2 — Siêu âm bụng khảo sát Giãn Đường Mật", "Phân định Ứ mật ngoài gan vs Ứ mật trong gan: Nếu đường mật dãn → Ứ mật ngoài gan cơ học (chỉ định MRCP hoặc ERCP can thiệp lấy sỏi, đặt stent giải áp u); Nếu đường mật không dãn → Ứ mật trong gan vi thể."),
        ("Bước 3 — Tầm soát nguyên nhân ứ mật trong gan", "Xét nghiệm Kháng thể kháng ty thể Anti-Mitochondrial Antibody (AMA) tìm Viêm đường mật nguyên phát (PBC); Rà soát toàn bộ tiền sử dùng thuốc gây ứ mật (Amoxicillin-clavulanate, kháng sinh macrolid, steroid đồng hóa); Tầm soát bệnh lý thâm nhiễm gan (U hạt Sarcoidosis, Amyloidosis, ung thư di căn gan).")
    ],
    "Phối hợp ALP và GGT là nguyên tắc bắt buộc để tránh chẩn đoán nhầm bệnh nhân gãy xương hoặc loãng xương thành bệnh nhân tắc mật.",
    is_algo=True
))

cards.append(make_card(
    "HS17-ALGO-04", "B_ALGO", "Thuật toán Suy gan cấp",
    "[⚡ THUẬT TOÁN QUYẾT ĐỊNH] Lưu Đồ Tiếp Cận và Xử Trí Suy Gan Cấp (ALF)<br>Trình bày các bước nhận diện tam chứng suy gan cấp và áp dụng Tiêu chuẩn King's College đánh giá chỉ định Ghép gan cấp cứu.",
    [
        ("Bước 1 — Nhận diện Tam chứng Định nghĩa Suy gan cấp", "Khẳng định cả 3 tiêu chí: 1) Tổn thương gan cấp (transaminase tăng cao); 2) Rối loạn đông máu nặng (INR > 1.5 hoặc PT kéo dài); 3) Bệnh não gan ở bất kỳ mức độ nào; trên bệnh nhân KHÔNG CÓ tiền sử bệnh gan mạn tính/xơ gan trước đó, thời gian khởi phát < 26 tuần."),
        ("Bước 2 — Phân tầng nguyên nhân và Khởi động Hồi sức tích cực", "Xác định căn nguyên ngộ độc Paracetamol vs Không do Paracetamol; Truyền ngay thuốc giải độc N-acetylcysteine (NAC); Chống phù não (nằm đầu cao 30 độ, thở máy kiểm soát PaCO2 35 mmHg, truyền Mannitol hoặc muối ưu trương 3% nếu tăng áp lực nội sọ)."),
        ("Bước 3 — Đánh giá Tiêu chuẩn Tiên lượng King's College Criteria", "Nhóm do Paracetamol: Chỉ định ghép gan khi pH máu động mạch < 7.30 sau bù dịch, HOẶC đồng thời có cả 3 tiêu chí: INR > 6.5, Creatinine máu > 300 µmol/L và Bệnh não gan độ III/IV; Nhóm không do Paracetamol: Chỉ định ghép gan khi INR > 6.5, HOẶC có bất kỳ 3 trong 5 tiêu chí: Tuổi < 10 hoặc > 40, Nguyên nhân vô căn/do thuốc, Thời gian từ vàng da đến hôn mê > 7 ngày, INR > 3.5, Bilirubin TP > 300 µmol/L.")
    ],
    "Tiêu chuẩn King's College Criteria là thước đo sinh hóa quyết định ranh giới sinh tử giữa việc tiếp tục điều trị nội khoa hay chuyển mổ ghép gan cấp cứu khẩn cấp.",
    is_algo=True
))

cards.append(make_card(
    "HS17-ALGO-05", "B_ALGO", "Thuật toán Nghiệm pháp Kohler",
    "[⚡ THUẬT TOÁN QUYẾT ĐỊNH] Lưu Đồ Nghiệm Pháp Kohler Phân Biệt Rối Loạn Đông Máu Do Gan<br>Trình bày lưu đồ thuật toán 3 bước thực hiện và ra quyết định lâm sàng từ kết quả Nghiệm pháp Kohler trên bệnh nhân có PT kéo dài.",
    [
        ("Bước 1 — Chỉ định và Đánh giá ban đầu", "Chỉ định trên bệnh nhân có Thời gian Prothrombin kéo dài (INR > 1.5) kèm theo hội chứng vàng da hoặc nghi ngờ bệnh lý gan mật; ghi nhận trị số INR nền trước can thiệp."),
        ("Bước 2 — Quy trình tiêm Vitamin K1 chuẩn hóa", "Tiêm bắp (hoặc tiêm dưới da nếu nguy cơ tụ máu cao) Vitamin K1 (Phytomenadione) liều 10 mg một lần mỗi ngày, thực hiện liên tục trong 3 ngày; xét nghiệm lại PT và INR sau 24 giờ kể từ mũi tiêm cuối cùng."),
        ("Bước 3 — Phân định 2 nhánh quyết định lâm sàng", "Nhánh 1 (Kohler Dương tính): INR rút ngắn về bình thường (hoặc PT tăng > 30 – 50% so với trước tiêm) → Kết luận chức năng tổng hợp của tế bào gan còn tốt, rối loạn đông máu do Tắc mật kém hấp thu Vitamin K → Tiếp tục bổ sung Vitamin K và tiến hành can thiệp giải áp đường mật an toàn; Nhánh 2 (Kohler Âm tính): INR không đổi hoặc cải thiện không đáng kể → Kết luận Suy hoại tử tế bào gan nặng (suy gan mất bù) → Báo động nguy cơ chảy máu, hội chẩn hồi sức và cân nhắc chỉ định truyền huyết tương tươi đông lạnh khi có can thiệp xâm lấn.")
    ],
    "Nghiệm pháp Kohler là cầu nối biện chứng giữa hóa sinh học hấp thu vitamin tan trong dầu và năng lực sinh tổng hợp protein của tế bào gan.",
    is_algo=True
))

# ==========================================
# GHI VÀO FILE CARDS.V2.JSON
# ==========================================

output_data = {
    "deck_id": DECK_ID,
    "deck_name": DECK_NAME,
    "card_count": len(cards),
    "cards": cards
}

OUTPUT_PATH.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Tong so the moi: {len(cards)} the")
print(f"Da ghi thanh cong vao {OUTPUT_PATH}")
