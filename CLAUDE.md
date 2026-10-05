# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> Mirror của `AGENTS.md` nhưng focus vào commands + architecture + Claude Code-specific tips.
> **Owner**: Bác sĩ Ngọc Hưng 🍅 🐈‍⬛ | **AI assistant**: tên model đang dùng (trước đây MiniMax Mavis)
> **Cập nhật**: 2026-06-27

---

## 1. Commands you will use daily

All workflows are Python scripts in `Bai hoc y khoa/10_Script Python/`. **Scripts and output dirs live under `Bai hoc y khoa/`, not at workspace root** — always prefix paths accordingly. There is no `package.json`, `Makefile`, or test suite. For a full catalog of available scripts, see `SCRIPTS_INDEX.md` at workspace root.

### Build a new medical lesson

```bash
# 1. Guideline preflight (mandatory before writing)
python "Bai hoc y khoa/10_Script Python/preflight_guideline_check.py" --topic "X" --guideline "Society YYYY"

# 2. Build Anki deck
python "Bai hoc y khoa/10_Script Python/build_<topic>_apkg.py" "Bai hoc y khoa/09_Source - Markdown/<topic>/<topic>_YYYY-MM-DD.cards.json" "Bai hoc y khoa/08_Anki Deck - apkg/<topic>.apkg"

```

### Verify gates (run after every build)

```bash
# Citation audit — MUST exit 0 (0 BLOCK)
python "Bai hoc y khoa/10_Script Python/citation_audit.py" "path.md"

# Diacritics gate — Vietnamese words must be >= 80% diacritic-marked
python "Bai hoc y khoa/10_Script Python/verify_diacritics.py"


# Depth gate — lesson must be >= 8000 words
python "Bai hoc y khoa/10_Script Python/depth_check.py" "path.md"

# Post-build health check (all gates + deliverables)
python "Bai hoc y khoa/10_Script Python/daily_lesson_health_check.py" --since-min 60
```

### Project-wide maintenance

```bash
# Audit every lesson
python "Bai hoc y khoa/10_Script Python/scan_all_lessons.py"

# Check guideline versions for updates
python "Bai hoc y khoa/10_Script Python/check_guideline_freshness.py"

# Rebuild all DOCX from MD (only when template changes)
python "Bai hoc y khoa/10_Script Python/rebuild_all_docx_v2.py"
```

---

## 2. High-level architecture

### Repository layout

