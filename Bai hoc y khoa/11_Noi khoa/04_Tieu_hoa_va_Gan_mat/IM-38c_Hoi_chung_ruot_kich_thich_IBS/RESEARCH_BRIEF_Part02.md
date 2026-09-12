# RESEARCH BRIEF — PART 02: CHẨN ĐOÁN & PHÂN LOẠI THEO TIÊU CHUẨN ROME IV
**Dự án:** Bài học y khoa Mavis (IM-IBS Hội chứng Ruột kích thích)  
**Mã bài:** Part 02 — `Part_02_Tieu_chuan_Rome_IV_va_Phan_the.md`  
**Trạng thái verification:** Tier 1 Complete (NCBI E-utilities verified abstracts)  
**Ngày lập:** 2026-07-26  

---

## 1. BẢNG KHÓA NGUỒN TÀI LIỆU & PMIDS ĐÃ VERIFY (0 HALLUCINATION)

| PMID | Tác giả & Tạp chí | Năm | Tiêu đề paper | Cấp độ chứng cứ | Vai trò trích dẫn |
|---|---|---|---|---|---|
| **33315591** | Lacy BE et al. (*Am J Gastroenterol*) | 2021 | ACG Clinical Guideline: Management of Irritable Bowel Syndrome | **ACG Guideline** | Tiêu chuẩn chẩn đoán dương tính, Celiac, Calprotectin, loại trừ IBD |
| **33049221** | Black CJ et al. (*Lancet*) | 2020 | Functional gastrointestinal disorders: advances in understanding and management | **Consensus (Rome IV)** | Tiêu chuẩn Rome IV, phân thể IBS-C, IBS-D, IBS-M |
| **35125827** | Hillestad EMR et al. (*World J Gastroenterol*) | 2022 | The microbiota-gut-brain axis in irritable bowel syndrome | **Review** | Thang điểm phân Bristol Stool Chart |

---

## 2. BẢNG CLAIMS & SỐ LIỆU ĐÃ VERIFY (STRICT CONTRACT FOR EXECUTION)

| # | Khái niệm / Claim | Dữ liệu & Số liệu đã verify | PMID đính kèm | Annotation Tag |
|---|---|---|---|---|
| 1 | **Chiến lược chẩn đoán dương tính (Positive Diagnostic Strategy)** | Khuyến cáo dùng chiến lược chẩn đoán dương tính (dựa vào tiêu chuẩn lâm sàng) thay vì chẩn đoán loại trừ tràn lan để rút ngắn thời gian điều trị. | **33315591** | `[GUIDELINE VERIFIED]` |
| 2 | **Tiêu chuẩn Rome IV cho IBS** | Đau bụng trung bình $\ge 1$ ngày/tuần trong 3 tháng gần nhất, khởi phát triệu chứng $\ge 6$ tháng trước, kèm $\ge 2$ trong 3 tiêu chí: (1) Liên quan đi tiêu, (2) Thay đổi tần suất phân, (3) Thay đổi hình dạng phân. | **33049221** | `[GUIDELINE VERIFIED]` |
| 3 | **Phân thể theo Thang Bristol Stool Chart** | IBS-D ($>25\%$ phân Bristol 5-7, $<25\%$ Bristol 1-2); IBS-C ($>25\%$ Bristol 1-2, $<25\%$ Bristol 5-7); IBS-M ($>25\%$ Bristol 1-2 VÀ $>25\%$ Bristol 5-7). | **33049221** | `[GUIDELINE VERIFIED]` |
| 4 | **Loại trừ Bệnh Celiac** | Khuyến cáo làm xét nghiệm huyết thanh (tTG-IgA) để loại trừ Celiac ở bệnh nhân IBS có triệu chứng tiêu chảy. | **33315591** | `[GUIDELINE VERIFIED]` |
| 5 | **Loại trừ Bệnh Viêm Ruột Mạn (IBD)** | Khuyến cáo đo **Fecal Calprotectin** (hoặc CRP) ở bệnh nhân nghi ngờ IBS-D để phân biệt với IBD. | **33315591** | `[GUIDELINE VERIFIED]` |

---

## 3. HƯỚNG DẪN DÀNH CHO MODEL EXECUTE (TẦNG 2)
1. Viết bài Part 02 chi tiết, dạy từ gốc, áp dụng bảng phân loại Bristol kèm mô tả tiếng Việt dễ hiểu.
2. Nêu rõ các Dấu hiệu Báo động (Red Flags) bắt buộc phải cho nội soi.
3. Không tự thêm PMID giả ngoài Brief.
