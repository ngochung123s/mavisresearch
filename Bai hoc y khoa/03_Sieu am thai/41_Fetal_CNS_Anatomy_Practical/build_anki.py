"""Build Anki APKG from Fetal CNS Anatomy Practical cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")

from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-04"
LESSON_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\41_Fetal_CNS_Anatomy_Practical"

JSON_IN = rf"{LESSON_DIR}\Fetal_CNS_Anatomy_Practical_{DATE}.cards.v2.json"
APKG_OUT = rf"{LESSON_DIR}\Anki - Fetal_CNS_Anatomy_Practical_{DATE} - {DATE}.apkg"

DECK_NAME = "Fetal CNS Anatomy - Khao sat giai phau than kinh thai"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=JSON_IN,
    basic_model_id=3098765432,
    cloze_model_id=3098765433,
    basic_model_name=f"Fetal CNS Anatomy Basic {DATE}",
    cloze_model_name=f"Fetal CNS Anatomy Cloze {DATE}",
    deck_id=3098765431,
    deck_name=DECK_NAME,
    deck_description=f"Khao sat giai phau he than kinh thai nhi tren sieu am — {DATE}",
    output_path=APKG_OUT,
)

print(f"\n[OK] APKG: {APKG_OUT}")
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
