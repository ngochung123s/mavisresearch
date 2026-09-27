# -*- coding: utf-8 -*-
"""
build_ped24_master_deck.py
Tạo bộ thẻ Anki Master hoàn chỉnh từ đầu cho bài PED-24: Croup (Viêm thanh khí phế quản cấp ở trẻ em).
Tuân thủ tuyệt đối Quy chuẩn Thép APKG (Full-Coverage & Exhaustive Depth Governance):
- Độ phủ 100% tiểu mục, không bỏ sót bất kỳ phần nào của bài giảng.
- Đầy đủ 6 tầng kiến thức: Định nghĩa, Cơ chế Why-based, Con số định lượng, Lưu đồ nâng bậc, Cạm bẫy cấm kỵ, Tình huống tại giường.
- Thẻ nguyên tử (Atomic): 1 thẻ = 1 thông tin duy nhất, mặt sau 3-4 dòng đọc xong trong 3-5 giây.
- Unicode 100%, không lỗi font, tương thích hoàn hảo Anki Desktop và Anki Mobile.
"""
import os
import json
import re
import genanki
from pathlib import Path

BASE_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\03_Ho_hap\PED-24_Croup_Viem_thanh_khi_phe_quan_cap")
OUTPUT_APKG = BASE_DIR / "PED-24_Croup_Viem_thanh_khi_phe_quan_cap_2026-09-17_RELEASE_v1.apkg"
OUTPUT_JSON = BASE_DIR / "PED-24_Croup_Viem_thanh_khi_phe_quan_cap_2026-09-17_RELEASE_v1.cards.v2.json"

