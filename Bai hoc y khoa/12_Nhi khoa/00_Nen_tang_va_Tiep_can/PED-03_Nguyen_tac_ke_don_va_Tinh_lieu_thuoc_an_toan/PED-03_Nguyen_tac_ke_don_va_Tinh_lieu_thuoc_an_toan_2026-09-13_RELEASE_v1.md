# BÀI HỌC Y KHOA: NGUYÊN TẮC KÊ ĐƠN & TÍNH LIỀU THUỐC AN TOÀN Ở TRẺ EM (PED-03)

**Mã bài:** PED-03  
**Chuyên khoa:** Nhi khoa / Dược lý lâm sàng & Hồi sức Cấp cứu Nhi  
**Đối tượng:** Bác sĩ thực hành, học viên lâm sàng, sinh viên y khoa chuẩn bị trực cấp cứu và điều trị nội trú Nhi (Chế độ sư phạm: L3_BEGINNER — Cầm tay chỉ việc cho người bắt đầu)  
**Đường học trước:** [PED-01: Đặc điểm sinh lý & Bảng sinh hiệu bình thường theo tuổi] · [PED-02: Tam giác đánh giá nhi khoa (PAT) & Tiếp cận ABCDE]  
**Đường học tiếp theo:** Mở khóa trực tiếp 19 bài tiếp theo trong Core 45: [PED-04: Hồi sức tim phổi PALS] · [PED-05: Xử trí sốc giờ đầu] · [PED-06: Phản vệ nhi khoa] · [PED-07: Co giật & Trạng thái động kinh] · [PED-08: Cơn hen cấp nặng] · [PED-10: Ngộ độc Paracetamol] · [PED-16: Nhiễm khuẩn sơ sinh] · [PED-17: Hạ đường huyết sơ sinh] · [PED-21: Viêm phổi cộng đồng CAP] · [PED-27: Tiêu chảy cấp] · [PED-33 & 34: Sốt xuất huyết Dengue] · [PED-35: Tay chân miệng] · [PED-37: Viêm màng não mủ] · [PED-40: Hội chứng thận hư] · [PED-45: DKA]  
**Revision phát hành:** RELEASE v1  
**Research brief khóa nguồn:** PED-03_RESEARCH_BRIEF.md  

---

## 0. TỔNG QUAN — VÌ SAO BÀI NÀY QUAN TRỌNG?

Ở người trưởng thành nặng 60 kg, việc nhầm lẫn liều 500 mg thành 600 mg hiếm khi đe dọa trực tiếp tính mạng bệnh nhân. Nhưng trong Nhi khoa, một bệnh nhi sơ sinh nặng 1 kg hay một trẻ nhũ nhi nặng 5 kg không bao giờ có được "khoảng dung sai an toàn" đó. Trong lâm sàng Nhi, **một dấu thập phân đặt sai vị trí đồng nghĩa với việc bệnh nhi nhận một liều thuốc gấp 10 lần hoặc chỉ bằng 1/10 nhu cầu điều trị — một bên gây ngộ độc tử vong tức thì, một bên làm thất bại điều trị cấp cứu**.

Một nghiên cứu dịch tễ kinh điển của Kaushal R và cộng sự trên tạp chí JAMA (PMID: 11311101) đã chỉ ra rằng: **tỷ lệ sai sót liên quan đến thuốc (Medication Errors) ở bệnh nhi nội trú cao gấp 3 lần so với bệnh nhân người lớn**, và nguy cơ dẫn đến các biến cố bất lợi tiềm tàng đe dọa tính mạng cao vượt trội. Trong đó, sai sót tính toán liều lượng ở khâu bác sĩ ra y lệnh chiếm tới hơn một nửa tổng số sai sót.

Nguyên nhân cốt lõi là trẻ em không phải người lớn thu nhỏ. Hơn thế nữa, **trẻ em ở các lứa tuổi khác nhau hoàn toàn không đồng nhất với nhau**. Một trẻ sơ sinh non tháng 28 tuần tuổi có cấu trúc dược động học, tỷ lệ nước và hoạt tính men gan khác xa một trẻ sơ sinh đủ tháng 3 ngày tuổi, khác một trẻ nhũ nhi 6 tháng tuổi, khác một trẻ 4 tuổi và hoàn toàn khác một thiếu niên 14 tuổi. Kê đơn cho bệnh nhi đòi hỏi người thầy thuốc phải nắm vững bản chất sinh lý học phát triển (Developmental Pharmacokinetics), luôn tuân thủ quy trình tính liều 5 bước chuẩn mực, và làm chủ các công cụ chuyển đổi dạng bào chế tại giường bệnh.

### 0.1 Nền tảng tối thiểu cần dùng ngay
*(Dành cho người học bắt đầu từ số 0 — Bắt buộc phải hiểu cặn kẽ các định nghĩa bản chất trước khi tính toán)*

Để kê đơn an toàn và tránh các bẫy chết người, người học cần nắm vững các thuật ngữ và định nghĩa cốt lõi sau đây:
- **Liều theo cân nặng (mg/kg)** là thông số liều lượng chuẩn hóa quốc tế được tính bằng số miligam hoạt chất trên một kilogam trọng lượng cơ thể của bệnh nhi trong một lần dùng hoặc trong 24 giờ.
- **Bẫy trần liều người lớn (Adult Ceiling Dose Trap)** là tình trạng khi áp dụng công thức nhân liều thông thường theo mg/kg ở những trẻ có cân nặng lớn (hoặc trẻ béo phì) sẽ dẫn đến một con số tính toán vượt qua liều tối đa hàng ngày được phép dùng ở người trưởng thành.
- **Thể tích phân bố (Volume of Distribution - Vd)** là thể tích dịch lý thuyết cần thiết để chứa toàn bộ lượng thuốc đưa vào cơ thể sao cho nồng độ thuốc trong thể tích dịch đó bằng đúng nồng độ thuốc đo được trong huyết tương.
- **Độ lọc cầu thận (Glomerular Filtration Rate - GFR)** là chỉ số thể tích huyết tương được lọc sạch qua mạng lưới mao mạch cầu thận của cả hai quả thận trong thời gian một phút tính trên diện tích da chuẩn hóa 1.73 m².
- **Dịch duy trì (Maintenance Fluid)** là thể tích nước và các chất điện giải tối thiểu cần cung cấp trong 24 giờ nhằm bù đắp lượng dịch mất đi qua đường sinh lý bình thường (nước tiểu, phân, mồ hôi và hơi thở) khi bệnh nhân không thể ăn uống qua đường tiêu hóa.
- **Phương pháp Holliday-Segar** là công thức kinh điển chuẩn hóa toàn cầu được tính theo nguyên tắc 100/50/20 ml/kg/24 giờ dựa trên mức tiêu hao năng lượng sinh lý của cơ thể trẻ theo từng khoảng cân nặng.
- **Quy tắc 4-2-1** là công thức tính nhanh tốc độ truyền dịch duy trì tính theo đơn vị ml/giờ, trong đó 4 ml/kg/giờ cho 10 kg đầu, 2 ml/kg/giờ cho 10 kg tiếp theo và 1 ml/kg/giờ cho mỗi kg vượt quá 20 kg.
- **Tốc độ truyền glucose (Glucose Infusion Rate - GIR)** là chỉ số đo lường lượng glucose được đưa vào cơ thể qua đường tĩnh mạch tính theo đơn vị mg/kg/phút nhằm duy trì đường huyết ổn định, đặc biệt sống còn ở trẻ sơ sinh.
- **Thuốc có nguy cơ cao (High-Alert Medications)** là nhóm thuốc mang nguy cơ gây hại nghiêm trọng hoặc gây tử vong tức thì cho bệnh nhân nếu xảy ra sai sót trong bất kỳ khâu chỉ định, pha chế, tính toán hay tiêm truyền.
- **Thuốc dễ nhầm lẫn (LASA - Look-Alike Sound-Alike)** là nhóm các cặp thuốc có bao bì, nhãn mác nhìn giống hệt nhau hoặc có tên gọi, cách phát âm gần tương tự nhau rất dễ dẫn đến tai biến dùng nhầm thuốc trong ca trực.
- **Diện tích bề mặt cơ thể (Body Surface Area - BSA)** là tổng diện tích da toàn bộ cơ thể tính bằng mét vuông (m²), thường được ước tính bằng công thức Mosteller dựa trên chiều cao và cân nặng.
- **Độ thanh thải thận (Renal Clearance - Clr)** là thể tích huyết tương được thận lọc sạch hoàn toàn một chất nhất định trong thời gian một đơn vị phút.

> 🚨 **BOX ĐỎ — NĂM NGUYÊN TẮC AN TOÀN SỐNG CÒN TRONG KÊ ĐƠN NHI:**  
> Dừng ngay hành động và kích hoạt quy trình kiểm soát độc lập (Double-check) nếu rơi vào các tình huống sau:  
> 1. **Cấm tuyệt đối tiêm bolus tĩnh mạch trực tiếp Kali clorua (KCl)** ➔ Gây mất phân cực màng cơ tim, xuất hiện rung thất và vô tâm thu ngừng tim tử vong ngay lập tức!  
> 2. **Cấm dùng dung dịch Dextrose ưu trương 30% hay 50% ở trẻ sơ sinh** ➔ Áp lực thẩm thấu quá cao gây hoại tử mô nếu thoát mạch, xuất huyết não thất và hạ đường huyết phản ứng dội ngược! Chỉ dùng Glucose 10% mini-bolus 2 ml/kg.  
> 3. **Cấm tiêm tĩnh mạch Adrenaline nồng độ 1:1.000 trực tiếp khi bệnh nhân còn mạch** ➔ Gây cơn tăng huyết áp kịch phát, xuất huyết não và loạn nhịp tử vong! Tiêm bắp phản vệ dùng 1:1.000 (0.01 ml/kg); tiêm tĩnh mạch hồi sức ngừng tim bắt buộc pha loãng thành 1:10.000 (0.1 ml/kg).  
> 4. **Cấm viết dấu thập phân nguy hiểm: thiếu số 0 dẫn đầu (viết `.5 mg`) hoặc thừa số 0 đuôi (viết `5.0 mg`)** ➔ Rất dễ đọc nhầm thành 5 mg (gấp 10 lần) hoặc 50 mg (gấp 10 lần)! Luôn viết `0,5 mg` và `5 mg`.  
> 5. **Cấm quên kiểm tra trần liều người lớn khi kê đơn cho trẻ em ≥ 40 kg** ➔ Công thức mg/kg ở trẻ béo phì hoặc trẻ lớn sẽ vượt trần liều độc hại của Ceftriaxone, Prednisolone, Paracetamol và Dexamethasone.  

---

## 1. ĐỊNH NGHĨA VÀ NĂM NGUYÊN TẮC CỐT LÕI TRONG DƯỢC ĐỘNG HỌC NHI

Để hiểu vì sao việc áp dụng máy móc liều người lớn cho trẻ em lại gây ra thảm họa, người thầy thuốc phải nắm vững 5 nguyên tắc dược động học (ADME Ontogeny) gắn liền với quá trình trưởng thành của các cơ quan theo công trình của Kearns GL và cộng sự (PMID: 13679531).

```text
               TIẾN TRÌNH TRƯỞNG THÀNH DƯỢC ĐỘNG HỌC NHI (ADME)
                                       │
     ┌─────────────────────────────────┼─────────────────────────────────┐
     ▼                                 ▼                                 ▼
[HẤP THU - A]                   [PHÂN BỐ - D]                    [CHUYỂN HÓA - M]
pH dạ dày sơ sinh cao           Nước cơ thể: 85% (non) -> 60%    CYP450/UGT sơ sinh kém
Hấp thu qua da cực lớn (x3)     Mỡ thấp, Albumin gắn kém         Trẻ 1-9 tuổi chuyển hóa
Tiêm bắp thất thường            Thuốc ưa nước cần liều nạp cao   nhanh hơn cả người lớn!
     │                                 │                                 │
     └─────────────────┬───────────────┴─────────────────┬───────────────┘
                       ▼                                 ▼
               [THẢI TRỪ - E]                     [HÀNG RÀO TKTW]
               GFR sơ sinh chỉ 20-40 ml/phút      Hàng rào máu não lỏng lẻo
               Đạt chuẩn lúc 1-2 tuổi             Dễ ngấm Opioid, An thần
               Aminoglycosid phải giãn cữ liều    Vàng da nhân não do Bilirubin
```

### 1.1 Khác biệt Hấp thu (A - Absorption)
- **Đường tiêu hóa**: Ở trẻ sơ sinh đủ tháng và đặc biệt là non tháng, nồng độ acid dịch vị dạ dày rất thấp (pH dịch vị lúc mới sinh thường kiềm tính từ 6 đến 8, sau đó giảm dần về mức pH 1.5 đến 3 sau vài tháng). Tình trạng giảm acid dịch vị làm tăng sinh khả dụng của các thuốc có bản chất kiềm yếu (như Penicillin, Ampicillin) nhưng lại làm giảm hấp thu các thuốc acid yếu (như Phenobarbital, Phenytoin). Tốc độ làm rỗng dạ dày ở trẻ nhũ nhi chậm và nhu động ruột thất thường, khiến nồng độ đỉnh của thuốc hấp thu qua đường tiêu hóa xuất hiện chậm và khó dự đoán.
- **Hấp thu qua da (Percutaneous Absorption)**: Lớp sừng da của trẻ sơ sinh và trẻ nhũ nhi rất mỏng, hàng rào lipid biểu bì chưa hoàn thiện, mạng lưới mao mạch dưới da cực kỳ phong phú. Đặc biệt, tỷ lệ diện tích bề mặt da trên trọng lượng cơ thể ($BSA / Weight$) ở trẻ sơ sinh cao gấp gần 3 lần người lớn. Do đó, thuốc bôi ngoài da hấp thu vào tuần hoàn hệ thống với nồng độ rất cao. Điển hình: việc bôi Corticoid diện rộng gây ức chế trục hạ đồi - tuyến yên - thượng thận (HPA), ngộ độc cồn do lau mát hạ sốt, hoặc ngộ độc Salicylate do bôi thuốc mỡ giảm đau.
- **Tiêm bắp (Intramuscular - IM)**: Khối cơ vân ở trẻ sơ sinh còn nhỏ, tưới máu cơ thất thường khi trẻ bị lạnh hoặc hạ huyết áp. Hấp thu thuốc tiêm bắp nhìn chung chậm và không ổn định. Ngoại lệ lâm sàng duy nhất: **mặt trước-ngoài đùi (cơ rộng ngoài - vastus lateralis)** có mạng lưới tưới máu dồi dào, là vị trí hấp thu chuẩn mực và nhanh nhất của Adrenaline trong xử trí cấp cứu sốc phản vệ.
- **Đường trực tràng (Rectal)**: Tĩnh mạch trực tràng dưới đổ trực tiếp vào tuần hoàn hệ thống (không qua gan lần đầu), trong khi tĩnh mạch trực tràng trên đổ vào hệ cửa qua gan. Mức độ hấp thu qua đường trực tràng ở trẻ nhỏ dao động rất lớn (sinh khả dụng Paracetamol đặt hậu môn chỉ đạt 60–70% so với đường uống), do đó chỉ dùng khi trẻ nôn ói liên tục, co giật hoặc hôn mê.

