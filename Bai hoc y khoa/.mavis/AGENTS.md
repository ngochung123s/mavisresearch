# Daily Medical Lesson - Project Conventions

> Project: F:\DL\mavisresearch\Bai hoc y khoa\
> Author: Bac si Ngoc
> AI: tên model đang dùng (trước đây: MiniMax Mavis; hiện tại: opencode deepseek-v4-pro)
> Updated: 2026-06-29

## Quy ước ngôn ngữ (CẬP NHẬT 2026-06-22)

**QUAN TRỌNG**: Từ bài 22/06/2026 trở đi, **NỘI DUNG bài học dùng tiếng Việt CÓ DẤU** đầy đủ. Trước đó (12-19/06) tôi dùng không dấu - đã convert sang có dấu qua script `add_diacritics.py`.

### Quy tắc cụ thể:
- **Filename / folder name**: KHÔNG dấu (giữ nguyên cấu trúc cũ, an toàn cho Windows + PowerShell)
- **Content trong file (.md, .apkg)**: CÓ dấu đầy đủ
- **Tiếng Việt là chính — tiếng Anh là phụ (CẬP NHẬT 29/06)**:
  - Nội dung bài giảng và card **PHẢI viết bằng tiếng Việt** làm ngôn ngữ chính
  - Từ tiếng Anh/thuật ngữ y khoa chỉ đặt trong **ngoặc đơn ()** sau từ tiếng Việt
  - **KHÔNG** viết tiếng Anh trước rồi tiếng Việt trong ngoặc
  - Ví dụ ĐÚNG: "kép đồng thời (dual trigger)", "hội chứng nang trống (empty follicle syndrome)", "hỗ trợ pha hoàng thể (luteal phase support)"
  - Ví dụ SAI: "dual trigger (kép đồng thời)" — sai thứ tự
  - Thuật ngữ tiếng Anh khó phải có nghĩa tiếng Việt ngay lần đầu: ví dụ "rối loạn phát triển quá mức (overgrowth disorder)", "lớp vỏ não còn lại (cortical mantle)", "bệnh do đường truyền mTOR (mTORopathy)".
- **Thuật ngữ y khoa**: Giữ nguyên tiếng Anh/La-tinh (vd: "Doppler", "cerebroplacental ratio", "DIE")
- **Tên riêng / viết tắt**: Giữ nguyên (vd: "NEJM", "ISSHP", "FIGO", "ASPRE", "T21/T18/T13")

## Quy tắc Giảng Cơ chế & Hướng dẫn Thực hành Lâm sàng (CẬP NHẬT 29/08)

- **Giảng cơ chế tập trung, không chỉ mỗi triệu chứng**: Bắt buộc giải thích theo chuỗi logic 7 tầng nhân quả liên hoàn: **Cơ chế phân tử / Receptor / Thần kinh thể dịch → Thay đổi chuyển hóa & Tế bào → Tổn thương mô & Cơ quan → Biểu hiện lâm sàng (Cơ năng & Thực thể) → Biến đổi cận lâm sàng & Xét nghiệm → Tiêu chuẩn chẩn đoán → Lựa chọn & Cơ chế điều trị**.
- **AI phải hướng dẫn người học các bước thực hiện chi tiết trên lâm sàng**: Đóng vai trò người thầy lâm sàng hướng dẫn từng bước: **Mục tiêu → Khi nào làm/không làm → Cần chuẩn bị gì → Khám hoặc đọc kết quả như thế nào → Kết quả thay đổi quyết định điều trị ra sao → Bẫy lâm sàng/An toàn → Xử trí cấp cứu & Tiêu chí chuyển tuyến**.

## Quy tắc đặt tên Anki Deck (CẬP NHẬT 2026-06-29)

**Deck hierarchy dùng `::` làm separator. 4 main deck cha:**

| Main deck | Chuyên khoa | Folder |
|---|---|---|
| **ART** | Hỗ trợ sinh sản | `02_Ho tro sinh san ART/` |
| **Fetal ultrasound** | Siêu âm thai | `03_Sieu am thai/` |
| **OB/GYN** | Sản phụ khoa tổng quát | `01_San phu khoa/` |
| **Internal medicine** | Nội khoa người lớn | `11_Noi khoa/` |

**Format:** `MAIN_DECK::Topic_Short::YYYY-MM-DD`

- Ví dụ: `ART::LPS::2026-06-29`, `ART::Trigger::Dual_Double::2026-06-29`, `OB/GYN::GDM::2026-06-28`, `Fetal ultrasound::Amniotic_Fluid::2026-06-27`
- `build_apkg.py` tự động detect main deck từ folder path của cards JSON
- Khi import vào Anki, deck cha sẽ tự động gộp các deck con cùng tên

## Cấu trúc folder release

