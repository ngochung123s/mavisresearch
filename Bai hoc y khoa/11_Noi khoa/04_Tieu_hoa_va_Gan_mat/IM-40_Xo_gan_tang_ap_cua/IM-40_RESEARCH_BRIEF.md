# RESEARCH BRIEF: Xơ gan và tăng áp cửa
****Mã bài học:** IM-40 | Ngày:** 2026-07-19 | **Model research:** DeepSeek V4 Pro | **Model execute:** DeepSeek V4 Pro

---

## 1. Papers đã chọn (kèm lý do chọn)

| # | PMID | Loại | Tại sao chọn |
|---|---|---|---|
| 1 | 35120736 | Guideline (Baveno VII) | 1,990 citations — consensus toàn cầu về tăng áp cửa, nền tảng xương sống |
| 2 | 37870298 | Guideline (AASLD 2024) | 288 citations — risk stratification & management portal HTN + varices |
| 3 | 37159031 | Review (JAMA 2023) | 237 citations — tổng quan toàn diện chẩn đoán & điều trị xơ gan |
| 4 | 33942342 | Guideline (AASLD 2021) | Ascites, SBP, HRS — guideline chính thức của AASLD |
| 5 | 36075500 | Guideline (AGA 2022) | 74 citations — AKI/HRS trong xơ gan, cập nhật thực hành |
| 6 | 41114681 | Guideline (AGA 2025) | Ascites, volume overload, hyponatremia — mới nhất 2025 |
| 7 | 29861076 | RCT (ANSWER, Lancet 2018) | Landmark trial long-term albumin — 38% reduction in mortality HR |
| 8 | 33657294 | RCT (CONFIRM, NEJM 2021) | Landmark trial terlipressin HRS-1 — verified reversal 32% vs 17% |
| 9 | 36972759 | Review (CGH 2023) | Update toàn diện treatment of complications of cirrhosis |
| 10 | 31176013 | Meta-analysis (CGH 2020) | 91 citations — HVPG response → reduced events/death |
| 11 | 37141993 | Meta-analysis (J Hepatol 2023) | 84 citations — TIPS prevents further decompensation |
| 12 | 30372514 | Cochrane Meta (2018) | 38 citations — carvedilol vs traditional NSBB |
| 13 | 33784794 | Cochrane NMA (2021) | Secondary prevention variceal bleeding network meta-analysis |
| 14 | 25042402 | Guideline (AASLD/EASL 2014) | Hepatic encephalopathy — guideline chung AASLD+EASL |
| 15 | 25631669 | Consensus (ICA 2015, Gut) | AKI criteria in cirrhosis — revised ICA consensus |
| 16 | 35589252 | Review (J Hepatol 2022) | 65 citations — long-term albumin treatment update |
| 17 | 36697778 | Meta-review (Adv Ther 2023) | Albumin meta-analyses overview |
| 18 | 37358642 | Consensus (Billroth IV, 2023) | 57 citations — Austrian consensus portal HTN |

**Đã loại:** 32431989 (editorial, không đủ nội dung), 38501671 (đánh giá AASLD guidance, không phải guideline gốc), các paper về microbiota/heart disease không liên quan.

---

## 2. Claims đã verify — chỉ viết claim CÓ trong abstract

