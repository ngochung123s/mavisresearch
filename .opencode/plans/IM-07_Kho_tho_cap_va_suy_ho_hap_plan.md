# Plan triển khai IM-07 — Tiếp cận bệnh nhân khó thở cấp và suy hô hấp

**Ngày lập:** 2026-07-17  
**Đích:** Bài P0 cho bác sĩ Nội khoa tuyến tỉnh, học viên sau đại học và sinh viên năm cuối.  
**Deliverables:** Bài Markdown nguồn + `cards.v2.json` + Anki `.apkg`; knowledge check sau build. PPTX không thuộc scope.

---

## 1. Mục tiêu và ranh giới

### Mục tiêu lâm sàng

Sau bài này, người học phải làm được năm việc trong lần tiếp cận đầu tiên:

1. Nhận diện ngay khó thở có dấu hiệu đe dọa tính mạng và gọi hỗ trợ/ICU đúng lúc.
2. Phân biệt ưu thế thất bại **oxy hóa** với thất bại **thông khí**, dựa trên khám, SpO₂ và khí máu đúng chỉ định.
3. Bắt đầu oxy/hỗ trợ hô hấp với mục tiêu bão hòa và thiết bị phù hợp, đồng thời đánh giá lại sớm.
4. Định hướng các nguyên nhân nguy hiểm cần loại trừ trước: tắc nghẽn đường thở trên, hen/COPD nặng, phù phổi cấp, viêm phổi/sepsis, thuyên tắc phổi, tràn khí màng phổi áp lực, chèn ép tim, toan chuyển hóa nặng/ngộ độc.
5. Quyết định được: theo dõi thường, theo dõi liên tục/đơn vị hồi sức, thử HFNO/NIV có giám sát, hay đặt nội khí quản và chuyển ICU ngay.

### Trong scope

- Tiếp cận 0–15 phút và đánh giá lại theo thời gian.
- ABCDE dành riêng cho khó thở; dấu hiệu mệt cơ hô hấp và dấu hiệu thất bại hỗ trợ không xâm nhập.
- Phân loại suy hô hấp giảm oxy máu, tăng CO₂, hoặc hỗn hợp.
- Oxy có mục tiêu; HFNO, CPAP/BiPAP/NIV ở mức **chỉ định, chống chỉ định, theo dõi và ngưỡng thất bại**.
- Chẩn đoán phân biệt theo pattern lâm sàng và xét nghiệm/hình ảnh tại giường.
- Khung chuyển ICU/chuyển tuyến và 3–4 ca tích hợp.

### Ngoài scope — phải link sang bài khác

- Phác đồ điều trị hoàn chỉnh của từng căn nguyên: COPD (IM-30), hen (IM-29), viêm phổi cộng đồng (IM-31), suy tim (IM-22), PE/DVT (IM-33), tràn khí/tràn dịch/empyema (IM-32), sepsis (IM-11), ACS (IM-21).
- Kỹ thuật đặt nội khí quản, cài đặt máy thở xâm nhập và ARDS đầy đủ; chỉ dạy **dấu hiệu gọi đội đặt nội khí quản/ICU**, không dạy quy trình thủ thuật.
- POCUS là xét nghiệm định hướng tại giường, không biến thành bài kỹ thuật; kỹ thuật POCUS riêng thuộc IM-93.
- Nhi khoa, sản khoa, chấn thương và chăm sóc tiền viện chuyên sâu.

### Liên kết curriculum

- IM-07 chính thức phụ thuộc IM-01 đến IM-06. Vì các bài này chưa có, mở bài phải đặt một box “nền cần nắm”: ABCDE, sinh hiệu/triage, problem list, khí máu cơ bản, ECG/X-quang ngực cơ bản và kê đơn an toàn.
- IM-07 là nền thực hành cho IM-29 đến IM-34 và hỗ trợ các bài cấp cứu khác.

---

## 2. Nguồn xương sống đã xác minh để research

