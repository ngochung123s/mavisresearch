"""Build .docx cho bai Endometrial Receptivity & ERA Test.

Su dung python-docx, format theo chuan bai hoc y khoa:
- Tieu de Heading 1/2/3
- Bang co border, header in dam
- Trich dan PMID ro rang
- Font: Times New Roman size 13 (body), 16 (h1), 14 (h2)
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\08_Endometrial_Receptivity_ERA\Endometrial_Receptivity_ERA_2026-06-16.docx"

doc = Document()

# Page setup
sec = doc.sections[0]
sec.top_margin = Cm(2.0)
sec.bottom_margin = Cm(2.0)
sec.left_margin = Cm(2.5)
sec.right_margin = Cm(2.0)

# Default font
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(13)
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.4

# Heading styles
for h, size, bold, color in [
    ('Heading 1', 16, True, RGBColor(0x0E, 0x4D, 0x92)),
    ('Heading 2', 14, True, RGBColor(0xBE, 0x18, 0x5D)),
    ('Heading 3', 13, True, RGBColor(0x1F, 0x29, 0x37)),
]:
    s = doc.styles[h]
    s.font.name = 'Times New Roman'
    s.font.size = Pt(size)
    s.font.bold = bold
    s.font.color.rgb = color
    s.paragraph_format.space_before = Pt(12)
    s.paragraph_format.space_after = Pt(6)
    s.paragraph_format.keep_with_next = True


def shade_cell(cell, color_hex):
    """Set background color of a cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def make_table(headers, rows, col_widths=None):
    """Create a formatted table with header shading + borders."""
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = 'Table Grid'
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # header
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = h
        for p in c.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.size = Pt(11)
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shade_cell(c, '0E4D92')
        c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    # rows
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            c = t.rows[ri + 1].cells[ci]
            c.text = str(val)
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(10.5)
            if ri % 2 == 1:
                shade_cell(c, 'F0F4FA')
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in t.rows:
                row.cells[i].width = Cm(w)
    return t


def add_p(text, bold=False, italic=False, size=None, color=None, align=None, indent=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if indent is not None:
        p.paragraph_format.left_indent = Cm(indent)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    if size:
        r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = color
    return p


def add_bullet(text, level=0):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Cm(0.6 + level * 0.6)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p


# ============= TITLE =============
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = title.add_run("ENDOMETRIAL RECEPTIVITY & ERA TEST TRONG IVF/FET")
r.font.name = 'Times New Roman'
r.font.size = Pt(18)
r.bold = True
r.font.color.rgb = RGBColor(0x0E, 0x4D, 0x92)

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run("Bai hoc y khoa chuyen sau — San phu khoa & Ho tro sinh san")
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r.italic = True
r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)

# Meta
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = meta.add_run("Ngay: 2026-06-16  |  Tac gia: MiniMax Mavis (cho BS Ngoc, VN)")
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.italic = True

doc.add_paragraph()  # spacer

# ============= 1. BOI CANH =============
doc.add_heading("1. Boi canh lam sang", level=1)
add_p("Khoang 10% benh nhan ART roi vao tinh trang Recurrent Implantation Failure (RIF) — nhieu chu ky chuyen phoi that bai mac du phoi chat luong tot (PMID 35669489). Trong so do, khoang 1/3 nguyen nhan den tu noi mac tu cung (endometrial factor) chu khong phai phoi (PMID 40221820). Day la ly do cac test danh gia endometrial receptivity ra doi, noi bat nhat la Endometrial Receptivity Analysis (ERA).")
add_p("Cau hoi lam sang dat ra:", bold=True)
add_bullet("Khi nao nen chi dinh ERA?")
add_bullet("ERA thuc su cai thien ti le live birth hay chi tang chi phi?")
add_bullet("Window of Implantation (WOI) la gi va dich chuyen the nao?")
add_bullet("FET nen chuan bi noi mac bang natural cycle hay HRT?")

