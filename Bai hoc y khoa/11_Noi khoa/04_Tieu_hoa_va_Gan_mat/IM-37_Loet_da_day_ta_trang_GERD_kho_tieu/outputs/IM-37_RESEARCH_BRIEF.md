# RESEARCH BRIEF: Bệnh loét dạ dày–tá tràng, GERD và khó tiêu
**Ngày:** 2026-07-20 | **Model research:** 9router/ocg/deepseek-v4-pro | **Model execute:** 9router/ocg/deepseek-v4-pro

---

## 1. Papers đã chọn (kèm lý do chọn)

| # | PMID | Loại | Tại sao chọn |
|---|---|---|---|---|
| 1 | 39626064 | Guideline | ACG 2024 — guideline hiện hành thay thế ACG 2017 về điều trị H. pylori; GRADE với 11 PICO + 6 key concepts; khuyến cáo BQT cho treatment-naive |
| 2 | 36714104 | Consensus | VNAGE 2022 — đường đi thực hành Việt Nam; quy định ngưỡng nội soi ≥35F/≥40M; phác đồ PTMB/PALB; kháng thuốc tại chỗ; 32 chuyên gia từ 14 trường/viện |
| 3 | 34807007 | Guideline | ACG GERD 2022 — toàn văn PMC; định nghĩa, PPI trial 8 tuần, chẩn đoán, trào ngược kháng trị, ngoài thực quản, phẫu thuật/nội soi |
| 4 | 28631728 | Guideline | ACG/CAG Dyspepsia 2017 — ngưỡng ≥60 tuổi để nội soi; test-and-treat H. pylori cho <60 tuổi không alarm; so sánh quốc tế |
| 5 | 33191311 | Guideline | Korean Drug-related PUD 2020 — toàn văn PMC; 9 statements về NSAID/aspirin/antiplatelet/anticoagulant; RR H. pylori eradication = 0.54; PPI cho NSAID giảm PU 54-76% |
| 6 | 33929377 | Guideline | ACG UGIB 2021 — dùng làm tài liệu ranh giới với IM-16/IM-36; GBS 0-1, Hb 7 g/dL, nội soi <24h; không dùng để tạo protocol chảy máu |
| 7 | 40337979 | Meta-analysis | Cochrane 2025 — 12 RCTs, n=8760; PPI giảm incident ulcer RR 0.29 (0.23-0.36), moderate certainty |
| 8 | 38173155 | Review | Refractory GERD 2024 — PMC; phân biệt unproven vs proven GERD; Lyon consensus; impedance-pH monitoring |
| 9 | 29990487 | Meta-analysis | H. pylori resistance global 2018 — 836 citations; dữ liệu kháng thuốc nền cho VNAGE; WHO high-priority designation |
| 10 | 26187502 | Consensus | Kyoto global consensus 2015 — 1707 citations; H. pylori gastritis = infectious disease; cơ sở cho chỉ định điều trị |
| 11 | 30338390 | Review | Functional dyspepsia 2018 — Rome IV; PPI/prokinetics/neuromodulators; cập nhật chẩn đoán và điều trị FD |

**Đã loại:**
- ACG H. pylori 2017 (PMID 28071660): đã bị ACG 2024 (39626064) thay thế hoàn toàn.
- Các paper về phẫu thuật chống trào ngược chuyên sâu, nội soi can thiệp GERD, IBD, xuất huyết tiêu hóa điều trị: ngoài phạm vi IM-37.
- Các guideline riêng về loét tiêu hóa chảy máu: thuộc IM-16/IM-36.

---

## 2. Claims đã verify — chỉ viết claim CÓ trong abstract/fulltext

Đây là phần QUAN TRỌNG NHẤT. Model execute CHỈ được dùng claim trong bảng này.
KHÔNG được thêm số liệu, KHÔNG được suy diễn.

### A. H. pylori — chẩn đoán và điều trị

