#!/usr/bin/env python3
"""
build_pink_apkg_nephron.py — Build APKG tone hồng cho bài IM-43b Sinh lý Nephron & Thuốc lợi tiểu.
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

def build_apkg():
    cards = []
    
    cards.extend([
        {
            'front': 'Trong bản đồ Nephron, Trạm 2 (Ống lượn gần - PCT) có nhiệm vụ sinh lý gì và tái hấp thu bao nhiêu % lượng Natri?',
            'back': 'PCT là trạm thu hồi rác khổng lồ, tái hấp thu khoảng <b>65% lượng Na+ và nước</b>, cùng với 100% glucose và acid amin. Cơ chế hoạt động chủ yếu nhờ enzyme Carbonic Anhydrase (CA).',
            'tag': 'SinhLy'
        },
        {
            'front': 'Thuốc Acetazolamide (nhóm ức chế Carbonic Anhydrase) tác động vào đoạn nào của Nephron và gây ra tác dụng phụ điện giải gì?',
            'back': 'Tác động vào <b>Ống lượn gần (PCT)</b>.<br>Hậu quả: Ức chế tái hấp thu HCO3-, làm HCO3- thải ra nước tiểu ồ ạt → Gây <b>Toan chuyển hóa (Metabolic acidosis)</b>.',
            'tag': 'DuocLy'
        },
        {
            'front': 'Đặc điểm "kỳ lạ" nhất của Nhánh lên dày Quai Henle (TAL) là gì và nó sử dụng bơm ion nào?',
            'back': 'Đặc điểm: <b>Hoàn toàn không thấm nước</b>, chỉ bơm muối ra ngoài tủy thận.<br>Bơm ion: <b>NKCC2 (Na-K-2Cl Cotransporter)</b>.',
            'tag': 'SinhLy'
        },
        {
            'front': 'Lợi tiểu quai (Furosemide) ức chế bơm nào, ở đâu, và gây ra hậu quả điện giải gì?',
            'back': 'Ức chế bơm <b>NKCC2</b> tại Nhánh lên dày Quai Henle (TAL).<br>Hậu quả: Mất Na+ và nước ồ ạt, <b>Hạ Kali máu</b>, <b>Hạ Canxi máu</b> và <b>Hạ Magie máu</b>.',
            'tag': 'DuocLy'
        },
        {
            'front': 'Nhóm Thiazide ức chế bơm nào, ở đoạn nào của Nephron, và có điểm gì khác biệt về Canxi so với Lợi tiểu quai?',
            'back': 'Ức chế bơm <b>NCC</b> tại Ống lượn xa (DCT).<br>Khác biệt: Thiazide làm <b>TĂNG tái hấp thu Canxi vào máu</b> (giữ Canxi lại), trong khi Lợi tiểu quai làm mất Canxi ra nước tiểu.',
            'tag': 'DuocLy'
        },
        {
            'front': 'Bơm ENaC tại Ống góp chịu sự chiết phối của hormone nào và có quy tắc trao đổi ion như thế nào?',
            'back': 'Chịu chiết phối của <b>Aldosterone</b>.<br>Quy tắc: <b>"Hút 1 Na+ vào máu thì phải vứt 1 K+ hoặc 1 H+ ra nước tiểu"</b>.',
            'tag': 'SinhLy'
        },
        {
            'front': 'Nhóm Lợi tiểu tiết kiệm Kali (như Spironolactone) gây ra tác dụng phụ điện giải nguy hiểm nào?',
            'back': 'Gây <b>TĂNG Kali máu (Hyperkalemia)</b> và Toan máu. (Do chặn Aldosterone/ENaC, không hút được Na+ vào nên không vứt được K+ và H+ ra).',
            'tag': 'DuocLy'
        },
        {
            'front': 'Chiến lược Khóa Nephron nối tiếp (Sequential Nephron Blockade - SNB) là gì và dùng khi nào?',
            'back': 'Là sự kết hợp <b>Lợi tiểu quai (đánh Trạm 3) + Thiazide (đánh Trạm 4)</b>.<br>Chỉ định: Khi bệnh nhân bị <b>Kháng lợi tiểu quai</b> (tế bào DCT phì đại vớt lại Na+ bị xổng từ quai Henle).',
            'tag': 'LamSang'
        },
        {
            'front': 'Tại sao bệnh nhân đang dùng lợi tiểu quai lại MẤT TÁC DỤNG thuốc khi uống thêm NSAIDs (Ibuprofen)?',
            'back': 'NSAIDs ức chế tổng hợp Prostaglandin ở thận, làm co tiểu động mạch đến, <b>giảm lượng máu tới thận</b> → Làm thuốc lợi tiểu quai không đến được vị trí tác dụng và mất hiệu quả.',
            'tag': 'LamSang'
        },
        {
            'front': 'Kể tên 4 Dấu hiệu báo động (Red Flags) cần dừng lợi tiểu ngay lập tức.',
            'back': '1. Creatinine máu tăng nhanh (Suy thận cấp trước thận).<br>2. Chuột rút, yếu cơ (Hạ Kali máu nặng).<br>3. Lú lẫn, ngủ gà (Hạ Natri máu nặng).<br>4. Vô niệu (Anuria).',
            'tag': 'RedFlags'
        }
    ])

    deck_name = "IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu"
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
    deck = genanki.Deck(deck_id, deck_name, description="Bộ thẻ ôn tập Sinh lý Nephron & Thuốc lợi tiểu - Tone Hồng")

    for i, card in enumerate(cards):
        note = genanki.Note(
            model=model,
            fields=[card['front'], card['back'], f'<span class="tag">Nephron</span> <span class="tag">{card["tag"]}</span>'],
            guid=stable_id(f"Nephron_card_{i}")
        )
        deck.add_note(note)

    out_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu' / f'Anki - {deck_name}.apkg'
    genanki.Package(deck).write_to_file(str(out_path))
    print(f"✅ Đã tạo thành công bộ flashcard tone hồng: {out_path}")
    print(f"Tổng số thẻ: {len(cards)}")

if __name__ == "__main__":
    build_apkg()
