# RESEARCH BRIEF — PART 04: DƯỢC LÝ & PHÁC ĐỒ ĐIỀU TRỊ CỤ THỂ THEO PHÂN THỂ
**Dự án:** Bài học y khoa Mavis (IM-IBS Hội chứng Ruột kích thích)  
**Mã bài:** Part 04 — `Part_04_Duoc_ly_dieu_tri_theo_Phan_the.md`  
**Trạng thái verification:** Tier 1 Complete (NCBI E-utilities verified abstracts)  
**Ngày lập:** 2026-07-26  

---

## 1. BẢNG KHÓA NGUỒN TÀI LIỆU & PMIDS ĐÃ VERIFY (0 HALLUCINATION)

| PMID | Tác giả & Tạp chí | Năm | Tiêu đề paper | Cấp độ chứng cứ | Vai trò trích dẫn |
|---|---|---|---|---|---|
| **33315591** | Lacy BE et al. (*Am J Gastroenterol*) | 2021 | ACG Clinical Guideline: Management of Irritable Bowel Syndrome | **ACG Guideline** | Khuyến cáo Rifaximin (IBS-D), Chloride channel (Lubiprostone) & Guanylate cyclase activators (Linaclotide cho IBS-C), TCAs |
| **34553347** | von Schassen H et al. (*Dtsch Med Wochenschr*) | 2021 | The new guideline on irritable bowel syndrome: what is new? | **Guideline Review** | Thuốc chống co thắt (Peppermint oil, Mebeverine), Macrogol (PEG) cho IBS-C, Neuromodulators cho đau quặn |

---

## 2. BẢNG CLAIMS & SỐ LIỆU ĐÃ VERIFY (STRICT CONTRACT FOR EXECUTION)

| # | Khái niệm / Claim | Dữ liệu & Số liệu đã verify | PMID đính kèm | Annotation Tag |
|---|---|---|---|---|
| 1 | **Rifaximin cho IBS thể Tiêu chảy (IBS-D)** | Khuyến cáo dùng Rifaximin (kháng sinh không hấp thu) để điều trị IBS-D toàn thân. | **33315591** | `[GUIDELINE VERIFIED]` |
| 2 | **Linaclotide & Lubiprostone cho IBS thể Táo bón (IBS-C)** | Khuyến cáo dùng các chất kích hoạt kênh Chloride (Lubiprostone) và kích hoạt Guanylate Cyclase (Linaclotide) cho IBS-C. | **33315591** | `[GUIDELINE VERIFIED]` |
| 3 | **Thuốc Chống co thắt (Spasmolytics)** | Thuốc chống co thắt (Mebeverine, Alverine, Peppermint oil) giúp cải thiện đau quặn bụng ở mọi thể IBS. | **34553347** | `[GUIDELINE VERIFIED]` |
| 4 | **Neuromodulators (TCA vs SSRI)** | Thuốc chống trầm cảm 3 vòng (TCA - Amitriptyline) giảm đau bụng tạng và làm chậm nhu động (tốt cho IBS-D); SSRI làm tăng nhu động (tốt cho IBS-C). | **34553347** | `[GUIDELINE VERIFIED]` |

---

## 3. HƯỚNG DẪN DÀNH CHO MODEL EXECUTE (TẦNG 2)
1. Viết Part 04 chi tiết, phân chia nhóm thuốc rõ ràng theo 3 thể lâm sàng: IBS-D, IBS-C và Đau quặn bụng.
2. Trình bày chi tiết cơ chế phân tử, liều dùng, đường dùng và chống chỉ định của từng nhóm thuốc.
3. Không tự thêm PMID giả ngoài Brief.
