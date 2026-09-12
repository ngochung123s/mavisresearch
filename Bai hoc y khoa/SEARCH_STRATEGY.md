# SEARCH_STRATEGY.md — Chiến lược tìm kiếm tài liệu cho bài học Sản Phụ khoa

> **Mục đích:** Mô tả cách tìm tài liệu cho mỗi loại nội dung trong bài học, từ guideline đến kiến thức nền.
> **Cập nhật:** 2026-07-15 (test thực tế trên 2 chủ đề: sinh non & GDM)
> **Công cụ:** `C:\Users\THANHANH\.local\bin\biomcp.exe` + web trực tiếp (`read`)

---

## Tại sao cần chiến lược tìm kiếm?

Qua các bài trước, mình tìm article bằng keyword đơn giản (`-k "..." --limit 5`). Cách này **vẫn tìm được bài** nhưng:

- Tốn 2-3 vòng trial-and-error, không có cấu trúc
- Không phân biệt guideline vs meta-analysis vs RCT
- Bỏ sót evidence vì không snowball
- Không dùng entity-typed search → bỏ sót paper dùng từ khác cho cùng bệnh
- Chỉ tìm trên PubMed → bỏ sót guideline từ web xã hội nghề nghiệp

File này thay thế cách cũ bằng một pipeline có cấu trúc.

---

## Khái niệm cốt lõi

### Entity-typed search — "Hỏi PubMed bằng KHÁI NIỆM, không phải CHỮ"

Khi bạn search `-k "preterm birth"`, PubMed tìm paper có **chính xác chữ đó**. Nhưng tác giả khác nhau dùng từ khác nhau cho cùng 1 bệnh:

| Bài A | Bài B | Bài C |
|---|---|---|
| "preterm birth" | "premature labor" | "PTB" |

→ Search bằng keyword bỏ sót bài B và C.

**Giải pháp:** `-d "premature birth"` map thẳng vào MeSH — bộ từ điển có kiểm soát của PubMed. Mọi paper về sinh non đều được gắn tag MeSH D047928, bất kể tác giả dùng từ gì.

```
"preterm birth" ──┐
"premature labor" ─┼──→ MeSH D047928 ──→ TÌM ĐƯỢC TẤT CẢ
"PTB" ────────────┘
```

### Citation graph — "1 paper tốt dẫn tới 10 paper liên quan"

Mỗi paper là một nút trong mạng lưới. Từ 1 paper, bạn đi được 3 hướng:

```
                    ┌─→ Citations: ai cite paper này? = evidence MỚI HƠN
                    │
BEST PAPER ─────────┼─→ References: paper này cite ai? = evidence NỀN
                    │
                    └─→ Recommendations: paper tương tự? = góc nhìn KHÁC
```

**Ví dụ thực tế (GDM):** Meta-analysis PMID 30103263 về treatment GDM → dùng `article citations` → tìm thấy GRACE trial (RCT đa trung tâm về CGM trong GDM). Search keyword thường **không bao giờ** tìm ra GRACE trial vì title của nó không chứa "metformin" hay "insulin". Nhưng vì nó cite meta-analysis về treatment GDM → citation graph phát hiện được.

---

## Tầng tìm kiếm — 2 tầng riêng biệt

### Tầng 0: Web trực tiếp xã hội nghề nghiệp (Tier 0 guideline)

**Vấn đề:** PubMed không phủ toàn bộ guideline. Nhiều guideline quan trọng tồn tại dạng PDF trên web xã hội nghề nghiệp, dài hơn và chi tiết hơn bản PubMed. Ví dụ: ISUOG guideline có flowchart, bảng, hình ảnh mà bản article trên *Ultrasound Obstet Gynecol* bị cắt.

**Giải pháp:** Bước đầu tiên của mọi bài học là vào web xã hội nghề nghiệp.

```
Dùng read() để vào thẳng trang guideline:
read https://www.isuog.org/clinical-resources/isuog-guidelines.html
read https://www.acog.org/clinical/clinical-guidance
read https://www.aium.org/resources/guidelines.aspx
read https://www.smfm.org/clinical-guidance
read https://www.figo.org/guidelines
read https://www.asrm.org/practice-guidance
read https://www.rcog.org.uk/guidance
read https://www.nice.org.uk/guidance
```

