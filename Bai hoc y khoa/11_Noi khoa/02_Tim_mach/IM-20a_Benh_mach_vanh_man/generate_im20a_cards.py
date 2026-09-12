# -*- coding: utf-8 -*-
"""
Generator for comprehensive IM-20a Anki V2 flashcards (>100 cards with rich Cloze & Basic).
Follows medical-flashcard-governance strictly:
- Basic: <b>📖 Văn bản gốc:</b><br> + <b>🔍 Góc nhìn bổ sung (AI):</b><br>
- Cloze: only {{c1::...}}
- Clean Unicode (no LaTeX math/arrows)
"""
import json
from pathlib import Path

cards = [
    # =========================================================================
    # PHẦN 1: ĐẠI CƯƠNG, 6 BỐI CẢNH LÂM SÀNG & SINH LÝ BỆNH MẠCH VÀNH
    # =========================================================================
    {
        "id": "IM20A_001",
        "type": "basic",
        "front": "Định nghĩa Hội chứng vành mạn (CCS — ESC 2024) và Bệnh mạch vành mạn (CCD — AHA/ACC 2023)? Tại sao từ bỏ thuật ngữ 'Đau thắt ngực ổn định'?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>CCS (ESC 2024):</b> Bệnh lý động học, mạn tính, tiến triển liên tục của xơ vữa động mạch và/hoặc rối loạn chức năng vi mạch, có thể ổn định kéo dài nhưng có thể chuyển biến đột ngột bất kỳ lúc nào thành Hội chứng vành cấp (ACS).<br>• <b>CCD (AHA/ACC 2023):</b> Thuật ngữ bao quát toàn bộ các giai đoạn mạn tính của bệnh mạch vành (sau can thiệp, sau NMCT, suy tim do TMCB, hoặc ANOCA/INOCA).<br>• <b>Lý do bỏ thuật ngữ cũ:</b> (1) Bệnh không hề ổn định mà tiến triển liên tục; (2) Nhiều bệnh nhân không hề đau ngực; (3) Mở rộng sang các thể không tắc nghẽn động mạch lớn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Sự thay đổi tên gọi nhấn mạnh tính chất nguy cơ biến cố tim mạch luôn tiềm ẩn, đòi hỏi điều trị nội khoa tối ưu (GDMT) suốt đời.",
        "tags": ["IM-20a", "CCS", "CCD", "Definition", "Overview"]
    },
    {
        "id": "IM20A_002",
        "type": "cloze",
        "text": "Hội chứng vành mạn (CCS) theo khuyến cáo ESC 2024 không phải là bệnh lý tĩnh mà là một quá trình {{c1::động học, viêm mạn tính tiến triển}} của mảng xơ vữa hoặc rối loạn chức năng vi mạch, có thể đột ngột chuyển thành {{c1::Hội chứng vành cấp (ACS)}}.",
        "extra": "Đây là lý do thuật ngữ 'Đau thắt ngực ổn định' chính thức bị bãi bỏ."
    },
    {
        "id": "IM20A_003",
        "type": "basic",
        "front": "Kể tên và nêu đặc điểm cốt lõi của 6 kịch bản lâm sàng (6 Clinical Scenarios) của Hội chứng vành mạn theo ESC?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Scenario 1:</b> Nghi ngờ CAD ở bệnh nhân có triệu chứng đau ngực ổn định và/hoặc khó thở khi gắng sức.<br>• <b>Scenario 2:</b> Bệnh nhân mới xuất hiện suy tim hoặc rối loạn chức năng thất trái nghi ngờ do căn nguyên thiếu máu cục bộ.<br>• <b>Scenario 3:</b> Bệnh nhân không triệu chứng hoặc triệu chứng ổn định trong vòng 1 năm đầu sau Hội chứng vành cấp (ACS) hoặc sau tái thông mạch vành (PCI/CABG).<br>• <b>Scenario 4:</b> Bệnh nhân không triệu chứng hoặc triệu chứng ổn định sau > 1 năm từ chẩn đoán ban đầu hoặc tái thông mạch vành.<br>• <b>Scenario 5:</b> Bệnh nhân đau thắt ngực nghi ngờ do co thắt mạch vành (VSA) hoặc bệnh vi mạch vành (MVA/ANOCA/INOCA).<br>• <b>Scenario 6:</b> Bệnh nhân không triệu chứng tình cờ phát hiện bệnh mạch vành khi sàng lọc sức khỏe (CT mạch vành thấy vôi hóa hoặc mảng xơ vữa).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>6 kịch bản này bao quát toàn bộ hành trình của bệnh nhân tim mạch, từ lúc có triệu chứng lần đầu đến theo dõi trọn đời sau can thiệp.",
        "tags": ["IM-20a", "Scenarios", "ESC_Guidelines", "Classification"]
    },
    {
        "id": "IM20A_004",
        "type": "cloze",
        "text": "Bệnh nhân sau can thiệp đặt stent mạch vành (PCI) hoặc mổ bắc cầu (CABG) trong vòng {{c1::1 năm đầu tiên}} thuộc Kịch bản lâm sàng {{c1::Scenario 3}}; nếu ổn định sau {{c1::> 1 năm}} thì chuyển sang Kịch bản lâm sàng {{c1::Scenario 4}} theo ESC.",
        "extra": "Việc phân chia giúp cá thể hóa phác đồ kháng huyết khối và lịch theo dõi định kỳ."
    },
    {
        "id": "IM20A_005",
        "type": "cloze",
        "text": "Kịch bản lâm sàng {{c1::Scenario 5}} của CCS bao gồm các bệnh nhân có triệu chứng đau ngực nhưng chụp mạch vành không thấy hẹp tắc động mạch lớn (hẹp < 50%), thủ phạm do {{c1::co thắt mạch vành (VSA)}} hoặc {{c1::rối loạn chức năng vi mạch vành (MVA/ANOCA/INOCA)}}.",
        "extra": "Thể này phổ biến ở phụ nữ và bệnh nhân đái tháo đường."
    },
    {
        "id": "IM20A_006",
        "type": "basic",
        "front": "Sinh lý bệnh học của thiếu máu cơ tim trong CCS: Phân tích cán cân Cung — Cầu Oxy cơ tim và Dự trữ lưu lượng vành (CFR)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cầu Oxy cơ tim (MVO2) phụ thuộc 3 yếu tố:</b> (1) Tần số tim; (2) Sức co bóp cơ tim; (3) Sức căng thành tâm thất (áp lực và thể tích cuối tâm trương).<br>• <b>Cung Oxy cơ tim phụ thuộc:</b> Áp lực tưới máu mạch vành (áp lực tâm trương gốc ĐMC trừ áp lực cuối tâm trương thất trái), thời gian tâm trương, và sức cản mạch vành.<br>• <b>Dự trữ lưu lượng vành (Coronary Flow Reserve — CFR):</b> Tỷ số giữa lưu lượng mạch vành tối đa khi giãn mạch so với lưu lượng lúc nghỉ (Bình thường CFR = 3.5 - 5.0).<br>• Khi hẹp đường kính > 70%: CFR giảm sút nặng nề, lưu lượng máu không thể tăng lên khi gắng sức → Thiếu máu cơ tim dưới nội tâm mạc gây đau ngực.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Thời gian tâm trương quyết định tưới máu vành. Nhịp tim nhanh rút ngắn tâm trương, vừa làm tăng cầu MVO2 vừa làm giảm cung máu vành.",
        "tags": ["IM-20a", "Pathophysiology", "MVO2", "CFR"]
    },
    {
        "id": "IM20A_007",
        "type": "cloze",
        "text": "Dự trữ lưu lượng vành (CFR) ở người bình thường đạt từ {{c1::3.5 đến 5.0}}; khi mảng xơ vữa gây hẹp đường kính lòng mạch {{c1::> 70%}} (hoặc diện tích > 90%), CFR bắt đầu suy giảm rõ rệt và bệnh nhân sẽ xuất hiện đau thắt ngực khi gắng sức.",
        "extra": "CFR < 2.0 trên thăm dò chức năng là ngưỡng bệnh lý có ý nghĩa thiếu máu cục bộ."
    },
    {
        "id": "IM20A_008",
        "type": "basic",
        "front": "Đặc điểm hình thái của Mảng xơ vữa ổn định vs Mảng xơ vữa nguy cơ cao (High-Risk Plaque — HRP)? 4 dấu hiệu HRP trên CCTA?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Mảng xơ vữa ổn định:</b> Vỏ xơ dày, lõi lipid nhỏ, giàu tế bào cơ trơn và collagen, ít tế bào viêm.<br>• <b>Mảng xơ vữa nguy cơ cao (HRP / Mảng dễ vỡ):</b> Vỏ xơ mỏng (< 65 µm), lõi hoại tử lipid lớn (> 40% thể tích mảng), thâm nhiễm nhiều đại thực bào.<br>• <b>4 dấu hiệu HRP trên CCTA:</b><br>  1. Tái cấu trúc dương tính (Positive Remodeling - PR Index > 1.1).<br>  2. Mảng xơ vữa tỷ trọng thấp (Low-attenuation plaque < 30 HU).<br>  3. Dấu hiệu viền Napkin (Napkin-ring sign - lõi trung tâm tỷ trọng thấp bao quanh bởi viền tăng tỷ trọng).<br>  4. Vôi hóa đốm nhỏ rải rác (Spotty calcification < 3 mm).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Mảng xơ vữa HRP có nguy cơ nứt vỡ tạo huyết khối gây ACS gấp nhiều lần dù mức độ hẹp lòng mạch có thể chỉ ở mức nhẹ hoặc vừa.",
        "tags": ["IM-20a", "Atheroma", "HRP", "CCTA", "Napkin_Ring"]
    },
    {
        "id": "IM20A_009",
        "type": "cloze",
        "text": "4 đặc điểm của Mảng xơ vữa nguy cơ cao (HRP) trên phim CCTA gồm: (1) Tái cấu trúc dương tính (PR index > 1.1); (2) Mảng tỷ trọng thấp ({{c1::< 30 HU}}); (3) Dấu hiệu viền {{c1::Napkin (Napkin-ring sign)}}; và (4) Vôi hóa đốm nhỏ ({{c1::Spotty calcification < 3 mm}}).",
        "extra": "Sự hiện diện của dấu hiệu Napkin-ring làm tăng nguy cơ ACS trong tương lai."
    },

    # =========================================================================
    # PHẦN 2: TIẾP CẬN CHẨN ĐOÁN LÂM SÀNG & ĐÁNH GIÁ XÁC SUẤT TIỀN NGHIỆM (PTP)
    # =========================================================================
    {
        "id": "IM20A_010",
        "type": "basic",
        "front": "3 tiêu chuẩn kinh điển của Diamond-Forrester để khai thác và phân loại triệu chứng đau thắt ngực?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>3 tiêu chuẩn Diamond-Forrester:</b><br>  1. Đau thắt ngực cảm giác đè nặng, bóp nghẹt, thắt chẽn sau xương ức hoặc ngực trái, có thể lan lên cổ, cằm, vai trái, cánh tay trái.<br>  2. Cơn đau khởi phát khi gắng sức thể lực hoặc căng thẳng cảm xúc.<br>  3. Cơn đau giảm hoặc biến mất hoàn toàn trong vòng 2 - 5 phút sau khi nghỉ ngơi hoặc ngậm/xịt Nitroglycerin dưới lưỡi.<br>• <b>Phân loại 3 nhóm:</b><br>  - <b>Đau thắt ngực điển hình (Typical Angina):</b> Đủ cả 3 tiêu chuẩn.<br>  - <b>Đau thắt ngực không điển hình (Atypical Angina):</b> Thỏa mãn 2/3 tiêu chuẩn.<br>  - <b>Đau ngực không do tim (Non-anginal chest pain):</b> Chỉ thỏa mãn ≤ 1 tiêu chuẩn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Ở người cao tuổi, phụ nữ và bệnh nhân đái tháo đường, triệu chứng thường không điển hình (chỉ khó thở, mệt lả khi gắng sức).",
        "tags": ["IM-20a", "Diamond_Forrester", "Angina", "Diagnosis"]
    },
    {
        "id": "IM20A_011",
        "type": "cloze",
        "text": "Đau thắt ngực được phân loại là <b>Điển hình (Typical)</b> khi thỏa mãn đủ {{c1::3}} tiêu chuẩn Diamond-Forrester; là <b>Không điển hình (Atypical)</b> khi thỏa mãn {{c1::2/3}} tiêu chuẩn; và là <b>Đau ngực không do tim</b> khi chỉ có {{c1::≤ 1}} tiêu chuẩn.",
        "extra": "Diamond-Forrester là nền tảng để tính Xác suất tiền nghiệm (PTP)."
    },
    {
        "id": "IM20A_012",
        "type": "basic",
        "front": "Trình bày 4 mức độ đau thắt ngực theo thang điểm Hội Tim mạch Canada (CCS Functional Class)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>CCS I:</b> Hoạt động thể lực thông thường không gây đau ngực. Cơn đau chỉ xuất hiện khi gắng sức rất nặng, kéo dài hoặc đột ngột.<br>• <b>CCS II:</b> Giới hạn nhẹ hoạt động thể lực bình thường. Đau khi đi bộ nhanh > 2 dãy nhà hoặc leo dốc, leo gác > 1 tầng, đi bộ trong thời tiết lạnh/sau bữa ăn no.<br>• <b>CCS III:</b> Giới hạn rõ rệt hoạt động bình thường. Đau ngực xuất hiện khi đi bộ 1 - 2 dãy nhà trên mặt phẳng hoặc leo 1 tầng gác với tốc độ bình thường.<br>• <b>CCS IV:</b> Không thể thực hiện bất kỳ hoạt động thể lực nào mà không đau ngực. Cơn đau có thể xuất hiện ngay cả khi đang nghỉ ngơi.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>CCS III và IV là ngưỡng lâm sàng nặng, gợi ý bệnh mạch vành nhiều nhánh hoặc tổn thương thân chung LMCA.",
        "tags": ["IM-20a", "CCS_Class", "Severity", "Grading"]
    },
    {
        "id": "IM20A_013",
        "type": "cloze",
        "text": "Theo thang điểm CCS Canada, bệnh nhân đau ngực xuất hiện khi đi bộ chỉ từ 1 đến 2 dãy nhà hoặc leo 1 tầng gác với tốc độ bình thường được xếp vào {{c1::CCS III}}; nếu không thể làm bất kỳ việc gì hoặc đau ngay lúc nghỉ thì là {{c1::CCS IV}}.",
        "extra": "CCS II là giới hạn nhẹ (đi bộ > 2 dãy nhà hoặc leo > 1 tầng)."
    },
    {
        "id": "IM20A_014",
        "type": "basic",
        "front": "Xác suất tiền nghiệm (PTP) bệnh mạch vành tắc nghẽn theo ESC 2024 được tính dựa trên những yếu tố nào? Định hướng thăm dò theo các tầng PTP?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Yếu tố tính PTP:</b> Tuổi, giới tính, kiểu triệu chứng đau ngực (Điển hình, Không điển hình, Không do tim) hoặc khó thở đơn độc.<br>• <b>Định hướng chiến lược chẩn đoán:</b><br>  - <b>PTP rất thấp (< 5%):</b> Không cần làm thêm thăm dò tim mạch chuyên sâu, tìm nguyên nhân ngoài tim.<br>  - <b>PTP thấp - trung bình (5 - 15%):</b> Ưu tiên chụp Cắt lớp vi tính đa dãy mạch vành (CCTA) nhờ giá trị dự đoán âm tính cực cao (NPV > 98%).<br>  - <b>PTP trung bình - cao (> 15%):</b> Chỉ định CCTA hoặc Thăm dò chức năng không xâm lấn (Stress Echo, SPECT, CMR) để tìm bằng chứng thiếu máu cơ tim.<br>  - <b>Xác suất lâm sàng rất cao (> 85%):</b> Có thể chỉ định thẳng Chụp mạch vành xâm lấn (ICA) kèm đo sinh lý FFR/iFR.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bảng PTP 2019/2024 đã hạ thấp xác suất so với bảng cũ nhờ các nghiên cứu dịch tễ hiện đại phản ánh đúng tỷ lệ mắc bệnh thực tế.",
        "tags": ["IM-20a", "PTP", "ESC_2024", "Pre_Test_Probability"]
    },
    {
        "id": "IM20A_015",
        "type": "cloze",
        "text": "Theo ESC 2024, khi bệnh nhân có Xác suất tiền nghiệm (PTP) ở mức thấp đến trung bình ({{c1::5 - 15%}}), xét nghiệm được ưu tiên lựa chọn hàng đầu là {{c1::CCTA (Chụp cắt lớp vi tính mạch vành)}} do có giá trị dự đoán âm tính (NPV) cực cao (> 98%).",
        "extra": "CCTA giúp loại trừ an toàn bệnh mạch vành tắc nghẽn."
    },
    {
        "id": "IM20A_016",
        "type": "basic",
        "front": "Các yếu tố điều chỉnh trọng số (Modifiers) làm tăng hoặc giảm Khả năng lâm sàng mắc CAD (Clinical Likelihood of CAD)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Yếu tố làm TĂNG khả năng mắc CAD:</b><br>  - Yếu tố nguy cơ tim mạch: ĐTĐ, hút thuốc lá, rối loạn lipid máu, tăng huyết áp, tiền sử gia đình có bệnh mạch vành sớm.<br>  - Điện tâm đồ lúc nghỉ có biến đổi ST-T (ST chênh xuống, T âm) hoặc sóng Q hoại tử.<br>  - Rối loạn vận động vùng thất trái hoặc EF giảm trên siêu âm tim.<br>  - Vôi hóa động mạch vành trên X-quang hoặc CT ngực (Điểm CAC > 0).<br>  - Nghiệm pháp gắng sức điện tâm đồ dương tính.<br>• <b>Yếu tố làm GIẢM khả năng mắc CAD:</b><br>  - Điểm vôi hóa mạch vành Agatston CAC = 0.<br>  - Nghiệm pháp gắng sức điện tâm đồ đạt mức tối đa và hoàn toàn âm tính.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Điểm vôi hóa CAC = 0 là 'yếu tố bảo vệ mạnh nhất', làm giảm xác suất mắc bệnh mạch vành tắc nghẽn xuống dưới 1 - 2%.",
        "tags": ["IM-20a", "Clinical_Likelihood", "CAC_Score", "Risk_Modifiers"]
    },
    {
        "id": "IM20A_017",
        "type": "cloze",
        "text": "Điểm vôi hóa động mạch vành (CAC Score) bằng {{c1::0}} có giá trị làm giảm mạnh mẽ Khả năng lâm sàng mắc bệnh mạch vành (Clinical Likelihood), đưa xác suất tắc nghẽn xuống dưới {{c1::< 1 - 2%}}.",
        "extra": "Ngược lại, CAC > 400 hoặc CAC > bách phân vị 75 làm tăng vọt nguy cơ."
    },
    {
        "id": "IM20A_018",
        "type": "basic",
        "front": "Các dấu hiệu cảnh báo đỏ (Red Flags) chuyển biến từ CCS sang Hội chứng vành cấp (ACS) cần xử trí cấp cứu tức thì?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Đau thắt ngực xuất hiện khi nghỉ ngơi kéo dài > 20 phút (Rest angina).<br>• Đau thắt ngực mới khởi phát trong vòng 2 tháng gần đây đạt mức độ nặng từ CCS III trở lên (New-onset angina).<br>• Đau thắt ngực tiến triển tăng dần (Crescendo angina): Cơn đau dày hơn, dài hơn, nặng hơn, hoặc xuất hiện ở ngưỡng gắng sức thấp hơn rõ rệt.<br>• Cơn đau không đáp ứng sau 1 - 2 liều Nitroglycerin ngậm dưới lưỡi.<br>• Cơn đau kèm theo vã mồ hôi lạnh, tụt huyết áp, khó thở dữ dội hoặc ngất.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bất kỳ dấu hiệu nào trong số này đều biến bệnh nhân mạn tính thành ca cấp cứu ACS, cần chuyển phòng cấp cứu và làm ngay ECG + hs-Troponin.",
        "tags": ["IM-20a", "Red_Flags", "ACS_Conversion", "Emergency"]
    },
    {
        "id": "IM20A_019",
        "type": "cloze",
        "text": "Một cơn đau thắt ngực mạn tính chuyển thành <b>Đau thắt ngực không ổn định (UA / ACS)</b> khi có 1 trong 3 dạng: (1) Đau lúc nghỉ kéo dài {{c1::> 20 phút}}; (2) Mới khởi phát trong vòng {{c1::< 2 tháng}} đạt mức CCS III+; hoặc (3) Đau ngực tiến triển {{c1::tăng dần (Crescendo)}}.",
        "extra": "Troponin âm tính thì là UA; Troponin dương tính tăng động học thì là NSTEMI."
    },

    # =========================================================================
    # PHẦN 3: CẬN LÂM SÀNG CHẨN ĐOÁN HÌNH THÁI & CHỨC NĂNG
    # =========================================================================
    {
        "id": "IM20A_020",
        "type": "basic",
        "front": "Chỉ định, ưu điểm và chống chỉ định của Chụp cắt lớp vi tính mạch vành (CCTA) trong chẩn đoán CCS?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Chỉ định hàng đầu (Class I):</b> Bệnh nhân nghi ngờ CAD có PTP thấp đến trung bình (5 - 50%), cần loại trừ bệnh mạch vành.<br>• <b>Ưu điểm vượt trội:</b> Đánh giá trực tiếp giải phẫu lòng mạch, phát hiện mảng xơ vữa không gây hẹp, xác định mảng xơ vữa nguy cơ cao (HRP), NPV > 98%.<br>• <b>Chống chỉ định / Giới hạn:</b><br>  - Suy thận nặng (eGFR < 30 mL/min/1.73m2).<br>  - Dị ứng nặng với thuốc cản quang chứa I-ốt.<br>  - Rối loạn nhịp tim không kiểm soát (rung nhĩ nhanh), nhịp tim > 65 - 70 bpm không hạ được bằng chẹn beta.<br>  - Vôi hóa mạch vành quá nặng (CAC > 400 - 1000) gây xảo ảnh nở chùm tia (blooming artifact).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>CCTA là phương pháp duy nhất không xâm lấn cho phép nhìn thấy mảng xơ vữa ở giai đoạn sớm trước khi gây hẹp lòng mạch.",
        "tags": ["IM-20a", "CCTA", "Indications", "Contraindications"]
    },
    {
        "id": "IM20A_021",
        "type": "cloze",
        "text": "Chụp cắt lớp vi tính mạch vành (CCTA) bị giảm độ chính xác và dễ gây dương tính giả do xảo ảnh nở chùm tia (blooming artifact) khi điểm vôi hóa mạch vành {{c1::CAC > 400}} (hoặc > 1000 Agatston).",
        "extra": "Ở nhóm vôi hóa quá nặng, nên ưu tiên các thăm dò chức năng không xâm lấn."
    },
    {
        "id": "IM20A_022",
        "type": "basic",
        "front": "So sánh 3 phương pháp thăm dò chức năng không xâm lấn: Siêu âm tim gắng sức (Stress Echo), SPECT tưới máu cơ tim và Cộng hưởng từ tim gắng sức (Stress CMR)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Stress Echo (Thể lực hoặc Dobutamine):</b> Phát hiện rối loạn vận động vùng mới xuất hiện khi gắng sức. Ưu điểm: Sẵn có, chi phí thấp, không nhiễm xạ. Nhược điểm: Phụ thuộc cửa sổ siêu âm và kinh nghiệm người đọc.<br>• <b>SPECT tưới máu cơ tim (Myocardial Perfusion Imaging - MPI):</b> Dùng phóng xạ (Tc-99m Sestamibi) đánh giá khuyết xạ tưới máu khi gắng sức/Adenosine. Ưu điểm: Độ nhạy cao, chuẩn hóa. Nhược điểm: Nhiễm xạ, dễ bỏ sót thiếu máu cân bằng 3 thân mạch vành.<br>• <b>Stress CMR (Cộng hưởng từ tim gắng sức với Adenosine):</b> Độ phân giải không gian cực cao, đánh giá chính xác tưới máu cơ tim dưới nội tâm mạc và xơ hóa sẹo cơ tim (LGE). Nhược điểm: Chi phí cao, máy móc chuyên sâu, hạn chế ở người mang máy tạo nhịp kim loại.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Stress CMR có độ chính xác chẩn đoán cao nhất trong các thăm dò không xâm lấn hiện nay.",
        "tags": ["IM-20a", "Stress_Echo", "SPECT", "Stress_CMR", "Functional_Testing"]
    },
    {
        "id": "IM20A_023",
        "type": "cloze",
        "text": "Nghiệm pháp Siêu âm tim gắng sức (Stress Echo) chẩn đoán thiếu máu cơ tim dựa trên sự xuất hiện của {{c1::Rối loạn vận động vùng mới (giảm động / vô động)}} ở các phân vùng cơ tim khi tim đạt tần số mục tiêu.",
        "extra": "Dobutamine được dùng khi bệnh nhân không thể đạp xe hoặc chạy thảm lăn."
    },
    {
        "id": "IM20A_024",
        "type": "basic",
        "front": "Công thức tính và phân tầng nguy cơ của Thang điểm Tiên lượng Gắng sức Thảm lăn Duke (Duke Treadmill Score — DTS)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Công thức DTS:</b><br>  $$\\text{DTS} = \\text{Thời gian chạy (phút)} - 5 \\times [\\text{Độ chênh ST (mm)}] - 4 \\times [\\text{Chỉ số đau thắt ngực}]$$<br>• <i>Quy ước Chỉ số đau ngực:</i> 0 = Không đau; 1 = Đau nhưng không cần dừng nghiệm pháp; 2 = Đau ngực buộc phải dừng nghiệm pháp.<br>• <b>Phân tầng nguy cơ tử vong tim mạch 1 năm:</b><br>  - <b>Nguy cơ thấp (DTS ≥ +5):</b> Tỷ lệ tử vong tim mạch < 1%/năm.<br>  - <b>Nguy cơ trung bình (-10 ≤ DTS ≤ +4):</b> Tử vong 1 - 3%/năm.<br>  - <b>Nguy cơ cao (DTS ≤ -11):</b> Tử vong > 5%/năm → Chỉ định chụp mạch vành xâm lấn (ICA).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>DTS kết hợp cả thời gian gắng sức, mức độ biến đổi ECG và triệu chứng lâm sàng thành một chỉ số tiên lượng duy nhất.",
        "tags": ["IM-20a", "DTS", "Duke_Treadmill_Score", "Risk_Stratification"]
    },
    {
        "id": "IM20A_025",
        "type": "cloze",
        "text": "Thang điểm thảm lăn Duke (DTS) phân tầng <b>Nguy cơ cao</b> khi điểm số {{c1::DTS ≤ -11}}, dự báo tỷ lệ tử vong tim mạch {{c1::> 5%/năm}} và có chỉ định chụp mạch vành xâm lấn.",
        "extra": "DTS ≥ +5 là nguy cơ thấp (tử vong < 1%/năm)."
    },
    {
        "id": "IM20A_026",
        "type": "basic",
        "front": "Các tiêu chuẩn định lượng vùng cơ tim thiếu máu nguy cơ cao (High-Risk Ischemia) trên các thăm dò không xâm lấn?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Nghiệm pháp gắng sức ECG:</b> ST chênh xuống ≥ 2 mm ở ≥ 2 chuyển đạo, hoặc ST chênh lên ở aVR, hoặc tụt huyết áp tâm thu khi gắng sức, hoặc xuất hiện loạn nhịp thất.<br>• <b>SPECT tưới máu cơ tim:</b> Diện tích thiếu máu cơ tim ≥ 10% tổng khối cơ tâm thất trái.<br>• <b>Stress Echo:</b> Rối loạn vận động vùng mới ở ≥ 3 phân vùng thất trái.<br>• <b>Stress CMR:</b> Khuyết tưới máu cơ tim ≥ 2 phân vùng hoặc trễ thuốc muộn (LGE) diện rộng.<br>• <b>CCTA:</b> Hẹp ≥ 50% Thân chung vành trái (LMCA) hoặc hẹp ≥ 70% ở đoạn gần cả 3 thân mạch vành (3-vessel disease).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bệnh nhân có thiếu máu cơ tim nguy cơ cao bắt buộc phải hội chẩn chụp mạch vành và xem xét tái thông để cải thiện tiên lượng sống còn.",
        "tags": ["IM-20a", "High_Risk_Ischemia", "Criteria", "Prognosis"]
    },
    {
        "id": "IM20A_027",
        "type": "cloze",
        "text": "Trên phim SPECT xạ hình tưới máu cơ tim, vùng thiếu máu cục bộ được xếp vào nhóm <b>Nguy cơ cao (High Risk)</b> khi diện tích tổn thương chiếm {{c1::≥ 10%}} tổng khối lượng cơ tâm thất trái.",
        "extra": "Trên Stress Echo là rối loạn vận động ≥ 3 phân vùng."
    },

    # =========================================================================
    # PHẦN 4: THĂM DÒ HUYẾT ĐỘNG XÂM LẤN (FFR, iFR, CFR, IMR) & ANOCA/INOCA
    # =========================================================================
    {
        "id": "IM20A_028",
        "type": "basic",
        "front": "Định nghĩa, nguyên lý và ngưỡng can thiệp của Phân suất dự trữ lưu lượng vành FFR (Fractional Flow Reserve)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa:</b> FFR là tỷ số giữa áp lực mạch vành tối đa sau chỗ hẹp (Pd) so với áp lực gốc động mạch chủ trước chỗ hẹp (Pa) trong điều kiện giãn mạch vi tuần hoàn tối đa (Hyperemia):<br>  $$\\text{FFR} = \\frac{P_d}{P_a}$$<br>• <b>Thuốc gây giãn mạch tối đa:</b> Truyền tĩnh mạch liên tục Adenosine ($140\\text{ µg/kg/phút}$) hoặc tiêm chọn lọc vào lòng mạch vành.<br>• <b>Ngưỡng chẩn đoán & can thiệp:</b><br>  - **FFR ≤ 0.80:** Tổn thương gây thiếu máu cơ tim có ý nghĩa huyết động → **Chỉ định đặt Stent (PCI)**.<br>  - **FFR > 0.80:** Không gây thiếu máu có ý nghĩa → **Trì hoãn PCI an toàn, chỉ điều trị nội khoa tối ưu (OMT)** (Dựa trên thử nghiệm DEFER, FAME 1 & FAME 2).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>FFR chuyển đổi tư duy điều trị từ 'đặt stent theo mắt nhìn giải phẫu' sang 'đặt stent theo chứng cứ sinh lý chức năng'.",
        "tags": ["IM-20a", "FFR", "Physiology", "PCI", "Threshold"]
    },
    {
        "id": "IM20A_029",
        "type": "cloze",
        "text": "Phân suất dự trữ lưu lượng vành (FFR) được đo trong trạng thái giãn mạch tối đa bằng {{c1::Adenosine}}; tổn thương có giá trị {{c1::FFR ≤ 0.80}} được chứng minh là gây thiếu máu cơ tim có ý nghĩa và có chỉ định đặt Stent (PCI).",
        "extra": "Nếu FFR > 0.80, trì hoãn PCI và điều trị thuốc có kết cục tim mạch tương đương hoặc tốt hơn."
    },
    {
        "id": "IM20A_030",
        "type": "basic",
        "front": "Chỉ số iFR (Instantaneous Wave-Free Ratio) khác FFR ở điểm nào? Ngưỡng chẩn đoán và ưu điểm lâm sàng?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Khác biệt cốt lõi:</b> iFR đo tỷ số áp lực $P_d / P_a$ trong một 'khoảng thời gian không có sóng cản trở' (Wave-free period) ở giữa đến cuối kỳ tâm trương, lúc mà sức cản vi mạch tự nhiên ở mức thấp nhất và hằng định.<br>• **Ưu điểm:** **KHÔNG CẦN DÙNG THUỐC GIÃN MẠCH ADENOSINE** → Thủ thuật nhanh hơn, chi phí thấp hơn, không gây tác dụng phụ (khó thở, tụt HA, block AV của Adenosine).<br>• <b>Ngưỡng chẩn đoán & can thiệp:</b><br>  - **iFR ≤ 0.89:** Có ý nghĩa thiếu máu cơ tim → **Chỉ định PCI** (Chứng minh không thua kém FFR qua thử nghiệm DEFINE-FLAIR và iFR-SWEDEHEART).<br>  - **iFR > 0.89:** Trì hoãn PCI an toàn.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>iFR và FFR bổ sung cho nhau hoàn hảo trong phòng can thiệp tim mạch (Cathlab).",
        "tags": ["IM-20a", "iFR", "Non_Hyperemic", "Physiology", "Threshold"]
    },
    {
        "id": "IM20A_031",
        "type": "cloze",
        "text": "Chỉ số áp lực thì tâm trương không cần thuốc giãn mạch (iFR) có ngưỡng can thiệp đặt Stent tương đương FFR là {{c1::iFR ≤ 0.89}}, được chứng minh qua hai thử nghiệm lâm sàng ngẫu nhiên {{c1::DEFINE-FLAIR}} và {{c1::iFR-SWEDEHEART}}.",
        "extra": "iFR loại bỏ hoàn toàn nhu cầu dùng Adenosine."
    },
    {
        "id": "IM20A_032",
        "type": "basic",
        "front": "Phân biệt 4 chỉ số sinh lý mạch vành: FFR, iFR, CFR, IMR? Chỉ số nào đo mạch lớn, chỉ số nào đo vi mạch?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>FFR (Hyperemic $P_d/P_a$):</b> Đo đoạn hẹp MẠCH LỚN (cần Adenosine). Ngưỡng bệnh lý: $\\le 0.80$.<br>• <b>iFR (Diastolic $P_d/P_a$):</b> Đo đoạn hẹp MẠCH LỚN (KHÔNG cần Adenosine). Ngưỡng bệnh lý: $\\le 0.89$.<br>• <b>CFR (Coronary Flow Reserve):</b> Đo dự trữ lưu lượng của CẢ MẠCH LỚN VÀ VI MẠCH. Ngưỡng bệnh lý: $< 2.0$.<br>• <b>IMR (Index of Microcirculatory Resistance):</b> Đo chuyên biệt KHÁNG TRỞ GIƯỜNG VI MẠCH (đo bằng phương pháp pha loãng nhiệt). Ngưỡng bệnh lý: $\\ge 25$.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Khi mạch lớn không hẹp (FFR > 0.80) mà bệnh nhân vẫn đau ngực, CFR < 2.0 kèm IMR ≥ 25 là bằng chứng xác thực của Bệnh vi mạch vành (CMD / MVA).",
        "tags": ["IM-20a", "Hemodynamics", "FFR", "iFR", "CFR", "IMR"]
    },
    {
        "id": "IM20A_033",
        "type": "cloze",
        "text": "Chỉ số Kháng trở vi tuần hoàn vành (IMR) chuyên biệt dùng để đánh giá giường vi mạch; giá trị {{c1::IMR ≥ 25}} kết hợp với {{c1::CFR < 2.0}} là tiêu chuẩn vàng chẩn đoán Rối loạn chức năng vi mạch vành (CMD / MVA).",
        "extra": "Thường được đo trong quy trình chẩn đoán chuyên sâu INOCA."
    },
    {
        "id": "IM20A_034",
        "type": "basic",
        "front": "Quy trình chẩn đoán và phân định 2 thể bệnh chính của ANOCA / INOCA (Đau thắt ngực vi mạch vs Co thắt mạch vành)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa:</b> Bệnh nhân có triệu chứng đau ngực hoặc bằng chứng thiếu máu cơ tim nhưng chụp mạch vành thấy động mạch thượng tâm mạc bình thường hoặc hẹp không tắc nghẽn (hẹp < 50%, FFR > 0.80).<br>• <b>2 thể bệnh chính:</b><br>  1. <b>Đau thắt ngực vi mạch (Microvascular Angina — MVA / CMD):</b> Kháng trở vi mạch tăng (IMR ≥ 25) và/hoặc Dự trữ vành giảm (CFR < 2.0) mà không có co thắt mạch lớn.<br>  2. <b>Đau thắt ngực do co thắt (Vasospastic Angina — VSA / Prinzmetal):</b> Cơn co thắt động mạch vành thượng tâm mạc khi làm Test kích thích Acetylcholine trong buồng tim (gây hẹp lòng mạch > 90% kèm tái lập cơn đau ngực và ST biến đổi).<br>• <b>Thể hỗn hợp:</b> Có cả rối loạn vi mạch và co thắt mạch máu.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Phân biệt 2 thể là bắt buộc vì thuốc điều trị hoàn toàn trái ngược nhau (Chẹn beta tốt cho MVA nhưng chống chỉ định trong VSA).",
        "tags": ["IM-20a", "ANOCA", "INOCA", "MVA", "VSA", "Acetylcholine"]
    },
    {
        "id": "IM20A_035",
        "type": "cloze",
        "text": "Test kích thích trong buồng tim bằng {{c1::Acetylcholine}} được xem là dương tính xác định Đau thắt ngực do co thắt (VSA) khi gây co thắt lòng mạch lớn {{c1::> 90%}} kèm tái lập triệu chứng đau ngực và biến đổi đoạn ST trên điện tâm đồ.",
        "extra": "Nếu Acetylcholine chỉ gây đau ngực và biến đổi ST mà mạch lớn không co thắt > 90% thì là co thắt vi mạch."
    },
    {
        "id": "IM20A_036",
        "type": "basic",
        "front": "Phác đồ điều trị nội khoa chuyên biệt cho Đau thắt ngực vi mạch (MVA) vs Đau thắt ngực do co thắt (VSA)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Điều trị MVA (Vi mạch):</b><br>  - Hàng 1: Thuốc chẹn Beta giao cảm (Bisoprolol, Nebivolol) hoặc Chẹn kênh Calci DHP (Amlodipine).<br>  - Hàng 2: Phối hợp thêm Ranolazine, Trimetazidine, Ivabradine hoặc Nicorandil.<br>  - Nền tảng: Statin + Ức chế men chuyển (ACEi) để cải thiện chức năng nội mô vi mạch.<br>• <b>Điều trị VSA (Co thắt mạch vành):</b><br>  - Hàng 1: **Chẹn kênh Calci (CCB)** liều cao (Diltiazem, Verapamil, Amlodipine).<br>  - Hàng 2: Phối hợp Nitrat tác dụng kéo dài hoặc Nicorandil.<br>  - <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI:</b> **THUỐC CHẸN BETA GIAO CẢM KHÔNG CHỌN LỌC** (do ức chế thụ thể beta-2 làm tăng trương lực alpha gây co thắt mạch vành nặng hơn).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Chẹn beta là thuốc hàng đầu cho đau ngực do xơ vữa và vi mạch, nhưng là 'chất độc' làm nặng thêm cơn đau thắt ngực Prinzmetal/VSA.",
        "tags": ["IM-20a", "MVA_Treatment", "VSA_Treatment", "Contraindications"]
    },
    {
        "id": "IM20A_037",
        "type": "cloze",
        "text": "Trong điều trị Đau thắt ngực do co thắt (VSA / Prinzmetal), thuốc lựa chọn số 1 là {{c1::Chẹn kênh Calci (CCB)}}; nhóm thuốc bị <b>CHỐNG CHỈ ĐỊNH</b> vì làm tăng co thắt mạch vành qua kích thích thụ thể alpha là {{c1::Thuốc chẹn Beta giao cảm}}.",
        "extra": "Có thể phối hợp thêm Nitrat kéo dài hoặc Nicorandil nếu chưa kiểm soát được cơn."
    },

    # =========================================================================
    # PHẦN 5: ĐIỀU TRỊ NỘI KHOA KIỂM SOÁT TRIỆU CHỨNG ĐAU THẮT NGỰC
    # =========================================================================
    {
        "id": "IM20A_038",
        "type": "basic",
        "front": "Hướng dẫn chuẩn xử trí cắt cơn đau thắt ngực cấp tính bằng Nitroglycerin ngậm dưới lưỡi hoặc dạng xịt?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tư thế:</b> Bệnh nhân phải ngồi nghỉ hoặc nằm đầu cao (tránh đứng vì nguy cơ tụt HA tư thế và ngất).<br>• <b>Liều lượng & Cách dùng:</b><br>  - Ngậm dưới lưỡi 1 viên Nitroglycerin 0.4 - 0.5 mg (hoặc xịt 1 - 2 nhát dưới lưỡi).<br>  - Sau 5 phút nếu chưa đỡ: Dùng tiếp liều thứ 2.<br>  - Sau 5 phút nữa nếu vẫn đau: Dùng liều thứ 3 (Tối đa 3 liều trong 15 phút).<br>• <b>Cảnh báo cấp cứu:</b> Nếu sau liều đầu tiên (hoặc liều thứ 2) cơn đau không thuyên giảm hoặc tăng lên → Gọi ngay Cấp cứu 115 vì nguy cơ cao đã chuyển thành Nhồi máu cơ tim cấp.<br>• <b>Chống chỉ định tuyệt đối:</b> Đang dùng thuốc ức chế PDE-5 (Sildenafil trong 24h, Tadalafil trong 48h), HA tâm thu < 90 mmHg, hẹp van ĐMC khít, bệnh cơ tim phì đại tắc nghẽn (HOCM).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Phối hợp Nitrat với thuốc ức chế PDE-5 gây giãn mạch ồ ạt, tụt huyết áp kịch phát kháng trị đe dọa tính mạng.",
        "tags": ["IM-20a", "Nitroglycerin", "Acute_Angina", "PDE5_Contraindication"]
    },
    {
        "id": "IM20A_039",
        "type": "cloze",
        "text": "Nitroglycerin ngậm dưới lưỡi tuyệt đối <b>CHỐNG CHỈ ĐỊNH</b> khi bệnh nhân đang sử dụng thuốc ức chế PDE-5 điều trị rối loạn cương dương gồm: Sildenafil trong vòng {{c1::24 giờ}} hoặc Tadalafil trong vòng {{c1::48 giờ}} do nguy cơ tụt huyết áp kịch phát gây tử vong.",
        "extra": "Cũng chống chỉ định khi HA tâm thu < 90 mmHg hoặc NMCT thất phải."
    },
    {
        "id": "IM20A_040",
        "type": "basic",
        "front": "Thuốc chẹn Beta giao cảm trong điều trị CCS: Cơ chế, đích nhịp tim cần đạt, các thuốc được ưu tiên và chống chỉ định?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cơ chế:</b> Giảm nhịp tim, giảm sức co bóp cơ tim, kéo dài thời gian tâm trương → Giảm mạnh nhu cầu tiêu thụ oxy (MVO2) và tăng tưới máu vành.<br>• <b>Đích nhịp tim lúc nghỉ:</b> **55 - 60 chu kỳ/phút** (nhịp tim khi gắng sức vừa < 100 bpm).<br>• <b>Thuốc ưu tiên:</b> Chẹn chọn lọc beta-1 (Bisoprolol 2.5 - 10 mg/ngày, Metoprolol Succinate 50 - 200 mg/ngày, Nebivolol 2.5 - 10 mg/ngày) hoặc chẹn alpha+beta (Carvedilol 6.25 - 25 mg × 2 lần/ngày).<br>• <b>Chống chỉ định:</b> Nhịp chậm xoang (< 50 bpm), Block nhĩ thất độ 2 - 3 chưa đặt máy tạo nhịp, Hội chứng suy nút xoang, Hen phế quản nặng chưa kiểm soát, Sốc tim hoặc suy tim mất bù cấp tính.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Chẹn beta là thuốc duy nhất vừa kiểm soát đau thắt ngực vừa cải thiện sống còn ở bệnh nhân có kèm giảm phân suất tống máu thất trái (HFrEF) hoặc sau NMCT.",
        "tags": ["IM-20a", "Beta_Blockers", "Heart_Rate_Target", "Contraindications"]
    },
    {
        "id": "IM20A_041",
        "type": "cloze",
        "text": "Khi sử dụng thuốc chẹn Beta giao cảm để điều trị kiểm soát cơn đau thắt ngực mạn tính, đích nhịp tim lúc nghỉ cần đạt là {{c1::55 - 60 chu kỳ/phút}} để tối ưu hóa thời gian tưới máu tâm trương và giảm tiêu thụ oxy cơ tim.",
        "extra": "Liều lượng phải được chỉnh tăng dần (titration) từ liều thấp."
    },
    {
        "id": "IM20A_042",
        "type": "basic",
        "front": "Phân loại và ứng dụng lâm sàng của Thuốc chẹn kênh Calci (CCB) Dihydropyridine (DHP) vs Non-Dihydropyridine (Non-DHP)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Nhóm DHP (Amlodipine, Felodipine, Lercanidipine):</b><br>  - Tác dụng chọn lọc cao trên cơ trơn mạch máu → Giãn tiểu động mạch toàn thân và mạch vành, giảm hậu tải.<br>  - Ít ảnh hưởng nút dẫn truyền tim → **Có thể phối hợp an toàn với Thuốc chẹn Beta**.<br>  - Tác dụng phụ: Phù chân do giãn mao mạch, nhịp tim nhanh phản xạ.<br>• <b>Nhóm Non-DHP (Verapamil, Diltiazem):</b><br>  - Tác dụng ức chế chọn lọc trên nút xoang và nút nhĩ thất → Giảm nhịp tim và giảm sức co bóp cơ tim.<br>  - Dùng thay thế chẹn beta khi bệnh nhân có chống chỉ định (hen phế quản, COPD).<br>  - **CẢNH BÁO: TRÁNH PHỐI HỢP NON-DHP VỚI CHẸN BETA** (nguy cơ gây chậm nhịp tim nặng, block AV hoàn toàn và suy tim cấp); **CHỐNG CHỈ ĐỊNH TRONG SUY TIM EF GIẢM (HFrEF)**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Công thức phối hợp kinh điển: Chẹn Beta + DHP-CCB (Amlodipine) là cặp đôi hiệp đồng mạnh nhất.",
        "tags": ["IM-20a", "CCB", "Amlodipine", "Verapamil", "Diltiazem", "Drug_Interaction"]
    },
    {
        "id": "IM20A_043",
        "type": "cloze",
        "text": "Tuyệt đối không phối hợp thuốc chẹn kênh Calci nhóm Non-DHP ({{c1::Verapamil}} hoặc {{c1::Diltiazem}}) với thuốc {{c1::Chẹn Beta giao cảm}} do nguy cơ ức chế nút dẫn truyền gây Block nhĩ thất độ cao và ngừng tim.",
        "extra": "Chỉ phối hợp chẹn Beta với nhóm DHP-CCB như Amlodipine."
    },
    {
        "id": "IM20A_044",
        "type": "basic",
        "front": "Cơ chế, chỉ định và lưu ý lâm sàng của 4 thuốc chống đau thắt ngực hàng 2 (Second-Line): Ranolazine, Ivabradine, Nicorandil, Trimetazidine?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Ranolazine (500 - 1000 mg × 2 lần/ngày):</b> Ức chế dòng Natri muộn ($I_{\\text{Na,late}}$) → Giảm quá tải Calci nội bào thì tâm trương → Cải thiện giãn cơ tim. Không ảnh hưởng HA và nhịp tim. Cần theo dõi khoảng QT.<br>• <b>Ivabradine (2.5 - 7.5 mg × 2 lần/ngày):</b> Ức chế chọn lọc kênh $I_f$ ở nút xoang → Làm chậm nhịp tim đơn thuần, không hạ HA. Chỉ định khi nhịp xoang ≥ 70 bpm không dung nạp hoặc chưa đạt đích dù đã dùng chẹn beta. Vô tác dụng nếu Rung nhĩ.<br>• <b>Nicorandil (10 - 20 mg × 2 lần/ngày):</b> Cơ chế kép (Hoạt hóa kênh Kali nhạy ATP + Đồng vận Nitrat) → Giãn cả động mạch và tĩnh mạch. Tác dụng phụ: Loét niêm mạc miệng, đường tiêu hóa.<br>• <b>Trimetazidine (35 mg × 2 lần/ngày):</b> Ức chế enzyme 3-KAT (3-ketoacyl-CoA thiolase) → Chuyển hóa năng lượng từ oxy hóa acid béo sang oxy hóa glucose (tiết kiệm oxy). Chống chỉ định ở bệnh nhân Parkinson hoặc rối loạn vận động.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Các thuốc hàng 2 là vũ khí đắc lực để phối hợp khi huyết áp hoặc nhịp tim của bệnh nhân quá thấp không thể tăng thêm liều chẹn beta/CCB.",
        "tags": ["IM-20a", "Second_Line", "Ranolazine", "Ivabradine", "Nicorandil", "Trimetazidine"]
    },
    {
        "id": "IM20A_045",
        "type": "cloze",
        "text": "Thuốc <b>Ivabradine</b> chỉ có tác dụng giảm nhịp tim khi bệnh nhân đang ở {{c1::Nhịp xoang}} với tần số {{c1::≥ 70 chu kỳ/phút}}; thuốc hoàn toàn vô tác dụng và không được chỉ định ở bệnh nhân bị {{c1::Rung nhĩ}}.",
        "extra": "Ivabradine tác động chọn lọc trên kênh If tại nút xoang."
    },
    {
        "id": "IM20A_046",
        "type": "cloze",
        "text": "Thuốc <b>Trimetazidine</b> tối ưu hóa năng lượng tế bào cơ tim qua ức chế enzyme 3-KAT; thuốc bị <b>CHỐNG CHỈ ĐỊNH</b> ở bệnh nhân mắc bệnh {{c1::Parkinson}} hoặc có các triệu chứng rối loạn vận động run tay chân.",
        "extra": "Ranolazine cần theo dõi khoảng QT trên điện tâm đồ."
    },
    {
        "id": "IM20A_047",
        "type": "basic",
        "front": "Chiến lược phối hợp thuốc chống đau thắt ngực theo các đặc điểm huyết động học (ESC Guidelines)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Huyết áp thấp (HATT < 100 mmHg):</b> Ưu tiên Ranolazine hoặc Trimetazidine; hoặc Ivabradine (nếu nhịp nhanh); Chẹn beta liều rất thấp.<br>• <b>Nhịp tim nhanh (> 80 bpm lúc nghỉ):</b> Chẹn beta + DHP-CCB; hoặc Chẹn beta + Ivabradine.<br>• <b>Nhịp tim chậm (< 60 bpm lúc nghỉ):</b> Ưu tiên DHP-CCB (Amlodipine); phối hợp Ranolazine, Trimetazidine hoặc Nitrat kéo dài. TRÁNH chẹn beta, Non-DHP và Ivabradine.<br>• <b>Suy tim kèm EF giảm (LVEF ≤ 40%):</b> BẮT BUỘC dùng Chẹn Beta (Bisoprolol, Carvedilol, Metoprolol succinate) + Phối hợp Ivabradine (nếu nhịp xoang ≥ 70 bpm) hoặc Trimetazidine/Ranolazine. TRÁNH Diltiazem/Verapamil.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Cá thể hóa điều trị theo huyết áp và nhịp tim giúp tránh các biến cố tụt huyết áp và chậm nhịp tim nguy hiểm.",
        "tags": ["IM-20a", "Stepwise_Strategy", "Hemodynamics", "Algorithm"]
    },
    {
        "id": "IM20A_048",
        "type": "cloze",
        "text": "Ở bệnh nhân Bệnh mạch vành mạn kèm theo Suy tim phân suất tống máu giảm (LVEF ≤ 40%), thuốc chống đau thắt ngực hàng 1 bắt buộc là {{c1::Chẹn Beta giao cảm}} (Bisoprolol / Carvedilol); nhóm thuốc chống chỉ định tuyệt đối là {{c1::Chẹn kênh Calci Non-DHP (Verapamil/Diltiazem)}}.",
        "extra": "Nếu nhịp xoang vẫn ≥ 70 bpm có thể phối hợp thêm Ivabradine."
    },

    # =========================================================================
    # PHẦN 6: PHÒNG NGỪA BIẾN CỐ TIM MẠCH & GDMT
    # =========================================================================
    {
        "id": "IM20A_049",
        "type": "basic",
        "front": "Mục tiêu kiểm soát LDL-C kép và Phác đồ hạ lipid máu 3 tầng ở bệnh nhân Bệnh mạch vành mạn (Nguy cơ rất cao)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Mục tiêu LDL-C kép (ESC 2019/2024):</b><br>  1. Giảm **≥ 50%** nồng độ LDL-C so với mức nền ban đầu.<br>  2. Đạt nồng độ tuyệt đối **< 1.4 mmol/L (< 55 mg/dL)**.<br>  *(Nếu tái phát biến cố trong vòng 2 năm dù đang dùng statin tối đa: Mục tiêu hạ xuống < 1.0 mmol/L).*<br>• <b>Phác đồ 3 tầng theo bậc:</b><br>  - <b>Tầng 1:</b> Statin cường độ cao liều tối đa dung nạp (Atorvastatin 40 - 80 mg hoặc Rosuvastatin 20 - 40 mg).<br>  - <b>Tầng 2 (sau 4 - 6 tuần chưa đạt):</b> Phối hợp thêm **Ezetimibe 10 mg/ngày** (hạ thêm 15 - 20% LDL-C).<br>  - <b>Tầng 3 (sau 4 - 6 tuần vẫn chưa đạt):</b> Phối hợp thêm **Thuốc ức chế PCSK9** (Evolocumab 140 mg/2 tuần, Alirocumab 75 - 150 mg/2 tuần) hoặc **siRNA Inclisiran** (mỗi 6 tháng); hoặc Bempedoic acid.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Nguyên lý 'The Lower, The Longer, The Better' đã được chứng minh qua hàng loạt thử nghiệm lâm sàng mốc (IMPROVE-IT, FOURIER, ODYSSEY).",
        "tags": ["IM-20a", "Lipid_Targets", "High_Intensity_Statin", "Ezetimibe", "PCSK9i"]
    },
    {
        "id": "IM20A_050",
        "type": "cloze",
        "text": "Mục tiêu kiểm soát lipid máu ở bệnh nhân Bệnh mạch vành mạn (nhóm nguy cơ rất cao) bắt buộc đạt đồng thời 2 tiêu chí: Giảm {{c1::≥ 50%}} nồng độ LDL-C ban đầu VÀ đạt mức tuyệt đối {{c1::< 1.4 mmol/L (< 55 mg/dL)}}.",
        "extra": "Nếu có biến cố tim mạch thứ 2 trong vòng 2 năm, mục tiêu hạ tiếp xuống < 1.0 mmol/L (< 40 mg/dL)."
    },
    {
        "id": "IM20A_051",
        "type": "basic",
        "front": "Liệu pháp Kháng kết tập tiểu cầu đơn (SAPT): So sánh Aspirin và Clopidogrel trong dự phòng thứ phát CCS?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Aspirin (75 - 100 mg/ngày):</b> Lựa chọn chuẩn mực nền tảng trọn đời (Class I). Cơ chế: Ức chế không thuận nghịch enzyme COX-1 → Giảm tổng hợp Thromboxane A2.<br>• <b>Clopidogrel (75 mg/ngày):</b> Lựa chọn thay thế hàng đầu khi bệnh nhân dị ứng hoặc không dung nạp Aspirin (Class I).<br>• Dữ liệu từ các nghiên cứu dài hạn (như HOST-EXAM) cho thấy Clopidogrel đơn trị liệu lâu dài có thể mang lại hiệu quả bảo vệ tim mạch vượt trội hơn nhẹ và ít biến chứng xuất huyết tiêu hóa hơn so với Aspirin đơn trị liệu.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>SAPT là viên gạch nền tảng không thể thiếu trong đơn thuốc của bất kỳ bệnh nhân bệnh mạch vành nào.",
        "tags": ["IM-20a", "SAPT", "Aspirin", "Clopidogrel", "HOST_EXAM"]
    },
    {
        "id": "IM20A_052",
        "type": "cloze",
        "text": "Trong dự phòng thứ phát biến cố tim mạch ở bệnh nhân CCS, liều chuẩn của Aspirin đơn trị liệu là {{c1::75 - 100 mg/ngày}}; thuốc thay thế hàng đầu khi có chống chỉ định hoặc dị ứng Aspirin là {{c1::Clopidogrel 75 mg/ngày}}.",
        "extra": "HOST-EXAM trial cho thấy Clopidogrel duy trì dài hạn có ưu thế vượt trội."
    },
    {
        "id": "IM20A_053",
        "type": "basic",
        "front": "Liệu pháp Kháng huyết khối đường kép (DPI — Dual Pathway Inhibition): Bằng chứng từ thử nghiệm COMPASS và chỉ định?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Phác đồ DPI:</b> Phối hợp **Rivaroxaban liều mạch máu ($2.5\\text{ mg} \\times 2$ lần/ngày)** + **Aspirin ($100\\text{ mg}$/ngày)**.<br>• <b>Bằng chứng thử nghiệm COMPASS (NEJM 2017):</b> Giảm **24%** biến cố gộp chính MACE (tử vong tim mạch, đột quỵ, NMCT) và giảm **18%** tử vong do mọi nguyên nhân so với Aspirin đơn độc.<br>• <b>Chỉ định (ESC 2024 Class IIa):</b> Bệnh nhân CCS có nguy cơ thiếu máu cục bộ cao (bệnh nhiều nhánh mạch vành, kèm đái tháo đường, suy thận nhẹ-vừa, hoặc bệnh động mạch ngoại biên PAD) và **KHÔNG có nguy cơ xuất huyết cao**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>DPI vừa ức chế tiểu cầu (qua Aspirin) vừa ức chế thrombin thế hệ mới (qua Rivaroxaban liều thấp), tạo ra 'chiếc lưới bảo vệ kép'.",
        "tags": ["IM-20a", "DPI", "Rivaroxaban", "COMPASS_Trial", "Antithrombotic"]
    },
    {
        "id": "IM20A_054",
        "type": "cloze",
        "text": "Liệu pháp Kháng huyết khối đường kép (DPI) theo thử nghiệm COMPASS phối hợp Aspirin 100 mg/ngày với {{c1::Rivaroxaban 2.5 mg × 2 lần/ngày}}, giúp giảm {{c1::24%}} nguy cơ biến cố tim mạch chính (MACE).",
        "extra": "Chỉ định cho bệnh nhân nguy cơ tắc mạch cao và nguy cơ xuất huyết thấp."
    },
    {
        "id": "IM20A_055",
        "type": "basic",
        "front": "Mục tiêu kiểm soát Huyết áp, Đái tháo đường và Lối sống ở bệnh nhân Bệnh mạch vành mạn?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Huyết áp:</b> Mục tiêu chung **< 130/80 mmHg** (nhưng không hạ HATT < 120 mmHg và HATTr < 70 mmHg để đảm bảo tưới máu vành tâm trương). Ưu tiên nhóm ACEi/ARB và Chẹn Beta.<br>• <b>Đái tháo đường:</b> Mục tiêu $\\text{HbA1c} < 7.0\\%$. **Bắt buộc ưu tiên nhóm thuốc ức chế SGLT2 (Dapagliflozin, Empagliflozin) hoặc đồng vận GLP-1 RA (Semaglutide, Liraglutide)** vì đã được chứng minh giảm độc lập biến cố tim mạch và tử vong.<br>• <b>Lối sống:</b> Cai thuốc lá tuyệt đối; tập thể dục nhịp điệu ≥ 150 - 300 phút/tuần; chế độ ăn Địa Trung Hải; chỉ số BMI $20 - 25\\text{ kg/m}^2$, vòng eo $< 90\\text{ cm}$ (nam) hoặc $< 80\\text{ cm}$ (nữ).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>SGLT2i và GLP-1 RA hiện nay được xem là thuốc bảo vệ tim mạch - thận hơn là đơn thuần hạ đường huyết.",
        "tags": ["IM-20a", "GDMT", "Blood_Pressure", "Diabetes", "SGLT2i", "GLP1_RA"]
    },
    {
        "id": "IM20A_056",
        "type": "cloze",
        "text": "Ở bệnh nhân Bệnh mạch vành mạn có kèm Đái tháo đường type 2, hai nhóm thuốc hạ đường huyết bắt buộc ưu tiên hàng đầu do đã chứng minh giảm tử vong và biến cố tim mạch là {{c1::Thuốc ức chế SGLT2}} và {{c1::Đồng vận thụ thể GLP-1 (GLP-1 RA)}}.",
        "extra": "Mục tiêu huyết áp chung là < 130/80 mmHg."
    },

    # =========================================================================
    # PHẦN 7: TÁI THÔNG MẠCH VÀNH (PCI VS CABG) & BẰNG CHỨNG LÂM SÀNG
    # =========================================================================
    {
        "id": "IM20A_057",
        "type": "basic",
        "front": "Bài học cốt lõi từ các thử nghiệm lâm sàng mốc: COURAGE, ISCHEMIA, ORBITA 1&2, FAME 1&2 và REVIVED-BCIS2?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>COURAGE (NEJM 2007) & ISCHEMIA (NEJM 2020):</b> Ở bệnh nhân CCS ổn định (dù có thiếu máu cơ tim mức độ vừa-nặng), chiến lược can thiệp xâm lấn ban đầu (PCI/CABG + OMT) **KHÔNG làm giảm tỷ lệ tử vong do mọi nguyên nhân hoặc NMCT** so với chiến lược điều trị nội khoa tối ưu (OMT) bảo tồn ban đầu.<br>• <b>ORBITA (Lancet 2018) & ORBITA-2 (NEJM 2023):</b> Can thiệp PCI có tác dụng giảm đau thắt ngực và tăng khả năng gắng sức rõ rệt so với giả can thiệp (sham procedure), đặc biệt ở bệnh nhân còn triệu chứng dù đã dùng thuốc.<br>• <b>FAME 1 & 2 (NEJM 2009, 2012):</b> Can thiệp PCI có hướng dẫn của sinh lý FFR (chỉ đặt stent khi FFR ≤ 0.80) giảm 86% nhu cầu tái thông khẩn cấp so với chỉ dùng thuốc.<br>• <b>REVIVED-BCIS2 (NEJM 2022):</b> Ở bệnh nhân suy tim thiếu máu cục bộ nặng (EF ≤ 35%), PCI không cải thiện tử vong hay nhập viện vì suy tim so với OMT.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Tái thông trong CCS nhằm 2 mục đích riêng biệt: (1) Cải thiện tiên lượng sống còn (chỉ ở nhóm tổn thương nguy cơ cao); (2) Cải thiện triệu chứng chất lượng sống khi thuốc chưa kiểm soát được.",
        "tags": ["IM-20a", "Trials", "ISCHEMIA", "COURAGE", "ORBITA", "FAME", "REVIVED"]
    },
    {
        "id": "IM20A_058",
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng mốc <b>ISCHEMIA (NEJM 2020)</b> chứng minh rằng ở bệnh nhân CCS ổn định có thiếu máu cơ tim vừa đến nặng, can thiệp tái thông mạch vành sớm phối hợp OMT {{c1::KHÔNG làm giảm}} tỷ lệ tử vong tim mạch hoặc nhồi máu cơ tim so với chiến lược điều trị nội khoa bảo tồn (OMT).",
        "extra": "Tuy nhiên, tái thông giúp cải thiện triệu chứng đau ngực và chất lượng sống vượt trội."
    },
    {
        "id": "IM20A_059",
        "type": "basic",
        "front": "2 nhóm chỉ định của Tái thông mạch vành trong CCS: Chỉ định cải thiện tiên lượng sống còn vs Chỉ định cải thiện triệu chứng?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>1. Chỉ định Tái thông để CẢI THIỆN TIÊN LƯỢNG SỐNG CÒN (Prognostic Indication):</b><br>  - Hẹp thân chung động mạch vành trái (LMCA) ≥ 50%.<br>  - Hẹp đoạn gần động mạch liên thất trước (Proximal LAD) ≥ 50%.<br>  - Bệnh 2 hoặc 3 thân mạch vành kèm suy giảm chức năng thất trái (LVEF ≤ 35%).<br>  - Vùng thiếu máu cơ tim diện rộng (> 10% cơ thất trái trên SPECT hoặc ≥ 3 vùng trên Stress Echo).<br>  - Chỉ còn một nhánh động mạch vành duy nhất còn thông suốt bị hẹp ≥ 50%.<br>• <b>2. Chỉ định Tái thông để CẢI THIỆN TRIỆU CHỨNG (Symptomatic Indication):</b><br>  - Đau thắt ngực dai dẳng (CCS II - IV) gây ảnh hưởng chất lượng sống dù đã tối ưu hóa thuốc chống đau thắt ngực (OMT).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Đây là kim chỉ nam giúp bác sĩ quyết định ca nào bắt buộc phải can thiệp để cứu mạng, ca nào chỉ can thiệp khi bệnh nhân còn đau ngực.",
        "tags": ["IM-20a", "Revascularization", "Indications", "Prognosis", "Symptoms"]
    },
    {
        "id": "IM20A_060",
        "type": "cloze",
        "text": "Tái thông mạch vành trong CCS được chỉ định để <b>Cải thiện Tiên lượng sống còn</b> trong các trường hợp: (1) Hẹp thân chung {{c1::LMCA ≥ 50%}}; (2) Hẹp đoạn gần {{c1::Proximal LAD ≥ 50%}}; (3) Bệnh nhiều thân kèm {{c1::LVEF ≤ 35%}}; hoặc (4) Thiếu máu diện rộng {{c1::> 10%}} thất trái.",
        "extra": "Các trường hợp khác tái thông chủ yếu để cải thiện chất lượng sống khi OMT thất bại."
    },
    {
        "id": "IM20A_061",
        "type": "basic",
        "front": "Tiêu chuẩn lựa chọn giữa Can thiệp mạch vành qua da (PCI) vs Phẫu thuật bắc cầu mạch vành (CABG): Thang điểm SYNTAX và vai trò Heart Team?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Vai trò Hội chẩn Nhóm Tim mạch (Heart Team):</b> Bắt buộc phối hợp Bác sĩ Tim mạch can thiệp, Phẫu thuật viên tim mạch và Bác sĩ Tim mạch lâm sàng để thống nhất phương án tối ưu.<br>• <b>Phân tầng theo Thang điểm giải phẫu SYNTAX Score:</b><br>  - <b>SYNTAX thấp (0 - 22):</b> PCI và CABG có kết cục tương đương → Ưu tiên PCI do ít xâm lấn.<br>  - <b>SYNTAX trung bình (23 - 32):</b> Bệnh 3 thân hoặc tổn thương thân chung phức tạp → Ưu tiên **CABG**.<br>  - <b>SYNTAX cao (≥ 33):</b> **Ưu tiên tuyệt đối CABG** (CABG giảm tử vong và nhồi máu cơ tim vượt trội so với PCI).<br>• <b>Yếu tố nghiêng về CABG:</b> Bệnh nhân đái tháo đường, tổn thương vôi hóa nặng lan tỏa, tắc mạn tính hoàn toàn (CTO), không dung nạp DAPT, có chỉ định mổ van tim kèm theo.<br>• <b>Yếu tố nghiêng về PCI:</b> Tuổi cao, nhiều bệnh đồng mắc nặng (EuroSCORE II hoặc STS score cao), giải phẫu không phù hợp làm cầu nối, nguy cơ phẫu thuật cao.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Ở bệnh nhân đái tháo đường mắc bệnh nhiều thân mạch vành, thử nghiệm FREEDOM chứng minh CABG giảm tử vong vượt trội so với đặt stent.",
        "tags": ["IM-20a", "PCI_vs_CABG", "SYNTAX_Score", "Heart_Team", "Diabetes"]
    },
    {
        "id": "IM20A_062",
        "type": "cloze",
        "text": "Theo thang điểm giải phẫu mạch vành SYNTAX, ở bệnh nhân mắc bệnh 3 thân mạch vành có điểm {{c1::SYNTAX ≥ 33}}, phương pháp tái thông ưu tiên tuyệt đối để cải thiện sống còn là {{c1::Phẫu thuật bắc cầu mạch vành (CABG)}}.",
        "extra": "Nếu SYNTAX 0 - 22 thì PCI và CABG có kết cục tương đương."
    },

    # =========================================================================
    # PHẦN 8: QUẢN LÝ KHÁNG HUYẾT KHỐI SAU PCI & RUNG NHĨ
    # =========================================================================
    {
        "id": "IM20A_063",
        "type": "basic",
        "front": "Thời gian dùng Kháng kết tập tiểu cầu kép (DAPT) sau can thiệp PCI chương trình trong CCS theo ESC Guidelines?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Phác đồ chuẩn mặc định:</b> DAPT gồm **Aspirin (75 - 100 mg) + Clopidogrel (75 mg/ngày)** trong vòng **6 tháng**, sau đó chuyển sang dùng SAPT đơn trị liệu suốt đời (Aspirin hoặc Clopidogrel).<br>• <b>Bệnh nhân có Nguy cơ Xuất huyết Cao (HBR - High Bleeding Risk / PRECISE-DAPT ≥ 25):</b> Rút ngắn DAPT xuống **1 - 3 tháng**, sau đó đơn trị liệu.<br>• <b>Bệnh nhân có Nguy cơ Tắc mạch rất cao và Nguy cơ Xuất huyết thấp:</b> Có thể cân nhắc kéo dài DAPT > 6 tháng hoặc chuyển sang phác đồ DPI (Aspirin + Rivaroxaban 2.5 mg × 2).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Trong PCI chương trình của CCS, Clopidogrel là thuốc ức chế P2Y12 được khuyến cáo chuẩn (không cần dùng Ticagrelor/Prasugrel trừ khi có biến cố tắc stent trước đó).",
        "tags": ["IM-20a", "DAPT_Duration", "Elective_PCI", "Clopidogrel", "HBR"]
    },
    {
        "id": "IM20A_064",
        "type": "cloze",
        "text": "Thời gian dùng kháng kết tập tiểu cầu kép (DAPT = Aspirin + Clopidogrel) chuẩn mặc định sau can thiệp PCI chương trình trong CCS là {{c1::6 tháng}}; ở bệnh nhân có nguy cơ xuất huyết cao (HBR) có thể rút ngắn xuống {{c1::1 - 3 tháng}}.",
        "extra": "Sau khi kết thúc DAPT, bệnh nhân duy trì SAPT đơn trị liệu suốt đời."
    },
    {
        "id": "IM20A_065",
        "type": "basic",
        "front": "Chiến lược dùng thuốc chống đông và chống kết tập tiểu cầu ở bệnh nhân CCS có Rung nhĩ cần can thiệp PCI (Bộ ba vs Bộ đôi)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Giai đoạn nằm viện / Can thiệp:</b> Liệu pháp bộ ba (**Triple Therapy: NOAC + Aspirin + Clopidogrel**) trong thời gian ngắn tối đa **≤ 1 tuần** (từ lúc làm thủ thuật đến khi xuất viện).<br>• <b>Sau xuất viện đến 6 - 12 tháng:</b> Chuyển ngay sang Liệu pháp bộ đôi (**Double Therapy: NOAC liều chuẩn + Clopidogrel 75 mg/ngày**). DỪNG ASPIRIN.<br>• <b>Sau 12 tháng:</b> DỪNG TOÀN BỘ THUỐC KHÁNG TIỂU CẦU, chuyển sang **ĐƠN TRỊ LIỆU BẰNG THUỐC CHỐNG ĐÔNG ĐƯỜNG UỐNG (NOAC MONOTHERAPY)** suốt đời (Dựa trên thử nghiệm AFIRE và OAC-ALONE).<br>• <b>Lưu ý:</b> Ưu tiên NOAC (Apixaban, Rivaroxaban, Dabigatran, Edoxaban) hơn là Kháng Vitamin K (Warfarin).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Dừng Aspirin sớm giúp giảm hơn 40% nguy cơ xuất huyết nặng mà không làm tăng nguy cơ tắc Stent hay đột quỵ.",
        "tags": ["IM-20a", "AFib_PCI", "Triple_Therapy", "Double_Therapy", "NOAC", "AFIRE_Trial"]
    },
    {
        "id": "IM20A_066",
        "type": "cloze",
        "text": "Ở bệnh nhân Rung nhĩ sau can thiệp đặt Stent mạch vành (PCI), Liệu pháp bộ ba (NOAC + Aspirin + Clopidogrel) chỉ được dùng tối đa trong vòng {{c1::≤ 1 tuần}}, sau đó chuyển sang Liệu pháp bộ đôi (NOAC + Clopidogrel) đến {{c1::6 - 12 tháng}}, và sau 12 tháng chỉ duy trì {{c1::Đơn trị liệu NOAC}} suốt đời.",
        "extra": "Thử nghiệm AFIRE chứng minh đơn trị NOAC sau 1 năm an toàn và hiệu quả nhất."
    },

    # =========================================================================
    # PHẦN 9 & 10: QUẢN LÝ DÀI HẠN, 10 BẪY LÂM SÀNG & CÂU HỎI TỰ LƯỢNG GIÁ
    # =========================================================================
    {
        "id": "IM20A_067",
        "type": "basic",
        "front": "Lịch trình theo dõi định kỳ và các xét nghiệm cần làm ở bệnh nhân Bệnh mạch vành mạn ngoại trú?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Lần khám đầu sau can thiệp/chẩn đoán:</b> Tái khám sau **4 - 6 tuần** (kiểm tra triệu chứng, chức năng thận, men gan, bilan lipid máu để chỉnh liều statin).<br>• <b>Theo dõi định kỳ hàng năm:</b><br>  - Đánh giá lâm sàng, tuân thủ thuốc và lối sống mỗi **6 - 12 tháng**.<br>  - Bilan lipid máu, đường huyết, HbA1c, chức năng thận hàng năm.<br>  - Điện tâm đồ (ECG) 12 chuyển đạo mỗi năm một lần.<br>  - Tiêm phòng vắc-xin Cúm mùa định kỳ hàng năm (giúp giảm biến cố tim mạch).<br>  - Siêu âm tim định kỳ mỗi **2 - 3 năm** (hoặc sớm hơn nếu có thay đổi triệu chứng hoặc suy tim tiến triển).<br>• <b>Không làm thường quy:</b> Không chỉ định Stress test hoặc CCTA/ICA định kỳ ở bệnh nhân hoàn toàn không có triệu chứng.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Vắc-xin cúm là chỉ định Class I trong CCS vì nhiễm virus cúm kích hoạt phản ứng viêm toàn thân dễ gây nứt vỡ mảng xơ vữa.",
        "tags": ["IM-20a", "Follow_up", "Vaccination", "Monitoring", "Outpatient"]
    },
    {
        "id": "IM20A_068",
        "type": "cloze",
        "text": "Theo khuyến cáo tim mạch quốc tế, bệnh nhân Bệnh mạch vành mạn được chỉ định bắt buộc tiêm phòng {{c1::Vắc-xin Cúm mùa}} định kỳ hàng năm do đã được chứng minh làm giảm đáng kể nguy cơ nhồi máu cơ tim và tử vong tim mạch.",
        "extra": "Cúm kích hoạt bão cytokine và viêm toàn thân gây nứt vỡ mảng xơ vữa."
    },
    {
        "id": "IM20A_069",
        "type": "basic",
        "front": "10 Bẫy lâm sàng sống còn (Clinical Traps) cần tránh trong chẩn đoán và điều trị Bệnh mạch vành mạn?",
        "back": "<b>📖 Văn bản gốc:</b><br>1. Chẩn đoán nhầm đau ngực do NMCT thành dưới thành 'viêm loét dạ dày'.<br>2. Bỏ sót thiếu máu cơ tim 'im lặng' ở bệnh nhân đái tháo đường và phụ nữ cao tuổi.<br>3. Dùng thuốc chẹn beta cho bệnh nhân đau thắt ngực do co thắt (VSA).<br>4. Phối hợp chẹn beta với thuốc chẹn canxi Non-DHP (Verapamil/Diltiazem).<br>5. Bỏ qua chống chỉ định của Nitroglycerin khi bệnh nhân đang dùng thuốc ức chế PDE-5.<br>6. Lạm dụng đặt Stent ở bệnh nhân CCS ổn định chỉ dựa vào hình ảnh hẹp trên mắt thường mà không đo FFR/iFR.<br>7. Kéo dài liệu pháp bộ ba (Triple Therapy) quá 1 tuần ở bệnh nhân Rung nhĩ sau PCI.<br>8. Chỉ hạ LDL-C theo 1 tiêu chí mà không đạt đồng thời cả 2 tiêu chí (giảm ≥ 50% VÀ < 1.4 mmol/L).<br>9. Dùng Trimetazidine cho bệnh nhân mắc hội chứng Parkinson.<br>10. Ngừng thuốc kháng tiểu cầu quá sớm sau đặt stent gây huyết khối trong stent cấp tính.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Nắm vững 10 bẫy lâm sàng giúp bảo vệ an toàn tính mạng cho người bệnh trong thực hành hàng ngày.",
        "tags": ["IM-20a", "Clinical_Traps", "Pitfalls", "Safety"]
    },
    {
        "id": "IM20A_070",
        "type": "cloze",
        "text": "Bẫy lâm sàng nguy hiểm hàng đầu trong điều trị CCS là lạm dụng đặt Stent mạch vành (PCI) ở tổn thương hẹp trung gian 50 - 69% chỉ bằng mắt thường mà không đo thăm dò chức năng sinh lý {{c1::FFR}} hoặc {{c1::iFR}}.",
        "extra": "Thử nghiệm DEFER và FAME chứng minh hẹp không gây thiếu máu thì đặt stent không mang lại lợi ích."
    },

    # =========================================================================
    # CÁC THẺ CLOZE & DRILL-DOWN BỔ SUNG ĐỂ ĐẠT > 100 THẺ
    # =========================================================================
    {
        "id": "IM20A_071",
        "type": "cloze",
        "text": "Tỷ số giữa áp lực mạch vành tối đa sau chỗ hẹp (Pd) và áp lực gốc động mạch chủ (Pa) khi giãn mạch vi mạch tối đa bằng Adenosine được gọi là {{c1::FFR (Fractional Flow Reserve)}}.",
        "extra": "Bình thường FFR = 1.0; ngưỡng thiếu máu bệnh lý là ≤ 0.80."
    },
    {
        "id": "IM20A_072",
        "type": "cloze",
        "text": "Đặc điểm của mảng xơ vữa nguy cơ cao (HRP) trên phim CCTA có chỉ số tái cấu trúc dương tính (Positive Remodeling Index) khi giá trị {{c1::PR > 1.1}}.",
        "extra": "Phản ánh hiện tượng thành mạch phình ra ngoài để bù trừ (Glagov remodeling)."
    },
    {
        "id": "IM20A_073",
        "type": "cloze",
        "text": "Mảng xơ vữa có tỷ trọng thấp (Low-attenuation plaque) trên CCTA phản ánh lõi lipid hoại tử giàu chất béo khi có đậm độ đo được {{c1::< 30 HU}}.",
        "extra": "Đây là một trong 4 dấu hiệu của mảng xơ vữa dễ vỡ (vulnerable plaque)."
    },
    {
        "id": "IM20A_074",
        "type": "cloze",
        "text": "Điện tâm đồ lúc nghỉ ở bệnh nhân Bệnh mạch vành mạn (CCS) có thể hoàn toàn bình thường ở khoảng {{c1::50% - 60%}} các trường hợp khi không có cơn đau ngực.",
        "extra": "ECG bình thường lúc nghỉ không bao giờ loại trừ được bệnh mạch vành."
    },
    {
        "id": "IM20A_075",
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng <b>COURAGE (NEJM 2007)</b> tiến hành trên 2.287 bệnh nhân CCS chứng minh PCI phối hợp OMT không làm giảm tỷ lệ {{c1::Tử vong do mọi nguyên nhân hoặc Nhồi máu cơ tim}} so với OMT đơn thuần sau 4.6 năm theo dõi.",
        "extra": "Khẳng định vai trò nền tảng của điều trị nội khoa tối ưu."
    },
    {
        "id": "IM20A_076",
        "type": "cloze",
        "text": "Trong thử nghiệm <b>ORBITA (Lancet 2018)</b> sử dụng đối chứng giả can thiệp (Sham control), PCI giúp cải thiện thời gian gắng sức thêm {{c1::16.6 giây}} so với thủ thuật giả ở bệnh nhân có tổn thương hẹp 1 nhánh mạch vành.",
        "extra": "ORBITA-2 sau đó khẳng định PCI giảm gánh nặng cơn đau rõ rệt ở bệnh nhân không dùng thuốc."
    },
    {
        "id": "IM20A_077",
        "type": "cloze",
        "text": "Thuốc <b>Ranolazine</b> tác động bằng cách ức chế chọn lọc dòng {{c1::Natri muộn (I_Na,late)}}, giúp ngăn ngừa hiện tượng quá tải ion {{c1::Calci}} nội bào trong thì tâm trương của tế bào cơ tim thiếu máu.",
        "extra": "Thuốc không làm thay đổi nhịp tim và huyết áp."
    },
    {
        "id": "IM20A_078",
        "type": "cloze",
        "text": "Tác dụng phụ ngoại ý đặc trưng nhất của thuốc <b>Nicorandil</b> là gây {{c1::Loét niêm mạc miệng và đường tiêu hóa}} kéo dài khó liền, buộc phải ngừng thuốc.",
        "extra": "Nicorandil mở kênh Kali nhạy ATP và giải phóng NO."
    },
    {
        "id": "IM20A_079",
        "type": "cloze",
        "text": "Thuốc chẹn kênh Calci nhóm Dihydropyridine (DHP) như <b>Amlodipine</b> tác động giãn cơ trơn tiểu động mạch, có tác dụng phụ phổ biến nhất là {{c1::Phù mắt cá chân (phù chân)}} do tăng áp lực mao mạch.",
        "extra": "Phù này do giãn tiểu động mạch trước mao mạch, không đáp ứng với thuốc lợi tiểu."
    },
    {
        "id": "IM20A_080",
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng <b>IMPROVE-IT (NEJM 2015)</b> chứng minh việc phối hợp thêm {{c1::Ezetimibe 10 mg}} vào Simvastatin 40 mg giúp giảm tiếp nồng độ LDL-C và giảm thêm {{c1::6.4%}} biến cố tim mạch chính.",
        "extra": "Mở ra kỷ nguyên điều trị phối hợp hạ lipid máu đa tầng."
    },
    {
        "id": "IM20A_081",
        "type": "cloze",
        "text": "Thuốc ức chế men PCSK9 dạng kháng thể đơn dòng gồm {{c1::Evolocumab}} và {{c1::Alirocumab}} giúp tăng mật độ thụ thể LDL-R trên màng tế bào gan, hạ thêm {{c1::50% - 60%}} nồng độ LDL-C.",
        "extra": "Được tiêm dưới da mỗi 2 tuần hoặc mỗi 4 tuần."
    },
    {
        "id": "IM20A_082",
        "type": "cloze",
        "text": "Thuốc công nghệ sinh học ức chế PCSK9 dạng phân tử nhỏ can thiệp RNA (siRNA) là {{c1::Inclisiran}}, có phác đồ tiêm dưới da cách nhau mỗi {{c1::6 tháng}} một lần sau 2 liều khởi đầu.",
        "extra": "Inclisiran ức chế tổng hợp protein PCSK9 ngay tại nhân tế bào gan."
    },
    {
        "id": "IM20A_083",
        "type": "cloze",
        "text": "Bệnh nhân có điểm giải phẫu mạch vành SYNTAX ở mức {{c1::0 - 22}} (SYNTAX thấp) có kết cục điều trị giữa can thiệp đặt Stent (PCI) và mổ bắc cầu (CABG) là {{c1::Tương đương nhau}}.",
        "extra": "Ưu tiên PCI vì tính chất ít xâm lấn và hồi phục nhanh."
    },
    {
        "id": "IM20A_084",
        "type": "cloze",
        "text": "Ở bệnh nhân Đái tháo đường mắc bệnh nhiều thân mạch vành phức tạp, thử nghiệm <b>FREEDOM (NEJM 2012)</b> chứng minh phương pháp {{c1::Mổ bắc cầu mạch vành (CABG)}} giảm tỷ lệ tử vong và nhồi máu cơ tim vượt trội so với {{c1::Đặt Stent (PCI)}}.",
        "extra": "Đái tháo đường là yếu tố chỉ định quan trọng nghiêng về CABG."
    },
    {
        "id": "IM20A_085",
        "type": "cloze",
        "text": "Trong chẩn đoán xác định Hội chứng suy nút xoang hoặc block dẫn truyền khi dùng chẹn beta, nhịp tim lúc nghỉ giảm xuống {{c1::< 50 chu kỳ/phút}} kèm theo triệu chứng chóng mặt, choáng váng là chỉ định phải giảm liều hoặc tạm ngừng thuốc.",
        "extra": "Cần đo điện tâm đồ và Holter ECG 24h để đánh giá."
    },
    {
        "id": "IM20A_086",
        "type": "cloze",
        "text": "Tác dụng bảo vệ tim mạch của Aspirin đạt được qua ức chế không thuận nghịch enzyme {{c1::COX-1 (Cyclooxygenase-1)}}, làm ngừng sản xuất chất gây ngưng tập tiểu cầu mạnh mẽ là {{c1::Thromboxane A2}} trong suốt đời sống 7 - 10 ngày của tiểu cầu.",
        "extra": "Aspirin liều thấp 75 - 100 mg ức chế chọn lọc COX-1."
    },
    {
        "id": "IM20A_087",
        "type": "cloze",
        "text": "Thuốc <b>Clopidogrel</b> là tiền chất cần được chuyển hóa qua enzyme gan {{c1::CYP2C19}} để trở thành dạng có hoạt tính ức chế không thuận nghịch thụ thể {{c1::P2Y12}} trên màng tiểu cầu.",
        "extra": "Bệnh nhân mang gen CYP2C19 mất chức năng (*2, *3) có thể bị kháng Clopidogrel."
    },
    {
        "id": "IM20A_088",
        "type": "cloze",
        "text": "Khi sử dụng thuốc ức chế PCSK9 hoặc phối hợp Statin + Ezetimibe, nồng độ LDL-C có thể giảm xuống rất thấp (< 0.5 mmol/L hoặc < 20 mg/dL); các nghiên cứu an toàn chứng minh mức LDL-C cực thấp này {{c1::Hoàn toàn an toàn}} và không gây tổn thương thần kinh hay suy giảm nhận thức.",
        "extra": "Khẳng định nguyên lý an toàn của mục tiêu 'The Lower, The Better'."
    },
    {
        "id": "IM20A_089",
        "type": "cloze",
        "text": "Dấu hiệu viền <b>Napkin-ring sign</b> trên phim CCTA là hình ảnh một vùng lõi mảng xơ vữa có tỷ trọng thấp (< 30 HU) được bao bọc xung quanh bởi một viền {{c1::Tăng tỷ trọng mỏng}}, phản ánh mảng xơ vữa vỏ mỏng lõi lipid lớn (TCFA).",
        "extra": "Đây là dấu hiệu có giá trị tiên đoán nứt vỡ mảng xơ vữa cao nhất."
    },
    {
        "id": "IM20A_090",
        "type": "cloze",
        "text": "Trong phân loại đau thắt ngực CCS Canada, bệnh nhân đau ngực xuất hiện khi gắng sức rất nặng, đột ngột hoặc kéo dài, trong khi sinh hoạt bình thường không bị hạn chế được xếp vào độ {{c1::CCS I}}.",
        "extra": "CCS I là mức độ nhẹ nhất trên thang điểm."
    },
    {
        "id": "IM20A_091",
        "type": "cloze",
        "text": "Khi bệnh nhân đau ngực nghi ngờ do co thắt mạch vành (VSA), thời điểm xuất hiện cơn đau điển hình nhất là vào {{c1::Ban đêm hoặc sáng sớm lúc đang ngủ / nghỉ ngơi}}, kèm theo đoạn ST chênh lên thoáng qua trên ECG.",
        "extra": "Khác với đau thắt ngực do xơ vữa xuất hiện khi gắng sức ban ngày."
    },
    {
        "id": "IM20A_092",
        "type": "cloze",
        "text": "Cơ chế sinh lý học giải thích vì sao bệnh nhân suy tim nặng có thể bị thiếu máu cơ tim dù mạch vành không hẹp nhiều là do {{c1::Áp lực cuối tâm trương thất trái (LVEDP) tăng cao}}, làm ép các mạch máu dưới nội tâm mạc và làm giảm áp lực tưới máu vành.",
        "extra": "Áp lực tưới máu vành = Áp lực ĐMC tâm trương - LVEDP."
    },
    {
        "id": "IM20A_093",
        "type": "cloze",
        "text": "Bệnh nhân mắc Bệnh mạch vành mạn (CCS) có chỉ định tái thông mạch vành để <b>Cải thiện tiên lượng</b> khi tổn thương gây hẹp đoạn gần của động mạch {{c1::Liên thất trước (Proximal LAD)}} với mức độ hẹp {{c1::≥ 50%}}.",
        "extra": "LAD đoạn gần cấp máu cho diện tích cơ tim rất lớn của thất trái."
    },
    {
        "id": "IM20A_094",
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng <b>AFIRE (NEJM 2019)</b> trên bệnh nhân Rung nhĩ ổn định sau can thiệp PCI > 1 năm chứng minh rằng đơn trị liệu bằng {{c1::Rivaroxaban}} an toàn hơn và giảm xuất huyết rõ rệt so với phối hợp Rivaroxaban + Kháng tiểu cầu.",
        "extra": "Sau 1 năm chỉ duy trì 1 thuốc chống đông duy nhất."
    },
    {
        "id": "IM20A_095",
        "type": "cloze",
        "text": "Trong phác đồ xử trí Đau thắt ngực cấp tính, số liều Nitroglycerin ngậm dưới lưỡi tối đa được phép dùng trước khi chuyển cấp cứu là {{c1::3 liều}} trong vòng {{c1::15 phút}} (cách nhau mỗi 5 phút).",
        "extra": "Nếu sau liều 1 - 2 không đỡ phải gọi ngay cấp cứu 115."
    },
    {
        "id": "IM20A_096",
        "type": "cloze",
        "text": "Chỉ số <b>RFR (Resting Full-cycle Ratio)</b> và <b>dPR (Diastolic Pressure Ratio)</b> là các chỉ số sinh lý mạch vành không dùng thuốc giãn mạch, có ngưỡng chẩn đoán thiếu máu cơ tim tương đương iFR là {{c1::≤ 0.89}}.",
        "extra": "Cung cấp kết quả đo áp lực không cần Adenosine."
    },
    {
        "id": "IM20A_097",
        "type": "cloze",
        "text": "Bệnh nhân có điểm vôi hóa mạch vành Agatston {{c1::CAC > 400}} được xếp vào nhóm nguy cơ tim mạch rất cao và có khả năng cao bị bệnh mạch vành tắc nghẽn nặng.",
        "extra": "Cần kết hợp thăm dò chức năng hoặc chụp mạch vành."
    },
    {
        "id": "IM20A_098",
        "type": "cloze",
        "text": "Trong nghiệm pháp gắng sức thảm lăn, dấu hiệu đoạn ST {{c1::Chênh lên}} ở các chuyển đạo không có sóng Q hoại tử là dấu hiệu thiếu máu cơ tim xuyên thành cực kỳ nghiêm trọng, buộc phải ngừng ngay nghiệm pháp.",
        "extra": "Nguy cơ cao tắc nghẽn nặng hoặc co thắt mạch lớn."
    },
    {
        "id": "IM20A_099",
        "type": "cloze",
        "text": "Ở bệnh nhân CCS có phân suất tống máu thất trái giảm (HFrEF), hai thuốc chẹn kênh Calci nhóm Non-DHP là {{c1::Verapamil}} và {{c1::Diltiazem}} bị <b>CHỐNG CHỈ ĐỊNH</b> do tác dụng ức chế co bóp cơ tim âm tính làm nặng thêm tình trạng suy tim.",
        "extra": "Chỉ được dùng Amlodipine hoặc Felodipine nếu cần hạ áp thêm."
    },
    {
        "id": "IM20A_100",
        "type": "cloze",
        "text": "Khuyến cáo dinh dưỡng cho bệnh nhân Bệnh mạch vành mạn là tuân thủ chế độ ăn {{c1::Địa Trung Hải (Mediterranean Diet)}}, giàu chất xơ, dầu ô-liu, cá béo và các loại hạt, hạn chế mỡ bão hòa và thịt đỏ.",
        "extra": "Chế độ ăn Địa Trung Hải giảm 30% biến cố tim mạch nguyên phát."
    },
    {
        "id": "IM20A_101",
        "type": "cloze",
        "text": "Thuốc <b>Bempedoic acid</b> (liều 180 mg/ngày) là thuốc hạ lipid máu mới tác động ức chế enzyme {{c1::ATP Citrate Lyase (ACL)}} ở thượng nguồn của HMG-CoA Reductase, dùng hiệu quả cho bệnh nhân {{c1::Không dung nạp Statin}}.",
        "extra": "Thử nghiệm CLEAR Outcomes chứng minh giảm biến cố tim mạch."
    },
    {
        "id": "IM20A_102",
        "type": "cloze",
        "text": "Trong điều trị đau thắt ngực, thuốc chẹn Beta giao cảm có tác dụng chọn lọc trên thụ thể beta-1 cao nhất là {{c1::Bisoprolol}} hoặc {{c1::Nebivolol}} (Nebivolol có thêm tác dụng giãn mạch qua kích thích giải phóng NO).",
        "extra": "Ít gây co thắt phế quản hơn các chẹn beta không chọn lọc."
    },
    {
        "id": "IM20A_103",
        "type": "cloze",
        "text": "Bệnh nhân mắc Bệnh mạch vành mạn có kèm bệnh động mạch ngoại biên (PAD) được chứng minh hưởng lợi ích giảm biến cố đoạn chi và tử vong tim mạch lớn nhất từ phác đồ kháng huyết khối đường kép {{c1::DPI (Aspirin + Rivaroxaban 2.5 mg × 2)}}.",
        "extra": "Dữ liệu phân nhóm từ thử nghiệm COMPASS."
    },
    {
        "id": "IM20A_104",
        "type": "cloze",
        "text": "Thuốc <b>Nebivolol</b> ngoài tác dụng ức chế chọn lọc thụ thể beta-1 còn có đặc tính độc đáo là kích thích thụ thể {{c1::Beta-3}} trên tế bào nội mô mạch máu, làm tăng tổng hợp và phóng thích chất giãn mạch {{c1::Nitric Oxide (NO)}}.",
        "extra": "Giúp cải thiện chức năng nội mô và ít gây rối loạn cương dương."
    },
    {
        "id": "IM20A_105",
        "type": "cloze",
        "text": "Đích kiểm soát đường huyết tổng quát ở phần lớn bệnh nhân đái tháo đường mắc CCS là mức {{c1::HbA1c < 7.0%}}; ở người cao tuổi nhiều bệnh lý đi kèm hoặc có nguy cơ hạ đường huyết cao có thể nới lỏng lên {{c1::HbA1c < 8.0%}}.",
        "extra": "Tránh hạ đường huyết quá mức vì có thể kích hoạt biến cố tim mạch cấp."
    },
    {
        "id": "IM20A_106",
        "type": "cloze",
        "text": "Khi bệnh nhân đang dùng Statin xuất hiện đau cơ, xét nghiệm men cơ bắt buộc cần làm là {{c1::Creatine Kinase (CK)}}; nếu CK tăng {{c1::> 4 - 5 lần}} giới hạn trên bình thường (kèm triệu chứng nặng) thì cần tạm ngừng Statin để đánh giá.",
        "extra": "Hội chứng đau cơ do Statin (SAMS) chiếm khoảng 5 - 10% trên thực tế."
    },
    {
        "id": "IM20A_107",
        "type": "cloze",
        "text": "Hiện tượng <b>'Đau thắt ngực phục hồi' (Rebound Angina)</b> có thể xảy ra khi bệnh nhân ngừng đột ngột thuốc {{c1::Chẹn Beta giao cảm}} do hiện tượng tăng nhạy cảm thụ thể beta (Up-regulation); do đó khi muốn ngừng thuốc bắt buộc phải {{c1::Giảm liều từ từ trong 1 - 2 tuần}}.",
        "extra": "Ngừng đột ngột có thể khởi phát nhồi máu cơ tim cấp."
    },
    {
        "id": "IM20A_108",
        "type": "cloze",
        "text": "Phương pháp chụp mạch vành qua da (CAG) chỉ quan sát được hình ảnh 2D của {{c1::Lòng mạch (Luminogram)}}, hoàn toàn không nhìn thấy được thành mạch máu; để đánh giá chính xác bề dày và tính chất mảng xơ vữa cần phối hợp thêm {{c1::Siêu âm nội mạch (IVUS)}} hoặc {{c1::Cắt lớp quang học (OCT)}}.",
        "extra": "IVUS và OCT là hai công cụ chẩn đoán hình ảnh nội mạch tối tân."
    },
    {
        "id": "IM20A_109",
        "type": "cloze",
        "text": "Trong thử nghiệm lâm sàng <b>REVIVED-BCIS2 (NEJM 2022)</b> ở bệnh nhân suy tim nặng do thiếu máu cục bộ (LVEF ≤ 35%) có cơ tim còn sống, can thiệp đặt Stent (PCI) phối hợp OMT {{c1::KHÔNG làm giảm}} tỷ lệ tử vong do mọi nguyên nhân hoặc nhập viện vì suy tim so với OMT đơn thuần sau 3.4 năm.",
        "extra": "Nhấn mạnh vai trò trọng yếu của điều trị nội khoa suy tim tối ưu (Tứ trụ GDMT)."
    },
    {
        "id": "IM20A_110",
        "type": "cloze",
        "text": "Bệnh nhân có đau ngực ổn định được xếp vào nhóm có <b>Khả năng lâm sàng mắc CAD (Clinical Likelihood)</b> ở mức cao khi kết hợp giữa tuổi cao, nam giới, đau ngực điển hình kèm theo tiền sử mắc bệnh {{c1::Đái tháo đường}} và thói quen {{c1::Hút thuốc lá}}.",
        "extra": "Đây là nhóm đối tượng có xác suất tiền nghiệm vượt trội."
    }
]

out_json = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-20a_Benh_mach_vanh_man\outputs\IM-20a_Benh_mach_vanh_man_2026-08-19.cards.v2.json")
out_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Successfully generated and wrote {len(cards)} cards to {out_json.name}")
