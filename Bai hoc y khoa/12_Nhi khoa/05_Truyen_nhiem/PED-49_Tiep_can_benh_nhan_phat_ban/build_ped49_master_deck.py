# -*- coding: utf-8 -*-
"""
build_ped49_master_deck.py
Đóng gói bộ thẻ Anki MASTER chuyên khoa Nhi cho:
PED-49 Tiếp cận bệnh nhân phát ban ở trẻ em (Approach to Pediatric Rash)
- Gồm 80 thẻ (40 Basic + 40 Cloze) tuân thủ 100% Medical Flashcard Governance.
- Phân tầng chuyên khoa: Cấp cứu & cờ đỏ, Hình thái học, Ban dát sẩn, Ban mụn nước, Kawasaki, Viêm mạch, Hạ sốt an toàn, Checkpoint lâm sàng.
- Tự động xuất APKG ra cả outputs/ và thư mục gốc của bài học.
- Xác thực số note trong SQLite nhị phân.
"""
import json
import re
import shutil
import sqlite3
import sys
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

import genanki

TARGET_DIR = Path(__file__).resolve().parent
JSON_PATH = TARGET_DIR / "PED-49_Tiep_can_benh_nhan_phat_ban_2026-09-25_RELEASE_v1.cards.v2.json"
OUTPUTS_DIR = TARGET_DIR / "outputs"
APKG_OUTPUT_PATH = OUTPUTS_DIR / "PED-49_Tiep_can_benh_nhan_phat_ban_2026-09-25_RELEASE_v1.apkg"
APKG_ROOT_PATH = TARGET_DIR / "PED-49_Tiep_can_benh_nhan_phat_ban_2026-09-25_RELEASE_v1.apkg"

DECK_ID = 2139366082049
DECK_NAME = "Nhi khoa Y6::PED-49: Tiếp cận bệnh nhân phát ban ở trẻ em"

REQUIRED_SECTIONS = ["SEC1", "SEC3", "SEC4_1", "SEC4_2", "SEC4_3", "SEC4_4", "SEC7", "SEC8"]

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
.badge-red {
  background-color: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.4);
}
.badge-amber {
  background-color: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-blue {
  background-color: rgba(14, 165, 233, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(14, 165, 233, 0.4);
}
.badge-green {
  background-color: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.4);
}
.badge-purple {
  background-color: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.4);
}
.badge-cyan {
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
.extra-title {
  font-weight: 700;
  color: #38bdf8;
  margin-bottom: 4px;
}
"""

BASIC_MODEL = genanki.Model(
    1709491001,
    "PED49_Master_Basic",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED49 Master Basic",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)

CLOZE_MODEL = genanki.Model(
    1709491002,
    "PED49_Master_Cloze",
    model_type=genanki.Model.CLOZE,
    fields=[
        {"name": "Text"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED49 Master Cloze",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div><hr id="answer">{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr)\b)", "&lt;", text)


def get_badge_info(section: str):
    mapping = {
        "SEC3": ("🚨 CẤP CỨU & CỜ ĐỎ", "badge-red"),
        "SEC1": ("🔍 HÌNH THÁI HỌC TỔN THƯƠNG", "badge-cyan"),
        "SEC4_1": ("🌸 BAN DÁT SẨN & ĐỘNG HỌC SỐT", "badge-amber"),
        "SEC4_2": ("💧 BAN MỤN NƯỚC & BÓNG NƯỚC", "badge-blue"),
        "SEC4_3": ("❤️ BỆNH KAWASAKI (AHA 2024)", "badge-purple"),
        "SEC4_4": ("🩸 VIÊM MẠCH IGA & NHIỄM TRÙNG DA", "badge-red"),
        "SEC8": ("🌡️ HẠ SỐT & CHĂM SÓC AN TOÀN", "badge-green"),
        "SEC7": ("⚡ CẤP CỨU PHẢN VỆ & CHECKPOINT", "badge-amber"),
    }
    return mapping.get(section, ("🔬 NHI KHOA LÂM SÀNG", "badge-blue"))


def main() -> int:
    print("=== BUILD PED-49 MASTER DECK ===")
    if not JSON_PATH.exists():
        print(f"[ERROR] Khong tim thay file JSON: {JSON_PATH}")
        return 1

    cards_data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    print(f"[LOAD] Da doc {len(cards_data)} the tu JSON.")

    # 1. Section coverage gate
    have = Counter(c.get("section") for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[BLOCK] Thieu the o cac section: {missing}")
        return 2
    print(f"[COVERAGE] Du {len(REQUIRED_SECTIONS)}/{len(REQUIRED_SECTIONS)} sections: {dict(sorted(have.items()))}")

    # 2. Field verification
    for c in cards_data:
        cid = c.get("id", "no-id")
        if c["type"] == "basic":
            assert str(c.get("front", "")).strip() and str(c.get("back", "")).strip(), cid
        elif c["type"] == "cloze":
            assert re.search(r"\{\{c\d+::.+?\}\}", str(c.get("text", ""))), cid
        else:
            raise ValueError(f"Unknown type in {cid}")

    n_basic = sum(1 for c in cards_data if c["type"] == "basic")
    n_cloze = len(cards_data) - n_basic
    print(f"[VALID] {len(cards_data)} the ({n_basic} basic + {n_cloze} cloze), tat ca fields hop le.")

    # 3. Build APKG
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for c in cards_data:
        sec = c.get("section", "SEC1")
        badge, bclass = get_badge_info(sec)
        tags = c.get("tags", ["PED-49", "Phat-ban"])
        cat = c.get("category", "")

        if c["type"] == "basic":
            note = genanki.Note(
                model=BASIC_MODEL,
                fields=[
                    escape_angle_brackets(c["front"]),
                    escape_angle_brackets(c["back"]),
                    escape_angle_brackets(c.get("extra", "")),
                    cat,
                    badge,
                    bclass,
                ],
                tags=tags,
            )
        else:
            note = genanki.Note(
                model=CLOZE_MODEL,
                fields=[
                    escape_angle_brackets(c["text"]),
                    escape_angle_brackets(c.get("extra", "")),
                    cat,
                    badge,
                    bclass,
                ],
                tags=tags,
            )
        deck.add_note(note)

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    genanki.Package(deck).write_to_file(str(APKG_OUTPUT_PATH))
    print(f"[APKG] Da xuat {len(cards_data)} the ra: {APKG_OUTPUT_PATH.name}")

    # Copy to root folder as well
    shutil.copy2(APKG_OUTPUT_PATH, APKG_ROOT_PATH)
    print(f"[APKG] Da dong bo ra thu muc goc: {APKG_ROOT_PATH.name}")

    # 4. Verify in SQLite
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(APKG_OUTPUT_PATH) as z:
            z.extract("collection.anki2", td)
        con = sqlite3.connect(f"{td}/collection.anki2")
        n_notes = con.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
        n_cards = con.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
        con.close()

    print(f"[VERIFY] SQLite: notes={n_notes}, cards={n_cards} (input={len(cards_data)})")
    if n_notes != len(cards_data):
        print(f"[FAIL] Note count khong khop ({n_notes} vs {len(cards_data)})!")
        return 2

    print("BUILD PED-49 COMPLETED SUCCESSFULLY.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
