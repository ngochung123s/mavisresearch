# Báo cáo gate remediation — IM-14 Rối loạn đường huyết cấp trong 15 phút đầu

**Chạy:** 2026-07-18 | **Thư mục:** `11_Noi khoa/IM-14_Roi_loan_duong_huyet_cap_15_phut_dau/`

## Kết quả gate

| Gate / lệnh | Exit code | Kết quả |
|---|---:|---|
| Preflight `preflight_guideline_check.py` cho ADA 2026, ADA/EASD 2024, JBDS 2023 | 0 / 0 / 0 | Registry mới nhận diện đúng 3 guideline hiện hành trước khi viết. |
| `python -m json.tool` cho hai registry + `python -m py_compile citation_audit.py` | 0 | Hai JSON hợp lệ; citation auditor biên dịch được. |
| `verify_all_pmids.py <MD> --strict` | 0 | 2/2 PMID OK: 39052901, 41358894. NCBI E-utilities trả trang chặn tạm thời; verifier đã dùng Europe PMC metadata fallback và xác minh title/journal/year. |
| `verify_claims.py <MD> --strict` | 0 | 2 OK, 0 WARN, 0 BLOCK. Không có claim tỷ lệ thử nghiệm; guideline tags bao phủ các chi tiết vận hành. |
| `citation_audit.py <MD> --json` | 0 | `summary.block = 0`; 2 citation guideline Tier 0 PASS. |
| Diacritics repository | 0 | Script báo không có Markdown dưới root cũ `09_Source - Markdown`; không quét IM-14. |
| Diacritics Markdown IM-14 độc lập | 0 | 96,0% (1.902/1.982 từ tiếng Việt có dấu). |
| Structural contract + JSON deck contract | 0 | Một H1; sections 0–13; 0.1; BOX ĐỎ trước 3.1; 2 Mermaid có narration; Plan A/B; 4 case năm bước; 5 lỗi; self-check; references; 80 basic cards, exact keys, 80 fronts chuẩn hóa duy nhất. |
| Build `build_apkg.py ... --verify` | 0 | Deck `Internal medicine::IM-14_Roi_loan_duong_huyet_cap_15_phut_dau::2026-07-18`; 80 notes, 80 cards. |
| `verify_apkg_diacritics.py` | 0 | 98,2% (1.761/1.793), 80 notes. |

## Learner-path smoke tests

- **52 mg/dL, tỉnh và nuốt an toàn:** flow 1, case 1 và cards chỉ định dừng insulin truyền nếu có, cho 15–20 g carbohydrate nhanh, đo lại 10–15 phút, lặp tối đa ba chu kỳ và escalation nếu còn <4,0 mmol/L sau 30–45 phút.
- **38 mg/dL, bất tỉnh:** flow 1, case 2 và cards cấm đường uống, bắt đầu ABCDE/gọi hỗ trợ, dùng 100 mL glucose 20% hoặc 200 mL glucose 10% IV trong 15 phút nếu có đường truyền; nếu chưa có IV dùng glucagon 1 mg IM; đo lại sau 10 phút.
- **SGLT2 + glucose 180 mg/dL + nôn/Kussmaul/ketone:** flow 2, case 3 và cards không trấn an bởi glucose; kích hoạt DKA euglycemic/IM-52 protocol.
- **Người cao tuổi suy tim, mất nước, nghi HHS:** flow 2, case 4 và cards chọn bolus 250 mL rồi đánh giá lại, không mặc định 500–1.000 mL/giờ.
- **Nghi DKA, kali 3,2 mmol/L:** flow 2, case 4 và cards đi tới điểm dừng “trì hoãn insulin, kích hoạt protocol kali”; không có liều insulin tự đặt.

## Publication decision

**✅ GATES ĐẠT — strict PMID, strict claims, citation, structure, diacritics, JSON và APKG đã xác minh.**