### 1.2 Khác biệt Phân bố (D - Distribution) & Động học Nước - Mỡ
- **Tỷ lệ nước toàn bộ cơ thể (Total Body Water - TBW)**: Đây là khác biệt sinh lý then chốt nhất trong dược động học phân bố.
  - Sơ sinh non tháng: Nước chiếm **85%** trọng lượng cơ thể.
  - Sơ sinh đủ tháng: Nước chiếm **78%** trọng lượng cơ thể.
  - Trẻ 1 tuổi: Nước chiếm **65%** trọng lượng cơ thể.
  - Người trưởng thành: Nước chỉ chiếm **55–60%** trọng lượng cơ thể.
- Khoang dịch ngoại bào (Extracellular Fluid - ECF) ở sơ sinh chiếm tới 40–50% trọng lượng (so với 20% ở người lớn). Hệ quả lâm sàng: Các thuốc ưa nước, tan trong nước (như kháng sinh nhóm Aminoglycosid: Gentamicin, Amikacin; kháng sinh nhóm Glycopeptid: Vancomycin) sẽ bị pha loãng mạnh trong thể tích phân bố ngoại bào khổng lồ của trẻ sơ sinh. Do đó, để đạt được nồng độ đỉnh trị liệu trong máu (Peak Concentration - Cmax), trẻ sơ sinh đòi hỏi **liều khởi đầu tính theo mg/kg cao hơn người lớn** (ví dụ Gentamicin liều sơ sinh là 5–7.5 mg/kg so với liều người lớn 3–5 mg/kg).
- **Mô mỡ và lượng protein huyết tương**: Khối mô mỡ ở trẻ sơ sinh rất thấp (chỉ khoảng 12% ở trẻ đủ tháng và < 3% ở trẻ non tháng). Các thuốc tan nhiều trong mỡ (như Diazepam, Thiopental) sẽ ít có mô mỡ để phân bố lại, khiến nồng độ tự do trong máu duy trì cao. Đồng thời, nồng độ Albumin và alpha-1 acid glycoprotein trong huyết tương sơ sinh còn thấp, ái lực liên kết protein yếu. Tỷ lệ thuốc ở dạng tự do (dạng có hoạt tính sinh học và gây độc tính) tăng cao đáng kể đối với các thuốc liên kết protein mạnh như Phenytoin, Theophyllin.
- **Cạnh tranh vị trí gắn Albumin**: Các thuốc như Ceftriaxone, Sulfonamid (Co-trimoxazole) có ái lực gắn Albumin rất mạnh, cạnh tranh và đẩy Bilirubin tự do ra khỏi Albumin. Bilirubin tự do không tan trong nước sẽ vượt qua hàng rào máu não chưa hoàn thiện, ngấm vào các nhân xám đáy não gây **Vàng da nhân não (Kernicterus)** — một tổn thương thần kinh vĩnh viễn gây tử vong hoặc bại não thể múa vờn.

### 1.3 Khác biệt Chuyển hóa gan (M - Metabolism) & Hệ Enzyme CYP / UGT
- **Giai đoạn sơ sinh**: Các enzyme chuyển hóa pha I (Cytochrome P450: CYP1A2, CYP2C9, CYP3A4) và đặc biệt là pha II (liên hợp Glucuronid hóa - UGT2B7) tại gan chưa trưởng thành. Khả năng liên hợp Glucuronid chỉ đạt mức người lớn sau 1 đến 2 năm tuổi.
  - *Ví dụ 1*: Sự thiếu hụt enzyme UDP-glucuronosyltransferase ở trẻ sơ sinh làm ứ đọng nồng độ thuốc không liên hợp, dẫn đến **Hội chứng xám (Grey baby syndrome)** chết người kinh điển khi dùng Chloramphenicol (trụy tim mạch, da tím tái màu xám tro, hạ thân nhiệt và tử vong).
  - *Ví dụ 2*: Chuyển hóa Paracetamol ở trẻ sơ sinh chủ yếu đi qua con đường liên hợp Sulfat hóa (Sulfation pathway), con đường Glucuronid hóa hoạt động yếu. Trẻ nhỏ có khả năng dự trữ và tái tạo Glutathione tại gan rất tốt, giúp trung hòa chất chuyển hóa độc hại NAPQI.
- **Giai đoạn trẻ nhỏ từ 1 đến 9 tuổi — "Động cơ chuyển hóa siêu tốc"**: Đây là một ngộ nhận lâm sàng phổ biến khi cho rằng trẻ em chuyển hóa thuốc chậm hơn người lớn. Ngược lại, trẻ từ 1 đến 9 tuổi có tỷ lệ khối lượng gan trên trọng lượng cơ thể lớn hơn người lớn gần 2 lần, lưu lượng máu qua gan tính theo kg cao hơn và hoạt tính nhiều enzyme CYP450 trưởng thành vượt bậc. Nhóm tuổi này **chuyển hóa nhiều loại thuốc (như Phenytoin, Carbamazepine, Valproate, Theophylline) nhanh hơn người trưởng thành**. Do đó, trẻ 1–9 tuổi thường cần liều tính theo mg/kg cao hơn và khoảng cách đưa liều ngắn hơn người lớn để duy trì nồng độ thuốc hiệu quả trong máu.
- **Bước vào tuổi dậy thì**: Tốc độ chuyển hóa qua gan giảm dần và ổn định về mức của người trưởng thành.
- **Đa hình di truyền CYP2D6**: Codein và Tramadol là các tiền chất (prodrug) bắt buộc phải nhờ enzyme CYP2D6 tại gan chuyển hóa thành Morphin có hoạt tính giảm đau. Ở những trẻ mang kiểu gen siêu chuyển hóa (Ultra-rapid metabolizers), lượng Morphin được tạo ra ồ ạt trong thời gian ngắn gây ngộ độc opioid cấp, ức chế trung tâm hô hấp dẫn đến ngừng thở và tử vong, đặc biệt sau phẫu thuật nạo VA hoặc cắt amydale.

### 1.4 Khác biệt Thải trừ thận (E - Excretion) & Sự trưởng thành GFR
- **Độ lọc cầu thận lúc chào đời**: Ở trẻ sơ sinh đủ tháng, độ lọc cầu thận (GFR) chỉ đạt khoảng **20 đến 40 ml/phút/1.73 m²** (tương đương 25–30% giá trị người lớn). Ở trẻ non tháng, GFR thậm chí chỉ đạt 10–15 ml/phút/1.73 m².
- **Chức năng bài tiết và tái hấp thu ống thận**: Cả cơ chế vận chuyển bài tiết chủ động anion/cation hữu cơ và khả năng cô đặc nước tiểu của quai Henle đều chưa hoàn thiện. Trẻ sơ sinh bài tiết nước tiểu nhược trương và không thể cô đặc nước tiểu tối đa khi thiếu nước.
- **Tiến trình trưởng thành**: GFR tăng nhanh trong 2 tuần đầu sau sinh nhờ sự sụt giảm sức cản mạch máu thận và tăng tưới máu vỏ thận, sau đó đạt mức trưởng thành của người lớn (100–120 ml/phút/1.73 m²) vào lúc **1 đến 2 tuổi**.
- **Hệ quả lâm sàng sống còn**: Do GFR thấp, thời gian bán thải sinh học ($T_{1/2}$) của các thuốc đào thải chủ yếu qua thận (như Penicillin, Cephalosporin, Aminoglycosid, Vancomycin) ở trẻ sơ sinh kéo dài gấp 2 đến 4 lần người lớn.
  - *Ví dụ 3*: Gentamicin ở người lớn có $T_{1/2}$ khoảng 2 giờ và dùng cách mỗi 8 giờ. Ở trẻ sơ sinh đủ tháng, $T_{1/2}$ kéo dài 6–8 giờ → bắt buộc phải giãn khoảng cách đưa liều thành **mỗi 24 giờ (q24h)**. Ở trẻ sơ sinh non tháng cực nhẹ cân, $T_{1/2}$ kéo dài tới 12–18 giờ → khoảng cách liều phải giãn ra **mỗi 36 đến 48 giờ (q36–48h)**. Nếu dùng khoảng cách q8h như người lớn, nồng độ đáy của thuốc sẽ tích lũy vượt ngưỡng độc tính, hủy hoại ốc tai - tiền đình vĩnh viễn và hoại tử ống thận cấp.

---

## 2. CƠ CHẾ DƯỢC LÝ SINH LÝ BỆNH VÀ CÁC CHUỖI NHÂN QUẢ 5 TẦNG

Mọi tai biến kê đơn trong Nhi khoa đều bắt nguồn từ việc phá vỡ các ranh giới sinh lý học. Dưới đây là 5 chuỗi nhân quả cơ chế sâu sắc giải thích bản chất bệnh sinh của các ngộ độc và tương tác thuốc kinh điển:

### 2.1 Chuỗi 1: Cơ chế ngộ độc hoại tử tế bào gan cấp của Paracetamol khi vượt liều
- Quá liều Paracetamol (> 150 mg/kg trong 24h) → Bão hòa hoàn toàn hai con đường chuyển hóa an toàn chính tại gan là Sulfat hóa và Glucuronid hóa → Lượng thuốc tự do dư thừa bị chuyển hướng sang oxy hóa qua hệ enzyme Cytochrome P450 (chủ yếu CYP2E1) → Sản sinh ồ ạt chất chuyển hóa trung gian cực độc có tính oxy hóa cao là N-acetyl-p-benzoquinone imine (NAPQI) → Cạn kiệt nguồn Glutathione dự trữ nội bào tại tế bào gan → NAPQI tự do gắn đồng hóa trị vào nhóm sulfhydryl của các protein ty thể và màng tế bào gan → Hủy hoại màng ty thể, giải phóng canxi nội bào, hoại tử đông tế bào gan vùng trung tâm tiểu thùy (Zone 3) → Suy gan cấp tính, vàng da, hôn mê gan và rối loạn đông máu nặng.

### 2.2 Chuỗi 2: Cơ chế Ceftriaxone gây vàng da nhân não và kết tủa canxi ở sơ sinh
- Kê Ceftriaxone cho trẻ sơ sinh < 28 ngày tuổi → Phân tử Ceftriaxone có ái lực cực mạnh với Albumin huyết tương → Cạnh tranh trực tiếp và đẩy Bilirubin gián tiếp tự do ra khỏi vị trí gắn kết trên Albumin → Nồng độ Bilirubin tự do không phân cực trong máu tăng vọt → Bilirubin tự do ngấm qua hàng rào máu não lỏng lẻo chưa myelin hóa của sơ sinh → Lắng đọng độc tính tại nhân xám đáy não (thể vân, nhân đuôi) và đồi thị → Gây hội chứng Vàng da nhân não (Kernicterus) với biểu hiện li bì, bỏ bú, gồng ưỡn người, co giật và tử vong.
- Đồng thời: Ceftriaxone đào thải qua mật và nước tiểu, khi gặp ion Canxi trong máu hoặc trong dịch truyền (như Ringer Lactat, Calci gluconat) → Phản ứng tạo thành muối kết tủa không tan Ceftriaxone - Canxi → Lắng đọng vi tinh thể tại mao mạch phổi và cầu thận → Gây tắc mạch phổi cấp, suy hô hấp tối cấp và suy thận vô niệu dẫn đến tử vong.

### 2.3 Chuỗi 3: Cơ chế đột biến gen CYP2D6 siêu chuyển hóa gây tử vong của Codein
- Cho trẻ em < 12 tuổi uống Codein giảm đau sau mổ cắt amydale → Codein là tiền chất trơ, hấp thu vào máu đến gan → Gặp cá thể mang đa hình di truyền sao chép gen CYP2D6 thể siêu chuyển hóa (Ultra-rapid metabolizer) → Hoạt tính enzyme CYP2D6 tăng vọt gấp nhiều lần → Chuyển hóa tức thì Codein thành Morphin tinh khiết với nồng độ đỉnh trong huyết tương tăng cao đột ngột → Morphin vượt qua hàng rào máu não gắn chọn lọc vào thụ thể mu-opioid tại trung tâm hô hấp ở hành não → Ức chế tính nhạy cảm của trung tâm hô hấp với CO₂ → Giảm thông khí phế nang, thở chậm, ngừng thở trong giấc ngủ và tử vong do thiếu oxy não.

### 2.4 Chuỗi 4: Cơ chế mất phân cực màng tế bào cơ tim gây vô tâm thu khi Bolus nhanh Kali
- Điều dưỡng tiêm bolus tĩnh mạch trực tiếp ống Kali clorua 10% → Nồng độ ion K⁺ trong khoang ngoại bào và huyết tương tăng vọt tức thì (> 8–10 mmol/L) → Làm triệt tiêu gradien nồng độ ion K⁺ bình thường giữa nội bào và ngoại bào → Theo phương trình Nernst, điện thế nghỉ của màng tế bào cơ tim ($Em$) bị dịch chuyển về phía dương tính (mất phân cực màng) → Bất hoạt các kênh Natri nhanh phụ thuộc điện thế ($Nav1.5$) → Mất hoàn toàn khả năng phát sinh điện thế hoạt động và tính dẫn truyền của cơ tim → Xuất hiện sóng T cao nhọn đối xứng, phức bộ QRS giãn rộng hòa lẫn sóng T tạo dạng sóng hình sin → Ngừng tim đột ngột ở thì tâm trương với nhịp vô tâm thu (Asystole) trơ hoàn toàn với mọi nỗ lực ép tim hồi sức.

