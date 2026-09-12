"""Convert Markdown file (Vietnamese co dau) -> DOCX.

Parser:
- # / ## / ### -> Heading 1/2/3
- **text** -> bold
- *text* -> italic
- `code` -> monospace
- - item -> bullet
- 1. item -> numbered
- |col|col| -> table
- ``` code block -> dedicated callout/code box (Consolas, light gray background, subtle border)
- paragraph -> normal text
- LaTeX-style math tokens -> clean Unicode converter

Note: giu nguyen tieng Viet co dau (UTF-8 doc duoc).
"""
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_cell_bg(cell, color_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def set_cell_border(cell, color_hex='000000', sz='4'):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), sz)
        border.set(qn('w:color'), color_hex)
        tc_borders.append(border)
    tc_pr.append(tc_borders)


def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tc_mar.append(node)
    tc_pr.append(tc_mar)


def clean_math(text):
    """Clean LaTeX math expressions and backslashes into clean Unicode/text."""
    if not text:
        return text

    # Handle corrupted escaped tokens caused by python string parsing (\t -> tab, \n -> newline, etc.)
    text = text.replace('\t', ' ').replace('\r', ' ')
    text = re.sub(r'[\t\r]+', ' ', text)
    text = text.replace(r'\nightarrow', r'\rightarrow')
    text = text.replace(r'	ext{', r'\text{')
    text = text.replace(r'	ext', '')
    
    # Fix corrupted Greek letters / biological terms
    text = text.replace('TNF- pha', 'TNF-α').replace('TNF-pha', 'TNF-α').replace('TNF-lpha', 'TNF-α').replace('TNF-alpha', 'TNF-α')
    text = text.replace('PPAR-lpha', 'PPAR-α').replace('PPAR-alpha', 'PPAR-α')
    text = text.replace('ightarrow', '→')

    # Unnest all \text{...} and ext{...}
    for _ in range(5):
        text = re.sub(r'\\text\{([^}]*)\}', r'\1', text)
        text = re.sub(r'ext\{([^}]*)\}', r'\1', text)
    
    text = text.replace(r'\text{', '').replace('ext{', '')
    text = text.replace(r'\text', '')

    # Standard LaTeX math commands
    text = re.sub(r'\\(ge|geq)\b', '≥', text)
    text = re.sub(r'\\(le|leq)\b', '≤', text)
    text = re.sub(r'\\(rightarrow|to)\b', '→', text)
    text = re.sub(r'\\times\b', '×', text)
    text = re.sub(r'\\pm\b', '±', text)
    text = re.sub(r'\\sim\b', '~', text)
    text = re.sub(r'\\approx\b', '≈', text)
    text = re.sub(r'\\alpha\b', 'α', text)
    text = re.sub(r'\\beta\b', 'β', text)
    text = re.sub(r'\\gamma\b', 'γ', text)

    # Subscripts/superscripts & ions
    text = text.replace('Fe^2+', 'Fe²⁺').replace('Ca^2+', 'Ca²⁺')
    text = text.replace('m^2', 'm²')
    text = re.sub(r'_\{([^}]*)\}', r'_\1', text)
    text = re.sub(r'\^\{([^}]*)\}', r'^\1', text)

    # Common notations
    text = text.replace(r'\%', '%')
    text = text.replace(r'\\', '')

    # Strip dollar signs $...$
    def unwrap_dollar(m):
        inner = m.group(1).strip()
        for _ in range(3):
            inner = re.sub(r'ext\{([^}]*)\}', r'\1', inner)
            inner = re.sub(r'\\text\{([^}]*)\}', r'\1', inner)
        return re.sub(r'\s+', ' ', inner)

    text = re.sub(r'\$([^$]+)\$', unwrap_dollar, text)
    text = text.replace('$', '')
    text = text.replace('LDL -C', 'LDL-C').replace('Non -HDL', 'Non-HDL').replace('HDL -C', 'HDL-C')
    text = re.sub(r' {2,}', ' ', text)
    return text

