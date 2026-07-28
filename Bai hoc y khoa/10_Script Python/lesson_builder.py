"""Shared utilities cho build medical lesson (docx + anki + html).

Tách ra từ make_long_lesson.py + make_doppler_lesson.py để tránh copy-paste
~600 dòng boilerplate giữa các daily lessons.

Cung cấp:
- DOCX cell helpers: set_cell_bg, set_cell_border, style_header, style_first_col, add_bullets
- ANKI Pastel theme model + deck factory (v3 — Google Fonts Be Vietnam Pro)
- ANKI markdown→HTML converter (_md_to_html) + diacritics check (_check_json_diacritics)
- HTML base template (Tailwind + Mermaid + Chart.js)
- HTML common sections (footer, mermaid init script)

Usage in per-lesson script:
    from lesson_builder import (set_cell_bg, set_cell_border, style_header,
                                 style_first_col, add_bullets,
                                 build_pastel_model_and_deck, write_html)
"""
import html as html_lib
import re
from pathlib import Path

from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import genanki


# ============================================================
# DOCX HELPERS
# ============================================================
def set_cell_bg(cell, color_hex):
    """Set background color cho DOCX cell. color_hex = 'RRGGBB' (không có #)."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tc_pr.append(shd)


def set_cell_border(cell):
    """Add single-line black border cho 4 cạnh của cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:color'), '000000')
        tc_borders.append(border)
    tc_pr.append(tc_borders)


def style_header(cell):
    """Style cho header row: white text + bold + blue background + border."""
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    set_cell_bg(cell, '2D5F8C')
    set_cell_border(cell)


def style_first_col(cell):
    """Style cho cột đầu: bold + light blue background + border."""
    for para in cell.paragraphs:
        for run in para.runs:
            run.font.bold = True
    set_cell_bg(cell, 'E8F0F7')
    set_cell_border(cell)


def add_bullets(doc, items):
    """Add list of items dưới dạng bulleted list."""
    for item in items:
        doc.add_paragraph(item, style='List Bullet')


def add_numbered(doc, items):
    """Add list of items dưới dạng numbered list."""
    for item in items:
        doc.add_paragraph(item, style='List Number')


def fill_table(table, headers, rows, header_style=True, first_col_style=True):
    """Fill a pre-created DOCX table with headers + rows.

    Args:
        table: docx.table.Table object (đã create với rows=len(rows)+1, cols=len(headers))
        headers: list of str
        rows: list of tuples
        header_style: apply style_header to row 0
        first_col_style: apply style_first_col to column 0
    """
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        if header_style:
            style_header(cell)
    for r, row_data in enumerate(rows, start=1):
        for c, value in enumerate(row_data):
            cell = table.rows[r].cells[c]
            cell.text = str(value)
            set_cell_border(cell)
            if c == 0 and first_col_style:
                style_first_col(cell)


# ============================================================
# ANKI PASTEL THEME (v3 — Google Fonts + tiếng Việt tối ưu)
# ============================================================
PASTEL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&display=swap');

