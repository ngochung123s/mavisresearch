# Medical Q&A

> Workflow tra cứu nhanh câu hỏi y khoa cho `mavisresearch`.
> Nội dung tiếng Việt có dấu; tên file QA tiếng Việt theo câu hỏi, không kèm ngày.

## Mục tiêu

- Lưu câu hỏi y khoa thường gặp để tìm lại nhanh.
- Giữ đủ nguồn và mức chắc chắn để tránh nhầm với kết luận y khoa chắc chắn.
- Cho phép nâng cấp câu hỏi quan trọng thành bài học đầy đủ trong `Bai hoc y khoa/`.

## Cấu trúc

```text
medical_qa/
  README.md
  _INDEX.md
  english_terms.md
  templates/
    qa_template.md
    case_template.md
  by_topic/
    sieu-am-thai/
  by_month/
    2026-07.md
```

Chỉ tạo topic folder khi có câu hỏi thật trong topic đó. Không giữ folder rỗng.

## Quy ước file

Mỗi câu hỏi là một file riêng trong `by_topic/<topic>/`:

```text
tên-câu-hỏi-bằng-tiếng-việt.md
```

Ví dụ:

```text
đau-đầu-kèm-buồn-nôn-có-nguy-hiểm-không.md
khi-nào-dùng-aspirin-trong-thai-kỳ.md
```

Ngày ghi bên trong file ở dòng `Ngày: YYYY-MM-DD`, không đưa vào tên file.

## Workflow hằng ngày

1. User hỏi câu hỏi y khoa.
2. Agent phải tạo todo ngay từ đầu: trả lời trong chat, lưu QA, cập nhật `_INDEX.md`, cập nhật `english_terms.md` nếu có thuật ngữ tiếng Anh.
3. Agent trả lời trong chat trước.
4. Nếu câu hỏi phù hợp lưu QA, agent tự lưu ngay sau khi trả lời, không chờ user nhắc lại.
5. Agent tạo file Markdown từ `templates/qa_template.md` hoặc `templates/case_template.md`.
6. Agent đặt file vào `by_topic/<topic>/`; nếu topic folder chưa có thì tạo mới.
7. Agent thêm một dòng vào `_INDEX.md`.
8. Nếu câu hỏi đủ lớn, đánh dấu `Promote: daily lesson`.

## Verify nguồn nhanh

- Ưu tiên PubMed MCP nếu agent hiện tại expose tool MCP native.
- Nếu không có MCP native, dùng BioMCP CLI trong PowerShell:
  - `biomcp search article --source pubmed -k "QUERY" --limit 5`
  - `biomcp get article PMID`
- Nếu BioMCP lỗi, bị rate-limit ngoài PubMed, hoặc không trả kết quả phù hợp, fallback E-utilities qua `webfetch`.
- Không cite PMID nếu chưa fetch title/abstract để xác nhận đúng bài.
- Với RR/OR/CI/%/n= hoặc protocol detail, vẫn cần PMID và mức verify rõ; nếu chưa đủ thì ghi `Cần kiểm chứng`.

## English term extraction

- Khi người dùng gửi một đoạn tiếng Anh y khoa, agent phải lọc các thuật ngữ tiếng Anh chuyên ngành và cập nhật `english_terms.md`.
- Mỗi thuật ngữ chỉ được lưu một lần; trước khi thêm phải kiểm tra tránh trùng.
- Không lưu từ tiếng Anh phổ thông, chỉ lưu thuật ngữ có giá trị làm flashcard sau này.
- Giữ nguyên tiếng Anh gốc; có thể thêm nghĩa tiếng Việt ngắn sau dấu `—` khi chắc chắn.

## Quy tắc thuật ngữ trong QA

- QA viết cho người Việt đọc nhanh, nên thuật ngữ tiếng Việt phải đứng trước.
- Nếu dùng thuật ngữ tiếng Anh chuyên ngành, chú thích tiếng Việt ngay lần đầu trong cùng câu: `tiếng Việt (English)`.
- Không để một chuỗi thuật ngữ Anh không giải thích. Ví dụ sai: `overgrowth, mTORopathy, cortical mantle`. Ví dụ đúng: `phát triển quá mức (overgrowth), bệnh do đường truyền mTOR (mTORopathy), lớp vỏ não còn lại (cortical mantle)`.
- `english_terms.md` vẫn lưu thuật ngữ Anh để làm vocab, nhưng trong nội dung QA/card phải có nghĩa Việt cạnh thuật ngữ khó.

## Quy tắc trình bày bảng (CẬP NHẬT 2026-07-05)

- KHÔNG dùng bảng Markdown `|...|` phức tạp (>=4 cột hoặc nhiều dòng dài) trong QA.
- Thay bằng **danh sách có tiêu đề**: dùng `### heading` làm tiêu đề nhóm, rồi liệt kê từng mục bằng `- bullet`.
- Mỗi mục ghi `tên: giá trị` hoặc `tên - giải thích`.
- Bảng đơn giản 2 cột ngắn vẫn được phép nếu thực sự cần.

## Mức chắc chắn

| Mức | Khi dùng |
|---|---|
| Cao | Có guideline hoặc nguồn mạnh, phù hợp câu hỏi |
| Trung bình | Có PubMed/PMID phù hợp nhưng chưa full verify |
| Thấp | Dựa trên cơ chế hoặc nguồn thứ cấp |
| Cần kiểm chứng | Câu trả lời tạm, chưa có nguồn đủ tốt |

## Rule citation

- Không ghi số RR/OR/CI/%/n= nếu chưa kiểm chứng.
- Nếu có số liệu cụ thể: bắt buộc PMID + `[FULL VERIFIED]`.
- Nếu là liều thuốc, protocol, timing, route, sequence, duration: bắt buộc nguồn rõ.
- Nếu là triệu chứng nguy hiểm: bắt buộc có mục `Khi nào cần đi khám/cấp cứu`.
- Không lưu định danh bệnh nhân.

## Tag chuẩn

```text
#san-phu-khoa #phu-khoa #art-ivf #sieu-am-thai #thuoc #xet-nghiem
#trieu-chung #cap-cuu #co-che #guideline #pmid #chua-kiem-chung
#case #benh-nhan
```
