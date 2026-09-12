# WORKFLOW - Daily Medical Lessons

> **Quy trình chuẩn cho mỗi bài học y khoa mới**
> Cập nhật: 2026-07-29 — provider-neutral NCBI-free evidence sync, offline build bắt buộc bundle và chặn egress.

## 📋 CHECKLIST TRƯỚC MỖI BÀI MỚI

In checklist này ra hoặc copy vào session, check từng mục:

```
[ ] 1. Topic mới (chưa trùng bài cũ)
 [ ] **1a. KHÓA LESSON PROFILE + ACCEPTANCE MATRIX + DEPTH CONTRACT** — chế độ duy nhất `L3_BEGINNER` (`L3 — Cầm tay chỉ việc cho người mất gốc`). Chọn `disease`, `foundation` hoặc `pharmacology` do `publish_gate.py --list-profiles` công bố; copy contract và `lesson_depth_contract` mới nhất từ `RESEARCH_BRIEF_TEMPLATE.md` trước research. Profile chỉ phân loại cấu trúc chuyên môn, tất cả đều bắt buộc dùng chế độ `L3_BEGINNER`.
       - Profile, required gates, `lesson_depth_contract` và output basename không được đổi sau khi research bắt đầu.
       - Gate fail vẫn được giữ candidate để sửa, nhưng không được promote hoặc cập nhật `_CATALOG.md`.
[ ] **2a. PREFLIGHT GUIDELINE CHECK** — `python 10_Script Python/preflight_guideline_check.py --topic "X" --guideline "Society YYYY"`
       - Exit 0 = OK, Exit 1 = WARN, Exit 2 = BLOCK (phải dùng version mới hơn)
[ ] **2b. TIER 0 SEARCH — Web trực tiếp xã hội nghề nghiệp** (ISUOG, ACOG, RCOG, ASRM, AIUM, SMFM, FIGO, NICE)
       - Dùng `read` vào trang guideline của xã hội liên quan → tìm guideline gốc
       - Guideline official source phải lưu local hash, version, document type, authority; bản dịch ghi `translation_of` + `endorsement_status`.
[ ] 3. **ONLINE EVIDENCE SYNC** — tìm nguồn theo `SEARCH_STRATEGY.md`, rồi chạy `evidence_sync.py`.
        - Europe PMC metadata/abstract query không lọc Open Access; OA full text là adapter riêng và chỉ dùng với license phù hợp.
        - Crossref/Retraction Watch kiểm integrity; OpenAlex corroborate identity/topic; official manifest xử lý guideline không PMID.
        - Raw cache immutable + normalized cache + bundle lưu SHA-256/provenance/freshness/license. HTTP 429/5xx/malformed/outage fail-closed, không retry/fallback NCBI.
        - Zero OA/full text không đồng nghĩa bài không tồn tại; existence chỉ từ exact unfiltered metadata record.
 [ ] **3b. RESEARCH BRIEF BẮT BUỘC** — tạo từ `RESEARCH_BRIEF_TEMPLATE.md` trước khi viết bài.
       - Khóa `profile`, danh sách `required_gates`, output basename và bộ nguồn; không đổi contract sau research.
       - Mỗi occurrence của claim có một `Claim ID`; nhiều claim dùng cùng PMID vẫn là nhiều đối tượng phải kiểm riêng.
       - Claim định lượng ghi đủ: quần thể (population), can thiệp/đối chứng (intervention/comparator), kết cục (outcome), thời điểm (timepoint), quote nguyên văn và PMID.
       - Model execute chỉ được dùng claim trong brief; không thêm claim hoặc con số ngoài brief.
[ ] **3c. STRICT BRIEF PREFLIGHT OFFLINE** — `python "10_Script Python/preflight_claim_check.py" <RESEARCH_BRIEF.md> --evidence-bundle <bundle.json> [--topic "..."]`.
       - Bảy gate: existence, exact identity, topic relevance, claim–abstract, numeric/full-text, guideline authority/document type, fresh retraction/correction.
       - `verify_claim_vs_abstract.py` kiểm từng claim occurrence; zero claim là BLOCK. `verify_pmid_topic.py` chỉ đọc bundle offline, không có network ẩn.
       - Metadata/abstract tối đa 72 giờ; retraction/correction tối đa 24 giờ; hash/schema/provenance/license sai hoặc stale đều BLOCK.
[ ] **3d. NĂM NHÃN VERIFICATION DUY NHẤT:**
       - `[FETCHED]`: chỉ xác nhận metadata nguồn; không cho phép claim định lượng.
       - `[ABSTRACT VERIFIED]`: claim định tính khớp abstract.
       - `[DATA VERIFIED]`: số liệu được đối chiếu chính xác với abstract/full text và có quote/artifact.
       - `[FULL TEXT VERIFIED]`: claim được đối chiếu từ toàn văn; artifact ghi bản toàn văn đã dùng.
       - `[GUIDELINE VERIFIED]`: khuyến cáo khớp guideline chính thức qua pipeline guideline riêng.
       - Cấm nhãn cũ `[ABSTRACT MATCH]`, `[FULL VERIFIED]`, `[DIRECTION ONLY]`, `[TEXTBOOK]` và `[Thông tin cơ bản - LLM verified]`. Kiến thức consensus/nền tảng viết tự do KHÔNG gán nhãn verification và không tạo áp lực bịa PMID/quote; chỉ claim có số liệu định lượng, ngưỡng, protocol, liều, guideline mới cần Claim ID + PMID + exact quote.
       - **CẤM TỰ CHẾ QUOTE:** Quote từ nguồn phải là exact substring từ local file/abstract. Guideline quote phải có exact substring + locator (mục/trang/đoạn).
       - **CẤM SỬA VERIFIER SCRIPT LÁCH GATE:** Cấm sửa verifier scripts (`publish_gate.py`, `profile_check.py`, `depth_check.py`, `verify_claims.py`...) trong cùng release workstream. Sửa verifier phải làm workstream/commit độc lập có regression test và rerun từ đầu.
       - **QUY TẮC DỪNG:** Chỉ dừng khi acceptance matrix và `lesson_depth_contract` đạt 100%, CẤM dừng vì "bài đã dài", CẤM lặp ý hay paraphrase padding.
 [ ] **3e. GUIDELINE EVIDENCE RIÊNG & CROSSCHECK** — lưu `guideline_evidence.json` và bản guideline local trong `outputs/sources/`.
        - Mỗi guideline object chứa đúng 14 trường: `claim_id`, `society`, `title`, `document_id`, `version`, `publication_date`, `accessed_at`, `canonical_url`, `local_copy`, `sha256`, `recommendation_text` (đoạn trích nguyên văn liên tục - exact continuous substring, không dùng ellipsis/dấu ba chấm), `locator` (mục/trang/đoạn/dòng), `pmid` (nullable), và `superseded_by`.
        - Chạy `verify_guidelines.py`; gate `guideline_evidence` và `guideline_evidence_crosscheck` sẽ kiểm tra freshness, hash, supersession và đối chiếu exact quote + locator với bản local. Bất kỳ sai khác nào đều BLOCK.
        - Educational resource không phải guideline. Translation không được tổ chức gốc endorse và guideline superseded/current-version false đều BLOCK.
- **DẠY TỪ GỐC & CHUỖI REASONING LOGIC 7 TẦNG (KHOAN SÂU NHÂN QUẢ):** Bắt buộc giảng cơ chế tập trung, không chỉ liệt kê triệu chứng đơn thuần. Mọi bài học phải giải thích chuỗi liên hoàn: **Cơ chế phân tử / Receptor / Thần kinh thể dịch → Thay đổi chuyển hóa & Tế bào → Tổn thương mô & Cơ quan → Biểu hiện lâm sàng (Cơ năng & Thực thể) → Biến đổi cận lâm sàng & Xét nghiệm → Tiêu chuẩn chẩn đoán → Lựa chọn & Cơ chế điều trị**.
- **HƯỚNG DẪN THỰC HÀNH LÂM SÀNG CẦM TAY CHỈ VIỆC:** AI phải hướng dẫn người học chi tiết các bước thực hiện trên thực tế lâm sàng: **Mục tiêu → Khi nào làm/không làm → Cần chuẩn bị gì → Khám hoặc đọc kết quả như thế nào → Kết quả thay đổi quyết định điều trị ra sao → Bẫy lâm sàng/An toàn → Xử trí cấp cứu & Tiêu chí chuyển tuyến**.
- **KỸ THUẬT ÉP ĐỘ DÀI & ĐỘ CHI TIẾT KHI BUILD BẰNG LLM/GEMINI:**
  - Không giới hạn độ dài. Nếu bài dài chạm trần token output, áp dụng quy trình Pass-by-Pass (Turn 1: Sec 0 -> Sec 4; Turn 2: Sec 5 -> Hết).
  - Đặt ngưỡng định lượng cụ thể trong prompt: tối thiểu 2 phác đồ đơn thuốc hoàn chỉnh, 10 Clinical Pearls, 5 bẫy lâm sàng 4 cột.
- **QUY TẮC NHÚNG VÀ HIỂN THỊ HÌNH ẢNH / BIỂU ĐỒ (IMAGE & DIAGRAM GOVERNANCE):**
  - **Sơ đồ tư duy / Flowchart**: Ưu tiên 100% dùng mã Mermaid (` ```mermaid `) để tự động hóa render HD khi xuất bản DOCX/HTML. Nếu chỉ dùng Markdown viewer online thì dùng ASCII Art.
  - **Ảnh y văn thực tế (Guideline/ECG/Siêu âm)**: Yêu cầu LLM tìm kiếm URL ảnh trực tiếp (.png/.jpg) từ nguồn chính thống uy tín (MedSci, Wikimedia, PubMed Central) và nhúng đúng cú pháp `![Mô tả ảnh](URL_truc_tiep)`.
  - **Script tự động nhúng ảnh vào DOCX**: `md_to_docx.py` sẽ tự động download ảnh từ URL hoặc render mã Mermaid thành ảnh HD nhúng thẳng vào Word.
