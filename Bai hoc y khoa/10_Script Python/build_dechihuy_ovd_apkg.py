"""Build APKG cho De chi huy (OVD) lesson - 23/06/2026."""
from pathlib import Path
import sys

sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\01_San phu khoa\07_De_chi_huy_OVD\de_chi_huy_ovd_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - De chi huy OVD 20 cards - 2026-06-23.apkg'

MODEL_ID = 1707001236001
DECK_ID = 1707001236002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='DeChiHuy_OVD_Pastel',
    deck_id=DECK_ID,
    deck_name='SanKhoa::DeChiHuy_OVD::2026-06-23',
    deck_description='Đẻ chỉ huy (Operative Vaginal Delivery) - 23/06/2026',
)

n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='DeChiHuy OVD Vacuum Forceps SanKhoa',
)

write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
