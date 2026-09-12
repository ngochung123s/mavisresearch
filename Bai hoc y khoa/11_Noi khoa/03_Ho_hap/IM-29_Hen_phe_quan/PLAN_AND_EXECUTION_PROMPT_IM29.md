# PLAN AND EXECUTION PROMPT: IM-29 Hen phế quản

## 1. Goal, Audience & Prerequisites
- **Goal:** Tạo bài học y khoa "IM-29 Hen phế quản" đạt chuẩn L3_BEGINNER (10–14k từ) cho chương trình Nội khoa người lớn (tuyến tỉnh Việt Nam).
- **Audience:** Sinh viên y khoa, bác sĩ mới, bác sĩ Nội tuyến tỉnh (cần hướng dẫn từ gốc, cầm tay chỉ việc, an toàn lâm sàng).
- **Prerequisites:** 
  - IM-01 đến IM-06 (Nền tảng tư duy và an toàn lâm sàng, kê đơn, đọc xét nghiệm/X-quang/ECG cơ bản).
  - IM-07 (Tiếp cận khó thở cấp và suy hô hấp).
  - IM-28 (Khám hô hấp và đọc X-quang ngực).
  - IM-34 (Ho ra máu, suy hô hấp giảm oxy và chỉ định NIV/intubation/chuyển ICU).
  - IM-47 (Rối loạn toan–kiềm và đọc khí máu động mạch).
- **Target Path:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/`
- **Basename:** `IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1.md` (thay YYYY-MM-DD bằng ngày thực tế).
- **Profile:** `disease` (xác định qua `publish_gate.py --list-profiles`; pending emitted gates).
- **Scope In:** Hen ổn định (60%) / Đợt cấp (40%); Hô hấp ký thực hành cơ bản; Thuốc hít (đủ để chọn controller/reliever, chọn dụng cụ và kỹ thuật hít); Bối cảnh Việt Nam (tính khả thi, an toàn).
- **Scope Out & Overlap:** Không đi sâu vào COPD (IM-30) hay Tâm phế mạn (IM-34a). Tập trung vào tính biến thiên (variability) và viêm đường thở do hen.
- **Safety Traps:** 
  - Chẩn đoán phân biệt với COPD: Không được tuyên bố rằng tính khả hồi với thuốc giãn phế quản (bronchodilator reversibility) phân biệt sạch sẽ hai bệnh này (COPD vẫn có thể khả hồi một phần, hen lâu năm có thể tắc nghẽn cố định).
  - Hô hấp ký bình thường không kết thúc quá trình chẩn đoán (workup) nếu nghi ngờ lâm sàng cao.
  - Plan B (thiếu nguồn lực): Thiếu máy phun khí dung (nebulizer) không tự động là một bất lợi — pMDI + buồng đệm (spacer) có thể hiệu quả tương đương hoặc hơn; không đề xuất phác đồ cấp cứu không có cơ sở.

## 2. Learning Outcomes
Sau khi học bài này, người học có thể:
1. Giải thích được cơ chế viêm đường thở và tính biến thiên của hen phế quản bằng ngôn ngữ đơn giản.
2. Khai thác bệnh sử, nhận diện các yếu tố khởi phát (triggers) và đánh giá triệu chứng biến thiên.
3. Đọc và phiên giải hô hấp ký cơ bản (tính khả hồi với thuốc giãn phế quản) và biết cách xử trí khi hô hấp ký bình thường.
4. Đánh giá mức độ kiểm soát hen và nguy cơ tương lai theo guideline hiện hành.
5. Lựa chọn chiến lược điều trị thuốc hít (ICS-containing strategy), phân biệt controller/reliever, và hướng dẫn kỹ thuật dùng dụng cụ hít.
6. Nhận diện, phân độ nặng và xử trí ban đầu đợt cấp hen phế quản, biết khi nào cần chuyển tuyến/ICU.
7. Lập kế hoạch hành động (action plan) và theo dõi dài hạn cho bệnh nhân hen trong bối cảnh Việt Nam.

## 3. Outline & Word Budget (14–18 sections, ~10,000 - 14,000 từ)
1. **Tổng quan & Mục tiêu** (500 từ)
2. **Nền tảng cần dùng** (300 từ)
3. **Sinh lý bệnh: Viêm đường thở & Tính biến thiên** (800 từ) - *Giải thích cơ chế dễ hiểu.*
4. **Yếu tố khởi phát (Triggers) & Yếu tố nguy cơ** (600 từ)
5. **Chẩn đoán lâm sàng: Bệnh sử & Khám thực thể** (700 từ) - *Tập trung vào triệu chứng biến thiên.*
6. **Cận lâm sàng: Hô hấp ký & Tính khả hồi** (900 từ) - *Chất lượng đo và đáp ứng giãn phế quản.*
7. **Làm gì khi hô hấp ký bình thường?** (500 từ) - *PEF diary, tổng quan test kích thích phế quản.*
8. **Chẩn đoán phân biệt & Các bệnh bắt chước (Mimics)** (600 từ) - *Tránh trùng COPD/Tâm phế mạn.*
9. **Đánh giá mức độ kiểm soát & Nguy cơ tương lai** (700 từ)
10. **Nguyên tắc điều trị thuốc hít (Inhaled Therapy)** (800 từ)
11. **Chiến lược chứa ICS (ICS-containing strategy)** (900 từ)
12. **Dụng cụ hít (Devices), Kỹ thuật & Tuân thủ** (800 từ)
13. **Nguyên tắc tăng/giảm bậc điều trị (Step up/down)** (700 từ)
14. **Đợt cấp hen phế quản: Phân độ nặng & Nhận diện** (800 từ)
15. **Xử trí đợt cấp: Thuốc giãn phế quản, Corticosteroid toàn thân, Oxy** (1000 từ) - *Chỉ định chuyển tuyến/ICU.*
16. **Bệnh đồng mắc (Comorbidities) thường gặp** (500 từ)
17. **Kế hoạch hành động (Action Plan), Dự phòng & Tái khám** (700 từ)
18. **Bối cảnh Việt Nam & Ca lâm sàng** (1200 từ)

## 4. Key Elements
- **Lưu đồ (ASCII Algorithm):** Cần 2 lưu đồ ASCII thuần túy (không Mermaid): 1) Tiếp cận chẩn đoán hen (từ triệu chứng đến hô hấp ký/PEF); 2) Tiếp cận và xử trí đợt cấp.
- **BOX ĐỎ:** Nhận diện cơn hen nguy kịch (Red flags) cần hồi sức ngay.
- **Plan B:** Xử trí đợt cấp khi thiếu nguồn lực (thiếu khí dung, dùng pMDI + spacer).
- **5 Ca lâm sàng (Mỗi ca giải quyết qua 5 bước: 1. Red flag, 2. Dữ kiện quyết định, 3. Hành động, 4. Monitoring/chuyển tuyến, 5. Why alternatives wrong):**
  1. **Ca 1:** Triệu chứng biến thiên mới xuất hiện.
  2. **Ca 2:** Hô hấp ký ban đầu bình thường.
  3. **Ca 3:** Kiểm soát kém do kỹ thuật hít/tuân thủ kém.
  4. **Ca 4:** Đợt cấp hen phế quản.
  5. **Ca 5:** Nghi ngờ hen nặng/mimic cần chuyển tuyến.

## 5. Candidate Claim Map (6 Targeted Verified Claims)
*Lưu ý: Không tự chế nhãn/PMID. Không dùng NCBI/E-utilities. Các claim định lượng/khuyến cáo phải được lấy từ offline evidence bundle (tạo qua `evidence_sync.py` với nguồn official). Nếu không verify được, bỏ qua liều/ngưỡng chính xác hoặc đặt câu hỏi `CẦN TỰ KIỂM CHỨNG` riêng biệt. Các nhãn canonical duy nhất hợp lệ theo AGENTS là: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`. Nhãn `[FETCHED]` không được dùng để support các claim định lượng hoặc khuyến cáo.*
*Nguồn chính: GINA Strategy Report/Summary Guide hiện hành (kiểm tra version/supersession); ERS/ATS hiện hành cho chẩn đoán/hen nặng; Hướng dẫn Bộ Y tế VN (nếu current).*

