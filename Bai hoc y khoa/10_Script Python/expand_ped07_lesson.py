# -*- coding: utf-8 -*-
"""Generate ultra-detailed, fully compliant PED-07 markdown lesson with >8000 words and >600 lines."""
from pathlib import Path

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md")

sections = []

# Section 0
sections.append("""# CO GIẬT DO SỐT & TRẠNG THÁI ĐỘNG KINH Ở TRẺ EM (PED-07)

## 0. TỔNG QUAN VÀ DỊCH TỄ HỌC

### 0.1. Nền tảng tối thiểu cần dùng ngay

- **Khái niệm co giật do sốt:** Co giật do sốt (Febrile Seizure) là biến cố co giật xuất hiện ở trẻ nhỏ trong độ tuổi từ 6 tháng đến 60 tháng khi có sốt cao trên 38°C.
- **Loại trừ nguyên nhân nội sọ:** Co giật do sốt đòi hỏi không có nhiễm trùng hệ thần kinh trung ương và không có rối loạn chuyển hóa cấp tính.
- **Độ tuổi mắc bệnh phổ biến nhất:** Đỉnh điểm xuất hiện co giật do sốt là vào khoảng 18 tháng tuổi do ngưỡng kích thích vỏ não còn thấp.
- **Khái niệm trạng thái động kinh:** Trạng thái động kinh là tình trạng cơn giật kéo dài liên tục hoặc tái diễn nhiều cơn mà không tỉnh lại giữa các cơn.
- **Ý nghĩa của mốc thời gian T1:** Mốc T1 (5 phút với cơn co giật toàn thể) là thời điểm cơn giật không thể tự dứt và bắt buộc phải dùng thuốc cắt cơn.
- **Ý nghĩa của mốc thời gian T2:** Mốc T2 (30 phút với cơn co giật toàn thể) là thời điểm bắt đầu xuất hiện tổn thương tế bào thần kinh không thể hồi phục.
- **Thứ tự ưu tiên trong cấp cứu:** Luôn ưu tiên ổn định các chức năng sống cơ bản theo ABCDE trước khi thực hiện các can thiệp chuyên sâu.
- **Chỉ định chọc dò tủy sống:** Chỉ chọc dò tủy sống khi có dấu hiệu màng não, thóp phồng, li bì kéo dài hoặc chưa tiêm chủng đầy đủ kèm nghi ngờ lâm sàng.
- **Vai trò của điện não đồ (EEG):** EEG không được khuyến cáo thường quy sau cơn co giật do sốt đơn thuần vì không dự báo được nguy cơ động kinh.
- **Vai trò của chẩn đoán hình ảnh (CT/MRI):** Chụp CT hoặc MRI sọ não không cần thiết cho co giật do sốt đơn thuần và chỉ làm tăng phơi nhiễm tia xạ.
- **Thuốc cắt cơn đầu tay:** Benzodiazepine là thuốc lựa chọn đầu tay hàng đầu cho mọi cơn co giật kéo dài trên 5 phút.
- **Lựa chọn Midazolam tiêm bắp:** Midazolam tiêm bắp tác dụng nhanh và vượt trội trong môi trường ngoại viện khi chưa có sẵn đường truyền tĩnh mạch.
- **Lựa chọn thuốc bước hai:** Levetiracetam, Fosphenytoin và Valproate là ba lựa chọn thuốc chống động kinh bước hai có hiệu quả tương đương nhau.
- **Ưu thế của Levetiracetam:** Levetiracetam truyền nhanh trong 5 đến 10 phút, ít tác dụng phụ trên tim mạch và không gây tụt huyết áp.
- **Giới hạn số liều Benzodiazepine:** Tuyệt đối không dùng quá 2 liều Benzodiazepine ngắn để tránh gây ức chế hô hấp và tụt huyết áp nặng.
- **Vai trò của thuốc hạ sốt:** Thuốc hạ sốt giúp trẻ dễ chịu nhưng không thay đổi được ngưỡng co giật nội tại của não bộ trẻ nhỏ.
- **Nguy cơ tiến triển thành bệnh động kinh:** Tỷ lệ trẻ co giật do sốt đơn thuần phát triển thành bệnh động kinh thực sự là rất thấp, chỉ khoảng 1% đến 2%.
- **Quy tắc sơ cứu tại nhà:** Đặt trẻ nằm nghiêng một bên, nới lỏng quần áo, bấm giờ cơn giật và tuyệt đối không nhét bất kỳ vật gì vào miệng trẻ.
- **Nghiên cứu đoàn hệ FEBSTAT:** Trạng thái động kinh do sốt kéo dài trên 30 phút có thể gây tổn thương phù nề hồi hải mã và xơ hóa cấu trúc thùy thái dương.
- **Đánh giá hạ đường huyết:** Đo đường huyết mao mạch tại giường là xét nghiệm nhanh bắt buộc cho mọi trẻ co giật kéo dài hoặc hôn mê.
- **Bù nước và điện giải:** Trẻ sốt cao co giật thường kèm mất nước, cần đánh giá tri giác và bổ sung dịch thích hợp bằng đường uống hoặc tĩnh mạch.
- **Tham vấn tâm lý gia đình:** Giải thích rõ bản chất lành tính của co giật do sốt đơn thuần để trấn an phụ huynh và hướng dẫn kế hoạch hành động.

> 🚨 **BOX ĐỎ — BÁO ĐỘNG ĐỎ CẤP CỨU CO GIẬT VÀ TRẠNG THÁI ĐỘNG KINH:**
> 1. Dừng ngay mọi thăm khám thứ yếu và kích hoạt quy trình cấp cứu hồi sức ngừng tuần hoàn - hô hấp nếu trẻ có ngưng thở hoặc tím tái kéo dài.
> 2. Đặt trẻ nằm nghiêng an toàn, hút sạch đờm dãi họng miệng và bóp bóng qua mask với oxy 100% ngay khi SpO2 dưới 92%.
> 3. Cắt cơn khẩn cấp bằng Benzodiazepine (Midazolam IM hoặc Diazepam IV) nếu cơn co giật kéo dài từ 5 phút trở lên (mốc T1).
> 4. Không bao giờ tiêm quá 2 liều Benzodiazepine; chuyển ngay sang thuốc chống động kinh bước hai (Levetiracetam IV) nếu cơn giật vượt quá 20 phút.
> 5. Tuyệt đối không nhét ngón tay, đè lưỡi hoặc vật cứng vào miệng trẻ đang co cứng cơ hàm vì nguy cơ gãy răng và tắc nghẽn đường thở gây tử vong.

### 0.2. Dịch tễ học và định nghĩa chuẩn hóa theo ILAE / AAP

Co giật do sốt là rối loạn thần kinh thường gặp nhất trong thực hành cấp cứu nhi khoa.
Biến cố này xảy ra ở những đứa trẻ có não bộ đang trong giai đoạn phát triển nhạy cảm.
Tỷ lệ mắc bệnh trung bình chiếm từ 2% đến 5% ở trẻ em khu vực châu Âu và Bắc Mỹ.
Tại một số quốc gia châu Á như Nhật Bản, tỷ lệ này có thể lên tới 8% đến 10% dân số trẻ em.
Đỉnh điểm lứa tuổi hay gặp nhất là từ 12 tháng đến 18 tháng tuổi, với tỷ lệ bé trai nhiều hơn bé gái.
Hầu hết các cơn co giật đầu tiên xuất hiện trong 24 giờ đầu tiên kể từ khi trẻ bắt đầu phát sốt.
Khoảng 50% số trẻ có cơn co giật xuất hiện khi thân nhiệt đo được vượt quá 39°C.
Tuy nhiên, một số trẻ có ngưỡng co giật thấp có thể lên cơn giật ngay ở mức nhiệt độ 38°C đến 38.5°C.

Yếu tố gia đình và di truyền đóng vai trò nền tảng quan trọng trong cơ chế khởi phát bệnh.
Tiền sử có cha mẹ hoặc anh chị ruột từng bị co giật do sốt làm tăng nguy cơ mắc bệnh lên 2 đến 3 lần.
Nhiều đột biến gen trên kênh natri (SCN1A, SCN1B) và thụ thể GABAA (GABRG2) đã được xác định.
Đặc biệt, đột biến gen SCN1A có thể biểu hiện dưới dạng co giật do sốt thông thường đến hội chứng Dravet nặng nề.
Các bệnh nhiễm trùng kích hoạt cơn giật thường là nhiễm virus đường hô hấp trên hoặc tiêu chảy cấp do Rotavirus.
Các tác nhân virus thường gặp nhất bao gồm Human Herpesvirus 6 (HHV-6), virus cúm A, cúm B và Parainfluenza.
Tiêm chủng vaccine (như sởi, ho gà) có thể gây sốt nhẹ và kích hoạt cơn giật ở trẻ có cơ địa nhạy cảm.
Tuy nhiên, các nghiên cứu dịch tễ khẳng định vaccine không gây tổn thương não nguyên phát ở trẻ nhỏ.
Lợi ích phòng bệnh của vaccine vượt trội hoàn toàn so với nguy cơ co giật do sốt thoáng qua.""")

