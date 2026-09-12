# RESEARCH BRIEF: IM-43 · Đọc creatinine/eGFR và tiếp cận tổn thương thận cấp
**Ngày khóa research:** 2026-07-22 | **Revision:** RELEASE v1 | **Model research:** Terra | **Model execute:** Terra

---

## 0. Lesson profile & release contract

Contract này được khóa trước khi viết bài. Bài là bài lâm sàng về đánh giá và xử trí an toàn tổn thương thận cấp (acute kidney injury, AKI), vì vậy dùng profile `disease`.

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

## 1. Tier 0 guideline proof and freshness record

**Đã truy cập ngày 2026-07-22:**

| Nguồn chính thức | Trạng thái đã quan sát | Cách dùng trong bài |
|---|---|---|
| KDIGO AKI/AKD: https://kdigo.org/guidelines/acute-kidney-injury/ | KDIGO ghi rõ tài liệu 2026 AKI/AKD đang là *public review draft*, chưa phải guideline cuối cùng. | Không dùng wording/recommendation của draft như hướng dẫn chính thức. Dùng KDIGO 2012 final cho định nghĩa/staging và nguồn tóm tắt Kellum et al. |
| NICE NG148: https://www.nice.org.uk/guidance/ng148/chapter/Recommendations | NICE NG148, published 18-12-2019; last updated 16-10-2024. | Dùng cho nguyên tắc tìm AKI khi bệnh cấp, so baseline, rà thuốc/nguy cơ, theo dõi thiểu niệu, chuyển chuyên khoa. |
| NIDDK adult eGFR: https://www.niddk.nih.gov/health-information/professionals/clinical-tools-patient-management/kidney-disease/laboratory-evaluation/estimated-gfr-calculators | Last reviewed May 2024; eGFR là estimate, công thức race-free được NIDDK hỗ trợ; creatinine–cystatin C kết hợp chính xác hơn trong một số quyết định ở người ổn định. | Dùng để giải thích eGFR là ước tính, không thay thế trend/lâm sàng khi creatinine đang biến đổi. |

**Kết quả preflight guideline đã chạy:**

- `KDIGO 2012 AKI`: **BLOCK** vì registry map nhầm chủ đề sang ACG acute diarrhea 2016; không phải bằng chứng chống lại KDIGO. Đã tái đọc nguồn KDIGO chính thức và xác nhận 2026 vẫn là draft.
- `KDIGO 2026 AKI/AKD`: **WARN** do registry map sai/stale; chỉ ghi nhận trạng thái draft, không dùng làm final source.
- `NICE NG148 2024 update`: **WARN** do registry map sai/stale; đã tái đọc trang NICE chính thức.

Không sửa `guideline_versions.json`. Các WARN/BLOCK registry này là bằng chứng registry không có key AKI đúng, không thay thế Tier 0 content review.

## 2. Papers đã chọn và khóa nguồn

| # | PMID | Loại | Vai trò đã xác nhận từ title + abstract |
|---|---|---|---|
| 1 | PMID: 22890468 | Guideline article | KDIGO 2012 AKI final guideline article; nguồn formal definition/staging. |
| 2 | PMID: 23394211 | Guideline summary/review | Tóm tắt KDIGO: definition, staging, evaluation, prevention và non-dialytic management. |
| 3 | PMID: 28239173 | ADQI consensus | Phân biệt AKI, AKD và CKD; AKI là thay đổi cấp, CKD cần kéo dài. |
| 4 | PMID: 25314242 | Review | AKI classification dựa vào creatinine và urine output; mỗi chỉ số có giới hạn; urinalysis/microscopy là công cụ bổ sung. |
| 5 | PMID: 26410133 | Review | Tiêu chuẩn AKI là thay đổi creatinine, urine output hoặc cả hai; dùng cả hai cải thiện nhận diện nguy cơ. |
| 6 | PMID: 18784207 | Observational diagnostic study | Urine sediment/microscopy hỗ trợ phân biệt ATN với pre-renal AKI trong bối cảnh phù hợp, không thay thế pretest probability. |
| 7 | PMID: 27169556 | Review | Ultrasound an toàn, lặp lại được; hỗ trợ đánh giá anatomy, urinary obstruction và AKI/CKD distinction. |
| 8 | PMID: 33752857 | Review | Nephrotoxin stewardship là quy trình dùng thuốc an toàn có cấu trúc; giảm sai sót/tổn hại do thuốc và hỗ trợ phòng drug-associated AKI. |
| 9 | PMID: 23265596 | Review | Hypotension/hypovolemia có thể gây hoặc làm nặng AKI; cần chú ý hemodynamics nhưng fluid overload liên quan kết cục xấu hơn. |
| 10 | PMID: 32668114 | Multicentre RCT | STARRT-AKI: accelerated KRT strategy không giảm tử vong 90 ngày so với standard strategy ở critically ill severe AKI. |
| 11 | PMID: 22113526 | Systematic review/meta-analysis | AKI liên quan nguy cơ dài hạn CKD, ESKD và tử vong; cần follow-up recovery/kidney risk. |
| 12 | PMID: 30473140 | Systematic review/meta-analysis | Meta-analysis cohort dùng consensus AKI definitions, đánh giá liên hệ AKI với CKD, ESKD và death dài hạn. |
| 13 | PMID: 27647862 | Review | Creatinine/cystatin C-based GFR estimates có quan hệ đáng tin khi steady state; cần hiểu giới hạn ngoài steady state. |
| 14 | PMID: 23062091 | Clinical review | Initial AKI assessment: history/exposure, volume examination, creatinine/electrolytes/urinalysis, imaging khi có nguy cơ obstruction; phân loại pre-renal/intrinsic/post-renal. |

