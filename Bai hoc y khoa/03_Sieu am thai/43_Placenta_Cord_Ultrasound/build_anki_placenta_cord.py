"""Build Anki APKG from Placenta & Cord Ultrasound cards JSON."""
import sys

sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-11"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\43_Placenta_Cord_Ultrasound"

basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\Placenta_Cord_Ultrasound_{DATE}.cards.v2.json",
    basic_model_id=5498765461,
    cloze_model_id=5498765462,
    basic_model_name=f"Placenta Cord Basic {DATE}",
    cloze_model_name=f"Placenta Cord Cloze {DATE}",
    deck_id=5498765460,
    deck_name="Sieu am thai - Banh nhau & Day ron",
    deck_description=f"Placenta previa, PAS, vasa previa, cord insertion, SUA — {DATE}",
    output_path=rf"{DIR}\Anki - Placenta_Cord_Ultrasound_{DATE} - {DATE}.apkg",
)

print(f"[OK] {basic} basic + {cloze} cloze = {basic + cloze} cards")