**Kết quả mong đợi:**
- Tìm thấy guideline liên quan → dùng bản web làm nguồn chính (cite: `[GUIDELINE VERIFIED] Society YYYY`)
- Nếu guideline đó cũng có PMID → cite cả hai: bản web đầy đủ + PMID để truy xuất
- Nếu không có guideline nào → ghi nhận và tiếp tục tìm trên PubMed

### Tầng 1: PubMed + Europe PMC (article)

Đây là tầng tìm article học thuật qua biomcp. **Lưu ý quan trọng về `--source` và `--type`:**

| Lệnh | Semantic Scholar? | Phủ được gì? | Trạng thái |
|---|---|---|---|
| `search article` (mặc định) | ✅ Có | PubMed + Europe PMC + Semantic Scholar + PubTator3 | ⚠️ S2 rate limit + PubTator3 lỗi → kết quả thiếu |
| `search article --source pubmed` | ❌ Tắt | Chỉ PubMed | ✅ **Ổn định — khuyến nghị** |
| `search article --source europepmc` | ❌ Tắt | Chỉ Europe PMC | ✅ **Ổn định — nhanh nhất (~7s)** |
| `search article --type review` | ❌ Tắt | Chỉ Europe PMC + PubMed | ✅ OK |
| `search article --type meta-analysis` | ❌ Tắt | Chỉ Europe PMC + PubMed | ✅ OK |

→ **Luôn dùng `--source pubmed` hoặc `--source europepmc`** thay vì mặc định. Khi cần lọc, thêm `--type`.

---

## Quy trình tìm kiếm chuẩn — 6 bước

> **QUAN TRỌNG (cập nhật 2026-07-19):** Semantic Scholar + PubTator3 trong biomcp
> hiện không khả dụng (rate limit + HTML error). Để search ổn định, LUÔN thêm
> `--source pubmed` hoặc `--source europepmc`:
> ```bash
> # PubMed only — ổn định nhất, ~15s
> biomcp search article --source pubmed -d "<disease>" -k "<keywords>" --limit 10
>
> # Europe PMC only — nhanh hơn (~7s), có fulltext link
> biomcp search article --source europepmc -d "<disease>" -k "<keywords>" --limit 10
> ```
> `biomcp get article <PMID>` hiện KHÔNG hoạt động (lỗi PubTator3).
> Dùng `python 10_Script Python/fetch_article.py --pmid <PMID>` thay thế.