**Đã loại, không đưa vào source lock:**

| Record | Lý do loại |
|---|---|
| `99_Inbox/im43_core_sources.json` | File scratch bị nhiễm PMID không liên quan AKI (cardio-oncology, hematology và chủ đề khác); đã xóa, không rename/comment/reuse. |
| Grep hits trong `abstracts.json` | Chỉ là discovery; một số bài cirrhosis/HRS có chữ AKI incidental, không phải corpus AKI được chọn. |
| Search output BioMCP không có metadata đầy đủ | Rate-limit/PubTator fallback errors; không dùng các result chỉ có ID hoặc warning mà chưa fetch title + abstract. |

## 3. Claims đã verify — phạm vi được phép

Model execute chỉ dùng các claim dưới đây; mọi phát biểu phải giữ định tính trừ khi `FULL VERIFIED` đã ghi rõ.

| # | Claim được phép | Nguồn | Tag |
|---|---|---|---|
| 1 | AKI là hội chứng suy giảm chức năng thận cấp; KDIGO dùng thay đổi creatinine và/hoặc urine output để định nghĩa, phân tầng. | PMID: 23394211; PMID: 26410133; KDIGO 2012 | [GUIDELINE VERIFIED] |
| 2 | Creatinine và urine output đều có giới hạn; một chỉ số đơn lẻ không đủ tự xác định nguyên nhân AKI. | PMID: 25314242; PMID: 26410133 | [ABSTRACT VERIFIED] |
| 3 | eGFR là ước tính từ marker nội sinh; mối quan hệ creatinine/cystatin C với GFR cần trạng thái steady state để diễn giải trực tiếp. | PMID: 27647862; NIDDK May 2024 | [ABSTRACT VERIFIED] |
| 4 | NIDDK hỗ trợ dùng công thức eGFR không race coefficient; đây là công cụ ước tính, không là phép đo trực tiếp. | NIDDK May 2024 | [GUIDELINE VERIFIED] |
| 5 | AKI là thay đổi cấp; CKD đòi hỏi tình trạng thận kéo dài, vì vậy creatinine/eGFR bất thường mới xuất hiện không tự động là CKD. | PMID: 28239173; NICE NG148 | [ABSTRACT VERIFIED] |
| 6 | Initial assessment cần xác nhận/baseline, trend creatinine và urine output, đánh giá perfusion/volume/exposure/medications, xét nghiệm nước tiểu–điện giải và tìm obstruction khi phù hợp. | PMID: 23062091; PMID: 23394211; NICE NG148 | [GUIDELINE VERIFIED] |
| 7 | Urine microscopy có thể hỗ trợ differential diagnosis trong bối cảnh lâm sàng; không tự nó chẩn đoán nguyên nhân AKI. | PMID: 18784207; PMID: 25314242 | [ABSTRACT VERIFIED] |
| 8 | Ultrasound là test an toàn, lặp lại được, hữu ích khi cần đánh giá anatomy/urinary obstruction; kết quả cần gắn risk và clinical context. | PMID: 27169556 | [ABSTRACT VERIFIED] |
| 9 | Thuốc có thể gây/làm nặng AKI; nephrotoxin stewardship đòi hỏi review có cấu trúc thuốc nephrotoxic và renally eliminated, với plan documented thay vì tự ngừng thuốc hàng loạt. | PMID: 33752857; NICE NG148 | [ABSTRACT VERIFIED] |
| 10 | Hypotension và hypovolemia có thể góp phần gây/làm nặng AKI; cần reassess hemodynamics và tránh blind fluid loading vì fluid overload liên quan recovery và mortality xấu hơn. | PMID: 23265596 | [ABSTRACT VERIFIED] |
| 11 | Kidney replacement therapy (KRT) là escalated support cho severe AKI theo conventional indications/specialist protocol; accelerated timing không giảm mortality 90 ngày trong STARRT-AKI. | PMID: 32668114 | [ABSTRACT VERIFIED] |
| 12 | Sau AKI có nguy cơ kidney outcomes dài hạn; recovery, kidney function và risk CKD/ESKD cần follow-up. | PMID: 22113526; PMID: 30473140; PMID: 28239173 | [ABSTRACT VERIFIED] |
| 13 | Hướng tiếp cận etiologic thuận tiện là pre-renal/perfusion, intrinsic kidney và post-renal/obstruction, nhưng classification phải dựa tổng hợp dữ kiện. | PMID: 23062091; PMID: 25314242 | [ABSTRACT VERIFIED] |
| 14 | Safety synthesis: các biểu hiện đe dọa tưới máu, hô hấp, bài niệu, điện giải/acid–base, thần kinh, tắc nghẽn hoặc systemic deterioration cần ưu tiên monitored emergency assessment thay vì outpatient algorithm. | KDIGO 2012; NICE NG148; phạm vi safety synthesis | [DIRECTION ONLY] |

