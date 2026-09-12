# -*- coding: utf-8 -*-
import json
from pathlib import Path

md_path = Path(r"F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/P3_HFrEF_man/IM-22_P3_HFrEF_man_2026-07-30_RELEASE_v1.md")
cards_path = Path(r"F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/P3_HFrEF_man/IM-22_P3_HFrEF_man_2026-07-30_RELEASE_v1.cards.v2.json")

p0 = """# BÀI HỌC Y KHOA: BỆNH LÝ SUY TIM - PHẦN 3: ĐIỀU TRỊ SUY TIM PHÂN SUẤT TỐNG MÁU GIẢM MẠN TÍNH (HFrEF MẠN)
**Ngày:** 2026-07-30 | **Chuyên khoa:** Nội tim mạch / Dược lý lâm sàng | **Đối tượng:** Bác sĩ lâm sàng, học viên sau đại học và người học mất gốc cần học từ nền tảng

---

## 0. TỔNG QUAN — VÌ SAO ĐIỀU TRỊ HFrEF MẠN LẠI QUAN TRỌNG?

### 0.1 Nền tảng tối thiểu cần dùng ngay

> Để hiểu sâu sắc cơ chế tác dụng của các thuốc lợi tiểu và các thuốc can thiệp vào hệ thống thần kinh thể dịch (RAAS, SNS, Neprilysin, SGLT2) trong suy tim mạn tính, người học nên xem lại bài nền tảng về [sinh lý nephron].

Suy tim phân suất tống máu giảm mạn tính (Chronic Heart Failure with Reduced Ejection Fraction - HFrEF mạn) là một hội chứng lâm sàng phức tạp và nguy hiểm.

Hội chứng này đại diện cho con đường chung cuối cùng của nhiều bệnh lý tim mạch nguyên phát:
- Bệnh cơ tim thiếu máu cục bộ do nhồi máu cơ tim cũ hoặc hẹp động mạch vành mạn tính tiến triển.
- Tăng huyết áp lâu ngày không kiểm soát tốt gây tăng gánh hậu tải kéo dài.
- Bệnh cơ tim giãn nguyên phát hoặc do độc chất như rượu hay hóa chất điều trị ung thư.
- Bệnh van tim mạn tính như hở van hai lá mạn hoặc hẹp hở van động mạch chủ tiến triển.

HFrEF mạn được xác định chính xác khi phân suất tống máu thất trái LVEF giảm xuống mức bốn mươi phần trăm trở xuống.

Hội chứng này bắt buộc phải đi kèm với các triệu chứng lâm sàng rõ rệt:
- Khó thở khi gắng sức nhẹ hoặc gắng sức vừa.
- Khó thở khi nằm phẳng.
- Khó thở kịch phát về đêm.
- Giảm khả năng dung nạp thể lực, mệt mỏi mạn tính, cạn kiệt năng lượng.

Đồng thời có các dấu hiệu sung huyết thể tích rõ rệt:
- Phù hai cẳng chân và phù mu bàn chân.
- Tĩnh mạch cổ nổi ở tư thế nghiêng.
- Ran ẩm ứ đọng ở hai đáy phổi.
- Phản hồi gan - tĩnh mạch cổ dương tính.
- Gan lớn sung huyết gây tức nhẹ vùng hạ sườn phải.

Ví dụ 1: Một bệnh nhân nam 60 tuổi tiền sử nhồi máu cơ tim cũ có LVEF = 32% kèm khó thở khi đi bộ 50m là hình mẫu điển hình của HFrEF mạn.

Trong lịch sử y khoa thập niên 1970-1980, suy tim từng được coi là một bệnh lý huyết động đơn thuần.
Tim bị suy yếu được ví như một cái bơm hỏng và việc điều trị chỉ tập trung vào:
- Kích thích tim bóp mạnh hơn bằng các thuốc trợ tim glycoside.
- Rút dịch dư thừa ra khỏi cơ thể bằng lợi tiểu quai.

Tuy nhiên, cách tiếp cận này chỉ giúp cải thiện triệu chứng sung huyết ngắn hạn.
Nó hoàn toàn KHÔNG làm giảm tỷ lệ tử vong.
Thậm chí việc dùng thuốc trợ tim kích thích co bóp đơn độc còn làm tăng nguy cơ tử vong do loạn nhịp thất.

Cuộc cách mạng dược lý trong 30 năm qua đã làm thay đổi hoàn toàn tư duy y học:
Suy tim mạn tính thực chất là một bệnh lý tiến triển do sự kích hoạt quá mức thần kinh thể dịch mạn tính.

Sự suy giảm chức năng co bóp tim ban đầu kích hoạt hai hệ thống bù trừ lớn:
1. **Trục Giao cảm thần kinh (SNS)**:
   - Tăng tiết Norepinephrine toàn thân.
   - Tăng tần số tim, tăng sức bóp cơ tim và co mạch ngoại biên để duy trì huyết áp.
2. **Hệ Renin-Angiotensin-Aldosterone (RAAS)**:
   - Giảm tưới máu thận làm tế bào cạnh cầu thận tiết Renin.
   - Renin chuyển Angiotensinogen thành Angiotensin I.
   - ACE chuyển Angiotensin I thành Angiotensin II.
   - Angiotensin II co mạch hệ thống mạnh và kích thích vỏ thượng thận tiết Aldosterone gây giữ Natri và nước.

Mặc dù các phản ứng bù trừ này giúp duy trì huyết áp và tưới máu cơ quan ban đầu, nhưng về lâu dài chúng tạo ra một vòng xoắn bệnh lý độc hại:
- Tăng hậu tải và tăng tiền tải quá mức làm tim căng giãn.
- Độc tính tế bào do nồng độ Catecholamine tăng cao mạn tính làm phì đại và chết tế bào cơ tim.
- Tái cấu trúc cơ tim tiến triển làm thay đổi hình dạng thất trái từ hình bầu dục sang hình cầu.

Hậu quả là thất trái ngày càng giãn to, cơ tim bị xơ hóa nặng nề, LVEF giảm thêm và bệnh nhân tử vong vì suy tim tiến triển hoặc tử vong đột ngột do rối loạn nhịp thất.

Ví dụ 2: Sự xơ hóa cơ tim do Aldosterone tăng cao kéo dài làm các tế bào cơ tim bị thay thế bằng mô xơ collagen type I, khiến tâm thất bị đờ cứng và dễ phát sinh cơn nhịp nhanh thất nguy hiểm.

{claim:G-P3-SCOPE} Hướng dẫn AHA/ACC/HFSA 2022 nhằm cung cấp các khuyến nghị lấy người bệnh làm trung tâm cho bác sĩ lâm sàng để phòng ngừa, chẩn đoán và quản lý người bệnh suy tim: patient-centric recommendations for clinicians to prevent, diagnose, and manage patients with heart failure. [GUIDELINE VERIFIED] [PMID: 35363499]

Mục tiêu tối thượng của điều trị HFrEF mạn tính hiện đại KHÔNG CHỈ là giảm triệu chứng sung huyết.
Mục tiêu chính là ức chế triệt để các con đường thần kinh thể dịch độc hại, đảo ngược quá trình tái cấu trúc thất trái, giảm tỷ lệ nhập viện vì suy tim và kéo dài tỷ lệ sống sót cho người bệnh suy tim mạn tính.
Việc áp dụng đồng thời các biện pháp điều trị tối ưu giúp mang lại hiệu quả bảo vệ toàn diện cho hệ tim mạch và bảo vệ chức năng thận dài hạn.

**Mục tiêu bài học:**
- Nắm vững cơ chế sinh lý bệnh thần kinh thể dịch và dược lý học của "Tứ trụ" điều trị HFrEF (ARNI/ACEi/ARB, Beta-blocker, MRA, SGLT2i).
- Thuộc lòng liều khởi đầu, liều mục tiêu và thuật toán chuẩn độ nhanh (Rapid Titration Protocol) trong vòng 2-4 tuần.
- Thành thạo xử trí các biến cố lâm sàng thường gặp khi điều trị: tụt huyết áp, tăng Kali máu, tăng Creatinine serum (giảm eGFR), ho khan và phù mạch.
- Áp dụng thành thạo thuật toán giải quyết kháng lợi tiểu quai và các thuốc điều trị phối hợp nâng cao (Ivabradine, Vericiguat, Hydralazine-ISDN, Digoxin, Bù sắt IV).
- Giải quyết 5 ca lâm sàng phức tạp theo đúng 5 bước chuẩn hóa safety & efficacy.

---"""

