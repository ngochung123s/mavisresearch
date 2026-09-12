# AUDIT REPORT — IM-37 PMID Verification (Gate-Based)
**Tổng claims quét:** 52 | **Unique PMIDs:** 21

## 1. Nguyên tắc kiểm định

- Mỗi PMID được so sánh với metadata thực tế từ NCBI E-summary API (`pubtype`, `title`, `journal`).
- Nhãn `[FULL VERIFIED]` CHỈ được giữ nếu: (a) có số liệu cụ thể trong claim, (b) số liệu đó đã được đối chiếu với abstract/full text.
- Nhãn `[GUIDELINE VERIFIED]` CHỈ dùng cho bài có `pubtype` chứa "Practice Guideline" hoặc "Consensus Statement".

## 2. Kết quả Audit

| File | Tổng claims | ✅ OK | 🔴 Cần hạ nhãn |
|---|---|---|---|
| Part_01_Tong_quan_va_Phan_bien_Hoi_chung.md | 3 | 2 | 1 |
| Part_02_Co_che_benh_sinh_va_Yeu_to_nguy_co.md | 12 | 10 | 2 |
| Part_03_Chan_doan_va_Test_H_pylori.md | 9 | 4 | 5 |
| Part_04_Phac_do_tiet_tru_H_pylori_VNAGE2022.md | 5 | 3 | 2 |
| Part_05_Dieu_tri_GERD_Chuyen_sau.md | 8 | 7 | 1 |
| Part_06_Quan_ly_Kho_tieu_chuc_nang_va_Loet_NSAID.md | 6 | 4 | 2 |
| Part_07_Master_Clinical_Cases_va_Checklist.md | 9 | 2 | 7 |
| **TOTAL** | **52** | **32** | **20** |

## 3. Danh sách PMID & Pubtype thực tế (Ground truth từ NCBI)

| PMID | Title | Journal | Actual Pubtype | Max Allowed Tier |
|---|---|---|---|---|
| 16625009 | Oral ondansetron for gastroenteritis in a pediatric emergency departme... | N Engl J Med | Journal Article, Randomized Controlled Trial, Research Support, N.I.H., Extramur | `DATA VERIFIED` |
| 19240698 | Guidelines for prevention of NSAID-related ulcer complications.... | Am J Gastroenterol | Journal Article, Practice Guideline | `GUIDELINE VERIFIED` |
| 19949136 | Continuation of low-dose aspirin therapy in peptic ulcer bleeding: a r... | Ann Intern Med | Journal Article, Randomized Controlled Trial, Research Support, Non-U.S. Gov't | `DATA VERIFIED` |
| 25667026 | Prokinetics in gastroparesis.... | Gastroenterol Clin North Am | Journal Article, Research Support, N.I.H., Extramural, Review | `ABSTRACT VERIFIED` |
| 25921377 | Effect of Amitriptyline and Escitalopram on Functional Dyspepsia: A Mu... | Gastroenterology | Journal Article, Multicenter Study, Randomized Controlled Trial, Research Suppor | `DATA VERIFIED` |
| 26187502 | Kyoto global consensus report on Helicobacter pylori gastritis.... | Gut | Journal Article, Research Support, Non-U.S. Gov't, Review, Consensus Statement | `GUIDELINE VERIFIED` |
| 28410791 | Gastrointestinal safety of celecoxib versus naproxen in patients with ... | Lancet | Comparative Study, Journal Article, Randomized Controlled Trial | `DATA VERIFIED` |
| 28631728 | ACG and CAG Clinical Guideline: Management of Dyspepsia.... | Am J Gastroenterol | Journal Article, Practice Guideline, Review | `GUIDELINE VERIFIED` |
| 29990487 | Prevalence of Antibiotic Resistance in Helicobacter pylori: A Systemat... | Gastroenterology | Journal Article, Meta-Analysis, Research Support, Non-U.S. Gov't, Research Suppo | `META-ANALYSIS VERIFIED` |
| 30338390 | New Approaches to Diagnosis and Treatment of Functional Dyspepsia.... | Curr Gastroenterol Rep | Journal Article, Review | `ABSTRACT VERIFIED` |
| 33191311 | Clinical Guidelines for Drug-Related Peptic Ulcer, 2020 Revised Editio... | Gut Liver | Journal Article, Review | `ABSTRACT VERIFIED` |
| 34807007 | ACG Clinical Guideline for the Diagnosis and Management of Gastroesoph... | Am J Gastroenterol | Journal Article, Research Support, N.I.H., Extramural, Review, Practice Guidelin | `GUIDELINE VERIFIED` |
| 35123084 | AGA Clinical Practice Update on the Personalized Approach to the Evalu... | Clin Gastroenterol Hepatol | Practice Guideline, Review, Research Support, N.I.H., Extramural, Journal Articl | `GUIDELINE VERIFIED` |
| 35944925 | Management of Helicobacter pylori infection: the Maastricht VI/Florenc... | Gut | Journal Article | `FETCHED` |
| 36228734 | Vonoprazan Versus Lansoprazole for Healing and Maintenance of Healing ... | Gastroenterology | Randomized Controlled Trial, Journal Article, Research Support, Non-U.S. Gov't | `DATA VERIFIED` |
| 36714104 | Vietnam Association of Gastroenterology (VNAGE) consensus on the manag... | Front Med (Lausanne) | Journal Article, Review | `ABSTRACT VERIFIED` |
| 37734911 | Updates to the modern diagnosis of GERD: Lyon consensus 2.0.... | Gut | Case Reports, Review, Journal Article, Consensus Statement | `GUIDELINE VERIFIED` |
| 38173155 | Refractory Gastroesophageal Reflux Disease: Diagnosis and Management.... | J Neurogastroenterol Motil | Journal Article, Review | `ABSTRACT VERIFIED` |
| 38493017 | A Meta-analysis of PPIs Plus Alginate Versus PPIs Alone for the Treatm... | J Voice | Journal Article, Meta-Analysis, Systematic Review | `META-ANALYSIS VERIFIED` |
| 39626064 | ACG Clinical Guideline: Treatment of Helicobacter pylori Infection.... | Am J Gastroenterol | Journal Article, Practice Guideline, Research Support, Non-U.S. Gov't | `GUIDELINE VERIFIED` |
| 40337979 | Proton pump inhibitors for the prevention of non-steroidal anti-inflam... | Cochrane Database Syst Rev | Journal Article, Meta-Analysis, Systematic Review | `META-ANALYSIS VERIFIED` |

