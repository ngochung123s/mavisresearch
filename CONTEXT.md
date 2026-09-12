# CONTEXT.md — User profile & cross-project context

> **Mục đích**: File này chứa toàn bộ context về USER (bác sĩ Ngọc Hưng) — copy vào `~/.claude/CLAUDE.md`
> (global) để Claude Code ở bất kỳ project nào cũng biết bạn là ai.
> **Cập nhật**: 2026-06-27
> **Tương thích**: Mavis memory format + Codex AGENTS.md format + Claude CLAUDE.md format.

---

## User Identity

- **Tên**: Ngọc Hưng (Bác sĩ Ngọc Hưng 🍅 🐈‍⬛)
- **Nghề nghiệp**: Bác sĩ tự học sản phụ khoa (xác nhận 2026-06-10)
- **Quốc gia**: Việt Nam
- **Có thể là một trong**: bác sĩ đa khoa / bác sĩ chuyên khoa khác muốn update sản phụ khoa / bác sĩ đang ôn thi / bác sĩ nghiên cứu
- **KHÔNG phải**: giảng viên, không trực tiếp đứng lớp

---

## Communication preferences

- **Ngôn ngữ**: Tiếng Việt là chính. **KHÔNG trộn tiếng Anh** vào câu thông thường.
- **Ngoại lệ** (giữ nguyên tiếng Anh/La-tinh):
  - Thuật ngữ y khoa: Doppler, ICSI, T21, DIE, FSH, LH, OHSS, PCOS, AMH, AFC, HSG, SIS, TESE, MESA, PGT-A, PGT-M.
  - Guideline abbreviations: FIGO, ASPRE, ACOG, ASRM, ESHRE, RCOG, NICE, ISUOG, ISSHP, WHO, NEJM, ICMART.
  - Tên thuốc: aspirin, hCG, GnRH, clomiphene, letrozole, metformin.
  - Tên riêng: ASPRE trial, Bologna criteria, Poseidon criteria, etc.
- **Tone**: Thẳng, không vòng vo. Thích dùng "theo ý bạn", "nghĩa là", ngắn gọn.
- **Default output**: **DÀI + CHI TIẾT**. KHÔNG tóm tắt cưỡng ép.
- **Slide/PowerPoint**: Chỉ làm khi user yêu cầu.
- **Kỳ vọng chất lượng**:
  - Guideline có **PMID + năm + doc ID**.
  - Cơ chế có **pathway rõ ràng**.
  - Phân biệt rõ "guideline nói X" vs "cơ chế giải thích Y".
  - Mỗi claim có **mức độ chắc chắn** (Strong/Moderate/Conditional, hoặc Tier 0/1/2).

---

## Depth preference: Guideline + Cơ chế

User **KHÔNG** muốn chỉ:
- ❌ "Theo ACOG thì nên làm X" (chỉ khuyến cáo)

User **MUỐN** cả hai:
- ✅ "Theo ACOG PB #175 (2020) thì nên làm X vì..."
- ✅ "...và về cơ chế, estrogen window đóng vai trò Y qua pathway Z (HPO axis...)"
- ✅ "Bằng chứng đằng sau: meta-analysis A (PMID NNNN) cho thấy..."

**Rule**: Mỗi guideline recommendation → giải thích cơ chế endocrine/molecular đằng sau.

---

## Tech comfort

- ✅ Biết khái niệm **MCP** (Model Context Protocol).
- ✅ Dùng **PubMed qua web** thường xuyên.
- ✅ Hệ điều hành: **Windows + PowerShell 5.1**.
- ✅ Biết Python cơ bản (chạy script, đọc JSON).
- ❌ KHÔNG muốn cài tool nặng (vd biomcp) — prefers lean solutions, không thích bloat.

---

## Workspace & file system

