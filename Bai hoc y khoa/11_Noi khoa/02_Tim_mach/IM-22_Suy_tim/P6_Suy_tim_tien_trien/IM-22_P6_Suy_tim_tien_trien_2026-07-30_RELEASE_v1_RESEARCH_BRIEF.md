---
profile: "disease"
lesson_depth_contract: "L3_BEGINNER"
output_basename: "IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1"
evidence_bundle: "outputs/IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1_evidence_bundle.json"
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
  "not_applicable": [],
  "approved_exemptions": []
}
```

## Release acceptance riêng của đợt remediation IM-22 Part 6

- **release_acceptance.min_total_words:** `10000`.
- **release_acceptance.max_total_words:** `14000`.
- **release_acceptance.exact_cases:** `5`.
- **Quan sát khóa ngày 2026-07-30:** bài có `12392` từ phân tách bằng khoảng trắng và đúng `5` ca lâm sàng.
- Khối này bổ sung tiêu chuẩn biên tập nghiêm ngặt của Part 6; khối `lesson_depth_contract` phía trên giữ đúng contract executable canonical của profile `disease`.

# Research Brief: Suy tim tiến triển và quản lý dài hạn — Part 6

## Metadata khóa trước prose

- **Profile:** `disease`.
- **Depth:** `L3_BEGINNER` — cầm tay chỉ việc cho người mất gốc.
- **Basename khóa:** `IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1`.
- **Bài nguồn khóa:** `IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1.md`.
- **Evidence bundle khóa:** `outputs/IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1_evidence_bundle.json`.
- **Guideline evidence:** `outputs/IM-22_P6_Suy_tim_tien_trien_2026-07-30_RELEASE_v1_guideline_evidence.json`.
- **Nguồn chính thức:** 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure, PMID 35363499, bản toàn văn chính thức lưu tại `outputs/sources/aha_acc_hfsa_2022_full.pdf`.
- **Ngày khóa claim:** 2026-07-30.

## 1. Phạm vi và preflight guideline

- **Đối tượng học:** bác sĩ, học viên sau đại học và người học mất gốc cần hiểu suy tim tiến triển từ khái niệm đến quyết định chuyển tuyến.
- **Trong phạm vi:** nhận diện advanced HF; I-NEED-HELP; khái niệm INTERMACS; thời điểm chuyển tuyến; ICD; CRT; van tim cơ năng; LVAD; đánh giá ghép tim; chăm sóc giảm nhẹ; phục hồi chức năng; tiêm chủng; tự theo dõi; follow-up.
- **Ngoài phạm vi:** chi tiết giảm sung huyết ICU, sốc tim, liều inotrope/vasopressor, kỹ thuật cấy thiết bị, cài đặt máy, phác đồ chống đông LVAD, ức chế miễn dịch sau ghép và lịch vắc-xin định lượng.
- **Nguyên tắc an toàn:** chuyển tuyến khi cửa sổ điều trị còn mở; không đợi suy đa tạng; mọi quyết định thiết bị, van, LVAD hoặc ghép tim do nhóm chuyên khoa đa ngành cá thể hóa.

## 2. Papers đã chọn

- **PMID: 35363499**
  - Loại nguồn: Practice Guideline / Clinical Practice Guideline chính thức AHA/ACC/HFSA.
  - Vai trò: nguồn duy nhất cho các khuyến cáo, ngưỡng và thuật toán định lượng trong bài.
  - Lý do chọn: bản current được ACC Heart Failure Guideline Hub công bố; nguồn chính thức có toàn văn local, hash và provenance.

**Nguồn đã xem nhưng không đưa vào claim set:**
- ESC 2021: hữu ích để đối chiếu bối cảnh, nhưng không đưa vào claim set để giữ một nguồn chính thức duy nhất.
- ISHLT transplant/LVAD documents: không khóa claim cụ thể do chưa có artifact official-source current đủ schema trong workstream này.
- Lịch tiêm chủng của cơ quan y tế: không khóa lịch, liều hoặc tuổi cụ thể; bài chỉ yêu cầu kiểm lịch quốc gia hiện hành.

## 3. Claims đã verify

| Claim ID | Claim | PMID / Source | Verification | Quote từ nguồn |
|---|---|---|---|---|
| P6-C01 | Timely referral for advanced HF specialty care is recommended to review management and assess suitability for LVAD, cardiac transplantation, palliative care, and palliative inotropes when consistent with goals of care. | PMID: 35363499 | [GUIDELINE VERIFIED] | In patients with advanced HF, when consistent with the patient’s goals of care, timely referral for HF specialty care is recommended to review HF management and assess suitability for advanced HF therapies (e.g., LVAD, cardiac transplantation, palliative care, and palliative inotropes) (1-6). |
| P6-C02 | I-NEED-HELP is a referral mnemonic covering intravenous inotropes, severe NYHA symptoms or elevated natriuretic peptides, end-organ dysfunction, low EF, defibrillator shocks, repeated hospitalizations, refractory edema, low systolic pressure or high heart rate, and progressive intolerance of prognostic medication. | PMID: 35363499 | [GUIDELINE VERIFIED] | I, Intravenous inotropes N, New York Heart Association (NYHA) class IIIB to IV or persistently elevated natriuretic peptides E, End-organ dysfunction E, EF #35% D, Defibrillator shocks H, Hospitalizations >1 E, Edema despite escalating diuretics L, Low systolic BP #90, high heart rate P, Prognostic medication; progressive intolerance or down-titration of GDMT |
| P6-C03 | INTERMACS uses seven profiles to stratify advanced HF from critical cardiogenic shock through stable advanced NYHA class III status. | PMID: 35363499 | [GUIDELINE VERIFIED] | The INTERMACS (Interagency Registry for Mechanically Assisted Circulatory Support) has developed 7 profiles that further stratify patients with advanced HF (Table 17) (7). |
| P6-C04 | Primary-prevention ICD is recommended for nonischemic DCM or ischemic heart disease at least 40 days after MI, LVEF 35% or lower, NYHA II–III on chronic GDMT, with expected meaningful survival longer than one year. | PMID: 35363499 | [GUIDELINE VERIFIED] | In patients with nonischemic DCM or ischemic heart disease at least 40 days post-MI with LVEF £35% and NYHA class II or III symptoms on chronic GDMT, who have reasonable expectation of meaningful survival for >1 year, ICD therapy is recommended for primary prevention of SCD to reduce total mortality (1-9). |
| P6-C05 | ICD and CRT-D are not indicated when comorbidity or frailty limits survival with good functional capacity to less than one year. | PMID: 35363499 | [GUIDELINE VERIFIED] | For patients whose comorbidities or frailty limit survival with good functional capacity to <1 year, ICD and cardiac resynchronization therapy with defibrillation (CRT-D) are not indicated (1-9,16-21). |
| P6-C06 | CRT is indicated for LVEF 35% or lower, sinus rhythm, LBBB with QRS at least 150 ms, and NYHA II, III or ambulatory IV symptoms on GDMT. | PMID: 35363499 | [GUIDELINE VERIFIED] | For patients who have LVEF £35%, sinus rhythm, left bundle branch block (LBBB) with a QRS duration ‡150 ms, and NYHA class II, III, or ambulatory IV symptoms on GDMT, CRT is indicated to reduce total mortality, reduce hospitalizations, and improve symptoms and QOL (16-21). |
| P6-C07 | CRT is not recommended when QRS duration is below 120 ms. | PMID: 35363499 | [GUIDELINE VERIFIED] | In patients with QRS duration <120 ms, CRT is not recommended (36-41). |
| P6-C08 | Significant valvular disease in HF warrants multidisciplinary evaluation, and chronic severe secondary MR with HFrEF requires GDMT optimization before intervention. | PMID: 35363499 | [GUIDELINE VERIFIED] | In patients with chronic severe secondary MR and HFrEF, optimization of GDMT is recommended before any intervention for secondary MR related to LV dysfunction (3-5,12-14). |
| P6-C09 | Durable LVAD is effective in selected advanced HFrEF patients with NYHA IV who depend on continuous intravenous inotropes or temporary MCS. | PMID: 35363499 | [GUIDELINE VERIFIED] | In select patients with advanced HFrEF with NYHA class IV symptoms who are deemed to be dependent on continuous intravenous inotropes or temporary MCS, durable LVAD implantation is effective to improve functional status, QOL, and survival (1-18). |
| P6-C10 | Cardiac transplantation is indicated for selected advanced HF patients despite GDMT to improve survival and quality of life. | PMID: 35363499 | [GUIDELINE VERIFIED] | For selected patients with advanced HF despite GDMT, cardiac transplantation is indicated to improve survival and QOL (1-3). |
| P6-C11 | Palliative and supportive care should be integrated for all HF patients, and discontinuation of life-extending therapy should be anticipated and revisited as condition and goals change. | PMID: 35363499 | [GUIDELINE VERIFIED] | For all patients with HF, palliative and supportive care—including high-quality communication, conveyance of prognosis, clarifying goals of care, shared decision-making, symptom management, and caregiver support—should be provided to improve QOL and relieve suffering (1). |
| P6-C12 | The option to discontinue life-extending therapy should be discussed from initiation and reassessed as medical conditions and goals change. | PMID: 35363499 | [GUIDELINE VERIFIED] | For patients with HF being considered for, or treated with, life-extending therapies, the option for discontinuation should be anticipated and discussed through the continuum of care, including at the time of initiation, and reassessed with changing medical conditions and shifting goals of care (2,3). |
| P6-C13 | Exercise or regular physical activity is recommended for patients able to participate; cardiac rehabilitation can improve functional capacity, exercise tolerance and quality of life. | PMID: 35363499 | [GUIDELINE VERIFIED] | For patients with HF who are able to participate, exercise training (or regular physical activity) is recommended to improve functional status, exercise performance, and QOL (1-9). |
| P6-C14 | Vaccination against respiratory illnesses is reasonable in HF, while exact products and schedules must follow current local immunization guidance. | PMID: 35363499 | [GUIDELINE VERIFIED] | In patients with HF, vaccinating against respiratory illnesses is reasonable to reduce mortality (10-16). |
| P6-C15 | HF patients should receive multidisciplinary education and support to facilitate self-care. | PMID: 35363499 | [GUIDELINE VERIFIED] | Patients with HF should receive specific education and support to facilitate HF self-care in a multidisciplinary manner (2,5-9). |

## 4. Claims và số liệu cấm dùng

- Không nêu lợi ích trial bằng HR, RR, CI, tỷ lệ phần trăm, cỡ mẫu hoặc thời gian sống vì không khóa claim trial định lượng.
- Không dùng ngưỡng COAPT chi tiết cho TEER; chỉ khóa nguyên tắc tối ưu GDMT rồi Heart Team đánh giá.
- Không dùng ngưỡng peak VO2, khoảng đi bộ, liều lợi tiểu, sodium, huyết áp hoặc natri để xác định advanced HF ngoài mnemonic đã khóa.
- Không ghi chống chỉ định ghép tim thành danh sách tuyệt đối theo tuổi, BMI, áp lực phổi, eGFR hoặc thời gian ung thư; các biên này phụ thuộc trung tâm và chưa có artifact ISHLT current trong bundle.
- Không ghi lịch, liều, tuổi hoặc sản phẩm vắc-xin cụ thể; yêu cầu đối chiếu lịch quốc gia hiện hành.
- Không ghi liều opioid, liều an thần hoặc protocol bất hoạt thiết bị.
- Không ghi tỷ lệ biến chứng LVAD; chỉ mô tả cơ chế và nhóm biến chứng định tính.
- Không khẳng định mọi người bệnh advanced HF đều phù hợp LVAD hay ghép tim.
- Không dùng con số tăng cân nhanh để tự tăng lợi tiểu vì chưa khóa protocol cá thể hóa.

## 5. Dàn ý chi tiết và coverage map

### 0. Tổng quan, prerequisite và boundary
- Giải thích Part 6 nối Part 3–5; cấp cứu sung huyết/sốc thuộc Part 5.
- Claim IDs: P6-C01.

### 1. Nền tảng và nhận diện advanced HF
- Stage D, trajectory, khác biệt giữa “EF thấp” và “advanced”.
- I-NEED-HELP từng chữ, giới hạn mnemonic.
- INTERMACS bảy profile theo ý nghĩa quỹ đạo, không dùng làm công cụ tự cấy LVAD.
- Claim IDs: P6-C01, P6-C02, P6-C03.

### 2. Referral timing và đánh giá đa ngành
- Chuyển khi còn cửa sổ; không đợi sốc hoặc suy đa tạng.
- Plan A trung tâm advanced HF; Plan B liên hệ tim mạch tuyến trên, tóm tắt hồ sơ và kế hoạch an toàn.
- Claim IDs: P6-C01.

### 3. ICD
- Phân biệt primary/secondary prevention; cơ chế nhận diện và chấm dứt VT/VF.
- Ngưỡng primary prevention khóa; secondary prevention trình bày nguyên tắc, không thêm ngưỡng.
- Shared decision, gánh nặng tử vong không do loạn nhịp, sốc phù hợp/không phù hợp.
- Claim IDs: P6-C04, P6-C05.

### 4. CRT
- Mất đồng bộ điện–cơ, tái đồng bộ thất, reverse remodeling.
- Phân biệt Cardiac Resynchronization Therapy với capillary refill time.
- Tiêu chuẩn mạnh, chống chỉ định narrow QRS, CRT-P/CRT-D theo quyết định đa ngành.
- Claim IDs: P6-C06, P6-C07.

### 5. Functional valve disease
- Secondary MR/TR là hậu quả hình học buồng tim; đánh giá sau GDMT/CRT.
- Heart Team, giải phẫu, nguy cơ thủ thuật, mục tiêu người bệnh.
- Claim IDs: P6-C08.

### 6. LVAD
- Pump hỗ trợ thất trái; bridge to transplant, bridge to candidacy/decision, destination therapy.
- Chọn bệnh nhân, caregiver, anticoagulation capacity, rehabilitation.
- Biến chứng định tính: chảy máu, huyết khối bơm, đột quỵ, nhiễm driveline, suy thất phải, loạn nhịp, hở van động mạch chủ, mất điện/controller.
- Claim IDs: P6-C09.

### 7. Ghép tim
- Đánh giá tim, cơ quan đích, ung thư/nhiễm trùng, tâm lý–xã hội, tuân thủ, caregiver.
- Biên chống chỉ định là quyết định trung tâm; phân biệt reversible vs irreversible.
- Claim IDs: P6-C10.

### 8. Chăm sóc giảm nhẹ và bất hoạt ICD
- Palliative song song điều trị kéo dài sống; giao tiếp prognosis; advance care planning.
- Bất hoạt chức năng shock không đồng nghĩa tắt pacing và không phải trợ tử.
- Claim IDs: P6-C11, P6-C12.

### 9. Quản lý dài hạn
- Cardiac rehabilitation, tiêm chủng theo lịch hiện hành, tự theo dõi, follow-up, remote monitoring có giới hạn.
- Claim IDs: P6-C13, P6-C14, P6-C15.

### 10. Flowchart ASCII, safety boxes, Plan A/Plan B, common traps
- Nhánh cấp cứu dừng ngoại trú và sang Part 5.
- Nhánh thiết bị, van, advanced therapy, palliative.

### 11. Đúng năm ca lâm sàng có lời giải
1. ICD candidate.
2. CRT candidate, giải nghĩa CRT.
3. Valve referral.
4. Advanced HF for LVAD/transplant.
5. Palliative/rehab/self-monitoring.

Mỗi ca bắt buộc đúng năm heading: `Red flag`; `Dữ kiện quyết định`; `Hành động`; `Monitoring/chuyển tuyến`; `Why alternatives wrong`.

### 12. Coverage target
- Ít nhất 10 section, 14 subsection, 4 reasoning chains năm tầng, 8 ví dụ, 8 bẫy, 5 checkpoint, 12 practical tips, đúng 5 ca.
- Bài học mục tiêu 10.000–14.000 từ thực tế; không padding.

## 6. Hướng dẫn model execute

1. Chỉ dùng claim P6-C01 đến P6-C15; giữ `{claim:P6-Cxx}`, `[GUIDELINE VERIFIED]` và `[PMID: 35363499]` cùng dòng với occurrence được trích.
2. Kiến thức sinh lý, khái niệm consensus và giải thích cơ chế không gắn nhãn.
3. Không thêm định lượng ngoài claim registry.
4. Viết tiếng Việt có dấu; tiếng Việt trước, tiếng Anh trong ngoặc ở lần đầu.
5. Không Mermaid; flowchart chỉ `text` ASCII; không bảng Markdown từ bốn cột trở lên.
6. Chỉ nhắc ICU decongestion/shock như red flag và cross-reference Part 5.
7. Safety boxes phải nói dấu hiệu → nguy cơ → hành động → nơi chuyển.
8. Mỗi quyết định có Plan A và Plan B khi nguồn lực hạn chế.
9. Đúng năm case và đủ đúng năm heading mỗi case.
10. Không tạo cards, APKG, DOCX hoặc knowledge check trong writing pass này.