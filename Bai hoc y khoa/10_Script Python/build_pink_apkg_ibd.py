#!/usr/bin/env python3
"""
build_pink_apkg_ibd.py — Build APKG tone hồng cho bài IM-38b IBD.
"""
import sys
import re
import hashlib
import warnings
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

warnings.filterwarnings('ignore', category=UserWarning, module='genanki')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import genanki

PINK_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&display=swap');

.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', 'Noto Sans', Arial, sans-serif;
  font-size: 17px;
  line-height: 1.8;
  text-align: left;
  color: #4a2c3a;
  background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
  padding: 24px;
  border-radius: 12px;
}
.card.nightMode {
  background: linear-gradient(135deg, #4a2c3a 0%, #5c3a4a 100%);
  color: #ffe4e1;
}
#front, #back {
  background-color: rgba(255, 255, 255, 0.85);
  padding: 18px 22px;
  border-radius: 10px;
  border: 1px solid #ffb6c1;
  box-shadow: 0 2px 6px rgba(255,182,193,0.2);
  margin-bottom: 14px;
}
.card.nightMode #front, .card.nightMode #back {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255,182,193,0.2);
  color: #fff0f5;
}
#front p, #back p { margin: 6px 0; }
#front ul, #back ul, #front ol, #back ol { margin: 6px 0; padding-left: 22px; }
#front li, #back li { margin: 4px 0; line-height: 1.7; }
#front b, #back b, #front strong, #back strong {
  color: #d1495b;
  font-weight: 600;
}
.card.nightMode #front b, .card.nightMode #back b,
.card.nightMode #front strong, .card.nightMode #back strong {
  color: #ffb6c1;
}
.tag {
  display: inline-block;
  background-color: #ffb6c1;
  color: #d1495b;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  margin-right: 6px;
  font-weight: 500;
}
hr#answer {
  margin: 12px 0;
  border: 0;
  border-top: 1px dashed #ffb6c1;
}
"""

def stable_id(seed_str):
    h = hashlib.md5(seed_str.encode()).hexdigest()[:12]
    return int(h, 16) % 9000000000000 + 1000000000000

def build_ibd_pink_apkg():
    cards = []
    
    cards.extend([
        {
            'front': 'Về mặt giải phẫu bệnh, tổn thương trong Viêm loét đại tràng (UC) có đặc điểm gì khác biệt so với Bệnh Crohn (CD)?',
            'back': '<b>UC:</b> Tổn thương <b>nông</b> (chỉ ở niêm mạc và dưới niêm mạc), <b>liên tục</b>, luôn bắt đầu từ trực tràng lan lên.<br><b>Crohn:</b> Tổn thương <b>sâu xuyên thành</b> (transmural), <b>ngắt quãng</b> (skip lesions), có thể gặp ở bất kỳ đoạn nào từ miệng đến hậu môn.',
            'tag': 'GiaiPhauBenh'
        },
        {
            'front': 'Dấu hiệu vi thể đặc trưng nhất để chẩn đoán Bệnh Crohn (CD) trên sinh thiết là gì?',
            'back': 'Sự hiện diện của <b>U hạt không bã đậu (Non-caseating granulomas)</b>.',
            'tag': 'GiaiPhauBenh'
        },
        {
            'front': 'Tại sao bệnh nhân Crohn thường có biến chứng hẹp lòng ruột (tắc ruột) hoặc rò rỉ (fistulas) trong khi bệnh nhân UC hiếm khi gặp?',
            'back': 'Vì tổn thương của Crohn là <b>viêm xuyên qua cả 4 lớp thành ruột (Transmural inflammation)</b>, làm thành ruột dày lên, xơ hóa gây hẹp, hoặc tạo đường hầm xuyên qua các cơ quan lân cận gây rò.',
            'tag': 'BienChung'
        },
        {
            'front': 'Kể tên 4 nhóm biểu hiện ngoài ruột (EIMs) thường gặp ở bệnh nhân IBD.',
            'back': '1. <b>Khớp:</b> Viêm khớp ngoại biên, viêm cột sống dính khớp.<br>2. <b>Da:</b> Hồng ban nút, viêm da mủ hoại thư.<br>3. <b>Mắt:</b> Viêm màng bồ đào, viêm thượng củng mạc.<br>4. <b>Gan mật:</b> Viêm đường mật xơ hóa nguyên phát (PSC - đặc biệt hay gặp ở UC).',
            'tag': 'LamSang'
        },
        {
            'front': 'Xét nghiệm Fecal Calprotectin ở ngưỡng nào có giá trị loại trừ IBD tốt nhất?',
            'back': 'Theo AGA, ngưỡng <b>50-60 μg/g</b> có độ nhạy 81% và độ đặc hiệu 87%, mang lại tỷ lệ âm tính giả thấp nhất. Nếu < 50 μg/g, nguy cơ IBD rất thấp.',
            'tag': 'CanLamSang'
        },
        {
            'front': 'Theo phân loại Montreal cho UC, tổn thương E1, E2, E3 tương ứng với các vùng giải phẫu nào?',
            'back': '<b>E1 (Viêm trực tràng):</b> Chỉ ở trực tràng.<br><b>E2 (Viêm đại tràng trái):</b> Lan đến góc lách.<br><b>E3 (Viêm toàn bộ đại tràng):</b> Vượt qua góc lách, đến manh tràng.',
            'tag': 'PhanLoai'
        },
        {
            'front': 'Biến chứng cấp cứu ngoại khoa nguy hiểm nhất của đợt cấp UC nặng là gì và dấu hiệu nhận biết trên X-quang?',
            'back': '<b>Phình đại tràng nhiễm độc (Toxic Megacolon)</b>.<br>Dấu hiệu X-quang: Đại tràng ngang giãn to <b>> 6 cm</b>, kèm theo tình trạng nhiễm độc toàn thân (sốt, mạch nhanh, tụt huyết áp).',
            'tag': 'CapCuu'
        },
        {
            'front': 'Tại sao TUYỆT ĐỐI KHÔNG dùng Loperamide cho bệnh nhân đang trong đợt cấp nặng của Viêm loét đại tràng (UC)?',
            'back': 'Loperamide làm liệt nhu động ruột. Đại tràng đang viêm nặng không thể co bóp tống khí và độc tố ra ngoài sẽ bị giãn ồ ạt, kích phát biến chứng <b>Phình đại tràng nhiễm độc (Toxic Megacolon)</b>.',
            'tag': 'DieuTri'
        },
        {
            'front': 'Trong điều trị UC, thuốc 5-ASA (Mesalazine) dạng uống có cần chia nhiều lần trong ngày không?',
            'back': '<b>Không.</b> Phân tích gộp cho thấy uống <b>1 lần/ngày (Once daily)</b> có hiệu quả lui bệnh và duy trì tương đương việc chia nhiều lần, đồng thời giúp tăng tuân thủ điều trị.',
            'tag': 'DuocLy'
        },
        {
            'front': 'Lỗi sai "tử huyệt" khi sử dụng Corticosteroid trong điều trị IBD là gì?',
            'back': 'Dùng Corticoid để <b>điều trị duy trì</b>. Corticoid chỉ được dùng để <b>cắt cơn cấp</b>, sau đó phải giảm liều dần. Dùng duy trì gây tác dụng phụ nghiêm trọng và không giữ được lui bệnh lâu dài.',
            'tag': 'DuocLy'
        },
        {
            'front': 'Tại Việt Nam, bệnh Crohn rất dễ bị chẩn đoán nhầm với bệnh lý truyền nhiễm nào do có tổn thương nội soi và sinh thiết tương tự?',
            'back': '<b>Lao ruột (Intestinal Tuberculosis)</b>.<br>Cả hai đều gây loét vùng hồi-manh tràng và có u hạt trên sinh thiết. Nếu chẩn đoán nhầm Crohn và cho ức chế miễn dịch, vi khuẩn lao sẽ bùng phát gây tử vong.',
            'tag': 'ThucChienVN'
        }
    ])

    deck_name = "IM-38b_Benh_Viem_Ruot_Man_IBD"
    model_id = stable_id(deck_name + "model")
    deck_id = stable_id(deck_name + "deck")
    
    model = genanki.Model(
        model_id,
        f"Pink Basic Model - {deck_name}",
        fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Tags'}],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div id="front">{{Question}}</div>',
                'afmt': '<div id="front">{{Question}}</div><hr id="answer"><div id="back">{{Answer}}</div><br>{{Tags}}',
            }
        ],
        css=PINK_CSS
    )
    deck = genanki.Deck(deck_id, deck_name, description="Bộ thẻ ôn tập Bệnh Viêm Ruột Mạn IBD (UC & Crohn) - Tone Hồng")

    for i, card in enumerate(cards):
        note = genanki.Note(
            model=model,
            fields=[card['front'], card['back'], f'<span class="tag">IBD</span> <span class="tag">{card["tag"]}</span>'],
            guid=stable_id(f"IBD_card_{i}")
        )
        deck.add_note(note)

    out_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-38b_Benh_Viem_Ruot_Man_IBD' / f'Anki - {deck_name}.apkg'
    genanki.Package(deck).write_to_file(str(out_path))
    print(f"✅ Đã tạo thành công bộ flashcard tone hồng: {out_path}")
    print(f"Tổng số thẻ: {len(cards)}")

if __name__ == "__main__":
    build_ibd_pink_apkg()
