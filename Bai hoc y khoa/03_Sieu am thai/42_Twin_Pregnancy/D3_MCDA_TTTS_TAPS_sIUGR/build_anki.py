"""Build Anki APKG from MCDA TTTS TAPS sIUGR cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-06"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\42_Twin_Pregnancy\D3_MCDA_TTTS_TAPS_sIUGR"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\MCDA_TTTS_TAPS_sIUGR_{DATE}.cards.v2.json",
    basic_model_id=8098765432, cloze_model_id=8098765433,
    basic_model_name=f"MCDA Basic {DATE}", cloze_model_name=f"MCDA Cloze {DATE}",
    deck_id=8098765431, deck_name="Twin - D3 - MCDA TTTS TAPS sIUGR",
    deck_description=f"MCDA complications — {DATE}",
    output_path=rf"{DIR}\Anki - MCDA_TTTS_TAPS_sIUGR_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
