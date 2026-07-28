"""Build APKG cho bai hoc Stimulation Protocols ART - 25/06/2026.
Su dung lesson_builder voi Pastel theme.
"""
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
CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\02_Ho tro sinh san ART\14_Stimulation_Protocols\stimulation_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Cac phac do kich trung ART 30 cards - 2026-06-25.apkg'

# Model + Deck IDs (random, persistent)
MODEL_ID = 1707025025001
DECK_ID = 1707025025002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='Stimulation_Protocols_ART_Pastel',
    deck_id=DECK_ID,
    deck_name='ART::Stimulation_Protocols::2026-06-25',
    deck_description='Cac phac do kich trung ART hien dai - 25/06/2026',
)

# Add cards
n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='Stimulation Protocols ART Antagonist Agonist PPOS DuoStim',
)

# Write
write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
