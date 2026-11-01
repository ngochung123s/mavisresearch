# HS-10 · PHIÊN MÃ, DỊCH MÃ Ở SINH VẬT NHÂN SƠ, NHÂN THỰC VÀ ĐIỀU HÒA BIỂU HIỆN GEN
> **Tác giả:** PGS. TS. BS. Trần Huy Thịnh — ĐHY Hà Nội
> **Nguồn trích xuất:** Giáo trình Hóa sinh Y học (GS. TS. BS. Tạ Thành Văn chủ biên, Tái bản lần thứ 7, Nhà xuất bản Y học, Tr. 216 – 233)
> **Chuẩn mực:** Khoa học chứng cứ (EBM), Danh pháp IUBMB & Y học lâm sàng
**Phần:** Phần II: Chuyển hóa chất | **Chuyên đề:** Sinh tổng hợp Protein và Điều hòa biểu hiện gen

---

## MỤC TIÊU BÀI HỌC (CHUẨN BỘ MÔN HÓA SINH - ĐH Y HÀ NỘI)
1. **Phân tích được 4 đặc điểm cốt lõi của mã di truyền** (tính bộ ba, tính liên tục - không chồng gối, tính thoái hóa kèm thuyết dao động Wobble của Francis Crick, tính vạn năng và các ngoại lệ trong ty thể).
2. **Trình bày được cấu trúc và vai trò của các thành phần tham gia dịch mã:** mRNA mang bộ ba mã sao (codon), tRNA mang bộ ba đối mã (anticodon) và đầu tiếp nhận acid amin $-CCA-3'$, rRNA và các tiểu đơn vị của Ribosom ở tế bào nhân sơ ($70S = 50S + 30S$) và nhân thực ($80S = 60S + 40S$).
3. **Mô tả chi tiết cơ chế phân tử của quá trình hoạt hóa acid amin** bởi enzyme aminoacyl-tRNA synthetase (2 bước phản ứng tiêu tốn năng lượng tương đương 2 liên kết phosphat cao năng, cơ chế sửa sai kép - proofreading).
4. **Phân tích chi tiết 3 giai đoạn dịch mã trên Ribosom:** Giai đoạn mở đầu (nhận diện mũ $5'\text{-cap}$/Shine-Dalgarno, các yếu tố IFs/eIFs), giai đoạn kéo dài (gắn aminoacyl-tRNA tại vị trí A, hình thành liên kết peptid nhờ ribozyme Peptidyl transferase của rRNA, sự chuyển vị translocation nhờ EF-G/eEF2) và giai đoạn kết thúc (các yếu tố giải phóng RFs/eRFs).
5. **Trình bày các hình thức biến đổi và hoàn thiện chuỗi polypeptide sau dịch mã:** Cắt bỏ fMet/Met, peptide tín hiệu (signal peptide) qua hạt nhận diện tín hiệu SRP, hình thành cầu disulfua, biến đổi cộng hóa trị các acid amin (phosphoryl hóa, glycosyl hóa, carboxyl hóa phụ thuộc Vitamin K, hydroxyl hóa phụ thuộc Vitamin C) và phân cắt tiền chất zymogen/preprohormone.
6. **Giải thích cơ chế phân tử tác dụng của các kháng sinh và độc tố ức chế dịch mã:** Tetracyclin, Aminoglycosid, Chloramphenicol, Macrolid/Clindamycin, Puromycin, Diphtheria toxin và Cycloheximide.
7. **Phân tích cơ chế điều hòa biểu hiện gen:** Ở sinh vật nhân sơ qua mô hình Operon Lac (điều hòa âm tính bởi LacI/Allolactose, điều hòa dương tính bởi phức hợp cAMP-CAP) và Operon Trp (điều hòa ức chế corepressor và cơ chế suy giảm - attenuation); ở sinh vật nhân thực qua kiểm soát dịch mã (phosphoryl hóa eIF2 bởi kinase HRI và PKR), biến đổi biểu sinh (epigenetics) và điều hòa sau phiên mã (microRNA).

---

## 1. MÃ DI TRUYỀN VÀ BẢN ĐỒ DỊCH MÃ

Sinh tổng hợp protein (dịch mã - translation) là quá trình tế bào chuyển đổi thông tin di truyền được mã hóa dưới dạng trình tự các nucleotide trên phân tử mRNA thành trình tự các acid amin liên kết với nhau bằng liên kết peptid để tạo nên chuỗi polypeptide đặc hiệu. Đây là mắt xích trung tâm của học thuyết trung tâm sinh học phân tử (Central Dogma):

$$\text{DNA} \xrightarrow{\text{Phiên mã (Transcription)}} \text{mRNA} \xrightarrow{\text{Dịch mã (Translation)}} \text{Protein}$$

### 1.1. Bốn đặc tính cốt lõi của Mã di truyền

Mã di truyền (Genetic code) là từ điển ngôn ngữ phân tử quy định mối quan hệ tương ứng giữa 4 loại nucleotide ($A, U, G, C$) trên mRNA và 20 loại acid amin chuẩn tạo protein. Bằng các thí nghiệm đột phá của Marshall Nirenberg, Heinrich Matthaei và Har Gobind Khorana (đoạt giải Nobel Y học năm 1968), cấu trúc mã di truyền đã được làm sáng tỏ với 4 đặc tính nền tảng:

1. **Mã bộ ba (Triplet code):**
   - Bộ ba nucleotide liên tiếp trên mRNA được gọi là một **codon** (mã sao).
   - Vì có 4 loại nucleotide ($A, U, G, C$), số lượng tổ hợp bộ ba khả dĩ là $4^3 = 64$ codon.
   - Trong 64 codon:
     - **61 codon mã hóa acid amin** (sense codons). Trong đó codon $\text{5'-AUG-3'}$ vừa là **mã mở đầu (Initiation codon)** quy định điểm bắt đầu dịch mã, vừa mã hóa cho **Methionin** (ở sinh vật nhân thực) hoặc **N-formylmethionin (fMet)** (ở sinh vật nhân sơ và ty thể).
     - **3 codon kết thúc (Stop codons / Nonsense codons):** $\text{5'-UAA-3'}$ (ochre), $\text{5'-UAG-3'}$ (amber), và $\text{5'-UGA-3'}$ (opal). Các codon này không mã hóa cho bất kỳ acid amin nào mà là tín hiệu để các yếu tố giải phóng (Release Factors) gắn vào chấm dứt dịch mã.
     - *Ngoại lệ mở rộng:* Trong một số điều kiện vi môi trường đặc biệt, $\text{UGA}$ có thể mã hóa cho acid amin thứ 21 là **Selenocystein (Sec, U)** với sự tham gia của yếu tố SECIS; codon $\text{UAG}$ ở một số vi khuẩn cổ mã hóa cho acid amin thứ 22 là **Pyrrolysine (Pyl, O)**.

2. **Tính liên tục và không chồng gối (Non-overlapping and Comma-less):**
   - Khung đọc mở (Open Reading Frame - ORF) được đọc liên tục từng bước 3 nucleotide một, bắt đầu từ codon mở đầu $\text{5'-AUG-3'}$ cho đến khi gặp codon kết thúc.
   - Giữa các codon kế tiếp không có nucleotide ngăn cách ("không dấu phẩy").
   - Các codon hoàn toàn tách biệt, nucleotide của codon này không thuộc về codon kế cận ("không chồng gối").
   - *Ý nghĩa bệnh học:* Đột biến thêm hoặc mất nucleotide với số lượng không phải là bội số của 3 sẽ gây **đột biến lệch khung (frameshift mutation)**, làm thay đổi toàn bộ trình tự acid amin từ vị trí đột biến về phía sau và thường xuất hiện codon kết thúc sớm, tạo ra protein cắt cụt mất chức năng (gặp trong bệnh loạn dưỡng cơ Duchenne).

3. **Tính thoái hóa hay độ dư thừa (Degeneracy / Redundancy):**
   - Ngoại trừ hai acid amin duy nhất chỉ được mã hóa bởi 1 codon là **Methionin** ($\text{AUG}$) và **Tryptophan** ($\text{UGG}$), 18 acid amin còn lại đều được mã hóa bởi từ 2 đến 6 codon đồng nghĩa (synonymous codons).
   - Ví dụ: Arginin, Leucin và Serin mỗi acid amin có tới 6 codon mã hóa khác nhau.
   - *Ý nghĩa sinh học:* Tính thoái hóa tạo ra tấm đệm an toàn giảm thiểu tác hại của các đột biến điểm. Nếu đột biến thay thế nucleotide xảy ra ở vị trí thứ ba của codon, nó thường không làm thay đổi acid amin được tạo ra (**đột biến đồng nghĩa / đột biến câm - silent mutation**).

4. **Tính vạn năng (Universal):**
   - Hầu như toàn bộ sinh giới, từ vi khuẩn $E. coli$, thực vật, nấm men đến động vật có vú và con người, đều dùng chung một bảng mã di truyền chuẩn.
   - *Ý nghĩa công nghệ sinh học:* Tính vạn năng cho phép chuyển gen của người vào vi khuẩn hoặc nấm men để sản xuất các protein trị liệu quý giá như Insulin người tái tổ hợp, Erythropoietin (EPO), Interferon, hormon tăng trưởng GH.
   - *Ngoại lệ:* DNA ty thể (mtDNA) ở người có một số biến đổi nhỏ so với bảng mã chuẩn:
     - $\text{UGA}$ mã hóa Tryptophan (thay vì tín hiệu kết thúc).
     - $\text{AGA}$ và $\text{AGG}$ đóng vai trò là codon kết thúc (thay vì mã hóa Arginin).
     - $\text{AUA}$ mã hóa Methionin (thay vì Isoleucin).

### 1.2. Thuyết dao động Wobble của Francis Crick

Mặc dù có 61 codon mã hóa acid amin, hầu hết các tế bào chỉ sở hữu khoảng 30 đến 45 loại tRNA khác nhau. Hiện tượng một phân tử tRNA có thể nhận diện và bắt cặp bổ sung với nhiều hơn một codon đồng nghĩa được Francis Crick giải thích thỏa đáng qua **Thuyết dao động (Wobble Hypothesis)** vào năm 1966:
- Hai nucleotide đầu tiên (vị trí 1 và 2 tính từ đầu $5'$) của codon trên mRNA tạo liên kết hydro rất nghiêm ngặt và chuẩn tắc theo nguyên tắc Watson-Crick ($A=U, G\equiv C$) với hai nucleotide ở vị trí 3 và 2 (tính từ đầu $5'$) của anticodon trên tRNA.
- Nucleotide thứ 3 ở đầu $3'$ của codon trên mRNA và nucleotide thứ 1 ở đầu $5'$ của anticodon trên tRNA có không gian linh động lỏng lẻo hơn (cho phép "dao động" - wobble).
- Tại vị trí dao động này:
  - Nếu đầu $5'$ của anticodon là $G$, nó có thể bắt cặp bổ sung với $C$ hoặc $U$ ở vị trí thứ 3 của codon.
  - Nếu đầu $5'$ của anticodon là $U$, nó có thể bắt cặp với $A$ hoặc $G$.
  - Nếu đầu $5'$ của anticodon là nucleotide biến đổi **Inosine ($I$)** (tạo thành do enzym khử amin Adenosin trên tRNA), Inosine có thể tạo liên kết hydro với cả 3 base $U, C$ hoặc $A$ ở vị trí thứ 3 của codon.

| Base ở đầu $5'$ của Anticodon (tRNA) | Các base có thể bắt cặp ở đầu $3'$ của Codon (mRNA) |
| :--- | :--- |
| **Cytosin ($C$)** | Chỉ $G$ (nghiêm ngặt chuẩn tắc) |
| **Adenin ($A$)** | Chỉ $U$ (nghiêm ngặt chuẩn tắc) |
| **Uracil ($U$)** | $A$ hoặc $G$ (dao động) |
| **Guanin ($G$)** | $C$ hoặc $U$ (dao động) |
| **Inosine ($I$)** | $U, C$ hoặc $A$ (linh hoạt tối đa, 1 tRNA nhận diện 3 codon) |

---

## 2. CÁC THÀNH PHẦN THAM GIA QUÁ TRÌNH DỊCH MÃ

Quá trình dịch mã đòi hỏi sự phối hợp nhịp nhàng của một bộ máy sinh hóa khổng lồ gồm hơn 300 phân tử đại phân tử trong tế bào chất:

### 2.1. Phân tử mRNA mang bản sao thông tin di truyền
- Ở **sinh vật nhân sơ (Prokaryotes)**: mRNA thường là **polycistronic** (một phân tử mRNA chứa trình tự mã hóa cho nhiều chuỗi polypeptide khác nhau cùng thuộc một operon chức năng). Mỗi cistron có codon mở đầu riêng và phía trước đó khoảng $8 - 10$ nucleotide là trình tự giàu purine **Shine-Dalgarno** ($\text{5'-AGGAGGU-3'}$) giúp tiểu đơn vị $30S$ nhận diện vị trí bắt đầu dịch mã.
- Ở **sinh vật nhân thực (Eukaryotes)**: mRNA hầu hết là **monocistronic** (chỉ mã hóa cho một chuỗi polypeptide duy nhất). Đầu $5'$ có cấu trúc **mũ $5'\text{-m}^7\text{Gppp}$ (7-methylguanosine cap)**, đầu $3'$ có **đuôi poly(A)** dài khoảng 100 - 250 gốc adenylat. Codon mở đầu $\text{AUG}$ thường nằm trong trình tự đồng thuận **Kozak** ($\text{5'-ACCAUGG-3'}$).

### 2.2. Phân tử tRNA vận chuyển acid amin
- tRNA là phân tử RNA sợi đơn gồm $73 - 93$ ribonucleotide, cuộn gấp thành cấu trúc bậc hai hình lá chẻ ba (cloverleaf) và cấu trúc bậc ba không gian hình chữ L ngược.
- Phân tử tRNA sở hữu các vùng chức năng đặc hiệu:
  1. **Đầu tiếp nhận acid amin (Acceptor stem):** Tận cùng bằng bộ ba nucleotide đơn sợi $\text{5'-CCA-3'}$. Nhóm $-OH$ ở vị trí $2'$ hoặc $3'$ của ribose thuộc nucleotide Adenosin tận cùng là nơi hình thành liên kết este cao năng với nhóm $-COOH$ của acid amin được hoạt hóa.
  2. **Vòng đối mã (Anticodon loop):** Chứa bộ ba anticodon đặc hiệu có chiều $3' \to 5'$, tiếp xúc và bắt cặp đối song song bổ sung với codon trên mRNA ($5' \to 3'$).
  3. **Vòng D (D-loop):** Chứa nhiều base lạ Dihydrouracil ($D$), tham gia vào sự nhận diện của enzyme aminoacyl-tRNA synthetase.
  4. **Vòng $T\psi C$ (T-loop):** Chứa base biến đổi Ribothymidin ($T$) và Pseudouridin ($\psi$), tham gia gắn kết tRNA với bề mặt ribosome.

![Cấu trúc của RNA vận chuyển tRNA](hoasinh_media/HS-10_fig10_1.png)
*Hình 10.1. Cấu trúc của RNA vận chuyển (tRNA) với đầu gắn acid amin CCA-3' và các nhánh đối mã, nhánh D, nhánh TψC.*

### 2.3. Ribosom - Nhà máy tổng hợp protein
Ribosom là một phức hợp ribonucleoprotein (RNP) khổng lồ gồm hai tiểu đơn vị không đối xứng:

| Đặc điểm phân tử | Ribosom Nhân sơ ($70S$) | Ribosom Nhân thực ($80S$) |
| :--- | :--- | :--- |
| **Tiểu đơn vị nhỏ** | **$30S$:** Gồm $16S\text{ rRNA}$ ($\,\approx 1540\text{ nt}$) và 21 protein ($S_1 - S_{21}$). Chịu trách nhiệm nhận diện trình tự Shine-Dalgarno và kiểm tra sự bắt cặp codon-anticodon. | **$40S$:** Gồm $18S\text{ rRNA}$ ($\,\approx 1900\text{ nt}$) và $\,\approx 33\text{ protein}$. Nhận diện mũ $5'\text{-cap}$ và quét tìm codon mở đầu Kozak AUG. |
| **Tiểu đơn vị lớn** | **$50S$:** Gồm $23S\text{ rRNA}$ ($\,\approx 2900\text{ nt}$), $5S\text{ rRNA}$ ($120\text{ nt}$) và 34 protein ($L_1 - L_{34}$). Chứa trung tâm xúc tác peptidyl transferase (ribozyme $23S$). | **$60S$:** Gồm $28S\text{ rRNA}$ ($\,\approx 4700\text{ nt}$), $5.8S\text{ rRNA}$ ($160\text{ nt}$), $5S\text{ rRNA}$ ($120\text{ nt}$) và $\,\approx 49\text{ protein}$. Chứa trung tâm xúc tác peptidyl transferase (ribozyme $28S$). |

Trên phân tử ribosom hoàn chỉnh lắp ráp có **3 vị trí gắn tRNA** quan trọng:
- **Vị trí A (Aminoacyl site):** Tiếp nhận phức hợp aminoacyl-tRNA mới đi vào theo đúng codon đối ứng trên mRNA.
- **Vị trí P (Peptidyl site):** Chứa peptidyl-tRNA đang mang chuỗi polypeptide đang kéo dài (hoặc fMet-tRNA / Met-tRNA mở đầu).
- **Vị trí E (Exit site):** Chứa phân tử tRNA đã mất acid amin (deacylated tRNA) chuẩn bị rời khỏi ribosom ra dịch bào.

![Cấu trúc của Ribosom](hoasinh_media/HS-10_fig10_2.png)
*Hình 10.2. Cấu trúc của Ribosom gồm các tiểu đơn vị và các vị trí gắn tRNA (vị trí A, P, E).*

---

## 3. CƠ CHẾ PHÂN TỬ CỦA QUÁ TRÌNH DỊCH MÃ

Quá trình dịch mã bao gồm 4 giai đoạn nối tiếp nhau: Hoạt hóa acid amin, Mở đầu chuỗi, Kéo dài chuỗi và Kết thúc chuỗi.

### 3.1. Giai đoạn 1: Hoạt hóa Acid Amin và Vai trò của Aminoacyl-tRNA Synthetase

Để có thể tham gia vào chuỗi polypeptide, acid amin tự do trong bào tương bắt buộc phải được hoạt hóa và gắn đồng hóa trị vào tRNA tương ứng. Quá trình này được xúc tác bởi họ enzyme **Aminoacyl-tRNA synthetase (aaRS)** gồm 20 enzyme đặc hiệu cho 20 loại acid amin.

Phản ứng hoạt hóa diễn ra qua 2 bước liên tiếp tại trung tâm hoạt động của enzyme:

$$\text{Bước 1: } \text{Acid Amin} + \text{ATP} + \text{Enzyme} \rightleftharpoons \text{Enzyme}\cdot[\text{Aminoacyl-AMP}] + \text{PP}_i$$

Nhóm carboxylate ($-COO^-$) của acid amin tấn công vào nguyên tử phosphor $\alpha$ của ATP, giải phóng Pyrophosphat vô cơ ($PP_i$) và tạo thành phức hợp trung gian cao năng **Aminoacyl-AMP (aminoacyl adenylate)** gắn chặt tại trung tâm hoạt động của enzyme. Phản ứng này được kéo theo một chiều không thuận nghịch nhờ enzyme pyrophosphatase vô cơ thủy phân tức thì $PP_i$:

$$\text{PP}_i + \text{H}_2\text{O} \xrightarrow{\text{Inorganic pyrophosphatase}} 2\,\text{P}_i \quad (\Delta G^{\circ\prime} \approx -19.2\,\text{kJ/mol})$$

$$\text{Bước 2: } \text{Enzyme}\cdot[\text{Aminoacyl-AMP}] + \text{tRNA} \rightleftharpoons \text{Aminoacyl-tRNA} + \text{AMP} + \text{Enzyme}$$

Nhóm hydroxyl ($-OH$ ở vị trí $2'$ hoặc $3'$) của ribose thuộc gốc Adenosin tận cùng tại đầu $CCA-3'$ của tRNA tấn công nucleophil vào liên kết este anhydrid của aminoacyl-AMP, chuyển gốc aminoacyl sang gắn với tRNA qua liên kết este giàu năng lượng, giải phóng AMP và giải phóng enzyme tự do.

- **Chi phí năng lượng:** Sự tiêu tốn 1 phân tử ATP biến thành AMP và $2\,P_i$ tương đương với việc tiêu thụ **2 liên kết phosphat cao năng** ($\,\sim 2\,\text{ATP}$) cho mỗi acid amin được hoạt hóa.
- **Cơ chế sửa sai kép (Double-sieve / Proofreading mechanism):**
  - Aminoacyl-tRNA synthetase là "người bảo vệ" trung thành nhất của mã di truyền. Nếu enzyme gắn nhầm acid amin vào tRNA (ví dụ gắn nhầm Valin thay vì Isoleucin), phân tử sai lệch sẽ bị chuyển sang một khoang xúc tác thứ hai gọi là **khoang hiệu đính (editing / hydrolytic site)** trên enzyme. Tại đây, liên kết este sai lệch bị thủy phân ngay lập tức trước khi phân tử rời khỏi enzyme.
  - Nhờ cơ chế sàng lọc kép này, tần suất sai sót của dịch mã giảm xuống dưới mức $1/10.000$.

![Giai đoạn hoạt hóa amino acid](hoasinh_media/HS-10_fig10_3.png)
*Hình 10.3. Giai đoạn hoạt hóa amino acid bởi aminoacyl-tRNA synthetase.*

---

### 3.2. Giai đoạn 2: Mở đầu Chuỗi Polypeptide (Initiation)

Giai đoạn mở đầu là bước then chốt quyết định tốc độ và độ chính xác của quá trình dịch mã, định vị chính xác codon mở đầu tại vị trí P của ribosome:

#### 3.2.1. Ở Sinh vật nhân sơ (Prokaryotes)
Yêu cầu sự tham gia của 3 yếu tố mở đầu: **IF1, IF2 (gắn GTP) và IF3**.
1. **Phân ly Ribosom:** Yếu tố IF3 gắn vào tiểu đơn vị nhỏ $30S$, ngăn không cho tiểu đơn vị lớn $50S$ kết hợp sớm với $30S$.
2. **Gắn mRNA:** Tiểu đơn vị $30S$ nhận diện phân tử mRNA nhờ sự bắt cặp bổ sung giữa đoạn giàu pyrimidine ở đầu $3'$ của $16S\text{ rRNA}$ ($\text{3'-UCCUCCA-5'}$) với trình tự giàu purine **Shine-Dalgarno** ($\text{5'-AGGAGGU-3'}$) trên mRNA, đặt codon mở đầu $\text{5'-AUG-3'}$ chuẩn xác vào vị trí P. Yếu tố IF1 gắn vào vị trí A để phong bế vị trí này.
3. **Đưa fMet-tRNA vào:** Phức hợp $\text{IF2-GTP}$ gắn kết đặc hiệu với **N-formylmethionyl-tRNA (fMet-tRNA$^{\text{fMet}}$)** đưa vào vị trí P, tại đây anticodon của tRNA bắt cặp với codon mở đầu AUG.
4. **Lắp ráp Ribosom $70S$ hoàn chỉnh:** Khi các thành phần đã khớp, IF3 rời đi. Tiểu đơn vị lớn $50S$ tiến vào kết hợp với $30S$. Sự tương tác này kích hoạt hoạt tính GTPase của IF2, thủy phân $\text{GTP} \to \text{GDP} + P_i$. IF1 và IF2-GDP tách rời khỏi ribosome, tạo thành **phức hợp mở đầu $70S$ hoàn chỉnh** với fMet-tRNA ngự trị tại vị trí P, trong khi vị trí A đang hoàn toàn trống sẵn sàng đón nhận aminoacyl-tRNA kế tiếp.

#### 3.2.2. Ở Sinh vật nhân thực (Eukaryotes)
Phức tạp hơn rất nhiều, đòi hỏi hơn 12 yếu tố mở đầu nhân thực (**eIFs**):
1. **Phức hợp tiền mở đầu $43S$:** Tiểu đơn vị $40S$ gắn với eIF3, eIF1, eIF1A và phức hợp tam phân gồm **eIF2-GTP** gắn với **Met-tRNA$_i^{\text{Met}}$** (không bị formyl hóa).
2. **Gắn mRNA qua mũ $5'\text{-cap}$:** Đầu $5'$ của mRNA nhân thực được nhận diện bởi phức hợp **eIF4F** (gồm eIF4E gắn trực tiếp vào mũ $m^7G$, protein giàn giáo eIF4G liên kết với PABP ở đuôi polyA, và eIF4A có hoạt tính helicase phụ thuộc ATP để tháo xoắn cấu trúc bậc hai của mRNA).
3. **Quét tìm codon mở đầu (Scanning):** Phức hợp $43S$ gắn vào đầu $5'$ của mRNA và trượt dọc theo chiều $5' \to 3'$ để "quét" tìm codon mở đầu AUG đầu tiên nằm trong trình tự đồng thuận **Kozak** ($\text{5'-ACCAUGG-3'}$).
4. **Hình thành Ribosom $80S$:** Khi gặp codon AUG, GTP trên eIF2 bị thủy phân nhờ eIF5 kích hoạt. Các eIFs giải phóng, cho phép tiểu đơn vị lớn $60S$ tiến vào gắn kết tạo nên **phức hợp mở đầu $80S$ hoạt động**.

![Giai đoạn mở đầu chuỗi polypeptide](hoasinh_media/HS-10_fig10_4.png)
*Hình 10.4. Giai đoạn mở đầu chuỗi tổng hợp polypeptide ở sinh vật nhân sơ.*

---

### 3.3. Giai đoạn 3: Kéo dài Chuỗi Polypeptide (Elongation)

Kéo dài là một chu kỳ lặp đi lặp lại gồm 3 bước tuần tự nhằm lắp ghép từng acid amin vào chuỗi theo đúng trật tự codon trên mRNA:

![Giai đoạn kéo dài chuỗi polypeptide 10.5A](hoasinh_media/HS-10_fig10_5A.png)
*Hình 10.5A. Giai đoạn kéo dài chuỗi: Gắn aminoacyl-tRNA mới vào vị trí A và tạo liên kết peptid.*

![Giai đoạn kéo dài chuỗi polypeptide 10.5B](hoasinh_media/HS-10_fig10_5B.png)
*Hình 10.5B. Giai đoạn kéo dài chuỗi: Chuyển vị của ribosom dọc theo phân tử mRNA.*

#### Bước 1: Gắn Aminoacyl-tRNA mới vào vị trí A (Decoding / A-site binding)
- Codon tiếp theo trên mRNA nằm lộ ra tại vị trí A của ribosom.
- Một phân tử aminoacyl-tRNA tương ứng được vận chuyển đến vị trí A dưới dạng phức hợp ba phần: **EF-Tu · GTP · Aminoacyl-tRNA** (ở vi khuẩn) hoặc **eEF1A · GTP · Aminoacyl-tRNA** (ở nhân thực).
- Nếu anticodon của tRNA bắt cặp bổ sung chính xác với codon trên mRNA tại vị trí A, ribosome sẽ kích hoạt hoạt tính GTPase của EF-Tu, thủy phân $\text{GTP} \to \text{GDP} + P_i$. Phức hợp $\text{EF-Tu}\cdot\text{GDP}$ giải phóng rời khỏi ribosom (sau đó được yếu tố EF-Ts tái tạo lại thành EF-Tu$\cdot$GTP).
- Tiêu tốn: **1 GTP**.

#### Bước 2: Hình thành Liên kết Peptid (Peptide bond formation)
- Nhóm $\alpha$-amin ($-NH_2$) tự do của aminoacyl-tRNA tại vị trí A thực hiện phản ứng tấn công ái nhân (nucleophilic attack) vào nhóm ester carbonyl ($-C=O$) của peptidyl-tRNA đang ngự ở vị trí P.
- Phản ứng này được xúc tác bởi trung tâm xúc tác **Peptidyl transferase** nằm trên tiểu đơn vị lớn của ribosom.
- *Khám phá chấn động:* Peptidyl transferase không phải là một enzyme protein mà là một **Ribozyme** — hoạt tính xúc tác hoàn toàn do phân tử **rRNA $23S$** (ở vi khuẩn) hoặc **rRNA $28S$** (ở nhân thực) đảm nhiệm.
- Kết quả: Liên kết este giữa chuỗi peptid và tRNA ở vị trí P bị cắt đứt; chuỗi peptid được nối dài thêm 1 acid amin và hiện đang gắn với tRNA nằm ở vị trí A (**peptidyl-tRNA tại vị trí A**), trong khi tRNA ở vị trí P đã mất acid amin (**deacylated tRNA**).
- Giai đoạn này **không tiêu tốn năng lượng ATP/GTP ngoại sinh**, năng lượng tạo liên kết peptid lấy trực tiếp từ thế năng của liên kết este cao năng giữa acid amin và tRNA vốn đã được nạp từ giai đoạn hoạt hóa.

#### Bước 3: Chuyển vị Ribosom (Translocation)
- Để tiếp tục đọc codon kế tiếp, ribosom phải dịch chuyển chính xác 3 nucleotide (1 codon) dọc theo phân tử mRNA theo chiều $5' \to 3'$.
- Quá trình chuyển vị đòi hỏi sự tham gia của yếu tố kéo dài **EF-G** (ở vi khuẩn) hoặc **eEF2** (ở nhân thực) gắn với GTP.
- Sự thủy phân $\text{GTP} \to \text{GDP} + P_i$ cung cấp năng lượng cơ học làm biến đổi cấu hình ribosom:
  - tRNA không mang acid amin bị đẩy từ vị trí P sang **vị trí E** và sau đó thoát ra dịch bào.
  - Peptidyl-tRNA đang mang chuỗi peptid dịch chuyển từ **vị trí A sang vị trí P**.
  - Codon tiếp theo trên mRNA được kéo vào ngự trị tại vị trí A đang trống.
- Tiêu tốn: **1 GTP**.

Chu kỳ 3 bước trên lặp lại liên tục với tốc độ khoảng 20 acid amin/giây ở vi khuẩn và 2 - 4 acid amin/giây ở tế bào nhân thực.

---

### 3.4. Giai đoạn 4: Kết thúc Chuỗi Polypeptide (Termination)

Quá trình dịch mã dừng lại khi một trong 3 codon kết thúc ($\text{UAA, UAG, UGA}$) xuất hiện tại vị trí A của ribosom:
- Không có bất kỳ tRNA nào có anticodon tương ứng với các codon kết thúc này. Thay vào đó, các **yếu tố giải phóng protein (Release Factors - RFs)** sẽ nhận diện codon kết thúc:
  - Ở vi khuẩn: **RF1** nhận diện UAA và UAG; **RF2** nhận diện UAA và UGA; **RF3-GTP** hỗ trợ sự giải phóng của RF1/RF2.
  - Ở nhân thực: Một yếu tố duy nhất **eRF1** nhận diện cả 3 codon kết thúc, phối hợp với **eRF3-GTP**.
- Khi RF gắn vào vị trí A, nó làm biến đổi cấu hình trung tâm peptidyl transferase, khiến enzyme này chuyển hướng xúc tác phản ứng chuyển nhóm peptid sang một phân tử **nước** thay vì nhóm amin của aminoacyl-tRNA.
- Chuỗi polypeptide hoàn chỉnh bị thủy phân cắt rời khỏi tRNA ở vị trí P và giải phóng vào bào tương.

![Giai đoạn kết thúc chuỗi polypeptide](hoasinh_media/HS-10_fig10_6.png)
*Hình 10.6. Giai đoạn kết thúc tổng hợp chuỗi polypeptide khi gặp codon kết thúc và giải phóng protein.*

![Minh họa toàn bộ quá trình sinh tổng hợp protein](hoasinh_media/HS-10_fig10_7.png)
*Hình 10.7. Minh họa quá trình sinh tổng hợp protein hoàn chỉnh từ nhân ra bào tương.*

### 3.5. Cân bằng Năng lượng của Sinh tổng hợp Protein

Để kết hợp **1 acid amin** vào chuỗi polypeptide, tế bào phải tiêu tốn ít nhất **4 liên kết phosphat cao năng** ($\,\sim 4\,\text{ATP/GTP}$):
1. **2 liên kết cao năng** cho quá trình hoạt hóa acid amin: $\text{ATP} \to \text{AMP} + 2\,P_i$.
2. **1 liên kết cao năng** ($\text{GTP} \to \text{GDP} + P_i$) cho sự gắn aminoacyl-tRNA vào vị trí A nhờ EF-Tu / eEF1A.
3. **1 liên kết cao năng** ($\text{GTP} \to \text{GDP} + P_i$) cho sự chuyển vị ribosome dọc mRNA nhờ EF-G / eEF2.
4. Ngoài ra còn tiêu tốn thêm năng lượng GTP trong giai đoạn mở đầu (IF2 / eIF2) và kết thúc tái chế (RF3 / eRF3 / RRF).

*Ý nghĩa sinh học:* Sinh tổng hợp protein là quá trình tiêu tốn năng lượng tế bào lớn nhất (chiếm tới $80 - 90\%$ tổng năng lượng chuyển hóa của một vi khuẩn phân chia nhanh). Sự tiêu hao năng lượng khổng lồ này là cái giá nhiệt động học bắt buộc để đảm bảo độ chính xác tuyệt đối trong việc bảo tồn thông tin di truyền thành cấu trúc protein chức năng.

---

## 4. HOÀN THIỆN VÀ BIẾN ĐỔI CHUỖI POLYPEPTIDE SAU DỊCH MÃ (POST-TRANSLATIONAL MODIFICATIONS - PTM)

Chuỗi polypeptide sau khi rời khỏi ribosome thường chưa có hoạt tính sinh học mà phải trải qua một loạt các biến đổi hoàn thiện sau dịch mã (PTM):

### 4.1. Cắt bỏ acid amin đầu N và peptide tín hiệu
- **Loại bỏ gốc mở đầu:** Ở vi khuẩn, gốc formyl được cắt bỏ bởi enzyme *Peptide deformylase*, sau đó gốc Methionin đầu $N$ thường bị cắt bởi enzyme *Methionine aminopeptidase*. Ở nhân thực, Methionin mở đầu cũng thường bị loại bỏ khỏi chuỗi.
- **Cắt peptide tín hiệu (Signal peptide cleavage):**
  - Các protein được định mệnh bài tiết ra ngoài tế bào, định vị trên màng sinh chất hoặc đưa vào lysosome đều mang một chuỗi peptide tín hiệu gồm 15 - 30 acid amin kỵ nước ở đầu $N$.
  - Khi peptide tín hiệu vừa ló ra khỏi ribosome, hạt nhận diện tín hiệu **SRP (Signal Recognition Particle)** sẽ gắn vào, tạm dừng dịch mã và đưa toàn bộ phức hợp ribosom đến gắn vào thụ thể SRP trên màng **Lưới nội chất hạt (RER)**.
  - Chuỗi polypeptide tiếp tục được tổng hợp và luồn qua kênh chuyển vị xuyên màng Sec61 vào lòng RER (cotranslational translocation).
  - Tại lòng RER, enzyme **Signal peptidase** cắt bỏ peptide tín hiệu giải phóng protein tự do vào lòng ống.

### 4.2. Hình thành cầu Disulfua ($-S-S-$) và Cuộn gấp Protein
- Các gốc Cysteine tự do trong chuỗi polypeptide tạo liên kết disulfua cộng hóa trị nội chuỗi hoặc liên phân tử nhờ enzyme **Protein Disulfide Isomerase (PDI)** trong lòng RER.
- Sự cuộn gấp đúng không gian 3 chiều được hỗ trợ bởi các protein kèm cặp **Chaperone** (như Hsp70, BiP, Calnexin). Nếu cuộn gấp sai, protein sẽ bị đào thải qua con đường thoái hóa protein liên kết lưới nội chất (ERAD) và đưa đến **Proteasome 26S** để phá hủy qua hệ thống **Ubiquitin hóa**.

### 4.3. Biến đổi cộng hóa trị các Acid amin đặc hiệu
1. **Phosphoryl hóa (Phosphorylation):** Xúc tác bởi các enzyme Protein Kinase, gắn nhóm phosphat từ ATP vào nhóm $-OH$ của gốc **Serin, Threonin hoặc Tyrosin**; phản ứng đảo ngược bởi Protein Phosphatase. Đây là công tắc phân tử phổ biến nhất điều hòa hoạt tính enzyme và dẫn truyền tín hiệu tế bào.
2. **Glycosyl hóa (Glycosylation):**
   - **N-glycosyl hóa:** Chuỗi oligosaccharide giàu mannose được gắn vào nguyên tử nitơ amide của gốc **Asparagine** (trình tự đồng thuận $Asn-X-Ser/Thr$) bắt đầu trong RER và hoàn thiện ở bộ máy Golgi.
   - **O-glycosyl hóa:** Chuỗi đường gắn vào nhóm $-OH$ của gốc **Serin hoặc Threonin** tại bộ máy Golgi (ví dụ mucin, kháng nguyên nhóm máu ABO).
3. **Carboxyl hóa phụ thuộc Vitamin K ($\gamma$-carboxylation):** Enzyme $\gamma$-glutamyl carboxylase gắn thêm nhóm $-COO^-$ vào vị trí carbon $\gamma$ của các gốc **Glutamat (Glu)** trên các yếu tố đông máu (**Yếu tố II, VII, IX, X, Protein C, S**), tạo ra acid $\gamma$-carboxyglutamic (Gla) có khả năng tạo phức càng cua bẫy ion $Ca^{2+}$, giúp các yếu tố đông máu gắn vào màng phospholipid tiểu cầu. Thuốc chống đông kháng Vitamin K (Warfarin) ức chế enzyme VKOR, ngăn chặn biến đổi này.
4. **Hydroxyl hóa phụ thuộc Vitamin C (Hydroxylation):** Gốc **Prolin và Lysin** trên chuỗi collagen được hydroxyl hóa thành **4-hydroxyprolin** và **5-hydroxylysin** nhờ enzyme prolyl hydroxylase và lysyl hydroxylase (cần cofactor là $Fe^{2+}$ và **Vitamin C / Acid Ascorbic**). Hydroxyprolin tạo liên kết hydro liên chuỗi làm bền vững chuỗi xoắn ba collagen. Thiếu Vitamin C gây bệnh **Scorbut** (chảy máu chân răng, vỡ mao mạch, vết thương lâu liền do collagen suy yếu).

### 4.4. Phân cắt chuỗi tiền chất tạo Protein hoạt động (Proteolytic Processing)
Nhiều protein và hormon được tổng hợp dưới dạng tiền chất bất hoạt (preproprotein hoặc zymogen) nhằm bảo vệ tế bào khỏi sự tự tiêu:
- **Tuyến tụy ngoại tiết:** Tiền enzyme trypsinogen, chymotrypsinogen được tiết vào tá tràng; tại đây enteropeptidase màng ruột cắt một đoạn peptide của trypsinogen thành trypsin hoạt động, sau đó trypsin hoạt hóa dây chuyền các zymogen khác.
- **Sinh tổng hợp Insulin:**
  $$\text{Preproinsulin} \xrightarrow{\text{Cắt peptide tín hiệu tại RER}} \text{Proinsulin} \xrightarrow{\text{Cắt đoạn Peptide C tại Golgi}} \text{Insulin hoạt động (chuỗi A + chuỗi B nối qua 2 cầu disulfua)}$$

---

## 5. CƠ CHẾ PHÂN TỬ CỦA KHÁNG SINH VÀ ĐỘC TỐ ỨC CHẾ DỊCH MÃ

Sự khác biệt về cấu trúc giữa ribosome $70S$ của vi khuẩn ($30S + 50S$) và ribosome $80S$ của tế bào nhân thực người ($40S + 60S$) là nền tảng cốt tử cho **độc tính chọn lọc (selective toxicity)** của các thuốc kháng sinh kháng khuẩn.

| Nhóm thuốc / Kháng sinh | Vị trí đích tác động | Cơ chế tác dụng phân tử | Ứng dụng lâm sàng & Độc tính |
| :--- | :--- | :--- | :--- |
| **Aminoglycosid**<br>*(Streptomycin, Gentamicin, Tobramycin, Amikacin)* | **Tiểu đơn vị $30S$** của ribosome vi khuẩn | - Gắn không thuận nghịch vào rRNA $16S$ của tiểu đơn vị $30S$.<br>- Biến dạng cấu trúc vị trí A, làm **đọc sai mã di truyền** (misreading of mRNA), đưa nhầm acid amin vào chuỗi.<br>- Ở nồng độ cao: phong bế sự tạo thành phức hợp mở đầu $70S$. Diệt khuẩn phụ thuộc nồng độ. | - Điều trị nhiễm khuẩn Gram (-) nặng, trực khuẩn mủ xanh (*Pseudomonas*), lao (*Streptomycin*).<br>- Độc tính: Độc với thận (hoại tử ống thận cấp) và độc với ốc tai tiền đình (gây điếc không hồi phục). |
| **Tetracyclin**<br>*(Tetracycline, Doxycycline, Minocycline)* | **Tiểu đơn vị $30S$** của ribosome vi khuẩn | - Gắn thuận nghịch vào rRNA $16S$ tiểu đơn vị $30S$.<br>- **Phong bế không gian vị trí A**, ngăn cản phức hợp Aminoacyl-tRNA tiến vào gắn với codon tương ứng trên mRNA.<br>- Kìm khuẩn phổ rộng. | - Điều trị vi khuẩn nội bào (*Chlamydia, Rickettsia, Mycoplasma*), mụn trứng cá, tả.<br>- Chống chỉ định phụ nữ có thai và trẻ em dưới 8 tuổi (gây lắng đọng men răng làm đổi màu răng vĩnh viễn và chậm phát triển xương). |
| **Chloramphenicol** | **Tiểu đơn vị $50S$** của ribosome vi khuẩn | - Gắn vào rRNA $23S$ của tiểu đơn vị $50S$.<br>- **Ức chế trực tiếp hoạt tính Peptidyl transferase**, ngăn chặn phản ứng hình thành liên kết peptid kéo dài chuỗi.<br>- Có thể ức chế một phần ribosom $55S$ trong ty thể người ở liều cao. | - Thuốc kìm khuẩn phổ rộng nhưng hạn chế sử dụng do độc tính nghiêm trọng: suy tủy xương bất sản không hồi phục và **Hội chứng xám ở trẻ sơ sinh (Gray baby syndrome)** do thiếu enzyme UDP-glucuronosyltransferase gan. |
| **Macrolid**<br>*(Erythromycin, Azithromycin, Clarithromycin)* & **Clindamycin** | **Tiểu đơn vị $50S$** của ribosome vi khuẩn | - Gắn vào rRNA $23S$ tại vị trí gần đường hầm thoát peptide (tunnel) của tiểu đơn vị $50S$.<br>- **Ngăn cản sự chuyển vị (translocation) của ribosome** và phong bế đường thoát của chuỗi peptide mới sinh, khiến chuỗi peptidyl-tRNA bị rơi rụng sớm. | - Điều trị nhiễm trùng đường hô hấp trên/dưới do vi khuẩn không điển hình (*Legionella, Mycoplasma*), thay thế dị ứng Penicillin.<br>- Tác dụng phụ: Kéo dài khoảng QT trên điện tim, ức chế CYP3A4 (Erythromycin), viêm đại tràng giả mạc do *C. difficile* (Clindamycin). |
| **Linezolid** (Oxazolidinone) | **Tiểu đơn vị $50S$** của ribosome vi khuẩn | - Gắn vào rRNA $23S$ tại giao diện với $30S$, ngăn cản sự lắp ráp của phức hợp mở đầu $70S$ ($30S + 50S$). | - Điều trị nhiễm khuẩn Gram (+) kháng thuốc nghiêm trọng như tụ cầu vàng kháng methicillin (MRSA) và cầu khuẩn ruột kháng vancomycin (VRE). |
| **Puromycin** | Cả ribosome **$70S$ và $80S$** | - Có cấu trúc tương đồng hóa học kỳ lạ với đầu $3'-tyrosyl-tRNA$.<br>- Puromycin chui vào vị trí A, tham gia nhận chuỗi peptid từ vị trí P tạo thành peptidyl-puromycin. Do không có liên kết với tRNA, chuỗi peptid bị **kết thúc sớm và giải phóng dở dang**. | - Sử dụng làm chất kháng sinh nghiên cứu trong phòng thí nghiệm; không dùng trên lâm sàng vì độc với cả tế bào người. |
| **Diphtheria Toxin** *(Độc tố bạch hầu)* | Yếu tố kéo dài **eEF2** ở tế bào nhân thực | - Phần A của ngoại độc tố xúc tác phản ứng chuyển nhóm ADP-ribose từ $\text{NAD}^+$ sang gắn đồng hóa trị vào gốc Diphthamide đặc thù trên **eEF2**, gây **bất hoạt vĩnh viễn eEF2**.<br>- Chấm dứt hoàn toàn sự chuyển vị dịch mã ở tế bào người, dẫn tới chết tế bào. | - Gây bệnh bạch hầu (*Corynebacterium diphtheriae*): tạo giả mạc hoại tử vùng hầu họng, độc tim (viêm cơ tim cấp) và liệt thần kinh ngoại biên. |
| **Cycloheximide** | **Tiểu đơn vị lớn $60S$** của ribosome nhân thực | - Ức chế hoạt tính Peptidyl transferase trên ribosome $80S$ của tế bào nhân thực; không tác động lên ribosom $70S$ vi khuẩn. | - Dùng trong nghiên cứu sinh học tế bào để chặn dịch mã nhân thực đặc hiệu. |

---

## 6. ĐIỀU HÒA BIỂU HIỆN GEN (REGULATION OF GENE EXPRESSION)

Tế bào không tổng hợp toàn bộ các loại protein mọi lúc với công suất tối đa mà liên tục điều chỉnh mức độ biểu hiện gen theo nhu cầu năng lượng, tình trạng dinh dưỡng và tín hiệu phát triển.

### 6.1. Điều hòa biểu hiện gen ở Sinh vật nhân sơ (Prokaryotes)

Ở vi khuẩn, mức độ điều hòa chủ yếu diễn ra tại **giai đoạn khởi đầu phiên mã** thông qua cấu trúc cụm gen chức năng gọi là **Operon**. Một operon điển hình gồm:
- **Promoter ($P$):** Vị trí khởi động gắn enzyme RNA polymerase.
- **Operator ($O$):** Vị trí vận hành gắn protein điều hòa.
- **Các gen cấu trúc ($Z, Y, A$ hoặc $TrpE, D, C, B, A$):** Mã hóa các enzyme trong cùng một con đường chuyển hóa.
- **Gen điều hòa ($R$ hoặc $I$):** Nằm ngoài operon, liên tục phiên mã tạo protein điều hòa (Repressor).

#### 6.1.1. Operon Lac (Mô hình cảm ứng kinh điển của Jacob & Monod - Nobel 1965)
Operon Lac của *E. coli* chứa 3 gen cấu trúc cần thiết cho việc vận chuyển và chuyển hóa đường lactose:
- $lacZ$: Mã hóa enzyme **$\beta$-galactosidase** (thủy phân lactose thành galactose và glucose; đồng phân hóa một lượng nhỏ thành allolactose).
- $lacY$: Mã hóa enzyme **Lactose permease** (bơm vận chuyển lactose qua màng tế bào).
- $lacA$: Mã hóa enzyme **Thiogalactoside transacetylase** (khử độc các dẫn xuất galactoside).

Hệ thống chịu sự điều hòa kép:
1. **Điều hòa âm tính (Negative control qua Allolactose):**
   - *Khi môi trường không có Lactose:* Protein ức chế LacI tự do ở trạng thái cấu hình hoạt động, gắn chặt vào Operator ($O$). Sự gắn này tạo cản trở không gian phong bế không cho RNA polymerase trượt từ Promoter sang các gen cấu trúc. Quá trình phiên mã bị tắt hoàn toàn (tiết kiệm năng lượng).
   - *Khi môi trường có Lactose:* Một lượng nhỏ allolactose (chất cảm ứng - inducer) tạo ra sẽ gắn vào protein ức chế LacI, gây biến đổi cấu hình dị lập thể khiến LacI mất ái lực và rời khỏi Operator. Operator được giải phóng, RNA polymerase tiến hành phiên mã cụm gen $lacZ, lacY, lacA$.
2. **Điều hòa dương tính (Positive control qua Glucose và cAMP-CAP):**
   - Vi khuẩn luôn ưu tiên tiêu thụ Glucose trước Lactose.
   - *Khi có nồng độ Glucose cao:* Enzyme Adenylyl cyclase bị ức chế $\to$ nồng độ $\text{cAMP}$ nội bào rất thấp. Protein hoạt hóa dị hóa **CAP (Catabolite Activator Protein)** không có cAMP sẽ không gắn vào Promoter. Tốc độ phiên mã của operon Lac chỉ ở mức nền rất thấp ngay cả khi có mặt lactose.
   - *Khi môi trường cạn kiệt Glucose nhưng có Lactose:* Tế bào phát tín hiệu "đói" $\to$ nồng độ $\text{cAMP}$ tăng vọt. $\text{cAMP}$ gắn vào CAP tạo phức hợp **cAMP-CAP**. Phức hợp này gắn vào vị trí gắn CAP ở ngay phía trước Promoter, làm bẻ cong sợi DNA và tăng ái lực của RNA polymerase với Promoter lên hàng chục lần, thúc đẩy phiên mã Operon Lac ở mức tối đa.

| Tình trạng môi trường Dinh dưỡng | Trạng thái Protein LacI | Nồng độ cAMP / Trạng thái CAP | Mức độ phiên mã Operon Lac |
| :--- | :--- | :--- | :--- |
| **+ Glucose, - Lactose** | Gắn chặt vào Operator (Khóa $O$) | cAMP thấp; CAP không gắn | **TẮT HOÀN TOÀN** (Không phiên mã) |
| **+ Glucose, + Lactose** | Allolactose gắn LacI; Rời $O$ | cAMP thấp; CAP không gắn | **MỨC NỀN CỰC THẤP** (Phiên mã yếu) |
| **- Glucose, - Lactose** | Gắn chặt vào Operator (Khóa $O$) | cAMP cao; Phức hợp cAMP-CAP gắn $P$ | **TẮT HOÀN TOÀN** (Bị khóa tại $O$) |
| **- Glucose, + Lactose** | Allolactose gắn LacI; Rời $O$ | cAMP cao; Phức hợp cAMP-CAP gắn $P$ | **BẬT TỐI ĐA** (Phiên mã cực mạnh) |


![Mô hình cảm ứng tổng hợp protein](hoasinh_media/HS-10_fig10_8.png)
*Hình 10.8. Mô hình cảm ứng tổng hợp protein (Operon Lac).*
#### 6.1.2. Operon Tryptophan (Mô hình kìm hãm và suy giảm - Attenuation)
Operon Trp mã hóa 5 enzyme tổng hợp acid amin Tryptophan:
- *Khi môi trường thiếu Tryptophan:* Protein ức chế TrpR ở trạng thái aporepressor bất hoạt, không gắn được vào Operator $\to$ Operon Trp được phiên mã tối đa để tổng hợp Tryptophan.
- *Khi Tryptophan dư thừa:* Tryptophan đóng vai trò là **chất đồng ức chế (corepressor)**, gắn vào TrpR làm chuyển sang cấu hình hoạt động gắn vào Operator, dập tắt phiên mã.
- *Cơ chế suy giảm (Attenuation):* Đoạn leader peptide phía trước operon chứa 2 codon Trp liên tiếp. Nếu thiếu Trp, ribosome bị ngập ngừng dừng lại ở các codon này, tạo điều kiện cho mRNA hình thành cấu trúc kẹp tóc $2-3$ (chống kết thúc), cho phép phiên mã tiếp tục. Nếu thừa Trp, ribosome trượt nhanh qua, thúc đẩy tạo cấu trúc kẹp tóc $3-4$ (tín hiệu kết thúc phụ thuộc Rho), cắt đứt phiên mã sớm.

![Mô hình kìm hãm tổng hợp protein](hoasinh_media/HS-10_fig10_9.png)
*Hình 10.9. Mô hình kìm hãm tổng hợp protein (Operon Tryptophan).*

---

### 6.2. Điều hòa biểu hiện gen ở Sinh vật nhân thực (Eukaryotes)

Khác với vi khuẩn, sinh vật nhân thực điều hòa biểu hiện gen ở nhiều tầng mức phân tử tinh vi:

#### 6.2.1. Điều hòa ở mức độ Dịch mã qua Phosphoryl hóa Yếu tố eIF2
Yếu tố mở đầu **eIF2** là tâm điểm kiểm soát tốc độ dịch mã chung của tế bào chất:
1. **Điều hòa tổng hợp Globin bởi Heme (HRI kinase):**
   - Trong tế bào tiền thân hồng cầu (hồng cầu lưới), chuỗi polypeptide Globin chỉ được phép tổng hợp khi có sẵn nhóm phụ Heme để tạo Hemoglobin chức năng, tránh tích lũy globin tự do gây kết tủa phá hủy tế bào.
   - *Khi Heme dồi dào:* Heme gắn ức chế enzyme **HRI (Heme-Regulated Inhibitor kinase)**. eIF2 ở trạng thái khử phosphoryl hóa hoạt động, chu kỳ tái nạp GTP nhờ eIF2B diễn ra trơn tru $\to$ chuỗi Globin được dịch mã mạnh mẽ.
   - *Khi thiếu sắt / thiếu Heme:* HRI kinase được giải phóng hoạt tính, xúc tác phosphoryl hóa tiểu đơn vị $\alpha$ của **eIF2** (tại gốc $Ser_{51}$). Dạng $\text{eIF2}(\alpha P)$ bẫy chặt yếu tố hoán đổi guanine **eIF2B** tạo phức hợp trơ vĩnh viễn, ngăn cản tái nạp $\text{GTP}$. Quá trình mở đầu dịch mã bị đình trệ hoàn toàn.
2. **Đáp ứng kháng virus bởi Interferon và PKR:**
   - Khi tế bào bị nhiễm virus, tế bào tiết ra **Interferon-$\alpha/\beta$**.
   - Interferon kích hoạt sự tổng hợp enzyme **Protein Kinase R (PKR)** trong tế bào.
   - RNA sợi đôi (dsRNA) của virus kích hoạt PKR tự phosphoryl hóa. Sau đó PKR phosphoryl hóa bất hoạt **eIF2-$\alpha$**, dập tắt toàn bộ quá trình sinh tổng hợp protein của tế bào ký chủ, khiến virus không thể nhân lên và tế bào nhiễm tự sát tế bào (apoptosis).

![Điều hòa tổng hợp protein bởi Interferon](hoasinh_media/HS-10_fig10_10.png)
*Hình 10.10. Điều hòa tổng hợp protein bởi interferon thông qua kích hoạt enzyme kinase phosphoryl hóa bất hoạt eIF2.*

#### 6.2.2. Điều hòa Biểu sinh (Epigenetics) và Cấu trúc Chromatin
- **Acetyl hóa Histone:** Enzyme *Histone Acetyltransferase (HAT)* chuyển nhóm acetyl từ Acetyl-CoA vào gốc Lysin trên đuôi histone, trung hòa điện tích dương của histone, làm lỏng lẻo tương tác tĩnh điện giữa histone và DNA tích điện âm $\to$ mở rộng chromatin (euchromatin), cho phép các yếu tố phiên mã tiếp cận gen để hoạt hóa phiên mã. Ngược lại, *Histone Deacetylase (HDAC)* đóng chặt chromatin (heterochromatin) làm câm lặng gen.
- **Methyl hóa DNA:** Xúc tác bởi DNA Methyltransferase (DNMT), gắn nhóm methyl vào carbon 5 của cytosine tại các đảo CpG ($5'\text{-m}^5\text{C-p-G-3'}$). Methyl hóa promoter thu hút các protein ức chế gắn vào, gây câm lặng gen bền vững qua các lần phân bào (bất hoạt nhiễm sắc thể X ở nữ giới, dấu ấn di truyền imprinting).

