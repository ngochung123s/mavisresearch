
### Output folder cho số liệu nghiên cứu y khoa (2026-06-13)

### Số liệu thay H — file canonical và pitfalls (2026-06-14)

### RPG Maker MV plugin load chain failures (2026-06-14)

### Ren'Py save pickle — cách inspect/modify thực tế (2026-06-15)
Type: technical
- Save file của Ren'Py thực ra là **ZIP** chứa `log` (pickle protocol 2), `json`, `screenshot.png`, `signatures`.
- `persistent` file thì là **pickle thuần** (không zip).
- Để load được pickle, cần bootstrap Ren'Py: tạo `sys.modules['renpy']` package với `__path__=game/renpy`, fake `renpy.game.log` (mutated = `{}` dict, không phải bool hay set), fake `renpy.update_path()`. Sau đó `from renpy.revertable import RevertableList` hoạt động.
- Pickle load trả về `(roots_dict, RollbackLog)`. **Game state thật ở `roots`** (dict id→object), KHÔNG phải `log.current.stores`.
- PSL 0.87.0: nhân vật chính là `roots['store.player']` (class `PlayerStats`), girl stats là `roots['store.<name>s']` (vd `store.sams`, `store.emilias`). Stats gồm: `affection`, `obedience`, `sluttiness`, `boldness`, `corruption`, `servicepoints`, `eventpoints`, `publicpoints`, `whorepoints`, `obscenepoints`, `romancepoints`, `_mood`, `_tired`, `_fitness`, `_allure`, `_confidence`, `_desire`, `_int`, `cash`, `corruption`, `body`, `breasts`, ...
- Stub class khi load pickle cần: `__setstate__` linh hoạt (dict hoặc tuple), `__getattr__` trả safe default (không raise), ưu tiên `__getattr__` thay vì class attr cứng.

### Game lỗi release — khi nào KHÔNG nên patch (2026-06-15)
Type: heuristic
- Nếu bản game release có bug cố hữu (vd PSL 0.87.0 crash mỗi `new_day` vì `MC is not defined`), patch bằng stub class thường GÂY THÊM bug (proxy + list = crash, override `__getattr__` ở stub ảnh hưởng rendering).
- Kinh nghiệm: hỏi user trước khi patch; nếu user nói "ignore là chạy được" → dừng, không patch. Mỗi fix có thể phá thứ khác (kiểu "mat hinh anh").
- Patch file `.rpy` Ren'Py compile thành `.rpyc` cached. **Phải xóa cả 2** khi restore bản gốc.

### Pixel art: less is more (2026-06-17)