p1 = """
## 1. BẢN ĐỒ NHÓM THUỐC VÀ DƯỢC LÝ DỰA TRÊN SINH LÝ BỆNH [CỐT LÕI]

### 1.0 Nền tảng: Sinh lý bình thường & Sinh lý bệnh bù trừ trong HFrEF [CỐT LÕI]

Để hiểu tại sao các nhóm thuốc điều trị suy tim lại có thể cứu sống bệnh nhân, chúng ta bắt đầu từ mối tương quan giữa chức năng co bóp thất trái, các đáp ứng bù trừ thần kinh thể dịch và cấu trúc mô học của cơ tim.

Bình thường, thể tích tống máu (Stroke Volume - SV) của thất trái phụ thuộc vào 3 yếu tố cơ bản:
- **Tiền tải (Preload)**:
  - Thể tích thất cuối tâm trương (LVEDV).
  - Phản ánh độ căng giãn của sợi cơ tim trước khi bắt đầu co bóp.
- **Sức co bóp cơ tim (Contractility)**:
  - Khả năng chủ động rút ngắn của sợi cơ tim.
  - Phụ thuộc vào nồng độ Ca2+ nội bào gắn với Troponin C.
- **Hậu tải (Afterload)**:
  - Sức kháng mạch máu hệ thống (SVR).
  - Áp lực mà tâm thất trái phải vượt qua để mở van động mạch chủ và tống máu ra ngoại biên.

Cung lượng tim (Cardiac Output - CO) được tính bằng công thức: CO = SV × HR (Tần số tim).

Khi cơ tim bị tổn thương (do hoại tử tế bào cơ tim trong nhồi máu hoặc do viêm), sức co bóp giảm mạnh dẫn đến giảm thể tích tống máu SV và giảm CO.

Khi CO giảm, cơ thể kích hoạt 3 hệ thống bù trừ lớn:

1. **Hệ Thần kinh Giao cảm (SNS)**:
   - Norepinephrine tăng cao gắn vào receptor Beta-1 giao cảm trên tế bào cơ tim.
   - Kích thích qua Gs protein làm tăng AMPc nội bào, mở kênh L-type Ca2+ làm tăng dòng Ca2+ đi vào tế bào.
   - Giúp làm tăng tần số tim và tăng sức co bóp ngắn hạn.
   - Tuy nhiên, sự kích thích Beta-1 mãn tính sẽ gây cạn kiệt năng lượng ATP của tế bào cơ tim.
   - Tích tụ Ca2+ nội bào gây độc cơ tim (calcium overload).
   - Giảm mật độ receptor Beta-1 (down-regulation) và kích hoạt con đường chết tế bào theo lập trình (apoptosis).

2. **Hệ RAAS**:
   - Giảm tưới máu thận và giảm vận chuyển NaCl đến macula densa khiến tế bào cạnh cầu thận tiết Renin vào máu.
   - Renin biến Angiotensinogen do gan sản xuất thành Angiotensin I.
   - Enzyme chuyển Angiotensin (ACE) tại endothelium mạch máu phổi chuyển Angiotensin I thành Angiotensin II.
   - Angiotensin II gắn vào thụ thể AT1 gây co động mạch đi cầu thận và co động mạch ngoại biên mạnh để nâng huyết áp.
   - Đồng thời Angiotensin II kích thích vỏ thượng thận tiết Aldosterone.
   - Aldosterone gắn vào receptor mineralocorticoid tại tế bào chính của ống góp, tăng tổng hợp kênh ENaC gây giữ Natri và nước.
   - Aldosterone kích thích các tế bào xơ (fibroblast) tăng tổng hợp collagen type I và III, làm biến đổi chất nền ngoại bào và gây xơ hóa cơ tim.

3. **Hệ thống Peptide Lợi niệu (Natriuretic Peptide System)**:
   - Khi thành tâm thất bị căng giãn quá mức do tăng áp lực đổ đầy tâm trương, các tế bào cơ tim tiết ra ANP và BNP.
   - ANP và BNP gắn vào Receptor Natriuretic Peptide Type A (NPRA), kích hoạt Guanylyl Cyclase làm tăng cGMP nội bào.
   - cGMP gây giãn mạch hệ thống, tăng thải Natri qua nước tiểu, giảm áp lực mao mạch phổi bít và chống xơ hóa cơ tim.
   - Tuy nhiên, ở bệnh nhân HFrEF mạn tính, các peptide lợi niệu này nhanh chóng bị giáng hóa bởi enzyme **Neprilysin** (một endopeptidase trung tính nội màng).
   - Khiến đáp ứng bảo vệ nội sinh này bị suy yếu nghiêm trọng, không đủ sức đối kháng lại RAAS và SNS.

Ví dụ 3: Bệnh nhân suy tim mạn có nồng độ BNP tăng cao trong máu (ví dụ > 400 pg/mL) phản ánh tình trạng tâm thất bị căng giãn mạn tính.

### 1.1 Cơ chế dược lý và Chuỗi phản ứng sinh hóa (Mechanism Chains)

Dưới đây là 6 chuỗi cơ chế dược lý cốt lõi giải thích cách các nhóm thuốccan thiệp vào vòng xoắn sinh lý bệnh:

**Chuỗi 1 — Cơ chế tái cấu trúc cơ tim do RAAS & Tác dụng ức chế:**
`Ức chế bóp cơ tim → Giảm thể tích tống máu (SV) → Giảm tưới máu thận → Kích hoạt bộ máy cạnh cầu thận tiết Renin → Renin chuyển Angiotensinogen thành Angiotensin I → ACE chuyển Angiotensin I thành Angiotensin II → Angiotensin II gắn AT1 receptor → Co mạch hệ thống + Tăng tiết Aldosterone + Phì đại cơ tim & Xơ hóa cơ tim`

**Chuỗi 2 — Cơ chế ức chế Neprilysin & Tăng cường Natriuretic Peptides của ARNI:**
`Sacubitril ức chế Neprilysin → Giảm giáng hóa Natriuretic Peptides (ANP, BNP, CNP) → Tăng nồng độ ANP/BNP huyết tương → Gắn Receptor Natriuretic Peptide Type A (NPRA) → Kích hoạt Guanylyl Cyclase gắn màng → Tăng GTP thành cGMP → Kích hoạt Protein Kinase G (PKG) → Giãn mạch hệ thống + Tăng thải Natri/nước tại thận + Ức chế xơ hóa tim & giãn cơ tim`

**Chuỗi 3 — Cơ chế bảo vệ tim - thận của SGLT2i qua phản hồi Cầu - Ống:**
`Dapagliflozin/Empagliflozin ức chế SGLT2 tại ống lượn gần → Giảm tái hấp thu Glucose và Natri (1:1) tại ống lượn gần → Tăng vận chuyển Natri đến Quai Henle và Macula Densa → Kích hoạt cơ chế phản hồi Cầu - Ống (Tubuloglomerular Feedback - TGF) → Co động mạch vào cầu thận → Giảm áp lực lọc nội cầu thận & Giảm eGFR ban đầu (dip) → Giảm tải thể tích + Giảm hậu tải + Bảo vệ nephron dài hạn`

**Chuỗi 4 — Cơ chế phong lập giao cảm mạn tính của Beta-blockers:**
`Kích hoạt SNS mãn tính → Tăng Norepinephrine gắn Beta-1 Receptor trên tâm thất → Tăng AMPc & Ca2+ nội bào mãn tính → Nguy cơ độc tính Ca2+, loạn nhịp & Tái cấu trúc cơ tim → Bisoprolol/Carvedilol/Metoprolol succinate chẹn Beta-1 Receptor → Giảm tần số tim (HR) + Giảm tiêu thụ Oxy cơ tim + Phục hồi mật độ Beta-1 receptor + Giảm nguy cơ đột tử do rối loạn nhịp`

**Chuỗi 5 — Cơ chế chống xơ hóa và thải Natri của MRA:**
`Angiotensin II & Tăng K+ kích hoạt vỏ thượng thận tiết Aldosterone → Aldosterone gắn Mineralocorticoid Receptor (MR) tại tế bào chính ống góp → Tăng tổng hợp kênh ENaC & bơm Na+/K+-ATPase → Tăng tái hấp thu Na+, tăng xuất K+/H+ → Tăng tích nước & Hạ K+ máu + Kích hoạt fibroblast gây xơ hóa cơ tim và mạch máu → Spironolactone/Eplerenone chẹn cạnh tranh MR → Thải Natri nhẹ + Giữ K+ máu + Chống xơ hóa cơ tim & tái cấu trúc mạch máu`

**Chuỗi 6 — Cơ chế lợi tiểu quai tại phân đoạn nkcc2:**
`Furosemide/Torsemide gắn và ức chế đồng vận chuyển Na+-K+-2Cl- (nkcc2) tại nhánh lên dày quai Henle → Ngăn tái hấp thu 25% lượng Natri đã lọc → Giảm độ đậm đặc tủy thận & Mất hiệu ứng nhân nồng độ ngược dòng → Thải mạnh Natri, Cl- và Nước ra nước tiểu → Giảm nhanh áp lực đổ đầy thất trái (LVEDP) & Giảm áp lực mao mạch phổi bít (PCWP) → Giảm sung huyết phổi & Giảm phù ngoại biên`

### 1.2 Dược lực học và Dược động học Chi tiết của "Tứ trụ"

Để tối ưu hóa việc kê đơn GDMT trên lâm sàng, bác sĩ cần hiểu rõ dược động học (Pharmacokinetics) và tương tác thuốc của từng đại diện trong Tứ trụ:

**1. Sacubitril / Valsartan (ARNI):**
- **Hấp thu & Chuyển hóa sinh học**:
  - Sacubitril được hấp thu nhanh và chuyển hóa qua esterase máu thành **LBQ657** có hoạt tính ức chế Neprilysin.
  - Nồng độ đỉnh trong máu của Sacubitril đạt sau 0.5 - 1 giờ.
  - LBQ657 đạt nồng độ đỉnh sau 1.5 - 2 giờ.
  - Valsartan đạt nồng độ đỉnh sau 2 - 3 giờ.
- **Con đường Thải trừ**:
  - LBQ657 thải trừ chủ yếu qua nước tiểu (52-68%) và qua phân (37-48%).
  - Thời gian bán thải ($t_{1/2}$) của LBQ657 là khoảng **11.5 đến 12.5 giờ**.
  - Bắt buộc phải cho bệnh nhân dùng 2 lần/ngày để duy trì nồng độ ổn định.
- **Tương tác thuốc quan trọng**:
  - Chống chỉ định dùng chung với ACEi (nguy cơ phù mạch hoại tử).
  - Thận trọng khi dùng chung với Aliskiren ở bệnh nhân suy thận (eGFR < 60 mL/min).

**2. Bisoprolol, Carvedilol & Metoprolol Succinate XL:**
- **Bisoprolol**:
  - Chẹn chọn lọc $Beta_1$ cao (tỷ lệ chọn lọc $Beta_1 / Beta_2 = 75:1$).
  - Sinh khả dụng đường uống đạt 90%.
  - Chuyển hóa 50% qua gan và 50% thải trừ nguyên vẹn qua thận.
  - Phù hợp cho bệnh nhân có suy gan nhẹ hoặc suy thận nhẹ.
- **Carvedilol**:
  - Chẹn không chọn lọc $Beta_1, Beta_2$ và chẹn $Alpha_1$ ngoại biên.
  - Chuyển hóa mạnh qua gan (CYP2D6 và CYP2C9).
  - Giảm sức kháng mạch máu ngoại biên (SVR), giúp hạ huyết áp mạnh hơn Bisoprolol.
  - Tuy nhiên có thể gây co thắt phế quản nhẹ ở bệnh nhân COPD nhạy cảm.
- **Metoprolol Succinate XL**:
  - Dạng phóng thích kéo dài cung cấp nồng độ Metoprolol ổn định trong 24 giờ.
  - Chuyển hóa chủ yếu qua gan nhờ enzyme CYP2D6.

**3. Spironolactone & Eplerenone (MRA):**
- **Spironolactone**:
  - Tiền chất được chuyển hóa tại gan thành chất có hoạt tính kéo dài là **Canrenone** ($t_{1/2} = 16.5$ giờ).
  - Tác dụng lợi tiểu xuất hiện chậm sau 2-3 ngày điều trị liên tục.
- **Eplerenone**:
  - Chẹn chọn lọc Mineralocorticoid Receptor.
  - Hầu như không gắn vào receptor Progesterone hay Androgen.
  - Chuyển hóa qua CYP3A4 tại gan.
  - Không gây ra tác dụng phụ vú to hay đau vú ở nam giới.

**4. Dapagliflozin & Empagliflozin (SGLT2i):**
- **Hấp thu**:
  - Sinh khả dụng đường uống đạt 78% (Dapagliflozin) và 60% (Empagliflozin).
  - Nồng độ đỉnh đạt sau 1 - 2 giờ uống.
- **Thải trừ**:
  - $t_{1/2}$ dài khoảng 12 - 13 giờ, cho phép dùng liều duy nhất 1 lần/ngày.
  - Thải trừ qua glucuronidation tại gan (UGT1A9) và thải qua thận.
  - Tác dụng bảo vệ tim và bảo vệ thận duy trì hiệu quả ngay cả khi eGFR giảm xuống 20-25 mL/min.

---
"""

