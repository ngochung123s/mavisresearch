# RESEARCH BRIEF — IM-04 PART 3: SINH HÓA VÀ TÍCH HỢP LÂM SÀNG

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "mode": "L3_BEGINNER",
  "required_gates": [
    "brief_pmid_preflight",
    "brief_claims_strict",
    "source_pmid_strict",
    "source_claims_strict",
    "source_retraction",
    "guideline_evidence",
    "depth_foundation",
    "guideline_evidence_crosscheck",
    "citation_zero_block",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "docx_build",
    "learner_smoke"
  ],
  "lesson_depth_contract": {
    "min_total_words": 5000,
    "min_total_lines": 500,
    "min_sections": 10,
    "min_subsections": 12,
    "min_mechanism_chains": 3,
    "min_examples": 6,
    "min_misconceptions": 6,
    "min_checkpoints": 4,
    "min_cases_with_solutions": 2,
    "min_practical_tips": 10,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [],
  "approved_exemptions": []
}
```

- **Output basename đã khóa:** `IM-04_Part3_Sinh_hoa_va_tich_hop_2026-07-29_RELEASE_v1`
- **Evidence bundle source lock duy nhất:** `outputs/evidence/part3/evidence_bundle.json`; content hash `1beb869140734f5767fb79d76e269ec1b00415125f8c19410a436d2b116cc3ee`; file SHA-256 `f60ccfe38a5f5fed8b2332231d59b31d2df3ea963c9ebbd8d34ea2ed1cb70e9e`.
- **Freshness và hash:** bundle tạo 2026-07-29T10:31:11Z, validation PASS; metadata/abstract và integrity nằm trong TTL; prepared artifact hashes đã đối chiếu lại ngày 2026-07-29.
- **Chuyên khoa:** Nội khoa người lớn; bài nền tảng tích hợp, không thay thế cấp cứu, hội chẩn chuyên khoa hoặc các bài IM-41/43/45/46/47/51/52.

## 1. Phạm vi và preflight guideline

- **Chủ đề:** đọc sinh hóa máu cơ bản theo cụm điện giải, thận, gan, đường huyết, viêm, tim, tuyến giáp và ferritin; tích hợp với CBC/đông máu bằng bốn ca an toàn.
- **Guideline chính thức khóa cho gate:** British Society of Gastroenterology 2018, *Guidelines on the management of abnormal liver blood tests*. Prepared bundle xác nhận exact identity, Practice Guideline, authority, `current_version=true`, full text CC BY và integrity sạch.
- **Nguồn current trong prepared bundle dùng làm nền biên tập:** Austrian Society for Nephrology 2024 về hạ natri; UK Kidney Association 2023 về tăng kali và tăng kali giả; BSG 2018 về xét nghiệm gan. Claim khóa BSG trực tiếp dạy cách đọc kết quả gan theo kết quả cũ, bệnh sử và tình trạng hiện tại.
- **KDIGO 2012:** bundle ghi `current_version=false`; dự thảo 2026 chưa phải guideline xuất bản. Không dùng KDIGO 2012 hoặc dự thảo 2026 để gắn `[GUIDELINE VERIFIED]`, không dùng tiêu chuẩn/khuyến cáo định lượng từ hai tài liệu này.
- **Ngoài phạm vi:** thuật toán chuyên sâu và phác đồ điều trị rối loạn Na/K, AKI/AKD/CKD, toan kiềm, bệnh gan, đái tháo đường, DKA/HHS; ngưỡng ADA; troponin delta hoặc protocol theo giờ; ngưỡng CRP/ESR/TSH/ferritin.

## 2. Paper/source set đã khóa

- **Source record:** `29122851`
  - **Expected title:** Guidelines on the management of abnormal liver blood tests
  - **Loại nguồn:** BSG clinical practice guideline, 2018; current official source trong prepared bundle, full text CC BY.
  - **Vai trò:** khóa khuyến nghị thực chất rằng kết quả xét nghiệm gan bất thường chỉ nên được diễn giải sau khi xem kết quả trước, bệnh sử và tình trạng bệnh hiện tại.
  - **Lý do chọn:** trực tiếp thuộc scope sinh hóa gan, exact quote hợp pháp trong local XML, hash/provenance/freshness và authority đã khóa.

### Nguồn bị giới hạn hoặc loại khỏi source lock

- KDIGO AKI 2012: `current_version=false`, pending 2026 public-review draft; không gán current guideline label.
- KDIGO 2026 draft: dự thảo, không phải final guideline.
- ADA 2026: không có reusable exact quote cho ngưỡng/interference; chỉ diễn giải glucose/HbA1c định tính.
- Troponin: ESC licensing gap và thiếu reusable exact recommendation; chỉ viết qualitative không nhãn/số.
- CRP/ESR: không có general official source đủ khóa; chỉ trình bày định tính.
- TSH và ferritin: chỉ metadata/partial source; không dùng threshold, cutoff hoặc con số.
- Không dùng tỷ lệ BUN/creatinine, AST/ALT ratio hoặc bất kỳ ngưỡng báo động phổ quát nào.

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-301 | Abnormal liver blood test results should only be interpreted after review of the previous results, past medical history and current medical condition. | 29122851 | [GUIDELINE VERIFIED] | Abnormal liver blood test results should only be interpreted after review of the previous results, past medical history and current medical condition. | Người có kết quả xét nghiệm gan bất thường | Đọc sau khi xem kết quả trước, bệnh sử và tình trạng hiện tại so với đọc số đơn độc | Diễn giải xét nghiệm gan theo baseline và bối cảnh lâm sàng | Tại lần đánh giá kết quả bất thường |

## 4. Claims và số liệu cấm dùng

- Không dùng ADA diagnostic thresholds, HbA1c cutoff hoặc định lượng yếu tố nhiễu.
- Không dùng troponin delta, ngưỡng percentile cụ thể, thuật toán theo giờ; troponin chỉ diễn giải định tính cùng triệu chứng, ECG, thời gian và động học theo labo.
- Không dùng ngưỡng hoặc con số CRP/ESR, TSH, ferritin; không gắn nhãn cho các đoạn này.
- Không dùng tiêu chuẩn AKI định lượng từ KDIGO 2012 và không gọi bản 2012 là guideline hiện hành.
- Không dùng ngưỡng Na/K điều trị hoặc tốc độ hiệu chỉnh; BOX ĐỎ chỉ yêu cầu nhận diện triệu chứng, ECG, xác minh mẫu và kích hoạt quy trình cấp cứu địa phương.
- Không dùng tỷ lệ BUN/creatinine, tỷ lệ AST/ALT, ngưỡng ALT, liều thuốc, chỉ định truyền máu hoặc chế phẩm đông máu.
- Bốn ca tích hợp chỉ dùng claim C-301 khi cần nguyên tắc đọc xét nghiệm gan theo baseline/bệnh sử/tình trạng hiện tại; các dữ kiện khác là bài tập pattern và không được biến thành threshold điều trị.

## 5. Dàn ý chi tiết

### 0. Nền tảng tối thiểu cần dùng ngay
- Phân biệt nồng độ, chức năng, dấu ấn tổn thương và giá trị ước tính; kiểm mẫu, đơn vị, khoảng tham chiếu labo, baseline, dynamics và clinical fit.

### 1. Tổng quan và định nghĩa
- Sinh hóa là ảnh chụp động của nước, điện giải, chuyển hóa và tín hiệu tổn thương; ô đỏ không tự là chẩn đoán.

### 2. Cơ chế
- Ba chuỗi 5 tầng: nước–natri–não; kali–điện thế màng–tim; tưới máu/khối cơ–creatinine–ước tính chức năng.

### 3. Chẩn đoán điện giải
- Na/K/Cl theo triệu chứng, ECG, chất lượng mẫu và xu hướng; định tính, không dạy phác đồ/ngưỡng.

### 4. Chẩn đoán thận
- Creatinine, BUN, eGFR như các mảnh ghép phụ thuộc baseline, khối cơ, dịch, sản xuất và trạng thái ổn định; tránh KDIGO claim hiện hành.

### 5. Chẩn đoán gan và protein
- AST/ALT, bilirubin, albumin theo pattern và bối cảnh; không dùng tỷ lệ hoặc cutoff chưa khóa.

### 6. Chẩn đoán glucose, viêm, tim, nội tiết và vi chất
- Glucose/HbA1c, CRP/ESR, troponin, TSH, ferritin đều định tính; nhấn mạnh giới hạn và động học/bối cảnh. Claim C-301 chỉ áp dụng trực tiếp cho đọc xét nghiệm gan.

### 7. Theo dõi và an toàn
- BOX ĐỎ, flowchart ASCII và Plan B khi thiếu ECG, baseline, xét nghiệm lặp hoặc tư vấn labo.

### 8. Bốn case tích hợp có lời giải
- Ca 1: chảy máu tiêu hóa/xơ gan, tránh tỷ lệ BUN/Cr và ngưỡng truyền máu.
- Ca 2: nhiễm trùng và chức năng thận/điện giải, tránh tiêu chuẩn KDIGO định lượng.
- Ca 3: tăng kali giả do mẫu vỡ hồng cầu so với bệnh lý thật, tránh điều trị số giả.
- Ca 4: đau ngực, troponin định tính theo động học labo/ECG/lâm sàng; không gắn claim hoặc nhãn troponin.

### 9. Tóm tắt, tips và tài liệu tham khảo
- Khung đọc tuần tự, mười tips thực hành, một exact locked guideline occurrence.

## 6. Hướng dẫn model execute

1. Viết tiếng Việt có dấu, mode `L3_BEGINNER`, tối thiểu 5.000 từ và 500 dòng không trống.
2. Chỉ dùng claim C-301 ở đúng một occurrence thuộc phần xét nghiệm gan, có source record đã khóa, nhãn `[GUIDELINE VERIFIED]` và `{claim:C-301}` trên cùng dòng.
3. Không thêm PMID khác; lesson PMID set phải đúng bằng brief source set.
4. ADA/troponin/CRP-ESR/TSH/ferritin phải định tính, không nhãn, không cutoff, không con số.
5. Không gọi KDIGO 2012 current; không gán verification cho KDIGO; chỉ nói trạng thái pending update nếu cần giải thích việc loại nguồn.
6. Có ít nhất mười section, mười hai subsection, ba chuỗi cơ chế, sáu ví dụ, sáu bẫy, bốn checkpoint, bốn case có lời giải 5 bước và mười tips.
7. Có BOX ĐỎ, flowchart ASCII, nhánh cấp cứu, Plan B và depth markers rõ; không padding hoặc placeholder.
8. Dữ kiện số trong case chỉ là kết quả giả định để so baseline/pattern; tuyệt đối không diễn giải thành universal threshold hay protocol.
