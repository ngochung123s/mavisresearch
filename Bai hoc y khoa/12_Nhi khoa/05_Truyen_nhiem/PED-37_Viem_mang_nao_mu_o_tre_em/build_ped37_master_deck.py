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
from ped37_cards_data import cards_data  # noqa: E402

DECK_ID = 170937001
DECK_NAME = "Nhi khoa Y6::PED-37: Viem mang nao mu o tre em - Can nguyen, DNT & Dieu tri da mo thuc"
JSON_PATH = TARGET_DIR / "PED-37_Viem_mang_nao_mu_o_tre_em_2026-10-19_RELEASE_v1.cards.v2.json"
APKG_PATH = TARGET_DIR / "PED-37_Viem_mang_nao_mu_o_tre_em_2026-10-19_RELEASE_v1.apkg"
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
.badge-algo {
  background-color: rgba(234, 179, 8, 0.15);
  color: #facc15;
  border: 1px solid rgba(234, 179, 8, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 12px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.03);
  border-left: 3px solid #38bdf8;
  padding: 14px 16px;
  border-radius: 0 8px 8px 0;
  margin-top: 14px;
  color: #cbd5e1;
}
.source-box {
  margin-top: 16px;
  padding-top: 10px;
  border-top: 1px dashed rgba(255, 255, 255, 0.15);
  font-size: 12px;
  color: #94a3b8;
}
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-top: 10px;
}
"""

BASIC_MODEL = genanki.Model(
    160737001,
    "PED-37 Basic Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
        {"name": "Extra"},
        {"name": "Category"},
        {"name": "Badge"},
        {"name": "BadgeClass"}
    ],
    templates=[
        {
            "name": "Standard Card",
            "qfmt": """
<div class="card">
  <div><span class="badge {{BadgeClass}}">{{Badge}}</span></div>
  <div class="question">{{Front}}</div>
</div>
""",
            "afmt": """
<div class="card">
  <div><span class="badge {{BadgeClass}}">{{Badge}}</span></div>
  <div class="question">{{Front}}</div>
  <hr id="answer" style="border: none; border-top: 1px solid rgba(255,255,255,0.1); margin: 16px 0;">
  <div class="answer-box">{{Back}}</div>
  {{#Extra}}
  <div class="source-box"><b>Nguồn đối soát:</b> {{Extra}}</div>
  {{/Extra}}
</div>
"""
        }
    ],
    css=CSS_STYLE
)

def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"<(?![a-zA-Z/])", "&lt;", text)

def verify_apkg(apkg_path: Path, expected_count: int) -> bool:
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(apkg_path, "r") as zf:
            zf.extractall(td)
        db_path = Path(td) / "collection.anki2"
        if not db_path.exists():
            db_path = Path(td) / "collection.anki21"
        if not db_path.exists():
            print("[FAIL] Khong tim thay collection.anki2 trong file APKG")
            return False

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM notes")
        actual = cur.fetchone()[0]
        conn.close()

        print(f"[VERIFY] So note trong APKG: {actual} / Ky vong: {expected_count}")
        return actual == expected_count

def main():
    print(f"=== BAT DAU BUILD MASTER DECK PED-37 ({len(cards_data)} THE) ===")

    # 1. Section coverage check
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
        raw_lt = re.findall(r"<(?![a-zA-Z/])", txt)
        if raw_lt:
            print(f"  [WARN] Card {c['id']} has unescaped '<': {raw_lt}")
            unescaped_lt += len(raw_lt)
        if ("$" in txt) or ("\\text{" in txt) or ("\\ge" in txt):
            print(f"  [WARN] Card {c['id']} has LaTeX symbols")
            latex_matches += 1
        if ("&lt;b&gt;" in txt) or ("&amp;" in txt):
            print(f"  [WARN] Card {c['id']} has double escapes")
            double_escapes += 1
        back_txt = c["back"].lower()
        if re.search(r"trang\s+\d+|giáo trình\s+nhi|nguồn\s*:", back_txt):
            print(f"  [WARN] Card {c['id']} has source reference in Back: {c['back'][:60]}...")
            back_purity_fails += 1

    print(f"  Unescaped '<': {unescaped_lt}")
    print(f"  LaTeX occurrences: {latex_matches}")
    print(f"  Double escapes: {double_escapes}")
    print(f"  Back purity failures: {back_purity_fails}")
    assert unescaped_lt == 0, "Found unescaped '<' in cards!"
    assert latex_matches == 0, "Found LaTeX in cards!"
    assert double_escapes == 0, "Found double escapes in cards!"
    assert back_purity_fails == 0, "Found source references in Back!"
    print("  => Linter 100% CLEAN!")

    # 3. Xuat JSON
    payload = {
        "deck_id": DECK_ID,
        "deck_name": DECK_NAME,
        "card_count": len(cards_data),
        "cards": cards_data
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"[OK] Da ghi {len(cards_data)} the vao {JSON_PATH.name}")

    # 4. Build APKG
    deck = genanki.Deck(DECK_ID, DECK_NAME)
    media_files = []
    if FIGURES_DIR.exists():
        media_files = [str(f) for f in FIGURES_DIR.glob("*.*") if f.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]]
        print(f"Tim thay {len(media_files)} media files trong {FIGURES_DIR.name}: {[Path(m).name for m in media_files]}")

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
            tags=c.get("tags", ["PED-37"])
        )
        deck.add_note(note)

    package = genanki.Package(deck)
    if media_files:
        package.media_files = media_files
    package.write_to_file(str(APKG_PATH))
    print(f"[OK] Da tao file APKG: {APKG_PATH.name} ({APKG_PATH.stat().st_size:,} bytes)")

    # 5. Verify SQLite note count
    if not verify_apkg(APKG_PATH, len(cards_data)):
        print("[FAIL] Doi soat APKG that bai!")
        return 1
    print("[PASS] Doi soat APKG khop 100% so luong the!")

    # 6. Verify diacritics
    verify_script = TARGET_DIR.parent.parent.parent / "10_Script Python" / "verify_apkg_diacritics.py"
    if not verify_script.exists():
        verify_script = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\verify_apkg_diacritics.py")
    if verify_script.exists():
        import subprocess
        res = subprocess.run([sys.executable, str(verify_script), str(APKG_PATH)], capture_output=True, text=True)
        print(res.stdout)
        if res.returncode != 0:
            print("[FAIL] Kiem tra dau tieng Viet that bai!")
            return res.returncode
        print("[PASS] Kiem tra dau tieng Viet dat chuan!")

    print("\n=== HOAN TAT BUILD MASTER DECK PED-37 THANH CONG RUC RO ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())
