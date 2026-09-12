# BÀI HỌC Y KHOA - THƯ MỤC

> Tất cả bài học y khoa được AI assistant viết cho bác sĩ Ngọc Hưng 🍅 🐈‍⬛
> Tổ chức: phân loại theo chuyên khoa
> Cập nhật: 2026-07-22

## Cấu trúc thư mục

```
Bai hoc y khoa/
├── _CATALOG.md                             ← Bảng tra cứu nhanh folder bài học
├── _CURRICULUM_NOI_KHOA.md                 ← Curriculum Nội khoa người lớn
├── 01_San phu khoa/                       ← Sản phụ khoa tổng quát
│   ├── 01_Lac noi mac tu cung - Endometriosis/
│   └── 02_Adenomyosis - Anh huong ART/
├── 02_Ho tro sinh san ART/                ← IVF/ICSI/FET/Andrology
│   ├── 01_MCMA - Song thai 1 buong oi/
│   ├── 02_FET - Frozen Embryo Transfer/
│   ├── 03_AndroGel - Testosterone priming/
│   ├── 04_Bai hoc IVF - 2026-06-12/        (bài cũ)
│   └── 05_DuoStim - Nang ton du/           (bài cũ)
├── 03_Sieu am thai/                       ← Ultrasound sản khoa
│   ├── 01_Sieu am tim thai/
│   └── 02_Bai hoc Fetal/
├── 04_Sieu am tong quat/                  ← Siêu âm bụng tổng quát (người lớn)
│   └── 01_Sieu_am_o_bung_tong_quat/
├── 05_Noi tiet - Hormone/                 ← (để dành - chưa có bài)
├── 06_Vi sinh - Mien dich/                ← (để dành)
├── 07_Ung thu phu khoa/                   ← (để dành)
├── 11_Noi khoa/                            ← Nội khoa người lớn
├── 10_Script Python/                      ← Script build Anki và audit
├── 80_Legacy_by_format/                   ← HTML/APKG/Markdown bài cũ theo format
├── 99_Inbox/                              ← File lẻ/chưa phân loại
└── _duplicates_review/                    ← Bản trùng/rỗng giữ lại để review, không xóa
```

## Quy ước đặt tên file (CẬP NHẬT 27/06)

**Từ bài 20 trở đi, tất cả deliverables của 1 bài học nằm chung 1 folder:**

```
XX_Chuyen_khoa/XX_Ten_bai/
  ├── Ten_bai_YYYY-MM-DD.md                  ← MD source (có dấu)
  ├── Ten_bai_YYYY-MM-DD.cards.v2.json       ← Flashcard JSON
  └── Anki - Ten_bai XX cards - YYYY-MM-DD.apkg  ← Anki deck
```

**Trước đây (bài 1-19)**: Mỗi format nằm 1 folder riêng (`03_Sieu am thai/` cho DOCX, `08_Anki Deck/` cho APKG, `07_Visual/` cho HTML, `09_Source/` cho MD).

**Cập nhật 03/07/2026**: các folder format cũ đã được gom vào `80_Legacy_by_format/`; file lẻ/chưa rõ đưa vào `99_Inbox/`; bản trùng hoặc folder rỗng đưa vào `_duplicates_review/` thay vì xóa.

Tra cứu nhanh bài học bằng `_CATALOG.md`.

## Quy ước dấu tiếng Việt (CẬP NHẬT 22/06)

| Phần | Có dấu? | Lý do |
|---|---|---|
| **Filename + folder** | ❌ KHÔNG | An toàn Windows + PowerShell, không phá cross-reference |
| **Nội dung .md / .apkg** | ✅ **CÓ DẤU ĐẦY ĐỦ** | Bài y khoa cho người Việt, phải đọc tự nhiên |
| **Thuật ngữ y khoa / tên riêng** | ❌ Giữ nguyên Anh/La-tinh | Doppler, ICSI, T21, FIGO, ASPRE, NEJM... |

