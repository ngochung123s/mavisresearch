# RESEARCH BRIEF: IM-38b Bệnh Viêm Ruột Mạn (IBD)

- **Mã bài học:** IM-38b
- **Tên bài học:** Bệnh Viêm Ruột Mạn (IBD): Viêm loét đại tràng (UC) & Bệnh Crohn (CD)
- **Chuyên khoa:** Nội khoa / Tiêu hóa
- **Profile phát hành:** `disease`
- **Cấp độ biên soạn:** L2 — Standard (Bài chi tiết cho bác sĩ đa khoa)

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

---

## 1. DÀN Ý BÀI HỌC (OUTLINE - L2 STANDARD)

1. **0.0 Tổng quan:** IBD là gì? Phân biệt UC và Crohn. Tầm quan trọng của việc không chẩn đoán nhầm với IBS hay Viêm đại tràng nhiễm trùng.
2. **1.0 Sinh lý bệnh & Cơ chế:**
   - Vai trò của hệ miễn dịch niêm mạc ruột và hệ vi sinh.
   - Tổn thương giải phẫu bệnh: UC (nông, liên tục, từ trực tràng) vs Crohn (xuyên thành, ngắt quãng, miệng-hậu môn, u hạt).
3. **2.0 Chẩn đoán Lâm sàng & Cận lâm sàng:**
   - Triệu chứng tiêu hóa: Tiêu chảy máu, đau quặn bụng, sụt cân.
   - Biểu hiện ngoài ruột (Extra-intestinal): Viêm khớp, hồng ban nút, PSC.
   - Vai trò của Fecal Calprotectin trong sàng lọc.
   - Tiêu chuẩn vàng: Nội soi đại tràng sinh thiết.
4. **3.0 Phân độ nặng (Severity):**
   - Tiêu chuẩn Truelove & Witts cho UC.
   - Chỉ số CDAI cho Crohn.
5. **4.0 Phác đồ Điều trị (Dược lý):**
   - Nhóm 5-ASA (Mesalazine): Điều trị duy trì UC nhẹ-vừa.
6. **5.0 Biến chứng & Cấp cứu:** Phình đại tràng nhiễm độc (Toxic Megacolon).
7. **6.0 Thực chiến Việt Nam:** Bẫy chẩn đoán nhầm Lao ruột (Intestinal TB) và lạm dụng Loperamide.
8. **7.0 Tóm tắt & Bảng tra cứu.**
9. **8.0 Bằng chứng y học & Guideline.**

---

## 2. VERIFIED CITATIONS & TEXTBOOK CLAIMS

- PMID: 30840605 — ACG Clinical Guideline: Ulcerative Colitis in Adults. [DIRECTION ONLY]
- PMID: 29610508 — ACG Clinical Guideline: Management of Crohn's Disease in Adults. [DIRECTION ONLY]
- PMID: 31351880 — Among fecal tests, fecal calprotectin in a range of 50-60 μg/g (pooled sensitivity 0.81; 95% confidence interval [CI], 0.75-0.86; pooled specificity 0.87; 95% CI, 0.78-0.92) presented the lowest proportion of false-negative results. [ABSTRACT MATCH]
- PMID: 22644954 — No difference was observed between the dosing strategies [once daily vs conventional] in the proportion of patients with clinical remission (relative risk [RR] 0.95; 95% confidence interval [CI] 0.82-1.10) or relapse at 6 (RR 1.10; 95% CI 0.83-1.46) or 12 months (RR 0.92; 95% CI 0.83-1.03). [ABSTRACT MATCH]
- PMID: 26263042 — At 76 weeks, 14% (1/7) of methotrexate patients maintained remission compared to 64% (7/11) of 6-MP patients (RR 0.22, 95% CI 0.03 to 1.45) and 0% (0/2) of 5-ASA patients (RR 1.13, 95% CI 0.06 to 20.71). [ABSTRACT MATCH]
- PMID: 35863682 — Hospitalization rates for a primary diagnosis were increasing in countries in stage 2 [including newly industrialized countries in Asia] for IBD (AAPC, 4.44%; 95% CI, 2.75 to 6.14), CD (AAPC, 8.34%; 95% CI, 4.38 to 12.29), and UC (AAPC, 3.90; 95% CI, 1.29 to 6.52). [ABSTRACT MATCH]
- PMID: 32736897 — Extraintestinal manifestations (EIMs) were reported in 199 (11.3%) Asian IBD patients, and EIMs appeared in 8% of patients before IBD diagnosis. [ABSTRACT MATCH]
- PMID: 14638335 — Toxic megacolon (TM) is an infrequent but devastating complication of colitis, and the majority occur in individuals with inflammatory bowel disease (IBD). [DIRECTION ONLY]
- PMID: 34716521 — Up to 25% of patients with ulcerative colitis (UC) may require hospitalization, and up to 30% of UC patients will fail to respond to initial intravenous corticosteroid. [ABSTRACT MATCH]
### A. TEXTBOOK CONSENSUS CLAIMS [TEXTBOOK] (Không gán PMID)
- Viêm loét đại tràng (UC) chỉ gây tổn thương lớp niêm mạc và dưới niêm mạc, tổn thương liên tục bắt đầu từ trực tràng lan lên trên. [TEXTBOOK]
- Bệnh Crohn (CD) gây tổn thương viêm xuyên thành, có thể xuất hiện ngắt quãng (skip lesions) ở bất kỳ đoạn nào từ miệng đến hậu môn. [TEXTBOOK]
- Phình đại tràng nhiễm độc (Toxic Megacolon) là biến chứng cấp cứu ngoại khoa đe dọa tính mạng của IBD. [TEXTBOOK]

### B. CLINICAL & PHYSIOLOGICAL CLAIMS WITH PMID [ABSTRACT MATCH / DIRECTION ONLY]
*(Sẽ bổ sung sau khi chạy extract_claims_from_abstract.py)*

---

## 3. CLAIMS & SỐ LIỆU Bị CẤM (CẤM HALLUCINATE)
- Không tự ý thêm số liệu % dịch tễ, liều lượng thuốc 5-ASA hay Corticoid nếu không có PMID xác minh.
- Không gán PMID cho các kiến thức giải phẫu bệnh cơ bản của UC và Crohn.
