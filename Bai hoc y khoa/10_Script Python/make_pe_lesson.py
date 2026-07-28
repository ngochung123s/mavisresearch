"""Build full lesson: docx + anki apkg + html visual summary.
Topic: Sang loc + Du phong Tien san giat - 2026-06-22 (user request).
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
LESSON_DIR = ROOT / "01_San phu khoa" / "03_Preeclampsia_Screening"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "01_San phu khoa" / "03_Preeclampsia_Screening"
DATE = "2026-06-22"

DOCX_OUT = LESSON_DIR / f"Sang loc Du phong Tien san giat - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - Sang loc Tien san giat 20 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - Sang loc Tien san giat - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "preeclampsia_cards.json"


def build_docx():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    title = doc.add_heading('SANG LOC & DU PHONG TIEN SAN GIAT', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bai hoc ngay {DATE} - San phu khoa (Obstetrics)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TONG QUAN - VI SAO BAI NAY QUAN TRONG?', 1)
    doc.add_paragraph(
        'Tien san giat (Preeclampsia - PE) la mot trong nhung nguyen nhan hang dau gay tu vong va benh tat cho me va thai nhi:\n'
        '- Uoc tinh 2-5% thai ky bi anh huong.\n'
        '- 76,000 phu nu va 500,000 tre so sinh tu vong moi nam (FIGO 2019, PMID 31111484).\n'
        '- Preterm PE (sinh < 37 tuan) lien quan tang nguy co tu vong chu sinh, SGA, BPD, bai nao.\n'
        '- Phu nu bi PE co tuoi tho giam trung binh 10 nam.'
    )
    doc.add_paragraph('Tin tot: PE co the DU PHONG DUOC neu sang loc som va dieu tri du phong kip thoi.')
    doc.add_paragraph('Theo [FIGO 2019 - Preeclampsia Screening] (PMID 31111484): "Universal screening for preterm pre-eclampsia during early pregnancy by the first-trimester combined test with maternal risk factors and biomarkers as a one-step procedure should be offered to all pregnant women."').runs[0].italic = True
    doc.add_paragraph('ASPRE trial (NEJM 2017, PMID 28657417): Aspirin 150 mg/dem tu 11-14 tuan -> 36 tuan GIAM 62% preterm PE o nhom nguy co cao.').runs[0].bold = True

    # 1. DINH NGHIA
    doc.add_heading('1. DINH NGHIA VA PHAN LOAI TIEN SAN GIAT (ISSHP 2018)', 1)
    doc.add_heading('1.1. Dinh nghia', 2)
    doc.add_paragraph('PE theo ISSHP 2018: HA >= 140/90 mmHg (it nhat 2 lan, cach nhau >= 4 gio) o phu nu truoc do binh thuong, SAU 20 tuan, kem MOT TRONG CAC tieu chi sau:')
    add_bullets(doc, [
        'Proteinuria: Protein/creatinine ratio >= 30 mg/mmol (>= 300 mg/24h) HOAC dipstick >= 2+.',
        'Roi loan chuc nang co quan: Than (creatinine >= 90 umol/L), gan (ALT/AST > 40 IU/L), than kinh (san giat, thay doi y thuc, mu, dot quy, clonus, dau dau nang), huyet hoc (tieu cau < 150,000/uL, DIC, tan huyet).',
        'Roi loan nhau thai - tu cung: FGR, abnormal umbilical artery Doppler, thai chet luu.',
    ])

    doc.add_heading('1.2. Phan loai theo thoi diem khoi phat (FIGO 2019)', 2)
    t1 = doc.add_table(rows=5, cols=3)
    fill_table(t1,
        ['Loai', 'Tieu chi', 'Dac diem'],
        [
            ('Early-onset PE', 'Sinh < 34+0 tuan', 'Nguy co cao nhat, lien quan nhau bat thuong nang'),
            ('Preterm PE', 'Sinh < 37+0 tuan', 'Muc tieu chinh cua screening + aspirin du phong'),
            ('Late-onset PE', 'Sinh >= 34+0 tuan', 'Thuong nhau it bat thuong, lien quan yeu to me'),
            ('Term PE', 'Sinh >= 37+0 tuan', 'Pho bien nhat, thuong nhe'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Luu y: Phan loai khong loai tru nhau - mot benh nhan co the vua early-onset vua preterm PE.').runs[0].bold = True

    doc.add_heading('1.3. PE nang (severe features) - ACOG 2019', 2)
    add_bullets(doc, [
        'HA >= 160/110 mmHg.',
        'Tieu cau < 100,000/uL.',
        'Men gan tang gap doi binh thuong (ALT/AST > 2x ULN).',
        'Suy than cap (creatinine > 1.1 mg/dL hoac tang gap doi).',
        'Phu phoi.',
        'Trieu chung than kinh moi (dau dau nang, roi loan thi truong, co gat - san giat).',
        'Dau ha suon phai du doi.',
    ])

    # 2. CO CHE
    doc.add_heading('2. CO CHE BENH SINH - 2-STEP THEORY', 1)
    doc.add_heading('2.1. Step 1: Bat thuong xam nhap te bao nuoi', 2)
    doc.add_paragraph(
        'Tuan 8-18: Trophoblast (te bao nuoi) xam nhap thanh mach mau xoan (spiral arteries) cua me.\n'
        '- Binh thuong: trophoblast pha huy lop co tron -> spiral arteries thanh mach co duong kinh lon, ap luc thap, cung cap mau cho nhau.\n'
        '- Bat thuong: trophoblast chi xam nhap mot phan -> spiral arteries giu duong kinh nho, ap luc cao -> nhau thieu mau, stress oxy hoa.'
    )
    doc.add_heading('2.2. Step 2: Mat can bang yeu to tao mach', 2)
    add_bullets(doc, [
        'Nhau thieu mau tiet: TANG sFlt-1 (chen VEGF, PlGF), GIAM PlGF.',
        'Hau qua: co that mach (tang HA), ton thuong noi mo (proteinuria, phu, roi loan dong mau), giam tuoi mau cac co quan (gan, than, nao, nhau).',
    ])
    doc.add_heading('2.3. Biomarker huyet thanh', 2)
    t2 = doc.add_table(rows=4, cols=3)
    fill_table(t2,
        ['Biomarker', 'Thay doi trong PE', 'Y nghia'],
        [
            ('PlGF (Placental Growth Factor)', 'GIAM (som nhat 11-13 tuan)', 'Marker nhay nhat trong 3 biomarkers'),
            ('sFlt-1 (soluble fms-like tyrosine kinase-1)', 'TANG (bieu hien ro tu 20-24 tuan)', 'Chan doan PE sau 20 tuan'),
            ('PAPP-A', 'GIAM nhe (it nhay hon PlGF)', 'Gia tri thap hon PlGF trong FMF Triple Test'),
        ])
    doc.add_paragraph()

    # 3. RISK FACTORS
    doc.add_heading('3. YEU TO NGUY CO (Maternal risk factors)', 1)
    doc.add_paragraph('Theo FIGO 2019 (PMID 31111484) va ACOG 2013/2019:')
    t3 = doc.add_table(rows=8, cols=2)
    fill_table(t3,
        ['Yeu to nguy co CAO (1 yeu to = du)', 'Yeu to nguy co TRUNG BINH (>= 2 yeu to)'],
        [
            ('Tien su PE (kem sinh non < 34 tu) - nguy co tai phat 16-32%', 'Tuoi me >= 35'),
            ('Benh than man', 'BMI >= 30'),
            ('Benh tu mien (SLE, APS)', 'Tien su gia dinh PE (me/chi em)'),
            ('Tang HA man (chronic hypertension)', 'Nulliparity'),
            ('Dai thao duong type 1 hoac 2', 'ART (thu tinh trong ong nghiem)'),
            ('Hoi chung antiphospholipid (APS)', 'Da thai'),
            ('Benh tim mach', 'Khoang cach thai ky > 10 nam hoac < 1 nam / Sac toc: Chau Phi, Nam A'),
        ])
    doc.add_paragraph()

    # 4. THUAT TOAN SANG LOC
    doc.add_heading('4. THUAT TOAN SANG LOC TIEN SAN GIAT - 3 CACH TIEP CAN', 1)
    doc.add_heading('4.1. So sanh hieu qua (Chaemsaithong 2022, PMID 32682859)', 2)
    t4 = doc.add_table(rows=4, cols=4)
    fill_table(t4,
        ['Phuong phap', 'DR preterm PE', 'DR term PE', 'FPR'],
        [
            ('ACOG 2013 (maternal risk factors only)', '5%', '2%', '0.2%'),
            ('NICE 2019 (maternal risk factors)', '41%', '34%', '10%'),
            ('FMF Triple Test (maternal + MAP + PlGF + UtA-PI)', '75-90%', '41-43%', '10%'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('NNT = 250 (sang loc 250 thai phu de phong 1 ca preterm PE).').runs[0].bold = True

    doc.add_heading('4.2. FMF Triple Test - thanh phan', 2)
    add_bullets(doc, [
        'Maternal risk factors: tuoi, BMI, chung toc, parity, tien su PE, tien su gia dinh, benh nen (HTN, DM, SLE, APS, than), ART, khoang cach thai ky, hut thuoc.',
        'MAP (Mean Arterial Pressure): do 2 lan, moi ben canh tay, nghi 5 phut. PE som: MAP TANG (dau hieu som nhat).',
        'PlGF (Placental Growth Factor): mau me, do ELISA. PE som: PlGF GIAM (< 0.7-0.8 MoM). Day la marker nhay nhat.',
        'UtA-PI (Uterine Artery Pulsatility Index): Doppler qua ca 2 dong mach tu cung. PE som: UtA-PI TANG + notching som.',
    ])
    doc.add_paragraph('Cut-off nguy co cao: >= 1:100 (theo FIGO 2019 va FMF).').runs[0].bold = True
    doc.add_paragraph('Risk calculator mien phi: fetalmedicine.org/research/assess/preeclampsia')

    doc.add_heading('4.3. Algorithm FMF (FIGO 2019)', 2)
    doc.add_paragraph(
        'Thai 11-13+6 tuan -> Thu thap: maternal factors + MAP + PlGF + UtA-PI -> Su dung FMF risk calculator.\n\n'
        '+----------------------------------+\n'
        '| Nguy co cao: >= 1:100            | -> Aspirin 150 mg/dem (cho den 36 tuan hoac sinh)\n'
        '+----------------------------------+\n'
        '   V\n'
        '+----------------------------------+\n'
        '| Nguy co trung binh: 1:101-1:1000 | -> Theo doi sat (co the can nhac aspirin 75-100 mg)\n'
        '+----------------------------------+\n'
        '   V\n'
        '+----------------------------------+\n'
        '| Nguy co thap: < 1:1000           | -> Routine prenatal care\n'
        '+----------------------------------+\n\n'
        'Contingent screening (cho he thong nguon luc han che):\n'
        '- Buoc 1: maternal factors + MAP cho tat ca.\n'
        '- Buoc 2: chi do PlGF + UtA-PI cho nhom nguy co trung binh-cao sau buoc 1.\n'
        '- Tiet kiem chi phi, van duy tri detection rate cao.'
    )

    # 5. ASPIRIN
    doc.add_heading('5. ASPIRIN DU PHONG - ASPRE TRIAL', 1)
    doc.add_heading('5.1. ASPRE MAIN RCT (NEJM 2017, PMID 28657417)', 2)
    doc.add_paragraph('Thiet ke: Multicentre, double-blind, placebo-controlled RCT.')
    add_bullets(doc, [
        'N = 1,776 phu nu singleton, nguy co cao preterm PE (theo FMF).',
        'Random 1:1: Aspirin 150 mg/dem vs Placebo.',
        'Tu 11-14 tuan -> 36 tuan (hoac sinh).',
        'Primary outcome: Preterm PE (sinh < 37 tuan).',
    ])
    doc.add_paragraph('Ket qua (FULL VERIFIED):').runs[0].bold = True
    add_bullets(doc, [
        'Preterm PE: 1.6% (13/798) aspirin vs 4.3% (35/822) placebo.',
        'OR 0.38 (95% CI 0.20-0.74), p = 0.004.',
        'Reduction 62%.',
        'Adherence: 79.9% uong >= 85% lieu.',
        'Khong co khac biet dang ke ve adverse neonatal/other events.',
    ])

    doc.add_heading('5.2. Co che aspirin (theo Rolnik 2023, PMID 37058400)', 2)
    add_bullets(doc, [
        'Aspirin KHONG anh huong: MAP trajectory (p = 0.340), PAPP-A (p = 0.259), PlGF (p = 0.335).',
        'Aspirin CO anh huong: Giam UtA-PI dang ke (p = 0.006), dac biet TRUOC 20 tuan.',
        '-> Co che chinh: cai thien su tai cau truc spiral arteries (giam suc can dong mach tu cung) thong qua uc che TXA2 -> uc che ket tieu tieu cau -> cai thien vi tuan hoan nhau.',
    ])

    doc.add_heading('5.3. Aspirin lieu, thoi gian', 2)
    add_bullets(doc, [
        'Lieu: 150 mg/dem (FIGO, NICE, WHO, USPSTF 2024) - lieu cao, ASPRE trial.',
        'Lieu duoi 100 mg: hieu qua thap hon (meta-analysis Roberge 2017).',
        'Bat dau: TRUOC 16 tuan (ly tuong 11-14 tuan). Sau 16 tuan: KHONG con hieu qua.',
        'Dung: 36 tuan (theo ASPRE protocol), hoac khi sinh, hoac khi chan doan PE.',
        'Ly do dung 36 tuan: tranh chay mau khi sinh, da du thoi gian du phong.',
    ])

    doc.add_heading('5.4. Aspirin co an toan khong? Co tang LGA khong?', 2)
    add_bullets(doc, [
        'KHONG tang LGA (large-for-gestational-age): 5.5% aspirin vs 6.2% placebo (p = 0.667) - theo Rolnik 2025 (PMID 40590060).',
        'Shift birthweight distribution tu < 2500g len 2500-4000g (cai thien nhe).',
        'NGOAI LE: Phu nu DAI THAO DUONG - aspirin co the tang LGA (can than trong).',
        'Khong tang nguy co di tat bam sinh, chay mau, hoac bong nhau. An toan trong 3 thang dau thai ky.',
    ])
    doc.add_paragraph('Ai KHONG nen dung aspirin: di ung aspirin/NSAID, loet da day-ta trang hoat dong, suyren nang do aspirin, roi loan dong mau (hemophilia, vWD nang), benh gan nang giai doan cuoi.').runs[0].bold = True

    # 6. YEU TO THAT BAI
    doc.add_heading('6. YEU TO DU BAO THAT BAI VOI ASPIRIN (Shen 2021, PMID 33998099)', 1)
    doc.add_paragraph('Theo Shen 2021 (UOG, PMID 33998099) - phan tich phu ASPRE:')
    t5 = doc.add_table(rows=5, cols=3)
    fill_table(t5,
        ['Yeu to', 'Nguy co preterm PE du aspirin', 'aOR (95% CI)'],
        [
            ('Chronic hypertension', 'Aspirin KHONG co effect', 'p interaction = 0.042'),
            ('Risk rat cao (1:2 den 1:10)', '7x cao hon so voi 1:51-1:100', 'aOR 6.71 (2.38-18.88)'),
            ('Risk cao (1:11 den 1:50)', '3x cao hon', 'aOR 2.77 (1.11-6.94)'),
            ('PlGF < 0.712 MoM (cut-off toi uu)', '3.7x cao hon', 'aOR 3.68 (1.53-8.86)'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Phu nu co chronic HTN can theo doi sat du aspirin - thuoc co the khong du hieu qua. Nhom rat cao (1:2-1:10) can can nhac bien phap bo sung.').runs[0].bold = True

    # 7. CALCIUM
    doc.add_heading('7. CALCIUM VA CAC BIEN PHAP DU PHONG KHAC', 1)
    doc.add_heading('7.1. Calcium (FIGO 2019 + WHO 2011)', 2)
    add_bullets(doc, [
        'Chi dinh: Phu nu co CALCIUM INTAKE < 800 mg/ngay (pho bien o cac nuoc thu nhap thap).',
        'Lieu: 1.5-2 g elemental calcium/ngay (chia 3 lan, tu sau 20 tuan).',
        'Co che: Giam co that mach, on dinh noi mo.',
        'Hieu qua (WHO 2011): Giam ~50% PE, dac biet EARLY-ONSET PE.',
        'Luu y: O cac nuoc phat trien co calcium intake du, KHONG co evidence ro rang ve loi ich.',
    ])

    doc.add_heading('7.2. Magnesium', 2)
    add_bullets(doc, [
        'KHONG khuyen cao du phong thuong quy.',
        'CHI DUNG trong: eclampsia (san giat) HOAC severe PE gan sinh (trong vong 24h).',
        'Lieu: Loading 4-6 g IV (15-20 phut) + maintenance 1-2 g/hr IV lien tuc.',
        'Tiep tuc 24h sau sinh (hoac 24h sau con giat cuoi cung neu eclampsia).',
        'Can theo doi phan xa (knee jerk), Mg nhiem than (RR < 12, SpO2 < 95%, urine output < 100 mL/4h) -> giam lieu hoac dung.',
        'Antidote: calcium gluconate 1g IV.',
    ])

    doc.add_heading('7.3. Cac bien phap KHONG khuyen cao', 2)
    add_bullets(doc, [
        'LMWH (heparin trong luong phan tu thap): KHONG du phong PE o thai phu thuong, chi can nhac trong APS.',
        'Nghi ngoi, han che van dong: KHONG co evidence giam PE, co the tang DVT.',
        'Che do an, chat chong oxy hoa (vitamin C/E, lycopene): meta-analysis khong thay loi ich.',
        'Vitamin D bo sung thuong quy (ACOG): chi bo sung neu thieu.',
    ])

    # 8. PHAN TICH PHU
    doc.add_heading('8. ASPRE TRIAL - CAC PHAN TICH PHU (2021-2025)', 1)
    doc.add_heading('8.1. ASPRE + SPREE (Nicolaides 2024, PMID 37749709)', 2)
    doc.add_paragraph('Phan tich ket hop 2 trial lon (N = 16,451 + 1,620):')
    t6 = doc.add_table(rows=4, cols=4)
    fill_table(t6,
        ['Outcome', 'DR (FMF Triple Test)', 'DR (NICE)', 'Aspirin effect'],
        [
            ('Spontaneous PTB (sPTB)', '17%', '12%', '14% reduction'),
            ('Iatrogenic PTB do PE (iPTB-PE)', '82%', '39%', '65% reduction'),
            ('Iatrogenic PTB khong do PE (iPTB-noPE)', '25%', '19%', '0% reduction'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Triple Test + aspirin HIEU QUA DAC BIET trong viec giam iPTB-PE (65%), khong anh huong sPTB/iPTB-noPE.').runs[0].bold = True

    doc.add_heading('8.2. ASPRE + birthweight (Rolnik 2025, PMID 40590060)', 2)
    add_bullets(doc, [
        'N = 1,571 singleton live neonates (777 aspirin, 794 placebo).',
        'Aspirin shift birthweight distribution tu < 2500g len 2500-4000g.',
        'KHONG tang LGA: 5.5% aspirin vs 6.2% placebo (p = 0.667).',
        'NGOAI LE: Phu nu DAI THAO DUONG - aspirin co the tang LGA (interaction p = 0.034).',
    ])

    # 9. EVIDENCE
    doc.add_heading('9. EVIDENCE & GUIDELINES', 1)
    doc.add_heading('9.1. [FIGO 2019 - Preeclampsia Screening] (PMID 31111484) - KEY GUIDELINE', 2)
    doc.add_paragraph('Poon LC et al., IJGO 2019. International Federation of Gynecology and Obstetrics.')
    doc.add_paragraph('Khuyen cao chinh:')
    add_bullets(doc, [
        'Universal screening: Tat ca phu nu mang thai can sang loc PE quy 1.',
        'FMF Triple Test: Maternal risk factors + MAP + PlGF + UtA-PI (best performance).',
        'High risk = >= 1:100: Aspirin 150 mg/dem tu 11-14+6 tuan -> 36 tuan.',
        'KHONG dung aspirin thuong quy cho tat ca thai phu (chi nhom nguy co cao).',
        'Calcium 1.5-2 g/ngay neu intake < 800 mg/ngay.',
        'Contingent screening cho nguon luc han che.',
        'Risk calculator mien phi: fetalmedicine.org/research/assess/preeclampsia.',
    ])

    doc.add_heading('9.2. ISSHP 2018', 2)
    add_bullets(doc, [
        'Quoc te dong thuan ve dinh nghia PE.',
        'Phan loai: early-onset, preterm, late-onset, term.',
        'Co the dung tieu chi proteinuria HOAC roi loan co quan khac (khong bat buoc proteinuria).',
    ])

    doc.add_heading('9.3. ACOG 2019 (Practice Bulletin #202)', 2)
    add_bullets(doc, [
        'Hypertension in pregnancy guideline.',
        'Khuyen cao low-dose aspirin (81 mg) cho phu nu nguy co cao PE (1 yeu to cao hoac >= 2 trung binh).',
        'Luu y: ACOG 2019 van dung 81 mg, chua cap nhat 150 mg (so voi FIGO 2019).',
    ])

    doc.add_heading('9.4. NICE 2019 (UK)', 2)
    add_bullets(doc, [
        'Sang loc theo maternal risk factors (chua dung triple test).',
        'Aspirin 75 mg/dem cho nhom nguy co cao (tu 12 tuan).',
        'NNT cao hon FMF Triple Test.',
    ])

    doc.add_heading('9.5. WHO 2011 + USPSTF 2024', 2)
    add_bullets(doc, [
        'WHO: Calcium 1.5-2 g/ngay cho populations with low dietary calcium intake.',
        'USPSTF 2024 (Grade B): Recommend low-dose aspirin (81 mg) cho phu nu nguy co cao PE tu 12 tuan.',
        'Chu y: USPSTF/ACOG dung 81 mg, FIGO dung 150 mg (co conflict).',
    ])

    doc.add_heading('9.6. Tong hop evidence', 2)
    t7 = doc.add_table(rows=10, cols=3)
    fill_table(t7,
        ['Paper', 'Loai', 'Ket qua chinh'],
        [
            ('Rolnik 2017 (NEJM, PMID 28657417)', 'RCT n=1776', 'Aspirin 150 mg giam 62% preterm PE'),
            ('Rolnik 2017 (UOG, PMID 28741785)', 'Screening n=25,797', 'FMF Triple Test DR 76.7% preterm PE'),
            ('Chaemsaithong 2022 (AJOG, PMID 32682859)', 'Review', 'FMF Triple Test vs ACOG/NICE'),
            ('Poon 2019 (IJGO, PMID 31111484)', 'FIGO guideline', 'Universal screening + 150 mg aspirin'),
            ('Rolnik 2023 (UOG, PMID 37058400)', 'Secondary analysis', 'Aspirin giam UtA-PI (p=0.006)'),
            ('Rolnik 2024 (AJOG, PMID 38151219)', 'Secondary analysis', 'Aspirin khong anh huong PlGF/PAPP-A'),
            ('Shen 2021 (UOG, PMID 33998099)', 'Secondary analysis', 'Chronic HTN + risk rat cao: aspirin kem'),
            ('Nicolaides 2024 (BJOG, PMID 37749709)', 'Combined analysis', 'FMF Triple Test + aspirin giam 65% iPTB-PE'),
            ('Rolnik 2025 (BJOG, PMID 40590060)', 'Secondary analysis', 'Aspirin khong tang LGA'),
        ])
    doc.add_paragraph()

    # 10. TIPS
    doc.add_heading('10. TIPS THUC HANH (CLINICAL PEARLS)', 1)
    add_bullets(doc, [
        'Sang loc PE cho TAT CA thai phu theo FIGO 2019, khong chi nhom "co ve nguy co".',
        'FMF Triple Test = tot nhat hien nay: DR 75-90% preterm PE, uu tien dung.',
        'Aspirin 150 mg/dem (FIGO) - KHONG phai 81 mg (ACOG cu) - 150 mg co evidence manh nhat.',
        'Bat dau aspirin 11-14 tuan - muon hon 16 tuan thi mat tac dung.',
        'Dung aspirin 36 tuan - tranh chay mau khi sinh, da du thoi gian du phong.',
        'Chronic HTN + aspirin: theo doi sat, co the khong du hieu qua.',
        'Calcium 1.5-2 g/ngay neu intake < 800 mg (chu yeu o populations thu nhap thap).',
        'Magnesium chi dung trong eclampsia hoac severe PE gan sinh - KHONG du phong.',
        'Heparin KHONG du phong PE o thai phu thuong (tru APS).',
        'FMF risk calculator MIEN PHI tai fetalmedicine.org - dung cho moi thai phu 11-14 tuan.',
    ])

    # 11. TONG KET
    doc.add_heading('11. TONG KET DIEM CAN NHO', 1)
    add_numbered(doc, [
        'Preeclampsia theo ISSHP 2018: HA >= 140/90 mmHg SAU 20 tuan + proteinuria HOAC roi loan co quan (gan, than, than kinh, huyet hoc, nhau).',
        'Phan loai: Early-onset (<34w), Preterm (<37w), Late-onset (>=34w), Term (>=37w).',
        'Tien su PE + chronic HTN + APS + benh than = nguy co CAO (1 yeu to du).',
        'FMF Triple Test (maternal + MAP + PlGF + UtA-PI) DR 75-90% preterm PE - vuot troi ACOG (5%) va NICE (41%).',
        'ASPRE trial (NEJM 2017, PMID 28657417): Aspirin 150 mg/dem tu 11-14 tuan -> 36 tuan GIAM 62% preterm PE (OR 0.38, p=0.004).',
        'Aspirin 11-14 tuan - sau 16 tuan mat tac dung. 150 mg/dem lieu khuyen cao FIGO.',
        'Co che aspirin: giam UtA-PI (cai thien remodeling spiral arteries), KHONG anh huong MAP/PlGF/PAPP-A.',
        'Calcium 1.5-2 g/ngay neu intake < 800 mg (giam ~50% PE, dac biet early-onset).',
        'Aspirin KHONG tang LGA (5.5% vs 6.2%, p=0.667) - tru dai thao duong.',
        'Chronic HTN + aspirin: theo doi sat, aspirin co the kem hieu qua.',
    ])

    # 12. TAI LIEU
    doc.add_heading('12. TAI LIEU THAM KHAO (VERIFY PUBMED)', 1)
    refs = [
        ('Rolnik DL, Wright D, Poon LC, et al. (2017)', 'PMID: 28657417', 'N Engl J Med.', 'DOI: 10.1056/NEJMoa1704559', '"Aspirin versus Placebo in Pregnancies at High Risk for Preterm Preeclampsia."'),
        ('Poon LC, Shennan A, Hyett JA, et al. (2019)', 'PMID: 31111484', 'Int J Gynaecol Obstet.', 'DOI: 10.1002/ijgo.12802', '"The International Federation of Gynecology and Obstetrics (FIGO) initiative on pre-eclampsia: A pragmatic guide for first-trimester screening and prevention."'),
        ('Rolnik DL, Wright D, Poon LCY, et al. (2017)', 'PMID: 28741785', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.18816', '"ASPRE trial: performance of screening for preterm pre-eclampsia."'),
        ('Chaemsaithong P, Sahota DS, Poon LC. (2022)', 'PMID: 32682859', 'Am J Obstet Gynecol.', 'DOI: 10.1016/j.ajog.2020.07.020', '"First trimester preeclampsia screening and prediction."'),
        ('Rolnik DL, Syngelaki A, O\'Gorman N, Wright D, Nicolaides KH, Poon LC. (2024)', 'PMID: 38151219', 'Am J Obstet Gynecol.', 'DOI: 10.1016/j.ajog.2023.12.031', '"Aspirin for evidence-based preeclampsia prevention trial: effects of aspirin on maternal serum pregnancy-associated plasma protein A and placental growth factor trajectories in pregnancy."'),
        ('Rolnik DL, Syngelaki A, O\'Gorman N, Wright D, Poon LC, Nicolaides KH. (2023)', 'PMID: 37058400', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.26222', '"ASPRE trial: effects of aspirin on mean arterial blood pressure and uterine artery pulsatility index trajectories in pregnancy."'),
        ('Shen L, Martinez-Portilla RJ, Rolnik DL, Poon LC. (2021)', 'PMID: 33998099', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.23668', '"ASPRE trial: risk factors for development of preterm pre-eclampsia despite aspirin prophylaxis."'),
        ('Nicolaides KH, Syngelaki A, Poon LC, Rolnik DL, Tan MY, Wright A, Wright D. (2024)', 'PMID: 37749709', 'BJOG.', 'DOI: 10.1111/1471-0528.17673', '"First-trimester prediction of preterm pre-eclampsia and prophylaxis by aspirin: Effect on spontaneous and iatrogenic preterm birth."'),
        ('Rolnik DL, Poon LC, Syngelaki A, et al. (2025)', 'PMID: 40590060', 'BJOG.', 'DOI: 10.1111/1471-0528.18263', '"Aspirin, Birthweight, and Large-For-Gestational-Age Neonates: A Secondary Analysis of the ASPRE Trial."'),
    ]
    for i, (author, pmid, journal, doi, title) in enumerate(refs, start=1):
        p = doc.add_paragraph(style='List Number')
        p.add_run(f'{author} ').bold = True
        p.add_run(f'{pmid}. {journal} {doi}.\n')
        p.add_run(title).italic = True

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


def build_anki():
    model, deck = build_pastel_model_and_deck(
        model_id=1607392323,
        model_name='Sang loc PE - Pastel',
        deck_id=2059400114,
        deck_name='Sang loc + Du phong Tien san giat - 22/06/2026',
        deck_description='Sang loc + Du phong Tien san giat (Preeclampsia) - 22/06/2026 - Pastel theme'
    )
    n = add_cards_from_json(deck, model, CARDS_JSON, 'OB-GYN · Preeclampsia · FMF · ASPRE')
    write_apkg(deck, APKG_OUT)
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {n}")


def build_html():
    header_html = '''
<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">Sang loc & Du phong Tien san giat</h1>
  <p class="text-stone-500 italic">Visual Summary - Bai hoc 22/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">OB-GYN</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">Preeclampsia</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">FMF Triple Test</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">ASPRE / Aspirin</span>
    <span class="tag pastel-lavender px-3 py-1 rounded-full text-sm">PlGF / UtA-PI</span>
  </div>
</header>
'''

    main_html = '''
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. ISSHP 2018 - Dinh nghia Preeclampsia</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">Tieu chi bat buoc</h3>
        <p class="text-sm text-stone-700">HA &gt;= 140/90 mmHg (it nhat 2 lan, cach nhau &gt;= 4 gio) <b>SAU 20 tuan</b> thai ky o phu nu truoc do binh thuong.</p>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">+ 1 trong 3 tieu chi</h3>
        <p class="text-sm text-stone-700">1. Proteinuria (P/C ratio &gt;= 30 mg/mmol)<br>2. Roi loan co quan (than, gan, than kinh, huyet hoc)<br>3. Roi loan nhau thai (FGR, abnormal UA Doppler)</p>
      </div>
    </div>
    <p class="text-sm text-stone-600 mt-3 italic">FIGO 2019 phan loai: Early-onset (&lt;34w) / Preterm (&lt;37w) / Late-onset (>=34w) / Term (>=37w). Muc tieu chinh cua screening la PRETERM PE.</p>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Algorithm sang loc (FIGO 2019)</h2>
    <div class="mermaid">
flowchart TD
    A["Thai 11-13+6 tuan<br/>Thu thap: maternal + MAP + PlGF + UtA-PI"] --> B{"FMF Risk Calculator<br/>(fetalmedicine.org)"}
    B -- ">= 1:100<br/>(nguy co cao)" --> Z1["Aspirin 150 mg/dem<br/>11-14+6 -> 36 tuan<br/>(ASPRE protocol)"]
    B -- "1:101 - 1:1000<br/>(trung binh)" --> Z2["Theo doi sat<br/>+ Can nhac aspirin 75-100 mg"]
    B -- "< 1:1000<br/>(thap)" --> Z3["Routine prenatal care"]
    Z1 --> C["Kiem tra: chronic HTN?<br/>Risk 1:2-1:10?<br/>PlGF < 0.712 MoM?"]
    C -- "Co" --> Z4["Theo doi sat<br/>Aspirin co the kem hieu qua<br/>(Shen 2021)"]
    C -- "Khong" --> Z5["Aspirin se hieu qua<br/>62% reduction<br/>(Rolnik 2017 NEJM)"]

    style Z1 fill:#f4c2c2
    style Z2 fill:#f7d1ba
    style Z3 fill:#c5e0c9
    style Z4 fill:#d4c5e2
    style Z5 fill:#c5d5e0
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">3. So sanh 3 phuong phap sang loc PE</h2>
    <p class="text-sm text-stone-600 italic mb-4">Chaemsaithong 2022 (AJOG PMID 32682859).</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Phuong phap nao tot nhat?</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>ACOG 2013:</b> chi 5% DR - kem</li>
          <li>• <b>NICE 2019:</b> 41% DR - trung binh</li>
          <li>• <b>FMF Triple Test:</b> 75-90% DR - <b style="color:#c8a4a5">tot nhat hien nay</b></li>
          <li>• NNT = 250 (sang loc 250 de phong 1 ca preterm PE)</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">4. ASPRE MAIN RCT (NEJM 2017, n=1776)</h2>
    <p class="text-sm text-stone-600 italic mb-4">Aspirin 150 mg/dem vs Placebo, 11-14 -> 36 tuan.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart2"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">ASPRE (Rolnik 2017, PMID 28657417)</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>Preterm PE:</b> 1.6% aspirin vs 4.3% placebo</li>
          <li>• <b>OR 0.38 (95% CI 0.20-0.74), p = 0.004</b></li>
          <li>• <b>Reduction 62%</b></li>
          <li>• Adherence: 79.9% uong >= 85% lieu</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">5. FMF Triple Test - 4 thanh phan</h2>
    <div class="grid md:grid-cols-2 gap-3">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">1. Maternal risk factors</h3>
        <p class="text-xs text-stone-700">Tuoi, BMI, chung toc, parity, tien su PE, tien su gia dinh, benh nen (HTN, DM, SLE, APS, than), ART, hut thuoc.</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">2. MAP (Mean Arterial Pressure)</h3>
        <p class="text-xs text-stone-700">Do 2 lan, moi ben canh tay, nghi 5 phut. PE som: MAP TANG (dau hieu som nhat).</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">3. PlGF (Placental Growth Factor)</h3>
        <p class="text-xs text-stone-700">Mau me, do ELISA. PE som: PlGF GIAM (&lt; 0.7-0.8 MoM). Day la <b>marker nhay nhat</b>.</p>
      </div>
      <div class="pastel-peach rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">4. UtA-PI (Uterine Artery)</h3>
        <p class="text-xs text-stone-700">Doppler qua ca 2 dong mach tu cung. PE som: UtA-PI TANG + notching som.</p>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">6. EVIDENCE TABLE - 9 papers quan trong</h2>
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
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">28657417</td><td class="px-3 py-2">Rolnik (2017)</td><td class="px-3 py-2">NEJM RCT, n=1776</td><td class="px-3 py-2">Aspirin 150 mg giam 62% preterm PE</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">31111484</td><td class="px-3 py-2">Poon (2019)</td><td class="px-3 py-2">FIGO guideline</td><td class="px-3 py-2">Universal screening + 150 mg aspirin</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">28741785</td><td class="px-3 py-2">Rolnik (2017)</td><td class="px-3 py-2">UOG screening, n=25,797</td><td class="px-3 py-2">FMF Triple Test DR 76.7% preterm PE</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">32682859</td><td class="px-3 py-2">Chaemsaithong (2022)</td><td class="px-3 py-2">AJOG review</td><td class="px-3 py-2">FMF Triple Test vs ACOG/NICE</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">38151219</td><td class="px-3 py-2">Rolnik (2024)</td><td class="px-3 py-2">AJOG secondary</td><td class="px-3 py-2">Aspirin khong anh huong PlGF/PAPP-A</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">37058400</td><td class="px-3 py-2">Rolnik (2023)</td><td class="px-3 py-2">UOG secondary</td><td class="px-3 py-2">Aspirin giam UtA-PI (p=0.006)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">33998099</td><td class="px-3 py-2">Shen (2021)</td><td class="px-3 py-2">UOG secondary</td><td class="px-3 py-2">Chronic HTN + risk rat cao: aspirin kem</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">37749709</td><td class="px-3 py-2">Nicolaides (2024)</td><td class="px-3 py-2">BJOG combined</td><td class="px-3 py-2">FMF + aspirin giam 65% iPTB-PE</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">40590060</td><td class="px-3 py-2">Rolnik (2025)</td><td class="px-3 py-2">BJOG secondary</td><td class="px-3 py-2">Aspirin khong tang LGA</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. Co che 2-step cua PE</h2>
    <div class="mermaid">
flowchart LR
    A["Step 1: Trophoblast xam nhap<br/>spiral arteries kem<br/>(8-18 tuan)"] --> B["Spiral arteries<br/>duong kinh nho, ap luc cao<br/>-> Nhau thieu mau"]
    B --> C["Step 2: Mat can bang<br/>angiogenic factors"]
    C --> D["Tang sFlt-1<br/>Giam PlGF"]
    D --> E["Co that mach<br/>tang HA"]
    D --> F["Ton thuong noi mo<br/>proteinuria, phu"]
    D --> G["Giam tuoi mau<br/>gan, than, nao, nhau"]

    style A fill:#f4c2c2
    style B fill:#f7d1ba
    style C fill:#d4c5e2
    style D fill:#c5d5e0
    style E fill:#c5e0c9
    style F fill:#c5e0c9
    style G fill:#c5e0c9
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. ASPRE Secondary Analyses 2021-2025</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">Phan tich</th>
            <th class="px-3 py-2 text-left">PMID</th>
            <th class="px-3 py-2 text-left">Ket qua chinh</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2">PAPP-A + PlGF trajectories (2024)</td><td class="px-3 py-2 font-mono text-xs">38151219</td><td class="px-3 py-2">Aspirin KHONG anh huong PAPP-A (p=0.259) va PlGF (p=0.335)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2">MAP + UtA-PI trajectories (2023)</td><td class="px-3 py-2 font-mono text-xs">37058400</td><td class="px-3 py-2">Aspirin giam UtA-PI (p=0.006) nhat la truoc 20 tuan, KHONG anh huong MAP (p=0.340)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2">Risk factors that bai (2021)</td><td class="px-3 py-2 font-mono text-xs">33998099</td><td class="px-3 py-2">Chronic HTN + risk rat cao (1:2-1:10) + PlGF &lt; 0.712 MoM: aspirin kem hieu qua</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2">Effect on PTB (2024)</td><td class="px-3 py-2 font-mono text-xs">37749709</td><td class="px-3 py-2">Aspirin giam 65% iPTB-PE, 14% sPTB, 0% iPTB-noPE</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2">Birthweight + LGA (2025)</td><td class="px-3 py-2 font-mono text-xs">40590060</td><td class="px-3 py-2">Aspirin khong tang LGA (5.5% vs 6.2%, p=0.667) - tru dai thao duong</td></tr>
        </tbody>
      </table>
    </div>
  </section>
'''

    custom_charts = '''
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['ACOG 2013', 'NICE 2019', 'FMF Triple Test'],
        datasets: [{
            label: 'Detection Rate - Preterm PE (%)',
            data: [5, 41, 90],
            backgroundColor: [
                'rgba(244, 194, 194, 0.85)',
                'rgba(247, 209, 186, 0.85)',
                'rgba(197, 224, 201, 0.85)'
            ],
            borderColor: [
                'rgba(244, 194, 194, 1)',
                'rgba(247, 209, 186, 1)',
                'rgba(197, 224, 201, 1)'
            ],
            borderWidth: 2
        }, {
            label: 'Detection Rate - Term PE (%)',
            data: [2, 34, 43],
            backgroundColor: [
                'rgba(244, 194, 194, 0.55)',
                'rgba(247, 209, 186, 0.55)',
                'rgba(197, 224, 201, 0.55)'
            ],
            borderColor: [
                'rgba(244, 194, 194, 1)',
                'rgba(247, 209, 186, 1)',
                'rgba(197, 224, 201, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'So sanh 3 phuong phap sang loc PE (Chaemsaithong 2022)' },
            tooltip: {
                callbacks: {
                    afterLabel: function(ctx) {
                        return 'FPR ~10% (ACOG 0.2%)';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
                title: { display: true, text: 'Detection Rate (%)' }
            }
        }
    }
});

new Chart(document.getElementById('chart2'), {
    type: 'bar',
    data: {
        labels: ['Aspirin 150 mg', 'Placebo'],
        datasets: [{
            label: 'Preterm PE incidence (%)',
            data: [1.6, 4.3],
            backgroundColor: [
                'rgba(197, 224, 201, 0.85)',
                'rgba(244, 194, 194, 0.85)'
            ],
            borderColor: [
                'rgba(197, 224, 201, 1)',
                'rgba(244, 194, 194, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        plugins: {
            title: { display: true, text: 'ASPRE MAIN RCT (NEJM 2017) - n=1,776' },
            legend: { display: false },
            tooltip: {
                callbacks: {
                    afterLabel: function(ctx) {
                        return 'OR 0.38 (95% CI 0.20-0.74), p=0.004';
                    }
                }
            }
        },
        scales: {
            x: {
                beginAtZero: true,
                max: 6,
                title: { display: true, text: 'Preterm PE incidence (%)' }
            }
        }
    }
});
'''

    footer_text = 'Bai hoc soan boi MiniMax Mavis cho Bs. Ngoc 🍅 🐈‍⬛ | Verified PubMed: 9 papers (PMID 28657417, 31111484, 28741785, 32682859, 38151219, 37058400, 33998099, 37749709, 40590060) - ASPRE trial Rolnik 2017 NEJM'

    html_content = build_lesson_html(
        title='Sang loc & Du phong Tien san giat - Visual Summary',
        header_html=header_html,
        main_html=main_html,
        footer_text=footer_text,
        custom_charts=custom_charts,
    )
    write_html(html_content, HTML_OUT)
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building PE Screening Lesson - {DATE} ===\n")
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
