"""mcq_lint.py — Linter for single-best-answer MCQ banks (mcq_runner JSON format).

Checks item-writing flaws that let a test-wise student guess the key without
knowing the content (NBME Item-Writing Guide; Haladyna, Downing & Rodriguez 2002):

  per item   structure, duplicates, "all/none of the above", combination options,
             length cue (key much longer/shorter than distractors), absolute words
             only in distractors, clang (stem phrase repeated only in the key),
             negative lead-in.
  per bank   key-position balance, key-is-longest / key-is-shortest rate,
             key-is-most-similar (convergence) rate, numeric key-in-middle rate,
             vignette share, and the accuracy of a cue-only guesser that never
             reads the stem for meaning (should stay near chance).

Usage:
  python mcq_lint.py bank.json [more.json ...] [--json report.json] [--options N]
Exit code: 0 = no BLOCK, 1 = at least one BLOCK.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

BANNED_OPTION_PATTERNS = [
    r"tất cả (các )?(ý|câu|đáp án|phương án)",
    r"tất cả (đều )?(đúng|sai)",
    r"không (có )?(ý|câu|đáp án|phương án) nào",
    r"cả (hai|ba|bốn|[a-e] và [a-e])",
    r"^\s*[a-e]\s*(,|và|\+|&)\s*[a-e]\b",
    r"\b(all|none) of the above\b",
]
ABSOLUTE_WORDS = ["luôn luôn", "luôn", "không bao giờ", "tuyệt đối", "duy nhất", "hoàn toàn", "chắc chắn", "mọi trường hợp", "100%"]
NEGATIVE_LEADIN = re.compile(r"\b(KHÔNG|NGOẠI TRỪ|TRỪ|SAI)\b")
NEGATIVE_LEADIN_LOWER = re.compile(r"\bnào\b[^?]{0,25}\bkhông\b|\b(không đúng|ngoại trừ|là sai|không phải)\b", re.IGNORECASE)
STOP_SYLLABLES = set(
    "và hoặc của là có không được cho các những một trong với khi do bởi thì này đó ở tại từ đến theo như "
    "nhất hơn rất bị sẽ đã đang để về ra vào lên nên mà nhưng nếu thường gây trẻ bệnh nhân".split()
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "").lower()
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def syllables(s: str) -> list[str]:
    return re.findall(r"[0-9a-zà-ỹđ]+", norm(s))


def content_bigrams(s: str) -> set[tuple[str, str]]:
    syl = syllables(s)
    return {(a, b) for a, b in zip(syl, syl[1:]) if not (a in STOP_SYLLABLES and b in STOP_SYLLABLES)}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a | b else 0.0


def leading_number(s: str) -> float | None:
    m = re.match(r"^\s*[<>≤≥~]?\s*(\d+(?:[.,]\d+)?)", s)
    return float(m.group(1).replace(",", ".")) if m else None


def has_absolute(s: str) -> bool:
    t = norm(s)
    return any(re.search(r"(?<![0-9a-zà-ỹđ])" + re.escape(w) + r"(?![0-9a-zà-ỹđ])", t) for w in ABSOLUTE_WORDS)


def lint_item(q: dict, n_options: int | None) -> tuple[list[dict], dict]:
    issues: list[dict] = []
    qid = q.get("id", "?")

    def add(level: str, code: str, msg: str) -> None:
        issues.append({"id": qid, "level": level, "code": code, "msg": msg})

    opts = q.get("options") or []
    key = q.get("correct")
    stem = q.get("text") or ""
    if n_options and len(opts) != n_options:
        add("BLOCK", "option_count", f"{len(opts)} phương án, cần {n_options}")
    if len(opts) < 3:
        add("BLOCK", "option_count", "ít hơn 3 phương án")
    if not isinstance(key, int) or not (0 <= key < len(opts)):
        add("BLOCK", "key_index", f"correct={key!r} không hợp lệ")
        return issues, {}
    if not stem.strip():
        add("BLOCK", "empty_stem", "thân câu rỗng")
    if not (q.get("explanation") or "").strip():
        add("BLOCK", "no_explanation", "thiếu giải thích")
    oe = q.get("option_explanations")
    if oe is not None and len(oe) != len(opts):
        add("BLOCK", "option_explanations", "option_explanations không khớp số phương án")
    normed = [norm(o) for o in opts]
    if len(set(normed)) != len(normed):
        add("BLOCK", "duplicate_option", "có phương án trùng nhau")
    for i, o in enumerate(normed):
        for pat in BANNED_OPTION_PATTERNS:
            if re.search(pat, o):
                add("BLOCK", "banned_option", f"phương án {chr(65+i)} dạng tất cả/không/kết hợp: {opts[i]!r}")
                break

    lens = [len(o.strip()) for o in opts]
    dlens = [l for i, l in enumerate(lens) if i != key]
    mean_d = sum(dlens) / len(dlens)
    ratio = lens[key] / mean_d if mean_d else 1.0
    if ratio > 1.4 and lens[key] - max(dlens) > 8:
        add("BLOCK", "length_cue_long", f"đáp án dài gấp {ratio:.2f} trung bình nhiễu (key {lens[key]} ký tự, nhiễu dài nhất {max(dlens)})")
    elif ratio < 0.6 and min(dlens) - lens[key] > 8:
        add("WARN", "length_cue_short", f"đáp án ngắn bằng {ratio:.2f} trung bình nhiễu")

    abs_key = has_absolute(opts[key])
    abs_d = [i for i in range(len(opts)) if i != key and has_absolute(opts[i])]
    if abs_d and not abs_key:
        add("WARN", "absolute_in_distractor", "từ tuyệt đối chỉ nằm ở phương án nhiễu: " + ", ".join(chr(65 + i) for i in abs_d))

    stem_bg = content_bigrams(stem)
    clang = [content_bigrams(o) & stem_bg for o in opts]
    if clang[key] and not any(clang[i] for i in range(len(opts)) if i != key):
        add("WARN", "clang", "đáp án lặp cụm từ của thân câu mà nhiễu không có: " + ", ".join(" ".join(b) for b in sorted(clang[key])[:3]))

    leadin = stem.strip().splitlines()[-1] if stem.strip() else ""
    negative = bool(NEGATIVE_LEADIN.search(leadin) or NEGATIVE_LEADIN_LOWER.search(leadin))
    if NEGATIVE_LEADIN_LOWER.search(leadin) and not NEGATIVE_LEADIN.search(leadin):
        add("WARN", "negative_not_emphasised", "câu hỏi phủ định nhưng không VIẾT HOA từ phủ định")
    if not leadin.rstrip().endswith("?"):
        add("WARN", "leadin_not_question", "câu dẫn không kết thúc bằng câu hỏi đóng (?)")

    sets = [set(syllables(o)) for o in opts]
    sim = [sum(jaccard(sets[i], sets[j]) for j in range(len(opts)) if j != i) / (len(opts) - 1) for i in range(len(opts))]
    nums = [leading_number(o) for o in opts]
    numeric = all(v is not None for v in nums)
    key_mid = None
    if numeric:
        order = sorted(range(len(opts)), key=lambda i: nums[i])
        rank = order.index(key)
        key_mid = 0 < rank < len(opts) - 1
        if order != list(range(len(opts))):
            add("WARN", "numeric_order", "phương án số nên xếp tăng dần")

    feats = {
        "key": key,
        "n": len(opts),
        "key_longest": lens[key] == max(lens) and lens.count(max(lens)) == 1,
        "key_shortest": lens[key] == min(lens) and lens.count(min(lens)) == 1,
        "key_most_similar": sim[key] == max(sim) and sim.count(max(sim)) == 1,
        "numeric": numeric,
        "key_mid": key_mid,
        "negative": negative,
        "vignette": q.get("type") == "vignette",
        "guess": cue_guess(opts, stem, lens, sim, clang),
    }
    return issues, feats


def cue_guess(opts, stem, lens, sim, clang) -> int:
    """Guess the key from surface cues only (length, convergence, clang, absolutes)."""
    mean_l = sum(lens) / len(lens)
    sd_l = (sum((l - mean_l) ** 2 for l in lens) / len(lens)) ** 0.5 or 1.0
    mean_s = sum(sim) / len(sim)
    sd_s = (sum((s - mean_s) ** 2 for s in sim) / len(sim)) ** 0.5 or 1.0
    scores = []
    for i, o in enumerate(opts):
        s = (lens[i] - mean_l) / sd_l + (sim[i] - mean_s) / sd_s
        s += 1.0 * bool(clang[i]) - 1.5 * has_absolute(o)
        scores.append(s)
    return max(range(len(opts)), key=lambda i: scores[i])


def lint_bank(bank: dict, n_options: int | None) -> dict:
    qs = bank.get("questions") or []
    issues: list[dict] = []
    feats: list[dict] = []
    ids = Counter(q.get("id") for q in qs)
    for qid, c in ids.items():
        if c > 1:
            issues.append({"id": qid, "level": "BLOCK", "code": "duplicate_id", "msg": f"id lặp {c} lần"})
    stems = Counter(norm(q.get("text", "")) for q in qs)
    for s, c in stems.items():
        if c > 1:
            issues.append({"id": "-", "level": "BLOCK", "code": "duplicate_stem", "msg": f"thân câu lặp {c} lần: {s[:60]}"})
    for q in qs:
        it, f = lint_item(q, n_options)
        issues += it
        if f:
            feats.append(f)

    n = len(feats)
    stats: dict = {"items": n}
    if n:
        k = Counter(f["n"] for f in feats).most_common(1)[0][0]
        chance = 1 / k
        pos = Counter(f["key"] for f in feats)
        stats["key_positions"] = {chr(65 + i): pos.get(i, 0) for i in range(k)}
        rate = lambda name: sum(bool(f[name]) for f in feats) / n
        stats["key_longest_rate"] = round(rate("key_longest"), 3)
        stats["key_shortest_rate"] = round(rate("key_shortest"), 3)
        stats["key_most_similar_rate"] = round(rate("key_most_similar"), 3)
        stats["negative_rate"] = round(rate("negative"), 3)
        stats["vignette_rate"] = round(rate("vignette"), 3)
        stats["cue_guess_accuracy"] = round(sum(f["guess"] == f["key"] for f in feats) / n, 3)
        stats["chance"] = round(chance, 3)
        numeric = [f for f in feats if f["numeric"]]
        stats["numeric_items"] = len(numeric)

        def bank_issue(level, code, msg):
            issues.append({"id": "BANK", "level": level, "code": code, "msg": msg})

        tol = max(0.12, 2.2 * (chance * (1 - chance) / n) ** 0.5)
        if stats["key_longest_rate"] > chance + tol:
            bank_issue("BLOCK", "bank_key_longest", f"đáp án là phương án dài nhất ở {stats['key_longest_rate']:.0%} câu (ngẫu nhiên ≈ {chance:.0%})")
        elif n >= 12 and stats["key_longest_rate"] < chance - tol:
            bank_issue("BLOCK", "bank_key_never_longest", f"đáp án gần như không bao giờ là phương án dài nhất ({stats['key_longest_rate']:.0%}, ngẫu nhiên ≈ {chance:.0%}): người làm bài loại được phương án dài nhất")
        if stats["key_shortest_rate"] > chance + tol:
            bank_issue("WARN", "bank_key_shortest", f"đáp án là phương án ngắn nhất ở {stats['key_shortest_rate']:.0%} câu")
        if stats["key_most_similar_rate"] > chance + tol:
            bank_issue("BLOCK", "bank_convergence", f"đáp án giống các phương án khác nhất ở {stats['key_most_similar_rate']:.0%} câu (hội tụ)")
        if stats["cue_guess_accuracy"] > chance + tol:
            bank_issue("BLOCK", "bank_cue_guess", f"đoán bằng mẹo bề mặt đúng {stats['cue_guess_accuracy']:.0%} (ngẫu nhiên ≈ {chance:.0%})")
        if n >= 8:
            for i in range(k):
                share = pos.get(i, 0) / n
                if abs(share - chance) > tol:
                    bank_issue("WARN", "bank_key_position", f"đáp án {chr(65+i)} chiếm {share:.0%}")
        if len(numeric) >= 4:
            mid = sum(bool(f["key_mid"]) for f in numeric) / len(numeric)
            expected = (k - 2) / k
            stats["numeric_key_mid_rate"] = round(mid, 3)
            if mid > expected + 0.2:
                bank_issue("WARN", "bank_numeric_middle", f"câu số: đáp án nằm giữa dãy {mid:.0%}")
        if stats["negative_rate"] > 0.1:
            bank_issue("WARN", "bank_negative", f"câu phủ định chiếm {stats['negative_rate']:.0%} (nên ≤ 10%)")
    return {"bank": bank.get("id"), "title": bank.get("title"), "stats": stats, "issues": issues}


def load_banks(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "questions" in data:
        return [data]
    if isinstance(data, dict) and "banks" in data:
        return data["banks"]
    if isinstance(data, list):
        return data
    raise ValueError(f"{path}: không nhận ra định dạng ngân hàng câu hỏi")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--json", type=Path, help="ghi báo cáo đầy đủ ra file JSON")
    ap.add_argument("--options", type=int, default=None, help="số phương án bắt buộc mỗi câu")
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    reports = [lint_bank(b, a.options) for p in a.paths for b in load_banks(p)]
    blocks = 0
    for r in reports:
        lv = Counter(i["level"] for i in r["issues"])
        blocks += lv.get("BLOCK", 0)
        print(f"== {r['bank']} — {r['title']}")
        print("   " + json.dumps(r["stats"], ensure_ascii=False))
        print(f"   BLOCK={lv.get('BLOCK', 0)} WARN={lv.get('WARN', 0)}")
        for i in r["issues"]:
            print(f"   [{i['level']}] {i['id']} {i['code']}: {i['msg']}")
    if a.json:
        a.json.write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if blocks else 0


if __name__ == "__main__":
    sys.exit(main())
