---
profile: "disease"
lesson_depth_contract: "L3_BEGINNER"
output_basename: "IM-22_P5_Suy_tim_cap_2026-07-30_RELEASE_v1"
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

# Research Brief: Suy tim cấp

## 0.1 Release acceptance — IM-22 Part 5 remediation lock

- `release_acceptance.min_actual_words`: 10000
- `release_acceptance.max_actual_words`: 14000
- `release_acceptance.exact_case_count`: 5
- `release_acceptance.observed_actual_words`: 12684
- `release_acceptance.observed_case_count`: 5
- Contract JSON above remains the canonical executable `disease` profile required by `publish_gate.py`; this stricter remediation acceptance is additive and cannot lower the executable gates.

## 1. Phạm vi và preflight guideline

- **Đối tượng:** bác sĩ, học viên sau đại học và người học mất gốc; bài dạy mức `L3_BEGINNER`.
- **Basename khóa:** `IM-22_P5_Suy_tim_cap_2026-07-30_RELEASE_v1`.
- **Phạm vi được phép:** nền tảng huyết động cấp; hồ sơ ấm/lạnh và ướt/khô; SCAPE; CHAMPIT; ABCDE; oxy và NIV; lợi tiểu quai tĩnh mạch, đánh giá sớm bằng natri niệu và lượng nước tiểu, phong bế nephron tuần tự; giãn mạch; sốc tim, tăng co bóp và vận mạch; monitoring; chuyển sang thuốc uống và khởi động lại GDMT.
- **Ngoài phạm vi:** chỉ định chi tiết LVAD, ghép tim, hỗ trợ tuần hoàn cơ học dài hạn hoặc chăm sóc suy tim tiến triển; nội dung này dành cho Part 6.
- **Nguồn official current đã khóa:** AHA/ACC/HFSA 2022. Không phát hiện tài liệu chính thức trong bundle tuyên bố nguồn này bị superseded đối với phạm vi suy tim cấp.
- **Evidence bundle:** `outputs/IM-22_P5_Suy_tim_cap_2026-07-30_RELEASE_v1_evidence_bundle.json`, tạo bởi canonical `evidence_sync.py` từ Europe PMC, OpenAlex, Crossref/Retraction Watch và official-source manifest.
- **Guideline evidence:** `outputs/IM-22_P5_Suy_tim_cap_2026-07-30_RELEASE_v1_guideline_evidence.json`.

## 2. Papers đã chọn

- **PMID 35363499:** AHA/ACC/HFSA 2022; nguồn official cho phân tầng sung huyết–tưới máu, yếu tố thúc đẩy, lợi tiểu, giãn mạch và chuyển tiếp.
- **PMID 36027559:** ADVOR; hỗ trợ acetazolamide phối hợp lợi tiểu quai trong quá tải thể tích.
- **PMID 21366472:** DOSE; hỗ trợ so sánh bolus/truyền liên tục và chiến lược liều cao/thấp.


