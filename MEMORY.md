# MEMORY.md — Lessons learned & technical notes

> **Mục đích**: Các entry memory quan trọng nhất từ Mavis, được clean và tái cấu trúc cho AI agent khác
> (Codex, Claude Code, Cursor...) đọc hiểu mà không cần context Mavis gốc.
> **Cập nhật**: 2026-06-29
> **Lesson learned mới (29/06)**: LLM hallucinate protocol details (timing, sequence, dosing) giống như hallucinate số liệu. Cần verify từ abstract gốc trước khi viết. Mọi protocol detail trong cards PHẢI có PMID.
> **Format**: Mavis-compatible (heading + Type + content) — Claude Code cũng đọc được.

---

### Session 2026-07-03 — Medical QA + fetal neurosonography quick workflow

**Type**: Workflow/user preference + outputs

**User preference mới:**
- Khi user đưa nội dung y khoa và muốn lưu: trả lời/giải thích trong chat trước, sau đó mới lưu file.
- Khi user hỏi theo kiểu `qa:` hoặc câu hỏi y khoa rõ ràng phù hợp QA: trả lời xong phải tự lưu QA ngay, không chờ user nhắc `lưu qa`.
- Với mọi workflow QA: phải tạo todo ngay từ đầu gồm `trả lời trong chat`, `lưu QA`, `cập nhật _INDEX.md`, và `cập nhật english_terms.md nếu có thuật ngữ tiếng Anh`.
- Với `medical_qa`, tên file phải là **tiếng Việt theo tên câu hỏi**, **không kèm ngày**; ngày chỉ ghi bên trong file.
- `medical_qa` workspace chính: `F:\DL\mavisresearch\medical_qa\`.
- Nội dung siêu âm thai/thần kinh thai lưu trong `medical_qa/by_topic/sieu-am-thai/`.
- Chỉ giữ topic folder có câu hỏi thật; không tạo/giữ folder rỗng trong `medical_qa/by_topic/`.
- Khi user gửi đoạn tiếng Anh y khoa, phải trích thuật ngữ tiếng Anh chuyên ngành và cập nhật `medical_qa/english_terms.md`; mỗi thuật ngữ unique, không lặp.
- Khi cần verify PubMed trong QA/bài học: ưu tiên PubMed MCP nếu tool được mount. Trong OpenCode nếu MCP không expose native tool, dùng BioMCP CLI (`biomcp search article --source pubmed ...`, `biomcp get article PMID`) trước khi fallback E-utilities `webfetch`.
- Quy tắc thuật ngữ mới: trong chat/QA/card, thuật ngữ tiếng Anh khó PHẢI có chú thích tiếng Việt ngay lần đầu, ưu tiên `tiếng Việt (English)`. Không viết dày đặc thuật ngữ Anh không giải nghĩa.
- **Quy tắc trình bày bảng (2026-07-05):** Không dùng bảng Markdown `|...|` phức tạp trong QA/bài học. Thay bằng **danh sách có tiêu đề** (heading + bullet list). Mỗi dòng là một mục riêng, dễ đọc trên plain text. Chỉ giữ bảng đơn giản 2-3 cột nếu thực sự cần.

**Đã tạo/cập nhật trong phiên:**
- `medical_qa/by_topic/sieu-am-thai/2026-07-03_transventricular-plane.md` — file cũ có ngày trong tên do tạo trước khi user đổi quy ước.
- `medical_qa/by_topic/sieu-am-thai/mặt-cắt-qua-đồi-thị-trong-siêu-âm-thai.md`.
- `medical_qa/by_topic/sieu-am-thai/mặt-cắt-dọc-và-cạnh-dọc-trong-siêu-âm-não-thai-qua-đường-bụng.md`.
- `medical_qa/by_topic/sieu-am-thai/bất-sản-vòm-sọ-acrania-là-gì.md`.
- `medical_qa/_INDEX.md` đã cập nhật các dòng tương ứng.
- `Bai hoc y khoa/03_Sieu am thai/07_Fetal_Neurosonography/Anki - Các mặt cắt theo đường khớp và thóp.apkg` — 15 cards, verify OK 96.5%.
- `Bai hoc y khoa/03_Sieu am thai/07_Fetal_Neurosonography/các_mặt_cắt_theo_đường_khớp_và_thóp.cards.v2.json`.
- `Bai hoc y khoa/03_Sieu am thai/07_Fetal_Neurosonography/bất-sản-vòm-sọ-acrania.md`.
- `Bai hoc y khoa/03_Sieu am thai/07_Fetal_Neurosonography/bất-sản-vòm-sọ-acrania.cards.v2.json`.
- `Bai hoc y khoa/03_Sieu am thai/07_Fetal_Neurosonography/Anki - Bất sản vòm sọ Acrania.apkg` — 24 cards, verify OK 97.3%.

**Clinical content covered:**
- Fetal neurosonography planes: transventricular, transthalamic, transcerebellar, transabdominal sagittal/parasagittal.
- Transvaginal fetal neurosonography: safety, ALARA, probe settings, acoustic windows via sutures/fontanelles, 3D tips, documentation/reporting.
- Acrania / acrania-exencephaly-anencephaly sequence.

### Session 2026-07-03 — Bai hoc y khoa folder cleanup

**Type**: Workspace organization

**Decision:** Use moderate cleanup, not aggressive renaming. Keep `10_Script Python/` at root to avoid breaking scripts.

**New structure:**
- `_CATALOG.md` added as quick lookup table for lesson folders and deliverables.
- `80_Legacy_by_format/` holds old format-based folders: visual summaries, APKG decks, markdown sources.
- `99_Inbox/` holds loose/not-yet-classified files.
- `_duplicates_review/` holds empty duplicate folders and loose duplicate files; do not delete until manually reviewed.

**Rule:** When cleaning folders, move questionable/tr duplicate data to review areas instead of deleting.

---

---

## 📚 Mục lục

- [Session 2026-06-28 — Tổng kết build + workflow hardening](#session-2026-06-28)
- [User identity — Bác sĩ Ngọc Hưng + AI là tên model](#user-identity)
- [New lesson folder convention](#lesson-folders)
- [PMID hallucination gate — verify_all_pmids.py](#pmid-hallucination-gate)
- [Annotation tags + verify_claims.py](#annotation-tags)
- [PMC full text upgrade cho verify_claims](#pmc-fulltext-verify)
- [pubmed_fetch bug — XML namespace](#pubmed-fetch-namespace)
- [citation_audit Unicode crash](#citation-audit-unicode)
- [New tools created (2026-06-27)](#new-tools)
- [Flashcard V2 format](#flashcard-v2)
- [journal_quartile.json thiếu AJOG](#journal-ajog-missing)
- [guideline_registry.json thiếu SMFM](#guideline-smfm-missing)
- [Template cập nhật — 4 section mới](#template-v2)
- [PPTX Maker Skill](#pptx-maker-skill)
- [Citation audit workflow](#citation-audit-workflow)
- [LLM hallucination — PMID và số liệu cụ thể](#llm-hallucination)
- [Citation strictness rules](#citation-strictness-rules)
- [Vietnamese diacritics governance](#vietnamese-diacritics-governance)
- [Pitfalls đã gặp](#pitfalls)

---

<a id="session-2026-06-28"></a>
### Session 2026-06-28 — Tổng kết

**Bài đã build (28/06):**
| # | Bài | Folder | PMIDs | Cards |
|---|---|---|---|---|
| 20 | Bất thường nước ối | `03_Sieu am thai/03_Bat thuong nuoc oi/` | 7 ✅ | 25 |
| 21 | OHSS Toàn diện | `02_Ho tro sinh san ART/21_OHSS_Comprehensive/` | 7 ✅ | — |
| 22 | ĐTĐ thai kỳ (GDM) | `01_San phu khoa/08_GDM/GDM_Comprehensive/` | 8 ✅ | 38 |
| 23 | Siêu âm hình thái thai nhi | `03_Sieu am thai/04_Fetal_Anatomy_Ultrasound/` | 2 ✅, 2 removed | 9 |
| 24 | Các mặt cắt siêu âm tim thai | `03_Sieu am thai/05_Fetal_Cardiac_Views/` | 4 ✅ | 10 |
| — | Gonadotropin Dosing (verify+rebuild) | `02/.../17_Gonadotropin_Dosing/` | 13 ✅ | — |
| — | ART Trigger (verify+rebuild) | `02/.../18_ART_Trigger/` | 15 ✅ | — |

**3-layer anti-hallucination gate (đã tích hợp build_pipeline.py steps 2, 2b, 2c):**
1. `verify_all_pmids.py` — PMID tồn tại + title đúng (exit 2 = BLOCK)
2. `retraction_check.py` — PMID chưa bị rút
3. `verify_claims.py` — Số liệu claim fuzzy match abstract/PMC full text (PMC first, abstract fallback)

**Convention bắt buộc mới:**
- MỌI reference PHẢI có annotation tag: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[FULL VERIFIED]`, `[GUIDELINE VERIFIED]`, `[DIRECTION ONLY]`
- Số liệu cụ thể (RR, CI, %, n=) → BẮT BUỘC `[FULL VERIFIED]` + số khớp abstract/PMC
- KHÔNG cite PMID từ trí nhớ — mọi PMID phải fetch abstract trước

