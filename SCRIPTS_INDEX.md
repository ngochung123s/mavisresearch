# SCRIPTS_INDEX.md — Index các script Python trong `10_Script Python/`

> **Mục đích**: Index tất cả scripts Python theo **chức năng**, để AI agent (Mavis, Claude Code, Codex...)
> biết dùng cái nào khi nào.
> **Cập nhật**: 2026-06-27
> **Path**: `F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\`

---

## 🟢 CORE — Dùng hàng ngày cho daily lesson

### Build pipeline (2 file chính)

| Script | Mục đích | Cách dùng | Lưu ý |
|---|---|---|---|
| **`lesson_builder.py`** | Shared utilities — ANKI Pastel model | Import trong các script build | Chứa `add_cards_from_json` |
| **`verify_diacritics.py`** | Scan % dấu trong MD files | `python verify_diacritics.py` | Threshold ≥ 80% = PASS. Ratio tính trên từ tiếng Việt (bỏ qua English/numbers) |

`md_to_docx.py` chỉ hỗ trợ rebuild hoặc xuất lại bài cũ; không dùng trong workflow bài mới.

### Audit / verify pipeline

| Script | Mục đích | Cách dùng | Lưu ý |
|---|---|---|---|
| **`citation_audit.py`** | Audit PMID + guideline (Tier 0-4) | `python citation_audit.py path.md` | **BẮT BUỘC 0 BLOCK**. Output report. |
| **`scan_all_lessons.py`** | Scan toàn project, output audit report | `python scan_all_lessons.py` | Output vào `audit_reports/audit_all_lessons_<date>.{md,json}` |
| **`preflight_guideline_check.py`** | Check guideline version trước khi viết | `python preflight_guideline_check.py --topic "X" --guideline "Society YYYY"` | Exit 0/1/2. Exit 2 = BLOCK. |
| **`check_guideline_freshness.py`** | Check version mới hơn cho guideline đang dùng | `python check_guideline_freshness.py` | Output `guideline_freshness_log.json` |
| **`depth_check.py`** | Gate check bài ≥ 8000 từ | `python depth_check.py path.md` | Fail → synthesis-writer phải expand |
| **`daily_lesson_health_check.py`** | Pre-flight check toàn bộ daily lesson | `python daily_lesson_health_check.py` | Tổng hợp tất cả gates |

### Workflow / cron

| Script | Mục đích | Cách dùng | Lưu ý |
|---|---|---|---|
| **`rebuild_all_docx_v2.py`** | Rebuild tất cả 16 DOCX từ MD (chuyển MD có dấu → DOCX có dấu) | `python rebuild_all_docx_v2.py` | Chỉ chạy 1 lần sau khi convert MD sang có dấu |
| **`add_diacritics.py`** | Convert MD không dấu → có dấu (dictionary-based) | Import hoặc chạy trực tiếp | ~80-90% accuracy. KHÔNG dùng cho bài mới. |
| **`apply_diacritics_all.py`** | Wrapper apply `add_diacritics` cho tất cả MD | `python apply_diacritics_all.py` | Batch convert 1 lần |
| **`make_lesson_cited.py`** | Wrapper gọi `citation_audit` cho CI | `python make_lesson_cited.py path.docx` | Exit 0/1 |

### Data files (JSON)

| File | Nội dung | Update khi nào |
|---|---|---|
| **`journal_quartile.json`** | ~120 journal sản phụ khoa mapping Q1-Q4 + aliases PubMed | Khi gặp journal mới |
| **`guideline_registry.json`** | ~30 guideline ASRM/ACOG/RCOG/ESHRE/ISUOG/NICE/FIGO/WHO + supersede tracking | Khi gặp guideline mới |
| **`guideline_versions.json`** | Current version + last_checked + superseded_by chain | Khi verify guideline mới |

---

## 🟡 BUILD-SPECIFIC — Một script cho mỗi bài

Mỗi bài học cũ có thể có scripts APKG/HTML; bài mới chỉ cần APKG. Ví dụ:

| Topic | Scripts |
|---|---|
| LPS (Luteal Phase Support) | `build_lps_apkg.py`, `build_lps_html.py` |
| Stimulation Protocols | `build_stimulation_apkg.py`, `build_stimulation_html.py` |
| Doppler Val Tim Thai | `build_doppler_valtim_apkg.py`, `build_doppler_valtim_html.py` |
| Endometriosis | `build_endo.py`, `endo_content.py` |
| ART Complications | `make_art_complications_lesson.py`, `make_art_complications_html.py` |
| ART Trigger | `make_art_trigger_lesson.py` |
| Oxytocin Induction | `make_oxytocin_induction.py` |
| Oxytocin De chi huy | `build_dechihuy_ovd_apkg.py`, `build_dechihuy_ovd_html.py` |
| Sinh ly chuyen da | `build_sinhlychuenda_apkg.py`, `build_sinhlychuenda_html.py` |
| UXO Tu cung Leiomyoma | `build_uxotucung_leiomyoma_apkg.py`, `build_uxotucung_leiomyoma_html.py` |
| Long GnRH | `make_long_lesson.py` |
| ICSI | `make_icsi_lesson.py` |
| FTS (First Trimester Screening) | `make_fts_lesson.py` |
| PE (Pre-eclampsia) | `make_pe_lesson.py` |
| Doppler (general) | `make_doppler_lesson.py` |
| Gonadotropin | `make_gonadotropin_lesson.py` |
| Hypoplastic | `make_hypoplastic_lesson.py` |
| Echo Word | `make_echo_word.py` |
| Nang Word | `make_nang_word.py` |

**Pattern:**
- `build_<topic>_apkg.py` thường RẤT NGẮN (~1KB) — chỉ import `lesson_builder.add_cards_from_json`.
- `build_<topic>_html.py` là legacy, chỉ dùng để rebuild HTML bài cũ.
- `make_<topic>_lesson.py` (cũ, ~30-50KB) — DEPRECATED, hardcode content.

**Best practice cho bài mới**:
- KHÔNG tạo script `make_*_lesson.py` hoặc `build_<topic>_html.py` riêng.
- Không build DOCX/HTML; `md_to_docx.py` và `md_to_html.py` chỉ dùng khi rebuild hoặc xuất lại bài cũ.
- Dùng `lesson_builder.add_cards_from_json` từ MD + cards.json.
- Lưu mọi deliverable trong folder bài theo chuyên khoa.


---

## 🟡 DEPRECATED — KHÔNG dùng cho bài mới

| Script | Lý do deprecate |
|---|---|
| `make_lesson_docx.py` | Hardcode content không dấu. Dùng `md_to_docx.py` thay. |
| `make_lesson_13_06.py` | Hardcode content cho bài IVF 12/06. Đã fix bằng `md_to_docx.py`. |
| `make_lesson_mcma.py` | Hardcode content cho bài MCMA. Đã fix. |
| `make_echo_word.py` | Build script cũ, hardcode. |
| `make_nang_word.py` | Build script cũ, hardcode. |
| `rebuild_all_docx.py` (v1) | Bị lỗi 1 số case. Dùng `rebuild_all_docx_v2.py`. |
| `make_*_lesson.py` (general) | Tất cả các script `make_<topic>_lesson.py` đều deprecated cho content mới. CHỈ dùng để rebuild cũ. |

---

## 🔵 UTILITIES — Helper scripts

| Script | Mục đích |
|---|---|
| `_build_yhct_v2.py` | Build YHCT (Y học cổ truyền) Anki deck từ cards JSON |
| `_check_sources.py` | Quick check sources trong MD |
| `_dump_groups.py`, `_dump_notes.py`, `_peek_4_thuoc.py` | Anki dump utilities |
| `_inspect_anki.py`, `_verify_apkgs.py` | Anki verification |
| `build_library_dashboard.py` | Build HTML dashboard tổng hợp library |
| `fetch_endo_abstracts.py`, `fetch_endo_direct.py` | PubMed fetch cho bài endometriosis |
| `search_endo_receptivity.py` | PubMed search cho endometrial receptivity |

## 🔎 PubMed / BioMCP quick fetch

Khi cần verify nhanh trong chat hoặc `medical_qa`, ưu tiên PubMed MCP nếu agent expose tool native. Trong OpenCode nếu MCP không mount trực tiếp, dùng BioMCP CLI:

```powershell
biomcp search article --source pubmed -k "craniosynostosis FGFR2" --limit 5
biomcp get article 41268110
```

Fallback khi BioMCP không khả dụng: E-utilities qua `webfetch` (`esearch.fcgi`, `efetch.fcgi`, `esummary.fcgi`).
| `cards_yhct_v2_short.json`, `cards_yhct_reverse.json` | YHCT cards data |

---

## 📁 Cấu trúc output của `citation_audit.py`

```
audit_reports/
├── audit_all_lessons_YYYY-MM-DD.md       ← Markdown report (human-readable)
├── audit_all_lessons_YYYY-MM-DD.json     ← JSON report (machine-readable)
└── unknown_journals_YYYY-MM-DD.txt       ← Unknown journals cần add vào registry
```

---

## 🚀 Quick reference — Flow điển hình

### Tạo daily lesson mới
```bash
# 1. Preflight guideline check
python preflight_guideline_check.py --topic "New topic" --guideline "ESHRE 2024"

