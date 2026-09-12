# RESEARCH BRIEF: IM-07 — Tiếp cận bệnh nhân khó thở cấp và suy hô hấp

**Ngày:** 2026-07-22  
**Research:** GPT-5.6 Terra  
**Execute:** GPT-5.6 Terra  
**Trạng thái:** Candidate đã khóa phạm vi, claims và release contract.

---

## 0. Lesson profile & release contract

```json
{
  "profile": "disease",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "depth_disease",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "learner_smoke"
  ],
  "not_applicable": [],
  "approved_exemptions": []
}
```

## 1. Khóa phạm vi

**Bài này là bài tiếp cận hội chứng trong 0–15 phút đầu.** Đích không phải chẩn đoán hoàn chỉnh mọi nguyên nhân, mà là đưa người bệnh đến đúng mức hỗ trợ hô hấp và nơi điều trị an toàn.

### Bài giải quyết

- Có dấu hiệu đe dọa đường thở, hô hấp, tuần hoàn hoặc tri giác không?
- Thất bại oxy hóa, thất bại thông khí, hay hỗn hợp?
- Cần oxy mục tiêu, HFNO, CPAP/BiPAP/NIV, hay gọi đội đặt nội khí quản/ICU ngay?
- Trong lúc ổn định, nguyên nhân nguy hiểm nào phải nhận diện: tắc nghẽn đường thở, hen/COPD, phù phổi cấp, viêm phổi, PE, tràn khí màng phổi áp lực, chèn ép tim, toan chuyển hóa/ngộ độc?

### Bài không giải quyết

Không viết protocol điều trị hoàn chỉnh cho COPD/hen/viêm phổi/suy tim/PE/tràn khí, kỹ thuật đặt nội khí quản, hay cài đặt máy thở xâm nhập. Các nội dung đó sẽ thuộc IM-22, IM-29–34, IM-93 và các bài cấp cứu liên quan.

---

## 2. Tier 0 — guideline đã kiểm chứng

| Nguồn | Phạm vi được phép dùng | Trạng thái |
|---|---|---|
| **SFMU/SRLF 2026** — *Guidelines for the Initial Assessment of Respiratory Distress in the Emergency Department*, PMID **41788490** | Dấu hiệu nặng, triage/theo dõi, định nghĩa oxy hóa–thông khí, chọn khí máu, chiến lược chẩn đoán và nơi chăm sóc | `[GUIDELINE VERIFIED]` |
| **AARC 2022** — *Management of Adult Patients With Oxygen in the Acute Care Setting*, PMID **34728574** | Oxy được kê đơn theo đích và đánh giá lại trong acute care | `[GUIDELINE VERIFIED]` |
| **ERS/ATS 2017** — *Noninvasive ventilation for acute respiratory failure*, PMID **28860265** | NIV theo phenotype: COPD có toan hô hấp; CPAP/bilevel NIV trong phù phổi cấp do tim; cần theo dõi sát và rescue xâm nhập | `[GUIDELINE VERIFIED]` |
| **ESICM 2023** — *ARDS respiratory support strategies*, PMID **37326646** | HFNO trong AHRF theo phenotype; giới hạn bằng chứng so sánh HFNO với NIV | `[GUIDELINE VERIFIED]` |
| **BTS/ICS 2016** — *Ventilatory management of acute hypercapnic respiratory failure*, PMID **26976648** | NIV trong suy hô hấp tăng CO₂; SaO₂ 88–92% chỉ trong phenotype đang điều trị NIV này | `[GUIDELINE VERIFIED]` |

**Quyết định registry:** không dùng khuyến cáo BTS oxygen 2017 đã loại vì strict preflight từng bị giới hạn HTTP 429. Không dùng nguồn này để mang oxygen target vào bài.

---

## 3. Evidence đã chọn và lý do chọn