def style_header_cell(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.size = Pt(10.5)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell, '1E4060', '4')
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)


def style_first_col_cell(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
    set_cell_bg(cell, 'E8F0F7')
    set_cell_border(cell, 'D0D0D0', '4')
    set_cell_margins(cell, top=80, bottom=80, left=120, right=120)


def parse_inline(text):
    """Parse **bold**, *italic*, `code` trong text sau khi da clean math."""
    text = clean_math(text)
    text = text.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    parts = []
    pattern = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)')
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            parts.append((text[pos:m.start()], False, False, False))
        token = m.group()
        if token.startswith('**'):
            parts.append((token[2:-2], True, False, False))
        elif token.startswith('*'):
            parts.append((token[1:-1], False, True, False))
        elif token.startswith('`'):
            parts.append((token[1:-1], False, False, True))
        pos = m.end()
    if pos < len(text):
        parts.append((text[pos:], False, False, False))
    return parts


def add_inline_paragraph(doc, text, style=None, bold=False, italic=False):
    """Add a paragraph with inline formatting (** * `)."""
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    for txt, b, i, c in parse_inline(text):
        if not txt:
            continue
        run = p.add_run(txt)
        if b:
            run.bold = True
        if i:
            run.italic = True
        if c:
            run.font.name = 'Consolas'
    return p


def add_code_block(doc, code_lines):
    """Add dedicated callout/code box for code blocks and ASCII diagrams."""
    if not code_lines:
        return
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    table.autofit = False

    cell = table.cell(0, 0)
    set_cell_bg(cell, 'F4F4F4')
    set_cell_border(cell, color_hex='CCCCCC', sz='4')
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)

    max_len = max(len(l) for l in code_lines) if code_lines else 0
    if max_len > 120:
        font_size = 7.5
    elif max_len > 100:
        font_size = 8.5
    else:
        font_size = 9.5

    for idx, line in enumerate(code_lines):
        p = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        run = p.add_run(line if line else ' ')
        run.font.name = 'Consolas'
        run.font.size = Pt(font_size)
        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)


def is_table_row(line):
    """Check if line is a markdown table row: |...|..."""
    stripped = line.strip()
    return stripped.startswith('|') and stripped.endswith('|') and stripped.count('|') >= 2


def is_table_separator(line):
    """Check if line is a markdown table separator: |---|..."""
    stripped = line.strip()
    return bool(re.match(r'^\|[\s\-:|]+\|$', stripped))


def parse_table_row(line):
    """Parse a table row into cells."""
    stripped = line.strip()
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    cells = re.split(r'(?<!\\)\|', stripped)
    return [c.strip() for c in cells]


def add_table(doc, lines, start_idx):
    """Add a table starting at lines[start_idx]. Returns the next index after the table."""
    if start_idx >= len(lines) or not is_table_row(lines[start_idx]):
        return start_idx
    header = parse_table_row(lines[start_idx])
    if start_idx + 1 >= len(lines) or not is_table_separator(lines[start_idx + 1]):
        add_inline_paragraph(doc, lines[start_idx])
        return start_idx + 1

    rows = []
    idx = start_idx + 2
    while idx < len(lines) and is_table_row(lines[idx]):
        rows.append(parse_table_row(lines[idx]))
        idx += 1

    if not header:
        return idx

    table = doc.add_table(rows=len(rows) + 1, cols=len(header))
    table.style = 'Light Grid Accent 1'

    # Header
    for c, h in enumerate(header):
        cell = table.rows[0].cells[c]
        p = cell.paragraphs[0]
        p.text = ''
        for txt, b, i, m in parse_inline(h):
            if not txt:
                continue
            run = p.add_run(txt)
            run.bold = True
            run.font.size = Pt(10.5)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            if m:
                run.font.name = 'Consolas'
        set_cell_bg(cell, '2D5F8C')
        set_cell_border(cell, '1E4060', '4')
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)

    # Data rows
    for r, row_data in enumerate(rows, start=1):
        for c, value in enumerate(row_data):
            if c < len(table.rows[r].cells):
                cell = table.rows[r].cells[c]
                p = cell.paragraphs[0]
                p.text = ''
                for txt, b, i, m in parse_inline(value):
                    if not txt:
                        continue
                    run = p.add_run(txt)
                    if b:
                        run.bold = True
                    if i:
                        run.italic = True
                    if m:
                        run.font.name = 'Consolas'
                set_cell_border(cell, 'D0D0D0', '4')
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                if c == 0:
                    style_first_col_cell(cell)
    return idx


