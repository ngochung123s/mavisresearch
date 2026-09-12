# RESEARCH BRIEF & RELEASE CONTRACT: IM-34a Tâm phế mạn (Cor Pulmonale)

## 0. Lesson profile & release contract

```json
{
  "profile": "disease",
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
  "lesson_depth_contract": {
    "min_total_words": 10000,
    "min_total_lines": 800,
    "min_sections": 10,
    "min_subsections": 14,
    "min_mechanism_chains": 4,
    "min_examples": 8,
    "min_misconceptions": 8,
    "min_checkpoints": 5,
    "min_cases_with_solutions": 5,
    "min_practical_tips": 12,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [],
  "approved_exemptions": []
}
```

- **Output basename đã khóa:** `IM-34a_Tam_phe_man_2026-07-30_RELEASE_v1`
- **Tên bài học:** Tâm phế mạn (Cor Pulmonale)
- **Đường dẫn bài học:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/IM-34a_Tam_phe_man_2026-07-30_RELEASE_v1.md`
- **Đường dẫn Evidence Bundle:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-34a_Tam_phe_man/outputs/IM-34a_Tam_phe_man_2026-07-30_RELEASE_v1_evidence_bundle.json`

---

## 1. Phạm vi và preflight guideline

- **Chủ đề:** Tiếp cận, chẩn đoán, phân tầng nguy cơ và quản lý điều trị Tâm phế mạn (Cor Pulmonale) do bệnh lý hô hấp mạn tính.
- **Đối tượng:** Bác sĩ Nội khoa, sinh viên Y khoa, bác sĩ tuyến tỉnh.
- **Guideline chính:** ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension (2022).
- **Phạm vi được phép:** Tăng áp phổi Nhóm 3 (do bệnh phổi mạn tính / thiếu oxy máu mạn), phân biệt với Nhóm 1 (PAH), Nhóm 2 (bệnh tim trái), Nhóm 4 (CTEPH).
- **Ngoài phạm vi:** Điều trị sâu phẫu thuật/can thiệp thuyên tắc mạch, điều trị chuyên khoa sâu PAH Group 1 (ngoại trừ nguyên tắc không dùng thường quy cho Group 3).

---

## 2. Guidelines & Evidence

File `outputs/guideline_evidence.json`:
```json
{
  "guidelines": [
    {
      "claim_id": "C-001",
      "society": "ESC/ERS",
      "title": "2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension",
      "document_id": "ESC/ERS PH 2022",
      "version": "2022",
      "publication_date": "2022-08-26",
      "accessed_at": "2026-07-30",
      "canonical_url": "https://academic.oup.com/eurheartj/article/43/38/3618/6673929",
      "local_copy": "outputs/sources/esc_ers_2022_raw.txt",
      "sha256": "43a29db76b1f24ddb5dbbb4fb6bcf3a1a457eeae64d852077e68cf0cfbbf968b",
      "recommendation_text": "The 2022 ESC/ERS Guidelines define pulmonary hypertension (PH) hemodynamically as mean pulmonary arterial pressure (mPAP) > 20 mmHg at rest. Pre-capillary PH is defined by mPAP > 20 mmHg, pulmonary capillary wedge pressure (PAWP) <= 15 mmHg, and pulmonary vascular resistance (PVR) > 2 Wood units.",
      "locator": "Section 3, Page 5, Paragraph 1",
      "pmid": "36017548",
      "superseded_by": null
    }
  ]
}
```

