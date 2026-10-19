# PED_RULES — Quy tắc canonical cho track Nhi khoa (PED)

> **Phạm vi:** mọi bài `PED-xx` trong `Bai hoc y khoa/12_Nhi khoa/` (bài giảng Markdown, PEDYTB, thẻ Anki, APKG, PedViewer).
> **Cập nhật:** 2026-10-19.
> Sản phụ khoa / ART / Siêu âm / Nội khoa vẫn theo `Bai hoc y khoa/WORKFLOW.md` + `Bai hoc y khoa/AGENTS.md`.

## 0. Thứ tự ưu tiên & cách đổi rule

1. **Nguồn chân lý nội dung rule PED** = 4 managed skill (đọc trước mỗi phiên PED):
   `medical-lesson-release-gates`, `medical-flashcard-governance`, `medical-verification-governance`, `medical-visual-evidence-extraction`
   (thư mục `C:/Users/THANHANH/.omp/agent/managed-skills/`). File này là bản tóm tắt trong repo để mọi agent (Claude Code, Codex, opencode…) đều thấy cùng một bộ rule.
2. **Nguồn chân lý thực thi** = code: `10_Script Python/ped_card_lint.py` (gate) + `ped_deck_builder.py` (build) + `ped_anki_sync.py` (đồng bộ Anki). Rule nào chưa có code chặn thì ghi rõ "chưa enforce", không được tuyên bố là đã PASS.
3. **Đổi rule (Rule-First):** cập nhật managed skill **và** file này trong cùng một thay đổi; nếu rule có thể kiểm tự động thì thêm check vào `ped_card_lint.py` + regression test `test_ped_card_lint.py` trong **commit riêng**, trước khi rebuild bài nào theo rule mới (không sửa linter để lách gate trong cùng commit release).
4. Khi WORKFLOW.md/AGENTS.md mâu thuẫn với file này trên phạm vi PED → **file này thắng**. Các ngoại lệ PED so với repo canonical:
   - Evidence: theo `medical-verification-governance` (artifact `ncbi_fetch.json` → `abstract_match.jsonl` → `full_verify_table.md` + `outputs/visual_evidence/`).
   - Đường build: `ped_deck_builder.py` (không qua `build_pipeline.py`/`publish_gate.py`; các `gate-results.json` cũ của PED-07/20/32/35/43/48/49 là lịch sử, không còn là điều kiện release).
   - Vị trí APKG/cards: **root folder bài** (PedViewer `build_ped_library.py` bỏ qua `outputs/`).

## 1. Phân luồng kép (Dual-track)

| Track | Nguồn | Yêu cầu | Badge thẻ |
|---|---|---|---|
| **Track 1 — Barem PEDYTB** | Giáo trình Nhi Y Thái Bình (`*_PEDYTB.md`) | 100% Zero-Omission: mọi câu chữ, bảng, con số | `🏛️ BAREM GỐC Y THÁI BÌNH` |
| **Track 2 — EBM Update** | AHA, NICE, AAP, IDSA, WHO, Nelson… | Cờ đỏ, thang điểm, bẫy chẩn đoán, phác đồ an toàn | `🔬 EBM HIỆN ĐẠI & LÂM SÀNG` |

Hai track có thể chung 1 deck (`Nhi khoa Y6::PED-xx: <Tên>`) hoặc tách deck EBM (`Nhi khoa Y6::PED-xx: <Tên> (EBM Update)`).

## 2. Chu trình phát hành 5 bước

```text
1. Soạn MD (RELEASE + PEDYTB) + kiểm duyệt evidence & hình ảnh
2. Viết pedXX_cards_data.py → python "10_Script Python/ped_deck_builder.py" <lesson_dir> --mode release
3. Đồng bộ Anki: thêm --sync-anki (cập nhật tại chỗ, không tạo note trùng)
4. Cập nhật _CURRICULUM_NHI_KHOA.md → python "12_Nhi khoa/build_ped_library.py"
5. Dọn file tạm → git commit (feat/fix(ped): …) → git push origin main (agent tự chạy)
```

Bài chỉ được ghi `✅ GATES ĐẠT` trong curriculum khi bước 2 chạy `--mode release` exit 0 và bước 3 đối soát số note khớp.

## 3. Cấu trúc folder mỗi bài