**Tooling enforce:**
- `10_Script Python\verify_diacritics.py` — scan MD files, ratio ≥ 80% = OK
- `10_Script Python\md_to_docx.py` — legacy parser cho rebuild/xuất lại bài cũ, không dùng cho bài mới
- `10_Script Python\add_diacritics.py` — dictionary mapping cho từ ambiguous (gan→gần, nam→năm...)

## Workflow daily lesson (21h)

Mỗi ngày 21h Mavis sẽ:
1. Tra PubMed evidence 2023-2025 về 1 chủ đề ART / siêu âm thai (luân phiên)
2. Copy `template_lesson.md`, viết bài **CÓ DẤU** + guideline + cơ chế + PMID
3. Chạy `verify_diacritics.py` — đảm bảo ≥ 80% từ tiếng Việt có dấu
4. Build APKG; MD là bài nguồn
5. Citation audit trên MD (BẮT BUỘC 0 BLOCK)
6. Lưu vào folder phân loại tương ứng trong `Bai hoc y khoa/`
7. Gửi qua Telegram kèm media tags

Chi tiết: xem `WORKFLOW.md` ở root.

## Danh sách bài đã build (cập nhật 2026-07-22)

| # | Bài | Ngày | Trạng thái |
|---|---|---|---|
| 1 | Siêu âm tim thai | 13/06 | ✅ |
| 1b | Siêu âm tim thai (siêu chi tiết) | 19/06 | ✅ |
| 2 | Bài học Fetal | 13/06 | ✅ |
| 3 | IVF cơ bản | 12/06 | ✅ |
| 4 | DuoStim (Nang ton du) | 13/06 | ✅ |
| 5 | Song thai MCMA (1 buồng ối) | 13/06 | ✅ |
| 6 | Endometriosis + Endometrioma | 13/06 | ✅ |
| 7 | FET trong Endometriosis | 13/06 | ✅ |
| 8 | AndroGel (Testosterone priming) | 13/06 | ✅ |
| 9 | Adenomyosis ảnh hưởng ART | 13/06 | ✅ |
| 10 | IUI - PUL EP IUP management | 13/06 | ✅ |
| 11 | OHSS - Prevention and Management | 13/06 | ✅ |
| 12 | Endometrial Receptivity ERA | 16/06 | ✅ |
| 13 | Cervical Length - PTB | 17/06 | ✅ |
| 14 | Long GnRH Agonist Protocol | 18/06 | ✅ |
| 15 | Fetal Doppler Ultrasound trong sản khoa | 19/06 | ✅ |
| 16 | ICSI (Intracytoplasmic Sperm Injection) trong IVF | 20/06 | ✅ |
| 17 | First Trimester Screening (11-14w) | 22/06 | ✅ |
| 18 | Sàng lọc & Dự phòng Tiền sản giật (ASPRE) | 22/06 | ✅ |
| 17 | Endometrial Receptivity & Advanced Ultrasound (ERA update, ESHRE 2023, EMT/3D) | 21/06 | ✅ |
| 19 | Luteal Phase Support trong ART (progesterone vaginal/SC/oral/dydrogesterone, GnRHa trigger, NMA 2024-2025) | 22/06 | ✅ |
| 20 | Bất thường nước ối — Thiểu ối & Đa ối (Sinh lý, Siêu âm, Guideline SMFM #46) | 27/06 | ✅ |
| 21 | Các tình huống lâm sàng khi đọc kết quả siêu âm HyCoSy & HyFoSy (8 tình huống + bẫy chẩn đoán) | 28/06 | ✅ |
| 24 | Siêu âm ổ bụng tổng quát — Giải phẫu, mặt cắt, bất thường và quy trình theo 7 tạng (Gan, Túi mật, Tụy, Lách, Thận, Bàng quang, ĐMC) | 28/06 | ✅ |
| 25 | Siêu âm tuyến giáp — Giải phẫu, TI-RADS, bất thường (nốt, Hashimoto, Basedow, K giáp), chỉ định FNA | 28/06 | ✅ |
| 26 | Siêu âm tuyến vú — Giải phẫu, BI-RADS, tổn thương lành/ác, hạch nách, Doppler & Elastography | 28/06 | ✅ |
| 27 | Chuyên đề Hỗ trợ Pha Hoàng Thể (Luteal Phase Support) trong ART — Cập nhật 2026 (PK/PD, FET chuyên sâu, cá thể hóa, PVR, AC-FET safety) | 29/06 | ✅ |
| 28 | Phân tích hình ảnh siêu âm tim thai trong bệnh lý — Chẩn đoán phân biệt & Cơ chế (10 CHD chính: AVSD, TOF, D-TGA, ccTGA, DORV, Truncus, HLHS, CoA/IAA, PA, Ebstein, Vascular Rings) | 30/06 | ✅ |
| 29 | Siêu âm hệ thần kinh thai nhi — Từ cơ bản đến nâng cao: Giải phẫu, Mặt cắt & Bệnh lý (23 sections) | 30/06 | ✅ |
| 30 | Siêu âm hình thái quý 2 toàn diện — Quy trình ISUOG, Kỹ thuật & Checklist từng cơ quan (ISUOG 26-item checklist, sinh trắc, CNS, mặt, tim, bụng, tiết niệu, chi, bánh nhau, dây rốn) | 30/06 | ✅ |
| 31 | Siêu âm Sinh trắc thai — Kỹ thuật đo, Công thức EFW & Biểu đồ tăng trưởng (BPD, HC, AC, FL, Hadlock, INTERGROWTH-21st, WHO, FMF, SGA vs FGR, LGA/macrosomia) | 02/07 | ✅ |
| 32 | Người đáp ứng kém trong IVF — Bologna, POSEIDON và chiến lược kích thích buồng trứng cá thể hóa (low responder, low prognosis, hypo-response, DuoStim/tích lũy noãn, adjuvants) | 02/07 | ✅ |
| 33 | Kỹ thuật siêu âm đầu dò âm đạo cơ bản — cầm đầu dò, định hướng hình ảnh, khảo sát tử cung - phần phụ và checklist báo cáo | 02/07 | ✅ |
| 34 | Các hình ảnh bệnh lý thường gặp trên siêu âm đầu dò âm đạo — tử cung, nội mạc, buồng trứng, phần phụ và túi cùng Douglas | 02/07 | ✅ |
| 35 | Khảo sát mặt thai quý 2 — mặt cắt mũi - môi, profile, ổ mắt, hàm trên và bất thường thường gặp | 02/07 | ✅ |
| 36 | Khảo sát bụng, ruột và thành bụng thai quý 2 — situs, dạ dày, ruột tăng âm, ruột giãn, omphalocele và gastroschisis | 02/07 | ✅ |
| 44 | Siêu âm giải phẫu sớm 13–16 tuần (Early anomaly scan / ECFAS) — checklist, red flags, incomplete pathway, giữ 18–22w | 15/07 | ✅ |
| 57 | IM-01 — Cách tiếp cận bệnh nhân Nội khoa người lớn | 22/07 | ✅ strict PMID/claims, citation 0 BLOCK, foundation profile, diacritics, DOCX và APKG 20 notes/22 cards đã smoke-test |
| 58 | IM-07 — Tiếp cận bệnh nhân khó thở cấp và suy hô hấp | 22/07 | ✅ strict PMID/claims, citation 0 BLOCK, disease depth, diacritics và APKG 36 notes/36 cards đã smoke-test |
| 45 | Đái tháo đường type 1 / type 2 — remediation beginner-first + safety | 16/07 | 📋 strict PMID/claim gate chưa đạt |
| 46 | Siêu âm tim Nội khoa — remediation beginner-first + 80 cards | 16/07 | ✅ DOI, structure và APKG gates đạt |
| 47 | Suy tim cấp và mạn — remediation beginner-first + ICU safety cutover | 17/07 | 📋 strict claim gate còn BLOCK |
| 48 | Hội chứng vành cấp — remediation beginner-first + resource Plan A/B | 17/07 | 📋 strict PMID gate bị HTTP 429 |
| 49 | Bệnh thận mạn (CKD) — remediation beginner-first + APKG 85 cards | 17/07 | 📋 strict claim gate còn BLOCK |
| 50 | Bệnh mạch vành mạn (CCS/CCD) — remediation beginner-first + canonical 80-card deck | 17/07 | 📋 strict PMID/claim gate chưa đạt |
| 51 | Rung nhĩ và nhịp nhanh trên thất — AF/SVT emergency-first + canonical 80-card deck | 18/07 | ✅ strict PMID/claims, citation, structure, diacritics và APKG gates đạt |
| 52 | Nhịp chậm, block nhĩ thất và loạn nhịp thất — pacing/VT emergency-first + canonical 80-card deck | 18/07 | ✅ strict PMID/claims, citation, structure, diacritics và APKG gates đạt |
| 54 | Tiếp cận đau bụng cấp và nôn/tiêu chảy (IM-35) — surgical triage + IDSA diarrhea | 20/07 | ✅ strict PMID/claims, citation, structure, diacritics và APKG gates đạt |
| 55 | Tiêu chảy cấp/mạn và viêm đại tràng (IM-38) — bù dịch, xét nghiệm, kháng sinh, C. difficile, IBD | 20/07 | ✅ strict PMID/claims, citation, structure, diacritics và APKG gates đạt |
| 56 | Bệnh loét dạ dày–tá tràng, GERD và khó tiêu (IM-37) — H. pylori VNAGE, PTMB/PALB, GERD PPI trial, NSAID dự phòng | 20/07 | ✅ strict PMID/claims, citation, depth, diacritics và APKG gates đạt |
| 59 | IM-43 — Đọc creatinine/eGFR và tiếp cận tổn thương thận cấp | 22/07 | ✅ strict PMID/claims, citation 0 BLOCK, disease depth, diacritics, APKG 80 notes/80 cards và learner smoke |
| 60 | [IM-44_Nguyen_ly_ECG_2026-07-28_RELEASE_v1](11_Noi%20khoa/IM-44_Nguyen_ly_ECG/IM-44_Nguyen_ly_ECG_2026-07-28_RELEASE_v1.md) — Nội khoa, foundation | 28/07 | 📋 RE-VERIFICATION REQUIRED |

## Ghi chú

- Tất cả bài có **PMID** (PubMed Identifier) cho mỗi paper tham khảo
- Ưu tiên guideline **ESHRE/ACOG/ASRM/RCOG/ISUOG** cập nhật 2020-2025
- Ngôn ngữ: **tiếng Việt CÓ DẤU** là chính, thuật ngữ y khoa giữ nguyên tiếng Anh/La-tinh
- Format: **dài + chi tiết**, có cơ chế + guideline + PMID + bảng chuẩn
- Output mỗi bài: tác giả soạn thảo Markdown + cards, các artifact DOCX/APKG/learner outputs do release runner tự động tạo khi chạy gate release.
- Theme Anki: **Pastel** (preference user)
- HTML visual: chỉ là deliverable legacy; không tạo cho bài mới.
- Citation audit: BẮT BUỘC 0 BLOCK, guideline > Q1 > Q2 > Q3 > Q4_AVOID

## Tác giả

- Bác sĩ: **Ngọc Hưng 🍅 🐈‍⬛** (Bác sĩ tự học sản phụ khoa, Việt Nam)
- AI assistant: **tên model hiện tại** (trước đây MiniMax Mavis, hiện tại opencode deepseek-v4-pro)
- Workspace gốc: `F:\DL\solieu thay H\Bai hoc y khoa\`

### IM-44: Nguyên lý ECG và nguyên lý hiển thị hình ảnh sóng ECG (RELEASE_v2)
- **Folder:** `11_Noi khoa/IM-44_Nguyen_ly_ECG/`
- **Revision:** `IM-44_Nguyen_ly_ECG_2026-07-29_RELEASE_v2`
- **Profile:** `foundation` | **Mode:** `L3_BEGINNER`
- **Status:** ✅ PUBLISH READY (16/16 required gates PASS)