| # | Claim | PMID | Tag |
|---|---|---|---|---|
| 1 | Chỉ xét nghiệm H. pylori khi có ý định điều trị tiệt trừ | 36714104 | [FULL VERIFIED] |
| 2 | Khó tiêu chưa điều tra, nữ ≥35t hoặc nam ≥40t hoặc có triệu chứng báo động → nội soi đường tiêu hóa trên + xét nghiệm dựa trên sinh thiết | 36714104 | [FULL VERIFIED] |
| 3 | RUT (rapid urease test) là xét nghiệm được chọn khi nội soi | 36714104 | [FULL VERIFIED] |
| 4 | UBT (urea breath test) là lựa chọn đầu tay trong xét nghiệm không xâm lấn (Sn 96%, Sp 93%) | 36714104 | [FULL VERIFIED] |
| 5 | Ngừng kháng sinh/bismuth ≥4 tuần, PPI ≥2 tuần trước khi xét nghiệm H. pylori | 36714104 | [FULL VERIFIED] |
| 6 | Xét nghiệm huyết thanh không được dùng để chẩn đoán nhiễm H. pylori đang hoạt động hoặc xác nhận tiệt trừ | 36714104 | [FULL VERIFIED] |
| 7 | Trong XHTH cấp, RUT và mô bệnh học có thể âm tính giả → xác nhận bằng test khác sau khi ổn định | 36714104 | [FULL VERIFIED] |
| 8 | Tỉ lệ kháng clarithromycin nguyên phát tại Việt Nam: 34.1%; metronidazole: 69.4% | 36714104 | [FULL VERIFIED] |
| 9 | Tỉ lệ kháng tetracycline còn thấp và ổn định; kháng amoxicillin và levofloxacin đang tăng | 36714104 | [FULL VERIFIED] |
| 10 | Thời gian tối ưu cho mọi phác đồ tiệt trừ H. pylori: 14 ngày | 36714104 | [FULL VERIFIED] |
| 11 | Phác đồ đầu tay: PTMB (PPI + Tetracycline + Metronidazole + Bismuth) | 36714104 | [FULL VERIFIED] |
| 12 | Phác đồ thay thế đầu tay: PALB (PPI + Amoxicillin + Levofloxacin + Bismuth) | 36714104 | [FULL VERIFIED] |
| 13 | Không dùng phác đồ ba thuốc chứa clarithromycin do tỉ lệ thất bại cao (tỉ lệ kháng 34.1%) | 36714104 | [FULL VERIFIED] |
| 14 | Phác đồ bậc hai: PTMB nếu chưa dùng; PALB nếu đã dùng PTMB | 36714104 | [FULL VERIFIED] |
| 15 | Sau hai lần thất bại: PTMB nếu chưa dùng; nếu đã dùng PTMB → kháng sinh đồ | 36714104 | [FULL VERIFIED] |
| 16 | Không dùng rifabutin tại Việt Nam do tình hình lao kháng thuốc phức tạp | 36714104 | [FULL VERIFIED] |
| 17 | UBT là test được chọn để xác nhận tiệt trừ (test-of-cure), thực hiện sau khi kết thúc điều trị | 36714104 | [FULL VERIFIED] |
| 18 | Tái nhiễm và tái phát H. pylori phổ biến tại Việt Nam | 36714104 | [FULL VERIFIED] |
| 19 | Không tuân thủ điều trị làm giảm tỉ lệ tiệt trừ >25% | 36714104 | [FULL VERIFIED] |
| 20 | Phác đồ được coi là hiệu quả khi tỉ lệ tiệt trừ ≥80% (intention-to-treat) | 36714104 | [FULL VERIFIED] |
| 21 | Liều PTMB: PPI liều chuẩn ×2/ngày + Tetracycline 500mg ×4/ngày + Metronidazole 500mg ×3/ngày + Bismuth (subcitrate 240mg hoặc subsalicylate 524mg) ×2-4/ngày, trong 14 ngày | 36714104 | [FULL VERIFIED] |
| 22 | Liều PALB: PPI liều chuẩn ×2/ngày + Amoxicillin 1000mg ×2/ngày + Levofloxacin 500mg ×2/ngày + Bismuth (như trên), trong 14 ngày | 36714104 | [FULL VERIFIED] |
| 23 | Metronidazole ≥1500 mg/ngày khi dùng trong phác đồ bốn thuốc chứa bismuth để vượt qua kháng thuốc | 36714104 | [FULL VERIFIED] |
| 24 | PPI (esomeprazole, rabeprazole) thế hệ mới cho tỉ lệ tiệt trừ tốt hơn PPI thế hệ đầu (omeprazole, lansoprazole, pantoprazole) do không bị ảnh hưởng bởi CYP-2C19 | 36714104 | [FULL VERIFIED] |

