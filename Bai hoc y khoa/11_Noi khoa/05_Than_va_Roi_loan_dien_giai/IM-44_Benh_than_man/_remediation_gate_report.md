# Báo cáo gate remediation — IM-44

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có 0.1, BOX ĐỎ, flow `[CỐT LÕI]` + diễn giải, Plan A/Plan B, case, tham khảo và annotation chuẩn.
- Diacritics Markdown: 94.4% (4,603/4,876).
- JSON/APKG: 85 notes, 85 cards; deck `Internal medicine::IM-44_Benh_than_man::2026-07-17`; diacritics APKG 93.8%.
- `citation_audit.py --json`: `summary.block = 0`.
- Giá/BHYT/cung ứng Việt Nam không xác minh đã chuyển sang hướng dẫn theo năng lực.

## Chưa đạt — publication blocker
- `verify_all_pmids.py --strict`: 6 WARN do PubMed HTTP 429.
- `verify_claims.py --strict`: 1 BLOCK tại ngữ cảnh PMID 11565518 và 5 WARN do abstract không có/không đủ; cần xóa/tách các số không xác minh và rerun khi PubMed phục hồi.

## Learner-path exercise
- eGFR giảm chưa đủ 3 tháng → đánh giá AKI/lặp xét nghiệm, không dán nhãn CKD.
- G4 hoặc biến chứng kháng trị → chuyển thận; thiếu UACR dùng sàng lọc/UPCR và gửi xét nghiệm, không loại trừ giả.