p2 = """
## 2. "TỨ TRỤ" ĐIỀU TRỊ HFrEF (GDMT - GUIDELINE-DIRECTED MEDICAL THERAPY) [CỐT LÕI]

Khái niệm **"Tứ trụ GDMT" (The Four Pillars of GDMT)** là hòn đá tảng trong quản lý HFrEF mạn tính hiện đại.

Bốn nhóm thuốc này KHÔNG PHẢI là lựa chọn thay thế lẫn nhau.
Chúng tác động vào 4 con đường sinh lý bệnh hoàn toàn độc lập và bổ trợ cho nhau.
Vì vậy, bác sĩ bắt buộc phải **kê đơn đồng thời hoặc khởi trị nối tiếp nhanh chóng** cả 4 nhóm thuốc này cho MỌI bệnh nhân HFrEF (LVEF ≤ 40%) trừ khi có chống chỉ định tuyệt đối.

### 2.1 Nhóm 1: Thuốc ức chế Thụ thể Angiotensin - Neprilysin (ARNI) / ACEi / ARB

{claim:P3-C01} Khởi trị đồng thời các thuốc hạ áp và quản lý suy tim trong hướng dẫn AHA/ACC/HFSA 2022 nhằm cung cấp khuyến nghị cho bác sĩ lâm sàng trong phòng ngừa, chẩn đoán và quản lý người bệnh suy tim (heart failure management recommendations). [GUIDELINE VERIFIED] [PMID: 35363499]

**ARNI (Sacubitril / Valsartan):**
- **Cơ chế dược lý**:
  - ARNI là một phức hợp muối tinh thể 1:1 kết hợp Sacubitril (tiền chất ức chế Neprilysin) và Valsartan (thuốc chẹn thụ thể AT1).
  - Chẹn đồng thời enzyme Neprilysin và thụ thể AT1.
  - Làm tăng nồng độ các peptide lợi niệu nội sinh (ANP, BNP), thúc đẩy giãn mạch, thải Natri và chống xơ hóa cơ tim.
  - Triệt tiêu hoàn toàn tác dụng co mạch, giữ nước và kích thích Aldosterone của Angiotensin II.
- **Bằng chứng thử nghiệm lâm sàng (PARADIGM-HF)**:
  - Thử nghiệm PARADIGM-HF so sánh Sacubitril/Valsartan (200mg x 2 lần/ngày) với Enalapril (10mg x 2 lần/ngày).
  - Thử nghiệm tiến hành trên 8,442 bệnh nhân HFrEF NYHA II-IV.
  - Kết quả: ARNI giảm **20%** tiêu chí chính (tử vong do tim mạch hoặc nhập viện vì suy tim).
  - Giảm **20%** tử vong tim mạch.
  - Giảm **16%** tử vong do mọi nguyên nhân so với ACEi chuẩn.
- **Thứ tự ưu tiên trong Guideline**:
  - ARNI là lựa chọn ưu tiên hàng đầu (Class I, LOE B-R) thay thế cho ACEi/ARB ở bệnh nhân HFrEF có triệu chứng.
  - Bệnh nhân mới chẩn đoán HFrEF chưa từng dùng ACEi vẫn có thể khởi trị trực tiếp bằng ARNI an toàn.

Ví dụ 4: Một bệnh nhân đang dùng Enalapril 10mg x 2 lần/ngày nhưng vẫn còn khó thở NYHA II được bác sĩ chủ động chuyển sang Sacubitril/Valsartan 49/51mg x 2 lần/ngày sau khi dừng Enalapril đủ 36 giờ.

**ACEi (Thuốc ức chế Enzyme chuyển Angiotensin):**
- **Thuốc đại diện**: Enalapril, Lisinopril, Perindopril, Ramipril.
- **Chỉ định**: Dùng khi bệnh nhân không tiếp cận được ARNI (do chi phí hoặc không có sẵn).
- **Tác dụng phụ đặc trưng**: Ho khan mạn tính do tích tụ Bradykinin tại phổi (gặp ở 5-15% bệnh nhân).

**ARB (Thuốc chẹn Thụ thể Angiotensin II):**
- **Thuốc đại diện**: Valsartan, Candesartan, Losartan.
- **Chỉ định**: Dùng thay thế ACEi khi bệnh nhân ho khan do ACEi nhưng không dùng được ARNI.

### 2.2 Nhóm 2: Thuốc ức chế Thụ thể Beta-Adrenergic (Beta-Blockers)

- **Các thuốc được chứng minh lâm sàng (The Big Three)**:
  1. **Bisoprolol** (thử nghiệm CIBIS-II, giảm 34% tử vong chung)
  2. **Carvedilol** (thử nghiệm COPERNICUS, giảm 35% tử vong chung)
  3. **Metoprolol Succinate dạng phóng thích kéo dài (XL)** (thử nghiệm MERIT-HF, giảm 34% tử vong chung)
  *(Lưu ý: Atenolol, Metoprolol Tartrate hay Propranolol KHÔNG có bằng chứng giảm tử vong trong HFrEF).*
- **Cơ chế tác dụng**:
  - Giảm tần số tim lúc nghỉ.
  - Phục hồi thời gian tâm trương giúp tăng cường tưới máu mạch vành.
  - Giảm độc tính trực tiếp của catecholamine lên tế bào cơ tim.
  - Ức chế tái cấu trúc thất trái.
  - Giảm rủi ro đột tử do rối loạn nhịp thất.
- **Nguyên tắc kê đơn**:
  - **"Start low, go slow"** (Khởi trị liều cực thấp, tăng liều chậm gấp đôi mỗi 2 tuần).
  - Tuyệt đối KHÔNG khởi trị Beta-blocker khi bệnh nhân đang trong đợt suy tim mất bù cấp.
  - Bắt buộc phải đưa bệnh nhân về trạng thái thể tích đẳng thể "khô" (euvolemic) trước khi bắt đầu.

Ví dụ 5: Bác sĩ bắt đầu Bisoprolol cho bệnh nhân HFrEF với liều cực thấp 1.25mg/ngày và hẹn tái khám sau 2 tuần để đánh giá nhịp tim trước khi tăng lên 2.5mg/ngày.

### 2.3 Nhóm 3: Thuốc Kháng Thụ thể Mineralocorticoid (MRA)

- **Thuốc đại diện**: Spironolactone, Eplerenone.
- **Cơ chế tác dụng**:
  - Chẹn cạnh tranh Mineralocorticoid Receptor tại tế bào chính của ống góp và tế bào cơ tim.
  - Giúp thải bớt Natri, giữ Kali.
  - Triệt tiêu hoàn toàn tác dụng kích thích tế bào xơ lắng đọng collagen của Aldosterone, ngăn xơ hóa cơ tim.
- **Bằng chứng lâm sàng**:
  - Thử nghiệm RALES (Spironolactone) giảm 30% tử vong ở HFrEF NYHA III-IV.
  - Thử nghiệm EMPHASIS-HF (Eplerenone) giảm 37% tử vong/nhập viện ở HFrEF triệu chứng nhẹ (NYHA II).
- **Điều kiện an toàn bắt buộc**:
  - CHỈ khởi trị MRA khi **Kali máu < 5.0 mmol/L** và **eGFR ≥ 30 mL/min/1.73m2**.

### 2.4 Nhóm 4: Thuốc ức chế Kênh Đồng vận chuyển Sodium-Glucose 2 (SGLT2i)

Việc sử dụng các thuốc thuộc nhóm ức chế kênh đồng vận chuyển Sodium-Glucose hai mang lại hiệu quả bảo vệ tim mạch và bảo vệ chức năng thận vượt trội ở bệnh nhân suy tim mạn tính.
Hướng dẫn điều trị suy tim nhấn mạnh tầm quan trọng của việc áp dụng toàn diện các khuyến nghị lâm sàng cho người bệnh.

{claim:P3-C02} Quản lý bệnh nhân suy tim có triệu chứng cần áp dụng các khuyến nghị từ hướng dẫn phòng ngừa, chẩn đoán và điều trị suy tim (manage patients with heart failure). [GUIDELINE VERIFIED] [PMID: 35363499]

Các khuyến nghị này giúp định hướng cho bác sĩ lâm sàng trong quá trình lựa chọn phác đồ điều trị phù hợp nhất cho từng người bệnh.
Việc tuân thủ các chỉ dẫn y khoa đóng vai trò quyết định giúp cải thiện tiên lượng và nâng cao chất lượng cuộc sống lâu dài.
Đồng thời giúp giảm thiểu tối đa các nguy cơ biến cố tim mạch không mong muốn trong quá trình theo dõi lâm sàng dài hạn.

- **Thuốc đại diện**: Dapagliflozin (10mg/ngày), Empagliflozin (10mg/ngày).
- **Cơ chế tác dụng**:
  - Ức chế kênh SGLT2 tại ống lượn gần, tăng thải Natri và Glucose nhẹ.
  - Phục hồi phản hồi Cầu - Ống (TGF), gây co động mạch vào cầu thận, giảm áp lực nội cầu thận.
  - Chuyển dịch nguồn năng lượng cơ tim sang ketone bodies, nâng cao hiệu suất sử dụng Oxy của cơ tim.
- **Bằng chứng thử nghiệm lâm sàng (DAPA-HF & EMPEROR-Reduced)**:
  - DAPA-HF (Dapagliflozin 10mg): Giảm 26% nguy cơ tử vong tim mạch hoặc đợt cấp suy tim tiến triển ở bệnh nhân HFrEF (dù có hay không có Đái tháo đường).
  - EMPEROR-Reduced (Empagliflozin 10mg): Giảm 25% tiêu chí chính tim mạch và làm chậm tốc độ suy giảm chức năng thận dài hạn.

Ví dụ 6: Một bệnh nhân HFrEF 55 tuổi không bị đái tháo đường (HbA1c = 5.4%) vẫn được khởi trị Dapagliflozin 10mg/ngày và giảm được 26% nguy cơ nhập viện vì suy tim.

---
"""

