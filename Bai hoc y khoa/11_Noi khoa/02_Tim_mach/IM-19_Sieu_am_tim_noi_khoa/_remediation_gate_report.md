# Báo cáo gate remediation — Siêu âm tim Nội khoa

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có 0.1, BOX ĐỎ, Mermaid + diễn giải, Plan A/Plan B, case, tham khảo và annotation chuẩn.
- Diacritics Markdown: 94.3% (2,809/2,978).
- JSON/APKG: deck được mở rộng từ 29 lên 80 notes; 80 notes, 80 cards; deck `Internal medicine::IM_Sieu_am_tim_noi_khoa::2026-07-16`; diacritics APKG 96.2%.
- `verify_all_pmids.py --strict` và `verify_claims.py --strict`: exit 0 vì Markdown chỉ dùng DOI/official society URL; `citation_audit.py --json`: `summary.block = 0`.

## Publication status

**✅ GATES ĐẠT.** `verify_doi.py` xác minh 4/4 DOI (0 WARN, 0 BLOCK; Crossref Tier 1/Q1). Bài đã đạt structure, strict PMID/claim (không có PMID), citation audit, DOI, diacritics và APKG integrity.
## Learner-path exercise
- Report thiếu E/e′/LAVI/TAPSE → Plan B làm lại/echo chuyên khoa, không gọi bình thường.
- Dịch màng tim kèm tụt huyết áp/collapse → BOX ĐỎ, đường cấp cứu lâm sàng chứ không chỉ follow-up report.