# 2. (Manual) Search PubMed qua webfetch, fetch abstracts, viết MD có dấu
# Lưu vào: 09_Source - Markdown/<topic>/<topic>_YYYY-MM-DD.md

# 3. Build APKG
python build_<topic>_apkg.py "09_Source - Markdown/<topic>/<topic>_YYYY-MM-DD.cards.json" "08_Anki Deck - apkg/<topic>.apkg"

# 4. Audit + verify
python citation_audit.py "09_Source - Markdown/<topic>/<topic>_YYYY-MM-DD.md"
python verify_diacritics.py

# 5. Update registry nếu có journal/guideline mới
# Edit journal_quartile.json / guideline_versions.json

# 6. Update _README.md (thêm bài mới vào danh sách)

```

### Audit toàn project
```bash
python scan_all_lessons.py
# Output: 10_Script Python/audit_reports/audit_all_lessons_YYYY-MM-DD.{md,json}
# Xử lý BLOCK + WARN + add unknown journal vào registry
```

### Rebuild DOCX bài cũ (chỉ khi cần)
```bash
python rebuild_all_docx_v2.py
# Chỉ áp dụng cho các bài cũ đã có DOCX
```

---

## ⚠️ Common mistakes khi dùng scripts

| Mistake | Hậu quả | Fix |
|---|---|---|
| Dùng `make_*_lesson.py` cũ cho bài mới | Mất dấu tiếng Việt | Viết MD có dấu; dùng `build_apkg.py` |
| Quên chạy `citation_audit.py` sau build | Có thể có paper sai topic | Audit là bắt buộc trước khi ship |
| Quên verify dấu sau khi build | PowerShell console hiển thị sai → tưởng lỗi | `python verify_diacritics.py` |
| Cần DOCX cho bài cũ | `md_to_docx.py` chỉ dành cho rebuild/xuất lại bài cũ | Không build DOCX cho bài mới |
| Copy bài cũ không dấu làm template | Bài mới viết không dấu theo | Copy từ `template_lesson.md` (có dấu sẵn) |
| Không update `guideline_versions.json` | Có thể dùng guideline cũ | Chạy `preflight_guideline_check.py` trước |

---

## 🔧 Khi muốn tạo script build cho bài mới

Nếu bạn (AI agent) cần tạo script build cho bài mới, pattern đề xuất:

### `build_<topic>_apkg.py` (RẤT NGẮN)
```python
import sys, json
sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')
from lesson_builder import add_cards_from_json

cards_json = sys.argv[1] if len(sys.argv) > 1 else "cards.json"
output_apkg = sys.argv[2] if len(sys.argv) > 2 else "output.apkg"

with open(cards_json, 'r', encoding='utf-8') as f:
    cards = json.load(f)

add_cards_from_json(cards, output_apkg, theme="Pastel")
print(f"✅ Built {output_apkg} ({len(cards)} cards)")
```


---

## 📞 Khi cần help

- Bug trong script → xem `MEMORY.md` mục "Pitfalls đã gặp".
- Workflow không rõ → xem `WORKFLOW.md` ở root.
- Cần thêm script mới → xem pattern ở trên + `lesson_builder.py` source code.
