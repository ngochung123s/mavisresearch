# `F:\DL\mavisresearch\` — Workspace root

> **Owner**: Bác sĩ Ngọc Hưng 🍅 🐈‍⬛ (Bác sĩ tự học sản phụ khoa, Việt Nam)
> **AI assistant**: Xác định theo tên model (ban đầu: MiniMax Mavis, hiện tại: opencode deepseek-v4-pro)
> **Cập nhật**: 2026-06-27

---

## Bạn là AI agent? Đọc file nào trước?

| Bạn là... | Đọc file này |
|---|---|
| **Bất kỳ AI agent nào** vào workspace này lần đầu | **`AGENTS.md`** (root context, đọc trước tiên) |
| **Claude Code** specifically | `CLAUDE.md` (slash commands, hooks, MCP tips) |
| Muốn biết user là ai (cross-project context) | `CONTEXT.md` |
| Muốn biết lesson learned + technical notes | `MEMORY.md` |
| Tìm script Python phù hợp | `SCRIPTS_INDEX.md` |
| Làm việc trong `Bai hoc y khoa/` | `Bai hoc y khoa/WORKFLOW.md` + `.mavis/AGENTS.md` |
| Lưu câu hỏi/trả lời y khoa để tra cứu nhanh | `medical_qa/README.md` + `medical_qa/templates/qa_template.md` |

**Đề xuất session start prompt**:
```
"đọc AGENTS.md + MEMORY.md + WORKFLOW.md, confirm đã hiểu workflow y khoa"
```

---

## Cấu trúc workspace

```
F:\DL\mavisresearch\
├── README.md                      ← File này
├── AGENTS.md                      ← Root context (Claude Code / Codex tự đọc)
├── CLAUDE.md                      ← Claude Code-specific tips
├── CONTEXT.md                     ← User profile (copy vào ~/.claude/CLAUDE.md global)
├── MEMORY.md                      ← Lessons learned + technical notes
├── SCRIPTS_INDEX.md               ← Index scripts Python
│
├── Bai hoc y khoa/                ← Daily medical lessons (~19 bài)
│   ├── _README.md
│   ├── WORKFLOW.md
│   ├── template_lesson.md
│   ├── .mavis/AGENTS.md           ← Project-local conventions
│   ├── 01_San phu khoa/
│   ├── 02_Ho tro sinh san ART/
│   ├── 03_Sieu am thai/
│   ├── ...
│   └── 10_Script Python/          ← build_apkg, citation_audit, lesson_builder...
│
├── So lieu thay H/                ← Clinical data dumps
├── daily_lessons/                 ← Notes thô
├── deep_dives/                    ← Research deep-dives
├── papers/                        ← Paper PDFs + PubMed cache
├── notes/                         ← raw + synthesis notes
├── medical_qa/                    ← Medical Q&A tra cứu nhanh dạng Markdown
├── agents/                        ← Mavis agent configs
├── tools/                         ← Custom tools
├── .harness/                      ← Mavis harness (4 agents: researcher, analyst, mechanism, writer)
└── memory_export/                 ← Memory export từ Mavis (cho Codex migration)
    ├── README_CODEX_MIGRATION.md
    ├── user_profile.md
    ├── agent_mavis_MEMORY.md
    └── agent_mavis_MEMORY_raw.md
```

---

## Quy tắc CỨNG

1. ❌ **KHÔNG ghi file vào ổ C:** — workspace là `F:\DL\mavisresearch\` thôi.
2. ✅ Filename KHÔNG dấu, content có dấu đầy đủ.
3. ✅ Mọi bài học y khoa phải citation audit 0 BLOCK.
4. ✅ Đọc `WORKFLOW.md` trước khi viết daily lesson mới.
5. ✅ Câu hỏi y khoa cần lưu nhanh → dùng `medical_qa/`, không cần build DOCX/APKG/HTML.

---

## Medical Q&A

`medical_qa/` là workflow nhẹ để lưu câu hỏi/trả lời y khoa thường gặp:

- Mỗi câu hỏi là một file Markdown riêng trong `medical_qa/by_topic/<topic>/`.
- Tên file/folder không dấu; nội dung tiếng Việt có dấu đầy đủ.
- Câu hỏi case bệnh nhân phải ẩn định danh.
- Số liệu cụ thể hoặc protocol detail phải có nguồn rõ; nếu chưa đủ nguồn thì đánh dấu `Cần kiểm chứng`.
- Khi user nói `lưu vào medical_qa`, tạo file từ template và thêm dòng vào `medical_qa/_INDEX.md`.

---

## Setup nhanh cho Claude Code

```bash
cd F:\DL\mavisresearch
claude
```

Claude Code sẽ tự load `AGENTS.md` (root). Để có context global về user:
```bash
# Windows PowerShell
Copy-Item "F:\DL\mavisresearch\CONTEXT.md" "$env:USERPROFILE\.claude\CLAUDE.md"
```

Để setup MCP `pubmed`:
```json
// File: %USERPROFILE%\.claude.json (hoặc .mcp.json trong project)
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

---

## Sync Google Drive

```powershell
# Sync workspace lên Google Drive
powershell -File "C:\Users\THANHANH\.mavis\scripts\sync_to_gdrive.ps1"
```

---

## Daily cron

| Cron | Mục đích | Schedule |
|---|---|---|
| `daily-lesson-2100` | Tạo daily lesson mới | 21:00 Vietnam time hàng ngày |
| `weekly-papers` | Tìm paper mới + gửi Telegram | Tối T7, 20:00 |
| `session-stall-detector` | Kill session stalled | Mỗi 15 phút |

(Lưu ý: các cron này của Mavis. Claude Code/Codex không có cron built-in — dùng Windows Task Scheduler nếu cần.)

---

## Contact / issues

- Bug trong script → xem `MEMORY.md` mục "Pitfalls đã gặp".
- Workflow không rõ → xem `Bai hoc y khoa/WORKFLOW.md`.
- Cần thêm journal/guideline → edit `Bai hoc y khoa/10_Script Python/journal_quartile.json` hoặc `guideline_versions.json`.