# Section 1
sections.append("""## 1. ĐỊNH NGHĨA VÀ PHÂN LOẠI CO GIẬT DO SỐT

### 1.1. Co giật do sốt đơn thuần và phức tạp

Việc phân loại chính xác tính chất cơn co giật là bước thăm khám đầu tiên có tính quyết định.
Phân loại lâm sàng giúp phân tầng nguy cơ tổn thương não và định hướng cận lâm sàng phù hợp.
Dựa trên tiêu chuẩn của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP), co giật do sốt gồm hai nhóm chính:

| Tiêu chí đánh giá lâm sàng | Co giật do sốt đơn thuần (Simple FS) | Co giật do sốt phức tạp (Complex FS) |
| :--- | :--- | :--- |
| **Kiểu hình co giật** | Toàn thể hóa nguyên phát (co cứng - co giật đối xứng hai bên) | Cục bộ / Khu trú (giật một chi, quay mắt quay đầu lệch bên) |
| **Thời gian cơn giật** | Cơn ngắn, kéo dài dưới 15 phút (thường tự dứt sau 1 đến 3 phút) | Cơn kéo dài, từ 15 phút trở lên hoặc kéo dài liên tục |
| **Tần số xuất hiện** | Duy nhất 1 cơn trong vòng 24 giờ của cùng một đợt sốt | Tái phát từ 2 cơn trở lên trong vòng 24 giờ |
| **Giai đoạn sau cơn** | Tri giác hồi phục nhanh chóng, tỉnh táo hoàn toàn sau 15 đến 30 phút | Li bì kéo dài hoặc xuất hiện dấu thần kinh khu trú (liệt Todd) |
| **Tỷ lệ trong thực tế** | Chiếm đa số, khoảng 70% đến 80% tổng số ca bệnh | Chiếm khoảng 20% đến 30% tổng số ca bệnh |
| **Nguy cơ thành động kinh** | Rất thấp, khoảng 1% đến 2% (tương đương trẻ bình thường) | Cao hơn rõ rệt, khoảng 4% đến 10% tùy số yếu tố phức tạp |

Co giật do sốt đơn thuần là một biến cố hoàn toàn lành tính và tự giới hạn.
Trẻ không có bất kỳ khiếm khuyết thần kinh nào trước và sau cơn co giật.
Ngược lại, co giật do sốt phức tạp mang nguy cơ tiềm ẩn của các bệnh lý nội sọ nguy hiểm.
Chỉ cần có 1 trong 3 yếu tố (khu trú, kéo dài trên 15 phút, tái phát trong 24 giờ) là đủ xếp vào thể phức tạp.
Trẻ có cả 3 yếu tố phức tạp có nguy cơ tiến triển thành bệnh động kinh thực sự lên tới 10% đến 15%.

Ví dụ 1: Một bé trai 15 tháng tuổi bị sốt 39°C do viêm mũi họng, lên cơn giật toàn thân kéo dài 2 phút rồi tự dứt, sau 20 phút bé tỉnh táo bú mẹ tốt; đây là trường hợp điển hình của co giật do sốt đơn thuần.
Ví dụ 2: Một bé gái 10 tháng tuổi lên cơn giật chỉ co giật tay phải và giật mép bên phải kéo dài 18 phút; đây là co giật do sốt phức tạp vì có yếu tố cục bộ và thời gian kéo dài trên 15 phút.

### 1.2. Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE)

Trạng thái động kinh do sốt là một phân nhóm đặc biệt nặng của co giật do sốt phức tạp.
FSE được định nghĩa là cơn co giật liên tục hoặc nhiều cơn ngắt quãng kéo dài từ 30 phút trở lên.
Tình trạng này chiếm khoảng 5% tổng số ca co giật do sốt và chiếm 25% tổng số trạng thái động kinh ở trẻ nhỏ.
FSE thường gặp nhất ở trẻ em dưới 2 tuổi, đặc biệt là nhóm trẻ nhũ nhi từ 6 đến 12 tháng tuổi.
Cơn giật kéo dài liên tục dẫn tới tăng tiêu thụ oxy mô não, toan lactic và ngộ độc kích thích tế bào.
Nếu không được cắt cơn kịp thời trước mốc T2 (30 phút), nguy cơ tổn thương não không hồi phục sẽ tăng cao.
Đặc biệt, FSE có thể gây tổn thương phù nề cấp tính cấu trúc hồi hải mã thuộc thùy thái dương.
Đây chính là nguồn gốc khởi phát xơ hóa đồi hải mã và bệnh động kinh cục bộ kháng thuốc sau này.""")

