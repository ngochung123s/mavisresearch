"""Build HTML visual summary cho bai hoc Stimulation Protocols ART - 25/06/2026.

Su dung Tailwind + Mermaid + Chart.js.
"""
from pathlib import Path
import sys

sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import build_lesson_html, write_html


TITLE = 'CÃ¡c phÃ¡c Ä‘á»“ kÃ­ch trá»©ng hiá»‡n Ä‘áº¡i trong ART'
DATE = '25/06/2026'

OUTPUT_HTML = r'F:\DL\mavisresearch\Bai hoc y khoa\07_Visual Summary - HTML\Visual summary - Cac phac do kich trung ART - 2026-06-25.html'


# ============ HEADER ============
HEADER = f'''
<header class="text-center py-12 mb-12 glass rounded-3xl shadow-lg">
  <div class="inline-block px-4 py-1 mb-4 rounded-full bg-purple-200 text-purple-800 text-sm font-semibold">
    ChuyÃªn khoa: Há»— trá»£ sinh sáº£n (ART)
  </div>
  <h1 class="text-4xl md:text-5xl font-bold mb-4 text-stone-800">{TITLE}</h1>
  <p class="text-stone-600 text-lg">NgÃ y {DATE} | Cho bÃ¡c sÄ© sáº£n phá»¥ khoa / há»c viÃªn sau Ä‘áº¡i há»c</p>
  <p class="text-sm text-stone-500 mt-2">BÃ¡c sÄ©: <strong>NgÆ°á»i dÃ¹ng</strong> | AI: <strong>MiniMax Mavis</strong></p>
  <p class="text-xs text-stone-400 mt-1">10 phÃ¡c Ä‘á»“ chÃ­nh + 6 case thá»±c hÃ nh + head-to-head comparison</p>
</header>
'''


# ============ SECTIONS ============

# 1. Tong quan
SECTION_OVERVIEW = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸŽ¯ Tá»”NG QUAN â€” VÃŒ SAO BÃ€I NÃ€Y QUAN TRá»ŒNG?</h2>
  <p class="text-stone-700 mb-4">
    <strong>Controlled Ovarian Stimulation (COS)</strong> lÃ  ná»n táº£ng cá»§a má»i chu ká»³ IVF/ICSI hiá»‡n Ä‘áº¡i.
    Trong 4 tháº­p ká»· qua, COS Ä‘Ã£ phÃ¡t triá»ƒn tá»« 1 phÃ¡c Ä‘á»“ (long GnRH agonist) sang <strong>Ã­t nháº¥t 10 phÃ¡c Ä‘á»“ cÃ¡ thá»ƒ hÃ³a</strong> theo phenotype bá»‡nh nhÃ¢n.
  </p>
  <div class="grid md:grid-cols-4 gap-4 mt-6">
    <div class="pastel-purple p-5 rounded-xl">
      <div class="text-3xl mb-2">ðŸ“Š</div>
      <div class="font-bold text-stone-800">ESHRE 2025</div>
      <div class="text-sm text-stone-600 mt-2">84 khuyáº¿n cÃ¡o - 18 cÃ¢u há»i lÃ¢m sÃ ng</div>
    </div>
    <div class="pastel-pink p-5 rounded-xl">
      <div class="text-3xl mb-2">ðŸ§¬</div>
      <div class="font-bold text-stone-800">Venetis 2023</div>
      <div class="text-sm text-stone-600 mt-2">Network meta-analysis 73 RCTs</div>
    </div>
    <div class="pastel-blue p-5 rounded-xl">
      <div class="text-3xl mb-2">ðŸ’‰</div>
      <div class="font-bold text-stone-800">Lambalk 2017</div>
      <div class="text-sm text-stone-600 mt-2">IPD meta-analysis 50 studies</div>
    </div>
    <div class="pastel-mint p-5 rounded-xl">
      <div class="text-3xl mb-2">ðŸ”¬</div>
      <div class="font-bold text-stone-800">Racca 2024</div>
      <div class="text-sm text-stone-600 mt-2">RCT DuoStim-fresh n=120</div>
    </div>
  </div>
  <div class="mt-6 p-4 pastel-yellow rounded-xl">
    <strong>ðŸŽ¯ Má»¥c tiÃªu COS tá»‘i Æ°u:</strong> 8-15 nang trÆ°á»Ÿng thÃ nh (â‰¥17 mm) táº¡i trigger day.<br>
    <strong>âš ï¸ Quyáº¿t Ä‘á»‹nh protocol áº£nh hÆ°á»Ÿng:</strong> sá»‘ noÃ£n, cháº¥t lÆ°á»£ng phÃ´i, OHSS risk, chi phÃ­, fresh vs freeze-all.
  </div>