#### 6.2.3. Can thiệp RNA qua MicroRNA (miRNA)
- Phân tử miRNA ngắn ($21 - 25\text{ nucleotide}$) không mã hóa, được xử lý bởi enzyme Dicer và tích hợp vào phức hợp **RISC (RNA-Induced Silencing Complex)**.
- RISC-miRNA tìm đến bắt cặp bổ sung không hoàn toàn với vùng $3'\text{-UTR}$ của mRNA đích, dẫn tới **ức chế dịch mã** hoặc thúc đẩy quá trình cắt ngắn đuôi polyA và thoái hóa mRNA, đóng vai trò kiểm soát biểu hiện gen trong ung thư học và biệt hóa tế bào.

---

## 7. HỆ THỐNG CÂU HỎI LƯỢNG GIÁ VÀ TÌNH HUỐNG LÂM SÀNG

### 7.1. Câu hỏi trắc nghiệm khách quan (MCQs - Kèm đáp án và giải thích chi tiết)

#### Câu 1:
Trong quá trình sinh tổng hợp protein ở tế bào nhân sơ, enzyme peptidyl transferase đóng vai trò xúc tác hình thành liên kết peptid giữa acid amin mới tại vị trí A với chuỗi peptidyl-tRNA tại vị trí P. Bản chất hóa học thực sự của enzyme này là gì và nguồn năng lượng trực tiếp cung cấp cho phản ứng tạo liên kết peptid đến từ đâu?
- A. Một tiểu đơn vị protein đặc hiệu nằm trên tiểu đơn vị ribosom 30S; năng lượng từ sự thủy phân 1 phân tử ATP.
- B. Phân tử rRNA 23S của tiểu đơn vị lớn 50S (hoạt tính Ribozyme); năng lượng lấy trực tiếp từ liên kết este cao năng giữa chuỗi peptidyl và tRNA tại vị trí P.
- C. Phân tử rRNA 16S của tiểu đơn vị nhỏ 30S; năng lượng từ sự thủy phân 1 phân tử GTP liên kết với yếu tố EF-Tu.
- D. Enzyme aminoacyl-tRNA synthetase tự do trong tế bào chất; năng lượng do yếu tố EF-G thủy phân GTP cung cấp.