- **TRÌNH BÀY CHUẨN MARKDOWN:**
  - **CẤM KÝ HIỆU PHẦN TRĂM (%) TRONG INLINE MATH ($...$):** Tuyệt đối không đưa dấu `%` hay các bất đẳng thức chứa `%` vào trong cặp dấu `$ ... $` (như `$50% \le FEV1 < 80\%$`) vì KaTeX/MathJax sẽ coi `%` là ký tự comment. Viết Plain Text cho phần trăm (`50% ≤ FEV1 < 80%`).
  - **BẢNG GỌN GÀNG:** Tránh bảng quá rộng (≥4 cột có chữ dài); ưu tiên danh sách có tiêu đề khi thông tin phức tạp.
  - **QUẢN LÝ OUTPUTS:** Tất cả sản phẩm xuất bản (`.docx`, `.apkg`, `.cards.v2.json`, `brief.md`) PHẢI nằm gọn trong subfolder `outputs/` của từng bài học.
- Mọi protocol detail, liều, timing, ngưỡng, RR/CI/%/n= phải có Claim ID và nguồn đã verify tương ứng.
[ ] **5. CHẠY RELEASE RUNNER CANONICAL** — một lệnh duy nhất:
       - `python "10_Script Python/build_pipeline.py" --brief <brief.md> --lesson <release.md> --cards <release.cards.v2.json> --guidelines <guideline_evidence.json> --evidence-bundle <bundle.json>`
       - Runner và mọi Python subprocess bị chặn network egress; verifier chỉ đọc bundle đã kiểm schema/hash/freshness.
       - Citation gate giữ mọi occurrence (không deduplicate) và yêu cầu **0 BLOCK, 0 WARN**. Required gate WARN/SKIP/thiếu artifact/exit khác 0 đều FAIL.