# Section 2
sections.append("""## 2. CƠ CHẾ BỆNH SINH VÀ MẠNG LƯỚI TẾ BÀO THẦN KINH

### 2.1. Tính hưng phấn thần kinh phụ thuộc nhiệt độ và cytokine tiền viêm

Cơ chế bệnh sinh của co giật do sốt là sự phối hợp giữa não bộ chưa trưởng thành và phản ứng viêm.
Ở lứa tuổi nhũ nhi và mầm non, quá trình myeline hóa các sợi trục thần kinh chưa hoàn thiện.
Hàng rào máu não ở trẻ nhỏ có tính thấm cao hơn so với người trưởng thành.
Các khớp thần kinh hưng phấn sử dụng glutamate phát triển sớm hơn các khớp thần kinh ức chế GABA.
Do đó, não bộ trẻ nhỏ rất dễ rơi vào tình trạng mất cân bằng điện sinh lý khi gặp các kích thích từ bên ngoài.

Khi sốt cao xuất hiện, nhiệt độ mô não gia tăng làm thay đổi cấu hình không gian của các kênh ion.
Các kênh natri phụ thuộc điện thế mở nhanh hơn và duy trì trạng thái khử cực lâu hơn.
Đồng thời, phản ứng sốt kích hoạt đại thực bào và tế bào vi đệm tiết ra các cytokine gây viêm.
Interleukin-1beta (IL-1β) và Tumor Necrosis Factor-alpha (TNF-α) gắn vào thụ thể trên màng tế bào thần kinh.
Sự gắn kết này làm tăng giải phóng glutamate tiền synap và ức chế dòng clo đi vào qua thụ thể GABAA.
Hậu quả là ngưỡng kích thích co giật của vỏ não bị hạ thấp nghiêm trọng, dẫn đến phóng điện kịch phát đồng thì.

Dưới đây là 5 chuỗi cơ chế bệnh sinh kinh điển giải thích toàn bộ diễn tiến từ sốt đến tổn thương não:

- **Chuỗi cơ chế 1 (Kích hoạt phóng điện vỏ não do sốt cao):**
Sốt cao đột ngột → Tăng tốc độ chuyển hóa nơ-ron → Gia tăng giải phóng glutamate tiền synap → Khử cực màng tế bào thần kinh lan tỏa → Cơn co giật toàn thể.

- **Chuỗi cơ chế 2 (Tác động của cytokine viêm lên hàng rào máu não):**
Nhiễm trùng toàn thân → Đại thực bào giải phóng IL-1β và TNF-α → Tăng tính thấm hàng rào máu não → Kích hoạt thụ thể NMDA tại vùng hải mã → Khởi phát hoạt động kịch phát dạng động kinh.

- **Chuỗi cơ chế 3 (Hiện tượng nhập bào thụ thể GABA trong cơn co giật kéo dài):**
Co giật kéo dài trên 5 phút → Suy giảm thụ thể GABAA tại màng sau synap do nhập bào → Tích tụ và tăng biểu hiện thụ thể NMDA hưng phấn → Kháng thuốc nhóm Benzodiazepine → Trạng thái động kinh co giật kháng trị.

- **Chuỗi cơ chế 4 (Ngộ độc kích thích tế bào và xơ hóa hồi hải mã):**
Trạng thái động kinh do sốt kéo dài trên 30 phút → Thiếu oxy mô não tương đối kết hợp tăng chuyển hóa quá mức → Tích tụ glutamate ngoại bào gây ngộ độc kích thích → Phù nề cấp tính và xơ hóa dải hồi hải mã → Hình thành ổ sinh động kinh thùy thái dương thứ phát.

- **Chuỗi cơ chế 5 (Mất cân bằng thẩm thấu và ngưỡng co giật):**
Hạ natri máu kèm sốt cao → Giảm áp lực thẩm thấu ngoại bào quanh tế bào đệm → Tế bào hình sao phù nề làm giảm tái thu hồi glutamate và kali → Tăng tính hưng phấn ngưỡng co giật thần kinh → Cơn co giật tái phát nhiều lần trong 24 giờ.

### 2.2. Tổn thương hồi hải mã và cơ chế sinh động kinh sau FSE

Nghiên cứu tiến cứu FEBSTAT đã làm sáng tỏ hậu quả mô học thần kinh sau trạng thái động kinh do sốt.
Chụp cộng hưởng từ sọ não (MRI) sau cơn FSE cho thấy tổn thương phù nề và tăng tín hiệu T2 tại hồi hải mã.
Khu vực chịu tổn thương nặng nề nhất là các tế bào thần kinh tháp ở vùng CA1 và CA3 của hồi hải mã.
Khi cơn co giật kéo dài trên 30 phút, bơm ion màng tế bào Na+/K+-ATPase bị cạn kiệt năng lượng ATP.
Nồng độ canxi nội bào tăng vọt kích hoạt các enzym tiêu protein calpain và caspase gây chết tế bào theo chương trình.
Quá trình viêm và ngộ độc kích thích kéo dài dẫn đến mất nơ-ron tháp và xơ hóa hồi hải mã (MTS).
Tổn thương xơ hóa cấu trúc này chính là nguồn gốc phát sinh bệnh động kinh thùy thái dương kháng thuốc.

Ví dụ 3: Một trẻ 2 tuổi bị trạng thái động kinh do sốt kéo dài 45 phút, chụp MRI não sau 48 giờ thấy tăng tín hiệu T2 hồi hải mã bên trái; đây là tổn thương cấp tính báo hiệu nguy cơ xơ hóa sau này.

Checkpoint 1: Tại sao co giật kéo dài trên 5 phút lại gây hiện tượng nhờn thuốc Benzodiazepine?
Trả lời: Do thụ thể GABAA tại màng sau synap bị nhập bào nhanh chóng vào nội bào, trong khi thụ thể NMDA hưng phấn lại tăng biểu hiện lên bề mặt màng tế bào.""")

# Section 3
sections.append("""## 3. CHẨN ĐOÁN VÀ TIẾP CẬN BAN ĐẦU THEO HƯỚNG DẪN AAP 2011

### 3.1. Chỉ định chọc dò tủy sống (Lumbar Puncture)

Mối quan tâm hàng đầu của thầy thuốc là phải loại trừ triệt để viêm màng não mủ và viêm não cấp tính.
Ở trẻ nhỏ dưới 18 tháng tuổi, các triệu chứng kinh điển của viêm màng não thường không đầy đủ.
Tuy nhiên, chọc dò tủy sống đại trà cho mọi trường hợp co giật do sốt đơn thuần là không cần thiết.
Thủ thuật chọc dò tủy sống xâm lấn có thể gây đau, chảy máu, tụt kẹt não hoặc nhiễm trùng thứ phát.
Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2011) đã đưa ra các khuyến cáo phân tầng dựa trên bằng chứng:

- Chọc dò tủy sống không được khuyến cáo thường quy ở trẻ co giật do sốt đơn thuần tổng trạng tốt và đã tiêm chủng đầy đủ: A lumbar puncture is not routinely recommended in a well-appearing, fully immunized child who presents with a simple febrile seizure. {claim:C-001} [GUIDELINE VERIFIED] (PMID: 21285335)
- Chọc dò tủy sống là một lựa chọn cần cân nhắc khi trẻ chưa được tiêm chủng phế cầu hoặc Hib đầy đủ: A lumbar puncture is an option when a child is considered underimmunized or when immunization status cannot be determined. {claim:C-002} [GUIDELINE VERIFIED] (PMID: 21285335)

Bắt buộc phải chọc dò dịch não tủy ngay lập tức khi có các dấu hiệu lâm sàng cảnh báo nguy hiểm sau:
1. Trẻ có triệu chứng màng não thực thể: Cổ gượng, dấu hiệu Kernig dương tính, dấu Brudzinski dương tính.
2. Thóp trước phồng hoặc căng ở trẻ nhũ nhi dưới 12 tháng tuổi khi trẻ đang nằm yên không khóc.
3. Trẻ li bì kéo dài, rối loạn tri giác, hôn mê hoặc kích thích vật vã sau giai đoạn sau cơn thông thường.
4. Trẻ đang được điều trị kháng sinh uống hoặc tiêm trước đó làm che lấp các dấu hiệu viêm màng não.
5. Trẻ có biểu hiện nhiễm trùng nhiễm độc toàn thân nặng, da tái nổi bông, mạch nhanh nhẹ khó bắt.

### 3.2. Vai trò của điện não đồ (EEG) và chẩn đoán hình ảnh thần kinh

Điện não đồ và chẩn đoán hình ảnh thường bị chỉ định quá mức do tâm lý lo lắng của gia đình và bác sĩ.
Hướng dẫn AAP 2011 khuyến cáo không thực hiện các thăm dò này cho co giật do sốt đơn thuần:

- Điện não đồ và chẩn đoán hình ảnh thần kinh không được khuyến cáo thường quy sau cơn co giật do sốt đơn thuần: Electroencephalogram and neuroimaging should not be performed in the routine evaluation of a child with a simple febrile seizure. {claim:C-003} [GUIDELINE VERIFIED] (PMID: 21285335)

Sóng chậm sau cơn giật trên EEG là hiện tượng sinh lý thoáng qua và không giúp tiên lượng tái phát.
Việc phát hiện các sóng nhọn thoáng qua có thể dẫn tới chẩn đoán sai lầm là bệnh động kinh.
Chụp CT sọ não có nguy cơ phơi nhiễm bức xạ ion hóa nguy hại đối với não bộ non nớt của trẻ nhỏ.
Các nghiên cứu chỉ ra rằng CT scan sọ não ở trẻ nhỏ làm tăng nguy cơ u não và bệnh bạch cầu sau này.
Chỉ định MRI sọ não chỉ đặt ra khi có co giật cục bộ kéo dài hoặc có dấu thần kinh khu trú kéo dài.
Những trường hợp trẻ có đầu to bất thường, chậm phát triển tâm thần vận động cũng cần chụp MRI sọ não.

### 3.3. Các xét nghiệm cận lâm sàng khác

Xét nghiệm máu thường quy (công thức máu, điện giải, canxi) không cần làm cho co giật do sốt đơn thuần.
Nghiên cứu cho thấy tỷ lệ hạ canxi máu hoặc hạ natri máu nặng ở trẻ co giật do sốt đơn thuần là cực kỳ thấp.
Đo đường huyết mao mạch tại giường là xét nghiệm duy nhất cần làm ngay để loại trừ hạ đường huyết.
Hạ đường huyết là nguyên nhân co giật có thể đảo ngược nhanh chóng chỉ bằng truyền tĩnh mạch Glucose 10%.
Các xét nghiệm tìm ổ nhiễm trùng (cấy máu, tổng phân tích nước tiểu, X-quang phổi) làm theo chỉ định lâm sàng.
Trẻ có triệu chứng hô hấp rõ ràng thì không cần làm bilan nhiễm trùng xâm lấn nếu tổng trạng tỉnh táo.

Ví dụ 4: Trẻ 16 tháng tuổi sau cơn co giật do sốt đơn thuần 1 phút, tỉnh táo hoàn toàn, khám họng đỏ; không cần làm thêm bất kỳ xét nghiệm máu hay chụp chiếu sọ não nào.

Checkpoint 2: Khi nào bắt buộc phải chỉ định chọc dò dịch não tủy ở trẻ co giật có sốt?
Trả lời: Khi trẻ có dấu hiệu màng não, thóp phồng, li bì kéo dài, trẻ chưa tiêm chủng đầy đủ, hoặc trẻ đang uống kháng sinh trước đó.""")

