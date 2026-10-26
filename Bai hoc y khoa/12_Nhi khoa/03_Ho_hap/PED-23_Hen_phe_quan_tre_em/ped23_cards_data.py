# -*- coding: utf-8 -*-
# PED-23 Hen phế quản trẻ em — nguồn thẻ duy nhất (barem gốc: 19 slide bài giảng Bộ môn Nhi).
# Mã barem từng dòng: Hen_phe_quan_PEDYTB.md (mỗi mã [Bx.yy] phải có ≥ 1 thẻ, ghi ở `extra`).


def _c(color, text):
    return f'<span style="color:{color}"><b>{text}</b></span>'


def R(t):  # cờ đỏ / triệu chứng bệnh lý
    return _c("#ff6b6b", t)


def Y(t):  # con số / ngưỡng / lứa tuổi
    return _c("#ffd43b", t)


def G(t):  # xử trí / thuốc
    return _c("#51cf66", t)


def B(t):  # tên bệnh / phân loại / thực thể
    return _c("#74c0fc", t)


BADGE = ("🏛️ BAREM GỐC · SLIDE BỘ MÔN NHI", "badge-barem")
SRC = "📖 Nguồn: Slide bài giảng Hen phế quản trẻ em — Bộ môn Nhi (19 ảnh chụp slide, nhận ngày 26/10/2026). Barem: "
KS_ASKS = ["Triệu chứng ban ngày", "Hạn chế hoạt động", "Triệu chứng ban đêm", "Nhu cầu thuốc cắt cơn",
           "Chức năng phổi", "Đợt kịch phát"]


def basic(cid, section, category, tier, front, core, ai, barem, tags, asks=None):
    card = {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "basic", "section": section, "category": category, "tier": tier,
        "front": front,
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>" + core + "<br><br><b>💡 Giải thích của AI:</b><br>" + ai,
        "extra": SRC + barem,
        "tags": ["PED-23", "Barem-goc"] + tags,
    }
    if asks:
        card["asks"] = asks
    return card


def algo(cid, section, category, title, core, ai, barem, tags):
    card = basic(cid, section, category, 1, "⚡ THUẬT TOÁN QUYẾT ĐỊNH — " + B(title), core, ai, barem,
                 tags + ["Thuat-toan"])
    card.pop("badge")
    card.pop("badge_class")
    return card


def cloze(cid, section, category, text, barem, tags):
    return {
        "id": cid, "track": "barem_goc", "badge": BADGE[0], "badge_class": BADGE[1],
        "type": "cloze", "section": section, "category": category, "tier": 2,
        "text": text, "extra": SRC + barem,
        "tags": ["PED-23", "Barem-goc", "Cloze-phu"] + tags,
    }