```bash
# ═══════════════════════════════════════════════════════════════
# BƯỚC 0: Web trực tiếp — tìm guideline gốc từ xã hội nghề nghiệp
# ═══════════════════════════════════════════════════════════════

# Vào web xã hội nghề nghiệp liên quan đến chủ đề:
# - Siêu âm Sản Phụ khoa → ISUOG, AIUM
# - Sản khoa tổng quát → ACOG, RCOG, NICE, FIGO, SMFM
# - ART / Hiếm muộn → ASRM, ESHRE
# - Ung thư Phụ khoa → ESGO, IGCS

# Mục tiêu: 1-2 guideline chính thức. Cite format:
# [GUIDELINE VERIFIED: Society YYYY — Document ID]


# ═══════════════════════════════════════════════════════════════
# BƯỚC 1: Tìm guideline/article trên PubMed (bổ sung)
# ═══════════════════════════════════════════════════════════════
# Dùng entity-typed + keyword đặc hiệu + --source pubmed.

biomcp search article \
  --source pubmed \
  -d "<disease>" \
  -k "<specific diagnostic criteria hoặc procedure>" \
  --sort date \
  --year-min 2022 \
  --limit 10

# Ví dụ GDM:
biomcp search article \
  --source pubmed \
  -d "diabetes gestational" \
  -k "oral glucose tolerance test diagnostic criteria screening" \
  --sort date --year-min 2022 --limit 10

# Ví dụ Sinh non:
biomcp search article \
  --source pubmed \
  -d "premature birth" \
  -k "cervical length screening transvaginal ultrasound cutoff" \
  --sort date --year-min 2022 --limit 10


# ═══════════════════════════════════════════════════════════════
# BƯỚC 2: Tìm meta-analysis / systematic review (xương sống evidence)
# ═══════════════════════════════════════════════════════════════
# --type meta-analysis + --source europepmc.

biomcp search article \
  --source europepmc \
  -d "<disease>" \
  -k "<intervention hoặc câu hỏi cụ thể>" \
  --type meta-analysis \
  --year-min 2018 \
  --sort citations \
  --limit 10

# Ví dụ Sinh non:
biomcp search article \
  --source europepmc \
  -d "premature birth" \
  -k "progesterone vaginal cerclage prevention randomized" \
  --type meta-analysis --year-min 2018 --sort citations --limit 10

# Ví dụ GDM:
biomcp search article \
  --source europepmc \
  -d "diabetes gestational" \
  -k "metformin versus insulin pregnancy outcomes" \
  --type meta-analysis --year-min 2018 --sort citations --limit 10


# ═══════════════════════════════════════════════════════════════
# BƯỚC 3: Citation snowball — từ 1 meta-analysis tốt → mạng lưới
# ═══════════════════════════════════════════════════════════════
# Lấy PMID của meta-analysis có citations cao nhất từ Bước 2.

BEST=...  # PMID tốt nhất từ bước 2

# Cách nhanh (fetch_article.py — NCBI elink, ~5s):
# 3a. Paper này cite những gì? → evidence NỀN
python 10_Script Python/fetch_article.py --pmid $BEST --references --limit 15 --tldr

# 3b. Ai cite paper này? → evidence MỚI HƠN
python 10_Script Python/fetch_article.py --pmid $BEST --citations --limit 10 --tldr

# Cách chi tiết (Europe PMC skill — có title, journal, hitCount, ~6s):
# 3a. Evidence NỀN:
uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py get_references MED $BEST --page_size 15 --output refs.json

# 3b. Evidence MỚI:
uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py get_citations MED $BEST --page_size 10 --output cites.json


# ═══════════════════════════════════════════════════════════════
# BƯỚC 4: Tìm kiến thức nền — review article về anatomy/physiology
# ═══════════════════════════════════════════════════════════════
# PHẢI có -d, nếu không sẽ ra kết quả không liên quan (bài học từ GDM).

biomcp search article \
  --source europepmc \
  -d "<disease>" \
  -k "pathophysiology mechanism review" \
  --type review \
  --sort citations \
  --limit 10

# Nếu cần anatomy thuần túy (không phải bệnh) → PubMed Bookshelf:
# read https://www.ncbi.nlm.nih.gov/books/
# Cite: [TEXTBOOK: Tên sách, chương, ấn bản. NBK ID]

# Ví dụ Sinh non:
biomcp search article \
  --source europepmc \
  -d "premature birth" \
  -k "cervical remodeling biomechanics mechanism review" \
  --type review --sort citations --limit 10

# Ví dụ GDM (sửa từ lỗi cũ):
biomcp search article \
  --source europepmc \
  -d "diabetes gestational" \
  -k "pathophysiology insulin resistance placental hormones mechanism review" \
  --type review --sort citations --limit 10


# ═══════════════════════════════════════════════════════════════
# BƯỚC 5: Tìm RCT gần đây — cập nhật mới nhất
# ═══════════════════════════════════════════════════════════════

biomcp search article \
  --source europepmc \
  -d "<disease>" \
  -k "<intervention> randomized trial" \
  --type research-article \
  --sort date \
  --year-min 2023 \
  --limit 10
```

---

## Sau khi tìm được paper — Fetch pipeline (3 bước)

Có 15-25 paper từ 6 bước search. Không fetch hết — **lọc bằng TLDR trước, chỉ fetch sâu paper đáng đọc.**

```
BƯỚC A: SCAN NHANH       →  python 10_Script Python/fetch_article.py --pmid <PMID> --tldr
         Mỗi paper 1 dòng: tác giả + tạp chí + năm + loại article + câu đầu abstract
         → Loại paper không liên quan, citation quá thấp
         → Còn ~5 paper đáng đọc

BƯỚC B: ĐỌC ABSTRACT     →  python 10_Script Python/fetch_article.py --pmid <PMID> --abstract
         Abstract đầy đủ 4 phần: Background, Methods, Results, Conclusions (từ efetch XML)
         → Xác nhận số liệu (RR, CI, n) trong abstract
         → Gắn tag [ABSTRACT VERIFIED]

BƯỚC C: ĐỌC TOÀN VĂN     →  python 10_Script Python/fetch_article.py --pmid <PMID> --fulltext
                               hoặc: uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py download_pdf <PMCID> --output paper.pdf
         Chỉ cho paper QUAN TRỌNG NHẤT (meta-analysis nền, guideline gốc)
         → Gắn tag [FULL VERIFIED]
         → Không phải paper nào cũng có fulltext miễn phí (~50% thành công)
         → fetch_article.py dùng PMC efetch (plain text), europepmc_api.py dùng PDF download
```

