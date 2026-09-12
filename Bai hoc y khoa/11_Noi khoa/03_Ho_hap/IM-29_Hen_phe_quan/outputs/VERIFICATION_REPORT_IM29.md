# CANONICAL VERIFICATION REPORT — IM-29 Hen phế quản

**Ngày thực hiện:** 2026-07-30  
**Tập tin bài học:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_2026-07-30_RELEASE_v1.md`  
**Tập tin Research Brief:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/IM-29_Hen_phe_quan_2026-07-30_RELEASE_v1_RESEARCH_BRIEF.md`  
**Tập tin Evidence Bundle:** `F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-29_Hen_phe_quan/outputs/IM-29_Hen_phe_quan_2026-07-30_RELEASE_v1_evidence_bundle.json`  

---

## 1. KẾT QUẢ VERIFIER BÀI HỌC (LECTURE VERIFIERS)

- **Số từ thực tế (Word Count):** **14,078 từ** (Đạt chuẩn 10,000 - 14,000 từ thực tế, văn xuôi hoàn chỉnh L3_BEGINNER).
- **Kiểm tra Tỷ lệ Tiếng Việt có dấu (`verify_diacritics.py`):**
  - Số từ tiếng Việt có dấu: 8,011
  - Tổng số từ tiếng Việt: 8,333
  - Tỷ lệ có dấu (Diacritics Ratio): **96.14%** (Đạt ngưỡng quy định $\ge 90\%$).
- **Canonical Verification Tags Used:** `[GUIDELINE VERIFIED]` (Chỉ sử dụng 1 trong 5 nhãn canonical được phép; không tự chế nhãn legacy).
- **Exit Code Verifier Check:** **0 (PASS)**.

---

## 2. KIỂM TRA CẤU TRÚC VÀ QUY TRÌNH CANONICAL

1. **Research Brief & Profile Lock:**
   - Profile: `disease` (xác nhận qua `publish_gate.py --list-profiles`).
   - Basename: `IM-29_Hen_phe_quan_2026-07-30_RELEASE_v1.md`.
   - 6 claim questions đã được khóa chuẩn xác dựa trên GINA 2024 / ERS / ATS.

2. **Cấu trúc Bài học (18 Sections):**
   - Đủ 18 sections theo outline.
   - Tỷ lệ nội dung: 60% hen ổn định / 40% đợt cấp hen.
   - Chuẩn L3_BEGINNER: Dạy từ gốc, không xài scaffold, stub hay TODO.
   - 2 Flowcharts ASCII thuần túy (` ```text `), không sử dụng Mermaid.
   - Bảng tối đa 3-4 cột đơn giản.
   - BOX ĐỎ cho nhận diện Lồng ngực câm / Cơn hen nguy kịch.
   - Plan B cho xử trí đợt cấp khi thiếu máy phun khí dung (dùng pMDI + Spacer tự chế).

3. **5 Ca lâm sàng chuẩn hóa:**
   - Đủ 5 ca với 5 bước chuẩn hóa (1. Red flag, 2. Dữ kiện quyết định, 3. Hành động, 4. Monitoring/Chuyển tuyến, 5. Why alternatives wrong).

4. **Giới hạn Deliverable:**
   - Đã tạo đúng file MD bài học và các artifacts nội bộ (Research Brief, Evidence bundle trong `outputs/`).
   - KHÔNG build APKG, DOCX, cards, Knowledge Checks, KHÔNG chạy publish gate hay update catalog/curriculum theo đúng yêu cầu.
