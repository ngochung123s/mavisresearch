# RESEARCH BRIEF: THẤP TIM (ACUTE RHEUMATIC FEVER) Ở TRẺ EM (PED-51)

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
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "docx_build",
    "learner_smoke"
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
    "min_cases_with_solutions": 2,
    "min_practical_tips": 10,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [],
  "approved_exemptions": []
}
```

- Chế độ duy nhất: `L3_BEGINNER` (`L3 — Cầm tay chỉ việc cho người mất gốc`).
- **Output basename đã khóa:** `PED-51_Thap_tim_2026-09-28_RELEASE_v1`.
- Profile, required gates, `lesson_depth_contract` và output basename KHÔNG được đổi sau khi research bắt đầu (khóa ngày 2026-09-28).
- Ghi chú profile: brief gốc chốt `foundation` theo tiền lệ PED-32/40; tuân thủ headings + markers foundation (`tổng quan, định nghĩa, cơ chế, chẩn đoán, theo dõi, tóm tắt, tips, tài liệu tham khảo`; `nền tảng tối thiểu cần dùng ngay`, ` ```text`, `case 1`, `box đỏ`; `### 0.1` ≥15 dòng).

### Mục tiêu đào tạo
- Làm chủ định nghĩa và cơ chế sinh lý bệnh tự miễn của thấp tim (ARF): bắt chước phân tử (molecular mimicry) giữa protein M của liên cầu khuẩn β tan huyết nhóm A (GAS) và kháng nguyên tự thân (myosin cơ tim, laminin, lysoganglioside hạch nền).
- Nắm vững giải phẫu bệnh 3 thì (xuất tiết → hạt Aschoff/tế bào Anitschkow → xơ hóa van và dây chằng).
- Nắm vững 5 tiêu chuẩn chính Jones và tiêu chuẩn phụ; vận dụng Jones 2015 (phân tầng nguy cơ, viêm đơn khớp/đau đa khớp là chính ở nguy cơ cao, viêm tim âm thầm trên siêu âm Doppler theo WHF 2023).
- Chẩn đoán phân biệt 6 nhóm (JIA, viêm khớp nhiễm khuẩn, viêm khớp phản ứng, Schönlein-Henoch, viêm cơ tim virus, viêm nội tâm mạc nhiễm khuẩn).
- Nắm vững điều trị đa tầng theo thể (nghỉ ngơi 4 mức, kháng sinh tiệt căn, chống viêm bậc thang, suy tim, múa vờn).
- Quản lý phòng thấp cấp I + II (lịch BPG 21–28 ngày, thời hạn phân tầng theo AHA 2009 + WHO 2024 + Úc 2025).

### 🚨 QUY TẮC ĐÓNG CĂNG (FREEZE RULE & NO-PADDING)
1. **Cấm sửa Verifier Script** trong cùng workstream phát hành.
2. **Cấm tự chế Quote:** quote phải là exact substring từ local file/abstract; guideline quote bắt buộc exact substring + locator.
3. **Quy tắc dừng:** dừng khi acceptance matrix & `lesson_depth_contract` đạt 100%. CẤM dừng vì "bài đã dài". CẤM lặp ý, paraphrase padding, danh sách trần.

## 1. Phạm vi và preflight guideline

- Chủ đề và đối tượng học: Thấp tim (ARF) ở trẻ em — chẩn đoán Jones, điều trị đợt cấp theo thể, phòng thấp I + II. Đối tượng: bác sĩ nhi tuyến tỉnh, học viên Y6 mất gốc.
- Guideline chính thức đã kiểm freshness (Tier 0 ngày 2026-09-28; `preflight_guideline_check.py` WARN-vắng-registry cho cả 5 vì registry chỉ có ART — currency xác minh thủ công):
  - AHA 2015 Revised Jones Criteria (Circulation 2015;131:1806-1818, PMID 25908771) — chuẩn chẩn đoán gốc, current.
  - AHA 2009 RF prevention + GAS pharyngitis (Circulation 2009, PMID 19246689) — phòng cấp I + nguyên tắc phòng cấp II, current.
  - WHO 2024 RF/RHD guideline (ISBN 9789240100077, không PMID) — GAS, Jones endorsement, BPG first-line, current.
  - WHF 2023 echo RHD (Nat Rev Cardiol 2024;21:250-263, PMID 37914787) — siêu âm tim, current (thay thế WHF 2012).
  - Australian ARF/RHD Edition 3.3 August 2025 (không PMID) — bảng Jones chi tiết, phác đồ, thời hạn phòng thấp, current.