def md_to_docx(md_path, docx_path, title=None):
    """Convert .md to .docx. Vietnamese diacritics preserved (UTF-8)."""
    md_path = Path(md_path)
    docx_path = Path(docx_path)
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')

    doc = Document()
    for sec in doc.sections:
        sec.top_margin = Cm(2)
        sec.bottom_margin = Cm(2)
        sec.left_margin = Cm(1.8)
        sec.right_margin = Cm(1.8)

    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    # Title
    if title:
        t = doc.add_heading(clean_math(title), 0)
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        first_heading = next((l for l in lines if l.startswith('# ')), None)
        if first_heading:
            t = doc.add_heading(clean_math(first_heading[2:].strip()), 0)
            t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph(f'Bai hoc y khoa - {md_path.stem}')

    in_code_block = False
    code_buffer = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code block
        if stripped.startswith('```'):
            if in_code_block:
                add_code_block(doc, code_buffer)
                code_buffer = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue
        if in_code_block:
            code_buffer.append(line)
            i += 1
            continue

        # Empty line
        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped):
            doc.add_paragraph()
            i += 1
            continue

        # Table
        if is_table_row(line):
            i = add_table(doc, lines, i)
            continue

        # Headings
        if line.startswith('# '):
            doc.add_heading(clean_math(line[2:].strip()), 0)
            i += 1
            continue
        if line.startswith('## '):
            doc.add_heading(clean_math(line[3:].strip()), 1)
            i += 1
            continue
        if line.startswith('### '):
            doc.add_heading(clean_math(line[4:].strip()), 2)
            i += 1
            continue
        if line.startswith('#### '):
            doc.add_heading(clean_math(line[5:].strip()), 3)
            i += 1
            continue

        # Bullet list
        if stripped.startswith('- ') or stripped.startswith('* '):
            text_content = stripped[2:]
            p = doc.add_paragraph(style='List Bullet')
            for txt, b, i_ital, c in parse_inline(text_content):
                if not txt:
                    continue
                run = p.add_run(txt)
                if b:
                    run.bold = True
                if i_ital:
                    run.italic = True
                if c:
                    run.font.name = 'Consolas'
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', stripped):
            text_content = re.sub(r'^\d+\.\s+', '', stripped)
            p = doc.add_paragraph(style='List Number')
            for txt, b, i_ital, c in parse_inline(text_content):
                if not txt:
                    continue
                run = p.add_run(txt)
                if b:
                    run.bold = True
                if i_ital:
                    run.italic = True
                if c:
                    run.font.name = 'Consolas'
            i += 1
            continue

        # Block quote
        if stripped.startswith('> '):
            text_content = stripped[2:]
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1)
            for txt, b, i_ital, c in parse_inline(text_content):
                if not txt:
                    continue
                run = p.add_run(txt)
                run.italic = True
                if b:
                    run.bold = True
                if c:
                    run.font.name = 'Consolas'
            i += 1
            continue

        # Regular paragraph
        add_inline_paragraph(doc, line)
        i += 1

    doc.save(str(docx_path))
    print(f"  [DOCX] Saved: {docx_path}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python md_to_docx.py <input.md> [output.docx] [title]")
        sys.exit(1)
    md = sys.argv[1]
    docx = sys.argv[2] if len(sys.argv) > 2 else str(Path(md).with_suffix('.docx'))
    title = sys.argv[3] if len(sys.argv) > 3 else None
    md_to_docx(md, docx, title)