### B. Khó tiêu — chẩn đoán và phân tầng

| # | Claim | PMID | Tag |
|---|---|---|---|---|
| 25 | Bệnh nhân ≥60 tuổi có khó tiêu → nội soi đường tiêu hóa trên (khuyến cáo có điều kiện) | 28631728 | [ABSTRACT VERIFIED] |
| 26 | Bệnh nhân <60 tuổi không có alarm → test-and-treat H. pylori không xâm lấn (khuyến cáo) | 28631728 | [ABSTRACT VERIFIED] |
| 27 | Người có nguy cơ ung thư dạ dày cao hơn (sống thời thơ ấu ở nước có nguy cơ cao, tiền sử gia đình) → nội soi ở tuổi trẻ hơn | 28631728 | [ABSTRACT VERIFIED] |

### C. GERD — chẩn đoán và điều trị

| # | Claim | PMID | Tag |
|---|---|---|---|---|
| 28 | GERD điển hình (ợ nóng + trào ngược) không có triệu chứng báo động: PPI thử nghiệm 8 tuần, 1 lần/ngày trước bữa ăn (Khuyến cáo mạnh, mức chứng cứ trung bình) | 34807007 | [FULL VERIFIED] |
| 29 | Cố gắng ngừng PPI nếu triệu chứng GERD điển hình đáp ứng với thử nghiệm 8 tuần (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 30 | Nội soi chẩn đoán sau khi ngừng PPI 2-4 tuần nếu không đáp ứng đầy đủ với PPI 8 tuần hoặc triệu chứng tái phát (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 31 | Đau ngực không kèm ợ nóng sau khi đã loại trừ bệnh tim: xét nghiệm khách quan GERD (nội soi và/hoặc reflux monitoring) (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 32 | Nội soi là xét nghiệm đầu tiên cho bệnh nhân có nuốt khó hoặc triệu chứng báo động (sụt cân, XHTH) (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 33 | Reflux monitoring off therapy để xác lập chẩn đoán khi nghi GERD chưa rõ và nội soi không có bằng chứng GERD (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 34 | Giảm cân ở bệnh nhân thừa cân/béo phì để cải thiện triệu chứng GERD (Khuyến cáo mạnh, mức chứng cứ trung bình) | 34807007 | [FULL VERIFIED] |
| 35 | Tránh ăn trong vòng 2-3 giờ trước khi đi ngủ (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 36 | PPI uống 30-60 phút trước bữa ăn, không uống trước khi đi ngủ (Khuyến cáo mạnh, mức chứng cứ trung bình) | 34807007 | [FULL VERIFIED] |
| 37 | PPI liều thấp nhất có hiệu quả cho điều trị duy trì GERD (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 38 | Không thêm thường quy các liệu pháp khác ở bệnh nhân không đáp ứng PPI (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 39 | PPI duy trì vô thời hạn hoặc phẫu thuật chống trào ngược cho LA grade C hoặc D (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 40 | Không dùng baclofen nếu không có bằng chứng khách quan của GERD (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 41 | Không dùng prokinetic cho GERD trừ khi có bằng chứng khách quan của liệt dạ dày (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 42 | Đánh giá nguyên nhân không phải GERD trước khi quy triệu chứng ngoài thực quản cho GERD (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 43 | Bệnh nhân có triệu chứng ngoài thực quản mà không có triệu chứng GERD điển hình: reflux testing trước khi dùng PPI (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |
| 44 | Bệnh nhân có cả triệu chứng ngoài thực quản và điển hình: cân nhắc PPI 2 lần/ngày trong 8-12 tuần trước xét nghiệm thêm (Khuyến cáo có điều kiện) | 34807007 | [FULL VERIFIED] |
| 45 | Tối ưu hóa PPI là bước đầu tiên trong xử trí GERD kháng trị (Khuyến cáo mạnh) | 34807007 | [FULL VERIFIED] |

### D. Loét do thuốc — dự phòng

| # | Claim | PMID | Tag |
|---|---|---|---|---|
| 46 | Yếu tố nguy cơ loét do NSAID: tuổi cao, tiền sử loét, NSAID liều cao, dùng kèm aspirin/antiplatelet/steroid | 33191311 | [FULL VERIFIED] |
| 47 | Diệt H. pylori làm giảm loét liên quan NSAID: RR 0.54 (95% CI 0.31-0.94); hiệu quả hơn ở người chưa từng dùng NSAID (RR 0.27, 95% CI 0.14-0.53) | 33191311 | [FULL VERIFIED] |
| 48 | PPI liều thấp cho bệnh nhân nguy cơ cao dùng NSAID dài hạn: giảm nguy cơ loét 54-76% (pooled RR 0.29 ở <12 tuần, 0.46 ở 12-24 tuần, 0.23 ở ≥24 tuần) | 33191311 | [FULL VERIFIED] |
| 49 | PPI + aspirin làm giảm loét tái phát: HR 0.17 (95% CI 0.12-0.25), NNT 7.7 | 33191311 | [FULL VERIFIED] |
| 50 | PPI cho bệnh nhân dùng warfarin nguy cơ cao: giảm XHTH trên RR 0.56 (95% CI 0.38-0.83) | 33191311 | [FULL VERIFIED] |
| 51 | PPI giảm incident ulcer so với placebo ở người dùng NSAID: RR 0.29 (95% CI 0.23-0.36), moderate certainty (Cochrane 2025, 12 RCTs, n=8760) | 40337979 | [ABSTRACT VERIFIED] |

### E. GERD kháng trị và khó tiêu chức năng (bổ sung)

| # | Claim | PMID | Tag |
|---|---|---|---|---|
| 52 | Triệu chứng dai dẳng dù đã dùng PPI thường bị gán nhãn sai là GERD kháng trị; cần phân biệt unproven GERD vs proven GERD | 38173155 | [ABSTRACT VERIFIED] |
| 53 | GERD chưa được chứng minh (unproven): xét nghiệm off PPI để tìm bằng chứng khách quan theo Lyon consensus | 38173155 | [ABSTRACT VERIFIED] |
| 54 | H. pylori gastritis được Kyoto consensus định nghĩa là bệnh nhiễm trùng; nên điều trị tiệt trừ trước khi tổn thương tiền ung thư phát triển | 26187502 | [ABSTRACT VERIFIED] |
| 55 | WHO xếp H. pylori kháng clarithromycin là ưu tiên cao cho nghiên cứu và phát triển kháng sinh (2017); tỉ lệ kháng ≥15% ở hầu hết khu vực WHO | 29990487 | [ABSTRACT VERIFIED] |

**Số liệu CẤM dùng (không có nguồn xác minh hoặc ngoài phạm vi bài):**
- Hiệu quả định lượng của từng PPI riêng lẻ (esomeprazole vs omeprazole vs rabeprazole) — chỉ có qualitative statement trong fulltext
- Số liệu dịch tễ H. pylori chính xác theo tỉnh/thành tại Việt Nam
- Tỉ lệ tái phát GERD định lượng sau ngừng PPI
- Ngưỡng tuổi nội soi của các nước châu Á khác ngoài Việt Nam
- Phác đồ kinh nghiệm khi chưa có kết quả kháng sinh đồ — phải chuyển tuyến hoặc hội chẩn

---

## 3. Kiến thức nền — anatomy/physiology (có nguồn textbook)

| # | Kiến thức | Nguồn |
|---|---|---|
| 1 | Dạ dày có 3 vùng chức năng: tâm vị (cardia), thân vị (fundus/body — tiết acid, pepsinogen), hang vị (antrum — tiết gastrin). Niêm mạc dạ dày được bảo vệ bởi lớp nhầy, bicarbonate, prostaglandin và dòng máu niêm mạc. | [TEXTBOOK: Harrison's Principles of Internal Medicine 21e, Ch. 314] |
| 2 | H. pylori là trực khuẩn Gram âm, hình xoắn, có urease (chuyển urea → NH₃ + CO₂ để sống trong môi trường acid). Nhiễm gây viêm dạ dày mạn → teo niêm mạc → dị sản ruột → loạn sản → ung thư (chuỗi Correa). | [REVIEW: PMID 26187502; TEXTBOOK: Harrison's 21e, Ch. 159] |
| 3 | Cơ thắt thực quản dưới (LES) + trụ hoành tạo hàng rào chống trào ngược. GERD xảy ra khi: (1) giãn LES thoáng qua không do nuốt (TLESR), (2) LES yếu, (3) thoát vị hoành, (4) giảm thanh thải thực quản, (5) chậm làm rỗng dạ dày. | [GUIDELINE BACKGROUND: PMID 34807007] |
| 4 | NSAID ức chế COX-1 → giảm prostaglandin niêm mạc → giảm lớp nhầy, giảm bicarbonate, giảm dòng máu niêm mạc → tổn thương niêm mạc → loét. Aspirin còn có tác dụng tại chỗ (tính acid yếu → bắt giữ ion trong tế bào niêm mạc). | [TEXTBOOK: Goodman & Gilman's 14e, Ch. 42] |
| 5 | PPI (proton pump inhibitor) gắn không hồi phục vào H⁺/K⁺-ATPase ở tế bào thành, chỉ tác dụng lên bơm đang hoạt động → phải uống trước bữa ăn 30-60 phút. | [GUIDELINE BACKGROUND: PMID 34807007] |

---

## 4. Dàn ý chi tiết (KHÔNG phải tiêu đề suông)

### Section 0: TỔNG QUAN (đầu bài, sau metadata)
- Vấn đề lâm sàng: Ba hội chứng thường gặp nhất ở phòng khám tiêu hóa — khó tiêu, loét dạ dày–tá tràng, GERD — cùng chia sẻ cơ chế acid và H. pylori nhưng đường đi chẩn đoán và điều trị khác biệt.
- Mục tiêu: (1) Phân biệt ba hội chứng; (2) BOX ĐỎ phân luồng cấp cứu; (3) Áp dụng test-and-treat H. pylori theo VNAGE; (4) Chọn phác đồ tiệt trừ dựa trên kháng thuốc; (5) Xử trí GERD từ thử nghiệm PPI đến kháng trị; (6) Quản lý nguy cơ loét do thuốc.
- Scope box: Liệt kê các bài liên quan IM-16/IM-35/IM-36/IM-38/IM-40/IM-42 (đường dẫn tương đối), nêu ranh giới sở hữu của IM-37.

### Section 1: ĐỊNH NGHĨA [CỐT LÕI]
- **1.0 Nhắc nhanh:** acid/prostaglandin/H. pylori/LES → bình thường và hỏng [kiến thức nền #1, #2, #3]
- **1.1 Khó tiêu (Dyspepsia):** Rome IV; uninvestigated vs functional [claims #25, #26]
- **1.2 Loét dạ dày–tá tràng (PUD):** Ổ loét qua lớp cơ niêm; nguyên nhân: H. pylori, NSAID [claims #1, #46]
- **1.3 GERD:** Trào ngược → triệu chứng/biến chứng; điển hình vs ngoài thực quản [claim #28]
- ⚠️ HỌC VIÊN HAY NHẦM: "Ợ nóng = GERD = cần PPI"

### Section 2: CƠ CHẾ BỆNH SINH [CỐT LÕI]
- Chuỗi Correa (H. pylori → ung thư) [kiến thức nền #2]
- Mất cân bằng tấn công/bảo vệ trong PUD [kiến thức nền #1, #4]
- Sinh lý bệnh GERD (TLESR, LES, thoát vị) [kiến thức nền #3]
- Cơ chế PPI [kiến thức nền #5]

### Section 3: CHẨN ĐOÁN [CỐT LÕI]
- **BOX ĐỎ** (TRƯỚC chẩn đoán thường quy, dạng bảng: dấu hiệu → nguy cơ → hành động ngay → nơi đến): sốc/hematemesis/melena (IM-16→IM-36); phúc mạc/thủng (IM-35); nuốt khó/sụt cân/thiếu máu (nội soi ngay); tắc ruột (IM-35); đau kiểu tụy/mật (IM-42)
- **3.1 Khó tiêu chưa điều tra:** Ngưỡng VNAGE: nữ ≥35t, nam ≥40t hoặc alarm → nội soi + RUT [claims #2, #3]; bảng so sánh ACG/CAG ≥60t [claim #25]
- **3.2 Xét nghiệm H. pylori:** UBT đầu tay không xâm lấn [claim #4]; RUT khi nội soi [claim #3]; chuẩn bị [claim #5]; huyết thanh học không dùng [claim #6]; XHTH cấp gây âm tính giả [claim #7]
- **3.3 Chẩn đoán GERD:** PPI thử nghiệm 8 tuần [claim #28]; nội soi nếu không đáp ứng [claim #30]; nội soi đầu tay nếu alarm [claim #32]; reflux monitoring khi chưa rõ [claim #33]

### Section 4: ĐIỀU TRỊ [CỐT LÕI]
- **4.1 H. pylori (VNAGE 2022 — authoritative):** Nguyên tắc ≥80% ITT [claim #20]; 14 ngày [claim #10]; tuân thủ [claim #19]; Đầu tay PTMB [claims #11, #21]; PALB [claims #12, #22]; metronidazole ≥1500mg/ngày [claim #23]; ưu tiên PPI thế hệ mới [claim #24]; Không clarithromycin [claim #13]; Bậc hai [claim #14]; Cứu vãn [claim #15]; Không rifabutin [claim #16]; Test-of-cure [claim #17]; Nội soi nếu loét dạ dày/nghi ác tính
- **4.2 GERD:** PPI 8 tuần [claim #28]; ngừng nếu đáp ứng [claim #29]; Lối sống [claims #34, #35, #36]; Duy trì [claims #37, #39]; Không đáp ứng [claims #38, #45]; Kháng trị [claims #52, #53]; Ngoài thực quản [claims #42, #43, #44]; Không baclofen/prokinetic [claims #40, #41]
- **4.3 Loét do thuốc:** Yếu tố nguy cơ [claim #46]; H. pylori eradication [claim #47]; PPI dự phòng [claims #48, #51]; Aspirin [claim #49]; Warfarin [claim #50]; Phối hợp CV risk
- **4.4 Khó tiêu chức năng:** Test-and-treat H. pylori trước; PPI, prokinetic, neuromodulator; review FD [PMID 30338390]

### Section 5: THEO DÕI [CỐT LÕI]
- Test-of-cure: UBT sau kết thúc điều trị, tuân thủ quy tắc ngừng thuốc [claim #17]
- Nội soi lại: loét dạ dày + sinh thiết; tổn thương tiền ung thư; Barrett
- GERD: step-down; theo dõi LA grade
- Thuốc: đánh giá lại chỉ định NSAID/aspirin; tác dụng phụ PPI dài hạn

### Section 6: LƯU ĐỒ QUYẾT ĐỊNH [CỐT LÕI]
Mermaid flowchart với cấu trúc:
```
Triệu chứng tiêu hóa trên
→ Emergency/bleeding/perforation/obstruction? → YES: IM-16/35/36 links
→ NO: Red flags (dysphagia, weight loss, anemia, vomiting)? → YES: Urgent endoscopy
→ NO: Syndrome classification
  → Classic heartburn/regurgitation: GERD branch → PPI trial 8 weeks
  → Dyspepsia/epigastric: Dyspepsia/PUD branch → Vietnam endoscopy threshold → UBT → PTMB/PALB → Test-of-cure
  → Non-cardiac chest pain: Objective testing
  → Isolated extraesophageal: Non-GERD evaluation → Reflux testing
→ Plan B: Document phenotype + medication history; UBT if available; PPI trial; refer if endoscopy/reflux monitoring needed
```
Dịch sang văn xuôi đánh số ngay dưới Mermaid.

### Section 7: SAI LẦM THƯỜNG GẶP [CỐT LÕI] (bảng 8 dòng)
1. Kê PPI trước phân tầng → che lấp ác tính, âm tính giả H. pylori
2. Dùng clarithromycin theo thói quen → tỉ lệ kháng 34.1% tại VN [claim #8] → dùng PTMB/PALB
3. Không ngừng PPI trước test H. pylori → âm tính giả → ngừng PPI ≥2 tuần [claim #5]
4. Gán nhãn GERD cho mọi ợ nóng → bỏ sót bệnh tim, co thắt thực quản
5. Quy ho/mất tiếng/hen cho GERD không bằng chứng → đánh giá non-GERD trước [claim #42]
6. Không test-of-cure sau điều trị H. pylori → không biết thất bại → UBT [claim #17]
7. Tiếp tục NSAID không bảo vệ dạ dày ở người nguy cơ cao → PPI dự phòng [claim #48]
8. Không nội soi loét dạ dày để loại trừ ác tính → sinh thiết mọi loét dạ dày

### Section 8: CASE LÂM SÀNG [NÂNG CAO] (4 cases, 5 bước mỗi case)
1. Nữ 32t, đau thượng vị không alarm → UBT → PTMB 14 ngày; nhấn mạnh tuân thủ + test-of-cure
2. Nam 55t, dùng ibuprofen, đau thượng vị → test H. pylori + PPI + đánh giá ngừng/đổi NSAID
3. Nam 40t, ợ nóng+trào ngược điển hình → PPI 8 tuần; hai kịch bản: đáp ứng (step-down) / không đáp ứng (nội soi)
4. Nam 50t, đau thượng vị + sụt cân + nuốt khó → RED FLAG → nội soi ngay, không test-and-treat

### Section 9: TIPS THỰC HÀNH [THAM KHẢO] (8 tips)
1. Tư vấn tuân thủ + giải thích tác dụng phụ trước khi kê phác đồ tiệt trừ
2. Luôn hỏi "Đã dùng kháng sinh gì trong 4 tuần qua?" trước test H. pylori
3. Nhắc bệnh nhân ngừng PPI 2 tuần trước UBT/test-of-cure
4. Ghi chú "UBT sau điều trị" ngay khi kê đơn — không để quên test-of-cure
5. Cảnh báo tương tác rượu–metronidazole (buồn nôn, nôn, đau đầu, đỏ bừng mặt)
6. Trong mọi BN đau thượng vị: ghi alarm (sụt cân? nuốt khó? thiếu máu? nôn?)
7. Trong mọi BN ≥40 tuổi dùng NSAID/aspirin dài hạn: đánh giá nguy cơ loét + PPI dự phòng nếu cần
8. GERD: kê PPI trước ăn 30-60 phút, không phải trước ngủ; tư vấn giảm cân + tránh ăn khuya

### Section 10: TỔNG KẾT [CỐT LÕI] (10 điểm vàng + checklist tự kiểm tra cuối bài)
Rút từ tất cả claims + sai lầm + cases.

---

## 5. Hướng dẫn cho model execute

```
Bạn là model execute. Nhiệm vụ: viết bài MD hoàn chỉnh từ brief này.

QUY TẮC CỨNG:
1. CHỈ dùng claims trong bảng "Claims đã verify" — KHÔNG thêm claim mới
2. CHỈ dùng số liệu có tag [FULL VERIFIED] — nếu không có tag này, chỉ viết định tính
3. CHỈ dùng kiến thức nền có nguồn trong bảng "Kiến thức nền"
4. Với mỗi section, follow dàn ý chi tiết — thêm ví dụ, paraphrase, nhưng không thêm ý
5. Tiếng Việt có dấu đầy đủ. Thuật ngữ y khoa giữ tiếng Anh.
6. Thêm checkpoint (🛑) sau mỗi 2-3 section
7. Nếu không chắc chắn về 1 claim → bỏ claim đó, không bịa
8. Đường đi Việt Nam (VNAGE 2022) là authoritative; ACG/CAG ≥60 chỉ là so sánh quốc tế
9. BOX ĐỎ TRƯỚC chẩn đoán thường quy, không phải sau
10. Mermaid flowchart PHẢI có nhánh cấp cứu + Plan B/thiếu nguồn lực
11. Scope box với link tương đối đến IM-16, IM-35, IM-36, IM-38, IM-40, IM-42

OUTPUT: File MD hoàn chỉnh theo template_lesson.md, lưu tại:
11_Noi khoa/IM-37_Loet_da_day_ta_trang_GERD_kho_tieu/IM-37_Loet_da_day_ta_trang_GERD_kho_tieu_2026-07-20.md
```
