# -*- coding: utf-8 -*-
"""Build Anki APKG from the leiomyoma ART knowledge check."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
from lesson_builder import add_cards_from_json_v2

DATE = "2026-07-12"
ROOT = Path(__file__).parent
CHECK = ROOT / f"U_xo_tu_cung_ART_Infertility_{DATE}_knowledge_check.md"
KEY = ROOT / f"U_xo_tu_cung_ART_Infertility_{DATE}_knowledge_check_answer_key.md"
JSON_OUT = ROOT / f"U_xo_tu_cung_ART_Infertility_{DATE}.cards.v2.json"
APKG_OUT = ROOT / f"Anki - U_xo_tu_cung_ART_Infertility_{DATE} - {DATE}.apkg"

BASIC_MODEL_ID = 5707123901
CLOZE_MODEL_ID = 5707123902
DECK_ID = 5707123900
DECK_NAME = "OB/GYN::U_xo_tu_cung_ART_Infertility::2026-07-12"


def section_map(text):
    sections = {}
    current = None
    for line in text.splitlines():
        m = re.match(r"##\s+([A-Z])\.\s+(.+)", line)
        if m:
            current = m.group(1)
            sections[current] = m.group(2).strip()
    return sections


def parse_questions(text):
    sections = section_map(text)
    current = None
    questions = []
    for line in text.splitlines():
        m = re.match(r"##\s+([A-Z])\.\s+(.+)", line)
        if m:
            current = m.group(1)
            continue
        m = re.match(r"(\d+)\.\s+(.+?)\s*$", line)
        if m and current:
            questions.append({
                "n": int(m.group(1)),
                "section": sections[current],
                "question": m.group(2).strip(),
            })
    return questions


def parse_answers(text):
    answers = {}
    current = None
    buf = []
    for line in text.splitlines():
        m = re.match(r"(\d+)\.\s+(.+)", line)
        if m:
            if current is not None:
                answers[current] = " ".join(buf).strip()
            current = int(m.group(1))
            buf = [m.group(2).strip()]
        elif current is not None and line.strip() and not line.startswith("---") and not line.startswith("##"):
            buf.append(line.strip())
    if current is not None:
        answers[current] = " ".join(buf).strip()
    return answers


def make_cards():
    questions = parse_questions(CHECK.read_text(encoding="utf-8"))
    answers = parse_answers(KEY.read_text(encoding="utf-8"))
    missing = [q["n"] for q in questions if q["n"] not in answers]
    if missing:
        raise SystemExit(f"Missing answers for questions: {missing}")
    cards = []
    for q in questions:
        n = q["n"]
        cards.append({
            "type": "basic",
            "front": f"U xơ tử cung & ART — Câu {n}: {q['question']}",
            "back": (
                f"<b>Nhóm:</b> {q['section']}<br><br>"
                f"<b>Ý chính:</b><br>{answers[n]}<br><br>"
                "<b>Nhớ quy tắc:</b> luôn phân biệt giảm triệu chứng / làm nhỏ u / sửa khoang / lợi ích ART."
            ),
            "extra": "Leiomyoma ART Infertility 2026-07-12",
        })
    return cards


def main():
    cards = make_cards()
    JSON_OUT.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    basic, cloze = add_cards_from_json_v2(
        json_path=str(JSON_OUT),
        basic_model_id=BASIC_MODEL_ID,
        cloze_model_id=CLOZE_MODEL_ID,
        basic_model_name=f"Leiomyoma ART Basic {DATE}",
        cloze_model_name=f"Leiomyoma ART Cloze {DATE}",
        deck_id=DECK_ID,
        deck_name=DECK_NAME,
        deck_description=f"U xơ tử cung, ART và vô sinh — self-check 65 câu — {DATE}",
        output_path=str(APKG_OUT),
    )
    print(f"[OK] cards JSON: {JSON_OUT}")
    print(f"[OK] APKG: {APKG_OUT}")
    print(f"[OK] {basic} basic + {cloze} cloze = {basic + cloze} cards")


if __name__ == "__main__":
    main()