```text
12_Nhi khoa/<Block>/PED-XX_<Ten_khong_dau>/
├── PED-XX_<Ten>_<YYYY-MM-DD>_RELEASE_vN.md   # bài Track 2 / master (có dấu)
├── PED-XX_<Ten>_PEDYTB.md                    # barem Track 1 (nếu có)
├── pedXX_cards_data.py                       # NGUỒN DUY NHẤT của thẻ (list `cards_data`)
├── ped_deck.json                             # spec deck (code, deck_id, deck_name, basename, sections, models)
├── pedXX_anki_lock.json                      # sinh tự động: GUID + Anki note id cố định cho từng card id
├── <basename>.cards.v2.json                  # sinh tự động (PedViewer đọc)
├── <basename>.apkg                           # sinh tự động — đúng 1 APKG/bài
└── outputs/
    ├── figures/                              # ảnh đã nén (≤150 KB, ≤1200 px)
    ├── visual_evidence/                      # ảnh bằng chứng Gate 2
    └── verification/<basename>/card-lint.json
```

- **Đúng 1 APKG + 1 cards.v2.json ở root.** Bản cũ/trùng chuyển vào `Bai hoc y khoa/_duplicates_review/` (giữ nguyên đường dẫn tương đối), không xóa.
- Không hardcode thẻ trong script build. Script `build_pedXX_master_deck.py` / `rebuild_pedXX.py` riêng từng bài là **legacy**; bài đã chuyển sang `ped_deck_builder.py` thì xóa script cũ.
- Filename/folder không dấu; **nội dung và tên deck có dấu**.

## 4. Schema thẻ (`pedXX_cards_data.py`)

```python
cards_data = [
  {"id": "PED63-B1-01", "type": "basic", "track": "ebm",      # basic | cloze ; barem_goc | ebm
   "section": "B1", "category": "Sinh lý", "tier": 1,          # tier 1 = khung tổng quan, 2 = chi tiết
   "badge": "🔬 EBM HIỆN ĐẠI & LÂM SÀNG", "badge_class": "badge-ebm",
   "front": "…", "back": "<b>🎯 Trả lời cốt lõi:</b><br>…<br><br><b>💡 Giải thích của AI:</b><br>…",
   "extra": "📖 Nguồn: …", "tags": ["PED-63", "EBM"]},
  {"id": "PED63-B4-07", "type": "cloze", "section": "B4", "text": "ANC < {{c1::500/mm³}} là giảm bạch cầu hạt nặng.", "extra": "📖 Nguồn: …"},
]
```

`id` là khóa vĩnh viễn: **không đổi id của thẻ đã phát hành** (đổi id = Anki coi là thẻ mới, mất lịch sử ôn).

## 5. Gate thẻ — ánh xạ rule → linter

`ped_card_lint.py` có 2 mode:
- `release` — mọi gate dưới đây BLOCK. Dùng cho bài mới và bài rebuild.
- `hotfix` — chỉ dùng để vá lỗi kỹ thuật cho bản đã phát hành: nhóm **T** (kỹ thuật) + **P** (back-purity) + **D** (deck) vẫn BLOCK; nhóm **G** (governance) được ghi thành *nợ* (`DEBT`) trong `card-lint.json`. Bản hotfix **không** được nâng trạng thái curriculum lên `✅ GATES ĐẠT` nếu còn DEBT.

| Gate skill | Mã linter | Kiểm tra | Nhóm |
|---|---|---|---|
| 2.9 Escape HTML | `T_ESCAPED_TAG` | Không còn `&lt;b`, `&lt;br`, `&lt;span`… (tag bị escape thành chữ) | T |
| 2.9 Double-escape | `T_DOUBLE_ESCAPE` | Không `&amp;lt;`, `&amp;gt;`, `&amp;amp;`, `<b&gt;` | T |
| 2.9 Ký tự điều khiển | `T_CONTROL_CHAR` | Không `\x08`, `\t`, ký tự C0 | T |
| 2.9 Anti-LaTeX | `T_LATEX` | Không `$`, `\rightarrow`, `\times`, `\ge`, `\text{`…; không `\` đứng trước ký hiệu Unicode (`\→`) | T |
| 2.9 HTML cân bằng | `T_TAG_BALANCE` | Số `<b>`/`</b>`, `<span`/`</span>`, `<div`/`</div>` khớp | T |
| Cấu trúc | `T_EMPTY`, `T_CLOZE_SYNTAX`, `T_DUP_ID`, `T_DUP_FRONT` | Field bắt buộc không rỗng; cloze có `{{cN::…}}` đóng đúng; basic không chứa cloze; id/front không trùng | T |
| 2.7 Back-purity | `P_BACK_SOURCE` | Back/Text không chứa vị trí nguồn: `trang N`, `giáo trình`, `văn bản gốc`, `nguồn:`, `PMID`, `Ch.N`, `mục N` | P |
| 2.3 Zero-omission | `D_SECTION_MISSING` | Mọi `required_sections` có ≥1 thẻ | D |
| Tên deck | `D_DECK_NAME` | `Nhi khoa Y6::PED-xx: <Tên có dấu>` [+ ` (EBM Update)`] | D |
| Media | `D_MEDIA` | Ảnh được tham chiếu phải tồn tại, ≤150 KB, ≤1200 px | D |
| 2.10 Dấu tiếng Việt | `D_DIACRITICS` | `verify_apkg_diacritics.py` ratio ≥ 80% trên APKG đã build | D |
| 2.1 Basic-first | `G_SECTION_NO_BASIC`, `G_CLOZE_ONLY` | Mỗi section có ≥1 thẻ Basic; deck không được 0 Basic | G |
| 2.2 Anti-spoiler | `G_PARTIAL_CLOZE` | Trong 1 câu liệt kê (≥3 phần tử; có `:` dẫn danh mục hoặc mọi phần tử ≤ 8 từ), không được vừa có phần tử bị che vừa có phần tử để trần. Heuristic — cloze che trọn danh mục trong 1 `{{c1::…}}` là hợp lệ | G |
| 2.7 Cấu trúc Back | `G_BACK_STRUCTURE` | Thẻ Basic có `🎯 Trả lời cốt lõi` và `💡 Giải thích của AI` | G |
| 2.7 Nguồn ở Extra | `G_EXTRA_EMPTY` | Mọi thẻ có Extra (`📖 Nguồn: …`) | G |
| 2.6 Màu ngữ nghĩa | `G_COLOR_FRONT`, `G_COLOR_BACK` | Basic có ≥1 màu palette ở Front và ở Back (`#ff6b6b`, `#ffd43b`, `#51cf66`, `#74c0fc`) | G |
| 2.8 Thuật toán | `G_ALGO_COUNT` | ≥3 thẻ badge `⚡ THUẬT TOÁN QUYẾT ĐỊNH` | G |
| 2.4 Phân tầng | `W_TIER` (WARN) | Chưa khai báo `tier` cho thẻ nào → cảnh báo | cảnh báo |
| 2.5 Semantic alignment | — | **Chưa enforce bằng code** — review thủ công khi soạn | — |