</section>
'''


# 2. 10 phac do
SECTION_10_PROTOCOLS = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ§¬ 10 PHÃC Äá»’ KÃCH TRá»¨NG CHÃNH</h2>

  <div class="mermaid">
  flowchart TD
    A[COS: Controlled Ovarian Stimulation] --> B[LH suppression strategies]
    A --> C[Stimulation intensity]
    A --> D[Special populations]
    B --> B1[Long GnRH agonist<br/>Downregulation 14d]
    B --> B2[Short Flare<br/>Flare + suppress]
    B --> B3[Microdose Flare<br/>20-50 Âµg x 2/d]
    B --> B4[GnRH Antagonist Fixed<br/>Day 5-6 - FIRST-LINE]
    B --> B5[GnRH Antagonist Flexible<br/>Khi nang 14 mm]
    B --> B6[PPOS<br/>Progesterone ngoai sinh]
    C --> C1[Mild/Mini-IVF<br/>FSH 100-150 IU]
    C --> C2[Natural/MNC<br/>0 hoac 75-100 IU]
    D --> D1[DuoStim + Random start<br/>2 phase trong 1 cycle]
    D --> D2[Letrozole-based<br/>Cho breast cancer FP]
    style B4 fill:#c5e0c9,stroke:#7ba87e,stroke-width:3px
    style B6 fill:#fce4ec,stroke:#c2185b
    style D1 fill:#fff3cd,stroke:#ffc107
    style D2 fill:#e3f2fd,stroke:#1976d2
  </div>

  <div class="mt-6 grid md:grid-cols-2 gap-4">
    <div class="pastel-mint p-4 rounded-xl">
      <h3 class="font-bold text-stone-800 mb-2">âœ… ESHRE 2025 First-line</h3>
      <p class="text-sm">GnRH Antagonist (fixed Day 5/6) - cho general IVF (strong recommendation)</p>
    </div>
    <div class="pastel-pink p-4 rounded-xl">
      <h3 class="font-bold text-stone-800 mb-2">ðŸ“Œ PPOS Ä‘áº·c biá»‡t cho</h3>
      <p class="text-sm">Freeze-all, PGT-A, fertility preservation, donor, low budget (mandatory freeze-all)</p>
    </div>
    <div class="pastel-yellow p-4 rounded-xl">
      <h3 class="font-bold text-stone-800 mb-2">ðŸ”„ DuoStim + Random start</h3>
      <p class="text-sm">Poor responder (POSEIDON 3+4), advanced age, oncology cáº§n gáº¥p</p>
    </div>
    <div class="pastel-blue p-4 rounded-xl">
      <h3 class="font-bold text-stone-800 mb-2">ðŸ’Š Letrozole-based</h3>
      <p class="text-sm">Ung thÆ° vÃº ER+ cáº§n fertility preservation - E2 tháº¥p an toÃ n</p>
    </div>
  </div>
</section>
'''


# 3. Co che Endocrine
SECTION_MECHANISM = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ§ª CÆ  CHáº¾ ENDOCRINE - HPO AXIS + 2-CELL + LH CEILING</h2>

  <h3 class="text-xl font-bold text-stone-700 mb-3">1. Trá»¥c HPO - Hypothalamic-Pituitary-Ovarian</h3>
  <div class="mermaid">
  flowchart LR
    H[HYPOTHALAMUS<br/>GnRH pulsatile<br/>90-120 min follicular] --> P[ANTERIOR PITUITARY]
    P -->|FSH| G[Granulosa cells<br/>Aromatase â†’ E2]
    P -->|LH| T[Theca cells<br/>Androstenedione]
    T -->|diffusion| G
    G -->|E2 + Inhibin B| N[Negative feedback<br/>len FSH]
    G -->|E2 cao 48h| P2[POSITIVE feedback<br/>LH surge]
    style P2 fill:#ffd54f,stroke:#f57c00,stroke-width:2px
  </div>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-6">2. LÃ½ thuyáº¿t 2-Cell (Falck 1959)</h3>
  <div class="mermaid">
  flowchart LR
    LH[LH] --> Th[Theca cell]
    Th -->|Cholesterol| And[Androstenedione]
    And -.->|diffusion| Gr[Granulosa cell]
    FSH[FSH] --> Gr
    Gr -->|Aromatase CYP19A1| E2[ESTRADIOL E2]
    style E2 fill:#ffcdd2,stroke:#c62828
  </div>

  <div class="mt-4 p-4 pastel-yellow rounded-xl">
    <h4 class="font-bold text-stone-800 mb-2">âš ï¸ LH CEILING vs LH FLOOR</h4>
    <p class="text-sm">
      <strong>LH CEILING (>1,5-2 IU/L):</strong> á»©c cháº¿ aromatase â†’ tÄƒng androgen ná»™i bÃ o, giáº£m cháº¥t lÆ°á»£ng nang.<br>
      <strong>LH FLOOR (quÃ¡ tháº¥p):</strong> deep suppression â†’ giáº£m E2 production, cáº§n r-LH á»Ÿ >35 tuá»•i + poor reserve.<br>
      <strong>ANTAGONIST giá»¯ LH á»Ÿ 0,5-1,5 IU/L</strong> (ceiling tá»‘i Æ°u) â†’ E2 sáº£n xuáº¥t Ä‘áº§y Ä‘á»§.
    </p>
  </div>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-6">3. Estrogen Window & 3 cÆ¡ cháº¿ ngÄƒn LH surge</h3>
  <div class="mermaid">
  flowchart TD
    E2[E2 â‰¥200 pg/mL<br/>kÃ©o dÃ i â‰¥48h] -->|Positive feedback| LH[LH SURGE]
    E2 -.->|Tháº¥p| Neg[Negative feedback<br/>á»©c cháº¿ FSH]
    LH -.->|Trong COS: KHONG MUON| Bad[NoÃ£n rá»¥ng sá»›m<br/>Há»ng cycle]
    Block[NgÄƒn surge - 3 cÆ¡ cháº¿] --> Agonist[1. GnRH agonist Long<br/>Desensitization 14d]
    Block --> Anta[2. GnRH antagonist<br/>Cáº¡nh tranh receptor tá»©c thÃ¬]
    Block --> Prog[3. Progesterone PPOS/DuoStim luteal<br/>Æ¯u cháº¿ HPO hypothalamus]
    style Bad fill:#ffcdd2,stroke:#c62828
    style Anta fill:#c5e0c9,stroke:#7ba87e
    style Agonist fill:#bbdefb,stroke:#1976d2
    style Prog fill:#fce4ec,stroke:#c2185b
  </div>