### 2.5 Chuỗi 5: Cơ chế ức chế Cyclooxygenase gây suy thận cấp và xuất huyết của NSAID trong Dengue
- Dùng Ibuprofen để hạ sốt cho trẻ mắc Sốt xuất huyết Dengue trong giai đoạn nguy hiểm (ngày 3–7) → NSAID ức chế không chọn lọc enzyme Cyclooxygenase (COX-1 và COX-2) → Giảm tổng hợp Prostaglandin $I_2$ ($PGI_2$) và Prostaglandin $E_2$ ($PGE_2$) tại tiểu động mạch đến của cầu thận → Co thắt tiểu động mạch đến, sụt giảm áp lực tưới máu cầu thận trong bối cảnh thể tích tuần hoàn đang bị thoát huyết tương → Suy thận cấp trước thận tiến triển nhanh thành hoại tử ống thận cấp.
- Đồng thời: Ức chế COX-1 tại tiểu cầu → Ngăn chặn tổng hợp Thromboxane $A_2$ ($TXA_2$) → Ức chế không hồi phục khả năng kết tập tiểu cầu → Trong bối cảnh số lượng tiểu cầu đang sụt giảm nặng do virus Dengue ức chế tủy xương và phá hủy ngoại vi → Gây xuất huyết tiêu hóa ồ ạt, nôn ra máu, đi ngoài phân đen và sốc xuất huyết tử vong.

---

## 3. CHẨN ĐOÁN VÀ QUY TRÌNH 5 BƯỚC TÍNH LIỀU THUỐC AN TOÀN

Để không bao giờ mắc sai sót khi kê đơn cho bệnh nhi, người bác sĩ phải rèn luyện quy trình 5 bước thành một phản xạ có điều kiện trước khi đặt bút ký đơn thuốc:

```text
                 QUY TRÌNH 5 BƯỚC TÍNH LIỀU THUỐC NHI AN TOÀN
                                       │
     ┌─────────────────────────┴─────────────────────────┐
     ▼                                                   ▼
[BƯỚC 1: CÂN NẶNG TRẺ]                       [BƯỚC 2: TRA CỨU LIỀU KHUYẾN CÁO]
Cân thật, trừ tã áo                          Xác định: mg/kg/LẦN hay /NGÀY?
Cấp cứu: Thước đo Broselow                   Chia mấy lần trong 24 giờ?
Ghi rõ kg góc trên đơn thuốc                 Nguồn guideline chuẩn (Bộ Y tế, WHO)
     │                                                   │
     └─────────────────────────┬─────────────────────────┘
                               ▼
               [BƯỚC 3: NHÂN CÂN NẶNG RA LIỀU LÝ THUYẾT]
               Liều (mg) = Liều chuẩn (mg/kg) x Cân nặng (kg)
               Tính cả liều mỗi lần VÀ tổng liều 24 giờ
               Rà soát lỗi dấu phẩy thập phân
                               │
                               ▼
               [BƯỚC 4: ĐỐI CHIẾU TRẦN LIỀU NGƯỜI LỚN]
               So sánh tổng liều tính được vs Trần người lớn
               LẤY GIÁ TRỊ NHỎ HƠN TRONG HAI SỐ!
               Trẻ >= 40 kg: Ngừng nhân liều, dùng trần
                               │
                               ▼
               [BƯỚC 5: QUY ĐỔI DẠNG BÀO CHẾ CÓ SẴN]
               Chọn dạng: Siro, Gói cốm, Viên đạn, Lọ tiêm
               Quy đổi ra thể tích (ml) hoặc số viên
               Viết đơn song song: HÀM LƯỢNG (mg) + THỂ TÍCH (ml)
```

### Bước 1: Cân trẻ — Cơ sở bất biến của mọi phép tính
- **Nguyên tắc**: Tuyệt đối không bao giờ dùng tuổi để suy diễn cân nặng và không ước lượng bằng mắt. Sai số cân nặng $\pm 20\%$ sẽ khuếch đại trực tiếp thành sai số liều lượng $\pm 20\%$.
- **Thực hành**: Cân trẻ khỏa thân hoặc chỉ mặc tã mỏng sạch trên cân điện tử đã chuẩn hóa. Luôn ghi rõ chỉ số cân nặng tính theo kilogam (đến 1 chữ số thập phân, ví dụ: 12.4 kg) ngay góc trên cùng của tờ đơn thuốc hoặc bệnh án.
- **Tình huống khẩn cấp**: Khi trẻ nguy kịch ngừng tim hoặc sốc nặng không thể cân, sử dụng **thước băng đo chiều dài Broselow** (Frush KS et al., PMID: 15466144) để quy đổi chiều dài cơ thể ra dải màu cân nặng và liều thuốc cấp cứu tương ứng, hoặc dùng công thức Luscombe/APLS: $\text{Cân nặng (kg)} = (3 \times \text{tuổi}) + 7$.

### Bước 2: Xác định chính xác bản chất liều khuyến cáo
- Đây là nguồn gốc của hơn 40% các ca ngộ độc thuốc trong nhi khoa.
- Bác sĩ phải trả lời rõ 4 câu hỏi:
  1. Liều khuyến cáo tính theo **mg/kg/LẦN** hay **mg/kg/NGÀY**?
  2. Nếu là liều theo ngày, thuốc được **chia làm mấy lần** trong 24 giờ?
  3. Đường dùng chỉ định là gì (Uống, Tiêm bắp, Tiêm tĩnh mạch chậm, Truyền tĩnh mạch)?
  4. Thuốc tính theo hoạt chất gốc hay dạng muối (ví dụ: Sắt nguyên tố vs Muối sắt sulfat; Ampicillin vs Ampicillin/Sulbactam)?
- *Ví dụ*:
  - Paracetamol: $10 - 15\text{ mg/kg/LẦN}$, mỗi 4–6 giờ (tối đa 4 lần/ngày).
  - Amoxicillin trong viêm phổi cộng đồng: $80 - 90\text{ mg/kg/NGÀY}$, chia 2 lần uống (tức mỗi lần $40 - 45\text{ mg/kg}$). Nếu đọc nhầm thành 90 mg/kg mỗi lần, bạn vừa cho trẻ uống liều gấp đôi!
  - Ceftriaxone: $50 - 100\text{ mg/kg/NGÀY}$, tiêm tĩnh mạch 1 lần duy nhất trong ngày.
  - Gentamicin: $5 - 7.5\text{ mg/kg/NGÀY}$, truyền tĩnh mạch 1 lần duy nhất trong ngày (ở trẻ ngoài giai đoạn sơ sinh).

### Bước 3: Nhân với cân nặng ra liều lý thuyết
- Áp dụng công thức:
  $$\text{Liều lý thuyết (mg)} = \text{Liều khuyến cáo (mg/kg)} \times \text{Cân nặng (kg)}$$
- Sau khi có liều lý thuyết, nếu là liều tính theo ngày, lấy tổng liều chia cho số lần dùng để ra liều mỗi lần.
- Tính toán đồng thời cả hai giá trị: **Liều mỗi lần (mg/lần)** và **Tổng liều 24 giờ (mg/ngày)** để chuẩn bị cho Bước 4.

### Bước 4: Đối chiếu trần liều người lớn — Bước sống còn bị lãng quên
- **Nguyên lý bất biến**: **"Liều tính theo cân nặng của một đứa trẻ không bao giờ được phép vượt quá liều tối đa hàng ngày của một người lớn khỏe mạnh"**.
- Luôn đặt hai con số cạnh nhau: $\text{Liều lý thuyết tính được}$ và $\text{Liều tối đa người lớn (Trần liều)}$.
- **Lấy giá trị NHỎ HƠN** trong hai giá trị trên để kê vào đơn thuốc.
- *Ví dụ phân tích bẫy*:
  - Một trẻ 11 tuổi nặng 45 kg bị viêm màng não mủ, phác đồ Ceftriaxone liều $100\text{ mg/kg/ngày}$.
  - Nếu nhân máy móc: $100 \times 45 = 4500\text{ mg/ngày} = 4.5\text{ g/ngày}$.
  - Trần liều Ceftriaxone tối đa của người lớn là $2000\text{ mg/ngày} = 2\text{ g/ngày}$ (trong viêm màng não tối đa có thể lên 4 g/ngày nhưng phác đồ chuẩn khuyến cáo không vượt 2 g/ngày trong đại đa số nhiễm khuẩn). Bạn vừa kê một liều gấp hơn 2 lần mức an toàn!
  - Hành động đúng: Chạm trần ở mức $2000\text{ mg/ngày}$ (hoặc 4000 mg/ngày nếu có hội chẩn chuyên khoa).

### Bước 5: Quy đổi dạng bào chế sẵn có & Viết đơn chống nhầm lẫn
- Quy đổi liều miligam (mg) ra thể tích mililit (ml) siro/hỗn dịch hoặc số lượng viên/gói:
  $$\text{Thể tích cần lấy (ml)} = \frac{\text{Liều cần dùng (mg)}}{\text{Hàm lượng trên nhãn (mg)}} \times \text{Thể tích trên nhãn (ml)}$$
- **Làm tròn thực hành**:
  - Dưới 1 ml: Dùng bơm tiêm 1 ml (chia vạch 0.01 ml), làm tròn đến 0.05 ml.
  - Từ 1 đến 5 ml: Dùng bơm tiêm 3 ml hoặc 5 ml, làm tròn đến 0.1 ml.
  - Trên 5 ml: Dùng cốc đong hoặc ống hút chia vạch ml, làm tròn đến 0.5 ml.
- **Quy tắc viết đơn song song**: Luôn viết cả hàm lượng (mg) và thể tích quy đổi (ml), ghi rõ nồng độ chế phẩm:
  - *Viết sai*: "Paracetamol 5 ml uống khi sốt" ➔ Vô cùng nguy hiểm vì trên thị trường có loại 120 mg/5 ml, 250 mg/5 ml và dung dịch giọt 100 mg/ml.
  - *Viết đúng*: "Paracetamol siro $120\text{ mg/5 ml}$ — Uống $6\text{ ml}$ ($= 144\text{ mg}$, tương đương $12\text{ mg/kg}$) mỗi 6 giờ khi sốt $\ge 38.5^\circ\text{C}$. Tối đa không quá 4 lần trong 24 giờ. Cân nặng: 12 kg."

---

## 4. THEO DÕI VÀ BẪY TRẦN LIỀU NGƯỜI LỚN — BẢNG TRA CỨU ĐIỂM CHẠM TRẦN

Khái niệm "Điểm chạm trần" (Cap threshold) là mốc cân nặng mà tại đó công thức nhân liều $mg/kg$ bắt đầu bằng hoặc vượt qua liều tối đa của người trưởng thành. Bác sĩ trực buồng bệnh bắt buộc phải thuộc lòng các điểm chạm trần sau:

| Tên thuốc | Chỉ định lâm sàng | Liều khuyến cáo nhi | Trần liều tối đa người lớn | Điểm chạm trần cân nặng | Hành vi kê đơn đúng khi vượt trần |
|---|---|---|---|:---:|---|
| **Ceftriaxone** | Nhiễm khuẩn nặng / Viêm phổi | $50 - 100\text{ mg/kg/ngày}$ | $2000\text{ mg/ngày}$ (2 g) | **20 kg** (ở liều 100 mg/kg) | Dừng ở mức 2 g/ngày tiêm 1 lần |
| **Dexamethasone** | Croup (Viêm thanh khí phế quản) | $0.15 - 0.6\text{ mg/kg}$ (liều duy nhất) | $10 - 12\text{ mg/liều}$ | **17 – 20 kg** (ở liều 0.6 mg/kg) | Dừng ở mức 10–12 mg uống 1 liều |
| **Prednisolone** | Cơn hen phế quản cấp | $1 - 2\text{ mg/kg/ngày}$ | $40 - 60\text{ mg/ngày}$ | **20 – 30 kg** (ở liều 2 mg/kg) | Dừng ở mức 40–60 mg/ngày |
| **Paracetamol** | Hạ sốt, giảm đau | $10 - 15\text{ mg/kg/lần}$ | $1000\text{ mg/lần}$ (1 g) & $4000\text{ mg/ngày}$ | **67 kg** (ở liều 15 mg/kg) | Dừng ở mức 1000 mg/lần, max 4 g/ngày |
| **Ibuprofen** | Hạ sốt, kháng viêm | $5 - 10\text{ mg/kg/lần}$ | $400\text{ mg/lần}$ & $1600 - 2400\text{ mg/ngày}$ | **40 kg** (ở liều 10 mg/kg) | Dừng ở mức 400 mg/lần, max 1.6 g/ngày |
| **Adrenaline** | Sốc phản vệ (Tiêm bắp sâu) | $0.01\text{ mg/kg}$ dung dịch 1:1000 | $0.3\text{ mg}$ (<30 kg) / $0.5\text{ mg}$ (≥30 kg) | **30 kg** (đổi bút 0.3 lên 0.5) | Trẻ ≥ 30 kg tiêm tối đa 0.5 ml (0.5 mg) |
| **Diazepam** | Cắt cơn co giật tĩnh mạch | $0.2 - 0.3\text{ mg/kg/lần}$ | $10\text{ mg/lần}$ | **33 kg** (ở liều 0.3 mg/kg) | Dừng ở mức 10 mg tiêm tĩnh mạch chậm |
| **Midazolam** | Cắt cơn co giật tĩnh mạch | $0.1 - 0.2\text{ mg/kg/lần}$ | $4 - 5\text{ mg/lần}$ | **25 kg** (ở liều 0.2 mg/kg) | Dừng ở mức 4–5 mg tiêm tĩnh mạch chậm |
| **Adenosin** | Cắt cơn tim nhanh trên thất (SVT) | $0.1\text{ mg/kg}$ liều 1; $0.2\text{ mg/kg}$ liều 2 | $6\text{ mg}$ (liều 1) / $12\text{ mg}$ (liều 2) | **60 kg** | Liều 1 tối đa 6 mg; liều 2 tối đa 12 mg |
| **Azithromycin** | Viêm phổi không điển hình | $10\text{ mg/kg}$ ngày 1; $5\text{ mg/kg}$ ngày 2–5 | $500\text{ mg}$ ngày 1; $250\text{ mg}$ ngày 2–5 | **50 kg** | Dùng liều cố định người lớn |

### Quy tắc Mốc cân nặng 40 kg & Kê đơn ở trẻ béo phì
- **Quy tắc 40 kg**: Khi một bệnh nhi đạt cân nặng từ **$\ge 40\text{ kg}$ trở lên** (thường rơi vào trẻ trên 10–12 tuổi), bác sĩ cần **ngừng tư duy nhân liều theo mg/kg thông thường** và chuyển sang kiểm tra bảng liều chuẩn của người lớn.
- **Tiếp cận trẻ thừa cân, béo phì**:
  - Mô mỡ thừa chứa rất ít nước (chỉ khoảng 10–20% so với 70% ở mô nạc).
  - Đối với các thuốc **tan trong nước (Hydrophilic)** như Aminoglycosid (Gentamicin, Amikacin), Vancomycin: Thể tích phân bố không tăng tương xứng với cân nặng thực tế (Total Body Weight - TBW). Nếu lấy TBW nhân liều, nồng độ thuốc trong huyết tương sẽ tăng vọt gây hoại tử ống thận cấp. Bắt buộc phải tính theo **Cân nặng lý tưởng (Ideal Body Weight - IBW)** hoặc **Cân nặng hiệu chỉnh (Adjusted Body Weight - ABW)**:
    $$ABW = IBW + 0.4 \times (TBW - IBW)$$
  - Đối với các thuốc **tan trong mỡ (Lipophilic)** như Diazepam, Midazolam: Thuốc phân bố rộng rãi vào mô mỡ, có thể tính theo TBW nhưng phải theo dõi sát nguy cơ kéo dài thời gian bán thải sinh học.

