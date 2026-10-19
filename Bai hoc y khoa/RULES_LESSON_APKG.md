# RULES_LESSON_APKG — Quy tắc build BÀI HỌC + APKG cho MỌI chuyên khoa

> **Phạm vi:** mọi bài trong `Bai hoc y khoa/` — Nhi khoa, Nội khoa, Sản phụ khoa, ART, Siêu âm thai, Siêu âm tổng quát, Vi sinh – Miễn dịch.
> **Cập nhật:** 2026-10-19. File này thay cho `12_Nhi khoa/PED_RULES.md` (đã gộp vào đây).
> **Chính sách áp dụng:** bài **mới** hoặc **viết lại** phải qua `release_lesson.py --mode release` (mọi gate chặn). Bài **cũ** không bị chặn: lỗi được ghi vào sổ nợ `_DEBT_LEDGER.md` và sửa dần.

## 0. Thứ tự ưu tiên & cách đổi rule

1. **Nội dung rule:** 4 managed skill `medical-lesson-release-gates`, `medical-flashcard-governance`, `medical-verification-governance`, `medical-visual-evidence-extraction` (thư mục `C:/Users/THANHANH/.omp/agent/managed-skills/`) + file này. File này là bản trong repo để mọi agent đều thấy cùng một bộ rule.
2. **Thực thi:** code trong `10_Script Python/`. Rule chưa có code chặn thì ghi rõ "chưa enforce"; không được tuyên bố PASS bằng lời.
3. **Đổi rule (Rule-First):** sửa managed skill + file này trong cùng một thay đổi. Rule kiểm được tự động → thêm check + regression test trong **commit riêng** trước khi build bài theo rule mới. Cấm sửa linter/verifier để lách gate trong commit phát hành.
4. `WORKFLOW.md`, `AGENTS.md`, `CLAUDE.md` mô tả pha **evidence** (Research Brief, `evidence_sync.py`, 7 gate nguồn) cho chuyên khoa `evidence_bundle`. Phần build bài + thẻ + APKG + Anki của mọi chuyên khoa theo file này.

## 1. Registry chuyên khoa — `10_Script Python/specialties.json`

| Chuyên khoa | Folder | Mã bài | Gốc deck Anki | Evidence | Nơi đặt APKG |
|---|---|---|---|---|---|
| Nhi khoa | `12_Nhi khoa` | `PED-xx` | `Nhi khoa Y6` | `ncbi_artifacts` | root folder bài (PedViewer đọc) |
| Nội khoa | `11_Noi khoa` | `IM-xx` | `1. Y Khoa - Nội Khoa & Cấp Cứu` | `evidence_bundle` | `outputs/` |
| Sản phụ khoa | `01_San phu khoa` | `OB-<số folder>` | `2. Y Khoa - Sản Phụ Khoa & ART` | `evidence_bundle` | `outputs/` |
| ART | `02_Ho tro sinh san ART` | `ART-<số folder>` | `2. Y Khoa - Sản Phụ Khoa & ART` | `evidence_bundle` | `outputs/` |
| Siêu âm thai | `03_Sieu am thai` | `FUS-<số folder>` | `2. Y Khoa - Sản Phụ Khoa & ART` | `evidence_bundle` | `outputs/` |
| Siêu âm tổng quát | `04_Sieu am tong quat` | `US-<số folder>` | `Imaging` | `evidence_bundle` | `outputs/` |
| Vi sinh – Miễn dịch | `05_Vi sinh - Mien dich` | `MIC-<số>` (`V4_` → `MIC-4`) | `2. Y Khoa - Sản Phụ Khoa & ART` | `evidence_bundle` | `outputs/` |

- **Tên deck:** `<Gốc deck>::[<Nhóm>::]<Mã bài>[:] <Tên bài có dấu>` (+ ` (EBM Update)` cho deck EBM tách riêng). Ví dụ:
  - `Nhi khoa Y6::PED-63: Biến thiên công thức bạch cầu theo tuổi`
  - `1. Y Khoa - Nội Khoa & Cấp Cứu::02. Tim Mạch::IM-22 Suy tim`
  - `2. Y Khoa - Sản Phụ Khoa & ART::Hỗ Trợ Sinh Sản (ART)::ART-44 Phân tích tinh dịch đồ`