### So sánh các phương pháp fetch

| Phương pháp | Tool | Thời gian | Trả về | Dùng khi |
|---|---|---|---|---|
| **TLDR** | `fetch_article.py --tldr` | ~3s | 1 dòng: tác giả + journal + năm + loại + câu đầu abstract | Scan 15 paper → chọn 5 đáng đọc |
| **Metadata JSON** | `fetch_article.py --pmid` | ~3s | Title, authors, journal, year, DOI, PMCID, pub types | Cần metadata không cần abstract |
| **Abstract XML** | `fetch_article.py --abstract` | ~3s | Abstract 4 phần (Background, Methods, Results, Conclusions) | Verify claims, trích số liệu |
| **Citation graph** | `fetch_article.py --citations/--references` | ~5s | Danh sách PMID cite/được cite | Snowball từ 1 paper tốt (nhanh) |
| **Citation graph (đầy đủ)** | `europepmc_api.py get_citations/get_references` | ~6s | JSON đầy đủ (title, author, journal, year) | Snowball chi tiết, có hitCount |
| **Fulltext** | `fetch_article.py --fulltext` hoặc `europepmc_api.py download_pdf` | ~10-30s | Toàn văn (nếu PMC OA) | Cần FULL VERIFIED — không ổn định |

### Nguyên tắc

- **Không fetch fulltext tất cả** — tốn thời gian, nhiều paper không có
- **TLDR luôn là bước đầu tiên** — 1 dòng đủ để loại paper không liên quan
- **XML Abstract cho ABSTRACT VERIFIED, Fulltext cho FULL VERIFIED** — đúng tier annotation
- **fetch_article.py dùng NCBI E-utilities** — KHÔNG phụ thuộc PubTator3 hay Semantic Scholar
- **europepmc_api.py dùng Europe PMC** — thay thế citation graph khi cần metadata chi tiết hơn
- **Fallback:** `fetch_article.py --pmid` (JSON metadata, 2-3s) khi chỉ cần tác giả, tạp chí, DOI

### Bài học từ thực thi (cập nhật 2026-07-19 — IM-16)

1. **PLAN PMIDs KHÔNG ĐƯỢC TIN TƯỞNG MÙ QUÁNG.** Luôn `fetch_article.py --pmid` để xác nhận trước khi cite. IM-16 có 2 PMID trong plan SAI: 33512469 (ESGE) thực tế là paper về TB; đúng là 33567467. 31501175 (BSG) là case report Sertoli-Leydig; BSG không có guideline upper GI riêng. Luôn verify, không assume.

2. **`biomcp.exe` (không full path) + `--source europepmc` là combo ổn định nhất.** Europe PMC nhanh hơn PubMed (~7s vs ~15s), không bị rate limit Semantic Scholar. Dùng forward slash cho path Windows trong bash.

3. **Nếu biomcp search bị truncate output → chuyển sang `fetch_article.py` trực tiếp qua PMID.** Không cần chạy lại search nhiều lần. Đã biết PMID → fetch thẳng.

4. **`verify_claims --strict` có ngưỡng thực tế ≤3 residual block.** Nguyên nhân: NCBI E-utilities trả về abstract bị cắt cụt (có dấu `…`), script không tìm thấy số liệu dù full abstract có. Đã verify thủ công với `fetch_article.py --abstract` → chấp nhận residual. Không chase 100%.

5. **Viết RESEARCH_BRIEF trước MD.** Brief là claims registry — mọi số liệu trong MD phải có trong brief. Làm ngược → mất thời gian sửa verify_claims.

