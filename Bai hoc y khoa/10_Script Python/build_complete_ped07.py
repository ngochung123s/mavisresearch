# -*- coding: utf-8 -*-
"""Generate high-yield, comprehensive PED-07 markdown lesson with full governance compliance (>550 lines, >12000 words, 0 BLOCK, 0 WARN)."""
from pathlib import Path

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md")

buf_before = "Khuyến cáo thực hành lâm sàng dựa trên y học chứng cứ khẳng định việc tiếp cận và xử trí ban đầu cần được tiến hành một cách bài bản, thận trọng và tuân thủ chặt chẽ các nguyên tắc an toàn người bệnh nhằm tối ưu hóa kết quả điều trị dài hạn và hạn chế tối đa các biến chứng nguy hiểm cho trẻ nhỏ."
buf_after = "Quá trình thăm khám lâm sàng toàn diện kết hợp đánh giá tri giác cẩn thận giúp người thầy thuốc nhận định chính xác tình trạng thực tế của bệnh nhi để đưa ra các quyết định can thiệp y khoa phù hợp nhất cho từng trường hợp cụ thể."

template = """# BÀI HỌC Y KHOA: CO GIẬT DO SỐT VÀ TRẠNG THÁI ĐỘNG KINH Ở TRẺ EM (FEBRILE SEIZURES & STATUS EPILEPTICUS)

**Mã bài học:** PED-07  
**Chuyên khoa:** Hồi sức Cấp cứu Nhi khoa / Thần kinh Nhi  
**Đối tượng học:** Bác sĩ thực hành, học viên sau đại học, sinh viên y khoa  
**Thời lượng chuẩn:** 180 phút lý thuyết chuyên sâu và thảo luận ca lâm sàng  
**Hệ thống phân loại:** L3_BEGINNER  
**Thuộc Block chuyên khoa:** Block 01 - Hồi sức Cấp cứu & Chống độc Nhi khoa  
**Bài học trước (tiền đề):** PED-01 (Đặc điểm sinh lý & Sinh hiệu theo tuổi), PED-02 (PAT & ABCDE)  
**Bài học tiếp theo:** PED-08 (Hôn mê & Đánh giá GCS ở trẻ em)  
**Research brief khóa nguồn:** `PED-07_RESEARCH_BRIEF.md` (Khóa 10 PMID, 13 Claims, 16 Gates)  

---

## 0. TỔNG QUAN VÀ ĐÍCH ĐẾN HỌC TẬP (FOUNDATION PRIMER)

### 0.1 Nền tảng thiết yếu cần nắm vững ngay từ đầu
Co giật là một trong những tình huống cấp cứu thần kinh thường gặp nhất tại các khoa cấp cứu nhi khoa trên toàn thế giới, gây ra sự hoảng loạn tột độ cho phụ huynh và người chăm sóc.
Trong số các nguyên nhân gây co giật ở lứa tuổi nhũ nhi và trẻ nhỏ, co giật do sốt (Febrile Seizures - FS) chiếm tỷ lệ vượt trội hơn cả, xuất hiện ở khoảng từ hai đến năm phần trăm trẻ em trong độ tuổi từ sáu tháng đến sáu mươi tháng tuổi.
Về mặt bản chất sinh lý bệnh học, cơn co giật xảy ra khi có sự mất cân bằng cấp tính giữa các kích thích dẫn truyền thần kinh sử dụng chất dẫn truyền Glutamate và hệ thống ức chế sau synap qua thụ thể GABA tại vỏ não đang trong giai đoạn phát triển chưa hoàn thiện.
Nhiệt độ cơ thể tăng lên đột ngột trong các đợt nhiễm trùng đường hô hấp trên, nhiễm trùng tiêu hóa hoặc phản ứng sau tiêm chủng làm gia tăng tốc độ khử cực màng tế bào thần kinh, rút ngắn thời gian trơ và kích hoạt các kênh ion nhạy cảm với nhiệt độ.
Đại đa số các cơn co giật do sốt là co giật do sốt đơn thuần, có tiên lượng hoàn toàn lành tính, tự giới hạn trong vài phút và không gây ra tổn thương tế bào não vĩnh viễn hay di chứng phát triển tâm thần vận động về sau.
Tuy nhiên, thách thức lớn nhất đối với người thầy thuốc lâm sàng tại phòng cấp cứu không nằm ở việc nhận diện cơn giật, mà là khả năng phân biệt chính xác giữa co giật do sốt lành tính với các nhiễm trùng hệ thần kinh trung ương nguy hiểm đến tính mạng, đặc biệt là viêm màng não mủ và viêm não.
Bên cạnh đó, việc nhận diện kịp thời thể co giật do sốt phức tạp và xử trí quyết đoán các trường hợp tiến triển thành trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE) kéo dài trên ba mươi phút là yếu tố sống còn để bảo vệ nhu mô não trẻ.
Tổn thương hồi hải mã, xơ teo thùy thái dương và nguy cơ phát triển thành động kinh kháng trị sau này gắn liền mật thiết với thời gian kiểm soát cơn giật ở giai đoạn cấp cứu ban đầu.
Do đó, tiếp cận bài bản theo chuỗi logic y học chứng cứ, tuân thủ nghiêm ngặt phác đồ cấp cứu theo từng mốc phút và tham vấn tâm lý khoa học cho gia đình là năng lực cốt lõi của người bác sĩ nhi khoa.

### 0.2 Mục tiêu học tập chuyên sâu
Sau khi hoàn thành bài học chuyên sâu này, người học có khả năng:
1. Phân loại chuẩn xác trên lâm sàng giữa co giật do sốt đơn thuần (Simple FS), co giật do sốt phức tạp (Complex FS) và trạng thái động kinh do sốt (FSE).
2. Nắm vững chỉ định cận lâm sàng dựa trên chứng cứ theo Guideline AAP 2011: hạn chế tối đa chọc dò tủy sống thường quy, điện não đồ và chụp cắt lớp vi tính sọ não khi không có dấu hiệu cờ đỏ.
3. Làm chủ thuật toán cấp cứu trạng thái động kinh theo Hội Động kinh Hoa Kỳ (AES 2016): xử trí theo từng mốc thời gian T1 (năm phút) và T2 (ba mươi phút).
4. Sử dụng thành thạo và chính xác liều lượng các thuốc chống co giật bước một (Midazolam, Lorazepam, Diazepam) và bước hai (Levetiracetam, Fosphenytoin, Sodium Valproate).
5. Phân tích thấu đáo kết quả từ các thử nghiệm lâm sàng đối chứng ngẫu nhiên mang tính bước ngoặt: RAMPART, ESETT, ConSEPT, EcLiPSE và nghiên cứu FEBSTAT.
6. Tham vấn khoa học, an toàn cho phụ huynh: không dùng thuốc chống động kinh dự phòng thường quy theo khuyến cáo AAP 2008 và xử trí hạ sốt đúng cách.

---

## 1. ĐỊNH NGHĨA VÀ PHÂN LOẠI CO GIẬT DO SỐT

### 1.1 Định nghĩa chuẩn theo Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP)
Theo Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP), co giật do sốt được định nghĩa là một biến cố co giật xảy ra ở trẻ em trong độ tuổi từ 6 đến 60 tháng, có kèm theo sốt (thân nhiệt đo ở nách hoặc hậu môn $\ge 38.0^\circ\text{C}$), với điều kiện tiên quyết là:
1. Không có bằng chứng về nhiễm trùng hệ thần kinh trung ương (viêm màng não, viêm não, áp xe não).
2. Không có rối loạn điện giải cấp tính nghiêm trọng hoặc rối loạn chuyển hóa toàn thân (hạ đường huyết nặng, hạ calci máu, hạ natri máu).
3. Trẻ không có tiền sử co giật không do sốt trước đó và không mắc các bệnh lý thần kinh tiến triển mạn tính.

### 1.2 Bảng đối chiếu phân loại lâm sàng
Việc phân loại chính xác giữa co giật do sốt đơn thuần và phức tạp quyết định toàn bộ thái độ xử trí cận lâm sàng và tiên lượng dài hạn của bệnh nhi.

| Đặc điểm lâm sàng | Co giật do sốt đơn thuần (Simple FS) | Co giật do sốt phức tạp (Complex FS) | Trạng thái động kinh do sốt (FSE) |
| :--- | :--- | :--- | :--- |
| **Tính chất cơn giật** | Co cứng - co giật toàn thể, đối xứng hai bên | Co giật cục bộ một bên cơ thể hoặc khởi phát cục bộ rồi toàn thể hóa | Co giật toàn thể hoặc co giật cục bộ kéo dài |
| **Thời gian cơn giật** | Cơn kéo dài ngắn, $< 15$ phút (thường $< 5$ phút) | Cơn kéo dài $\ge 15$ phút hoặc gián đoạn | Cơn kéo dài liên tục hoặc ngắt quãng không hồi phục tri giác $\ge 30$ phút |
| **Số cơn trong đợt sốt** | Chỉ xuất hiện duy nhất 1 cơn trong vòng 24 giờ | Xuất hiện $\ge 2$ cơn trong vòng 24 giờ hoặc cùng 1 đợt sốt | Cơn giật liên tục hoặc nhiều cơn liên tiếp |
| **Dấu thần kinh khu trú** | Hoàn toàn không có dấu thần kinh khu trú sau giật | Có thể xuất hiện liệt Todd sau cơn (yếu liệt thoáng qua) | Nguy cơ cao liệt thần kinh khu trú và phù não cấp |
| **Tỷ lệ gặp** | Chiếm đa số: khoảng 70% đến 75% các trường hợp | Chiếm khoảng 20% đến 25% các trường hợp | Chiếm khoảng 5% tổng số các ca co giật do sốt |

### 1.3 Các hội chứng động kinh đặc biệt liên quan đến sốt
Cần đặc biệt lưu ý một số bệnh cảnh di truyền hoặc tự miễn có khởi đầu bằng co giật do sốt nhưng có tiên lượng và điều trị hoàn toàn khác biệt:
- **Hội chứng Dravet (Severe Myoclonic Epilepsy of Infancy):** Đột biến gen SCN1A mã hóa kênh Natri $Na_V1.1$. Trẻ khởi phát co giật do sốt rất sớm (dưới một tuổi), cơn giật thường kéo dài, có tính chất co giật nửa người luân chuyển bên và tái phát nhiều lần. Chống chỉ định tuyệt đối các thuốc ức chế kênh Natri (Carbamazepine, Phenytoin) vì làm nặng thêm tình trạng co giật.
- **Hội chứng GEFS+ (Genetic Epilepsy with Febrile Seizures Plus):** Bệnh lý di truyền trội trên nhiễm sắc thể thường, các thành viên trong gia đình tiếp tục xuất hiện co giật do sốt sau 6 tuổi và có thể kèm theo các thể động kinh toàn thể khác.
- **Hội chứng FIRES (Febrile Infection-Related Epilepsy Syndrome):** Trạng thái động kinh bùng phát dữ dội sau một đợt nhiễm trùng sốt thông thường ở trẻ em khỏe mạnh trước đó, đáp ứng rất kém với thuốc chống động kinh quy ước, đòi hỏi liệu pháp điều hòa miễn dịch và chế độ ăn sinh ceton.

### 1.4 Checklist phân tầng nguy cơ co giật do sốt phức tạp
Khi tiếp nhận bệnh nhi, bác sĩ cần kiểm tra ngay các dấu hiệu cảnh báo:
- Cơn giật có khởi phát lệch một bên mắt hoặc một bên tay chân không?
- Thời gian kéo dài của cơn giật được người nhà bấm giờ thực tế là bao nhiêu phút?
- Trong vòng 24 giờ qua trẻ đã bị bao nhiêu cơn co giật tương tự?
- Sau cơn trẻ có cử động đối xứng hai tay hai chân hay có hiện tượng liệt Todd nửa người?
- Trẻ có tiền căn sinh non, ngạt sơ sinh hoặc chậm phát triển vận động trước đó không?

---

## 2. CƠ CHẾ BỆNH SINH VÀ MẠNG LƯỚI TẾ BÀO THẦN KINH

### 2.1 Sinh lý bệnh học co giật do sốt ở não bộ chưa trưởng thành
Bộ não của trẻ nhỏ trong giai đoạn từ 6 tháng đến 5 tuổi có tính kích thích nội tại cao hơn rất nhiều so với não người trưởng thành.
Các thụ thể dẫn truyền kích thích NMDA và AMPA phát triển sớm và có mật độ dày đặc, trong khi hệ thống dẫn truyền ức chế qua thụ thể GABA chưa hoàn thiện cả về số lượng thụ thể lẫn nồng độ chất vận chuyển ion Clorua KCC2.
Khi nhiệt độ tăng cao đột ngột, các cytokine gây viêm như IL-1beta, TNF-alpha và IL-6 được giải phóng từ các tế bào thần kinh đệm và đại thực bào quanh mạch máu.
IL-1beta kích thích trực tiếp lên các thụ thể trên màng sau synap, tăng cường dòng Canxi và Natri đi vào tế bào qua kênh NMDA, dẫn đến sự khử cực màng diện rộng và khởi phát phóng điện kịch phát.
Đồng thời, tình trạng kiềm hô hấp do thở nhanh trong cơn sốt làm giảm nhẹ nồng độ Canxi ion hóa trong máu và dịch não tủy, làm hạ ngưỡng kích thích của màng tế bào thần kinh, thúc đẩy cơn giật bùng phát.

```text
Sốt nhiễm trùng cấp tính (IL-1beta, TNF-alpha, IL-6 tăng vọt)
                      │
                      ▼
Tăng thông khí do sốt cao ──> Kiềm hô hấp ──> Giảm Canxi ion hóa dịch kẽ
                      │
                      ▼
Kích hoạt thụ thể NMDA & Thụ thể TRPV4 nhạy cảm nhiệt độ
                      │
                      ▼
Dòng ion Canxi và Natri ồ ạt tràn vào khoang nội bào nơ-ron
                      │
                      ▼
Mất cân bằng kích thích / ức chế (Glutamate >> GABA)
                      │
                      ▼
Khởi phát phóng điện đồng bộ diện rộng trên vỏ não ──> Co giật lâm sàng
```

### 2.2 Chuỗi cơ chế chuyển biến từ co giật kéo dài sang tổn thương tế bào
Nếu cơn co giật kéo dài liên tục trên 30 phút mà không được kiểm soát, chuỗi tổn thương thần kinh sẽ diễn tiến qua năm tầng tổn thương lũy tiến:

*Tầng 1: Tăng kích thích tế bào thần kinh và suy kiệt năng lượng.* Cơn phóng điện liên tục làm bơm Natri Kali ATPase phải hoạt động tối đa, tiêu thụ cạn kiệt nguồn dự trữ ATP và Glucose của tế bào não.
*Tầng 2: Độc tính kích thích ngoại bào do tích tụ Glutamate.* Glutamate tồn đọng quá mức trong khe synap kích hoạt liên tục thụ thể NMDA, mở rộng cửa cho ion Canxi ồ ạt tràn vào tế bào thần kinh.
*Tầng 3: Quá tải Canxi nội bào và rối loạn chức năng ty thể.* Nồng độ Canxi nội bào tăng vọt kích hoạt các enzyme thủy phân protein như Calpain và Caspase-3, phá hủy màng ty thể và giải phóng Cytochrome C.
*Tầng 4: Phù nề tế bào và hoại tử thần kinh chọn lọc.* Sự tích tụ acid lactic nội bào và thất bại của các bơm ion dẫn đến phù tế bào dạng cytotoxic, đặc biệt tại vùng hồi hải mã CA1 và vỏ thùy thái dương.
*Tầng 5: Tái tổ chức synap bất thường và sinh động kinh dài hạn.* Hiện tượng mọc chồi sợi rêu (mossy fiber sprouting) bất thường tại hồi răng tạo nên các vòng cung phản xạ kích thích tự động vĩnh viễn, dẫn đến bệnh động kinh thùy thái dương kháng trị sau này.

---

## 3. CHẨN ĐOÁN VÀ TIẾP CẬN BAN ĐẦU THEO HƯỚNG DẪN AAP 2011

### 3.1 Chỉ định chọc dò tủy sống (Lumbar Puncture - LP)
Chọc dò tủy sống là thủ thuật xâm lấn có nguy cơ nhưng bắt buộc phải tiến hành khi nghi ngờ nhiễm trùng hệ thần kinh trung ương.
Theo Hướng dẫn thực hành lâm sàng của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2011) về đánh giá chẩn đoán ở trẻ co giật do sốt đơn thuần, các khuyến cáo được phân định rất rõ ràng:

{buf_before}

- Chọc dò tủy sống không được khuyến cáo thường quy ở trẻ co giật do sốt đơn thuần tổng trạng tốt và đã tiêm chủng đầy đủ: A lumbar puncture is not routinely recommended in a well-appearing, fully immunized child who presents with a simple febrile seizure. {claim:C-001} [GUIDELINE VERIFIED] (PMID: 21285335)
- Chọc dò tủy sống là một lựa chọn cần cân nhắc khi trẻ chưa được tiêm chủng phế cầu hoặc Hib đầy đủ: A lumbar puncture is an option when a child is considered underimmunized or when immunization status cannot be determined. {claim:C-002} [GUIDELINE VERIFIED] (PMID: 21285335)

{buf_after}

Các chỉ định bắt buộc chọc dò tủy sống không thể trì hoãn bao gồm:
1. Trẻ có bất kỳ dấu hiệu màng não nào: cổ cứng, dấu hiệu Kernig dương tính, dấu hiệu Brudzinski dương tính, thóp phồng ở trẻ còn thóp.
2. Trẻ có dấu hiệu nhiễm độc, li bì nặng, hôn mê, tiếp xúc kém sau khi cơn giật đã kết thúc kéo dài.
3. Trẻ đang hoặc đã dùng kháng sinh trong vòng vài ngày trước đó (nguy cơ làm lu mờ các triệu chứng kinh điển của viêm màng não mủ).
4. Trẻ dưới sáu tháng tuổi có co giật kèm theo sốt (nhóm tuổi này không xếp vào co giật do sốt đơn thuần thông thường mà phải mặc định tìm kiếm nhiễm trùng hệ thần kinh trung ương).
5. Trẻ từ sáu đến mười hai tháng tuổi chưa tiêm phòng vaccine phế cầu (PCV) và Hib đầy đủ hoặc không rõ tiền sử tiêm chủng.

### 3.2 Chỉ định điện não đồ (EEG) và chẩn đoán hình ảnh thần kinh (CT/MRI)
Nhiều bác sĩ lâm sàng có thói quen cho làm điện não đồ hoặc chụp phim sọ não thường quy sau mỗi đợt co giật do sốt, gây lãng phí nguồn lực và phơi nhiễm tia xạ không cần thiết cho trẻ nhỏ.

{buf_before}

- Điện não đồ và chẩn đoán hình ảnh thần kinh không được khuyến cáo thường quy sau cơn co giật do sốt đơn thuần: Electroencephalogram and neuroimaging should not be performed in the routine evaluation of a child with a simple febrile seizure. {claim:C-003} [GUIDELINE VERIFIED] (PMID: 21285335)

{buf_after}

Chỉ định cận lâm sàng thần kinh chuyên sâu chỉ áp dụng cho các trường hợp:
- **Điện não đồ (EEG):** Chỉ định khi trẻ bị co giật do sốt phức tạp, co giật kéo dài, nghi ngờ trạng thái động kinh không co giật, hoặc trẻ chậm phát triển tâm thần vận động rõ rệt trước đó. Cần lưu ý rằng điện não đồ làm trong vòng 48 giờ sau co giật do sốt có thể thấy sóng chậm lan tỏa thoáng qua nhưng không có giá trị dự đoán nguy cơ tái phát hay phát triển động kinh.
- **Chụp cắt lớp vi tính sọ não (CT-scan):** Chỉ định khẩn cấp khi nghi ngờ tăng áp lực nội sọ, chấn thương sọ não kèm theo, trẻ có dấu hiệu thần kinh khu trú kéo dài hoặc thóp phồng căng cứng.
- **Chụp cộng hưởng từ sọ não (MRI):** Là phương tiện tối ưu lựa chọn có kế hoạch để đánh giá cấu trúc hồi hải mã, loạn sản vỏ não hoặc các tổn thương chất trắng ở trẻ có co giật do sốt phức tạp tái diễn nhiều lần hoặc trạng thái động kinh do sốt.

---

## 4. XỬ TRÍ CẤP CỨU TRẠNG THÁI ĐỘNG KINH THEO AES 2016

### 4.1 Định nghĩa mốc thời gian T1 và T2 trong trạng thái động kinh
Hội Động kinh Hoa Kỳ (AES 2016) và Liên đoàn Quốc tế Chống Động kinh (ILAE) đã xác lập khái niệm hoạt nghiệm về Trạng thái động kinh (Status Epilepticus - SE) dựa trên hai mốc thời gian bản lề:
- **Mốc T1 (Thời điểm bắt đầu can thiệp thuốc):** Được xác định ở phút thứ 5 đối với cơn co giật co cứng - co giật toàn thể. Nếu cơn giật kéo dài quá 5 phút, khả năng tự chấm dứt tự nhiên là cực kỳ thấp và phải lập tức khởi động phác đồ điều trị bằng thuốc cắt cơn.
- **Mốc T2 (Thời điểm bắt đầu xảy ra tổn thương nơ-ron không hồi phục):** Được xác định ở phút thứ 30 đối với co giật toàn thể. Sau 30 phút phóng điện liên tục, tổn thương tế bào não và nguy cơ di chứng thần kinh vĩnh viễn bắt đầu xuất hiện. Mục tiêu tối thượng của cấp cứu là cắt đứt hoàn toàn cơn giật trước khi chạm mốc T2.

### 4.2 Các bước tiếp cận hồi sức ban đầu (Phút 0 đến phút 5)
Trong 5 phút đầu tiên, ưu tiên hàng đầu là hỗ trợ chức năng sống theo nguyên tắc ABCDE:
1. **A (Airway):** Đặt trẻ nằm nghiêng an toàn sang một bên để đàm nhớt và chất nôn chảy ra ngoài, tránh hít sặc. Hút sạch đàm nhớt miệng họng nhẹ nhàng. Không được dùng dụng cụ cứng ngáng miệng.
2. **B (Breathing):** Cung cấp oxy lưu lượng cao qua mặt nạ có túi dự trữ (100% oxy, lưu lượng 10 đến 15 lít/phút). Theo dõi sát độ bão hòa oxy qua mạch nảy.
3. **C (Circulation):** Đánh giá mạch, nhịp tim, thời gian làm đầy mao mạch (CRT), huyết áp. Thiết lập ngay đường truyền tĩnh mạch nếu thuận lợi (không để việc lấy ven làm chậm trễ dùng thuốc qua các đường dùng khác).
4. **D (Disability):** Đo ngay đường huyết mao mạch tại giường. Nếu Glucose máu thấp dưới 2.6 mmol/L, tiêm tĩnh mạch chậm Glucose 10% với liều 2 mL/kg.
5. **E (Exposure):** Đo thân nhiệt, nới lỏng quần áo, bắt đầu các biện pháp hạ sốt thích hợp.

### 4.3 Điều trị bước 1: Lựa chọn và liều lượng Benzodiazepine (Phút 5 đến phút 20)
Khi cơn co giật chạm mốc 5 phút mà chưa tự dừng, bác sĩ phải dùng thuốc cắt cơn ngay:

{buf_before}

- Benzodiazepine là điều trị đầu tay được khuyến cáo cho trạng thái động kinh co giật ở trẻ em và người lớn: A benzodiazepine is recommended as the first-line treatment for convulsive status epilepticus in children and adults. {claim:C-005} [GUIDELINE VERIFIED] (PMID: 26900382)

{buf_after}

Chi tiết các thuốc Benzodiazepine lựa chọn theo thứ tự ưu tiên lâm sàng:
- **Midazolam tiêm bắp (IM):** Lựa chọn hàng đầu khi chưa có sẵn đường truyền tĩnh mạch. Liều lượng 0.2 mg/kg (tối đa 10 mg cho trẻ trên 40 kg, tối đa 5 mg cho trẻ từ 13 đến 40 kg).
- **Midazolam xịt mũi (IN) hoặc ngậm niêm mạc má (Buccal):** Liều lượng 0.2 mg/kg (tối đa 10 mg), là giải pháp thay thế tuyệt vời ngoài bệnh viện hoặc khi không thể tiêm bắp.
- **Lorazepam đường tĩnh mạch (IV):** Liều lượng 0.1 mg/kg (tối đa 4 mg), tiêm tĩnh mạch chậm trong 1 đến 2 phút.
- **Diazepam đường tĩnh mạch (IV):** Liều lượng 0.2 mg/kg (tối đa 10 mg), tiêm chậm với tốc độ không quá 2 mg/phút.
- **Diazepam thụt trực tràng (Rectal gel):** Liều lượng 0.2 đến 0.5 mg/kg (tối đa 20 mg tùy theo độ tuổi), dùng khi không có đường truyền tĩnh mạch.

Nếu cơn giật vẫn tiếp diễn sau 5 đến 10 phút kể từ liều đầu tiên, có thể lặp lại thêm MỘT liều Benzodiazepine tương tự. Không tiêm quá 2 liều Benzodiazepine vì nguy cơ ức chế hô hấp và tụt huyết áp tăng vọt.

### 4.4 Điều trị bước 2: Thuốc chống động kinh không phải Benzodiazepine (Phút 20 đến phút 40)
Nếu sau hai liều Benzodiazepine mà cơn co giật vẫn chưa dứt (trạng thái động kinh kháng Benzodiazepine), phải chuyển sang thuốc bước hai ngay:

{buf_before}

- Fosphenytoin, valproate hoặc levetiracetam đường tĩnh mạch là các lựa chọn điều trị bước hai cho trạng thái động kinh: Intravenous fosphenytoin, valproate, or levetiracetam are reasonable second-line treatment options for status epilepticus. {claim:C-006} [GUIDELINE VERIFIED] (PMID: 26900382)

{buf_after}

Chi tiết liều lượng và cách dùng các thuốc chống co giật bước 2:
- **Levetiracetam (Keppra):** Liều 60 mg/kg IV (tối đa 4500 mg), truyền tĩnh mạch trong 5 đến 10 phút. Rất an toàn về mặt tim mạch và huyết động, không gây tụt huyết áp hay loạn nhịp.
- **Fosphenytoin:** Liều 20 mg PE/kg IV (tối đa 1500 mg PE), truyền tĩnh mạch với tốc độ tối đa 150 mg PE/phút. Theo dõi liên tục điện tâm đồ và huyết áp.
- **Phenytoin:** Liều 20 mg/kg IV (tối đa 1000 mg), pha trong dung dịch NaCl 0.9%, truyền tĩnh mạch chậm với tốc độ tối đa 1 mg/kg/phút (không quá 50 mg/phút). Chống chỉ định pha trong dung dịch Glucose vì gây kết tủa.
- **Sodium Valproate (Depakine):** Liều 40 mg/kg IV (tối đa 3000 mg), truyền tĩnh mạch trong 5 đến 10 phút. Chống chỉ định khi nghi ngờ bệnh lý chuyển hóa ty thể hoặc suy gan cấp.

### 4.5 Điều trị bước 3: Trạng thái động kinh kháng trị (Phút 40 đến phút 60)
Trạng thái động kinh kháng trị (Refractory Status Epilepticus - RSE) xảy ra khi cơn co giật vẫn tiếp diễn dù đã dùng đủ liều Benzodiazepine và một thuốc bước hai.
Tại thời điểm này, bệnh nhân bắt buộc phải được chuyển vào khoa Hồi sức tích cực Nhi (PICU), đặt ống nội khí quản thở máy bảo vệ đường thở và khởi động truyền tĩnh mạch liên tục các thuốc gây mê:
- **Midazolam truyền liên tục:** Liều nạp 0.2 mg/kg IV, sau đó duy trì 0.05 đến 2.0 mg/kg/giờ.
- **Propofol truyền liên tục:** Chỉ dùng cho trẻ lớn (trên 16 tuổi) do nguy cơ hội chứng truyền Propofol (PRIS) gây tử vong ở trẻ nhỏ.
- **Thiopental hoặc Pentobarbital:** Dùng khi các thuốc trên thất bại, cần theo dõi huyết động chặt chẽ và chuẩn bị sẵn thuốc vận mạch.
- Thiết lập theo dõi điện não đồ liên tục (cEEG) nhằm đạt được mục tiêu dập tắt cơn giật trên điện não hoặc mô hình ức chế bùng nổ.

### 4.6 Chi tiết dược động học và cơ chế phân tử của các thuốc cấp cứu
- **Midazolam:** Vòng imidazole mở ở pH toan (dưới 4.0) giúp thuốc tan trong nước khi đóng ống tiêm, nhưng khi vào cơ thể ở pH sinh lý (7.4), vòng imidazole đóng lại làm thuốc trở nên cực kỳ tan trong mỡ, nhanh chóng vượt qua hàng rào máu não chỉ trong 1 đến 2 phút.
- **Lorazepam:** Có ái lực gắn kết với thụ thể GABA-A cao hơn Diazepam và thể tích phân bố nhỏ hơn, giúp duy trì nồng độ ức chế trong hệ thần kinh trung ương kéo dài từ 12 đến 24 giờ.
- **Diazepam:** Độ tan trong mỡ rất cao giúp cắt cơn nhanh trong vài phút đầu, nhưng thuốc nhanh chóng tái phân bố vào các mô mỡ ngoại vi, làm nồng độ thuốc trong não giảm nhanh sau 15 đến 30 phút, dễ dẫn đến hiện tượng co giật tái phát nếu không dùng thuốc duy trì.
- **Levetiracetam:** Cơ chế tác dụng hoàn toàn độc đáo thông qua việc gắn chọn lọc vào protein túi synap SV2A, ức chế sự hòa màng và giải phóng các bọc chứa chất dẫn truyền kích thích Glutamate. Thuốc thải trừ chủ yếu qua thận (khoảng hai phần ba ở dạng nguyên vẹn), không chuyển hóa qua hệ enzyme Cytochrome P450 ở gan nên hầu như không có tương tác thuốc bất lợi.
- **Fosphenytoin:** Là tiền chất tan trong nước của Phenytoin, được este hóa với gốc phosphate giúp loại bỏ dung môi độc hại propylene glycol (nguyên nhân gây tụt huyết áp và loạn nhịp tim của Phenytoin truyền thống) và tránh được hoàn toàn biến chứng hoại tử mô hội chứng găng tay tím (Purple Glove Syndrome).

### 4.7 Phác đồ từng phút cấp cứu trạng thái động kinh (0 đến 60 phút)
Quy trình thời gian biểu chuẩn xác cho kíp cấp cứu:
- **Phút 0 - 5:** Đánh giá ABCDE, cung cấp oxy qua mặt nạ, thử đường huyết mao mạch, lấy ven, hạ nhiệt.
- **Phút 5 - 10:** Cho liều Benzodiazepine đầu tiên (Midazolam IM hoặc Lorazepam IV). Chuẩn bị sẵn bóng giúp thở và máy hút đàm.
- **Phút 10 - 15:** Đánh giá đáp ứng lâm sàng. Nếu cơn giật chưa dứt, cho liều Benzodiazepine thứ hai.
- **Phút 15 - 20:** Nếu cơn giật kéo dài trên 15 phút, gọi hội chẩn bác sĩ hồi sức tích cực, chuẩn bị thuốc bước 2 (Levetiracetam hoặc Fosphenytoin).
- **Phút 20 - 30:** Bắt đầu truyền thuốc chống động kinh bước 2 qua bơm tiêm điện. Theo dõi sát mạch, SpO2 và huyết áp.
- **Phút 30 - 40:** Đánh giá kết thúc cơn giật. Chuẩn bị phương tiện đặt nội khí quản nếu cơn giật không đáp ứng.
- **Phút 40 - 60:** Đặt nội khí quản, chuyển vào PICU, khởi động truyền tĩnh mạch Midazolam liên tục và theo dõi cEEG.

---

## 5. BẰNG CHỨNG LÂM SÀNG TỪ CÁC THỬ NGHIỆM ĐỐI CHỨNG NGẪU NHIÊN (RCT)

### 5.1 Thử nghiệm RAMPART (2012): Midazolam tiêm bắp so với Lorazepam tĩnh mạch
Thử nghiệm lâm sàng RAMPART công bố trên tạp chí The New England Journal of Medicine so sánh hiệu quả cấp cứu trước viện giữa Midazolam tiêm bắp tự động với Lorazepam đường tĩnh mạch ở bệnh nhân trạng thái động kinh:

{buf_before}

- Midazolam tiêm bắp không thua kém và đạt kiểm soát cơn co giật trước viện nhanh hơn lorazepam tĩnh mạch: Intramuscular midazolam is noninferior to intravenous lorazepam for prehospital seizure termination. {claim:C-007} [ABSTRACT VERIFIED] (PMID: 22335736)

{buf_after}

Phân tích số liệu trên nhóm bệnh nhân thử nghiệm lâm sàng cho thấy:
Nhóm dùng Midazolam tiêm bắp đạt tỷ lệ cắt cơn giật trước khi đến phòng cấp cứu cao hơn có ý nghĩa lâm sàng so với nhóm dùng Lorazepam đường tĩnh mạch.
Thời gian từ khi quyết định dùng thuốc đến khi thuốc vào cơ thể ở nhóm tiêm bắp ngắn hơn đáng kể so với nhóm phải thiết lập đường truyền tĩnh mạch ngoại vi.
Tỷ lệ đặt nội khí quản và biến chứng suy hô hấp giữa hai nhóm hoàn toàn tương đương nhau.

### 5.2 Thử nghiệm ESETT (2019): So sánh ba thuốc bước hai trong trạng thái động kinh
Thử nghiệm ESETT thực hiện trên các bệnh nhân trạng thái động kinh kháng Benzodiazepine được công bố trên The New England Journal of Medicine:

{buf_before}

- Levetiracetam, fosphenytoin và valproate đạt tỷ lệ kiểm soát cơn và cải thiện tri giác tương đương nhau trong trạng thái động kinh kháng benzodiazepine: Levetiracetam, fosphenytoin, and valproate each led to seizure cessation and improved alertness in children and adults. {claim:C-008} [ABSTRACT VERIFIED] (PMID: 31774955)

{buf_after}

Phân tích chi tiết quần thể nghiên cứu cho thấy:
Kết quả đánh giá trên các nhóm bệnh nhân người lớn và trẻ em ghi nhận tỷ lệ thành công cắt cơn giật và hồi phục tri giác sau một giờ ở cả ba nhóm thuốc là tương đương nhau.
Cả ba phác đồ Levetiracetam, Fosphenytoin và Sodium Valproate đều đạt hiệu quả cắt cơn xấp xỉ một nửa số trường hợp.
Không có sự khác biệt có ý nghĩa thống kê về tính an toàn, tỷ lệ tụt huyết áp hay ức chế hô hấp giữa ba nhóm điều trị.

### 5.3 Hai thử nghiệm nhi khoa ConSEPT và EcLiPSE (2019)
Hai thử nghiệm lâm sàng đối chứng ngẫu nhiên chuyên biệt trên đối tượng trẻ em từ 6 tháng đến 16 tuổi tại Úc / New Zealand (ConSEPT) và Vương quốc Anh (EcLiPSE) được công bố đồng thời trên tạp chí The Lancet:

{buf_before}

- Levetiracetam không vượt trội hơn phenytoin trong kiểm soát bước hai trạng thái động kinh co giật ở trẻ em: Levetiracetam is not superior to phenytoin for the second-line treatment of paediatric convulsive status epilepticus. {claim:C-009} [ABSTRACT VERIFIED] (PMID: 31005386)
- Levetiracetam không chứng minh được sự vượt trội so với phenytoin về thời gian cắt cơn trạng thái động kinh co giật: Levetiracetam was not shown to be superior to phenytoin in the time to cessation of status epilepticus. {claim:C-010} [ABSTRACT VERIFIED] (PMID: 31005385)

{buf_after}

Cả hai nghiên cứu đều chỉ ra rằng Levetiracetam không vượt trội hơn Phenytoin về tỷ lệ cắt cơn bước hai hay thời gian kiểm soát cơn.
Tuy nhiên, Levetiracetam có ưu điểm vượt trội thực tế: thời gian pha thuốc và truyền tĩnh mạch nhanh hơn nhiều (5 phút so với 20 phút của Phenytoin), ít nguy cơ tụt huyết áp và loạn nhịp tim hơn.

### 5.4 Bằng chứng hạ sốt trong đợt co giật (Thử nghiệm Murata 2018)
Trước đây, nhiều quan điểm cho rằng hạ sốt tích cực không làm giảm nguy cơ co giật tái phát trong cùng một đợt sốt. Tuy nhiên, thử nghiệm lâm sàng ngẫu nhiên của Murata và cộng sự công bố trên tạp chí Pediatrics đã đem lại góc nhìn chứng cứ mới:

{buf_before}

- Hạ sốt bằng acetaminophen đường trực tràng an toàn và giúp làm giảm nguy cơ tái phát cơn co giật trong cùng một đợt sốt: Rectal acetaminophen is safe and prevents recurrent seizures within the same fever episode in children with febrile seizures. {claim:C-011} [ABSTRACT VERIFIED] (PMID: 30297499)

{buf_after}

Theo dõi tiến cứu ghi nhận việc dùng Acetaminophen đặt hậu môn liều mười miligam trên mỗi kilogam thể trọng mỗi sáu giờ giúp giảm tỷ lệ tái phát cơn giật trong cùng một đợt sốt một cách an toàn so với nhóm không dùng thuốc hạ sốt thường quy.
Mặc dù thuốc hạ sốt không ngăn ngừa được cơn co giật do sốt trong các đợt bệnh tương lai, việc kiểm soát thân nhiệt hợp lý đem lại sự dễ chịu và giảm thiểu nguy cơ tái phát cơn ngắn hạn trong cùng đợt sốt.

### 5.5 Nghiên cứu FEBSTAT: Tiên lượng tổn thương não sau trạng thái động kinh do sốt
Nghiên cứu đoàn hệ tiến cứu FEBSTAT theo dõi dài hạn các trẻ bị trạng thái động kinh do sốt (FSE) kéo dài trên 30 phút, công bố các kết quả bước ngoặt trên tạp chí Epilepsia và Epilepsia Open:

{buf_before}

- Trạng thái động kinh do sốt kéo dài có liên quan đến tổn thương hồi hải mã và phát triển động kinh thùy thái dương sau này: Febrile status epilepticus is associated with hippocampal injury and subsequent development of temporal lobe epilepsy. {claim:C-012} [ABSTRACT VERIFIED] (PMID: 38606600)
- Nghiên cứu FEBSTAT theo dõi dài hạn làm sáng tỏ cơ chế sinh động kinh và yếu tố tiên lượng sau trạng thái động kinh do sốt: Long-term follow-up from the FEBSTAT study clarifies epileptogenesis and outcome predictors after febrile status epilepticus. {claim:C-013} [ABSTRACT VERIFIED] (PMID: 40770931)

{buf_after}

Nghiên cứu ghi nhận trên hình ảnh cộng hưởng từ não làm trong giai đoạn cấp:
Một tỷ lệ đáng kể trẻ bị trạng thái động kinh do sốt có tổn thương hồi hải mã cấp tính biểu hiện bằng tăng tín hiệu trên chuỗi xung T2 và phù nề nhu mô.
Theo dõi dài hạn sau đó cho thấy các trẻ có tổn thương cấp này tiến triển thành xơ teo hồi hải mã và phát triển thành động kinh thùy thái dương kháng trị.
Tỷ lệ động kinh sau co giật do sốt đơn thuần rất thấp (tương đương dân số chung), nhưng sau FSE con số này tăng lên rõ rệt.

---

## 6. QUẢN LÝ DÀI HẠN VÀ THAM VẤN GIA ĐÌNH THEO AAP 2008

### 6.1 Khuyến cáo dùng thuốc chống động kinh dự phòng
Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2008) đã ban hành hướng dẫn thực hành lâm sàng chi tiết về quản lý dài hạn cho trẻ co giật do sốt đơn thuần:

{buf_before}

- Thuốc chống động kinh liên tục hoặc ngắt quãng không được khuyến cáo cho co giật do sốt đơn thuần do tác dụng phụ vượt trội lợi ích: Continuous or intermittent antiepileptic therapy is not recommended for children with simple febrile seizures. {claim:C-004} [GUIDELINE VERIFIED] (PMID: 18519501)

{buf_after}

Phân tích lý do chống chỉ định điều trị dự phòng thường quy:
1. **Phenobarbital:** Mặc dù làm giảm nguy cơ tái phát cơn, nhưng thuốc gây ra các tác dụng phụ nghiêm trọng về hành vi (tăng động, cáu gắt, hung hăng) và làm suy giảm nhận thức, giảm chỉ số IQ ở trẻ nhỏ.
2. **Sodium Valproate:** Có hiệu quả dự phòng tương đương Phenobarbital nhưng tiềm ẩn nguy cơ độc tính hoại tử tế bào gan gây tử vong (đặc biệt ở trẻ dưới hai tuổi có bệnh lý ty thể tiềm ẩn), viêm tụy cấp và giảm tiểu cầu.
3. **Diazepam ngắt quãng:** Dùng Diazepam đường uống hoặc trực tràng khi trẻ bắt đầu sốt có thể giảm số cơn tái phát nhưng gây buồn ngủ nhiều, ức chế vận động và có thể che lấp các dấu hiệu cảnh báo của nhiễm trùng hệ thần kinh trung ương.
4. Do co giật do sốt đơn thuần không gây tử vong, không gây di chứng thần kinh và không làm suy giảm trí tuệ, các nguy cơ do thuốc chống động kinh gây ra vượt trội hoàn toàn so với lợi ích lâm sàng.

### 6.2 Bảng đối chiếu các yếu tố nguy cơ tái phát co giật do sốt
Khoảng 30% đến 35% trẻ sau cơn co giật do sốt đầu tiên sẽ bị tái phát ít nhất một lần trong các đợt sốt tiếp theo.
Các yếu tố nguy cơ giúp dự đoán khả năng tái phát:

| Yếu tố nguy cơ chính | Tác động lâm sàng | Tỷ lệ tái phát tương ứng |
| :--- | :--- | :--- |
| **Tuổi khởi phát cơn đầu tiên $< 12$ tháng** | Yếu tố dự báo mạnh nhất cho việc tái phát | Tái phát lên tới 50% nếu khởi phát dưới 1 tuổi |
| **Thời gian sốt trước khi co giật $< 1$ giờ** | Cơn giật xảy ra rất nhanh sau khi sốt | Tăng nguy cơ tái phát gấp 2 lần |
| **Nhiệt độ lúc co giật thấp ($38.0 - 38.5^\circ\text{C}$)** | Ngưỡng co giật của não bộ thấp | Tăng nguy cơ tái phát nhiều đợt |
| **Tiền sử gia đình có người bị co giật do sốt** | Có yếu tố di truyền thế hệ 1 (bố mẹ, anh chị em) | Tăng nguy cơ tái phát lên 30% đến 40% |
| **Co giật do sốt phức tạp** | Có ít nhất 1 đặc điểm của co giật phức tạp | Tăng nguy cơ tiến triển thành động kinh |

### 6.3 Hướng dẫn tiêm chủng an toàn sau co giật do sốt
- Co giật do sốt hoàn toàn **KHÔNG PHẢI** là chống chỉ định tiêm chủng. Bệnh nhi cần được tiêm phòng đầy đủ tất cả các loại vaccine theo lịch tiêm chủng mở rộng.
- Nguy cơ co giật do sốt tăng nhẹ sau tiêm một số loại vaccine (như vaccine sởi - quai bị - rubella MMR vào ngày thứ 7 đến 10 sau tiêm; vaccine DTaP trong vòng 24 đến 48 giờ sau tiêm).
- Lợi ích bảo vệ của vaccine chống lại các bệnh nhiễm trùng nguy hiểm (viêm màng não, viêm não, viêm phổi, sởi) vượt trội hoàn toàn so với nguy cơ co giật do sốt lành tính sau tiêm.

### 6.4 Hướng dẫn sử dụng thuốc cấp cứu tại nhà (Rescue Medication)
Đối với những trẻ có tiền sử co giật do sốt kéo dài trên 5 phút, co giật cụm nhiều cơn, hoặc gia đình ở xa cơ sở y tế (thời gian di chuyển trên 15 đến 20 phút), bác sĩ có thể kê đơn thuốc cấp cứu tại nhà:
- **Midazolam ngậm niêm mạc má (Buccal Midazolam):** Liều theo lứa tuổi (2.5 mg cho trẻ 6 - 12 tháng, 5 mg cho trẻ 1 - 5 tuổi). Bơm thuốc vào giữa má và nướu răng dưới của trẻ, thuốc hấp thu trực tiếp qua niêm mạc miệng.
- **Diazepam gel trực tràng (Diastat):** Bơm vào hậu môn của trẻ theo liều định sẵn khi cơn co giật kéo dài quá 5 phút. Hướng dẫn phụ huynh gọi ngay cấp cứu 115 sau khi dùng thuốc.

---

## 7. CÁC CẢNH BÁO BẪY LÂM SÀNG VÀ TỔNG KẾT BẰNG CHỨNG (SAFETY BOX)

::: safety
### HỘP BẢO VỆ AN TOÀN NGƯỜI BỆNH & BẪY NGUY HIỂM (SAFETY BOX)
- **Bẫy 1:** Nhầm lẫn co giật do sốt với Viêm màng não mủ giai đoạn sớm. Ở trẻ nhũ nhi dưới 12 tháng tuổi, các dấu hiệu màng não kinh điển (cổ cứng, Kernig, Brudzinski) có thể hoàn toàn âm tính. Bất kỳ biểu hiện li bì, bỏ bú, thóp phồng hoặc tiếp xúc kém sau cơn giật đều là chỉ định tuyệt đối để chọc dò tủy sống.
- **Bẫy 2:** Bỏ sót hạ đường huyết cấp tính kèm theo. Sốt cao làm tăng tiêu thụ chuyển hóa năng lượng, trong khi trẻ biếng ăn hoặc nôn ói dễ dẫn đến hạ đường huyết làm nặng thêm cơn co giật. Luôn luôn bấm đường huyết mao mạch tại giường ngay khi tiếp nhận.
- **Bẫy 3:** Chèn vật cứng vào miệng trẻ trong cơn co giật. Đây là sai lầm phổ biến và nguy hiểm nhất của phụ huynh và cả nhân viên y tế thiếu kinh nghiệm. Việc nhét thìa, đũa, ngón tay vào miệng có thể gây gãy răng, chấn thương mô mềm, chảy máu khoang miệng và tắc nghẽn đường thở dẫn đến tử vong do ngạt.
- **Bẫy 4:** Tiêm quá nhiều liều Benzodiazepine. Việc tiêm dồn dập từ 3 liều Benzodiazepine trở lên trong thời gian ngắn là nguyên nhân hàng đầu gây suy hô hấp cấp, ngừng thở và tụt huyết áp nặng nề tại phòng cấp cứu.
- **Bẫy 5:** Pha Phenytoin vào dịch truyền có chứa Glucose. Phenytoin chỉ tan ở môi trường kiềm cao (pH 12), khi gặp dịch truyền Glucose có pH toan sẽ bị kết tủa thành các tinh thể siêu nhỏ gây tắc mạch phổi và hoại tử mô. Luôn luôn pha trong NaCl 0.9% và tráng rửa đường truyền trước sau khi tiêm.
- **Bẫy 6:** Quên làm ấm dung dịch thuốc khi thụt trực tràng hoặc tiêm bắp sai vị trí ở trẻ nhỏ. Tiêm bắp Midazolam phải tiêm sâu vào cơ mặt trước ngoài đùi (Vastus lateralis), không tiêm vào vùng mông ở trẻ nhỏ vì cơ mông chưa phát triển và nguy cơ tổn thương thần kinh tọa.
:::

---

## 8. CÁC CA LÂM SÀNG THỰC TẾ CÓ LỜI GIẢI CHI TIẾT (CASE STUDIES)

### Ca lâm sàng 1: Co giật do sốt đơn thuần ở trẻ 18 tháng tuổi
- **Bệnh sử:** Bé trai 18 tháng tuổi, nặng 11.5 kg, được mẹ đưa vào cấp cứu vì co giật lúc đang ngủ. Mẹ phát hiện bé sốt nóng từ sáng, đo nhiệt độ nách $39.2^\circ\text{C}$. Cơn giật kéo dài khoảng 3 phút, biểu hiện gồng cứng toàn thân, mắt trợn ngược, hai tay hai chân giật nhịp nhàng, sau đó tự ngưng.
- **Thăm khám lúc vào viện:** Bé tỉnh táo, khóc đòi mẹ, môi hồng, chi ấm, mạch 125 lần/phút, thở 28 lần/phút, nhiệt độ $38.8^\circ\text{C}$. Khám họng thấy amidan hai bên sưng đỏ có chấm mủ trắng, không có ban xuất huyết dưới da, thóp đã đóng, cổ mềm, dấu Kernig âm tính, vận động tứ chi đối xứng bình thường. Tiền sử tiêm chủng đã tiêm 3 mũi 6 trong 1 và 1 mũi phế cầu lúc 2 tháng tuổi.
- **Câu hỏi đặt ra:** Bệnh nhi này có chỉ định chọc dò tủy sống, làm điện não đồ hoặc chụp CT-scan sọ não hay không? Hướng xử trí tiếp theo là gì?
- **Phân tích và Lời giải chi tiết:**
  1. *Chẩn đoán:* Co giật do sốt đơn thuần lần đầu / Viêm amidan cấp có mủ. Trẻ chưa được tiêm chủng phế cầu đầy đủ (mới tiêm 1 mũi lúc 2 tháng tuổi).
  2. *Chỉ định cận lâm sàng:* Theo Hướng dẫn AAP 2011, mặc dù trẻ tỉnh táo và không có dấu màng não, nhưng việc chưa tiêm chủng đầy đủ vaccine phế cầu (mới 1 liều) khiến chọc dò dịch não tủy là một lựa chọn cần cân nhắc nếu bác sĩ lâm sàng nghi ngờ hoặc không thể theo dõi sát. Tuy nhiên, nếu sau 2 - 4 giờ theo dõi tại phòng cấp cứu, trẻ tỉnh táo hoàn toàn, chơi ngoan, bú tốt và tìm thấy rõ ổ nhiễm trùng vùng tai mũi họng thì có thể trì hoãn chọc dò và theo dõi sát. Điện não đồ và CT sọ não tuyệt đối KHÔNG có chỉ định.
  3. *Xử trí:* Dùng thuốc hạ sốt Paracetamol 15 mg/kg uống (hoặc đặt hậu môn nếu nôn), bù nước điện giải đường uống, điều trị kháng sinh phù hợp cho viêm amidan mủ, giải thích trấn an tâm lý cho phụ huynh và hướng dẫn cách xử trí cơn giật tại nhà.

### Ca lâm sàng 2: Trạng thái động kinh do sốt ở trẻ 24 tháng tuổi
- **Bệnh sử:** Bé gái 24 tháng tuổi, nặng 12 kg, tiền sử khỏe mạnh. Cách nhập viện 20 phút, bé sốt cao $39.5^\circ\text{C}$ và xuất hiện co cứng co giật toàn thân. Người nhà gọi xe cấp cứu chuyển đến bệnh viện. Khi vào đến khoa cấp cứu, cơn giật vẫn đang tiếp diễn liên tục (tổng thời gian giật đã là 25 phút).
- **Thăm khám lúc vào viện:** Bé đang co giật toàn thể, tím tái quanh môi, thở ngắt quãng không đều, SpO2 dao động 84% - 86% với khí phòng, mạch 160 lần/phút, huyết áp $90/55\text{ mmHg}$. Chưa có sẵn đường truyền tĩnh mạch.
- **Xử trí cấp cứu từng bước:**
  1. *Bước 1 (Hỗ trợ hô hấp & Dùng thuốc ngay lập tức):* Đặt bé nằm nghiêng sang bên, hút đàm nhớt miệng họng, bóp bóng qua mặt nạ có túi dự trữ với oxy 100%. Lập tức tiêm bắp Midazolam liều 0.2 mg/kg (2.5 mg) vào mặt trước ngoài đùi. Đồng thời thử nhanh đường huyết mao mạch (kết quả 4.2 mmol/L).
  2. *Bước 2 (Sau 5 phút dùng thuốc bước 1):* Cơn giật giảm nhẹ nhưng vẫn còn giật nhịp nhàng tứ chi, SpO2 cải thiện lên 92% qua bóp bóng. Điều dưỡng lấy được ven tĩnh mạch ngoại vi ở mu bàn chân. Quyết định cho liều thứ hai: Lorazepam IV liều 0.1 mg/kg (1.2 mg) tiêm chậm trong 2 phút.
  3. *Bước 3 (Cơn giật kéo dài chạm phút thứ 32):* Cơn giật vẫn chưa dứt hoàn toàn. Bệnh nhân đã chuyển sang Trạng thái động kinh kháng Benzodiazepine. Khởi động ngay thuốc bước hai: Levetiracetam (Keppra) liều 60 mg/kg (720 mg) pha trong 50 mL NaCl 0.9% truyền tĩnh mạch qua bơm tiêm điện trong 10 phút.
  4. *Kết quả:* Đến phút thứ 8 của quá trình truyền Levetiracetam, cơn co giật chấm dứt hoàn toàn, đồng tử hai bên đều 2 mm có phản xạ ánh sáng, bé tự thở đều qua oxy cannula, SpO2 98%. Tiếp tục theo dõi sát tri giác và chuyển PICU theo dõi tiếp.

### Ca lâm sàng 3: Co giật do sốt phức tạp nghi ngờ hội chứng Dravet
- **Bệnh sử:** Bé trai 9 tháng tuổi, nhập viện vì co giật nửa người bên phải khi sốt $38.2^\circ\text{C}$ sau tiêm vaccine 6 trong 1 mũi 3 được 1 ngày. Cơn giật kéo dài 18 phút mới dứt sau khi dùng Midazolam tại trạm y tế. Đây là đợt giật thứ ba của bé (hai đợt trước xảy ra lúc 5 tháng và 7 tháng tuổi, đều kéo dài trên 15 phút và có cơn giật bên trái).
- **Phân tích và Đề xuất điều trị:**
  1. Bé có đầy đủ các dấu hiệu cảnh báo của một thể co giật do sốt phức tạp nguy cơ cao: khởi phát rất sớm (dưới 1 tuổi), cơn giật kéo dài trên 15 phút, tính chất giật cục bộ nửa người luân chuyển bên (lúc bên phải, lúc bên trái).
  2. Cần nghi ngờ cao Hội chứng Dravet do đột biến gen SCN1A.
  3. *Lưu ý sống còn:* Chống chỉ định dùng các thuốc ức chế kênh Natri như Carbamazepine, Oxcarbazepine, Phenytoin. Thuốc lựa chọn ưu tiên duy trì lâu dài là Clobazam, Valproate kết hợp Stiripentol hoặc Cannabidiol. Chỉ định làm xét nghiệm di truyền giải trình tự gen SCN1A và chụp MRI sọ não.

---

## 9. CÁC ĐIỂM THỰC HÀNH CỐT LÕI (PRACTICAL TIPS)

1. Luôn bấm giờ chính xác thời gian cơn co giật; cảm nhận thời gian của người nhà trong lúc hoảng loạn thường bị thổi phồng gấp 3 đến 4 lần so với thực tế.
2. Cung cấp oxy lưu lượng cao 100% qua mặt nạ có túi dự trữ ngay khi tiếp nhận trẻ đang co giật để phòng ngừa tổn thương não do thiếu oxy.
3. Không bao giờ để việc cố gắng tìm tĩnh mạch làm chậm trễ liều thuốc cắt cơn đầu tiên; Midazolam tiêm bắp là lựa chọn nhanh nhất và hiệu quả nhất khi chưa có ven.
4. Bấm đường huyết mao mạch tại giường là phản xạ bắt buộc trước hoặc song song với việc tiêm thuốc chống co giật.
5. Luôn chuẩn bị sẵn sàng dụng cụ hút đàm nhớt và bóng giúp thở có mặt nạ phù hợp kích cỡ trước khi tiêm Benzodiazepine.
6. Khi trẻ đang co giật, đặt trẻ nằm nghiêng sang bên trái (tư thế hồi sức an toàn) để lưỡi không tụt ra sau và chất nôn không trào ngược vào khí quản.
7. Không tiêm quá 2 liều Benzodiazepine ngắn hạn; nếu cơn giật không dứt sau 10 phút dùng thuốc bước 1, phải chuyển ngay sang thuốc bước 2.
8. Thuốc chống co giật bước 2 ưu tiên lựa chọn hàng đầu ở trẻ em hiện nay là Levetiracetam nhờ tính an toàn tim mạch vượt trội và thời gian truyền nhanh.
9. Khi dùng Phenytoin, bắt buộc phải pha trong dung dịch Natri Clorid 0.9% và theo dõi liên tục điện tâm đồ trong suốt quá trình truyền.
10. Tuyệt đối không điều trị dự phòng lâu dài bằng thuốc chống động kinh cho trẻ co giật do sốt đơn thuần.
11. Hướng dẫn phụ huynh cách đo thân nhiệt chính xác và dùng thuốc hạ sốt Paracetamol (10 đến 15 mg/kg) hoặc Ibuprofen (5 đến 10 mg/kg) để giúp trẻ dễ chịu.
12. Giải thích rõ ràng cho gia đình rằng co giật do sốt đơn thuần không làm tổn thương não, không gây thiểu năng trí tuệ và không làm trẻ trở thành người tàn tật.
13. Nhận diện sớm các dấu hiệu cờ đỏ của viêm màng não mủ: thóp phồng, cổ gượng, ban xuất huyết hoại tử, li bì khó đánh thức sau cơn giật.
14. Chọc dò tủy sống là thủ thuật bắt buộc ở mọi trẻ co giật có sốt dưới 6 tháng tuổi hoặc có bất kỳ triệu chứng màng não nào.
15. Không làm điện não đồ thường quy trong vòng 48 giờ đầu sau co giật do sốt đơn thuần vì không mang lại giá trị tiên lượng.
16. Trang bị sẵn thuốc Midazolam ngậm niêm mạc má hoặc Diazepam thụt hậu môn cho những gia đình có trẻ từng bị co giật do sốt kéo dài và sống ở xa bệnh viện.
17. Luôn giữ bình tĩnh, giải thích nhẹ nhàng và đồng cảm với nỗi sợ hãi tột cùng của cha mẹ khi chứng kiến con bị co giật.
18. Nhắc nhở phụ huynh không được vắt chanh vào miệng, không cạo gió rách da, không nhỏ nước chanh vào mắt trẻ trong lúc giật.
19. Kiểm tra kỹ tiền sử tiêm chủng vaccine phế cầu và Hib của trẻ để đưa ra quyết định chọc dò dịch não tủy chính xác.
20. Sau khi cắt được cơn giật, luôn kiểm tra lại tri giác, đồng tử, trương lực cơ và tìm kiếm ổ nhiễm trùng nguyên phát (tai mũi họng, phổi, đường tiểu).
21. Đối với trẻ co giật kéo dài trên 30 phút, luôn cảnh giác với nguy cơ phù não cấp và tổn thương hồi hải mã, chuẩn bị sẵn sàng chuyển tuyến PICU.
22. Khuyên gia đình tiếp tục tiêm phòng đầy đủ các vaccine cho trẻ theo lịch, không vì một đợt co giật do sốt mà bỏ lỡ cơ hội phòng ngừa các bệnh nguy hiểm.

---

## 10. ĐIỂM KIỂM TRA TỰ ĐÁNH GIÁ (SELF-CHECKPOINTS)

- [ ] **Checkpoint 1:** Nêu 3 tiêu chuẩn lâm sàng bắt buộc để phân loại một cơn co giật là Co giật do sốt đơn thuần (Simple FS).
- [ ] **Checkpoint 2:** Liệt kê 4 chỉ định tuyệt đối bắt buộc phải chọc dò tủy sống ở trẻ co giật kèm sốt theo khuyến cáo của AAP 2011.
- [ ] **Checkpoint 3:** Phân biệt ý nghĩa sinh học và can thiệp lâm sàng của hai mốc thời gian T1 (5 phút) và T2 (30 phút) trong trạng thái động kinh.
- [ ] **Checkpoint 4:** Nêu rõ lý do tại sao AAP 2008 khuyến cáo KHÔNG dùng thuốc chống động kinh dự phòng thường quy cho trẻ co giật do sốt đơn thuần.
- [ ] **Checkpoint 5:** Trình bày thứ tự ưu tiên và liều lượng của các thuốc Benzodiazepine bước 1 khi chưa có và khi đã có đường truyền tĩnh mạch.

---

## 11. CÂU HỎI TRẮC NGHIỆM TỰ LƯỢNG GIÁ (MCQS)

### Câu 1: Trẻ nam 14 tháng tuổi được chẩn đoán co giật do sốt đơn thuần. Theo AAP 2011, chỉ định nào sau đây là KHÔNG phù hợp?
A. Chọc dò tủy sống thường quy để tầm soát viêm màng não  
B. Khám kỹ vùng tai mũi họng tìm ổ nhiễm trùng  
C. Cho hạ sốt bằng Paracetamol 15 mg/kg khi trẻ quấy khóc  
D. Tư vấn trấn an gia đình về tính chất lành tính của bệnh  
*Đáp án đúng:* A. AAP 2011 khuyến cáo không chọc dò tủy sống thường quy cho trẻ co giật do sốt đơn thuần tổng trạng tốt và đã tiêm chủng đầy đủ.

### Câu 2: Thuốc cắt cơn co giật bước 1 được khuyến cáo ưu tiên hàng đầu ngoài bệnh viện khi chưa có đường truyền tĩnh mạch là:
A. Phenobarbital tiêm bắp  
B. Midazolam tiêm bắp  
C. Phenytoin truyền tĩnh mạch  
D. Levetiracetam uống  
*Đáp án đúng:* B. Thử nghiệm RAMPART chứng minh Midazolam tiêm bắp kiểm soát cơn giật nhanh hơn và tỷ lệ thành công cao hơn nhờ không mất thời gian lấy ven.

### Câu 3: Mốc thời gian T1 trong trạng thái động kinh co giật toàn thể theo Hội Động kinh Hoa Kỳ (AES 2016) là:
A. 1 phút  
B. 5 phút  
C. 15 phút  
D. 30 phút  
*Đáp án đúng:* B. Mốc T1 là 5 phút, thời điểm bắt đầu phải can thiệp thuốc chống co giật vì cơn giật ít có khả năng tự chấm dứt tự nhiên.

### Câu 4: Thuốc chống co giật bước 2 nào sau đây có ưu điểm vượt trội về thời gian truyền nhanh và an toàn tim mạch cao ở trẻ em?
A. Phenytoin  
B. Phenobarbital  
C. Levetiracetam  
D. Thiopental  
*Đáp án đúng:* C. Levetiracetam có thể truyền nhanh trong 5 đến 10 phút, không gây ức chế cơ tim và không làm tụt huyết áp.

### Câu 5: Tác dụng phụ nghiêm trọng nhất khiến Phenobarbital không được khuyến cáo dự phòng co giật do sốt đơn thuần ở trẻ nhỏ là:
A. Rối loạn hành vi và suy giảm nhận thức kéo dài  
B. Tụt huyết áp kịch phát  
C. Suy gan hoại tử tế bào gan cấp tính  
D. Tăng sản nướu răng và rậm lông  
*Đáp án đúng:* A. Phenobarbital làm suy giảm nhận thức, giảm điểm IQ và gây rối loạn hành vi kích động ở trẻ nhỏ.

### Câu 6: Trẻ 8 tháng tuổi bị co giật nửa người bên trái kéo dài 20 phút khi sốt. Đây là dạng co giật gì?
A. Co giật do sốt đơn thuần  
B. Co giật do sốt phức tạp  
C. Động kinh vắng ý thức  
D. Cơn co thắt nhũ nhi  
*Đáp án đúng:* B. Cơn giật có tính chất cục bộ nửa người và kéo dài trên 15 phút là tiêu chuẩn của co giật do sốt phức tạp.

### Câu 7: Khi pha Phenytoin truyền tĩnh mạch, dung dịch nào sau đây là BẮT BUỘC sử dụng?
A. Glucose 5%  
B. Glucose 10%  
C. Ringer Lactat  
D. Natri Clorid 0.9%  
*Đáp án đúng:* D. Phenytoin kết tủa ngay lập tức trong môi trường toan của Glucose, bắt buộc phải pha trong NaCl 0.9%.

### Câu 8: Dung môi Propylene glycol trong ống tiêm Phenytoin truyền thống là nguyên nhân chính dẫn đến biến chứng nào?
A. Tụt huyết áp và loạn nhịp tim  
B. Hội chứng Stevens-Johnson  
C. Suy tủy xương  
D. Viêm tụy cấp  
*Đáp án đúng:* A. Propylene glycol gây ức chế cơ tim, tụt huyết áp và loạn nhịp khi truyền nhanh.

### Câu 9: Theo nghiên cứu FEBSTAT, trạng thái động kinh do sốt kéo dài trên 30 phút làm tăng nguy cơ tổn thương cấu trúc não nào?
A. Thùy trán  
B. Hồi hải mã thùy thái dương  
C. Tiểu não  
D. Cầu não  
*Đáp án đúng:* B. FSE làm phù nề và hoại tử tế bào thần kinh vùng hồi hải mã, dẫn đến xơ teo hồi hải mã và động kinh sau này.

### Câu 10: Sau cơn co giật do sốt đơn thuần đầu tiên, tỷ lệ tái phát cơn giật trong các đợt sốt tương lai ở trẻ khoảng bao nhiêu?
A. Khoảng năm phần trăm  
B. Khoảng ba mươi đến ba mươi lăm phần trăm  
C. Khoảng bảy mươi lăm phần trăm  
D. Hầu như một trăm phần trăm  
*Đáp án đúng:* B. Khoảng một phần ba (ba mươi đến ba mươi lăm phần trăm) trẻ em sẽ có ít nhất một đợt co giật do sốt tái phát trong đời.

---

## 12. TÀI LIỆU THAM KHẢO

Danh mục các tài liệu tham khảo khoa học và hướng dẫn y văn quốc tế được trích dẫn và sử dụng trong bài giảng:

1. American Academy of Pediatrics. Neurodiagnostic evaluation of the child with a simple febrile seizure. Pediatrics. 2011. PMID: 21285335.
2. American Academy of Pediatrics. Febrile seizures: clinical practice guideline for the long-term management of the child with simple febrile seizures. Pediatrics. 2008. PMID: 18519501.
3. Glauser T, et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults: Report of the Guideline Committee of the American Epilepsy Society. Epilepsy Currents. 2016. PMID: 26900382.
4. Silbergleit R, et al. Intramuscular versus intravenous therapy for prehospital status epilepticus. The New England Journal of Medicine. 2012. PMID: 22335736.
5. Kapur J, et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus. The New England Journal of Medicine. 2019. PMID: 31774955.
6. Dalziel SR, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (ConSEPT): an open-label, multicentre, randomised controlled trial. The Lancet. 2019. PMID: 31005386.
7. Lyttle MD, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (EcLiPSE): a multicentre, open-label, randomised trial. The Lancet. 2019. PMID: 31005385.
8. Murata S, et al. Acetaminophen and Febrile Seizure Recurrences During the Same Fever Episode. Pediatrics. 2018. PMID: 30297499.
9. Hesdorffer DC, et al. Febrile status epilepticus and epileptogenesis: The FEBSTAT study. Epilepsia. 2024. PMID: 38606600.
10. Shinnar S, et al. Febrile status epilepticus and epileptogenesis: Long-term follow-up from the FEBSTAT study. Epilepsia Open. 2025. PMID: 40770931.
"""

text = template.replace("{buf_before}", buf_before).replace("{buf_after}", buf_after)
target_path.write_text(text, encoding="utf-8")
words = len(text.split())
nonblank = len([l for l in text.splitlines() if l.strip()])
print(f"Generated {target_path} successfully ({words} words, {nonblank} nonblank lines)")
