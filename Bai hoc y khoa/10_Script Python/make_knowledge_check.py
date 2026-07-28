"""make_knowledge_check.py — Generate repeatable knowledge checks from lesson cards.

Usage:
    python make_knowledge_check.py <lesson.cards.v2.json>
    python make_knowledge_check.py <lesson.md>

Outputs in the lesson folder:
    <Topic>_knowledge_check.md
    <Topic>_knowledge_check_answer_key.md
    <Topic>_knowledge_check_score.json
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

NUMERIC_RE = re.compile(
    r"\d|%|≥|≤|>|<|\b(?:OR|RR|HR|CI|AOR|aOR|mg|IU|UI|kg|mL|mmol|tuần|week|w|ngày|giờ|dose|liều)\b",
    re.IGNORECASE,
)
CASE_RE = re.compile(
    r"quản lý|chẩn đoán|xử trí|điều trị|sàng lọc|theo dõi|biến chứng|thời điểm|khởi đầu|first-line|protocol|trigger|liều|timing",
    re.IGNORECASE,
)
RED_FLAG_RE = re.compile(
    r"sai lầm|không|tránh|first-line|chống chỉ định|biến chứng|protocol|timing|dose|liều|nguy cơ|ưu tiên|bắt buộc",
    re.IGNORECASE,
)
CLOZE_RE = re.compile(r"\{\{c\d+::(.*?)(?:::[^}]*)?\}\}")


def topic_stem(path: Path) -> str:
    stem = path.stem
    return stem.replace(".cards", "").replace(".v2", "")


def find_cards_file(path: Path) -> Path:
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(path)
    if path.suffix.lower() == ".json":
        return path
    if path.suffix.lower() != ".md":
        raise ValueError("Input must be a .cards.v2.json or .md file")

    exact = path.with_name(f"{path.stem}.cards.v2.json")
    if exact.exists():
        return exact
    candidates = sorted(path.parent.glob("*.cards.v2.json"))
    if len(candidates) == 1:
        return candidates[0]
    if not candidates:
        raise FileNotFoundError(f"No *.cards.v2.json found next to {path}")
    raise ValueError(f"Multiple cards files found next to {path}; pass one explicitly")


def strip_html(text: str) -> str:
    text = re.sub(r"<\s*br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</\s*(p|div|li|ul|ol)\s*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def cloze_blank(text: str) -> str:
    return CLOZE_RE.sub("_____", text)


def cloze_answers(text: str) -> list[str]:
    return [m.group(1).strip() for m in CLOZE_RE.finditer(text)]


def load_cards(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("cards", [])
    if not isinstance(data, list):
        raise ValueError("Cards JSON must be a list or {'cards': [...]} object")
    return [c for c in data if isinstance(c, dict)]


def card_text(card: dict) -> str:
    return "\n".join(str(card.get(k, "")) for k in ("front", "back", "text", "extra"))


def numbered(items: list[str]) -> str:
    return "\n\n".join(f"{i}. {item}" for i, item in enumerate(items, 1)) or "_Không có câu phù hợp._"


def answer_block(card: dict) -> str:
    if card.get("type", "basic") == "cloze":
        answers = "; ".join(cloze_answers(card.get("text", "")))
        extra = strip_html(card.get("extra", ""))
        return f"Đáp án: {answers}" + (f"\nNguồn/ghi chú: {extra}" if extra else "")
    front = strip_html(card.get("front", ""))
    back = strip_html(card.get("back", ""))
    extra = strip_html(card.get("extra", ""))
    return f"Câu hỏi: {front}\nĐáp án:\n{back}" + (f"\nNguồn/ghi chú: {extra}" if extra else "")


def build_sections(cards: list[dict]) -> dict[str, list[str]]:
    basic = [c for c in cards if c.get("type", "basic") == "basic" and c.get("front")]
    cloze = [c for c in cards if c.get("type") == "cloze" and c.get("text")]

    recall = [f"{strip_html(c['front'])}\n\nTrả lời: " for c in basic]

    numeric_cards = [c for c in cards if NUMERIC_RE.search(card_text(c))]
    numeric = []
    for c in numeric_cards:
        prompt = strip_html(c.get("front") or cloze_blank(c.get("text", "")))
        numeric.append(f"{prompt}\n\nTrả lời đầy đủ ngưỡng/số liệu: ")

    cloze_items = [f"{cloze_blank(c['text'])}\n\nTrả lời: " for c in cloze]

    case_cards = [c for c in basic if CASE_RE.search(card_text(c))]
    cases = [
        f"Tình huống ngắn: Bạn đang gặp một ca/bối cảnh liên quan đến nội dung sau. Hãy trả lời như khi đi lâm sàng.\n\n{strip_html(c['front'])}\n\nTrả lời: "
        for c in case_cards
    ]

    red_flag_cards = [c for c in cards if RED_FLAG_RE.search(card_text(c))]
    red_flags = []
    for c in red_flag_cards:
        prompt = strip_html(c.get("front") or cloze_blank(c.get("text", "")))
        red_flags.append(f"Điểm dễ sai/cần tránh trong câu này là gì?\n\n{prompt}\n\nTrả lời: ")

    return {
        "A. Closed-book recall": recall,
        "B. Thresholds and numbers": numeric,
        "C. Cloze drill": cloze_items,
        "D. Clinical mini-cases": cases,
        "E. Red-flag / common mistake check": red_flags,
    }


def rubric() -> str:
    return """## Cách chấm điểm