[ ] **6. EVIDENCE MANIFEST** — runner tự sinh `outputs/verification/<release-id>/gate-results.json`.
       - Không tự viết dòng `PASS`. Mỗi gate lưu command, exit code, release ID, input paths, artifact paths và SHA-256.
       - `publish_gate.py` đọc lại file/hash; sửa lesson/cards/artifact sau verify làm promotion thất bại.
[ ] **7. PACKAGE + DOCX GATES:**
       - Cards V2 không rỗng, field bắt buộc hợp lệ; APKG build với `--verify`.
       - Note count trong APKG phải bằng số card input; package diacritics exit 0.
       - DOCX bắt buộc nằm trong `outputs/`, được tạo từ đúng Markdown release và được hash trong manifest.
[ ] **8. LEARNER SMOKE TRƯỚC PUBLISH:**
       - Generator exit 0; knowledge check, answer key và score JSON đều tồn tại, không rỗng.
       - Có đúng 5 section, `total_questions > 0`, trạng thái ban đầu `not_graded`. Không yêu cầu learner mastery trước publish.
[ ] **9. PUBLISH GATE:** runner gọi `publish_gate.py`; chỉ `PUBLISH READY` exit 0 mới được promote.
[ ] **10. SAU PUBLISH:** cập nhật `_README.md` và `_CATALOG.md`; smoke-test chính xác Markdown, cards, APKG và DOCX release.
[ ] **11. NẾU FAIL:** giữ candidate trong remediation; không gắn `PUBLISH_READY`, không cập nhật catalog.
```

## 🔄 WORKFLOW VISUALIZATION

```text
Tier 0: Web trực tiếp (ISUOG, ACOG, RCOG, ASRM...)
    ↓
