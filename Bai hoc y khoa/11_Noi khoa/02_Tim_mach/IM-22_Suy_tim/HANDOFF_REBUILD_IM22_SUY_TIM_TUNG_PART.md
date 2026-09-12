# HANDOFF: REBUILD IM-22 SUY TIM (PART 1 ĐẾN 6)

**Ngày Handoff:** 2026-07-29
**Mục tiêu:** Xây dựng lại toàn bộ series IM-22 Suy tim thành 6 phần riêng biệt, đạt chuẩn PUBLISH READY theo quy tắc canonical nghiêm ngặt.
**Bối cảnh:** Bản legacy `IM-22_Suy_tim_2026-07-17.md` (546 dòng) đã rớt các cổng phát hành (publication gates). File này có 91 notes/cards, diacritics MD 95.9%, APKG 96.3%, 0 citation block nhưng có 7 strict PMID WARNs (do lỗi 429) và 5 claim BLOCKs (số liệu trial không khớp). Bản legacy thiếu một locked research brief mới, thiếu evidence bundle, và thiếu hashed canonical gate manifest. Nó sử dụng các nhãn cũ bị cấm (`[DIRECTION ONLY]`, `[TEXTBOOK]`), có chứa Mermaid diagrams và bảng >=4 cột. Đây KHÔNG được coi là một bản release học sâu.

---

## 1. EXACT FILES PHẢI ĐỌC TRƯỚC (PREREQUISITES)

Trước khi bắt đầu bất kỳ hành động nào, bạn BẮT BUỘC phải đọc các file sau:
1. `F:/DL/mavisresearch/AGENTS.md` (Root project rules)
2. `F:/DL/mavisresearch/Bai hoc y khoa/AGENTS.md` (Canonical medical rules)
3. `F:/DL/mavisresearch/Bai hoc y khoa/WORKFLOW.md` (Quy trình build)
4. `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/IM-22_Suy_tim_2026-07-17.md` (Legacy MD)
5. `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/_remediation_gate_report.md` (Báo cáo lỗi)
6. `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/_remediation_evidence.md` (Bằng chứng lỗi)
7. `F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/build_pipeline.py` (Canonical build script)
8. `F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/evidence_sync.py` (Canonical evidence sync)
9. `F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/publish_gate.py` (Canonical publish gate)
10. `F:/DL/mavisresearch/Bai hoc y khoa/template_lesson.md` (Template chuẩn)

---

## 2. AUDIT & STRICT RULES (TUYỆT ĐỐI KHÔNG COPY MÙ LEGACY)

Bạn PHẢI xác minh lại các claim sau từ đầu bằng toolchain evidence canonical. **KHÔNG kế thừa các claim legacy chưa qua cổng kiểm định (unverified).**

*   **Universal Definition 2026:** Xác minh exact identity và authority. Có phải bản current không?
*   **Phân loại EF/HFimpEF:** Xác minh exact thresholds và định nghĩa.
*   **NT-proBNP:** Xác minh ngưỡng cấp/mạn, điều chỉnh theo tuổi, CKD, AF, và câu claim "luôn là xét nghiệm đầu tiên".
*   **SGLT2i Class:** Xác minh khuyến cáo cho HFmrEF và HFpEF.
*   **Khởi trị GDMT:** Xác minh khuyến cáo khởi trị ĐỒNG THỜI 4 trụ cột.
*   **Liều/Chuẩn độ/Theo dõi:** Xác minh liều cụ thể, ngưỡng eGFR, và ngưỡng Kali (K).
*   **Mục tiêu Oxy:** Xác minh exact SpO2 targets.
*   **Lợi tiểu cấp:** Xác minh thuật toán IV loop diuretic + urine sodium response.
*   **Giãn mạch/Inotrope/Vận mạch:** Xác minh exact dosing và official protocols.
*   **Tiêu chuẩn ICD/CRT:** Xác minh exact indications (phân biệt rõ CRT với capillary refill time).
*   **Bối cảnh Việt Nam:** Xác minh các claim về giá cả và khả năng tiếp cận (nếu có).
*   **Dữ liệu Trial:** Xác minh TẤT CẢ các con số HR, CI, và *n* cho PARADIGM-HF, DAPA-HF, EMPEROR-Reduced, DELIVER, EMPEROR-Preserved.

**QUY TẮC NHÃN KÉP (CANONICAL LABELS ONLY):**
*   Tuyệt đối CẤM các nhãn legacy: `[FULL VERIFIED]`, `[DIRECTION ONLY]`, `[TEXTBOOK]`, `[ABSTRACT MATCH]`.
*   Chỉ sử dụng 5 nhãn canonical SAU KHI artifact tương ứng được tạo ra: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.
*   CẤM sử dụng NCBI/E-utilities trong release workflow (bất chấp các text skill cũ).

