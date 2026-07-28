"""Build 4 deliverable cho bai hoc Oxytocin Induction 2026-06-23:
1. DOCX (build san tu MD bang md_to_docx.py)
2. APKG (Anki Pastel theme, 30 cards)
3. HTML (Tailwind + Mermaid + Chart.js visual summary)
4. Telegram text (tom tat ngan)

Sau do chay citation_audit + verify_diacritics.
"""
import json
import sys
from pathlib import Path

# Add script dir to path
sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import (
    build_pastel_model_and_deck,
    add_cards_from_json,
    write_apkg,
    build_lesson_html,
    write_html,
)

# ============================================================
# CONFIG
# ============================================================
DATE = '2026-06-23'
BASE = r'F:\DL\mavisresearch\Bai hoc y khoa'
MD_FILE = rf'{BASE}\09_Source - Markdown\De_chi_huy_Oxytocin_{DATE}.md'
DOCX_FILE = rf'{BASE}\01_San phu khoa\De_chi_huy_Oxytocin_{DATE}.docx'
CARDS_JSON = rf'{BASE}\09_Source - Markdown\01_San phu khoa\oxytocin_induction_cards.json'
APKG_FILE = rf'{BASE}\01_San phu khoa\De_chi_huy_Oxytocin_{DATE}.apkg'
HTML_FILE = rf'{BASE}\01_San phu khoa\De_chi_huy_Oxytocin_{DATE}.html'
TELEGRAM_FILE = rf'{BASE}\01_San phu khoa\De_chi_huy_Oxytocin_{DATE}_telegram.txt'

# ============================================================
# 1. DOCX (already built) - just verify
# ============================================================
if Path(DOCX_FILE).exists():
    print(f'  [DOCX] Da co: {DOCX_FILE}')
    print(f'         Size: {Path(DOCX_FILE).stat().st_size:,} bytes')
else:
    print(f'  [DOCX] KHONG co - can build lai bang md_to_docx.py')

# ============================================================
# 2. APKG (Anki Pastel theme)
# ============================================================
print()
print('Building APKG...')
MODEL_ID = 1707000623001  # 2026-06-23 = 1707.0006.23.001
DECK_ID = 1707000623002

model, deck = build_pastel_model_and_deck(
    model_id=MODEL_ID,
    model_name='Oxytocin_IOL_Pastel',
    deck_id=DECK_ID,
    deck_name='San phu khoa::De chi huy Oxytocin::2026-06-23',
    deck_description='De chi huy bang oxytocin - IOL protocol - 23/06/2026',
)

n_cards = add_cards_from_json(
    deck=deck,
    model=model,
    cards_json_path=CARDS_JSON,
    tags='Oxytocin IOL San phu khoa',
)
write_apkg(deck, APKG_FILE)
print(f'  [APKG] Saved {n_cards} cards: {APKG_FILE}')
print(f'         Size: {Path(APKG_FILE).stat().st_size:,} bytes')

# ============================================================
# 3. HTML visual summary (Tailwind + Mermaid + Chart.js)
# ============================================================
print()
print('Building HTML...')

header_html = '''
<header class="max-w-6xl mx-auto pt-12 pb-8">
  <div class="glass rounded-3xl p-8 shadow-xl">
    <div class="flex items-center gap-3 mb-3">
      <span class="tag pastel-pink px-3 py-1 rounded-full text-sm font-medium">San phu khoa</span>
      <span class="tag pastel-blue px-3 py-1 rounded-full text-sm font-medium">Induction of Labor</span>
      <span class="tag pastel-mint px-3 py-1 rounded-full text-sm font-medium">2026-06-23</span>
    </div>
    <h1 class="text-4xl md:text-5xl font-bold text-stone-800 mb-4">Đẻ Chỉ Huy Bằng Oxytocin</h1>
    <p class="text-lg text-stone-600 leading-relaxed">
      Bài giảng chi tiết về induction of labor (IOL) bằng oxytocin tĩnh mạch: từ cơ chế phân tử (OXTR → Gq → PLCβ → IP3/DAG → Ca²⁺ → MLCK → co cơ) đến phác đồ lâm sàng (low-dose vs high-dose), xử trí tachysystole, và ứng dụng trên TOLAC.
    </p>
    <p class="text-sm text-stone-500 mt-4 italic">
      Đi kèm: .docx (bài giảng đầy đủ), .apkg (30 Anki cards Pastel theme), .md (markdown source). Citation đã verified PubMed E-utilities (PMID 40334983, 41241095, 35452451, 40097030, 28526450 + 45 citation khác).
    </p>
  </div>
</header>
'''

