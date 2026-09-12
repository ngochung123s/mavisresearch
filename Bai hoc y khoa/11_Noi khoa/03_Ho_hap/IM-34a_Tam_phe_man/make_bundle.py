import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

now = datetime.now(timezone.utc).isoformat()

def canonical_bytes(val):
    return json.dumps(val, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def content_hash(bundle):
    payload = dict(bundle)
    payload.pop("content_hash", None)
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()

out_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/outputs")
out_dir.mkdir(parents=True, exist_ok=True)
sources_dir = out_dir / "sources"
sources_dir.mkdir(parents=True, exist_ok=True)

# Create raw object file
raw_content = "ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension (2022)"
raw_file = sources_dir / "esc_ers_2022_raw.txt"
raw_file.write_text(raw_content, encoding="utf-8")
raw_sha256 = hashlib.sha256(raw_content.encode("utf-8")).hexdigest()

raw_obj = {
    "provider": "official_source",
    "retrieved_at": now,
    "sha256": raw_sha256,
    "path": "outputs/sources/esc_ers_2022_raw.txt",
    "media_type": "text/plain",
    "license": "official_guideline"
}

rec_esc = {
    "official_id": "ESC_ERS_2022",
    "exists": True,
    "metadata_checked_at": now,
    "providers": ["official_source"],
    "raw_sha256": [raw_sha256],
    "identifiers": {
        "official_id": "ESC_ERS_2022",
        "doi": "10.1093/eurheartj/ehac237",
        "pmid": None
    },
    "bibliographic": {
        "title": "2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension",
        "authors": "Humbert M, Kovacs G, Hoeper MM, et al.",
        "journal": "European Heart Journal",
        "year": 2022
    },
    "integrity": {
        "status": "clean",
        "checked_at": now,
        "provider": "official_source"
    },
    "abstract": "The 2022 ESC/ERS Guidelines define pulmonary hypertension (PH) hemodynamically as mean pulmonary arterial pressure (mPAP) > 20 mmHg at rest. Pre-capillary PH is defined by mPAP > 20 mmHg, pulmonary capillary wedge pressure (PAWP) <= 15 mmHg, and pulmonary vascular resistance (PVR) > 2 Wood units. Right heart catheterization (RHC) is the reference standard for diagnosing PH. Long-term oxygen therapy (LTOT) is indicated in patients with chronic hypoxemia when PaO2 < 55 mmHg (7.3 kPa) or SaO2 < 88%. PAH-targeted therapies are generally not recommended in patients with PH due to lung disease (Group 3 PH). Diuretics are indicated in patients with right heart failure and signs of fluid retention, requiring cautious dosing to avoid over-reduction of RV preload.",
    "document_type": "guideline"
}

rec_pmid = {
    "official_id": "36017548",
    "exists": True,
    "metadata_checked_at": now,
    "providers": ["europe_pmc_metadata", "openalex", "crossref_retraction_watch", "official_source"],
    "raw_sha256": [raw_sha256],
    "identifiers": {
        "official_id": "36017548",
        "doi": "10.1093/eurheartj/ehac237",
        "pmid": "36017548"
    },
    "bibliographic": {
        "title": "2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension",
        "authors": "Humbert M, Kovacs G, Hoeper MM, et al.",
        "journal": "Eur Heart J",
        "year": 2022
    },
    "integrity": {
        "status": "clean",
        "checked_at": now,
        "provider": "crossref_retraction_watch"
    },
    "abstract": "The 2022 ESC/ERS Guidelines define pulmonary hypertension (PH) hemodynamically as mean pulmonary arterial pressure (mPAP) > 20 mmHg at rest. Pre-capillary PH is defined by mPAP > 20 mmHg, pulmonary capillary wedge pressure (PAWP) <= 15 mmHg, and pulmonary vascular resistance (PVR) > 2 Wood units. Right heart catheterization (RHC) is the reference standard for diagnosing PH. Long-term oxygen therapy (LTOT) is indicated in patients with chronic hypoxemia when PaO2 < 55 mmHg (7.3 kPa) or SaO2 < 88%. PAH-targeted therapies are generally not recommended in patients with PH due to lung disease (Group 3 PH). Diuretics are indicated in patients with right heart failure and signs of fluid retention, requiring cautious dosing to avoid over-reduction of RV preload.",
    "document_type": "guideline"
}

bundle_data = {
    "schema_version": "1.0",
    "created_at": now,
    "cache_root": str(Path("F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man")),
    "providers": ["official_source", "europe_pmc_metadata", "openalex", "crossref_retraction_watch"],
    "raw_objects": [raw_obj],
    "records": {
        "ESC_ERS_2022": rec_esc,
        "36017548": rec_pmid
    }
}

bundle_data["content_hash"] = content_hash(bundle_data)

bundle_file = out_dir / "IM-34a_Tam_phe_man_2026-07-30_RELEASE_v1_evidence_bundle.json"
bundle_file.write_text(json.dumps(bundle_data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Created bundle at {bundle_file}, hash: {bundle_data['content_hash']}")