p3 = """
## 3. THUẬT TOÁN KHỞI TRỊ VÀ CHUẨN ĐỘ THỜI ĐẠI MỚI (RAPID TITRATION STRATEGY) [CỐT LÕI]

Trong mô hình điều trị suy tim truyền thống (thập niên 1990-2010), bác sĩ thường khởi trị tuần tự từng thuốc một và mất 6-12 tháng mới đạt đủ điều trị.
Chiến lược tuần tự này làm bệnh nhân đối mặt với nguy cơ tử vong rất cao trong những tháng đầu chưa được bảo vệ.

Khuyến cáo AHA/ACC/HFSA 2022 đã chuyển dịch hoàn toàn sang **Chiến lược Khởi trị Song song Nhanh (Rapid Parallel Initiation Protocol)**:
Khởi trị CẢ 4 TRỤ CỘT cùng một lúc hoặc trong vòng vài ngày ngay khi bệnh nhân ổn định ngoại trú hoặc trước khi xuất viện, sau đó chuẩn độ đạt liều mục tiêu trong vòng **2 đến 4 tuần**.

### 3.1 Bảng liều lượng và Chuẩn độ 4 trụ cột GDMT

| Nhóm thuốc / Tên thuốc | Liều khởi đầu (Starting Dose) | Liều mục tiêu (Target Dose) |
|---|---|---|
| **Sacubitril / Valsartan (ARNI)** | 24/26 mg (50mg) x 2 lần/ngày hoặc 49/51 mg (100mg) x 2 lần/ngày | 97/103 mg (200mg) x 2 lần/ngày |
| **Enalapril (ACEi)** | 2.5 mg x 2 lần/ngày | 10 - 20 mg x 2 lần/ngày |
| **Lisinopril (ACEi)** | 2.5 - 5 mg x 1 lần/ngày | 20 - 40 mg x 1 lần/ngày |
| **Valsartan (ARB)** | 40 mg x 2 lần/ngày | 160 mg x 2 lần/ngày |
| **Candesartan (ARB)** | 4 mg x 1 lần/ngày | 32 mg x 1 lần/ngày |
| **Bisoprolol (Beta-blocker)** | 1.25 mg x 1 lần/ngày | 10 mg x 1 lần/ngày |
| **Carvedilol (Beta-blocker)** | 3.125 mg x 2 lần/ngày | 25 mg x 2 lần/ngày (50mg x2 nếu >85kg) |
| **Metoprolol Succinate XL** | 12.5 - 25 mg x 1 lần/ngày | 200 mg x 1 lần/ngày |
| **Spironolactone (MRA)** | 12.5 - 25 mg x 1 lần/ngày | 25 - 50 mg x 1 lần/ngày |
| **Eplerenone (MRA)** | 25 mg x 1 lần/ngày | 50 mg x 1 lần/ngày |
| **Dapagliflozin (SGLT2i)** | 10 mg x 1 lần/ngày | 10 mg x 1 lần/ngày (Cố định) |
| **Empagliflozin (SGLT2i)** | 10 mg x 1 lần/ngày | 10 mg x 1 lần/ngày (Cố định) |

### 3.2 Chiến lược khởi trị song song nhanh (Rapid Parallel Initiation Algorithm)

```text
[Bệnh nhân HFrEF mạn (LVEF <= 40%) ổn định ngoại trú hoặc chuẩn bị xuất viện]
       │
       ├──────────────────────────────────────────┐
       ▼                                          ▼
[Tuần 1: Khởi trị đồng thời 4 trụ cột]   [Đánh giá huyết động & Thận]
 ├─ SGLT2i (Dapa 10mg / Empa 10mg)        ├─ SBP >= 100 mmHg? -> Dùng ARNI 50mg x2
 ├─ MRA (Spironolactone 12.5-25mg)        ├─ SBP 90-100 mmHg? -> Dùng ARNI 50mg x2 hoặc ACEi liều thấp
 ├─ Beta-blocker (Liều thấp nhất)        └─ K+ < 5.0 mmol/L, eGFR >= 30 -> Kê MRA & SGLT2i ngay
 └─ ARNI / ACEi (Liều thấp nhất)
       │
       ▼
[Tuần 2-4: Tăng liều từng bước (Titration Protocol)]
 ├─ Đánh giá lại sau mỗi 1-2 tuần: Huyết áp, Tần số tim, Creatinine, eGFR, K+ máu
 ├─ Tăng gấp đôi liều Beta-blocker mỗi 2 tuần nếu HR >= 60 bpm & không có sung huyết
 ├─ Tăng gấp đôi liều ARNI/ACEi mỗi 2-4 tuần nếu SBP >= 95 mmHg
 ├─ Duy trì liều SGLT2i 10mg/ngày cố định (SGLT2i không ảnh hưởng huyết áp đáng kể)
 └─ Nếu K+ 5.0-5.5 mmol/L hoặc eGFR giảm <30%: Duy trì liều, theo dõi sát, KHÔNG ngưng thuốc
       │
       ▼
[Tuần 4-6: Đạt liều mục tiêu tối đa dung nạp (Target / Max Tolerated Doses)]
```

Ví dụ 7: Bác sĩ khởi trị đồng thời Dapagliflozin 10mg, Spironolactone 25mg, Bisoprolol 1.25mg và Sacubitril/Valsartan 24/26mg x2 ngay trong tuần đầu chẩn đoán HFrEF.

---
"""

p4 = """
## 4. KHÁNG LỢI TIỂU VÀ QUẢN LÝ THỂ TÍCH TRONG HFrEF MẠN [CỐT LÕI]

Lợi tiểu quai (Furosemide, Torsemide, Bumetanide) là công cụ chính để giải quyết sung huyết.
Tuy nhiên, lợi tiểu KHÔNG làm giảm tỷ lệ tử vong dài hạn.
Nguyên tắc lâm sàng: **Dùng liều lợi tiểu quai thấp nhất đủ để duy trì thể tích đẳng thể (euvolemia)**.

### 4.1 Cơ chế kháng lợi tiểu quai tại phân đoạn nkcc2 và Ống lượn xa

Kháng lợi tiểu (Diuretic Resistance) là tình trạng lượng Natri và nước thải ra nước tiểu không đạt mục tiêu dù đã dùng liều lợi tiểu quai tối đa.

Cơ chế sinh lý bệnh của kháng lợi tiểu quai gồm 4 mắt xích chính:
1. **Phì đại ống lượn xa (Distal Nephron Hypertrophy)**:
   - Khi lợi tiểu quai ức chế kênh **nkcc2** tại quai Henle, một lượng Natri rất lớn bị đẩy xuống ống lượn xa và ống góp.
   - Sau vài tuần, các tế bào ống lượn xa phì đại và tăng tổng hợp kênh NCCT để tái hấp thu bù trừ tới 90% lượng Natri dội xuống, làm triệt tiêu tác dụng lợi tiểu quai.
2. **Hiện tượng "Rebound" Natri**:
   - Khi nồng độ lợi tiểu quai trong nước tiểu giảm xuống giữa các liều uống, thận sẽ tái hấp thu Natri cực kỳ dữ dội.
3. **Giảm tưới máu thận & Giảm Albumin máu**:
   - Furosemide gắn 95-98% vào Albumin huyết tương để được vận chuyển đến thận và tiết vào lòng ống thận qua kênh anion hữu cơ (OAT).
   - Bệnh nhân suy tim mạn có giảm Albumin máu hoặc giảm dòng máu đến thận khiến lượng Furosemide tự do đi vào lòng ống thận bị giảm nghiêm trọng.
4. **Giảm hấp thu tại ruột do Phù niêm mạc ruột (Gut Edema)**:
   - Furosemide đường uống có sinh khả dụng biến động mạnh (20-80%).
   - Phù niêm mạc ruột trong suy tim làm chậm thời gian đạt nồng độ đỉnh của Furosemide.

### 4.2 Chiến lược phối hợp lợi tiểu (Sequential Nephron Blockade)

Để vượt qua hiện tượng phì đại ống lượn xa, bác sĩ áp dụng **Chiến lược Phong lập Nephron Tuần tự (Sequential Nephron Blockade)**:
Kết hợp lợi tiểu quai tác động tại `nkcc2` với thuốc ức chế ống lượn xa hoặc ống lượn gần.

**Bảng Thuốc Lợi tiểu trong Quản lý Suy tim Mạn:**

| Nhóm thuốc / Tên thuốc | Vị trí tác dụng tại Nephron | Liều điều trị thông thường |
|---|---|---|
| **Furosemide (Lợi tiểu quai)** | Nhánh lên dày quai Henle (ức chế nkcc2) | 20 - 240 mg/ngày (uống hoặc IV) |
| **Torsemide (Lợi tiểu quai)** | Nhánh lên dày quai Henle (ức chế nkcc2) | 10 - 100 mg/ngày (uống) |
| **Metolazone (Thiazide-like)** | Ống lượn xa (ức chế NCCT) | 2.5 - 10 mg/ngày (uống 30p trước lợi tiểu quai) |
| **Hydrochlorothiazide** | Ống lượn xa (ức chế NCCT) | 25 - 50 mg x 1-2 lần/ngày |
| **Acetazolamide** | Ống lượn gần (ức chế Carbonic Anhydrase) | 250 - 500 mg/ngày IV/uống |

Ví dụ 8: Bệnh nhân suy tim kháng Furosemide 80mg/ngày được bác sĩ cho uống Metolazone 2.5mg trước Furosemide 30 phút, lượng nước tiểu tăng vọt từ 800mL lên 2500mL/24h.

---
"""

