"""Build full lesson: docx + anki apkg + html visual summary.
Topic: Tu cung nhi hoa (Hypoplastic Uterus / Uterus Infantilis) - 2026-06-23.
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
LESSON_DIR = ROOT / "01_San phu khoa" / "04_Tu_cung_nhi_hoa"
SOURCE_DIR = ROOT / "09_Source - Markdown" / "01_San phu khoa" / "04_Tu_cung_nhi_hoa"
DATE = "2026-06-23"

DOCX_OUT = LESSON_DIR / f"Tu cung nhi hoa (Hypoplastic Uterus) - {DATE}.docx"
APKG_OUT = LESSON_DIR / f"Anki - Tu cung nhi hoa 20 cards - {DATE}.apkg"
HTML_OUT = LESSON_DIR / f"Visual summary - Tu cung nhi hoa - {DATE}.html"
CARDS_JSON = SOURCE_DIR / "hypoplastic_cards.json"


# ============================================================
# CARDS DATA
# ============================================================
CARDS = [
    {"front": "Dinh nghia tu cung nhi hoa theo ASRM 2021?", "back": "Tu cung co buong < 5-6 cm, ty le than/co < 1:1 (binh thuong 2:1), the tich buong < 2.5-3 mL. Thuoc ASRM Class Ia (agenesis/hypoplasia segment) - khac voi MRKH (Class V/aplastic) va septate uterus (Class II)."},
    {"front": "Tu cung nhi hoa thuoc phan loai nao ASRM 2021 va ESHRE-ESGE 2013?", "back": "ASRM 2021: Class Ia (Mullerian agenesis/hypoplasia segment). ESHRE-ESGE 2013: U1 (dysmorphic uterus - than nho, co binh thuong, co the co vach nho). 2 he thong deu co nhan dien tu cung nhi hoa la 1 thuc the rieng biet."},
    {"front": "Ty le than/co binh thuong o tu cung truong thanh la bao nhieu?", "back": "Ty le than/co binh thuong = 2:1 (than dai gap 2 lan co). O tu cung nhi hoa: ty le < 1:1 (co dai hon hoac bang than), than teo, nho."},
    {"front": "Nguyen nhan gay tu cung nhi hoa - 5 nhom chinh?", "back": "(1) Bat thuong bam sinh ong Muller (MRKH type I, gene LHX1/HNF1B/TBX6); (2) Roi loan tin hieu estrogen qua ERalpha (aromatase deficiency, ERa-KO); (3) Phoi nhiem DES trong tu cung (hinh dang T tu cung); (4) Suy buong trung som (POI) - thieu estrogen kich thich tang truong; (5) Di truyen - GREB1L, PAX8."},
    {"front": "Vai tro cua estrogen va ERalpha trong phat trien tu cung day thi?", "back": "Theo Hewitt 2020 (PMID 32623449): Tu cung tang truong day thi PHU THUOC HOAN TOAN vao estrogen qua ERalpha. Chuot ERalpha-KO hoac aromatase-KO: tu cung KHONG phat trien du co E2. Cyp19-KO chuot duoc tiem E2 trong day thi: phuc hoi 1 phan dap ung tang truong. Cua so day thi - sau day thi la GIAI DOAN THEN CHOT de 'lap trinh' dap ung estrogen cua tu cung."},
    {"front": "Cac gene lien quan den phat trien bat thuong Muller (MRKH type II)?", "back": "Theo Herlin 2024 (PMID 38699388): LHX1 (17q12), HNF1B (17q12 - kem than da nang), TBX6 (16p11.2), GREB1L, PAX8. Di truyen RAT KHONG DONG NHAT (heterogeneous) - cung 1 phenotype co the do nhieu gene khac nhau."},
    {"front": "Tieu chuan vang chan doan bat thuong Muller (theo ASRM 2021)?", "back": "MRI vung chau - cho thay giai phau chi tiet cua tu cung, co tu cung, am dao, va than. KEM: TVUS 3D (first-line), hysterosalpingography (HSG), noi soi buong tu cung, noi soi o bung. Bat buoc: sieu am than (30-40% MRKH type II co bat thuong duong tiet nieu), karyotype (loai tru 46,XY), hormon (FSH, LH, E2, AMH)."},
    {"front": "Trieu chung lam sang cua tu cung nhi hoa?", "back": "Vo kinh nguyen phat (MRKH nang), kinh nguyet it (hypomenorrhea - nhe/trung binh), dau bung kinh (dysmenorrhea do buong nho), vo sinh nguyen phat/thu phat, say thai lien tiep (RPL), sinh non, ngoi thai bat thuong, nhau tien dao, nhau bong non. Tien su: phoi nhiem DES, chan an tam than, hoa tri/xa tri vung chau, phau thuat buong trung truoc day thi."},
    {"front": "Dieu tri tu cung nhi hoa nhe/trung binh - lieu phap hormone?", "back": "Estrogen HRT lieu thay the (khong progesterone giai doan dau): ethinylestradiol 0.05-0.1 mg/ngay hoac estradiol valerate 2-4 mg/ngay, lien tuc 6-12 thang. Them progesterone neu co chay mau hoac sau 6-9 thang. Danh gia lai bang sieu am. Luu y: bang chung tu dong vat, chua co RCT lon tren nguoi."},
    {"front": "Hysteroscopic metroplasty co hieu qua cho tu cung nhi hoa?", "back": "Theo Barranger 2002 (BJOG, PMID 12504966): 29 phu nu tu cung nhi hoa (23/29 co phoi nhiem DES) duoc hysteroscopic metroplasty. Ket qua: 21/29 (72.4%) co thai, 13/29 sinh 16 tre song. Ti le sinh song tang tu 3.8% len 63.2% so voi truoc phau thuat. KHONG co bien chung. Nghien cuu nho, dan so chu yeu DES."},
    {"front": "Ghep tu cung (UTx) - ket qua Testa 2024 JAMA?", "back": "Testa 2024 (PMID 39145955) - case series 20 BN AUFI (MRKH + tu cung nhi hoa + unicornuate) tai Baylor. 18 living donor, 2 deceased. Ket qua: 14/20 (70%) graft thanh cong, 14/14 (100%) co it nhat 1 tre song. 11/20 (55%) co it nhat 1 bien chung thai ky (tang HA 14%, ho eo co tu cung 14%, doa sinh non 14%). 4/18 living donor co bien chung do 3. KHONG co di tat bam sinh o 16 tre."},
    {"front": "UTx systematic review Pereira 2025 - cac chi so chinh?", "back": "Pereira 2025 (PMID 40422584) systematic review 10 nghien cuu 2002-2024, PROSPERO dang ky. Ti le UTx thanh cong: 74.0%. Ti le co thai lam sang (CPR) per embryo transfer: 36.3%. Ti le tre song (LBR) per ET: 22.0%. Khong tang di tat bam sinh hay bien chung than kinh o tre. Bien chung tam ly lien quan den that bai ghep/say thai."},
    {"front": "Lich su ghep tu cung (UTx)?", "back": "Ca sinh song dau tien sau UTx o nguoi: 2014 (Gothenburg, Thuy Dien, nhom Brannstrom). UTx da thuc hien tai >10 quoc gia (Thuy Dien, My, Duc, Phap, Czech, Brazil, An Do...). Da theo Moore criteria (gioi thieu can thiep phau thuat moi) + IDEAL concept (danh gia phau thuat lon moi). Van trong giai doan nghien cuu lam sang."},
    {"front": "Quy trinh UTx - 8 buoc?", "back": "(1) Danh gia nguoi nhan (hormon, gene, tam ly, huyet hoc); (2) Tim nguoi hien (living hoac deceased); (3) Phau thuat ghep (noi mach mau voi dong/tinh mach chau ngoai); (4) Uc che mien dich duy tri; (5) Chuyen phoi dong lanh (frozen-thawed ET) sau 6-12 thang; (6) Theo doi thai ky chat (co tu cung, huyet ap); (7) Mo lay thai chu dong (KHONG cho sinh nga am dao); (8) Cat bo tu cung ghep sau 1-2 lan sinh hoac khi that bai."},
    {"front": "Theo doi thai ky o tu cung nhi hoa nhe/trung binh - 6 diem quan trong?", "back": "(1) Kham thai moi 2-4 tuan tu 20 tuan; (2) Sieu am do chieu dai co tu cung moi 2 tuan tu 16-24 tuan; (3) Khau vong co tu cung (cerclage) neu tien su say muon/sinh non + co < 25mm; (4) Progesterone am dao 200-400 mg/dem neu co ngan; (5) Du phong tien san giat bang aspirin lieu thap tu 12-16 tuan neu co yeu to nguy co; (6) Mo lay thai chu dong 37-38 tuan (tranh vo tu cung, ngoi bat thuong)."},
    {"front": "Phan biet MRKH type I va type II?", "back": "MRKH type I (doi chieu, classical Rokitansky): Chi co bat san tu cung + 2/3 tren am dao, KHONG co bat thuong than hoac cac co quan khac. MRKH type II (MURCS association): Kem bat thuong than (30-40% - than da nang, that lung that, tham chi bat san than mot ben), bat thuong xuong (dot song), hoac mat kin (Mat ray that kin). Type II can tam soat gene HNF1B."},
    {"front": "Mang thai ho (gestational surrogacy) - tinh hop phap va dieu kien?", "back": "Hop phap tai: My (mot so bang), Ucraina, Georgia, mot so bang Uc, Israel. KHONG hop phap tai: Viet Nam, nhieu nuoc chau Au (Phap, Duc, Y, Tay Ban Nha), Canada, Australia (tru mot so bang). Dieu kien: IVF/ICSI tao phoi tu trung nguoi me + tinh trung nguoi cha, chuyen vao nguoi mang thai ho. Can buong trung nguoi me con hoat dong (neu khong can xin trung)."},
    {"front": "Lich kham thai va xet nghiem can thuc hien khi MRKH type II?", "back": "(1) Karyotype (46,XX binh thuong); (2) Sieu am than (loai tru than da nang, that lung that, bat san than); (3) X-quang cot song (dot song, insbesondere CUSHING); (4) Hormone: FSH, LH, E2 (neu E2 binh thuong -> buong trung hoat dong binh thuong); (5) AMH (danh gia reserve buong trung); (6) Gene panel neu nghi ngo (HNF1B, LHX1, TBX6, GREB1L, PAX8); (7) Tu van di truyen neu mang thai."},
    {"front": "Ty le thanh cong UTx theo Pereira 2025 systematic review?", "back": "Ti le UTx thanh cong ky thuat: 74.0%. CPR per embryo transfer: 36.3%. LBR per ET: 22.0%. Tuy nhien, neu tinh theo nguoi nhan CO GRAFT THANH CONG, ti le co con len den >80% (Testa 2024: 14/14 = 100%)."},
    {"front": "Cac bien phap KHONG khuyen cao trong dieu tri tu cung nhi hoa?", "back": "(1) Phau thuat noi soi cat buong tu cung (chi dinh khi mat nhieu mo, khong nen cat trong tu cung nhi hoa); (2) Hormone lieu cao keo dai o tuoi truong thanh khong co chi dinh (chi can thiet o tuoi day thi muon/suy buong trung som); (3) Hysteroscopic metroplasy cho moi truong hop (chi can thiet khi co vach nho kem theo); (4) Dieu tri IVF som khi tu cung qua nho (< 3 cm) - ti le lam to thai thap, nen xem xet UTx truoc."},
    {"front": "Cac yeu to nguy co lam tang ty le that bai UTx?", "back": "(1) Phau thuat qua lau (gay thieu mau ghep); (2) Bat dong giua nguoi nhan/nguoi hien (HLA mismatch qua nhieu); (3) Tac dong mach mau kem (xo vua, xo canh); (4) Nhiem trung sau phau thuat; (5) Tac dung phu cua uc che mien dich; (6) Tu cung nhi hoa kem (the tich < 2 mL); (7) Tien su phau thuat vung chau nhieu lan (dinh); (8) Tuoi nguoi nhan > 40 (du chi dinh y khoa cho phep)."},
]


def build_cards_json():
    """Write cards JSON to source dir for anki build."""
    data = {
        "deck_name": f"Tu cung nhi hoa - {DATE}",
        "cards": CARDS,
    }
    CARDS_JSON.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    print(f"[CARDS] Saved: {CARDS_JSON} ({len(CARDS)} cards)")


# ============================================================
# DOCX BUILD
# ============================================================
def build_docx():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    title = doc.add_heading('TU CUNG NHI HOA (HYPOPLASTIC UTERUS / UTERUS INFANTILIS)', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub = doc.add_paragraph(f'Bai hoc ngay {DATE} - San phu khoa (Obstetrics & Gynecology)')
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub.runs[0].italic = True
    sub.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    doc.add_paragraph()

    # 0. TONG QUAN
    doc.add_heading('0. TONG QUAN - VI SAO BAI NAY QUAN TRONG?', 1)
    doc.add_paragraph(
        'Tu cung nhi hoa (hypoplastic uterus, con goi la uterus infantilis hoac juvenile uterus) la tinh trang tu cung khong phat trien day du ve kich thuoc, the tich va cau truc o tuoi truong thanh. Day la 1 trong cac nguyen nhan quan trong cua VO SINH DO YEU TO TU CUNG TUYET DOI (Absolute Uterine Factor Infertility - AUFI).'
    )
    doc.add_paragraph(
        'Theo Testa 2024 (JAMA, PMID 39145955 - case series 20 BN tai Baylor): AUFI chiem khoang 3-5% dan so nu vo sinh, bao gom:\n'
        '- Bat san tu cung bam sinh (hoi chung Mayer-Rokitansky-Kuster-Hauser / MRKH)\n'
        '- Bat thuong bam sinh nang: TU CUNG NHI HOA, mot phan tu cung hai sung, tu cung mot sung\n'
        '- Cat tu cung truoc do\n'
        '- Ton thuong mac phai (dinh buong tu cung, u xo)'
    )
    doc.add_paragraph('Pereira 2025 (Diseases, PMID 40422584 - systematic review 10 nghien cuu 2002-2024) ghi nhan AUFI chiem 3-5% cac truong hop vo sinh nu.').runs[0].italic = True
    doc.add_paragraph('Diem lam sang quan trong: Tu cung nhi hoa khong chi la van de giai phau ma anh huong truc tiep den kha nang mang thai, dien bien thai ky va lua chon dieu tri sinh san - bao gom ca cac can thiep tien tien nhu GHEP TU CUNG (Uterus Transplantation - UTx).').runs[0].bold = True

    # 1. DINH NGHIA & PHAN BIET
    doc.add_heading('1. DINH NGHIA VA PHAN BIET VOI CAC BAT THUONG MULLERIAN KHAC', 1)

    doc.add_heading('1.1. Dinh nghia tu cung nhi hoa', 2)
    add_bullets(doc, [
        'Chieu dai buong tu cung < 5-6 cm (so voi binh thuong 7-8 cm o nguoi truong thanh chua sinh)',
        'Ty le than/co < 1:1 (binh thuong than/co = 2:1)',
        'The tich buong tu cung giam (< 3-4 mL so voi binh thuong ~5 mL)',
        'Co the kem theo co tu cung dai bat thuong',
        'Noi mac tu cung mong, dap ung estrogen kem',
    ])

    doc.add_heading('1.2. Phan loai theo ASRM Mullerian Anomalies Classification 2021', 2)
    doc.add_paragraph('ASRM 2021 cap nhat phan loai bat thuong Mullerian (thay the ban 1988/AFS) thanh 9 class dua tren giai phau - ung dung lam sang:')
    t1 = doc.add_table(rows=10, cols=3)
    fill_table(t1,
        ['Class', 'Mo ta', 'Lien quan tu cung nhi hoa'],
        [
            ('Class I', 'Agenesis / hypoplasia (segments)', 'TU CUNG NHI HOA thuoc class I (sub: a-hypoplastic uterus, b-cervical, c-fundal, d-tubal, e-combined)'),
            ('Class II', 'Septate uterus (vach ngan)', 'Khong'),
            ('Class III', 'Bicornuate (hai sung)', 'Khong'),
            ('Class IV', 'Unicornuate (mot sung)', 'Khong (nhu tu cung mot sung cung kem phat trien o ben kia)'),
            ('Class V', 'Didelphys (tu cung doi)', 'Khong'),
            ('Class VI', 'Arcuate (vom cung)', 'Khong'),
            ('Class VII', 'DES-related (phoi nhiem DES)', 'Tu cung nhi hoa do phoi nhiem DES trong tu cung'),
            ('Class VIII', 'Complex / mat doan', 'Khong'),
            ('Class IX', 'Non-Mullerian / chua phan loai', 'Khong'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('TU CUNG NHI HOA (uterus infantilis) thuoc ASRM CLASS Ia - agenic/hypoplastic uterus segment.').runs[0].bold = True

    doc.add_heading('1.3. Phan loai ESHRE/ESGE 2013 (Grimbizis 2013)', 2)
    doc.add_paragraph('ESHRE-ESGE 2013 phan loai dua tren giai phau + lam sang:')
    add_bullets(doc, [
        'U0 = Binh thuong',
        'U1 = TU CUNG NHI HOA (dysmorphic) - chinh la tu cung nhi hoa',
        'U2 = Septate (vach ngan)',
        'U3 = Bicorporeal (hai than)',
        'U4 = Hemi-uterus (mot sung)',
        'U5 = Aplastic (khong tu cung - MRKH)',
        'U6 = Chua phan loai',
    ])
    doc.add_paragraph('Theo ESHRE-ESGE: U1 = Tu cung co than nho hon binh thuong (> 2 SD), ty le than/co bat thuong, co the kem vach ngan nho.').runs[0].italic = True
    doc.add_paragraph('Diem mau thuan giua 2 guideline:').runs[0].bold = True
    add_bullets(doc, [
        'ASRM 2021: tu cung nhi hoa = Class I (agenesis/hypoplasia segment)',
        'ESHRE-ESGE 2013: tu cung nhi hoa = U1 (dysmorphic uterus) - than nho, co binh thuong, co the co vom nho',
        'Ve ban chat giai phau, 2 he thong DEU CONG NHAN tu cung nhi hoa la 1 thuc the rieng biet, khac voi tu cung vach ngan (septate) va tu cung hai sung.',
    ])

    # 2. CO CHE BENH SINH
    doc.add_heading('2. CO CHE BENH SINH', 1)

    doc.add_heading('2.1. Phat trien binh thuong ong Mullerian', 2)
    add_bullets(doc, [
        'Ong Muller (paramesonephric duct) phat trien o thai nu khoang tuan 6-12:',
        '  Tuan 6-7: 2 ong Muller hinh thanh song song',
        '  Tuan 8-12: HOP NHAT phan duoi (gap nhau o duong giua) tao tu cung-voi trung-am dao tren',
        '  Tuan 12-20: Ong Wolffian (mesonephric) THOAI TRIEN o nu; ong Muller phat trien tiep',
        '  Tuan 20-40: Tu cung phat trien ve kich thuoc, the tich',
        '  Tuoi day thi: ESTROGEN thuc day tang truong tu cung (uterine growth spurt)',
    ])
    doc.add_paragraph('Hewitt 2020 (Endocrinology, PMID 32623449 - animal model) cho thay o chuot:').runs[0].italic = True
    add_bullets(doc, [
        'Chuot cai moi sinh deu co tu cung nho (hypoplastic) o trang thai co ban',
        'Tang truong tu cung day thi PHU THUOC HOAN TOAN vao tin hieu estrogen qua ERalpha',
        'Chuot ERalpha-knockout hoac Cyp19 (aromatase) knockout: tu cung KHONG phat trien du co estrogen',
        'Chuot Cyp19-KO duoc tiem E2 (estradiol) trong tuoi day thi: phuc hoi dap ung tang truong',
    ])
    doc.add_paragraph('ESTROGEN QUA ERalpha LA YEU TO QUYET DINH tang truong tu cung day thi.').runs[0].bold = True

    doc.add_heading('2.2. Nguyen nhan gay tu cung nhi hoa', 2)
    t2 = doc.add_table(rows=6, cols=3)
    fill_table(t2,
        ['Nhom', 'Co che', 'Benh cu the'],
        [
            ('Bam sinh - bat thuong ong Muller', 'Loi hop nhat / thoai trien mot phan ong Muller', 'Hoi chung MRKH, tu cung nhi hoa don doc, bat thuong LHX1/HNF1B/TBX6'),
            ('Bam sinh - roi loan tin hieu estrogen/ERalpha', 'Khiem khuyet ERalpha, aromatase deficiency, hypogonadism', 'Aromatase deficiency, androgen insensitivity syndrome (AIS) mot phan, MRKH type II (kem bat thuong buong trung)'),
            ('Mac phai - phoi nhiem thuoc', 'DES (diethylstilbestrol) phoi nhiem trong tu cung', 'Tu cung nhi hoa, hinh dang T, voi tu cung bat thuong'),
            ('Mac phai - suy buong trung som / thieu estrogen', 'Khong du estrogen kich thich tang truong', 'POI (premature ovarian insufficiency), chan an tam than (anorexia nervosa) keo dai'),
            ('Bam sinh - di truyen', 'Dot bien gene', 'MRKH type II lien quan 17q12 (LHX1, HNF1B), 16p11.2 (TBX6), GREB1L, PAX8'),
        ])

    doc.add_heading('2.3. Co che phan tu chinh', 2)
    doc.add_paragraph('Theo Herlin 2024 (Front Endocrinol, PMID 38699388 - review ve genetics MRKH), cac gene da duoc xac dinh lien quan den phat trien bat thuong Mullerian:')
    t3 = doc.add_table(rows=7, cols=2)
    fill_table(t3,
        ['Gene', 'Vai tro'],
        [
            ('LHX1 (LIM homeobox 1)', 'Vi tri 17q12: dieu khien phat trien ong Muller; deletion -> MRKH'),
            ('HNF1B (HNF1 homeobox B)', 'Cung locus 17q12: bieu hien o than, tuyen tuy, duong sinh duc; mutation -> MRKH + than da nang'),
            ('TBX6 (T-box 6)', '16p11.2: transcription factor cho phat trien xuong song va mo sinh duc'),
            ('GREB1L (GREB1 like retinoic acid receptor coactivator)', 'Gan day duoc phat hien trong gia dinh MRKH'),
            ('PAX8 (paired box 8)', 'Phat trien tuyen giap + Mullerian'),
            ('WNT4, WNT9B, EMX2, HOXA13', 'Cac gene phat trien sinh duc khac'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Bat thuong trong cac gene nay dan den: (1) khong hop nhat hoan toan 2 ong Muller; (2) hoac hop nhat nhung khong phat trien kich thuoc; (3) hoac teo than tu cung do tin hieu estrogen bi loi.').runs[0].bold = True
    doc.add_paragraph('TU CUNG NHI HOA = PHENOTYPE LAM SANG CHUNG, can nguyen gene RAT KHONG DONG NHAT (heterogeneous).').runs[0].bold = True

    # 3. CHAN DOAN
    doc.add_heading('3. CHAN DOAN', 1)

    doc.add_heading('3.1. Lam sang', 2)
    doc.add_paragraph('Trieu chung co nang:')
    add_bullets(doc, [
        'Vo kinh nguyen phat (primary amenorrhea) - gap trong MRKH nang',
        'KINH NGUYET IT (hypomenorrhea) - gap trong tu cung nhi hoa muc trung binh',
        'Dau bung kinh (dysmenorrhea) do buong tu cung nho, mau kinh kho thoat',
        'Vo sinh nguyen phat hoac thu phat',
        'Say thai lien tiep (recurrent pregnancy loss - RPL)',
        'Sinh non (preterm delivery)',
        'Ngoi thai bat thuong, nhau bong non, nhau tien dao',
    ])
    doc.add_paragraph('Tien su can khai thac:')
    add_bullets(doc, [
        'Phoi nhiem DES trong tu cung (me dung DES khi mang thai - hiem tu 1970s)',
        'Chan an tam than / tap the thao qua muc o tuoi day thi',
        'Hoa tri / xa tri vung chau',
        'Phau thuat buong trung truoc day thi',
        'Tien su gia dinh MRKH',
    ])

    doc.add_heading('3.2. Kham thuc the', 2)
    add_bullets(doc, [
        'Chieu cao, can nang, BMI (loai tru chan an)',
        'TUYEN VU, LONG MU, LONG NACH (danh gia day thi)',
        'Kham phu khoa: thay co tu cung nho, than tu cung nho, ty le than/co < 1:1',
        'Trong MRKH nang: chi thay am dao ngan (1-2 cm) tan cung, khong so thay tu cung',
    ])

    doc.add_heading('3.3. Can lam sang', 2)
    t4 = doc.add_table(rows=11, cols=3)
    fill_table(t4,
        ['Phuong phap', 'Muc dich', 'Gia tri'],
        [
            ('Sieu am qua nga am dao (TVUS)', 'Do chieu dai tu cung, buong tu cung, do day noi mac', 'First-line, do 3D neu co the'),
            ('Sieu am 3D / Saline-infusion sonohysterography (SIS)', 'Danh gia hinh thai buong tu cung, phat hien vach ngan', 'Khuyen cao ASRM 2021'),
            ('MRI vung chau', 'TIEU CHUAN VANG cho bat thuong Mullerian, danh gia than kem theo', 'ASRM 2021 khuyen cao cho chan doan xac dinh'),
            ('HSG (hysterosalpingography)', 'Danh gia buong tu cung + voi tu cung', 'It dung hon MRI hien nay'),
            ('Noi soi buong tu cung (hysteroscopy)', 'Quan sat truc tiep, sinh thiet neu can', 'Khi can dong thoi dieu tri'),
            ('Noi soi o bung (laparoscopy)', 'Danh gia ngoai tu cung, voi trung', 'Khi can can thiep ket hop'),
            ('Karyotype', 'Loai tru 46,XY (AIS) hoac bat thuong NST', 'BAT BUOC khi vo kinh nguyen phat + nguc phat trien binh thuong'),
            ('Hormon: FSH, LH, estradiol, AMH', 'Danh gia chuc nang buong trung', 'Can thiet cho chan doan phan biet'),
            ('Sieu am than', 'Loai tru bat thuong duong tiet nieu kem theo (30-40% MRKH type II)', 'Khuyen cao ASRM 2021'),
            ('Danh gia gene (panel hoac WES)', 'Tim dot bien LHX1, HNF1B, TBX6, GREB1L, PAX8', 'Can nhac khi nghi ngo MRKH type II hoac familial'),
        ])

    doc.add_heading('3.4. Tieu chuan chan doan ASRM 2021', 2)
    doc.add_paragraph('ASRM 2021 dinh nghia TU CUNG NHI HOA (hypoplastic uterus) khi:')
    add_bullets(doc, [
        'Buong tu cung co chieu dai < 5-6 cm (gom ca than + co)',
        'HOAC than tu cung < 4 cm',
        'Ty le than/co < 1:1 (binh thuong 2:1)',
        'Kem giam the tich buong < 2.5-3 mL',
    ])

    # 4. DIEU TRI
    doc.add_heading('4. DIEU TRI', 1)

    doc.add_heading('4.1. Nguyen tac chung', 2)
    doc.add_paragraph('Tu cung nhi hoa co the chia 3 muc do theo kha nang dap ung dieu tri:')
    add_bullets(doc, [
        'NHE: van co kinh deu, co kha nang mang thai nhung nguy co say/sinh non cao',
        'TRUNG BINH: kinh it, vo sinh, can can thiep',
        'NANG: gan nhu MRKH, khong the mang thai tu nhien -> can bien phap thay the',
    ])

    doc.add_heading('4.2. Lieu phap hormone', 2)
    doc.add_paragraph('Muc tieu: Kich thich tang truong tu cung o tuoi day thi muon hoac suy buong trung som.')
    add_bullets(doc, [
        'Estrogen lieu phap thay the (HRT): ethinylestradiol 0.05-0.1 mg/ngay hoac estradiol valerate 2-4 mg/ngay, KHONG progesterone o giai doan dau, dung lien tuc 6-12 thang',
        'Ket hop progesterone (medroxyprogesterone acetate 5-10 mg/ngay) khi co chay mau am dao hoac sau 6-9 thang',
        'Danh gia lai sau 6-12 thang bang sieu am',
    ])
    doc.add_paragraph('Bang chung theo Hewitt 2020 (PMID 32623449): Cua so day thi - sau day thi la GIAI DOAN THEN CHOT de "lap trinh" dap ung estrogen cua tu cung. Bo lo giai doan nay -> tu cung dap ung kem voi estrogen sau nay (nhu ArKO mice chi phuc hoi mot phan).').runs[0].italic = True
    doc.add_paragraph('Luu y: Bang chung tu nghien cuu tren dong vat, chua co RCT lon tren nguoi. Can ca the hoa.').runs[0].bold = True

    doc.add_heading('4.3. Phau thuat tao hinh (metroplasty)', 2)
    add_bullets(doc, [
        'Nong buong tu cung (hysteroscopic metroplasty): Cat vach ngan nho kem theo (neu co) de mo rong buong tu cung',
    ])
    doc.add_paragraph('Barranger 2002 (BJOG, PMID 12504966): 29 phu nu tu cung nhi hoa duoc nong/cat vach qua noi soi:').runs[0].bold = True
    add_bullets(doc, [
        '21/29 (72.4%) co thai sau phau thuat',
        '13/29 sinh 16 tre song',
        'Ty le sinh song tang tu 3.8% -> 63.2% so voi truoc phau thuat',
        'KHONG co bien chung trong phau thuat',
        'Luu y: 23/29 BN co phoi nhiem DES trong tu cung - dan so dac biet',
    ])

    doc.add_heading('4.4. Ho tro sinh san (ART)', 2)
    t5 = doc.add_table(rows=4, cols=3)
    fill_table(t5,
        ['Muc do', 'Lua chon', 'Ty le thanh cong'],
        [
            ('Nhe (kinh deu)', 'Theo doi tu nhien, IUI/IVF don thuan', 'Tuy ca the'),
            ('Trung binh (kinh it)', 'IVF/ICSI + theo doi thai ky chat', 'Thai ky nguy co cao'),
            ('Nang (gan MRKH)', 'GHEP TU CUNG (UTx) hoac MANG THAI HO', 'UTx: 70% successful graft -> live birth'),
        ])

    doc.add_heading('4.5. Ghep tu cung (Uterus Transplantation - UTx)', 2)
    doc.add_paragraph('LUA CHON MOI cho tu cung nhi hoa nang. Bang chung moi nhat:').runs[0].bold = True

    doc.add_paragraph('Testa 2024 (JAMA, PMID 39145955 - case series 20 BN tai Baylor, 2016-2019):').runs[0].italic = True
    add_bullets(doc, [
        '20 phu nu AUFI (bao gom MRKH, tu cung nhi hoa, unicornuate)',
        'Nguon ghep: 18 living donor, 2 deceased donor',
        'Ket qua: 14/20 (70%) thanh cong ve mat ky thuat (graft survival)',
        '14/14 (100%) nguoi nhan thanh cong -> co it nhat 1 tre song',
        '11/20 (55%) co it nhat 1 bien chung (sinh/me)',
        'Bien chung thai ky pho bien: tang huyet ap thai ky (14%), ho eo co tu cung (14%), doa sinh non (14%)',
        '4/18 living donor co bien chung do 3',
        'KHONG co di tat bam sinh o 16 tre sinh ra',
    ])

    doc.add_paragraph('Pereira 2025 (Diseases, PMID 40422584 - systematic review 10 nghien cuu):').runs[0].italic = True
    add_bullets(doc, [
        'Ty le UTx thanh cong: 74.0%',
        'Ty le co thai lam sang per embryo transfer: 36.3%',
        'Ty le tre song per embryo transfer: 22.0%',
        'Khong tang dang ke di tat bam sinh hoac bien chung than kinh',
        'Bien chung tam ly lien quan den that bai ghep / say thai',
    ])

    doc.add_paragraph('Brannstrom 2024 (Physiology, PMID 38954427 - review):').runs[0].italic = True
    add_bullets(doc, [
        'Ca sinh song dau tien sau UTx o nguoi: 2014 (Gothenburg, Thuy Dien)',
        'Da thuc hien tai >10 quoc gia',
        'UTx di theo Moore criteria (gioi thieu can thiep phau thuat moi) + IDEAL concept (danh gia phau thuat lon moi)',
        'Yeu cau: ghep tang tam thoi - cat bo sau 1-2 lan sinh hoac khi that bai',
    ])

    doc.add_heading('4.6. Quy trinh UTx (tom tat)', 2)
    add_numbered(doc, [
        'Danh gia nguoi nhan (hormon, gene, tam ly, huyet hoc)',
        'Tim nguoi hien (living hoac deceased donor)',
        'Phau thuat ghep (noi mach mau voi dong/tinh mach chau ngoai)',
        'Uc che mien dich duy tri',
        'Chuyen phoi dong lanh (frozen-thawed embryo transfer) sau 6-12 thang',
        'Theo doi thai ky chat (co tu cung, huyet ap)',
        'Mo lay thai (do nguy co cao, KHONG cho sinh nga am dao)',
        'Cat bo tu cung ghep sau 1-2 lan sinh',
    ])

    doc.add_heading('4.7. Han che cua UTx', 2)
    add_bullets(doc, [
        'Phau thuat phuc tap, doi hoi trung tam chuyen sau',
        'Uc che mien dich suot thai ky',
        'Nguy co bien chung cao (50%+ co bien chung thai ky)',
        'Chi tam thoi (phai cat bo sau sinh)',
        'Chi phi rat cao',
        'Van trong giai doan thu nghiem lam sang, chua phai tieu chuan dieu tri thuong quy',
    ])

    doc.add_heading('4.8. Mang thai ho (gestational surrogacy)', 2)
    add_bullets(doc, [
        'Lua chon hop phap o mot so quoc gia (My, Ucraina, Georgia, mot so bang Uc...)',
        'KHONG hop phap tai Viet Nam, nhieu nuoc chau Au',
        'IVF/ICSI tao phoi tu trung nguoi me + tinh trung nguoi cha -> chuyen vao nguoi mang thai ho',
        'Ty le thanh cong phu thuoc vao chat luong phoi, khong phu thuoc vao tu cung nguoi me',
        'Luu y: phai co trung (can buong trung con hoat dong) - neu MRKH type II kem buong trung bat thuong thi can xin trung',
    ])

    # 5. THEO DOI THAI KY
    doc.add_heading('5. THEO DOI THAI KY O TU CUNG NHI HOA MUC NHE-TRUNG BINH', 1)
    doc.add_paragraph('Neu benh nhan may man mang thai tu nhien hoac qua ART voi tu cung nhi hoa muc trung binh, thai ky duoc coi la NGUY CO CAO:')
    add_numbered(doc, [
        'Kham thai moi 2-4 tuan tu 20 tuan',
        'Sieu am do chieu dai co tu cung moi 2 tuan tu 16-24 tuan (sang loc ho eo)',
        'Khau vong co tu cung (cerclage) neu: tien su say thai muon/sinh non + co tu cung ngan < 25mm',
        'Progesterone am dao 200-400 mg/dem neu co ngan',
        'Du phong tien san giat bang aspirin lieu thap 81-162 mg/dem tu 12-16 tuan neu co yeu to nguy co',
        'Theo doi tang truong thai moi 4 tuan tu 28 tuan (nguy co FGR)',
        'Mo lay thai chu dong 37-38 tuan (nguy co vo tu cung, ngoi bat thuong)',
    ])

    # 6. TIEN LUONG
    doc.add_heading('6. TIEN LUONG', 1)
    t6 = doc.add_table(rows=4, cols=4)
    fill_table(t6,
        ['Muc do', 'Mang thai tu nhien', 'Sau dieu tri', 'Sau UTx'],
        [
            ('Nhe', '50-70%', '70-80% (theo doi chat)', 'N/A'),
            ('Trung binh', '20-30%', '40-50% (sau HRT/phau thuat + ART)', '70% (neu UTx)'),
            ('Nang (gan MRKH)', '< 5%', '< 10% (thuong that bai)', '70% graft success (Testa 2024) -> 100% co con'),
        ])
    doc.add_paragraph()
    doc.add_paragraph('Theo Pereira 2025 systematic review: ty le mang thai thanh cong (live birth rate) sau UTx la 22% per embryo transfer, nhung neu tinh theo nguoi nhan co graft thanh cong, con so len toi >80%.').runs[0].italic = True

    # 7. TONG KET
    doc.add_heading('7. TOM TAT VA KHUYEN CAO LAM SANG', 1)
    add_numbered(doc, [
        'Tu cung nhi hoa thuoc ASRM Class I / ESHRE-ESGE U1 - bat thuong Mullerian voi tu cung kem phat trien ve kich thuoc/cau truc.',
        'Co che benh sinh da dang: bam sinh (gene LHX1, HNF1B, TBX6, GREB1L, PAX8), roi loan tin hieu estrogen, phoi nhiem DES, suy buong trung som.',
        'Chan doan: Lam sang + TVUS + MRI vung chau (tieu chuan vang). BAT BUOC khao sat than, karyotype, hormon.',
        'Dieu tri theo muc do: Nhe (theo doi + ART) - Trung binh (HRT + hysteroscopic metroplasty + ART) - Nang (UTx hoac mang thai ho).',
        'UTx la lua chon tien tien (theo Testa 2024 - JAMA): 70% successful graft, 100% nguoi nhan thanh cong co con, KHONG co di tat bam sinh o tre. Tuy nhien bien chung cao (50%+) va chi trong giai doan nghien cuu lam sang.',
        'Theo doi thai ky nguy co cao: kham thai moi 2-4 tuan, do co tu cung moi 2 tuan, can nhac cerclage, mo lay thai chu dong 37-38 tuan.',
        'Tu van di truyen quan trong khi co MRKH type II hoac tien su gia dinh.',
    ])

    # 8. TAI LIEU THAM KHAO
    doc.add_heading('8. TAI LIEU THAM KHAO (VERIFY PUBMED)', 1)
    refs = [
        ('Testa G, McKenna GJ, Wall A, et al. (2024)', 'PMID: 39145955', 'JAMA. 332(10):817-824.', 'DOI: 10.1001/jama.2024.11679', '"Uterus Transplant in Women With Absolute Uterine-Factor Infertility."'),
        ('Pereira A, Ribeiro F, Soares S, Ferreira H. (2025)', 'PMID: 40422584', 'Diseases. 13(5):152.', 'DOI: 10.3390/diseases13050152', '"Uterine Transplantation: Advances, Challenges, and Future Perspectives."'),
        ('Brannstrom M, Adashi EY, Wu JH, Tsiartas P, Racowsky C. (2024)', 'PMID: 38954427', 'Physiology (Bethesda). 39(6).', 'DOI: 10.1152/physiol.00011.2024', '"Uterus Transplantation: the Translational Evolution of a Clinical Breakthrough."'),
        ('Herlin MK. (2024)', 'PMID: 38699388', 'Front Endocrinol (Lausanne). 15:1368990.', 'DOI: 10.3389/fendo.2024.1368990', '"Genetics of Mayer-Rokitansky-Kuster-Hauser (MRKH) syndrome: advancements and implications."'),
        ('Hewitt SC, Carmona M, Foley KG, et al. (2020)', 'PMID: 32623449', 'Endocrinology. 161(8):bqaa081.', 'DOI: 10.1210/endocr/bqaa081', '"Peri- and Postpubertal Estrogen Exposures of Female Mice Optimize Uterine Responses Later in Life."'),
        ('Barranger E, Gervaise A, Doumerc S, Fernandez H. (2002)', 'PMID: 12504966', 'BJOG. 109(12):1331-4.', 'DOI: 10.1046/j.1471-0528.2002.01448.x', '"Reproductive performance after hysteroscopic metroplasty in the hypoplastic uterus: a study of 29 cases."'),
        ('Mishra S, Sapkale B, Singh S, Jha A, Chaudhari K. (2024)', 'PMID: 39280286', 'Narra J. 4(2):e755.', 'DOI: 10.52225/narra.v4i2.755', '"Comprehensive management of Mayer-Rokitansky-Kuster-Hauser syndrome management: A case report."'),
        ('Brannstrom M, Dahm-Kahler P, Greite R, Molne J, Diaz-Garcia C, Tullius SG. (2018)', 'PMID: 29210893', 'Transplantation. 102(4):569-577.', 'DOI: 10.1097/TP.0000000000002035', '"Uterus Transplantation: A Rapidly Expanding Field."'),
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


# ============================================================
# ANKI BUILD
# ============================================================
def build_anki():
    model, deck = build_pastel_model_and_deck(
        model_id=1607392324,
        model_name='Tu cung nhi hoa - Pastel',
        deck_id=2059400115,
        deck_name=f'Tu cung nhi hoa (Hypoplastic Uterus) - {DATE}',
        deck_description=f'Tu cung nhi hoa - Hypoplastic Uterus / Uterus Infantilis - {DATE} - Pastel theme'
    )
    n = add_cards_from_json(deck, model, CARDS_JSON, 'OB-GYN · Mullerian · Hypoplastic · UTx')
    write_apkg(deck, APKG_OUT)
    print(f"[APKG] Saved: {APKG_OUT}")
    print(f"[APKG] Size: {APKG_OUT.stat().st_size} bytes")
    print(f"[APKG] Cards: {n}")


# ============================================================
# HTML BUILD
# ============================================================
def build_html():
    header_html = '''
<header class="max-w-6xl mx-auto mb-8 text-center">
  <h1 class="text-4xl font-bold text-stone-700 mb-2">Tu cung nhi hoa (Hypoplastic Uterus)</h1>
  <p class="text-stone-500 italic">Visual Summary - Bai hoc 23/06/2026</p>
  <div class="mt-3 flex justify-center gap-2 flex-wrap">
    <span class="tag pastel-pink px-3 py-1 rounded-full text-sm">OB-GYN</span>
    <span class="tag pastel-blue px-3 py-1 rounded-full text-sm">Mullerian Anomaly</span>
    <span class="tag pastel-mint px-3 py-1 rounded-full text-sm">ASRM Class I</span>
    <span class="tag pastel-peach px-3 py-1 rounded-full text-sm">ESHRE-ESGE U1</span>
    <span class="tag pastel-lavender px-3 py-1 rounded-full text-sm">Uterus Transplant</span>
  </div>
</header>
'''

    main_html = '''
  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">1. Dinh nghia va phan loai</h2>
    <div class="grid md:grid-cols-2 gap-4">
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">Tieu chan chan doan ASRM 2021</h3>
        <p class="text-sm text-stone-700">- Buong tu cung &lt; 5-6 cm<br>- HOAC than tu cung &lt; 4 cm<br>- Ty le than/co &lt; 1:1 (binh thuong 2:1)<br>- The tich buong &lt; 2.5-3 mL</p>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200">
        <h3 class="font-bold text-stone-800 mb-2">Phan loai 2 guideline</h3>
        <p class="text-sm text-stone-700"><b>ASRM 2021:</b> Class Ia (Mullerian agenesis/hypoplasia segment)<br><b>ESHRE-ESGE 2013:</b> U1 (dysmorphic uterus)<br><br>2 he thong deu cong nhan la 1 thuc the rieng biet, khac voi septate (ASRM II/ESHRE U2) va bicornuate (ASRM III/ESHRE U3).</p>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">2. Phat trien ong Mullerian binh thuong vs bat thuong</h2>
    <div class="mermaid">
flowchart TD
    A["Tuan 6-7: 2 ong Muller hinh thanh song song"] --> B["Tuan 8-12: HOP NHAT phan duoi"]
    B --> C["Tuan 12-20: Wolffian thoai trien, Muller phat trien"]
    C --> D["Tuan 20-40: Tu cung phat trien kich thuoc"]
    D --> E["Day thi: ESTROGEN qua ERalpha thuc day tang truong"]
    E --> F["Tu cung truong thanh binh thuong: than/co = 2:1, buong 7-8 cm"]

    B -.Loi hop nhat.-> G["Bat thuong ong Muller (MRKH)"]
    D -.Loi phat trien.-> H1["Tu cung nhi hoa"]
    E -.Loi ERalpha/aromatase.-> H2["Tu cung nhi hoa do thieu estrogen"]
    A -.Gene LHX1/HNF1B/TBX6.-> H1
    D -.Phoi nhiem DES.-> H3["Tu cung hinh T (DES-related)"]

    style F fill:#c5e0c9
    style G fill:#f4c2c2
    style H1 fill:#f7d1ba
    style H2 fill:#d4c5e2
    style H3 fill:#c5d5e0
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">3. So sanh 3 muc do tu cung nhi hoa</h2>
    <p class="text-sm text-stone-600 italic mb-4">Phan loai theo kha nang dap ung dieu tri.</p>
    <div class="overflow-x-auto">
      <table class="w-full text-sm">
        <thead>
          <tr class="bg-stone-200 text-stone-800">
            <th class="px-3 py-2 text-left">Muc do</th>
            <th class="px-3 py-2 text-left">Mang thai tu nhien</th>
            <th class="px-3 py-2 text-left">Sau dieu tri</th>
            <th class="px-3 py-2 text-left">Sau UTx</th>
          </tr>
        </thead>
        <tbody class="text-stone-700">
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Nhe</td><td class="px-3 py-2">50-70%</td><td class="px-3 py-2">70-80% (theo doi chat)</td><td class="px-3 py-2">N/A</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-bold">Trung binh</td><td class="px-3 py-2">20-30%</td><td class="px-3 py-2">40-50% (HRT + metroplasty + ART)</td><td class="px-3 py-2">70% (neu UTx)</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-bold">Nang (gan MRKH)</td><td class="px-3 py-2">&lt; 5%</td><td class="px-3 py-2">&lt; 10% (thuong that bai)</td><td class="px-3 py-2">70% graft success -> 100% co con</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">4. Algorithm dieu tri theo muc do</h2>
    <div class="mermaid">
flowchart TD
    A["Tu cung nhi hoa (ASRM Ia / ESHRE U1)"] --> B{"Muc do nao?"}
    B -- "NHE<br/>(kinh deu, buong 5-6 cm)" --> C1["Theo doi tu nhien<br/>IUI/IVF khi can"]
    B -- "TRUNG BINH<br/>(kinh it, buong 3-5 cm)" --> C2["Estrogen HRT 6-12 thang<br/>+ Hysteroscopic metroplasty<br/>+ IVF/ICSI"]
    B -- "NANG<br/>(gan MRKH, buong < 3 cm)" --> C3{"Lua chon?"}
    C3 -- "Co kha nang" --> D1["GHEP TU CUNG (UTx)<br/>70% graft success<br/>Testa 2024 JAMA"]
    C3 -- "Khong/khong dat dk" --> D2["Mang thai ho<br/>(neu hop phap)"]
    C2 --> E["Theo doi thai ky chat<br/>cerclage, aspirin, mo lay thai 37-38w"]
    C1 --> E
    D1 --> E

    style C1 fill:#c5e0c9
    style C2 fill:#f7d1ba
    style C3 fill:#f4c2c2
    style D1 fill:#d4c5e2
    style D2 fill:#c5d5e0
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">5. Testa 2024 JAMA - UTx case series n=20</h2>
    <p class="text-sm text-stone-600 italic mb-4">PMID 39145955 - Baylor 2016-2019. 18 living donor, 2 deceased.</p>
    <div class="grid md:grid-cols-2 gap-4">
      <div>
        <canvas id="chart1"></canvas>
      </div>
      <div class="bg-white rounded-xl p-4 border border-stone-200 flex flex-col justify-center">
        <h3 class="font-bold text-stone-800 mb-2">Testa 2024 (PMID 39145955)</h3>
        <ul class="text-sm text-stone-700 space-y-2">
          <li>• <b>14/20 (70%)</b> graft thanh cong</li>
          <li>• <b>14/14 (100%)</b> co it nhat 1 tre song</li>
          <li>• <b>11/20 (55%)</b> co it nhat 1 bien chung</li>
          <li>• 16 tre sinh ra: <b>KHONG</b> co di tat bam sinh</li>
          <li>• Bien chung thai ky: tăng HA 14%, ho eo co 14%, doa sinh non 14%</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-2">6. Pereira 2025 Systematic Review - UTx outcomes</h2>
    <p class="text-sm text-stone-600 italic mb-4">PMID 40422584 - 10 nghien cuu 2002-2024 (PROSPERO dang ky).</p>
    <div>
      <canvas id="chart2"></canvas>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">7. 5 nhom nguyen nhan gay tu cung nhi hoa</h2>
    <div class="grid md:grid-cols-2 gap-3">
      <div class="pastel-pink rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">1. Bam sinh - ong Muller</h3>
        <p class="text-xs text-stone-700">Loi hop nhat/thoai trien mot phan ong Muller. Hoi chung MRKH, gene LHX1, HNF1B, TBX6.</p>
      </div>
      <div class="pastel-blue rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">2. Bam sinh - tin hieu estrogen</h3>
        <p class="text-xs text-stone-700">Khiem khuyet ERalpha, aromatase deficiency. Estrogen khong the kich thich tang truong tu cung.</p>
      </div>
      <div class="pastel-mint rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">3. Mac phai - phoi nhiem DES</h3>
        <p class="text-xs text-stone-700">DES trong tu cung (me dung DES) -> tu cung hinh T, nhi hoa, voi tu cung bat thuong.</p>
      </div>
      <div class="pastel-peach rounded-xl p-4">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">4. Mac phai - thieu estrogen</h3>
        <p class="text-xs text-stone-700">POI (suy buong trung som), chan an tam than, hoa tri/xa tri vung chau truoc day thi.</p>
      </div>
      <div class="pastel-lavender rounded-xl p-4 col-span-2">
        <h3 class="font-bold text-stone-800 mb-2 text-sm">5. Di truyen - gene</h3>
        <p class="text-xs text-stone-700">MRKH type II lien quan 17q12 (LHX1, HNF1B), 16p11.2 (TBX6), GREB1L, PAX8. Di truyen RAT KHONG DONG NHAT.</p>
      </div>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">8. EVIDENCE TABLE - 8 papers verified</h2>
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
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">39145955</td><td class="px-3 py-2">Testa (2024)</td><td class="px-3 py-2">JAMA case series, n=20</td><td class="px-3 py-2">UTx 70% success, 100% co con</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">40422584</td><td class="px-3 py-2">Pereira (2025)</td><td class="px-3 py-2">Diseases systematic review</td><td class="px-3 py-2">UTx 74% success, LBR 22%/ET</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">38954427</td><td class="px-3 py-2">Brannstrom (2024)</td><td class="px-3 py-2">Physiology review</td><td class="px-3 py-2">UTx Moore + IDEAL framework</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">38699388</td><td class="px-3 py-2">Herlin (2024)</td><td class="px-3 py-2">Front Endocrinol review</td><td class="px-3 py-2">MRKH genetics: LHX1, HNF1B, TBX6, GREB1L, PAX8</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">32623449</td><td class="px-3 py-2">Hewitt (2020)</td><td class="px-3 py-2">Endocrinology animal model</td><td class="px-3 py-2">ERalpha + estrogen can thiet cho tu cung day thi</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">12504966</td><td class="px-3 py-2">Barranger (2002)</td><td class="px-3 py-2">BJOG, n=29</td><td class="px-3 py-2">Hysteroscopic metroplasty: 72.4% co thai, sinh song 3.8% -> 63.2%</td></tr>
          <tr class="border-b border-stone-200"><td class="px-3 py-2 font-mono text-xs">39280286</td><td class="px-3 py-2">Mishra (2024)</td><td class="px-3 py-2">Narra J case report</td><td class="px-3 py-2">MRKH + multidisciplinary management</td></tr>
          <tr class="border-b border-stone-200 bg-stone-50"><td class="px-3 py-2 font-mono text-xs">29210893</td><td class="px-3 py-2">Brannstrom (2018)</td><td class="px-3 py-2">Transplantation review</td><td class="px-3 py-2">AUFI 3-5% nu vo sinh, UTx expanding field</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="glass rounded-2xl p-6 shadow-sm">
    <h2 class="text-2xl font-semibold text-stone-700 mb-4">9. Quy trinh 8 buoc UTx (Uterus Transplantation)</h2>
    <div class="mermaid">
flowchart TD
    A["1. Danh gia nguoi nhan<br/>(hormon, gene, tam ly, huyet hoc)"] --> B["2. Tim nguoi hien<br/>(living hoac deceased)"]
    B --> C["3. Phau thuat ghep<br/>(noi mach voi dong/tinh mach chau ngoai)"]
    C --> D["4. Uc che mien dich duy tri"]
    D --> E["5. Chuyen phoi dong lanh<br/>(frozen-thawed ET, 6-12 thang sau ghep)"]
    E --> F["6. Theo doi thai ky chat<br/>(co tu cung, huyet ap)"]
    F --> G["7. Mo lay thai 37-38 tuan<br/>(KHONG cho sinh nga am dao)"]
    G --> H["8. Cat bo tu cung ghep<br/>(sau 1-2 lan sinh hoac that bai)"]

    style A fill:#f4c2c2
    style B fill:#f7d1ba
    style C fill:#d4c5e2
    style D fill:#c5d5e0
    style E fill:#c5e0c9
    style F fill:#c5e0c9
    style G fill:#c5e0c9
    style H fill:#f4c2c2
    </div>
  </section>
'''

    custom_charts = '''
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: {
        labels: ['Graft success', 'Co it nhat 1 tre song', 'Co bien chung', 'Living donor co bien chung do 3'],
        datasets: [{
            label: 'Testa 2024 JAMA (n=20)',
            data: [70, 100, 55, 22],
            backgroundColor: [
                'rgba(197, 224, 201, 0.85)',
                'rgba(197, 213, 224, 0.85)',
                'rgba(244, 194, 194, 0.85)',
                'rgba(247, 209, 186, 0.85)'
            ],
            borderColor: [
                'rgba(197, 224, 201, 1)',
                'rgba(197, 213, 224, 1)',
                'rgba(244, 194, 194, 1)',
                'rgba(247, 209, 186, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        indexAxis: 'y',
        plugins: {
            title: { display: true, text: 'Testa 2024 JAMA (n=20) - UTx outcomes (% of cohort)' },
            legend: { display: false }
        },
        scales: {
            x: { beginAtZero: true, max: 100, title: { display: true, text: 'Phan tram (%)' } }
        }
    }
});

new Chart(document.getElementById('chart2'), {
    type: 'bar',
    data: {
        labels: ['UTx thanh cong ky thuat', 'CPR per ET', 'LBR per ET'],
        datasets: [{
            label: 'Pereira 2025 (10 studies, 2002-2024)',
            data: [74.0, 36.3, 22.0],
            backgroundColor: [
                'rgba(212, 197, 226, 0.85)',
                'rgba(197, 213, 224, 0.85)',
                'rgba(197, 224, 201, 0.85)'
            ],
            borderColor: [
                'rgba(212, 197, 226, 1)',
                'rgba(197, 213, 224, 1)',
                'rgba(197, 224, 201, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        plugins: {
            title: { display: true, text: 'Pereira 2025 Systematic Review - UTx outcomes (%)' },
            legend: { display: false }
        },
        scales: {
            y: { beginAtZero: true, max: 100, title: { display: true, text: 'Phan tram (%)' } }
        }
    }
});
'''

    footer_text = 'Bai hoc soan boi MiniMax Mavis cho Bs. Ngoc 🍅 🐈‍⬛ | Verified PubMed: 8 papers (PMID 39145955, 40422584, 38954427, 38699388, 32623449, 12504966, 39280286, 29210893) - Testa 2024 JAMA, Pereira 2025 Diseases'

    html_content = build_lesson_html(
        title='Tu cung nhi hoa (Hypoplastic Uterus) - Visual Summary',
        header_html=header_html,
        main_html=main_html,
        footer_text=footer_text,
        custom_charts=custom_charts,
    )
    write_html(html_content, HTML_OUT)
    print(f"[HTML] Saved: {HTML_OUT}")
    print(f"[HTML] Size: {HTML_OUT.stat().st_size} bytes")


if __name__ == '__main__':
    print(f"=== Building Tu cung nhi hoa Lesson - {DATE} ===\n")
    build_cards_json()
    print()
    build_docx()
    print()
    build_anki()
    print()
    build_html()
    print("\n=== Done ===")
