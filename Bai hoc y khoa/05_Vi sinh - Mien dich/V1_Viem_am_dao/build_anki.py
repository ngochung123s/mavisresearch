"""Build Anki APKG from Viem am dao cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-06"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\05_Vi sinh - Mien dich\V1_Viem_am_dao"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\Viem_am_dao_{DATE}.cards.v2.json",
    basic_model_id=2498765432, cloze_model_id=2498765433,
    basic_model_name=f"Vaginitis Basic {DATE}", cloze_model_name=f"Vaginitis Cloze {DATE}",
    deck_id=2498765431, deck_name="Vi sinh - V1 - Viem am dao BV Candida Trichomonas",
    deck_description=f"Vaginitis diagnosis & treatment — {DATE}",
    output_path=rf"{DIR}\Anki - Viem_am_dao_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
