"""Build Anki APKG from Menstrual Cycle Mastery cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")

from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-05"
LESSON_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\36_Menstrual_Cycle_Mastery"

JSON_IN = rf"{LESSON_DIR}\Menstrual_Cycle_Mastery_{DATE}.cards.v2.json"
APKG_OUT = rf"{LESSON_DIR}\Anki - Menstrual_Cycle_Mastery_{DATE} - {DATE}.apkg"

DECK_NAME = "OBGYN - Lam chu kinh nguyet - Kiem soat chu ky"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=JSON_IN,
    basic_model_id=5098765432,
    cloze_model_id=5098765433,
    basic_model_name=f"Menstrual Mastery Basic {DATE}",
    cloze_model_name=f"Menstrual Mastery Cloze {DATE}",
    deck_id=5098765431,
    deck_name=DECK_NAME,
    deck_description=f"Sinh ly HPO + kiem soat kinh nguyet bang noi tiet — {DATE}",
    output_path=APKG_OUT,
)

print(f"\n[OK] APKG: {APKG_OUT}")
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
