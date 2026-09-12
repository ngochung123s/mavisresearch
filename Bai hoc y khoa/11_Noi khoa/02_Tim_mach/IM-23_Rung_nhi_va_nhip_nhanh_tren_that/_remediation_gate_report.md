# Báo cáo gate remediation — IM-23 Rung nhĩ và nhịp nhanh trên thất

**Chạy:** 2026-07-18 | **Thư mục:** `11_Noi khoa/IM-23_Rung_nhi_va_nhip_nhanh_tren_that/`

## Kết quả gate

| Gate / lệnh | Exit code | Kết quả |
|---|---:|---|
| Preflight `preflight_guideline_check.py` cho ESC 2024 AF, ACC/AHA/ACCP/HRS 2023 AF, ESC 2019 SVT | 1 (WARN registry) | Registry chưa có các guideline tim mạch này; đã xác minh trực tiếp trang chính thức ESC và PubMed title trước viết; registry đã được cập nhật cùng đợt. |
| `verify_all_pmids.py <MD> --strict` | 0 | 3/3 PMID OK: 39210723, 38033089, 31504425. |
| `verify_claims.py <MD> --strict` | 0 | 3 OK, 0 WARN, 0 BLOCK. |
| `citation_audit.py <MD> --json` | 0 | `summary.block = 0`; 2 citations audited, đều PASS. |
| DOI gate | N/A | Không có DOI-only citation trong Markdown. |
| Structural contract check | 0 | Một H1; sections 0–13; 0.1; BOX ĐỎ trước 3.1; 2 Mermaid có narration; Plan A/B; 4 case năm bước; 5 lỗi; self-check; references. |
| Diacritics Markdown | 0 | 97.1% (2,449/2,523 từ Việt có dấu). |
| JSON deck contract | 0 | 80 basic cards; exact keys `type/front/back/extra`; 80 front chuẩn hóa duy nhất. |
| Build `build_apkg.py ... --verify` | 0 | Deck `Internal medicine::IM-23_Rung_nhi_va_nhip_nhanh_tren_that::2026-07-18`; 80 notes, 80 cards. |
| `verify_apkg_diacritics.py` | 0 | 97.0% (1,684/1,736), 80 notes. |

## Learner-path smoke tests

- **Irregular tachycardia + hypotension:** BOX ĐỎ, Mermaid, case 1 và cards đều kết thúc ở hồi sức có monitor + sốc điện đồng bộ/escalation hoặc chuyển khẩn; không có nhánh rate-control/anticoagulation ngoại trú.
- **Stable AF, onset uncertain:** flow 2, case 2 và cards đều dừng trước chuyển nhịp chọn lọc cho đến khi giải quyết đường chống đông/hình ảnh an toàn.
- **Thiết bị hạn chế:** Plan B vẫn yêu cầu ABC theo nhu cầu, monitor/đường truyền, gọi tuyến nhận và chuyển khẩn.

## Publication decision

**✅ GATES ĐẠT — đã xác minh strict PMID, strict claims, citation, structure, diacritics, JSON và APKG.**