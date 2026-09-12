# BẢN ĐỒ NGUỒN VÀ RANH GIỚI TÀI LIỆU — IM-04 PART 2 VÀ PART 3
> **Chuyên đề**: IM-04 — Hướng dẫn đọc xét nghiệm máu cơ bản
> **Phân loại**: Block 0 — Nền tảng tư duy và an toàn lâm sàng (Profile `foundation`, Chế độ duy nhất `L3_BEGINNER`)
> **Ngày chuẩn hóa**: 2026-07-29
> **Phạm vi tài liệu**: Part 2 (Huyết học & Đông máu) và Part 3 (Sinh hóa & Tích hợp)
> **Trạng thái PubMed Preflight**: **Chưa sẵn sàng** (`NCBI_API_KEY` và `USER_EMAIL` thiếu trong `.env`).
> **Quy tắc kiểm định fail-closed**: Xây dựng chiến lược nguồn dựa trên Official Tier 0 Web & Local Evidence. Tuyệt đối **không tự gán nhãn verify** và **không sử dụng các nhãn deprecated**. Chỉ 5 nhãn canonical được phép xuất hiện sau khi qua pipeline kiểm định: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.

---

## I. TỔNG QUAN VÀ KHUNG TƯ DUY NGUỒN CHO PART 2 VÀ PART 3

Bản đồ nguồn này xác định chiến lược tài liệu, ranh giới chống dẫm chân bài chuyên sâu, danh mục claim candidates cần kiểm định và các cảnh báo an toàn lâm sàng cho Part 2 và Part 3 thuộc chuyên đề IM-04. File này đóng vai trò lập bản đồ định hướng, không phải bằng chứng phát hành (evidence release) và không thay thế cho Research Brief hay bài học.

### 1. Nguyên tắc tuân thủ pháp lý & PubMed Credentials
- **Trạng thái Preflight**: Không tự ý thực hiện cuộc gọi PubMed API / E-utilities trực tiếp do thiếu credentials trong môi trường.
- **Chiến lược nguồn**: Sử dụng chiến lược tra cứu tài liệu Tier 0 chính thức (Official Guidelines / Web / Standard Textbooks).
- **Phân loại PMID Candidates**: Toàn bộ PMID trong bản đồ này được ghi nhận rõ là **ứng viên chưa xác minh (unverified candidate)**. Chưa thực hiện canonical fetch hay trích xuất metadata/abstract chính thức do preflight chưa sẵn sàng.
- **Quy định về Local QA**: Các tài liệu QA sẵn có (`QA-XN-Dong-Mau_2026-07-20.md`, `QA-BUN_2026-07-20.md`) được dùng làm **tài liệu tham khảo định hướng tư duy**, KHÔNG được tính là evidence release chính thức khi chưa có manifest/hash kiểm định fail-closed tương ứng.

### 2. Phân định Ranh giới & Chống dẫm chân (Strict Cross-Reference Boundaries)

#### Part 2: Huyết học & Đông máu cơ bản
- **Phạm vi tập trung (In-Scope)**:
  - Tiếp cận nhận diện pattern công thức máu 3 dòng (CBC): Hồng cầu (RBC, Hb, Hct, MCV, MCH, RDW), Bạch cầu (WBC, Neutrophil, Lymphocyte, ANC, ALC, left shift), Tiểu cầu (PLT, MPV).
  - Tiếp cận bộ đông máu cơ bản: PT, INR, aPTT, Fibrinogen (Clauss).
  - Phân tầng nguy cơ cấp cứu, nhận diện mẫu xét nghiệm báo động (bệnh lý cấp tính vs nhiễu xét nghiệm).
