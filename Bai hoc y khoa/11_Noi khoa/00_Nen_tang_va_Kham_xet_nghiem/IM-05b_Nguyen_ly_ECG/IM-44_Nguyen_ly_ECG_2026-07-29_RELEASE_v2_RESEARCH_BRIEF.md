# RESEARCH_BRIEF.md — IM-44_Nguyen_ly_ECG_2026-07-29_RELEASE_v2

> File Research Brief cho bài học IM-44 Nguyên lý ECG và nguyên lý hiển thị hình ảnh sóng ECG (Phiên bản RELEASE_v2).

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

- Output basename: `IM-44_Nguyen_ly_ECG_2026-07-29_RELEASE_v2`
- Profile: `foundation` (Nền tảng sinh lý học & điện học y khoa)
- Chế độ duy nhất: `L3_BEGINNER` (Cầm tay chỉ việc cho người mất gốc)

---

## 1. Phạm vi và preflight guideline

- **Chủ đề**: Nguyên lý điện học cơ bản của tim, cơ chế hình thành vector sóng điện thế, hệ thống chuyển đạo tam giác Einthoven và hệ 6 trục mặt phẳng trán, chuyển đạo trước tim mặt phẳng ngang, cùng nguyên lý kỹ thuật thu nhận, lọc nhiễu, số hóa, hiển thị giấy ECG và nhận diện lỗi mắc dây / nhiễu giả ảnh.
- **Đối tượng học**: Học viên mất gốc điện tim, bác sĩ lâm sàng cần nắm bản chất vật lý và sinh lý của sóng ECG từ gốc.
- **Guideline & Tiêu chuẩn kỹ thuật chính**:
  - Khuyến cáo AHA/ACC về dải tần số lọc (Bandwidth recommendations: 0.05 Hz – 150 Hz cho ECG 12 chuyển đạo tiêu chuẩn ở người lớn).
  - Tiêu chuẩn tốc độ giấy chuẩn 25 mm/s và biên độ chuẩn 10 mm/mV.
- **Phạm vi được phép**: Điện thế màng, cơ chế kênh ion ($Na^+$, $K^+$, $Ca^{2+}$), phân cực/khử cực/tái cực, vector điện thế tim, 12 chuyển đạo tiêu chuẩn, nguyên lý mạch khuếch đại/lọc nhiễu (low-pass, high-pass, notch filter), tốc độ/biên độ giấy, nhận diện nhiễu và mắc nhầm điện cực.
- **Ngoài phạm vi**: Tiêu chí chẩn đoán chuyên sâu các bệnh lý loạn nhịp phức tạp (VT/VF, nhĩ thất phân liệt), tiêu chí chi tiết của tất cả các loại hội chứng gen hiếm gặp (Brugada, Long QT) nằm ngoài phạm vi bài nguyên lý cơ bản.

---

## 2. Papers đã chọn

- **PMID: 27498055**
  - *Loại nguồn*: Prospective Observational Study (Journal of Electrocardiology, Q2).
  - *Vai trò*: Bằng chứng thực nghiệm về ảnh hưởng của bộ lọc tần số cao (40 Hz vs 150 Hz) đến chất lượng bản ghi ECG và sự xuất hiện giả ảnh / sai lệch biên độ.
  - *Lý do chọn*: Cung cấp số liệu định lượng chính xác về tỷ lệ bản ghi đạt chất lượng tối ưu và thay đổi biên độ sóng QRS/J-point khi thay đổi bộ lọc.
- **PMID: 17317378**
  - *Loại nguồn*: Observational Clinical Audit (The American Journal of Cardiology, Q2).
  - *Vai trò*: Bằng chứng về thực trạng cài đặt bộ lọc ECG trên lâm sàng.
  - *Lý do chọn*: Cung cấp tỷ lệ phần trăm thực tế các bản ghi ECG vi phạm dải tần chuẩn AHA trong cộng đồng lâm sàng.
- **PMID: 41103868**
  - *Loại nguồn*: Clinical Observational Study (Cureus, Q3).
  - *Vai trò*: Dịch tễ học và tỷ lệ mắc lỗi dây điện cực (lead reversal) tại bệnh viện tuyến trung ương.
  - *Lý do chọn*: Cung cấp số liệu tần suất mắc sai dây điện cực chi chi tiết (LA-LL vs RA-LA vs chuyển đạo trước tim).