| # | Claim | PMID | Tag |
|---|---|---|---|
| 1 | Cirrhosis affects ~2.2M US adults; mortality 14.9→21.9/100K (2010-2021) | 37159031 | [FULL VERIFIED] |
| 2 | Most common US causes: alcohol ~45%, NAFLD 26%, HCV 41% | 37159031 | [FULL VERIFIED] |
| 3 | Elastography ≥15 kPa confirms cirrhosis | 37159031 | [FULL VERIFIED] |
| 4 | ~40% diagnosed when presenting with decompensation (ascites/HE) | 37159031 | [FULL VERIFIED] |
| 5 | First-line: carvedilol/propranolol (variceal bleeding prevention), lactulose (HE), spironolactone+furosemide (ascites), terlipressin (HRS) | 37159031 | [ABSTRACT VERIFIED] |
| 6 | HVPG responders (↓>20% or <12mmHg): reduced events (ascites/VH/HE) OR 0.35 (95% CI 0.22-0.56); death/LT OR 0.50 (95% CI 0.32-0.78) | 31176013 | [FULL VERIFIED] |
| 7 | TIPS vs SOC: 2-year further decompensation 0.48 vs 0.63 (p<0.0001); HR 0.44 (95% CI 0.37-0.54) | 37141993 | [FULL VERIFIED] |
| 8 | CONFIRM: terlipressin vs placebo HRS reversal 32% vs 17% (P=0.006); any reversal 39% vs 18% (P<0.001) | 33657294 | [FULL VERIFIED] |
| 9 | ANSWER: long-term albumin 18-month survival 77% vs 66% (p=0.028); mortality HR 0.62 (95% CI 0.40-0.95) | 29861076 | [FULL VERIFIED] |
| 10 | NSBB prevents decompensation in CSPH; pre-emptive TIPS for high-risk variceal bleeding (CP 10-13 or CP 8-9 + active bleeding) | 36972759 | [ABSTRACT VERIFIED] |
| 11 | Baveno VII: cACLD definition, CSPH (HVPG ≥10 mmHg), non-invasive tools for CSPH diagnosis | 35120736 | [ABSTRACT VERIFIED] |
| 12 | Long-term HA reduced ascites recurrence but not mortality; HA post-LVP reduced PCCD and hyponatremia; HA in SBP reduced mortality | 36697778 | [ABSTRACT VERIFIED] |
| 13 | Carvedilol more effective at reducing HVPG than traditional NSBB but uncertain clinical benefit (low quality evidence) | 30372514 | [ABSTRACT VERIFIED] |
| 14 | VBL fewer serious adverse events than sclerotherapy; TIPS large decrease in symptomatic rebleed vs VBL | 33784794 | [ABSTRACT VERIFIED] |
| 15 | Compensated vs decompensated cirrhosis: different survival rates; decompensation = ascites, VH, HE | 36972759 | [ABSTRACT VERIFIED] |

**Số liệu CẤM dùng (không có trong abstract đã fetch):**
- Tỉ lệ cụ thể của từng biến chứng theo từng năm (chỉ có range 5-10%/năm cho ascites từ plan — chưa verify)
- Số liệu về hiệu quả của EVL so với NSBB trong dự phòng tiên phát (Cochrane 33784794 chỉ cho secondary)
- Tỉ lệ tử vong cụ thể của từng biến chứng

---

## 3. Kiến thức nền — anatomy/physiology (có nguồn textbook)

