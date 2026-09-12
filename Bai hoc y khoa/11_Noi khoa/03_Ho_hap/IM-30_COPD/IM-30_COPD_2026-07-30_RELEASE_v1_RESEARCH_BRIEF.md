# RESEARCH BRIEF: IM-30 COPD (Bệnh phổi tắc nghẽn mạn tính)

**Release Basename:** `IM-30_COPD_2026-07-30_RELEASE_v1.md`  
**Profile:** `disease`  
**Required Gates:** `brief_pmid_preflight`, `brief_claims_strict`, `source_pmid_strict`, `source_claims_strict`, `source_retraction`, `guideline_evidence`, `depth_disease`, `guideline_evidence_crosscheck`, `citation_zero_block`, `cards_schema`, `candidate_apkg_build`, `package_note_count`, `package_diacritics`, `source_diacritics`, `docx_build`, `learner_smoke`  
**Date:** 2026-07-30  
**Target Level:** L3_BEGINNER (Học từ nền tảng, cầm tay chỉ việc, an toàn lâm sàng)

---

## 1. MỤC TIÊU & PHẠM VI NGUYÊN TẮC (SCOPE)
- **Tỷ lệ trọng tâm:** COPD ổn định 60% / Đợt cấp COPD 40%.
- **Đối tượng:** Sinh viên y khoa, bác sĩ mới, bác sĩ Nội khoa tuyến tỉnh Việt Nam.
- **Tiêu chuẩn chiều sâu (depth profile):** `disease` (tập trung chẩn đoán, phân tầng, điều trị ban đầu, theo dõi, nhận diện biến chứng & red flags, xử trí cấp cứu & chuyển tuyến).

---

## 2. KHÓA 7 CLAIM QUESTIONS (CANDIDATE CLAIM MAP)

### Claim 1 (C-001): Diagnostic Criterion (Tiêu chuẩn chẩn đoán xác định COPD)
- **Câu hỏi:** Tiêu chuẩn hô hấp ký chẩn đoán xác định COPD sau khi sử dụng thuốc giãn phế quản là gì?
- **Khóa tiêu chuẩn:**
  - Tiêu chuẩn chẩn đoán xác định giới hạn luồng khí dai dẳng (tắc nghẽn hô hấp) là tỷ số FEV1/FVC < 0.70 (hoặc FEV1/FEV6 < 0.70) đo sau test phục hồi phế quản.
- **Trạng thái evidence:** Consensus guideline chính thức từ GOLD Report (Global Initiative for Chronic Obstructive Lung Disease).

### Claim 2 (C-002): GOLD Assessment Grouping (Phân nhóm GOLD A, B, E)
- **Câu hỏi:** Phân nhóm GOLD A, B, E hiện hành dựa trên những tiêu chí nào để đưa ra quyết định chọn phác đồ khởi đầu?
- **Khóa tiêu chuẩn:**
  - Phân nhóm A, B, E dựa vào mức độ triệu chứng (thang điểm mMRC hoặc CAT) và tiền sử đợt cấp trong 12 tháng qua.
  - Nhóm A: Triệu chứng ít (mMRC 0-1 hoặc CAT < 10), 0 hoặc 1 đợt cấp trung bình (không nhập viện).
  - Nhóm B: Triệu chứng nhiều (mMRC ≥ 2 hoặc CAT ≥ 10), 0 hoặc 1 đợt cấp trung bình (không nhập viện).
  - Nhóm E: Có tiền sử đợt cấp nặng (≥ 1 đợt cấp phải nhập viện) HOẶC ≥ 2 đợt cấp trung bình trong 12 tháng qua, bất kể điểm triệu chứng.
- **Trạng thái evidence:** Consensus guideline chính thức từ GOLD Report.

### Claim 3 (C-003): ICS Indication & Eosinophil Cutoff (Chỉ định ICS và ngưỡng Bạch cầu ái toan)
- **Câu hỏi:** Chỉ định phối hợp ICS vào phác đồ giãn phế quản ở bệnh nhân COPD ổn định dựa trên những yếu tố nào và ngưỡng Eosinophil máu là bao nhiêu?
- **Khóa tiêu chuẩn:**
  - Phối hợp ICS (thường dưới dạng LABA+LAMA+ICS hoặc LABA+ICS) được khuyến cáo mạnh mẽ khi bệnh nhân có tiền sử đợt cấp (nhóm E) VÀ số lượng bạch cầu ái toan trong máu (blood eosinophil count) ≥ 300 tế bào/µL, hoặc có tiền sử hen phế quản đi kèm.
  - Ngưỡng eosinophil < 100 tế bào/µL là yếu tố tiên lượng ít đáp ứng với ICS và không nên khởi đầu ICS.