# ============= 2. WOI =============
doc.add_heading("2. Co che sinh hoc — Window of Implantation (WOI)", level=1)

doc.add_heading("2.1. Chu ky noi mac tu cung", level=2)
add_p("Noi mac tu cung (endometrium) trai qua 3 giai doan moi chu ky ~28 ngay:")
make_table(
    ["Giai doan", "Ngay chu ky", "Su kien chinh", "Hormone chi phoi"],
    [
        ["Proliferative (tang sinh)", "Day 5–14", "Niem mac day len, tuyen noi mac phat trien, mach mau tang sinh", "Estrogen (E2) tu nang noan"],
        ["Secretory (che tiet)", "Day 15–28", "Tuyen noi mac cuon xoan, glycogen tich tu, decidual hoa, mach mau xoan oc", "Progesterone (P4) tu hoang the"],
        ["Menstrual (hanh kinh)", "Day 1–4", "Bong niem mac, xuat huyet", "Sup do E2 + P4"],
    ],
    col_widths=[3.5, 2.0, 6.0, 3.5]
)
add_p("Window of Implantation (WOI) = khoang thoi gian ~48–72 gio trong giai doan secretory muon (trung binh ngay 20–24 cua chu ky 28 ngay, tuong duong P+5 den P+7 trong chu ky HRT) khi noi mac san sang don phoi lam to.", italic=True)

doc.add_heading("2.2. Muc do phan tu cua receptivity", level=2)
add_p("Trong WOI, noi mac bieu hien hang tram gen theo mot chuong trinh chinh xac, goi la receptivity signature:")
add_bullet("Cytokines & chemokines: LIF (Leukemia Inhibitory Factor), IL-6, IL-11, CXCL12 — bao hieu cho phoi.")
add_bullet("Adhesion molecules: integrins (alpha-V-beta-3, alpha-1-beta-1), selectins, cadherins — bam dinh phoi vao bieu mo.")
add_bullet("Glycodelin & MUC-1: glycoprotein bao ve be mat niem mac.")
add_bullet("Pinopodes: cau truc vi nhung mao tren be mat te bao bieu mo, xuat hien vao ngay 20–21.")
add_bullet("Decidualization: te bao stromal bien doi thanh decidual cells, cung cap nang luong + dieu hoa mien dich.")
add_bullet("LncRNAs: 742 lncRNA o nguoi duoc cho la dieu hoa receptivity (PMID 38875127).")
add_bullet("MicroRNAs trong dich tu cung: co tiem nang lam biomarker xam lan toi thieu (PMID 38641194).")
add_p("Y nghia: Khi WOI dich chuyen (displacement), phoi chuyen vao \"dung ngay\" theo protocol tieu chuan co the truot mat co hoi lam to → RIF.", bold=True)

doc.add_heading("2.3. Ba dang WOI theo ERA", level=2)
make_table(
    ["Dang", "Ti le o RIF", "Dac diem", "Xu tri"],
    [
        ["Receptive (binh thuong)", "~25–50%", "WOI dung P+5", "ET theo protocol chuan"],
        ["Pre-receptive (truoc)", "~50–75% displacement", "WOI muon hon → can them progesterone 12–24h", "pET: doi gio ET"],
        ["Post-receptive (sau)", "~5%", "WOI som hon → can rut progesterone", "pET: chuyen som hon"],
        ["Early receptive (som mot phan)", "hiem", "WOI dang trung gian", "pET: ca nhoi"],
    ],
    col_widths=[3.5, 2.5, 6.0, 4.0]
)
add_p("Du lieu thuc te: 73% RIF co WOI displacement (PMID 37261585), trong do 74% pre-receptive, 24% early receptive, 2% post-receptive. Trong nghien cuu Zheng Y 2025 (PMID 40221820), 28% benh nhan RIF co WOI displacement, tat ca deu pre-receptive.", italic=True)

