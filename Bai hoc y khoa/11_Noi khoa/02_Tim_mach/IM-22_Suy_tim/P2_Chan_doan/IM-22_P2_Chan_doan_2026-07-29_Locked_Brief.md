---
profile: "disease"
lesson_depth_contract: "L3_BEGINNER"
output_basename: "IM-22_P2_Chan_doan_2026-07-29_RELEASE_v1"
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

# Part 2: Chẩn đoán (Triệu chứng, Khám, Biomarker, Siêu âm tim) - Locked Research Brief

## Official Current Sources
- ACC/AHA/HFSA 2022 Guideline for the Management of Heart Failure [PMID: 35363499].

## 1. Claims to Verify

| Claim ID | Claim Content | Verification | Quote | Source |
|---|---|---|---|---|
| P2-C01 | Chẩn đoán (diagnose) suy tim (heart failure) bắt đầu bằng đánh giá xác suất tiền nghiệm dựa trên bệnh sử, khám lâm sàng và điện tâm đồ (ECG). | [FETCHED] | "heart failure" "diagnose" | PMID:35363499 |
| P2-C02 | Peptide lợi niệu (natriuretic peptides) như BNP và NT-proBNP là xét nghiệm có giá trị cao để loại trừ (rule out) suy tim (heart failure) nhờ độ nhạy cao. | [FETCHED] | "heart failure" | PMID:35363499 |
| P2-C03 | Siêu âm tim qua thành ngực (TTE) là xét nghiệm hình ảnh học quan trọng nhất để đánh giá cấu trúc và chức năng tim, bao gồm phân suất tống máu thất trái (LVEF), trong chẩn đoán suy tim (heart failure). | [FETCHED] | "heart failure" | PMID:35363499 |
| G-P2-SCOPE | Hướng dẫn AHA/ACC/HFSA 2022 nhằm cung cấp các khuyến nghị lấy người bệnh làm trung tâm cho bác sĩ lâm sàng để phòng ngừa, chẩn đoán (diagnose) và quản lý người bệnh suy tim (heart failure). | [GUIDELINE VERIFIED] | "The 2022 guideline is intended to provide patient-centric recommendations for clinicians to prevent, diagnose, and manage patients with heart failure." | PMID:35363499 |