---

## 3. PHÂN CHIA 6 PART CHI TIẾT

Series PHẢI được chia thành 6 part. Mỗi part phải có đầy đủ các mục sau:

### Part 1: Nền tảng (Foundations)
*   **Mục tiêu:** Hiểu rõ định nghĩa, cơ chế sinh lý bệnh, và các kiểu hình huyết động cơ bản.
*   **Prerequisite:** Sinh lý tim mạch cơ bản (CO, preload, afterload).
*   **Boundaries (In/Out):** Bao gồm định nghĩa 2026, phân loại EF, cơ chế bù trừ. KHÔNG đi sâu vào thuốc cụ thể ở phần này.
*   **Nội dung:** Sinh lý bệnh, Định nghĩa, Staging/Trajectory, Nguyên nhân, Phenotype huyết động (warm/cold, wet/dry).
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. Warm-wet (ấm-ướt).
    2. Cold-wet shock recognition (nhận diện sốc lạnh-ướt).
    3. Cold-dry vs hypovolemia (lạnh-khô phân biệt giảm thể tích).
    4. Right HF/systemic congestion (suy tim phải/sung huyết hệ thống).
*   **Coverage Map:** ~80-140 cards bao phủ các khái niệm cốt lõi, định nghĩa, và phân loại.

### Part 2: Chẩn đoán (Diagnosis)
*   **Mục tiêu:** Chẩn đoán xác định và phân biệt suy tim cấp/mạn, sử dụng biomarker và siêu âm.
*   **Prerequisite:** Part 1, cách đọc ECG/XQ cơ bản.
*   **Boundaries (In/Out):** Tập trung vào lâm sàng, NT-proBNP, Echo. Thuật toán H2FPEF/HFA-PEFF CHỈ đưa vào nếu nguồn là current.
*   **Nội dung:** Triệu chứng và khám; ECG; X-quang ngực; xét nghiệm và peptide lợi niệu; siêu âm tim; quy trình chẩn đoán HFpEF; chẩn đoán phân biệt; tìm nguyên nhân.
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. HF vs COPD/pneumonia/PE (phân biệt suy tim với bệnh phổi).
    2. HFrEF first diagnosis (chẩn đoán HFrEF lần đầu).
    3. HFpEF with AF/obesity (HFpEF kèm rung nhĩ/béo phì).
    4. CKD with elevated NP (bệnh thận mạn có tăng natriuretic peptide).
    5. Etiologic ischemic/valve clue (manh mối nguyên nhân thiếu máu cục bộ/van tim).
*   **Coverage Map:** ~80-140 cards về triệu chứng, ngưỡng biomarker, chỉ số siêu âm.

### Part 3: HFrEF mạn (Chronic HFrEF)
*   **Mục tiêu:** Nắm vững và kê đơn được "tứ trụ" GDMT cho HFrEF.
*   **Prerequisite:** Part 1, Part 2.
*   **Boundaries (In/Out):** Chỉ HFrEF mạn và tối ưu GDMT; không đi sâu HFpEF hoặc xử trí suy tim cấp.
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. New HFrEF initiation (khởi trị HFrEF mới).
    2. Low BP titration (chuẩn độ khi huyết áp thấp).
    3. HyperK/eGFR worsening (xử trí tăng Kali/giảm eGFR).
    4. Decompensation medication hold/restart (tạm ngưng/bắt đầu lại thuốc khi mất bù).
    5. Adherence/NSAID (tuân thủ điều trị/sử dụng NSAID).
*   **Nội dung:** 4 pillars, Initiation/Titration/Doses/Monitoring, Hypotension/Hyperkalemia/eGFR management, Adjuncts, Adherence.
*   **Coverage Map:** ~80-140 cards về liều lượng, chống chỉ định, xử trí tác dụng phụ.

### Part 4: HFmrEF/HFpEF/HFimpEF + Comorbidities
*   **Mục tiêu:** Quản lý các thể suy tim EF bảo tồn/giảm nhẹ và bệnh đồng mắc.
*   **Prerequisite:** Part 1, Part 2, Part 3.
*   **Boundaries (In/Out):** Tập trung vào SGLT2i, lợi tiểu, và kiểm soát bệnh nền.
*   **Nội dung:** Specific management for HFmrEF, HFpEF, HFimpEF; Comorbidities (Obesity, DM, CKD, AF, HTN, Iron deficiency, Sleep apnea, Amyloid).
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. HFpEF obesity/DM (HFpEF kèm béo phì/đái tháo đường).
    2. HFpEF AF/HTN (HFpEF kèm rung nhĩ/tăng huyết áp).
    3. CKD (suy tim kèm bệnh thận mạn).
    4. HFimpEF continuation (tiếp tục điều trị HFimpEF).
    5. Suspected amyloid/iron deficiency/sleep apnea (nghi ngờ amyloidosis/thiếu sắt/ngưng thở khi ngủ).
