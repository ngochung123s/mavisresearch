# RESEARCH BRIEF — PART 01: TỔNG QUAN & SINH LÝ BỆNH TRỤC NÃO - RUỘT TRONG IBS
**Dự án:** Bài học y khoa Mavis (IM-IBS Hội chứng Ruột kích thích)  
**Mã bài:** Part 01 — `Part_01_Tong_quan_va_Co_che_Truc_Nao_Ruot.md`  
**Trạng thái verification:** Tier 1 Complete (NCBI E-utilities verified abstracts)  
**Ngày lập:** 2026-07-26  

---

## 1. BẢNG KHÓA NGUỒN TÀI LIỆU & PMIDS ĐÃ VERIFY (0 HALLUCINATION)

| PMID | Tác giả & Tạp chí | Năm | Tiêu đề paper | Cấp độ chứng cứ | Vai trò trích dẫn |
|---|---|---|---|---|---|
| **33049221** | Black CJ et al. (*Lancet*) | 2020 | Functional gastrointestinal disorders: advances in understanding and management | **Consensus (Rome IV)** | Định nghĩa DGBI, mô hình biopsychosocial, dịch tễ 40% dân số |
| **33493503** | Margolis KG et al. (*Gastroenterology*) | 2021 | The Microbiota-Gut-Brain Axis: From Motility to Mood | **Expert Review** | Trục não-ruột-vi sinh, vai trò của Serotonin (5-HT) |
| **35125827** | Hillestad EMR et al. (*World J Gastroenterol*) | 2022 | Gut bless you: The microbiota-gut-brain axis in irritable bowel syndrome | **Systematic Review** | Biến đổi hệ vi sinh, tính thấm niêm mạc, phản ứng với Low-FODMAP |
| **34631603** | Xiao L et al. (*Front Cell Infect Microbiol*) | 2021 | Gut Microbiota-Derived Metabolites in Irritable Bowel Syndrome | **Review** | Chuyển hóa vi sinh: Axit béo chuỗi ngắn (SCFA), Axit mật, Serotonin |
| **33023902** | Perna E et al. (*Gut*) | 2021 | Effect of resolvins on sensitisation of TRPV1 and visceral hypersensitivity in IBS | **Basic/Clinical Study** | Nhạy cảm thần kinh ruột, thụ thể TRPV1, histamine, IBS sau nhiễm trùng |
| **37096434** | Lee A et al. (*Korean J Gastroenterol*) | 2023 | Brain-Gut-Microbiota Axis | **Review** | Tương tác 2 chiều: thần kinh, miễn dịch, nội tiết giữa não và ruột |
| **34430628** | Tang HY et al. (*Ann Transl Med*) | 2021 | Uncovering the pathophysiology of irritable bowel syndrome by exploring the gut-brain axis | **Review** | Đa yếu tố sinh lý bệnh: Nhu động, nhạy cảm tạng, viêm mức độ thấp |

---

## 2. BẢNG CLAIMS & SỐ LIỆU ĐÃ VERIFY (STRICT CONTRACT FOR EXECUTION)

> **Mô tả contract:** Model execute (Tầng 2) CHỈ ĐƯỢC DÙNG các claim và số liệu trong bảng này. Tuyệt đối KHÔNG tự bịa số %, KHÔNG thêm PMID ngoài bảng.

