"""Build full lesson: docx + anki apkg + html visual summary.
Topic: Fetal Doppler Ultrasound trong san khoa - 2026-06-19.

Refactored: dung shared utilities tu lesson_builder.py (boilerplate giam 60%).
"""
import json
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
LESSON_DIR = ROOT / "03_Sieu am thai" / "10_Fetal_Doppler"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "10_Fetal_Doppler"
DATE = "2026-06-19"

DOCX_OUT = LESSON_DIR / f"Fetal Doppler thai ky - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - Fetal Doppler thai ky 20 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - Fetal Doppler thai ky - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "fetal_doppler_cards.json"

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
    title = doc.add_heading('FETAL DOPPLER ULTRASOUND TRONG SAN KHOA', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bai hoc ngay {DATE} - Sieu am thai ky (Fetal Ultrasound)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TONG QUAN - VI SAO BAI NAY QUAN TRONG?', 1)
    doc.add_paragraph(
        'Doppler thai ky la mot trong nhung tien bo quan trong nhat cua san khoa hien dai, cho phep bac si '
        'danh gia chuc nang nhau thai va tinh trang thai mot cach khong xam lan. Ba mach mau cot loi can khao sat:\n'
        '- Umbilical artery (UA): phan anh suc can tuan hoan nhau-nhau (uteroplacental + fetoplacental).\n'
        '- Middle cerebral artery (MCA): phan anh su phan phoi mau len nao ("brain-sparing effect").\n'
        '- Ductus venosus (DV): phan anh chuc nang tim thai va tinh trang toan.'
    )
    doc.add_paragraph('Bac si san phu khoa can nam Doppler thai vi:')
    add_bullets(doc, [
        'FGR (Fetal Growth Restriction): la nguyen nhan hang dau gay tu vong chu sinh o thai ky du thanh (chiem ~10% pregnancies, theo SMFM 2020 PMID 32407785). Doppler UA la tieu chuan vang de theo doi.',
        'Anemia thai: MCA-PSV >= 1.5 MoM la test khong xam lan thay the cordocentesis.',
        'Preeclampsia screening: Uterine artery Doppler o quy 1-2 giup sang loc som.',
        'Twin pregnancy: Doppler giup phan biet TTTS (twin-to-twin transfusion syndrome) va theo doi su phat trien khong deu.',
    ])
    doc.add_paragraph('Theo [ISUOG 2021 - Doppler] Practice Guidelines (Bhide A. et al., PMID 34278615), Doppler velocimetry nen duoc su dung theo chi dinh lam sang ro rang, KHONG phai routine trong moi thai ky.')

    # 1. CO CHE
    doc.add_heading('1. CO CHE SINH LY - TAI SAO DOPPLER HOAT DONG?', 1)
    doc.add_heading('1.1. Nguyen ly Doppler co ban', 2)
    doc.add_paragraph(
        'Hieu ung Doppler mo ta su thay doi tan so song am khi nguon phat (hong cau) chuyen dong tuong doi voi dau do:\n'
        'Delta f = 2 x f0 x v x cos(theta) / c\n\n'
        'Trong do:\n'
        '- Delta f = shift tan so\n'
        '- f0 = tan so phat\n'
        '- v = van toc dong mau\n'
        '- theta = goc giua chum sieu am va dong mau (ly tuong < 30 do)\n'
        '- c = van toc am trong mo (~1540 m/s)\n\n'
        'Luu y thuc hanh: Giu goc insonation < 30 do de tinh van toc chinh xac. Khi goc > 30 do, sai so tang nhanh.'
    )

    doc.add_heading('1.2. Cac chi so Doppler quan trong', 2)
    t1 = doc.add_table(rows=5, cols=3)
    fill_table(t1,
        ['Chi so', 'Cong thuc', 'Y nghia lam sang'],
        [
            ('S/D ratio (Systolic/Diastolic)', 'PSV / EDV', 'Ty le tam thu/tam truong'),
            ('PI (Pulsatility Index) - Gosling', '(PSV - EDV) / TAV', 'Pho bien nhat'),
            ('RI (Resistance Index) - Pourcelot', '(PSV - EDV) / PSV', 'It dung hon PI'),
            ('PSV (Peak Systolic Velocity)', 'Van toc dinh tam thu', 'Dung cho MCA-PSV (anemia)'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Nguyen tac sinh ly:').runs[0].bold = True
    add_bullets(doc, [
        'PI/RI TANG = suc can mach mau TANG -> dong mau kho di qua (vd: UA-PI cao = nhau xo hoa, mach mau nhau bi pha huy).',
        'PI/RI GIAM = suc can GIAM -> dong mau de di qua (vd: MCA-PI giam o FGR = "brain-sparing" - nao co mach it de nhan nhieu mau hon).',
    ])

    doc.add_heading('1.3. Tai sao Doppler UA phan anh suc khoe nhau?', 2)
    doc.add_paragraph(
        'Binh thuong, mach mau nhau (villi) phat trien theo kieu "mach mau hoa thap -> mach mau hoa cao":\n'
        '- Quy 1: Dong mach nhau co thanh day, co tron nhieu -> suc can CAO -> EDV thap, co the am tinh.\n'
        '- Quy 2-3: Mach mau nhau phat trien, thanh mong -> suc can GIAM -> EDV tang dan.\n\n'
        'Khi nhau SUY (FGR do nguyen nhan nhau):\n'
        '- Villi it mach mau hoa, mo dem tang.\n'
        '- Suc can UA tang -> PI/RI tang.\n'
        '- EDV giam dan, co the MAT (absent EDV) hoac DAO NGUOC (reversed EDV) = dau hieu nang.'
    )

    doc.add_heading('1.4. Tai sao MCA-PSV phan anh anemia?', 2)
    add_bullets(doc, [
        'Khi thai thieu mau -> do nhot mau GIAM -> dong chay tang van toc.',
        'Nao uu tien nhan mau (tang cardiac output den nao) -> MCA-PSV TANG.',
        'Nguong MCA-PSV >= 1.5 MoM (multiple of median) = canh bao anemia trung binh-nang.',
        'Day la test khong xam lan thay the cordocentesis, theo Martinez-Portilla 2019 meta-analysis (PMID 30932276).',
    ])

    # 2. UA DOPPLER
    doc.add_heading('2. UMBILICAL ARTERY (UA) DOPPLER - MACH MAU CO BAN NHAT', 1)
    doc.add_heading('2.1. Ky thuat do (theo [ISUOG 2021 - Doppler], PMID 34278615)', 2)
    add_bullets(doc, [
        'Vi tri lay mau: Day ron tu do (free loop), TRANH gan bam ron (~5 cm tu cho bam).',
        'Goc insonation: < 30 do.',
        'Ky thuat: Sample volume 2-4 mm, gate dat o giua lumen day ron.',
        'Tin hieu chat luong: Hinh dang song ro, it nhieu, >= 5 song lien tiep dong nhat.',
        'Cach tinh: Do tren nhieu song roi lay trung binh.',
    ])

    doc.add_heading('2.2. Dien gia gia tri UA-PI', 2)
    doc.add_paragraph('Theo SMFM 2020 (PMID 32407785) va [ISUOG 2021 - Doppler] (PMID 34278615):')
    t2 = doc.add_table(rows=6, cols=3)
    fill_table(t2,
        ['UA Doppler', 'Y nghia', 'Xu tri'],
        [
            ('Binh thuong (PI < p95)', 'Nhau hoat dong tot', 'Theo doi thuong quy'),
            ('PI tang (>= p95)', 'Suc can tang - nghi ngo suy nhau', 'Tang tan suat theo doi (1-2 lan/tuan)'),
            ('EDV giam (decreased)', 'Bat dau suy nhau ro', 'Doppler 1-2 lan/tuan (GRADE 2C)'),
            ('Absent EDV (AEDV)', 'Suy nhau nang', 'Doppler 2-3 lan/tuan, can nhac corticosteroid (GRADE 1C)'),
            ('Reversed EDV (REDV)', 'Suy nhau rat nang', 'Nhap vien, corticosteroid, can nhac can thiep (GRADE 2C)'),
        ])
    doc.add_paragraph()

    doc.add_heading('2.3. Quyet dinh thoi diem sinh theo SMFM 2020 (PMID 32407785)', 2)
    t3 = doc.add_table(rows=5, cols=3)
    fill_table(t3,
        ['Tinh huong', 'Thoi diem sinh', 'GRADE'],
        [
            ('FGR + EFW < p3 hoac UA-PI tang (decreased diastolic flow)', '37 tuan', '1B'),
            ('FGR + UA binh thuong + EFW p3-p10', '38-39 tuan', '2C'),
            ('FGR + Absent EDV', '33-34 tuan', '1B'),
            ('FGR + Reversed EDV', '30-32 tuan', '1B'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Luu y quan trong: UA Doppler BINH THUONG KHONG loai tru FGR, vi late-onset FGR (~70% cac ca) thuong co UA-PI binh thuong. Can ket hop MCA + CPR (xem phan 4-5).').runs[0].bold = True

    doc.add_heading('2.4. Mach mau tu cung (Uterine Artery) - Tien san giat', 2)
    doc.add_paragraph(
        'Theo Cao L. et al. 2024 (PMID 38805623) meta-analysis, uterine artery Doppler co gia tri sang loc:\n'
        '- Quy 1 (11-14 tuan): PI cao + notching = tang nguy co preeclampsia + FGR.\n'
        '- Ket hop voi PAPP-A, PlGF: hieu qua sang loc tang (ASPRE trial, Rolnik 2017 PMID 28741785, dung aspirin 150 mg/dem tu 11-14 tuan -> giam 62% preterm preeclampsia).'
    )

    # 3. MCA DOPPLER
    doc.add_heading('3. MIDDLE CEREBRAL ARTERY (MCA) DOPPLER', 1)
    doc.add_heading('3.1. Ky thuat do', 2)
    add_bullets(doc, [
        'Mat cat: Ngang qua thai (transverse section) o muc xuong dinh (ban song song voi duong giua).',
        'Xac dinh: Da giac Willis -> MCA gan nhat voi dau do (thuong la MCA gan).',
        'Sample volume: Dat o 1/3 gan cua MCA (gan nguon goc tu da giac Willis), TRANH dat qua xa (se gan vi tri phan nhanh thanh nhieu nhanh nho).',
        'Goc insonation: < 30 do (tot nhat 0 do).',
    ])

    doc.add_heading('3.2. Hai chi so quan trong', 2)
    doc.add_paragraph('a) MCA-PSV (dung cho anemia)').runs[0].bold = True
    add_bullets(doc, [
        'Nguong chinh: MCA-PSV >= 1.5 MoM = nghi ngo anemia trung binh-nang.',
        'Don vi: cm/s, so sanh voi bang MoM theo tuoi thai (Mari 1995, hien van dung).',
        'Theo Martinez-Portilla 2019 (PMID 30932276), meta-analysis 12 nghien cuu, 696 thai:',
        '   - AUC 0.83 cho anemia trung binh-nang.',
        '   - Pooled sensitivity 79% (95% CI 70-86), specificity 73% (95% CI 62-82).',
        '   - Voi thai CHUA truyen mau: AUC 0.87, sens 86% (95% CI 75-93), spec 71% (95% CI 49-87).',
        '   - Sai so tang theo so lan truyen mau trong tu cung (do nhay giam 5.5% moi lan, P=0.039).',
        '   - Vai tro tot nhat o thai CHUA duoc truyen mau lan nao.',
    ])

    doc.add_paragraph('b) MCA-PI (dung cho "brain-sparing")').runs[0].bold = True
    add_bullets(doc, [
        'Trong thai ky binh thuong: MCA-PI GIAM dan theo tuoi thai (nao phat trien, nhu cau mau tang).',
        'Trong FGR: MCA-PI giam them so voi binh thuong -> "brain-sparing effect".',
        'Y nghia: Co the thai uu tien mau cho nao, hy sinh cac co quan khac.',
    ])

    doc.add_heading('3.3. Ung dung lam sang', 2)
    doc.add_paragraph('Anemia thai (chi dinh MCA-PSV theo [ISUOG 2021 - Doppler] PMID 34278615):')
    add_bullets(doc, [
        'Alloimmune hemolytic disease (Rh isoimmunization).',
        'Parvovirus B19 infection.',
        'Twin-to-twin transfusion syndrome (TTTS) - thai cho mau.',
        'Chay mau thai-me (FMH).',
        'Thalassemia, sickle cell.',
    ])
    doc.add_paragraph('Hypoxemia thai:')
    add_bullets(doc, [
        'Ket hop voi UA Doppler + CPR (xem phan 4).',
        'Luu y: SMFM 2020 (PMID 32407785) khuyen cao KHONG dung MCA Doppler thuong quy de quan ly FGR (GRADE 2B), nhung co gia tri gia tang giam sat o thai co dau hieu nguy co.',
    ])

    # 4. CPR
    doc.add_heading('4. CEREBROPLACENTAL RATIO (CPR) - CHI SO "BRAIN-SPARING"', 1)
    doc.add_heading('4.1. Dinh nghia va cach tinh', 2)
    doc.add_paragraph(
        'CPR = MCA-PI / UA-PI\n'
        '(hoac dao nguoc UCR = UA-PI/MCA-PI; hai chi so cung y nghia, chi khac chieu so sanh)\n\n'
        '- CPR binh thuong: >= p5 (hoac > 1.08 theo mot so nghien cuu).\n'
        '- CPR thap: < p5 = canh bao "brain-sparing" -> thai dang phan phoi lai tuan hoan uu tien nao.'
    )

    doc.add_heading('4.2. Vai tro trong tien doan bien chung', 2)
    doc.add_paragraph('Conde-Agudelo 2018 (PMID 29920817) - meta-analysis lon nhat ve CPR trong suspected FGR:').runs[0].bold = True
    add_bullets(doc, [
        '22 nghien cuu, 4,301 phu nu.',
        'Ket qua:',
        '   - Perinatal death: sensitivity 93% (cao nhat), specificity 76%, summary LR+ 3.9, LR- 0.09.',
        '   - SGA at birth: LR+ 7.4 (trung binh cao).',
        '   - Composite adverse outcome, Apgar < 7, NICU admission: LR+ thap (1.1-2.5).',
        'CPR co gia tri nhat cho perinatal death va cho early-onset FGR.',
    ])

    doc.add_paragraph('Quan trong - Vollgraff Heidweiller-Schreurs 2021 (PMID 32363701) - Individual Patient Data (IPD) meta-analysis lon hon:').runs[0].bold = True
    add_bullets(doc, [
        '10 trung tam, 17 dataset, 18,731 participants.',
        'So sanh: UA-PI alone vs CPR alone vs UA-PI + CPR.',
        'Ket qua:',
        '   - UA-PI alone: AUC 0.775 (95% CI 0.709-0.828).',
        '   - CPR alone: AUC 0.778 (95% CI 0.715-0.831).',
        '   - UA-PI + CPR: AUC 0.778 (95% CI 0.714-0.831) - chi tang 0.003 diem.',
        '- Ket luan: CPR them KHONG cai thien du bao so voi UA-PI alone, khi phan tich IPD lon.',
        '- Tweetable abstract: "CPR in clinical practice has limited added predictive value to umbilical artery alone".',
    ])

    doc.add_heading('4.3. Luu y thuc hanh (hoa giai hai meta-analysis)', 2)
    doc.add_paragraph(
        'Su khac biet giua Conde-Agudelo 2018 va Vollgraff 2021 co the giai thich:\n'
        '- Conde-Agudelo aggregate studies -> CPR co them gia tri.\n'
        '- Vollgraff IPD (kiem soat confounders tot hon) -> CPR them it gia tri.\n'
        '- Trong clinical practice: UA-PI van la chi so chinh, CPR ho tro nhung khong thay the.'
    )
    doc.add_paragraph('Kahramanoglu 2022 (PMID 34569419) - retrospective 407 thai late-onset FGR:')
    add_bullets(doc, [
        'CPR < p5 = yeu to du bao doc lap cho adverse perinatal outcome (sau khi dieu chinh birth weight, oligohydramnios).',
        'Late-onset FGR van co gia tri dung CPR.',
    ])

    # 5. DV
    doc.add_heading('5. DUCTUS VENOSUS (DV) DOPPLER - DAU HIEU TIM MACH QUAN TRONG', 1)
    doc.add_heading('5.1. Co che sinh ly', 2)
    doc.add_paragraph('DV la mach mau noi tinh mach ron voi tinh mach chau duoi, LAI DONG MAU GIAU OXY di thang tu nhau -> tim -> nao (qua foramen ovale), bypass gan.')
    doc.add_paragraph('Song binh thuong DV gom 3 pha (goi la pho 3 dinh):')
    add_bullets(doc, [
        'S (systolic peak): dinh tam thu.',
        'D (diastolic peak): dinh tam truong.',
        'A (atrial contraction): song tien tam thu (a-wave) - phan NHAY CAM NHAT voi toan/tim suy.',
    ])

    doc.add_heading('5.2. Bat thuong DV va y nghia', 2)
    t4 = doc.add_table(rows=5, cols=3)
    fill_table(t4,
        ['Song DV', 'Y nghia', 'Giai doan suy thai'],
        [
            ('Binh thuong (a-wave duong)', 'Tim thai bu tru tot', 'Binh thuong'),
            ('A-wave giam', 'Bat dau mat bu', 'Suy thai trung binh'),
            ('Absent A-wave (a = 0)', 'Suy thai ro, co the toan', 'Suy thai nang'),
            ('Reversed A-wave (a < 0)', 'Suy thai rat nang, nguy co tu vong 1-7 ngay', 'CUC NANG'),
        ])
    doc.add_paragraph()

    doc.add_heading('5.3. Vai tro trong early-onset FGR - Bang chung TRUFFLE', 2)
    doc.add_paragraph('TRUFFLE trial (Lees 2013 PMID 24078432, Frusca 2018 PMID 29422211):').runs[0].bold = True
    add_bullets(doc, [
        'European multicenter RCT, 503 phu nu, FGR som 26-32 tuan.',
        'So sanh 3 chien luoc can thiep:',
        '   - cCTG alone (computerized cardiotocography).',
        '   - cCTG + early DV (can thiep khi a-wave absent).',
        '   - cCTG + late DV (can thiep khi a-wave reversed, muon hon).',
        '- Ket qua (Frusca 2018):',
        '   - Tong: 92% (463/503) song sot, 1% (6/443) bai nao.',
        '   - Trong so song sot: 95% (133/144) nhom late DV co outcome than kinh binh thuong vs 85% (111/131) nhom cCTG alone (P < 0.01).',
        '- Ket luan: cCTG + late DV changes = chien luoc toi uu cho early-onset FGR.',
    ])

    doc.add_paragraph('Ganzevoort 2020 (PMID 31125465) - phan tich ket hop GRIT + TRUFFLE:').runs[0].bold = True
    add_bullets(doc, [
        'Nhom cCTG + DV Doppler: 84% song sot khong ton thuong than kinh (95% CI 80-89%).',
        'Nhom immediate delivery: 70% (95% CI 61-78%).',
        'Nhom CTG alone: 69% (95% CI 57-82%).',
        'P < 0.01 cho trend -> cCTG + DV cho outcome tot nhat.',
    ])

    doc.add_paragraph('Lees 2022 Clinical Opinion (PMID 35026129) tong hop: "Trong early-onset FGR, ket hop cCTG + DV Doppler giup 95% tre song co outcome than kinh binh thuong o 2 tuoi."').runs[0].italic = True

    doc.add_heading('5.4. Vi tri DV Doppler trong cascade hien nay', 2)
    doc.add_paragraph('Theo Lees 2022 (PMID 35026129) va SMFM 2020 (PMID 32407785):')
    add_bullets(doc, [
        'UA Doppler: xet nghiem Doppler dau tay trong FGR.',
        'DV Doppler: them vao khi UA bat thuong o early-onset FGR.',
        'MCA/CPR: huu ich cho late-onset FGR va tang cuong giam sat.',
        'Chi quyet dinh can thiep dua tren DV: trong early-onset FGR, theo TRUFFLE.',
    ])

    # 6. EVIDENCE & GUIDELINES
    doc.add_heading('6. EVIDENCE & GUIDELINES', 1)
    doc.add_heading('6.1. [ISUOG 2021 - Doppler] Practice Guidelines (Bhide A. et al., PMID 34278615)', 2)
    doc.add_paragraph('Tieu chuan vang cho Doppler thai ky. Consensus cua 22 chuyen gia quoc te, update 2013 guideline.')
    doc.add_paragraph('Khuyen cao chinh:')
    add_bullets(doc, [
        'Umbilical artery Doppler: nen dung o thai nghy ngo FGR (good practice point).',
        'Middle cerebral artery: nen dung o thai FGR; dung MCA-PSV >= 1.5 MoM de sang loc anemia trung binh-nang (Grade A).',
        'Ductus venosus: dung o early-onset FGR voi UA bat thuong, dac biet < 32 tuan.',
        'Uterine artery: sang loc preeclampsia/FGR quy 1 (ket hop voi biomarkers).',
        'KHONG khuyen cao Doppler routine trong thai ky khong bien chung.',
    ])

    doc.add_heading('6.2. SMFM 2020 Consult Series #52 (PMID 32407785)', 2)
    doc.add_paragraph('Guideline My cho FGR, 21 GRADE recommendations (la guideline co nhieu recommendation cu the nhat hien nay).')
    doc.add_paragraph('Cac recommendation lien quan Doppler:')
    add_bullets(doc, [
        '(9) Doppler UA serial sau khi chan doan FGR (GRADE 1C).',
        '(10) Doppler 1 lan/tuan khi decreased diastolic flow (GRADE 2C).',
        '(11) Doppler 2-3 lan/tuan khi absent EDV (GRADE 1C).',
        '(12) Nhap vien + corticosteroid + monitoring 1-2 lan/ngay khi reversed EDV (GRADE 2C).',
        '(13) KHONG dung DV/MCA/UA Doppler cho quan ly thuong quy FGR som hoac muon (GRADE 2B).',
        '(15) Sinh o 37 tuan voi decreased diastolic flow (1B).',
        '(16) Sinh o 33-34 tuan voi absent EDV (1B).',
        '(17) Sinh o 30-32 tuan voi reversed EDV (1B).',
        '(18) Sinh o 38-39 tuan voi EFW p3-p10 va UA binh thuong (2C).',
    ])

    doc.add_heading('6.3. Lees 2022 Clinical Opinion (PMID 35026129)', 2)
    doc.add_paragraph(
        'Bai tong quan consensus lon nhat 2022, ky boi 27 chuyen gia quoc te. Tom gon evidence moi nhat:\n'
        '"Trong early-onset FGR, ket hop computerized CTG + DV Doppler cho ket qua than kinh 2 nam tot nhat. CPR co the tang giam sat o late-onset FGR, nhung khong nen dung de quyet dinh thoi diem can thiep."'
    )
    doc.add_paragraph('Lees 2022 phan loai FGR som/muon:').runs[0].bold = True
    add_bullets(doc, [
        'Early-onset FGR: < 32 tuan, thuong co UA-PI bat thuong.',
        'Late-onset FGR: >= 32 tuan, thuong chi co MCA-PI/CPR bat thuong, UA binh thuong.',
    ])

    doc.add_heading('6.4. Ochoa 2025 (PMID 40187275)', 2)
    doc.add_paragraph(
        'Bai review moi nhat (BPRCOG 2025) - Doppler van la cong cu thiet yeu cho fetal monitoring. Tuong lai:\n'
        '- AI/ML tich hop Doppler.\n'
        '- Doppler ket hop biomarker (PlGF, sFlt-1).\n'
        '- Ca nhan hoa nguong theo chung toc, BMI me.'
    )

    # 7. TONG HOP UNG DUNG
    doc.add_heading('7. TONG HOP UNG DUNG LAM SANG', 1)
    doc.add_heading('7.1. Bang tong hop khi nao dung Doppler nao', 2)
    t5 = doc.add_table(rows=8, cols=4)
    fill_table(t5,
        ['Tinh huong lam sang', 'Doppler dau tay', 'Doppler thu hai', 'Ghi chu'],
        [
            ('Nghi ngo FGR (EFW < p10)', 'UA serial', 'MCA, CPR', 'UA la chuan vang'),
            ('FGR som (< 32 tuan)', 'UA', 'DV', 'DV giup timing can thiep'),
            ('FGR muon (>= 32 tuan)', 'UA', 'MCA, CPR', 'Brain-sparing marker'),
            ('Thai anemia (Rh, parvovirus, FMH)', 'MCA-PSV', 'UA', 'PSV >= 1.5 MoM = anemia nghi ngo'),
            ('Preeclampsia (screening quy 1)', 'Uterine artery', 'Ket hop PAPP-A, PlGF', 'ASPRE trial: aspirin 150 mg'),
            ('Twin pregnancy', 'UA ca 2 thai', 'MCA ca 2, DV cho TTTS', 'MCA-PSV tang o thai cho mau'),
            ('MCA-PSV bat thuong', 'cordocentesis', 'Lap lai Doppler 1-2 tuan/lan', 'Sai so tang theo so lan truyen mau'),
        ])
    doc.add_paragraph()

    doc.add_heading('7.2. Algorithm Doppler trong FGR som (early-onset, < 32 tuan)', 2)
    doc.add_paragraph(
        'Thai <32 tuan + EFW <p10\n'
        '   V\n'
        'UA Doppler\n'
        '   V\n'
        '+----------------------------------+\n'
        '| Binh thuong (PI < p95)           | -> MCA-PI, CPR danh gia them\n'
        '|                                  |   Tiep tuc theo doi 1-2 lan/tuan\n'
        '+----------------------------------+\n'
        '   V\n'
        '+----------------------------------+\n'
        '| UA bat thuong                    |\n'
        '| (PI >= p95, AEDV, REDV)         |\n'
        '+----------------------------------+\n'
        '   V\n'
        'DV Doppler + cCTG\n'
        '   V\n'
        '+----------------------------------+\n'
        '| a-wave binh thuong               | -> Corticosteroid, theo doi sat\n'
        '+----------------------------------+\n'
        '   V\n'
        '+----------------------------------+\n'
        '| a-wave absent                    | -> Can nhac can thiep tuy tuoi thai\n'
        '+----------------------------------+\n'
        '   V\n'
        '+----------------------------------+\n'
        '| a-wave reversed                  | -> Can thiep NANG (theo TRUFFLE)\n'
        '+----------------------------------+\n'
        '   V\n'
        'Quyet dinh: cCTG + late DV (theo Frusca 2018 - 95% normal outcome)'
    )

    doc.add_heading('7.3. Cac loi thuong gap', 2)
    add_bullets(doc, [
        'Dat sample volume sai vi tri tren MCA: gan phan nhanh -> PSV giam gia -> am tinh gia anemia.',
        'Do UA gan bam ron: PI thap hon thuc (it suc can) -> am tinh gia FGR.',
        'Goc insonation > 30 do: sai so tang theo cos theta.',
        'Dung Doppler trong thai ky binh thuong: ton thoi gian, gay lo lang khong can thiet.',
        'Bo qua bien thien sinh ly: UA-PI co the tang nhe thoang qua -> khong ket luan ngay.',
        'Quen ghi ro gestational age: bang MoM/percentile theo tuoi thai.',
    ])

    # 8. TIPS
    doc.add_heading('8. TIPS THUC HANH (CLINICAL PEARLS)', 1)
    add_bullets(doc, [
        'Bat dau voi UA khi nghi ngo FGR - KHONG nhay thang sang MCA/DV.',
        'MCA-PSV >= 1.5 MoM = nguong anemia thai theo Mari 1995 (van dung den nay). Tot nhat o thai CHUA truyen mau.',
        'Late-onset FGR (~70% ca FGR): UA-PI thuong BINH THUONG -> can CPR + MCA-PI de phat hien.',
        'Absent EDV o tuan 30-34: chuan bi corticosteroid + can thiep trong vong 1-2 tuan.',
        'Reversed EDV: can thiep KHAN - corticosteroid + monitor sat.',
        'DV a-wave absent/reversed o FGR som = can nhac can thiep (theo TRUFFLE).',
        'Dung dung CPR mot minh de quyet dinh can thiep - Vollgraff 2021 cho thay them rat it gia tri so voi UA-PI alone.',
        'Uterine artery + PlGF quy 1 = sang loc tot nhat cho preeclampsia (ASPRE trial).',
        'MCA-PSV KHONG dung sau nhieu lan truyen mau: sai so tang.',
        'Cascade Doppler: UA binh thuong -> theo doi. UA bat thuong -> them DV (early FGR) hoac MCA/CPR (late FGR).',
    ])

    # 9. TONG KET
    doc.add_heading('9. TONG KET DIEM CAN NHO', 1)
    add_numbered(doc, [
        'Ba mach mau cot loi: UA (nhau), MCA (nao), DV (tim). Moi mach cung cap thong tin khac nhau.',
        'UA Doppler: tieu chuan vang cho FGR. Absent EDV = sinh 33-34 tuan; Reversed EDV = sinh 30-32 tuan (theo SMFM 2020 PMID 32407785).',
        'MCA-PSV >= 1.5 MoM: nguong anemia thai. Sens 79%, spec 73% theo meta-analysis 12 nghien cuu, 696 thai (Martinez-Portilla 2019 PMID 30932276).',
        'CPR (MCA-PI/UA-PI): giam trong FGR = "brain-sparing". Theo Vollgraff 2021 (PMID 32363701) IPD meta-analysis 18,731 phu nu, CPR them KHONG cai thien gia tri du bao so voi UA-PI alone (AUC 0.775 vs 0.778).',
        'DV Doppler trong early-onset FGR: late DV a-wave reversed = chien luoc toi uu theo TRUFFLE - 95% tre song co outcome than kinh binh thuong o 2 tuoi (Frusca 2018 PMID 29422211).',
        'Ganzevoort 2020 (PMID 31125465): cCTG + DV Doppler cho 84% song sot khong ton thuong (95% CI 80-89) vs 70% o nhom can thiep som.',
        '[ISUOG 2021 - Doppler] (Bhide A. et al. PMID 34278615): guideline chinh cho Doppler thai ky. KHONG dung routine.',
        'SMFM 2020 (PMID 32407785): 21 GRADE recommendations - guideline quyet dinh timing can thiep cu the nhat.',
        'Uterine artery quy 1 ket hop PAPP-A, PlGF = sang loc tot nhat preeclampsia. Aspirin 150 mg/dem tu 11-14 tuan giam 62% preterm preeclampsia (ASPRE).',
        'Algorithm: UA binh thuong -> theo doi. UA bat thuong + < 32 tuan -> DV. UA bat thuong + >= 32 tuan -> MCA/CPR.',
    ])

    # 10. TAI LIEU
    doc.add_heading('10. TAI LIEU THAM KHAO (VERIFY PUBMED)', 1)
    refs = [
        ('Bhide A. et al. (2021)', 'PMID: 34278615', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.23698', '"ISUOG Practice Guidelines (updated): use of Doppler velocimetry in obstetrics."'),
        ('Martins JG, Biggio JR, Abuhamad A. (SMFM, 2020)', 'PMID: 32407785', 'Am J Obstet Gynecol.', 'DOI: 10.1016/j.ajog.2020.05.010', '"Society for Maternal-Fetal Medicine Consult Series #52: Diagnosis and management of fetal growth restriction."'),
        ('Lees CC, Romero R, Stampalija T. et al. (2022)', 'PMID: 35026129', 'Am J Obstet Gynecol.', 'DOI: 10.1016/j.ajog.2021.11.1357', '"Clinical Opinion: The diagnosis and management of suspected fetal growth restriction: an evidence-based approach."'),
        ('Conde-Agudelo A, Villar J, Kennedy SH, Papageorghiou AT. (2018)', 'PMID: 29920817', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.19117', '"Predictive accuracy of cerebroplacental ratio for adverse perinatal and neurodevelopmental outcomes in suspected fetal growth restriction: systematic review and meta-analysis."'),
        ('Vollgraff Heidweiller-Schreurs CA et al. (CPR IPD Study Group, 2021)', 'PMID: 32363701', 'BJOG.', 'DOI: 10.1111/1471-0528.16287', '"Cerebroplacental ratio in predicting adverse perinatal outcome: a meta-analysis of individual participant data."'),
        ('Ganzevoort W, Thornton JG, Marlow N. et al. (2020)', 'PMID: 31125465', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.20354', '"Comparative analysis of 2-year outcomes in GRIT and TRUFFLE trials."'),
        ('Martinez-Portilla RJ et al. (2019)', 'PMID: 30932276', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.20273', '"Performance of fetal middle cerebral artery peak systolic velocity for prediction of anemia in untransfused and transfused fetuses: systematic review and meta-analysis."'),
        ('Frusca T, Todros T, Lees C, Bilardo CM. (TRUFFLE, 2018)', 'PMID: 29422211', 'Am J Obstet Gynecol.', 'DOI: 10.1016/j.ajog.2017.12.226', '"Outcome in early-onset fetal growth restriction is best combining computerized fetal heart rate analysis with ductus venosus Doppler."'),
        ('Ochoa JH, Cafici D. (2025)', 'PMID: 40187275', 'Best Pract Res Clin Obstet Gynaecol.', 'DOI: 10.1016/j.bpobgyn.2025.102594', '"Fetal Doppler assessment in pregnancy."'),
        ('Kahramanoglu O et al. (2022)', 'PMID: 34569419', 'J Obstet Gynaecol.', 'DOI: 10.1080/01443615.2021.1954148', '"Cerebroplacental doppler ratio and perinatal outcome in late-onset foetal growth restriction."'),
        ('Lees C, Marlow N, Arabin B. et al. (TRUFFLE, 2013)', 'PMID: 24078432', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.13190', '"Perinatal morbidity and mortality in early-onset fetal growth restriction: cohort outcomes of the trial of randomized umbilical and fetal flow in Europe (TRUFFLE)."'),
        ('Cao L et al. (2024)', 'PMID: 38805623', 'Med Ultrason.', 'DOI: 10.11152/mu-4355', '"Utility of uterine artery Doppler ultrasound imaging in predicting preeclampsia during pregnancy: a meta-analysis."'),
        ('Rolnik DL et al. (ASPRE trial, 2017)', 'PMID: 28741785', 'Ultrasound Obstet Gynecol.', 'DOI: 10.1002/uog.18816', '"ASPRE trial: performance of screening for preterm pre-eclampsia."'),
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
        model_id=1607392320,
        model_name='Fetal Doppler thai ky - Pastel',
        deck_id=2059400111,
        deck_name='Fetal Doppler thai ky - 19/06/2026',
        deck_description='Fetal Doppler Ultrasound trong san khoa - 19/06/2026 - Pastel theme'
    )
    n = add_cards_from_json(deck, model, CARDS_JSON, 'Fetal US · Doppler · FGR')
    write_apkg(deck, APKG_OUT)
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {n}")


# ============================================================
# HTML VISUAL SUMMARY (uses shared template)
# Chart #1: ZOOMED IN 0.770-0.780 để thấy delta 0.003 giữa các AUC
# ============================================================
def build_html():
    # Header
    header_html = '''
<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">Fetal Doppler Ultrasound trong San khoa</h1>
  <p class="text-stone-500 italic">Visual Summary - Bai hoc 19/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">Fetal US</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">Doppler</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">FGR</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">Anemia thai</span>
    <span class="tag pastel-lavender px-3 py-1 rounded-full text-sm">Preeclampsia</span>
  </div>
</header>
'''

    # Main sections
    main_html = '''

  <!-- SECTION 1: 3 MACH MAU COT LOI -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. Ba mach mau cot loi trong Doppler thai ky</h2>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Umbilical Artery (UA)</h3>
        <p class="text-sm text-stone-700">Phan anh <b>suc can tuan hoan nhau-nhau</b> (uteroplacental + fetoplacental). Tieu chuan vang cho FGR.</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Middle Cerebral Artery (MCA)</h3>
        <p class="text-sm text-stone-700">Phan anh <b>su phan phoi mau len nao</b> ("brain-sparing effect"). MCA-PSV &gt;= 1.5 MoM = anemia thai.</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Ductus Venosus (DV)</h3>
        <p class="text-sm text-stone-700">Phan anh <b>chuc nang tim thai va tinh trang toan</b>. a-wave reversed = can thiep nang.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 2: ALGORITHM -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Algorithm Doppler trong FGR som (&lt;32 tuan)</h2>
    <div class="mermaid">
flowchart TD
    A["Thai &lt;32 tuan + EFW &lt;p10"] --&gt; B["UA Doppler"]
    B --&gt; C{"Ket qua UA?"}
    C -- "Binh thuong<br/>(PI &lt; p95)" --&gt; D["MCA-PI, CPR<br/>danh gia them"]
    D --&gt; E["Theo doi 1-2 lan/tuan"]
    C -- "Bat thuong<br/>(PI &gt;= p95, AEDV, REDV)" --&gt; F["DV Doppler + cCTG"]
    F --&gt; G{"a-wave DV?"}
    G -- "Binh thuong" --&gt; H["Corticosteroid<br/>Theo doi sat"]
    G -- "Absent" --&gt; I["Can nhac can thiep<br/>tuy tuoi thai"]
    G -- "Reversed" --&gt; J["Can thiep NANG<br/>(theo TRUFFLE)"]
    J --&gt; K["Quyet dinh: cCTG + late DV<br/>(Frusca 2018 - 95% normal)"]

    style A fill:#f4c2c2
    style B fill:#c5d5e0
    style F fill:#c5e0c9
    style J fill:#d4c5e2
    style K fill:#f7d1ba
    </div>
  </section>

  <!-- SECTION 3: BA CHI SO DOPPLER -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">3. Ba chi so Doppler co ban</h2>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">PI (Pulsatility Index) - Gosling</h3>
        <p class="text-sm text-stone-700 font-mono bg-stone-100 p-2 rounded">PI = (PSV - EDV) / TAV</p>
        <p class="text-sm text-stone-600 mt-2">Pho bien nhat. PI tang = suc can tang. PI giam = suc can giam.</p>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">RI (Resistance Index) - Pourcelot</h3>
        <p class="text-sm text-stone-700 font-mono bg-stone-100 p-2 rounded">RI = (PSV - EDV) / PSV</p>
        <p class="text-sm text-stone-600 mt-2">It dung hon PI, thuong dung cho Doppler than.</p>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">PSV (Peak Systolic Velocity)</h3>
        <p class="text-sm text-stone-700 font-mono bg-stone-100 p-2 rounded">PSV (cm/s)</p>
        <p class="text-sm text-stone-600 mt-2">Dung cho MCA-PSV (anemia). Nguong: &gt;= 1.5 MoM = nghi anemia.</p>
      </div>
    </div>
  </section>

  <!-- SECTION 4: BANG UA DOPPLER -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">4. Phan tang UA Doppler trong FGR</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">UA Doppler</th>
            <th class="px-3 py-2 text-left">Y nghia</th>
            <th class="px-3 py-2 text-left">Thoi diem sinh (SMFM 2020)</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Binh thuong</td><td class="px-3 py-2">Nhau tot</td><td class="px-3 py-2">38-39 tuan (neu FGR + EFW p3-p10)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">PI tang</td><td class="px-3 py-2">Suy nhau bat dau</td><td class="px-3 py-2">37 tuan (GRADE 1B)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">EDV giam</td><td class="px-3 py-2">Suy nhau ro</td><td class="px-3 py-2">37 tuan (GRADE 1B)</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">Absent EDV</td><td class="px-3 py-2">Suy nhau nang</td><td class="px-3 py-2">33-34 tuan (GRADE 1B)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Reversed EDV</td><td class="px-3 py-2">Suy nhau rat nang</td><td class="px-3 py-2">30-32 tuan (GRADE 1B)</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 5: EVIDENCE -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">5. Evidence - Meta-analysis &amp; Trials quan trong</h2>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">PMID</th>
            <th class="px-3 py-2 text-left">Tac gia (Nam)</th>
            <th class="px-3 py-2 text-left">Loai nghien cuu</th>
            <th class="px-3 py-2 text-left">Ket qua chinh</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">34278615</td><td class="px-3 py-2">Bhide A. (2021)</td><td class="px-3 py-2">ISUOG Practice Guideline</td><td class="px-3 py-2">Doppler khong routine; chi dinh cu the</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">32407785</td><td class="px-3 py-2">SMFM (2020)</td><td class="px-3 py-2">Consult Series 21 GRADE recs</td><td class="px-3 py-2">Timing sinh theo UA Doppler</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">35026129</td><td class="px-3 py-2">Lees CC (2022)</td><td class="px-3 py-2">Clinical Opinion 27 chuyen gia</td><td class="px-3 py-2">cCTG + DV cho FGR som; CPR cho FGR muon</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">29920817</td><td class="px-3 py-2">Conde-Agudelo (2018)</td><td class="px-3 py-2">Meta-analysis 22 studies, n=4301</td><td class="px-3 py-2">CPR sens 93% cho perinatal death</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">32363701</td><td class="px-3 py-2">Vollgraff (2021)</td><td class="px-3 py-2">IPD meta-analysis 18,731 PN</td><td class="px-3 py-2">CPR them KHONG cai thien du bao</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">31125465</td><td class="px-3 py-2">Ganzevoort (2020)</td><td class="px-3 py-2">GRIT + TRUFFLE IPD 741 PN</td><td class="px-3 py-2">cCTG+DV: 84% song sot khong ton thuong</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">30932276</td><td class="px-3 py-2">Martinez-Portilla (2019)</td><td class="px-3 py-2">Meta-analysis 12 studies, 696 thai</td><td class="px-3 py-2">MCA-PSV AUC 0.83 cho anemia</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">29422211</td><td class="px-3 py-2">Frusca (2018)</td><td class="px-3 py-2">TRUFFLE RCT 503 PN</td><td class="px-3 py-2">Late DV: 95% normal outcome 2 tuoi</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- SECTION 6: CHART 1 - CPR AUC comparison - ZOOM IN -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">6. CPR khong them gia tri du bao (Vollgraff 2021)</h2>
    <p class="text-sm text-stone-600 italic mb-4">Zoom vao scale AUC 0.770-0.780 de thay ro delta 0.003 - khong co y nghia lam sang.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">IPD Meta-analysis 18,731 phu nu</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>UA-PI alone:</b> AUC 0.775</li>
          <li>• <b>CPR alone:</b> AUC 0.778</li>
          <li>• <b>UA-PI + CPR:</b> AUC 0.778 (chi tang 0.003)</li>
          <li>• <b>Ket luan:</b> CPR them khong cai thien du bao</li>
          <li>• Tweetable: "CPR has limited added predictive value to UA alone"</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 7: CHART 2 - TRUFFLE outcomes -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. TRUFFLE + GRIT - Song sot khong ton thuong than kinh 2 tuoi</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart2"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Ganzevoort 2020 (PMID 31125465)</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• Phan tich ket hop GRIT + TRUFFLE</li>
          <li>• Early-onset FGR 26-32 tuan</li>
          <li>• cCTG + DV cho outcome tot nhat</li>
          <li>• P &lt; 0.01 cho trend</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SECTION 8: DV DOPPLER -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. Ductus Venosus - Song 3 dinh &amp; bat thuong</h2>
    <div class="mermaid">
flowchart LR
    A["Binh thuong<br/>a-wave DUONG<br/>Tim bu tru tot"] --&gt; B["A-wave GIAM<br/>Bat dau mat bu<br/>Suy thai trung binh"]
    B --&gt; C["Absent A-wave<br/>Suy thai ro<br/>Co the toan"]
    C --&gt; D["Reversed A-wave<br/>Suy thai CUC NANG<br/>Nguy co tu vong 1-7 ngay"]

    style A fill:#c5e0c9
    style B fill:#f7d1ba
    style C fill:#f4c2c2
    style D fill:#d4c5e2
    </div>
    <p class="text-sm text-stone-600 mt-3 italic">DV: mach noi tinh mach ron voi tinh mach chau duoi, lai dong giau oxy tu nhau -&gt; tim -&gt; nao. Song a-wave (tien tam thu) nhay cam nhat voi toan/tim suy.</p>
  </section>

  <!-- SECTION 9: KHI NAO DUNG DOPPLER NAO -->
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">9. Khi nao dung Doppler nao?</h2>
    <div class="grid md:grid-cols-2 gap-3">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Nghi ngo FGR (EFW &lt; p10)</h3>
        <p class="text-sm text-stone-700">UA serial -&gt; MCA, CPR</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">FGR som (&lt; 32 tuan)</h3>
        <p class="text-sm text-stone-700">UA -&gt; DV (giup timing can thiep)</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">FGR muon (&gt;= 32 tuan)</h3>
        <p class="text-sm text-stone-700">UA -&gt; MCA, CPR (brain-sparing)</p>
      </div>
      <div class="pastel-peach rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Thai anemia</h3>
        <p class="text-sm text-stone-700">MCA-PSV (&gt;= 1.5 MoM = nghi anemia)</p>
      </div>
      <div class="pastel-lavender rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Preeclampsia screening</h3>
        <p class="text-sm text-stone-700">Uterine artery quy 1 + PAPP-A, PlGF</p>
      </div>
      <div class="bg-stone-200 rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2">Twin pregnancy</h3>
        <p class="text-sm text-stone-700">UA ca 2 + MCA ca 2 + DV cho TTTS</p>
      </div>
    </div>
  </section>
'''

    # Custom Chart.js scripts - CHART 1 ZOOMED IN to highlight the 0.003 delta
    custom_charts = '''
// Chart 1: CPR AUC comparison - ZOOMED IN to highlight 0.003 delta
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['UA-PI alone', 'CPR alone', 'UA-PI + CPR'],
        datasets: [{
            label: 'AUC',
            data: [0.775, 0.778, 0.778],
            backgroundColor: [
                'rgba(197, 213, 224, 0.85)',
                'rgba(244, 194, 194, 0.85)',
                'rgba(212, 197, 226, 0.85)'
            ],
            borderColor: [
                'rgba(197, 213, 224, 1)',
                'rgba(244, 194, 194, 1)',
                'rgba(212, 197, 226, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Vollgraff 2021 - AUC zoom 0.770-0.780' },
            legend: { display: false },
            tooltip: {
                callbacks: {
                    afterLabel: function(ctx) {
                        const vals = [0.775, 0.778, 0.778];
                        const delta = (vals[ctx.dataIndex] - vals[0]).toFixed(3);
                        return delta === '0.000' ? 'Baseline (UA-PI alone)' : 'Delta vs UA-PI: +' + delta;
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: false,
                min: 0.770,
                max: 0.780,
                ticks: { stepSize: 0.002 },
                title: { display: true, text: 'AUC (zoomed)' }
            }
        }
    }
});

// Chart 2: TRUFFLE+GRIT survival without impairment
new Chart(document.getElementById('chart2'), {
    type: 'bar',
    data: {
        labels: ['Immediate delivery', 'CTG alone', 'cCTG only', 'cCTG + DV Doppler'],
        datasets: [{
            label: '% Song sot khong ton thuong than kinh (2 tuoi)',
            data: [70, 69, 77, 84],
            backgroundColor: [
                'rgba(244, 194, 194, 0.7)',
                'rgba(247, 209, 186, 0.7)',
                'rgba(197, 213, 224, 0.7)',
                'rgba(197, 224, 201, 0.7)'
            ],
            borderColor: [
                'rgba(244, 194, 194, 1)',
                'rgba(247, 209, 186, 1)',
                'rgba(197, 213, 224, 1)',
                'rgba(197, 224, 201, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        plugins: {
            title: { display: true, text: 'Ganzevoort 2020 - GRIT + TRUFFLE 2-year outcomes' },
            legend: { display: false }
        },
        scales: { x: { beginAtZero: 50, max: 100 } }
    }
});
'''

    # Footer text
    footer_text = 'Bai hoc soan boi MiniMax Mavis cho Bs. Ngoc 🍅 🐈‍⬛ | Verified PubMed: 13 papers (PMID 34278615, 32407785, 35026129, 29920817, 32363701, 31125465, 30932276, 29422211, 40187275, 34569419, 24078432, 38805623, 28741785)'

    html_content = build_lesson_html(
        title='Fetal Doppler thai ky - Visual Summary',
        header_html=header_html,
        main_html=main_html,
        footer_text=footer_text,
        custom_charts=custom_charts,
    )
    write_html(html_content, HTML_OUT)
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building Fetal Doppler Lesson - {DATE} (refactored) ===\n")
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
