# RESEARCH BRIEF — IM-04 PART 2: HUYẾT HỌC VÀ ĐÔNG MÁU CƠ BẢN

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

- **Output basename đã khóa:** `IM-04_Part2_Huyet_hoc_va_dong_mau_2026-07-29_RELEASE_v1`
- **Evidence bundle source lock duy nhất:** `outputs/evidence/part2/evidence_bundle.json`; content hash `626dff6bab4befacb1e798a0d2d465228d17bd224b4ec1c71d504984b16a58e4`.
- **Chuyên khoa:** Nội khoa người lớn; bài nền tảng, không thay thế hội chẩn Huyết học hoặc Y học truyền máu.

## 1. Phạm vi và preflight guideline

- **Chủ đề:** cách đọc công thức máu toàn bộ (CBC/FBC) theo ba dòng tế bào và bộ xét nghiệm đông máu cơ bản PT/INR, aPTT, fibrinogen.
- **Guideline chính thức khóa:** WHO 2024, *Guideline on haemoglobin cutoffs to define anaemia in individuals and populations*; local PDF hợp pháp từ WHO IRIS, CC BY-NC-SA 3.0 IGO, SHA-256 đã khóa trong bundle.
- **Nguồn định hướng không cấp nhãn:** BSH 2022 FBC và clotting-screen slides là educational presentations, tuyệt đối không gọi là formal guideline.
- **Nguồn formal bổ trợ đã có trong bundle:** EHA/EuNet-INNOCHRON 2023, Croatian PTCP 2024, Croatian coagulation preanalytics 2019, ICSH fibrinogen 2024, CHEST 2025, AABB 2023/2025. Chúng chỉ làm nền biên tập; source set PMID của release này cố ý khóa ở đúng một claim WHO để mọi occurrence có thể crosscheck đầy đủ.
- **Ngoài phạm vi:** chẩn đoán và điều trị bệnh huyết học chuyên sâu; phác đồ DIC; chỉnh liều thuốc chống đông; chỉ định chế phẩm máu theo từng thủ thuật; hóa sinh Part 3.

## 2. Paper/source set đã khóa

- **PMID:** `38530913`
  - **Expected title:** Guideline on haemoglobin cutoffs to define anaemia in individuals and populations
  - **Loại nguồn:** WHO clinical practice guideline, 2024.
  - **Vai trò:** khóa một claim chính thức về chuẩn đo haemoglobin; tạo nền an toàn trước khi diễn giải Hb/Hct và các chỉ số hồng cầu.
  - **Lý do chọn:** current, official, local exact copy, legal reuse, hash/provenance/freshness đầy đủ trong bundle `626dff6b…`.

### Nguồn bị giới hạn hoặc loại khỏi source lock

- BSH FBC/clotting 2022: educational, không dùng `[GUIDELINE VERIFIED]`.
- Correction notice liên quan đồng thuận neutropenia: cần adjudication; không dùng trong release và không đưa định danh vào source set khóa.
- AABB 2023/2025 metadata-only: không dùng làm full-text claim trong release này.
- Không dùng ngưỡng fibrinogen thay thế phổ quát; không dùng một con số truyền máu cho mọi quần thể.

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-201 | Trong khuyến nghị về đo haemoglobin (haemoglobin measurement), WHO khuyến nghị dùng máu tĩnh mạch (venous blood), máy phân tích huyết học tự động (automated haematology analysers) và các biện pháp kiểm soát chất lượng cao (high-quality control measures) để đánh giá nồng độ haemoglobin ở cá thể và quần thể. | 38530913 | [GUIDELINE VERIFIED] | Use of venous blood, automated haematology analysers and high-quality control measures are recommended for the assessment of haemoglobin concentration in individuals and populations. | Cá thể và quần thể được đánh giá nồng độ haemoglobin | Máu tĩnh mạch, máy phân tích huyết học tự động và kiểm soát chất lượng cao so với các nguồn máu, thiết bị hoặc quy trình không đáp ứng đồng thời các điều kiện này | Đánh giá nồng độ haemoglobin | Tại thời điểm đo haemoglobin |
## 4. Claims và số liệu cấm dùng

- Không áp một khoảng tham chiếu CBC chung cho mọi labo, tuổi, giới, thai kỳ hoặc độ cao.
- Không gọi Hb thấp đồng nghĩa thiếu sắt; không gọi MCV thấp đồng nghĩa duy nhất thiếu sắt.
- Không chẩn đoán giảm tiểu cầu thật trước khi xem cờ máy, phết máu và khả năng kết cụm EDTA.
- Không xem PT/aPTT bình thường là loại trừ mọi rối loạn chảy máu.
- Không bù fibrinogen hoặc truyền RBC/platelet chỉ từ một con số không có bối cảnh.
- Không dùng BSH slides như guideline; không tự gán nhãn cho nội dung educational.

## 5. Dàn ý chi tiết

### 0. Nền tảng tối thiểu cần dùng ngay
- Phiếu CBC là các phép đo liên quan nhưng không đồng nghĩa; luôn kiểm đơn vị, khoảng tham chiếu, cờ máy và chất lượng mẫu.

### 1. Tổng quan và định nghĩa
- CBC theo ba dòng; haemostasis và ý nghĩa giới hạn của PT/INR/aPTT/fibrinogen.

### 2. Cơ chế
- Ba chuỗi: tạo hồng cầu–kích thước–Hb; nhiễm trùng–đáp ứng bạch cầu; cầm máu–fibrin.

### 3. Chẩn đoán hồng cầu
- Hb/Hct/RBC, MCV/MCH/MCHC/RDW, reticulocyte; đọc pattern thay vì một ô.

### 4. Chẩn đoán bạch cầu
- Tổng WBC, differential tuyệt đối, ANC/ALC, left shift; mức khẩn cấp phụ thuộc lâm sàng.

### 5. Chẩn đoán tiểu cầu
- Số lượng, MPV/cờ máy, pseudothrombocytopenia; chảy máu và thủ thuật là bối cảnh bắt buộc.

### 6. Đông máu cơ bản
- PT/INR, aPTT, fibrinogen Clauss; mẫu citrate và pattern kéo dài.

### 7. Theo dõi và an toàn
- Baseline, xu hướng, thuốc, truyền dịch/truyền máu, gọi labo; BOX ĐỎ và Plan B.

### 8. Case có lời giải
- Case 1: Hb giảm, MCV thấp, RDW tăng nhưng chưa kết luận nguyên nhân.
- Case 2: platelet giảm đột ngột kèm cờ platelet clumps.

### 9. Tổng kết, tips và tài liệu tham khảo
- Khung đọc tuần tự, mười tips thực hành, một exact guideline claim occurrence.

## 6. Hướng dẫn model execute

1. Viết tiếng Việt có dấu, mode `L3_BEGINNER`, tối thiểu 5.000 từ và 500 dòng không trống.
2. Chỉ dùng claim C-201 ở đúng một occurrence có `PMID: 38530913`, `[GUIDELINE VERIFIED]` và `{claim:C-201}` trên cùng dòng.
3. Không thêm PMID khác; lesson PMID set phải đúng bằng brief source set.
4. Kiến thức nền không nhãn; tránh mọi ngưỡng truyền máu hoặc fibrinogen phổ quát.
5. Có ít nhất mười section, mười hai subsection, ba chuỗi cơ chế, sáu ví dụ, sáu bẫy, bốn checkpoint, hai case có lời giải và mười tips.
6. Có BOX ĐỎ, flowchart ASCII, nhánh cấp cứu, Plan B; không padding, placeholder hoặc lấn Part 3.