</section>
'''


# 4. Head-to-head comparison
SECTION_HEAD_TO_HEAD = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">âš–ï¸ HEAD-TO-HEAD: SO SÃNH CÃC PHÃC Äá»’</h2>

  <h3 class="text-xl font-bold text-stone-700 mb-3">A. Antagonist vs Long Agonist (cÃ¢u há»i cá»• Ä‘iá»ƒn nháº¥t)</h3>
  <div class="overflow-x-auto">
    <table class="w-full text-sm border-collapse">
      <thead>
        <tr class="bg-purple-200 text-stone-800">
          <th class="p-3 text-left">TiÃªu chÃ­</th>
          <th class="p-3 text-left">Antagonist</th>
          <th class="p-3 text-left">Long Agonist</th>
          <th class="p-3 text-left">Nguá»“n</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b">
          <td class="p-3 font-bold">OPR general IVF</td>
          <td class="p-3">Reference</td>
          <td class="p-3">RR 0,89 (95% CI 0,82-0,96) â€” long cao hÆ¡n</td>
          <td class="p-3 text-xs">Lambalk 2017<br/>PMID 28903472</td>
        </tr>
        <tr class="border-b pastel-mint">
          <td class="p-3 font-bold">OHSS general</td>
          <td class="p-3">Reference</td>
          <td class="p-3 font-bold">RR 0,63 (95% CI 0,50-0,81) â€” antagonist tháº¥p hÆ¡n</td>
          <td class="p-3 text-xs">Lambalk 2017</td>
        </tr>
        <tr class="border-b pastel-mint">
          <td class="p-3 font-bold">OHSS PCOS</td>
          <td class="p-3">Reference</td>
          <td class="p-3 font-bold">RR 0,53 (95% CI 0,30-0,95)</td>
          <td class="p-3 text-xs">Lambalk 2017</td>
        </tr>
        <tr class="border-b">
          <td class="p-3 font-bold">OPR PCOS</td>
          <td class="p-3">TÆ°Æ¡ng Ä‘Æ°Æ¡ng</td>
          <td class="p-3">TÆ°Æ¡ng Ä‘Æ°Æ¡ng (RR 0,97, 95% CI 0,84-1,11)</td>
          <td class="p-3 text-xs">Lambalk 2017</td>
        </tr>
        <tr class="border-b">
          <td class="p-3 font-bold">OPR poor responder</td>
          <td class="p-3">TÆ°Æ¡ng Ä‘Æ°Æ¡ng</td>
          <td class="p-3">TÆ°Æ¡ng Ä‘Æ°Æ¡ng (RR 0,87, 95% CI 0,65-1,17)</td>
          <td class="p-3 text-xs">Lambalk 2017</td>
        </tr>
        <tr>
          <td class="p-3 font-bold">Káº¿t luáº­n</td>
          <td class="p-3" colspan="3"><strong>ESHRE 2025 first-line general IVF</strong> - safety > small efficacy difference</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-8">B. Fixed Antagonist vs Flexible Antagonist (Venetis 2023)</h3>
  <div class="overflow-x-auto">
    <table class="w-full text-sm border-collapse">
      <thead>
        <tr class="bg-blue-200 text-stone-800">
          <th class="p-3 text-left">So sÃ¡nh</th>
          <th class="p-3 text-left">Fixed Day 5/6</th>
          <th class="p-3 text-left">Flexible</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b pastel-mint">
          <td class="p-3 font-bold">OPR</td>
          <td class="p-3">Reference</td>
          <td class="p-3">RR 0,76 (95% CI 0,62-0,94) - flexible tháº¥p hÆ¡n</td>
        </tr>
        <tr class="border-b">
          <td class="p-3 font-bold">SUCRA score</td>
          <td class="p-3 font-bold">84% (cao nháº¥t)</td>
          <td class="p-3">Tháº¥p hÆ¡n</td>
        </tr>
        <tr>
          <td class="p-3 font-bold">OCP pretreatment</td>
          <td class="p-3">NÃªn trÃ¡nh</td>
          <td class="p-3">OPR giáº£m RR 0,79 (95% CI 0,69-0,92)</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="text-xs text-stone-500 mt-2">ðŸ“š Venetis 2023, PMID 36594696, FULL VERIFIED - 73 RCTs network meta-analysis</p>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-8">C. DuoStim vs Single Stimulation (poor responder, Racca 2024)</h3>
  <div class="grid md:grid-cols-2 gap-4">
    <div class="pastel-yellow p-4 rounded-xl">
      <h4 class="font-bold text-stone-800">DuoStim fresh (n=53)</h4>
      <p class="text-sm">Phase 1 (luteal) + Phase 2 (follicular) trong 1 cycle</p>
      <p class="text-lg font-bold text-purple-700 mt-2">+0,81 good-quality blastocyst</p>
      <p class="text-xs">(95% CI 0,12-1,49) vs single</p>
    </div>
    <div class="pastel-blue p-4 rounded-xl">
      <h4 class="font-bold text-stone-800">Single fresh (n=54)</h4>
      <p class="text-sm">1 stimulation cycle thÃ´ng thÆ°á»ng</p>
      <p class="text-lg font-bold text-stone-700 mt-2">OPR 22,2% fresh</p>
      <p class="text-xs">vs DuoStim 24,5% (khÃ´ng khÃ¡c biá»‡t)</p>
    </div>
  </div>
  <p class="text-xs text-stone-500 mt-2">ðŸ“š Racca 2024 DUOSTIM-fresh, PMID 38845190, FULL VERIFIED - RCT n=120 phá»¥ ná»¯ <40, AMH <1,2 ng/mL</p>
  <p class="text-sm text-stone-700 mt-2"><strong>Ã nghÄ©a:</strong> DuoStim cáº£i thiá»‡n Sá» BLASTOCYST, khÃ´ng cáº£i thiá»‡n OPR fresh. Lá»£i Ã­ch cho poor responder: cumulative LBR qua nhiá»u FET.</p>
</section>
'''