`F:\DL\mavisresearch\` is a personal medical-research workspace. The primary product is `Bai hoc y khoa/` — daily OB/GYN lessons published as `.md` and `.apkg`.

| Sub-project | Purpose |
|---|---|
| `Bai hoc y khoa/` | Main daily-lesson pipeline |
| `So lieu thay H/` | Clinical reference data |
| `daily_lessons/`, `deep_dives/`, `papers/`, `notes/` | Raw knowledge base |
| `.harness/` | Mavis 4-agent harness config (researcher, guideline-analyst, mechanism-reviewer, synthesis-writer) |
| `memory_export/` | Mavis → Claude/Codex migration artifacts |

### Daily lesson build pipeline

```
PubMed E-utilities (webfetch) → MD source → APKG → audit gates → publish
```

The canonical source of truth is the **UTF-8 markdown file** in `09_Source - Markdown/`. APKG is produced through `lesson_builder.py`. `md_to_docx.py` is legacy support for rebuilding or exporting old lessons only. Never hardcode lesson content in build scripts — that was the root cause of the 2026-06-22 diacritics bug.

### Key scripts and their roles

| Script | Role |
|---|---|
| `md_to_docx.py` | Legacy markdown → DOCX parser for rebuilding or exporting old lessons only |
| `lesson_builder.py` | Shared library: Anki Pastel model/deck factory |
| `citation_audit.py` | Verifies PMIDs, assigns citation tiers (0–5), enforces hybrid strictness, produces BLOCK/WARN report |
| `verify_diacritics.py` | Computes diacritic ratio on Vietnamese words only; threshold >= 80% |
| `journal_quartile.json` | ~120 journal → Q1/Q2/Q3/Q4 mapping with PubMed aliases |
| `guideline_versions.json` | Current guideline versions, supersede chains, last-checked dates |

### Multi-agent harness

`.harness/reins/` defines four specialist agents whose outputs feed into `deep_dives/<topic>/`:

- `medical-researcher` → `clinical-evidence.md`
- `guideline-analyst` → `guideline-review.md`
- `mechanism-reviewer` → `mechanism-review.md`
- `medical-synthesis-writer` → `final-report.md`

### Citation tier system

- Tier 0: Official guidelines (ESHRE, ACOG, RCOG, ASRM, ISUOG, NICE, FIGO, ISSHP, WHO)
- Tier 1–2: Q1–Q2 journals
- Tier 3: Unknown journals (default)
- Tier 4: Q4_AVOID journals → BLOCK for specific claims
- Tier 5: PMID not found → BLOCK

Specific claims (RR, CI, %, n=) from Tier 1/2 require `[FULL VERIFIED]` from the actual abstract. Direction-only claims can use `[ABSTRACT VERIFIED]`.

---

## 3. Claude Code-specific notes

### PubMed access

The MCP `pubmed_fetch` endpoint is buggy and returns empty. Always use `webfetch` against NCBI E-utilities directly:

```text
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=QUERY&retmax=20&sort=date&reldate=1825&datetype=pdat&retmode=json&api_key=...
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=PMID&retmode=xml&api_key=...
```

For guideline searches, always use `sort=date`, never `sort=relevance`.

### Windows / PowerShell pitfalls

- This project uses **PowerShell 5.1**, not bash. Do not use `&&` chains; use `;` or `if ($?) { ... }`.
- Do not use `head`, `tail`, `grep`, `wc` — use `Select-Object`, `Select-String`.
- Do not use `Get-Content | Set-Content` for UTF-8 files (corrupts encoding). Use Claude Code `Read/Write/Edit` tools instead.
- The console may render Vietnamese diacritics as `?`. Verify with `python -c "print(open(f,encoding='utf-8').read())"`.

### Recommended session start prompt

```
"đọc AGENTS.md + MEMORY.md + WORKFLOW.md, confirm đã hiểu workflow y khoa"
```

### Files to read before acting

| Task | Read |
|---|---|
| Understand user + workspace | `AGENTS.md` |
| Write a new lesson | `Bai hoc y khoa/WORKFLOW.md` + `template_lesson.md` |
| Audit citations | `MEMORY.md` (Citation audit workflow) |
| Add journal/guideline | `journal_quartile.json` / `guideline_versions.json` |
| Diacritics issue | `MEMORY.md` (Vietnamese diacritics governance) |

### Hard rules

1. Never write files to `C:\` — workspace is `F:\DL\mavisresearch\` only.
2. Filenames/folders: NO Vietnamese diacritics. Content in `.md/.apkg`: FULL diacritics required.
3. Every medical lesson must pass citation audit with **0 BLOCK**.
4. Read `Bai hoc y khoa/WORKFLOW.md` before writing a new daily lesson.
5. Automatically build styled `.docx` for all markdown lessons/parts and save them into the `outputs/` subfolder.
6. Do not cite specific numbers without `[FULL VERIFIED]` from a fetched abstract.
6.1. NEVER self-assign verification tags ([FULL VERIFIED], [ABSTRACT VERIFIED], [GUIDELINE VERIFIED]) based on speculation. Tags are ONLY permitted after running verification scripts or directly fetching/confirming from NCBI/BioMCP APIs.
- **Markdown Live Preview Rules (MarkdownLivePreview.dev)**:
  - Flowchart: Không dùng Mermaid block. Dùng ` ```text ` hoặc danh sách thụt lề.
   - LaTeX Math: Dùng `$ inline $` và `$$ block $$`. **CẤM gõ ký hiệu `%` hoặc các biểu thức chỉ số phần trăm/bất đẳng thức phần trăm (như `$50% \le \text{FEV1} < 80\%$`) inside inline LaTeX `$ ... $`** vì parser KaTeX/MathJax coi `%` là dấu comment làm ẩn/lỗi mất toàn bộ chữ phía sau. Mọi con số %, khoảng %, bất đẳng thức % (SpO2, FEV1, PaO2) PHẢI viết bằng plain text (vd: `50% ≤ FEV1 < 80%`, `SpO2 < 88%`).
  - Output files: Đưa tất cả sản phẩm phụ xuất bản (.docx, .apkg, .json, brief) vào subfolder `outputs/` thuộc bài học.
  - Mandatory Verification Report: Mọi output xuất bản phải công bố kết quả kiểm tra qua các script verify trong chat (`md_to_docx.py`, `citation_audit.py`, `verify_diacritics.py`).
  - Clinical Case Answers: Always write detailed clinical case solutions directly at the end of the corresponding `.md` Part file and update the `.docx` in `outputs/`.
7. **Medical Flashcard Governance**: Khi thiết kế thẻ Anki, bắt buộc tuân thủ bộ quy tắc trong skill `medical-flashcard-governance`: không lộ tên thuốc/liều đầu tay ở câu dẫn, tất cả cloze dùng `{{c1::...}}`, trường extra không làm lộ đáp án của bậc tiếp theo, phần nguồn/vị trí thông tin tuyệt đối không để ở mặt `Back` (chuyển sang trường `Extra`/`Source`), mặt `Back` giữ nguyên vẹn cấu trúc: `🎯 Trả lời cốt lõi` + `💡 Giải thích của AI` (cơ chế/logic/mẹo nhớ), và 100% dùng ký tự Unicode chuẩn (`→`, `≥`, `≤`, `×`, `µg`, `β`), tuyệt đối không viết mã LaTeX trong thẻ.
8. **Visual Chat Box Layout**: Định dạng câu trả lời bằng khung viền mở đầu `╭─ 🤖 CLAUDE ──────────────────────────────────────────────` và kết thúc `╰──────────────────────────────────────────────────────────` để phân cách rõ ràng với dòng prompt của người dùng.
