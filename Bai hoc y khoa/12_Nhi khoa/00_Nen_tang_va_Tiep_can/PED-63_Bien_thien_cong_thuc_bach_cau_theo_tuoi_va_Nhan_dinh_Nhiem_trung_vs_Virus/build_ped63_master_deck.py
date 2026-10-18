# -*- coding: utf-8 -*-
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
from ped63_cards_data import cards_data  # noqa: E402

DECK_ID = 170963001
DECK_NAME = "Nhi khoa Y6::PED-63: Bien thien cong thuc bach cau theo tuoi & Nhan dinh Nhiem trung vs Virus"
JSON_PATH = TARGET_DIR / "PED-63_Bien_thien_cong_thuc_bach_cau_theo_tuoi_va_Nhan_dinh_Nhiem_trung_vs_Virus_2026-10-16_RELEASE_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-63_Bien_thien_cong_thuc_bach_cau_theo_tuoi_va_Nhan_dinh_Nhiem_trung_vs_Virus_2026-10-16_RELEASE_v1.apkg"

REQUIRED_SECTIONS = [
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"
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
  border-left: 3px solid #06b6d4;
  margin-top: 12px;
  font-size: 14.5px;
}
.extra-box {
  margin-top: 16px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.02);
  border-left: 3px solid #64748b;
  font-size: 13.5px;
  color: #94a3b8;
}
.extra-title {
  font-weight: 700;
  color: #cbd5e1;
  margin-bottom: 4px;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
"""

BASIC_MODEL = genanki.Model(
    170963101,
    "PED63_Master_Basic",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED-63 Master Basic Card",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn trích dẫn y chứng & Tài liệu học tập:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?![a-zA-Z/])", "&lt;", text)


def main() -> int:
    print(f"=== BUILD PED-63 MASTER DECK: '{DECK_NAME}' ===")
    print(f"Total input cards: {len(cards_data)}")

    # 1. Coverage Gate across sections
    have = Counter(c["section"] for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[FAIL] Missing cards in required sections: {missing}")
        return 2
    print(f"[GATE PASS] Coverage: All {len(REQUIRED_SECTIONS)} sections covered: {dict(sorted(have.items()))}")

    # 2. Linter quy chuẩn thẻ
    print("\nKiểm tra Linter quy chuẩn thẻ:")
    unescaped_lt = 0
    latex_matches = 0
    double_escapes = 0
    back_purity_fails = 0

    for idx, c in enumerate(cards_data, 1):
        txt = c["front"] + " " + c["back"] + " " + c.get("extra", "")
        # Check unescaped <
        raw_lt = re.findall(r"<(?![a-zA-Z/])", txt)
        if raw_lt:
            print(f"  [WARN] Card {c['id']} has unescaped '<': {raw_lt}")
            unescaped_lt += len(raw_lt)

        # Check LaTeX
        if "$" in txt or "\\times" in txt or "\\ge" in txt or "\\le" in txt or "\\rightarrow" in txt:
            print(f"  [WARN] Card {c['id']} has LaTeX tokens!")
            latex_matches += 1

        # Check double escapes
        if any(d in txt for d in ["<b&gt;", "<br&gt;", "&lt;b&gt;", "&lt;br&gt;"]):
            print(f"  [WARN] Card {c['id']} has double escaped HTML tags!")
            double_escapes += 1

        # Check Back-purity (no source/page in back)
        back_txt = c["back"].lower()
        if re.search(r"trang\s+\d+|giáo trình\s+nhi|nguồn\s*:", back_txt):
            print(f"  [WARN] Card {c['id']} has source reference in Back: {c['back'][:60]}...")
            back_purity_fails += 1

    print(f"  Unescaped '<': {unescaped_lt}")
    print(f"  LaTeX occurrences: {latex_matches}")
    print(f"  Double escapes: {double_escapes}")
    print(f"  Back purity failures: {back_purity_fails}")
    assert unescaped_lt == 0, "Found unescaped '<' in cards!"
    assert latex_matches == 0, "Found LaTeX '$' in cards!"
    assert double_escapes == 0, "Found double escapes in cards!"
    assert back_purity_fails == 0, "Found source references in Back!"
    print("  => Linter 100% CLEAN!")

    # 3. Xuất JSON
    payload = {
        "deck_id": DECK_ID,
        "deck_name": DECK_NAME,
        "card_count": len(cards_data),
        "cards": cards_data
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"[OK] Đã ghi {len(cards_data)} thẻ vào {JSON_PATH.name}")

    # 4. Build APKG
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for c in cards_data:
        front_clean = escape_angle_brackets(c["front"])
        back_clean = escape_angle_brackets(c["back"])
        extra_clean = escape_angle_brackets(c.get("extra", ""))

        note = genanki.Note(
            model=BASIC_MODEL,
            fields=[
                front_clean,
                back_clean,
                extra_clean,
                c.get("category", "Lâm sàng"),
                c.get("badge", "EBM Master"),
                c.get("badge_class", "badge-ebm")
            ],
            tags=c.get("tags", ["PED-63"])
        )
        deck.add_note(note)

    package = genanki.Package(deck)
    package.write_to_file(str(APKG_PATH))
    print(f"[OK] Đã đóng gói thành công: {APKG_PATH.name} ({APKG_PATH.stat().st_size / 1024:.1f} KB)")

    # 5. Post-build SQLite verification
    print("\nĐang đối soát cấu trúc SQLite bên trong APKG...")
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        with zipfile.ZipFile(APKG_PATH, "r") as zf:
            zf.extractall(tmp_path)

        db_file = tmp_path / "collection.anki2"
        if not db_file.exists():
            db_file = tmp_path / "collection.anki21"
        assert db_file.exists(), "Không tìm thấy collection.anki2(1)!"

        conn = sqlite3.connect(str(db_file))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM notes")
        notes_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM cards")
        cards_count = cur.fetchone()[0]
        conn.close()

        print(f"  SQLite Notes count: {notes_count}")
        print(f"  SQLite Cards count: {cards_count}")
        print(f"  Input cards count : {len(cards_data)}")
        assert notes_count == len(cards_data), f"Notes ({notes_count}) != Cards ({len(cards_data)})"
        assert cards_count == len(cards_data), f"Cards ({cards_count}) != Input ({len(cards_data)})"
        print("  => POST-BUILD SQLITE VERIFY: 100% MATCH PASS!")

    return 0

if __name__ == "__main__":
    sys.exit(main())
