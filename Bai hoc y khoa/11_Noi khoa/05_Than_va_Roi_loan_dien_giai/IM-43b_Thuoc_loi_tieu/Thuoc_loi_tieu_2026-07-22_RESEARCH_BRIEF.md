# RESEARCH BRIEF: Thuốc lợi tiểu
****Mã bài học:** IM-43b | Ngày:** 2026-07-22 | **Research:** Terra | **Execute:** Terra  
**Tiên quyết:** [Sinh lý Nephron](../Sinh_ly_nephron/Sinh_ly_nephron_2026-07-22.md). Bài này dùng bản đồ nephron của bài nền; không lặp lại chương sinh lý và không thay thế thuật toán bệnh-specific.

---

## 1. Guideline freshness và nguồn đã chọn

### Kết quả preflight

| Lệnh | Kết quả | Cách xử lý |
|---|---|---|
| `preflight_guideline_check.py --topic "diuretics" --guideline "KDIGO 2024"` | WARN: registry chưa có topic diuretics | Đã đọc KDIGO 2024 PDF chính thức; chỉ dùng khung an toàn CKD, không suy diễn protocol lợi tiểu. |
| `... --guideline "ESC 2024"` | WARN: registry chưa có topic diuretics | Không dùng để đặt liều; liên kết IM-20/IM-22 cho thuật toán bệnh-specific. |
| `... --guideline "AASLD 2021"` | WARN: registry chưa có topic diuretics | Không lặp thuật toán cổ trướng; liên kết IM-40, nơi quản lý xơ gan/cổ trướng được giữ tập trung. |

### Papers và nguồn chọn

| # | Nguồn | Loại | Lý do chọn |
|---|---|---|---|
| 1 | Ellison DH. *Clinical Pharmacology in Diuretic Use*. PMID: 30936153; PMCID: PMC6682831 | Review toàn văn | Đã đọc trực tiếp trên PMC: vị trí tác động, kháng lợi tiểu, NSAID, nguy cơ điện giải và nguyên tắc cá thể hóa. |
| 2 | Wu L, et al. *Diuretic Treatment in Heart Failure: A Practical Guide for Clinicians*. PMID: 39124738 | Review | Abstract xác nhận sung huyết là trung tâm suy tim mất bù và lợi tiểu quai là nhóm ưu tiên giảm sung huyết; dùng cho claim định hướng. |
| 3 | KDIGO 2024 CKD Guideline. PMID: 38490803 | Guideline | Đã đọc PDF chính thức: CKD/electrolyte phải được đánh giá bằng chức năng thận, thuốc và theo dõi nguy cơ. |
| 4 | Biggins SW, et al. AASLD ascites guidance. PMID: 33942342 | Guideline | Nguồn tham chiếu cho IM-40; không dùng để thêm liều/protocol khi không đọc được văn bản chính thức qua reader. |


**Đã loại:** Không dùng giá/đường dùng/liều tối đa, khoảng theo dõi, ngưỡng điện giải hoặc protocol truyền dịch khi không có nguồn full-text/guideline trực tiếp được xác minh trong brief.

---

## 2. Claims đã kiểm chứng

