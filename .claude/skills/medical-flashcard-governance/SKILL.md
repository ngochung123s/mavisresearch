---
name: medical-flashcard-governance
description: "Quy tắc chuẩn hóa thiết kế bộ thẻ flashcard Anki Y khoa siêu chi tiết từ tài liệu bài giảng (văn bản gốc + góc nhìn bổ sung AI), chống lỗi hiển thị LaTeX/ký tự, chống lộ đáp án ở extra và chống đục lỗ ngược thứ bậc kiến thức."
---

# Quy tắc Thiết kế Flashcard Y khoa Siêu Chi Tiết (Anki Flashcard Governance)

## 1. Triết Lý Cốt Lõi
- **Chi Tiết Là Vua (Detail is King):** Mọi thông tin trong bài giảng gốc (con số, triệu chứng, tiêu chuẩn, chỉ số, ngoại lệ, bẫy lâm sàng) TẤT CẢ đều phải được chuyển thể thành flashcard. Tuyệt đối không tóm tắt hay lược bỏ thông tin.
- **Nguyên Tắc "Một Đơn V vị Kiến Thức - Một Thẻ" (Minimum Information Principle):** 
  - Mỗi thẻ chỉ kiểm tra và đại diện cho duy nhất 1 đơn vị kiến thức/1 phân độ/1 bậc/1 tiêu chuẩn.
  - Tuyệt đối KHÔNG gộp chung nhiều bậc hoặc nhét bậc kế tiếp vào phần giải thích của bậc trước.
- **Trung thực tuyệt đối:** Không tự bịa, không thêm bớt thông tin ngoài bài giảng.

## 2. Cấu Trúc Nội Dung Thẻ Basic (Hỏi - Đáp)
Phần `back` của mỗi thẻ Basic bắt buộc gồm 2 khối phân biệt rõ ràng:
1. `<b>📖 Văn bản gốc:</b><br>`: Trích dẫn câu trả lời bám sát 100% tài liệu gốc dưới dạng gạch đầu dòng (`• `).
2. `<b>🔍 Góc nhìn bổ sung (AI):</b><br>`: Giải thích bản chất y khoa, cơ chế sinh lý bệnh, ý nghĩa lâm sàng hoặc lưu ý chống nhầm lẫn để người học hiểu sâu bản chất.

## 3. Quy Tắc Thẻ Cloze (Điền Khuyết) & Đục Lỗ Chuẩn Y Khoa

### A. Quy tắc kỹ thuật Cloze:
- TẤT CẢ chỗ trống trong cùng một thẻ cloze BẮT BUỘC dùng `{{c1::...}}`. Tuyệt đối KHÔNG dùng `c2`, `c3`.
- Dùng cloze cho các con số định lượng, tiêu chuẩn chẩn đoán, mốc phân độ, tên thuốc đầu tay.

### B. Quy tắc "Đi từ Cốt lõi đến Chi tiết" (Core-to-Detail Hierarchy):
- **CẤM LỘ TÊN THUỐC / LIỀU ĐẦU TAY TRONG CÂU DẪN (Anti-Prompt Leakage):**
  - Không được "dâng sẵn" tên thuốc cốt lõi và phác đồ đầu tay trong câu dẫn rồi chỉ đục lỗ vụn vặt ở đuôi câu.
  - *Ví dụ lỗi:* "Cách dùng Furosemid liều cao trong STC: Tiêm TM 5-10 ống (100-200mg)... hoặc truyền TM `[...]`, tổng liều `[...]`" $\rightarrow$ Thẻ này làm lộ luôn tên thuốc Furosemid và liều tiêm 100-200mg mà chưa hề kiểm tra người học xem họ có nhớ Furosemid và liều tiêm đó hay không!
- **Thứ bậc tạo thẻ bắt buộc khi gặp một phác đồ thuốc:**
  1. **Thẻ Cốt lõi (Bậc 1):** Thuốc chỉ định là gì? Liều khởi đầu/đầu tay là bao nhiêu? (Đục lỗ chính Tên thuốc và Liều khởi đầu).
  2. **Thẻ Chi tiết/Mở rộng (Bậc 2):** Tốc độ truyền TM duy trì hoặc Liều tối đa cho phép là bao nhiêu?
  3. **Thẻ Cảnh báo/Theo dõi (Bậc 3):** Tác dụng phụ cần theo dõi (độc tính tai, điện giải) hoặc chống chỉ định.