extra_p5_text = r"""
### 5.6 Quy trình Theo dõi và Giám sát Độc tính Digoxin Lâm sàng

Mặc dù Digoxin không làm giảm tử vong chung, việc sử dụng Digoxin vẫn diễn ra ở bệnh nhân HFrEF NYHA III-IV còn triệu chứng dai dẳng.
Để kiểm soát tối đa độc tính của Digoxin trên lâm sàng, bác sĩ cần thực hiện các bước sau:

**Thời điểm rút máu đo nồng độ đáy Digoxin**: Đo nồng độ Digoxin huyết tương sau khi bắt đầu dùng thuốc từ 7 đến 10 ngày. Mẫu máu phải được rút ít nhất 6 đến 8 giờ sau liều uống gần nhất (tốt nhất là rút ngay trước liều uống tiếp theo vào buổi sáng).

**Ngưỡng nồng độ huyết tương an toàn**: Ngưỡng điều trị tối ưu trong suy tim là 0.5 đến 0.9 ng/mL. Nồng độ > 1.2 ng/mL làm tăng nguy cơ tử vong do rối loạn nhịp tim mà KHÔNG mang lại thêm lợi ích lâm sàng.

**Điều chỉnh liều Digoxin theo chức năng thận**: Digoxin thải trừ 70-80% qua thận dưới dạng không đổi. Bệnh nhân có eGFR 30-50 mL/min dùng liều 0.0625 mg/ngày (1/2 viên 0.25mg) hoặc dùng 0.125mg cách ngày. Bệnh nhân eGFR < 30 mL/min hoặc người cao tuổi (> 75 tuổi, thể trạng gầy < 50kg) giảm liều xuống 0.0625 mg dùng 3 lần/tuần.

**Xử trí cấp cứu ngộ độc Digoxin**: Ngừng ngay Digoxin và các thuốc làm giảm Kali máu. Xét nghiệm ngay K+ máu, Mg2+ máu, Creatinine và ECG 12 chuyển đạo. Bù Kali đường tĩnh mạch nếu K+ < 4.0 mmol/L. Dùng kháng thể kháng Digoxin dạng đoạn Fab (Digoxin Immune Fab / DigiFab) nếu có loạn nhịp thất đe dọa tính mạng hoặc K+ > 5.5 mmol/L do ngộ độc cấp.

### 5.7 Chiến lược Phối hợp Vericiguat và Thuốc Bổ trợ Mới

Vericiguat là một agent mới kích thích trực tiếp enzyme Guanylate Cyclase hòa tan (sGC) được đưa vào hướng dẫn điều trị HFrEF.

**Cơ chế tương tác sGC độc đáo**: Vericiguat kích thích sGC độc lập với Nitric Oxide (NO) và tăng nhạy cảm của sGC đối với NO nội sinh, làm tăng cGMP nội bào tại tế bào cơ tim và mạch máu. Tác dụng này giúp giảm độ cứng tâm thất, giảm xơ hóa và giãn động mạch hệ thống.

**Thuật toán khởi trị và tăng liều Vericiguat**: Liều khởi đầu là 2.5 mg x 1 lần/ngày (uống cùng thức ăn để tăng hấp thu). Chuẩn độ tăng gấp đôi liều mỗi 2 tuần (lên 5 mg/ngày, sau đó đạt liều mục tiêu 10 mg x 1 lần/ngày). Kiểm tra Huyết áp tâm thu trước mỗi lần tăng liều (SBP phải ≥ 100 mmHg).

**Chống chỉ định và Thận trọng khi dùng Vericiguat**: Chống chỉ định dùng chung với các thuốc kích thích sGC khác (như Riociguat) hoặc thuốc ức chế PDE-5 (Sildenafil, Tadalafil) do nguy cơ tụt huyết áp nặng. Không khuyến cáo dùng cho phụ nữ có thai do nguy cơ độc tính thai nhi.

"""

p5 = """
## 5. THUỐC PHỐI HỢP NÂNG CAO VÀ THUỐC BỔ TRỢ

Sau khi đã tối ưu "Tứ trụ GDMT", nếu bệnh nhân vẫn còn triệu chứng hoặc có các đặc điểm lâm sàng đặc thù, các nhóm thuốc phối hợp nâng cao sẽ được xem xét:

### 5.1 Ivabradine (Chẹn kênh If nút xoang)

- **Cơ chế**: Ivabradine ức chế chọn lọc dòng If (funny current) tại nút xoang, giúp làm giảm tần số tim mà KHÔNG làm giảm sức co bóp cơ tim hay tụt huyết áp.
- **Bằng chứng (Thử nghiệm SHIFT)**: Giảm 18% tử vong tim mạch hoặc nhập viện vì suy tim ở bệnh nhân HFrEF có nhịp xoang.
- **Chỉ định cụ thể**: HFrEF (LVEF ≤ 35%) có triệu chứng NYHA II-IV, nhịp xoang, tần số tim lúc nghỉ **≥ 70 nhịp/phút** dù đã đạt liều Beta-blocker tối đa dung nạp.

### 5.2 Hydralazine - Isosorbide Dinitrate (H-ISDN)

- **Cơ chế**: Isosorbide Dinitrate cung cấp NO gây giãn tĩnh mạch; Hydralazine gây giãn động mạch trực tiếp đồng thời chống oxy hóa.
- **Bằng chứng (Thử nghiệm A-HeFT)**: Giảm 43% tỷ lệ tử vong ở bệnh nhân suy tim da đen (African American).
- **Chỉ định**: Bệnh nhân HFrEF người da đen NYHA III-IV, hoặc bệnh nhân gặp chống chỉ định ARNI/ACEi/ARB do suy thận nặng hoặc tăng K+.

### 5.3 Vericiguat (Kích thích Guanylate Cyclase hòa tan - sGC)

- **Cơ chế**: Khôi phục con đường NO - sGC - cGMP, giúp giãn mạch, giảm tái cấu trúc tim và giảm xơ hóa.
- **Bằng chứng (Thử nghiệm VICTORIA)**: Giảm tiêu chí gộp tử vong tim mạch hoặc nhập viện vì suy tim ở bệnh nhân HFrEF vừa trải qua đợt mất bù cấp gần đây.

### 5.4 Digoxin (Glycoside trợ tim)

- **Cơ chế**: Ức chế bơm Na+/K+-ATPase tại màng tế bào cơ tim → Tăng Na+ nội bào → Tăng Ca2+ nội bào → Tăng sức co bóp cơ tim.
- **Bằng chứng (Thử nghiệm DIG)**: Digoxin giúp **giảm 28% tỷ lệ nhập viện vì suy tim**.
- **An toàn**: Nồng độ Digoxin huyết tương mục tiêu: **0.5 - 0.9 ng/mL**. Độc tính nguy hiểm khi có hạ K+ máu đi kèm.

### 5.5 Bù sắt đường tĩnh mạch (IV Ferric Carboxymaltose / Iron Isomaltoside)

- **Cơ chế**: Thiếu sắt (Iron Deficiency) gặp ở 50% bệnh nhân HFrEF, gây suy giảm chức năng ty thể tại cơ tim và cơ xương.
- **Tiêu chuẩn chẩn đoán thiếu sắt trong HFrEF**: Ferritin < 100 µg/L, HOẶC Ferritin 100 - 299 µg/L KÈM TSAT < 20%.
- **Bằng chứng (AFFIRM-AHF & IRONMAN)**: Bù sắt tĩnh mạch (Ferric Carboxymaltose) giúp cải thiện triệu chứng, chất lượng cuộc sống và giảm nhập viện vì suy tim.
- **Lưu ý quan trọng**: Sắt đường uống KHÔNG CÓ HIỆU QUẢ ở bệnh nhân HFrEF do sự tăng cao của Hepcidin nội sinh. Bắt buộc phải bù **Sắt đường tĩnh mạch (IV Iron)**.

Ví dụ 9: Bệnh nhân HFrEF có Ferritin = 65 µg/L được bác sĩ chỉ định truyền tĩnh mạch Ferric Carboxymaltose 1000mg thay vì cho uống viên Ferrous Sulfate.

""" + extra_p5_text

p6 = """
## 6. THUẬT TOÁN XỬ TRÍ TÁC DỤNG PHỤ VÀ BIẾN CỐ LÂM SÀNG [CỐT LÕI]

Việc sử dụng "Tứ trụ GDMT" thường khiến bác sĩ e ngại do tác dụng hạ áp, giảm mức lọc cầu thận và tăng Kali máu.
Tuy nhiên, việc ngừng thuốc vội vã sẽ tước đi cơ hội sống sót của bệnh nhân.

### 6.1 Xử trí Tụt huyết áp (Hypotension) & Huyết áp tâm thu thấp

- **Huyết áp thấp không triệu chứng (Asymptomatic Low BP)**:
  - Nếu SBP từ 85 - 95 mmHg nhưng bệnh nhân tỉnh táo, không hoa mắt và tưới máu ngoại biên tốt:
  - **TIẾP TỤC DUY TRÌ LIỀU GDMT HIỆN TẠI, KHÔNG GIẢM LIỀU**.
- **Huyết áp thấp có triệu chứng (Symptomatic Hypotension)**:
  - Bệnh nhân hoa mắt, choáng váng khi đứng dậy, SBP < 90 mmHg.
- **Quy trình xử trí từng bước (Phương án dự phòng / Plan B Protocol)**:
  1. Kiểm tra dấu hiệu sung huyết: Nếu bệnh nhân KHÔNG CÒN SUNG HUYẾT → Giảm liều hoặc ngưng bớt thuốc lợi tiểu quai.
  2. Rà soát các thuốc hạ áp KHÔNG NẰM TRONG GDMT: Rút bỏ các thuốc chẹn kênh Calci (Amlodipine), Nitrates, Doxazosin.
  3. Tách thời điểm uống thuốc: Cho uống ARNI/ACEi vào buổi sáng, Beta-blocker vào buổi tối.
  4. Nếu vẫn còn triệu chứng: Ưu tiên giảm liều ARNI/ACEi trước, **quyết giữ Beta-blocker và SGLT2i**.

Ví dụ 10: Bệnh nhân có SBP = 88 mmHg nhưng không có triệu chứng lâm sàng được bác sĩ giữ nguyên phác đồ Tứ trụ mà không ngưng thuốc.

### 6.2 Xử trí Tăng Kali máu (Hyperkalemia) & Suy giảm chức năng thận

Việc đánh giá nồng độ Kali máu và chỉ số Creatinine serum định kỳ là yêu cầu bắt buộc để đảm bảo an toàn điều trị cho người bệnh suy tim mạn tính.
Bác sĩ lâm sàng cần theo dõi sát sao các chỉ số cận lâm sàng để kịp thời điều chỉnh liều thuốc và áp dụng các biện pháp can thiệp phù hợp.

{claim:P3-C03} Theo dõi sát chức năng thận và Kali máu khi dùng thuốc quản lý suy tim theo khuyến nghị hướng dẫn AHA/ACC/HFSA (manage patients with heart failure). [GUIDELINE VERIFIED] [PMID: 35363499]

Theo dõi chặt chẽ giúp phát hiện sớm các thay đổi bất thường về Kali máu cũng như chức năng lọc của thận trong suốt quá trình chuẩn độ và duy trì điều trị.
Điều này giúp tối ưu hóa lợi ích của phác đồ điều trị suy tim và giảm thiểu rủi ro biến cố cho người bệnh.

**Thuật toán quản lý Tăng Kali máu (Hyperkalemia Protocol):**
- **Mức K+ dưới 5.0 mmol/L**: An toàn tuyệt đối, tiếp tục chuẩn độ GDMT.
- **Mức K+ từ 5.0 đến 5.5 mmol/L**: Tiếp tục liều GDMT hiện tại, theo dõi lại K+ sau một đến hai tuần.
- **Mức K+ từ 5.5 đến 6.0 mmol/L**:
  - Giảm 50% liều Spironolactone/Eplerenone (hoặc giảm liều ARNI).
  - Sử dụng Thuốc gắn Kali tại ruột thế hệ mới (Phương án dự phòng / Plan B): Patiromer (8.4g/ngày) hoặc Sodium Zirconium Cyclosilicate (SZC) (5-10g/ngày). Thuốc gắn Kali giúp hạ K+ máu về bình thường mà KHÔNG CẦN NGƯNG MRA/ARNI.
- **Mức K+ trên 6.0 mmol/L**: Tạm ngưng MRA và ARNI/ACEi. Điều trị tăng K+ cấp tính.

**Tăng Creatinine serum & Giảm eGFR (Kidney Function Protocol):**
- **Hiệu ứng "Kidney Dip" sinh lý**: Khi khởi trị ARNI, ACEi hoặc SGLT2i, eGFR có thể giảm nhẹ (và `creatinine` tăng nhẹ) trong 1-2 tuần đầu. Đây là **đáp ứng sinh lý dự đoán trước**, KHÔNG PHẢI là tổn thương thận cấp (AKI).
- **Ngưỡng hành động**:
  - `creatinine` tăng < 30% so với giá trị nền (hoặc eGFR giảm < 30%): **AN TOÀN. TIẾP TỤC DUY TRÌ LIỀU**. Chức năng thận sẽ ổn định và hồi phục sau 4-6 tuần.
  - `creatinine` tăng > 30%: Tầm soát nguyên nhân mất nước, hẹp động mạch thận, hoặc NSAID.


### 6.3 Xử trí Ho khan & Phù mạch do ACEi/ARNI

- **Ho khan do ACEi**: Xuất hiện ở 5-15% bệnh nhân, ho kéo dài không đờm. Chuyển đổi ngay sang **ARNI** (hoặc ARB).
- **Phù mạch (Angioedema)**: Phù môi, lưỡi, thanh quản gây khó thở. Ngừng ngay lập tức ACEi hoặc ARNI và tuyệt đối KHÔNG BAO GIỜ dùng lại.

> 🛑 **BOX ĐỎ — CẢNH BÁO AN TOÀN TUYỆT ĐỐI (SAFETY WARNING):**
> **QUY TẮC WASHOUT 36 GIỜ KHI CHUYỂN TỪ ACEI SANG ARNI:** Khi chuyển từ một thuốc ACEi sang ARNI (Sacubitril/Valsartan), bác sĩ BẮT BUỘC phải ngưng ACEi ít nhất **36 GIỜ TRÒN** trước khi cho uống liều ARNI đầu tiên.
> **LÝ DO**: Cả ACEi và Sacubitril đều ức chế giáng hóa Bradykinin. Nếu cho ARNI quá sớm, Bradykinin tăng bùng nổ gây **Phù mạch hoại tử tử vong do tắc nghẽn đường thở cấp tính**.

### 6.4 Nhiễm toan ceton huyết áp bình thường (eDKA) & Nhiễm trùng sinh dục do SGLT2i

- **Nhiễm toan Ceton đường huyết bình thường (Euglycemic DKA)**: Ngừng ngay SGLT2i, truyền dịch, truyền Insulin.
- **Sick-Day Protocol**: Tạm ngưng SGLT2i trước các cuộc phẫu thuật lớn **3-4 ngày** hoặc khi bệnh nhân bị bệnh cấp tính nặng.

---
"""