---

## 5. BẢN ĐỒ DƯỢC ĐIỂN 52 THUỐC NHI KHOA THỰC HÀNH THEO NHÓM

Dưới đây là bảng dữ liệu thực chiến của 52 hoạt chất cốt lõi nhất được sử dụng hàng ngày tại bệnh phòng và khoa cấp cứu Nhi:

### 5.1 Nhóm Hạ sốt – Giảm đau – Kháng viêm (02 thuốc)
1. **Paracetamol (Acetaminophen)**:
   - *Liều*: $10 - 15\text{ mg/kg/lần}$, mỗi 4–6 giờ khi sốt $\ge 38.5^\circ\text{C}$. Tối đa $60\text{ mg/kg/ngày}$ và không quá $4000\text{ mg/ngày}$.
   - *Dạng bào chế*: Gói bột 80 mg, 150 mg, 250 mg; Siro 120 mg/5 ml, 250 mg/5 ml; Dung dịch giọt 100 mg/ml; Viên đạn đặt hậu môn 80 mg, 150 mg, 300 mg; Chai truyền tĩnh mạch 10 mg/ml (100 ml).
   - *Bẫy lâm sàng*: Cộng dồn tất cả các chế phẩm chứa paracetamol (kể cả thuốc ho thảo dược hoặc viên đạn). Ngưỡng ngộ độc cấp tính khi dùng một liều $> 150\text{ mg/kg}$.
2. **Ibuprofen**:
   - *Liều*: $5 - 10\text{ mg/kg/lần}$, mỗi 6–8 giờ sau ăn no. Tối đa $40\text{ mg/kg/ngày}$ và không quá $1600 - 2400\text{ mg/ngày}$.
   - *Dạng bào chế*: Siro 100 mg/5 ml, 200 mg/5 ml; Viên nén 200 mg, 400 mg.
   - *Chống chỉ định tuyệt đối*: Trẻ dưới 6 tháng tuổi, Sốt xuất huyết Dengue, nôn ói mất nước, suy thận cấp, loét dạ dày tá tràng, sau mổ cắt amydale.

### 5.2 Nhóm Kháng sinh – Kháng virus – Kháng nấm (18 thuốc)
3. **Amoxicillin**: $25 - 90\text{ mg/kg/ngày}$, chia 2–3 lần uống. Viêm tai giữa và viêm phổi dùng liều cao $80 - 90\text{ mg/kg/ngày}$ để vượt MIC của phế cầu kháng thuốc. Dạng gói 250 mg; siro 125 mg/5 ml, 250 mg/5 ml; viên 500 mg. Trần 3000 mg/ngày.
4. **Amoxicillin / Acid Clavulanic**: Tính theo amoxicillin $40 - 90\text{ mg/kg/ngày}$, chia 2 lần. Phối hợp tỷ lệ 7:1 hoặc 14:1 (ít gây tiêu chảy hơn tỷ lệ 4:1). Siro 250 mg/5 ml, gói 250 mg, viên 875/125 mg. Trần 3000 mg amoxicillin/ngày.
5. **Ampicillin**: $100 - 200\text{ mg/kg/ngày}$ chia 4 lần tiêm tĩnh mạch. Nhiễm khuẩn sơ sinh và viêm màng não nghi Listeria liều $200 - 300\text{ mg/kg/ngày}$. Lọ tiêm 500 mg, 1 g. Trần 12 g/ngày.
6. **Cefotaxim**: $100 - 200\text{ mg/kg/ngày}$ chia 3–4 lần tiêm tĩnh mạch. Kháng sinh cephalosporin thế hệ 3 hàng đầu thay thế an toàn cho Ceftriaxone ở trẻ sơ sinh. Lọ 500 mg, 1 g. Trần 12 g/ngày.
7. **Ceftriaxone**: $50 - 100\text{ mg/kg/ngày}$ tiêm tĩnh mạch 1 lần duy nhất trong ngày. Chống chỉ định sơ sinh < 28 ngày tuổi. Lọ 500 mg, 1 g. Trần 2 g/ngày (chạm trần từ 20 kg).
8. **Cefazolin**: $50 - 100\text{ mg/kg/ngày}$ chia 3 lần tiêm tĩnh mạch. Kháng sinh thế hệ 1, dự phòng phẫu thuật và nhiễm tụ cầu nhạy methicillin. Lọ 1 g. Trần 6 g/ngày. Dễ nhầm với Cefotaxim (LASA).
9. **Cloxacillin**: $50 - 100\text{ mg/kg/ngày}$ chia 4 lần uống lúc đói hoặc tiêm tĩnh mạch. Đặc trị tụ cầu nhạy methicillin (MSSA). Nang 500 mg, lọ tiêm 500 mg, 1 g.
10. **Gentamicin**: $5 - 7.5\text{ mg/kg/ngày}$ truyền tĩnh mạch 1 lần duy nhất trong ngày (truyền trong 30–60 phút). Sơ sinh non tháng giãn cách liều mỗi 24–48 giờ. Ống 80 mg/2 ml, 40 mg/1 ml. Trần 500 mg/ngày. Độc tai và thận.
11. **Amikacin**: $15 - 20\text{ mg/kg/ngày}$ truyền tĩnh mạch 1 lần duy nhất trong ngày. Dùng cho nhiễm khuẩn gram âm kháng gentamicin. Ống 500 mg/2 ml. Trần 1500 mg/ngày.
12. **Azithromycin**: $10\text{ mg/kg}$ ngày đầu tiên, sau đó $5\text{ mg/kg/ngày}$ từ ngày 2 đến ngày 5 (uống 1 lần/ngày lúc đói). Gói 200 mg, hỗn dịch 200 mg/5 ml, viên 250 mg, 500 mg. Trần 500 mg ngày đầu.
13. **Clarithromycin**: $15\text{ mg/kg/ngày}$ chia 2 lần uống. Điều trị viêm phổi không điển hình và diệt H. pylori. Hỗn dịch 125 mg/5 ml, viên 250 mg, 500 mg. Trần 1000 mg/ngày.
14. **Vancomycin**: $40 - 60\text{ mg/kg/ngày}$ chia 4 lần truyền tĩnh mạch (mỗi lần truyền chậm tối thiểu $\ge 60\text{ phút}$). Chống chỉ định tiêm nhanh (hội chứng Red-man). Lọ 500 mg, 1 g. Trần 2 g/ngày.
15. **Meropenem**: $60 - 120\text{ mg/kg/ngày}$ chia 3 lần tiêm tĩnh mạch trong 30 phút. Nhiễm khuẩn gram âm đa kháng hoặc viêm màng não mủ (120 mg/kg). Lọ 500 mg, 1 g. Trần 6 g/ngày.
16. **Metronidazol**: $30\text{ mg/kg/ngày}$ chia 3 lần uống hoặc truyền tĩnh mạch. Đặc trị vi khuẩn kỵ khí và đơn bào (amip, giardia). Viên 250 mg, chai truyền 500 mg/100 ml. Trần 2 g/ngày.
17. **Co-trimoxazol (TMP-SMX)**: Tính theo TMP $6 - 8\text{ mg/kg/ngày}$ chia 2 lần uống. Chống chỉ định trẻ < 2 tháng tuổi. Viên 480 mg (TMP 80 mg), hỗn dịch 240 mg/5 ml (TMP 40 mg).
18. **Aciclovir (tiêm tĩnh mạch)**: $20\text{ mg/kg/lần}$ mỗi 8 giờ (tổng $60\text{ mg/kg/ngày}$), truyền tĩnh mạch chậm trong 1 giờ kèm bù đủ dịch tránh lắng đọng tinh thể ống thận. Đặc trị viêm não HSV. Lọ 250 mg, 500 mg.
19. **Oseltamivir**: Uống 2 lần/ngày trong 5 ngày. Liều theo cân nặng: $\le 15\text{ kg}: 30\text{ mg} \times 2$; $> 15 - 23\text{ kg}: 45\text{ mg} \times 2$; $> 23 - 40\text{ kg}: 60\text{ mg} \times 2$; $> 40\text{ kg}: 75\text{ mg} \times 2$. Viên nang 30 mg, 45 mg, 75 mg.
20. **Nystatin**: $100.000\text{ UI/lần} \times 4\text{ lần/ngày}$ rơ miệng sau ăn điều trị nấm miệng candida. Gói bột 100.000 UI, hỗn dịch 100.000 UI/ml. Không hấp thu qua ruột.

### 5.3 Nhóm Hô hấp – Croup – Hen phế quản (06 thuốc)
21. **Salbutamol khí dung**: Trẻ $< 25\text{ kg}: 2.5\text{ mg/lần}$ (1 ống 2.5 mg/2.5 ml); Trẻ $\ge 25\text{ kg}: 5\text{ mg/lần}$ (2 ống). Trong cơn hen nặng: Khí dung liên tục hoặc lặp lại mỗi 20 phút trong giờ đầu. Ống 2.5 mg/2.5 ml, bình xịt định liều MDI 100 µg/nhát.
22. **Ipratropium bromid khí dung**: Phối hợp Salbutamol trong 3 lần khí dung đầu của cơn hen nặng. Trẻ $< 6\text{ tuổi}: 0.25\text{ mg/lần}$; Trẻ $\ge 6\text{ tuổi}: 0.5\text{ mg/lần}$. Ống 0.25 mg/2 ml, 0.5 mg/2 ml.
23. **Adrenaline khí dung (trong Croup)**: Dung dịch Adrenaline 1:1000 liều $0.5\text{ ml/kg}$ (tối đa 5 ml) khí dung qua mặt nạ trong viêm thanh khí phế quản cấp trung bình - nặng. Co mạch giảm phù nề tức thì trong 30 phút.
24. **Dexamethasone**: $0.15 - 0.6\text{ mg/kg}$ uống hoặc tiêm bắp/tĩnh mạch 1 liều duy nhất trong Croup. Trần tối đa $10 - 12\text{ mg}$. Viên 0.5 mg, 4 mg; ống tiêm 4 mg/ml.
25. **Methylprednisolone**: $1 - 2\text{ mg/kg/ngày}$ tiêm tĩnh mạch trong cơn hen cấp nặng hoặc phản vệ. Lọ 40 mg, 125 mg. Trần 60 mg/ngày (chạm trần từ 30 kg).
26. **Prednisolone (uống)**: $1 - 2\text{ mg/kg/ngày}$ uống 1 lần buổi sáng sau ăn trong đợt cấp hen phế quản (dùng 3–5 ngày). Siro 15 mg/5 ml, viên 5 mg, 20 mg. Trần 40–60 mg/ngày.

### 5.4 Nhóm Cấp cứu – Hồi sức – Chống độc (14 thuốc)
27. **Adrenaline tiêm bắp (Sốc phản vệ)**: Ống nguyên vẹn 1:1000 ($1\text{ mg/1 ml}$). Liều $0.01\text{ mg/kg} = 0.01\text{ ml/kg}$ tiêm bắp sâu mặt trước-ngoài đùi. Trần: 0.3 mg (trẻ < 30 kg) và 0.5 mg (trẻ ≥ 30 kg).
28. **Adrenaline tiêm tĩnh mạch (Ngừng tim - PALS)**: Bắt buộc pha loãng thành dung dịch 1:10.000 ($1\text{ mg/10 ml}$): Lấy 1 ml ống 1:1000 + 9 ml NaCl 0.9%. Liều $0.1\text{ ml/kg}$ tiêm tĩnh mạch hoặc trong xương mỗi 3–5 phút.
29. **Amiodaron**: $5\text{ mg/kg}$ truyền tĩnh mạch chậm trong 20–60 phút trong rung thất hoặc nhanh thất vô mạch trơ sốc điện. Ống 150 mg/3 ml. Trần 300 mg/lần.
30. **Adenosin**: $0.1\text{ mg/kg}$ (tối đa 6 mg) tiêm tĩnh mạch cực nhanh < 5 giây tại chạc ba sát tĩnh mạch trung tâm + flush ngay 5–10 ml NaCl 0.9%. Liều 2: $0.2\text{ mg/kg}$ (tối đa 12 mg). Cắt cơn SVT. Ống 6 mg/2 ml.
31. **Atropin**: $0.02\text{ mg/kg}$ tiêm tĩnh mạch (liều tối thiểu 0.1 mg tránh nhịp chậm nghịch thường, trần 0.5 mg ở trẻ nhỏ, 1 mg ở trẻ lớn). Điều trị nhịp tim chậm do cường phó giao cảm. Ống 0.25 mg, 0.5 mg/ml.
32. **Natri bicarbonat 4.2%**: $1 - 2\text{ mmol/kg}$ tiêm tĩnh mạch chậm trong toan chuyển hóa nặng sau khi đã thông khí tốt hoặc tăng kali máu đe dọa ngừng tim. Ống 4.2% (1 ml = 0.5 mmol). Cấm dùng loại 8.4% cho sơ sinh.
33. **Calci gluconat 10%**: $0.5\text{ ml/kg}$ ($50\text{ mg/kg}$) tiêm tĩnh mạch chậm trong 5–10 phút dưới monitor theo dõi nhịp tim. Ổn định màng tế bào cơ tim khi tăng kali máu nặng. Ống 10% 10 ml. Trần 20 ml.
34. **Magnesi sulfat**: $25 - 50\text{ mg/kg}$ truyền tĩnh mạch chậm trong 20–30 phút trong cơn hen phế quản cấp nặng kháng trị hoặc xoắn đỉnh. Ống 15% 10 ml (150 mg/ml), ống 50%. Trần 2 g.
35. **Naloxon**: $0.1\text{ mg/kg}$ tiêm tĩnh mạch hoặc tiêm bắp (trần 2 mg/liều) đảo ngược ngộ độc ức chế hô hấp do opioid. Ống 0.4 mg/ml. Sơ sinh: 0.01 mg/kg.
36. **Furosemid**: $1\text{ mg/kg/lần}$ tiêm tĩnh mạch chậm trong phù phổi cấp, quá tải thể tích hoặc suy tim ứ huyết. Ống 20 mg/2 ml, viên 40 mg. Trần 40 mg/lần.
37. **Mannitol 20%**: $0.5 - 1\text{ g/kg} = 2.5 - 5\text{ ml/kg}$ truyền tĩnh mạch trong 20–30 phút qua bầu lọc trong phù não cấp dọa tụt kẹt. Chai 20% 250 ml.
38. **NaCl 3% (tăng trương)**: $2 - 5\text{ ml/kg}$ (chuẩn $3\text{ ml/kg}$) truyền tĩnh mạch trong 20–30 phút cắt cơn co giật do hạ Natri máu cấp tính. Mục tiêu nâng Na máu lên 4–6 mmol/L để cắt phù não.
39. **Glucose 10% (Cấp cứu hạ đường huyết)**: $2\text{ ml/kg} = 0.2\text{ g/kg}$ tiêm tĩnh mạch chậm trong 2–5 phút, sau đó duy trì ngay tốc độ truyền đường GIR. Tuyệt đối không dùng D30% hay D50% ở sơ sinh.
40. **N-acetylcystein (NAC)**: Giải độc Paracetamol phác đồ truyền tĩnh mạch 21 giờ: Liều tải $150\text{ mg/kg}$ trong 1 giờ → $50\text{ mg/kg}$ trong 4 giờ tiếp → $100\text{ mg/kg}$ trong 16 giờ tiếp (tổng liều 300 mg/kg). Lọ 2 g/10 ml.

