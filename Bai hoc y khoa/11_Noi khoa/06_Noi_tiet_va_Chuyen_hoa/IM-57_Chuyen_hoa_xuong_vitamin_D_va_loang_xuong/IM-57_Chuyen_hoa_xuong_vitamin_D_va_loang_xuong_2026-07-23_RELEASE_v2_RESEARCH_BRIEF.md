# RESEARCH BRIEF: IM-57 — Chuyển hóa xương, vitamin D và loãng xương
**Ngày:** 2026-07-23 | **Profile:** foundation | **Đối tượng:** người học mất nền
**Rebuild từ:** v1 brief 2026-07-22 — không fetch lại PMIDs, kế thừa toàn bộ claims đã verify.

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "profile_foundation",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "learner_smoke"
  ],
  "not_applicable": ["drug_dosage_patterns"],
  "approved_exemptions": [
    {
      "gate": "drug_dosage_patterns",
      "reason": "Brief section 5 cấm đưa liều/lịch từng thuốc cụ thể vì không có guideline địa phương đã verify. Bảng thuốc section 8 chỉ liệt kê tên thuốc, đường dùng và ghi chú an toàn — không có số mg cụ thể. Gate drug_dosage_patterns không applicable cho bài này."
    }
  ]
}
```

**Output basename đã khóa:** `IM-57_Chuyen_hoa_xuong_vitamin_D_va_loang_xuong_2026-07-23_RELEASE_v2`.

## 1. Preflight guideline và phạm vi

Kế thừa từ v1 brief — NOGG 2024, Endocrine Society 2024, ISCD 2023, USPSTF 2025 đều WARN (không BLOCK). Freshness đã xác nhận: NOGG Updated December 2024, ISCD 2023, Endocrine Society PMID 38828931. NOGG là khung UK — ngưỡng/công cụ không áp thẳng sang Việt Nam.

## 2. Papers đã chọn (kế thừa từ v1, không fetch lại)

| PMID | Loại | Vai trò đã xác nhận |
|---|---|---|
| 35478046 | BHOF Clinician's Guide | Gãy ở người lớn tuổi là sentinel event; prevention, diagnosis, treatment, monitoring. |
| 38828931 | Endocrine Society guideline | Không dùng 25(OH)D thường quy để phòng bệnh ở người không có chỉ định. |
| 40921943 | NOGG 2024 guideline | Case finding, risk assessment, thuốc, sequence và follow-up. |
| 39808425 | USPSTF final recommendation | Screening phụ nữ từ 65 tuổi; selective screening phụ nữ trẻ hơn có nguy cơ. |
| 19671655 | FREEDOM RCT | Denosumab vs placebo; nguy cơ vertebral fracture tăng sau ngừng không kế hoạch. |
| 17476007 | HORIZON RCT | Zoledronic acid vs placebo ở postmenopausal osteoporosis. |
| 28892457 | ARCH RCT | Romosozumab rồi alendronate vs alendronate đơn thuần. |
| 29129436 | VERO RCT | Teriparatide vs risedronate ở severe osteoporosis. |
| 11346808 | PTH RCT | PTH(1-34) vs placebo ở phụ nữ sau mãn kinh có vertebral fracture. |
| 7477143 | Alendronate RCT | Alendronate vs placebo ở postmenopausal osteoporosis. |
| 17190893 | FLEX RCT | Continuing vs stopping alendronate after prior treatment. |
| 21411557 | FREEDOM subgroup | Denosumab fracture outcomes in higher-risk subgroups. |

## 3. Claims đã khóa (kế thừa từ v1)

Xem v1 brief — 12 claims đã verify với tags [ABSTRACT VERIFIED] / [GUIDELINE VERIFIED]. Không thêm claim mới.

## 4. Số liệu CẤM dùng (kế thừa từ v1)

- Không đưa ngưỡng vitamin D, liều calcium/vitamin D, interval DXA, duration drug holiday, **liều/lịch từng thuốc**, hoặc threshold treatment của UK vào bài/cards.
- Không đưa số liệu hiệu quả RCT (RR, CI, %, cỡ mẫu) vào bài/cards.
- Không biến T-score đơn lẻ hoặc 25(OH)D đơn lẻ thành chẩn đoán.

**Lý do drug_dosage gate = not_applicable:** Brief cấm liều cụ thể → bảng thuốc section 8 không có số mg → gate drug_dosage_patterns sẽ fail nhưng đây là intentional, không phải thiếu sót.