# ============= 3. ERA =============
doc.add_heading("3. Endometrial Receptivity Analysis (ERA) — Cong nghe", level=1)

doc.add_heading("3.1. Nguyen ly", level=2)
add_p("ERA (Igenomix, 2011 — Carlos Simon) la test transcriptomic phan tich bieu hien 238 gene trong mau sinh thiet noi mac. Su dung machine learning classifier de phan loai noi mac thanh: Receptive, Pre-receptive, Post-receptive.")

doc.add_heading("3.2. Quy trinh thuc hien", level=2)
n = 1
for s in [
    "Chuan bi noi mac bang HRT chu ky gia lap: E2 → P4 vao cung ngay mo phong WOI.",
    "Sinh thiet noi mac vao P+5 (120 gio sau khi bat dau progesterone).",
    "RNA extraction + sequencing (hoac microarray cho phien ban cu).",
    "Phan tich bioinformatic → ket qua: WOI o dau, ET nen doi bao nhieu gio.",
    "pET (personalized Embryo Transfer): chu ky FET sau, dung cung HRT nhung doi gio ET theo ERA result.",
]:
    add_bullet(f"{n}. {s}")
    n += 1

doc.add_heading("3.3. Phien ban moi", level=2)
add_bullet("ERT (Endometrial Receptivity Test) — phien ban RNA-seq + AI cua Trung Quoc (PMID 40221820).")
add_bullet("Tb-ERA (Transcriptome-based ERA) cho population Trung Quoc (PMID 35669489).")
add_bullet("miRNA-based test — dang nghien cuu, lay mau dich tu cung (PMID 38641194).")

# ============= 4. EVIDENCE =============
doc.add_heading("4. Bang chung lam sang — ERA co thuc su hieu qua?", level=1)

doc.add_heading("4.1. Bang chung TICH CUC", level=2)
make_table(
    ["Nghien cuu", "Thiet ke", "n", "Ket qua chinh", "PMID"],
    [
        ["Simon C 2020 (RCT 5 nam)", "RCT 3-arm (PET/ERA vs FET vs Fresh)", "458", "Cumulative live birth 71.2% (PET) vs 55.4% (FET) vs 48.9% (Fresh), p<0.05", "32723696"],
        ["Zheng Y 2025 (Trung Quoc)", "Prospective cohort", "85 RIF", "Clinical pregnancy 57.78% (ERT) vs 35.00% (control), p=0.036; LBR 53.33% vs 30.00%, p=0.030", "40221820"],
    ],
    col_widths=[3.0, 4.0, 1.5, 6.5, 2.0]
)

doc.add_heading("4.2. Bang chung TRUNG LAP / TIEU CUC", level=2)
make_table(
    ["Nghien cuu", "Thiet ke", "n", "Ket qua chinh", "PMID"],
    [
        ["Arian SE 2023 (meta-analysis)", "8 studies", "2,784", "LBR/ongoing pregnancy: OR 1.38 (95% CI 0.79–2.41), khong khac biet", "36414088"],
        ["Edimiris P 2023 (Duc)", "Retrospective cohort", "99 RIF", "Pregnancy rate 49% (pET) vs 44% (standard), khong khac biet y nghia", "37261585"],
    ],
    col_widths=[3.0, 4.0, 1.5, 6.5, 2.0]
)

doc.add_heading("4.3. Phan tich", level=2)
add_bullet("Trong population chung: ERA khong cai thien dang ke LBR (Arian 2023).")
add_bullet("Trong RIF specifically: ERA cho thay loi ich o mot so cohort (Zheng 2025) nhung khong o cohort khac (Edimiris 2023).")
add_bullet("Gia thuyet \"personalization\": Co the chi mot subset RIF (khoang 28% theo Zheng 2025) co WOI displacement that su, va pET chi hieu qua voi nhom nay.")
add_p("Co che giai thich vi sao ERA co the that bai o mot so ca:", bold=True)
add_bullet("Window of implantation co the thay doi theo chu ky (intra-cycle variability), khong co dinh nhu ERA gia dinh.")
add_bullet("HRT cycle co the khac ve hormonal milieu so voi natural cycle → ERA dua tren HRT co the khong chinh xac khi ap dung FET NC.")
add_bullet("pET chi doi gio ±12–24h, co the khong du de bat kip WOI that.")

