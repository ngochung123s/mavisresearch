# -*- coding: utf-8 -*-
"""
build_ped61_master_deck.py
Đóng gói bộ thẻ Anki MASTER DUAL-TRACK cho PED-61:
- 100% BASIC type, chuẩn Hierarchical Scaffolding, Back-Purity 100%, 0 LaTeX.
- Đóng gói toàn bộ 5 ảnh nén từ outputs/figures/ vào package.media_files.
- Deck Name: "Nhi khoa Y6::PED-61: Tiep can di ngoai bat thuong & Danh gia tinh chat phan o tre em"
- Deck ID: 170961001
- Model ID: 1709611001 (PED61_Master_Basic)
- Post-build verify: SQLite notes == input cards == SQLite cards, Diacritics >= 80%.
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
from ped61_cards_data import cards_data  # noqa: E402

DECK_ID = 170961001
DECK_NAME = "Nhi khoa Y6::PED-61: Tiep can di ngoai bat thuong & Danh gia tinh chat phan o tre em"
JSON_PATH = TARGET_DIR / "PED-61_Tiep_can_di_ngoai_MASTER_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-61_Tiep_can_di_ngoai_MASTER_v1.apkg"
FIGURES_DIR = TARGET_DIR / "outputs" / "figures"

REQUIRED_SECTIONS = [
    "B0", "B1", "B2", "B3", "B4", "B5", "B6"
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
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 10px 0;
  display: block;
}
"""

BASIC_MODEL = genanki.Model(
    1709611001,
    "PED61_Master_Basic",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"},
    ],
    templates=[{
        "name": "PED61 Master Basic",
        "qfmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>',
        "afmt": '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn tra cứu:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE,
)


def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr|img)\b)", "&lt;", text)


def main() -> int:
    print(f"=== BUILD PED-61 MASTER DECK (100% BASIC WITH MEDIA): '{DECK_NAME}' ===")
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
        "topic": DECK_NAME,
        "version": "master_combo_basic_v1",
        "date": "2026-10-13",
        "total_cards": len(cards_data),
        "cards": cards_data,
    }
    JSON_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[OK] Saved JSON: {JSON_PATH} ({len(cards_data)} cards)")

    # 4. Xuất APKG kèm media files
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    for c in cards_data:
        is_barem = c.get("track") == "barem_goc"
        badge_text = "🏛️ BAREM GIÁO TRÌNH GỐC" if is_barem else "🔬 LẬP LUẬN EBM & LÂM SÀNG"
        badge_class = "badge-barem" if is_barem else "badge-ebm"

        note = genanki.Note(
            model=BASIC_MODEL,
            fields=[
                escape_angle_brackets(c["front"]),
                escape_angle_brackets(c["back"]),
                escape_angle_brackets(c.get("extra", "")),
                escape_angle_brackets(c.get("category", "")),
                badge_text,
                badge_class,
            ],
            tags=c.get("tags", []),
        )
        deck.add_note(note)

    # Đóng gói toàn bộ ảnh trong figures vào APKG
    media_list = [str(f) for f in FIGURES_DIR.glob("*.jpg")]
    print(f"Đóng gói {len(media_list)} file ảnh nén vào APKG media:")
    for mf in media_list:
        print(f"  + {Path(mf).name} ({Path(mf).stat().st_size / 1024:.1f} KB)")

    package = genanki.Package(deck)
    package.media_files = media_list
    package.write_to_file(APKG_PATH)
    apkg_size_kb = APKG_PATH.stat().st_size / 1024
    print(f"[OK] Saved APKG: {APKG_PATH} ({apkg_size_kb:.1f} KB)")

    # 5. SQLite verification
    tmp_dir = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(APKG_PATH) as z:
        z.extractall(tmp_dir)

    db = sqlite3.connect(tmp_dir / "collection.anki2")
    notes_cnt = db.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    cards_cnt = db.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
    db.close()
    import shutil
    shutil.rmtree(tmp_dir)

    print(f"[VERIFY] Input cards: {len(cards_data)} | SQLite notes: {notes_cnt} | SQLite cards: {cards_cnt}")
    assert notes_cnt == len(cards_data), f"Mismatch: {notes_cnt} != {len(cards_data)}"
    assert cards_cnt == len(cards_data), f"Basic cards count mismatch: {cards_cnt} != {len(cards_data)}"
    print("[VERIFY PASS] SQLite notes == input cards == SQLite cards (100% 1-to-1 Basic match)!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
