# RESEARCH BRIEF: IM-43b Sinh lý Nephron & Dược lý Thuốc lợi tiểu

- **Mã bài học:** IM-43b
- **Tên bài học:** Sinh lý Nephron & Dược lý Thuốc lợi tiểu (Từ Cơ chế đến Lâm sàng)
- **Chuyên khoa:** Nội khoa / Nội thận / Tim mạch
- **Profile phát hành:** `foundation`
- **Cấp độ biên soạn:** L3 — Hand-holding (Cầm tay chỉ việc cho người bắt đầu / học lại từ đầu)

---

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "profile_foundation",
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

## 1. DÀN Ý BÀI HỌC (OUTLINE - L3 DETAILED)

1. **0.0 Tổng quan:** Tại sao phải học Sinh lý Nephron và Thuốc lợi tiểu cùng nhau? Phép so sánh "Dòng sông và các Trạm thu phí".
2. **0.1 Nền tảng tối thiểu:** Các khái niệm Lọc (Filtration), Tái hấp thu (Reabsorption), Bài tiết (Secretion).
3. **1.0 Cầu thận (Glomerulus): Trạm kiểm soát đầu nguồn.**
   - Hàng rào lọc: Cho nước và chất tan nhỏ qua, giữ lại Hồng cầu và Protein.
   - Ứng dụng: Đánh giá eGFR và Protein niệu.
4. **2.0 Ống lượn gần (PCT): Trạm thu hồi rác tái chế khổng lồ.**
   - Sinh lý: Tái hấp thu 65% Nước, Na+, HCO3-, Glucose, Acid amin.
   - Dược lý: Nhóm Ức chế Carbonic Anhydrase (Acetazolamide). Cơ chế gây toan chuyển hóa.
5. **3.0 Quai Henle (Loop of Henle): Trạm vắt kiệt nước và muối.**
   - Sinh lý: Nhánh xuống (thấm nước), Nhánh lên dày (TAL - thấm muối qua bơm NKCC2).
   - Dược lý: Lợi tiểu quai (Furosemide). Cơ chế xả đập ồ ạt, mất Na+, K+, Ca2+, Mg2+.
6. **4.0 Ống lượn xa (DCT): Trạm tinh chỉnh muối.**
   - Sinh lý: Bơm NCC (Na-Cl Cotransporter).
   - Dược lý: Nhóm Thiazide. Tại sao Thiazide lại giữ Canxi (tốt cho sỏi thận/loãng xương)?
7. **5.0 Ống góp (Collecting Duct): Trạm thu phí cuối cùng do Sếp quản lý.**
   - Sinh lý: Bơm ENaC (chịu sự chiết phối của Aldosterone) và Kênh Aquaporin (chịu sự chiết phối của ADH).
   - Dược lý: Nhóm Tiết kiệm Kali (Spironolactone, Amiloride). Cơ chế gây tăng Kali máu.
8. **6.0 Kháng lợi tiểu & Khóa nephron nối tiếp (Sequential Nephron Blockade).**
   - Tại sao dùng Furosemide lâu ngày lại hết tác dụng? (Phì đại DCT).
   - Phối hợp Lợi tiểu quai + Thiazide.
---

## 2. VERIFIED CITATIONS & TEXTBOOK CLAIMS

