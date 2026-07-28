"""Build HTML visual summary cho bai hoc Bat thuong nuoc oi - 27/06/2026.
Tailwind + Mermaid + Chart.js.
"""
import sys
sys.path.insert(0, r'F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python')

from lesson_builder import build_lesson_html, write_html

TITLE = 'Bất thường nước ối — Thiểu ối & Đa ối'
DATE = '27/06/2026'
OUTPUT_HTML = r'F:\DL\mavisresearch\Bai hoc y khoa\07_Visual Summary - HTML\Visual summary - Bat thuong nuoc oi - 2026-06-27.html'

HEADER = f'''<header class="text-center py-12 mb-12 glass rounded-3xl shadow-lg">
  <div class="inline-block px-4 py-1 mb-4 rounded-full bg-blue-200 text-blue-800 text-sm font-semibold">Chuyên khoa: Siêu âm sản khoa</div>
  <h1 class="text-4xl md:text-5xl font-bold mb-4 text-stone-800">{TITLE}</h1>
  <p class="text-stone-600 text-lg">Ngày {DATE} | Cho bác sĩ sản phụ khoa / học viên sau đại học</p>
  <p class="text-sm text-stone-500 mt-2">Bác sĩ: <strong>Ngọc 🍅 🐈‍⬛</strong> | AI: <strong>MiniMax Mavis</strong></p>
  <p class="text-xs text-stone-400 mt-1">Bài số 20 — Sinh lý + Siêu âm + Guideline SMFM #46 + 6 Case thực hành</p>
</header>'''

MERMAID_CHART = '''<div class="mermaid text-center my-8">
flowchart TD
    A["Placental Insufficiency\n(Nhau thai thiểu năng)"] --> B["UA PI ↑\nDoppler ĐM rốn"]
    B --> C["Fetal Hypoxia\n(Thiếu oxy mạn)"]
    C --> D["Sympathetic Activation\n↑ Catecholamine"]
    D --> E["Blood Redistribution\n(Brain-Sparing Effect)"]
    E --> F["Não: MCA ↓PI\n(Ưu tiên tưới máu)"]
    E --> G["Thận: Renal Artery\nVASOCONSTRICTION"]
    G --> H["↓ GFR\n↓ Fetal Urine Output"]
    H --> I["OLIGOHYDRAMNIOS\n(Thiểu ối)"]
    style A fill:#ffcccc,stroke:#cc0000,color:#000
    style I fill:#ff6666,stroke:#990000,color:#fff,font-weight:bold
    style F fill:#ccffcc,stroke:#009900,color:#000
    style G fill:#ffcc99,stroke:#ff6600,color:#000
</div>'''

