"""Build Anki APKG from Chorionicity & Amnionicity cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-05"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\42_Twin_Pregnancy\D1_Chorionicity_Amnionicity"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=rf"{DIR}\Chorionicity_Amnionicity_{DATE}.cards.v2.json",
    basic_model_id=6098765432, cloze_model_id=6098765433,
    basic_model_name=f"Chorionicity Basic {DATE}",
    cloze_model_name=f"Chorionicity Cloze {DATE}",
    deck_id=6098765431,
    deck_name="Twin - D1 - Chorionicity & Amnionicity",
    deck_description=f"Xac dinh chorionicity amnionicity song thai — {DATE}",
    output_path=rf"{DIR}\Anki - Chorionicity_Amnionicity_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
