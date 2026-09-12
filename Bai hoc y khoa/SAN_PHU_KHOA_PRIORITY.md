# Danh sách ưu tiên bài học Sản Phụ khoa

> Lập ngày 2026-07-15 từ `LESSON_BACKLOG.md`, `_CATALOG.md`, cây thư mục thực tế và `SESSION_LOG_2026-07-06.md`.
>
> Phạm vi: Sản Phụ khoa theo nghĩa thực hành, gồm sản khoa, phụ khoa, hỗ trợ sinh sản (ART), siêu âm thai và siêu âm phụ khoa. Đây là **thứ tự làm bài**, không khẳng định các bài cũ đã đạt toàn bộ cổng kiểm tra. Trước khi build bất kỳ bài nào, bắt buộc chạy quy trình trong `WORKFLOW.md`.

## Nguyên tắc xếp ưu tiên

1. **P0**: khoảng trống có nguy cơ ảnh hưởng trực tiếp đến quyết định lâm sàng, hoặc bài đang trống/thiếu MD nguồn nên chưa thể kiểm chứng và tái sử dụng an toàn.
2. **P1**: nội dung nền tảng có tần suất cao; hoàn thiện sau khi các khoảng trống P0 được xử lý.
3. **P2**: chuyên sâu hoặc mở rộng sau khi chuỗi lõi đã vững.
4. Trong cùng mức ưu tiên, ưu tiên bài đã có thư mục và tài liệu nền để hoàn thiện trước; tránh tạo một bài trùng phạm vi với bài đang có.
5. Một bài chỉ được đánh dấu hoàn tất khi có MD nguồn, `cards.v2.json`, APKG và các cổng kiểm tra bắt buộc đều đạt.

## P0 — Làm trước

### 1. Độ dài cổ tử cung và dự phòng sinh non

- Mã: `03_Sieu am thai/09_Cervical_Length_PTB`
- Trạng thái: Cần cập nhật; bài cũ thiếu MD nguồn theo session log.
- Vì sao trước: đo cổ tử cung, progesterone và cerclage là quyết định có thời điểm rõ, sai kỹ thuật hoặc chỉ định gây hậu quả lớn.
- Phạm vi tối thiểu: kỹ thuật đo TVS, funneling, sludge, chỉ định/giới hạn progesterone, cerclage và pessary.

### 2. Thai chậm tăng trưởng (FGR): Doppler và quyết định theo dõi/chấm dứt thai kỳ

- Mã: `03_Sieu am thai/12_FGR_Doppler_UmbA_MCA`
- Trạng thái: Cần cập nhật MD và thẻ.
- Vì sao trước: bài hiện có chủ yếu là Doppler; còn thiếu liên kết Doppler với theo dõi, corticosteroid và thời điểm sinh.
- Phạm vi tối thiểu: UmbA, MCA, ductus venosus, early/late FGR, khoảng theo dõi và nguyên tắc chấm dứt thai kỳ.

### 3. Ối vỡ non (PPROM): siêu âm và quản lý

- Mã đề xuất: `03_Sieu am thai/45_PPROM_Ultrasound_Management`
- Trạng thái: Bài mới.
- Vì sao trước: khoảng trống rõ trong backlog; liên quan nhiễm trùng, sinh non và quyết định theo dõi/sinh.
- Phạm vi tối thiểu: xác nhận chẩn đoán, AFI/DVP, latency, dấu hiệu nhiễm trùng ối, giới hạn vai trò siêu âm và các điểm cần hội chẩn.

### 4. Theo dõi siêu âm trong kích thích buồng trứng

- Mã: `02_Ho tro sinh san ART/41_US_Monitoring_Ovarian_Stimulation`
- Trạng thái: Cần hoàn thiện cards/APKG; tồn tại thư mục trình chiếu trùng cần gộp về bài này.
- Vì sao trước: là thao tác thường nhật của ART và là nền để dùng thuốc, trigger, phòng OHSS.
- Phạm vi tối thiểu: AFC nền, số/lớn nang, nội mạc, E2 khi có chỉ định, tiêu chí đánh giá nguy cơ và quyết định tiếp theo.

### 5. Nang buồng trứng trước kích thích buồng trứng (COS)

- Mã: `02_Ho tro sinh san ART/35_Ovarian_Cyst_Before_COS`
- Trạng thái: Cần xây lại MD nguồn; hiện không đủ chuỗi deliverable chuẩn.
- Vì sao trước: quyết định bắt đầu, trì hoãn hay xử trí nang có tác động trực tiếp đến chu kỳ điều trị.
- Phạm vi tối thiểu: phân biệt nang chức năng/nang bệnh lý, đánh giá bằng siêu âm-hormone, tiêu chí trì hoãn và những điều không nên làm thường quy.

