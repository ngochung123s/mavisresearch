"""Build full lesson: docx + anki apkg + html visual summary.
Topic: ICSI (Intracytoplasmic Sperm Injection) trong IVF - 2026-06-20.

Refactored: dung shared utilities tu lesson_builder.py.
"""
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from lesson_builder import (
    set_cell_bg, set_cell_border, style_header, style_first_col,
    add_bullets, add_numbered, fill_table,
    build_pastel_model_and_deck, add_cards_from_json, write_apkg,
    build_lesson_html, write_html,
)

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
LESSON_DIR = ROOT / "02_Ho tro sinh san ART" / "10_ICSI"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "02_Ho tro sinh san ART" / "10_ICSI"
DATE = "2026-06-20"

DOCX_OUT = LESSON_DIR / f"ICSI trong IVF - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - ICSI trong IVF 20 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - ICSI trong IVF - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "icsi_cards.json"

# ============================================================
# DOCX BUILDER
# ============================================================
def build_docx():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    # TITLE
    title = doc.add_heading('ICSI (INTRACYTOPLASMIC SPERM INJECTION) TRONG IVF', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bai hoc ngay {DATE} - Ho tro sinh san (ART)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TONG QUAN - VI SAO BAI NAY QUAN TRONG?', 1)
    doc.add_paragraph(
        'ICSI (Intracytoplasmic Sperm Injection) ra doi nam 1992 boi Palermo, ban dau chi dinh cho vo sinh nam nang '
        '(severe male factor). Den nay, ICSI da tro thanh phuong phap thu tinh pho bien nhat trong ART tren toan the gioi, '
        'chiem ~70-80% cycle o nhieu nuoc (My, chau Au, chau A).'
    )
    doc.add_paragraph('Boi canh lam sang:')
    add_bullets(doc, [
        'Ty le ICSI tang tu < 20% (2000) len > 70% (2020) du ty le vo sinh nam nang khong tang tuong ung.',
        '2 RCT lon nam 2024 (Lancet, PMID 38330980) va 2025 (Nat Med, PMID 40217077) cho thay: ICSI KHONG cai thien live birth rate so voi conventional IVF o non-severe male factor.',
        'Esteves 2018 (Nat Rev Urol, PMID 29967387) canh bao ve risks o offspring (di tat bam sinh, epigenetic disorders, cancer).',
    ])
    doc.add_paragraph('Bac si ART can nam ro ICSI vi:')
    add_bullets(doc, [
        'Quyet dinh ICSI vs IVF la quyet dinh thuong gap nhat trong lab - anh huong truc tiep den outcome + cost.',
        'Chi dinh ICSI ngay cang bi thu hep sau cac RCT 2024-2025.',
        'Risks o offspring can tu van cho benh nhan.',
        'Sperm DNA damage co the la chi dinh moi noi cho ICSI.',
        'Embryology lab can nam ky thuat chuan.',
    ])

    # 1. CO CHE KY THUAT
    doc.add_heading('1. CO CHE KY THUAT - ICSI LAM GI KHAC CONVENTIONAL IVF?', 1)
    doc.add_heading('1.1. Conventional IVF (c-IVF)', 2)
    doc.add_paragraph(
        'Trong c-IVF, noan va tinh trung duoc cho gap nhau trong dia culture:\n'
        '- ~50,000-100,000 tinh trung / noan.\n'
        '- Tinh trung tu boi, tu xam nhap qua zona pellucida (ZP) va mang noan (oolemma).\n'
        '- Qua trinh thu tinh tu nhien phu thuoc vao: kha nang di dong (motility), kha nang xam nhap ZP (acrosome reaction binh thuong), so luong tinh trung du de canh tranh.'
    )
    doc.add_heading('1.2. ICSI - Bypass hoan toan qua trinh tu nhien', 2)
    doc.add_paragraph('ICSI tiem truc tiep 1 tinh trung vao bao tuong noan (ooplasm) bang micropipette duoi kinh hien vi thao tac (micromanipulator).')
    doc.add_paragraph('Cac buoc chinh:')
    add_bullets(doc, [
        'Oocyte denudation: Noan sau choc hut du u voi hyaluronidase (80 IU/mL, ~30-60 giay), strip nhe nhang de loai bo cumulus cells + corona radiata. Kiem tra do truong thanh (MII co cuc cau = san sang).',
        'Sperm preparation: Lua chon tinh trung qua density gradient hoac swim-up. Chon 1 tinh trung tot nhat co the (morphology binh thuong, motility tot).',
        'Sperm immobilization: Dung micropipette ICSI ep nhe duoi tinh trung de mat kha nang di dong, tranh tu xoay trong noan.',
        'Aspiration: Hut tinh trung vao pipette ICSI voi dau tu (blunt tip).',
        'Oocyte positioning: Giu noan bang holding pipette, cuc cau o vi tri 6h hoac 12h.',
        'Injection: Xuyen pipette ICSI qua ZP + oolemma o vi tri 3h (doi dien cuc cau). Tiem tinh trung vao ooplasm voi luong nho (~1-2 pL cytoplasm).',
        'Sau tiem: Rua + nuoi trong cleavage medium. Kiem tra fertilization sau 16-18 gio (2PN + 2 polar body = thu tinh binh thuong).',
    ])
    doc.add_heading('1.3. So sanh ky thuat c-IVF vs ICSI', 2)
    t1 = doc.add_table(rows=9, cols=3)
    fill_table(t1,
        ['Tieu chi', 'c-IVF', 'ICSI'],
        [
            ('So tinh trung/noan', '50,000-100,000', '1 (chon loc)'),
            ('Can motility binh thuong', 'Co (bat buoc)', 'Khong (ep nhan tao)'),
            ('Yeu cau acrosome reaction', 'Co', 'Khong'),
            ('Can micromanipulator', 'Khong', 'Co (bat buoc)'),
            ('Chi phi them', '0', '+ ~$500-2000/cycle'),
            ('Thoi gian embryologist', 'Ngan', 'Dai (20-30 phut/noan)'),
            ('Ty le fertilization', '60-70%', '70-80%'),
            ('Ty le thu tinh that bai (FFR)', '5-10%', '1-3%'),
        ])
    doc.add_paragraph()

    # 2. CHI DINH
    doc.add_heading('2. CHI DINH ICSI - KHI NAO NEN DUNG?', 1)
    doc.add_paragraph('Theo ASRM Practice Committee va ESHRE guidelines (Esteves 2018, PMID 29967387):')
    doc.add_heading('2.1. Chi dinh CHAC CHAN (Strong indications) - ICSI duoc khuyen cao', 2)
    t2 = doc.add_table(rows=7, cols=3)
    fill_table(t2,
        ['Chi dinh', 'Nguong', 'Ghi chu'],
        [
            ('Severe oligozoospermia', '< 5-10 trieu/mL', 'WHO 2021 nguong thap hon'),
            ('Cryptozoospermia', 'Tinh trung chi thay trong pellet sau centrifugation', ''),
            ('Azoospermia (NOA, OA)', 'Tinh trung tu TESE/MESA/PESA', 'BAT BUOC ICSI'),
            ('Asthenozoospermia nang', 'Motility < 5-10%', ''),
            ('Teratozoospermia nang', 'Morphology binh thuong < 1% (strict Kruger)', ''),
            ('Globozoospermia', '100% tinh trung round-headed, khong acrosome', 'ICSI lua chon duy nhat'),
        ])
    doc.add_paragraph()

    doc.add_heading('2.2. Tiep theo - cac chi dinh chac chan khac', 2)
    add_bullets(doc, [
        'Tien su fertilization failure voi c-IVF: FFR truoc do (>50% noan khong thu tinh) -> tranh tai dien.',
        'PGT/PGT-A: can tranh DNA tinh trung bam ngoai ZP, giam contamination.',
        'Frozen oocyte: sau warming - ICSI uu tien vi ZP cung hon.',
        'In vitro maturation (IVM): noan chua truong thanh.',
        'Sperm DNA fragmentation cao: DFI > 30% - evidence moi, con tranh cai.',
    ])

    doc.add_heading('2.3. Chi dinh CAN NHAC (Relative indications)', 2)
    t3 = doc.add_table(rows=5, cols=3)
    fill_table(t3,
        ['Tinh huong', 'Bang chung', 'Ghi chu'],
        [
            ('Unexplained infertility', 'Khong co RCT lon', 'Wang 2024 RCT cho thay ICSI khong cai thien'),
            ('Borderline male factor', 'Oligo-astheno-teratozoospermia nhe', 'Berntsen 2025 RCT cho thay khong cai thien'),
            ('Tuoi me cao', 'Khong phai chi dinh', 'Lien quan chat luong noan, khong phai tinh trung'),
            ('So noan it (< 4)', 'Tranh cai', 'Mot so lab uu tien ICSI de tranh FFR'),
        ])
    doc.add_paragraph()
    doc.add_heading('2.4. Chi dinh KHONG NEN (Iatrogenic ICSI)', 2)
    doc.add_paragraph('Tinh huong KHONG nen dung ICSI:')
    add_bullets(doc, [
        'Non-severe male factor (count binh thuong, motility > 10%, morphology > 4%).',
        'IVF cycle dau tien khong co yeu to nguy co.',
        'Khi khong co ly do cu the.',
    ])
    doc.add_paragraph('=> Bac si can tu van ro cho benh nhan rang ICSI khong phai luc nao cung tot hon - no chi tot hon khi co chi dinh dung.').runs[0].bold = True

    # 3. EVIDENCE 2024-2025
    doc.add_heading('3. EVIDENCE MOI NHAT: ICSI vs CONVENTIONAL IVF (2024-2025)', 1)
    doc.add_heading('3.1. Wang Y. et al. 2024 - Lancet RCT (PMID 38330980)', 2)
    doc.add_paragraph('Thiet ke: Investigator-initiated, multicentre, open-label RCT, 10 trung tam tai Trung Quoc.')
    doc.add_paragraph('Dan so:').runs[0].bold = True
    add_bullets(doc, [
        'Couples infertility voi non-severe male factor, khong co tien su poor fertilization.',
        'Sang loc 3,879 couples, randomized 2,387 (1,184 ICSI vs 1,203 c-IVF).',
        'Sau loai tru: 1,154 ICSI + 1,175 c-IVF trong phan tich chinh (intention-to-treat).',
    ])
    doc.add_paragraph('Primary outcome: Live birth sau first embryo transfer.')
    doc.add_paragraph('Ket qua:').runs[0].bold = True
    add_bullets(doc, [
        'ICSI: 33.8% (390/1,154) live birth.',
        'c-IVF: 36.6% (430/1,175) live birth.',
        'Adjusted RR = 0.92 (95% CI 0.83-1.03), p = 0.16 - KHONG CO SU KHAC BIET.',
        'Neonatal death: 2 (0.2%) ICSI vs 1 (0.1%) c-IVF (khong dang ke).',
    ])
    doc.add_paragraph('Ket luan tac gia: "In couples with infertility with non-severe male factor, ICSI did not improve live birth rate compared with conventional IVF. Given that ICSI is an invasive procedure associated with additional costs and potential increased risks to offspring health, routine use is not recommended in this population."').runs[0].italic = True

    doc.add_heading('3.2. Berntsen S. et al. 2025 - Nature Medicine RCT (INVICSI study, PMID 40217077)', 2)
    doc.add_paragraph('Thiet ke: Open-label, multicentre RCT, 6 phong kham cong tai Dan Mach.')
    doc.add_paragraph('Dan so:').runs[0].bold = True
    add_bullets(doc, [
        '824 phu nu lam IVF cycle dau tien, khong co severe male factor.',
        'Randomized: 414 ICSI vs 410 c-IVF.',
        'Thoi gian: 11/2019 - 12/2022.',
    ])
    doc.add_paragraph('Primary outcome: Cumulative Live Birth Rate (CLBR) - ti le sinh con song tich luy qua multiple cycles.')
    doc.add_paragraph('Ket qua:').runs[0].bold = True
    add_bullets(doc, [
        'ICSI: 43.2% (179/414) CLBR.',
        'c-IVF: 47.3% (193/408) CLBR.',
        'RR = 0.91 (95% CI 0.79-1.06) - KHONG CO SU KHAC BIET.',
        '(Luu y: 2 phu nu c-IVF bi loai sau randomization, n=408 thay vi 410.)',
    ])
    doc.add_paragraph('Ket luan tac gia: "ICSI does not improve CLBR compared to c-IVF and support c-IVF as the preferred first-line treatment for patients with normal or nonseverely decreased sperm quality. ICSI should be reserved for severe male factor infertility."').runs[0].italic = True

    doc.add_heading('3.3. Y nghia lam sang cua 2 RCT nay', 2)
    doc.add_paragraph('Cung thong diep tu 2 RCT lon o 2 chau luc (Trung Quoc + Dan Mach):')
    add_bullets(doc, [
        'ICSI KHONG cai thien live birth o non-severe male factor.',
        'ICSI co cost them (embryologist time, equipment).',
        'ICSI co risks o offspring (se noi o phan 5).',
        '=> c-IVF nen la first-line o non-severe male factor.',
    ])
    doc.add_paragraph('Truoc 2024, nhieu guideline van khuyen cao ICSI "co the can nhac" o borderline cases - sau 2 RCT nay, xu huong thu hep chi dinh ICSI.').runs[0].bold = True

    # 4. SPERM DNA DAMAGE
    doc.add_heading('4. SPERM DNA DAMAGE - KHI NAO ICSI CO LOI?', 1)
    doc.add_heading('4.1. Co che', 2)
    doc.add_paragraph('Sperm DNA fragmentation (SDF) tang trong:')
    add_bullets(doc, [
        'Varicocele, nhiem trung sinh duc, sot cao.',
        'Loi song: hut thuoc, ruou, stress oxy hoa.',
        'Tuoi cha cao (> 50).',
        'Idiopathic.',
    ])
    doc.add_paragraph('Anh huong cua SDF:')
    add_bullets(doc, [
        'Giam kha nang thu tinh.',
        'Tang ti le say thai.',
        'Co the anh huong phat trien phoi.',
        'Tang nguy co di tat bam sinh o con.',
    ])

    doc.add_heading('4.2. Evidence tu Ribas-Maynou 2021 (PMID 33644978)', 2)
    doc.add_paragraph('Meta-analysis lon nhat ve sperm DNA damage + ART outcomes:')
    add_bullets(doc, [
        '78 nghien cuu, 25,639 IVF/ICSI cycles.',
        '32 nghien cuu + 12,380 cycles trong meta-analysis dinh luong.',
    ])
    t4 = doc.add_table(rows=4, cols=3)
    fill_table(t4,
        ['Outcome', 'IVF (SDF cao vs thap)', 'ICSI (SDF cao vs thap)'],
        [
            ('Implantation rate', 'RR 0.68 (0.52-0.89) giam ro', 'RR 0.79 (0.60-1.04) - khong y nghia'),
            ('Pregnancy rate', 'RR 0.72 (0.55-0.95) giam ro', 'RR 0.89 (0.78-1.02) - khong y nghia'),
            ('Live birth rate', 'RR 0.48 (0.22-1.02) - xu huong giam', 'RR 0.92 (0.67-1.27) - khong y nghia'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Y nghia:')
    add_bullets(doc, [
        'O c-IVF: SDF cao lam giam RO RET implantation va pregnancy rate.',
        'O ICSI: SDF cao KHONG anh huong dang ke.',
        '=> ICSI co the "buffer" anh huong cua DNA damage vi bypass qua trinh tu nhien (tinh trung bi DNA damage van co the thu tinh noan khi tiem truc tiep).',
    ])

    doc.add_heading('4.3. Tranh cai ve DNA testing thuong quy', 2)
    add_bullets(doc, [
        'ESHRE: co the test, co gia tri tien doan.',
        'ASRM: KHONG khuyen cao test thuong quy (vi chua co intervention ro rang neu SDF cao).',
        'Practical approach: Test SDF khi: vo sinh khong ro nguyen nhan + SA binh thuong, tien su say thai lien tiep, truoc khi quyet dinh ICSI vs IVF o borderline male factor.',
    ])

    # 5. OFFSPRING SAFETY
    doc.add_heading('5. OFFSPRING SAFETY - ICSI CO AN TOAN?', 1)
    doc.add_heading('5.1. Canh bao tu Esteves 2018 (PMID 29967387)', 2)
    doc.add_paragraph('Bai tong quan quan trong nhat ve ICSI offspring (Nat Rev Urol). Tong hop 25 nam du lieu:')
    doc.add_paragraph('Risks tang o ICSI con so voi natural conception:')
    add_bullets(doc, [
        'Congenital malformations (di tat bam sinh): tang ~1.5-2 lan mot so he (tim, co xuong, tiet nieu-sinh duc).',
        'Epigenetic disorders (roi loan imprinting): hiem nhung nghiem trong (Beckwith-Wiedemann, Angelman).',
        'Chromosomal abnormalities: chu yeu do di truyen tu cha (Y chromosome, balanced translocation).',
        'Subfertility o the he sau: con trai cua ICSI co the thua huong Y microdeletion.',
        'Cancer o tre: tang nhe (dac biet hepatoblastoma, leukemia - can data them).',
        'Delayed psychological/neurological development: tranh cai.',
        'Impaired cardiometabolic profile: tang huyet ap, roi loan lipid (data moi).',
    ])
    doc.add_heading('5.2. Nhung can hieu confounding', 2)
    doc.add_paragraph('Esteves 2018 cung canh bao khong the tach biet hoan toan:')
    add_bullets(doc, [
        'Subfertility cua CHA co the la yeu to chinh (gene di truyen, epigenetic bat thuong).',
        'Subfertility cua ME (tuoi cao, PCOS, endometriosis) cung anh huong.',
        'Yeu to moi truong trong ART (culture medium, manipulation).',
    ])
    doc.add_paragraph('=> Khi tu van benh nhan, can noi ro: risks tang nhe, khong co nghia ICSI "nguy hiem" - loi ich khi co chi dinh dung van vuot troi.').runs[0].bold = True

    doc.add_heading('5.3. Giam thieu risks', 2)
    add_bullets(doc, [
        'Chi dinh chat che ICSI (khong lam dung).',
        'Preimplantation Genetic Testing (PGT) khi co chi dinh.',
        'Sperm selection cai tien: PICSI (hyaluronic acid), MACS (magnetic-activated cell sorting), microfluidic.',
        'Dieu tri nguyen nhan truoc ICSI (varicocele repair, antioxidants).',
    ])

    # 6. UNG DUNG LAM SANG
    doc.add_heading('6. TONG HOP UNG DUNG LAM SANG', 1)
    doc.add_heading('6.1. Bang quyet dinh ICSI vs c-IVF', 2)
    t5 = doc.add_table(rows=10, cols=3)
    fill_table(t5,
        ['Tinh huong', 'Khuyen cao', 'Bang chung chinh'],
        [
            ('Severe male factor (count < 5M, motility < 5%, morphology < 1% Kruger)', 'ICSI', 'Esteves 2018, ASRM, ESHRE'),
            ('Azoospermia (TESE/MESA)', 'ICSI (bat buoc)', 'Esteves 2018'),
            ('Globozoospermia', 'ICSI (lua chon duy nhat)', ''),
            ('Tien su fertilization failure voi c-IVF', 'ICSI', ''),
            ('PGT-A / PGT-M can lam', 'ICSI', 'Tranh contamination'),
            ('Frozen oocyte sau warming', 'ICSI uu tien', ''),
            ('Sperm DNA fragmentation cao (>30%)', 'ICSI (xem xet)', 'Ribas-Maynou 2021'),
            ('Non-severe male factor', 'c-IVF', 'Wang 2024 (Lancet), Berntsen 2025 (Nat Med)'),
            ('Borderline male factor', 'c-IVF truoc, ICSI neu FFR', 'Wang 2024, Berntsen 2025'),
        ])
    doc.add_paragraph()

    doc.add_heading('6.2. Algorithm quyet dinh ICSI vs c-IVF', 2)
    doc.add_paragraph(
        'Danh gia SA (sperm analysis) + tien su\n'
        '   V\n'
        '+----------------------------------+\n'
        '| Severe male factor?              | -> ICSI (Esteves 2018)\n'
        '| - Count < 5M                     |\n'
        '| - Motility < 5%                  |\n'
        '| - Morphology < 1%                |\n'
        '| - Globozoospermia                |\n'
        '| - Azoospermia (TESE/MESA)        |\n'
        '+----------------------------------+\n'
        '   V Khong\n'
        '+----------------------------------+\n'
        '| Tien su fertilization failure?   | -> ICSI\n'
        '| - FFR truoc do voi c-IVF         |\n'
        '+----------------------------------+\n'
        '   V Khong\n'
        '+----------------------------------+\n'
        '| PGT-A / PGT-M can lam?          | -> ICSI\n'
        '+----------------------------------+\n'
        '   V Khong\n'
        '+----------------------------------+\n'
        '| Frozen oocyte / IVM?             | -> ICSI uu tien\n'
        '+----------------------------------+\n'
        '   V Khong\n'
        '+----------------------------------+\n'
        '| SDF cao (>30%)?                  | -> Can nhac ICSI\n'
        '+----------------------------------+\n'
        '   V Khong\n'
        '   V\n'
        'c-IVF (Wang 2024, Berntsen 2025)'
    )

    doc.add_heading('6.3. Ty le ICSI toan cau', 2)
    add_bullets(doc, [
        'My: ~75% cycle (CDC 2021 data) - cao nhat the gioi.',
        'Chau Au: ~70% (ESHRE 2020).',
        'Chau A: ~60-80% tuy nuoc.',
        'Uc/New Zealand: ~65%.',
        'Xu huong: Sau Wang 2024 + Berntsen 2025, nhieu nuoc bat dau thu hep chi dinh ICSI.',
    ])

    # 7. EVIDENCE & GUIDELINES
    doc.add_heading('7. EVIDENCE & GUIDELINES', 1)
    doc.add_heading('7.1. ASRM Practice Committee Opinion (gan nhat 2023-2024)', 2)
    doc.add_paragraph('Khuyen cao chinh:')
    add_bullets(doc, [
        'ICSI chi dinh ro rang cho severe male factor.',
        'KHONG khuyen cao ICSI thuong quy cho non-male factor.',
        'PGT nen dung ICSI.',
        'Frozen oocyte nen dung ICSI.',
        'Moi lab nen co tieu chi rieng ve fertilization rate threshold.',
    ])
    doc.add_heading('7.2. ESHRE 2020 Position Statement', 2)
    add_bullets(doc, [
        'ICSI cho severe male factor la chuan.',
        'Non-male factor: khong du bang chung de khuyen cao ICSI.',
        'Sperm DNA testing: co the xem xet, khong bat buoc.',
        'Single embryo transfer (SET) nen la mac dinh.',
    ])
    doc.add_heading('7.3. Tong hop 2 RCT lon 2024-2025', 2)
    t6 = doc.add_table(rows=3, cols=7)
    fill_table(t6,
        ['Trial', 'N', 'Population', 'ICSI LBR', 'c-IVF LBR', 'Effect (RR 95% CI)', 'p'],
        [
            ('Wang 2024 (Lancet)', '2,329', 'Non-severe male factor, first cycle', '33.8%', '36.6%', '0.92 (0.83-1.03)', '0.16'),
            ('Berntsen 2025 (Nat Med)', '822', 'Non-severe male factor, first cycle, CLBR', '43.2%', '47.3%', '0.91 (0.79-1.06)', 'NS'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('=> Cung thong diep: ICSI khong cai thien live birth o non-severe male factor.')

    doc.add_heading('7.4. Esteves 2018 (Nat Rev Urol)', 2)
    add_bullets(doc, [
        'Bai tong quan toan dien nhat.',
        'ICSI cho moi loai vo sinh nam.',
        'Canh bao ve offspring safety.',
        '25 nam du lieu (1992-2018).',
        'Ket luan: ICSI bi overused, can thu hep chi dinh.',
    ])

    # 8. TIPS
    doc.add_heading('8. TIPS THUC HANH (CLINICAL PEARLS)', 1)
    add_bullets(doc, [
        'CHI DINH ICSI chat che: Sau Wang 2024 + Berntsen 2025, can co ly do ro rang. Non-severe male factor -> c-IVF truoc.',
        'Tu van benh nhan ve cost them: ICSI ton them $500-2000/cycle, khong phai luc nao cung tot hon.',
        'PGT-A can ICSI: Tranh DNA tinh trung bam ngoai zona pellucida gay nhieu ket qua.',
        'Frozen oocyte sau warming nen dung ICSI (zona cung hon, fertilization rate thap hon voi c-IVF).',
        'Severe male factor (count < 5M) -> ICSI la lua chon duy nhat, khong can thu c-IVF.',
        'TESE/MESA cho azoospermia: ICSI bat buoc, lay tinh trung tuoi hoac dong lanh.',
        'Fertilization failure truoc do voi c-IVF: chuyen ICSI o cycle sau.',
        'SDF testing khi: unexplained infertility + recurrent pregnancy loss + borderline male factor.',
        'Single embryo transfer (SET): mac dinh cho ca ICSI va c-IVF (giam multiple pregnancy).',
        'Canh bao offspring risks: Tu van benh nhan ve risks (nhe) khi dung ICSI, dac biet khi khong co chi dinh ro rang.',
    ])

    # 9. TONG KET
    doc.add_heading('9. TONG KET DIEM CAN NHO', 1)
    add_numbered(doc, [
        'ICSI (Intracytoplasmic Sperm Injection) ra doi 1992, ban dau cho severe male factor, nay chiem 70-80% cycle toan cau.',
        'Ky thuat: Bypass tu nhien bang cach tiem 1 tinh trung vao ooplasm qua micropipette duoi micromanipulator.',
        'Chi dinh chac chan: Severe male factor (count <5M, motility <5%, morphology <1% Kruger), azoospermia (TESE/MESA), globozoospermia, fertilization failure truoc, PGT, frozen oocyte.',
        'Wang 2024 (Lancet, PMID 38330980): ICSI 33.8% vs c-IVF 36.6% LBR, RR 0.92 (0.83-1.03), p=0.16 - khong cai thien o non-severe male factor.',
        'Berntsen 2025 (Nat Med, PMID 40217077): ICSI 43.2% vs c-IVF 47.3% CLBR, RR 0.91 (0.79-1.06) - khong cai thien.',
        'Ribas-Maynou 2021 (Biol Rev, PMID 33644978): 78 studies, 25,639 cycles - SDF cao anh huong IVF nhieu hon ICSI (ICSI co the "buffer" DNA damage).',
        'Esteves 2018 (Nat Rev Urol, PMID 29967387): ICSI offspring co risks tang nhe (di tat bam sinh, epigenetic disorders, cancer) - nhung kho tach biet khoi subfertility.',
        'c-IVF nen la first-line cho non-severe male factor, unexplained infertility, IVF dau tien.',
        'SDF testing can nhac khi: unexplained infertility, recurrent pregnancy loss, borderline male factor.',
        'ASRM/ESHRE: ICSI chi dinh ro rang, KHONG thuong quy; SET (single embryo transfer) la mac dinh.',
    ])

    # 10. TAI LIEU
    doc.add_heading('10. TAI LIEU THAM KHAO (VERIFY PUBMED)', 1)
    refs = [
        ('Wang Y. et al. (2024)', 'PMID: 38330980', 'Lancet.', 'DOI: 10.1016/S0140-6736(23)02416-9', '"Intracytoplasmic sperm injection versus conventional in-vitro fertilisation for couples with infertility with non-severe male factor: a multicentre, open-label, randomised controlled trial."'),
        ('Berntsen S, Zedeler A, Nohr B. et al. (2025)', 'PMID: 40217077', 'Nat Med.', 'DOI: 10.1038/s41591-025-03621-x', '"IVF versus ICSI in patients without severe male factor infertility: a randomized clinical trial."'),
        ('Esteves SC, Roque M, Bedoschi G, Haahr T, Humaidan P. (2018)', 'PMID: 29967387', 'Nat Rev Urol.', 'DOI: 10.1038/s41585-018-0051-8', '"Intracytoplasmic sperm injection for male infertility and consequences for offspring."'),
        ('Ribas-Maynou J, Yeste M, Becerra-Tomas N. et al. (2021)', 'PMID: 33644978', 'Biol Rev Camb Philos Soc.', 'DOI: 10.1111/brv.12700', '"Clinical implications of sperm DNA damage in IVF and ICSI: updated systematic review and meta-analysis."'),
    ]
    for i, (author, pmid, journal, doi, title) in enumerate(refs, start=1):
        p = doc.add_paragraph(style='List Number')
        p.add_run(f'{author} ').bold = True
        p.add_run(f'{pmid}. {journal} {doi}.\n')
        p.add_run(title).italic = True

    # FOOTER
    doc.add_paragraph()
    footer = doc.add_paragraph(f'— Het bai hoc ngay {DATE} —')
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.runs[0].italic = True
    footer.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    footer2 = doc.add_paragraph('Bac si: Ngoc 🍅 🐈‍⬛ | AI assistant: MiniMax Mavis')
    footer2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer2.runs[0].font.size = Pt(9)
    footer2.runs[0].font.color.rgb = RGBColor(0xA0, 0xA0, 0xA0)

    doc.save(str(DOCX_OUT))
    print(f"[DOCX] Saved: {DOCX_OUT}")
    print(f"[DOCX] Size: {DOCX_OUT.stat().st_size} bytes")


# ============================================================
# ANKI BUILDER (uses shared model)
# ============================================================
def build_anki():
    model, deck = build_pastel_model_and_deck(
        model_id=1607392321,
        model_name='ICSI trong IVF - Pastel',
        deck_id=2059400112,
        deck_name='ICSI trong IVF - 20/06/2026',
        deck_description='ICSI (Intracytoplasmic Sperm Injection) trong IVF - 20/06/2026 - Pastel theme'
    )
    n = add_cards_from_json(deck, model, CARDS_JSON, 'ART · IVF · ICSI · Embryology')
    write_apkg(deck, APKG_OUT)
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {n}")


# ============================================================
# HTML VISUAL SUMMARY
# ============================================================
def build_html():
    header_html = '''
<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">ICSI trong IVF</h1>
  <p class="text-stone-500 italic">Visual Summary - Bai hoc 20/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">ART</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">IVF/ICSI</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">Embryology</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">Male Factor</span>
    <span class="tag pastel-lavender px-3 py-1 rounded-full text-sm">Sperm DNA</span>
  </div>
</header>
'''

    main_html = '''

  <!-- SECTION 1: ICSI LA GI -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. ICSI la gi?</h2>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Dinh nghia</h3>
        <p class="text-sm text-stone-700"><b>Intracytoplasmic Sperm Injection</b> - tiem truc tiep 1 tinh trung vao bao tuong noan (ooplasm) qua micropipette.</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Lich su</h3>
        <p class="text-sm text-stone-700">Phat minh boi <b>Palermo nam 1992</b>. Ban dau chi cho severe male factor, nay chiem <b>70-80%</b> cycle toan cau.</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Bypass tu nhien</h3>
        <p class="text-sm text-stone-700">ICSI <b>bypass hoan toan</b> ZP va oolemma, khong can motility hay acrosome reaction binh thuong.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 2: TECHNIQUE 7 BUOC -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Ky thuat ICSI - 7 buoc chinh</h2>
    <div class="mermaid">
flowchart TD
    A["1. Oocyte Denudation<br/>(Hyaluronidase 80 IU/mL, 30-60s)"] --> B["2. Kiem tra do truong thanh<br/>(chi MII co polar body)"]
    B --> C["3. Sperm Preparation<br/>(Density gradient hoac Swim-up)"]
    C --> D["4. Sperm Immobilization<br/>(Ep duoi tinh trung)"]
    D --> E["5. Oocyte Positioning<br/>(Holding pipette, polar body 6h hoac 12h)"]
    E --> F["6. Injection o vi tri 3h<br/>(Doi dien polar body, bao ve spindle)"]
    F --> G["7. Kiem tra fertilization 16-18h<br/>(2PN + 2 polar body = binh thuong)"]

    style A fill:#f4c2c2
    style B fill:#f7d1ba
    style C fill:#c5d5e0
    style D fill:#c5e0c9
    style E fill:#d4c5e2
    style F fill:#f4c2c2
    style G fill:#c5e0c9
    </div>
  </section>

  <!-- SECTION 3: SO SANH c-IVF vs ICSI -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">3. So sanh c-IVF vs ICSI</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">Tieu chi</th>
            <th class="px-3 py-2 text-left">c-IVF</th>
            <th class="px-3 py-2 text-left">ICSI</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">So tinh trung</td><td class="px-3 py-2">50,000-100,000</td><td class="px-3 py-2">1 (chon loc)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">Can motility</td><td class="px-3 py-2">Co (bat buoc)</td><td class="px-3 py-2">Khong</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Can acrosome reaction</td><td class="px-3 py-2">Co</td><td class="px-3 py-2">Khong</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">Can micromanipulator</td><td class="px-3 py-2">Khong</td><td class="px-3 py-2">Co</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Chi phi them</td><td class="px-3 py-2">0</td><td class="px-3 py-2">+$500-2000/cycle</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">Fertilization rate</td><td class="px-3 py-2">60-70%</td><td class="px-3 py-2">70-80%</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">FFR (fertilization failure)</td><td class="px-3 py-2">5-10%</td><td class="px-3 py-2">1-3%</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 4: ALGORITHM -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">4. Algorithm quyet dinh ICSI vs c-IVF</h2>
    <div class="mermaid">
flowchart TD
    A["Danh gia SA + tien su"] --> B{"Severe male factor?<br/>(count<5M, motility<5%,<br/>morphology<1% Kruger,<br/>globozoospermia,<br/>azoospermia TESE/MESA)"}
    B -- "Co" --> Z1["ICSI"]
    B -- "Khong" --> C{"Tien su FFR<br/>voi c-IVF?"}
    C -- "Co" --> Z1
    C -- "Khong" --> D{"PGT-A / PGT-M<br/>can lam?"}
    D -- "Co" --> Z1
    D -- "Khong" --> E{"Frozen oocyte<br/>hoac IVM?"}
    E -- "Co" --> Z1
    E -- "Khong" --> F{"SDF cao<br/>(>30%)?"}
    F -- "Co" --> Z1
    F -- "Khong" --> Z2["c-IVF<br/>(Wang 2024, Berntsen 2025)"]

    style Z1 fill:#f4c2c2
    style Z2 fill:#c5e0c9
    style A fill:#f7d1ba
    </div>
  </section>

  <!-- SECTION 5: CHART 1 - 2 RCT LIVE BIRTH -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">5. ICSI khong cai thien live birth (2 RCT 2024-2025)</h2>
    <p class="text-sm text-stone-600 italic mb-4">Cung ket qua tu 2 chau luc: Trung Quoc (Lancet 2024) va Dan Mach (Nat Med 2025).</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Wang 2024 + Berntsen 2025</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>Wang 2024 (Lancet, n=2329):</b> ICSI 33.8% vs c-IVF 36.6% LBR, RR 0.92 (0.83-1.03)</li>
          <li>• <b>Berntsen 2025 (Nat Med, n=822):</b> ICSI 43.2% vs c-IVF 47.3% CLBR, RR 0.91 (0.79-1.06)</li>
          <li>• <b>Ket luan:</b> c-IVF nen la first-line cho non-severe male factor</li>
          <li>• ICSI danh rieng cho severe male factor</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 6: CHART 2 - SDF + IVF vs ICSI -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">6. Sperm DNA damage - ICSI buffer tot hon IVF</h2>
    <p class="text-sm text-stone-600 italic mb-4">Ribas-Maynou 2021 (Biol Rev, PMID 33644978) - meta 25,639 cycles.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart2"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Y nghia SDF</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• SDF cao: giam RO o IVF, KHONG anh huong o ICSI</li>
          <li>• ICSI bypass acrosome reaction, nen DNA damage it anh huong</li>
          <li>• Chi dinh ICSI khi SDF > 30% (DFI)</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 7: EVIDENCE TABLE -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. Evidence - Papers quan trong</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">PMID</th>
            <th class="px-3 py-2 text-left">Tac gia (Nam)</th>
            <th class="px-3 py-2 text-left">Loai</th>
            <th class="px-3 py-2 text-left">Ket qua chinh</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">38330980</td><td class="px-3 py-2">Wang Y. (2024)</td><td class="px-3 py-2">Lancet RCT, n=2329</td><td class="px-3 py-2">ICSI 33.8% vs c-IVF 36.6% LBR, RR 0.92 (0.83-1.03)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">40217077</td><td class="px-3 py-2">Berntsen S. (2025)</td><td class="px-3 py-2">Nat Med RCT, n=822</td><td class="px-3 py-2">ICSI 43.2% vs c-IVF 47.3% CLBR, RR 0.91 (0.79-1.06)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">29967387</td><td class="px-3 py-2">Esteves SC. (2018)</td><td class="px-3 py-2">Nat Rev Urol Review</td><td class="px-3 py-2">ICSI offspring risks tang nhe, ICSI bi overused</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">33644978</td><td class="px-3 py-2">Ribas-Maynou J. (2021)</td><td class="px-3 py-2">Biol Rev meta 25,639 cycles</td><td class="px-3 py-2">SDF cao giam IVF outcomes, ICSI buffer tot hon</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 8: TY LE ICSI TOAN CAU -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. Ty le ICSI toan cau (2020-2021)</h2>
    <div class="grid md:grid-cols-4 gap-3">
      <div class="pastel-pink rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">~75%</div>
        <div class="text-sm text-stone-600">My (CDC 2021)</div>
      </div>
      <div class="pastel-blue rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">~70%</div>
        <div class="text-sm text-stone-600">Chau Au (ESHRE 2020)</div>
      </div>
      <div class="pastel-mint rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">~60-80%</div>
        <div class="text-sm text-stone-600">Chau A (tuy nuoc)</div>
      </div>
      <div class="pastel-peach rounded-xl p-4 text-center">
        <div class="text-3xl font-bold text-stone-800">~65%</div>
        <div class="text-sm text-stone-600">Uc/NZ</div>
      </div>
    </div>
    <p class="text-sm text-stone-600 mt-3 italic">Xu huong: Sau Wang 2024 + Berntsen 2025, nhieu nuoc bat dau thu hep chi dinh ICSI.</p>
  </section>

  <!-- SECTION 9: OFFSPRING RISKS -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">9. ICSI offspring - Risks (Esteves 2018)</h2>
    <div class="grid md:grid-cols-2 gap-3">
      <div class="pastel-pink rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Di tat bam sinh</h3>
        <p class="text-xs text-stone-700">~1.5-2x (tim, co xuong, tiet nieu-sinh duc)</p>
      </div>
      <div class="pastel-blue rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Epigenetic disorders</h3>
        <p class="text-xs text-stone-700">Beckwith-Wiedemann, Angelman (hiem, nang)</p>
      </div>
      <div class="pastel-mint rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Chromosomal abn</h3>
        <p class="text-xs text-stone-700">Y microdeletion, balanced translocation tu cha</p>
      </div>
      <div class="pastel-peach rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Subfertility the he sau</h3>
        <p class="text-xs text-stone-700">Con trai co the thua huong Y microdeletion</p>
      </div>
      <div class="pastel-lavender rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Cancer tang nhe</h3>
        <p class="text-xs text-stone-700">Hepatoblastoma, leukemia (can data them)</p>
      </div>
      <div class="bg-stone-200 rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">Cardiometabolic</h3>
        <p class="text-xs text-stone-700">Tang HA, roi loan lipid (data moi)</p>
      </div>
    </div>
  </section>
'''

    custom_charts = '''
// Chart 1: 2 RCT live birth comparison
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['Wang 2024 (Lancet)\\nICSI', 'Wang 2024 (Lancet)\\nc-IVF', 'Berntsen 2025 (Nat Med)\\nICSI', 'Berntsen 2025 (Nat Med)\\nc-IVF'],
        datasets: [{
            label: '% Live Birth / CLBR',
            data: [33.8, 36.6, 43.2, 47.3],
            backgroundColor: [
                'rgba(244, 194, 194, 0.85)',
                'rgba(197, 213, 224, 0.85)',
                'rgba(244, 194, 194, 0.85)',
                'rgba(197, 213, 224, 0.85)'
            ],
            borderColor: [
                'rgba(244, 194, 194, 1)',
                'rgba(197, 213, 224, 1)',
                'rgba(244, 194, 194, 1)',
                'rgba(197, 213, 224, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'ICSI vs c-IVF - Live Birth / CLBR' },
            legend: { display: false },
            tooltip: {
                callbacks: {
                    afterLabel: function(ctx) {
                        const i = ctx.dataIndex;
                        if (i === 0) return 'RR 0.92 (0.83-1.03), p=0.16';
                        if (i === 1) return 'RR 0.92 (0.83-1.03), p=0.16';
                        if (i === 2) return 'RR 0.91 (0.79-1.06), NS';
                        if (i === 3) return 'RR 0.91 (0.79-1.06), NS';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: false,
                min: 30,
                max: 50,
                title: { display: true, text: '% Live Birth / CLBR' }
            }
        }
    }
});

// Chart 2: SDF impact on IVF vs ICSI
new Chart(document.getElementById('chart2'), {
    type: 'bar',
    data: {
        labels: ['Implantation\\n(IVF)', 'Implantation\\n(ICSI)', 'Pregnancy\\n(IVF)', 'Pregnancy\\n(ICSI)'],
        datasets: [{
            label: 'RR (SDF cao vs thap)',
            data: [0.68, 0.79, 0.72, 0.89],
            backgroundColor: [
                'rgba(244, 194, 194, 0.85)',
                'rgba(197, 213, 224, 0.85)',
                'rgba(244, 194, 194, 0.85)',
                'rgba(197, 213, 224, 0.85)'
            ],
            borderColor: [
                'rgba(244, 194, 194, 1)',
                'rgba(197, 213, 224, 1)',
                'rgba(244, 194, 194, 1)',
                'rgba(197, 213, 224, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Ribas-Maynou 2021 - SDF cao lam giam IVF nhung khong ICSI' },
            legend: { display: false },
            annotation: {}
        },
        scales: {
            y: {
                beginAtZero: false,
                min: 0.5,
                max: 1.0,
                title: { display: true, text: 'Risk Ratio (RR)' }
            }
        }
    }
});
'''

    footer_text = 'Bai hoc soan boi MiniMax Mavis cho Bs. Ngoc 🍅 🐈‍⬛ | Verified PubMed: 4 papers (PMID 38330980, 40217077, 29967387, 33644978) - 2 RCT lon 2024-2025 thay doi chi dinh ICSI'

    html_content = build_lesson_html(
        title='ICSI trong IVF - Visual Summary',
        header_html=header_html,
        main_html=main_html,
        footer_text=footer_text,
        custom_charts=custom_charts,
    )
    write_html(html_content, HTML_OUT)
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building ICSI Lesson - {DATE} ===\n")
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