**Đáp án đúng: B**
*Giải thích chi tiết:*
- **B đúng:** Peptidyl transferase không phải là một enzyme protein cổ điển mà là một **Ribozyme** nằm trên tiểu đơn vị lớn của ribosom vi khuẩn, cấu tạo bởi phân tử **rRNA 23S** (hoặc rRNA 28S ở sinh vật nhân thực). Năng lượng để hình thành liên kết peptid không cần nguồn ATP hay GTP ngoại sinh thủy phân tại chỗ, mà lấy trực tiếp từ thế năng của **liên kết este cao năng** giữa nhóm carboxyl của acid amin (hoặc chuỗi peptid) và nhóm hydroxyl ở đầu $CCA-3'$ của tRNA vốn đã được tích lũy từ bước hoạt hóa acid amin trước đó.
- A, C, D sai: Sai về bản chất xúc tác (rRNA 23S chứ không phải protein hay rRNA 16S) và sai về nguồn gốc cung cấp năng lượng.

---

#### Câu 2:
Một bệnh nhân nữ 35 tuổi được chẩn đoán mắc viêm phổi cộng đồng không điển hình do vi khuẩn *Mycoplasma pneumoniae*. Bác sĩ kê đơn kháng sinh Azithromycin (thuốc nhóm Macrolid). Cơ chế tác dụng phân tử ở mức độ dịch mã của nhóm kháng sinh này đối với vi khuẩn là gì?
- A. Gắn không thuận nghịch vào rRNA 16S của tiểu đơn vị 30S, gây đọc sai mã di truyền.
- B. Gắn vào tiểu đơn vị 30S tại vị trí A, phong bế không gian ngăn cản aminoacyl-tRNA gắn vào ribosom.
- C. Gắn vào rRNA 23S của tiểu đơn vị 50S, ức chế sự chuyển vị (translocation) của ribosom dọc mRNA và phong bế đường hầm thoát peptide.
- D. Phong bế enzyme DnaG primase, ngăn chặn sự tổng hợp đoạn mồi RNA trong quá trình tái bản.

