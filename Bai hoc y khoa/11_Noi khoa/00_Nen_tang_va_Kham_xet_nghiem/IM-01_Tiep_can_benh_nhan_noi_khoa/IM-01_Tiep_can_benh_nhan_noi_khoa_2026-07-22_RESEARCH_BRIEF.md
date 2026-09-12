# RESEARCH BRIEF: IM-01 — Cách tiếp cận bệnh nhân Nội khoa người lớn

**Ngày:** 2026-07-22 | **Profile:** foundation | **Đối tượng:** Người học chưa có nền tảng

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "profile_foundation",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "learner_smoke"
  ],
  "not_applicable": [],
  "approved_exemptions": []
}
```

## 1. Preflight guideline

- **WARN (đã chạy):** `preflight_guideline_check.py` chưa có topic “Cách tiếp cận bệnh nhân Nội khoa người lớn” trong registry. Không thêm guideline registry chỉ để làm preflight pass.
- **Nguồn Tier 0 web đã đọc:** Resuscitation Council UK. *The ABCDE Approach*, updated July 2024. Dùng cho nguyên tắc ABCDE, ưu tiên vấn đề đe dọa tính mạng, gọi hỗ trợ sớm, điều trị trước khi sang bước kế tiếp và đánh giá lại.

## 2. Nguồn đã chọn

| Nguồn | Loại | Phạm vi được dùng |
|---|---|---|
| Resuscitation Council UK (2024), *The ABCDE Approach* | Hướng dẫn web chính thức | ABCDE; ưu tiên cấp cứu; đánh giá lại; gọi hỗ trợ; lịch sử/xét nghiệm/hồ sơ sau ổn định ban đầu. |
| Bruinink et al. (2024), *Resuscitation Plus*, PMID: 39345661 | Scoping review; abstract đã fetch | ABCDE là tiếp cận đánh giá ban đầu có ưu tiên cho người bệnh nặng/chấn thương; bằng chứng outcome người bệnh còn hạn chế. |
| Bickley LS. *Bates’ Guide to Physical Examination and History Taking*, 13e | Textbook | Khung bệnh sử, khám tổng quát và khám có trọng điểm. |
| McGee S. *Evidence-Based Physical Diagnosis*, 5e | Textbook | Liên kết dấu khám với xác suất và giới hạn diễn giải. |

## 3. Claims được phép

1. ABCDE là cách tiếp cận có ưu tiên cho đánh giá ban đầu người bệnh nặng/chấn thương; đánh giá ưu tiên vấn đề đe dọa tính mạng, điều trị trước khi chuyển sang bước kế tiếp và đánh giá lại sau can thiệp. [GUIDELINE VERIFIED; ABSTRACT VERIFIED — PMID: 39345661]
2. Scoping review 2024 xác định có nhiều công cụ ABCDE khác nhau, mức tuân thủ biến thiên và dữ liệu về outcome người bệnh còn hạn chế; không được tuyên bố ABCDE tự nó cải thiện tử vong. [ABSTRACT VERIFIED — PMID: 39345661]
3. Khi người bệnh chưa ổn định, mục tiêu ban đầu là nhận diện và xử trí nguy cơ tức thì, huy động hỗ trợ, theo dõi và mua thời gian cho chẩn đoán nguyên nhân; không hoàn thành bệnh sử thường quy trước khi xử trí cấp cứu. [GUIDELINE VERIFIED]
4. Bệnh sử, khám và xét nghiệm được tổ chức để trả lời một câu hỏi lâm sàng, cập nhật problem list và quyết định mức chăm sóc; các bước này không thay thế đánh giá lại khi tình trạng thay đổi. [TEXTBOOK: Bates 13e; McGee 5e; GUIDELINE VERIFIED]
5. Problem list là danh sách vấn đề có ưu tiên: mỗi mục nêu bằng chứng, mức độ khẩn, giả thuyết/differential, dữ liệu còn thiếu, hành động và kế hoạch theo dõi/chuyển tuyến. [TEXTBOOK: Bates 13e; McGee 5e]
6. Để tránh đóng chẩn đoán quá sớm, người học dùng biểu diễn vấn đề ngắn, differential theo hội chứng, tìm dữ kiện phủ định và đánh giá lại. Đây là kỹ thuật khung thực hành, không phải claim định lượng hay claim hiệu quả điều trị.

## 4. Số liệu và protocol cấm dùng

- Không dùng tỷ lệ tuân thủ, số study, cỡ mẫu, tỷ lệ outcome hay bất kỳ hiệu quả điều trị nào từ PMID 39345661 trong MD/cards.
- Không đưa liều, đường dùng, thời điểm hoặc protocol thuốc/oxy/dịch/CPR vào IM-01. Các nội dung này thuộc IM-02 và các bài cấp cứu chuyên biệt.
- Không dùng cutoff sinh hiệu, thang điểm, ngưỡng xét nghiệm hay quyết định ICU nếu không có nguồn trực tiếp trong brief.
- Không dùng PMID nào ngoài 39345661 nếu chưa fetch rồi ghi rõ vai trò/tag.

## 5. Dàn ý thực thi

1. Tổng quan: IM-01 là bản đồ làm việc trước khi chẩn đoán bệnh; ổn định hay chưa ổn định là câu hỏi đầu tiên.
2. Nền tảng tối thiểu: người bệnh, triệu chứng, dấu hiệu, sinh hiệu, vấn đề, dữ kiện, chẩn đoán phân biệt và kế hoạch; giải thích bằng ví dụ đơn giản.
3. Định nghĩa: bệnh sử, khám có trọng điểm, xét nghiệm, problem list, differential, assessment, plan và reassessment.
4. Cơ chế/lý do: vì sao ưu tiên nguy hiểm trước, vì sao dữ kiện không phải chẩn đoán, vì sao đánh giá lại thay đổi kế hoạch.
5. Chẩn đoán và theo dõi: chuỗi thực hành từ quan sát ban đầu → ABCDE/red flags → bệnh sử → khám → dữ liệu → problem list → differential → kế hoạch/đánh giá lại.
6. Evidence & guideline: giới hạn đúng phạm vi của ABCDE; không ngộ nhận evidence outcome.
7. Lưu đồ: red flags/cấp cứu → ABCDE và gọi hỗ trợ; nếu ổn định → bệnh sử/khám/problem list; Plan B khi thiếu nguồn lực.
8. Case 1: không ổn định, phải dừng khai thác thường quy. Case 2: ổn định, tạo problem list và first-hour plan.
9. Tổng kết, tips và references.

## 6. Hướng dẫn execute

- Chỉ dùng claims ở brief; không thêm số liệu hoặc protocol.
- Tiếng Việt có dấu; giải thích thuật ngữ Anh ở lần đầu.
- Trước nhánh thường quy luôn có BOX ĐỎ, flowchart có nhánh cấp cứu/thiếu nguồn lực, và case theo năm bước quyết định.
- Markdown là source of truth; cards/APKG/DOCX chỉ được tạo sau MD đã review.
