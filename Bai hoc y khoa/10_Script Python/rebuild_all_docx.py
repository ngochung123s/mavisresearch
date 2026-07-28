"""Apply md_to_docx for all lesson files."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from md_to_docx import md_to_docx

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
SRC = ROOT / "09_Source - Markdown"


def title_from_md(md_path):
    """Extract title tu first # heading trong MD file."""
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return md_path.stem


def main():
    """Auto-find all bai hoc MD files va build DOCX co dau."""
    # Mapping MD path -> DOCX output folder (lesson folder)
    # (relative_md_path, lesson_folder_name, output_filename)
    LESSONS = [
        # 12/06
        ("Adenomyosis_ART_2026-06-13.md", "02_Ho tro sinh san ART", None),
        ("AndroGel_ART_2026-06-13.md", "02_Ho tro sinh san ART", None),
        ("Endometriosis_2026-06-13.md", "02_Ho tro sinh san ART", None),
        ("FET_Endometriosis_2026-06-13.md", "02_Ho tro sinh san ART", None),
        ("MCMA_2026-06-13.md", "02_Ho tro sinh san ART", None),
        ("duostim_summary.md", "02_Ho tro sinh san ART", None),
        # 16-17/06
        ("02_Ho tro sinh san ART/07_OHSS/OHSS_Prevention_Management_2026-06-14.md", "02_Ho tro sinh san ART", None),
        ("02_Ho tro sinh san ART/08_Endometrial_Receptivity_ERA/Endometrial_Receptivity_ERA_2026-06-16.md", "02_Ho tro sinh san ART", None),
        ("03_Sieu am thai/09_Cervical_Length_PTB/Cervical_Length_Preterm_Birth_2026-06-17.md", "03_Sieu am thai", None),
        # 18-19/06
        ("09_Long_GnRH_Agonist/Long_GnRH_Agonist_Protocol_2026-06-18.md", "02_Ho tro sinh san ART", None),
        ("10_Fetal_Doppler/Fetal_Doppler_2026-06-19.md", "03_Sieu am thai", None),
        ("03_Sieu am thai/01_Sieu am tim thai/Sieu am tim thai - sieu chi tiet - 2026-06-19.md", "03_Sieu am thai", None),
        # 20-21/06
        ("02_Ho tro sinh san ART/10_ICSI/ICSI_2026-06-20.md", "02_Ho tro sinh san ART", None),
        ("Endometrial_Receptivity_Advanced_US_2026-06-21.md", "02_Ho tro sinh san ART", None),
        # 22/06
        ("03_Sieu am thai/11_First_Trimester_Screening/First_Trimester_Screening_2026-06-22.md", "03_Sieu am thai", None),
        ("01_San phu khoa/03_Preeclampsia_Screening/Preeclampsia_Screening_2026-06-22.md", "01_San phu khoa", None),
    ]

    converted = 0
    failed = []
    for rel_md, top_folder, _ in LESSONS:
        md_path = SRC / rel_md
        if not md_path.exists():
            print(f"  [SKIP] {rel_md}")
            failed.append(rel_md)
            continue
        # Output: same parent folder, same filename with .docx
        # Try to put in a "bài học" subfolder if exists, else just parent
        # Simpler: put output in same parent directory of MD file
        out_path = md_path.with_suffix('.docx')
        # Move to lesson folder
        # Use the actual lesson folder - look up the bai hoc folder based on topic
        lesson_dirs = {
            "Adenomyosis_ART_2026-06-13.md": ("02_Ho tro sinh san ART/02_Adenomyosis - Anh huong ART", "Adenomyosis ART - 2026-06-13.docx"),
            "AndroGel_ART_2026-06-13.md": ("02_Ho tro sinh san ART/03_AndroGel - Testosterone priming", "AndroGel (Testosterone priming) - 2026-06-13.docx"),
            "Endometriosis_2026-06-13.md": ("02_Ho tro sinh san ART/01_MCMA - Song thai 1 buong oi", "Endometriosis - 2026-06-13.docx"),
            "FET_Endometriosis_2026-06-13.md": ("02_Ho tro sinh san ART/02_FET - Frozen Embryo Transfer", "FET trong Endometriosis - 2026-06-13.docx"),
            "MCMA_2026-06-13.md": ("02_Ho tro sinh san ART/01_MCMA - Song thai 1 buong oi", "Song thai 1 buong oi - MCMA - 2026-06-13.docx"),
            "duostim_summary.md": ("02_Ho tro sinh san ART/05_DuoStim - Nang ton du", "Nang ton du ART (DuoStim) - 2026-06-13.docx"),
            "02_Ho tro sinh san ART/07_OHSS/OHSS_Prevention_Management_2026-06-14.md": ("02_Ho tro sinh san ART/07_OHSS - Prevention and Management", "OHSS - Prevention and Management - 2026-06-14.docx"),
            "02_Ho tro sinh san ART/08_Endometrial_Receptivity_ERA/Endometrial_Receptivity_ERA_2026-06-16.md": ("02_Ho tro sinh san ART/08_Endometrial_Receptivity_ERA", "Endometrial Receptivity ERA - 2026-06-16.docx"),
            "03_Sieu am thai/09_Cervical_Length_PTB/Cervical_Length_Preterm_Birth_2026-06-17.md": ("03_Sieu am thai/09_Cervical_Length_PTB", "Cervical Length Preterm Birth - 2026-06-17.docx"),
            "09_Long_GnRH_Agonist/Long_GnRH_Agonist_Protocol_2026-06-18.md": ("02_Ho tro sinh san ART/09_Long_GnRH_Agonist_Protocol", "Long GnRH Agonist Protocol - 2026-06-18.docx"),
            "10_Fetal_Doppler/Fetal_Doppler_2026-06-19.md": ("03_Sieu am thai/10_Fetal_Doppler", "Fetal Doppler thai ky - 2026-06-19.docx"),
            "03_Sieu am thai/01_Sieu am tim thai/Sieu am tim thai - sieu chi tiet - 2026-06-19.md": ("03_Sieu am thai/01_Sieu am tim thai", "Sieu am tim thai - sieu chi tiet - 2026-06-19.docx"),
            "02_Ho tro sinh san ART/10_ICSI/ICSI_2026-06-20.md": ("02_Ho tro sinh san ART/10_ICSI", "ICSI trong IVF - 2026-06-20.docx"),
            "Endometrial_Receptivity_Advanced_US_2026-06-21.md": ("02_Ho tro sinh san ART/11_Endometrial_Receptivity_Advanced_US_2026-06-21", "Endometrial Receptivity Advanced US - 2026-06-21.docx"),
            "03_Sieu am thai/11_First_Trimester_Screening/First_Trimester_Screening_2026-06-22.md": ("03_Sieu am thai/11_First_Trimester_Screening", "First Trimester Screening - 2026-06-22.docx"),
            "01_San phu khoa/03_Preeclampsia_Screening/Preeclampsia_Screening_2026-06-22.md": ("01_San phu khoa/03_Preeclampsia_Screening", "Sang loc Du phong Tien san giat - 2026-06-22.docx"),
        }

        if md_path.name not in lesson_dirs:
            # Use generic: put in top_folder
            out_path = ROOT / top_folder / (md_path.stem + ".docx")
        else:
            rel_out, filename = lesson_dirs[md_path.name]
            out_path = ROOT / rel_out / filename

        try:
            title = title_from_md(md_path)
            md_to_docx(md_path, out_path, title)
            converted += 1
        except Exception as e:
            print(f"  [ERR] {rel_md} - {e}")
            failed.append(rel_md)
    print(f"\nConverted: {converted}/{len(LESSONS)}")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
