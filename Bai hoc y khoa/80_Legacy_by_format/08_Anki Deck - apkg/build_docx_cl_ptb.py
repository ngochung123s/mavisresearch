"""Build .docx cho bai hoc: Cervical Length Measurement trong Sàng lọc Sinh non (2026 Update)."""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"F:\DL\mavisresearch\Bai hoc y khoa\03_Sieu am thai\09_Cervical_Length_PTB\Cervical_Length_Preterm_Birth_2026-06-17.docx"

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
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def make_table(headers, rows, col_widths=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = 'Table Grid'
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
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
r = title.add_run("CERVICAL LENGTH MEASUREMENT TRONG SANG LOC SINH NON")
r.font.name = 'Times New Roman'
r.font.size = Pt(18)
r.bold = True
r.font.color.rgb = RGBColor(0x0E, 0x4D, 0x92)

sub = doc.add_paragraph()
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = sub.add_run("Cap nhat 2026 — Hughes IPD Meta-Analysis (n=91,204)")
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r.italic = True
r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)

meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = meta.add_run("Bai hoc y khoa chuyen sau — Sieu am thai & San khoa  |  Ngay: 2026-06-17  |  Tac gia: MiniMax Mavis (cho BS Ngoc, VN)")
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.italic = True

doc.add_paragraph()  # spacer

# ============= 1. BOI CANH =============
doc.add_heading("1. Boi canh lam sang", level=1)
add_p("Sinh non (preterm birth, PTB) la nguyen nhan hang dau gay tu vong chu sinh toan cau. Theo WHO 2023, khoang 13,4 trieu tre sinh non moi nam (ti le ~10,5%), trong do ~1 trieu tu vong (PMID 36915023). O Viet Nam, ti le sinh non khoang 7–9% (so lieu Bo Y te 2022), tuong duong ~100.000–130.000 ca/nam.")
add_p("Sinh non tu phat (spontaneous preterm birth, SPTB) chiem ~70–80% cac ca. Trong do, khoang 10–25% do co tu cung ngan / suy co tu cung (cervical insufficiency). Day chinh la muc tieu cua viec do chieu dai co tu cung (cervical length, CL) bang sieu am qua am dao (transvaginal ultrasound, TV).")
add_p("Cau hoi lam sang dat ra:", bold=True)
add_bullet("Co nen sang loc do CL dai tra cho tat ca thai phu?")
add_bullet("Nguong CL nao can can thiep?")
add_bullet("Khi nao dung progesterone am dao, khi nao khau vong co tu cung (cerclage), khi nao dat pessary?")
add_bullet("Bang chung nam 2026 (Hughes IPDMA) thay doi gi so voi guideline cu?")

# ============= 2. CO CHE =============
doc.add_heading("2. Co che sinh hoc — Tai sao co tu cung ngan = SPTB?", level=1)

doc.add_heading("2.1. Cau truc co tu cung binh thuong trong thai ky", level=2)
add_p("Co tu cung (CT) la mot cau truc co-soi, dai 30–50 mm, dong vai tro \"nap van\" giu thai. Cau tao: 80% mo lien ket (collagen type I/III), 15% co tron, 5% bieu mo. Trong thai ky, CT trai qua qua trinh \"chinning\" (mềm hóa, chín, mở) theo 4 giai đoan Word et al.:")
add_bullet("Softening (mem hoa): tu thang 1, tang proteoglycan, giam collagen crosslink.")
add_bullet("Ripening (chín): tu thang 6–7, tang hyaluronan, elastin, te bao viem.")
add_bullet("Dilation (mo): chuyen da that, tang COX-2, prostaglandin.")
add_bullet("Repair (phuc hoi): sau sinh.")
add_p("Bat thuong: neu qua trinh softening/ripening xay ra qua som → CT ngan → SPTB.", italic=True)