- Phạm vi được phép: dịch tễ toàn cầu (số VN dạng barem sách, không nhãn); LCA và mimicry; giải phẫu bệnh 3 giai đoạn; Jones 2015 + bảng delta Jones 1988 (sách) ↔ 2015; siêu âm tim WHF 2023; CĐPB 6 nhóm + mở rộng; điều trị đợt cấp; phòng thấp I + II.
- Ngoài phạm vi: can thiệp ngoại khoa van hậu thấp chi tiết; viêm nội tâm mạc nhiễm khuẩn (bài riêng); vắc xin LCA; suy tim mạn toàn diện (dẫn chiếu PED-48).

Guideline không PMID hợp lệ với evidence riêng (`pmid: null`). `guideline_evidence.json` + bản local trong `sources/` (tiền lệ PASS PED-32/40).

## 2. Papers đã chọn

- **PMID: 25908771** — Loại nguồn: AHA scientific statement (guideline). Vai trò: chuẩn chẩn đoán Jones 2015 gốc (viêm tim âm thầm là chính, phân tầng nguy cơ). Lý do chọn: chuẩn vàng chẩn đoán ARF toàn cầu.
- **PMID: 19246689** — Loại nguồn: AHA scientific statement (guideline). Vai trò: nguyên tắc phòng cấp I (cấy họng chuẩn vàng, penicillin lựa chọn) + khung phòng cấp II. Lý do chọn: guideline AHA về phòng thấp còn hiệu lực.
- **PMID: 37914787** — Loại nguồn: WHF guideline. Vai trò: tiêu chuẩn siêu âm xác định + sàng lọc, phân tầng A–D. Lý do chọn: chuẩn siêu âm RHD hiện hành.
- **PMID: 34767321** — Loại nguồn: RCT (GOAL, NEJM 2022). Vai trò: hiệu quả BPG dự phòng RHD tiềm ẩn (0.8% vs 8.2%). Lý do chọn: RCT nền cho phòng thấp ở bệnh tiềm ẩn.
- **PMID: 28834488** — Loại nguồn: GBD 2015 (NEJM 2017). Vai trò: gánh nặng toàn cầu (319,400 tử vong, 33.4M ca). Lý do chọn: dịch tễ chuẩn.
- **PMID: 38625703** — Loại nguồn: meta-analysis (JAMA Network Open 2024). Vai trò: điều trị múa vờn (corticoid, valproate, kháng sinh). Lý do chọn: tổng hợp lớn nhất về Sydenham chorea (1479 BN).
- **PMID: 17034886** — Loại nguồn: systematic review (Int J Cardiol 2007). Vai trò: tần suất viêm tim âm thầm 16.8%. Lý do chọn: SR nền cho subclinical carditis.
- **PMID: 17671255** — Loại nguồn: echo screening (NEJM 2007, Cambodia/Mozambique). Vai trò: siêu âm phát hiện gấp ~10 lần khám lâm sàng. Lý do chọn: landmark khu vực Đông Nam Á.
- **PMID: 27188830** — Loại nguồn: primer review (Nat Rev Dis Primers 2016, 720 cites). Vai trò: khung sinh bệnh + khẳng định penicillin mainstay. Lý do chọn: tổng quan chuẩn mực nhất về ARF/RHD.

