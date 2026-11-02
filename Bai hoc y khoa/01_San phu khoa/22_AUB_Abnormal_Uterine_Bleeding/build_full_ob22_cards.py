# -*- coding: utf-8 -*-
"""Script nâng cấp và mở rộng toàn diện bộ thẻ Anki cho bài OB-22 AUB (B0 đến B15)."""
import json
from pathlib import Path

cards_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/01_San phu khoa/22_AUB_Abnormal_Uterine_Bleeding/AUB_Abnormal_Uterine_Bleeding_2026-06-29.cards.v2.json")
existing_data = json.loads(cards_path.read_text(encoding="utf-8"))
old_cards = existing_data.get("cards", existing_data)

# Danh sách 49 thẻ cũ đã sửa lỗi
fixed_old_cards = []
for c in old_cards[:49]:
    card = dict(c)
    if "back" in card:
        card["back"] = card["back"].replace("$\\rightarrow$", "→").replace("\\rightarrow", "→").replace("$", "")
    if "front" in card:
        card["front"] = card["front"].replace("$\\rightarrow$", "→").replace("\\rightarrow", "→").replace("$", "")
    
    if card["id"] == "OB22-B0-06":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tầng đặc bề mặt:</b> Tầng đặc (<span style=\"color:#74c0fc\"><b>Stratum compactum</b></span>) nằm nông sát lòng buồng tử cung, chứa các cổ tuyến hẹp và tế bào đệm biến đổi màng rụng hóa dày đặc.<br>2) <b>Tầng xốp đệm:</b> Tầng xốp (<span style=\"color:#51cf66\"><b>Stratum spongiosum</b></span>) nằm sâu hơn ở giữa, chứa thân tuyến ngoằn ngoèo giãn rộng với các động mạch xoắn cuộn khúc dồi dào.<br><br><b>💡 Giải thích của AI:</b><br>Khi Progesterone tụt giảm, toàn bộ tầng đặc và tầng xốp cùng bong tróc ra ngoài tạo dòng kinh nguyệt, chừa lại tầng đáy Basalis nguyên vẹn."
    elif card["id"] == "OB22-B1-03":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chất co mạch PGF2α:</b> <span style=\"color:#51cf66\"><b>PGF2α</b></span> gắn vào thụ thể FP trên cơ trơn mạch máu gây co thắt động mạch xoắn và kích thích cơn co tử cung tống xuất máu kinh.<br>2) <b>Chất giãn mạch PGE2:</b> <span style=\"color:#ff6b6b\"><b>PGE2 và Prostacyclin (PGI2)</b></span> gắn vào thụ thể IP/EP gây giãn mạch và ức chế ngưng tập tiểu cầu; ở phụ nữ HMB, tỷ lệ PGF2α/PGE2 bị sụt giảm nghiêm trọng làm chảy máu ồ ạt.<br><br><b>💡 Giải thích của AI:</b><br>Thuốc NSAIDs (Axit Mefenamic) ức chế enzyme COX làm giảm tổng hợp PGE2 và PGI2, khôi phục lại ưu thế co mạch của PGF2α giúp giảm 30-40% lượng máu kinh."
    elif card["id"] == "OB22-B2-03":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thuật ngữ DUB:</b> Thuật ngữ <span style=\"color:#ff6b6b\"><b>DUB (Dysfunctional Uterine Bleeding)</b></span> trước đây dùng vô tội vạ cho mọi ca chảy máu không u cục, làm lu mờ ranh giới giữa rối loạn rụng trứng (AUB-O) và tổn thương nội mạc tại chỗ (AUB-E).<br>2) <b>Thuật ngữ Menorrhagia:</b> Thuật ngữ <span style=\"color:#ff6b6b\"><b>Menorrhagia</b></span> (rong kinh) gây nhầm lẫn trên lâm sàng và không có định nghĩa định lượng rõ ràng; được thay thế chuẩn xác bằng <span style=\"color:#74c0fc\"><b>HMB (Heavy Menstrual Bleeding) và IMB</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Việc sử dụng thuật ngữ chuẩn hóa FIGO giúp các nghiên cứu thử nghiệm lâm sàng và giao tiếp chuyên môn đạt tính chính xác quốc tế."
    elif card["id"] == "OB22-B4-03":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Type 1 số lượng:</b> Type 1 chiếm <span style=\"color:#ffd43b\"><b>70–80%</b></span>, là sự thiếu hụt một phần số lượng yếu tố vWF, triệu chứng chảy máu nhẹ đến vừa, đáp ứng rất tốt với Desmopressin (DDAVP).<br>2) <b>Type 2 chất lượng:</b> Type 2 chiếm <span style=\"color:#74c0fc\"><b>15–20%</b></span>, là sự rối loạn cấu trúc chức năng của phân tử vWF (dù số lượng có thể bình thường), chia thành các phân nhóm 2A, 2B, 2M, 2N.<br><br><b>💡 Giải thích của AI:</b><br>Type 3 là thể đồng hợp tử lặn hiếm gặp gây thiếu hụt hoàn toàn vWF và Yếu tố VIII dẫn đến xuất huyết cực kỳ trầm trọng giống như Hemophilia."
    elif card["id"] == "OB22-B4-04":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế nội tiết:</b> Không rụng trứng → không có hoàng thể và thiếu Progesterone; Estrogen kích thích nội mạc tăng sinh liên tục vượt quá khả năng cấp máu gây <span style=\"color:#ff6b6b\"><b>hoại tử bong tróc rải rác</b></span>.<br>2) <b>Nguyên nhân lâm sàng:</b> Hội chứng buồng trứng đa nang (<span style=\"color:#ff6b6b\"><b>PCOS</b></span>), trục HPO chưa trưởng thành ở tuổi dậy thì, suy giảm buồng trứng tiền mãn kinh, bệnh suy giáp, và tăng prolactin máu.<br><br><b>💡 Giải thích của AI:</b><br>AUB-O chiếm hơn 70% các ca xuất huyết tử cung bất thường ở lứa tuổi vị thành niên và tiền mãn kinh."
    elif card["id"] == "OB22-B4-05":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Khiếm khuyết phân tử:</b> Thiếu hụt chất co mạch <span style=\"color:#ff6b6b\"><b>Endothelin-1 và PGF2α</b></span> tại chỗ, đồng thời tăng tiết quá mức chất giãn mạch Prostacyclin và chất tiêu sợi huyết tPA.<br>2) <b>Tiêu chuẩn chẩn đoán:</b> AUB-E là một chẩn đoán loại trừ, được xác định ở phụ nữ có chu kỳ rụng trứng đều đặn nhưng kinh nhiều HMB, sau khi đã loại trừ hoàn toàn các tổn thương <span style=\"color:#74c0fc\"><b>PALM</b></span> và rối loạn đông máu <span style=\"color:#74c0fc\"><b>C</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Điều trị tối ưu cho AUB-E là ức chế tiêu sợi huyết bằng Tranexamic acid hoặc làm teo niêm mạc bằng vòng LNG-IUS."
    elif card["id"] == "OB22-B4-06":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thuốc chống đông:</b> Thuốc chống đông <span style=\"color:#ff6b6b\"><b>Warfarin và DOACs (Rivaroxaban, Apixaban)</b></span> làm nặng nề thêm lượng máu kinh ở 20–30% phụ nữ, đặc biệt khi INR vượt ngưỡng mục tiêu 2.0 – 3.0.<br>2) <b>Dụng cụ tử cung:</b> <span style=\"color:#74c0fc\"><b>Vòng tránh thai chứa đồng (Copper-IUD)</b></span> kích hoạt phản ứng viêm vô khuẩn và tăng tiêu sợi huyết tại khoang nội mạc gây tăng 50% lượng máu kinh trong 3-6 tháng đầu.<br><br><b>💡 Giải thích của AI:</b><br>Nếu bệnh nhân dùng vòng đồng bị HMB nặng, giải pháp thay thế hoàn hảo là đổi sang vòng nội tiết LNG-IUS (Mirena)."
    elif card["id"] == "OB22-B5-06":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Xét nghiệm TSH đầu tay:</b> TSH là xét nghiệm sàng lọc nội tiết bắt buộc hàng đầu trong chẩn đoán AUB-O để phát hiện các rối loạn tuyến giáp tiềm ẩn.<br>2) <b>Hậu quả suy giáp:</b> Suy giáp làm tăng hormone TRH vùng dưới đồi → kích thích tăng tiết prolactin tuyến yên → ức chế phát xung GnRH gây <span style=\"color:#ff6b6b\"><b>kinh nhiều HMB hoặc vô kinh</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Điều trị ổn định suy giáp bằng Levothyroxine sẽ tự động khôi phục chu kỳ kinh nguyệt bình thường mà không cần dùng thuốc nội tiết phụ khoa kéo dài."
    elif card["id"] == "OB22-B6-04":
        card["back"] = "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tác động trên nội mạc:</b> Tamoxifen có tác dụng kháng estrogen trên tuyến vú nhưng lại có hoạt tính chủ vận estrogen một phần trên nội mạc tử cung → làm tăng nguy cơ polyp, quá sản và ung thư nội mạc tử cung gấp <span style=\"color:#ff6b6b\"><b>2 – 7 lần</b></span>.<br>2) <b>Xử trí khi ra máu:</b> Không khuyến cáo sinh thiết thường quy ở người không triệu chứng; nhưng bất kỳ đợt ra máu âm đạo nào dù nhỏ nhất đều là chỉ định <span style=\"color:#51cf66\"><b>sinh thiết nội mạc tử cung khẩn cấp</b></span>.<br><br><b>💡 Giải thích của AI:</b><br>Tamoxifen làm biến đổi mô đệm nội mạc dạng nang giả (subepithelial stromal condensation) rất dễ nhầm với quá sản trên siêu âm."
    
    fixed_old_cards.append(card)