- **PMID: 25213624**
  - *Loại nguồn*: Validation Study (Journal of Electrocardiology, Q2).
  - *Vai trò*: Thuật toán cảnh báo sớm tự động phát hiện đảo cực dây ECG.
  - *Lý do chọn*: Cung cấp chỉ số độ nhạy, độ đặc hiệu của việc phát hiện đảo dây bằng trục QRS và biên độ sóng P.
- **PMID: 11320465**
  - *Loại nguồn*: Methodological Clinical Study (Journal of Electrocardiology, Q2).
  - *Vai trò*: Thuật toán 3 bước dựa trên hướng sóng P và cực aVR để phân biệt các loại đảo dây chi.
  - *Lý do chọn*: Nguyên lý vector sóng P sinh lý trong phân biệt 5 kiểu đảo dây chi.
- **PMID: 22929906**
  - *Loại nguồn*: Clinical Review (The Journal of Emergency Medicine, Q2).
  - *Vai trò*: Nhận diện hình thái giả nhồi máu tim và thay đổi ST-T do mắc sai vị trí điện cực trước tim.
  - *Lý do chọn*: Phân tích cơ chế mất đà phát triển sóng R từ V1 đến V6 khi đặt sai liên sườn.

---

## 3. Claims đã verify

Registry máy đọc được cho bài học RELEASE_v2:

| Claim ID | Claim | PMID | Verification | Quote từ nguồn | Population | Intervention / comparator | Outcome | Timepoint |
|---|---|---|---|---|---|---|---|---|
| C-001 | Khuyến cáo tiêu chuẩn dải tần số lọc (bandwidth) cho bản ghi ECG 12 chuyển đạo tiêu chuẩn ở người lớn là 0.05 Hz đến 150 Hz. | 27498055 | [GUIDELINE VERIFIED] | established a standard 0.05 to 150Hz bandwidth for the routine recording of 12-lead electrocardiograms | Bệnh nhân người lớn đo ECG ngoại trú | Bộ lọc dải tần chuẩn 0.05–150 Hz | Tiêu chuẩn kỹ thuật băng thông ECG | Đánh giá trước phẫu thuật |
| C-002 | Tỷ lệ bản ghi ECG đạt chất lượng tối ưu ở dải 150 Hz là 54.6% so với 93.4% khi dùng bộ lọc khác. | 27498055 | [DATA VERIFIED] | quality ECGs compared to the 150Hz cutoff (93.4% vs 54.6%; p<0.001) and a lower | 1582 bệnh nhân người lớn chuẩn bị phẫu thuật | Bộ lọc tần số cao 40 Hz so với 150 Hz | Tỷ lệ bản ghi tối ưu và tỷ lệ bản ghi không đọc được | Lần đo ECG trước mổ |
| C-003 | Trong thực tế lâm sàng, chỉ có 25 phần trăm bản ghi ECG (65 trong số 256) tuân thủ đúng tiêu chuẩn bộ lọc khuyến cáo. | 17317378 | [DATA VERIFIED] | Only 25% of ECGs | 256 bản ghi ECG ngoại trú liên tiếp | Cài đặt bộ lọc thực tế so với tiêu chuẩn khuyến cáo AHA | Tỷ lệ tuân thủ dải tần số bộ lọc chuẩn | Khảo sát 3 tuần tại bệnh viện |
| C-004 | Khảo sát tại bệnh viện cho thấy tỷ lệ mắc nhầm dây điện cực là 1.5% (15/1.000 ECG), trong đó đảo dây chi chiếm 1.1%. | 41103868 | [DATA VERIFIED] | (1.5%). Eleven (1.1%) of these had limb lead reversal, of which eight were LA-LL | 1.000 bản ghi ECG liên tiếp tại bệnh viện | Quy trình mắc dây thực tế so với đối chiếu kiểm tra lại | Tỷ lệ và phân loại các kiểu mắc sai dây điện cực | Khảo sát 2 tháng |
| C-005 | Thuật toán cảnh báo tự động có thể phát hiện 7 kiểu đảo dây điện cực phổ biến nhất với độ đặc hiệu 99.8% per type và độ nhạy trung bình 90%. | 25213624 | [DATA VERIFIED] | of 99.8% per type and an average sensitivity of 90%, excluding LA-LL reversal | Cơ sở dữ liệu >18.000 bản ghi ECG bệnh viện | Thuật toán phân tích trục QRS và biên độ sóng P/QRS | Độ nhạy, độ đặc hiệu và tỷ lệ giảm lỗi mắc dây | Kiểm thử thuật toán tự động |
| C-006 | Năm kiểu mắc nhầm dây chi (không liên quan đến dây chân phải/đất) có thể được phân biệt dựa trên trục sóng P xoang mặt phẳng trán và vị trí của chuyển đạo aVR. | 11320465 | [ABSTRACT VERIFIED] | The 5 types of electrocardiograms of limb lead misplacement can be differentiated according to the P wave axis, the location of the lead aVR in the electrocardiogram | Bệnh nhân có hình thái ECG mắc sai dây chi | Thuật toán 3 bước phân tích sóng P và aVR | Chẩn đoán phân biệt 5 dạng mắc sai dây chi | Phân tích bản ghi ECG |
| C-007 | Việc đặt sai vị trí hoặc đảo ngược điện cực trước tim vi phạm quy luật phát triển biên độ sóng R/S từ V1 đến V6 và có thể tạo hình ảnh giả nhồi máu cơ tim hoặc thay đổi ST-T giả tạo. | 22929906 | [ABSTRACT VERIFIED] | Precordial electrode misplacement (improper positioning of the electrodes on the chest) is common and may mimic a pseudoinfarction pattern, or ST-segment/T-wave changes | Bệnh nhân đo ECG tại khoa cấp cứu | Đặt sai vị trí khoang liên sườn hoặc đảo dây trước tim | Hình thái giả bệnh lý nhồi máu và biến đổi ST-T | Đánh giá cấp cứu |

