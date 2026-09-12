# RESEARCH BRIEF: Sinh lý Nephron — Release v2
****Mã bài học:** IM-43a | Ngày khóa research:** 2026-07-22 | **Revision:** RELEASE v2 | **Model research:** Terra | **Model execute:** Terra

---

## 0. Lesson profile & release contract

Contract này được khóa **trước preflight và review/tái tạo artifact RELEASE v2**. Nó không sửa hoặc hợp thức hóa candidate ngày 2026-07-22 trước đó.

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

## 1. Source selection mới cho revision

| PMID | Vai trò cho RELEASE v2 | Giới hạn dùng |
|---|---|---|
| PMID: 10653444 | Bản đồ vận chuyển natri dọc nephron. | Cơ chế định hướng, không dùng liều hay protocol. |
| PMID: 11152761 | Vai trò Na+/K+-ATPase và điều hòa vận chuyển natri. | Cơ chế nền. |
| PMID: 11496061 | Định vị NHE3, NKCC2 và NCC. | Cơ chế theo đoạn. |
| PMID: 12642017 | Điều hòa vận chuyển ống thận qua angiotensin II. | Liên hệ thể tích/tưới máu. |
| PMID: 16914536 | Xử lý acid–base tại PCT. | Cơ chế bicarbonate/H+. |
| PMID: 19654544 | Điều hòa tái hấp thu muối PCT. | Cơ chế nền. |
| PMID: 21170887 | Vận chuyển acid–base PCT. | Cơ chế nền. |
| PMID: 35895103 | Điều hòa Na+ đoạn xa, NCC/ENaC và cân bằng nội môi. | Cơ chế distal nephron. |
| PMID: 30936153 | Cầu nối sang mục tiêu lợi tiểu theo nephron. | Chỉ liên kết, không dạy kê đơn. |
| PMID: 38490803 | Khung an toàn CKD, điện giải và đánh giá theo xu hướng. | Không dùng để tạo thuật toán điều trị bệnh-specific. |

**Nguồn textbook nền:** Hall JE, Hall ME. *Guyton and Hall Textbook of Medical Physiology*, 14th ed.

**Đã loại:** Không đưa tỷ lệ dịch tễ, liều thuốc, ngưỡng điều trị hoặc protocol bệnh-specific vào bài foundation. Các chủ đề này thuộc IM-20, IM-22, IM-40, IM-44 và bài Thuốc lợi tiểu.

## 2. Claims được phép sau preflight

- Nephron tạo nước tiểu bằng lọc cầu thận, tái hấp thu và bài tiết; PCT, quai Henle, DCT và ống góp có vai trò khác nhau trong nước–điện giải–acid/base. [ABSTRACT VERIFIED]
- NHE3 tại PCT, NKCC2 tại TAL và NCC tại DCT là các mắt xích có thể dùng để định vị vận chuyển NaCl. [ABSTRACT VERIFIED]
- TAL tái hấp thu NaCl mà không cho nước đi kèm, góp phần tạo gradient tủy; ADH làm ống góp thấm nước hơn khi gradient còn hiệu lực. [ABSTRACT VERIFIED]
- ENaC/aldosterone liên hệ với giữ Na+ và xu hướng bài tiết K+; diễn giải kali và acid–base luôn phải gắn xét nghiệm, thuốc và thể tích. [ABSTRACT VERIFIED]
- CKD, thay đổi creatinine nhanh, vô niệu, giảm tưới máu hoặc điện giải nguy hiểm cần đánh giá theo bối cảnh/chuyển tuyến, không suy luận từ một xét nghiệm đơn độc. [GUIDELINE VERIFIED]

### Số liệu CẤM dùng
- Không thêm tỷ lệ tái hấp thu, osmolarity, ngưỡng xét nghiệm, liều hay khoảng theo dõi nếu không được xác minh trực tiếp trong revision này.
- Không biến cơ chế nephron thành thuật toán kê thuốc hoặc điều trị CKD/suy tim/xơ gan/tăng huyết áp.

## 3. Execute contract

1. Candidate `Sinh_ly_nephron_2026-07-22.md` chỉ là input để review theo source set này; artifact release phải mang tên `RELEASE_v2`.
2. Giữ cấu trúc foundation: tổng quan, định nghĩa, cơ chế, chẩn đoán/theo dõi an toàn, flowchart, case, tips, tóm tắt và tài liệu tham khảo.
3. Chỉ tái tạo cards/APKG từ lesson release đã review; đủ 80 note `basic`, tiếng Việt có dấu.
4. Trước promotion, tất cả gate trong contract phải có một kết quả `PASS` duy nhất.