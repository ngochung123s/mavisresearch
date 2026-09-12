# RESEARCH BRIEF: IM-05 Sinh lý và Nguyên lý tạo hình ảnh trên ECG

- **Mã bài học:** IM-05
- **Tên bài học:** Sinh lý và Nguyên lý tạo hình ảnh trên ECG (ECG Fundamental Physiology & Lead Vectors)
- **Chuyên khoa:** Nội khoa / Tim mạch (Internal Medicine / Cardiology)
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

1. **0.0 Tổng quan & Khái niệm cốt lõi:** Điện thế thế nghỉ, Khử cực, Tái cực của tế bào cơ tim.
2. **0.1 Nền tảng tối thiểu:** Điện học tế bào cơ tim, Kênh ion ($Na^+$, $K^+$, $Ca^{2+}$) và hình thành Dòng điện vector.
3. **1.0 Nguyên lý Máy quay phim (Lead Vector Principle):**
   - Cực Âm (-), Cực Dương (+), Đèn chiếu vector.
   - 3 Quy tắc sóng: Về phía cực dương $\rightarrow$ Sóng (+); Ra xa cực dương $\rightarrow$ Sóng (-); Vuông góc $\rightarrow$ Sóng hai pha/đẳng điện.
4. **2.0 Tam giác Einthoven & 6 Chuyển đạo ngoại biên (D1, D2, D3, aVR, aVL, aVF):**
   - Chuyển đạo lưỡng cực vs Đơn cực chi.
   - Mặt phẳng trán (Frontal Plane) & Trục điện tim góc α.
5. **3.0 6 Chuyển đạo trước tim (V1 đến V6):**
   - Mặt phẳng ngang (Horizontal Plane).
   - Sự tiến triển sóng R từ V1 đến V6 (R progression) và Vùng chuyển tiếp.
6. **4.0 Giải mã từng sóng và đoạn trên ECG 12 chuyển đạo:**
   - **Sóng P:** Khử cực nhĩ (Nhĩ phải trước, nhĩ trái sau).
   - **Đoạn PR:** Chậm truyền qua nút nhĩ thất (AV node delay).
   - **Phức bộ QRS:** Khử cực thất (Sóng Q: Vách liên thất trái $\rightarrow$ phải; Sóng R: mỏm tim & thất trái; Sóng S: đáy thất).
   - **Đoạn ST & Sóng T:** Tái cực thất (Tại sao sóng T lại dương dù là tái cực?).
   - **Sóng U & Khoảng QT:** Ý nghĩa sinh lý & an toàn điện học.
7. **5.0 Tóm tắt chuỗi Reasoning 5 tầng cho nguyên lý tạo sóng ECG.**
8. **6.0 Bẫy lâm sàng & Sai sót kỹ thuật thường gặp:**
   - Mắc ngược dây chì (aVR dương bất thường).
   - Nhiễu cơ, nhiễu điện lưới 50Hz.
9. **7.0 Ứng dụng thực tế Việt Nam:** Phân luồng máy ECG 3 cần/6 cần/12 cần tại tuyến y tế cơ sở.
10. **8.0 Case lâm sàng giả định (4 case):** Nhận diện sóng sinh lý bình thường vs biến dạng do đặt sai điện cực.
11. **9.0 Checkpoint & Bảng tổng hợp tra cứu nhanh.**
12. **10.0 Danh mục tài liệu tham khảo & PMID Verified.**

---

## 2. VERIFIED CITATIONS & TEXTBOOK CLAIMS

### A. TEXTBOOK CONSENSUS CLAIMS [TEXTBOOK] (Không gán PMID)
- Tế bào cơ tim lúc nghỉ có điện thế âm ở trong (-90mV) và dương ở ngoài. [TEXTBOOK]
- Khử cực xảy ra khi ion $Na^+$ đi vào trong tế bào qua kênh nhanh $Na^+$. [TEXTBOOK]
- Tam giác Einthoven được tạo bởi 3 cực ở Tay phải (RA), Tay trái (LA), Chân trái (LL). [TEXTBOOK]
- Chuyển đạo DII có cực dương ở Chân trái và cực âm ở Tay phải, trùng với trục tổng thể của dòng khử cực tim. [TEXTBOOK]
- Sóng P bình thường rộng < 0.12s và cao < 2.5mm ở DII. [TEXTBOOK]
- Sóng T dương ở DII, V5, V6 là do lớp cơ ngoài màng tim tái cực trước lớp cơ trong tâm mạc. [TEXTBOOK]

### B. CLINICAL & PHYSIOLOGICAL CLAIMS WITH PMID [ABSTRACT MATCH / DIRECTION ONLY]
- PMID: 19281931 — AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part IV: the ST segment, T and U waves, and the QT interval. [ABSTRACT MATCH]
- PMID: 19281930 — AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part III: intraventricular conduction disturbances. [ABSTRACT MATCH]
- PMID: 22929906 — Electrocardiographic electrode misplacement, misconnection, and artifact. [ABSTRACT MATCH]
- PMID: 19419407 — ECG manifestations of multiple electrolyte imbalance: peaked T wave to P wave. [ABSTRACT MATCH]
- PMID: 35672420 — A large-scale multi-label 12-lead electrocardiogram database with standardized diagnostic statements. [ABSTRACT MATCH]

---

## 3. CLAIMS & SỐ LIỆU Bị CẤM (CẤM HALLUCINATE)
- Không tự ý thêm số liệu % biến đổi sóng khi không có trong Brief.
- Không gán PMID cho khái niệm cơ bản như "Sóng P là sóng khử cực nhĩ".
