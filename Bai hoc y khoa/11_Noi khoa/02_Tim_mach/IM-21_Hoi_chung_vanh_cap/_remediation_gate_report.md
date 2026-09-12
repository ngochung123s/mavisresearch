# Báo cáo gate remediation — IM-21

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có 0.1, BOX ĐỎ, 3 Mermaid và diễn giải từng flow, Plan A/Plan B, case, tham khảo, annotation chuẩn.
- Diacritics Markdown: 95.0% (8,307/8,746).
- JSON/APKG: 99 notes, 99 cards; deck `Internal medicine::IM-21_Hoi_chung_vanh_cap::2026-07-17`; diacritics APKG 94.5%.
- `citation_audit.py --json`: `summary.block = 0`.

## Chưa đạt — publication blocker
- `verify_all_pmids.py --strict`: 5 WARN do PubMed HTTP 429.
- `verify_claims.py --strict`: 6 WARN vì abstract không truy xuất được/rút ngắn trong đợt 429; không có BLOCK nhưng strict exit khác 0.

## Learner-path exercise
- STEMI không có PCI chỉ đi nhánh tái tưới máu sau khi kiểm thời điểm, chống chỉ định, protocol đã xác minh và năng lực xử trí chảy máu; nếu thiếu dữ kiện/năng lực → chuyển PCI.
- ECG đầu bình thường nhưng triệu chứng còn → ECG/troponin nối tiếp hoặc chuyển cấp cứu, không xuất viện.