| # | Kiến thức | Nguồn |
|---|---|---|
| 1 | Giải phẫu gan: thùy gan, tiểu thùy, khoảng cửa (portal triad: ĐM gan, TM cửa, ống mật), xoang gan (sinusoid), tĩnh mạch trung tâm | [TEXTBOOK: Sleisenger and Fordtran's Gastrointestinal and Liver Disease 11e, Ch.71] |
| 2 | Tuần hoàn cửa: TM cửa = hợp lưu TM mạc treo tràng trên + TM lách; áp lực cửa bình thường 5-10 mmHg; HVPG = WHVP - FHVP | [TEXTBOOK: Sleisenger and Fordtran 11e, Ch.72] |
| 3 | Chức năng gan: chuyển hóa (glucose, lipid, protein), tổng hợp (albumin, yếu tố đông máu), khử độc (ammonia→urea), bài tiết mật, miễn dịch (tế bào Kupffer) | [TEXTBOOK: Guyton and Hall 14e, Ch.71] |
| 4 | Sinh lý bệnh xơ hóa: HSC (hepatic stellate cell) activation → myofibroblast transformation → collagen type I/III deposition → sinusoidal capillarization | [REVIEW: PMID 32260126 (Roehlen et al., Cells 2020)] |
| 5 | Child-Pugh score: 5 tham số (bilirubin, albumin, INR, ascites, HE) → Class A (5-6), B (7-9), C (10-15) | [TEXTBOOK: Sleisenger and Fordtran 11e] |
| 6 | MELD score: bilirubin, creatinine, INR, Na → ưu tiên ghép gan. MELD-Na chính xác hơn | [TEXTBOOK: Sleisenger and Fordtran 11e] |
| 7 | Cơ chế SAAG: SAAG = albumin huyết thanh - albumin dịch báng; ≥1.1 g/dL = portal hypertension (dịch thấm); <1.1 = non-portal HTN (dịch tiết) | [TEXTBOOK: Sleisenger and Fordtran 11e, Ch.93] |
| 8 | Cơ chế HE: ammonia → astrocyte swelling → cytotoxic edema → neurotransmitter dysfunction; vai trò của GABA/BZD-like substances, inflammation | [GUIDELINE: PMID 25042402] |

---

## 4. Dàn ý chi tiết (KHÔNG phải tiêu đề suông)

### Section 0: Tổng quan — Vì sao bài này quan trọng?
- Mở đầu tình huống: BN xơ gan mất bù vào viện bụng to, lơ mơ, hoặc nôn ra máu
- Phép so sánh: gan = nhà máy lọc máu; xơ = sẹo làm tắc ống → áp lực tăng → 4 biến chứng
- 4 biến chứng chính: cổ trướng, HE, variceal bleeding, SBP
- Mục tiêu bài: 6 mục tiêu theo plan
- 0.1 Nền tảng tối thiểu: giải thích chức năng gan, tuần hoàn cửa, Child-Pugh, MELD

### Section 1: Sinh lý bệnh — Từ xơ gan đến tăng áp cửa [CỐT LÕI]
- 1.0 Nhắc nhanh: giải phẫu gan + tuần hoàn cửa (kiến thức nền #1, #2)
- 1.1 Cơ chế xơ hóa gan: HSC activation → collagen deposition → sinusoidal remodeling (kiến thức nền #4)
- 1.2 Tăng áp cửa: increased intrahepatic resistance + splanchnic vasodilation → hyperdynamic circulation
- 1.3 Hậu quả: ascites, varices, PHG, hypersplenism
- Mermaid: sơ đồ từ tổn thương gan → 4 biến chứng

### Section 2: Cổ trướng (Ascites) [CỐT LÕI]
- 2.1 Cơ chế: sinusoidal HTN → splanchnic vasodilation → effective hypovolemia → RAAS/SNS/ADH
- 2.2 Chẩn đoán: shifting dullness, fluid wave, SAST, diagnostic paracentesis
- 2.3 Xét nghiệm dịch báng: SAAG ≥ 1.1 (kiến thức nền #7), cell count, albumin, culture
- 2.4 Điều trị: hạn chế muối <2g/ngày, spironolactone + furosemide 100:40, theo dõi cân nặng
- 2.5 Cổ trướng kháng trị: LVP + albumin, TIPS, ghép gan; dùng claim #7, #9, #10
- BOX ĐỎ trước phần điều trị
- Bảng thuốc lợi tiểu

### Section 3: Nhiễm trùng dịch báng (SBP) [CỐT LÕI]
- 3.1 Cơ chế: bacterial translocation → ascitic fluid infection
- 3.2 Chẩn đoán: PMN ≥ 250 cells/mm³, cấy (+)
- 3.3 Điều trị: ceftriaxone/cefotaxime, albumin 1.5g/kg day 1 + 1g/kg day 3; dùng claim #12
- 3.4 Dự phòng: norfloxacin/TMP-SMX

### Section 4: Bệnh não gan (HE) [CỐT LÕI]
- 4.1 Cơ chế: ammonia → astrocyte swelling (kiến thức nền #8)
- 4.2 West Haven Grade 1–4
- 4.3 Yếu tố khởi phát: infection, GI bleeding, constipation, electrolytes, sedatives, TIPS
- 4.4 Điều trị: lactulose (3-4 BM/day), rifaximin 550mg BID; dùng guideline 25042402
- 4.5 Tiên lượng và dự phòng thứ phát

### Section 5: Giãn TMTQ và xuất huyết [CỐT LÕI]
- 5.1 Cơ chế: portosystemic collaterals → esophageal/gastric varices
- 5.2 Sàng lọc: EGD tất cả BN mới chẩn đoán; phân độ varices
- 5.3 Dự phòng tiên phát: NSBB (carvedilol/propranolol) hoặc EVL; dùng claim #6, #13, #14
- 5.4 XHTH cấp: hồi sức → kháng sinh → vasoactive drugs (terlipressin/octreotide) → EVL < 12h
- 5.5 Dự phòng thứ phát: EVL mỗi 2-4 tuần + NSBB; dùng claim #14
- 5.6 TIPS: chỉ định, CCĐ, biến chứng; dùng claim #7
- BOX ĐỎ: ABCDE approach cho variceal bleeding

### Section 6: Evidence & Guidelines [CỐT LÕI]
- 6.1 Baveno VII (2022) [GUIDELINE VERIFIED: PMID 35120736]
- 6.2 AASLD Portal Hypertension/Varices (2024) [GUIDELINE VERIFIED: PMID 37870298]
- 6.3 AASLD Ascites/SBP/HRS (2021) [GUIDELINE VERIFIED: PMID 33942342]
- 6.4 AASLD/EASL HE (2014) [GUIDELINE VERIFIED: PMID 25042402]
- 6.5 Landmark trials: ANSWER (PMID 29861076), CONFIRM (PMID 33657294)

### Section 7: Điều trị & Quản lý [CỐT LÕI]
- 7.1 Nguyên tắc: điều trị nguyên nhân + kiểm soát biến chứng + ghép gan
- 7.2 Phác đồ tổng hợp: bảng 4 biến chứng → bậc 1, bậc 2, theo dõi
- 7.3 HRS-AKI: ICA 2015 criteria (PMID 25631669), terlipressin + albumin; dùng claim #8
- 7.4 HCC screening: SA + AFP mỗi 6 tháng
- 7.5 Tiêm chủng: HAV, HBV, pneumococcal, influenza, COVID-19

### Section 8: Lưu đồ quyết định lâm sàng [CỐT LÕI]
- Mermaid 1: BN xơ gan mới chẩn đoán → phân tầng còn bù/mất bù → sàng lọc varices + HCC
- Mermaid 2: BN mất bù vào cấp cứu → phân nhánh theo triệu chứng chính

### Section 9: Sai lầm thường gặp [CỐT LÕI]
5 lỗi (theo plan)

### Section 10: Bảng thuốc [THAM KHẢO]
10 thuốc (theo plan)

### Section 11: Áp dụng tại Việt Nam [CỐT LÕI]
- Dịch tễ VN: HBV → cirrhosis #1, rượu #2
- Thuốc sẵn có, Plan A/Plan B cho mỗi biến chứng

### Section 12: Case lâm sàng [NÂNG CAO]
4 cases (theo plan)

### Section 13: Tips thực hành [THAM KHẢO]
10 tips

### Section 14: Tổng kết [CỐT LÕI]
10 điểm

### Section 15: Tài liệu tham khảo
~18 references

---

## 5. Hướng dẫn cho model execute

```
Bạn là model execute. Nhiệm vụ: viết bài MD hoàn chỉnh từ brief này.

QUY TẮC CỨNG:
1. CHỈ dùng claims trong bảng "Claims đã verify" — KHÔNG thêm claim mới
2. CHỈ dùng số liệu có tag [FULL VERIFIED] — nếu không có tag này, chỉ viết định tính
3. CHỈ dùng kiến thức nền có nguồn trong bảng "Kiến thức nền"
4. Với mỗi section, follow dàn ý chi tiết — thêm ví dụ, paraphrase, nhưng không thêm ý
5. Tiếng Việt có dấu đầy đủ. Thuật ngữ y khoa giữ tiếng Anh.
6. Thêm checkpoint (🛑) sau mỗi 2-3 section
7. Nếu không chắc chắn về 1 claim → bỏ claim đó, không bịa
8. Viết theo template_lesson.md — dùng BOX ĐỎ, bảng, Mermaid, checkpoint
9. Giải thích mọi khái niệm từ gốc cho người mất gốc — prerequisite chưa build
10. Phép so sánh: dùng "nhà máy lọc máu" cho gan, "sẹo làm tắc ống" cho xơ hóa

OUTPUT: File MD hoàn chỉnh theo template_lesson.md, ≥ 8,000 từ.
```