| # | Khái niệm / Claim | Dữ liệu & Số liệu đã verify | PMID đính kèm | Annotation Tag |
|---|---|---|---|---|
| 1 | **Tên gọi mới của rối loạn chức năng tiêu hóa** | Khái niệm "Functional GI disorders" được đổi thành "Disorders of Gut-Brain Interaction" (DGBIs - Rối loạn tương tác Não - Ruột). | **33049221** | `[GUIDELINE VERIFIED]` |
| 2 | **Tỷ lệ mắc DGBIs toàn cầu** | DGBIs ảnh hưởng đến **tới 40% dân số** tại một thời điểm; **2/3 bệnh nhân** có triệu chứng mạn tính, dao động. | **33049221** | `[FULL VERIFIED]` |
| 3 | **Bản chất 2 chiều của Trục Não - Ruột** | Tương tác 2 chiều (bidirectional dysregulation): Não tác động lên nhu động, tiết dịch và miễn dịch ruột; Hệ vi sinh & ruột tác động lên não bộ và cảm xúc qua thần kinh, nội tiết, miễn dịch. | **33493503**, **37096434** | `[ABSTRACT VERIFIED]` |
| 4 | **Tương quan Serotonin (5-HT)** | 95% Serotonin của cơ thể được tổng hợp và lưu trữ tại đường tiêu hóa (tế bào enterochromaffin). Serotonin điều hòa cả nhu động ruột và tâm trạng tại thần kinh trung ương. | **33493503** | `[ABSTRACT VERIFIED]` |
| 5 | **Tăng nhạy cảm tạng (Visceral Hypersensitivity)** | Thụ thể TRPV1 trên sợi thần kinh cảm giác ruột bị nhạy cảm hóa bởi Histamine và chất trung gian viêm nhẹ $\rightarrow$ Hạ thấp ngưỡng chịu đau (Colorectal distention). | **33023902** | `[ABSTRACT VERIFIED]` |
| 6 | **Sản phẩm chuyển hóa hệ vi sinh (Metabolites)** | Axit béo chuỗi ngắn (SCFA), Axit mật (Bile acids) và Serotonin bị rối loạn chuyển hóa $\rightarrow$ Gây thay đổi tính thấm niêm mạc và kích thích thần kinh ruột. | **34631603** | `[ABSTRACT VERIFIED]` |
| 7 | **IBS sau nhiễm trùng (Post-Infectious IBS - PI-IBS)** | Phát triển sau một đợt viêm dạ dày-ruột cấp tính; đặc trưng bởi viêm mức độ thấp dai dẳng, tăng tính thấm niêm mạc và nhạy cảm hóa thụ thể TRPV1. | **33023902**, **34430628** | `[ABSTRACT VERIFIED]` |

---

## 3. DÀN Ý CHI TIẾT DẠY TỪ GỐC FOR PART 01

### Phần 0: Tổng quan — Từ "Rối loạn chức năng" đến "Rối loạn tương tác Não - Ruột"
- Định nghĩa lại IBS theo Rome IV (DGBI).
- Tại sao không còn gọi là "bệnh giả vờ" hay "chức năng thuần túy"?

### Phần 1: Nền tảng Giải phẫu & Sinh lý Trục Não - Ruột (Brain-Gut Axis)
- **Hệ thần kinh ruột (ENS - Enteric Nervous System):** "Bộ não thứ hai" chứa 2 đám rối (Meissner & Auerbach).
- **Đường truyền 2 chiều:** Dây thần kinh phế vị (Vagus - 80% sợi hướng tâm), trục HPA (Hypothalamic-Pituitary-Adrenal), hệ miễn dịch ruột (GALT).
- **Serotonin (5-HT):** Vai trò của tế bào Enterochromaffin (EC), thụ thể 5-HT3 và 5-HT4 trong vận động và cảm giác đau ruột.

### Phần 2: Đa cơ chế Sinh lý bệnh trong IBS (Multifactorial Pathophysiology)
1. **Rối loạn điều hòa Trục Não - Ruột & Stress:** Stress kích hoạt HPA $\rightarrow$ Giải phóng CRH $\rightarrow$ Tăng tính thấm ruột & thay đổi nhu động.
2. **Tăng nhạy cảm tạng (Visceral Hypersensitivity):** Vai trò của thụ thể TRPV1 và sự nhạy cảm hóa thần kinh cảm giác (Hyperalgesia).
3. **Mất cân bằng Hệ vi sinh (Microbial Dysbiosis) & Metabolites:** Rối loạn SCFA, Axit mật và sản phẩm chuyển hóa vi sinh.
4. **Viêm mức độ thấp & IBS sau nhiễm trùng (Post-Infectious IBS):** Sự kích hoạt tế bào Mast (Mast cells) và tăng giải phóng Histamine sau đợt nhiễm trùng ruột.
5. **Rối loạn tính thấm niêm mạc (Gut Permeability):** "Gut leakiness" và sự xâm nhập của dị nguyên/độc tố.

### Phần 3: Phân tích Thực chiến tại Việt Nam (Thiếu Nguồn Lực / Plan B)
- Giải thích vì sao ở Việt Nam bệnh nhân IBS hay bị chẩn đoán nhầm thành "Viêm đại tràng mạn" và cho kháng sinh kéo dài vô ích.
- Tiếp cận giải thích cho bệnh nhân hiểu về Trục Não - Ruột để giải tỏa tâm lý lo âu.

---

## 4. HƯỚNG DẪN DÀNH CHO MODEL EXECUTE (TẦNG 2)
1. Tuân thủ chuẩn `template_lesson.md`: Dạy từ gốc, không giới hạn độ dài, giải thích nhân quả 5 tầng.
2. Dùng đúng các PMID và claims đã verify trong bảng trên.
3. Không tự thêm PMID giả hoặc số liệu % ngoài Brief.
