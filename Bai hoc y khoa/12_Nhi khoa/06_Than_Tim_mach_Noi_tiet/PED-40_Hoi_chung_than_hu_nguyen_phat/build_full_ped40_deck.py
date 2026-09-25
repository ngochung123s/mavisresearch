# -*- coding: utf-8 -*-
"""
build_full_ped40_deck.py
Tạo bộ thẻ Anki SIÊU CHI TIẾT (105 thẻ) bao phủ 100% bài giảng PED-40: Hội chứng thận hư nguyên phát ở trẻ em.
Tuân thủ nghiêm ngặt skill medical-flashcard-governance:
- Ưu tiên thẻ Basic (Hỏi - Đáp) làm chủ đạo (≥ 75-80%).
- Thẻ Cloze có nhiều số: BẮT BUỘC dùng đa cloze {{c1::...}} trong 1 thẻ.
- Ký tự Unicode chuẩn (→, ≥, ≤, ×, µg, µmol/L, %), không lỗi font LaTeX hay HTML tag.
"""
import re
import json
import genanki
from pathlib import Path

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\06_Than_Tim_mach_Noi_tiet\PED-40_Hoi_chung_than_hu_nguyen_phat")
OUTPUTS_DIR = TARGET_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #090e17;
  padding: 20px;
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
.badge-basic {
  background-color: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.4);
}
.badge-cloze {
  background-color: rgba(168, 85, 247, 0.15);
  color: #c084fc;
  border: 1px solid rgba(168, 85, 247, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 14px;
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
  padding: 0 3px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(245, 158, 11, 0.08);
  border-left: 3px solid #f59e0b;
  font-size: 13.5px;
  color: #cbd5e1;
}
.extra-title {
  font-weight: 700;
  color: #fbbf24;
  margin-bottom: 4px;
}
"""

BASIC_MODEL = genanki.Model(
    1709403001,
    'PED40_Full_Basic_Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Extra'},
        {'name': 'Category'},
    ],
    templates=[{
        'name': 'PED40 Basic Card',
        'qfmt': '<div class="badge badge-basic">📘 PED-40 • {{Category}}</div><div class="question">{{Front}}</div>',
        'afmt': '<div class="badge badge-basic">📘 PED-40 • {{Category}}</div><div class="question">{{Front}}</div><hr id="answer"><div class="answer-box">{{Back}}</div>{{#Extra}}<div class="extra-box"><div class="extra-title">⚠️ BẪY LÂM SÀNG & LƯU Ý CỐT LÕI:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE
)

CLOZE_MODEL = genanki.Model(
    1709403002,
    'PED40_Full_Cloze_Model',
    model_type=genanki.Model.CLOZE,
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
        {'name': 'Category'},
    ],
    templates=[{
        'name': 'PED40 Multi-Cloze Card',
        'qfmt': '<div class="badge badge-cloze">⚡ PED-40 • {{Category}}</div><div class="question">{{cloze:Text}}</div>',
        'afmt': '<div class="badge badge-cloze">⚡ PED-40 • {{Category}}</div><div class="question">{{cloze:Text}}</div><hr id="answer">{{#Extra}}<div class="extra-box"><div class="extra-title">💡 GIẢI THÍCH LÂM SÀNG & EBM:</div>{{Extra}}</div>{{/Extra}}',
    }],
    css=CSS_STYLE
)

def escape_angle_brackets(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr|ul|/ul|li|/li)\b)', '&lt;', text)

# Tải danh sách 105 thẻ chi tiết
from ped40_cards_data import all_cards

def main():
    print(f"=== BẮT ĐẦU ĐÓNG GÓI BỘ THẺ ANKI PED-40 TOÀN DIỆN (105 THẺ) ===")
    deck_id = 1709402026
    deck_name = "Nhi khoa Y6::PED-40: Hội chứng thận hư nguyên phát ở trẻ em"
    
    deck = genanki.Deck(deck_id, deck_name)
    
    total_basic = 0
    total_cloze = 0

    for c in all_cards:
        if c["type"] == "basic":
            note = genanki.Note(
                model=BASIC_MODEL,
                fields=[
                    escape_angle_brackets(c["front"]),
                    escape_angle_brackets(c["back"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", "Lâm sàng")
                ],
                tags=["PED-40", "Hoi_chung_than_hu", "Nhi_khoa", "EBM", "Basic"]
            )
            deck.add_note(note)
            total_basic += 1
        elif c["type"] == "cloze":
            note = genanki.Note(
                model=CLOZE_MODEL,
                fields=[
                    escape_angle_brackets(c["text"]),
                    escape_angle_brackets(c.get("extra", "")),
                    c.get("category", "Tiêu chuẩn")
                ],
                tags=["PED-40", "Hoi_chung_than_hu", "Nhi_khoa", "Cloze", "EBM"]
            )
            deck.add_note(note)
            total_cloze += 1

    # 1. Xuất file JSON
    json_payload = {
        "topic": "PED-40: Hội chứng thận hư nguyên phát ở trẻ em (Approach to Pediatric Idiopathic Nephrotic Syndrome)",
        "lesson_id": "PED-40",
        "version": "2026-09-21_RELEASE_v1",
        "total_cards": len(all_cards),
        "total_basic": total_basic,
        "total_cloze": total_cloze,
        "basic_percentage": f"{(total_basic / len(all_cards)) * 100:.1f}%",
        "cards": all_cards
    }
    
    json_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.cards.v2.json"
    json_path.write_text(json.dumps(json_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Đã lưu file JSON: {json_path} ({len(all_cards)} thẻ: {total_basic} Basic [{total_basic/len(all_cards)*100:.1f}%], {total_cloze} Cloze)")

    # 2. Xuất file APKG Release v1
    apkg_release_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.apkg"
    genanki.Package(deck).write_to_file(str(apkg_release_path))
    print(f"✓ Đã xuất APKG Release v1: {apkg_release_path}")

    # 3. Xuất file APKG Master v1
    apkg_master_path = TARGET_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_MASTER_v1.apkg"
    genanki.Package(deck).write_to_file(str(apkg_master_path))
    print(f"✓ Đã xuất APKG Master v1: {apkg_master_path}")

    # 4. Sao chép vào outputs/
    output_apkg = OUTPUTS_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.apkg"
    output_json = OUTPUTS_DIR / "PED-40_Hoi_chung_than_hu_nguyen_phat_2026-09-21_RELEASE_v1.cards.v2.json"
    output_apkg.write_bytes(apkg_release_path.read_bytes())
    output_json.write_text(json_path.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"✓ Đã đồng bộ sang outputs/: {output_apkg}")

    print("=== HOÀN TẤT ĐÓNG GÓI APKG PED-40 THÀNH CÔNG ===")

if __name__ == "__main__":
    main()