- Thêm chuyên khoa mới = thêm 1 mục vào `specialties.json` (không sửa code).
- Hai chế độ evidence:
  - `ncbi_artifacts`: artifact `ncbi_fetch.json` → `abstract_match.jsonl` → `full_verify_table.md` (+ `guideline_evidence.json`, `outputs/visual_evidence/`) theo skill `medical-verification-governance`. `lesson_lint` đối chiếu từng nhãn với artifact.
  - `evidence_bundle`: `evidence_sync.py` → Research Brief → `build_pipeline.py --evidence-bundle` (offline, 16 gate, `publish_gate.py`) theo `WORKFLOW.md`.

## 2. Chu trình phát hành — MỘT lệnh

```text
1. Research Brief + nguồn  →  2. Soạn bài .md + nguồn thẻ  →  3. lesson.json
→ 4. python "10_Script Python/release_lesson.py" <lesson_dir> --mode release --sync-anki [--evidence-bundle B --guidelines G]
     manifest → lesson_lint → (evidence_bundle: build_pipeline) → deck_builder (card_lint + APKG + verify + Anki) → post_release
→ 5. cập nhật dòng trạng thái trong curriculum của chuyên khoa → dọn file tạm → git commit + push origin main (agent tự chạy)
```

- Kết quả từng bước: `outputs/verification/<basename>/` gồm `release.json`, `lesson-lint.json`, `card-lint.json` (+ `gate-results.json` nếu `evidence_bundle`).
- Chỉ ghi `✅ GATES ĐẠT` trong curriculum khi `release.json` có `status = PUBLISH_READY`.
- `--mode hotfix` chỉ để **vá bài cũ**: lỗi bài + lỗi quy chuẩn thẻ ghi thành nợ, chỉ chặn lỗi kỹ thuật của thẻ; không chạy `build_pipeline`; không được nâng trạng thái lên `✅ GATES ĐẠT`.
- `post_release` của chuyên khoa chạy tự động (Nhi khoa: `12_Nhi khoa/build_unified_med_library.py` → web HungMed `data.js` gồm **cả Nhi + Sản khoa**, `CATALOG_PED_VIEWER.json`, `checklist.html`, số `?v=` trong app/mobile/checklist). Builder dừng (BLOCK) nếu thiếu nguồn Sản khoa; push `main` = Cloudflare Pages `dvnhmed` deploy ngay.

## 3. Cấu trúc folder bài & `lesson.json`