# 5. Algorithm chon phac do
SECTION_ALGORITHM = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ”€ ALGORITHM CHá»ŒN PHÃC Äá»’ THEO PHENOTYPE</h2>

  <div class="mermaid">
  flowchart TD
    Start[Bá»‡nh nhÃ¢n Ä‘áº¿n IVF<br/>Test OR: AMH + AFC + tuá»•i] --> Q1{AMH &lt;0,5<br/>AFC &lt;5?}
    Start --> Q2{AMH 0,5-1,1<br/>AFC 5-7?}
    Start --> Q3{AMH 1,2-3,5<br/>AFC 8-20?}
    Start --> Q4{AMH &gt;3,5<br/>AFC &gt;24?}
    Q1 --> Q1a{Tuá»•i?}
    Q1a -->|&lt;35 POSEIDON 3| DuoS1[DuoStim + Mini]
    Q1a -->|â‰¥35 POSEIDON 4| Nat1[Natural + Mini-IVF]
    Q2 --> Q2a{Tuá»•i?}
    Q2a -->|&lt;35 POSEIDON 1| Anta1[Antagonist high-dose<br/>225-300 IU + r-LH]
    Q2a -->|â‰¥35 POSEIDON 2| DuoS2[Antagonist high-dose<br/>+ cÃ¢n nháº¯c DuoStim]
    Q3 --> Anta2[ANTAGONIST Fixed Day 5/6<br/>FIRST-LINE ESHRE 2025]
    Q4 --> PCOS1[Antagonist +<br/>GnRH trigger<br/>FREEZE-ALL]
    Anta2 -.->|Endometriosis IV| Long1[Long Agonist<br/>ultra-long 3-6 thÃ¡ng]
    Anta2 -.->|Ung thÆ° vÃº ER+| Letro1[Letrozole +<br/>random start]
    Anta2 -.->|PGT-A| PPOS1[PPOS freeze-all]
    style Anta2 fill:#c5e0c9,stroke:#7ba87e,stroke-width:3px
    style PCOS1 fill:#ffcdd2,stroke:#c62828
    style DuoS1 fill:#fff3cd,stroke:#ffc107
    style Nat1 fill:#fff3cd,stroke:#ffc107
    style Long1 fill:#bbdefb,stroke:#1976d2
    style Letro1 fill:#e1bee7,stroke:#7b1fa2
    style PPOS1 fill:#fce4ec,stroke:#c2185b
  </div>