Khóa profile + acceptance matrix trong Research Brief
    ↓
Online evidence sync
    ├─ Europe PMC metadata/abstract (unfiltered OA)
    ├─ Europe PMC OA full text (license-gated)
    ├─ Crossref/Retraction Watch + OpenAlex corroboration
    └─ Official sources (authority/type/translation/version)
    ↓ immutable raw + normalized cache + hashed bundle
Research Brief → offline 7 gates → viết MD/cards
    ↓ build_pipeline.py --evidence-bundle (egress blocked)
APKG + DOCX + learner artifacts + hashed gate manifest
publish_gate.py (mọi required gate = PASS)
    ├─ PASS → update README + CATALOG / promote
    └─ FAIL → giữ candidate, remediation; không promote
```

## 🛠️ TOOLS - File nào dùng khi nào

| Task | Tool | Lưu ý |
|---|---|---|
| **Tier 0 — Web trực tiếp** | **`read` vào web xã hội nghề nghiệp** | **BẮT BUỘC trước khi search article — ISUOG, ACOG, RCOG, ASRM, AIUM, SMFM, FIGO, NICE** |
| Online evidence sync | `evidence_sync.py` | Tạo immutable raw/normalized cache và provider-neutral hashed bundle; không gọi NCBI/E-utilities. |
| **Research Brief + contract** | **`RESEARCH_BRIEF_TEMPLATE.md`** | Khóa profile, Claim ID, PICO/outcome/timepoint và nguồn trước research. |
| Brief source gates | `preflight_claim_check.py --evidence-bundle` | Strict 7 gates từng occurrence; topic advisory cũng offline. |
| Guideline evidence | `verify_guidelines.py` + official bundle record | URL/version/access/local hash/supersession/authority/document type/translation endorsement. |
| Release runner | `build_pipeline.py --evidence-bundle` | Offline canonical path; chặn egress, sinh hashed evidence manifest. |
| Promotion decision | `publish_gate.py` | Chỉ tin manifest đủ command/exit/artifact/hash; fail-closed. |
| Build APKG/DOCX | `build_apkg.py`, `md_to_docx.py` | Chỉ được gọi qua release runner cho release mới. |


## 🖥️ PPTX WORKFLOW (CẬP NHẬT 2026-07-13)

PPTX là deliverable tùy chọn, chỉ tạo khi user yêu cầu. Quy trình canonical mới:

```text
source/outline
→ slide plan với page types
→ PptxGenJS generation theo skill `pptx`
→ content/PMID QA
→ structural QA bằng qa_pptx.py
→ Windows render/export nếu có PowerPoint/LibreOffice
→ screenshot/manual review
→ fix-and-reverify ít nhất 1 vòng
```

Quy tắc:

- Dùng canvas 10 × 5.625 inch (`LAYOUT_16x9`) cho deck mới.
- Mọi non-cover slide có page badge.
- Deck y khoa nên có speaker notes theo kiểu: **Làm gì? → Tại sao làm vậy? → Nếu bỏ qua/làm sai thì nguy cơ gì?**
- Citation nên là claim-specific trong notes/caption, không lặp cùng một footer PMID dài trên mọi slide.
- Ảnh/siêu âm/hình từ paper cần nguồn, quyền/license hoặc ghi chú provenance, và caption/alt ngắn.
- Chạy `C:\Users\THANHANH\.claude\skills\pptx\scripts\qa_pptx.py` trước khi bàn giao.
- `F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\slider3636.py` là workflow legacy 13.33 × 7.5; chỉ dùng khi cần rebuild deck cũ hoặc user yêu cầu giữ format cũ.

## 🏷️ ANKI DECK NAMING (CẬP NHẬT 2026-06-29)

**4 main deck cha, dùng `::` làm separator:**

| Main deck | Chuyên khoa | Ví dụ deck con |
|---|---|---|
| **ART** | Hỗ trợ sinh sản | `ART::LPS::2026-06-29`, `ART::Trigger::EFS::2026-06-29` |
| **Fetal ultrasound** | Siêu âm thai | `Fetal ultrasound::Doppler::2026-06-24` |
| **OB/GYN** | Sản phụ khoa tổng quát | `OB/GYN::GDM::2026-06-28` |
| **Internal medicine** | Nội khoa người lớn | `Internal medicine::Topic_Short::YYYY-MM-DD` |

- `build_apkg.py` tự động detect main deck từ path folder
- Khi import vào Anki, deck cha cùng tên sẽ tự gộp → đồng bộ

## 🛠️ TOOLCHAIN PHÁT HÀNH

- `evidence_sync.py`: pha online duy nhất; Europe PMC metadata không ép OA + OA full text/license + Crossref/Retraction Watch + OpenAlex + official sources.
- `build_pipeline.py --evidence-bundle`: release runner offline canonical, chặn network subprocess.
- `publish_gate.py`: xác thực contract và hashed evidence manifest.
- `preflight_check_pmids.py` / `verify_all_pmids.py`: existence + exact identity + relevance từ bundle.
- `verify_claim_vs_abstract.py` / `verify_claims.py`: mọi occurrence, không deduplicate.
- `verify_pmid_topic.py`: advisory offline; không network.
- `verify_guidelines.py`: local PDF/web evidence + official bundle authority/type/translation/supersession.
- `retraction_check.py`: fresh integrity data từ Crossref/Retraction Watch bundle.
- `citation_audit.py --evidence-bundle`: occurrence-based; release yêu cầu 0 BLOCK/0 WARN.
- `profile_check.py` / `depth_check.py`: cấu trúc và chiều sâu theo profile.
- `build_apkg.py --verify` + `verify_apkg_diacritics.py`: build và kiểm package.
- `md_to_docx.py`: tạo DOCX release trong `outputs/`.
- `make_knowledge_check.py --output-dir outputs`: learner smoke trước publish.

Script `make_*_lesson.py` và HTML builder là legacy; chỉ dùng để rebuild bài cũ.

### CŨ (DEPRECATED - chỉ dùng để rebuild bài cũ):
- ⚠️ `make_*_lesson.py` (Long, Doppler, ICSI, FTS, PE) - hardcode content
- ⚠️ `make_lesson_docx.py`, `make_lesson_mcma.py`, etc. - build scripts cũ

## 🌍 NGÔN NGỮ (CẬP NHẬT 2026-06-22)

### Quy tắc cứng:
- **Filename/folder**: KHÔNG dấu (giữ nguyên cấu trúc cũ, an toàn Windows + PowerShell + cross-reference)
- **Content trong .md, .apkg**: CÓ DẤU đầy đủ
- **Thuật ngữ y khoa**: Giữ nguyên tiếng Anh/La-tinh (Doppler, cerebroplacental ratio, DIE, T21, ICSI)
- **Tên riêng / viết tắt**: Giữ nguyên (NEJM, ISSHP, FIGO, ASPRE)
- **Thuật ngữ tiếng Anh khó**: PHẢI có chú thích tiếng Việt ngay lần đầu. Dùng format `tiếng Việt (English)`; ví dụ `rối loạn phát triển quá mức (overgrowth disorder)`, `lớp vỏ não còn lại (cortical mantle)`, `bệnh do đường truyền mTOR (mTORopathy)`. Không để người đọc phải tự đoán nghĩa.
- **Quy tắc trình bày bảng (05/07)**: KHÔNG dùng bảng Markdown `|...|` phức tạp. Thay bằng danh sách có tiêu đề (`###` + `-`). Giữ bảng đơn giản 2 cột nếu thực sự ngắn.