| # | Claim được phép dùng | Nguồn/tag |
|---|---|---|
| 1 | Lợi tiểu được phân nhóm theo đoạn nephron và cơ chế vận chuyển mà chúng ức chế. | Ellison 2019 [ABSTRACT VERIFIED] |
| 2 | Lợi tiểu quai ức chế NKCC2 ở TAL; thiazide/thiazide-like ức chế NCC ở DCT. | Ellison 2019 [ABSTRACT VERIFIED] |
| 3 | Amiloride/triamterene chẹn ENaC; spironolactone/eplerenone đối kháng thụ thể mineralocorticoid ở đoạn xa/ống góp. | Ellison 2019 [ABSTRACT VERIFIED] |
| 4 | Lợi tiểu quai, thiazide và tiết kiệm kali có những hướng độc tính điện giải khác nhau; hạ kali, hạ natri, tăng kali, giảm thể tích, suy thận trước thận và ototoxicity là các nguy cơ cần biết theo nhóm/bối cảnh. | Ellison 2019 [ABSTRACT VERIFIED] |
| 5 | NSAID có thể giảm đáp ứng lợi tiểu và làm tăng nguy cơ tổn thương thận, nhất là khi có bệnh tim/thận và phối hợp thuốc ảnh hưởng huyết động thận. | Ellison 2019 [ABSTRACT VERIFIED] |
| 6 | Kháng lợi tiểu có thể liên quan giảm bài tiết thuốc, giảm GFR/tải natri, ăn mặn và tái hấp thu bù đoạn xa; thêm thiazide/thiazide-like có thể khôi phục lợi natri nhưng tăng nguy cơ hạ kali. | Ellison 2019 [ABSTRACT VERIFIED] |
| 7 | Trong suy tim mất bù, sung huyết và giữ dịch là vấn đề trung tâm; lợi tiểu quai được guideline ưu tiên để giảm sung huyết, nhưng sử dụng phải gắn với theo dõi và bệnh cảnh. | Wu 2024 [ABSTRACT VERIFIED] |
| 8 | CKD, bệnh gan mất bù, rối loạn điện giải hoặc giảm tưới máu đòi hỏi theo dõi/chuyển chuyên khoa tùy mức độ; không áp dụng một liều chung. | KDIGO 2024 [GUIDELINE VERIFIED] |


### Số liệu CẤM dùng
- Không dùng liều khởi đầu/tối đa, tốc độ tăng liều, tỷ lệ phối hợp, tần suất xét nghiệm hay ngưỡng lab như chỉ định phổ quát.
- Không dùng ngưỡng eGFR cứng để phủ định mọi thiazide; nêu nguyên tắc là hiệu quả và nguy cơ thay đổi theo GFR/bệnh cảnh.
- Không tự đưa thuật toán suy tim, tăng huyết áp, cổ trướng hay CKD; liên kết IM-22, IM-20, IM-40, IM-44.

---

## 3. Dàn ý thực thi

### 0–1. Tổng quan và nhắc nền nephron
- Giải thích lợi tiểu là gì; bắt buộc link bài nền và một đoạn nhắc PCT–TAL–DCT–ống góp.
- BOX ĐỎ trước nhánh thường quy: giảm oxy/phù phổi, sốc/giảm tưới máu, vô niệu, lú lẫn, rối loạn điện giải nặng hoặc suy thận xấu nhanh → đánh giá cấp cứu/chuyển tuyến.

### 2. Bản đồ nhóm–đoạn
- Với mỗi nhóm: đoạn đích, vận chuyển bình thường bị chặn, hệ quả dịch/điện giải, chỉ định boundary và hướng adverse-effect.

### 3–4. Chọn theo mục tiêu và kê đơn an toàn
- Mục tiêu → kiểm phù hợp/chống chỉ định → đường/thời điểm theo protocol địa phương → đo đáp ứng → theo dõi thể tích–cân nặng–điện giải–creatinine → dừng/escalate.
- Cross-link thay vì sao chép IM-20, IM-22, IM-40, IM-44.

### 5–7. Kháng lợi tiểu, an toàn và flowchart
- Rà tuân thủ, muối, NSAID, tưới máu, CKD/hấp thu trước sequential blockade.
- Nếu cần phối hợp, chỉ dưới theo dõi có thể xét nghiệm; mô tả red flag và Plan A/Plan B.

### 8–11. Cases, tips, summary, references
- Ba cases: phù ổn định; phù phổi/sốc/anuria/lú lẫn; sung huyết dai dẳng sau lợi tiểu quai.
- Mỗi case đủ 5 bước ra quyết định và nêu lựa chọn không phù hợp.

---

## 4. Hướng dẫn execute

1. Chỉ dùng claims trong brief; không tự thêm số, liều hoặc thời gian.
2. Dùng citation theo tên tác giả trong body; PMID chỉ đặt ở reference list để tránh checker gán số minh họa cho paper.
3. Bài này dạy dược lý tái sử dụng; thuật toán bệnh-specific thuộc các bài liên kết.
4. Mọi phối hợp lợi tiểu nguy cơ cao phải ghi điều kiện theo dõi và ngưỡng chuyển tuyến, không biến thành y lệnh ngoại trú.