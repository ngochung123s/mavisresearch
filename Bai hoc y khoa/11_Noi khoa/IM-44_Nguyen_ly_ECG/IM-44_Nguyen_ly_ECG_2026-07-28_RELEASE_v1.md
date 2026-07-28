# Nguyên lý ECG và nguyên lý hiển thị hình ảnh sóng ECG

**Revision phát hành:** RELEASE v1
**Research brief khóa nguồn:** [IM-44_Nguyen_ly_ECG_2026-07-28_RELEASE_v1_RESEARCH_BRIEF.md](IM-44_Nguyen_ly_ECG_2026-07-28_RELEASE_v1_RESEARCH_BRIEF.md)

---

## 0.1 Nền tảng tối thiểu cần dùng ngay

- **Điện thế nghỉ:** Khi tế bào cơ tim nghỉ ngơi, bên trong màng mang điện tích âm so với bên ngoài.
- **Khử cực (Depolarization):** Là quá trình đảo ngược điện thế, khi dòng ion dương (chủ yếu là Na+ và Ca2+) ồ ạt đi vào trong tế bào, làm bên trong trở nên dương hơn.
- **Tái cực (Repolarization):** Là quá trình phục hồi lại điện thế nghỉ, chủ yếu do dòng K+ đi ra ngoài tế bào.
- **Lưỡng cực điện (Dipole):** Khi một phần tế bào đã khử cực (bề mặt tích điện âm) và phần kế tiếp chưa khử cực (bề mặt tích điện dương), giữa chúng xuất hiện một sự chênh lệch điện thế, tạo thành một vector điện học hướng từ vùng âm sang vùng dương.

## 1. Tổng quan và định nghĩa

Điện tâm đồ (Electrocardiogram - ECG) là bản ghi lại các thay đổi điện thế của tim theo thời gian, được thu nhận từ các điện cực đặt trên bề mặt cơ thể. Nó không đo trực tiếp sức co bóp của cơ tim, mà chỉ đo lường các dòng điện kích hoạt sự co bóp đó.

## 2. Cơ chế điện sinh lý cơ bản

Quá trình tạo ra sóng ECG diễn ra qua nhiều tầng:

- **Tầng 1 (Phân tử):** Các kênh ion trên màng tế bào mở ra. Dòng Na+ đi vào rất nhanh tạo pha khử cực nhanh ở tế bào cơ nhĩ và cơ thất. Dòng Ca2+ đi vào chậm hơn tạo pha bình nguyên (plateau), và dòng K+ đi ra tạo pha tái cực.
- **Tầng 2 (Tế bào/Mô):** Sự khử cực không diễn ra đồng thời ở mọi tế bào. Nó bắt đầu từ nút xoang (SA), lan ra cơ nhĩ, hội tụ tại nút nhĩ thất (AV), đi xuống bó His, mạng Purkinje và cuối cùng lan tỏa khắp cơ thất. Sự lan truyền tuần tự này tạo ra một ranh giới di chuyển liên tục giữa vùng đã khử cực và vùng chưa khử cực.
- **Tầng 3 (Lâm sàng/Hiển thị):** Hàng triệu tế bào khử cực cùng lúc tạo ra hàng triệu vector nhỏ. Tổng hợp tất cả các vector này tại một thời điểm nhất định sẽ cho ra một **Vector điện học trung bình của tim** trong không gian 3 chiều.
- **Tầng 4 (Quyết định):** Máy ECG đóng vai trò như một vôn kế (voltmeter) cực nhạy. Nó không thể vẽ trực tiếp vector 3D này, mà chỉ có thể ghi lại **hình chiếu** của vector đó lên các trục chuyển đạo (Leads) 1 chiều.
- **Tầng 5 (Hậu quả/Sai lầm):** Nếu hiểu sai nguyên lý hình chiếu, người đọc có thể nhầm lẫn một sóng âm bình thường (do vector hướng ra xa điện cực) thành một dấu hiệu bệnh lý (như sóng Q hoại tử).

## 3. Nguyên lý hình chiếu Vector (CỐT LÕI)

Mỗi chuyển đạo (Lead) của ECG có một điện cực dương và một điện cực âm (hoặc một điểm trung tính làm mốc). Trục của chuyển đạo là đường thẳng nối từ cực âm đến cực dương. Máy ECG ghi lại hình chiếu của vector điện tim lên trục này theo 3 quy tắc vàng:

1. **Quy tắc 1 (Sóng dương):** Khi vector điện tim hướng **về phía** điện cực dương của một chuyển đạo, máy sẽ ghi lại một sóng đi lên (sóng dương). Vector càng song song với trục, sóng càng cao.
2. **Quy tắc 2 (Sóng âm):** Khi vector điện tim hướng **ra xa** điện cực dương, máy sẽ ghi lại một sóng đi xuống (sóng âm).
3. **Quy tắc 3 (Sóng 2 pha/Triệt tiêu):** Khi vector điện tim hướng **vuông góc** với trục của chuyển đạo, máy sẽ ghi lại một sóng có biên độ bằng 0 (đường đẳng điện) hoặc một sóng có cả phần dương và phần âm bằng nhau (sóng 2 pha).

## 4. Hệ thống chuyển đạo (Leads)

Để quan sát vector điện tim 3D, chúng ta cần nhiều góc nhìn khác nhau. ECG chuẩn 12 chuyển đạo cung cấp 12 góc nhìn, chia làm hai mặt phẳng:

### 4.1 Mặt phẳng trán (Frontal plane)
Được tạo bởi 6 chuyển đạo chi, giúp xác định trục điện tim lên/xuống, trái/phải.
- **Tam giác Einthoven (Chuyển đạo lưỡng cực):** 
  - DI: Từ tay phải (-) sang tay trái (+). Nhìn tim từ bên trái.
  - DII: Từ tay phải (-) sang chân trái (+). Nhìn tim từ dưới lên, chếch trái. Đây là góc nhìn song song nhất với trục khử cực bình thường của tim, nên sóng P và R thường cao nhất ở DII.
  - DIII: Từ tay trái (-) sang chân trái (+). Nhìn tim từ dưới lên, chếch phải.
- **Chuyển đạo chi tăng cường (Chuyển đạo đơn cực):**
  - aVR: Điện cực dương ở tay phải. Nhìn tim từ vai phải xuống. Vì trục tim bình thường hướng xuống dưới và sang trái (ra xa tay phải), mọi sóng ở aVR bình thường đều âm.
  - aVL: Điện cực dương ở tay trái. Nhìn tim từ vai trái.
  - aVF: Điện cực dương ở chân trái. Nhìn tim từ dưới lên.
Sáu chuyển đạo này cắt nhau tạo thành **Hệ thống trục tọa độ 6 chiều (Hexaxial reference system)**.

### 4.2 Mặt phẳng ngang (Horizontal plane)
Được tạo bởi 6 chuyển đạo trước tim (V1 đến V6), giúp nhìn tim từ trước ra sau, từ phải sang trái.
- V1, V2: Nhìn thất phải và vách liên thất.
- V3, V4: Nhìn thành trước thất trái.
- V5, V6: Nhìn thành bên thất trái.

## 5. Chuẩn hóa kỹ thuật và giấy ECG

Giấy ECG là giấy kẻ ô ly chuẩn, di chuyển với tốc độ không đổi. Trục hoành biểu diễn thời gian, trục tung biểu diễn biên độ điện thế.

- **Trục thời gian (Ngang):** 
  - Vận tốc giấy chuẩn là 25 mm/s. {claim:C-002} PMID: 17349896 [GUIDELINE VERIFIED]
  - Ở tốc độ này, 1 ô vuông nhỏ (1 mm) = 0.04 giây.
  - 1 ô vuông lớn (5 ô nhỏ) = 0.2 giây.
- **Trục biên độ (Dọc):**
  - Test amplitude (calibration) chuẩn là 10 mm/mV. {claim:C-003} PMID: 17349896 [GUIDELINE VERIFIED]
  - Nghĩa là 1 ô vuông nhỏ (1 mm) = 0.1 mV.
  - 1 ô vuông lớn (5 ô nhỏ) = 0.5 mV.
- **Tần số cắt lọc (Filter):**
  - Máy ECG dùng các bộ lọc để loại bỏ nhiễu (như nhiễu điện lưới 50/60Hz, nhiễu do rung cơ).
  - Tần số cắt lọc (filter) chuẩn cho ECG chẩn đoán người lớn là 0.05 Hz đến 150 Hz. {claim:C-001} PMID: 17349896 [GUIDELINE VERIFIED]

