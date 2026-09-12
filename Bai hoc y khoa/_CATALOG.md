# Catalog - Bài học Y khoa (Workspace Catalog)
**Cập nhật chuẩn hóa:** 2026-08-30 (Chuẩn hóa toàn bộ mã số tiền tố IM-XX và Block chuyên khoa)

---

## 1. PHÂN LOẠI CHUYÊN KHOA LỚN (LEVEL 1)

| Mã chuyên khoa | Tên chuyên khoa lớn | Đường dẫn thư mục | Nội dung trọng tâm |
|:---:|:---|:---|:---|
| **00** | **Tổng hợp & Thư viện** | `00_Tong hop/` | Tài liệu y văn, library nền tảng |
| **01** | **Sản phụ khoa tổng quát** | `01_San phu khoa/` | Chuyển dạ, tiền sản giật, GDM, AUB, u xơ, Asherman |
| **02** | **Hỗ trợ sinh sản (ART/IVF)** | `02_Ho tro sinh san ART/` | IVF/ICSI, kích trứng, FET, OHSS, PGT, ERA, HyCoSy |
| **03** | **Siêu âm thai (Fetal US)** | `03_Sieu am thai/` | Siêu âm hình thái thai, Doppler thai, tim thai, não thai |
| **04** | **Siêu âm tổng quát** | `04_Sieu am tong quat/` | Siêu âm bụng tổng quát, tuyến giáp, tuyến vú |
| **05** | **Vi sinh & Miễn dịch** | `05_Vi sinh - Mien dich/` | Viêm âm đạo, HPV, bệnh lý nhiễm trùng |
| **06** | **Ung thư phụ khoa** | `06_Ung thu phu khoa/` | Ung thư cổ tử cung, buồng trứng, nội mạc |
| **10** | **Scripts Python & Toolchain** | `10_Script Python/` | Bộ công cụ build APKG, verify diacritics, citation audit |
| **11** | **Nội khoa người lớn** | `11_Noi khoa/` | Chương trình 100 bài Nội khoa phân theo 13 Block chuẩn |

---

## 2. BẢNG MÃ SỐ CHUẨN HÓA CÁC BÀI HỌC TRONG 11_NOI KHOA (LEVEL 2)

```text
F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\
├── 📁 00_Nen_tang_va_Kham_xet_nghiem/
│   ├── IM-01_Tiep_can_benh_nhan_noi_khoa
│   ├── IM-04_Huong_dan_doc_xet_nghiem_mau_co_ban
│   ├── IM-05_Sinh_ly_va_nguyen_ly_tao_anh_ECG
│   └── IM-05b_Nguyen_ly_ECG (trước đây là IM-44 ECG, đã chuẩn hóa để tránh trùng IM-44 CKD)
│
├── 📁 01_Cap_cuu_va_Hoi_chung_cap/
│   ├── IM-07_Tiep_can_kho_tho_cap
│   ├── IM-14_Roi_loan_duong_huyet_cap_15_phut_dau
│   ├── IM-15_Tang_huyet_ap_cap_cuu
│   └── IM-16_Xuat_huyet_tieu_hoa_cap
│
├── 📁 02_Tim_mach/
│   ├── IM-19_Sieu_am_tim_noi_khoa
│   ├── IM-20_Tang_huyet_ap
│   ├── IM-20_QA_Tang_huyet_ap
│   ├── IM-20a_Benh_mach_vanh_man
│   ├── IM-21_Hoi_chung_vanh_cap
│   ├── IM-22_Suy_tim
│   ├── IM-23_Rung_nhi_va_nhip_nhanh_tren_that
│   ├── IM-23b_Cac_roi_loan_nhip_tim
│   └── IM-24_Nhip_cham_block_nhi_that_va_loan_nhip_that
│
├── 📁 03_Ho_hap/
│   ├── IM-29_Hen_phe_quan
│   ├── IM-30_COPD
│   └── IM-34a_Tam_phe_man
│
├── 📁 04_Tieu_hoa_va_Gan_mat/
│   ├── IM-35_Tiep_can_dau_bung_cap
│   ├── IM-36_Xuat_huyet_tieu_hoa_sau_hoi_suc
│   ├── IM-37_Loet_da_day_ta_trang_GERD_kho_tieu
│   ├── IM-37_QA_H_pylori_dieu_tri
│   ├── IM-38_Tieu_chay_va_viem_dai_trang
│   ├── IM-38b_Benh_Viem_Ruot_Man_IBD
│   ├── IM-38c_Hoi_chung_ruot_kich_thich_IBS
│   ├── IM-40_Xo_gan_tang_ap_cua
│   ├── IM-40_QA_Transamin_LOLA_HE
│   ├── IM-42_Viem_tuy_cap_benh_tui_mat_duong_mat
│   └── IM-42a_Viem_tuy_cap
│
├── 📁 05_Than_va_Roi_loan_dien_giai/
│   ├── IM-43_Doc_creatinine_eGFR_va_tiep_can_ton_thuong_than_cap
│   ├── IM-43a_Sinh_ly_nephron
│   ├── IM-43b_Thuoc_loi_tieu
│   ├── IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu
│   ├── IM-43c_QA_BUN_Blood_Urea_Nitrogen
│   ├── IM-44_Benh_than_man
│   └── IM-47_Roi_loan_toan_kiem_va_doc_khi_mau_dong_mach
│
├── 📁 06_Noi_tiet_va_Chuyen_hoa/
│   ├── IM-51_Dai_thao_duong
│   ├── IM-53_Suy_giap
│   ├── IM-53b_Buou_giap_don_thuan
│   ├── IM-54_Hoi_chung_Cushing
│   ├── IM-54b_Suy_tuyen_thuong_than
│   ├── IM-56_Roi_loan_lipid_mau
│   └── IM-57_Chuyen_hoa_xuong_vitamin_D_va_loang_xuong
│
├── 📁 08_Huyet_hoc_va_Dong_mau/
│   └── IM-69_XN_dong_mau_PT_aPTT_Fibrinogen
│
└── 📁 10_Co_xuong_khop/
    └── IM-82_Gout_va_tang_acid_uric
```

---

## 3. ĐỒNG BỘ MÃ SỐ TRONG TỪNG FILE MARKDOWN & FLASHCARD
* 100% các file bài học `.md` đều đã được gắn đúng tiêu đề mã số `IM-XX` ở dòng đầu (`**Mã bài học:** IM-XX`).
* 100% các bộ thẻ Anki `.cards.v2.json` đều được gắn tag định danh `extra` chứa đúng mã bài học `IM-XX`.
* File `_CURRICULUM_NOI_KHOA.md` và `_CATALOG.md` đã hoàn toàn đồng nhất với cây thư mục thực tế.
