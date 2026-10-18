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
from ped62_cards_data import cards_data  # noqa: E402

DECK_ID = 170962001
DECK_NAME = "Nhi khoa Y6::PED-62: Dac diem benh hoc & Can nguyen vi sinh ho hap o tre em"
JSON_PATH = TARGET_DIR / "PED-62_Can_nguyen_vi_sinh_ho_hap_o_tre_em_2026-10-14_RELEASE_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-62_Can_nguyen_vi_sinh_ho_hap_o_tre_em_2026-10-14_RELEASE_v1.apkg"
FIGURES_DIR = TARGET_DIR / "outputs" / "figures"

REQUIRED_SECTIONS = [
    "B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"
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
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 10px 0;
  display: block;
}
"""

BASIC_MODEL = genanki.Model(
    1709621001,
    "PED62_Master_Basic",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED62 Master Basic",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn tra cứu:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)

def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr|img))", "&lt;", text)

def main() -> int:
    print(f"=== BUILD PED-62 MASTER DECK: '{DECK_NAME}' ===")
    print(f"Total input cards: {len(cards_data)}")

    # 1. Coverage gate
    have = Counter(c.get("section") for c in cards_data)
    missing = [s for s in REQUIRED_SECTIONS if have.get(s, 0) == 0]
    if missing:
        print(f"[BLOCK] Missing sections: {missing}")
        return 2
    print(f"[GATE PASS] Coverage: All {len(REQUIRED_SECTIONS)} sections covered: {dict(sorted(have.items()))}")

    # 2. Linter rules check
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
        if ("$" in txt) or ("\\text{" in txt) or ("\\ge" in txt):
            print(f"  [WARN] Card {c['id']} has LaTeX symbols: '$'")
            latex_matches += 1
        # Check double escapes
        if ("&lt;b&gt;" in txt) or ("&amp;" in txt):
            print(f"  [WARN] Card {c['id']} has double escapes")
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
    media_files = []
    if FIGURES_DIR.exists():
        media_files = [str(f) for f in FIGURES_DIR.glob("*.*") if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]]
        print(f"Tìm thấy {len(media_files)} media files trong {FIGURES_DIR.name}: {[Path(m).name for m in media_files]}")

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
            tags=c.get("tags", ["PED-62"])
        )
        deck.add_note(note)

    package = genanki.Package(deck)
    package.media_files = media_files
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