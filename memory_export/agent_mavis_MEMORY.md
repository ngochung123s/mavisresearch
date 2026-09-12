
### Output folder cho sß╗æ liß╗çu nghi├¬n cß╗⌐u y khoa (2026-06-13)

### Sß╗æ liß╗çu thay H ΓÇö file canonical v├á pitfalls (2026-06-14)

### RPG Maker MV plugin load chain failures (2026-06-14)

### Ren'Py save pickle ΓÇö c├ích inspect/modify thß╗▒c tß║┐ (2026-06-15)
Type: technical
- Save file cß╗ºa Ren'Py thß╗▒c ra l├á **ZIP** chß╗⌐a `log` (pickle protocol 2), `json`, `screenshot.png`, `signatures`.
- `persistent` file th├¼ l├á **pickle thuß║ºn** (kh├┤ng zip).
- ─Éß╗â load ─æ╞░ß╗úc pickle, cß║ºn bootstrap Ren'Py: tß║ío `sys.modules['renpy']` package vß╗¢i `__path__=game/renpy`, fake `renpy.game.log` (mutated = `{}` dict, kh├┤ng phß║úi bool hay set), fake `renpy.update_path()`. Sau ─æ├│ `from renpy.revertable import RevertableList` hoß║ít ─æß╗Öng.
- Pickle load trß║ú vß╗ü `(roots_dict, RollbackLog)`. **Game state thß║¡t ß╗ƒ `roots`** (dict idΓåÆobject), KH├öNG phß║úi `log.current.stores`.
- PSL 0.87.0: nh├ón vß║¡t ch├¡nh l├á `roots['store.player']` (class `PlayerStats`), girl stats l├á `roots['store.<name>s']` (vd `store.sams`, `store.emilias`). Stats gß╗ôm: `affection`, `obedience`, `sluttiness`, `boldness`, `corruption`, `servicepoints`, `eventpoints`, `publicpoints`, `whorepoints`, `obscenepoints`, `romancepoints`, `_mood`, `_tired`, `_fitness`, `_allure`, `_confidence`, `_desire`, `_int`, `cash`, `corruption`, `body`, `breasts`, ...
- Stub class khi load pickle cß║ºn: `__setstate__` linh hoß║ít (dict hoß║╖c tuple), `__getattr__` trß║ú safe default (kh├┤ng raise), ╞░u ti├¬n `__getattr__` thay v├¼ class attr cß╗⌐ng.

### Game lß╗ùi release ΓÇö khi n├áo KH├öNG n├¬n patch (2026-06-15)
Type: heuristic
- Nß║┐u bß║ún game release c├│ bug cß╗æ hß╗»u (vd PSL 0.87.0 crash mß╗ùi `new_day` v├¼ `MC is not defined`), patch bß║▒ng stub class th╞░ß╗¥ng G├éY TH├èM bug (proxy + list = crash, override `__getattr__` ß╗ƒ stub ß║únh h╞░ß╗ƒng rendering).
- Kinh nghiß╗çm: hß╗Åi user tr╞░ß╗¢c khi patch; nß║┐u user n├│i "ignore l├á chß║íy ─æ╞░ß╗úc" ΓåÆ dß╗½ng, kh├┤ng patch. Mß╗ùi fix c├│ thß╗â ph├í thß╗⌐ kh├íc (kiß╗âu "mat hinh anh").
- Patch file `.rpy` Ren'Py compile th├ánh `.rpyc` cached. **Phß║úi x├│a cß║ú 2** khi restore bß║ún gß╗æc.

### Pixel art: less is more (2026-06-17)

