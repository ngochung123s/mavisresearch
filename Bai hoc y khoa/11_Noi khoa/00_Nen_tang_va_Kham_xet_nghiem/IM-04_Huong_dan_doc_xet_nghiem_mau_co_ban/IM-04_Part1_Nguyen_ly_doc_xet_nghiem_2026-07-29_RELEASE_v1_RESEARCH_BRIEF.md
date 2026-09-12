# RESEARCH BRIEF — IM-04 PART 1: NGUYÊN LÝ ĐỌC XÉT NGHIỆM

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "mode": "L3_BEGINNER",
  "required_gates": [
    "brief_pmid_preflight",
    "brief_claims_strict",
    "source_pmid_strict",
    "source_claims_strict",
    "source_retraction",
    "guideline_evidence",
    "depth_foundation",
    "guideline_evidence_crosscheck",
    "citation_zero_block",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "docx_build",
    "learner_smoke"
  ],
  "lesson_depth_contract": {
    "min_total_words": 5000,
    "min_total_lines": 500,
    "min_sections": 10,
    "min_subsections": 12,
    "min_mechanism_chains": 3,
    "min_examples": 6,
    "min_misconceptions": 6,
    "min_checkpoints": 4,
    "min_cases_with_solutions": 2,
    "min_practical_tips": 10,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [],
  "approved_exemptions": []
}
```

- **Output basename đã khóa:** `IM-04_Part1_Nguyen_ly_doc_xet_nghiem_2026-07-29_RELEASE_v1`
- **Chuyên khoa:** Nội khoa người lớn.
- **Đối tượng:** bác sĩ, học viên sau đại học và người học mất gốc cần xây lại tư duy xét nghiệm.

## 1. Phạm vi và preflight guideline

- **Chủ đề:** nguyên lý chung để đọc xét nghiệm máu an toàn trước khi diễn giải từng chỉ số.
- **Guideline chính thức đã kiểm freshness:** WHO, *WHO guidelines on drawing blood: best practices in phlebotomy*, 2010, ISBN 9789241599221; trang phát hành và file tiếng Anh vẫn hiện diện trong WHO IRIS ngày 2026-07-29; không phát hiện tài liệu WHO thay thế toàn bộ văn bản.
- **Phạm vi được phép:** ba giai đoạn của quy trình xét nghiệm; chất lượng mẫu; khoảng tham chiếu; ngưỡng quyết định; giá trị báo động; baseline, động học, delta check; đơn vị; khung đọc năm bước; an toàn và giao tiếp labo.
- **Ngoài phạm vi:** diễn giải chi tiết CBC, đông máu và các chỉ số sinh hóa cơ quan; ngưỡng bệnh cụ thể; kê đơn.
- **Audit EFLM bắt buộc:** file `outputs/sources/part1/eflm_colabiocli_venous_blood_sampling_2018.pdf` là bản dịch tiếng Romania công bố 2023/2024, DOI 10.2478/rrlm-2024-0004. Chính file ghi EFLM không endorse hoặc approve nội dung bản dịch và yêu cầu trích bản gốc DOI 10.1515/cclm-2018-0602. Vì bản gốc hợp pháp không tải được từ publisher trong lần audit này, bản dịch bị loại khỏi guideline evidence và không cấp nhãn.

## 2. Papers đã chọn

- **PMID:** `23741774`
  - **Expected title:** WHO Guidelines on Drawing Blood: Best Practices in Phlebotomy
  - **Loại nguồn:** Practice Guideline / Review; official WHO publication.
  - **Vai trò:** khóa một claim guideline định tính về quy trình lấy máu an toàn và chất lượng mẫu.
  - **Lý do chọn:** nguồn chính thức, local exact copy từ WHO IRIS, authority rõ, không phải bản dịch, có thể crosscheck exact quote.

### Nguồn đã loại

- Định danh sai từng được đề xuất cho một bài Apicomplexa: sai bài và sai chủ đề, loại tuyệt đối; không đưa mã đó vào source set đã khóa.
- Bản Romania DOI 10.2478/rrlm-2024-0004: chỉ là translation; EFLM không endorse/approve nội dung bản dịch; không dùng làm guideline evidence.
- Bản gốc EFLM DOI 10.1515/cclm-2018-0602: identity và authority đã xác nhận, nhưng full text hợp pháp từ publisher không tải được trong lần audit; không dùng exact quote hay gán nhãn.
- CLSI GP41 và EP28: paywall; không tải hoặc trích trái phép.
- Survey Lithuania 2024: bài khảo sát thực hành, không phải guideline; không cần cho claim khóa của Part 1.

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Hướng dẫn WHO về lấy máu (phlebotomy) cung cấp hướng dẫn về các bước lấy máu an toàn (safe phlebotomy) và nhắc lại các nguyên tắc được chấp nhận trong lấy và thu thập máu (drawing and collecting blood). | 23741774 | [GUIDELINE VERIFIED] | This document provides guidance on the steps recommended for safe phlebotomy, and reiterates the accepted principles for drawing and collecting blood. | Nhân viên y tế và người bệnh trong các cơ sở có thực hành lấy máu | Áp dụng thực hành lấy máu an toàn so với quy trình không chuẩn hóa | Chất lượng mẫu và an toàn cho người bệnh, nhân viên y tế | Trong toàn bộ lần lấy máu và vận chuyển mẫu |

## 4. Claims và số liệu cấm dùng

- Không dùng tỷ lệ phần trăm sai số tiền phân tích nếu không có exact evidence đã khóa.
- Không dùng giới hạn garôt, thứ tự rút ống hoặc số lần đảo ống từ bản dịch Romania.
- Không dùng ngưỡng critical value cố định toàn cầu; bài phải yêu cầu đối chiếu danh sách của labo sở tại.
- Không dùng công thức RCV hay hệ số quy đổi cụ thể vì không được khóa trong brief này.
- Không dùng ngưỡng chẩn đoán bệnh thuộc Part 2/Part 3.

## 5. Dàn ý chi tiết

### 0. Nền tảng tối thiểu cần dùng ngay
- Phân biệt người bệnh, mẫu bệnh phẩm, đại lượng đo, kết quả và quyết định.
- Claim IDs: không có.

### 1. Tổng quan và định nghĩa
- Ba pha của tổng quy trình xét nghiệm; sai số và bất định.
- Claim IDs: C-001.

### 2. Cơ chế
- Chuỗi 1: tư thế/garôt → dịch chuyển nước → cô đặc tương đối → thay đổi kết quả → kiểm lại điều kiện lấy mẫu.
- Chuỗi 2: tổn thương tế bào → giải phóng chất nội bào/nhiễu quang → kết quả giả → kiểm chất lượng mẫu.
- Chuỗi 3: sai nhận diện → kết quả đúng của sai người → quyết định sai → xác minh định danh.

### 3. Chẩn đoán và phân tầng
- Khung năm bước: đúng người và đúng mẫu; kiểm cấp cứu; kiểm điều kiện đo; đọc pattern và động học; chốt hành động.

### 4. Theo dõi
- Baseline cá thể, động học, delta check và trao đổi với labo.

### 5. Flowchart ASCII và BOX ĐỎ
- Nhánh cấp cứu: ưu tiên tình trạng người bệnh; không trì hoãn xử trí chỉ để giải thích bảng xét nghiệm.
- Nhánh thường quy: xác minh mẫu rồi mới diễn giải.
- Nhánh thiếu nguồn lực/Plan B: gọi labo, xem phiếu giấy, lấy lại mẫu khi an toàn.

### 6. Case và lời giải
- Case 1: kali tăng bất ngờ trên mẫu có dấu hiệu chất lượng kém.
- Case 2: hemoglobin giảm đột ngột nhưng định danh và bối cảnh không khớp.

### 7. Tổng kết và tài liệu tham khảo
- Một nguồn guideline chính thức duy nhất cho claim khóa; kiến thức nền còn lại trình bày không nhãn.

## 6. Hướng dẫn model execute

1. Viết tiếng Việt có dấu, mode `L3_BEGINNER`, tối thiểu 5.000 từ và 500 dòng không trống.
2. Chỉ dùng claim C-001 ở đúng một occurrence có PMID, tag và `{claim:C-001}` trên cùng dòng.
3. Kiến thức consensus không gắn nhãn, không thêm con số lâm sàng ngoài brief.
4. Có ít nhất mười section, mười hai subsection, ba chuỗi cơ chế năm tầng, sáu ví dụ, sáu bẫy, bốn checkpoint, hai case có lời giải năm bước và mười tips.
5. Có BOX ĐỎ trước flowchart thường quy, nhánh cấp cứu và Plan B.
6. Không gọi bản dịch Romania là bản gốc, không dùng bản dịch để cấp guideline verified.
7. Không padding, không placeholder, không viết lấn Part 2 hoặc Part 3.