### Thuật ngữ tiếng Anh từ đoạn nguồn

- Khi user gửi một đoạn tiếng Anh y khoa, ngoài việc giải thích/lưu QA nếu được yêu cầu, phải trích các thuật ngữ chuyên ngành tiếng Anh và cập nhật `F:\DL\mavisresearch\medical_qa\english_terms.md`.
- Mỗi thuật ngữ trong `english_terms.md` phải unique, không lặp lại.
- Không thêm từ phổ thông; chỉ thêm thuật ngữ có giá trị làm flashcard.
- Giữ nguyên thuật ngữ tiếng Anh; thêm nghĩa tiếng Việt ngắn sau dấu `—` khi chắc chắn.

### Ví dụ đúng:
- ✅ "Tiền sản giật", "Buồng trứng", "Mạch máu xoắn", "Doppler động mạch tử cung"
- ✅ "ISSHP 2018", "FIGO 2019", "NEJM", "ASPRE trial"
- ✅ Filename: `Sang loc Du phong Tien san giat - 2026-06-22.docx` (KHÔNG dấu)

### Ví dụ SAI:
- ❌ "Tien san giat", "Buong trung", "Mach mau xoan" (thiếu dấu)
- ❌ "Tiền Sản Giật", "BUỒNG TRỨNG" trong filename