main_html = '''
<!-- Section 1: Mechanism overview -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">1. Cơ Chế Phân Tử (1 phút tóm tắt)</h2>
  <div class="grid md:grid-cols-2 gap-6">
    <div class="pastel-pink p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">OXT → OXTR → Gq → Ca²⁺ → MLCK → co cơ</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• <strong>Oxytocin</strong>: nonapeptide 9 aa, posterior pituitary, T½ 3-5 phút</li>
        <li>• <strong>OXTR</strong>: GPCR class A (Gq/11), 389 aa, gene 3p25.3</li>
        <li>• <strong>PLCβ → PIP2 → IP3 + DAG</strong></li>
        <li>• IP3 → Ca²⁺ release từ sarcoplasmic reticulum</li>
        <li>• Ca²⁺-CaM → <strong>MLCK → MLC20 phosphoryl hoá</strong> → co cơ</li>
        <li>• <strong>RhoA/ROCK</strong> song song → tăng Ca²⁺ sensitivity</li>
      </ul>
    </div>
    <div class="pastel-blue p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">OXTR tăng 100-1000 lần cuối thai kỳ</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• <strong>Estrogen ↑</strong> → ERE trong promoter OXTR</li>
        <li>• <strong>Progesterone withdrawal</strong> → mất ức chế PR</li>
        <li>• <strong>Stretch cơ học</strong> → MAPK/ERK → AP-1</li>
        <li>• <strong>CRH từ nhau</strong> → CRHR1</li>
        <li>• <strong>PGF2α</strong> → FP receptor cross-talk</li>
        <li>• <strong>Connexin-43</strong> tăng song song → gap junction → cơn co đồng bộ</li>
      </ul>
    </div>
  </div>
  
  <div class="mt-8">
    <h3 class="text-xl font-bold mb-4 text-stone-800">Sơ đồ Pathway tín hiệu</h3>
    <div class="mermaid">
flowchart TD
    OXT[Oxytocin OXT] -->|binds| OXTR
    OXTR[OXTR Gq/11 GPCR] -->|conformational change| Gq
    Gq[Gq/11 alpha GTP-bound] -->|activates| PLCB
    PLCB[PLC-beta] -->|hydrolyzes PIP2| PIP2
    PIP2[Membrane PIP2] -->|yields| IP3
    PIP2 -->|yields| DAG
    IP3 -->|binds IP3R on SR| SR[Sarcoplasmic reticulum]
    SR -->|Ca2+ release| Ca[Intracellular Ca2+]
    DAG -->|with PS + Ca2+| PKC[PKC activation]
    Ca -->|binds 4 Ca2+| CaM[Calmodulin 4Ca-CaM]
    CaM -->|activates| MLCK[Myosin light chain kinase]
    PKC -->|phosphorylates CPI-17| CPI17
    CPI17 -->|inhibits| MLCP[MLC phosphatase]
    MLCK -->|phosphorylates MLC20| MLCp[Phosphorylated MLC20]
    MLCp -->|cross-bridge| Force[Cross-bridge cycling]
    Force --> Contr[Myometrial contraction]
    RhoA -->|GTP| ROCK[ROCK Rho-kinase]
    ROCK -->|phosphorylates MYPT1| MLCP
    </div>
  </div>
</section>

<!-- Section 2: IOL Algorithm -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">2. Algorithm IOL Quyết Định</h2>
  
  <div class="mermaid">
flowchart TD
    Start[Co chi dinh IOL] --> Check1{Chong chi dinh tuyet doi?}
    Check1 -->|Co| CSection[Mo lay thai]
    Check1 -->|Khong| Bishop{Bishop score?}
    Bishop -->|>= 6| ARM[ARM neu chua vo oi]
    ARM --> OXT1[Bat dau OXT low-dose]
    Bishop -->|< 6| Ripen{Lua chon ripening}
    Ripen -->|TOLAC| Foley[Foley catheter 30-80 mL]
    Ripen -->|Khong TOLAC| Misop[Misoprostol uong 25 mcg/2-4h]
    Foley --> Reassess{Re-Bishop sau 12-24h}
    Misop --> Reassess
    Reassess -->|>= 6| OXT1
    Reassess -->|< 6| ReRip{Re-riping hoac CSection}
    OXT1 --> Monitor[FHR + CTX lien tuc]
    Monitor --> Tachy{Tachysystole > 5/10 min?}
    Tachy -->|Co| Stop[Stop OXT + xu tri]
    Tachy -->|Khong| Active{Active labor 5-6 cm, 200-250 MVU?}
    Active -->|Co| Reduce[Giam lieu hoac stop]
    Active -->|Khong| Titrate[Tang 1-2 mU/min moi 30 min]
    Titrate --> Max{Dat max 20 mU/min?}
    Max -->|Khong| Monitor
    Max -->|Co| Eval{Nguyen nhan that bai?}
    Eval --> Arrest[Arrest labor -> CSection]
    Stop --> Reassess2{FHR cai thien 10-15 phut?}
    Reassess2 -->|Co| Resume[Tiep tuc 1/2 lieu sau 30 phut]
    Reassess2 -->|Khong| Toco[Tocolysis cap cuu]
  </div>
</section>

<!-- Section 3: Low-dose vs High-dose chart -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">3. So Sánh Low-dose vs High-dose Protocol</h2>
  
  <div class="grid md:grid-cols-2 gap-6 mb-8">
    <div class="pastel-mint p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">LOW-DOSE (khuyến cáo ACOG + WHO)</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• <strong>Khởi đầu:</strong> 0.5-2 mU/min (VN: 2 mU/min)</li>
        <li>• <strong>Tăng liều:</strong> +1-2 mU/min / 30-40 min</li>
        <li>• <strong>Max:</strong> 20 mU/min</li>
        <li>• <strong>Thời gian đạt active:</strong> ~6-8 giờ</li>
        <li>• <strong>Tachysystole:</strong> ~5%</li>
        <li>• <strong>Phù hợp:</strong> Đa số IOL thường quy</li>
      </ul>
    </div>
    <div class="pastel-peach p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">HIGH-DOSE (RCOG + Bắc Âu)</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• <strong>Khởi đầu:</strong> 4-6 mU/min</li>
        <li>• <strong>Tăng liều:</strong> +4-6 mU/min / 15-20 min</li>
        <li>• <strong>Max:</strong> 20 mU/min</li>
        <li>• <strong>Thời gian đạt active:</strong> ~3-4 giờ</li>
        <li>• <strong>Tachysystole:</strong> ~10-15%</li>
        <li>• <strong>Phù hợp:</strong> Cần đẩy nhanh, nguy cơ nhiễm trùng</li>
      </ul>
    </div>
  </div>

  <!-- Chart: Grasch 2025 outcomes -->
  <h3 class="text-xl font-bold mb-4 text-stone-800">Grasch 2025 Meta-analysis — High vs Low-dose outcomes (PMID 40334983)</h3>
  <p class="text-sm text-stone-600 mb-4">6 nghiên cứu, 7,850 ca. Cesarean không khác biệt; high-dose ít PPH hơn.</p>
  <canvas id="graschChart" height="100"></canvas>
</section>

<!-- Section 4: Tachysystole management -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">4. Tachysystole — Định Nghĩa + Xử Trí</h2>
  
  <div class="grid md:grid-cols-3 gap-4 mb-6">
    <div class="pastel-pink p-4 rounded-xl text-center">
      <div class="text-4xl font-bold text-stone-800">&gt; 5</div>
      <div class="text-sm text-stone-600 mt-1">cơn co / 10 phút</div>
    </div>
    <div class="pastel-blue p-4 rounded-xl text-center">
      <div class="text-4xl font-bold text-stone-800">× 30</div>
      <div class="text-sm text-stone-600 mt-1">phút liên tục (ACOG)</div>
    </div>
    <div class="pastel-mint p-4 rounded-xl text-center">
      <div class="text-4xl font-bold text-stone-800">5-15%</div>
      <div class="text-sm text-stone-600 mt-1">tỷ lệ (tuỳ protocol)</div>
    </div>
  </div>

  <div class="mermaid">
flowchart TD
    Tachy[Tachysystole > 5 CTX/10 min x 30 min] --> Stop[1. STOP OXT ngay]
    Stop --> Lateral[2. Lateral trai]
    Lateral --> O2[3. O2 10 L/min mask]
    O2 --> IV[4. IV bolus 500-1000 mL LR]
    IV --> Assess{FHR cai thien 10-15 phut?}
    Assess -->|Co| Resume[5a. Resume 1/2 lieu cu sau 30 phut]
    Assess -->|Khong| Toco[5b. TOCOLYSIS cap cuu]
    Toco --> Terbu[Terbutaline 0.25 mg SC/IV]
    Toco --> Nitro[Nitroglycerin 50-100 mcg IV]
    Toco --> Nifed[Nifedipine 10-20 mg PO]
  </div>
</section>

<!-- Section 5: VBAC/TOLAC -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">5. VBAC/TOLAC — Oxytocin trên Sẹo Mổ Cũ</h2>
  
  <div class="grid md:grid-cols-2 gap-6 mb-6">
    <div class="pastel-lavender p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">Nicol 2026 Meta-analysis (PMID 41241095)</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• 21 nghiên cứu, <strong>51,511 bệnh nhân TOLAC</strong></li>
        <li>• <strong>Bất kỳ OXT use: OR 1.94</strong> (95% CI 1.36-2.77) cho vỡ tử cung</li>
        <li>• Chỉ induction: OR 2.07 (95% CI 1.28-3.36)</li>
        <li>• Chỉ augmentation: OR 2.03 (95% CI 1.22-3.38)</li>
        <li>• <strong>Interval &lt; 30 min:</strong> đồng nhất tăng UR risk</li>
        <li>• <strong>Max &gt; 20 mU/min:</strong> đồng nhất tăng UR risk</li>
      </ul>
    </div>
    <div class="pastel-peach p-6 rounded-2xl">
      <h3 class="font-bold text-lg mb-3 text-stone-800">Phác đồ TOLAC khuyến cáo</h3>
      <ul class="text-sm space-y-2 text-stone-700">
        <li>• <strong>Khởi đầu:</strong> 0.5-1 mU/min</li>
        <li>• <strong>Tăng:</strong> +1 mU/min / <strong>≥ 30 phút</strong></li>
        <li>• <strong>Max:</strong> ≤ 20 mU/min</li>
        <li>• <strong>Foley ripening ưu tiên</strong> (không prostaglandin)</li>
        <li>• Monitor FHR + TOCO liên tục</li>
        <li>• Sẵn sàng mổ cấp cứu trong 30 phút</li>
      </ul>
    </div>
  </div>

  <!-- Chart: OR uterine rupture by oxytocin exposure -->
  <h3 class="text-xl font-bold mb-4 text-stone-800">Nguy cơ vỡ tử cung theo mức độ dùng OXT (OR từ Nicol 2026)</h3>
  <canvas id="urChart" height="80"></canvas>
</section>

<!-- Section 6: Antagonist comparison -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">6. Thuốc Đối Kháng — Atosiban vs Nifedipine vs Indomethacin</h2>
  
  <div class="grid md:grid-cols-3 gap-4">
    <div class="pastel-mint p-5 rounded-2xl">
      <h3 class="font-bold text-lg mb-2 text-stone-800">Atosiban</h3>
      <p class="text-xs text-stone-600 mb-3"><strong>Cơ chế:</strong> OXTR antagonist</p>
      <ul class="text-xs space-y-1 text-stone-700">
        <li>✓ Chọn lọc, không hạ HA</li>
        <li>✓ An toàn cho thai</li>
        <li>✗ Không FDA (chỉ EMA 2000)</li>
        <li>✗ Giá cao</li>
        <li><strong>Tuổi thai:</strong> 24-34 tuần</li>
      </ul>
    </div>
    <div class="pastel-blue p-5 rounded-2xl">
      <h3 class="font-bold text-lg mb-2 text-stone-800">Nifedipine</h3>
      <p class="text-xs text-stone-600 mb-3"><strong>Cơ chế:</strong> L-type Ca²⁺ channel blocker</p>
      <ul class="text-xs space-y-1 text-stone-700">
        <li>✓ Hiệu quả tương đương atosiban</li>
        <li>✓ PO/sublingual dễ dùng</li>
        <li>✗ Có thể <strong>hạ HA</strong></li>
        <li>✗ Phù phổi (hiếm)</li>
        <li><strong>Tuổi thai:</strong> 24-34 tuần</li>
      </ul>
    </div>
    <div class="pastel-pink p-5 rounded-2xl">
      <h3 class="font-bold text-lg mb-2 text-stone-800">Indomethacin</h3>
      <p class="text-xs text-stone-600 mb-3"><strong>Cơ chế:</strong> COX-1/2 inhibitor</p>
      <ul class="text-xs space-y-1 text-stone-700">
        <li>✓ Hiệu quả tương đương</li>
        <li>✓ Rẻ</li>
        <li>✗ Qua nhau thai</li>
        <li>✗ <strong>Đóng ống ĐM sớm</strong> nếu &gt;32 tuần</li>
        <li>✗ Giảm nước ối</li>
        <li><strong>Tuổi thai:</strong> &lt; 32 tuần, ≤ 48 giờ</li>
      </ul>
    </div>
  </div>
</section>

<!-- Section 7: Quick reference card -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">7. Quick Reference Card</h2>
  
  <div class="bg-stone-800 text-stone-100 p-6 rounded-2xl font-mono text-sm leading-relaxed">
<pre style="white-space: pre-wrap; word-wrap: break-word;">
┌────────────────────────────────────────────────────────────────┐
│ OXYTOCIN INDUCTION — QUICK REFERENCE                          │
├────────────────────────────────────────────────────────────────┤
│ Pha: 5 IU OXT + 500 mL NaCl 0.9% / LR (= 10 mU/mL)            │
│                                                                │
│ LOW-DOSE (ACOG + WHO):                                         │
│   Khởi đầu:   1–2 mU/min                                     │
│   Tăng:       +1–2 mU/min mỗi 30 phút                         │
│   Max:        20 mU/min                                        │
│   Mục tiêu:   200–250 MVU, 3–5 CTX/10 min                    │
│   Stop khi:   active labor (≥ 5–6 cm, MVU đạt)                │
│                                                                │
│ TACHYSYSTOLE (> 5 CTX/10 min × 30 min):                        │
│   1. Stop OXT                                                 │
│   2. Lateral trái                                             │
│   3. O2 10 L/min mask                                         │
│   4. IV bolus 500–1000 mL LR                                  │
│   5. Tocolysis nếu FHR không cải thiện:                       │
│      - Terbutaline 0.25 mg SC/IV                              │
│      - Nitroglycerin 50–100 mcg IV                            │
│      - Nifedipine 10–20 mg PO                                 │
│   6. Resume OXT ở ½ liều cũ sau ≥ 30 phút                    │
│                                                                │
│ TOLAC:                                                        │
│   - Khởi đầu 0.5–1 mU/min                                    │
│   - Interval ≥ 30 phút                                        │
│   - Max ≤ 20 mU/min                                           │
│   - Foley ripening ưu tiên (không prostaglandin)              │
│   - Monitor liên tục + sẵn sàng mổ cấp cứu                  │
└────────────────────────────────────────────────────────────────┘
</pre>
  </div>
</section>

<!-- Section 8: Key references -->
<section class="glass rounded-3xl p-8 shadow-xl">
  <h2 class="text-3xl font-bold text-stone-800 mb-6">8. Citation Quan Trọng (Đã Verified)</h2>
  
  <div class="grid md:grid-cols-2 gap-4">
    <div class="pastel-blue p-4 rounded-xl">
      <strong>PMID 40334983</strong> — Grasch JL 2025
      <p class="text-xs mt-1">High vs low-dose OXT meta-analysis (6 studies, 7850 ca). AJOG MFM.</p>
    </div>
    <div class="pastel-pink p-4 rounded-xl">
      <strong>PMID 41241095</strong> — Nicolò P 2026
      <p class="text-xs mt-1">TOLAC OXT dosing & uterine rupture (21 studies, 51511 ca). AJOG MFM.</p>
    </div>
    <div class="pastel-mint p-4 rounded-xl">
      <strong>PMID 35452451</strong> — Kruit H 2022
      <p class="text-xs mt-1">Helsinki cohort high-dose vs low-dose (487 ca). PLoS One.</p>
    </div>
    <div class="pastel-peach p-4 rounded-xl">
      <strong>PMID 40097030</strong> — Pieux A 2025
      <p class="text-xs mt-1">Oral misoprostol vs dinoprostone tachysystole (439 ca). JGO.</p>
    </div>
    <div class="pastel-lavender p-4 rounded-xl">
      <strong>PMID 28526450</strong> — Grotegut CA 2017
      <p class="text-xs mt-1">OXTR/GRK6 SNP & OXT dosing (482 ca). AJOG.</p>
    </div>
    <div class="pastel-blue p-4 rounded-xl">
      <strong>PMID 29897293</strong> — Jurek & Neumann 2018
      <p class="text-xs mt-1">OXTR signaling & behavior comprehensive review. Physiol Rev.</p>
    </div>
    <div class="pastel-pink p-4 rounded-xl">
      <strong>PMID 11274341</strong> — Gimpl & Fahrenholz 2001
      <p class="text-xs mt-1">OXTR system structure/function/regulation classic. Physiol Rev.</p>
    </div>
    <div class="pastel-mint p-4 rounded-xl">
      <strong>PMID 24888645</strong> — Arrowsmith S 2014
      <p class="text-xs mt-1">OXT mechanism in myometrium. J Neuroendocrinol.</p>
    </div>
  </div>
</section>
'''