**Đáp án đúng: C**
*Giải thích chi tiết:*
- **C đúng:** Kháng sinh nhóm Macrolid (Azithromycin, Clarithromycin, Erythromycin) và Lincosamid (Clindamycin) gắn vào vùng rRNA 23S của tiểu đơn vị lớn 50S tại vị trí gần lối vào của đường hầm thoát chuỗi peptide (polypeptide exit tunnel). Sự gắn kết này ngăn cản chuyển động chuyển vị của ribosome (translocation) và ngăn cản chuỗi peptide mới sinh kéo dài chui qua đường hầm, dẫn tới việc chuỗi peptidyl-tRNA bị rơi rụng sớm khỏi ribosome, dập tắt quá trình dịch mã.
- A sai: Đây là cơ chế của nhóm Aminoglycosid (Gentamicin, Amikacin).
- B sai: Đây là cơ chế của nhóm Tetracyclin (Doxycycline).
- D sai: Tác động lên tái bản DNA, không phải dịch mã.

---

#### Câu 3:
Một trẻ nam 6 tuổi chưa được tiêm chủng vaccine mở rộng đầy đủ được đưa đến viện vì sốt, đau họng dữ dội, khó thở và xuất hiện mảng giả mạc màu xám dai dẳng bám chặt vào niêm mạc hầu họng. Bác sĩ chẩn đoán xác định bệnh Bạch hầu (*Corynebacterium diphtheriae*). Cơ chế gây độc tế bào của ngoại độc tố bạch hầu (Diphtheria toxin) ở mức độ sinh học phân tử là gì?
- A. Gắn vào tiểu đơn vị 30S làm sai lệch đọc mã codon trên mRNA.
- B. Xúc tác phản ứng ADP-ribosyl hóa bất hoạt vĩnh viễn yếu tố kéo dài eEF2 của tế bào nhân thực, đình trệ chuyển vị dịch mã.
- C. Ức chế cạnh tranh với ATP tại trung tâm hoạt động của aminoacyl-tRNA synthetase.
- D. Cắt đứt mũ 5'-cap của mRNA tế bào ký chủ khiến mRNA bị thoái hóa hàng loạt.