## 🔍 VERIFICATION TỰ ĐỘNG

Sau khi viết bài mới, chạy:
```bash
python F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\verify_diacritics.py
```

Script sẽ:
1. Scan tất cả file .md trong 09_Source - Markdown
2. Tính % từ có dấu vs không dấu
3. Báo cáo bài nào < 80% có dấu → cần review
4. Output: danh sách file OK + file cần fix

## 📁 CẤU TRÚC FOLDER (CẬP NHẬT 2026-06-28)

**Từ bài 21 trở đi, MỌI deliverable của 1 bài học PHẢI nằm trong 1 folder riêng theo chuyên khoa:**

```
Bai hoc y khoa/XX_Chuyen_khoa/XX_Ten_bai/
  ├── Ten_bai_YYYY-MM-DD.md                   # Bài nguồn (có dấu)
  ├── Ten_bai_YYYY-MM-DD.cards.v2.json        # Flashcard JSON
  └── outputs/                                 # DOCX, APKG, learner smoke, sources, verification
```

**Phân loại chuyên khoa:**
- **`01_San phu khoa/`**: chuyển dạ, đẻ chỉ huy, tiền sản giật, GDM, u xơ tử cung, Asherman...
- **`02_Ho tro sinh san ART/`**: tubal patency, infertility workup, IVF/ICSI/FET, OHSS, ERA, luteal phase, stimulation, PGT...
- **`03_Sieu am thai/`**: fetal ultrasound, nước ối, Doppler, sàng lọc, độ dài cổ tử cung... (CHỈ fetal, KHÔNG chứa bài gynecology)
- **`11_Noi khoa/`**: Nội khoa người lớn.

```
F:\DL\mavisresearch\Bai hoc y khoa\
├── _README.md                          ← Danh sách 21+ bài
├── _CATALOG.md                         ← Bảng tra cứu nhanh bài học/folder/deliverables
├── WORKFLOW.md                          ← File này
├── template_lesson.md                  ← Template có dấu sẵn
├── .mavis/
│   └── AGENTS.md                        ← Project memory (cập nhật mỗi khi đổi workflow)
├── 01_San phu khoa/                    ← Bài sản khoa tổng quát
├── 02_Ho tro sinh san ART/             ← Bài ART ( cả tubal patency / HyCoSy)
├── 03_Sieu am thai/                    ← Bài siêu âm THAI (chỉ fetal)
├── 11_Noi khoa/                           ← Nội khoa người lớn
├── 10_Script Python/
│   ├── build_pipeline.py                ← Release runner canonical
│   ├── publish_gate.py                  ← Kiểm manifest có hash
│   ├── verify_claims.py                 ← Kiểm từng claim occurrence
│   ├── verify_guidelines.py             ← Guideline evidence riêng
│   ├── md_to_docx.py                    ← DOCX release bắt buộc
│   ├── build_apkg.py                    ← APKG candidate/release
│   ├── verify_diacritics.py             ← Verify dấu
│   └── make_*_lesson.py                 ← DEPRECATED
├── 80_Legacy_by_format/                ← HTML/APKG/Markdown bài cũ theo format
├── 99_Inbox/                           ← File lẻ/chưa phân loại
├── _duplicates_review/                 ← Bản trùng/folder rỗng giữ lại để review, không xóa
└── ...
```

