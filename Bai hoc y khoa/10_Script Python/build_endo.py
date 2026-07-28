# -*- coding: utf-8 -*-
"""
Build 4 deliverable cho daily lesson Endometrial Receptivity.
Input: endo_content.LESSON
Output:
  - Folder lesson: .docx, .apkg, .html, telegram.txt
  - Folder source: .md, .cards.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from endo_content import LESSON  # noqa

# Paths
ROOT = Path("F:/DL/mavisresearch/Bai hoc y khoa")
LESSON_FOLDER = ROOT / "02_Ho tro sinh san ART" / LESSON["folder"]
SOURCE_FOLDER = ROOT / "09_Source - Markdown"
LESSON_FOLDER.mkdir(parents=True, exist_ok=True)
SOURCE_FOLDER.mkdir(parents=True, exist_ok=True)


def build_md_and_json():
    """Build markdown source + cards.json."""
    md_path = SOURCE_FOLDER / f"Endometrial_Receptivity_Advanced_US_{LESSON['date']}.md"
    json_path = SOURCE_FOLDER / f"Endometrial_Receptivity_Advanced_US_{LESSON['date']}.cards.json"

    lines = [f"# {LESSON['title_vi']}", "",
             f"**Ngày**: {LESSON['date']}  ",
             f"**Chuyên đề**: {LESSON['topic_focus']}  ",
             f"**Phan loai**: {LESSON['category']}",
             ""]

    # Citations block
    lines += ["## Tai lieu tham khao", ""]
    for c in LESSON["citations"]:
        if c["type"] == "guideline":
            lines.append(f"- **[{c['cite']}]** {c['title']}. *{c['journal']}* {c['year']}. "
                         f"PMID: {c['pmid']}")
        else:
            lines.append(f"- [{c['cite']}] {c['title']}. *{c['journal']}* {c['year']}. "
                         f"PMID: {c['pmid']}")
    lines += ["", "---", ""]

    # Sections
    for sec in LESSON["sections"]:
        lines.append(f"## {sec['h']}")
        lines.append("")
        lines.append(sec["body"])
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    json_path.write_text(json.dumps(LESSON["cards"], indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[OK] md: {md_path}")
    print(f"[OK] json: {json_path}")


def build_docx():
    """Build Word .docx voi formatting dep."""
    from docx import Document
    from docx.shared import Pt, RGBColor, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    doc = Document()
    # Set default font (Calibri)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    # Title
    title = doc.add_heading(LESSON["title_vi"], 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Subtitle
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f"Ngày {LESSON['date']} | {LESSON['category']}")
    run.italic = True
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    # Topic focus box
    p = doc.add_paragraph()
    p.add_run("Trọng tâm: ").bold = True
    p.add_run(LESSON["topic_focus"])

    # Citation table
    doc.add_heading("Bảng tóm tắt tài liệu", 1)
    table = doc.add_table(rows=1, cols=4)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    hdr[0].text = "Cite"
    hdr[1].text = "Type"
    hdr[2].text = "Journal / Year"
    hdr[3].text = "PMID"
    for c in LESSON["citations"]:
        row = table.add_row().cells
        row[0].text = c["cite"]
        row[1].text = c["type"]
        row[2].text = f"{c['journal']} {c['year']}"
        row[3].text = c.get("pmid", "—")

    # Sections
    for sec in LESSON["sections"]:
        doc.add_heading(sec["h"], 1)
        # Body - parse markdown light
        for para in sec["body"].split("\n\n"):
            para = para.strip()
            if not para:
                continue
            if para.startswith("|"):
                # Markdown table - convert to docx table
                rows = [r.strip().strip("|").split("|") for r in para.split("\n") if "|" in r]
                rows = [[c.strip() for c in r] for r in rows if any(c.strip() for c in r)]
                if len(rows) >= 2 and all(set(r) <= {"-", ""} for r in rows[1]):
                    rows = [rows[0]] + rows[2:]
                if rows:
                    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
                    t.style = "Light Grid Accent 1"
                    for i, r in enumerate(rows):
                        for j, c in enumerate(r):
                            cell = t.rows[i].cells[j]
                            cell.text = c
                            if i == 0:
                                for run in cell.paragraphs[0].runs:
                                    run.bold = True
            elif para.startswith(">"):
                # Blockquote
                p = doc.add_paragraph()
                run = p.add_run(para.lstrip(">").strip())
                run.italic = True
                run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
            elif para.startswith("- "):
                for item in para.split("\n"):
                    doc.add_paragraph(item.lstrip("- ").strip(), style="List Bullet")
            elif "**" in para:
                # Bold + plain
                p = doc.add_paragraph()
                parts = para.split("**")
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        p.add_run(part)
                    else:
                        p.add_run(part).bold = True
            else:
                doc.add_paragraph(para)

    docx_path = LESSON_FOLDER / f"Endometrial_Receptivity_Advanced_US_{LESSON['date']}.docx"
    doc.save(docx_path)
    print(f"[OK] docx: {docx_path}")


def build_apkg():
    """Build Anki deck .apkg voi Pastel theme."""
    import genanki
    import random

    # Stable IDs
    MODEL_ID = 1607392319
    DECK_ID = 2059400110

    model = genanki.Model(
        MODEL_ID,
        "Endometrial Receptivity Card",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Card",
                "qfmt": "<div style='font-family: Calibri; font-size: 18px; color: #5D5C8C;'>{{Question}}</div>",
                "afmt": (
                    "{{FrontSide}}<hr id=answer>"
                    "<div style='font-family: Calibri; font-size: 16px; color: #444; "
                    "background: #FFF8E7; padding: 12px; border-radius: 8px; "
                    "border-left: 4px solid #FFB6B9;'>{{Answer}}</div>"
                ),
            }
        ],
        css=(
            ".card { font-family: Calibri; background: #FAF7F2; } "
            ".card { color: #2D2D2D; }"
        ),
    )

    deck = genanki.Deck(DECK_ID, f"Endometrial Receptivity :: {LESSON['date']}")
    for card in LESSON["cards"]:
        note = genanki.Note(
            model=model,
            fields=[card["q"], card["a"]],
        )
        deck.add_note(note)

    apkg_path = LESSON_FOLDER / f"Anki - Endometrial Receptivity {len(LESSON['cards'])} cards - {LESSON['date']}.apkg"
    genanki.Package(deck).write_to_file(str(apkg_path))
    print(f"[OK] apkg: {apkg_path} ({len(LESSON['cards'])} cards)")


def build_html():
    """Build visual summary HTML voi Tailwind + Mermaid + Chart.js."""
    html_path = LESSON_FOLDER / f"Visual summary - Endometrial Receptivity - {LESSON['date']}.html"

    mermaid = LESSON["html_elements"]["mermaid_flowchart"]
    chart = LESSON["html_elements"]["comparison_chart"]

    # Build citations HTML
    cit_html = []
    for c in LESSON["citations"]:
        if c["type"] == "guideline":
            cit_html.append(
                f'<div class="bg-green-50 border-l-4 border-green-500 p-3 rounded mb-2">'
                f'<div class="font-bold text-green-900">[GUIDELINE] {c["cite"]}</div>'
                f'<div class="text-sm text-gray-700">{c["title"]}</div>'
                f'<div class="text-xs text-gray-500">{c["journal"]} {c["year"]} | PMID: '
                f'<a href="https://pubmed.ncbi.nlm.nih.gov/{c["pmid"]}/" class="text-blue-600 underline">{c["pmid"]}</a>'
                f'</div></div>'
            )
        else:
            cit_html.append(
                f'<div class="bg-gray-50 border-l-4 border-gray-300 p-3 rounded mb-2">'
                f'<div class="font-bold text-gray-900">{c["cite"]} '
                f'<span class="text-xs bg-gray-200 px-2 py-0.5 rounded">Tier {c["tier"]}</span></div>'
                f'<div class="text-sm text-gray-700">{c["title"]}</div>'
                f'<div class="text-xs text-gray-500">{c["journal"]} {c["year"]} | PMID: '
                f'<a href="https://pubmed.ncbi.nlm.nih.gov/{c["pmid"]}/" class="text-blue-600 underline">{c["pmid"]}</a>'
                f'</div></div>'
            )
    citations_html = "\n".join(cit_html)

    # Build sections HTML (skip references - already in citations)
    sec_html = []
    for sec in LESSON["sections"][:-1]:  # skip "Tai lieu tham khao"
        # Light markdown parsing
        body = sec["body"]
        body_html = body
        # bold
        import re
        body_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", body_html)
        # blockquote
        body_html = re.sub(r"^&gt;\s*(.+)$", r"<blockquote class='border-l-4 border-amber-400 bg-amber-50 p-3 my-2 italic text-gray-700'>\1</blockquote>", body_html, flags=re.MULTILINE)
        # tables - rough
        if "|" in body_html and "\n|" in body_html:
            table_match = re.search(r"((?:\|.+\n)+)", body_html)
            if table_match:
                tbl_text = table_match.group(1).strip()
                tbl_rows = [r.strip().strip("|").split("|") for r in tbl_text.split("\n") if r.strip()]
                tbl_rows = [[c.strip() for c in r] for r in tbl_rows]
                # Filter separator
                tbl_rows = [r for r in tbl_rows if not all(set(c) <= {"-", ""} for c in r)]
                if tbl_rows:
                    thead = "".join(f"<th class='border px-2 py-1 bg-gray-100'>{c}</th>" for c in tbl_rows[0])
                    tbody = ""
                    for r in tbl_rows[1:]:
                        tbody += "<tr>" + "".join(f"<td class='border px-2 py-1'>{c}</td>" for c in r) + "</tr>"
                    html_table = f"<table class='border-collapse border w-full my-3 text-sm'><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>"
                    body_html = body_html.replace(table_match.group(1), html_table)
        # line breaks
        body_html = body_html.replace("\n\n", "</p><p>")
        sec_html.append(
            f'<section class="mb-6">'
            f'<h2 class="text-2xl font-bold text-indigo-900 mb-3 border-b-2 border-indigo-200 pb-1">'
            f'{sec["h"]}</h2>'
            f'<div class="text-gray-800 leading-relaxed"><p>{body_html}</p></div>'
            f'</section>'
        )
    sections_html = "\n".join(sec_html)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{LESSON['title_vi']} - Visual Summary {LESSON['date']}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4/dist/chart.umd.min.js"></script>
<style>
body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #FAF7F2; }}
.hero {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
</style>
</head>
<body class="max-w-5xl mx-auto p-6">

<header class="hero text-white rounded-lg p-8 mb-8 shadow-lg">
    <div class="text-sm uppercase tracking-wider opacity-80">{LESSON['category']} | {LESSON['date']}</div>
    <h1 class="text-4xl font-bold mt-2 mb-3">{LESSON['title_vi']}</h1>
    <p class="text-lg opacity-90">{LESSON['topic_focus']}</p>
    <div class="mt-4 flex gap-2 flex-wrap">
        <span class="bg-white/20 px-3 py-1 rounded-full text-sm">ESHRE 2023 RIF Guideline</span>
        <span class="bg-white/20 px-3 py-1 rounded-full text-sm">3 meta-analyses 2023</span>
        <span class="bg-white/20 px-3 py-1 rounded-full text-sm">13 citations verified</span>
    </div>
</header>

<div class="grid md:grid-cols-2 gap-6 mb-8">
    <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-bold text-indigo-900 mb-3">Key Numbers</h3>
        <ul class="space-y-2 text-sm">
            <li><strong>Displaced WOI trong RIF:</strong> 34% (95% CI 24-43%)</li>
            <li><strong>Arian 2023 OR (LBR):</strong> 1.38 (95% CI 0.79-2.41) - NS</li>
            <li><strong>p-ET vs sET trong RIF:</strong> 40.7% vs 49.6%, OR 0.94</li>
            <li><strong>EMT &lt;7mm pregnancy OR:</strong> 0.61 (95% CI 0.52-0.70)</li>
            <li><strong>EMT 3D volume ROC AUC:</strong> 0.48 (95% CI 0.38-0.58)</li>
        </ul>
    </div>
    <div class="bg-white rounded-lg shadow p-6">
        <h3 class="text-lg font-bold text-indigo-900 mb-3">ESHRE 2023 RIF Color Code</h3>
        <div class="space-y-2 text-sm">
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-green-500"></span><strong>GREEN:</strong> TVUS 3D, karyotype, APS</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-amber-500"></span><strong>ORANGE:</strong> ERA, NK cells, microbiome</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-red-500"></span><strong>RED:</strong> IVIG, corticosteroids, scratching</div>
        </div>
    </div>
</div>

<section class="bg-white rounded-lg shadow p-6 mb-6">
    <h3 class="text-xl font-bold text-indigo-900 mb-4">Algorithm: Endometrial Assessment</h3>
    <div class="mermaid">{mermaid}</div>
</section>

<section class="bg-white rounded-lg shadow p-6 mb-6">
    <h3 class="text-xl font-bold text-indigo-900 mb-4">So sanh: EMT thap vs cao (OR cho pregnancy)</h3>
    <canvas id="emtChart" height="200"></canvas>
    <p class="text-xs text-gray-500 mt-2">Nguon: Gao 2020 meta-analysis (PMID 31786047), 30 study, 88,056 cycles. OR&lt;1 = lower EMT xau hon.</p>
</section>

<div class="bg-white rounded-lg shadow p-6 mb-6">
    <h3 class="text-xl font-bold text-indigo-900 mb-4">Noi dung chi tiet</h3>
    {sections_html}
</div>

<section class="bg-white rounded-lg shadow p-6 mb-6">
    <h3 class="text-xl font-bold text-indigo-900 mb-4">Tai lieu tham khao</h3>
    {citations_html}
</section>

<footer class="text-center text-gray-500 text-sm mt-8">
    Bai hoc duoc tao boi MiniMax Mavis cho BS Ngoc. So lieu da verify abstract trong file citations.
</footer>

<script>
mermaid.initialize({{ startOnLoad: true, theme: 'default' }});

new Chart(document.getElementById('emtChart'), {{
    type: 'bar',
    data: {{
        labels: {json.dumps(chart["labels"])},
        datasets: [{{
            label: 'OR (95% CI)',
            data: {json.dumps(chart["values"])},
            backgroundColor: 'rgba(102, 126, 234, 0.7)',
            borderColor: 'rgba(102, 126, 234, 1)',
            borderWidth: 1
        }}]
    }},
    options: {{
        responsive: true,
        scales: {{
            y: {{
                beginAtZero: true,
                max: 1.0,
                title: {{ display: true, text: 'Odds Ratio (<1 means lower EMT worse)' }}
            }}
        }},
        plugins: {{
            tooltip: {{
                callbacks: {{
                    label: function(ctx) {{
                        const labels = {json.dumps([f"{l} (CI {lo}-{hi})" for l, lo, hi in zip(chart["labels"], chart["ci_low"], chart["ci_high"])])};
                        return labels[ctx.dataIndex];
                    }}
                }}
            }}
        }}
    }}
}});
</script>

</body>
</html>
"""
    html_path.write_text(html, encoding="utf-8")
    print(f"[OK] html: {html_path}")


def build_telegram():
    """Build telegram message text file."""
    tg_path = LESSON_FOLDER / f"Telegram - Endometrial Receptivity - {LESSON['date']}.txt"
    tg_path.write_text(LESSON["telegram"], encoding="utf-8")
    print(f"[OK] telegram: {tg_path}")


if __name__ == "__main__":
    print(f"=== Building lesson: {LESSON['title']} ===")
    build_md_and_json()
    build_docx()
    build_apkg()
    build_html()
    build_telegram()
    print("\n=== DONE ===")
