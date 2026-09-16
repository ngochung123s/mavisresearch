# -*- coding: utf-8 -*-
"""Generate 36 governance-compliant high-yield flashcards for PED-07."""
import json
from pathlib import Path

cards = [
    {
        "type": "cloze",
        "text": "Theo AAP, co giật do sốt được định nghĩa là biến cố co giật xảy ra ở trẻ em trong độ tuổi từ {{c1::6 đến 60 tháng}}, có kèm theo sốt thân nhiệt ≥ {{c1::38.0°C}} mà không có bằng chứng nhiễm trùng thần kinh trung ương hay rối loạn chuyển hóa.",
        "extra": "Cơ chế: Ở lứa tuổi 6 đến 60 tháng, não bộ chưa trưởng thành có ngưỡng kích thích thấp do hệ thống ức chế GABA chưa phát triển hoàn chỉnh."
    },
    {
        "type": "cloze",
        "text": "Co giật do sốt đơn thuần (Simple FS) có tính chất co cứng - co giật {{c1::toàn thể, đối xứng hai bên}}, thời gian kéo dài dưới {{c1::15 phút}} và chỉ xuất hiện {{c1::1 cơn duy nhất}} trong vòng 24 giờ.",
        "extra": "Cơ chế: Co giật do sốt đơn thuần chiếm 70% đến 75% các trường hợp, hoàn toàn lành tính và không để lại di chứng thần kinh."
    },
    {
        "type": "cloze",
        "text": "Co giật do sốt phức tạp (Complex FS) được xác định khi có ít nhất một trong ba đặc điểm: cơn giật {{c1::cục bộ một bên}}, thời gian kéo dài từ {{c1::15 phút trở lên}}, hoặc xuất hiện từ {{c1::2 cơn trở lên}} trong vòng 24 giờ.",
        "extra": "Cơ chế: Co giật do sốt phức tạp chiếm khoảng 20% đến 25% các trường hợp và làm tăng nhẹ nguy cơ tiến triển thành động kinh sau này."
    },
    {
        "type": "cloze",
        "text": "Trạng thái động kinh do sốt (Febrile Status Epilepticus - FSE) là tình trạng co giật liên tục hoặc nhiều cơn co giật ngắt quãng không hồi phục tri giác kéo dài từ {{c1::30 phút trở lên}}.",
        "extra": "Cơ chế: FSE chiếm khoảng 5% các ca co giật do sốt và có thể gây tổn thương phù nề tế bào thần kinh vùng hồi hải mã."
    },
    {
        "type": "cloze",
        "text": "Hội chứng Dravet khởi phát bằng co giật do sốt sớm trước 1 tuổi thường do đột biến gen {{c1::SCN1A}} mã hóa kênh Natri NaV1.1, và chống chỉ định tuyệt đối các thuốc {{c1::chẹn kênh Natri (Carbamazepine, Phenytoin)}}.",
        "extra": "Cơ chế: Thuốc chẹn kênh Natri làm giảm chức năng của các interneuron ức chế GABAergic vốn đã bị khiếm khuyết, làm cơn co giật bùng phát dữ dội hơn."
    },
    {
        "type": "cloze",
        "text": "Trong hội chứng GEFS+ (Genetic Epilepsy with Febrile Seizures Plus), bệnh nhi có đặc điểm co giật do sốt tiếp diễn sau {{c1::6 tuổi}} và di truyền theo tính trạng {{c1::trội trên nhiễm sắc thể thường}}.",
        "extra": "Cơ chế: GEFS+ liên quan đến các đột biến gen kênh ion SCN1A, SCN1B hoặc GABRG2 dẫn đến tăng tính kích thích nơ ron lan tỏa trong gia đình."
    },
    {
        "type": "cloze",
        "text": "Hội chứng FIRES là tình trạng trạng thái động kinh bùng phát dữ dội sau một đợt nhiễm trùng sốt thông thường, đáp ứng kém với thuốc chống động kinh quy ước và đòi hỏi điều trị bằng {{c1::điều hòa miễn dịch (Anakinra) và chế độ ăn sinh ceton}}.",
        "extra": "Cơ chế: FIRES đặc trưng bởi cơn bão viêm thần kinh cấp tính qua thụ thể IL-1 với sự kích hoạt quá mức của tế bào vi mô đệm."
    },
    {
        "type": "cloze",
        "text": "Khi nhiệt độ tăng cao đột ngột, cytokine gây viêm {{c1::IL-1β}} được giải phóng từ tế bào thần kinh đệm kích thích trực tiếp lên thụ thể {{c1::NMDA}}, làm dòng ion Canxi và Natri tràn vào nội bào gây khử cực màng.",
        "extra": "Cơ chế: IL-1β làm tăng cường dẫn truyền kích thích Glutamate và ức chế dòng Clorua qua thụ thể GABAA, hạ thấp ngưỡng co giật."
    },
    {
        "type": "cloze",
        "text": "Tình trạng tăng thông khí thở nhanh do sốt cao gây ra {{c1::kiềm hô hấp}}, làm giảm nồng độ {{c1::Canxi ion hóa}} trong dịch kẽ não tủy và làm tăng tính kích thích màng tế bào thần kinh.",
        "extra": "Cơ chế: Kiềm máu làm tăng gắn kết Canxi với Albumin, làm giảm Canxi tự do ngoại bào vốn đóng vai trò ổn định điện thế màng nơ ron."
    },
    {
        "type": "cloze",
        "text": "Trong chuỗi 5 tầng tổn thương tế bào của trạng thái động kinh, hiện tượng Glutamate tích tụ kích hoạt thụ thể NMDA mở cửa cho ion Canxi tràn vào tế bào thuộc {{c1::Tầng 2 (Độc tính kích thích ngoại bào)}}.",
        "extra": "Cơ chế: Canxi nội bào tăng vọt ở Tầng 3 sẽ kích hoạt Calpain và Caspase-3 phá hủy màng ty thể, dẫn đến hoại tử thần kinh ở Tầng 4."
    },
    {
        "type": "cloze",
        "text": "Hậu quả lâu dài của trạng thái động kinh kéo dài trên 30 phút ở Tầng 5 là hiện tượng {{c1::mọc chồi sợi rêu bất thường (mossy fiber sprouting)}} tại hồi răng, tạo vòng cung phản xạ kích thích tự động dẫn đến động kinh thùy thái dương.",
        "extra": "Cơ chế: Sự tái cấu trúc synap kích thích bất thường làm biến đổi cấu trúc mạng lưới thần kinh vĩnh viễn không thể đảo ngược."
    },
    {
        "type": "cloze",
        "text": "Theo Hướng dẫn AAP 2011, chọc dò tủy sống {{c1::không được khuyến cáo thường quy}} ở trẻ co giật do sốt đơn thuần có tổng trạng tốt và đã được {{c1::tiêm chủng đầy đủ vaccine phế cầu và Hib}}.",
        "extra": "Cơ chế: Tỷ lệ viêm màng não mủ ở trẻ co giật do sốt đơn thuần tỉnh táo hoàn toàn và tiêm chủng đầy đủ là dưới 0.5%."
    },
    {
        "type": "cloze",
        "text": "Theo AAP 2011, chọc dò tủy sống là một lựa chọn cần cân nhắc khi trẻ từ 6 đến 12 tháng tuổi {{c1::chưa được tiêm chủng phế cầu/Hib đầy đủ}} hoặc {{c1::không thể xác minh lịch sử tiêm chủng}}.",
        "extra": "Cơ chế: Ở trẻ chưa tiêm vaccine, các dấu hiệu màng não có thể không rõ ràng trong giai đoạn đầu của viêm màng não do phế cầu hoặc Hib."
    },
    {
        "type": "cloze",
        "text": "Bốn chỉ định bắt buộc phải chọc dò dịch não tủy không thể trì hoãn gồm: có dấu hiệu màng não, dấu hiệu nhiễm độc li bì, {{c1::đang hoặc đã dùng kháng sinh trước đó}}, và trẻ dưới {{c1::6 tháng tuổi}}.",
        "extra": "Cơ chế: Kháng sinh trước đó có thể làm lu mờ triệu chứng cổ cứng; trẻ dưới 6 tháng tuổi co giật có sốt có nguy cơ viêm màng não rất cao."
    },
    {
        "type": "cloze",
        "text": "Theo Guideline AAP 2011, điện não đồ (EEG) và chẩn đoán hình ảnh thần kinh (CT/MRI) {{c1::không được khuyến cáo thường quy}} trong đánh giá ban đầu trẻ co giật do sốt đơn thuần.",
        "extra": "Cơ chế: Bản ghi EEG trong 48 giờ đầu có thể thấy sóng chậm lan tỏa thoáng qua nhưng không có giá trị tiên lượng tái phát hay động kinh tương lai."
    },
    {
        "type": "cloze",
        "text": "Trong phác đồ cấp cứu trạng thái động kinh của Hội Động kinh Hoa Kỳ (AES 2016), mốc T1 là {{c1::5 phút}} (thời điểm bắt đầu can thiệp thuốc cắt cơn) và mốc T2 là {{c1::30 phút}} (thời điểm tổn thương nơ ron không hồi phục bắt đầu xuất hiện).",
        "extra": "Cơ chế: Sau 5 phút, cơ chế tự chấm dứt cơn giật của não thất bại; sau 30 phút, tổn thương tế bào não do cạn kiệt ATP và độc tính Canxi bắt đầu xảy ra."
    },
    {
        "type": "cloze",
        "text": "Trong 5 phút đầu cấp cứu co giật (Phút 0 - 5), ưu tiên hàng đầu là hỗ trợ hô hấp ABCDE và thử nhanh {{c1::đường huyết mao mạch tại giường}}, nếu Glucose < 2.6 mmol/L tiêm tĩnh mạch Glucose 10% liều {{c1::2 mL/kg}}.",
        "extra": "Cơ chế: Hạ đường huyết làm tăng tính kích thích tế bào não và làm nặng thêm tổn thương nơ ron do thiếu hụt năng lượng."
    },
    {
        "type": "cloze",
        "text": "Thuốc cắt cơn bước 1 lựa chọn hàng đầu ngoài bệnh viện khi chưa có đường truyền tĩnh mạch là {{c1::Midazolam tiêm bắp (IM)}} với liều lượng {{c1::0.2 mg/kg}} (tối đa 10 mg cho trẻ > 40 kg).",
        "extra": "Cơ chế: Thử nghiệm RAMPART (NEJM 2012) chứng minh Midazolam IM cắt cơn nhanh hơn và tỷ lệ thành công cao hơn Lorazepam IV do không mất thời gian lấy ven."
    },
    {
        "type": "cloze",
        "text": "Khi đã có sẵn đường truyền tĩnh mạch, thuốc Benzodiazepine bước 1 ưu tiên lựa chọn là {{c1::Lorazepam IV}} liều {{c1::0.1 mg/kg}} (tối đa 4 mg), tiêm tĩnh mạch chậm trong 1 đến 2 phút.",
        "extra": "Cơ chế: Lorazepam có ái lực cao với thụ thể GABAA và thể tích phân bố nhỏ, duy trì tác dụng ức chế thần kinh trung ương kéo dài từ 12 đến 24 giờ."
    },
    {
        "type": "cloze",
        "text": "Nếu dùng Diazepam đường tĩnh mạch để cắt cơn, liều khuyến cáo là {{c1::0.2 mg/kg}} (tối đa 10 mg) và tốc độ tiêm không được vượt quá {{c1::2 mg/phút}}.",
        "extra": "Cơ chế: Tiêm Diazepam quá nhanh có thể gây ngừng thở đột ngột, co thắt thanh quản và tụt huyết áp do dung môi propylene glycol."
    },
    {
        "type": "cloze",
        "text": "Trong xử trí bước 1 trạng thái động kinh, số liều Benzodiazepine tối đa được phép dùng trước khi chuyển sang thuốc bước 2 là {{c1::2 liều}}.",
        "extra": "Cơ chế: Dùng từ 3 liều Benzodiazepine trở lên làm tăng vọt nguy cơ suy hô hấp, ngừng thở và tụt huyết áp mà không làm tăng tỷ lệ cắt cơn giật."
    },
    {
        "type": "cloze",
        "text": "Theo hướng dẫn AES 2016, ba lựa chọn thuốc chống động kinh bước 2 đường tĩnh mạch cho trạng thái động kinh kháng Benzodiazepine là {{c1::Levetiracetam, Fosphenytoin và Sodium Valproate}}.",
        "extra": "Cơ chế: Thử nghiệm ESETT (NEJM 2019) chứng minh cả ba loại thuốc này đạt hiệu quả cắt cơn và hồi phục tri giác tương đương nhau (khoảng 45% đến 47%)."
    },
    {
        "type": "cloze",
        "text": "Liều khuyến cáo của Levetiracetam (Keppra) truyền tĩnh mạch trong điều trị bước 2 trạng thái động kinh là {{c1::60 mg/kg}} (tối đa 4500 mg), truyền tĩnh mạch trong {{c1::5 đến 10 phút}}.",
        "extra": "Cơ chế: Levetiracetam rất an toàn về tim mạch, không gây tụt huyết áp hay loạn nhịp, thời gian truyền nhanh vượt trội so với Phenytoin."
    },
    {
        "type": "cloze",
        "text": "Cơ chế phân tử độc đáo của Levetiracetam là gắn chọn lọc vào protein túi synap {{c1::SV2A}}, ức chế giải phóng chất dẫn truyền thần kinh kích thích {{c1::Glutamate}} vào khe synap.",
        "extra": "Cơ chế: Thuốc thải trừ 66% qua thận dưới dạng nguyên vẹn, không chuyển hóa qua Cytochrome P450 nên không gây tương tác thuốc bất lợi."
    },
    {
        "type": "cloze",
        "text": "Liều khuyến cáo của Fosphenytoin đường tĩnh mạch là {{c1::20 mg PE/kg}} (tối đa 1500 mg PE), với tốc độ truyền tối đa là {{c1::150 mg PE/phút}}.",
        "extra": "Cơ chế: Fosphenytoin là tiền chất tan trong nước của Phenytoin, không chứa propylene glycol nên tránh được biến chứng hoại tử mô hội chứng găng tay tím."
    },
    {
        "type": "cloze",
        "text": "Khi pha dung dịch Phenytoin truyền tĩnh mạch, dung dịch pha duy nhất được phép sử dụng là {{c1::Natri Clorid 0.9%}}, tuyệt đối không được pha trong {{c1::Glucose}} vì gây kết tủa tinh thể.",
        "extra": "Cơ chế: Phenytoin chỉ tan ở pH kiềm cao (pH 12), khi gặp môi trường toan của Glucose sẽ kết tủa tinh thể gây tắc mạch và hoại tử mô."
    },
    {
        "type": "cloze",
        "text": "Liều khuyến cáo của Sodium Valproate đường tĩnh mạch là {{c1::40 mg/kg}} (tối đa 3000 mg), và thuốc chống chỉ định tuyệt đối khi nghi ngờ {{c1::bệnh lý ty thể (đột biến gen POLG) hoặc suy gan cấp}}.",
        "extra": "Cơ chế: Valproate gây ức chế chu trình oxy hóa beta acid béo trong ty thể, dẫn đến hoại tử tế bào gan cấp tính tử vong ở trẻ có khiếm khuyết ty thể."
    },
    {
        "type": "cloze",
        "text": "Hai thử nghiệm nhi khoa ConSEPT và EcLiPSE (Lancet 2019) chứng minh rằng Levetiracetam {{c1::không vượt trội hơn Phenytoin}} về tỷ lệ cắt cơn, nhưng có ưu thế vượt trội về {{c1::thời gian pha truyền nhanh hơn và an toàn tim mạch cao hơn}}.",
        "extra": "Cơ chế: Phenytoin cần truyền chậm trong 20 phút và theo dõi điện tim liên tục, trong khi Levetiracetam truyền xong trong 5 đến 10 phút mà không cần monitoring tim mạch phức tạp."
    },
    {
        "type": "cloze",
        "text": "Theo thử nghiệm ngẫu nhiên của Murata 2018 trên tạp chí Pediatrics, việc đặt hậu môn Acetaminophen liều {{c1::10 mg/kg mỗi 6 giờ}} giúp làm giảm an toàn tỷ lệ tái phát co giật {{c1::trong cùng một đợt sốt (9.1% so với 23.5%)}}.",
        "extra": "Cơ chế: Mặc dù thuốc hạ sốt không ngăn được cơn co giật trong các đợt bệnh tương lai, việc kiểm soát thân nhiệt ổn định giúp giảm tỷ lệ tái phát ngắn hạn trong 24 giờ đầu."
    },
    {
        "type": "cloze",
        "text": "Theo nghiên cứu đoàn hệ FEBSTAT, khoảng {{c1::11.5%}} trẻ bị trạng thái động kinh do sốt có tổn thương cấp tính ở {{c1::hồi hải mã}} trên phim MRI, tiến triển thành xơ teo hồi hải mã và động kinh thùy thái dương sau này.",
        "extra": "Cơ chế: Tỷ lệ động kinh sau co giật do sốt đơn thuần chỉ là 1% đến 2%, nhưng sau trạng thái động kinh do sốt (FSE) tỷ lệ này tăng vọt lên 10% đến 15%."
    },
    {
        "type": "cloze",
        "text": "Hướng dẫn thực hành lâm sàng AAP 2008 khuyến cáo {{c1::KHÔNG điều trị dự phòng thường quy}} bằng thuốc chống động kinh liên tục hoặc ngắt quãng cho trẻ co giật do sốt đơn thuần vì {{c1::tác dụng phụ của thuốc vượt trội hơn hẳn lợi ích}}.",
        "extra": "Cơ chế: Co giật do sốt đơn thuần hoàn toàn lành tính, không gây tử vong hay tổn thương não, trong khi Phenobarbital và Valproate gây độc gan và suy giảm trí tuệ."
    },
    {
        "type": "cloze",
        "text": "Tác dụng không mong muốn nghiêm trọng nhất khiến Phenobarbital bị loại bỏ trong điều trị dự phòng co giật do sốt ở trẻ nhỏ là {{c1::suy giảm nhận thức, giảm chỉ số IQ và rối loạn hành vi kích động}}.",
        "extra": "Cơ chế: Phenobarbital tác động lên thụ thể GABAA toàn thể trong não đang phát triển, làm ức chế synap kéo dài và cản trở quá trình hình thành đuôi gai nơ ron."
    },
    {
        "type": "cloze",
        "text": "Yếu tố dự báo mạnh nhất cho nguy cơ tái phát co giật do sốt ở trẻ nhỏ là {{c1::tuổi khởi phát cơn đầu tiên dưới 12 tháng tuổi}} (nguy cơ tái phát lên tới {{c1::50%}}).",
        "extra": "Cơ chế: Khởi phát càng sớm chứng tỏ ngưỡng co giật bẩm sinh của não càng thấp, trẻ còn nhiều đợt sốt nhiễm trùng trong các năm tiếp theo."
    },
    {
        "type": "cloze",
        "text": "Hành vi chèn thìa, đũa hoặc ngón tay vào miệng trẻ đang co giật là bẫy nguy hiểm phổ biến, có thể gây {{c1::gãy răng, chấn thương mô mềm và tắc nghẽn đường thở dẫn đến tử vong do ngạt}}.",
        "extra": "Cơ chế: Trẻ đang co giật không bao giờ tự cắn đứt lưỡi; hành động chèn vật cứng kích thích phản xạ nôn và đẩy đàm nhớt, răng gãy vào khí quản."
    },
    {
        "type": "cloze",
        "text": "Sau cơn co giật do sốt, trẻ {{c1::hoàn toàn KHÔNG bị chống chỉ định tiêm chủng}} và cần được tiếp tục tiêm phòng đầy đủ tất cả các loại vaccine theo lịch tiêm chủng mở rộng.",
        "extra": "Cơ chế: Lợi ích bảo vệ của vaccine chống viêm màng não, viêm não, sởi vượt trội hoàn toàn so với nguy cơ co giật do sốt lành tính thoáng qua sau tiêm."
    },
    {
        "type": "cloze",
        "text": "Thuốc cấp cứu cắt cơn tại nhà có thể kê đơn cho gia đình có tiền sử co giật kéo dài trên 5 phút hoặc ở xa bệnh viện là {{c1::Midazolam ngậm niêm mạc má (Buccal Midazolam)}} hoặc {{c1::Diazepam gel thụt trực tràng (Diastat)}}.",
        "extra": "Cơ chế: Thuốc hấp thu nhanh chóng qua niêm mạc miệng hoặc trực tràng vào tuần hoàn, giúp cắt cơn giật sớm trước khi chuyển biến thành trạng thái động kinh."
    }
]

target_cards_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.cards.v2.json")
target_cards_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Generated {len(cards)} flashcards to {target_cards_path} successfully.")