DECK_ID = 1789747310024
DECK_NAME = "Nhi khoa Y6::PED-24: Croup (Viêm thanh khí phế quản cấp)"

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', -apple-system, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #0b1120;
  padding: 20px;
  max-width: 680px;
  margin: 0 auto;
}
.badge {
  display: inline-block;
  padding: 3px 9px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.badge-basic {
  background-color: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.35);
}
.badge-cloze {
  background-color: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.35);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 12px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.04);
  border-radius: 8px;
  padding: 12px 14px;
  border-left: 3px solid #38bdf8;
  margin-top: 10px;
  font-size: 14.5px;
}
.cloze {
  font-weight: 700;
  color: #38bdf8;
  border-bottom: 2px solid #0284c7;
  padding: 0 3px;
}
.extra-box {
  margin-top: 12px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(30, 41, 59, 0.6);
  border: 1px dashed rgba(148, 163, 184, 0.25);
  font-size: 13px;
  color: #94a3b8;
}
"""

BASIC_MODEL_ID = 1789747320024
basic_model = genanki.Model(
    BASIC_MODEL_ID,
    'PED-24 Basic Model (Master Medical)',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Extra'},
        {'name': 'Category'}
    ],
    templates=[
        {
            'name': 'Medical Card',
            'qfmt': '''
<div class="card">
  <div class="badge badge-basic">{{Category}}</div>
  <div class="question">{{Front}}</div>
</div>
''',
            'afmt': '''
<div class="card">
  <div class="badge badge-basic">{{Category}}</div>
  <div class="question">{{Front}}</div>
  <div class="answer-box">
    {{Back}}
  </div>
  {{#Extra}}
  <div class="extra-box">
    <b>🔍 Chi tiết mở rộng:</b><br>{{Extra}}
  </div>
  {{/Extra}}
</div>
'''
        }
    ],
    css=CSS_STYLE
)

CLOZE_MODEL_ID = 1789747330024
cloze_model = genanki.Model(
    CLOZE_MODEL_ID,
    'PED-24 Cloze Model (Master Medical)',
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
        {'name': 'Category'}
    ],
    templates=[
        {
            'name': 'Medical Cloze',
            'qfmt': '''
<div class="card">
  <div class="badge badge-cloze">{{Category}}</div>
  <div class="question">{{cloze:Text}}</div>
</div>
''',
            'afmt': '''
<div class="card">
  <div class="badge badge-cloze">{{Category}}</div>
  <div class="question">{{cloze:Text}}</div>
  {{#Extra}}
  <div class="extra-box">
    <b>🔍 Bản chất cơ chế & Lưu ý:</b><br>{{Extra}}
  </div>
  {{/Extra}}
</div>
'''
        }
    ],
    css=CSS_STYLE,
    model_type=genanki.Model.CLOZE
)

def clean_html(text):
    if not text:
        return ""
    text = text.replace("<br&gt;", "<br>").replace("</br&gt;", "")
    text = re.sub(r'<(?=[0-9= ])', '&lt;', text)
    return text

CARDS_DATA = [
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Vị trí giải phẫu nào bị tổn thương viêm và phù nề chủ yếu trong bệnh cảnh Croup (Viêm thanh khí phế quản cấp)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vùng hạ thanh môn (Subglottic space), nằm ngay dưới hai dây thanh âm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Được bao bọc bởi vòng sụn nhẫn kín; đây là điểm hẹp nhất của đường thở ở trẻ em.",
        "extra": "Tình trạng phù nề niêm mạc tại vòng sụn nhẫn làm lòng ống thở hẹp vào trong, gây cản trở thông khí thì hít vào."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Lứa tuổi nào mắc Croup phổ biến nhất trong thực hành lâm sàng Nhi khoa?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Trẻ từ 6 tháng đến 36 tháng tuổi (đỉnh cao mắc bệnh từ 1 đến 2 tuổi).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Lứa tuổi này đường thở có khẩu kính rất nhỏ và lượng kháng thể thụ động từ mẹ đã cạn kiệt.",
        "extra": "Trẻ &lt; 6 tháng hiếm gặp hơn nhờ kháng thể mẹ, trẻ &gt; 3-6 tuổi đường thở đã phát triển lớn hơn."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Tại sao trẻ dưới 6 tháng tuổi lại ít mắc bệnh Croup hơn so với lứa tuổi 1 - 2 tuổi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nhờ lượng kháng thể IgG kháng virus Parainfluenza truyền thụ động từ mẹ qua nhau thai trong thai kỳ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Kháng thể này suy giảm dần và biến mất sau 6 tháng đầu đời, tạo nên 'khoảng trống miễn dịch'.",
        "extra": "Nếu trẻ &lt; 3-6 tháng có thở rít, cần cảnh giác thêm với các dị tật bẩm sinh như mềm sụn thanh quản."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Căn nguyên vi sinh học hàng đầu gây Viêm thanh khí phế quản cấp ở trẻ em là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Virus Á cúm người (Human Parainfluenza Virus - HPIV), chiếm 65% – 75% trường hợp.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trong đó HPIV type 1 là chủng phổ biến nhất gây dịch mùa thu đông.",
        "extra": "HPIV type 2 gây bệnh cảnh tương tự nhưng nhẹ hơn; HPIV type 3 thường kết hợp viêm tiểu phế quản và viêm phổi."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Các tác nhân virus khác ngoài HPIV có thể gây bệnh cảnh Croup bao gồm những loại nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Virus Cúm A và B (Influenza A/B), Virus hợp bào hô hấp (RSV), Adenovirus, Rhinovirus.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Croup do Cúm A thường có xu hướng diễn tiến lâm sàng nặng nề hơn HPIV.",
        "extra": "Hiếm gặp hơn có thể do Coronavirus, Metapneumovirus hoặc vi khuẩn Mycoplasma pneumoniae."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Thời điểm nào trong ngày các triệu chứng ho ông ổng và thở rít của Croup thường bùng phát nặng nề nhất?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ban đêm (đặc biệt từ nửa đêm đến gần sáng).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do nồng độ Cortisol nội sinh hạ xuống thấp nhất vào ban đêm kết hợp với nhiệt độ và độ ẩm không khí giảm.",
        "extra": "Ban ngày trẻ thường chỉ có triệu chứng viêm long hô hấp trên nhẹ, đêm đến mới đột ngột khó thở."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Croup co thắt (Spasmodic Croup) khác biệt với Croup do virus thông thường ở những điểm mấu chốt nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đột ngột nửa đêm, KHÔNG SỐT, không có tiền triệu viêm long, khỏi nhanh trong vài giờ và hay tái phát.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bản chất liên quan đến cơ địa dị ứng/tăng phản ứng đường thở hơn là nhiễm trùng trực tiếp.",
        "extra": "Xử trí Croup co thắt vẫn đáp ứng rất tốt với một liều Dexamethasone hoặc trấn an người nhà."
    },
    {
        "type": "basic",
        "category": "Định nghĩa & Dịch tễ",
        "front": "[PEDYTB - Ôn thi] Giai đoạn tiền triệu (Prodrome) của Croup do virus thường kéo dài bao lâu và có biểu hiện gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kéo dài 1 đến 3 ngày với biểu hiện: Sốt nhẹ, chảy nước mũi, đau họng và ho nhẹ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Virus nhân lên tại niêm mạc mũi hầu trước khi lan tỏa xuống thanh khí quản.",
        "extra": "Sau 1-3 ngày, triệu chứng ho chuyển dạng đột ngột sang ho ông ổng và xuất hiện thở rít."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Điểm hẹp nhất của đường dẫn khí ở trẻ em dưới 8 tuổi nằm ở đâu và khác người lớn thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ở trẻ em: Vùng hạ thanh môn (ngang mức sụn nhẫn).<br>• Ở người lớn: Khe thanh môn (giữa hai dây thanh âm).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tạo nên hình phễu đặc trưng của thanh quản trẻ nhỏ.",
        "extra": "Do sụn nhẫn là một vòng sụn khép kín hoàn toàn, mô liên kết lỏng lẻo bên trong khi phù nề không thể giãn nở ra ngoài."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Tại sao vòng sụn nhẫn (Cricoid ring) lại là cạm bẫy giải phẫu khiến phù nề hạ thanh môn trở nên nguy hiểm?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vì đây là vòng sụn duy nhất của đường thở KHÉP KÍN HOÀN TOÀN 360 độ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khi niêm mạc bị viêm phù nề, nó không thể giãn nở ra phía ngoài mà bắt buộc phải phồng chèn ép vào trong lòng ống.",
        "extra": "Lớp hạ niêm mạc vùng này có cấu trúc mô liên kết rất lỏng lẻo và giàu mạch máu, cực kỳ dễ tích tụ dịch viêm."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Theo định luật Poiseuille, kháng lực đường thở (R) phụ thuộc vào bán kính lòng ống (r) theo mối quan hệ nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kháng lực tỉ lệ nghịch với bán kính lũy thừa bậc 4 (R ∝ 1 / r⁴).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Một sự thu hẹp rất nhỏ của bán kính lòng ống sẽ làm kháng lực dòng khí tăng vọt theo cấp số nhân.",
        "extra": "Công thức dòng chảy tầng: ΔP = V̇ × (8ηL / πr⁴)."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Khi phù nề 1 mm ở niêm mạc hạ thanh môn, diện tích thiết diện và kháng lực đường thở ở trẻ nhũ nhi thay đổi thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Diện tích lòng ống giảm tới 75% và kháng lực tăng vọt gấp 16 lần!<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bán kính từ 2 mm giảm còn 1 mm (giảm một nửa): 1 / (1/2)⁴ = 16 lần.",
        "extra": "Ở người lớn (bán kính 4 mm), phù 1 mm chỉ làm giảm 44% diện tích và tăng kháng lực lên 3 lần."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Hiệu ứng Bernoulli (Bernoulli Effect) làm nặng thêm tình trạng tắc nghẽn thanh quản trong Croup như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Khi dòng khí tăng tốc qua chỗ hẹp hạ thanh môn, áp suất thành bên tụt giảm, hút sụp thành đường thở mềm vào trong.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ càng gắng sức hít mạnh thì lòng thanh quản càng bị bóp nghẹt thêm (Dynamic collapse).",
        "extra": "Đó là lý do tại sao khi trẻ quấy khóc, tình trạng khó thở và thở rít tăng lên dữ dội."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Tam chứng lâm sàng kinh điển của Viêm thanh khí phế quản cấp (Croup) gồm 3 triệu chứng nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1. Ho ông ổng (Barking cough).<br>2. Thở rít thanh quản thì hít vào (Inspiratory stridor).<br>3. Khàn tiếng (Hoarseness).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Xuất hiện sau 1-3 ngày có triệu chứng viêm long hô hấp trên.",
        "extra": "Tiếng ho của Croup được ví kinh điển như tiếng chó sủa hoặc tiếng hải cẩu kêu (seal-like bark)."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Cơ chế sinh lý bệnh tạo nên tiếng Ho ông ổng (Barking cough) đặc thù trong Croup là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dây thanh âm và hạ thanh môn phù nề làm luồng khí ho thoát qua một khe hẹp cứng nhắc, gây rung động âm thanh bất thường.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Vòng sụn nhẫn đóng vai trò như buồng cộng hưởng âm thanh khiến tiếng ho vang, khô và trầm đục.",
        "extra": "Khi trẻ ho, áp lực dương trong đường thở cố tống dị vật/đờm qua vùng hạ thanh môn đang bị chít hẹp."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Tại sao tiếng Thở rít (Stridor) trong Croup điển hình lại xuất hiện ở THÌ HÍT VÀO?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ở thì hít vào, áp lực âm trong lòng đường thở ngoài lồng ngực làm kéo sụp mô mềm hạ thanh môn vào trong, gây hẹp nặng hơn.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Dòng khí xoáy (turbulent flow) tốc độ cao va đập qua chỗ hẹp tạo nên âm thanh rít thô ráp.",
        "extra": "Ngược lại, ở thì thở ra áp lực dương đẩy lòng ống mở rộng ra một phần nên thở rít thì thở ra ít gặp trừ khi tắc nghẽn quá nặng."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Cơ chế nào giải thích triệu chứng Khàn tiếng (Hoarseness) ở trẻ Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Do quá trình viêm lan lên dây thanh âm làm dây thanh bị phù nề, dày lên và rung động không đều.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Hai dây thanh âm không thể khép kín hoàn toàn khi phát âm, tạo ra giọng nói thô ráp hoặc mất tiếng.",
        "extra": "Nếu khàn tiếng kèm theo khó thở thanh quản dữ dội, cần phân biệt với liệt dây thanh âm hoặc u nhú thanh quản."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Thở rít hai thì (Biphasic Stridor - cả hít vào và thở ra) ở trẻ Croup cảnh báo điều gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cảnh báo tắc nghẽn đường thở cố định và CỰC KỲ NẶNG NỀ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Lòng hạ thanh môn hẹp đến mức ngay cả áp lực dương thì thở ra cũng không thể mở thông được luồng khí.",
        "extra": "Đây là dấu hiệu cờ đỏ báo động suy hô hấp nguy kịch cần can thiệp khí dung Adrenaline và chuẩn bị đặt nội khí quản ngay."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Cơ chế tác dụng dược lý của Adrenaline khí dung giúp giải cứu đường thở trong Croup là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kích thích thụ thể Alpha-1 adrenergic gây co mạch máu mao mạch hạ niêm mạc, làm xẹp mô phù nề tức thì.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khởi phát tác dụng cực nhanh sau 10 - 30 phút, giúp nới rộng khẩu kính đường thở cấp cứu.",
        "extra": "Tác dụng của Adrenaline chỉ kéo dài tối đa khoảng 2 giờ, sau đó nguy cơ tái phát phù nề do hiện tượng dội ngược."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PEDYTB - Ôn thi] Cơ chế tác dụng dược lý của Dexamethasone trong điều trị Croup là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Gắn thụ thể Glucocorticoid nội bào, ức chế yếu tố phiên mã NF-κB, giảm tổng hợp cytokine và tính thấm thành mạch.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bắt đầu tác dụng sau 1 - 2 giờ, đạt đỉnh sau 4 - 6 giờ và duy trì kéo dài 36 - 72 giờ.",
        "extra": "Dexamethasone là thuốc nền tảng giúp ngăn chặn hiện tượng dội ngược sau khi Adrenaline hết tác dụng."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PEDYTB - Ôn thi] Thang điểm Westley (Westley Croup Score) đánh giá mức độ nặng của Croup dựa trên bao nhiêu tiêu chí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• 5 tiêu chí lâm sàng: Thở rít, Co kéo lồng ngực, Thông khí vào phổi, Tím tái và Tri giác.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tổng điểm dao động từ 0 đến 17 điểm.",
        "extra": "Là công cụ tiêu chuẩn vàng được các hướng dẫn quốc tế (AAP, NICE, BV Nhi Đồng) sử dụng để phân độ và chỉ định thuốc."
    },
    {
        "type": "cloze",
        "category": "Thang điểm Westley",
        "text": "[PEDYTB - Ôn thi] Tiêu chí 1 trong thang điểm Westley - Thở rít (Inspiratory Stridor): Không có = {{c1::0 điểm}}; Có khi kích thích/quấy khóc = {{c1::1 điểm}}; Có khi nằm yên tĩnh = {{c1::2 điểm}}.",
        "extra": "Thở rít khi nằm yên là ranh giới lâm sàng phân định từ thể Nhẹ sang thể Vừa."
    },
    {
        "type": "cloze",
        "category": "Thang điểm Westley",
        "text": "[PEDYTB - Ôn thi] Tiêu chí 2 trong thang điểm Westley - Co kéo lồng ngực (Chest wall retractions): Không có = {{c1::0 điểm}}; Nhẹ = {{c1::1 điểm}}; Vừa = {{c1::2 điểm}}; Nặng = {{c1::3 điểm}}.",
        "extra": "Co kéo nặng bao gồm rút lõm dưới sườn sâu, co kéo hõm trên ức và phập phồng cánh mũi."
    },
    {
        "type": "cloze",
        "category": "Thang điểm Westley",
        "text": "[PEDYTB - Ôn thi] Tiêu chí 3 trong thang điểm Westley - Thông khí vào phổi (Air entry): Bình thường = {{c1::0 điểm}}; Giảm nhẹ = {{c1::1 điểm}}; Giảm nặng = {{c1::2 điểm}}.",
        "extra": "Thông khí giảm nặng chứng tỏ luồng khí đi vào phế nang bị tắc nghẽn nghiêm trọng."
    },
    {
        "type": "cloze",
        "category": "Thang điểm Westley",
        "text": "[PEDYTB - Ôn thi] Tiêu chí 4 trong thang điểm Westley - Tím tái (Cyanosis): Không có = {{c1::0 điểm}}; Tím khi kích thích/quấy khóc = {{c1::4 điểm}}; Tím khi nằm yên tĩnh = {{c1::5 điểm}}.",
        "extra": "Tím tái được chấm điểm nhảy vọt (4-5 điểm) vì đây là dấu hiệu suy hô hấp giảm oxy máu đe dọa tính mạng."
    },
    {
        "type": "cloze",
        "category": "Thang điểm Westley",
        "text": "[PEDYTB - Ôn thi] Tiêu chí 5 trong thang điểm Westley - Tri giác (Level of consciousness): Bình thường = {{c1::0 điểm}}; Bứt rứt, lo âu hoặc li bì = {{c1::5 điểm}}.",
        "extra": "Rối loạn tri giác ở trẻ khó thở là biểu hiện của thiếu oxy máu não hoặc ứ trệ CO2 nghiêm trọng."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PEDYTB - Ôn thi] Croup thể Nhẹ (Mild Croup) tương ứng với bao nhiêu điểm Westley và có đặc điểm lâm sàng gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Điểm Westley: 0 đến 2 điểm.<br>• Lâm sàng: Ho ông ổng, khàn tiếng, KHÔNG CÓ thở rít khi nằm yên, co kéo nhẹ hoặc không.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ vẫn chơi ngoan, bú tốt và tỉnh táo.",
        "extra": "Thở rít chỉ xuất hiện thoáng qua khi trẻ khóc to hoặc quấy giãy."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PEDYTB - Ôn thi] Croup thể Vừa (Moderate Croup) tương ứng với bao nhiêu điểm Westley và có dấu hiệu bản lề nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Điểm Westley: 3 đến 5 điểm.<br>• Dấu hiệu bản lề: THỞ RÍT XUẤT HIỆN NGAY CẢ KHI NẰM YÊN TĨNH, kèm co kéo vừa.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Thông khí vào phổi vẫn còn tốt, trẻ tỉnh táo không kích thích.",
        "extra": "Sự xuất hiện của thở rít khi nằm yên là chỉ định bắt buộc phải cho trẻ nằm lưu theo dõi và dùng thuốc tích cực."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PEDYTB - Ôn thi] Croup thể Nặng (Severe Croup) tương ứng với bao nhiêu điểm Westley và biểu hiện như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Điểm Westley: 6 đến 11 điểm.<br>• Lâm sàng: Thở rít dữ dội khi nằm yên, co kéo ngực nặng, giảm thông khí, bứt rứt kích thích.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ lo âu, hoảng hốt do bắt đầu có tình trạng thiếu oxy mô.",
        "extra": "Bắt buộc cấp cứu bằng Adrenaline khí dung và Dexamethasone ngay lập tức."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PEDYTB - Ôn thi] Croup thể Dọa suy hô hấp (Impending Respiratory Failure) tương ứng với điểm Westley nào và có bẫy gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Điểm Westley: ≥ 12 điểm (12 - 17 điểm).<br>• Biểu hiện: Li bì, lơ mơ, tím tái, tiếng thở rít GIẢM DẦN do kiệt sức (Phổi câm), nhịp tim chậm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bẫy: Tiếng rít giảm không phải bệnh đỡ mà do luồng khí quá yếu không đủ tạo âm thanh.",
        "extra": "Cần hô hoán hỗ trợ, bóp bóng qua mask và chuẩn bị đặt nội khí quản cấp cứu ngay."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Viêm nắp thanh môn cấp (Epiglottitis) do vi khuẩn nào gây ra chủ yếu và thường gặp ở lứa tuổi nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vi khuẩn Haemophilus influenzae type b (HiB).<br>• Lứa tuổi: Trẻ lớn hơn (2 đến 7 tuổi), đặc biệt trẻ chưa tiêm vaccine HiB.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tỷ lệ bệnh đã giảm mạnh nhờ chương trình tiêm chủng mở rộng vaccine 5 trong 1 / 6 trong 1.",
        "extra": "Có thể gặp do Phế cầu khuẩn hoặc Liên cầu nhóm A ở trẻ đã tiêm phòng HiB."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Bốn dấu hiệu cờ đỏ phân biệt Viêm nắp thanh môn cấp (Epiglottitis) với Croup thông thường là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sốt cao nhiễm độc, KHÔNG HO (hoặc ho rất yếu), chảy nước dãi (Drooling) và tư thế kiềng 3 chân (Tripod).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nắp thanh môn sưng to cản trở nuốt nước bọt; trẻ ngồi cúi để mở rộng đường thở.",
        "extra": "Trẻ ngồi chồm ra trước, cằm chìa, ngửa cổ để mở tối đa đường thở; vẻ mặt kinh hoàng sợ hãi."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Hành vi nào bị CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI khi nghi ngờ trẻ bị Viêm nắp thanh môn cấp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• TUYỆT ĐỐI CẤM DÙNG CÂY ĐÈ LƯỠI KHÁM HỌNG hoặc chọc ngoáy đường thở.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Kích thích đè lưỡi sẽ gây co thắt thanh quản phản xạ hoàn toàn, khiến trẻ ngừng thở tử vong ngay lập tức.<br>",
        "extra": "Mọi can thiệp đường thở chỉ được thực hiện trong phòng mổ với sự chuẩn bị sẵn sàng của bác sĩ Tai Mũi Họng và Gây mê hồi sức."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Viêm khí quản do vi khuẩn (Bacterial Tracheitis) thường do vi khuẩn nào gây ra?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tụ cầu vàng (Staphylococcus aureus), bao gồm cả MRSA; ngoài ra có Phế cầu và Liên cầu A.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Thường là bội nhiễm vi khuẩn thứ phát sau một đợt Croup do virus HPIV hoặc Cúm.",
        "extra": "Niêm mạc khí quản bị hoại tử tạo thành các mảng giả mạc và nút mủ đặc quánh bít tắc lòng ống."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Hai dấu hiệu lâm sàng then chốt giúp bác sĩ nhận diện Viêm khí quản vi khuẩn (Bacterial Tracheitis) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1. Trẻ sốt cao tái diễn kèm bộ mặt nhiễm trùng, nhiễm độc nặng nề.<br>2. KHÔNG ĐÁP ỨNG hoặc đáp ứng rất kém với khí dung Adrenaline.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nút đờm mủ cơ học làm tắc lòng khí quản nên thuốc co mạch Adrenaline không thể giải quyết được.",
        "extra": "Cần soi hút mủ cấp cứu qua nội khí quản và điều trị kháng sinh phổ rộng (Ceftriaxone + Vancomycin)."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Dấu hiệu lâm sàng đặc thù nào giúp gợi ý Áp xe thành sau họng (Retropharyngeal Abscess - RPA)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vẹo cổ (Torticollis), hạn chế cử động ngửa cổ, sưng phồng thành sau họng, nuốt đau.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khối áp xe khoang sau hầu chèn ép đẩy lồi thành họng ra trước vào lòng đường thở.",
        "extra": "Chẩn đoán xác định bằng chụp CT scan cổ có cản quang hoặc X-quang cổ nghiêng thấy dày phần mềm trước cột sống."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Tại sao Áp xe thành sau họng (RPA) hầu như chỉ gặp ở trẻ dưới 5 tuổi?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Do các hạch lympho nằm trong khoang sau họng (hạch Gillette) teo biến và thoái hóa sau 4-5 tuổi.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Ở trẻ nhỏ, nhiễm trùng vùng mũi hầu dẫn lưu vào hạch này gây viêm hoại tử và tạo ổ áp xe.",
        "extra": "Sau 5 tuổi, nhiễm trùng khoang sau họng thường chỉ xảy ra sau chấn thương xuyên thủng (như hóc xương)."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Đặc điểm bệnh sử nào giúp phân biệt Dị vật đường thở (Foreign Body) với Croup cấp?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Khởi phát ĐỘT NGỘT khi đang ăn hoặc chơi đồ chơi nhỏ, KHÔNG SỐT, có 'Hội chứng xâm nhập' điển hình.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ ho sặc sụa, tím tái dữ dội sau đó chuyển sang thở rít thanh quản.",
        "extra": "Croup luôn có giai đoạn viêm long đường hô hấp trên 1-3 ngày trước đó; dị vật thì không."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PEDYTB - Ôn thi] Các dấu hiệu kèm theo nào giúp phân biệt Phù mạch dị ứng / Phản vệ với bệnh Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nổi mề đay, ngứa, phù môi/mí mắt, xuất hiện cấp tính sau tiếp xúc dị nguyên, có thể tụt huyết áp.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Phản ứng quá mẫn giải phóng Histamin gây phù nề thanh quản cấp; đáp ứng tức thì với Adrenaline tiêm bắp.",
        "extra": "Croup do virus không bao giờ có kèm ban mề đay dị ứng hay sưng phù mặt môi."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Dấu hiệu Nóc nhà thờ (Steeple sign) trên phim X-quang cổ thẳng (AP view) có bản chất hình ảnh học là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sự thu hẹp đối xứng của cột khí vùng hạ thanh môn, tạo thành hình tháp nhọn như nóc nhà thờ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Mất đi dạng bờ vai vuông vức bình thường của hạ thanh môn do phù nề niêm mạc dưới sụn nhẫn.",
        "extra": "Dấu hiệu này còn được gọi là 'dấu hiệu đầu bút chì' (pencil-point sign)."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Độ nhạy của Dấu hiệu Nóc nhà thờ (Steeple sign) trên X-quang ở bệnh nhi Croup là khoảng bao nhiêu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ đạt khoảng 50% các trường hợp.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Một phim X-quang cổ hoàn toàn bình thường KHÔNG LOẠI TRỪ được bệnh Croup.",
        "extra": "Croup là một chẩn đoán lâm sàng thuần túy; không bắt buộc phải có hình ảnh X-quang mới được điều trị."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Khi nào có chỉ định chụp X-quang vùng cổ ở trẻ nghi ngờ mắc Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chỉ chụp khi: Chẩn đoán không điển hình, nghi ngờ dị vật đường thở, hoặc trẻ không đáp ứng với điều trị.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>TUYỆT ĐỐI KHÔNG CHỤP THƯỜNG QUY ở trẻ Croup điển hình đang suy hô hấp.",
        "extra": "Bắt trẻ nằm ngửa ngửa cổ chụp phim trong lúc đang thở rít dễ làm trẻ hoảng loạn và ngừng thở."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Dấu hiệu Dấu ngón tay (Thumbprint sign) trên phim X-quang cổ nghiêng chỉ điểm bệnh lý nguy hiểm nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Viêm nắp thanh môn cấp (Epiglottitis).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nắp thanh môn bị viêm sưng to tròn như hình bóng ngón tay cái in trên phim.",
        "extra": "Bình thường trên phim nghiêng, nắp thanh môn chỉ là một dải mô mềm mảnh mai như ngón tay út."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Xét nghiệm công thức máu và CRP có vai trò gì trong chẩn đoán và xử trí ban đầu bệnh Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• KHÔNG CÓ CHỈ ĐỊNH THƯỜNG QUY.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhiễm virus HPIV có thể gây tăng nhẹ bạch cầu; chọc kim lấy máu làm trẻ khóc thét làm tăng công thở nguy hiểm.",
        "extra": "Chỉ làm xét nghiệm máu khi nghi ngờ nhiễm trùng huyết, viêm khí quản vi khuẩn hoặc bệnh nhi quá nặng."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PEDYTB - Ôn thi] Khí máu động mạch/mao mạch có nên lấy thường quy ở trẻ Croup không và tại sao?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• KHÔNG NÊN LẤY THƯỜNG QUY.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Thao tác chọc động mạch rất đau, làm trẻ khóc thét và hoảng loạn, có thể kích hoạt co thắt thanh quản nghẹt thở.",
        "extra": "Chỉ lấy khí máu khi trẻ đã suy hô hấp rất nặng, đặt nội khí quản hoặc theo dõi trong hồi sức PICU."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Thuốc điều trị nền tảng số 1 bắt buộc cho MỌI THỂ CROUP (kể cả thể Nhẹ) là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dexamethasone (Corticosteroid toàn thân).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Cochrane chứng minh cho Dexamethasone sớm giảm rõ rệt tỷ lệ nhập viện và tái khám cấp cứu.",
        "extra": "Quan điểm cũ 'thể nhẹ chỉ theo dõi không cho thuốc' hiện nay đã hoàn toàn bị bãi bỏ."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Liều Dexamethasone chuẩn quốc tế khuyến cáo trong điều trị Croup là bao nhiêu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• 0.15 mg/kg uống liều duy nhất (liều tối đa thông thường: 10 mg – 16 mg).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhiều thử nghiệm RCTs chứng minh liều 0.15 mg/kg có hiệu quả tương đương liều cao kinh điển 0.6 mg/kg.",
        "extra": "Trong trường hợp Croup thể nặng hoặc dọa suy hô hấp, bác sĩ có thể dùng liều 0.6 mg/kg."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Tại sao Dexamethasone lại được ưu tiên vượt trội so với Prednisolone hay Hydrocortisone trong Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hoạt lực kháng viêm mạnh gấp 25-30 lần Hydrocortisone, không giữ muối nước và thời gian bán thải dài 36-72 giờ.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhờ tác dụng kéo dài, chỉ cần uống ĐÚNG MỘT LIỀU DUY NHẤT là đủ bao phủ toàn bộ đợt bệnh.",
        "extra": "Prednisolone thời gian bán thải ngắn hơn nên phải uống 2-3 ngày, tăng nguy cơ quên thuốc."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Đường dùng nào của Dexamethasone được ưu tiên hàng đầu trong điều trị Croup và tại sao?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đường uống (Dạng siro hoặc viên hòa tan).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Sinh khả dụng đường uống rất cao, hiệu quả lâm sàng tương đương tiêm bắp nhưng không gây đau đớn cho trẻ.",
        "extra": "Chỉ dùng đường tiêm bắp (IM) hoặc tiêm tĩnh mạch (IV) khi trẻ nôn liên tục hoặc suy hô hấp quá nặng."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Nếu trẻ nôn ói không dung nạp Dexamethasone đường uống, thuốc khí dung nào được chọn thay thế tương đương?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Budesonide khí dung liều duy nhất 2 mg (khí dung qua máy nén khí).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Hiệu quả làm giảm phù nề và cải thiện điểm Westley tương đương Dexamethasone đường uống.",
        "extra": "Nhược điểm của Budesonide là giá thành cao hơn Dexamethasone và trẻ phải đeo mặt nạ khí dung."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Nếu tại cơ sở y tế không có sẵn Dexamethasone, có thể dùng Prednisolone đường uống thay thế với liều nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Prednisolone uống liều 1 mg/kg/ngày trong 2 đến 3 ngày.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Thời gian bán thải của Prednisolone ngắn hơn Dexamethasone (12-36h vs 36-72h) nên cần dùng 2-3 ngày.",
        "extra": "Dexamethasone vẫn là lựa chọn ưu tiên số 1 vì chỉ cần uống đúng 1 liều duy nhất."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Chỉ định dùng L-Adrenaline khí dung trong Croup áp dụng cho những phân tầng mức độ nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Croup thể Vừa (Westley 3–5) và Croup thể Nặng (Westley 6–11) hoặc Dọa suy hô hấp.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>KHÔNG chỉ định Adrenaline cho Croup thể Nhẹ (Westley ≤ 2 điểm).",
        "extra": "Adrenaline là vũ khí giải cứu cấp tốc hạ thanh môn khi trẻ bắt đầu có thở rít khi nằm yên tĩnh."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Liều lượng và cách dùng L-Adrenaline 1:1.000 (1 mg/mL) khí dung ở trẻ Croup như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Liều 0.5 mL/kg (Tối thiểu 2.5 mL, tối đa 5 mL) dung dịch nguyên chất 1:1.000, khí dung qua oxy 6–8 L/phút.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Dùng thẳng dịch nguyên chất không bắt buộc phải pha loãng nếu thể tích đã đủ 2.5–5 mL.",
        "extra": "Trẻ &lt; 5 kg dùng 2.5 mL; trẻ ≥ 10 kg dùng tối đa 5 mL."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Hiệu quả lâm sàng của L-Adrenaline thông thường so với Adrenaline racemic (đồng phân racemic) có khác nhau không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hiệu quả và tính an toàn tương đương tuyệt đối.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Không cần tìm kiếm Adrenaline racemic đắt tiền; ống L-Adrenaline 1 mg/mL sẵn có tại mọi tủ thuốc cấp cứu là chuẩn mực.",
        "extra": "Cochrane review khẳng định L-Adrenaline 1:1.000 hoàn toàn có thể thay thế Adrenaline racemic."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PEDYTB - Ôn thi] Sau bao lâu có thể lặp lại liều Adrenaline khí dung nếu trẻ Croup nặng chưa cải thiện khó thở?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Sau 15 đến 30 phút có thể lặp lại liều thứ 2 (hoặc liều thứ 3).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nếu sau 2–3 liều Adrenaline khí dung mà trẻ không đáp ứng, bắt buộc phải nghĩ đến chẩn đoán khác (Bacterial Tracheitis).",
        "extra": "Theo dõi sát nhịp tim khi dùng lặp lại Adrenaline (nhịp nhanh xoang thoáng qua là tác dụng phụ thường gặp)."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Hiện tượng dội ngược (Rebound phenomenon) sau khi khí dung Adrenaline trong Croup là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Triệu chứng thở rít và phù nề tái phát trở lại sau khoảng 2 giờ khi tác dụng co mạch của thuốc hết đi.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Giãn mạch hồi ứng sau co mạch làm dịch viêm thoát trở lại vào mô kẽ hạ thanh môn.",
        "extra": "Đây là lý do Dexamethasone phải luôn được cho cùng lúc để kịp phát huy tác dụng kháng viêm sau 2 giờ."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Thời gian theo dõi bắt buộc tối thiểu tại phòng cấp cứu sau liều Adrenaline khí dung cuối cùng là bao lâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Ít nhất 3 đến 4 giờ liên tục.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhằm đảm bảo trẻ đã vượt qua cửa sổ nguy cơ của hiện tượng dội ngược và tác dụng Dexamethasone đã phát huy.",
        "extra": "Cho trẻ về nhà trước 2 giờ sau khí dung Adrenaline là cạm bẫy tử vong rất nguy hiểm."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Tại sao liệu pháp xông hơi ẩm nước nóng (Mist therapy) bị các Hướng dẫn quốc tế KHÔNG KHUYẾN CÁO trong Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tổng quan Cochrane chứng minh xông ẩm KHÔNG làm cải thiện điểm Westley, không rút ngắn thời gian bệnh.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Hơi nước nóng còn gây nguy cơ bỏng đường thở, làm trẻ sợ hãi quấy khóc và ướt lạnh hạ thân nhiệt.",
        "extra": "Phương pháp dân gian bế trẻ vào phòng tắm xả nước nóng hiện nay không còn được y học khuyến cáo."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Tại sao kháng sinh KHÔNG ĐƯỢC CHỈ ĐỊNH trong điều trị Viêm thanh khí phế quản cấp thông thường?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vì > 95% căn nguyên là do virus (chủ yếu là Parainfluenza); kháng sinh không có tác dụng tiêu diệt virus.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Dùng kháng sinh không rút ngắn thời gian bệnh mà làm tăng nguy cơ tiêu chảy và kháng thuốc.",
        "extra": "Chỉ dùng kháng sinh khi có bằng chứng chắc chắn của bội nhiễm vi khuẩn thứ phát hoặc Viêm khí quản vi khuẩn."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Tại sao thuốc chống dị ứng kháng Histamin (Antihistamines) không nên dùng cho trẻ Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Kháng Histamin có tác dụng kháng Cholinergic làm khô niêm mạc và làm đờm dịch hạ thanh môn cô đặc lại.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Chất nhầy đặc quánh đóng nút bít tắc đường thở hẹp, làm trẻ khó thở nặng hơn.",
        "extra": "Trừ trường hợp Spasmodic Croup có kèm viêm mũi dị ứng rõ ràng, còn Croup do virus không dùng kháng Histamin."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Thuốc an thần (Sedatives) có được dùng để làm dịu trẻ Croup đang quấy khóc, bứt rứt không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• TUYỆT ĐỐI CHỐNG CHỈ ĐỊNH.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bứt rứt là dấu hiệu cảnh báo thiếu oxy não; thuốc an thần gây ức chế hô hấp làm trẻ ngừng thở đột ngột.",
        "extra": "Bác sĩ cho an thần ở trẻ khó thở thanh quản là sai lầm có thể dẫn đến tử vong trước tòa án."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Nguyên tắc 'Can thiệp tối thiểu' (Minimal handling) trong chăm sóc bệnh nhi Croup có ý nghĩa gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tránh mọi thủ thuật không cần thiết gây kích động trẻ (không lấy ven sớm ở thể nhẹ/vừa, không đè lưỡi).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khi trẻ khóc, lưu lượng khí qua thanh quản tăng làm áp lực âm tăng vọt, đường thở hẹp sụp nặng hơn.",
        "extra": "Luôn ưu tiên để trẻ nằm hoặc ngồi yên tĩnh trong lòng mẹ hoặc người chăm sóc trong suốt quá trình điều trị."
    },
    {
        "type": "basic",
        "category": "Biện pháp cấm & Lưu ý",
        "front": "[PED - Lâm sàng] Kỹ thuật cung cấp oxy an toàn cho trẻ Croup bị suy hô hấp nên thực hiện như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thở oxy dòng tự do (Blow-by oxygen) bằng cách để đầu ống oxy cách mũi trẻ 1-2 cm do mẹ cầm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Ép chặt mask vào mặt hoặc nhét canula vào mũi trẻ đang hoảng sợ sẽ làm trẻ khóc thét và nghẹt thở nặng hơn.",
        "extra": "Chỉ định oxy khi SpO2 &lt; 92% (hoặc SpO2 &lt; 90% theo AAP) hoặc trẻ có dấu hiệu tím tái."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Sai lầm kinh điển: 'Chỉ dùng Dexamethasone khi Croup chuyển sang thể nặng' có hậu quả gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bỏ lỡ cơ hội ngăn chặn tiến triển nặng; trẻ thể nhẹ không dùng steroid có tỷ lệ tái khám cấp cứu cao gấp 3 lần.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Dexamethasone liều duy nhất 0.15 mg/kg cực kỳ an toàn và bắt buộc dùng cho MỌI THỂ CROUP.",
        "extra": "Ngay cả khi trẻ chỉ ho ông ổng nhẹ tại phòng khám, 1 liều Dexamethasone uống cũng giúp trẻ ngủ yên giấc cả đêm."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Sai lầm kinh điển: Cho trẻ xuất viện ngay sau khi khí dung Adrenaline thấy hết tiếng thở rít dẫn đến nguy hiểm gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Trẻ bị hiện tượng dội ngược (Rebound) tái phát tắc nghẽn thanh quản dữ dội trên đường về nhà hoặc trong đêm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Adrenaline chỉ có tác dụng tạm thời 2 giờ; bắt buộc phải giữ lại theo dõi ít nhất 3-4 giờ tại bệnh viện.",
        "extra": "Chỉ cho về khi sau 4 giờ trẻ vẫn thở êm, không còn thở rít khi nằm yên và tác dụng Dexamethasone đã ổn định."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Xử trí chuẩn tại giường khi bệnh nhi nôn trớ ngay sau khi uống Dexamethasone như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nếu nôn trong vòng 15 phút: Cho uống lại liều tương đương; nếu nôn tiếp chuyển sang Budesonide khí dung 2 mg.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nếu trẻ nôn sau &gt; 30 - 60 phút: Thuốc đã được hấp thu vào dạ dày, không cần cho uống lại.",
        "extra": "Dexamethasone dạng siro vị ngọt dễ uống hơn viên nghiền đắng gây kích thích nôn."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Nếu một trẻ chẩn đoán Croup không cải thiện hoặc nặng hơn sau 2 liều Adrenaline khí dung liên tiếp, bác sĩ phải làm gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Lập tức nghi ngờ chẩn đoán khác: Viêm khí quản vi khuẩn (Bacterial Tracheitis), Dị vật đường thở hoặc Epiglottitis.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Báo động kíp PICU/Tai Mũi Họng chuẩn bị nội soi can thiệp đường thở và đặt ống nội khí quản có chuẩn bị.",
        "extra": "Không tiếp tục khí dung Adrenaline vô ích vì sẽ gây nhịp tim nhanh và co giật."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Tại sao không được ép trẻ Croup nằm ngửa trên bàn khám khi trẻ đang muốn ngồi dậy?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nằm ngửa làm các cơ vùng cổ chùng xuống, đáy lưỡi và mô phù nề hạ thanh môn tụt ra sau chèn ép đường thở.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ ngồi dậy là tư thế tự vệ sinh lý để huy động cơ hô hấp phụ và mở rộng tối đa đường thở.",
        "extra": "Hãy để trẻ tự do lựa chọn tư thế dễ chịu nhất, tốt nhất là ngồi tựa vào ngực mẹ."
    },
    {
        "type": "basic",
        "category": "Ca lâm sàng thực chiến",
        "front": "[PED - Lâm sàng] Ca lâm sàng 1: Bé 18 tháng, 11 kg, vào viện 2h sáng vì thở rít khi nằm yên, co kéo lồng ngực vừa, SpO2 96%. Phác đồ xử trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chẩn đoán: Croup thể vừa (Westley 4 điểm).<br>• Xử trí: Dexamethasone uống 1.65 mg (hoặc 2 mg) + Khí dung L-Adrenaline 1:1.000 liều 5 mL qua oxy.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Theo dõi tại phòng cấp cứu tối thiểu 3 - 4 giờ.",
        "extra": "Không cho trẻ về ngay sau khi khí dung; giải thích cho mẹ về hiện tượng dội ngược."
    },
    {
        "type": "basic",
        "category": "Ca lâm sàng thực chiến",
        "front": "[PED - Lâm sàng] Ca lâm sàng 2: Trẻ 3 tuổi Croup thở rít nặng, sốt 39.5°C, vẻ mặt nhiễm độc, khí dung 2 liều Adrenaline không đỡ. Chẩn đoán và xử trí?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chẩn đoán: Viêm khí quản vi khuẩn (Bacterial Tracheitis).<br>• Xử trí: Chuyển PICU đặt NKQ hút mủ hoại tử, cấy đờm máu và tiêm kháng sinh Ceftriaxone + Vancomycin.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tụ cầu vàng kháng thuốc (MRSA) là thủ phạm hàng đầu gây bít tắc khí quản bằng nút mủ giả mạc.",
        "extra": "Cần soi hút rửa làm sạch lòng khí quản để thông khí hiệu quả."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Tip đặt nội khí quản: Khi bắt buộc phải đặt nội khí quản cho trẻ Croup nặng, quy tắc chọn cỡ ống là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bắt buộc chuẩn bị sẵn ống nội khí quản NHỎ HƠN 0.5 đến 1.0 CỠ so với công thức tính theo tuổi thông thường.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Vùng hạ thanh môn bị phù nề làm thu hẹp lòng ống; cố đẩy ống đúng cỡ chuẩn sẽ gây rách loét và hoại tử sụn nhẫn.",
        "extra": "Ví dụ: Trẻ 2 tuổi chuẩn là ống cỡ 4.5 thì phải chuẩn bị sẵn ống 4.0 và 3.5."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Ba tiêu chuẩn xuất viện an toàn cho bệnh nhi Croup tại phòng cấp cứu là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1. Hết thở rít khi nằm yên tĩnh sau ít nhất 3 - 4 giờ theo dõi.<br>2. Tỉnh táo, uống tốt, SpO2 ≥ 94% khí phòng.<br>3. Người nhà được tư vấn đầy đủ dấu hiệu cờ đỏ và có khả năng quay lại viện.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nếu nhà quá xa viện (&gt; 30 phút) hoặc vào đêm khuya, nên lưu viện theo dõi đến sáng.",
        "extra": "Dặn người nhà quay lại ngay nếu trẻ thở rít trở lại, thở co kéo mạnh hoặc không uống được."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Năm tiêu chuẩn chỉ định nhập viện điều trị nội trú đối với bệnh nhi Croup là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Điểm Westley ≥ 3 sau 3-4h, cần ≥ 2 liều Adrenaline, SpO2 &lt; 92%, trẻ nhỏ &lt; 6 tháng tuổi hoặc gia đình không an toàn.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ &lt; 6 tháng hoặc khó thở dai dẳng có nguy cơ suy hô hấp tiến triển nhanh.",
        "extra": "Bất kỳ nghi ngờ nào về viêm khí quản vi khuẩn hoặc dị vật đều là chỉ định nhập viện tuyệt đối."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Lời dặn dò cốt lõi dành cho cha mẹ khi chăm sóc trẻ Croup nhẹ tại nhà là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Đưa trẻ đi tái khám cấp cứu ngay nếu: Trẻ thở rít khi đang ngủ yên, thở rút lõm ngực, chảy dãi hoặc không uống được.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Cơn khó thở có thể tái phát vào đêm thứ 2 hoặc thứ 3 của bệnh.",
        "extra": "Khuyên cha mẹ giữ không khí phòng thoáng mát, cho trẻ uống nhiều nước ấm từng ngụm nhỏ."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PED - Lâm sàng] Dấu hiệu 'Audible slap' (tiếng đập nghe thấy) và 'Palpatory thud' (tiếng chạm sờ thấy) chỉ điểm bệnh cảnh nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dị vật khí quản di động (chuyển động lên xuống theo luồng khí thở đập vào thanh môn).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Dị vật không cố định mà bật nảy trong lòng khí quản; cần phân biệt với tiếng thở rít cố định của Croup.",
        "extra": "Đây là dấu hiệu kinh điển của dị vật dạng hạt (hạt dưa, hạt đậu phộng) nằm lơ lửng trong khí quản."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PED - Lâm sàng] Trẻ nhũ nhi 1 tháng tuổi có tiếng thở rít êm dịu từ tuần thứ 2-4 sau sinh, tăng khi nằm ngửa/bú, giảm khi nằm sấp ngực nghiêng gợi ý bệnh gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Mềm sụn thanh quản bẩm sinh (Laryngomalacia).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Là nguyên nhân bẩm sinh hàng đầu gây thở rít ở trẻ sơ sinh và nhũ nhi nhỏ; không kèm sốt hay ho sủa.",
        "extra": "Sụn thanh thiệt mềm nhão hình chữ Omega sụp vào thanh môn ở thì hít vào."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PED - Lâm sàng] Trẻ 3 tháng tuổi có tiếng thở rít hai thì tiến triển nặng dần, kèm theo bớt mạch máu vùng râu/cổ gợi ý chẩn đoán gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• U máu vùng hạ thanh môn (Subglottic hemangioma).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khối u máu phát triển tăng sinh mạnh từ tháng thứ 2 đến tháng thứ 6 gây hẹp dần lòng hạ thanh môn.",
        "extra": "Điều trị hiệu quả hiện nay là dùng Propranolol đường uống dưới sự theo dõi của chuyên khoa."
    },
    {
        "type": "basic",
        "category": "Chẩn đoán phân biệt",
        "front": "[PED - Lâm sàng] Trẻ có tiền sử thở máy sơ sinh kéo dài 2 tuần, nay 9 tháng tuổi xuất hiện thở rít tái diễn mỗi đợt nhiễm trùng hô hấp nghĩ tới gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Hẹp hạ thanh môn mắc phải do sẹo xơ sau đặt nội khí quản (Acquired subglottic stenosis).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Áp lực bóng chèn (cuff) hoặc ống NKQ cọ xát gây thiếu máu hoại tử niêm mạc tạo sẹo co kéo.",
        "extra": "Khi trẻ bị cảm cúm thông thường, phù nề nhẹ trên nền sẹo hẹp cũ sẽ gây tắc nghẽn thanh quản dữ dội."
    },
    {
        "type": "basic",
        "category": "Triệu chứng & Khám",
        "front": "[PED - Lâm sàng] Phân biệt 3 âm thanh thở bất thường: Stridor (thở rít), Wheezing (khò khè) và Stertor (thở ngáy)?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Stridor: Âm cao thô ráp, thì hít vào (thanh khí quản).<br>• Wheezing: Âm nhạc rít, thì thở ra (phế quản nhỏ).<br>• Stertor: Âm trầm ục ịch, thì hít vào (mũi hầu).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Vị trí tắc nghẽn quyết định thì thở và tần số âm thanh.",
        "extra": "Trẻ Croup điển hình có Inspiratory Stridor; nếu có kèm Wheezing là Croup lan tỏa xuống phế quản (Laryngotracheobronchitis)."
    },
    {
        "type": "basic",
        "category": "Triệu chứng & Khám",
        "front": "[PED - Lâm sàng] Thời điểm chuẩn xác nhất để bác sĩ lượng giá tiêu chí Thở rít trong thang điểm Westley là khi nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bắt buộc khi trẻ NẰM YÊN TĨNH, HOÀN TOÀN KHÔNG KHÓC.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nếu đánh giá lúc trẻ đang khóc giãy, tiếng rít sẽ bị chấm điểm giả tạo (nhầm từ thể nhẹ sang thể vừa).",
        "extra": "Hãy cho trẻ ngậm ti mẹ hoặc nằm trong lòng mẹ cho trẻ nín hẳn trước khi đặt ống nghe."
    },
    {
        "type": "basic",
        "category": "Triệu chứng & Khám",
        "front": "[PED - Lâm sàng] Tại sao trẻ Croup do virus thường chỉ sốt nhẹ 38 - 38.5°C, nếu sốt cao vọt 39.5 - 40°C cần cảnh giác cao độ?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Gợi ý chẩn đoán nhiễm trùng vi khuẩn xâm lấn nguy hiểm: Viêm nắp thanh môn cấp (HiB) hoặc Viêm khí quản vi khuẩn (Tụ cầu).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Virus Á cúm thông thường hiếm khi gây hội chứng đáp ứng viêm toàn thân sốt cao kéo dài.",
        "extra": "Sốt cao kèm vẻ mặt nhiễm trùng là cờ đỏ báo động không bao giờ được bỏ qua."
    },
    {
        "type": "basic",
        "category": "Triệu chứng & Khám",
        "front": "[PED - Lâm sàng] Vị trí co kéo cơ hô hấp phụ nào xuất hiện sớm nhất khi bắt đầu có tắc nghẽn thanh quản?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Co kéo hõm trên xương ức và rút lõm khoảng liên sườn.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do áp lực âm tạo ra ở lồng ngực trên kéo sụp các vùng mô mềm mỏng manh nhất trước tiên.",
        "extra": "Rút lõm dưới sườn và phập phồng cánh mũi thường xuất hiện khi mức độ tắc nghẽn đã tiến triển nặng hơn."
    },
    {
        "type": "basic",
        "category": "Cận lâm sàng & Hình ảnh",
        "front": "[PED - Lâm sàng] Yêu cầu kỹ thuật khi chụp X-quang cổ thẳng (AP) tìm dấu hiệu Steeple sign là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Chụp ở thì HÍT VÀO với tư thế cổ thẳng trục; tránh chụp thì thở ra.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nếu chụp ở thì thở ra, sự xẹp sinh lý của khí quản có thể tạo ra hình ảnh giả hẹp hạ thanh môn.",
        "extra": "Không bao giờ để việc chụp X-quang làm trì hoãn chỉ định dùng thuốc Dexamethasone hay Adrenaline."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Dùng Dexamethasone liều duy nhất trong Croup có gây ức chế trục hạ đồi - tuyến yên - thượng thận (HPA) không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• HOÀN TOÀN KHÔNG.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Chỉ 1 liều duy nhất (kể cả liều cao 0.6 mg/kg) không gây teo vỏ thượng thận và KHÔNG CẦN GIẢM LIỀU DẦN.",
        "extra": "Trục HPA chỉ bị ức chế đáng kể khi dùng Glucocorticoid liên tục trên 14 ngày."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Tại sao máy khí dung siêu âm (Ultrasonic nebulizer) KHÔNG NÊN DÙNG để khí dung Adrenaline?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nhiệt lượng sinh ra từ sóng siêu âm tần số cao có thể làm biến tính và phá hủy hoạt chất Adrenaline.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Bắt buộc sử dụng máy khí dung dòng khí nén (Jet nebulizer) với nguồn oxy hoặc khí nén 6-8 L/phút.",
        "extra": "Khí dung bằng nguồn oxy còn giúp bổ sung oxy đồng thời cho trẻ đang khó thở."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Một ống L-Adrenaline 1 mg/1 mL tương đương bao nhiêu thể tích khi dùng cho trẻ 5 kg bị Croup nặng?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Liều 0.5 mL/kg = 2.5 mL (dùng đúng 2 ống rưỡi dung dịch 1:1.000 nguyên chất).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>2.5 mL là ngưỡng thể tích tối thiểu để buồng khí dung hoạt động hiệu quả tạo hạt sương mù.",
        "extra": "Trẻ 10 kg dùng 5 mL (5 ống nguyên chất); không cần pha loãng thêm nước muối nếu thể tích đã đủ 2.5 - 5 mL."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Tác dụng phụ thường gặp nhất trên tim mạch sau khi khí dung L-Adrenaline là gì?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nhịp nhanh xoang thoáng qua (tần số tim tăng thêm 20-30 bpm) và da hơi tái nhợt.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Do một lượng nhỏ thuốc hấp thu toàn thân kích thích thụ thể Beta-1 và Alpha-1 ngoại vi.",
        "extra": "Hiện tượng này hoàn toàn lành tính và tự hết sau 30-45 phút; rất hiếm khi gây loạn nhịp tim nguy hiểm ở trẻ nhỏ."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Trẻ Croup thể nhẹ có cần dùng kháng sinh dự phòng bội nhiễm vi khuẩn không?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• TUYỆT ĐỐI KHÔNG.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Tỷ lệ bội nhiễm vi khuẩn ở Croup rất thấp (&lt; 1%); kháng sinh không có tác dụng dự phòng mà gây loạn khuẩn ruột.",
        "extra": "Hướng dẫn của AAP và NICE đồng thuận cấm chỉ định kháng sinh dự phòng cho Croup."
    },
    {
        "type": "basic",
        "category": "Chăm sóc hỗ trợ",
        "front": "[PED - Lâm sàng] Chế độ dinh dưỡng cho trẻ Croup thể nặng (Westley ≥ 6 điểm) tại buồng cấp cứu như thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Tạm nhịn ăn uống đường miệng hoàn toàn (NPO - Nil per os).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ đang khó thở gắng sức nặng nuốt thức ăn/sữa rất dễ hít sặc vào khí quản, và để dạ dày rỗng chuẩn bị đặt nội khí quản cấp cứu.",
        "extra": "Bù dịch qua đường truyền tĩnh mạch trong khi chờ đợi đáp ứng của thuốc."
    },
    {
        "type": "basic",
        "category": "Chăm sóc hỗ trợ",
        "front": "[PED - Lâm sàng] Nếu trẻ Croup thể nặng cần truyền dịch duy trì, loại dịch truyền nào được ưu tiên lựa chọn?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Dung dịch đẳng trương: Glucose 5% trong NaCl 0.9% (hoặc Ringer Lactat).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>TUYỆT ĐỐI TRÁNH dịch nhược trương (D5 0.2% NaCl) để phòng ngừa nguy cơ hạ Natri máu cấp nếu trẻ có tăng tiết ADH.",
        "extra": "Duy trì tốc độ dịch khoảng 70-80% nhu cầu cơ bản ở trẻ khó thở nặng."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Tại sao không được dùng thuốc giảm ho chứa Codeine hoặc Dextromethorphan ở trẻ Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Làm ức chế phản xạ ho tự nhiên tống dịch đờm và nguy cơ ức chế trung tâm hô hấp gây ngừng thở.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Ho trong Croup là do phù nề hạ thanh môn cơ học; điều trị ho là dùng Corticoid làm xẹp phù nề chứ không dùng thuốc giảm ho.",
        "extra": "FDA khuyến cáo cấm dùng thuốc ho có Opioid/Codeine cho trẻ dưới 12 tuổi."
    },
    {
        "type": "basic",
        "category": "Cạm bẫy lâm sàng",
        "front": "[PED - Lâm sàng] Tại sao không nên dùng bình xịt định liều Salbutamol (Ventolin MDI) cho bệnh Croup?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Salbutamol tác dụng trên thụ thể Beta-2 ở cơ trơn phế quản nhỏ, hoàn toàn không có tác dụng co mạch giảm phù nề hạ thanh môn.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Vùng hạ thanh môn không có cơ trơn phế quản để giãn; dùng Salbutamol làm nhịp tim nhanh vô ích.",
        "extra": "Thuốc giãn phế quản chỉ có vai trò trong Hen phế quản; trong Croup thuốc giải cứu duy nhất là Adrenaline."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Khi trẻ Croup thở rít nặng cần thở oxy nhưng sợ hãi giãy giụa, người chăm sóc nên giữ trẻ ở tư thế nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Bế ngồi tựa ngực mẹ, mẹ cầm đầu dây oxy dòng tự do (blow-by) để cách mũi trẻ 2-3 cm.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Trẻ được mẹ bế sẽ an tâm nín khóc; nín khóc làm giảm công thở và giảm sụp hẹp thanh quản ngay lập tức.",
        "extra": "Sự bình tĩnh của cha mẹ và trẻ là liều thuốc giảm tắc nghẽn đường thở đầu tiên."
    },
    {
        "type": "basic",
        "category": "Tips lâm sàng",
        "front": "[PED - Lâm sàng] Trẻ bị Croup tái phát nhiều lần trong năm (≥ 3 đợt/năm) cần được chỉ định thăm dò chuyên khoa nào?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nội soi tai mũi họng - thanh khí phế quản (Laryngoscopy / Bronchoscopy).<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhằm tầm soát các bất thường giải phẫu tiềm ẩn: Hẹp hạ thanh môn bẩm sinh, u máu, mềm sụn thanh quản hoặc trào ngược dạ dày thực quản (GERD).",
        "extra": "Croup tái phát thường xuyên (Recurrent Croup) không đơn thuần là nhiễm virus HPIV ngẫu nhiên."
    },
    {
        "type": "basic",
        "category": "Tiêu chuẩn xuất viện",
        "front": "[PED - Lâm sàng] Thời gian tồn tại trung bình của triệu chứng ho ông ổng ở trẻ Croup là bao lâu?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Giảm rõ rệt sau 48 giờ và khỏi hẳn hoàn toàn trong vòng 3 đến 7 ngày.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Sau khi hết thở rít thanh quản, trẻ có thể chuyển sang ho đờm nhẹ như cảm cúm thông thường.",
        "extra": "Nếu triệu chứng ho rít kéo dài trên 7-10 ngày, bắt buộc phải khám tìm nguyên nhân khác."
    },
    {
        "type": "basic",
        "category": "Tiêu chuẩn xuất viện",
        "front": "[PED - Lâm sàng] Dấu hiệu cảnh báo nào cha mẹ cần được dặn dò để phát hiện trẻ Croup tái phát nặng tại nhà?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Thở rít nghe rõ khi trẻ đang nằm ngủ yên tĩnh, lồng ngực rút lõm sâu, trẻ mệt lả không bú được hoặc tím môi.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Cơn khó thở thanh quản có thể bùng phát trở lại vào đêm thứ 2 hoặc thứ 3 của đợt bệnh.",
        "extra": "Cung cấp tờ rơi hướng dẫn dấu hiệu nguy hiểm cho gia đình trước khi cho xuất viện."
    },
    {
        "type": "basic",
        "category": "Thang điểm Westley",
        "front": "[PED - Lâm sàng] Tại sao hai tiêu chí Tím tái và Tri giác lại có trọng số điểm cao nhất (4 - 5 điểm) trong thang Westley?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Vì phản ánh tình trạng mất bù sinh lý học: Thiếu oxy máu nặng và suy giảm oxy hóa mô não đe dọa ngừng thở.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Chỉ cần 1 trong 2 tiêu chí này xuất hiện là trẻ lập tức rơi vào nhóm Thể nặng hoặc Dọa suy hô hấp.",
        "extra": "Bệnh nhi có tím tái hoặc li bì bắt buộc phải được xử trí trong phòng hồi sức cấp cứu tối khẩn."
    },
    {
        "type": "basic",
        "category": "Giải phẫu & Sinh lý bệnh",
        "front": "[PED - Lâm sàng] Lớp hạ niêm mạc vùng hạ thanh môn có đặc điểm vi thể nào khiến nó dễ tích tụ dịch phù nề?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Cấu tạo bởi mô liên kết xốp lỏng lẻo, giàu mạng lưới mao mạch máu và tế bào mast.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Khi virus xâm nhập, các chất trung gian hóa học làm tăng tính thấm mao mạch ồ ạt, dịch viêm tràn ngập khoang kẽ lỏng lẻo.",
        "extra": "Mô liên kết lỏng lẻo này bị giam hãm bên trong khung sụn nhẫn cứng nhắc nên chỉ phồng vào trong lòng ống thở."
    },
    {
        "type": "basic",
        "category": "Chiến lược điều trị",
        "front": "[PED - Lâm sàng] Sau khi khí dung Adrenaline, chỉ số nhịp thở và tiếng thở rít của trẻ thay đổi thế nào sau 15-30 phút nếu đáp ứng tốt?",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>• Nhịp thở giảm chậm lại, lồng ngực bớt co kéo rõ rệt, tiếng thở rít hạ thanh môn êm dịu dần hoặc biến mất.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Nhịp tim có thể hơi nhanh thoáng qua do tác dụng của Adrenaline, sau đó ổn định lại khi trẻ bớt khó thở.",
        "extra": "Nếu sau 30 phút mà nhịp thở vẫn nhanh dốc và tiếng rít không giảm, phải chuẩn bị khí dung liều thứ 2."
    },
    {
        "type": "basic",
        "category": "Tổng kết thực hành",
        "front": "[PED - Lâm sàng] Tóm tắt 3 mệnh lệnh sống còn trong xử trí bệnh Croup tại phòng cấp cứu:",
        "back": "<b>🎯 Trả lời cốt lõi:</b><br>1. Dexamethasone 0.15 mg/kg uống cho MỌI THỂ Croup.<br>2. Adrenaline 1:1.000 khí dung ngay khi có THỞ RÍT KHI NẰM YÊN.<br>3. Giữ trẻ bình tĩnh trong lòng mẹ, tuyệt đối cấm kích động hay đè lưỡi.<br><br><b>💡 Cơ chế / Lưu ý:</b><br>Theo dõi tối thiểu 3-4 giờ sau liều Adrenaline cuối cùng trước khi quyết định cho về.",
        "extra": "Ba nguyên tắc này giúp giảm trên 80% tỷ lệ đặt nội khí quản và tử vong do Croup."
    }
]

def main():
    print(f"Building master deck for {DECK_NAME}...")
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    
    formatted_cards = []
    
    for i, c in enumerate(CARDS_DATA, 1):
        card_id = f"PED24-MASTER-{i:03d}"
        cat = c.get("category", "Lâm sàng Croup")
        
        if c["type"] == "basic":
            f_clean = clean_html(c["front"])
            b_clean = clean_html(c["back"])
            e_clean = clean_html(c.get("extra", ""))
            
            note = genanki.Note(
                model=basic_model,
                fields=[f_clean, b_clean, e_clean, cat],
                tags=["PED-24", "Croup", cat.replace(" ", "-")]
            )
            deck.add_note(note)
            formatted_cards.append({
                "id": card_id,
                "type": "basic",
                "category": cat,
                "front": f_clean,
                "back": b_clean,
                "extra": e_clean,
                "tags": ["PED-24", "Croup", cat.replace(" ", "-")]
            })
        elif c["type"] == "cloze":
            t_clean = clean_html(c["text"])
            e_clean = clean_html(c.get("extra", ""))
            
            note = genanki.Note(
                model=cloze_model,
                fields=[t_clean, e_clean, cat],
                tags=["PED-24", "Croup", "Westley", cat.replace(" ", "-")]
            )
            deck.add_note(note)
            formatted_cards.append({
                "id": card_id,
                "type": "cloze",
                "category": cat,
                "text": t_clean,
                "extra": e_clean,
                "tags": ["PED-24", "Croup", "Westley", cat.replace(" ", "-")]
            })

    # Export APKG
    package = genanki.Package(deck)
    package.write_to_file(OUTPUT_APKG)
    print(f"Successfully generated {OUTPUT_APKG} with {len(formatted_cards)} master cards!")
    
    # Export JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(formatted_cards, f, indent=2, ensure_ascii=False)
    print(f"Successfully updated {OUTPUT_JSON}!")

if __name__ == "__main__":
    main()