**Papers/identifiers loại:** Hai định danh sai trong stub cũ trỏ lần lượt đến DELIVER và một ca niêm mạc dạ dày lạc chỗ ở thực quản, không phải ADVOR/EMPULSE. Chúng đã bị loại hoàn toàn khỏi tập nguồn khóa, lesson và bundle.

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| P5-C01 | Đánh giá mức sung huyết và mức tưới máu ở người bệnh nhập viện vì suy tim để định hướng phân luồng và điều trị ban đầu. | 35363499 | [GUIDELINE VERIFIED] | In patients hospitalized with HF, severity of congestion and adequacy of perfusion should be assessed to guide triage and initial therapy (1-5). | Người bệnh nhập viện vì suy tim | Đánh giá sung huyết và tưới máu | Phân luồng và điều trị ban đầu phù hợp | Khi nhập viện |
| P5-C02 | Đánh giá yếu tố thúc đẩy thường gặp và quỹ đạo bệnh để định hướng điều trị. | 35363499 | [GUIDELINE VERIFIED] | In patients hospitalized with HF, the common precipitating factors and the overall patient trajectory should be assessed to guide appropriate therapy (5,6). | Người bệnh nhập viện vì suy tim | Đánh giá yếu tố thúc đẩy và quỹ đạo | Điều trị phù hợp nguyên nhân | Trong đánh giá ban đầu |
| P5-C03 | Quá tải dịch đáng kể cần được điều trị sớm bằng lợi tiểu quai tĩnh mạch. | 35363499 | [GUIDELINE VERIFIED] | Patients with HF admitted with evidence of signiﬁcant ﬂuid overload should be promptly treated with intravenous loop diuretics to improve symptoms and reduce morbidity (1). | Người bệnh nhập viện có quá tải dịch đáng kể | Lợi tiểu quai tĩnh mạch | Cải thiện triệu chứng và giảm gánh bệnh | Sớm trong nhập viện |
| P5-C04 | Nếu bài niệu không đủ, tăng cường bằng liều lợi tiểu quai tĩnh mạch cao hơn hoặc thêm lợi tiểu thứ hai là hợp lý. | 35363499 | [GUIDELINE VERIFIED] | In patients hospitalized with HF when diuresis is inadequate to relieve symptoms and signs of congestion, it is reasonable to intensify the diuretic regimen using either: a. higher doses of intravenous loop diuretics (1,3); or b. addition of a second diuretic (3). | Người bệnh nhập viện còn sung huyết và bài niệu không đủ | Tăng liều loop hoặc thêm lợi tiểu thứ hai | Tăng giảm sung huyết | Khi đáp ứng ban đầu không đủ |
| P5-C05 | Khi không tụt huyết áp hệ thống, nitroglycerin hoặc nitroprusside tĩnh mạch có thể được cân nhắc bổ trợ lợi tiểu để giảm khó thở. | 35363499 | [GUIDELINE VERIFIED] | In patients who are admitted with decompensated HF, in the absence of systemic hypotension, intra- venous nitroglycerin or nitroprusside may be considered as an adjuvant to diuretic therapy for relief of dyspnea (1,2). | Người bệnh nhập viện vì suy tim mất bù không tụt huyết áp hệ thống | Nitroglycerin hoặc nitroprusside tĩnh mạch bổ trợ lợi tiểu | Giảm khó thở | Trong giai đoạn cấp |
| P5-C07 | Trước xuất viện cần hướng dẫn lấy người bệnh làm trung tâm kèm kế hoạch chuyển tiếp rõ ràng. | 35363499 | [GUIDELINE VERIFIED] | In patients hospitalized with worsening HF, patient-centered discharge instructions with a clear plan for transitional care should be provided before hospital discharge (5,6). | Người bệnh nằm viện vì suy tim nặng lên | Hướng dẫn và kế hoạch chuyển tiếp | Chuyển chăm sóc an toàn | Trước xuất viện |
| P5-C10 | Thêm acetazolamide vào lợi tiểu quai làm tăng khả năng giảm sung huyết thành công ở suy tim mất bù cấp có quá tải thể tích. | 36027559 | [ABSTRACT VERIFIED] | The addition of acetazolamide to loop diuretic therapy in patients with acute decompensated heart failure resulted in a greater incidence of successful decongestion. | Suy tim mất bù cấp có quá tải thể tích | Acetazolamide cộng loop so với giả dược cộng loop | Giảm sung huyết thành công | Trong đợt nằm viện |
| P5-C11 | Trong DOSE, không có khác biệt có ý nghĩa về đánh giá triệu chứng toàn thể hoặc thay đổi chức năng thận giữa bolus và truyền liên tục, hay giữa chiến lược liều cao và liều thấp. | 21366472 | [ABSTRACT VERIFIED] | Among patients with acute decompensated heart failure, there were no significant differences in patients' global assessment of symptoms or in the change in renal function when diuretic therapy was administered by bolus as compared with continuous infusion or at a high dose as compared with a low dose. | Suy tim mất bù cấp | Bolus so với truyền liên tục; liều cao so với liều thấp | Triệu chứng toàn thể và thay đổi chức năng thận | Trong đợt điều trị thử nghiệm |

## 4. Claims và số liệu cấm dùng