### Số liệu CẤM dùng

- Không viết ngưỡng creatinine, urine-output, stage table, fluid bolus/maintenance volume, vasopressor dose, drug dose, contrast protocol, diuretic dose, dialysis dose/timing, biomarker cutoff, FeNa/FeUrea cutoff hoặc referral cutoff.
- Không đưa số liệu trial/STARRT-AKI, pooled hazard ratio hoặc incidence từ abstracts vào lesson; bài này dùng ý nghĩa định tính để tránh biến evidence review thành protocol.
- Không suy diễn “eGFR changing = drug-dose value”, không tạo phác đồ hold/restart ACEi/ARB/diuretic/NSAID/SGLT2i, và không biến KRT timing thành chỉ định tự thực hiện.

## 4. Kiến thức nền và ranh giới chương trình

| Nội dung nền | Nguồn hoặc liên kết | Giới hạn |
|---|---|---|
| Nephron, filtration, tubular handling, urine formation | Sinh lý nephron RELEASE v2; Guyton and Hall Textbook of Medical Physiology, 14e | Chỉ nhắc đủ để hiểu creatinine, filtration và urine output. |
| Creatinine, GFR/eGFR và steady state | PMID: 27647862; NIDDK May 2024 | Không dạy công thức hay dùng eGFR đang thay đổi để stage CKD. |
| AKI/AKD/CKD boundary | PMID: 28239173 | IM-43 đánh giá acute change trước; IM-44 phụ trách CKD G×A, chronic treatment và dialysis preparation. |
| Medication safety | PMID: 33752857; NICE NG148 | Không có drug-dose protocol; bài Thuốc lợi tiểu giải thích cơ chế/kê đơn lợi tiểu. |

**Không trùng lặp:**

- **IM-44:** không dạy CKD G×A, SGLT2i/ACEi/ARB chronic strategy, complications CKD hoặc chuẩn bị dialysis.
- **IM-45–IM-50:** khi case gợi bệnh thận chuyên biệt, bài này dừng ở nhận diện intrinsic clue và referral đúng nơi.
- **Thuốc lợi tiểu:** không dùng lợi tiểu để “điều trị số creatinine” hay hướng dẫn liều; chỉ nêu medication review/safety.

## 5. Dàn ý chi tiết cho lesson release

### Section 0 · Tổng quan và nền tảng tối thiểu
- Giải thích “creatinine hơi cao” là một tín hiệu, không phải diagnosis; nhấn tần suất/gánh nặng AKI phụ thuộc setting và cần nhận diện sớm.
- Mục tiêu: đọc trend, phân biệt acute/chronic, nhận emergency physiology, triển khai work-up và escalation an toàn.
- `### 0.1 Nền tảng tối thiểu cần dùng ngay`: nephron, filtration, creatinine, GFR/eGFR, steady state, urine output, AKI vs CKD.

