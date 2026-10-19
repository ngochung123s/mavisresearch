# 12. Nhi khoa — Kho bài giảng & Ca lâm sàng (Core 45)

Thư mục chứa các bài học Nhi khoa thực chiến, bám sát khung **Core 45** tại `_CURRICULUM_NHI_KHOA.md`.

> **Quy tắc canonical build bài/thẻ/APKG (mọi chuyên khoa, gồm Nhi khoa): [`../RULES_LESSON_APKG.md`](../RULES_LESSON_APKG.md)**. Mỗi bài có `lesson.json`; lock Anki là `anki_lock.json`. Phát hành bằng `release_lesson.py`.

## Các folder block hiện có

- **`00_Nen_tang_va_Tiep_can`**: Block 0 — nền tảng, tiếp cận & dược lý. Chứa PED-01, PED-02 (+ `PED-02b_…nghiem_phap_nhi_khoa.md`), PED-03, **PED-63** (công thức bạch cầu theo tuổi) và thư mục `sources/`.
- **`01_Hoi_suc_Cap_cuu_Ngo_doc`**: Block 1 — hồi sức, cấp cứu & ngộ độc. Chứa PED-07, PED-11, PED-50, PED-52.
- **`02_So_sinh_hoc`**: Block 2 — sơ sinh học. Chứa PED-13 – PED-17.
- **`03_Ho_hap`**: Block 3 — hô hấp. Chứa PED-20, 21, 22, 24, 25, 56, 58, 59, 62 và 1 biểu mẫu hỏi bệnh/khám thực thể hô hấp (`.md`). **Đây là block hô hấp chính theo curriculum.**
- **`04_Tieu_hoa_va_Dinh_duong`**: Block 4 — tiêu hóa & dinh dưỡng. Chứa PED-27, 30, 46, 55, 60, 61 và các cẩm nang/phiếu khám dinh dưỡng rời (`.html`/`.pdf`/`.md`).
- **`05_Truyen_nhiem`**: Block 5 — truyền nhiễm. Chứa PED-32, 35, 37, 49, 53, 54, 57.
- **`06_Than_Tim_mach_Noi_tiet`**: Block 6 — thận, tim mạch, huyết học & nội tiết. Chứa PED-40, 43, 47, 48, 51.

### Folder nghi trùng / cần hợp nhất (chưa di chuyển gì)

- **`02_Ho_hap`** — **cần hợp nhất** vào `03_Ho_hap`: không có folder `PED-xx`, chỉ chứa tài liệu rời về hô hấp (cẩm nang viêm phế quản / viêm phổi / Zero-Omission, infographic RSV & cúm A, `.md` về RSV–cúm A và viêm tai giữa cấp). Cùng chuyên khoa với Block 3 và đánh số trùng tiền tố `02_` với `02_So_sinh_hoc`.
- **`01_Dai_cuong_va_Kham_Nhi`** — **cần hợp nhất / xếp lại**: chỉ có 1 hướng dẫn khai thác tiền sử tiêm chủng trẻ em (`.html` + `.pdf`), không có bài PED; nội dung thuộc nhóm nền tảng/tiếp cận → ứng viên chuyển sang `00_Nen_tang_va_Tiep_can`. Trùng tiền tố `01_` với `01_Hoi_suc_Cap_cuu_Ngo_doc`.

Ngoài các block còn có bộ PedViewer ở root (`index.html`, `app.html`, `mobile.html`, `checklist.html`, `data.js`, `CATALOG_PED_VIEWER.json`, `build_ped_library.py`, `build_unified_med_library.py`, `build_master_ped_decks.py`, cấu hình Netlify). PedViewer chỉ đọc file ở **root folder bài** và bỏ qua `outputs/`.

## Cấu trúc lưu trữ mỗi bài (theo `RULES_LESSON_APKG.md` §3)

```text
12_Nhi khoa/<Block>/PED-XX_<Ten_khong_dau>/
├── PED-XX_<Ten>_<YYYY-MM-DD>_RELEASE_vN.md   # bài Track 2 / master (nội dung có dấu)
├── PED-XX_<Ten>_PEDYTB.md                    # barem Track 1 (nếu có)
├── pedXX_cards_data.py                       # NGUỒN DUY NHẤT của thẻ (list cards_data)
├── lesson.json                               # spec bài/deck
├── anki_lock.json                            # sinh tự động: GUID + Anki note id cố định
├── <basename>.cards.v2.json                  # sinh tự động (PedViewer đọc)
├── <basename>.apkg                           # sinh tự động — đúng 1 APKG/bài
└── outputs/
    ├── figures/                              # ảnh đã nén (≤150 KB, ≤1200 px)
    ├── visual_evidence/                      # ảnh bằng chứng Gate 2
    └── verification/<basename>/card-lint.json
```

- Đúng 1 APKG + 1 `cards.v2.json` ở root folder bài; bản cũ/trùng chuyển vào `Bai hoc y khoa/_duplicates_review/`.
- Build bằng `python "10_Script Python/release_lesson.py" <lesson_dir> --mode release [--sync-anki]` (→ `deck_builder.py`); deck theo `RULES_LESSON_APKG.md` §1 (`Nhi khoa Y6::PED-xx: <Tên có dấu>`, bản EBM: ` (EBM Update)`).
- Filename/folder không dấu; nội dung và tên deck có dấu.
- Một số bài cũ chưa chuyển sang cấu trúc này (ví dụ `.md` rời trong block) — theo dõi trạng thái trong `_CURRICULUM_NHI_KHOA.md`.