---

## 4. Claims và số liệu cấm dùng

- **CẤM** gán nhãn `[FULL VERIFIED]` hoặc `[TEXTBOOK]` hoặc `[Thông tin cơ bản - LLM verified]` (đã bị bãi bỏ theo quy chế mới).
- **CẤM** bịa đặt quote hoặc cắt ghép quote bằng dấu ba chấm (`...`).
- **CẤM** dùng các con số tỷ lệ phần trăm nhiễu hoặc tần số bộ lọc không có trong 7 claims đã verify ở trên.
- **CẤM** khẳng định bộ lọc 40 Hz không làm thay đổi biên độ ST trong mọi trường hợp nhồi máu cơ tim cấp (vì thực tế lọc 40 Hz có thể làm tù đỉnh QRS và làm sụt giảm nhẹ độ chênh ST).
- **CẤM** sử dụng bản guideline AHA 2007 trích dẫn giả mạo full-text paywalled mà không có nguồn local hợp lệ.

---

## 5. Dàn ý chi tiết cho bài học RELEASE_v2

### 0. TỔNG QUAN — VÌ SAO BÀI NÀY QUAN TRỌNG?
- Giới thiệu bài học theo phong cách L3_BEGINNER: Cầm tay chỉ việc cho người chưa biết gì về điện tim.
- Đặt vấn đề: ECG là công cụ ghi lại dòng điện của tim từ bề mặt da. Nếu không hiểu cơ chế lý hóa từ tế bào đến vector, người học sẽ chỉ thuộc lòng vẹt hình dạng dạng sóng và liên tục mắc bẫy khi gặp nhiễu, sai dây hoặc biến đổi tư thế tim.