6. **Self-audit gates trước khi báo cáo done.** Chạy tất cả script xác minh, đọc output, xác nhận chạy đúng file. Ở IM-16, `verify_diacritics.py` chạy trên file IM-40 thay vì IM-16 do hardcode path.

## MeSH mapping — disease entity reference

Khi dùng `-d`, biomcp map sang MeSH. Bảng dưới là các entity thường dùng trong Sản Phụ khoa:

| Chủ đề | Flag `-d` |
|---|---|
| Sinh non | `"premature birth"` |
| Tiền sản giật | `"pre-eclampsia"` |
| ĐTĐ thai kỳ | `"diabetes gestational"` |
| Sảy thai liên tiếp | `"abortion habitual"` |
| OHSS | `"ovarian hyperstimulation syndrome"` |
| Lạc nội mạc tử cung | `"endometriosis"` |
| U xơ tử cung | `"leiomyoma"` |
| PCOS | `"polycystic ovary syndrome"` |
| Vô sinh | `"infertility"` |
| Mãn kinh | `"menopause"` |
| PPROM | `"fetal membranes premature rupture"` |
| Thai ngoài tử cung | `"pregnancy ectopic"` |
| Rau tiền đạo | `"placenta previa"` |
| Rau bong non | `"abruptio placentae"` |
| Đa ối | `"polyhydramnios"` |
| Thiểu ối | `"oligohydramnios"` |
| FGR | `"fetal growth retardation"` |
| Song thai | `"pregnancy twin"` |
| Nhiễm trùng hậu sản | `"puerperal infection"` |
| Viêm vùng chậu | `"pelvic inflammatory disease"` |
| Ung thư cổ tử cung | `"uterine cervical neoplasms"` |
| Ung thư nội mạc | `"endometrial neoplasms"` |
| Ung thư buồng trứng | `"ovarian neoplasms"` |

---

## Kỹ thuật nâng cao

### Citation snowball

Từ 1 paper tốt, đi 3 hướng bằng 2 công cụ:

**Cách nhanh (fetch_article.py — NCBI elink):**

```bash
BEST=30103263  # PMID của meta-analysis tốt nhất

# Evidence mới (ai cite paper này?)
python 10_Script Python/fetch_article.py --pmid $BEST --citations --limit 10 --tldr

# Evidence nền (paper này cite ai?)
python 10_Script Python/fetch_article.py --pmid $BEST --references --limit 10 --tldr
```

**Cách chi tiết (Europe PMC skill — có title, author, journal, hitCount):**

```bash
# Evidence nền (paper này cite ai?)
uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py get_references MED $BEST --page_size 15 --output refs.json

# Evidence mới (ai cite paper này?)
uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py get_citations MED $BEST --page_size 10 --output cites.json

# Paper tương tự → dùng biomcp search với keyword từ paper
# (biomcp article recommendations không khả dụng do Semantic Scholar rate limit)
```

### Hybrid ranking

```bash
# Khi cần evidence vừa liên quan semantic vừa có ảnh hưởng cao
biomcp search article \
  -d "endometriosis" \
  -k "infertility ART outcome" \
  --ranking-mode hybrid \
  --weight-semantic 0.3 \
  --weight-citations 0.4 \
  --weight-lexical 0.3 \
  --limit 10
```

### Session loop-breaker

```bash
# Tự động gợi ý query thay thế khi kết quả kém
biomcp --json search article -k "cervical length screening" --session ob-lesson-1 --limit 10
# → _meta.suggestions chứa query thay thế nếu overlap >60%
```

### PubMed Bookshelf

```
read https://www.ncbi.nlm.nih.gov/books/
Cite: [TEXTBOOK: Tên sách, chương, ấn bản. NBK ID]
```

---

## Bằng chứng — Test thực tế 2026-07-15

### Test 1: Sinh non + Cổ tử cung

| | Cách cũ | Cách mới |
|---|---|---|
| Query | `-k "sinh non preterm birth cervical length guideline"` | 6 bước (web + biomcp entity-typed + snowball) |
| Paper đúng chủ đề | 0 | 12 |
| Meta-analysis | 0 | 4 (có bài 112 citations: "Progesterone = Cerclage") |
| Evidence từ snowball | 0 | 3 |
| Kiến thức nền | 0 | 3 review kinh điển (97-253 citations) |

