"""Generate abstract_match.jsonl (Gate 1) from brief quotes + abstracts."""
import glob
import json
import re
from pathlib import Path

BASE = Path("12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-51_Thap_tim")

brief = (BASE / "PED-51_RESEARCH_BRIEF.md").read_text(encoding="utf-8")
claims = {}
for line in brief.splitlines():
    if line.startswith("| C-"):
        cols = [c.strip() for c in line.split("|")]
        claims[cols[1]] = {"claim": cols[2], "pmid": cols[3], "tag": cols[4], "quote": cols[5]}

ab = {}
for f in glob.glob(str(BASE / "tmp_search" / "abstract_*.txt")) + glob.glob(str(BASE / "tmp_search" / "epmc_abstract_*.txt")):
    m = re.search(r"(\d{8})", Path(f).name)
    if m and "wrapped" not in f:
        ab.setdefault(m.group(1), Path(f).read_text(encoding="utf-8"))

TYPES = {
    "C-009": "factual", "C-010": "factual",
    "C-017": "factual", "C-018": "factual", "C-019": "factual",
    "C-033": "numeric", "C-034": "numeric", "C-035": "numeric",
    "C-036": "numeric", "C-037": "numeric", "C-038": "numeric",
    "C-039": "factual",
}
# WHF claims verified via full-text PDF, not abstract
FULLTEXT_ONLY = {"C-014": "37914787", "C-015": "37914787", "C-016": "37914787"}

rows = []
for cid, ctype in TYPES.items():
    c = claims[cid]
    pmid = re.search(r"(\d{8})", c["pmid"]).group(1)
    abstract = ab[pmid]
    clean = re.sub(r"<[^>]+>", " ", abstract)
    clean = re.sub(r"\s+", " ", clean)
    if c["quote"] in abstract or c["quote"] in clean:
        match, reason = True, "Quote is exact substring of abstract."
    else:
        match, reason = False, "Quote NOT found in abstract — INVESTIGATE."
    rows.append({"pmid": pmid, "claim_id": cid, "claim_text": c["claim"],
                 "abstract_snippet": c["quote"][:400], "claim_type": ctype,
                 "match": match, "reason": reason})

for cid, pmid in FULLTEXT_ONLY.items():
    c = claims[cid]
    rows.append({"pmid": pmid, "claim_id": cid, "claim_text": c["claim"],
                 "abstract_snippet": "N/A - Doppler/staging numbers are in full-text PDF, not abstract.",
                 "claim_type": "guideline", "match": False,
                 "reason": "Verified via full-text PDF (whf_2023_echo_rhd.pdf + excerpt); see full_verify_table.md and guideline_evidence.json."})

out = BASE / "abstract_match.jsonl"
with open(out, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
n_true = sum(1 for r in rows if r["match"] is True)
print(f"WROTE {len(rows)} rows ({n_true} match=true) -> {out}")
bad = [r["claim_id"] for r in rows if r["match"] is not True and r["claim_id"] not in FULLTEXT_ONLY]
print("UNEXPECTED FAILS:", bad)
assert not bad
