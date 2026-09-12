# RESEARCH BRIEF: IM-36 — Xuất huyết tiêu hóa trên & dưới sau hồi sức
**Ngày:** 2026-07-19 | **Model research:** DeepSeek (ocg) | **Model execute:** DeepSeek (ocg)

---

## 1. Papers đã chọn

| # | PMID | Loại | Tiêu đề | Tại sao chọn |
|---|---|---|---|---|
| 1 | 25308912 | Cochrane MA | Epinephrine injection vs epinephrine + second method in high-risk bleeding ulcers (2014) | **Xương sống dual therapy** — 19 RCTs, n=2.033. Là bằng chứng mạnh nhất cho "không tiêm epinephrine đơn thuần" |
| 2 | 33567467 | Guideline | ESGE 2021: NVUGIH | **Tier 0** — tái dùng từ IM-16. Phần endoscopic management: Forrest, dual therapy, aspirin management, H. pylori |
| 3 | 33929377 | Guideline | ACG 2021: UGIB | **Tier 0** — tái dùng từ IM-16. Khuyến cáo endoscopic therapy, PPI post-endoscopy |
| 4 | 35120736 | Consensus | Baveno VII 2022: Portal hypertension | **Tier 0** — tái dùng từ IM-16. Secondary prophylaxis: NSBB + EVL, carvedilol preference |
| 5 | 27147389 | Meta-analysis | Carvedilol for portal hypertension in cirrhosis (2016) | **Carvedilol > propranolol** — 12 RCTs, bằng chứng cho ưu tiên carvedilol trong dự phòng thứ phát |
| 6 | 30792244 | Guideline | BSG 2019: Lower GI bleeding | **Tier 0 cho XHTH dưới** — CTA trước nội soi, embolization, transfusion |

**Reusable từ IM-16 (không fetch lại):**
- Cochrane restrictive vs liberal transfusion (28397699) — dùng cho phần transfusion trong XHTH dưới
- TRIGGER trial (23281973) — restrictive transfusion
- HALT-IT (32563378) — TXA negative

**Đã loại:**
- PMID 33822357 (Cochrane 2021 primary prevention variceal) — là PRIMARY prevention, không phải secondary. Không dùng cho IM-36.
- PMID 42270957 (UGIB comprehensive review 2026) — review chung, không có số liệu mới. Dùng làm background nếu cần.

---

## 2. Claims đã verify

### 2.1 Dual therapy nội soi (Cochrane 2014)

| # | Claim | PMID | Tag |
|---|---|---|---|
| D1 | 19 RCTs, n=2.033 BN loét nguy cơ cao (Forrest Ia–IIb) | 25308912 | [FULL VERIFIED: PMID 25308912] |
| D2 | Epinephrine + second method → giảm further bleeding: RR 0.53 (95% CI 0.35–0.81) | 25308912 | [FULL VERIFIED: PMID 25308912] |
| D3 | Giảm overall bleeding (persistent + recurrent): RR 0.57 (95% CI 0.43–0.76) | 25308912 | [FULL VERIFIED: PMID 25308912] |
| D4 | Giảm emergency surgery: RR 0.68 (95% CI 0.50–0.93) | 25308912 | [FULL VERIFIED: PMID 25308912] |
| D5 | Mortality không khác biệt có ý nghĩa giữa 2 nhóm | 25308912 | [DIRECTION ONLY] |
| D6 | Kết luận: "Additional endoscopic treatment after epinephrine injection reduces further bleeding and need for surgery" | 25308912 | [ABSTRACT VERIFIED] |

### 2.2 ESGE 2021 (tái dùng từ IM-16)

| # | Claim | PMID | Tag |
|---|---|---|---|
| E1 | Endoscopic therapy recommended for Forrest Ia, Ib, IIa | 33567467 | [GUIDELINE VERIFIED: PMID 33567467] |
| E2 | Epinephrine NOT as monotherapy — combine with clip or thermal | 33567467 | [GUIDELINE VERIFIED: PMID 33567467] |
| E3 | Aspirin for secondary CV prophylaxis: do not interrupt. Restart within 3–5 days | 33567467 | [GUIDELINE VERIFIED: PMID 33567467] |
| E4 | H. pylori testing for all PUD bleeding patients | 33567467 | [GUIDELINE VERIFIED: PMID 33567467] |
| E5 | High-dose PPI IV (bolus + continuous) for 72h after endoscopic hemostasis | 33567467 | [GUIDELINE VERIFIED: PMID 33567467] |