```text
<Chuyên khoa>/<Nhóm>/<MÃ>_<Ten_khong_dau>/
├── lesson.json                                  # manifest duy nhất của bài
├── <MÃ>_<Ten>_<YYYY-MM-DD>_RELEASE_vN.md        # bài học (có dấu)
├── <MÃ>_RESEARCH_BRIEF.md                       # brief + contract `## 0. Lesson profile & release contract`
├── <MÃ>_<Ten>_PEDYTB.md                         # barem Track 1 (Nhi khoa, nếu có)
├── <ma>_cards_data.py  hoặc  <basename>.cards.v2.json   # NGUỒN DUY NHẤT của thẻ
├── anki_lock.json                               # tự sinh: GUID + note id cố định theo card id
└── outputs/  (figures/, visual_evidence/, verification/<basename>/, APKG/DOCX của chuyên khoa evidence_bundle)
```

```json
{
  "id": "PED-13", "specialty": "nhi", "profile": "foundation",
  "lesson": "PED-13_Suy_ho_hap_so_sinh_va_Lieu_phap_Surfactant_2026-09-15_RELEASE_v1.md",
  "brief": "PED-13_RESEARCH_BRIEF.md",
  "deck": {"deck_id": 4631985485563, "deck_name": "Nhi khoa Y6::PED-13: Suy hô hấp sơ sinh & Chỉ định Surfactant",
           "basename": "PED-13_Suy_ho_hap_so_sinh_va_Lieu_phap_Surfactant_MASTER_v2",
           "required_sections": ["B0", "B1"], "cards_source": "ped13_cards_data.py"}
}
```

- `profile` ∈ `disease | foundation | pharmacology`, phải trùng contract trong brief.
- `evidence_bundle`: `deck.basename` phải trùng tên file bài (vì `build_pipeline` đặt APKG theo `lesson.stem`).
- Tùy chọn: `barem`, `deck.legacy_anki_decks` (tên deck cũ cần gom về), `deck.media_dir` (mặc định `outputs/figures`).
- Mỗi bài đúng **1 APKG + 1 cards.v2.json**; bản cũ/trùng chuyển vào `Bai hoc y khoa/_duplicates_review/` (giữ đường dẫn tương đối), không xóa. Không viết script build riêng từng bài.
- Filename/folder không dấu; nội dung và tên deck có dấu.

## 4. Rule bài học `.md` — `lesson_lint.py`

Chế độ đọc duy nhất `L3_BEGINNER`. Khung bài theo `template_lesson.md`. Bài phải dạy từ gốc theo chuỗi **cơ chế phân tử → tế bào → mô/cơ quan → lâm sàng → cận lâm sàng → chẩn đoán → điều trị**, kèm hướng dẫn cầm tay chỉ việc (mục tiêu → khi nào làm → chuẩn bị → cách làm/đọc → thay đổi quyết định → bẫy/an toàn → chuyển tuyến).

| Nhóm | Mã | Kiểm tra |
|---|---|---|
| Manifest | `M_MANIFEST`, `M_FILENAME`, `M_PROFILE` | `lesson.json` hợp lệ; mã bài khớp folder + registry; tên file `<MÃ>_<Ten>_YYYY-MM-DD_RELEASE_vN.md`; profile = contract của brief |
| Cấu trúc & độ sâu | `S_DEPTH` | Toàn bộ gate chặn của `depth_check.py` theo profile (một engine duy nhất): mục bắt buộc theo profile, Box đỏ, nền tảng tối thiểu, lưu đồ (```text/```mermaid/cây ASCII), ca lâm sàng có lời giải, ≥ số từ tối thiểu (foundation 5.000, disease/pharmacology 6.000), chuỗi cơ chế, ví dụ, bẫy, checkpoint, tips, dấu tiếng Việt ≥ 80%, không placeholder, không padding |
| Định dạng | `F_TAB_INDENT`, `F_INDENTED_CODE`, `F_LATEX`, `F_CONTROL_CHAR` | Ngoài code fence: không Tab đầu dòng, không đoạn thụt ≥4 dấu cách sau dòng trống (marked.js biến thành code block), không `$…$`/`$$`/`\text{}`/`\rightarrow`/tàn dư `ightarrow`, không ký tự điều khiển. 100% Unicode `→ ≥ ≤ ×` |
| Chuỗi cơ chế | `C_CHAIN_FORMAT` | ≥ `min_mechanism_chains` của profile (3/4/5) chuỗi dạng blockquote `> 🔄 **Chuỗi cơ chế:** A → B → C …` |
| Ảnh | `I_REMOTE`, `I_PATH`, `I_ALT`, `I_NAME`, `I_MISSING`, `I_SIZE`, `I_COUNT` | Ảnh local trong `outputs/figures/`, có alt, tên `<MÃ không gạch>_figN_<ten>.jpg`, ≤150 KB, ≤1200 px, ≤4 ảnh/bài. Cấm ảnh AI; CT lát cắt Axial/Coronal thật đúng cửa sổ; X-quang tư thế chuẩn; siêu âm 2D/Doppler thật có thang đo (kiểm duyệt bằng mắt — chưa enforce bằng code) |
| Nhãn verification | `V_BANNED_LABEL`, `V_UNKNOWN_LABEL` | Chỉ `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[GUIDELINE VERIFIED]`, `[FULL TEXT VERIFIED]`, `[FULL TEXT / VISUAL VERIFIED]`. Cấm `[FULL VERIFIED]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[TEXTBOOK]`, `[PMC VERIFIED]`. Kiến thức nền không gắn nhãn |
| Nhãn ↔ artifact (`ncbi_artifacts`) | `V_NO_PMID`, `V_NOT_FETCHED`, `V_NO_ABSTRACT_MATCH`, `V_NOT_GUIDELINE`, `V_NO_FULL_VERIFY` | Mỗi dòng có nhãn phải có PMID (guideline không PMID: có mục trong `guideline_evidence.json`); PMID có trong `ncbi_fetch.json`; `[ABSTRACT/GUIDELINE VERIFIED]` có dòng match trong `abstract_match.jsonl`; `[GUIDELINE VERIFIED]` có pubtype Guideline/Consensus; `[DATA/FULL TEXT VERIFIED]` có trong `full_verify_table.md` |
| Nhãn ↔ claim (`evidence_bundle`) | gate của `build_pipeline.py` | `brief_pmid_preflight`, `brief_claims_strict`, `source_claims_strict`, `guideline_evidence(_crosscheck)`, `citation_zero_block`, `source_retraction`… (xem `WORKFLOW.md`) |

Chưa enforce bằng code: chất lượng y khoa của nội dung, chọn ảnh đúng bản chất lâm sàng, độ chính xác số liệu ngoài phạm vi claim có nhãn → soát tay khi review.

## 5. Rule thẻ — `card_lint.py`

Mặt sau Basic: `<b>🎯 Trả lời cốt lõi:</b><br>…<br><br><b>💡 Giải thích của AI:</b><br>…`. Nguồn chỉ ở `Extra` (`📖 Nguồn: …`). Màu: 🔴 `#ff6b6b` cờ đỏ/triệu chứng, 🟡 `#ffd43b` con số/tuổi/âm tính, 🟢 `#51cf66` xử trí/thuốc, 🔵 `#74c0fc` tên bệnh/giải phẫu/phân loại. Basic-first: mọi danh mục có thẻ Basic nền tảng; cloze chỉ nhắc phụ cho con số/ngưỡng, từ khóa định nghĩa 1 mệnh đề, tên hội chứng; liệt kê thì che trọn danh mục trong 1 cloze hoặc dùng Basic. 3–5 thẻ `⚡ THUẬT TOÁN QUYẾT ĐỊNH`.

