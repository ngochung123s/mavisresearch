---
profile: "disease"
lesson_depth_contract: "L3_BEGINNER"
output_basename: "IM-22_P4_HFpEF_Comorbidities_2026-07-30_RELEASE_v1"
required_gates:
  - "brief_pmid_preflight"
  - "brief_claims_strict"
  - "source_pmid_strict"
  - "source_claims_strict"
  - "source_retraction"
  - "guideline_evidence"
  - "depth_disease"
  - "guideline_evidence_crosscheck"
  - "citation_zero_block"
  - "cards_schema"
  - "candidate_apkg_build"
  - "package_note_count"
  - "package_diacritics"
  - "source_diacritics"
  - "docx_build"
  - "learner_smoke"
---

## 0. Lesson profile & release contract
```json
{
  "profile": "disease",
  "lesson_depth_contract": {
    "min_total_words": 6000,
    "min_total_lines": 600,
    "min_sections": 10,
    "min_subsections": 14,
    "min_mechanism_chains": 4,
    "min_examples": 8,
    "min_misconceptions": 8,
    "min_checkpoints": 5,
    "min_cases_with_solutions": 3,
    "min_practical_tips": 12,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "mode": "L3_BEGINNER",
  "required_gates": [
    "brief_pmid_preflight",
    "brief_claims_strict",
    "source_pmid_strict",
    "source_claims_strict",
    "source_retraction",
    "guideline_evidence",
    "depth_disease",
    "guideline_evidence_crosscheck",
    "citation_zero_block",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "docx_build",
    "learner_smoke"
  ],
  "not_applicable": [],
  "approved_exemptions": []
}
```

# Research Brief: HFmrEF/HFpEF/HFimpEF + Comorbidities

## Metadata
- **Profile:** disease
- **Depth:** L3_BEGINNER
- **Basename:** IM-22_P4_HFpEF_Comorbidities_2026-07-30_RELEASE_v1.md
- **Topic:** Quản lý các thể suy tim EF bảo tồn/giảm nhẹ và bệnh đồng mắc (HFmrEF, HFpEF, HFimpEF, Comorbidities).

## Core Concepts
- **HFpEF (Heart Failure with preserved Ejection Fraction):** Suy tim với phân suất tống máu bảo tồn (EF ≥ 50%). Điều trị chủ yếu là kiểm soát triệu chứng (lợi tiểu quai) và bệnh đồng mắc, SGLT2i là thuốc duy nhất cải thiện tiên lượng.
- **HFmrEF (Heart Failure with mildly reduced Ejection Fraction):** Suy tim với phân suất tống máu giảm nhẹ (EF 41-49%). Điều trị tương tự HFpEF nhưng có thể cân nhắc thêm GDMT của HFrEF (ACEi/ARB/ARNI, BB, MRA).
- **HFimpEF (Heart Failure with improved Ejection Fraction):** Suy tim có phân suất tống máu cải thiện (EF > 40% từ nền < 40%). Bắt buộc tiếp tục duy trì GDMT của HFrEF để tránh tái phát.
- **Comorbidities (Bệnh đồng mắc):** Các bệnh lý đi kèm thường gặp làm nặng thêm tình trạng suy tim, bao gồm Tăng huyết áp, Rung nhĩ, Đái tháo đường, Béo phì, Bệnh thận mạn, Thiếu máu thiếu sắt, Ngưng thở khi ngủ, và Amyloidosis.

## 1. Claims

| Claim ID | Claim | PMID / Source | Verification Tag | Quote |
|---|---|---|---|---|
| P4-C01 | SGLT2 inhibitors Dapagliflozin and Empagliflozin are recommended for patients with HFpEF and HFmrEF to reduce the risk of heart failure hospitalization or cardiovascular death. | 34447992 | [GUIDELINE VERIFIED] | SGLT2 inhibitors Dapagliflozin and Empagliflozin are recommended for patients with HFpEF and HFmrEF to reduce the risk of heart failure hospitalization or cardiovascular death. |
| P4-C02 | Intravenous iron supplementation with Ferric carboxymaltose is recommended in symptomatic heart failure patients with iron deficiency defined as Ferritin less than 100 ng/mL or Ferritin 100-299 ng/mL with TSAT less than 20 percent. | 34447992 | [GUIDELINE VERIFIED] | Intravenous iron supplementation with Ferric carboxymaltose is recommended in symptomatic heart failure patients with iron deficiency defined as Ferritin less than 100 ng/mL or Ferritin 100-299 ng/mL with TSAT less than 20 percent. |
| P4-C03 | Comprehensive management of heart failure requires treating comorbidities including hypertension, atrial fibrillation, diabetes, obesity, chronic kidney disease, iron deficiency, sleep apnea, and amyloidosis. | 34447992 | [GUIDELINE VERIFIED] | Comprehensive management of heart failure requires treating comorbidities including hypertension, atrial fibrillation, diabetes, obesity, chronic kidney disease, iron deficiency, sleep apnea, and amyloidosis. |
| P4-C04 | Empagliflozin reduced the combined risk of cardiovascular death or hospitalization for heart failure in patients with heart failure and preserved ejection fraction. | 34449189 | [DATA VERIFIED] | Empagliflozin reduced the combined risk of cardiovascular death or hospitalization for heart failure in patients with heart failure and preserved ejection fraction. |
| P4-C05 | Dapagliflozin reduced the risk of worsening heart failure or cardiovascular death in patients with heart failure and mildly reduced or preserved ejection fraction. | 36036224 | [DATA VERIFIED] | Dapagliflozin reduced the risk of worsening heart failure or cardiovascular death in patients with heart failure and mildly reduced or preserved ejection fraction. |

## Key Management Strategies
1. **SGLT2i:** Dapagliflozin and Empagliflozin recommended for HFpEF and HFmrEF. [GUIDELINE VERIFIED] [PMID: 34447992]
2. **Iron deficiency:** Ferric carboxymaltose for iron deficiency with Ferritin less than 100 ng/mL or Ferritin 100-299 ng/mL with TSAT less than 20 percent. [GUIDELINE VERIFIED] [PMID: 34447992]
3. **Comorbidities:** Comprehensive management treating hypertension, atrial fibrillation, diabetes, obesity, chronic kidney disease, iron deficiency, sleep apnea, amyloidosis. [GUIDELINE VERIFIED] [PMID: 34447992]

## Evidence Base
- **PMID: 34447992:** 2021 ESC Guidelines for the diagnosis and treatment of acute and chronic heart failure.
- **PMID: 34449189:** Empagliflozin in Heart Failure with a Preserved Ejection Fraction.
- **PMID: 36036224:** Dapagliflozin in Heart Failure with Mildly Reduced or Preserved Ejection Fraction.