Bài không dùng một guideline duy nhất cho toàn bộ khó thở cấp; dùng mỗi guideline đúng phạm vi của nó.

1. **SFMU/SRLF 2026 — Initial Assessment of Respiratory Distress in the Emergency Department**. PMID: 41788490. Nguồn chính cho triage, dấu hiệu nặng, theo dõi, khí máu, hướng PE, BNP và siêu âm tim-phổi tích hợp.
2. **AARC 2022 — Management of Adult Patients With Oxygen in the Acute Care Setting**. PMID: 34728574. Nguồn chính cho oxy có mục tiêu và HFNO trong acute care.
3. **BTS emergency oxygen guideline 2017, interim update 2019**. PMID: 28507176; bản web BTS xác nhận vẫn giữ target 94–98% ở đa số bệnh nhân và 88–92% khi nguy cơ suy hô hấp tăng CO₂, trong khi chờ khí máu.
4. **ERS/ATS NIV guideline 2017**. PMID: 28860265. Nguồn chính cho NIV trong đợt cấp COPD có toan hô hấp và phù phổi cấp do tim; dùng cẩn trọng ở suy hô hấp giảm oxy mới xuất hiện.
5. **ESICM ARDS/AHRF 2023**. PMID: 37326646. Nguồn chính cho HFNO trong suy hô hấp giảm oxy cấp không do COPD/phù phổi cấp do tim và cảnh báo không trì hoãn đặt nội khí quản.
6. **BTS/ICS acute hypercapnic respiratory failure 2016**. PMID: 26976648. Nguồn bổ sung cho suy hô hấp tăng CO₂ và tổ chức NIV.

### Nguyên tắc evidence khi execute

- Chỉ đưa **liều, lưu lượng, thời điểm, chỉ số hoặc ngưỡng số học** khi đã fetch guideline/paper gốc và xác minh ở abstract/toàn văn; ghi PMID sát claim và tag `[FULL VERIFIED]` nếu là số liệu cụ thể.
- Khuyến cáo của SFMU/SRLF có thể dùng cho quy trình triage, nhưng cần ghi rõ đây là guideline của cấp cứu/hồi sức Pháp; không mặc định coi là protocol Bộ Y tế Việt Nam.
- Phải kiểm tra hướng dẫn Bộ Y tế Việt Nam từng căn nguyên nếu đưa nội dung “áp dụng tại Việt Nam”; nếu không tìm được văn bản phù hợp, chỉ mô tả giới hạn nguồn lực và đường hội chẩn, không bịa protocol quốc gia.
- Registry hiện chưa có nhóm guideline Nội khoa/hô hấp. Preflight script match sai sang ESHRE, nên **không dùng kết quả match đó**; khi build phải thêm các guideline đã chọn vào registry theo convention hiện có rồi chạy lại preflight/verification.

---

## 3. Cấu trúc bài Markdown đề xuất

### 0. Tổng quan — “Khó thở là hội chứng, không phải chẩn đoán” [CỐT LÕI]

- Nêu nguyên tắc: ổn định sinh lý trước, không chờ chẩn đoán hoàn chỉnh.
- 5 mục tiêu lâm sàng nêu trên.
- Box prerequisite IM-01–IM-06.

### 1. Nhận diện suy hô hấp và dấu hiệu cần hành động ngay [CỐT LÕI]

- Phân biệt dyspnea (triệu chứng), respiratory distress (biểu hiện), acute respiratory failure (thất bại trao đổi khí).
- Dấu hiệu đỏ: không nói được câu trọn, tri giác giảm, tím, vã mồ hôi, co kéo/cơ hô hấp phụ, thở bụng nghịch thường, ngừng thở/kiệt sức, huyết động không ổn.
- Không dùng một con số SpO₂ hoặc tần số thở đơn độc để an tâm; đặt trong xu hướng và công thở.
- Checkpoint 1: nhận diện “bệnh nhân sắp mệt cơ hô hấp”.

