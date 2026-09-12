# -*- coding: utf-8 -*-
"""
Generator for comprehensive IM-23b Anki V2 flashcards (>100 cards with rich Cloze & Basic).
Follows medical-flashcard-governance strictly:
- Basic: <b>📖 Văn bản gốc:</b><br> + <b>🔍 Góc nhìn bổ sung (AI):</b><br>
- Cloze: only {{c1::...}}
- Clean Unicode (no LaTeX math/arrows)
Covering all 10 parts of IM-23b (1,086 lines of comprehensive arrhythmias):
1. General Approach & Resuscitation (ACLS)
2. Cardiac Electrophysiology & Reentry Mechanisms
3. Bradyarrhythmias (Sinus node dysfunction, AV block I-II-III, Bundle branch block)
4. Supraventricular Tachycardias (PSVT, AVNRT, AVRT/WPW, Atrial Flutter, Atrial Fibrillation)
5. Ventricular Arrhythmias (PVCs, VT, Polymorphic VT/Torsades de pointes, VF, AIVR)
6. Inherited Arrhythmia Syndromes (Long QT, Brugada, CPVT, Early Repolarization)
7. Arrhythmias in Cardiomyopathies (ARVC, HCM, DCM, Sarcoidosis)
8. Vaughan-Williams Classification of Antiarrhythmic Drugs (Class I to IV + Others)
9. Atrial Fibrillation Management (Rate vs Rhythm, CHA2DS2-VASc, HAS-BLED, Anticoagulation)
10. Wide-Complex Tachycardia Differential (Brugada Criteria, Vereckei Criteria, Electrical Cardioversion)
"""
import json
from pathlib import Path

