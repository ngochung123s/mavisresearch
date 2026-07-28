"""Convert Markdown file (Vietnamese co dau) -> DOCX.

Parser don gian:
- # / ## / ### -> Heading 1/2/3
- **text** -> bold
- *text* -> italic
- `code` -> monospace
- - item -> bullet
- 1. item -> numbered
- |col|col| -> table
- ``` code block -> skip (preserve as monospace)
- paragraph -> normal text

Note: giu nguyen tieng Viet co dau (UTF-8 doc duoc).
"""
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_cell_bg(cell, color_hex):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def set_cell_border(cell):
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:color'), '000000')
        tc_borders.append(border)
    tc_pr.append(tc_borders)


def style_header_cell(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)


def style_first_col_cell(cell):
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
    set_cell_bg(cell, 'E8F0F7')
    set_cell_border(cell)


def parse_inline(text):
    """Parse **bold**, *italic*, `code` trong text. Tra ve list (text, bold, italic, code) tuples."""
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


def add_simple_paragraph(doc, text):
    """Add paragraph with no inline parsing (e.g., for code blocks)."""
    return doc.add_paragraph(text)


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
    # Remove leading/trailing |
    if stripped.startswith('|'):
        stripped = stripped[1:]
    if stripped.endswith('|'):
        stripped = stripped[:-1]
    # Split by | (but not escaped \|)
    cells = re.split(r'(?<!\\)\|', stripped)
    return [c.strip() for c in cells]


def add_table(doc, lines, start_idx):
    """Add a table starting at lines[start_idx]. Returns the next index after the table."""
    # First row is header
    if start_idx >= len(lines) or not is_table_row(lines[start_idx]):
        return start_idx
    header = parse_table_row(lines[start_idx])
    # Check next line is separator
    if start_idx + 1 >= len(lines) or not is_table_separator(lines[start_idx + 1]):
        # Not a table, just a regular row
        add_simple_paragraph(doc, lines[start_idx])
        return start_idx + 1
    # Collect data rows
    rows = []
    idx = start_idx + 2
    while idx < len(lines) and is_table_row(lines[idx]):
        rows.append(parse_table_row(lines[idx]))
        idx += 1
    # Create table
    if not header:
        return idx
    table = doc.add_table(rows=len(rows) + 1, cols=len(header))
    table.style = 'Light Grid Accent 1'
    # Header
    for c, h in enumerate(header):
        cell = table.rows[0].cells[c]
        cell.text = h
        style_header_cell(cell)
    # Data rows
    for r, row_data in enumerate(rows, start=1):
        for c, value in enumerate(row_data):
            if c < len(table.rows[r].cells):
                cell = table.rows[r].cells[c]
                # Parse inline formatting
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
                set_cell_border(cell)
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
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)

    # Title
    if title:
        t = doc.add_heading(title, 0)
        t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        # Extract from first # heading
        first_heading = next((l for l in lines if l.startswith('# ')), None)
        if first_heading:
            t = doc.add_heading(first_heading[2:].strip(), 0)
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
                # End of code block
                if code_buffer:
                    p = doc.add_paragraph()
                    run = p.add_run('\n'.join(code_buffer))
                    run.font.name = 'Consolas'
                    run.font.size = Pt(9)
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
            doc.add_heading(line[2:].strip(), 0)
            i += 1
            continue
        if line.startswith('## '):
            doc.add_heading(line[3:].strip(), 1)
            i += 1
            continue
        if line.startswith('### '):
            doc.add_heading(line[4:].strip(), 2)
            i += 1
            continue
        if line.startswith('#### '):
            doc.add_heading(line[5:].strip(), 3)
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

        # Regular paragraph (with inline formatting)
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