Papers đã loại và lý do (xem §4): "AHA 2020 Secondary Prevention" (không tồn tại — PMID 32972288 là bài m6A RNA); "Webb 2021 JACC" (không tìm thấy — PMID 33514798 là bài ILC2); PMID 37872322 (bài ung thư, không phải WHF 2023); WHF 2012 (superseded); WHO TRS 923 (superseded); IDSA 2012 (archived, update 2025 chưa xong phần điều trị); GOAL-Post 2026 (PMID 42179243, không có abstract quotable).

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Chẩn đoán ARF đợt đầu xác định: 2 chính + bằng chứng Strep A, hoặc 1 chính + 2 phụ + bằng chứng | null (Aus 2025) | [GUIDELINE VERIFIED] | Definite initial episode of ARF: 2 major manifestations + evidence of preceding Strep A infection, or 1 major + 2 minor manifestations + evidence of preceding Strep A infection. | Mọi quần thể nghi ARF | Tiêu chuẩn Jones | Chẩn đoán xác định | Đợt đầu |
| C-002 | Chẩn đoán ARF tái phát (có tiền sử ARF/RHD): 2 chính, hoặc 1 chính + 2 phụ, hoặc 3 phụ + bằng chứng | null (Aus 2025) | [GUIDELINE VERIFIED] | Definite recurrent episode of ARF in a patient with a documented history of ARF or RHD: 2 major manifestations + evidence of preceding Strep A infection, or 1 major + 2 minor manifestations + evidence of preceding Strep A infection, or 3 minor manifestations + evidence of a preceding Strep A infection. | BN có tiền sử ARF/RHD | Tiêu chuẩn Jones tái phát | Chẩn đoán xác định | Tái phát (>90 ngày) |
| C-003 | Tiêu chuẩn chính ở nguy cơ cao gồm viêm tim (kể cả âm thầm), viêm đa khớp/viêm đơn khớp vô khuẩn/đau đa khớp, múa vờn, hồng ban vòng, hạt dưới da | null (Aus 2025) | [GUIDELINE VERIFIED] | Major manifestations (high-risk groups): Carditis (including subclinical evidence of rheumatic valvulitis on echocardiogram); Polyarthritis or aseptic monoarthritis or polyarthralgia; Sydenham chorea; Erythema marginatum; Subcutaneous nodules. | Quần thể nguy cơ cao | Tiêu chuẩn chính | Chẩn đoán | Đợt cấp |
| C-004 | Tiêu chuẩn phụ ở nguy cơ cao: sốt ≥38°C, đau đơn khớp, VS ≥30 mm/h hoặc CRP ≥30 mg/L, PR kéo dài | null (Aus 2025) | [GUIDELINE VERIFIED] | Minor manifestations (high-risk groups): Fever >=38C; Monoarthralgia; ESR >=30 mm/h or CRP >=30 mg/L; Prolonged P-R interval or advanced conduction abnormalities on ECG. | Quần thể nguy cơ cao | Tiêu chuẩn phụ | Chẩn đoán | Đợt cấp |
| C-005 | Nguy cơ cao = cộng đồng có ARF >30/100,000/năm (5–14 tuổi) hoặc RHD >2/1000 | null (Aus 2025) | [GUIDELINE VERIFIED] | High-risk groups are those living in communities with high rates of ARF (incidence >30/100,000 per year in 5-14-year-olds) or RHD (all-age prevalence >2/1000). | Cộng đồng | Phân tầng dịch tễ | Áp dụng tiêu chuẩn | — |
| C-006 | Bằng chứng Strep A trước đó: ASO/anti-DNase B tăng, hoặc cấy họng/RADT/NAAT dương | null (Aus 2025) | [GUIDELINE VERIFIED] | Evidence of preceding Strep A infection: Elevated or rising antistreptolysin O or Anti-DNase B, or a positive throat culture or rapid antigen or nucleic acid test for preceding Strep A infection. | BN nghi ARF | Xét nghiệm liên cầu | Bằng chứng nhiễm | Đợt cấp |
| C-007 | Múa vờn không cần biểu hiện khác hay bằng chứng Strep A nếu đã loại trừ nguyên nhân khác | null (Aus 2025) | [GUIDELINE VERIFIED] | Chorea does not require other manifestations or evidence of preceding Strep A infection, provided other causes of chorea are excluded. | BN múa vờn | Ngoại lệ Jones | Chẩn đoán | Muộn (2–6 tháng) |
| C-008 | Tái phát yêu cầu >90 ngày sau khởi phát đợt trước | null (Aus 2025) | [GUIDELINE VERIFIED] | Recurrent definite, probable or possible ARF requires a time period of more than 90 days after the onset of symptoms from the previous episode of definite, probable or possible ARF. | BN có tiền sử ARF | Quy tắc thời gian | Phân biệt tái phát | >90 ngày |
| C-009 | AHA 2015: siêu âm Doppler chẩn đoán viêm tim kể cả khi không có dấu lâm sàng; viêm tim âm thầm là tiêu chuẩn chính | 25908771 | [GUIDELINE VERIFIED] | a methodological assessment of the numerous published studies that support the use of Doppler echocardiography as a means to diagnose cardiac involvement in acute rheumatic fever, even when overt clinical findings are not apparent, was undertaken to determine the evidence basis for defining subclinical carditis and including it as a major criterion of the Jones criteria. | BN ARF | Siêu âm Doppler | Viêm tim âm thầm | Đợt cấp |
| C-010 | AHA 2015: lần sửa đổi lớn đầu tiên từ 1992; xác định quần thể nguy cơ cao + siêu âm tim | 25908771 | [GUIDELINE VERIFIED] | This revision of the Jones criteria now brings them into closer alignment with other international guidelines for the diagnosis of acute rheumatic fever by defining high-risk populations, recognizing variability in clinical presentation in these high-risk populations, and including Doppler echocardiography as a tool to diagnose cardiac involvement. | Quần thể toàn cầu | Jones 2015 | Chuẩn chẩn đoán | 2015 |
| C-011 | WHO: dùng tiêu chuẩn Jones chẩn đoán thấp tim ở trẻ em, vị thành niên và người lớn (Strong, low) | null (WHO 2024) | [GUIDELINE VERIFIED] | The Jones criteria should be used for RF diagnosis in children, adolescents and adults with suspected RF. (Strong recommendation, low certainty evidence) | Trẻ em/vị thành niên/người lớn nghi RF | Jones | Chẩn đoán | — |
| C-012 | Siêu âm tim là tiêu chuẩn vàng đánh giá viêm tim thấp và bệnh van hậu thấp (>25 nghiên cứu vượt trội hơn nghe tim) | null (WHO 2024) | [GUIDELINE VERIFIED] | Echocardiography has become the gold standard for evaluating patients for rheumatic carditis (during RF) and valvular pathology (during RHD), with more than 25 studies showing superiority in sensitivity and specificity compared to auscultation. | BN RF/RHD | Siêu âm vs nghe tim | Chẩn đoán van tim | — |
| C-013 | Siêu âm phát hiện 12.9/1000 so với nghe tim 2.9/1000 ở vùng lưu hành | null (WHO 2024) | [GUIDELINE VERIFIED] | identifying 12.9 cases per 1000 people (95% CI: 8.9-18.6) in endemic areas, compared to cardiac auscultation (2.9 cases detected per 1000 people; 95% CI: 1.7-5.0). | Vùng lưu hành | Siêu âm vs nghe | Phát hiện RHD | Sàng lọc |
| C-014 | WHF 2023: phân tầng RHD thành A–D theo nguy cơ tiến triển; bỏ thuật ngữ borderline/definite/latent | 37914787 | [GUIDELINE VERIFIED] | Classification of RHD into stages A, B, C and D on the basis of the risk of progression to more advanced valvular heart disease; the terms 'borderline', 'definite' and 'latent' RHD are no longer recommended. | BN RHD siêu âm | Phân tầng WHF 2023 | Nguy cơ tiến triển | — |
| C-015 | WHF 2023 xác định hở hai lá bệnh lý: 2 mặt cắt, jet ≥1.5 cm (<30 kg) hoặc ≥2.0 cm (≥30 kg), vận tốc >3.0 m/s, toàn tâm thu | 37914787 | [GUIDELINE VERIFIED] | Criteria for pathological MR (requires all): Observed in two views; Minimum MR jet length (1.5 cm for patients weighing <30 kg and 2.0 cm for patients weighing >=30 kg) observed in one view; Velocity >3.0 m/s; Pan-systolic jet. | BN nghi RHD | Doppler van hai lá | Hở van bệnh lý | — |
| C-016 | WHF 2023 xác định hở chủ bệnh lý: 2 mặt cắt, jet ≥1.0 cm, vận tốc ≥3.0 m/s đầu tâm trương, toàn tâm trương; hẹp hai lá: gradient trung bình ≥4.0 mmHg | 37914787 | [GUIDELINE VERIFIED] | Pathological (at least mild) AR (all criteria must be met): Observed in at least two views; Observed in at least one view, AR jet length >= 1.0 cm; Velocity >= 3.0 m/s in early diastole; Pan-diastolic jet in at least one envelope. | BN nghi RHD | Doppler van chủ | Hở van bệnh lý | — |
| C-017 | Phòng cấp I: nhận diện đúng + điều trị kháng sinh đầy đủ viêm họng GAS; cấy họng là tiêu chuẩn vàng | 19246689 | [GUIDELINE VERIFIED] | Primary prevention of acute rheumatic fever is accomplished by proper identification and adequate antibiotic treatment of group A beta-hemolytic streptococcal (GAS) tonsillopharyngitis. | Trẻ viêm họng GAS | Kháng sinh đầy đủ | Phòng ARF | Cấp I |
| C-018 | Penicillin (V uống hoặc benzathine tiêm) là lựa chọn hàng đầu; chưa ghi nhận GAS kháng penicillin | 19246689 | [GUIDELINE VERIFIED] | Penicillin (either oral penicillin V or injectable benzathine penicillin) is the treatment of choice, because it is cost-effective, has a narrow spectrum of activity, and has long-standing proven efficacy, and GAS resistant to penicillin have not been documented. | Viêm họng GAS | Penicillin | Tiệt căn | 10 ngày/1 liều |
| C-019 | Người đã bị thấp tim nguy cơ tái phát rất cao, cần dự phòng kháng sinh liên tục; thời hạn tùy số đợt, thời gian, phơi nhiễm, tuổi, tổn thương tim | 19246689 | [GUIDELINE VERIFIED] | The individual who has had an attack of rheumatic fever is at very high risk of developing recurrences after subsequent GAS pharyngitis and needs continuous antimicrobial prophylaxis to prevent such recurrences (secondary prevention). | BN sau ARF | Dự phòng liên tục | Phòng tái phát | Cấp II |
| C-020 | WHO: viêm họng có XN GAS dương tính phải điều trị kháng sinh (Strong, moderate); vùng nguy cơ cao không có XN thì điều trị theo lâm sàng (Strong, very low); penicillin first-line (Conditional, low) | null (WHO 2024) | [GUIDELINE VERIFIED] | For patients with a positive diagnostic test for GAS pharyngitis or with clinically-suspected GAS, WHO recommends penicillin (intramuscular (IM) or oral) as first-line treatment for the prevention of RF/RHD. (Conditional recommendation, low certainty evidence) | Viêm họng GAS/nghi GAS | Penicillin IM/uống | Phòng RF/RHD | Cấp I |
| C-021 | WHO: mọi trẻ/vị thành niên/người lớn chẩn đoán RF hoặc RHD đều cần dự phòng kháng sinh (Strong, moderate) | null (WHO 2024) | [GUIDELINE VERIFIED] | Children, adolescents and adults diagnosed with RF or RHD should be prescribed antibiotic prophylaxis to prevent RF recurrence. (Strong recommendation, moderate certainty evidence) | BN RF/RHD | Dự phòng kháng sinh | Phòng tái phát | Cấp II |
| C-022 | WHO: BPG tiêm bắp là first-line dự phòng tái phát (Strong, moderate); penicillin uống chấp nhận được nếu cần thay thế (Conditional, moderate) | null (WHO 2024) | [GUIDELINE VERIFIED] | IM benzathine benzylpenicillin (BPG), is the preferred first-line approach to prevent recurrence of RF in patients with prior RF or RHD. (Strong recommendation, moderate certainty evidence) | BN RF/RHD | BPG IM | Phòng tái phát | Cấp II |
| C-023 | BPG dự phòng: dị ứng 2%, phản vệ/tử vong 0.27%; tuân thủ >80% mũi tiêm giảm tử vong RHD | null (WHO 2024) | [GUIDELINE VERIFIED] | A review of patients receiving BPG for RHD prophylaxis reported an overall rate of allergic reactions of 2%, and anaphylactic reactions and fatalities of 0.27%. | BN dự phòng BPG | BPG IM | An toàn/tuân thủ | Dài hạn |
| C-024 | Úc 2025 dự phòng cấp II: BPG 1,200,000 đv (≥20 kg) / 600,000 đv (<20 kg) tiêm bắp sâu mỗi 28 ngày (21 ngày cho nhóm chọn lọc) | null (Aus 2025) | [GUIDELINE VERIFIED] | First line: Benzathine benzylpenicillin G (BPG) 1,200,000 units (>=20 kg) or 600,000 units (<20 kg), deep intramuscular injection, every 28 days (every 21 days for selected groups). | BN RF/RHD | BPG IM | Phòng tái phát | 21–28 ngày |
| C-025 | Úc 2025 thời hạn: ARF không tim 5 năm/21 tuổi; có tim 10 năm/21 tuổi; Stage A 2 năm; Stage B 10 năm/21 tuổi; C vừa 10 năm/35 tuổi; C nặng/D 10 năm/40 tuổi | null (Aus 2025) | [GUIDELINE VERIFIED] | Definite ARF (no cardiac involvement): Minimum of 5 years after most recent episode of ARF, or until age 21 years (whichever is longer), then reassess. | BN ARF/RHD phân tầng | BPG theo thời hạn | Phòng tái phát | 2–10+ năm |
| C-026 | Úc 2025 điều trị viêm họng Strep A: BPG 1 liều duy nhất theo cân nặng, hoặc penicillin V/azithromycin/cefalexin/amoxicillin uống | null (Aus 2025) | [GUIDELINE VERIFIED] | All cases: Benzathine benzylpenicillin G (BPG) single deep intramuscular injection once (Child <10 kg: 450,000 units; 10 to <20 kg: 600,000 units; >=20 kg and Adult: 1,200,000 units). | Viêm họng Strep A | BPG/kháng sinh uống | Tiệt căn | 1 liều/5–10 ngày |
| C-027 | Khi ARF đã biểu hiện, cấy thường âm tính nhưng vẫn phải tiệt căn liên cầu có thể còn tồn tại | null (Aus 2025) | [GUIDELINE VERIFIED] | streptococcal infection may not be evident by the time ARF manifests (e.g. cultures often negative) but eradication therapy for possible persisting streptococci is recommended, nonetheless. | BN ARF mới | Tiệt căn LCA | Diệt ổ còn lại | Đợt cấp |
| C-028 | Chờ xác định chẩn đoán: paracetamol là giảm đau ưu tiên để tránh che lấp triệu chứng khớp di chuyển/sốt/viêm | null (Aus 2025) | [GUIDELINE VERIFIED] | preferred initial analgesia during diagnostic uncertainty, to avoid the masking effect that anti-inflammatory use can have on migratory joint symptoms, fever and inflammatory markers. | Nghi ARF chưa rõ | Paracetamol | Giảm đau không che lấp | Chờ CĐ |
| C-029 | Viêm khớp sau xác định ARF: naproxen/ibuprofen/aspirin 50–60 mg/kg/ngày chia 4–5 lần, tối đa 80–100 mg/kg/ngày | null (Aus 2025) | [GUIDELINE VERIFIED] | Aspirin adults and children 50-60 mg/kg/day orally, in four to five divided doses, escalated up to a maximum of 80-100 mg/kg/day in four to five divided doses. | Viêm khớp ARF | NSAID/aspirin | Giảm viêm khớp | Đợt cấp |
| C-030 | Múa vờn vừa–nặng: carbamazepine/valproate + prednisolone 1–2 mg/kg tối đa 80 mg | null (Aus 2025) | [GUIDELINE VERIFIED] | Symptomatic management of moderate to severe chorea: Carbamazepine 3.5 to 10 mg/kg per dose orally, twice daily; Sodium valproate 7.5 to 10 mg/kg per dose orally, twice daily; plus Prednisone/prednisolone 1 to 2 mg/kg up to a maximum of 80 mg orally, once daily or in divided doses. | Múa vờn vừa–nặng | Chống múa vờn | Kiểm soát vận động | Đợt cấp |
| C-031 | Viêm tim suy tim trẻ em: furosemide 1–2 mg/kg rồi 0.5–1 mg/kg (tối đa 6 mg/kg); spironolactone; enalapril tăng dần tối đa 1 mg/kg | null (Aus 2025) | [GUIDELINE VERIFIED] | Symptomatic management of carditis (paediatric dosing): Furosemide 1 to 2 mg/kg orally as a single dose, then 0.5 to 1 mg/kg (to a maximum of 6 mg/kg) orally, 6- to 24-hourly | Viêm tim suy tim | Lợi tiểu/ức chế men chuyển | Ổn định huyết động | Cấp cứu |
| C-032 | Corticoid (prednisolone 1–2 mg/kg, tối đa 80 mg) chỉ cân nhắc ca viêm tim nặng chọn lọc vì meta-analysis không thấy lợi ích tổng thể (2C) | null (Aus 2025) | [GUIDELINE VERIFIED] | Considered for use in selected cases of severe carditis, despite meta-analyses in which overall benefit was not evident. | Viêm tim nặng chọn lọc | Prednisolone | Miễn dịch | Đợt cấp |
| C-033 | GOAL: BPG mỗi 4 tuần × 2 năm giảm tiến triển RHD tiềm ẩn còn 0.8% so với 8.2% (RD −7.5pp, 95% CI −10.2 đến −4.7, P<0.001) | 34767321 | [DATA VERIFIED] | A total of 3 participants (0.8%) in the prophylaxis group had echocardiographic progression at 2 years, as compared with 33 (8.2%) in the control group (risk difference, -7.5 percentage points; 95% confidence interval, -10.2 to -4.7; P<0.001). | Trẻ 5–17 tuổi RHD tiềm ẩn Uganda | BPG IM q4w × 2 năm vs không dự phòng | Tiến triển siêu âm | 2 năm |
| C-034 | RHD ảnh hưởng >40.5 triệu người, 306,000 tử vong/năm toàn cầu | 34767321 | [DATA VERIFIED] | Rheumatic heart disease affects more than 40.5 million people worldwide and results in 306,000 deaths annually. | Toàn cầu | — | Gánh nặng RHD | Hằng năm |
| C-035 | GBD 2015: 319,400 tử vong RHD; tử vong chuẩn tuổi giảm 47.8% (1990–2015); 33.4M ca; 10.5M DALY | 28834488 | [DATA VERIFIED] | We estimated that there were 319,400 (95% uncertainty interval, 297,300 to 337,300) deaths due to rheumatic heart disease in 2015. | Toàn cầu 1990–2015 | — | Tử vong/ca/DALY | 2015 |
| C-036 | Múa vờn (1479 BN): corticoid ≥1 tháng rút ngắn 1.2 vs 2.8 tháng; kháng sinh/corticoid/valproate giảm tái phát (OR 0.28/0.32/0.33) | 38625703 | [DATA VERIFIED] | The median chorea duration in patients receiving 1 or more months of corticosteroids was 1.2 months (95% CI, 1.2-2.0) vs 2.8 months (95% CI, 2.0-3.0) for patients receiving none (P = .004). | Múa vờn Sydenham | Corticoid ≥1 tháng | Thời gian múa vờn | Theo dõi |
| C-037 | Viêm tim âm thầm gộp 16.8% ARF (95% CI 11.9–21.6); tồn tại/nặng lên 44.7% sau 3–23 tháng | 17034886 | [DATA VERIFIED] | The weighted pooled prevalence of SCC in ARF was 16.8% (95%CI 11.9 to 21.6). | BN ARF (23 nghiên cứu) | Siêu âm tim | Viêm tim âm thầm | Đợt cấp |
| C-038 | Sàng lọc siêu âm phát hiện RHD gấp ~10 lần khám lâm sàng (Cambodia 21.5 vs 2.2/1000; Mozambique 30.4 vs 2.3/1000) | 17671255 | [DATA VERIFIED] | Systematic screening with echocardiography, as compared with clinical screening, reveals a much higher prevalence of rheumatic heart disease (approximately 10 times as great). | Học sinh 6–17 tuổi Cambodia/Mozambique | Siêu âm vs khám | Phát hiện RHD | Sàng lọc |
| C-039 | Penicillin là mainstay hàng thập kỷ; chưa có điều trị nào khác được chứng minh làm đổi tiến triển RHD sau ARF | 27188830 | [ABSTRACT VERIFIED] | Indeed, penicillin has been the mainstay of treatment for decades and there is no other treatment that has been proven to alter the likelihood or the severity of RHD after an episode of ARF. | BN sau ARF | Penicillin vs khác | Tiến triển RHD | Dài hạn |