### 6. Thất bại làm tổ tái diễn (RIF)

- Mã: `02_Ho tro sinh san ART/45_Recurrent_Implantation_Failure_RIF`
- Trạng thái: Thư mục trống.
- Vì sao trước: nhu cầu thực hành cao và dễ dẫn tới xét nghiệm/can thiệp không có bằng chứng.
- Phạm vi tối thiểu: định nghĩa đang dùng, đánh giá có chọn lọc, yếu tố phôi-tử cung-toàn thân và các can thiệp không khuyến cáo thường quy.

### 7. Phác đồ đối kháng GnRH

- Mã đề xuất: `02_Ho tro sinh san ART/46_GnRH_Antagonist_Protocol`
- Trạng thái: Bài mới.
- Vì sao trước: là phác đồ cốt lõi chưa có bài chuyên sâu riêng; cần nối trực tiếp với monitoring, trigger và OHSS.
- Phạm vi tối thiểu: chỉ định, khởi động antagonist, trigger, luteal support và các chi tiết protocol phải có nguồn gốc đã kiểm chứng.

### 8. Nhiễm trùng lây truyền qua đường tình dục (STIs) trong Sản Phụ khoa

- Mã đề xuất: `05_Vi sinh - Mien dich/V2_STIs`
- Trạng thái: Bài mới; đã được session log xác định là bài kế tiếp.
- Vì sao trước: bao phủ Chlamydia, lậu, giang mai, HSV; ảnh hưởng trực tiếp đến sàng lọc, điều trị bạn tình và thai kỳ.
- Phạm vi tối thiểu: tiếp cận hội chứng, xét nghiệm, điều trị theo guideline hiện hành, quản lý bạn tình và các điểm riêng trong thai kỳ.

### 9. Bệnh viêm vùng chậu (PID) và áp xe phần phụ

- Mã đề xuất: `05_Vi sinh - Mien dich/V3_PID`
- Trạng thái: Bài mới.
- Vì sao trước: cấp cứu phụ khoa phổ biến, cần liên kết với đau bụng cấp, vô sinh và nguy cơ TOA.
- Phạm vi tối thiểu: chẩn đoán lâm sàng, chỉ định nhập viện, siêu âm TOA, kháng sinh theo guideline và theo dõi thất bại điều trị.

### 10. Bất thường ống Müller: phân loại và siêu âm 3D

- Mã đề xuất: `01_San phu khoa/40_Mullerian_Anomalies_3D_US`
- Trạng thái: Bài mới; các bài Asherman/tử cung nhi hóa không thay thế được.
- Vì sao trước: tránh nhầm vách ngăn tử cung với tử cung hai sừng, vốn dẫn tới chỉ định can thiệp khác nhau.
- Phạm vi tối thiểu: phân loại ASRM/ESHRE, mặt phẳng coronal của siêu âm 3D, septate/bicornuate/didelphys và chỉ định hội chẩn.

## P1 — Hoàn thiện chuỗi lõi

### Sản khoa

1. **Siêu âm quý 1 cơ bản: vị trí thai, thai sống và tuổi thai** — bài mới; gồm thai trong/ngoài tử cung, CRL/GS/yolk sac, sảy thai sớm và thai trứng trống.
2. **Sàng lọc tiền sản giật và dự phòng** — `01_San phu khoa/03_Preeclampsia_Screening`; cần xây lại MD nguồn và thẻ.
3. **Đái tháo đường thai kỳ (GDM)** — `01_San phu khoa/08_GDM/GDM_Comprehensive`; cần rà soát toàn bộ cổng kiểm tra.
4. **Sinh lý chuyển dạ, khởi phát chuyển dạ và đẻ chỉ huy** — `01_San phu khoa/05_Sinh_ly_chuyen_da_Do_de` và `07_De_chi_huy_OVD`; cần chuẩn hóa MD/thẻ/APKG, tách phạm vi rõ nếu cần.
5. **Siêu âm tăng trưởng quý 3 và thai nhỏ so với tuổi thai (SGA)** — bài mới; là tiền đề cho bài FGR đã cập nhật.
6. **Đánh giá sức khỏe thai: BPP, NST và chỉ định Doppler** — bài mới; tránh lặp FGR, tập trung nguyên tắc chọn và diễn giải test.
7. **Thai to (LGA/macrosomia) và dự báo khó sinh vai** — bài mới.
8. **Bất đồng Rh và thiếu máu thai bằng MCA-PSV** — bài mới.

### Phụ khoa