Cloze hợp lệ (chỉ là thẻ nhắc phụ): con số/ngưỡng/mốc thời gian, từ khóa định nghĩa 1 mệnh đề, tên hội chứng. Liệt kê thì che **toàn bộ danh mục trong 1 cloze** hoặc chuyển sang Basic.

## 6. Anki — đồng bộ không mất lịch sử

- `ped_deck_builder.py` gán **GUID cố định** theo `pedXX_anki_lock.json` (thẻ mới: `guid_for(code, card_id)`), nên import lại APKG sẽ cập nhật note cũ thay vì sinh note trùng.
- `--sync-anki` (AnkiConnect `127.0.0.1:8765`): cập nhật field tại chỗ cho note đã có (giữ lịch sử ôn), thêm note mới, đổi tên deck về tên chuẩn.
- Note trong deck không còn trong `cards_data` (ví dụ cloze vi phạm anti-spoiler) → **suspend + chuyển sang `Nhi khoa Y6::_Archive::PED-xx`**, gắn tag `ped_archived`. Không xóa note của người học.
- Sau sync: số note trong deck == số thẻ input, nội dung field khớp; lệch là FAIL.

## 7. Bài giảng Markdown & hình ảnh (tóm tắt skill)

- Chuỗi cơ chế dạng blockquote `> 🔄 **Chuỗi cơ chế:** … → …`, 100% Unicode `→ ≥ ≤ ×`, không `$…$`, không `\text{}`, không thụt tab đầu dòng.
- Ảnh: cấm ảnh AI, cấm chọn ảnh theo tên file; CT phải lát cắt Axial/Coronal thật đúng cửa sổ; X-quang tư thế chuẩn; siêu âm B-mode/Doppler thật. Nén qua `fetch_medical_image.py` (≤150 KB, ≤1200 px), đặt `outputs/figures/PEDxx_figN_<ten>.jpg`; trong thẻ dùng `<img src="TEN_FILE">`. Định mức 2–4 ảnh high-yield/bài.
- Nhãn verification theo bảng của `medical-verification-governance`: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[GUIDELINE VERIFIED]`, `[FULL TEXT / VISUAL VERIFIED]` (cách gọi `[FULL VERIFIED]` trong skill là cùng nhãn này). Không artifact → không gán nhãn.

## 8. Lệnh nhanh

```bash
# Lint + build + sync 1 bài
python "Bai hoc y khoa/10_Script Python/ped_deck_builder.py" "Bai hoc y khoa/12_Nhi khoa/<Block>/PED-XX_<Ten>" --mode release --sync-anki
# Lint nhanh toàn bộ APKG hiện có (báo cáo nợ)
python "Bai hoc y khoa/10_Script Python/ped_card_lint.py" --scan-apkg "Bai hoc y khoa/12_Nhi khoa"
# Regression test linter
cd "Bai hoc y khoa/10_Script Python" && python -m unittest test_ped_card_lint -v
```
