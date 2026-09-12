# -*- coding: utf-8 -*-
"""Build Anki APKG from Semen Analysis Male Infertility cards JSON."""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")

from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-13"
LESSON_DIR = r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\44_Semen_Analysis_Male_Infertility"

JSON_IN = rf"{LESSON_DIR}\Semen_Analysis_Male_Infertility_{DATE}.cards.v2.json"
APKG_OUT = rf"{LESSON_DIR}\Anki - Semen_Analysis_Male_Infertility_{DATE} - {DATE}.apkg"

basic_count, cloze_count = add_cards_from_json_v2(
    json_path=JSON_IN,
    basic_model_id=4407130002,
    cloze_model_id=4407130003,
    basic_model_name=f"Semen Analysis Male Infertility Basic {DATE}",
    cloze_model_name=f"Semen Analysis Male Infertility Cloze {DATE}",
    deck_id=4407130001,
    deck_name="ART - Tinh dich do trong vo sinh nam",
    deck_description=f"Tinh dich do, vo sinh nam va ART — WHO 2021, AUA/ASRM 2024, EAU 2026 — {DATE}",
    output_path=APKG_OUT,
)

print(f"\n[OK] APKG: {APKG_OUT}")
print(f"[OK] {basic_count} basic + {cloze_count} cloze = {basic_count + cloze_count} cards")
