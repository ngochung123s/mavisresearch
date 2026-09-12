"""Build APKG cho bai hoc Sieu am o bung tong quat - 28/06/2026."""
from pathlib import Path
import sys
sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')
from lesson_builder import build_pastel_model_and_deck, add_cards_from_json, write_apkg

CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\04_Sieu am tong quat\01_Sieu_am_o_bung_tong_quat\Sieu_am_o_bung_tong_quat_2026-06-28.cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\04_Sieu am tong quat\01_Sieu_am_o_bung_tong_quat\Anki - Sieu am o bung 20 cards - 2026-06-28.apkg'

model, deck = build_pastel_model_and_deck(
    model_id=1707025026068,
    model_name='Abdomen_US_Pastel',
    deck_id=1707025026069,
    deck_name='Imaging::Abdomen_US::General::2026-06-28',
    deck_description='Sieu am o bung tong quat - 7 tang (gan, tui mat, tuy, lach, than, bang quang, dong mach chu) - 28/06/2026',
)

n_cards = add_cards_from_json(
    deck=deck, model=model, cards_json_path=CARDS_JSON,
    tags='abdominal ultrasound liver gallbladder pancreas spleen kidney bladder aorta',
)

write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
