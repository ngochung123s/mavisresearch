#!/usr/bin/env python3
"""
build_pink_apkg_viem_tuy.py — Build APKG tone hồng cho bài Viêm tụy cấp.
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
.cloze, .cloze-b {
  font-weight: 700;
  color: #d1495b;
  background: rgba(255, 182, 193, 0.3);
  padding: 1px 4px;
  border-radius: 3px;
}
.card.nightMode .cloze, .card.nightMode .cloze-b {
  color: #ffb6c1;
  background: rgba(255, 182, 193, 0.2);
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

def build_pink_apkg():
    # Load JSON files
    json_path_v2 = PROJECT_ROOT / '11_Noi khoa' / 'IM-42a_Viem_tuy_cap' / 'IM-42a_Viem_tuy_cap_2026-07-23_RELEASE_v1.cards.v2.json'
    json_path_cloze = PROJECT_ROOT / '11_Noi khoa' / 'IM-42a_Viem_tuy_cap' / 'IM-42a_Viem_tuy_cap_cards.json'
    
    cards_basic = []
    cards_cloze = []
    
    # Parse basic cards
    if json_path_v2.exists():
        with open(json_path_v2, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if item.get('card_type') == 'Basic' or 'front' in item:
                    cards_basic.append(item)
    
    # Parse cloze cards
    if json_path_cloze.exists():
        with open(json_path_cloze, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if item.get('type') == 'cloze' or 'question' in item:
                    cards_cloze.append(item)

    # Build Deck
    deck_name = "IM-42a_Viem_tuy_cap_Tone_Hong"
    deck_id = stable_id(deck_name + "deck")
    deck = genanki.Deck(deck_id, deck_name, description="Bộ thẻ ôn tập Viêm tụy cấp (IM-42a) - Tone Hồng")
    
    # Basic Model
    basic_model_id = stable_id(deck_name + "basic_model")
    basic_model = genanki.Model(
        basic_model_id,
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
    
    # Cloze Model
    cloze_model_id = stable_id(deck_name + "cloze_model")
    cloze_model = genanki.Model(
        cloze_model_id,
        f"Pink Cloze Model - {deck_name}",
        model_type=genanki.Model.CLOZE,
        fields=[{'name': 'Text'}, {'name': 'Extra'}, {'name': 'Tags'}],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '<div id="front">{{cloze:Text}}</div>',
                'afmt': '<div id="front">{{cloze:Text}}</div><hr id="answer"><div id="back">{{Extra}}</div><br>{{Tags}}',
            }
        ],
        css=PINK_CSS
    )

    # Add Basic Cards
    for i, card in enumerate(cards_basic):
        tags_html = " ".join([f'<span class="tag">{t}</span>' for t in card.get('tag', ['VTC'])])
        note = genanki.Note(
            model=basic_model,
            fields=[card['front'], card['back'], tags_html],
            guid=stable_id(f"VTC_basic_{i}")
        )
        deck.add_note(note)
        
    # Add Cloze Cards
    for i, card in enumerate(cards_cloze):
        tags_html = '<span class="tag">VTC</span> <span class="tag">Cloze</span>'
        note = genanki.Note(
            model=cloze_model,
            fields=[card.get('question', ''), card.get('extra', ''), tags_html],
            guid=stable_id(f"VTC_cloze_{i}")
        )
        deck.add_note(note)

    out_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-42a_Viem_tuy_cap' / f'Anki - {deck_name}.apkg'
    genanki.Package(deck).write_to_file(str(out_path))
    print(f"✅ Đã tạo thành công bộ flashcard tone hồng: {out_path}")
    print(f"Tổng số thẻ Basic: {len(cards_basic)}")
    print(f"Tổng số thẻ Cloze: {len(cards_cloze)}")
    print(f"Tổng cộng: {len(cards_basic) + len(cards_cloze)} thẻ")

if __name__ == "__main__":
    build_pink_apkg()