### 2. Tiếp cận 0–15 phút: ABCDE song song với xử trí [CỐT LÕI]

- A: tắc nghẽn đường thở trên, tiếng thở rít, dị vật/phù mạch; gọi hỗ trợ sớm.
- B: đánh giá công thở, RR, SpO₂, nghe phổi, khí máu khi nó thay đổi quyết định hỗ trợ/đích đến.
- C/D/E: sốc, ACS/loạn nhịp, sốt/sepsis, bất thường chuyển hóa, thuốc/ngộ độc.
- Đặt monitor, đường truyền, ECG; chẩn đoán và can thiệp chạy song song.
- Mermaid flowchart 1: “khó thở cấp tại cửa cấp cứu”.

### 3. Hai kiểu thất bại sinh lý: oxy hóa và thông khí [CỐT LÕI]

- Cơ chế ngắn: V/Q mismatch, shunt, giảm thông khí phế nang, tăng công thở/mệt cơ.
- Bảng nhỏ: giảm oxy máu, tăng CO₂/toan hô hấp, hỗn hợp — dấu hiệu, khí máu, nguyên nhân gợi ý, hành động.
- SpO₂, VBG/ABG: khi VBG chỉ hỗ trợ đánh giá CO₂; không dùng VBG để định lượng oxy hóa. ABG không làm thường quy nhưng dùng khi SpO₂ không tin cậy, nghi tăng CO₂/toan, cần NIV/intubation hoặc quyết định ICU.
- Checkpoint 2: giải thích một ca “SpO₂ cải thiện nhưng bệnh nhân xấu đi”.

### 4. Oxy và hỗ trợ hô hấp: chọn đúng công cụ, đánh giá lại đúng lúc [CỐT LÕI]

- Oxy là thuốc: ghi target trước khi chọn dụng cụ; đa số 94–98%, nguy cơ tăng CO₂ 88–92% cho đến khi có khí máu/đánh giá lại.
- Oxy thông thường → HFNO → CPAP/BiPAP/NIV → hỗ trợ xâm nhập: mô tả **mục tiêu sinh lý**, nơi dùng, bệnh cảnh có bằng chứng, giới hạn và monitoring.
- NIV:
  - COPD có toan hô hấp: bằng chứng mạnh, phải đánh giá đáp ứng sớm.
  - Phù phổi cấp do tim: CPAP hoặc BiPAP/NIV có bằng chứng.
  - Suy hô hấp giảm oxy mới xuất hiện: không trình bày NIV như mặc định; HFNO là lựa chọn có bằng chứng tốt hơn oxy thường ở population phù hợp.
- Box “Không thử NIV/HFNO kéo dài” khi mất bảo vệ đường thở, ngừng thở, sốc/loạn nhịp đe dọa, tiết đàm không kiểm soát, kích động không hợp tác, xấu đi nhanh hoặc không thể đặt nội khí quản khẩn tại nơi đang điều trị.
- Mermaid flowchart 2: lựa chọn hỗ trợ hô hấp và điểm đánh giá lại.

### 5. Chẩn đoán nguyên nhân theo pattern, nguy hiểm trước [CỐT LÕI]

Chia thành 5 nhánh để tránh danh sách dài rời rạc:

1. **Tắc nghẽn:** hen/COPD, tắc nghẽn đường thở trên, tràn khí màng phổi áp lực.
2. **Nhu mô phổi:** viêm phổi, ARDS, hít sặc.
3. **Tim mạch/màng phổi:** phù phổi cấp, PE, chèn ép tim, tràn dịch màng phổi.
4. **Chuyển hóa/huyết học/độc chất:** toan chuyển hóa, thiếu máu nặng, salicylate/opioid, DKA.
5. **Không bỏ sót:** ACS, sepsis, lo âu chỉ là chẩn đoán loại trừ khi không có red flag.