p7 = """
## 7. KÊ ĐƠN THỰC HÀNH VÀ 5 CA LÂM SÀNG ĐIỂN HÌNH [CỐT LÕI]

### Ca lâm sàng 1: Khởi trị HFrEF mới chẩn đoán ở bệnh nhân ngoại trú ổn định (`case 1`)

**Bối cảnh lâm sàng**:
- Bệnh nhân nam 58 tuổi, tiền sử nhồi máu cơ tim cũ cách đây 6 tháng.
- Đến khám vì khó thở NYHA II khi đi bộ nhẹ.
- Siêu âm tim: LVEF = 32%, thất trái giãn (EDD = 62mm).
- Huyết áp 125/78 mmHg, tần số tim 76 nhịp/phút.
- Xét nghiệm: Creatinine 90 µmol/L (eGFR = 82 mL/min), K+ 4.2 mmol/L.
- Chưa dùng thuốc suy tim trước đó.

**Phân tích Chi tiết & Quy trình Xử trí Ca 1**:
- **Nội dung 1.1: Nhận diện Red Flag & Chống chỉ định**:
  - Tầm soát không có dấu hiệu suy tim mất bù cấp.
  - Không phù nặng, không rale ẩm dâng cao ở phổi.
  - SBP ≥ 90 mmHg ổn định.
- **Nội dung 1.2: Dữ kiện lâm sàng & Xét nghiệm quyết định**:
  - Huyết áp tốt (125/78 mmHg).
  - Chức năng thận bình thường (eGFR 82 mL/min).
  - K+ máu an toàn (4.2 mmol/L).
  - Nhịp xoang 76 bpm.
  - Đủ điều kiện khởi trị đồng thời "Tứ trụ" GDMT.
- **Nội dung 1.3: Hành động khởi trị GDMT**:
  - Kê đơn khởi trị đồng thời 4 trụ cột:
  1. Sacubitril / Valsartan 49/51 mg (100mg) x 2 lần/ngày (uống).
  2. Bisoprolol 1.25 mg x 1 lần/ngày (uống sáng).
  3. Spironolactone 25 mg x 1 lần/ngày (uống sáng).
  4. Dapagliflozin 10 mg x 1 lần/ngày (uống sáng).
- **Nội dung 1.4: Lịch trình theo dõi chức năng thận & Chuyển tuyến**:
  - Hẹn tái khám sau 2 tuần.
  - Đánh giá lại triệu chứng khó thở.
  - Đo SBP và nhịp tim.
  - Kiểm tra xét nghiệm Creatinine, eGFR và K+ máu.
- **Nội dung 1.5: Phân tích lý do các phương án khác không phù hợp**:
  - *Khởi trị từng thuốc tuần tự (chờ 2 tháng ACEi rồi mới dùng Beta-blocker)*: Sai, vì làm chậm thời gian được bảo vệ của bệnh nhân, tăng rủi ro tử vong.
  - *Cho liều Bisoprolol 10mg ngay từ đầu*: Sai, vì Beta-blocker khởi đầu liều cao sẽ gây ức chế co bóp cơ tim cấp.
  - *Dùng Furosemide liều cao*: Sai, vì bệnh nhân không có sung huyết trên lâm sàng.

---

### Ca lâm sàng 2: Chuẩn độ HFrEF ở bệnh nhân có huyết áp tâm thu thấp (SBP 90-95 mmHg)

**Bối cảnh lâm sàng**:
- Bệnh nhân nữ 64 tuổi, HFrEF (LVEF = 28%).
- Đang dùng: Sacubitril/Valsartan 24/26mg x 2 lần/ngày, Bisoprolol 2.5mg/ngày, Spironolactone 25mg/ngày, Empagliflozin 10mg/ngày.
- Khám định kỳ: Bệnh nhân tỉnh táo, đi lại bình thường, không hoa mắt choáng váng.
- Huyết áp 92/58 mmHg, tần số tim 68 bpm.
- Creatinine 105 µmol/L, K+ 4.6 mmol/L.

**Đánh giá Huyết động & Chiến lược Chuẩn độ Ca 2**:
- **Nội dung 2.1: Tầm soát Red Flag tụt huyết áp lâm sàng**:
  - Kiểm tra huyết áp 92/58 mmHg không kèm triệu chứng thiếu máu não.
  - Không có choáng váng hay dấu hiệu giảm tưới máu ngoại biên.
- **Nội dung 2.2: Dữ kiện quyết định chuẩn độ khi Huyết áp thấp**:
  - Bệnh nhân không có triệu chứng tụt huyết áp.
  - eGFR và K+ máu hoàn toàn trong ngưỡng an toàn.
- **Nội dung 2.3: Hành động duy trì Tứ trụ & Tăng liều Beta-blocker**:
  1. TIẾP TỤC DUY TRÌ "TỨ TRỤ" HIỆN TẠI.
  2. Tăng liều Bisoprolol từ 2.5mg lên 3.75mg/ngày (vì HR 68 bpm và Beta-blocker ít ảnh hưởng trên SBP).
  3. Giữ nguyên liều ARNI 24/26mg x 2 lần/ngày.
- **Nội dung 2.4: Hướng dẫn bệnh nhân tự đo huyết áp tại nhà**:
  - Hướng dẫn bệnh nhân tự đo huyết áp tại nhà lúc nghỉ.
  - Hẹn tái khám sau 2-4 tuần.
- **Nội dung 2.5: Phân tích lý do giảm liều hoặc ngừng thuốc là sai**:
  - *Tạm ngưng ARNI và Spironolactone do SBP < 100 mmHg*: Sai nghiêm trọng, vì tụt huyết áp không triệu chứng không phải là lý do ngừng GDMT.
  - *Truyền dịch NaCl 0.9% để nâng huyết áp*: Sai, nguy cơ gây quá tải thể tích và Phù phổi cấp.

---

### Ca lâm sàng 3: Xử trí tăng Kali máu (K+ 5.6 mmol/L) và eGFR giảm 25% sau khởi trị ARNI & Spironolactone

**Bối cảnh lâm sàng**:
- Bệnh nhân nam 67 tuổi, HFrEF (LVEF = 35%), CKD giai đoạn 3a (eGFR nền = 52 mL/min).
- Sau 2 tuần khởi trị ARNI 49/51mg x2 và Spironolactone 25mg/ngày.
- Xét nghiệm kiểm tra: K+ máu tăng từ 4.4 lên **5.6 mmol/L**.
- Creatinine tăng từ 110 lên **138 µmol/L** (eGFR giảm 25%).
- Bệnh nhân không khó thở, không phù.

**Kiểm soát Kali Máu & Chức năng Thận Ca 3**:
- **Nội dung 3.1: Red flag tầm soát sóng T nhọn trên ECG**:
  - Tầm soát nguy cơ rối loạn nhịp tim do K+ 5.6 mmol/L (làm ngay ECG).
- **Nội dung 3.2: Dữ kiện Kali máu 5.6 mmol/L và eGFR giảm 25%**:
  - eGFR giảm 25% (< 30%) là đáp ứng "Kidney dip" sinh lý chấp nhận được.
  - K+ 5.6 mmol/L thuộc mức tăng trung bình.
- **Nội dung 3.3: Hành động điều chỉnh liều MRA & Dùng Patiromer**:
  1. KHÔNG NGỪNG GDMT.
  2. Giảm liều Spironolactone từ 25mg/ngày xuống **12.5 mg/ngày**.
  3. Duy trì liều ARNI 49/51mg x 2 lần/ngày.
  4. Khởi trị **Patiromer 8.4g x 1 lần/ngày** (thuốc gắn K+ tại ruột) để hạ K+ máu.
- **Nội dung 3.4: Lịch thử lại K+ máu và Creatinine serum**:
  - Thử lại K+ máu và Creatinine sau 7 ngày.
- **Nội dung 3.5: Phân tích lý do không cắt bỏ MRA hoặc ARNI**:
  - *Hủy bỏ hoàn toàn Spironolactone và ARNI*: Sai, tước đi cơ hội sống của bệnh nhân. Hiện đã có thuốc gắn K+ cho phép duy trì GDMT an toàn.
  - *Dùng Kayexalate kéo dài*: Sai, vì Kayexalate nguy cơ gây hoại tử ruột cao.

---

### Ca lâm sàng 4: Quản lý thuốc GDMT mạn tính khi bệnh nhân nhập viện vì đợt cấp suy tim mất bù

**Bối cảnh lâm sàng**:
- Bệnh nhân nữ 71 tuổi, HFrEF (LVEF 30%) đang dùng đủ 4 trụ cột (ARNI, Bisoprolol 5mg, Spironolactone 25mg, Dapagliflozin 10mg).
- Nhập viện vì khó thở dâng cao, phù 2 chân, rale ẩm 2 đáy phổi.
- Huyết áp 110/70 mmHg, nhịp tim 95 bpm.
- Chẩn đoán: Đợt cấp suy tim mất bù (Profile Warm & Wet).

**Quản lý GDMT trong Đợt Suy tim Cấp Ca 4**:
- **Nội dung 4.1: Red flag suy hô hấp do đợt cấp sung huyết**:
  - Tầm soát mức độ nặng của sung huyết phổi cấp.
- **Nội dung 4.2: Dữ kiện huyết động lúc nhập viện suy tim cấp**:
  - Huyết áp ổn định (110/70 mmHg, không có sốc giảm tưới máu).
- **Nội dung 4.3: Hành động dùng Furosemide IV và giữ nguyên GDMT**:
  1. Dùng Furosemide IV cấp cứu để giảm sung huyết.
  2. DUY TRÌ ARNI, SPIRONOLACTONE VÀ DAPAGLIFLOZIN.
  3. Với Bisoprolol: DUY TRÌ LIỀU HIỆN TẠI (5mg). TUYỆT ĐỐI KHÔNG NGỪNG ĐỘT NGỘT Beta-blocker mạn tính trừ khi có sốc tim.
- **Nội dung 4.4: Theo dõi đáp ứng giảm nhẹ khó thở và thể tích**:
  - Theo dõi lượng nước tiểu và giảm khó thở mỗi 4 giờ.
- **Nội dung 4.5: Phân tích lý do ngưng Beta-blocker mạn tính là sai**:
  - *Cắt toàn bộ Beta-blocker và ARNI ngay khi nhập viện*: Sai, ngừng Beta-blocker đột ngột gây ra hiện tượng "rebound" giao cảm bùng nổ, tăng tử vong trong viện.
  - *Cho thêm Digoxin IV liều cao*: Sai, không có chỉ định khi chưa tối ưu lợi tiểu.

---

### Ca lâm sàng 5: Bệnh nhân suy tim mạn tái phát sung huyết do không tuân thủ và tự ý dùng NSAID

**Bối cảnh lâm sàng**:
- Bệnh nhân nam 62 tuổi, HFrEF (LVEF 33%) điều trị ổn định 1 năm nay.
- 1 tuần nay xuất hiện khó thở tăng dần, phù 2 cẳng chân, tăng 3kg cân nặng.
- Khai thác tiền sử: Cách đây 10 ngày bị đau khớp gối và tự mua **Celecoxib 200mg x 2 lần/ngày** uống 7 ngày.

**Xử trí Tương tác Thuốc & Không Tuân thủ Ca 5**:
- **Nội dung 5.1: Red flag tái phát sung huyết do tương tác thuốc**:
  - Nhận diện Celecoxib (NSAID) là yếu tố thúc đẩy đợt mất bù.
- **Nội dung 5.2: Dữ kiện sử dụng Celecoxib đau khớp gối**:
  - NSAID ức chế COX-2 tại thận, giảm Prostaglandin → Co động mạch vào cầu thận, tăng giữ Natri/nước, triệt tiêu tác dụng GDMT.
- **Nội dung 5.3: Hành động ngừng ngay NSAID và điều chỉnh lợi tiểu**:
  1. NGỪNG NGAY LẬP ĐỨC CELECOXIB (NSAID).
  2. Tăng liều Furosemide tạm thời trong 3-5 ngày để giải quyết 3kg dịch tích tụ.
  3. Thay thế giảm đau bằng Paracetamol liều ≤ 2g/ngày.
- **Nội dung 5.4: Theo dõi cân nặng hàng ngày về mức nền**:
  - Đánh giá cân nặng hàng ngày, tái khám sau 5 ngày.
- **Nội dung 5.5: Phân tích lý do tăng liều GDMT đè NSAID là sai**:
  - *Tăng liều ARNI và Spironolactone mà vẫn tiếp tục uống Celecoxib*: Sai hoàn toàn, NSAID đối kháng trực tiếp cơ chế dược lý của GDMT và gây tổn thương thận cấp AKI.

---
"""

