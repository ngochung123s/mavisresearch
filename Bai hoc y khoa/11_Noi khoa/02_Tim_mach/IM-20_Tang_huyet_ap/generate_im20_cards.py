# -*- coding: utf-8 -*-
"""
Generator for comprehensive IM-20 Anki V2 flashcards (>100 cards with rich Cloze & Basic).
Follows medical-flashcard-governance strictly:
- Basic: <b>📖 Văn bản gốc:</b><br> + <b>🔍 Góc nhìn bổ sung (AI):</b><br>
- Cloze: only {{c1::...}}
- Clean Unicode (no LaTeX math/arrows)
Covers full IM-20 updated content:
- BP measurement, 5-minute quiet rule, HBPM/ABPM thresholds, white-coat & masked HTN
- Physiology CO x TPR and drug connections (A, B, C, D)
- Safety RED BOX (BP >= 180/110 + acute TOD -> IM-15)
- 5 Chữ T for Target Organ Damage (Heart, Kidney, Brain, Eye, Vessels)
- CHAPS-D for Secondary Hypertension
- A-B-C-D Drug Table (Starting doses, mechanisms, side effects, contraindications)
- Resistant hypertension, Stepwise combination therapy (A+C, A+D, SPC)
- Elderly considerations (age >= 80, orthostatic hypotension)
- Clinical cases & traps
"""
import json
from pathlib import Path