| Gate skill | Mã linter | Kiểm tra | Nhóm |
|---|---|---|---|
| 2.9 Escape HTML | `T_ESCAPED_TAG` | Không còn `&lt;b`, `&lt;br`, `&lt;span`… | T |
| 2.9 Double-escape | `T_DOUBLE_ESCAPE` | Không `&amp;lt;`, `&amp;gt;`, `<b&gt;` | T |
| 2.9 Ký tự điều khiển | `T_CONTROL_CHAR` | Không `\x08`, `\t`, `\r` (tàn dư `\rightarrow` trong string thường), ký tự C0 | T |
| 2.9 Anti-LaTeX | `T_LATEX` | Không `$`, `\rightarrow`, `\times`, `\text{`, tàn dư `ightarrow`/`ext{`, `\` trước ký hiệu Unicode (`\→`) | T |
| 2.9 HTML cân bằng | `T_TAG_BALANCE` | `<b>`/`<span>`/`<div>` mở-đóng khớp | T |
| Cấu trúc | `T_EMPTY`, `T_CLOZE_SYNTAX`, `T_DUP_ID`, `T_DUP_FRONT` | Field bắt buộc; cloze đúng cú pháp; basic không chứa cloze; id/front không trùng | T |
| 2.7 Back-purity | `P_BACK_SOURCE` | Back/Text không chứa `trang N`, `giáo trình`, `văn bản gốc`, `nguồn:`, `PMID`, `Ch.N`, `mục N` | P |
| 2.3 Zero-omission | `D_SECTION_MISSING` | Mọi `required_sections` có ≥1 thẻ | D |
| Tên deck | `D_DECK_NAME` | Theo §1 (gốc deck của chuyên khoa, mã bài khớp manifest, tên có dấu) | D |
| Media | `D_MEDIA` | Ảnh trong thẻ tồn tại, ≤150 KB, ≤1200 px | D |
| 2.10 Dấu tiếng Việt | `D_DIACRITICS` | APKG ratio ≥ 80% | D |
| 2.1 Basic-first | `G_SECTION_NO_BASIC`, `G_CLOZE_ONLY` | Mỗi section có Basic; deck không 0 Basic | G |
| 2.2 Anti-spoiler | `G_PARTIAL_CLOZE` | Heuristic: câu liệt kê ≥3 phần tử không được vừa che vừa để trần | G |
| 2.7 Cấu trúc Back | `G_BACK_STRUCTURE`, `G_EXTRA_EMPTY` | Basic có 🎯 + 💡; mọi thẻ có Extra | G |
| 2.6 Màu | `G_COLOR_FRONT`, `G_COLOR_BACK` | Basic có màu palette ở Front và Back | G |
| 2.8 Thuật toán | `G_ALGO_COUNT` | ≥3 thẻ `⚡ THUẬT TOÁN QUYẾT ĐỊNH` | G |
| 2.4 Phân tầng | `W_TIER` | cảnh báo nếu không thẻ nào khai báo `tier` | W |
| 2.5 Semantic alignment | — | chưa enforce bằng code — soát tay | — |

Mode `release`: T/P/D/G đều BLOCK. Mode `hotfix`: T/P/D BLOCK, G thành DEBT.

Schema 1 thẻ: `{"id", "type": "basic|cloze", "section", "category", "tier", "track": "barem_goc|ebm", "badge", "badge_class", "front", "back" | "text", "extra", "tags"}`. **Không đổi `id` của thẻ đã phát hành** (đổi id = thẻ mới, mất lịch sử ôn). Notetype mặc định `YKhoa_Master_Basic` / `YKhoa_Master_Cloze`; chuyên khoa đã có deck trong Anki khai báo notetype riêng trong `specialties.json` → `models` (Nhi khoa giữ `NhiKhoa_Master_*` — **không đổi id/tên/template**, vì đổi thì import APKG sẽ bỏ qua note cùng GUID).

## 6. Anki — `anki_sync.py` (qua `--sync-anki`)

- GUID cố định theo `anki_lock.json` → import lại APKG cập nhật note cũ, không nhân đôi.
- Note đã có: cập nhật field tại chỗ (giữ lịch sử ôn, giữ notetype cũ). Thẻ mới: thêm note.
- Note trong deck không còn trong nguồn thẻ → suspend + chuyển sang `<Gốc deck>::_Archive::<Mã bài>`, tag `lesson_archived`. **Không xóa note của người học.**
- Sau sync: số note trong deck == số thẻ, field khớp; lệch là BLOCK. AnkiConnect chậm → chạy các bài **tuần tự**; chạy lại an toàn (ghép lại note theo nội dung).

## 7. Lệnh nhanh

```bash
cd "Bai hoc y khoa/10_Script Python"
python release_lesson.py "<lesson_dir>" --mode release --sync-anki                    # Nhi khoa
python release_lesson.py "<lesson_dir>" --mode release --sync-anki --evidence-bundle B.json --guidelines G.json   # chuyên khoa evidence_bundle
python lesson_lint.py "<lesson_dir>" --mode release                                   # chỉ kiểm bài .md
python deck_builder.py "<lesson_dir>" --mode release --lint-only                      # chỉ kiểm thẻ
python debt_ledger.py                                                                  # sinh lại _DEBT_LEDGER.md
python -m unittest discover -s . -p "test_*.py"                                       # regression
```

## 8. Bài cũ — sổ nợ

- `_DEBT_LEDGER.md` (tự sinh, không sửa tay): mỗi bài/APKG của mọi chuyên khoa với nợ bài (M/S/F/C/I/V) và nợ thẻ (T/P/D/G).
- Bài cũ chưa có `lesson.json` được quét với profile giả định `disease`.
- Nâng cấp một bài cũ = tạo `lesson.json` + sửa bài/thẻ → `release_lesson.py --mode release` đạt `PUBLISH_READY` → chạy lại `debt_ledger.py`.