- **Workspace gốc**: `F:\DL\` (thư mục Download/tài liệu trên ổ F:).
- **Output folder bài học y khoa**: `F:\DL\mavisresearch\Bai hoc y khoa\` (CẬP NHẬT 2026-06-13).
- ❌ **TUYỆT ĐỐI KHÔNG ghi file vào ổ C:** (C sắp kiệt).
- **Sync**: Workspace sync lên Google Drive qua `sync_to_gdrive.ps1`.

### Cấu trúc `Bai hoc y khoa/`

```
01_San phu khoa/              ← Sản phụ khoa tổng quát
02_Ho tro sinh san ART/       ← IVF/ICSI/FET/Andrology
03_Sieu am thai/              ← Ultrasound sản khoa
04_Noi tiet - Hormone/        ← (để dành)
05_Vi sinh - Mien dich/       ← (để dành)
06_Ung thu phu khoa/          ← (để dành)
07_Visual Summary - HTML/     ← HTML visual summaries bài cũ
08_Anki Deck - apkg/          ← Anki decks
09_Source - Markdown/         ← MD source + cards.json
10_Script Python/             ← Build scripts (build_apkg, lesson_builder, citation_audit...)
```

---

## ART/IVF Knowledge Level (2026-06-12)

### ĐÃ BIẾT (không cần dạy lại)
- ✅ Trigger protocols: HCG, GnRH agonist trigger.
- ✅ Phác đồ: Antagonist protocol, PPOS (progestin-primed ovarian stimulation).
- ✅ Sinh trắc học cơ bản (biometrics basics — chưa sâu).

### CẦN HỌC SÂU HƠN (chủ đề daily lesson sẽ xoay quanh đây)
- 🔍 GnRH agonist long protocol (chi tiết).
- 🔍 GnRH agonist short/flare protocol.
- 🔍 Mild stimulation / Natural cycle IVF.
- 🔍 Double stimulation (DuoStim).
- 🔍 Advanced biometrics: endometrial volume, 3D/4D ultrasound, ovarian reserve tests (AMH, AFC chi tiết).
- 🔍 Uterine factor: HSG, HyFoSy, SIS, hysteroscopy.
- 🔍 Male factor: SA (semen analysis), DNA fragmentation, TESE/MESA.
- 🔍 Embryology: ICSI, time-lapse, PGT-A/PGT-M.
- 🔍 Siêu âm thai kỳ chuyên sâu: cervical length, Doppler, growth charts, fetal biometry.

---

## Tools available (cập nhật 2026-06-13)

### MCP servers
- **`pubmed`** tại `C:\Users\THANHANH\.mavis\mcp\pubmed.py` — 8 tools:
  - `pubmed_search` — search PubMed, có filter (year, article_type, free_full_text, sort).
  - `pubmed_fetch` — fetch full abstract by PMID. **⚠️ BỊ LỖI TRẢ EMPTY — dùng webfetch E-utilities thay**.
  - `pubmed_related` — similar articles.
  - `pubmed_pmc_link` — check PMC availability + return URLs.
  - `pubmed_pmc_pdf` — download PDF (UNRELIABLE cho paper mới, ưu tiên fulltext).
  - `pubmed_pmc_fulltext` — fetch full text as plain text (parse JATS XML từ Europe PMC) — **CÁCH TỐT NHẤT để đọc paper open-access**.
  - `trial_search` — search ClinicalTrials.gov v2.
  - `trial_fetch` — fetch trial by NCT ID.

- **NCBI API key**: `e71bce83...63408` (đã set) → rate limit 10 req/s (gấp 3 lần không key).
- **Cache key normalize** (diacritics-strip, lowercase) → hit rate tốt hơn.

### Custom scripts (tại `C:\Users\THANHANH\.mavis\scripts\`)
- `weekly_papers.py` — Tự động tìm paper mới về ART/IVF + Fetal Ultrasound, gửi Telegram mỗi tối thứ 7 lúc 20h.
- `multi_pmid.py` — Tóm tắt + so sánh nhiều PMID (cho literature review).
- `citation_graph.py` — Vẽ sơ đồ citation giữa các paper (HTML + vis.js).
- `sync_to_gdrive.ps1` — Sync `.mavis` lên Google Drive.
- `make_anki_deck.py` — JSON → Anki .apkg.

---

## Daily lesson workflow

- **Tần suất**: 1 bài/ngày, **21:00 Vietnam time** (cron `daily-lesson-2100` của Mavis).
- **Output**: 2 dạng mỗi bài:
  1. **Tin nhắn Telegram** (tóm tắt + link).
  2. **File .apkg** (Anki deck, theme **Pastel**).

- **Anki deck content**: Chỉ cần văn bản gốc, KHÔNG cần phần "Góc nhìn bổ sung của AI".

- **Topic rotation**: Luân phiên ART (02_) và Fetal US (03_) — không 2 bài cùng domain.

---

## Citation rules (CRITICAL)

### Tier system
| Tier | Loại | Xử lý |
|---|---|---|
| **0** | Guideline (ESHRE, ACOG, RCOG, ASRM, ISUOG, NICE, FIGO, ISSHP, WHO) | **Mạnh nhất**, OK cho cả specific claim |
| **1** | Q1 journal (Fertil Steril, Hum Reprod, NEJM, Lancet, BJOG, UOG) | Specific claim cần `[FULL VERIFIED]` |
| **2** | Q2 journal | Specific claim cần `[FULL VERIFIED]` |
| **3** | Q3 journal (default cho unknown) | Cân nhắc |
| **4** | Q4_AVOID (predatory, sai topic) | **BLOCK** nếu có specific claim |
| **5** | PMID NOT_FOUND | **BLOCK** |

### Strictness hybrid
- **Specific claim** (RR/CI/%/n=) + Tier 4 → **BLOCK** (không publish).
- **Specific claim** + Tier 1/2 → **WARN** (cần `[FULL VERIFIED]`).
- **Direction only** + Tier 1/2 → **OK**.

### Cite format
- **Guideline**: `[SOCIETY YYYY - Doc ID]` vd `[ESHRE 2025 - OS Rec]`, `[ACOG PB #175]`, `[FIGO 2019 - Preeclampsia Screening]`.
- **Paper**: `Author YYYY (PMID: NNNNNNNN)` + tier note + verified flag.

### Quy tắc số liệu cụ thể (lesson learned 2026-06-19)
- LLM hay **bịa RR/CI/%** khi viết về meta-analysis/clinical trial.
- **BẮT BUỘC** mark `[FULL VERIFIED]` + fetch abstract qua webfetch E-utilities trước khi cite số cụ thể.
- `[ABSTRACT VERIFIED]` chỉ đủ cho direction/qualitative claim.

---

## Workflow bài học (10 bước — XEM WORKFLOW.md để chi tiết)

```
1. PREFLIGHT GUIDELINE CHECK (preflight_guideline_check.py)
2. Tìm PubMed (sort=date) + fetch abstract (webfetch E-utilities)
3. Viết MD có dấu từ đầu (template_lesson.md)
4. Build APKG bằng lesson_builder.add_cards_from_json
5. Citation audit trên file MD (citation_audit.py) — BẮT BUỘC 0 BLOCK
6. Verify dấu MD (verify_diacritics.py) — ratio ≥ 80%
7. Update _README.md
8. Update AGENTS.md nếu có quy ước mới
9. Add journal mới vào journal_quartile.json
10. Add guideline mới vào guideline_versions.json
```

---

## Diacritics governance (CRITICAL — đã có bug nghiêm trọng 22/06)

| Phần | Có dấu? | Lý do |
|---|---|---|
| **Filename + folder** | ❌ KHÔNG | Windows + PowerShell safe |
| **Content trong .md / .apkg** | ✅ **CÓ DẤU ĐẦY ĐỦ** | Bài cho người Việt |
| **Thuật ngữ y khoa / tên riêng** | ❌ Giữ Anh/La-tinh | Doppler, ICSI, FIGO, ASPRE |

**DOCX là định dạng legacy:** `md_to_docx.py` chỉ dùng khi cần rebuild hoặc xuất lại bài cũ; không build DOCX cho bài mới.

**Tooling enforce**:
- `verify_diacritics.py` — scan MD, threshold ≥ 80%.
- `add_diacritics.py` — manual mapping cho từ y khoa (~500 entries).
- **Ambiguous (KHÔNG auto-convert)**: gan, nam, mo, co, benh, huyet, etc.

---

## Quy tắc PowerShell (Windows + PS 5.1)

1. **PowerShell only** — KHÔNG `bash -c "..."` (bash trên Windows = WSL launcher).
2. **File ops**: Dùng `Read/Write/Edit` tools, KHÔNG `Get-Content | Set-Content` (corrupt UTF-8).
3. **Refresh PATH** sau khi cài: `$env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User')`.
4. **Tìm exe**: `where.exe` / `Get-Command` / registry — KHÔNG `Get-ChildItem -Recurse` trên C:.
5. **Dùng `;` hoặc `if ($?)`** — KHÔNG `&&`.
6. **Dùng `Select-Object`, `Select-String`** — KHÔNG `head`, `tail`, `grep`, `wc`.
7. **workdir parameter** thay cho `cd dir && cmd`.

---

## Setup lệch khỏi Mavis (dùng Claude Code thuần)

Nếu muốn dùng Claude Code không qua Mavis:
1. Copy `CONTEXT.md` này → `~/.claude/CLAUDE.md` (global).
2. Trong project `F:\DL\mavisresearch\`, copy `AGENTS.md` (root) + `MEMORY.md` + `SCRIPTS_INDEX.md`.
3. Trong `Bai hoc y khoa/`, copy `.mavis/AGENTS.md` + `WORKFLOW.md` + `template_lesson.md`.
4. Setup MCP `pubmed` trong `~/.claude.json`:
   ```json
   {
     "mcpServers": {
       "pubmed": {
         "command": "python",
         "args": ["C:/Users/THANHANH/.mavis/mcp/pubmed.py"],
         "env": { "NCBI_API_KEY": "e71bce83...63408" }
       }
     }
   }
   ```
5. Đầu session: gõ "đọc AGENTS.md + MEMORY.md + WORKFLOW.md, confirm đã hiểu workflow y khoa".

---

## To clarify next time (open questions về user)

- Chuyên khoa hiện tại + chuyên khoa muốn học sâu (Sản vs Phụ vs Hỗ trợ sinh sản vs Mục tiêu thi).
- Quốc gia/tỉnh thành đang công tác — để biết guideline nào sát thực tế (BV Việt Nam theo BYT, theo ACOG/ASRM, hay theo RCOG/ESHRE).
- Có tài khoản thư viện số ĐH Y / bv không? (nếu có, có thể build tool tải paper từ Fert Steril/Obstet Gynecol qua EZproxy).
- Mức độ sâu của "guideline + cơ chế" — đã ổn chưa hay cần thêm pathway molecular?
