# -*- coding: utf-8 -*-
"""Generate comprehensive PED-07 lesson markdown."""
import sys
from pathlib import Path

target_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh")
out_file = target_dir / "PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md"

content = """# PED-07: CO GIẬT DO SỐT & TRẠNG THÁI ĐỘNG KINH Ở TRẺ EM

> **Chuyên khoa:** Cấp cứu Nhi khoa - Thần kinh Nhi (Pediatric Emergency & Child Neurology)  
> **Mã bài học:** PED-07 (Nhi khoa Lâm sàng Toàn diện - Block 01: Hồi sức - Cấp cứu - Chống độc)  
> **Đối tượng:** Bác sĩ Nội trú Nhi khoa, Bác sĩ Cấp cứu, Bác sĩ Nhi tổng quát, Học viên Sau đại học  
> **Phiên bản:** 2026-09-16_RELEASE_v1  
> **Tiêu chuẩn kiểm định:** Evidence-Based Medicine (EBM) - 10 Verified PMIDs - 16 Offline Release Gates

---

## 1. Tổng quan & Nền tảng tối thiểu cần dùng ngay

### 1.1 Tổng quan lâm sàng
Co giật do sốt (Febrile Seizures - FS) là tình trạng co giật thường gặp nhất ở lứa tuổi nhũ nhi và trẻ nhỏ, ảnh hưởng từ 2% đến 5% trẻ em trong độ tuổi từ 6 đến 60 tháng theo hướng dẫn của Viện Hàn lâm Nhi khoa Hoa Kỳ AAP 2008 (PMID: 18519501) [DATA VERIFIED]. Co giật do sốt xảy ra khi thân nhiệt tăng cao (thường ≥ 38.0°C hoặc 100.4°F) nhưng không có bằng chứng của nhiễm khuẩn hệ thần kinh trung ương (viêm màng não, viêm não), không có rối loạn điện giải hoặc chuyển hóa cấp tính, và không có tiền sử co giật không do sốt trước đó.

Hầu hết các cơn co giật do sốt là lành tính, tự giới hạn trong vòng dưới 5 phút và không để lại di chứng thần kinh lâu dài. Tuy nhiên, khi cơn co giật kéo dài ≥ 5 phút, nguy cơ tiến triển thành Trạng thái động kinh co giật (Convulsive Status Epilepticus - CSE) hoặc Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE) tăng vọt. Theo khuyến cáo của Hội Động kinh Hoa Kỳ AES 2016 (PMID: 26900382) [GUIDELINE VERIFIED], mốc thời gian t1 = 5 phút là thời điểm bắt buộc phải can thiệp cấp cứu cắt cơn ngay lập tức bằng thuốc cắt cơn bước 1 (Benzodiazepine), và mốc t2 = 30 phút là thời điểm bắt đầu xuất hiện tổn thương tế bào thần kinh không hồi phục và suy đa cơ quan.

Nghiên cứu theo dõi dài hạn 10 năm FEBSTAT (PMID: 38606600) [DATA VERIFIED] đã chỉ ra rằng trạng thái động kinh do sốt kéo dài có thể gây tổn thương phù nề cấp tính vùng hải mã và tiến triển thành xơ teo hải mã (Hippocampal Sclerosis) ở 10 trong số 14 trẻ có tổn thương MRI ban đầu, tạo ổ sinh động kinh gây động kinh thùy thái dương kháng trị trong tương lai. Do đó, việc nắm vững lưu đồ cấp cứu phân tầng theo từng phút là sinh mạng của bệnh nhi.

### 1.2 Nền tảng tối thiểu cần dùng ngay (Actionable Prerequisite at Bedside)
Khi tiếp nhận một trẻ đang có cơn co giật hoặc vừa trải qua cơn giật kèm sốt tại phòng cấp cứu, bác sĩ lâm sàng cần thực hiện ngay lập tức 5 hành động phản xạ không điều kiện sau:

1. **Định vị an toàn & Khai thông đường thở (Positioning & Airway):**
   - Đặt trẻ nằm nghiêng sang một bên (tư thế hồi sức an toàn - Recovery position) trên mặt phẳng êm, đầu hơi ngửa để đờm dãi chảy ra ngoài tự nhiên, chống hít sặc dịch nôn vào phổi.
   - Hút sạch đờm dãi, chất nôn ở khoang miệng hầu họng nhẹ nhàng bằng ống hút mềm.
   - Cung cấp oxy qua mask có túi dự trữ 10–15 L/phút hoặc cannula 2–4 L/phút để duy trì SpO2 ≥ 94%.
   - **Tuyệt đối không:** Chèn ngón tay, đũa, muỗng, gạc hoặc bất kỳ vật cứng nào vào miệng trẻ. Co thắt cơ cắn khi co giật có thể làm gãy răng, chấn thương mô mềm hầu họng và tạo dị vật đường thở gây tử vong.

2. **Đo ngay đường huyết mao mạch tại giường (Immediate Point-of-Care Blood Glucose):**
   - Co giật có thể là biểu hiện của hạ đường huyết nặng (Blood Glucose < 2.6 mmol/L hoặc < 45–50 mg/dL). Nếu hạ đường huyết, xử trí cấp cứu ngay bằng Bolus tĩnh mạch Glucose 10% liều 2 mL/kg (0.2 g/kg), sau đó duy trì dịch truyền tĩnh mạch có Glucose.

3. **Bấm giờ chính xác thời gian cơn giật (Clock the Seizure):**
   - Ghi nhận chính xác số phút cơn giật diễn ra. Nếu cơn giật kéo dài ≥ 5 phút, kích hoạt ngay quy trình cấp cứu Trạng thái động kinh bước 1 theo AES 2016 (PMID: 26900382) [GUIDELINE VERIFIED].

4. **Chuẩn bị thuốc cắt cơn Benzodiazepine đầu tay:**
   - Nếu chưa có đường truyền tĩnh mạch: Dùng Midazolam tiêm bắp (IM) liều 0.2 mg/kg (tối đa 10 mg) theo bằng chứng vượt trội từ thử nghiệm RAMPART (PMID: 22335736) [DATA VERIFIED], hoặc Diazepam bơm hậu môn 0.5 mg/kg (trẻ < 2 tuổi) / 0.3–0.5 mg/kg (trẻ ≥ 2 tuổi).
   - Nếu đã có đường truyền tĩnh mạch sẵn: Dùng Diazepam tiêm tĩnh mạch chậm 0.15–0.2 mg/kg (tối đa 10 mg, tốc độ tiêm không quá 1–2 mg/phút) hoặc Midazolam IV 0.1–0.15 mg/kg.

5. **Hạ sốt & Đánh giá tìm ổ nhiễm trùng:**
   - Cởi bớt quần áo, lau mát bằng nước ấm (nhiệt độ nước thấp hơn thân nhiệt trẻ 1–2°C).
   - Đặt hậu môn Paracetamol liều 10–15 mg/kg nếu trẻ chưa uống được, giúp hạ sốt và giảm nguy cơ tái phát co giật trong cùng đợt sốt theo thử nghiệm Murata 2018 (PMID: 30297499) [DATA VERIFIED].

---

## 2. Định nghĩa & Phân loại lâm sàng chuẩn xác

### 2.1 Định nghĩa chính thức
Theo đồng thuận của Viện Hàn lâm Nhi khoa Hoa Kỳ AAP 2008 (PMID: 18519501) [GUIDELINE VERIFIED], Liên đoàn Quốc tế Chống Động kinh (ILAE) và Tổ chức Y tế Thế giới (WHO):

> **Co giật do sốt (Febrile Seizure):** Là một cơn co giật xảy ra ở trẻ em trong độ tuổi từ 6 đến 60 tháng (đỉnh điểm từ 12 đến 18 tháng tuổi), có liên quan đến sốt (thân nhiệt ≥ 38.0°C), nhưng không có bằng chứng của nhiễm khuẩn hệ thần kinh trung ương (như viêm màng não, viêm não, áp xe não), không có rối loạn chuyển hóa toàn thân cấp tính có thể gây co giật (hạ đường huyết, hạ natri máu, hạ canxi máu), và không có tiền sử co giật không do sốt trước đó.

### 2.2 Phân loại co giật do sốt: Đơn thuần vs Phức hợp
Việc phân loại chính xác giữa thể Đơn thuần và Phức hợp có ý nghĩa sống còn trong việc quyết định chỉ định cận lâm sàng, thời gian theo dõi tại viện và tiên lượng tiến triển thành bệnh động kinh sau này.

| Đặc điểm lâm sàng | Co giật do sốt Đơn thuần (Simple FS) | Co giật do sốt Phức hợp (Complex FS) |
|---|---|---|
| **Tỷ lệ gặp** | Chiếm đa số (70–80%) | Chiếm thiểu số (20–30%) |
| **Tính chất cơn giật** | Co giật toàn thể (Generalized): co cứng - co giật hai bên đối xứng | Co giật cục bộ (Focal): giật một chi, nửa người, mắt liếc một bên, méo miệng |
| **Thời gian cơn giật** | Cơn ngắn: kéo dài < 15 phút (thường < 5 phút) | Cơn kéo dài: ≥ 15 phút |
| **Tần số trong 24 giờ** | Chỉ xuất hiện 1 cơn duy nhất trong vòng 24 giờ (hoặc trong 1 đợt sốt) | Tái phát ≥ 2 cơn trong vòng 24 giờ (hoặc tái phát trong cùng đợt bệnh) |
| **Dấu thần kinh sau giật** | Trẻ tỉnh lại hoàn toàn nhanh chóng, không có liệt khu trú | Có thể có dấu liệt Todd sau giật (liệt thoáng qua một chi hoặc nửa người) |
| **Tiền căn thần kinh** | Trẻ phát triển thể chất và tinh thần vận động hoàn toàn bình thường | Có thể có chậm phát triển tâm vận, dị tật thần kinh bẩm sinh kèm theo |
| **Nguy cơ động kinh tương lai** | Rất thấp: khoảng 1–2% (tương đương dân số nói chung ~ 1%) | Tăng cao: từ 4% đến 10–15% nếu có nhiều yếu tố phức hợp |

### 2.3 Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE)
- **Định nghĩa:** Là một thể đặc biệt nghiêm trọng của co giật do sốt phức hợp, trong đó cơn co giật kéo dài liên tục ≥ 30 phút, hoặc hai hay nhiều cơn co giật liên tiếp kéo dài tổng cộng ≥ 30 phút mà tri giác của trẻ không hồi phục hoàn toàn giữa các cơn.
- **Dịch tễ học:** Chiếm khoảng 5% tổng số các trường hợp co giật do sốt. FSE là nguyên nhân gây ra khoảng một phần ba (33%) tất cả các ca trạng thái động kinh ở trẻ em dưới 2 tuổi.
- **Ý nghĩa bệnh lý:** FSE là một cấp cứu thần kinh nội khoa tối khẩn cấp. Thời gian co giật kéo dài liên tục trên 30 phút gây tổn thương tế bào thần kinh do độc tính kích thích glutamate (excitotoxicity), thiếu oxy não cục bộ và viêm thần kinh cấp tính, để lại di chứng thực thể nặng nề.

---

## 3. Cơ chế sinh lý bệnh học & Sinh động kinh

Sự xuất hiện của co giật do sốt ở trẻ nhỏ là kết quả của sự tương tác phức tạp giữa: (1) Tính nhạy cảm nhiệt của não bộ chưa trưởng thành; (2) Các yếu tố di truyền điều biến kênh ion và thụ thể dẫn truyền; và (3) Các cytokine tiền viêm được giải phóng trong phản ứng sốt.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 SỐT CẤP TÍNH (Nhiễm virus hô hấp, HHV-6, Cúm, Sởi)          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
┌───────────────────────────────┐             ┌───────────────────────────────┐
│ GIẢI PHÓNG CYTOKINE TIỀN VIÊM │             │ TĂNG THÔNG KHÍ DO SỐT CAO     │
│  - IL-1β, TNF-α, IL-6 tại não │             │  - Thở nhanh thải trừ CO2     │
│  - Tăng tính thấm hàng rào não│             │  - Giảm PaCO2 → Kiềm hô hấp   │
│  - Kích hoạt dòng thụ thể NMDA│             │  - pH máu và não tăng kiềm    │
└───────────────┬───────────────┘             └───────────────┬───────────────┘
                │                                             │
                └──────────────────────┬──────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│          MẤT CÂN BẰNG HỆ THỐNG DẪN TRUYỀN THẦN KINH TẠI NÃO TRẺ             │
│   • Tăng phóng thích Glutamate (chất dẫn truyền kích thích)                 │
│   • Tăng nhạy cảm kênh NMDA / AMPA với Glutamate do kiềm hóa não            │
│   • Đột biến nhạy cảm nhiệt kênh Na+ (SCN1A) & giảm chức năng GABA-A        │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PHÓNG ĐIỆN ĐỒNG THÌ BẤT THƯỜNG DIỆN RỘNG                    │
│   • Vỏ não và cấu trúc hải mã (Hippocampus) bị kích thích kịch phát         │
│   • CƠN CO GIẬT CO CỨNG - CO GIẬT TOÀN THỂ BÙNG PHÁT                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Chuỗi cơ chế 1: Sự chưa trưởng thành của não bộ trẻ nhỏ & Ngưỡng co giật
1. Ở lứa tuổi từ 6 đến 60 tháng, hệ thần kinh trung ương của trẻ đang trong giai đoạn phát triển và tái tổ chức synap cực kỳ mạnh mẽ (synaptogenesis).
2. Trong giai đoạn này, hệ thống dẫn truyền kích thích (sử dụng chất dẫn truyền thần kinh Glutamate) phát triển sớm hơn và chiếm ưu thế vượt trội so với hệ thống ức chế (sử dụng GABA).
3. Thụ thể GABA-A ở não nhũ nhi trong một số cấu trúc dưới vỏ còn có thể đóng vai trò khử cực kích thích do nồng độ ion Cl⁻ nội bào cao hơn ngoại bào (do biểu hiện kênh đồng vận NKCC1 cao hơn KCC2).
4. Khi thân nhiệt tăng nhanh đột ngột, tốc độ chuyển hóa tế bào thần kinh tăng vọt, tiêu thụ oxy và glucose tăng cao, làm giảm ngưỡng chịu đựng phóng điện của màng tế bào nơ-ron, tạo điều kiện thuận lợi cho sự bùng nổ phóng điện đồng thì.

### 3.2 Chuỗi cơ chế 2: Cytokine tiền viêm và tính nhạy cảm nhiệt của kênh ion
1. Khi nhiễm trùng ngoại vi (thường gặp nhất là nhiễm virus như Human Herpesvirus 6 [HHV-6], Influenza, Parainfluenza, Adenovirus, Enterovirus), các tế bào miễn dịch tiết ra các cytokine gây sốt nội sinh gồm Interleukin-1 beta (IL-1β), Tumor Necrosis Factor-alpha (TNF-α) và Interleukin-6 (IL-6).
2. Các cytokine này tác động lên trung tâm điều nhiệt ở vùng dưới đồi làm tăng điểm đặt nhiệt (set-point), đồng thời kích thích các thụ thể cytokine trên tế bào nội mô mạch máu não và tế bào thần kinh đệm (astrocytes, microglia).
3. IL-1β trực tiếp ức chế dòng ức chế qua thụ thể GABA-A và tăng cường dẫn truyền kích thích qua thụ thể NMDA, gây kích thích thần kinh quá mức.
4. Yếu tố di truyền đóng vai trò cốt lõi: Các đột biến điểm hoặc đa hình trên gen mã hóa kênh Natri phụ thuộc điện thế Nav1.1 (*SCN1A*, *SCN1B*) hoặc tiểu đơn vị thụ thể GABA (*GABRG2*) làm cho kênh ion trở nên cực kỳ nhạy cảm với nhiệt độ (thermosensitive). Khi nhiệt độ tăng, kênh Natri chậm khử hoạt hoặc kênh GABA giảm mở kênh Clo, dẫn đến khử cực màng tế bào kéo dài và khởi phát cơn giật.

### 3.3 Chuỗi cơ chế 3: Tăng thông khí gây kiềm hô hấp và kích thích thụ thể NMDA
1. Khi nhiệt độ cơ thể tăng cao, trung tâm hô hấp ở hành não bị kích thích trực tiếp gây thở nhanh sâu (hyperventilation).
2. Tăng thông khí dẫn đến đào thải quá mức CO2, gây giảm phân áp PaCO2 máu động mạch và kiềm hô hấp cấp tính.
3. Vì phân tử CO2 khuếch tán rất nhanh qua hàng rào máu não, nồng độ H⁺ trong dịch kẽ não giảm mạnh, gây kiềm hóa môi trường ngoại bào thần kinh.
4. Môi trường kiềm hóa làm mất đi sự ức chế sinh lý của ion H⁺ lên thụ thể NMDA, làm mở rộng lỗ kênh NMDA và cho phép dòng ion Ca²⁺ ồ ạt tràn vào trong nơ-ron, gây khử cực bùng nổ diện rộng tại vỏ não và hồi hải mã.

### 3.4 Cơ chế tổn thương hồi hải mã và sinh động kinh (Epileptogenesis in FSE)
Khi cơn co giật do sốt kéo dài trên 30 phút (Febrile Status Epilepticus - FSE), cân bằng chuyển hóa bị phá vỡ hoàn toàn:
1. Dòng Ca²⁺ nội bào tràn ngập kích hoạt các enzyme phân giải protein (calpain, caspase) và các gốc oxy hóa tự do (ROS), gây tổn thương ty thể và chết tế bào thần kinh theo chương trình (apoptosis) cũng như hoại tử tế bào tại các vùng nhạy cảm nhất của não, đặc biệt là phân vùng CA1, CA3 và hồi răng (dentate gyrus) của hồi hải mã.
2. Hình ảnh MRI sọ não cấp tính trong nghiên cứu FEBSTAT (PMID: 40770931) [DATA VERIFIED] ghi nhận hiện tượng tăng tín hiệu T2 (T2 signal hyperintensity) một bên hồi hải mã đi kèm phù nề cấp tính.
3. Sau giai đoạn cấp, quá trình viêm thần kinh mạn tính và tái tổ chức sợi trục bất thường (mossy fiber sprouting) diễn ra trong nhiều tháng đến nhiều năm.
4. Nghiên cứu FEBSTAT 10 năm (PMID: 38606600) [DATA VERIFIED] chứng minh rằng 10 trong số 14 trẻ có tổn thương T2 ban đầu đã tiến triển thành xơ teo hồi hải mã thực thể (definite hippocampal sclerosis), hình thành mạng lưới nơ-ron dẫn truyền kích thích tự duy trì gây ra bệnh động kinh thùy thái dương kháng trị (Mesial Temporal Lobe Epilepsy - MTLE).

---

## 4. Chẩn đoán lâm sàng & Lưu đồ cận lâm sàng AAP 2011

### 4.1 Đánh giá lâm sàng toàn diện
Mục tiêu hàng đầu của đánh giá lâm sàng khi tiếp cận trẻ co giật có sốt là:
1. **Xác định cơn co giật:** Khai thác bệnh sử chi tiết từ người chứng kiến (tính chất co cứng, co giật, giật cục bộ hay toàn thể, mắt liếc, sùi bọt mép, tím tái, thời gian kéo dài bao nhiêu phút, trẻ có tỉnh lại hoàn toàn hay li bì sau cơn).
2. **Loại trừ nhiễm khuẩn thần kinh trung ương:** Khám phát hiện các dấu hiệu màng não (thóp phồng ở trẻ nhũ nhi, cổ gượng, dấu Kernig, dấu Brudzinski) và dấu hiệu thần kinh khu trú.
3. **Tìm kiếm ổ nhiễm trùng nguyên phát:** Khám kỹ tai mũi họng (viêm tai giữa cấp, viêm họng mủ), đường hô hấp (viêm phế quản, viêm phổi), tiêu hóa (tiêu chảy nhiễm trùng do Shigella, Salmonella), tiết niệu và da.

### 4.2 Hướng dẫn cận lâm sàng của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2011)
Hướng dẫn thực hành lâm sàng của AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED] đưa ra các khuyến cáo chuẩn mực nhằm giảm thiểu các thủ thuật xâm lấn và can thiệp không cần thiết cho trẻ co giật do sốt đơn thuần:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 TRẺ 6 - 60 THÁNG CO GIẬT CÓ SỐT CẤP TÍNH                   │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
                     ┌───────────────────────────────────┐
                     │ PHÂN LOẠI THỂ CO GIẬT LÂM SÀNG   │
                     └─────────────────┬─────────────────┘
                                       │
        ┌──────────────────────────────┴──────────────────────────────┐
        ▼                                                             ▼
┌──────────────────────────────────┐        ┌──────────────────────────────────┐
│  CO GIẬT DO SỐT ĐƠN THUẦN        │        │   CO GIẬT DO SỐT PHỨC HỢP        │
│  - Toàn thể, < 15 phút           │        │   - Cục bộ, HOẶC ≥ 15 phút,      │
│  - 1 cơn duy nhất trong 24h      │        │   - HOẶC ≥ 2 cơn trong 24h       │
└───────────────┬──────────────────┘        └─────────────────┬────────────────┘
                │                                             │
                ▼                                             ▼
┌──────────────────────────────────┐        ┌──────────────────────────────────┐
│ ĐÁNH GIÁ NGUY CƠ NHIỄM KHUẨN TKTW│        │ • Xem xét chọc dò tủy sống (LP)  │
│ 1. Dấu màng não / Khám thần kinh │        │ • Xét nghiệm tìm căn nguyên      │
│ 2. Tiền sử tiêm chủng Hib, Phế cầu│       │ • Đo EEG nếu giật cục bộ/kéo dài │
│ 3. Đang điều trị kháng sinh trước│        │ • Xem xét MRI não nếu có dấu khu │
└───────────────┬──────────────────┘        │   trú hoặc chậm phát triển       │
                │                           └──────────────────────────────────┘
    ┌───────────┴───────────┐
    ▼                       ▼
【CÓ CỜ ĐỎ / NGUY CƠ】   【KHÔNG CÓ CỜ ĐỎ】
• Có dấu màng não       • Toàn trạng tỉnh táo
• Thóp phồng            • Tiêm đủ Hib, Phế cầu
• Li bì, kích thích     • Khám thần kinh bình thường
• Đã dùng kháng sinh    • Có ổ nhiễm trùng rõ
    │                       │
    ▼                       ▼
┌──────────────────────┐┌──────────────────────────────────────────────┐
│ BẮT BUỘC CHỌC DÒ     ││ KHÔNG CHỈ ĐỊNH THƯỜNG QUY (AAP 2011):        │
│ TỦY SỐNG (LP) NGAY   ││ 1. Không chọc dò tủy sống (LP) thường quy    │
│ ĐỂ LOẠI TRỪ VIÊM     ││ 2. Không đo điện não đồ (EEG) thường quy     │
│ MÀNG NÃO NHIỄM KHUẨN ││ 3. Không chụp CT / MRI sọ não thường quy     │
└──────────────────────┘│ 4. Chỉ xét nghiệm máu khi cần tìm ổ nhiễm    │
                        └──────────────────────────────────────────────┘
```

#### 1. Chọc dò tủy sống (Lumbar Puncture - LP)
- **Khuyến cáo AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED]:** Không chỉ định thường quy chọc dò tủy sống cho trẻ có cơn co giật do sốt đơn thuần nếu trẻ tỉnh táo, toàn trạng tốt và đã tiêm chủng vắc xin đầy đủ phòng ngừa *Haemophilus influenzae* type b (Hib) và Phế cầu khuẩn (*Streptococcus pneumoniae*).
- **Chỉ định bắt buộc chọc dò tủy sống:**
  1. Trẻ có bất kỳ triệu chứng hoặc dấu hiệu màng não nào (thóp phồng, cổ cứng, dấu Kernig, dấu Brudzinski).
  2. Bệnh sử hoặc thăm khám lâm sàng gợi ý nhiễm trùng thần kinh trung ương (li bì kéo dài sau cơn giật, hôn mê, kích thích vật vã không dỗ được).
  3. Trẻ từ 6 đến 12 tháng tuổi có tình trạng tiêm chủng Hib hoặc Phế cầu chưa đầy đủ hoặc không rõ tiền sử tiêm chủng.
  4. Trẻ đã được điều trị kháng sinh trước đó: Kháng sinh có thể làm che lấp các dấu hiệu kinh điển của viêm màng não nhiễm khuẩn (viêm màng não cụt đầu).

#### 2. Điện não đồ (Electroencephalography - EEG)
- **Khuyến cáo AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED]:** Không chỉ định đo điện não đồ thường quy cho trẻ có phát triển thần kinh bình thường sau một cơn co giật do sốt đơn thuần.
- **Lý do khoa học:** Nhiều trẻ bình thường có thể có sóng chậm hoặc phóng điện dạng động kinh thoáng qua sau sốt, nhưng các sóng này không có giá trị tiên đoán nguy cơ tái phát co giật do sốt hay nguy cơ phát triển thành bệnh động kinh. Làm EEG tràn lan gây hoang mang tâm lý không đáng có cho gia đình và dẫn đến điều trị thuốc quá mức.
- **Chỉ định EEG:** Chỉ đo khi trẻ có co giật do sốt phức hợp (đặc biệt là cơn giật cục bộ), trạng thái động kinh do sốt, hoặc trẻ có bất thường thần kinh thực thể từ trước.

#### 3. Chẩn đoán hình ảnh thần kinh (Neuroimaging: CT / MRI sọ não)
- **Khuyến cáo AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED]:** Không chỉ định thường quy chụp CT hoặc MRI sọ não sau cơn co giật do sốt đơn thuần.
- **Lý do khoa học:** Chụp CT sọ não khiến trẻ phải phơi nhiễm với bức xạ ion hóa nguy hiểm làm tăng nguy cơ ung thư sau này, trong khi MRI đòi hỏi phải an thần hoặc gây mê tĩnh mạch ở trẻ nhỏ. Tỷ lệ phát hiện tổn thương ngoại khoa can thiệp được ở trẻ co giật do sốt đơn thuần là xấp xỉ 0%.
- **Chỉ định chụp:** Chỉ chụp khi nghi ngờ tăng áp lực nội sọ, chấn thương sọ não đi kèm, trẻ có dấu hiệu thần kinh khu trú kéo dài, hoặc trạng thái động kinh do sốt không đáp ứng thuốc.

#### 4. Xét nghiệm máu và điện giải
- Không khuyến cáo làm công thức máu, điện giải đồ, canxi máu thường quy cho mọi trẻ co giật do sốt đơn thuần trừ khi trẻ có triệu chứng mất nước nặng do nôn ói, tiêu chảy kéo dài hoặc nghi ngờ rối loạn chuyển hóa.

---

## 5. Tiếp cận & Xử trí cấp cứu Trạng thái động kinh AES 2016

Trạng thái động kinh co giật (Convulsive Status Epilepticus - CSE) ở trẻ em đòi hỏi phải xử trí theo nguyên tắc "thời gian là tế bào não" (Time is Brain). Phác đồ điều trị 4 giai đoạn chuẩn của Hội Động kinh Hoa Kỳ AES 2016 (PMID: 26900382) [GUIDELINE VERIFIED] được thiết kế phân định rõ ràng theo từng mốc thời gian cụ thể:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│             LƯU ĐỒ CẤP CỨU CẮT CƠN TRẠNG THÁI ĐỘNG KINH AES 2016            │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 0 - 5 PHÚT: HỒI SỨC BAN ĐẦU & ỔN ĐỊNH BỆNH NHI                   │
│ • Kiểm soát đường thở (Airway), thở oxy qua mask có túi dự trữ (Breathing)   │
│ • Theo dõi mạch, huyết áp, điện tim, SpO2 (Circulation)                     │
│ • Bấm giờ chính xác cơn giật; đo ngay Đường huyết mao mạch tại giường       │
│ • Nếu Đường huyết < 2.6 mmol/L: Bolus Glucose 10% 2 mL/kg tĩnh mạch          │
│ • Thiết lập đường truyền tĩnh mạch (IV) hoặc chuẩn bị tiêm bắp (IM)         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Cơn giật kéo dài ≥ 5 phút
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 5 - 20 PHÚT (BƯỚC 1): LIỆU PHÁP BENZODIAZEPINE ĐẦU TAY            │
│ ─────────────────────────────────────────────────────────────────────────── │
│ LỰA CHỌN A (CHƯA CÓ ĐƯỜNG TRUYỀN IV) - Khuyến cáo ưu tiên RAMPART:          │
│  ► Midazolam tiêm bắp (IM): 0.2 mg/kg (Tối đa: 10 mg)                       │
│  ► Hoặc Diazepam bơm hậu môn: 0.2 - 0.5 mg/kg (dung dịch trực tràng)       │
│                                                                             │
│ LỰA CHỌN B (ĐÃ CÓ ĐƯỜNG TRUYỀN IV):                                         │
│  ► Lorazepam tiêm tĩnh mạch: 0.1 mg/kg (Tối đa: 4 mg, tiêm chậm 2 phút)     │
│  ► Hoặc Diazepam tiêm tĩnh mạch: 0.15 - 0.2 mg/kg (Tối đa: 10 mg)           │
│                                                                             │
│ ⚠️ Đánh giá lại sau 5 phút: Nếu cơn giật chưa ngừng, lặp lại liều thứ 2     │
│    (Chỉ lặp lại duy nhất 1 lần; chuẩn bị bóng Ambu và dụng cụ NKQ)          │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Cơn giật kéo dài ≥ 20 phút (Refractory to BZD)
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 20 - 40 PHÚT (BƯỚC 2): THUỐC CHỐNG ĐỘNG KINH TIÊM TĨNH MẠCH BẬC 2 │
│ ─────────────────────────────────────────────────────────────────────────── │
│ Chọn 1 trong 3 thuốc sau (Hiệu quả tương đương theo ESETT, ConSEPT, EcLiPSE):│
│                                                                             │
│ 1. LEVETIRACETAM (Keppra) IV - Lựa chọn ưu tiên an toàn tim mạch:           │
│    • Liều: 60 mg/kg truyền tĩnh mạch (Tối đa: 4500 mg) trong 10 - 15 phút   │
│                                                                             │
│ 2. FOSPHENYTOIN IV (hoặc Phenytoin IV):                                     │
│    • Fosphenytoin: 20 mg PE/kg (Tối đa: 1500 mg PE) truyền tĩnh mạch         │
│    • Phenytoin: 20 mg/kg pha NaCl 0.9% truyền tốc độ ≤ 1 mg/kg/phút         │
│      (CẦN THEO DÕI MONITOR ĐIỆN TIM VÀ HUYẾT ÁP LIÊN TỤC)                   │
│                                                                             │
│ 3. VALPROATE NATRI (Depakine) IV:                                           │
│    • Liều: 40 mg/kg truyền tĩnh mạch (Tối đa: 3000 mg) trong 10 - 15 phút   │
│      (CHỐNG CHỈ ĐỊNH: Trẻ < 2 tuổi nghi ngờ bệnh ty thể/đột biến POLG)     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │ Cơn giật kéo dài ≥ 40 phút
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ GIAI ĐOẠN 40 - 60 PHÚT (BƯỚC 3): TRẠNG THÁI ĐỘNG KINH KHÁNG TRỊ (RSE)       │
│ • Đặt nội khí quản thở máy xâm lấn, hồi sức tích cực tại ICU                │
│ • Gây mê toàn thân: Midazolam truyền liên tục, Propofol, hoặc Ketamine      │
│ • Theo dõi điện não đồ liên tục (Continuous cEEG) nhằm dập tắt đợt bùng nổ │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Giai đoạn 0–5 phút: Ổn định ban đầu
- Hồi sức theo nguyên tắc ABCDE (Airway - Breathing - Circulation - Disability - Exposure).
- Khai thông đường thở, hút đờm dãi, thở oxy lưu lượng cao qua mask có túi dự trữ.
- Đo ngay đường huyết mao mạch. Nếu Glucose < 2.6 mmol/L, tiêm tĩnh mạch Glucose 10% liều 2 mL/kg.
- Gắn monitor theo dõi nhịp tim, huyết áp, SpO2 và nhiệt độ liên tục.

### 5.2 Giai đoạn 5–20 phút: Thuốc cắt cơn bước 1 (Benzodiazepines)
Theo AES 2016 (PMID: 26900382) [GUIDELINE VERIFIED], Benzodiazepine là nhóm thuốc cắt cơn đầu tay bắt buộc:
- **Midazolam tiêm bắp (IM):** Liều 0.2 mg/kg (tối đa 10 mg). Đây là lựa chọn hàng đầu khi chưa có đường truyền tĩnh mạch, được chứng minh qua thử nghiệm RAMPART (PMID: 22335736) [DATA VERIFIED] là cắt cơn nhanh hơn và hiệu quả hơn so với việc cố gắng lấy ven để tiêm tĩnh mạch Lorazepam.
- **Lorazepam tiêm tĩnh mạch (IV):** Liều 0.1 mg/kg (tối đa 4 mg), tiêm chậm trong 2 phút.
- **Diazepam tiêm tĩnh mạch (IV):** Liều 0.15–0.2 mg/kg (tối đa 10 mg), tiêm chậm 1–2 mg/phút.
- **Diazepam bơm trực tràng:** Dùng dạng gel hoặc dung dịch bơm hậu môn liều 0.2–0.5 mg/kg nếu không có Midazolam tiêm bắp và chưa có ven.
- *Lưu ý quan trọng:* Nếu sau 5 phút cơn giật chưa dứt, có thể lặp lại một liều Benzodiazepine tương tự lần 2. Không dùng quá 2 liều Benzodiazepine vì nguy cơ ức chế hô hấp và tụt huyết áp tăng vọt.

### 5.3 Giai đoạn 20–40 phút: Thuốc chống động kinh tiêm tĩnh mạch bước 2
Nếu cơn giật kéo dài ≥ 20 phút sau khi đã dùng đủ 2 liều Benzodiazepine, kích hoạt ngay bước 2:
1. **Levetiracetam (Keppra) IV:** Liều 60 mg/kg (tối đa 4500 mg) pha trong NaCl 0.9% truyền tĩnh mạch trong 10–15 phút. Ưu điểm nổi bật: an toàn tim mạch, không gây tụt huyết áp hay loạn nhịp, thời gian truyền nhanh.
2. **Fosphenytoin IV / Phenytoin IV:** Liều 20 mg PE/kg (Fosphenytoin, tối đa 1500 mg PE) hoặc Phenytoin 20 mg/kg pha NaCl 0.9% truyền tốc độ không quá 1 mg/kg/phút (tối đa 50 mg/phút). Bắt buộc gắn monitor theo dõi điện tim liên tục để phát hiện block nhĩ thất, kéo dài đoạn QT và tụt huyết áp.
3. **Valproate natri (Depakine) IV:** Liều 40 mg/kg (tối đa 3000 mg) pha truyền tĩnh mạch trong 10 phút. Chống chỉ định ở trẻ nghi ngờ bệnh ty thể.

### 5.4 Giai đoạn 40–60 phút: Trạng thái động kinh kháng trị (RSE)
Cơn giật kéo dài trên 40 phút được xếp vào nhóm kháng trị (Refractory Status Epilepticus):
- Khẩn trương đặt nội khí quản thở máy để bảo vệ đường thở.
- Chuyển khoa Hồi sức tích cực Nhi (PICU).
- Khởi động thuốc mê truyền tĩnh mạch liên tục: Midazolam truyền liên tục (0.05–2 mg/kg/giờ), Propofol (1–5 mg/kg/giờ), hoặc Ketamine.
- Mắc điện não đồ liên tục (continuous EEG - cEEG) để theo dõi và điều chỉnh liều thuốc mê đạt mục tiêu triệt tiêu phóng điện kịch phát (Burst Suppression Pattern).

---

## 6. Bằng chứng thử nghiệm lâm sàng ngẫu nhiên đối chứng (RCT Evidence)

Các quyết định điều trị co giật do sốt và trạng thái động kinh trong y học hiện đại được định hình bởi các thử nghiệm lâm sàng ngẫu nhiên đối chứng (RCT) then chốt sau:

### 6.1 Thử nghiệm RAMPART (NEJM 2012) - Midazolam tiêm bắp vs Lorazepam tiêm tĩnh mạch
- **Nghiên cứu:** Silbergleit R và cộng sự (PMID: 22335736) [DATA VERIFIED] thực hiện thử nghiệm ngẫu nhiên mù đôi đa trung tâm trên 893 bệnh nhân co giật kéo dài ≥ 5 phút tại hiện trường trước khi vào viện.
- **Kết quả:** Tỷ lệ cắt cơn thành công trước khi đến viện ở nhóm dùng Midazolam tiêm bắp (IM) đạt 73.4% (329/448) so với nhóm dùng Lorazepam tiêm tĩnh mạch (IV) là 63.4% (282/445), chênh lệch tuyệt đối 10 percentage points (95% CI 4.0 đến 16.1, p < 0.001 cho cả tính không thua kém và tính vượt trội).
- **Ý nghĩa lâm sàng:** Thời gian trung vị từ khi nhân viên y tế tiếp cận đến khi đưa được thuốc vào cơ thể ở nhóm IM là 1.2 phút so với 4.8 phút ở nhóm IV (tiết kiệm được gần 4 phút quý giá do không phải loay hoay tìm ven). Tỷ lệ đặt nội khí quản giữa 2 nhóm tương đương nhau (14.1% IM vs 14.4% IV). Bằng chứng này khẳng định Midazolam tiêm bắp là lựa chọn tối ưu tại cộng đồng và cơ sở y tế ban đầu.

### 6.2 Thử nghiệm ESETT (NEJM 2019) - So sánh 3 thuốc chống động kinh bước 2
- **Nghiên cứu:** Kapur J và cộng sự (PMID: 31774955) [DATA VERIFIED] thực hiện thử nghiệm ngẫu nhiên mù đôi đa trung tâm (ESETT) trên 384 bệnh nhân (gồm trẻ em và người lớn) bị trạng thái động kinh kháng Benzodiazepine.
- **Kết quả:** Tỷ lệ cắt cơn và hồi phục tri giác tại thời điểm 60 phút không có sự khác biệt có ý nghĩa thống kê giữa 3 nhóm:
  - Levetiracetam 60 mg/kg: đạt 47% (68/145; 95% credible interval 39 đến 55).
  - Fosphenytoin 20 mg PE/kg: đạt 45% (53/118; 95% credible interval 36 đến 54).
  - Valproate natri 40 mg/kg: đạt 46% (56/121; 95% credible interval 38 đến 55).
- **Ý nghĩa lâm sàng:** Cả ba thuốc đều có hiệu quả tương đương (~ 45–47%) và độ an toàn tương tự nhau. Tuy nhiên, Levetiracetam được nhiều bác sĩ nhi khoa ưa chuộng hơn do truyền nhanh hơn (10 phút) và hoàn toàn không gây độc tính tim mạch hay tụt huyết áp như Phenytoin.

### 6.3 Thử nghiệm ConSEPT & EcLiPSE (Lancet 2019) - Levetiracetam vs Phenytoin ở trẻ em
Hai thử nghiệm ngẫu nhiên đối chứng độc lập được công bố song song trên tạp chí *The Lancet* năm 2019:
1. **Thử nghiệm ConSEPT (Úc & New Zealand):** Babl FE và cộng sự (PMID: 31005386) [DATA VERIFIED] trên 233 trẻ em từ 3 tháng đến 16 tuổi. Tỷ lệ cắt cơn sau 5 phút truyền xong thuốc giữa Levetiracetam 40 mg/kg đạt 50% (60/119) so với Phenytoin 20 mg/kg đạt 60% (68/114), chênh lệch nguy cơ -9.2% (95% CI -21.9 đến 3.5, p = 0.16), không có ý nghĩa thống kê.
2. **Thử nghiệm EcLiPSE (Vương quốc Anh):** Lyttle MD và cộng sự (PMID: 31005385) [DATA VERIFIED] trên 286 trẻ từ 6 tháng đến dưới 18 tuổi. Tỷ lệ thành công của Levetiracetam 40 mg/kg là 70% (106/152) so với Phenytoin 20 mg/kg là 64% (86/134), thời gian trung vị từ khi bắt đầu can thiệp đến khi cắt cơn là 35 phút ở nhóm Levetiracetam so với 45 phút ở nhóm Phenytoin.
- **Kết luận đồng thuận:** Levetiracetam có hiệu quả tương đương Phenytoin nhưng vượt trội về tính dễ chuẩn bị, tốc độ truyền nhanh và ít biến chứng tại đường truyền, củng cố vị thế của Levetiracetam là lựa chọn hàng đầu bước 2 tại các khoa cấp cứu nhi.

### 6.4 Thử nghiệm Murata 2018 (Pediatrics) - Vai trò của thuốc hạ sốt
- **Nghiên cứu:** Murata S và cộng sự (PMID: 30297499) [DATA VERIFIED] tiến hành thử nghiệm lâm sàng ngẫu nhiên đối chứng trên 423 trẻ em từ 6 đến 60 tháng tuổi bị co giật do sốt.
- **Phương pháp:** Nhóm can thiệp (n=219) được dùng Paracetamol đặt hậu môn liều 10 mg/kg mỗi 6 giờ trong 24 giờ đầu sau cơn giật nếu nhiệt độ > 38.0°C; nhóm đối chứng (n=204) không dùng hạ sốt thường quy.
- **Kết quả:** Tỷ lệ tái phát co giật trong cùng đợt sốt ở nhóm dùng Paracetamol đặt hậu môn thấp hơn có ý nghĩa thống kê: 9.1% so với 23.5% ở nhóm không dùng hạ sốt (p < 0.001; OR = 5.6, 95% CI 2.3 đến 13.3).
- **Ý nghĩa lâm sàng:** Paracetamol đặt hậu môn đúng liều mỗi 6 giờ giúp hạ nhiệt độ ổn định và giảm tỷ lệ tái phát co giật sớm trong 24 giờ đầu của cùng một đợt sốt. Tuy nhiên, phụ huynh cần được giải thích rõ: thuốc hạ sốt không ngăn ngừa được co giật trong các đợt sốt khác trong tương lai.

---

## 7. Theo dõi dài hạn, Tiên lượng & Phục hồi chức năng

### 7.1 Nguy cơ tái phát co giật do sốt
Khoảng 30–35% trẻ bị co giật do sốt sẽ trải qua ít nhất 1 đợt tái phát trong những đợt sốt sau. Các yếu tố nguy cơ chính làm tăng tỷ lệ tái phát bao gồm:
1. **Tuổi khởi phát cơn đầu tiên nhỏ:** Trẻ < 12–15 tháng tuổi có tỷ lệ tái phát lên tới 50%.
2. **Nhiệt độ khi co giật thấp:** Co giật xảy ra khi thân nhiệt mới chỉ sốt nhẹ (38.0–38.5°C).
3. **Thời gian sốt ngắn trước giật:** Cơn co giật xuất hiện trong vòng < 1 giờ kể từ khi bắt đầu sốt.
4. **Tiền sử gia đình:** Có người thân trực hệ (bố mẹ, anh chị em ruột) từng bị co giật do sốt.
- Trẻ có cả 4 yếu tố trên có tỷ lệ tái phát > 70%; trẻ không có yếu tố nào chỉ có tỷ lệ tái phát < 15%.

### 7.2 Nguy cơ phát triển thành bệnh động kinh thực sự (Epilepsy)
Ở trẻ co giật do sốt đơn thuần, tỷ lệ tiến triển thành bệnh động kinh sau này chỉ khoảng 1–2%, xấp xỉ tỷ lệ mắc động kinh tự nhiên trong dân số chung. Tuy nhiên, tỷ lệ này tăng lên đáng kể (4–15%) nếu trẻ có các yếu tố sau:
1. Co giật do sốt thể phức hợp (cơn cục bộ, kéo dài ≥ 15 phút, hoặc lặp lại trong 24 giờ).
2. Có bất thường phát triển tâm thần vận động hoặc dị tật thần kinh trước cơn giật đầu tiên.
3. Tiền sử gia đình có người thân bị bệnh động kinh không do sốt.
4. Trạng thái động kinh do sốt (FSE kéo dài ≥ 30 phút).

### 7.3 Bằng chứng từ nghiên cứu FEBSTAT 10 năm (Epilepsia 2024)
Nghiên cứu FEBSTAT (PMID: 40770931, PMID: 38606600) [DATA VERIFIED] theo dõi dọc trên 200 trẻ có trạng thái động kinh do sốt (FSE) trong suốt 10 năm đã làm sáng tỏ mối quan hệ nhân quả:
- Trong số các trẻ có tổn thương tăng tín hiệu T2 hồi hải mã trên MRI cấp tính, có 10 trên 14 trẻ (71.4%) tiến triển thành xơ teo hồi hải mã thực thể (definite hippocampal sclerosis) kéo dài suốt 10 năm.
- Có 44 trẻ trong đoàn hệ phát triển thành bệnh động kinh thực sự, trong đó 6 trẻ phát triển thành động kinh thùy thái dương trong (Mesial Temporal Lobe Epilepsy).
- Phát hiện này nhấn mạnh: Trạng thái động kinh do sốt không đơn thuần là một cơn sốt co giật lành tính kéo dài, mà là một biến cố thần kinh nghiêm trọng có thể khởi động quá trình sinh động kinh mạn tính.

### 7.4 Hướng dẫn AAP 2008 về quản lý dài hạn
Theo hướng dẫn của AAP 2008 (PMID: 18519501) [GUIDELINE VERIFIED]:
- **Không khuyến cáo điều trị dự phòng bằng thuốc chống động kinh:** Các thuốc như Phenobarbital, Valproate, Carbamazepine hay Phenytoin KHÔNG được khuyến cáo sử dụng thường quy ngắt quãng hoặc liên tục cho trẻ co giật do sốt đơn thuần.
- **Lý do:** Mặc dù Phenobarbital và Valproate có thể làm giảm số cơn tái phát, nhưng chúng KHÔNG làm giảm nguy cơ phát triển thành bệnh động kinh sau này. Ngược lại, Phenobarbital gây rối loạn hành vi, giảm khả năng tập trung và giảm sút nhận thức ở trẻ; Valproate có nguy cơ gây viêm gan nhiễm độc cấp, viêm tụy cấp và tử vong.
- **Tư vấn gia đình:** Hướng dẫn phụ huynh cách xử trí tại nhà khi trẻ sốt (dùng hạ sốt đúng liều, bù đủ nước) và cách sơ cứu an toàn khi trẻ lên cơn giật (nằm nghiêng, không nhét vật cứng vào miệng, bấm giờ và đưa trẻ đến viện nếu giật quá 5 phút).

---

## 8. Box an toàn & Cảnh báo bẫy tử vong (Box đỏ)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BOX ĐỎ - CẢNH BÁO AN TOÀN TỐI KHẨN                    │
│           (RED BOX - CRITICAL SAFETY RULES & FATAL CLINICAL PITFALLS)       │
└─────────────────────────────────────────────────────────────────────────────┘

🔴 1. TUYỆT ĐỐI CẤM CHÈN BẤT KỲ VẬT CỨNG NÀO VÀO MIỆNG TRẺ ĐANG CO GIẬT:
   • Không dùng muỗng, đũa, ngón tay, que đè lưỡi chèn vào miệng trẻ.
   • Co thắt cơ cắn khi giật cực mạnh có thể bẻ gãy răng rơi vào thanh quản
     gây tắc nghẽn đường thở tử vong, hoặc dập nát niêm mạc khoang miệng.
   • Lưỡi không bao giờ tự tụt xuống gây nghẹt nếu trẻ được đặt nằm nghiêng an toàn!

🔴 2. TUYỆT ĐỐI CẤM TIÊM TĨNH MẠCH NHANH PHENYTOIN KHÔNG KIỂM SOÁT:
   • Tiêm bolus tĩnh mạch nhanh Phenytoin có thể gây trụy tim mạch tức thì, block
     dẫn truyền nhĩ thất cấp độ 3, rung thất và tử vong trên bàn cấp cứu.
   • Phenytoin chỉ được pha trong NaCl 0.9% (tuyệt đối không pha trong Glucose vì
     gây tủa thuốc lập tức), tốc độ truyền tối đa ≤ 1 mg/kg/phút (max 50 mg/phút).
   • Hiện tượng thoát mạch Phenytoin gây hoại tử thiếu máu mô nặng nề (Hội chứng
     bàn tay tím - Purple Glove Syndrome) dẫn đến nguy cơ phải đoạn chi!

🔴 3. TUYỆT ĐỐI CẤM DÙNG VALPROATE CHO TRẺ < 2 TUỔI NGHI BỆNH TY THỂ:
   • Trẻ dưới 2 tuổi có chậm phát triển tâm thần vận động hoặc nghi ngờ rối loạn
     chuyển hóa/bệnh ty thể (đột biến gen POLG - Hội chứng Alpers-Huttenlocher):
     Dùng Valproate natri sẽ khởi phát cơn suy gan cấp bùng phát hoại tử tế bào
     gan dẫn đến tử vong trong 100% các trường hợp!

🔴 4. TUYỆT ĐỐI CẤM BỎ QUA DẤU HIỆU VIÊM MÀNG NÃO CỤT ĐẦU DO ĐÃ DÙNG KHÁNG SINH:
   • Trẻ đã uống kháng sinh ngoại trú vài ngày trước khi co giật có thể không còn
     dấu cổ gượng hay sốt cao rầm rộ. Bắt buộc phải chọc dò tủy sống (LP) để kiểm
     tra tế bào và sinh hóa dịch não tủy, không được chủ quan xếp vào co giật do sốt!

🔴 5. TUYỆT ĐỐI CẤM LẠM DỤNG BENZODIAZEPINE QUÁ 2 LIỀU LIÊN TIẾP:
   • Dùng liên tiếp nhiều liều Diazepam/Midazolam không làm tăng tỷ lệ cắt cơn mà
     làm tăng gấp 4 lần nguy cơ ức chế trung tâm hô hấp và trụy mạch, buộc phải
     đặt nội khí quản thở máy cấp cứu. Nếu 2 liều BZD thất bại, chuyển ngay sang bước 2!
```

---

## 9. Tóm tắt cốt lõi & Lưu đồ hành động nhanh

### 9.1 Mười nguyên tắc vàng ghi nhớ (Ten Golden Takeaways)
1. Co giật do sốt ảnh hưởng 2% đến 5% trẻ từ 6 đến 60 tháng tuổi; đa số là thể đơn thuần lành tính (PMID: 18519501) [DATA VERIFIED].
2. Phân loại đơn thuần vs phức hợp quyết định toàn bộ hướng tiếp cận cận lâm sàng và tiên lượng lâu dài.
3. Cơn giật ≥ 5 phút là mốc t1 bắt buộc phải can thiệp cắt cơn; cơn giật ≥ 30 phút là mốc t2 bắt đầu gây hoại tử tế bào não (AES 2016 - PMID: 26900382) [GUIDELINE VERIFIED].
4. Đặt trẻ nằm nghiêng an toàn, tuyệt đối không nhét bất kỳ vật cứng nào vào miệng trẻ.
5. Đo ngay đường huyết mao mạch để loại trừ hạ đường huyết trước khi dùng thuốc hướng thần.
6. Midazolam tiêm bắp (0.2 mg/kg, max 10 mg) là lựa chọn hàng đầu trước viện hoặc khi chưa có ven tĩnh mạch (RAMPART - PMID: 22335736) [DATA VERIFIED].
7. Thuốc chống động kinh bước 2 gồm Levetiracetam (60 mg/kg), Fosphenytoin (20 mg PE/kg) và Valproate (40 mg/kg) có hiệu quả tương đương nhau (ESETT - PMID: 31774955) [DATA VERIFIED].
8. Không chỉ định thường quy chọc dò tủy sống, EEG và CT/MRI sọ não cho trẻ co giật do sốt đơn thuần đã tiêm chủng đầy đủ (AAP 2011 - PMID: 21285335) [GUIDELINE VERIFIED].
9. Không điều trị dự phòng kéo dài bằng Phenobarbital hay Valproate cho co giật do sốt đơn thuần vì độc tính vượt trội lợi ích (AAP 2008 - PMID: 18519501) [GUIDELINE VERIFIED].
10. Paracetamol đặt hậu môn 10 mg/kg mỗi 6 giờ giúp giảm tái phát co giật trong 24 giờ đầu của cùng đợt sốt (Murata 2018 - PMID: 30297499) [DATA VERIFIED].

### 9.2 Lưu đồ hành động nhanh tại giường bệnh (Rapid Bedside Flowchart)
```text
CƠN CO GIẬT KÈM SỐT Ở TRẺ NHỎ (TẠI PHÒNG CẤP CỨU)
│
├── Phút 0 - 5: ỔN ĐỊNH BAN ĐẦU
│   ├── Nằm nghiêng an toàn + Thở oxy mask 10-15 L/p
│   ├── Đo Đường huyết mao mạch (Glucose 10% 2 mL/kg nếu < 2.6 mmol/L)
│   └── Bấm giờ chính xác cơn giật
│
├── Phút 5 - 20: BƯỚC 1 (BENZODIAZEPINE)
│   ├── Chưa có ven: Midazolam IM 0.2 mg/kg (max 10 mg)
│   ├── Đã có ven: Lorazepam IV 0.1 mg/kg HOẶC Diazepam IV 0.2 mg/kg
│   └── Chưa ngừng sau 5 phút: Lặp lại liều thứ 2 DUY NHẤT
│
├── Phút 20 - 40: BƯỚC 2 (THUỐC CHỐNG ĐỘNG KINH TĨNH MẠCH)
│   ├── Lựa chọn 1: Levetiracetam IV 60 mg/kg truyền trong 10-15 phút (Ưu tiên)
│   ├── Lựa chọn 2: Fosphenytoin IV 20 mg PE/kg (theo dõi monitor ECG)
│   └── Lựa chọn 3: Valproate natri IV 40 mg/kg (tránh trẻ < 2 tuổi nghi ty thể)
│
└── Phút 40 - 60: BƯỚC 3 (TRẠNG THÁI ĐỘNG KINH KHÁNG TRỊ)
    ├── Đặt nội khí quản thở máy xâm lấn
    ├── Chuyển PICU hồi sức tích cực
    └── Truyền Midazolam liên tục / Gây mê Propofol / cEEG
```

---

## 10. Tips thực hành lâm sàng & Xử trí tình huống (Tips)

1. **Tip 1 - Tính liều Midazolam tiêm bắp siêu tốc:** Với nồng độ Midazolam ống 5 mg/mL, liều tiêm bắp 0.2 mg/kg tương đương với thể tích 0.04 mL/kg (ví dụ: trẻ 10 kg tiêm 0.4 mL, trẻ 15 kg tiêm 0.6 mL).
2. **Tip 2 - Xử trí khi không tiêm bắp được:** Nếu không có Midazolam tiêm bắp và ven khó lấy, có thể dùng Midazolam dạng tiêm nhỏ niêm mạc mũi (Intranasal) hoặc nhỏ niêm mạc má (Buccal) với liều 0.2–0.3 mg/kg, thuốc hấp thu rất nhanh qua hệ mao mạch dồi dào.
3. **Tip 3 - Pha loãng Diazepam tĩnh mạch đúng cách:** Diazepam tiêm tĩnh mạch trực tiếp không pha loãng với các dịch truyền khác ngoài NaCl 0.9% vì rất dễ bị kết tủa và dính vào dây truyền nhựa PVC. Tiêm chậm qua chạc 3 đang truyền NaCl 0.9%.
4. **Tip 4 - Kiểm tra đồng tử và phản xạ ánh sáng:** Sau cơn giật, nếu đồng tử hai bên giãn không đều hoặc mất phản xạ ánh sáng, nghi ngờ ngay thoát vị não hoặc phù não cấp, khẩn trương chống phù não bằng Mannitol 20% (0.5–1 g/kg) hoặc NaCl 3% (3–5 mL/kg) và chụp CT sọ não cấp cứu.
5. **Tip 5 - Phân biệt cơn giật vs rùng mình khi sốt (Shivering / Rigors):** Trẻ sốt cao rét run có thể bị nhầm với giật. Nghiệm pháp phân biệt: Giữ chặt chi đang run, nếu là run do sốt thì động tác run sẽ ngừng lại hoặc giảm rõ rệt; nếu là co giật vỏ não thực sự thì bàn tay bác sĩ sẽ cảm nhận được xung lực co cơ kịch phát liên tục không thể cưỡng lại.
6. **Tip 6 - Tránh bẫy hạ sốt quá liều:** Phụ huynh thường quá hoảng sợ nên cho trẻ uống xen kẽ Paracetamol và Ibuprofen dày đặc gây ngộ độc gan cấp tính. Nhắc nhở rõ khoảng cách tối thiểu giữa 2 lần Paracetamol là 4 đến 6 giờ (không quá 4 lần/24h, tổng liều < 60 mg/kg/ngày).
7. **Tip 7 - Chú ý viêm tai giữa tiềm ẩn:** Nhiễm khuẩn tai giữa cấp do phế cầu là ổ nhiễm trùng rất phổ biến khởi phát co giật do sốt nhưng thường bị bỏ sót nếu không soi màng nhĩ cẩn thận bằng đèn soi tai.
8. **Tip 8 - Đánh giá tiêm chủng vắc xin:** Trẻ co giật sau tiêm vắc xin DTP hoặc Sởi-Quai bị-Rubella (MMR) thường do phản ứng sốt kích hoạt cơn giật ở trẻ có cơ địa nhạy cảm, không phải là viêm não do vắc xin. Vẫn khuyến cáo tiêm chủng đầy đủ các mũi tiếp theo sau khi tư vấn kỹ.
9. **Tip 9 - Bẫy hạ natri máu do bù nước sai cách:** Trẻ sốt nôn ói được người nhà cho uống nước lọc hoặc sữa quá loãng có thể bị hạ natri máu cấp gây co giật. Luôn kiểm tra điện giải đồ nếu trẻ có nôn nhiều hoặc co giật tái phát.
10. **Tip 10 - Kỹ thuật tư vấn tâm lý giải tỏa sang chấn cho cha mẹ:** Chứng kiến con co giật tím tái là trải nghiệm kinh hoàng gây ám ảnh sâu sắc cho phụ huynh (họ tưởng con mình đã chết). Bác sĩ cần dành thời gian giải thích từ tốn: cơn co giật do sốt đơn thuần không gây tổn thương não, không làm giảm trí thông minh của trẻ và hướng dẫn các bước sơ cứu cụ thể bằng tờ rơi hướng dẫn.

---

## 11. Các ca lâm sàng thực tế có lời giải chi tiết (Case Studies)

### Case 1: Co giật do sốt đơn thuần ở trẻ 16 tháng tuổi
- **Bệnh sử:** Bé trai 16 tháng tuổi, nặng 11 kg, được mẹ đưa đến cấp cứu sau khi lên cơn co cứng co giật toàn thân kéo dài khoảng 2 phút tại nhà. Trước đó vài giờ bé bắt đầu sốt nóng, chảy mũi trong. Sau cơn giật trẻ khóc to, sau đó ngủ thiếp đi.
- **Thăm khám:** Nhiệt độ 39.2°C, SpO2 98% khí trời, mạch 130 lần/phút, huyết áp 95/60 mmHg. Trẻ tỉnh táo hoàn toàn, tương tác tốt với mẹ, thóp trước đã đóng, cổ mềm, dấu Kernig âm tính, không có dấu thần kinh khu trú. Họng đỏ nhẹ, hai màng nhĩ sáng bóng, phổi trong. Tiền sử tiêm chủng đầy đủ 3 mũi 6 trong 1 và 3 mũi vắc xin Phế cầu Synflorix.
- **Xử trí & Biện luận lâm sàng:**
  1. *Chẩn đoán:* Co giật do sốt đơn thuần (cơn giật toàn thể, thời gian < 15 phút, chỉ có 1 cơn trong 24 giờ, trẻ phát triển bình thường, không có dấu hiệu màng não).
  2. *Chỉ định cận lâm sàng:* Theo khuyến cáo AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED], trẻ đã tiêm chủng đầy đủ Hib và Phế cầu, khám thần kinh bình thường, không có triệu chứng màng não → **KHÔNG** chỉ định chọc dò dịch não tủy, **KHÔNG** đo điện não đồ và **KHÔNG** chụp CT/MRI sọ não.
  3. *Điều trị:* Hạ sốt bằng Paracetamol 150 mg đặt hậu môn (~ 13.6 mg/kg), cho trẻ uống thêm nước oresol.
  4. *Tư vấn:* Giải thích cho gia đình bản chất lành tính của bệnh, không kê đơn thuốc chống động kinh dự phòng theo AAP 2008 (PMID: 18519501) [GUIDELINE VERIFIED]. Theo dõi tại viện 4–6 giờ, xuất viện khi trẻ ổn định.

### Case 2: Co giật do sốt phức hợp tái phát ở trẻ 8 tháng tuổi
- **Bệnh sử:** Bé gái 8 tháng tuổi, nặng 8 kg, được đưa vào viện vì co giật lần 2 trong ngày. Sáng cùng ngày bé sốt 38.5°C và bị co giật toàn thể kéo dài 3 phút. Đến chiều, bé sốt lại 39°C và xuất hiện cơn co giật giật nửa người bên phải kéo dài 10 phút. Bé chưa được tiêm phòng vắc xin Phế cầu.
- **Thăm khám:** Nhiệt độ 38.8°C, mạch 145 lần/phút, thở 38 lần/phút. Trẻ lừ đừ, bú kém, thóp trước hơi căng nhẹ nhưng không phồng rõ, cổ hơi gượng nhẹ khó đánh giá do trẻ quấy khóc. Dấu liệt Todd thoáng qua: tay phải ít cử động hơn tay trái sau cơn giật khoảng 15 phút, sau đó cử động dần hồi phục.
- **Xử trí & Biện luận lâm sàng:**
  1. *Chẩn đoán:* Co giật do sốt thể phức hợp (cơn giật cục bộ nửa người bên phải, lặp lại 2 cơn trong vòng 24 giờ, có dấu liệt Todd sau giật).
  2. *Đánh giá nguy cơ:* Trẻ 8 tháng tuổi, chưa tiêm vắc xin Phế cầu, thóp căng nhẹ và lừ đừ → Nguy cơ cao nhiễm khuẩn thần kinh trung ương (viêm màng não mủ).
  3. *Chỉ định can thiệp:* Bắt buộc thực hiện **Chọc dò tủy sống (LP)** sau khi đã ổn định tri giác và loại trừ tăng áp lực nội sọ. Làm công thức máu, CRP, cấy máu, cấy dịch não tủy.
  4. *Điều trị ban đầu:* Trong khi chờ kết quả xét nghiệm, nếu nghi ngờ viêm màng não, khởi động ngay kháng sinh tĩnh mạch phổ rộng Ceftriaxone 100 mg/kg/ngày (hoặc Cefotaxime) phối hợp Vancomycin 60 mg/kg/ngày. Đo điện não đồ (EEG) khi trẻ ổn định để đánh giá ổ phóng điện cục bộ bán cầu trái.

### Case 3: Trạng thái động kinh do sốt kéo dài 25 phút
- **Bệnh sử:** Bé trai 24 tháng tuổi, nặng 12 kg, có tiền sử co giật do sốt đơn thuần lúc 14 tháng. Trưa nay bé sốt cao đột ngột 40°C và lên cơn co giật co cứng - giật rung toàn thân liên tục. Mẹ đưa bé vào trạm y tế địa phương sau 10 phút giật, trạm y tế không có thuốc tiêm nên chuyển gấp đến bệnh viện. Khi đến phòng cấp cứu, cơn co giật đã kéo dài liên tục 22 phút chưa dứt.
- **Thăm khám tại giường cấp cứu:** Trẻ đang giật giàn giụa, tím môi, SpO2 84%, sùi bọt mép, đồng tử hai bên 3 mm đều, phản xạ ánh sáng còn. Chưa có đường truyền tĩnh mạch.
- **Quy trình xử trí cấp cứu khẩn cấp:**
  1. *Phút 22 (ABCDE):* Đặt trẻ nằm nghiêng, hút đờm dãi, thở oxy mask có túi dự trữ 10 L/phút. Đo nhanh đường huyết mao mạch: 5.2 mmol/L.
  2. *Phút 23 (Cắt cơn bước 1 - Không có ven sẵn):* Áp dụng bằng chứng RAMPART (PMID: 22335736) [DATA VERIFIED] và AES 2016 (PMID: 26900382) [GUIDELINE VERIFIED], tiêm bắp ngay Midazolam liều 0.2 mg/kg = 2.4 mg (rút 0.48 mL từ ống 5 mg/mL tiêm bắp đùi trước ngoài). Đồng thời điều dưỡng lấy đường truyền tĩnh mạch và lấy máu xét nghiệm.
  3. *Phút 28 (Đánh giá sau 5 phút):* Cơn giật giảm nhẹ nhưng vẫn còn giật mắt và co giật cơ tứ chi (cơn giật đã bước sang phút thứ 28). Ven ngoại biên đã lấy thành công. Lặp lại liều Benzodiazepine thứ 2: Diazepam tiêm tĩnh mạch chậm 0.2 mg/kg = 2.4 mg trong 2 phút.
  4. *Phút 32 (Kháng Benzodiazepine - Bước sang giai đoạn Bước 2):* Cơn giật vẫn còn tiếp diễn → Trạng thái động kinh kháng Benzodiazepine. Khởi động ngay thuốc chống động kinh bước 2: **Levetiracetam (Keppra) IV** liều 60 mg/kg = 720 mg pha trong NaCl 0.9% truyền tĩnh mạch nhanh trong 10 phút. Chuẩn bị sẵn bóng Ambu, mask phù hợp cỡ và bộ đặt nội khí quản tại đầu giường.
  5. *Phút 38:* Sau khi truyền được 6 phút Levetiracetam, cơn co giật chấm dứt hoàn toàn. SpO2 tăng lên 97% với oxy mask, nhịp tim 125 lần/phút, huyết áp 95/60 mmHg. Trẻ thở đều, đồng tử 2.5 mm đều hai bên.
  6. *Kế hoạch tiếp theo:* Đặt hậu môn Paracetamol 150 mg hạ sốt. Chuyển trẻ vào phòng hồi sức thần kinh theo dõi tri giác và hô hấp liên tục. Chỉ định chụp MRI sọ não trong vòng vài ngày tới để khảo sát tổn thương phù nề hải mã cấp tính theo khuyến cáo của nghiên cứu FEBSTAT (PMID: 38606600) [DATA VERIFIED].

---

## 12. Câu hỏi kiểm tra kiến thức tích hợp (Checkpoints)

### Checkpoint 1
**Câu hỏi:** Một trẻ 14 tháng tuổi được chẩn đoán co giật do sốt đơn thuần. Mẹ trẻ vô cùng hoảng sợ và tha thiết yêu cầu bác sĩ kê đơn thuốc uống hàng ngày để "cháu không bao giờ bị giật lại nữa". Theo khuyến cáo của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2008), câu trả lời và hành động nào sau đây của bác sĩ là đúng đắn nhất?  
A. Kê đơn Phenobarbital uống hàng ngày trong 6 tháng để bảo vệ não trẻ.  
B. Kê đơn Valproate natri siro hàng ngày vì ít tác dụng phụ hơn Phenobarbital.  
C. Giải thích không dùng thuốc chống động kinh dự phòng thường quy vì nguy cơ tác dụng phụ vượt trội lợi ích và thuốc không ngăn được nguy cơ động kinh sau này.  
D. Kê đơn Diazepam uống liên tục mỗi ngày cho đến khi trẻ được 3 tuổi.  
*Đáp án đúng:* **C**.  
*Giải thích:* AAP 2008 (PMID: 18519501) [GUIDELINE VERIFIED] khẳng định cả điều trị liên tục lẫn ngắt quãng bằng thuốc chống động kinh đều không được khuyến cáo cho co giật do sốt đơn thuần. Phenobarbital gây suy giảm nhận thức, Valproate gây độc gan; và quan trọng nhất, các thuốc này không làm thay đổi nguy cơ tiến triển thành động kinh trong tương lai.

### Checkpoint 2
**Câu hỏi:** Đội cấp cứu ngoại viện tiếp cận một trẻ 3 tuổi đang co giật liên tục kéo dài 8 phút do sốt cao. Trẻ chưa có đường truyền tĩnh mạch và điều dưỡng khó tìm ven do trẻ giãy giụa và co mạch. Theo thử nghiệm lâm sàng RAMPART (NEJM 2012) và hướng dẫn AES 2016, can thiệp dùng thuốc nào là tối ưu nhất tại thời điểm này?  
A. Tiếp tục cố gắng lấy ven bằng mọi giá để tiêm tĩnh mạch Lorazepam.  
B. Tiêm bắp Midazolam liều 0.2 mg/kg (tối đa 10 mg) ngay lập tức.  
C. Tiêm bắp Phenytoin 20 mg/kg vào cơ delta.  
D. Tiêm bắp Phenobarbital 20 mg/kg.  
*Đáp án đúng:* **B**.  
*Giải thích:* Thử nghiệm RAMPART (PMID: 22335736) [DATA VERIFIED] chứng minh tiêm bắp Midazolam đạt tỷ lệ cắt cơn trước viện 73.4% so với 63.4% của tiêm tĩnh mạch Lorazepam (p < 0.001), do tiết kiệm được thời gian thiết lập đường truyền tĩnh mạch (1.2 phút vs 4.8 phút).

### Checkpoint 3
**Câu hỏi:** Một trẻ 10 tháng tuổi có cơn co giật do sốt đơn thuần kéo dài 3 phút. Trẻ chưa từng được tiêm chủng bất kỳ mũi vắc xin nào do gia đình theo phong trào anti-vắc xin. Khám lâm sàng trẻ tỉnh, bú tốt, thóp phẳng, không có dấu hiệu cổ gượng. Thái độ xử trí phù hợp nhất theo AAP 2011 là gì?  
A. Cho trẻ về nhà ngay và không cần làm thêm xét nghiệm gì.  
B. Chụp MRI sọ não cấp cứu.  
C. Chọc dò tủy sống (LP) là một chỉ định cần xem xét vì trẻ chưa được tiêm phòng vắc xin Hib và Phế cầu.  
D. Kê đơn kháng sinh uống ngoại trú và cho về.  
*Đáp án đúng:* **C**.  
*Giải thích:* Theo AAP 2011 (PMID: 21285335) [GUIDELINE VERIFIED], ở trẻ từ 6 đến 12 tháng tuổi chưa được tiêm chủng đầy đủ vắc xin phòng Hib và Phế cầu khuẩn, chọc dò tủy sống là chỉ định cần xem xét (an option) vì nguy cơ viêm màng não do vi khuẩn ở đối tượng này tăng cao và các triệu chứng màng não ở lứa tuổi nhũ nhi thường rất kín đáo.

### Checkpoint 4
**Câu hỏi:** Trong thử nghiệm ESETT (NEJM 2019) về điều trị trạng thái động kinh kháng Benzodiazepine, kết luận nào sau đây là chính xác về hiệu quả của 3 thuốc Levetiracetam, Fosphenytoin và Valproate natri?  
A. Levetiracetam vượt trội hoàn toàn so với Fosphenytoin và Valproate về tỷ lệ cắt cơn.  
B. Valproate natri có hiệu quả kém nhất trong ba thuốc.  
C. Cả 3 thuốc đều có hiệu quả cắt cơn tương đương nhau ở thời điểm 60 phút (~ 45–47%).  
D. Fosphenytoin là thuốc duy nhất đạt tỷ lệ cắt cơn trên 80%.  
*Đáp án đúng:* **C**.  
*Giải thích:* Thử nghiệm ESETT (PMID: 31774955) [DATA VERIFIED] cho thấy tỷ lệ thành công ở phút thứ 60 giữa Levetiracetam (47%), Fosphenytoin (45%) và Valproate (46%) không có sự khác biệt có ý nghĩa thống kê, với độ an toàn tương đương nhau.

### Checkpoint 5
**Câu hỏi:** Nghiên cứu theo dõi dài hạn 10 năm FEBSTAT (Epilepsia 2024) ở trẻ bị Trạng thái động kinh do sốt (FSE kéo dài ≥ 30 phút) đã rút ra kết luận quan trọng nào về mặt hình ảnh học và tiên lượng thần kinh?  
A. 100% trẻ bị FSE sẽ phát triển thành bệnh động kinh toàn thể nguyên phát.  
B. Tổn thương tăng tín hiệu T2 hồi hải mã cấp tính sau FSE có nguy cơ cao tiến triển thành xơ teo hồi hải mã thực thể (Hippocampal Sclerosis).  
C. FSE hoàn toàn không để lại bất kỳ biến đổi vi cấu trúc nào trên MRI sọ não.  
D. Tất cả các tổn thương trên MRI sau FSE đều tự biến mất hoàn toàn mà không để lại di chứng.  
*Đáp án đúng:* **B**.  
*Giải thích:* Nghiên cứu FEBSTAT 10 năm (PMID: 38606600) [DATA VERIFIED] chỉ ra rằng ở những trẻ có tăng tín hiệu T2 hải mã cấp tính, có 10 trong số 14 trẻ (71.4%) tiến triển thành xơ teo hồi hải mã thực thể (definite hippocampal sclerosis), là nguyên nhân hàng đầu gây động kinh thùy thái dương kháng trị.

---

## 13. Tài liệu tham khảo

1. **Subcommittee on Febrile Seizures; American Academy of Pediatrics (AAP Guideline, 2011)**: *Neurodiagnostic evaluation of the child with a simple febrile seizure.* Pediatrics. PMID: **21285335**. [GUIDELINE VERIFIED]
2. **Steering Committee on Quality Improvement and Management, Subcommittee on Febrile Seizures; American Academy of Pediatrics (AAP Guideline, 2008)**: *Febrile seizures: clinical practice guideline for the long-term management of the child with simple febrile seizures.* Pediatrics. PMID: **18519501**. [GUIDELINE VERIFIED]
3. **Glauser T, Shinnar S, Gloss D, et al. (AES Guideline, 2016)**: *Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults: Report of the Guideline Committee of the American Epilepsy Society.* Epilepsy Curr. PMID: **26900382**. [GUIDELINE VERIFIED]
4. **Silbergleit R, Durkalski V, Lowenstein D, et al. (RAMPART Trial, 2012)**: *Intramuscular versus intravenous therapy for prehospital status epilepticus.* N Engl J Med. PMID: **22335736**. [DATA VERIFIED]
5. **Kapur J, Elm J, Chamberlain JM, et al. (ESETT Trial, 2019)**: *Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus.* N Engl J Med. PMID: **31774955**. [DATA VERIFIED]
6. **Babl FE, Herd D, Borland M, et al. (ConSEPT Trial, 2019)**: *Levetiracetam versus phenytoin for second-line treatment of convulsive status epilepticus in children (ConSEPT): an open-label, multicentre, randomised controlled trial.* Lancet. PMID: **31005386**. [DATA VERIFIED]
7. **Lyttle MD, Rainford NEA, Gamble C, et al. (EcLiPSE Trial, 2019)**: *Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (EcLiPSE): a multicentre, open-label, randomised trial.* Lancet. PMID: **31005385**. [DATA VERIFIED]
8. **Murata S, Okasora K, Tanabe T, et al. (Pediatrics RCT, 2018)**: *Acetaminophen and Febrile Seizure Recurrences During the Same Fever Episode.* Pediatrics. PMID: **30297499**. [DATA VERIFIED]
9. **Hesdorffer DC, Lewis DV, Bello JA, et al. (FEBSTAT Study, 2025)**: *Febrile status epilepticus and epileptogenesis: The FEBSTAT study.* Epilepsia Open. PMID: **40770931**. [DATA VERIFIED]
10. **Shinnar S, Bello JA, Chan S, et al. (FEBSTAT 10-Year Study, 2024)**: *Hippocampal sclerosis and temporal lobe epilepsy following febrile status epilepticus: The FEBSTAT study.* Epilepsia. PMID: **38606600**. [DATA VERIFIED]
"""

out_file.write_text(content.strip(), encoding="utf-8")
print(f"Generated {len(content)} characters, {len(content.splitlines())} lines to {out_file}")