**Dọn folder 03/07/2026:** Không xóa dữ liệu khi dọn. Bản trùng đưa vào `_duplicates_review/`, file chưa rõ đưa vào `99_Inbox/`, legacy format cũ đưa vào `80_Legacy_by_format/`. `10_Script Python/` vẫn giữ ở root để không gãy script.

## 🔄 ROTATION TOPIC

- **Luân phiên giữa ART (02_) và Fetal US (03_)** - không 2 bài cùng domain
- Đã có ~18 bài, xem `_README.md`

## ⚠️ COMMON MISTAKES (TRÁNH!)

1. ❌ Hardcode content trong build script (gây rebuild mất dấu)
2. ❌ Quên chạy `citation_audit.py` (có thể có paper sai topic)
3. ❌ Quên verify dấu sau khi build (PowerShell console hiển thị sai)
4. ❌ Cố build bằng `make_*_lesson.py` cũ (đã deprecated)
5. ❌ Copy bài cũ không dấu làm template (sẽ tiếp tục viết không dấu)
6. ❌ Dùng PowerShell `head`/`tail`/`grep` (không có - dùng `Select-Object`)
7. **❌ Cite PMID chỉ vì tồn tại.** Luôn sync bundle và qua đủ exact identity/topic/claim gates; regression `29910186` phải BLOCK sai chủ đề.
8. **❌ Suy đoán protocol/con số.** Claim định lượng cần exact quote từ abstract hoặc suitably licensed full text và Claim ID/PICO/timepoint.

## 📞 KHI CÓ VẤN ĐỀ

| Vấn đề | Giải pháp |
|---|---|
| MD có dấu nhưng DOCX không | Build lại bằng `md_to_docx.py` (KHÔNG dùng make_*_lesson.py cũ) |
| PowerShell hiển thị `?` | Verify content bằng `python -c` |
| Evidence sync 429/5xx/malformed/outage | Fail-closed; không retry/proxy/NCBI fallback; sync lại sau khi provider phục hồi |
| Citation audit > 0 BLOCK/WARN | Sửa occurrence/source/claim/authority rồi tạo bundle mới; không hạ gate |
| Muốn đổi workflow mới | Update `WORKFLOW.md` + `AGENTS.md` + `MEMORY.md` (3 chỗ) |

## 🔗 RELATED FILES

- `_README.md` - Danh sách bài đã có
- `.mavis/AGENTS.md` - Project memory (conventions chi tiết)
- `template_lesson.md` - Template bài học có dấu
- `10_Script Python/verify_diacritics.py` - Verify tự động
- `10_Script Python/citation_audit.py` - Citation audit
- `10_Script Python/md_to_docx.py` - MD → DOCX parser
- `RESEARCH_BRIEF_TEMPLATE.md` - Template brief cho 2-tier research → execute
- `STRICT_EXECUTE_PROMPT.md` - Prompt mẫu siết chặt cho Model Execute (Tầng 2)
- `LEARNING_PATH.md` - Bản đồ prerequisite giữa các bài
- `KNOWLEDGE_CHECK_WORKFLOW.md` - Tạo bài kiểm tra sau bài học
- `10_Script Python/verify_pmid_topic.py` - Gate MeSH alignment (mới từ 26/07/2026)
- `10_Script Python/verify_claim_vs_abstract.py` - Gate claim-abstract match (mới)
- `10_Script Python/preflight_claim_check.py` - Gate pre-execution blocker (mới)

---

## 📏 CHI TIẾT BÀI HỌC — MẶC ĐỊNH CHẾ ĐỘ L3_BEGINNER