# ============= 5. FET =============
doc.add_heading("5. FET Endometrial Preparation — Natural Cycle vs HRT", level=1)

doc.add_heading("5.1. Cac protocol chuan bi noi mac", level=2)
make_table(
    ["Protocol", "Cach tien hanh", "Chi dinh chinh", "Uu diem", "Nhuoc diem"],
    [
        ["True Natural Cycle (tNC)", "Theo doi LH surge tu nhien, ET sau LH+7 (blastocyst)", "Phu nu co phong noan deu", "Khong dung hormone ngoai sinh, gan gui tu nhien", "Phai monitor thuong xuyen, kho chu dong, co the huy chu ky"],
        ["Modified Natural Cycle (mNC)", "Trigger hCG khi follicle du truong, ET sau hCG+7", "tNC that bai, can chu dong hon", "Chu dong hon tNC, van co hoang the", "Van can theo doi"],
        ["HRT (Artificial Cycle)", "E2 → P4, ET sau P+5 (blastocyst)", "Khong phong noan, can flexibility", "Chu dong hoan toan, de len lich", "Tang nguy co pre-eclampsia, khong co corpus luteum"],
        ["Mild Ovarian Stimulation", "Letrozole/clomiphene + trigger", "It gap, tuy trung tam", "Co hoang the", "Ket qua khong vuot troi HRT"],
        ["P4-modified NC", "NC + them progesterone ho tro", "Toi uu hoa NC", "Linh hoat timing", "Chua co consensus"],
    ],
    col_widths=[3.0, 4.0, 3.0, 3.0, 3.0]
)

doc.add_heading("5.2. Bang chung NC vs HRT", level=2)
make_table(
    ["Nghien cuu", "Thiet ke", "n", "Ket qua", "PMID"],
    [
        ["Liu X 2025 — COMPETE RCT (Trung Quoc, don trung tam)", "RCT 1:1, NC vs HRT", "902", "LBR 54.0% (NC) vs 43.0% (HRT), RR 1.26 (1.10–1.44). Miscarriage & antepartum hemorrhage thap hon NC", "40561125"],
        ["Wei D 2026 — BMJ RCT (Trung Quoc, da trung tam)", "RCT 1:1, NC vs HRT", "4,376", "Healthy LBR 41.6% (NC) vs 40.6% (HRT), RR 1.03 (0.96–1.10), p=0.49 — khong khac biet. Pre-eclampsia thap hon NC", "41565309"],
        ["Kornilov N 2024", "Retrospective, euploid blastocyst", "723 cycles", "P4mNC vs HRT: CPR 50.2% vs 47.0%, LBR 45.0% vs 39.6%, khong khac biet", "39244908"],
        ["Hsueh YW 2023 (review)", "Literature review", "—", "NC co xu huong CPR + LBR cao hon HRT; AC tang early pregnancy loss & gestational hypertension", "37711892"],
    ],
    col_widths=[3.5, 3.5, 1.5, 6.5, 2.0]
)

doc.add_heading("5.3. Phan tich", level=2)
add_bullet("COMPETE (Liu 2025): NC vuot troi HRT (54% vs 43% LBR).")
add_bullet("Wei 2026 (BMJ): NC va HRT ngang nhau ve LBR, nhung NC giam pre-eclampsia.")
add_bullet("Ly do khac biet: COMPETE don trung tam, co the co selection bias; Wei BMJ da trung tam, n=4376 → manh hon ve generalizability.")
add_bullet("Consensus hien tai (2024–2025): NC uu tien cho phu nu co phong noan deu, nhung HRT van la lua chon hop ly neu can flexibility. Pre-eclampsia risk trong HRT cycle → can aspirin prophylaxis theo ASRM guidelines.")