.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', 'Noto Sans', Arial, sans-serif;
  font-size: 17px;
  line-height: 1.8;
  text-align: left;
  color: #3a3a3a;
  background: linear-gradient(135deg, #fef9f3 0%, #f7e8e0 100%);
  padding: 24px;
  border-radius: 12px;
}
.card.nightMode {
  background: linear-gradient(135deg, #2d3142 0%, #4f5d75 100%);
  color: #f0e9e0;
}
#front, #back {
  background-color: rgba(255, 255, 255, 0.75);
  padding: 18px 22px;
  border-radius: 10px;
  border: 1px solid #e6d2c4;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  margin-bottom: 14px;
}
.card.nightMode #front, .card.nightMode #back {
  background-color: rgba(255, 255, 255, 0.08);
  border-color: rgba(255,255,255,0.15);
  color: #f0e9e0;
}
#front p, #back p {
  margin: 6px 0;
}
#front ul, #back ul, #front ol, #back ol {
  margin: 6px 0 6px 0;
  padding-left: 22px;
}
#front li, #back li {
  margin: 4px 0;
  line-height: 1.7;
}
#front b, #back b, #front strong, #back strong {
  color: #5c3a3a;
  font-weight: 600;
}
.card.nightMode #front b, .card.nightMode #back b,
.card.nightMode #front strong, .card.nightMode #back strong {
  color: #f0c5c5;
}
.cloze, .cloze-b {
  font-weight: 700;
  color: #c47a5a;
  background: rgba(228, 184, 152, 0.18);
  padding: 1px 4px;
  border-radius: 3px;
}
.card.nightMode .cloze, .card.nightMode .cloze-b {
  color: #f0c5c5;
  background: rgba(200, 164, 165, 0.25);
}
.tag {
  display: inline-block;
  background-color: #c8a4a5;
  color: #fff;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  margin-right: 6px;
}
hr#answer {
  margin: 12px 0;
  border: 0;
  border-top: 1px dashed #d4b8b8;
}
"""


def build_pastel_model_and_deck(model_id, model_name, deck_id, deck_name, deck_description):
    """Tạo genanki Model + Deck với Pastel theme.

    Returns: (model, deck)
    """
    model = genanki.Model(
        model_id,
        model_name,
        fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Tags'}],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div id="front">{{Question}}</div>',
                'afmt': '<div id="front">{{Question}}</div><hr id="answer"><div id="back">{{Answer}}<br><br><span class="tag">{{Tags}}</span></div>',
            }
        ],
        css=PASTEL_CSS
    )

    deck = genanki.Deck(deck_id, deck_name)
    deck.description = deck_description
    return model, deck


def _md_to_html(text):
    """Convert plain text with markdown-like formatting to safe HTML cho Anki.
    
    Xử lý: **bold** → <b>, newlines → <br>. Escapes HTML-sensitive chars.
    Input: plain text (có thể chứa **bold** markdown, \n line breaks).
    Output: HTML-safe string dùng được trong Anki fields.
    """
    # Step 1: Replace **text** with sentinel markers (trước khi escape)
    text = re.sub(r'\*\*([^*]+?)\*\*', r'__B__\1__Bb__', text)
    # Step 2: Escape HTML-sensitive chars (&, <, >, ")
    text = html_lib.escape(text)
    # Step 3: Restore sentinel → HTML tags
    text = text.replace('__B__', '<b>').replace('__Bb__', '</b>')
    # Step 4: Convert newlines to <br>
    text = text.replace('\n', '<br>')
    return text


def add_card_to_deck(deck, model, front, back, tags=''):
    """Add 1 card với markdown → HTML conversion + HTML escape."""
    front_html = _md_to_html(front)
    back_html = _md_to_html(back)
    note = genanki.Note(
        model=model,
        fields=[front_html, back_html, tags]
    )
    deck.add_note(note)


def add_cards_from_json(deck, model, cards_json_path, tags):
    """Load cards từ JSON file + add vào deck.

    Expected JSON format:
    {
      "deck_name": "...",
      "cards": [
        {"front": "...", "back": "..."},
        ...
      ]
    }
    """
    import json
    with open(cards_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for card in data['cards']:
        add_card_to_deck(deck, model, card['front'], card['back'], tags)
    return len(data['cards'])


def write_apkg(deck, output_path):
    """Write deck ra file .apkg."""
    genanki.Package(deck).write_to_file(str(output_path))


def build_pastel_cloze_model(model_id, model_name):
    """Tạo genanki Model cho thẻ Cloze với Pastel theme.
    
    Cú pháp: {{c1::text bị ẩn}}. Tất cả dùng c1, không dùng c2/c3.
    Extra field hiển thị dưới dạng tooltip bổ sung.
    """
    model = genanki.Model(
        model_id,
        model_name,
        fields=[{'name': 'Text'}, {'name': 'Extra'}],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '<div id="front">{{cloze:Text}}</div>',
                'afmt': '<div id="front">{{cloze:Text}}</div><hr id="answer"><div id="back">{{Extra}}</div>',
            }
        ],
        model_type=genanki.Model.CLOZE,
        css=PASTEL_CSS
    )
    return model


def _check_json_diacritics(data):
    """Kiểm tra nhanh dấu tiếng Việt trong cards JSON data (trước khi build).
    Returns (vn_diac, vn_total, ratio). In cảnh báo nếu ratio < 80%.
    """
    VN_DIAC = set(
        "àáảãạằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ"
        "ÀÁẢÃẠẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘỜỚỞỠỢÙÚỦŨỤỪỨỬỮỰỲÝỶỸỴ"
    )
    VN_SPECIAL = set("ăâđêôơưĂÂĐÊÔƠƯ")
    
    all_text = ""
    for card in data:
        for key in ('front', 'back', 'text', 'extra'):
            val = card.get(key, '')
            if val:
                # Strip HTML tags để chỉ đếm text
                clean = re.sub(r'<[^>]+>', ' ', val)
                all_text += ' ' + clean
    
    words = all_text.split()
    vn_diac = 0
    vn_total = 0
    for w in words:
        if len(w) < 2 or not any(c.isalpha() for c in w):
            continue
        has_diac = any(c in VN_DIAC for c in w)
        has_vn = any(c in VN_SPECIAL for c in w) or has_diac
        if has_vn:
            vn_total += 1
            if has_diac:
                vn_diac += 1
    
    ratio = vn_diac / vn_total if vn_total > 0 else 1.0
    return vn_diac, vn_total, ratio


def add_cards_from_json_v2(json_path, basic_model_id, cloze_model_id,
                           basic_model_name, cloze_model_name,
                           deck_id, deck_name, deck_description,
                           output_path):
    """Load cards từ JSON format V2 (basic + cloze) + build APKG.
    
    Expected JSON format (array):
    [
      {
        "type": "basic",
        "front": "Câu hỏi",
        "back": "<b>📖 Văn bản gốc:</b><br>...<br><br><b>🔍 Góc nhìn bổ sung:</b><br>...",
        "extra": ""
      },
      {
        "type": "cloze",
        "text": "Câu chứa {{c1::phần ẩn}}.",
        "extra": "Ghi chú bổ sung"
      }
    ]
    
    Rules (from flashcard.txt):
    - type là BẮT BUỘC: "basic" hoặc "cloze"
    - Thẻ basic PHẢI có: type, front, back
    - Thẻ cloze PHẢI có: type, text
    - Cú pháp cloze: chỉ dùng {{c1::...}}, KHÔNG dùng c2/c3
    - HTML cho định dạng: <b>, <i>, <br>
    - KHÔNG dùng LaTeX ($, $$, \\frac{}{})
    """
    import json
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # DIACRITICS CHECK — bắt buộc trước khi build
    vn_diac, vn_total, ratio = _check_json_diacritics(data)
    if vn_total > 10 and ratio < 0.80:
        print(f"  [APKG WARN] Diacritics ratio {ratio:.1%} (<80%) — có thể thiếu dấu tiếng Việt!")
        print(f"  [APKG WARN] {vn_diac}/{vn_total} từ tiếng Việt có dấu. Nguồn: {Path(json_path).name}")
    else:
        print(f"  [APKG OK] Diacritics: {ratio:.1%} ({vn_diac}/{vn_total} từ VN có dấu)")

    # Build models
    basic_model = build_pastel_model_and_deck(
        model_id=basic_model_id,
        model_name=basic_model_name,
        deck_id=deck_id,
        deck_name=deck_name,
        deck_description=deck_description,
    )[0]

    cloze_model = build_pastel_cloze_model(
        model_id=cloze_model_id,
        model_name=cloze_model_name
    )

    deck = genanki.Deck(deck_id, deck_name)
    deck.description = deck_description

    basic_count = 0
    cloze_count = 0

    for card in data:
        card_type = card.get('type', 'basic')
        if card_type == 'basic':
            front = card.get('front', '')
            back = card.get('back', '')
            extra = card.get('extra', '')
            # Escape HTML in front (plain text — may contain < for comparisons like HbA1c <6.0%)
            front = html_lib.escape(front)
            if extra:
                back = back + ('<br><br>' + html_lib.escape(extra) if back else html_lib.escape(extra))
            note = genanki.Note(
                model=basic_model,
                fields=[front, back, '']
            )
            deck.add_note(note)
            basic_count += 1
        elif card_type == 'cloze':
            text = card.get('text', '')
            extra = card.get('extra', '')
            extra = html_lib.escape(extra)
            note = genanki.Note(
                model=cloze_model,
                fields=[text, extra]
            )
            deck.add_note(note)
            cloze_count += 1

    write_apkg(deck, output_path)
    return basic_count, cloze_count


# ============================================================
# HTML TEMPLATE (Tailwind + Mermaid + Chart.js)
# ============================================================
HTML_BASE_HEADER = '''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  body {{ font-family: 'Inter', system-ui, sans-serif; background: linear-gradient(135deg, #fef9f3 0%, #f7e8e0 100%); }}
  .glass {{ background: rgba(255,255,255,0.7); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.3); }}
  .pastel-pink {{ background: #f4c2c2; }}
  .pastel-blue {{ background: #c5d5e0; }}
  .pastel-mint {{ background: #c5e0c9; }}
  .pastel-peach {{ background: #f7d1ba; }}
  .pastel-lavender {{ background: #d4c5e2; }}
  .mermaid {{ background: white; border-radius: 12px; padding: 16px; }}
  /* Chart.js canvas: giới hạn max-width để không bị kéo dãn khi render
     trên màn hình rộng. Kết hợp với height attr trên <canvas> để giữ tỉ lệ.
     Lý do: Chart.js mặc định maintainAspectRatio=false + responsive=true
     sẽ fill 100% container width -> bar/doughnut bị oval/méo khi container
     rộng hơn canvas internal pixel ratio. */
  canvas {{ display: block; max-width: 800px; margin: 0 auto; height: auto !important; }}
</style>
</head>
<body class="min-h-screen p-6">
'''

HTML_FOOTER_WITH_SCRIPT = '''
<script>
mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
{custom_charts}
</script>
</body>
</html>'''


def build_lesson_html(title, header_html, main_html, footer_text='', custom_charts=''):
    """Build complete HTML doc. Caller provides main_html (sections) + custom_charts script.

    Args:
        title: page title
        header_html: string cho <header>...</header>
        main_html: string cho <main>...</main> contents
        footer_text: hiển thị ở <footer>
        custom_charts: JS code cho Chart.js (đặt trong <script>)
    """
    footer_html = f'''
<footer class="text-center text-stone-500 text-sm py-6">
  <p>{footer_text}</p>
</footer>
''' if footer_text else ''

    # NOTE: HTML_BASE_HEADER and HTML_FOOTER_WITH_SCRIPT dùng {{ }} để escape JS braces
    return (
        HTML_BASE_HEADER.format(title=html_lib.escape(title))
        + header_html
        + '<main class="max-w-6xl mx-auto space-y-8">\n'
        + main_html
        + '\n</main>\n'
        + footer_html
        + HTML_FOOTER_WITH_SCRIPT.format(custom_charts=custom_charts)
    )


def write_html(html_content, output_path):
    """Write HTML content to file (UTF-8)."""
    Path(output_path).write_text(html_content, encoding='utf-8')