### Team plan vß╗¢i medical-synthesis-writer - pattern thß║Ñt bß║íi (2026-06-19)
Type: lesson-learned
- Task tß╗òng hß╗úp "30+ page docx + 100+ Anki cards + markdown source" th╞░ß╗¥ng timeout ß╗ƒ medical-synthesis-writer (3 lß║ºn retry, 15min/runtime limit).
- Pattern fail: agent ─æi qu├í s├óu v├áo planning + viß║┐t content lß║ºn l╞░ß╗út tß╗½ng block thay v├¼ generate hß║┐t content trong structured Python data tr╞░ß╗¢c rß╗ôi mß╗¢i build.
- C├ích work tß╗æt h╞ín: agent C┼¿ ─æ├ú l├ám ─æ├║ng (tß║ío `sat_content.py` 99KB vß╗¢i structured data + `build_sat.py` builder) nh╞░ng timeout tr╞░ß╗¢c khi chß║íy. Verify output trong workspace tr╞░ß╗¢c khi retry - work ─æ├ú c├│ thß╗â ─æ├ú xong.
- Khi agent timeout: check `C:\Users\THANHANH\.mavis\plans\plan_<id>\workspace\` + `outputs\<task>\` xem c├│ file partial kh├┤ng. Nß║┐u c├│, owner c├│ thß╗â take over v├á chß║íy nß╗æt.

### Citation audit workflow cho b├ái hß╗ìc y khoa (2026-06-19)
Type: technical
- Project daily medical lesson tß║íi `F:\DL\mavisresearch\Bai hoc y khoa\` cß║ºn citation audit v├¼ LLM hay hallucinate PMID + sß╗æ liß╗çu cß╗Ñ thß╗â (RR, CI, %, n=).
- 3 file ch├¡nh trong `10_Script Python/`:
  - `journal_quartile.json` ΓÇö ~50 journal sß║ún phß╗Ñ khoa mapping Q1-Q4 + aliases PubMed
  - `guideline_registry.json` ΓÇö ~30 guideline ASRM/ACOG/RCOG/ESHRE/ISUOG/NICE/FIGO/WHO + supersede tracking
  - `citation_audit.py` ΓÇö main script: extract PMID + guideline, verify qua PubMed E-utilities, assign Tier 0-4, output report
- Tier system: Tier 0 (Guideline) > Tier 1 (Q1) > Tier 2 (Q2) > Tier 3 (Q3) > Tier 4 (Q4_AVOID) > Tier 5 (NOT_FOUND).
- Strictness hybrid: specific claim (RR/CI/%/n=) + Tier 4 ΓåÆ BLOCK; specific claim + Tier 1/2 ΓåÆ WARN; direction only + Tier 1/2 ΓåÆ OK.
- Wrapper `make_lesson_cited.py` gß╗ìi audit script, exit 0/1 cho CI.
- Cite format guideline: `[SOCIETY YYYY - Doc ID]` vd `[ACOG PB #175]`, `[ISUOG 2023 - Fetal Biometry]`.
- PMID fetch rate limit: 0.35s giß╗»a c├íc call (E-utilities).
- **Bß║«T BUß╗ÿC verify abstract TR╞»ß╗ÜC khi cite sß╗æ liß╗çu cß╗Ñ thß╗â**. Chß╗ë PMID tß╗ôn tß║íi + title khß╗¢p KH├öNG ─æß╗º.

### LLM hallucination ΓÇö PMID v├á sß╗æ liß╗çu cß╗Ñ thß╗â (2026-06-19)
Type: lesson-learned
- **B├ái hß╗ìc 17/06 Cervical Length**: 7/19 PMID (37%) SAI TOPIC ΓÇö paper vß╗ü lao (PMID 21514889), cß╗ò ch├ón (25658069), vai (26921128), mß║ích m├íu (22504511), ung th╞░ COVID tiß║┐ng Nga (33301247), COPD (35787523), khß║úo s├ít (36915023). 1 PMID (19888076) kh├┤ng tß╗ôn tß║íi trong PubMed (c├│ thß╗â typo cß╗ºa 19888080).
- **B├ái hß╗ìc 18/06 Long GnRH Agonist** (t├┤i tß╗▒ viß║┐t): 10/10 PMID tß╗ôn tß║íi v├á title khß╗¢p, NH╞»NG t├┤i ─æ├ú bß╗ïa sß╗æ liß╗çu cß╗Ñ thß╗â: "RR 0.96, 95% CI 0.90-1.03, p=0.27", "RR 0.48, 95% CI 0.38-0.61" cho Liu 2023 (PMID 38095077) ΓÇö KH├öNG c├│ trong abstract. T╞░╞íng tß╗▒ vß╗¢i Kadoura 2022 (PMID 35292717), Hu 2024 (37884809).
- **Pattern**: LLM dß╗à d├áng bß╗ïa c├íc con sß╗æ cß╗Ñ thß╗â (RR, CI, %, sample size) khi viß║┐t vß╗ü meta-analysis/clinical trial. Cß║ºn fetch full text hoß║╖c abstract r├╡ r├áng c├│ sß╗æ ─æ├│ tr╞░ß╗¢c khi cite.
- **Quy tß║»c mß╗¢i**: Claim c├│ sß╗æ liß╗çu cß╗Ñ thß╗â ΓåÆ Bß║«T BUß╗ÿC mark `[FULL VERIFIED]` v├á fetch full text. Claim direction/qualitative ΓåÆ `[ABSTRACT VERIFIED]` l├á ─æß╗º.

### Citation strictness rules cho medical writing (2026-06-19)
Type: heuristic
- Cite PMID chß╗ë vß╗¢i title/abstract verified ΓåÆ c├│ thß╗â hß╗úp l├╜ nh╞░ng KH├öNG cite sß╗æ liß╗çu cß╗Ñ thß╗â.
- Tier 4 (Q4 / predatory journal) + specific claim ΓåÆ BLOCK (kh├┤ng publish).
- Tier 4 + direction only ΓåÆ WARN (chß╗ë d├╣ng khi kh├┤ng c├│ source tß╗æt h╞ín).
- Unknown journal (kh├┤ng c├│ trong table) + specific claim ΓåÆ WARN mß║ính "VERIFY TOPIC RELEVANCE".
- Default cho journal unknown: Tier 3 (c├ón nhß║»c) ─æß╗â tr├ính false positive.
- Guideline superseded ΓåÆ WARN vß╗¢i gß╗úi ├╜ d├╣ng bß║ún mß╗¢i h╞ín.
- Guideline kh├┤ng trong registry ΓåÆ UNKNOWN_GUIDELINE, verify thß╗º c├┤ng hoß║╖c th├¬m v├áo registry.

### Citation audit scan to├án project (2026-06-19)
Type: technical
- Script `scan_all_lessons.py` scan tß║Ñt cß║ú .docx + .md trong `F:\DL\mavisresearch\Bai hoc y khoa\` (skip source/script dirs), output audit report v├áo `10_Script Python/audit_reports/audit_all_lessons_<date>.{md,json}` + `unknown_journals_<date>.txt`.
- Lß║ºn scan ─æß║ºu: 21 files, 294 citations, **2 BLOCK (cß║ú 2 NOT_FOUND PMID)**, **96 unique unknown journals**. Sau khi add 115 journals (Q1-Q4) + 64 aliases: **0 unknown**, 5 BLOCK (tß║Ñt cß║ú ─æß╗üu legitimate - sai topic hoß║╖c NOT_FOUND).
- 5 BLOCK legit:
  - PMID 16195969 (Zentralbl Gynakol) - ENZIAN-score trong b├ái Endometriosis
  - PMID 19888080 NOT_FOUND trong b├ái IVF 12/06 (typo cß╗ºa 19888076 hoß║╖c kh├íc)
  - PMID 23350334 (An R Acad Nac Med Madrid) - Spanish cardiology lecture, sai topic
  - PMID 33301247 (Khirurgiia Moscow) - Russian COVID cancer, sai topic
  - PMID 19888076 NOT_FOUND trong b├ái Cervical Length 17/06
- Cron `daily-lesson-2100` ─æ├ú update vß╗¢i workflow mß╗¢i: bß║»t buß╗Öc fetch abstract, kh├┤ng hallucinate sß╗æ liß╗çu, chß║íy citation_audit sau build, fail nß║┐u BLOCK.
- `journal_quartile.json` v3 c├│ 100+ journal: OB/GYN core + ART + ultrasound + cardiology (fetal echo) + pediatrics + endocrinology + molecular bio. Q4_AVOID bao gß╗ôm 8+ journal sai topic ─æ├ú thß║Ñy trong audit (Khirurgiia, An R Acad Nac Med, J Sport Rehabil, Vasc Endovascular Surg, Tuberculosis, J Surg Res, Arthroscopy, J Phys Chem A).

### Vietnamese content PHß║óI c├│ dß║Ñu ─æß║ºy ─æß╗º (2026-06-22)

### Daily medical lessons - tieng Viet co dau trong content (2026-06-22)

### MD -> DOCX parser script created (2026-06-22)

### Vietnamese diacritics governance cho b├ái hß╗ìc y khoa (2026-06-22)
Type: workflow
- **Quy ╞░ß╗¢c split**: filename/folder KH├öNG dß║Ñu (Windows safe) nh╞░ng **content trong .md/.docx/.apkg/.html PHß║óI C├ô Dß║ñU ─Éß║ªY ─Éß╗ª**.
- **Giß╗» nguy├¬n tiß║┐ng Anh**: thuß║¡t ngß╗» y khoa (Doppler, ICSI, T21), guideline abbreviations (FIGO, ASPRE, NEJM, ACOG), t├¬n thuß╗æc (aspirin, hCG), t├¬n ri├¬ng.
- **Bug ngß║ºm ─æ├ú sß╗¡a (22/06)**: `make_*_lesson.py` c┼⌐ hardcode content kh├┤ng dß║Ñu trong Python source ΓåÆ user report "vß║½n kh├┤ng c├│ dß║Ñu" d├╣ MD ─æ├ú convert. Root cause: script build kh├┤ng ─æß╗ìc tß╗½ MD.
  - **Fix**: tß║ío `md_to_docx.py` parser MD ΓåÆ DOCX ─æß╗ìc UTF-8 trß╗▒c tiß║┐p tß╗½ file MD (KH├öNG hardcode content). ├üp dß╗Ñng cho 16 b├ái bß║▒ng `rebuild_all_docx_v2.py`.
- **Tooling enforce (4 lß╗¢p)**:
  1. `WORKFLOW.md` ß╗ƒ root + `10_Script Python\WORKFLOW.md` ΓÇö checklist workflow
  2. `template_lesson.md` ΓÇö template c├│ dß║Ñu sß║╡n, copy khi viß║┐t b├ái mß╗¢i
  3. `verify_diacritics.py` ΓÇö scan % dß║Ñu trong MD, threshold ΓëÑ 80% = OK. Logic: classify word th├ánh vn_diac / vn_no_diac / other, ratio = vn_diac / (vn_diac + vn_no_diac). Bß╗Å qua English/numbers khi t├¡nh.
  4. `.mavis/AGENTS.md` ß╗ƒ root ΓÇö project memory document conventions
- **add_diacritics.py** (~500 entries): manual mapping cho tß╗½ y khoa phß╗ò biß║┐n. Ambiguous (KH├öNG auto-convert): gan, nam, mo, co, benh, huyet, etc.
- **verify_diacritics.py kß║┐t quß║ú 22/06**: 16/16 MD files ─æß║ít 90-96% ratio (PASS). Threshold l├║c ─æß║ºu 80% ─æß║╖t tr├¬n tß╗òng tß╗½ ΓåÆ 16/16 FAIL v├¼ thuß║¡t ngß╗» Anh (PMID, T21, FIGO) l├ám t─âng tß╗òng. Fix: chß╗ë t├¡nh ratio tr├¬n tß╗½ tiß║┐ng Viß╗çt.
- **PowerShell hiß╗ân thß╗ï UTF-8 sai** (`?` thay v├¼ dß║Ñu): phß║úi verify bß║▒ng `python -c "print(open(f).read())"` ─æß╗â xem content thß║¡t.
- **Citation audit**: 0 BLOCK y├¬u cß║ºu, tier system Tier 0 (guideline) > 1 (Q1) > 2 (Q2) > 3 (Q3) > 4 (Q4_AVOID) > 5 (NOT_FOUND).
- **Daily cron `daily-lesson-2100`**: build b├ái mß╗¢i 21h Vietnam time, 4 deliverable (.docx + .apkg + .html + Telegram text).

### LPS lesson - workflow note (2026-06-22)
Type: workflow
- B├ái LPS (Luteal Phase Support trong ART) build xong 22/06 21h00. 9 citations verified qua E-utilities webfetch, 0 BLOCK, 8 WARN (Q1/Q2 + specific claim - all FULL VERIFIED).
- Journal additions v├áo journal_quartile.json: Nature Reviews Endocrinology (Q1, IF 31), Current Opinion in Obstetrics and Gynecology (Q2, IF 2.5). Cß║ú 2 cß║ºn add alias v├¼ citation_audit map bß║▒ng alias.
- Kastora 2024 (Sci Rep) tier Q2 (IF 4.6 - ─æ├ú c├│), nh╞░ng ─æ├ú verify abstract trß╗▒c tiß║┐p - c├íc sß╗æ liß╗çu OR/CrI ─æß╗üu ch├¡nh x├íc.
- Pattern th├ánh c├┤ng: search PubMed cho topic ΓåÆ verify abstract bß║▒ng webfetch E-utilities (v├¼ MCP pubmed_fetch trß║ú empty) ΓåÆ ghi [FULL VERIFIED] cho sß╗æ liß╗çu cß╗Ñ thß╗â.


### Daily session stop - root cause + fix (2026-06-23)