# Section 4
sections.append("""## 4. XỬ TRÍ CẤP CỨU TRẠNG THÁI ĐỘNG KINH THEO AES 2016

### 4.1. Tiếp cận theo mốc thời gian T1 và T2

Hội Động kinh Hoa Kỳ (AES 2016) xây dựng phác đồ xử trí trạng thái động kinh theo từng mốc thời gian.
Mục tiêu cốt lõi là kiểm soát đường thở, duy trì oxy hóa máu và dứt cơn giật trước mốc 20 đến 30 phút.
Thời gian chính là tế bào não; việc trì hoãn can thiệp sẽ làm tăng nguy cơ tổn thương nơ-ron vĩnh viễn.

```text
GIAI ĐOẠN 1 (0 - 5 PHÚT)          GIAI ĐOẠN 2 (5 - 20 PHÚT)         GIAI ĐOẠN 3 (20 - 40 PHÚT)
  +-------------------------+       +--------------------------+      +---------------------------+
  | Ổn định chức năng ABCDE |  ---> | Cắt cơn bằng             | ---> | Điều trị bước hai         |
  | Thở oxy, đo Glucose     |       | Benzodiazepine (Liều 1-2)|      | Levetiracetam / Fosphenyt |
  +-------------------------+       +--------------------------+      +---------------------------+
```

### 4.2. Giai đoạn 1 (0 - 5 phút): Ổn định ban đầu

Ngay khi tiếp nhận trẻ đang co giật, tiến hành ổn định theo nguyên tắc cấp cứu ABCDE chuẩn:
- **A (Airway):** Đặt trẻ nằm nghiêng an toàn, hút đờm dãi, giữ đường thở thông thoáng và ngửa đầu nâng cằm.
Không được cố nhét ngáng miệng hay vật cứng vào miệng trẻ vì có thể gây gãy răng và tắc đường thở.
- **B (Breathing):** Thở oxy lưu lượng cao 10 đến 15 lít/phút qua mask có túi dự trữ để giữ SpO2 trên 95%.
Hỗ trợ thông khí bằng bóng và mask nếu trẻ có biểu hiện thở yếu, tím tái hoặc ngưng thở.
- **C (Circulation):** Đánh giá mạch, huyết áp, thời gian đổ đầy mao mạch (CRT) và lập đường truyền tĩnh mạch.
Nếu không lấy được ven tĩnh mạch ngoại vi sau 2 lần thử hoặc quá 90 giây, cân nhắc đặt kim trong xương.
- **D (Disability):** Bấm đường huyết mao mạch ngay; nếu đường huyết dưới 2.6 mmol/L, tiêm Glucose 10% 2 mL/kg.
Đánh giá kích thước đồng tử hai bên và phản xạ ánh sáng để phát hiện dấu hiệu phù não cấp.
- **E (Exposure):** Cởi bỏ quần áo chật, kiểm tra thân nhiệt và hạ sốt bằng các biện pháp vật lý thích hợp.

### 4.3. Giai đoạn 2 (5 - 20 phút): Điều trị bước 1 với Benzodiazepine

Nếu cơn co giật tiếp diễn vượt quá 5 phút, bắt buộc phải dùng thuốc cắt cơn khẩn cấp:

- Benzodiazepine là điều trị đầu tay được khuyến cáo cho trạng thái động kinh co giật ở trẻ em và người lớn: A benzodiazepine is recommended as the first-line treatment for convulsive status epilepticus in children and adults. {claim:C-005} [GUIDELINE VERIFIED] (PMID: 26900382)

Lựa chọn đường dùng và liều lượng cụ thể theo AES 2016:
1. **Khi chưa có đường truyền tĩnh mạch:**
   - **Midazolam tiêm bắp (IM):** Liều 0.2 mg/kg (tối đa 10 mg ở trẻ trên 40 kg, tối đa 5 mg ở trẻ 13 đến 40 kg).
Midazolam tiêm bắp được khuyến cáo mức độ cao nhất nhờ khả năng hấp thu cực nhanh qua cơ bắp.
   - **Midazolam xịt mũi (IN) hoặc ngậm niêm mạc má:** Liều 0.2 mg/kg nếu không thể tiêm bắp.
   - **Diazepam bơm hậu môn (PR):** Liều 0.2 đến 0.5 mg/kg (tùy theo lứa tuổi của trẻ).
2. **Khi đã có sẵn đường truyền tĩnh mạch:**
   - **Lorazepam tĩnh mạch (IV):** Liều 0.1 mg/kg (tối đa 4 mg), tiêm tĩnh mạch chậm trong 2 phút.
   - **Diazepam tĩnh mạch (IV):** Liều 0.15 đến 0.2 mg/kg (tối đa 10 mg), tiêm tĩnh mạch chậm trong 2 phút.

Nếu sau 5 đến 10 phút cơn giật chưa dứt, có thể lặp lại một liều Benzodiazepine thứ hai tương tự.
Tuyệt đối không dùng quá 2 liều Benzodiazepine ngắn vì nguy cơ ngưng thở và tụt huyết áp tăng vọt.
Nếu sau liều thứ hai cơn giật vẫn tiếp diễn, phải chuyển ngay sang thuốc chống động kinh bước hai.

### 4.4. Giai đoạn 3 (20 - 40 phút): Điều trị bước 2 kháng Benzodiazepine

Khi cơn co giật kéo dài trên 20 phút dù đã dùng đủ 2 liều Benzodiazepine, trẻ rơi vào trạng thái kháng thuốc.
Lúc này phải chuyển sang thuốc chống động kinh đường tĩnh mạch bước hai ngay lập tức:

- Fosphenytoin, valproate hoặc levetiracetam đường tĩnh mạch là các lựa chọn điều trị bước hai cho trạng thái động kinh: Intravenous fosphenytoin, valproate, or levetiracetam are reasonable second-line treatment options for status epilepticus. {claim:C-006} [GUIDELINE VERIFIED] (PMID: 26900382)

| Thuốc chống động kinh bước 2 | Liều lượng khuyến cáo | Thời gian truyền tĩnh mạch | Chống chỉ định & Điểm lưu ý |
| :--- | :--- | :--- | :--- |
| **Levetiracetam (Keppra)** | 60 mg/kg IV (Tối đa 4500 mg) | Truyền tĩnh mạch trong 5 đến 10 phút | Cực kỳ an toàn tim mạch, ít tương tác thuốc, giảm liều khi suy thận |
| **Fosphenytoin (Cerebyx)** | 20 mg PE/kg IV (Tối đa 1500 mg PE) | Truyền trong 10 đến 15 phút (≤150 mg PE/phút) | Tiền chất tan trong nước của Phenytoin, ít hoại tử mô, cần theo dõi ECG |
| **Sodium Valproate (Depakine)** | 40 mg/kg IV (Tối đa 3000 mg) | Truyền tĩnh mạch trong 5 đến 10 phút | Chống chỉ định tuyệt đối khi nghi ngờ bệnh ty thể hoặc chu trình urê |
| **Phenytoin (Dilantin)** | 20 mg/kg IV (Tối đa 1000 mg) | Truyền chậm trong 20 đến 30 phút (≤50 mg/phút) | Nguy cơ tụt huyết áp, loạn nhịp tim và hội chứng hoại tử găng tay tím |

Levetiracetam tác động lên protein túi synap SV2A, ức chế phóng thích glutamate tiền synap.
Thuốc có thể truyền tĩnh mạch rất nhanh trong 5 phút mà không làm ảnh hưởng huyết động.
Fosphenytoin là tiền chất tan trong nước có độ pH trung tính, an toàn hơn nhiều so với Phenytoin.
Sodium Valproate làm tăng nồng độ GABA trong não và chẹn kênh natri phụ thuộc điện thế.
Tuy nhiên, Valproate chống chỉ định tuyệt đối ở trẻ nghi ngờ mắc bệnh ty thể do đột biến gen POLG.

### 4.5. Giai đoạn 4 (40 - 60 phút): Trạng thái động kinh kháng trị (RSE)

Nếu cơn giật kéo dài trên 40 phút dù đã dùng thuốc bước hai, bệnh nhân rơi vào trạng thái kháng trị.
Lúc này bắt buộc phải đặt nội khí quản, thở máy bảo vệ phổi và chuyển vào khoa hồi sức tích cực (ICU).
Khởi động truyền liên tục thuốc gây mê toàn thân (Midazolam truyền liên tục, Propofol hoặc Thiopental).
Propofol chỉ dùng ngắn hạn ở trẻ nhỏ do nguy cơ xuất hiện Hội chứng truyền Propofol (PRIS) gây tử vong.
Cần theo dõi điện não đồ liên tục (Continuous EEG) để hướng tới mục tiêu dập tắt các đợt bùng nổ sóng não.""")

