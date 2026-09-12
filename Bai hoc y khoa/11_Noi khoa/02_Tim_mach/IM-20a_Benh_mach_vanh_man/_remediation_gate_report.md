# Báo cáo gate remediation — IM-20a

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có `0.1`, BOX ĐỎ, Mermaid + diễn giải ngay sau flow, Plan A/Plan B, case, tài liệu tham khảo và annotation chuẩn.
- Diacritics Markdown: 95.4% (4,710/4,938).
- JSON: 80 notes. APKG được build lại và kiểm tra: 80 notes, 80 cards, deck `Internal medicine::IM-20a_Benh_mach_vanh_man::2026-07-17`, diacritics 94.9%.
- `citation_audit.py --json`: `summary.block = 0`.

## Chưa đạt — publication blocker
- `verify_all_pmids.py --strict`: 5 WARN vì PubMed E-utilities trả HTTP 429.
- `verify_claims.py --strict`: 3 BLOCK ở ngữ cảnh FOURIER (28304224), ODYSSEY OUTCOMES (30403574), CLEAR Outcomes (36876740): context rộng vẫn bắt các số không thuộc claim thử nghiệm. Không công bố là hoàn tất cho đến khi các đoạn số được tách/xóa và gate chạy 0 sau khi dịch vụ PubMed phục hồi.

## Learner-path exercise
- Đau gắng sức ổn định → sàng red flag âm tính → CCTA/stress imaging hoặc Plan B có chuyển tuyến.
- Đau nghỉ mới/tăng dần → BOX ĐỎ → ECG + hs-cTn → workflow ACS; không hẹn test ngoại trú.