- Đặt các gói xét nghiệm theo câu hỏi lâm sàng, không phải “panel cho mọi người”: ECG, X-quang; POCUS tim-phổi tích hợp nếu có người thành thạo; BNP để hỗ trợ loại trừ suy tim trong bối cảnh thích hợp; PE theo xác suất tiền test + pathway.
- Không tạo phác đồ kháng sinh, lợi tiểu, kháng đông hay tiêu sợi huyết chi tiết — link bài căn nguyên.

### 6. Nơi điều trị, chuyển ICU và chuyển tuyến [CỐT LÕI]

- Logic dựa trên trajectory: cần hỗ trợ hô hấp tăng dần, không cải thiện sau can thiệp đầu, suy cơ quan khác, tri giác/huyết động xấu, nhu cầu theo dõi liên tục.
- Checklist bàn giao SBAR: timeline, baseline hô hấp, oxygen device/FiO₂ và SpO₂, RR/công thở, khí máu, nghi nguyên nhân, điều trị đã làm, đáp ứng, giới hạn điều trị nếu có.

### 7. Sai lầm thường gặp [CỐT LÕI]

Tối thiểu 6 lỗi có hậu quả và cách tránh:

- Đợi kết quả X-quang/CT rồi mới oxy hóa–thông khí.
- Đánh giá mức độ nặng bằng SpO₂ đơn lẻ, bỏ qua kiệt sức và tăng CO₂.
- Cho oxy tự do không đặt target ở người nguy cơ tăng CO₂.
- Dùng NIV ở người cần kiểm soát đường thở hoặc kéo dài thử khi không đáp ứng.
- Chẩn đoán “COPD/hen quen thuộc” rồi bỏ sót phù phổi, PE, tràn khí áp lực hoặc sepsis.
- Không ghi xu hướng và không xác định thời điểm đánh giá lại/điểm thất bại.

### 8. Áp dụng tại Việt Nam [CỐT LÕI]

- Phân tầng theo nơi có/không có ABG, HFNO, NIV và ICU.
- Nhấn mạnh gọi hỗ trợ, xử trí trong khi chuyển, và bàn giao có cấu trúc.
- Chỉ ghi thuốc, thiết bị hay protocol địa phương sau khi xác minh availability và văn bản.

### 9. Ca lâm sàng [NÂNG CAO]

1. COPD nghi đợt cấp: buồn ngủ, SpO₂ thấp, tăng CO₂/toan — chọn oxy mục tiêu, khí máu, NIV và mốc thất bại.
2. Phù phổi cấp do tim: tăng HA, orthopnea, ran ẩm/B-lines — hỗ trợ hô hấp song song với điều trị nguyên nhân, phân biệt sốc tim.
3. Viêm phổi giảm oxy máu nặng: HFNO và đánh giá lại; tránh trì hoãn ICU/intubation.
4. Khó thở kèm đau ngực/choáng: PE hoặc tràn khí áp lực — ưu tiên can thiệp và pathway chẩn đoán.

### 10. Tổng kết — 10 điểm cần nhớ và tự kiểm tra

- 10 “take-home points” thiên về hành động.
- 3 câu tích hợp cuối bài, trong đó ít nhất một ca buộc chọn hỗ trợ hô hấp và nơi điều trị.

### 11. Tài liệu tham khảo

- Guideline trước; review nền và RCT/meta-analysis tiếp sau.
- Mọi reference có PMID thật và annotation tag chuẩn.

---

## 4. Kế hoạch Anki

**Mục tiêu:** khoảng 32–40 cards V2; ưu tiên các decision node hơn định nghĩa thuộc lòng.

- 6–8 cards red flags và ABCDE.
- 6–8 cards oxy/SpO₂/khí máu, gồm ít nhất 2 cloze về target và giới hạn VBG.
- 8–10 cards chọn HFNO/CPAP-BiPAP/NIV, chống chỉ định và failure/escalation.
- 6–8 cards pattern chẩn đoán phân biệt, POCUS/ECG/X-ray theo câu hỏi.
- 4–6 mini-case cards về COPD tăng CO₂, phù phổi cấp, viêm phổi giảm oxy, PE/tràn khí.