### 2.3 ACG 2021 (tái dùng từ IM-16)

| # | Claim | PMID | Tag |
|---|---|---|---|
| A1 | Endoscopic therapy for active spurting/oozing and nonbleeding visible vessels | 33929377 | [GUIDELINE VERIFIED: PMID 33929377] |
| A2 | PPI bolus + continuous infusion for 3 days after endoscopic hemostasis | 33929377 | [GUIDELINE VERIFIED: PMID 33929377] |
| A3 | Routine second-look endoscopy NOT recommended | 33929377 | [GUIDELINE VERIFIED: PMID 33929377] |

### 2.4 Baveno VII (tái dùng từ IM-16)

| # | Claim | PMID | Tag |
|---|---|---|---|
| B1 | NSBB + EVL for secondary prophylaxis of variceal bleeding | 35120736 | [GUIDELINE VERIFIED: PMID 35120736] |
| B2 | Carvedilol preferred over propranolol for portal hypertension | 35120736 | [GUIDELINE VERIFIED: PMID 35120736] |
| B3 | EVL every 2–4 weeks until varices eradicated | 35120736 | [GUIDELINE VERIFIED: PMID 35120736] |
| B4 | Endoscopic surveillance every 6–12 months after eradication | 35120736 | [GUIDELINE VERIFIED: PMID 35120736] |
| B5 | TIPS (covered stent) when NSBB + EVL fails | 35120736 | [GUIDELINE VERIFIED: PMID 35120736] |

### 2.5 Carvedilol meta (2016)

| # | Claim | PMID | Tag |
|---|---|---|---|
| C1 | 12 RCTs | 27147389 | [FULL VERIFIED: PMID 27147389] |
| C2 | Carvedilol vs propranolol: greater HVPG reduction (MD −8.49%, 95% CI −12.36 to −4.63) | 27147389 | [FULL VERIFIED: PMID 27147389] |
| C3 | Carvedilol không giảm MAP nhiều hơn propranolol | 27147389 | [DIRECTION ONLY] |
| C4 | Carvedilol vs EVL: no significant difference in mortality or bleeding | 27147389 | [DIRECTION ONLY] |
| C5 | Overall quality of evidence is low — need more RCTs | 27147389 | [DIRECTION ONLY] |

### 2.6 BSG 2019 — Lower GI Bleeding

| # | Claim | PMID | Tag |
|---|---|---|---|
| L1 | CT angiography for hemodynamically unstable patients with suspected LGIB | 30792244 | [GUIDELINE VERIFIED: PMID 30792244] |
| L2 | Colonoscopy within 24h after adequate bowel preparation | 30792244 | [GUIDELINE VERIFIED: PMID 30792244] |
| L3 | Angiographic embolization first-line when endoscopy fails or not feasible | 30792244 | [GUIDELINE VERIFIED: PMID 30792244] |
| L4 | Restrictive transfusion (Hb <7, or <8 in CVD) | 30792244 | [GUIDELINE VERIFIED: PMID 30792244] |

---

## 3. Kiến thức nền (textbook)

