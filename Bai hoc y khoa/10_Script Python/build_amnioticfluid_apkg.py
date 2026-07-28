"""Build APKG cho bai hoc Bat thuong nuoc oi - 27/06/2026.
Su dung lesson_builder voi Pastel theme.
"""
from pathlib import Path
import sys

sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\Amniotic_Fluid_Abnormalities_2026-06-27.cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Bat thuong nuoc oi 25 cards - 2026-06-27.apkg'

MODEL_ID = 1707025026001
DECK_ID = 1707025026002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='Amniotic_Fluid_Pastel',
    deck_id=DECK_ID,
    deck_name='OB-GYN::Amniotic_Fluid::Oligo_Polyhydramnios::2026-06-27',
    deck_description='Bat thuong nuoc oi - Thieu oi & Da oi - 27/06/2026',
)

n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='amniotic fluid oligohydramnios polyhydramnios AFI SDP ultrasound SMFM ISUOG ACOG',
)

write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
