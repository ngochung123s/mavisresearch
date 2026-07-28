"""Build APKG cho Doppler Van Tim Thai (Mechanism supplement) - recover 24/06 -> 25/06/2026."""
import sys

sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\03_Sieu am thai\Doppler_Val_Tim_Thai_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\Anki - Doppler Van Tim Thai 22 cards - 2026-06-24.apkg'

# Model + Deck IDs (random, persistent)
MODEL_ID = 1707001237001
DECK_ID = 1707001237002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='DopplerVanTimThai_Pastel',
    deck_id=DECK_ID,
    deck_name='SieuAmThai::DopplerVanTimThai::2026-06-24',
    deck_description='Cơ chế Doppler qua van tim thai + Waveform Morphology - 24/06/2026 (recover 25/06)',
)

n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='Doppler ValTimThai SieuAmThai FMF Waveform',
)

write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
