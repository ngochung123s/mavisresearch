# RESEARCH BRIEF: IM-16 — Xuất huyết tiêu hóa cấp: Hồi sức 0–60 phút
**Ngày:** 2026-07-19 | **Model research:** DeepSeek (ocg) | **Model execute:** DeepSeek (ocg)

---

## 1. Papers đã chọn (kèm lý do chọn)

| # | PMID | Loại | Tiêu đề (rút gọn) | Tại sao chọn |
|---|---|---|---|---|
| 1 | 33567467 | Guideline | ESGE 2021: Endoscopic diagnosis and management of NVUGIH | **Tier 0 guideline chính** — khuyến cáo GBS, restrictive transfusion, PPI, erythromycin, nội soi <24h |
| 2 | 33929377 | Guideline | ACG 2021: Upper Gastrointestinal and Ulcer Bleeding | **Tier 0 guideline chính** — bổ sung ESGE, GRADE approach, GBS 0-1 = outpatient |
| 3 | 35120736 | Consensus | Baveno VII 2022: Portal hypertension | **Tier 0 variceal bleeding** — vasoactive drugs, KS dự phòng, restrictive transfusion, nội soi <12h. Đã verify trong IM-40, tái sử dụng claims |
| 4 | 32563378 | RCT | HALT-IT 2020: TXA in GI bleeding (Lancet, n=12.009) | **Landmark RCT** — TXA KHÔNG giảm tử vong, TĂNG VTE → KHÔNG dùng TXA |
| 5 | 23281973 | RCT | TRIGGER 2013: Restrictive vs liberal transfusion (NEJM, n=921) | **Landmark RCT** — restrictive (Hb<7) giảm tử vong (HR 0.55), giảm tái XH (10% vs 16%) |
| 6 | 28397699 | Meta-analysis | Cochrane 2017: Restrictive vs liberal transfusion in GI bleeding (n=1965) | **Meta-analysis xương sống** — restrictive: ↓ mortality RR 0.65, ↓ rebleeding RR 0.58 |
| 7 | 30508958 | Meta-analysis | Terlipressin for acute variceal bleeding (n=3344, 30 RCTs) | **Meta-analysis chính cho terlipressin** — cải thiện kiểm soát chảy máu 48h (OR 2.94), ↓ tử vong nội viện (OR 0.31) |
| 8 | 33723542 | Meta-analysis | Vasoactive Agents: T-V vs O-S for AVB (21 RCTs) | **So sánh terlipressin vs octreotide/somatostatin** — tử vong tương đương (RR 1.01), T-V nhiều AE hơn (RR 2.39) |
| 9 | 34661508 | Meta-analysis | Risk scores in predicting outcomes in AVB (28 studies) | **Phân tầng nguy cơ AVB** — CTP AUC 0.824 (tốt nhất cho tử vong nội viện), AIMS65 specificity 0.774 |
| 10 | 27640399 | Systematic Review | Pre-endoscopic risk scores for UGIB in ED (16 studies) | **GBS validation** — GBS sensitivity 0.98, specificity 0.16 ở cutoff 0 |
| 11 | 40611560 | NMA | Pre-endoscopy erythromycin vs metoclopramide for UGIB (16 studies, n=1447) | **Erythromycin evidence** — cải thiện visualization (SMD 0.58), adequate visualization (RR 1.55) |
| 12 | 32024301 | Review | Diagnosis and Management of Non-Variceal GI Hemorrhage (2020) | **Tổng quan non-variceal** — current guidelines and future perspectives |
| 13 | 30313117 | Meta-analysis | 5-day vasoactive drug after endoscopic hemostasis for AVB | **Duration of vasoactive** — adjuvant 5-day giảm very early rebleeding |
| 14 | 31921329 | Guideline | WSES 2020: Perforated and bleeding peptic ulcer | **Bổ sung ngoại khoa** — PUD complications management |

**Đã loại:**
- PMID 33512469 (plan ghi sai — là paper về TB biobank, không phải ESGE 2021). ESGE 2021 đúng = PMID 33567467.
- PMID 31501175 (plan ghi sai — là case report Sertoli-Leydig tumor, không phải BSG 2019). BSG 2019 chỉ có guideline LOWER GI bleeding (PMID 30792244); BSG không có guideline riêng cho upper GI — UK dùng NICE CG141.
- PMID 29862492 (Cochrane 2018: UGIB prevention in ICU) — là stress ulcer prophylaxis, không phải XHTH cấp điều trị, không dùng.