| # | PMID / nguồn | Loại | Vai trò trong bài |
|---|---|---|---|
| 1 | **PMID: 41788490** | Guideline 2026 | Xương sống cho triage, dấu hiệu nặng, khí máu, chẩn đoán định hướng và destination |
| 2 | **PMID: 34728574** | Guideline 2022 | Oxy có đích và đánh giá lại |
| 3 | **PMID: 28860265** | Guideline 2017 | NIV phenotype-specific: COPD toan hô hấp, phù phổi cấp do tim |
| 4 | **PMID: 37326646** | Guideline 2023 | HFNO ở AHRF và giới hạn bằng chứng |
| 5 | **PMID: 26976648** | Guideline 2016 | Suy hô hấp tăng CO₂/NIV, controlled target khi đang NIV |
| 6 | **PMID: 25981908** | RCT FLORALI | Bằng chứng phenotype-limited cho HFNO |
| 7 | **PMID: 7651472** | RCT | Bằng chứng nền NIV ở COPD chọn lọc |
| 8 | **PMID: 18614781** | RCT 3CPO | Đáp ứng sớm với NIV ở phù phổi cấp do tim |
| 9 | **PMID: 32496521** | Systematic review/network meta-analysis | Bất định và heterogeneity của các chiến lược oxy hóa không xâm nhập |
| 10 | **PMID: 35504747** | Meta-analysis | LUS so với X-quang trong phù phổi cấp do tim |
| 11 | **PMID: 27481760** | Prospective cohort | ROX trong pneumonia/HFNC/12 giờ |
| 12 | **PMID: 37266791** | Clinical review | Nền tảng dyspnea, respiratory distress và khung chẩn đoán |
| 13 | **NBK526127** | NCBI Bookshelf | Nền sinh lý type 1/type 2, V/Q mismatch, shunt và hypoventilation |

---

## 4. Claims đã verify — được phép dùng

> Chỉ các claim trong mục này được phép đưa vào MD/cards. Số liệu phải giữ nguyên ý nghĩa, PMID sát claim và tag đúng mức.

### A. Nhận diện nặng và triage

| Claim được phép dùng | Nguồn | Tag |
|---|---|---|
| Dấu hiệu cần chủ động tìm khi respiratory distress gồm RR >25/phút, không nói được câu trọn, cyanosis ngoại vi, vã mồ hôi, bất đồng bộ ngực–bụng và thay đổi tri giác. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| RR >25/phút liên quan nguy cơ intubation, ICU admission và tử vong nội viện cao hơn; altered consciousness, thở bụng nghịch thường và dùng cơ hô hấp phụ cũng là dấu hiệu tiên lượng xấu. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Bệnh nhân có severity criteria cần continuous monitoring: BP, HR, RR, nhiệt độ, tri giác và SpO₂; RR nên được đo ít nhất 30 giây khi tiếp nhận. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Cân nhắc ICU cho bệnh nhân đang NIV, cần oxygen flow cao kéo dài, hoặc có thêm suy cơ quan ngoài hô hấp; invasive ventilation là chỉ định direct ICU. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |

### B. Định nghĩa và sinh lý bệnh

| Claim được phép dùng | Nguồn | Tag |
|---|---|---|
| Acute respiratory failure là thất bại trao đổi khí; SFMU/SRLF định nghĩa hypoxemia là PaO₂ <60 mmHg hoặc SpO₂ <90% khi thở khí phòng, hoặc PaO₂/FiO₂ <300 khi đang oxy; hypercapnia là PaCO₂ >45 mmHg, có hoặc không acidemia. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Type 1 predominates hypoxemia; type 2 includes hypercapnia and thường liên quan thất bại bơm hô hấp/hypoventilation. | NBK526127 | `[TEXTBOOK VERIFIED]` |
| V/Q mismatch là cơ chế thường gặp của type 1; shunt thật (ví dụ severe pneumonia, pulmonary edema, atelectasis) đáp ứng kém với supplemental oxygen hơn V/Q mismatch. | NBK526127 | `[TEXTBOOK VERIFIED]` |
| Hypercapnic failure xuất hiện khi alveolar ventilation không đủ so với CO₂ production; “won't breathe” (central drive) và “can't breathe” (neuromuscular, chest wall, resistive/restrictive load) là khung giải thích hữu ích. | NBK526127 | `[TEXTBOOK VERIFIED]` |