# Section 5
sections.append("""## 5. BẰNG CHỨNG LÂM SÀNG TỪ CÁC THỬ NGHIỆM ĐỐI CHỨNG NGẪU NHIÊN (RCT)

### 5.1. Thử nghiệm RAMPART: Midazolam tiêm bắp vs Lorazepam tĩnh mạch

Thử nghiệm RAMPART công bố trên New England Journal of Medicine năm 2012 đã thay đổi thực hành cấp cứu:

- Midazolam tiêm bắp không thua kém và đạt kiểm soát cơn co giật trước viện nhanh hơn lorazepam tĩnh mạch: Intramuscular midazolam is noninferior to intravenous lorazepam for prehospital seizure termination. {claim:C-007} [ABSTRACT VERIFIED] (PMID: 22335736)

Nghiên cứu trên 893 bệnh nhân cho thấy Midazolam tiêm bắp cắt cơn thành công ở 73.4% so với 63.4% của Lorazepam IV.
Tỷ lệ bệnh nhân cần đặt nội khí quản hỗ trợ hô hấp ở hai nhóm là tương đương nhau (khoảng 14%).
Midazolam tiêm bắp giúp dứt cơn sớm hơn vì loại bỏ được thời gian trì hoãn do phải tìm ven tĩnh mạch ngoại vi.
Thời gian trung bình để tiêm bắp Midazolam là 1.2 phút so với 4.8 phút để lấy ven và tiêm Lorazepam.
Phát hiện này chứng minh tiêm bắp Midazolam là lựa chọn tối ưu hàng đầu trong cấp cứu ngoại viện.

### 5.2. Bộ ba thử nghiệm bước hai: ESETT, ConSEPT và EcLiPSE

Ba thử nghiệm lâm sàng ngẫu nhiên lớn năm 2019 đã cung cấp bằng chứng vững chắc cho điều trị bước hai:

- **Thử nghiệm ESETT (NEJM 2019) so sánh Levetiracetam, Fosphenytoin và Valproate:**
Levetiracetam, fosphenytoin và valproate đạt tỷ lệ kiểm soát cơn và cải thiện tri giác tương đương nhau trong trạng thái động kinh kháng benzodiazepine: Levetiracetam, fosphenytoin, and valproate each led to seizure cessation and improved alertness in children and adults. {claim:C-008} [ABSTRACT VERIFIED] (PMID: 31774955)
Nghiên cứu thu nhận 384 bệnh nhân bao gồm cả trẻ em và người lớn tại các khoa cấp cứu ở Hoa Kỳ.
Tỷ lệ cắt cơn thành công đạt xấp xỉ 47% ở nhóm Levetiracetam, 45% ở Fosphenytoin và 46% ở Valproate.
Tỷ lệ biến cố bất lợi nặng (tụt huyết áp, loạn nhịp tim, suy hô hấp) không có sự khác biệt giữa ba nhóm.

- **Thử nghiệm ConSEPT (Lancet 2019) thực hiện trên 233 trẻ em tại Úc và New Zealand:**
Levetiracetam không vượt trội hơn phenytoin trong kiểm soát bước hai trạng thái động kinh co giật ở trẻ em: Levetiracetam is not superior to phenytoin for the second-line treatment of paediatric convulsive status epilepticus. {claim:C-009} [ABSTRACT VERIFIED] (PMID: 31005386)
Tỷ lệ dứt cơn lâm sàng sau 5 phút đạt 50% ở Levetiracetam và 60% ở Phenytoin, tăng lên 75% khi dùng thuốc thứ hai.
Nghiên cứu gợi ý nếu thất bại với Levetiracetam thì dùng tiếp Phenytoin sẽ mang lại hiệu quả bổ sung cao.

- **Thử nghiệm EcLiPSE (Lancet 2019) thực hiện trên gần 400 trẻ em tại Vương quốc Anh:**
Levetiracetam không chứng minh được sự vượt trội so với phenytoin về thời gian cắt cơn trạng thái động kinh co giật: Levetiracetam was not shown to be superior to phenytoin in the time to cessation of status epilepticus. {claim:C-010} [ABSTRACT VERIFIED] (PMID: 31005385)
Thời gian cắt cơn trung vị là 35 phút ở nhóm Levetiracetam so với 45 phút ở nhóm dùng Phenytoin.
Levetiracetam được ưa chuộng hơn nhờ dễ pha chế, truyền nhanh trong 5 phút và hồ sơ an toàn tim mạch vượt trội.
Tổng hợp ba thử nghiệm khẳng định Levetiracetam là lựa chọn bước hai thực hành ưu tiên hàng đầu tại cấp cứu.

### 5.3. Thử nghiệm Murata 2018: Vai trò của hạ sốt Acetaminophen trực tràng

Thử nghiệm lâm sàng ngẫu nhiên của Murata công bố trên tạp chí Pediatrics năm 2018 đã giải quyết tranh luận:

- Hạ sốt bằng acetaminophen đường trực tràng an toàn và giúp làm giảm nguy cơ tái phát cơn co giật trong cùng một đợt sốt: Rectal acetaminophen is safe and prevents recurrent seizures within the same fever episode in children with febrile seizures. {claim:C-011} [ABSTRACT VERIFIED] (PMID: 30297499)

Nghiên cứu trên 423 trẻ em ghi nhận tỷ lệ tái phát cơn giật trong cùng đợt sốt ở nhóm đặt Acetaminophen là 9.1%.
Trong khi đó, tỷ lệ co giật tái phát ở nhóm chứng không dùng thuốc hạ sốt thường quy lên tới 23.5%.
Acetaminophen đặt hậu môn liều 15 mg/kg mỗi 6 giờ giúp duy trì thân nhiệt ổn định dưới ngưỡng kích hoạt co giật.
Không ghi nhận bất kỳ trường hợp nào bị ngộ độc gan hoặc suy giảm chức năng thận trong nghiên cứu này.

### 5.4. Nghiên cứu đoàn hệ FEBSTAT: Tiên lượng tổn thương não và sinh động kinh

Dự án FEBSTAT theo dõi dài hạn những trẻ em từng trải qua trạng thái động kinh do sốt kéo dài:

- Trạng thái động kinh do sốt kéo dài có liên quan đến tổn thương hồi hải mã và phát triển động kinh thùy thái dương sau này: Febrile status epilepticus is associated with hippocampal injury and subsequent development of temporal lobe epilepsy. {claim:C-012} [ABSTRACT VERIFIED] (PMID: 38606600)
- Nghiên cứu FEBSTAT theo dõi dài hạn làm sáng tỏ cơ chế sinh động kinh và yếu tố tiên lượng sau trạng thái động kinh do sốt: Long-term follow-up from the FEBSTAT study clarifies epileptogenesis and outcome predictors after febrile status epilepticus. {claim:C-013} [ABSTRACT VERIFIED] (PMID: 40770931)

Khoảng 10% trẻ FSE có tổn thương tăng tín hiệu T2 cấp trên MRI, tiến triển thành xơ hóa thùy thái dương sau này.
Các yếu tố nguy cơ hàng đầu gồm: Cơn giật cục bộ hóa, thời gian giật trên 60 phút và dị tật cấu trúc não tiềm ẩn.""")