**Tier 0 web guidelines bổ sung:**
- NICE CG141 (2012, reviewed 2018): Acute upper GI bleeding management. Comprehensive UK guideline, 2018 surveillance: no new evidence → vẫn current.
- Không có BSG guideline riêng cho upper GI bleeding; BSG chỉ có lower GI (PMID 30792244).

---

## 2. Claims đã verify — chỉ viết claim CÓ trong abstract

### 2.1 Restrictive vs Liberal Transfusion

| # | Claim | PMID | Tag |
|---|---|---|---|
| T1 | Restrictive transfusion → giảm all-cause mortality: RR 0.65 (95% CI 0.44–0.97, p=0.03) | 28397699 | [FULL VERIFIED] |
| T2 | Restrictive transfusion → giảm rebleeding: RR 0.58 (95% CI 0.40–0.84, p=0.004) | 28397699 | [FULL VERIFIED] |
| T3 | Số RBC units thấp hơn ở restrictive: mean difference −1.73 units (95% CI −2.36 to −1.11, p<0.0001) | 28397699 | [FULL VERIFIED] |
| T4 | Restrictive (Hb<7): survival at 6 weeks 95% vs liberal (Hb<9) 91%; HR for death 0.55 (95% CI 0.33–0.92, P=0.02) | 23281973 | [FULL VERIFIED] |
| T5 | Restrictive: 51% không cần truyền máu vs liberal: 14% (P<0.001) | 23281973 | [FULL VERIFIED] |
| T6 | Further bleeding: restrictive 10% vs liberal 16% (P=0.01) | 23281973 | [FULL VERIFIED] |
| T7 | Adverse events: restrictive 40% vs liberal 48% (P=0.02) | 23281973 | [FULL VERIFIED] |

### 2.2 ESGE 2021 Guideline Claims

| # | Claim | PMID | Tag |
|---|---|---|---|
| E1 | GBS ≤1: very low risk, safe for outpatient management with outpatient endoscopy (Strong recommendation, moderate evidence) | 33567467 | [GUIDELINE VERIFIED] |
| E2 | Low-dose aspirin monotherapy for secondary CV prophylaxis: should NOT be interrupted. If interrupted, restart within 3–5 days | 33567467 | [GUIDELINE VERIFIED] |
| E3 | PPI liều cao IV trước nội soi (khuyến cáo cho tất cả BN nghi XHTH trên) | 33567467 | [GUIDELINE VERIFIED] |
| E4 | Erythromycin IV trước nội soi cải thiện chất lượng hình ảnh | 33567467 | [GUIDELINE VERIFIED] |
| E5 | Nội soi <24h cho BN nguy cơ cao | 33567467 | [GUIDELINE VERIFIED] |

### 2.3 ACG 2021 Guideline Claims

| # | Claim | PMID | Tag |
|---|---|---|---|
| A1 | GBS 0–1: very-low-risk, có thể xuất viện với outpatient follow-up | 33929377 | [GUIDELINE VERIFIED] |
| A2 | RBC transfusion threshold: Hb 7 g/dL (suggested) | 33929377 | [GUIDELINE VERIFIED] |
| A3 | Erythromycin infusion suggested before endoscopy | 33929377 | [GUIDELINE VERIFIED] |
| A4 | Endoscopy suggested within 24 hours after presentation | 33929377 | [GUIDELINE VERIFIED] |
| A5 | Endoscopic therapy recommended for ulcers with active spurting/oozing and nonbleeding visible vessels | 33929377 | [GUIDELINE VERIFIED] |

### 2.4 HALT-IT Trial (TXA)

| # | Claim | PMID | Tag |
|---|---|---|---|
| H1 | n=12.009 (TXA 5.994 vs placebo 6.015), 164 hospitals, 15 countries | 32563378 | [FULL VERIFIED] |
| H2 | Death due to bleeding within 5 days: TXA 4% (222/5956) vs placebo 4% (226/5981); RR 0.99 (95% CI 0.82–1.18) | 32563378 | [FULL VERIFIED] |
| H3 | VTE (DVT or PE) higher in TXA group: 0.7% vs 0.4% — increased risk | 32563378 | [DIRECTION ONLY] |
| H4 | Interpretation: "TXA did not reduce death from GI bleeding... should not be used for treatment of GI bleeding outside randomized trial" | 32563378 | [FULL VERIFIED] |

