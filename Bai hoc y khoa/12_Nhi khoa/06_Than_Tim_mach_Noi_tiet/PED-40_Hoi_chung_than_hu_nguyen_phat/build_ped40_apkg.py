# -*- coding: utf-8 -*-
"""
build_ped40_apkg.py
Tạo bộ thẻ Anki chuẩn hóa cho bài PED-40: Hội chứng thận hư nguyên phát ở trẻ em.
Quy tắc:
- Ưu tiên dạng Basic câu hỏi (có 📖 Văn bản gốc & 🔍 Góc nhìn bổ sung AI).
- Với dạng Cloze có nhiều số/chỉ số trong 1 câu/tiêu chuẩn: dùng ĐA CLOZE TRONG 1 THẺ (toàn bộ {{c1::...}}).
- Tuyệt đối dùng ký tự Unicode (→, ≥, ≤, ×, µg, µmol/L, %), không dùng LaTeX bị lỗi font/hiển thị.
- Xuất file .cards.v2.json và .apkg đầy đủ cho thư mục bài học và outputs/.
"""
import json
import genanki
from pathlib import Path

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\06_Than_Tim_mach_Noi_tiet\PED-40_Hoi_chung_than_hu_nguyen_phat")
OUTPUTS_DIR = TARGET_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #090e17;
  padding: 20px;
  max-width: 680px;
  margin: 0 auto;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.badge-basic {
  background-color: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.4);
}
.badge-cloze {
  background-color: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 14px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 14px 16px;
  border-left: 3px solid #38bdf8;
  margin-top: 10px;
  font-size: 14.5px;
}
.cloze {
  font-weight: 700;
  color: #38bdf8;
  border-bottom: 2px solid #0284c7;
  padding: 0 3px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(245, 158, 11, 0.08);
  border-left: 3px solid #f59e0b;
  font-size: 13.5px;
  color: #cbd5e1;
}
.extra-title {
  font-weight: 700;
  color: #fbbf24;
  margin-bottom: 4px;
}
"""

BASIC_MODEL = genanki.Model(
    1709401001,
    'PED40_Basic_Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Extra'},
        {'name': 'Category'},
    ],
    templates=[{
        'name': 'PED40 Basic Card',
        'qfmt': '<div class="badge badge-basic">📘 PED-40 • {{Category}}</div><div class="question">{{Front}}</div>',
        'afmt': '<div class="badge badge-basic">📘 PED-40 • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">⚠️ BẪY LÂM SÀNG & LƯU Ý CỐT LÕI:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE
)

CLOZE_MODEL = genanki.Model(
    1709401002,
    'PED40_Cloze_Model',
    model_type=genanki.Model.CLOZE,
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
        {'name': 'Category'},
    ],
    templates=[{
        'name': 'PED40 Multi-Cloze Card',
        'qfmt': '<div class="badge badge-cloze">⚡ PED-40 • {{Category}}</div><div class="question">{{cloze:Text}}</div>',
        'afmt': '<div class="badge badge-cloze">⚡ PED-40 • {{Category}}</div><div class="question">{{cloze:Text}}</div><hr id="answer">{{#Extra}}<div class="extra-box"><div class="extra-title">💡 GIẢI THÍCH LÂM SÀNG & EBM:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE
)

cards_data = [
    # -------------------------------------------------------------------------
    # PHẦN 1: CẢNH BÁO AN TOÀN & LƯU ĐỒ CẤP CỨU TẠI GIƯỜNG
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Cảnh báo an toàn",
        "front": "Tại sao chống chỉ định tuyệt đối dùng Furosemid đơn độc ở trẻ hội chứng thận hư đang có giảm thể tích tuần hoàn?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Trẻ hội chứng thận hư dù phù toàn thân nhưng thể tích nội mạch thực tế có thể đang bị cạn kiệt nặng (hiện tượng Underfill).<br>• Dùng Furosemid đơn độc khi mạch nhanh nhỏ, CRT kéo dài, chi lạnh hoặc huyết áp tụt sẽ đẩy trẻ vào sốc giảm thể tích mất bù, tắc mạch huyết khối lan tỏa và suy thận cấp hoại tử ống thận cấp.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Thiểu niệu trong trường hợp này là phản xạ bù trừ sinh mạng của thận nhằm giữ lại thể tích dịch nội mạch ít ỏi. Cưỡng bức bài niệu bằng Furosemid sẽ triệt tiêu phản xạ bù trừ này, làm sập hoàn toàn huyết động.",
        "extra": "Chỉ được dùng Furosemid sau khi đã truyền ít nhất 1/2 chai Albumin 20% và tưới máu mô đã cải thiện rõ (CRT < 2s, mạch chậm lại)."
    },
    {
        "type": "basic",
        "category": "Cảnh báo an toàn",
        "front": "Căn nguyên vi khuẩn hàng đầu gây viêm phúc mạc tiên phát ở trẻ em mắc hội chứng thận hư là gì và tại sao trẻ lại có nguy cơ cao?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Căn nguyên hàng đầu: Phế cầu khuẩn (<i>Streptococcus pneumoniae</i>), chiếm trên 50% các trường hợp.<br>• Nguyên nhân nguy cơ cao: Do trẻ bị thất thoát một lượng khổng lồ kháng thể IgG và các yếu tố bổ thể (Yếu tố B, Yếu tố D) qua nước tiểu, làm suy giảm nghiêm trọng khả năng opsonin hóa các vi khuẩn có vỏ bọc.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bất kỳ trẻ thận hư nào có báng bụng kèm sốt, đau bụng hoặc tăng cảm ứng phúc mạc phải được chọc dò dịch báng, cấy máu và dùng ngay Ceftriaxone tĩnh mạch liều cao (80-100 mg/kg/ngày).",
        "extra": "Tránh nhầm lẫn đau bụng do viêm phúc mạc tiên phát với đau bụng do phù nề niêm mạc ruột. Không được phẫu thuật mở bụng thăm dò vì làm tăng nguy cơ nhiễm trùng và sốc."
    },
    {
        "type": "basic",
        "category": "Cảnh báo an toàn",
        "front": "Các yếu tố nguy cơ độc lập hàng đầu gây biến chứng tắc mạch huyết khối ở trẻ mắc hội chứng thận hư là gì?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Lứa tuổi: Trẻ lớn trên 12 tuổi có nguy cơ cao vượt trội.<br>• Mức độ giảm Albumin máu: Albumin huyết thanh < 20 g/L (đặc biệt nguy kịch khi < 15 g/L).<br>• Mức độ cô đặc máu: Hematocrit > 45%.<br>• Mức độ tăng đông: Fibrinogen huyết tương > 6 g/L và Antithrombin III giảm < 60%.<br>• Yếu tố can thiệp: Đặt catheter tĩnh mạch trung tâm (CVC).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Tình trạng tăng đông là hậu quả của bộ ba Virchow: mất yếu tố chống đông (AT III, Protein S) qua nước tiểu + gan tăng tổng hợp fibrinogen bù trừ + cô đặc máu do dịch thoát vào khoang kẽ.",
        "extra": "Hạn chế tối đa đặt catheter tĩnh mạch trung tâm ở trẻ thận hư nếu không thực sự bắt buộc."
    },
    {
        "type": "basic",
        "category": "Cảnh báo an toàn",
        "front": "Tại sao chống chỉ định ngừng đột ngột Prednisolone sau đợt điều trị tấn công ở trẻ hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Tuyến thượng thận của trẻ bị ức chế hoàn toàn sau 2 tuần dùng Prednisolone liều cao hàng ngày.<br>• Tự ý bỏ thuốc hoặc cắt liều đột ngột sẽ dẫn đến cơn suy thượng thận cấp kịch phát (Adrenal Crisis) với trụy mạch, tụt huyết áp, hạ đường huyết và tử vong nhanh chóng.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Sau khi hoàn thành 4-6 tuần liều tấn công hàng ngày, bắt buộc phải chuyển sang phác đồ duy trì cách ngày (Alternate-day) trong 4-6 tuần để kích thích trục hạ đồi - tuyến yên - thượng thận phục hồi dần chức năng.",
        "extra": "Dấu hiệu hội chứng Cushing (mặt tròn như mặt trăng, rậm lông) là tác dụng phụ dự kiến, không được vì hoảng sợ mà ngừng thuốc đột ngột."
    },

    # -------------------------------------------------------------------------
    # PHẦN 2: DỊCH TỄ HỌC & GIẢI PHẪU SINH LÝ BỆNH MÀNG LỌC
    # -------------------------------------------------------------------------
    {
        "type": "cloze",
        "category": "Dịch tễ học",
        "text": "Theo IPNA 2023, tỷ lệ mới mắc hàng năm của hội chứng thận hư nguyên phát ở trẻ em là {{c1::1.15 đến 16.9 trên 100,000 trẻ}}, đỉnh tuổi mắc bệnh phổ biến nhất từ {{c1::2 đến 6 tuổi}}, với tỷ lệ trai:gái khoảng {{c1::2:1}}.",
        "extra": "Ở trẻ em dưới 10 tuổi, Bệnh tổn thương tối thiểu (MCD) chiếm ưu thế tuyệt đối (85-90%)."
    },
    {
        "type": "cloze",
        "category": "Mô bệnh học",
        "text": "Ở trẻ dưới 10 tuổi mắc hội chứng thận hư nguyên phát, bệnh tổn thương tối thiểu (MCD) chiếm {{c1::85% đến 90%}}, trong khi xơ chai cầu thận khu trú từng phần (FSGS) chiếm {{c1::10% đến 15%}}.",
        "extra": "FSGS thường gặp hơn ở trẻ lớn trên 10-12 tuổi và có tỷ lệ kháng thuốc steroid rất cao."
    },
    {
        "type": "basic",
        "category": "Giải phẫu màng lọc",
        "front": "Hàng rào lọc cầu thận (Glomerular Filtration Barrier) gồm những lớp giải phẫu nào và vai trò của từng lớp?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Lớp tế bào nội mô mao mạch (Endothelial cells): Có nhiều lỗ thủng đường kính 70-100 nm, phủ glycocalyx tích điện âm mạnh ngăn tế bào máu và đại phân tử.<br>• Màng đáy cầu thận (GBM): Cấu trúc ngoại bào dày 250-350 nm cấu tạo từ Collagen type IV, Laminin-521 và Heparan sulfate proteoglycan; ngăn phân tử > 70 kDa và tích điện âm.<br>• Lớp tế bào có chân (Podocytes): Chân thứ cấp cài lồng vào nhau, liên kết bởi màng ngăn có chân (slit diaphragm) có khe lọc siêu vi 4-40 nm.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Màng ngăn slit diaphragm là cửa ngõ cuối cùng và quan trọng nhất quyết định tính chọn lọc kích thước và điện tích của màng lọc cầu thận.",
        "extra": ""
    },
    {
        "type": "basic",
        "category": "Sinh lý bệnh podocyte",
        "front": "Vai trò của phức hợp protein Nephrin và Podocin tại màng ngăn có chân (Slit Diaphragm) là gì?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Nephrin (mã hóa bởi gen NPHS1): Glycoprotein xuyên màng vươn ra khoang khe lọc, đan chéo với nephrin đối diện tạo thành bộ khung mắt lưới chính của khe lọc.<br>• Podocin (mã hóa bởi gen NPHS2): Protein màng dạng kẹp tóc tại bè lipid, có nhiệm vụ neo giữ, tập hợp và điều hòa tín hiệu của Nephrin và CD2AP với khung xương sợi actin nội bào.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Đột biến gen NPHS1 gây hội chứng thận hư bẩm sinh kiểu Phần Lan; đột biến gen NPHS2 gây hội chứng thận hư kháng steroid có tính gia đình, không đáp ứng với ức chế miễn dịch.",
        "extra": ""
    },
    {
        "type": "basic",
        "category": "Sinh lý bệnh",
        "front": "Phân biệt cơ chế phù theo Thuyết Underfill và Thuyết Overfill trong hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Thuyết Underfill (Chiếm đa số ở trẻ nhỏ MCD): Giảm albumin máu nặng → Giảm áp lực keo huyết tương → Dịch thoát ra khoang kẽ → Giảm thể tích tuần hoàn hiệu dụng → Kích hoạt hệ RAAS giữ muối nước bù trừ → Mạch nhanh, CRT kéo dài, chi lạnh, HA thấp. Nguy cơ sốc nếu dùng lợi tiểu đơn độc.<br>• Thuyết Overfill (Trẻ lớn, FSGS, viêm cầu thận): Khiếm khuyết bài tiết Natri nguyên phát tại ống góp (kênh ENaC) → Ứ muối nước nguyên phát → Tăng thể tích tuần hoàn hiệu dụng → Ức chế RAAS → Huyết áp cao, tĩnh mạch cổ nổi, tim gallop T3. Đáp ứng tốt với lợi tiểu đơn độc.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Đa số trẻ em mắc MCD thuộc nhóm Underfill, do đó việc đánh giá huyết động và tưới máu ngoại vi trước khi kê đơn là bắt buộc.",
        "extra": ""
    },

    # -------------------------------------------------------------------------
    # PHẦN 3: 4 TIÊU CHUẨN CHẨN ĐOÁN KINH ĐIỂN THEO IPNA / KDIGO
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Tiêu chuẩn chẩn đoán",
        "front": "Nêu đầy đủ 4 tiêu chuẩn chẩn đoán kinh điển của Hội chứng thận hư theo khuyến cáo quốc tế IPNA và KDIGO?",
        "back": "<b>📖 Văn bản gốc:</b><br>• 1. Phù: Phù trắng, mềm, ấn lõm, đối xứng, xuất hiện đầu tiên ở mi mắt/mặt vào buổi sáng, sau đó lan toàn thân kèm tràn dịch đa màng.<br>• 2. Protein niệu ngưỡng thận hư (BẮT BUỘC): Protein niệu 24h ≥ 50 mg/kg/ngày (hoặc ≥ 40 mg/m2/giờ) HOẶC Up/Ucr sáng sớm ≥ 2.0 mg/mg (≥ 200 mg/mmol) HOẶC que thử 3+ đến 4+.<br>• 3. Giảm Albumin máu nặng (BẮT BUỘC): Albumin huyết thanh < 25 g/L (< 2.5 g/dL) kèm Protein toàn phần < 55 g/L.<br>• 4. Tăng Lipid máu: Cholesterol toàn phần > 5.2 mmol/L (> 200 mg/dL), kèm tăng Triglyceride, VLDL, LDL.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Trong 4 tiêu chuẩn trên, Protein niệu ngưỡng thận hư và Giảm Albumin máu < 25 g/L là hai tiêu chuẩn sinh hóa bắt buộc để xác định bệnh.",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Tiêu chuẩn sinh hóa",
        "text": "Tiêu chuẩn bắt buộc chẩn đoán hội chứng thận hư gồm Protein niệu 24 giờ đạt ≥ {{c1::50 mg/kg/ngày}} (hoặc tỷ số Up/Ucr sáng sớm ≥ {{c1::2.0 mg/mg}}) kết hợp nồng độ Albumin huyết thanh giảm xuống < {{c1::25 g/L}}.",
        "extra": "Mốc Albumin < 25 g/L là tiêu chuẩn cập nhật thống nhất của IPNA 2023 và KDIGO 2021 (thay cho mốc cũ < 30 g/L)."
    },
    {
        "type": "cloze",
        "category": "Tiêu chuẩn bán định lượng",
        "text": "Trên que thử nước tiểu bán định lượng (dipstick), kết quả protein niệu gợi ý ngưỡng thận hư dao động liên tục từ {{c1::3+ (300 mg/dL)}} đến {{c1::4+ (≥ 1000 mg/dL)}}.",
        "extra": "Que thử là công cụ đầu tay quan trọng tại phòng khám cấp cứu và phương tiện cho gia đình theo dõi tái phát tại nhà."
    },
    {
        "type": "cloze",
        "category": "Tiêu chuẩn mỡ máu",
        "text": "Tiêu chuẩn rối loạn lipid máu trong hội chứng thận hư ở trẻ em được xác định khi Cholesterol toàn phần trong máu > {{c1::5.2 mmol/L}} (tương đương > {{c1::200 mg/dL}}).",
        "extra": "Tăng lipid máu là hậu quả của gan tăng tổng hợp lipoprotein bù trừ khi áp lực keo huyết tương sụt giảm nghiêm trọng."
    },
    {
        "type": "basic",
        "category": "Phương pháp đo lường",
        "front": "Ưu điểm của tỷ số Protein/Creatinin nước tiểu ngẫu nhiên buổi sáng (Up/Ucr) so với thu thập nước tiểu 24 giờ ở trẻ nhỏ là gì?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Thu thập nước tiểu 24 giờ ở trẻ nhỏ chưa tự chủ tiểu tiện (chưa bỏ tã) cực kỳ khó khăn, dễ rơi vãi sai số và làm chậm trễ thời gian xử trí cấp cứu.<br>• Tỷ số Up/Ucr lấy mẫu nước tiểu đầu tiên vào buổi sáng có độ tương quan rất cao với protein niệu 24 giờ.<br>• Ngưỡng Up/Ucr ≥ 2.0 mg/mg (hoặc ≥ 200 mg/mmol) đại diện chính xác cho protein niệu ngưỡng thận hư (≥ 50 mg/kg/ngày).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Ở trẻ khỏe mạnh bình thường, Up/Ucr < 0.2 mg/mg (ở trẻ dưới 2 tuổi < 0.5 mg/mg).",
        "extra": ""
    },

    # -------------------------------------------------------------------------
    # PHẦN 4: 7 CHỈ ĐỊNH SINH THIẾT THẬN THEO IPNA / KDIGO
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Chỉ định sinh thiết thận",
        "front": "Tại sao không chỉ định sinh thiết thận thường quy ở thời điểm chẩn đoán ban đầu cho trẻ từ 1 đến 10 tuổi mắc hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Trên 85% đến 90% trẻ em khởi phát hội chứng thận hư trong độ tuổi 1-10 tuổi mắc bệnh tổn thương tối thiểu (MCD).<br>• MCD có đặc tính sinh học là đáp ứng hoàn toàn với liệu pháp điều trị bằng Glucocorticoid đường uống (> 90%).<br>• Sinh thiết thận là thủ thuật xâm lấn có nguy cơ chảy máu, tụ máu quanh thận và đái máu, do đó không cần thiết ở nhóm tuổi điển hình này.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Chỉ định sinh thiết chỉ đặt ra khi có các dấu hiệu cảnh báo bệnh lý cầu thận phức tạp (ngoài MCD) hoặc khi thất bại với điều trị steroid chuẩn.",
        "extra": ""
    },
    {
        "type": "basic",
        "category": "Chỉ định sinh thiết thận",
        "front": "Kể tên 7 chỉ định sinh thiết thận bắt buộc trong hội chứng thận hư trẻ em theo khuyến cáo IPNA và KDIGO?",
        "back": "<b>📖 Văn bản gốc:</b><br>• 1. Tuổi khởi phát không điển hình: Dưới 1 tuổi (nghi ngờ đột biến gen) hoặc trên 12 tuổi (nguy cơ cao FSGS, bệnh thận màng, Lupus).<br>• 2. Đái máu đại thể dai dẳng.<br>• 3. Tăng huyết áp thực tổn kéo dài (HA > bách phân vị thứ 95).<br>• 4. Suy giảm chức năng thận thực tổn (Creatinin tăng, eGFR giảm dai dẳng sau khi đã bù đủ thể tích tuần hoàn).<br>• 5. Giảm nồng độ bổ thể C3 hoặc C4 huyết thanh.<br>• 6. Biểu hiện lâm sàng ngoài thận gợi ý bệnh thứ phát (ban cánh bướm, sốt kéo dài, loét miệng, viêm khớp, ban Henoch).<br>• 7. Hội chứng thận hư kháng steroid (SRNS): Không lui bệnh sau 4 tuần tấn công Prednisolone liều chuẩn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Sinh thiết thận ở nhóm kháng steroid là bắt buộc trước khi chuyển sang các thuốc ức chế miễn dịch bậc hai (CNI, MMF) để xác định thể mô bệnh học (MCD vs FSGS) và đánh giá mức độ xơ hóa mô kẽ.",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Chỉ định sinh thiết thận",
        "text": "Hai mốc tuổi khởi phát không điển hình bắt buộc phải sinh thiết thận ở trẻ mắc hội chứng thận hư là trẻ dưới {{c1::1 tuổi}} (nghi hội chứng thận hư bẩm sinh/đột biến gen) và trẻ trên {{c1::12 tuổi}} (nguy cơ cao FSGS và Lupus).",
        "extra": "Trẻ 1-12 tuổi có biểu hiện lâm sàng kinh điển được điều trị thử bằng Prednisolone mà không cần sinh thiết thận trước."
    },

    # -------------------------------------------------------------------------
    # PHẦN 5: PHÁC ĐỒ CORTICOID ĐỢT ĐẦU THEO IPNA 2023 & KDIGO 2021
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Phác đồ điều trị đợt đầu",
        "front": "Trình bày chi tiết phác đồ điều trị tấn công hàng ngày bằng Prednisolone cho đợt khởi phát ban đầu theo IPNA 2023?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Liều lượng: 2.0 mg/kg/ngày tính theo cân nặng HOẶC 60 mg/m2/ngày tính theo diện tích da.<br>• Liều tối đa tuyệt đối: Không vượt quá 60 mg/ngày.<br>• Cách dùng: Uống một lần duy nhất vào buổi sáng (khoảng 7:00 - 8:00 sáng sau ăn no).<br>• Thời gian điều trị tấn công: Kéo dài liên tục trong 4 tuần (có thể kéo dài tối đa 6 tuần nếu đang đáp ứng nhưng chưa âm tính hẳn).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Uống 1 lần vào buổi sáng mô phỏng nhịp sinh học tiết cortisol tự nhiên của vỏ thượng thận, giúp giảm thiểu tối đa nguy cơ ức chế trục hạ đồi - tuyến yên - thượng thận (HPA axis).",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Phác đồ điều trị đợt đầu",
        "text": "Liều tấn công hàng ngày của Prednisolone trong đợt đầu là {{c1::2.0 mg/kg/ngày}} (hoặc {{c1::60 mg/m2/ngày}}), liều tối đa không vượt quá {{c1::60 mg/ngày}}, dùng liên tục trong {{c1::4 đến 6 tuần}}.",
        "extra": "Tính theo diện tích da (60 mg/m2) chuẩn xác hơn ở trẻ béo phì hoặc thừa cân để tránh quá liều thuốc."
    },
    {
        "type": "basic",
        "category": "Phác đồ điều trị đợt đầu",
        "front": "Trình bày phác đồ điều trị duy trì cách ngày (Alternate-day) bằng Prednisolone sau giai đoạn tấn công?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Liều lượng: 1.5 mg/kg cách ngày HOẶC 40 mg/m2 cách ngày.<br>• Liều tối đa tuyệt đối: Không vượt quá 40 mg/ngày.<br>• Cách dùng: Uống một lần duy nhất vào buổi sáng của ngày chỉ định (ví dụ sáng thứ 2, 4, 6, chủ nhật; các ngày còn lại nghỉ hoàn toàn).<br>• Thời gian duy trì: Kéo dài trong 4 tuần đến 6 tuần.<br>• Quy trình ngưng: Giảm dần liều mỗi 1-2 tuần rồi ngưng hẳn HOẶC ngưng trực tiếp theo protocol rút gọn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Tổng thời gian điều trị toàn bộ đợt đầu thống nhất từ 8 đến 12 tuần (khoảng 2 đến 3 tháng).",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Phác đồ điều trị đợt đầu",
        "text": "Liều duy trì cách ngày của Prednisolone là {{c1::1.5 mg/kg cách ngày}} (hoặc {{c1::40 mg/m2 cách ngày}}), liều tối đa không vượt quá {{c1::40 mg/ngày}}, duy trì trong {{c1::4 đến 6 tuần}}.",
        "extra": "Chế độ cách ngày cho phép tuyến thượng thận của trẻ tự sản xuất cortisol nội sinh vào ngày nghỉ thuốc, phục hồi dần chức năng vỏ thượng thận."
    },
    {
        "type": "basic",
        "category": "Bằng chứng EBM Cochrane",
        "front": "Kết luận cốt lõi từ phân tích gộp Cochrane 2020 về thời gian điều trị corticosteroid đợt đầu ở trẻ em là gì?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Phân tích các RCT nguy cơ sai lệch thấp (như PREDNOS) khẳng định: Kéo dài thời gian điều trị trên 2-3 tháng (8-12 tuần) KHÔNG LÀM GIẢM nguy cơ tái phát so với phác đồ chuẩn 2-3 tháng (RR = 0.95, 95% CI: 0.81 - 1.12).<br>• Tỷ lệ duy trì lui bệnh sau 12-24 tháng theo dõi là tương đương nhau giữa nhóm 2-3 tháng và nhóm kéo dài 6 tháng.<br>• Nhóm kéo dài thời gian điều trị phải chịu tổng liều corticoid tích lũy cao hơn rõ rệt, làm gia tăng nghiêm trọng các tác dụng phụ: chậm lớn, béo phì Cushing, tăng huyết áp.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bằng chứng y văn quốc tế khẳng định thời gian chuẩn hóa đợt đầu là 8 đến 12 tuần, tuyệt đối không kéo dài quá 3 tháng một cách không cần thiết.",
        "extra": ""
    },

    # -------------------------------------------------------------------------
    # PHẦN 6: ĐỊNH NGHĨA ĐÁP ỨNG STEROID THEO IPNA (REMISSION, RELAPSE, FRNS, SDNS, SRNS)
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Định nghĩa đáp ứng",
        "front": "Định nghĩa Lui bệnh hoàn toàn (Complete Remission) và Tái phát (Relapse) theo khuyến cáo IPNA 2020/2023?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Lui bệnh hoàn toàn (Complete Remission): Tỷ số Up/Ucr < 0.2 mg/mg (hoặc < 20 mg/mmol) HOẶC que thử nước tiểu cho kết quả âm tính hoặc vết (trace) liên tục trong 3 ngày liên tiếp.<br>• Tái phát (Relapse): Tỷ số Up/Ucr ≥ 2.0 mg/mg (hoặc ≥ 200 mg/mmol) HOẶC que thử nước tiểu ≥ 3+ liên tục trong 3 ngày liên tiếp ở bệnh nhân trước đó đã đạt lui bệnh hoàn toàn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Nếu que thử chỉ xuất hiện 1+ hoặc 2+ trong đợt sốt nhiễm siêu vi, chưa gọi là tái phát; cần tiếp tục theo dõi nước tiểu mỗi sáng trong vài ngày.",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Định nghĩa đáp ứng",
        "text": "Lui bệnh hoàn toàn được xác định khi tỷ số Up/Ucr < {{c1::0.2 mg/mg}} hoặc que thử âm tính/vết liên tục trong {{c1::3 ngày}}; Tái phát được xác định khi Up/Ucr ≥ {{c1::2.0 mg/mg}} hoặc que thử ≥ {{c1::3+}} liên tục trong {{c1::3 ngày}}.",
        "extra": "Lui bệnh một phần (Partial Remission): Up/Ucr từ 0.2 đến 2.0 mg/mg kèm Albumin máu ≥ 30 g/L."
    },
    {
        "type": "basic",
        "category": "Định nghĩa đáp ứng",
        "front": "Định nghĩa Thể tái phát thường xuyên (FRNS) và Thể phụ thuộc steroid (SDNS) theo chuẩn quốc tế IPNA?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Thể tái phát thường xuyên (Frequently Relapsing Nephrotic Syndrome - FRNS): Xuất hiện ≥ 2 đợt tái phát trong vòng 6 tháng kể từ khi khởi phát bệnh HOẶC ≥ 4 đợt tái phát trong bất kỳ khoảng thời gian 12 tháng nào.<br>• Thể phụ thuộc steroid (Steroid-Dependent Nephrotic Syndrome - SDNS): Xuất hiện 2 đợt tái phát liên tiếp trong khi đang giảm dần liều steroid HOẶC trong vòng 14 ngày (2 tuần) sau khi ngưng thuốc hoàn toàn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Cả hai thể FRNS và SDNS đều có nguy cơ ngộ độc steroid cao do phải dùng lặp đi lặp lại nhiều đợt tấn công, là chỉ định bắt buộc dùng thuốc ức chế miễn dịch bậc hai (Steroid-sparing agents).",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Định nghĩa đáp ứng",
        "text": "Thể tái phát thường xuyên (FRNS) được định nghĩa khi có ≥ {{c1::2 đợt}} tái phát trong 6 tháng đầu hoặc ≥ {{c1::4 đợt}} tái phát trong 12 tháng; Thể phụ thuộc steroid (SDNS) là tái phát {{c1::2 đợt liên tiếp}} khi đang giảm liều hoặc trong vòng {{c1::14 ngày}} sau ngừng thuốc.",
        "extra": "Khoảng 50% trẻ có hội chứng thận hư nhạy cảm steroid sẽ diễn tiến thành thể FRNS hoặc SDNS."
    },
    {
        "type": "basic",
        "category": "Định nghĩa đáp ứng",
        "front": "Định nghĩa Hội chứng thận hư kháng steroid (Steroid-Resistant Nephrotic Syndrome - SRNS) theo IPNA 2020?",
        "back": "<b>📖 Văn bản gốc:</b><br>• SRNS được định nghĩa khi bệnh nhân thất bại trong việc đạt lui bệnh hoàn toàn sau 4 tuần điều trị liên tục bằng Prednisolone liều chuẩn hàng ngày (60 mg/m2/ngày hoặc 2 mg/kg/ngày).<br>• Phải đảm bảo trẻ đã uống đúng liều, không bị nôn ói và không có ổ nhiễm trùng tiềm ẩn cản trở đáp ứng.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Khi xác định SRNS, bắt buộc thực hiện sinh thiết thận và xét nghiệm di truyền học tìm đột biến gen podocyte trước khi khởi động thuốc ức chế miễn dịch bậc hai (Calcineurin Inhibitor).",
        "extra": "Không được kết luận kháng thuốc quá sớm trước khi đủ 4 tuần điều trị tấn công."
    },

    # -------------------------------------------------------------------------
    # PHẦN 7: XỬ TRÍ BIẾN CHỨNG CẤP TÍNH (SỐC GIẢM THỂ TÍCH, SBP, TẮC MẠCH, CANXI)
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Cấp cứu biến chứng",
        "front": "Quy trình cấp cứu 2 bước giảm thể tích tuần hoàn ở trẻ mắc hội chứng thận hư theo IPNA và SINePe?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Bước 1 — Phục hồi thể tích nội mạch: Truyền tĩnh mạch dung dịch Albumin 20% liều 0.5 - 1.0 g/kg (tương đương 2.5 - 5.0 mL/kg) truyền chậm qua bơm tiêm điện trong 2 đến 4 giờ. (Nếu sốc mất bù, truyền nhanh NaCl 0.9% 10-20 mL/kg trước trong khi chuẩn bị Albumin).<br>• Bước 2 — Thúc đẩy bài niệu bằng Lợi tiểu quai: CHỈ DÙNG khi đã truyền được ít nhất 1/2 chai Albumin và huyết động đã cải thiện rõ rệt. Dùng Furosemid 1.0 - 2.0 mg/kg tiêm TM chậm vào giữa hoặc cuối buổi truyền Albumin.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Theo dõi sát nhịp thở, SpO2, mạch, huyết áp mỗi 15-30 phút trong quá trình truyền để phát hiện sớm biến chứng quá tải tuần hoàn cấp và phù phổi cấp.",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Cấp cứu biến chứng",
        "text": "Liều truyền dung dịch Albumin 20% trong cấp cứu giảm thể tích tuần hoàn là {{c1::0.5 đến 1.0 g/kg}} (tương đương {{c1::2.5 đến 5.0 mL/kg}}), truyền chậm trong {{c1::2 đến 4 giờ}}; sau đó tiêm Furosemid liều {{c1::1.0 đến 2.0 mg/kg TM}}.",
        "extra": "Tuyệt đối không tiêm Furosemid trước khi bù Albumin vì sẽ gây sốc tụt huyết áp và hoại tử ống thận cấp."
    },
    {
        "type": "basic",
        "category": "Cấp cứu nhiễm trùng",
        "front": "Phác đồ điều trị kháng sinh cấp cứu viêm phúc mạc tiên phát (SBP) ở trẻ mắc hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Kháng sinh đầu tay: Ceftriaxone 80 - 100 mg/kg/ngày tiêm TM 1 lần/ngày HOẶC Cefotaxime 150 mg/kg/ngày chia 3 lần.<br>• Phối hợp: Bổ sung Vancomycin 40 - 60 mg/kg/ngày nếu nghi ngờ phế cầu kháng penicillin hoặc bệnh nhân trong tình trạng sốc nhiễm khuẩn.<br>• Thời gian điều trị: Tối thiểu 10 đến 14 ngày.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bắt buộc cấy máu và chọc dò màng bụng xét nghiệm tế bào (bạch cầu > 250/mm3 với ưu thế đa nhân) trước khi tiêm liều kháng sinh đầu tiên.",
        "extra": ""
    },
    {
        "type": "basic",
        "category": "Rối loạn điện giải",
        "front": "Giải thích hiện tượng hạ canxi máu giả tạo trong hội chứng thận hư và công thức hiệu chỉnh canxi theo albumin máu?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Cơ chế: Khoảng 40% canxi toàn phần trong máu gắn với Albumin. Khi Albumin giảm sâu, lượng canxi gắn kết giảm làm Canxi toàn phần xét nghiệm giảm thấp (&lt; 2.0 mmol/L). Tuy nhiên, Canxi ion hóa (Ca2+) có hoạt tính sinh học thường vẫn hoàn toàn bình thường (1.15 - 1.30 mmol/L).<br>• Công thức hiệu chỉnh: Canxi hiệu chỉnh (mmol/L) = Canxi đo được (mmol/L) + 0.02 × (40 - Albumin máu (g/L)).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Chống chỉ định tiêm canxi tĩnh mạch nếu trẻ không có triệu chứng lâm sàng (Chvostek, Trousseau, co giật) và canxi ion hóa bình thường.",
        "extra": "Tiêm canxi tĩnh mạch bừa bãi có thể gây rối loạn nhịp tim nguy hiểm và hoại tử mô nếu thoát mạch."
    },
    {
        "type": "basic",
        "category": "Biến chứng tắc mạch",
        "front": "Chỉ định dự phòng chống đông và các thuốc được lựa chọn ở trẻ mắc hội chứng thận hư có nguy cơ tắc mạch cao?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Chỉ định: Trẻ có nguy cơ rất cao (tuổi > 12 tuổi, Albumin máu &lt; 15-20 g/L, Fibrinogen > 6 g/L, có đặt catheter tĩnh mạch trung tâm hoặc có tiền sử huyết khối).<br>• Thuốc lựa chọn:<br>  - Aspirin liều thấp: 2 - 5 mg/kg/ngày (tối đa 81 - 100 mg/ngày) đường uống.<br>  - HOẶC Enoxaparin (LMWH): 1 mg/kg tiêm dưới da mỗi 12-24 giờ.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bên cạnh thuốc, các biện pháp không dùng thuốc tối quan trọng gồm: vận động sớm, bù đủ dịch tránh cô đặc máu và rút sớm catheter tĩnh mạch trung tâm.",
        "extra": ""
    },
    # PHẦN 8: THUỐC ỨC CHẾ MIỄN DỊCH BẬC HAI (STEROID-SPARING AGENTS)
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Thuốc bậc hai",
        "front": "Kể tên các nhóm thuốc ức chế miễn dịch bậc hai (Steroid-sparing agents) và chỉ định ưu tiên của từng thuốc trong hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Levamisole (2.5 mg/kg cách ngày): Lựa chọn đầu tay cho thể FRNS hoặc SDNS mức độ nhẹ, độc tính thấp nhất.<br>• Cyclophosphamide (2.0 mg/kg/ngày trong 8-12 tuần): Chỉ định cho thể FRNS/SDNS sau khi đã đạt lui bệnh bằng steroid.<br>• Cyclosporin A (4-5 mg/kg/ngày) & Tacrolimus (0.10-0.15 mg/kg/ngày): Thuốc ức chế calcineurin (CNI), lựa chọn hàng đầu cho thể kháng steroid (SRNS) và SDNS nặng.<br>• Mycophenolate Mofetil - MMF (1200 mg/m2/ngày): Thuốc tiết kiệm steroid hiệu quả cao cho SDNS/FRNS, không gây độc thận.<br>• Rituximab (375 mg/m2/liều TM): Kháng thể kháng CD20, chỉ định cho SDNS kháng trị hoặc phụ thuộc CNI liều cao.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Tacrolimus được ưu tiên hơn Cyclosporin A ở trẻ em vì ít gây phì đại nướu và không gây rậm lông.",
        "extra": ""
    },
    {
        "type": "cloze",
        "category": "Thuốc bậc hai",
        "text": "Để phòng ngừa vô sinh vĩnh viễn và viêm bàng quang xuất huyết khi dùng Cyclophosphamide, tổng liều tích lũy tuyệt đối không được vượt quá {{c1::168 mg/kg}} (tương đương liều {{c1::2.0 mg/kg/ngày}} dùng trong tối đa {{c1::12 tuần}}).",
        "extra": "Cần cho trẻ uống nhiều nước và đi tiểu thường xuyên trong quá trình dùng thuốc để tránh tích tụ acrolein tại bàng quang."
    },
    {
        "type": "cloze",
        "category": "Thuốc bậc hai",
        "text": "Nồng độ đáy mục tiêu (C0) trong máu của Cyclosporin A là {{c1::100 đến 150 ng/mL}}, trong khi nồng độ đáy mục tiêu của Tacrolimus là {{c1::5 đến 8 ng/mL}} trong 6 tháng đầu điều trị SRNS.",
        "extra": "Cả hai thuốc CNI đều có nguy cơ độc tính trên thận (gây co thắt tiểu động mạch vào và xơ hóa mô kẽ), cần theo dõi sát creatinin máu."
    },
    {
        "type": "cloze",
        "category": "Thuốc bậc hai",
        "text": "Liều điều trị của Mycophenolate Mofetil (MMF) ở trẻ mắc thể SDNS/FRNS là {{c1::1200 mg/m2/ngày}} (hoặc {{c1::30 mg/kg/ngày}}) chia làm 2 lần uống, ưu điểm nổi bật là {{c1::không gây độc tính trên thận}}.",
        "extra": "Tác dụng phụ thường gặp nhất của MMF là rối loạn tiêu hóa (tiêu chảy, đau quặn bụng) và giảm bạch cầu."
    },
    {
        "type": "basic",
        "category": "Thuốc sinh học",
        "front": "Cơ chế tác dụng và chỉ định của Rituximab trong hội chứng thận hư ở trẻ em?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Cơ chế: Rituximab là một kháng thể đơn dòng tái tổ hợp kháng kháng nguyên CD20 trên bề mặt tế bào lympho B, gây ly giải và làm suy giảm tạm thời dòng lympho B (mục tiêu tế bào B CD19 < 1%), giúp tái lập cân bằng miễn dịch podocyte.<br>• Chỉ định: Dành cho thể phụ thuộc steroid (SDNS) nặng kháng trị hoặc phụ thuộc CNI liều cao có nguy cơ ngộ độc thận.<br>• Liều dùng: 375 mg/m2/liều truyền tĩnh mạch từ 1 đến 4 liều (cách nhau 1 tuần).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Cần theo dõi sát nguy cơ phản ứng phản vệ trong khi truyền và nguy cơ nhiễm trùng cơ hội (viêm phổi do Pneumocystis jirovecii) sau khi dùng thuốc.",
        "extra": ""
    },

    # -------------------------------------------------------------------------
    # PHẦN 9: BÃY LÂM SÀNG & QUẢN LÝ DINH DƯỠNG, TIÊM CHỦNG
    # -------------------------------------------------------------------------
    {
        "type": "basic",
        "category": "Chế độ dinh dưỡng",
        "front": "Nguyên tắc dinh dưỡng về lượng muối và protein cho trẻ mắc hội chứng thận hư trong đợt phù và đợt lui bệnh?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Lượng muối: Ăn nhạt (giảm muối) trong giai đoạn phù to và tăng huyết áp (khoảng 1 - 2 g muối/ngày, tương đương < 35 mg/kg/ngày Natri). Khi đã hết phù và lui bệnh, trở về chế độ ăn bình thường.<br>• Lượng Protein: Duy trì lượng protein chuẩn theo lứa tuổi (1.5 - 2.0 g/kg/ngày). Tuyệt đối KHÔNG kiêng khem đạm nghiêm ngặt (gây suy dinh dưỡng teo cơ) và cũng KHÔNG ép ăn quá nhiều đạm (làm tăng áp lực lọc cầu thận và tổn thương thêm podocyte).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Đảm bảo đủ năng lượng (100 kcal/kg/ngày cho trẻ nhỏ) để hạn chế dị hóa cơ thể.",
        "extra": ""
    },
    {
        "type": "basic",
        "category": "Tiêm chủng vắc xin",
        "front": "Quy tắc tiêm chủng vắc xin cho trẻ mắc hội chứng thận hư đang điều trị thuốc ức chế miễn dịch?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Vắc xin sống giảm độc lực (Sởi, Quai bị, Rubella, Thủy đậu, Lao BCG): CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI khi trẻ đang dùng Prednisolone liều cao (≥ 2 mg/kg/ngày) hoặc các thuốc ức chế miễn dịch khác.<br>• Thời điểm tiêm vắc xin sống: Chỉ được tiêm sau khi đã ngưng hoàn toàn corticoid liều cao ít nhất 1 đến 3 tháng.<br>• Vắc xin bất hoạt (Phế cầu, Cúm mùa, Viêm gan B): Được khuyến cáo tiêm đầy đủ, đặc biệt là vắc xin Phế cầu liên hợp (PCV13) và vắc xin phế cầu đa polysaccharide (PPSV23) để phòng viêm phúc mạc tiên phát.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Người nhà sống cùng nhà với trẻ cũng cần được tiêm phòng cúm và thủy đậu để tạo miễn dịch vòng bảo vệ bệnh nhi.",
        "extra": "Tiêm vắc xin sống khi đang dùng ức chế miễn dịch có thể gây nhiễm virus vắc xin lan tỏa toàn thân dẫn đến tử vong."
    },
    {
        "type": "basic",
        "category": "Tiêu chuẩn xuất viện",
        "front": "Các tiêu chuẩn xuất viện an toàn cho trẻ khởi phát đợt đầu hội chứng thận hư?",
        "back": "<b>📖 Văn bản gốc:</b><br>• 1. Huyết động hoàn toàn ổn định, không còn dấu hiệu giảm thể tích tuần hoàn hay quá tải thể tích.<br>• 2. Phù giảm rõ rệt, trẻ đi tiểu tốt (lượng nước tiểu > 1.5 - 2.0 mL/kg/giờ).<br>• 3. Đã loại trừ hoàn toàn các ổ nhiễm trùng cấp tính (viêm phúc mạc, viêm phổi, viêm mô tế bào).<br>• 4. Trẻ dung nạp tốt với Prednisolone đường uống, không nôn ói.<br>• 5. Gia đình được tập huấn thành thạo kỹ năng thử nước tiểu bằng que thử tại nhà mỗi sáng và nhận biết các dấu hiệu nguy hiểm cần tái khám ngay.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Việc hướng dẫn gia đình tự thử nước tiểu bằng dipstick tại nhà là chìa khóa vàng giúp phát hiện sớm đợt tái phát trước khi trẻ bị phù to.",
        "extra": ""
    }
]

def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    import re
    return re.sub(r'<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr|ul|/ul|li|/li)\b)', '&lt;', text)

def main():
    print(f"=== BẮT ĐẦU ĐÓNG GÓI ANKI PED-40: HỘI CHỨNG THẬN HƯ NGUYÊN PHÁT ===")
    deck_id = 1709402026
    deck_name = "Nhi khoa Lâm sàng - PED-40: Hội chứng thận hư nguyên phát ở trẻ em"
    
    deck = genanki.Deck(deck_id, deck_name)
    
    total_basic = 0
    total_cloze = 0

    for c in cards_data:
        if c["type"] == "basic":
            note = genanki.Note(
                model=BASIC_MODEL,
                fields=[
                    escape_angle_brackets(c["front"]),
                    escape_angle_brackets(c["back"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", "Lâm sàng")
                ],
                tags=["PED-40", "Hoi_chung_than_hu", "Nhi_khoa", "EBM"]
            )
            deck.add_note(note)
            total_basic += 1
        elif c["type"] == "cloze":
            note = genanki.Note(
                model=CLOZE_MODEL,
                fields=[
                    escape_angle_brackets(c["text"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", "Tiêu chuẩn")
                ],
                tags=["PED-40", "Hoi_chung_than_hu", "Nhi_khoa", "Cloze", "EBM"]
            )
            deck.add_note(note)
            total_cloze += 1
    # 1. Xuất file JSON
    json_payload = {
        "topic": "PED-40: Hội chứng thận hư nguyên phát ở trẻ em (Approach to Pediatric Idiopathic Nephrotic Syndrome)",
        "lesson_id": "PED-40",
        "version": "2026-09-21_RELEASE_v1",
        "total_cards": len(cards_data),
        "total_basic": total_basic,
        "total_cloze": total_cloze,
        "cards": cards_data
    }
    
    json_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.cards.v2.json"
    json_path.write_text(json.dumps(json_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Đã lưu file JSON: {json_path} ({len(cards_data)} thẻ: {total_basic} Basic, {total_cloze} Cloze)")

    # 2. Xuất file APKG Release v1
    apkg_release_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.apkg"
    genanki.Package(deck).write_to_file(str(apkg_release_path))
    print(f"✓ Đã xuất APKG Release v1: {apkg_release_path}")

    # 3. Xuất file APKG Master v1
    apkg_master_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_MASTER_v1.apkg"
    genanki.Package(deck).write_to_file(str(apkg_master_path))
    print(f"✓ Đã xuất APKG Master v1: {apkg_master_path}")

    # 4. Sao chép vào outputs/
    output_apkg = OUTPUTS_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.apkg"
    output_json = OUTPUTS_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.cards.v2.json"
    output_apkg.write_bytes(apkg_release_path.read_bytes())
    output_json.write_text(json_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"✓ Đã đồng bộ sang outputs/: {output_apkg}")

    print("=== HOÀN TẤT ĐÓNG GÓI APKG PED-40 THÀNH CÔNG ===")

if __name__ == "__main__":
    main()
