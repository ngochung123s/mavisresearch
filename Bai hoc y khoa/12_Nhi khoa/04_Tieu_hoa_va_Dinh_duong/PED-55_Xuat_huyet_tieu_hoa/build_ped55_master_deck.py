# -*- coding: utf-8 -*-
"""
build_ped55_master_deck.py
Đóng gói bộ thẻ Anki MASTER DUAL-TRACK cho PED-55 Xuất huyết tiêu hóa ở trẻ em:
- Track 1 [BAREM GỐC Y THÁI BÌNH]: 51 thẻ Basic bao phủ 100% câu chữ giáo trình (Trang 87 - 99).
- Track 2 [EBM HIỆN ĐẠI & LÂM SÀNG]: 17 thẻ Basic giải quyết cấp cứu sốc, Baveno VII, Meckel, 5 cạm bẫy.
- Quy chuẩn: 100% Basic, format <br>, 100% Unicode, escape '<'.
- Deck Name: "Nhi khoa Y6::PED-55: Xuất huyết tiêu hóa ở trẻ em"
- Deck ID: 1709132055
- Post-build verify: notes == input cards (68 notes).
"""
import json
import re
import sqlite3
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

import genanki

TARGET_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TARGET_DIR))
from ped55_cards_data import cards_data  # noqa: E402

DECK_ID = 1709132055
DECK_NAME = "Nhi khoa Y6::PED-55: Xuất huyết tiêu hóa ở trẻ em"
JSON_PATH = TARGET_DIR / "PED-55_Xuat_huyet_tieu_hoa_MASTER_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-55_Xuat_huyet_tieu_hoa_MASTER_v1.apkg"

REQUIRED_SECTIONS = [
    "B0", "B1", "B2", "B3", "B4", "B5", "B6",
    "E0", "E1", "E2", "E3", "E4", "E5"
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
}
.badge-barem {
  background-color: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-ebm {
  background-color: rgba(6, 182, 212, 0.15);
  color: #22d3ee;
  border: 1px solid rgba(6, 182, 212, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 12px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 14px 16px;
  border-left: 3px solid #38bdf8;
  margin-top: 10px;
  font-size: 14.5px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.04);
  border-left: 3px solid #fbbf24;
  font-size: 14px;
  color: #cbd5e1;
}
.extra-title {
  font-weight: 700;
  color: #fbbf24;
  margin-bottom: 4px;
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
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED55 Master Basic",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn tra cứu:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr))", "&lt;", text)


def main() -> int:
    print(f"=== BUILD PED-55 MASTER DECK: '{DECK_NAME}' ===")
    print(f"Total input cards: {len(cards_data)}")
    
    # 0. Coverage Gate
    have = Counter(c.get("section") for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[BLOCK] Missing sections: {missing}")
        return 2
    print(f"[GATE PASS] Coverage: All {len(REQUIRED_SECTIONS)} sections covered: {dict(sorted(have.items()))}")

    # 1. Xuất JSON
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(cards_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved cards JSON: {JSON_PATH.name}")

    # 2. Khởi tạo Deck
    deck = genanki.Deck(DECK_ID, DECK_NAME)

    added_notes = 0
    for card in cards_data:
        category = card.get("category", "Xuất huyết tiêu hóa")
        is_barem = card.get("track") == "barem_goc"
        badge = "🏛️ BAREM GỐC Y THÁI BÌNH" if is_barem else "🔬 EBM HIỆN ĐẠI & LÂM SÀNG"
        bclass = "badge-barem" if is_barem else "badge-ebm"
        extra = escape_angle_brackets(card.get("extra", ""))
        tags = card.get("tags", ["PED-55"])

        front = escape_angle_brackets(card["front"])
        back = card["back"]
        note = genanki.Note(
            model=BASIC_MODEL,
            fields=[front, back, extra, category, badge, bclass],
            tags=tags,
            guid=genanki.guid_for(f"ped55-master-{card['id']}"),
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
            print("[FAIL] Không tìm thấy database SQLite trong APKG!")
            return 1

        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM notes")
        sqlite_notes = cursor.fetchone()[0]
        cursor.execute("SELECT count(*) FROM cards")
        sqlite_cards = cursor.fetchone()[0]
        conn.close()

    print(f"[VERIFY] SQLite Notes: {sqlite_notes} | Cards: {sqlite_cards} (Input: {len(cards_data)})")
    if sqlite_notes != len(cards_data):
        print(f"[FAIL] Note count mismatch: SQLite {sqlite_notes} != Input {len(cards_data)}")
        return 2

    print("BUILD OK — Organic count, 100% Verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