**Đáp án đúng: B**
*Giải thích chi tiết:*
- **B đúng:** Ngoại độc tố bạch hầu (Diphtheria toxin) do vi khuẩn *Corynebacterium diphtheriae* (mang phage $\beta$) tiết ra là một độc tố gồm 2 tiểu phần A và B. Tiểu phần A là một enzyme ADP-ribosyltransferase xâm nhập vào tế bào chất của tế bào ký chủ, xúc tác chuyển nhóm ADP-ribose từ $\text{NAD}^+$ sang gắn đồng hóa trị vào gốc acid amin Diphthamide biến đổi trên **yếu tố kéo dài eEF2 (eukaryotic Elongation Factor 2)**. Phản ứng này làm bất hoạt hoàn toàn eEF2, phong bế bước chuyển vị của ribosom 80S, làm đình trệ toàn bộ sinh tổng hợp protein của tế bào nhân thực, dẫn tới chết tế bào, hoại tử mô tạo giả mạc và viêm cơ tim.
- A sai: Vi khuẩn không tác động theo kiểu aminoglycoside.
- C, D sai: Không phải đích tác động của độc tố bạch hầu. Độc tố *Pseudomonas aeruginosa* (Exotoxin A) cũng có cơ chế ức chế eEF2 giống hệt độc tố bạch hầu.