# ============= 6. ESHRE 2023 =============
doc.add_heading("6. Dinh nghia RIF — ESHRE 2023 Good Practice Recommendations", level=1)
add_p("Theo ESHRE 2023 (PMID 37332387), RIF duoc dinh nghia la:", italic=True)
add_p("\"RIF describes the scenario in which the transfer of embryos considered to be viable has failed to result in a positive pregnancy test sufficiently often in a specific patient to warrant consideration of further investigation and/or intervention.\"", italic=True)
add_p("Tieu chi cu the:", bold=True)
add_bullet("≥ 3 lan chuyen phoi that bai (ket qua β-hCG am tinh)")
add_bullet("Hoac ≥ 2 lan neu phoi chat luong tot (euploid blastocyst, PGT-A binh thuong)")
add_bullet("Tuoi me can duoc tinh den")
add_bullet("Phoi phai duoc danh gia \"viable\" (hinh the tot, phat trien dung ngay)")
add_p("Khuyen cao ESHRE 2023 ve ERA:", bold=True)
add_bullet("Khong khuyen cao thuong quy ERA trong RIF do evidence chua du manh.")
add_bullet("ERA co the can nhac trong subgroup co ≥3 FET that bai voi phoi tot.")
add_bullet("Can them RCT da trung tam, sample size lon.")
add_p("Khuyen cao ESHRE 2023 ve endometrial scratch / hCG intrauterine:", bold=True)
add_bullet("Endometrial scratch: khong khuyen cao thuong quy (PMID 38982352 cho thay hCG intrauterine co the co loi).")
add_bullet("hCG intrauterine perfusion: co the cai thien CPR va implantation rate (PMID 38982352 — meta-analysis 13 studies, 2,157 benh nhan).")

# ============= 7. THUAT TOAN =============
doc.add_heading("7. Thuat toan de xuat — Khi nao dung ERA?", level=1)
add_p("Dua tren evidence hien tai (PMID 37332387, 40221820, 36414088, 37261585):")
algo_lines = [
    "Benh nhan IVF/FET:",
    "  ├── Chu ky FET dau tien",
    "  │     └──→ NC (neu ovulatory deu) hoac HRT — KHONG CAN ERA",
    "  ├── Sau 1 lan FET that bai voi phoi tot",
    "  │     └──→ Review phoi + protocol; KHONG CAN ERA ngay",
    "  ├── Sau 2 lan FET that bai (RIF tiem an)",
    "  │     ├── Kiem tra: Karyotype ca 2 vo chong, anatomy (SIS/HSG), thrombophilia",
    "  │     ├── Can nhac hCG intrauterine (PMID 38982352)",
    "  │     └──→ ERA: CAN NHAC neu phoi euploid + blastocyst tot",
    "  └── Sau ≥3 lan FET that bai (RIF xac dinh theo ESHRE 2023)",
    "        ├── Full RIF workup",
    "        ├──→ ERA: can nhac tung ca, giai thich benh nhan ve evidence mau thuan",
    "        └──→ pET neu ERA cho thay WOI displacement (pre-receptive chu yeu)",
]
for line in algo_lines:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(line)
    r.font.name = 'Consolas'
    r.font.size = Pt(10.5)
    if '└──' in line or '├──' in line:
        r.font.color.rgb = RGBColor(0x0E, 0x4D, 0x92)

