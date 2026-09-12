# Nội khoa người lớn

## Chọn bài học ở đâu?

Xem danh sách đầy đủ 108 lựa chọn tại [`../_CURRICULUM_NOI_KHOA.md`](../_CURRICULUM_NOI_KHOA.md).

- Cột **ID** là mã để chọn, ví dụ `IM-01`, `IM-14`, `IM-36`, hoặc `IM-C1`.
- Cột **Ưu tiên**: `P0` = lõi; `P1` = nâng cao; `P2` = ca tích hợp.
- Cột **Phụ thuộc** cho biết kiến thức cần học trước.
- Cột **Trạng thái**: `❌ CHƯA CÓ` nghĩa là chưa có bài học/deliverable.

Bạn chỉ cần nhắn một mã, một dải mã, hoặc một block. Ví dụ:

- `Làm IM-01`
- `Làm Block 0`
- `Làm IM-07 đến IM-18`

## Thứ tự khuyến nghị

Bắt đầu theo P0, đặc biệt:

1. **Block 0 — Nền tảng tư duy và an toàn lâm sàng:** `IM-01` đến `IM-06`.
2. **Block 1 — Cấp cứu và hội chứng cấp tính:** `IM-07` đến `IM-18`.
3. Sau đó học các block cơ quan P0: tim mạch, hô hấp, tiêu hóa–gan mật, thận–điện giải, nội tiết và nhiễm trùng.
4. P1 và các ca P2 học sau khi hoàn thành nền P0 liên quan.

Các lesson đã build nằm trong folder con `IM-XX_Ten_bai/`. Trạng thái chỉ được gọi là hoàn tất khi evidence, citation, diacritic và APKG gates đều đạt; xem `_remediation_gate_report.md` trong từng folder khi bài đang remediation.

## Bài đã build — trạng thái xác minh

| ID | Bài học | Ngày | Trạng thái xác minh |
|---|---|---|---|
| IM-01 | Cách tiếp cận bệnh nhân Nội khoa người lớn | 2026-07-22 | ✅ GATES ĐẠT — strict PMID/claims, citation 0 BLOCK, foundation profile, diacritics, DOCX và APKG (20 notes/22 cards) đã smoke-test |
| IM-07 | Tiếp cận bệnh nhân khó thở cấp và suy hô hấp | 2026-07-22 | ✅ GATES ĐẠT — strict PMID/claims, citation 0 BLOCK, disease profile, diacritics và APKG (36 notes/36 cards) đã smoke-test |
| IM-20 | Tăng huyết áp | 2026-07-18 | ✅ GATES ĐẠT — strict PMID/claims, citation, structure, diacritics và APKG đã xác minh |
| IM-20a | Bệnh mạch vành mạn (CCS/CCD) | 2026-07-17 | 📋 strict PMID/claim gate chưa đạt |
| IM-21 | Hội chứng vành cấp | 2026-07-17 | 📋 strict PMID gate bị HTTP 429 |
| IM-22 | Suy tim cấp và mạn | 2026-07-17 | 📋 strict claim gate còn BLOCK |
| IM-23 | Rung nhĩ và nhịp nhanh trên thất | 2026-07-18 | ✅ GATES ĐẠT — strict PMID/claims, citation, structure, diacritics và APKG đã xác minh |
| IM-24 | Nhịp chậm, block nhĩ thất và loạn nhịp thất | 2026-07-18 | ✅ GATES ĐẠT — strict PMID/claims, citation, structure, diacritics và APKG đã xác minh |
| IM-44 | Bệnh thận mạn | 2026-07-17 | 📋 strict claim gate còn BLOCK |
| IM-51 | Đái tháo đường type 1 / type 2 | 2026-07-16 | 📋 strict PMID/claim gate chưa đạt |
| — | Siêu âm tim Nội khoa — Chỉ số & Đọc kết quả | 2026-07-16 | ✅ GATES ĐẠT — DOI, structure và APKG đã xác minh |

Mỗi folder có Markdown, card JSON, APKG đã smoke-test và `_remediation_evidence.md`/`_remediation_gate_report.md`; APKG không thay thế source gate.

