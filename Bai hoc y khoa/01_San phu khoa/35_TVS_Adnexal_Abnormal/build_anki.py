"""Build Anki APKG from TVS_Adnexal_Abnormal cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")

from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-04"
LESSON_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\35_TVS_Adnexal_Abnormal"

JSON_IN = rf"{LESSON_DIR}\TVS_Adnexal_Abnormal_{DATE}.cards.v2.json"
APKG_OUT = rf"{LESSON_DIR}\Anki - TVS_Adnexal_Abnormal_{DATE} - {DATE}.apkg"

DECK_NAME = "TVS - Phan biet cau truc bat thuong phan phu"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=JSON_IN,
    basic_model_id=2098765432,
    cloze_model_id=2098765433,
    basic_model_name=f"TVS Adnexal Basic {DATE}",
    cloze_model_name=f"TVS Adnexal Cloze {DATE}",
    deck_id=2098765431,
    deck_name=DECK_NAME,
    deck_description=f"Phan biet cac cau truc bat thuong phan phu tren sieu am TVS — {DATE}",
    output_path=APKG_OUT,
)

print(f"\n[OK] APKG: {APKG_OUT}")
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
