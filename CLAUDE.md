# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> Mirror của `AGENTS.md` nhưng focus vào commands + architecture + Claude Code-specific tips.
> **Owner**: Bác sĩ Ngọc Hưng 🍅 🐈‍⬛ | **AI assistant**: tên model đang dùng (trước đây MiniMax Mavis)
> **PED:** track Nhi khoa (`Bai hoc y khoa/12_Nhi khoa/`) theo `Bai hoc y khoa/12_Nhi khoa/PED_RULES.md`; phần còn lại của file này canonical cho Sản/ART/Siêu âm/Nội (xem `Bai hoc y khoa/WORKFLOW.md` + `Bai hoc y khoa/AGENTS.md`).
> **Cập nhật**: 2026-06-27

---

## 1. Commands you will use daily

All workflows are Python scripts in `Bai hoc y khoa/10_Script Python/`. **Scripts and output dirs live under `Bai hoc y khoa/`, not at workspace root** — always prefix paths accordingly. There is no `package.json`, `Makefile`, or test suite. For a full catalog of available scripts, see `SCRIPTS_INDEX.md` at workspace root.

### Build a new medical lesson

```bash
# 1. Guideline preflight (mandatory before writing)
python "Bai hoc y khoa/10_Script Python/preflight_guideline_check.py" --topic "X" --guideline "Society YYYY"

# 2. Release runner (gates + APKG + DOCX), offline from evidence bundle
python "Bai hoc y khoa/10_Script Python/build_pipeline.py" --brief <brief.md> --lesson <release.md> --cards <release.cards.v2.json> --guidelines <guideline_evidence.json> --evidence-bundle <bundle.json>

```

### Verify gates (run after every build)

```bash
# Citation audit — MUST exit 0 (0 BLOCK)
python "Bai hoc y khoa/10_Script Python/citation_audit.py" "path.md"

# Diacritics gate — Vietnamese words must be >= 80% diacritic-marked
python "Bai hoc y khoa/10_Script Python/verify_diacritics.py"


# Depth gate — thresholds come from the profile's lesson_depth_contract (foundation >= 5.000, disease/pharmacology >= 6.000 từ; see RESEARCH_BRIEF_TEMPLATE.md)
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
Europe PMC / Crossref / OpenAlex (evidence_sync.py) → offline evidence bundle → lesson MD + cards V2 → build_pipeline.py (gates + APKG + DOCX) → publish_gate.py
```

The canonical source of truth is the **UTF-8 markdown release file inside each lesson folder** (`Bai hoc y khoa/XX_Chuyen_khoa/XX_Ten_bai/`, outputs in its `outputs/`). Cards V2 JSON → APKG via `build_apkg.py`, invoked by the release runner `build_pipeline.py`. `lesson_builder.py` is only a shared Anki model/deck library. `md_to_docx.py` is legacy support for rebuilding or exporting old lessons only. Never hardcode lesson content in build scripts — that was the root cause of the 2026-06-22 diacritics bug.

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

Specific claims (RR, CI, %, n=) require `[DATA VERIFIED]` (exact quote vs abstract/full text), `[FULL TEXT VERIFIED]` or `[GUIDELINE VERIFIED]`. Qualitative direction-only claims can use `[ABSTRACT VERIFIED]`. Canonical 5 labels only; see `Bai hoc y khoa/AGENTS.md`.

---

## 3. Claude Code-specific notes

### PubMed / evidence access

Non-PED release workflow: do NOT call NCBI E-utilities and do not use the buggy MCP `pubmed_fetch`. The only online evidence phase is `Bai hoc y khoa/10_Script Python/evidence_sync.py` (Europe PMC metadata/abstract, Crossref/Retraction Watch, OpenAlex, official manifests); build then runs offline from the bundle via `build_pipeline.py --evidence-bundle`. See `Bai hoc y khoa/AGENTS.md`.

**PED track** follows `Bai hoc y khoa/12_Nhi khoa/PED_RULES.md` (evidence per `medical-verification-governance`, NCBI artifacts allowed there).

