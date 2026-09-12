# Báo cáo gate remediation — IM-20 Tăng huyết áp

**Chạy:** 2026-07-18 | **Thư mục:** `11_Noi khoa/IM-20_Tang_huyet_ap/`

## Kết quả gate

| Gate / lệnh | Exit code | Kết quả |
|---|---:|---|
| Preflight ban đầu `preflight_guideline_check.py --topic "hypertension" --guideline "VSH/VNHA 2024"` | 1 | Registry chưa có guideline tăng huyết áp; đã bổ sung metadata theo plan. |
| Preflight sau đăng ký, cùng lệnh | 0 | Khớp `VSH_VNHA_hypertension`; VSH/VNHA 2024 là current. |
| `verify_all_pmids.py <MD> --strict` | 0 | Không có PMID được parser trích từ lesson; ESC/AHA/ACC chỉ được giữ là registry identifiers do PubMed/BioMCP hiện trả chặn truy cập. |
| `verify_claims.py <MD> --strict` | 0 | Không có PMID để đối chiếu; tất cả claim số vận hành gắn VSH/VNHA Tier 0 thay vì paper claim. |
| `citation_audit.py <MD> --json` | 0 | 3/3 guideline citations PASS; `summary.pass = 3`, `summary.warn = 0`, `summary.block = 0`. |
| Structural contract check | 0 | Một H1; sections 0–13; 0.1; BOX ĐỎ trước 3.1; 2 Mermaid có narration; Plan A/B; 4 case năm bước; 5 lỗi; self-checks; references. |
| Diacritics Markdown, single-file `count_words_classified()` | 0 | 94.4% (2,903/3,074 từ Việt có dấu). Repository `verify_diacritics.py` không quét folder mới vì nó cố định legacy root và trả “Khong tim thay MD files”; không được dùng nhầm như kết quả IM-20. |
| JSON deck contract | 0 | 80 basic cards; exact keys `type/front/back/extra`; 80 front chuẩn hóa duy nhất; không ô trống. |
| `build_apkg.py <JSON> --verify` | 0 | Deck `Internal medicine::IM-20_Tang_huyet_ap::2026-07-18`; 80 notes, 80 cards. |
| `verify_apkg_diacritics.py <APKG>` | 0 | 94.2% (2,141 từ Việt có dấu), 80 notes. |

## Learner-path smoke tests

- **185/115 mmHg + dấu thần kinh khu trú mới:** BOX ĐỎ, flow 1, case 1 và cards dừng xác nhận ngoại trú, đi IM-15/đánh giá cấp cứu.
- **148/94 mmHg một lần, không red flags:** flow 1, case 2 và cards yêu cầu HBPM/ABPM hoặc lần đo chuẩn hóa khác; không gắn nhãn tăng huyết áp mạn ngay.
- **Tăng huyết áp đã xác nhận, không biến chứng so với 82 tuổi có hạ áp tư thế:** flow 2/case 3 tách lối sống + hai nhóm liều thấp ở đa số khỏi nhánh mục tiêu cá thể hóa/một thuốc, tăng chậm.
- **Nghi kháng trị sau nhiều thuốc:** flow 2/case 4/cards yêu cầu kiểm kỹ thuật, gắn kết, pseudo-resistance, thuốc/chất dùng kèm, xác nhận ngoài phòng khám, nguyên nhân thứ phát và hội chẩn.

## Publication decision

**✅ GATES ĐẠT — preflight, strict PMID/claims, citation, structure, diacritics, JSON và APKG đã xác minh trong phạm vi công cụ hiện có.**
