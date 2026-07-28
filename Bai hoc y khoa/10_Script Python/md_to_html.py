"""md_to_html.py — Auto-convert medical MD lesson to Tailwind HTML visual summary.

Usage:
    python md_to_html.py <input.md> [output.html] [specialty] [date]

Converts:
  - # H1 → HTML title
  - ## Section headings → glass-rounded Tailwind sections
  - ### Sub-headings → sub-sections
  - Markdown tables → Tailwind-styled HTML tables
  - Bold/italic/code → HTML
  - Bullet/numbered lists → HTML lists
  - > blockquotes → highlight boxes
  - ```mermaid → Mermaid diagrams
  - Horizontal rules

Output: Full Tailwind + Mermaid + Chart.js HTML via lesson_builder.
"""
from pathlib import Path
import re
import sys


def _parse_meta(lines):
    """Extract (title, specialty, date) from MD header lines."""
    title, specialty, date = '', '', ''
    for line in lines[:30]:
        s = line.strip()
        if s.startswith('# ') and 'bài học' in s.lower():
            title = s[2:].strip()
        elif 'Chuyên khoa' in s:
            m = re.search(r'\*\*(.+?)\*\*', s)
            if m: specialty = m.group(1)
        elif 'Ngày' in s:
            m = re.search(r'(\d{4}-\d{2}-\d{2})', s)
            if m: date = m.group(1)
            if not date:  # try Ngay: 2026-06-27
                m2 = re.search(r'(\d{2}/\d{2}/\d{4})', s)
                if m2: date = m2.group(1)
    return title, specialty, date


def _fm(line):
    """Inline format: bold, italic, code."""
    line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', line)
    line = re.sub(r'`([^`]+)`', r'<code class="bg-stone-200 px-1 rounded">\1</code>', line)
    return line


def _blockquote(lines, i):
    """Parse > lines into callout box. Returns (html, next_i)."""
    parts = []
    while i < len(lines):
        s = lines[i]
        if s.startswith('> '):
            parts.append(s[2:])
        elif s.startswith('>'):
            parts.append(s[1:])
        else:
            break
        i += 1
    content = '<br>'.join(_fm(p.strip()) for p in parts if p.strip())
    html = f'<div class="p-4 my-4 border-l-4 border-blue-500 bg-blue-50 rounded-r-lg text-stone-700">{content}</div>'
    return html, i


def _table(lines, i):
    """Parse MD table. Returns (html, next_i)."""
    # header
    hdr = [c.strip() for c in lines[i].split('|')[1:-1]]
    i += 1
    # separator
    if i < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i]):
        i += 1
    # rows
    rows = []
    while i < len(lines) and lines[i].strip().startswith('|'):
        cells = [c.strip() for c in lines[i].split('|')[1:-1]]
        rows.append(cells)
        i += 1

    h = '<div class="overflow-x-auto my-4"><table class="w-full text-left border-collapse text-sm">'
    h += '<thead><tr class="bg-blue-100">'
    for c in hdr:
        h += f'<th class="p-2 border whitespace-nowrap">{_fm(c)}</th>'
    h += '</tr></thead><tbody>'
    for row in rows:
        green = 'bg-green-50' if any('bình' in r.lower() or 'normal' in r.lower() for r in row) else ''
        h += f'<tr class="{green}">'
        for c in row:
            h += f'<td class="p-2 border">{_fm(c)}</td>'
        h += '</tr>'
    h += '</tbody></table></div>'
    return h, i


def _list_block(lines, i):
    """Parse bullet or numbered list. Returns (html, next_i)."""
    items = []
    ordered = None
    while i < len(lines):
        s = lines[i]
        if not s.strip():
            i += 1
            continue
        m_num = re.match(r'^(\d+)\.\s+', s)
        m_bul = re.match(r'^[-*]\s+', s)
        if m_num:
            if ordered is None: ordered = True
            items.append((_fm(s[m_num.end():].strip()), m_num.group(1)))
            i += 1
        elif m_bul:
            if ordered is None: ordered = False
            items.append((_fm(s[m_bul.end():].strip()), None))
            i += 1
        else:
            break

    tag = 'ol' if ordered else 'ul'
    cls = 'list-decimal list-inside space-y-1 mb-4' if ordered else 'list-disc list-inside space-y-1 mb-4'
    items_html = '\n'.join(f'<li>{txt}</li>' for txt, _ in items)
    return f'<{tag} class="{cls}">{items_html}</{tag}>', i


def _fence(lines, i):
    """Parse ```...``` block. Returns (html, next_i)."""
    lang = lines[i].strip()[3:].strip()
    i += 1
    parts = []
    while i < len(lines):
        if lines[i].strip().startswith('```'):
            i += 1
            break
        parts.append(lines[i])
        i += 1
    code = '\n'.join(parts)
    if lang == 'mermaid':
        return f'<div class="mermaid text-center my-6">{code}</div>', i
    return f'<pre class="bg-stone-100 p-4 rounded-lg overflow-x-auto my-4 text-sm"><code>{code}</code></pre>', i


