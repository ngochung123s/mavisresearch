"""Build Anki APKG from ART Endocrine Markers cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-06"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\43_ART_Endocrine_Markers"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\ART_Endocrine_Markers_{DATE}.cards.v2.json",
    basic_model_id=1498765432, cloze_model_id=1498765433,
    basic_model_name=f"ART Endocrine Basic {DATE}", cloze_model_name=f"ART Endocrine Cloze {DATE}",
    deck_id=1498765431, deck_name="ART - 4 chi so noi tiet AMH FSH E2 P4 LH",
    deck_description=f"Noi tiet ART AMH FSH E2 P4 LH — {DATE}",
    output_path=rf"{DIR}\Anki - ART_Endocrine_Markers_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
