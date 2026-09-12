# BÀN GIAO: QA theo dõi đáp ứng, điện giải và chỉnh liều lợi tiểu

## Prompt dán nguyên văn cho model tiếp theo

Bạn đang làm việc trong workspace:

`F:\DL\mavisresearch\Bai hoc y khoa\`

Hãy đọc trước:

1. `F:\DL\mavisresearch\AGENTS.md`
2. `F:\DL\mavisresearch\Bai hoc y khoa\AGENTS.md`
3. `F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu\IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu_2026-07-29_RELEASE_v3.cards.v2.json`
4. `F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\Thuoc_loi_tieu\Thuoc_loi_tieu_2026-07-22_RELEASE_v2.md`
5. `F:\DL\mavisresearch\medical_qa\templates\qa_template.md`

### Yêu cầu của người dùng

Tạo **một QA thực hành độc lập** ngay trong folder:

`F:\DL\mavisresearch\Bai hoc y khoa\11_Noi khoa\IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu\`

Chủ đề chính xác:

> Hướng dẫn theo dõi đáp ứng lợi tiểu, theo dõi điện giải đồ và chỉnh liều lợi tiểu trong các bệnh lý phổ biến.

QA phải đi kèm một **APKG riêng**, đủ chi tiết để học bằng Anki mà không buộc phải đọc lại toàn bộ QA.

### Đầu ra bắt buộc

1. QA Markdown, đề xuất basename:
   - `QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.md`
2. Cards V2 JSON đặt cạnh QA:
   - `QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.cards.v2.json`
3. APKG đặt trong `outputs/`:
   - `outputs/Anki - QA_Huong_dan_theo_doi_va_chinh_lieu_loi_tieu_2026-07-29.apkg`
4. Báo cáo package-level trong `outputs/`, ghi rõ những gate thực sự đã chạy; không tạo PASS giả.

### Phạm vi nội dung phải phủ

#### 1. Khung chung trước khi chỉnh liều

- Xác định mục tiêu: giảm sung huyết/phù, kiểm soát huyết áp hoặc mục tiêu chuyên khoa.
- Đánh giá ban đầu: cân nặng khô/hiện tại, triệu chứng, phù, tĩnh mạch cổ/phổi khi phù hợp, huyết áp kể cả tư thế, tưới máu, lượng nước tiểu và dịch vào–ra.
- Xét nghiệm nền: Na, K, creatinine/eGFR; cân nhắc Mg, Cl, bicarbonate, ure, glucose, uric acid theo nhóm thuốc và bệnh cảnh.
- Rà thuốc/yếu tố cản đáp ứng: NSAID, ăn mặn, bỏ liều, giảm hấp thu đường uống, CKD, giảm tưới máu, thuốc ảnh hưởng hệ renin–angiotensin và thuốc giữ kali.
- Không dùng “tiểu nhiều” đơn độc làm tiêu chuẩn đáp ứng.

#### 2. Cách đánh giá đáp ứng

- Ngoại trú: triệu chứng, cân nặng theo chuỗi, phù, huyết áp, tưới máu, khả năng hoạt động và xét nghiệm.
- Nội trú: triệu chứng/hô hấp, cân nặng hằng ngày, dịch vào–ra, lượng nước tiểu theo thời điểm, Na/K/Mg/creatinine và huyết động.
- Phân biệt:
  - còn sung huyết nhưng tưới máu ổn;
  - đã gần euvolemia;
  - giảm thể tích;
  - kháng lợi tiểu giả do không tuân thủ/ăn mặn/NSAID;
  - kháng lợi tiểu thật cần hội chẩn hoặc khóa nephron nối tiếp.

#### 3. Theo dõi và chỉnh liều theo thuốc

- Lợi tiểu quai: furosemide/torsemide/bumetanide.
- Thiazide/thiazide-like: hydrochlorothiazide, indapamide, chlorthalidone, metolazone.
- Đối kháng mineralocorticoid: spironolactone/eplerenone.
- Chẹn ENaC: amiloride/triamterene ở mức nguyên tắc an toàn.
- Acetazolamide và mannitol chỉ trình bày khi có chỉ định chuyên khoa; không biến thành thuốc giảm phù ngoại trú thường quy.
- Với mỗi nhóm phải nêu: theo dõi gì, thời điểm kiểm lại, hướng rối loạn điện giải/acid–base, khi nào giảm liều, tạm ngưng, ngừng và chuyển tuyến.

#### 4. Các bệnh cảnh phổ biến

- Suy tim mạn có sung huyết.
- Suy tim cấp/phù phổi: chỉ xử trí trong môi trường có monitor; không cho thuật toán tự chỉnh tại nhà.
- Tăng huyết áp dùng thiazide/thiazide-like.
- CKD có quá tải dịch.
- Hội chứng thận hư/phù do bệnh cầu thận.
- Xơ gan cổ trướng.
- Có thể thêm phù do thuốc/suy tĩnh mạch để nhấn mạnh không phải mọi phù đều cần tăng lợi tiểu.

#### 5. Khóa nephron nối tiếp

- Chỉ cân nhắc sau khi rà tuân thủ, natri ăn vào, NSAID, hấp thu, tưới máu và chức năng thận.
- Nêu rõ nguy cơ hạ Na, hạ K, hạ Mg, AKI và giảm thể tích.
- Phối hợp quai + thiazide/thiazide-like phải có kế hoạch xét nghiệm sớm và năng lực xử trí; thiếu xét nghiệm là lý do chuyển tuyến, không phải lý do phối hợp mù.

#### 6. Red flags và nhánh dừng

- Giảm oxy/phù phổi.
- Sốc hoặc dấu giảm tưới máu.
- Vô niệu/thiểu niệu mới rõ.
- Lú lẫn, co giật hoặc triệu chứng thần kinh.
- Loạn nhịp, yếu cơ nặng hoặc nghi K bất thường có ý nghĩa.
- Creatinine tăng nhanh/AKI.
- Hạ Na có triệu chứng.
- Tăng K nặng hoặc thay đổi ECG.
- Xơ gan có lú lẫn, nhiễm trùng, tụt huyết áp hoặc suy thận.

### Yêu cầu về thuật toán chỉnh liều

- Không viết một “liều chuẩn” áp dụng cho mọi bệnh nhân.
- Mọi thay đổi liều phải dựa đồng thời trên:
  1. còn hay hết sung huyết;
  2. tưới máu/thể tích;
  3. Na/K/Mg và acid–base;
  4. creatinine/eGFR và xu hướng;
  5. bệnh nền và thuốc phối hợp.
- Tạo các nhánh rõ:
  - **Đáp ứng tốt, còn sung huyết, an toàn:** tiếp tục theo protocol và đánh giá lại.
  - **Đã euvolemia:** giảm về liều thấp nhất duy trì; tránh giữ liều tấn công.
  - **Không đáp ứng nhưng chưa độc tính:** rà nguyên nhân sửa được trước khi tăng/phối hợp.
  - **Giảm thể tích hoặc AKI:** không tăng liều; đánh giá giảm/ngưng theo bệnh cảnh và xử trí nguyên nhân.
  - **Rối loạn điện giải:** sửa theo mức độ và thuốc gây ra; triệu chứng/nặng → cấp cứu hoặc hội chẩn.
- Phân biệt MRA dùng như điều trị nền suy tim với MRA dùng để lợi tiểu/cổ trướng; không giảm/ngừng thuốc chỉ dựa vào creatinine đơn độc mà bỏ qua K, thể tích, chỉ định và protocol.

### Nguồn chính đã tìm được

Các URL sau đã đọc được và nên dùng làm nền. Phải kiểm tra lại phiên bản/ngày cập nhật khi viết:

1. NHS Specialist Pharmacy Service — Furosemide monitoring, cập nhật 20-02-2025:
   - https://www.sps.nhs.uk/monitorings/furosemide-monitoring/
   - Baseline: huyết áp, điện giải, creatinine.
   - Sau khởi trị/tăng liều: 1–2 tuần; 5–7 ngày nếu nguy cơ cao.
   - Ổn định: điện giải và creatinine mỗi 6 tháng.
   - Có các nhánh theo % tăng creatinine/eGFR, K và Na; cần trích chính xác từ trang, không nhớ rồi viết lại.

2. NHS SPS — Spironolactone monitoring, cập nhật 19-02-2026:
   - https://sps.nhs.uk/monitorings/spironolactone-monitoring/
   - Trong suy tim: baseline creatinine/eGFR, điện giải, K.
   - Sau khởi trị/tăng liều: sau 1 tuần; hằng tháng 3 tháng đầu; sau đó mỗi 3 tháng trong một năm; ổn định mỗi 6 tháng.
   - Có ngưỡng giảm liều/ngừng theo K, creatinine và eGFR; trích đúng từ nguồn.

3. NHS SPS — Eplerenone monitoring, cập nhật 16-12-2025:
   - https://www.sps.nhs.uk/monitorings/eplerenone-monitoring/
   - Baseline eGFR/creatinine, điện giải, K; sau 1 tuần rồi hằng tháng 3 tháng đầu; ổn định mỗi 6 tháng.
   - Có thuật toán chỉnh liều theo K và eGFR; trích đúng.

4. KDIGO 2024 CKD Guideline chính thức:
   - https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf
   - Theo dõi GFR/albuminuria ít nhất hằng năm ở CKD; thường xuyên hơn nếu nguy cơ cao và kết quả làm thay đổi điều trị.
   - Thay đổi eGFR >20% vượt biến thiên kỳ vọng và cần đánh giá.
   - Dùng phần medication review, volume depletion, hyperkalemia và specialist referral.
   - Không áp ngưỡng của ACEi/ARB sang lợi tiểu nếu nguồn không nói như vậy.

5. AASLD clinical education — Management of Refractory Ascites in Cirrhosis, 29-09-2025:
   - https://www.aasld.org/liver-fellow-network/core-series/clinical-pearls/management-refractory-ascites-cirrhosis
   - Đây là trang giáo dục/clinical pearl, **không tự gán `[GUIDELINE VERIFIED]`**.
   - Trang dẫn đến AASLD 2021 guidance và mô tả cổ trướng kháng trị/không dung nạp do azotemia, bệnh não gan hoặc rối loạn điện giải.
   - Nên tìm và dùng official AASLD 2021 guidance làm nguồn thẩm quyền chính cho liều/tỷ lệ/mốc dừng.

6. Existing project lessons for context only:
   - `11_Noi khoa/Thuoc_loi_tieu/Thuoc_loi_tieu_2026-07-22_RELEASE_v2.md`
   - `11_Noi khoa/IM-22_Suy_tim/IM-22_Suy_tim_2026-07-17.md`
   - `11_Noi khoa/IM-40_Xo_gan_tang_ap_cua/IM-40_Xo_gan_tang_ap_cua_2026-07-19.md`
   - Không sao chép mù: một số bài legacy có nhãn cũ, flowchart Mermaid, con số chưa qua pipeline mới hoặc nội dung quá cứng.

### Governance nguồn — bắt buộc

- Project hiện dùng provider-neutral evidence bundle; không gọi NCBI/E-utilities trong release workflow.
- Không tự gắn bất kỳ nhãn verification nào.
- Chỉ năm nhãn canonical được phép khi có đúng artifact: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.
- Cấm các nhãn legacy: `[TEXTBOOK]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[FULL VERIFIED]`.
- Claim định lượng, liều, timing, ngưỡng K/Na/creatinine/eGFR phải có nguồn chính xác và được phân biệt theo thuốc/bệnh cảnh.
- Nếu chưa build được evidence bundle canonical, vẫn có thể tạo QA/APKG package-level nhưng phải ghi rõ **không phải PUBLISH READY**; không dựng manifest PASS giả.
- Không viện dẫn bài cũ làm nguồn thẩm quyền cho protocol.

### Quy cách viết QA

- Tiếng Việt có dấu đầy đủ; thuật ngữ Việt trước, tiếng Anh trong ngoặc ở lần đầu.
- Không dùng bảng Markdown phức tạp từ 4 cột trở lên; ưu tiên heading + bullet.
- Không dùng Mermaid; dùng danh sách phân cấp hoặc flowchart ASCII trong block `text`.
- QA phải có:
  - câu hỏi gốc;
  - trả lời ngắn;
  - thuật toán thực hành;
  - giải thích;
  - các bệnh cảnh;
  - red flags/cấp cứu;
  - câu hỏi cần hỏi thêm;
  - nguồn và mức chứng cứ;
  - liên kết đến IM-43b.
- Nêu rõ đây là tài liệu học tập cho nhân viên y tế, không thay protocol bệnh viện và đánh giá trực tiếp.

### Cards V2/APKG

- Cards V2 là list JSON, mỗi thẻ ít nhất có:
  - `type: "basic"`
  - `front`
  - `back`
  - `extra`
  - ID ổn định riêng, ví dụ `QA-DIURETIC-001`.
- APKG phải đủ sâu để thay việc đọc QA, đề xuất khoảng 80–120 thẻ tùy độ dài thực tế; không ép số lượng nếu dẫn đến thẻ trùng.
- Phải phủ: baseline, đánh giá đáp ứng, lịch lab, Na/K/Mg/creatinine, các nhóm thuốc, từng bệnh cảnh, kháng lợi tiểu, chỉnh liều, sick-day advice, red flags và cases.
- Không có front/back rỗng; không trùng câu hỏi; không có thẻ meta kiểu “bài này dạy gì”.
- Build bằng:

```text
python "F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python/build_apkg.py" "<cards.v2.json>" --output "<outputs/APKG>" --verify
```

- Sau build phải mở SQLite trong APKG và xác nhận:
  - source count = note count = card count;
  - 0 missing source pairs;
  - 0 unexpected pairs;
  - 0 blank pairs;
  - 0 duplicate pairs;
  - dấu tiếng Việt PASS.

### Tình trạng workstream trước bàn giao

- Chưa tạo QA, Cards V2 hoặc APKG QA.
- Chỉ mới khảo sát template và nguồn.
- APKG chính của IM-43b đã rebuild trước đó, không được ghi đè:
  - `outputs/Anki - IM-43b_Sinh_ly_Nephron_va_Thuoc_loi_tieu_2026-07-29_RELEASE_v3.apkg`
  - 160 notes/160 cards, dấu tiếng Việt 95,8%.
- Hãy tạo deck QA riêng với model/deck ID tự sinh từ basename mới.

### Acceptance criteria

- QA trả lời thực hành được câu hỏi “đo gì, đo khi nào, diễn giải thế nào, tăng/giảm/ngừng khi nào” mà không biến thành đơn thuốc chung cho mọi người.
- Bệnh cảnh suy tim, tăng huyết áp, CKD/phù thận và xơ gan được tách rõ.
- Tất cả liều/ngưỡng/timing có nguồn và đúng phạm vi nguồn.
- APKG riêng import được, đầy đủ, không trùng/rỗng, note/card count khớp Cards V2.
- Báo cáo cuối phải liệt kê file, số thẻ, lệnh/gate đã chạy và giới hạn verification còn lại.