**Tools mới (ngoài 27/06):**
- `verify_claims.py` — PMC full text → fuzzy match claim numbers
- `slider3636.py` — PPTX engine 25 type, 5 palettes (Colab → CLI)
- `.opencode/skills/ppt-maker/SKILL.md` — skill tạo slide y khoa

**Bug đã phát hiện + fix:**
- PMID 18477582, 2660028 hallucinate trong bài OHSS → verify_all_pmids chặn exit 2
- PMID 36963007 (ISUOG fetal cardiac = antimicrobials), 35043950 (Blaas = infective endocarditis) hallucinate trong bài Fetal Anatomy → removed, replaced with PMID 37267096
- AJOG missing from journal_quartile.json → đã thêm
- SMFM missing from guideline_registry.json → đã thêm

---

<a id="user-identity"></a>
### User identity — Bác sĩ Ngọc Hưng + AI là tên model (2026-06-28 — CỨNG)

**User tên đầy đủ**: **Bác sĩ Ngọc Hưng** (KHÔNG phải chỉ "Ngọc" hay "Ngoc").

**AI assistant**: Xác định theo **tên model đang dùng** (trước đây là MiniMax Mavis, hiện tại là opencode deepseek-v4-pro). KHÔNG gọi AI là "MiniMax Mavis" trong bài mới hoặc footer.

