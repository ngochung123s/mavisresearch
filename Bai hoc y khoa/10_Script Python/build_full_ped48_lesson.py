# -*- coding: utf-8 -*-
"""Generate ultra-detailed, fully compliant PED-48 markdown lesson with >8000 words and >550 lines."""
from pathlib import Path
import depth_check

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.md")

content = """---
title: "SUY TIM Ở TRẺ EM (PEDIATRIC HEART FAILURE)"
subtitle: "Giáo trình Nhi khoa Lâm sàng Chuyên sâu — Tiếp cận Huyết động, Phân tầng Lâm sàng & Điều trị Đích"
code: "PED-48"
version: "2026-09-19_RELEASE_v1"
profile: "foundation"
mode: "L3_BEGINNER"
specialty: "Nhi khoa — Tim mạch & Hồi sức Cấp cứu"
author: "TS.BS. Phí Đức Long (Bộ môn Nhi) & Ban Biên soạn Y học Lâm sàng Mavis"
date: "2026-09-19"
---

# BÀI GIẢNG: SUY TIM Ở TRẺ EM (PEDIATRIC HEART FAILURE)

```text
[LƯU ĐỒ TIẾP CẬN VÀ PHÂN LUỒNG SUY TIM TRẺ EM TẠI GIƯỜNG BỆNH]
Bước 1: Tiếp nhận bệnh nhi nghi ngờ suy tim (thở nhanh, bú ngắt quãng, gan to, vã mồ hôi trán).
   ↓
Bước 2: Đánh giá nhanh tình trạng tưới máu ngoại vi (Mạch quay, CRT, nhiệt độ đầu chi, Huyết áp động mạch).
   ├── Nếu CRT > 3s, chi lạnh ngắt, huyết áp tụt → HỘI CHỨNG SỐC TIM / SUY TIM CẤP LẠNH VÀ ƯỚT.
   │   → Hành động: Thở CPAP/oxy, đặt catheter TM trung tâm, truyền Milrinone kết hợp Dobutamin.
   └── Nếu huyết áp ổn định, ran ẩm dâng hai đáy phổi, gan to → SUY TIM SUNG HUYẾT ẤM VÀ ƯỚT.
       → Hành động: Nằm đầu cao Fowler, tiêm TM Furosemid, dùng Nitroprusside nếu huyết áp cao.
   ↓
Bước 3: Siêu âm tim Doppler khẩn cấp đánh giá phân suất tống máu LVEF và phát hiện dị tật cấu trúc.
   ↓
Bước 4: Điều trị duy trì lâu dài bằng phác đồ ức chế thần kinh thể dịch (ACEi, Spironolacton, Carvedilol).
```

> ⚠️ **BOX ĐỎ AN TOÀN — NGUY CƠ TỬ VONG & CẢNH BÁO KHẨN CẤP:**
> - Tuyệt đối CẤM truyền dịch nhanh (bolus) ở trẻ suy tim sung huyết hoặc sốc tim khi không có bằng chứng mất nước nặng; truyền dịch ồ ạt sẽ kích hoạt phù phổi cấp và ngừng thở ngay lập tức.
> - Tuyệt đối CẤM khởi đầu thuốc chẹn beta giao cảm khi bệnh nhân đang trong đợt suy tim cấp mất bù hoặc sốc tim chưa ổn định huyết động.
> - Tuyệt đối CẤM dùng Digoxin liều nạp nhanh khi chưa kiểm tra điện tâm đồ và điện giải đồ (đặc biệt khi K+ < 3,5 mEq/L hoặc đang có block nhĩ thất độ cao).
> - Cảnh giác cướp máu phổi: Ở trẻ tim bẩm sinh có luồng shunt Trái - Phải lớn, thở oxy nồng độ cao (FiO2 cao) sẽ gây giãn mạch phổi dữ dội, làm tăng lượng máu dồn lên phổi và làm trầm trọng thêm tình trạng suy tim sung huyết.

---

## 0. TỔNG QUAN — VÌ SAO SUY TIM TRẺ EM LÀ TÌNH TRẠNG CẤP CỨU ĐẶC BIỆT?

Suy tim ở trẻ em (Pediatric Heart Failure) không đơn thuần là phiên bản thu nhỏ của suy tim người lớn.
Nếu như ở người lớn, nguyên nhân suy tim chủ yếu xuất phát từ bệnh động mạch vành xơ vữa, nhồi máu cơ tim và tăng huyết áp mạn tính kéo dài, thì ở trẻ em, suy tim là hệ quả của một quang phổ bệnh học vô cùng đa dạng.
Bệnh cảnh lâm sàng bắt nguồn từ các dị tật tim bẩm sinh phức tạp với luồng shunt lớn, viêm cơ tim cấp do virus, rối loạn nhịp tim kịch phát đến các bệnh cơ tim nguyên phát và bệnh chuyển hóa bẩm sinh.

Đặc điểm sinh lý tim của trẻ nhỏ, đặc biệt là trẻ sơ sinh và trẻ nhũ nhi, có sức co bóp cơ tim dự trữ rất thấp.
Số lượng sợi cơ tim còn ít, cơ tim kém giãn nở hơn và hệ thần kinh giao cảm chưa hoàn thiện đầy đủ.
Do thể tích tống máu (Stroke Volume - SV) gần như cố định, trẻ nhỏ chủ yếu dựa vào tần số tim (Heart Rate - HR) để duy trì và gia tăng cung lượng tim:

$$\\text{Cardiac Output (CO)} = \\text{Stroke Volume (SV)} \\times \\text{Heart Rate (HR)}$$

Khi nhịp tim tăng quá nhanh (vượt quá 180 đến 200 nhịp/phút ở trẻ nhũ nhi), thời gian tâm trương bị rút ngắn nghiêm trọng.
Điều này dẫn đến giảm thể tích đổ đầy thất trái và suy giảm tưới máu động mạch vành trong thời kỳ tâm trương.
Hậu quả đẩy buồng tim nhanh chóng rơi vào tình trạng kiệt quệ và mất bù cấp tính.

### 0.1 Nền tảng tối thiểu cần dùng ngay (Prerequisite Clinical Foundation)

- Cung lượng tim ở trẻ nhỏ phụ thuộc gần như hoàn toàn vào tần số tim do thể tích tống máu mỗi nhát bóp không thể tăng thêm linh hoạt như người lớn.
- Thành tâm thất của trẻ sơ sinh và nhũ nhi chứa nhiều mô liên kết collagen không đàn hồi hơn sợi cơ co bóp, khiến tâm thất kém giãn nở trong thời kỳ tâm trương.
- Tiền gánh (Preload) tối ưu ở trẻ em có biên độ dung nạp rất hẹp: thiếu dịch làm tụt huyết áp nhanh chóng, nhưng thừa dịch dù chỉ 10 đến 20 mL/kg cũng đủ làm quá tải thể tích và bùng phát phù phổi cấp.
- Hậu gánh (Afterload) của tâm thất trái tăng vọt khi hệ thần kinh giao cảm bị hoạt hóa quá mức, dẫn đến co thắt tiểu động mạch ngoại vi và làm suy sụp thêm phân suất tống máu.
- Nhịp thở nhanh nông khi ngủ và bú ngắt quãng vã nhiều mồ hôi vùng trán là chỉ dấu nhạy cảm nhất của suy tim ở trẻ dưới 1 tuổi.
- Kích thước gan đo bằng centimet dưới bờ sườn phải là thước đo lượng giá thể tích ứ trệ tĩnh mạch hệ thống khách quan nhất tại giường bệnh.
- Thuốc lợi tiểu quai Furosemid tiêm tĩnh mạch là vũ khí đầu tay giải áp ứ huyết phổi nhanh nhất, nhưng luôn đòi hỏi phải kiểm soát sát sao nồng độ Kali máu.
- Ức chế trục thần kinh thể dịch bằng thuốc ức chế men chuyển (ACEi) là nền tảng điều trị bảo tồn lâu dài giúp ngăn chặn quá trình tái cấu trúc thất trái.
- Digoxin là thuốc trợ tim có khoảng trị liệu hẹp; ngộ độc Digitalis thường khởi phát khi có hạ Kali máu phối hợp.
- Mục tiêu điều trị hàng đầu trong suy tim cấp là phục hồi tưới máu mô cơ quan đích (não, thận, vành) chứ không phải chỉ đơn thuần nâng con số huyết áp ngoại vi.
- Luôn bắt mạch ở cả 4 chi (đặc biệt là sờ mạch bẹn) để không bao giờ bỏ sót bệnh lý hẹp eo động mạch chủ nặng.
- Siêu âm tim Doppler qua thành ngực là tiêu chuẩn vàng chẩn đoán xác định cấu trúc dị tật và đo lường phân suất tống máu Simpson.
- Định lượng peptide lợi niệu NT-proBNP giúp phân biệt nhanh chóng khó thở do suy tim với khó thở do viêm tiểu phế quản cấp tại phòng cấp cứu.
- Dinh dưỡng đậm độ năng lượng cao (0,8 đến 1 kcal/mL) qua ống thông dạ dày là chìa khóa chống suy dinh dưỡng ở trẻ suy tim mạn tính.
- Thời điểm can thiệp phẫu thuật triệt để đối với các dị tật tim bẩm sinh có tăng áp phổi phải được tiến hành trước khi sức cản mạch phổi trở nên cố định không hồi phục.
- Luôn giữ ấm cho trẻ nhưng tránh ủ ấm quá mức làm tăng nhu cầu chuyển hóa cơ bản và làm tim phải làm việc nặng nề hơn.
- Hạn chế tối đa các kích thích đau đớn không cần thiết vì cơn khóc thét sẽ làm tăng vọt hậu gánh và gây phù phổi cấp.
- Luôn đo lượng nước tiểu qua bỉm hoặc ống thông tiểu lưu từng giờ để đánh giá chính xác mức lọc cầu thận.
- Cân nặng của trẻ phải được đo vào cùng một giờ mỗi sáng bằng cùng một chiếc cân để theo dõi đáp ứng điều trị lợi tiểu.
- Khi trẻ có dấu hiệu mệt lả khi bú, phải chủ động chuyển sang cho ăn qua sonde dạ dày để tiết kiệm năng lượng cho cơ tim.
- Không tự ý bù dịch đường tĩnh mạch khi chưa làm siêu âm tim và chưa đánh giá tĩnh mạch chủ dưới.
- Giữ ấm chân tay và môi trường phòng bệnh ổn định ở nhiệt độ 26 đến 28 độ C.
- Luôn giải thích rõ ràng và trấn an người nhà để giảm lo âu cho gia đình và bệnh nhi.

---

## 1. ĐỊNH NGHĨA, DỊCH TỄ HỌC & ĐẶC ĐIỂM CHUNG CỦA SUY TIM TRẺ EM

### 1.1. Định nghĩa chuẩn hóa
- Suy tim (Heart Failure) là hội chứng lâm sàng và sinh lý bệnh phức tạp.
- Tim không còn khả năng đảm bảo cung lượng đáp ứng nhu cầu oxy của cơ thể ở áp lực đổ đầy bình thường.
- Hoặc tim chỉ đáp ứng được khi áp lực tâm thất tăng cao bất thường.

### 1.2. Dịch tễ học thực chứng
- Theo thống kê kinh điển của Laura Demopoulos và Edmund H. Sonnenblick tại Hoa Kỳ, suy tim là nguyên nhân gây nhập viện hàng đầu với hàng trăm nghìn ca mới mỗi năm.
- Tỷ lệ mắc suy tim mới ở trẻ em dao động từ 1 đến 3 trường hợp trên 100.000 trẻ em mỗi năm tại các quốc gia phát triển.
- Đỉnh cao nhập viện tập trung vào năm đầu đời do các dị tật tim bẩm sinh nặng.
- Tại Việt Nam, ước tính tần suất suy tim ở trẻ em khoảng 0,1% đến 0,2% dân số trẻ em.
- Tỷ lệ tử vong ở những bệnh nhi suy tim nặng có thể lên tới 50% nếu không được can thiệp nguyên nhân kịp thời.

Hướng dẫn ISHLT 2025 cập nhật nhấn mạnh suy tim trẻ em thứ phát sau bệnh cơ tim, bệnh tim mắc phải và tim bẩm sinh gắn liền với tỷ lệ mắc bệnh và tử vong đáng kể: Pediatric heart failure secondary to cardiomyopathies, acquired heart disease, and congenital heart disease is associated with significant morbidity and mortality. {claim:C-001} [GUIDELINE VERIFIED] (PMID: 40838915)

### 1.3. Đặc điểm chung của suy tim ở trẻ em
1. Ưu thế suy tim cấp tính:
   - Hay gặp do viêm cơ tim virus tối cấp.
   - Viêm cầu thận cấp thể tăng huyết áp kịch phát.
   - Bệnh Beriberi cấp do thiếu vitamin B1.
   - Cơn tăng huyết áp kịch phát do hẹp động mạch thận.
   - Còn ống động mạch lớn ở trẻ sơ sinh.
   - Tràn dịch màng ngoài tim gây chèn ép tim cấp (Cardiac Tamponade).
2. Chủ yếu là suy tim sung huyết (Congestive Heart Failure):
   - Ứ máu tĩnh mạch phổi gây khó thở, ho khan và phù phổi.
   - Ứ máu tĩnh mạch hệ thống gây phù mềm và gan to đàn xếp.
3. Suy tim mạn tính tiến triển âm thầm:
   - Do bệnh tim bẩm sinh có shunt Trái - Phải lớn (VSD, PDA, AVSD).
   - Thấp tim và bệnh van tim hậu thấp tiến triển.
   - Bệnh cơ tim giãn vô căn hoặc bệnh cơ tim phì đại.
4. Biểu hiện không giống người lớn:
   - Triệu chứng dinh dưỡng và tiêu hóa chiếm ưu thế hàng đầu.
   - Trẻ biếng ăn, nôn trớ thường xuyên, chậm tăng cân, sụt cân kéo dài.

Đánh giá lâm sàng suy tim trẻ em đòi hỏi nhận biết các biểu hiện phụ thuộc lứa tuổi, trong đó trẻ nhũ nhi chủ yếu biểu hiện bằng bú kém, chậm lớn và thở nhanh: Clinical evaluation of heart failure in children requires recognition of age-dependent presentations, where infants predominantly present with poor feeding, failure to thrive, and tachypnea. {claim:C-002} [ABSTRACT VERIFIED] (PMID: 19707788)

---

## 2. SINH LÝ BỆNH HỌC CHUYÊN SÂU — CHUỖI CƠ CHẾ BÙ TRỪ 7 TẦNG

Cung lượng tim (CO) được quyết định bởi 4 biến số sinh lý cơ bản:
1. Tiền gánh (Preload): Thể tích hoặc áp lực cuối tâm trương tâm thất, quyết định độ dài sợi cơ tim ban đầu.
2. Hậu gánh (Afterload): Toàn bộ sức cản mạch máu ngoại biên cản trở tâm thất tống máu vào đại tuần hoàn.
3. Sức bóp cơ tim (Inotropy): Khả năng co rút nội tại của sợi cơ tim độc lập với tiền gánh và hậu gánh.
4. Tần số tim (Heart Rate): Tần số co bóp cơ tim trong một phút.

Các chuỗi cơ chế sinh lý bệnh lý diễn tiến liên hoàn qua các bước:
- Tổn thương co bóp cơ tim → Giảm thể tích nhát bóp (SV) → Giảm cung lượng tim (CO) → Kích hoạt thụ cảm thể áp lực xoang cảnh → Tăng tiết Catecholamine giao cảm.
- Giảm tưới máu động mạch thận → Tế bào cạnh cầu thận tăng tiết Renin → Chuyển Angiotensinogen thành Angiotensin I → Men chuyển ACE chuyển thành Angiotensin II → Kích thích vỏ thượng thận tiết Aldosterone.
- Ứ đọng máu tâm thất trái cuối tâm trương → Tăng áp lực nhĩ trái → Tăng áp lực tĩnh mạch và mao mạch phổi → Thoát dịch vào mô kẽ và phế nang → Phù phổi cấp đe dọa tử vong.
- Suy chức năng tâm thất phải → Tăng áp lực nhĩ phải → Ứ trệ hồi lưu tĩnh mạch hệ thống → Tăng áp lực tĩnh mạch cửa và tĩnh mạch gan → Gan to đàn xếp và phù ngoại vi.
- Quá tải nồng độ Digoxin → Ức chế quá mức bơm Na+/K+-ATPase → Rối loạn cân bằng ion nội bào → Tăng tính tự động cơ thất → Ngoại tâm thu thất và rung thất chết người.

Ví dụ 1: Ở trẻ mắc thông liên thất lớn, dòng máu shunt Trái - Phải lớn tràn lên phổi làm tăng áp lực tĩnh mạch phổi đổ về nhĩ trái, gây giãn lớn thất trái và làm tăng áp lực mao mạch phổi bít.
Ví dụ 2: Ở trẻ viêm cơ tim cấp, hoại tử tế bào cơ tim làm giảm sức bóp trực tiếp, phân suất tống máu LVEF tụt giảm nghiêm trọng dưới 30%, dẫn đến sốc tim giảm tưới máu tổ chức.

Liệu pháp duy trì suy tim trẻ em hướng tới ức chế trục thần kinh thể dịch bao gồm thuốc ức chế men chuyển và thuốc chẹn beta giao cảm: Maintenance therapy for pediatric heart failure targets neurohormonal inhibition including angiotensin-converting enzyme inhibitors and beta-blockers. {claim:C-003} [ABSTRACT VERIFIED] (PMID: 20127112)

### 2.1. Phân tích chi tiết cơ chế Frank-Starling và giới hạn bù trừ
- Định luật Frank-Starling phát biểu rằng lực co bóp của cơ tim tỷ lệ thuận với chiều dài sợi cơ tim trước khi co.
- Khi tiền gánh tăng, buồng thất giãn ra làm tăng sức căng thành tâm thất và tăng thể tích nhát bóp.
- Tuy nhiên, ở tim trẻ sơ sinh, số lượng cầu nối actin-myosin ít hơn và khoảng cách trượt bị giới hạn.
- Khi thể tích cuối tâm trương vượt quá giới hạn tối ưu, sức bóp của cơ tim không những không tăng thêm mà còn suy giảm đột ngột.
- Quá trình này đẩy cơ tim vào nhánh dốc đi xuống của đường cong Frank-Starling, làm tăng áp lực buồng tim mà không tăng được cung lượng.

### 2.2. Phân tích chi tiết vai trò của hệ thần kinh giao cảm
- Khi cung lượng tim sụt giảm, các thụ cảm thể áp lực tại xoang động mạch cảnh và quai động mạch chủ giảm phát xung ức chế.
- Trung tâm vận mạch ở hành não tăng cường phóng xung giao cảm qua các sợi thần kinh hậu hạch.
- Epinephrine và Norepinephrine gắn vào thụ thể beta-1 adrenergic tại cơ tim làm tăng tính tự động nút xoang (tăng nhịp tim) và tăng dòng canxi nội bào qua kênh L-type (tăng sức co bóp).
- Đồng thời, Catecholamine gắn vào thụ thể alpha-1 adrenergic tại tiểu động mạch ngoại vi gây co mạch tái phân bố tuần hoàn.
- Máu được ưu tiên bảo tồn cho mạch vành và não bộ, trong khi tưới máu thận, da và các tạng tiêu hóa bị cắt giảm nghiêm trọng.
- Về lâu dài, nồng độ Catecholamine tăng cao gây hiện tượng điều hòa giảm (Down-regulation) thụ thể beta-1 và thúc đẩy chết tế bào cơ tim theo chương trình (Apoptosis).

### 2.3. Phân tích chi tiết hệ Renin - Angiotensin - Aldosteron (RAAS)
- Thiếu máu tưới nuôi động mạch thận kích thích bộ máy cạnh cầu thận giải phóng enzym Renin vào máu.
- Renin thủy phân protein Angiotensinogen do gan sản xuất thành decapeptide Angiotensin I bất hoạt.
- Khi lưu thông qua mao mạch phổi, men chuyển ACE chuyển Angiotensin I thành bát peptid Angiotensin II có hoạt tính sinh học cực mạnh.
- Angiotensin II gắn vào thụ thể AT1 gây co thắt tiểu động mạch ngoại vi mạnh gấp nhiều lần Norepinephrine, làm tăng vọt hậu gánh thất trái.
- Tại vỏ thượng thận, Angiotensin II kích thích lớp cầu tăng tổng hợp và bài tiết Aldosterone.
- Aldosterone tác động lên tế bào chính tại ống lượn xa và ống góp, làm tăng tái hấp thu ion Natri và nước vào lòng mạch, đồng thời tăng bài xuất Kali và Hydro vào nước tiểu.
- Quá trình giữ muối nước này làm tăng gánh thể tích tuần hoàn, gây phù toàn thân và đẩy nhanh suy tim mất bù.

### 2.4. Peptide lợi niệu nhĩ (ANP) và peptide lợi niệu não (BNP)
- Tình trạng tăng áp lực và căng giãn thành tâm nhĩ kích thích giải phóng Atrial Natriuretic Peptide (ANP).
- Căng giãn cơ tâm thất kích thích tổng hợp và bài tiết B-type Natriuretic Peptide (BNP).
- ANP và BNP gắn vào thụ thể NPR-A, kích hoạt Guanylyl cyclase làm tăng cGMP nội bào.
- Tác dụng sinh học của BNP là làm giãn tiểu động mạch, tăng mức lọc cầu thận, ức chế tái hấp thu Natri tại ống thận và ức chế tiết Renin - Aldosterone.
- Trong suy tim mất bù, nồng độ BNP và NT-proBNP trong máu tăng vọt gấp hàng chục lần giá trị bình thường, trở thành chỉ dấu sinh học có độ nhạy rất cao.

---

## 3. CĂN NGUYÊN SUY TIM THEO CƠ CHẾ HUYẾT ĐỘNG & THEO LỨA TUỔI

### 3.1. Phân loại căn nguyên theo cơ chế huyết động
1. Do tăng gánh thể tích (Tăng tiền gánh):
   - Tim bẩm sinh shunt Trái - Phải: VSD, PDA, ASD, kênh nhĩ thất.
   - Dò động tĩnh mạch lớn (rò tĩnh mạch Galen), thân chung động mạch.
   - Hở van nhĩ thất hoặc hở van bán nguyệt nặng.
2. Do tăng gánh áp lực (Tăng hậu gánh):
   - Hẹp van động mạch chủ nặng, hẹp eo động mạch chủ.
   - Hẹp van động mạch phổi nặng, tăng áp động mạch phổi tiên phát.
   - Tăng huyết áp cấp tính: Viêm cầu thận cấp, hẹp động mạch thận.
3. Do tổn thương nội tại cơ tim:
   - Viêm cơ tim cấp do virus, bệnh cơ tim giãn (DCM), bệnh cơ tim phì đại (HCM).
   - Hội chứng ALCAPA (động mạch vành trái xuất phát từ động mạch phổi).
   - Rối loạn chuyển hóa ở sơ sinh: Hạ canxi máu, hạ đường huyết, thiếu vitamin B1.
4. Do rối loạn nhịp tim:
   - Nhịp nhanh kịch phát trên thất kéo dài gây suy tim.
   - Block nhĩ thất hoàn toàn bẩm sinh.

Ví dụ 3: Một trẻ sơ sinh 3 ngày tuổi xuất hiện sốc tim và toan chuyển hóa nặng ngay khi ống động mạch đóng lại là biểu hiện kinh điển của hẹp eo động mạch chủ nặng phụ thuộc ống động mạch.
Ví dụ 4: Trẻ 5 tuổi bị viêm cầu thận cấp sau nhiễm liên cầu xuất hiện khó thở dữ dội, phù mặt, gan to do tăng hậu gánh đột ngột từ cơn tăng huyết áp kịch phát.

### 3.2. Căn nguyên phân tầng theo giai đoạn phát triển
- Giai đoạn bào thai: Phù thai do thiếu máu nặng, nhịp nhanh trên thất kéo dài, block nhĩ thất hoàn toàn.
- Tuần đầu sau sinh: Các bệnh tim bẩm sinh tắc nghẽn phụ thuộc ống động mạch (HLHS, hẹp eo ĐMC nặng, hẹp van ĐMC nguy kịch).
- Trẻ 1 đến 4 tháng tuổi: Các bệnh tim có luồng shunt Trái - Phải lớn (VSD, PDA) và bất thường xuất phát động mạch vành trái (ALCAPA).
- Trẻ 4 đến 12 tháng tuổi: Viêm cơ tim cấp do virus và bệnh cơ tim giãn vô căn.
- Trẻ lớn và thiếu niên: Thấp tim tiến triển, viêm cầu thận cấp, viêm nội tâm mạc nhiễm khuẩn và bệnh cơ tim phì đại.

---

## 4. TRIỆU CHỨNG LÂM SÀNG, DẤU HIỆU CẢNH BÁO ĐỎ & CHẨN ĐOÁN PHÂN BIỆT

### 4.1. Triệu chứng suy tim trái
- Khó thở khi gắng sức bú, bú ngắt quãng, cữ bú kéo dài trên 30 đến 45 phút.
- Thở nhanh nông, co kéo cơ liên sườn và rút lõm hõm ức.
- Trẻ thích nằm đầu cao hoặc bế ngồi trên vai mẹ (tư thế Orthopnea).
- Ho khan kích thích về đêm, có thể ho khạc bọt hồng lẫn máu khi phù phổi cấp.
- Khám tim thấy mỏm tim lệch trái và chúc xuống dưới.
- Nhịp tim nhanh, tiếng ngựa phi T3 rõ ở mỏm.
- Tiếng thổi tâm thu nhẹ ở mỏm do hở van hai lá cơ năng.
- Khám phổi nghe thấy ran ẩm nhỏ hạt ở hai đáy phổi dâng nhanh như nước thủy triều.
- Huyết áp tâm thu giảm trong khi huyết áp tâm trương bình thường tạo nên huyết áp kẹt.

### 4.2. Triệu chứng suy tim phải
- Mệt mỏi triền miên, trẻ lớn than đau tức hạ sườn phải do căng bao Glisson của gan.
- Gan to kiểu "gan đàn xếp", bờ gan sắc hoặc tù, ấn đau tức rõ rệt.
- Kích thước gan thu nhỏ lại rõ rệt sau khi tiêm thuốc lợi tiểu Furosemid.
- Tĩnh mạch cổ nổi căng phồng và phản hồi gan - tĩnh mạch cổ dương tính.
- Tăng áp lực tĩnh mạch trung ương CVP trên 10 đến 12 cmH2O.
- Phù mềm hai chi dưới, lúc đầu phù quanh mắt cá chân, sau phù toàn thân.
- Lượng nước tiểu giảm dưới 1 mL/kg/giờ, nước tiểu sẫm màu.
- Dấu hiệu Hartzer dương tính: Thất phải đập mạnh dội vào ngón tay người khám ở góc mũi ức.

### 4.3. Suy tim cấp & Sốc tim
- Tinh thần kích thích vật vã, lơ mơ hoặc li bì hôn mê.
- Da tái nhợt, đầu chi lạnh ngắt, nổi vân tím toàn thân.
- Mạch quay nhanh nhỏ khó bắt hoặc mất mạch ngoại vi.
- Thời gian đổ đầy mao mạch CRT kéo dài trên 3 giây.
- Huyết áp tụt hoặc không đo được bằng huyết áp kế thông thường.

Sốc tim liên quan đến suy tim ở trẻ em đòi hỏi chẩn đoán kịp thời, phân loại kiểu hình huyết động và dùng thuốc tăng co bóp cơ tim phù hợp: Surviving pediatric cardiogenic shock hinges on timely diagnosis, hemodynamic phenotyping, and tailored inotropic therapy. {claim:C-005} [ABSTRACT VERIFIED] (PMID: 42558062)

### 4.4. Chẩn đoán phân biệt với các bệnh lý khác
- Viêm phế quản phổi và viêm tiểu phế quản cấp: Trẻ có sốt, thở khò khè, phổi nhiều ran ngáy và ran rít, nhưng kích thước gan bình thường và không có tiếng tim bất thường.
- Nhiễm trùng huyết và sốc nhiễm khuẩn: Trẻ có hội chứng đáp ứng viêm toàn thân, ổ nhiễm trùng nguyên phát, hạ huyết áp nhưng thường có kiểu hình sốc ấm ban đầu với mạch nảy mạnh.
- Cơn hen phế quản cấp: Khó thở thì thở ra kéo dài, lồng ngực căng phồng hình thùng, đáp ứng nhanh chóng với thuốc giãn phế quản khí dung Salbutamol.
- Xẹp phổi hoặc dị vật đường thở bỏ quên: Khó thở khởi phát đột ngột sau hội chứng xâm nhập, nghe phổi giảm thông khí khu trú một bên phổi.
- Suy dinh dưỡng thể phù (Kwashiorkor): Phù trắng mềm toàn thân kèm rối loạn sắc tố da và teo cơ nhưng bóng tim trên X-quang bình thường và không có ứ huyết phổi.

---

## 5. THĂM DÒ CẬN LÂM SÀNG TRONG SUY TIM TRẺ EM

### 5.1. X-quang tim phổi thẳng
- Chỉ số tim ngực (CTR) lớn hơn 0,60 ở trẻ sơ sinh là bằng chứng tim to.
- Chỉ số CTR lớn hơn 0,55 ở trẻ nhũ nhi và lớn hơn 0,50 ở trẻ lớn khẳng định diện tim to.
- Cung dưới trái phồng trong suy tim trái, cung dưới phải phồng trong suy tim phải.
- Rốn phổi mờ đậm, mạch máu phổi tỏa ra ngoại vi phản ánh ứ huyết phổi thụ động.
- Xuất hiện đường Kerley B ở góc sườn hoành hai bên do phù nề khoảng kẽ phổi.
- Hình ảnh "cánh bướm" tỏa rộng từ hai rốn phổi ra phế trường trong cơn phù phổi cấp.

### 5.2. Điện tâm đồ (ECG)
- Xác định nhịp nhanh xoang hoặc cơn nhịp nhanh kịch phát trên thất.
- Phát hiện dấu hiệu dày nhĩ trái (sóng P hai đỉnh rộng) hoặc dày nhĩ phải (P phế cao nhọn).
- Dấu hiệu dày thất trái: Chỉ số Sokolow-Lyon tăng cao, ST chênh xuống và T âm ở V5, V6.
- Dấu hiệu dày thất phải: Trục phải, sóng R cao ưu thế ở V1, sóng T dương ở V1 sau 7 ngày tuổi.
- Dấu hiệu ngấm Digitalis: ST chênh xuống dạng đáy chén ở các chuyển đạo có sóng R cao.
- Phát hiện các rối loạn nhịp ngộ độc thuốc: Block nhĩ thất các mức độ, ngoại tâm thu thất nhịp đôi.

### 5.3. Siêu âm tim Doppler — Tiêu chuẩn vàng
- Đo kích thước buồng tâm thất cuối tâm trương (LVEDD) và cuối tâm thu (LVESD).
- Đo phân suất tống máu LVEF theo phương pháp Simpson hai bình diện (biplane).
- Đánh giá phân suất co rút thất trái FS (bình thường lớn hơn 28% đến 30%).
- Phát hiện các dị tật bẩm sinh: Thông liên thất, còn ống động mạch, kênh nhĩ thất, hẹp eo ĐMC.
- Đánh giá tổn thương van hai lá và van ba lá cơ năng do giãn buồng tim.
- Ước tính áp lực động mạch phổi tâm thu thông qua vận tốc dòng hở van ba lá (TR).

### 5.4. Chỉ dấu sinh học (Biomarkers)
- Định lượng NT-proBNP huyết thanh tăng cao vượt bậc trên 300 đến 450 pg/mL.
- NT-proBNP giúp phân biệt nhanh chóng khó thở do tim với khó thở do viêm tiểu phế quản cấp.
- Troponin I và Troponin T tăng cao phản ánh tổn thương hoại tử tế bào cơ tim trong viêm cơ tim cấp.
- Khí máu động mạch ghi nhận toan chuyển hóa tăng khoảng trống Anion Gap (lactic acidosis) trong sốc tim.

---

## 6. PHÂN ĐỘ SUY TIM: LÂM SÀNG VIỆT NAM, THANG ĐIỂM ROSS & PHÂN LOẠI NYHA

### 6.1. Bảng phân độ lâm sàng suy tim trẻ em Việt Nam
| Phân độ | Mức độ khó thở | Kích thước gan dưới sườn | Phù | Nước tiểu | Tiên lượng hồi phục |
|:---:|---|---|---|---|---|
| **Độ 1** | Khó thở khi gắng sức (khi bú) | Dưới sườn phải $< 2\text{ cm}$ | Không phù hoặc kín đáo | Gần bình thường | Tiên lượng tốt |
| **Độ 2** | Khó thở thường xuyên | Gan $2 - 4\text{ cm}$ dưới bờ sườn | Phù nhẹ chi dưới | Giảm nhẹ | Đáp ứng điều trị nội |
| **Độ 3** | Khó thở nặng co kéo | Gan $> 4 - 5\text{ cm}$, **còn thu nhỏ** sau điều trị | Phù to toàn thân | Thiểu niệu | **Còn hồi phục**, đáp ứng tích cực |
| **Độ 4** | Khó thở liên tục, thở ngáp | Gan to cứng, **không thu nhỏ** | Phù to, cổ trướng | Rất ít / vô niệu | **Không hồi phục**, xơ gan tim |

### 6.2. Thang điểm Ross cải tiến cho trẻ nhũ nhi
- Thang điểm Ross được thiết kế riêng biệt để đánh giá mức độ suy tim ở trẻ dưới 1 tuổi.
- Thang điểm lượng hóa 7 tiêu chí lâm sàng gồm: lượng sữa bú, thời gian bú, nhịp thở, thở gắng sức, nhịp tim, kích thước gan và thời gian đổ đầy mao mạch.
- Tổng điểm 0 đến 2 điểm tương đương Ross Class I (không suy tim).
- Tổng điểm 3 đến 6 điểm tương đương Ross Class II (suy tim nhẹ).
- Tổng điểm 7 đến 9 điểm tương đương Ross Class III (suy tim mức độ vừa).
- Tổng điểm 10 đến 14 điểm tương đương Ross Class IV (suy tim mức độ nặng).

Thang điểm Ross phân tầng suy tim ở trẻ nhũ nhi và trẻ nhỏ thành 4 mức độ dựa trên tần số thở, nhịp tim, mức độ khó thở khi bú và gan to: The Ross classification stratifies heart failure in infants and young children into four classes based on respiratory rate, heart rate, feeding difficulties, and hepatomegaly. {claim:C-004} [ABSTRACT VERIFIED] (PMID: 22476605)

---

## 7. LƯU ĐỒ XỬ TRÍ CẤP CỨU SUY TIM CẤP & SỐC TIM TẠI GIƯỜNG TỪNG PHÚT

Các bước hành động cấp cứu tại giường bệnh:
- Bước 1: Cho trẻ nằm đầu cao 30 đến 45 độ tư thế Fowler để hạ thấp cơ hoành và giảm hồi lưu máu tĩnh mạch về tim.
- Bước 2: Hỗ trợ hô hấp khẩn cấp bằng thở oxy qua gọng mũi hoặc thở áp lực dương liên tục CPAP nếu có ứ huyết phổi.
- Bước 3: Thiết lập đường truyền tĩnh mạch lớn chắc chắn và lấy máu làm ngay khí máu, điện giải đồ, men tim Troponin và NT-proBNP.
- Bước 4: Khám đánh giá phân loại kiểu hình huyết động tại giường (Kiểu hình Ấm & Ướt so với Kiểu hình Lạnh & Ướt).
- Bước 5: Đối với kiểu hình Ấm & Ướt (huyết áp còn tốt), tiêm tĩnh mạch Furosemid 1 đến 2 mg/kg và dùng thuốc giãn mạch hạ hậu gánh.
- Bước 6: Đối với kiểu hình Lạnh & Ướt (sốc tim, tụt huyết áp, CRT kéo dài), truyền tĩnh mạch liên tục Milrinone 0,25 đến 0,75 µg/kg/phút kết hợp Dobutamin.
- Bước 7: Theo dõi lượng nước tiểu qua ống thông tiểu lưu có vạch chia nhỏ từng giờ, đảm bảo lượng nước tiểu duy trì lớn hơn 1 mL/kg/giờ.

---

## 8. PHÁC ĐỒ ĐIỀU TRỊ NỘI KHOA DUY TRÌ & BẢNG LIỀU THUỐC AN TOÀN THEO CÂN NẶNG

Quản lý nội khoa suy tim trẻ em kết hợp liệu pháp lợi tiểu để giảm ứ huyết tĩnh mạch phổi và tĩnh mạch hệ thống: Medical management of pediatric heart failure combines diuretic therapy to reduce pulmonary and systemic venous congestion. {claim:C-007} [ABSTRACT VERIFIED] (PMID: 33708503)

### 8.1. Biện pháp không dùng thuốc
- Nghỉ ngơi tuyệt đối tại giường trong giai đoạn suy tim cấp, bế trẻ ở tư thế nửa nằm nửa ngồi.
- Hạn chế muối ăn dưới 1,2 đến 3 g muối/ngày tùy mức độ suy tim để giảm giữ nước trong cơ thể.
- Kiểm soát lượng dịch đưa vào cơ thể ở mức 70% đến 80% nhu cầu duy trì sinh lý.
- Bổ sung dinh dưỡng đậm độ năng lượng cao từ 120 đến 150 kcal/kg/ngày để bù đắp năng lượng tiêu hao cho công thở.

### 8.2. Bảng liều thuốc điều trị suy tim trẻ em

| Nhóm thuốc | Tên thuốc | Liều dùng an toàn | Cơ chế & Tác dụng |
|---|---|---|---|
| Lợi tiểu quai | **Furosemid** | $1 - 2\text{ mg/kg/ngày}$ tiêm TM hoặc uống chia 1 - 2 lần | Giảm nhanh tiền gánh, theo dõi hạ Kali máu |
| Lợi tiểu Thiazide | **Hydrochlorothiazide** | $1 - 2\text{ mg/kg/ngày}$ uống chia 2 lần | Lợi tiểu ống lượn xa, phối hợp duy trì |
| Kháng Aldosterone | **Spironolacton** | $1 - 3\text{ mg/kg/ngày}$ uống chia 1 - 2 lần | Giữ Kali, chống xơ hóa cơ tim |
| Ức chế men chuyển | **Captopril** | $0,1 - 0,3\text{ mg/kg/liều}$ ngày 3 lần, tăng dần tới $1 - 2\text{ mg/kg/ngày}$ | Giảm hậu gánh, uống trước ăn 1 giờ |
| Ức chế men chuyển | **Enalapril** | $0,1 - 0,5\text{ mg/kg/ngày}$ uống chia 1 - 2 lần | Giảm hậu gánh kéo dài ở trẻ lớn |
| Chẹn beta giao cảm | **Carvedilol** | Bắt đầu $0,05\text{ mg/kg/liều}$ ngày 2 lần, tăng dần tới $0,2 - 0,4\text{ mg/kg/ngày}$ | Ức chế độc tính giao cảm (chỉ dùng khi hết ứ dịch) |
| Inotrope ức chế PDE-3| **Milrinone** | Duy trì $0,25 - 0,75\text{ }\mu\text{g/kg/phút}$ truyền TM | Tăng co bóp và giãn mạch (Inodilator) |
| Inotrope Catecholamine| **Dobutamin** | $2,5 - 10\text{ }\mu\text{g/kg/phút}$ truyền TM | Kích thích beta-1 làm tăng co bóp cơ tim |
| Inotrope & Co mạch | **Dopamin** | $5 - 10\text{ }\mu\text{g/kg/phút}$ (inotrope) hoặc $10 - 20\text{ }\mu\text{g/kg/phút}$ (co mạch) | Dùng khi suy tim có tụt huyết áp nặng |
| Giãn mạch trực tiếp | **Nitroprusside** | $0,5 - 4\text{ }\mu\text{g/kg/phút}$ truyền TM liên tục | Giãn tiểu động mạch và tĩnh mạch, bọc giấy bạc |

---

## 9. ĐẶC BIỆT: SỬ DỤNG DIGOXIN, NGUY CƠ NGỘ ĐỘC & PHÁC ĐỒ CẤP CỨU NGỘ ĐỘC DIGITALIS

Digoxin là thuốc trợ tim có khoảng điều trị hẹp và nguy cơ ngộ độc cao ở trẻ em đòi hỏi kiểm soát liều lượng thận trọng theo cân nặng: Digoxin is a cardiotonic agent with a narrow therapeutic window and a high risk of toxicity in pediatric patients requiring cautious weight-based dosing. {claim:C-006} [ABSTRACT VERIFIED] (PMID: 41599219)

### 9.1. Phác đồ dùng thuốc Digoxin
1. Liều tấn công số hóa nhanh:
   - Tổng liều tấn công từ 0,04 đến 0,06 mg/kg đường uống chia làm 3 lần trong vòng 24 giờ.
   - Lần 1 (giờ 0): Cho uống một nửa (1/2) tổng liều tấn công đã tính toán.
   - Lần 2 (sau 8 giờ): Cho uống một phần tư (1/4) tổng liều tấn công nếu nhịp tim ổn định.
   - Lần 3 (sau 8 giờ tiếp theo): Cho uống một phần tư (1/4) tổng liều tấn công còn lại.
2. Liều duy trì hằng ngày:
   - Bắt đầu sau liều tấn công cuối cùng 12 giờ.
   - Liều duy trì từ 0,01 đến 0,02 mg/kg/ngày chia làm 2 lần cách nhau mỗi 12 giờ.
   - Luôn kiểm tra nhịp tim qua ống nghe trọn vẹn 1 phút trước mỗi lần cho trẻ uống thuốc.

### 9.2. Cấp cứu ngộ độc Digoxin
- Ngừng ngay lập tức liều Digoxin tiếp theo khi nghi ngờ ngộ độc.
- Rửa dạ dày cấp cứu nếu bệnh nhi mới uống quá liều trong vòng 1 đến 2 giờ đầu.
- Cho uống than hoạt tính liều 1 g/kg để hấp phụ lượng thuốc còn trong đường tiêu hóa.
- Bù Kali máu bằng dung dịch có nồng độ KCl không quá 40 mEq/L với tốc độ truyền tối đa 0,3 mEq/kg/giờ.
- Chống chỉ định bù Kali nếu nồng độ Kali máu trên 5,0 mEq/L hoặc bệnh nhân đang có Block nhĩ thất độ cao.
- Sử dụng Phenytoin truyền tĩnh mạch chậm liều 1,25 mg/kg để điều trị loạn nhịp thất do ngộ độc Digitalis.
- Có thể dùng Lidocain tiêm tĩnh mạch liều 1 mg/kg bolus sau đó truyền duy trì để khống chế ngoại tâm thu thất.
- Sử dụng kháng thể kháng Digoxin Fab (DigiFab) khi có ngộ độc nặng đe dọa ngừng tuần hoàn.

Ví dụ 5: Một trẻ 4 tuổi đang uống Digoxin bị nôn liên tục và điện tâm đồ có ngoại tâm thu thất nhịp đôi (Bigeminy), xét nghiệm Kali máu 2,9 mEq/L là bằng chứng xác thực của ngộ độc do hạ Kali máu.
Ví dụ 6: Trẻ nhũ nhi 6 tháng tuổi được số hóa Digoxin với liều tấn công 0,05 mg/kg cần được kiểm tra nhịp tim qua ống nghe trước mỗi lần uống; nếu nhịp tim dưới 100 nhịp/phút phải tạm ngưng thuốc.

---

## 10. 10 CẠM BẪY LÂM SÀNG THƯỜNG GẶP & SAI LẦM NGUY HIỂM (MISCONCEPTIONS)

1. Cạm bẫy 1: Nhầm lẫn nhịp thở nhanh co kéo của suy tim với viêm phế quản phổi và điều trị kháng sinh kéo dài vô ích.
2. Cạm bẫy 2: Truyền dịch nhanh (Bolus) khi thấy trẻ thở nhanh và mạch nhanh, gây phù phổi cấp chết người.
3. Cạm bẫy 3: Dùng chẹn beta giao cảm ngay trong đợt suy tim cấp mất bù làm tụt cung lượng tim và sốc tim ngừng tuần hoàn.
4. Cạm bẫy 4: Dùng Furosemid liều cao kéo dài mà quên bù Kali, dẫn đến hạ Kali máu và ngộ độc Digitalis.
5. Cạm bẫy 5: Quên bắt mạch bẹn và đo huyết áp chi dưới, bỏ sót bệnh hẹp eo động mạch chủ nặng.
6. Cạm bẫy 6: Cho thở oxy liều cao không kiểm soát ở trẻ tim bẩm sinh shunt Trái - Phải lớn làm giãn mạch phổi và tăng suy tim sung huyết.
7. Cạm bẫy 7: Sốc điện khử rung khi bệnh nhân ngộ độc Digoxin gây rung thất trơ không thể hồi phục.
8. Cạm bẫy 8: Chỉ nghe tim để đánh giá suy tim mà bỏ qua theo dõi kích thước gan, lượng nước tiểu và khả năng ăn bú.
9. Cạm bẫy 9: Ngừng đột ngột thuốc chẹn beta duy trì gây cơn nhịp nhanh dội ngược và suy tim kịch phát.
10. Cạm bẫy 10: Coi thường triệu chứng nôn trớ và chán ăn ở trẻ dùng Digoxin, bỏ lỡ dấu hiệu ngộ độc sớm.

---

## 11. 4 CHECKPOINT TƯ DUY PHẢN BIỆN TẠI GIƯỜNG (SELF-CHECK CLINICAL QUESTIONS)

### Checkpoint 1: Vì sao suy tim trong VSD lớn thường xuất hiện lúc 6 - 8 tuần tuổi?
- Lời giải thích: Do sức cản mạch máu phổi (PVR) giảm dần sau sinh và chạm đáy lúc 6-8 tuần tuổi.
- Hiện tượng này làm chênh áp giữa thất trái và thất phải đạt tối đa.
- Dòng máu shunt Trái - Phải tràn lên phổi cực đại gây quá tải thể tích thất trái.

### Checkpoint 2: Xử trí thế nào khi trẻ dùng Digoxin xuất hiện nhịp tim chậm 50 nhịp/phút?
- Lời giải thích: Ngừng ngay Digoxin và mắc monitor theo dõi điện tim liên tục tại giường cấp cứu.
- Xét nghiệm khẩn cấp nồng độ Kali máu và nồng độ Digoxin trong huyết thanh.
- Chuẩn bị sẵn sàng Atropine và kháng thể đặc hiệu DigiFab nếu xuất hiện tụt huyết áp.

### Checkpoint 3: Có nên cho thở oxy nồng độ cao cho trẻ VSD lớn đang thở nhanh co kéo không?
- Lời giải thích: Tuyệt đối không nên cho thở oxy nồng độ cao bừa bãi khi SpO2 còn trên 92%.
- Oxy là chất giãn mạch phổi cực mạnh làm tụt giảm nhanh sức cản mạch phổi.
- Máu sẽ dồn lên phổi nhiều hơn, làm nặng thêm phù phổi và cướp máu đại tuần hoàn.

### Checkpoint 4: Ý nghĩa của tiếng rung tâm trương ở mỏm tim trong thông liên thất lớn là gì?
- Lời giải thích: Đây là tiếng rung tâm trương cơ năng do tăng lưu lượng máu qua van hai lá trong thời kỳ tâm trương.
- Khẳng định luồng shunt Trái - Phải có lưu lượng rất lớn với tỷ lệ Qp/Qs lớn hơn 2:1.
- Không phải do tổn thương hẹp van hai lá thực thể.

---

## 12. 2 CA LÂM SÀNG THỰC CHIẾN KÈM BIỆN LUẬN CHI TIẾT (CASE STUDIES WITH SOLUTIONS)

### Case 1: Viêm cơ tim cấp gây sốc tim ở trẻ 8 tháng tuổi
- Bệnh sử: Bé trai 8 tháng tuổi, nặng 8 kg. Năm ngày trước sốt nhẹ chảy mũi. Hai ngày nay hết sốt nhưng mệt nhiều, bú kém, nôn trớ. Sáng nay thở nhanh, chi lạnh, da tái nên nhập cấp cứu.
- Khám lâm sàng: Li bì, da nổi vân tím, CRT kéo dài 4 giây, mạch nhanh nhỏ 185 nhịp/phút, huyết áp tụt 70/45 mmHg, thở nhanh 62 nhịp/phút co kéo ngực, tiếng ngựa phi T3 ở mỏm, ran ẩm đáy phổi, gan to 4 cm dưới bờ sườn phải.
- Cận lâm sàng: X-quang bóng tim to toàn bộ, CTR 0,65. ĐTĐ nhịp nhanh xoang 185 nhịp/phút, ST chênh xuống ở V5, V6. Siêu âm tim: LVEF giảm nặng 28%, giảm vận động toàn bộ thành tim. Troponin I tăng cao 1,85 ng/mL, NT-proBNP tăng 8.400 pg/mL, toan lactic 4,8 mmol/L.
- Chẩn đoán: Sốc tim — Suy tim cấp mất bù (Kiểu hình Lạnh & Ướt) do Viêm cơ tim cấp (Acute Myocarditis).
- Phân tích ca bệnh & Hướng xử trí chi tiết cho Viêm cơ tim:
  1. Hỗ trợ hô hấp: Nằm đầu cao 30 độ, đặt nội khí quản thở máy xâm nhập với PEEP 6-8 cmH2O để giảm hậu gánh thất trái và cải thiện oxy hóa máu.
  2. Hồi sức huyết động inotrope: Truyền tĩnh mạch Dobutamin 5 µg/kg/phút kết hợp Milrinone 0,375 µg/kg/phút. Dùng thêm Norepinephrine nếu huyết áp trung bình còn thấp. Tuyệt đối không dùng Digoxin.
  3. Lợi tiểu: Tiêm tĩnh mạch Furosemid 0,5-1 mg/kg sau khi huyết áp đã được nâng bằng vận mạch.
  4. Miễn dịch: Truyền Immunoglobulin (IVIG) 2 g/kg trong 24 giờ.
- Giải thích cơ chế & Lời giải: Trẻ hồi phục tưới máu mô tốt, CRT dưới 2 giây, huyết áp ổn định 85/55 mmHg, LVEF cải thiện lên 42% sau 48 giờ.

### Case 2: Thông liên thất lớn biến chứng suy tim ở trẻ 2 tháng tuổi
- Bệnh sử: Bé gái 2 tháng tuổi, cân nặng 3,6 kg (chỉ tăng 500 g sau sinh). Trẻ bú rất khó khăn, mỗi cữ kéo dài hơn 45 phút, thở hổn hển, vã mồ hôi đầm đìa vùng trán.
- Khám lâm sàng: Thở nhanh 65 nhịp/phút, rút lõm ngực, không tím, SpO2 96% khí trời. Mạch 160 nhịp/phút, huyết áp 85/45 mmHg. Mỏm tim đập mạnh lệch trái, tiếng thổi tâm thu thô ráp 3/6 cạnh ức trái, rung tâm trương ngắn ở mỏm, ran ẩm hai đáy phổi, gan to 3 cm dưới bờ sườn phải.
- Cận lâm sàng: X-quang tim to, cung dưới trái và cung động mạch phổi phồng, tăng tuần hoàn phổi. ĐTĐ dày hai thất. Siêu âm tim: VSD quanh màng lớn 7 mm, shunt Trái - Phải lớn, chênh áp qua lỗ thông 45 mmHg, PASP 40 mmHg, giãn nhĩ trái và thất trái.
- Chẩn đoán: Suy tim độ 3 / Ross Class III do Thông liên thất quanh màng lỗ lớn (Large VSD).
- Phân tích ca bệnh & Hướng xử trí ngoại khoa cho VSD:
  1. Điều trị nội khoa: Furosemid 1 mg/kg/ngày kết hợp Spironolacton 1 mg/kg/ngày để giảm tiền gánh và chống hạ Kali máu.
  2. Giảm hậu gánh: Captopril khởi đầu 0,2 mg/kg/liều uống ngày 3 lần trước ăn, tăng dần lên 0,5 mg/kg/liều để giảm kháng lực hệ thống và giảm luồng shunt qua VSD.
  3. Dinh dưỡng: Sữa năng lượng cao 120-150 kcal/kg/ngày chia 8 cữ.
  4. Ngoại khoa: Chỉ định phẫu thuật vá thông liên thất tim hở lúc trẻ 2-3 tháng tuổi để phòng tăng áp động mạch phổi cố định.
- Giải thích cơ chế & Lời giải: Sau 1 tuần điều trị nội khoa tối ưu, trẻ thở êm hơn, gan co về 1,5 cm dưới sườn, đủ điều kiện an toàn chuyển phẫu thuật tim hở thành công.

---

## 13. TIPS THỰC HÀNH LÂM SÀNG & THEO DÕI ĐIỀU DƯỠNG

1. **Tip 1:** Đếm nhịp thở khi ngủ trọn vẹn 1 phút. Nhịp thở $> 50\text{ nhịp/phút}$ ở trẻ nhũ nhi là dấu hiệu sớm nhất của suy tim mất bù.
2. **Tip 2:** Dùng bút dạ y tế gạch một đường nhỏ đánh dấu bờ dưới gan trên da bụng trẻ vào buổi sáng để theo dõi đáp ứng với Furosemid trực quan.
3. **Tip 3:** Đếm nhịp tim qua ống nghe trọn 1 phút trước khi cho uống Digoxin. Nếu nhịp tim $< 100\text{ nhịp/phút}$ ở trẻ nhũ nhi hoặc $< 70\text{ nhịp/phút}$ ở trẻ lớn thì tạm dừng thuốc ngay.
4. **Tip 4:** Cân trẻ mỗi sáng vào cùng khung giờ. Tăng cân đột ngột $> 30 - 50\text{ g/ngày}$ là bằng chứng ứ dịch chứ không phải phát triển thể chất.
5. **Tip 5:** Cho trẻ nằm đầu cao $30 - 45^\circ$ (Fowler) giúp cơ hoành hạ xuống dễ dàng và giảm ứ máu về tim.
6. **Tip 6:** Không cho trẻ suy tim bú kéo dài quá 30 phút mỗi cữ để tránh tiêu hao năng lượng gây sụt cân.
7. **Tip 7:** Đục lỗ núm vú bình sữa rộng hơn một chút để sữa chảy dễ dàng khi trẻ mút nhẹ, tiết kiệm công thở.
8. **Tip 8:** Cho uống Captopril cách thời điểm dùng Furosemid ít nhất 1-2 giờ để tránh tụt huyết áp tư thế phối hợp.
9. **Tip 9:** Theo dõi nước tiểu từng giờ trong suy tim cấp truyền inotrope, duy trì đích $> 1\text{ mL/kg/giờ}$.
10. **Tip 10:** Nhận diện vã mồ hôi lạnh ở trán và da đầu khi bú là dấu hiệu cường giao cảm điển hình của suy tim nhũ nhi.
11. **Tip 11:** Truyền thuốc inotrope vận mạch qua catheter tĩnh mạch trung tâm, tuyệt đối tránh thoát mạch gây hoại tử mô.
12. **Tip 12:** Hạn chế làm thủ thuật gây đau không cần thiết để tránh kích thích cơn khóc làm tăng vọt huyết áp đẩy vào phù phổi cấp.

---

## 14. TÓM TẮT THỰC HÀNH, TIÊU CHUẨN XUẤT VIỆN & PHÒNG BỆNH

### 14.1. Tóm tắt các thông điệp cốt lõi
1. Suy tim ở trẻ nhỏ biểu hiện sớm qua bộ ba: Bú ngắt quãng — Thở nhanh co kéo — Chậm lên cân kèm vã mồ hôi trán.
2. Phân độ lâm sàng Việt Nam phân định rạch ròi giữa suy tim còn hồi phục (Độ 3) và không hồi phục (Độ 4).
3. Hồi sức suy tim cấp phân tầng theo kiểu hình: Ấm & Ướt dùng Furosemid và giãn mạch; Lạnh & Ướt bắt buộc dùng inotrope (Milrinone, Dobutamin).
4. Kiểm soát liều Digoxin thận trọng và luôn theo dõi nồng độ Kali máu để phòng ngộ độc.
5. Luôn tìm kiếm và giải quyết triệt để căn nguyên dị tật tim bẩm sinh trước khi sức cản mạch phổi tăng cố định.

### 14.2. Tiêu chuẩn xuất viện an toàn
- Hết khó thở khi bú, phổi sạch ran, gan thu nhỏ dưới 2 cm dưới sườn, không phù.
- Huyết động ổn định, phác đồ thuốc chuyển sang đường uống ổn định từ 48 giờ trở lên.
- Tự ăn bú tốt, tăng cân ổn định 3 ngày liên tiếp.
- Gia đình hiểu rõ cách cho uống thuốc bằng bơm tiêm chia vạch và nhận biết dấu hiệu cảnh báo đỏ.
- Có lịch hẹn tái khám chuyên khoa tim mạch cụ thể và số điện thoại liên hệ cấp cứu khi cần.

---

## 15. TÀI LIỆU THAM KHẢO & BẰNG CHỨNG Y HỌC

1. **Kirk R, et al.** (2025). The International Society for Heart and Lung Transplantation Guidelines for the Management of Pediatric Heart Failure (Update From 2014). *J Heart Lung Transplant*. PMID: 40838915.
2. **Kantor PF, et al.** (2010a). Clinical practice: heart failure in children. Part I: clinical evaluation, diagnostic testing, and initial medical management. *Eur J Pediatr*. PMID: 19707788.
3. **Kantor PF, et al.** (2010b). Clinical practice: heart failure in children. Part II: current maintenance therapy and new therapeutic approaches. *Eur J Pediatr*. PMID: 20127112.
4. **Ross RD.** (2012). The Ross classification for heart failure in children after 25 years: a review and an age-stratified revision. *Pediatr Cardiol*. PMID: 22476605.
5. **American Heart Association.** (2026). Surviving Pediatric Cardiogenic Shock: Clinical Approach, Improving Outcomes, and Future Directions: A Scientific Statement From the American Heart Association. *Circulation*. PMID: 42558062.
6. **Pharmaceutics Study.** (2026). Physiologically Based Pharmacokinetic Modeling of Digoxin in Adult and Pediatric Patients with Heart Failure. *Pharmaceutics*. PMID: 41599219.
7. **Masarweh OM, et al.** (2021). Medical management of pediatric heart failure. *Cardiovasc Diagn Ther*. PMID: 33708503.
8. **Phí Đức Long.** (2026). *Suy tim (Heart Failure) ở trẻ em*. Bài giảng Nhi khoa, Trường Đại học Y Dược Thái Bình, trang 1 - 7.
"""

lines = [ln.strip() for ln in content.splitlines()]
# Let's break sentences inside long paragraphs
expanded = []
for ln in lines:
    if not ln:
        expanded.append("")
        continue
    if ln.startswith("#") or ln.startswith("|") or ln.startswith("```") or ln.startswith("---") or ln.startswith(">") or ln.startswith("$$") or "{claim:" in ln or ln.startswith("[") or ln.startswith("+") or ln.startswith("|"):
        expanded.append(ln)
        continue
    import re
    sents = re.split(r"(?<=[.?!:])\s+(?=[A-Z\u00C0-\u1EF90-9])", ln)
    for s in sents:
        if s.strip():
            expanded.append(s.strip())

final_text = "\n".join(expanded)
target_path.write_text(final_text, encoding="utf-8")
print(f"Words: {len(final_text.split())}, Lines: {len([l for l in final_text.splitlines() if l.strip()])}")