- **Trạng thái evidence:** Consensus guideline chính thức từ GOLD Report.

### Claim 4 (C-004): Acute Oxygen Target (Mục tiêu Oxy liệu pháp trong Đợt cấp)
- **Câu hỏi:** Mục tiêu độ bão hòa oxy (SpO2) khi thở oxy liệu pháp trong xử trí đợt cấp COPD là bao nhiêu và tại sao?
- **Khóa tiêu chuẩn:**
  - Mục tiêu SpO2 chuẩn trong đợt cấp COPD là 88% – 92% (hoặc 88% - 93%).
  - Tránh thở oxy liều cao mù quáng vì nguy cơ gây tăng CO2 máu (hypercapnia) do giảm phản ứng co mạch phổi do thiếu oxy (hypoxic pulmonary vasoconstriction suppression / Haldane effect) và giảm thông khí phế nang, dẫn đến toan hô hấp và lơ mơ/hôn mê.
- **Trạng thái evidence:** Consensus guideline từ GOLD Report / ATS / ERS.

### Claim 5 (C-005): Systemic Steroid in Exacerbation (Liều và thời gian dùng Corticoid toàn thân trong đợt cấp)
- **Câu hỏi:** Liều lượng và thời gian khuyến cáo cho Corticoid toàn thân trong xử trí đợt cấp COPD là bao nhiêu?
- **Khóa tiêu chuẩn:**
  - Corticoid toàn thân đường uống (Prednisolone 40 mg/ngày) được khuyến cáo dùng trong thời gian 5 ngày.
  - Không kéo dài quá 5-7 ngày để tránh tác dụng phụ và nguy cơ nhiễm trùng.
- **Trạng thái evidence:** Consensus guideline từ GOLD Report.

### Claim 6 (C-006): Antibiotic Criteria in Exacerbation (Tiêu chuẩn chỉ định Kháng sinh trong đợt cấp)
- **Câu hỏi:** Tiêu chuẩn chỉ định kháng sinh trong đợt cấp COPD theo Anthonisen và GOLD là gì?
- **Khóa tiêu chuẩn:**
  - Kháng sinh được chỉ định khi bệnh nhân có đủ 3 triệu chứng chính (tăng khó thở, tăng thể tích đờm, đờm mủ), HOẶC có 2 triệu chứng chính trong đó bắt buộc có tăng đờm mủ, HOẶC bệnh nhân đợt cấp nặng cần thông khí cơ học (xâm nhập hoặc không xâm nhập).
- **Trạng thái evidence:** Tiêu chuẩn Anthonisen / GOLD Report consensus.

### Claim 7 (C-007): LTOT & NIV Indications (Chỉ định Oxy dài hạn và NIV tại nhà)
- **Câu hỏi:** Chỉ định cho liệu pháp oxy dài hạn tại nhà (LTOT) và thông khí không xâm nhập (NIV) mạn tính ở bệnh nhân COPD là gì?
- **Khóa tiêu chuẩn:**
  - LTOT chỉ định khi PaO2 ≤ 55 mmHg (hoặc SpO2 ≤ 88%) ở trạng thái nghỉ ngơi, HOẶC PaO2 56–59 mmHg kèm theo bằng chứng tâm phế mạn, phù do suy tim phải, hoặc đa hồng cầu (hematocrit > 55%).
  - NIV tại nhà mạn tính chỉ định ở bệnh nhân COPD có tăng CO2 máu mạn tính dai dẳng (PaCO2 > 52 mmHg) sau nhập viện vì đợt cấp suy hô hấp.
- **Trạng thái evidence:** Consensus guideline từ GOLD Report.

---

## 3. CHỈ ĐỊNH PHÁT HÀNH & BỒI THƯỜNG DỮ LIỆU
Mọi số liệu consensus từ Guideline GOLD (Global Initiative for Chronic Obstructive Lung Disease) và ATS/ERS là kiến thức chuẩn mực quốc tế, được trình bày đầy đủ, chính xác trong bài học với định danh tài liệu rõ ràng.
