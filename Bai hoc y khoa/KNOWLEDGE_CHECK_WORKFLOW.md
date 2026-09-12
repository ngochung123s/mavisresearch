# Knowledge Check Workflow — kiểm tra kiến thức sau mỗi bài học

Mục tiêu: sau khi tạo xong một bài học, luôn có một bài kiểm tra ngắn, có đáp án và có file điểm để theo dõi xem mình đã thật sự nắm bài chưa.

## Khi nào chạy?

Chạy sau khi đã có file flashcard:

```text
*.cards.v2.json
```
Thường nằm cùng folder với bài `.md` và `.apkg`.

## Cách yêu cầu Claude Code chạy

Copy prompt này và thay đường dẫn bài học:

```text
Sau khi tạo xong một bài học, hãy chạy knowledge check cho bài này:
<đường dẫn lesson.md hoặc cards.v2.json>

Yêu cầu:
1. Tạo file knowledge_check.md
2. Tạo answer_key.md
3. Tôi sẽ tự trả lời vào file knowledge_check.md
4. Sau đó hãy chấm điểm theo rubric, chỉ ra lỗ hổng kiến thức và tạo danh sách ôn lại.
```

## Nếu muốn tự chạy bằng terminal

```text
python "F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\make_knowledge_check.py" "<path-to-cards.v2.json>"
```

Ví dụ:

```text
python "F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\make_knowledge_check.py" "F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\08_GDM\GDM_Comprehensive\GDM_Comprehensive_2026-06-28.cards.v2.json"
```

Có thể đưa file `.md`; script sẽ tự tìm file `.cards.v2.json` cùng folder nếu chỉ có một file cards.

## File được tạo

Trong folder bài học sẽ có:

```text
<Topic>_knowledge_check.md
<Topic>_knowledge_check_answer_key.md
<Topic>_knowledge_check_score.json
```

Ý nghĩa:

- `knowledge_check.md`: bài kiểm tra để tự làm closed-book.
- `answer_key.md`: đáp án từ flashcard gốc.
- `score.json`: nơi lưu điểm, critical miss, weak areas.

## Cấu trúc bài kiểm tra

Bài kiểm tra luôn có 5 phần:

1. **Closed-book recall** — nhớ lại ý chính.
2. **Thresholds and numbers** — ngưỡng, %, OR/RR, liều, tuần, thời điểm.
3. **Cloze drill** — điền chỗ trống.
4. **Clinical mini-cases** — trả lời theo kiểu lâm sàng.
5. **Red-flag / common mistake check** — điểm dễ sai, điều cần tránh.

## Cách chấm

```text
0 = không nhớ / sai nguy hiểm
1 = nhớ ý chính nhưng thiếu số liệu hoặc điều kiện
2 = đúng đầy đủ, có ngưỡng/số liệu/ngoại lệ quan trọng
```

Ngưỡng đạt:

```text
≥80%: đạt
60-79%: cần ôn lại
<60%: chưa đạt, không nên coi là nắm bài
```

Critical miss:

```text
Sai dose/timing/protocol/cutoff quan trọng = phải ôn lại dù tổng điểm cao
```

## Workflow lặp lại sau mỗi bài
1. Tạo bài học `.md` và `.apkg` như thường lệ.
2. Chạy PMID/DOI/retraction/claim audit.
3. Chạy `make_knowledge_check.py` trên file cards.
4. Tự làm `knowledge_check.md` không nhìn đáp án.
5. Đưa file đã trả lời cho Claude chấm với `answer_key.md`.
6. Claude tạo danh sách phần yếu cần ôn lại.
7. Nếu cần, chuyển phần yếu thành flashcard bổ sung.

## Prompt chấm điểm

Sau khi tự trả lời, dùng prompt này:

```text
Hãy chấm bài knowledge check này cho tôi:
- Bài trả lời: <đường dẫn knowledge_check.md đã điền>
- Đáp án: <đường dẫn answer_key.md>
- Score file: <đường dẫn score.json>

Yêu cầu:
1. Chấm theo thang 0-1-2
2. Đánh dấu critical miss nếu sai ngưỡng/liều/timing/protocol/cutoff
3. Ghi điểm tổng, % đạt, weak areas vào score.json
4. Tạo danh sách ôn lại ngắn gọn
5. Nếu cần, đề xuất flashcard bổ sung
```
