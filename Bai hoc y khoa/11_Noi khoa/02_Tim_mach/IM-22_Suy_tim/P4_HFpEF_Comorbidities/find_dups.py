import re
from pathlib import Path

text = Path("F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/P4_HFpEF_Comorbidities/IM-22_P4_HFpEF_Comorbidities_2026-07-30_RELEASE_v1.md").read_text(encoding="utf-8")
lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
candidates = [ln for ln in lines if len(ln) >= 25 and not ln.startswith("#") and not ln.startswith("```") and not ln.startswith("|---")]
seen = set()
for ln in candidates:
    if ln in seen:
        print("VERBATIM DUP:", repr(ln))
    else:
        seen.add(ln)

norm_counts = {}
for ln in candidates:
    norm = re.sub(r"\d+", "N", ln)
    norm_counts[norm] = norm_counts.get(norm, 0) + 1
for norm, count in norm_counts.items():
    if count >= 3:
        print("TEMPLATE REPEAT:", count, repr(norm[:80]))