### 5.5 Nhóm Tiêu hóa – Dinh dưỡng – Vi chất (06 thuốc)
41. **Ondansetron**: $0.15\text{ mg/kg/lần}$ tiêm tĩnh mạch chậm hoặc uống điều trị nôn ói cấp tính do viêm dạ dày ruột. Thuốc chống nôn an toàn hàng đầu thay thế Metoclopramid ở trẻ em. Ống 4 mg/2 ml, viên 4 mg. Trần 4 mg (<30 kg) và 8 mg (≥30 kg).
42. **Omeprazol**: $0.5 - 1\text{ mg/kg/ngày}$ uống trước ăn sáng 30 phút hoặc tiêm tĩnh mạch chậm. Lọ 40 mg, viên bao tan trong ruột 20 mg. Trần 40 mg/ngày.
43. **Kẽm (Zinc gluconat/sulfat)**: Bổ sung trong tiêu chảy cấp: Trẻ $< 6\text{ tháng}: 10\text{ mg/ngày}$; Trẻ $\ge 6\text{ tháng}: 20\text{ mg/ngày}$ uống trong 10–14 ngày liên tục. Tái tạo nhung mao ruột và giảm 25% tỷ lệ tái phát.
44. **ORS (Oresol áp lực thẩm thấu thấp)**: Phác đồ A (phòng mất nước tại nhà); Phác đồ B ($75\text{ ml/kg}$ trong 4 giờ tại cơ sở y tế); Phác đồ C (Ringer Lactat truyền tĩnh mạch). Pha đúng thể tích nước ghi trên gói.
45. **Vitamin A liều cao**: Điều trị bệnh sởi: Trẻ $< 6\text{ tháng}: 50.000\text{ UI}$; $6 - 11\text{ tháng}: 100.000\text{ UI}$; $\ge 12\text{ tháng}: 200.000\text{ UI}$ uống ngày 1, ngày 2 và nhắc lại sau 2–4 tuần. Giảm 50% tử vong do sởi.
46. **Sắt nguyên tố**: Điều trị thiếu máu thiếu sắt $3 - 6\text{ mg sắt nguyên tố/kg/ngày}$ chia 2–3 lần uống giữa hai bữa ăn. Bắt buộc quy đổi ra hàm lượng sắt nguyên tố trên nhãn.

### 5.6 Nhóm Thần kinh – Cắt cơn co giật (06 thuốc)
47. **Midazolam**: Cắt cơn co giật cấp: Tiêm tĩnh mạch $0.1 - 0.2\text{ mg/kg}$ (trần 4 mg); Nhỏ niêm mạc má hoặc xịt mũi $0.2 - 0.3\text{ mg/kg}$ (trần 10 mg). Lựa chọn hàng đầu trước viện. Ống 5 mg/ml.
48. **Diazepam**: Bơm hậu môn $0.5\text{ mg/kg}$ (ống 5 mg cho trẻ < 3 tuổi, ống 10 mg cho trẻ ≥ 3 tuổi); Tiêm tĩnh mạch chậm $0.2 - 0.3\text{ mg/kg}$ với tốc độ không quá 2 mg/phút tránh ngưng thở. Ống 10 mg/2 ml.
49. **Lorazepam**: $0.1\text{ mg/kg}$ tiêm tĩnh mạch chậm trong 2 phút (trần 4 mg). Tác dụng chống co giật kéo dài 12–24 giờ do ít tan trong mỡ hơn diazepam.
50. **Phenobarbital**: $15 - 20\text{ mg/kg}$ truyền tĩnh mạch chậm trong 20–30 phút (tốc độ $\le 1\text{ mg/kg/phút}$). Lựa chọn hàng đầu trong cắt cơn co giật sơ sinh. Ống 100 mg/ml, 200 mg/ml.
51. **Levetiracetam**: $40 - 60\text{ mg/kg}$ truyền tĩnh mạch trong 10–15 phút điều trị trạng thái động kinh kháng benzodiazepine. Không chuyển hóa qua CYP450, ít tương tác thuốc. Lọ 500 mg/5 ml. Trần 4500 mg.
52. **Phenytoin**: $15 - 20\text{ mg/kg}$ truyền tĩnh mạch chậm với tốc độ không quá $1\text{ mg/kg/phút}$ pha trong NaCl 0.9% dưới monitor theo dõi điện tim. Nguy cơ tụt huyết áp và loạn nhịp thất. Trần 1000 mg.

### 5.7 Bảng hướng dẫn 10 thuốc hồi sức truyền liên tục qua bơm tiêm điện
Khi truyền thuốc vận mạch và hồi sức, công thức quy đổi tốc độ chuẩn:
$$\text{Tốc độ truyền (ml/giờ)} = \frac{\text{Liều (mcg/kg/phút)} \times \text{Cân nặng (kg)} \times 60}{\text{Nồng độ dịch sau pha (mcg/ml)}}$$

| Tên thuốc | Dải liều chuẩn | Quy cách pha chuẩn nhi (trong bơm 50 ml) | Nồng độ dịch sau pha | Tác dụng dược lý chính |
|---|---|---|---|---|
| **Adrenaline** | $0.05 - 1\text{ mcg/kg/phút}$ | 3 mg ($3\text{ ống}$) + NaCl 0.9% vừa đủ 50 ml | $60\text{ mcg/ml}$ | Beta-1 (tăng co bóp), Alpha-1 (co mạch nâng HA) |
| **Noradrenaline** | $0.05 - 1\text{ mcg/kg/phút}$ | 4 mg ($4\text{ ống}$) + Dextrose 5% vừa đủ 50 ml | $80\text{ mcg/ml}$ | Alpha-1 mạnh (co mạch nâng HA trong sốc ấm) |
| **Dopamin** | $2 - 20\text{ mcg/kg/phút}$ | 200 mg ($1\text{ ống}$) + NaCl 0.9% vừa đủ 50 ml | $4000\text{ mcg/ml}$ | Liều thấp (dãn mạch thận), liều vừa (beta-1), liều cao (alpha-1) |
| **Dobutamin** | $2 - 20\text{ mcg/kg/phút}$ | 250 mg ($1\text{ lọ}$) + Dextrose 5% vừa đủ 50 ml | $5000\text{ mcg/ml}$ | Inotrope đơn thuần (tăng co bóp cơ tim trong sốc tim) |
| **Milrinon** | $0.25 - 0.75\text{ mcg/kg/phút}$ | 10 mg ($1\text{ ống}$) + Dextrose 5% vừa đủ 50 ml | $200\text{ mcg/ml}$ | Ức chế PDE-3: Inodilator (tăng co bóp + dãn mạch phổi) |
| **Insulin Regular (DKA)** | $0.05 - 0.1\text{ UI/kg/giờ}$ | 25 UI + NaCl 0.9% vừa đủ 50 ml (tráng dây 20 ml) | $0.5\text{ UI/ml}$ | Hạ đường huyết, chặn sinh toan ceton, không bolus |
| **Heparin** | $10 - 28\text{ UI/kg/giờ}$ | 1250 UI + NaCl 0.9% vừa đủ 50 ml | $25\text{ UI/ml}$ | Chống đông máu, chỉnh liều theo aPTT mục tiêu 60–85s |
| **Midazolam** | $0.5 - 5\text{ mcg/kg/phút}$ | 25 mg ($5\text{ ống}$) + NaCl 0.9% vừa đủ 50 ml | $500\text{ mcg/ml}$ | An thần duy trì máy thở, giãn cơ, chống co giật |
| **Fentanyl** | $0.5 - 3\text{ mcg/kg/phút}$ | 500 mcg ($5\text{ ống}$) + NaCl 0.9% vừa đủ 50 ml | $10\text{ mcg/ml}$ | Giảm đau hồi sức mạnh gấp 100 lần morphin |
| **Salbutamol TM** | $0.05 - 0.3\text{ mcg/kg/phút}$ | 500 mcg ($1\text{ ống}$) + Dextrose 5% vừa đủ 50 ml | $10\text{ mcg/ml}$ | Dãn phế quản trong hen nặng kháng khí dung |

---

## 6. DỊCH TRUYỀN, ĐIỆN GIẢI VÀ TỐC ĐỘ TRUYỀN TRONG NHI KHOA (ASCII)

```text
                 LƯU ĐỒ RA QUYẾT ĐỊNH DỊCH TRUYỀN TẠI BUỒNG BỆNH
                                         │
     ┌───────────────────────────────────┴───────────────────────────────────┐
     ▼                                                                       ▼
[CẤP CỨU — CÓ SỐC]                                          [NỘI TRÚ — DỊCH DUY TRÌ]
Mạch nhanh, CRT > 2s, tụt HA                                Nhịn ăn trước mổ, viêm ruột
Bolus tinh thể: NaCl 0.9% / RL                              Công thức Holliday-Segar (4-2-1)
20 ml/kg trong 10-20 phút                                   Dung dịch đẳng trương có Dextrose
(10 ml/kg nếu sốc tim/non tháng)                            (VD: D5% 1/2 NS hoặc D5% NS)
     │ [Đánh giá đáp ứng tuần hoàn]                                          │ [Kiểm soát nồng độ Natri]
     ▼ (Sau mỗi lần bolus dịch)                                              ▼ (Lựa chọn loại dịch truyền)
ĐÁNH GIÁ LẠI SAU MỖI BOLUS:                                  CẤM DÙNG D5% ĐƠN THUẦN:
- Cải thiện CRT, mạch, tri giác?                             ADH tăng sinh lý khi bệnh cấp
- Ran ẩm phổi, gan to? (Quá tải)                             Gây hạ Natri máu cấp, phù não
     │ [Hội tụ nguyên tắc điện giải]                                         │ [Chỉ định an toàn bổ sung K+]
     └───────────────────────────────────┬───────────────────────────────────┘
                                         ▼
                         [AN TOÀN BÙ KALI CLORUA TĨNH MẠCH]
                         - Chỉ bù khi ĐÃ CÓ NƯỚC TIỂU (> 1 ml/kg/h)
                         - Nồng độ ngoại vi: ≤ 40 mmol/L (0.3% KCl)
                         - Tốc độ truyền tối đa: ≤ 0.5 mmol/kg/giờ
                         - CẤM TIÊM BOLUS TĨNH MẠCH TRỰC TIẾP!
```

### 6.1 Công thức dịch duy trì Holliday-Segar (100/50/20 & Quy tắc 4-2-1)
Phương pháp Holliday-Segar (Pediatrics 1957, PMID: 13431307) dựa trên tỷ lệ tiêu hao năng lượng sinh lý: 1 ml nước cho mỗi 1 kcal chuyển hóa.
- **Tính tổng thể tích dịch duy trì trong 24 giờ**:
  - $10\text{ kg đầu tiên}$: $100\text{ ml/kg/ngày}$.
  - Từ $11\text{ đến }20\text{ kg}$: Cộng thêm $50\text{ ml/kg/ngày}$ cho mỗi kg vượt trên 10 kg.
  - Trên $20\text{ kg}$: Cộng thêm $20\text{ ml/kg/ngày}$ cho mỗi kg vượt trên 20 kg.
  - Tối đa: Không quá $2400 - 2500\text{ ml/ngày}$ (mức người lớn).
- **Tính tốc độ truyền theo giờ (Quy tắc 4-2-1)**:
  - $10\text{ kg đầu tiên}$: $4\text{ ml/kg/giờ}$.
  - Từ $11\text{ đến }20\text{ kg}$: Cộng thêm $2\text{ ml/kg/giờ}$ cho mỗi kg vượt trên 10 kg.
  - Trên $20\text{ kg}$: Cộng thêm $1\text{ ml/kg/giờ}$ cho mỗi kg vượt trên 20 kg.
  - *Ví dụ 4*: Trẻ nặng 14 kg:
    - Cách 1 (24 giờ): $(10 \times 100) + (4 \times 50) = 1000 + 200 = 1200\text{ ml/24 giờ} \rightarrow 1200 \div 24 = 50\text{ ml/giờ}$.
    - Cách 2 (Quy tắc 4-2-1): $(10 \times 4) + (4 \times 2) = 40 + 8 = 48\text{ ml/giờ}$ (làm tròn thực hành là 50 ml/giờ).

### 6.2 Quy đổi tốc độ truyền sang giọt/phút
$$\text{Số giọt/phút} = \frac{\text{Tốc độ truyền (ml/giờ)} \times \text{Hệ số giọt của dây (giọt/ml)}}{60\text{ phút}}$$
- **Dây truyền dịch tiêu chuẩn người lớn (Hệ số giọt = 20 giọt/ml)**:
  $$\text{Số giọt/phút} = \frac{\text{Tốc độ (ml/giờ)}}{3}$$
  (Ví dụ: Cài đặt 60 ml/giờ $\rightarrow 60 \div 3 = 20\text{ giọt/phút}$).
- **Dây truyền dịch nhi khoa / Dây vi giọt buret (Hệ số giọt = 60 giọt/ml)**:
  $$\text{Số giọt/phút} = \text{Tốc độ (ml/giờ)}$$
  (Ví dụ: Cài đặt 50 ml/giờ $\rightarrow$ đếm đúng $50\text{ giọt/phút}$ trên bầu đếm).

