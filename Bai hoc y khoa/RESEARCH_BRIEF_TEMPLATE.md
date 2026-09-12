# RESEARCH_BRIEF.md — Template khóa nguồn trước khi viết bài

> Tạo file này sau research và trước bài Markdown. Model execute chỉ được dùng claim đã khóa ở đây.

## 0. Lesson profile & release contract

Chế độ duy nhất: `L3_BEGINNER` (hiển thị: `L3 — Cầm tay chỉ việc cho người mất gốc`). Chọn profile bằng `python "10_Script Python/publish_gate.py" --list-profiles`, rồi copy **đúng toàn bộ** danh sách gate và khóa `lesson_depth_contract` tương ứng trong Research Brief trước research. Profile chỉ phân loại cấu trúc chuyên môn (`foundation`, `disease`, `pharmacology`), tất cả đều bắt buộc dùng chế độ `L3_BEGINNER`.

Ví dụ contract cho profile `foundation` (bài nền tảng cho người mất gốc):

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
    "depth_foundation",
    "guideline_evidence",
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

**Ngưỡng độ sâu tối thiểu theo profile:**
- **Foundation (`foundation`):** $\ge 5.000$ từ, $\ge 500$ dòng, $\ge 10$ sections, $\ge 12$ subsections, $\ge 3$ mechanism chains (dây chuyền nhân quả 5 tầng), $\ge 6$ ví dụ minh họa, $\ge 6$ bẫy/nhầm lẫn, $\ge 4$ checkpoints dừng tự kiểm tra, $\ge 2$ ca lâm sàng có lời giải đầy đủ 5 bước, $\ge 10$ practical tips. (Thuật ngữ chuyên môn phải được giải thích ngay ở lần đầu xuất hiện). *Lưu ý:* Không ép buộc kê đơn / liều thuốc đối với bài foundation thuần sinh lý/giải phẫu không có thuốc.
- **Disease (`disease`):** $\ge 6.000$ từ, $\ge 600$ dòng, $\ge 10$ sections, $\ge 14$ subsections, $\ge 4$ mechanism chains, $\ge 8$ ví dụ, $\ge 8$ bẫy/nhầm lẫn, $\ge 5$ checkpoints, $\ge 3$ ca lâm sàng có lời giải, $\ge 12$ tips, $\ge 2$ phác đồ mẫu hoàn chỉnh.
- **Pharmacology (`pharmacology`):** $\ge 6.000$ từ, $\ge 600$ dòng, $\ge 8$ sections, $\ge 14$ subsections, $\ge 5$ mechanism chains, $\ge 8$ ví dụ, $\ge 8$ bẫy/nhầm lẫn, $\ge 5$ checkpoints, $\ge 3$ ca lâm sàng có lời giải, $\ge 12$ tips, $\ge 3$ phác đồ mẫu hoàn chỉnh.

- Required gates phải khớp chính xác profile; required gate không được miễn.
- **Output basename đã khóa:** `[Ten_bai_YYYY-MM-DD_RELEASE_vN]`.
- Chạy phát hành bằng `build_pipeline.py`; không tự viết `gate-results.json`.

### 🚨 QUY TẮC ĐÓNG CĂNG (FREEZE RULE & NO-PADDING)
1. **Cấm sửa Verifier Script:** Cấm tuyệt đối sửa các script verifier (`publish_gate.py`, `profile_check.py`, `depth_check.py`, `verify_claims.py`...) trong cùng workstream phát hành để lách gate. Nếu gate fail, PHẢI sửa nội dung/evidence trong brief và bài học. Việc thay đổi verifier script (nếu có) phải thực hiện trong một workstream/commit độc lập kèm regression test và rerun toàn bộ pipeline từ đầu.
2. **Cấm tự chế Quote:** Quote từ nguồn phải là exact substring từ local file/abstract. Cấm tự bịa quote hoặc paraphrase quote. Đối với Guideline quote, bắt buộc có exact substring + locator (mục/trang/đoạn).
3. **Quy tắc dừng:** Model chỉ được dừng khi acceptance matrix & `lesson_depth_contract` thỏa mãn đầy đủ về độ sâu và độ phủ. CẤM dừng với lý do "bài đã dài". CẤM lặp ý, paraphrase padding, danh sách trần.
## 1. Phạm vi và preflight guideline

