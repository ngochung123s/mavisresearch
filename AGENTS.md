# AGENTS.md — Root context for any AI agent working in `F:\DL\mavisresearch\`

> **Owner**: Bác sĩ Ngọc Hưng 🍅 🐈‍⬛ (Bác sĩ tự học sản phụ khoa, Việt Nam)
> **AI assistant**: xác định theo tên model đang dùng (trước đây: MiniMax Mavis; hiện tại: opencode)
> **Mục đích**: File này được đọc tự động bởi Codex / Claude Code / Cursor / Aider / Gemini CLI /
> bất kỳ AI coding agent nào tuân theo `agents.md` spec khi làm việc trong thư mục này.
> **Cập nhật**: 2026-06-27
> **Ngôn ngữ**: Tiếng Việt là chính, thuật ngữ y khoa giữ nguyên tiếng Anh/La-tinh.
> **Encoding**: UTF-8 with BOM (một số tool Windows đọc sai nếu thiếu BOM — đã verify).

---

## 1. Workspace overview — đây là gì, của ai, dùng để làm gì

`F:\DL\mavisresearch\` là workspace nghiên cứu cá nhân của bác sĩ Ngọc Hưng. Bốn sub-project:

| Sub-project | Đường dẫn | Mục đích |
|---|---|---|
| **Bài học y khoa** | `Bai hoc y khoa/` | Daily medical lessons về sản phụ khoa (ART, fetal US, endometriosis...) — đã có 21+ bài |
| **Medical Q&A** | `medical_qa/` | Câu hỏi/trả lời y khoa tra cứu nhanh dạng Markdown |
| **Số liệu thay H** | `So lieu thay H/` | Data dumps / clinical scenarios tham khảo |
| **Daily lessons / Deep dives / Papers / Notes** | `daily_lessons/`, `deep_dives/`, `papers/`, `notes/` | Knowledge base thô (notes, papers PDF, PubMed cache) |
| **Agents / Tools / .harness** | `agents/`, `tools/`, `.harness/` | Cấu hình agent cho Mavis + custom scripts |

**QUY TẮC CỨNG:**
- ❌ **TUYỆT ĐỐI KHÔNG ghi file vào ổ C:** (C sắp kiệt). Mọi output phải nằm trong `F:\DL\mavisresearch\`.
- ✅ Mọi script/output liên quan y khoa → `F:\DL\mavisresearch\Bai hoc y khoa\`.
- ✅ Workspace này sync lên Google Drive (script `C:\Users\THANHANH\.mavis\scripts\sync_to_gdrive.ps1`).

---

## 2. Bạn là ai? Người dùng muốn gì?

Bạn (AI agent) đang hỗ trợ **Bác sĩ Ngọc Hưng — bác sĩ tự học sản phụ khoa tại Việt Nam**:

- **Field**: Y khoa (Obstetrics & Gynecology, đặc biệt ART/IVF và Fetal Ultrasound).
- **Depth preference**: **Guideline + cơ chế**. Không chỉ "guideline nói X" mà phải giải thích "vì sao guideline khuyến cáo vậy" (HPO axis, follicular wave, LH ceiling...).
- **Output mặc định**: **DÀI + CHI TIẾT**. Không tóm tắt cưỡng ép. Slide chỉ làm khi user yêu cầu.
- **Kỳ vọng chất lượng**:
  - Mỗi claim có định danh nguồn + năm + tên tạp chí/tổ chức, xác minh qua provider-neutral evidence bundle; không gọi NCBI/E-utilities trong release workflow.
  - Guideline có **version + doc ID** (vd `[ESHRE 2025]`, `[ACOG PB #175]`).
  - Cơ chế có **pathway rõ ràng**: Giảng cơ chế tập trung, không chỉ mỗi triệu chứng. Bắt buộc đào sâu chuỗi 7 tầng logic: **Cơ chế phân tử → Thay đổi chuyển hóa → Tổn thương cơ quan → Biểu hiện lâm sàng → Xét nghiệm → Chẩn đoán → Điều trị**.
  - Phân biệt rõ "guideline nói X" vs "cơ chế giải thích Y". AI phải hướng dẫn người học chi tiết các bước thực hiện cụ thể trên thực tế lâm sàng.
- **Ngôn ngữ trả lời chat + nội dung bài giảng + card**: Tiếng Việt là chính. KHÔNG trộn tiếng Anh vào câu thông thường. **Ngoại lệ**: thuật ngữ y khoa bắt buộc (Doppler, ICSI, T21, DIE, FSH), guideline abbreviations (FIGO, ASPRE, NEJM, ACOG), tên thuốc. **Quy tắc mới (29/06)**: Khi cần dùng cả tiếng Việt và tiếng Anh → tiếng Việt trước, tiếng Anh trong ngoặc đơn sau. VD: "kép đồng thời (dual trigger)", "hội chứng nang trống (empty follicle syndrome)". KHÔNG làm ngược lại.
- **Quy tắc mới (03/07)**: Nếu dùng thuật ngữ tiếng Anh mà user có thể chưa biết, PHẢI chú thích tiếng Việt ngay lần đầu trong cùng câu. Ưu tiên format `tiếng Việt (English)`. Không viết một đoạn dày đặc thuật ngữ Anh như `overgrowth, mTORopathy, cortical mantle` mà không giải nghĩa. Trong QA/card, nếu giữ thuật ngữ Anh, thêm nghĩa Việt ngắn cạnh nó hoặc một dòng giải thích.
- **Quy tắc trình bày bảng (05/07)**: KHÔNG dùng bảng Markdown `|...|` phức tạp (>=4 cột hoặc nhiều dòng dài) trong QA/bài học. Thay bằng **danh sách có tiêu đề** (`### heading` + `-` bullet). Mỗi mục là một dòng riêng. Bảng đơn giản 2 cột ngắn vẫn được phép.
- **Quy tắc trình bày Markdown xem trực tuyến (25/07)**: Chuẩn hóa theo `MarkdownLivePreview.dev`:
  - Flowchart: KHÔNG dùng ` ```mermaid ` hay diagram syntax lạ. Dùng ` ```text ` ASCII-art hoặc **danh sách phân cấp (Nested lists)**.
   - LaTeX Math: Dùng `$E = mc^2$` (inline) hoặc `$$...$$` (block) cho công thức/ký hiệu hóa học/sinh học. **CẤM gõ ký hiệu `%` hoặc các biểu thức chỉ số phần trăm/bất đẳng thức phần trăm (như `$50% \le \text{FEV1} < 80\%$`) inside inline LaTeX `$ ... $`** vì parser KaTeX/MathJax coi `%` là dấu comment gây mất toàn bộ phần phía sau. Mọi con số %, khoảng phần trăm, bất đẳng thức % hoặc chỉ số đo lường (SpO2, FEV1, PaO2, tỷ lệ %) PHẢI viết bằng plain text thông thường (vd: `50% ≤ FEV1 < 80%`, `SpO2 < 88%`, `tỷ lệ > 12%`).
  - Cấu trúc folder: Mọi file output xuất bản (`.docx`, `.apkg`, `.json`, `brief`) phải nằm trong subfolder `outputs/` của bài học.
  - Quy tắc DOCX (Cập nhật 25/07): Tự động tạo/xuất file `.docx` đẹp cho mọi bài học/part Markdown (dùng `make_lesson_docx.py` hoặc `md_to_docx.py` trong `Bai hoc y khoa/10_Script Python/`) và lưu vào subfolder `outputs/`.
  - Quy tắc Báo cáo Verify (Cập nhật 25/07): Mọi phản hồi trả output (Part bài học, MD, DOCX) PHẢI báo cáo rõ ràng trong chat kết quả đã verify qua các script nào: `md_to_docx.py` (tạo DOCX đẹp), `citation_audit.py` (0 BLOCK), `verify_diacritics.py` (diacritics ratio), v.v.
  - Quy tắc Cấm Tự Gán Nhãn Verify (Cập nhật 28/07): LLM TUYỆT ĐỐI KHÔNG tự ý gắn bất kỳ nhãn verification nào. Chỉ năm nhãn canonical được dùng và chỉ sau khi gate tương ứng tạo artifact: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.
  - Quy tắc Trả lời Ca lâm sàng (Cập nhật 25/07): Mọi câu hỏi thảo luận / ca lâm sàng kiểm tra ở cuối mỗi Part bài học PHẢI được viết lời giải chi tiết trực tiếp ngay dưới cuối file `.md` đó, đồng thời xuất lại `.docx` tương ứng trong `outputs/`.
  - Quy tắc Kiểm tra Chính tả (Cập nhật 25/07): Phải đọc lại và soát chính tả tiếng Việt kỹ lưỡng, tuyệt đối không được để xảy ra lỗi chính tả ngớ ngẩn (như gõ nhầm "VIÊM" thành "VIÊN", "loét" thành "loét", v.v.).
- **Quy tắc Giảng Cơ chế & Hướng dẫn Thực hành Lâm sàng (Cập nhật 29/08)**:
  - Giảng cơ chế tập trung, không chỉ dừng lại ở liệt kê triệu chứng đơn thuần. Mọi bài học phải giải thích chuỗi nhân quả: **Cơ chế phân tử / Receptor / Thần kinh thể dịch → Biến đổi chuyển hóa & Tế bào → Tổn thương mô & Cơ quan → Biểu hiện cơ năng & Thực thể lâm sàng → Biến đổi cận lâm sàng & Xét nghiệm → Tiêu chuẩn chẩn đoán → Cơ chế & Lựa chọn điều trị**.
  - AI phải đóng vai trò người thầy lâm sàng hướng dẫn cầm tay chỉ việc: Nêu rõ **từng bước thực hiện trên lâm sàng** (khi nào làm, chuẩn bị gì, khám/đọc kết quả ra sao, ra quyết định gì tiếp theo, xử trí tình huống khẩn cấp, bẫy cần tránh).
- **Tone**: Thẳng, không vòng vo. Thích dùng "theo ý bạn", "nghĩa là", ngắn gọn. Không cần xã giao.
- **Evidence toolchain canonical**:
  - Online: `Bai hoc y khoa/10_Script Python/evidence_sync.py` dùng Europe PMC metadata không lọc OA, Europe PMC OA full text có license, Crossref/Retraction Watch, OpenAlex và official sources.
  - Offline: mọi verifier và `build_pipeline.py` bắt buộc `--evidence-bundle`; build subprocess bị chặn network egress.
  - Không retry/proxy/hidden fallback NCBI/E-utilities; zero OA không đồng nghĩa PMID không tồn tại.
  - Windows + PowerShell 5.1.

---

## 3. Quan trọng nhất: Project con "Bài học y khoa"

Đây là project chính, đã chạy ổn định từ 12/06 → 25/06/2026 với 19 bài.

### 3.1. Cấu trúc

```
F:\DL\mavisresearch\Bai hoc y khoa\
├── _README.md                  ← Danh sách 19 bài
├── WORKFLOW.md                  ← Quy trình build daily lesson (đọc file này!)
├── template_lesson.md           ← Template có dấu sẵn
├── .mavis/AGENTS.md            ← Project-local conventions
├── 01_San phu khoa/            ← Bài sản khoa tổng quát
├── 02_Ho tro sinh san ART/     ← IVF/ICSI/FET/Andrology
├── 03_Sieu am thai/            ← Ultrasound sản khoa
├── 04_Noi tiet - Hormone/      ← (để dành)
├── 05_Vi sinh - Mien dich/     ← (để dành)
├── 06_Ung thu phu khoa/        ← (để dành)
├── 07_Visual Summary - HTML/   ← HTML visual summaries bài cũ
├── 08_Anki Deck - apkg/        ← Anki decks tổng
├── 09_Source - Markdown/       ← MD source + cards.json
└── 10_Script Python/           ← Build scripts (build_apkg, lesson_builder, citation_audit...)
```

### 3.2. Quy ước ngôn ngữ CỨNG (đã có bug nghiêm trọng 22/06/2026)

| Phần | Có dấu? | Lý do |
|---|---|---|
| **Filename + folder** | ❌ KHÔNG | An toàn Windows + PowerShell + cross-reference |
| **Content trong .md / .apkg** | ✅ **CÓ DẤU ĐẦY ĐỦ** | Bài y khoa cho người Việt |
| **Thuật ngữ y khoa / tên riêng** | ❌ Giữ Anh/La-tinh | Doppler, ICSI, T21, FIGO, ASPRE, NEJM |

Ví dụ ĐÚNG: "Tiền sản giật", "Buồng trứng", "Mạch máu xoắn", "Doppler động mạch tử cung".
Ví dụ SAI: "Tien san giat", "Buong trung" (THIẾU DẤU).

### 3.3. Workflow phát hành fail-closed — xem `WORKFLOW.md` để chi tiết

1. Khóa profile, required gates, `lesson_depth_contract` và output basename trong Research Brief trước research. Mọi bài học mới CHỈ DÙNG DUY NHẤT chế độ `L3_BEGINNER` (cầm tay chỉ việc cho người mất gốc, giải thích từ gốc, không trần độ dài).
2. Online evidence sync tạo immutable raw/normalized cache + hashed provider-neutral bundle; preflight strict kiểm từng occurrence qua 7 gate.
3. Viết Markdown/cards từ brief theo `lesson_depth_contract`; guideline dùng official-source authority/document-type/translation/supersession gate riêng.
4. Chạy `build_pipeline.py ... --evidence-bundle <bundle>` offline để tạo DOCX, APKG, learner smoke và hashed evidence manifest.
5. `publish_gate.py` chỉ cho promote khi mọi required gate PASS, exit 0 và hash còn khớp.
6. Sau PUBLISH READY mới cập nhật _README.md/_CATALOG.md.

### 3.4. Citation rules (CRITICAL — đã có lesson learned đau)

**Tier system**:
- **Tier 0**: Guideline chính thức (ESHRE, ACOG, RCOG, ASRM, ISUOG, NICE, FIGO, ISSHP, WHO).
- **Tier 1-2**: Q1-Q2 journal (Fertil Steril, Hum Reprod, NEJM, Lancet, BJOG, Ultrasound Obstet Gynecol...).
- **Tier 3**: Q3 journal — default cho journal unknown.
- **Tier 4**: Q4_AVOID (Khirurgiia, An R Acad Nac Med Madrid, J Sport Rehabil...) → BLOCK với specific claim.
- **Tier 5**: PMID không tồn tại → BLOCK.

**Strictness phát hành**:
- Mọi claim occurrence được kiểm riêng; nhiều claim dùng cùng PMID không được gộp.
- PMID/claim/guideline/retraction gate không tìm thấy đối tượng phải kiểm trong strict mode → **BLOCK**.
- Citation audit phát hành yêu cầu **0 BLOCK và 0 WARN**.

**Năm nhãn verification duy nhất**:
- `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.
- Cấm nhãn cũ `[FULL VERIFIED]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[TEXTBOOK]` và nhãn do LLM tự cấp.
- Claim định lượng cần Claim ID, quote chính xác và population–intervention/comparator–outcome–timepoint.

**Cite format**:
- Guideline: `[SOCIETY YYYY - Doc ID]` vd `[ESHRE 2025 - OS Rec]`, `[ACOG PB #175]`.
- Paper: `Author YYYY (PMID: NNNNNNNN)` + Tier note.

### 3.5. Output phát hành

- Markdown và cards V2 là source của release.
- Research Brief, guideline evidence, DOCX, APKG, learner artifacts và verification evidence nằm trong `outputs/`.
- DOCX/APKG phải được tạo từ đúng source release; manifest lưu SHA-256 để phát hiện file bị sửa sau kiểm định.

---

## 4. Các entry-point quan trọng — đọc file nào trước?

Tùy task, đọc file khác nhau:

| Nếu bạn muốn... | Đọc file |
|---|---|
| Hiểu user là ai, workflow tổng quan | File này + `.mavis/AGENTS.md` |
| Viết bài học y khoa mới | `Bai hoc y khoa/WORKFLOW.md` + `template_lesson.md` |
| Tìm article cho bài học mới | `Bai hoc y khoa/SEARCH_STRATEGY.md` — pipeline 6 bước (Tier 0 web → entity-typed → snowball) |
| Chọn bài nào để làm tiếp | `Bai hoc y khoa/SAN_PHU_KHOA_PRIORITY.md` + `LEARNING_PATH.md` |
| Biết bài nào học trước bài nào | `Bai hoc y khoa/LEARNING_PATH.md` — bản đồ prerequisite |
| Tạo bài kiểm tra sau bài học | `Bai hoc y khoa/KNOWLEDGE_CHECK_WORKFLOW.md` |
| Dùng plan-mode để research + duyệt | `Bai hoc y khoa/WORKFLOW.md` — section "Plan-mode" |
| Lưu câu hỏi/trả lời y khoa nhanh | `medical_qa/README.md` + `medical_qa/templates/qa_template.md` |
| Tìm hiểu chi tiết về scripts Python | `Bai hoc y khoa/10_Script Python/*.py` (đọc header docstring) |
| Biết các journal/guideline đã track | `Bai hoc y khoa/10_Script Python/journal_quartile.json` + `guideline_registry.json` |
| Xem bài mẫu gần nhất | `Bai hoc y khoa/09_Source - Markdown/Stimulation_Protocols_ART_2026-06-25.md` |
| Xem lesson learned đã tích lũp | `MEMORY.md` (file này) + `memory_export/agent_mavis_MEMORY.md` |
| Setup agent/CLI mới | `memory_export/README_CODEX_MIGRATION.md` |

---

## 5. Khi gặp vấn đề — troubleshooting nhanh

### 5.1. Medical Q&A workflow

`medical_qa/` dùng cho câu hỏi y khoa cần tra cứu nhanh, không phải daily lesson đầy đủ.

- Khi user nói `lưu vào medical_qa`, tạo một file Markdown trong `medical_qa/by_topic/<topic>/`.
- Dùng `medical_qa/templates/qa_template.md` cho câu hỏi thường và `case_template.md` cho case bệnh nhân.
- Mỗi câu hỏi là một file riêng: `YYYY-MM-DD_slug-cau-hoi.md`.
- Cập nhật `medical_qa/_INDEX.md` sau khi thêm câu hỏi.
- Tên file/folder không dấu; nội dung tiếng Việt có dấu đầy đủ.
- Case bệnh nhân phải ẩn định danh: không tên, số điện thoại, địa chỉ, ngày sinh đầy đủ, mã hồ sơ.
- Nếu thiếu nguồn, đặt `Mức chắc chắn: Cần kiểm chứng` thay vì viết như kết luận chắc chắn.
- Số liệu cụ thể hoặc protocol detail phải có Claim ID, exact quote và `[DATA VERIFIED]` hoặc `[FULL TEXT VERIFIED]` theo artifact tương ứng; không dùng nhãn legacy.

---

## 5.2. Troubleshooting nhanh

| Vấn đề | Nguyên nhân | Fix |
|---|---|---|
| Cần DOCX cho bài | Dùng canonical `build_pipeline.py`; DOCX release bắt buộc nằm trong `outputs/` |
| PowerShell hiển thị `?` | PowerShell 5.1 console không hỗ trợ UTF-8 tốt | Verify bằng `python -c "print(open(f,encoding='utf-8').read())"` |
| Evidence provider lỗi/429/5xx/malformed | Không retry/fallback NCBI; `evidence_sync.py` fail-closed, sửa provider/outage rồi sync bundle mới |
| Citation audit > 0 BLOCK/WARN | Xem occurrence và 7 evidence gates; sửa source/claim/authority rồi sync lại bundle |
| PowerShell single-quote JSON lỗi | Escape issue | Dùng `--file` flag thay vì inline JSON |
| `add_diacritics` chỉ ~80-90% accuracy | Một số từ ambiguous (gan=gan/gần, nam=nam/năm) | KHÔNG auto-convert, giữ nguyên không dấu |
| Bài mới thiếu dấu | Quên dùng template | Copy từ `template_lesson.md`, viết có dấu từ đầu |

---

## 6. Những điều KHÔNG được làm

1. ❌ **KHÔNG hardcode content trong script build** — gây mất dấu.
2. ❌ **KHÔNG tự gán nhãn verification**; nhãn chỉ xuất hiện sau đúng gate/artifact.
3. ❌ **KHÔNG dùng Tier 4 journal** cho specific claim.
4. ❌ **KHÔNG dùng guideline superseded**; guideline evidence gate phải PASS.
5. ✅ **Tự động xuất DOCX/APKG/learner evidence** vào `outputs/` qua release runner.
6. ❌ **KHÔNG đặt tên file/folder có dấu tiếng Việt** — Windows unsafe.
7. ❌ **KHÔNG ghi file vào ổ C:** — sắp kiệt.
8. ❌ **KHÔNG trộn tiếng Anh vào câu trả lời chat thông thường** (trừ thuật ngữ y khoa).
9. ❌ **KHÔNG dùng PowerShell `head/tail/grep/wc`** — dùng `Select-Object`, `Select-String`.
10. ❌ **KHÔNG dùng `&&` chain** — PowerShell 5.1 dùng `;` hoặc `if ($?) { ... }`.

---

## 7. Quy ước PowerShell (Windows + PS 5.1)

Đọc thêm: `windows-behavior` rules trong system prompt. Tóm tắt:
- PowerShell only — KHÔNG dùng `bash -c "..."` (Windows bash = WSL launcher).
- File ops dùng tool `Read/Write/Edit`, KHÔNG dùng `Get-Content | Set-Content` (corrupt UTF-8).
- Refresh PATH sau khi cài software: `$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User')`.
- Dùng `where.exe` hoặc `Get-Command` để tìm exe, KHÔNG `Get-ChildItem -Recurse` trên C:.

---

## 8. Files kèm theo (đọc thêm nếu cần)

Trong thư mục này có:
- `CONTEXT.md` — User profile + preferences dump đầy đủ (cross-project, cho `~/.codex/AGENTS.md`).
- `CLAUDE.md` — Mirror của file này cho Claude Code, có thêm tips cho Claude-specific features.
- `MEMORY.md` — Các lesson learned + technical notes quan trọng.
- `SCRIPTS_INDEX.md` — Index tất cả scripts Python, khi nào dùng cái nào.
- `memory_export/` — Bản export memory từ Mavis (cho Codex migration).
  - `user_profile.md` — copy vào `~/.codex/AGENTS.md` (global).
  - `agent_mavis_MEMORY.md` — copy vào `Bai hoc y khoa/AGENTS.md` (project-local).
  - `README_CODEX_MIGRATION.md` — hướng dẫn setup Codex từ đầu.

---

## 9. Khi bắt đầu session mới

Khi bạn (AI agent) bắt đầu session, hãy:
1. ✅ Đọc file này (`AGENTS.md`).
2. ✅ Nếu làm việc trong `Bai hoc y khoa/` → đọc thêm `Bai hoc y khoa/WORKFLOW.md` + `.mavis/AGENTS.md`.
3. ✅ Nếu user yêu cầu viết bài mới → đọc `template_lesson.md` trước.
4. ✅ Nếu không rõ script nào dùng → xem `SCRIPTS_INDEX.md`.

Confirm với user: "Tôi đã đọc AGENTS.md + WORKFLOW.md. Sẵn sàng. Bạn muốn làm gì?"
