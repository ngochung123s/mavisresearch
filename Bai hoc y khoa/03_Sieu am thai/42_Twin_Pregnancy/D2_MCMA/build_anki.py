"""Build Anki APKG from MCMA cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-05"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\42_Twin_Pregnancy\D2_MCMA"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\MCMA_{DATE}.cards.v2.json",
    basic_model_id=7098765432, cloze_model_id=7098765433,
    basic_model_name=f"MCMA Basic {DATE}", cloze_model_name=f"MCMA Cloze {DATE}",
    deck_id=7098765431, deck_name="Twin - D2 - MCMA - Song thai 1 buong oi",
    deck_description=f"MCMA management & follow-up — {DATE}",
    output_path=rf"{DIR}\Anki - MCMA_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