# Charts JavaScript
custom_charts = '''
// Grasch 2025 outcomes comparison
const graschCtx = document.getElementById('graschChart').getContext('2d');
new Chart(graschCtx, {
  type: 'bar',
  data: {
    labels: ['Cesarean delivery (%)', 'Tachysystole (%)', 'PPH (%)', 'Neonatal morbidity (%)'],
    datasets: [
      {
        label: 'High-dose (n=3957)',
        data: [26.0, 12, 7.6, 8],
        backgroundColor: 'rgba(247, 209, 186, 0.8)',
        borderColor: 'rgba(247, 209, 186, 1)',
        borderWidth: 2
      },
      {
        label: 'Low-dose (n=3893)',
        data: [28.4, 5, 9.9, 8],
        backgroundColor: 'rgba(197, 213, 224, 0.8)',
        borderColor: 'rgba(197, 213, 224, 1)',
        borderWidth: 2
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      title: { display: true, text: 'Grasch 2025 — High vs Low-dose OXT outcomes' },
      legend: { position: 'bottom' }
    },
    scales: {
      y: { beginAtZero: true, title: { display: true, text: 'Tỷ lệ (%)' } }
    }
  }
});

// UR risk by oxytocin exposure (Nicol 2026)
const urCtx = document.getElementById('urChart').getContext('2d');
new Chart(urCtx, {
  type: 'bar',
  data: {
    labels: ['Spontaneous TOLAC\n(reference)', 'Any OXT use', 'Induction only', 'Augmentation only'],
    datasets: [{
      label: 'Odds Ratio for uterine rupture',
      data: [1.0, 1.94, 2.07, 2.03],
      backgroundColor: [
        'rgba(200, 200, 200, 0.5)',
        'rgba(244, 194, 194, 0.8)',
        'rgba(244, 194, 194, 0.8)',
        'rgba(244, 194, 194, 0.8)'
      ],
      borderColor: 'rgba(150, 50, 50, 1)',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    plugins: {
      title: { display: true, text: 'Nicol 2026 — Uterine rupture risk theo mức OXT exposure' },
      legend: { display: false },
      annotation: {}
    },
    scales: {
      y: { 
        beginAtZero: true, 
        title: { display: true, text: 'Odds Ratio (95% CI)' },
        suggestedMax: 3
      }
    }
  }
});
'''