</section>
'''


# 6. 6 case thuc hanh
SECTION_6_CASES = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ¥ 6 CASE THá»°C HÃ€NH â€” Äáº¦Y Äá»¦ QUáº¦N THá»‚ Bá»†NH NHÃ‚N</h2>

  <div class="grid md:grid-cols-2 gap-4">

    <div class="pastel-yellow p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 1: Poor Responder 38t</h3>
      <p class="text-sm mt-1"><strong>AMH 0,8, AFC 4, Ä‘Ã£ 1 IVF tháº¥t báº¡i</strong></p>
      <p class="text-sm mt-2"><strong>â†’ DUOSTIM</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>Phase 1 luteal: FSH 300 IU + antagonist day 5 â†’ trigger</li>
        <li>Phase 2 follicular 5 ngÃ y sau: FSH tiáº¿p tá»¥c</li>
        <li>Ká»³ vá»ng 6-8 noÃ£n, 3-4 blastocyst (Racca 2024 PMID 38845190)</li>
      </ul>
    </div>

    <div class="pastel-pink p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 2: PCOS 28t</h3>
      <p class="text-sm mt-1"><strong>AMH 8,5, AFC 36, OHSS risk cao</strong></p>
      <p class="text-sm mt-2"><strong>â†’ ANTAGONIST + GnRH TRIGGER + FREEZE-ALL</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>FSH 150 IU + Cetrorelix day 5-6 (KHÃ”NG OCP)</li>
        <li>Trigger: Triptorelin 0,2 mg â†’ cryo all</li>
        <li>OHSS gáº§n nhÆ° 0% (Lambalk 2017 PMID 28903472)</li>
      </ul>
    </div>

    <div class="pastel-blue p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 3: Advanced Age 42t</h3>
      <p class="text-sm mt-1"><strong>AMH 0,3, AFC 2, FSH day 2 = 18</strong></p>
      <p class="text-sm mt-2"><strong>â†’ MINI-IVF hoáº·c NATURAL CYCLE</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>Letrozole 5 mg + FSH 75-100 IU</li>
        <li>Trigger hCG khi nang 17-18 mm</li>
        <li>LBR/cycle 5-10% â€” tÆ° váº¥n egg donation</li>
      </ul>
    </div>

    <div class="pastel-purple p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 4: Endometriosis IV 32t</h3>
      <p class="text-sm mt-1"><strong>ÄÃ£ pháº«u thuáº­t ná»™i soi 6 thÃ¡ng trÆ°á»›c</strong></p>
      <p class="text-sm mt-2"><strong>â†’ LONG GnRH AGONIST ULTRA-LONG 3-6 thÃ¡ng</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>Triptorelin 3,75 mg IM má»—i 4 tuáº§n Ã— 3-6 thÃ¡ng</li>
        <li>Sau suppress: FSH 200 IU + r-LH 75</li>
        <li>Cáº£i thiá»‡n integrin Î±vÎ²3, receptivity (Tian 2023 PMID 36690299)</li>
      </ul>
    </div>

    <div class="pastel-mint p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 5: Ung thÆ° vÃº ER+ 30t</h3>
      <p class="text-sm mt-1"><strong>Sáº¯p hÃ³a trá»‹ 3-4 tuáº§n, cáº§n FP gáº¥p</strong></p>
      <p class="text-sm mt-2"><strong>â†’ LETROZOLE + RANDOM START + DUOSTIM</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>Letrozole 5 mg/ngÃ y + FSH 225 IU + HMG 75</li>
        <li>Trigger á»Ÿ báº¥t ká»³ pha nÃ o (random start)</li>
        <li>Phase 2 luteal sau 5 ngÃ y (Chen 2022 PMID 34656436)</li>
      </ul>
    </div>

    <div class="pastel-yellow p-5 rounded-xl">
      <h3 class="font-bold text-stone-800 text-lg">CASE 6: Donor + PGT-A</h3>
      <p class="text-sm mt-1"><strong>Recipient 35t POF, donor 25t, cáº§n PGT-A</strong></p>
      <p class="text-sm mt-2"><strong>â†’ PPOS cho DONOR + HRT FET cho RECIPIENT</strong></p>
      <ul class="text-xs list-disc pl-5 mt-2">
        <li>Donor: MPA 4 mg + FSH 200 IU â†’ trigger</li>
        <li>ICSI + PGT-A biopsy day 5-6</li>
        <li>FET sau HRT cycle: E2 + progesterone (Ata 2024 PMID 38159467)</li>
      </ul>
    </div>
  </div>
</section>
'''