# ============= 8. SO SANH =============
doc.add_heading("8. So sanh cac marker receptivity moi", level=1)
make_table(
    ["Marker", "Loai", "Uu diem", "Han che", "PMID"],
    [
        ["ERA (238 gene transcriptomic)", "RNA-based", "Da thuong mai hoa, nhieu data", "Ton kem, can sinh thiet, evidence mau thuan", "32723696, 36414088"],
        ["ERT (RNA-seq + AI)", "RNA-based + ML", "Phat hien WOI displacement 28% RIF", "Moi, can validation lon", "40221820"],
        ["Tb-ERA (Trung Quoc)", "RNA-based", "Population-specific", "Chi Trung Quoc", "35669489"],
        ["Uterine fluid miRNA", "miRNA panel", "Non-invasive", "Sensitivity chua ro", "38641194"],
        ["LncRNA (742 candidates)", "RNA-based", "Insight co che", "Chua co clinical test", "38875127"],
        ["Pinopodes (SEM)", "Morphology", "Truc quan", "Invasive, subjective", "—"],
        ["Ultrasound endometrial pattern", "Imaging", "Non-invasive, san co", "Sensitivity thap", "—"],
    ],
    col_widths=[3.5, 2.5, 3.5, 3.5, 2.0]
)

# ============= 9. CLINICAL PEARLS =============
doc.add_heading("9. Diem can nho (clinical pearls)", level=1)
pearls = [
    "Khong phai moi RIF deu do endometrial factor. Khoang 28–30% co WOI displacement that su; phan con lai do phoi, mien dich, dong mau, anatomy.",
    "ERA ton kem (~1,500–3,000 USD/test) va evidence chua nhat quan → giai thich ky cho benh nhan truoc khi chi dinh.",
    "NC uu tien HRT cho phu nu ovulatory deu (PMID 40561125) — giam pre-eclampsia risk, co the tang LBR.",
    "Pre-eclampsia risk trong HRT cycle dang ke (RR ~1.5–2 theo mot so meta-analysis) → aspirin 81–162 mg tu 12–16 tuan theo USPSTF/ACOG.",
    "Window of Implantation timing chinh xac (PMID 37711892): True NC = LH surge + 6 ngay; Modified NC = hCG + 7 ngay; HRT = P + 5 ngay.",
    "hCG intrauterine (500–1000 IU truoc ET 3–7 ngay) co the cai thien outcomes RIF (PMID 38982352), co che: kich thich decidualization, keo dai WOI, tang hCG receptors.",
    "PGT-A ket hop ERA: chi that su co y nghia khi transfer embryo euploid — neu phoi bat thuong nhiem sac the, ERA khong cuu van duoc.",
]
for pearl in pearls:
    add_bullet(pearl)

# ============= 10. TOM TAT =============
doc.add_heading("10. Tom tat & Khuyen cao thuc hanh", level=1)
doc.add_heading("10.1. Tom tat", level=2)
add_bullet("Window of Implantation (WOI) la cua so sinh hoc ~48–72h khi noi mac receptive, dieu hoa boi estrogen → progesterone va bieu hien hang tram gene.")
add_bullet("ERA test phan tich 238 gene → xac dinh WOI receptive / pre / post.")
add_bullet("Evidence ERA: tich cuc trong mot so cohort RIF (PMID 40221820), trung lap trong population chung (PMID 36414088).")
add_bullet("ESHRE 2023: khong khuyen cao ERA thuong quy; can nhac ca-le tung benh nhan.")
add_bullet("FET preparation: NC vuot troi HRT o mot so nghien cuu (PMID 40561125) nhung ngang bang o BMJ RCT 2026 (PMID 41565309); NC giam pre-eclampsia.")