| # | Kiến thức | Nguồn |
|---|---|---|
| 1 | Forrest classification: Ia spurting, Ib oozing, IIa visible vessel, IIb adherent clot, IIc flat spot, III clean base | [TEXTBOOK: Sleisenger and Fordtran's GI and Liver Disease, 11e, Ch.20] |
| 2 | Rockall score: age + shock + comorbidity + endoscopic diagnosis + SRH → predicts mortality | [TEXTBOOK: Sleisenger and Fordtran, 11e] |
| 3 | H. pylori → chronic gastritis → ulcer → bleeding. Eradication reduces recurrence | [TEXTBOOK: Harrison's Principles of Internal Medicine, 21e, Ch.190] |
| 4 | Portal hypertension pathophysiology: increased resistance + increased flow → varices | [TEXTBOOK: Sleisenger and Fordtran, 11e, Ch.92] |
| 5 | NSBB mechanism: β1 blockade → ↓ CO; β2 blockade → splanchnic vasoconstriction → ↓ portal flow | [TEXTBOOK: Guyton and Hall, 15e] |
| 6 | EVL mechanism: rubber band ligation → ischemic necrosis → fibrosis → variceal obliteration | [TEXTBOOK: Sleisenger and Fordtran, 11e] |
| 7 | CT angiography for GI bleeding: detects bleeding rate >0.3–0.5 mL/min, guides embolization | [TEXTBOOK: Harrison's, 21e] |

---

## 4. Số liệu CẤM dùng

- Số liệu cụ thể về hiệu quả H. pylori eradication (NNT) — chưa fetch được meta-analysis riêng. Chỉ dùng khuyến cáo guideline.
- Tỉ lệ biến chứng cụ thể của từng kỹ thuật nội soi — textbook knowledge, không có PMID.
- Số liệu về tỉ lệ thành công của EVL/TIPS tại VN — không có dữ liệu.

---

## 5. Dàn ý chi tiết (để expand MD)

### Section 0: Tổng quan
- Mở bằng ca IM-16 đã hồi sức xong, giờ đến nội soi
- IM-36 = "sau nội soi": Forrest → can thiệp → nguyên nhân → dự phòng
- KHÔNG lặp IM-16

### Section 1: Chẩn đoán phân biệt nguồn chảy [CỐT LÕI]
- Dùng claim: none (textbook + clinical reasoning)
- Ba tình huống sau nội soi
- Bảng variceal vs non-variceal

### Section 2: Forrest [CỐT LÕI]
- Dùng kiến thức nền #1
- Bảng Forrest I–III với nguy cơ tái XH
- Caveats: IIa bắt buộc can thiệp, IIb vùng xám, PPI "hạ cấp"

### Section 3: Kỹ thuật nội soi [CỐT LÕI]
- Dùng claims D1–D6 (dual therapy)
- Dùng claims E1–E2 (ESGE khuyến cáo dual)
- Bảng 6 kỹ thuật + so sánh
- Biến chứng

### Section 4: Rockall score [CỐT LÕI]
- Dùng kiến thức nền #2
- Bảng tính đầy đủ
- Diễn giải điểm

### Section 5: Điều trị nguyên nhân [CỐT LÕI]
- Dùng claims E3–E5 (ESGE)
- H. pylori test-and-treat (guideline)
- NSAID/aspirin management
- PPI maintenance

### Section 6: Dự phòng non-variceal
- Tổng hợp từ Section 5

### Section 7: Dự phòng variceal [CỐT LÕI]
- Dùng claims B1–B5 (Baveno VII)
- Dùng claims C1–C5 (carvedilol)
- NSBB titration, EVL schedule, TIPS

### Section 8: XHTH dưới [CỐT LÕI]
- Dùng claims L1–L4 (BSG 2019)
- CTA → embolization → colonoscopy
- Mermaid flowchart

### Section 9: Evidence — CHỈ số liệu đã verify
- Claims từ tất cả các bảng trên, format [FULL VERIFIED: PMID XXXXX]

### Section 10–15: Sai lầm, VN, Cases, Tips, Tổng kết, References

---

## 6. Hướng dẫn cho model execute

```
QUY TẮC CỨNG:
1. Body text (Sections 1–8): CHỈ viết định tính, mô tả, giải thích cơ chế. KHÔNG số liệu cụ thể.
2. Section 9 (Evidence): TẤT CẢ số liệu cụ thể, mỗi dòng có [FULL VERIFIED: PMID XXXXX] hoặc [GUIDELINE VERIFIED: PMID XXXXX].
3. Mỗi claim số liệu chỉ gắn MỘT tag — không gộp nhiều PMID trong cùng một tag.
4. Tiếng Việt có dấu. Thuật ngữ y khoa giữ tiếng Anh.
5. Từ khóa: Forrest, dual therapy, Rockall, H. pylori eradication, NSBB, EVL, carvedilol, CTA, embolization.
```
