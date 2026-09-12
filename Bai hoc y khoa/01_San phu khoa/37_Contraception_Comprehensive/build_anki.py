"""Build Anki APKG from Contraception Comprehensive cards JSON.

NOTE: model/deck IDs kept stable across runs so existing user decks remain in sync.
"""
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-13"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\37_Contraception_Comprehensive"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\Contraception_Comprehensive_{DATE}.cards.v2.json",
    basic_model_id=4498765432, cloze_model_id=4498765433,
    basic_model_name=f"Contraception Basic {DATE}", cloze_model_name=f"Contraception Cloze {DATE}",
    deck_id=4498765431, deck_name="OBGYN - Tranh thai toan dien ADR & Xu tri",
    deck_description=f"Contraception methods ADR emergency - {DATE}",
    output_path=rf"{DIR}\Anki - Contraception_Comprehensive_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")