### 6.3 Tốc độ truyền Glucose (GIR) & Xử trí hạ đường huyết sơ sinh
- Sơ sinh có khối lượng não bộ chiếm tới 10% trọng lượng cơ thể và mức tiêu thụ glucose của não cực kỳ cao.
- **Công thức tính GIR**:
  $$\text{GIR (mg/kg/phút)} = \frac{\text{Nồng độ Dextrose (\%)} \times \text{Tốc độ dịch (ml/giờ)}}{6 \times \text{Cân nặng (kg)}}$$
- **Mục tiêu duy trì**: Sơ sinh đủ tháng cần GIR từ **$4 - 8\text{ mg/kg/phút}$**. Trẻ non tháng có thể cần $6 - 10\text{ mg/kg/phút}$.
- **Xử trí hạ đường huyết sơ sinh (< 2.6 mmol/L hay < 47 mg/dL)**:
  1. *Mini-bolus khẩn cấp*: Glucose 10% liều $2\text{ ml/kg}$ ($= 0.2\text{ g/kg}$) tiêm tĩnh mạch chậm trong 2–5 phút.
  2. *Duy trì tức thì*: Bắt đầu truyền dung dịch Glucose 10% với tốc độ đáp ứng GIR $6 - 8\text{ mg/kg/phút}$.
  3. Kiểm tra lại đường huyết mao mạch sau 30 phút. Tuyệt đối không dùng dung dịch Glucose 30% hay 50%.

### 6.4 Ba nguyên tắc vàng khi bù Kali clorua (KCl) tĩnh mạch
1. **Chỉ thêm Kali khi đã có nước tiểu**: Phải xác nhận bệnh nhi có lưu lượng nước tiểu $\ge 1\text{ ml/kg/giờ}$. Nếu thận vô niệu, lượng Kali đưa vào sẽ gây tăng kali máu tử vong.
2. **Nồng độ ngoại vi tối đa $\le 40\text{ mmol/L}$ (0.3% KCl)**: Nồng độ cao hơn gây viêm tĩnh mạch hoại tử mô. Đường truyền tĩnh mạch trung tâm có thể pha đến 60–80 mmol/L.
3. **Tốc độ truyền tối đa $\le 0.5\text{ mmol/kg/giờ}$**: Luôn truyền qua bơm tiêm điện hoặc máy truyền dịch có kiểm soát và gắn monitor theo dõi điện tim liên tục.
4. **Quy đổi hóa học**: **$1\text{ g KCl} = 13.4\text{ mmol K⁺}$** (không phải 10 mmol).

---

## 7. BẢNG 24 THUỐC CHỐNG CHỈ ĐỊNH VÀ CẢNH BÁO NGUY HIỂM THEO TUỔI

| Tên thuốc | Độ tuổi / Hoàn cảnh chống chỉ định | Hậu quả cơ chế sinh học | Thuốc thay thế an toàn |
|---|---|---|---|
| **Aspirin** | Trẻ < 16 tuổi mắc cúm / thủy đậu | Gây **Hội chứng Reye**: thoái hóa mỡ gan cấp tính, suy tế bào gan và phù não nhiễm độc tử vong | Paracetamol (10–15 mg/kg) |
| **Codein** | Trẻ < 12 tuổi; sau nạo VA/cắt amydale | Đa hình CYP2D6 siêu chuyển hóa tạo Morphin ồ ạt gây ngưng thở tử vong | Paracetamol, Ibuprofen |
| **Tramadol** | Trẻ < 12 tuổi | Đột biến gen CYP2D6 gây ngộ độc opioid cấp tính, suy hô hấp ngừng thở | Paracetamol, Ibuprofen |
| **Ceftriaxone** | Sơ sinh < 28 ngày tuổi; dùng kèm Canxi | Đẩy Bilirubin gây vàng da nhân não; kết tủa tinh thể Ceftriaxone-Canxi ở phổi và thận | **Cefotaxim** (100–200 mg/kg/ngày) |
| **Promethazin** | Trẻ < 2 tuổi | Ức chế trung tâm hô hấp gây ngưng thở đột ngột trong giấc ngủ; hội chứng ngoại tháp | Kháng histamin H1 thế hệ 2 |
| **Loperamid** | Trẻ < 2 tuổi (không khuyên dùng < 6t) | Liệt ruột cơ năng, chướng bụng hoại tử, nhiễm độc toàn thân và che giấu mất nước | Bù ORS + Bổ sung Kẽm |
| **Thuốc ho/cảm OTC** | Trẻ < 6 tuổi | Chứa Dextromethorphan, Phenylephrin gây co giật, nhịp nhanh, ảo giác, tử vong | Rửa mũi NaCl 0.9%, mật ong (>1 tuổi) |
| **Tetracyclin** | Trẻ < 8 tuổi | Chelat hóa Canxi photphat làm hỏng men răng vĩnh viễn (răng xỉn màu vàng/nâu) và chậm phát triển xương | Amoxicillin, Macrolid |
| **Fluoroquinolon** | Trẻ < 18 tuổi (hạn chế thường quy) | Gây tổn thương và thoái hóa sụn khớp ở sụn tiếp hợp; đứt gân Achilles | Beta-lactam, Aminoglycosid |
| **Chloramphenicol** | Trẻ sơ sinh | Enzyme UGT chưa hoàn thiện gây tích lũy thuốc dẫn đến **Hội chứng xám (Grey baby)** | Ampicillin, Cefotaxim |
| **Co-trimoxazole** | Trẻ < 2 tháng tuổi | Cạnh tranh gắn Albumin đẩy Bilirubin tự do gây vàng da nhân não (Kernicterus) | Ampicillin, Amoxicillin |
| **Dextrose 30% - 50%** | Trẻ sơ sinh | Áp lực thẩm thấu cực cao gây xuất huyết não thất sơ sinh và hạ đường huyết phản ứng | **Glucose 10%** (2 ml/kg) |
| **Kali clorua Bolus** | Mọi lứa tuổi | Mất phân cực màng tế bào cơ tim, rung thất và vô tâm thu ngừng tim tức thì | Pha loãng truyền tĩnh mạch chậm |
| **Bicarbonat thường quy** | Ngừng tim PALS chưa thông khí | Sinh CO₂ nội bào khuếch tán nhanh vào tế bào não làm nặng thêm toan nội bào | Thông khí áp lực dương hiệu quả |
| **Propofol kéo dài** | Trẻ em hồi sức thở máy | Gây **Hội chứng truyền Propofol (PRIS)**: toan lactic, ly giải cơ vân, suy tim | Midazolam, Fentanyl |
| **Ibuprofen trong Dengue**| Sốt xuất huyết nghi ngờ / xác định | Ức chế kết tập tiểu cầu + ức chế tưới máu thận gây xuất huyết tiêu hóa và suy thận | Paracetamol đơn thuần |
| **Vincristin tủy sống** | Mọi lứa tuổi (chỉ được tiêm TM) | Gây viêm não - tủy hoại tử tiến triển, tử vong 100% | Bắt buộc dán nhãn cảnh báo đỏ |
| **Valproat natri** | Trẻ < 2 tuổi | Nguy cơ độc gan tối cấp gây hoại tử tế bào gan do khiếm khuyết chu trình chuyển hóa ty thể | Levetiracetam, Topiramat |
| **Naphazolin nhỏ mũi** | Trẻ sơ sinh và trẻ nhũ nhi | Hấp thu toàn thân qua niêm mạc mũi gây co mạch dữ dội, tụt thân nhiệt, hôn mê | Nước muối sinh lý NaCl 0.9% |
| **Ciprofloxacin nhỏ tai**| Trẻ thủng màng nhĩ (dạng phối hợp) | Độc tính ốc tai - tiền đình nếu thuốc chứa tá dược cồn hoặc corticoid không thích hợp | Thuốc nhỏ tai chuyên dụng vô khuẩn |
| **Metoclopramid** | Trẻ nhỏ | Gây hội chứng ngoại tháp cấp tính: cơn quay mắt, co cứng cổ, loạn trương lực cơ | **Ondansetron** (0.15 mg/kg) |
| **Dịch D5% đơn thuần** | Dịch truyền duy trì bệnh cấp | Thiếu Natri trong bối cảnh ADH tăng tiết gây hạ Natri máu cấp tính, phù não co giật | Dịch đẳng trương có Natri |
| **Corticoid bôi rộng** | Trẻ sơ sinh và nhũ nhi | Da mỏng hấp thu toàn thân gây ức chế trục hạ đồi - tuyến yên - thượng thận (HPA) | Dưỡng ẩm, Corticoid nhẹ ngắn ngày |
| **Paracetamol + Viên đạn**| Kê đồng thời siro và viên đạn | Phụ huynh dùng song song gây quá liều Paracetamol dẫn đến hoại tử tế bào gan cấp | Chỉ chọn 1 đường dùng duy nhất |

---

## 8. MƯỜI BỐN CẠM BẪY KÊ ĐƠN KINH ĐIỂN VÀ VÍ DỤ ĐƠN SAI

Dưới đây là 14 ca bẫy kê đơn kinh điển đối chiếu trực diện đơn sai và đơn đúng nhằm triệt tiêu các sai lầm và ngộ nhận trong thực hành lâm sàng:

### Cạm bẫy 1: Thiếu số 0 trước dấu phẩy thập phân (Leading Zero Trap)
- ❌ **Đơn sai**: `Midazolam .5 mg tiêm tĩnh mạch chậm khi co giật`.
- 🔍 **Ngộ nhận**: Dấu chấm nhỏ bị mờ hoặc nét chữ viết tay vội khiến điều dưỡng đọc thành `Midazolam 5 mg` (liều gấp 10 lần) ➔ Trẻ ngưng thở lập tức.
- ✅ **Đơn đúng**: `Midazolam 0,5 mg tiêm tĩnh mạch chậm trong 2 phút`. Luôn có số 0 dẫn đầu.

### Cạm bẫy 2: Thừa số 0 sau dấu phẩy thập phân (Trailing Zero Trap)
- ❌ **Đơn sai**: `Furosemid 20.0 mg tiêm tĩnh mạch chậm`.
- 🔍 **Ngộ nhận**: Dấu chấm bị mờ biến đơn thành `200 mg` (gấp 10 lần) ➔ Điếc không hồi phục và trụy mạch do mất nước cấp.
- ✅ **Đơn đúng**: `Furosemid 20 mg tiêm tĩnh mạch chậm`. Tuyệt đối không viết số 0 thừa sau số nguyên.

### Cạm bẫy 3: Chỉ ghi thể tích (ml) mà không ghi hàm lượng (mg)
- ❌ **Đơn sai**: `Paracetamol siro: uống 5 ml mỗi 6 giờ khi sốt`.
- 🔍 **Ngộ nhận**: Phụ huynh ra nhà thuốc mua chai siro nồng độ 250 mg/5 ml (thay vì loại 120 mg/5 ml) nhưng vẫn cho uống 5 ml ➔ Trẻ 10 kg nhận 25 mg/kg mỗi lần (quá liều).
- ✅ **Đơn đúng**: `Paracetamol siro 120 mg/5 ml: uống 5 ml (= 120 mg, tương đương 12 mg/kg) mỗi 6 giờ khi sốt ≥ 38.5°C`.

### Cạm bẫy 4: Kê đồng thời siro uống và viên đạn đặt hậu môn
- ❌ **Đơn sai**: Kê Paracetamol siro uống ban ngày và cho thêm viên đạn đặt hậu môn ban đêm "cho tiện".
- 🔍 **Ngộ nhận**: Trẻ sốt cao không hạ, phụ huynh vừa cho uống siro xong 30 phút sau thấy chưa hạ sốt liền nhét thêm viên đạn ➔ Tổng liều vượt 150 mg/kg/ngày gây suy gan cấp.
- ✅ **Đơn đúng**: Chỉ kê 1 đường dùng duy nhất. Dặn rõ: "Nếu trẻ nôn ói không uống được thì mới dùng viên đạn, tuyệt đối không dùng cả hai loại cùng một ngày".

### Cạm bẫy 5: Bỏ qua bẫy trần liều người lớn ở trẻ lớn
- ❌ **Đơn sai**: Bệnh nhi 12 tuổi nặng 45 kg bị viêm phổi thùy, kê `Ceftriaxone 100 mg/kg x 45 kg = 4.5 g/ngày`.
- 🔍 **Ngộ nhận**: Nhân máy móc theo kg mà quên mất trần liều người lớn của Ceftriaxone là 2 g/ngày.
- ✅ **Đơn đúng**: `Ceftriaxone 2 g tiêm tĩnh mạch 1 lần/ngày (Chạm trần liều người lớn)`.

### Cạm bẫy 6: Ước lượng cân nặng bệnh nhi bằng mắt
- ❌ **Đơn sai**: Nhìn một trẻ phù to hoặc béo phì ước chừng "chắc khoảng 15 kg" rồi tính liều.
- 🔍 **Ngộ nhận**: Sai số cân nặng thực tế lên tới 30–40%, dẫn đến kê thiếu liều kháng sinh hoặc ngộ độc thuốc gây mê.
- ✅ **Đơn đúng**: Bắt buộc cân trẻ trên cân chuẩn. Nếu cấp cứu không cân được, dùng thước đo chiều dài Broselow.

### Cạm bẫy 7: Dùng thìa cà phê gia đình để đong siro
- ❌ **Đơn sai**: Dặn phụ huynh "cho cháu uống 1 thìa cà phê siro ho".
- 🔍 **Ngộ nhận**: Thể tích thìa gia đình dao động thực tế từ 2.5 ml đến 7 ml, gây sai liều nghiêm trọng.
- ✅ **Đơn đúng**: Cấp xilanh hoặc cốc đong có vạch ml: "Dùng xilanh hút đúng 3 ml siro cho cháu uống".

### Cạm bẫy 8: Nhầm lẫn nồng độ Adrenaline trong cấp cứu
- ❌ **Đơn sai**: Bệnh nhân phản vệ còn mạch, lấy ống Adrenaline 1:1000 tiêm tĩnh mạch trực tiếp.
- 🔍 **Ngộ nhận**: Co mạch vành, tăng huyết áp kịch phát gây phù phổi cấp và xuất huyết não.
- ✅ **Đơn đúng**: Tiêm bắp sâu mặt ngoài đùi bằng ống nguyên vẹn 1:1000 liều 0.01 ml/kg. Tiêm tĩnh mạch chỉ dùng khi ngừng tuần hoàn và phải pha loãng 1:10.000.