## 6. Flowchart và BOX ĐỎ

### Flowchart tiếp cận hình thức bản ghi
```text
Bản ghi ECG
   ↓
Kiểm tra Calibration (Test mV)
   ├─ Không phải 10 mm/mV → Chú ý khi đọc biên độ (phì đại)
   └─ 10 mm/mV → Tiếp tục
         ↓
Kiểm tra Tốc độ giấy
   ├─ Không phải 25 mm/s → Chú ý khi tính nhịp và các khoảng thời gian
   └─ 25 mm/s → Tiếp tục
         ↓
Kiểm tra Filter
   ├─ Cắt tần số thấp quá cao (vd: 0.5 Hz) → Cẩn thận méo ST
   └─ Chuẩn 0.05 - 150 Hz → Bắt đầu đọc các sóng
```

### BOX ĐỎ: An toàn kỹ thuật
- **Mắc lộn điện cực (Lead reversal):** Lỗi phổ biến nhất là đổi chỗ điện cực tay phải (đỏ) và tay trái (vàng). Hậu quả là DI bị đảo ngược hoàn toàn (P âm, QRS âm, T âm), aVR và aVL đổi chỗ cho nhau. Rất dễ chẩn đoán nhầm thành nhịp nhĩ lạc chỗ, trục lệch phải, hoặc nhồi máu cơ tim cũ thành bên. Luôn nghi ngờ khi thấy P âm ở DI và P dương ở aVR.
- **Cài đặt filter sai:** Nếu bộ lọc tần số thấp (low-frequency filter) được cài đặt quá cao (ví dụ 0.5 Hz thay vì 0.05 Hz để lọc nhiễu đường nền), nó có thể làm méo đoạn ST, tạo ra hình ảnh ST chênh lên hoặc chênh xuống giả tạo, dẫn đến chẩn đoán nhầm nhồi máu cơ tim cấp.

## 7. Case 1 lâm sàng, Chẩn đoán sai lầm và Theo dõi

- **Case 1:** Một bệnh nhân đến khám sức khỏe định kỳ. Bản ghi ECG cho thấy sóng P âm, phức bộ QRS âm và sóng T âm ở chuyển đạo DI. Ở chuyển đạo aVR, toàn bộ các sóng này lại dương. Bệnh nhân không có tiền sử bệnh tim mạch, khám lâm sàng mỏm tim vẫn ở bên trái lồng ngực.
  - **Phân tích (Chẩn đoán):** Theo nguyên lý vector, trục khử cực nhĩ bình thường hướng từ phải sang trái, tức là hướng về phía điện cực dương của DI (tay trái). Do đó P ở DI phải dương. Việc toàn bộ sóng ở DI âm và aVR dương ở một người có tim nằm bên trái gợi ý mạnh mẽ rằng vector đã bị "nhìn ngược".
  - **Kết luận (Theo dõi):** Đây là lỗi mắc lộn điện cực tay phải và tay trái. Cần mắc lại điện cực và đo lại ECG trước khi đưa ra bất kỳ chẩn đoán bệnh lý nào.

## 8. Tóm tắt và Mẹo lâm sàng (Tips)

- ECG ghi lại hình chiếu của vector điện tim 3D lên các trục chuyển đạo 1D.
- Vector hướng về cực dương tạo sóng dương, hướng ra xa tạo sóng âm, vuông góc tạo sóng 2 pha.
- Luôn kiểm tra chuẩn hóa trước khi đọc: tốc độ 25 mm/s, biên độ 10 mm/mV, và filter 0.05-150 Hz.
- Hiểu rõ nguyên lý hình chiếu giúp nhận biết các lỗi kỹ thuật (như mắc lộn điện cực) và tránh chẩn đoán nhầm.

## 9. Tài liệu tham khảo

1. **Kligfield P, Gettes LS, Bailey JJ, et al.** Recommendations for the standardization and interpretation of the electrocardiogram: part I: the electrocardiogram and its technology: a scientific statement from the American Heart Association Electrocardiography and Arrhythmias Committee, Council on Clinical Cardiology; the American College of Cardiology Foundation; and the Heart Rhythm Society. *J Am Coll Cardiol* 2007;49(10):1109-1127. [PMID: 17349896] [GUIDELINE VERIFIED]