### 2.5 Variceal Bleeding — Vasoactive Drugs

| # | Claim | PMID | Tag |
|---|---|---|---|
| V1 | Terlipressin vs no vasoactive: cải thiện bleeding control 48h (OR 2.94, P=0.0008), ↓ in-hospital mortality (OR 0.31, P=0.008) | 30508958 | [FULL VERIFIED] |
| V2 | 30 RCTs, n=3344 bệnh nhân | 30508958 | [FULL VERIFIED] |
| V3 | Terlipressin có nguy cơ complications cao hơn somatostatin (OR 2.44, P=0.04) | 30508958 | [FULL VERIFIED] |
| V4 | T-V vs O-S: mortality RR 1.01 (95%CI 0.83–1.22) — tương đương | 33723542 | [FULL VERIFIED] |
| V5 | T-V có adverse events cao hơn O-S: RR 2.39 (95%CI 1.58–3.63, I²=57%) | 33723542 | [FULL VERIFIED] |
| V6 | 21 RCTs included | 33723542 | [FULL VERIFIED] |

### 2.6 Erythromycin Pre-endoscopy

| # | Claim | PMID | Tag |
|---|---|---|---|
| Er1 | Erythromycin cải thiện endoscopic visualization score: SMD 0.58 (95% CI 0.26–0.91) | 40611560 | [FULL VERIFIED] |
| Er2 | Adequate mucosal visualization: RR 1.55 (95% CI 1.18–2.04) | 40611560 | [FULL VERIFIED] |
| Er3 | Erythromycin giảm need for second-look endoscopy, transfusion, hospital stay | 40611560 | [DIRECTION ONLY] |
| Er4 | Metoclopramide KHÔNG hiệu quả hơn placebo | 40611560 | [DIRECTION ONLY] |
| Er5 | 16 studies, n=1.447 | 40611560 | [FULL VERIFIED] |

### 2.7 Risk Stratification Scores

| # | Claim | PMID | Tag |
|---|---|---|---|
| R1 | GBS sensitivity 0.98, specificity 0.16 (cutoff 0) | 27640399 | [FULL VERIFIED] |
| R2 | GBS cutoff 0 có sensitivity 0.99, specificity 0.08 | 27640399 | [FULL VERIFIED] |
| R3 | AIMS65 sensitivity 0.79, specificity 0.61 | 27640399 | [FULL VERIFIED] |
| R4 | CTP best for in-hospital mortality in AVB: AUC 0.824, sensitivity 0.910, specificity 0.666 | 34661508 | [FULL VERIFIED] |
| R5 | AIMS65 highest specificity 0.774 for in-hospital mortality | 34661508 | [FULL VERIFIED] |
| R6 | 28 articles included | 34661508 | [FULL VERIFIED] |

### 2.8 Baveno VII (tái sử dụng từ IM-40, PMID 35120736)

| # | Claim | PMID | Tag |
|---|---|---|---|
| B1 | Vasoactive drugs (terlipressin/somatostatin/octreotide) NGAY khi nghi vỡ TMTQ — không chờ nội soi xác nhận | 35120736 | [GUIDELINE VERIFIED] |
| B2 | Kháng sinh dự phòng (ceftriaxone) cho tất cả BN xơ gan có XHTH — giảm nhiễm trùng, tái XH, tử vong | 35120736 | [GUIDELINE VERIFIED] |
| B3 | Restrictive transfusion (Hb <7) | 35120736 | [GUIDELINE VERIFIED] |
| B4 | Nội soi <12h cho vỡ TMTQ | 35120736 | [GUIDELINE VERIFIED] |
| B5 | KHÔNG dùng FFP để điều chỉnh INR kéo dài ở BN xơ gan | 35120736 | [GUIDELINE VERIFIED] |

---

## 3. Kiến thức nền — anatomy/physiology (có nguồn)