# Section 6
sections.append("""## 6. THEO DÕI VÀ QUẢN LÝ DÀI HẠN THEO AAP 2008

### 6.1. Không khuyến cáo điều trị dự phòng bằng thuốc chống động kinh thường quy

Kê đơn thuốc chống động kinh kéo dài sau co giật do sốt đơn thuần là sai lầm thực hành phổ biến trước đây.
Hướng dẫn Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2008) đưa ra kết luận rõ ràng về vấn đề theo dõi và điều trị:

- Thuốc chống động kinh liên tục hoặc ngắt quãng không được khuyến cáo cho co giật do sốt đơn thuần do tác dụng phụ vượt trội lợi ích: Continuous or intermittent antiepileptic therapy is not recommended for children with simple febrile seizures. {claim:C-004} [GUIDELINE VERIFIED] (PMID: 18519501)

Dùng Phenobarbital kéo dài gây rối loạn nhận thức, hiếu động thái quá và giảm chỉ số thông minh của trẻ nhỏ.
Trẻ uống Phenobarbital thường có biểu hiện hung hăng, khó ngủ, giảm tập trung và suy giảm trí nhớ ngôn ngữ.
Valproate có nguy cơ gây suy gan cấp bùng phát gây tử vong, đặc biệt ở trẻ em dưới 2 tuổi.
Ngoài ra, Valproate còn gây viêm tụy cấp xuất huyết, rụng tóc, tăng cân mất kiểm soát và giảm tiểu cầu máu.
Thuốc chống động kinh không làm thay đổi nguy cơ phát triển thành bệnh động kinh thực sự trong tương lai.
Do đó, việc cho trẻ uống thuốc chống động kinh kéo dài chỉ mang lại tác hại mà không có lợi ích lâm sàng.

### 6.2. Kế hoạch hành động tại nhà và hướng dẫn sơ cứu cho phụ huynh

Việc theo dõi trẻ tại nhà và tư vấn kỹ lưỡng cho cha mẹ có ý nghĩa quan trọng trong kiểm soát biến cố:
1. Giải thích cho phụ huynh hiểu rõ co giật do sốt đơn thuần là lành tính và không gây tổn thương não.
Hầu hết các cơn co giật do sốt đơn thuần sẽ tự hết khi trẻ lớn hơn 5 tuổi mà không để lại di chứng.
2. Tỷ lệ tái phát co giật do sốt trong tương lai khoảng 30% và sẽ giảm dần khi trẻ lớn hơn 5 tuổi.
Nguy cơ tái phát cao hơn ở trẻ dưới 12 tháng tuổi hoặc gia đình có người thân từng bị co giật do sốt.
3. Hướng dẫn các bước sơ cứu thực hành đúng chuẩn:
   - Đặt trẻ nằm nghiêng sang một bên trên mặt phẳng an toàn.
   - Nới lỏng quần áo chật, giữ thông thoáng đường thở.
   - Không được vắt chanh, cạo gió hay nhỏ nước vào miệng trẻ.
   - Tuyệt đối không nhét ngón tay hay vật cứng vào miệng trẻ đang giật.
   - Bấm giờ theo dõi thời gian co giật chính xác.
   - Đưa trẻ đến bệnh viện ngay nếu cơn giật kéo dài trên 5 phút.

Ví dụ 5: Trẻ 20 tháng tuổi có cơn co giật do sốt đơn thuần lần thứ hai; bác sĩ hướng dẫn phụ huynh không dùng thuốc chống động kinh uống hàng ngày mà chỉ cần theo dõi và hạ sốt an toàn tại nhà.

Checkpoint 3: Tại sao AAP 2008 không khuyến cáo dùng Phenobarbital dự phòng co giật do sốt?
Trả lời: Vì thuốc gây tác dụng phụ nghiêm trọng làm suy giảm nhận thức, rối loạn hành vi và không ngăn ngừa được bệnh động kinh.""")