Quy tắc nhãn: 5 nhãn canonical duy nhất. Kiến thức consensus (sinh lý, mimicry cơ bản, giải phẫu bệnh kinh điển) viết tự do KHÔNG nhãn, KHÔNG PMID.

## 4. Claims và số liệu cấm dùng

- "AHA 2020 Secondary Prevention" (PMID 32972288 là bài m6A RNA — tuyên bố guideline này KHÔNG tồn tại sau khi tìm kiếm title): cấm toàn bộ C-005..C-009 của brief cũ.
- "Webb 2021 JACC" (PMID 33514798 là bài ILC2 — không tìm thấy bài đúng title): cấm toàn bộ liều aspirin/prednisolone gán cho nguồn này; liều EBM lấy từ Úc 2025 Table 7.1 (C-029/C-030/C-032).
- PMID 37872322 (bài ung thư): cấm; WHF 2023 đúng là PMID 37914787.
- WHF 2012 (Reményi): superseded bởi WHF 2023 (bỏ borderline/definite/latent, thêm weight-based jet).
- WHO TRS 923 (2004): superseded bởi WHO 2024 cho khuyến cáo chung; thời hạn phòng thấp lấy từ Úc 2025 Table 10.3.
- IDSA 2012 GAS (PMID 22965026): archived, update 2025 mới xong phần đánh giá nguy cơ; kháng sinh lấy từ AHA 2009 + Úc 2025.
- GOAL-Post 2026 (PMID 42179243): không có abstract quotable (EPMC core rỗng, OpenAlex cụt) — cấm trích số 5 năm.
- Số VN 3.94/1000 trẻ/năm và 20 triệu/5 triệu (sách YTB): không truy được nguồn citable → trình bày dạng barem sách, KHÔNG nhãn verification, KHÔNG bịa PMID/quote.
- Aspirin sách 100 mg/kg tấn công → 75 mg/kg duy trì: barem thi (Track 1), đối chiếu delta với Úc 2025 (50–60 → tối đa 80–100) trong bài, không gán nhãn EBM cho số sách.
- Jones 1988 của sách: barem thi (Track 1); chuẩn EBM là Jones 2015 (Track 2) + bảng delta.

