# RESEARCH BRIEF: RỐI LOẠN TOAN KIỀM & ĐỌC KHÍ MÁU ĐỘNG MẠCH Ở TRẺ EM (PED-11)

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
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
    "source_diacritics"
  ],
  "lesson_depth_contract": {
    "min_total_words": 5000,
    "min_total_lines": 500,
    "min_sections": 10,
    "min_subsections": 12,
    "min_mechanism_chains": 3,
    "min_examples": 6,
    "min_misconceptions": 6,
    "min_checkpoints": 4,
    "min_cases_with_solutions": 3,
    "min_practical_tips": 10,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "docx_build",
    "learner_smoke"
  ],
  "approved_exemptions": [
    "APKG artifacts postponed until both PED-50 and PED-11 theoretical modules are completed, per explicit clinical developer instruction."
  ]
}
```

---

## 1. Phạm vi, mục tiêu & văn bản hướng dẫn cốt lõi (Guidelines)

### 1.1 Mục tiêu đào tạo
- Làm chủ sinh lý điều hòa thăng bằng toan kiềm ở trẻ em: Phương trình Henderson-Hasselbalch, 3 hàng rào bảo vệ (hệ đệm ngoại bào Bicarbonat $\text{HCO}_3^-$, đáp ứng thông khí nhanh của phổi, đáp ứng bài tiết và tái hấp thu chậm của thận).
- Nắm vững các chỉ số khí máu động mạch (ABG) bình thường theo lứa tuổi (Sơ sinh, Nhũ nhi, Trẻ lớn) và phân biệt rạch ròi khí máu động mạch (ABG) vs khí máu tĩnh mạch (VBG).
- Phân biệt bản chất 4 rối loạn toan kiềm tiên phát: Toan chuyển hóa, Kiềm chuyển hóa, Toan hô hấp và Kiềm hô hấp.
- Nắm vững cơ chế sinh toan trong mất nước nặng: Toan chuyển hóa tăng Anion Gap (toan Lactic do giảm tưới máu mô) kết hợp Toan chuyển hóa Anion Gap bình thường (mất trực tiếp $\text{HCO}_3^-$ qua phân kèm tăng Clo máu bù trừ).
- Phân tích cơ chế kiềm chuyển hóa giảm Clo và giảm Kali trong hẹp phì đại môn vị ở trẻ nhũ nhi (HPS) kèm nước tiểu toan nghịch lý.
- Làm chủ lưu đồ 5 bước đọc khí máu động mạch tại giường: Đánh giá $\text{pH} \rightarrow$ Xác định rối loạn tiên phát $\rightarrow$ Kiểm tra bù trừ bằng công thức Winter $\rightarrow$ Tính Anion Gap $\rightarrow$ Tính Delta Gap ($\Delta\text{AG}/\Delta\text{HCO}_3^-$) để bóc tách rối loạn hỗn hợp.
- Nắm vững chỉ định khắt khe và công thức tính bù Natri Bicarbonat ($\text{NaHCO}_3$) an toàn: Chỉ bù khi $\text{pH} < 7,10$ hoặc $\text{HCO}_3^- < 8 - 10\text{ mEq/L}$ có rối loạn huyết động trơ; mục tiêu chỉ nâng lên $12 - 15\text{ mEq/L}$; nhận diện 5 biến chứng nguy hiểm (toan dịch não tủy nghịch thường, hạ Kali máu, hạ Canxi ion hóa, hiệu ứng Bohr, quá tải thể tích).

### 1.2 Guidelines & Chứng cứ Y học cốt lõi
1. **Indian J Crit Care Med (2022 - PMID: 36755633):** Acute Diarrhea and Severe Dehydration in Children: Does Non-anion-gap Component of Severe Metabolic Acidemia Need More Attention? (Chứng minh toan chuyển hóa trong tiêu chảy mất nước nặng là thể hỗn hợp tăng AG do toan lactic và toan bình thường AG do mất Bicarbonat qua phân).
2. **Pediatr Crit Care Med (2025 - PMID: 40249229):** Early Sodium Bicarbonate Use in Pediatric In-Hospital Cardiac Arrest: A Single-Center, Retrospective Cohort Study, 2013-2023. (Khuyến cáo không dùng sớm Natri Bicarbonat thường quy trong ngừng tim và hồi sức toan máu ở trẻ em vì không cải thiện tỷ lệ sống còn).
3. **Front Med (2026 - PMID: 42666620):** Physiologic response to sodium bicarbonate administration during pediatric in-hospital cardiac arrest. (Phân tích động học sinh khí CO2 gây toan dịch não tủy nghịch thường, hạ Canxi ion hóa và hạ Kali sau tiêm Natri Bicarbonat).
4. **BMC Pediatr (2025 - PMID: 41120922):** Clinical value of albumin-corrected anion gap combined with lactate dehydrogenase in predicting sepsis-associated liver injury in children. (Giá trị của khoảng trống Anion Gap hiệu chỉnh theo nồng độ Albumin máu ở bệnh nhi nặng).
5. **Pediatr Res (2026 - PMID: 40983691):** Pyloric index: a novel nomogram predictor of metabolic alkalosis in congenital hypertrophic pyloric stenosis. (Cơ chế sinh lý bệnh kiềm chuyển hóa giảm Clo và giảm Kali trong hẹp phì đại môn vị ở trẻ nhũ nhi).
6. **J Pers Med (2023 - PMID: 37511675):** Arterial Blood Gas Analysis for Survival Prediction in Pediatric Patients with Out-of-Hospital Cardiac Arrest. (Vai trò tiên lượng của pH, PaO2, PaCO2 và kiềm dư BE trong hồi sức cấp cứu nhi).

---

## 2. Bảng trích dẫn PMIDs kiểm tra tính xác thực

| PMID | Tác giả & Năm | Tên bài báo / Hướng dẫn | Tạp chí | Vai trò chứng cứ |
|---|---|---|---|---|
| **36755633** | Singhi S et al. (2022) | Acute Diarrhea and Severe Dehydration in Children: Does Non-anion-gap Component of Severe Metabolic Acidemia Need More Attention? | *Indian J Crit Care Med* | Chứng minh toan chuyển hóa hỗn hợp trong tiêu chảy mất nước nặng |
| **40249229** | Raymond TT et al. (2025) | Early Sodium Bicarbonate Use in Pediatric In-Hospital Cardiac Arrest: A Single-Center, Retrospective Cohort Study, 2013-2023 | *Pediatr Crit Care Med* | Bằng chứng chống chỉ định dùng sớm NaHCO3 thường quy trong hồi sức cấp cứu nhi |
| **42666620** | Morgan RW et al. (2026) | Physiologic response to sodium bicarbonate administration during pediatric in-hospital cardiac arrest | *Front Med* | Cơ chế toan dịch não tủy nghịch thường và hạ Canxi, Kali sau tiêm Bicarbonat |
| **41120922** | Wang L et al. (2025) | Clinical value of albumin-corrected anion gap combined with lactate dehydrogenase in predicting sepsis-associated liver injury in children | *BMC Pediatr* | Công thức Anion Gap hiệu chỉnh theo Albumin ở bệnh nhi hồi sức cấp cứu |
| **40983691** | Hernanz-Perez B et al. (2026) | Pyloric index: a novel nomogram predictor of metabolic alkalosis in congenital hypertrophic pyloric stenosis | *Pediatr Res* | Cơ chế nôn mất acid HCl gây kiềm chuyển hóa và hạ Clo, Kali trong hẹp môn vị |
| **37511675** | Lee J et al. (2023) | Arterial Blood Gas Analysis for Survival Prediction in Pediatric Patients with Out-of-Hospital Cardiac Arrest | *J Pers Med* | Giá trị tiên lượng của các chỉ số ABG và kiềm dư BE trong cấp cứu nhi |