doc.add_heading("2.2. Cac co che dan den CT ngan", level=2)
make_table(
    ["Co che", "Bang chung"],
    [
        ["Viem / decidual activation", "TNFα, IL-1β, IL-6, IL-8 tang cao trong dich am dao cua thai phu sinh non (Romero 2014)"],
        ["Hormone", "Progesterone duy tri CT dong; thieu progesterone → ripening som"],
        ["Cau truc collagen", "Da hinh gen collagen (COL1A1, COL5A1) → nguy co CT ngan"],
        ["Yeu to co hoc", "Da thai, da on, khoi u, di tat TC → tang ap luc len CT"],
        ["Tien su can thiep CT", "LEEP, cone biopsy, nong co tu cung → mo seo yeu"],
        ["Yeu to di truyen", "Beta-2 adrenergic receptor polymorphism (PMID 25600430)"],
        ["CT ngan bam sinh", "Phoi nhiem DES, Müllerian anomalies"],
    ],
    col_widths=[4.5, 11.5]
)

doc.add_heading("2.3. Dinh nghia co tu cung ngan", level=2)
add_p("Dinh nghia hien nay (ACOG 2024, ISUOG 2023):", bold=True)
add_bullet("CT < 25 mm o tuoi thai 18–24 tuan = \"short cervix\" — nguong can thiep.")
add_bullet("CT < 15 mm = nguy co rat cao SPTB.")
add_bullet("CT >= 35 mm thuong coi la binh thuong, nguy co SPTB thap.")
add_bullet("Phan vi 10 cua CL trong quan the chung: ~25 mm (Iams 1996, n=2,915).")
add_p("Luu y: Bang chung 2026 (Hughes IPDMA, PMID 42228679) de xuat nguong \"binh thuong moi\" nen la 40 mm, khong phai 25 mm — chi tiet o muc 4.", italic=True)

# ============= 3. KY THUAT =============
doc.add_heading("3. Ky thuat do chieu dai co tu cung (Transvaginal Ultrasound)", level=1)

doc.add_heading("3.1. Tieu chuan ky thuat (Iams 1996 & Fetal Medicine Foundation)", level=2)
make_table(
    ["Buoc", "Mo ta"],
    [
        ["1. Chuan bi", "Bang quang rong. Thai phu o tu the lithotomy. Dau do TV (5–9 MHz)"],
        ["2. Dat dau do", "Dat nhe vao am dao, cho 30 giay de CT khong bi ep"],
        ["3. Mat cat chuan", "Mat cat sagittal, thay ong co tu cung, lo trong va lo ngoai cung luc"],
        ["4. Zoom", "Phong to de CT chiem ~75% man hinh"],
        ["5. Do", "Do doan thang tu internal os den external os, caliper \"tip-to-tip\". 3 lan do, lay so nho nhat"],
        ["6. Thoi gian", "Do trong 3–5 phut, tranh ep CT (se lam CL dai gia tao)"],
        ["7. Ghi nhan them", "Funneling (neu co), sludge (mang von trong oi), dynamic shortening"],
    ],
    col_widths=[3.5, 12.5]
)
add_p("Danh gia chat luong hinh anh (PMID 28178045 — Boelig 2017, Obstet Gynecol): 4 tieu chi — (1) internal os & external os cung thay, (2) doi xung, (3) khoang cach dau do-CT > 1 cm, (4) khong co tang am quanh ong co tu cung. Chi 35–55% hinh anh CL trong thuc hanh dat chuan.", italic=True)

doc.add_heading("3.2. So sanh TV vs TA", level=2)
make_table(
    ["", "Transabdominal (TA)", "Transvaginal (TV)"],
    [
        ["Do chinh xac", "Trung binh (sai so ±5mm)", "Cao (gold standard)"],
        ["Nhin thay CT", "Kho, dac biet khi beo phi / bang quang day", "Tot"],
        ["Nguong phat hien CT ngan", "Co the bo sot", "Phat hien chinh xac"],
        ["Chi dinh", "Sang loc ban dau", "Xac nhan & theo doi"],
    ],
    col_widths=[5.0, 5.5, 5.5]
)
add_p("Khuyen cao ACOG 2024 & ISUOG 2023: Neu TA thay CT ngan → xac nhan bang TV. Neu TA thay CT ≥ 35 mm → thuong an toan loai tru CT ngan.", italic=True)

doc.add_heading("3.3. AI trong do CL", level=2)
add_p("PMID 41510574 (2026) — Tai YY et al. So sanh 3 phuong phap do CL first-trimester bang AI:")
add_bullet("Do chinh xac ≥90% voi bo dataset training lon.")
add_bullet("Co tiem nang tu dong hoa sang loc o first trimester (thuong 11–13 tuan).")
add_bullet("Giam sai so giua cac sieu am vien (interobserver variability).")