- **Ranh giới cứng (Strict Out-of-Scope / Prohibited Overlap)**:
  - ❌ **IM-68 (Tiếp cận thiếu máu)**: Không đi sâu vào thuật toán nguyên nhân thiếu máu chuyên sâu, sắt/ferritin nâng cao, điện di Hb, tủy đồ.
  - ❌ **IM-69 (Giảm tiểu cầu & Rối loạn đông máu/DIC)**: Không đi sâu vào phác đồ điều trị ITP, TTP/HUS, tiêu chuẩn ISTH DIC chi tiết, phác đồ thay thế huyết tương hay bù yếu tố đông máu chuyên sâu.
  - ❌ **IM-70 (Bạch cầu tăng/giảm & Pancytopenia)**: Không đi sâu vào chẩn đoán bệnh lý huyết học ác tính (Bạch cầu cấp/mạn, Myelodysplastic Syndrome, Tủy suy), không đọc phết máu ngoại vi chi tiết.

#### Part 3: Sinh hóa cơ bản & Tích hợp lâm sàng
- **Phạm vi tập trung (In-Scope)**:
  - Điện giải cốt lõi (Na+, K+, Cl-), Chức năng thận (Creatinine, BUN, eGFR), Chức năng gan (AST, ALT, Bilirubin toàn phần/trực tiếp, Albumin), Đường huyết (Glucose ngẫu nhiên/đói, HbA1c), Chỉ số viêm (CRP, ESR), Chỉ số tim/nội tiết/vi chất mức sơ khởi (Troponin, TSH, Ferritin cơ bản).
  - **4 Ca tích hợp lâm sàng thực tế**: Phối hợp CBC + Sinh hóa + Đông máu để ra quyết định lâm sàng ban đầu tại giường bệnh.
- **Ranh giới cứng (Strict Out-of-Scope / Prohibited Overlap)**:
  - ❌ **IM-41 (Vàng da & XN gan chuyên sâu)**: Không đi sâu vào thuật toán phân biệt tổn thương tế bào gan vs ứ mật chuyên sâu, phác đồ viêm gan virus hay tự miễn.
  - ❌ **IM-43 (Creatinine, eGFR & Tiếp cận tổn thương thận cấp)**: Không lặp lại chi tiết công thức CKD-EPI, phân loại KDIGO AKI 3 giai đoạn hay tiêu chuẩn sinh thiết thận.
  - ❌ **IM-45 (Rối loạn Na)**: Không đi sâu vào phác đồ bù Na ưu trương trong SIADH, bù Natri cấp cứu, hội chứng hủy myelin cầu não (ODS).
  - ❌ **IM-46 (Rối loạn K)**: Không đi sâu vào phác đồ hạ Kali cấp cứu bằng Insulin-Glucose, Calci gluconate hay phác đồ bù K đường tĩnh mạch chuyên sâu.
  - ❌ **IM-47 (Toan kiềm & Khí máu)**: Không đi sâu vào phân tích khí máu động mạch (ABG/VBG), Delta Ratio, Winter formula hay rối loạn toan kiềm hỗn hợp.
  - ❌ **IM-51 (Đái tháo đường)**: Không đi sâu vào phác đồ chỉnh Insulin lâm sàng, phác đồ OADs hay quản lý biến chứng mạn.
  - ❌ **IM-52 (Cấp cứu đường huyết DKA/HHS)**: Không đi sâu vào phác đồ truyền Insulin bù dịch hồi sức DKA/HHS.

---

## II. PART 2 SOURCE MAP: HUYẾT HỌC & ĐÔNG MÁU CƠ BẢN

### 1. Nguồn Tier 0 Ưu tiên (Guidelines & Societies chính thức)

1. **BSH (British Society for Haematology)**:
   - Các hướng dẫn cập nhật của BSH về đọc công thức máu (FBC/CBC), xét nghiệm đông máu (clotting screen), antiphospholipid syndrome và lupus anticoagulant. *Tài liệu cụ thể sẽ được trích dẫn kèm Document ID và năm ban hành chính thức khi xây dựng Brief.*
2. **ICSH (International Council for Standardization in Haematology) & CLSI**:
   - Khuyến cáo của ICSH về khoảng tham chiếu và phân tích tế bào tự động.
   - Standard CLSI H21 về thu thập, vận chuyển và xử lý mẫu xét nghiệm đông máu.