### Test 2: GDM

| | Cách cũ | Cách mới |
|---|---|---|
| Query | `-k "GDM gestational diabetes screening guideline"` | 6 bước |
| Paper đúng chủ đề | 0 | 15 |
| Meta-analysis | 0 | 4 (có Cochrane overview 83 citations) |
| Evidence từ snowball | 0 | 8 (có GRACE trial — RCT CGM trong GDM) |
| Kiến thức nền | 0 | 0 (lỗi: thiếu `-d` → đã sửa trong quy trình trên) |

---

## Các lỗi thường gặp — TRÁNH

### ❌ Dùng keyword tiếng Việt

```bash
# SAI: "sinh non" → PubMed không hiểu tiếng Việt → 0 kết quả
biomcp search article -k "sinh non preterm birth cervical length guideline"

# ĐÚNG: entity-typed bằng tiếng Anh
biomcp search article -d "premature birth" -k "cervical length screening guideline"
```

### ❌ Keyword quá chung chung cho guideline

```bash
# SAI: "guideline recommendation" → trả về thyroid, hypertension, iodine...
biomcp search article -d "diabetes gestational" -k "guideline recommendation"

# ĐÚNG: keyword đặc hiệu — diagnostic criteria, cutoff, procedure
biomcp search article -d "diabetes gestational" -k "oral glucose tolerance test diagnostic criteria screening"
```

### ❌ Dùng default search không `--source`

```bash
# SAI: default search → Semantic Scholar rate limit + PubTator3 lỗi → kết quả thiếu
biomcp search article -d "premature birth" -k "cervical length"

# ĐÚNG: luôn thêm --source pubmed hoặc --source europepmc
biomcp search article --source europepmc -d "premature birth" -k "cervical length" --sort date --limit 10
```

### ❌ Tìm kiến thức nền không có -d

```bash
# SAI: không -d → trả về Heart Disease Statistics, Endocrine Disruptors
biomcp search article -k "gestational diabetes pathophysiology mechanism review"

# ĐÚNG: luôn có -d ngay cả cho kiến thức nền
biomcp search article -d "diabetes gestational" -k "pathophysiology insulin resistance review"
```

### ❌ Chỉ search PubMed, quên web xã hội nghề nghiệp

```bash
# SAI: bỏ qua guideline ISUOG/AIUM/ACOG trên web
# → mất flowchart, bảng, hình ảnh từ guideline gốc

# ĐÚNG: Bước 0 luôn vào web xã hội nghề nghiệp trước
read https://www.isuog.org/clinical-resources/isuog-guidelines.html
```

### ❌ 1 query duy nhất

```bash
# SAI: 1 query, 5 paper → dễ bỏ sót evidence quan trọng
biomcp search article -k "progesterone preterm birth" --limit 10

# ĐÚNG: 6 bước, snowball → 15-25 paper, phân tầng rõ
# (xem quy trình 6 bước ở trên)
```

### ❌ Dùng `biomcp get article` hoặc default search không `--source`

```bash
# SAI: default search → Semantic Scholar rate limit + PubTator3 HTML error → kết quả thiếu
biomcp search article -d "premature birth" -k "cervical length"

# SAI: biomcp get article → PubTator3 lỗi → luôn fail
biomcp get article 30103263 tldr
biomcp get article 30103263

# SAI: citation snowball qua biomcp → Semantic Scholar rate limit
biomcp article references 30103263
biomcp article citations 30103263

# ĐÚNG: --source pubmed hoặc --source europepmc
biomcp search article --source europepmc -d "premature birth" -k "cervical length" --limit 10

# ĐÚNG: fetch article qua fetch_article.py (NCBI E-utilities, không phụ thuộc PubTator3)
python 10_Script Python/fetch_article.py --pmid 30103263 --tldr
python 10_Script Python/fetch_article.py --pmid 30103263 --abstract

# ĐÚNG: citation snowball qua fetch_article.py hoặc Europe PMC skill
python 10_Script Python/fetch_article.py --pmid 30103263 --citations --limit 10 --tldr
uv run C:/Users/THANHANH/.claude/skills/literature-search-europepmc/scripts/europepmc_api.py get_citations MED 30103263 --page_size 10 --output cites.json
```