### Team plan với medical-synthesis-writer - pattern thất bại (2026-06-19)
Type: lesson-learned
- Task tổng hợp "30+ page docx + 100+ Anki cards + markdown source" thường timeout ở medical-synthesis-writer (3 lần retry, 15min/runtime limit).
- Pattern fail: agent đi quá sâu vào planning + viết content lần lượt từng block thay vì generate hết content trong structured Python data trước rồi mới build.
- Cách work tốt hơn: agent CŨ đã làm đúng (tạo `sat_content.py` 99KB với structured data + `build_sat.py` builder) nhưng timeout trước khi chạy. Verify output trong workspace trước khi retry - work đã có thể đã xong.
- Khi agent timeout: check `C:\Users\THANHANH\.mavis\plans\plan_<id>\workspace\` + `outputs\<task>\` xem có file partial không. Nếu có, owner có thể take over và chạy nốt.

### Citation audit workflow cho bài học y khoa (2026-06-19)
Type: technical
- Project daily medical lesson tại `F:\DL\mavisresearch\Bai hoc y khoa\` cần citation audit vì LLM hay hallucinate PMID + số liệu cụ thể (RR, CI, %, n=).
- 3 file chính trong `10_Script Python/`:
  - `journal_quartile.json` — ~50 journal sản phụ khoa mapping Q1-Q4 + aliases PubMed
  - `guideline_registry.json` — ~30 guideline ASRM/ACOG/RCOG/ESHRE/ISUOG/NICE/FIGO/WHO + supersede tracking
  - `citation_audit.py` — main script: extract PMID + guideline, verify qua PubMed E-utilities, assign Tier 0-4, output report
- Tier system: Tier 0 (Guideline) > Tier 1 (Q1) > Tier 2 (Q2) > Tier 3 (Q3) > Tier 4 (Q4_AVOID) > Tier 5 (NOT_FOUND).
- Strictness hybrid: specific claim (RR/CI/%/n=) + Tier 4 → BLOCK; specific claim + Tier 1/2 → WARN; direction only + Tier 1/2 → OK.
- Wrapper `make_lesson_cited.py` gọi audit script, exit 0/1 cho CI.
- Cite format guideline: `[SOCIETY YYYY - Doc ID]` vd `[ACOG PB #175]`, `[ISUOG 2023 - Fetal Biometry]`.
- PMID fetch rate limit: 0.35s giữa các call (E-utilities).
- **BẮT BUỘC verify abstract TRƯỚC khi cite số liệu cụ thể**. Chỉ PMID tồn tại + title khớp KHÔNG đủ.

### LLM hallucination — PMID và số liệu cụ thể (2026-06-19)
Type: lesson-learned
- **Bài học 17/06 Cervical Length**: 7/19 PMID (37%) SAI TOPIC — paper về lao (PMID 21514889), cổ chân (25658069), vai (26921128), mạch máu (22504511), ung thư COVID tiếng Nga (33301247), COPD (35787523), khảo sát (36915023). 1 PMID (19888076) không tồn tại trong PubMed (có thể typo của 19888080).
- **Bài học 18/06 Long GnRH Agonist** (tôi tự viết): 10/10 PMID tồn tại và title khớp, NHƯNG tôi đã bịa số liệu cụ thể: "RR 0.96, 95% CI 0.90-1.03, p=0.27", "RR 0.48, 95% CI 0.38-0.61" cho Liu 2023 (PMID 38095077) — KHÔNG có trong abstract. Tương tự với Kadoura 2022 (PMID 35292717), Hu 2024 (37884809).
- **Pattern**: LLM dễ dàng bịa các con số cụ thể (RR, CI, %, sample size) khi viết về meta-analysis/clinical trial. Cần fetch full text hoặc abstract rõ ràng có số đó trước khi cite.
- **Quy tắc mới**: Claim có số liệu cụ thể → BẮT BUỘC mark `[FULL VERIFIED]` và fetch full text. Claim direction/qualitative → `[ABSTRACT VERIFIED]` là đủ.

### Citation strictness rules cho medical writing (2026-06-19)
Type: heuristic
- Cite PMID chỉ với title/abstract verified → có thể hợp lý nhưng KHÔNG cite số liệu cụ thể.
- Tier 4 (Q4 / predatory journal) + specific claim → BLOCK (không publish).
- Tier 4 + direction only → WARN (chỉ dùng khi không có source tốt hơn).
- Unknown journal (không có trong table) + specific claim → WARN mạnh "VERIFY TOPIC RELEVANCE".
- Default cho journal unknown: Tier 3 (cân nhắc) để tránh false positive.
- Guideline superseded → WARN với gợi ý dùng bản mới hơn.
- Guideline không trong registry → UNKNOWN_GUIDELINE, verify thủ công hoặc thêm vào registry.

### Citation audit scan toàn project (2026-06-19)
Type: technical
- Script `scan_all_lessons.py` scan tất cả .docx + .md trong `F:\DL\mavisresearch\Bai hoc y khoa\` (skip source/script dirs), output audit report vào `10_Script Python/audit_reports/audit_all_lessons_<date>.{md,json}` + `unknown_journals_<date>.txt`.
- Lần scan đầu: 21 files, 294 citations, **2 BLOCK (cả 2 NOT_FOUND PMID)**, **96 unique unknown journals**. Sau khi add 115 journals (Q1-Q4) + 64 aliases: **0 unknown**, 5 BLOCK (tất cả đều legitimate - sai topic hoặc NOT_FOUND).
- 5 BLOCK legit:
  - PMID 16195969 (Zentralbl Gynakol) - ENZIAN-score trong bài Endometriosis
  - PMID 19888080 NOT_FOUND trong bài IVF 12/06 (typo của 19888076 hoặc khác)
  - PMID 23350334 (An R Acad Nac Med Madrid) - Spanish cardiology lecture, sai topic
  - PMID 33301247 (Khirurgiia Moscow) - Russian COVID cancer, sai topic
  - PMID 19888076 NOT_FOUND trong bài Cervical Length 17/06
- Cron `daily-lesson-2100` đã update với workflow mới: bắt buộc fetch abstract, không hallucinate số liệu, chạy citation_audit sau build, fail nếu BLOCK.
- `journal_quartile.json` v3 có 100+ journal: OB/GYN core + ART + ultrasound + cardiology (fetal echo) + pediatrics + endocrinology + molecular bio. Q4_AVOID bao gồm 8+ journal sai topic đã thấy trong audit (Khirurgiia, An R Acad Nac Med, J Sport Rehabil, Vasc Endovascular Surg, Tuberculosis, J Surg Res, Arthroscopy, J Phys Chem A).

### Vietnamese content PHẢI có dấu đầy đủ (2026-06-22)

### Daily medical lessons - tieng Viet co dau trong content (2026-06-22)

### MD -> DOCX parser script created (2026-06-22)

### Vietnamese diacritics governance cho bài học y khoa (2026-06-22)
Type: workflow
- **Quy ước split**: filename/folder KHÔNG dấu (Windows safe) nhưng **content trong .md/.docx/.apkg/.html PHẢI CÓ DẤU ĐẦY ĐỦ**.
- **Giữ nguyên tiếng Anh**: thuật ngữ y khoa (Doppler, ICSI, T21), guideline abbreviations (FIGO, ASPRE, NEJM, ACOG), tên thuốc (aspirin, hCG), tên riêng.
- **Bug ngầm đã sửa (22/06)**: `make_*_lesson.py` cũ hardcode content không dấu trong Python source → user report "vẫn không có dấu" dù MD đã convert. Root cause: script build không đọc từ MD.
  - **Fix**: tạo `md_to_docx.py` parser MD → DOCX đọc UTF-8 trực tiếp từ file MD (KHÔNG hardcode content). Áp dụng cho 16 bài bằng `rebuild_all_docx_v2.py`.
- **Tooling enforce (4 lớp)**:
  1. `WORKFLOW.md` ở root + `10_Script Python\WORKFLOW.md` — checklist workflow
  2. `template_lesson.md` — template có dấu sẵn, copy khi viết bài mới
  3. `verify_diacritics.py` — scan % dấu trong MD, threshold ≥ 80% = OK. Logic: classify word thành vn_diac / vn_no_diac / other, ratio = vn_diac / (vn_diac + vn_no_diac). Bỏ qua English/numbers khi tính.
  4. `.mavis/AGENTS.md` ở root — project memory document conventions
- **add_diacritics.py** (~500 entries): manual mapping cho từ y khoa phổ biến. Ambiguous (KHÔNG auto-convert): gan, nam, mo, co, benh, huyet, etc.
- **verify_diacritics.py kết quả 22/06**: 16/16 MD files đạt 90-96% ratio (PASS). Threshold lúc đầu 80% đặt trên tổng từ → 16/16 FAIL vì thuật ngữ Anh (PMID, T21, FIGO) làm tăng tổng. Fix: chỉ tính ratio trên từ tiếng Việt.
- **PowerShell hiển thị UTF-8 sai** (`?` thay vì dấu): phải verify bằng `python -c "print(open(f).read())"` để xem content thật.
- **Citation audit**: 0 BLOCK yêu cầu, tier system Tier 0 (guideline) > 1 (Q1) > 2 (Q2) > 3 (Q3) > 4 (Q4_AVOID) > 5 (NOT_FOUND).
- **Daily cron `daily-lesson-2100`**: build bài mới 21h Vietnam time, 4 deliverable (.docx + .apkg + .html + Telegram text).

### LPS lesson - workflow note (2026-06-22)
Type: workflow
- Bài LPS (Luteal Phase Support trong ART) build xong 22/06 21h00. 9 citations verified qua E-utilities webfetch, 0 BLOCK, 8 WARN (Q1/Q2 + specific claim - all FULL VERIFIED).
- Journal additions vào journal_quartile.json: Nature Reviews Endocrinology (Q1, IF 31), Current Opinion in Obstetrics and Gynecology (Q2, IF 2.5). Cả 2 cần add alias vì citation_audit map bằng alias.
- Kastora 2024 (Sci Rep) tier Q2 (IF 4.6 - đã có), nhưng đã verify abstract trực tiếp - các số liệu OR/CrI đều chính xác.
- Pattern thành công: search PubMed cho topic → verify abstract bằng webfetch E-utilities (vì MCP pubmed_fetch trả empty) → ghi [FULL VERIFIED] cho số liệu cụ thể.


### Daily session stop - root cause + fix (2026-06-23)