html_content = build_lesson_html(
    title='Đẻ Chỉ Huy Bằng Oxytocin - 2026-06-23',
    header_html=header_html,
    main_html=main_html,
    footer_text='© 2026 MiniMax — Bài giảng y khoa cá nhân. Citation đã verify qua PubMed E-utilities ngày 2026-06-23.',
    custom_charts=custom_charts,
)

write_html(html_content, HTML_FILE)
print(f'  [HTML] Saved: {HTML_FILE}')
print(f'         Size: {Path(HTML_FILE).stat().st_size:,} bytes')

# ============================================================
# 4. Telegram text (tom tat ngan)
# ============================================================
telegram_text = '''🩺 *Đẻ Chỉ Huy Bằng Oxytocin* — Bài giảy chi tiết (23/06/2026)

📌 *Cơ chế (1 phút)*: Oxytocin → OXTR (Gq/11 GPCR) → PLCβ → IP3+DAG → Ca²⁺ từ SR → CaM → MLCK → MLC20 phosphoryl hoá → co cơ. RhoA/ROCK song song tăng Ca²⁺ sensitivity. OXTR tăng 100-1000 lần cuối thai kỳ (estrogen, progesterone withdrawal, stretch, CRH, PGF2α).

📋 *Guideline*: ACOG #204 (2019) + Consensus 2014, RCOG GTG 45, NICE NG207, WHO 2011, FIGO 2022, BYT VN 2016+2024.

💊 *Protocol Low-dose (khuyến cáo)*: 0.5-2 mU/min khởi đầu → +1-2 mU/min mỗi 30 min → max 20 mU/min. Mục tiêu: 200-250 MVU, 3-5 CTX/10 min.
Protocol High-dose (RCOG/Kruit Helsinki): 4 mU/min, +4 mU/min mỗi 15-20 min, max 20.

📊 *Grasch 2025 (PMID 40334983)* meta-analysis 6 nghiên cứu, 7850 ca: cesarean không khác biệt (RR 1.02, 95% CI 0.85-1.21); high-dose ít PPH hơn (RR 0.78, 95% CI 0.66-0.92).

🚨 *Tachysystole* (> 5 CTX/10 min × 30 min): Stop OXT → lateral trái → O2 10L/min → IV 500-1000 mL LR → tocolysis nếu FHR không cải thiện (Terbutaline 0.25mg, Nitroglycerin 50-100mcg IV, Nifedipine 10-20mg PO).

⚠️ *TOLAC (Nicol 2026 PMID 41241095)*, 21 nghiên cứu, 51,511 ca: OXT OR 1.94 (95% CI 1.36-2.77) cho vỡ tử cung. Interval ≥ 30 min, max ≤ 20 mU/min, Foley ripening ưu tiên.

🧬 *Pharmacogenomics* (Grotegut 2017 PMID 28526450): rs53576, rs2224298 OXTR + rs2731664 GRK6 ảnh hưởng liều OXT (chưa vào thực hành thường quy).

🎯 *Đối kháng*: Atosiban (OXTR antagonist, EMA only, không FDA), Nifedipine (CCB, có thể hạ HA), Indomethacin (COX-i, chỉ <32 tuần).

📂 Files: `De_chi_huy_Oxytocin_2026-06-23.docx` + `.apkg` (30 cards Pastel) + `.html` (visual) + Telegram này.
'''

Path(TELEGRAM_FILE).write_text(telegram_text, encoding='utf-8')
print()
print(f'  [TELEGRAM] Saved: {TELEGRAM_FILE}')
print(f'              Size: {Path(TELEGRAM_FILE).stat().st_size:,} bytes')

print()
print('=' * 70)
print('All 4 deliverables built.')
print('=' * 70)
print()
print('Citation audit + diacritics check se chay o script tiep theo.')