---

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Định nghĩa huyết động tăng áp phổi mạn: mPAP > 20 mmHg | 36017548 | [GUIDELINE VERIFIED] | mean pulmonary arterial pressure (mPAP) > 20 mmHg at rest | Bệnh nhân nghi ngờ PH | RHC đo mPAP | Chẩn đoán PH | Ban đầu |
| C-002 | Định nghĩa tăng áp phổi tiền mao mạch: mPAP > 20 mmHg, PAWP <= 15 mmHg, PVR > 2 Wood units | 36017548 | [GUIDELINE VERIFIED] | Pre-capillary PH is defined by mPAP > 20 mmHg, pulmonary capillary wedge pressure (PAWP) <= 15 mmHg, and pulmonary vascular resistance (PVR) > 2 Wood units | Bệnh nhân PH tiền mao mạch | RHC | Phân loại huyết động | Ban đầu |
| C-003 | RHC là tiêu chuẩn tham chiếu (reference standard) để xác định chẩn đoán PH | 36017548 | [GUIDELINE VERIFIED] | Right heart catheterization (RHC) is the reference standard for diagnosing PH | Bệnh nhân nghi PH | RHC vs Non-invasive | Tiêu chuẩn chẩn đoán | Ban đầu |
| C-004 | Chỉ định LTOT khi PaO2 < 55 mmHg hoặc SaO2 < 88% ở bệnh nhân thiếu oxy mạn | 36017548 | [GUIDELINE VERIFIED] | Long-term oxygen therapy (LTOT) is indicated in patients with chronic hypoxemia when PaO2 < 55 mmHg (7.3 kPa) or SaO2 < 88% | Bệnh nhân COPD/bệnh phổi mạn | LTOT vs Không LTOT | Tỷ lệ sống còn | Dài hạn |
| C-005 | Không khuyến cáo dùng thuốc giãn mạch phổi (PAH-targeted therapy) thường quy cho Group 3 PH | 36017548 | [GUIDELINE VERIFIED] | PAH-targeted therapies are generally not recommended in patients with PH due to lung disease (Group 3 PH) | Bệnh nhân Group 3 PH | PAH-targeted drugs vs GDMT phổi | Kết cục lâm sàng | Dài hạn |
| C-006 | Thuốc lợi tiểu được chỉ định trong suy tim phải có ứ dịch, cần thận trọng tránh giảm quá mức tiền gánh thất phải | 36017548 | [GUIDELINE VERIFIED] | Diuretics are indicated in patients with right heart failure and signs of fluid retention, requiring cautious dosing to avoid over-reduction of RV preload | Bệnh nhân suy tim phải ứ dịch | Lợi tiểu liều điều chỉnh | Giảm sung huyết mà không tụt CO | Giai đoạn cấp/mạn |
| C-007 | Thuật ngữ Cor Pulmonale mô tả sự thay đổi cấu trúc/chức năng thất phải do bệnh lý hệ hô hấp | 36017548 | [GUIDELINE VERIFIED] | Cor pulmonale refers to right ventricular alteration caused by pulmonary hypertension secondary to lung disease | Bệnh nhân bệnh phổi mạn | Đánh giá thất phải | Định nghĩa bệnh | Mạn tính |

---

## 4. Claims và số liệu cấm dùng

- Cấm tự chế các con số định lượng về tỷ lệ tử vong %, RR, OR chưa được verify từ bundle.
- Cấm tự gán các nhãn verification cũ (`[FULL VERIFIED]`, `[ABSTRACT MATCH]`, `[TEXTBOOK]`).

---

## 5. Dàn ý chi tiết (18 Sections)

1. **0. TỔNG QUAN — VÌ SAO BÀI NÀY QUAN TRỌNG?**
2. **0.1 NỀN TẢNG TỐI THIỂU CẦN DÙNG NGAY**
3. **1. ĐỊNH NGHĨA VÀ LỊCH SỬ THUẬT NGỮ [CỐT LÕI]**
4. **2. SINH LÝ VÀ CƠ CHẾ BỆNH SINH [CỐT LÕI]**
5. **3. NGUYÊN NHÂN VÀ PHÂN LOẠI ETIOLOGY [CỐT LÕI]**
6. **4. BIỂU HIỆN LÂM SÀNG VÀ KHÁM THỂ CHẤT [CỐT LÕI]**
7. **5. CẬN LÂM SÀNG CƠ BẢN: ECG VÀ X-QUANG NGỰC [CỐT LÕI]**
8. **6. SIÊU ÂM TIM VÀ ĐÁNH GIÁ CHỨC NĂNG THẤT PHẢI [CỐT LÕI]**
9. **7. XÉT NGHIỆM KHÍ MÁU VÀ CHỨC NĂNG HÔ HẤP [CỐT LÕI]**
10. **8. THÔNG TIM PHẢI VÀ CHỈ ĐỊNH CHUYỂN TUYẾN CHUYÊN KHOA [CỐT LÕI]**
11. **9. CHẨN ĐOÁN PHÂN BIỆT RÕ RÀNG [CỐT LÕI]**
12. **10. NGUYÊN TẮC ĐIỀU TRỊ VÀ QUẢN LÝ BỆNH NỀN HÔ HẤP [CỐT LÕI]**
13. **11. LIỆU PHÁP OXY DÀI HẠN (LTOT) VÀ THÔNG KHÍ HỖ TRỢ [CỐT LÕI]**
14. **12. NGUYÊN TẮC SỬ DỤNG THUỐC LỢI TIỂU VÀ THẬN TRỌNG HUYẾT ĐỘNG [CỐT LÕI]**
15. **13. VÀI TRÒ VÀ GIỚI HẠN CỦA THUỐC GIÃN MẠCH PHỔI (PAH-TARGETED THERAPY) [CỐT LÕI]**
16. **14. ĐỢT MẤT BÙ CẤP TÍNH VÀ SUY THẤT PHẢI CẤP (DECOMPENSATED RV FAILURE) [CỐT LÕI]**
17. **15. TIÊN LƯỢNG, PHỤC HỒI CHỨC NĂNG VÀ QUẢN LÝ DÀI HẠN [CỐT LÕI]**
18. **16. LƯU ĐỒ QUYẾT ĐỊNH LÂM SÀNG, BỐI CẢNH VIỆT NAM VÀ PLAN B [CỐT LÕI]**
