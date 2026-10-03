"""Generate guideline_evidence.json from brief quotes (assert exact containment)."""
import hashlib
import json
import re
from pathlib import Path

BASE = Path("12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-51_Thap_tim")
ABS = Path("F:/DL/mavisresearch/Bai hoc y khoa") / BASE

GUIDELINES = {
    "AHA15": {
        "society": "AHA",
        "title": "Revision of the Jones Criteria for the Diagnosis of Acute Rheumatic Fever in the Era of Doppler Echocardiography: A Scientific Statement From the American Heart Association",
        "document_id": "AHA-2015-JONES",
        "version": "2015",
        "publication_date": "2015-04-01",
        "canonical_url": "https://www.ahajournals.org/doi/10.1161/CIR.0000000000000205",
        "local_copy": str(ABS / "sources" / "aha_2015_jones.txt"),
        "pmid": "25908771",
    },
    "AHA09": {
        "society": "AHA",
        "title": "Prevention of Rheumatic Fever and Diagnosis and Treatment of Acute Streptococcal Pharyngitis: A Scientific Statement From the American Heart Association",
        "document_id": "AHA-2009-RF-PREV",
        "version": "2009",
        "publication_date": "2009-03-01",
        "canonical_url": "https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.109.191959",
        "local_copy": str(ABS / "sources" / "aha_2009_rf_prevention.txt"),
        "pmid": "19246689",
    },
    "WHO24": {
        "society": "WHO",
        "title": "WHO guideline on the prevention and diagnosis of rheumatic fever and rheumatic heart disease",
        "document_id": "WHO-2024-RF-RHD",
        "version": "2024",
        "publication_date": "2024-10-01",
        "canonical_url": "https://www.who.int/publications/i/item/9789240100077",
        "local_copy": str(ABS / "sources" / "who_2024_rf_rhd.txt"),
        "pmid": None,
    },
    "WHF23": {
        "society": "WHF",
        "title": "2023 World Heart Federation guidelines for the echocardiographic diagnosis of rheumatic heart disease",
        "document_id": "WHF-2023-ECHO",
        "version": "2023",
        "publication_date": "2023-11-01",
        "canonical_url": "https://www.nature.com/articles/s41569-023-00940-9",
        "local_copy": str(ABS / "sources" / "whf_2023_echo_rhd.txt"),
        "pmid": "37914787",
    },
    "AUS25": {
        "society": "RHDA",
        "title": "Australian guideline for the prevention, diagnosis and management of acute rheumatic fever and rheumatic heart disease (Edition 3.3)",
        "document_id": "RHDA-2025-ARF-RHD",
        "version": "3.3-2025",
        "publication_date": "2025-08-01",
        "canonical_url": "https://www.rhdaustralia.org.au/arf-rhd-guidelines/",
        "local_copy": str(ABS / "sources" / "aus_2025_arf_rhd.txt"),
        "pmid": None,
    },
}

# claim -> (guideline key, locator)
CLAIM_MAP = {
    "C-001": ("AUS25", "Table 6.3, Chapter 6 Diagnosis of ARF"),
    "C-002": ("AUS25", "Table 6.3, Chapter 6 Diagnosis of ARF"),
    "C-003": ("AUS25", "Table 6.3 Major manifestations, Chapter 6"),
    "C-004": ("AUS25", "Table 6.3 Minor manifestations, Chapter 6"),
    "C-005": ("AUS25", "Table 6.3 footnote high-risk, Chapter 6"),
    "C-006": ("AUS25", "Table 6.3 footnote Strep A evidence, Chapter 6"),
    "C-007": ("AUS25", "Table 6.3 footnote chorea, Chapter 6"),
    "C-008": ("AUS25", "Table 6.3 footnote recurrence, Chapter 6"),
    "C-009": ("AHA15", "Abstract, Methods and results"),
    "C-010": ("AHA15", "Abstract, Conclusions"),
    "C-011": ("WHO24", "Section 4.5 Recommendation, p18-19"),
    "C-012": ("WHO24", "Section 4.6.1 Background, p20"),
    "C-013": ("WHO24", "Section 4.6.1 Background, p20"),
    "C-014": ("WHF23", "Box 2 New features"),
    "C-015": ("WHF23", "Confirmatory criteria pathological MR"),
    "C-016": ("WHF23", "Confirmatory criteria pathological AR"),
    "C-017": ("AHA09", "Abstract"),
    "C-018": ("AHA09", "Abstract"),
    "C-019": ("AHA09", "Abstract"),
    "C-020": ("WHO24", "Section 4.4 Recommendation 3, p17"),
    "C-021": ("WHO24", "Section 4.7 Recommendation 1, p26"),
    "C-022": ("WHO24", "Section 4.7 Recommendation 4, p26"),
    "C-023": ("WHO24", "Section 4.7.1 Background, p25"),
    "C-024": ("AUS25", "Table 10.2, Chapter 10 Secondary prophylaxis"),
    "C-025": ("AUS25", "Table 10.3, Chapter 10 Secondary prophylaxis"),
    "C-026": ("AUS25", "Table 5.3, Chapter 5 Primary prevention"),
    "C-027": ("AUS25", "Table 7.1 Eradication, Chapter 7"),
    "C-028": ("AUS25", "Table 7.1 Analgesia, Chapter 7"),
    "C-029": ("AUS25", "Table 7.1 Arthritis, Chapter 7"),
    "C-030": ("AUS25", "Table 7.1 Chorea, Chapter 7"),
    "C-031": ("AUS25", "Table 7.1 Carditis, Chapter 7"),
    "C-032": ("AUS25", "Table 7.1 Disease-modifying, Chapter 7"),
}

brief = (BASE / "PED-51_RESEARCH_BRIEF.md").read_text(encoding="utf-8")
quotes = {}
for line in brief.splitlines():
    if line.startswith("| C-"):
        cols = [c.strip() for c in line.split("|")]
        quotes[cols[1]] = (cols[5], cols[4])

entries = []
for cid, (gkey, locator) in CLAIM_MAP.items():
    quote, tag = quotes[cid]
    assert tag == "[GUIDELINE VERIFIED]", f"{cid} tag is {tag}"
    g = GUIDELINES[gkey]
    local_text = Path(g["local_copy"]).read_text(encoding="utf-8")
    assert quote in local_text, f"{cid} quote NOT exact substring of {gkey}"
    sha = hashlib.sha256(Path(g["local_copy"]).read_bytes()).hexdigest()
    entries.append({
        "claim_id": cid,
        "society": g["society"],
        "title": g["title"],
        "document_id": g["document_id"],
        "version": g["version"],
        "publication_date": g["publication_date"],
        "accessed_at": "2026-09-28",
        "canonical_url": g["canonical_url"],
        "local_copy": g["local_copy"],
        "sha256": sha,
        "recommendation_text": quote,
        "locator": locator,
        "pmid": g["pmid"],
        "superseded_by": None,
    })

out = BASE / "guideline_evidence.json"
out.write_text(json.dumps({"guidelines": entries}, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"WROTE {len(entries)} entries -> {out}")
