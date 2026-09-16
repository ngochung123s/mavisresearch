# -*- coding: utf-8 -*-
"""Generate high-yield, comprehensive PED-07 markdown lesson with full governance compliance."""
from pathlib import Path

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md")

content = """# CO GIẬT DO SỐT & TRẠNG THÁI ĐỘNG KINH Ở TRẺ EM (PED-07)

## 0. TỔNG QUAN VÀ DỊCH TỄ HỌC

### 0.1. Nền tảng tối thiểu cần dùng ngay

- **Co giật do sốt là gì?** Co giật do sốt (Febrile Seizure - FS) là một biến cố co giật xuất hiện ở trẻ nhỏ trong độ tuổi từ 6 tháng đến 60 tháng (5 tuổi), đi kèm với sốt từ 38°C (100.4°F) trở lên qua đo nhiệt kế, nhưng không có bằng chứng của nhiễm trùng hệ thần kinh trung ương (viêm màng não, viêm não), không có rối loạn chuyển hóa toàn thân cấp tính và tiền căn không có cơn co giật không do sốt trước đó.
- **Tại sao lứa tuổi 6 đến 60 tháng lại dễ bị co giật do sốt nhất?** Đây là giai đoạn cửa sổ phát triển đặc biệt nhạy cảm của não bộ trẻ nhỏ, khi ngưỡng co giật của vỏ não còn thấp, quá trình myeline hóa các sợi thần kinh dẫn truyền chưa hoàn thiện, và sự cân bằng giữa chất dẫn truyền hưng phấn (Glutamate) với chất dẫn truyền ức chế (GABA) rất dễ bị phá vỡ khi thân nhiệt gia tăng đột ngột.
- **Trạng thái động kinh là gì?** Trạng thái động kinh (Status Epilepticus - SE) là tình trạng một cơn co giật kéo dài liên tục hoặc nhiều cơn co giật liên tiếp tái diễn mà tri giác của trẻ không hồi phục hoàn toàn giữa các cơn, đạt tới mốc thời gian T1 mà tại đó cơn giật không còn khả năng tự chấm dứt tự nhiên và cần can thiệp y tế khẩn cấp.
- **Mốc thời gian T1 và T2 là gì?** Theo định nghĩa sinh lý bệnh hiện đại của Liên đoàn Chống Động kinh Quốc tế (ILAE), mốc T1 là thời điểm cần bắt đầu dùng thuốc cắt cơn (đối với co giật co cứng - co giật toàn thể là 5 phút), và mốc T2 là thời điểm tổn thương tế bào thần kinh vĩnh viễn bắt đầu xảy ra nếu cơn co giật vẫn tiếp diễn (đối với co giật toàn thể là 30 phút).
- **Mục tiêu ưu tiên số một trong cấp cứu là gì?** Đảm bảo kiểm soát đường thở thông thoáng, cung cấp đủ oxy, duy trì huyết động ổn định và cắt cơn giật nhanh chóng bằng Benzodiazepine trước khi tổn thương nơ-ron do thiếu oxy và nhiễm toan chuyển hóa xuất hiện.
- **Chọc dò tủy sống có bắt buộc cho mọi trẻ co giật do sốt không?** Hoàn toàn không; chọc dò tủy sống chỉ được chỉ định khi trẻ có dấu hiệu màng não, thóp phồng, tri giác li bì kéo dài sau cơn, hoặc trẻ chưa được tiêm chủng phế cầu và Hib đầy đủ kết hợp với tình trạng lâm sàng nghi ngờ.
- **Thuốc hạ sốt có ngăn ngừa được cơn co giật tái phát trong tương lai không?** Thuốc hạ sốt (Paracetamol, Ibuprofen) có tác dụng hạ thân nhiệt giúp trẻ dễ chịu và giảm mất nước, nhưng không làm thay đổi ngưỡng kích thích co giật nội tại của vỏ não và không ngăn chặn được các đợt co giật do sốt trong những lần ốm sau này.
- **Trẻ co giật do sốt có biến thành bệnh động kinh không?** Nguy cơ phát triển thành bệnh động kinh thực sự sau co giật do sốt đơn thuần là rất thấp, chỉ khoảng 1% đến 2% (gần tương đương với quần thể trẻ em khỏe mạnh thông thường).
- **Phụ huynh cần làm gì đầu tiên khi trẻ co giật tại nhà?** Đặt trẻ nằm nghiêng sang một bên trên mặt phẳng an toàn, nới lỏng quần áo quanh cổ, bấm giờ theo dõi cơn co giật, tuyệt đối không nhét bất kỳ vật cứng nào vào miệng trẻ và gọi cấp cứu nếu cơn giật kéo dài trên 5 phút.
- **Thử nghiệm RAMPART chứng minh điều gì?** Midazolam tiêm bắp tác dụng nhanh, kiểm soát cơn co giật trước viện hiệu quả hơn lorazepam tĩnh mạch nhờ tiết kiệm thời gian thiết lập đường truyền tĩnh mạch trong cấp cứu ngoại viện.
- **Bộ ba thử nghiệm ESETT, ConSEPT, EcLiPSE đưa ra thông điệp gì?** Trong điều trị bước hai trạng thái động kinh co giật kháng Benzodiazepine ở trẻ em, Levetiracetam có hiệu quả tương đương Phenytoin/Fosphenytoin và Valproate nhưng có ưu điểm nổi bật là truyền nhanh trong 5 đến 10 phút và ít độc tính trên tim mạch hơn.

### 0.2. Dịch tễ học và định nghĩa chuẩn hóa theo ILAE / AAP

Co giật do sốt là rối loạn co giật phổ biến nhất ở lứa tuổi sơ sinh và trẻ nhỏ. Dữ liệu dịch tễ học toàn cầu ghi nhận tỷ lệ mắc co giật do sốt dao động từ 2% đến 5% ở trẻ em khu vực Bắc Mỹ và Tây Âu, và có thể lên tới 8% đến 10% ở một số quần thể châu Á như Nhật Bản và đảo Guam. Đỉnh điểm xuất hiện của co giật do sốt là vào khoảng 18 tháng tuổi, với tỷ lệ bé trai nhỉnh hơn bé gái một chút (tỷ lệ nam/nữ khoảng 1.2:1).

Yếu tố gia đình và di truyền đóng vai trò nổi bật trong cơ chế bệnh sinh của co giật do sốt. Tiền sử gia đình có người thân trực hệ thế hệ thứ nhất (cha, mẹ, anh chị em ruột) từng bị co giật do sốt làm tăng nguy cơ mắc ở trẻ lên gấp 2 đến 3 lần. Các nghiên cứu di truyền học phân tử đã xác định được nhiều locus gen liên quan (FEBS1 đến FEBS11) cũng như các đột biến trên gen mã hóa kênh natri phụ thuộc điện thế (SCN1A, SCN1B, SCN2A) và thụ thể GABAA (GABRG2). Đáng lưu ý, đột biến gen SCN1A có thể biểu hiện từ thể nhẹ như co giật do sốt có tính gia đình đến các bệnh cảnh não động kinh cực kỳ trầm trọng như Hội chứng Dravet.

Về mặt nguyên nhân gây sốt, hầu hết các đợt co giật do sốt xảy ra trong bối cảnh các bệnh nhiễm trùng đường hô hấp trên do virus thông thường (Human Herpesvirus 6 - HHV-6, virus cúm A, cúm B, Adenovirus, Parainfluenza, Enterovirus) hoặc các đợt nhiễm trùng đường tiêu hóa cấp (Rotavirus, Norovirus). Ngoài ra, sốt phản ứng sau một số mũi tiêm chủng vaccine (như sởi - quai bị - rubella [MMR] hoặc bạch hầu - ho gà - uốn ván [DTP]) cũng có thể kích hoạt cơn co giật ở những trẻ có sẵn cơ địa nhạy cảm, tuy nhiên lợi ích bảo vệ của vaccine vượt trội hoàn toàn so với nguy cơ co giật thoáng qua này.

---

## 1. ĐỊNH NGHĨA VÀ PHÂN LOẠI CO GIẬT DO SỐT

### 1.1. Co giật do sốt đơn thuần và phức tạp

Việc phân loại chính xác tính chất cơn co giật do sốt là bước thăm khám đầu tiên có tính chất quyết định, giúp bác sĩ phân tầng nguy cơ tổn thương thần kinh, chỉ định cận lâm sàng phù hợp và tiên lượng nguy cơ tái phát. Dựa trên các đặc điểm lâm sàng về thời gian cơn, kiểu hình co giật và số lần xuất hiện trong một đợt bệnh, Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP) và Liên đoàn Chống Động kinh Quốc tế (ILAE) chia co giật do sốt thành hai nhóm lớn: Co giật do sốt đơn thuần (Simple Febrile Seizure) và Co giật do sốt phức tạp (Complex Febrile Seizure).

| Tiêu chí đánh giá lâm sàng | Co giật do sốt đơn thuần (Simple FS) | Co giật do sốt phức tạp (Complex FS) |
| :--- | :--- | :--- |
| **Kiểu hình co giật (Seizure Type)** | Toàn thể hóa nguyên phát (Cơn co cứng - co giật đối xứng hai bên) | Cục bộ / Khu trú (Giật một chi, quay mắt quay đầu) hoặc cục bộ hóa thứ phát |
| **Thời gian cơn giật (Duration)** | Ngắn, kéo dài dưới 15 phút (Đa số thường tự dứt trong 1 đến 3 phút) | Kéo dài, từ 15 phút trở lên hoặc kéo dài thành trạng thái động kinh |
| **Tần số xuất hiện (Frequency)** | Duy nhất 1 cơn trong vòng 24 giờ (hoặc trong 1 đợt sốt của cùng một bệnh) | Tái phát từ 2 cơn trở lên trong vòng 24 giờ hoặc trong cùng một đợt bệnh |
| **Giai đoạn sau cơn (Post-ictal state)** | Hồi phục tri giác nhanh chóng, trẻ tỉnh táo hoàn toàn sau 10 đến 30 phút | Li bì kéo dài hoặc xuất hiện dấu thần kinh khu trú (Liệt Todd sau cơn) |
| **Tỷ lệ gặp trong thực tế** | Chiếm khoảng 70% đến 80% tổng số các trường hợp co giật do sốt | Chiếm khoảng 20% đến 30% tổng số các trường hợp co giật do sốt |
| **Nguy cơ tiến triển thành Động kinh** | Rất thấp (khoảng 1% đến 2%, tương đương dân số bình thường) | Cao hơn rõ rệt (khoảng 4% đến 10%, đặc biệt nếu có nhiều yếu tố phức tạp) |

### 1.2. Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE)

Trạng thái động kinh do sốt là một phân nhóm đặc biệt nghiêm trọng của co giật do sốt phức tạp. FSE được định nghĩa là một cơn co giật liên tục hoặc nhiều cơn co giật ngắt quãng không hồi phục tri giác kéo dài từ 30 phút trở lên đi kèm với sốt. FSE chiếm khoảng 5% tổng số các trường hợp co giật do sốt và chiếm tới 25% đến 30% tổng số các ca trạng thái động kinh ở trẻ nhỏ lứa tuổi nhũ nhi và mầm non.

Khác với co giật do sốt đơn thuần vốn là một biến cố lành tính và không để lại di chứng thần kinh, trạng thái động kinh do sốt kéo dài đặt hệ thần kinh non nớt của trẻ vào tình trạng thiếu máu cục bộ tương đối, tiêu thụ glucose và oxy não tăng vọt, giải phóng ồ ạt các chất dẫn truyền thần kinh kích thích gây ngộ độc tế bào (Excitotoxicity). Cơn giật kéo dài liên tục trên 30 phút có thể gây phù nề cấp tính hồi hải mã và xơ hóa cấu trúc thùy thái dương, làm gia tăng đáng kể nguy cơ phát triển thành động kinh kháng trị sau này.

---

## 2. CƠ CHẾ BỆNH SINH VÀ MẠNG LƯỚI TẾ BÀO THẦN KINH

### 2.1. Tính hưng phấn thần kinh phụ thuộc nhiệt độ và cytokine tiền viêm

Cơ chế bệnh sinh của co giật do sốt là sự tương tác đa yếu tố phức tạp giữa não bộ chưa trưởng thành, yếu tố di truyền nhạy cảm nhiệt độ, và phản ứng viêm toàn thân cấp tính. Khi thân nhiệt tăng cao nhanh chóng, các kênh ion màng tế bào thần kinh bị thay đổi động học đóng mở, dẫn đến tăng tính hưng phấn điện sinh lý toàn vỏ não.

Dưới đây là các chuỗi phản ứng sinh lý bệnh then chốt giải thích quá trình khởi phát và duy trì cơn co giật ở trẻ em:

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

Nghiên cứu đoàn hệ tiến cứu FEBSTAT (Consequences of Febrile Status Epilepticus) đã làm thay đổi sâu sắc hiểu biết y khoa về hậu quả của những cơn co giật do sốt kéo dài. Sử dụng hình ảnh cộng hưởng từ (MRI) sọ não độ phân giải cao thực hiện trong vòng vài ngày sau biến cố FSE, các nhà nghiên cứu phát hiện thấy khoảng 10% đến 12% trẻ xuất hiện tình trạng tăng tín hiệu T2 và phì đại phù nề cấp tính cấu trúc hồi hải mã, đặc biệt là ở vùng T2 hồi hải mã (CA1, CA3).

Theo dõi dọc dài hạn sau 5 đến 10 năm cho thấy vùng hồi hải mã từng bị phù nề cấp tính này dần dần teo nhỏ và hình thành tổn thương xơ hóa cấu trúc đồi hải mã (Mesial Temporal Sclerosis - MTS). Tổn thương này chính là cơ sở giải phẫu bệnh lý điển hình của bệnh động kinh thùy thái dương kháng thuốc ở người lớn, đòi hỏi phải can thiệp phẫu thuật cắt bỏ ổ động kinh. Do đó, việc chặn đứng cơn co giật trước khi nó vượt qua mốc thời gian 30 phút (mốc T2) là mục tiêu sống còn để bảo tồn cấu trúc vi thể của não bộ trẻ nhỏ.

---

## 3. CHẨN ĐOÁN VÀ TIẾP CẬN BAN ĐẦU THEO HƯỚNG DẪN AAP 2011

### 3.1. Chỉ định chọc dò tủy sống (Lumbar Puncture)

Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2011) đã ban hành hướng dẫn thực hành lâm sàng dựa trên bằng chứng về việc đánh giá chẩn đoán thần kinh ở trẻ co giật do sốt đơn thuần. Mối quan tâm hàng đầu của mọi thầy thuốc lâm sàng khi tiếp cận trẻ co giật có sốt là phải loại trừ triệt để viêm màng não mủ hoặc viêm não cấp tính. Tuy nhiên, việc chọc dò tủy sống đại trà cho mọi trường hợp co giật do sốt đơn thuần là không cần thiết, gây đau đớn cho trẻ và tốn kém nguồn lực y tế.

Dựa trên tổng hợp bằng chứng từ các nghiên cứu tiến cứu quy mô lớn, AAP 2011 đã đưa ra các khuyến cáo phân tầng chỉ định chọc dò tủy sống như sau:

- Chọc dò tủy sống không được khuyến cáo thường quy ở trẻ co giật do sốt đơn thuần tổng trạng tốt và đã tiêm chủng đầy đủ: A lumbar puncture is not routinely recommended in a well-appearing, fully immunized child who presents with a simple febrile seizure. {claim:C-001} [GUIDELINE VERIFIED] (PMID: 21285335)
- Chọc dò tủy sống là một lựa chọn cần cân nhắc khi trẻ chưa được tiêm chủng phế cầu hoặc Hib đầy đủ: A lumbar puncture is an option when a child is considered underimmunized or when immunization status cannot be determined. {claim:C-002} [GUIDELINE VERIFIED] (PMID: 21285335)

Ngoài ra, bác sĩ lâm sàng bắt buộc phải chỉ định chọc dò tủy sống ngay lập tức trong các tình huống sau:
1. Trẻ có bất kỳ triệu chứng hoặc dấu hiệu thực thể nào gợi ý nhiễm trùng màng não: Cổ gượng, dấu hiệu Kernig dương tính, dấu hiệu Brudzinski dương tính, thóp trước phồng hoặc căng cứng ở trẻ nhũ nhi.
2. Trẻ có biểu hiện nhiễm độc toàn thân (Toxic appearance), li bì, khó đánh thức, tương tác xã hội kém hoặc rối loạn tri giác kéo dài sau cơn giật vượt quá giai đoạn sau cơn thông thường.
3. Trẻ đang được điều trị kháng sinh trước đó: Kháng sinh đường uống hoặc tiêm có thể che lấp các triệu chứng lâm sàng kinh điển của viêm màng não (tình trạng viêm màng não mất đầu), khiến việc đánh giá lâm sàng trở nên không đáng tin cậy.

### 3.2. Vai trò của điện não đồ (EEG) và chẩn đoán hình ảnh thần kinh

Một sai lầm rất phổ biến trong thực hành lâm sàng là vội vã chỉ định làm điện não đồ (EEG) và chụp cắt lớp vi tính (CT) sọ não cho mọi trẻ sau cơn co giật do sốt đơn thuần. Hướng dẫn AAP 2011 đã khẳng định rất rõ ràng về vấn đề này:

- Điện não đồ và chẩn đoán hình ảnh thần kinh không được khuyến cáo thường quy sau cơn co giật do sốt đơn thuần: Electroencephalogram and neuroimaging should not be performed in the routine evaluation of a child with a simple febrile seizure. {claim:C-003} [GUIDELINE VERIFIED] (PMID: 21285335)

Lý do của khuyến cáo này bao gồm:
1. **Đối với điện não đồ (EEG):** Sóng chậm lan tỏa sau cơn giật do sốt là một hiện tượng sinh lý thoáng qua rất thường gặp và không có giá trị dự báo nguy cơ tái phát cơn co giật do sốt hay sự phát triển của bệnh động kinh sau này. Ngược lại, việc phát hiện các sóng nhọn thoáng qua có thể dẫn đến việc chẩn đoán quá mức và chỉ định dùng thuốc chống động kinh kéo dài không cần thiết.
2. **Đối với chẩn đoán hình ảnh (CT/MRI sọ não):** Ở trẻ co giật do sốt đơn thuần với vòng đầu bình thường và khám thần kinh bình thường, tỷ lệ phát hiện các bất thường cấu trúc nội sọ có ý nghĩa lâm sàng là gần như bằng không. Việc chụp CT sọ não còn làm cho não bộ non nớt của trẻ phải tiếp xúc với tia xạ ion hóa có hại, làm gia tăng nguy cơ ung thư trong tương lai. Chỉ định chụp MRI sọ não chỉ được đặt ra đối với co giật do sốt phức tạp có dấu hiệu thần kinh khu trú kéo dài hoặc trẻ có trạng thái động kinh do sốt kéo dài.

### 3.3. Các xét nghiệm cận lâm sàng khác

Việc thực hiện các xét nghiệm máu thường quy (công thức máu, điện giải đồ, đường huyết, canxi máu) không được khuyến cáo thường quy cho co giật do sốt đơn thuần trừ khi trẻ có tiền sử mất nước nặng do nôn mửa, tiêu chảy cấp, hoặc có biểu hiện nhiễm trùng nặng cần tìm ổ nhiễm trùng nguyên phát. Kiểm tra đường huyết mao mạch tại giường là bước duy nhất cần thực hiện nhanh chóng ở mọi trẻ có co giật kéo dài hoặc tri giác chậm hồi phục để loại trừ hạ đường huyết cấp tính.

---

## 4. XỬ TRÍ CẤP CỨU TRẠNG THÁI ĐỘNG KINH THEO AES 2016

### 4.1. Tiếp cận theo mốc thời gian T1 và T2

Hội Động kinh Hoa Kỳ (American Epilepsy Society - AES 2016) đã công bố hướng dẫn điều trị dựa trên bằng chứng cho trạng thái động kinh co giật ở trẻ em và người lớn. Phác đồ này nhấn mạnh vào tính cấp bách của thời gian và phân chia quá trình xử trí thành 4 giai đoạn can thiệp nối tiếp nhau một cách chặt chẽ.

```text
0 phút                        5 phút                       20 phút                      40 phút
  |                             |                            |                            |
  v                             v                            v                            v
[Ổn định ABCDE]  ------>  [Bước 1: Benzodiazepine] ------> [Bước 2: Chống động kinh IV] -> [Bước 3: Gây mê RSE]
(Đường thở, Oxy,          (Midazolam IM /            (Levetiracetam,              (Propofol,
 Glucose mao mạch)         Lorazepam IV /             Fosphenytoin, Valproate)     Midazolam truyền,
                           Diazepam IV/PR)                                         Ketamine)
```

### 4.2. Giai đoạn 1 (0 - 5 phút): Ổn định ban đầu

Ngay khi tiếp nhận trẻ đang có cơn co giật, mục tiêu tối thượng trong 5 phút đầu tiên là kiểm soát các chức năng sống cơ bản theo nguyên tắc ABCDE:
- **A (Airway):** Đặt trẻ nằm nghiêng an toàn để dẫn lưu đờm dãi, hút sạch chất tiết ở khoang miệng, ngửa đầu nâng cằm nhẹ nhàng nếu có tắc nghẽn đường thở trên. Tuyệt đối không cố nhét đè lưỡi hay vật cứng vào miệng trẻ đang co cứng hàm.
- **B (Breathing):** Cung cấp oxy lưu lượng cao qua mask có túi dự trữ (10 đến 15 lít/phút) để duy trì SpO2 từ 95% trở lên.
- **C (Circulation):** Đánh giá mạch, huyết áp, thời gian đổ đầy mao mạch (CRT); gắn monitor theo dõi dấu hiệu sinh tồn liên tục; nhanh chóng thiết lập đường truyền tĩnh mạch nếu có thể (nhưng không được làm trì hoãn việc dùng thuốc cắt cơn).
- **D (Disability):** Đo ngay đường huyết mao mạch tại giường. Nếu đường huyết dưới 2.6 mmol/L (dưới 45 mg/dL ở trẻ nhỏ), truyền ngay Glucose 10% với liều 2 đến 5 mL/kg tĩnh mạch chậm.
- **E (Exposure):** Đo thân nhiệt lõi, cởi bỏ bớt chăn gạc ủ ấm quá mức, áp dụng các biện pháp làm mát vật lý và chuẩn bị thuốc hạ sốt khi cần.

### 4.3. Giai đoạn 2 (5 - 20 phút): Điều trị bước 1 với Benzodiazepine

Nếu cơn co giật vẫn tiếp diễn quá 5 phút (đạt mốc T1), đây chính thức là trạng thái động kinh co giật và bắt buộc phải dùng thuốc cắt cơn ngay lập tức:

- Benzodiazepine là điều trị đầu tay được khuyến cáo cho trạng thái động kinh co giật ở trẻ em và người lớn: A benzodiazepine is recommended as the first-line treatment for convulsive status epilepticus in children and adults. {claim:C-005} [GUIDELINE VERIFIED] (PMID: 26900382)

Lựa chọn thuốc và liều lượng cụ thể theo hướng dẫn AES 2016:
1. **Nếu chưa có đường truyền tĩnh mạch (Môi trường trước viện hoặc cấp cứu ban đầu):**
   - **Midazolam tiêm bắp (IM):** Liều 0.2 mg/kg (tối đa 10 mg ở trẻ trên 40 kg, tối đa 5 mg ở trẻ 13 đến 40 kg). Đây là lựa chọn có mức độ khuyến cáo cao nhất (Class I, Level A) nhờ khả năng hấp thu cực nhanh qua cơ bắp.
   - **Midazolam xịt mũi (IN) hoặc ngậm dưới má (Buccal):** Liều 0.2 mg/kg nếu không thể tiêm bắp.
   - **Diazepam bơm hậu môn (Rectal gel):** Liều 0.2 đến 0.5 mg/kg (tùy theo lứa tuổi).
2. **Nếu đã có sẵn đường truyền tĩnh mạch:**
   - **Lorazepam tĩnh mạch (IV):** Liều 0.1 mg/kg (tối đa 4 mg/liều), tiêm tĩnh mạch chậm trong 2 phút.
   - **Diazepam tĩnh mạch (IV):** Liều 0.15 đến 0.2 mg/kg (tối đa 10 mg/liều), tiêm tĩnh mạch chậm trong 2 phút.

Nếu sau liều đầu tiên từ 5 đến 10 phút mà cơn giật vẫn chưa dứt hoàn toàn, có thể lặp lại thêm 1 liều Benzodiazepine tương tự một lần duy nhất. Tuyệt đối không dùng quá 2 liều Benzodiazepine ngắn vì nguy cơ ức chế hô hấp và hạ huyết áp tăng lên theo cấp số nhân trong khi hiệu quả cắt cơn giảm đi rõ rệt.

### 4.4. Giai đoạn 3 (20 - 40 phút): Điều trị bước 2 kháng Benzodiazepine

Khi cơn co giật kéo dài vượt quá 20 phút mặc dù đã dùng đủ 2 liều Benzodiazepine, trẻ bước vào giai đoạn trạng thái động kinh kháng Benzodiazepine. Lúc này, việc lặp lại Benzodiazepine sẽ thất bại do hiện tượng nhập bào thụ thể GABAA và tích tụ thụ thể NMDA hưng phấn. Bác sĩ phải chuyển ngay sang thuốc chống động kinh đường tĩnh mạch bước hai:

- Fosphenytoin, valproate hoặc levetiracetam đường tĩnh mạch là các lựa chọn điều trị bước hai cho trạng thái động kinh: Intravenous fosphenytoin, valproate, or levetiracetam are reasonable second-line treatment options for status epilepticus. {claim:C-006} [GUIDELINE VERIFIED] (PMID: 26900382)

| Thuốc chống động kinh bước 2 | Liều lượng khuyến cáo | Thời gian truyền tĩnh mạch | Chống chỉ định & Lưu ý an toàn |
| :--- | :--- | :--- | :--- |
| **Levetiracetam (Keppra)** | 60 mg/kg IV (Tối đa 4500 mg) | Truyền nhanh trong 5 đến 10 phút | An toàn tim mạch rất cao; chỉnh liều nếu suy thận nặng; ít tương tác thuốc |
| **Fosphenytoin (Cerebyx)** | 20 mg PE/kg IV (Tối đa 1500 mg PE) | Truyền trong 10 đến 15 phút (tối đa 150 mg PE/phút) | Tiền chất tan trong nước của Phenytoin; ít gây hoại tử mô; cần theo dõi ECG |
| **Sodium Valproate (Depakine)** | 40 mg/kg IV (Tối đa 3000 mg) | Truyền trong 5 đến 10 phút | Chống chỉ định tuyệt đối khi nghi ngờ bệnh ty thể hoặc rối loạn chu trình urê |
| **Phenytoin (Dilantin)** | 20 mg/kg IV (Tối đa 1000 mg) | Truyền chậm trong 20 đến 30 phút (tối đa 50 mg/phút) | Nguy cơ tụt huyết áp, loạn nhịp tim; nguy cơ hội chứng găng tay tím (Purple Glove) |

### 4.5. Giai đoạn 4 (40 - 60 phút): Trạng thái động kinh kháng trị (RSE)

Nếu cơn giật kéo dài trên 40 phút mà không đáp ứng với thuốc bước hai, bệnh nhân đã rơi vào Trạng thái động kinh kháng trị (Refractory Status Epilepticus - RSE). Lúc này, trẻ bắt buộc phải được đặt nội khí quản thở máy xâm nhập, hồi sức tích cực và bắt đầu truyền liên tục các thuốc gây mê toàn thân (Midazolam truyền liên tục, Propofol hoặc Thiopental/Pentobarbital) kết hợp với theo dõi điện não đồ liên tục tại giường (Continuous EEG) để hướng tới mục tiêu dập tắt hoàn toàn các đợt bùng nổ trên sóng điện não (Burst-Suppression).

---

## 5. BẰNG CHỨNG LÂM SÀNG TỪ CÁC THỬ NGHIỆM ĐỐI CHỨNG NGẪU NHIÊN (RCT)

### 5.1. Thử nghiệm RAMPART: Midazolam tiêm bắp vs Lorazepam tĩnh mạch

Thử nghiệm lâm sàng mù đôi đối chứng ngẫu nhiên RAMPART (Rapid Anticonvulsant Medication Prior to Arrival Trial) công bố trên tạp chí New England Journal of Medicine năm 2012 là một bước ngoặt lớn trong cấp cứu trạng thái động kinh ngoại viện:

- Midazolam tiêm bắp không thua kém và đạt kiểm soát cơn co giật trước viện nhanh hơn lorazepam tĩnh mạch: Intramuscular midazolam is noninferior to intravenous lorazepam for prehospital seizure termination. {claim:C-007} [ABSTRACT VERIFIED] (PMID: 22335736)

Trong thử nghiệm RAMPART thực hiện trên 893 bệnh nhân co giật ngoài bệnh viện, việc sử dụng bơm tiêm tự động Autoinjector tiêm bắp Midazolam đã giúp cắt cơn giật khi đến viện ở 73.4% bệnh nhân so với 63.4% ở nhóm dùng Lorazepam tĩnh mạch. Mặc dù sau khi vào được tĩnh mạch thì Lorazepam có tác dụng dứt cơn nhanh hơn một chút, nhưng tổng thời gian từ lúc nhân viên y tế tiếp cận bệnh nhân đến lúc cắt được cơn co giật ở nhóm Midazolam IM lại ngắn hơn đáng kể nhờ loại bỏ được thời gian trì hoãn do phải tìm ven thiết lập đường truyền tĩnh mạch ở bệnh nhân đang co giật dữ dội.

### 5.2. Bộ ba thử nghiệm bước hai: ESETT, ConSEPT và EcLiPSE

Trong nhiều thập kỷ, Phenytoin đường tĩnh mạch được xem là tiêu chuẩn vàng duy nhất cho điều trị bước hai trạng thái động kinh. Tuy nhiên, Phenytoin có nhiều nhược điểm lớn như tốc độ truyền chậm, nguy cơ tụt huyết áp nặng, rối loạn nhịp tim và hội chứng hoại tử găng tay tím khi chệch ven. Năm 2019, ba thử nghiệm lâm sàng đối chứng ngẫu nhiên đa trung tâm quy mô lớn được đồng loạt công bố đã thiết lập lại toàn bộ chứng cứ cho điều trị bước hai:

- **Thử nghiệm ESETT (Established Status Epilepticus Treatment Trial, NEJM 2019):**
So sánh mù đôi đối chứng trực tiếp giữa Levetiracetam (60 mg/kg), Fosphenytoin (20 mg PE/kg) và Valproate (40 mg/kg) ở cả người lớn và trẻ em trạng thái động kinh kháng Benzodiazepine:
Levetiracetam, fosphenytoin và valproate đạt tỷ lệ kiểm soát cơn và cải thiện tri giác tương đương nhau trong trạng thái động kinh kháng benzodiazepine: Levetiracetam, fosphenytoin, and valproate each led to seizure cessation and improved alertness in children and adults. {claim:C-008} [ABSTRACT VERIFIED] (PMID: 31774955)
Kết quả ghi nhận tỷ lệ thành công cắt cơn và hồi phục tri giác sau 60 phút ở ba nhóm là hoàn toàn tương đương nhau (khoảng 47% ở nhóm Levetiracetam, 45% ở nhóm Fosphenytoin và 46% ở nhóm Valproate), với hồ sơ an toàn và biến cố ức chế hô hấp không có sự khác biệt có ý nghĩa thống kê.

- **Thử nghiệm ConSEPT (Lancet 2019) thực hiện tại Úc và New Zealand:**
Đánh giá trên 233 trẻ em từ 3 tháng đến 16 tuổi bị trạng thái động kinh co giật:
Levetiracetam không vượt trội hơn phenytoin trong kiểm soát bước hai trạng thái động kinh co giật ở trẻ em: Levetiracetam is not superior to phenytoin for the second-line treatment of paediatric convulsive status epilepticus. {claim:C-009} [ABSTRACT VERIFIED] (PMID: 31005386)
Tỷ lệ cắt cơn lâm sàng sau 5 phút kết thúc truyền thuốc đạt 50% ở nhóm Levetiracetam và 60% ở nhóm Phenytoin. Đáng chú ý, khi gộp chung kết quả của những trẻ thất bại với thuốc đầu tiên và được dùng tiếp thuốc đối chứng thứ hai, tỷ lệ cắt cơn tích lũy tăng vọt lên khoảng 75%, cho thấy Levetiracetam và Phenytoin có tác dụng hiệp đồng bổ khuyết rất tốt.

- **Thử nghiệm EcLiPSE (Lancet 2019) thực hiện tại Vương quốc Anh:**
So sánh Levetiracetam (40 mg/kg) và Phenytoin (20 mg/kg) trên gần 400 trẻ em:
Levetiracetam không chứng minh được sự vượt trội so với phenytoin về thời gian cắt cơn trạng thái động kinh co giật: Levetiracetam was not shown to be superior to phenytoin in the time to cessation of status epilepticus. {claim:C-010} [ABSTRACT VERIFIED] (PMID: 31005385)
Thời gian trung vị để cắt cơn là 35 phút ở nhóm Levetiracetam và 45 phút ở nhóm Phenytoin. Mặc dù không chứng minh được sự vượt trội về mặt thống kê, các tác giả nhấn mạnh Levetiracetam dễ pha chế hơn, thời gian truyền nhanh hơn (5 phút so với ít nhất 20 phút của Phenytoin) và ít tác dụng phụ đe dọa tính mạng hơn, khiến nó trở thành lựa chọn thực hành ưu tiên hàng đầu tại hầu hết các khoa cấp cứu nhi khoa.

### 5.3. Thử nghiệm Murata 2018: Vai trò của hạ sốt Acetaminophen trực tràng

Một chủ đề gây nhiều tranh cãi trong nhiều năm là liệu việc dùng thuốc hạ sốt có làm giảm được nguy cơ co giật tái phát hay không. Thử nghiệm lâm sàng đối chứng ngẫu nhiên của Murata và cộng sự công bố trên tạp chí Pediatrics năm 2018 đã làm sáng tỏ câu hỏi này:

- Hạ sốt bằng acetaminophen đường trực tràng an toàn và giúp làm giảm nguy cơ tái phát cơn co giật trong cùng một đợt sốt: Rectal acetaminophen is safe and prevents recurrent seizures within the same fever episode in children with febrile seizures. {claim:C-011} [ABSTRACT VERIFIED] (PMID: 30297499)

Nghiên cứu được tiến hành trên 423 trẻ từ 6 đến 60 tháng tuổi nhập viện vì co giật do sốt. Nhóm can thiệp được đặt Acetaminophen hậu môn liều 15 mg/kg mỗi 6 giờ khi nhiệt độ từ 38.0°C trở lên, trong khi nhóm chứng không dùng hạ sốt thường quy. Kết quả cho thấy tỷ lệ tái phát co giật trong cùng đợt sốt ở nhóm dùng Acetaminophen thấp hơn rõ rệt (9.1%) so với nhóm chứng (23.5%), với sự khác biệt có ý nghĩa thống kê cao mà không ghi nhận bất kỳ tác dụng phụ nghiêm trọng nào trên chức năng gan thận.

### 5.4. Nghiên cứu đoàn hệ FEBSTAT: Tiên lượng tổn thương não và sinh động kinh

Dự án nghiên cứu đoàn hệ FEBSTAT (The Consequences of Febrile Status Epilepticus) là nghiên cứu tiến cứu quy mô lớn nhất thế giới theo dõi những trẻ trải qua trạng thái động kinh do sốt:

- Trạng thái động kinh do sốt kéo dài có liên quan đến tổn thương hồi hải mã và phát triển động kinh thùy thái dương sau này: Febrile status epilepticus is associated with hippocampal injury and subsequent development of temporal lobe epilepsy. {claim:C-012} [ABSTRACT VERIFIED] (PMID: 38606600)
- Nghiên cứu FEBSTAT theo dõi dài hạn làm sáng tỏ cơ chế sinh động kinh và yếu tố tiên lượng sau trạng thái động kinh do sốt: Long-term follow-up from the FEBSTAT study clarifies epileptogenesis and outcome predictors after febrile status epilepticus. {claim:C-013} [ABSTRACT VERIFIED] (PMID: 40770931)

Các công bố mới nhất từ FEBSTAT xác nhận rằng những trẻ có hình ảnh tăng tín hiệu T2 cấp tính hồi hải mã trên MRI não sau cơn FSE có nguy cơ cao phát triển xơ hóa đồi hải mã và xuất hiện các cơn động kinh không sốt sau giai đoạn ủ bệnh từ vài năm đến cả thập kỷ. Các yếu tố tiên lượng nguy cơ cao bao gồm: Cơn giật cục bộ hóa, thời gian giật kéo dài trên 60 phút, và có bất thường cấu trúc não tiềm ẩn trước đó.

---

## 6. QUẢN LÝ DÀI HẠN VÀ TƯ VẤN GIA ĐÌNH THEO AAP 2008

### 6.1. Không khuyến cáo điều trị dự phòng bằng thuốc chống động kinh thường quy

Một trong những can thiệp y tế thường bị lạm dụng trong quá khứ là kê đơn thuốc chống động kinh uống hàng ngày (như Phenobarbital, Valproate) cho trẻ sau cơn co giật do sốt đơn thuần để phòng ngừa tái phát. Hướng dẫn thực hành lâm sàng của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2008) đã đưa ra kết luận mang tính nguyên tắc:

- Thuốc chống động kinh liên tục hoặc ngắt quãng không được khuyến cáo cho co giật do sốt đơn thuần do tác dụng phụ vượt trội lợi ích: Continuous or intermittent antiepileptic therapy is not recommended for children with simple febrile seizures. {claim:C-004} [GUIDELINE VERIFIED] (PMID: 18519501)

Các bằng chứng khoa học chỉ ra rằng:
1. Mặc dù Phenobarbital hoặc Valproate dùng hàng ngày có thể làm giảm nhẹ tỷ lệ tái phát co giật do sốt, chúng hoàn toàn không làm giảm được nguy cơ phát triển thành bệnh động kinh thực sự trong tương lai.
2. Tác dụng phụ của các thuốc này là cực kỳ đáng lo ngại đối với sự phát triển tâm thần vận động của trẻ nhỏ: Phenobarbital gây rối loạn hành vi, kích động, giảm chú ý và suy giảm chỉ số IQ ngôn ngữ không hồi phục; trong khi Valproate có nguy cơ gây độc tế bào gan bùng phát gây tử vong ở trẻ dưới 2 tuổi và gây viêm tụy cấp, tăng cân, rụng tóc.
3. Việc sử dụng Diazepam đường uống ngắt quãng khi trẻ bắt đầu sốt cũng gây buồn ngủ li bì, mất điều hòa vận động và có thể làm che lấp các dấu hiệu tổn thương thần kinh trung ương nguy hiểm.

### 6.2. Kế hoạch hành động tại nhà và hướng dẫn sơ cứu cho phụ huynh

Chứng kiến con mình lên cơn co giật là một trải nghiệm kinh hoàng và gây ám ảnh nặng nề cho phụ huynh. Đa số các bậc cha mẹ đều tưởng rằng con mình sắp tử vong hoặc sẽ bị tổn thương não vĩnh viễn. Do đó, vai trò tư vấn, trấn an và hướng dẫn sơ cứu đúng cách của bác sĩ nhi khoa là vô cùng quan trọng.

Bác sĩ cần giải thích rõ cho gia đình:
1. Co giật do sốt đơn thuần là biến cố lành tính, không gây tử vong, không làm giảm trí thông minh và hầu hết trẻ sẽ tự hết co giật sau 5 tuổi.
2. Tỷ lệ tái phát cơn co giật do sốt trong tương lai là khoảng 30% đến 35% tổng số trẻ (tăng lên 50% nếu cơn đầu tiên xảy ra trước 12 tháng tuổi hoặc gia đình có tiền sử co giật do sốt).
3. Hướng dẫn quy trình sơ cứu co giật tại nhà:
   - Giữ bình tĩnh, không hoảng loạn la hét.
   - Đặt trẻ nằm nghiêng sang một bên trên bề mặt mềm phẳng để tránh hít sặc chất nôn vào đường thở.
   - Nới lỏng cổ áo và tháo khăn quàng hoặc cúc áo chật chội.
   - Tuyệt đối không vắt chanh, nhỏ nước xả, cạo gió hoặc nhét bất kỳ ngón tay hay vật cứng nào vào miệng trẻ.
   - Theo dõi đồng hồ bấm giờ xem cơn giật kéo dài bao nhiêu phút.
   - Nếu cơn co giật kéo dài quá 5 phút, lập tức gọi cấp cứu 115 hoặc đưa trẻ đến cơ sở y tế gần nhất. Đối với những trẻ có tiền sử co giật do sốt kéo dài hoặc FSE trước đó, bác sĩ có thể kê đơn sẵn Midazolam xịt mũi hoặc Diazepam bơm hậu môn để gia đình chủ động cắt cơn tại nhà khi cơn giật vượt quá 5 phút.

---

## 7. CÁC CA LÂM SÀNG KÈM LỜI GIẢI CHI TIẾT

### 7.1. Ca lâm sàng 1: Co giật do sốt đơn thuần ở trẻ 14 tháng tuổi

- **Bệnh sử:** Bé trai 14 tháng tuổi, tiền căn sản khoa và phát triển hoàn toàn bình thường, đã tiêm chủng đầy đủ vaccine theo lịch (bao gồm 3 mũi 6 trong 1 và 3 mũi Phế cầu Synflorix). Trẻ bắt đầu sốt nhẹ và chảy mũi nước từ sáng. Đến chiều cùng ngày, nhiệt độ đo ở nách là 39.2°C, trẻ bất ngờ lên cơn gồng cứng toàn thân, trợn mắt, hai tay và hai chân giật co thắt nhịp nhàng, kéo dài trong khoảng 2 phút rồi tự dứt. Phụ huynh hốt hoảng đưa bé vào khoa cấp cứu.
- **Thăm khám lúc vào viện:** Trẻ tỉnh táo, tiếp xúc tốt, đang bú mẹ, thân nhiệt 38.5°C, nhịp tim 125 lần/phút, thở êm 28 lần/phút, SpO2 98% khí phòng. Khám họng đỏ nhẹ, không có giả mạc. Thóp trước đã đóng phẳng. Cổ mềm, không gượng, dấu Kernig âm tính, dấu Brudzinski âm tính. Khám thần kinh định vị hoàn toàn bình thường, hai tay chân cử động đối xứng tốt.
- **Biện luận và xử trí chi tiết cho Ca lâm sàng 1:**
  - *Chẩn đoán xác định:* Co giật do sốt đơn thuần lần đầu, nghi ngờ do viêm đường hô hấp trên do siêu vi.
  - *Lý do:* Trẻ trong độ tuổi điển hình (14 tháng), cơn giật toàn thể hóa nguyên phát, thời gian ngắn dưới 15 phút (2 phút), chỉ có 1 cơn duy nhất trong 24 giờ, tri giác hồi phục hoàn toàn sau cơn, không có dấu hiệu thần kinh khu trú.
  - *Chỉ định cận lâm sàng:* Theo khuyến cáo AAP 2011, trẻ tổng trạng tốt, đã tiêm chủng phế cầu đầy đủ, khám không có dấu hiệu màng não, do đó **không có chỉ định** chọc dò tủy sống, không có chỉ định làm EEG, không có chỉ định chụp CT/MRI sọ não và không cần làm xét nghiệm máu thường quy.
  - *Điều trị:* Cho trẻ uống Paracetamol hạ sốt liều 15 mg/kg, bù dịch bằng đường uống Oresol, hướng dẫn người nhà theo dõi tri giác và dấu hiệu hô hấp trong 4 đến 6 giờ tại phòng lưu cấp cứu trước khi cho xuất viện về nhà theo dõi ngoại trú.

### 7.2. Ca lâm sàng 2: Co giật do sốt phức tạp nghi ngờ viêm màng não

- **Bệnh sử:** Bé gái 8 tháng tuổi, chưa tiêm vaccine phế cầu và mới chỉ tiêm 1 mũi vaccine 5 trong 1 lúc 2 tháng tuổi do gia đình trì hoãn. Trẻ sốt cao 39.5°C liên tục 2 ngày kèm bỏ bú và nôn trớ 4 lần. Sáng nay, mẹ phát hiện bé bị giật giật nửa người bên phải (tay phải và chân phải co giật, mắt liếc sang phải), cơn giật kéo dài khoảng 18 phút. Sau cơn giật, bé li bì, không nhận biết được cha mẹ.
- **Thăm khám lúc vào viện:** Trẻ li bì, kích thích đau đáp ứng chậm, khóc yếu ớt. Thân nhiệt 39.8°C, mạch 160 lần/phút, thở rên nhẹ 45 lần/phút, SpO2 95% khí phòng. Thóp trước kích thước 2.5x2.5 cm, sờ thấy phồng căng rõ rệt. Cổ gượng nhẹ. Khám vận động ghi nhận tay phải và chân phải cử động yếu hơn bên trái rõ rệt (nghi ngờ liệt Todd sau cơn).
- **Biện luận và xử trí chi tiết cho Ca lâm sàng 2:**
  - *Chẩn đoán xác định:* Co giật do sốt phức tạp thể kéo dài kèm cục bộ hóa, theo dõi Viêm màng não mủ cấp tính biến chứng liệt Todd nửa người.
  - *Lý do:* Cơn co giật khu trú nửa người, thời gian kéo dài trên 15 phút (18 phút), trẻ chưa được tiêm chủng phế cầu và Hib đầy đủ, khám lâm sàng có dấu hiệu thóp phồng, cổ gượng và hội chứng nhiễm trùng nhiễm độc toàn thân.
  - *Chỉ định cận lâm sàng:* Bắt buộc thực hiện chọc dò tủy sống ngay lập tức để làm xét nghiệm dịch não tủy (tế bào, protein, glucose dịch não tủy/máu, soi nhuộm Gram và cấy dịch não tủy). Thực hiện công thức máu, cấy máu, CRP, Procalcitonin, điện giải đồ và khí máu động mạch. Chỉ định chụp CT sọ não có tiêm thuốc cản quang để loại trừ phù não nặng hoặc ổ áp xe nội sọ.
  - *Điều trị:* Thở oxy qua gọng mũi, thiết lập đường truyền tĩnh mạch, dùng Ceftriaxone liều viêm màng não (100 mg/kg/ngày chia 1 hoặc 2 lần) phối hợp với Vancomycin (60 mg/kg/ngày chia 4 lần) ngay sau khi cấy máu và chọc dịch não tủy (hoặc dùng ngay nếu việc chọc dò bị trì hoãn). Theo dõi sát tri giác và chuẩn bị sẵn thuốc chống động kinh bước hai nếu tái phát cơn giật.

### 7.3. Ca lâm sàng 3: Trạng thái động kinh co giật kháng Benzodiazepine

- **Bệnh sử:** Bé trai 3 tuổi (cân nặng 15 kg), có tiền sử co giật do sốt đơn thuần lúc 18 tháng tuổi. Trẻ đang bị viêm amidan mủ cấp sốt 39.4°C. Trẻ bắt đầu lên cơn co giật toàn thể lúc 14h00 tại nhà. Gia đình gọi xe cấp cứu 115 đưa trẻ đến bệnh viện lúc 14h15 (cơn giật đã kéo dài 15 phút liên tục). Tại phòng cấp cứu, trẻ đã được tiêm bắp Midazolam liều 3 mg (0.2 mg/kg) lúc 14h18, nhưng đến 14h25 cơn giật vẫn tiếp diễn liên tục không dứt. Bác sĩ cấp cứu tiếp tục cho tiêm tĩnh mạch liều thứ hai Diazepam 3 mg (0.2 mg/kg) lúc 14h26. Đến 14h35 (tổng thời gian giật là 35 phút), trẻ vẫn đang co cứng - co giật nhịp nhàng toàn thân, tím tái môi, thở khò khè ứ đọng đờm dãi.
- **Thăm khám lúc 14h35:** Hôn mê, đồng tử hai bên 3 mm co hồi ánh sáng kém, co giật toàn thân nhịp nhàng liên tục. SpO2 tụt xuống 88% dù đang thở oxy qua mask. Đường huyết mao mạch tại giường là 5.8 mmol/L. Thân nhiệt 39.0°C.
- **Biện luận và xử trí chi tiết cho Ca lâm sàng 3:**
  - *Chẩn đoán xác định:* Trạng thái động kinh co giật do sốt kéo dài (Febrile Status Epilepticus), giai đoạn kháng Benzodiazepine (thời gian co giật 35 phút, đã thất bại với 2 liều Benzodiazepine).
  - *Chiến lược xử trí cấp cứu khẩn cấp:*
    1. **Kiểm soát đường thở và hô hấp:** Hút đàm nhớt sâu họng miệng, bóp bóng qua mask với oxy 100%, chuẩn bị sẵn bộ đặt nội khí quản và máy thở.
    2. **Chuyển ngay sang thuốc điều trị bước hai:** Dựa trên chứng cứ từ các thử nghiệm ESETT, ConSEPT và EcLiPSE, lựa chọn tối ưu hàng đầu là **Levetiracetam (Keppra)** đường tĩnh mạch:
       - *Liều dùng:* 60 mg/kg × 15 kg = 900 mg Levetiracetam pha trong 50 mL dung dịch NaCl 0.9%, truyền tĩnh mạch nhanh trong vòng 5 đến 10 phút.
       - *Lựa chọn thay thế:* Nếu không có sẵn Levetiracetam, có thể dùng Fosphenytoin liều 20 mg PE/kg (300 mg PE) truyền tĩnh mạch trong 10 phút dưới monitor theo dõi điện tim liên tục, hoặc Sodium Valproate liều 40 mg/kg (600 mg) truyền trong 10 phút.
    3. **Chuẩn bị bước ba (Gây mê hồi sức):** Nếu sau khi kết thúc truyền Levetiracetam 10 phút mà cơn giật vẫn không ngừng (tổng thời gian giật vượt quá 45 - 50 phút), lập tức tiến hành đặt nội khí quản, thở máy bảo vệ phổi và khởi động truyền liên tục Midazolam tĩnh mạch (liều nạp 0.2 mg/kg, sau đó duy trì 0.05 đến 2 mg/kg/giờ) để kiểm soát trạng thái động kinh kháng trị (RSE).

---

## 8. BẪY LÂM SÀNG VÀ CÁC QUAN NIỆM SAI LẦM PHỔ BIẾN

Trong quá trình tiếp cận và xử trí trẻ co giật có sốt, bác sĩ lâm sàng rất dễ mắc phải những sai lầm kinh điển dưới đây:

- **Bẫy lâm sàng 1: Nhầm lẫn giữa co giật do sốt với viêm màng não mủ ở trẻ đã dùng kháng sinh trước đó.**
Nhiều trẻ bị viêm màng não mủ nhưng được phòng khám tư kê kháng sinh uống vài ngày trước đó làm các triệu chứng màng não (cổ gượng, Kernig) bị che mờ hoặc mất đi hoàn toàn. Khi trẻ lên cơn co giật, bác sĩ dễ chủ quan chẩn đoán là co giật do sốt đơn thuần. Bất kỳ trẻ nào có co giật kèm sốt mà đang uống kháng sinh dở dang đều phải được đánh giá vô cùng cẩn trọng và có ngưỡng chỉ định chọc dò tủy sống rất thấp.

- **Bẫy lâm sàng 2: Nhồi nhét vật cứng, ngón tay hoặc đè lưỡi vào miệng trẻ đang co giật.**
Đây là hành vi tai hại phổ biến nhất của cả người nhà và một số nhân viên y tế thiếu kinh nghiệm do lo sợ trẻ cắn vào lưỡi. Việc cố cạy răng nhét vật cứng vào miệng trẻ đang co cứng hàm có thể làm gãy răng, bật dị vật rơi vào đường thở gây tắc thở đột ngột, rách nát niêm mạc khoang miệng và kích thích nôn gây hít sặc dịch vị vào phổi. Trẻ có thể cắn nhẹ vào đầu lưỡi nhưng vết thương này hầu hết tự lành nhanh chóng, trong khi biến chứng do nhét vật cứng vào miệng có thể gây tử vong.

- **Bẫy lâm sàng 3: Lạm dụng Benzodiazepine quá 2 liều trong trạng thái động kinh.**
Khi thấy cơn giật chưa dứt sau 2 liều Midazolam hoặc Diazepam, nhiều bác sĩ lo lắng tiếp tục tiêm thêm liều thứ 3, thứ 4. Điều này hoàn toàn sai lầm về mặt dược lý học vì lúc này thụ thể GABAA đã bị nhập bào và mất nhạy cảm. Việc tiêm dồn dập Benzodiazepine không giúp cắt được cơn giật mà chỉ làm tụt huyết áp nặng và ngừng thở đột ngột. Bắt buộc phải chuyển ngay sang thuốc bước hai (Levetiracetam, Fosphenytoin, Valproate) sau 2 liều Benzodiazepine thất bại.

- **Bẫy lâm sàng 4: Cho rằng thuốc hạ sốt giúp ngăn ngừa co giật tái phát trong những lần ốm sau.**
Nhiều bác sĩ tư vấn cho phụ huynh rằng phải tích cực uống hạ sốt thật sớm ngay khi trẻ vừa ấm đầu để con không bị giật. Lời khuyên này vô tình tạo ra tâm lý hoảng loạn tột độ cho cha mẹ, dẫn đến việc dùng thuốc hạ sốt quá liều (uống Paracetamol cách mỗi 2 giờ hoặc phối hợp bừa bãi Ibuprofen) gây ngộ độc hoại tử tế bào gan cấp tính. Cần giải thích rõ hạ sốt chỉ giúp trẻ dễ chịu, không thay đổi được ngưỡng co giật nội tại của não bộ.

- **Bẫy lâm sàng 5: Bỏ sót run giật do lạnh (Rigor / Chills) ở trẻ sốt cao giai đoạn co mạch.**
Khi nhiệt độ cơ thể đang tăng nhanh trong pha co mạch, trẻ thường rét run bần bật, run rẩy các chi và run môi. Nhiều phụ huynh và điều dưỡng trẻ nhầm hiện tượng rét run này với cơn co giật. Điểm phân biệt then chốt: Trẻ rét run hoàn toàn tỉnh táo, mắt nhìn có định hướng, tiếp xúc tốt, và khi nắm chặt tay chân của trẻ thì động tác run sẽ ngừng lại hoặc giảm đi rõ rệt. Cơn co giật thực sự luôn đi kèm với mất ý thức, mắt trợn ngược hoặc đứng tròng, và động tác giật không thể kìm hãm lại bằng cách giữ cơ học.

- **Bẫy lâm sàng 6: Kê đơn thuốc chống động kinh dài hạn sau cơn co giật do sốt đơn thuần.**
Kê đơn Valproate hoặc Phenobarbital uống hàng ngày trong 6 tháng đến 1 năm cho trẻ co giật do sốt đơn thuần là một sai lầm thực hành nghiêm trọng bị AAP 2008 nghiêm cấm. Thuốc không ngăn ngừa được bệnh động kinh sau này nhưng lại làm chậm phát triển trí tuệ, rối loạn hành vi và tiềm ẩn độc tính gan mật nguy hiểm cho trẻ.

---

## 9. TIPS THỰC HÀNH LÂM SÀNG

Dưới đây là 12 mẹo thực hành lâm sàng đắt giá được đúc kết từ các chuyên gia hồi sức và thần kinh nhi khoa:

- **Tip 1:** Luôn luôn đo đường huyết mao mạch tại giường cho mọi trẻ co giật kéo dài hoặc chậm tỉnh sau co giật; hạ đường huyết là nguyên nhân có thể đảo ngược nhanh nhất chỉ bằng vài mL Glucose 10%.
- **Tip 2:** Không bao giờ cố tìm ven đặt đường truyền tĩnh mạch ở trẻ đang co giật dữ dội ngoài bệnh viện; hãy tiêm bắp ngay Midazolam 0.2 mg/kg vào mặt trước ngoài đùi để dứt cơn nhanh nhất theo bằng chứng RAMPART.
- **Tip 3:** Khi dùng Diazepam bơm hậu môn cho trẻ nhỏ, dùng ngón tay ép chặt hai mông của trẻ lại với nhau trong ít nhất 3 đến 5 phút sau khi bơm thuốc để ngăn dịch thuốc bị tống xuất ngược ra ngoài.
- **Tip 4:** Hãy chuẩn bị sẵn ống hút đờm dãi và bóng mask trước khi tiêm Benzodiazepine vì thuốc có thể làm giãn cơ hầu họng và ức chế trung tâm hô hấp ở hành não.
- **Tip 5:** Levetiracetam đường tĩnh mạch liều 60 mg/kg có thể truyền nhanh trong 5 phút mà không sợ tụt huyết áp hay ngừng tim như Phenytoin; đây là thuốc bước hai lý tưởng tại khoa cấp cứu.
- **Tip 6:** Nếu chọn dùng Phenytoin truyền tĩnh mạch, bắt buộc phải pha trong dung dịch NaCl 0.9% (tuyệt đối không pha trong Glucose vì thuốc sẽ kết tủa ngay lập tức) và phải theo dõi điện tâm đồ liên tục.
- **Tip 7:** Ở trẻ dưới 12 tháng tuổi bị co giật có sốt, triệu chứng màng não thường rất nghèo nàn; hãy đặc biệt chú ý dấu hiệu thóp phồng, mắt lờ đờ và tiếng khóc thét the thé rên rỉ.
- **Tip 8:** Luôn ghi nhận chính xác thời điểm cơn co giật bắt đầu (bấm đồng hồ); quyết định can thiệp từng bước trong trạng thái động kinh phải dựa trên số phút thực tế chứ không dựa trên cảm giác chủ quan.
- **Tip 9:** Sau khi trẻ cắt cơn giật, hãy đặt trẻ ở tư thế nằm nghiêng an toàn (Recovery position) để dịch tiết khoang miệng tự chảy ra ngoài, tránh nguy cơ hít sặc vào phổi trong giai đoạn ngủ sau cơn.
- **Tip 10:** Đối với trẻ có tiền sử co giật do sốt kéo dài, hãy hướng dẫn phụ huynh phương pháp hạ sốt bằng Acetaminophen đặt hậu môn 15 mg/kg mỗi 6 giờ khi sốt từ 38°C trở lên để giảm nguy cơ tái phát theo Murata 2018.
- **Tip 11:** Không vội vã chỉ định làm EEG ngay trong ngày đầu tiên sau cơn co giật do sốt đơn thuần vì sóng chậm sau cơn là bình thường và dễ gây hiểu lầm dẫn đến chẩn đoán sai lệch.
- **Tip 12:** Dành ít nhất 10 phút để trò chuyện, giải thích cặn kẽ và xoa dịu nỗi sợ hãi của cha mẹ; sự thấu hiểu của gia đình chính là liều thuốc an thần tốt nhất cho bệnh nhi.

---

## 10. TÀI LIỆU THAM KHẢO

1. American Academy of Pediatrics. Neurodiagnostic evaluation of the child with a simple febrile seizure. Pediatrics. 2011;127(2):389-394. PMID: 21285335.
2. American Academy of Pediatrics. Febrile seizures: clinical practice guideline for the long-term management of the child with simple febrile seizures. Pediatrics. 2008;121(6):1281-1286. PMID: 18519501.
3. Glauser T, Shinnar S, Gloss D, et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults: Report of the Guideline Committee of the American Epilepsy Society. Epilepsy Curr. 2016;16(1):48-61. PMID: 26900382.
4. Silbergleit R, Durkalski V, Lowenstein D, et al. Intramuscular versus intravenous therapy for prehospital status epilepticus. N Engl J Med. 2012;366(7):591-600. PMID: 22335736.
5. Kapur J, Elm J, Chamberlain JM, et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus. N Engl J Med. 2019;381(22):2103-2113. PMID: 31774955.
6. Dalziel SR, Borland ML, Furyk J, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (ConSEPT): an open-label, multicentre, randomised controlled trial. Lancet. 2019;393(10186):2135-2145. PMID: 31005386.
7. Lyttle MD, Rainford NEA, Gamble C, et al. Levetiracetam versus phenytoin for second-line treatment of paediatric convulsive status epilepticus (EcLiPSE): a multicentre, open-label, randomised trial. Lancet. 2019;393(10186):2125-2134. PMID: 31005385.
8. Murata S, Okasora K, Tanabe T, et al. Acetaminophen and Febrile Seizure Recurrences During the Same Fever Episode. Pediatrics. 2018;142(5):e20181009. PMID: 30297499.
9. Hesdorffer DC, Shinnar S, Lewis DV, et al. Febrile status epilepticus and epileptogenesis: The FEBSTAT study. Epilepsia. 2024;65(6):1620-1632. PMID: 38606600.
10. Shinnar S, Hesdorffer DC, Bello JA, et al. Febrile status epilepticus and epileptogenesis: The FEBSTAT study. Epilepsia Open. 2025;10(1):e12450. PMID: 40770931.
"""

target_path.write_text(content.strip() + "\n", encoding="utf-8")
print(f"Generated {target_path} successfully ({len(content.split())} words, {len([l for l in content.splitlines() if l.strip()])} nonblank lines)")
