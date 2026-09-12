# RESEARCH BRIEF: Thuốc lợi tiểu — Release v2
****Mã bài học:** IM-43b | Ngày khóa research:** 2026-07-22 | **Revision:** RELEASE v2 | **Model research:** Terra | **Model execute:** Terra

---

## 0. Lesson profile & release contract

Contract này được khóa **trước preflight và review/tái tạo artifact RELEASE v2**. Nó không hồi tố candidate ngày 2026-07-22.

```json
{
  "profile": "pharmacology",
  "required_gates": [
    "brief_pmid_preflight",
    "source_pmid_strict",
    "source_claims_strict",
    "citation_zero_block",
    "profile_pharmacology",
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

## 1. Source selection mới cho revision

| PMID | Vai trò cho RELEASE v2 | Giới hạn dùng |
|---|---|---|
| PMID: 30936153 | Đích nephron, kháng lợi tiểu, NSAID, nguy cơ điện giải và nguyên tắc cá thể hóa. | Không suy ra liều/interval phổ quát. |
| PMID: 39124738 | Sung huyết trong suy tim và vai trò định hướng của lợi tiểu quai. | Thuật toán suy tim vẫn thuộc IM-22. |
| PMID: 38490803 | Khung đánh giá CKD, medication stewardship và nguy cơ điện giải. | Không tạo protocol lợi tiểu CKD. |
| PMID: 33942342 | Bối cảnh cổ trướng/xơ gan để liên kết IM-40. | Không sao chép tỷ lệ phối hợp hoặc liều. |

**Đã loại:** Không dùng liều khởi đầu/tối đa, khoảng điều chỉnh, ngưỡng eGFR cứng, tỷ lệ phối hợp, tần suất xét nghiệm hoặc protocol truyền dịch không được xác minh trong revision. Không sao chép thuật toán IM-20/IM-22/IM-40/IM-44.

## 2. Claims được phép sau preflight

- Lợi tiểu được phân nhóm theo đoạn nephron và cơ chế bị ức chế; quai tác động NKCC2 ở TAL, thiazide/thiazide-like tác động NCC ở DCT. [ABSTRACT VERIFIED]
- Amiloride/triamterene chẹn ENaC; spironolactone/eplerenone đối kháng thụ thể mineralocorticoid ở đoạn xa/ống góp. [ABSTRACT VERIFIED]
- Các nhóm có hướng nguy cơ điện giải/thể tích khác nhau; NSAID có thể làm giảm đáp ứng lợi tiểu và tăng nguy cơ tổn thương thận trong bối cảnh dễ tổn thương. [ABSTRACT VERIFIED]
- Khi không đáp ứng, rà tuân thủ, natri ăn, NSAID, tưới máu, CKD/hấp thu và tái hấp thu bù trước; sequential blockade chỉ khi có chỉ định và monitor. [ABSTRACT VERIFIED]
- Sung huyết/giữ dịch là vấn đề trung tâm của suy tim mất bù; lợi tiểu quai có vai trò giảm sung huyết nhưng dùng theo theo dõi/bệnh cảnh. [ABSTRACT VERIFIED]
- Giảm oxy, phù phổi, sốc/giảm tưới máu, vô niệu, lú lẫn, rối loạn điện giải có triệu chứng hoặc suy thận xấu nhanh là nhánh đánh giá cấp cứu/chuyển tuyến. [GUIDELINE VERIFIED]

### Số liệu CẤM dùng
- Không thêm liều, route, tốc độ tăng liều, mốc xét nghiệm, ngưỡng điện giải hay chỉ định điều trị phổ quát.
- Không trình bày lợi tiểu như y lệnh ngoại trú; phải nêu đánh giá phù hợp, theo dõi, mốc dừng/escalate và Plan B.

## 3. Execute contract

1. Candidate `Thuoc_loi_tieu_2026-07-22.md` chỉ là input để review theo source set này; artifact release phải mang tên `RELEASE_v2`.
2. Dạy pharmacology tái sử dụng: liên kết bài Sinh lý Nephron, bản đồ nhóm–đoạn, kê đơn an toàn, kháng lợi tiểu, adverse effects, flowchart, cases, tips và tổng kết.
3. Tái tạo 80 cards `basic` từ lesson release; các card tình huống phải kiểm mục tiêu, monitoring và red-flag escalation.
4. Trước promotion, tất cả gate trong contract phải có một kết quả `PASS` duy nhất.

## 4. Đối chiếu kiểm tra theo plan gốc

- Ngày 2026-07-22, ba lệnh `preflight_guideline_check.py` cho topic `diuretics` với KDIGO 2024, ESC 2024 và AASLD 2021 đều trả `WARN`/exit 1 vì registry không có topic này. Đây là thiếu coverage của registry, không phải guideline bị stale; các nguồn trực tiếp đã khóa ở Mục 1, nên registry không bị sửa ngoài scope.
- `depth_check.py` của bài RELEASE v2 trả `FAIL` vì rubric chung cho disease lesson đòi định nghĩa/chẩn đoán/điều trị, ít nhất 10 PMID, 6 bảng và 8 tips ở Section 7. Bài này là pharmacology profile, không chứa các gate đó trong contract khóa ở Mục 0; kết quả không được diễn giải là PASS hoặc exemption.
- Các gate thực sự bắt buộc của profile `pharmacology` đã được chạy lại sau khi checker PMID fail-closed thay đổi: strict brief preflight `4 OK / 0 WARN / 0 BLOCK`, `EXIT:0`; `publish_gate.py` xác nhận `PUBLISH READY` với 11/11 required gates.