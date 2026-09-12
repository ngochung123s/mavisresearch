"""Build Anki APKG from BI-RADS Breast US Atlas cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-11"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\04_Sieu am tong quat\03_Sieu_am_tuyen_vu"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\BI-RADS_Sieu_am_vu_Atlas_{DATE}.cards.v2.json",
    basic_model_id=5498765432, cloze_model_id=5498765433,
    basic_model_name=f"BI-RADS Breast Basic {DATE}", cloze_model_name=f"BI-RADS Breast Cloze {DATE}",
    deck_id=5498765431, deck_name="Sieu am vu - BI-RADS Atlas & Tinh diem",
    deck_description=f"BI-RADS US breast scoring — {DATE}",
    output_path=rf"{DIR}\Anki - BI-RADS_Sieu_am_vu_Atlas_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