### 1. NỀN TẢNG ĐIỆN HỌC & ĐIỆN THẾ MÀNG TẾ BÀO TIM [CỐT LÕI]
- **1.1. Điện thế nghỉ và nồng độ ion**: Sự chênh lệch nồng độ $Na^+$, $K^+$, $Ca^{2+}$ qua màng tế bào cơ tim. Bơm $Na^+/K^+$-ATPase duy trì điện thế nghỉ $-90\text{ mV}$ (tế bào cơ tâm thất).
- **1.2. Điện thế hoạt động (Action Potential)**: 5 pha (Pha 0 khử cực nhanh qua kênh $Na^+$ nhanh; Pha 1 tái cực sớm; Pha 2 cao nguyên qua kênh $Ca^{2+}$ L-type; Pha 3 tái cực nhanh qua kênh $K^+$; Pha 4 điện thế nghỉ).
- **1.3. Khử cực, tái cực và tính trơ**: Khái niệm trơ tuyệt đối và trơ tương đối.
- *Mechanism Chain 1*: Sự di chuyển ion qua màng $\rightarrow$ Biến đổi điện thế trong/ngoài tế bào $\rightarrow$ Dòng điện nội bào $\rightarrow$ Điện thế bề mặt da.

### 2. TỪ TẾ BÀO ĐẾN VECTOR ĐIỆN HỌC TIM [CỐT LÕI]
- **2.1. Lưỡng cực điện (Dipole) và Vector tổng**: Một tế bào đang khử cực tạo ra cực dương phía trước và cực âm phía sau. Tổng hợp hàng triệu tế bào tạo nên Vector điện thế tim.
- **2.2. Quy tắc ghi sóng của máy ECG (3 Quy tắc vàng bắt buộc nhớ)**:
  - *Quy tắc 1*: Vector hướng **về phía** cực dương $\rightarrow$ Sóng **dương** (hướng lên).
  - *Quy tắc 2*: Vector hướng **xa** cực dương $\rightarrow$ Sóng **âm** (hướng xuống).
  - *Quy tắc 3*: Vector **vuông góc** với trục chuyển đạo $\rightarrow$ Sóng **hai pha** hoặc đẳng điện.
- **2.3. Sự khác biệt giữa Khử cực và Tái cực**: Tại sao khử cực đi từ trong cơ tim ra ngoài cơ tim thì sóng QRS cùng chiều vector khử cực, nhưng tái cực lại đi từ ngoài cơ tim vào trong cơ tim làm sóng T thường cùng chiều với QRS ({claim:C-006}).
- *Mechanism Chain 2*: Hướng lan truyền sóng khử cực/tái cực $\rightarrow$ Hướng vector điện thế tổng $\rightarrow$ Góc hợp với trục chuyển đạo $\rightarrow$ Biên độ và chiều sóng hiển thị trên giấy ECG.

### 3. HỆ THỐNG CHUYỂN ĐẠO CHI & HỆ TRỤC SÁU CHIỀU [CỐT LÕI]
- **3.1. Tam giác Einthoven và Chuyển đạo chuẩn lưỡng cực (I, II, III)**:
  - Chuyển đạo I: Tay phải (âm) $\rightarrow$ Tay trái (dương).
  - Chuyển đạo II: Tay phải (âm) $\rightarrow$ Chân trái (dương).
  - Chuyển đạo III: Tay trái (âm) $\rightarrow$ Chân trái (dương).
  - Định luật Einthoven: $\text{Lead I} + \text{Lead III} = \text{Lead II}$.
- **3.2. Chuyển đạo đơn cực chi tăng cường (aVR, aVL, aVF)**:
  - Khái niệm cực trung tính Goldberger.
  - Vì sao aVR luôn có sóng P, QRS, T âm ở nhịp xoang bình thường.
- **3.3. Hệ trục sáu chiều (Mặt phẳng trán - Frontal Plane)**:
  - Góc của 6 chuyển đạo: I ($0^\circ$), aVL ($-30^\circ$), II ($+60^\circ$), aVF ($+90^\circ$), III ($+120^\circ$), aVR ($-150^\circ$).

### 4. HỆ THỐNG CHUYỂN ĐẠO TRƯỚC TIM & MẶT PHẲNG NGANG [CỐT LÕI]
- **4.1. Vị trí giải phẫu chính xác của 6 chuyển đạo trước tim (V1–V6)**:
  - V1: Khoang liên sườn 4 bờ phải xương ức.
  - V2: Khoang liên sườn 4 bờ trái xương ức.
  - V3: Điểm giữa V2 và V4.
  - V4: Khoang liên sườn 5 đường trung đòn trái.
  - V5: Khoang liên sườn 5 đường nách trước trái.
  - V6: Khoang liên sườn 5 đường nách giữa trái.