3. **ASH (American Society of Hematology)**:
   - Clinical practice guidelines của ASH về tiếp cận giảm tiểu cầu và các ngưỡng chỉ số tế bào máu.
4. **WHO (World Health Organization)**:
   - Khuyến cáo của WHO về định ngưỡng Haemoglobin trong chẩn đoán và phân độ thiếu máu.

### 2. Các PMID Ứng viên (Ứng viên chưa xác minh — Cần Canonical Fetch sau)

*Lưu ý: Các PMID dưới đây là đối tượng tiềm năng cho chiến lược tra cứu, hoàn toàn chưa qua canonical fetch hay xác minh abstract/fulltext.*

- **PMID 34914193** — *Ứng viên chưa xác minh*: Review về tiếp cận đọc Full Blood Count trong thực hành lâm sàng.
- **PMID 32174066** — *Ứng viên chưa xác minh*: Đánh giá hiệu năng máy đếm tế bào tự động và cạm bẫy lâm sàng.
- **PMID 30588647** — *Ứng viên chưa xác minh*: Cạm bẫy tiền phân tích và phân tích trong xét nghiệm đông máu.
- **PMID 29424795** — *Ứng viên chưa xác minh*: Diễn giải con đường đông máu PT, INR, aPTT và Fibrinogen.

### 3. Tài liệu Tham khảo Định hướng Local (Local Guidance Notes)

- `Bai hoc y khoa/11_Noi khoa/XN-dong-mau-PT-aPTT-Fibrinogen/QA-XN-Dong-Mau_2026-07-20.md`:
  - *Giá trị định hướng*: Khung tư duy 4 pattern đông máu cơ bản, quy trình loại trừ nhiễu trước khi cân nhắc Mixing Study. *(Chỉ sử dụng làm gợi ý cấu trúc, không phải bằng chứng phát hành)*.

### 4. Các Hạng mục Claim Candidates (Cấm sử dụng khi chưa PASS exact quote / artifact)

*Tất cả các ngưỡng số dưới đây là **claim candidate — CẤM DÙNG trước khi exact quote / artifact PASS**.*

| Hạng mục Claim Candidate | Số liệu định hướng (Claim Candidate) | Yêu cầu Bằng chứng Bắt buộc | Note Kiểm định Fail-Closed |
|---|---|---|---|
| **Ngưỡng Hb báo động cấp cứu** | $Hb < 7.0 \text{ g/dL}$ (hoặc $< 8.0 \text{ g/dL}$ ở BN bệnh mạch vành cấp) *(Claim candidate)* | Guideline chính thức (AABB / BSH) | Bắt buộc exact quote về ngưỡng truyền máu bảo thủ (restrictive threshold). |
| **Bạch cầu Neutrophil & ANC** | $ANC < 0.5 \times 10^9/\text{L}$ ($500/\mu\text{L}$) = Giảm bạch cầu hạt nặng *(Claim candidate)* | Guideline / Consensus chính thức | Bắt buộc verify exact quote về nguy cơ nhiễm trùng cơ hội. |
| **Tiểu cầu & Ngưỡng xuất huyết** | $PLT < 10 \times 10^9/\text{L}$ (xuất huyết tự phát), $< 50 \times 10^9/\text{L}$ (thủ thuật) *(Claim candidate)* | Guideline ASH / BSH chính thức | Bắt buộc verify phân định xuất huyết tự phát vs thủ thuật xâm lấn. |
| **Fibrinogen Clauss** | $< 1.5 \text{ g/L}$ hoặc $< 1.0 \text{ g/L}$ *(Claim candidate)* | Guideline BSH / Hematology consensus | Bắt buộc exact quote phương pháp Clauss vs PT-derived. |
| **aPTT Kéo dài & Mixing Study** | Quy trình 3 bước: Tiền phân tích $\rightarrow$ Loại trừ thuốc $\rightarrow$ Mixing study 1:1 *(Claim candidate)* | Guideline BSH / Standard textbook | Cần bằng chứng tiêu chuẩn cho chỉ định Mixing study. |

### 5. Claims Nguy hiểm & Điều Cấm (Critical Safety Warnings for Part 2)

