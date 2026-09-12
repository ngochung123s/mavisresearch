# Europe PMC provider probe — IM-04

- **Timestamp (UTC):** `2026-07-29T08:48:34Z`
- **Provider / endpoint:** Europe PMC, `https://www.ebi.ac.uk/europepmc/webservices/rest/`
- **Skill used:** `literature-search-europepmc`
- **Wrapper:** `skill://literature-search-europepmc/scripts/europepmc_api.py`
- **Rate limit:** `1 request/second` (wrapper `qps=1.0`; an explicit `sleep 1` was also placed between the two invocations)
- **Result type:** `core`
- **NCBI E-utilities:** not called
- **Scope:** provider probe only. No verification label is assigned and no verifier is modified.

## Commands

```text
uv run skill://literature-search-europepmc/scripts/europepmc_api.py search "EXT_ID:29910186 AND SRC:MED" --max_results 10 --result_type core --output _tmp/europepmc_provider_probe/29910186.json
sleep 1
uv run skill://literature-search-europepmc/scripts/europepmc_api.py search "EXT_ID:27235445 AND SRC:MED" --max_results 10 --result_type core --output _tmp/europepmc_provider_probe/27235445.json
```

The wrapper automatically appended `OPEN_ACCESS:y`. Effective queries:

```text
(EXT_ID:29910186 AND SRC:MED) AND OPEN_ACCESS:y
(EXT_ID:27235445 AND SRC:MED) AND OPEN_ACCESS:y
```

## Results

### PMID 29910186

`hitCount = 1`.

| Requested datum | Europe PMC response |
|---|---|
| title | `Structural Basis of Phosphatidic Acid Sensing by APH in Apicomplexan Parasites.` |
| journal | `Structure (London, England : 1993)` |
| year | `2018` |
| abstractText | Present; full value preserved in JSON and raw evidence |
| pmid | `29910186` |
| pmcid | `PMC6084407` |
| DOI | `10.1016/j.str.2018.05.001` (response key: `doi`) |
| authorString | `Darvill N, Dubois DJ, Rouse SL, Hammoudi PM, Blake T, Benjamin S, Liu B, Soldati-Favre D, Matthews S.` |
| publicationTypes | Exact key absent. Semantic values returned under `pubTypeList.pubType`: `Research Support, Non-U.S. Gov't`; `research-article`; `Journal Article` |
| isOpenAccess | `Y` |
| retractedIn | Field absent |
| retractedBy | Field absent |
| expression of concern | No corresponding field observed |

Paper URL: https://europepmc.org/article/MED/29910186

### PMID 27235445

`hitCount = 0`; no record and therefore none of the requested fields were returned.

Because the actual query included `OPEN_ACCESS:y`, this result **does not establish that PMID 27235445 does not exist**. It only establishes that the wrapper returned no match for the open-access-filtered query. No inference about title, journal, year, abstract, identifiers, publication type, or retraction/EOC status is made.

Reference URL: https://europepmc.org/article/MED/27235445

## Field coverage in this two-PMID probe

| Field / function | Coverage | Long-term provider implication |
|---|---:|---|
| PMID existence | One positive hit; one ambiguous zero | **Insufficient for general existence checks** with this wrapper. A positive exact-ID hit is usable; a zero hit cannot distinguish absent from non-open-access. |
| abstractText | 1/2 | **Conditionally sufficient for abstract matching** when a hit contains `abstractText`; unavailable for the zero-hit PMID. |
| title / journal / year | 1/2 each | Available on the positive core record; unavailable on the filtered-out/absent record. |
| pmid / pmcid / DOI | 1/2 each | Useful cross-identifiers on a positive record, not complete across candidates. |
| authorString | 1/2 | Available on the positive record. |
| publication types | 1/2 semantically; exact requested key 0/2 | Returned as `pubTypeList.pubType`, not `publicationTypes`. The list mixes `research-article`, `Journal Article`, and funding/support categorization; an explicit mapping would be required, and NCBI-equivalent completeness must not be assumed. |
| isOpenAccess | 1/2 | Expected because the wrapper enforces OA; no datum on the zero hit. |
| retractedIn / retractedBy | 0/2 fields present | **Insufficient for retraction screening.** Absence of these fields is not evidence of no retraction. |
| expression of concern | 0/2 fields present | **Insufficient for EOC screening.** No status/relationship field was observed. |

## Data missing relative to an unfiltered NCBI PubMed lookup

Without calling NCBI, this probe shows the following required data are missing or not equivalent:

1. No unfiltered PMID-existence answer for `27235445` because the mandated wrapper restricts searches to open access.
2. No metadata or abstract for `27235445`.
3. No exact `publicationTypes` field; only `pubTypeList.pubType` was observed for the positive hit, with mixed label semantics.
4. No explicit retraction or expression-of-concern relationship/status fields in the positive record. Their absence cannot be interpreted as a clean status.

## Assessment

Europe PMC via the mandated skill wrapper is **not sufficient as a complete long-term replacement for NCBI for PMID existence**, because mandatory `OPEN_ACCESS:y` introduces false-negative ambiguity for non-open-access records. It **is sufficient for PMID + abstract matching only when an exact-ID hit returns `abstractText`**, as occurred for `29910186`; it is not sufficient for `27235445` in this probe.

For a long-term provider, publication-type normalization and a separately demonstrated retraction/EOC mechanism would be required. This probe supplies neither evidence of full publication-type equivalence nor reliable negative retraction/EOC status.

## Evidence

- `EUROPE_PMC_PROVIDER_PROBE.json`
- `EUROPE_PMC_RAW_29910186.json`
- `EUROPE_PMC_RAW_27235445.json`

License notice recorded at workspace root: `.licenses/literature_search_europepmc_LICENSE.txt`. The user must review https://europepmc.org/ and check each paper's license for restrictions.
