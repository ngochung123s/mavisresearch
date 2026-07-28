# RESEARCH BRIEF: IM-44 — Nguyên lý ECG và nguyên lý hiển thị hình ảnh sóng ECG
**Ngày:** 2026-07-28 | **Profile:** foundation | **Đối tượng:** người học mất nền

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "required_gates": [
    "brief_pmid_preflight",
    "brief_claims_strict",
    "source_pmid_strict",
    "source_claims_strict",
    "source_retraction",
    "guideline_evidence",
    "citation_zero_block",
    "profile_foundation",
    "cards_schema",
    "candidate_apkg_build",
    "package_note_count",
    "package_diacritics",
    "source_diacritics",
    "docx_build",
    "learner_smoke"
  ],
  "not_applicable": [],
  "approved_exemptions": []
}
```

- **Output basename đã khóa:** `IM-44_Nguyen_ly_ECG_2026-07-28_RELEASE_v1`.

## 1. Phạm vi và preflight guideline

- **Chủ đề và đối tượng học:** Nguyên lý điện sinh lý cơ tim, nguyên tắc hình chiếu vector và các chuẩn hóa kỹ thuật cơ bản của máy ECG. Dành cho người học mất gốc cần hiểu bản chất trước khi đọc bệnh lý.
- **Guideline chính thức đã kiểm freshness:** AHA/ACC/HRS Recommendations for the Standardization and Interpretation of the Electrocardiogram (Part I: The Electrocardiogram and Its Technology, 2007). Dù cũ nhưng đây là guideline nền tảng về kỹ thuật chưa bị thay thế.
- **Phạm vi được phép:** Điện thế hoạt động, hệ thống dẫn truyền, nguyên tắc vector, tam giác Einthoven, hệ thống trục 6 chiều, các thông số chuẩn hóa giấy và filter.
- **Ngoài phạm vi:** Phân tích hình thái sóng bệnh lý (nhồi máu, phì đại, rối loạn nhịp) — sẽ nằm ở các bài riêng.

## 2. Papers đã chọn

- **PMID:** `17349896`
  - Loại nguồn: AHA/ACC/HRS Scientific Statement (Guideline)
  - Vai trò: Cung cấp các tiêu chuẩn kỹ thuật (filter, calibration, tốc độ giấy).
  - Lý do chọn: Đây là tài liệu chuẩn hóa gốc của Hoa Kỳ về công nghệ ECG.

## 3. Claims đã verify

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Tần số cắt lọc (filter) chuẩn cho ECG chẩn đoán người lớn là 0.05 Hz đến 150 Hz | 17349896 | [GUIDELINE VERIFIED] | "For adults, the recommended low-frequency cutoff is 0.05 Hz... high-frequency cutoff is 150 Hz" | Người lớn | — | — | — |
| C-002 | Vận tốc giấy chuẩn là 25 mm/s | 17349896 | [GUIDELINE VERIFIED] | "A recording speed of 25 mm/s is the standard" | — | — | — | — |
| C-003 | Test amplitude (calibration) chuẩn là 10 mm/mV | 17349896 | [GUIDELINE VERIFIED] | "standard calibration of 10 mm/mV" | — | — | — | — |

## 4. Claims và số liệu cấm dùng

- Không đưa các tiêu chuẩn chẩn đoán bệnh lý (ví dụ: ST chênh lên bao nhiêu mm) vào bài này.
- Không tự suy diễn các tần số filter khác ngoài 0.05-150 Hz cho ECG chuẩn 12 chuyển đạo.

## 5. Dàn ý chi tiết

### 0. Nền tảng tối thiểu cần dùng ngay

- Kiến thức consensus cần giải thích: Khái niệm về điện thế màng tế bào lúc nghỉ (âm bên trong, dương bên ngoài) và sự khử cực (dòng ion dương tràn vào).
- Claim IDs: —

### 1. Tổng quan và định nghĩa

- Điện tâm đồ (ECG) là gì: Là bản ghi lại các thay đổi điện thế của tim theo thời gian từ các điện cực đặt trên bề mặt cơ thể.
- Claim IDs: —

### 2. Cơ chế (Điện sinh lý cơ bản)

- Tầng 1 (Phân tử): Dòng ion Na+, Ca2+ đi vào tạo khử cực; K+ đi ra tạo tái cực.
- Tầng 2 (Tế bào/Mô): Sự lan truyền sóng khử cực từ tế bào này sang tế bào khác tạo thành một lưỡng cực điện (dipole).
- Tầng 3 (Tổng hợp): Tổng hợp các dipole tại một thời điểm tạo thành Vector điện học trung bình của tim.
- Claim IDs: —

### 3. Nguyên lý hình chiếu Vector (CỐT LÕI)

- Máy ECG như một vôn kế (voltmeter).
- Quy tắc 1: Vector hướng về điện cực dương → sóng dương.
- Quy tắc 2: Vector hướng ra xa điện cực dương → sóng âm.
- Quy tắc 3: Vector vuông góc với trục chuyển đạo → sóng 2 pha (hoặc triệt tiêu).
- Claim IDs: —

### 4. Hệ thống chuyển đạo (Leads)

- Tam giác Einthoven (DI, DII, DIII).
- Các chuyển đạo chi tăng cường (aVR, aVL, aVF).
- Hệ thống trục tọa độ 6 chiều (Hexaxial reference system).
- Các chuyển đạo trước tim (V1-V6) nhìn tim trên mặt phẳng ngang.
- Claim IDs: —

### 5. Chuẩn hóa kỹ thuật và giấy ECG

- Ý nghĩa các ô vuông: 1 ô nhỏ = 0.04s (ngang) và 0.1mV (dọc).
- Chuẩn hóa vận tốc giấy và biên độ. {claim:C-002}, {claim:C-003}
- Tần số cắt lọc (Filter) để tránh méo sóng. {claim:C-001}

### 6. Flowchart ASCII và BOX ĐỎ

- Nhánh thường quy: Đọc ECG luôn bắt đầu bằng việc kiểm tra test calibration và tốc độ giấy.
- BOX ĐỎ:
  - Mắc lộn điện cực (Lead reversal) làm đảo ngược hình chiếu vector.
  - Cài đặt filter sai (ví dụ cắt tần số thấp ở 0.5 Hz thay vì 0.05 Hz) có thể làm đoạn ST bị méo, gây chẩn đoán nhầm nhồi máu.

### 7. Case và lời giải

- Case 1: Một bản ghi ECG có sóng P và phức bộ QRS âm hoàn toàn ở DI. Giải thích nguyên nhân phổ biến nhất dựa trên nguyên lý vector (mắc lộn điện cực tay phải - tay trái).

### 8. Tổng kết và tài liệu tham khảo

- Tóm tắt các quy tắc vector và thông số chuẩn hóa.

## 6. Hướng dẫn model execute

1. Chỉ dùng claims trong bảng và giữ `{claim:C-xxx}` gần claim tương ứng trong bản nháp để verifier truy vết.
2. Không thêm claim, PMID, guideline hoặc con số ngoài brief.
3. Chỉ dùng năm nhãn verification chuẩn.
4. Kiến thức consensus không cần nhãn; claim định lượng phải có evidence.
5. Viết tiếng Việt có dấu; tiếng Việt trước, English trong ngoặc lần đầu.
6. Flowchart dùng `text` ASCII/danh sách phân cấp, không dùng Mermaid.
7. Nếu một claim không đủ bằng chứng, bỏ claim thay vì suy diễn.
8. Output gồm Markdown + cards V2; DOCX, APKG và learner smoke do release runner tạo trong `outputs/`.