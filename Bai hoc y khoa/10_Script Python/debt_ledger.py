# -*- coding: utf-8 -*-
"""debt_ledger.py — sinh SỔ NỢ chất lượng cho bài cũ của mọi chuyên khoa.

    python debt_ledger.py            # ghi Bai hoc y khoa/_DEBT_LEDGER.md + _DEBT_LEDGER.json

Bài cũ không bị chặn (policy RULES_LESSON_APKG.md §8): mọi lỗi của lesson_lint và card_lint được chạy ở mode
`hotfix` và ghi thành nợ. Khi một bài được viết lại / nâng cấp, nó phải qua `release_lesson.py --mode release`
(0 nợ) thì mới được xóa khỏi sổ. File sinh tự động — không sửa tay.
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import card_lint  # noqa: E402
import lesson_lint  # noqa: E402
import specialties  # noqa: E402

ROOT = specialties.LESSONS_ROOT
LABELS = {"M": "manifest", "S": "cấu trúc/độ sâu", "F": "định dạng", "C": "chuỗi cơ chế", "I": "ảnh", "V": "nhãn/artifact",
          "T": "kỹ thuật thẻ", "P": "nguồn ở mặt sau", "D": "deck", "G": "quy chuẩn thẻ"}


def families(by_code: dict) -> str:
    fam = Counter()
    for code, n in by_code.items():
        fam[code.split("_", 1)[0]] += n
    return ", ".join(f"{LABELS.get(k, k)} {v}" for k, v in fam.most_common()) or "—"


def main() -> int:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    lessons = lesson_lint.scan(ROOT)
    decks = defaultdict(list)
    for path in card_lint.release_apkgs(ROOT):
        issues, meta = card_lint.lint_apkg(path, "hotfix")
        s = card_lint.summarize(issues)
        decks[(meta["specialty"], meta["id"])].append({"apkg": str(path.relative_to(ROOT)).replace("\\", "/"), **meta,
                                                       "block": s["block"], "debt": s["debt"], "by_code": s["by_code"]})
    rows = []
    for row in lessons:
        row["decks"] = decks.pop((row["specialty"], row["id"]), [])
        rows.append(row)
    for (spec_key, lesson_id), items in decks.items():  # APKG không có bài .md tương ứng
        rows.append({"specialty": spec_key, "id": lesson_id, "folder": str(Path(items[0]["apkg"]).parent), "manifest": False,
                     "profile": None, "lesson": None, "debt": 0, "by_code": {}, "depth_fails": [], "decks": items})

    out_json = ROOT / "_DEBT_LEDGER.json"
    out_json.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# SỔ NỢ CHẤT LƯỢNG BÀI HỌC & APKG (tự sinh — không sửa tay)",
        "",
        f"> Sinh bởi `10_Script Python/debt_ledger.py` lúc {dt.datetime.now():%Y-%m-%d %H:%M}. "
        "Bài cũ không bị chặn; nâng cấp bài = chạy `release_lesson.py --mode release` đạt 0 nợ. "
        "Quy tắc: `RULES_LESSON_APKG.md`.",
        "",
        "| Chuyên khoa | Số bài | Có lesson.json | Bài đạt 0 nợ (bài) | Deck 0 nợ | Deck còn lỗi chặn |",
        "|---|---|---|---|---|---|",
    ]
    for spec in specialties.load().values():
        sub = [r for r in rows if r["specialty"] == spec.key]
        if not sub:
            continue
        all_decks = [d for r in sub for d in r["decks"]]
        lines.append(f"| {spec.name} | {len(sub)} | {sum(1 for r in sub if r['manifest'])} | "
                     f"{sum(1 for r in sub if r['lesson'] and r['debt'] == 0)} | "
                     f"{sum(1 for d in all_decks if d['debt'] == 0 and d['block'] == 0)}/{len(all_decks)} | "
                     f"{sum(1 for d in all_decks if d['block'])} |")
    for spec in specialties.load().values():
        sub = sorted((r for r in rows if r["specialty"] == spec.key), key=lambda r: r["id"])
        if not sub:
            continue
        lines += ["", f"## {spec.name} (`{spec.folder}`)", "",
                  "| Mã | Bài .md | Nợ bài | Gate độ sâu chưa đạt | APKG | Nợ thẻ |", "|---|---|---|---|---|---|"]
        for r in sub:
            lesson = r["lesson"] or "— (chưa có .md)"
            depth = "; ".join(r["depth_fails"][:4]) + (" …" if len(r["depth_fails"]) > 4 else "") if r["depth_fails"] else "—"
            if r["decks"]:
                for i, d in enumerate(r["decks"]):
                    first = i == 0
                    lines.append(f"| {r['id'] if first else ''} | {lesson if first else ''} | "
                                 f"{(families(r['by_code']) if first else '')} | {depth if first else ''} | "
                                 f"{Path(d['apkg']).name} | {'⛔ ' if d['block'] else ''}{families(d['by_code'])} |")
            else:
                lines.append(f"| {r['id']} | {lesson} | {families(r['by_code'])} | {depth} | — | — |")
    (ROOT / "_DEBT_LEDGER.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Đã ghi {out_json.name} + _DEBT_LEDGER.md: {len(rows)} bài, {sum(len(r['decks']) for r in rows)} APKG")
    return 0


if __name__ == "__main__":
    sys.exit(main())