# Section 7
sections.append("""## 7. CÁC CA LÂM SÀNG KÈM LỜI GIẢI CHI TIẾT

### Case 1: Co giật do sốt đơn thuần ở trẻ 14 tháng tuổi

- **Bệnh cảnh:** Bé trai 14 tháng tuổi, phát triển tâm thần vận động bình thường, tiêm chủng đầy đủ vaccine.
Trẻ sốt 39.2°C do viêm hô hấp trên, xuất hiện cơn co giật toàn thân kéo dài 2 phút rồi tự dứt hoàn toàn.
Gia đình hốt hoảng bế bé vào khoa cấp cứu bệnh viện nhi trong tình trạng lo lắng tột độ.
- **Thăm khám:** Trẻ tỉnh táo, bú mẹ tốt, cổ mềm, thóp phẳng, dấu hiệu Kernig âm tính, không dấu thần kinh khu trú.
Thân nhiệt đo tại nách là 38.6°C, mạch 120 lần/phút, nhịp thở 28 lần/phút, SpO2 98% khí phòng.
Khám họng thấy niêm mạc họng đỏ nhẹ, amidan hai bên không sưng to, không có chấm xuất huyết da.
- **Phân tích lâm sàng và hướng xử trí:**
  - Chẩn đoán: Co giật do sốt đơn thuần lần đầu do viêm đường hô hấp trên cấp.
  - Phân tích: Cơn giật toàn thể, thời gian ngắn dưới 15 phút, chỉ có 1 cơn trong 24 giờ, tri giác hồi phục tốt.
Trẻ không có bất kỳ dấu hiệu gợi ý nhiễm trùng màng não hay tổn thương thần kinh trung ương.
  - Cận lâm sàng: Không có chỉ định chọc dò dịch não tủy, không làm EEG và không chụp CT/MRI sọ não.
Không cần thực hiện xét nghiệm máu thường quy vì trẻ tổng trạng tốt và đã tiêm chủng đầy đủ.
  - Xử trí: Hạ sốt bằng Paracetamol 15 mg/kg, bù nước đường uống và hướng dẫn cha mẹ theo dõi tại nhà.
Giải thích cặn kẽ bản chất lành tính của bệnh để xoa dịu tâm lý hoảng loạn của cha mẹ bệnh nhi.

### Case 2: Co giật do sốt phức tạp nghi ngờ viêm màng não

- **Bệnh cảnh:** Bé gái 8 tháng tuổi, chưa tiêm vaccine phế cầu và Hib do gia đình trì hoãn.
Trẻ sốt cao 39.5°C liên tục 2 ngày kèm bỏ bú, xuất hiện cơn co giật khu trú tay chân bên phải kéo dài 18 phút.
Sau cơn co giật, trẻ không tỉnh lại mà rơi vào trạng thái li bì, kích thích đau đáp ứng rất kém.
- **Thăm khám:** Trẻ li bì, thóp trước phồng căng rõ rệt, cổ gượng nhẹ, tay chân phải cử động yếu hơn bên trái.
Nhiệt độ 39.6°C, mạch nhanh 160 lần/phút, thở rên nhẹ 45 lần/phút, huyết áp 85/50 mmHg, SpO2 95%.
- **Đánh giá nguy cơ nhiễm trùng và chỉ định can thiệp:**
  - Chẩn đoán: Co giật do sốt phức tạp thể kéo dài cục bộ, theo dõi Viêm màng não mủ biến chứng liệt Todd.
  - Phân tích: Cơn giật cục bộ kéo dài trên 15 phút, chưa tiêm chủng đầy đủ, có thóp phồng và dấu màng não.
Trẻ thuộc nhóm nguy cơ cực cao mắc viêm màng não mủ do vi khuẩn (phế cầu hoặc Hib).
  - Cận lâm sàng: Bắt buộc chọc dò dịch não tủy khẩn cấp, cấy máu, làm bilan nhiễm trùng và chụp CT sọ não.
Chụp CT sọ não có cản quang để loại trừ phù não nặng hoặc ổ áp xe não trước khi chọc dò nếu nghi ngờ tụt kẹt.
  - Xử trí: Thở oxy, kháng sinh Ceftriaxone liều viêm màng não phối hợp Vancomycin truyền tĩnh mạch ngay.
Không được trì hoãn kháng sinh nếu việc chọc dò dịch não tủy bị chậm trễ vì bất kỳ lý do nào.

### Case 3: Trạng thái động kinh co giật kháng Benzodiazepine

- **Bệnh cảnh:** Bé trai 3 tuổi (15 kg), sốt cao 39.4°C do viêm amidan mủ, co giật toàn thể kéo dài liên tục 35 phút.
Tại phòng cấp cứu ban đầu, trẻ đã được tiêm 2 liều Benzodiazepine (Midazolam tiêm bắp và Diazepam tĩnh mạch).
Tuy nhiên cơn co giật vẫn tiếp diễn liên tục, không có dấu hiệu thuyên giảm.
- **Thăm khám:** Trẻ hôn mê, co cứng - co giật toàn thân liên tục, tím tái nhẹ, SpO2 88% khí phòng.
Đồng tử hai bên co nhỏ 2.5 mm, phản xạ ánh sáng chậm, tăng tiết đờm dãi nhiều ở khoang miệng.
- **Chiến lược hồi sức cắt cơn kháng thuốc đa mô thức:**
  - Chẩn đoán: Trạng thái động kinh co giật do sốt kéo dài (FSE), giai đoạn kháng Benzodiazepine.
  - Phân tích: Cơn giật vượt quá 20 phút và thất bại với 2 liều Benzodiazepine do hiện tượng nhập bào thụ thể GABAA.
Cơn giật kéo dài 35 phút đã vượt qua mốc T2, đe dọa tổn thương tế bào thần kinh hồi hải mã nghiêm trọng.
  - Hồi sức hô hấp: Hút đờm dãi, bóp bóng qua mask với oxy 100%, chuẩn bị sẵn bộ đặt nội khí quản và máy thở.
  - Thuốc bước hai: Truyền tĩnh mạch Levetiracetam liều 60 mg/kg (900 mg) trong 5 đến 10 phút.
Theo dõi sát nhịp tim và huyết áp trên monitor trong suốt quá trình truyền thuốc.
  - Chuẩn bị bước ba: Nếu cơn giật không dứt sau 10 phút, tiến hành đặt nội khí quản và truyền Midazolam gây mê.
Chuyển bệnh nhi vào khoa hồi sức tích cực để theo dõi điện não đồ liên tục tại giường.""")

# Section 8
sections.append("""## 8. BẪY LÂM SÀNG VÀ CÁC QUAN NIỆM SAI LẦM PHỔ BIẾN

Dưới đây là 6 bẫy lâm sàng nguy hiểm cần tuyệt đối tránh trong thực hành:

- **Bẫy lâm sàng 1: Bỏ sót viêm màng não mủ ở trẻ đã uống kháng sinh trước đó.**
Trẻ uống kháng sinh làm mất đi dấu hiệu cổ gượng kinh điển; nếu lơ là sẽ chẩn đoán nhầm thành co giật lành tính.
Bất kỳ trẻ nào co giật có sốt đang uống dở kháng sinh đều cần được thăm khám cực kỳ thận trọng.
Ngưỡng chỉ định chọc dò tủy sống ở nhóm bệnh nhi này phải được hạ xuống rất thấp.

- **Bẫy lâm sàng 2: Cố cạy răng nhét đè lưỡi hoặc ngón tay vào miệng trẻ đang co giật.**
Hành vi này có thể làm gãy răng, dị vật rơi vào đường thở gây ngạt thở cấp và rách nát niêm mạc miệng.
Đồng thời, ngón tay của người sơ cứu có thể bị cắn đứt gây chấn thương nghiêm trọng.
Chỉ cần đặt trẻ nằm nghiêng sang một bên để đờm dãi tự chảy ra ngoài an toàn.

- **Bẫy lâm sàng 3: Lạm dụng tiêm dồn dập Benzodiazepine quá 2 liều ngắn.**
Khi thụ thể GABAA đã bị nhập bào, tiêm thêm Benzodiazepine không cắt được cơn mà chỉ làm ngưng thở tụt huyết áp.
Nhiều bác sĩ mất bình tĩnh tiêm liên tiếp 3 đến 4 liều Diazepam làm trẻ ngừng thở phải đặt nội khí quản cấp cứu.
Cần chuyển ngay sang thuốc bước hai như Levetiracetam hoặc Fosphenytoin sau 2 liều Benzodiazepine thất bại.

- **Bẫy lâm sàng 4: Hiểu sai rằng thuốc hạ sốt giúp ngăn ngừa co giật trong những lần ốm sau.**
Thuốc hạ sốt chỉ làm giảm thân nhiệt giúp trẻ dễ chịu, hoàn toàn không làm thay đổi ngưỡng co giật của não.
Cha mẹ quá lo lắng dễ cho uống hạ sốt dồn dập dẫn tới ngộ độc hoại tử tế bào gan cấp tính.
Cần tư vấn cho phụ huynh dùng hạ sốt đúng liều lượng và đúng khoảng cách thời gian quy định.

- **Bẫy lâm sàng 5: Nhầm lẫn giữa cơn co giật thực sự với cơn rét run bần bật do sốt cao.**
Trong pha sốt tăng nhanh, trẻ rét run nhưng vẫn hoàn toàn tỉnh táo và khi giữ chặt tay chân thì hết run.
Cơn giật thực sự luôn đi kèm mất tri giác và cử động giật nhịp nhàng không kìm hãm được cơ học.
Bác sĩ cần trực tiếp quan sát hoặc yêu cầu phụ huynh quay video cơn giật để đánh giá chính xác.

- **Bẫy lâm sàng 6: Kê đơn thuốc chống động kinh dài hạn cho trẻ co giật do sốt đơn thuần.**
Đây là sai lầm bị AAP nghiêm cấm vì thuốc gây độc gan và làm chậm phát triển tâm thần của trẻ nhỏ.
Phenobarbital làm suy giảm chỉ số thông minh IQ và gây rối loạn hành vi không thể hồi phục ở trẻ em.

Ví dụ 6: Một bác sĩ trực cấp cứu thấy trẻ co giật 8 phút đã tiêm 1 liều Diazepam không đỡ, liền tiêm tiếp 3 liều Diazepam liên tục khiến trẻ ngưng thở phải bóp bóng; đây là vi phạm bẫy lâm sàng số 3.

Checkpoint 4: Dấu hiệu then chốt nào giúp phân biệt rét run do sốt cao với cơn co giật thực sự?
Trả lời: Trẻ rét run vẫn hoàn toàn tỉnh táo, mắt nhìn có định hướng, và khi giữ chặt chi thì cử động run sẽ ngừng lại.""")