*   **Coverage Map:** ~80-140 cards về chỉ định SGLT2i, mục tiêu huyết áp, bù sắt.

### Part 5: Suy tim cấp (Acute HF)
*   **Mục tiêu:** Cấp cứu ban đầu, giảm sung huyết (decongestion), và xử trí sốc (shock).
*   **Prerequisite:** Part 1, Part 2, kiến thức hồi sức cơ bản.
*   **Boundaries (In/Out):** Xử trí tại cấp cứu/ICU. Chỉ dùng official protocols cho inotrope/vasopressor.
*   **Nội dung:** ABCDE, profiles, oxygen/NIV, decongestion response, vasodilators, shock/inotrope/vasopressor official protocols, triggers, discharge transition.
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. SCAPE/warm-wet (phù phổi cấp/ấm-ướt).
    2. Inadequate diuretic response (đáp ứng lợi tiểu kém).
    3. Cold-wet shock (sốc lạnh-ướt).
    4. ACS/arrhythmia trigger (yếu tố thúc đẩy hội chứng vành cấp/rối loạn nhịp).
    5. Discharge transition (chuyển tiếp xuất viện).
*   **Coverage Map:** ~80-140 cards về protocol lợi tiểu, liều vận mạch, tiêu chí ra viện.

### Part 6: Suy tim tiến triển & Dài hạn (Advanced/Long-term)
*   **Mục tiêu:** Nhận diện bệnh nhân cần can thiệp thiết bị, ghép tim hoặc chăm sóc giảm nhẹ, và quản lý dài hạn.
*   **Prerequisite:** Part 3, Part 4, Part 5.
*   **Boundaries (In/Out):** Chỉ định thiết bị, ghép tim, phục hồi chức năng, theo dõi ngoại trú.
*   **Nội dung:** Advanced referral, ICD/CRT, valve, LVAD/transplant/palliative, rehab/vaccination/self-monitoring/follow-up.
*   **Cases (Bắt buộc 5 bước giải: red flag, dữ kiện quyết định, hành động, monitoring/transfer, why alternatives wrong):**
    1. ICD candidate (chỉ định ICD).
    2. CRT candidate with terminology distinction (chỉ định CRT, phân biệt rõ thuật ngữ CRT với capillary refill time).
    3. Valve referral (chuyển tuyến can thiệp van).
    4. Advanced HF LVAD/transplant (suy tim tiến triển cần LVAD/ghép tim).
    5. Palliative/rehab/self-monitoring (chăm sóc giảm nhẹ/phục hồi chức năng/tự theo dõi).
*   **Coverage Map:** ~80-140 cards về tiêu chuẩn ICD/CRT, lịch tiêm chủng, theo dõi.

---

## 4. WORKFLOW BẮT BUỘC TUẦN TỰ & NAMING CONVENTION

Bạn PHẢI thực hiện workflow này tuần tự. **KHÔNG bắt đầu Part tiếp theo nếu Part hiện tại chưa PUBLISH READY.**

**Quy ước Naming (Naming Convention):**
*   Folder con: `P1_Nen_tang`, `P2_Chan_doan`, v.v.
*   Basename: `IM-22_P1_Nen_tang_YYYY-MM-DD_RELEASE_v1`
*   Output: Phải nằm đúng trong thư mục `outputs/` của từng Part.
*   File/Folder: KHÔNG DẤU tiếng Việt. Nội dung file: CÓ DẤU đầy đủ.

**Các bước cho MỖI PART:**

1.  **Chạy `publish_gate.py --list-profiles`:** Xác định đúng profile (chỉ dùng các profile có sẵn: `disease`, `foundation`, `pharmacology`) cho Part đó. (Lưu ý: `L3_BEGINNER` là `lesson_depth_contract` quy định độ sâu, KHÔNG PHẢI là profile).
2.  **Tạo Fresh Locked Research Brief:** Khóa profile đã chọn, `lesson_depth_contract` (`L3_BEGINNER`), Claim IDs, output basename, và required gates. Xác định official current sources.
3.  **Evidence Sync (Online):** Chạy `evidence_sync.py` (provider-neutral). Cấm network egress trong build.
4.  **Preflight Check (Offline):** Chạy `preflight_claim_check.py`. **MỌI preflight evidence gates của locked brief PHẢI PASS TRƯỚC KHI bắt đầu viết content.**
5.  **Viết Content (MD & Cards):** Viết Markdown và Cards V2 JSON. Không tự gán nhãn verify.
6.  **Build Pipeline (Offline):** Chạy `build_pipeline.py`. Yêu cầu: 0 BLOCK, 0 WARN. Full build/release gates phải PASS sau khi viết.
7.  **Verify Deliverables:** Đảm bảo đủ MD, DOCX, APKG, hashed gate-results, evidence artifacts trong `outputs/`.
8.  **Publish Ready:** Chỉ chuyển sang Part tiếp theo khi Part hiện tại đạt PUBLISH READY.

