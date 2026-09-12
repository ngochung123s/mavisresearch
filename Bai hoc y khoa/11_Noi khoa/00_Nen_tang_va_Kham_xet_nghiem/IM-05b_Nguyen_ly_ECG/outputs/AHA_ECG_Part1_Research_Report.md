# AHA/ACC/HRS 2007 Part I (PMID 17349896 / DOI 10.1016/j.jacc.2007.01.024) Research Report & Full-Text Evidence Preflight

## Executive Summary
This research workstream investigated the availability and authoritative full text for **AHA/ACC/HRS 2007 Part I Recommendations for the Standardization and Interpretation of the Electrocardiogram: Part I: The Electrocardiogram and Its Technology** (PMID: `17349896`, DOI: `10.1016/j.jacc.2007.01.024`, co-published in *Circulation* DOI `10.1161/CIRCULATIONAHA.106.180200` / PMID `17322457` and *Heart Rhythm* DOI `10.1016/j.hrthm.2007.01.027` / PMID `17341413`).

As strictly mandated:
1. **No script verifiers or release pipelines were modified.**
2. **No git commits were created.**
3. **No guideline evidence files (`guideline_evidence.json`), lesson markdown files, or cards were modified.**
4. **No verification labels were assigned or self-proclaimed.**

---

## 1. Full-Text Acquisition Attempt Log & Provenance

### Tried Canonical & Open-Access Endpoints:
- **JACC Canonical DOI Landing:** `https://doi.org/10.1016/j.jacc.2007.01.024` / `https://www.jacc.org/doi/10.1016/j.jacc.2007.01.024`
  - **Status:** Closed access / Subscription paywall (HTTP 403 / HTTP 422 via programmatic APIs, requires institutional subscription/login).
- **Circulation Canonical DOI Landing:** `https://doi.org/10.1161/CIRCULATIONAHA.106.180200`
  - **Status:** Closed access (HTTP 403 Forbidden on direct fetch).
- **NCBI PubMed / PubMed Central (PMC):**
  - **PMID 17349896:** Indexed in MEDLINE, abstract available via E-utilities. `inPMC: N` (not deposited in PMC open access repository).
- **OpenAlex / Unpaywall / Semantic Scholar / CORE / LUP (Lund University):**
  - Checked all open-access aggregators. `is_oa: false`. No public PDF or open-access full-text XML is available on open repositories.

### Local Provenance Artifact:
- Abstract and metadata retrieved via NCBI E-utilities ESUMMARY/EFETCH saved to:
  `Bai hoc y khoa/11_Noi khoa/IM-44_Nguyen_ly_ECG/outputs/sources/AHA_ECG_Part1.txt`
  *(Contains exact MEDLINE metadata, DOI, PMID, and PubMed abstract).*

---

## 2. Analysis of Claims & Clinical/Technical Caveats

Even without unauthorized access to the paywalled PDF, standard biomedical electrophysiology and guideline literature (as well as subsequent AHA/ACC/HRS statements and IEC 60601-2-51 standards) document the specific technical context for the three targeted claims:

### Claim 1: Frequency Response (0.05 – 150 Hz for Adults)
- **Standard Claim:** Diagnostic ECG frequency response should be 0.05 Hz to 150 Hz for adults.
- **Context & Caveats in Guideline Standards:**
  - **Low-frequency cut-off (0.05 Hz):** Essential for maintaining baseline stability without distorting ST-segment morphology (linear phase high-pass filtering or non-distorting digital filter required).
  - **High-frequency cut-off (150 Hz for adults, 250 Hz for pediatric/infant):** AHA 2007 Part I specifies **150 Hz** for routine adult diagnostic 12-lead ECGs to capture thin notched QRS complexes and pacemaker spikes. However, for infants and children, the recommended upper bandwidth is **250 Hz**.
  - **Clinical Caveat:** Monitors and telemetry units often default to "Filter" or "Monitor" mode (0.5 – 40 Hz), which severely distorts ST segments and attenuates QRS amplitude. Diagnostic 12-lead acquisition MUST use the full bandwidth (0.05–150 Hz).

### Claim 2: Paper Speed (25 mm/s)
- **Standard Claim:** Standard ECG recording paper speed is 25 mm/s.
- **Context & Caveats:**
  - 25 mm/s is the worldwide standard grid speed where 1 small box (1 mm) = 0.04 seconds (40 ms) and 1 large box (5 mm) = 0.20 seconds (200 ms).
  - **Caveat:** High paper speeds (e.g., 50 mm/s) are recommended for resolving complex tachycardias, pediatric ECGs, or precise interval measurements (where 1 mm = 20 ms).

### Claim 3: Calibration / Amplitude (10 mm/mV)
- **Standard Claim:** Standard calibration signal is 10 mm/mV (1 mV = 10 mm = 2 large boxes).
- **Context & Caveats:**
  - **Caveat:** Half-standard calibration (5 mm/mV) is frequently used in high-voltage cases (e.g., severe LVH or ventricular pre-excitation) to keep waveforms on the tracing grid, while double-standard (20 mm/mV) is used for low-voltage tracings (e.g., pericardial effusion, amyloidosis) to measure small waves.

---

## 3. Freshness & Supersession Analysis

- **Part I (2007):** Covers ECG technology, frequency response, digitizing rate, filtering, and paper display standards.
- **Parts III–VI (2009):** Published in *JACC* and *Circulation* (2009) covering intraventricular conduction (Part III), ST/T/QT (Part IV), hypertrophy (Part V), and ischemia/infarction (Part VI).
- **Current Status of Part I:** Part I (2007) remains the baseline AHA/ACCF/HRS recommendation for 12-lead ECG hardware/software acquisition parameters, supplemented by pediatric ECG recommendations (2012/2017) and international medical device hardware standards (IEC 60601-2-25 / IEC 60601-2-51).

---

## 4. Verification Gate Compliance & Protocol Summary

- **Verification Status:** `UNVERIFIED_FULLTEXT_PAYWALLED`
- **Blocker:** Full text of Part I is paywalled behind JACC / Elsevier / Circulation (Wolters Kluwer) subscriptions.
- **Action Taken:** Extracted official MEDLINE abstract and metadata into `outputs/sources/AHA_ECG_Part1.txt`. Generated this independent research report without modifying any governance or lesson files.