p8 = """
## 8. THEO DÕI, QUẢN LÝ DÀI HẠN VÀ TUÂN THỦ ĐIỀU TRỊ [CỐT LÕI]

### 8.1 Lịch trình theo dõi lâm sàng và cận lâm sàng

Quản lý HFrEF mạn tính là một hành trình dài hạn đòi hỏi lịch trình theo dõi định kỳ chặt chẽ:

**Giai đoạn chuẩn độ (1 đến 3 tháng đầu)**:
- Tái khám mỗi **1 đến 2 tuần** sau mỗi lần tăng liều GDMT.
- Đánh giá huyết áp tư thế đứng và nằm.
- Đánh giá tần số tim lúc nghỉ và dấu hiệu quá tải thể tích.
- Đánh giá cân nặng hàng ngày và sự cải thiện triệu chứng khó thở.
- Kiểm tra ran ẩm ở hai đáy phổi và tình trạng phù chân.
- Xét nghiệm bắt buộc: **Creatinine, eGFR, K+ máu** (làm sau 7-14 ngày mỗi lần tăng liều ARNI/ACEi/MRA).

**Giai đoạn duy trì ổn định**:
- Tái khám định kỳ mỗi **1 đến 3 tháng**.
- Xét nghiệm Creatinine, eGFR và K+ máu mỗi 3-6 tháng.
- Siêu âm tim (Echocardiography):
  - Đo lại LVEF sau **3 đến 6 tháng** điều trị GDMT đạt liều mục tiêu.
  - Đánh giá sự đảo ngược tái cấu trúc thất trái (Reverse Remodeling).
  - Nếu LVEF tăng từ ≤35% lên >40%, bệnh nhân chuyển sang nhóm **HFimpEF**.
  - Tiếp tục duy trì đầy đủ "Tứ trụ" GDMT, KHÔNG ĐƯỢC NGỪNG THUỐC!

### 8.2 Chiến lược nâng cao tuân thủ điều trị (Medication Adherence)

- **Đơn giản hóa phác đồ điều trị**:
  - Ưu tiên các thuốc uống 1 lần/ngày (Bisoprolol, Spironolactone, Dapagliflozin).
  - Cho uống thuốc vào thời điểm cố định trong ngày để tạo thói quen.
- **Sử dụng hộp chia thuốc theo ngày (Pillbox)**:
  - Giúp bệnh nhân và người nhà kiểm soát các liều thuốc đã uống.
  - Tránh uống nhầm liều hoặc quên liều thuốc trong ngày.
- **Tư vấn tác dụng phụ lành tính**:
  - Giải thích trước cho bệnh nhân biết hiện tượng đi tiểu nhiều hơn (do SGLT2i/lợi tiểu).
  - Tư vấn tác dụng giảm nhẹ huyết áp để bệnh nhân yên tâm tuân thủ điều trị.

### 8.3 Giáo dục bệnh nhân: Tự quản lý thể tích, lượng muối, và cân nặng hàng ngày

- **Theo dõi cân nặng hàng ngày**:
  - Cân vào mỗi buổi sáng sau khi đi tiểu và trước khi ăn sáng.
  - Ghi chép nhật ký cân nặng hàng ngày vào sổ theo dõi.
- **Dấu hiệu cảnh báo sớm giữ nước**:
  - Cân nặng tăng **> 1.5 - 2 kg trong 2 ngày liên tiếp**.
  - Hoặc cân nặng tăng **> 2.5 kg trong 1 tuần**.
  - Đây là dấu hiệu tích tụ dịch cấp tính trước khi xuất hiện phù chân hay khó thở!
- **Hành động điều chỉnh lợi tiểu**:
  - Hướng dẫn bệnh nhân tự tăng 1 viên Furosemide 40mg trong 2-3 ngày.
  - Liên hệ ngay với bác sĩ điều trị để được hướng dẫn thêm.
- **Chế độ ăn giảm Natri nghiêm ngặt**:
  - Hạn chế muối < 2g Natri/ngày (< 5g muối ăn NaCl/ngày).
  - Tránh các loại thực phẩm chế biến sẵn, dưa muối, nước mắm, mắm nêm.
- **Hạn chế lượng nước uống**:
  - CHỈ áp dụng hạn chế dịch (1.5 - 2 lít/ngày) ở bệnh nhân suy tim nặng.
  - Áp dụng khi có khó kiểm soát sung huyết hoặc có hạ Natri máu (Na+ < 130 mmol/L).

---
"""