# 7. So sanh Numbers Chart
SECTION_CHARTS = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ“Š Sá» LIá»†U Tá»ª NGHIÃŠN Cá»¨U Lá»šN</h2>

  <h3 class="text-xl font-bold text-stone-700 mb-3">Chart 1: OHSS Risk - Antagonist vs Long Agonist</h3>
  <div class="grid md:grid-cols-2 gap-6 mb-6">
    <div>
      <canvas id="ohssChart" height="200"></canvas>
    </div>
    <div class="text-sm text-stone-700 space-y-2">
      <p><strong>General IVF:</strong> Antagonist giáº£m OHSS <strong>37%</strong> (RR 0,63)</p>
      <p><strong>PCOS:</strong> Antagonist giáº£m OHSS <strong>47%</strong> (RR 0,53)</p>
      <p class="text-xs text-stone-500">ðŸ“š Lambalk 2017 PMID 28903472, IPD meta-analysis 50 studies</p>
    </div>
  </div>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-6">Chart 2: Sá»‘ Blastocyst - DuoStim vs Single</h3>
  <div class="grid md:grid-cols-2 gap-6">
    <div>
      <canvas id="blastocystChart" height="200"></canvas>
    </div>
    <div class="text-sm text-stone-700 space-y-2">
      <p><strong>DuoStim fresh:</strong> ~4,5 good-quality blastocysts</p>
      <p><strong>Single fresh:</strong> ~3,7 good-quality blastocysts</p>
      <p><strong>Mean difference: +0,81 (95% CI 0,12-1,49)</strong></p>
      <p class="text-xs text-stone-500">ðŸ“š Racca 2024 PMID 38845190, RCT n=120 phá»¥ ná»¯ <40, AMH <1,2 ng/mL</p>
    </div>
  </div>

  <h3 class="text-xl font-bold text-stone-700 mb-3 mt-6">Chart 3: Sá»‘ NoÃ£n theo Protocol</h3>
  <div class="grid md:grid-cols-2 gap-6">
    <div>
      <canvas id="oocytesChart" height="200"></canvas>
    </div>
    <div class="text-sm text-stone-700 space-y-2">
      <p>Trung bÃ¬nh sá»‘ noÃ£n MII thu Ä‘Æ°á»£c theo protocol</p>
      <p class="text-xs text-stone-500">Mild/Mini cho 4-7; Standard 8-14; DuoStim 16-22 (2 cycles)</p>
    </div>
  </div>
