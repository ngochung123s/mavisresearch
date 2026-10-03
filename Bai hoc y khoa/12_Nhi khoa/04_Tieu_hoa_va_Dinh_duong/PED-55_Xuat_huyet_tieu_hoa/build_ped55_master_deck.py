# -*- coding: utf-8 -*-
"""
build_ped55_master_deck.py
Đóng gói bộ thẻ Anki MASTER BAREM cho PED-55 Xuất huyết tiêu hóa ở trẻ em:
- Track: BAREM GỐC Y THÁI BÌNH (Giáo trình Nhi khoa Trang 87 - 99).
- Quy chuẩn: atomic, back <= 3-4 dòng, 100% Unicode, escape '<'.
- Deck Name: "Nhi khoa Y6::PED-55: Xuất huyết tiêu hóa ở trẻ em"
- Deck ID: 1709132055
- Post-build verify: notes == input cards.
"""
import json
import re
import sqlite3
import sys
import tempfile
import zipfile
from pathlib import Path

import genanki

TARGET_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TARGET_DIR))
from ped55_cards_data import cards_data  # noqa: E402

DECK_ID = 1709132055
DECK_NAME = "Nhi khoa Y6::PED-55: Xuất huyết tiêu hóa ở trẻ em"
JSON_PATH = TARGET_DIR / "PED-55_Xuat_huyet_tieu_hoa_MASTER_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-55_Xuat_huyet_tieu_hoa_MASTER_v1.apkg"
from collections import Counter

REQUIRED_SECTIONS = [
    "B1",
    "B2_1", "B2_2", "B2_3", "B2_4", "B2_5",
    "B3_1", "B3_2", "B3_3",
    "B4_1", "B4_2",
    "B5_1", "B5_2", "B5_3", "B5_4", "B5_5", "B5_6",
    "B6_1", "B6_2", "B6_3", "B6_4", "B6_5", "B6_6", "B6_7", "B6_8"
]

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #0b1120;
  padding: 20px;
  max-width: 680px;
  margin: 0 auto;
  border-radius: 12px;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 12px;
  background-color: rgba(245, 158, 11, 0.18);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 12px;
}
.cloze {
  font-weight: 700;
  color: #fbbf24;
  border-bottom: 2px solid #d97706;
  padding: 0 2px;
}
hr#answer {
  border: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(245, 158, 11, 0.4), transparent);
  margin: 16px 0;
}
.answer-box {
  background-color: rgba(15, 23, 42, 0.6);
  border-left: 3px solid #fbbf24;
  border-radius: 8px;
  padding: 12px 16px;
  margin-top: 10px;
  color: #f1f5f9;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.04);
  border-left: 3px solid #f59e0b;
  font-size: 14px;
  color: #cbd5e1;
}
.extra-title {
  font-weight: 700;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 4px;
  color: #fbbf24;
}
"""

BASIC_MODEL = genanki.Model(
    1709551001,
    "PED55_Master_Basic",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
    ],
    templates=[{
        "name": "PED55 Master Basic",
        "qfmt": '<div class="badge">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & Barem:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)

CLOZE_MODEL = genanki.Model(
    1709551002,
    "PED55_Master_Cloze",
    model_type=genanki.Model.CLOZE,
    fields=[
        {"name": "Text"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
    ],
    templates=[{
        "name": "PED55 Master Cloze",
        "qfmt": '<div class="badge">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div>',
        "afmt": '<div class="badge">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div><hr id="answer">{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & Barem:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr)\b)", "&lt;", text)


def main() -> int:
    print(f"=== BUILD PED-55 MASTER DECK: '{DECK_NAME}' ===")
    print(f"Total input cards: {len(cards_data)}")
    # 0. Exhaustive Barem Coverage Gate (Zero-Omission)
    have = Counter(c.get("section") for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[BLOCK] Exhaustive Barem Coverage Failed! Missing sections: {missing}")
        return 2
    print(f"[GATE PASS] Exhaustive Barem Coverage: All {len(REQUIRED_SECTIONS)} sections covered (0 missing).")


    # 1. Xuất JSON
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(cards_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved cards JSON: {JSON_PATH.name}")

    # 2. Khởi tạo Deck
    deck = genanki.Deck(DECK_ID, DECK_NAME)

    added_notes = 0
    for card in cards_data:
        card_type = card.get("type", "basic")
        category = card.get("category", "Xuất huyết tiêu hóa")
        badge = "BAREM GỐC Y THÁI BÌNH"
        extra = escape_angle_brackets(card.get("extra", ""))
        tags = card.get("tags", ["PED-55", "Barem-goc"])

        if card_type == "cloze":
            text = escape_angle_brackets(card["text"])
            note = genanki.Note(
                model=CLOZE_MODEL,
                fields=[text, extra, category, badge],
                tags=tags,
                guid=genanki.guid_for(f"ped55-barem-{card['id']}"),
            )
        else:
            front = escape_angle_brackets(card["front"])
            back = card["back"]
            note = genanki.Note(
                model=BASIC_MODEL,
                fields=[front, back, extra, category, badge],
                tags=tags,
                guid=genanki.guid_for(f"ped55-barem-{card['id']}"),
            )

        deck.add_note(note)
        added_notes += 1

    # 3. Đóng gói APKG
    package = genanki.Package(deck)
    package.write_to_file(str(APKG_PATH))
    print(f"[OK] Generated APKG: {APKG_PATH.name} ({APKG_PATH.stat().st_size} bytes)")

    # 4. Kiểm tra verify SQLite
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        with zipfile.ZipFile(APKG_PATH, "r") as zf:
            zf.extractall(tmp_path)

        db_path = tmp_path / "collection.anki2"
        if not db_path.exists():
            db_path = tmp_path / "collection.anki21"

        if not db_path.exists():
            print("[FAIL] Khong tim thay database SQLite trong APKG!")
            return 1

        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM notes")
        notes_count = cursor.fetchone()[0]
        cursor.execute("SELECT count(*) FROM cards")
        cards_count = cursor.fetchone()[0]
        cursor.execute("SELECT flds FROM notes LIMIT 3")
        samples = cursor.fetchall()
        conn.close()

    print(f"[VERIFY] Notes in SQLite: {notes_count} (Input: {len(cards_data)})")
    print(f"[VERIFY] Cards in SQLite: {cards_count}")

    if notes_count != len(cards_data):
        print(f"[FAIL] Note count mismatch: {notes_count} != {len(cards_data)}")
        return 1

    for (s,) in samples:
        if any(c in s for c in "áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ"):
            print("[OK] Diacritics test passed: Vietnamese characters intact.")
            break
    else:
        print("[WARN] Diacritics check could not confirm accented characters.")

    print("=== BUILD HOÀN TẤT THÀNH CÔNG (100% PASS) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