### Cạm bẫy 9: Tiêm bolus Kali clorua qua tĩnh mạch
- ❌ **Đơn sai**: Thấy Kali máu 2.8 mmol/L, lấy ống KCl 10% tiêm tĩnh mạch chậm cho nhanh lên.
- 🔍 **Ngộ nhận**: Nồng độ kali ngoại bào tăng đột ngột làm mất điện thế nghỉ tế bào cơ tim ➔ Vô tâm thu ngừng tim tử vong.
- ✅ **Đơn đúng**: Pha loãng vào chai dịch truyền sao cho nồng độ ≤ 40 mmol/L, truyền tốc độ ≤ 0.5 mmol/kg/giờ qua máy truyền dịch.

### Cạm bẫy 10: Dùng Glucose 30% hay 50% cấp cứu sơ sinh
- ❌ **Đơn sai**: Trẻ sơ sinh hạ đường huyết 1.8 mmol/L, tiêm tĩnh mạch Glucose 30%.
- 🔍 **Ngộ nhận**: Nồng độ ưu trương làm xuất huyết não thất và kích thích tụy phóng insulin gây tụt đường tái phát.
- ✅ **Đơn đúng**: Chỉ dùng Glucose 10% tiêm tĩnh mạch chậm 2 ml/kg trong 2–5 phút, sau đó duy trì tốc độ GIR.

### Cạm bẫy 11: Truyền Vancomycin quá nhanh
- ❌ **Đơn sai**: Y lệnh truyền chai Vancomycin 500 mg trong 20 phút.
- 🔍 **Ngộ nhận**: Phóng thích histamin ồ ạt không qua IgE gây hội chứng người đỏ (Red-man syndrome) và tụt huyết áp.
- ✅ **Đơn đúng**: Pha loãng nồng độ ≤ 5 mg/ml và truyền chậm tối thiểu trong thời gian $\ge 60\text{ phút}$.

### Cạm bẫy 12: Nghiền viên nén phóng thích kéo dài
- ❌ **Đơn sai**: Nghiền viên Depakine Chrono 500 mg chia làm 4 phần cho trẻ 10 kg uống.
- 🔍 **Ngộ nhận**: Phá hủy khung bao phóng thích chậm làm giải phóng ồ ạt dược chất (dose dumping) gây ngộ độc cấp.
- ✅ **Đơn đúng**: Chuyển sang dạng siro Depakine dung dịch uống chia liều bằng xilanh chuyên dụng.

### Cạm bẫy 13: Kê Ibuprofen trong sốt xuất huyết Dengue
- ❌ **Đơn sai**: Thấy trẻ sốt cao 39.5°C không hạ, kê phối hợp Ibuprofen siro.
- 🔍 **Ngộ nhận**: Ức chế kết tập tiểu cầu trên nền tảng giảm tiểu cầu do Dengue ➔ Xuất huyết tiêu hóa ồ ạt.
- ✅ **Đơn đúng**: Tuyệt đối chỉ dùng Paracetamol 10–15 mg/kg mỗi 4–6 giờ kết hợp chườm ấm lau mát.

### Cạm bẫy 14: Kê Ceftriaxone cho trẻ sơ sinh < 28 ngày tuổi
- ❌ **Đơn sai**: Trẻ sơ sinh 10 ngày tuổi sốt nghi nhiễm khuẩn huyết, kê Ceftriaxone 80 mg/kg/ngày.
- 🔍 **Ngộ nhận**: Ceftriaxone đẩy Bilirubin gây vàng da nhân não và kết tủa với canxi máu.
- ✅ **Đơn đúng**: Kê Cefotaxim 100–150 mg/kg/ngày chia 3 lần hoặc phối hợp Ampicillin + Gentamicin.

---

## 9. ĐIỂM DỪNG TỰ KIỂM TRA (CHECKPOINTS)

Người học hãy tự giải quyết 5 bài toán lâm sàng tại các điểm dừng kiểm tra sau đây trước khi bước vào ca lâm sàng:

- **Checkpoint 1 (Tính liều siro kháng sinh)**: Một bệnh nhi 18 tháng tuổi, nặng 11 kg, được chẩn đoán viêm tai giữa cấp. Bác sĩ chỉ định Amoxicillin liều cao 90 mg/kg/ngày chia 2 lần uống. Kho dược bệnh viện hiện có sẵn chai Amoxicillin dạng hỗn dịch $250\text{ mg/5 ml}$. Hãy tính: Liều mỗi lần uống (mg) và thể tích siro cần lấy cho mỗi lần uống (ml)?
  - *Đáp án Checkpoint 1*: Tổng liều 24 giờ = $90 \times 11 = 990\text{ mg/ngày}$. Liều mỗi lần = $990 \div 2 = 495\text{ mg/lần}$ (làm tròn thực hành là 500 mg/lần). Thể tích siro mỗi lần = $(495 \div 250) \times 5 = 9.9\text{ ml}$ (làm tròn là **$10\text{ ml/lần}$**, ngày uống 2 lần cách nhau 12 giờ).

- **Checkpoint 2 (Kiểm tra bẫy trần liều Ceftriaxone)**: Một trẻ 10 tuổi, nặng 35 kg, bị viêm phổi cộng đồng mức độ nặng có chỉ định dùng Ceftriaxone tĩnh mạch liều 80 mg/kg/ngày. Liều khuyến cáo tối đa hàng ngày của Ceftriaxone ở người lớn là 2000 mg/ngày. Bác sĩ nên ra y lệnh liều Ceftriaxone cho bệnh nhi này là bao nhiêu?
  - *Đáp án Checkpoint 2*: Phép tính lý thuyết = $80 \times 35 = 2800\text{ mg/ngày}$. So sánh với trần liều người lớn: $2800\text{ mg} > 2000\text{ mg}$. Bác sĩ bắt buộc phải áp dụng trần liều: Kê **$2000\text{ mg/ngày}$ (tương đương 2 g/ngày tiêm tĩnh mạch 1 lần duy nhất)**.

- **Checkpoint 3 (Liều Adrenaline tiêm bắp phản vệ)**: Một trẻ nhũ nhi 7 tháng tuổi, nặng 8 kg, xuất hiện mày đay toàn thân, thở rít thanh quản và tím tái sau khi tiêm vắc xin (Phản vệ độ III). Hãy chọn nồng độ ống Adrenaline, đường tiêm, vị trí tiêm và thể tích thuốc cần lấy chính xác?
  - *Đáp án Checkpoint 3*: Dùng ống nguyên vẹn nồng độ **$1:1000$ ($1\text{ mg/1 ml}$)**. Liều tính theo công thức: $0.01\text{ ml/kg} \times 8\text{ kg} = \mathbf{0.08\text{ ml}}$ ($= 0.08\text{ mg}$). Dùng xilanh 1 ml chia vạch 0.01 ml để lấy đúng 0.08 ml. Tiêm bắp sâu tại **mặt trước-ngoài đùi (cơ rộng ngoài)**.

- **Checkpoint 4 (Tính dịch duy trì Holliday-Segar & tốc độ giọt)**: Một bệnh nhi nặng 16 kg cần nhịn ăn trước phẫu thuật ruột thừa và được chỉ định truyền dịch duy trì tốc độ 100%. Khoa sử dụng bộ dây truyền dịch tiêu chuẩn 20 giọt/ml. Hãy tính tốc độ truyền theo ml/giờ và số giọt/phút cần đếm trên bầu đếm?
  - *Đáp án Checkpoint 4*: Thể tích 24 giờ = $(10 \times 100) + (6 \times 50) = 1000 + 300 = 1300\text{ ml/24 giờ}$. Tốc độ ml/giờ = $1300 \div 24 \approx \mathbf{54\text{ ml/giờ}}$ (hoặc tính theo 4-2-1: $[10 \times 4] + [6 \times 2] = 40 + 12 = 52\text{ ml/giờ}$). Quy đổi giọt/phút với dây 20 giọt/ml: $54 \div 3 = \mathbf{18\text{ giọt/phút}}$.

- **Checkpoint 5 (Tốc độ truyền Glucose sơ sinh - GIR)**: Một trẻ sơ sinh 2 ngày tuổi, nặng 3 kg, đang được truyền dung dịch Glucose 10% với tốc độ 9 ml/giờ qua bơm tiêm điện. Tốc độ truyền glucose (GIR) của bệnh nhi này hiện tại là bao nhiêu mg/kg/phút và có nằm trong dải sinh lý bình thường không?
  - *Đáp án Checkpoint 5*: $\text{GIR} = (10 \times 9) \div (6 \times 3) = 90 \div 18 = \mathbf{5\text{ mg/kg/phút}}$. Con số này hoàn toàn nằm trong dải sinh lý chuẩn của trẻ sơ sinh ($4 - 8\text{ mg/kg/phút}$).

---

## 10. BỐN CA LÂM SÀNG PHÂN TÍCH 5 BƯỚC CÓ LỜI GIẢI CHI TIẾT

### Case 1: Trẻ 22 kg viêm phổi thùy — Bẫy trần liều Ceftriaxone & pha tiêm
- **Bệnh cảnh**: Bệnh nhi nam, 6 tuổi, nặng 22 kg, vào viện vì sốt cao liên tục 4 ngày, ho đờm nhiều, thở nhanh 38 lần/phút, X-quang phổi có hình ảnh đông đặc thùy dưới phổi phải. Chẩn đoán: Viêm phổi thùy mắc phải cộng đồng mức độ nặng. Bác sĩ chỉ định dùng Ceftriaxone tiêm tĩnh mạch liều cao 100 mg/kg/ngày.
- **Lời giải cụ thể theo 5 bước tiếp cận cho ca 1 (Viêm phổi)**:
  - *Bước 1 (Cân nặng)*: Cân thực tế là 22 kg. Ghi rõ "Cân nặng: 22 kg" vào bệnh án.
  - *Bước 2 (Bản chất liều)*: Liều khuyến cáo là $100\text{ mg/kg/ngày}$, tiêm tĩnh mạch 1 lần/ngày.
  - *Bước 3 (Nhân cân nặng)*: Liều lý thuyết = $100 \times 22 = 2200\text{ mg/ngày}$.
  - *Bước 4 (Đối chiếu trần liều)*: Trần liều người lớn tối đa của Ceftriaxone là $2000\text{ mg/ngày}$ (2 g). So sánh: $2200\text{ mg} > 2000\text{ mg}$. Bác sĩ bắt buộc phải áp dụng trần liều là **2000 mg/ngày (2 g)**.
  - *Bước 5 (Quy đổi & Viết y lệnh)*: Kho dược có lọ bột Ceftriaxone 1 g. Cần 2 lọ. Pha mỗi lọ 1 g với 9.6 ml nước cất (được 10 ml dung dịch 100 mg/ml), tiêm tĩnh mạch chậm trong 3–5 phút hoặc pha vào 50 ml NaCl 0.9% truyền trong 30 phút.
  - ✍️ **Y lệnh hoàn chỉnh**:  
    `Ceftriaxone lọ bột 1 g: 02 lọ (tổng liều 2000 mg = 2 g). Pha loãng tiêm tĩnh mạch chậm 1 lần/ngày lúc 08h00. (Chạm trần liều người lớn. Cân nặng: 22 kg)`.

### Case 2: Trẻ 8 kg phản vệ độ III — Xử trí tức thì Adrenaline bắp đùi ngoài
- **Bệnh cảnh**: Bé gái 9 tháng tuổi, nặng 8 kg, tiền căn khỏe mạnh. Sau khi uống siro kháng sinh Amoxicillin tại nhà 15 phút, trẻ đột ngột nổi ban đỏ mày đay khắp người, môi sưng phù, thở rít thanh quản nghe rõ khi nằm yên, SpO₂ giảm còn 88%, tay chân lạnh, CRT 3 giây, nhịp tim nhanh 175 lần/phút. Chẩn đoán: Sốc phản vệ độ III nguy kịch đe dọa tính mạng.
- **Phân tích phương án cấp cứu phản vệ ca 2 theo từng bước**:
  - *Bước 1 (Cân nặng)*: Trẻ nguy kịch, mẹ khai cân nặng tiêm chủng tuần trước là 8 kg.
  - *Bước 2 (Bản chất liều)*: Phác đồ cấp cứu phản vệ: Adrenaline tiêm bắp sâu liều $0.01\text{ mg/kg} = 0.01\text{ ml/kg}$ dung dịch 1:1000 ($1\text{ mg/1 ml}$).
  - *Bước 3 (Nhân cân nặng)*: Thể tích Adrenaline cần lấy = $0.01\text{ ml/kg} \times 8\text{ kg} = \mathbf{0.08\text{ ml}}$ (tương đương $0.08\text{ mg}$).
  - *Bước 4 (Đối chiếu trần liều)*: Trần liều trẻ < 30 kg là 0.3 ml (0.3 mg). Liều 0.08 ml nằm hoàn toàn trong giới hạn an toàn.
  - *Bước 5 (Kỹ thuật tiêm)*: Lấy ống Adrenaline 1 mg/1 ml nguyên vẹn. Dùng bơm tiêm 1 ml (chia vạch 0.01 ml) rút chính xác 0.08 ml. Tiêm bắp sâu vuông góc 90 độ tại **mặt trước-ngoài đùi phải (cơ rộng ngoài)**. Cho thở oxy qua mặt nạ có túi dự trữ. Theo dõi sinh hiệu và đánh giá lại sau 5 phút để quyết định liều Adrenaline thứ 2 nếu chưa cải thiện.
  - ✍️ **Y lệnh khẩn cấp**:  
    `Adrenaline 1 mg/1 ml (1:1000): Tiêm bắp sâu mặt trước-ngoài đùi 0.08 ml (= 0.08 mg) ngay lập tức. Đánh giá lại sinh hiệu sau 5 phút. Cân nặng: 8 kg`.