</section>
'''


# 8. Tips thuc hanh
SECTION_TIPS = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ’¡ 10 TIPS THá»°C HÃ€NH (CLINICAL PEARLS)</h2>

  <div class="grid md:grid-cols-2 gap-3">
    <div class="pastel-mint p-4 rounded-xl">
      <span class="font-bold text-stone-800">1. Trigger timing:</span>
      <p class="text-sm">Progesterone >1,5 ng/mL táº¡i trigger day = noÃ£n giÃ . Trigger khi 3+ nang 17-18 mm + E2 ~200 pg/mL má»—i nang.</p>
    </div>
    <div class="pastel-pink p-4 rounded-xl">
      <span class="font-bold text-stone-800">2. Antagonist + PCOS = báº¡n Ä‘á»“ng hÃ nh:</span>
      <p class="text-sm">Antagonist giáº£m OHSS rÃµ á»Ÿ PCOS (RR 0,53). Káº¿t há»£p GnRH trigger + freeze-all gáº§n nhÆ° loáº¡i bá» OHSS náº·ng.</p>
    </div>
    <div class="pastel-blue p-4 rounded-xl">
      <span class="font-bold text-stone-800">3. Long agonist deep â†’ r-LH:</span>
      <p class="text-sm">Bá»‡nh nhÃ¢n >35 + AMH tháº¥p + deep suppression (E2 <30 sau 5d FSH) â†’ thÃªm r-LH 75-150 IU.</p>
    </div>
    <div class="pastel-yellow p-4 rounded-xl">
      <span class="font-bold text-stone-800">4. DuoStim Ä‘áº·c biá»‡t tá»‘t cho oncology:</span>
      <p class="text-sm">Random-start + DuoStim trá»¯ 8-15 noÃ£n chá»‰ trong 2-3 tuáº§n trÆ°á»›c hÃ³a trá»‹. Letrozole náº¿u breast cancer.</p>
    </div>
    <div class="pastel-purple p-4 rounded-xl">
      <span class="font-bold text-stone-800">5. Äá»«ng Ã©p FSH á»Ÿ poor responder:</span>
      <p class="text-sm">FSH 450-600 IU khÃ´ng cáº£i thiá»‡n noÃ£n. Chuyá»ƒn DuoStim hoáº·c accept mild response.</p>
    </div>
    <div class="pastel-mint p-4 rounded-xl">
      <span class="font-bold text-stone-800">6. PPOS = "oral + freeze-all":</span>
      <p class="text-sm">DÃ¹ng cho freeze-all, PGT, FP, ngáº¡i tiÃªm, low budget. Nhá»› KHÃ”NG fresh ET.</p>
    </div>
    <div class="pastel-pink p-4 rounded-xl">
      <span class="font-bold text-stone-800">7. Mini-IVF cho advanced age:</span>
      <p class="text-sm">Äá»«ng Ã©p 40+ vÃ o standard. Mini-IVF cho noÃ£n cháº¥t lÆ°á»£ng hÆ¡n, Ã­t cost.</p>
    </div>
    <div class="pastel-blue p-4 rounded-xl">
      <span class="font-bold text-stone-800">8. Set day 5-6, KHÃ”NG flexible:</span>
      <p class="text-sm">Venetis 2023: flexible OPR tháº¥p hÆ¡n fixed (RR 0,76). Default fixed.</p>
    </div>
    <div class="pastel-yellow p-4 rounded-xl">
      <span class="font-bold text-stone-800">9. Monitor nang kÃ­ch thÆ°á»›c:</span>
      <p class="text-sm">â‰¥3 nang Ä‘áº¡t 17-18 mm â†’ trigger. E2 1500-2500 pg/mL cho 8-12 nang. Äá»«ng chá» E2 >3500.</p>
    </div>
    <div class="pastel-purple p-4 rounded-xl">
      <span class="font-bold text-stone-800">10. Luteal support Báº®T BUá»˜C:</span>
      <p class="text-sm">Progesterone 200 mg vaginal x 3/ngÃ y + hCG 1.500 IU náº¿u fresh ET antagonist. KhÃ´ng cáº§n náº¿u freeze-all.</p>
    </div>
  </div>
</section>
'''


# 9. Khuyen cao ESHRE 2025
SECTION_GUIDELINES = '''
<section class="glass rounded-2xl p-8 shadow-md mb-8">
  <h2 class="text-3xl font-bold text-purple-700 mb-6">ðŸ“‹ KHUYáº¾N CÃO LÃ‚M SÃ€NG Cá»T LÃ•I (12 Ä‘iá»ƒm)</h2>

  <ol class="space-y-3 list-decimal pl-6 text-stone-700">
    <li><strong>GnRH antagonist = first-line cho general IVF</strong> (strong rec, ESHRE 2025 PMID 41732035)</li>
    <li><strong>Antagonist + GnRH trigger + freeze-all</strong> cho high responder, PCOS, tiá»n sá»­ OHSS (ESHRE 2025)</li>
    <li><strong>OCP/oestrogen pretreatment</strong> KHÃ”NG thÆ°á»ng quy cho antagonist vÃ¬ giáº£m OPR (RR 0,79, Venetis 2023 PMID 36594696)</li>
    <li><strong>Fixed Day 5/6 antagonist</strong> Æ°u tiÃªn hÆ¡n flexible (OPR cao hÆ¡n, Venetis 2023)</li>
    <li><strong>AMH hoáº·c AFC</strong> Ä‘á»ƒ dá»± Ä‘oÃ¡n high/poor response (strong rec, ESHRE 2025)</li>
    <li><strong>POSEIDON criteria</strong> thay Bologna cho poor responder classification</li>
    <li><strong>DuoStim</strong> cho poor responder, advanced age, oncology (Racca 2024 PMID 38845190)</li>
    <li><strong>Long GnRH agonist</strong> váº«n valid cho endometriosis (ultra-long 3-6 thÃ¡ng) + PGT cáº§n fresh ET</li>
    <li><strong>PPOS</strong> = lá»±a chá»n tá»‘t cho freeze-all, PGT, FP (Ata 2024 PMID 38159467)</li>
    <li><strong>Letrozole</strong> + random start cho FP ung thÆ° vÃº (Chen 2022 PMID 34656436)</li>
    <li><strong>Adjuvants</strong> (metformin, GH, testosterone, DHEA, aspirin, sildenafil) KHÃ”NG thÆ°á»ng quy (ESHRE 2025)</li>
    <li><strong>Single embryo transfer (SET)</strong> cho <35 tuá»•i, phÃ´i tá»‘t (ACOG PB 231 PMID 34011891)</li>
  </ol>
</section>
'''