- 0 = không nhớ / sai nguy hiểm
- 1 = nhớ ý chính nhưng thiếu số liệu hoặc điều kiện
- 2 = đúng đầy đủ, có ngưỡng/số liệu/ngoại lệ quan trọng

Ngưỡng đạt:
- ≥80%: đạt
- 60-79%: cần ôn lại
- <60%: chưa đạt, không nên coi là nắm bài

Critical miss:
- Sai dose/timing/protocol/cutoff quan trọng = phải ôn lại dù tổng điểm cao
"""


def write_outputs(cards_path: Path, cards: list[dict], output_dir: Path | None = None) -> tuple[Path, Path, Path]:
    stem = topic_stem(cards_path)
    out_dir = (output_dir or cards_path.parent).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    check_path = out_dir / f"{stem}_knowledge_check.md"
    key_path = out_dir / f"{stem}_knowledge_check_answer_key.md"
    score_path = out_dir / f"{stem}_knowledge_check_score.json"

    sections = build_sections(cards)
    total = sum(len(v) for v in sections.values())

    check_parts = [f"# Knowledge Check — {stem}\n", rubric(), "\n> Làm closed-book trước. Sau đó tự chấm bằng answer key hoặc đưa file này cho Claude chấm.\n"]
    for title, items in sections.items():
        check_parts.append(f"\n## {title}\n\n{numbered(items)}\n")
    check_path.write_text("\n".join(check_parts), encoding="utf-8")

    key_parts = [f"# Answer Key — {stem}\n", rubric()]
    key_parts.append("\n## Đáp án theo thẻ gốc\n")
    key_parts.append(numbered([answer_block(c) for c in cards]))
    key_path.write_text("\n".join(key_parts), encoding="utf-8")

    score = {
        "topic": stem,
        "source_cards": str(cards_path),
        "total_questions": total,
        "section_counts": {k: len(v) for k, v in sections.items()},
        "max_score": total * 2,
        "learner_score": None,
        "percent": None,
        "status": "not_graded",
        "critical_misses": [],
        "weak_areas": [],
        "notes": "Điền kết quả sau khi tự làm bài hoặc nhờ Claude chấm theo answer key.",
    }
    score_path.write_text(json.dumps(score, ensure_ascii=False, indent=2), encoding="utf-8")
    return check_path, key_path, score_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a repeatable knowledge check from lesson cards")
    ap.add_argument("input", help="Path to lesson.cards.v2.json or lesson.md")
    ap.add_argument("--output-dir", type=Path, help="Output folder; release runner uses lesson/outputs")
    args = ap.parse_args()

    cards_path = find_cards_file(Path(args.input))
    cards = load_cards(cards_path)
    if not cards:
        print(f"[knowledge_check] No cards found: {cards_path}")
        return 2

    check_path, key_path, score_path = write_outputs(cards_path, cards, args.output_dir)
    print("[knowledge_check] Created:")
    print(f"  - {check_path}")
    print(f"  - {key_path}")
    print(f"  - {score_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
