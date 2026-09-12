"""Build Anki APKG from DCDA Monitoring cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-06"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\42_Twin_Pregnancy\D4_DCDA_Monitoring"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\DCDA_Monitoring_{DATE}.cards.v2.json",
    basic_model_id=9098765432, cloze_model_id=9098765433,
    basic_model_name=f"DCDA Basic {DATE}", cloze_model_name=f"DCDA Cloze {DATE}",
    deck_id=9098765431, deck_name="Twin - D4 - DCDA Theo doi & Sinh",
    deck_description=f"DCDA monitoring & delivery — {DATE}",
    output_path=rf"{DIR}\Anki - DCDA_Monitoring_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
