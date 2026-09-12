# Báo cáo gate remediation — IM-24 Nhịp chậm, block nhĩ thất và loạn nhịp thất

**Chạy:** 2026-07-18 | **Thư mục:** `11_Noi khoa/IM-24_Nhip_cham_block_nhi_that_va_loan_nhip_that/`

## Kết quả gate

| Gate / lệnh | Exit code | Kết quả |
|---|---:|---|
| Preflight `preflight_guideline_check.py` cho ESC 2021 pacing và ESC 2022 ventricular arrhythmia | 1 (WARN registry) | Registry chưa có các guideline tim mạch này; đã xác minh trực tiếp trang chính thức ESC và PubMed title trước viết; registry đã được cập nhật cùng đợt. |
| `verify_all_pmids.py <MD> --strict` | 0 | 2/2 PMID OK: 34455430, 36017572. |
| `verify_claims.py <MD> --strict` | 0 | 2 OK, 0 WARN, 0 BLOCK. |
| `citation_audit.py <MD> --json` | 0 | `summary.block = 0`; 2 citations audited, đều PASS. |
| DOI gate | N/A | Không có DOI-only citation trong Markdown. |
| Structural contract check | 0 | Một H1; sections 0–13; 0.1; BOX ĐỎ trước 3.1; 2 Mermaid có narration; Plan A/B; 4 case năm bước; 5 lỗi; self-check; references; pulseless handoff sang IM-18, không lặp arrest lesson. |
| Diacritics Markdown | 0 | 97.1% (1,761/1,814 từ Việt có dấu). |
| JSON deck contract | 0 | 80 basic cards; exact keys `type/front/back/extra`; 80 front chuẩn hóa duy nhất. |
| Build `build_apkg.py ... --verify` | 0 | Deck `Internal medicine::IM-24_Nhip_cham_block_nhi_that_va_loan_nhip_that::2026-07-18`; 80 notes, 80 cards. |
| `verify_apkg_diacritics.py` | 0 | 96.3% (1,370/1,423), 80 notes. |

## Learner-path smoke tests

- **Symptomatic high-grade AV block, first-line non-response:** flow 1, case 1 và cards kết thúc ở pacing qua da và/hoặc dopamine/epinephrine theo AHA, expert help và urgent transfer; không quan sát.
- **Undifferentiated regular wide-complex tachycardia:** flow 2, case 3 và cards coi là VT tiềm tàng; không kết thúc bằng empiric AV-nodal blockade.
- **Thiết bị hạn chế:** Plan B vẫn yêu cầu ABC, monitor, gọi tuyến nhận và chuyển khẩn khi giảm tưới máu/block cao độ/VT nguy hiểm.

## Publication decision

**✅ GATES ĐẠT — đã xác minh strict PMID, strict claims, citation, structure, diacritics, JSON và APKG.**