| # | Kiến thức | Nguồn |
|---|---|---|
| 1 | Ống tiêu hóa nuôi bởi 3 nhánh ĐM chủ bụng: thân tạng, mạc treo tràng trên, mạc treo tràng dưới | [TEXTBOOK: Netter's Atlas of Human Anatomy, 8e, Plates 278-300] |
| 2 | Góc Treitz = chỗ nối tá tràng-hỗng tràng, mốc phân biệt XHTH trên/dưới | [TEXTBOOK: Gray's Anatomy, 42e] |
| 3 | Thể tích máu ~70 mL/kg. Sốc mất máu phân loại ATLS class I-IV | [TEXTBOOK: ATLS Student Course Manual, 10e. ACS] |
| 4 | Baroreflex: ↓HA → ↓kích thích thụ thể áp lực xoang cảnh/quai ĐMC → ↑giao cảm → ↑HR, co mạch ngoại vi/tạng | [TEXTBOOK: Guyton and Hall, 15e, Ch.25] |
| 5 | Pepsin tiêu fibrin ở pH thấp; pH >6 → cục máu đông bền | [TEXTBOOK: Guyton and Hall, 15e, Ch.37] |
| 6 | Cầm máu 3 cơ chế: co mạch tại chỗ, nút tiểu cầu, đông máu huyết tương (fibrin) | [TEXTBOOK: Guyton and Hall, 15e, Ch.37] |
| 7 | BUN/Cr >30:1 gợi ý XHTH trên (hấp thu protein máu ở ruột non→↑BUN) | [TEXTBOOK: Harrison's Principles of Internal Medicine, 21e, Ch.47] |
| 8 | Xơ gan → ↑NO nội sinh → giãn mạch tạng nền → HA nền thấp → tụt HA sớm khi mất máu | [TEXTBOOK: Sleisenger and Fordtran's GI and Liver Disease, 11e] |

---

## 4. Số liệu CẤM dùng (không có trong abstract đã fetch)

Các claim sau KHÔNG được phép viết vào MD vì chưa verify được từ abstract:
- Tỉ lệ tử vong cụ thể của XHTH trên/theo từng nguyên nhân tại Việt Nam (chỉ mô tả định tính)
- Số liệu về NNT (number needed to treat) cho kháng sinh dự phòng trong vỡ TMTQ (chỉ biết direction)
- So sánh cụ thể PPI bolus ngắt quãng vs truyền liên tục (chưa có meta-analysis cụ thể trong brief)
- Hiệu quả của từng prokinetic cụ thể ngoài erythromycin (metoclopramide đã có bằng chứng KHÔNG hiệu quả)
- Chi phí/thống kê sẵn có thuốc tại BV Việt Nam (chỉ mô tả định tính, không số liệu)

---

## 5. Dàn ý chi tiết

### Section 0: Tổng quan
- Mở bằng case lâm sàng: BN 55t, nôn máu đỏ tươi, HA 85/50, mạch 120
- Phép so sánh: ống tiêu hóa = đường ống
- XHTH trên (trên góc Treitz) vs XHTH dưới (dưới góc Treitz)
- "Cấp cứu trước chẩn đoán" — không cần biết nguồn chảy trong 60 phút đầu
- IM-16 prerequisite cho IM-36
- Mục tiêu: (1) nhận diện sốc mất máu, (2) hồi sức, (3) thuốc ban đầu, (4) phân tầng GBS/AIMS65, (5) quyết định nội soi/chuyển tuyến
- 0.1 Nền tảng tối thiểu: kiến thức nền #1–4, ABCDE, restrictive transfusion

### Section 1: Sinh lý bệnh — Mất máu cấp [CỐT LÕI]
- 1.0 Nhắc nhanh: kiến thức nền #1–2
- 1.1 ATLS class I–IV: bảng chi tiết
- 1.2 Đáp ứng bù trừ + bẫy lâm sàng: kiến thức nền #4, #8; người già/chẹn beta/ĐTĐ không nhịp nhanh; xơ gan tụt HA sớm
- 1.3 Cầm máu tự nhiên: kiến thức nền #6, #5 — cơ sở dùng PPI

### Section 2: Nhận diện & Đánh giá ban đầu [CỐT LÕI]
- 2.1 ABCDE: chi tiết từng bước
- 2.2 Hỏi nhanh 4 câu: bảng
- 2.3 Khám thực thể trọng điểm
- BOX ĐỎ: nôn máu đỏ tươi lượng lớn + tụt HA + lú lẫn
- 🛑 checkpoint

### Section 3: Xét nghiệm trong 60 phút đầu [CỐT LÕI]
- 3.1 Xét nghiệm bắt buộc: CTM (bẫy Hb ban đầu), đông máu, nhóm máu, sinh hóa (BUN/Cr >30:1 = kiến thức nền #7), lactate
- 3.2 Xét nghiệm tùy tình huống: troponin, ECG
- 3.3 NG tube: chỉ định, chống chỉ định

### Section 4: Hồi sức dịch và truyền máu [CỐT LÕI]
- 4.1 Dịch truyền: crystalloid (RL hoặc NaCl 0.9%), bolus 500–1000 mL, KHÔNG colloid. Mục tiêu: HATT ≥100, HR <100, UO >0.5 mL/kg/h, lactate ↓
- 4.2 Restrictive transfusion: claims T1–T7, E5, A2, B3. Ngưỡng Hb <7 (hoặc <8 ở bệnh tim mạch)
- 4.3 MTP: khi nào kích hoạt, tỉ lệ 1:1:1
- 4.4 BN đặc biệt: xơ gan (không FFP để chỉnh INR), bệnh tim mạch

### Section 5: Thuốc ban đầu trong 60 phút [CỐT LÕI]
- 5.1 PPI: cơ chế (kiến thức nền #5), chỉ định, cách dùng, claims E3, A3
- 5.2 Vasoactive drugs: terlipressin (2 mg IV bolus → 1–2 mg mỗi 4–6h), octreotide (50 mcg bolus → 25–50 mcg/h). Claims V1–V6, B1
- 5.3 Kháng sinh dự phòng: ceftriaxone 1g IV/24h × 7d. Claim B2
- 5.4 Erythromycin: 250 mg IV 30–90 phút trước nội soi. Claims Er1–Er5
- 5.5 TXA: KHÔNG khuyến cáo. Claims H1–H4
- 5.6 Đảo ngược kháng đông/kháng TC: warfarin (vit K + PCC), DOAC, aspirin, DAPT

### Section 6: Phân tầng nguy cơ và quyết định nội soi [CỐT LÕI]
- 6.1 GBS: 8 biến, GBS 0–1 = outpatient (claims E1, A1, R1–R2)
- 6.2 AIMS65: 5 biến, đơn giản (claims R3, R5)
- 6.3 Rockall: sau nội soi → IM-36
- 6.4 Phân luồng nội soi: cấp cứu <6h, sớm <24h, trì hoãn (claims E5, A4, B4)

### Section 7: Evidence & Guidelines [CỐT LÕI]
- 7.1 ESGE 2021 (33567467): key recommendations
- 7.2 ACG 2021 (33929377): key recommendations
- 7.3 Baveno VII (35120736): key recommendations
- 7.4 HALT-IT (32563378): TXA negative
- 7.5 TRIGGER + Cochrane meta: transfusion evidence

### Section 8: Lưu đồ quyết định lâm sàng [CỐT LÕI]
- Mermaid 1: Tiếp cận BN XHTH 0–60 phút
- Mermaid 2: Nhánh nghi vỡ TMTQ

### Section 9: Sai lầm thường gặp [CỐT LÕI]
(Bảng 7 lỗi — từ plan + clinical experience)

### Section 10: Bảng thuốc và liều dùng [THAM KHẢO]

### Section 11: Áp dụng tại Việt Nam [CỐT LÕI]
- Plan A/Plan B cho từng tình huống
- Thuốc sẵn có/không sẵn có
- Chuyển tuyến khi không thể nội soi cấp cứu

### Section 12: Case lâm sàng [NÂNG CAO]
(4 cases từ plan)

### Section 13: Tips thực hành [THAM KHẢO]
(10 tips)

### Section 14: Tổng kết [CỐT LÕI]
(10 điểm)

### Section 15: Tài liệu tham khảo

---

## 6. Hướng dẫn cho model execute

```
Bạn là model execute. Nhiệm vụ: viết bài MD hoàn chỉnh từ brief này.

QUY TẮC CỨNG:
1. CHỈ dùng claims trong bảng "Claims đã verify" — KHÔNG thêm claim mới
2. CHỈ dùng số liệu có tag [FULL VERIFIED] — nếu không có tag này, chỉ viết định tính
3. CHỈ dùng kiến thức nền có nguồn trong bảng "Kiến thức nền"
4. Với mỗi section, follow dàn ý chi tiết — thêm ví dụ, paraphrase, nhưng không thêm ý
5. Tiếng Việt có dấu đầy đủ. Thuật ngữ y khoa giữ tiếng Anh.
6. Thêm checkpoint (🛑) sau mỗi 2–3 section
7. Nếu không chắc chắn về 1 claim → bỏ claim đó, không bịa
8. Template: theo template_lesson.md

OUTPUT: File MD hoàn chỉnh theo template_lesson.md
```