### Section 1 · Định nghĩa
- Định nghĩa AKI/stages theo KDIGO final bằng nguyên tắc; không in numeric thresholds/stage table.
- Giải thích why changing creatinine lags physiology và why eGFR is an estimate.
- Nêu boundary AKI–AKD–CKD; `abnormal < chronic duration` không được gọi CKD tự động.

### Section 2 · Cơ chế
- Trình bày pre-renal/perfusion, intrinsic và post-renal như khung differential, không như ba hộp chẩn đoán đóng kín.
- Nối perfusion, tubular injury, obstruction với clues/history/urine output; nhắc thuốc/exposure.

### Section 3 · Chẩn đoán
- Đặt `BOX ĐỎ` trước routine algorithm: dấu hiệu → nguy cơ → hành động ngay → nơi chuyển.
- Chuỗi bắt buộc: confirm/baseline → emergency physiology → urine output/trend → volume/perfusion/exposure → medicines → urinalysis/microscopy → electrolytes/acid–base → intrinsic clues → ultrasound when obstruction plausible → stage/cause/location.
- Bảng giải thích tại sao single creatinine, eGFR, FeNa/FeUrea, urine sodium và ultrasound không đủ độc lập.

### Section 4 · Điều trị
- Điều trị cause, restore perfusion when deficient with reassessment, avoid blind loading/overload, medication safety plan, manage complications, and specialist escalation for KRT/local protocol.
- Không viết doses, volume, timing threshold, contrast or dialysis protocol.

### Section 5 · Theo dõi
- Trend urine/creatinine/clinical physiology; reassess response and complications.
- Kế hoạch recovery/follow-up; AKI increases long-term kidney-risk, không dán nhãn CKD trước khi temporal requirement rõ.

### Section 6 · Tóm tắt
- 10 điểm vàng từ interpretation đến escalation.

### Section 7 · Tips
- Ít nhất tám mistakes/pearls: baseline, eGFR non-steady state, urine output, medication review, fluid reassessment, microscopy, obstruction, referral.

### Section 8 · Bằng chứng
- KDIGO 2012 final; NICE 2024; NIDDK 2024; STARRT-AKI và evidence recovery.

### Section 9 · Tài liệu tham khảo
- Dùng đủ 14 PMIDs đã khóa với annotation tag; mọi PMID lesson phải thuộc bảng source lock này.

### Mermaid + Plan B
- Branches bắt buộc: `red flag?` → `acute change/baseline known?` → `urine output and trend` → `volume/perfusion/exposure` → `intrinsic clues` → `obstruction risk` → `response/reassessment` → `referral/escalation`.
- Limited settings: repeat creatinine/electrolytes when available; strict I/O/vital trend; safe medication review only under documented plan; bedside urine test; early transfer if shock/sepsis/obstruction/rapid progression plausible; never invent baseline.

### Four five-step cases
1. Dehydration/sepsis, rising creatinine, uncertain baseline.
2. AKI on CKD: identify acute change before applying chronic framework.
3. Medication/nephrotoxin exposure with oliguria/electrolyte concern.
4. Obstruction or intrinsic clues requiring ultrasound/nephrology/urology escalation.

## 6. Execute contract

1. Write only claims in Section 3; all figures/protocol details remain prohibited unless this locked brief is revised after direct full-text verification.
2. Use Vietnamese with full diacritics and explain first use as: what it is → normal behavior → why abnormal matters → how to recognize it → what to do next.
3. Exact required headings: `## 0. TỔNG QUAN`, `## 1. ĐỊNH NGHĨA`, `## 2. CƠ CHẾ`, `## 3. CHẨN ĐOÁN`, `## 4. ĐIỀU TRỊ`, `## 5. THEO DÕI`, `## 6. TÓM TẮT`, `## 7. TIPS`, `## 8. BẰNG CHỨNG`, `## 9. TÀI LIỆU THAM KHẢO`.
4. Release must have at least 12 `###` subsections, 6 substantive tables, 8 tips, 4 cases, Mermaid plus Plan B, more than 12,000 characters and 250 lines. Do not add filler.
5. Create exactly 80 `basic` cards with non-empty `front`, `back`, `extra`; no card may add a claim/dose/threshold/protocol not in this brief.
6. Build named APKG, independently check 80 notes/80 cards, generate learner knowledge check, then run every gate listed in the release contract.
7. Do not edit indexes until `publish_gate.py` returns `PUBLISH READY: profile=disease; 11 required gates PASS`.