## 5. Dàn ý chi tiết

Mỗi mục ghi Claim ID sử dụng. Flowchart ASCII `text`, không Mermaid.

### 0. Nền tảng tối thiểu cần dùng ngay
- Kiến thức consensus: GAS là gì, Jones là gì, thấp tim khác thấp khớp thế nào, vì sao tim nguy hiểm nhất.
- Claim IDs: C-034 (gánh nặng), C-039 (penicillin mainstay).

### 1. Tổng quan và định nghĩa
- Định nghĩa ARF/RHD (Carapetis), dịch tễ GBD + GOAL background + VN barem (không nhãn).
- Bảng delta Jones 1988 (sách) ↔ 2015 (EBM): nguy cơ thấp/cao, viêm tim âm thầm, khớp, sốt/VS.
- Claim IDs: C-034, C-035, C-010, C-011.

### 2. Cơ chế
- Chuỗi 5 tầng: protein M/GAS họng → mimicry (myosin/laminin/ganglioside) → LB/LT → viêm tim/khớp/não/da → Jones.
- Sơ đồ Warren Toews (sách) + giải thích hiện đại; trang 136 thiếu trong scan — lấp từ y văn, ghi chú rõ.
- Claim IDs: C-039 (tự miễn hậu GAS).

### 3. Chẩn đoán và phân tầng
- Jones 2015 đầy đủ (luật đợt đầu/tái phát, chính/phụ theo nguy cơ, bằng chứng Strep A, ngoại lệ múa vờn, quy tắc 90 ngày, chống double-count).
- Siêu âm tim: gold standard, WHF 2023 (sàng lọc + xác định + staging A–D), SCC 16.8%, Marijon ~10x, WHO 12.9 vs 2.9/1000.
- CLS: ASO/anti-DNase B, cấy họng, VS/CRP, ECG (PR), XQ.
- CĐPB 6 nhóm sách + mở rộng.
- Claim IDs: C-001..C-010, C-012..C-016, C-037, C-038.