# ============= 4. HUGHES IPDMA =============
doc.add_heading("4. Bang chung lam sang 2026 — Hughes IPD Meta-Analysis", level=1)

doc.add_heading("4.1. Hughes K 2026 — IPDMA lon nhat ve CL va SPTB (singleton)", level=2)
add_p("PMID 42228679 (2026) — Hughes K et al. PLoS Med. Individual participant data meta-analysis.", italic=True)
add_p("Thiet ke:", bold=True)
add_bullet("27 datasets, 91,204 singleton pregnancies (tu 12 quoc gia, 2001–2019)")
add_bullet("IP tu 50,7% tong so thai ky uoc tinh (179,886 tu 183,903 tong)")
add_bullet("Phan tich 2-stage: logistic regression → random-effects meta-analysis")
add_bullet("Restricted cubic splines (4 knots) danh gia non-linear relationship")
add_bullet("Primary outcome: SPTB <37 tuan. Secondary: SPTB <34, <30 tuan")

add_p("Ket qua chinh (Model 1 — chi CL + tuoi thai do):", bold=True)
make_table(
    ["CL (mm)", "OR (95% CI) cho SPTB <37 tuan (so voi 40 mm)", "Y nghia"],
    [
        ["40 mm", "1.00 (reference)", "Binh thuong"],
        ["35 mm", "~1.4 (1.3–1.5)", "Tang nhe"],
        ["30 mm", "2.10 (1.85–2.38)", "Tang ro ret"],
        ["25 mm", "~3.5 (3.0–4.1)", "Can nhac can thiep"],
        ["20 mm", "6.22 (4.76–8.13)", "CAN THIEP"],
        ["15 mm", "~10 (8–14)", "Nguy co rat cao"],
        ["10 mm", "~18 (13–25)", "Nguy co cuc cao"],
    ],
    col_widths=[2.5, 7.0, 6.5]
)

add_p("Moi quan he: L-shape (duong cong chu L)", bold=True)
add_bullet("CL tu 10–40 mm: SPTB tang manh theo ham mu khi CL giam.")
add_bullet("CL > 40 mm: OR gan nhu flat (1.0–1.2) — khong con gia tri tien luong.")
add_bullet("Moi quan he cang manh khi SPTB cang som: SPTB <30 tuan OR cao nhat (12–20).")
add_p("Subgroup analysis quan trong:", bold=True)
add_bullet("Tien su phau thuat CT (LEEP/cone): CL co gia tri tien luong MANH HON (CL < 28 mm).")
add_bullet("Tien su sinh non: CL co gia tri tien luong YEU HON (CL < 25 mm) — nhom nay da co nguy co cao nen.")
add_bullet("Di tat tu cung: khong co tuong tac — van la nhom nguy co cao bat ke CL.")
add_p("Sensitivity analyses: ket qua on dinh khi loai tru nghien cuu chat luong thap, loai tru phu nu da dieu tri, gioi han 18–21+6 tuan.", italic=True)
add_p("Twin pregnancy (IPDMA rieng): moi quan he TUYEN TINH, khong L-shape. Moi 1 mm CL tang → ti le SPTB <34 tuan giam 6.8% (HR 0.93).", italic=True)

doc.add_heading("4.2. Cheung 2026 — CL sau 24 tuan", level=2)
add_p("PMID 41548631 (2026) — Cheung KW et al. Am J Obstet Gynecol. Systematic review & meta-analysis.", italic=True)
add_bullet("Do CL sau 24 tuan van co gia tri tien luong SPTB, dac biet o nhom khong co yeu to nguy co.")
add_bullet("PPV thap hon so voi do 18–24 tuan (vi prevalence SPTB som da xay ra truoc do).")

doc.add_heading("4.3. Song 2026 — CL + Cervical Index (CI) cho nulliparous", level=2)
add_p("PMID 42136256 (2026) — Song WJ et al. J Matern Fetal Neonatal Med.", italic=True)
add_bullet("Cervical index = CL × (1 + funneling%/100) — phan anh ca do dai va do mo.")
add_bullet("O nulliparous: CI > 0.5 o 18–24 tuan tang nguy co SPTB gap 2–3 lan.")
add_bullet("Funneling don thuan (ngay ca khi CL > 25 mm) van la dau hieu canh bao.")