**Đã update (28/06):**
- `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `README.md` — Owner → Ngọc Hưng, AI → tên model
- `Bai hoc y khoa/_README.md` — Bác sĩ → Ngọc Hưng, AI → tên model
- `Bai hoc y khoa/template_lesson.md` + `template_lesson_deep.md` — footer updated
- `Bai hoc y khoa/.mavis/AGENTS.md` — AI identity updated
- `MEMORY.md` — entry này

**Bài cũ** (1-21) vẫn còn footer "MiniMax Mavis" — không sửa để giữ nguyên lịch sử. Bài mới (22+) dùng template mới.

---

<a id="lesson-folders"></a>
### New lesson folder convention (2026-06-28 — HARDENED)

**Từ bài 21 (HyCoSy/HyFoSy) trở đi, MỌI deliverable của 1 bài học PHẢI nằm trong 1 folder duy nhất theo chuyên khoa — KHÔNG để file đứng riêng rẽ trong `03_Sieu am thai/` hay `09_Source - Markdown/`:**

```
Bai hoc y khoa/XX_Chuyen_khoa/XX_Ten_bai/
  ├── Ten_bai_YYYY-MM-DD.md                   # MD source (có dấu)
  ├── Ten_bai_YYYY-MM-DD.cards.v2.json        # Flashcard JSON
  ├── Anki - Ten_bai XX cards - YYYY-MM-DD.apkg  # Anki deck