SECTIONS = f'''<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">TỔNG QUAN</h2>
<div class="grid md:grid-cols-4 gap-4 mt-6">
<div class="pastel-blue p-5 rounded-xl"><div class="text-3xl mb-2">💧</div><div class="font-bold text-stone-800">Nguồn gốc AF</div><div class="text-sm text-stone-600 mt-2">Nước tiểu thai (từ 16w) + Dịch phổi thai</div></div>
<div class="pastel-purple p-5 rounded-xl"><div class="text-3xl mb-2">📏</div><div class="font-bold text-stone-800">Đo AF</div><div class="text-sm text-stone-600 mt-2">AFI (4 góc) hoặc SDP (1 túi sâu nhất)</div></div>
<div class="pastel-mint p-5 rounded-xl"><div class="text-3xl mb-2">⚠️</div><div class="font-bold text-stone-800">Thiểu ối</div><div class="text-sm text-stone-600 mt-2">AFI ≤5 cm / SDP <2 cm — 0.5-5%</div></div>
<div class="pastel-pink p-5 rounded-xl"><div class="text-3xl mb-2">🌊</div><div class="font-bold text-stone-800">Đa ối</div><div class="text-sm text-stone-600 mt-2">SDP ≥8 cm / AFI ≥24 cm — 1-2%</div></div>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">ĐỊNH NGHĨA & CUT-OFF SIÊU ÂM</h2>
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead><tr class="bg-blue-100"><th class="p-3 border">Phân loại</th><th class="p-3 border">AFI (cm)</th><th class="p-3 border">SDP (cm)</th><th class="p-3 border">Ghi chú</th></tr></thead>
<tbody>
<tr><td class="p-2 border font-bold text-red-700">Đa ối nặng</td><td class="p-2 border">≥35</td><td class="p-2 border">&gt;15</td><td class="p-2 border">Tertiary center (SMFM #46 GRADE 1C)</td></tr>
<tr><td class="p-2 border text-red-600">Đa ối vừa</td><td class="p-2 border">30-34.9</td><td class="p-2 border">12-15</td><td class="p-2 border">Cân nhắc antenatal surveillance</td></tr>
<tr><td class="p-2 border text-orange-600">Đa ối nhẹ</td><td class="p-2 border">24-29.9</td><td class="p-2 border">8-11.9</td><td class="p-2 border">SMFM: KHÔNG cần surveillance</td></tr>
<tr class="bg-green-50"><td class="p-2 border font-bold text-green-700">BÌNH THƯỜNG</td><td class="p-2 border">8.1-23.9</td><td class="p-2 border">2-7.9</td><td class="p-2 border">—</td></tr>
<tr><td class="p-2 border text-yellow-600">Ranh giới</td><td class="p-2 border">5.1-8.0</td><td class="p-2 border">2</td><td class="p-2 border">Theo dõi serial, KHÔNG induction khẩn</td></tr>
<tr><td class="p-2 border text-orange-600">Thiểu ối nhẹ</td><td class="p-2 border">2.1-5.0</td><td class="p-2 border">1-1.9</td><td class="p-2 border">Cân nhắc induction ≥37w</td></tr>
<tr><td class="p-2 border font-bold text-red-700">Thiểu ối nặng</td><td class="p-2 border">≤2</td><td class="p-2 border">&lt;1</td><td class="p-2 border">INDUCTION! AOR 1.96 (Ganem 2026)</td></tr>
</tbody>
</table>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">CƠ CHẾ THIỂU ỐI TRONG FGR — BRAIN-SPARING</h2>
{MERMAID_CHART}
<p class="text-stone-700 mt-4"><strong>Trình tự thời gian:</strong> UA PI↑ (sớm nhất) → MCA PI↓ (brain-sparing) → CPR↓ + <strong>Thiểu ối</strong> (redistribution) → DV bất thường (mất bù) → BPP bất thường.<br>
<strong>Ý nghĩa:</strong> Thiểu ối trong FGR = đã ở giai đoạn redistribution đáng kể, KHÔNG phải dấu hiệu sớm.</p>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">SMFM CONSULT #46 — KHUYẾN CÁO ĐA ỐI (Tier 0, PMID 30048635)</h2>
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead><tr class="bg-purple-100"><th class="p-3 border">#</th><th class="p-3 border">Khuyến cáo</th><th class="p-3 border">GRADE</th><th class="p-3 border">Ý chính</th></tr></thead>
<tbody>
<tr><td class="p-2 border font-bold">1</td><td class="p-2 border">Định nghĩa</td><td class="p-2 border">2C</td><td class="p-2 border">SDP ≥8 cm HOẶC AFI ≥24 cm</td></tr>
<tr><td class="p-2 border font-bold">2</td><td class="p-2 border">Amnioreduction</td><td class="p-2 border"><span class="text-green-700 font-bold">1C</span></td><td class="p-2 border">CHỈ khi triệu chứng mẹ nặng</td></tr>
<tr><td class="p-2 border font-bold">3</td><td class="p-2 border">Indomethacin</td><td class="p-2 border"><span class="text-green-700 font-bold">1B</span></td><td class="p-2 border"><strong>KHÔNG</strong> dùng để giảm AF</td></tr>
<tr><td class="p-2 border font-bold">4</td><td class="p-2 border">Antenatal surveillance</td><td class="p-2 border">2C</td><td class="p-2 border">KHÔNG cần cho mild idiopathic</td></tr>
<tr><td class="p-2 border font-bold">5</td><td class="p-2 border">Timing delivery</td><td class="p-2 border"><span class="text-green-700 font-bold">1C</span></td><td class="p-2 border">Chuyển dạ tự nhiên, KHÔNG induction <39w</td></tr>
<tr><td class="p-2 border font-bold">6</td><td class="p-2 border">Nơi sinh</td><td class="p-2 border"><span class="text-green-700 font-bold">1C</span></td><td class="p-2 border">Severe → Tertiary center</td></tr>
</tbody>
</table>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">EVIDENCE CHÍNH</h2>
<div class="grid md:grid-cols-2 gap-6">
<div class="border border-blue-200 rounded-xl p-5 bg-blue-50">
<h3 class="font-bold text-blue-800 mb-2">Chauhan 2004 RCT (PMID 15343260)</h3>
<p class="text-sm"><strong>So sánh AFI vs SDP</strong> trong m-BPP<br>
n = 1,080 thai phụ nguy cơ cao ≥28w<br>
AFI chẩn đoán oligo: <strong>17%</strong><br>
SDP chẩn đoán oligo: <strong>10%</strong> (p=0.002)<br>
→ Adverse outcome KHÔNG khác biệt<br>
→ <strong>SDP = ưu tiên (SMFM/ACOG)</strong></p>
</div>
<div class="border border-red-200 rounded-xl p-5 bg-red-50">
<h3 class="font-bold text-red-800 mb-2">Ganem 2026 (PMID 41765752)</h3>
<p class="text-sm"><strong>Thiểu ối đơn độc đủ tháng</strong><br>
n = 432 ca từ 29,759 ca sinh<br>
Severe (AFI ≤2): adverse outcome <strong>22.7%</strong><br>
Mild (AFI 2.1-5.0): <strong>12.8%</strong><br>
<strong>AOR 1.96</strong> (95% CI 1.09-3.78)<br>
→ <strong>Phân tầng mức độ để cá thể hóa</strong></p>
</div>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">NGUYÊN NHÂN ĐA ỐI</h2>
<div class="grid md:grid-cols-3 gap-4 mt-4">
<div class="pastel-mint p-5 rounded-xl text-center"><div class="text-4xl mb-2">🏠</div><div class="font-bold text-stone-800 text-lg">50-60%</div><div class="text-sm text-stone-600">Vô căn (Idiopathic)<br>Thường mức độ nhẹ</div></div>
<div class="pastel-purple p-5 rounded-xl text-center"><div class="text-4xl mb-2">🍬</div><div class="font-bold text-stone-800 text-lg">15-20%</div><div class="text-sm text-stone-600">ĐTĐ mẹ (GDM/DM)<br>Osmotic diuresis thai</div></div>
<div class="pastel-pink p-5 rounded-xl text-center"><div class="text-4xl mb-2">👶</div><div class="font-bold text-stone-800 text-lg">15-20%</div><div class="text-sm text-stone-600">Bất thường thai<br>GI atresia, CNS, T21/T18</div></div>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">TÓM TẮT 3 NGUYÊN TẮC VÀNG</h2>
<div class="space-y-4">
<div class="flex items-start gap-3"><span class="text-2xl">1️⃣</span><div><strong>Luôn tìm nguyên nhân trước khi can thiệp</strong><br><span class="text-sm text-stone-600">Bất thường AF là marker — không phải chẩn đoán cuối cùng. Cần hỏi tiền sử, siêu âm giải phẫu, Doppler, xét nghiệm.</span></div></div>
<div class="flex items-start gap-3"><span class="text-2xl">2️⃣</span><div><strong>Tuổi thai quyết định hướng xử trí</strong><br><span class="text-sm text-stone-600">Cùng 1 AFI 4 cm ở 28w (expectant + corticosteroids) vs 39w (induction) — quản lý hoàn toàn khác nhau.</span></div></div>
<div class="flex items-start gap-3"><span class="text-2xl">3️⃣</span><div><strong>Phân tầng mức độ — đừng xử trí giống nhau</strong><br><span class="text-sm text-stone-600">Mild idiopathic polyhydramnios: KHÔNG can thiệp. Severe oligo (AFI ≤2): INDUCTION.</span></div></div>
</div>
</section>

<section class="glass rounded-2xl p-8 shadow-md mb-8">
<h2 class="text-3xl font-bold text-blue-700 mb-6">TÀI LIỆU THAM KHẢO CHÍNH</h2>
<div class="grid md:grid-cols-2 gap-4 text-sm">
<div class="border p-3 rounded-lg"><strong>Tier 0</strong> — SMFM Consult #46 (2019)<br>Polyhydramnios — Am J Obstet Gynecol<br>PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/30048635" class="text-blue-600">30048635</a></div>
<div class="border p-3 rounded-lg"><strong>Tier 0</strong> — ACOG PB #229 (2020)<br>Antepartum Fetal Surveillance<br>Reaffirmed 2023</div>
<div class="border p-3 rounded-lg"><strong>Tier 0</strong> — ISUOG 2023<br>Practice Guidelines: Fetal Biometry<br>Kỹ thuật đo AFI/SDP</div>
<div class="border p-3 rounded-lg"><strong>Q1</strong> — Ganem N et al. (2026)<br>J Matern Fetal Neonatal Med<br>PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/41765752" class="text-blue-600">41765752</a></div>
<div class="border p-3 rounded-lg"><strong>Q1</strong> — Chauhan SP et al. (2004)<br>AFI vs SDP RCT — Am J Obstet Gynecol<br>PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/15343260" class="text-blue-600">15343260</a></div>
<div class="border p-3 rounded-lg"><strong>Q1</strong> — Johnson JM et al. (2007)<br>3 criteria oligo — Am J Obstet Gynecol<br>PMID: <a href="https://pubmed.ncbi.nlm.nih.gov/17689653" class="text-blue-600">17689653</a></div>
</div>
</section>'''

FOOTER = 'Bác sĩ: Ngọc 🍅 🐈‍⬛ | AI: MiniMax Mavis | Bài số 20 | 27/06/2026'

html = build_lesson_html(
    title=TITLE,
    header_html=HEADER,
    main_html=SECTIONS,
    footer_text=FOOTER,
    custom_charts=''
)

write_html(html, OUTPUT_HTML)
print(f'  [HTML] Saved: {OUTPUT_HTML}')