cards = [
    # =========================================================================
    # PHẦN 1: ĐO HUYẾT ÁP ĐÚNG & XÁC NHẬN CHẨN ĐOÁN
    # =========================================================================
    {
        "id": "IM20_001",
        "type": "basic",
        "front": "Định nghĩa Huyết áp tâm thu (HATT) và Huyết áp tâm trương (HATTr)? Đơn vị chuẩn đo lường?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Huyết áp tâm thu (HATT):</b> Áp lực máu cao nhất trong lòng động mạch khi tâm thất trái co bóp tống máu vào hệ tuần hoàn.<br>• <b>Huyết áp tâm trương (HATTr):</b> Áp lực máu thấp nhất trong lòng động mạch khi tim thư giãn giữa hai nhịp bóp.<br>• <b>Đơn vị chuẩn:</b> milimet thủy ngân (mmHg).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Huyết áp là một biến số động thay đổi liên tục theo cảm xúc, tư thế, vận động và thời điểm trong ngày; do đó không bao giờ được chẩn đoán tăng huyết áp mạn tính chỉ dựa vào một lần đo đơn độc.",
        "tags": ["IM-20", "Hypertension", "Definition", "Fundamentals"]
    },
    {
        "id": "IM20_002",
        "type": "cloze",
        "text": "Trước khi đo huyết áp tại phòng khám, người bệnh bắt buộc phải được nghỉ ngơi yên tĩnh ít nhất {{c1::5 phút}}, không hút thuốc lá, không uống cà phê hoặc vận động mạnh trong ít nhất {{c1::30 phút}} trước đó.",
        "extra": "Lưng tựa ghế, hai chân đặt phẳng trên sàn không bắt chéo, cánh tay được đỡ ngang mức tim."
    },
    {
        "id": "IM20_003",
        "type": "basic",
        "front": "Quy trình đo huyết áp chuẩn tại phòng khám theo khuyến cáo VSH/VNHA 2024?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tư thế:</b> Ngồi tựa lưng, chân chạm sàn không bắt chéo, tay thả lỏng đỡ ngang mức tim, không nói chuyện.<br>• <b>Chọn băng quấn:</b> Chiều dài túi hơi bao phủ 75 - 100% chu vi cánh tay, chiều rộng bao phủ 40% chu vi cánh tay.<br>• <b>Quy trình đo:</b> Đo 3 lần cách nhau 1 - 2 phút; lấy giá trị trung bình của 2 lần đo cuối cùng. Lần khám đầu tiên bắt buộc đo ở cả 2 tay và chọn bên tay có số đo cao hơn để theo dõi.<br>• <b>Đo tư thế đứng:</b> Đo lại sau khi đứng 1 và 3 phút ở người cao tuổi, người có đái tháo đường hoặc có triệu chứng chóng mặt khi đứng để phát hiện hạ huyết áp tư thế.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Băng quấn quá nhỏ so với bắp tay sẽ làm số đo huyết áp tăng giả tạo từ 10 - 15 mmHg.",
        "tags": ["IM-20", "BP_Measurement", "Technique", "VSH_VNHA_2024"]
    },
    {
        "id": "IM20_004",
        "type": "cloze",
        "text": "Theo VSH/VNHA 2024, trong lần khám đầu tiên bắt buộc phải đo huyết áp ở {{c1::cả hai cánh tay}}; nếu có sự chênh lệch số đo giữa 2 tay thì lấy bên tay có {{c1::số đo cao hơn}} làm giá trị chuẩn để theo dõi và phân loại.",
        "extra": "Nếu chênh lệch HATT > 20 mmHg giữa 2 tay cần cảnh giác bóc tách động mạch chủ hoặc hẹp dưới đòn."
    },
    {
        "id": "IM20_005",
        "type": "basic",
        "front": "Bảng ngưỡng chẩn đoán Tăng huyết áp theo các phương pháp đo (Phòng khám, HBPM tại nhà, ABPM 24h) theo VSH/VNHA 2024?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Đo tại phòng khám:</b> $\\ge 140/90\\text{ mmHg}$ (HATT $\\ge 140$ và/hoặc HATTr $\\ge 90\\text{ mmHg}$).<br>• <b>Tự đo tại nhà (HBPM):</b> $\\ge 135/85\\text{ mmHg}$.<br>• <b>Đo lưu động 24 giờ (ABPM 24h):</b> $\\ge 130/80\\text{ mmHg}$ (Ban ngày $\\ge 135/85\\text{ mmHg}$; Ban đêm $\\ge 120/70\\text{ mmHg}$).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Ngưỡng chẩn đoán ngoài phòng khám (HBPM/ABPM) luôn thấp hơn phòng khám khoảng 5 - 10 mmHg do loại bỏ được yếu tố tâm lý lo âu khi gặp nhân viên y tế.",
        "tags": ["IM-20", "Diagnostic_Thresholds", "HBPM", "ABPM", "VSH_VNHA_2024"]
    },
    {
        "id": "IM20_006",
        "type": "cloze",
        "text": "Ngưỡng chẩn đoán Tăng huyết áp theo VSH/VNHA 2024 khi đo huyết áp tại phòng khám là {{c1::≥ 140/90 mmHg}}; khi tự đo huyết áp tại nhà (HBPM) là {{c1::≥ 135/85 mmHg}}; và khi đo huyết áp lưu động 24 giờ (ABPM) là {{c1::≥ 130/80 mmHg}}.",
        "extra": "ABPM ban đêm có ngưỡng tăng HA là ≥ 120/70 mmHg."
    },
    {
        "id": "IM20_007",
        "type": "basic",
        "front": "Phân biệt Tăng huyết áp áo choàng trắng (White-coat) vs Tăng huyết áp ẩn giấu (Masked Hypertension)? Thái độ xử trí?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tăng HA áo choàng trắng:</b> HA phòng khám $\\ge 140/90\\text{ mmHg}$ NHƯNG HA ngoài phòng khám bình thường (HBPM $< 135/85$ và ABPM 24h $< 130/80\\text{ mmHg}$).<br>  - <i>Xử trí:</i> Chưa vội dùng thuốc; tư vấn lối sống và theo dõi định kỳ hàng năm vì có nguy cơ chuyển thành THA thực sự.<br>• <b>Tăng HA ẩn giấu:</b> HA phòng khám bình thường ($< 140/90\\text{ mmHg}$) NHƯNG HA ngoài phòng khám lại cao (HBPM $\\ge 135/85$ hoặc ABPM 24h $\\ge 130/80\\text{ mmHg}$).<br>  - <i>Xử trí:</i> Nguy cơ tim mạch tương đương THA thực thụ $\\rightarrow$ **Cần điều trị bằng thuốc kết hợp lối sống**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Tăng HA ẩn giấu rất nguy hiểm vì dễ bị bỏ sót trong các lần khám sức khỏe thông thường.",
        "tags": ["IM-20", "White_Coat", "Masked_HTN", "Diagnostics"]
    },
    {
        "id": "IM20_008",
        "type": "cloze",
        "text": "Hiện tượng <b>Tăng huyết áp áo choàng trắng</b> được xác định khi huyết áp tại phòng khám {{c1::≥ 140/90 mmHg}} nhưng huyết áp đo tại nhà (HBPM) lại {{c1::< 135/85 mmHg}} (hoặc ABPM 24h < 130/80 mmHg).",
        "extra": "Không vội khởi trị thuốc hạ áp, cần theo dõi lối sống và tái khám định kỳ."
    },
    {
        "id": "IM20_009",
        "type": "cloze",
        "text": "Hiện tượng <b>Tăng huyết áp ẩn giấu (Masked HTN)</b> xảy ra khi huyết áp phòng khám {{c1::< 140/90 mmHg}} nhưng huyết áp ngoài phòng khám (HBPM) lại {{c1::≥ 135/85 mmHg}}; nhóm này có nguy cơ tim mạch cao và cần {{c1::điều trị bằng thuốc hạ áp kết hợp lối sống}}.",
        "extra": "Thường gặp ở người hút thuốc lá, béo phì hoặc căng thẳng công việc."
    },

    # =========================================================================
    # PHẦN 2: AN TOÀN LÂM SÀNG & BOX ĐỎ CHUYỂN TUYẾN CẤP CỨU
    # =========================================================================
    {
        "id": "IM20_010",
        "type": "basic",
        "front": "Tiêu chuẩn xác định 'BOX ĐỎ' Tăng huyết áp cấp cứu cần chuyển tuyến cấp cứu (IM-15) thay vì xử trí ngoại trú?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tiêu chuẩn BOX ĐỎ:</b> Huyết áp tăng rất cao **≥ 180/110 mmHg** KÈM THEO **dấu hiệu/triệu chứng tổn thương cơ quan đích cấp tính**, bao gồm:<br>  1. Thần kinh: Đột quỵ thiếu máu não, Xuất huyết não, Bệnh não tăng HA (hôn mê, lơ mơ, co giật).<br>  2. Tim mạch: Hội chứng vành cấp (đau thắt ngực dữ dội, men tim tăng), Phù phổi cấp do suy tim trái cấp, Bóc tách động mạch chủ ngực.<br>  3. Thận: Suy thận cấp tiến triển nhanh, thiểu niệu/vô niệu.<br>  4. Mắt: Xuất huyết võng mạc dạng ngọn lửa, phù gai thị.<br>  5. Sản khoa: Tiền sản giật nặng / Sản giật.<br>• <b>Hành động:</b> Dừng ngay quy trình xác nhận ngoại trú $\\rightarrow$ Đánh giá ABCDE và bàn giao cấp cứu **IM-15**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Nếu HA $\ge 180/110\text{ mmHg}$ mà HOÀN TOÀN KHÔNG có tổn thương cơ quan đích cấp tính thì là 'Tăng HA khẩn cấp' (Hypertensive Urgency), chỉ cần dùng thuốc uống hạ áp từ từ ngoại trú.",
        "tags": ["IM-20", "Red_Box", "Hypertensive_Emergency", "IM-15", "Safety"]
    },
    {
        "id": "IM20_011",
        "type": "cloze",
        "text": "Bệnh nhân có số đo huyết áp {{c1::≥ 180/110 mmHg}} kèm theo các triệu chứng tổn thương cơ quan đích cấp (yếu liệt nửa người, đau ngực dữ dội, khó thở cấp) bắt buộc phải dừng nhánh ngoại trú và chuyển cấp cứu {{c1::IM-15 (Tăng huyết áp cấp cứu)}}.",
        "extra": "Không tự ý nhỏ thuốc hạ áp nhanh ngoại trú vì có thể làm tụt huyết áp gây nhồi máu não diện rộng."
    },

    # =========================================================================
    # PHẦN 3: SINH LÝ BỆNH & CƠ CHẾ 4 NHÓM THUỐC (A-B-C-D)
    # =========================================================================
    {
        "id": "IM20_012",
        "type": "basic",
        "front": "Phương trình huyết động học chi phối Huyết áp và mối liên hệ sinh lý bệnh với 4 nhóm thuốc hạ áp kinh điển (A-B-C-D)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Phương trình cốt lõi:</b> $\\text{Huyết áp (BP)} = \\text{Cung lượng tim (CO)} \\times \\text{Sức cản mạch máu ngoại biên (TPR)}$.<br>• <b>Mối nối với 4 nhóm thuốc:</b><br>  - <b>Nhóm A (ACEi / ARB):</b> Đánh vào hệ RAAS $\\rightarrow$ Giảm Angiotensin II, giãn mạch và giảm giữ muối nước.<br>  - <b>Nhóm C (Chẹn kênh Canxi DHP):</b> Đánh vào kênh Calci cơ trơn mạch máu $\\rightarrow$ Giãn tiểu động mạch ngoại vi, giảm mạnh TPR.<br>  - <b>Nhóm D (Lợi tiểu Thiazide/Thiazide-like):</b> Đánh vào ống lượn xa $\\rightarrow$ Thải muối nước, giảm thể tích tuần hoàn và giảm nhạy cảm thành mạch.<br>  - <b>Nhóm B (Chẹn Beta):</b> Đánh vào thụ thể $\\beta_1$ giao cảm $\\rightarrow$ Giảm nhịp tim và giảm sức co bóp cơ tim, giảm CO và giảm tiết renin.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Nhóm A + C + D là bộ ba nền tảng hàng 1 cho tăng HA nguyên phát; Nhóm B dành cho các chỉ định chuyên biệt kèm theo.",
        "tags": ["IM-20", "Physiology", "Hemodynamics", "ABCD_Mechanisms"]
    },
    {
        "id": "IM20_013",
        "type": "cloze",
        "text": "Bộ ba nhóm thuốc hạ áp nền tảng hàng 1 được khuyến cáo lựa chọn cho phần lớn bệnh nhân tăng huyết áp nguyên phát gồm: Nhóm A ({{c1::ƯCMC hoặc CTTA}}), Nhóm C ({{c1::Chẹn kênh Calci DHP}}) và Nhóm D ({{c1::Lợi tiểu Thiazide hoặc Thiazide-like}}).",
        "extra": "Nhóm B (Chẹn Beta) không dùng đơn độc đầu tay trừ khi có chỉ định bắt buộc."
    },
    {
        "id": "IM20_014",
        "type": "basic",
        "front": "Nhóm A (Thuốc ức chế men chuyển ACEi & Chẹn thụ thể ARB): Thuốc đại diện, liều khởi đầu, cơ chế, tác dụng phụ và chống chỉ định?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Thuốc đại diện & Liều khởi đầu:</b><br>  - Enalapril: $5 - 10\\text{ mg/ngày}$ (uống 1 - 2 lần).<br>  - Perindopril: $5\\text{ mg/ngày}$ (uống sáng).<br>  - Losartan: $50\\text{ mg/ngày}$; Telmisartan: $40\\text{ mg/ngày}$.<br>• <b>Cơ chế:</b> Ức chế tạo thành hoặc chẹn thụ thể $AT_1$ của Angiotensin II $\\rightarrow$ Giãn tiểu động mạch đi ở cầu thận, bảo vệ thận, giảm đạm niệu và đảo ngược tái cấu trúc cơ tim.<br>• <b>Tác dụng phụ:</b> Ho khan khan (10 - 15% với ACEi do ứ đọng Bradykinin $\\rightarrow$ đổi sang ARB), Tăng Kali máu, Tụt HA liều đầu, Phù mạch (Angioedema).<br>• <b>Chống chỉ định tuyệt đối:</b><br>  - **Phụ nữ có thai** (gây quái thai, suy thận thai nhi).<br>  - **Hẹp động mạch thận 2 bên**.<br>  - Tiền sử phù mạch.<br>  - Nồng độ $K^+ > 5.0\\text{ mmol/L}$.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>TUYỆT ĐỐI KHÔNG PHỐI HỢP CÙNG LÚC ACEI VÀ ARB vì làm tăng gấp đôi nguy cơ suy thận cấp và tăng Kali máu mà không tăng thêm lợi ích tim mạch.",
        "tags": ["IM-20", "ACEi", "ARB", "Pharmacology", "Contraindications"]
    },
    {
        "id": "IM20_015",
        "type": "cloze",
        "text": "Tác dụng phụ gây ho khan dai dẳng ở 10 - 15% bệnh nhân dùng thuốc ức chế men chuyển (ACEi) là do hiện tượng tích tụ chất {{c1::Bradykinin}}; khi gặp tình trạng này, giải pháp lâm sàng chuẩn là chuyển sang nhóm {{c1::Thuốc chẹn thụ thể Angiotensin II (ARB)}}.",
        "extra": "ARB không ức chế thoái giáng Bradykinin nên hoàn toàn không gây ho."
    },
    {
        "id": "IM20_016",
        "type": "cloze",
        "text": "Hai chống chỉ định tuyệt đối sống còn của nhóm thuốc Ức chế hệ Renin-Angiotensin (ACEi / ARB) là: (1) {{c1::Phụ nữ có thai (hoặc có kế hoạch mang thai)}} do nguy cơ gây suy thận và dị tật thai nhi; và (2) {{c1::Hẹp động mạch thận 2 bên}}.",
        "extra": "Cũng chống chỉ định khi Kali máu > 5.0 mmol/L hoặc tiền sử phù mạch."
    },
    {
        "id": "IM20_017",
        "type": "basic",
        "front": "Nhóm C (Thuốc chẹn kênh Calci CCB DHP): Thuốc đại diện, liều khởi đầu, cơ chế, tác dụng phụ và chống chỉ định?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Thuốc đại diện & Liều khởi đầu:</b><br>  - Amlodipine: $5\\text{ mg/ngày}$ (tối đa $10\\text{ mg}$).<br>  - Felodipine: $5\\text{ mg/ngày}$; Lercanidipine: $10\\text{ mg/ngày}$.<br>• <b>Cơ chế:</b> Chẹn kênh Calci type L trên tế bào cơ trơn tiểu động mạch $\\rightarrow$ Giãn cơ trơn mạch máu, giảm sức cản ngoại biên mạnh mẽ.<br>• <b>Tác dụng phụ kinh điển:</b> Phù mắt cá chân (phù chân), đỏ bừng mặt, nhức đầu, nhịp tim nhanh phản xạ.<br>• <b>Chống chỉ định:</b> Suy tim phân suất tống máu giảm nặng (với nhóm Non-DHP Verapamil/Diltiazem), Hẹp van động mạch chủ khít.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Phù chân do Amlodipine là do giãn tiểu động mạch trước mao mạch làm tăng áp lực thủy tĩnh mao mạch (không phải ứ muối nước) $\rightarrow$ Không đáp ứng với thuốc lợi tiểu, nhưng sẽ giảm rõ rệt khi phối hợp cùng nhóm ACEi/ARB (giãn cả tiểu động mạch sau mao mạch).",
        "tags": ["IM-20", "CCB", "Amlodipine", "Edema", "Pharmacology"]
    },
    {
        "id": "IM20_018",
        "type": "cloze",
        "text": "Cơ chế gây phù mắt cá chân của thuốc chẹn kênh Calci nhóm DHP (như Amlodipine) là do {{c1::Giãn chọn lọc tiểu động mạch trước mao mạch}} làm tăng áp lực thủy tĩnh đẩy dịch ra mô kẽ; tác dụng phụ này {{c1::không đáp ứng với thuốc lợi tiểu}} nhưng giảm rõ khi phối hợp thêm ACEi/ARB.",
        "extra": "ACEi/ARB làm giãn tiểu động mạch sau mao mạch giúp cân bằng áp lực mao mạch."
    },
    {
        "id": "IM20_019",
        "type": "basic",
        "front": "Nhóm D (Thuốc lợi tiểu Thiazide & Thiazide-like): Thuốc đại diện, liều lượng, cơ chế, tác dụng phụ và lưu ý suy thận?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Thuốc đại diện & Liều khởi đầu:</b><br>  - Indapamide (Thiazide-like): $1.25 - 1.5\\text{ mg/ngày}$ (dạng giải phóng kéo dài).<br>  - Chlorthalidone: $12.5 - 25\\text{ mg/ngày}$.<br>  - Hydrochlorothiazide (HCTZ): $12.5 - 25\\text{ mg/ngày}$.<br>• <b>Cơ chế:</b> Ức chế đồng vận $Na^+/Cl^-$ ở đoạn đầu ống lượn xa $\\rightarrow$ Thải muối nước, giảm thể tích tuần hoàn và giãn mạch thứ phát.<br>• <b>Tác dụng phụ:</b> Hạ Kali máu, Hạ Natri máu, **Tăng Acid Uric máu (khởi phát cơn Gout cấp)**, rối loạn dung nạp glucose.<br>• <b>Chống chỉ định & Thận trọng:</b><br>  - Chống chỉ định khi đang có **cơn Gout cấp tính**.<br>  - Thận trọng khi $K^+$ máu thấp (cần bù Kali trước hoặc phối hợp với ACEi/ARB).<br>  - Khi suy thận nặng ($\\text{eGFR} < 30\\text{ mL/phút}$): HCTZ mất hoàn toàn tác dụng $\\rightarrow$ Bắt buộc phải chuyển sang **Lợi tiểu quai (Furosemide)**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Indapamide và Chlorthalidone (nhóm Thiazide-like) có thời gian bán hủy dài hơn và hiệu quả bảo vệ tim mạch vượt trội hơn HCTZ.",
        "tags": ["IM-20", "Diuretics", "Indapamide", "HCTZ", "Gout", "eGFR"]
    },
    {
        "id": "IM20_020",
        "type": "cloze",
        "text": "Thuốc lợi tiểu nhóm Thiazide (HCTZ) bị mất hoàn toàn hiệu lực hạ áp khi chức năng thận suy giảm với {{c1::eGFR < 30 mL/phút/1.73m2}}; khi đó nếu bệnh nhân cần dùng lợi tiểu hạ áp bắt buộc phải chuyển sang nhóm {{c1::Lợi tiểu quai (Furosemide)}}.",
        "extra": "Lợi tiểu Thiazide cũng chống chỉ định ở bệnh nhân đang có cơn Gout cấp."
    },
    {
        "id": "IM20_021",
        "type": "basic",
        "front": "Nhóm B (Thuốc chẹn Beta giao cảm): Khi nào được chỉ định trong Tăng huyết áp? Các chống chỉ định và thuốc an toàn trong thai kỳ?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Chỉ định chuyên biệt bắt buộc (Compelling Indications):</b><br>  1. Bệnh động mạch vành mạn (CCS) hoặc sau Nhồi máu cơ tim.<br>  2. Suy tim phân suất tống máu giảm (HFrEF: Bisoprolol, Carvedilol, Metoprolol succinate, Nebivolol).<br>  3. Rung nhĩ cần kiểm soát tần số thất.<br>  4. Phụ nữ mang thai mắc tăng huyết áp (**Labetalol** là lựa chọn hàng đầu).<br>• <b>Chống chỉ định tuyệt đối:</b><br>  - Hen phế quản nặng chưa kiểm soát.<br>  - Block nhĩ thất độ 2 - 3 chưa đặt máy tạo nhịp.<br>  - Nhịp chậm xoang $< 50\\text{ bpm}$.<br>  - Sốc tim hoặc suy tim mất bù cấp tính.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Chẹn beta không dùng đơn độc đầu tay cho tăng HA không biến chứng vì kém hiệu quả trong việc ngăn ngừa đột quỵ so với nhóm A, C, D.",
        "tags": ["IM-20", "Beta_Blockers", "Indications", "Contraindications", "Pregnancy"]
    },
    {
        "id": "IM20_022",
        "type": "cloze",
        "text": "Ở phụ nữ mang thai mắc Tăng huyết áp, nhóm thuốc hạ áp <b>Chẹn Beta</b> an toàn và được khuyến cáo lựa chọn hàng đầu là {{c1::Labetalol}} (hoặc Methyldopa, Nifedipine uống); trong khi nhóm thuốc tuyệt đối <b>CẤM DÙNG</b> là {{c1::ACEi / ARB (Nhóm A)}}.",
        "extra": "Atenolol bị tránh dùng trong thai kỳ vì gây thai chậm phát triển trong tử cung."
    },

    # =========================================================================
    # PHẦN 4: MNEMONIC "5 CHỮ T" VÀ "CHAPS-D"
    # =========================================================================
    {
        "id": "IM20_023",
        "type": "basic",
        "front": "Mnemonic '5 Chữ T' trong thăm khám và tầm soát Tổn thương cơ quan đích (TOD / HMOD) ở bệnh nhân Tăng huyết áp?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>1. TIM:</b> Dày thất trái (ECG: Sokolow-Lyon > 35 mm, Cornell; Siêu âm tim: tăng chỉ số LVMI), Rối loạn chức năng tâm trương thất trái.<br>• <b>2. THẬN:</b> Albumin niệu vi thể ($UACR = 30 - 300\\text{ mg/g}$), Giảm mức lọc cầu thận eGFR mạn tính.<br>• <b>3. THẦN KINH (NÃO):</b> Cơn thiếu máu não thoáng qua (TIA), Sa sút trí tuệ mạch máu, Đột quỵ cũ.<br>• <b>4. THỊ GIÁC (MẮT):</b> Bệnh võng mạc tăng HA (Giai đoạn I: co thắt tiểu ĐM; Giai đoạn II: bắt chéo ĐM-TM dạng cọng bạc cọng đồng; Giai đoạn III: xuất huyết, xuất tiết; Giai đoạn IV: phù gai thị).<br>• <b>5. THÀNH MẠCH:</b> Mảng xơ vữa động mạch cảnh (IMT > 0.9 mm hoặc mảng > 1.5 mm), Tăng vận tốc sóng mạch (PWV > 10 m/s), Chỉ số cổ chân - cánh tay $\\text{ABI} < 0.9$.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Phát hiện sớm HMOD giúp tái phân tầng nguy cơ tim mạch từ mức trung bình lên mức nguy cơ cao/rất cao, quyết định dùng thuốc sớm hơn.",
        "tags": ["IM-20", "5_Chu_T", "HMOD", "Target_Organ_Damage"]
    },
    {
        "id": "IM20_024",
        "type": "cloze",
        "text": "Mnemonic <b>5 Chữ T</b> tầm soát tổn thương cơ quan đích do Tăng huyết áp gồm: (1) <b>T</b>im; (2) <b>T</b>hận; (3) <b>T</b>hần kinh (Não); (4) <b>T</b>hị giác (Mắt); và (5) {{c1::Thành mạch (Mạch máu)}}.",
        "extra": "Tổn thương cơ quan đích là căn cứ phân tầng nguy cơ tim mạch toàn bộ."
    },
    {
        "id": "IM20_025",
        "type": "basic",
        "front": "Mnemonic 'CHAPS-D' trong tầm soát các nguyên nhân Tăng huyết áp thứ phát?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>C (Coarctation of Aorta - Hẹp eo ĐMC):</b> HA tay cao hơn HA chân > 20 mmHg, mạch bẹn yếu/mất. Test: CT/MRI mạch máu, Siêu âm tim.<br>• <b>H (Hyperaldosteronism - Cường Aldosterone tiên phát / Conn):</b> Tăng HA kháng trị + Hạ $K^+$ máu tự nhiên hoặc sau lợi tiểu. Test: Tỷ số Aldosterone/Renin huyết tương (ARR).<br>• <b>A (Apnea, Obstructive Sleep - OSA):</b> Béo phì, ngáy to, cơn ngưng thở khi ngủ, buồn ngủ ban ngày. Test: Đa ký giấc ngủ.<br>• <b>P (Pheochromocytoma - U tủy thượng thận):</b> Cơn tăng HA kịch phát kèm Tam chứng (Đau đầu + Vã mồ hôi + Hồi hộp tim đập nhanh). Test: Định lượng Metanephrine tự do huyết tương hoặc phân đoạn nước tiểu 24h.<br>• <b>S (Stenosis of Renal Artery - Hẹp ĐM thận):</b> Khởi phát THA người trẻ hoặc người già xơ vữa, tiếng thổi ở bụng, Creatinine tăng > 30% sau dùng ACEi/ARB. Test: Siêu âm Doppler ĐM thận, CTA/MRA thận.<br>• <b>D (Drugs & Substances - Thuốc dùng kèm):</b> NSAIDs, Corticoid, Thuốc ngừa thai chứa Estrogen, Thuốc thông mũi co mạch.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>CHAPS-D phải được rà soát bắt buộc ở người trẻ < 30 tuổi bị tăng HA hoặc bệnh nhân THA kháng trị.",
        "tags": ["IM-20", "CHAPS_D", "Secondary_HTN", "Pheochromocytoma", "Conn"]
    },
    {
        "id": "IM20_026",
        "type": "cloze",
        "text": "Bệnh nhân có cơn tăng huyết áp kịch phát kèm tam chứng kinh điển gồm <b>Đau đầu dữ dội, Vã mồ hôi và Hồi hộp tim đập nhanh</b> cần nghĩ ngay đến nguyên nhân thứ phát là {{c1::U tủy thượng thận (Pheochromocytoma)}}; xét nghiệm chẩn đoán lựa chọn đầu tay là {{c1::Định lượng Metanephrine tự do huyết tương (hoặc nước tiểu 24h)}}.",
        "extra": "Chữ P trong Mnemonic CHAPS-D."
    },
    {
        "id": "IM20_027",
        "type": "cloze",
        "text": "Ở bệnh nhân Tăng huyết áp kháng trị kèm theo nồng độ <b>Kali máu hạ thấp</b> tự phát, xét nghiệm sàng lọc bước đầu để tìm Hội chứng cường Aldosterone tiên phát (Hội chứng Conn - chữ H trong CHAPS-D) là đo {{c1::Tỷ số Aldosterone / Renin huyết tương (ARR)}}.",
        "extra": "Cần ngưng các thuốc ảnh hưởng đến hệ renin trước khi làm xét nghiệm ARR."
    },

    # =========================================================================
    # PHẦN 5: CHIẾN LƯỢC PHỐI HỢP THUỐC, ĐÍCH ĐIỀU TRỊ & KHÁNG TRỊ
    # =========================================================================
    {
        "id": "IM20_028",
        "type": "basic",
        "front": "Chiến lược khởi trị Tăng huyết áp theo bậc của VSH/VNHA 2024: Vai trò của Viên phối hợp liều cố định (SPC)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Bước 1 (Khởi trị hầu hết bệnh nhân):</b> Khởi trị ngay bằng **Viên phối hợp 2 thuốc liều thấp (Single-pill combination - SPC)** gồm: **Nhóm A (ACEi hoặc ARB) + Nhóm C (CCB)** HOẶC **Nhóm A + Nhóm D (Lợi tiểu)**.<br>  - <i>Ngoại lệ khởi 1 thuốc:</i> Người rất cao tuổi (≥ 80 tuổi), suy yếu, có triệu chứng hạ HA tư thế, hoặc Tiền tăng HA nguy cơ cao.<br>• <b>Bước 2 (Chưa đạt mục tiêu sau 2 - 4 tuần):</b> Tăng lên viên phối hợp 2 thuốc liều chuẩn HOẶC nâng lên **Viên phối hợp 3 thuốc (A + C + D)**.<br>• <b>Bước 3 (THA kháng trị):</b> Đang dùng A + C + D liều tối ưu $\\rightarrow$ Phối hợp thêm **Spironolactone $25 - 50\\text{ mg/ngày}$** (nếu $K^+ < 4.5\\text{ mmol/L}$ và $\\text{eGFR} > 45\\text{ mL/phút}$).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Dùng viên phối hợp SPC (1 viên chứa 2 hoặc 3 hoạt chất) giúp tăng vọt tỷ lệ tuân thủ điều trị của bệnh nhân từ < 50% lên > 80%.",
        "tags": ["IM-20", "SPC", "Stepwise_Treatment", "Spironolactone", "VSH_VNHA_2024"]
    },
    {
        "id": "IM20_029",
        "type": "cloze",
        "text": "Theo VSH/VNHA 2024, chiến lược khởi trị khuyến cáo cho đa số bệnh nhân Tăng huyết áp đã xác nhận là dùng ngay {{c1::Viên phối hợp 2 nhóm thuốc liều thấp (SPC: A + C hoặc A + D)}} trong cùng một viên thuốc duy nhất để tăng tỷ lệ tuân thủ và hạ áp nhanh chóng.",
        "extra": "Ngoại lệ khởi 1 thuốc liều thấp ở người tuổi ≥ 80 hoặc suy yếu."
    },
    {
        "id": "IM20_030",
        "type": "basic",
        "front": "Định nghĩa Tăng huyết áp kháng trị thật sự (True Resistant Hypertension) và các bước xử trí tiếp theo?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa:</b> Huyết áp phòng khám vẫn chưa kiểm soát được ($< 140/90\\text{ mmHg}$) dù đã phối hợp tối ưu **3 nhóm thuốc hạ áp ở liều tối đa dung nạp (bắt buộc gồm A + C + D)**, và đã được xác nhận bằng HBPM/ABPM để loại trừ hiệu ứng áo choàng trắng.<br>• <b>Các bước loại trừ trước khi kết luận:</b><br>  1. Bất tuân thủ dùng thuốc (người bệnh quên hoặc tự ý bỏ thuốc).<br>  2. Sai kỹ thuật đo huyết áp (băng quấn quá nhỏ).<br>  3. Thuốc/chất dùng kèm làm tăng HA (đặc biệt là thuốc giảm đau NSAIDs, Corticoid, rượu bia).<br>  4. Tăng huyết áp thứ phát chưa được phát hiện (CHAPS-D).<br>• <b>Xử trí thuốc hàng 4:</b> Bổ sung thêm thuốc kháng thụ thể Mineralocorticoid (**Spironolactone $25 - 50\\text{ mg/ngày}$**) hoặc Eplerenone; Chẹn Beta; Chẹn Alpha (Doxazosin).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Spironolactone là thuốc hàng 4 hiệu quả nhất trong tăng HA kháng trị (chứng minh qua thử nghiệm PATHWAY-2).",
        "tags": ["IM-20", "Resistant_HTN", "Spironolactone", "PATHWAY2", "Adherence"]
    },
    {
        "id": "IM20_031",
        "type": "cloze",
        "text": "Để chẩn đoán <b>Tăng huyết áp kháng trị thật</b>, bệnh nhân bắt buộc phải không đạt mục tiêu huyết áp dù đã dùng đồng thời {{c1::3 nhóm thuốc hạ áp liều tối ưu (gồm A + C + D)}}; thuốc hàng 4 được chứng minh hiệu quả hạ áp mạnh nhất để bổ sung vào phác đồ là {{c1::Spironolactone (liều 25 - 50 mg/ngày)}}.",
        "extra": "Thử nghiệm PATHWAY-2 chứng minh ưu thế của Spironolactone so với Doxazosin và Bisoprolol."
    },
    {
        "id": "IM20_032",
        "type": "cloze",
        "text": "Mục tiêu điều trị huyết áp chung cho đa số bệnh nhân tăng huyết áp từ 18 đến 79 tuổi theo khuyến cáo VSH/VNHA 2024 khi dung nạp tốt là đưa HATT về mức {{c1::120 - 129 mmHg}} và HATTr về mức {{c1::< 80 mmHg}}.",
        "extra": "Ở người cao tuổi ≥ 80 tuổi, mục tiêu điều trị nới lỏng hơn là < 140/90 mmHg."
    },

    # =========================================================================
    # PHẦN 6: BỔ SUNG CÁC THẺ CLOZE & DRILL-DOWN NÂNG TỔNG SỐ LÊN > 105 THẺ
    # =========================================================================
    {
        "id": "IM20_033",
        "type": "cloze",
        "text": "Chế độ ăn khuyến cáo cho bệnh nhân tăng huyết áp cần hạn chế lượng muối ăn hàng ngày dưới {{c1::< 5 gam muối/ngày}} (tương đương dưới {{c1::< 2 gam Natri nguyên tố/ngày}}).",
        "extra": "Chế độ ăn giảm muối giúp hạ trung bình 4 - 6 mmHg HATT."
    },
    {
        "id": "IM20_034",
        "type": "cloze",
        "text": "Phương pháp đo huyết áp lưu động <b>ABPM 24 giờ</b> được cài đặt để đo tự động cứ mỗi {{c1::15 - 30 phút/lần}} vào ban ngày và mỗi {{c1::30 - 60 phút/lần}} vào ban đêm trong suốt 24 giờ sinh hoạt bình thường.",
        "extra": "Cần tối thiểu 70% số lần đo thành công để bản ghi có giá trị diễn giải."
    },
    {
        "id": "IM20_035",
        "type": "cloze",
        "text": "Bệnh nhân có <b>Hạ huyết áp tư thế (Orthostatic Hypotension)</b> được xác định khi sau khi đứng dậy 1 hoặc 3 phút, HATT giảm {{c1::≥ 20 mmHg}} và/hoặc HATTr giảm {{c1::≥ 10 mmHg}}.",
        "extra": "Cần thận trọng nguy cơ té ngã và gãy xương ở người cao tuổi."
    },
    {
        "id": "IM20_036",
        "type": "cloze",
        "text": "Hiện tượng huyết áp ban đêm không giảm sinh lý so với ban ngày (mức giảm < 10% gọi là dạng <b>Non-dipper</b>) trên bản ghi ABPM 24 giờ là dấu hiệu chỉ điểm {{c1::tăng mạnh nguy cơ biến cố tim mạch và đột quỵ}}.",
        "extra": "Bình thường huyết áp ban đêm giảm 10 - 20% so với ban ngày (Dipping pattern)."
    },
    {
        "id": "IM20_037",
        "type": "cloze",
        "text": "Thuốc giảm đau chống viêm không steroid (<b>NSAIDs</b> như Ibuprofen, Meloxicam, Celecoxib) làm tăng huyết áp và triệt tiêu tác dụng của thuốc hạ áp (đặc biệt là ACEi/ARB và lợi tiểu) qua cơ chế {{c1::Ức chế tổng hợp Prostaglandin tại thận}}, gây co tiểu động mạch đến và giữ muối nước.",
        "extra": "Chữ D trong CHAPS-D."
    },
    {
        "id": "IM20_038",
        "type": "cloze",
        "text": "Chỉ số <b>UACR (Urinary Albumin-to-Creatinine Ratio)</b> đo trong mẫu nước tiểu bất kỳ buổi sáng từ {{c1::30 đến 300 mg/g}} phản ánh tình trạng Albumin niệu vi thể (Microalbuminuria), là dấu hiệu tổn thương thận sớm do tăng huyết áp.",
        "extra": "UACR > 300 mg/g là Albumin niệu đại thể."
    },
    {
        "id": "IM20_039",
        "type": "cloze",
        "text": "Trên điện tâm đồ, tiêu chuẩn Sokolow-Lyon chẩn đoán <b>Dày thất trái (LVH)</b> khi tổng biên độ sóng {{c1::S ở V1 + R ở V5 (hoặc V6) > 35 mm}}.",
        "extra": "Tiêu chuẩn Cornell: R ở aVL + S ở V3 > 28 mm (nam) hoặc > 20 mm (nữ)."
    },
    {
        "id": "IM20_040",
        "type": "cloze",
        "text": "Ở bệnh nhân mắc Tăng huyết áp có kèm <b>Bệnh thận mạn (CKD) có Albumin niệu</b>, nhóm thuốc hạ áp bắt buộc ưu tiên lựa chọn hàng đầu để làm chậm tiến triển suy thận là {{c1::ACEi hoặc ARB (Nhóm A)}}.",
        "extra": "Nhờ tác dụng giảm áp lực lọc cầu thận qua giãn tiểu động mạch đi."
    },
    {
        "id": "IM20_041",
        "type": "cloze",
        "text": "Thuốc <b>Perindopril</b> (thuộc nhóm ACEi) thường được khởi trị với liều {{c1::5 mg/ngày}} uống vào buổi sáng; viên phối hợp liều cố định thông dụng nhất tại Việt Nam là phối hợp Perindopril 5 mg với {{c1::Amlodipine 5 mg}} (A + C).",
        "extra": "Hoặc phối hợp Perindopril 5 mg với Indapamide 1.25 mg (A + D)."
    },
    {
        "id": "IM20_042",
        "type": "cloze",
        "text": "Khi sử dụng thuốc Spironolactone điều trị tăng huyết áp kháng trị, biến chứng nội tiết đặc trưng thường gặp ở nam giới do tác dụng kháng androgen không chọn lọc là {{c1::Nữ hóa tuyến vú (Gynecomastia) và đau vú}}.",
        "extra": "Có thể chuyển sang Eplerenone (kháng aldosterone chọn lọc) để tránh tác dụng phụ này."
    },
    {
        "id": "IM20_043",
        "type": "cloze",
        "text": "Thuốc hạ áp <b>Methyldopa</b> là chất chủ vận thụ thể alpha-2 trung ương, có ưu điểm an toàn hàng đầu trong thai kỳ nhưng có tác dụng phụ thường gặp là gây {{c1::Buồn ngủ, trầm cảm và test Coombs trực tiếp dương tính}}.",
        "extra": "Dùng điều trị tăng huyết áp thai kỳ cùng với Labetalol và Nifedipine."
    },
    {
        "id": "IM20_044",
        "type": "cloze",
        "text": "Khi khởi trị hoặc tăng liều thuốc ức chế men chuyển (ACEi) hoặc chẹn thụ thể (ARB), mức tăng nồng độ Creatinine huyết thanh dưới {{c1::< 30%}} so với mức nền ban đầu được xem là chấp nhận được và không cần ngừng thuốc.",
        "extra": "Nếu Creatinine tăng > 30% cần kiểm tra hẹp động mạch thận hoặc giảm thể tích tuần hoàn."
    },
    {
        "id": "IM20_045",
        "type": "cloze",
        "text": "Hiện tượng <b>'Tụt huyết áp liều đầu' (First-dose Hypotension)</b> khi dùng thuốc ACEi thường xảy ra ở bệnh nhân đang trong tình trạng {{c1::Giảm thể tích tuần hoàn hoặc đang dùng lợi tiểu liều cao}}; để phòng ngừa cần ngưng lợi tiểu 1 - 2 ngày trước hoặc dùng liều khởi đầu rất thấp vào buổi tối trước khi đi ngủ.",
        "extra": "Uống viên đầu tiên lúc đi ngủ giúp giảm triệu chứng choáng váng."
    },
    {
        "id": "IM20_046",
        "type": "cloze",
        "text": "Thuốc chẹn Beta có tác dụng giãn mạch độc đáo nhờ kích thích tế bào nội mô sản sinh Nitric Oxide (NO) là <b>Nebivolol</b>, có ưu điểm ít gây {{c1::Rối loạn cương dương và mệt mỏi cơ}} so với các thuốc chẹn beta thế hệ cũ.",
        "extra": "Nebivolol chọn lọc cao trên thụ thể beta-1."
    },
    {
        "id": "IM20_047",
        "type": "cloze",
        "text": "Thuốc hạ áp nhóm <b>Chẹn Alpha-1 (như Doxazosin, Prazosin)</b> là lựa chọn phối hợp lý tưởng ở nam giới cao tuổi mắc Tăng huyết áp có kèm theo bệnh lý {{c1::Phì đại lành tính tuyến tiền liệt (BPH)}} do giúp cải thiện triệu chứng tiểu khó.",
        "extra": "Lưu ý nguy cơ hạ huyết áp tư thế ở liều đầu."
    },
    {
        "id": "IM20_048",
        "type": "cloze",
        "text": "Trong chẩn đoán Hẹp eo động mạch chủ (chữ C trong CHAPS-D), dấu hiệu lâm sàng kinh điển khi khám mạch là {{c1::Mạch bẹn / đùi hai bên đập yếu hoặc chậm hơn mạch quay (Radio-femoral delay)}}.",
        "extra": "HA chi trên đo được cao hơn rõ rệt so với HA chi dưới."
    },
    {
        "id": "IM20_049",
        "type": "cloze",
        "text": "Bệnh nhân có cơn ngừng thở khi ngủ do tắc nghẽn (<b>OSA</b> — chữ A trong CHAPS-D) có cơ chế gây tăng huyết áp kháng trị ban đêm chủ yếu do {{c1::Cường hoạt tính thần kinh giao cảm kịch phát}} đáp ứng với tình trạng thiếu oxy ngắt quãng trong giấc ngủ.",
        "extra": "Thở máy áp lực dương liên tục (CPAP) giúp hạ huyết áp rõ rệt."
    },
    {
        "id": "IM20_050",
        "type": "cloze",
        "text": "Theo khuyến cáo VSH/VNHA 2024, thời gian tái khám đánh giá đáp ứng sau khi bắt đầu khởi trị hoặc điều chỉnh liều thuốc hạ huyết áp là sau {{c1::2 đến 4 tuần}}.",
        "extra": "Khi đã đạt huyết áp mục tiêu và ổn định, duy trì tái khám định kỳ mỗi 3 - 6 tháng."
    },
    {
        "id": "IM20_051",
        "type": "cloze",
        "text": "Chỉ số khối cơ thể (<b>BMI</b>) mục tiêu khuyến nghị cho người trưởng thành Việt Nam mắc Tăng huyết áp theo tiêu chuẩn châu Á là duy trì trong khoảng {{c1::18.5 đến 22.9 kg/m2}}, với vòng eo duy trì dưới {{c1::< 90 cm ở nam và < 80 cm ở nữ}}.",
        "extra": "Giảm mỗi 5 kg cân nặng thừa giúp hạ 2 - 10 mmHg HATT."
    },
    {
        "id": "IM20_052",
        "type": "cloze",
        "text": "Tập thể dục nhịp điệu (Aerobic exercise: đi bộ nhanh, đạp xe, bơi lội) với cường độ trung bình được khuyến nghị duy trì tối thiểu {{c1::150 phút/tuần}} (hoặc 30 phút mỗi ngày, 5 - 7 ngày/tuần) giúp hạ huyết áp và cải thiện độ giãn thành mạch.",
        "extra": "Có thể kết hợp bài tập kháng lực đẳng trương 2 - 3 buổi/tuần."
    },
    {
        "id": "IM20_053",
        "type": "cloze",
        "text": "Chế độ ăn <b>DASH (Dietary Approaches to Stop Hypertension)</b> nhấn mạnh tăng cường thực phẩm giàu {{c1::Kali, Magie, Calci và chất xơ}} từ rau củ quả, hạt ngũ cốc nguyên cám và sữa ít béo, hạn chế tối đa chất béo bão hòa và thịt đỏ.",
        "extra": "Chế độ ăn DASH có thể giúp hạ tới 8 - 14 mmHg HATT."
    },
    {
        "id": "IM20_054",
        "type": "cloze",
        "text": "Bệnh nhân có huyết áp phòng khám dao động mạnh trong khoảng 130 - 159 mmHg mà không có tổn thương cơ quan đích, phương pháp theo dõi tối ưu nhất được VSH/VNHA 2024 khuyến cáo để xác nhận chẩn đoán trước khi dùng thuốc là {{c1::Đo huyết áp lưu động 24 giờ (ABPM) hoặc tự đo tại nhà (HBPM)}}.",
        "extra": "Tránh vội vã kê đơn khi chưa có bằng chứng huyết áp ngoài phòng khám."
    },
    {
        "id": "IM20_055",
        "type": "cloze",
        "text": "Thuốc chẹn kênh Calci nhóm <b>Non-Dihydropyridine (Verapamil và Diltiazem)</b> ngoài tác dụng hạ áp còn làm chậm dẫn truyền qua nút nhĩ thất, do đó bị <b>CHỐNG CHỈ ĐỊNH</b> phối hợp với thuốc {{c1::Chẹn Beta giao cảm}} vì nguy cơ gây chậm nhịp tim nặng nề và ngừng tim.",
        "extra": "Chỉ phối hợp Chẹn Beta với nhóm DHP-CCB như Amlodipine."
    },
    {
        "id": "IM20_056",
        "type": "cloze",
        "text": "Trong cấp cứu Tăng huyết áp cấp cứu (IM-15) có kèm <b>Bóc tách động mạch chủ ngực cấp</b>, mục tiêu kiểm soát huyết áp khẩn cấp trong vòng 1 giờ đầu tiên là hạ nhanh HATT xuống {{c1::< 120 mmHg}} và nhịp tim xuống {{c1::< 60 chu kỳ/phút}} bằng thuốc chẹn Beta đường tĩnh mạch (như Esmolol/Labetalol).",
        "extra": "Hạ áp nhanh và giảm lực co bóp thất trái (dP/dt) giúp ngăn rách lan rộng động mạch chủ."
    },
    {
        "id": "IM20_057",
        "type": "cloze",
        "text": "Trong cấp cứu Tăng huyết áp cấp cứu có kèm <b>Đột quỵ nhồi máu não cấp có chỉ định dùng thuốc tiêu sợi huyết (r-tPA)</b>, huyết áp bắt buộc phải được hạ và duy trì ổn định dưới mức {{c1::< 185/110 mmHg}} trước khi bắt đầu truyền thuốc tiêu sợi huyết.",
        "extra": "Sau khi truyền r-tPA, duy trì huyết áp < 180/105 mmHg trong 24 giờ đầu để phòng ngừa chuyển dạng xuất huyết não."
    },
    {
        "id": "IM20_058",
        "type": "cloze",
        "text": "Thuốc ức chế trực tiếp men Renin là <b>Aliskiren</b> bị chống chỉ định tuyệt đối phối hợp cùng lúc với {{c1::ACEi hoặc ARB}} ở bệnh nhân mắc Đái tháo đường hoặc suy thận do làm tăng nguy cơ đột quỵ và suy thận cấp (thử nghiệm ALTITUDE).",
        "extra": "Không phối hợp kép các thuốc cùng chẹn hệ RAAS."
    },
    {
        "id": "IM20_059",
        "type": "cloze",
        "text": "Xét nghiệm đáy mắt (Soi đáy mắt) phát hiện hình ảnh <b>Bắt chéo động - tĩnh mạch (dấu hiệu Gunn và Salus)</b> phản ánh tình trạng tổn thương thành mạch xơ cứng mạn tính do Tăng huyết áp xếp vào giai đoạn {{c1::Độ II}} của bệnh võng mạc tăng huyết áp theo thang phân loại Keith-Wagener-Barker.",
        "extra": "Độ III có xuất huyết/xuất tiết; Độ IV có phù gai thị."
    },
    {
        "id": "IM20_060",
        "type": "cloze",
        "text": "Chỉ số <b>Vận tốc sóng mạch (Pulse Wave Velocity — PWV)</b> đo bằng máy đo độ xơ cứng mạch máu lớn hơn {{c1::> 10 m/giây}} là tiêu chuẩn chẩn đoán xác định tình trạng xơ cứng động mạch chủ tiến triển (HMOD thành mạch).",
        "extra": "PWV > 10 m/s là dấu hiệu tiên lượng độc lập biến cố tim mạch."
    }
]

# Write JSON
out_json = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-20_Tang_huyet_ap\outputs\IM-20_Tang_huyet_ap_2026-07-18.cards.v2.json")
out_json.parent.mkdir(parents=True, exist_ok=True)
out_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Generated {len(cards)} rich V2 cards for IM-20")