cards_data = [
    # ------------------------------------------------------------ B0. Chẩn đoán > 5 tuổi: lâm sàng & tiền sử
    basic(
        "PED23-B0-01", "B0", "Chẩn đoán hen trẻ > 5 tuổi", 1,
        f"{B('[Chẩn đoán hen trẻ > 5 tuổi — GINA 2019]')} Chẩn đoán dựa trên {Y('2 nhóm bằng chứng')} lớn nào?",
        f"1) {B('Nhóm 1')} — dựa vào {R('triệu chứng lâm sàng và tiền sử')}.<br>"
        f"2) {B('Nhóm 2')} — {G('bằng chứng của luồng thông khí thở ra thay đổi')} (đo chức năng hô hấp, PEF).",
        "Đây là khung tầng 1. Hen là bệnh có triệu chứng thay đổi và tắc nghẽn thay đổi: chỉ có triệu chứng thì chưa đủ "
        "(nhiều bệnh khác cũng gây ho, khò khè), nên GINA yêu cầu thêm bằng chứng khách quan rằng luồng khí thở ra dao động "
        "bất thường. Trẻ > 5 tuổi đã hợp tác đo hô hấp ký được, nên nhóm 2 làm được — khác với trẻ ≤ 5 tuổi.",
        "B0.01, B1.01", ["Chan-doan", "Khung-bai"],
    ),
    basic(
        "PED23-B0-02", "B0", "Chẩn đoán hen trẻ > 5 tuổi", 2,
        f"{B('[Hen trẻ > 5 tuổi]')} Kể {Y('4 triệu chứng lâm sàng điển hình')} của hen, và thường xuất hiện đơn lẻ hay phối hợp?",
        f"1) {R('Ho')}.<br>2) {R('Khò khè')}.<br>3) {R('Khó thở')}.<br>4) {R('Nặng ngực')}.<br>"
        f"→ Thường có {Y('nhiều hơn một')} triệu chứng này cùng lúc.",
        "Một triệu chứng đơn lẻ (ví dụ ho kéo dài đơn thuần) ít gợi ý hen. Khi ho đi kèm khò khè, khó thở, nặng ngực thì "
        "khả năng hen tăng lên rõ, vì cả bốn đều là hậu quả của cùng một cơ chế: co thắt cơ trơn, phù nề niêm mạc và tăng "
        "tiết nhầy làm hẹp đường thở.",
        "B0.01, B0.02", ["Chan-doan", "Lam-sang"],
    ),
    basic(
        "PED23-B0-03", "B0", "Chẩn đoán hen trẻ > 5 tuổi", 2,
        f"{B('[Hen trẻ > 5 tuổi]')} Triệu chứng hen diễn biến {Y('theo thời gian')} như thế nào và hay xảy ra {Y('vào lúc nào')} trong ngày?",
        f"1) {R('Thay đổi theo thời gian và cường độ')} (lúc có lúc không, lúc nặng lúc nhẹ).<br>"
        f"2) Hay xảy ra {Y('ban đêm hoặc lúc thức giấc')}.",
        "Tính thay đổi là dấu ấn của hen: tắc nghẽn hồi phục được, tự nhiên hoặc sau thuốc. Ban đêm và sáng sớm trương lực "
        "phó giao cảm tăng, cortisol nội sinh thấp, nên co thắt phế quản dễ bộc lộ — vì vậy hỏi 'con có ho, khò khè về đêm "
        "không' là câu hỏi rất có giá trị.",
        "B0.03, B0.04", ["Chan-doan", "Lam-sang"],
    ),
    basic(
        "PED23-B0-04", "B0", "Chẩn đoán hen trẻ > 5 tuổi", 2,
        f"{B('[Hen trẻ > 5 tuổi]')} Kể các {R('yếu tố khởi phát')} triệu chứng hen, và triệu chứng hay xấu đi sau loại nhiễm trùng nào?",
        f"1) {R('Tập thể dục')}.<br>2) {R('Cười lớn')}.<br>3) {R('Tiếp xúc với dị nguyên')}.<br>4) {R('Không khí lạnh')}.<br>"
        f"5) Triệu chứng thường xảy ra hoặc xấu đi {R('sau nhiễm virus')}.",
        "Gắng sức, cười lớn, khí lạnh làm tăng thông khí và làm khô, lạnh niêm mạc đường thở → kích thích phế quản vốn tăng "
        "phản ứng co thắt. Dị nguyên gây phản ứng viêm qua IgE. Nhiễm virus hô hấp là yếu tố khởi phát cơn hen thường gặp "
        "nhất ở trẻ em.",
        "B0.05, B0.06", ["Chan-doan", "Yeu-to-khoi-phat"],
    ),

    # ------------------------------------------------------------ B1. Bằng chứng luồng thông khí thay đổi
    basic(
        "PED23-B1-01", "B1", "Bằng chứng luồng thông khí thay đổi", 1,
        f"{B('[Hen trẻ > 5 tuổi — GINA 2019]')} Kể {Y('5 bằng chứng')} của {G('luồng thông khí thở ra thay đổi')}.",
        f"1) Ít nhất một lần có {R('FEV1 thấp')} và {R('tỷ số FEV1/FVC giảm')}.<br>"
        f"2) Dao động chức năng hô hấp {R('cao hơn người bình thường')}.<br>"
        f"3) {G('Test phục hồi phế quản')}: FEV1 tăng {Y('hơn 12% và 200 ml')} sau hít thuốc giãn phế quản.<br>"
        f"4) {G('PEF')} dao động trung bình hằng ngày {Y('> 10%')}.<br>"
        f"5) FEV1 tăng {Y('hơn 12% và 200 ml')} so với ban đầu sau {Y('4 tuần')} điều trị dự phòng dạng hít.",
        "Ý 1 chứng minh có tắc nghẽn. Ý 2–5 chứng minh tắc nghẽn đó thay đổi được: tự dao động trong ngày (PEF), hồi phục "
        "nhanh sau giãn phế quản, hoặc cải thiện sau thời gian chống viêm. Tắc nghẽn có hồi phục chính là điểm phân biệt hen "
        "với các bệnh tắc nghẽn cố định.",
        "B1.01, B1.02, B1.03, B1.04, B1.05", ["Chan-doan", "CNHH"],
    ),
    basic(
        "PED23-B1-02", "B1", "Bằng chứng luồng thông khí thay đổi", 2,
        f"{B('[Test phục hồi phế quản]')} Test này làm thế nào, và kết quả {Y('dương tính')} khi nào?",
        f"1) Đo FEV1 trước, rồi cho {G('hít thuốc giãn phế quản (GPQ)')} và đo lại.<br>"
        f"2) Dương tính khi {R('FEV1 tăng hơn')} {Y('12% và 200 ml')} so với trước hít.",
        "Phải đạt cả hai ngưỡng: tỷ lệ % và thể tích tuyệt đối. Chỉ dùng % thì ở trẻ có FEV1 nền nhỏ, một thay đổi rất nhỏ "
        "về thể tích cũng có thể vượt 12% do sai số đo; thêm ngưỡng 200 ml giúp chắc chắn đó là thay đổi thật.",
        "B1.03", ["Chan-doan", "Test-phuc-hoi"],
    ),
    cloze(
        "PED23-B1-03", "B1", "Bằng chứng luồng thông khí thay đổi",
        f"Test phục hồi phế quản dương tính khi FEV1 tăng hơn {{{{c1::{Y('12% và 200 ml')}}}}} sau khi hít thuốc giãn phế quản.",
        "B1.03", ["Test-phuc-hoi"],
    ),
    cloze(
        "PED23-B1-04", "B1", "Bằng chứng luồng thông khí thay đổi",
        f"Bằng chứng luồng thông khí thay đổi: PEF dao động trung bình hằng ngày {{{{c1::{Y('> 10%')}}}}}.",
        "B1.04", ["PEF"],
    ),
    cloze(
        "PED23-B1-05", "B1", "Bằng chứng luồng thông khí thay đổi",
        f"FEV1 tăng hơn 12% và 200 ml so với giá trị ban đầu sau {{{{c1::{Y('4 tuần')}}}}} điều trị dự phòng dạng hít cũng là bằng chứng của hen.",
        "B1.05", ["Dieu-tri-thu"],
    ),

    # ------------------------------------------------------------ B2. Lưu ý khi thăm dò
    basic(
        "PED23-B2-01", "B2", "Lưu ý khi thăm dò chức năng hô hấp", 2,
        f"{B('[Thăm dò chức năng hô hấp trong hen]')} Nên {G('lặp lại thăm dò')} vào những thời điểm nào, và vì sao càng nhiều lần đánh giá càng tốt?",
        f"1) Thời điểm lặp lại: {Y('khi xảy ra triệu chứng')}, {Y('vào sáng sớm')}, hoặc {Y('sau khi dùng thuốc giãn phế quản')}.<br>"
        f"2) Lý do: {R('dao động vượt mức')} càng lớn và thấy trong càng nhiều lần đánh giá thì {G('chẩn đoán càng chắc chắn')}.",
        "Ngoài cơn, chức năng hô hấp của trẻ hen có thể hoàn toàn bình thường. Đo đúng lúc có triệu chứng hoặc sáng sớm "
        "(lúc phế quản co thắt nhiều nhất) giúp 'bắt' được tắc nghẽn; đo lại sau thuốc giãn phế quản cho thấy nó hồi phục.",
        "B2.01, B2.02", ["Chan-doan", "CNHH"],
    ),
    basic(
        "PED23-B2-02", "B2", "Lưu ý khi thăm dò chức năng hô hấp", 2,
        f"{B('[Test phục hồi phế quản âm tính]')} Test có thể {R('không thấy phục hồi')} trong hoàn cảnh nào, khi đó bước tiếp theo dựa vào đâu, và có thể làm thêm thăm dò nào?",
        f"1) Có thể không thấy phục hồi trong {R('cơn hen kịch phát nặng')} hoặc khi {R('nhiễm virus')}.<br>"
        f"2) Bước tiếp theo phụ thuộc {Y('mức độ nặng trên lâm sàng')} và {Y('các thăm dò khác')}.<br>"
        f"3) Thăm dò thêm: {G('test kích thích phế quản')}, {G('đo nồng độ NO')} (khí thở ra).",
        "Trong cơn nặng hoặc khi nhiễm virus, đường thở phù nề và đầy đờm nên thuốc giãn phế quản không mở ra được ngay → "
        "test âm tính giả. Test âm tính một lần không loại trừ hen. Test kích thích phế quản tìm tăng phản ứng đường thở; "
        "NO khí thở ra phản ánh viêm đường thở tăng bạch cầu ái toan.",
        "B2.03, B2.04, B2.05", ["Chan-doan", "Bay"],
    ),

    # ------------------------------------------------------------ B3. Chẩn đoán ≤ 5 tuổi
    basic(
        "PED23-B3-01", "B3", "Chẩn đoán hen trẻ ≤ 5 tuổi", 1,
        f"{B('[Chẩn đoán hen trẻ ≤ 5 tuổi — GINA 2019]')} Nêu {Y('4 ý')} khái quát về chẩn đoán hen ở lứa tuổi này.",
        f"1) Đây là {R('một thách thức')}.<br>"
        f"2) Chẩn đoán {G('chủ yếu dựa vào lâm sàng')}.<br>"
        f"3) Triệu chứng chủ yếu để chẩn đoán là {R('khò khè tái đi tái lại')} hay {R('khò khè dai dẳng')}.<br>"
        f"4) Cần {G('chẩn đoán phân biệt')} với các nguyên nhân gây khò khè khác ở trẻ em.",
        "Trẻ ≤ 5 tuổi chưa hợp tác đo hô hấp ký, nên không có bằng chứng khách quan như trẻ lớn. Thêm nữa, khò khè do virus "
        "rất phổ biến ở lứa tuổi này và phần lớn tự hết khi lớn — đó là lý do chẩn đoán khó và phải loại trừ nguyên nhân khác "
        "(dị vật, trào ngược, dị tật đường thở, viêm tiểu phế quản…).",
        "B3.01, B3.02, B3.03, B3.04", ["Chan-doan", "Duoi-5-tuoi"],
    ),
    basic(
        "PED23-B3-02", "B3", "Chẩn đoán hen trẻ ≤ 5 tuổi", 2,
        f"{B('[Hen trẻ ≤ 5 tuổi]')} Kể {Y('4 dữ kiện')} dùng để chẩn đoán hen ở trẻ ≤ 5 tuổi theo slide.",
        f"1) Khò khè hoặc ho xảy ra {R('sau gắng sức, sau cười, khóc')} mà {Y('không có dấu hiệu nhiễm khuẩn')}.<br>"
        f"2) Tiền sử {B('bệnh dị ứng')} (chàm, viêm mũi dị ứng) hoặc {B('hen ở bố mẹ')}.<br>"
        f"3) Lâm sàng {G('cải thiện sau 2–3 tháng điều trị dự phòng')}, {R('xấu đi khi ngừng thuốc')}.<br>"
        f"4) {G('Loại trừ')} các chẩn đoán phân biệt khác.",
        "Ý 1 tách khò khè do hen (do kích thích không nhiễm trùng) khỏi khò khè chỉ đi kèm cảm lạnh. Ý 2 là nền cơ địa dị ứng. "
        "Ý 3 là điều trị thử: đáp ứng rồi tái phát khi ngừng thuốc là bằng chứng gián tiếp mạnh nhất ở trẻ nhỏ, thay cho "
        "test phục hồi phế quản ở trẻ lớn.",
        "B3.05, B3.06, B3.07, B3.08", ["Chan-doan", "Duoi-5-tuoi"],
    ),
    cloze(
        "PED23-B3-03", "B3", "Chẩn đoán hen trẻ ≤ 5 tuổi",
        f"Trẻ ≤ 5 tuổi: triệu chứng cải thiện sau {{{{c1::{Y('2–3 tháng')}}}}} điều trị dự phòng và xấu đi khi ngừng thuốc gợi ý hen.",
        "B3.07", ["Dieu-tri-thu"],
    ),

    # ------------------------------------------------------------ B4. API
    basic(
        "PED23-B4-01", "B4", "Chỉ số tiên đoán hen (API)", 2,
        f"{B('[Chỉ số tiên đoán hen — API]')} Kể {Y('3 tiêu chuẩn chính')} của API.",
        f"1) {B('Cha, mẹ bị hen')}.<br>"
        f"2) {B('Chàm da')} (được bác sĩ chẩn đoán).<br>"
        f"3) {B('Dị ứng với dị nguyên đường hít')} (xác định bằng bệnh sử hoặc test dị ứng).",
        "Ba tiêu chuẩn chính đều phản ánh cơ địa dị ứng mạnh (di truyền từ bố mẹ, chàm, mẫn cảm dị nguyên hô hấp). Bổ sung "
        "ngoài slide: theo API cải biên, trẻ có khò khè tái diễn (≥ 4 đợt/năm) kèm ≥ 1 tiêu chuẩn chính hoặc ≥ 2 tiêu chuẩn phụ "
        "thì nguy cơ thành hen thật sự khi lớn tăng cao.",
        "B4.01, B4.02, B4.03", ["API"],
    ),
    basic(
        "PED23-B4-02", "B4", "Chỉ số tiên đoán hen (API)", 2,
        f"{B('[Chỉ số tiên đoán hen — API]')} Kể {Y('3 tiêu chuẩn phụ')} của API.",
        f"1) {R('Khò khè không liên quan đến cảm lạnh')}.<br>"
        f"2) {R('Eosinophil máu ngoại vi')} {Y('≥ 4%')}.<br>"
        f"3) {B('Dị ứng thức ăn')}.",
        "Khò khè không do cảm lạnh gợi ý co thắt phế quản do cơ địa chứ không chỉ do virus. Eosinophil tăng và dị ứng thức ăn "
        "là dấu hiệu viêm type 2 (dị ứng). Đây là các yếu tố yếu hơn nên cần ≥ 2 tiêu chuẩn phụ mới tương đương 1 tiêu chuẩn chính "
        "(quy tắc tính điểm là bổ sung ngoài slide).",
        "B4.04, B4.05, B4.06", ["API"],
    ),
    cloze(
        "PED23-B4-03", "B4", "Chỉ số tiên đoán hen (API)",
        f"Tiêu chuẩn phụ của API: eosinophil máu ngoại vi {{{{c1::{Y('≥ 4%')}}}}}.",
        "B4.05", ["API"],
    ),

    # ------------------------------------------------------------ B5. Triệu chứng cơn hen cấp
    basic(
        "PED23-B5-01", "B5", "Triệu chứng cơn hen cấp", 2,
        f"{B('[Cơn hen cấp]')} Kể {Y('4 triệu chứng cơ năng')} của cơn hen cấp và các dấu hiệu {Y('báo trước')} cơn.",
        f"1) {R('Ho')}.<br>2) {R('Khò khè')}.<br>3) {R('Khó thở')}.<br>4) {R('Nặng ngực')}.<br>"
        f"5) Báo trước: {R('hắt hơi, ngứa mũi, ngạt mũi, chảy nước mũi')}; hoặc {R('chán ăn, đau bụng, nặng ngực')}…",
        "Dấu hiệu báo trước thường là triệu chứng mũi (viêm mũi dị ứng hoặc nhiễm virus khởi đầu) — đường hô hấp trên và dưới "
        "là một khối liên tục. Ở trẻ nhỏ, đau bụng và chán ăn có thể là cách trẻ diễn tả cảm giác khó thở, nặng ngực.",
        "B5.01, B5.02, B5.03, B5.04, B5.05", ["Lam-sang", "Co-nang"],
    ),
    basic(
        "PED23-B5-02", "B5", "Triệu chứng cơn hen cấp", 2,
        f"{B('[Cơn hen cấp]')} Khi {Y('gõ phổi')} và {Y('nghe phổi')} thấy gì, và lồng ngực thay đổi ra sao khi {R('HPQ kéo dài')}?",
        f"1) Gõ phổi: có thể {R('vang hơn bình thường')}.<br>"
        f"2) Nghe phổi: {R('ran rít, ran ngáy, tiếng khò khè')}; rì rào phế nang âm sắc trở nên rít; {R('thì thở ra mạnh và kéo dài')}.<br>"
        f"3) HPQ kéo dài: lồng ngực có thể {R('nhô ra phía trước, biến dạng')}.",
        "Hẹp đường thở làm khí vào được nhưng ra khó → bẫy khí, phổi căng (gõ vang) và thì thở ra kéo dài. Luồng khí qua phế "
        "quản hẹp tạo tiếng rít, ngáy. Ứ khí mạn tính lâu ngày ở trẻ đang lớn làm lồng ngực biến dạng nhô ra trước.",
        "B5.06, B5.07, B5.08", ["Lam-sang", "Thuc-the"],
    ),

    # ------------------------------------------------------------ B6. Cận lâm sàng
    basic(
        "PED23-B6-01", "B6", "Cận lâm sàng", 1,
        f"{B('[Cận lâm sàng trong hen]')} Kể {Y('4 thăm dò')} được nêu và {G('mục đích')} của từng thăm dò.",
        f"1) {G('Đo lưu lượng đỉnh thì thở ra (PEF)')}: giúp chẩn đoán, đánh giá mức độ nặng của hen.<br>"
        f"2) {G('X quang ngực')}: thấy ứ khí, giãn lồng ngực và biến chứng tắc nghẽn (xẹp phổi).<br>"
        f"3) {G('Khí máu')}: làm {R('khi có suy hô hấp')}.<br>"
        f"4) {G('Thăm dò chức năng hô hấp')}: đánh giá mức độ nặng, độ tắc nghẽn đường thở và kết quả điều trị.",
        "PEF rẻ, làm tại giường và tại nhà, nên dùng để theo dõi. Hô hấp ký chính xác hơn, đo được nhiều chỉ số. X quang không "
        "để chẩn đoán hen mà để tìm biến chứng hoặc bệnh khác. Khí máu chỉ cần khi cơn nặng có suy hô hấp — PaCO₂ bình thường "
        "hoặc tăng ở trẻ đang thở nhanh là dấu hiệu mệt cơ, sắp ngừng thở.",
        "B6.01, B6.04, B6.05", ["Can-lam-sang", "Khung-bai"],
    ),
    basic(
        "PED23-B6-02", "B6", "Cận lâm sàng", 2,
        f"{B('[X quang ngực trong hen]')} Hình ảnh X quang thay đổi thế nào {Y('theo giai đoạn')}, và thấy gì khi trẻ {R('ho khạc nhiều đờm')}?",
        f"1) Giai đoạn đầu: thường {Y('bình thường')}.<br>"
        f"2) Sau đó: {R('lồng ngực giãn rộng, có hiện tượng ứ khí')}.<br>"
        f"3) Ho khạc nhiều đờm: có thể thấy biến chứng tắc nghẽn — {R('rối loạn thông khí, xẹp phổi')}.",
        "X quang bình thường không loại trừ hen. Ứ khí là hậu quả của bẫy khí thì thở ra. Nút nhầy bít phế quản làm phần phổi "
        "phía sau hết khí → xẹp phổi; hay gặp ở trẻ nhỏ vì phế quản nhỏ và thông khí bàng hệ kém.",
        "B6.02, B6.03", ["Can-lam-sang", "X-quang"],
    ),
    basic(
        "PED23-B6-03", "B6", "Cận lâm sàng", 2,
        f"{B('[Chức năng hô hấp trong hen]')} Các chỉ số {Y('FEV1, FVC, FEV1/FVC, RV')} thay đổi thế nào, và {B('vòng lưu lượng–thể tích')} kiểu tắc nghẽn trông ra sao?",
        f"1) {R('FEV1 giảm')}.<br>2) {R('FVC giảm')}.<br>3) {R('Tỷ lệ FEV1/FVC giảm')}.<br>4) {R('Dung tích cặn (RV) tăng')}.<br>"
        f"5) Vòng lưu lượng–thể tích: nhánh thở ra {R('lõm xuống')} (khác dạng tam giác thẳng của người bình thường).",
        "FEV1/FVC giảm là dấu ấn của rối loạn thông khí tắc nghẽn. RV tăng vì khí bị bẫy lại sau thở ra. Nhánh thở ra lõm vì "
        "lưu lượng tụt nhanh khi các đường thở nhỏ bị hẹp đóng sớm.",
        "B6.06, B6.07", ["Can-lam-sang", "CNHH"],
    ),

    # ------------------------------------------------------------ B7. Phân loại cơn ≤ 5 tuổi
    basic(
        "PED23-B7-01", "B7", "Phân loại cơn hen cấp ≤ 5 tuổi", 1,
        f"{B('[Phân loại cơn hen cấp trẻ ≤ 5 tuổi]')} Cơn được xếp {R('nặng hoặc đe dọa tính mạng')} khi có bao nhiêu dấu hiệu, gồm những dấu hiệu nào?",
        f"Chỉ cần {Y('một trong')} các dấu hiệu:<br>"
        f"1) Ý thức: {R('li bì hoặc u ám')}; {R('không uống hoặc nói được')}.<br>"
        f"2) Hô hấp: {R('rút lõm lồng ngực hoặc rút lõm khoang liên sườn')}.<br>"
        f"3) Bão hòa oxy: {Y('< 92%')}.<br>"
        f"4) Tím: {R('tím trung ương')}.<br>"
        f"5) Khò khè: {R('phổi câm')}.<br>"
        f"6) Mạch: {Y('> 200 lần/phút (0–3 tuổi)')} hoặc {Y('> 180 lần/phút (4–5 tuổi)')}.",
        "Trẻ nhỏ chỉ chia 2 mức (nhẹ/trung bình và nặng/đe dọa) để dễ ra quyết định: có một dấu hiệu nặng là phải xử trí như cơn "
        "nặng. 'Phổi câm' là dấu hiệu nguy hiểm nhất: không còn nghe khò khè vì luồng khí quá ít, không phải vì đã đỡ.",
        "B7.01, B7.02, B7.03, B7.04, B7.05, B7.06", ["Phan-do", "Duoi-5-tuoi"],
    ),
    basic(
        "PED23-B7-02", "B7", "Phân loại cơn hen cấp ≤ 5 tuổi", 2,
        f"{B('[Phân loại cơn hen cấp trẻ ≤ 5 tuổi]')} Cơn {G('nhẹ hoặc trung bình')} có biểu hiện gì ở 6 dấu hiệu: ý thức, hô hấp, bão hòa oxy, tím, khò khè, mạch?",
        f"1) Ý thức: {G('tỉnh hoặc kích thích')}.<br>"
        f"2) Hô hấp: {R('khó thở')}.<br>"
        f"3) Bão hòa oxy: {Y('≥ 92%')}.<br>"
        f"4) Tím: {Y('không')}.<br>"
        f"5) Khò khè: {R('thay đổi')}.<br>"
        f"6) Mạch: {Y('≤ 200 lần/phút (0–3 tuổi)')} hoặc {Y('≤ 180 lần/phút (4–5 tuổi)')}.",
        "Mỗi dòng là mặt trái của dấu hiệu nặng tương ứng. Cách nhớ: trẻ còn tỉnh, còn uống được, SpO₂ ≥ 92%, không tím → "
        "điều trị ban đầu ngoại trú được; mất bất kỳ điều nào → chuyển sang nhánh cơn nặng.",
        "B7.01, B7.02, B7.03, B7.04, B7.05, B7.06", ["Phan-do", "Duoi-5-tuoi"],
    ),
    cloze(
        "PED23-B7-03", "B7", "Phân loại cơn hen cấp ≤ 5 tuổi",
        f"Trẻ ≤ 5 tuổi: bão hòa oxy dưới {{{{c1::{Y('92%')}}}}} là dấu hiệu cơn hen nặng hoặc đe dọa tính mạng.",
        "B7.03", ["SpO2"],
    ),
    cloze(
        "PED23-B7-04", "B7", "Phân loại cơn hen cấp ≤ 5 tuổi",
        f"Trẻ ≤ 5 tuổi: cơn hen nặng khi mạch > {{{{c1::{Y('200')}}}}} lần/phút ở trẻ 0–3 tuổi hoặc > {{{{c2::{Y('180')}}}}} lần/phút ở trẻ 4–5 tuổi.",
        "B7.06", ["Mach"],
    ),

    # ------------------------------------------------------------ B8. Phân loại cơn > 5 tuổi
    basic(
        "PED23-B8-01", "B8", "Phân loại cơn hen cấp > 5 tuổi", 1,
        f"{B('[Phân loại cơn hen cấp trẻ > 5 tuổi]')} Chia thành {Y('mấy mức')}, và dựa trên {Y('những dấu hiệu')} nào?",
        f"1) {Y('4 mức')}: {G('nhẹ')}, {Y('trung bình')}, {R('nặng')}, {R('đe dọa tính mạng')}.<br>"
        f"2) {Y('9 dấu hiệu')}: ý thức, nói, tư thế, nhịp thở, khò khè, co kéo cơ hô hấp phụ, bão hòa oxy, mạch, PEF.",
        "Trẻ lớn nói được và đo được PEF nên phân độ chi tiết hơn trẻ nhỏ. Mẹo nhớ 9 dấu hiệu theo trình tự khám: nhìn (ý thức, "
        "nói, tư thế, nhịp thở, co kéo) → nghe (khò khè) → đo (SpO₂, mạch, PEF).",
        "B8.01, B8.02, B8.03, B8.04, B8.05, B8.06, B8.07, B8.08, B8.09", ["Phan-do", "Tren-5-tuoi", "Khung-bai"],
    ),
    basic(
        "PED23-B8-02", "B8", "Phân loại cơn hen cấp > 5 tuổi", 2,
        f"{B('[Cơn hen cấp NHẸ — trẻ > 5 tuổi]')} Mô tả 9 dấu hiệu: ý thức, nói, tư thế, nhịp thở, khò khè, co kéo cơ hô hấp phụ, bão hòa oxy, mạch, PEF.",
        f"1) Ý thức: {G('tỉnh')}.<br>2) Nói: {G('nói câu dài')}.<br>3) Tư thế: {G('có thể nằm được')}.<br>"
        f"4) Nhịp thở: {R('tăng')}.<br>5) Khò khè: {R('trung bình')}.<br>6) Co kéo cơ hô hấp phụ: {Y('không')}.<br>"
        f"7) Bão hòa oxy: {Y('> 95%')}.<br>8) Mạch: {Y('< 100 lần/phút')}.<br>9) PEF: {Y('> 50% giá trị dự đoán')}.",
        "Cơn nhẹ: trẻ vẫn sinh hoạt gần bình thường — nói cả câu, nằm được, không co kéo. SpO₂ > 95% là mốc riêng của cơn nhẹ.",
        "B8.01, B8.02, B8.03, B8.04, B8.05, B8.06, B8.07, B8.08, B8.09", ["Phan-do", "Tren-5-tuoi"],
    ),
    basic(
        "PED23-B8-03", "B8", "Phân loại cơn hen cấp > 5 tuổi", 2,
        f"{B('[Cơn hen cấp TRUNG BÌNH — trẻ > 5 tuổi]')} Mô tả 9 dấu hiệu: ý thức, nói, tư thế, nhịp thở, khò khè, co kéo cơ hô hấp phụ, bão hòa oxy, mạch, PEF.",
        f"1) Ý thức: {Y('tỉnh, ít kích thích')}.<br>2) Nói: {Y('nói câu ngắn')}.<br>3) Tư thế: {Y('thích tư thế ngồi hơn nằm')}.<br>"
        f"4) Nhịp thở: {R('tăng')}.<br>5) Khò khè: {R('nặng')}.<br>6) Co kéo cơ hô hấp phụ: {Y('không')}.<br>"
        f"7) Bão hòa oxy: {Y('90–95%')}.<br>8) Mạch: {Y('100–120 lần/phút')}.<br>9) PEF: {Y('> 50% giá trị dự đoán')}.",
        "Trung bình khác nhẹ ở chỗ trẻ bắt đầu hụt hơi khi nói (câu ngắn), muốn ngồi để thở dễ hơn, SpO₂ tụt về 90–95% và mạch "
        "tăng. PEF vẫn > 50% như cơn nhẹ, nên không dùng PEF để tách nhẹ với trung bình.",
        "B8.01, B8.02, B8.03, B8.04, B8.05, B8.06, B8.07, B8.08, B8.09", ["Phan-do", "Tren-5-tuoi"],
    ),
    basic(
        "PED23-B8-04", "B8", "Phân loại cơn hen cấp > 5 tuổi", 2,
        f"{B('[Cơn hen cấp NẶNG — trẻ > 5 tuổi]')} Mô tả 9 dấu hiệu: ý thức, nói, tư thế, nhịp thở, khò khè, co kéo cơ hô hấp phụ, bão hòa oxy, mạch, PEF.",
        f"1) Ý thức: {R('kích thích')}.<br>2) Nói: {R('nói từng cụm từ')}.<br>3) Tư thế: {R('ngồi gập mình về phía trước')}.<br>"
        f"4) Nhịp thở: {Y('> 30 lần/phút')}.<br>5) Khò khè: {R('nặng')}.<br>6) Co kéo cơ hô hấp phụ: {R('có')}.<br>"
        f"7) Bão hòa oxy: {Y('< 90%')}.<br>8) Mạch: {Y('> 120 lần/phút')}.<br>9) PEF: {Y('≤ 50% giá trị dự đoán')}.",
        "Tư thế ngồi gập người ra trước (tì tay) giúp cơ hô hấp phụ làm việc hiệu quả hơn — nhìn tư thế là đoán được cơn nặng. "
        "Co kéo cơ hô hấp phụ và PEF ≤ 50% là hai dấu hiệu chỉ có từ mức nặng.",
        "B8.01, B8.02, B8.03, B8.04, B8.05, B8.06, B8.07, B8.08, B8.09", ["Phan-do", "Tren-5-tuoi"],
    ),
    basic(
        "PED23-B8-05", "B8", "Phân loại cơn hen cấp > 5 tuổi", 2,
        f"{B('[Cơn hen ĐE DỌA TÍNH MẠNG — trẻ > 5 tuổi]')} Kể {Y('5 dấu hiệu')} ở các ô ý thức, nói, khò khè, cơ hô hấp và mạch.",
        f"1) Ý thức: {R('u ám, lẫn')}.<br>2) Nói: {R('không nói được')}.<br>3) Khò khè: {R('phổi câm')}.<br>"
        f"4) Cơ hô hấp: {R('di động ngực bụng bất thường')}.<br>5) Mạch: {R('mạch chậm')}.",
        "Đây là các dấu hiệu kiệt sức: cơ hô hấp mỏi nên khò khè 'giảm' (phổi câm), ngực–bụng di động nghịch thường, thiếu oxy "
        "não gây lẫn, và mạch đang nhanh chuyển sang chậm báo hiệu sắp ngừng tim–ngừng thở. Đừng nhầm 'bớt khò khè, mạch chậm "
        "lại' là trẻ đang đỡ.",
        "B8.01, B8.02, B8.05, B8.06, B8.08", ["Phan-do", "Tren-5-tuoi", "Co-do"],
    ),
    cloze(
        "PED23-B8-06", "B8", "Phân loại cơn hen cấp > 5 tuổi",
        f"Trẻ > 5 tuổi, bão hòa oxy theo mức cơn: cơn nhẹ {{{{c1::{Y('> 95%')}}}}}, cơn trung bình {{{{c1::{Y('90–95%')}}}}}, cơn nặng {{{{c1::{Y('< 90%')}}}}}.",
        "B8.07", ["SpO2"],
    ),
    cloze(
        "PED23-B8-07", "B8", "Phân loại cơn hen cấp > 5 tuổi",
        f"Trẻ > 5 tuổi, mạch theo mức cơn: cơn nhẹ {{{{c1::{Y('< 100')}}}}}, cơn trung bình {{{{c1::{Y('100–120')}}}}}, cơn nặng {{{{c1::{Y('> 120')}}}}} lần/phút.",
        "B8.08", ["Mach"],
    ),
    cloze(
        "PED23-B8-08", "B8", "Phân loại cơn hen cấp > 5 tuổi",
        f"Trẻ > 5 tuổi: cơn hen nặng có nhịp thở {{{{c1::{Y('> 30 lần/phút')}}}}} và PEF {{{{c2::{Y('≤ 50%')}}}}} giá trị dự đoán.",
        "B8.04, B8.09", ["Nhip-tho", "PEF"],
    ),

    # ------------------------------------------------------------ B9. Điều trị cơn nhẹ / trung bình
    basic(
        "PED23-B9-01", "B9", "Điều trị cơn hen nhẹ và trung bình", 1,
        f"{B('[Cơn hen nhẹ và trung bình]')} Thuốc cắt cơn ban đầu tại ngoại trú dùng thế nào cho từng mức, và {Y('đánh giá lại')} khi nào?",
        f"1) Cơn nhẹ: {G('khí dung salbutamol 2,5 mg/lần')}, hoặc {G('MDI salbutamol với buồng đệm')} {Y('2–4 nhát/lần')}, mỗi {Y('20 phút × 3 lần')} nếu cần.<br>"
        f"2) Cơn trung bình: {G('khí dung salbutamol 2,5 mg/lần')}, hoặc {G('MDI salbutamol với buồng đệm')} {Y('6–8 nhát/lần')}, mỗi {Y('20 phút × 3 lần')} nếu cần.<br>"
        f"3) Thời điểm đánh giá lại: sau {Y('mỗi lần khí dung/phun')}, và đánh giá tổng thể {Y('sau 1 giờ')}.",
        "Hai mức dùng cùng một thuốc (SABA), chỉ khác liều MDI: cơn trung bình cần gấp đôi–gấp ba số nhát. MDI có buồng đệm "
        "hiệu quả tương đương khí dung ở cơn nhẹ–trung bình. Ba liều cách nhau 20 phút trong giờ đầu là 'giờ vàng' để biết trẻ "
        "có đáp ứng hay không.",
        "B9.01, B9.02, B9.03", ["Dieu-tri", "Con-nhe-TB"],
    ),
    basic(
        "PED23-B9-02", "B9", "Điều trị cơn hen nhẹ và trung bình", 2,
        f"{B('[Cơn hen nhẹ/TB — sau 1 giờ]')} {G('Đáp ứng tốt')}: tiêu chí là gì và xử trí thế nào?",
        f"1) Tiêu chí: {G('hết khò khè')}, {G('không khó thở')}, {Y('SaO₂ ≥ 95%')}.<br>"
        f"2) Xử trí: {G('điều trị ngoại trú')} — tiếp tục {G('MDI salbutamol mỗi 3–4 giờ')} trong {Y('24–48 giờ')}; hẹn tái khám.",
        "Trẻ đáp ứng tốt vẫn cần duy trì SABA thêm 1–2 ngày vì viêm đường thở còn, cơn dễ tái nếu ngừng ngay. Hẹn tái khám để "
        "xem lại kiểm soát hen và nhu cầu điều trị dự phòng.",
        "B9.04", ["Dieu-tri", "Dap-ung"], asks=["Tiêu chí", "Xử trí"],
    ),
    basic(
        "PED23-B9-03", "B9", "Điều trị cơn hen nhẹ và trung bình", 2,
        f"{B('[Cơn hen nhẹ/TB — sau 1 giờ]')} {Y('Đáp ứng không hoàn toàn')}: tiêu chí là gì và xử trí thế nào?",
        f"1) Tiêu chí: {R('còn ran rít')}, {R('còn khó thở')}, {Y('SaO₂ 92–95%')}.<br>"
        f"2) Xử trí: {G('xem xét chỉ định nhập viện')}; {G('khí dung salbutamol 2,5 mg/lần + khí dung ipratropium 250 mcg/lần')}; "
        f"{G('prednisone uống sớm')} (khi không đáp ứng với 1 lần khí dung salbutamol).",
        "Thêm ipratropium (kháng cholinergic) hiệp đồng với salbutamol khi một mình SABA chưa đủ. Corticoid uống cho sớm vì cần "
        "vài giờ mới có tác dụng chống viêm — chờ thất bại hẳn mới cho là đã muộn.",
        "B9.05", ["Dieu-tri", "Dap-ung"], asks=["Tiêu chí", "Xử trí"],
    ),
    basic(
        "PED23-B9-04", "B9", "Điều trị cơn hen nhẹ và trung bình", 2,
        f"{B('[Cơn hen nhẹ/TB — sau 1 giờ]')} {R('Không đáp ứng')}: tiêu chí là gì và xử trí thế nào?",
        f"1) Tiêu chí: {R('còn ran rít, khó thở, rút lõm ngực')}; {Y('SaO₂ < 92%')}.<br>"
        f"2) Xử trí: {R('nhập viện')}; {G('khí dung salbutamol 2,5 mg/lần và ipratropium 250 mcg/lần')}; {G('prednisolone uống')}.",
        "SaO₂ < 92% và rút lõm ngực chính là tiêu chuẩn cơn nặng — tức là cơn đã tiến triển thành nặng dù ban đầu nhẹ/TB. "
        "Lúc này bắt buộc nhập viện, không còn lựa chọn ngoại trú.",
        "B9.06", ["Dieu-tri", "Dap-ung"], asks=["Tiêu chí", "Xử trí"],
    ),
    cloze(
        "PED23-B9-05", "B9", "Điều trị cơn hen nhẹ và trung bình",
        f"MDI salbutamol với buồng đệm (mỗi 20 phút × 3 lần nếu cần): cơn nhẹ {{{{c1::{Y('2–4 nhát/lần')}}}}}; cơn trung bình {{{{c2::{Y('6–8 nhát/lần')}}}}}.",
        "B9.01, B9.02", ["Lieu", "MDI"],
    ),
    cloze(
        "PED23-B9-06", "B9", "Điều trị cơn hen nhẹ và trung bình",
        f"Liều khí dung trong phác đồ cơn hen: salbutamol {{{{c1::{Y('2,5 mg/lần')}}}}} phối hợp ipratropium {{{{c2::{Y('250 mcg/lần')}}}}}.",
        "B9.05, B9.06", ["Lieu", "Ipratropium"],
    ),
    algo(
        "PED23-B9-07", "B9", "Lưu đồ cơn nhẹ/TB",
        "Cơn hen nhẹ/trung bình: sau 1 giờ điều trị đi nhánh nào?",
        f"1) Đáp ứng tốt — hết khò khè, không khó thở, {Y('SaO₂ ≥ 95%')} → {G('ngoại trú')}: MDI salbutamol mỗi 3–4 giờ × 24–48 giờ, hẹn tái khám.<br>"
        f"2) Đáp ứng không hoàn toàn — còn ran rít, còn khó thở, {Y('SaO₂ 92–95%')} → {Y('xem xét nhập viện')}: KD salbutamol 2,5 mg + ipratropium 250 mcg; prednisone uống sớm.<br>"
        f"3) Không đáp ứng — còn ran rít, khó thở, rút lõm ngực, {Y('SaO₂ < 92%')} → {R('nhập viện')}: KD salbutamol 2,5 mg + ipratropium 250 mcg; prednisolone uống.",
        "Quyết định xoay quanh SaO₂ với hai mốc 95% và 92%: ≥ 95% về nhà, 92–95% cân nhắc nhập viện, < 92% bắt buộc nhập viện. "
        "Nhánh 2 và 3 có cùng bộ thuốc (thêm ipratropium + corticoid uống); khác nhau ở mức độ bắt buộc nhập viện.",
        "B9.03, B9.04, B9.05, B9.06", ["Luu-do"],
    ),

    # ------------------------------------------------------------ B10. Điều trị cơn nặng / dọa ngừng thở
    basic(
        "PED23-B10-01", "B10", "Điều trị cơn hen nặng và dọa ngừng thở", 1,
        f"{B('[Cơn hen NẶNG nhập cấp cứu]')} Kể {Y('3 biện pháp')} điều trị ban đầu.",
        f"1) {G('Oxy qua mặt nạ')}.<br>"
        f"2) {G('Khí dung salbutamol 2,5 mg/lần + khí dung ipratropium')}, mỗi {Y('20 phút × 3 lần')} (đánh giá lại sau mỗi lần phun).<br>"
        f"3) {G('Hydrocortisone hoặc methylprednisolone tĩnh mạch')}.",
        "Ba trụ cột: oxy chống thiếu oxy, giãn phế quản kép (SABA + kháng cholinergic) mở đường thở nhanh, corticoid toàn thân "
        "chống viêm. Ở cơn nặng dùng corticoid đường tĩnh mạch thay vì uống vì trẻ khó thở, có thể không uống được.",
        "B10.01", ["Dieu-tri", "Con-nang"],
    ),
    basic(
        "PED23-B10-02", "B10", "Điều trị cơn hen nặng và dọa ngừng thở", 2,
        f"{B('[Cơn hen DỌA NGỪNG THỞ nhập cấp cứu]')} Kể {Y('4 biện pháp')} điều trị ban đầu, và thuốc nào {R('chỉ có ở mức này')} so với cơn nặng?",
        f"1) {G('Oxy qua mặt nạ')}.<br>"
        f"2) {R('Adrenaline tiêm dưới da (TDD)')} mỗi {Y('20 phút × 3 lần')} — thuốc chỉ có ở mức dọa ngừng thở.<br>"
        f"3) {G('Khí dung salbutamol')} {Y('2,5–5 mg/lần')} + {G('ipratropium')}, mỗi {Y('20 phút × 3 lần')} (đánh giá lại sau mỗi lần phun).<br>"
        f"4) {G('Hydrocortisone hoặc methylprednisolone tĩnh mạch')}.",
        "Khi trẻ sắp ngừng thở, luồng khí quá yếu nên thuốc khí dung khó vào sâu; adrenaline tiêm dưới da đi đường toàn thân, "
        "giãn phế quản không phụ thuộc thông khí. Liều salbutamol cũng được nâng lên tới 5 mg/lần.",
        "B10.02", ["Dieu-tri", "Doa-ngung-tho"],
    ),
    basic(
        "PED23-B10-03", "B10", "Điều trị cơn hen nặng và dọa ngừng thở", 2,
        f"{B('[Cơn nặng/dọa ngừng thở — đánh giá sau 1 giờ]')} Khi {G('đáp ứng tốt')}: tiếp tục thuốc gì trong 24 giờ, và khi nào chuyển ngoại trú với đơn gì?",
        f"1) Tiếp tục: {G('khí dung salbutamol ± ipratropium mỗi 4–6 giờ')} trong {Y('24 giờ')}; {G('hydrocortisone hoặc methylprednisolone TM')}.<br>"
        f"2) Chuyển ngoại trú khi {G('không khó thở')}, {Y('SaO₂ ≥ 95%')}.<br>"
        f"3) Đơn ngoại trú: {G('MDI salbutamol mỗi 3–4 giờ')} trong {Y('24–48 giờ')}; {G('prednisolone uống × 3 ngày')}; hẹn tái khám.",
        "Dù đáp ứng tốt sau 1 giờ, trẻ cơn nặng vẫn phải nằm viện theo dõi ít nhất 24 giờ với khí dung giãn dần (4–6 giờ/lần). "
        "Khi ra viện chuyển corticoid TM sang prednisolone uống 3 ngày để không bị tái cơn.",
        "B10.03, B10.04, B10.05", ["Dieu-tri", "Con-nang"],
    ),
    basic(
        "PED23-B10-04", "B10", "Điều trị cơn hen nặng và dọa ngừng thở", 2,
        f"{B('[Cơn nặng/dọa ngừng thở — đáp ứng không hoàn toàn/xấu]')} Chuyển đi đâu và kể {Y('5 biện pháp')} điều trị tiếp theo.",
        f"Chuyển {R('hồi sức')}:<br>"
        f"1) {G('Khí dung salbutamol mỗi giờ')} + {G('khí dung ipratropium mỗi 2–4 giờ')}.<br>"
        f"2) {G('Hydrocortisone / methylprednisolone TM')}.<br>"
        f"3) {G('Truyền tĩnh mạch magnesium sulfate')}.<br>"
        f"4) {G('Truyền tĩnh mạch aminophyllin')} ({Y('< 1 tuổi')}).<br>"
        f"5) {G('Truyền tĩnh mạch salbutamol')}; {R('đặt nội khí quản, thở máy')}.",
        "Thứ tự leo thang: tăng tần suất khí dung → thêm thuốc giãn phế quản đường tĩnh mạch (MgSO₄ làm giãn cơ trơn, "
        "aminophyllin, salbutamol TTM) → hỗ trợ hô hấp xâm nhập khi trẻ kiệt sức. Đặt NKQ là biện pháp cuối vì thở máy ở bệnh "
        "nhân hen dễ gây bẫy khí, tràn khí màng phổi.",
        "B10.06", ["Dieu-tri", "Hoi-suc"],
    ),
    cloze(
        "PED23-B10-05", "B10", "Điều trị cơn hen nặng và dọa ngừng thở",
        f"Cơn hen dọa ngừng thở: khí dung salbutamol {{{{c1::{Y('2,5–5 mg/lần')}}}}}, kèm adrenaline tiêm dưới da mỗi {{{{c2::{Y('20 phút × 3 lần')}}}}}.",
        "B10.02", ["Lieu", "Doa-ngung-tho"],
    ),
    cloze(
        "PED23-B10-06", "B10", "Điều trị cơn hen nặng và dọa ngừng thở",
        f"Ra viện sau cơn hen nặng đáp ứng tốt: prednisolone uống × {{{{c1::{Y('3 ngày')}}}}}.",
        "B10.05", ["Corticoid"],
    ),
    algo(
        "PED23-B10-07", "B10", "Lưu đồ cơn nặng/dọa ngừng thở",
        "Cơn hen nặng/dọa ngừng thở: sau 1 giờ điều trị đi nhánh nào?",
        f"1) Khởi đầu (giờ đầu): oxy mặt nạ + khí dung salbutamol/ipratropium mỗi 20 phút × 3 lần + corticoid TM; thêm {R('adrenaline TDD')} nếu dọa ngừng thở.<br>"
        f"2) Đáp ứng tốt → {G('khí dung mỗi 4–6 giờ × 24 giờ + corticoid TM')} → khi {Y('không khó thở, SaO₂ ≥ 95%')} → ngoại trú: MDI salbutamol mỗi 3–4 giờ × 24–48 giờ, prednisolone uống × 3 ngày, tái khám.<br>"
        f"3) Đáp ứng không hoàn toàn/xấu → {R('hồi sức')}: khí dung salbutamol mỗi giờ + ipratropium mỗi 2–4 giờ, corticoid TM, MgSO₄ TTM, aminophyllin TTM, salbutamol TTM, đặt NKQ thở máy.",
        "Mốc quyết định vẫn là đánh giá sau 1 giờ. Nhánh tốt giãn dần khí dung rồi chuyển đường uống; nhánh xấu leo thang lên "
        "thuốc tĩnh mạch rồi thở máy.",
        "B10.01, B10.02, B10.03, B10.04, B10.05, B10.06", ["Luu-do"],
    ),
    algo(
        "PED23-B10-08", "B10", "Bảng liều thuốc bỏ túi",
        "Bảng liều thuốc cắt cơn hen có trong phác đồ",
        f"1) Salbutamol khí dung: {Y('2,5 mg/lần')} (cơn nhẹ, TB, nặng); {Y('2,5–5 mg/lần')} (dọa ngừng thở); mỗi 20 phút × 3 lần trong giờ đầu.<br>"
        f"2) Salbutamol MDI + buồng đệm: {Y('2–4 nhát')} (nhẹ), {Y('6–8 nhát')} (TB) mỗi 20 phút × 3 lần; duy trì mỗi 3–4 giờ × 24–48 giờ.<br>"
        f"3) Ipratropium khí dung: {Y('250 mcg/lần')}; mỗi 20 phút × 3 lần (giờ đầu cơn nặng), mỗi 2–4 giờ ở hồi sức.<br>"
        f"4) Adrenaline: {G('tiêm dưới da')} mỗi {Y('20 phút × 3 lần')} — chỉ cơn dọa ngừng thở.<br>"
        f"5) Corticoid: {G('hydrocortisone/methylprednisolone TM')} (cơn nặng); {G('prednisolone uống')} (ngoại trú × 3 ngày sau cơn nặng).",
        "Slide chỉ ghi liều cố định cho salbutamol và ipratropium; liều theo cân nặng của corticoid, adrenaline, MgSO₄, "
        "aminophyllin không có trong slide — cần tra phác đồ của khoa trước khi kê.",
        "B9.01, B9.02, B9.05, B10.01, B10.02, B10.05", ["Lieu"],
    ),
    algo(
        "PED23-B8-09", "B8", "Phân độ nhanh tại giường",
        "Phân độ nhanh cơn hen cấp tại giường theo tuổi",
        f"1) Trẻ ≤ 5 tuổi — chỉ 2 mức: có {Y('một')} dấu hiệu sau là {R('nặng/đe dọa tính mạng')}: li bì/u ám, không uống/nói được, rút lõm ngực, {Y('SpO₂ < 92%')}, tím trung ương, phổi câm, mạch {Y('> 200 (0–3 tuổi) / > 180 (4–5 tuổi)')}.<br>"
        f"2) Trẻ > 5 tuổi — 4 mức theo SpO₂: {Y('> 95%')} nhẹ, {Y('90–95%')} trung bình, {Y('< 90%')} nặng.<br>"
        f"3) Trẻ > 5 tuổi — mạch: {Y('< 100')} nhẹ, {Y('100–120')} trung bình, {Y('> 120')} nặng, {R('mạch chậm')} = đe dọa tính mạng.<br>"
        f"4) Đe dọa tính mạng (> 5 tuổi): {R('u ám/lẫn, không nói được, phổi câm, di động ngực bụng bất thường, mạch chậm')}.",
        "Bẫy: ngưỡng SpO₂ khác nhau theo tuổi — trẻ nhỏ lấy 92%, trẻ lớn lấy 90% cho cơn nặng. Dấu hiệu đe dọa tính mạng "
        "đều là dấu hiệu kiệt sức, có thể bị hiểu nhầm là 'đỡ khò khè'.",
        "B7.03, B7.06, B8.07, B8.08", ["Phan-do"],
    ),

    # ------------------------------------------------------------ B11. Nguyên tắc điều trị
    basic(
        "PED23-B11-01", "B11", "Nguyên tắc điều trị HPQ", 1,
        f"{B('[Nguyên tắc điều trị HPQ trẻ em]')} Nêu {Y('3 nguyên tắc')} điều trị theo slide.",
        f"1) Dùng {G('SABA')} làm giãn phế quản cho {Y('tất cả')} các trẻ có triệu chứng hen.<br>"
        f"2) Trẻ nhỏ: khởi đầu phòng bệnh bằng {G('ICS liều thấp')} hoặc {G('montelukast')}.<br>"
        f"3) Hầu hết trẻ nhỏ HPQ {Y('thể nhẹ')} → khuyến cáo dùng {G('SABA')}, {R('không nên dùng thuốc phòng hen kéo dài')}.",
        "SABA (salbutamol) là thuốc cắt cơn cho mọi trẻ. Thuốc phòng bệnh (ICS, montelukast) chỉ khi cần, và ở trẻ nhỏ thể nhẹ "
        "thì không nên dùng kéo dài vì nhiều trẻ khò khè sẽ tự hết khi lớn, còn ICS lâu dài có thể ảnh hưởng tăng trưởng.",
        "B11.01, B11.02, B11.03", ["Dieu-tri", "Nguyen-tac"],
    ),

    # ------------------------------------------------------------ B12. Thuốc phòng bệnh & phối hợp
    basic(
        "PED23-B12-01", "B12", "Thuốc phòng bệnh", 2,
        f"{B('[Thuốc phòng bệnh hen]')} Kể {Y('3 nhóm')} thuốc phòng bệnh.",
        f"1) {G('ICS')} (corticoid dạng hít).<br>"
        f"2) {G('Thuốc kháng thụ thể leukotriene (LTRAs)')} — ví dụ montelukast.<br>"
        f"3) {G('Cromones')}: {G('cromoglycate')} và {G('nedocromil')}.",
        "Cả 3 nhóm đều nhắm vào viêm đường thở, không cắt cơn. ICS mạnh nhất và là nền tảng; LTRA dạng uống nên dễ dùng ở trẻ "
        "nhỏ; cromones ổn định tế bào mast, an toàn nhưng tác dụng yếu nên hiện ít dùng.",
        "B12.01", ["Thuoc", "Du-phong"],
    ),
    basic(
        "PED23-B12-02", "B12", "Thuốc phối hợp", 2,
        f"{B('[Thuốc điều trị phối hợp]')} Kể {Y('2 cặp')} thuốc phối hợp và tên biệt dược tương ứng.",
        f"1) {G('Fluticasone + salmeterol')} — {B('Seretide')}.<br>"
        f"2) {G('Budesonide + eformoterol (formoterol)')} — {B('Symbicort')}.",
        "Cả hai đều là ICS + LABA (giãn phế quản tác dụng kéo dài) trong một bình hít: ICS chống viêm, LABA giữ phế quản giãn "
        "suốt 12 giờ. Mẹo nhớ: Seretide = Salmeterol + fluticasone; Symbicort = budesonide + formoterol.",
        "B12.02", ["Thuoc", "Phoi-hop"],
    ),

    # ------------------------------------------------------------ B13. Mức độ kiểm soát
    basic(
        "PED23-B13-01", "B13", "Mức độ kiểm soát hen", 1,
        f"{B('[Mức độ kiểm soát hen]')} Đánh giá trong khoảng {Y('thời gian')} nào, chia {Y('mấy mức')}, và dựa trên {Y('6 đặc tính')} nào?",
        f"1) Thời gian: {Y('4 tuần qua')}.<br>"
        f"2) 3 mức: {G('kiểm soát')}, {Y('kiểm soát một phần')}, {R('chưa kiểm soát')}.<br>"
        f"3) 6 đặc tính: triệu chứng ban ngày; hạn chế hoạt động; triệu chứng ban đêm/thức giấc; nhu cầu dùng thuốc cắt cơn; "
        f"chức năng phổi (PEF hoặc FEV1); đợt kịch phát.",
        "Mức kiểm soát quyết định có cần tăng bậc thuốc dự phòng hay không. 4 đặc tính đầu là triệu chứng hằng ngày, 2 đặc tính "
        "sau là khách quan (chức năng phổi) và nguy cơ (đợt kịch phát).",
        "B13.01, B13.02, B13.03, B13.04, B13.05, B13.06", ["Kiem-soat", "Khung-bai"],
    ),
    basic(
        "PED23-B13-02", "B13", "Mức độ kiểm soát hen", 2,
        f"{B('[Hen KIỂM SOÁT — cần đủ tất cả]')} Mô tả 6 đặc tính: triệu chứng ban ngày, hạn chế hoạt động, triệu chứng ban đêm, nhu cầu thuốc cắt cơn, chức năng phổi, đợt kịch phát.",
        f"1) Triệu chứng ban ngày: {G('không')} ({Y('≤ 2 lần/tuần')}).<br>"
        f"2) Hạn chế hoạt động: {G('không')}.<br>"
        f"3) Triệu chứng ban đêm/thức giấc: {G('không')}.<br>"
        f"4) Nhu cầu thuốc cắt cơn: {G('không')} ({Y('≤ 2 lần/tuần')}).<br>"
        f"5) Chức năng phổi (PEF/FEV1): {G('bình thường')}.<br>"
        f"6) Đợt kịch phát: {G('không')}.",
        "Chú ý: 'không' triệu chứng ban ngày và 'không' dùng thuốc cắt cơn vẫn cho phép tối đa 2 lần/tuần. Riêng triệu chứng "
        "đêm và hạn chế hoạt động thì phải hoàn toàn không có.",
        "B13.01, B13.02, B13.03, B13.04, B13.05, B13.06", ["Kiem-soat"], asks=KS_ASKS,
    ),
    basic(
        "PED23-B13-03", "B13", "Mức độ kiểm soát hen", 2,
        f"{B('[Hen KIỂM SOÁT MỘT PHẦN — đặc tính bất kỳ/tuần bất kỳ]')} Mô tả ngưỡng của 6 đặc tính: triệu chứng ban ngày, hạn chế hoạt động, triệu chứng ban đêm, nhu cầu thuốc cắt cơn, chức năng phổi, đợt kịch phát.",
        f"1) Triệu chứng ban ngày: {Y('> 2 lần/tuần')}.<br>"
        f"2) Hạn chế hoạt động: {R('bất kỳ')}.<br>"
        f"3) Triệu chứng ban đêm/thức giấc: {R('bất kỳ')}.<br>"
        f"4) Nhu cầu thuốc cắt cơn: {Y('> 2 lần/tuần')}.<br>"
        f"5) Chức năng phổi (PEF/FEV1): {Y('< 80%')} ước tính hoặc lúc tốt nhất trong bất kỳ ngày nào.<br>"
        f"6) Đợt kịch phát: {Y('> 1 lần/năm')}.",
        "Chỉ cần một đặc tính rơi vào cột này trong bất kỳ tuần nào là đã mất mức 'kiểm soát'. Hạn chế hoạt động và triệu chứng "
        "đêm chỉ cần xuất hiện một lần là tính.",
        "B13.01, B13.02, B13.03, B13.04, B13.05, B13.06", ["Kiem-soat"], asks=KS_ASKS,
    ),
    basic(
        "PED23-B13-04", "B13", "Mức độ kiểm soát hen", 2,
        f"{B('[Hen CHƯA KIỂM SOÁT]')} Định nghĩa thế nào, và ngưỡng {R('đợt kịch phát')} ở mức này là gì?",
        f"1) Có {Y('≥ 3 yếu tố')} của kiểm soát một phần {Y('trong một tuần bất kỳ')}.<br>"
        f"2) Đợt kịch phát: xảy ra {R('trong 1 tuần bất kỳ')}.",
        "Chưa kiểm soát không cần đếm từng đặc tính như hai cột kia: chỉ cần gom ≥ 3 yếu tố của mức một phần trong cùng một tuần. "
        "Một đợt kịch phát trong tuần đó cũng xếp tuần đó vào chưa kiểm soát.",
        "B13.06, B13.07", ["Kiem-soat"],
    ),
    cloze(
        "PED23-B13-05", "B13", "Mức độ kiểm soát hen",
        f"Hen chưa kiểm soát: có {{{{c1::{Y('≥ 3 yếu tố')}}}}} của kiểm soát một phần trong một tuần bất kỳ.",
        "B13.07", ["Kiem-soat"],
    ),
    cloze(
        "PED23-B13-06", "B13", "Mức độ kiểm soát hen",
        f"Mức độ kiểm soát hen được đánh giá trong vòng {{{{c1::{Y('4 tuần')}}}}} qua; hen kiểm soát cho phép triệu chứng ban ngày tối đa {{{{c2::{Y('2 lần/tuần')}}}}}.",
        "B13.01", ["Kiem-soat"],
    ),
    algo(
        "PED23-B13-07", "B13", "Đánh giá kiểm soát nhanh",
        "Xếp mức kiểm soát hen trong 4 tuần qua",
        f"1) Tất cả 6 đặc tính đều 'không'/bình thường (ban ngày và thuốc cắt cơn {Y('≤ 2 lần/tuần')}) → {G('kiểm soát')}.<br>"
        f"2) Có {Y('1–2 yếu tố')} của cột một phần (ban ngày hoặc thuốc cắt cơn {Y('> 2 lần/tuần')}, bất kỳ hạn chế hoạt động hay triệu chứng đêm, PEF/FEV1 {Y('< 80%')}, kịch phát {Y('> 1 lần/năm')}) → {Y('kiểm soát một phần')}.<br>"
        f"3) {Y('≥ 3 yếu tố')} trong một tuần bất kỳ, hoặc có đợt kịch phát trong tuần → {R('chưa kiểm soát')}.",
        "Cách đếm 1–2 vs ≥ 3 yếu tố là hệ quả trực tiếp của định nghĩa trong bảng: chưa kiểm soát cần ≥ 3 yếu tố, nên 1–2 yếu tố "
        "là một phần.",
        "B13.02, B13.03, B13.04, B13.05, B13.06, B13.07", ["Kiem-soat"],
    ),
]
