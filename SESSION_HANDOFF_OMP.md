# SESSION HANDOFF & CONTEXT CỦA PHIÊN LÀM VIỆC (Dành cho Oh My Pi / OMP)

**Ngày tạo:** 2026-09-13  
**Chủ dự án:** Bác sĩ Ngọc Hưng (Mavis Research)  
**Workspace chính:** `F:\DL\mavisresearch\`  
**GitHub Repository:** `https://github.com/ngochung123s/mavisresearch.git`

---

## 1. Các File Ngữ Cảnh & Bộ Nhớ Dài Hạn (Memory & Context Links)
1. **User Profile & Phong cách làm việc**: `F:\DL\mavisresearch\CONTEXT.md`
   - Bác sĩ tự học/nghiên cứu Sản phụ khoa & Nhi khoa.
   - Phong cách **Why-based learning**: Làm gì + Tại sao làm vậy (Cơ chế sinh lý/nội tiết + Khuyến cáo Guideline có PMID/Doc ID).
   - Ngôn ngữ: Tiếng Việt chuẩn mực, giữ nguyên thuật ngữ viết tắt tiếng Anh và tên thuốc quốc tế.
2. **Quy tắc dự án & Pipeline kiến trúc**: `F:\DL\mavisresearch\CLAUDE.md` và `F:\DL\mavisresearch\AGENTS.md`
3. **Bộ nhớ Persistent Memory của Claude**:
   - `C:\Users\THANHANH\.claude\projects\C--Users-THANHANH\memory\MEMORY.md`
   - `C:\Users\THANHANH\.claude\projects\C--Users-THANHANH\memory\primary-workspace.md` (F:\DL\mavisresearch là thư mục làm việc chính)
   - `C:\Users\THANHANH\.claude\projects\C--Users-THANHANH\memory\why-based-lesson-style.md`

---

## 2. Toàn bộ Công việc Đã Hoàn Thành trong Phiên này

### A. Hệ thống Nhi khoa Core 45 (`Bai hoc y khoa/12_Nhi khoa/`)
- Đã cấu trúc lại 7 Block chuyên khoa theo chuẩn `00_Nen_tang_va_Tiep_can` đến `06_Than_Tim_mach_Noi_tiet`.
- File theo dõi tiến độ: `Bai hoc y khoa/_CURRICULUM_NHI_KHOA.md`
- **PED-01** (Đặc điểm sinh lý & Bảng sinh hiệu bình thường theo tuổi):
  - Bài Markdown 12.378 từ: `12_Nhi khoa/00_Nen_tang_va_Tiep_can/PED-01_Dac_diem_sinh_ly_va_Sinh_hieu_theo_tuoi/PED-01_..._RELEASE_v1.md` (PASS 100% depth_check).
  - 48 Flashcards Anki: `...cards.v2.json` và `...RELEASE_v1.apkg` (PASS 95.6% diacritics).
  - Web App lâm sàng tương tác: `...theo_tuoi.html`.
- **PED-02** (Tam giác đánh giá nhi khoa PAT & Tiếp cận ABCDE):
  - Bài Markdown 16.114 từ: `12_Nhi khoa/00_Nen_tang_va_Tiep_can/PED-02_Tam_giac_danh_gia_PAT_va_ABCDE/PED-02_..._RELEASE_v1.md` (PASS 100% depth_check).
  - 48 Flashcards Anki: `...cards.v2.json` và `...RELEASE_v1.apkg` (PASS 96.6% diacritics).
  - Web App lâm sàng tương tác: `...ABCDE.html`.

### B. Số hóa Giáo trình Sản Phụ Khoa ĐHYD Thái Bình 2021
- **File gốc:** `F:\DL\BG_ĐAI_HỌC_BM_4_12_2021_FINAL_S_Repaired_Đã_sửa_chữa.doc` (35MB).
- **Thư viện số hóa:** `F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021\` và bản backup trong `F:\DL\mavisresearch\banks\giao_trinh_san_khoa_2021\`.
- Đã khử sạch 100% font cũ TCVN3 sang Unicode NFC chuẩn.
- Đã chia tách đủ **54 bài học thuộc 6 chương**, mỗi bài gồm cả `.md` và `.json` bóc tách sẵn mốc số liệu tuần thai/ml máu (`key_numbers`) và tên thuốc (`key_drugs`).
- File mục lục tổng hợp: `CATALOG_BAI_GIANG.md` và `index.json`.
- File toàn văn sách gộp: `FULL_TEXT_BOOK_UNICODE.txt`.

### C. Phần mềm Học thuộc Lòng & Chép Chính tả BSNT: MedSpelling
- File ứng dụng: `F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021\app.html` (chạy offline 100% qua Chrome/Edge, nạp dữ liệu từ `data.js`).
- Shortcut ngoài Desktop: `C:\Users\THANHANH\Desktop\MedSpelling - Học thuộc Sản Khoa BSNT.url`.
- Tích hợp đủ 4 chế độ:
  1. *Guided Fading*: Kéo thanh trượt che từ mốc 0 đến 4.
  2. *Cue Recall*: Mồi chữ cái đầu, điền khuyết chữ cái đầu, mồi gạch đầu dòng 4T.
  3. *Dictation Typing*: Word Runner chuẩn MonkeyType, tương thích 100% bộ gõ Telex/VNI Unikey, kèm chọn mục nhỏ (chunking 50-150 từ) và đo WPM/Accuracy.
  4. *Bareme Matcher*: Bấm đề thi gợi ý, tự gõ bài làm, máy tự chấm điểm /10 theo từ khóa, số liệu và từ điển đồng nghĩa y khoa.
- Toàn bộ source code app và thư viện đã được commit và push lên GitHub repo `ngochung123s/mavisresearch` (Commit `15b433e`).