### C. Quy tắc nghiêm ngặt về trường `extra` của thẻ Cloze:
- ❌ **CẤM TUYỆT ĐỐI (Negative Constraint):** Không được lấy dòng tiếp theo, bậc kế tiếp hoặc tiêu chuẩn liền kề trong bảng/danh sách để đưa vào trường `extra` (Ví dụ: Thẻ hỏi Bậc R thì CẤM để thông tin Bậc I vào `extra`). Hành vi này làm lộ đáp án thẻ sau (Priming effect) và gây ảo tưởng nhớ bài (Illusion of competence).
- ✅ **Trường `extra` CHỈ ĐƯỢC CHỨA:**
  1. Cơ chế sinh lý bệnh giải thích tại sao có con số/dấu hiệu đó.
  2. Lưu ý lâm sàng hoặc bẫy chẩn đoán để chống nhầm lẫn.
  3. Ý nghĩa điều trị/hành động cấp cứu tức thì.
- ⚠️ Nếu không có cơ chế hay lưu ý chuyên sâu để giải thích cho chính đơn vị kiến thức đó, BẮT BUỘC để trống `extra: ""` (hoặc không ghi), TUYỆT ĐỐI KHÔNG copy nội dung của mục khác để lấp chỗ trống.

## 4. Quy Tắc Định Dạng & Kỹ Thuật (Text, HTML & Anki Rendering) - CỰC KỲ QUAN TRỌNG

### ❌ CÁC LỖI KINH ĐIỂN CẦN TRÁNH TUYỆT ĐỐI
- **Lỗi mũi tên LaTeX:** ❌ `$\rightarrow$` hoặc `\\rightarrow` $\rightarrow$ ✅ BẮT BUỘC DÙNG KÝ TỰ UNICODE `→`.
- **Lỗi liều lượng / đơn vị LaTeX:** ❌ `$40\text{ mg} \times 1$`, `$10\text{ mg/kg}$` $\rightarrow$ ✅ BẮT BUỘC DÙNG `40 mg × 1 viên/ngày`, `10 mg/kg`.
- **Lỗi ký hiệu so sánh & vi sinh:** ❌ `$\ge$`, `$\le$`, `$\mu\text{mol/L}$`, `$\text{IL-1}\beta$` $\rightarrow$ ✅ BẮT BUỘC DÙNG `≥`, `≤`, `µmol/L`, `IL-1β`.

### 📌 BẢNG TRA CỨU KÝ TỰ UNICODE BẮT BUỘC:
| Ý nghĩa | ❌ CẤM VIẾT LATEX | ✅ BẮT BUỘC VIẾT UNICODE |
| :--- | :--- | :--- |
| **Mũi tên suy ra / dẫn đến** | `$\rightarrow$`, `\rightarrow`, `->` | `→` |
| **Mũi tên hai chiều** | `$\leftrightarrow$` | `↔` |
| **Lớn hơn hoặc bằng** | `$\ge$`, `$\geq$`, `>=` | `≥` |
| **Nhỏ hơn hoặc bằng** | `$\le$`, `$\leq$`, `<=` | `≤` |
| **Dấu nhân** | `\times`, `*` | `×` *(hoặc `x`)* |
| **Micro (µ)** | `\mu`, `\mu\text{g}`, `\mu\text{mol/L}` | `µg`, `µmol/L` |
| **Beta, Alpha** | `\beta`, `\alpha` | `β`, `α` |
| **Phần nghìn, phần trăm** | `14\text{‰}`, `$50\%$` | `14‰`, `50%` |

## 5. JSON Schema Chuẩn
- Basic: `{"type": "basic", "front": "...", "back": "...", "extra": ""}`
- Cloze: `{"type": "cloze", "text": "...", "extra": ""}`