- **4.2. Nguyên lý diễn tiến sóng R/S từ V1 đến V6 (R-wave Progression)**:
  - V1–V2: Thất phải và vách liên thất $\rightarrow$ Sóng rS (S ưu thế).
  - V3–V4: Vùng chuyển tiếp (R/S $\approx 1$).
  - V5–V6: Thất trái ưu thế $\rightarrow$ Sóng qR hoặc R cao (R ưu thế).
- *Mechanism Chain 3*: Độ dày cơ thất trái vượt trội thất phải $\rightarrow$ Dominance của vector thất trái hướng về sau-trái-dưới $\rightarrow$ Tiến trình tăng dần biên độ sóng R và giảm dần sóng S từ V1 đến V6.

### 5. NGUYÊN LÝ HOẠT ĐỘNG CỦA MÁY ECG: THU NHẬN, LỌC VÀ SỐ HÓA [CỐT LÕI]
- **5.1. Thu nhận tín hiệu và Khuếch đại vi sai (Differential Amplifier)**:
  - Điện thế sinh học bề mặt da rất nhỏ ($0.1\text{ mV} - 5\text{ mV}$).
  - Mạch khuếch đại đảo và tỷ lệ loại bỏ tín hiệu chung (CMRR). Điện cực chân phải (RL) làm cực đất loại bỏ nhiễu điện lưới.
- **5.2. Nguyên lý Bộ lọc (Filter settings)**:
  - Bộ lọc thông cao (High-pass filter / Low-frequency cutoff): Chuẩn 0.05 Hz ({claim:C-001}). Nếu nâng lên 0.5 Hz hoặc 1 Hz sẽ làm đường đẳng điện biến dạng và ST giả trôi.
  - Bộ lọc thông thấp (Low-pass filter / High-frequency cutoff): Chuẩn 150 Hz ({claim:C-001}). Ảnh hưởng của việc hạ xuống 40 Hz ({claim:C-002}, {claim:C-003}).
  - Bộ lọc nhiễu điện lưới (Notch filter / Line filter): 50 Hz hoặc 60 Hz.
- **5.3. Số hóa tín hiệu (ADC - Analog-to-Digital Converter)**: Tần số lấy mẫu (Sampling rate $\ge 500\text{ Hz}$) và độ phân giải bit.

### 6. QUY ƯỚC GIẤY ECG & Ý NGHĨA CÁC Ô ĐO LƯỜNG [CỐT LÕI]
- **6.1. Tốc độ chạy giấy (Paper Speed)**:
  - Tốc độ chuẩn $25\text{ mm/s}$: 1 ô nhỏ ($1\text{ mm}$) = $0.04\text{ s}$ ($40\text{ ms}$); 1 ô lớn ($5\text{ mm}$) = $0.20\text{ s}$ ($200\text{ ms}$).
  - Tốc độ $50\text{ mm/s}$: 1 ô nhỏ = $0.02\text{ s}$ ($20\text{ ms}$). Khi nào cần dùng? (Phân tích nhịp nhanh).
- **6.2. Biên độ chuẩn (Calibration / Gain)**:
  - Biên độ chuẩn $10\text{ mm/mV}$ ($1\text{ mV} = 10\text{ mm} = 2\text{ ô lớn}$).
  - Biên độ $5\text{ mm/mV}$ ($1/2\text{ Standard}$) và $20\text{ mm/mV}$ ($2\text{ Standard}$).
- **6.3. Bảng tra cứu quy đổi nhanh ô giấy $\rightarrow$ Thời gian & Điện thế**.

### 7. NHẬN DIỆN NHIỄU, GIẢ ẢNH VÀ LỖI MẮC DÂY ĐIỆN CỰC [CỐT LÕI]
- **7.1. Các dạng nhiễu giả ảnh (Artifacts)**:
  - Nhiễu cơ (Somatic tremor / Muscle artifact): Do bệnh nhân run, lạnh, Parkinson.
  - Nhiễu đường đẳng điện trôi trượt (Wandering baseline): Do nhịp thở, mồ hôi, điện cực tiếp xúc kém.
  - Nhiễu điện lưới AC (50/60 Hz powerline interference): Do thiết bị điện xung quanh, bong tróc gel tiếp xúc.
