"""Build Anki APKG from HPV cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-06"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\05_Vi sinh - Mien dich\V4_HPV"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\HPV_{DATE}.cards.v2.json",
    basic_model_id=3498765432, cloze_model_id=3498765433,
    basic_model_name=f"HPV Basic {DATE}", cloze_model_name=f"HPV Cloze {DATE}",
    deck_id=3498765431, deck_name="Vi sinh - V4 - HPV & Du phong ung thu CTC",
    deck_description=f"HPV screening vaccination CIN colposcopy — {DATE}",
    output_path=rf"{DIR}\Anki - HPV_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
