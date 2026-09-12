# RESEARCH BRIEF — PART 06: MASTER CLINICAL CASES & POCKET GUIDE
**Dự án:** Bài học y khoa Mavis (IM-IBS Hội chứng Ruột kích thích)  
**Mã bài:** Part 06 — `QA-IBS_Master_Cases_va_Pocket_Guide.md`  
**Trạng thái verification:** Tier 1 Complete (NCBI E-utilities verified abstracts)  
**Ngày lập:** 2026-07-26  

---

## 1. BẢNG KHÓA NGUỒN TÀI LIỆU & PMIDS ĐÃ VERIFY (0 HALLUCINATION)

| PMID | Tác giả & Tạp chí | Năm | Tiêu đề paper | Cấp độ chứng cứ | Vai trò trích dẫn |
|---|---|---|---|---|---|
| **33315591** | Lacy BE et al. (*Am J Gastroenterol*) | 2021 | ACG Clinical Guideline: Management of Irritable Bowel Syndrome | **ACG Guideline** | Phác đồ điều trị IBS-D (Rifaximin), IBS-C (Linaclotide), Psyllium, Low-FODMAP |
| **33049221** | Black CJ et al. (*Lancet*) | 2020 | Functional gastrointestinal disorders: advances in understanding and management | **Consensus (Rome IV)** | Tiêu chuẩn Rome IV, phân thể IBS, mô hình Biopsychosocial |
| **34553347** | von Schassen H et al. (*Dtsch Med Wochenschr*) | 2021 | The new guideline on irritable bowel syndrome: what is new? | **Guideline Review** | Neuromodulators (Amitriptyline liều thấp), Spasmolytics (Mebeverine) |
| **33023902** | Perna E et al. (*Gut*) | 2021 | Effect of resolvins on sensitisation of TRPV1 and visceral hypersensitivity in IBS | **Basic/Clinical Study** | Nhạy cảm tạng, Post-Infectious IBS |

---

## 2. BẢNG CLAIMS & SỐ LIỆU ĐÃ VERIFY (STRICT CONTRACT FOR EXECUTION)

| # | Khái niệm / Claim | Dữ liệu & Số liệu đã verify | PMID đính kèm | Annotation Tag |
|---|---|---|---|---|
| 1 | **Xử trí Ca 1: IBS-D thất bại với Loperamide** | Rifaximin 550mg x 3 lần/ngày (14 ngày) kết hợp Amitriptyline 10-25mg giúp giảm tiêu chảy và đau quặn bụng. | **33315591** | `[GUIDELINE VERIFIED]` |
| 2 | **Xử trí Ca 2: IBS-C trướng bụng mạn tính** | Đổi xơ không hòa tan sang Psyllium 5-10g/ngày + PEG 3350 17g/ngày $\rightarrow$ Linaclotide nếu không đáp ứng. | **33315591** | `[GUIDELINE VERIFIED]` |
| 3 | **Xử trí Ca 3: Post-Infectious IBS (IBS sau nhiễm trùng)** | Khởi phát sau ngộ độc ăn uống; điều trị bằng Mebeverine + Neuromodulator, tránh dùng lại kháng sinh phổ rộng. | **33023902**, **34553347** | `[ABSTRACT VERIFIED]` |
| 4 | **Xử trí Ca 4: IBS có Red Flags (Báo động)** | Tiêu chảy đêm + sụt cân ở người 52t $\rightarrow$ Bắt buộc nội soi đại tràng phát hiện IBD/Ung thư. | **33315591** | `[GUIDELINE VERIFIED]` |

---

## 3. HƯỚNG DẪN DÀNH CHO MODEL EXECUTE (TẦNG 2)
1. Viết file QA Master Clinical Cases gồm 4 ca lâm sàng thực tế với lời giải tỉ mỉ, biện luận từng bước.
2. Cung cấp Bảng Tổng hợp Pocket Guide toàn bộ Chuyên đề IBS.
3. Không tự thêm PMID giả ngoài Brief.
