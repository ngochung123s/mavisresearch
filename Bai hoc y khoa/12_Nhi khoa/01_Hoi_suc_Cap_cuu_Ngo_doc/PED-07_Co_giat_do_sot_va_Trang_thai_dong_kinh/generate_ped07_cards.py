# -*- coding: utf-8 -*-
"""Generate high-yield Anki flashcards for PED-07 conforming to medical-flashcard-governance."""
import json
from pathlib import Path

target_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh")
cards_file = target_dir / "PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.cards.v2.json"

cards = [
    {
        "type": "cloze",
        "text": "Co giật do sốt (Febrile Seizures) được định nghĩa là cơn co giật xảy ra ở trẻ từ {{c1::6 đến 60 tháng tuổi}} (hoặc 3 tháng đến 5 tuổi) có thân nhiệt từ {{c1::38°C}} trở lên, không có nhiễm trùng hệ thần kinh trung ương và không có rối loạn chuyển hóa toàn thân cấp tính.",
        "extra": "Cơ chế: Não bộ trẻ nhũ nhi và trẻ nhỏ đang trong giai đoạn phát triển nhanh, ngưỡng co giật thấp và dễ bị kích thích khi thân nhiệt tăng đột ngột."
    },
    {
        "type": "cloze",
        "text": "Tỷ lệ mắc co giật do sốt ở trẻ em nói chung dao động trong khoảng {{c1::2% đến 5%}}, với lứa tuổi có tỷ lệ mắc cao nhất (đỉnh mắc bệnh) là từ {{c1::12 đến 18 tháng tuổi}}.",
        "extra": "Cơ chế: Đây là dạng rối loạn co giật phổ biến nhất ở lứa tuổi nhi khoa, đa số có tính chất lành tính và tiên lượng lâu dài rất tốt."
    },
    {
        "type": "cloze",
        "text": "Co giật do sốt đơn thuần (Simple Febrile Seizures) có ba đặc điểm kinh điển: cơn co giật mang tính chất {{c1::toàn thể}}, thời gian kéo dài {{c1::< 15 phút}}, và chỉ xuất hiện {{c1::1 cơn duy nhất}} trong vòng 24 giờ (hoặc trong 1 đợt sốt).",
        "extra": "Cơ chế: Trẻ tỉnh táo hoàn toàn sau cơn giật (giai đoạn sau cơn ngắn), không để lại bất kỳ dấu thần kinh khu trú nào."
    },
    {
        "type": "cloze",
        "text": "Co giật do sốt phức hợp (Complex Febrile Seizures) được chẩn đoán khi có ít nhất một trong ba tiêu chuẩn: cơn co giật mang tính chất {{c1::cục bộ}}, thời gian kéo dài {{c1::≥ 15 phút}}, hoặc tái phát {{c1::≥ 2 cơn}} trong vòng 24 giờ.",
        "extra": "Cơ chế: Cần đặc biệt cảnh giác với tổn thương thực thể thần kinh tiềm ẩn hoặc nhiễm trùng hệ thần kinh trung ương ở nhóm này."
    },
    {
        "type": "cloze",
        "text": "Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE) được định nghĩa khi cơn co giật do sốt kéo dài liên tục từ {{c1::≥ 30 phút}} hoặc xuất hiện chuỗi các cơn co giật mà trẻ {{c1::không hồi phục hoàn toàn tri giác}} giữa các cơn.",
        "extra": "Cơ chế: FSE chiếm khoảng 5% tổng số các ca co giật do sốt và là một cấp cứu thần kinh nhi khoa khẩn cấp."
    },
    {
        "type": "cloze",
        "text": "Nghiên cứu theo dõi đoàn hệ FEBSTAT chỉ ra rằng trẻ bị trạng thái động kinh do sốt kéo dài có nguy cơ xuất hiện tổn thương tăng tín hiệu T2 cấp tính ở {{c1::hồi hải mã (Hippocampus)}} trên phim chụp MRI sọ não, dẫn tới nguy cơ tiến triển thành {{c1::xơ hóa hồi hải mã (Hippocampal Sclerosis)}} sau này.",
        "extra": "Cơ chế: Phóng điện liên tục kéo dài gây phóng thích quá mức Glutamate, kích hoạt độc tính tế bào do ion Canxi tràn ngập nội bào tại vùng hải mã."
    },
    {
        "type": "cloze",
        "text": "Theo khuyến cáo của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2011), chỉ định chọc dò dịch não tủy là {{c1::bắt buộc}} khi trẻ có bất kỳ dấu hiệu gợi ý {{c1::viêm màng não}} hoặc nhiễm trùng hệ thần kinh trung ương (cổ cứng, Kernig (+), Brudzinski (+), thóp phồng).",
        "extra": "Cơ chế: Co giật có thể là biểu hiện khởi đầu duy nhất của viêm màng não mủ ở trẻ nhỏ."
    },
    {
        "type": "cloze",
        "text": "Theo khuyến cáo AAP 2011, chọc dò thắt lưng nên được cân nhắc đặc biệt ở trẻ từ {{c1::6 đến 12 tháng tuổi}} bị co giật do sốt nếu trẻ {{c1::chưa được tiêm chủng đầy đủ}} vaccine phòng Hib và Phế cầu khuẩn (hoặc không rõ tiền sử tiêm chủng).",
        "extra": "Cơ chế: Ở lứa tuổi dưới 12 tháng, các dấu hiệu màng não cổ điển thường rất mờ nhạt hoặc không xuất hiện rõ ràng."
    },
    {
        "type": "cloze",
        "text": "Trẻ bị co giật do sốt đang được điều trị bằng {{c1::kháng sinh đường toàn thân}} trước đó nên được cân nhắc chỉ định chọc dịch não tủy vì kháng sinh có thể {{c1::che lấp các triệu chứng lâm sàng}} kinh điển của viêm màng não.",
        "extra": "Cơ chế: Kháng sinh uống làm giảm phản ứng viêm tại màng não nhưng chưa đủ tiệt trùng hoàn toàn dịch não tủy."
    },
    {
        "type": "cloze",
        "text": "Theo khuyến cáo chính thức của AAP 2011, ghi điện não đồ (EEG) và chẩn đoán hình ảnh sọ não (CT/MRI) {{c1::không được khuyến cáo thường quy}} trong đánh giá ban đầu ở trẻ có tình trạng phát triển thần kinh bình thường bị {{c1::co giật do sốt đơn thuần}}.",
        "extra": "Cơ chế: EEG và CT/MRI không dự đoán được nguy cơ tái phát co giật do sốt cũng như không giúp phát hiện bệnh lý não thực thể ở nhóm lành tính này."
    },
    {
        "type": "cloze",
        "text": "Khuyến cáo thực hành lâm sàng của AAP 2008 khẳng định {{c1::không sử dụng}} thuốc chống động kinh (Phenobarbital, Valproate, Carbamazepine, Phenytoin) để điều trị dự phòng liên tục hoặc ngắt quãng cho trẻ bị {{c1::co giật do sốt đơn thuần}}.",
        "extra": "Cơ chế: Thuốc chống động kinh tiềm ẩn nhiều tác dụng phụ nghiêm trọng (Phenobarbital gây suy giảm nhận thức, Valproate gây độc gan) trong khi co giật do sốt đơn thuần là lành tính."
    },
    {
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng ngẫu nhiên của Murata 2018 (Pediatrics) chứng minh dùng {{c1::Paracetamol đặt hậu môn}} liều 10 mg/kg mỗi 6 giờ trong 24 giờ đầu giúp giảm tỷ lệ tái phát co giật trong cùng đợt sốt xuống {{c1::9.1%}} so với {{c1::23.5%}} ở nhóm không dùng hạ sốt.",
        "extra": "Cơ chế: Giữ thân nhiệt ổn định tránh các đợt sốt vọt đột ngột tái diễn trong 24 giờ đầu, nhưng không ngăn được co giật ở các đợt sốt trong tương lai."
    },
    {
        "type": "cloze",
        "text": "Theo phân loại hiện đại của ILAE (2015), mốc thời gian t₁ để kích hoạt xử trí cấp cứu trạng thái động kinh co giật (CSE) là {{c1::5 phút}}, và mốc thời gian t₂ bắt đầu xuất hiện tổn thương tế bào thần kinh không hồi phục là {{c1::30 phút}}.",
        "extra": "Cơ chế: Cơn co giật kéo dài trên 5 phút hầu như không thể tự dứt tự nhiên và cần can thiệp cắt cơn bằng thuốc ngay lập tức."
    },
    {
        "type": "cloze",
        "text": "Hai cơ chế sinh học phân tử cốt lõi duy trì trạng thái động kinh co giật kéo dài là sự nhập bào giảm số lượng thụ thể {{c1::GABA_A (ức chế)}} và sự tăng biểu hiện ra màng tế bào của thụ thể {{c1::NMDA / AMPA (kích thích)}}.",
        "extra": "Cơ chế: Hiện tượng này giải thích vì sao càng để cơn giật kéo dài quá 20-30 phút thì Benzodiazepine càng mất dần hiệu lực cắt cơn (kháng Benzodiazepine)."
    },
    {
        "type": "cloze",
        "text": "Trong bậc 1 điều trị cắt cơn trạng thái động kinh (thời điểm 5–20 phút), liều Midazolam tiêm bắp được khuyến cáo theo AES 2016 là {{c1::0.2 mg/kg}} (liều tối đa một lần là {{c1::10 mg}}).",
        "extra": "Cơ chế: Midazolam hấp thu qua cơ bắp cực nhanh, đạt nồng độ đỉnh trong máu tương đương đường tiêm tĩnh mạch mà không mất thời gian dò tìm tĩnh mạch."
    },
    {
        "type": "cloze",
        "text": "Thử nghiệm lâm sàng RAMPART (NEJM 2012) chứng minh Midazolam tiêm bắp đạt tỷ lệ cắt cơn thành công trước viện là {{c1::73.4%}}, vượt trội so với Lorazepam tiêm tĩnh mạch đạt {{c1::63.4%}} nhờ tiết kiệm thời gian tiếp cận thuốc.",
        "extra": "Cơ chế: Nhóm tiêm bắp đưa được thuốc vào cơ thể chỉ sau 1.2 phút so với 4.8 phút ở nhóm phải thiết lập đường truyền tĩnh mạch."
    },
    {
        "type": "cloze",
        "text": "Trong cấp cứu cắt cơn trạng thái động kinh nếu chưa có đường truyền tĩnh mạch, liều Diazepam bơm hậu môn là {{c1::0.2 đến 0.5 mg/kg}} và liều Midazolam ngậm niêm mạc má là {{c1::0.2 đến 0.5 mg/kg}}.",
        "extra": "Cơ chế: Niêm mạc má và trực tràng có mạng lưới mao mạch phong phú, giúp thuốc hấp thu trực tiếp vào tuần hoàn chung mà không qua chuyển hóa bước đầu tại gan."
    },
    {
        "type": "cloze",
        "text": "Trong xử trí trạng thái động kinh ở trẻ em, số liều Benzodiazepine tối đa được phép dùng trước khi chuyển sang thuốc bậc hai là {{c1::2 liều}} (cách nhau 5-10 phút).",
        "extra": "Cơ chế: Lặp lại quá 2 liều Benzodiazepine làm tăng vọt nguy cơ ức chế trung tâm hô hấp và tụt huyết áp mà không làm tăng thêm tỷ lệ cắt cơn."
    },
    {
        "type": "cloze",
        "text": "Trong bậc 2 điều trị trạng thái động kinh kháng Benzodiazepine (thời điểm 20–40 phút), ba thuốc tĩnh mạch được khuyến cáo tương đương theo thử nghiệm ESETT (NEJM 2019) là {{c1::Levetiracetam}}, {{c1::Fosphenytoin (hoặc Phenytoin)}}, và {{c1::Valproate natri}}.",
        "extra": "Cơ chế: ESETT chứng minh tỷ lệ cắt cơn ở phút 60 tương đương nhau giữa 3 nhóm (Levetiracetam 47%, Fosphenytoin 45%, Valproate 46%)."
    },
    {
        "type": "cloze",
        "text": "Liều nạp đường tĩnh mạch của Levetiracetam trong điều trị bước hai trạng thái động kinh co giật ở trẻ em theo ESETT là {{c1::60 mg/kg}} (liều tối đa {{c1::4500 mg}}), truyền tĩnh mạch trong 5–10 phút.",
        "extra": "Cơ chế: Levetiracetam gắn chọn lọc vào protein túi synap SV2A, ức chế giải phóng các chất dẫn truyền thần kinh kích thích Glutamate."
    },
    {
        "type": "cloze",
        "text": "Liều nạp tĩnh mạch của Valproate natri trong điều trị bước hai trạng thái động kinh co giật ở trẻ em theo ESETT là {{c1::40 mg/kg}} (liều tối đa {{c1::3000 mg}}), truyền trong 5–10 phút.",
        "extra": "Cơ chế: Valproate làm tăng nồng độ GABA trong não qua ức chế enzyme GABA-transaminase và chẹn kênh Natri nhạy cảm điện thế."
    },
    {
        "type": "cloze",
        "text": "Liều nạp tĩnh mạch của Fosphenytoin trong điều trị bước hai trạng thái động kinh co giật là {{c1::20 mg PE/kg}} (liều tối đa {{c1::1500 mg PE}}), truyền trong 10–15 phút.",
        "extra": "Cơ chế: PE là Phenytoin Equivalent (tương đương Phenytoin). Fosphenytoin là tiền chất tan trong nước, pH trung tính, ít gây kích ứng mạch máu hơn Phenytoin."
    },
    {
        "type": "cloze",
        "text": "Hai thử nghiệm ngẫu nhiên lớn ConSEPT và EcLiPSE công bố trên Lancet (2019) chứng minh {{c1::Levetiracetam}} có hiệu quả cắt cơn tương đương {{c1::Phenytoin}}, nhưng có ưu thế vượt trội về độ an toàn tim mạch và không gây biến chứng hoại tử da do thoát mạch.",
        "extra": "Cơ chế: Phenytoin có pH kiềm mạnh (pH 12), nếu thoát mạch sẽ gây viêm tĩnh mạch hoại tử mô nghiêm trọng (Hội chứng găng tay tím - Purple Glove Syndrome)."
    },
    {
        "type": "cloze",
        "text": "Thuốc chống động kinh bước hai Valproate natri chống chỉ định tuyệt đối ở trẻ dưới 2 tuổi nghi ngờ hoặc mắc {{c1::bệnh lý ty thể (Mitochondrial disease)}} do đột biến gen {{c1::POLG}} vì nguy cơ gây suy gan cấp hoại tử tử vong.",
        "extra": "Cơ chế: Valproate ức chế chu trình oxy hóa acid béo trong ty thể, làm cạn kiệt Carnitine và gây tổn thương tế bào gan không thể phục hồi."
    },
    {
        "type": "cloze",
        "text": "Tốc độ truyền tĩnh mạch của Phenytoin không được vượt quá {{c1::1 mg/kg/phút}} (hoặc tối đa {{c1::50 mg/phút}}) và bắt buộc phải theo dõi liên tục {{c1::điện tâm đồ (ECG)}} cùng huyết áp.",
        "extra": "Cơ chế: Dung môi Propylene glycol trong dịch tiêm Phenytoin và tác dụng chẹn kênh Natri cơ tim liều cao có thể gây tụt huyết áp nặng, block nhĩ thất và ngừng tim."
    },
    {
        "type": "cloze",
        "text": "Trạng thái động kinh kháng trị (Refractory Status Epilepticus - RSE) được xác định khi cơn co giật tiếp diễn sau khi đã dùng đủ liều một thuốc {{c1::Benzodiazepine (bước 1)}} và một thuốc {{c1::chống động kinh tĩnh mạch (bước 2)}}.",
        "extra": "Cơ chế: Bắt buộc chuyển trẻ vào khoa Hồi sức tích cực Nhi (PICU), đặt ống nội khí quản thở máy bảo vệ đường thở và dùng thuốc gây mê toàn thân."
    },
    {
        "type": "cloze",
        "text": "Ba thuốc gây mê truyền tĩnh mạch liên tục được lựa chọn hàng đầu trong xử trí trạng thái động kinh kháng trị (RSE) ở trẻ em là {{c1::Midazolam}}, {{c1::Propofol}}, và {{c1::Ketamine}} (hoặc Pentobarbital/Thiopental).",
        "extra": "Cơ chế: Mục tiêu điều trị là đạt kiểu hình điện não triệt tiêu đợt bùng nổ (Burst Suppression Pattern) trên cEEG trong 24–48 giờ."
    },
    {
        "type": "cloze",
        "text": "Hội chứng truyền Propofol (PRIS - Propofol Infusion Syndrome) là một biến chứng nhiễm độc đe dọa tính mạng khi truyền Propofol liều cao kéo dài (> 4-5 mg/kg/giờ quá 48 giờ), đặc trưng bởi {{c1::toan chuyển hóa nặng}}, {{c1::tiêu cơ vân}}, suy tim và tăng Triglyceride máu.",
        "extra": "Cơ chế: Propofol ức chế chuỗi chuyền điện tử ty thể và cản trở oxy hóa acid béo, gây thiếu hụt năng lượng tế bào cấp tính."
    },
    {
        "type": "cloze",
        "text": "Bốn yếu tố nguy cơ kinh điển làm tăng tỷ lệ tái phát co giật do sốt trong tương lai bao gồm: tuổi khởi phát cơn đầu tiên {{c1::< 12 tháng}}, sốt {{c1::nhiệt độ thấp (< 38.5°C)}}, thời gian sốt trước khi giật {{c1::< 1 giờ}}, và tiền sử gia đình có người thân co giật do sốt.",
        "extra": "Cơ chế: Nếu có đủ cả 4 yếu tố nguy cơ, tỷ lệ tái phát cơn giật ở các đợt sốt sau có thể lên tới trên 70%."
    },
    {
        "type": "cloze",
        "text": "Trẻ có co giật do sốt đơn thuần có nguy cơ tiến triển thành bệnh động kinh thực sự sau này là khoảng {{c1::1% đến 2%}}, chỉ nhỉnh hơn một chút so với tỷ lệ mắc động kinh tự nhiên trong dân số nói chung (khoảng {{c1::1%}}).",
        "extra": "Cơ chế: Đây là con số then chốt cần giải thích rõ ràng để giải tỏa tâm lý hoang mang, lo âu tột độ của cha mẹ bệnh nhi."
    },
    {
        "type": "basic",
        "front": "Phân biệt sự khác nhau giữa Co giật do sốt đơn thuần (Simple Febrile Seizures) và Co giật do sốt phức hợp (Complex Febrile Seizures) dựa trên 3 tiêu chí lâm sàng cốt lõi?",
        "back": "<b>Văn bản gốc:</b><br>- Tính chất cơn giật: Đơn thuần mang tính chất toàn thể (Generalised); Phức hợp có tính chất khu trú/cục bộ (Focal).<br>- Thời gian kéo dài: Đơn thuần < 15 phút; Phức hợp kéo dài ≥ 15 phút.<br>- Tần suất trong đợt bệnh: Đơn thuần chỉ 1 cơn duy nhất trong vòng 24 giờ; Phức hợp xuất hiện ≥ 2 cơn trong vòng 24 giờ.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Đơn thuần lành tính, không cần hình ảnh học hay EEG, nguy cơ chuyển động kinh rất thấp (~1-2%).<br>- Phức hợp cần cảnh giác viêm màng não, tổn thương thần kinh thực thể, nguy cơ chuyển thành động kinh cao hơn (~5-10%).",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Nêu 3 chỉ định bắt buộc hoặc cần cân nhắc chặt chẽ chọc dò dịch não tủy (Lumbar Puncture) ở trẻ co giật do sốt theo khuyến cáo của AAP 2011?",
        "back": "<b>Văn bản gốc:</b><br>1. Bắt buộc: Trẻ có bất kỳ dấu hiệu hoặc triệu chứng gợi ý viêm màng não / nhiễm trùng TKTW (cổ cứng, thóp phồng, Kernig/Brudzinski (+), hôn mê li bì sau cơn kéo dài).<br>2. Cân nhắc mạnh mẽ: Trẻ từ 6 đến 12 tháng tuổi chưa tiêm chủng đầy đủ vaccine phòng Hib và Phế cầu khuẩn (hoặc không rõ tiền sử tiêm phòng).<br>3. Cân nhắc: Trẻ đã dùng kháng sinh đường toàn thân trước đó (do kháng sinh che lấp triệu chứng kinh điển của viêm màng não).<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Ở trẻ dưới 12 tháng tuổi, dấu hiệu cứng gáy thường không nhạy, co giật có thể là dấu hiệu duy nhất của nhiễm trùng thần kinh.",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Tóm tắt phác đồ điều trị cắt cơn trạng thái động kinh co giật (CSE) theo từng mốc thời gian dựa trên hướng dẫn chuẩn của AES 2016?",
        "back": "<b>Văn bản gốc:</b><br>- 0–5 phút (Hồi sức ban đầu): ABCDE, thở oxy 100%, đo đường huyết mao mạch, đặt tư thế nằm nghiêng an toàn.<br>- 5–20 phút (Bước 1 - Benzodiazepine): Midazolam tiêm bắp 0.2 mg/kg (tối đa 10 mg) HOẶC Lorazepam IV 0.1 mg/kg HOẶC Diazepam IV 0.2 mg/kg. Lặp lại liều 2 sau 5-10 phút nếu chưa cắt cơn (tối đa 2 liều).<br>- 20–40 phút (Bước 2 - Kháng Benzodiazepine): Truyền tĩnh mạch Levetiracetam 60 mg/kg (tối đa 4500 mg) HOẶC Fosphenytoin 20 mg PE/kg (tối đa 1500 mg PE) HOẶC Valproate 40 mg/kg (tối đa 3000 mg).<br>- > 40 phút (Bước 3 - Kháng trị RSE): Đặt nội khí quản, chuyển PICU, gây mê toàn thân bằng Midazolam, Propofol hoặc Ketamine truyền tĩnh mạch liên tục.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Quy tắc vàng: Hành động khẩn trương, không trì hoãn chờ đợi kết quả xét nghiệm máu khi trẻ đang co giật liên tục.",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Tại sao Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP 2008) khuyến cáo KHÔNG sử dụng thuốc chống động kinh để dự phòng co giật do sốt đơn thuần?",
        "back": "<b>Văn bản gốc:</b><br>- Các thuốc chống động kinh (Phenobarbital, Valproate) không làm giảm nguy cơ phát triển thành bệnh động kinh thực sự trong tương lai.<br>- Nguy cơ và tác dụng phụ nặng nề của thuốc vượt trội hơn lợi ích: Phenobarbital gây giảm nhận thức, rối loạn hành vi, giảm chú ý và hạ IQ; Valproate gây độc gan hoại tử cấp tính gây tử vong và viêm tụy; Carbamazepine và Phenytoin không có hiệu quả dự phòng co giật do sốt.<br>- Bản chất co giật do sốt đơn thuần là lành tính, không gây tổn thương não và không ảnh hưởng đến phát triển trí tuệ.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Trọng tâm điều trị là trấn an, tư vấn giáo dục gia đình và hướng dẫn xử trí sơ cứu ban đầu tại nhà khi sốt.",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Thử nghiệm lâm sàng RAMPART (NEJM 2012) mang lại bằng chứng thực chứng đột phá nào đối với cấp cứu trạng thái động kinh ngoại viện?",
        "back": "<b>Văn bản gốc:</b><br>- Thử nghiệm chứng minh Midazolam tiêm bắp đạt tỷ lệ cắt cơn thành công trước viện 73.4% (329/448), vượt trội có ý nghĩa thống kê so với Lorazepam tiêm tĩnh mạch 63.4% (282/445) với chênh lệch tuyệt đối 10 percentage points (95% CI 4.0 to 16.1, P < 0.001).<br>- Thời gian từ khi nhân viên y tế tiếp cận đến khi đưa được thuốc vào cơ thể ở nhóm tiêm bắp là 1.2 phút so với 4.8 phút ở nhóm tiêm tĩnh mạch (tiết kiệm thời gian quý giá do không phải dò tìm tĩnh mạch).<br>- Tỷ lệ đặt nội khí quản và tái phát co giật ở hai nhóm là tương đương nhau.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Midazolam tiêm bắp là lựa chọn đầu tay tối ưu khi chưa có sẵn đường truyền tĩnh mạch ở bệnh nhân co giật cấp cứu.",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Kết quả cốt lõi của thử nghiệm lâm sàng ESETT (NEJM 2019) về các thuốc chống động kinh bước 2 trong trạng thái động kinh kháng Benzodiazepine là gì?",
        "back": "<b>Văn bản gốc:</b><br>- Tỷ lệ cắt cơn co giật và hồi phục tri giác ở phút thứ 60 giữa 3 nhóm thuốc là tương đương nhau: Levetiracetam đạt 47% (68/145), Fosphenytoin đạt 45% (53/118), và Valproate natri đạt 46% (56/121).<br>- Không có sự khác biệt có ý nghĩa thống kê về tính an toàn và tỷ lệ biến cố bất lợi nặng (suy hô hấp, tụt huyết áp) giữa ba loại thuốc.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Bác sĩ có thể tự tin lựa chọn bất kỳ loại thuốc nào trong 3 thuốc tùy thuộc vào tính sẵn có và chống chỉ định cụ thể của người bệnh (ví dụ tránh Valproate nếu nghi bệnh ty thể, ưu tiên Levetiracetam nếu có nguy cơ loạn nhịp tim).",
        "extra": ""
    },
    {
        "type": "basic",
        "front": "Nêu 4 cạm bẫy thực hành lâm sàng nguy hiểm cần tuyệt đối tránh khi tiếp cận và cấp cứu trẻ co giật do sốt?",
        "back": "<b>Văn bản gốc:</b><br>1. Tuyệt đối không cạy miệng, ngáng đũa, nhét khăn hay vắt chanh vào miệng trẻ đang co giật: Gây gãy răng, tổn thương niêm mạc miệng, hít sặc dị vật vào phổi và tắc nghẽn đường thở.<br>2. Tuyệt đối không lặp lại quá 2 liều Benzodiazepine ở bước 1: Làm tăng vọt nguy cơ ức chế hô hấp và ngừng thở.<br>3. Không dùng Valproate cho trẻ < 2 tuổi nghi ngờ bệnh lý ty thể (đột biến POLG): Nguy cơ hoại tử gan cấp tử vong.<br>4. Không tiêm truyền Phenytoin tĩnh mạch quá nhanh (> 1 mg/kg/phút): Nguy cơ tụt huyết áp kịch phát, loạn nhịp tim và ngừng tuần hoàn.<br><br><b>Góc nhìn bổ sung (AI):</b><br>- Giữ bình tĩnh, đặt trẻ nằm nghiêng an toàn, nới lỏng quần áo và tính chính xác thời gian co giật là nguyên tắc sơ cứu vàng.",
        "extra": ""
    }
]

cards_file.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Successfully generated {len(cards)} flashcards to {cards_file}")