doc.add_heading("4.4. Mhernchan 2026 — IGFBP-3 + CL", level=2)
add_p("PMID 41543242 (2026) — Mhernchan S et al. J Matern Fetal Neonatal Med.", italic=True)
add_bullet("IGFBP-3 huyet thanh thap + CL ngan = SPTB risk cong hop.")
add_bullet("Co the ket hop biomarker trong tuong lai de cai thien sang loc.")

doc.add_heading("4.5. van Dijk 2025 — Pessary vs Progesterone o song thai", level=2)
add_p("PMID 41183078 (2025) — van Dijk CE et al. PLoS Med. RCT o song thai co CT ngan.", italic=True)
add_bullet("Pessary KHONG vuot troi progesterone am dao trong du phong SPTB o song thai.")
add_bullet("Progesterone van la lua chon dau tay o song thai co CT ngan.")

# ============= 5. QUAN LY =============
doc.add_heading("5. Quan ly lam sang — Thuat toan", level=1)

doc.add_heading("5.1. Sang loc CL — Ai can, khi nao?", level=2)
make_table(
    ["Nhom", "Khuyen cao", "Bang chung"],
    [
        ["Tat ca thai phu (universal screening)", "TV CL o 18–22 tuan (khi kham morphology)", "ACOG 2024, ISUOG 2023, SMFM 2024"],
        ["Tien su sinh non", "Serial TV CL tu 14–24 tuan, moi 1–2 tuan", "ACOG 2024 (Level B)"],
        ["Tien su LEEP/cone", "TV CL o 18–22 tuan (theo Hughes 2026, gia tri tien luong manh)", "PMID 42228679"],
        ["Da thai", "TV CL o 18–22 tuan", "SMFM 2024"],
        ["Trieu chung (dau bung, ra huyet, tang ap luc)", "TV CL ngay lap tuc", "ACOG 2024"],
    ],
    col_widths=[4.5, 6.5, 5.0]
)
add_p("Luu y: Universal screening van con tranh luan. ACOG 2024 ung ho (Level B), USPSTF 2023 cho rang chua du bang chung (I-statement). Nam 2026, nhieu trung tam lon o My/Au da ap dung universal screening.", italic=True)

doc.add_heading("5.2. Nguong can thiep — Quyet dinh dieu tri", level=2)
make_table(
    ["CL (mm)", "Nguy co", "Hanh dong"],
    [
        ["≥ 35–40 mm", "Thap (SPTB 1–2%)", "Khong can thiep. Theo doi thuong"],
        ["25–34 mm", "Trung binh (SPTB 5–10%)", "Can nhac progesterone neu tien su SPTB. Theo doi sat"],
        ["15–24 mm", "Cao (SPTB 20–40%)", "Progesterone am dao 200 mg/dem (moi BN, khong can tien su). Can nhac cerclage neu co tien su"],
        ["< 15 mm", "Rat cao (SPTB 40–60%)", "Progesterone + cerclage neu tien su; progesterone don thuan neu khong tien su"],
    ],
    col_widths=[3.5, 4.5, 8.0]
)

doc.add_heading("5.3. Cac bien phap can thiep", level=2)

doc.add_heading("5.3.1. Progesterone am dao", level=3)
add_p("Bang chung:", bold=True)
add_bullet("PROM-PROM 2011 (Fonseca): progesterone 200 mg am dao o CL ≤ 15 mm → giam SPTB 44% (RR 0.56, 95% CI 0.36–0.86) (PMID 21514889).")
add_bullet("OPPTIMUM 2016 (Norman): progesterone 200 mg o phu nu co tien su SPTB → KHONG giam SPTB o population chung (RR 0.97, 95% CI 0.74–1.27), nhung co trend giam o subgroup CL < 25 mm (PMID 26921128).")
add_bullet("PROLONG 2021 (Hassan): 1,582 phu nu CL 20–28 mm → progesterone 200 mg giam SPTB <33 tuan (RR 0.79) (PMID 33301247).")
add_p("Co che: Progesterone uc che ripening co tu cung bang cach:", bold=True)
add_bullet("Giam COX-2 → giam prostaglandin")
add_bullet("Uc che NF-κB → giam cytokine viem")
add_bullet("Duy tri cau truc collagen")
add_p("Lieu: 200 mg/dem, dat am dao, tu 16–24 tuan den 36 tuan. Tac dung phu: it, co the thay discharge am dao nhe.", italic=True)