### Case 3: Trẻ 12 kg tiêu chảy mất nước & sốt — Bù ORS, bẫy Paracetamol siro vs viên đạn
- **Bệnh cảnh**: Bé trai 2 tuổi, nặng 12 kg, vào viện vì tiêu chảy phân lỏng toé nước 8 lần trong ngày kèm sốt cao 39.2°C, mắt trũng, khát nước uống háo hức, nếp véo da mất chậm. Chẩn đoán: Tiêu chảy cấp có mất nước (Phác đồ B theo WHO). Người nhà cho biết ở nhà đã vừa cho uống siro hạ sốt vừa nhét thuốc đạn vì "thấy sốt cao quá không hạ".
- **Hướng dẫn xử trí bù dịch và hạ sốt ca 3 có phân tích**:
  - *Bước 1 (Cân nặng)*: Cân thực tế 12 kg.
  - *Bước 2 (Phác đồ bù dịch & Hạ sốt)*:
    - Bù dịch Phác đồ B: ORS áp lực thẩm thấu thấp liều $75\text{ ml/kg}$ uống trong 4 giờ đầu. Thể tích ORS = $75 \times 12 = \mathbf{900\text{ ml}}$ uống từng thìa nhỏ trong 4 giờ.
    - Kẽm: Bổ sung 20 mg/ngày trong 14 ngày.
    - Hạ sốt: Cảnh báo gia đình ngừng ngay việc nhét thuốc đạn. Chỉ dùng Paracetamol đường uống liều $10 - 15\text{ mg/kg/lần} = 120 - 180\text{ mg/lần}$, mỗi 4–6 giờ khi sốt $\ge 38.5^\circ\text{C}$.
  - *Bước 3 (Nhân liều hạ sốt)*: Chọn liều trung bình 12.5 mg/kg: $12.5 \times 12 = \mathbf{150\text{ mg/lần}}$.
  - *Bước 4 (Đối chiếu trần)*: Trần liều Paracetamol tối đa là 1000 mg/lần. Liều 150 mg an toàn.
  - *Bước 5 (Chọn dạng bào chế)*: Khoa có sẵn gói bột Paracetamol 150 mg hoặc siro 120 mg/5 ml (cần 6.25 ml). Chọn gói bột 150 mg pha vào 10–15 ml nước cho uống rất tiện lợi và chính xác.
  - ✍️ **Đơn thuốc & Y lệnh**:  
    1. `Oresol áp lực thẩm thấu thấp (gói pha 200 ml): Pha 05 gói vào đúng 1000 ml nước đun sôi để nguội. Cho trẻ uống 900 ml rải rác từng thìa trong 4 giờ đầu. Tiếp tục cho bú mẹ.`  
    2. `Paracetamol gói bột 150 mg: Uống 01 gói (= 150 mg) khi sốt ≥ 38.5°C, cách mỗi 4–6 giờ. Tối đa không quá 4 gói/24 giờ. Cấm dùng kèm thuốc đạn hậu môn.`  
    3. `Kẽm gluconat 20 mg: Uống 01 viên/ngày sau ăn, dùng liên tục 14 ngày.`

### Case 4: Trẻ 30 kg hen phế quản cấp nặng — Salbutamol khí dung & Corticoid chạm trần
- **Bệnh cảnh**: Bệnh nhi nam, 9 tuổi, nặng 30 kg, tiền căn hen phế quản. Vào viện trong tình trạng khó thở dữ dội, ngồi thở co kéo hõm ức và cơ liên sườn, nói từng từ, SpO₂ 89%, phổi ran rít ngáy lan tỏa hai phế trường. Chẩn đoán: Cơn hen phế quản cấp mức độ nặng.
- **Đánh giá giải thích phác đồ kiểm soát cơn hen ca 4**:
  - *Bước 1 (Cân nặng)*: Cân nặng 30 kg.
  - *Bước 2 (Phác đồ xử trí)*:
    - Salbutamol khí dung qua oxy dòng 6–8 lít/phút. Trẻ 30 kg ($\ge 25\text{ kg}$) dùng liều **5 mg/lần** phối hợp Ipratropium bromid **0.5 mg/lần**, khí dung 3 lần liên tiếp cách nhau 20 phút trong giờ đầu.
    - Corticoid toàn thân: Methylprednisolone tiêm tĩnh mạch liều $1 - 2\text{ mg/kg/ngày}$.
  - *Bước 3 (Nhân liều Corticoid)*: Lấy liều 2 mg/kg: $2 \times 30 = \mathbf{60\text{ mg/ngày}}$.
  - *Bước 4 (Đối chiếu trần liều)*: Trần liều khuyến cáo của Methylprednisolone trong cơn hen cấp là **$40 - 60\text{ mg/ngày}$**. Con số 60 mg chạm đúng trần liều tối đa. Tuyệt đối không tăng thêm liều.
  - *Bước 5 (Quy đổi dạng bào chế)*: Kho dược có lọ Methylprednisolone (Solu-Medrol) 40 mg. Dùng 1.5 lọ tiêm tĩnh mạch (hoặc 1 lọ 40 mg tiêm ngay, sau 12 giờ tiêm tiếp 20 mg).
  - ✍️ **Y lệnh cấp cứu**:  
    1. `Thở oxy qua mặt nạ 6 lít/phút, duy trì SpO₂ ≥ 94%.`  
    2. `Salbutamol 5 mg (02 ống 2.5 mg/2.5 ml) + Ipratropium bromid 0.5 mg (01 ống 0.5 mg/2 ml): Khí dung qua oxy ngay lập tức, lặp lại mỗi 20 phút x 3 lần đầu.`  
    3. `Methylprednisolone lọ bột 40 mg: Tiêm tĩnh mạch 1.5 lọ (= 60 mg) tiêm tĩnh mạch chậm. (Chạm trần liều người lớn. Cân nặng: 30 kg)`.

---

## 11. TIPS VÀ MẸO THỰC HÀNH LÂM SÀNG (CLINICAL PEARLS)

1. **Mẹo ghi cân nặng "bất di bất dịch"**: Luôn ghi cân nặng của trẻ to rõ ràng ở góc trên bên phải của mọi tờ đơn thuốc và trang đầu bệnh án. Một y lệnh không có cân nặng là một y lệnh khiếm khuyết tiềm ẩn nguy cơ tử vong.
2. **Mẹo viết số thập phân của ISMP**: Nhẩm câu thần chú: *"Không bao giờ để số 0 cô đơn sau dấu phẩy (No Trailing Zero), nhưng luôn bắt số 0 đứng trước dấu phẩy (Leading Zero)"*. Viết `0,5` thay vì `.5`; viết `5` thay vì `5.0`.
3. **Mẹo kiểm tra trần liều nhanh**: Bất kỳ khi nào tính ra một liều thuốc mà bản thân cảm thấy "con số này hình như to bằng liều người lớn", hãy dừng lại 10 giây để tra cứu liều tối đa trong Dược thư Quốc gia.
4. **Mẹo nhớ trần Ceftriaxone**: Trẻ từ **20 kg** trở lên khi dùng liều viêm màng não/nhiễm khuẩn nặng 100 mg/kg sẽ chạm trần **2 g/ngày**. Không bao giờ kê quá 2 g/ngày cho bệnh nhi nếu không có ý kiến hội chẩn của chuyên gia truyền nhiễm.
5. **Mẹo đong siro không có cốc**: Khi gia đình không có cốc đong ml, hãy hướng dẫn họ mua một chiếc **bơm tiêm xilanh 5 ml bỏ kim** tại hiệu thuốc. Đây là dụng cụ lấy thể tích siro chính xác nhất, rẻ tiền nhất và dễ cho trẻ uống nhất mà không bị đổ trào.
6. **Mẹo nhớ dây truyền dịch**: Dây truyền nhi khoa (60 giọt/ml) có số giọt/phút đúng bằng số ml/giờ. Dây truyền người lớn (20 giọt/ml) có số giọt/phút bằng số ml/giờ chia cho 3.
7. **Mẹo nhớ liều Adrenaline phản vệ**: Thể tích dung dịch Adrenaline 1:1000 ($1\text{ mg/1 ml}$) tiêm bắp bằng đúng **$0.01 \times \text{cân nặng}$**. Trẻ 5 kg tiêm 0.05 ml; trẻ 10 kg tiêm 0.1 ml; trẻ 20 kg tiêm 0.2 ml; trẻ 30 kg tiêm 0.3 ml. Dễ nhớ, không bao giờ nhầm!
8. **Mẹo bù Kali an toàn**: Không bao giờ lấy ống Kali clorua ra khỏi tủ thuốc nếu bệnh nhi chưa có nước tiểu. Nhớ tỷ lệ vàng: 1 ống KCl 10% 10 ml chứa 13.4 mmol K⁺; pha vào chai dịch 500 ml sẽ tạo ra nồng độ ~27 mmol/L (hoàn toàn an toàn qua ven ngoại vi).
9. **Mẹo phòng ngừa hội chứng Red-man của Vancomycin**: Luôn dặn điều dưỡng cài đặt máy truyền dịch tối thiểu 60 phút cho liều 500 mg, và 120 phút cho liều 1000 mg.
10. **Mẹo chống bẫy hạ sốt kép**: Khi giải thích cho phụ huynh, luôn nhấn mạnh: *"Siro và thuốc đạn nhét đít này cùng là một chất Paracetamol, chỉ khác nhau đường đi vào người. Tuyệt đối không được dùng cả hai cùng lúc"*.
11. **Mẹo kiểm tra độc lập (Double-check) thuốc High-Alert**: Với 5 loại thuốc: Insulin, Heparin, Kali clorua, Adrenaline truyền liên tục và Thuốc an thần/giãn cơ — bắt buộc hai người (bác sĩ và điều dưỡng) tính toán độc lập và đối chiếu kết quả trước khi nhấn nút máy tiêm truyền.
12. **Mẹo phân tầng trẻ béo phì**: Với trẻ béo phì, kháng sinh tan trong nước (Aminoglycosid, Vancomycin) tính theo cân nặng lý tưởng (IBW); kháng sinh beta-lactam tính theo cân nặng thực tế nhưng phải khống chế trần liều người lớn.

---

## 12. TÓM TẮT CỐT LÕI — 10 NGUYÊN TẮC VÀNG KÊ ĐƠN NHI KHOA

```text
               10 NGUYÊN TẮC VÀNG MANG VÀO CA TRỰC BỆNH VIỆN
               ─────────────────────────────────────────────
               1. Cân thật bệnh nhi, cấm đoán mò bằng mắt.
               2. Phân biệt rõ ràng: mg/kg/LẦN vs mg/kg/NGÀY.
               3. Kiểm tra trần liều người lớn — Lấy số nhỏ hơn!
               4. Trẻ từ 40 kg trở lên: Cân nhắc liều người lớn.
               5. Viết đơn song song cả mg và ml cho dạng lỏng.
               6. Tuyệt đối cấm tiêm Bolus Kali clorua tĩnh mạch.
               7. Sơ sinh hạ đường huyết: Chỉ dùng Glucose 10%.
               8. Cấm viết .5 mg hay 5.0 mg (Luôn viết 0,5 mg và 5 mg).
               9. Cấm Aspirin (<16t), Codein (<12t), Ceftriaxone (<28 ngày).
               10. Double-check độc lập với tất cả thuốc High-Alert.
```

### Bảng kiểm 10 điểm an toàn trước khi ký đơn thuốc (Prescription Safety Checklist)
- [ ] 1. Đã ghi chỉ số cân nặng (kg) và tuổi của bệnh nhi trên đầu đơn chưa?
- [ ] 2. Đã xác định rõ thuốc tính theo mg/kg/lần hay mg/kg/ngày và số lần chia trong ngày chưa?
- [ ] 3. Đã làm phép nhân chính xác và kiểm tra không bị lệch dấu phẩy thập phân chưa?
- [ ] 4. Đã so sánh với trần liều tối đa hàng ngày của người lớn chưa? (Đã chạm trần nếu vượt quá).
- [ ] 5. Với thuốc dạng lỏng (siro/hỗn dịch), đã ghi cả hàm lượng (mg) và thể tích quy đổi (ml) chưa?
- [ ] 6. Có sử dụng số 0 dẫn đầu (`0,5 mg`) và loại bỏ số 0 thừa sau đuôi (`5 mg`) chưa?
- [ ] 7. Đã kiểm tra bệnh nhi có chống chỉ định đặc thù theo tuổi không (Aspirin, Codein, Ceftriaxone sơ sinh...)?
- [ ] 8. Có bị trùng lặp thuốc hạ sốt giữa đường uống và đường đặt trực tràng không?
- [ ] 9. Dịch truyền duy trì có dung dịch Dextrose và điện giải đẳng trương thích hợp không (tránh D5% đơn thuần)?
- [ ] 10. Nếu là thuốc High-Alert (Insulin, Kali, Vận mạch), đã có chữ ký xác nhận của người thứ hai kiểm tra độc lập chưa?

---

## 13. TÀI LIỆU THAM KHẢO & BẰNG CHỨNG Y VĂN

1. **AHA / PALS Guidelines (2020)**: *Pediatric Advanced Life Support: 2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care.* Circulation, 142(16_suppl_2):S469-S523. [GUIDELINE VERIFIED]
2. **World Health Organization (WHO, 2019)**: *Pocket Book of Hospital Care for Children: Guidelines for the Management of Common Childhood Illnesses.* 2nd Edition. Geneva: World Health Organization. [GUIDELINE VERIFIED]
3. **American Academy of Pediatrics (AAP, 2020)**: *Prevention of Medication Errors in the Pediatric Inpatient Setting.* Pediatrics, 146(5):e2020025845. [GUIDELINE VERIFIED]
4. **Bộ Y tế Việt Nam (2022)**: *Dược thư Quốc gia Việt Nam.* Lần xuất bản thứ ba. NXB Y học, Hà Nội. [GUIDELINE VERIFIED]
5. **Holliday MA, Segar WE. (1957)**: *The maintenance need for water in parenteral fluid therapy.* Pediatrics, 19(5):823-832. PMID: **13431307**. [DATA VERIFIED]
6. **Kearns GL, Abdel-Rahman SM, Alander SW, et al. (2003)**: *Developmental pharmacology--drug efflux, metabolism, and transport in the first years of life.* N Engl J Med, 349(12):1157-1167. PMID: **13679531**. [DATA VERIFIED]
7. **Kaushal R, Bates DW, Landrigan C, et al. (2001)**: *Medication errors and adverse drug events in pediatric inpatients.* JAMA, 285(16):2114-2120. PMID: **11311101**. [DATA VERIFIED]
8. **Schwartz GJ, Work DF. (2009)**: *Measurement and estimation of GFR in children and adolescents.* Clin J Am Soc Nephrol, 4(11):1832-1843. PMID: **19820136**. [DATA VERIFIED]
9. **Mosteller RD. (1987)**: *Simplified calculation of body-surface area.* N Engl J Med, 317(17):1098. PMID: **3657876**. [DATA VERIFIED]
10. **Rumack BH, Matthew H. (1975)**: *Acetaminophen poisoning and toxicity.* Pediatrics, 55(6):871-876. PMID: **1134886**. [DATA VERIFIED]
11. **Frush KS, Hohenhaus SM, Luo X, et al. (2004)**: *Evaluation of a color-coded tape for weight estimation in pediatrics.* Acad Emerg Med, 11(5):548. PMID: **15466144**. [DATA VERIFIED]
12. **Cuzzolin L, Atzei A, Fanos V. (2006)**: *Off-label and unlicensed drug treatments in neonatal intensive care: an Italian multicentre study.* Eur J Clin Pharmacol, 62(4):303-308. PMID: **16758319**. [DATA VERIFIED]