- 🚫 **CẤM gộp aPTT kéo dài là bắt buộc thiếu yếu tố chảy máu**: Lupus anticoagulant làm aPTT kéo dài trên labo nhưng lâm sàng lại nguy cơ tăng đông (tắc mạch), không phải chảy máu.
- 🚫 **CẤM đọc tiểu cầu giảm mà bỏ qua bẫy EDTA (Pseudothrombocytopenia)**: Phải kiểm tra phết máu ngoại vi hoặc làm lại ống Sodium Citrate/Heparin trước khi chẩn đoán giảm tiểu cầu thật sự hoặc chỉ định truyền tiểu cầu.
- 🚫 **CẤM bù Fibrinogen chỉ dựa trên số liệu đơn độc**: Không bù tủa lạnh/fibrinogen nếu BN không có xuất huyết lâm sàng hoặc chuẩn bị làm thủ thuật nguy cơ cao.
- 🚫 **CẤM bỏ qua bạch cầu giả giảm do kết tụ (Leukocyte aggregation) hoặc Neutrophil bám mạch (Margination)**.

---

## III. PART 3 SOURCE MAP: SINH HÓA VÀ TÍCH HỢP LÂM SÀNG

### 1. Nguồn Tier 0 Ưu tiên (Guidelines & Societies chính thức)

1. **ADLM (Association for Diagnostics & Laboratory Medicine - trước đây là AACC)**:
   - Tài liệu định hướng của ADLM về quản lý xét nghiệm điện giải, chức năng gan, thận và biomarkers tim (Troponin).
2. **KDIGO (Kidney Disease: Improving Global Outcomes)**:
   - Guideline của KDIGO về AKI và CKD đối với Creatinine và eGFR baseline. *(Lưu ý: Tỷ lệ BUN/Creatinine là chỉ số kinh điển hỗ trợ gợi ý phân loại trước thận/tại thận, KHÔNG phải là tiêu chuẩn định nghĩa chính thức của KDIGO).*
3. **EASL / AASLD (European/American Association for the Study of Liver)**:
   - Guidelines của EASL/AASLD về đánh giá bất thường xét nghiệm gan: phân lập tổn thương tế bào gan (AST/ALT) vs Cấu trúc đường mật (ALP, GGT, Bilirubin).
4. **ADA (American Diabetes Association)**:
   - ADA Standards of Care về tiêu chuẩn chẩn đoán Glucose và HbA1c, cùng các yếu tố nhiễu (bệnh lý hồng cầu, biến thể Hb).
5. **ESC / ACC / AHA (Cardiology Societies)**:
   - Consensus về Fourth Universal Definition of Myocardial Infarction: Đánh giá động học Troponin (hs-cTn). *(Lưu ý: Thay đổi delta Troponin phụ thuộc vào assay cụ thể và protocol 0h/1h hoặc 0h/2h/3h của từng labo, KHÔNG có con số delta >20% áp dụng cho mọi trường hợp).*

### 2. Các PMID Ứng viên (Ứng viên chưa xác minh — Cần Canonical Fetch sau)

*Lưu ý: Các PMID dưới đây là đối tượng tiềm năng cho chiến lược tra cứu, hoàn toàn chưa qua canonical fetch hay xác minh abstract/fulltext.*

- **PMID 31920804** — *Ứng viên chưa xác minh*: Review về diễn giải xét nghiệm chức năng gan AST, ALT, Bilirubin, Albumin.
- **PMID 33036934** — *Ứng viên chưa xác minh*: Diễn giải lâm sàng các bất thường điện giải giải máu.
- **PMID 29337649** — *Ứng viên chưa xác minh*: Ứng dụng High-Sensitivity Cardiac Troponin tại khoa Cấp cứu và động học hs-cTn.
- **PMID 32415177** — *Ứng viên chưa xác minh*: Các yếu tố ảnh hưởng đến đo lường HbA1c.

### 3. Tài liệu Tham khảo Định hướng Local (Local Guidance Notes)

