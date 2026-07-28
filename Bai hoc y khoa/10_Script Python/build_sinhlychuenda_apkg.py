"""Build APKG cho Sinh ly chuyen da & Do de lesson - 23/06/2026."""
from pathlib import Path
import sys

# Add script dir to path
sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

# Config
CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\01_San phu khoa\05_Sinh_ly_chuyen_da_Do_de\sinhl y_chuyen_da_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Sinh ly chuyen da & Do de 20 cards - 2026-06-23.apkg'

# Model + Deck IDs (random, persistent)
MODEL_ID = 1707001235001
DECK_ID = 1707001235002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='SinhLyChuyenDa_Pastel',
    deck_id=DECK_ID,
    deck_name='SanKhoa::SinhLyChuyenDa::2026-06-23',
    deck_description='Sinh lý chuyển dạ & Hướng dẫn đỡ đẻ - 23/06/2026',
)

# Add cards
n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='ChuyenDa DoDe SanKhoa',
)

# Write
write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