- **7.2. Lỗi mắc sai dây điện cực chi (Limb Lead Reversals)**:
  - Đảo dây Tay phải - Tay trái (RA-LA reversal): Sóng P, QRS, T ở chuyển đạo I âm hoàn toàn; aVR và aVL tráo đổi vị trí ({claim:C-004}, {claim:C-005}, {claim:C-006}).
  - Đảo dây Tay phải - Chân trái (RA-LL reversal): Giả sóng nhồi máu cơ tim thành dưới.
  - Đảo dây Tay trái - Chân trái (LA-LL reversal): Thay đổi nhẹ trục, rất khó phát hiện ({claim:C-004}, {claim:C-005}).
  - Đảo dây Chân phải (Ground lead reversal): Xuất hiện đường bằng phẳng (Flatline) ở chuyển đạo II hoặc III.
- **7.3. Lỗi mắc sai vị trí điện cực trước tim (Precordial Lead Reversals & Misplacements)**:
  - Mắc sai thứ tự V1-V6: Vi phạm sự tiến triển tự nhiên của sóng R ({claim:C-007}).
  - Mắc V1, V2 quá cao (khoang liên sườn 2–3): Giả hình ảnh Brugada hoặc rSr' vách liên thất.

### 8. LƯU ĐỒ KIỂM TRA CHẤT LƯỢNG BẢN GHI ECG TRƯỚC KHI ĐỌC [CỐT LÕI]
- Flowchart ASCII kiểm tra chất lượng bản ghi theo từng bước:
  - Bước 1: Kiểm tra thông số Calibration (Speed & Gain).
  - Bước 2: Kiểm tra tín hiệu nhiễu baseline / nhiễu cơ.
  - Bước 3: Kiểm tra dấu hiệu mắc sai dây chi (P và QRS ở aVR có âm không?).
  - Bước 4: Kiểm tra đà phát triển sóng R trước tim (V1 $\rightarrow$ V6).

### 9. BẪY VÀ PHẢN VÍ DỤ NGHỊCH LÝ [CỐT LÕI]
- Liệt kê 6 bẫy hiểu sai kinh điển về nguyên lý ECG (vd: nhầm lẫn giữa điện cực âm/dương với bản chất sóng âm/dương; tưởng aVR âm là bệnh lý; nhầm nhiễu cơ Parkinson với cuồng nhĩ F wave; v.v.).

### 10. CHECKPOINT TỰ KIỂM TRA & CA LÂM SÀNG CÓ LỜI GIẢI [CỐT LÕI]
- 4 Checkpoint tự kiểm tra ngắn có đáp án chi tiết.
- 2 Ca lâm sàng thực tế với lời giải 6 bước chi tiết (Nhận diện vấn đề $\rightarrow$ Phân tích vector $\rightarrow$ Dự đoán hình dạng $\rightarrow$ Đối chiếu chuyển đạo $\rightarrow$ Loại phương án sai $\rightarrow$ Kết luận).

---

## 6. Hướng dẫn model execute

1. Viết bài với chế độ duy nhất `L3_BEGINNER`. Đảm bảo giải thích cực kỳ chi tiết từ gốc vật lý/sinh lý học.
2. Tuân thủ 100% `lesson_depth_contract` của profile `foundation` ($\ge 5.000$ từ, $\ge 500$ dòng không rỗng, $\ge 10$ sections, $\ge 12$ subsections, $\ge 3$ mechanism chains, $\ge 6$ ví dụ, $\ge 6$ bẫy/nhầm lẫn, $\ge 4$ checkpoints, $\ge 2$ ca lâm sàng có lời giải, $\ge 10$ practical tips).
3. Chỉ gắn nhãn verification chuẩn: `[GUIDELINE VERIFIED]`, `[DATA VERIFIED]`, `[ABSTRACT VERIFIED]`.
4. Viết tiếng Việt có dấu đầy đủ. Thuật ngữ tiếng Anh đặt trong ngoặc đơn sau tiếng Việt ở lần xuất hiện đầu tiên.
5. Flowchart vẽ bằng khối `text` ASCII. Không dùng Mermaid.