# Thẻ Cloze bổ trợ cho B0 - B7 để tăng mật độ và độ sâu
cloze_b0_b7 = [
    {
        "id": "OB22-B0-C01",
        "type": "cloze",
        "section": "B0",
        "category": "Trục HPO",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Để tạo đỉnh phóng noãn LH (LH surge), nồng độ Estradiol huyết tương của nang noãn trội phải đạt ngưỡng {{c1::> 200 pg/mL}} và duy trì liên tục trong tối thiểu {{c2::48 giờ}}.",
        "extra": "📖 Nguồn: Yen & Jaffe's Reproductive Endocrinology 8th Edition",
        "tags": ["OB-22", "B0", "LH_surge", "Nguong_E2"]
    },
    {
        "id": "OB22-B1-C01",
        "type": "cloze",
        "section": "B1",
        "category": "Thang điểm PBAC",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Trên bảng điểm hình ảnh đánh giá mất máu kinh nguyệt (PBAC), một chu kỳ có tổng điểm từ {{c1::≥ 100 điểm}} trở lên được xác định là Rong kinh (HMB), tương đương với lượng máu kinh mất thực tế {{c2::> 80 mL}}.",
        "extra": "📖 Nguồn: Higham JM et al. Br J Obstet Gynaecol & FIGO 2018",
        "tags": ["OB-22", "B1", "PBAC_100", "HMB_80mL"]
    },
    {
        "id": "OB22-B2-C01",
        "type": "cloze",
        "section": "B2",
        "category": "Thông số chu kỳ FIGO",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Theo tiêu chuẩn chuẩn hóa của FIGO, chu kỳ kinh nguyệt bình thường có độ dài từ {{c1::24 đến 38 ngày}}, số ngày hành kinh kéo dài không quá {{c2::8 ngày}}, và mức độ dao động giữa các chu kỳ không quá {{c3::7 đến 9 ngày}}.",
        "extra": "📖 Nguồn: Munro MG et al. Int J Gynaecol Obstet 2018 (FIGO Systems 1 and 2)",
        "tags": ["OB-22", "B2", "FIGO_parameters", "Chu_ky_chuan"]
    },
    {
        "id": "OB22-B3-C01",
        "type": "cloze",
        "section": "B3",
        "category": "U xơ dưới niêm mạc FIGO",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Trong phân loại FIGO u xơ tử cung: Type 0 là u xơ có cuống nằm hoàn toàn trong lòng tử cung; Type 1 là u xơ lồi vào buồng tử cung {{c1::≥ 50%}}; Type 2 là u xơ lồi vào buồng tử cung {{c2::< 50%}}.",
        "extra": "📖 Nguồn: FIGO Fibroid Subclassification System (Munro 2011/2018)",
        "tags": ["OB-22", "B3", "FIGO_Type_0_1_2"]
    },
    {
        "id": "OB22-B4-C01",
        "type": "cloze",
        "section": "B4",
        "category": "Rối loạn đông máu",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Bệnh lý đông máu di truyền phổ biến nhất gây rong kinh nặng ở phụ nữ trẻ là {{c1::bệnh von Willebrand (vWD)}}, chiếm tỷ lệ lên tới {{c2::10% đến 20%}} ở nhóm vị thành niên nhập viện vì Acute AUB.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 651 & James AH et al.",
        "tags": ["OB-22", "B4", "vWD_cloze", "Coagulopathy"]
    },
    {
        "id": "OB22-B5-C01",
        "type": "cloze",
        "section": "B5",
        "category": "Thời điểm siêu âm",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Thời điểm vàng để thực hiện siêu âm đầu dò âm đạo (TVUS) khảo sát nội mạc tử cung ở phụ nữ độ tuổi sinh sản là vào {{c1::ngày 4 đến ngày 6 của chu kỳ kinh nguyệt (ngay sau khi vừa sạch kinh)}}, khi nội mạc mỏng nhất giúp dễ phát hiện polyp và u xơ dưới niêm.",
        "extra": "📖 Nguồn: AIUM Practice Parameter for Gynecologic Ultrasound Examination",
        "tags": ["OB-22", "B5", "Thoi_diem_TVUS"]
    },
    {
        "id": "OB22-B6-C01",
        "type": "cloze",
        "section": "B6",
        "category": "Chỉ định sinh thiết ACOG",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Theo ACOG Practice Bulletin 128, mọi phụ nữ xuất huyết tử cung bất thường từ {{c1::≥ 45 tuổi}} trở lên đều có chỉ định bắt buộc phải {{c2::sinh thiết nội mạc tử cung}} trước khi bắt đầu bất kỳ liệu trình điều trị nội tiết dài hạn nào.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 128",
        "tags": ["OB-22", "B6", "Sinh_thiet_45_tuoi"]
    },
    {
        "id": "OB22-B7-C01",
        "type": "cloze",
        "section": "B7",
        "category": "COCs dồn dập cấp cứu",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Phác đồ hormone đường uống dồn dập cấp cứu Acute AUB theo ACOG PB #557: Sử dụng viên tránh thai kết hợp (COCs chứa 30–35 µg EE) uống {{c1::1 viên mỗi 6 đến 8 giờ}} cho đến khi ngưng ra máu hoàn toàn, sau đó giảm liều dần theo bậc thang.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 557 · Acute AUB",
        "tags": ["OB-22", "B7", "COCs_acute"]
    }
]