```text
Bai hoc y khoa/XX_Chuyen_khoa/XX_Ten_bai/
  ├── Ten_bai_YYYY-MM-DD_RELEASE_vN.md
  ├── Ten_bai_YYYY-MM-DD_RELEASE_vN.cards.v2.json
  └── outputs/
      ├── Ten_bai_YYYY-MM-DD_RELEASE_vN.docx
      ├── Ten_bai_YYYY-MM-DD_RELEASE_vN.apkg
      ├── sources/
      └── verification/<release-id>/
```

**Phân loại chuyên khoa:**
- **`01_San phu khoa/`**: chuyển dạ, đẻ chỉ huy, tiền sản giật, GDM, u xơ tử cung, Asherman...
- **`02_Ho tro sinh san ART/`**: tubal patency, infertility workup, IVF/ICSI/FET, OHSS, ERA, luteal phase, stimulation, PGT...
- **`03_Sieu am thai/`**: fetal ultrasound, nước ối, Doppler, sàng lọc tam cá nguyệt thứ nhất, độ dài cổ tử cung...
- **`11_Noi khoa/`**: Nội khoa người lớn.

```
Bai hoc y khoa/
├── 01_San phu khoa/               ← San khoa tong quat
├── 02_Ho tro sinh san ART/        ← IVF/ICSI/FET/Andrology/Tubal patency
├── 03_Sieu am thai/               ← Fetal ultrasound (KHÔNG chứa bài gynecology)
├── 04_Noi tiet - Hormone/         ← (de danh)
├── 05_Vi sinh - Mien dich/        ← (de danh)
├── 06_Ung thu phu khoa/           ← (de danh)
├── 07_Visual Summary - HTML/      ← HTML visual summary cac bai cu (bài 1-19)
├── 08_Anki Deck - apkg/           ← (de danh - Anki deck dung chung)
├── 09_Source - Markdown/           ← Markdown nguon (bài 1-19 ONLY)
├── 11_Noi khoa/                    ← Nội khoa người lớn
└── 10_Script Python/              ← Script build APKG và audit
```

## Workflow daily lesson — canonical 2026-07-28

1. Khóa profile, required gates, `lesson_depth_contract` và output basename trong Research Brief trước research. Mặc định chế độ duy nhất `L3_BEGINNER`.
2. Preflight strict PMID + từng claim occurrence; zero PMID/zero parsed claim đều BLOCK.
3. Viết MD/cards từ brief theo `lesson_depth_contract`; không thêm claim ngoài brief.
4. Chạy duy nhất `build_pipeline.py --brief ... --lesson ... --cards ... --guidelines ...`.
5. Runner tạo DOCX/APKG/learner smoke và evidence manifest có SHA-256 trong `outputs/`.
6. Chỉ `PUBLISH READY` exit 0 mới được cập nhật catalog.

## Scripts trong 10_Script Python/

| Script | Mục đích |
|---|---|
| `build_pipeline.py` | Release runner canonical; sinh evidence manifest có hash và gọi publish gate |
| `publish_gate.py` | Xác thực contract, command, exit code, inputs/artifacts và SHA-256 |
| `verify_claims.py` | Kiểm từng claim occurrence; zero claim là BLOCK |
| `verify_guidelines.py` | Kiểm guideline web/PDF, freshness và supersession |
| `build_apkg.py` | Build APKG candidate/release từ cards JSON |
| `verify_apkg_diacritics.py` | Kiểm dấu và số note/card thực trong APKG |
| `md_to_docx.py` | Tạo DOCX release bắt buộc trong `outputs/` |
| `citation_audit.py` | Citation lint; release yêu cầu 0 BLOCK và 0 WARN |
| `add_diacritics.py` | Legacy: chỉ convert bài cũ, không dùng cho bài mới |

## Citation và verification rules — năm nhãn duy nhất

Đơn vị kiểm định là **mỗi claim occurrence**, không phải mỗi PMID. Nhiều claim dùng cùng PMID phải được kiểm riêng.

- `[FETCHED]`: chỉ xác nhận metadata; cấm claim định lượng.
- `[ABSTRACT VERIFIED]`: claim định tính khớp abstract.
- `[DATA VERIFIED]`: số liệu khớp chính xác quote và abstract/full text.
- `[FULL TEXT VERIFIED]`: claim được đối chiếu từ toàn văn có artifact.
- `[GUIDELINE VERIFIED]`: khuyến cáo khớp guideline chính thức qua `verify_guidelines.py`.

Cấm nhãn cũ `[ABSTRACT MATCH]`, `[FULL VERIFIED]`, `[DIRECTION ONLY]`, `[TEXTBOOK]` và `[Thông tin cơ bản - LLM verified]`. Kiến thức consensus/sinh lý/giải phẫu cơ bản viết tự do không gán nhãn verification và không tạo áp lực bịa PMID/quote; loại nguồn (textbook/RCT/review/guideline) tách khỏi trạng thái verification.

