"""Build APKG cho U xo tu cung - Leiomyoma (2026-06-27)."""
import sys

sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
)

CARDS_JSON = r'F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\01_San phu khoa\07_U_xo_tu_cung_Leiomyoma\U_xo_tu_cung_Leiomyoma_cards.json'
OUTPUT_APKG = r'F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\07_U_xo_tu_cung_Leiomyoma\Anki - U xo tu cung Leiomyoma 25 cards - 2026-06-27.apkg'

# Model + Deck IDs (random, persistent)
MODEL_ID = 1707006272701
DECK_ID = 1707006272702

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='UXoTuCungLeiomyoma_Pastel',
    deck_id=DECK_ID,
    deck_name='SanPhuKhoa::UXoTuCungLeiomyoma::2026-06-27',
    deck_description='U xo tu cung va anh huong den ART - Phan loai FIGO + Co che + Dieu tri + Meta-analysis 2021-2026',
)

n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='UXoTuCung Leiomyoma FIGO ART IVF Myomectomy Linzagolix TRFA EndometrialReceptivity',
)

write_apkg(deck, OUTPUT_APKG)
print(f'  [APKG] Saved {n_cards} cards: {OUTPUT_APKG}')