### 4. Điều trị/theo dõi
- Tiệt căn LCA (BPG/liều sách + Úc), paracetamol chờ CĐ, NSAID/aspirin (delta sách↔Úc), corticoid chọn lọc viêm tim nặng, suy tim (furosemide/spiro/enalapril), múa vờn (carbamazepine/valproate + prednisolone; số liệu MA 2024).
- Nghỉ ngơi 4 mức (sách, barem).
- Phòng cấp I (điều trị viêm họng GAS + kinh nghiệm Úc/WHO) và cấp II (BPG 28/21 ngày, thời hạn phân tầng, tuân thủ >80%, an toàn BPG, GOAL).
- Claim IDs: C-017..C-033, C-036.

### 5. Flowchart ASCII và BOX ĐỎ
- Nhánh cấp cứu: suy tim cấp/viêm tim ác tính, đau ngực/ngất (viêm màng ngoài tim, block).
- Nhánh thường quy: nghi ARF → Jones + bằng chứng Strep A + siêu âm → phân thể → điều trị + phòng thấp.
- Nhánh thiếu nguồn lực/Plan B: không siêu âm/XN → Jones lâm sàng + điều trị kinh nghiệm + chuyển tuyến.
- BOX ĐỎ: aspirin + virus (Reye), che lấp chẩn đoán do NSAID sớm, sốc phản vệ BPG, tuân thủ.