- `Bai hoc y khoa/11_Noi khoa/BUN-Blood-Urea-Nitrogen/QA-BUN_2026-07-20.md`: Khái niệm quy đổi BUN $\leftrightarrow$ Ure, cơ chế tăng BUN trong XHTH trên. *(Tài liệu tham khảo định hướng, không phải evidence release)*.
- `Bai hoc y khoa/11_Noi khoa/IM-43_Doc_creatinine_eGFR_va_tiep_can_ton_thuong_than_cap/...`: Khái niệm Creatinine nền, sự phụ thuộc vào khối cơ. *(Tài liệu tham khảo định hướng)*.
- `Bai hoc y khoa/11_Noi khoa/IM-51_Dai_thao_duong/...`: Định hướng ngưỡng đường huyết chẩn đoán. *(Tài liệu tham khảo định hướng)*.

### 4. Các Hạng mục Claim Candidates (Cấm sử dụng khi chưa PASS exact quote / artifact)

*Tất cả các ngưỡng số dưới đây là **claim candidate — CẤM DÙNG trước khi exact quote / artifact PASS**.*

| Hạng mục Claim Candidate | Số liệu định hướng (Claim Candidate) | Yêu cầu Bằng chứng Bắt buộc | Note Kiểm định Fail-Closed |
|---|---|---|---|
| **Báo động Điện giải** | $K^+ < 2.5 \text{ mmol/L}$ hoặc $> 6.0 \text{ mmol/L}$; $Na^+ < 120 \text{ mmol/L}$ hoặc $> 160 \text{ mmol/L}$ *(Claim candidate)* | Consensus ADLM / Emergency Medicine | Bắt buộc verify exact quote về nguy cơ loạn nhịp và biến chứng thần kinh. |
| **Tỷ lệ BUN / Creatinine** | $\text{BUN/Cr} > 20:1$ (tính theo mg/dL) gợi ý nguyên nhân trước thận / XHTH *(Claim candidate)* | Standard Medical Textbook / Renal Consensus | Khẳng định chỉ mang tính gợi ý, KHÔNG phải tiêu chuẩn chẩn đoán xác định đơn độc. |
| **Tỷ lệ AST / ALT** | $\text{AST/ALT} > 2:1$ (gợi ý do rượu), $ALT > 1000 \text{ U/L}$ (viêm gan cấp/thuốc/thiếu máu) *(Claim candidate)* | Guideline EASL / AASLD chính thức | Bắt buộc verify exact quote phân lập tổn thương gan. |
| **Động học Troponin (Delta hs-cTn)** | Động học tăng/giảm theo assay cụ thể và protocol của labo *(Claim candidate)* | ESC / ACC Universal Definition | Cần bằng chứng phân biệt tổn thương cơ tim (myocardial injury) vs Nhồi máu cơ tim cấp (MI). |
| **Nhiễu HbA1c** | Thiếu máu thiếu sắt tăng giả; Bệnh hồng cầu liềm/tán huyết giảm giả *(Claim candidate)* | ADA Standards of Care chính thức | Bắt buộc verify các yếu tố nhiễu phương pháp đo. |

### 5. Claims Nguy hiểm & Điều Cấm (Critical Safety Warnings for Part 3)

- 🚫 **CẤM kết luận nhồi máu cơ tim chỉ dựa vào 1 trị số Troponin đơn độc tăng nhẹ**: Phải có **động học (delta check theo protocol labo)** và lâm sàng/ECG. Troponin tăng mạn tính gặp trong suy thận, suy tim, nhiễm trùng huyết.
- 🚫 **CẤM đọc Creatinine bình thường là chức năng thận bình thường ở BN người già teo cơ**: Ở người già/suy kiệt, Creatinine sản xuất ít nên Creatinine máu có thể "bình thường" nhưng eGFR thực tế đã giảm nặng.
- 🚫 **CẤM chẩn đoán XHTH trên chỉ dựa vào tỷ lệ BUN/Creatinine**: Phải kết hợp lâm sàng, thăm khám phân, huyết động và nội soi.
- 🚫 **CẤM bỏ qua Kali máu tăng giả do vỡ hồng cầu (Hemolysis)**: Khi Kali tăng đơn độc không phù hợp lâm sàng/ECG, phải kiểm tra chỉ số H (Hemolysis index) trên mẫu máu trước khi xử trí hạ Kali dồn dập.

