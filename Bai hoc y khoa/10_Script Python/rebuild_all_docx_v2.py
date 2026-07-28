"""Build all 16 DOCX files with diacritics. Mapping chinh xac."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from md_to_docx import md_to_docx

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
SRC = ROOT / "09_Source - Markdown"


# Mapping CHINH XAC: MD relative path -> (lesson_folder_relative, output_filename)
MAPPING = [
    # ===== 01_San phu khoa =====
    ("01_San phu khoa/03_Preeclampsia_Screening/Preeclampsia_Screening_2026-06-22.md",
     "01_San phu khoa/03_Preeclampsia_Screening",
     "Sang loc Du phong Tien san giat - 2026-06-22.docx"),
    # MD files ở root 09_Source - Markdown
    ("Adenomyosis_ART_2026-06-13.md",
     "01_San phu khoa/02_Adenomyosis - Anh huong ART",
     "Adenomyosis - Anh huong ART - 2026-06-13.docx"),
    ("Endometriosis_2026-06-13.md",
     "01_San phu khoa/01_Lac noi mac tu cung - Endometriosis",
     "Lac noi mac tu cung (Endometriosis) - 2026-06-13.docx"),

    # ===== 02_Ho tro sinh san ART =====
    ("02_Ho tro sinh san ART/07_OHSS/OHSS_Prevention_Management_2026-06-14.md",
     "02_Ho tro sinh san ART/07_OHSS - Prevention and Management",
     "OHSS - Prevention and Management - 2026-06-14.docx"),
    ("02_Ho tro sinh san ART/08_Endometrial_Receptivity_ERA/Endometrial_Receptivity_ERA_2026-06-16.md",
     "02_Ho tro sinh san ART/08_Endometrial_Receptivity_ERA",
     "Endometrial Receptivity ERA - 2026-06-16.docx"),
    ("02_Ho tro sinh san ART/10_ICSI/ICSI_2026-06-20.md",
     "02_Ho tro sinh san ART/10_ICSI",
     "ICSI trong IVF - 2026-06-20.docx"),
    # MD files ở root
    ("AndroGel_ART_2026-06-13.md",
     "02_Ho tro sinh san ART/03_AndroGel - Testosterone priming",
     "AndroGel (Testosterone priming) - 2026-06-13.docx"),
    ("duostim_summary.md",
     "02_Ho tro sinh san ART/05_DuoStim - Nang ton du",
     "Nang ton du ART (DuoStim) - 2026-06-13.docx"),
    ("FET_Endometriosis_2026-06-13.md",
     "02_Ho tro sinh san ART/02_FET - Frozen Embryo Transfer",
     "FET trong Endometriosis - 2026-06-13.docx"),
    ("MCMA_2026-06-13.md",
     "02_Ho tro sinh san ART/01_MCMA - Song thai 1 buong oi",
     "Song thai 1 buong oi (MCMA) - 2026-06-13.docx"),
    ("09_Long_GnRH_Agonist/Long_GnRH_Agonist_Protocol_2026-06-18.md",
     "02_Ho tro sinh san ART/09_Long_GnRH_Agonist_Protocol",
     "Long GnRH Agonist Protocol - 2026-06-18.docx"),
    ("Endometrial_Receptivity_Advanced_US_2026-06-21.md",
     "02_Ho tro sinh san ART/11_Endometrial_Receptivity_Advanced_US_2026-06-21",
     "Endometrial Receptivity Advanced US - 2026-06-21.docx"),

    # ===== 03_Sieu am thai =====
    ("03_Sieu am thai/01_Sieu am tim thai/Sieu am tim thai - sieu chi tiet - 2026-06-19.md",
     "03_Sieu am thai/01_Sieu am tim thai",
     "Sieu am tim thai - sieu chi tiet - 2026-06-19.docx"),
    ("03_Sieu am thai/09_Cervical_Length_PTB/Cervical_Length_Preterm_Birth_2026-06-17.md",
     "03_Sieu am thai/09_Cervical_Length_PTB",
     "Cervical Length Preterm Birth - 2026-06-17.docx"),
    ("03_Sieu am thai/11_First_Trimester_Screening/First_Trimester_Screening_2026-06-22.md",
     "03_Sieu am thai/11_First_Trimester_Screening",
     "First Trimester Screening - 2026-06-22.docx"),
    ("10_Fetal_Doppler/Fetal_Doppler_2026-06-19.md",
     "03_Sieu am thai/10_Fetal_Doppler",
     "Fetal Doppler thai ky - 2026-06-19.docx"),
]


def title_from_md(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return md_path.stem


def main():
    converted = 0
    failed = []
    for rel_md, rel_out_folder, filename in MAPPING:
        md_path = SRC / rel_md
        out_path = ROOT / rel_out_folder / filename
        if not md_path.exists():
            print(f"  [SKIP] {rel_md} - not found")
            failed.append(rel_md)
            continue
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            title = title_from_md(md_path)
            md_to_docx(md_path, out_path, title)
            converted += 1
        except Exception as e:
            print(f"  [ERR]  {rel_md} - {e}")
            failed.append(rel_md)
    print(f"\nConverted: {converted}/{len(MAPPING)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