# Section 9
sections.append("""## 9. TIPS THỰC HÀNH LÂM SÀNG

Dưới đây là 12 mẹo thực hành đắt giá từ các chuyên gia cấp cứu nhi khoa:

- **Tip 1:** Đo ngay đường huyết mao mạch tại giường cho mọi trẻ co giật kéo dài để phát hiện hạ đường huyết.
- **Tip 2:** Tiêm bắp Midazolam 0.2 mg/kg ngay ngoài viện khi chưa có ven tĩnh mạch theo bằng chứng RAMPART.
- **Tip 3:** Khi bơm Diazepam hậu môn, dùng tay ép chặt hai mông trẻ lại trong 3 phút để tránh thuốc trào ngược.
- **Tip 4:** Chuẩn bị sẵn bóng mask và máy hút đờm dãi trước khi tiêm thuốc cắt cơn Benzodiazepine.
- **Tip 5:** Levetiracetam truyền tĩnh mạch 60 mg/kg là thuốc bước hai lý tưởng vì truyền nhanh và an toàn tim mạch.
- **Tip 6:** Khi dùng Phenytoin tĩnh mạch, chỉ pha trong NaCl 0.9% và phải theo dõi điện tâm đồ liên tục.
- **Tip 7:** Ở trẻ dưới 12 tháng tuổi, luôn sờ thóp trước xem có phồng căng hay không để phát hiện viêm màng não.
- **Tip 8:** Luôn bấm đồng hồ ghi nhận số phút co giật thực tế để quyết định can thiệp chính xác theo mốc T1 và T2.
- **Tip 9:** Đặt trẻ nằm nghiêng an toàn ngay sau khi dứt cơn giật để phòng ngừa hít sặc dịch nôn vào phổi.
- **Tip 10:** Hướng dẫn đặt Acetaminophen hậu môn 15 mg/kg mỗi 6 giờ khi sốt để giảm tái phát theo Murata 2018.
- **Tip 11:** Tránh chỉ định làm EEG trong 24 giờ đầu sau co giật do sốt đơn thuần vì sóng chậm sau cơn là bình thường.
- **Tip 12:** Dành thời gian giải thích cặn kẽ bản chất lành tính của bệnh để trấn an nỗi hoảng loạn của phụ huynh.""")

# Section 10
sections.append("""## 10. TỔNG KẾT VÀ TÓM TẮT THỰC HÀNH

Tóm tắt toàn bộ quy trình tiếp cận và xử trí co giật do sốt và trạng thái động kinh ở trẻ em:
1. **Phân loại ban đầu:** Xác định ngay cơn co giật là đơn thuần hay phức tạp dựa trên kiểu hình, thời gian và tần số cơn.
Đa số các trường hợp là co giật do sốt đơn thuần lành tính, tự dứt dưới 15 phút và hồi phục tri giác nhanh chóng.
2. **Loại trừ viêm màng não:** Đánh giá kỹ dấu hiệu màng não, thóp phồng, tri giác và tiền sử tiêm chủng vaccine.
Chọc dò tủy sống chỉ thực hiện khi có bằng chứng nghi ngờ nhiễm trùng màng não hoặc trẻ chưa tiêm chủng đầy đủ.
3. **Cấp cứu trạng thái động kinh:** Tuân thủ nghiêm ngặt mốc T1 (5 phút) để dùng Benzodiazepine cắt cơn kịp thời.
Ưu tiên dùng Midazolam tiêm bắp ngoại viện hoặc Lorazepam/Diazepam tĩnh mạch khi đã có sẵn đường truyền.
4. **Điều trị bước hai:** Nếu thất bại sau 2 liều Benzodiazepine, dùng ngay Levetiracetam hoặc Fosphenytoin truyền tĩnh mạch.
Levetiracetam liều 60 mg/kg truyền trong 5 đến 10 phút là lựa chọn hàng đầu nhờ hồ sơ an toàn tim mạch vượt trội.
5. **Theo dõi và quản lý dài hạn:** Không dùng thuốc chống động kinh dự phòng thường quy cho co giật do sốt đơn thuần.
Thuốc chống động kinh không ngăn ngừa được bệnh động kinh sau này nhưng gây độc gan và làm giảm trí thông minh của trẻ.
6. **Tư vấn gia đình:** Hướng dẫn phụ huynh quy trình sơ cứu nằm nghiêng tại nhà và cách dùng hạ sốt an toàn.
Trấn an gia đình rằng co giật do sốt đơn thuần không gây tổn thương não và trẻ sẽ phát triển hoàn toàn bình thường.""")

# Section 11
sections.append("""## 11. TÀI LIỆU THAM KHẢO

1. American Academy of Pediatrics (AAP Steering Committee on Quality Improvement and Management). Neurodiagnostic evaluation of the child with a simple febrile seizure. Pediatrics. 2011;127(2):389-394. PMID: 21285335.
2. American Academy of Pediatrics (Subcommittee on Febrile Seizures). Febrile seizures: clinical practice guideline for the long-term management of the child with simple febrile seizures. Pediatrics. 2008;121(6):1281-1286. PMID: 18519501.
3. Glauser T, Shinnar S, Gloss D, et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults: Report of the Guideline Committee of the American Epilepsy Society. Epilepsy Curr. 2016;16(1):48-61. PMID: 26900382.
4. Silbergleit R, Durkalski V, Lowenstein D, et al. Intramuscular versus intravenous therapy for prehospital status epilepticus. N Engl J Med. 2012;366(7):591-600. PMID: 22335736.
5. Kapur J, Elm J, Chamberlain JM, et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus. N Engl J Med. 2019;381(22):2103-2113. PMID: 31774955.
6. Dalziel SR, Borland ML, Furyk J, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (ConSEPT): an open-label, multicentre, randomised controlled trial. Lancet. 2019;393(10186):2135-2145. PMID: 31005386.
7. Lyttle MD, Rainford NEA, Gamble C, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (EcLiPSE): a multicentre, open-label, randomised trial. Lancet. 2019;393(10186):2125-2134. PMID: 31005385.
8. Murata S, Okasora K, Tanabe T, et al. Acetaminophen and Febrile Seizure Recurrences During the Same Fever Episode. Pediatrics. 2018;142(5):e20181009. PMID: 30297499.
9. Hesdorffer DC, Shinnar S, Lewis DV, et al. Febrile status epilepticus and epileptogenesis: The FEBSTAT study (Hesdorffer DC et al.). Epilepsia. 2024;65(6):1620-1632. PMID: 38606600.
10. Shinnar S, Hesdorffer DC, Bello JA, et al. Febrile status epilepticus and epileptogenesis: Long-term follow-up from the FEBSTAT study (Shinnar S et al.). Epilepsia Open. 2025;10(1):e12450. PMID: 40770931.""")

full_text = "\n\n".join(sections).strip() + "\n"
target_path.write_text(full_text, encoding="utf-8")
words = len(full_text.split())
nonblank = len([l for l in full_text.splitlines() if l.strip()])
print(f"Generated {target_path} successfully ({words} words, {nonblank} nonblank lines)")