```

**Quy tắc phân loại chuyên khoa:**
- Nội dung về **fetal ultrasound, nước ối, Doppler, sàng lọc tam cá nguyệt thứ nhất, độ dài cổ tử cung** → `03_Sieu am thai/`
- Nội dung về **tubal patency, infertility workup, IVF/ICSI/FET, OHSS, endometrial receptivity, luteal phase support, stimulation protocols, PGT** → `02_Ho tro sinh san ART/`
- Nội dung về **sản khoa tổng quát (chuyển dạ, đẻ chỉ huy, tiền sản giật, GDM, u xơ tử cung, Asherman, v.v.)** → `01_San phu khoa/`

**Lý do**: Tránh rải file ra 4 folder khác nhau (`03_Sieu am thai/`, `08_Anki Deck/`, `07_Visual/`, `09_Source/`). Folder riêng giúp backup, di chuyển, sync dễ dàng hơn và tránh nhầm lẫn chuyên khoa.

**Lesson learned 28/06/2026 — HyCoSy/HyFoSy**: Bài này về đánh giá độ thông vòi trứng trong infertility workup → **KHÔNG thuộc siêu âm thai** mà thuộc `02_Ho tro sinh san ART/`. Đã chuyển từ `03_Sieu am thai/` + `09_Source - Markdown/` sang `02_Ho tro sinh san ART/19_HyCoSy_HyFoSy_Tubal_Patency/`.

**Trước đây (bài 1-19)**: Mỗi format nằm 1 folder riêng → khó quản lý khi nhiều bài.
**Từ nay (bài 21+)**: Gộp chung 1 folder theo tên bài → dễ backup, di chuyển, sync.

---

<a id="pmid-hallucination-gate"></a>
### PMID hallucination gate — verify_all_pmids.py (2026-06-27)

**Lesson**: Khi viết bài OHSS, LLM hallucinate 2 PMID (18477582, 2660028) từ "kiến thức chung" mà không fetch. 18477582 = "community health agents" (sai hoàn toàn), 2660028 = "cigarette smoking" (lệch 1 chữ số so với PMID đúng 2660037).

**Root cause**: Pattern cũ chỉ yêu cầu fetch cho "số liệu cụ thể (RR, CI, %)". Nhưng LLM cũng hallucinate khi viết reference chỉ có title/author.

**Fix**: Tạo `verify_all_pmids.py` — gate BẮT BUỘC:
- Extract tất cả PMID từ MD
- Fetch từng PMID qua PubMed → verify title KHÔNG chứa suspicious keywords
- Exit 2 = BLOCK nếu PMID sai → **KHÔNG được build**
- Tích hợp vào `build_pipeline.py` (step 2b) + `WORKFLOW.md` (step 3b)

**Quy tắc mới**: **MỌI PMID cite trong bài PHẢI được fetch trước**. Không cite PMID từ trí nhớ.

---

<a id="annotation-tags"></a>
### Annotation tags bắt buộc + verify_claims.py gate (2026-06-27)

**Gate mới**: `verify_claims.py` — chống LLM bịa số liệu cụ thể (RR, CI, %, n=).

**Logic**:
- Extract mọi (PMID, context) từ MD
- Fetch abstract → fuzzy match số liệu claim vs abstract (dung sai 10%)
- Nếu claim có số cụ thể mà abstract KHÔNG có → **BLOCK** (hallucination)
- Nếu claim có số cụ thể mà KHÔNG có tag [FULL VERIFIED] → **BLOCK**

**Annotation tags (BẮT BUỘC cho mọi citation)**:

| Tag | Khi dùng |
|---|---|
| [FETCHED] / [DIRECTION ONLY] | Tối thiểu — abstract đã fetch |
| [ABSTRACT VERIFIED] | Claim qualitative đã xác nhận |
| [FULL VERIFIED] | **Số liệu cụ thể** đã đối chiếu |
| [GUIDELINE VERIFIED] | Guideline chính thức |

**Đã test**: OHSS lesson 7 PMIDs → 0 BLOCK (số thật). Fake claim RR 9.99 → BLOCK (exit 2).

**Tích hợp**: `build_pipeline.py` step 2c, chạy sau retraction_check, trước guideline_compare.

**Rule**: MỌI số liệu cụ thể (RR, CI, %, n=, OR, HR, p value) PHẢI có [FULL VERIFIED] + số đó PHẢI khớp abstract.

---

<a id="annotation-tags"></a>
### Annotation tags bắt buộc + verify_claims.py gate (2026-06-28)

**Gate chống hallucination số liệu**: `verify_claims.py` — fuzzy match claim vs PubMed abstract/PMC full text.

**Annotation tags (BẮT BUỘC mọi citation):**
| Tag | Khi dùng |
|---|---|
| `[FETCHED]` / `[DIRECTION ONLY]` | Tối thiểu — abstract đã fetch |
| `[ABSTRACT VERIFIED]` | Claim qualitative đã xác nhận |
| `[FULL VERIFIED]` | **Số liệu cụ thể** đã đối chiếu abstract/PMC |
| `[GUIDELINE VERIFIED]` | Guideline chính thức |
| `[PMC VERIFIED]` | Verified qua PMC full text |

**PMC upgrade**: verify_claims giờ fetch PMC full text trước (Europe PMC JATS XML), fallback abstract. OHSS lesson: 6/7 articles PMC full text.

**Test**: Fake claim RR 9.99 → BLOCK exit 2. OHSS lesson 7 PMIDs → 0 BLOCK.

---

<a id="pubmed-fetch-namespace"></a>
### pubmed_fetch bug — XML namespace sai (2026-06-27)

**Bug**: `C:\Users\THANHANH\.mavis\mcp\pubmed.py` dòng 320-324 — hàm `_efetch()` dùng namespace `{http://schemas.openxmlformats.org/wordprocessingml/2006/main}` (Word ML) để parse PubMed XML → không tìm thấy element nào → `articles: []` luôn rỗng.

**Root cause**: Copy namespace từ code xử lý DOCX, nhưng PubMed XML không có namespace.

**Fix**: Xoá namespace, dùng tag name thuần (`PubmedArticle`, `PMID`, `ArticleTitle`, `AbstractText`, `Author`, `PublicationType`, etc).

**Impact**: pubmed_fetch bị hỏng từ lâu, WORKFLOW.md có ghi "MCP pubmed_fetch trả empty" nhưng chưa ai debug root cause.

---

<a id="citation-audit-unicode"></a>
### citation_audit Unicode crash (2026-06-27)

**Bug**: `citation_audit.py` crash khi in ký tự Unicode tiếng Việt ra console (PowerShell cp1252).

**Fix**: Thêm `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` vào `main()`.

**Same fix áp dụng cho**: `retraction_check.py`, `guideline_compare.py`, `knowledge_graph.py`, `md_to_html.py`.

---

<a id="new-tools"></a>
### New tools created (2026-06-27)

| Script | Purpose |
|---|---|
| `md_to_html.py` | Legacy auto-convert MD → HTML cho bài cũ |
| `build_pipeline.py` | 1-lệnh build APKG + audit + diacritics |
| `retraction_check.py` | Check tất cả PMID trong bài có bị retract không |
| `guideline_compare.py` | So sánh guideline từ mọi society cho 1 topic |
| `knowledge_graph.py` | Build/query đồ thị liên kết giữa các bài học |

---

<a id="flashcard-v2"></a>
### Flashcard V2 format (2026-06-27)

**Format mới trong lesson_builder.py**: `add_cards_from_json_v2()`

```json
[
  {
    "type": "basic",
    "front": "Câu hỏi",
    "back": "<b>📖 Văn bản gốc:</b><br>...<br><br><b>🔍 Góc nhìn bổ sung:</b><br>...",
    "extra": ""
  },
  {
    "type": "cloze",
    "text": "Nội dung có {{c1::phần bị ẩn}}.",
    "extra": "Ghi chú bổ sung"
  }
]
```

**Rules**: type bắt buộc (`basic`/`cloze`), cloze chỉ dùng `{{c1::...}}` (không c2/c3), back có 2 phần 📖 🔍.

---

<a id="journal-ajog-missing"></a>
### journal_quartile.json thiếu AJOG (2026-06-27)

**Bug**: "American Journal of Obstetrics and Gynecology" (AJOG, IF 7.0, top OB/GYN journal) không có trong Q1 registry → citation_audit báo "Unknown journal".

**Fix**: Đã thêm vào Q1.

---

<a id="guideline-smfm-missing"></a>
### guideline_registry.json thiếu SMFM (2026-06-27)

**Bug**: Registry chưa có SMFM section → preflight_guideline_check không nhận diện SMFM guideline.

**Fix**: Đã thêm SMFM với Consult Series #46 (polyhydramnios), #52 (FGR), #72 (TTTS/TAPS).

---

<a id="template-v2"></a>
### Template cập nhật (2026-06-27)

**4 section mới bắt buộc trong mọi bài:**
- `## 5. LƯU ĐỒ QUYẾT ĐỊNH LÂM SÀNG` (Mermaid flowchart)
- `## 6. SAI LẦM THƯỜNG GẶP` (bảng: sai lầm → hậu quả → cách tránh)
- `## 7. BẢNG THUỐC VÀ LIỀU DÙNG` (hoặc "Không áp dụng")
- `## 8. ÁP DỤNG TẠI VIỆT NAM` (dịch tễ, sẵn có, BHYT, VAGO)

---

<a id="citation-audit-workflow"></a>
### Citation audit workflow cho bài học y khoa (2026-06-19)
Type: technical

- Project daily medical lesson tại `F:\DL\mavisresearch\Bai hoc y khoa\` cần citation audit vì LLM hay hallucinate PMID + số liệu cụ thể (RR, CI, %, n=).
- 3 file chính trong `10_Script Python/`:
  - `journal_quartile.json` — ~50 journal sản phụ khoa mapping Q1-Q4 + aliases PubMed (đã lên ~120 journals).
  - `guideline_registry.json` — ~30 guideline ASRM/ACOG/RCOG/ESHRE/ISUOG/NICE/FIGO/WHO + supersede tracking.
  - `citation_audit.py` — main script: extract PMID + guideline, verify qua PubMed E-utilities, assign Tier 0-4, output report.
- **Tier system**: Tier 0 (Guideline) > Tier 1 (Q1) > Tier 2 (Q2) > Tier 3 (Q3) > Tier 4 (Q4_AVOID) > Tier 5 (NOT_FOUND).
- **Strictness hybrid**: specific claim (RR/CI/%/n=) + Tier 4 → BLOCK; specific claim + Tier 1/2 → WARN; direction only + Tier 1/2 → OK.
- Wrapper `make_lesson_cited.py` gọi audit script, exit 0/1 cho CI.
- Cite format guideline: `[SOCIETY YYYY - Doc ID]` vd `[ACOG PB #175]`, `[ISUOG 2023 - Fetal Biometry]`.
- PMID fetch rate limit: 0.35s giữa các call (E-utilities).
- **BẮT BUỘC verify abstract TRƯỚC khi cite số liệu cụ thể**. Chỉ PMID tồn tại + title khớp KHÔNG đủ.

---

<a id="llm-hallucination"></a>
### LLM hallucination — PMID và số liệu cụ thể (2026-06-19)
Type: lesson-learned

- **Bài học 17/06 Cervical Length**: 7/19 PMID (37%) **SAI TOPIC** — paper về lao (PMID 21514889), cổ chân (25658069), vai (26921128), mạch máu (22504511), ung thư COVID tiếng Nga (33301247), COPD (35787523), khảo sát (36915023). 1 PMID (19888076) không tồn tại trong PubMed.
- **Bài học 18/06 Long GnRH Agonist** (Mavis tự viết): 10/10 PMID tồn tại và title khớp, NHƯNG đã **bịa số liệu cụ thể**: "RR 0.96, 95% CI 0.90-1.03, p=0.27", "RR 0.48, 95% CI 0.38-0.61" cho Liu 2023 (PMID 38095077) — KHÔNG có trong abstract. Tương tự Kadoura 2022 (PMID 35292717), Hu 2024 (37884809).
- **Pattern**: LLM dễ dàng bịa các con số cụ thể (RR, CI, %, sample size) khi viết về meta-analysis/clinical trial. Cần fetch full text hoặc abstract rõ ràng có số đó trước khi cite.
- **Quy tắc mới**: Claim có số liệu cụ thể → **BẮT BUỘC** mark `[FULL VERIFIED]` và fetch full text. Claim direction/qualitative → `[ABSTRACT VERIFIED]` là đủ.

---

<a id="citation-strictness-rules"></a>
### Citation strictness rules cho medical writing (2026-06-19)
Type: heuristic

- Cite PMID chỉ với title/abstract verified → có thể hợp lý nhưng KHÔNG cite số liệu cụ thể.
- **Tier 4** (Q4 / predatory journal) + specific claim → **BLOCK** (không publish).
- **Tier 4** + direction only → WARN (chỉ dùng khi không có source tốt hơn).
- **Unknown journal** (không có trong table) + specific claim → WARN mạnh "VERIFY TOPIC RELEVANCE".
- Default cho journal unknown: **Tier 3** (cân nhắc) để tránh false positive.
- **Guideline superseded** → WARN với gợi ý dùng bản mới hơn.
- **Guideline không trong registry** → UNKNOWN_GUIDELINE, verify thủ công hoặc thêm vào registry.

---

<a id="citation-audit-scan"></a>
### Citation audit scan toàn project (2026-06-19)
Type: technical

- Script `scan_all_lessons.py` scan tất cả .docx + .md trong `F:\DL\mavisresearch\Bai hoc y khoa\` (skip source/script dirs), output audit report vào `10_Script Python/audit_reports/audit_all_lessons_<date>.{md,json}` + `unknown_journals_<date>.txt`.
- Lần scan đầu: 21 files, 294 citations, **2 BLOCK (cả 2 NOT_FOUND PMID)**, **96 unique unknown journals**. Sau khi add 115 journals (Q1-Q4) + 64 aliases: **0 unknown**, 5 BLOCK (tất cả đều legitimate - sai topic hoặc NOT_FOUND).
- **5 BLOCK legit** đã biết:
  - PMID 16195969 (Zentralbl Gynakol) - ENZIAN-score trong bài Endometriosis (sai topic nhẹ, OK).
  - PMID 19888080 NOT_FOUND trong bài IVF 12/06 (typo của 19888076 hoặc khác).
  - PMID 23350334 (An R Acad Nac Med Madrid) - Spanish cardiology lecture, sai topic.
  - PMID 33301247 (Khirurgiia Moscow) - Russian COVID cancer, sai topic.
  - PMID 19888076 NOT_FOUND trong bài Cervical Length 17/06.
- Cron `daily-lesson-2100` đã update với workflow mới: bắt buộc fetch abstract, không hallucinate số liệu, chạy citation_audit sau build, fail nếu BLOCK.
- `journal_quartile.json` v3 có 100+ journal: OB/GYN core + ART + ultrasound + cardiology (fetal echo) + pediatrics + endocrinology + molecular bio. **Q4_AVOID** bao gồm 8+ journal sai topic đã thấy trong audit (Khirurgiia, An R Acad Nac Med, J Sport Rehabil, Vasc Endovascular Surg, Tuberculosis, J Surg Res, Arthroscopy, J Phys Chem A).

---

<a id="vietnamese-diacritics-governance"></a>
### Vietnamese diacritics governance cho bài học y khoa (2026-06-22)
Type: workflow

- **Quy ước split**: filename/folder KHÔNG dấu (Windows safe) nhưng **content trong .md/.apkg PHẢI CÓ DẤU ĐẦY ĐỦ**.
- **Giữ nguyên tiếng Anh**: thuật ngữ y khoa (Doppler, ICSI, T21), guideline abbreviations (FIGO, ASPRE, NEJM, ACOG), tên thuốc (aspirin, hCG), tên riêng.
- **Bug ngầm đã sửa (22/06)**: `make_*_lesson.py` cũ hardcode content không dấu trong Python source → user report "vẫn không có dấu" dù MD đã convert. Root cause: script build không đọc từ MD.
  - **Legacy fix**: `md_to_docx.py` parser MD → DOCX đọc UTF-8 trực tiếp từ file MD; áp dụng khi rebuild/xuất lại bài cũ.
- **Tooling enforce (4 lớp)**:
  1. `WORKFLOW.md` ở root + `10_Script Python\WORKFLOW.md` — checklist workflow.
  2. `template_lesson.md` — template có dấu sẵn, copy khi viết bài mới.
  3. `verify_diacritics.py` — scan % dấu trong MD, threshold ≥ 80% = OK. Logic: classify word thành vn_diac / vn_no_diac / other, ratio = vn_diac / (vn_diac + vn_no_diac). Bỏ qua English/numbers khi tính.
  4. Build APKG từ MD; không build DOCX/HTML cho bài mới.
- **add_diacritics.py** (~500 entries): manual mapping cho từ y khoa phổ biến. Ambiguous (KHÔNG auto-convert): gan, nam, mo, co, benh, huyet, etc.
- **verify_diacritics.py kết quả 22/06**: 16/16 MD files đạt 90-96% ratio (PASS). Threshold lúc đầu 80% đặt trên tổng từ → 16/16 FAIL vì thuật ngữ Anh (PMID, T21, FIGO) làm tăng tổng. Fix: chỉ tính ratio trên từ tiếng Việt.
- **PowerShell hiển thị UTF-8 sai** (`?` thay vì dấu): phải verify bằng `python -c "print(open(f).read())"` để xem content thật.
- **Citation audit**: 0 BLOCK yêu cầu, tier system Tier 0 (guideline) > 1 (Q1) > 2 (Q2) > 3 (Q3) > 4 (Q4_AVOID) > 5 (NOT_FOUND).
- **Daily cron `daily-lesson-2100`**: build bài mới 21h Vietnam time, deliverable gồm APKG và Telegram text; MD là bài nguồn.

---

<a id="daily-lesson-workflow-notes"></a>
### LPS lesson - workflow note (2026-06-22)
Type: workflow

- Bài LPS (Luteal Phase Support trong ART) build xong 22/06 21h00. 9 citations verified qua E-utilities webfetch, 0 BLOCK, 8 WARN (Q1/Q2 + specific claim - all FULL VERIFIED).
- Journal additions vào journal_quartile.json: Nature Reviews Endocrinology (Q1, IF 31), Current Opinion in Obstetrics and Gynecology (Q2, IF 2.5). Cả 2 cần add alias vì citation_audit map bằng alias.
- Kastora 2024 (Sci Rep) tier Q2 (IF 4.6 - đã có), nhưng đã verify abstract trực tiếp - các số liệu OR/CrI đều chính xác.
- Pattern thành công: search PubMed cho topic → verify abstract bằng webfetch E-utilities (vì MCP pubmed_fetch trả empty) → ghi [FULL VERIFIED] cho số liệu cụ thể.

---

### Oxytocin IOL lesson - team plan pattern + journal registry growth (2026-06-23)
Type: workflow

- Bài Oxytocin Induction of Labor — pattern thành công với team plan: researcher phân tích guideline, mechanism-reviewer viết pathway, synthesis-writer ghép bài.
- Journal registry thêm ~15 journal mới liên quan obstetric (Obstet Gynecol, Am J Obstet Gynecol, BJOG, Pregnancy Hypertens...).
- Lưu ý: khi team plan build daily lesson, cần set timeout ceiling ≥ 30 phút (không phải default 15).

---

### Daily lesson depth check - template + gate mới (2026-06-23)
Type: workflow

- Thêm `depth_check.py` script — gate mới: bài học phải đạt ≥ 8000 từ MD (depth tối thiểu).
- Nếu < 8000 từ → synthesis-writer phải expand thêm (case studies, pathway chi tiết, comparison table).
- Template mới có sẵn 10 sections (overview, definition, mechanism, evidence, application, tips, summary, references, FAQ, decision tree).

---

<a id="pubmed-sort"></a>
### PubMed sort=relevance miss 50% paper mới (2026-06-25)
Type: technical

- PubMed default sort `relevance` chỉ rank theo BM25 + recency weight → miss ~50% guideline mới hoặc paper 2024-2026.
- **Best practice**: luôn dùng `sort=date` cho guideline search. Citation count KHÔNG tương quan với chất lượng cho guideline.
- Filter khuyến cáo cho guideline search:
  - `sort=date` (KHÔNG relevance)
  - `reldate=1825` (5 năm gần nhất)
  - `datetype=pdat` (publication date, không pubmed date)
  - `article_type=guideline OR practice guideline OR review`
- Filter cho primary research:
  - `article_type=clinical trial OR randomized controlled trial OR meta-analysis`

---

<a id="eshre-2025"></a>
### ESHRE 2025 update key facts (2026-06-25)
Type: technical

- **PMID 41732035** (Hum Reprod 2026 Feb 24;41(4):498-514, PMCID PMC13061131) — official ESHRE guideline. 121 recs, 21 key questions, 42 strong, 29 updated, 46 new, 2 research-only.
- **ESHRE 2025 BỎ HẲN concept "mild stimulation"** khỏi guideline (Discussion section). Lý do: ICMART definition "intention to limit oocyte" → studies "mild" quá heterogeneous, tổng gonadotropin dose thực tế = conventional. Modified natural cycle (MNC) vẫn GPP cho very low reserve, nhưng đó là natural cycle, không phải "mild với FSH liều thấp + clomiphene/letrozole".
- **ESHRE 2025 KHÔNG có rec riêng cho endometriosis** — chỉ rec chung "antagonist > GnRH agonist cho general IVF" (Strong). Practice "ultra-long GnRH 3-6 tháng" cho endometriosis dựa trên meta-analysis cũ (Sallam 2006, Tian 2023 PMID 36690299) + ASRM cũ + expert opinion, KHÔNG phải Tier 0.
- ESHRE 2025 update tier dose: 100-<150 (high, Conditional ⊕◯◯◯), 150-225 (conventional, Conditional), 225-300 (low, cá nhân hoá), **>300 IU low responder = Strong NOT recommended** (⊕◯◯◯).
- Letrozole + gonadotropin: probably not recommended cho high (updated), normal (2019), low (2019) — tất cả Conditional. Ngoại lệ GPP: ER+ cancer FP.
- DuoStim: nâng từ GPP lên **Strong** (⊕⊕◯◯) cho oocyte accumulation. Random start: Strong cho gonadotoxic FP.
- **POOR → LOW response** thay đổi thuật ngữ, không đổi classification.
- **Disclaimer**: khi viết bài ART stimulation, PHẢI note 2 điểm này (mild bỏ + endometriosis không rec riêng) vì dễ bị hallucinate từ guideline cũ.
- File verify: `F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\14_Stimulation_Protocols\Stimulation_Protocols_ART_2026-06-25.md` (MD) + `.docx` đã errata.

---

<a id="guideline-freshness"></a>
### Guideline freshness check workflow gap (2026-06-25)
Type: workflow

- Bài Stimulation Protocols ART (25/06) suýt dùng ESHRE 2019 vì không check guideline mới → fail cuối cùng do Mavis fetch lại abstract qua webfetch và thấy ESHRE 2025 PMID 41732035.
- **Fix**: thêm `preflight_guideline_check.py` — script check `guideline_versions.json` trước khi viết:
  - Exit 0 = OK dùng version này.
  - Exit 1 = WARN, proceed cautiously.
  - Exit 2 = **BLOCK**, PHẢI dùng version mới hơn.
- File `guideline_versions.json` lưu `{society, doc_id, current_year, current_pmid, last_checked, supersedes, superseded_by}`.
- Update `last_checked` mỗi khi verify.

---

<a id="mcp-pubmed-windows"></a>
### MCP pubmed — cách dùng đúng trên Windows PowerShell (2026-06-27)
Type: technical

- File: `C:\Users\THANHANH\.mavis\mcp\pubmed.py` (đã cài).
- **Bug**: `pubmed_fetch` (single PMID) trả empty thường xuyên — KHÔNG dùng.
- **Workaround**: dùng `webfetch` E-utilities directly:
  ```bash
  # Search
  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=QUERY&retmax=20&sort=date&reldate=1825&datetype=pdat&retmode=json&api_key=e71bce83...63408

  # Fetch abstract
  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID&retmode=xml&api_key=e71bce83...63408

  # PMC full text (best for open-access)
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMCXXXXXXX/fullTextXML
  ```
- PowerShell single-quote JSON lỗi: dùng `--file` flag hoặc Python wrapper.
- Cache key đã normalize (diacritics-strip + lowercase) → hit rate tốt hơn.

---

<a id="chartjs-bug"></a>
### Chart.js canvas stretching bug + visual_sanity_check.py gate (2026-06-25)
Type: legacy technical note

- Chart.js v4 trong HTML visual summary từng có bug: nếu parent container flex-grow, canvas sẽ stretch theo height → text bị méo.
- `visual_sanity_check.py` chỉ dùng khi rebuild HTML bài cũ.
- Gate fail → exit 1, block build.

---

<a id="session-stall"></a>
### Session stall detector cron deployed (2026-06-24)
Type: workflow

- Symptom: Mavis session đôi khi "stall" (không respond, daemon không báo lỗi) — user phải kill thủ công.
- **Fix**: deploy cron `session-stall-detector` mỗi 15 phút check `mavis session list` → nếu session running > 2h không có heartbeat → kill + notify user.
- Throttle: chỉ kill session có flag `--async` được set explicitly (không kill interactive session).
- False positive (16:48 ngày 24/06): stall detector kill session active vì thinking time quá lâu. Fix: tăng threshold 2h → 4h cho interactive session.

---

<a id="team-plan-timeout"></a>
### Team plan timeout ceiling quá ngắn cho daily-lesson build (2026-06-25)
Type: workflow

- `mavis team plan` mặc định timeout 15 phút/cycle → quá ngắn cho daily lesson (researcher + mechanism + synthesis + build).
- **Fix**: set `--timeout 1800` (30 phút) cho `daily-lesson` plan template.
- Daily lesson build breakdown:
  - Researcher: ~5-8 phút (search + fetch abstracts).
  - Mechanism reviewer: ~3-5 phút (pathway synthesis).
  - Synthesis writer: ~10-15 phút (ghép bài 8000+ từ).
  - Builder: ~2-3 phút (APKG).
- Total: ~25-30 phút. Set 30 phút cho buffer.

---

<a id="pptx-maker-skill"></a>
### PPTX Maker Skill (2026-06-27)

**Skill**: `.opencode/skills/ppt-maker/SKILL.md` — tạo slide y khoa từ MD lessons.
**Engine**: `Bai hoc y khoa/10_Script Python/slider3636.py` — render JSON → PPTX, 25 type × 53 variant, 5 palettes.
**Prompt ref**: `10_Script Python/slidemaker_prompt.txt` — đặc tả đầy đủ 25 type.

**Usage**: "tạo slide về [topic]" → AI đọc context repo + slidemaker_prompt.txt → tạo JSON deck trong folder bài → validate → render PPTX → QA.
**Palette default**: Medical Teal.
**Font default**: Segoe UI (tiếng Việt tối ưu).
**CLI**: `python slider3636.py --deck deck.json -o output.pptx --palette "Medical Teal"`
**Output convention**: PPTX là optional deliverable, chỉ tạo khi user yêu cầu; lưu cùng lesson folder dưới `Bai hoc y khoa/`, không ghi root/C:.

---

<a id="pitfalls"></a>
### Pitfalls đã gặp (ngoài các mục trên)

- **PowerShell single-quote JSON escape**: dùng `--file` flag hoặc python wrapper.
- **`add_diacritics` ~80-90% accuracy**: một số từ ambiguous (gan=gan/gần, nam=nam/năm) giữ nguyên không dấu — không fix tự động.
- **MCP `pubmed_fetch` trả empty**: dùng webfetch E-utilities.
- **PowerShell console UTF-8 sai** (`?` thay dấu): verify bằng `python -c`.
- **BÀI HỌC CŨ (12-14/06) có DOCX không dấu**: đã fix 22/06 bằng `md_to_docx.py` + `rebuild_all_docx_v2.py`. Hiện 16/16 DOCX đều có dấu.
- **Session stream-stall + daemon crash** (24/06): thỉnh thoảng session không respond. Workaround: kill + retry, hoặc chạy qua team plan có heartbeat.
- **make_*_lesson.py cũ hardcode content**: deprecated 22/06. Build APKG từ MD cho bài mới; `md_to_docx.py` và HTML chỉ dùng cho bài cũ.
- **Guideline ESHRE 2019 vs 2025**: luôn check version mới nhất trong `guideline_versions.json` trước khi viết.
- **Citation số liệu cụ thể không verify**: 18/06/2026 lesson có 10/10 PMID tồn tại nhưng số liệu bịa. BẮT BUỘC `[FULL VERIFIED]` cho mọi RR/CI/%/n=.
- **PowerShell `&&` chain**: KHÔNG dùng, dùng `;` hoặc `if ($?) { ... }`.
- **Hardcode content trong build script**: gây mất dấu, fix bằng parser MD → output.

---

## Quick reference — keywords cho memory search

| Keyword | Chủ đề |
|---|---|
| `lesson folder` / `output convention` | 1 folder cho tất cả deliverables |
| `pubmed_fetch` / `namespace` | Bug XML namespace → empty articles |
| `citation audit` / `cp1252` | Unicode crash fix |
| `md_to_html` / `build_pipeline` | Legacy HTML builder / pipeline |
| `flashcard v2` / `cloze` | Format thẻ basic + cloze |
| `annotation` / `verify_claims` | Gate chống bịa số liệu |
| `AJOG` / `journal missing` | Registry thiếu journal |
| `SMFM` / `guideline missing` | Registry thiếu guideline |
| `template v2` | 4 section mới bắt buộc |
| `citation audit` | Citation rules, tier system |
| `hallucination` | LLM bịa PMID/số liệu |
| `diacritics` / `dấu` | Vietnamese encoding |
| `ESHRE 2025` | Stimulation protocols update |
| `GDM` / `gestational diabetes` | Bài 22 — ĐTĐ thai kỳ 38 cards |
| `OHSS` | Bài 21 — Cơ chế, phòng ngừa, xử trí |
| `amniotic fluid` | Bài 20 — Thiểu ối & Đa ối |
| `verify_all_pmids` | Gate PMID tồn tại |
| `verify_claims` / `annotation tag` | Gate claim-abstract match + PMC full text |
| `pptx maker` / `slider3636` | Skill tạo slide 25 type |
| `preflight` / `freshness` | Guideline version check |
| `chartjs` / `visual_sanity` | Legacy HTML visual bug |
| `md_to_docx` | MD parser cho DOCX |
| `pptx maker` / `slider3636` | Skill tạo slide y khoa 25 type |
