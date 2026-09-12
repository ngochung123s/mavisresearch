"""Build Anki APKG from Polyp Buong Tu Cung cards JSON."""
import sys
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-11"
DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\38_Polyp_Buong_Tu_Cung"
basic, cloze = add_cards_from_json_v2(
    json_path=rf"{DIR}\Polyp_Buong_Tu_Cung_{DATE}.cards.v2.json",
    basic_model_id=5498765451, cloze_model_id=5498765452,
    basic_model_name=f"Polyp Buong Tu Cung Basic {DATE}", cloze_model_name=f"Polyp Buong Tu Cung Cloze {DATE}",
    deck_id=5498765450, deck_name="SPK - Polyp buong tu cung (Endometrial Polyp)",
    deck_description=f"Polyp buong tu cung — chan doan, phan biet, quan ly — {DATE}",
    output_path=rf"{DIR}\Anki - Polyp_Buong_Tu_Cung_{DATE} - {DATE}.apkg",
)
print(f"[OK] {basic} basic + {cloze} cloze = {basic+cloze} cards")