---

## 5. NGUỒN TỐI THIỂU (MINIMUM REQUIRED SOURCES)

Phải được verify qua các nguồn chính thức và current:
*   ESC 2021 + Focused Update 2023.
*   ACC/AHA/HFSA 2022.
*   Current ACC consensus on HFrEF/HFpEF.
*   Universal Definition 2026 (chỉ khi exact authority là current).
*   Official acute/advanced/device sources.
*   **Official current document registry metadata:** Phải kiểm tra authority, document type, version, supersession, và translation endorsement. Bất kỳ bản cập nhật ESC/ACC nào mới hơn (current updates beyond named legacy documents) đều phải được dùng nếu bản cũ đã bị superseded.

---

## 6. DELIVERABLES & FORMATTING

Mỗi Part phải có:
*   Release Markdown (`.md`) duy nhất.
*   DOCX outputs (trong `outputs/`).
*   Cards V2 JSON (đủ thay thế MD/DOCX, cover depth map, ~80-140 cards, không quota-padding).
*   APKG (trong `outputs/`).
*   Knowledge check (5 sections + answer key + score scaffold).
*   Evidence artifacts & hashed gate-results.
*   3-5 Cases có giải chi tiết viết trực tiếp trong file MD.
*   Red flags, Plan A/B, common traps, clinical reasoning, why alternatives wrong.

**Formatting Rules:**
*   CHỈ DÙNG ASCII/nested lists. **CẤM Mermaid.**
*   **CẤM bảng >= 4 cột.**
*   Tiếng Việt trước, tiếng Anh trong ngoặc đơn (vd: "kép đồng thời (dual trigger)").

---

## 7. ACCEPTANCE CRITERIA (TIÊU CHÍ NGHIỆM THU)

**Cho MỖI PART:**
*   Source claim set trong lesson khớp hoàn toàn với locked brief.
*   `build_pipeline.py` trả về **0 BLOCK / 0 WARN**.
*   Tất cả required gates row đều **PASS**.
*   `publish_gate.py` trả về exit code **0**.
*   Exact artifact hashes là current.
*   DOCX/MD/cards/APKG smoke paths hợp lệ.
*   Knowledge check không rỗng, đủ 5 sections, có answer key, score scaffold, và total_questions > 0.
*   APKG SQLite verify: `source card count = SQLite notes = SQLite cards` (0 missing/unexpected/blank/duplicate). Diacritics exit 0.

**Cho TOÀN SERIES (Clean Cutover Rule):**
*   Bản legacy PHẢI ĐƯỢC GIỮ NGUYÊN trong suốt quá trình làm việc.
*   CHỈ KHI toàn bộ 6 Part đều đạt PUBLISH READY, mới tiến hành update catalog và cutover. Tuyệt đối không dùng aliases hay shims.

---

## 8. HÀNH ĐỘNG ĐẦU TIÊN (EXPLICIT FIRST ACTION)

1.  Chạy `publish_gate.py --list-profiles` để xem danh sách profile.
2.  Đọc các file prerequisite được liệt kê ở Mục 1.
3.  Tạo **Part 1 Locked Research Brief** với profile phù hợp (chọn 1 trong 3: `disease`, `foundation`, `pharmacology`).
4.  **TUYỆT ĐỐI KHÔNG bắt đầu viết nội dung Part 1 trước khi preflight gates PASS.**

---

## CHECKLIST TỰ KIỂM TRA (SELF-AUDIT)
- [ ] 1. Viết chủ yếu bằng tiếng Việt.
- [ ] 2. Phân biệt rõ `profile` (từ `publish_gate.py`) và `lesson_depth_contract` (`L3_BEGINNER`).
- [ ] 3. Có mục "Exact files phải đọc trước" đầy đủ.
- [ ] 4. Mỗi Part có đủ mục tiêu, prerequisite, boundaries, nội dung, cases, coverage map.
- [ ] 5. Có naming convention cụ thể (không dấu, basename chuẩn).
- [ ] 6. Có acceptance criteria cho MỖI part và TOÀN series.
- [ ] 7. Sửa workflow: first action chạy list-profiles, preflight gates PASS trước khi viết.
- [ ] 8. Có quy tắc clean cutover (giữ legacy, update khi cả 6 part xong).
- [ ] 9. Explicitly ban legacy labels, canonical five only, ban NCBI/E-utilities.
- [ ] 10. Có checklist chi tiết này.