---

#### Câu 4:
Trong mô hình điều hòa Operon Lac ở vi khuẩn *Escherichia coli*, khi vi khuẩn được nuôi cấy trong môi trường chứa **nồng độ Glucose cao và nồng độ Lactose cao**, trạng thái hoạt động của hệ thống điều hòa và mức độ biểu hiện của cụm gen cấu trúc $lacZ, lacY, lacA$ sẽ như thế nào?
- A. Protein ức chế LacI gắn chặt vào Operator; Operon bị khóa hoàn toàn không phiên mã.
- B. Protein ức chế LacI bị allolactose bất hoạt không gắn vào Operator; phức hợp cAMP-CAP không gắn vào Promoter; Operon phiên mã ở mức nền rất thấp.
- C. Phức hợp cAMP-CAP gắn mạnh vào Promoter kích hoạt phiên mã tối đa; protein LacI rời Operator.
- D. RNA polymerase bị thoái hóa hoàn toàn do hiện tượng kìm hãm dị hóa.

**Đáp án đúng: B**
*Giải thích chi tiết:*
- **B đúng:** Khi có Lactose: một lượng nhỏ allolactose hình thành sẽ gắn dị lập thể vào protein ức chế LacI, khiến nó đổi cấu hình và rời khỏi vị trí Operator ($O$), giải tỏa sự phong bế đối với RNA polymerase. Tuy nhiên, do môi trường có **nồng độ Glucose cao**, enzyme Adenylyl cyclase bị ức chế, dẫn đến nồng độ $\text{cAMP}$ nội bào rất thấp. Thiếu $\text{cAMP}$, protein CAP không thể tạo phức hợp cAMP-CAP để gắn vào vị trí hoạt hóa trước Promoter ($P$). Do thiếu sự hỗ trợ của phức hợp cAMP-CAP, RNA polymerase gắn vào promoter với ái lực rất yếu, khiến tốc độ phiên mã cụm gen $lacZ, lacY, lacA$ chỉ diễn ra ở **mức nền rất thấp** (chỉ đủ duy trì vài bản sao enzyme).
- A sai: Vì có mặt lactose nên LacI đã bị tách khỏi Operator.
- C sai: Nồng độ Glucose cao làm giảm cAMP, phức hợp cAMP-CAP không thể hình thành để kích hoạt phiên mã tối đa.
- D sai: RNA polymerase không bị thoái hóa.