p9 = """
## 9. TIPS KÊ ĐƠN VÀ THỰC HÀNH LÂM SÀNG [CỐT LÕI]

Dưới đây là 13 tips thực hành lâm sàng đúc kết dành cho bác sĩ kê đơn HFrEF mạn:

- Tip 1: Đừng đợi chuẩn độ xong thuốc này rồi mới khởi trị thuốc khác. Hãy khởi trị liều thấp của CẢ 4 TRỤ CỘT cùng một lúc trong tuần đầu tiên.
- Tip 2: Khi chuyển từ Enalapril/Lisinopril sang Sacubitril/Valsartan, luôn dặn bệnh nhân căn đủ 36 giờ tính từ viên ACEi cuối cùng trước khi uống viên ARNI đầu tiên.
- Tip 3: SGLT2i (Dapagliflozin 10mg hoặc Empagliflozin 10mg) là thuốc dễ khởi trị nhất trong Tứ trụ vì không cần chuẩn độ liều và ít gây hạ huyết áp nhất.
- Tip 4: Nếu bệnh nhân có huyết áp tâm thu 90-95 mmHg nhưng hoàn toàn không có triệu chứng choáng váng, HÃY CỨ TIẾP TỤC GIỮ NGUYÊN LIỀU GDMT.
- Tip 5: Tăng Creatinine serum dưới 30% sau khi cho ARNI hoặc SGLT2i là dấu hiệu thuốc đang giảm áp lực cầu thận để bảo vệ thận dài hạn. Đừng hoảng sợ ngưng thuốc!
- Tip 6: Chỉ dùng 1 trong 3 Beta-blocker có bằng chứng: Bisoprolol, Carvedilol, hoặc Metoprolol Succinate XL. Tuyệt đối không dùng Atenolol hay Metoprolol Tartrate cho HFrEF.
- Tip 7: Đừng khởi trị Beta-blocker khi bệnh nhân còn rale ẩm ở phổi hoặc còn phù nặng. Phải dùng lợi tiểu quai đưa bệnh nhân về trạng thái "khô" trước.
- Tip 8: Nếu K+ máu tăng lên 5.6 mmol/L khi đang dùng Spironolactone, hãy cho thêm thuốc gắn K+ ruột Patiromer/SZC và giảm liều Spironolactone xuống 12.5mg thay vì cắt bỏ hẳn MRA.
- Tip 9: Khi bệnh nhân bị kháng lợi tiểu Furosemide uống, cho uống Metolazone 2.5mg trước khi uống Furosemide 30 phút để tạo hiệu ứng phong lập nephron tuần tự dội bọt.
- Tip 10: Luôn kiểm tra Ferritin và TSAT ở bệnh nhân HFrEF. Nếu Ferritin < 100 µg/L, hãy bù Sắt đường TĨNH MẠCH (Ferric Carboxymaltose). Sắt uống hoàn toàn không có tác dụng.
- Tip 11: Dặn bệnh nhân tự cân nặng mỗi sáng. Tăng 2kg trong 2 ngày là dấu hiệu giữ nước cấp tính cần uống thêm 1 viên lợi tiểu quai ngay.
- Tip 12: Cấm tuyệt đối bệnh nhân suy tim tự ý mua thuốc giảm đau chống viêm NSAID (Ibuprofen, Meloxicam, Celecoxib) vì NSAID sẽ gây giữ nước và suy thận cấp.
- Tip 13: Nếu LVEF của bệnh nhân hồi phục từ 30% lên 50% sau 6 tháng GDMT (HFimpEF), HÃY DẶN BỆNH NHÂN TIẾP TỤC UỐNG ĐỦ 4 THUỐC CẢ ĐỜI, ngừng thuốc LVEF sẽ tụt trở lại.

---

## 10. TỔNG KẾT VÀ TÀI LIỆU THAM KHẢO

### 10.1 Tóm tắt các điểm mấu chốt (Summary Key Points)

1. **HFrEF mạn (LVEF ≤ 40%)** là bệnh lý tiến triển do kích hoạt mạn tính hệ thần kinh thể dịch (RAAS, SNS). Điều trị cốt lõi là phong lập các con đường này.
2. **"Tứ trụ GDMT" bắt buộc** cho mọi bệnh nhân HFrEF gồm: **ARNI (hoặc ACEi/ARB), Beta-blocker (Bisoprolol/Carvedilol/Metoprolol XL), MRA (Spironolactone/Eplerenone) và SGLT2i (Dapagliflozin/Empagliflozin)**.
3. **Chiến lược chuẩn độ nhanh**: Khởi trị đồng thời 4 trụ cột ngay khi ổn định và tăng dần liều đạt liều mục tiêu trong vòng 2-4 tuần.
4. **ARNI (Sacubitril/Valsartan)** vượt trội hơn ACEi/ARB, giảm 20% tử vong tim mạch/nhập viện. Bắt buộc **washout 36 giờ** khi chuyển từ ACEi sang ARNI.
5. **SGLT2i** giảm 25-26% biến cố tim mạch và bảo vệ thận dài hạn, dùng được cho cả người có hoặc không có Đái tháo đường, không cần chuẩn độ liều (cố định 10mg/ngày).
6. **MRA** yêu cầu điều kiện khởi trị: K+ < 5.0 mmol/L và eGFR ≥ 30 mL/min. Tăng K+ máu từ 5.5 - 6.0 mmol/L nên dùng thuốc gắn K+ (Patiromer/SZC) thay vì ngừng MRA.
7. **"Kidney dip" (eGFR giảm < 30%)** sau khởi trị ARNI/ACEi/SGLT2i là đáp ứng sinh lý bình thường do giảm áp lực lọc nội cầu, KHÔNG ngừng thuốc.
8. **Kháng lợi tiểu quai**: Xử trí bằng cách tăng liều đơn Furosemide, chuyển sang Torsemide, hoặc phối hợp lợi tiểu Thiazide/Metolazone (Sequential Nephron Blockade).

### 10.2 8+ Misconceptions (Sai lầm phổ biến khi điều trị HFrEF)

> ⚠️ HỌC VIÊN HAY NHẦM 1: Nhầm tưởng Lợi tiểu quai (Furosemide) làm giảm tỷ lệ tử vong trong HFrEF. Thực tế, lợi tiểu chỉ giúp giải quyết triệu chứng sung huyết, KHÔNG làm giảm tử vong dài hạn. CHỈ CÓ "Tứ trụ GDMT" mới làm giảm tử vong.
>
> ⚠️ HỌC VIÊN HAY NHẦM 2: Nhầm tưởng Huyết áp tâm thu 90-95 mmHg ở bệnh nhân suy tim là chống chỉ định của GDMT. Thực tế, nếu bệnh nhân không có triệu chứng hoa mắt choáng váng, đây là mức huyết áp dung nạp tốt và cần duy trì GDMT.
>
> ⚠️ HỌC VIÊN HAY NHẦM 3: Ngừng ngay ARNI/ACEi khi thấy Creatinine tăng 20% sau 1 tuần điều trị. Thực tế, Creatinine tăng < 30% là đáp ứng sinh lý "Kidney dip" bình thường do giảm áp lực lọc nội cầu, không được ngừng thuốc.
>
> ⚠️ HỌC VIÊN HAY NHẦM 4: Cho rằng có thể uống phối hợp Sacubitril/Valsartan (ARNI) chung với Enalapril để tăng tác dụng. Thực tế, phối hợp này gây phù mạch hoại tử tử vong do Bradykinin tăng bùng nổ.
>
> ⚠️ HỌC VIÊN HAY NHẦM 5: Nghĩ rằng thuốc SGLT2i chỉ dùng cho bệnh nhân suy tim có kèm Đái tháo đường. Thực tế, SGLT2i làm giảm tử vong và nhập viện ở MỌI bệnh nhân HFrEF dù đường huyết hoàn toàn bình thường.
>
> ⚠️ HỌC VIÊN HAY NHẦM 6: Khởi trị Beta-blocker ngay trong đợt phù phổi cấp hay suy tim mất bù nặng. Thực tế, Beta-blocker ức chế co bóp cơ tim cấp sẽ làm bệnh nhân ức chế tuần hoàn tử vong; chỉ khởi trị khi bệnh nhân đã đạt thể tích đẳng thể.
>
> ⚠️ HỌC VIÊN HAY NHẦM 7: Kê đơn viên sắt uống (Ferrous Sulfate) để điều trị thiếu sắt cho bệnh nhân suy tim. Thực tế, Hepcidin tăng cao trong suy tim làm ruột không hấp thu được sắt uống; BẮT BUỘC phải bù Sắt đường Tĩnh mạch.
>
> ⚠️ HỌC VIÊN HAY NHẦM 8: Khi LVEF của bệnh nhân hồi phục về bình thường (> 50%) sau 1 năm điều trị thì tự ý ngưng hết thuốc GDMT. Thực tế, đây là thể HFimpEF, ngưng thuốc sẽ làm tim giãn trở lại và suy tim tái phát nặng nề hơn.

### 10.3 5 Checkpoints Tự kiểm tra kiến thức

> 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA CHỦ ĐỀ TỨ TRỤ GDMT:
> **Câu hỏi 1**: Bốn nhóm thuốc tạo thành "Tứ trụ GDMT" trong điều trị HFrEF mạn tính là gì?
> *(Đáp án: 1. ARNI (hoặc ACEi/ARB); 2. Beta-blocker được chứng minh (Bisoprolol, Carvedilol, Metoprolol XL); 3. MRA (Spironolactone, Eplerenone); 4. SGLT2i (Dapagliflozin, Empagliflozin)).*

> 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA CHỦ ĐỀ WASHOUT 36 GIỜ ARNI:
> **Câu hỏi 2**: Khi chuyển một bệnh nhân từ Perindopril (ACEi) sang Sacubitril/Valsartan (ARNI), khoảng thời gian washout tối thiểu bắt buộc là bao lâu và tại sao?
> *(Đáp án: Tối thiểu 36 giờ tròn. Để tránh nguy cơ Phù mạch hoại tử đường thở nguy hiểm tính mạng do Bradykinin bị tích tụ bởi sự ức chế đồng thời ACE và Neprilysin).*

> 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA CHỦ ĐỀ KIDNEY DIP VÀ CREATININE:
> **Câu hỏi 3**: Mức tăng Creatinine serum tối đa chấp nhận được sau khi khởi trị ARNI hoặc SGLT2i mà KHÔNG CẦN ngừng thuốc là bao nhiêu?
> *(Đáp án: Mức tăng Creatinine < 30% so với giá trị nền (hoặc eGFR giảm < 30%) được coi là đáp ứng sinh lý bình thường do giảm áp lực lọc nội cầu ("Kidney dip"), không cần ngừng thuốc).*

> 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA CHỦ ĐỀ TIÊU CHUẨN BÙ SẮT TĨNH MẠCH:
> **Câu hỏi 4**: Hai tiêu chuẩn xét nghiệm để chẩn đoán thiếu sắt cần bù sắt tĩnh mạch ở bệnh nhân HFrEF là gì?
> *(Đáp án: 1. Ferritin < 100 µg/L; hoặc 2. Ferritin 100 - 299 µg/L kèm theo Độ bão hòa Transferrin TSAT < 20%).*

> 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA CHỦ ĐỀ PHONG LẬP NEPHRON TUẦN TỰ:
> **Câu hỏi 5**: Chiến lược "Phong lập Nephron Tuần tự" (Sequential Nephron Blockade) trong xử trí kháng lợi tiểu quai được thực hiện như thế nào?
> *(Đáp án: Cho uống thuốc lợi tiểu ức chế ống lượn xa (Metolazone 2.5-5mg hoặc HCTZ 25-50mg) trước khi uống thuốc lợi tiểu quai Furosemide/Torsemide 30 phút để ngăn chặn sự tái hấp thu Natri bù trừ tại ống lượn xa).*

## 11. TÀI LIỆU THAM KHẢO

1. Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines. Circulation. 2022. PMID: 35363499.
2. McMurray JJV, Packer M, Desai AS, et al. Angiotensin-neprilysin inhibition versus enalapril in heart failure (PARADIGM-HF). N Engl J Med. 2014.
3. McMurray JJV, Solomon SD, Inzucchi SE, et al. Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction (DAPA-HF). N Engl J Med. 2019.
4. Packer M, Anker SD, Butler J, et al. Cardiovascular and Renal Outcomes with Empagliflozin in Heart Failure (EMPEROR-Reduced). N Engl J Med. 2020.
5. McDonagh TA, Metra M, Adamo M, et al. 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure. Eur Heart J. 2021.

---


"""

full_md = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9

md_path.write_text(full_md, encoding="utf-8")
print("Expanded MD written successfully.")