- Chủ đề và đối tượng học:
- Guideline chính thức đã kiểm freshness:
- Phạm vi được phép:
- Ngoài phạm vi:

Guideline không có PMID vẫn hợp lệ nếu có evidence riêng (`pmid` có thể là `null` hoặc string). Lưu `guideline_evidence.json` và bản local trong `outputs/sources/`.
Mỗi object trong `guideline_evidence.json` bắt buộc chứa đúng **14 trường schema** khớp 100% với verifier:
1. `claim_id`: Claim ID liên kết trong Research Brief (vd: "C-001")
2. `society`: Tên tổ chức/xã hội nghề nghiệp (vd: "ACOG", "ESHRE", "FIGO")
3. `title`: Tên đầy đủ của guideline
4. `document_id`: Mã số văn bản/bulletin (vd: "PB #175")
5. `version`: Phiên bản/năm xuất bản (vd: "2023")
6. `publication_date`: Ngày/năm xuất bản chính thức (vd: "2023-05-15")
7. `accessed_at`: Ngày truy cập đối chiếu (vd: "2026-07-28")
8. `canonical_url`: Đường dẫn HTTPS chính thức
9. `local_copy`: Đường dẫn file local trong `outputs/sources/`
10. `sha256`: Mã băm SHA-256 của file local
11. `recommendation_text`: Đoạn trích khuyến cáo **nguyên văn liên tục (exact continuous substring)** từ file local/web, **tuyệt đối không dùng dấu ba chấm (`...` / ellipsis)** để cắt ghép hay lách match
12. `locator`: Vị trí chính xác trong tài liệu local (vd: "Section 3.2, Page 14, Paragraph 2")
13. `pmid`: PMID nếu có trên PubMed, hoặc `null` nếu là web/PDF trực tiếp
14. `superseded_by`: `null` hoặc string thông tin bản thay thế nếu đã cũ

**Ví dụ JSON object đầy đủ trong `guideline_evidence.json`:**
```json
{
  "guidelines": [
    {
      "claim_id": "C-001",
      "society": "ACOG",
      "title": "ACOG Practice Bulletin No. 175: Ultrasound in Pregnancy",
      "document_id": "PB #175",
      "version": "2017",
      "publication_date": "2017-12-01",
      "accessed_at": "2026-07-29",
      "canonical_url": "https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2017/12/ultrasound-in-pregnancy",
      "local_copy": "outputs/sources/acog_pb175.pdf",
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "recommendation_text": "Fetal biometry including biparietal diameter, head circumference, abdominal circumference, and femur length should be measured to estimate gestational age.",
      "locator": "Section 4, Page 6, Paragraph 3",
      "pmid": "29189689",
      "superseded_by": null
    }
  ]
}
```
## 2. Papers đã chọn

- **PMID:** `[12345678]`
  - Loại nguồn:
  - Vai trò:
  - Lý do chọn:

Liệt kê riêng các paper đã loại và lý do.

## 3. Claims đã verify

Đây là registry máy đọc được. **Mỗi occurrence có một Claim ID**, kể cả khi nhiều claim dùng cùng PMID. Không gộp theo PMID.

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Can thiệp làm giảm kết cục định tính | 12345678 | [ABSTRACT VERIFIED] | Exact source sentence | Người trưởng thành | A so với B | Kết cục chính | 12 tuần |
| C-002 | Nguy cơ giảm 20% | 12345678 | [DATA VERIFIED] | Exact sentence containing 20% | Người trưởng thành | A so với B | Kết cục chính | 12 tuần |

Quy tắc:

- `[FETCHED]`: chỉ metadata; claim không được có con số.
- `[ABSTRACT VERIFIED]`: claim định tính khớp abstract.
- `[DATA VERIFIED]`: số liệu khớp chính xác quote và abstract/full text.
- `[FULL TEXT VERIFIED]`: đã đối chiếu toàn văn và có artifact toàn văn.
- `[GUIDELINE VERIFIED]`: khớp guideline chính thức trong `guideline_evidence.json`.
- **NĂM NHÃN DUY NHẤT:** Cấm tuyệt đối 5 nhãn cũ `[ABSTRACT MATCH]`, `[FULL VERIFIED]`, `[DIRECTION ONLY]`, `[TEXTBOOK]`, `[Thông tin cơ bản - LLM verified]`.
- **TÁCH BIỆT KIẾN THỨC CONSENSUS & CLAIM CẦN EVIDENCE:** Kiến thức consensus/sinh lý/giải phẫu cơ bản (ổn định $\ge 10$ năm) viết tự do KHÔNG gán nhãn verification và KHÔNG cần PMID, tuyệt đối không tạo áp lực bịa PMID/quote. Chỉ claim có con số định lượng (%, mg/kg, RR/CI), ngưỡng, protocol detail, liều thuốc, khuyến cáo guideline mới cần Claim ID + PMID/guideline evidence + exact quote.
- Claim định lượng bắt buộc có exact quote nguyên văn từ local source và đủ population/intervention-comparator/outcome/timepoint.
## 4. Claims và số liệu cấm dùng

- Claim đã xem nhưng nguồn không hỗ trợ:
- Con số chỉ có trong secondary source:
- Liều/timing/protocol chưa verify:
- Guideline cũ hoặc bị superseded:

## 5. Dàn ý chi tiết

Mỗi mục ghi rõ Claim ID nào được dùng. Flowchart mô tả bằng logic phân nhánh để model execute viết khối `text` ASCII hoặc danh sách phân cấp; không dùng Mermaid.

### 0. Nền tảng tối thiểu cần dùng ngay

- Kiến thức consensus cần giải thích:
- Claim IDs:

### 1. Tổng quan và định nghĩa

- Claim IDs:

### 2. Cơ chế

- Chuỗi 5 tầng: cơ chế phân tử → tế bào/mô/tưới máu → lâm sàng/xét nghiệm → quyết định → phản chứng/hậu quả.
- Claim IDs:

### 3. Chẩn đoán và phân tầng

- Claim IDs:

### 4. Điều trị/theo dõi

- Claim IDs:

### 5. Flowchart ASCII và BOX ĐỎ

- Nhánh cấp cứu:
- Nhánh thường quy:
- Nhánh thiếu nguồn lực/Plan B:

### 6. Case và lời giải

- Case 1:
- Case 2:

### 7. Tổng kết và tài liệu tham khảo

- Claim IDs:

## 6. Hướng dẫn model execute

1. **Chế độ duy nhất:** `L3_BEGINNER` (`L3 — Cầm tay chỉ việc cho người mất gốc`). Viết chi tiết, dạy từ gốc cho người mất gốc, phủ đầy đủ theo `lesson_depth_contract`.
2. Chỉ dùng claims trong bảng và giữ `{claim:C-xxx}` gần claim tương ứng trong bản nháp để verifier truy vết.
3. Không thêm claim, PMID, guideline hoặc con số ngoài brief.
4. Chỉ dùng năm nhãn verification chuẩn: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`. Cấm tuyệt đối các nhãn cũ.
5. **Tách biệt nguồn:** Kiến thức consensus không cần nhãn/PMID; claim định lượng phải có evidence và exact quote. Không được bịa PMID/quote để làm bài dài.
6. Viết tiếng Việt có dấu; tiếng Việt trước, English trong ngoặc lần đầu.
7. Flowchart dùng `text` ASCII/danh sách phân cấp, KHÔNG DÙNG MERMAID.
8. Nếu một claim không đủ bằng chứng, bỏ claim thay vì suy diễn.
9. **Quy tắc dừng:** Dừng khi acceptance matrix & `lesson_depth_contract` thỏa mãn 100%. CẤM dừng vì "bài đã dài", CẤM lặp ý hay paraphrase padding.
10. Output gồm Markdown + cards V2; DOCX, APKG và learner smoke do release runner tạo trong `outputs/`.