Claim có RR/OR/HR/CI/%/n=/liều/timing/ngưỡng phải có Claim ID, quote chính xác nguyên văn (exact substring) từ local file/abstract và đủ population–intervention/comparator–outcome–timepoint. Protocol detail luôn cần nguồn gốc. Đối với Guideline quote, bắt buộc có exact substring + locator (mục/trang/đoạn).

Guideline dùng pipeline riêng: `guideline_evidence.json` bắt buộc 14 trường (`claim_id`, `society`, `title`, `document_id`, `version`, `publication_date`, `accessed_at`, `canonical_url`, `local_copy`, `sha256`, `recommendation_text` làm exact continuous substring quote không ellipsis, `locator`, `pmid` nullable, `superseded_by`). Gate `guideline_evidence` và `guideline_evidence_crosscheck` bắt buộc PASS. Guideline superseded là BLOCK.

Quy tắc dừng: Model chỉ dừng khi acceptance matrix và `lesson_depth_contract` thỏa mãn 100%. CẤM dừng vì "bài đã dài", CẤM lặp ý hay paraphrase padding.
`citation_audit.py` là citation lint, không thay thế claim verification. Release yêu cầu 0 BLOCK và 0 WARN.

## Bài học đã có (tính đến 2026-06-22)

Xem `_README.md` để biết danh sách đầy đủ. Format: `STT | Tên bài | Ngày | Status`.

## Topic rotation

- **Luân phiên giữa ART (02_)** và Fetal US (03_)** - không làm 2 bài cùng domain liên tiếp
- **ART topics available**: IVF cơ bản, ICSI, FET, PGT, OHSS, ERA, Long/short GnRH, DuoStim, mild stimulation, male factor
- **Fetal US topics available**: Fetal echo, Doppler, First Trimester Screening, Cervical length, Fetal biometry, Multiple pregnancy, NIPT, anomaly scan

## Tools thường dùng

- `pubmed_search` / PubMed MCP - search với filter nếu MCP được mount
- `biomcp search article --source pubmed` và `biomcp get article PMID` - workflow chính khi MCP không expose native tool trong OpenCode
- `webfetch` với E-utilities - fallback khi MCP/BioMCP lỗi hoặc cần query đặc biệt
- `web_search` (MCP matrix) - tìm guideline chính thức trên web
- `python` (PowerShell) - chạy build scripts
- `build_pipeline.py` - chạy toàn bộ release gate và xuất báo cáo kiểm định

## Bugs đã biết & cách workaround

1. **PowerShell single-quote JSON**: Dùng `--file` flag thay vì inline
2. **MCP `pubmed_fetch` trả empty hoặc MCP không được mount trong agent**: Dùng `biomcp` CLI trước, rồi mới fallback `webfetch` E-utilities directly
3. **MCP PubMed search fail với UTF-8** (ký tự Greek, Turkish): Dùng search query đơn giản hơn
4. **PowerShell console hiển thị UTF-8 sai** (ký tự `?`): Dùng Python `-c` để verify content
5. **add_diacritics ~80-90% accuracy**: Một số từ ambiguous giữ nguyên không dấu (vd "gan" = gan/gần, "nam" = nam/năm)
6. **BÀI HỌC CŨ (12-14/06) có DOCX không dấu** vì `make_*_lesson.py` cũ hardcode content. **ĐÃ FIX** bằng `md_to_docx.py` + `rebuild_all_docx_v2.py` chạy 22/06. Hiện 16/16 DOCX đều có dấu.
7. **TỪ GIỜ**: bài mới viết có dấu từ đầu; DOCX và APKG đều do release runner tạo trong `outputs/`. HTML chỉ dùng khi rebuild bài cũ.
8. **PROTOCOL HALLUCINATION (29/06)**: LLM suy đoán protocol details (timing, sequence, dosing) dựa trên mechanistic reasoning thay vì evidence. ĐÃ XẢY RA: double trigger bị viết sai thứ tự (hCG 40h → GnRHa 36h, đúng là GnRHa 40h → hCG 34h theo Haas 2014 PMID 25296696). **FIX**: Mọi protocol detail trong cards PHẢI có PMID gốc đính kèm. Fetch abstract của paper gốc trước khi viết.

## Workflow release hiện hành

1. Tạo research brief từ `RESEARCH_BRIEF_TEMPLATE.md`.
2. Chạy `preflight_claim_check.py`; MeSH topic chỉ advisory.
3. Viết Markdown/cards có dấu và dùng flowchart ASCII (`text`), không Mermaid.
4. Chạy canonical `build_pipeline.py`; required gate không được WARN/SKIP.
5. DOCX, APKG, learner artifacts và verification evidence nằm trong `outputs/`.
6. Chỉ promote sau `publish_gate.py` exit 0.