### A. TEXTBOOK CONSENSUS CLAIMS [TEXTBOOK] (Không gán PMID)
- Nephron tạo nước tiểu thông qua 3 quá trình: Lọc tại cầu thận, Tái hấp thu và Bài tiết tại các đoạn ống thận. [TEXTBOOK]
- Ống lượn gần (PCT) tái hấp thu khoảng 65% lượng Na+ và nước được lọc, cùng với toàn bộ glucose và acid amin. [TEXTBOOK]
- Nhánh lên dày của quai Henle (TAL) tái hấp thu khoảng 25% lượng Na+ qua bơm đồng vận chuyển Na-K-2Cl (NKCC2) và hoàn toàn không thấm nước. [TEXTBOOK]
- Lợi tiểu quai (như Furosemide) ức chế mạnh mẽ bơm NKCC2 tại nhánh lên dày quai Henle, gây bài xuất một lượng lớn Na+, K+, Cl-, Ca2+, và Mg2+. [TEXTBOOK]
- Ống lượn xa (DCT) tái hấp thu khoảng 5% lượng Na+ qua bơm đồng vận chuyển Na-Cl (NCC). [TEXTBOOK]
- Nhóm Thiazide ức chế bơm NCC tại ống lượn xa, làm tăng bài xuất Na+ và Cl-, nhưng lại làm tăng tái hấp thu Ca2+ vào máu. [TEXTBOOK]
- Tại ống góp, Aldosterone kích thích tái hấp thu Na+ và bài tiết K+ qua kênh ENaC. Thuốc lợi tiểu tiết kiệm kali (như Spironolactone) đối kháng tác dụng này, giúp giữ lại K+. [TEXTBOOK]

### B. CLINICAL & PHYSIOLOGICAL CLAIMS WITH PMID [ABSTRACT MATCH / DIRECTION ONLY]
- PMID: 35294605 — Typically, the pharmacological group consists of five classes: thiazide diuretics, loop diuretics, potassium-sparing diuretics, osmotic diuretics, and carbonic anhydrase inhibitors. [DIRECTION ONLY]
- PMID: 36792826 — Structure and thiazide inhibition mechanism of the human Na-Cl cotransporter. [DIRECTION ONLY]
- PMID: 35776281 — A quantitative systems pharmacology model of plasma potassium regulation by the kidney and aldosterone. [DIRECTION ONLY]
- PMID: 41520701 — IV furosemide alone was administered in 78% of cases, while 22% received combination diuretic therapy. [ABSTRACT MATCH]
- PMID: 35688407 — Metolazone and intravenous (IV) chlorothiazide are commonly used diuretics for sequential nephron blockade (SNB) in patients with acute decompensated heart failure (ADHF). [DIRECTION ONLY]
- PMID: 28274923 — Effect of diuretics on renal tubular transport of calcium and magnesium. [DIRECTION ONLY]
- PMID: 32639593 — A Systematic Review and Meta-Analysis of Metolazone Compared to Chlorothiazide for Treatment of Acute Decompensated Heart Failure. [DIRECTION ONLY]
- PMID: 29500794 — The Art and Science of Using Diuretics in the Treatment of Heart Failure in Diverse Clinical Settings. [DIRECTION ONLY]
- PMID: 27056656 — Decongestion: Diuretics and other therapies for hospitalized heart failure. [DIRECTION ONLY]
- PMID: 26687765 — Intra-abdominal Hypertension: An Important Consideration for Diuretic Resistance in Acute Decompensated Heart Failure. [DIRECTION ONLY]
- PMID: 36592186 — The addition of SGLT2i to conventional therapy for AHF decreased mean daily doses of loop diuretics in mg of furosemide equivalent (MD -34.90; 95% CI [- 52.58, - 17.21]; p < 0.001) without increasing the incidence worsening renal function. [ABSTRACT MATCH]
- PMID: 34298494 — After adjustment, the use of continuous loop-diuretic infusion was associated with a higher 24-h urine output (β: 732, 95% CI:669-795, p < 0.001), lower 24-h fluid balance (p < 0.001) and greater weight loss at 48-h (p < 0.001). [ABSTRACT MATCH]
---

## 3. CLAIMS & SỐ LIỆU Bị CẤM (CẤM HALLUCINATE)
- Không tự ý thêm số liệu % tái hấp thu ở các đoạn ống thận khác ngoài các số liệu đã được xác nhận ở phần TEXTBOOK (65%, 25%, 5%).
- Không gán PMID cho các kiến thức sinh lý giải phẫu cơ bản của Nephron.
