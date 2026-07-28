"""Build full lesson: docx + anki apkg + html visual summary.
Topic: First Trimester Screening - 2026-06-22.
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
LESSON_DIR = ROOT / "03_Sieu am thai" / "11_First_Trimester_Screening"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "03_Sieu am thai" / "11_First_Trimester_Screening"
DATE = "2026-06-22"

DOCX_OUT = LESSON_DIR / f"First Trimester Screening - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - First Trimester Screening 20 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - First Trimester Screening - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "first_trimester_screening_cards.json"


def build_docx():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    title = doc.add_heading('FIRST TRIMESTER SCREENING (SANG LOC QUY 1)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bai hoc ngay {DATE} - Sieu am thai ky (Fetal Ultrasound)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TONG QUAN - VI SAO BAI NAY QUAN TRONG?', 1)
    doc.add_paragraph(
        'First trimester screening (FTS) o tuan thai 11+0 den 13+6 ngay (CRL 45-84 mm) la cot moc quan trong nhat trong thai ky vi 3 muc tieu chinh duoc giai quyet trong 1 lan kham:'
    )
    add_bullets(doc, [
        'Xac dinh tuoi thai chinh xac (CRL).',
        'Sang loc bat thuong nhiem sac the (T21, T18, T13) - Combined test hoac NIPT.',
        'Danh gia giai phau thai som (early anatomy scan) - phat hien ~50% di tat lon.',
    ])
    doc.add_paragraph('Theo [ISUOG 2022 - 11-14w Ultrasound] (PMID 36594739) - guideline moi nhat:')
    add_bullets(doc, [
        'BAT BUOC sieu am 11-14 tuan cho moi thai ky.',
        'Combined test (NT + PAPP-A + free beta-hCG) detect ~90% T21 voi false positive 5%.',
        'NIPT (cfDNA) co sensitivity >99% cho T21 nhung KHONG thay the sieu am.',
    ])
    doc.add_paragraph('Bromley B. 2024 (PMID 38723258): "Use of cell-free DNA alone for aneuploidy screening while foregoing an accompanying early anatomic evaluation of the fetus will result in many anomalies that are typically detected in the first trimester not being identified until later in pregnancy."').runs[0].italic = True

    # 1. BA MUC TIEU
    doc.add_heading('1. BA MUC TIEU CHINH CUA FTS', 1)
    doc.add_heading('1.1. Xac dinh tuoi thai', 2)
    add_bullets(doc, [
        'Crown-Rump Length (CRL) la phuong phap chinh xac nhat (Robinson, Hadlock).',
        'Do tu dinh dau den mong thai, thai o tu the trung lap.',
        'Tuoi thai = CRL-based formula, chinh xac +/- 5-7 ngay.',
        'Theo ISUOG 2019 fetal biometry (PMID 31169958): khi CRL > 84 mm (~14 tuan), chuyen sang dung Head Circumference (HC) de dating.',
        'Luu y: neu da co CRL som o 8-10 tuan, KHONG dung sieu am sau de recalculate gestational age.',
    ])

    doc.add_heading('1.2. Sang loc bat thuong NST (Aneuploidy screening)', 2)
    t1 = doc.add_table(rows=4, cols=5)
    fill_table(t1,
        ['Phuong phap', 'Detect rate T21', 'False positive', 'Uu diem', 'Nhuoc diem'],
        [
            ('Combined test\n(NT + PAPP-A + free beta-hCG)', '~90%', '5%', 'Re, tich hop sieu am, phat hien them NT/di tat', 'Can mau me + sieu am'),
            ('NIPT (cfDNA)', '>99% (T21), 98% (T18), 100% (T13)', '<0.1%', 'Sensitivity cao nhat, chi mau me', 'Dat, khong phat hien NT/di tat'),
            ('Contingent (Combined truoc, NIPT neu intermediate)', '~95%', '1-2%', 'Tiet kiem chi phi', 'Phuc tap logistics'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Theo Zhang H. 2015 (PMID 25598039) - NIPT 146,958 pregnancies:')
    add_bullets(doc, [
        'Sensitivity T21: 99.17%.',
        'Sensitivity T18: 98.24%.',
        'Sensitivity T13: 100%.',
        'Specificity: >99.95% cho ca 3 trisomy.',
        'Khong khac biet high-risk vs low-risk populations.',
    ])

    doc.add_heading('1.3. Early anatomy scan', 2)
    doc.add_paragraph('Theo ISUOG 2022 (PMID 36594739) va Bromley 2024 (PMID 38723258):')
    add_bullets(doc, [
        'Phat hien ~50% di tat lon co the thay o 11-14 tuan.',
        'Cau truc co the danh gia: nao (ventricles, choroid plexus), 4 chamber heart, da day, bang quang, cot song, tay chan, day ron (vessels), placenta, amniotic fluid.',
        'Markers quan trong cho aneuploidy: NT day, absence of nasal bone, tricuspid regurgitation, ductus venosus a-wave abnormal.',
    ])

    # 2. NT TECHNIQUE
    doc.add_heading('2. KY THUAT DO NUCHAL TRANSLUCENCY (NT)', 1)
    doc.add_heading('2.1. Yeu cau ky thuat (theo FMF)', 2)
    t2 = doc.add_table(rows=7, cols=2)
    fill_table(t2,
        ['Yeu cau', 'Chi tiet'],
        [
            ('Tuoi thai', '11+0 den 13+6 tuan (CRL 45-84 mm)'),
            ('Mat cat', 'Sagittal (dung doc giua thai)'),
            ('Hinh anh', 'Thai chiem 75% man hinh, mat va nguc thai song song voi probe'),
            ('Vi tri do', 'Vung day nhat cua khoang duoi da sau co (subcutaneous translucency)'),
            ('Calipers', 'ON-ON (dat tren duong trang-trong cua da, khong de vao)'),
            ('Phan biet', 'Da (membranous) khac amnion (o tuoi thai nay chua dinh)'),
        ])
    doc.add_paragraph()

    doc.add_heading('2.2. Dien gia NT', 2)
    t3 = doc.add_table(rows=5, cols=3)
    fill_table(t3,
        ['NT (mm)', 'Y nghia', 'Can lam gi'],
        [
            ('< 3.0 mm (< p95 theo CRL)', 'Binh thuong', 'Tiep tuc routine'),
            ('3.0-3.4 mm', 'Borderline', 'Combined test chi tiet + NIPT can nhac'),
            ('>= 3.5 mm', 'Day', 'Combined test + NIPT + CVS/amniocentesis tu van'),
            ('>= 6.0 mm', 'Rat day', 'Nguy co cao aneuploidy + cardiac defect; can diagnostic test + fetal echo 18-22 tuan'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Luu y: NT day khong chi la aneuploidy - con lien quan: cardiac defect (5-10% thai co NT >= p99 co CHD), genetic syndromes (Noonan, Smith-Lemli-Opitz), fetal anemia (Parvovirus B19, alloimmunization).').runs[0].bold = True

    # 3. COMBINED TEST
    doc.add_heading('3. CO SO SINH HOC CUA COMBINED TEST', 1)
    doc.add_heading('3.1. Nuchal translucency sinh hoc', 2)
    doc.add_paragraph('Khoang duoi da chua dich ke (interstitial fluid). O thai aneuploidy, tang tich tu dich do: roi loan tuan hoan bach huyet, suy tim som, thay doi thanh phan extracellular matrix, tang apoptosis.')

    doc.add_heading('3.2. PAPP-A va free beta-hCG', 2)
    t4 = doc.add_table(rows=4, cols=3)
    fill_table(t4,
        ['Trisomy', 'PAPP-A', 'Free beta-hCG'],
        [
            ('T21', 'GIAM (low MoM)', 'TANG (high MoM)'),
            ('T18', 'GIAM MANH', 'GIAM'),
            ('T13', 'GIAM', 'GIAM'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('PAPP-A: glycoprotein do nhau tiet, tang dan theo tuoi thai. Free beta-hCG: tiet tu hop bao nuoi (syncytiotrophoblast). Pattern khac nhau giup phan biet T21 vs T18/T13 som.')

    doc.add_heading('3.3. Cong thuc tinh risk', 2)
    doc.add_paragraph(
        'Risk = Base risk (theo tuoi me) x Likelihood ratio (LR)\n'
        '     = Base risk x LR(NT) x LR(PAPP-A) x LR(free beta-hCG)\n\n'
        'Vi du: Me 35 tuoi (base risk T21 = 1:350)\n'
        '- NT 2.5 mm (binh thuong) -> LR ~0.5\n'
        '- PAPP-A 0.8 MoM (binh thuong) -> LR ~0.7\n'
        '- Free beta-hCG 1.5 MoM (cao nhe) -> LR ~1.5\n'
        '- Final risk = 1:350 x 0.5 x 0.7 x 1.5 = 1:1111 (giam so voi base risk)\n\n'
        'Phan mem: FMF risk calculator (https://fetalmedicine.org), Astraia, ViewPoint.'
    )

    # 4. NIPT
    doc.add_heading('4. NIPT (NON-INVASIVE PRENATAL TESTING / cfDNA)', 1)
    doc.add_heading('4.1. Co che', 2)
    add_bullets(doc, [
        'Tu tuan thu 5+, cell-free DNA cua thai (cfDNA) xuat hien trong mau me.',
        'cfDNA tu apoptosis cua trophoblast (nhau thai).',
        'Ty le cfDNA thai / tong cfDNA = fetal fraction (thuong 5-15% o 11 tuan).',
        'Phan tich cfDNA bang massively parallel sequencing hoac SNP-based methods.',
    ])

    doc.add_heading('4.2. Hieu qua (Zhang H. 2015, n=146,958)', 2)
    t5 = doc.add_table(rows=4, cols=4)
    fill_table(t5,
        ['Trisomy', 'Sensitivity', 'Specificity', 'PPV (high-risk vs low-risk)'],
        [
            ('T21', '99.17%', '99.95%', '~95% vs ~85%'),
            ('T18', '98.24%', '99.95%', '~90% vs ~70%'),
            ('T13', '100%', '99.96%', '~85% vs ~50%'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Luu y: PPV (positive predictive value) phu thuoc vao a priori risk - o low-risk population, PPV thap hon vi prevalence thap.')

    doc.add_heading('4.3. Han che cua NIPT', 2)
    add_bullets(doc, [
        'CHI SANG LOC, KHONG CHAN DOAN (ACMG 2016): Positive NIPT -> CAN diagnostic test (CVS/amniocentesis) truoc khi quyet dinh. Negative NIPT -> van can theo doi sieu am.',
        'Test failure ~2-5%: thai qua som, fetal fraction thap, maternal obesity.',
        'False positive: confined placental mosaicism (CPM), maternal CNV, vanishing twin, maternal malignancy (hiem).',
        'False negative: fetal fraction thap (< 4%), mosaicism thap, maternal obesity (BMI > 35).',
        'NIPT KHONG phat hien: structural fetal anomalies, NT day, pre-eclampsia screening markers, monochorionic twins co han che.',
    ])

    doc.add_paragraph('Theo Suciu 2021 (PMID 31766927): "Introducing screening by NIPT instead of a first-trimester screening will cause the loss of other valuable information including accurate dating of pregnancy, diagnosing major structural fetal abnormalities and multiple pregnancies at an early gestational age."').runs[0].italic = True

    doc.add_heading('4.4. NIPT mo rong (Beyond common trisomies)', 2)
    doc.add_paragraph('Mot so lab cung cap:')
    add_bullets(doc, [
        'Sex chromosome aneuploidy (Turner 45,X, Klinefelter 47,XXY): nhay hon nhung PPV thap.',
        'Microdeletion syndromes (22q11.2 = DiGeorge, 1p36, etc.): PPV rat thap.',
        'Rare autosomal trisomy (RAT).',
    ])
    doc.add_paragraph('=> Can nhac ky truoc khi offer extended NIPT vi PPV thap co the dan den unnecessary invasive procedures.').runs[0].bold = True

    # 5. EARLY ANATOMY
    doc.add_heading('5. FIRST TRIMESTER ANATOMY SCAN (EARLY ANATOMY)', 1)
    doc.add_heading('5.1. Cau truc danh gia duoc o 11-14 tuan', 2)
    doc.add_paragraph('Theo ISUOG 2022 (PMID 36594739) va Bromley 2024 (PMID 38723258): phat hien ~50% di tat lon.')
    add_bullets(doc, [
        'Nao: skull, midline, choroid plexus, ventricles.',
        'Mat: orbits, nasal bone, profile.',
        'Tim: 4-chamber view (thuong), outflow tracts (kho hon).',
        'Bung: stomach, liver, kidneys, bladder.',
        'Cot song: 3 vung (co, nguc, that lung).',
        'Tu chi: 3 segments (dui, cang, ban).',
        'Day ron: 3 vessels.',
        'Placenta, amniotic fluid.',
    ])
    doc.add_paragraph('Bromley 2024: nen offer cho MOI thai phu khong phu thuoc ket qua aneuploidy screening.').runs[0].bold = True

    doc.add_heading('5.2. Markers quan trong cho aneuploidy', 2)
    t6 = doc.add_table(rows=6, cols=6)
    fill_table(t6,
        ['Marker', 'T21', 'T18', 'T13', 'Turner', 'Cach danh gia'],
        [
            ('NT day (>= p95)', '+++', '+++', '+++', '+++', 'Do nhu muc 2'),
            ('Absent/hypoplastic nasal bone', '+++', '++', '+', '-', 'Profile view, 11-13 tuan'),
            ('Tricuspid regurgitation', '++', '+', '+', '-', 'Doppler qua valve 3 la'),
            ('Abnormal DV a-wave', '++', '+++', '+', '+++', 'Doppler DV'),
            ('Aberrant right subclavian artery', '+', '-', '-', '-', '3VT view'),
        ])
    doc.add_paragraph()

    # 6. ALGORITHM
    doc.add_heading('6. ALGORITHM SANG LOC ANEUPLOIDY - 2024', 1)
    doc.add_paragraph('Theo ISUOG 2022 + ACMG 2020 + ACOG:')
    doc.add_paragraph(
        'Thai 11-13+6 tuan -> Sieu am 11-14 tuan (ISUOG) -> Danh gia nguy co co ban.\n\n'
        'Buoc 1: Nguyen co cao (me >= 35, tien su aneuploidy, NT >= 3.5 mm, structural anomaly)?\n'
        '-> Tu van diagnostic test (CVS/amniocentesis) + NIPT neu khong muon invasive.\n\n'
        'Buoc 2: Nguyen co trung binh (me < 35, khong yeu to nguy co)?\n'
        '-> Combined test HOAC NIPT (neu co dieu kien).\n\n'
        'Buoc 3: Nguyen co thap (me tre, binh thuong)?\n'
        '-> Combined test (NIPT khong khuyen cao vi PPV thap).\n\n'
        'Buoc 4: Ket qua Combined:\n'
        '- High risk (>= 1:150) -> diagnostic test hoac NIPT.\n'
        '- Intermediate (1:151-1:1000) -> NIPT (Contingent).\n'
        '- Low risk (< 1:1000) -> Tiep tuc routine, anatomy scan 18-22 tuan.'
    )

    # 7. CONTINGENT
    doc.add_heading('7. CONTINGENT SCREENING - CHIEN LUOC TIET KIEM', 1)
    doc.add_paragraph('Theo Suciu 2021 (PMID 31766927):')
    add_bullets(doc, [
        'Contingent = Combined test truoc, NIPT cho nhom intermediate risk.',
        'Uu diem: tiet kiem chi phi so voi NIPT cho tat ca, van duy tri detection rate cao (>95% voi cut-off toi uu), phu hop voi public health system.',
        'Cac nuoc da ap dung: UK (NHS), Dan Mach, Ha Lan, mot so bang Australia, mot so tinh Trung Quoc.',
        'Cut-off dien hinh: NIPT cho nhom risk 1:100 den 1:1000 (mot so he thong 1:50 den 1:2500).',
    ])

    # 8. TWINS
    doc.add_heading('8. ANEUPLOIDY SCREENING TRONG TWINS', 1)
    doc.add_paragraph('Theo Hopkins 2023 (PMID 37438894):')
    add_bullets(doc, [
        'NIPT first-line cho twins (ca MC va DC) theo ACOG/SMFM 2020.',
        'Neu NIPT khong kha thi: Combined test (NT do ca 2 thai) + serum markers.',
        'NT cut-off o twins: van dung nguong singleton (chua co consensus rieng).',
        'Chorionicity phai xac dinh o 11-14 tuan (lambda sign hoac T-sign).',
        'NIPT o DC twins: sens T21 ~95% (thap hon singleton ~99%), T13 ~80%.',
        'NIPT o MC twins: tuong duong singleton (vi cung cfDNA).',
        'Vanishing twin: NIPT co the false positive do cfDNA thai chet.',
    ])

    # 9. PLACENTA MARKERS
    doc.add_heading('9. PLACENTA MARKERS - MORTAKI 2024', 1)
    doc.add_paragraph('Theo Mortaki A. 2024 (PMID 39305990) - meta-analysis 8 studies, 1,886 patients:')
    add_bullets(doc, [
        'First trimester biomarkers cho Placenta Accreta Spectrum (PAS):',
        '   - PAPP-A: PAS > previa (MD 0.48 MoM; 95% CI 0.23-0.73, p=0.0001).',
        '   - Free beta-hCG: previa > binh thuong (MD 0.27 MoM; 95% CI 0.17-0.38, p<0.00001).',
        'Y nghia: First trimester combined test co the giup sang loc som PAS o thai phu co nguy co (tien su mo lay thai + placenta previa).',
        'Luu y: Can nhac PAS neu thai phu co tien su mo lay thai nhieu lan + placenta previa, dac biet o vung sau (posterior) hoac anterior low-lying.',
    ])

    # 10. EVIDENCE
    doc.add_heading('10. EVIDENCE & GUIDELINES', 1)
    doc.add_heading('10.1. [ISUOG 2022 - 11-14w Ultrasound] (PMID 36594739)', 2)
    doc.add_paragraph('MAIN GUIDELINE cho first trimester scan. Bilardo et al. UOG 2023;61(1):127-143.')
    doc.add_paragraph('Khuyen cao chinh:')
    add_bullets(doc, [
        'BAT BUOC sieu am 11-14 tuan cho moi thai ky.',
        '3 muc tieu: dating, aneuploidy, anatomy.',
        'NT do theo chuan FMF.',
        'Combined test la lua chon dau tay cho aneuploidy.',
        'Early anatomy scan nen co gang danh gia o muc toi da.',
        'NIPT la advanced screening test (chi khi co chi dinh).',
    ])

    doc.add_heading('10.2. ACOG / SMFM 2020 (Practice Bulletin #226)', 2)
    add_bullets(doc, [
        'Universal aneuploidy screening offered cho moi thai phu.',
        'NIPT la mot trong cac lua chon valid cho high-risk va low-risk.',
        'KHONG dung NIPT thay the sieu am.',
        'Diagnostic test (CVS/amniocentesis) can offer cho high-risk results.',
    ])

    doc.add_heading('10.3. ACMG 2020', 2)
    add_bullets(doc, [
        'NIPT la advanced screening (khong phai diagnostic).',
        'Positive NIPT -> can diagnostic confirmation truoc khi quyet dinh thai ky.',
        'Nen offer screening cho moi thai phu (khong chi high-risk).',
    ])

    doc.add_heading('10.4. Tong hop evidence', 2)
    t7 = doc.add_table(rows=8, cols=4)
    fill_table(t7,
        ['Paper', 'N', 'Loai', 'Ket qua chinh'],
        [
            ('ISUOG 2022 (PMID 36594739)', 'Consensus 10 experts', 'Practice guideline', 'Standard 11-14w scan'),
            ('Bromley 2024 (PMID 38723258)', 'Review', 'Clinical recommendation', 'Early anatomy scan tat ca thai phu'),
            ('Zhang 2015 (PMID 25598039)', '146,958', 'Clinical series', 'NIPT sens 99% (T21)'),
            ('Hopkins 2023 (PMID 37438894)', 'Review', 'Clinical recommendation', 'NIPT first-line cho twins'),
            ('Mortaki 2024 (PMID 39305990)', '1,886 (8 studies)', 'Meta-analysis', 'PAS biomarkers tang Q1'),
            ('Suciu 2021 (PMID 31766927)', 'Review', 'Survey + analysis', 'Contingent screening tiet kiem'),
            ('Salomon 2019 (PMID 31169958)', 'Consensus', 'ISUOG biometry', 'HC khi CRL > 84 mm'),
        ])
    doc.add_paragraph()

    # 11. TIPS
    doc.add_heading('11. TIPS THUC HANH (CLINICAL PEARLS)', 1)
    add_bullets(doc, [
        '3 muc tieu FTS = dating + aneuploidy + anatomy. KHONG chi la aneuploidy screening.',
        'CRL > 84 mm (~14 tuan) -> chuyen sang dung HC de dating (theo ISUOG 2019 fetal biometry).',
        'NT ON-ON, mat cat sagittal, thai o tu the trung lap, phan biet da voi amnion.',
        'NT day >= 3.5 mm: tu van diagnostic test (CVS/amniocentesis) + fetal echo 18-22 tuan (du karyotype binh thuong).',
        'Combined test = NT + PAPP-A + free beta-hCG. Pattern dac trung: T21 tang beta giam PAPP-A, T18 giam manh PAPP-A, T13 giam beta giam PAPP-A.',
        'NIPT sens >99% T21 nhung KHONG thay the sieu am (khong phat hien NT/di tat).',
        'Positive NIPT -> diagnostic test (CVS/amniocentesis) truoc khi quyet dinh thai ky (ACMG 2020).',
        'NIPT test failure (~2-5%): thai som, obesity, fetal fraction thap. KHONG lap lai NIPT - chuyen sang combined test hoac diagnostic.',
        'Twins aneuploidy screening: NIPT first-line. Chorionicity xac dinh o 11-14 tuan.',
        'Vanishing twin: NIPT co the false positive. Can khai thac tien su thai ky ky.',
    ])

    # 12. TONG KET
    doc.add_heading('12. TONG KET DIEM CAN NHO', 1)
    add_numbered(doc, [
        'First trimester screening 11+0 den 13+6 tuan (CRL 45-84 mm) - 3 muc tieu: dating, aneuploidy, anatomy.',
        '[ISUOG 2022 - 11-14w Ultrasound] (PMID 36594739): BAT BUOC sieu am 11-14 tuan cho moi thai ky.',
        'Combined test (NT + PAPP-A + free beta-hCG): detect ~90% T21 voi false positive 5%.',
        'NIPT (Zhang 2015, n=146,958): sens 99.17% T21, 98.24% T18, 100% T13; specificity >99.95%.',
        'NT day >= 3.5 mm: tu van diagnostic test + fetal echo 18-22 tuan.',
        'Early anatomy scan (Bromley 2024): phat hien ~50% di tat lon, nen offer cho moi thai phu.',
        'Positive NIPT -> CAN diagnostic test (CVS/amniocentesis) truoc khi quyet dinh thai ky.',
        'Twins: NIPT first-line theo ACOG 2020. Chorionicity xac dinh 11-14 tuan.',
        'Contingent screening: Combined truoc, NIPT cho intermediate risk - tiet kiem chi phi.',
        'CRL > 84 mm -> dung HC de dating. NT do ON-ON, mat cat sagittal, phan biet da voi amnion.',
    ])

    # 13. TAI LIEU
    doc.add_heading('13. TAI LIEU THAM KHAO (VERIFY PUBMED)', 1)
    refs = [
        ('International Society of Ultrasound in Obstetrics and Gynecology; Bilardo CM, Chaoui R, Hyett JA, et al. (2022)', 'PMID: 36594739', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.26106', '"Practice guidelines (updated): performance of 11-14-week ultrasound scan."'),
        ('Bromley B, Platt LD. (2024)', 'PMID: 38723258', 'Obstet Gynecol.', 'DOI: 10.1097/AOG.0000000000005594', '"First-Trimester Ultrasound Screening in Routine Obstetric Practice."'),
        ('Zhang H, Gao Y, Jiang F, et al. (2015)', 'PMID: 25598039', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.14792', '"Non-invasive prenatal testing for trisomies 21, 18 and 13: clinical experience from 146,958 pregnancies."'),
        ('Hopkins MK, Neumann O, Kuller JA, Dugoff L. (2023)', 'PMID: 37438894', 'Clin Obstet Gynecol.', 'DOI: 10.1097/GRF.0000000000000797', '"First Trimester Ultrasound and Aneuploidy Screening in Twins."'),
        ('Mortaki A, Douligeris A, Panagiotopoulos M, et al. (2024)', 'PMID: 39305990', 'J Obstet Gynaecol Can.', 'DOI: 10.1016/j.jogc.2024.102663', '"First- and Second-Trimester Aneuploidy Screening Biomarkers and Risk Assessment of Placenta Previa and Accreta: A Systematic Review and Meta-Analysis."'),
        ('Suciu I, Galeva S, Abdel Azim S, Pop L, Toader O. (2021)', 'PMID: 31766927', 'J Matern Fetal Neonatal Med.', 'DOI: 10.1080/14767058.2019.1698031', '"First-trimester screening-biomarkers and cell-free DNA."'),
        ('Salomon LJ, Alfirevic Z, Da Silva Costa F, et al. (2019)', 'PMID: 31169958', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.20272', '"ISUOG Practice Guidelines: ultrasound assessment of fetal biometry and growth."'),
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
        model_id=1607392322,
        model_name='First Trimester Screening - Pastel',
        deck_id=2059400113,
        deck_name='First Trimester Screening - 22/06/2026',
        deck_description='First Trimester Screening 11+0-13+6w: NT, combined test, NIPT, anatomy - 22/06/2026 - Pastel theme'
    )
    n = add_cards_from_json(deck, model, CARDS_JSON, 'Fetal US · First Trimester · NIPT · Aneuploidy')
    write_apkg(deck, APKG_OUT)
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {n}")


def build_html():
    header_html = '''
<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">First Trimester Screening (Sang loc Quy 1)</h1>
  <p class="text-stone-500 italic">Visual Summary - Bai hoc 22/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">Fetal US</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">11-14w Scan</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">NT / Combined</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">NIPT / cfDNA</span>
    <span class="tag pastel-lavender px-3 py-1 rounded-full text-sm">Aneuploidy</span>
  </div>
</header>
'''

    main_html = '''
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. 3 muc tieu FTS (11+0 den 13+6 tuan)</h2>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">1. Dating</h3>
        <p class="text-sm text-stone-700">Xac dinh tuoi thai chinh xac qua <b>CRL</b> (chinh xac +/- 5-7 ngay). Khi CRL > 84 mm chuyen sang HC.</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">2. Aneuploidy screening</h3>
        <p class="text-sm text-stone-700"><b>Combined test</b> (NT + PAPP-A + free beta-hCG) hoac <b>NIPT</b> (cfDNA). Detect T21 ~90-99%.</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">3. Early anatomy</h3>
        <p class="text-sm text-stone-700">Phat hien <b>~50% di tat lon</b>. Cau truc: nao, tim, bung, cot song, tu chi, day ron, placenta.</p>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Algorithm FTS 2024 (theo ISUOG 2022 + ACMG + ACOG)</h2>
    <div class="mermaid">
flowchart TD
    A["Thai 11-13+6 tuan<br/>Sieu am ISUOG<br/>+ Danh gia base risk"] --> B{"Nguy co cao?<br/>(me >= 35,<br/>tier su aneuploidy,<br/>NT >= 3.5 mm,<br/>structural anomaly)"}
    B -- "Co" --> Z1["Tu van diagnostic test<br/>(CVS hoac amniocentesis)<br/>+ NIPT neu khong muon invasive"]
    B -- "Khong" --> C{"Nguy co trung binh?<br/>(me < 35,<br/>khong yeu to nguy co)"}
    C -- "Co" --> D["Combined test<br/>HOAC NIPT<br/>(neu co dieu kien)"]
    C -- "Khong (thap)" --> E["Combined test<br/>(NIPT khong khuyen cao<br/>vi PPV thap)"]
    D --> F{"Ket qua Combined"}
    E --> F
    F -- "High risk >= 1:150" --> Z1
    F -- "Intermediate 1:151-1:1000" --> Z2["NIPT<br/>(Contingent screening)"]
    F -- "Low risk < 1:1000" --> Z3["Tiep tuc routine<br/>+ Anatomy scan 18-22 tuan"]

    style Z1 fill:#f4c2c2
    style Z2 fill:#c5d5e0
    style Z3 fill:#c5e0c9
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">3. NIPT performance (Zhang 2015, n=146,958)</h2>
    <p class="text-sm text-stone-600 italic mb-4">Clinical experience BGI - 146,958 pregnancies, khong khac biet high-risk vs low-risk.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">NIPT (cfDNA) - Zhang 2015</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>Sensitivity T21:</b> 99.17%</li>
          <li>• <b>Sensitivity T18:</b> 98.24%</li>
          <li>• <b>Sensitivity T13:</b> 100%</li>
          <li>• <b>Specificity:</b> >99.95% ca 3 trisomy</li>
          <li>• PPV phu thuoc a priori risk (low-risk co PPV thap hon)</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">4. Combined test - Pattern dac trung</h2>
    <p class="text-sm text-stone-600 italic mb-4">PAPP-A va free beta-hCG giup phan biet T21 vs T18 vs T13 som.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart2"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Pattern biochem</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>T21:</b> PAPP-A giam, free beta-hCG tang</li>
          <li>• <b>T18:</b> PAPP-A giam manh, beta-hCG giam</li>
          <li>• <b>T13:</b> PAPP-A giam, beta-hCG giam</li>
          <li>• Risk = base risk x LR(NT) x LR(PAPP-A) x LR(beta-hCG)</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">5. EVIDENCE TABLE</h2>
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
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">36594739</td><td class="px-3 py-2">ISUOG 2022 (Bilardo et al.)</td><td class="px-3 py-2">Practice guideline</td><td class="px-3 py-2">Standard 11-14w scan, 3 muc tieu</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">38723258</td><td class="px-3 py-2">Bromley (2024)</td><td class="px-3 py-2">Clinical recommendation</td><td class="px-3 py-2">Early anatomy scan tat ca thai phu</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">25598039</td><td class="px-3 py-2">Zhang (2015)</td><td class="px-3 py-2">Clinical series, n=146,958</td><td class="px-3 py-2">NIPT sens 99% T21</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">37438894</td><td class="px-3 py-2">Hopkins (2023)</td><td class="px-3 py-2">Review</td><td class="px-3 py-2">NIPT first-line cho twins</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">39305990</td><td class="px-3 py-2">Mortaki (2024)</td><td class="px-3 py-2">Meta 1,886 (8 studies)</td><td class="px-3 py-2">PAS biomarkers tang Q1</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">31766927</td><td class="px-3 py-2">Suciu (2021)</td><td class="px-3 py-2">Review</td><td class="px-3 py-2">Contingent screening tiet kiem</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">31169958</td><td class="px-3 py-2">Salomon (2019)</td><td class="px-3 py-2">ISUOG biometry</td><td class="px-3 py-2">HC khi CRL > 84 mm</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">6. So sanh Combined vs NIPT vs Contingent</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">Phuong phap</th>
            <th class="px-3 py-2 text-left">Detect T21</th>
            <th class="px-3 py-2 text-left">FPR</th>
            <th class="px-3 py-2 text-left">Uu diem</th>
            <th class="px-3 py-2 text-left">Nhuoc diem</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Combined test</td><td class="px-3 py-2">~90%</td><td class="px-3 py-2">5%</td><td class="px-3 py-2">Re, tich hop sieu am, phat hien NT/di tat</td><td class="px-3 py-2">Can mau me + sieu am</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">NIPT</td><td class="px-3 py-2">>99%</td><td class="px-3 py-2"><0.1%</td><td class="px-3 py-2">Sens cao nhat, chi mau me</td><td class="px-3 py-2">Dat, khong phat hien NT/di tat</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Contingent</td><td class="px-3 py-2">~95%</td><td class="px-3 py-2">1-2%</td><td class="px-3 py-2">Tiet kiem chi phi</td><td class="px-3 py-2">Phuc tap logistics</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. 5 markers aneuploidy Q1</h2>
    <div class="mermaid">
flowchart LR
    A["NT day<br/>(>= p95)"] --> B["Absent/hypoplastic<br/>nasal bone"]
    B --> C["Tricuspid<br/>regurgitation"]
    C --> D["Abnormal DV<br/>a-wave"]
    D --> E["Aberrant right<br/>subclavian artery"]

    style A fill:#f4c2c2
    style B fill:#c5d5e0
    style C fill:#c5e0c9
    style D fill:#f7d1ba
    style E fill:#d4c5e2
    </div>
    <p class="text-sm text-stone-600 mt-3 italic">NT day + 4 markers khac giup phat hien som T21, T18, T13, Turner. Markers co do nhay khac nhau cho moi loai trisomy.</p>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. Han che quan trong cua NIPT (5 diem)</h2>
    <div class="grid md:grid-cols-2 gap-3">
      <div class="pastel-pink rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">1. CHI SANG LOC, KHONG CHAN DOAN</h3>
        <p class="text-xs text-stone-700">Positive NIPT CAN diagnostic test truoc khi quyet dinh thai ky</p>
      </div>
      <div class="pastel-blue rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">2. Test failure ~2-5%</h3>
        <p class="text-xs text-stone-700">Thai som, fetal fraction thap, maternal obesity</p>
      </div>
      <div class="pastel-mint rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">3. False positive</h3>
        <p class="text-xs text-stone-700">Confined placental mosaicism, maternal CNV, vanishing twin, malignancy</p>
      </div>
      <div class="pastel-peach rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">4. False negative</h3>
        <p class="text-xs text-stone-700">Fetal fraction < 4%, mosaicism thap, BMI > 35</p>
      </div>
      <div class="pastel-lavender rounded-xl p-3">
        <h3 class="font-bold text-stone-800 mb-1 text-sm">5. NIPT khong phat hien</h3>
        <p class="text-xs text-stone-700">Structural anomalies, NT day, pre-eclampsia markers, MC twins</p>
      </div>
    </div>
  </section>
'''

    custom_charts = '''
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['T21', 'T18', 'T13'],
        datasets: [{
            label: 'Sensitivity (%)',
            data: [99.17, 98.24, 100],
            backgroundColor: 'rgba(197, 213, 224, 0.85)',
            borderColor: 'rgba(197, 213, 224, 1)',
            borderWidth: 2
        }, {
            label: 'Specificity (%)',
            data: [99.95, 99.95, 99.96],
            backgroundColor: 'rgba(197, 224, 201, 0.85)',
            borderColor: 'rgba(197, 224, 201, 1)',
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Zhang 2015 - NIPT n=146,958 pregnancies' },
            tooltip: {
                callbacks: {
                    afterLabel: function(ctx) {
                        const i = ctx.dataIndex;
                        const sens = [99.17, 98.24, 100];
                        const spec = [99.95, 99.95, 99.96];
                        if (ctx.datasetIndex === 0) return 'Specificity: ' + spec[i] + '%';
                        return 'Sensitivity: ' + sens[i] + '%';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: false,
                min: 95,
                max: 100,
                title: { display: true, text: 'Performance (%)' }
            }
        }
    }
});

new Chart(document.getElementById('chart2'), {
    type: 'bar',
    data: {
        labels: ['T21 (PAPP-A)', 'T21 (beta-hCG)', 'T18 (PAPP-A)', 'T18 (beta-hCG)', 'T13 (PAPP-A)', 'T13 (beta-hCG)'],
        datasets: [{
            label: 'MoM thay doi (Giam/Tang)',
            data: [0.5, 2.0, 0.3, 0.5, 0.5, 0.5],
            backgroundColor: [
                'rgba(244, 194, 194, 0.85)', 'rgba(197, 224, 201, 0.85)',
                'rgba(244, 194, 194, 0.85)', 'rgba(244, 194, 194, 0.85)',
                'rgba(244, 194, 194, 0.85)', 'rgba(244, 194, 194, 0.85)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        plugins: {
            title: { display: true, text: 'Pattern PAPP-A + free beta-hCG (MoM thay doi)' },
            legend: { display: false },
            annotation: { annotations: {} }
        },
        scales: {
            x: {
                beginAtZero: true,
                title: { display: true, text: 'MoM (Multiple of Median)' }
            }
        }
    }
});
'''

    footer_text = 'Bai hoc soan boi MiniMax Mavis cho Bs. Ngoc 🍅 🐈‍⬛ | Verified PubMed: 7 papers (PMID 36594739, 38723258, 25598039, 37438894, 39305990, 31766927, 31169958)'

    html_content = build_lesson_html(
        title='First Trimester Screening - Visual Summary',
        header_html=header_html,
        main_html=main_html,
        footer_text=footer_text,
        custom_charts=custom_charts,
    )
    write_html(html_content, HTML_OUT)
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building First Trimester Screening Lesson - {DATE} ===\n")
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