Mỗi card chỉ bảo vệ một quyết định quan sát được. Không đưa một “protocol card” có liều hoặc ngưỡng chưa được `[FULL VERIFIED]`.

Deck đích: `Internal medicine::Acute_Dyspnea::YYYY-MM-DD` do `build_apkg.py` tự nhận diện từ đường dẫn `11_Noi khoa`.

---

## 5. Trình tự execute

1. Tạo folder `11_Noi khoa/IM-07_Kho_tho_cap_suy_ho_hap/` và copy cấu trúc tên file không dấu, có ngày build.
2. Cập nhật guideline registry với SFMU/SRLF 2026, AARC 2022, BTS oxygen, ERS/ATS NIV, ESICM 2023; không sửa registry trước khi các version/link/PMID được kiểm chứng lại.
3. Chạy Tier 0 web và BioMCP theo 6 bước, nhưng chia truy vấn theo 4 câu hỏi: triage/diagnosis, oxygen target, HFNO, NIV. Fetch sâu 5–8 paper/guideline chọn lọc.
4. Viết `RESEARCH_BRIEF.md` chứa claims được phép dùng, claims/số liệu cấm dùng, nền sinh lý có nguồn, và dàn ý trên.
5. Viết MD từ brief; mỗi protocol detail có nguồn sát bên.
6. Tạo `cards.v2.json`, build APKG, kiểm tra deck và dấu tiếng Việt.
7. Chạy bắt buộc: `verify_all_pmids.py`, `verify_claims.py`, retraction check, `citation_audit.py` (0 BLOCK), `verify_diacritics.py`, `verify_apkg_diacritics.py` (≥80%).
8. Chạy `make_knowledge_check.py`; tạo knowledge check, answer key, score file.
9. Khi mọi gate đạt: cập nhật `11_Noi khoa/README.md`, curriculum IM-07 thành ✅, `_README.md`, và `LESSON_BACKLOG.md` để loại trạng thái trống.

---

## 6. Tiêu chí nghiệm thu

- Người học có thể hoàn thành đúng một flow từ cửa cấp cứu đến “theo dõi / ICU / đặt nội khí quản” ở bốn ca trọng tâm.
- Hai flowchart Mermaid render được: ABCDE/triage và lựa chọn hỗ trợ hô hấp/escalation.
- Không có thuốc, liều, lưu lượng, ngưỡng hoặc timeline protocol nào không có nguồn đã verify.
- Không trùng scope phác đồ đầy đủ của IM-29–34 và IM-22; mọi nội dung nguyên nhân chỉ có “recognize → initial action → hand-off/link”.
- MD, cards và APKG đều nằm cùng folder IM-07; content tiếng Việt có dấu, filename không dấu.
- Citation audit có **0 BLOCK**; PMID/claim/retraction gates pass; diacritics MD/APKG đạt ngưỡng project.
- Knowledge check sinh từ cards, có ít nhất một mini-case về failure/escalation.

---

## 7. Rủi ro cần kiểm soát

- **Rủi ro nguy hiểm nhất:** “gộp tất cả khó thở thành một protocol cố định”. Giải pháp: mọi flow phải bắt đầu từ stability và physiology, sau đó tách theo phenotype/căn nguyên.
- **Rủi ro thứ hai:** cho cảm giác NIV/HFNO thay thế được đặt nội khí quản. Giải pháp: boxed failure criteria và reassessment loop ở cả MD/cards/cases.
- **Rủi ro evidence:** guideline cũ hơn về NIV/oxygen vẫn có giá trị nhưng phải kiểm tra update; guideline 2026 chỉ phủ assessment, không dùng để suy ra protocol thông khí.
- **Rủi ro registry/script:** registry hiện thiên OB/GYN và preflight match sai topic nội khoa; xác minh thực tế trên source trước, không tin match tự động.