---

## IV. BẢN ĐỒ KẾT NỐI 4 CA TÍCH HỢP LÂM SÀNG (PART 3 INTEGRATION CASES)

Part 3 kết thúc bằng **4 Ca lâm sàng thực tế**, phối hợp toàn bộ kiến thức CBC (Part 2), Đông máu (Part 2) và Sinh hóa (Part 3) theo Quy tắc 5 bước đọc tại giường bệnh:

1. **Ca 1: Xuất huyết tiêu hóa cấp trên bệnh nhân Xơ gan**
   - *Phối hợp*: CBC (Hb giảm, PLT giảm do cường lách), Đông máu (PT/INR kéo dài do giảm tổng hợp yếu tố gan), Sinh hóa (BUN tăng cao lệch so với Creatinine, Bilirubin tăng, Albumin giảm).
   - *Định hướng*: Hồi sức thể tích, phân biệt BUN tăng do máu ruột vs AKI trước thận, ngưỡng truyền máu/tiểu cầu/huyết tương tươi.
2. **Ca 2: Tổn thương thận cấp (AKI) sau nhiễm trùng huyết / Đau bụng cấp**
   - *Phối hợp*: CBC (WBC tăng cao, Neutrophil chuyển trái), Sinh hóa (Creatinine tăng nhanh từ baseline, BUN tăng, K+ tăng, CRP tăng cao), Đông máu (Fibrinogen tăng như phản ứng pha cấp hoặc giảm trong DIC giai đoạn muộn).
   - *Định hướng*: Phát hiện AKI giai đoạn sớm, xử trí báo động Kali máu, điều chỉnh liều thuốc theo eGFR.
3. **Ca 3: Mẫu máu vỡ hồng cầu (Hemolysis) vs Bệnh lý tán huyết thật sự**
   - *Phối hợp*: CBC (RBC giảm, RDW tăng trong tán huyết thật), Sinh hóa (K+ tăng cao, LDH tăng, Bilirubin gián tiếp tăng trong tán huyết thật; K+ tăng đơn độc kèm H-index dương tính trong vỡ hồng cầu tiền phân tích).
   - *Định hướng*: Tránh xử trí nhầm Kali tăng giả, yêu cầu lấy lại mẫu máu chuẩn.
4. **Ca 4: Đau ngực cấp vào viện — Phân biệt Nhồi máu cơ tim vs Bệnh lý toàn thân**
   - *Phối hợp*: Sinh hóa (hs-Troponin T/I tăng kèm delta thay đổi rõ sau 1-2 giờ theo protocol labo, Glucose máu tăng phản ứng), CBC (WBC tăng nhẹ do stress), Đông máu (PT/aPTT bình thường trước khi dùng chống đông).
   - *Định hướng*: Đánh giá động học Troponin theo thời gian, ra quyết định can thiệp mạch vành cấp cứu.

---

## V. XÁC NHẬN BẢO TOÀN VÀ NGUYÊN TẮC PHÁT HÀNH

1. **Không cập nhật Catalog / Readme**: File catalog (`DANH_SACH_BAI_HOC.md`, `_README.md`) giữ nguyên cho đến khi bài xuất bản hoàn tất qua `publish_gate.py`.
2. **Không viết Brief / Lesson / Cards**: File này chỉ đóng vai trò **Bản đồ nguồn & Ranh giới (Source Map & Boundaries)**.
3. **Định dạng & Lưu trữ**:
   - Đường dẫn chuẩn: `Bai hoc y khoa/11_Noi khoa/IM-04_Huong_dan_doc_xet_nghiem_mau_co_ban/IM-04_PART2_PART3_SOURCE_MAP.md`
   - Tên file không dấu, nội dung tiếng Việt có dấu 100%.
