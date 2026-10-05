# -*- coding: utf-8 -*-
"""
build_ped54_master_deck.py
Đóng gói bộ thẻ Anki MASTER barem-only cho PED-54 Tiếp cận trẻ đau khớp:
- Track: [BAREM GỐC Y THÁI BÌNH]: basic trả lời cốt lõi + cloze verbatim giáo trình.
Quy tắc: atomic, back <= 3-4 dòng, Unicode 100%, escape '<', organic count.
Coverage gate: BLOCK nếu bất kỳ section nào trong 9 sections (B0-B8) không có thẻ.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

import genanki

TARGET_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TARGET_DIR))
from ped54_cards_data import cards_data  # noqa: E402

DECK_ID = 1709132054
DECK_NAME = "Nhi khoa Y6::PED-54: Tiếp cận trẻ đau khớp"
JSON_PATH = TARGET_DIR / "PED-54_Tiep_can_tre_dau_khop_MASTER_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-54_Tiep_can_tre_dau_khop_MASTER_v1.apkg"

REQUIRED_SECTIONS = [
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7",
    "E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"
]

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #090e17;
  padding: 18px;
  max-width: 680px;
  margin: 0 auto;
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
  margin-bottom: 10px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 14px 16px;
  border-left: 3px solid #38bdf8;
  margin-top: 10px;
  font-size: 14.5px;
}
.cloze {
  font-weight: 700;
  color: #38bdf8;
  border-bottom: 2px solid #0284c7;
  padding: 0 2px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.04);
  border-left: 3px solid #38bdf8;
  font-size: 14px;
  color: #cbd5e1;
}
.extra-box-barem {
  border-left-color: #fbbf24;
}
.extra-title {
  font-weight: 700;
  color: #38bdf8;
  margin-bottom: 4px;
}
.extra-title-barem {
  color: #fbbf24;
}
"""

BASIC_MODEL = genanki.Model(
    1709541001,
    "PED54_Master_Basic",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Extra"},
            {"name": "Category"}, {"name": "Badge"}, {"name": "BadgeClass"}],
    templates=[{
        "name": "PED54 Master Basic",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box {{BadgeClass}}"><div class="extra-title {{BadgeClass}}">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)

CLOZE_MODEL = genanki.Model(
    1709541002,
    "PED54_Master_Cloze",
    model_type=genanki.Model.CLOZE,
    fields=[{"name": "Text"}, {"name": "Extra"}, {"name": "Category"},
            {"name": "Badge"}, {"name": "BadgeClass"}],
    templates=[{
        "name": "PED54 Master Cloze",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div><hr id="answer">{{#Extra}}<div class="extra-box {{BadgeClass}}"><div class="extra-title {{BadgeClass}}">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr)\b)", "&lt;", text)


def main() -> int:
    print("=== BUILD PED-54 MASTER DECK (BAREM GOC YTB) ===")
    # 1. Coverage gate (BLOCK neu thieu section)
    have = Counter(c["section"] for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[BLOCK] Thieu the o sections: {missing}")
        return 2
    print(f"[COVERAGE] Du {len(REQUIRED_SECTIONS)}/{len(REQUIRED_SECTIONS)} sections: {dict(sorted(have.items()))}")

    # 2. Validate fields
    for c in cards_data:
        if c["type"] == "basic":
            assert str(c.get("front", "")).strip() and str(c.get("back", "")).strip(), c["id"]
        elif c["type"] == "cloze":
            assert re.search(r"\{\{c\d+::.+?\}\}", str(c.get("text", ""))), c["id"]
        else:
            raise ValueError(f"unknown type {c['id']}")

    ids = [c["id"] for c in cards_data]
    assert len(ids) == len(set(ids)), "duplicate ids"
    n_basic = sum(1 for c in cards_data if c["type"] == "basic")
    n_cloze = len(cards_data) - n_basic
    print(f"[VALID] {len(cards_data)} the ({n_basic} basic + {n_cloze} cloze), ID duy nhat, field hop le.")

    # 3. JSON
    payload = {
        "topic": DECK_NAME,
        "version": "master_combo_v1",
        "date": "2026-09-28",
        "total_cards": len(cards_data),
        "cards": cards_data
    }
    JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[JSON] Da luu: {JSON_PATH.name}")

    # 4. APKG
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for c in cards_data:
        is_barem = c.get("track") == "barem_goc"
        badge = "🏛️ BAREM GỐC Y THÁI BÌNH" if is_barem else "🔬 EBM HIỆN ĐẠI & LÂM SÀNG"
        bclass = "badge-barem" if is_barem else "badge-ebm"
        if c["type"] == "basic":
            note = genanki.Note(
                model=BASIC_MODEL,
                fields=[
                    escape_angle_brackets(c["front"]),
                    escape_angle_brackets(c["back"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", ""),
                    badge,
                    bclass
                ],
                tags=c.get("tags", [])
            )
        else:
            note = genanki.Note(
                model=CLOZE_MODEL,
                fields=[
                    escape_angle_brackets(c["text"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", ""),
                    badge,
                    bclass
                ],
                tags=c.get("tags", [])
            )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(str(APKG_PATH))
    print(f"[APKG] Da xuat {len(cards_data)} the: {APKG_PATH.name}")

    # 5. Verify note count
    import sqlite3
    import tempfile
    import zipfile
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(APKG_PATH) as z:
            z.extract("collection.anki2", td)
        con = sqlite3.connect(f"{td}/collection.anki2")
        n_notes = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
        n_cards = con.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
        con.close()
    print(f"[VERIFY] notes={n_notes} cards={n_cards} (input={len(cards_data)})")
    if n_notes != len(cards_data):
        print("[FAIL] Lech note count!")
        return 2

    print("BUILD OK — organic count, khong ep so tron.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