# ============ ASSEMBLE ============
sections = [
    SECTION_OVERVIEW,
    SECTION_10_PROTOCOLS,
    SECTION_MECHANISM,
    SECTION_HEAD_TO_HEAD,
    SECTION_ALGORITHM,
    SECTION_6_CASES,
    SECTION_CHARTS,
    SECTION_TIPS,
    SECTION_GUIDELINES,
]


# Chart.js scripts
CHART_SCRIPTS = '''
<script>
  // Chart 1: OHSS Risk
  new Chart(document.getElementById('ohssChart'), {
    type: 'bar',
    data: {
      labels: ['General IVF', 'PCOS'],
      datasets: [{
        label: 'OHSS Risk Ratio (Antagonist vs Long Agonist)',
        data: [0.63, 0.53],
        backgroundColor: ['#a5d6a7', '#c5e0c9'],
        borderColor: ['#388e3c', '#7ba87e'],
        borderWidth: 2,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 1.0, title: { display: true, text: 'Risk Ratio (<1.0 = Antagonist tá»‘t hÆ¡n)' } }
      },
      plugins: {
        legend: { display: false },
        title: { display: true, text: 'Antagonist giáº£m OHSS Ä‘Ã¡ng ká»ƒ so vá»›i Long Agonist', font: { size: 14, weight: 'bold' } }
      }
    }
  });

  // Chart 2: Blastocyst count DuoStim vs Single
  new Chart(document.getElementById('blastocystChart'), {
    type: 'bar',
    data: {
      labels: ['DuoStim fresh', 'Single fresh'],
      datasets: [{
        label: 'Good-quality blastocysts (mean)',
        data: [4.5, 3.7],
        backgroundColor: ['#fff3cd', '#e3f2fd'],
        borderColor: ['#ffc107', '#1976d2'],
        borderWidth: 2,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: { beginAtZero: true, max: 6, title: { display: true, text: 'Number of blastocysts' } }
      },
      plugins: {
        legend: { display: false },
        title: { display: true, text: 'DuoStim cáº£i thiá»‡n sá»‘ blastocyst (mean diff +0,81)', font: { size: 14, weight: 'bold' } }
      }
    }
  });

  // Chart 3: Oocytes per protocol
  new Chart(document.getElementById('oocytesChart'), {
    type: 'bar',
    data: {
      labels: ['Natural cycle', 'Mini-IVF', 'PPOS', 'Antagonist std', 'Long Agonist', 'DuoStim (2 cycles)'],
      datasets: [{
        label: 'Sá»‘ noÃ£n MII trung bÃ¬nh',
        data: [1.5, 5.5, 10, 10, 12, 19],
        backgroundColor: ['#e0e0e0', '#bbdefb', '#fce4ec', '#c5e0c9', '#fff3cd', '#ffccbc'],
        borderColor: ['#757575', '#1976d2', '#c2185b', '#388e3c', '#ffc107', '#e64a19'],
        borderWidth: 2,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      indexAxis: 'y',
      scales: {
        x: { beginAtZero: true, max: 22, title: { display: true, text: 'Number of MII oocytes' } }
      },
      plugins: {
        legend: { display: false },
        title: { display: true, text: 'Sá»‘ noÃ£n MII theo protocol', font: { size: 14, weight: 'bold' } }
      }
    }
  });
</script>
'''


# Footer
FOOTER = '''
<footer class="text-center mt-12 py-8 text-stone-500 text-sm">
  <p>ðŸ“š BÃ i há»c y khoa: <strong>CÃ¡c phÃ¡c Ä‘á»“ kÃ­ch trá»©ng hiá»‡n Ä‘áº¡i trong ART</strong> | 25/06/2026</p>
  <p class="mt-1">BÃ¡c sÄ©: NgÆ°á»i dÃ¹ng | AI: MiniMax Mavis</p>
  <p class="text-xs mt-2">Nguá»“n: ESHRE 2025 (PMID 41732035), Venetis 2023 (PMID 36594696), Lambalk 2017 (PMID 28903472), Racca 2024 (PMID 38845190), Ata 2024 (PMID 38159467), Chen 2022 (PMID 34656436), ACOG PB 231 (PMID 34011891)</p>
</footer>
'''


main_html = '\n'.join(sections)
footer_text = 'BÃ i há»c y khoa: CÃ¡c phÃ¡c Ä‘á»“ kÃ­ch trá»©ng hiá»‡n Ä‘áº¡i trong ART | 25/06/2026 | BÃ¡c sÄ©: NgÆ°á»i dÃ¹ng | AI: MiniMax Mavis'

html = build_lesson_html(
    title=TITLE,
    header_html=HEADER,
    main_html=main_html + FOOTER,
    footer_text=footer_text,
    custom_charts=CHART_SCRIPTS,
)

write_html(html, OUTPUT_HTML)
print(f'  [HTML] Saved: {OUTPUT_HTML}')