### 6. Case và lời giải
- Case 1: trẻ 8 tuổi viêm đa khớp di chuyển + thổi tim mới (Jones đủ, viêm tim nhẹ) — chẩn đoán + phác đồ + phòng thấp.
- Case 2: trẻ 11 tuổi múa vờn đơn độc sau 4 tháng (ngoại lệ Jones) — chẩn đoán + điều trị múa vờn + phòng thấp.
- Claim IDs: C-001, C-003, C-007, C-024, C-025, C-029, C-030, C-036.

### 7. Tổng kết và tài liệu tham khảo
- Tóm tắt 10 mệnh lệnh (Jones, siêu âm, BPG, phòng thấp, tuân thủ).
- TÀI LIỆU THAM KHẢO: 9 papers + 2 guidelines (đánh số, PMID đầy đủ).
- Claim IDs: toàn bộ.

## 6. Hướng dẫn model execute

1. **Chế độ duy nhất:** `L3_BEGINNER`. Viết chi tiết, dạy từ gốc, phủ đầy đủ `lesson_depth_contract` foundation.
2. Chỉ dùng claims trong bảng và giữ `{claim:C-xxx}` gần claim tương ứng để verifier truy vết.
3. Không thêm claim, PMID, guideline hoặc con số ngoài brief.
4. Chỉ dùng năm nhãn verification chuẩn. Cấm tuyệt đối các nhãn cũ.
5. **Tách biệt nguồn:** Kiến thức consensus không cần nhãn/PMID; claim định lượng phải có evidence và exact quote. Không được bịa PMID/quote.
6. Viết tiếng Việt có dấu; tiếng Việt trước, English trong ngoặc lần đầu.
7. Flowchart dùng `text` ASCII/danh sách phân cấp, KHÔNG DÙNG MERMAID.
8. Nếu một claim không đủ bằng chứng, bỏ claim thay vì suy diễn.
9. **Quy tắc dừng:** Dừng khi acceptance matrix & `lesson_depth_contract` thỏa mãn 100%. CẤM dừng vì "bài đã dài", CẤM lặp ý hay paraphrase padding.
10. Output gồm Markdown + cards V2; DOCX, APKG và learner smoke do release runner tạo trong `outputs/`.
11. Dual-track: Track 1 `[🏛️ BAREM GỐC Y THÁI BÌNH]` (Jones 1988, liều sách, nghỉ ngơi, phòng thấp VN) + Track 2 `[🔬 EBM HIỆN ĐẠI]` (Jones 2015, WHF 2023, BPG, GOAL) + bảng delta mỗi khi khác nhau.
12. Trình bày chuẩn: KHÔNG `%` trong `$math$`; bảng ≤3 cột chữ dài; filename không dấu.