---

#### Câu 5:
Một đột biến điểm xảy ra trên gen cấu trúc của chuỗi $\beta$-globin làm thay đổi codon tại vị trí số 6 từ $\text{5'-GAG-3'}$ (mã hóa cho Glutamat) thành codon $\text{5'-GUG-3'}$ (mã hóa cho Valin). Hậu quả dẫn tới bệnh Hồng cầu hình liềm (HbS). Dạng đột biến này thuộc loại đột biến di truyền nào sau đây?
- A. Đột biến vô nghĩa (Nonsense mutation).
- B. Đột biến sai nghĩa (Missense mutation).
- C. Đột biến đồng nghĩa / câm (Silent mutation).
- D. Đột biến lệch khung (Frameshift mutation).

**Đáp án đúng: B**
*Giải thích chi tiết:*
- **B đúng:** Đột biến sai nghĩa (Missense mutation) là đột biến thay thế nucleotide làm thay đổi bộ ba mã hóa từ acid amin này thành một acid amin khác. Trong bệnh hồng cầu hình liềm, base A tại vị trí thứ 2 của codon $\text{GAG}$ bị thay bằng U tạo thành $\text{GUG}$, làm thay thế gốc Glutamat (mang điện tích âm, ưa nước) tại vị trí số 6 của chuỗi $\beta$-globin thành Valin (kỵ nước, không mang điện tích). Sự xuất hiện của "miếng dán kỵ nước" Valin6 khiến phân tử HbS khi ở trạng thái khử oxy ($deoxy-HbS$) kết tập lại thành các sợi polymer hình que dài, làm biến dạng hồng cầu thành hình liềm dễ tắc mạch và tan máu.
- A sai: Đột biến vô nghĩa là thay đổi codon mã hóa thành một trong 3 codon kết thúc (UAA, UAG, UGA), tạo protein cắt cụt sớm.
- C sai: Đột biến đồng nghĩa là thay đổi nucleotide nhưng không làm đổi loại acid amin do tính thoái hóa của mã di truyền.
- D sai: Đột biến lệch khung là do mất hoặc thêm nucleotide không phải bội số của 3.

---

### 7.2. Câu hỏi Tự luận chuyên sâu (Kèm Barem điểm chi tiết)

#### Câu hỏi 1 (5,0 điểm):
**Trình bày cơ chế phân tử của quá trình dịch mã chuỗi polypeptide ở sinh vật nhân sơ (*E. coli*) qua 3 giai đoạn: Mở đầu, Kéo dài và Kết thúc. Phân tích chi phí năng lượng (tính theo liên kết phosphat cao năng tương đương ATP/GTP) để tổng hợp nên một liên kết peptid trong chuỗi polypeptide.**

#### BAREM ĐÁP ÁN VÀ THANG ĐIỂM CHI TIẾT CÂU 1:

| Nội dung yêu cầu | Điểm thành phần |
| :--- | :--- |
| **1. Giai đoạn Mở đầu chuỗi (Initiation):**<br>- Tiểu đơn vị 30S gắn IF3 (ngăn gắn sớm với 50S) và IF1 (phong bế vị trí A).<br>- Đoạn giàu pyrimidine ở đầu $3'$ của $16S\text{ rRNA}$ bắt cặp bổ sung với trình tự giàu purine **Shine-Dalgarno** ($\text{5'-AGGAGGU-3'}$) trên mRNA, định vị codon mở đầu $\text{5'-AUG-3'}$ chính xác vào vị trí P.<br>- Phức hợp $\text{IF2-GTP}$ đưa aminoacyl-tRNA mở đầu đặc hiệu là **fMet-tRNA$^{\text{fMet}}$** vào vị trí P, anticodon bắt cặp với codon AUG.<br>- IF3 rời đi; tiểu đơn vị lớn 50S tiến vào gắn kết; hoạt tính GTPase của IF2 được kích hoạt thủy phân $\text{GTP} \to \text{GDP} + P_i$; IF1 và IF2-GDP tách rời tạo nên phức hợp mở đầu 70S hoạt động với fMet-tRNA tại vị trí P. | **1,5 điểm**<br>(0,5 điểm cho nhận diện Shine-Dalgarno; 0,5 điểm cho vai trò IF2 và fMet-tRNA; 0,5 điểm cho lắp ráp tiểu đơn vị 50S và thủy phân GTP) |
| **2. Giai đoạn Kéo dài chuỗi (Elongation) - Chu kỳ 3 bước:**<br>- **Bước 1 (Gắn aminoacyl-tRNA vào vị trí A):** Phức hợp $\text{EF-Tu}\cdot\text{GTP}\cdot\text{Aminoacyl-tRNA}$ đưa aminoacyl-tRNA kế tiếp vào vị trí A. Sự bắt cặp codon-anticodon chính xác kích hoạt EF-Tu thủy phân $\text{GTP} \to \text{GDP} + P_i$, EF-Tu-GDP rời đi (tiêu tốn 1 GTP).<br>- **Bước 2 (Hình thành liên kết peptid):** Hoạt tính **Peptidyl transferase** của **rRNA 23S** (ribozyme) xúc tác chuyển chuỗi peptid từ vị trí P sang nhóm amin của aminoacyl-tRNA tại vị trí A qua liên kết peptid. Bước này không dùng ATP/GTP tự do mà dùng thế năng liên kết este cao năng của aminoacyl-tRNA.<br>- **Bước 3 (Chuyển vị Translocation):** Yếu tố **EF-G gắn GTP** thúc đẩy ribosom trượt 1 codon theo chiều $5' \to 3'$. Thủy phân $\text{GTP} \to \text{GDP} + P_i$ đẩy tRNA rỗng sang vị trí E rồi rời ribosom, chuyển peptidyl-tRNA từ vị trí A sang vị trí P, giải phóng vị trí A sẵn sàng đón tRNA mới (tiêu tốn 1 GTP). | **1,5 điểm**<br>(0,5 điểm cho bước gắn vị trí A và vai trò EF-Tu; 0,5 điểm cho peptidyl transferase rRNA 23S; 0,5 điểm cho chuyển vị EF-G) |
| **3. Giai đoạn Kết thúc chuỗi (Termination):**<br>- Khi một trong 3 codon kết thúc (UAA, UAG, UGA) xuất hiện tại vị trí A, không có tRNA tương ứng.<br>- Các yếu tố giải phóng **RF1** (nhận diện UAA, UAG) hoặc **RF2** (nhận diện UAA, UGA) cùng **RF3-GTP** gắn vào vị trí A.<br>- RF kích hoạt peptidyl transferase chuyển chuỗi peptid sang phân tử $H_2O$, thủy phân giải phóng chuỗi polypeptide hoàn chỉnh khỏi tRNA ở vị trí P.<br>- Yếu tố tái chế ribosome **RRF** và EF-G cùng sự thủy phân thêm GTP/ATP làm phân ly hoàn toàn phức hợp ribosom 70S thành các tiểu đơn vị 30S, 50S, mRNA và tRNA rỗng để tái sử dụng. | **1,0 điểm**<br>(0,5 điểm cho nhận diện codon kết thúc bởi RF1/RF2; 0,5 điểm cho thủy phân giải phóng chuỗi polypeptide và tái chế ribosom) |
| **4. Phân tích Chi phí Năng lượng:**<br>- Để kết hợp 1 acid amin vào chuỗi polypeptide, tế bào tiêu tốn ít nhất **4 liên kết phosphat cao năng** ($\,\sim 4\,\text{ATP/GTP}$):<br>+ **2 liên kết cao năng** cho quá trình Hoạt hóa acid amin: $\text{Acid amin} + \text{ATP} + \text{tRNA} \to \text{Aminoacyl-tRNA} + \text{AMP} + 2\,P_i$ (do enzyme inorganic pyrophosphatase thủy phân ngay $PP_i \to 2\,P_i$, tương đương 2 ATP).<br>+ **1 liên kết cao năng** (1 GTP) cho sự gắn kết chính xác aminoacyl-tRNA vào vị trí A nhờ EF-Tu.<br>+ **1 liên kết cao năng** (1 GTP) cho sự chuyển vị của ribosom dọc mRNA nhờ EF-G.<br>- Nhận định ý nghĩa sinh học: Năng lượng tiêu tốn rất lớn phản ánh cái giá nhiệt động học bắt buộc để duy trì tính trung thực và độ chính xác tối cao của mã di truyền. | **1,0 điểm**<br>(0,5 điểm cho tính toán chính xác 4 liên kết cao năng; 0,5 điểm cho giải thích phân tích chi tiết từng vị trí và ý nghĩa sinh học) |

---

#### Câu hỏi 2 (5,0 điểm):
**Phân tích cơ chế điều hòa biểu hiện gen của mô hình Operon Lac ở vi khuẩn *E. coli* theo thuyết Jacob & Monod. Phân biệt rõ vai trò của cơ chế điều hòa âm tính (qua Protein ức chế LacI và Allolactose) và cơ chế điều hòa dương tính (qua nồng độ Glucose, cAMP và protein CAP). Nêu ý nghĩa sinh học và ứng dụng của operon Lac trong công nghệ biểu hiện protein tái tổ hợp.**

#### BAREM ĐÁP ÁN VÀ THANG ĐIỂM CHI TIẾT CÂU 2:

| Nội dung yêu cầu | Điểm thành phần |
| :--- | :--- |
| **1. Cấu trúc chức năng của Operon Lac:**<br>- Trình bày đầy đủ cấu trúc gồm: Vị trí khởi động Promoter ($P$), vị trí vận hành Operator ($O$), và 3 gen cấu trúc:<br>+ $lacZ$: Mã hóa enzyme **$\beta$-galactosidase** (thủy phân lactose thành galactose và glucose; tạo allolactose).<br>+ $lacY$: Mã hóa **Lactose permease** (vận chuyển lactose qua màng).<br>+ $lacA$: Mã hóa **Thiogalactoside transacetylase** (khử độc galactoside).<br>- Gen điều hòa $lacI$: Nằm phía trước operon, liên tục phiên mã tạo protein ức chế LacI. | **1,0 điểm**<br>(0,5 điểm cho promoter, operator, gen I; 0,5 điểm cho 3 gen cấu trúc và enzyme tương ứng) |
| **2. Cơ chế Điều hòa Âm tính (Negative Control):**<br>- **Khi không có lactose:** Protein ức chế LacI ở trạng thái hoạt động tự nhiên, gắn chặt vào Operator ($O$). Sự gắn này phong bế vật lý sự di chuyển của RNA polymerase từ Promoter vào các gen cấu trúc $\to$ Quá trình phiên mã bị khóa tắt hoàn toàn.<br>- **Khi có lactose:** Một lượng nhỏ lactose vào tế bào chuyển thành **Allolactose** (chất cảm ứng inducer). Allolactose gắn dị lập thể vào LacI làm thay đổi cấu hình không gian $\to$ LacI mất ái lực, rời khỏi Operator $\to$ Operator được giải phóng, RNA polymerase có thể tiến hành phiên mã. | **1,5 điểm**<br>(0,75 điểm cho trạng thái không có lactose; 0,75 điểm cho vai trò allolactose làm rời LacI khỏi operator) |
| **3. Cơ chế Điều hòa Dương tính (Positive Control) và Hiện tượng kìm hãm dị hóa:**<br>- Vi khuẩn ưu tiên sử dụng Glucose. Nồng độ Glucose cao ức chế enzyme Adenylyl cyclase $\to$ Nồng độ $\text{cAMP}$ nội bào rất thấp.<br>- Khi Glucose cạn kiệt: Nồng độ $\text{cAMP}$ tăng cao, gắn vào protein hoạt hóa dị hóa CAP tạo thành phức hợp **cAMP-CAP**.<br>- Phức hợp cAMP-CAP gắn vào vị trí gắn CAP ở phía trước Promoter, bẻ cong sợi DNA và tương tác trực tiếp với RNA polymerase, làm tăng ái lực gắn của enzyme này lên hàng chục lần $\to$ Thúc đẩy phiên mã ở mức tối đa.<br>- Tóm tắt 4 trạng thái môi trường: (- Glu, + Lac): BẬT TỐI ĐA; (+ Glu, + Lac): PHIÊN MÃ MỨC NỀN; (- Lac): TẮT HOÀN TOÀN bất kể có glucose hay không. | **1,5 điểm**<br>(0,5 điểm cho cơ chế chuyển hóa glucose và cAMP; 0,5 điểm cho vai trò phức hợp cAMP-CAP bẻ cong DNA; 0,5 điểm cho bảng 4 trạng thái phối hợp) |
| **4. Ý nghĩa sinh học và Ứng dụng trong Công nghệ Sinh học:**<br>- **Ý nghĩa sinh học:** Giúp vi khuẩn thích ứng tối ưu với môi trường dinh dưỡng, tiết kiệm tối đa năng lượng và acid amin, chỉ tổng hợp enzyme khi có cơ chất và khi nguồn carbon ưu tiên (glucose) cạn kiệt.<br>- **Ứng dụng công nghệ:**<br>+ Được sử dụng làm hệ thống vector biểu hiện gen tái tổ hợp (như hệ plasmid pET) để sản xuất protein trị liệu (Insulin, Somatotropin).<br>+ Sử dụng chất cảm ứng tương đồng **IPTG (Isopropyl $\beta$-D-1-thiogalactopyranoside)**: IPTG gắn bất hoạt protein ức chế LacI nhưng không bị $\beta$-galactosidase thủy phân, duy trì trạng thái cảm ứng phiên mã gen ngoại lai liên tục với hiệu suất cực cao. | **1,0 điểm**<br>(0,5 điểm cho ý nghĩa sinh học thích ứng và tiết kiệm; 0,5 điểm cho vector biểu hiện gen và ứng dụng chất cảm ứng IPTG) |

---

## 8. TÀI LIỆU THAM KHẢO CHUẨN MỰC
1. GS. TS. BS. Tạ Thành Văn (Chủ biên) (2023). *Giáo trình Hóa sinh Y học*, Tái bản lần thứ 7, Nhà xuất bản Y học Hà Nội (Chương 12: Sinh tổng hợp Protein, Tr. 216 – 233).
2. David L. Nelson, Michael M. Cox (2021). *Lehninger Principles of Biochemistry*, 8th Edition, W. H. Freeman and Company (Chapter 27: Protein Metabolism; Chapter 28: Regulation of Gene Expression).
3. Victor W. Rodwell, David A. Bender, Kathleen M. Botham, Peter J. Kennelly, P. Anthony Weil (2022). *Harper’s Illustrated Biochemistry*, 32nd Edition, McGraw-Hill Education (Chapter 37: Protein Synthesis and the Genetic Code; Chapter 38: Regulation of Gene Expression).
4. Bruce Alberts, Alexander Johnson, Julian Lewis, David Morgan, Martin Raff, Keith Roberts, Peter Walter (2022). *Molecular Biology of the Cell*, 7th Edition, W. W. Norton & Company (Chapter 6: How Cells Read the Genome: From DNA to Protein; Chapter 7: Control of Gene Expression).
5. Bertram G. Katzung, Anthony J. Trevor (2021). *Basic & Clinical Pharmacology*, 15th Edition, McGraw-Hill (Chapter 44: Protein Synthesis Inhibitors).