doc.add_heading("10.2. Khuyen cao (theo ESHRE 2023 + ASRM 2023 + evidence 2023–2026)", level=2)
recs = [
    "FET dau tien: NC neu ovulatory deu, HRT neu can flexibility.",
    "Sau 1–2 FET that bai: Review phoi + protocol, chua can ERA.",
    "RIF xac dinh (≥3 FET that bai, phoi tot): Workup toan dien (karyotype, anatomy, immune, thrombophilia), can nhac ERA neu phoi euploid + da loai tru nguyen nhan khac.",
    "HRT cycle: can nhac aspirin 81 mg tu 12–16 tuan de giam pre-eclampsia risk.",
    "Ho tro hoang the (luteal phase support): progesterone 200–400 mg/ngay duong am dao + co the them hCG hoac GnRH agonist (neu khong co contraindication).",
]
for rec in recs:
    add_bullet(rec)

doc.add_heading("10.3. Huong nghien cuu tuong lai", level=2)
add_bullet("Non-invasive biomarker (uterine fluid miRNA, exosome) — dang nghien cuu.")
add_bullet("AI-enhanced ERA voi RNA-seq + machine learning (PMID 40221820).")
add_bullet("RCT da trung tam lon ERA vs standard trong RIF — van thieu.")

# ============= 11. TAI LIEU THAM KHAO =============
doc.add_heading("11. Tai lieu tham khao (PubMed IDs)", level=1)
refs = [
    "PMID 40221820 (2025) — Zheng Y et al. Novel endometrial receptivity test in RIF. Int J Gynaecol Obstet.",
    "PMID 40561125 (2025) — Liu X et al. COMPETE RCT: NC vs HRT for FET. PLoS Med.",
    "PMID 37711892 (2023) — Hsueh YW et al. Optimal preparation and timing of endometrium in FET. Front Endocrinol.",
    "PMID 32723696 (2020) — Simon C et al. 5-year RCT PET/ERA vs FET vs Fresh. Reprod Biomed Online.",
    "PMID 37261585 (2023) — Edimiris P et al. One center experience with pFET in RIF. J Assist Reprod Genet.",
    "PMID 38875127 (2024) — Hasanabadi HE et al. LncRNAs in endometrial receptivity. JBRA Assist Reprod.",
    "PMID 41565309 (2026) — Wei D et al. Natural ovulation vs programmed FET (BMJ RCT). BMJ.",
    "PMID 38455647 (2024) — Xu Y et al. Editorial: optimal endometrial prep. Front Endocrinol.",
    "PMID 38641194 (2024) — Rokhsartalab Azar P et al. Uterine fluid miRNAs in RIF. Clin Chim Acta.",
    "PMID 39244908 (2024) — Kornilov N et al. P4mNC preparation for FET. Reprod Biomed Online.",
    "PMID 37332387 (2023) — Cimadomo D et al. ESHRE good practice recommendations on RIF. Hum Reprod Open.",
    "PMID 38982352 (2024) — Luo X et al. Meta-analysis intrauterine hCG in RIF. BMC Pregnancy Childbirth.",
    "PMID 36414088 (2023) — Arian SE et al. ERA before FET: systematic review and meta-analysis. Fertil Steril.",
    "PMID 35669489 (2022) — Zhang WB et al. Tb-ERA in Chinese RIF patients: RCT protocol. Contemp Clin Trials Commun.",
]
for r in refs:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("• " + r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

add_p("")
add_p("Muc do chan chan (certainty of evidence):", bold=True)
add_bullet("ESHRE RIF recommendations 2023: Cao (good practice, khong phai formal guideline).")
add_bullet("ERA efficacy: Trung binh (mau thuan giua cac nghien cuu).")
add_bullet("NC vs HRT for FET: Cao — Wei BMJ 2026 la RCT lon nhat (n=4376).")
add_bullet("hCG intrauterine in RIF: Trung binh (PMID 38982352, meta-analysis nhung da so retrospective).")

# Footer
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = foot.add_run("Tai lieu duoc tao boi MiniMax Mavis, kiem chung PubMed ngay 2026-06-16. Moi quyet dinh lam sang can duoc bac si dieu tri can nhac voi benh nhan cu the.")
r.font.name = 'Times New Roman'
r.font.size = Pt(10)
r.italic = True
r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)

# Save
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