For guideline searches, always sort by date, never by relevance.

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
6. Do not cite specific numbers without a verified label (`[DATA VERIFIED]` / `[FULL TEXT VERIFIED]` / `[GUIDELINE VERIFIED]`) backed by `evidence_sync.py` bundle + quote artifact.
6.1. NEVER self-assign verification tags (5 canonical labels: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`). Tags are ONLY permitted after running verification scripts / evidence bundle (`evidence_sync.py` → `build_pipeline.py`). Legacy labels `[FULL VERIFIED]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[TEXTBOOK]` are banned. (PED: labels per `PED_RULES.md` §7.)
- **Markdown Live Preview Rules (MarkdownLivePreview.dev)**:
  - Flowchart: Không dùng Mermaid block. Dùng ` ```text ` hoặc danh sách thụt lề.
   - LaTeX Math: Dùng `$ inline $` và `$$ block $$`. **CẤM gõ ký hiệu `%` hoặc các biểu thức chỉ số phần trăm/bất đẳng thức phần trăm (như `$50% \le \text{FEV1} < 80\%$`) inside inline LaTeX `$ ... $`** vì parser KaTeX/MathJax coi `%` là dấu comment làm ẩn/lỗi mất toàn bộ chữ phía sau. Mọi con số %, khoảng %, bất đẳng thức % (SpO2, FEV1, PaO2) PHẢI viết bằng plain text (vd: `50% ≤ FEV1 < 80%`, `SpO2 < 88%`).
  - Output files: Đưa tất cả sản phẩm phụ xuất bản (.docx, .apkg, .json, brief) vào subfolder `outputs/` thuộc bài học.
  - Mandatory Verification Report: Mọi output xuất bản phải công bố kết quả kiểm tra qua các script verify trong chat (`md_to_docx.py`, `citation_audit.py`, `verify_diacritics.py`).
  - Clinical Case Answers: Always write detailed clinical case solutions directly at the end of the corresponding `.md` Part file and update the `.docx` in `outputs/`.
7. **Medical Flashcard Governance**: Khi thiết kế thẻ Anki, bắt buộc tuân thủ bộ quy tắc trong skill `medical-flashcard-governance`: Kiến trúc thẻ phân tầng từ Tổng quan đến Chi tiết (Thẻ Tầng 1 hỏi khung tổng thể "A gồm những gì/mấy nhóm/các tiêu chuẩn nào", liệt kê đầy đủ danh mục $\rightarrow$ Thẻ Tầng 2 đào sâu chi tiết từng nhánh con, không cắt xén thông tin vì sợ thẻ dài), không lộ tên thuốc/liều đầu tay ở câu dẫn, tất cả cloze dùng `{{c1::...}}`, trường extra không làm lộ đáp án của bậc tiếp theo, phần nguồn/vị trí thông tin tuyệt đối không để ở mặt `Back` (chuyển sang trường `Extra`/`Source`), mặt `Back` giữ nguyên vẹn cấu trúc: `🎯 Trả lời cốt lõi` + `💡 Giải thích của AI` (cơ chế/logic/mẹo nhớ), và 100% dùng ký tự Unicode chuẩn (`→`, `≥`, `≤`, `×`, `µg`, `β`), tuyệt đối không viết mã LaTeX trong thẻ.
7.1. **Nhi khoa (PED)**: rule 7 trên chỉ canonical cho Sản/ART/Nội. Track `Bai hoc y khoa/12_Nhi khoa/PED-xx` theo `Bai hoc y khoa/12_Nhi khoa/PED_RULES.md` (+ 4 managed skill `medical-lesson-release-gates`, `medical-flashcard-governance`, `medical-verification-governance`, `medical-visual-evidence-extraction`): Basic-first, back `🎯`/`💡`, build bằng `ped_deck_builder.py`, APKG/cards ở root folder bài, deck `Nhi khoa Y6::PED-xx: <Tên có dấu>`.
8. **Visual Chat Box Layout**: Định dạng câu trả lời bằng khung viền mở đầu `╭─ 🤖 CLAUDE ──────────────────────────────────────────────` và kết thúc `╰──────────────────────────────────────────────────────────` để phân cách rõ ràng với dòng prompt của người dùng.