### C. SpO₂, khí máu và oxy mục tiêu

| Claim được phép dùng | Nguồn | Tag |
|---|---|---|
| SpO₂ là theo dõi oxy hóa, không đo PaCO₂ hoặc pH; VBG không dùng để đánh giá mức hypoxemia. ABG hỗ trợ khi cần định lượng hypercapnia–respiratory acidosis, xác nhận cần hỗ trợ thông khí hoặc quyết định nơi chăm sóc. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Oxy là một can thiệp phải được kê đơn theo khoảng đích và đánh giá lại; ở người có nguy cơ suy hô hấp tăng CO₂, dùng đích thấp hơn có kiểm soát thay vì mặc định oxy tối đa. | AARC 2022 và SFMU/SRLF 2026, PMID 34728574; PMID 41788490 | `[GUIDELINE VERIFIED]` |
| SaO₂ 88–92% được phép nêu chỉ cho người suy hô hấp tăng CO₂ đang điều trị NIV, không dùng như mục tiêu chung. | BTS/ICS 2016, PMID 26976648 | `[GUIDELINE VERIFIED]` |

### D. HFNO, NIV và escalation

| Claim được phép dùng | Nguồn | Tag |
|---|---|---|
| Ở non-mechanically ventilated AHRF **không do acute COPD exacerbation hoặc cardiogenic pulmonary edema**, ESICM khuyến cáo HFNO thay conventional oxygen để giảm intubation; không đưa được khuyến cáo mortality benefit. | ESICM 2023, PMID 37326646 | `[GUIDELINE VERIFIED]` |
| ESICM không thể khuyến cáo HFNO hay CPAP/NIV hơn phương án còn lại cho unselected AHRF không do COPD/CPE, do evidence không đủ; chọn theo phenotype, tolerance, expertise, monitoring và khả năng intubate rescue. | ESICM 2023, PMID 37326646 | `[GUIDELINE VERIFIED]` |
| ERS/ATS khuyến cáo bilevel NIV cho acute hoặc acute-on-chronic respiratory acidosis do COPD exacerbation; một trial NIV cần monitoring sát và rapid access to intubation nếu không cải thiện. | ERS/ATS 2017, PMID 28860265 | `[GUIDELINE VERIFIED]` |
| ERS/ATS khuyến cáo CPAP hoặc bilevel NIV ở acute respiratory failure do cardiogenic pulmonary edema; kết luận này không áp dụng mặc định cho cardiogenic shock/acute coronary syndrome. | ERS/ATS 2017, PMID 28860265 | `[GUIDELINE VERIFIED]` |
| Với COPD respiratory acidosis, pH hoặc RR phải cải thiện sớm mới gợi ý NIV success; guideline mô tả đáp ứng thường thấy trong 1–4 giờ. | ERS/ATS 2017, PMID 28860265 | `[ABSTRACT/FULLTEXT VERIFIED]` |
| FLORALI: ở 310 bệnh nhân nonhypercapnic AHRF với PaO₂/FiO₂ ≤300, intubation day 28 không khác biệt có ý nghĩa; 90-day mortality thấp hơn ở HFNO so với oxygen chuẩn hoặc NIV trong trial này. | PMID 25981908 | `[FULL VERIFIED]` |
| RCT COPD chọn lọc: NIV giảm intubation, complications, length of stay và in-hospital mortality so với standard treatment; không ngoại suy thành chỉ định NIV cho mọi dyspnea. | PMID 7651472 | `[FULL VERIFIED]` |
| 3CPO: NIV trong CPE cải thiện dyspnea, HR, acidosis và hypercapnia sớm hơn standard oxygen, nhưng không khác 7-day mortality trong trial; ERS/ATS recommendation dựa trên tổng hợp toàn bộ evidence. | PMID 18614781 | `[FULL VERIFIED]` |
| ROX = (SpO₂/FiO₂)/RR. Trong cohort pneumonia on HFNC, ROX ≥4.88 tại 12 giờ liên quan risk mechanical ventilation thấp hơn; đây là **risk aid**, không phải điều kiện để trì hoãn ICU/intubation khi clinical deterioration. | PMID 27481760 | `[FULL VERIFIED]` |