- Không khóa liều truyền nitroglycerin, nitroprusside, norepinephrine, dobutamine hoặc milrinone; lesson yêu cầu theo protocol ICU địa phương và dược sĩ lâm sàng.
- Không dùng lại hai định danh sai của ADVOR và EMPULSE trong stub cũ.
- Không dùng tỷ lệ ấm–ướt, tử vong sốc tim, lợi ích định lượng của NIV, hoặc ngưỡng SpO2 mục tiêu vì chưa có artifact đủ tier cho claim định lượng trong bundle này.
- Không dùng ngưỡng natri niệu, mục tiêu mL/giờ hoặc con số cân nặng làm mệnh lệnh phổ quát. Lesson dạy lấy mẫu sớm và đánh giá xu hướng/đủ–không đủ; protocol định lượng theo cơ sở.
- Không dùng acetazolamide như mặc định cho mọi người bệnh; chỉ giải thích lựa chọn phối hợp ở quá tải thể tích sau khi kiểm tra chống chỉ định và điện giải.
- Không mô tả LVAD, ECMO, IABP, Impella hay ghép tim ngoài việc chuyển sớm đến trung tâm có khả năng hỗ trợ tuần hoàn khi thuốc không duy trì được cơ quan.

## 5. Dàn ý chi tiết

- Nền tảng: cung lượng tim, tiền tải, hậu tải, áp lực đổ đầy, tái phân bố dịch, sung huyết và tưới máu.
- Phân tầng ấm/lạnh–ướt/khô; SCAPE; không đồng nhất cold-wet với mọi tụt huyết áp.
- CHAMPIT và nguyên tắc điều trị song song yếu tố thúc đẩy.
- ABCDE; oxy theo tình trạng thiếu oxy, NIV khi suy hô hấp phù hợp; chống chỉ định và Plan B.
- Giảm sung huyết: loop IV, lấy natri niệu sớm và theo dõi lượng nước tiểu, tăng cường liều, phong bế nephron tuần tự, acetazolamide, thiazide, siêu lọc chỉ sau hội chẩn.
- Giãn mạch ở người không tụt huyết áp, đặc biệt tăng huyết áp/phù phổi; không dùng trong giảm tưới máu.
- Sốc tim: nhận diện cơ quan đích, siêu âm/ECG, tăng co bóp, vận mạch theo protocol ICU, shock team và chuyển tuyến.
- Monitoring theo vấn đề; Plan A đầy đủ nguồn lực và Plan B thiếu nguồn lực.
- Chuyển thuốc uống, đánh giá sung huyết, tiếp tục/giữ/khởi động lại GDMT dựa trên huyết động–thận–điện giải.
- Đúng năm ca: SCAPE/ấm–ướt; đáp ứng lợi tiểu kém; lạnh–ướt sốc; ACS/rối loạn nhịp; chuyển tiếp xuất viện. Mỗi ca dùng đúng năm heading hợp đồng.

## 6. Hướng dẫn model execute

1. Viết 10.000–14.000 từ thực tế, tiếng Việt có dấu, L3_BEGINNER, không lặp ý để đủ số lượng.
2. Chỉ dùng các claim đã khóa P5-C01 đến P5-C05, P5-C07, P5-C10 và P5-C11; mỗi occurrence có `{claim:P5-Cxx}`, nhãn canonical và PMID gần nhau. Các claim P5-C06, P5-C08, P5-C09, P5-C12 và P5-C13 được chủ động loại khỏi prose gắn nhãn vì artifact hiện có không đủ để vượt mọi kiểm tra claim/citation offline mà không tạo WARN hoặc BLOCK.
3. Kiến thức sinh lý ổn định viết không nhãn; mọi liều, ngưỡng, timing định lượng ngoài claim khóa phải bỏ hoặc chuyển thành yêu cầu theo protocol địa phương.
4. Flowchart chỉ dùng ASCII trong khối `text`; không Mermaid; không bảng từ bốn cột.
5. Đúng năm ca và đúng các heading: `Red flag`, `Dữ kiện quyết định`, `Hành động`, `Monitoring/chuyển tuyến`, `Why alternatives wrong`.
6. Không dạy kỹ thuật hỗ trợ tuần hoàn cơ học hoặc nội dung ghép/LVAD dành cho Part 6.
