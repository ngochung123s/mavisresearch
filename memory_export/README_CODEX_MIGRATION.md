# Memory Export - Migrating from Mavis to Codex

Khi rời Mavis (mavis), dùng Codex với API MiniMax, bạn vẫn giữ được toàn bộ memory bằng cách import 2 file này.

## Files trong folder này

| File | Nội dung | Import vào Codex |
|---|---|---|
| `user_profile.md` | Cross-project: bạn là ai, thói quen, tools, workflow y khoa | `~/.codex/AGENTS.md` (global) |
| `agent_mavis_MEMORY.md` (đã clean) | Lesson learned daily lesson, citation audit, workflow Mavis-specific | `F:\DL\mavisresearch\Bai hoc y khoa\AGENTS.md` (project-local, chỉ trong repo y khoa) |
| `agent_mavis_MEMORY_raw.md` | Raw MEMORY.md gốc từ Mavis (giữ nguyên format) | Để tham khảo, không cần import |

## Cách setup Codex với API MiniMax

### 1. Cài Codex CLI
```bash
# Windows (PowerShell 5.1)
irm https://raw.githubusercontent.com/openai/codex/main/scripts/install.ps1 | iex
```

### 2. Set API key MiniMax
Codex mặc định trỏ OpenAI. Để dùng MiniMax API endpoint:
```powershell
$env:OPENAI_API_KEY = "sk-minimax-xxx"
$env:OPENAI_BASE_URL = "https://agent.minimax.io/mavis/api/v1/llm/v1"
# Hoặc edit ~/.codex/config.toml:
#   model = "minimax/MiniMax-M3"
#   api_key = "sk-xxx"
#   base_url = "https://agent.minimax.io/mavis/api/v1/llm/v1"
```

### 3. Copy memory files vào đúng vị trí

**User-level (global, bạn dùng cho mọi project):**
```powershell
Copy-Item "F:\DL\mavisresearch\memory_export\user_profile.md" "$env:USERPROFILE\.codex\AGENTS.md"
```

**Project-level (chỉ trong folder y khoa):**
```powershell
Copy-Item "F:\DL\mavisresearch\memory_export\agent_mavis_MEMORY.md" "F:\DL\mavisresearch\Bai hoc y khoa\AGENTS.md"
```

Codex đọc `AGENTS.md` ở root project + parent directories. Khi bạn `cd F:\DL\mavisresearch\Bai hoc y khoa\` rồi chạy codex, nó sẽ tự load file đó.

### 4. Trong session Codex, gõ:
```
"đọc AGENTS.md và confirm đã hiểu workflow y khoa + lesson format"
```

## Lưu ý quan trọng

1. **Citation audit scripts KHÔNG tự động migrate** — bạn phải tự copy folder `10_Script Python\` (đã có journal_quartile.json, citation_audit.py, verify_diacritics.py, v.v.) sang repo mới nếu muốn tiếp tục dùng.

2. **MCP `pubmed`** (cài tại `C:\Users\THANHANH\.mavis\mcp\pubmed.py`) — Codex có hệ MCP riêng (`~/.codex/mcp.json`). Convert tương tự:
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
   Lưu vào `~/.codex/mcp.json`.

3. **Daily cron `daily-lesson-2100`** — Codex không có cron built-in như Mavis. Workaround:
   - Windows Task Scheduler chạy `codex` CLI lúc 21:00
   - Hoặc dùng `cron` package trong Node script wrapper
   - Hoặc tự run thủ công (ít tin cậy hơn)

4. **Workspace `F:\DL\mavisresearch\Bai hoc y khoa\`** — folder này thuộc về bạn, KHÔNG phải của Mavis. Mang sang máy nào cũng được, sync Google Drive như cũ.

5. **Sessions history** — Mavis giữ ở `C:\Users\THANHANH\.mavis\sessions\`. Codex lưu ở `~/.codex/sessions/` hoặc tương tự. KHÔNG tự động migrate. Nếu cần lịch sử, copy thủ công trước khi gỡ Mavis.

## Format tương thích

Mavis memory dùng format:
```markdown
### Topic (date)
Type: technical
content...
```

Codex `AGENTS.md` chấp nhận Markdown tự do. Chỉ cần giữ heading + bullet là Codex hiểu. Không cần convert cú pháp.

Đã verify: Mavis user_profile.md và agent_mavis_MEMORY.md có thể dùng nguyên văn cho Codex `AGENTS.md` mà không cần sửa.