def _render_section(title, body_lines):
    """Convert a section (title + body lines) to HTML."""
    h = f'<section class="glass rounded-2xl p-8 shadow-md mb-8">\n'
    h += f'<h2 class="text-3xl font-bold text-blue-700 mb-6">{title}</h2>\n'

    i = 0
    while i < len(body_lines):
        s = body_lines[i]
        raw = body_lines[i]

        # empty
        if not s.strip():
            i += 1
            continue

        # fenced block
        if s.startswith('```'):
            block, i = _fence(body_lines, i)
            h += block + '\n'
            continue

        # sub-heading
        if s.startswith('### ') or s.startswith('#### '):
            level = 3 if s.startswith('### ') else 4
            txt = _fm(s[s.index(' ') + 1:])
            color = 'text-purple-700 text-xl' if level == 3 else 'text-stone-700 text-lg'
            h += f'<h{level} class="font-bold {color} mt-6 mb-3">{txt}</h{level}>\n'
            i += 1
            continue

        # blockquote
        if raw.startswith('>'):
            block, i = _blockquote(body_lines, i)
            h += block + '\n'
            continue

        # table
        if s.startswith('|') and i + 1 < len(body_lines) and re.match(r'^\|[\s\-:|]+\|$', body_lines[i + 1].strip()):
            block, i = _table(body_lines, i)
            h += block + '\n'
            continue

        # list
        if re.match(r'^(\d+\.|[-*])\s', s):
            block, i = _list_block(body_lines, i)
            h += block + '\n'
            continue

        # horizontal rule
        if s == '---':
            h += '<hr class="my-6 border-stone-300">\n'
            i += 1
            continue

        # paragraph (skip TOC/metadata lines)
        if s.startswith('> ') or s.startswith('**Citation'): 
            i += 1
            continue

        h += f'<p class="text-stone-700 mb-3">{_fm(s)}</p>\n'
        i += 1

    h += '</section>\n'
    return h


def md_to_html(md_path, output_path, specialty=None, date=None):
    """Full pipeline."""
    lines = Path(md_path).read_text(encoding='utf-8').splitlines()
    title, meta_spec, meta_date = _parse_meta(lines)
    specialty = specialty or meta_spec or 'Y khoa'
    date = date or meta_date or ''

    # Split into sections by ## headings
    sections = []  # list of (title, body_lines)
    current_title = None
    current_body = []
    in_toc = False
    in_refs = False

    for line in lines:
        s = line.strip()

        # Detect TOC start
        if s.startswith('## MỤC') or s == '## MỤC LỤC':
            in_toc = True
            continue

        # Detect TOC end (next ## heading)
        if in_toc and s.startswith('## ') and not s.startswith('## MỤC'):
            in_toc = False
            current_body = []

        if in_toc:
            continue

        # Detect references section
        if s.startswith('## 9. TÀI LIỆU') or s.startswith('## 8. TÀI LIỆU') or s.startswith('# TÀI LIỆU'):
            in_refs = True
            continue
        if in_refs and s.startswith('## '):
            # references ended at next ## (edge case, shouldn't happen)
            pass
        if in_refs:
            continue

        # Section boundary
        if s.startswith('## '):
            if current_title and current_body:
                sections.append((current_title, current_body))
            current_title = s[3:].strip()
            current_body = []
            continue

        # Skip H1 title line in body
        if s.startswith('# ') and not s.startswith('## '):
            continue

        # Skip meta lines
        if s.startswith('**Ngày:') or s.startswith('> ') and 'Tier 0' in s:
            current_body.append(line)
            continue

        if current_title is not None:
            current_body.append(line)

    # Last section
    if current_title and current_body:
        sections.append((current_title, current_body))

    # Import lesson_builder
    script_dir = Path(__file__).parent
    sys.path.insert(0, str(script_dir))
    from lesson_builder import build_lesson_html, write_html

    # Build header
    header = f'''<header class="text-center py-12 mb-12 glass rounded-3xl shadow-lg">
  <div class="inline-block px-4 py-1 mb-4 rounded-full bg-blue-200 text-blue-800 text-sm font-semibold">
    Chuyên khoa: {specialty}
  </div>
  <h1 class="text-4xl md:text-5xl font-bold mb-4 text-stone-800">{title}</h1>
  <p class="text-stone-600 text-lg">Ngày {date} | Cho bác sĩ sản phụ khoa / học viên sau đại học</p>
  <p class="text-sm text-stone-500 mt-2">Bác sĩ: <strong>Ngọc 🍅 🐈‍⬛</strong> | AI: <strong>MiniMax Mavis</strong></p>
</header>'''

    # Render sections
    main_parts = []
    for sec_title, sec_body in sections:
        main_parts.append(_render_section(sec_title, sec_body))
    main_html = '\n'.join(main_parts)

    footer = f'Bác sĩ: Ngọc 🍅 🐈‍⬛ | AI: MiniMax Mavis | {date}'

    html = build_lesson_html(
        title=title or 'Bài học y khoa',
        header_html=header,
        main_html=main_html,
        footer_text=footer,
        custom_charts='',
    )

    write_html(html, output_path)
    section_count = len(sections)
    html_size = len(html)
    print(f'  [HTML] Auto-generated: {output_path}')
    print(f'  Title: OK | Sections: {section_count} | HTML: {html_size:,} bytes')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input.md> [output.html] [specialty] [date]")
        sys.exit(1)

    md_file = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else str(Path(md_file).with_suffix('.html'))
    spec = sys.argv[3] if len(sys.argv) > 3 else None
    d = sys.argv[4] if len(sys.argv) > 4 else None

    md_to_html(md_file, output, spec, d)