1. **Tiêu chuẩn chẩn đoán biến thiên (Diagnostic variability criteria):** Tiêu chuẩn chính xác về FEV1 khả hồi hoặc biến thiên PEF là gì theo GINA/ERS/ATS hiện hành?
2. **Khuyến cáo về SABA đơn độc và ICS-containing (No SABA-only recommendation):** Khuyến cáo hiện hành về việc sử dụng SABA đơn độc là gì? Chiến lược ICS-containing được áp dụng cho quần thể/độ tuổi nào và lý do sinh lý bệnh/lâm sàng đằng sau khuyến cáo này theo GINA hiện hành?
3. **Chiến lược Reliever/Controller ưu tiên (Preferred strategy & age scope):** Thuật ngữ chính xác của Track 1 (MART) là gì? Đối tượng nào (độ tuổi, quần thể) đủ điều kiện áp dụng và liều lượng cụ thể ra sao theo GINA hiện hành?
4. **Công cụ đánh giá kiểm soát/nguy cơ (Control/risk assessment):** Các tiêu chí cụ thể để đánh giá hen kiểm soát tốt/một phần/không kiểm soát là gì?
5. **Xử trí đợt cấp (Acute bronchodilator/systemic steroid/oxygen specifics):** Liều lượng SABA (khí dung hoặc pMDI+spacer), liều corticosteroid toàn thân và mục tiêu SpO2 trong đợt cấp là bao nhiêu? Tiêu chuẩn chuyển viện là gì?
6. **Ranh giới chuyển tuyến hen nặng (Severe asthma referral/biologic boundary):** Khi nào bệnh nhân được định nghĩa là hen nặng cần chuyển chuyên khoa để xét dùng thuốc sinh học?