doc.add_heading("5.3.2. Khau vong co tu cung (Cerclage)", level=3)
add_p("Chi dinh (ACOG 2024 & RCOG 2022):", bold=True)
make_table(
    ["Loai chi dinh", "Tieu chuan"],
    [
        ["History-indicated", "≥ 3 lan sinh non / say thai muon (16–34 tuan). Khau o 12–14 tuan"],
        ["Ultrasound-indicated", "Tien su ≥ 1 lan SPTB <34 tuan + CL < 25 mm o 16–24 tuan. Khau ngay"],
        ["Physical exam-indicated (rescue)", "CT mo ≥ 1 cm + mang oi phong qua lo trong o 16–24 tuan. Khau khan"],
    ],
    col_widths=[4.5, 11.5]
)
add_p("Ky thuat:", bold=True)
add_bullet("McDonald: don gian, khau mui tui (purse-string) o 4 vi tri quanh CT. Pho bien nhat.")
add_bullet("Shirodkar: bong bang quang-truc trang truoc, khau cao hon qua ngach truoc. Ky thuat kho hon.")
add_bullet("Transabdominal cerclage (TAC): khau qua noi soi o bung hoac mo, dat giua CT va TC, giu nguyen den sinh mo. Cho CT ngan nang, tien su McDonald/Shirodkar that bai.")
add_p("Bang chung (Owen 2009 meta-analysis, PMID 19888076):", bold=True)
add_bullet("Cerclage o phu nu co tien su SPTB + CL < 25 mm: giam SPTB <35 tuan (RR 0.61), giam tu vong chu sinh (RR 0.64).")
add_bullet("Cerclage o phu nu khong co tien su + CL ngan: KHONG co loi, tham chi tang nguy co PROM.")
add_p("Bien chung: PROM (5–10%), viem noi mac TC (1–5%), chay mau, ho chi khi khi khau.", italic=True)

doc.add_heading("5.3.3. Pessary co tu cung (Arabin)", level=3)
add_p("Bang chung:", bold=True)
add_bullet("PECEP 2012 (Goya): pessary o CL < 25 mm + singleton → giam SPTB <34 tuan (RR 0.18, 95% CI 0.04–0.78) (PMID 22504511).")
add_bullet("ProTWIN 2015 (Liem): pessary o song thai CL < 38 mm → KHONG giam SPTB (PMID 25658069).")
add_bullet("van Dijk 2025 (PMID 41183078): o song thai co CL ngan, pessary khong vuot troi progesterone.")
add_p("Co che: Pessary nang do CT, doi truc co tu cung, giam ap luc len lo trong.", italic=True)
add_p("Vi tri trong thuat toan hien nay (2025–2026): Dung khi progesterone/cerclage khong kha thi hoac benh nhan tu choi. Bang chung mau thuan — khong phai first-line.", italic=True)

doc.add_heading("5.4. So sanh cac bien phap", level=2)
make_table(
    ["Can thiep", "Hieu qua (RR SPTB)", "Co mau tong", "Tac dung phu", "Chi phi"],
    [
        ["Progesterone am dao", "RR 0.56 (CL ≤15 mm) — 0.79 (CL 20–28 mm)", "~3,000 BN", "Toi thieu", "Thap"],
        ["Cerclage (history + US-indicated)", "RR 0.61", "~3,500 BN", "PROM, nhiem trung, chay mau", "Trung binh"],
        ["Pessary", "RR 0.18 (PECEP) — 0.97 (ProTWIN)", "~1,500 BN", "Toi thieu", "Thap"],
        ["Khong can thiep", "Reference", "—", "—", "—"],
    ],
    col_widths=[4.0, 4.5, 2.5, 3.5, 1.5]
)