# Thẻ mới cho B8 đến B15
new_cards_b8_b15 = [
    # ==========================================
    # PHẦN B8: PROTOCOL ĐIỀU TRỊ MẠN TÍNH & NỘI KHOA (8 thẻ)
    # ==========================================
    {
        "id": "OB22-B8-01",
        "type": "basic",
        "section": "B8",
        "category": "Điều trị nội khoa HMB",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Cơ chế vòng Mirena", "Hiệu quả giảm máu"],
        "front": "<span style=\"color:#74c0fc\"><b>Cơ chế vòng Mirena</b></span> (LNG-IUS) và <span style=\"color:#51cf66\"><b>hiệu quả giảm máu</b></span> trong điều trị HMB mạn tính?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế vòng Mirena:</b> Giải phóng tại chỗ <span style=\"color:#74c0fc\"><b>Levonorgestrel 20 µg/ngày</b></span> gây ức chế mạnh thụ thể estrogen và progesterone tại nội mạc, làm mỏng teo lớp mô đệm tuyến và ức chế phản ứng viêm.<br>2) <b>Hiệu quả giảm máu:</b> Giúp giảm từ <span style=\"color:#51cf66\"><b>70% đến 90% lượng máu kinh</b></span> sau 6 đến 12 tháng sử dụng, đưa 20–50% phụ nữ về trạng thái vô kinh an toàn.<br><br><b>💡 Giải thích của AI:</b><br>NICE NG88 và ACOG đều xếp LNG-IUS là lựa chọn đầu tay (first-line) cho phụ nữ HMB không có ý định mang thai ngay.",
        "extra": "📖 Nguồn: NICE NG88 (2018) & Cochrane Review on LNG-IUS",
        "tags": ["OB-22", "B8", "LNG_IUS", "Mirena", "First_line"]
    },
    {
        "id": "OB22-B8-02",
        "type": "basic",
        "section": "B8",
        "category": "Thuốc Tranexamic acid",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Liều dùng đường uống", "Ưu điểm lâm sàng"],
        "front": "<span style=\"color:#51cf66\"><b>Liều dùng đường uống</b></span> của Tranexamic acid và <span style=\"color:#74c0fc\"><b>ưu điểm lâm sàng</b></span> cho phụ nữ muốn sinh con?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Liều dùng đường uống:</b> Uống <span style=\"color:#51cf66\"><b>1.000 mg đến 1.300 mg (2 viên 500 mg hoặc 650 mg) x 3 lần/ngày</b></span> chỉ uống trong những ngày có kinh nhiều (tối đa 4-5 ngày/chu kỳ).<br>2) <b>Ưu điểm lâm sàng:</b> <span style=\"color:#74c0fc\"><b>Không chứa hormone</b></span>, không ức chế phóng noãn, không ảnh hưởng đến khả năng thụ thai tự nhiên, giúp giảm 40–50% lượng máu kinh.<br><br><b>💡 Giải thích của AI:</b><br>Tranexamic acid là lựa chọn không chứa nội tiết đầu tay cho phụ nữ muốn giữ chu kỳ tự nhiên để có thai.",
        "extra": "📖 Nguồn: Cochrane Systematic Review & ACOG PB 128",
        "tags": ["OB-22", "B8", "Tranexamic_acid", "Khong_hormone"]
    },
    {
        "id": "OB22-B8-03",
        "type": "basic",
        "section": "B8",
        "category": "Thuốc NSAIDs",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Cơ chế hạ Prostaglandin", "Chỉ định phối hợp"],
        "front": "<span style=\"color:#74c0fc\"><b>Cơ chế hạ Prostaglandin</b></span> của NSAIDs và <span style=\"color:#51cf66\"><b>chỉ định phối hợp</b></span> ở bệnh nhân vừa rong kinh vừa đau bụng kinh?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Cơ chế hạ Prostaglandin:</b> Ức chế men cyclooxygenase (COX) làm giảm nồng độ chất giãn mạch PGE2 và Prostacyclin (PGI2), giúp giảm <span style=\"color:#ffd43b\"><b>khoảng 30% lượng máu kinh</b></span>.<br>2) <b>Chỉ định phối hợp:</b> Dùng <span style=\"color:#51cf66\"><b>Axit Mefenamic 500 mg x 3 lần/ngày</b></span> uống từ ngày đầu kỳ kinh; là thuốc tối ưu cho bệnh nhân vừa có HMB vừa có đau bụng kinh (dysmenorrhea).<br><br><b>💡 Giải thích của AI:</b><br>NSAIDs không làm tăng nguy cơ huyết khối như estrogen, thích hợp cho bệnh nhân có chống chỉ định hormone.",
        "extra": "📖 Nguồn: Bofill Rodriguez M et al. Cochrane Database Syst Rev 2019",
        "tags": ["OB-22", "B8", "NSAIDs", "Mefenamic_acid"]
    },
    {
        "id": "OB22-B8-04",
        "type": "basic",
        "section": "B8",
        "category": "Thuốc GnRH đối kháng",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Thuốc Relugolix combo", "Ưu điểm add-back"],
        "front": "Cơ chế của <span style=\"color:#51cf66\"><b>thuốc Relugolix combo</b></span> đường uống và <span style=\"color:#74c0fc\"><b>ưu điểm add-back</b></span> trong AUB do u xơ (AUB-L)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thuốc Relugolix combo:</b> Phối hợp <span style=\"color:#51cf66\"><b>Relugolix 40 mg (GnRH antagonist)</b></span> với Estradiol 1 mg và Norethindrone acetate 0.5 mg uống 1 viên/ngày giúp ức chế nhanh gonadotropin làm ngưng chảy máu sau 1-2 tháng.<br>2) <b>Ưu điểm add-back:</b> Liều rất nhỏ estrogen và progestin kèm theo giúp <span style=\"color:#74c0fc\"><b>ngăn ngừa loãng xương và triệu chứng bốc hỏa</b></span> mà không làm u xơ to lại.<br><br><b>💡 Giải thích của AI:</b><br>Thuốc GnRH antagonist đường uống mới này thay thế cho các mũi tiêm GnRHa bắp gây bốc hỏa dữ dội trước đây.",
        "extra": "📖 Nguồn: Al-Hendy A et al. N Engl J Med 2021 (LIBERTY trials)",
        "tags": ["OB-22", "B8", "Relugolix", "GnRH_antagonist"]
    },
    {
        "id": "OB22-B8-C01",
        "type": "cloze",
        "section": "B8",
        "category": "Hiệu quả Mirena",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Vòng nội tiết LNG-IUS (Mirena) giải phóng tại chỗ 20 µg levonorgestrel mỗi ngày, giúp giảm lượng máu mất trong chu kỳ kinh nguyệt tới {{c1::70% đến 90%}} sau 6-12 tháng sử dụng.",
        "extra": "📖 Nguồn: NICE Guideline NG88 (2018) & FIGO 2018",
        "tags": ["OB-22", "B8", "Mirena_cloze"]
    },
    {
        "id": "OB22-B8-C02",
        "type": "cloze",
        "section": "B8",
        "category": "Bổ sung sắt",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Ở bệnh nhân HMB mạn tính có nồng độ Ferritin huyết thanh dưới {{c1::30 ng/mL}} hoặc nồng độ Hemoglobin dưới {{c2::100 g/L}}, bắt buộc chỉ định bổ sung sắt đường uống hoặc sắt truyền tĩnh mạch (Ferric carboxymaltose).",
        "extra": "📖 Nguồn: FIGO Recommendations on Iron Deficiency Anemia in AUB",
        "tags": ["OB-22", "B8", "Ferritin_cutoff"]
    },

    # ==========================================
    # PHẦN B9: PROTOCOL ĐIỀU TRỊ NGOẠI KHOA & CAN THIỆP (5 thẻ)
    # ==========================================
    {
        "id": "OB22-B9-01",
        "type": "basic",
        "section": "B9",
        "category": "Cắt đốt nội mạc tử cung",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Điều kiện chỉ định", "Chống chỉ định bắt buộc"],
        "front": "<span style=\"color:#51cf66\"><b>Điều kiện chỉ định</b></span> phẫu thuật cắt đốt nội mạc tử cung (Endometrial Ablation) và <span style=\"color:#ff6b6b\"><b>chống chỉ định bắt buộc</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Điều kiện chỉ định:</b> Dành cho phụ nữ HMB thất bại với điều trị nội khoa, <span style=\"color:#51cf66\"><b>đã đủ số con mong muốn</b></span> và kích thước buồng tử cung không quá biến dạng.<br>2) <b>Chống chỉ định bắt buộc:</b> Phụ nữ <span style=\"color:#ff6b6b\"><b>còn muốn sinh con</b></span>, có quá sản nội mạc tử cung không điển hình hoặc ung thư nội mạc, tử cung có sẹo mổ cũ rách hở.<br><br><b>💡 Giải thích của AI:</b><br>Cắt đốt nội mạc phá hủy lớp đáy basalis; nếu mang thai sau thủ thuật sẽ có nguy cơ cực cao bị nhau cài răng lược (PAS) và vỡ tử cung.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 81 · Endometrial Ablation",
        "tags": ["OB-22", "B9", "Ablation", "Cat_dot_noi_mac"]
    },
    {
        "id": "OB22-B9-02",
        "type": "basic",
        "section": "B9",
        "category": "Cắt u xơ soi buồng tử cung",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chỉ định TCR-M theo FIGO", "Ngưỡng kích thước an toàn"],
        "front": "<span style=\"color:#74c0fc\"><b>Chỉ định TCR-M theo FIGO</b></span> trong mổ cắt u xơ qua soi buồng tử cung và <span style=\"color:#ffd43b\"><b>ngưỡng kích thước an toàn</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chỉ định TCR-M theo FIGO:</b> Phẫu thuật cắt u xơ dưới niêm mạc qua ngã nội soi buồng tử cung là tiêu chuẩn vàng cho u xơ <span style=\"color:#74c0fc\"><b>FIGO Type 0 và Type 1</b></span> (lồi vào lòng buồng ≥ 50%).<br>2) <b>Ngưỡng kích thước an toàn:</b> Kích thước khối u lý tưởng <span style=\"color:#ffd43b\"><b>dưới 3 đến 4 cm</b></span> để hoàn thành phẫu thuật trong 1 thì, tránh nguy cơ ngộ độc dịch làm căng buồng tử cung (TURP syndrome).<br><br><b>💡 Giải thích của AI:</b><br>Với Type 2 (lồi < 50%), phẫu thuật khó khăn hơn và thường phải chia làm 2 thì mổ.",
        "extra": "📖 Nguồn: ESGE Guidelines on Hysteroscopic Myomectomy",
        "tags": ["OB-22", "B9", "TCR_M", "FIGO_type_0_1"]
    },
    {
        "id": "OB22-B9-03",
        "type": "basic",
        "section": "B9",
        "category": "Thuyên tắc động mạch tử cung",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Nguyên lý nút mạch UAE", "Cảnh báo bảo tồn sinh sản"],
        "front": "<span style=\"color:#51cf66\"><b>Nguyên lý nút mạch UAE</b></span> và <span style=\"color:#ff6b6b\"><b>cảnh báo bảo tồn sinh sản</b></span> ở bệnh nhân AUB do u xơ tử cung?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Nguyên lý nút mạch UAE:</b> Luồn catheter chọn lọc vào động mạch tử cung 2 bên bơm hạt vi cầu (PVA hoặc Gelatin) làm tắc mạch máu nuôi u xơ, gây thiếu máu hoại tử và teo nhỏ khối u.<br>2) <b>Cảnh báo bảo tồn sinh sản:</b> <span style=\"color:#ff6b6b\"><b>Không khuyến cáo ưu tiên cho phụ nữ còn muốn sinh con</b></span> do nguy cơ suy buồng trứng sớm, hoại tử nội mạc tử cung và biến chứng sảy thai/nhau bám bất thường.<br><br><b>💡 Giải thích của AI:</b><br>UAE là lựa chọn thay thế phẫu thuật tuyệt vời cho phụ nữ muốn giữ tử cung nhưng không còn nguyện vọng mang thai.",
        "extra": "📖 Nguồn: CIRSE Guidelines on Uterine Artery Embolization & ACOG PB 128",
        "tags": ["OB-22", "B9", "UAE", "Nut_mach", "Canh_bao_sinh_san"]
    },
    {
        "id": "OB22-B9-C01",
        "type": "cloze",
        "section": "B9",
        "category": "Cắt tử cung",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Phẫu thuật cắt tử cung toàn bộ (Hysterectomy) là giải pháp {{c1::triệt để 100%}} cho xuất huyết tử cung bất thường kháng trị với nội khoa, nhưng chỉ được chỉ định khi người phụ nữ {{c2::đã đủ con và có sự đồng thuận đầy đủ}}.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 128",
        "tags": ["OB-22", "B9", "Cat_tu_cung"]
    },
    {
        "id": "OB22-B9-04",
        "type": "basic",
        "section": "B9",
        "category": "Hội chứng sau nút mạch",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Triệu chứng kinh điển", "Xử trí giảm đau"],
        "front": "<span style=\"color:#ff6b6b\"><b>Triệu chứng kinh điển</b></span> của Hội chứng sau nút mạch tử cung (Post-UAE syndrome) và <span style=\"color:#51cf66\"><b>xử trí giảm đau</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Triệu chứng kinh điển:</b> Xuất hiện trong 24-48 giờ đầu gồm <span style=\"color:#ff6b6b\"><b>đau bụng vùng chậu dữ dội</b></span>, sốt nhẹ 38°C, buồn nôn, mệt mỏi và tăng bạch cầu phản ứng do mô u xơ hoại tử vô trùng.<br>2) <b>Xử trí giảm đau:</b> Truyền tĩnh mạch giảm đau nhóm <span style=\"color:#51cf66\"><b>Opioid (Morphine/Fentanyl) kết hợp NSAIDs và thuốc chống nôn</b></span> trong 48 giờ đầu sau thủ thuật.<br><br><b>💡 Giải thích của AI:</b><br>Cần phân biệt sốt vô trùng của hội chứng sau nút mạch với viêm nhiễm trùng tử cung cấp tính.",
        "extra": "📖 Nguồn: Society of Interventional Radiology Standards of Practice",
        "tags": ["OB-22", "B9", "Hoi_chung_sau_nut_mach", "UAE"]
    },

    # ==========================================
    # PHẦN B10: AUB THEO TỪNG GIAI ĐOẠN TUỔI (5 thẻ)
    # ==========================================
    {
        "id": "OB22-B10-01",
        "type": "basic",
        "section": "B10",
        "category": "AUB vị thành niên",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Căn nguyên thống trị", "Chỉ định tầm soát vWD"],
        "front": "<span style=\"color:#74c0fc\"><b>Căn nguyên thống trị</b></span> gây AUB ở tuổi vị thành niên và <span style=\"color:#ff6b6b\"><b>chỉ định tầm soát vWD</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Căn nguyên thống trị:</b> <span style=\"color:#74c0fc\"><b>Trục HPO chưa trưởng thành (AUB-O)</b></span> chiếm 70–80% các ca do chưa thiết lập phản hồi dương của LH để phóng noãn.<br>2) <b>Chỉ định tầm soát vWD:</b> Bắt buộc tầm soát bệnh von Willebrand khi bé gái bị <span style=\"color:#ff6b6b\"><b>HMB nặng ngay từ kỳ kinh đầu tiên (menarche)</b></span> hoặc kèm tiền sử chảy máu cam, chảy máu chân răng, bầm tím tự nhiên.<br><br><b>💡 Giải thích của AI:</b><br>Khoảng 20% các ca vị thành niên nhập viện vì rong huyết nặng thực chất có bệnh lý rối loạn đông máu nền.",
        "extra": "📖 Nguồn: Brookhart 2025 (PMID: 40924008) & ACOG Committee Opinion No. 651",
        "tags": ["OB-22", "B10", "Vi_thanh_nien", "vWD", "AUB_O"]
    },
    {
        "id": "OB22-B10-02",
        "type": "basic",
        "section": "B10",
        "category": "Xuất huyết sau mãn kinh PMB",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Quy tắc vàng chẩn đoán", "Ngưỡng bề dày nội mạc"],
        "front": "<span style=\"color:#ff6b6b\"><b>Quy tắc vàng chẩn đoán</b></span> ở phụ nữ xuất huyết sau mãn kinh (PMB) và <span style=\"color:#ffd43b\"><b>ngưỡng bề dày nội mạc</b></span> an toàn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Quy tắc vàng chẩn đoán:</b> <span style=\"color:#ff6b6b\"><b>PMB là ung thư nội mạc tử cung cho đến khi chứng minh ngược lại</b></span> (khoảng 10–15% phụ nữ PMB thực sự mắc ung thư).<br>2) <b>Ngưỡng bề dày nội mạc:</b> Bề dày nội mạc tử cung trên TVUS <span style=\"color:#ffd43b\"><b>≤ 4 mm</b></span> có giá trị dự đoán âm tính (NPV) > 99% đối với ung thư; nếu <span style=\"color:#ff6b6b\"><b>ET > 4 mm</b></span> hoặc ra máu tái diễn bắt buộc phải sinh thiết nội mạc tử cung.<br><br><b>💡 Giải thích của AI:</b><br>Dù chỉ ra máu một giọt nâu nhạt sau mãn kinh cũng bắt buộc phải siêu âm đo ET và không được cho về với đơn thuốc cầm máu.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 734 · Postmenopausal Bleeding",
        "tags": ["OB-22", "B10", "PMB", "Ung_thu_noi_mac", "ET_4mm"]
    },
    {
        "id": "OB22-B10-C01",
        "type": "cloze",
        "section": "B10",
        "category": "Ngưỡng PMB",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Ở phụ nữ xuất huyết sau mãn kinh (PMB), bề dày nội mạc tử cung đo trên siêu âm đầu dò âm đạo từ {{c1::≤ 4 mm}} trở xuống có giá trị dự đoán âm tính (NPV) lên tới {{c2::> 99%}} đối với ung thư nội mạc tử cung.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 734",
        "tags": ["OB-22", "B10", "PMB_cutoff"]
    },
    {
        "id": "OB22-B10-03",
        "type": "basic",
        "section": "B10",
        "category": "AUB tiền mãn kinh",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Đặc điểm sinh lý bệnh", "Chiến lược bảo vệ"],
        "front": "<span style=\"color:#74c0fc\"><b>Đặc điểm sinh lý bệnh</b></span> của AUB quanh mãn kinh và <span style=\"color:#51cf66\"><b>chiến lược bảo vệ</b></span> nội mạc khỏi ung thư?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Đặc điểm sinh lý bệnh:</b> Số lượng nang noãn cạn kiệt gây các chu kỳ không phóng noãn xen kẽ, nồng độ Estrogen dao động thất thường không có Progesterone đối kháng làm nội mạc tăng sinh không kiểm soát.<br>2) <b>Chiến lược bảo vệ:</b> Ở phụ nữ ≥ 45 tuổi, <span style=\"color:#51cf66\"><b>sinh thiết nội mạc tử cung trước tiên</b></span>; sau khi loại trừ ác tính, đặt vòng <span style=\"color:#51cf66\"><b>LNG-IUS (Mirena)</b></span> là liệu pháp số 1 vừa cầm máu vừa bảo vệ nội mạc đến khi mãn kinh hẳn.<br><br><b>💡 Giải thích của AI:</b><br>Tuổi quanh mãn kinh là đỉnh cao của nguy cơ quá sản nội mạc tiến triển thành ung thư biểu mô.",
        "extra": "📖 Nguồn: NAMS Menopause Practice Guidelines & ACOG PB 128",
        "tags": ["OB-22", "B10", "Tien_man_kinh", "Mirena"]
    },
    {
        "id": "OB22-B10-C02",
        "type": "cloze",
        "section": "B10",
        "category": "AUB độ tuổi sinh sản",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Ở phụ nữ trong độ tuổi sinh sản, nhóm nguyên nhân cấu trúc {{c1::PALM (đặc biệt là Polyp và U xơ dưới niêm mạc)}} và nguyên nhân do thuốc tránh thai {{c2::AUB-I}} chiếm tỷ lệ lớn nhất trong các đợt khám phụ khoa.",
        "extra": "📖 Nguồn: FIGO Systems 1 and 2 (Munro 2018)",
        "tags": ["OB-22", "B10", "Tuoi_sinh_san"]
    },

    # ==========================================
    # PHẦN B11: SO SÁNH GUIDELINE: FIGO vs ACOG vs NICE (4 thẻ)
    # ==========================================
    {
        "id": "OB22-B11-01",
        "type": "basic",
        "section": "B11",
        "category": "So sánh Guideline",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Khác biệt định nghĩa HMB", "Lựa chọn đầu tay NICE vs ACOG"],
        "front": "<span style=\"color:#74c0fc\"><b>Khác biệt định nghĩa HMB</b></span> giữa FIGO và NICE cùng <span style=\"color:#51cf66\"><b>lựa chọn đầu tay NICE vs ACOG</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Khác biệt định nghĩa HMB:</b> FIGO và ACOG chú trọng tiêu chí định lượng (PBAC ≥ 100 điểm hoặc > 80 mL máu); trong khi <span style=\"color:#74c0fc\"><b>NICE NG88 định nghĩa thuần túy theo chất lượng cuộc sống</b></span> (lượng máu gây ảnh hưởng thể chất, cảm xúc, xã hội của người phụ nữ).<br>2) <b>Lựa chọn đầu tay NICE vs ACOG:</b> NICE chọn <span style=\"color:#51cf66\"><b>vòng LNG-IUS là lựa chọn số 1 tuyệt đối</b></span> cho mọi bệnh nhân HMB; ACOG linh hoạt cá thể hóa lựa chọn giữa LNG-IUS, COCs, Tranexamic acid tùy nguyện vọng có thai.<br><br><b>💡 Giải thích của AI:</b><br>NICE tiếp cận theo mô hình hiệu quả - chi phí y tế công cộng (cost-effectiveness), trong khi ACOG tiếp cận cá thể hóa theo lựa chọn bệnh nhân.",
        "extra": "📖 Nguồn: Tsakiridis 2022 (PMID: 36053280) & NICE NG88 (2018)",
        "tags": ["OB-22", "B11", "So_sanh_guideline", "NICE_ACOG"]
    },
    {
        "id": "OB22-B11-02",
        "type": "basic",
        "section": "B11",
        "category": "Tiêu chuẩn sinh thiết nội mạc",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Tiêu chuẩn tuổi ACOG", "Tiêu chuẩn chọn lọc NICE"],
        "front": "<span style=\"color:#ffd43b\"><b>Tiêu chuẩn tuổi ACOG</b></span> chỉ định sinh thiết nội mạc tử cung so với <span style=\"color:#74c0fc\"><b>tiêu chuẩn chọn lọc NICE</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Tiêu chuẩn tuổi ACOG:</b> Bắt buộc sinh thiết nội mạc tử cung cho mọi phụ nữ AUB từ <span style=\"color:#ffd43b\"><b>≥ 45 tuổi</b></span>, hoặc phụ nữ < 45 tuổi có phơi nhiễm estrogen kéo dài (PCOS, béo phì BMI ≥ 30).<br>2) <b>Tiêu chuẩn chọn lọc NICE:</b> Chỉ định sinh thiết cho phụ nữ từ <span style=\"color:#ffd43b\"><b>≥ 45 tuổi</b></span> HOẶC thất bại với điều trị nội khoa hoặc ra máu dai dẳng giữa chu kỳ.<br><br><b>💡 Giải thích của AI:</b><br>Cả hai hiệp hội đều thống nhất mốc 45 tuổi là ranh giới bắt buộc phải sinh thiết loại trừ ung thư trước khi dùng nội tiết dài hạn.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 128 & NICE NG88",
        "tags": ["OB-22", "B11", "Sinh_thiet_45_tuoi"]
    },
    {
        "id": "OB22-B11-C01",
        "type": "cloze",
        "section": "B11",
        "category": "Review Tsakiridis 2022",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Nghiên cứu tổng quan của Tsakiridis et al. (2022) so sánh 5 hướng dẫn quốc tế (ACOG, NICE, RANZCOG, SOGC, FIGO) cho thấy sự đồng thuận 100% trong việc sử dụng hệ thống phân loại {{c1::PALM-COEIN}} để chẩn đoán nguyên nhân AUB.",
        "extra": "📖 Nguồn: Tsakiridis I et al. Arch Gynecol Obstet 2022 (PMID: 36053280)",
        "tags": ["OB-22", "B11", "Tsakiridis_2022"]
    },
    {
        "id": "OB22-B11-03",
        "type": "basic",
        "section": "B11",
        "category": "Chỉ định hình ảnh học",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chỉ định TVUS đầu tay", "Chỉ định SIS bậc hai"],
        "front": "<span style=\"color:#51cf66\"><b>Chỉ định TVUS đầu tay</b></span> và <span style=\"color:#74c0fc\"><b>chỉ định SIS bậc hai</b></span> theo đồng thuận các guideline quốc tế?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chỉ định TVUS đầu tay:</b> Mọi guideline đều khuyến cáo siêu âm đầu dò âm đạo (<span style=\"color:#51cf66\"><b>TVUS</b></span>) là phương tiện chẩn đoán hình ảnh số 1 để đánh giá cấu trúc tử cung và buồng trứng.<br>2) <b>Chỉ định SIS bậc hai:</b> Siêu âm bơm nước buồng tử cung (<span style=\"color:#74c0fc\"><b>SIS</b></span>) hoặc nội soi buồng tử cung được chỉ định khi TVUS nghi ngờ có polyp, u xơ dưới niêm hoặc đường nội mạc không đồng nhất.<br><br><b>💡 Giải thích của AI:</b><br>SIS có độ nhạy vượt trội trong việc phân định u xơ Type 1 hay Type 2 trước phẫu thuật.",
        "extra": "📖 Nguồn: ACOG PB 128 & NICE NG88",
        "tags": ["OB-22", "B11", "TVUS", "SIS_chi_dinh"]
    },

    # ==========================================
    # PHẦN B12: 6 CASE LÂM SÀNG GIẢ ĐỊNH CÓ LỜI GIẢI (6 thẻ)
    # ==========================================
    {
        "id": "OB22-B12-01",
        "type": "basic",
        "section": "B12",
        "category": "Case 1: Vị thành niên vWD",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chẩn đoán nguyên nhân", "Xử trí cấp cứu"],
        "front": "Nữ 14 tuổi kinh nguyệt ướt sũng băng mỗi giờ kèm nhổ răng chảy máu 2 ngày, Hb 7.2 g/dL: <span style=\"color:#74c0fc\"><b>Chẩn đoán nguyên nhân</b></span> và <span style=\"color:#51cf66\"><b>xử trí cấp cứu</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chẩn đoán nguyên nhân:</b> Xuất huyết tử cung cấp tính nặng do rối loạn đông máu <span style=\"color:#74c0fc\"><b>AUB-C (nghi ngờ bệnh von Willebrand)</b></span> trên nền thiếu máu trung bình.<br>2) <b>Xử trí cấp cứu:</b> Hồi sức truyền dịch, truyền khối hồng cầu duy trì Hb > 70 g/L, dùng <span style=\"color:#51cf66\"><b>Tranexamic acid tiêm tĩnh mạch + COCs liều cao</b></span> và hội chẩn Huyết học định lượng yếu tố vWF.<br><br><b>💡 Giải thích của AI:</b><br>Tránh dùng NSAIDs cho bệnh nhân nghi rối loạn đông máu vì sẽ làm suy giảm thêm chức năng tiểu cầu.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 651 & Case 1 Study",
        "tags": ["OB-22", "B12", "Case_1", "vWD_cap_cuu"]
    },
    {
        "id": "OB22-B12-02",
        "type": "basic",
        "section": "B12",
        "category": "Case 2: PCOS béo phì",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Phân loại theo FIGO", "Phác đồ nội tiết"],
        "front": "Nữ 28 tuổi béo phì BMI 31, rậm lông, kinh thưa 2-3 tháng/lần ra máu kéo dài: <span style=\"color:#74c0fc\"><b>Phân loại theo FIGO</b></span> và <span style=\"color:#51cf66\"><b>phác đồ nội tiết</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Phân loại theo FIGO:</b> <span style=\"color:#74c0fc\"><b>AUB-O (Ovulatory dysfunction)</b></span> do Hội chứng buồng trứng đa nang (PCOS) gây không rụng trứng mạn tính.<br>2) <b>Phác đồ nội tiết:</b> Dùng Progestin chu kỳ (<span style=\"color:#51cf66\"><b>Dydrogesterone 10-20 mg/ngày hoặc MPA 10 mg/ngày từ ngày 16 đến ngày 25</b></span>) để tạo chu kỳ kinh nhân tạo, bảo vệ nội mạc tử cung khỏi nguy cơ quá sản ung thư.<br><br><b>💡 Giải thích của AI:</b><br>Nếu chưa muốn có thai, viên tránh thai kết hợp (COCs) hoặc vòng LNG-IUS cũng là lựa chọn hàng đầu.",
        "extra": "📖 Nguồn: ASRM PCOS Practice Guideline & Case 2 Study",
        "tags": ["OB-22", "B12", "Case_2", "PCOS", "AUB_O"]
    },
    {
        "id": "OB22-B12-03",
        "type": "basic",
        "section": "B12",
        "category": "Case 3: Adenomyosis",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Dấu hiệu siêu âm TVUS", "Điều trị đầu tay"],
        "front": "Nữ 36 tuổi kinh nhiều đóng cục, đau bụng kinh dữ dội tăng dần: <span style=\"color:#74c0fc\"><b>Dấu hiệu siêu âm TVUS</b></span> và <span style=\"color:#51cf66\"><b>điều trị đầu tay</b></span> bảo tồn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Dấu hiệu siêu âm TVUS:</b> Tử cung to hình cầu, cơ tử cung dày bất đối xứng, vùng chuyển tiếp <span style=\"color:#74c0fc\"><b>JZmax = 13 mm</b></span> có các nang nhỏ trong cơ bóng lưng hình rẻ quạt (Adenomyosis).<br>2) <b>Điều trị đầu tay:</b> Đặt vòng nội tiết <span style=\"color:#51cf66\"><b>LNG-IUS (Mirena)</b></span> giúp teo tuyến lạc chỗ, giảm 80-90% lượng máu kinh và cải thiện rõ rệt triệu chứng đau bụng kinh.<br><br><b>💡 Giải thích của AI:</b><br>Mirena là giải pháp bảo tồn tử cung tốt nhất cho phụ nữ Adenomyosis muốn tránh phẫu thuật cắt tử cung.",
        "extra": "📖 Nguồn: MUSA 2022 & Case 3 Study",
        "tags": ["OB-22", "B12", "Case_3", "Adenomyosis", "Mirena"]
    },
    {
        "id": "OB22-B12-04",
        "type": "basic",
        "section": "B12",
        "category": "Case 4: U xơ Type 1",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chẩn đoán vị trí FIGO", "Phương pháp phẫu thuật"],
        "front": "Nữ 48 tuổi HMB thiếu máu, siêu âm có khối u xơ 35mm lồi 70% vào buồng tử cung: <span style=\"color:#74c0fc\"><b>Chẩn đoán vị trí FIGO</b></span> và <span style=\"color:#51cf66\"><b>phương pháp phẫu thuật</b></span> chuẩn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chẩn đoán vị trí FIGO:</b> U xơ dưới niêm mạc <span style=\"color:#74c0fc\"><b>FIGO Type 1</b></span> (lồi vào buồng tử cung ≥ 50% nhưng chưa có cuống trọn vẹn).<br>2) <b>Phương pháp phẫu thuật:</b> <span style=\"color:#51cf66\"><b>Phẫu thuật nội soi buồng tử cung cắt u xơ (TCR-M)</b></span> bằng dao điện đơn cực hoặc lưỡng cực qua ngã âm đạo, bảo tồn nguyên vẹn tử cung.<br><br><b>💡 Giải thích của AI:</b><br>TCR-M giải quyết triệt để triệu chứng rong huyết mà không cần mổ mở ổ bụng.",
        "extra": "📖 Nguồn: ESGE Guidelines on TCR-M & Case 6 Study",
        "tags": ["OB-22", "B12", "Case_4", "TCR_M", "FIGO_Type_1"]
    },
    {
        "id": "OB22-B12-05",
        "type": "basic",
        "section": "B12",
        "category": "Case 5: PMB nghi ung thư",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chẩn đoán phân biệt", "Hành động bắt buộc"],
        "front": "Phụ nữ 53 tuổi mãn kinh 2 năm ra máu âm đạo ít, TVUS đo ET = 7mm: <span style=\"color:#ff6b6b\"><b>Chẩn đoán phân biệt</b></span> và <span style=\"color:#51cf66\"><b>hành động bắt buộc</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chẩn đoán phân biệt:</b> <span style=\"color:#ff6b6b\"><b>Nghi ngờ AUB-M (Ung thư hoặc Quá sản nội mạc tử cung)</b></span>, polyp nội mạc tử cung hoặc viêm teo nội mạc.<br>2) <b>Hành động bắt buộc:</b> Thực hiện ngay <span style=\"color:#51cf66\"><b>hút sinh thiết nội mạc tử cung bằng ống Pipelle</b></span> tại phòng khám; nếu thất bại hoặc kết quả nghi ngờ thì soi buồng tử cung sinh thiết dưới hướng dẫn nhìn trực tiếp.<br><br><b>💡 Giải thích của AI:</b><br>ET = 7mm (> 4mm) ở phụ nữ sau mãn kinh mất đi giá trị loại trừ an toàn, bắt buộc phải có kết quả giải phẫu bệnh.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 734 & Case 5 Study",
        "tags": ["OB-22", "B12", "Case_5", "PMB", "Pipelle"]
    },
    {
        "id": "OB22-B12-06",
        "type": "basic",
        "section": "B12",
        "category": "Case 6: Polyp nội mạc IMB",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Đặc điểm ra máu IMB", "Chỉ định can thiệp"],
        "front": "Phụ nữ 42 tuổi ra máu giữa kỳ (IMB) có khối tăng âm 12mm cuống mạch đơn độc: <span style=\"color:#74c0fc\"><b>Đặc điểm ra máu IMB</b></span> và <span style=\"color:#51cf66\"><b>chỉ định can thiệp</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Đặc điểm ra máu IMB:</b> Ra máu thấm giọt giữa hai kỳ kinh nguyệt đều đặn là dấu hiệu kinh điển của <span style=\"color:#74c0fc\"><b>Polyp nội mạc tử cung (AUB-P)</b></span>.<br>2) <b>Chỉ định can thiệp:</b> <span style=\"color:#51cf66\"><b>Cắt polyp qua nội soi buồng tử cung (Hysteroscopic polypectomy)</b></span> để vừa cầm máu triệt để vừa gửi giải phẫu bệnh loại trừ ác tính.<br><br><b>💡 Giải thích của AI:</b><br>Điều trị nội khoa không làm tiêu biến polyp buồng tử cung thực thụ.",
        "extra": "📖 Nguồn: AAGL Practice Guidelines on Endometrial Polyps & Case 4 Study",
        "tags": ["OB-22", "B12", "Case_6", "Polyp", "IMB"]
    },

    # ==========================================
    # PHẦN B13: SAI LẦM THƯỜNG GẶP & CẠM BẪY LÂM SÀNG (4 thẻ)
    # ==========================================
    {
        "id": "OB22-B13-01",
        "type": "basic",
        "section": "B13",
        "category": "Bẫy thử beta-hCG",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Sai lầm bỏ qua beta-hCG", "Hậu quả đe dọa tính mạng"],
        "front": "<span style=\"color:#ff6b6b\"><b>Sai lầm bỏ qua beta-hCG</b></span> ở phụ nữ tuổi sinh sản và <span style=\"color:#ff6b6b\"><b>hậu quả đe dọa tính mạng</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sai lầm bỏ qua beta-hCG:</b> Tin vào lời khẳng định của bệnh nhân ('tôi không thể có thai / chồng tôi đi vắng') mà không xét nghiệm nước tiểu hoặc máu.<br>2) <b>Hậu quả đe dọa tính mạng:</b> Bỏ sót <span style=\"color:#ff6b6b\"><b>Thai ngoài tử cung vỡ gây sốc mất máu</b></span>, sảy thai băng huyết, hoặc bệnh nguyên bào nuôi (chửa trứng/ung thư nguyên bào nuôi).<br><br><b>💡 Giải thích của AI:</b><br>Nguyên tắc số 1 của cấp cứu phụ khoa: Mọi phụ nữ trong độ tuổi hoạt động sinh sản bị ra máu bất thường đều phải test beta-hCG.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 128 & Pitfalls in Gynecologic Emergencies",
        "tags": ["OB-22", "B13", "Bay_lam_sang", "beta_hCG"]
    },
    {
        "id": "OB22-B13-02",
        "type": "basic",
        "section": "B13",
        "category": "Bẫy dị dạng động tĩnh mạch AVM",
        "tier": 1,
        "track": "ebm",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-algo",
        "asks": ["Dấu hiệu cảnh báo AVM", "Hành động tuyệt đối cấm"],
        "front": "⚡ <b>CỜ ĐỎ TỬ VONG:</b> <span style=\"color:#74c0fc\"><b>Dấu hiệu cảnh báo AVM</b></span> tử cung trên siêu âm Doppler và <span style=\"color:#ff6b6b\"><b>hành động tuyệt đối cấm</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Dấu hiệu cảnh báo AVM:</b> Khối búi mạch dạng hang trong cơ tử cung, trên Doppler màu có hình ảnh <span style=\"color:#74c0fc\"><b>dòng chảy xoáy đa sắc (Mosaic pattern) với vận tốc tâm thu đỉnh PSV rất cao (> 50-70 cm/s) và RI thấp</b></span>.<br>2) <b>Hành động tuyệt đối cấm:</b> <span style=\"color:#ff6b6b\"><b>TUYỆT ĐỐI CẤM NẠO HÚT BUỒNG TỬ CUNG (D&C)</b></span>; nạo hút sẽ làm rách búi thông động tĩnh mạch gây chảy máu xối xả đe dọa tử vong trong vài phút.<br><br><b>💡 Giải thích của AI:</b><br>Xử trí đúng của AVM là nút mạch động mạch tử cung (UAE) qua can thiệp mạch máu.",
        "extra": "📖 Nguồn: Timor-Tritsch IE et al. Ultrasound Obstet Gynecol · Uterine AVM",
        "tags": ["OB-22", "B13", "AVM", "Tuyet_doi_cam_nao"]
    },
    {
        "id": "OB22-B13-03",
        "type": "basic",
        "section": "B13",
        "category": "Bẫy Estrogen đơn thuần",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Sai lầm dùng Estrogen đơn độc", "Hậu quả bùng phát máu"],
        "front": "<span style=\"color:#ff6b6b\"><b>Sai lầm dùng Estrogen đơn độc</b></span> cho bệnh nhân AUB-O và <span style=\"color:#ff6b6b\"><b>hậu quả bùng phát máu</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Sai lầm dùng Estrogen đơn độc:</b> Cho bệnh nhân không rụng trứng (PCOS) uống Estrogen liều cao kéo dài mà không có Progesterone phối hợp đối kháng.<br>2) <b>Hậu quả bùng phát máu:</b> Làm nội mạc tử cung vốn đã dày càng tăng sinh dữ dội hơn, khi ngừng thuốc sẽ gây <span style=\"color:#ff6b6b\"><b>đợt băng kinh ồ ạt (estrogen withdrawal/breakthrough)</b></span> và thúc đẩy quá sản nội mạc tiến triển thành ung thư.<br><br><b>💡 Giải thích của AI:</b><br>AUB-O bản chất là thừa Estrogen thiếu Progesterone, điều trị bắt buộc phải dùng Progestin đối kháng.",
        "extra": "📖 Nguồn: Yen & Jaffe's Reproductive Endocrinology",
        "tags": ["OB-22", "B13", "Estrogen_don_doc", "PCOS_sai_lam"]
    },
    {
        "id": "OB22-B13-C01",
        "type": "cloze",
        "section": "B13",
        "category": "Bẫy lạm dụng D&C",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Lạm dụng nạo buồng tử cung (D&C) lặp đi lặp lại như một biện pháp điều trị mạn tính cho rong kinh {{c1::hoàn toàn KHÔNG có hiệu quả lâu dài}} (máu kinh sẽ nhiều trở lại sau 1 chu kỳ) và làm tăng nguy cơ {{c2::dính buồng tử cung (Asherman)}}.",
        "extra": "📖 Nguồn: ACOG Committee Opinion No. 557 & SOGC Guidelines",
        "tags": ["OB-22", "B13", "Lam_dung_DC"]
    },

    # ==========================================
    # PHẦN B14: LƯU ĐỒ 3 BƯỚC & ÁP DỤNG VIỆT NAM (4 thẻ)
    # ==========================================
    {
        "id": "OB22-B14-01",
        "type": "basic",
        "section": "B14",
        "category": "Lưu đồ 3 bước giường bệnh",
        "tier": 1,
        "track": "ebm",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-algo",
        "asks": ["Bước 1 Ổn định & Thai", "Bước 2 Chống ung thư", "Bước 3 Điều trị đích"],
        "front": "⚡ <b>LƯU ĐỒ 3 BƯỚC GIƯỜNG BỆNH:</b> Quy trình phản xạ <span style=\"color:#ff6b6b\"><b>Bước 1 Ổn định & Thai</b></span>, <span style=\"color:#ffd43b\"><b>Bước 2 Chống ung thư</b></span> và <span style=\"color:#51cf66\"><b>Bước 3 Điều trị đích</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Bước 1 Ổn định & Thai:</b> Đánh giá sinh hiệu huyết động (mạch, HA); test <span style=\"color:#ff6b6b\"><b>β-hCG ngay lập tức</b></span> loại trừ biến chứng thai nghén cấp cứu.<br>2) <b>Bước 2 Chống ung thư:</b> Phụ nữ ≥ 45 tuổi hoặc PMB hoặc < 45 tuổi có nguy cơ cao (PCOS, béo phì) → <span style=\"color:#ffd43b\"><b>bắt buộc sinh thiết nội mạc tử cung trước tiên</b></span>.<br>3) <b>Bước 3 Điều trị đích:</b> Dùng TVUS/SIS phân loại theo <span style=\"color:#51cf66\"><b>FIGO PALM-COEIN</b></span>; ưu tiên bảo tồn tử cung bằng vòng LNG-IUS (Mirena) hoặc Tranexamic acid.<br><br><b>💡 Giải thích của AI:</b><br>Quy trình 3 bước này ngăn ngừa 100% các sai lầm bỏ sót cấp cứu đe dọa tính mạng và ung thư phụ khoa.",
        "extra": "📖 Nguồn: FIGO Menstrual Disorders Committee & Lưu đồ thực hành AUB 2026",
        "tags": ["OB-22", "B14", "Luu_do_3_buoc", "Thuat_toan"]
    },
    {
        "id": "OB22-B14-02",
        "type": "basic",
        "section": "B14",
        "category": "Áp dụng tại Việt Nam",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["Chiến lược tuyến cơ sở", "Vai trò thuốc BHYT"],
        "front": "<span style=\"color:#51cf66\"><b>Chiến lược tuyến cơ sở</b></span> tại Việt Nam và <span style=\"color:#74c0fc\"><b>vai trò thuốc BHYT</b></span> trong điều trị HMB mạn tính?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Chiến lược tuyến cơ sở:</b> Dùng siêu âm đầu dò âm đạo (TVUS) làm cận lâm sàng chủ lực; điều trị cầm máu nội khoa bằng <span style=\"color:#51cf66\"><b>Tranexamic acid (Transamin) phối hợp COCs liều chuẩn</b></span>.<br>2) <b>Vai trò thuốc BHYT:</b> Tranexamic acid và viên COCs được BHYT chi trả rộng rãi, chi phí thấp, sẵn có; vòng LNG-IUS (Mirena) giá còn cao (khoảng 2-3 triệu) cần tư vấn tính kinh tế dài hạn trong 5 năm.<br><br><b>💡 Giải thích của AI:</b><br>Tuyến cơ sở cần chuyển tuyến khi nghi ngờ ung thư nội mạc, khối u xơ to cần mổ nội soi hoặc Acute AUB tụt huyết áp.",
        "extra": "📖 Nguồn: Phác đồ điều trị Sản Phụ khoa BV Từ Dũ / Hùng Vương & Bộ Y Tế",
        "tags": ["OB-22", "B14", "Viet_Nam", "Tuyen_co_so", "BHYT"]
    },
    {
        "id": "OB22-B14-C01",
        "type": "cloze",
        "section": "B14",
        "category": "Tuyến chuyển viện",
        "tier": 2,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Tại tuyến y tế cơ sở ở Việt Nam, chỉ định chuyển tuyến trên khẩn cấp bao gồm: xuất huyết tử cung cấp tính kèm tụt huyết áp không đáp ứng bù dịch, nghi ngờ {{c1::dị dạng động tĩnh mạch tử cung (AVM)}}, và xuất huyết sau mãn kinh có {{c2::nội mạc tử cung dày > 4 mm}}.",
        "extra": "📖 Nguồn: Hướng dẫn chẩn đoán và điều trị các bệnh Sản Phụ khoa - Bộ Y Tế",
        "tags": ["OB-22", "B14", "Chuyen_tuyen"]
    },

    # ==========================================
    # PHẦN B15: TIPS THỰC HÀNH & CÂU HỎI THỰC CHIẾN (6 thẻ)
    # ==========================================
    {
        "id": "OB22-B15-01",
        "type": "basic",
        "section": "B15",
        "category": "Clinical Pearls cốt lõi",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "asks": ["AUB không phải chẩn đoán", "Quy tắc PMB"],
        "front": "Hai nguyên lý cốt tử: Tại sao <span style=\"color:#74c0fc\"><b>AUB không phải chẩn đoán</b></span> và <span style=\"color:#ff6b6b\"><b>quy tắc PMB</b></span> bất biến?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>AUB không phải chẩn đoán:</b> AUB chỉ là một <span style=\"color:#74c0fc\"><b>triệu chứng lâm sàng</b></span>; chẩn đoán cuối cùng bắt buộc phải mang tên một nguyên nhân cụ thể trong hệ thống FIGO PALM-COEIN.<br>2) <b>Quy tắc PMB bất biến:</b> <span style=\"color:#ff6b6b\"><b>Ra máu sau mãn kinh là ung thư nội mạc tử cung cho đến khi chứng minh ngược lại</b></span>; không bao giờ được phép chủ quan dù bệnh nhân chỉ ra máu một lần rất ít.<br><br><b>💡 Giải thích của AI:</b><br>Ghi chẩn đoán trong bệnh án là 'AUB' đơn thuần là thiếu sót chuyên môn.",
        "extra": "📖 Nguồn: FIGO 2018 & ACOG Practice Bulletin No. 128",
        "tags": ["OB-22", "B15", "Clinical_pearls", "PMB", "PALM_COEIN"]
    },
    {
        "id": "OB22-B15-02",
        "type": "basic",
        "section": "B15",
        "category": "Câu hỏi thực chiến 1",
        "tier": 1,
        "track": "ebm",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-algo",
        "asks": ["Thuốc uống kèm bắt buộc", "Quy tắc giảm liều"],
        "front": "⚡ <b>CẤP CỨU THỰC CHIẾN:</b> Khi dùng COCs liều cao dồn dập cầm máu cấp — <span style=\"color:#51cf66\"><b>Thuốc uống kèm bắt buộc</b></span> và <span style=\"color:#ff6b6b\"><b>quy tắc giảm liều</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thuốc uống kèm bắt buộc:</b> Uống kèm <span style=\"color:#51cf66\"><b>thuốc chống nôn (Metoclopramide 10mg hoặc Ondansetron 4-8mg)</b></span> trước viên COC 30 phút vì nồng độ Estrogen cao kích thích trung tâm nôn rất dữ dội.<br>2) <b>Quy tắc giảm liều:</b> <span style=\"color:#ff6b6b\"><b>Tuyệt đối không ngừng thuốc đột ngột</b></span>; phải giảm liều từ từ (Tapering): 3 viên/ngày x 2 ngày → 2 viên/ngày x 2 ngày → 1 viên/ngày cho đủ vỉ 21 ngày để tránh chảy máu bong tróc tái phát.<br><br><b>💡 Giải thích của AI:</b><br>Nếu bệnh nhân nôn hết thuốc ra ngoài, phác đồ hormone dồn dập sẽ thất bại hoàn toàn.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 557 · Acute AUB Management",
        "tags": ["OB-22", "B15", "COCs_tapering", "Chong_non"]
    },
    {
        "id": "OB22-B15-03",
        "type": "basic",
        "section": "B15",
        "category": "Câu hỏi thực chiến 2",
        "tier": 1,
        "track": "ebm",
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH",
        "badge_class": "badge-algo",
        "asks": ["Thể tích bơm bóng Foley", "Thời gian lưu bóng tối đa"],
        "front": "⚡ <b>THỦ THUẬT THỰC CHIẾN:</b> <span style=\"color:#ffd43b\"><b>Thể tích bơm bóng Foley</b></span> chèn buồng tử cung và <span style=\"color:#ff6b6b\"><b>thời gian lưu bóng tối đa</b></span>?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1) <b>Thể tích bơm bóng Foley:</b> Bơm từ <span style=\"color:#ffd43b\"><b>10 đến 30 mL nước muối sinh lý vô khuẩn</b></span> vào bóng chèn ép trực diện diện chảy máu buồng tử cung.<br>2) <b>Thời gian lưu bóng tối đa:</b> Chỉ lưu bóng tối đa trong vòng <span style=\"color:#ff6b6b\"><b>12 đến 24 giờ</b></span> kết hợp dùng kháng sinh dự phòng để tránh nguy cơ hoại tử cơ tử cung và nhiễm trùng nặng.<br><br><b>💡 Giải thích của AI:</b><br>Chèn bóng Foley là biện pháp bắc cầu cứu mạng giúp giữ huyết động trong khi chờ chuẩn bị phòng mổ.",
        "extra": "📖 Nguồn: ACOG PB 557 & Practical Gynecologic Procedures",
        "tags": ["OB-22", "B15", "Foley_tamponade", "The_tich_bom"]
    },
    {
        "id": "OB22-B15-C01",
        "type": "cloze",
        "section": "B15",
        "category": "Thời gian lưu bóng Foley",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Bóng Foley chèn buồng tử cung cầm máu trong Acute AUB chỉ được lưu tối đa trong vòng {{c1::12 đến 24 giờ}} và bơm thể tích từ {{c2::10 đến 30 mL}} nước muối sinh lý vô khuẩn.",
        "extra": "📖 Nguồn: ACOG Practice Bulletin No. 557 (Reaffirmed 2020)",
        "tags": ["OB-22", "B15", "Foley_cloze"]
    },
    {
        "id": "OB22-B15-C02",
        "type": "cloze",
        "section": "B15",
        "category": "Ngưỡng truyền máu",
        "tier": 1,
        "track": "ebm",
        "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-ebm",
        "text": "Trong cấp cứu Acute AUB ở phụ nữ trẻ khỏe mạnh không có bệnh tim mạch, ngưỡng nồng độ Hemoglobin để chỉ định truyền khối hồng cầu là {{c1::Hb < 70 g/L (hoặc Hct < 21%)}}.",
        "extra": "📖 Nguồn: AABB Guidelines on Blood Transfusion & ACOG PB 557",
        "tags": ["OB-22", "B15", "Truyen_mau_cutoff"]
    }
]

# Gộp danh sách và xuất file
all_cards = fixed_old_cards + cloze_b0_b7 + new_cards_b8_b15
print(f"Tong so the moi: {len(all_cards)} the")

output_file = cards_path
output_file.write_text(json.dumps({"cards": all_cards}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Da ghi thanh cong vao {output_file}")
