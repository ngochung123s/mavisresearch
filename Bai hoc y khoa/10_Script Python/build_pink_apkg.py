#!/usr/bin/env python3
"""
build_pink_apkg.py — Build APKG với tone hồng (Pink theme) cho bài IBS.
"""
import sys
import re
import hashlib
import json
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

def build_pink_model_and_deck(model_id, model_name, deck_id, deck_name, deck_description):
    model = genanki.Model(
        model_id,
        model_name,
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
    deck = genanki.Deck(deck_id, deck_name, description=deck_description)
    return model, deck

def stable_id(seed_str):
    h = hashlib.md5(seed_str.encode()).hexdigest()[:12]
    return int(h, 16) % 9000000000000 + 1000000000000

def build_ibs_pink_apkg():
    # Since the QA file doesn't have a standard Q: A: format, we'll create cards from the Master Cases
    qa_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-IBS_Hoi_chung_ruot_kich_thich' / 'QA-IBS_Master_Cases_va_Pocket_Guide.md'
    with open(qa_path, 'r', encoding='utf-8') as f:
        content = f.read()

    cards = []
    
    # Extract Case 1
    cards.append({
        'front': '<b>CA LÂM SÀNG 1:</b> IBS thể Tiêu chảy (IBS-D) thất bại với Loperamide kéo dài.<br>Tại sao bệnh nhân uống Loperamide kéo dài lại làm bụng đau quặn nhiều hơn và rất trướng?',
        'back': 'Loperamide chỉ là thuốc liệt nhu động làm rắn phân cấp thời, <b>không giải quyết được bản chất Tăng nhạy cảm tạng và Rối loạn Trục Não - Ruột</b>. Việc tự ý uống Loperamide kéo dài làm ứ trệ hơi và chất thải, gây căng trướng đại tràng và làm tăng cảm giác đau quặn.'
    })
    
    # Extract Case 2
    cards.append({
        'front': '<b>CA LÂM SÀNG 2:</b> IBS thể Táo bón (IBS-C).<br>Tại sao dùng Chất xơ Không hòa tan (Insoluble fiber — cám lúa mì, rau thô) lại làm trầm trọng thêm tình trạng đau bụng và trướng bụng?',
        'back': 'Loại chất xơ này gây ma sát cơ học lên niêm mạc đại tràng đang bị nhạy cảm và bị vi khuẩn lên men sinh khí mạnh mẽ → <b>Làm trầm trọng thêm tình trạng đau bụng và trướng bụng</b>. Cần chuyển sang Chất xơ Hòa tan (Soluble fiber) như Psyllium.'
    })
    
    # Extract Case 3
    cards.append({
        'front': '<b>CA LÂM SÀNG 3:</b> IBS sau Nhiễm trùng (Post-Infectious IBS / PI-IBS).<br>Cơ chế bệnh sinh chính của PI-IBS là gì?',
        'back': 'Nhiễm trùng tiêu hóa cấp tính làm tổn thương hàng rào niêm mạc ruột, dẫn đến <b>viêm vi thể kéo dài (Low-grade inflammation)</b> và tăng tính thấm niêm mạc. Điều này kích hoạt các tế bào miễn dịch (Mast cells) giải phóng hóa chất trung gian, làm tăng nhạy cảm các tận cùng thần kinh ruột.'
    })
    
    # Extract Case 4
    cards.append({
        'front': '<b>CA LÂM SÀNG 4:</b> Bệnh nhân giả IBS có Dấu hiệu Báo động (Red Flags).<br>Kể tên các Dấu hiệu Báo động (Red Flags) cần loại trừ trước khi chẩn đoán IBS.',
        'back': '1. Sụt cân không chủ ý.<br>2. Đi tiêu ra máu.<br>3. Triệu chứng xuất hiện về đêm (đánh thức bệnh nhân).<br>4. Khởi phát triệu chứng sau 50 tuổi.<br>5. Tiền sử gia đình có ung thư đại trực tràng, IBD, hoặc bệnh Celiac.<br>6. Thiếu máu, CRP tăng, hoặc Calprotectin phân tăng.'
    })

    # Build Deck
    deck_name = "IBS-AI tự tạo"
    model_id = stable_id(deck_name + "model")
    deck_id = stable_id(deck_name + "deck")
    
    model, deck = build_pink_model_and_deck(
        model_id, 
        f"Pink Basic Model - {deck_name}", 
        deck_id, 
        deck_name, 
        "Bộ thẻ ôn tập Hội chứng ruột kích thích (IBS) - Tone Hồng"
    )

    for i, card in enumerate(cards):
        note = genanki.Note(
            model=model,
            fields=[card['front'], card['back'], '<span class="tag">IBS</span> <span class="tag">Case-Study</span>'],
            guid=stable_id(f"IBS_card_{i}")
        )
        deck.add_note(note)

    out_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-IBS_Hoi_chung_ruot_kich_thich' / f'Anki - {deck_name}.apkg'
    genanki.Package(deck).write_to_file(str(out_path))
    print(f"✅ Đã tạo thành công bộ flashcard tone hồng: {out_path}")
    print(f"Tổng số thẻ: {len(cards)}")

if __name__ == "__main__":
    build_ibs_pink_apkg()
