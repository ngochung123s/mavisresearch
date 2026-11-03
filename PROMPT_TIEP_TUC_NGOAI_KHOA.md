# 🚀 PROMPT KHỞI ĐỘNG TIẾP TỤC DỰ ÁN NGOẠI KHOA THỰC CHIẾN (SURG)

> **Vị trí lưu:** `Desktop` & `F:\DL\mavisresearch\PROMPT_TIEP_TUC_NGOAI_KHOA.md`  
> **Cập nhật:** 2026-11-03  
> **Người sở hữu:** Bác sĩ Đỗ Văn Ngọc Hưng 🍅 🐈‍⬛  
> **Repo làm việc:** `F:\DL\mavisresearch\`  
> **Web tra cứu:** [dvnhmed.pages.dev](https://dvnhmed.pages.dev) (HungMed)

---

## 📋 COPY ĐOẠN PROMPT DƯỚI ĐÂY DÁN VÀO SESSION MỚI

```markdown
Chào bạn, tiếp tục dự án Bệnh học Ngoại khoa Lâm sàng (16_Ngoai khoa) trong repo F:\DL\mavisresearch.

1. Bối cảnh hiện tại:
- Đã quy hoạch 86 bài học Ngoại khoa tại `Bai hoc y khoa/_CURRICULUM_NGOAI_KHOA.md`.
- Đã tích hợp chuyên khoa Ngoại vào web HungMed (dvnhmed.pages.dev) qua `build_unified_med_library.py`.
- Đã hoàn thành xuất bản 2 bài đầu tiên với đầy đủ hồ sơ y chứng (Gate 0 ncbi_fetch.json, Gate 1 abstract_match.jsonl, Gate 2 full_verify_table.md, Research Brief, Master MD):
  + SURG-16: Viêm ruột thừa cấp và các thể biến chứng phức tạp.
  + SURG-17: Thủng ổ loét dạ dày - tá tràng và thủng tạng rỗng cấp cứu.

2. Nhiệm vụ hôm nay:
Tiếp tục triển khai bài tiếp theo: **SURG-18: Tắc ruột cơ học: Cơ chế quai kín, thắt nghẹt & Tắc do bít** (P0).

3. Quy trình thực hiện BẮT BUỘC (Tuân thủ nghiêm ngặt skill medical-verification-governance & RULES_LESSON_APKG.md, TUYỆT ĐỐI KHÔNG DÙNG KNOWLEDGE LLM ĐỂ BỊA SỐ LIỆU):
- Bước 1: Tra cứu y văn chính thống trên PubMed bằng NCBI E-utilities (E-summary, E-fetch) lấy các bài báo/guideline chuẩn (WSES 2017/2021 Bologna guidelines on adhesive SBO, landmark RCTs, reviews).
- Bước 2: Tạo bộ artifacts Gate 0 (`ncbi_fetch.json`), Gate 1 (`abstract_match.jsonl`), Gate 2 (`full_verify_table.md`) và file `SURG-18_RESEARCH_BRIEF.md` khóa contract profile `disease`.
- Bước 3: Soạn Master Markdown `SURG-18_..._RELEASE_v1.md` bám sát Logic 7 tầng:
  + Độ dài ≥ 6000 từ, ≥ 600 dòng.
  + Đủ 10 sections bắt buộc (Tổng quan, Định nghĩa, Cơ chế, Chẩn đoán, Điều trị, Theo dõi, Tóm tắt, Tips, Bằng chứng, Tài liệu tham khảo).
  + ≥ 5 chuỗi cơ chế (`> 🔄 **Chuỗi cơ chế:** ... → ...`).
  + ≥ 8 ví dụ lâm sàng (`Ví dụ:`).
  + ≥ 8 bẫy lâm sàng / sai lầm (`> ⚠️ HỌC VIÊN HAY NHẦM:` / `> ⚠️ BẪY LÂM SÀNG:`).
  + ≥ 5 Checkpoint tự kiểm tra (`### 🛑 DỪNG 1 PHÚT — TỰ KIỂM TRA (CHECKPOINT N)`).
  + ≥ 3 ca lâm sàng thực tế có lời giải chi tiết.
  + Định dạng Unicode 100% (→, ≥, ≤, ×), TUYỆT ĐỐI KHÔNG dùng LaTeX `$`, `$$`, `\text{}`, `\ge`, không tab đầu dòng.
  + Box đỏ cảnh báo an toàn (`> 🛑 **Box đỏ cảnh báo an toàn lâm sàng:**`).
- Bước 4: Kiểm tra linter bằng lệnh:
  `python "Bai hoc y khoa/10_Script Python/lesson_lint.py" "Bai hoc y khoa/16_Ngoai khoa/SURG-18_Tac_ruot_co_hoc"`
  Yêu cầu bắt buộc: BLOCK=0 DEBT=0.
- Bước 5: Cập nhật `_CURRICULUM_NGOAI_KHOA.md`, chạy `python "Bai hoc y khoa/hungmed/build_unified_med_library.py"` để biên dịch lại `data.js`, sau đó git commit và push origin main.

Bắt đầu thực hiện ngay từ Bước 1!
```

---

## 📊 BẢNG THEO DÕI TIẾN ĐỘ NGOẠI KHOA (SURG)

| Mã bài | Tên chuyên đề | Profile | Artifacts Evidence | Master MD | Linter | Web HungMed | Trạng thái |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **SURG-16** | **Viêm ruột thừa cấp & Biến chứng** | `disease` | ✅ Đủ Gate 0, 1, 2 + Brief | ✅ 55.000 ký tự | ✅ 0 BLOCK | ✅ Đã build data.js | **HOÀN TẤT** |
| **SURG-17** | **Thủng tạng rỗng & Thủng dạ dày - tá tràng** | `disease` | ✅ Đủ Gate 0, 1, 2 + Brief | ✅ 50.000 ký tự | ✅ 0 BLOCK | ✅ Đã build data.js | **HOÀN TẤT** |
| **SURG-18** | **Tắc ruột cơ học (Quai kín, thắt nghẹt & bít)** | `disease` | ⏳ Chờ làm | ⏳ Chờ làm | ⏳ Chờ làm | ⏳ Chờ làm | **KẾ TIẾP** |
| **SURG-19** | **Xoắn đại tràng Sigma & Xoắn manh tràng** | `disease` | 📋 Quy hoạch | 📋 Quy hoạch | 📋 Quy hoạch | 📋 Quy hoạch | Chờ duyệt |
| **SURG-20** | **Hẹp môn vị dạ dày - tá tràng** | `disease` | 📋 Quy hoạch | 📋 Quy hoạch | 📋 Quy hoạch | 📋 Quy hoạch | Chờ duyệt |

---

## 🛠️ CÁC LỆNH HỆ THỐNG THƯỜNG DÙNG

1. **Kiểm tra Linter bài học:**
   ```bash
   python "F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\lesson_lint.py" "F:\DL\mavisresearch\Bai hoc y khoa\16_Ngoai khoa\<folder_bai>"
   ```
2. **Biên dịch thư viện web HungMed (dvnhmed.pages.dev):**
   ```bash
   python "F:\DL\mavisresearch\Bai hoc y khoa\hungmed\build_unified_med_library.py"
   ```
3. **Đẩy mã nguồn lên GitHub (tự động trigger Cloudflare Pages):**
   ```bash
   cd "F:\DL\mavisresearch"
   git add "Bai hoc y khoa/"
   git commit -m "feat(surg): phat hanh <ma_bai>"
   git push origin main
   ```
