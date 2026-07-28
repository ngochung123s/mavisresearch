"""Build APKG cho Luteal Phase Support lesson - 22/06/2026.

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
CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\02_Ho tro sinh san ART\12_Luteal_Phase_Support\lps_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Ho tro pha hoang the Luteal Phase Support 20 cards - 2026-06-22.apkg'

# Model + Deck IDs (random, persistent)
MODEL_ID = 1707001234001  # custom ID for this lesson
DECK_ID = 1707001234002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='LPS_ART_Pastel',
    deck_id=DECK_ID,
    deck_name='ART::LPS::2026-06-22',
    deck_description='Luteal Phase Support trong ART - 22/06/2026',
)

# Add cards
n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='LPS ART Progesterone',
)

# Write
write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