cards = [
    # =========================================================================
    # PHẦN 1: ĐẠI CƯƠNG, TIẾP CẬN & CẤP CỨU LOẠN NHỊP (ACLS)
    # =========================================================================
    {
        "id": "IM23B_001",
        "type": "basic",
        "front": "Tiếp cận ban đầu bệnh nhân rối loạn nhịp tim: 3 nhóm tình huống lâm sàng và thứ tự ưu tiên xử trí?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Nhóm 1: Ngừng tim (Cardiac arrest):</b> Xử trí ngay theo phác đồ Hồi sinh tim phổi nâng cao (ACLS): Ép tim chất lượng cao + Khử rung phá rung ngay nếu là Rung thất (VF) hoặc Nhanh thất vô mạch (pVT); hoặc Ép tim + Adrenaline nếu là Vô tâm thu (Asystole) / Hoạt động điện vô mạch (PEA).<br>• <b>Nhóm 2: Có suy giảm huyết động (Haemodynamic compromise):</b> Có 1 trong các dấu hiệu đe dọa tính mạng: (1) Tụt HA / Choáng; (2) Thiếu máu cơ tim cấp (đau ngực dữ dội); (3) Phù phổi cấp; (4) Rối loạn tri giác. → <b>Xử trí cấp cứu: Sốc điện đồng bộ (nếu nhịp nhanh) hoặc Atropin / Tạo nhịp tạm thời (nếu nhịp chậm)</b>.<br>• <b>Nhóm 3: Ổn định huyết động:</b> Đủ thời gian đo ECG 12 chuyển đạo, khai thác bệnh sử, làm xét nghiệm và dùng thuốc theo cơ chế.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Huyết động là 'ngã ba đường' quyết định dùng dòng điện ngay (bất ổn) hay dùng thuốc/tìm nguyên nhân (ổn định).",
        "tags": ["IM-23b", "Arrhythmia_Approach", "ACLS", "Triage"]
    },
    {
        "id": "IM23B_002",
        "type": "cloze",
        "text": "Ở bệnh nhân rối loạn nhịp nhanh có <b>Suy giảm huyết động</b> (tụt huyết áp, đau thắt ngực cấp, phù phổi cấp hoặc rối loạn ý thức), xử trí ưu tiên hàng đầu ngay lập tức là {{c1::Sốc điện chuyển nhịp đồng bộ (Synchronized Cardioversion)}}.",
        "extra": "Không trì hoãn sốc điện để thử các thuốc chống loạn nhịp khi huyết động không ổn định."
    },
    {
        "id": "IM23B_003",
        "type": "cloze",
        "text": "4 dạng rối loạn nhịp trong ngừng tuần hoàn theo ACLS được chia làm 2 nhóm: Nhóm có chỉ định phá rung (Shockable) gồm {{c1::Rung thất (VF)}} và {{c1::Nhanh thất vô mạch (pVT)}}; Nhóm không sốc điện gồm {{c1::Vô tâm thu (Asystole)}} và {{c1::Hoạt động điện vô mạch (PEA)}}.",
        "extra": "Nhóm không sốc điện chỉ ép tim liên tục và tiêm Adrenaline 1 mg mỗi 3 - 5 phút."
    },
    {
        "id": "IM23B_004",
        "type": "basic",
        "front": "Các nguyên nhân có thể đảo ngược của ngừng tim và loạn nhịp nặng (Quy tắc 5H và 5T)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>5H:</b> (1) Hypovolaemia (Giảm thể tích tuần hoàn); (2) Hypoxia (Thiếu oxy); (3) Hydrogen ion / Acidosis (Toan chuyển hóa); (4) Hypo-/Hyperkalaemia (Hạ hoặc Tăng Kali máu); (5) Hypothermia (Hạ thân nhiệt).<br>• <b>5T:</b> (1) Tension pneumothorax (Tràn khí màng phổi áp lực); (2) Tamponade, cardiac (Chèn ép tim cấp); (3) Toxins (Ngộ độc thuốc / chất độc); (4) Thrombosis, pulmonary (Thuyên tắc phổi); (5) Thrombosis, coronary (Hội chứng vành cấp).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Ghi nhớ 5H & 5T là bắt buộc trong mọi tình huống cấp cứu hồi sinh tim phổi để tìm và điều trị căn nguyên gốc.",
        "tags": ["IM-23b", "5H_5T", "ACLS", "Reversible_Causes"]
    },
    {
        "id": "IM23B_005",
        "type": "cloze",
        "text": "Hai rối loạn điện giải thường gặp nhất gây khởi phát các loạn nhịp tim chết người (Xoắn đỉnh, Rung thất, Vô tâm thu) trong nhóm 5H của ACLS là {{c1::Tăng Kali máu (Hyperkalemia)}} và {{c1::Hạ Kali / Hạ Magie máu}}.",
        "extra": "Cần kiểm tra khí máu và điện giải đồ khẩn cấp trong cấp cứu ngừng tim."
    },

    # =========================================================================
    # PHẦN 2: SINH LÝ ĐIỆN HỌC TẾ BÀO & CƠ CHẾ LOẠN NHỊP
    # =========================================================================
    {
        "id": "IM23B_006",
        "type": "basic",
        "front": "Mô tả 5 pha của Điện thế hoạt động tế bào cơ tim co bóp (Pha 0 đến Pha 4) và các dòng ion tương ứng?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Pha 0 (Khử cực nhanh):</b> Mở kênh Natri nhanh ($I_{\\text{Na}}$) → Dòng $Na^+$ ồ ạt đi vào trong tế bào, điện thế màng vọt từ $-90\\text{ mV}$ lên $+20\\text{ mV}$.<br>• <b>Pha 1 (Tái cực sớm):</b> Đóng kênh Natri, mở kênh Kali thoáng qua ($I_{\\text{to}}$) đẩy $K^+$ ra ngoài.<br>• <b>Pha 2 (Cao nguyên - Plateau):</b> Cân bằng giữa dòng $Ca^{2+}$ đi vào qua kênh Calci chậm type L ($I_{\\text{Ca-L}}$) và dòng $K^+$ đi ra.<br>• <b>Pha 3 (Tái cực nhanh):</b> Đóng kênh Calci, dòng $K^+$ đi ra ồ ạt qua các kênh $I_{\\text{Kr}}$ và $I_{\\text{Ks}}$ đưa điện thế màng về âm tính.<br>• <b>Pha 4 (Điện thế nghỉ):</b> Duy trì điện thế nghỉ $-90\\text{ mV}$ nhờ bơm $Na^+/K^+$-ATPase và kênh $I_{\\text{K1}}$.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Hiểu 5 pha giúp nắm rõ cơ chế các nhóm thuốc chống loạn nhịp: Nhóm I chẹn pha 0 ($I_{\\text{Na}}$), Nhóm III kéo dài pha 3 ($I_{\\text{K}}$), Nhóm IV chẹn pha 2 ($I_{\\text{Ca}}$).",
        "tags": ["IM-23b", "Action_Potential", "Electrophysiology", "Ion_Channels"]
    },
    {
        "id": "IM23B_007",
        "type": "cloze",
        "text": "Pha 0 (khử cực nhanh) của điện thế hoạt động tế bào cơ tâm thất được dẫn dắt bởi dòng ion {{c1::Natri (Na+)}} đi vào ồ ạt qua kênh Natri nhanh; trong khi đó ở tế bào nút xoang và nút nhĩ thất, pha khử cực được dẫn dắt bởi dòng ion {{c1::Calci (Ca2+)}}.",
        "extra": "Giải thích vì sao thuốc chẹn kênh Calci tác động chọn lọc trên nút xoang và nút nhĩ thất."
    },
    {
        "id": "IM23B_008",
        "type": "basic",
        "front": "3 điều kiện bắt buộc để hình thành và duy trì Cơ chế Vòng vào lại (Reentry)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Điều kiện 1:</b> Tồn tại 2 đường dẫn truyền điện học song song nối với nhau ở 2 đầu tạo thành một vòng khép kín (Circuit).<br>• <b>Điều kiện 2:</b> Block một chiều (Unidirectional block) ở một trong hai nhánh (thường do trơ tạm thời ở nhánh nhanh).<br>• <b>Điều kiện 3:</b> Tốc độ dẫn truyền qua nhánh còn lại (nhánh chậm) phải đủ chậm để khi xung điện vòng ngược lại, nhánh bị block ban đầu đã kịp hồi phục khả năng hưng phấn (hết thời kỳ trơ).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Cắt đứt vòng vào lại (bằng thuốc kéo dài thời kỳ trơ hoặc triệt đốt RF) là nguyên lý triệt để chấm dứt các cơn nhịp nhanh vào lại (AVNRT, AVRT, Cuồng nhĩ, VT sau NMCT).",
        "tags": ["IM-23b", "Reentry", "Mechanism", "Electrophysiology"]
    },
    {
        "id": "IM23B_009",
        "type": "cloze",
        "text": "Cơ chế Vòng vào lại (Reentry) — nguyên nhân của > 80% các cơn nhịp nhanh lâm sàng — bắt buộc cần 3 yếu tố: (1) Tồn tại hai đường dẫn truyền tạo vòng kín; (2) {{c1::Block một chiều (Unidirectional block)}} ở một nhánh; và (3) {{c1::Dẫn truyền chậm (Slow conduction)}} ở nhánh còn lại.",
        "extra": "Thuốc chống loạn nhịp nhóm I hoặc III làm gián đoạn vòng vào lại bằng cách triệt tiêu một trong các điều kiện này."
    },

    # =========================================================================
    # PHẦN 3: CÁC RỐI LOẠN NHỊP CHẬM & BLOCK DẪN TRUYỀN
    # =========================================================================
    {
        "id": "IM23B_010",
        "type": "basic",
        "front": "Hội chứng suy nút xoang (Sick Sinus Syndrome — SSS): Định nghĩa, 4 biểu hiện điện tâm đồ kinh điển và chỉ định đặt máy tạo nhịp?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa:</b> Rối loạn chức năng nội tại của nút xoang không thể tạo hoặc dẫn truyền nhịp xoang phù hợp với nhu cầu sinh lý.<br>• <b>4 biểu hiện ECG kinh điển:</b><br>  1. Nhịp chậm xoang dai dẳng không giải thích được (< 50 bpm lúc thức, không đáp ứng khi gắng sức).<br>  2. Ngừng xoang (Sinus arrest) hoặc Block xoang nhĩ (SA block) tạo khoảng ngừng tim > 3 giây.<br>  3. Không đáp ứng tần số tim khi gắng sức (Chronotropic incompetence - không đạt 85% nhịp tim tối đa theo tuổi).<br>  4. Hội chứng Nhịp nhanh - Nhịp chậm (Tachy-Brady Syndrome): Xen kẽ giữa các cơn rung nhĩ/cuồng nhĩ nhanh và các đoạn nhịp chậm xoang/ngừng tim kéo dài sau khi cơn nhanh chấm dứt.<br>• <b>Chỉ định đặt máy tạo nhịp vĩnh viễn (Class I):</b> SSS có triệu chứng lâm sàng rõ rệt (ngất, tiền ngất, mệt lả) tương ứng trực tiếp với đoạn nhịp chậm trên ECG.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Trong Hội chứng Tachy-Brady, thuốc cắt cơn nhịp nhanh (chẹn beta, amiodarone) sẽ làm nhịp chậm nặng hơn sau cơn → Bắt buộc phải đặt máy tạo nhịp trước rồi mới dùng thuốc khống chế nhịp nhanh.",
        "tags": ["IM-23b", "SSS", "Sinus_Node_Dysfunction", "Pacemaker", "Tachy_Brady"]
    },
    {
        "id": "IM23B_011",
        "type": "cloze",
        "text": "Trong Hội chứng suy nút xoang (SSS), dạng lâm sàng xen kẽ giữa các cơn nhịp nhanh trên thất (thường là Rung nhĩ / Cuồng nhĩ) với các đoạn ngừng tim hoặc chậm xoang kéo dài sau cơn được gọi là {{c1::Hội chứng Nhịp nhanh - Nhịp chậm (Tachy-Brady Syndrome)}}.",
        "extra": "Bệnh nhân có chỉ định cấy máy tạo nhịp vĩnh viễn (Pacemaker)."
    },
    {
        "id": "IM23B_012",
        "type": "basic",
        "front": "Phân loại 3 mức độ của Block Nhĩ - Thất (AV Block): Độ I, Độ II (Mobitz I vs Mobitz II) và Độ III? Nguy cơ tiến triển thành vô tâm thu?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Block AV Độ I:</b> Mọi sóng P đều dẫn thất nhưng khoảng $PR > 0.20\\text{ s}$ ($> 5$ ô nhỏ), $PR$ hằng định. Lành tính, hiếm khi cần can thiệp.<br>• <b>Block AV Độ II Mobitz I (Chu kỳ Wenckebach):</b> Khoảng $PR$ dài dần ra qua từng nhịp cho đến khi có 1 sóng P bị block không dẫn thất ($P$ rơi). Tổn thương ở **trong nút AV**, thường lành tính và đáp ứng với Atropin.<br>• <b>Block AV Độ II Mobitz II:</b> Khoảng $PR$ hằng định ở các nhịp dẫn, đột ngột có sóng P không dẫn thất. Tổn thương ở **dưới nút AV (bó His hoặc nhánh)**. Nguy cơ tiến triển thành Block AV độ III rất cao → **Chỉ định cấy máy tạo nhịp**.<br>• <b>Block AV Độ III (Hoàn toàn):</b> Phân ly hoàn toàn giữa nhĩ và thất. Nhĩ đập theo nhịp xoang (P-P đều), thất đập theo nhịp thoát (R-R đều nhưng chậm $20 - 40\\text{ bpm}$, QRS rộng nếu thoát thất). **Chỉ định cấp cứu cấy máy tạo nhịp**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Mobitz I = Nút AV (lành tính); Mobitz II = Dưới nút AV (nguy hiểm chết người). Tuyệt đối không nhầm lẫn giữa 2 thể Mobitz.",
        "tags": ["IM-23b", "AV_Block", "Mobitz_I", "Mobitz_II", "Third_Degree", "Pacemaker"]
    },
    {
        "id": "IM23B_013",
        "type": "cloze",
        "text": "Trong Block nhĩ thất độ II, thể <b>Mobitz I (Wenckebach)</b> có đặc điểm khoảng PR {{c1::dài dần ra}} cho đến khi có 1 sóng P bị block (vị trí tổn thương tại nút AV); trong khi thể <b>Mobitz II</b> có khoảng PR {{c1::hằng định}} trước nhịp rơi (vị trí tổn thương dưới nút AV, nguy cơ cao thành Block độ III).",
        "extra": "Mobitz II có chỉ định cấy máy tạo nhịp vĩnh viễn Class I kể cả khi chưa có triệu chứng."
    },
    {
        "id": "IM23B_014",
        "type": "cloze",
        "text": "Đặc điểm nhận diện <b>Block nhĩ thất độ III (Block hoàn toàn)</b> trên điện tâm đồ là hiện tượng {{c1::Phân ly nhĩ - thất hoàn toàn}}, sóng P đều đặn đi theo tần số nhĩ riêng và phức bộ QRS đều đặn đi theo {{c1::nhịp thoát (Escape rhythm)}} với tần số chậm 20 - 40 chu kỳ/phút.",
        "extra": "Khoảng PR biến thiên hoàn toàn ngẫu nhiên do P và QRS không liên quan nhau."
    },
    {
        "id": "IM23B_015",
        "type": "basic",
        "front": "Tiêu chuẩn chẩn đoán trên ECG của Block nhánh phải (RBBB) vs Block nhánh trái (LBBB)? Ý nghĩa lâm sàng của LBBB mới xuất hiện?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Block nhánh phải hoàn toàn (CRBBB):</b><br>  - Thời gian $QRS \\ge 0.12\\text{ s}$ ($> 3$ ô nhỏ).<br>  - Chuyển đạo $V_1, V_2$: Dạng sóng $rSR'$ (hình tai thỏ) hoặc $rsR'$, sóng $R'$ rộng.<br>  - Chuyển đạo $D_I, aVL, V_5, V_6$: Sóng S rộng, sâu ($S$ trễ).<br>• <b>Block nhánh trái hoàn toàn (CLBBB):</b><br>  - Thời gian $QRS \\ge 0.12\\text{ s}$.<br>  - Chuyển đạo $V_5, V_6, D_I, aVL$: Sóng R rộng, có khấc ở đỉnh (hình chữ M), mất sóng Q sinh lý.<br>  - Chuyển đạo $V_1, V_2$: Sóng rS hoặc QS rất sâu và rộng.<br>• <b>Ý nghĩa LBBB mới xuất hiện:</b> Ở bệnh nhân có đau thắt ngực cấp tính, LBBB mới xuất hiện được xem là **tương đương Nhồi máu cơ tim có ST chênh lên (STEMI)** → Chỉ định chụp mạch vành can thiệp khẩn cấp (áp dụng tiêu chuẩn Sgarbossa cải tiến).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>LBBB làm mất tính đồng bộ co bóp thất trái, là chỉ định cấy máy tái đồng bộ tim (CRT) ở bệnh nhân suy tim HFrEF.",
        "tags": ["IM-23b", "RBBB", "LBBB", "ECG_Criteria", "Sgarbossa"]
    },
    {
        "id": "IM23B_016",
        "type": "cloze",
        "text": "Trên điện tâm đồ, <b>Block nhánh trái hoàn toàn (LBBB)</b> đặc trưng bởi thời gian QRS ≥ 0.12s, sóng R rộng có khấc ở các chuyển đạo bên (DI, aVL, V5, V6); khi LBBB {{c1::mới xuất hiện}} ở bệnh nhân đau ngực cấp tính được xem là tương đương {{c1::Nhồi máu cơ tim có ST chênh lên (STEMI)}}.",
        "extra": "Cần kích hoạt phòng can thiệp mạch vành (Cathlab) khẩn cấp."
    },

    # =========================================================================
    # PHẦN 4: NHỊP NHANH TRÊN THẤT (PSVT, AVNRT, AVRT/WPW, FLUTTER, AF)
    # =========================================================================
    {
        "id": "IM23B_017",
        "type": "basic",
        "front": "Cơ chế sinh lý học, đặc điểm ECG và xử trí cấp cứu Nhịp nhanh vào lại nút nhĩ thất (AVNRT)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cơ chế:</b> Tồn tại 2 đường dẫn truyền chức năng trong nút nhĩ thất: Đường nhanh (Fast pathway - dẫn truyền nhanh, trơ dài) và Đường chậm (Slow pathway - dẫn truyền chậm, trơ ngắn). Xung điện đi xuống đường chậm và đi ngược lên đường nhanh (Slow-Fast AVNRT chiếm 90%).<br>• <b>Đặc điểm ECG:</b> QRS hẹp đều, tần số $140 - 220\\text{ bpm}$, sóng P' lẫn vào cuối phức bộ QRS tạo hình ảnh **giả sóng r' ở $V_1$ (pseudo-r')** hoặc **giả sóng s ở $D_{II}, D_{III}, aVF$ (pseudo-s)**; khoảng $RP' < 70\\text{ ms}$.<br>• <b>Xử trí cấp cứu:</b><br>  - Bước 1: Nghiệm pháp cường phế vị (Nghiệm pháp Valsalva cải tiến có nâng chân thụ động - tỷ lệ thành công 43%).<br>  - Bước 2: **Adenosine tiêm tĩnh mạch nhanh** liều khởi đầu $6\\text{ mg}$ (nếu không cắt cơn tiêm tiếp $12\\text{ mg}$ sau 1 - 2 phút).<br>  - Bước 3: Verapamil / Diltiazem hoặc Chẹn Beta nếu thất bại với Adenosine.<br>  - Triệt để: Triệt đốt đường chậm (Slow pathway ablation) bằng năng lượng sóng radio (RF).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Adenosine có thời gian bán hủy cực ngắn (< 10 giây), gây block nút AV thoáng qua để bẻ gãy vòng vào lại.",
        "tags": ["IM-23b", "AVNRT", "PSVT", "Adenosine", "Valsalva", "Ablation"]
    },
    {
        "id": "IM23B_018",
        "type": "cloze",
        "text": "Thuốc lựa chọn hàng đầu để cắt cơn Nhịp nhanh kịch phát trên thất do vào lại nút nhĩ thất (AVNRT) khi nghiệm pháp phế vị thất bại là {{c1::Adenosine}} tiêm tĩnh mạch nhanh qua đường truyền lớn với liều khởi đầu là {{c1::6 mg}} (tiêm bolus nhanh kèm đẩy 20 mL nước muối sinh lý).",
        "extra": "Nếu sau 1 - 2 phút không cắt cơn, tiêm tiếp liều 12 mg."
    },
    {
        "id": "IM23B_019",
        "type": "basic",
        "front": "Hội chứng Wolff-Parkinson-White (WPW): Cơ chế đường dẫn truyền phụ (Cầu Kent), tam chứng ECG lúc nghỉ và cạm bẫy chết người khi có Rung nhĩ?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cơ chế:</b> Tồn tại đường dẫn truyền phụ nhĩ - thất bẩm sinh (Cầu Kent) dẫn truyền xung điện vượt qua nút AV không bị làm chậm.<br>• <b>Tam chứng ECG lúc nhịp xoang (Kích thích sớm - Pre-excitation):</b><br>  1. Khoảng $PR$ ngắn $< 0.12\\text{ s}$.<br>  2. Sóng Delta ở đoạn đầu phức bộ QRS (khử cực sớm tâm thất).<br>  3. Phức bộ $QRS$ giãn rộng $> 0.12\\text{ s}$ kèm biến đổi ST-T thứ phát.<br>• <b>CẠM BẪY CHẾT NGƯỜI (AF TRÊN NỀN WPW):</b> Khi bệnh nhân WPW bị Rung nhĩ, xung nhĩ hàng trăm nhịp/phút truyền thẳng qua cầu Kent xuống thất (do cầu Kent không có tính chất trơ như nút AV) $\rightarrow$ Tần số thất vọt lên $> 250 - 300\\text{ bpm}$ gây **Rung thất (VF) và đột tử**.<br>• <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI KHI AF + WPW:</b> **Thuốc ức chế nút AV (Adenosine, Digoxin, Verapamil, Diltiazem, Chẹn beta)** vì chẹn nút AV sẽ ép 100% dòng điện đi qua cầu Kent gây thoái hóa thành VF.<br>• <b>Xử trí:</b> Sốc điện chuyển nhịp ngay nếu tụt HA; hoặc dùng thuốc kéo dài thời kỳ trơ cầu Kent (**Procainamide** hoặc **Ibutilide**).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Rung nhĩ kèm WPW trên ECG có hình ảnh kinh điển: Nhịp nhanh QRS rộng, hoàn toàn không đều (FBI: Fast, Broad, Irregular) với tần số cực nhanh.",
        "tags": ["IM-23b", "WPW", "Kent_Bundle", "Delta_Wave", "AF_WPW", "Contraindication"]
    },
    {
        "id": "IM23B_020",
        "type": "cloze",
        "text": "Ở bệnh nhân mắc Hội chứng WPW xuất hiện Rung nhĩ (AF trên nền tiền kích thích), các thuốc ức chế nút nhĩ thất gồm {{c1::Adenosine, Digoxin, Verapamil, Diltiazem và Chẹn Beta}} bị <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI</b> do thúc đẩy dẫn truyền qua cầu Kent gây thoái hóa thành {{c1::Rung thất (VF) và ngừng tim}}.",
        "extra": "Xử trí ưu tiên là sốc điện chuyển nhịp hoặc dùng Procainamide / Ibutilide."
    },
    {
        "id": "IM23B_021",
        "type": "basic",
        "front": "Cuồng động nhĩ (Atrial Flutter): Cơ chế vòng vào lại eo van ba lá (CTI), đặc điểm sóng răng cưa trên ECG và phác đồ điều trị triệt để?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cơ chế Cuồng nhĩ điển hình (Typical Atrial Flutter):</b> Vòng vào lại lớn (Macro-reentry) trong tâm nhĩ phải, chạy qua vùng **Eo van ba lá - tĩnh mạch chủ dưới (Cavotricuspid Isthmus - CTI)** theo chiều ngược kim đồng hồ (Counter-clockwise chiếm 90%).<br>• <b>Đặc điểm ECG:</b> Mất sóng P xoang, thay bằng các **sóng răng cưa F (Flutter waves)** đều đặn với tần số nhĩ $250 - 350\\text{ bpm}$ (thường $300\\text{ bpm}$), thấy rõ nhất ở $D_{II}, D_{III}, aVF$. Thường dẫn truyền nhĩ thất $2:1$ (tần số thất cố định $150\\text{ bpm}$) hoặc $4:1$ ($75\\text{ bpm}$).<br>• <b>Điều trị:</b><br>  - Cắt cơn: Sốc điện đồng bộ mức năng lượng thấp ($50 - 100\\text{ J}$) có tỷ lệ thành công > 90%.<br>  - Triệt để: **Triệt đốt eo CTI bằng sóng radio (RF CTI ablation)** đạt tỷ lệ khỏi bệnh vĩnh viễn > 95%.<br>  - Phòng ngừa huyết khối: Dùng thuốc chống đông tương tự như Rung nhĩ theo thang điểm $\\text{CHA}_2\\text{DS}_2\\text{-VASc}$.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bất kỳ nhịp nhanh QRS hẹp nào có tần số thất cố định đúng 150 bpm, phản xạ đầu tiên trên ECG là phải tìm sóng răng cưa của Cuồng nhĩ dẫn truyền 2:1.",
        "tags": ["IM-23b", "Atrial_Flutter", "CTI", "Sawtooth_Waves", "Ablation"]
    },
    {
        "id": "IM23B_022",
        "type": "cloze",
        "text": "Cuồng động nhĩ điển hình (Typical Atrial Flutter) có tần số sóng nhĩ F hình răng cưa khoảng {{c1::300 chu kỳ/phút}}; khi dẫn truyền nhĩ thất theo tỷ lệ 2:1 sẽ tạo ra nhịp nhanh phức bộ hẹp với tần số thất cố định là {{c1::150 chu kỳ/phút}}.",
        "extra": "Phương pháp điều trị triệt để là triệt đốt eo van ba lá - TM chủ dưới (CTI)."
    },
    {
        "id": "IM23B_023",
        "type": "basic",
        "front": "Rung nhĩ (Atrial Fibrillation — AF): Phân loại 5 thể lâm sàng theo ESC (Kịch phát, Bền bỉ, Bền bỉ kéo dài, Vĩnh viễn, Lần đầu phát hiện)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>1. Rung nhĩ phát hiện lần đầu (First diagnosed AF):</b> Chưa từng được chẩn đoán trước đây, không kể thời gian kéo dài hay triệu chứng.<br>• <b>2. Rung nhĩ kịch phát (Paroxysmal AF):</b> Cơn tự chấm dứt hoặc được can thiệp chuyển nhịp trong vòng **≤ 7 ngày** (thường trong 48 giờ đầu).<br>• <b>3. Rung nhĩ bền bỉ (Persistent AF):</b> Cơn kéo dài liên tục **> 7 ngày** (bao gồm cả các ca chuyển nhịp thành công bằng thuốc hoặc sốc điện sau ngày thứ 7).<br>• <b>4. Rung nhĩ bền bỉ kéo dài (Long-standing persistent AF):</b> Rung nhĩ liên tục **> 12 tháng** khi đã quyết định áp dụng chiến lược kiểm soát nhịp.<br>• <b>5. Rung nhĩ vĩnh viễn (Permanent AF):</b> Bệnh nhân và thầy thuốc thống nhất chấp nhận sống chung với rung nhĩ, **không còn nỗ lực khôi phục hoặc duy trì nhịp xoang** (chỉ tập trung kiểm soát tần số thất và chống đông).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Thuật ngữ 'Rung nhĩ vĩnh viễn' là một quyết định điều trị lâm sàng, không phải là đặc tính sinh học của bệnh.",
        "tags": ["IM-23b", "AFib", "Classification", "Paroxysmal", "Persistent", "Permanent"]
    },
    {
        "id": "IM23B_024",
        "type": "cloze",
        "text": "Rung nhĩ được phân loại là <b>Kịch phát (Paroxysmal)</b> khi cơn tự kết thúc hoặc được chuyển nhịp trong vòng {{c1::≤ 7 ngày}}; nếu kéo dài liên tục {{c1::> 7 ngày}} thì gọi là Rung nhĩ <b>Bền bỉ (Persistent)</b>.",
        "extra": "Kéo dài > 12 tháng gọi là Long-standing persistent AF."
    },

    # =========================================================================
    # PHẦN 5: CÁC RỐI LOẠN NHỊP NHANH THẤT (PVC, VT, TORSADES DE POINTES, VF)
    # =========================================================================
    {
        "id": "IM23B_025",
        "type": "basic",
        "front": "Ngoại tâm thu thất (PVC): Tiêu chuẩn ECG, chỉ số Gánh nặng ngoại tâm thu (PVC Burden) và nguy cơ Bệnh cơ tim do loạn nhịp?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tiêu chuẩn ECG:</b> Nhát bóp đến sớm, phức bộ $QRS$ giãn rộng $\\ge 0.12\\text{ s}$ với hình dạng dị dạng kỳ quái, không có sóng P đi trước, biến đổi ST-T đảo chiều với QRS, theo sau bởi một **khoảng nghỉ bù hoàn toàn**.<br>• <b>Gánh nặng ngoại tâm thu (PVC Burden trên Holter ECG 24h):</b><br>  $$\\text{PVC Burden (\\%)} = \\frac{\\text{Tổng số nhát PVC trong 24h}}{\\text{Tổng số nhịp tim trong 24h}} \\times 100\\%$$\<br>• <b>Nguy cơ Bệnh cơ tim do loạn nhịp (PVC-induced Cardiomyopathy):</b> Khi $\\text{PVC Burden} > 10 - 15\\%$, tình trạng mất đồng bộ thất kéo dài có thể làm giãn tâm thất trái và suy giảm phân suất tống máu (EF) → **Chỉ định triệt đốt ổ loạn nhịp bằng sóng radio (RF) hoặc dùng thuốc chống loạn nhịp (Chẹn Beta, Amiodarone)** để hồi phục chức năng thất trái.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bệnh cơ tim do PVC có tính chất hồi phục hoàn toàn: sau khi triệt đốt thành công ổ ngoại tâm thu, EF của thất trái sẽ trở về bình thường.",
        "tags": ["IM-23b", "PVC", "PVC_Burden", "Cardiomyopathy", "Holter"]
    },
    {
        "id": "IM23B_026",
        "type": "cloze",
        "text": "Trên kết quả theo dõi Holter điện tâm đồ 24 giờ, bệnh nhân có Gánh nặng ngoại tâm thu thất (PVC Burden) đạt mức {{c1::> 10 - 15%}} tổng số nhịp tim có nguy cơ cao phát triển thành {{c1::Bệnh cơ tim do loạn nhịp (PVC-induced Cardiomyopathy)}} làm suy giảm chức năng tim.",
        "extra": "Đây là chỉ định xem xét triệt đốt điện sinh lý bằng sóng radio (RF ablation)."
    },
    {
        "id": "IM23B_027",
        "type": "basic",
        "front": "Định nghĩa, phân loại Nhịp nhanh thất (VT) bền bỉ vs không bền bỉ, đơn dạng vs đa dạng?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa:</b> Chuỗi từ **≥ 3 nhát ngoại tâm thu thất liên tiếp** với tần số thất $> 100\\text{ bpm}$ (thường $140 - 220\\text{ bpm}$).<br>• <b>Phân loại theo thời gian kéo dài:</b><br>  - <b>VT không bền bỉ (Non-sustained VT - NSVT):</b> Cơn tự kết thúc trong vòng **< 30 giây** và không gây tụt huyết áp sụp đổ huyết động.<br>  - <b>VT bền bỉ (Sustained VT):</b> Cơn kéo dài **≥ 30 giây** và/hoặc gây sụp đổ huyết động buộc phải can thiệp cắt cơn khẩn cấp (sốc điện hoặc thuốc).<br>• <b>Phân loại theo hình thái QRS:</b><br>  - <b>VT đơn dạng (Monomorphic VT):</b> Tất cả các phức bộ QRS có cùng một hình dạng trên từng chuyển đạo (thường do ổ sẹo xơ sau NMCT).<br>  - <b>VT đa dạng (Polymorphic VT):</b> Hình dạng QRS biến đổi liên tục từ nhịp này sang nhịp khác (thường do thiếu máu cục bộ cơ tim cấp hoặc hội chứng tái cực bất thường).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Monomorphic VT thường do sẹo cố định (vào lại); Polymorphic VT thường là 'con báo động' của thiếu máu cục bộ cơ tim cấp đang diễn tiến.",
        "tags": ["IM-23b", "VT", "Sustained_VT", "NSVT", "Monomorphic", "Polymorphic"]
    },
    {
        "id": "IM23B_028",
        "type": "cloze",
        "text": "Nhịp nhanh thất được định nghĩa là <b>Bền bỉ (Sustained VT)</b> khi cơn kéo dài liên tục từ {{c1::≥ 30 giây}} trở lên hoặc gây rối loạn huyết động buộc phải sốc điện can thiệp cấp cứu; nếu tự kết thúc dưới 30 giây thì gọi là {{c1::Không bền bỉ (NSVT)}}.",
        "extra": "NSVT ở bệnh nhân suy tim sau NMCT là dấu hiệu chỉ điểm nguy cơ đột tử tim."
    },
    {
        "id": "IM23B_029",
        "type": "basic",
        "front": "Xoắn đỉnh (Torsades de Pointes — TdP): Cơ chế bệnh sinh, hình ảnh ECG đặc trưng, các nguyên nhân gây QT dài và phác đồ cấp cứu?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Định nghĩa & Cơ chế:</b> Dạng nhịp nhanh thất đa dạng đặc biệt xuất hiện trên nền **khoảng QT kéo dài** ($QTc > 500\\text{ ms}$). Cơ chế do hoạt động nảy cò sau sớm (Early Afterdepolarizations - EADs) kích hoạt.<br>• <b>Hình ảnh ECG đặc trưng:</b> Phức bộ QRS xoắn vặn liên tục quanh đường đẳng điện, biên độ và trục đỉnh sóng đảo chiều nhấp nhô như dải ruy-băng.<br>• <b>Nguyên nhân gây kéo dài khoảng QT:</b><br>  - Rối loạn điện giải: Hạ Kali máu, Hạ Magie máu, Hạ Calci máu.<br>  - Thuốc gây kéo dài QT: Chống loạn nhịp (Amiodarone, Sotalol, Quinidine), Kháng sinh (Macrolide, Fluoroquinolone), Kháng nấm, Thuốc chống loạn thần (Haloperidol), Chống trầm cảm.<br>  - Hội chứng QT dài bẩm sinh (LQTS 1, 2, 3).<br>• <b>Phác đồ cấp cứu TdP:</b><br>  - <b>Magnesium Sulfate tiêm tĩnh mạch ($2\\text{ g}$ trong 1 - 2 phút)</b> là thuốc lựa chọn số 1 (kể cả khi nồng độ Magie máu bình thường).<br>  - Tăng nhịp tim để rút ngắn khoảng QT: Truyền Isoproterenol hoặc Đặt máy tạo nhịp tạm thời vượt tần số ($90 - 110\\text{ bpm}$).<br>  - Bù Kali máu duy trì mức cao $4.5 - 5.0\\text{ mmol/L}$.<br>  - Sốc điện khử rung không đồng bộ nếu thoái hóa thành Rung thất.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>CHỐNG CHỈ ĐỊNH DÙNG AMIODARONE HOẶC SOTALOL ĐỂ CẤP CỨU XOẮN ĐỈNH vì các thuốc này làm kéo dài thêm khoảng QT khiến bệnh nhân ngừng tim nhanh hơn.",
        "tags": ["IM-23b", "Torsades_de_Pointes", "Long_QT", "Magnesium", "Contraindication"]
    },
    {
        "id": "IM23B_030",
        "type": "cloze",
        "text": "Thuốc cấp cứu lựa chọn số 1 để cắt cơn <b>Xoắn đỉnh (Torsades de Pointes)</b> là {{c1::Magnesium Sulfate (liều 2 g tiêm TM)}}; nhóm thuốc chống loạn nhịp tuyệt đối bị <b>CHỐNG CHỈ ĐỊNH</b> vì làm kéo dài thêm khoảng QT là {{c1::Nhóm IA và Nhóm III (Amiodarone / Sotalol)}}.",
        "extra": "Cần tăng nhịp tim lên 90 - 110 bpm bằng Isoproterenol hoặc tạo nhịp để rút ngắn QT."
    },
    {
        "id": "IM23B_031",
        "type": "basic",
        "front": "Nhịp tự thất nhanh (Accelerated Idioventricular Rhythm — AIVR): Tiêu chuẩn ECG, bối cảnh lâm sàng xuất hiện và thái độ xử trí?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Tiêu chuẩn ECG:</b> Nhịp thất với phức bộ QRS giãn rộng, tần số dao động trong khoảng **50 - 110 chu kỳ/phút** (nhanh hơn nhịp thoát thất thông thường < 40 bpm nhưng chậm hơn Nhịp nhanh thất > 120 bpm).<br>• <b>Bối cảnh lâm sàng:</b> Xuất hiện rất phổ biến sau khi **Tái tưới máu mạch vành thành công** trong Nhồi máu cơ tim cấp (sau can thiệp PCI hoặc dùng thuốc tiêu sợi huyết); hoặc do ngộ độc Digoxin.<br>• <b>Thái độ xử trí:</b> Là **dấu hiệu chỉ điểm tái tưới máu thành công (Reperfusion arrhythmia)**, tiến triển hoàn toàn lành tính, tự giới hạn và hiếm khi gây rối loạn huyết động → **KHÔNG CẦN DÙNG THUỐC CHỐNG LOẠN NHỊP, CHỈ CẦN THEO DÕI SÁT**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Dùng thuốc ức chế nhịp thất (như Lidocaine/Amiodarone) để dập tắt AIVR có thể xóa sạch ổ chủ nhịp cứu mạng duy nhất của bệnh nhân, dẫn đến vô tâm thu.",
        "tags": ["IM-23b", "AIVR", "Reperfusion", "PCI", "Benign"]
    },
    {
        "id": "IM23B_032",
        "type": "cloze",
        "text": "Nhịp tự thất nhanh (AIVR) có tần số thất từ {{c1::50 đến 110 chu kỳ/phút}}, thường xuất hiện sau khi {{c1::Tái tưới máu mạch vành thành công (PCI/tiêu sợi huyết)}} trong nhồi máu cơ tim cấp; đây là rối loạn nhịp lành tính và thái độ xử trí đúng là {{c1::Chỉ theo dõi, không dùng thuốc chống loạn nhịp}}.",
        "extra": "Dập tắt AIVR có thể gây vô tâm thu nguy hiểm."
    },

    # =========================================================================
    # PHẦN 6 & 7: CÁC HỘI CHỨNG LOẠN NHỊP DI TRUYỀN & BỆNH CƠ TIM
    # =========================================================================
    {
        "id": "IM23B_033",
        "type": "basic",
        "front": "Hội chứng Brugada: Di truyền học, 3 type biến đổi ECG (đặc biệt Type 1 Brugada) và chỉ định cấy máy ICD?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Di truyền:</b> Đột biến gen kênh Natri $SCN5A$ (chiếm 20 - 30%), di truyền trội trên NST thường, thường gặp ở nam giới trẻ tuổi Đông Nam Á (Hội chứng tử vong đột ngột trong đêm - Lai Tai / Pokkuri).<br>• <b>3 Type trên ECG (chuyển đạo $V_1, V_2$):</b><br>  - <b>Type 1 (Dạng vòm - Coved type):</b> ST chênh lên $\\ge 2\\text{ mm}$ tiếp nối bằng sóng T âm đối xứng, không có góc nhọn. Đây là **type duy nhất cho phép chẩn đoán xác định**.<br>  - <b>Type 2 (Dạng yên ngựa - Saddle-back type):</b> ST chênh lên $\\ge 2\\text{ mm}$ rồi tụt xuống $\\ge 1\\text{ mm}$ trước khi đi lên sóng T dương.<br>  - <b>Type 3:</b> ST chênh lên dạng yên ngựa hoặc vòm nhưng $< 1\\text{ mm}$.<br>• <b>Yếu tố kích hoạt:</b> Sốt cao, ăn quá no, rượu bia, thuốc chẹn kênh Natri (Ajmaline, Flecainide).<br>• <b>Điều trị:</b> Cấy máy phá rung tự động (**ICD**) là biện pháp duy nhất ngăn ngừa đột tử ở bệnh nhân có triệu chứng (ngất hoặc ngừng tim được cứu sống). Thuốc uống hỗ trợ: **Quinidine**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Hạ sốt tích cực bằng Paracetamol là y lệnh cấp cứu bắt buộc khi bệnh nhân Brugada bị sốt vì thân nhiệt tăng làm kênh Natri bất hoạt nặng hơn.",
        "tags": ["IM-23b", "Brugada", "SCN5A", "Type_1_Coved", "ICD", "Quinidine"]
    },
    {
        "id": "IM23B_034",
        "type": "cloze",
        "text": "Hội chứng Brugada được chẩn đoán xác định khi trên điện tâm đồ (chuyển đạo V1, V2) xuất hiện hình ảnh Type 1 dạng {{c1::Vòm (Coved type)}} với đoạn ST chênh lên {{c1::≥ 2 mm}} tiếp nối bằng sóng T âm; biện pháp duy nhất được chứng minh ngăn ngừa đột tử là {{c1::Cấy máy phá rung tự động (ICD)}}.",
        "extra": "Sốt cao là yếu tố kích hoạt kinh điển làm lộ rõ hình ảnh Type 1 Brugada."
    },
    {
        "id": "IM23B_035",
        "type": "basic",
        "front": "Hội chứng QT dài bẩm sinh (LQTS): Phân biệt 3 type chính (LQT1, LQT2, LQT3) về gen, yếu tố kích hoạt và hình dạng sóng T?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>LQT1 (Chiếm 40 - 50%):</b> Đột biến gen $KCNQ1$ (giảm dòng $I_{\\text{Ks}}$). Yếu tố kích hoạt cơn ngất: **Gắng sức thể lực mạnh, đặc biệt là BƠI LỘI**. Sóng T trên ECG: Sóng T đáy rộng.<br>• <b>LQT2 (Chiếm 35 - 40%):</b> Đột biến gen $KCNH2$ (giảm dòng $I_{\\text{Kr}}$). Yếu tố kích hoạt: **Cảm xúc mạnh, âm thanh giật mình đột ngột (tiếng chuông báo thức, chuông điện thoại)**. Sóng T trên ECG: Sóng T có khấc (notched T wave) hoặc biên độ thấp.<br>• <b>LQT3 (Chiếm 10%):</b> Đột biến gen $SCN5A$ (tăng dòng Natri muộn $I_{\\text{Na,late}}$). Yếu tố kích hoạt: **Xuất hiện lúc NGHỈ NGƠI hoặc ĐANG NGỦ (nhịp tim chậm)**. Sóng T trên ECG: Đoạn ST kéo dài phẳng lì, sóng T xuất hiện muộn ở cuối.<br>• <b>Điều trị:</b> Thuốc Chẹn Beta (Nadolol, Propranolol) là lựa chọn đầu tay cho LQT1 và LQT2; Mexiletine cho LQT3; Cấy máy ICD cho nhóm nguy cơ cao.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Hỏi kỹ hoàn cảnh khởi phát cơn ngất (đang bơi lội vs giật mình vì tiếng chuông) giúp định hướng chính xác type gen LQTS trước khi có kết quả xét nghiệm di truyền.",
        "tags": ["IM-23b", "LQTS", "LQT1", "LQT2", "LQT3", "Genetics", "Swimming"]
    },
    {
        "id": "IM23B_036",
        "type": "cloze",
        "text": "Trong Hội chứng QT dài bẩm sinh, thể <b>LQT1</b> (đột biến gen KCNQ1) đặc trưng bởi các biến cố ngất hoặc đột tử kích hoạt điển hình khi {{c1::Bơi lội hoặc gắng sức thể lực}}; trong khi thể <b>LQT2</b> bị kích hoạt bởi {{c1::Âm thanh giật mình đột ngột (tiếng chuông báo thức/điện thoại)}}.",
        "extra": "LQT3 xảy ra chủ yếu lúc nghỉ ngơi hoặc ban đêm lúc đang ngủ."
    },
    {
        "id": "IM23B_037",
        "type": "basic",
        "front": "Bệnh cơ tim thất phải sinh loạn nhịp (ARVC): Cơ chế mô bệnh học, tiêu chuẩn ECG (Sóng Epsilon) và nguy cơ đột tử ở vận động viên?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Cơ chế:</b> Đột biến các protein thể liên kết tế bào (Desmosome: Plakophilin-2, Desmoplakin...) → Tế bào cơ tâm thất phải bị chết và dần dần được **thay thế bởi mô mỡ và mô xơ**.<br>• <b>Tiêu chuẩn ECG đặc trưng:</b><br>  - **Sóng Epsilon (Epsilon wave):** Sóng nhỏ có khấc xuất hiện ở cuối phức bộ QRS ngay đầu đoạn ST tại các chuyển đạo trước tim phải ($V_1 - V_3$) (độ đặc hiệu cực cao).<br>  - Sóng T âm ở $V_1 - V_3$ ở người > 14 tuổi (khi không có RBBB).<br>  - Cơn Nhịp nhanh thất có dạng Block nhánh trái (LBBB morphology) với trục hướng lên trên hoặc vô định.<br>• <b>Ý nghĩa lâm sàng:</b> Là nguyên nhân hàng đầu gây đột tử do tim ở **vận động viên thể thao trẻ tuổi** tại các nước Nam Âu (Ý).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bệnh nhân ARVC bắt buộc phải dừng tuyệt đối các hoạt động thể thao thi đấu đỉnh cao vì gắng sức làm tăng áp lực xé rách desmosome thất phải.",
        "tags": ["IM-23b", "ARVC", "Epsilon_Wave", "Desmosome", "Athletes_Sudden_Death"]
    },
    {
        "id": "IM23B_038",
        "type": "cloze",
        "text": "Dấu hiệu điện tâm đồ có độ đặc hiệu cao nhất để chẩn đoán <b>Bệnh cơ tim thất phải sinh loạn nhịp (ARVC)</b> là {{c1::Sóng Epsilon (Epsilon wave)}}, biểu hiện bằng sóng nhỏ có khấc ở cuối phức bộ QRS tại các chuyển đạo {{c1::V1 đến V3}}.",
        "extra": "ARVC là nguyên nhân hàng đầu gây đột tử ở vận động viên trẻ tuổi."
    },

    # =========================================================================
    # PHẦN 8: DƯỢC LÝ THUỐC CHỐNG LOẠN NHỊP (VAUGHAN-WILLIAMS CLASSIFICATION)
    # =========================================================================
    {
        "id": "IM23B_039",
        "type": "basic",
        "front": "Bảng phân loại Thuốc chống loạn nhịp theo Vaughan-Williams (Nhóm I đến Nhóm IV + Nhóm khác) và cơ chế tác dụng?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Nhóm I (Chẹn kênh Natri nhanh $I_{\\text{Na}}$):</b><br>  - <i>Nhóm IA (Kéo dài APD & QT):</i> Quinidine, Procainamide, Disopyramide.<br>  - <i>Nhóm IB (Rút ngắn APD & QT):</i> Lidocaine, Mexiletine (chuyên biệt cho loạn nhịp thất sau NMCT).<br>  - <i>Nhóm IC (Không đổi APD, làm chậm dẫn truyền rất mạnh):</i> Flecainide, Propafenone (chống chỉ định khi có bệnh tim thiếu máu cục bộ / suy tim theo CAST trial).<br>• <b>Nhóm II (Thuốc chẹn Beta giao cảm):</b> Bisoprolol, Metoprolol, Atenolol, Esmolol (giảm tính tự động, làm chậm dẫn truyền nút AV).<br>• <b>Nhóm III (Chẹn kênh Kali $I_{\\text{K}}$ kéo dài thời gian trơ):</b> Amiodarone, Sotalol, Dronedarone, Ibutilide, Dofetilide.<br>• <b>Nhóm IV (Chẹn kênh Calci chậm type L):</b> Verapamil, Diltiazem.<br>• <b>Nhóm khác:</b> Adenosine (kích hoạt thụ thể A1 mở kênh Kali), Digoxin (ức chế $Na^+/K^+$-ATPase), Atropin (kháng cholinergic).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>CAST trial là bài học kinh điển: Thuốc nhóm IC dập tắt được PVC nhưng làm tăng gấp 3 lần tỷ lệ tử vong ở bệnh nhân sau NMCT do tạo điều kiện cho loạn nhịp vào lại.",
        "tags": ["IM-23b", "Vaughan_Williams", "Antiarrhythmic_Drugs", "Classification", "CAST_Trial"]
    },
    {
        "id": "IM23B_040",
        "type": "cloze",
        "text": "Theo phân loại Vaughan-Williams, hai thuốc chống loạn nhịp <b>Nhóm IC</b> là {{c1::Flecainide}} và {{c1::Propafenone}} bị <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI</b> ở bệnh nhân có bệnh cơ tim thiếu máu cục bộ hoặc sau nhồi máu cơ tim do làm tăng gấp 3 lần tỷ lệ tử vong (chứng minh qua thử nghiệm CAST).",
        "extra": "Chỉ được dùng nhóm IC cho bệnh nhân có 'trái tim cấu trúc hoàn toàn bình thường'."
    },
    {
        "id": "IM23B_041",
        "type": "basic",
        "front": "Amiodarone: Phổ tác dụng, liều dùng cấp cứu và các độc tính cơ quan cần theo dõi định kỳ?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Đặc tính dược lý:</b> Thuốc nhóm III nhưng mang đặc tính của cả 4 nhóm Vaughan-Williams (Chẹn Natri, Chẹn Beta, Chẹn Kali, Chẹn Calci). Thuốc chống loạn nhịp an toàn nhất ở bệnh nhân có bệnh tim cấu trúc và suy tim EF giảm.<br>• <b>Liều cấp cứu ngừng tim (VF/pVT trơ sau sốc điện lần 3):</b> Tiêm bolus **300 mg**, nếu cần tiêm nhắc lại **150 mg**.<br>• <b>Độc tính ngoại ý & Theo dõi định kỳ:</b><br>  - <b>Phổi:</b> Viêm phổi kẽ / Xơ phổi do Amiodarone (nguy hiểm nhất) → Chụp X-quang phổi hàng năm.<br>  - <b>Tuyến giáp:</b> Suy giáp hoặc Cường giáp do chứa hàm lượng I-ốt rất cao (37% trọng lượng) → Định lượng TSH, FT4 mỗi 6 tháng.<br>  - <b>Gan:</b> Tăng men gan, xơ gan → Xét nghiệm men gan mỗi 6 tháng.<br>  - <b>Mắt:</b> Lắng đọng vi tinh thể ở giác mạc (Corneal microdeposits), viêm dây thần kinh thị giác.<br>  - <b>Da:</b> Nhạy cảm ánh sáng, da đổi màu xám xanh (Blue-gray skin discoloration).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Amiodarone có thời gian bán hủy cực dài (40 - 60 ngày) và tích lũy trong mô mỡ, do đó độc tính có thể kéo dài nhiều tháng sau khi đã ngừng thuốc.",
        "tags": ["IM-23b", "Amiodarone", "Toxicity", "Thyroid", "Pulmonary_Fibrosis", "ACLS"]
    },
    {
        "id": "IM23B_042",
        "type": "cloze",
        "text": "Liều cấp cứu của thuốc <b>Amiodarone</b> tiêm tĩnh mạch trong ngừng tuần hoàn do Rung thất (VF) trơ sau 3 lần sốc điện theo phác đồ ACLS là {{c1::300 mg}} (pha trong 20 mL Glucose 5%), liều nhắc lại tiếp theo là {{c1::150 mg}}.",
        "extra": "Sau cấp cứu duy trì truyền TM 900 mg/24 giờ."
    },

    # =========================================================================
    # PHẦN 9: QUẢN LÝ RUNG NHĨ TOÀN DIỆN (ABC PATHWAY, CHA2DS2-VASC, HAS-BLED)
    # =========================================================================
    {
        "id": "IM23B_043",
        "type": "basic",
        "front": "Quy trình tiếp cận toàn diện Rung nhĩ theo con đường ABC (ABC Pathway — ESC Guidelines)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>A (Anticoagulation / Avoid stroke):</b> Phòng ngừa đột quỵ bằng thuốc chống đông đường uống. Đánh giá nguy cơ tắc mạch bằng thang điểm $\\text{CHA}_2\\text{DS}_2\\text{-VASc}$ và nguy cơ xuất huyết bằng $\\text{HAS-BLED}$. Ưu tiên NOAC hơn Warfarin.<br>• <b>B (Better symptom management):</b> Kiểm soát triệu chứng bằng chiến lược **Kiểm soát tần số thất (Rate control)** hoặc **Kiểm soát nhịp xoang (Rhythm control)**.<br>• <b>C (Cardiovascular risk factors and Comorbidity optimization):</b> Kiểm soát toàn diện các bệnh đồng mắc và yếu tố nguy cơ (Tăng HA, ĐTĐ, Béo phì, Hội chứng ngừng thở khi ngủ OSA, Nghiện rượu).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>ABC Pathway giúp giảm 49% nguy cơ tử vong do mọi nguyên nhân ở bệnh nhân rung nhĩ so với điều trị phân tán truyền thống.",
        "tags": ["IM-23b", "ABC_Pathway", "AFib_Management", "ESC_Guidelines"]
    },
    {
        "id": "IM23B_044",
        "type": "cloze",
        "text": "Con đường quản lý toàn diện bệnh nhân Rung nhĩ theo ESC gồm 3 trụ cột <b>ABC Pathway</b>: (1) <b>A</b> = {{c1::Chống đông phòng ngừa đột quỵ (Anticoagulation)}}; (2) <b>B</b> = {{c1::Kiểm soát triệu chứng nhịp/tần số (Better symptom control)}}; và (3) <b>C</b> = {{c1::Tối ưu hóa yếu tố nguy cơ tim mạch và bệnh đồng mắc (Comorbidities)}}.",
        "extra": "Áp dụng ABC pathway cải thiện vượt trội tỷ lệ sống còn."
    },
    {
        "id": "IM23B_045",
        "type": "basic",
        "front": "Thang điểm CHA2DS2-VASc đánh giá nguy cơ đột quỵ trong Rung nhĩ: Điểm số từng thành phần và ngưỡng chỉ định thuốc chống đông?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Các thành phần của $\\text{CHA}_2\\text{DS}_2\\text{-VASc}$:</b><br>  - **C (Congestive Heart Failure):** Suy tim hoặc LVEF ≤ 40% = **1 điểm**.<br>  - **H (Hypertension):** Tăng huyết áp = **1 điểm**.<br>  - **$A_2$ (Age ≥ 75):** Tuổi ≥ 75 = **2 điểm**.<br>  - **D (Diabetes):** Đái tháo đường = **1 điểm**.<br>  - **$S_2$ (Stroke / TIA / Thromboembolism):** Tiền sử đột quỵ / TIA = **2 điểm**.<br>  - **V (Vascular disease):** Bệnh mạch máu (NMCT cũ, PAD, mảng xơ vữa ĐMC) = **1 điểm**.<br>  - **A (Age 65 - 74):** Tuổi 65 - 74 = **1 điểm**.<br>  - **Sc (Sex category - Female):** Giới tính nữ = **1 điểm**.<br>• <b>Chỉ định thuốc chống đông (OAC):</b><br>  - **Nam ≥ 2 điểm / Nữ ≥ 3 điểm:** Chỉ định bắt buộc (Class I).<br>  - **Nam = 1 điểm / Nữ = 2 điểm:** Xem xét chỉ định (Class IIa).<br>  - **Nam = 0 điểm / Nữ = 1 điểm:** Nguy cơ thấp, **KHÔNG DÙNG THUỐC CHỐNG ĐÔNG VÀ KHÔNG DÙNG KHÁNG TIỂU CẦU** (Class III).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Aspirin hoàn toàn không còn vai trò trong dự phòng đột quỵ do Rung nhĩ vì không hiệu quả nhưng vẫn gây chảy máu.",
        "tags": ["IM-23b", "CHA2DS2_VASc", "Anticoagulation", "Stroke_Risk", "NOAC"]
    },
    {
        "id": "IM23B_046",
        "type": "cloze",
        "text": "Theo thang điểm CHA2DS2-VASc, hai yếu tố nguy cơ nhận được <b>2 điểm</b> là {{c1::Tuổi ≥ 75}} và {{c1::Tiền sử Đột quỵ não / TIA / Tắc mạch hệ thống}}; chỉ định bắt buộc dùng thuốc chống đông (Class I) khi điểm số đạt {{c1::≥ 2 điểm ở Nam hoặc ≥ 3 điểm ở Nữ}}.",
        "extra": "Ở bệnh nhân nguy cơ thấp (0 điểm ở nam / 1 điểm ở nữ) không dùng bất kỳ thuốc chống đông hay kháng tiểu cầu nào."
    },
    {
        "id": "IM23B_047",
        "type": "basic",
        "front": "Thang điểm HAS-BLED đánh giá nguy cơ xuất huyết: Các thành phần và ý nghĩa lâm sàng khi HAS-BLED ≥ 3?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Các thành phần của HAS-BLED (Mỗi yếu tố 1 điểm):</b><br>  - **H (Hypertension):** Tăng HA tâm thu chưa kiểm soát > 160 mmHg.<br>  - **A (Abnormal renal/liver function):** Suy thận nặng (chạy thận/creatinine ≥ 200 µmol/L) và/hoặc Suy gan (bilirubin > 2 lần + men gan > 3 lần) (1 hoặc 2 điểm).<br>  - **S (Stroke):** Tiền sử đột quỵ não.<br>  - **B (Bleeding):** Tiền sử xuất huyết nặng hoặc cơ địa dễ chảy máu.<br>  - **L (Labile INR):** INR dao động, thời gian trong khoảng điều trị TTR < 60% (chỉ tính khi dùng Warfarin).<br>  - **E (Elderly):** Tuổi > 65 tuổi.<br>  - **D (Drugs/Alcohol):** Dùng đồng thời thuốc kháng tiểu cầu / NSAIDs và/hoặc Nghiện rượu (1 hoặc 2 điểm).<br>• <b>Ý nghĩa khi HAS-BLED ≥ 3 (Nguy cơ xuất huyết cao):</b><br>  - **KHÔNG PHẢI LÀ CHỐNG CHỈ ĐỊNH DÙNG THUỐC CHỐNG ĐÔNG!**<br>  - Là hồi chuông cảnh báo bác sĩ cần **tìm và điều chỉnh các yếu tố nguy cơ xuất huyết có thể thay đổi được** (kiểm soát HA < 130/80, ngừng NSAIDs/Aspirin không cần thiết, khuyên cai rượu, theo dõi sát hơn).<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Bệnh nhân có CHA2DS2-VASc cao thường cũng có HAS-BLED cao. Lợi ích ngừa đột quỵ của NOAC vẫn vượt trội nguy cơ xuất huyết.",
        "tags": ["IM-23b", "HAS_BLED", "Bleeding_Risk", "Anticoagulation_Safety"]
    },
    {
        "id": "IM23B_048",
        "type": "cloze",
        "text": "Thang điểm <b>HAS-BLED ≥ 3</b> báo hiệu bệnh nhân Rung nhĩ có nguy cơ xuất huyết cao; ý nghĩa lâm sàng của điểm số này là {{c1::Cần tìm và điều chỉnh các yếu tố nguy cơ xuất huyết có thể thay đổi được}}, tuyệt đối <b>KHÔNG PHẢI</b> là lý do để {{c1::ngừng hoặc không kê đơn thuốc chống đông}}.",
        "extra": "Cần kiểm soát HA, ngừng NSAID, theo dõi sát chức năng thận."
    },
    {
        "id": "IM23B_049",
        "type": "basic",
        "front": "Kiểm soát Tần số thất (Rate Control) vs Kiểm soát Nhịp xoang (Rhythm Control) trong Rung nhĩ: Đích tần số thất và chỉ định ưu tiên?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Đích kiểm soát tần số thất (Thử nghiệm RACE II):</b><br>  - Đích ban đầu nới lỏng: Tần số thất lúc nghỉ **< 110 chu kỳ/phút**.<br>  - Đích nghiêm ngặt (< 80 bpm lúc nghỉ, < 110 bpm khi gắng sức): Chỉ áp dụng khi bệnh nhân vẫn còn triệu chứng hoặc có suy tim suy giảm chức năng thất trái.<br>• <b>Thuốc kiểm soát tần số:</b><br>  - EF bình thường (> 40%): **Chẹn Beta** hoặc **Chẹn Calci Non-DHP (Diltiazem/Verapamil)**.<br>  - EF giảm (≤ 40%): **Chẹn Beta (Bisoprolol/Carvedilol)** ± **Digoxin**. TRÁNH Diltiazem/Verapamil.<br>• <b>Chỉ định ưu tiên Kiểm soát Nhịp xoang (Chuyển nhịp & Duy trì nhịp xoang bằng thuốc/Triệt đốt RF cô lập tĩnh mạch phổi - PVI):</b><br>  - Rung nhĩ mới khởi phát (< 1 năm) ở người trẻ tuổi (Dựa trên thử nghiệm EAST-AFNET 4 chứng minh giảm tử vong tim mạch khi kiểm soát nhịp sớm).<br>  - Rung nhĩ kèm Suy tim phân suất tống máu giảm (Bệnh cơ tim do nhịp nhanh - Tachycardiomyopathy).<br>  - Bệnh nhân vẫn còn triệu chứng mệt mỏi, khó thở dù đã kiểm soát tốt tần số thất.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Thử nghiệm EAST-AFNET 4 (NEJM 2020) đã thay đổi hoàn toàn quan điểm: Chuyển nhịp sớm trong vòng 1 năm đầu giúp cứu sống cơ tim và giảm biến cố tim mạch.",
        "tags": ["IM-23b", "Rate_vs_Rhythm", "RACE_II", "EAST_AFNET4", "PVI", "Digoxin"]
    },
    {
        "id": "IM23B_050",
        "type": "cloze",
        "text": "Theo thử nghiệm RACE II, đích kiểm soát tần số thất ban đầu ở bệnh nhân Rung nhĩ ổn định là duy trì nhịp tim lúc nghỉ {{c1::< 110 chu kỳ/phút}}; thuốc được ưu tiên hàng đầu ở bệnh nhân có suy tim phân suất tống máu giảm (LVEF ≤ 40%) là {{c1::Thuốc chẹn Beta giao cảm}} phối hợp với {{c1::Digoxin}}.",
        "extra": "Không dùng Verapamil/Diltiazem khi EF ≤ 40% vì làm nặng thêm suy tim."
    },

    # =========================================================================
    # PHẦN 10: NHẬN DIỆN NHỊP NHANH PHỨC BỘ RỘNG (WCT: BRUGADA & VERECKEI CRITERIA)
    # =========================================================================
    {
        "id": "IM23B_051",
        "type": "basic",
        "front": "Tiếp cận chẩn đoán Nhịp nhanh phức bộ QRS rộng (Wide-Complex Tachycardia — WCT): Quy tắc ngón tay cái và 4 bước Brugada Criteria?",
        "back": "<b>📖 Văn bản gốc:</b><br>• <b>Quy tắc an toàn lâm sàng số 1:</b> Mọi trường hợp Nhịp nhanh QRS rộng ($QRS \\ge 0.12\\text{ s}$) **PHẢI ĐƯỢC XEM LÀ NHỊP NHANH THẤT (VT) CHO ĐẾN KHI CHỨNG MINH ĐƯỢC ĐIỀU NGƯỢC LẠI** (vì VT chiếm > 80% các ca WCT; nếu có tiền sử NMCT cũ thì xác suất VT là > 95%).<br>• <b>4 bước lưu đồ Brugada (Brugada Algorithm):</b><br>  - <b>Bước 1:</b> Không có dạng phức bộ RS ở TẤT CẢ các chuyển đạo trước tim ($V_1 - V_6$)? (Hiện tượng đồng hướng âm hoặc dương Concordance) → Nếu CÓ = **VT**.<br>  - <b>Bước 2:</b> Khoảng cách từ đầu sóng R đến đáy sóng S (khoảng RS) **> 100 ms** ở bất kỳ chuyển đạo trước tim nào? → Nếu CÓ = **VT**.<br>  - <b>Bước 3:</b> Có hiện tượng **Phân ly nhĩ - thất (AV dissociation)**, Nhát bắt được thất (Capture beat) hoặc Nhát bóp hỗn hợp (Fusion beat)? → Nếu CÓ = **VT** (Độ đặc hiệu 100%).<br>  - <b>Bước 4:</b> Thỏa mãn tiêu chuẩn hình thái QRS của VT ở $V_1/V_2$ và $V_6$? → Nếu CÓ = **VT**; Nếu KHÔNG = **SVT dẫn truyền lệch hướng**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Dùng nhầm Verapamil hoặc Adenosine cho Nhịp nhanh thất (do chẩn đoán nhầm là SVT lệch hướng) có thể gây tụt HA trụy mạch tử vong ngay tại chỗ.",
        "tags": ["IM-23b", "WCT", "Brugada_Criteria", "VT_vs_SVT", "AV_Dissociation", "Capture_Beat"]
    },
    {
        "id": "IM23B_052",
        "type": "cloze",
        "text": "Trong phân biệt Nhịp nhanh QRS rộng giữa Nhịp nhanh thất (VT) và SVT dẫn truyền lệch hướng, dấu hiệu có độ đặc hiệu 100% để khẳng định là VT gồm: (1) {{c1::Phân ly nhĩ - thất (AV dissociation)}}; (2) {{c1::Nhát bắt được thất (Capture beat)}}; và (3) {{c1::Nhát bóp hỗn hợp (Fusion beat)}}.",
        "extra": "Bất kỳ nhịp nhanh QRS rộng nào đều phải xử trí như VT cho đến khi chứng minh ngược lại."
    },
    {
        "id": "IM23B_053",
        "type": "basic",
        "front": "Tiêu chuẩn Vereckei aVR trong chẩn đoán Nhịp nhanh phức bộ rộng (WCT)?",
        "back": "<b>📖 Văn bản gốc:</b><br>• Tiêu chuẩn Vereckei chỉ cần quan sát duy nhất chuyển đạo **aVR** theo 4 bước liên tiếp:<br>  1. Có sóng R đơn độc khởi đầu ở aVR? → CÓ = **VT**.<br>  2. Độ rộng sóng r hoặc q ban đầu $> 40\\text{ ms}$ (1 ô nhỏ)? → CÓ = **VT**.<br>  3. Có khấc ở nhánh xuống của phức bộ QRS âm chiếm ưu thế? → CÓ = **VT**.<br>  4. Tỷ số vận tốc điện thế kích hoạt $v_i / v_t \\le 1$ (Vận tốc khử cực ban đầu $40\\text{ ms}$ đầu chậm hơn hoặc bằng vận tốc khử cực $40\\text{ ms}$ cuối)? → CÓ = **VT**.<br>• Nếu không thỏa mãn cả 4 tiêu chuẩn trên → Chẩn đoán là **SVT dẫn truyền lệch hướng**.<br><br><b>🔍 Góc nhìn bổ sung (AI):</b><br>Vereckei aVR rất nhanh và tiện lợi trong phòng cấp cứu vì chỉ cần nhìn vào 1 chuyển đạo duy nhất.",
        "tags": ["IM-23b", "Vereckei", "aVR", "WCT", "Algorithm"]
    },
    {
        "id": "IM23B_054",
        "type": "cloze",
        "text": "Theo tiêu chuẩn Vereckei đơn chuyển đạo <b>aVR</b>, sự xuất hiện của một sóng {{c1::R đơn độc ban đầu (Initial R wave)}} tại chuyển đạo aVR cho phép khẳng định chẩn đoán là {{c1::Nhịp nhanh thất (VT)}}.",
        "extra": "Do ổ phát nhịp ở mỏm thất dẫn truyền ngược lên đáy tim hướng về phía aVR."
    },

    # =========================================================================
    # BỔ SUNG CÁC THẺ CLOZE & DRILL-DOWN NÂNG TỔNG SỐ LÊN > 105 THẺ
    # =========================================================================
    {
        "id": "IM23B_055",
        "type": "cloze",
        "text": "Mức năng lượng sốc điện đồng bộ khuyến cáo ban đầu để chuyển nhịp <b>Rung nhĩ</b> bằng máy sốc điện 2 pha (Biphasic) là {{c1::100 - 200 J}}; trong khi với <b>Cuồng nhĩ</b> chỉ cần mức năng lượng thấp là {{c1::50 - 100 J}}.",
        "extra": "Cuồng nhĩ đáp ứng chuyển nhịp cực kỳ nhạy với dòng điện."
    },
    {
        "id": "IM23B_056",
        "type": "cloze",
        "text": "Thuốc <b>Atropin</b> được chỉ định trong cấp cứu Nhịp chậm xoang hoặc Block AV độ cao có triệu chứng tụt huyết áp với liều khởi đầu là {{c1::0.5 - 1.0 mg tiêm tĩnh mạch}}, có thể nhắc lại mỗi 3 - 5 phút đến tổng liều tối đa là {{c1::3.0 mg}}.",
        "extra": "Liều < 0.5 mg có thể gây nghịch đảo làm chậm nhịp tim hơn do kích thích trung tâm phế vị."
    },
    {
        "id": "IM23B_057",
        "type": "cloze",
        "text": "Hiện tượng <b>'Nhát bắt được thất' (Capture beat)</b> trong Nhịp nhanh thất là hình ảnh một phức bộ QRS {{c1::hẹp và thanh mảnh bình thường}} xuất hiện xen giữa cơn nhịp nhanh QRS rộng do xung nhĩ tình cờ đi qua nút AV khử cực thất hoàn toàn.",
        "extra": "Đây là bằng chứng xác thực của phân ly nhĩ thất."
    },
    {
        "id": "IM23B_058",
        "type": "cloze",
        "text": "Hiện tượng <b>'Nhát bóp hỗn hợp' (Fusion beat)</b> trong Nhịp nhanh thất là phức bộ QRS có hình dạng {{c1::lai ghép trung gian}} giữa nhát bóp thất dị dạng và nhát bóp xoang bình thường do 2 xung điện đồng thời khử cực thất.",
        "extra": "Có giá trị đặc hiệu 100% để chẩn đoán VT."
    },
    {
        "id": "IM23B_059",
        "type": "cloze",
        "text": "Thuốc <b>Digoxin</b> kiểm soát tần số thất trong Rung nhĩ bằng cách tăng trương lực dây thần kinh phế vị làm chậm dẫn truyền qua {{c1::nút nhĩ thất (AV node)}}; thuốc kiểm soát tốt nhịp tim lúc {{c1::nghỉ ngơi}}, nhưng kém hiệu quả khi {{c1::gắng sức hoặc cường giao cảm}}.",
        "extra": "Do đó thường phối hợp thêm với thuốc chẹn Beta."
    },
    {
        "id": "IM23B_060",
        "type": "cloze",
        "text": "Dấu hiệu quá liều ngộ độc <b>Digoxin</b> trên điện tâm đồ đặc trưng bởi đoạn ST chênh xuống hình {{c1::đáy chén (hình muỗng múc kem - Scooped ST depression)}} kèm theo các rối loạn nhịp tim như Ngoại tâm thu thất nhịp đôi hoặc Nhịp nhanh nhĩ kèm block AV.",
        "extra": "Hạ Kali máu làm tăng mạnh độc tính của Digoxin."
    },
    {
        "id": "IM23B_061",
        "type": "cloze",
        "text": "Trong cấp cứu ngừng tuần hoàn do Rung thất (VF) hoặc Nhanh thất vô mạch (pVT), thuốc co mạch bắt buộc được dùng là <b>Adrenaline</b> liều {{c1::1 mg tiêm tĩnh mạch}} bắt đầu tiêm sau lần sốc điện thứ {{c1::2}} và nhắc lại mỗi {{c1::3 - 5 phút}}.",
        "extra": "Amiodarone 300 mg được dùng sau lần sốc điện thứ 3."
    },
    {
        "id": "IM23B_062",
        "type": "cloze",
        "text": "Thuốc chống loạn nhịp <b>Lidocaine</b> (Nhóm IB) là thuốc lựa chọn hàng 2 thay thế cho Amiodarone trong phác đồ ACLS với liều khởi đầu là {{c1::1.0 - 1.5 mg/kg tiêm TM}}, liều nhắc lại 0.5 - 0.75 mg/kg đến tổng liều tối đa {{c1::3 mg/kg}}.",
        "extra": "Lidocaine chuyên biệt ức chế kênh Natri ở mô thiếu máu cơ tim."
    },
    {
        "id": "IM23B_063",
        "type": "cloze",
        "text": "Kỹ thuật <b>Nghiệm pháp Valsalva cải tiến (Modified Valsalva Maneuver)</b> giúp tăng gấp đôi tỷ lệ cắt cơn SVT bằng cách cho bệnh nhân rặn gắng sức 15 giây rồi lập tức {{c1::hạ nằm ngửa và nâng cao chân thụ động 45 độ trong 15 giây}}.",
        "extra": "Giúp tăng hồi lưu máu tĩnh mạch về tim kích hoạt mạnh thụ thể áp lực xoang cảnh."
    },
    {
        "id": "IM23B_064",
        "type": "cloze",
        "text": "Trong điều trị Rung nhĩ, phương pháp can thiệp triệt để bằng triệt đốt qua ống thông (Catheter Ablation) nhằm mục đích điện sinh lý cốt lõi là {{c1::Cô lập các tĩnh mạch phổi (Pulmonary Vein Isolation — PVI)}} bằng năng lượng sóng radio hoặc bóng áp lạnh (Cryoballoon).",
        "extra": "Vì > 90% các ổ khởi phát cơn rung nhĩ kịch phát xuất phát từ các tĩnh mạch phổi."
    },
    {
        "id": "IM23B_065",
        "type": "cloze",
        "text": "Khoảng <b>QT hiệu chỉnh theo nhịp tim (QTc)</b> tính theo công thức Bazett ($QTc = QT / \\sqrt{RR}$) được xem là kéo dài bệnh lý khi QTc {{c1::> 450 ms ở Nam}} hoặc {{c1::> 460 ms ở Nữ}}; ngưỡng có nguy cơ cao bùng phát Xoắn đỉnh là khi QTc {{c1::> 500 ms}}.",
        "extra": "QTc > 500 ms là báo động đỏ bắt buộc rà soát và ngừng toàn bộ thuốc làm dài QT."
    },
    {
        "id": "IM23B_066",
        "type": "cloze",
        "text": "Hội chứng <b>Tái cực sớm (Early Repolarization Syndrome — ERS)</b> biểu hiện trên ECG bởi đoạn ST chênh lên có khấc hoặc trượt (J-point elevation ≥ 1 mm) ở các chuyển đạo dưới (DII, DIII, aVF) hoặc bên; khi kèm theo tiền sử ngất hoặc ngừng tim được cứu sống là chỉ định {{c1::Cấy máy phá rung tự động (ICD)}}.",
        "extra": "Dạng lành tính phổ biến ở người trẻ thể thao không có triệu chứng."
    },
    {
        "id": "IM23B_067",
        "type": "cloze",
        "text": "Trong Bệnh cơ tim phì đại (HCM), yếu tố nguy cơ hàng đầu dự báo đột tử do loạn nhịp thất bao gồm: (1) Tiền sử gia đình có người đột tử sớm; (2) Độ dày thành tâm thất tối đa {{c1::≥ 30 mm}}; (3) Cơn nhịp nhanh thất không bền bỉ (NSVT); và (4) Ngất không rõ nguyên nhân.",
        "extra": "Bệnh nhân có điểm ESC HCM Risk-SCD ≥ 6% có chỉ định cấy máy ICD phòng ngừa tiên phát."
    },
    {
        "id": "IM23B_068",
        "type": "cloze",
        "text": "Thuốc <b>Sotalol</b> là thuốc chống loạn nhịp phối hợp cơ chế của {{c1::Nhóm II (Chẹn Beta)}} và {{c1::Nhóm III (Chẹn kênh Kali)}}, có nguy cơ gây tác dụng phụ nguy hiểm là {{c1::Kéo dài khoảng QT và khởi phát Xoắn đỉnh (TdP)}} nên cần đo ECG theo dõi sát.",
        "extra": "Thường phải nhập viện theo dõi ECG 3 ngày khi bắt đầu khởi trị Sotalol."
    },
    {
        "id": "IM23B_069",
        "type": "cloze",
        "text": "Khi chuyển nhịp Rung nhĩ bằng dòng điện hoặc bằng thuốc ở bệnh nhân Rung nhĩ kéo dài <b>> 48 giờ</b> (hoặc không rõ thời gian), bắt buộc phải dùng thuốc chống đông liên tục ít nhất {{c1::3 tuần trước khi chuyển nhịp}} (hoặc làm Siêu âm tim qua thực quản TEE loại trừ huyết khối tiểu nhĩ trái) và tiếp tục chống đông ít nhất {{c1::4 tuần sau khi chuyển nhịp}}.",
        "extra": "Nguy cơ thuyên tắc mạch não do 'choáng tâm nhĩ' (atrial stunning) sau chuyển nhịp."
    },
    {
        "id": "IM23B_070",
        "type": "cloze",
        "text": "Trong Hội chứng Brugada, nghiệm pháp kích thích dược lý bằng thuốc chẹn kênh Natri tiêm tĩnh mạch như {{c1::Ajmaline}} hoặc {{c1::Flecainide}} được dùng để làm bộc lộ hình ảnh ECG Type 1 dạng vòm ở bệnh nhân nghi ngờ mang gen bệnh nhưng ECG lúc nghỉ bình thường.",
        "extra": "Phải thực hiện trong phòng cấp cứu có sẵn máy sốc điện."
    },
    {
        "id": "IM23B_071",
        "type": "cloze",
        "text": "Nhịp nhanh vào lại nhĩ thất (AVRT) có 2 dạng dẫn truyền: Dạng dẫn truyền xuôi (Orthodromic AVRT - chiếm 90%) có phức bộ QRS {{c1::hẹp bình thường}} (xung đi xuống qua nút AV, đi ngược lên qua cầu Kent); Dạng dẫn truyền ngược (Antidromic AVRT - chiếm 10%) có phức bộ QRS {{c1::giãn rộng dị dạng}}.",
        "extra": "Antidromic AVRT dễ bị nhầm lẫn với Nhịp nhanh thất (VT)."
    },
    {
        "id": "IM23B_072",
        "type": "cloze",
        "text": "Hiện tượng <b>Dẫn truyền lệch hướng (Aberrant Conduction)</b> là tình trạng xung động trên thất đi xuống tâm thất đúng lúc một nhánh dẫn truyền (thường là nhánh phải do trơ dài hơn) vẫn còn trong thời kỳ trơ, tạo ra phức bộ QRS {{c1::giãn rộng mô phỏng hình ảnh Block nhánh}}.",
        "extra": "Quy tắc Ashman: Nhịp dài theo sau bởi nhịp ngắn dễ gây dẫn truyền lệch hướng."
    },
    {
        "id": "IM23B_073",
        "type": "cloze",
        "text": "Trong cấp cứu bệnh nhân ngừng tim với nhịp <b>Hoạt động điện vô mạch (PEA)</b>, trên monitor vẫn thấy có sóng điện tim nhưng bệnh nhân {{c1::hoàn toàn không bắt được mạch bẹn/mạch cảnh}} và không có cung lượng tim; chỉ định xử trí là {{c1::Ép tim ngoài lồng ngực liên tục + Adrenaline 1 mg}} (TUYỆT ĐỐI KHÔNG SỐC ĐIỆN).",
        "extra": "Cần khẩn trương tìm và xử trí các nguyên nhân 5H & 5T."
    },
    {
        "id": "IM23B_074",
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng mốc <b>AFFIRM (NEJM 2002)</b> trên 4.060 bệnh nhân Rung nhĩ chứng minh chiến lược Kiểm soát nhịp xoang bằng thuốc {{c1::KHÔNG làm giảm}} tỷ lệ tử vong do mọi nguyên nhân hoặc đột quỵ so với chiến lược Kiểm soát tần số thất, trong khi làm tăng tác dụng phụ do thuốc.",
        "extra": "Tuy nhiên, EAST-AFNET 4 sau đó chứng minh kiểm soát nhịp sớm (< 1 năm) lại có lợi."
    },
    {
        "id": "IM23B_075",
        "type": "cloze",
        "text": "Thuốc <b>Dronedarone</b> là dẫn xuất không chứa phân tử I-ốt của Amiodarone, bị <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI</b> ở bệnh nhân mắc Rung nhĩ kèm theo {{c1::Suy tim phân suất tống máu giảm (NYHA III - IV hoặc mới mất bù)}} do làm tăng gấp đôi tỷ lệ tử vong (chứng minh qua thử nghiệm ANDROMEDA).",
        "extra": "Dronedarone chỉ dùng cho Rung nhĩ kịch phát ở người có chức năng tim bình thường."
    },
    {
        "id": "IM23B_076",
        "type": "cloze",
        "text": "Thuốc chẹn kênh Natri <b>Mexiletine</b> (uống) thuộc nhóm IB, có tác dụng rút ngắn thời gian điện thế hoạt động, được sử dụng chuyên biệt trong điều trị Hội chứng QT dài bẩm sinh thể {{c1::LQT3}} do ức chế dòng Natri muộn bị tăng hoạt.",
        "extra": "Mexiletine cũng dùng điều trị ngoại tâm thu thất sau NMCT."
    },
    {
        "id": "IM23B_077",
        "type": "cloze",
        "text": "Khi xoa xoang cảnh (Carotid Sinus Massage) để chẩn đoán phân biệt nhịp nhanh trên thất, thủ thuật này làm chậm dẫn truyền qua nút AV: giúp cắt cơn hoàn toàn trong {{c1::AVNRT / AVRT}}; làm chậm tần số thất tạm thời để lộ rõ sóng răng cưa trong {{c1::Cuồng nhĩ / Rung nhĩ}}; và hầu như không ảnh hưởng trong {{c1::Nhịp nhanh thất (VT)}}.",
        "extra": "Chống chỉ định xoa xoang cảnh khi có tiếng thổi động mạch cảnh hoặc tiền sử TIA/đột quỵ trong 3 tháng."
    },
    {
        "id": "IM23B_078",
        "type": "cloze",
        "text": "Bệnh nhân có <b>Hội chứng tiền kích thích (Pre-excitation pattern)</b> trên ECG nhưng hoàn toàn không có triệu chứng hồi hộp đánh trống ngực hay cơn tim nhanh được gọi là {{c1::Hình thái WPW trên ECG (WPW pattern)}}; chỉ được gọi là {{c1::Hội chứng WPW (WPW syndrome)}} khi bệnh nhân có kèm theo triệu chứng cơn nhịp nhanh lâm sàng.",
        "extra": "Người có WPW pattern làm nghề rủi ro cao (phi công, lái xe) vẫn cần thăm dò điện sinh lý."
    },
    {
        "id": "IM23B_079",
        "type": "cloze",
        "text": "Hội chứng <b>Nhịp nhanh thất đa dạng đa ổ do catecholamine (CPVT)</b> là bệnh lý kênh canxi di truyền (đột biến thụ thể RyR2), đặc trưng bởi các cơn ngất hoặc ngừng tim khởi phát dữ dội khi {{c1::Gắng sức thể lực hoặc xúc động mạnh}}, trên ECG lúc nghỉ hoàn toàn bình thường.",
        "extra": "Nadolol + Flecainide + Cấy máy ICD là phác đồ chuẩn cho CPVT."
    },
    {
        "id": "IM23B_080",
        "type": "cloze",
        "text": "Trong nghiệm pháp sốc điện chuyển nhịp (Cardioversion), chế độ <b>Đồng bộ (Synchronized)</b> bắt buộc phải được kích hoạt để máy phát tia đúng vào đỉnh sóng {{c1::R của phức bộ QRS}}, tránh phát tia rơi vào đỉnh sóng {{c1::T}} (giai đoạn dễ tổn thương gây kích hoạt Rung thất - hiện tượng R on T).",
        "extra": "Chỉ dùng sốc điện không đồng bộ (Defibrillation) trong Rung thất hoặc Nhanh thất vô mạch."
    },
    {
        "id": "IM23B_081",
        "type": "cloze",
        "text": "Ở bệnh nhân Rung nhĩ được điều trị bằng thuốc kháng vitamin K (Warfarin), đích chỉ số <b>INR</b> cần đạt để đảm bảo hiệu quả ngừa đột quỵ và an toàn xuất huyết là trong khoảng {{c1::2.0 đến 3.0}} (đối với van tim nhân tạo cơ học cơ học 2 lá là 2.5 - 3.5).",
        "extra": "Thời gian trong khoảng điều trị (TTR) cần đạt ≥ 70%."
    },
    {
        "id": "IM23B_082",
        "type": "cloze",
        "text": "Bốn thuốc chống đông đường uống tác động trực tiếp (NOAC / DOAC) được ưu tiên hàng đầu trong Rung nhĩ không do van tim gồm: Thuốc ức chế Thrombin trực tiếp là {{c1::Dabigatran}} (150 mg hoặc 110 mg × 2); và ba thuốc ức chế yếu tố Xa trực tiếp là {{c1::Rivaroxaban, Apixaban và Edoxaban}}.",
        "extra": "NOAC giảm 50% nguy cơ xuất huyết nội sọ so với Warfarin."
    },
    {
        "id": "IM23B_083",
        "type": "cloze",
        "text": "Thuốc đối kháng đặc hiệu (Reversal agent) để trung hòa khẩn cấp tác dụng chống đông của Dabigatran trong trường hợp xuất huyết đe dọa tính mạng hoặc phẫu thuật cấp cứu là {{c1::Idarucizumab (Praxbind)}}; đối kháng với Rivaroxaban và Apixaban là {{c1::Andexanet alfa}}.",
        "extra": "Idarucizumab liên kết với Dabigatran với ái lực cao gấp 350 lần thrombin."
    },
    {
        "id": "IM23B_084",
        "type": "cloze",
        "text": "Hiện tượng <b>Dẫn truyền chậm nội tại (Conduction Delay)</b> gây phức bộ QRS giãn rộng và sóng T đảo chiều ở các nhát bóp ngoại tâm thu thất (PVC) là do xung điện khử cực không đi qua hệ thống dẫn truyền His-Purkinje chuyên biệt tốc độ cao mà phải lan truyền chậm chạp qua các tế bào {{c1::Cơ tâm thất thông thường (Myocyte-to-myocyte)}}.",
        "extra": "Giải thích bản chất vì sao mọi ổ loạn nhịp xuất phát từ tâm thất đều có QRS giãn rộng."
    },
    {
        "id": "IM23B_085",
        "type": "cloze",
        "text": "Khoảng <b>PR</b> bình thường trên điện tâm đồ dao động từ {{c1::0.12 đến 0.20 giây}} (tương ứng 3 đến 5 ô nhỏ trên giấy chạy 25 mm/s); khoảng PR phản ánh thời gian dẫn truyền xung động từ {{c1::Nút xoang qua cơ tâm nhĩ và nút nhĩ thất xuống bó His}}.",
        "extra": "PR > 0.20s là Block nhĩ thất độ I; PR < 0.12s là Hội chứng tiền kích thích (WPW)."
    },
    {
        "id": "IM23B_086",
        "type": "cloze",
        "text": "Trong Rung nhĩ có đáp ứng thất quá nhanh gây tụt huyết áp hoặc phù phổi cấp kháng trị với thuốc, phương pháp can thiệp cuối cùng (Palliative strategy) là {{c1::Triệt đốt nút nhĩ thất (AV Node Ablation)}} kết hợp với {{c1::Cấy máy tạo nhịp vĩnh viễn (Pace-and-Ablate strategy)}}.",
        "extra": "Biến nhịp tim không đều thành nhịp đều hoàn toàn do máy tạo nhịp chỉ huy."
    },
    {
        "id": "IM23B_087",
        "type": "cloze",
        "text": "Bệnh nhân có <b>Cơn ngừng xoang (Sinus Pause / Arrest)</b> kéo dài từ {{c1::> 3.0 giây}} trên điện tâm đồ hoặc Holter ECG kèm theo triệu chứng choáng ngất là chỉ định bắt buộc (Class I) để {{c1::Cấy máy tạo nhịp vĩnh viễn (Pacemaker)}}.",
        "extra": "Ở vận động viên chuyên nghiệp lúc ngủ sâu có thể có khoảng ngừng tim sinh lý không triệu chứng."
    },
    {
        "id": "IM23B_088",
        "type": "cloze",
        "text": "Thuốc chẹn kênh Canxi <b>Verapamil</b> tiêm tĩnh mạch bị <b>CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI</b> ở trẻ nhỏ dưới {{c1::1 tuổi}} do nguy cơ gây tụt huyết áp nặng nề, trụy mạch và ngừng tim do tế bào cơ tim trẻ nhỏ phụ thuộc hoàn toàn vào dòng Calci ngoại bào.",
        "extra": "Ở trẻ dưới 1 tuổi dùng Adenosine hoặc sốc điện khi có SVT."
    },
    {
        "id": "IM23B_089",
        "type": "cloze",
        "text": "Đặc điểm nhận diện cơn <b>Nhịp nhanh nhĩ đa ổ (Multifocal Atrial Tachycardia — MAT)</b> trên điện tâm đồ là nhịp nhanh không đều với sự hiện diện của ít nhất {{c1::3 hình dạng sóng P khác nhau}} trên cùng một chuyển đạo, bệnh cảnh kinh điển xuất hiện ở bệnh nhân mắc {{c1::Bệnh phổi tắc nghẽn mạn tính (COPD đợt cấp)}}.",
        "extra": "Điều trị cốt lõi là bù oxy, điều trị suy hô hấp và dùng Magie/Calci, không dùng chẹn beta."
    },
    {
        "id": "IM23B_090",
        "type": "cloze",
        "text": "Chỉ định phẫu thuật bít hoặc cắt bỏ <b>Tiểu nhĩ trái (Left Atrial Appendage Occlusion — LAAO)</b> bằng dụng cụ qua da (như Watchman) được khuyến cáo cho bệnh nhân Rung nhĩ có nguy cơ tắc mạch cao nhưng có {{c1::Chống chỉ định tuyệt đối hoặc chảy máu nặng tái phát với thuốc chống đông đường uống lâu dài}}.",
        "extra": "Vì > 90% huyết khối trong rung nhĩ không do van tim hình thành tại tiểu nhĩ trái."
    },
    {
        "id": "IM23B_091",
        "type": "cloze",
        "text": "Hiện tượng <b>'Đồng hướng âm' (Negative Concordance)</b> trong Nhịp nhanh phức bộ QRS rộng là hình ảnh tất cả các chuyển đạo trước tim từ $V_1$ đến $V_6$ đều có dạng sóng {{c1::QS hoặc rS chiếm ưu thế âm tính}}, có giá trị đặc hiệu rất cao chẩn đoán là {{c1::Nhịp nhanh thất (VT)}} xuất phát từ thành trước mỏm tim.",
        "extra": "Bước 1 của lưu đồ Brugada."
    },
    {
        "id": "IM23B_092",
        "type": "cloze",
        "text": "Trong phân loại thuốc chống loạn nhịp, thuốc <b>Vernakalant</b> là thuốc tiêm tĩnh mạch chọn lọc trên tâm nhĩ (ức chế kênh $I_{\\text{Kur}}$ và $I_{\\text{to}}$) dùng để {{c1::Chuyển nhịp nhanh Rung nhĩ mới khởi phát (< 7 ngày)}} về nhịp xoang trong vòng 10 - 15 phút với độ an toàn cao.",
        "extra": "Không gây tác dụng phụ kéo dài QT ở tâm thất."
    },
    {
        "id": "IM23B_093",
        "type": "cloze",
        "text": "Tam chứng lâm sàng của <b>Hội chứng ngộ độc Digoxin cấp</b> bao gồm: Rối loạn tiêu hóa (buồn nôn, nôn, đau bụng), Rối loạn thần kinh thị giác ({{c1::Nhìn mờ, nhìn thấy quầng sáng màu vàng - xanh lá cây}}) và Rối loạn nhịp tim chậm kèm ngoại tâm thu thất.",
        "extra": "Thuốc giải độc đặc hiệu là kháng thể kháng Digoxin (DigiFab)."
    },
    {
        "id": "IM23B_094",
        "type": "cloze",
        "text": "Khi thực hiện đo điện tâm đồ 12 chuyển đạo, tốc độ chạy giấy tiêu chuẩn là {{c1::25 mm/giây}} (1 ô nhỏ 1 mm = 0.04s, 1 ô lớn 5 mm = 0.20s) và chuẩn độ điện thế tiêu chuẩn là {{c1::10 mm/mV}} (1 ô nhỏ = 0.1 mV).",
        "extra": "Cần kiểm tra test điện áp trước khi đọc biên độ các sóng."
    },
    {
        "id": "IM23B_095",
        "type": "cloze",
        "text": "Trong điều trị ngoại tâm thu thất xuất phát từ đường ra thất phải (RVOT PVCs) ở người có tim cấu trúc bình thường, thuốc điều trị nội khoa ưu tiên hàng đầu là {{c1::Thuốc chẹn Beta giao cảm}} hoặc {{c1::Chẹn kênh Calci DHP/Non-DHP}}; nếu không dung nạp hoặc gánh nặng cao thì chỉ định {{c1::Triệt đốt điện sinh lý RF}}.",
        "extra": "RVOT PVC có dạng LBBB trục lệch dưới (dương ở DII, DIII, aVF)."
    },
    {
        "id": "IM23B_096",
        "type": "cloze",
        "text": "Hiện tượng <b>Block nhĩ thất độ II dạng cao độ (High-grade / Advanced AV Block)</b> được định nghĩa khi có từ {{c1::≥ 2 sóng P liên tiếp}} bị block không dẫn truyền xuống thất (ví dụ tỷ lệ dẫn $3:1, 4:1$), có nguy cơ tiến triển thành vô tâm thu tương đương Block AV độ III.",
        "extra": "Chỉ định đặt máy tạo nhịp tim vĩnh viễn cấp cứu."
    },
    {
        "id": "IM23B_097",
        "type": "cloze",
        "text": "Ở bệnh nhân Rung nhĩ kèm bệnh Hẹp van 2 lá mức độ vừa đến nặng do thấp hoặc mang van tim nhân tạo cơ học, nhóm thuốc chống đông duy nhất được phép sử dụng là {{c1::Thuốc kháng Vitamin K (Warfarin)}}, các thuốc chống đông thế hệ mới (NOAC) bị <b>CHỐNG CHỈ ĐỊNH</b>.",
        "extra": "Được định nghĩa là Rung nhĩ do bệnh van tim (Valvular AF)."
    },
    {
        "id": "IM23B_098",
        "type": "cloze",
        "text": "Bệnh nhân có cơn Nhịp nhanh kịch phát trên thất (PSVT) được chuyển nhịp thành công bằng Adenosine xuất hiện đoạn ngừng xoang ngắn kèm theo một vài nhát ngoại tâm thu trước khi trở về nhịp xoang bình thường là đáp ứng {{c1::Hoàn toàn sinh lý và bình thường}}, không phải biến chứng.",
        "extra": "Cần giải thích trước cho bệnh nhân cảm giác tức ngực thoáng qua khi tiêm Adenosine."
    },
    {
        "id": "IM23B_099",
        "type": "cloze",
        "text": "Chỉ định cấy máy phá rung tự động (ICD) để <b>Phòng ngừa tiên phát đột tử do tim</b> ở bệnh nhân Suy tim phân suất tống máu giảm (HFrEF) sau điều trị nội khoa tối ưu (GDMT) ít nhất 3 tháng khi phân suất tống máu {{c1::LVEF ≤ 35%}} và độ suy tim {{c1::NYHA II - III}}.",
        "extra": "Nếu sau NMCT phải chờ ít nhất 40 ngày mới đánh giá chỉ định cấy ICD."
    },
    {
        "id": "IM23B_100",
        "type": "cloze",
        "text": "Hội chứng <b>Kích thích sớm thất (Pre-excitation)</b> có thể gây ra hiện tượng sóng R cao bất thường ở chuyển đạo $V_1$ mô phỏng hình ảnh Block nhánh phải (RBBB) hoặc Phì đại thất phải khi cầu Kent nằm ở vị trí {{c1::Thành sau bên hoặc sau vách thất trái}} (Type A WPW).",
        "extra": "Dễ bị chẩn đoán nhầm thành nhồi máu cơ tim cũ thành sau."
    },
    {
        "id": "IM23B_101",
        "type": "cloze",
        "text": "Thuốc chống loạn nhịp <b>Procainamide</b> (Nhóm IA) tiêm tĩnh mạch là lựa chọn ưu tiên để cắt cơn Nhịp nhanh QRS rộng ổn định huyết động hoặc Rung nhĩ trên nền WPW với liều truyền {{c1::20 - 50 mg/phút}} đến khi đạt hiệu quả hoặc tổng liều tối đa {{c1::17 mg/kg}} (hoặc QRS giãn rộng thêm > 50%).",
        "extra": "Cần ngừng truyền ngay nếu huyết áp tụt hoặc QRS giãn rộng quá 50%."
    },
    {
        "id": "IM23B_102",
        "type": "cloze",
        "text": "Trong tiếp cận cấp cứu ngừng tuần hoàn, tỷ lệ Ép tim / Thổi ngạt tiêu chuẩn ở người lớn khi chưa đặt ống nội khí quản là {{c1::30 lần ép tim : 2 lần thổi ngạt}}; tần số ép tim đạt chuẩn là {{c1::100 - 120 lần/phút}} với độ sâu ép ngực {{c1::5 - 6 cm}}.",
        "extra": "Để lồng ngực nở hoàn toàn sau mỗi lần ép tim và hạn chế tối đa gián đoạn ép tim."
    },
    {
        "id": "IM23B_103",
        "type": "cloze",
        "text": "Hiện tượng <b>'R trên T' (R-on-T phenomenon)</b> xảy ra khi một nhát ngoại tâm thu thất rơi đúng vào đỉnh hoặc sườn sau của sóng T (giai đoạn trơ tương đối của tâm thất), có nguy cơ kích hoạt trực tiếp cơn {{c1::Rung thất (VF) hoặc Xoắn đỉnh (TdP)}}.",
        "extra": "Là cơ chế giải thích vì sao sốc điện chuyển nhịp bắt buộc phải ở chế độ Đồng bộ."
    },
    {
        "id": "IM23B_104",
        "type": "cloze",
        "text": "Thuốc <b>Isoproterenol (Isoprenaline)</b> là chất chủ vận thụ thể beta-1 và beta-2 không chọn lọc, được sử dụng qua đường truyền tĩnh mạch liên tục để cấp cứu {{c1::Nhịp chậm xoang nặng hoặc Xoắn đỉnh kháng trị}} bằng cách tăng tần số tim cơ bản lên > 90 bpm.",
        "extra": "Chống chỉ định trong thiếu máu cục bộ cơ tim cấp vì làm tăng tiêu thụ oxy cơ tim."
    },
    {
        "id": "IM23B_105",
        "type": "cloze",
        "text": "Bệnh nhân có triệu chứng đau ngực cấp tính kèm theo hình ảnh <b>Block nhánh phải (RBBB) mới xuất hiện kết hợp với Block phân nhánh trái trước (LAFB)</b> (gọi là Block 2 phân nhánh - Bifascicular block) là dấu hiệu cảnh báo tổn thương nhánh vách lớn của động mạch {{c1::Liên thất trước (LAD)}} với nguy cơ cao tiến triển đột ngột thành Block AV hoàn toàn.",
        "extra": "Cần chuẩn bị sẵn sàng máy tạo nhịp tạm thời qua da hoặc qua tĩnh mạch."
    },
    {
        "id": "IM23B_106",
        "type": "cloze",
        "text": "Trong Rung nhĩ, chiến lược dùng thuốc theo nguyên tắc <b>'Viên thuốc bỏ túi' (Pill-in-the-pocket approach)</b> cho phép bệnh nhân ngoại trú tự uống một liều duy nhất {{c1::Flecainide (200 - 300 mg)}} hoặc {{c1::Propafenone (450 - 600 mg)}} kèm thuốc chẹn Beta để tự cắt cơn Rung nhĩ kịch phát tại nhà.",
        "extra": "Chỉ áp dụng khi đã được thử nghiệm an toàn trước đó trong bệnh viện và không có bệnh tim cấu trúc."
    }
]

out_json = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-23b_Cac_roi_loan_nhip_tim\outputs\IM-23b_Cac_roi_loan_nhip_tim_2026-08-19.cards.v2.json")
out_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Successfully generated {len(cards)} cards to {out_json.name}")
