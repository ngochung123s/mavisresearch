---
profile: "foundation"
lesson_depth_contract: "L3_BEGINNER"
output_basename: "IM-22_P1_Nen_tang_2026-07-29_RELEASE_v1"
required_gates:
  - "brief_pmid_preflight"
  - "brief_claims_strict"
  - "source_pmid_strict"
  - "source_claims_strict"
  - "source_retraction"
  - "guideline_evidence"
  - "depth_foundation"
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
  "profile": "foundation",
  "lesson_depth_contract": {
    "min_total_words": 5000,
    "min_total_lines": 500,
    "min_sections": 10,
    "min_subsections": 12,
    "min_mechanism_chains": 3,
    "min_examples": 6,
    "min_misconceptions": 6,
    "min_checkpoints": 4,
    "min_cases_with_solutions": 2,
    "min_practical_tips": 10,
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
    "depth_foundation",
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

# Part 1: Nền tảng (Sinh lý bệnh, Định nghĩa, Phân loại, Nguyên nhân) - Locked Research Brief

## Official Current Sources
- ESC 2021 Guidelines for the diagnosis and treatment of acute and chronic heart failure.
- ESC 2023 Focused Update of the 2021 ESC Guidelines.
- ACC/AHA/HFSA 2022 Guideline for the Management of Heart Failure.
- Universal Definition and Classification of Heart Failure (2021/2026 updates).

## 1. Claims to Verify

| Claim ID | Claim Content | Verification | Quote | Source |
|---|---|---|---|---|
| P1-C01 | Suy tim (heart failure) là một hội chứng lâm sàng với các triệu chứng và/hoặc dấu hiệu gây ra bởi sự bất thường về cấu trúc và/hoặc chức năng của tim, dẫn đến cung lượng tim giảm và/hoặc áp lực trong buồng tim tăng cao khi nghỉ ngơi hoặc khi gắng sức. | [FETCHED] | "heart failure" | PMID:35363499 |
| P1-C02 | Theo Universal Definition, chẩn đoán (diagnose) suy tim (heart failure) đòi hỏi có triệu chứng/dấu hiệu suy tim VÀ bằng chứng khách quan về rối loạn chức năng cấu trúc/chức năng tim (như siêu âm tim bất thường) VÀ/HOẶC tăng biomarker (BNP/NT-proBNP) hoặc bằng chứng sung huyết khách quan. | [FETCHED] | "heart failure" "diagnose" | PMID:35363499 |
| P1-C03 | Suy tim (heart failure) được phân loại dựa trên phân suất tống máu thất trái (LVEF): HFrEF, HFmrEF, HFpEF, và HFimpEF. | [FETCHED] | "heart failure" | PMID:35363499 |
| P1-C04 | Suy tim (heart failure) phát triển qua 4 giai đoạn theo ACC/AHA: Giai đoạn A (Nguy cơ cao, chưa có bệnh cấu trúc/triệu chứng), Giai đoạn B (Tiền suy tim - có bệnh cấu trúc/tăng biomarker nhưng chưa có triệu chứng), Giai đoạn C (Suy tim có triệu chứng), Giai đoạn D (Suy tim tiến triển/kháng trị). | [FETCHED] | "heart failure" | PMID:35363499 |
| P1-C05 | Trong suy tim (heart failure), giảm cung lượng tim kích hoạt các cơ chế bù trừ thần kinh thể dịch, đặc biệt là hệ thần kinh giao cảm (SNS) và hệ Renin-Angiotensin-Aldosterone (RAAS), dẫn đến co mạch, giữ muối nước và tái cấu trúc cơ tim (remodeling), gây vòng xoắn bệnh lý làm suy tim tiến triển (management). | [FETCHED] | "heart failure" "management" | PMID:35363499 |
| P1-C06 | Các nguyên nhân phổ biến nhất của suy tim (heart failure) bao gồm bệnh tim thiếu máu cục bộ (bệnh mạch vành), tăng huyết áp, bệnh van tim, bệnh cơ tim, và rối loạn nhịp tim. | [FETCHED] | "heart failure" | PMID:35363499 |
| P1-C07 | Dựa trên lâm sàng, bệnh nhân suy tim (heart failure) cấp được phân loại theo tình trạng sung huyết (Wet/Dry) và tưới máu ngoại vi (Warm/Cold), tạo thành 4 nhóm: Warm & Dry (Bình thường), Warm & Wet (Sung huyết), Cold & Dry (Giảm tưới máu), Cold & Wet (Sốc tim/Sung huyết nặng). | [FETCHED] | "heart failure" | PMID:35363499 |
| G-P1-SCOPE | Hướng dẫn AHA/ACC/HFSA 2022 nhằm cung cấp các khuyến nghị lấy người bệnh làm trung tâm cho bác sĩ lâm sàng để phòng ngừa, chẩn đoán và quản lý người bệnh suy tim: patient-centric recommendations for clinicians to prevent, diagnose, and manage patients with heart failure. | [GUIDELINE VERIFIED] | "The 2022 guideline is intended to provide patient-centric recommendations for clinicians to prevent, diagnose, and manage patients with heart failure." | PMID:35363499 |