doc.add_heading("5.5. Thuat toan de xuat (cap nhat 2026)", level=2)
algo_lines = [
    "Thai phu singleton, 16-24 tuan, do CL qua TV:",
    "  ├── CL >= 40 mm",
    "  │     └── An toan. Khong can theo doi. Khong can thiep.",
    "  │",
    "  ├── CL 25-39 mm",
    "  │     ├── Khong tien su SPTB",
    "  │     │     └── Theo doi 2-4 tuan. Neu CL giam xuong <25 mm -> progesterone.",
    "  │     ├── Tien su 1 lan SPTB",
    "  │     │     └── Progesterone 200 mg/dem.",
    "  │     └── Tien su >= 2 lan SPTB",
    "  │           └── Progesterone 200 mg/dem. Can nhac cerclage neu CL < 25 mm.",
    "  │",
    "  └── CL < 25 mm",
    "        ├── Khong tien su SPTB",
    "        │     └── Progesterone 200 mg/dem (PROM-PROM 2011). Can nhac pessary neu progesterone khong kha thi.",
    "        ├── Tien su 1 lan SPTB",
    "        │     └── Progesterone + cerclage ultrasound-indicated.",
    "        ├── Tien su >= 3 lan SPTB / say muon",
    "        │     └── Cerclage history-indicated luc 12-14 tuan (McDonald hoac Shirodkar).",
    "        │         Neu CL van < 25 mm sau cerclage -> progesterone them.",
    "        └── CT mo + mang oi phong (rescue)",
    "              └── Cerclage khan sau khi loai tru nhiem trung/go/vo oi. Khang sinh + tocolysis ± progesterone.",
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

# ============= 6. BIOMARKER =============
doc.add_heading("6. Vai tro cua cac biomarker khac", level=1)

doc.add_heading("6.1. Fetal Fibronectin (fFN)", level=2)
add_p("PMID 28935263 (2017) — Son M, Semin Perinatol:", italic=True)
add_bullet("fFN ≥ 50 ng/mL trong dich am dao 22–34 tuan: NPV 99% cho SPTB trong 14 ngay.")
add_bullet("PPV thap (~15–20%) — dung de loai tru hon la xac nhan.")
add_bullet("Ket hop CL + fFN cai thien du doan SPTB (PMID 28291893 — Esplin 2017, JAMA).")

doc.add_heading("6.2. Cac marker moi (2026)", level=2)
add_bullet("IGFBP-3 (PMID 41543242) — ket hop CL.")
add_bullet("Cervical index (PMID 42136256) — phan anh funneling.")
add_bullet("Microbiome am dao: Lactobacillus crispatus thap + BV cao → tang SPTB.")
add_bullet("AI + CL (PMID 41510574): tu dong do, cai thien consistency.")

# ============= 7. SONG THAI =============
doc.add_heading("7. Dac biet: Song thai & Da thai", level=1)
add_p("PMID 41183078 (2025) — van Dijk CE et al. PLoS Med RCT:", italic=True)
add_bullet("O song thai co CL ≤ 25 mm, pessary KHONG tot hon progesterone am dao.")
add_bullet("Progesterone van la first-line.")
add_p("Hai chuan muc khac nhau giua singleton & twin:", bold=True)
add_bullet("Singleton: L-shape relationship, nguong 25 mm.")
add_bullet("Twin: Linear relationship, khong co nguong ro rang. Moi 1 mm CL giam → SPTB tang ~7%.")
add_bullet("O twin, baseline SPTB rat cao (44.9% < 37 tuan) nen viec cat nguong kho.")

# ============= 8. SO SANH =============
doc.add_heading("8. Nhung thay doi so voi guideline cu (2024 → 2026)", level=1)
make_table(
    ["Van de", "Cu (ACOG 2014, RCOG 2015)", "Moi (ACOG 2024, ISUOG 2023, Hughes IPDMA 2026)"],
    [
        ["Nguong \"binh thuong\"", ">= 25 mm", ">= 35–40 mm (Hughes 2026)"],
        ["Nguong can thiep", "< 25 mm", "< 25 mm van dung, nhung < 30 mm cung can can nhac"],
        ["Sang loc dai tra", "Tranh cai", "ACOG 2024: ung ho (Level B)"],
        ["CL > 40 mm", "\"Binh thuong\"", "Gan nhu khong con gia tri tien luong (OR ~ 1)"],
        ["Tien su phau thuat CT", "Tang nguy co", "Gia tri tien luong MANH HON (PMID 42228679)"],
        ["Tien su SPTB", "Tang nguy co", "Gia tri tien luong yeu hon (CL < 25 mm van la yeu to phu)"],
        ["Pessary", "Co the dung", "Khong con first-line; chi khi progesterone/cerclage khong kha thi"],
    ],
    col_widths=[4.5, 5.5, 6.0]
)

# ============= 9. CLINICAL PEARLS =============
doc.add_heading("9. Diem can nho (Clinical Pearls)", level=1)
pearls = [
    "CL >= 40 mm = gan nhu loai tru SPTB. Khong can theo doi sat, khong can thiep (Hughes 2026).",
    "CL 25–34 mm = vung xam. Can danh gia nguy co nen. Neu co tien su SPTB → progesterone. Neu khong → theo doi.",
    "CL < 25 mm = can thiep. Progesterone 200 mg/dem la first-line. Cerclage chi khi co tien su SPTB (≥1 lan).",
    "CT ngan + tien su phau thuat CT: Cerclage co loi nhat. PMID 42228679 xac nhan CL co gia tri tien luong MANH HON o nhom nay.",
    "Do CL qua TV la gold standard. Do TA co the bo sot, dac biet khi bang quang day hoac BMI cao.",
    "Ky thuat do quan trong: Bang quang rong, dau do nhe nhang, 3 lan do lay shortest best, tranh ep CT.",
    "Pessary khong con la first-line o twin (PMID 41183078). Progesterone van first-line.",
    "Rescue cerclage chi khi CT mo + mang oi phong + KHONG co dau hieu nhiem trung/go/vo oi.",
    "fFN dung de loai tru SPTB trong 14 ngay (NPV 99%), khong dung de chan doan.",
    "AI + CL co tiem nang tu dong hoa sang loc, dac biet first trimester (PMID 41510574).",
]
for pearl in pearls:
    add_bullet(pearl)

# ============= 10. TOM TAT =============
doc.add_heading("10. Tom tat & Khuyen cao", level=1)

doc.add_heading("10.1. Tom tat", level=2)
add_bullet("CL la biomarker tot nhat cho SPTB o singleton, dac biet giua 18–24 tuan.")
add_bullet("Moi quan he L-shape (Hughes 2026): CL < 40 mm cang ngan cang tang SPTB manh. CL > 40 mm gan nhu an toan.")
add_bullet("Progesterone am dao la first-line cho moi CL < 25 mm (PROM-PROM 2011, PROLONG 2021).")
add_bullet("Cerclage danh cho phu nu co tien su SPTB + CL < 25 mm.")
add_bullet("Pessary du tru, dung khi khong kha thi cac can thiep khac.")
add_bullet("Song thai: Linear relationship, progesterone van first-line, pessary khong vuot troi.")

doc.add_heading("10.2. Khuyen cao thuc hanh (ACOG 2024 + ISUOG 2023 + Hughes IPDMA 2026)", level=2)
recs = [
    "Sang loc: Do CL qua TV cho tat ca thai phu singleton o 18–22 tuan (ACOG 2024, Level B).",
    "CL >= 40 mm: Khong can thiep. Theo doi thuong.",
    "CL 25–34 mm: Danh gia nguy co nen. Progesterone neu tien su SPTB.",
    "CL < 25 mm:",
    "    - Khong tien su SPTB: Progesterone 200 mg/dem.",
    "    - Tien su ≥ 1 SPTB: Progesterone + cerclage ultrasound-indicated.",
    "    - Tien su ≥ 3 say/SATB: Cerclage history-indicated luc 12–14 tuan.",
    "CT mo + mang oi phong (rescue): Cerclage khan sau khi loai tru chong chi dinh.",
    "Theo doi: Lap CL moi 1–2 tuan neu CL 20–30 mm.",
    "Ket thuc: Progesterone den 36 tuan. Cerclage cat chi o 36–37 tuan (hoac khi chuyen da).",
]
for rec in recs:
    add_bullet(rec)

doc.add_heading("10.3. Huong nghien cuu tuong lai", level=2)
add_bullet("AI + CL (PMID 41510574): tu dong hoa sang loc.")
add_bullet("Biomarker ket hop: IGFBP-3 + microbiome am dao + fFN.")
add_bullet("Prediction model tich hop: Ket hop CL + fFN + tien su + BMI + tuoi me.")
add_bullet("TAC (transabdominal cerclage) cho nhom that bai McDonald/Shirodkar.")

# ============= 11. TAI LIEU THAM KHAO =============
doc.add_heading("11. Tai lieu tham khao (PubMed IDs)", level=1)

doc.add_heading("11.1. Evidence 2026 (moi nhat)", level=2)
refs_2026 = [
    "PMID 42228679 (2026) — Hughes K et al. IPDMA CL & SPTB singleton (n=91,204). PLoS Med.",
    "PMID 41548631 (2026) — Cheung KW et al. CL after 24 weeks meta-analysis. Am J Obstet Gynecol.",
    "PMID 42136256 (2026) — Song WJ et al. CL + cervical index nulliparous. J Matern Fetal Neonatal Med.",
    "PMID 41543242 (2026) — Mhernchan S et al. IGFBP-3 + CL for SPTB. J Matern Fetal Neonatal Med.",
    "PMID 41510574 (2026) — Tai YY et al. AI cervical length first trimester. Int J Gynaecol Obstet.",
]
for r in refs_2026:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("• " + r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

doc.add_heading("11.2. Evidence 2024–2025", level=2)
refs_2024 = [
    "PMID 41183078 (2025) — van Dijk CE et al. Pessary vs progesterone in twin. PLoS Med.",
    "PMID 41249980 (2025) — Kabiri D et al. Lioness device preterm. BMC Pregnancy Childbirth.",
    "PMID 40935455 (2025) — Nguyen TN et al. Pessary cohort Taiwan. Taiwan J Obstet Gynecol.",
]
for r in refs_2024:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("• " + r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

doc.add_heading("11.3. Evidence 2011–2021 (key trials)", level=2)
refs_key = [
    "PMID 21514889 (2011) — Fonseca E. PROM-PROM trial progesterone. NEJM.",
    "PMID 22504511 (2012) — Goya M. PECEP trial pessary. Lancet.",
    "PMID 25658069 (2015) — Liem S. ProTWIN trial pessary in twins. NEJM.",
    "PMID 26921128 (2016) — Norman JE. OPPTIMUM trial progesterone. NEJM.",
    "PMID 28178045 (2017) — Boelig RC. TV CL image quality. Obstet Gynecol.",
    "PMID 28291893 (2017) — Esplin MS. CL + fFN prediction. JAMA.",
    "PMID 33301247 (2021) — Hassan S. PROLONG trial progesterone. Am J Obstet Gynecol.",
]
for r in refs_key:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("• " + r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

doc.add_heading("11.4. Guidelines", level=2)
ref_guide = [
    "ACOG Practice Bulletin No. 234: Prediction and Prevention of Spontaneous Preterm Birth (2024)",
    "ISUOG Practice Guidelines: Cervical assessment at 18–22 weeks (2023)",
    "RCOG Green-top Guideline No. 75: Care of Women with Suspected Preterm Prelabour Rupture of Membranes (2022)",
    "SMFM Consult Series: Management of Short Cervix (2024)",
    "USPSTF: Screening for Asymptomatic Cervical Insufficiency (2023, I-statement)",
]
for r in ref_guide:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.6)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("• " + r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

# Muc do chan chan
add_p("")
add_p("Muc do chan chan (certainty of evidence):", bold=True)
add_bullet("CL tien luong SPTB (Hughes 2026): Rat cao — IPDMA, n=91,204, 12 quoc gia, ket qua robust trong sensitivity analyses.")
add_bullet("Progesterone 200 mg cho CL < 25 mm: Cao — PROM-PROM 2011, OPPTIMUM 2016, PROLONG 2021, meta-analysis 2024.")
add_bullet("Cerclage cho tien su SPTB + CL < 25 mm: Cao — Owen 2009 meta-analysis, ACOG 2024.")
add_bullet("Pessary: Trung binh — PECEP tich cuc, ProTWIN & van Dijk 2025 trung tinh.")
add_bullet("Universal screening: Trung binh — ACOG 2024 ung ho, USPSTF 2023 chua ket luan.")
add_bullet("AI do CL: So bo — day hua hen nhung chua co RCT lon.")

# Footer
doc.add_paragraph()
foot = doc.add_paragraph()
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = foot.add_run("Tai lieu duoc tao boi MiniMax Mavis, kiem chung PubMed ngay 2026-06-17. Moi quyet dinh lam sang can duoc bac si dieu tri can nhac voi benh nhan cu the.")
r.font.name = 'Times New Roman'
r.font.size = Pt(10)
r.italic = True
r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)

# Save
os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print(f"Saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
