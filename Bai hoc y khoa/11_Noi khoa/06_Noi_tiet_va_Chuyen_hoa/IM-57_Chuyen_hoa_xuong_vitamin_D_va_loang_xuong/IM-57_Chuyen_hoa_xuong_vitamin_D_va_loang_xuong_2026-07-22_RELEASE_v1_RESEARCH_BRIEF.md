# RESEARCH BRIEF: IM-57 — Chuyển hóa xương, vitamin D và loãng xương
**Ngày:** 2026-07-22 | **Profile:** foundation | **Đối tượng:** người học mất nền

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "profile_foundation",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "learner_smoke"
  ],
  "not_applicable": [],
  "approved_exemptions": []
}
```

**Output basename đã khóa:** `IM-57_Chuyen_hoa_xuong_vitamin_D_va_loang_xuong_2026-07-22_RELEASE_v1`.

## 1. Preflight guideline và phạm vi

- `preflight_guideline_check.py` đã chạy riêng cho NOGG 2024, Endocrine Society 2024, ISCD 2023 và USPSTF 2025: cả bốn trả **WARN**, không có BLOCK. Registry không có các key osteoporosis/bone density/screening; riêng heuristic vitamin D ghép nhầm ESC 2019. Không sửa registry để hợp thức hóa kết quả.
- Freshness đã xác nhận trực tiếp: NOGG official page ghi **Updated December 2024**; ISCD Adult Official Positions ghi cập nhật/được chấp thuận năm 2023; Endocrine Society guideline là PMID: 38828931. USPSTF là trục screening US; do official URL thay đổi/không fetch được, không dùng cutoff USPSTF trong bài.
- NOGG là khung UK: ngưỡng/công cụ theo NOGG **không phải ngưỡng Việt Nam**. Khi dùng FRAX, dùng model quốc gia phù hợp nếu có; không thay model UK bằng suy đoán.
- IM-57 sở hữu remodeling, vitamin D, nguy cơ gãy, DXA/FRAX, osteoporosis, nguyên nhân thứ phát, điều trị và theo dõi. Chỉ nối tuyến sang IM-55 (rối loạn calcium/phosphat/PTH), IM-44 (CKD), IM-88 (té ngã) và IM-81–86 (cơ xương khớp), không dạy lại chúng.

## 2. Papers đã chọn

| PMID | Loại | Vai trò đã xác nhận |
|---|---|---|
| 35478046 | BHOF Clinician’s Guide | Gãy ở người lớn tuổi là sentinel event; prevention, diagnosis, treatment, monitoring. |
| 38828931 | Endocrine Society guideline | Không dùng xét nghiệm 25(OH)D thường quy để phòng bệnh ở người không có chỉ định; không dùng bổ sung quá mức thường quy. |
| 40921943 | NOGG 2024 guideline | Case finding, risk assessment, thuốc, sequence và follow-up. |
| 39808425 | USPSTF final recommendation | Screening women from age 65; selective screening of younger postmenopausal women at increased risk; scope and limits. |
| 19671655 | FREEDOM RCT | Denosumab so với placebo ở phụ nữ sau mãn kinh osteoporosis; outcome vertebral/nonvertebral/hip fracture. |
| 17476007 | HORIZON RCT | Zoledronic acid so với placebo ở postmenopausal osteoporosis; fracture outcomes. |
| 28892457 | ARCH RCT | Romosozumab rồi alendronate so với alendronate ở phụ nữ osteoporosis có fragility fracture. |
| 29129436 | VERO RCT | Teriparatide so với risedronate ở phụ nữ sau mãn kinh severe osteoporosis; fracture outcomes. |
| 11346808 | PTH RCT | PTH(1-34) so với placebo ở phụ nữ sau mãn kinh có vertebral fracture. |
| 7477143 | Alendronate RCT | Alendronate so với placebo ở phụ nữ postmenopausal osteoporosis. |
| 17190893 | FLEX RCT | Continuing versus stopping alendronate after prior treatment. |
| 21411557 | FREEDOM subgroup RCT analysis | Denosumab fracture outcomes in higher-risk subgroups. |

**Đã loại:** PMID 25182228 là Clinician’s Guide cũ, abstract quá ngắn để đóng claim; không dùng làm nguồn claim. Không dùng số liệu, liều hoặc protocol trial trong lesson/cards chỉ để làm phong phú bài.

## 3. Claims đã khóa

| # | Claim được phép | Nguồn | Tag |
|---|---|---|---|
| 1 | Xương liên tục được remodeling bởi osteoclast, osteoblast và osteocyte; mất cân bằng kéo dài làm suy giảm khối lượng/chất lượng xương. | Harrison’s 21e; NOGG 2024 | [TEXTBOOK; GUIDELINE VERIFIED] |
| 2 | Gãy fragility là gãy sau lực thấp; một gãy ở người từ trung niên trở lên là tín hiệu đánh giá nguy cơ gãy tiếp theo, không chờ DXA mới xử trí secondary prevention. | PMID: 35478046; NOGG 2024 | [ABSTRACT VERIFIED; GUIDELINE VERIFIED] |
| 3 | DXA đo BMD; ở phụ nữ sau mãn kinh và nam từ 50 tuổi, T-score dùng cho phân loại densitometry; người trẻ hơn ưu tiên Z-score và không chẩn đoán osteoporosis chỉ từ BMD. | ISCD 2023 | [GUIDELINE VERIFIED] |
| 4 | FRAX kết hợp clinical risk factors, có thể dùng có hoặc không có femoral-neck BMD; output không thay clinical judgement, không đo đáp ứng thuốc và phải dùng model quốc gia phù hợp. | NOGG 2024 | [GUIDELINE VERIFIED] |
| 5 | Người có osteoporosis/fragility fracture cần tìm nguyên nhân thứ phát; low BMD không tự phân biệt osteomalacia, CKD-MBD, cường cận giáp, myeloma hay di căn. | NOGG 2024; ISCD 2023 | [GUIDELINE VERIFIED] |
| 6 | Nền tảng phòng gãy gồm vận động chịu lực/kháng lực phù hợp, dinh dưỡng, calcium ưu tiên từ khẩu phần, tránh thuốc lá/rượu quá mức và phòng té ngã; không thay thế thuốc khi thuốc được chỉ định. | PMID: 35478046 | [ABSTRACT VERIFIED] |
| 7 | Antiresorptive là lựa chọn đầu tay ở đa số người có nguy cơ gãy; very-high risk có thể phù hợp anabolic/dual-action rồi antiresorptive nối tiếp. | NOGG 2024; PMID: 28892457; PMID: 29129436 | [GUIDELINE VERIFIED; ABSTRACT VERIFIED] |
| 8 | Trước parenteral anti-osteoporosis therapy phải nhận diện và xử lý hypocalcemia/vitamin D deficiency thích hợp; CKD hoặc rối loạn chuyển hóa phức tạp cần chọn/chuyển chuyên khoa an toàn. | NOGG 2024 | [GUIDELINE VERIFIED] |
| 9 | Không được tự ngừng hoặc trì hoãn denosumab khi chưa có kế hoạch antiresorptive tiếp theo vì nguy cơ vertebral fracture tăng sau ngừng không có kế hoạch. | NOGG 2024; PMID: 19671655 | [GUIDELINE VERIFIED; ABSTRACT VERIFIED] |
| 10 | Đau đùi/bẹn/hip không giải thích ở người dùng antiresorptive cần nghĩ AFF và imaging femur; triệu chứng răng miệng/dental disease cần đánh giá trước quản lý thích hợp. | NOGG 2024 | [GUIDELINE VERIFIED] |
| 11 | Ở người không có established indication, Endocrine Society không ủng hộ routine 25(OH)D testing chỉ để phòng bệnh; điều này không áp dụng để bỏ qua đánh giá người nghi deficiency/osteomalacia. | PMID: 38828931 | [ABSTRACT VERIFIED] |
| 12 | USPSTF 2025 applies to adults without known osteoporosis, fragility fracture, secondary osteoporosis or chronic bone-loss medication exposure: screen women from age 65 with central DXA, with or without fracture-risk assessment; for younger postmenopausal women, first identify risk factors then use clinical risk assessment before DXA. Evidence is insufficient for population screening in men. | PMID: 39808425; USPSTF 2025 | [ABSTRACT VERIFIED; GUIDELINE VERIFIED] |

## 4. Kiến thức nền có nguồn

| Kiến thức | Nguồn |
|---|---|
| Xương vỏ tạo vỏ cứng; xương bè có mạng bè chịu lực và chuyển hóa nhanh hơn. | [TEXTBOOK: Harrison’s 21e, metabolic bone disease] |
| Osteoblast tạo osteoid; osteoclast tiêu xương; osteocyte cảm nhận tải lực và điều phối remodeling. | [TEXTBOOK: Robbins & Cotran 10e, bone] |
| Vitamin D từ da/thức ăn được chuyển thành 25(OH)D, rồi dạng hoạt động; PTH, calcium và phosphat phối hợp duy trì khoáng hóa. | [TEXTBOOK: Harrison’s 21e, calcium and bone metabolism] |

## 5. Số liệu CẤM dùng

- Không đưa ngưỡng vitamin D, liều calcium/vitamin D, interval DXA, duration drug holiday, liều/lịch từng thuốc, hoặc threshold treatment của UK vào bài/cards nếu không kèm trực tiếp guideline/full-text phù hợp thực hành địa phương.
- Không đưa số liệu hiệu quả RCT (RR, CI, phần trăm, cỡ mẫu) vào bài/cards.
- Không biến T-score đơn lẻ hoặc 25(OH)D đơn lẻ thành chẩn đoán mọi đau xương/gãy xương.

## 6. Dàn ý thực thi

1. Tổng quan và hộp phạm vi; dạy nền tảng ngay tại chỗ.
2. Định nghĩa fragility fracture, osteoporosis, osteomalacia và mục tiêu giảm gãy.
3. Cơ chế: remodeling, ageing, vitamin D/PTH/calcium/phosphat; nối cơ chế với gãy.
4. Chẩn đoán: BOX ĐỎ trước nhánh ngoại trú; risk factors, DXA T/Z score, FRAX, secondary work-up, differential và Plan B thiếu DXA.
4a. Screening: case phụ nữ 67 tuổi chưa có gãy/known osteoporosis thuộc scope USPSTF; giải thích DXA central có hoặc không risk assessment, rồi đánh giá và quản lý theo kết quả; không chuyển khuyến cáo US thành chính sách Việt Nam.
5. Điều trị: nền tảng, phân tầng low/high/very-high, antiresorptive, parenteral, anabolic/dual-action và sequence; tránh protocol chưa khóa.
6. Theo dõi/an toàn: adherence, reassessment, AFF/ONJ, hypocalcemia, denosumab.
7. Flowchart có red flag, fracture hiện hữu, DXA có/không, secondary cause và referral.
8. Bốn case đúng năm bước; tips, summary, evidence và references.

## 7. Hướng dẫn execute

- Chỉ dùng claims trên; chỉ dùng số cụ thể khi đã full verified, ưu tiên không dùng số cụ thể.
- Dùng tiếng Việt có dấu; giải thích thuật ngữ lần đầu.
- Đặt BOX ĐỎ trước thuật toán thường quy. Flowchart có nhánh cấp cứu và thiếu nguồn lực.
- Mọi PMID của reference phải giữ tag hợp lệ. Markdown là source of truth; cards/APKG sau lesson source gate.
- Case screening chỉ dùng scope/đường đi đã khóa từ USPSTF 2025; không suy diễn interval, treatment threshold hoặc khuyến cáo population screening cho nam.