### E. Chẩn đoán định hướng

| Claim được phép dùng | Nguồn | Tag |
|---|---|---|
| Ở very low pre-test suspicion PE, PERC có thể loại trừ PE không cần test thêm; với suspected PE, YEARS hoặc PEGeD được SFMU/SRLF ưu tiên hơn một số pathway cổ điển để giảm test không cần thiết. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| BNP/NT-proBNP giúp rule out acute heart failure khi diễn giải cùng clinical context; obesity và renal function ảnh hưởng interpretation. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Integrated cardiac and lung ultrasound hỗ trợ tìm nguyên nhân acute dyspnea; không dùng cardio-pulmonary ultrasound để rule in/rule out PE ở bệnh nhân không sốc. | SFMU/SRLF 2026, PMID 41788490 | `[GUIDELINE VERIFIED]` |
| Meta-analysis trong suspected ADHF: LUS nhạy và đặc hiệu hơn CXR cho cardiogenic pulmonary edema (91.8% vs 76.5%; 92.3% vs 87.0%). | PMID 35504747 | `[FULL VERIFIED]` |

---

## 5. Claims / protocol details CẤM dùng ở vòng execute

1. Bất kỳ flow/threshold intubation đơn lẻ kiểu “SpO₂ X thì phải intubate”; quyết định phải dựa trajectory, công thở, tri giác, huyết động, khí máu và khả năng rescue.
2. Liều thuốc (bronchodilator, nitrate, diuretic, antibiotic, anticoagulant, steroid), dịch, vasopressor hoặc intubation drugs — ngoài scope hoặc chưa verify.
3. Thông số khởi đầu/titration NIV/HFNO, trừ khi chọn một local protocol đã được user xác nhận và fetch bản gốc. BTS appendix đã đọc là **QI/local algorithm**, không tự áp thành universal protocol Việt Nam.
4. Dùng ROX cutoff ở admission, hoặc ngoài pneumonia/HFNC context, như một rule quyết định tuyệt đối.
5. Dùng POCUS để loại trừ PE ở người ổn định.
6. Khẳng định HFNO/NIV làm giảm mortality ở mọi AHRF hoặc thay thế intubation.
7. Coi anxiety là chẩn đoán cuối cùng trước khi đã đánh giá red flags/căn nguyên tim phổi–chuyển hóa.

---

## 6. Dàn ý execute đã gắn nguồn

### Section 0 — Tổng quan

- Khó thở là complaint, respiratory distress là observable syndrome, acute respiratory failure là biological failure. [41788490]
- Mục tiêu: stability → physiology → support → cause → destination.
- Prerequisite: IM-01–IM-06; vì chưa tồn tại nên nhắc ngắn ABCDE/ABG/ECG/X-ray.

### Section 1 — Nhận diện nguy kịch [CỐT LÕI]

- Red flags và RR >25. [41788490]
- “Không nói được câu + tri giác thay đổi + paradoxical breathing” quan trọng hơn một SpO₂ đơn lẻ.
- Checkpoint: phân biệt distressed-but-compensating và fatigue/impending arrest.

### Section 2 — ABCDE 0–15 phút [CỐT LÕI]

