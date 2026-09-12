# Báo cáo gate remediation — IM-51

**Chạy:** 2026-07-18

## Đạt
- Structural audit: có 0.1, BOX ĐỎ, 2 Mermaid + diễn giải, Plan A/Plan B, case, tham khảo và annotation chuẩn.
- Diacritics Markdown: 93.9% (5,880/6,260).
- JSON/APKG: 90 notes, 90 cards; deck `Internal medicine::IM-51_Dai_thao_duong::2026-07-16`; diacritics APKG 93.6%.
- `citation_audit.py --json`: `summary.block = 0`.
- DKA/HHS protocol chi tiết đã được rút khỏi nhánh ngoại trú; bài chỉ nhận diện, kích hoạt protocol cấp cứu và chuyển tuyến.

## Chưa đạt — publication blocker
- `verify_all_pmids.py --strict`: 1 BLOCK (PMID 33441402 bị false-positive “suspicious title”) và 11 WARN do PubMed HTTP 429.
- `verify_claims.py --strict`: 8 BLOCK tại các ngữ cảnh số liệu trial/review; cần rà từng số với abstract/full text hoặc đổi thành claim định hướng trước rerun.

## Learner-path exercise
- Tăng đường huyết ngoại trú không red flag → xác nhận chẩn đoán, đánh giá bệnh kèm, điều trị/Plan B an toàn.
- Ketone/toan hoặc hạ đường huyết cần hỗ trợ → BOX ĐỎ → cấp cứu; Plan B không thay DKA/HHS care.