## 6. Canonical Research Workflow
1. **Khóa Research Brief:** Tạo file `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1_RESEARCH_BRIEF.md` (thay YYYY-MM-DD) với 6 claims trên. Khóa profile `disease` (hoặc profile phù hợp sau khi kiểm tra `publish_gate.py --list-profiles`), basename `IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1.md`.
2. **Sync Evidence:** Chạy `evidence_sync.py` để tạo provider-neutral bundle từ các nguồn official (GINA, ERS/ATS) hiện hành. KHÔNG dùng NCBI/Eutils.
3. **Offline Preflight:** Chạy `preflight_claim_check.py` với bundle offline.
4. **Viết bài:** Viết file Markdown dựa trên brief đã khóa. Chỉ dùng các nhãn canonical (`[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`) SAU KHI artifact tương ứng đã được sinh ra. Bắt buộc kiểm tra authority, current version, supersession, license, và provenance. Cấm dùng các nhãn cũ: `[TEXTBOOK]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[FULL VERIFIED]`.

## 7. Acceptance Checklist
- [ ] Độ dài 10,000 - 14,000 từ, văn xuôi hoàn chỉnh (không chỉ là dàn ý).
- [ ] Tỷ lệ hen ổn định 60%, đợt cấp 40%.
- [ ] Cấu trúc 18 sections như plan.
- [ ] Claims trong bài khớp hoàn toàn với Research Brief.
- [ ] Không có nhãn verification nào được gán nếu không có artifact chứng minh.
- [ ] File MD bài học là deliverable học tập duy nhất (không build APKG, DOCX, cards, Knowledge Check (KC), không chạy publish gate, không update catalog). Các artifact nội bộ (Research Brief, evidence bundle trong thư mục `outputs/`) được phép và bắt buộc tạo.
- [ ] Chạy các verifier chỉ dành cho bài giảng (lecture-only verifiers) nếu hỗ trợ, báo cáo giới hạn và exit code trung thực.
- [ ] Không có scaffold/stub; bài viết phải là văn xuôi hoàn chỉnh, đạt đủ word-count.

## 8. Execution Prompt for Next Model

```markdown
Bạn là AI assistant chuyên viết bài học y khoa cho dự án Mavis Research.
Nhiệm vụ của bạn là thực hiện quy trình nghiên cứu và viết bài học "IM-29 Hen phế quản" dựa trên Plan đã duyệt.

**YÊU CẦU BẮT BUỘC:**
1. **Đọc các file nền tảng (đường dẫn tuyệt đối):**
   - `F:/DL/mavisresearch/AGENTS.md`
   - `F:/DL/mavisresearch/Bai hoc y khoa/AGENTS.md`
   - `F:/DL/mavisresearch/Bai hoc y khoa/_CURRICULUM_NOI_KHOA.md`
   - `F:/DL/mavisresearch/Bai hoc y khoa/template_lesson.md`
   - `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/PLAN_AND_EXECUTION_PROMPT_IM29.md`
2. **Thực thi Canonical Workflow:**
   - Tạo `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1_RESEARCH_BRIEF.md` khóa profile `disease` (sau khi verify qua `--list-profiles` và lock emitted required gates), basename `IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1.md`, và 6 claim questions.
   - Inspect tool CLI trước khi chạy.
   - Chạy `evidence_sync.py` để tạo bundle trong `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/outputs/` (KHÔNG dùng NCBI/Eutils).
   - Chạy `preflight_claim_check.py` offline.
3. **Viết bài học:**
   - Viết file `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_YYYY-MM-DD_RELEASE_v1.md`.
   - Độ dài 10–14k từ, chuẩn L3_BEGINNER, văn xuôi hoàn chỉnh.
   - Tuân thủ Acceptance Checklist (không Mermaid, không bảng >=4 cột, có ASCII algorithm, BOX ĐỎ, Plan B). Không để lại scaffold/stub.
   - 5 Ca lâm sàng giải quyết qua đúng 5 bước: 1. Red flag, 2. Dữ kiện quyết định, 3. Hành động, 4. Monitoring/chuyển tuyến, 5. Why alternatives wrong.
   - Chẩn đoán phân biệt COPD: giải thích rõ tính khả hồi không phân biệt sạch sẽ hai bệnh; hô hấp ký bình thường không kết thúc workup.
   - Nếu một claim không thể verify qua bundle, HÃY BỎ QUA liều/ngưỡng chính xác hoặc thêm câu hỏi `CẦN TỰ KIỂM CHỨNG` riêng biệt; KHÔNG tự bịa số liệu.
   - CHỈ gán 5 nhãn canonical sau khi có artifact. Cấm dùng legacy labels.
4. **Giới hạn Deliverable:**
   - CHỈ trả về file MD bài học (deliverable học tập) và các artifact nội bộ (Research Brief, evidence bundle).
   - KHÔNG build APKG, DOCX, cards, KC. KHÔNG chạy publish. KHÔNG update catalog.
   - Chạy lecture-only verifiers (nếu có), báo cáo word-count thực tế, exit code trung thực và giới hạn.

Hãy bắt đầu bằng việc tạo Research Brief và tiến hành quy trình.
```
