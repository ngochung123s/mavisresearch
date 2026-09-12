"""Build Anki APKG from Scrotal Ultrasound Male Infertility cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")

from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-05"
LESSON_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\42_Scrotal_Ultrasound_Male_Infertility"

JSON_IN = rf"{LESSON_DIR}\Scrotal_Ultrasound_Male_Infertility_{DATE}.cards.v2.json"
APKG_OUT = rf"{LESSON_DIR}\Anki - Scrotal_Ultrasound_Male_Infertility_{DATE} - {DATE}.apkg"

DECK_NAME = "ART - Sieu am bieu & TRUS trong vo sinh nam"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=JSON_IN,
    basic_model_id=4098765432,
    cloze_model_id=4098765433,
    basic_model_name=f"Scrotal US Male Infertility Basic {DATE}",
    cloze_model_name=f"Scrotal US Male Infertility Cloze {DATE}",
    deck_id=4098765431,
    deck_name=DECK_NAME,
    deck_description=f"Sieu am he sinh duc nam trong ho tro sinh san — {DATE}",
    output_path=APKG_OUT,
)

print(f"\n[OK] APKG: {APKG_OUT}")
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