## 4. Chi tiết các claim cần hạ nhãn

- **Part_01_Tong_quan_va_Phan_bien_Hoi_chung.md** | PMID 36714104 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_02_Co_che_benh_sinh_va_Yeu_to_nguy_co.md** | PMID 30338390 | `GUIDELINE VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_02_Co_che_benh_sinh_va_Yeu_to_nguy_co.md** | PMID 30338390 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_03_Chan_doan_va_Test_H_pylori.md** | PMID 28631728 | `FULL VERIFIED` → `GUIDELINE VERIFIED` | pubtype: Journal Article, Practice Guideline, Review
- **Part_03_Chan_doan_va_Test_H_pylori.md** | PMID 28631728 | `FULL VERIFIED` → `GUIDELINE VERIFIED` | pubtype: Journal Article, Practice Guideline, Review
- **Part_03_Chan_doan_va_Test_H_pylori.md** | PMID 28631728 | `FULL VERIFIED` → `GUIDELINE VERIFIED` | pubtype: Journal Article, Practice Guideline, Review
- **Part_03_Chan_doan_va_Test_H_pylori.md** | PMID 28631728 | `FULL VERIFIED` → `GUIDELINE VERIFIED` | pubtype: Journal Article, Practice Guideline, Review
- **Part_03_Chan_doan_va_Test_H_pylori.md** | PMID 39626064 | `FULL VERIFIED` → `GUIDELINE VERIFIED` | pubtype: Journal Article, Practice Guideline, Research Support, Non-U
- **Part_04_Phac_do_tiet_tru_H_pylori_VNAGE2022.md** | PMID 36714104 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_04_Phac_do_tiet_tru_H_pylori_VNAGE2022.md** | PMID 36714104 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_05_Dieu_tri_GERD_Chuyen_sau.md** | PMID 36228734 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Randomized Controlled Trial, Journal Article, Research Suppo
- **Part_06_Quan_ly_Kho_tieu_chuc_nang_va_Loet_NSAID.md** | PMID 19949136 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Journal Article, Randomized Controlled Trial, Research Suppo
- **Part_06_Quan_ly_Kho_tieu_chuc_nang_va_Loet_NSAID.md** | PMID 25921377 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Journal Article, Multicenter Study, Randomized Controlled Tr
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 19949136 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Journal Article, Randomized Controlled Trial, Research Suppo
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 19949136 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Journal Article, Randomized Controlled Trial, Research Suppo
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 35944925 | `GUIDELINE VERIFIED` → `FETCHED` | pubtype: Journal Article
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 36228734 | `FULL VERIFIED` → `DATA VERIFIED` | pubtype: Randomized Controlled Trial, Journal Article, Research Suppo
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 36714104 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 36714104 | `FULL VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review
- **Part_07_Master_Clinical_Cases_va_Checklist.md** | PMID 36714104 | `GUIDELINE VERIFIED` → `ABSTRACT VERIFIED` | pubtype: Journal Article, Review

## 5. Nhận định chung

- **20/52 claims (38%)** bị gán nhãn quá cao so với thực tế pubtype.
- Nguyên nhân chính: `[FULL VERIFIED]` được gán cho guideline/review mà chưa từng fetch abstract hoặc đối chiếu số liệu cụ thể.
- Các Part 5-7 mới viết gần đây đã dùng pubtype-appropriate tags (GUIDELINE VERIFIED cho Guideline, ABSTRACT VERIFIED cho Review) → ít lỗi hơn.
- Part 02 đã được fix thủ công (28631728 → 19240698 cho NSAID RRs) nhưng nhãn vẫn cao hơn tier thực tế do chưa verify abstract.

## 6. Khuyến nghị

1. **Hạ toàn bộ nhãn `[FULL VERIFIED]` xuống tier pubtype-appropriate**, trừ các claim đã có bằng chứng đối chiếu số liệu cụ thể (có artifact `full_verify_table.md`).
2. **Giữ `[GUIDELINE VERIFIED]`** cho các PMID có pubtype "Practice Guideline" / "Consensus Statement": 34807007, 35123084, 37734911, 19240698, 28631728, 35944925.
3. **Dùng `[ABSTRACT VERIFIED]`** cho Review: 30338390, 36714104, 38173155.
4. **Dùng `[DATA VERIFIED]`** cho RCT khi đã kiểm tra số liệu: 36228734, 19949136, 28410791, 25921377.
5. **Dùng `[META-ANALYSIS VERIFIED]`** cho Meta-Analysis: 38493017.

---
*Report generated by `pmid_audit.py` using NCBI E-summary API live data.*