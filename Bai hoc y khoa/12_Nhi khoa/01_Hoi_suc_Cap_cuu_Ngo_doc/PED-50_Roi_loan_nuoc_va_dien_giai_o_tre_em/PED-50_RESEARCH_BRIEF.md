# RESEARCH BRIEF: TIẾP CẬN & XỬ TRÍ RỐI LOẠN NƯỚC VÀ ĐIỆN GIẢI Ở TRẺ EM (PED-50)

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
- Làm chủ sinh lý phân bố nước và các ngăn dịch (nội bào, ngoại bào) theo lứa tuổi: Công thức khối lượng nước toàn phần $V = 0,6P + 0,25$, tỷ lệ ECF giảm dần từ $60\%$ ở trẻ 1 tháng xuống $36\%$ ở trẻ 15 tuổi.
- Nắm vững 3 phương pháp tính nhu cầu nước duy trì hàng ngày (Holliday - Segar $100 - 50 - 20$, diện tích da $1500\text{ ml/m}^2$, năng lượng $100 - 150\text{ ml}/100\text{ kcal}$) và các con đường xuất nhập nước (mất vô hình, nước tiểu, nước chuyển hóa nội sinh).
- Nắm vững bảng phân bố điện giải nội bào vs ngoại bào và nhu cầu điện giải duy trì hàng ngày ($\text{Na}^+ 2 - 3\text{ mEq/kg}$, $\text{K}^+ 1 - 2\text{ mEq/kg}$, $\text{Mg}^{++} 0,4 - 0,8\text{ mEq/kg}$, $\text{Ca}^{++} 50 - 200\text{ mg/kg}$).
- Đánh giá phân độ mất nước theo sụt cân (Độ I, II, III) và bảng 4 mức độ lâm sàng (tri giác, khát, niêm mạc, mắt trũng, nước mắt, nếp véo da Casper).
- Chẩn đoán phân biệt 3 thể mất nước: Mất nước đẳng trương ($\text{Na}^+ 130 - 150$), Mất nước ưu trương ($\text{Na}^+ > 150$), Mất nước nhược trương ($\text{Na}^+ < 130$).
- Phác đồ xử trí cấp cứu các rối loạn điện giải đe dọa tính mạng:
  + Cấp cứu Hạ Natri máu nặng có triệu chứng co giật: Bolus tĩnh mạch $\text{NaCl } 3\% \text{ } 4\text{ ml/kg}$ trong $20 - 30\text{ phút}$.
  + Xử trí Tăng Natri máu: Bù nước tự do, kiểm soát tốc độ hạ $\text{Na}^+ \le 0,5\text{ mEq/L/giờ}$ ($\le 10 - 12\text{ mEq/L/24h}$) trong $36 - 48\text{ giờ}$ để ngăn ngừa phù não cấp và tử vong.
  + Cấp cứu Tăng Kali máu nặng: Bảo vệ màng cơ tim bằng Calcium gluconate $10\%$, dịch chuyển Kali vào nội bào (Glucose + Insulin, khí dung Salbutamol), đào thải Kali.
  + Xử trí Hạ Kali máu: Bẫy lâm sàng chỉ bù Kali khi trẻ đã có nước tiểu; nồng độ pha truyền ngoại vi $\le 40\text{ mEq/L}$, tốc độ tối đa $0,5\text{ mEq/kg/h}$.
  + Xử trí Hạ Canxi máu cấp có co giật / cơn tetany: Calcium gluconate $10\% \text{ } 0,5 - 1\text{ ml/kg}$ tiêm tĩnh mạch chậm trong 10 phút dưới theo dõi tim mạch.
- Giải thành thạo và kê đơn chuẩn xác 3 bài toán tính bù dịch lâm sàng kinh điển (Đẳng trương, Nhược trương, Ưu trương) từ giáo trình ĐHYD Thái Bình.

### 1.2 Guidelines & Chứng cứ y học cốt lõi
1. **AAP 2018 Guideline:** Clinical Practice Guideline: Maintenance Intravenous Fluids in Children (Pediatrics, PMID: 30478247).
2. **CJASN 2023 Review & Guidance:** Correcting Hypernatremia in Children (Clin J Am Soc Nephrol, PMID: 36888887).
3. **BMC Pediatrics 2026 Multicenter PICU Cohort:** Hyponatremia upon PICU admission: a 10-year retrospective analysis of outcomes and independent prognostic value (BMC Pediatr, PMID: 42015038).
4. **Pediatric Nephrology 2024 Clinical Review:** Management of hyperkalemia in children (Pediatr Nephrol, PMID: 38001558).
5. **Frontiers in Endocrinology 2026 Multicenter Cohort:** Severe pediatric hypocalcemia in Vietnam: etiologic profile, clinical outcomes and risk factors in 246 cases (Front Endocrinol, PMID: 41704483).
6. **Arch Dis Child 2026 Systematic Review:** Intravenous rehydration in children with severe malnutrition and severe dehydration: a systematic review and meta-analysis (Arch Dis Child, PMID: 42161576).

---

## 2. Bảng trích dẫn PMIDs kiểm tra tính xác thực

| PMID | Tác giả & Năm | Tên bài báo / Hướng dẫn | Tạp chí | Vai trò chứng cứ |
|---|---|---|---|---|
| **30478247** | Feld LG et al. (2018) | Clinical Practice Guideline: Maintenance Intravenous Fluids in Children | *Pediatrics* | Guideline AAP khuyến cáo dung dịch đẳng trương duy trì tránh hạ Natri mắc phải viện |
| **36888887** | Somers MJ et al. (2023) | Correcting Hypernatremia in Children | *Clin J Am Soc Nephrol* | Bằng chứng kiểm soát tốc độ hạ Natri $\le 0,5\text{ mEq/L/h}$ chống phù não cấp |
| **42015038** | Chen Y et al. (2026) | Hyponatremia upon PICU admission: a 10-year retrospective analysis of outcomes and independent prognostic value | *BMC Pediatr* | Tiên lượng và phân tầng nguy cơ hạ Natri máu tại khoa hồi sức cấp cứu nhi |
| **38001558** | Alfonzo A et al. (2024) | Management of hyperkalemia in children | *Pediatr Nephrol* | Khuyến cáo bậc thang xử trí cấp cứu tăng Kali máu: Ổn định màng $\rightarrow$ Dịch chuyển $\rightarrow$ Đào thải |
| **41704483** | Nguyen TH et al. (2026) | Severe pediatric hypocalcemia in Vietnam: etiologic profile, clinical outcomes and risk factors in 246 cases | *Front Endocrinol* | Dịch tễ học, căn nguyên còi xương / suy cận giáp và phác đồ cấp cứu hạ Canxi máu tại Việt Nam |
| **42161576** | Walson JL et al. (2026) | Intravenous rehydration in children with severe malnutrition and severe dehydration: a systematic review and meta-analysis | *Arch Dis Child* | Nguyên tắc bù dịch thận trọng trên trẻ suy dinh dưỡng nặng mất nước |
