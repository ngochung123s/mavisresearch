# User Profile

## Confirmed
- **Field**: Y khoa (medical). Self-identified in 2026-06-10 session.
- **Role**: B├íc s─⌐ tß╗▒ hß╗ìc (x├íc nhß║¡n 2026-06-10). Kh├┤ng phß║úi giß║úng vi├¬n, kh├┤ng trß╗▒c tiß║┐p ─æß╗⌐ng lß╗¢p. C├│ thß╗â l├á: b├íc s─⌐ ─æa khoa / b├íc s─⌐ chuy├¬n khoa kh├íc muß╗æn update sß║ún phß╗Ñ khoa / b├íc s─⌐ ─æang ├┤n thi / b├íc s─⌐ nghi├¬n cß╗⌐u.
- **Depth preference** (2026-06-10): **Guideline + c╞í chß║┐** ΓÇö tß╗⌐c cß║ºn cß║ú hai: (a) khuyß║┐n c├ío hiß╗çn h├ánh (ASRM/ACOG/ESHRE/RCOG/NICE...) k├¿m mß╗⌐c evidence, (b) sinh l├╜/pathway ─æß║▒ng sau ─æß╗â hiß╗âu v├¼ sao guideline khuyß║┐n c├ío vß║¡y.
- **Workflow**: Tß╗▒ hß╗ìc, cß║ºn tß╗òng hß╗úp + fact-check kß╗╣. Khi n├áo cß║ºn slide th├¼ bß║úo, c├▓n b├¼nh th╞░ß╗¥ng th├¼ viß║┐t **chi tiß║┐t** v├áo. ΓåÆ mß║╖c ─æß╗ïnh output d├ái, c├│ c╞í chß║┐, c├│ guideline, c├│ citation ─æß║ºy ─æß╗º, c├│ mß╗⌐c ─æß╗Ö chß║»c chß║»n.
- **Tech comfort**: Biß║┐t kh├íi niß╗çm MCP, d├╣ng PubMed qua web th╞░ß╗¥ng xuy├¬n, d├╣ng Windows + PowerShell 5.1, tiß║┐ng Viß╗çt ch├¡nh.
- **Workspace**: `F:\DL\` (th╞░ mß╗Ñc Download/t├ái liß╗çu tr├¬n ß╗ò F:).
- **Output folder b├ái hß╗ìc y khoa** (Cß║¼P NHß║¼T 2026-06-13): `F:\DL\mavisresearch\Bai hoc y khoa\` ΓÇö **TUYß╗åT ─Éß╗ÉI KH├öNG ghi file b├ái hß╗ìc y khoa v├áo ß╗ò C:** (C sß║»p kiß╗çt). D├╣ng cß║Ñu tr├║c folder c├│ sß║╡n: `01_San phu khoa/`, `02_Ho tro sinh san ART/`, `03_Sieu am thai/`, `09_Source - Markdown/`, `10_Script Python/`. ─Éß╗ìc `_README.md` ─æß╗â biß║┐t cß║Ñu tr├║c chi tiß║┐t.
- **Email d├╣ng cho NCBI**: `thanh-anh.researcher@example.com` (placeholder ΓÇö bß║ín ch╞░a cung cß║Ñp email thß║¡t, nh╞░ng ─æ├ú cung cß║Ñp NCBI API key `e71bce83...63408` ─æß╗â t─âng rate limit).
- **Stance**: Kh├┤ng muß╗æn c├ái biomcp v├¼ nß║╖ng ΓåÆ prefers lean solutions, kh├┤ng th├¡ch bloat.

## Tools available (cß║¡p nhß║¡t 2026-06-10)
─É├ú c├ái MCP `pubmed` tß║íi `C:\Users\THANHANH\.mavis\mcp\pubmed.py` vß╗¢i 8 tool:

## Custom scripts (cß║¡p nhß║¡t 2026-06-13)
Tß║íi `C:\Users\THANHANH\.mavis\scripts\`:
- `weekly_papers.py` ΓÇö Tß╗▒ ─æß╗Öng t├¼m paper mß╗¢i vß╗ü ART/IVF + Fetal Ultrasound, gß╗¡i Telegram mß╗ùi tß╗æi thß╗⌐ 7 l├║c 20h
- `multi_pmid.py` ΓÇö T├│m tß║»t + so s├ính nhiß╗üu PMID (cho literature review)
- `citation_graph.py` ΓÇö Vß║╜ s╞í ─æß╗ô citation giß╗»a c├íc paper (HTML + vis.js)
- `sync_to_gdrive.ps1` ΓÇö Sync `.mavis` l├¬n Google Drive
- `make_anki_deck.py` ΓÇö skill chuyß╗ân JSON ΓåÆ Anki .apkg
- `pubmed_search` ΓÇö search PubMed, c├│ filter (year, article_type, free_full_text, sort)
- `pubmed_fetch` ΓÇö fetch full abstract by PMID
- `pubmed_related` ΓÇö similar articles
- `pubmed_pmc_link` ΓÇö check PMC availability + return URLs
- `pubmed_pmc_pdf` ΓÇö download PDF (UNRELIABLE cho paper mß╗¢i, ╞░u ti├¬n fulltext)
- `pubmed_pmc_fulltext` ΓÇö fetch full text as plain text (parse JATS XML tß╗½ Europe PMC) ΓÇö **C├üCH Tß╗ÉT NHß║ñT ─æß╗â ─æß╗ìc paper open-access**
- `trial_search` ΓÇö search ClinicalTrials.gov v2
- `trial_fetch` ΓÇö fetch trial by NCT ID

API key ─æ├ú set ΓåÆ rate limit 10 req/s (gß║Ñp 3 lß║ºn kh├┤ng key).
Cache key ─æ├ú normalize (diacritics-strip, lowercase) ΓåÆ hit rate tß╗æt h╞ín.

## To clarify next time
- T├¬n thß║¡t / c├ích gß╗ìi (hiß╗çn ch╞░a biß║┐t).
- Chuy├¬n khoa hiß╗çn tß║íi + chuy├¬n khoa muß╗æn hß╗ìc s├óu (Sß║ún vs Phß╗Ñ vs Hß╗ù trß╗ú sinh sß║ún vs Mß╗Ñc ti├¬u thi).
- Quß╗æc gia/tß╗ënh th├ánh ─æang c├┤ng t├íc ΓÇö ─æß╗â biß║┐t guideline n├áo s├ít thß╗▒c tß║┐ (BV Viß╗çt Nam theo BYT, theo ACOG/ASRM, hay theo RCOG/ESHRE).
- C├│ t├ái khoß║ún th╞░ viß╗çn sß╗æ ─ÉH Y / bv kh├┤ng? (nß║┐u c├│, c├│ thß╗â build tool tß║úi paper tß╗½ Fert Steril/Obstet Gynecol qua EZproxy).

## ART/IVF Knowledge Level (2026-06-12)
**─É├â BIß║╛T:**
- Trigger protocols: HCG, GnRH agonist trigger (─æ├ú biß║┐t, kh├┤ng dß║íy lß║íi)
- Ph├íc ─æß╗ô: Antagonist protocol, PPOS (─æ├ú biß║┐t, kh├┤ng dß║íy lß║íi)
- Sinh trß║»c hß╗ìc c╞í bß║ún (biometrics basics ΓÇö ch╞░a s├óu)

**Cß║ªN Hß╗îC S├éU H╞áN:**
- GnRH agonist long protocol (chi tiß║┐t)
- GnRH agonist short/flare protocol
- Mild stimulation / Natural cycle IVF
- Double stimulation (DuoStim)
- Advanced biometrics: endometrial volume, 3D/4D ultrasound, ovarian reserve tests (AMH, AFC chi tiß║┐t)
- Uterine factor: HSG, HyFoSy, SIS, hysteroscopy
- Male factor: SA, DNA fragmentation, TESE/MESA
- Embryology: ICSI, time-lapse, PGT-A/PGT-M
- Si├¬u ├óm thai kß╗│ chuy├¬n s├óu: cervical length, Doppler, growth charts, fetal biometry

## Preferences observed
- Ng├┤n ngß╗»: **Tiß║┐ng Viß╗çt l├á ch├¡nh**, thuß║¡t ngß╗» y khoa giß╗» nguy├¬n tiß║┐ng Anh/La-tinh khi cß║ºn. KH├öNG trß╗Ön tiß║┐ng Anh nhiß╗üu v├áo c├óu trß║ú lß╗¥i th├┤ng th╞░ß╗¥ng ΓÇö chß╗ë giß╗» thuß║¡t ngß╗» y khoa bß║»t buß╗Öc.
- Tone: Thß║│ng, kh├┤ng th├¡ch v├▓ng vo. Th├¡ch d├╣ng "theo ├╜ bß║ín", "ngh─⌐a l├á", ngß║»n gß╗ìn.
- Default output: **d├ái v├á chi tiß║┐t**, kh├┤ng t├│m tß║»t c╞░ß╗íng ├⌐p. Slide chß╗ë l├ám khi user y├¬u cß║ºu.
- Kß╗│ vß╗ìng chß║Ñt l╞░ß╗úng: guideline c├│ PMID + n─âm, c╞í chß║┐ c├│ pathway r├╡, ph├ón biß╗çt r├╡ "guideline n├│i X" vs "c╞í chß║┐ giß║úi th├¡ch Y".
- Daily lesson: 18:00 h├áng ng├áy, verify PubMed tr╞░ß╗¢c khi gß╗¡i. Kh├┤ng dß║íy tr├╣ng topic ─æ├ú biß║┐t.
- **File deliverable: lu├┤n xuß║Ñt .docx hoß║╖c .pdf**, KH├öNG trß║ú .md khi ─æ├│ l├á deliverable. Bß║úng phß║úi format chuß║⌐n, header in ─æß║¡m, border, c─ân chß╗ënh ─æß║╣p.
- **Anki deck theme mß║╖c ─æß╗ïnh: Pastel** (cß║¡p nhß║¡t 2026-06-13)
- **Anki deck content**: chß╗ë cß║ºn v─ân bß║ún gß╗æc, KH├öNG cß║ºn phß║ºn "G├│c nh├¼n bß╗ò sung cß╗ºa AI" v├¼ user hiß╗âu rß╗ôi
- **Daily lesson output format** (4 phß║ºn): (1) tin nhß║»n Telegram, (2) file .docx, (3) file .apkg, (4) file .html visual summary
- **HTML visual format**: Tailwind CSS + Mermaid (flowchart) + Chart.js (bar/doughnut), mß╗ƒ bß║▒ng tr├¼nh duyß╗çt l├á xem ngay. D├╣ng cho algorithm, so s├ính, dß╗ïch tß╗à, pathway.
