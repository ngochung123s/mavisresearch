# Báo cáo gate remediation — IM-22

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có 0.1, BOX ĐỎ, Mermaid + diễn giải, Plan A/Plan B, case, tham khảo và annotation chuẩn.
- Diacritics Markdown: 95.9% (3,536/3,687).
- JSON/APKG: 91 notes, 91 cards; deck `Internal medicine::IM-22_Suy_tim::2026-07-17`; diacritics APKG 96.3%.
- `citation_audit.py --json`: `summary.block = 0`.
- Protocol ICU không xác minh đã được thay bằng yêu cầu protocol ICU địa phương và chuyển tuyến.

## Chưa đạt — publication blocker
- `verify_all_pmids.py --strict`: 7 WARN do PubMed HTTP 429.
- `verify_claims.py --strict`: 5 BLOCK tại các ngữ cảnh trial chứa số chưa khớp abstract; cần tách/xóa số và rerun khi PubMed phục hồi.

## Learner-path exercise
- Warm/wet → giảm sung huyết có monitor theo protocol.
- Cold/wet/sốc → ICU/tim mạch; không tăng GDMT ngoại trú hay dùng protocol rút gọn.