9. **Đau bụng cấp phụ khoa qua siêu âm đầu dò** — bài mới; PID/TOA, xoắn phần phụ, nang xuất huyết và thai ngoài tử cung.
10. **Khối phần phụ: IOTA, ADNEX và O-RADS** — bài mới; tiếp nối `35_TVS_Adnexal_Abnormal`, không lặp lại giải phẫu cơ bản.
11. **Siêu âm nội mạc tử cung: IETA, polyp, tăng sản và ung thư nội mạc** — bài mới.
12. **AUB theo PALM-COEIN** — `01_San phu khoa/22_AUB_Abnormal_Uterine_Bleeding`; rà soát gate và cập nhật nếu guideline đã đổi.
13. **Lạc nội mạc tử cung** — `01_San phu khoa/01_Lac noi mac tu cung - Endometriosis`; cần xây lại MD nguồn và thẻ.
14. **Adenomyosis và ảnh hưởng đến sinh sản/ART** — `01_San phu khoa/02_Adenomyosis - Anh huong ART`; cần xây lại MD nguồn và thẻ.
15. **U xơ tử cung trong vô sinh và ART** — `01_San phu khoa/39_U_xo_tu_cung_ART_Infertility`; cần rà soát gate trước khi xem là bài hoàn tất.
16. **Tránh thai toàn diện** — `01_San phu khoa/37_Contraception_Comprehensive`; rà soát cổng, vì MD/thẻ/APKG đã có.

### ART

17. **OHSS: dự phòng và xử trí** — `02_Ho tro sinh san ART/07_OHSS - Prevention and Management` và `21_OHSS_Comprehensive`; hợp nhất phạm vi, chọn một bài MD chuẩn.
18. **Trigger trong ART và hội chứng nang trống** — `02_Ho tro sinh san ART/18_ART_Trigger`; rà soát cổng và hoàn thiện thẻ.
19. **Luteal phase support** — `02_Ho tro sinh san ART/22_Luteal_Phase_Support_Chuyen_De`; rà soát cổng và dùng làm bài chuẩn, không duy trì hai bài trùng.
20. **Thai ngoài tử cung/vị trí thai không rõ sau ART** — mở rộng từ `02_Ho tro sinh san ART/06_IUI - PUL EP IUP management`; cần chuẩn hóa MD, thẻ và APKG.

## P2 — Chuyên sâu sau khi P0–P1 ổn định

1. Sàng lọc quý 1 chuyên sâu: NT, nasal bone, tricuspid regurgitation, ductus venosus và combined test.
2. Siêu âm lồng ngực thai: CDH, CPAM, BPS, tràn dịch màng phổi và thiểu sản phổi.
3. Bất thường thành bụng thai chuyên sâu: bladder/cloacal exstrophy, limb-body wall complex, pentalogy of Cantrell.
4. Ngôi mông/ngôi ngang và ngoại xoay thai.
5. Chọc ối, sinh thiết gai nhau, giảm thiểu thai và thai bám sẹo mổ lấy thai.
6. OPU và chuyển phôi dưới hướng dẫn siêu âm.
7. PCOS/PCOM và AFC.
8. Nội tiết sinh sản: PCOS, mãn kinh, HRT — mở chuỗi `04_Noi tiet - Hormone`.
9. Ung thư phụ khoa: cổ tử cung, nội mạc tử cung, buồng trứng, GTD — mở chuỗi `06_Ung thu phu khoa`.
10. Viêm nhiễm thai kỳ, hậu sản, HIV và HBV trong thai kỳ — hoàn tất chuỗi V5–V8.

## Lộ trình thực thi khuyến nghị

- **Đợt 1:** P0 mục 1–5 để khóa các quyết định siêu âm/ART thường gặp.
- **Đợt 2:** P0 mục 6–10 để phủ RIF, nhiễm trùng và bất thường tử cung.
- **Đợt 3:** P1 theo ba nhánh song song về nội dung, nhưng chỉ build từng bài sau khi bài trước qua toàn bộ gate.
- **Quy tắc chọn bài kế tiếp:** ưu tiên mục P0 có sẵn thư mục hoặc có nhu cầu lâm sàng tức thời; nếu không có tín hiệu nhu cầu, làm theo thứ tự danh sách.

## Cổng hoàn tất cho từng bài

- Preflight guideline check đạt yêu cầu.
- MD tiếng Việt có dấu và nguồn PMID/guideline đã kiểm chứng.
- `verify_all_pmids.py`, `verify_claims.py`, citation audit và kiểm tra dấu đạt yêu cầu.
- Có `cards.v2.json` và APKG; APKG đạt kiểm tra dấu.
- Cập nhật `_README.md` và `_CATALOG.md` sau khi hoàn tất.