Mọi bài học y khoa mới bắt buộc chạy ở chế độ **`L3_BEGINNER`** (tên hiển thị: `L3 — Cầm tay chỉ việc cho người mất gốc`). Không có lựa chọn cấp độ hay rút gọn bài. Profile (`foundation`, `disease`, `pharmacology`) chỉ phân loại cấu trúc chuyên môn, tất cả đều phải thỏa mãn tiêu chuẩn cầm tay chỉ việc, giải thích từ gốc cho người mất gốc và không giới hạn độ dài tối đa.

| Profile | Ngưỡng tối thiểu `lesson_depth_contract` (bắt buộc mode `L3_BEGINNER`) | Đối tượng & Yêu cầu |
|---|---|---|
| **Foundation (`foundation`)** | $\ge 5.000$ từ, $\ge 500$ dòng, $\ge 10$ sections, $\ge 12$ subsections, $\ge 3$ mechanism chains (5 tầng), $\ge 6$ ví dụ, $\ge 6$ bẫy/nhầm lẫn, $\ge 4$ checkpoints, $\ge 2$ case có lời giải 5 bước, $\ge 10$ practical tips | Người mất gốc, sinh viên. Giải thích từ gốc. *Lưu ý:* Không ép buộc kê đơn/liều thuốc với bài foundation thuần sinh lý/giải phẫu không có thuốc. |
| **Disease (`disease`)** | $\ge 6.000$ từ, $\ge 600$ dòng, $\ge 10$ sections, $\ge 14$ subsections, $\ge 4$ mechanism chains, $\ge 8$ ví dụ, $\ge 8$ bẫy/nhầm lẫn, $\ge 5$ checkpoints, $\ge 3$ case có lời giải, $\ge 12$ tips, $\ge 2$ phác đồ mẫu | Bác sĩ, học viên. Chi tiết lâm sàng, chẩn đoán, điều trị toàn diện. |
| **Pharmacology (`pharmacology`)** | $\ge 6.000$ từ, $\ge 600$ dòng, $\ge 8$ sections, $\ge 14$ subsections, $\ge 5$ mechanism chains, $\ge 8$ ví dụ, $\ge 8$ bẫy/nhầm lẫn, $\ge 5$ checkpoints, $\ge 3$ case có lời giải, $\ge 12$ tips, $\ge 3$ phác đồ mẫu | Bác sĩ, dược sĩ. Khoan sâu dược lý, cơ chế 5 tầng, tương tác & chỉnh liều. |

### Quy tắc cấu trúc cho L3_BEGINNER:
- **Dạy từ gốc:** Mọi thuật ngữ khó lần đầu xuất hiện dùng format `tiếng Việt (English)`.
- **Cơ chế 5 tầng:** Tầng 1 (phân tử/receptor) → Tầng 2 (tế bào/mô) → Tầng 3 (lâm sàng/xét nghiệm) → Tầng 4 (quyết định) → Tầng 5 (phản chứng/hậu quả).
- **Flowchart:** KHÔNG dùng Mermaid diagram syntax. Dùng khối `text` ASCII-art hoặc danh sách phân cấp (Nested lists).
- **Case có lời giải:** Phải giải 5 bước (nhận diện nguy cơ → dữ kiện thay đổi → hành động ngay → theo dõi/chuyển tuyến → lý do loại phương án sai).

### Quy tắc xây dựng cho chế độ L3_BEGINNER:

1. **Khóa contract trước research:** Mọi bài học mới đều phải đăng ký `lesson_depth_contract` với profile phù hợp (`foundation`, `disease`, `pharmacology`) và `"mode": "L3_BEGINNER"` trong Research Brief.
2. **Không trần độ dài:** Thỏa mãn tối thiểu số từ, số dòng, subsections, mechanism chains 5 tầng, ví dụ, bẫy, checkpoints, cases có lời giải, practical tips và phác đồ theo profile.
3. **Cấm lặp ý/padding:** Bài viết dài nhờ chiều sâu giải thích, reasoning chain, ví dụ thực tế và trường hợp lâm sàng đặc thù — không lặp lại câu từ hoặc danh sách trần.

## 🧠 PLAN-MODE — Khi nào dùng

**Plan-mode** là skill có sẵn trong harness, tự động research → plan → chờ duyệt → execute.