- A: stridor/airway obstruction.
- B: work of breathing, RR, SpO₂, auscultation, oxygen/support.
- C/D/E: shock, ACS, sepsis, metabolic/toxic cause.
- Monitor and reassess based on severity. [41788490]
- **Flowchart 1:** stability-first acute dyspnea.

### Section 3 — Oxy hóa vs thông khí [CỐT LÕI]

- Type 1/2, V/Q/shunt/pump failure. [NBK526127; 41788490]
- Table: clinical clue → gas-exchange problem → likely patterns → immediate next observation/test.
- SpO₂/VBG/ABG đúng việc. [41788490]

### Section 4 — Oxy và respiratory support [CỐT LÕI]

- Oxy có đích: kê đơn khoảng đích và đánh giá lại; nếu có nguy cơ suy hô hấp tăng CO₂, dùng đích thấp hơn có kiểm soát thay vì mặc định oxy tối đa. Chỉ nêu SaO₂ 88–92% cho phenotype suy hô hấp tăng CO₂ đang điều trị NIV. [34728574; 41788490; 26976648]
- HFNO: phenotype and limitation. [37326646]
- NIV: COPD acidotic vs CPE; not default in de novo hypoxemia. [28860265]
- **Escalation box:** lost airway protection, respiratory arrest, shock/unstable arrhythmia, secretion burden, poor cooperation, progressive exhaustion, or unavailable immediate invasive rescue → do not prolong noninvasive trial.
- **Flowchart 2:** oxygen → HFNO/NIV phenotype → reassessment → ICU/intubation.

### Section 5 — Dangerous causes by pattern [CỐT LÕI]

- Obstructive; parenchymal; cardiac/vascular/pleural; metabolic/toxic.
- No “shotgun tests”: test answers a question.
- PE pathway, BNP, integrated LUS/cardiac POCUS and limits. [41788490; 35504747]

### Section 6 — Disposition/bàn giao [CỐT LÕI]

- Continuous monitoring/ICU criteria. [41788490]
- SBAR handoff: baseline, timeline, device/FiO₂/SpO₂, RR/work, ABG, working diagnosis, treatment/response, ceiling of care.

### Sections 7–10 — lỗi, Việt Nam, cases, tổng kết

- 6 errors from the above claims.
- Vietnam section limited to resource-aware escalation/transfer and does not claim a national protocol until verified.
- Four cases: acidotic COPD, CPE, hypoxemic pneumonia, PE/tension pneumothorax phenotype.
- 10 takeaways and end-of-lesson integration test.

---

## 7. Cards brief

**Chính xác 36 notes V2: 30 `basic` và 6 `cloze`.**

- 8: red flags/ABCDE/reassessment.
- 7: physiology, SpO₂–VBG–ABG.
- 8: oxygen/HFNO/NIV/escalation.
- 6: diagnostic patterns và POCUS limits.
- 7: mini-cases/disposition decisions.

Mỗi cloze có đúng một `{{c1::...}}`; do đó deck tạo chính xác 36 cards.

Không tạo card cho dose/setting chưa được verify. Mỗi card bảo vệ một decision node observable.

---

## 8. Quyết định đã chốt trước execute

1. Không tìm được guideline Việt Nam/local hiện hành đã xác minh cho flow HFNO, NIV settings hoặc protocol chuyển viện; vì vậy không đưa flow thiết bị, áp lực, titration, liều thuốc, ngưỡng đặt nội khí quản đơn lẻ, hay khẳng định protocol quốc gia vào IM-07.
2. Citation snowball không phải điều kiện phát hành: 12 PMID giữ lại đã vượt ngưỡng disease tối thiểu 10 PMID. Nguồn mới chỉ được thay thế khi trực tiếp hơn và được verify đầy đủ.
3. Nếu strict preflight không lấy được một nguồn không load-bearing từ PubMed, Europe PMC và PMC, phải bỏ nguồn cùng mọi claim phụ thuộc; không đổi WARN thành PASS. PMID 41788490 và PMCID PMC12934415 là load-bearing bắt buộc.
